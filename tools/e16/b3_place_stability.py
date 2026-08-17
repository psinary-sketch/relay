"""B3 — PLACE-SET STABILITY OF THE ADDRESS OBJECT.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
INSTRUMENT track. This is about the remainder route's failure COUNT only.

THE OBJECT
===========
Give the corpus's Toeplitz-on-eta apparatus a FREELY CHOSEN place-set parameter:

    S  = a finite set of PRIMES, chosen independently of the support
    Phi_{L,S} = the same form on the window of length log L, with the lag terms
                restricted to the prime powers q = p^k < L for p in S

Then the two operations B1(iv) asks about both exist on ONE object:
    widening support  = increasing L        (the forced content changes)
    ### adding a place = enlarging S        (a free choice, CC's place-set shape)

### AND CC'S OWN QUESTION, ASKED OF OUR OBJECT: is the negative count STABLE under
### enlarging S at fixed support?

WHAT THE MATCHING-NUMBER LAW ALREADY SAYS, BEFORE ANY RUN
==========================================================
Enlarging S ADDS EDGES to the shift graph and removes none. A maximum matching is
non-decreasing under adding edges. So:

    ### mu(S) IS NON-DECREASING IN S, ALWAYS -- and "stable" means exactly
    ### THE ADDED EDGES DO NOT INCREASE THE MAXIMUM MATCHING.

That is a graph-theoretic condition, not an analytic one: mu increases exactly when the
new edges create an augmenting path with respect to a maximum matching of the old graph.
### SO IF STABILITY HOLDS ANYWHERE, THE CONDITION UNDER WHICH SUPPORT-FORCED AND
### FREELY-CHOSEN COINCIDE IS ALREADY NAMEABLE, AND IT IS "NO AUGMENTING PATH".

THE EVIDENCE ALREADY IN HAND, QUOTED SO THE RUN CANNOT SURPRISE ANYONE
======================================================================
2026-08-17 measured the effect of admitting log 3 beside log 2:
    L = 9  (omega 1e-3 / 2e-3):  +285 / +143 offenders     ### NOT STABLE
    L = 12 (omega 1e-3 / 2e-3):   -1  /  +0  offenders     ### STABLE to one offender
Both at the same support-forced schedule, differing only in the window.

REGISTERED PREDICTIONS, BOTH BRANCHES LONGHAND
===============================================
P1  (BLOCKING) mu(S) is non-decreasing along every chain S_1 subset S_2 subset ...
    ### If it ever decreases, the matching computation is wrong and nothing below is read.
P2  NPOS(operator on V) tracks mu to within 3 offenders at every cell, as it has from
    r = 1.7 to r = 8.
P3  ### STABILITY IS NOT GLOBAL AND NOT ABSENT: there are steps with large Delta and steps
    with Delta = 0, at the same L or at different L.
    -> IF SO: column (iv) is priced exactly. The two axes are different kinds of thing ON
       THIS OBJECT -- enlarging S sometimes moves the count and sometimes does not, while
       widening L moves it by the sawtooth. ### The corpus's instrument is confirmed
       "two objects glued" BY ITS OWN TEST, and that is an honest MEASURED distance from T2.
    -> IF EVERY STEP IS STABLE: the free choice never moves the count, the object has CC's
       stability property, and ### that is Road B's first real handle -- the condition would
       be named and the two frames would share a theorem rather than a coordinate.
    -> IF NO STEP IS STABLE: the free choice always moves the count, stability fails
       outright, and the pair differ at a theorem. Also a clean answer.
P4  THE APEX CANDIDATE, registered as a candidate and not as a belief: the destabilising
    steps are those where the newly admitted prime enters at or near its own apex
    (L ~ p^2). ### It is registered because L = 9 = 3^2 destabilised and L = 12 did not,
    which is one instance and one non-instance -- far too little, and said so here.

WHAT IS NOT CLAIMED
====================
### NO SIGN SENTENCE. NO BOUND. Nothing here bears on W_inf - W_2. The count is a bench
quantity of a discretized form. And nothing here identifies this object with CC's --
a shared theorem would be evidence about the objects; it is not offered as an identity.

Usage:  python b3_place_stability.py register | run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
from twoshift_graph import build, components, max_matching_bipartite

LOG2 = math.log(2.0)
CELLS = [9.0, 12.0, 16.0, 27.0, 32.0]
OM = 1.0e-3
CHAIN = [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]
TOL = 3


def lags_for(L, S):
    """Prime powers q = p^k < L with p in S, as (label, ell, coefficient)."""
    out = []
    for p in S:
        k = 1
        while p ** k < L:
            q = p ** k
            lab = "log %d" % q if k == 1 else "%d log %d" % (k, p)
            out.append((lab, math.log(q), E1.coeff(q, p)))
            k += 1
    return sorted(out, key=lambda t: t[1])


def registration():
    print("=" * 116)
    print("B3 — PLACE-SET STABILITY — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 116)
    print(__doc__)
    print("  the admitted lag sets, fixed by arithmetic alone:")
    print("  %-7s %-8s %-22s %s" % ("L", "M", "S", "admitted lags (address k_q)"))
    for L in CELLS:
        M = int(round(math.log(L) / OM))
        for S in CHAIN:
            lg = lags_for(L, S)
            if not lg:
                continue
            desc = ", ".join("%s@%d" % (lab, int(round(ell / OM))) for lab, ell, _ in lg)
            print("  %-7.0f %-8d %-22s %s" % (L, M, "{" + ",".join(map(str, S)) + "}", desc))
        print()
    print("=" * 116)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    need = int(round(math.log(max(CELLS)) / OM))
    t0 = time.time()
    qv = P._qvals(OM, need, E1.NG_Q)
    print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]\n" % (OM, need, time.time() - t0))

    print("=" * 116)
    print("THE MEASUREMENT — Phi_{L,S} on V, S enlarged at FIXED support")
    print("=" * 116)
    print("  %-7s %-14s %-6s %-9s %-11s %-11s %-13s %s"
          % ("L", "S", "#lags", "mu", "NPOS", "NPOS - mu", "step in NPOS", "verdict"))
    p1_ok, p2_ok = True, True
    steps = []
    for L in CELLS:
        M = int(round(math.log(L) / OM))
        prev_npos, prev_mu = None, None
        for S in CHAIN:
            lg = lags_for(L, S)
            if not lg:
                continue
            ks = sorted({int(round(ell / OM)) for _, ell, _ in lg if 0 < int(round(ell / OM)) < M})
            adj, edges = build(M, ks)
            mu = max_matching_bipartite(M, adj)
            n, dim, frac, _ = E1.measure(L, OM, lg, qv, e1p)
            if prev_mu is not None and mu < prev_mu:
                p1_ok = False
            if abs(n - mu) > TOL:
                p2_ok = False
            step = "" if prev_npos is None else "%+d" % (n - prev_npos)
            verdict = ""
            if prev_npos is not None:
                d = n - prev_npos
                verdict = "### STABLE STEP" if abs(d) <= 1 else "### MOVES (%+d)" % d
                steps.append((L, "{" + ",".join(map(str, S)) + "}", d, len(ks)))
            print("  %-7.0f %-14s %-6d %-9d %-11d %-11s %-13s %s"
                  % (L, "{" + ",".join(map(str, S)) + "}", len(ks), mu, n,
                     "%+d" % (n - mu), step, verdict))
            prev_npos, prev_mu = n, mu
            sys.stdout.flush()
        print()

    print("=" * 116)
    print("  P1 (mu non-decreasing) : %s" % ("HOLDS" if p1_ok else "### FAILS — nothing below is read"))
    print("  P2 (NPOS tracks mu)    : %s" % ("HOLDS at every cell" if p2_ok else "### FAILS"))
    if not p1_ok:
        return
    stable = [s for s in steps if abs(s[2]) <= 1]
    moving = [s for s in steps if abs(s[2]) > 1]
    print("  P3 : %d stable steps, %d moving steps, of %d" % (len(stable), len(moving), len(steps)))
    print("       stable : %s" % ", ".join("L=%.0f %s" % (a, b) for a, b, _, _ in stable) or "none")
    print("       moving : %s" % ", ".join("L=%.0f %s (%+d)" % (a, b, d) for a, b, d, _ in moving) or "none")
    if stable and moving:
        print("  ### P3 LANDS: stability is NEITHER global NOR absent.")
    elif stable:
        print("  ### EVERY STEP STABLE — the object has the stability property.")
    else:
        print("  ### NO STEP STABLE — stability fails outright.")

    print("\n  --- P4, the apex candidate, tabulated not concluded ---")
    print("  %-7s %-14s %-9s %-13s %s" % ("L", "new prime p", "p^2", "p^2 < L ?", "step"))
    for L, Sdesc, d, _ in steps:
        newp = int(Sdesc.strip("{}").split(",")[-1])
        print("  %-7.0f %-14d %-9d %-13s %+d"
              % (L, newp, newp * newp, "yes" if newp * newp < L else "no", d))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
