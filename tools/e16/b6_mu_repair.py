"""B6(c) REPAIR — the pure column re-read: exact matching number + floored pure counts.

The first run's pure column used (ev > 0) with NO spectral floor on a lag-only matrix
with an exact kernel; noise splits the kernel and inflates the count (psi_0 + psi_1
pure counts exceeded dim, impossible for exactly proportional matrices). WITHDRAWN.
The registered comparator is the MATCHING NUMBER mu, computed here exactly
(Hopcroft-Karp on the audited-bipartite union graph), plus pure counts at floors.
"""
import math
import sys
from collections import deque
import numpy as np
import exp1_two_prime as E1

L = 3.5
OMEGAS = [2.0e-3, 1.0e-3, 5.0e-4]
INF = float("inf")

def hopcroft_karp(M, ks):
    # bipartition by 2-colouring (audited bipartite)
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
    adj = {v: [] for v in left}
    for v in left:
        for k in ks:
            for w in (v-k, v+k):
                if 0 <= w < M:
                    adj[v].append(w)
    matchL = {v: None for v in left}
    matchR = {}
    def bfs():
        dist = {}
        q = deque()
        for v in left:
            if matchL[v] is None: dist[v] = 0; q.append(v)
            else: dist[v] = INF
        found = False
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

print("B6(c) REPAIR — exact mu and floored pure counts, cell L = 3.5")
print("%-10s %-6s %-8s %-30s %-30s" % ("omega","M","mu","pure psi_0 @ floors 0/1e-9/1e-6","pure psi_1 @ same"))
for om in OMEGAS:
    M = int(round(math.log(L)/om))
    ks = [int(round(math.log(N)/om)) for N in (2,3)]
    mu = hopcroft_karp(M, ks)
    outs = []
    for j in (0,1):
        lags = []
        for N,p,k in [(2,2,1),(3,3,1)]:
            m = 2.0*math.cos(2.0*math.pi*j*1*k/3.0)
            lags.append(("m", math.log(N), E1.coeff(N,p)*m))
        A, _ = __import__("b6_class_probe").pure_matrix_V(L, om, lags)
        ev = np.linalg.eigvalsh(A)
        sc = np.abs(ev).max()
        cnt = [int((ev > f*sc).sum()) for f in (0.0, 1e-9, 1e-6)]
        outs.append("/".join(map(str,cnt)))
    print("%-10.1e %-6d %-8d %-30s %-30s" % (om, M, mu, outs[0], outs[1]))
    sys.stdout.flush()
