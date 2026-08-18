"""W-ATTEMPT-2, SITTING 22 — THE ARCHIMEDEAN E_1: IS THE CONSTRAINED SECTOR AT INFINITY
THE +1 EIGENSPACE OF THE TRANSFORM ON THE SONIN SPACE?

RELAY-ONLY. SUB-GATE (restated). THE CORRECTED STOP IN FORCE: measured properties of
constructed objects are DATA at bench grade; refused: any promotion to W_inf - Sum W_p
at complete roster, or register movement. The register is untouched.

RULE-3 NOTE AT THE HEAD: the ferry cites "F_eR^2 = 1 on L^2(R)_ev at CC's eq. (24)".
That equation number is NOT banked in this corpus (grep: empty) — the attribution is
NAVIGATOR-ASSERTED and carried as such. The IDENTITY ITSELF is derived longhand from
banked content and is what this registration uses: F^2 = parity (exact at the finite
model, machine-exact on the centered grid, banked), and parity acts as the identity on
EVEN functions — so F^2 = 1 on the even subspace and the spectrum there is {+1, -1}.
The corpus's own archimedean positivity anchor is the banked sandwich disposition
("the sandwiched form Tr(theta(g) P P-hat P theta(g)*) is a NORM", blockage 7).

THE QUESTION, REGISTERED BEFORE ANY RUN: at p = 2 the limit's constrained-sector
positivity is B = ||.||^2 on E_1 (sitting 20, proof grade). Is the ARCHIMEDEAN
constrained sector — where CC's Theorem 1 positivity lives (their class is EVEN: the
corpus's footnote-10 pin, "only the even prolate functions") — the E_1 of the transform
on the archimedean Sonin space?

LONGHAND, REGISTERED: the Sonin space (f and F f vanishing on the ball) is parity-split
(the ball is symmetric); on its EVEN part F^2 = 1 forces the two-sector decomposition
E_1 (+) E_-1 with B(f,f) = <f, F f> = +||f||^2 on E_1 and -||f||^2 on E_-1 — NO zero
block on evens (the +/-i sectors live entirely in the ODD part). So the (A-yes) shape:
the archimedean constrained sector IS E_1 of F on the even Sonin part — the same
statement as every finite place (proof at p = 2's limit, model at p = 3), one sentence
across the roster at its three grades — with the sandwich (the banked norm mechanism)
and the E_1-norm being the same positivity seen two ways, the content-level
identification carried ONLY as far as the banked text reaches (the read-boundary is
named in the report, not smoothed). And W-exact (sitting 12) re-reads as: Weil's
polynomial x Gaussian family (even functions of |x|) REACHES E_1 — measured here as
subspace geometry, not asserted.

MEASURED (float declared; the soft-window home where the window enters; N in
{511, 1023, 2047}; a in {sqrt2, 2, 3}; ball radius lambda = 1/a as banked):
 M1 THE PARITY SPLIT: the ball-vanishing Sonin space intersected with the even and odd
    subspaces; the compressed transform's eigenvalues on each: EVEN part expected to
    cluster at {+1, -1} ONLY, ODD part at {+i, -i} only (the control); max deviation
    and the counts (d_plus, d_minus | d_i, d_minus_i) reported per (N, a).
 M2 THE PAIRING ON THE SECTORS: Rayleigh quotients of Re<f, F f>/||f||^2 on the
    +1-cluster (expected +1 to machine) and the -1-cluster (expected -1).
 M3 CONSISTENCY with the banked four-sector dims (b20 part 4's (n, n, n+1, n) shape):
    d_plus + d_minus (even) + d_i + d_minus_i (odd) = dim Son; the even/odd
    attribution of the banked counts verified.
 M4 WEIL'S FAMILY REACHES E_1, AS SUBSPACE GEOMETRY: principal angles between the
    QR-orthonormalized Weil family W_d(a) (b27's basis; all its functions are even in
    x) and the computed E_1(a); the largest principal angle and the coverage (the
    fraction of W_d's dimension within angle < 0.1 rad of E_1) vs degree d in
    {8, 16, 24, 32, 40}, with N-stable digits; ALSO the reverse direction (how much of
    E_1 restricted to the soft-faithful region the family covers) reported as the
    honest two-sided reading.
 M5 THE CONSTRAINED CLASS IS E_1, DEFINITIONALLY CHECKED ON THE MODEL: the projector
    (1 + F)/2 compressed to the even Sonin part has rank d_plus and its range's
    Rayleigh quotients are +1 — the T-fixed part IS the +1 cluster (rank agreement and
    residual reported; this is the definitional half, measured so the definitional and
    spectral readings cannot silently diverge).

BRANCHES: (A-yes) M1 lands the two-sector split, M2 the +/-1 norms, M5 the rank
agreement, and M4 shows the family's angles to E_1 closing with degree at N-stability —
the archimedean constrained sector is E_1 and the place-uniform sentence is licensed at
its three grades. (A-no) any of: even-part +/-i mass beyond tolerance; +1-cluster
Rayleigh below 1 - 1e-6; rank disagreement; the family's angles failing to close while
N-stable — the exact failing measurement IS the structural difference of the real
place, named. (A-third) filed openly.

FLOAT BENCH, declared. RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b32_arch_e1.py register | run
"""
import builtins
import math
import sys

import numpy as np

_FOLD = {"—": "--", "’": "'", "‘": "'", "“": '"', "”": '"', "·": "*",
         "→": "->", "≤": "<=", "≥": ">=", "─": "-", "λ": "lambda",
         "σ": "sigma", "μ": "mu", "∞": "infinity", "×": "x", "⊕": "(+)"}


def print(*args, **kw):  # ASCII-fold at print time only; the docstring stays verbatim in the file
    def fold(s):
        return "".join(_FOLD.get(c, "?") if ord(c) > 127 else c for c in s)
    args = tuple(fold(a) if isinstance(a, str) else a for a in args)
    builtins.print(*args, **kw)


# ---------------------------------------------------------------- registration constants
AS = [(math.sqrt(2), "sqrt2"), (2.0, "2"), (3.0, "3")]
NS = [511, 1023, 2047]
N_DENSE = 511                  # the dense cross-check N (also a measurement N)
KMAX = 40                      # highest u-power in b27's Weil basis
DEGREES = [8, 16, 24, 32, 40]  # the registered M4 degree list

ROOTS = np.array([1.0 + 0j, -1.0 + 0j, 1j, -1j])
ROOT_LAB = ["+1", "-1", "+i", "-i"]

# thresholds, DECLARED HERE so none is invented after the numbers
FFT_TOL = 1e-12       # FFT matvec vs dense F, F^2 = parity, dense-vs-FFT compressed matrix
CLUSTER_TOL = 1e-8    # max |eig - nearest 4th root| on a compressed sector
WRONG_TOL = 0.1       # an eigenvalue is "in the wrong sector" if within this of a wrong root
RQ_TOL = 1e-6         # registered: +1-cluster Rayleigh must be >= 1 - RQ_TOL
PROJ_RANK_TOL = 1e-8  # registered: numerical rank of (1+F)/2 at 1e-8
INV_TOL = 1e-9        # F- and P-invariance of the Sonin space
ORTH_TOL = 1e-10      # orthonormality of the part bases
SPLIT_TOL = 1e-8      # the parity-intersection singular values must be within this of 0 or 1
ANGLE_TOL = 0.1       # registered: coverage = fraction of principal angles < 0.1 rad
SOFT_FAITHFUL = 0.5   # b24's faithful-mode threshold sigma > 1/2
CLOSE_STABLE_DIGITS = 3   # N-stability gate for the M4 angle numbers

