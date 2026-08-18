"""W-ATTEMPT-2, SITTING 12 — DOES WEIL'S FAMILY REACH EXACTNESS: THE POLYNOMIAL-DEGREE SWEEP.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
TESTING CONTINUES; the register is untouched. The ferry's correction carried on the face:
"0.872 is the archimedean deficit" was an over-read of a model number — RETIRED; the
window-independent fact is the residual.

THE OBJECT, DISTINGUISHED FROM SITTING 11's (registered so the two sigma_max's cannot be
conflated): sitting 11 measured multiplication-window compressions G F G (the shape
applied twice as a multiplier). THIS sitting measures the compression of F to WEIL'S
TEST-CLASS SUBSPACE at degree d:
    W_d(a) = span{ u^k e^(-u^2/2) : k <= d, k even },  u = ln|x| / ln(a)
(even k = symmetric under the window's own inversion x <-> 1/x; the 1952 lemma's
polynomial-times-Gaussian family at cite, calibrated to the diagonal's window as in
sitting 11). sigma_max(d, a) = the largest singular value of P_W F P_W — equivalently
the generalized eigenproblem (B* F* B)(B* B)^(-1)(B* F B) w = sigma^2 (B* B) w over the
degree-d coefficient space — SOLVED EXACTLY (QR-orthonormalize the basis on the grid,
SVD the compressed matrix Q* F Q), NOT SEARCHED. This is the lemma's own exactness
question: how faithfully does the transform act on Weil's family at degree d.

THE DENSITY LONGHAND, registered before any number: in u-coordinates the family's weight
is Gaussian, whose moment problem is DETERMINATE (Hermite completeness), so the span over
all degrees is dense in the relevant even sector and IN THE CONTINUUM sigma_max(d) -> 1
as d -> infinity is the expected shape. The measured content is therefore: (i) whether
the MODEL reproduces the approach within N-stability, and at what RATE (successive
deficit ratios reported plainly — no fitted constants); (ii) the a-dependence; (iii) the
branch sentence.

BRANCHES:
 (W-exact) the deficit 1 - sigma_max(d) decays through the N-stable range with a
           consistent rate — THE ARCHIMEDEAN INTERLEAVE IS EXACT IN THE LIMIT OF WEIL'S
           FAMILY AT THE MODEL: the real place's inexactness was finite-degree. SCOPE
           SAID WITH IT: the centered-DFT archimedean model, calibrated windows; the
           continuum-density longhand above is the shape it confirms.
 (W-floor) the deficit stalls at a positive value across >= 4 consecutive even degrees
           while N-stable — the floor banked to full precision as the archimedean
           residual in Weil's natural family; its a-dependence recorded; candidates
           compared at >= 6 digits from the FIXED sitting-11 point list (the prolate
           quantities at c = 2*pi; Si(4pi)/(4pi) and its complement; cos(1/2); sqrt(3)/2;
           e^(-1/8); 2/sqrt(2*pi)), NO FITTING.
 (W-third) filed openly as found.

MEASUREMENT DISCIPLINE: a in {sqrt2, 2, 3}; N in {1023, 4095, 16383}; even degrees
d = 0, 2, 4, ..., 40. Basis: Hermite-recursion polynomials in u (same span as monomials,
conditioned), evaluated on the grid, QR-orthonormalized; the compressed (dim W_d)-square
matrix Q* F Q via one FFT matvec per basis column. A degree's sigma_max is REPORTED AS A
NUMBER only when >= 6 digits agree across the three N — degrees beyond that gate are
listed as BEYOND THE MODEL'S AFFORDANCE, not reported. Secondary column, cheap and
declared: the full-degree sweep (odd u-powers included) beside the ferried even list.

FLOAT BENCH, declared. RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b27_attempt2_s12.py register | run
"""
import builtins
import math
import os
import sys

import numpy as np

_FOLD = {"—": "--", "’": "'", "‘": "'", "“": '"', "”": '"', "·": "*",
         "→": "->", "≤": "<=", "≥": ">=", "─": "-", "λ": "lambda",
         "σ": "sigma", "μ": "mu", "∞": "infinity"}


def print(*args, **kw):  # ASCII-fold at print time only; the docstring stays verbatim in the file
    def fold(s):
        return "".join(_FOLD.get(c, "?") if ord(c) > 127 else c for c in s)
    args = tuple(fold(a) if isinstance(a, str) else a for a in args)
    builtins.print(*args, **kw)


# ---------------------------------------------------------------- registration constants
AS = [(math.sqrt(2), "sqrt2"), (2.0, "2"), (3.0, "3")]
NS = [1023, 4095, 16383]
N_DENSE = 255
KMAX = 40                      # highest u-power in the basis
DEGREES_EVEN = list(range(0, KMAX + 1, 2))
DEGREES_FULL = list(range(0, KMAX + 1))

FFT_TOL = 1e-12                # FFT matvec vs dense F, and F^2 = parity
DENSE_TOL = 1e-11              # compressed matrix / sigma_max, FFT route vs dense route
GATE_DIGITS = 6                # N-stability gate: >= 6 agreeing digits across the three N
MONO_SLACK = 1e-12             # nested-subspace monotonicity slack
RANK_TOL = 1e-12               # |R[j,j]| (columns pre-normalised) below this = collinear
UNITARY_SLACK = 1e-12          # sigma_max <= 1 + slack

