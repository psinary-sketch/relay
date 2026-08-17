"""THE THIRD WINDOW — L = 256, r = 8: does the scaling limit stand across a sixteenfold range?

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THIS CELL EXISTS, AND IT IS THE DAY'S OWN LAW APPLIED TO THE DAY'S OWN CLAIM
================================================================================
2026-08-17 measured the remainder's positive family at L = 16 and L = 64 and found it FIXED
in u = t/log L -- node-matched overlaps 0.9847, 0.9944, 0.9952, 0.9927, 0.9657 -- and filed
that as a SCALING LIMIT.

    ### THE STANDING LAW MINTED THIS MORNING: A LAW READ OFF A RANGE IS A LAW ABOUT THAT
    ### RANGE -- ONE CELL OUTSIDE IS THE CHEAP DEFENCE.

Two windows are a range. L = 256 (r = 8) is the cell outside it, and it makes the span
sixteenfold in L and a factor of two in r.

REGISTERED PREDICTIONS, PRINTED BEFORE ANY MEASUREMENT
=======================================================
S1  THE FAMILY. The first members at r = 8 match the r = 4 and r = 6 members by NODE COUNT,
    in u, to the tolerance already seen (node-matched overlaps > 0.90, off-diagonals small).
    ### IF THEY DO: the scaling limit stands at three windows spanning a factor of sixteen in
    L, and the family is an object with a defined limit rather than a local coincidence.
    ### IF THEY DRIFT: the u-agreement at 16-vs-64 was local, two windows were not a scaling
    limit, and the day's claim is corrected by the day's own law -- which is the outcome the
    law exists to produce and would be reported as the finding.

S2  THE ANTI-ALIGNMENT RULE, CHECKED UNREFITTED AT r = 8.
        R(v_n) ~ 2(1 - 1/r) cos(n pi / r)  =  1.75 * cos(n pi / 8)  at r = 8
    giving, for n = 1..8:
        +1.617, +1.237, +0.670, 0.000, -0.670, -1.237, -1.617, -1.750
    ### AND THE SHARPENED RULE FROM THE r = 4 AND r = 6 CELLS -- positive exactly for
    ### n < r/2, WITH THE BOUNDARY MODE n = r/2 FALLING NEGATIVE -- PREDICTS EXACTLY
    ### THREE POSITIVE EXCEPTIONS AT r = 8: n = 1, 2, 3, with n = 4 negative.

    ### A CORRECTION TO THIS BLOCK, MADE BEFORE ANY MEASUREMENT AND LEFT VISIBLE. The grid
    ### gives r = 8.0014, so a literal 'n < r/2' admits n = 4 and would predict FOUR. That is
    ### NOT the rule the r = 4 and r = 6 cells measured: there the boundary modes (n = 2 at
    ### r = 4.0014, n = 3 at r = 6.0014) were BOTH admitted by the literal inequality and
    ### BOTH came out NEGATIVE. The rule is therefore n <= round(r/2) - 1, which gives
    ### 1, 2, 3 at r = 4, 6, 8 and reproduces both measured counts.
    ### THE REGISTERED PREDICTION IS THREE. The literal-inequality count of four is recorded
    ### beside it so that landing three cannot later be read as fitting the rule to the
    ### answer.
    Every window measured so far has had 1 (r = 4) and 2 (r = 6). ### THREE IS THE NEXT
    ### VALUE AND IT IS WRITTEN DOWN BEFORE THE RUN.

S3  NEGATIVE-DOMINANCE on the band r/2 < n < 3r/2, i.e. 4 < n < 12: every member in that
    band has R < 0. It has held 3 of 3 at r = 4 and 5 of 5 at r = 6.

    ### IF S2 GIVES 3: the mechanism has now predicted the exception count at two windows it
    had never seen (2 at r = 6, 3 at r = 8) and the rule is worth stating as a candidate.
    ### IF S2 GIVES ANYTHING ELSE: the cos model predicted the r = 6 change by luck, and the
    rule is filed as an observation about r = 4 and r = 6 only.

WHAT IS NOT CLAIMED EITHER WAY
===============================
### NO BOUND. A bound on |NPOS(A) - NPOS(S_k)| would additionally need (a) the family to be
COMPLETE for A_main's positive part and (b) the CROSS TERMS between members under the lag
form. Neither is in hand and neither is touched here. A diagonal sign pattern is not an
inertia bound.

Usage:  python ladder_third.py register | run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
from amain_identify import amain_V, lift, profile, shift_rayleigh

LOG2 = math.log(2.0)
LS = [16.0, 64.0, 256.0]
OM = 1.0e-3
NGRID = 4000
BANK = r"D:\relay\data\ladder_family_three_2026-08-17.csv"


def registration():
    print("=" * 116)
    print("THE THIRD WINDOW — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 116)
    print(__doc__)
    k2 = int(round(LOG2 / OM))
    print("  %-7s %-7s %-9s %-14s %-16s %-12s %s"
          % ("L", "M", "r = M/k", "literal n<r/2", "REGISTERED rule", "measured", "prediction"))
    for L in LS:
        M = int(round(math.log(L) / OM))
        r = M / k2
        lit = len([n for n in range(1, 30) if n < r / 2])
        reg = int(round(r / 2)) - 1
        seen = {4: "1", 6: "2"}.get(int(round(r)), "-")
        print("  %-7.0f %-7d %-9.4f %-14d %-16d %-12s %s"
              % (L, M, r, lit, reg, seen,
                 "(already measured)" if seen != "-" else "### THREE"))
    print("\n  cos-model values at r = 8, n = 1..8:")
    r8 = int(round(math.log(256.0) / OM)) / k2
    print("     " + "  ".join("%+.3f" % (2 * (1 - 1 / r8) * math.cos(n * math.pi / r8))
                              for n in range(1, 9)))
    print("=" * 116)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    need = int(round(math.log(max(LS)) / OM))
    t0 = time.time()
    qv = P._qvals(OM, need, E1.NG_Q)
    print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]\n" % (OM, need, time.time() - t0))

    k2 = int(round(LOG2 / OM))
    grid = np.linspace(0.0, 1.0, NGRID)
    fam = {}
    for L in LS:
        t0 = time.time()
        A, u, M = amain_V(L, OM, qv, e1p)
        ev, evec = np.linalg.eigh(A)
        pos = np.where(ev > 0)[0][::-1]
        r = M / k2
        print("=" * 116)
        print("L = %.0f   M = %d   r = %.4f   ### NPOS(A_main) = %d      [%.0fs]"
              % (L, M, r, len(pos), time.time() - t0))
        print("=" * 116)
        print("  %-5s %-14s %-9s %-11s %-12s %-14s %s"
              % ("nodes", "eigenvalue", "parity", "centroid u", "head mass",
                 "R measured", "1.75-style model"))
        vs = []
        for j in pos:
            v = lift(evec[:, j], u)
            par, nodes, ct, cu, head, rough = profile(v, OM, M)
            R = shift_rayleigh(v, k2)
            model = 2 * (1 - 1 / r) * math.cos(nodes * math.pi / r)
            vs.append((v, nodes, par, R, model, float(ev[j])))
            print("  %-5d %-14.6e %+.4f (%s) %-11.5f %-12.5f %+-14.6f %+.6f %s"
                  % (nodes, float(ev[j]), par, "EVEN" if par > 0 else "ODD ", cu, head, R, model,
                     "" if (R > 0) == (model > 0) else "### SIGN MISMATCH"))
            sys.stdout.flush()
        resc = []
        for v, nodes, par, R, model, lam in vs:
            uu = (np.arange(len(v)) + 0.5) / len(v)
            w = np.interp(grid, uu, v)
            w = w / max(np.linalg.norm(w), 1e-300)
            if w[np.argmax(np.abs(w))] < 0:
                w = -w
            resc.append((w, nodes))
        fam[L] = (resc, vs, r)
        npos_pos = sum(1 for _, _, _, R, _, _ in vs if R > 0)
        pred = int(round(r / 2)) - 1
        print("\n  ### positive-Rayleigh modes: %d   (sharpened rule n < r/2 = %.4f predicts %d)  %s"
              % (npos_pos, r / 2, pred, "### S2 LANDS" if npos_pos == pred else "### S2 FAILS"))
        del A, ev, evec

    print("\n" + "=" * 116)
    print("S1 — THE FAMILY IN u ACROSS THREE WINDOWS (a sixteenfold range in L)")
    print("=" * 116)
    pairs = [(LS[0], LS[1]), (LS[1], LS[2]), (LS[0], LS[2])]
    verdicts = []
    for a, b in pairs:
        ra, rb = fam[a][0], fam[b][0]
        print("\n  L = %.0f  vs  L = %.0f" % (a, b))
        print("        " + " ".join("n=%-6d" % nb for _, nb in rb[:9]))
        diag = []
        for wa, na in ra[:9]:
            row = [abs(float(wa @ wb)) for wb, _ in rb[:9]]
            best = max(range(len(row)), key=lambda i: row[i])
            diag.append((na, rb[best][1], row[best], max(x for i, x in enumerate(row) if i != best)))
            print("  n=%-4d %s" % (na, " ".join("%-8.4f" % x for x in row)))
        matched = [(na, ov, off) for na, nb, ov, off in diag if na == nb]
        print("  node-matched overlaps : %s" % ", ".join("n=%d:%.4f" % (n, o) for n, o, _ in matched))
        print("  largest off-diagonal  : %s" % ", ".join("n=%d:%.4f" % (n, f) for n, _, f in matched))
        ok = bool(matched) and min(o for _, o, _ in matched) > 0.90
        verdicts.append(ok)
        print("  ### %s" % ("HOLDS" if ok else "### DRIFTS"))

    print("\n" + "=" * 116)
    print("  ### S1 VERDICT: %s"
          % ("THE SCALING LIMIT STANDS AT THREE WINDOWS (16, 64, 256 — a sixteenfold range)"
             if all(verdicts) else "### THE FAMILY DRIFTS — two windows were not a scaling limit"))
    print("=" * 116)

    print("\n" + "=" * 116)
    print("S3 — NEGATIVE-DOMINANCE ON r/2 < n < 3r/2")
    print("=" * 116)
    for L in LS:
        resc, vs, r = fam[L]
        band = [(n, R) for _, n, _, R, _, _ in vs if r / 2 < n < 3 * r / 2]
        pos = [(n, R) for _, n, _, R, _, _ in vs if R > 0]
        print("  L = %-6.0f r = %.3f   band members: %d   all negative: %s"
              % (L, r, len(band), "### HOLDS" if all(R < 0 for _, R in band) else "### FAILS"))
        print("        band : %s" % (", ".join("n=%d R=%+.4f" % (n, R) for n, R in band) or "none"))
        print("        positive exceptions : %s"
              % (", ".join("n=%d R=%+.4f" % (n, R) for n, R in pos) or "none"))

    six = fam[LS[-1]][0][:6]
    with open(BANK, "w", encoding="utf-8") as f:
        f.write("u," + ",".join("mode_n%d" % n for _, n in six) + "\n")
        for i in range(0, NGRID, 4):
            f.write("%.6f," % grid[i] + ",".join("%.8e" % w[i] for w, _ in six) + "\n")
    print("\n  r = 8 family banked as functions: %s" % BANK)


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
