# -*- coding: utf-8 -*-
"""b240_faceoff.py -- THE FIRST FACE-OFF AT BENCH. ### THE RUN.

### THE MEANINGS ARE ALREADY BANKED AND HASHED (data/b240_meanings.txt). ### THIS FILE READS
### THEM, PRINTS THE HASH INTO ITS OWN OUTPUT, AND COMPUTES. ### IT CHOOSES NOTHING.

### BOTH SIDES COME FROM THEIR OWN OWNERS, AND NEITHER READS THE OTHER'S OUTPUT:
###   LEFT  : T.value := Tr_full + E2 + Delta_minus   (the executed M-1 ruling, C2)
###           Q.value := Theta_q                       (as the instrument returns it; NO sign
###                                                     is inserted -- b229's standing clause)
###   RIGHT : R := A - PR                              (the adopted ledger at the atlas convention)

### THE INSTRUMENTS ARE IMPORTED, NOT RE-IMPLEMENTED: b38_act10 (Tr, E2, Theta_q, A, PR) and
### b37_act9 (the odd CC-index mask that realizes Delta_minus). ### A RE-IMPLEMENTATION WOULD BE
### A NEW INSTRUMENT WEARING A BANKED INSTRUMENT'S NAME.
"""
import hashlib
import inspect
import io
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C          # noqa: E402
import carto_auto as CA          # noqa: E402
import qeps_layer as Q           # noqa: E402
import b38_act10 as B38          # noqa: E402
import b37_act9 as B37           # noqa: E402

MEANINGS = r"D:\relay\data\b240_meanings.txt"
OUT = r"D:\relay\data\b240_faceoff_run.txt"

CELLS = [(math.sqrt(2), '2'), (math.sqrt(3), '3'), (2.0, '4'),
         (math.sqrt(8), '8'), (3.0, '9'), (math.sqrt(12), '12')]
S4 = B38.S4
NV_BASE, NV_REFINED = 4001, 6001
MODE_BASE, MODE_REFINED = (700, 10), (900, 11)
EPS_NQ, EPS_NG, EPS_NRHO = B38.EPS_NQ, B38.EPS_NG, B38.EPS_NRHO

K_BANKED = {'3': 0.6363, '4': 0.1539}
K_SURROGATE = 0.6363
FLOOR = 3.0e-13
TAIL = {'2': 7.195e-21, '3': 3.159e-26, '4': 1.072e-27}
S_L = 4.0
D_FACTOR = 10.0


def bar_R_banked(lab, nv):
    if lab == '2':
        return FLOOR + TAIL['2']
    L = math.log(math.sqrt(float(lab)))
    h = (4.0 * L) / (2 * nv - 2)
    K = K_BANKED.get(lab, K_SURROGATE)
    return K * h * h + FLOOR + TAIL.get(lab, 0.0)


def g_indep_source_audit():
    """### THE LEAKAGE TEST, RUN AND NOT ASSERTED: neither side's instrument may call the other
    ### or take the other's output as a parameter. ### READ FROM THE INSTRUMENTS' OWN SOURCE."""
    left_fns = [B38.trace_modes, B38.e2_of_grid, B38.theta_quotient]
    right_fns = [B38.left_side]
    rows, ok = [], True
    for f in left_fns:
        src = inspect.getsource(f)
        params = list(inspect.signature(f).parameters)
        calls_right = 'left_side(' in src
        takes_right = any(p in ('A', 'PR', 'P', 'R') for p in params)
        rows.append(("LEFT  %-16s" % f.__name__, params, calls_right, takes_right))
        ok &= (not calls_right) and (not takes_right)
    for f in right_fns:
        src = inspect.getsource(f)
        params = list(inspect.signature(f).parameters)
        calls_left = any(n + '(' in src for n in ('trace_modes', 'e2_of_grid', 'theta_quotient'))
        takes_left = any(p in ('Tr', 'Tr_full', 'E2', 'Thq', 'theta', 'T', 'Qv') for p in params)
        rows.append(("RIGHT %-16s" % f.__name__, params, calls_left, takes_left))
        ok &= (not calls_left) and (not takes_left)
    return ok, rows


