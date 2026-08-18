"""W-ATTEMPT-2, SITTING 10 (folded item) — THE SOFT ARCHIMEDEAN FACTOR: GAUSSIAN WINDOW AT INFINITY.

RELAY-ONLY. SUB-GATE (restated). THE CORRECTED STOP IN FORCE: measured properties of
constructed objects are DATA at bench grade; refused: any promotion to W_inf - Sum W_p at
complete roster, or register movement. The protocol correction carried: this is testing.

THE QUESTION, REGISTERED (before any run)
=========================================
Sitting 6 banked: the real place REFUSES the hard two-sided window — the exact
double-support space is empty at every a <= 2 and its a = 3 transients DIE under
refinement (19 -> 14 -> 9), the uncertainty principle watched. THE FERRY'S QUESTION: does
that refusal DISSOLVE under soft truncation (then it was an artifact of the hard cutoff)
or PERSIST (then it is the mathematics)?

THE SOFT WINDOW, DECLARED: on the b19 centered grid (N odd, self-dual spacing,
F^2 = parity at machine), the window [1/a, a] in |x| is made soft by the log-Gaussian
    g(x) = exp( -(ln|x|)^2 / (2 (ln a)^2) ),   g(0) = 0
— g = 1 at |x| = 1, g = e^(-1/2) at the window edges |x| = a^(+/-1), decaying beyond;
the Gaussian choice is Weil's own lemma mechanics (Gaussians are the transform's
self-dual shapes), AT CITE. The soft double compression is A_soft = G F G with
G = diag g; the hard comparison object is A_hard = P_W F P_W with P_W the indicator of
{1/a <= |x| <= a}. IDENTICAL statistics for both, so the comparison is honest:
 S1  the singular-value profile of A: #(sigma > 1/2) ("faithful modes") and
     #(sigma > 1 - 1e-6) ("near-exact modes"), and sigma_max — per (N, a);
 S2  the transform-invariance of the associated space: S = projector onto the top-k
     right singular vectors (k = faithful count); residual ||(1 - S) F S||;
 S3  the constrained-sector positivity: compress F to the S-space, cluster its
     eigenvalues to {1,-1,i,-i} (max deviation reported), and on the +1-cluster
     eigenvectors report the min Rayleigh quotient of Re<v, F v>/<v,v> — the
     soft-space analogue of the fixed-sector positivity (sitting 7's infinity part).

BRANCHES, registered:
 (soft-dissolves) the soft faithful count is N-STABLE at fixed a (vs the hard near-exact
                  count's banked death), the soft invariance residual is small and
                  N-stable, and the fixed-sector positivity holds — the refusal was the
                  HARD CUTOFF, an artifact; the archimedean factor's honest form is
                  soft-windowed (ball-vanishing with Gaussian outer weight).
 (soft-persists)  the soft profile also collapses under refinement — the refusal is the
                  MATHEMATICS, and the real place's non-interleaving address stands.
LONGHAND EXPECTATION, said before the run: dissolves — the Gaussian is the transform's
own fixed shape, so G F G retains faithful modes where an indicator cannot (Paley-Wiener
kills hard two-sided support; nothing kills Gaussian-weighted concentration), at cite.

FLOAT BENCH, declared throughout (the archimedean model is float; exactness lives at the
finite places). RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b24_attempt2_s10_soft.py register | run
"""
import builtins
import math
import sys
import numpy as np

_FOLD = {"—": "--", "’": "'", "·": "*", "→": "->", "≤": "<=", "≥": ">="}


def print(*args, **kw):  # ASCII-fold at print time only; the docstring stays verbatim in the file
    args = tuple("".join(_FOLD.get(c, c) if ord(c) > 127 else c for c in a) if isinstance(a, str) else a
                 for a in args)
    builtins.print(*args, **kw)

AS = [(1.3, "1.3"), (math.sqrt(2), "sqrt2"), (2.0, "2"), (3.0, "3")]
NS = [255, 511, 1023]


def grid(N):
    m = np.arange(N) - (N - 1) // 2
    h = math.sqrt(2 * math.pi / N)
    F = np.exp(2j * np.pi * np.outer(m, m) / N) / math.sqrt(N)
    return m * h, F


def stats(A, F, tag):
    U, s, Vh = np.linalg.svd(A)
    k12 = int((s > 0.5).sum())
    kex = int((s > 1 - 1e-6).sum())
    row = {"faithful": k12, "nearexact": kex, "smax": float(s[0])}
    if k12 == 0:
        row.update({"inv": float("nan"), "maxdev": float("nan"), "minRQ": float("nan")})
        return row
    S = Vh[:k12].conj().T
    P = S @ S.conj().T
    row["inv"] = float(np.linalg.norm((np.eye(len(A)) - P) @ F @ S))
    Fc = S.conj().T @ F @ S
    ev, evec = np.linalg.eig(Fc)
    roots = np.array([1, -1, 1j, -1j])
    dev = np.abs(ev[:, None] - roots[None, :]).min(axis=1)
    row["maxdev"] = float(dev.max())
    fixed = np.abs(ev - 1) < 0.1
    if fixed.any():
        V1 = evec[:, fixed]
        rq = []
        for c in range(V1.shape[1]):
            v = S @ V1[:, c]
            rq.append(float(np.real(np.vdot(v, F @ v)) / np.real(np.vdot(v, v))))
        row["minRQ"] = min(rq)
    else:
        row["minRQ"] = float("nan")
    return row


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 10 (soft window) — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    for N in NS:
        x, F = grid(N)
        print("--- N = %d ---" % N)
        print("  %-7s %-6s %-9s %-10s %-9s %-12s %-10s %-14s" %
              ("a", "kind", "faithful", "nearexact", "smax", "inv resid", "maxdev", "minRQ(+1 sect)"))
        for a, alab in AS:
            W = (np.abs(x) >= 1 / a - 1e-12) & (np.abs(x) <= a + 1e-12)
            Ph = np.diag(W.astype(float))
            lg = np.where(np.abs(x) > 0, np.log(np.maximum(np.abs(x), 1e-300)), -np.inf)
            g = np.exp(-np.where(np.isfinite(lg), lg ** 2, np.inf) / (2 * math.log(a) ** 2))
            G = np.diag(g)
            for kind, A in [("hard", Ph @ F @ Ph), ("soft", G @ F @ G)]:
                r = stats(A, F, kind)
                print("  %-7s %-6s %-9d %-10d %-9.5f %-12.3e %-10.2e %-14s" %
                      (alab, kind, r["faithful"], r["nearexact"], r["smax"], r["inv"],
                       r["maxdev"], ("%.9f" % r["minRQ"]) if r["minRQ"] == r["minRQ"] else "n/a"))
                sys.stdout.flush()
        print()
    print("--- verdict read by the report; branches as registered ---")


if __name__ == "__main__":
    main()
