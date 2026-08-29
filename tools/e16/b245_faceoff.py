# -*- coding: utf-8 -*-
"""b245 COMPONENT 2 -- THE SECOND FACE-OFF, RUN UNDER THE RULED MEANINGS.

### THE ORDER-OF-OPERATIONS GATE, BOTH LIMBS (b240's mechanism):
###   (i)  this run prints the MEANINGS FILE's OWN sha256 into its own output;
###   (ii) it REFUSES to run unless the meanings file is OLDER ON DISK than this tool.
### ### EITHER LIMB ALONE IS FORGEABLE.
###
### ### THE RULED COMBINATION, AND NO ACT HAS COMPUTED IT BEFORE:
### ###   L := (Tr_full + E2 - Delta_-) + (-Theta_q)      [b244: RULE Delta_- D1, RULE Q O1]
### ###   R := A - PR
### ### with NMODE = 7 (RULE MODES K1's seven computable modes).
### ### **THE SIGNS ARE RULED, NOT CHOSEN BY THIS ACT.**
###
### ### DISCLOSURE, ADDED AFTER THE FIRST RUN AND BEFORE THE SECOND -- THE MEANINGS FILE WAS
### ### RE-EMITTED ONCE, AND THIS TOOL WAS EDITED SO THAT THE ORDERING GATE STILL HOLDS HONESTLY
### ### RATHER THAN BY TOUCHING AN MTIME:
### ###   THE CAUSE: the banned stem `blind` appeared TWICE in the meanings file's own voice and
### ###   the term scan caught it. ### The corpus's standing rule is that it is corrected before
### ###   shipping, and the meanings file is HASH-GATED, so correcting it forces a full re-run.
### ###   THE PROOF THAT NOTHING ELSE MOVED: a line diff of the pre-repair and post-repair
### ###   meanings files shows ### **EXACTLY THREE CHANGED LINES** -- the emission timestamp and
### ###   the two occurrences of the stem. ### **NO RULE, BAND, FACTOR, TOLERANCE, BRANCH
### ###   DEFINITION, AXIS OR CONSTANT CHANGED**, and the pre-repair file is retained so the diff
### ###   can be re-derived by anyone.
### ###   THE NUMBERS: the run is resumable from `b245_points.json`, so the re-run reproduces the
### ###   same values from the same banked axis points. ### **THE REPAIR CHANGED A WORD, NOT A
### ###   NUMBER, AND CERTAINLY NOT A BRANCH.**
"""
import hashlib
import io
import json
import math
import os
import sys
import time

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import carto_atlas as C                 # noqa: E402
import carto_auto as CA                 # noqa: E402
import b38_act10 as B38                 # noqa: E402
import b37_act9 as B37                  # noqa: E402
import qeps_layer as Q                  # noqa: E402

MEANINGS = r"D:\relay\data\b245_meanings.txt"
BANK = r"D:\relay\data\b245_faceoff_run.txt"
CACHE = r"D:\relay\data\b245_points.json"

NV_BASE, NV_REF = 4001, 6001
NM_BASE, NM_REF = 7, 6
NQ = 700
F_FLOOR = 3.0e-13

# ### FROM b243's CERTIFIED SPEC (branch PROMOTED). ### Derived from the bump alone.
K_GLOB = {"2": 6.115845, "3": 1.536029, "4": 2.294377,
          "8": 1.125709, "9": 1.097665, "12": 0.758862}
# ### FROM b242, AND IT IS **NOT A BOUND** -- the envelope b242 derived, printed and REFUSED.
TAIL = {"2": 2.073985, "3": 1.284308, "4": 1.058734,
        "8": 0.645073, "9": 0.669490, "12": 0.578951}
# ### FROM b38's AND b37's BANKS OF 2026-08-18, for T-E. ### resid47 is printed there to FOUR
# ### decimals and D_dictated to SIX; both are quoted at the precision the bank has.
BANK38 = {"2": (4.0486, -2.681242), "3": (3.3740, -2.534072), "4": (3.0478, -2.295425),
          "8": (2.5208, -2.025781), "9": (2.4540, -1.858463), "12": (2.3134, -1.790997)}