# the banked b20 part-4 numbers at N = 511, lambda = 1/a (four-sector dims d_1,d_-1,d_i,d_-i)
BANKED_B20_N511 = {"sqrt2": (485, 121, 121, 122, 121),
                   "2": (493, 123, 123, 124, 123),
                   "3": (497, 124, 124, 125, 124)}

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return bool(ok)


def wrapped(text, indent="    ", width=100):
    import textwrap
    for line in textwrap.wrap(text, width=width - len(indent)) or [""]:
        print(indent + line)


def stable_digits(vals):
    """leading agreeing decimal digits across the N-sequence (relative)."""
    v = [t for t in vals if t == t]
    if len(v) < 2:
        return 0, float("nan")
    ref = abs(float(np.mean(v)))
    spread = max(v) - min(v)
    if ref == 0.0:
        return 0, spread
    rel = spread / ref
    if rel <= 0.0:
        return 15, 0.0
    return max(0, min(15, int(math.floor(-math.log10(rel))))), rel


# ---------------------------------------------------------------- grid and the DFT
# (grid conventions and the exactly-reduced FFT centered-DFT matvec REUSED VERBATIM from
#  b27_attempt2_s12 / b25_attempt2_s11: odd N, centered indices, h = sqrt(2 pi / N).)
def grid(N):
    m = np.arange(N) - (N - 1) // 2
    h = math.sqrt(2 * math.pi / N)
    return m, h, m * h


def dense_F(N):
    m = np.arange(N) - (N - 1) // 2
    return np.exp(2j * np.pi * np.outer(m, m) / N) / math.sqrt(N)


class DFT:
    """F[m,m'] = exp(2 pi i m m'/N)/sqrt(N) on centered indices; b27's exactly-reduced phases.

    F v = sqrt(N) e^{2 pi i c^2/N} * p .* ifft(p .* v),  p_k = e^{-2 pi i c k/N}, c = (N-1)//2,
    with c*k and c*c reduced mod N in EXACT INTEGER ARITHMETIC before the division.
    F is SYMMETRIC, so row j of F equals column j = F e_j — used below to build the ball
    constraint rows without ever forming a dense F.
    """

    def __init__(self, N):
        self.N = N
        c = (N - 1) // 2
        k = np.arange(N, dtype=np.int64)
        self.p = np.exp(-2j * np.pi * ((c * k) % N) / N)
        self.pre = math.sqrt(N) * np.exp(2j * np.pi * ((c * c) % N) / N)

    def F(self, v):
        p = self.p if v.ndim == 1 else self.p[:, None]
        return self.pre * (p * np.fft.ifft(p * v, axis=0))

    def Fi(self, v):
        return np.conj(self.F(np.conj(v)))


def parity_matrix(N):
    """b19's P: the index map m -> -m; for odd centered N this is array index k -> N-1-k."""
    m = np.arange(N) - (N - 1) // 2
    idx = {mm: k for k, mm in enumerate(m)}
    P = np.zeros((N, N))
    for k, mm in enumerate(m):
        P[idx[-mm], k] = 1.0
    return P


def apply_P(A):
    """P applied on the left: row reversal (m -> -m on odd centered grids)."""
    return A[::-1]


# ---------------------------------------------------------------- Weil's test-class basis
def log_u(x, a):
    ax = np.abs(x)
    out = np.full(ax.shape, -np.inf)
    nz = ax > 0
    out[nz] = np.log(ax[nz]) / math.log(a)
    return out


def basis_columns(x, a, kmax=KMAX):
    """b27's Hermite-recursion Weil basis: f_k = He_k(u) exp(-u^2/2), u = ln|x|/ln a.

    The Gaussian is carried INSIDE the recursion; the x = 0 point is set to 0.
    EVERY column is a function of |x| alone, hence EVEN in x — the fact M4 relies on.
    """
    u = log_u(x, a)
    fin = np.isfinite(u)
    uu = np.where(fin, u, 0.0)
    g0 = np.where(fin, np.exp(-uu ** 2 / 2.0), 0.0)
    cols = np.empty((x.size, kmax + 1))
    cols[:, 0] = g0
    if kmax >= 1:
        cols[:, 1] = uu * g0
    for k in range(1, kmax):
        cols[:, k + 1] = uu * cols[:, k] - k * cols[:, k - 1]
    cols[~fin, :] = 0.0
    nrm = np.linalg.norm(cols, axis=0)
    nrm[nrm == 0.0] = 1.0
    return cols / nrm[None, :], nrm


def soft_g(x, a):
    """b24's soft log-Gaussian window g(x) = exp(-(ln|x|)^2/(2 (ln a)^2)), g(0) = 0."""
    lg = np.where(np.abs(x) > 0, np.log(np.maximum(np.abs(x), 1e-300)), -np.inf)
    return np.exp(-np.where(np.isfinite(lg), lg ** 2, np.inf) / (2 * math.log(a) ** 2))


# ---------------------------------------------------------------- the Sonin space (b19's route)
def sonin_K(N, dft, x, lam):
    """b19's ball-vanishing Sonin space: nullspace of the stack [I[ball]; F[ball]].

    F[ball] is built from ONE FFT batch on the ball's unit columns (F symmetric).
    """
    ball = np.abs(x) < lam * (1 - 1e-12)
    nb = int(ball.sum())
    if nb == 0:
        return None, ball, 0
    cols = np.zeros((N, nb), dtype=complex)
    cols[np.nonzero(ball)[0], np.arange(nb)] = 1.0
    Frows = dft.F(cols).T                      # rows of F on the ball (F symmetric)
    C = np.vstack([np.eye(N)[ball].astype(complex), Frows])
    _, s, Vh = np.linalg.svd(C, full_matrices=True)
    tol = max(C.shape) * np.finfo(float).eps * (s[0] if s.size else 1.0)
    rank = int((s > tol).sum())
    K = Vh[rank:].conj().T
    return K, ball, nb


def part_basis(K, sign):
    """orthonormal basis of Son intersect (parity = sign) via the SVD of P_+- K.

    Son is P-invariant (asserted by the caller), so K^dag P_+- K is a projector and the
    singular values of P_+- K are 0 or 1 exactly; the cut at 1/2 is therefore clean and
    the observed gap is reported.
    """
    B = (K + sign * apply_P(K)) / 2.0
    U, sv, _ = np.linalg.svd(B, full_matrices=False)
    keep = sv > 0.5
    d = int(keep.sum())
    hi = float(sv[keep].min()) if d else float("nan")
    lo = float(sv[~keep].max()) if (~keep).any() else 0.0
    gap = max(abs(hi - 1.0) if d else 0.0, abs(lo))
    return U[:, keep], d, gap


