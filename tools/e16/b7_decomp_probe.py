"""B7(4) — THE IDENTIFICATION PROBE EXTENDED: THE SCALAR CASE DECOMPOSED. ONE CELL.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE FERRY'S ASK, AND A READING AMBIGUITY NAMED NOT SMOOTHED
===========================================================
The ferry: "re-run the scalar full-vs-mu cell with the psi-decomposition applied post hoc;
registered expectation: the +-1 lives in the psi-sum, each psi-component exact."

The scalar precedent ("within ONE offender", r = 1..8) was banked on the RATIONAL bench,
where no class group exists to decompose. The well-defined reading on the banked
instrument, REGISTERED HERE AS THE CHOICE (per the exp1 precedent of naming ferry
discrepancies): one cell, three columns side by side --

    scalar-Q : the rational bench form (lags log 2, log 3; rational coefficients C(q))
    psi_0    : the K = Q(sqrt(-23)) class-summed component (multiplier +2 both lags)
    psi_1    : the non-trivial component (multiplier -1 both lags)

each measured FULL vs exact mu, at a NEW bipartite cell L = 3.9 (same live norms as B6's
L = 3.5; wider window gives A_main more room to contribute its scalar +-1 if it is going
to). Floors applied from the start (B6's repair inherited); mu exact via Hopcroft-Karp;
bipartiteness audited per omega.

REGISTERED, BOTH BRANCHES
=========================
Q1  If ALL columns are exact (|full - mu| = 0): the scalar +-1 has NO analog at the
    bipartite cells this instrument can reach; the ferry's expectation is VACUOUSLY
    consistent there and the +-1's home remains the higher-r regime, out of reach of
    exact mu (blossom absent, declared). Reported plainly.
Q2  If a +-1 appears: report WHICH column and whether it is component-uniform
    (A_main-driven -- the class-silent archimedean part pushes the same offender into
    every component) or component-specific (lag-driven -- a finding about the lift).
    The ferry's registered expectation reads as: scalar shows the +-1, components exact.
GATE inherited: the scalar known-answer row (exp1 targets) must reproduce.

Usage:  python b7_decomp_probe.py register | run
"""
import math
import sys

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
import b6_class_probe as B6

L_CELL = 3.9
OMEGAS = [2.0e-3, 1.0e-3, 5.0e-4]


def hopcroft_karp(M, ks):
    from collections import deque
    INF = float("inf")
    colour = -np.ones(M, dtype=int)
    for s in range(M):
        if colour[s] >= 0: continue
        colour[s] = 0; st = [s]
        while st:
            v = st.pop()
            for k in ks:
                for w in (v-k, v+k):
                    if 0 <= w < M and colour[w] < 0:
                        colour[w] = 1 - colour[v]; st.append(w)
    left = [v for v in range(M) if colour[v] == 0]
    adj = {v: [w for k in ks for w in (v-k, v+k) if 0 <= w < M] for v in left}
    matchL = {v: None for v in left}; matchR = {}
    def bfs():
        dist = {}; q = deque(); found = False
        for v in left:
            if matchL[v] is None: dist[v] = 0; q.append(v)
            else: dist[v] = INF
        while q:
            v = q.popleft()
            for w in adj[v]:
                u = matchR.get(w)
                if u is None: found = True
                elif dist.get(u, INF) is INF:
                    dist[u] = dist[v] + 1; q.append(u)
        return found, dist
    def dfs(v, dist):
        for w in adj[v]:
            u = matchR.get(w)
            if u is None or (dist.get(u, INF) == dist[v] + 1 and dfs(u, dist)):
                matchL[v] = w; matchR[w] = v; return True
        dist[v] = INF; return False
    mu = 0
    while True:
        found, dist = bfs()
        if not found: break
        for v in left:
            if matchL[v] is None and dfs(v, dist): mu += 1
    return mu


def columns(cf):
    """[(name, lags)] for the three columns at the cell."""
    sq = [("log 2", math.log(2.0), cf(2, 2)), ("log 3", math.log(3.0), cf(3, 3))]
    cols = [("scalar-Q", sq)]
    for j in (0, 1):
        lg = []
        for N, p, k in [(2, 2, 1), (3, 3, 1)]:
            m = B6.multiplier(j, B6.CLASS_INDEX[p], k)
            lg.append(("logN %d" % N, math.log(N), cf(N, p) * m))
        cols.append(("psi_%d" % j, lg))
    return cols


def registration():
    W = 100
    print("=" * W)
    print("B7(4) — THE DECOMPOSITION PROBE · REGISTRATION. NO MEASURED NUMBER.")
    print("=" * W)
    print(__doc__)
    print("  columns at the cell (registered convention):")
    for name, lg in columns(E1.coeff):
        print("    %-9s %s" % (name, "  ".join("%s: %+.6f" % (l, c) for l, _, c in lg)))
    print("=" * W)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    nmax = {om: int(round(math.log(max(L_CELL, 3.0)) / om)) for om in OMEGAS}
    qvs = {om: P._qvals(om, nmax[om], E1.NG_Q) for om in OMEGAS}
    ok, _ = E1.gate(qvs, e1p)
    if not ok:
        print("\n### THE GATE DID NOT PASS. THE PROBE IS NOT RUN. THAT IS THE RESULT.")
        return
    W = 112
    for tag, cf, oms in [("REGISTERED", E1.coeff, OMEGAS), ("SENSITIVITY (Weil)", E1.coeff_weil, [1.0e-3])]:
        print("\n" + "=" * W)
        print("B7(4) — %s   ·   L = %.1f" % (tag, L_CELL))
        print("=" * W)
        print("  %-10s %-6s %-11s %-9s %-8s %-24s %-18s %s"
              % ("omega", "M", "bipartite", "column", "mu", "pure @ 0/1e-9/1e-6", "FULL", "|full-mu|"))
        for om in oms:
            M = int(round(math.log(L_CELL) / om))
            ks = [int(round(math.log(N) / om)) for N in (2, 3)]
            colour_ok, _ = B6.bipartite_audit(L_CELL, om)
            mu = hopcroft_karp(M, ks)
            for name, lg in columns(cf):
                Ap, _ = B6.pure_matrix_V(L_CELL, om, lg)
                ev = np.linalg.eigvalsh(Ap)
                sc = np.abs(ev).max()
                pure = "/".join(str(int((ev > f * sc).sum())) for f in (0.0, 1e-9, 1e-6))
                del Ap, ev
                nf, dimf, _, _ = E1.measure(L_CELL, om, lg, qvs[om], e1p)
                floored = int(pure.split("/")[1])
                print("  %-10.1e %-6d %-11s %-9s %-8d %-24s %-18s %d"
                      % (om, M, "YES" if colour_ok else "### NO", name, mu, pure,
                         "%d / %d" % (nf, dimf), abs(nf - mu)))
                sys.stdout.flush()
        print("=" * W)


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