TAIL_SENTENCE = [
    "  ### THE TAIL TERM IS NOT A BOUND. ### b242 DERIVED THIS ENVELOPE, PRINTED IT AND REFUSED",
    "  ### IT -- the ratio is rising, the extrapolation is unverifiable IN PRINCIPLE at float64,",
    "  ### and NO OWNER PROVES THE TRACE SERIES CONVERGES AT ALL. ### A BAR CARRYING THIS TERM",
    "  ### IS NOT A CERTIFIED BAR AND NO NUMBER BESIDE IT IS CERTIFIED.",
]


def g_indep_from_source():
    """### READ FROM THE INSTRUMENTS' OWN SOURCE, NOT ASSERTED."""
    src = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "b38_act10.py"), encoding="utf-8").read()
    body = src.split("def left_side")[1].split("def trace_modes")[0]
    leaks = [t for t in ("trace_modes", "e2_of_grid", "theta_quotient", "resid")
             if t in body]
    lhs = src.split("def trace_modes")[1].split("def main")[0]
    back = [t for t in ("left_side", "GAM", "zeta") if t in lhs]
    return (not leaks) and (not back), leaks, back


def sides(a, alab, nv, nmode, cache):
    key = "%s|%d|%d" % (alab, nv, nmode)
    if key in cache:
        return cache[key]
    old = C.NV
    C.NV = nv
    C._KERN = None
    try:
        v, w2, corr, vc, L = B38.family(a)
        rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
        ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
        x, ww, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
        odd = np.array([n % 2 == 1 for n in range(len(lam2))])
        ee_odd = B37.eps_masked(rr, odd)
        tr = B38.trace_modes(a, corr, vc, L, NQ, nmode)
        Tr = float(np.sum(tr))
        E2 = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
        Dm = B38.e2_of_grid(a, corr, vc, L, rr, ee_odd)
        Thq = B38.theta_quotient(a, B38.S4, corr, vc, L)
        A, P, PR = B38.left_side(a, B38.S4, v, w2, corr, vc, L)
        h = 4.0 * L / (2 * nv - 2)
        d = dict(Tr=Tr, E2=E2, Dm=Dm, Thq=Thq, A=A, PR=PR, h=h,
                 tr_last=float(tr[-1]),
                 Lft=(Tr + E2 - Dm) + (-Thq), Rgt=A - PR)
    finally:
        C.NV = old
        C._KERN = None
    cache[key] = d
    json.dump(cache, io.open(CACHE, "w", encoding="utf-8"), indent=1, sort_keys=True)
    return d