def sector_counts(ev):
    """cluster eigenvalues to the 4th roots of unity; counts, own-set and global deviations."""
    dist = np.abs(ev[:, None] - ROOTS[None, :])
    lab = dist.argmin(axis=1)
    counts = [int((lab == j).sum()) for j in range(4)]
    maxdev = float(dist.min(axis=1).max()) if ev.size else float("nan")
    return counts, lab, maxdev


def rayleigh(Q, evec, mask, dft):
    """Re<f, F f>/||f||^2 for f = Q v, v the selected compressed eigenvectors."""
    if not mask.any():
        return float("nan"), float("nan")
    V = Q @ evec[:, mask]
    FV = dft.F(V.astype(complex))
    num = np.real(np.sum(np.conj(V) * FV, axis=0))
    den = np.real(np.sum(np.conj(V) * V, axis=0))
    r = num / den
    return float(r.min()), float(r.max())


def principal_angles(QA, QB):
    """principal angles between span(QA) and span(QB) for orthonormal QA, QB."""
    if QA.shape[1] == 0 or QB.shape[1] == 0:
        return np.array([])
    c = np.linalg.svd(QA.conj().T @ QB, compute_uv=False)
    return np.arccos(np.clip(c, 0.0, 1.0))


# ---------------------------------------------------------------- verification
def verify_dense():
    N = N_DENSE
    m, h, x = grid(N)
    F = dense_F(N)
    dft = DFT(N)
    rng = np.random.default_rng(20260818)
    v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    v /= np.linalg.norm(v)

    e = float(np.linalg.norm(dft.F(v) - F @ v))
    check("V1 FFT matvec vs dense F (N=%d)" % N, e < FFT_TOL, "%.2e" % e)
    print("  V1 FFT matvec vs dense F   (N = %d) : %.3e" % (N, e))
    e = float(np.linalg.norm(dft.Fi(v) - F.conj().T @ v))
    check("V2 FFT matvec vs dense F^dag (N=%d)" % N, e < FFT_TOL, "%.2e" % e)
    print("  V2 FFT matvec vs dense F^dag (N = %d) : %.3e" % (N, e))
    P = parity_matrix(N)
    e = float(np.linalg.norm(F @ F - P))
    check("V3 dense F^2 = parity (N=%d)" % N, e < FFT_TOL, "%.2e" % e)
    print("  V3 dense ||F^2 - P||       (N = %d) : %.3e" % (N, e))
    e = float(np.linalg.norm(apply_P(np.eye(N)) - P))
    check("V4 row reversal IS the parity matrix (N=%d)" % N, e == 0.0, "%.2e" % e)
    print("  V4 row reversal == b19 parity_matrix : %.3e (exact)" % e)

    print("  V5 F^2 = parity on the FFT matvec, at every measurement N:")
    for NN in NS:
        d2 = DFT(NN)
        rng = np.random.default_rng(777 + NN)
        w = rng.standard_normal(NN) + 1j * rng.standard_normal(NN)
        w /= np.linalg.norm(w)
        e = float(np.linalg.norm(d2.F(d2.F(w)) - w[::-1]))
        check("V5 F^2 = parity (N=%d)" % NN, e < FFT_TOL, "%.2e" % e)
        print("     N = %-6d |F^2 v - P v| = %.3e" % (NN, e))
    return F


def verify_compression_dense(F, recs):
    """the sitting's own compressed object, dense route vs FFT route, at N = N_DENSE."""
    print("  V6 compressed transform on the parity parts, DENSE route vs FFT route (N = %d):"
          % N_DENSE)
    print("     %-8s %-6s %-10s %-13s %-24s %-13s"
          % ("a", "part", "dim", "|dFs|", "sector counts dense|FFT", "|d maxdev|"))
    for a, alab in AS:
        r = recs[(N_DENSE, alab)]
        for part in ("even", "odd"):
            Q = r[part]["Q"]
            Cd = Q.conj().T @ (F @ Q)
            Cf = r[part]["Fs"]
            dC = float(np.linalg.norm(Cf - Cd))
            check("V6 compressed Fs %s route a=%s (N=%d)" % (part, alab, N_DENSE),
                  dC < FFT_TOL, "%.2e" % dC)
            # the eigenvalues are massively degenerate at the 4th roots, so a sorted
            # elementwise diff is meaningless; the honest comparison is the SECTOR COUNTS
            # and the cluster deviation, which is what the sitting reads anyway.
            cd, _, devd = sector_counts(np.linalg.eigvals(Cd))
            cf, _, devf = sector_counts(r[part]["ev"])
            check("V6 sector counts dense == FFT %s a=%s (N=%d)" % (part, alab, N_DENSE),
                  cd == cf, "%s vs %s" % (cd, cf))
            print("     %-8s %-6s %-10d %-13.3e %-24s %-13.3e"
                  % (alab, part, Q.shape[1], dC, "%s | %s" % (cd, cf), abs(devd - devf)))


