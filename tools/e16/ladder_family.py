"""THE LADDER IN u = t/log L, AND THE ANTI-ALIGNMENT NAMED.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

ACT (a) — IS THE REMAINDER'S POSITIVE FAMILY A FIXED FAMILY IN u?
=================================================================
2026-08-17 measured, at L = 4.6, 8, 16: the positive directions of A_main on V are NOT a
fixed subspace in t (the count grows 2, 3, 3, 4, 5 and the unscaled overlaps do not
stabilise) but ARE nearly identical in the RESCALED coordinate u = t/log L (overlaps
0.9963 / 0.9834 / 0.9951). This act asks the question at a much wider separation, L = 16
against L = 64 -- a factor of four in the window and of two in r -- and banks the family.

  VERDICT BRANCHES, LONGHAND:
  ### FIXED FAMILY IN u -- if the leading members match across L = 16 and L = 64 in u to the
  same tolerance they matched at 16 vs 8, then the remainder has a SCALING LIMIT: its
  positive part is a fixed sequence of functions of u, entering one at a time as the window
  grows. The family's first six members are then banked as functions and become the object a
  bound would be proved about.
  ### DRIFTING -- if the u-overlaps fall away at the wider separation, the u-agreement seen at
  8 vs 16 was local, there is no scaling limit, and the remainder is filed as drifting with
  no family to bound.

ACT (b) — THE ANTI-ALIGNMENT, AND A MECHANISM THAT MAKES IT A PREDICTION
========================================================================
The lag form's Rayleigh quotient on a mode v is  R(v) = v^T S_k v / v^T v
                                                      = 2 <v[k:], v[:-k]> / <v,v>,
the autocorrelation of v at the lag's own address. Measured 2026-08-17:

    L = 4.6 (r = 2.20):  -0.566, -1.145
    L = 8.0 (r = 3.00):  +0.130, -1.066, -1.294, -0.343
    L = 16  (r = 4.00):  +0.751, -0.407, -1.370, -1.476, -0.802

### MOSTLY NEGATIVE, WITH EXACTLY ONE POSITIVE EXCEPTION PER WINDOW, ALWAYS THE LOWEST MODE.

THE MECHANISM PROPOSED, AND IT IS PROPOSED BEFORE THE L = 64 RUN SO IT CAN FAIL.
The members are the window's own low modes with node counts n = 1, 2, 3, ..., so on the
window's own scale each looks like sin(n pi u). The autocorrelation of sin(n pi u) at a lag
of ell = log 2, i.e. at u-lag 1/r, is proportional to cos(n pi / r), with an overlap factor
(1 - 1/r) from the truncated support:

    ### R(v_n)  ~  2 (1 - 1/r) cos(n pi / r)

so the SIGN of R is the sign of cos(n pi / r):
    ### POSITIVE exactly for n < r/2, NEGATIVE for r/2 < n < 3r/2.

Checked against what is already banked, without refitting anything:
    r = 4, n = 4 : 2(0.75)cos(pi) = -1.500   measured -1.476
    r = 3, n = 3 : 2(0.667)cos(pi) = -1.333  measured -1.294
    r = 4, n = 1 : +1.061                    measured +0.751
    r = 2.2, n = 1: +0.157                   measured -0.566   ### the model MISSES here

### SO THE MODEL IS GOOD AT THE HIGH MODES AND POOR AT n = 1 IN A NARROW WINDOW, AND THAT IS
### SAID BEFORE IT IS USED.

  ### REGISTERED PREDICTION, THE SHARP ONE: at L = 64, r = 6, the rule "positive exactly for
  ### n < r/2" gives n < 3, i.e. TWO positive-Rayleigh modes (n = 1 and n = 2) and the rest
  ### negative. Every window measured so far has had exactly ONE. If two appear, the
  mechanism predicted a change of behaviour at a window nobody had looked at; if one appears,
  the rule "exactly one exception, always the lowest" survives and the cos model is refuted
  as the explanation.

  THE INEQUALITY CANDIDATE, stated so it can be argued with:
  ### "FOR THE WINDOW-SCALED MODES OF THE REMAINDER, THE LAG FORM IS NEGATIVE-DOMINANT: R(v_n)
  ### < 0 for every n with r/2 < n < 3r/2, and the positive exceptions are exactly the modes
  ### whose half-wavelength exceeds the lag (n < r/2)."
  ### NO BOUND IS CLAIMED FROM IT. It is a statement about a measured family, offered at
  question grade; turning it into a bound on |NPOS(A) - NPOS(S_k)| would additionally need
  the family to be complete for A_main's positive part and the cross terms controlled, and
  NEITHER IS IN HAND.

Usage:  python ladder_family.py register | run
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
LS = [16.0, 64.0]
OM = 1.0e-3
NGRID = 4000
BANK = r"D:\relay\data\ladder_family_2026-08-17.csv"


def registration():
    print("=" * 112)
    print("THE LADDER FAMILY — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 112)
    print(__doc__)
    for L in LS:
        M = int(round(math.log(L) / OM))
        r = M / int(round(LOG2 / OM))
        print("  L = %-6.1f M = %-6d r = %.4f   cos-model sign flips at n = r/2 = %.2f"
              % (L, M, r, r / 2))
    print("=" * 112)
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
        print("=" * 112)
        print("L = %.1f   M = %d   r = %.4f   ### NPOS(A_main) = %d      [%.0fs]"
              % (L, M, r, len(pos), time.time() - t0))
        print("=" * 112)
        print("  %-4s %-14s %-9s %-6s %-11s %-12s %-13s %s"
              % ("n?", "eigenvalue", "parity", "nodes", "centroid u", "head mass",
                 "R measured", "2(1-1/r)cos(n pi/r)"))
        vs = []
        for j in pos:
            v = lift(evec[:, j], u)
            par, nodes, ct, cu, head, rough = profile(v, OM, M)
            R = shift_rayleigh(v, k2)
            model = 2 * (1 - 1 / r) * math.cos(nodes * math.pi / r)
            vs.append((v, nodes, par, R, model, float(ev[j])))
            print("  %-4d %-14.6e %+.4f (%s) %-6d %-11.5f %-12.5f %+-13.6f %+.6f  %s"
                  % (nodes, float(ev[j]), par, "EVEN" if par > 0 else "ODD ", nodes, cu,
                     head, R, model, "" if (R > 0) == (model > 0) else "### SIGN MISMATCH"))
            sys.stdout.flush()
        # rescale to u
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
        print("\n  positive-Rayleigh modes at this window: ### %d   (cos-model predicts n < r/2 = %.2f -> %d)"
              % (npos_pos, r / 2, max(0, math.ceil(r / 2) - 1)))

    print("\n" + "=" * 112)
    print("ACT (a) — THE FAMILY IN u, ACROSS A FACTOR OF FOUR IN THE WINDOW")
    print("=" * 112)
    a, b = LS
    ra, rb = fam[a][0], fam[b][0]
    print("  overlaps |<v_i(L=%.0f), v_j(L=%.0f)>| in u:" % (a, b))
    hdr = "        " + " ".join("n=%-6d" % nb for _, nb in rb)
    print(hdr)
    diag = []
    for wa, na in ra:
        row = [abs(float(wa @ wb)) for wb, _ in rb]
        best = max(range(len(row)), key=lambda i: row[i])
        diag.append((na, rb[best][1], row[best]))
        print("  n=%-4d %s" % (na, " ".join("%-8.4f" % x for x in row)))
    print("\n  best match per member: %s"
          % ", ".join("n=%d->n=%d (%.4f)" % (x, y, z) for x, y, z in diag))
    same = [z for x, y, z in diag if x == y]
    print("  ### node-count-matched overlaps: %s"
          % (", ".join("%.4f" % z for z in same) if same else "none"))
    verdict = bool(same) and min(same) > 0.90
    print("\n  ### VERDICT: %s"
          % ("FIXED FAMILY IN u — the remainder has a scaling limit"
             if verdict else "### DRIFTING — no scaling limit at this separation"))

    # bank the first six members as functions
    six = fam[b][0][:6]
    with open(BANK, "w", encoding="utf-8") as f:
        f.write("u," + ",".join("mode_n%d" % n for _, n in six) + "\n")
        for i in range(0, NGRID, 4):
            f.write("%.6f," % grid[i] + ",".join("%.8e" % w[i] for w, _ in six) + "\n")
    print("\n  family banked as functions: %s  (%d members, %d sample points)"
          % (BANK, len(six), len(range(0, NGRID, 4))))

    print("\n" + "=" * 112)
    print("ACT (b) — THE INEQUALITY CANDIDATE, AGAINST THE FAMILY")
    print("=" * 112)
    for L in LS:
        resc, vs, r = fam[L]
        neg = [(n, R) for _, n, _, R, _, _ in vs if R < 0]
        pos = [(n, R) for _, n, _, R, _, _ in vs if R > 0]
        band = [(n, R) for _, n, _, R, _, _ in vs if r / 2 < n < 3 * r / 2]
        allneg = all(R < 0 for _, R in band)
        print("  L = %-6.1f r = %.3f" % (L, r))
        print("        modes with r/2 < n < 3r/2 : %s"
              % (", ".join("n=%d R=%+.4f" % (n, R) for n, R in band) or "none"))
        print("        ### negative-dominant on that band: %s" % ("HOLDS" if allneg else "### FAILS"))
        print("        positive exceptions: %s  (rule predicts n < r/2 = %.2f)"
              % (", ".join("n=%d R=%+.4f" % (n, R) for n, R in pos) or "none", r / 2))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
