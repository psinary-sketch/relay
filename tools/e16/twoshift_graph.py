"""THE TWO-SHIFT GRAPH — theory first, then one discriminating cell each at L = 9 and L = 12.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE OBJECT
===========
Two lags live: k2 = round(log 2 / omega) and k3 = round(log 3 / omega). The lag part of the
form is c2*S_{k2} + c3*S_{k3}, where (S_k)_{ij} = 1 iff |i-j| = k. Read as a graph G on
{0,...,M-1}: an edge i ~ i+k2 and an edge i ~ i+k3, wherever both endpoints fit.

WHAT CAN BE DERIVED, AND IT IS MORE THAN THE ONE-LAG CASE GAVE
===============================================================
STEP 1 — COMPONENTS. On Z the steps generate d*Z with d = gcd(k2, k3), so components refine
into the d residue classes mod d. On the finite segment a class need not be connected: moving
by d requires a Bezout combination whose intermediate points all stay inside [0, M).
### SO THE COMPONENT COUNT IS NOT gcd ALONE — it is gcd together with whether M is long
### enough to realise the combination. Measured below, not assumed.

STEP 2 — CYCLES, AND THE RATIO'S CONVERGENTS. A cycle is a closed walk with
a*k2 - b*k3 = 0, a,b >= 0 not both zero. The minimal solution is a = k3/d, b = k2/d, whose
all-plus-then-all-minus realisation spans lcm(k2, k3). Interleaving can shorten the span, and
how much it can shorten is exactly the theory of the continued fraction of k3/k2 -- a good
rational approximation p/q to k3/k2 means q*k3 ~ p*k2, i.e. a NEARLY closed short walk.
### THE CONVERGENTS OF log 3 / log 2 ARE THEREFORE WHAT DECIDE WHETHER A WINDOW IS LONG
### ENOUGH TO CARRY A CYCLE AT ALL. Both are printed below.

STEP 3 — AND IF THERE ARE NO CYCLES, THE COUNT IS A MATCHING NUMBER.
    * a forest is bipartite, so its (weighted) adjacency spectrum is symmetric about 0;
    * for a FOREST with all edge weights nonzero, rank = 2*mu, where mu is the maximum
      matching number.
Together: ### inertia = (mu, mu, M - 2mu), so NPOS = mu -- AND IT DOES NOT DEPEND ON THE
### EDGE WEIGHTS AT ALL, only on which edges exist.

    THE RANK IDENTITY IS CLASSICAL AND IS CITED, NOT PROVED HERE (Cvetkovic-Gutman for
    unweighted forests; the weighted case follows because a tree has at most one perfect
    matching, so a weighted principal minor is nonzero exactly when the unweighted one is).
    ### IT IS CHECKED NUMERICALLY AT EVERY CELL BELOW rather than taken on trust.

STEP 4 — THE ONE-LAG CASE IS THE SPECIAL CASE, AND THE OLD FORMULA FALLS OUT.
With a single lag the graph is a disjoint union of PATHS, mu(P_m) = floor(m/2), and
    sum_r floor(m_r/2) = (M - #odd-length chains)/2,
### which is exactly the sawtooth formula. The matching statement is the same theorem said
### in a way that survives a second lag.

STEP 5 — AND IT ANSWERS WONDER TWO FOR THE PURE FORM, WHICH SYLVESTER DID NOT.
Sylvester gave only that a COMMON factor cannot move the count. ### The forest identity gives
### that NO choice of nonzero coefficients can move it -- the shape direction as well as the
### scale direction. The 2026-08-17 measurement of -1, -2, -2 offenders under the convention
change is then entirely A_main's, not the weights'.

WHAT CANNOT BE DERIVED HERE, NAMED EXACTLY
===========================================
### IF THE GRAPH HAS A CYCLE, rank = 2*mu CAN FAIL and there is no closed form for the
### nullity that this sitting can derive. Bipartiteness -- hence the symmetric spectrum and
### the halving -- survives whenever k2 and k3 are both ODD (a closed walk then has an even
number of steps, since a sum of odd numbers vanishes only with evenly many terms), but the
nullity itself does not. That case is reported if it occurs, not guessed at.

THE CELLS, AND THE PREDICTIONS ARE PRINTED BEFORE ANY MEASUREMENT
=================================================================
L = 9  -- the ratio-integer window: log 9 = 2 log 3, so the window is exactly the log-3 lag's
          own apex, and both lags are live.
L = 12 -- both lags live, no arithmetic coincidence between window and lag.
At omega = 1e-3 and 2e-3, which differ in gcd(k2,k3) and so test STEP 1 directly.

REGISTERED, both branches longhand:
  T1  the graph is a FOREST at every cell (edges = M - components, checked exactly);
  T2  mu computed combinatorially equals NPOS of the pure two-shift form computed
      numerically, at the registered coefficients AND at unit coefficients AND at the Weil
      coefficients -- ### three weightings, one count;
  T3  the FULL OPERATOR on V lands within 3 offenders of mu.
  IF T1 fails: a cycle fits in the window, the matching identity is off the table there, and
  the sitting reports the component/cycle structure and stops -- no count is predicted.
  IF T2 fails while T1 holds: the rank identity does not apply as cited, which would be a
  finding about the citation and is reported as one.
  IF T3 fails while T1 and T2 hold: the pure form is understood and the remainder is not,
  which localises A_main's contribution to a named window rather than leaving it general.

Usage:  python twoshift_graph.py register | run
"""
import math
import sys
import time
from fractions import Fraction

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2, LOG3 = math.log(2.0), math.log(3.0)
CELLS = [(9.0, 1.0e-3), (9.0, 2.0e-3), (12.0, 1.0e-3), (12.0, 2.0e-3)]
TOL = 3


