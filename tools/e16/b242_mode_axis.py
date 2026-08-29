# -*- coding: utf-8 -*-
"""b242 COMPONENT 1 -- THE LEFT MODE AXIS, MEASURED. ### NO ENVELOPE IS DERIVED HERE.

### WHAT THIS TOOL DOES THAT b240 COULD NOT: ### b240's ONE STEP moved NQ AND NMODE TOGETHER
### (b38's TRIPLE (700,10) -> (900,11)), so what it measured was quadrature AND truncation
### MIXED. ### THIS TOOL MOVES THEM SEPARATELY:
###   AXIS 1 -- PURE TRUNCATION : NMODE = 1..11, NQ HELD at 700.
###   AXIS 2 -- PURE QUADRATURE : NQ in {500,700,900,1100,1300}, NMODE HELD at 10.
###
### ### SCOPE WALL: ### THE LEFT SIDE ONLY. ### `A` enters ONLY as the constant inside
### ### `resid47 := Tr_full - A - E2N` and is never compared to anything. ### `PR`, `Theta_q`
### ### and every right-side object are ABSENT from this file.
###
### ### THIS TOOL DERIVES NO ENVELOPE AND CERTIFIES NOTHING. ### The envelope is Component 2
### ### and is banked and hashed BEFORE the certifying run, per the order-of-operations law.
"""
import io
import json
import math
import os
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import b38_act10 as B38                 # noqa: E402
import b37_act9 as B37                  # noqa: E402
import qeps_layer as Q                  # noqa: E402

BANK = r"D:\relay\data\b242_mode_axis_run.txt"
CACHE = r"D:\relay\data\b242_axis_points.json"

NQ_BASE = 700
NMODE_CAP = 11                          # ### Lemma F.1's CERTIFIED ceiling. NOT a choice.
NQ_AXIS = [500, 700, 900, 1100, 1300]