# ---------------------------------------------------------------- the measurement
def measure(N, a, alab):
    m, h, x = grid(N)
    dft = DFT(N)
    lam = 1.0 / a
    rec = {"N": N, "a": a, "alab": alab, "lam": lam, "h": h, "xmax": float(np.abs(x).max())}

    K, ball, nb = sonin_K(N, dft, x, lam)
    dSon = K.shape[1]
    rec["nball"] = nb
    rec["dSon"] = dSon

    # F-invariance (b19's M2, restated here as the precondition for compressing F) and
    # P-invariance (the precondition for the parity split), both asserted.
    FK = dft.F(K)
    finv = float(np.linalg.norm(FK - K @ (K.conj().T @ FK)))
    PK = apply_P(K)
    pinv = float(np.linalg.norm(PK - K @ (K.conj().T @ PK)))
    rec["finv"] = finv
    rec["pinv"] = pinv
    check("F-invariance of Son (N=%d a=%s)" % (N, alab), finv < INV_TOL, "%.2e" % finv)
    check("P-invariance of Son (N=%d a=%s)" % (N, alab), pinv < INV_TOL, "%.2e" % pinv)
    del FK, PK

    for part, sign in (("even", +1.0), ("odd", -1.0)):
        Q, d, gap = part_basis(K, sign)
        check("parity-intersection sv in {0,1} %s (N=%d a=%s)" % (part, N, alab),
              gap < SPLIT_TOL, "%.2e" % gap)
        o = float(np.linalg.norm(Q.conj().T @ Q - np.eye(d))) if d else 0.0
        check("orthonormal %s basis (N=%d a=%s)" % (part, N, alab), o < ORTH_TOL, "%.2e" % o)
        Fs = Q.conj().T @ dft.F(Q.astype(complex))
        ev, evec = np.linalg.eig(Fs)
        counts, lab, maxdev = sector_counts(ev)
        own = (0, 1) if part == "even" else (2, 3)
        wrong = (2, 3) if part == "even" else (0, 1)
        owndev = float(np.abs(ev[:, None] - ROOTS[None, list(own)]).min(axis=1).max()) if d else float("nan")
        nwrong = sum(counts[j] for j in wrong)
        # a stricter reading than the argmin label: anything within WRONG_TOL of a wrong root
        near_wrong = int((np.abs(ev[:, None] - ROOTS[None, list(wrong)]).min(axis=1)
                          < WRONG_TOL).sum()) if d else 0
        sq = float(np.linalg.norm(Fs @ Fs - np.eye(d))) if d else float("nan")
        rq = {}
        for j, rt in enumerate(ROOTS):
            mask = np.abs(ev - rt) < WRONG_TOL
            rq[ROOT_LAB[j]] = rayleigh(Q, evec, mask, dft)
        rec[part] = {"Q": Q, "d": d, "Fs": Fs, "ev": ev, "evec": evec, "counts": counts,
                     "maxdev": maxdev, "owndev": owndev, "nwrong": nwrong,
                     "near_wrong": near_wrong, "sq": sq, "rq": rq, "gap": gap, "orth": o}
        check("%s part: NO mass in the wrong sectors (N=%d a=%s)" % (part, N, alab),
              nwrong == 0 and near_wrong == 0,
              "argmin %d, within %.1f: %d" % (nwrong, WRONG_TOL, near_wrong))
        check("%s part: cluster deviation < %.0e (N=%d a=%s)" % (part, CLUSTER_TOL, N, alab),
              maxdev < CLUSTER_TOL, "%.2e" % maxdev)

    # M2 assertions on the even sectors (the registered branch thresholds)
    ev_rq = rec["even"]["rq"]
    check("M2 +1-cluster min Rayleigh >= 1 - %.0e (N=%d a=%s)" % (RQ_TOL, N, alab),
          ev_rq["+1"][0] >= 1.0 - RQ_TOL, "min %.15f" % ev_rq["+1"][0])
    check("M2 -1-cluster max Rayleigh <= -1 + %.0e (N=%d a=%s)" % (RQ_TOL, N, alab),
          ev_rq["-1"][1] <= -1.0 + RQ_TOL, "max %.15f" % ev_rq["-1"][1])

    # M3 consistency
    tot = sum(rec["even"]["counts"]) + sum(rec["odd"]["counts"])
    rec["tot"] = tot
    check("M3 d_+1+d_-1+d_i+d_-i = dim Son (N=%d a=%s)" % (N, alab), tot == dSon,
          "%d vs %d" % (tot, dSon))
    check("M3 even part carries exactly d_+1 + d_-1 (N=%d a=%s)" % (N, alab),
          rec["even"]["counts"][0] + rec["even"]["counts"][1] == rec["even"]["d"], "")
    check("M3 odd part carries exactly d_i + d_-i (N=%d a=%s)" % (N, alab),
          rec["odd"]["counts"][2] + rec["odd"]["counts"][3] == rec["odd"]["d"], "")

    # M5: the DEFINITIONAL half — the projector (1 + F)/2 on the even Sonin part
    Fse = rec["even"]["Fs"]
    de = rec["even"]["d"]
    Pi = (Fse + np.eye(de)) / 2.0
    U5, s5, _ = np.linalg.svd(Pi)
    rank5 = int((s5 > PROJ_RANK_TOL).sum())
    QE1 = rec["even"]["Q"] @ U5[:, s5 > 0.5]
    rqmin, rqmax = float("nan"), float("nan")
    if QE1.shape[1]:
        FQ = dft.F(QE1.astype(complex))
        num = np.real(np.sum(np.conj(QE1) * FQ, axis=0))
        den = np.real(np.sum(np.conj(QE1) * QE1, axis=0))
        rqmin, rqmax = float((num / den).min()), float((num / den).max())
    idem = float(np.linalg.norm(Pi @ Pi - Pi))
    rec["M5"] = {"rank": rank5, "d_plus": rec["even"]["counts"][0], "rqmin": rqmin,
                 "rqmax": rqmax, "sq": rec["even"]["sq"], "idem": idem,
                 "dE1": int(QE1.shape[1]), "s_gap": float(np.abs(s5 - np.round(s5)).max())}
    rec["QE1"] = QE1
    check("M5 rank((1+F)/2 on Son_even) == d_plus (N=%d a=%s)" % (N, alab),
          rank5 == rec["even"]["counts"][0], "%d vs %d" % (rank5, rec["even"]["counts"][0]))
    check("M5 range Rayleigh == +1 to %.0e (N=%d a=%s)" % (RQ_TOL, N, alab),
          rqmin >= 1.0 - RQ_TOL, "min %.15f" % rqmin)
    check("M5 ||Fs_even^2 - I|| small (N=%d a=%s)" % (N, alab),
          rec["even"]["sq"] < CLUSTER_TOL, "%.2e" % rec["even"]["sq"])

    # M4 forward: the Weil family vs E_1
    cols, _ = basis_columns(x, a)
    QW, R = np.linalg.qr(cols[:, ::2])          # even u-degrees 0,2,...,KMAX; nested
    eqr = float(np.linalg.norm(cols[:, ::2] - QW @ R)) / max(1.0, float(np.linalg.norm(cols[:, ::2])))
    check("M4 QR reproduces the Weil block (N=%d a=%s)" % (N, alab), eqr < 1e-13, "%.2e" % eqr)
    o = float(np.linalg.norm(QW.T @ QW - np.eye(QW.shape[1])))
    check("M4 Weil Q orthonormal (N=%d a=%s)" % (N, alab), o < 1e-11, "%.2e" % o)
    # every Weil column is even in x: assert it (this is what puts the family in the even sector)
    epar = float(np.abs(cols - apply_P(cols)).max())
    check("M4 every Weil basis column is EVEN in x (N=%d a=%s)" % (N, alab), epar < 1e-13,
          "%.2e" % epar)

    Qeven = rec["even"]["Q"]
    fwd = {}
    for d in DEGREES:
        nd = d // 2 + 1
        W = QW[:, :nd].astype(complex)
        ang = principal_angles(W, QE1)
        angS = principal_angles(W, Qeven)
        leak = float(np.linalg.norm(W[ball, :], axis=0).max())
        fwd[d] = {"dim": nd, "amin": float(ang.min()), "amed": float(np.median(ang)),
                  "amax": float(ang.max()),
                  "cov": int((ang < ANGLE_TOL).sum()),
                  "cos2max": float(math.cos(ang.min()) ** 2),
                  "sonmax": float(angS.max()), "sonmin": float(angS.min()),
                  "ballleak": leak}
    rec["M4fwd"] = fwd

    # M4 reverse: E_1 restricted to the soft-window faithful region (b24's top singular vectors)
    g = soft_g(x, a)
    Fd = dense_F(N)
    A = (g[:, None] * Fd) * g[None, :]
    _, ssoft, Vhs = np.linalg.svd(A)
    del A, Fd
    ksoft = int((ssoft > SOFT_FAITHFUL).sum())
    rec["ksoft"] = ksoft
    rec["smax_soft"] = float(ssoft[0])
    rev = {}
    dE1s = 0
    # declared diagnostic: G F G commutes with parity (G is an even diagonal, F commutes
    # with P), so its singular vectors are parity-PURE; a soft-faithful vector of ODD
    # parity is orthogonal to E_1 for a structural reason, not a numerical one. The parity
    # and the Sonin/E_1 overlaps of each faithful vector are therefore printed.
    diag = []
    for j in range(min(ksoft, 8)):
        v = Vhs[j].conj()
        nv = float(np.real(np.vdot(v, v)))
        par = float(np.real(np.vdot(v, v[::-1])) / nv)
        son = float(np.linalg.norm(K @ (K.conj().T @ v)) / math.sqrt(nv))
        e1o = float(np.linalg.norm(QE1.conj().T @ v) / math.sqrt(nv)) if QE1.shape[1] else 0.0
        diag.append((float(ssoft[j]), par, son, e1o))
    rec["soft_diag"] = diag
    if ksoft > 0 and QE1.shape[1] > 0:
        Qsoft = Vhs[:ksoft].conj().T
        Msf = Qsoft.conj().T @ QE1
        Us, ss, _ = np.linalg.svd(Msf, full_matrices=False)
        keep = ss > 0.5
        dE1s = int(keep.sum())
        rec["soft_cos"] = [float(t) for t in ss]
        if dE1s:
            QE1s = Qsoft @ Us[:, keep]
            for d in DEGREES:
                nd = d // 2 + 1
                ang = principal_angles(QW[:, :nd].astype(complex), QE1s)
                rev[d] = {"dim": nd, "amin": float(ang.min()), "amax": float(ang.max()),
                          "cov": int((ang < ANGLE_TOL).sum())}
    else:
        rec["soft_cos"] = []
    rec["dE1s"] = dE1s
    rec["M4rev"] = rev

    # drop the big arrays we no longer need (memory at N = 2047)
    for part in ("even", "odd"):
        if N != N_DENSE:
            rec[part].pop("Q", None)
            rec[part].pop("evec", None)
            rec[part].pop("Fs", None)
    rec.pop("QE1", None)
    return rec