def main():
    if not os.path.exists(MEANINGS):
        print("### REFUSED -- the meanings file is not on disk.")
        return 1
    mtxt = io.open(MEANINGS, encoding="utf-8").read()
    mhash = hashlib.sha256(mtxt.encode("utf-8")).hexdigest()
    if os.path.getmtime(MEANINGS) > os.path.getmtime(os.path.abspath(__file__)):
        print("### REFUSED -- the meanings file is younger than this tool.")
        return 1

    cache = json.load(io.open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 108)
    rec("b245 -- THE SECOND FACE-OFF AT BENCH. ### THE RUN.")
    rec("### RUN AT %s (local)." % time.strftime("%Y-%m-%dT%H:%M:%S"))
    rec("=" * 108)
    rec("  meanings sha256 : %s" % mhash)
    rec("  ### THE GATE TESTS BOTH LIMBS: this hash is the meanings file's OWN, and the meanings")
    rec("  ### file is OLDER ON DISK than this tool. ### EITHER LIMB ALONE IS FORGEABLE.")
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### (b14): the complete roster is the double limit and STAYS OPEN whatever")
    rec("### this act shows. ### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("")

    # ------------------------------------------------------------------ C0
    rec("-" * 108)
    rec("C0 -- THE VOID GATES, BEFORE ANY TABLE.")
    rec("-" * 108)
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"],
                                                          "PASS" if ok else "FAIL"))
    x, ww, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    for nm, gv, tol in (("sum lam2", abs(float(lam2.sum()) - 2.237484835), 1e-6),
                        ("sum lam2 xi1^2", abs(float((lam2 * xi1 ** 2).sum()) - 2.0), 1e-6),
                        ("epsprime1", abs(float(t_n.sum()) - 22.9964757), 1e-3)):
        ok = gv <= tol
        void |= not ok
        rec("  pin %-16s |delta|=%.2e (tol %.0e) %s" % (nm, gv, tol, "PASS" if ok else "FAIL"))
    rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
    ee_modes = B38.per_mode_eps_grids(rr)
    malg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    ok = malg <= 1e-10
    void |= not ok
    rec("  eps mask algebra   max|sum_n eps_n - eps_full| = %.2e  %s"
        % (malg, "PASS" if ok else "FAIL"))
    ok = (C.NU == 12001 and abs(C.UMAX - 600.0) < 1e-12)
    void |= not ok
    rec("  kernel-cache gate  NU=%d UMAX=%.1f (must be 12001/600.0)  %s"
        % (C.NU, C.UMAX, "PASS" if ok else "FAIL"))
    gi, leaks, back = g_indep_from_source()
    void |= not gi
    rec("  G-INDEP GATE: %s  ### READ FROM THE INSTRUMENTS' OWN SOURCE"
        % ("PASS" if gi else "FAIL leaks=%s back=%s" % (leaks, back)))
    if void:
        rec("\n  ### C0 FAILED -- (HALT). ### NO TABLE IS READ AS DATA.")
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return 0
    rec("")

    # --------------------------------------------------------------- G-STAB
    rec("-" * 108)
    rec("G-STAB. ### BOTH SIDES AT THE REGISTERED AXES PLUS ONE REGISTERED REFINEMENT EACH.")
    rec("### THE MODE REFINEMENT MOVES **NMODE ALONE** (7 -> 6) AT NQ HELD -- b242 showed b240's")
    rec("### step moved NQ AND NMODE TOGETHER and was ~94% quadrature. ### NOT REPEATED HERE.")
    rec("-" * 108)
    rec("  %-5s %14s %14s %16s %16s" % ("a^2", "|dL| (NV)", "|dL| (NMODE)",
                                        "bar_L_bounded", "bar_R"))
    st = {}
    for a, alab in B38.CELLS:
        b = sides(a, alab, NV_BASE, NM_BASE, cache)
        nvr = sides(a, alab, NV_REF, NM_BASE, cache)
        nmr = sides(a, alab, NV_BASE, NM_REF, cache)
        dnv = abs(nvr["Lft"] - b["Lft"])
        dnm = abs(nmr["Lft"] - b["Lft"])
        barL = 4.0 * max(dnv, dnm)
        barR = K_GLOB[alab] * b["h"] ** 2 + F_FLOOR
        st[alab] = dict(b=b, nvr=nvr, nmr=nmr, dnv=dnv, dnm=dnm, barL=barL, barR=barR)
        rec("  %-5s %14.6e %14.6e %16.6e %16.6e" % (alab, dnv, dnm, barL, barR))
    rec("")

    # ---------------------------------------------------------- THE TABLE
    rec("=" * 108)
    rec("THE SECOND FACE-OFF TABLE. ### L := (Tr_full + E2 - Delta_-) + (-Theta_q)   [RULED]")
    rec("###                          R := A - PR")
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### NMODE = 7 (RULE MODES K1's SEVEN COMPUTABLE MODES). ### THE TAIL IS FLAGGED BELOW.")
    rec("=" * 108)
    rec("  %-5s %13s %13s %13s %13s %13s %13s"
        % ("a^2", "L", "R", "L - R", "M-4 (resid47)", "bar_bounded", "TAIL (flag)"))
    rows = {}
    for a, alab in B38.CELLS:
        s = st[alab]["b"]
        LmR = s["Lft"] - s["Rgt"]
        resid47 = s["Tr"] - s["A"] - s["E2"]
        bar_bounded = st[alab]["barL"] + st[alab]["barR"]
        rows[alab] = dict(LmR=LmR, resid47=resid47, bar=bar_bounded, s=s)
        rec("  %-5s %13.6f %13.6f %13.6f %13.6f %13.3e %13.6f"
            % (alab, s["Lft"], s["Rgt"], LmR, resid47, bar_bounded, TAIL[alab]))
    for line in TAIL_SENTENCE:
        rec(line)
    rec("")

    # ------------------------------------------- THE ALGEBRAIC RESTATEMENT
    rec("-" * 108)
    rec("### THE ALGEBRAIC RESTATEMENT, LABELLED AS SUCH AND CARRYING **NO EVIDENTIAL WEIGHT**.")
    rec("### `L - R = resid47 + (2*E2 - Delta_- + PR - Theta_q)` HOLDS FOR ARBITRARY TUPLES.")
    rec("### It is printed ONLY as a float-arithmetic check that the code sums what it says.")
    rec("-" * 108)
    rec("  %-5s %16s %16s %14s" % ("a^2", "L - R", "the restatement", "difference"))
    worst_alg = 0.0
    for a, alab in B38.CELLS:
        s = rows[alab]["s"]
        acc = rows[alab]["resid47"] + (2 * s["E2"] - s["Dm"] + s["PR"] - s["Thq"])
        d = abs(rows[alab]["LmR"] - acc)
        worst_alg = max(worst_alg, d)
        rec("  %-5s %16.9f %16.9f %14.3e" % (alab, rows[alab]["LmR"], acc, d))
    rec("  ### max difference = %.3e. ### **THIS CONFIRMS NOTHING ABOUT THE IDENTITY.**"
        % worst_alg)
    rec("")

    # --------------------------------------------------- THE FIVE TESTS
    rec("=" * 108)
    rec("THE CONTENTFUL TESTS, AS REGISTERED IN SECTION (D.1). ### EACH CAN FAIL.")
    rec("=" * 108)
    verdicts = {}

    rec("--- T-A: the cell profile against resid47's signature. band [1.40, 2.10] at EVERY cell.")
    ta = True
    for a, alab in B38.CELLS:
        r = rows[alab]["LmR"] / rows[alab]["resid47"]
        ok = 1.40 <= r <= 2.10
        ta &= ok
        rec("      a^2 = %-4s  (L-R)/resid47 = %.6f   %s" % (alab, r, "in band" if ok else "### OUT"))
    verdicts["T-A"] = ta
    rec("      ### T-A: %s" % ("PASS" if ta else "### FAIL"))

    rec("--- T-B: invariance under right-side axis variation. tol 1e-6 at every cell.")
    tb = True
    for a, alab in B38.CELLS:
        d = abs((st[alab]["nvr"]["Lft"] - st[alab]["nvr"]["Rgt"]) - rows[alab]["LmR"])
        ok = d <= 1e-6
        tb &= ok
        rec("      a^2 = %-4s  |d(L-R)| over NV 4001->6001 = %.3e   %s"
            % (alab, d, "within" if ok else "### OVER"))
    verdicts["T-B"] = tb
    rec("      ### T-B: %s" % ("PASS" if tb else "### FAIL"))

    rec("--- T-C: the archimedean-only reduction at a^2 = 2 (PR and Theta_q must be exactly 0).")
    s2 = rows["2"]["s"]
    arch = s2["Tr"] + s2["E2"] - s2["Dm"] - s2["A"]
    tc = (s2["PR"] == 0.0 and s2["Thq"] == 0.0 and abs(rows["2"]["LmR"] - arch) <= 1e-12)
    verdicts["T-C"] = tc
    rec("      PR = %.17g   Theta_q = %.17g" % (s2["PR"], s2["Thq"]))
    rec("      (L-R) = %.12f   archimedean-only = %.12f   |diff| = %.3e"
        % (rows["2"]["LmR"], arch, abs(rows["2"]["LmR"] - arch)))
    rec("      ### T-C: %s" % ("PASS" if tc else "### FAIL"))

    rec("--- T-D: the mode-axis signature. (L-R) at NMODE=7 exceeds NMODE=6 by tr[6], tol 1e-9.")
    td = True
    for a, alab in B38.CELLS:
        d7 = rows[alab]["LmR"]
        d6 = st[alab]["nmr"]["Lft"] - st[alab]["nmr"]["Rgt"]
        step = d7 - d6
        tr6 = st[alab]["b"]["tr_last"]
        ok = (step > 0) and abs(step - tr6) <= 1e-9
        td &= ok
        rec("      a^2 = %-4s  step = %+.9f   tr[6] = %+.9f   |diff| = %.2e   %s"
            % (alab, step, tr6, abs(step - tr6), "ok" if ok else "### FAIL"))
    verdicts["T-D"] = td
    rec("      ### T-D: %s" % ("PASS" if td else "### FAIL"))

    rec("--- T-E: the bank cross-check against b38/b37's runs of 2026-08-18. tol 1e-5.")
    te = True
    worst_te = 0.0
    for a, alab in B38.CELLS:
        rb, db = BANK38[alab]
        pred = rb - db
        d = abs(rows[alab]["LmR"] - pred)
        worst_te = max(worst_te, d)
        ok = d <= 1e-5
        te &= ok
        rec("      a^2 = %-4s  run = %.9f   bank(resid47 - D_dict) = %.9f   |diff| = %.3e   %s"
            % (alab, rows[alab]["LmR"], pred, d, "within" if ok else "### OVER"))
    verdicts["T-E"] = te
    rec("      ### T-E: %s   (worst |diff| = %.3e)" % ("PASS" if te else "### FAIL", worst_te))
    rec("")

    # ------------------------------------------------------------ BRANCH
    rec("=" * 108)
    rec("THE BRANCH, BY THE RULES BANKED BEFORE ANY NUMBER.")
    rec("=" * 108)
    allpass = all(verdicts.values())
    consonant = all(abs(rows[al]["LmR"]) <= rows[al]["bar"] for _, al in B38.CELLS)
    # ### D_ACC = 3: a contentful test failing by 3x or more.
    beyond = False
    for a, alab in B38.CELLS:
        r = rows[alab]["LmR"] / rows[alab]["resid47"]
        if r < 1.40 / 3.0 or r > 2.10 * 3.0:
            beyond = True
    if worst_te > 3e-5:
        beyond = True
    for k, v in sorted(verdicts.items()):
        rec("  %-5s : %s" % (k, "PASS" if v else "### FAIL"))
    rec("")
    if beyond:
        rec("### ### THE ACT'S BRANCH: ### **(DISSONANT-BEYOND)**")
    elif consonant:
        rec("### ### THE ACT'S BRANCH: ### **(CONSONANT)**")
    elif allpass:
        rec("### ### THE ACT'S BRANCH: ### **(ACCOUNTED)**")
    else:
        rec("### ### THE ACT'S BRANCH: ### **(INDETERMINATE)**")
    rec("")
    rec("### NO AXIS, MESH, MODE COUNT, eps OR CONSTANT WAS CHANGED AFTER A NUMBER WAS SEEN.")
    rec("### NO GRADE MOVED. ### M-2..M-5 STAND OPEN. ### NOTHING ABOUT h2 BEYOND THE REGISTER")
    rec("### SENTENCE EXACT. ### NOTHING DEPOSITS.")
    rec("=" * 108)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
