"""B8(1) — THE DIMENSION CHECK: the local Sonin model at a finite place. PRICED, NOW RUN.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE MODEL, DECLARED
===================
Functions on the finite quotient G = p^{-n} Z_p / p^n Z_p, identified with Z/p^{2n} via
x = p^{-n} m. Fourier transform = the DFT of size N = p^{2n} with kernel e^{2 pi i mk / N}
(the standard additive character of conductor Z_p descends to this pairing). The INTEGERS'
BALL B = {|x|_p <= 1} = {m == 0 mod p^n}, |B| = p^n.

THE CANDIDATE SPACE (section 8.3's candidate, transposed to the model):
    Son(p, n) = { f : f|_B = 0  and  (DFT f)|_B = 0 }.

The scaling action theta_p on L2(K_p) is (U f)(x) = p^{-1/2} f(p x); on the model it is
m -> p*m mod N with the |p|^{1/2} normalization -- the truncation of the unitary scaling;
edge effects at the outer shell are a declared model artifact.

REGISTERED QUANTITIES AND VERDICT MAP (before any number)
=========================================================
D   dim Son(p, n) for p in {2, 3, 5}, n in {1, 2}, plus the shell-support profile.
Q   the compressed-action mass Q(p, n) = ||S U S||_F, S = orthoprojection onto Son(p, n).
W   IF Q > 0: the p-scaling of Q at fixed n across p = 2, 3, 5 (fitted power alpha in
    Q ~ p^alpha), reported as measured. "Weight-carrying at model grade" means a nonzero
    fitted power consistent with a q^{+-1/2}-type coefficient; log p itself is the lag
    UNIT (the orbit spacing) and is carried by the time normalization, declared not
    measured. The two banked coefficient conventions disagree in the SIGN of the power
    ("nothing in the banked record separates them" -- exp1's registration); this bench
    reports the measured power and adjudicates no convention.

VERDICTS (the ferry's three, mapped):
    TRIVIAL                       dim = 0 at every cell             -> E2 first face
    NON-TRIVIAL, WEIGHT-SILENT    dim > 0 but Q = 0 (the compressed
                                  action dies on the space), or no
                                  systematic p-power                -> E2 second face
    NON-TRIVIAL, WEIGHT-CARRYING  dim > 0, Q > 0, systematic power  -> E1; filed first-class

Both branches finish; the candidate CLOSES at the measured verdict either way.

Usage:  python b8_sonin_dim.py register | run
"""
import sys
import numpy as np

PS = [2, 3, 5]
NS = [1, 2]


def model(p, n):
    N = p ** (2 * n)
    F = np.exp(2j * np.pi * np.outer(np.arange(N), np.arange(N)) / N) / np.sqrt(N)
    ball = np.arange(N) % (p ** n) == 0
    return N, F, ball


def sonin_basis(p, n):
    N, F, ball = model(p, n)
    # constraints: rows of identity on ball, rows of F on ball
    C = np.vstack([np.eye(N)[ball], F[ball]])
    _, s, Vh = np.linalg.svd(C)
    tol = max(C.shape) * np.finfo(float).eps * (s[0] if len(s) else 1.0)
    rank = int((s > tol).sum())
    kernel = Vh[rank:].conj().T          # columns: orthonormal basis of Son(p,n)
    return N, kernel


def scaling_matrix(p, n):
    N = p ** (2 * n)
    U = np.zeros((N, N))
    for m in range(N):
        U[(p * m) % N, m] = 1.0
    return U / np.sqrt(p)                # |p|^{1/2} normalization, truncated model


def shells(p, n, vec):
    """mass per shell |x| = p^{n-v(m)} for the kernel basis (summed)."""
    N = p ** (2 * n)
    out = {}
    for m in range(N):
        mm, v = m, 0
        if m == 0:
            v = 2 * n
        else:
            while mm % p == 0:
                mm //= p
                v += 1
        sh = n - v                         # |x|_p = p^sh
        out[sh] = out.get(sh, 0.0) + float((np.abs(vec[m]) ** 2).sum())
    return {k: round(v, 6) for k, v in sorted(out.items()) if v > 1e-12}


def registration():
    print("=" * 100)
    print("B8(1) — THE DIMENSION CHECK · REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()


def run():
    print("  %-4s %-4s %-8s %-6s %-14s %-30s" % ("p", "n", "N", "dim", "Q=||SUS||_F", "shell mass (|x|=p^s: mass)"))
    qs = {}
    for p in PS:
        for n in NS:
            N, K = sonin_basis(p, n)
            d = K.shape[1]
            if d == 0:
                print("  %-4d %-4d %-8d %-6d %-14s %-30s" % (p, n, N, 0, "-", "-"))
                continue
            U = scaling_matrix(p, n)
            SUS = K.conj().T @ U @ K       # compressed action in the Sonin basis
            q = float(np.linalg.norm(SUS))
            qs[(p, n)] = q
            print("  %-4d %-4d %-8d %-6d %-14.6f %-30s" % (p, n, N, d, q, str(shells(p, n, K))))
            sys.stdout.flush()
    for n in NS:
        pts = [(p, qs.get((p, n))) for p in PS if qs.get((p, n)) not in (None, 0.0)]
        if len(pts) >= 2:
            lp = np.log([p for p, _ in pts]); lq = np.log([q for _, q in pts])
            alpha = float(np.polyfit(lp, lq, 1)[0])
            print("  n=%d: fitted power alpha in Q ~ p^alpha : %+0.4f   (points: %s)"
                  % (n, alpha, ", ".join("p=%d Q=%.6f" % t for t in pts)))
    sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