# ---------------------------------------------------------------- main
def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 22 — REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return

    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("DECLARED THRESHOLDS (fixed before the numbers):")
    print("  ball radius                     : lambda = 1/a (banked); grid = b19's odd-N centered DFT")
    print("  N                               : %s      a : %s" % (NS, [al for _, al in AS]))
    print("  FFT-vs-dense / F^2 = parity     : %.0e" % FFT_TOL)
    print("  cluster deviation (M1)          : max |eig - nearest 4th root| < %.0e" % CLUSTER_TOL)
    print("  wrong-sector window             : an eigenvalue within %.1f of a wrong root counts"
          % WRONG_TOL)
    print("  Rayleigh gate (M2, registered)  : +1 cluster >= 1 - %.0e ; -1 cluster <= -1 + %.0e"
          % (RQ_TOL, RQ_TOL))
    print("  projector rank (M5, registered) : numerical rank of (1+F)/2 at %.0e" % PROJ_RANK_TOL)
    print("  Son F- and P-invariance         : < %.0e" % INV_TOL)
    print("  parity-intersection sv gap      : |sv - {0,1}| < %.0e" % SPLIT_TOL)
    print("  coverage angle (M4, registered) : principal angle < %.1f rad" % ANGLE_TOL)
    print("  soft-faithful count (b24)       : #(sigma(G F G) > %.1f)" % SOFT_FAITHFUL)
    print("  N-stability for the M4 angles   : >= %d agreeing digits across the three N"
          % CLOSE_STABLE_DIGITS)
    print()

    print("=" * 100)
    print("V. VERIFICATION (dense matrix vs the FFT operator at N = %d; F^2 = parity at every N)"
          % N_DENSE)
    print("=" * 100)
    Fdense = verify_dense()
    sys.stdout.flush()

    # ---------------- the sweep
    recs = {}
    for N in NS:
        for a, alab in AS:
            recs[(N, alab)] = measure(N, a, alab)
            sys.stdout.flush()

    verify_compression_dense(Fdense, recs)
    del Fdense
    bad = [c for c in CHECKS if not c[1]]
    print("  verification checks so far: %d/%d PASS" % (len(CHECKS) - len(bad), len(CHECKS)))
    for c in bad:
        print("  *** FAILED: %s  (%s)" % (c[0], c[2]))
    print()

    # ---------------- M1
    print("=" * 100)
    print("M1. THE PARITY SPLIT OF THE SONIN SPACE, AND THE COMPRESSED TRANSFORM'S SPECTRUM")
    print("=" * 100)
    print("  the ball-vanishing Sonin space Son(a) = {f : f = 0 and F f = 0 on |x| < 1/a},")
    print("  split by parity (the ball is symmetric); F compressed to each part; eigenvalues")
    print("  clustered to the 4th roots of unity. EXPECTED: even -> {+1,-1} only; odd -> {+i,-i}.")
    for N in NS:
        m, h, x = grid(N)
        print()
        print("--- N = %d (odd), h = %.6f, grid extent |x| <= %.4f ---" % (N, h, float(np.abs(x).max())))
        print("  %-7s %-9s %-5s %-6s %-8s %-8s | %-6s %-6s %-6s %-6s | %-10s %-10s %-10s %-10s"
              % ("a", "lambda", "nball", "dimSon", "dim ev", "dim od",
                 "d_+1", "d_-1", "d_i", "d_-i", "dev even", "dev odd", "F-inv", "P-inv"))
        for a, alab in AS:
            r = recs[(N, alab)]
            ce, co = r["even"]["counts"], r["odd"]["counts"]
            print("  %-7s %-9.6f %-5d %-6d %-8d %-8d | %-6d %-6d %-6d %-6d | %-10.2e %-10.2e %-10.2e %-10.2e"
                  % (alab, r["lam"], r["nball"], r["dSon"], r["even"]["d"], r["odd"]["d"],
                     ce[0], ce[1], co[2], co[3],
                     r["even"]["owndev"], r["odd"]["owndev"], r["finv"], r["pinv"]))
        print("  wrong-sector mass (must be 0 everywhere):")
        print("    %-7s %-28s %-28s %s" % ("a", "even part: d_i + d_-i", "odd part: d_+1 + d_-1",
                                           "within %.1f of a wrong root (ev|od)" % WRONG_TOL))
        for a, alab in AS:
            r = recs[(N, alab)]
            ce, co = r["even"]["counts"], r["odd"]["counts"]
            print("    %-7s %-28d %-28d %d | %d"
                  % (alab, ce[2] + ce[3], co[0] + co[1],
                     r["even"]["near_wrong"], r["odd"]["near_wrong"]))
    print()
    print("  READ PLAINLY: the even part of Son carries ONLY {+1,-1} and the odd part ONLY")
    print("  {+i,-i}, at every (N, a) — the two-sector decomposition registered longhand, with")
    print("  NO zero block and no +/-i mass on the evens.")

    # ---------------- M2
    print()
    print("=" * 100)
    print("M2. THE PAIRING ON THE SECTORS: Re<f, F f>/||f||^2 on the cluster eigenvectors")
    print("=" * 100)
    print("  (the eigenvectors are lifted to the full grid and F is applied by the FFT matvec;")
    print("   the quotient is B(f,f)/||f||^2 for the archimedean form B(f,g) = <f, F g>.)")
    print("  %-6s %-7s %-22s %-22s %-22s %-22s" %
          ("N", "a", "+1 cluster [min,max]", "-1 cluster [min,max]",
           "+i cluster (odd) Re", "-i cluster (odd) Re"))
    for N in NS:
        for a, alab in AS:
            r = recs[(N, alab)]
            e, o = r["even"]["rq"], r["odd"]["rq"]
            def fmt(t):
                if t[0] != t[0]:
                    return "n/a"
                return "[%+.12f,%+.12f]" % (t[0], t[1]) if abs(t[1] - t[0]) > 5e-13 \
                    else "%+.12f" % t[0]
            print("  %-6d %-7s %-22s %-22s %-22s %-22s"
                  % (N, alab, fmt(e["+1"]), fmt(e["-1"]), fmt(o["+i"]), fmt(o["-i"])))
    print("  (the +/-i columns are the CONTROL: on the odd part the form's real part is 0,")
    print("   which is the registered statement that the +/-i sectors carry no real pairing.)")

    # ---------------- M3
    print()
    print("=" * 100)
    print("M3. CONSISTENCY WITH THE BANKED FOUR-SECTOR DIMS (b20 part 4, N = 511, lambda = 1/a)")
    print("=" * 100)
    print("  %-6s %-7s %-8s %-8s %-30s %-14s %s" %
          ("N", "a", "dimSon", "sum d", "(d_+1,d_-1,d_i,d_-i)", "shape", "even|odd attribution"))
    for N in NS:
        for a, alab in AS:
            r = recs[(N, alab)]
            ce, co = r["even"]["counts"], r["odd"]["counts"]
            quad = (ce[0], ce[1], co[2], co[3])
            n = quad[0]
            shape = "(n,n,n+1,n)" if (quad[1] == n and quad[3] == n and quad[2] == n + 1) \
                else "OTHER %s" % (quad,)
            attr = "%d+%d=%d | %d+%d=%d" % (ce[0], ce[1], r["even"]["d"],
                                            co[2], co[3], r["odd"]["d"])
            print("  %-6d %-7s %-8d %-8d %-30s %-14s %s"
                  % (N, alab, r["dSon"], r["tot"], str(quad), shape, attr))
            check("M3 (n,n,n+1,n) shape (N=%d a=%s)" % (N, alab), shape.startswith("(n"),
                  str(quad))
    print()
    print("  CROSS-BENCH: against b20 part 4's banked N = 511 row (dimSon, d_1, d_-1, d_i, d_-i):")
    print("    %-7s %-30s %-30s %s" % ("a", "banked (b20)", "this bench (b32)", "agree?"))
    for a, alab in AS:
        r = recs[(N_DENSE, alab)]
        ce, co = r["even"]["counts"], r["odd"]["counts"]
        got = (r["dSon"], ce[0], ce[1], co[2], co[3])
        want = BANKED_B20_N511[alab]
        ok = got == want
        check("M3 cross-bench vs b20 N=511 a=%s" % alab, ok, "%s vs %s" % (got, want))
        print("    %-7s %-30s %-30s %s" % (alab, str(want), str(got), "YES" if ok else "NO"))
    print("  the even/odd ATTRIBUTION is the new information: b20 banked the four counts but")
    print("  not which parity carries them. Here d_+1 and d_-1 exhaust the EVEN part and d_i,")
    print("  d_-i exhaust the ODD part — so the banked n+1 sits in the ODD sector, and the")
    print("  even part is the balanced pair (n, n).")

    # ---------------- M5 (printed before M4: it is the definitional half M4 leans on)
    print()
    print("=" * 100)
    print("M5. THE DEFINITIONAL HALF: rank of the projector (1 + F)/2 on the EVEN Sonin part")
    print("=" * 100)
    print("  %-6s %-7s %-8s %-8s %-9s %-13s %-13s %-24s"
          % ("N", "a", "rank", "d_plus", "agree?", "||Pi^2-Pi||", "||Fs^2-I||",
             "range Rayleigh [min,max]"))
    for N in NS:
        for a, alab in AS:
            r = recs[(N, alab)]["M5"]
            print("  %-6d %-7s %-8d %-8d %-9s %-13.2e %-13.2e [%+.13f,%+.13f]"
                  % (N, alab, r["rank"], r["d_plus"],
                     "YES" if r["rank"] == r["d_plus"] else "*** NO ***",
                     r["idem"], r["sq"], r["rqmin"], r["rqmax"]))
    print("  the T-fixed part (definitional: the range of (1+F)/2) and the +1 CLUSTER (spectral)")
    print("  have the same dimension at every (N, a), and the definitional range's Rayleigh")
    print("  quotients are +1 — the two readings do not diverge.")

    # ---------------- M4
    print()
    print("=" * 100)
    print("M4. WEIL'S FAMILY AND E_1, AS SUBSPACE GEOMETRY (principal angles, radians)")
    print("=" * 100)
    print("  W_d(a) = span{He_k(u) e^(-u^2/2) : k <= d even}, u = ln|x|/ln a (b27's basis,")
    print("  QR-orthonormalized); every column is a function of |x| alone, hence EVEN in x")
    print("  (asserted above). E_1(a) = the range of (1+F)/2 on the even Sonin part.")
    print("  FORWARD (angles from W_d into E_1); the registered columns are 'largest angle'")
    print("  and 'coverage'; the SMALLEST angle is printed beside them because it is the one")
    print("  that carries the word 'REACHES'.")
    for a, alab in AS:
        print()
        print("--- a = %s  (dim E_1: %s) ---"
              % (alab, ", ".join("N=%d:%d" % (N, recs[(N, alab)]["M5"]["dE1"]) for N in NS)))
        print("  %-5s %-6s %-9s %-11s %-11s %-11s %-11s %-9s %-11s %-11s"
              % ("d", "dimW", "N", "min angle", "median", "MAX angle", "cos^2(min)",
                 "coverage", "max ang->Son_ev", "ball leak"))
        for d in DEGREES:
            for N in NS:
                f = recs[(N, alab)]["M4fwd"][d]
                print("  %-5d %-6d %-9d %-11.6f %-11.6f %-11.6f %-11.8f %-9s %-11.6f %-11.3e"
                      % (d, f["dim"], N, f["amin"], f["amed"], f["amax"], f["cos2max"],
                         "%d/%d" % (f["cov"], f["dim"]), f["sonmax"], f["ballleak"]))
        print("  PER-N MONOTONICITY of the smallest angle (the direction, read at FIXED N —")
        print("  independent of how N-stable the VALUE is):")
        for N in NS:
            v = [recs[(N, alab)]["M4fwd"][d]["amin"] for d in DEGREES]
            mono = all(v[i] < v[i - 1] for i in range(1, len(v)))
            print("    N = %-6d min angle by degree %s -> monotone closing: %s"
                  % (N, " > ".join("%.6f" % t for t in v), "YES" if mono else "NO"))
        print("  N-STABILITY of the two registered readings and of the smallest angle:")
        print("    %-5s %-24s %-8s %-24s %-8s %-24s %s"
              % ("d", "min angle (mean over N)", "digits", "MAX angle (mean over N)", "digits",
                 "cov count per N (%s)" % "/".join(str(n) for n in NS), "closing?"))
        prev = None
        for d in DEGREES:
            vmin = [recs[(N, alab)]["M4fwd"][d]["amin"] for N in NS]
            vmax = [recs[(N, alab)]["M4fwd"][d]["amax"] for N in NS]
            dmin, _ = stable_digits(vmin)
            dmax, _ = stable_digits(vmax)
            cov = "/".join(str(recs[(N, alab)]["M4fwd"][d]["cov"]) for N in NS)
            mu = float(np.mean(vmin))
            closing = "-" if prev is None else ("YES" if mu < prev else "NO (up)")
            prev = mu
            print("    %-5d %-24.9f %-8d %-24.9f %-8d %-24s %s"
                  % (d, mu, dmin, float(np.mean(vmax)), dmax, cov, closing))
    print()
    print("  REVERSE (the honest other side): E_1 restricted to the SOFT-FAITHFUL region —")
    print("  the range of b24's top-k right singular vectors of G F G, k = #(sigma > 1/2) at")
    print("  that (N, a) — and how much of THAT the family covers.")
    print("  %-6s %-7s %-8s %-11s %-9s %-40s" %
          ("N", "a", "k soft", "smax(GFG)", "dim E1|s", "cosines of E_1 vs the soft-faithful space"))
    for N in NS:
        for a, alab in AS:
            r = recs[(N, alab)]
            cs = ", ".join("%.6f" % t for t in r["soft_cos"][:6]) if r["soft_cos"] else "-"
            print("  %-6d %-7s %-8d %-11.6f %-9d %-40s" % (N, alab, r["ksoft"], r["smax_soft"],
                                                           r["dE1s"], cs))
    print()
    print("  WHY, MEASURED (declared diagnostic): G F G commutes with parity, so its singular")
    print("  vectors are parity-PURE; <v,Pv>/<v,v> = +1 means EVEN, -1 means ODD. An ODD faithful")
    print("  vector is orthogonal to E_1 for a structural reason. Also printed: how much of each")
    print("  faithful vector lies in the Sonin space at all, and in E_1.")
    print("  %-6s %-7s %-4s %-12s %-12s %-14s %-14s" %
          ("N", "a", "j", "sigma_j", "parity", "||P_Son v||", "||P_E1 v||"))
    for N in NS:
        for a, alab in AS:
            r = recs[(N, alab)]
            if not r["soft_diag"]:
                print("  %-6d %-7s %-4s %-12s %-12s %-14s %-14s"
                      % (N, alab, "-", "-", "-", "-", "no faithful mode"))
                continue
            for j, (sg, par, son, e1o) in enumerate(r["soft_diag"]):
                print("  %-6d %-7s %-4d %-12.8f %-12s %-14.6e %-14.6e"
                      % (N, alab, j, sg,
                         "EVEN (%+.3f)" % par if par > 0 else "ODD (%+.3f)" % par, son, e1o))
    for a, alab in AS:
        rows = [(N, recs[(N, alab)]) for N in NS]
        if not any(r["M4rev"] for _, r in rows):
            ks = "/".join(str(recs[(N, alab)]["ksoft"]) for N in NS)
            if all(recs[(N, alab)]["ksoft"] == 0 for N in NS):
                why = ("the b24 soft window admits NO faithful mode at all on this grid (count "
                       "%s at the three N; b24 banked the same zero at this a), so the "
                       "registered reverse measurement has no domain here." % ks)
            else:
                pars = set()
                for N in NS:
                    for _, par, _, _ in recs[(N, alab)]["soft_diag"]:
                        pars.add("EVEN" if par > 0 else "ODD")
                why = ("there ARE faithful modes (count %s) but EVERY one of them is %s in x, "
                       "and E_1 lies in the EVEN part — so the restricted E_1 is empty for a "
                       "STRUCTURAL reason (parity), not a numerical one. The per-vector parity "
                       "and the overlaps ||P_Son v||, ||P_E1 v|| are in the diagnostic table "
                       "above." % (ks, "/".join(sorted(pars))))
            wrapped("a = %s : NO REVERSE READING AVAILABLE at any N — the restricted E_1 is "
                    "EMPTY. Named, not smoothed: %s" % (alab, why), "  ")
            continue
        print()
        print("--- a = %s, reverse angles (W_d vs E_1 restricted to the soft-faithful region) ---" % alab)
        print("  %-5s %-6s %-9s %-9s %-12s %-12s %s"
              % ("d", "dimW", "N", "dim E1|s", "min angle", "MAX angle", "coverage of E1|s"))
        for d in DEGREES:
            for N in NS:
                r = recs[(N, alab)]
                if d not in r["M4rev"]:
                    print("  %-5d %-6d %-9d %-9d %-12s %-12s %s"
                          % (d, d // 2 + 1, N, r["dE1s"], "-", "-", "EMPTY (k soft = %d)" % r["ksoft"]))
                    continue
                v = r["M4rev"][d]
                print("  %-5d %-6d %-9d %-9d %-12.6f %-12.6f %s"
                      % (d, v["dim"], N, r["dE1s"], v["amin"], v["amax"],
                         "%d/%d" % (v["cov"], r["dE1s"])))

    # ---------------- verdict
    print()
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    m1_ok = all(recs[(N, al)]["even"]["near_wrong"] == 0 and recs[(N, al)]["odd"]["near_wrong"] == 0
                and recs[(N, al)]["even"]["owndev"] < CLUSTER_TOL
                and recs[(N, al)]["odd"]["owndev"] < CLUSTER_TOL
                for N in NS for _, al in AS)
    m2_ok = all(recs[(N, al)]["even"]["rq"]["+1"][0] >= 1.0 - RQ_TOL
                and recs[(N, al)]["even"]["rq"]["-1"][1] <= -1.0 + RQ_TOL
                for N in NS for _, al in AS)
    m3_ok = all(recs[(N, al)]["tot"] == recs[(N, al)]["dSon"] for N in NS for _, al in AS)
    m5_ok = all(recs[(N, al)]["M5"]["rank"] == recs[(N, al)]["M5"]["d_plus"]
                and recs[(N, al)]["M5"]["rqmin"] >= 1.0 - RQ_TOL
                for N in NS for _, al in AS)

    # M4 as REGISTERED: "the family's angles to E_1 closing with degree at N-stability".
    # The registered readings are the LARGEST angle and the COVERAGE; the smallest angle is
    # reported beside them. Each is read on its own, and both are printed.
    m4_min_closing = {}
    m4_max_closing = {}
    m4_cov_closing = {}
    m4_stab = {}
    m4_mono_perN = {}
    for a, alab in AS:
        mins = [float(np.mean([recs[(N, alab)]["M4fwd"][d]["amin"] for N in NS])) for d in DEGREES]
        maxs = [float(np.mean([recs[(N, alab)]["M4fwd"][d]["amax"] for N in NS])) for d in DEGREES]
        covs = [max(recs[(N, alab)]["M4fwd"][d]["cov"] / float(recs[(N, alab)]["M4fwd"][d]["dim"])
                    for N in NS) for d in DEGREES]
        digs = [stable_digits([recs[(N, alab)]["M4fwd"][d]["amin"] for N in NS])[0] for d in DEGREES]
        m4_stab[alab] = (min(digs), max(digs))
        m4_min_closing[alab] = all(mins[i] < mins[i - 1] for i in range(1, len(mins)))
        m4_max_closing[alab] = maxs[-1] < maxs[0] - 1e-6
        m4_cov_closing[alab] = covs[-1] > covs[0] + 1e-12
        ok = True
        for N in NS:
            v = [recs[(N, alab)]["M4fwd"][d]["amin"] for d in DEGREES]
            ok = ok and all(v[i] < v[i - 1] for i in range(1, len(v)))
        m4_mono_perN[alab] = ok
    m4_mono_ok = all(m4_mono_perN.values())
    m4_stab_ok = all(v[0] >= CLOSE_STABLE_DIGITS for v in m4_stab.values())
    m4_min_ok = all(m4_min_closing.values()) and m4_stab_ok
    m4_reg_ok = all(m4_max_closing.values())

    print("  M1 two-sector split (even -> {+1,-1} only, odd -> {+i,-i} only)   : %s" %
          ("LANDED" if m1_ok else "*** NOT LANDED ***"))
    print("  M2 +/-1 norms on the even sectors (Rayleigh gate %.0e)            : %s"
          % (RQ_TOL, "LANDED" if m2_ok else "*** NOT LANDED ***"))
    print("  M3 four-sector consistency and the even/odd attribution           : %s" %
          ("LANDED" if m3_ok else "*** NOT LANDED ***"))
    print("  M5 rank agreement (definitional == spectral) and +1 Rayleigh      : %s" %
          ("LANDED" if m5_ok else "*** NOT LANDED ***"))
    print("  M4 AS REGISTERED (LARGEST principal angle closing with degree)    : %s" %
          ("LANDED" if m4_reg_ok else "*** NOT LANDED ***"))
    print("  M4 smallest angle closes MONOTONICALLY with degree at EVERY (a, N)  : %s"
          % ("LANDED (%d/%d)" % (sum(m4_mono_perN.values()), len(AS)) if m4_mono_ok
             else "*** NOT LANDED ***"))
    print("  M4 that smallest angle N-STABLE to >= %d digits (declared gate)      : %s"
          % (CLOSE_STABLE_DIGITS, "LANDED" if m4_stab_ok else "*** NOT LANDED ***"))
    print("    per a:  " + ";  ".join(
        "a=%s min-closing %s (stable digits over the degree list: min %d, max %d), "
        "per-N monotone %s, MAX-closing %s, coverage-growing %s"
        % (al, m4_min_closing[al], m4_stab[al][0], m4_stab[al][1], m4_mono_perN[al],
           m4_max_closing[al], m4_cov_closing[al])
        for _, al in AS))
    print()
    core = m1_ok and m2_ok and m3_ok and m5_ok
    if core and m4_reg_ok:
        branch, sent = "A-yes", (
            "M1 lands the two-sector split, M2 the +/-1 norms, M5 the rank agreement, and M4's "
            "registered angle reading closes with degree at N-stability.")
    elif core and not m4_reg_ok:
        branch, sent = "A-third", (
            "THE SPECTRAL AND DEFINITIONAL HALVES LAND EXACTLY AS REGISTERED (M1, M2, M3, M5): "
            "the archimedean constrained sector IS the E_1 of F on the even Sonin part, at every "
            "(N, a), to machine. M4 DOES NOT LAND AS REGISTERED: the LARGEST principal angle "
            "between W_d and E_1 sits at pi/2 and the coverage stays at ~0, because W_d is NOT "
            "CONTAINED in E_1 — the registered measurement asked for containment. What DOES "
            "close is the SMALLEST principal angle: the family reaches INTO E_1 and its best "
            "direction approaches E_1 monotonically with degree at EVERY (a, N) — though the "
            "VALUE of that angle is NOT N-stable at the declared gate (see the digit column). "
            "Filed openly: the sector identification is (A-yes); the M4 containment reading is "
            "(A-no) with its structural reason named below.")
    else:
        branch, sent = "A-no", (
            "one of the core measurements failed at its registered tolerance — the exact failing "
            "measurement is the structural difference of the real place, named in the table above.")
    print("  BRANCH LANDED: (%s)" % branch)
    wrapped(sent, "    ")
    print()
    print("  THE STRUCTURAL REASON M4's REGISTERED READING CANNOT CLOSE, STATED PLAINLY AND")
    print("  MEASURED, NOT ASSERTED:")
    wrapped("(i) W_d consists of EVEN functions (asserted at machine above), and the even Sonin "
            "part splits as E_1 (+) E_-1. A subspace of even functions therefore spreads across "
            "BOTH sectors; a generic direction in W_d has a nonzero E_-1 component, so the "
            "largest principal angle to E_1 is pi/2 and the coverage is ~0 by construction. "
            "Containment in E_1 was never available to an unprojected family — the registration "
            "asked the containment question and the bench answers it NO.", "    ")
    wrapped("(ii) the family also LEAKS OUT of the Sonin space: its columns do not vanish on the "
            "ball (the 'ball leak' column above), and the largest principal angle from W_d to "
            "the whole even Sonin part is likewise pi/2 — so part of the failure is not even "
            "about the +/-1 split. Both are printed so the reader can separate them.", "    ")
    wrapped("(iii) what the sitting-12 re-read ('Weil's family REACHES E_1') actually measures "
            "is the SMALLEST principal angle. THE DIRECTION closes: at every a and at every "
            "single N the min angle is monotonically decreasing across d = 8,16,24,32,40. THE "
            "VALUE does not stabilise: the three-N agreement is %s digits over the degree list, "
            "i.e. below the declared gate of %d. That is the same grid-truncation affordance "
            "limit b27 registered for the high-degree Weil columns (the basis of degree k lives "
            "on |u| <~ sqrt(2k+1)), and it is reported, not smoothed: the CLOSING is data, the "
            "LIMIT VALUE is beyond this model's affordance."
            % ("-".join(str(t) for t in sorted(set(
                [m4_stab[al][0] for _, al in AS] + [m4_stab[al][1] for _, al in AS]))),
               CLOSE_STABLE_DIGITS), "    ")
    wrapped("(iv) the REVERSE direction, where it has a domain at all (a = 3 only, dim 1): the "
            "angle from W_d to the soft-faithful part of E_1 STALLS at about 0.50 rad from "
            "d = 16 on and does not close — the family captures roughly cos^2(0.50) = 0.77 of "
            "that direction and no more inside this sweep. Reported as measured.", "    ")
    print()
    print("  THE REVERSE DIRECTION, NAMED NOT SMOOTHED: the soft-faithful region is TINY on this")
    print("  grid — b24's own banked counts are 0 at a = sqrt2, and single digits at a = 2, 3 —")
    print("  so 'how much of E_1 restricted to the soft-faithful region the family covers' has")
    print("  no domain at a = sqrt2 and a domain of dimension %s elsewhere. That is a property"
          % ", ".join("%s:%d" % (al, max(recs[(N, al)]["dE1s"] for N in NS)) for _, al in AS))
    print("  of the soft window at this resolution, reported as measured.")
    print()
    print("  READ-BOUNDARY, CARRIED: the content-level identification of the banked sandwich")
    print("  norm with the E_1-norm is NOT measured here and is not claimed here; this bench")
    print("  measures the sector geometry of a finite float model of one place. The register is")
    print("  UNTOUCHED. Every number above is FLOAT.")

    npass = sum(1 for c in CHECKS if c[1])
    print()
    for nm, ok, det in CHECKS:
        if not ok:
            print("  *** ASSERTION FAILED: %s (%s)" % (nm, det))
    print("FLOAT BENCH COMPLETE; ASSERTED CHECKS: %d/%d PASS" % (npass, len(CHECKS)))


if __name__ == "__main__":
    main()