def cf(x, n=12):
    out = []
    for _ in range(n):
        a = math.floor(x)
        out.append(int(a))
        x -= a
        if x < 1e-13:
            break
        x = 1.0 / x
    return out


def convergents(terms):
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    out = [(p1, q1)]
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        out.append((p1, q1))
    return out


def build(M, ks):
    """adjacency lists for the shift graph on M points with shifts ks."""
    adj = [[] for _ in range(M)]
    edges = 0
    for k in ks:
        for i in range(M - k):
            adj[i].append(i + k)
            adj[i + k].append(i)
            edges += 1
    return adj, edges


def components(M, adj):
    seen = [False] * M
    comps = 0
    for s in range(M):
        if seen[s]:
            continue
        comps += 1
        stack = [s]
        seen[s] = True
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if not seen[w]:
                    seen[w] = True
                    stack.append(w)
    return comps


def max_matching_bipartite(M, adj):
    """Maximum matching by augmenting paths. Valid for any BIPARTITE graph, not just forests.

    Both shifts are odd at every cell here, so every edge joins an even index to an odd one
    and the parity of the index IS the bipartition — no search for one is needed.
    """
    matchL = [-1] * M
    matchR = [-1] * M
    mu = 0
    for s in range(0, M, 2):
        if matchL[s] != -1:
            continue
        visited = bytearray(M)
        prev = {}
        stack = [(s, iter(adj[s]))]
        found = -1
        while stack:
            v, it = stack[-1]
            nxt = -1
            for w in it:
                if not visited[w]:
                    nxt = w
                    break
            if nxt < 0:
                stack.pop()
                continue
            visited[nxt] = 1
            prev[nxt] = v
            if matchR[nxt] == -1:
                found = nxt
                break
            stack.append((matchR[nxt], iter(adj[matchR[nxt]])))
        if found >= 0:
            w = found
            while True:
                v = prev[w]
                nw = matchL[v]
                matchL[v] = w
                matchR[w] = v
                if nw == -1:
                    break
                w = nw
            mu += 1
    return mu


def pure_inertia(M, ks, coeffs):
    A = np.zeros((M, M))
    for k, c in zip(ks, coeffs):
        idx = np.arange(M - k)
        A[idx + k, idx] += c
        A[idx, idx + k] += c
    ev = np.linalg.eigvalsh(A)
    tol = 1e-9 * max(1.0, float(np.abs(ev).max()))
    return int((ev > tol).sum()), int((ev < -tol).sum()), int((np.abs(ev) <= tol).sum())


def structure_line(L, om):
    M = int(round(math.log(L) / om))
    k2, k3 = int(round(LOG2 / om)), int(round(LOG3 / om))
    d = math.gcd(k2, k3)
    adj, edges = build(M, [k2, k3])
    comps = components(M, adj)
    forest = (edges == M - comps)
    return M, k2, k3, d, edges, comps, forest, adj