# branch criteria, DECLARED HERE (printed in the run so no threshold is invented after
# the numbers): a STEP is "stalled" when the successive deficit ratio is >= STALL_RATIO
# (the deficit falls by less than 0.1% per degree step); a floor needs STALL_DEGREES
# consecutive gated degrees inside such a stall.  A step "decays" when the ratio is
# <= DECAY_RATIO; the decay is "consistent" (the registered word) when EVERY resolved
# gated step decays, with no reversal.  RATE_SPREAD_MAX is a DESCRIPTOR ONLY, not a
# branch gate: it labels the decay geometric (ratios within max/min <= RATE_SPREAD_MAX)
# or accelerating.  A deficit at or below FLOAT_FLOOR is AT THE DOUBLE-PRECISION FLOOR:
# 1 - sigma_max is no longer resolvable in float64 (an SVD of a unitary compression
# carries absolute error ~1e-15), so such a value is NEITHER a decay nor a stall and its
# ratios are excluded from the branch reading, said here and not after the numbers.
STALL_RATIO = 0.999
STALL_DEGREES = 4
DECAY_RATIO = 0.99
RATE_SPREAD_MAX = 3.0
FLOAT_FLOOR = 1e-14
POINT_DIGITS = 6               # candidate-comparison agreement threshold, no fitting
PROLATE_NQ = 700

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return bool(ok)


# ---------------------------------------------------------------- the grid and the DFT
# (grid conventions and the FFT centered-DFT matvec REUSED VERBATIM from b25_attempt2_s11:
#  odd N, centered indices, self-dual spacing h = sqrt(2 pi / N).)
def grid(N):
    """centered indices m, self-dual spacing h, positions x = m*h."""
    m = np.arange(N) - (N - 1) // 2
    h = math.sqrt(2 * math.pi / N)
    return m, h, m * h


def dense_F(N):
    m = np.arange(N) - (N - 1) // 2
    return np.exp(2j * np.pi * np.outer(m, m) / N) / math.sqrt(N)


class DFT:
    """F[m,m'] = exp(2 pi i m m'/N)/sqrt(N) on centered indices m = k - c, c = (N-1)//2.

    (F v)_k = sum_k' exp(2 pi i (k-c)(k'-c)/N) v_k' / sqrt(N)
            = e^{2 pi i c^2/N} e^{-2 pi i c k/N} sum_k' e^{2 pi i k k'/N} (e^{-2 pi i c k'/N} v_k') / sqrt(N)
    and sum_k' e^{+2 pi i k k'/N} w_k' = N * ifft(w)_k, so
      F v = sqrt(N) e^{2 pi i c^2/N} * p .* ifft(p .* v),   p_k = e^{-2 pi i c k/N}.
    F^dagger v = conj(F conj(v)) since F is symmetric.

    ONE ACCURACY REFINEMENT over b25's identical formula, declared: the phase arguments
    c*k and c*c are reduced mod N IN EXACT INTEGER ARITHMETIC before the division, so the
    argument handed to exp() never exceeds 2 pi.  Unreduced, c*k reaches ~1.3e8 at
    N = 16383 and the argument's own rounding (eps * 2 pi c k / N ~ 1e-11 rad) is the
    dominant error — which is why the unreduced form misses F^2 = parity at 5e-12 there.
    The reduction changes nothing mathematically (e^{2 pi i t} is 1-periodic in t) and the
    result is re-verified against the dense matrix at N = 255 below.
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
    m = np.arange(N) - (N - 1) // 2
    idx = {mm: k for k, mm in enumerate(m)}
    P = np.zeros((N, N))
    for k, mm in enumerate(m):
        P[idx[-mm], k] = 1.0
    return P


# ---------------------------------------------------------------- Weil's test-class basis
def log_u(x, a):
    """u = ln|x| / ln(a); u = -inf at the single grid point x = 0."""
    ax = np.abs(x)
    out = np.full(ax.shape, -np.inf)
    nz = ax > 0
    out[nz] = np.log(ax[nz]) / math.log(a)
    return out


def basis_columns(x, a, kmax=KMAX):
    """columns f_k = He_k(u) exp(-u^2/2), k = 0..kmax, on the grid; x = 0 point set to 0.

    The Gaussian is carried INSIDE the recursion (f_0 = e^(-u^2/2), f_1 = u f_0,
    f_(k+1) = u f_k - k f_(k-1)) — algebraically identical to He_k times the Gaussian,
    and free of the overflow that He_40(u) alone would hit at the grid's |u|.
    The x = 0 point is set to 0 explicitly (u = -infinity, the factor vanishes).
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
    # column normalisation: span-preserving, purely for QR conditioning
    nrm = np.linalg.norm(cols, axis=0)
    nrm[nrm == 0.0] = 1.0
    return cols / nrm[None, :], nrm


