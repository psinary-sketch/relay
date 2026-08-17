"""EXPERIMENT ONE, THE E2 PROFILE — diagnosing the omega-instability the sweep found.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHAT THE SWEEP RETURNED (exp1_run_2026-08-17.txt), and why it cannot be reported as it stands:

    L = 3.2, 3.6   (lags log 2, log 3)              measured AT E1, stable across all three omega
    L >= 4.2       (lags log 2, log 3, 2 log 2, ..) measured DEPARTS, and the departure is
                                                    NOT STABLE IN omega:
        L = 4.2   omega 2e-3 -> 0.500697 | omega 1e-3 -> 0.483264 | omega 5e-4 -> 0.500174
        L = 7.0   omega 2e-3 -> 0.500000 | omega 1e-3 -> 0.475578 | omega 5e-4 -> 0.499100

The registered verdict rule withheld those rows as UNSTABLE. A departure that moves with the
grid is a statement about the grid until it is shown to be a statement about the mechanism.

THE HYPOTHESIS, REGISTERED WITH ITS MECHANISM BEFORE ANY NEW NUMBER IS COMPUTED
--------------------------------------------------------------------------------
H:  The instability is a COMMENSURABILITY ARTIFACT OF THE GRID.

    In the continuum the prime-power lags carry exact arithmetic relations: log 4 = 2 log 2.
    On the grid each lag sits at the integer address k_q = round(log q / omega), and

        k_4 = 2 k_2   iff   frac(log 2 / omega) is in [0, 1/4) U [3/4, 1).

    So the discretization either PRESERVES or DESTROYS the relation log 4 = 2 log 2 depending
    on omega alone. When it is preserved the two shift matrices commute as powers of one shift
    and generate a smaller algebra; when it is destroyed they do not. NOTHING IN THE WINDOW
    LENGTH OR THE COEFFICIENTS CHANGES — only the arithmetic of the rounding.

    The sweep's own three omega already split this way, which is what generated H and is
    therefore NOT evidence for it:
        omega 2e-3  frac = 0.574  INCOMMENSURATE   measured ~ 0.500
        omega 1e-3  frac = 0.147  COMMENSURATE     measured < 0.500
        omega 5e-4  frac = 0.294  INCOMMENSURATE   measured ~ 0.500

REGISTERED PREDICTIONS, on omega values the hypothesis has never seen
--------------------------------------------------------------------------------
P1  At L = 4.2, at each of three NEW INCOMMENSURATE omega (1.2e-3, 1.7e-3, 0.8e-3):
    fraction ~ 0.500, within 0.002.
P2  At L = 4.2, at each of three NEW COMMENSURATE omega (1.1e-3, 0.9e-3, 1.4e-3):
    fraction BELOW 0.497.
P3  At L = 3.6 — where no log-4 lag exists, so H predicts no split — all six omega agree
    with each other and with E1 to 0.002.
P4  MECHANISM CONTROL. At L = 4.2, omega = 1e-3 (commensurate), DROPPING ONLY the log-4 lag
    and keeping log 2 and log 3 returns the fraction to E1 (within 0.002). If the departure
    survives the removal of the log-4 lag, H is refuted at its named mechanism.
P5  INERTNESS CONTROL. At L = 3.6, omega = 1e-3, dropping the log-3 lag changes NOTHING.
    This separates "E1 confirmed" from "the second lag was inert" — two readings the sweep's
    AT-E1 verdict cannot tell apart, and only one of which is a result about the mechanism.

IF P1 AND P2 BOTH LAND, the L >= 4.2 rows measure the grid's arithmetic and not the two-prime
room, and no E2 verdict may be read off them at any omega.
IF EITHER FAILS, H is refuted and the departure is not the commensurability, which is a
finding about the mechanism and is reported as one.

Usage:  python exp1_e2_profile.py register
        python exp1_e2_profile.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2 = math.log(2.0)

OM_INCOMM = [1.2e-3, 1.7e-3, 0.8e-3]
OM_COMM = [1.1e-3, 0.9e-3, 1.4e-3]
L_SPLIT = 4.2
L_CONTROL = 3.6


def commensurate(omega):
    """True iff round(2 log2/omega) == 2 * round(log2/omega) — the grid keeps log 4 = 2 log 2."""
    k2 = int(round(LOG2 / omega))
    k4 = int(round(2 * LOG2 / omega))
    return k4 == 2 * k2


def frac_log2(omega):
    x = LOG2 / omega
    return x - math.floor(x)


def registration():
    W = 96
    print("=" * W)
    print("E2 PROFILE — REGISTRATION. PRINTED BEFORE ANY NEW MEASURED NUMBER.")
    print("=" * W)
    print(__doc__)
    print("-" * W)
    print("THE OMEGA VALUES, CLASSIFIED BY THE HYPOTHESIS BEFORE THEY ARE RUN")
    print("-" * W)
    print("  %-10s %-10s %-8s %-8s %-16s %s"
          % ("omega", "frac", "k_2", "k_4", "k_4 == 2 k_2 ?", "H predicts"))
    for om in sorted(OM_INCOMM + OM_COMM, reverse=True):
        k2 = int(round(LOG2 / om))
        k4 = int(round(2 * LOG2 / om))
        c = commensurate(om)
        print("  %-10.1e %-10.4f %-8d %-8d %-16s %s"
              % (om, frac_log2(om), k2, k4, "YES" if c else "no",
                 "below 0.497" if c else "~ 0.500"))
    print("\n  Three of each. The classification above is fixed by arithmetic alone and does")
    print("  not use the operator, the window, or any measured quantity.")
    print("=" * W)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n  eps'(1+) = %.7f\n" % e1p)

    omegas = sorted(set(OM_INCOMM + OM_COMM), reverse=True)
    nmax = {om: int(round(math.log(max(L_SPLIT, L_CONTROL)) / om)) for om in omegas}
    qvs = {}
    for om in omegas:
        t0 = time.time()
        qvs[om] = P._qvals(om, nmax[om], E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, %d lags, %.1f s]"
              % (om, nmax[om] + 1, time.time() - t0))
        sys.stdout.flush()

    W = 104
    for L, pnames in ((L_SPLIT, "P1 / P2"), (L_CONTROL, "P3")):
        pred = E1.e1_union(L)
        lags = E1.lag_schedule(L)
        print("\n" + "=" * W)
        print("%s — L = %.1f   lags: %s   E1 = %.6f"
              % (pnames, L, ", ".join(l for l, _, _ in lags), pred))
        print("=" * W)
        print("  %-10s %-14s %-8s %-16s %-11s %-12s %s"
              % ("omega", "class", "M", "measured", "fraction", "E2", "vs prediction"))
        for om in omegas:
            n, dim, frac, M = E1.measure(L, om, lags, qvs[om], e1p)
            c = commensurate(om)
            if L == L_SPLIT:
                ok = (frac < 0.497) if c else (abs(frac - 0.5) < 2e-3)
                tag = ("P2 " if c else "P1 ") + ("LANDS" if ok else "### FAILS")
            else:
                ok = abs(frac - pred) < 2e-3
                tag = "P3 " + ("LANDS" if ok else "### FAILS")
            print("  %-10.1e %-14s %-8d %-16s %-11.6f %-12s %s"
                  % (om, "COMMENSURATE" if c else "incommensurate", M,
                     "%d / %d" % (n, dim), frac, "%+.6f" % (frac - pred), tag))
            sys.stdout.flush()

    # ---------------------------------------------------------------- P4, P5
    om = 1.0e-3
    qv = P._qvals(om, int(round(math.log(L_SPLIT) / om)), E1.NG_Q)
    print("\n" + "=" * W)
    print("P4 — MECHANISM CONTROL at L = 4.2, omega = 1e-3 (COMMENSURATE)")
    print("=" * W)
    pred = E1.e1_union(L_SPLIT)
    full = E1.lag_schedule(L_SPLIT)
    no4 = [x for x in full if x[0] != "2 log 2"]
    only2 = [x for x in full if x[0] == "log 2"]
    for label, lg in (("all lags", full), ("log-4 lag REMOVED", no4), ("log 2 only", only2)):
        n, dim, frac, M = E1.measure(L_SPLIT, om, lg, qv, e1p)
        print("  %-22s %-28s %6d / %-6d = %.6f   E2 = %+.6f"
              % (label, "[" + ", ".join(l for l, _, _ in lg) + "]", n, dim, frac, frac - pred))
        sys.stdout.flush()
    print("  E1 = %.6f" % pred)

    om = 1.0e-3
    qv = P._qvals(om, int(round(math.log(L_CONTROL) / om)), E1.NG_Q)
    print("\n" + "=" * W)
    print("P5 — INERTNESS CONTROL at L = 3.6, omega = 1e-3")
    print("=" * W)
    pred = E1.e1_union(L_CONTROL)
    full = E1.lag_schedule(L_CONTROL)
    only2 = [x for x in full if x[0] == "log 2"]
    res = {}
    for label, lg in (("log 2 + log 3", full), ("log 3 REMOVED", only2)):
        n, dim, frac, M = E1.measure(L_CONTROL, om, lg, qv, e1p)
        res[label] = (n, dim, frac)
        print("  %-22s %-28s %6d / %-6d = %.6f   E2 = %+.6f"
              % (label, "[" + ", ".join(l for l, _, _ in lg) + "]", n, dim, frac, frac - pred))
        sys.stdout.flush()
    a, b = res["log 2 + log 3"], res["log 3 REMOVED"]
    print("  E1 = %.6f" % pred)
    print("  ### THE LOG-3 LAG IS %s: it moves the count by %+d offenders."
          % ("INERT" if a[0] == b[0] else "ACTIVE", a[0] - b[0]))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