def registration():
    print("=" * 116)
    print("THE TWO-SHIFT GRAPH — REGISTRATION. NO MEASURED SPECTRUM IN THIS BLOCK.")
    print("=" * 116)
    print(__doc__)
    print("-" * 116)
    print("THE RATIO AND ITS CONVERGENTS (arithmetic only — no operator, no spectrum)")
    print("-" * 116)
    terms = cf(LOG3 / LOG2)
    print("  log 3 / log 2 = %.12f" % (LOG3 / LOG2))
    print("  continued fraction: %s" % terms)
    print("  convergents p/q  : %s"
          % ", ".join("%d/%d" % (p, q) for p, q in convergents(terms)[:8]))
    print()
    print("  %-7s %-9s %-7s %-7s %-6s %-9s %-11s %-11s %s"
          % ("L", "omega", "M", "k2", "k3", "gcd", "edges", "components", "forest? (edges = M - comps)"))
    for L, om in CELLS:
        M, k2, k3, d, edges, comps, forest, _ = structure_line(L, om)
        print("  %-7.1f %-9.1e %-7d %-7d %-6d %-9d %-11d %-11d %s"
              % (L, om, M, k2, k3, d, edges, comps,
                 "### FOREST" if forest else "### HAS %d INDEPENDENT CYCLES" % (edges - M + comps)))
        print("        lcm(k2,k3) = %d  (the all-plus-then-all-minus cycle's span; M = %d)"
              % (k2 * k3 // d, M))
        print("        k3/k2 = %s in lowest terms -> minimal relation %d*k2 = %d*k3"
              % (Fraction(k3, k2), k3 // d, k2 // d))
    print("=" * 116)

    # ------------------------------------------------------------------ addendum
    print()
    print("=" * 116)
    print("ADDENDUM — ### T1 IS REFUTED BY THIS REGISTRATION BLOCK ITSELF, ON ARITHMETIC,")
    print("BEFORE ANY SPECTRUM IS COMPUTED. WHAT REPLACES IT IS REGISTERED HERE.")
    print("=" * 116)
    print("""
### THE GRAPHS ARE NOT FORESTS. Every cell carries hundreds of independent cycles.

### AND MY REASON FOR EXPECTING A FOREST WAS WRONG IN A NAMEABLE WAY. I argued from
### lcm(k2,k3) = 108801 >> M = 2197 that no cycle could fit. That bounds the span of the
### all-plus-then-all-minus realisation and NOTHING ELSE. A cycle needs its PARTIAL SUMS to
### stay in [0, M), not its total displacement to be small -- and an interleaved walk
### (+k2, +k2, -k3, ...) drifts by only 2*k2 - k3 = 287 per period at omega = 1e-3, so a
### 256-step cycle sits comfortably inside a 2197-point window.
### THE MINIMAL RELATION BOUNDS THE CYCLE'S LENGTH IN EDGES (157 + 99 = 256), NOT ITS SPAN
### IN VERTICES. I conflated the two. Named here, before it could contaminate a verdict.

WHAT SURVIVES, AND IT IS REGISTERED NOW WITH NO SPECTRUM YET COMPUTED:

T1'  ### BIPARTITENESS SURVIVES, AND IT IS DERIVED, NOT MEASURED. k2 and k3 are BOTH ODD at
     every cell (693, 1099 at omega=1e-3; 347, 549 at 2e-3). Every edge therefore joins an
     even index to an odd one, so the parity of the index IS a bipartition, so the graph is
     bipartite whatever its cycles. Hence the weighted adjacency spectrum is SYMMETRIC about
     zero and ### NPOS = NNEG = (M - nullity)/2 still holds.
     ### TESTABLE: NPOS == NNEG at every cell and every weighting. If that fails the
     bipartite argument is wrong and nothing else in this file may be read.

T2'  ### WEIGHT-INDEPENDENCE IS NOW GENUINELY OPEN, AND THAT IS THE POINT OF RUNNING IT.
     The forest identity rank = 2*mu was the whole reason to expect the count not to move
     with the coefficients, and it does not apply once cycles exist: for a bipartite graph
     with cycles, rank >= 2*mu with equality NOT guaranteed, and the rank can depend on the
     weights (a cycle's weighted determinant can vanish for special weights).
       IF the three weightings -- registered, unit, Weil -- give the SAME NPOS at every cell,
       then weight-independence holds well beyond forests here, it needs an explanation this
       sitting does not have, and Wonder Two's silence is broader than its proof.
       IF they DIFFER, then the coefficient question is LIVE for two lags in a way it was not
       for one, and the one-lag silence was a property of paths rather than of the mechanism.

T2'' mu is computed anyway, for every cell, by augmenting paths on the parity bipartition.
     ### THE COMPARISON mu vs NPOS IS NOW A MEASUREMENT OF HOW FAR rank = 2*mu SURVIVES
     ### CYCLES, not an assumption. Registered expectation: NPOS >= mu, with equality not
     expected once cycles are present.

T3'  the FULL OPERATOR on V, both lags, against the pure form's own NPOS (not against mu).
     ### This is the only cell-level prediction that survives T1's refutation, and it is the
     one the ferry chartered: the pure two-lag form's count, with full-operator agreement
     bench-grade until the remainder is controlled.
""")
    print("=" * 116)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("=" * 116)
    print("T1 / T2 — THE PURE TWO-SHIFT FORM: structure, matching number, and three weightings")
    print("=" * 116)
    print("  %-7s %-9s %-7s %-9s %-9s %-11s %-11s %-11s %s"
          % ("L", "omega", "M", "forest", "mu", "NPOS reg", "NPOS unit", "NPOS Weil", "nullity"))
    mus = {}
    for L, om in CELLS:
        M, k2, k3, d, edges, comps, forest, adj = structure_line(L, om)
        mu = max_matching_bipartite(M, adj)
        cr = [E1.coeff(2, 2), E1.coeff(3, 3)]
        cu = [1.0, 1.0]
        cw = [E1.coeff_weil(2, 2), E1.coeff_weil(3, 3)]
        nr = pure_inertia(M, [k2, k3], cr)
        nu = pure_inertia(M, [k2, k3], cu)
        nw = pure_inertia(M, [k2, k3], cw)
        mus[(L, om)] = (mu, nr[0])
        print("  %-7.1f %-9.1e %-7d %-9s %-9d %-11d %-11d %-11d %d/%d/%d"
              % (L, om, M, "YES" if forest else "NO", mu, nr[0], nu[0], nw[0],
                 nr[2], nu[2], nw[2]))
        sym = (nr[0] == nr[1] and nu[0] == nu[1] and nw[0] == nw[1])
        same = (nr[0] == nu[0] == nw[0])
        print("        T1  %s   T1' bipartite/symmetric %s   T2' weight-independent %s"
              % ("forest" if forest else "### NOT A FOREST (refuted at registration)",
                 "HOLDS (NPOS = NNEG at all three weightings)" if sym else "### FAILS",
                 "HOLDS — one count, three weightings" if same else "### FAILS"))
        print("        T2'' mu = %d, NPOS = %d, NPOS - mu = %+d ; M - 2mu = %d vs measured nullity %d"
              % (mu, nr[0], nr[0] - mu, M - 2 * mu, nr[2]))
        sys.stdout.flush()

    print("\n" + "=" * 116)
    print("T3 — THE FULL OPERATOR ON V, both lags live")
    print("=" * 116)
    print("  %-7s %-9s %-7s %-14s %-11s %-11s %-12s %s"
          % ("L", "omega", "M", "measured", "pure form", "one-lag", "meas - pure", "verdict"))
    for L, om in CELLS:
        M = int(round(math.log(L) / om))
        qv = P._qvals(om, M, E1.NG_Q)
        full = [x for x in E1.lag_schedule(L) if x[0] in ("log 2", "log 3")]
        one = [x for x in full if x[0] == "log 2"]
        n2, dim, f2, _ = E1.measure(L, om, full, qv, e1p)
        n1, _, f1, _ = E1.measure(L, om, one, qv, e1p)
        mu, pure = mus[(L, om)]
        print("  %-7.1f %-9.1e %-7d %-14s %-11d %-11d %-12s %s"
              % (L, om, M, "%d/%d" % (n2, dim), pure, n1, "%+d" % (n2 - pure),
                 "### LANDS" if abs(n2 - pure) <= TOL else "### FAILS"))
        print("        two-lag fraction %.6f   one-lag %.6f   interaction %+d offenders"
              % (f2, f1, n2 - n1))
        sys.stdout.flush()
        del qv


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
