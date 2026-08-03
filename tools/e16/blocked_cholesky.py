# THE INSTRUMENT (Stage A): blocked, checkpointable Cholesky for the high-dps regime.
# G = R^T R with R upper triangular, processed in row-blocks of size B; after each block
# the state (completed rows of R, dps, block index, a content hash) is saved; resume loads
# and continues.  Checkpoint format v1: JSON header line + mp.nstr rows.
import os, json, hashlib
import mpmath as mp

def _hash_rows(rows_txt):
    h = hashlib.sha256()
    for r in rows_txt:
        h.update(r.encode())
    return h.hexdigest()[:16]

def blocked_cholesky(G, n, ckpt_path, block=32, max_blocks=None):
    """Returns R (list of rows, each a list of mpf, upper triangular) or None if paused
    after max_blocks (checkpoint saved).  G is a callable (i, j) -> mpf."""
    R = []
    start = 0
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f:
            header = json.loads(f.readline())
            assert header["v"] == 1 and header["n"] == n and header["dps"] == mp.mp.dps, \
                "checkpoint/config mismatch - halt"
            rows_txt = [line.rstrip("\n") for line in f]
        assert _hash_rows(rows_txt) == header["hash"], "checkpoint hash mismatch - halt"
        for txt in rows_txt:
            R.append([mp.mpf(x) for x in txt.split()])
        start = len(R)
        print(f"[resume] loaded {start} rows from checkpoint")
    blocks_done = 0
    i = start
    while i < n:
        upto = min(i + block, n)
        for row_i in range(i, upto):
            row = [mp.mpf(0)] * n
            for j in range(row_i, n):
                s = G(row_i, j)
                for k in range(row_i):
                    s -= R[k][row_i] * R[k][j]
                if j == row_i:
                    assert s > 0, f"pivot <= 0 at {row_i} (precision floor or non-PSD) - halt"
                    piv = mp.sqrt(s)
                    row[j] = piv
                else:
                    row[j] = s / piv
            R.append(row)
        i = upto
        blocks_done += 1
        rows_txt = [" ".join(mp.nstr(x, mp.mp.dps) for x in r) for r in R]
        with open(ckpt_path, "w") as f:
            f.write(json.dumps({"v": 1, "n": n, "dps": mp.mp.dps, "rows": len(R),
                                "hash": _hash_rows(rows_txt)}) + "\n")
            for t in rows_txt:
                f.write(t + "\n")
        if max_blocks is not None and blocks_done >= max_blocks and i < n:
            print(f"[pause] {len(R)}/{n} rows banked")
            return None
    return R

def jacobi_from_R(R, depth, m0):
    al, beta = [], [m0]
    for k in range(depth):
        t1 = R[k][k + 1] / R[k][k]
        t0 = R[k - 1][k] / R[k - 1][k - 1] if k >= 1 else mp.mpf(0)
        al.append(t1 - t0)
        if k >= 1:
            beta.append((R[k][k] / R[k - 1][k - 1]) ** 2)
    return al, beta

def selftest():
    """Resume test on a deliberately interrupted small run BEFORE production (the gate)."""
    mp.mp.dps = 150
    n = 12
    atoms = [mp.mpf(1) / (j + 2) for j in range(60)]
    s = [None] + [sum(a ** k * a for a in atoms) for k in range(2 * n + 2)]
    Gf = lambda i, j: s[i + j + 1]
    ck = os.path.join(os.environ.get("TEMP", "."), "bc_selftest.ckpt")
    if os.path.exists(ck): os.remove(ck)
    r1 = blocked_cholesky(Gf, n, ck, block=4, max_blocks=1)   # deliberate interrupt
    assert r1 is None, "expected pause"
    R = blocked_cholesky(Gf, n, ck, block=4)                  # resume to completion
    Gm = mp.matrix(n, n)
    for i in range(n):
        for j in range(n): Gm[i, j] = s[i + j + 1]
    Rd = mp.cholesky(Gm).T
    worst = max(abs(R[i][j] - Rd[i, j]) / (abs(Rd[i, j]) + mp.mpf(10) ** (-50))
                for i in range(n) for j in range(i, n))
    os.remove(ck)
    print(f"[selftest] interrupted+resumed vs direct: worst rel {mp.nstr(worst, 3)} "
          f"({'PASS' if worst < mp.mpf(10) ** (-40) else 'FAIL - HALT'})")
    return worst < mp.mpf(10) ** (-40)

if __name__ == "__main__":
    selftest()