def compressed(dft, cols, tag):
    """Q from ONE reduced QR of the (already nested) column block; C = Q* F Q.

    numpy's reduced QR has span(Q[:, :j]) = span(B[:, :j]) for every j, so the nested
    subspaces come out of a single factorisation and every leading principal submatrix
    of C is exactly the compression at that degree.  Returns (C, rank_ok, rdiag).
    """
    Q, R = np.linalg.qr(cols)
    rdiag = np.abs(np.diag(R))
    rank_ok = rdiag > RANK_TOL
    # real assertions on the factorisation itself; the RANK verdict is DATA, recorded as a
    # note by the caller (a collinear column at grid resolution is a finding about the
    # model's affordance, not a defect of the code, so it is not scored as a check)
    e = float(np.linalg.norm(cols - Q @ R)) / max(1.0, float(np.linalg.norm(cols)))
    check("QR reproduces the basis block %s" % tag, e < 1e-13, "rel %.2e" % e)
    o = float(np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1])))
    check("Q orthonormal %s" % tag, o < 1e-11, "%.2e" % o)
    FQ = dft.F(Q.astype(complex))
    C = Q.T.conj() @ FQ
    return C, rank_ok, rdiag


def sigma_ladder(C, dims):
    """largest singular value of the leading dim-square blocks of C."""
    out = []
    for n in dims:
        s = np.linalg.svd(C[:n, :n], compute_uv=False)
        out.append(float(s[0]))
    return out


# ---------------------------------------------------------------- verification at N = 255
def verify_dense():
    N = N_DENSE
    m, h, x = grid(N)
    F = dense_F(N)
    dft = DFT(N)
    rng = np.random.default_rng(12345)
    v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    v = v / np.linalg.norm(v)

    e = float(np.linalg.norm(dft.F(v) - F @ v))
    check("A1 FFT matvec vs dense F (N=255)", e < FFT_TOL, "%.2e" % e)
    print("  A1 FFT matvec vs dense F (N=255)            : %.3e" % e)
    e = float(np.linalg.norm(dft.Fi(v) - F.conj().T @ v))
    check("A2 FFT matvec vs dense F^dag (N=255)", e < FFT_TOL, "%.2e" % e)
    print("  A2 FFT matvec vs dense F^dag (N=255)        : %.3e" % e)
    e = float(np.linalg.norm(dft.Fi(dft.F(v)) - v))
    check("A3 F^dag F = 1 on the matvec (N=255)", e < FFT_TOL, "%.2e" % e)
    print("  A3 F^dag F = 1 on the matvec (N=255)        : %.3e" % e)
    P = parity_matrix(N)
    e = float(np.linalg.norm(dft.F(dft.F(v)) - P @ v))
    check("A4 F^2 = parity on the matvec (N=255)", e < FFT_TOL, "%.2e" % e)
    print("  A4 F^2 = parity on the matvec (N=255)       : %.3e" % e)

    # the sitting's own object, both routes, at every a: dense P_W F P_W vs the FFT route
    print("  A5 compressed matrix and sigma_max, FFT route vs DENSE route (N = 255):")
    print("     %-8s %-6s %-16s %-16s %-11s %-11s" %
          ("a", "d", "sigma dense", "sigma FFT", "|dC|", "|dsigma|"))
    for a, alab in AS:
        cols, _ = basis_columns(x, a)
        even = cols[:, ::2]
        Q, R = np.linalg.qr(even)
        C_fft = Q.T.conj() @ dft.F(Q.astype(complex))
        C_den = Q.T.conj() @ (F @ Q)
        dC = float(np.linalg.norm(C_fft - C_den))
        check("A5 compressed C FFT vs dense a=%s (N=255)" % alab, dC < DENSE_TOL, "%.2e" % dC)
        for d in (0, 10, 40):
            n = d // 2 + 1
            sd = float(np.linalg.svd(C_den[:n, :n], compute_uv=False)[0])
            sf = float(np.linalg.svd(C_fft[:n, :n], compute_uv=False)[0])
            ds = abs(sd - sf)
            check("A5 sigma_max FFT vs dense a=%s d=%d (N=255)" % (alab, d), ds < DENSE_TOL,
                  "%.2e" % ds)
            print("     %-8s %-6d %-16.12f %-16.12f %-11.2e %-11.2e" % (alab, d, sd, sf, dC, ds))


def verify_parity_all_N():
    print("  A6 F^2 = parity on a test vector, at every measurement N:")
    for N in NS:
        dft = DFT(N)
        rng = np.random.default_rng(777 + N)
        v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        v = v / np.linalg.norm(v)
        w = dft.F(dft.F(v))
        # parity acts on centered indices m -> -m, i.e. array index k -> N-1-k for odd N
        e = float(np.linalg.norm(w - v[::-1]))
        check("A6 F^2 = parity (N=%d)" % N, e < FFT_TOL, "%.2e" % e)
        print("     N = %-7d |F^2 v - P v| = %.3e" % (N, e))


# ---------------------------------------------------------------- helpers
def wrapped(text, indent="    ", width=96):
    import textwrap
    for line in textwrap.wrap(text, width=width - len(indent)) or [""]:
        print(indent + line)


