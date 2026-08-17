"""EXPERIMENT ONE, THE SEPARATING ACT — localizing the omega-split to a lag PAIR or a lag ADDRESS.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THIS ACT EXISTS — A CONFOUND IN MY OWN PROFILE, CAUGHT BEFORE ITS NUMBERS WERE READ
-----------------------------------------------------------------------------------------
The profile registered the split as a COMMENSURABILITY effect: k_4 = 2 k_2 or not. Before
its results were read I checked whether its six omega could separate that from a PARITY
effect (k_4 even or odd) and found they could not — every one of the six was commensurate
exactly when k_4 was even.

THEY COULD NOT HAVE. THE TWO ARE THE SAME CONDITION, AND HERE IS THE ONE-LINE PROOF:

    for any real x,  |round(2x) - 2 round(x)| <= 1.
    2 round(x) is even. So k_4 != 2 k_2 forces k_4 = 2 k_2 +/- 1, hence k_4 ODD;
    and k_4 = 2 k_2 forces k_4 EVEN.

        ### k_4 = 2 k_2   <=>   k_4 is even.   Identically, for every omega.

So no choice of omega can ever separate "the grid preserves log 4 = 2 log 2" from "the log-4
address is even". The profile was not confounded by bad luck in its six values; the question
as posed is not decidable by varying omega AT ALL. Registering the mechanism did not save the
design — checking whether the design could distinguish the mechanisms is a separate act, and
it is this one.

WHAT CAN SEPARATE THEM: VARYING THE LAG SET, NOT THE GRID
-----------------------------------------------------------------------------------------
If the effect is the RELATION log 4 = 2 log 2 rendered on the grid, it needs BOTH addresses
present: S^{k_4} = (S^{k_2})^2 is a statement about a pair. If it is a property of the log-4
address alone, it survives with log 2 removed.

    L = 4.2 fixed. E1(4.2) = 1 - log2/log(4.2), the same number at every omega.
    omega_even = 1.0e-3   k_2 = 693, k_3 = 1099, k_4 = 1386 = 2 k_2   (EVEN)
    omega_odd  = 1.2e-3   k_2 = 578, k_3 =  916, k_4 = 1155 != 2 k_2  (ODD)

    Six lag sets at each: {log2} · {log2,log3} · {log2,2log2} · {log3,2log2} · {2log2} · all.
    SPLIT(set) := | fraction at omega_even - fraction at omega_odd |, called present if > 0.01.

REGISTERED PREDICTIONS
-----------------------------------------------------------------------------------------
R1  {log2} and {log2,log3} show NO split at either omega, and both sit at E1.
    (Replicates the sweep's stable rows; if this fails the whole diagnosis is void.)
R2  IF the split is present for {log2,2log2} and ABSENT for both {log3,2log2} and {2log2},
    THEN the effect requires the log2-log4 PAIR: it is the grid's rendering of the
    arithmetic relation log 4 = 2 log 2, and it is an artifact of the discretization of a
    true relation rather than a property of the operator.
R3  IF the split is present for {2log2} ALONE, THEN it is a property of a single address's
    parity, no relation is involved, and the commensurability reading is wrong even though
    it fits every omega — because it was never separable from parity to begin with.
R4  IF the split is present for {log3,2log2} but absent for {log2,2log2}, neither reading
    survives and the act reports the pattern without a mechanism.

    A fifth outcome is possible and is registered as such: NO SPLIT ANYWHERE except in the
    full set, which would locate the effect in a three-lag interaction and refute both R2
    and R3.

Usage:  python exp1_e2_separate.py register
        python exp1_e2_separate.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

L = 4.2
OM_EVEN = 1.0e-3
OM_ODD = 1.2e-3
SPLIT_THRESHOLD = 0.01

SETS = [
    ("{log2}", ["log 2"]),
    ("{log2,log3}", ["log 2", "log 3"]),
    ("{log2,2log2}", ["log 2", "2 log 2"]),
    ("{log3,2log2}", ["log 3", "2 log 2"]),
    ("{2log2}", ["2 log 2"]),
    ("{log2,log3,2log2}", ["log 2", "log 3", "2 log 2"]),
]


def registration():
    W = 96
    print("=" * W)
    print("THE SEPARATING ACT — REGISTRATION. PRINTED BEFORE ANY NEW MEASURED NUMBER.")
    print("=" * W)
    print(__doc__)
    print("-" * W)
    print("  addresses, fixed by arithmetic alone:")
    for om in (OM_EVEN, OM_ODD):
        k2 = round(math.log(2) / om)
        k3 = round(math.log(3) / om)
        k4 = round(2 * math.log(2) / om)
        print("    omega=%.1e  M=%d  k_2=%d  k_3=%d  k_4=%d  (%s, %s)"
              % (om, round(math.log(L) / om), k2, k3, k4,
                 "even" if k4 % 2 == 0 else "odd",
                 "k_4 = 2k_2" if k4 == 2 * k2 else "k_4 != 2k_2"))
    print("  E1(%.1f) = %.6f at both omega." % (L, E1.e1_union(L)))
    print("=" * W)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    pred = E1.e1_union(L)
    full = {lab: (lab, ell, c) for lab, ell, c in E1.lag_schedule(L)}

    qvs = {}
    for om in (OM_EVEN, OM_ODD):
        t0 = time.time()
        qvs[om] = P._qvals(om, int(round(math.log(L) / om)), E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, %.1f s]" % (om, time.time() - t0))
        sys.stdout.flush()

    W = 104
    print("\n" + "=" * W)
    print("L = %.1f   E1 = %.6f   split threshold %.3f" % (L, pred, SPLIT_THRESHOLD))
    print("=" * W)
    print("  %-20s %-24s %-24s %-11s %s"
          % ("lag set", "omega=1.0e-3 (k4 EVEN)", "omega=1.2e-3 (k4 odd)", "|split|", "reading"))
    out = {}
    for name, labels in SETS:
        lg = [full[l] for l in labels]
        row = []
        for om in (OM_EVEN, OM_ODD):
            n, dim, frac, M = E1.measure(L, om, lg, qvs[om], e1p)
            row.append((n, dim, frac))
        sp = abs(row[0][2] - row[1][2])
        out[name] = (row, sp)
        print("  %-20s %-24s %-24s %-11.6f %s"
              % (name,
                 "%d/%d = %.6f" % (row[0][0], row[0][1], row[0][2]),
                 "%d/%d = %.6f" % (row[1][0], row[1][1], row[1][2]),
                 sp, "### SPLIT" if sp > SPLIT_THRESHOLD else "no split"))
        sys.stdout.flush()

    print("\n" + "-" * W)
    print("  E2 against E1 = %.6f, per cell:" % pred)
    for name, _ in SETS:
        row, sp = out[name]
        print("    %-20s  even: %+.6f    odd: %+.6f" % (name, row[0][2] - pred, row[1][2] - pred))

    print("\n" + "-" * W)
    s = {k: v[1] > SPLIT_THRESHOLD for k, v in out.items()}
    print("  R1 %s — {log2} split=%s, {log2,log3} split=%s"
          % ("HOLDS" if not (s["{log2}"] or s["{log2,log3}"]) else "### FAILS",
             s["{log2}"], s["{log2,log3}"]))
    if s["{log2,2log2}"] and not s["{log3,2log2}"] and not s["{2log2}"]:
        print("  ### R2 — THE EFFECT REQUIRES THE log2-log4 PAIR. It is the grid's rendering")
        print("      of log 4 = 2 log 2, not a property of the operator.")
    elif s["{2log2}"]:
        print("  ### R3 — THE EFFECT IS PRESENT WITH log 4 ALONE. No relation is involved;")
        print("      the commensurability reading is not the mechanism.")
    elif s["{log3,2log2}"] and not s["{log2,2log2}"]:
        print("  ### R4 — pattern reported without a mechanism.")
    elif s["{log2,log3,2log2}"]:
        print("  ### FIFTH OUTCOME — the split lives only in the three-lag set. Both R2 and")
        print("      R3 are refuted; the effect is a three-lag interaction.")
    else:
        print("  ### NO SPLIT ANYWHERE — including the full set. That contradicts the sweep")
        print("      and the instrument, not the hypothesis. Report as a failure to reproduce.")


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
