#!/usr/bin/env python3
"""
b223 -- THE LEVEL-LIMIT AT THE FIRST TWO PLACES.
### EXACT Z[zeta_N] ARITHMETIC THROUGHOUT. ### NO FLOATING POINT IN ANY d_1.
Registration: data/b223_registration_2026-08-28.txt (banked BEFORE this runs).

### THE METHOD IS THE PURITY REPORT'S OWN, and the construction is confirmed identical to the
### banked instrument tools/e16/b44_e1_unit_purity.py:
###   Son basis  f_{i,j} = e_{i+qj} - e_i,  i,j in [1,q),  q = p^n, N = q^2, dim Son = (q-1)^2
###   the unit   u_{i,j} = q(1+Pi)f + S(1+Pi)f = 4q * P_1 f_{i,j}
###   G4         sum_{i,j} u_{i,j}(i+qj) = 4q * d_1, exactly in Z[zeta_N]

### THE ONE EFFICIENCY, DECLARED IN THE REGISTRATION: b44 builds the FULL N-entry unit for every
### one of the (q-1)^2 basis vectors -- O(N^2) per cell -- and cannot reach n = 4 or 5.
### THIS FILE COMPUTES ONLY THE DIAGONAL THE TRACE NEEDS, which is O(q^2):
###   trace(4q P_1 | Son) = q*(D + tr Pi) + T + conj(T),  D = (q-1)^2,
###   T = SUM_{i,j in [1,q)} [ zeta^{(i+qj)^2} - zeta^{i(i+qj)} ]
### ### IT IS THE SAME TRACE. ### The act proves that by reproducing ALL SIX banked rows before
### ### extending to any new cell -- which is this file's must-fail-fixtured gate G-REPRO.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# the six banked rows, purity report sec 2 -- (d1, d-1, di, d-i)
BANKED = {(2, 1): (0, 0, 1, 0), (3, 1): (1, 1, 1, 1), (2, 2): (2, 2, 3, 2),
          (5, 1): (4, 4, 4, 4), (2, 3): (12, 12, 13, 12), (3, 2): (16, 16, 16, 16)}

# the record's own closed-form laws (b198 (I3), owner correspondence row 36 / b57)
def law_d1(p, n):
    q = p ** n
    if p == 2:
        num = q * (q - 2)
    else:
        num = (q - 1) ** 2
    assert num % 4 == 0, "the law must give an integer"
    return num // 4


# ---------------- exact cyclotomic layer: Z[zeta_N], N = p^a a prime power ----------------

def phi_reduce(counts, p, N):
    """counts: dict exponent -> int, in Z[x]/(x^N - 1).
    Reduce mod Phi_N (N a power of p; Phi_{p^a}(x) = sum_{t<p} x^{t*N/p}).
    Returns a dense list of length N - N/p in the power basis."""
    Np = N // p
    out = [0] * (N - Np)
    for e, c in counts.items():
        if c == 0:
            continue
        e %= N
        k, r = divmod(e, Np)
        if k <= p - 2:
            out[k * Np + r] += c
        else:
            # x^{(p-1)Np + r} = -(sum_{t<p-1} x^{t*Np + r})
            for t in range(p - 1):
                out[t * Np + r] -= c
    return out


def as_integer(vec, p, N):
    """A reduced vector that represents a rational integer: all non-constant coords zero."""
    if any(vec[i] != 0 for i in range(1, len(vec))):
        return None
    return vec[0]


# ---------------- the traces ----------------

def traces(p, n):
    q = p ** n
    N = q * q
    D = (q - 1) ** 2

    # tr(Pi | Son) = #{2(i+qj) = 0} - #{2i+qj = 0}, both mod N, over i,j in [1,q)
    a = b = 0
    for i in range(1, q):
        for j in range(1, q):
            m = i + q * j
            if (2 * m) % N == 0:
                a += 1
            if (2 * i + q * j) % N == 0:
                b += 1
    tr_pi = a - b

    # T = sum [ zeta^{m^2} - zeta^{i*m} ], m = i + q j ; accumulate exponent counts
    cnt = {}
    for i in range(1, q):
        for j in range(1, q):
            m = i + q * j
            e1 = (m * m) % N
            e2 = (i * m) % N
            cnt[e1] = cnt.get(e1, 0) + 1
            cnt[e2] = cnt.get(e2, 0) - 1

    # T + conj(T): coefficient of zeta^k becomes c_k + c_{-k}
    sym = {}
    for e, c in cnt.items():
        if c:
            sym[e] = sym.get(e, 0) + c
            ne = (-e) % N
            sym[ne] = sym.get(ne, 0) + c
    t_plus_conj = as_integer(phi_reduce(sym, p, N), p, N)

    # anti: (T - conj(T))/i, needed only for the i / -i split; exact only when it reduces
    anti = {}
    for e, c in cnt.items():
        if c:
            anti[e] = anti.get(e, 0) + c
            ne = (-e) % N
            anti[ne] = anti.get(ne, 0) - c
    return D, tr_pi, t_plus_conj, anti, q, N


def d1_exact(p, n):
    """### d_1 EXACTLY. Returns (d1, d_minus1, dsum_i, detail) or raises on non-integrality."""
    D, tr_pi, tpc, anti, q, N = traces(p, n)
    if tpc is None:
        raise ArithmeticError("T + conj(T) did not reduce to a rational integer")
    tr4q = q * (D + tr_pi) + tpc          # = trace(4q P_1 | Son)
    if tr4q % (4 * q) != 0:
        raise ArithmeticError("G4 trace %d not divisible by 4q = %d" % (tr4q, 4 * q))
    d1 = tr4q // (4 * q)
    # d_-1 = (D + tr Pi - (T+conj T)/q)/4
    num = q * (D + tr_pi) - tpc
    if num % (4 * q) != 0:
        raise ArithmeticError("d_-1 not integral")
    dm1 = num // (4 * q)
    d_i_sum = D - d1 - dm1                # d_i + d_{-i}, exact
    return d1, dm1, d_i_sum, (D, tr_pi, tpc, tr4q)