def stable_digits(vals):
    """leading agreeing decimal digits across the N-sequence (relative)."""
    v = [t for t in vals if t == t]
    if len(v) < 2:
        return 0, 0.0
    ref = abs(float(np.mean(v)))
    spread = max(v) - min(v)
    if ref == 0.0:
        return 0, spread
    rel = spread / ref
    if rel <= 0.0:
        return 15, 0.0
    return max(0, min(15, int(math.floor(-math.log10(rel))))), rel


def measure(a, family):
    """sigma_max(d) at each N for one a and one family ('even' or 'full').

    returns dict: N -> list of sigma_max over the family's degree list, plus the
    monotonicity and rank bookkeeping.
    """
    degs = DEGREES_EVEN if family == "even" else DEGREES_FULL
    dims = [d // 2 + 1 for d in degs] if family == "even" else [d + 1 for d in degs]
    per_N = {}
    rank_notes = []
    for N in NS:
        m, h, x = grid(N)
        dft = DFT(N)
        cols, _ = basis_columns(x, a)
        block = cols[:, ::2] if family == "even" else cols
        tag = "%s a=%s N=%d" % (family, a, N)
        C, rank_ok, rdiag = compressed(dft, block, tag)
        if not np.all(rank_ok):
            bad = [int(i) for i in np.nonzero(~rank_ok)[0]]
            rank_notes.append((N, [degs[i] for i in bad], float(rdiag.min())))
        s = sigma_ladder(C, dims)
        # nested-subspace monotonicity, and unitarity bound
        drops = [(degs[i], s[i - 1] - s[i]) for i in range(1, len(s))
                 if s[i] < s[i - 1] - MONO_SLACK]
        worst = max(drops, key=lambda t: t[1]) if drops else None
        check("monotone sigma_max in d (%s)" % tag, len(drops) == 0,
              "%d drops, worst %.2e at d=%d" % (len(drops), worst[1], worst[0])
              if worst else "")
        over = max(s) - 1.0
        check("sigma_max <= 1 (%s)" % tag, over <= UNITARY_SLACK, "max-1 = %.2e" % over)
        per_N[N] = s
    return degs, per_N, rank_notes


def converge(degs, per_N):
    """per degree: converged value, digit count, gate flag, plus the two-largest-N
    diagnostic (declared as a diagnostic, NOT a reported number)."""
    rows = []
    for i, d in enumerate(degs):
        vals = [per_N[N][i] for N in NS]
        dig, rel = stable_digits(vals)
        pdig, _ = stable_digits(vals[1:])
        conv = float(np.mean(vals))
        rows.append({"d": d, "vals": vals, "dig": dig, "rel": rel, "pdig": pdig,
                     "conv": conv, "gated": dig >= GATE_DIGITS,
                     "deficit": 1.0 - conv})
    return rows


def analyse(rows, step):
    """branch analysis over the gated degrees; returns (branch, sentence, detail dict)."""
    g = [r for r in rows if r["gated"]]
    det = {"n_gated": len(g), "gated_degrees": [r["d"] for r in g], "ratios": [], "rs": [],
           "stall_degrees": 0, "n_decay": 0, "rate_spread": float("nan"),
           "floor_degree": None, "terminal": g[-1]["deficit"] if g else float("nan")}
    at_floor = [r for r in g if r["deficit"] <= FLOAT_FLOOR]
    det["floor_degree"] = at_floor[0]["d"] if at_floor else None
    if len(g) < 2:
        return ("W-third", "fewer than two gated degrees — the N-stability gate cuts the "
                "sweep before any rate can be read; BEYOND THE MODEL'S AFFORDANCE.", det)
    # consecutive gated pairs only (a gap breaks the chain); pairs touching the
    # double-precision floor are marked and excluded from the branch reading
    ratios = []
    for i in range(1, len(g)):
        if g[i]["d"] - g[i - 1]["d"] != step:
            ratios.append((g[i]["d"], None, "gap"))
        elif g[i - 1]["deficit"] <= FLOAT_FLOOR or g[i]["deficit"] <= FLOAT_FLOOR:
            ratios.append((g[i]["d"], None, "floor"))
        else:
            ratios.append((g[i]["d"], g[i]["deficit"] / g[i - 1]["deficit"], "ok"))
    det["ratios"] = ratios
    rs = [r for _, r, k in ratios if k == "ok" and math.isfinite(r)]
    det["rs"] = rs
    # stall run: consecutive stalled resolved steps -> stalled degrees = steps + 1
    best = cur = 0
    for _, r, k in ratios:
        if k == "ok" and r >= STALL_RATIO:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    det["stall_degrees"] = best + 1 if best > 0 else 0
    decaying = [r for r in rs if r <= DECAY_RATIO]
    det["n_decay"] = len(decaying)
    spread = (max(rs) / min(rs)) if rs and min(rs) > 0 else float("nan")
    det["rate_spread"] = spread
    det["rate_char"] = ("geometric (ratios within max/min <= %.1f)" % RATE_SPREAD_MAX
                        if rs and spread <= RATE_SPREAD_MAX else
                        "ACCELERATING / irregular (ratio max/min = %.3g)" % spread
                        if rs else "no resolved step")
    if best + 1 >= STALL_DEGREES:
        return ("W-floor",
                "the deficit STALLS at a positive value across %d consecutive gated "
                "degrees, above the double-precision floor — a floor, not an approach "
                "to 1." % (best + 1), det)
    if len(rs) >= 2 and len(decaying) == len(rs):
        tail = ("and reaches the DOUBLE-PRECISION FLOOR at d = %d (1 - sigma_max no longer "
                "resolvable in float64)" % det["floor_degree"] if det["floor_degree"] is not None
                else "and is still decaying at the last gated degree (terminal deficit "
                     "%.6e)" % det["terminal"])
        return ("W-exact",
                "the deficit DECAYS at EVERY resolved gated step with no reversal "
                "(%d/%d steps, rate %s) %s." % (len(decaying), len(rs), det["rate_char"], tail),
                det)
    return ("W-third",
            "neither a stall of %d gated degrees nor a decay at every resolved gated step "
            "(%d/%d steps decaying, %d resolved steps in all) — filed openly as found."
            % (STALL_DEGREES, len(decaying), len(rs), len(rs)), det)


def candidate_list():
    import mpmath
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    import prolate_layer
    _, _, mu, _, _ = prolate_layer.prolate(PROLATE_NQ)
    lam0 = math.sqrt(float(mu[0]))
    mu1 = float(mu[1])
    mu2 = float(mu[2])
    si4n = float(mpmath.si(4 * math.pi)) / (4 * math.pi)
    return [
        ("lambda(0) = sqrt(mu_0)", lam0),
        ("lambda(0)^2 = mu_0", lam0 ** 2),
        ("1 - lambda(0)", 1.0 - lam0),
        ("1 - lambda(0)^2", 1.0 - lam0 ** 2),
        ("sqrt(1 - lambda(0)^2)", math.sqrt(max(0.0, 1.0 - lam0 ** 2))),
        ("mu_1", mu1),
        ("mu_2", mu2),
        ("sqrt(mu_1)", math.sqrt(mu1)),
        ("Si(4pi)/(4pi)", si4n),
        ("1 - Si(4pi)/(4pi)", 1.0 - si4n),
        ("cos(1/2)", math.cos(0.5)),
        ("sqrt(3)/2", math.sqrt(3) / 2),
        ("e^(-1/8)", math.exp(-0.125)),
        ("2/sqrt(2*pi)", 2.0 / math.sqrt(2 * math.pi)),
    ]


def compare_candidates(target, label, cands):
    print("  --- candidate comparison against %s = %.15f (fixed list; NO FITTING) ---"
          % (label, target))
    print("     %-26s %-18s %-12s %-8s %s" % ("candidate", "value", "|diff|", "digits", "match?"))
    hits = []
    for nm, val in cands:
        dd = abs(val - target)
        if dd == 0.0:
            ag = 15
        elif target == 0.0:
            ag = 0
        else:
            ag = max(0, min(15, int(math.floor(-math.log10(dd / abs(target))))))
        ok = ag >= POINT_DIGITS
        if ok:
            hits.append(nm)
        print("     %-26s %-18.12f %-12.3e %-8d %s" % (nm, val, dd, ag, "MATCH" if ok else "-"))
    if hits:
        print("     VERDICT: closed-form match at >= %d digits: %s" % (POINT_DIGITS, ", ".join(hits)))
    else:
        print("     VERDICT: no closed form found (no candidate in the fixed list agrees to"
              " >= %d digits)." % POINT_DIGITS)
    return hits


# ---------------------------------------------------------------- main
def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 12 — REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return

    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("DECLARED THRESHOLDS (fixed before the numbers):")
    print("  N-stability gate            : >= %d agreeing digits across N = %s" % (GATE_DIGITS, NS))
    print("  stalled step                : deficit ratio >= %.4f" % STALL_RATIO)
    print("  floor needs                 : >= %d consecutive gated degrees inside a stall"
          % STALL_DEGREES)
    print("  decaying step               : deficit ratio <= %.4f" % DECAY_RATIO)
    print("  CONSISTENT decay (W-exact)  : EVERY resolved gated step decays, no reversal")
    print("  rate DESCRIPTOR (not a gate): geometric if ratio max/min <= %.1f, else"
          " accelerating" % RATE_SPREAD_MAX)
    print("  double-precision floor      : deficit <= %.0e is NOT resolvable in float64 —"
          % FLOAT_FLOOR)
    print("                                such steps are excluded from the rate reading")
    print("  monotonicity slack          : %.0e ; QR rank floor %.0e ; unitarity slack %.0e"
          % (MONO_SLACK, RANK_TOL, UNITARY_SLACK))
    print("  QR rank truncation          : RECORDED AS DATA (a note), not scored as a check")
    print()

    # ---------------- verification
    print("=" * 100)
    print("V. VERIFICATION (dense matrix vs FFT operator at N = 255; F^2 = parity at every N)")
    print("=" * 100)
    verify_dense()
    verify_parity_all_N()
    bad = [c for c in CHECKS if not c[1]]
    print("  verification checks so far: %d/%d PASS" % (len(CHECKS) - len(bad), len(CHECKS)))
    for c in bad:
        print("  *** FAILED: %s  (%s)" % (c[0], c[2]))
    sys.stdout.flush()

    # ---------------- the grid's reach in u, printed before the tables (it is the affordance)
    print()
    print("=" * 100)
    print("G. THE GRID'S REACH IN u = ln|x|/ln(a) — the model's affordance, stated in advance")
    print("=" * 100)
    print("  %-8s %-8s %-12s %-12s %-12s %-14s %s" %
          ("a", "N", "h", "|x|max", "u range", "du at |x|=1", "He_40 turning pt sqrt(2k+1)"))
    for a, alab in AS:
        for N in NS:
            m, h, x = grid(N)
            xmax = float(np.abs(x).max())
            umax = math.log(xmax) / math.log(a)
            umin = math.log(h) / math.log(a)
            du1 = h / math.log(a)
            print("  %-8s %-8d %-12.6f %-12.4f [%7.3f,%7.3f] %-14.5f %.3f"
                  % (alab, N, h, xmax, umin, umax, du1, math.sqrt(2 * KMAX + 1)))
    print("  (READ PLAINLY: a basis function of degree k lives on |u| <~ sqrt(2k+1) = %.2f at"
          % math.sqrt(2 * KMAX + 1))
    print("   k = 40; where the grid's u-range is shorter than that, the high-degree columns are")
    print("   TRUNCATED by the grid, not resolved — this is exactly what the N-stability gate is")
    print("   there to catch, and it is registered here BEFORE the numbers.)")

    # ---------------- the sweeps
    results = {}
    for family, degs_all, step in (("even", DEGREES_EVEN, 2), ("full", DEGREES_FULL, 1)):
        for a, alab in AS:
            degs, per_N, rank_notes = measure(a, family)
            rows = converge(degs, per_N)
            results[(family, alab)] = (rows, rank_notes)
            sys.stdout.flush()

    print()
    print("=" * 100)
    print("M1. THE EVEN FAMILY (WEIL'S LIST): sigma_max(P_W F P_W), d = 0,2,...,%d" % KMAX)
    print("=" * 100)
    for a, alab in AS:
        rows, rank_notes = results[("even", alab)]
        print()
        print("--- a = %s   (dim W_d = d/2 + 1) ---" % alab)
        print("  %-4s %-5s %-15s %-15s %-15s %-4s %-5s %-17s %-16s %s" %
              ("d", "dim", "N=1023", "N=4095", "N=16383", "dig", "[pair]",
               "sigma_max (conv)", "deficit (FL=floor)", "ratio"))
        prev = None
        for r in rows:
            n = r["d"] // 2 + 1
            if r["gated"]:
                conv = "%.14f" % r["conv"]
                dfc = "%+.6e" % r["deficit"]
                if r["deficit"] <= FLOAT_FLOOR:
                    dfc += " FL"
                if prev is not None and prev[0] == r["d"] - 2 and prev[1] > FLOAT_FLOOR \
                        and r["deficit"] > FLOAT_FLOOR:
                    rat = "%.6f" % (r["deficit"] / prev[1])
                elif prev is not None and prev[0] == r["d"] - 2:
                    rat = "at float floor"
                else:
                    rat = "-"
                prev = (r["d"], r["deficit"])
            else:
                conv = "BEYOND AFFORDANCE"
                dfc = "-"
                rat = "-"
            print("  %-4d %-5d %-15.12f %-15.12f %-15.12f %-4d [%-3d] %-17s %-16s %s"
                  % (r["d"], n, r["vals"][0], r["vals"][1], r["vals"][2],
                     r["dig"], r["pdig"], conv, dfc, rat))
        if rank_notes:
            for N, ds, mn in rank_notes:
                wrapped("!! QR RANK TRUNCATION at N = %d: degrees %s collinear at grid"
                        " resolution (min |R_jj| = %.2e) — RECORDED AS DATA, sweep continued."
                        % (N, ds, mn), "  ")
        else:
            print("  QR rank: full at every N (no collinear column at grid resolution).")
        print("  ([pair] = agreeing digits across the two largest N only — a DIAGNOSTIC, not a")
        print("   reported number; the registered gate is the three-N digit count.)")

    print()
    print("=" * 100)
    print("M2. SECONDARY, DECLARED: THE FULL-DEGREE SWEEP (odd u-powers included), d = 0..%d" % KMAX)
    print("=" * 100)
    for a, alab in AS:
        rows, rank_notes = results[("full", alab)]
        print()
        print("--- a = %s   (dim W_d = d + 1; all k, not just even) ---" % alab)
        print("  %-4s %-5s %-4s %-19s %-16s %-10s | %-4s %-5s %-4s %-19s %-16s %s" %
              ("d", "dim", "dig", "sigma_max (conv)", "deficit (FL=floor)", "ratio",
               "d", "dim", "dig", "sigma_max (conv)", "deficit (FL=floor)", "ratio"))
        cells = []
        prev = None
        for r in rows:
            if r["gated"]:
                conv = "%.14f" % r["conv"]
                dfc = "%+.6e" % r["deficit"]
                if r["deficit"] <= FLOAT_FLOOR:
                    dfc += " FL"
                if prev is not None and prev[0] == r["d"] - 1 and prev[1] > FLOAT_FLOOR \
                        and r["deficit"] > FLOAT_FLOOR:
                    rat = "%.6f" % (r["deficit"] / prev[1])
                elif prev is not None and prev[0] == r["d"] - 1:
                    rat = "floor"
                else:
                    rat = "-"
                prev = (r["d"], r["deficit"])
            else:
                conv, dfc, rat = "BEYOND AFFORDANCE", "-", "-"
            cells.append("%-4d %-5d %-4d %-19s %-16s %-10s" %
                         (r["d"], r["d"] + 1, r["dig"], conv, dfc, rat))
        half = (len(cells) + 1) // 2
        for i in range(half):
            left = cells[i]
            right = cells[i + half] if i + half < len(cells) else ""
            print("  %s| %s" % (left, right))
        if rank_notes:
            for N, ds, mn in rank_notes:
                wrapped("!! QR RANK TRUNCATION at N = %d: degrees %s (min |R_jj| = %.2e)"
                        % (N, ds, mn), "  ")

    # ---------------- branch analysis
    print()
    print("=" * 100)
    print("M3. BRANCH ANALYSIS PER a (even family = Weil's list; the full sweep beside it)")
    print("=" * 100)
    verdicts = {}
    for a, alab in AS:
        rows, _ = results[("even", alab)]
        br, sent, det = analyse(rows, 2)
        verdicts[alab] = (br, sent, det, rows)
        rowsf, _ = results[("full", alab)]
        brf, sentf, detf = analyse(rowsf, 1)
        verdicts[alab + "|full"] = (brf, sentf, detf, rowsf)
        print()
        print("--- a = %s ---" % alab)
        wrapped("EVEN family: gated degrees %s" %
                (str(det["gated_degrees"]) if det["gated_degrees"] else "NONE"), "  ")
        if det["n_gated"]:
            g = [r for r in rows if r["gated"]]
            lo, hi = g[0]["d"], g[-1]["d"]
            below = [r["d"] for r in rows if not r["gated"] and r["d"] < lo]
            gaps = [r["d"] for r in rows if not r["gated"] and lo < r["d"] < hi]
            above = [r["d"] for r in rows if not r["gated"] and r["d"] > hi]
            print("    WHERE THE N-STABILITY GATE CUTS: gated band d = %d .. %d" % (lo, hi))
            print("      ungated BELOW the band (too coarse / not yet stable): %s"
                  % (below if below else "none"))
            print("      ungated GAPS inside the band                        : %s"
                  % (gaps if gaps else "none"))
            print("      ungated ABOVE the band (grid truncates the basis)   : %s"
                  % (above if above else "none"))
            print("    deficits at the gated degrees:")
            for r in g:
                print("      d = %-4d deficit = %+.15e   sigma_max = %.15f%s" %
                      (r["d"], r["deficit"], r["conv"],
                       "   [AT THE DOUBLE-PRECISION FLOOR]" if r["deficit"] <= FLOAT_FLOOR else ""))
            if det["ratios"]:
                print("    successive deficit ratios (deficit(d)/deficit(d-2)):")
                wrapped(", ".join("d=%d:%s" % (d, k if r is None else "%.6f" % r)
                                  for d, r, k in det["ratios"]), "      ")
                if det.get("rs"):
                    wrapped("ratio spread (max/min) = %.4g -> %s ; stalled-degree run = %d ;"
                            " decaying steps %d/%d resolved"
                            % (det["rate_spread"], det["rate_char"], det["stall_degrees"],
                               det["n_decay"], len(det["rs"])), "    ")
                else:
                    print("    no resolved ratio (every gated pair is broken by a gap or sits"
                          " at the double-precision floor).")
            if det["floor_degree"] is not None:
                print("    FIRST GATED DEGREE AT THE DOUBLE-PRECISION FLOOR: d = %d"
                      % det["floor_degree"])
        print("    BRANCH (a = %s, even) : (%s)" % (alab, br))
        wrapped(sent, "      ")
        if br == "W-exact" and det["floor_degree"] is None and det["terminal"] > 1e-3:
            print("    !! CAUTION, SAID PROMINENTLY: the gated band ENDS with the deficit still")
            print("       at %.6e. (W-exact) here reads the DIRECTION of %d steps only; it is"
                  % (det["terminal"], len(det["rs"])))
            print("       NOT an observed approach to 1 inside this a's affordance. The rest of")
            print("       the sweep is BEYOND THE MODEL'S AFFORDANCE and is not reported.")
        wrapped("FULL sweep: gated degrees %s -> branch (%s)" %
                (str(detf["gated_degrees"]) if detf["gated_degrees"] else "NONE", brf), "  ")
        wrapped(sentf, "      ")

    # ---------------- the floor, where one landed
    print()
    print("=" * 100)
    print("M4. THE FLOOR AND ITS a-DEPENDENCE (banked to full precision where W-floor landed)")
    print("=" * 100)
    floors = {}
    for a, alab in AS:
        br, sent, det, rows = verdicts[alab]
        g = [r for r in rows if r["gated"]]
        if br == "W-floor" and g:
            floors[alab] = (g[-1]["d"], g[-1]["deficit"], g[-1]["conv"])
    if floors:
        print("  %-8s %-6s %-24s %s" % ("a", "d", "floor deficit 1-sigma_max", "sigma_max at the floor"))
        for alab in [al for _, al in AS if al in floors]:
            d, dfc, sg = floors[alab]
            print("  %-8s %-6d %-24.17e %.17f" % (alab, d, dfc, sg))
        print()
        print("  a-DEPENDENCE, read plainly: " +
              "; ".join("a=%s -> %.12e" % (al, floors[al][1]) for _, al in AS if al in floors))
        cands = candidate_list()
        for _, alab in AS:
            if alab not in floors:
                continue
            d, dfc, sg = floors[alab]
            print()
            print("  == a = %s ==" % alab)
            compare_candidates(dfc, "the floor deficit (a = %s)" % alab, cands)
            compare_candidates(sg, "sigma_max at the floor (a = %s)" % alab, cands)
    else:
        print("  NO (W-floor) landed at any a — no floor is banked, and the fixed candidate")
        print("  list is NOT exercised (comparing it to a non-floor would be exactly the")
        print("  over-read the ferry's correction retired).")

    # ---------------- verdict
    print()
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    brs = [verdicts[al][0] for _, al in AS]
    weak = []
    for _, alab in AS:
        br, sent, det, rows = verdicts[alab]
        gd = det["gated_degrees"]
        print("  a = %-7s BRANCH (%s)  gated band d = %s..%s (%d degrees), terminal deficit"
              " %+.4e%s" %
              (alab, br, gd[0] if gd else "-", gd[-1] if gd else "-", det["n_gated"],
               det["terminal"],
               ", AT THE DOUBLE-PRECISION FLOOR from d = %d" % det["floor_degree"]
               if det["floor_degree"] is not None else ""))
        if br == "W-exact" and det["floor_degree"] is None and det["terminal"] > 1e-3:
            weak.append(alab)
    uniq = sorted(set(brs))
    if len(uniq) == 1:
        overall = uniq[0]
        print()
        print("  OVERALL BRANCH LANDED: (%s) — the same at every a in {sqrt2, 2, 3}." % overall)
    else:
        overall = "W-third"
        print()
        print("  OVERALL BRANCH LANDED: (W-third) — the a-points do not agree (%s); filed"
              " openly as found." % ", ".join("%s:%s" % (al, verdicts[al][0]) for _, al in AS))
    if weak:
        print()
        print("  !! NOT LANDING AS REGISTERED, SAID PROMINENTLY: at a = %s the gated band ends"
              % ", ".join(weak))
        print("     with the deficit still far from 0, so the (W-exact) reading there is the")
        print("     DIRECTION of a handful of steps, NOT an observed approach to 1. The a where")
        print("     the model actually carries the question to the double-precision floor inside")
        print("     the gate is %s." % ", ".join(
            al for _, al in AS if verdicts[al][2]["floor_degree"] is not None) or "none")
    print("  the DENSITY LONGHAND registered before the run said sigma_max(d) -> 1 IN THE")
    print("  CONTINUUM; what is measured here is whether the MODEL reproduces that approach")
    print("  inside the N-stable range, and nothing more.")
    print()
    print("  SECONDARY, DECLARED — DOES INCLUDING THE ODD u-POWERS CHANGE THE STORY?")
    print("  %-8s %-40s %-40s %s" %
          ("a", "EVEN family (Weil's list)", "FULL sweep (odd included)", "same story?"))
    for _, alab in AS:
        be, _, de, _ = verdicts[alab]
        bf, _, df, _ = verdicts[alab + "|full"]
        se = "(%s) %2d gated, d<=%-3s def %+.3e" % (
            be, de["n_gated"], de["gated_degrees"][-1] if de["gated_degrees"] else "-",
            de["terminal"])
        sf = "(%s) %2d gated, d<=%-3s def %+.3e" % (
            bf, df["n_gated"], df["gated_degrees"][-1] if df["gated_degrees"] else "-",
            df["terminal"])
        print("  %-8s %-40s %-40s %s" % (alab, se, sf, "YES" if be == bf else "NO"))
    print("  (the FULL sweep is a richer family at the same degree label d — dim d+1 against")
    print("   dim d/2+1 — so a faster approach is EXPECTED; what is measured is whether the")
    print("   branch sentence itself changes, not whether the numbers move.)")
    print("  SECONDARY branches: " +
          "; ".join("a=%s -> (%s)" % (al, verdicts[al + "|full"][0]) for _, al in AS))
    print("  the register is UNTOUCHED; this is bench-grade DATA about a constructed object.")
    print("  the sitting-11 sigma_max (||G F G||) and this sitting's sigma_max (||P_W F P_W||)")
    print("  are DIFFERENT OBJECTS, as registered — they are not to be conflated.")

    npass = sum(1 for c in CHECKS if c[1])
    print()
    for nm, ok, det in CHECKS:
        if not ok:
            print("  *** ASSERTION FAILED: %s (%s)" % (nm, det))
    print("FLOAT BENCH COMPLETE; ASSERTED CHECKS: %d/%d PASS" % (npass, len(CHECKS)))


if __name__ == "__main__":
    main()
