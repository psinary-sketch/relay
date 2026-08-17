"""EXPERIMENT ONE, THE BASELINE ACT — the ONE-PRIME law re-measured over the sweep's own range.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THIS ACT EXISTS — THE MECHANISM CONTROL REFUTED THE HYPOTHESIS AND THE DESIGN TOGETHER
--------------------------------------------------------------------------------------------
The profile's P4 removed the log-4 lag at L = 4.2, omega = 1e-3, and then removed log 3 too:

    all lags  [log 2, log 3, 2 log 2]   693 / 1434 = 0.483264
    log 2 ONLY                          693 / 1434 = 0.483264      IDENTICAL, to the offender

    E1 = 0.516999

### THE DEPARTURE IS PRESENT WITH THE SINGLE log-2 LAG. THE EXTRA PRIME POWERS DO NOT CAUSE IT.

So the sweep's E2, defined as (measured - E1), was not measuring the two-prime room at all. It
was measuring E1's own failure at these window lengths and attributing it to the extra lags,
because the one-prime law had never been measured beyond L = 4.0 and was assumed to hold there.

    ### A BASELINE THAT IS ASSUMED IS NOT A BASELINE. E2 was defined against a PREDICTION where
    it had to be defined against a MEASUREMENT.

THE REPAIR, AND IT IS A DEFINITION CHANGE REGISTERED BEFORE ITS RUN
--------------------------------------------------------------------------------------------
    E2-INTERACTION(L, omega) := fraction[all active lags] - fraction[log 2 only]

at the SAME L and the SAME omega, so every quantity the two share — the grid, the window, the
operator, the law's own behaviour at that L — cancels, and what remains is what the extra prime
powers do and nothing else. The old quantity is retained under its own name:

    E1-RESIDUAL(L, omega)   := fraction[log 2 only] - E1-UNION(L)

which is now correctly labelled as a statement about the ONE-PRIME law, not about the sweep.

REGISTERED PREDICTIONS
--------------------------------------------------------------------------------------------
B1  E1-RESIDUAL is small (|.| < 0.002) at L = 3.2 and 3.6 and LARGE (|.| > 0.01) at every
    L >= 4.2, at the commensurate omega — i.e. the one-prime law's own failure begins between
    L = 3.6 and L = 4.2, and the sweep's "departure" is that failure.
B2  E1-RESIDUAL carries the omega-class split (commensurate vs not) at every L >= 4.2, with
    log 2 as the ONLY lag present — so the split is a property of the one-prime measurement.
B3  E2-INTERACTION is at most a few offenders in the whole grid at every L and every omega —
    the extra prime powers are inert, as the log-3 lag was measured to be at L = 3.6
    (+1 offender in 1280).
B4  IF B3 fails at any L, the extra prime powers ARE doing measurable work there, and the
    magnitude and sign of E2-INTERACTION at that L is the experiment's actual result.

    Registered explicitly: B1 and B2 are predictions about a LAW THE CORPUS ALREADY BANKED,
    at window lengths it was never measured at. A failure of the one-prime law past L = 4 is a
    finding about the delta/L relation itself and is reported as one, whatever E2 does.

Usage:  python exp1_baseline.py register
        python exp1_baseline.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LS = [3.2, 3.6, 4.2, 4.6, 5.5, 7.0]
OMEGAS = [2.0e-3, 1.0e-3, 5.0e-4]
LOG2 = math.log(2.0)


def commensurate(omega):
    return int(round(2 * LOG2 / omega)) == 2 * int(round(LOG2 / omega))


def registration():
    W = 96
    print("=" * W)
    print("THE BASELINE ACT — REGISTRATION. PRINTED BEFORE ANY NEW MEASURED NUMBER.")
    print("=" * W)
    print(__doc__)
    print("-" * W)
    print("  the omega classes, fixed by arithmetic alone:")
    for om in OMEGAS:
        print("    omega=%.1e  k_2=%d  k_4=%d  %s"
              % (om, round(LOG2 / om), round(2 * LOG2 / om),
                 "COMMENSURATE" if commensurate(om) else "incommensurate"))
    print("\n  E1-UNION per L (unchanged, closed form):")
    for L in LS:
        print("    L=%.1f  E1 = %.6f    log2/logL = %.6f" % (L, E1.e1_union(L), LOG2 / math.log(L)))
    print("=" * W)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    nmax = {om: int(round(math.log(max(LS)) / om)) for om in OMEGAS}
    qvs = {}
    for om in OMEGAS:
        t0 = time.time()
        qvs[om] = P._qvals(om, nmax[om], E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, %.1f s]" % (om, time.time() - t0))
        sys.stdout.flush()

    W = 118
    print("\n" + "=" * W)
    print("THE ONE-PRIME BASELINE AND THE ISOLATED INTERACTION, ALL ON V")
    print("=" * W)
    print("  %-6s %-10s %-15s %-8s %-15s %-15s %-13s %s"
          % ("L", "omega", "class", "M", "log 2 only", "all lags", "E1-RESIDUAL", "E2-INTERACTION"))
    rows = []
    for L in LS:
        pred = E1.e1_union(L)
        full = E1.lag_schedule(L)
        only2 = [x for x in full if x[0] == "log 2"]
        for om in OMEGAS:
            n1, d1, f1, M = E1.measure(L, om, only2, qvs[om], e1p)
            nA, dA, fA, _ = E1.measure(L, om, full, qvs[om], e1p)
            rows.append((L, om, M, n1, d1, f1, nA, fA, pred))
            print("  %-6.1f %-10.1e %-15s %-8d %-15s %-15s %-13s %s"
                  % (L, om, "COMMENSURATE" if commensurate(om) else "incommensurate", M,
                     "%d = %.6f" % (n1, f1), "%d = %.6f" % (nA, fA),
                     "%+.6f" % (f1 - pred),
                     "%+.6f (%+d)" % (fA - f1, nA - n1)))
            sys.stdout.flush()
        print()

    print("=" * W)
    print("  VERDICTS AGAINST THE REGISTERED PREDICTIONS")
    print("=" * W)
    big = [r for r in rows if abs(r[5] - r[8]) > 0.01]
    small = [r for r in rows if abs(r[5] - r[8]) <= 0.002]
    print("  B1: |E1-RESIDUAL| > 0.01 at %d of %d cells; <= 0.002 at %d."
          % (len(big), len(rows), len(small)))
    print("      L values with a large one-prime residual anywhere: %s"
          % sorted(set(r[0] for r in big)))
    print("      L values with a small one-prime residual everywhere: %s"
          % sorted(set(r[0] for r in rows) - set(r[0] for r in big)))
    worst = max(rows, key=lambda r: abs(r[6] - r[3]))
    print("  B3: largest |E2-INTERACTION| in offenders = %d, at L = %.1f, omega = %.1e"
          % (abs(worst[6] - worst[3]), worst[0], worst[1]))
    print("      -> %s" % ("B3 HOLDS: the extra prime powers are inert to within a few offenders."
                           if abs(worst[6] - worst[3]) <= 5 else
                           "### B3 FAILS: the extra prime powers do measurable work; see B4."))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