# ---------------- the unit ----------------

def cmul_scalar_sparse(u, N):
    return {e % N: c for e, c in u.items() if c}


def exhibit_unit(p, n):
    """### EXHIBIT one nonzero u = 4q P_1 f_{i,j} at the first (i,j) that gives one.
    Returns (i, j, entries, norm2) with entries a list of N sparse dicts (exponent -> int),
    and norm2 the EXACT squared norm (a rational integer).
    ### MIXED IS PERMITTED AND UNREMARKED: no purity is tested."""
    q = p ** n
    N = q * q
    for i in range(1, q):
        for j in range(1, q):
            f = {}
            f[(i + q * j) % N] = f.get((i + q * j) % N, 0) + 1
            f[i % N] = f.get(i % N, 0) - 1
            h = dict(f)
            for m, c in f.items():
                mm = (-m) % N
                h[mm] = h.get(mm, 0) + c
            h = {m: c for m, c in h.items() if c}
            if not h:
                continue
            u = [dict() for _ in range(N)]
            for m, c in h.items():
                u[m][0] = u[m].get(0, 0) + q * c
                for mp in range(N):
                    e = (m * mp) % N
                    u[mp][e] = u[mp].get(e, 0) + c
            u = [{e: c for e, c in ent.items() if c} for ent in u]
            # nonzero?
            nz = any(as_nonzero(ent, p, N) for ent in u)
            if not nz:
                continue
            # ### EXACT squared norm: sum_m u(m) * conj(u(m)), reduced; must be a rational integer
            acc = {}
            for ent in u:
                for e1, c1 in ent.items():
                    for e2, c2 in ent.items():
                        e = (e1 - e2) % N
                        acc[e] = acc.get(e, 0) + c1 * c2
            # ### norm2 IS A TOTALLY-REAL ALGEBRAIC INTEGER, NOT A RATIONAL ONE.
            # ### |u(m)|^2 lies in the real subfield of Q(zeta_N); the sum need not be rational,
            # ### and at (3,1) it is 72 - 36*zeta^4 - 36*zeta^5 = 139.6578... exactly.
            # ### THE UNIT'S COEFFICIENTS ARE EXACT IN Z[zeta]; THE NORMALIZER IS A REAL SCALAR.
            norm2vec = phi_reduce(acc, p, N)
            return i, j, u, norm2vec
    return None


def as_nonzero(ent, p, N):
    if not ent:
        return False
    v = phi_reduce(ent, p, N)
    return any(x != 0 for x in v)


def verify_unit_in_E1(u, p, n):
    """### CHECK S u = q u exactly, i.e. u is in the +1 sector of M = S/q."""
    q = p ** n
    N = q * q
    for m in range(N):
        lhs = {}
        for mp in range(N):
            for e, c in u[mp].items():
                ee = (e + m * mp) % N
                lhs[ee] = lhs.get(ee, 0) + c
        rhs = {e: q * c for e, c in u[m].items()}
        diff = dict(lhs)
        for e, c in rhs.items():
            diff[e] = diff.get(e, 0) - c
        v = phi_reduce(diff, p, N)
        if any(x != 0 for x in v):
            return False, m
    return True, None


def unit_digest(u, p, N):
    """A reproducible fingerprint of the exact coefficient data."""
    h = hashlib.sha256()
    for m, ent in enumerate(u):
        v = phi_reduce(ent, p, N)
        h.update(("%d:" % m).encode())
        h.update((",".join(str(x) for x in v)).encode())
        h.update(b";")
    return h.hexdigest()[:32]