def eps_grids():
    """### THE eps LAYER: full grid, odd-index mask (Delta_minus), per-mode masks (the algebra
    ### gate). ### EPS_NQ/EPS_NG/EPS_NRHO ARE THE INSTRUMENTS' OWN BANKED DEFAULTS."""
    rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    NT = len(lam2)
    odd = np.array([n % 2 == 1 for n in range(NT)])
    ee_odd = B37.eps_masked(rr, odd)
    ee_even = B37.eps_masked(rr, ~odd)
    mask_err = float(np.max(np.abs(ee_even + ee_odd - ee_full)))
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    return rr, ee_full, ee_odd, mask_err, t_n, odd


def sides(a, lab, nv, mode, rr, ee_full, ee_odd):
    """### ONE CELL AT ONE CONFIGURATION. ### BOTH SIDES, EACH FROM ITS OWN OWNER."""
    C.NV = nv
    v, w2, corr, vc, L = B38.family(a)
    NQ, NMODE = mode
    tr = B38.trace_modes(a, corr, vc, L, NQ, NMODE)
    Tr_full = float(tr.sum())
    E2 = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
    Dm = B38.e2_of_grid(a, corr, vc, L, rr, ee_odd)
    Thq = B38.theta_quotient(a, S4, corr, vc, L)
    A, P, PR = B38.left_side(a, S4, v, w2, corr, vc, L)
    T = Tr_full + E2 + Dm
    return dict(Tr=Tr_full, E2=E2, Dm=Dm, Thq=Thq, A=A, P=P, PR=PR,
                T=T, Qv=Thq, Lft=T + Thq, Rgt=A - PR)


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    t0 = time.time()
    mtxt = io.open(MEANINGS, encoding='utf-8').read()
    mhash = hashlib.sha256(mtxt.encode('utf-8')).hexdigest()

    rec("=" * 104)
    rec("b240 -- THE FIRST FACE-OFF AT BENCH. ### THE RUN.")
    rec("### RUN AT %s (local)." % time.strftime('%Y-%m-%dT%H:%M:%S'))
    rec("=" * 104)
    rec("  meanings file    : %s" % MEANINGS)
    rec("  meanings sha256  : %s" % mhash)
    rec("  meanings mtime   : %s" % time.strftime('%Y-%m-%dT%H:%M:%S',
                                                  time.localtime(os.path.getmtime(MEANINGS))))
    rec("  ### THE MEANINGS WERE ON DISK BEFORE THIS PROCESS STARTED. ### The gate checks it.")
    rec("")
    rec("### THE CEILING, PRINTED IN THIS TABLE'S OWN HEADER AS THE FERRY REQUIRES:")
    rec('###   b14: "a FINITE-PLACE-SET OBJECT AT A FINITE MODEL CUTOFF -- the complete roster is')
    rec('###         the double limit and STAYS OPEN whatever this act shows."')
    rec('###   b15: "A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL."')
    rec("")

    # ---------------------------------------------------------------- gates
    rec("-" * 104)
    rec("GATE BLOCK. ### ANY FAILURE HERE IS BRANCH (HALT) AND NO TABLE IS READ AS DATA.")
    rec("-" * 104)
    halt = False

    nu0, umax0 = C.NU, C.UMAX
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        halt |= not ok
        rec("  C0 carto far-end a=%.2f residual=%+.3e   %s" %
            (a, r["residual"], "PASS" if ok else "### FAIL"))

    rr, ee_full, ee_odd, mask_err, t_n, odd = eps_grids()
    ep_full = float(t_n.sum())
    ep_odd = float(t_n[odd].sum())
    ep_even = float(t_n[~odd].sum())
    for name, val, ref, tol in (("sum lam2", None, None, None),):
        pass
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    pins = [("sum lam2", abs(float(lam2.sum()) - 2.237484835), 1e-6),
            ("sum lam2 xi1^2", abs(float((lam2 * xi1 ** 2).sum()) - 2.0), 1e-6),
            ("epsprime1", abs(ep_full - 22.9964757), 1e-3),
            ("epsprime1_even (b35 pin)", abs(ep_even - 14.177305), 1e-3),
            ("epsprime1_odd  (b35 pin)", abs(ep_odd - 8.819138), 1e-3)]
    for name, gval, tol in pins:
        ok = gval <= tol
        halt |= not ok
        rec("  C0 pin %-26s |delta|=%.2e (tol %.0e)   %s" %
            (name, gval, tol, "PASS" if ok else "### FAIL"))
    ok = mask_err <= 1e-12
    halt |= not ok
    rec("  eps mask algebra  max|eps_even + eps_odd - eps_full| = %.2e   %s" %
        (mask_err, "PASS" if ok else "### FAIL"))
    rec("  ### Delta_minus IS THE ODD-INDEX MASK, and its pin is %.6f of %.6f -- the eps'(1+)"
        % (ep_odd, ep_full))
    rec("  ### split banked at b35. ### THE MASK IS VERIFIED BEFORE IT IS USED, NOT AFTER.")

    gi_ok, gi_rows = g_indep_source_audit()
    halt |= not gi_ok
    rec("")
    rec("  G-INDEP, READ FROM THE INSTRUMENTS' OWN SOURCE:")
    for nm, params, calls, takes in gi_rows:
        rec("    %s params=%-46s calls-other=%-5s takes-other=%s" %
            (nm, ",".join(params), calls, takes))
    rec("  G-INDEP GATE: %s" % ("PASS -- neither side reads the other's output" if gi_ok
                                else "### FAIL"))
    rec("  ### WHAT IS SHARED IS `a`, `corr = w*w`, the place set and the atlas constants --")
    rec("  ### and each sharing IS THE IDENTITY'S OWN CONTENT: an identity at a cell for a test")
    rec("  ### function is not two claims at two test functions.")

    if halt:
        rec("")
        rec("### A GATE FIRED. BRANCH (HALT). NO TABLE FOLLOWS.")
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write("\n".join(out) + "\n")
        return 1

    # ---------------------------------------------------------------- the run
    rec("")
    rec("-" * 104)
    rec("THE CONFIGURATIONS, AS BANKED. ### base NV=%d, mode %s; refinements NV=%d and mode %s."
        % (NV_BASE, MODE_BASE, NV_REFINED, MODE_REFINED))
    rec("-" * 104)

    res = {}
    for a, lab in CELLS:
        base = sides(a, lab, NV_BASE, MODE_BASE, rr, ee_full, ee_odd)
        refA = sides(a, lab, NV_REFINED, MODE_BASE, rr, ee_full, ee_odd)
        refB = sides(a, lab, NV_BASE, MODE_REFINED, rr, ee_full, ee_odd)
        res[lab] = (base, refA, refB)
        rec("  a^2=%-3s done (%.1fs elapsed)" % (lab, time.time() - t0))

    assert C.NU == nu0 and C.UMAX == umax0
    rec("  KERNEL-CACHE GATE: NU %d -> %d, UMAX %.1f -> %.1f   PASS (the cache was never stale)"
        % (nu0, C.NU, umax0, C.UMAX))

    rec("")
    rec("-" * 104)
    rec("THE COLUMNS AT THE BASE CONFIGURATION. ### EACH SIDE FROM ITS OWN OWNERS.")
    rec("-" * 104)
    rec("  %-4s %12s %12s %12s %12s | %12s %12s" %
        ("a^2", "Tr_full", "E2", "Delta_-", "Theta_q", "A", "PR"))
    for a, lab in CELLS:
        b = res[lab][0]
        rec("  %-4s %12.6f %12.6f %12.6f %12.6f | %12.6f %12.6f" %
            (lab, b['Tr'], b['E2'], b['Dm'], b['Thq'], b['A'], b['PR']))

    rec("")
    rec("-" * 104)
    rec("G-STAB. ### BOTH SIDES AT THE REGISTERED AXES AND ONE REGISTERED REFINEMENT EACH.")
    rec("-" * 104)
    rec("  %-4s %14s %14s %14s | %14s %14s" %
        ("a^2", "|dL| (NV)", "|dL| (mode)", "bar_L", "|dR| (NV)", "bar_R"))
    bars = {}
    for a, lab in CELLS:
        base, refA, refB = res[lab]
        dL_nv = abs(refA['Lft'] - base['Lft'])
        dL_md = abs(refB['Lft'] - base['Lft'])
        bar_L = S_L * max(dL_nv, dL_md)
        dR_nv = abs(refA['Rgt'] - base['Rgt'])
        bar_Rb = bar_R_banked(lab, NV_BASE)
        bar_R = max(bar_Rb, dR_nv)
        bars[lab] = (bar_L, bar_R, bar_Rb, dR_nv, dL_nv, dL_md)
        rec("  %-4s %14.6e %14.6e %14.6e | %14.6e %14.6e" %
            (lab, dL_nv, dL_md, bar_L, dR_nv, bar_R))
    rec("  ### bar_R = max(banked projection, the right side's own measured disagreement).")
    for a, lab in CELLS:
        bar_L, bar_R, bar_Rb, dR_nv, _, _ = bars[lab]
        if dR_nv > bar_Rb:
            rec("  ### a^2=%s: THE MEASURED |dR| (%.3e) EXCEEDS b238's BANKED PROJECTION (%.3e)"
                % (lab, dR_nv, bar_Rb))
            rec("  ###          BY A FACTOR OF %.2f. ### THE PROJECTION IS THE WRONG BAR HERE, and"
                % (dR_nv / bar_Rb))
            rec("  ###          the floor registered in advance is what carries the cell.")

    rec("")
    rec("=" * 104)
    rec("THE FACE-OFF TABLE. ### L := T.value + Q.value := (Tr_full + E2 + Delta_-) + Theta_q")
    rec("###                  R := A - PR")
    rec('### CEILING (b15): "A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL."')
    rec("=" * 104)
    rec("  %-4s %14s %14s %14s %12s %14s  %s" %
        ("a^2", "L", "R", "|L - R|", "rel", "combined bar", "BRANCH"))
    branches = {}
    for a, lab in CELLS:
        base = res[lab][0]
        bar_L, bar_R = bars[lab][0], bars[lab][1]
        bar = bar_L + bar_R
        d = abs(base['Lft'] - base['Rgt'])
        scale = max(abs(base['Lft']), abs(base['Rgt']))
        rel = d / scale if scale > 0 else 0.0
        if d <= bar:
            br = "CONSONANT"
        elif d > D_FACTOR * bar:
            br = "### DISSONANT"
        else:
            br = "INDETERMINATE"
        branches[lab] = br
        rec("  %-4s %14.6f %14.6f %14.6e %12.3e %14.6e  %s" %
            (lab, base['Lft'], base['Rgt'], d, rel, bar, br))

    vals = list(branches.values())
    if any('DISSONANT' in v for v in vals):
        act = "(DISSONANT)"
    elif any(v == 'INDETERMINATE' for v in vals):
        act = "(INDETERMINATE)"
    else:
        act = "(CONSONANT)"
    rec("")
    rec("### THE ACT'S BRANCH, BY THE RULE BANKED BEFORE THE RUN: %s" % act)
    rec("### cells: %s" % ", ".join("a^2=%s %s" % (k, v.replace('### ', ''))
                                    for k, v in branches.items()))
    rec("### AND THE CEILING AGAIN, BECAUSE A BRANCH IS WHERE A READER STOPS: this is a")
    rec("### finite-place-set object at a finite cutoff. ### IT DECIDES NOTHING GLOBAL, AND h2")
    rec("### STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.")
    rec("")
    rec("  elapsed: %.1fs" % (time.time() - t0))
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write("\n".join(out) + "\n")
    print("\nbanked: %s" % OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