def load_cache():
    """### RESUMABILITY (hazard H-d): banked axis points are re-READ, never remembered."""
    if os.path.exists(CACHE):
        try:
            return json.load(io.open(CACHE, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(c):
    io.open(CACHE, "w", encoding="utf-8").write(json.dumps(c, indent=1, sort_keys=True))


def eps_grids():
    rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
    ee_modes = B38.per_mode_eps_grids(rr)
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    NT = len(lam2)
    odd = np.array([n % 2 == 1 for n in range(NT)])
    ee_odd = B37.eps_masked(rr, odd)
    return rr, ee_full, ee_modes, ee_odd


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    cache = load_cache()

    rec("=" * 104)
    rec("b242 COMPONENT 1 -- THE LEFT MODE AXIS, MEASURED. ### NO ENVELOPE DERIVED HERE.")
    rec("### REGISTRATION BANKED FIRST: data/b242_registration_2026-08-29.txt")
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("### SCOPE: LEFT SIDE ONLY. ### No right-side object is computed and no residual against")
    rec("### the right side is formed anywhere in this run.")
    rec("")

    # ------------------------------------------------------------------ C0
    rec("-" * 104)
    rec("C0 -- THE GATES, BEFORE ANY TABLE.")
    rec("-" * 104)
    void = False
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ_BASE)
    rec("  NTERM (qeps_layer:41, Lemma F.1)  : %d" % Q.NTERM)
    rec("  len(lam2) / xi.shape[1] live      : %d / %d" % (len(lam2), xi.shape[1]))
    g1 = abs(float(lam2.sum()) - 2.237484835)
    g2 = abs(float((lam2 * xi1 ** 2).sum()) - 2.0)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    g3 = abs(float(t_n.sum()) - 22.9964757)
    for nm, gv, tol in (("sum lam2", g1, 1e-6), ("sum lam2 xi1^2", g2, 1e-6),
                        ("epsprime1", g3, 1e-3)):
        ok = gv <= tol
        void |= not ok
        rec("  pin %-18s |delta|=%.2e (tol %.0e) %s" % (nm, gv, tol, "PASS" if ok else "FAIL"))

    # ### THE PARTIAL-SUM INVARIANCE GATE. ### The whole measurement rests on the claim that
    # ### `tr[n]` does not depend on NMODE (NMODE only bounds the loop), so that ONE call at
    # ### NMODE=11 yields every partial sum by cumsum. ### THAT CLAIM IS CHECKED, NOT ASSUMED.
    v, w2, corr, vc, L = B38.family(B38.CELLS[2][0])
    tr_a = B38.trace_modes(B38.CELLS[2][0], corr, vc, L, NQ_BASE, 5)
    tr_b = B38.trace_modes(B38.CELLS[2][0], corr, vc, L, NQ_BASE, NMODE_CAP)
    inv = float(np.max(np.abs(tr_a - tr_b[:5])))
    ok = inv == 0.0
    void |= not ok
    rec("  partial-sum invariance  max|tr(NMODE=5) - tr(NMODE=11)[:5]| = %.2e  %s"
        % (inv, "PASS" if ok else "FAIL"))
    rec("  ### THAT GATE IS WHAT LICENSES ONE CALL PER (cell, NQ) INSTEAD OF ELEVEN.")
    if void:
        rec("\n  C0 FAILED -- VOID. No table follows.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return
    rec("")

    # ------------------------------------------------- THE POSITIVE CONTROLS
    rec("-" * 104)
    rec("THE POSITIVE CONTROLS -- MODE SERIES ON THIS SAME LAYER WITH KNOWN LIMITS.")
    rec("### IF THE METHOD CANNOT SEE A CONVERGENCE THAT IS THERE, ITS VERDICT ON A SERIES THAT")
    rec("### MAY NOT CONVERGE IS WORTH NOTHING.")
    rec("-" * 104)
    c1 = np.cumsum(lam2 * xi1 ** 2)
    c2 = np.cumsum(t_n)
    rec("  CONTROL A: sum_n lam2_n xi_n(1)^2 -> 2.0 EXACTLY (b38's own C0 gate)")
    rec("  %-5s %18s %16s %14s" % ("N", "partial", "|limit - partial|", "ratio"))
    prev = None
    for n in range(1, len(c1) + 1):
        d = abs(2.0 - c1[n - 1])
        r = ("%.4f" % (d / prev)) if (prev not in (None, 0.0)) else "--"
        rec("  %-5d %18.12f %16.3e %14s" % (n, c1[n - 1], d, r))
        prev = d if d > 0 else prev
    rec("")
    rec("  CONTROL B: sum_n t(n) -> 22.9964757 (the eps'(1+) pin, BANKED not exact)")
    rec("  %-5s %18s %16s %14s" % ("N", "partial", "|pin - partial|", "ratio"))
    prev = None
    for n in range(1, len(c2) + 1):
        d = abs(22.9964757 - c2[n - 1])
        r = ("%.4f" % (d / prev)) if (prev not in (None, 0.0)) else "--"
        rec("  %-5d %18.9f %16.3e %14s" % (n, c2[n - 1], d, r))
        prev = d if d > 0 else prev
    rec("")

    # ------------------------------------------------------- THE EPS GRIDS
    rr, ee_full, ee_modes, ee_odd = eps_grids()
    mode_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    rec("  ### b38's OWN MASK GATE, RE-RUN: max|sum_n eps_n - eps_full| = %.2e  %s"
        % (mode_alg, "PASS" if mode_alg <= 1e-10 else "FAIL"))
    if mode_alg > 1e-10:
        rec("  MASK GATE FAILED -- VOID.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return
    rec("")

    # ============================================= AXIS 1 -- PURE TRUNCATION
    rec("=" * 104)
    rec("AXIS 1 -- ### PURE TRUNCATION. ### NMODE = 1..%d, NQ HELD AT %d." % (NMODE_CAP, NQ_BASE))
    rec("### THIS IS THE AXIS b240 COULD NOT ISOLATE.")
    rec("=" * 104)

    per_cell = {}
    for a, alab in B38.CELLS:
        key = "trunc|%s" % alab
        if key in cache:
            d = cache[key]
        else:
            v, w2, corr, vc, L = B38.family(a)
            A = B38.left_side(a, B38.S4, v, w2, corr, vc, L)[0]
            tr = B38.trace_modes(a, corr, vc, L, NQ_BASE, NMODE_CAP)
            E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n])
                            for n in range(len(tr))])
            E2full = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
            Dm = B38.e2_of_grid(a, corr, vc, L, rr, ee_odd)
            d = dict(A=A, tr=list(map(float, tr)), E2n=list(map(float, E2n)),
                     E2full=float(E2full), Dm=float(Dm))
            cache[key] = d
            save_cache(cache)
        per_cell[alab] = d

        tr = np.array(d["tr"])
        E2n = np.array(d["E2n"])
        A = d["A"]
        Trc = np.cumsum(tr)
        E2c = np.cumsum(E2n)
        rec("")
        rec("  a^2 = %-4s   A = %+.9f   Delta_- = %+.9f   E2full = %.9f"
            % (alab, A, d["Dm"], d["E2full"]))
        rec("  %-4s %14s %14s %14s %14s %13s"
            % ("NMODE", "tr[n]", "Tr_full", "E2N", "resid47", "|d resid47|"))
        prevr = None
        for n in range(NMODE_CAP):
            resid = Trc[n] - A - E2c[n]
            dr = ("%.4e" % abs(resid - prevr)) if prevr is not None else "--"
            rec("  %-4d %+14.9f %+14.9f %14.9f %+14.9f %13s"
                % (n + 1, tr[n], Trc[n], E2c[n], resid, dr))
            prevr = resid
        neg = [n for n in range(NMODE_CAP) if tr[n] < 0]
        rec("    ### mode terms negative at n = %s   ### (sec 25(a) records them >= 0)"
            % (neg if neg else "NONE"))
        rec("    ### THE WITHHELD ELEVENTH, BOTH FACES:")
        rec("    ###   eps  face: E2n[10] = %+.6e   ### (b241 measured 8.993e-15)" % E2n[10])
        rec("    ###   TRACE face: tr[10] = %+.9f   ### NOT COMPUTED AT THE BASE AXIS NMODE=10"
            % tr[10])
        rec("    ###   resid47(10 modes) = %+.9f   resid47(11 modes) = %+.9f   delta = %+.9f"
            % (Trc[9] - A - E2c[9], Trc[10] - A - E2c[10],
               (Trc[10] - A - E2c[10]) - (Trc[9] - A - E2c[9])))

    # ============================================ AXIS 2 -- PURE QUADRATURE
    rec("")
    rec("=" * 104)
    rec("AXIS 2 -- ### PURE QUADRATURE. ### NQ in %s, NMODE HELD AT 10." % NQ_AXIS)
    rec("### NOTE, SAID RATHER THAN LEFT TO BE INFERRED: this sweeps the TRACE's own NQ.")
    rec("### The eps layer is built at b38's EPS_NQ = %d and does NOT move here, so `E2N` and"
        % B38.EPS_NQ)
    rec("### `Delta_-` are CONSTANT down each column below -- by construction, not by luck.")
    rec("=" * 104)
    rec("  %-4s %-6s %16s %16s %14s" % ("a^2", "NQ", "Tr_full(10)", "resid47(10)", "|d Tr|"))
    for a, alab in B38.CELLS:
        prevT = None
        for nq in NQ_AXIS:
            key = "quad|%s|%d" % (alab, nq)
            if key in cache:
                d = cache[key]
            else:
                v, w2, corr, vc, L = B38.family(a)
                A = B38.left_side(a, B38.S4, v, w2, corr, vc, L)[0]
                tr = B38.trace_modes(a, corr, vc, L, nq, 10)
                d = dict(A=A, Tr=float(np.sum(tr)))
                cache[key] = d
                save_cache(cache)
            E2c10 = float(np.sum(np.array(per_cell[alab]["E2n"])[:10]))
            resid = d["Tr"] - d["A"] - E2c10
            dT = ("%.4e" % abs(d["Tr"] - prevT)) if prevT is not None else "--"
            rec("  %-4s %-6d %16.9f %16.9f %14s" % (alab, nq, d["Tr"], resid, dT))
            prevT = d["Tr"]
        rec("")

    rec("=" * 104)
    rec("### WHAT THIS RUN DID NOT DO: it derived NO envelope, certified NOTHING, touched no")
    rec("### right-side object, and moved no grade. ### THE ENVELOPE IS COMPONENT 2 AND IS")
    rec("### BANKED AND HASHED BEFORE ANY CERTIFYING RUN. ### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
