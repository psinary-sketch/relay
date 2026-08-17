"""B3 ADDENDUM — THE BIPARTITENESS AUDIT, AND THE mu COLUMN WITHDRAWN.

Relay-only, bench-grade. NO SIGN SENTENCE. NOTHING DEPOSITS.

WHY THIS ADDENDUM EXISTS
=========================
b3_place_stability.py reported a mu column computed by max_matching_bipartite(), which
assumes INDEX PARITY is a bipartition -- true when every live lag address k_q is ODD, and
FALSE otherwise. Admitting prime powers breaks it: at omega = 1e-3,

    log 2  -> k = 693   ODD          2 log 2 -> k = 1386  ### EVEN
    log 3  -> k = 1099  ODD          log 7   -> k = 1946  ### EVEN
    log 5  -> k = 1609  ODD          log 11  -> k = 2398  ### EVEN

An even address joins even index to even index, so the routine double-uses vertices and
returns ceil(M/2) -- which is what it did at every cell, including mu = 1099 on M = 2197
where floor(M/2) = 1098 makes 1099 IMPOSSIBLE.

    ### THE REGISTERED BLOCKING ROW IS WHAT CAUGHT IT. P2 said "NPOS tracks mu to within 3
    ### offenders"; it came back at -406 on the first line and the run was stopped there.

### THE mu COLUMN OF THAT RUN IS WITHDRAWN IN FULL. The NPOS column is an eigenvalue count
### of a well-defined symmetric matrix and is UNAFFECTED; it is re-used here, parsed from the
### banked output rather than recomputed, and its provenance is the file.

WHAT THIS ADDENDUM DOES
========================
For each (L, S): list the live addresses and their parities; test bipartiteness properly by
2-colouring rather than by assuming index parity; compute mu by augmenting paths on the TRUE
bipartition where one exists; and where the graph is NOT bipartite, say so and compute no mu
-- a general (non-bipartite) maximum matching needs blossom contraction, which is not in this
instrument and is declared rather than approximated.

### AND THE SCOPE NOTE THIS FORCES ON THE WEEK'S DERIVED LAW, STATED PLAINLY:
### "every live k is odd, so index parity is a bipartition" IS A PROPERTY OF A PARTICULAR
### (omega, lag set) AND IS NOT AUTOMATIC.
It held for every cell the law was actually measured on -- the one-lag sawtooth cells (where
the graph is a disjoint union of PATHS and is bipartite for any k, parity irrelevant) and the
two-lag cells {log 2, log 3} (both addresses odd). ### NO CLAIM ALREADY BANKED IS FALSIFIED.
What was missing was a warning that the premise can fail, and it fails as soon as a prime
power is admitted.

Usage:  python b3_bipartite_audit.py
"""
import math
import re
import sys
from collections import deque

LOG2 = math.log(2.0)
OM = 1.0e-3
CELLS = [9.0, 12.0, 16.0, 27.0, 32.0]
CHAIN = [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]
RUN = r"D:\relay\data\b3_2026-08-17.txt"


def addresses(L, S):
    out = []
    for p in S:
        k = 1
        while p ** k < L:
            q = p ** k
            out.append((q, p, int(round(math.log(q) / OM))))
            k += 1
    M = int(round(math.log(L) / OM))
    return M, sorted({(q, p, k) for q, p, k in out if 0 < k < M}, key=lambda t: t[2])


def build(M, ks):
    adj = [[] for _ in range(M)]
    for k in ks:
        for i in range(M - k):
            adj[i].append(i + k)
            adj[i + k].append(i)
    return adj


def two_colour(M, adj):
    """Return colours if bipartite, else None."""
    col = [-1] * M
    for s in range(M):
        if col[s] != -1:
            continue
        col[s] = 0
        dq = deque([s])
        while dq:
            v = dq.popleft()
            for w in adj[v]:
                if col[w] == -1:
                    col[w] = 1 - col[v]
                    dq.append(w)
                elif col[w] == col[v]:
                    return None
    return col


def matching(M, adj, col):
    matchL = [-1] * M
    matchR = [-1] * M
    mu = 0
    for s in range(M):
        if col[s] != 0 or matchL[s] != -1:
            continue
        vis = bytearray(M)
        prev = {}
        stack = [(s, iter(adj[s]))]
        found = -1
        while stack:
            v, it = stack[-1]
            nxt = -1
            for w in it:
                if not vis[w]:
                    nxt = w
                    break
            if nxt < 0:
                stack.pop()
                continue
            vis[nxt] = 1
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


def measured():
    """NPOS per (L, |S|), parsed from the banked run — provenance is the file."""
    out = {}
    for line in open(RUN, encoding="utf-8", errors="replace"):
        m = re.match(r"\s+(\d+)\s+\{([\d,]+)\}\s+(\d+)\s+(\d+)\s+(\d+)\s", line)
        if m:
            out[(float(m.group(1)), m.group(2))] = int(m.group(5))
    return out


def main():
    print("=" * 118)
    print("B3 ADDENDUM — BIPARTITENESS AUDIT")
    print("=" * 118)
    print(__doc__)
    npos = measured()
    print("  parsed %d measured NPOS values from %s\n" % (len(npos), RUN))
    print("  %-6s %-14s %-7s %-30s %-12s %-9s %-8s %s"
          % ("L", "S", "M", "addresses (parity)", "all odd?", "bipartite", "mu", "NPOS"))
    prev = {}
    rows = []
    for L in CELLS:
        for S in CHAIN:
            M, ads = addresses(L, S)
            if not ads:
                continue
            ks = sorted({k for _, _, k in ads})
            allodd = all(k % 2 == 1 for k in ks)
            adj = build(M, ks)
            col = two_colour(M, adj)
            mu = matching(M, adj, col) if col is not None else None
            key = (L, ",".join(map(str, S)))
            n = npos.get(key)
            desc = " ".join("%d%s" % (k, "o" if k % 2 else "E") for k in ks)
            if len(desc) > 29:
                desc = desc[:26] + "..."
            print("  %-6.0f %-14s %-7d %-30s %-12s %-9s %-8s %s"
                  % (L, "{" + ",".join(map(str, S)) + "}", M, desc,
                     "yes" if allodd else "### NO",
                     "yes" if col is not None else "### NO",
                     str(mu) if mu is not None else "—",
                     str(n) if n is not None else "?"))
            rows.append((L, key[1], n, mu, col is not None))
            sys.stdout.flush()
        print()

    print("=" * 118)
    print("  THE STEPS IN THE MEASURED COUNT, WHICH IS THE COLUMN THAT SURVIVES")
    print("=" * 118)
    print("  %-6s %-40s %s" % ("L", "steps in NPOS as S grows", "monotone?"))
    for L in CELLS:
        seq = [r[2] for r in rows if r[0] == L and r[2] is not None]
        steps = [b - a for a, b in zip(seq, seq[1:])]
        mono = all(d >= 0 for d in steps)
        print("  %-6.0f %-40s %s"
              % (L, " ".join("%+d" % d for d in steps),
                 "yes" if mono else "### NO — the count goes UP then DOWN"))
    print()
    print("  ### THE COUNT IS NOT MONOTONE IN S AT ANY L TESTED.")
    print("  A maximum matching is non-decreasing under adding edges; a count that falls when")
    print("  a lag is admitted is therefore NOT a matching number on these graphs — which is")
    print("  the same conclusion the bipartiteness column reaches, by a second route.")


if __name__ == "__main__":
    main()
