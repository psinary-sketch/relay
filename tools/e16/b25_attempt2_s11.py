"""W-ATTEMPT-2, SITTING 11 — WHAT IS 0.872: THE ARCHIMEDEAN EXACTNESS DEFICIT PROBED.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
TESTING CONTINUES under the protocol correction; the register is untouched.

THE QUESTION, REGISTERED (before any run): sitting 10 banked sigma_max = 0.87182 (a = 3,
log-Gaussian window, N-independent to ~5 digits) — the real place's exactness deficit,
stable under refinement. Is that number the MODEL'S (it moves with the window) or is it
ABOUT R (window-independent, with a closed form or not)?

THE CALIBRATION, SAID IN ADVANCE SO THE SUP-QUESTION IS HONEST: the unconstrained sup of
sigma_max over soft windows is TRIVIALLY 1 (let G -> 1 off the origin and ||GFG|| -> 1),
so the meaningful family is CALIBRATED to the diagonal's window [1/a, a]: every shape is
a function of u = ln|x| / ln(a), equal to 1 at u = 0 (|x| = 1), vanishing at |x| = 0, and
committed to the window scale (its shape parameterized by u, not by an independent width
that can be sent to infinity). Within that family the ferried question is live: does any
calibrated shape reach 1?

THE FAMILY (fixed in this registration):
  W-lgHALF   log-Gaussian, sigma_w = ln(a)/2 : g = exp(-2 u^2)
  W-lg1      log-Gaussian, sigma_w = ln(a)   : g = exp(-u^2 / 2)      [the banked window]
  W-lg2      log-Gaussian, sigma_w = 2 ln(a) : g = exp(-u^2 / 8)
  W-fejer    triangular in u: g = max(0, 1 - |u|)
  W-rcos     raised cosine: g = (1 + cos(pi u)) / 2 on |u| <= 1, else 0
  W-wp1/W-wp2 Weil-lemma Gaussian-polynomial shapes, the 1952 mechanics transposed to the
             log coordinate (declared as the transposition): g = (1 + beta u^2) exp(-u^2/2)
             normalized to max 1, beta in {0.5, 1}.

MEASURED (per shape, a in {1.3, sqrt2, 2, 3}, N in {1023, 4095, 16383} via FFT-based
centered DFT, verified against the dense matrix at N = 255; sigma_max by power iteration
on A^dagger A to 1e-12):
 M1  sigma_max(shape, a) with its N-stable digit count — the SHAPE SPREAD at fixed a;
     the maximizing calibrated shape named; whether any reaches 1 - 1e-3.
 M2  the a-curve per shape, recorded (four points).
 M3  THE CANDIDATE COMPARISON at a = 3, W-lg1, converged digits — the list FIXED HERE,
     compared by plain subtraction, NO FITTING; a match at >= 6 digits reported, else
     "no closed form found":
     point candidates: lambda(0), lambda(0)^2, 1 - lambda(0), 1 - lambda(0)^2,
       sqrt(1 - lambda(0)^2), mu_1, mu_2, sqrt(mu_1), Si(4pi)/(4pi), 1 - Si(4pi)/(4pi),
       cos(1/2), sqrt(3)/2, e^(-1/8), 2/sqrt(2*pi)*... none beyond this list;
       (prolate quantities from the certified prolate_layer at c = 2*pi, NQ = 700).
     parameter-free curve candidates (compared across ALL FOUR a-points at once —
       a curve match is a finding, a single-point closeness is not):
       erf(ln a) ; tanh(ln a) = (a^2-1)/(a^2+1) ; 1 - a^(-2) ; erf(ln(a)/sqrt(2)).
 M4  THE REFINED INFINITY-WEIGHT IN ITS STABLE HOME: Q_inf_soft(a) = ||G D G||_F with
     D the scaling generator (b19's exact grid affordance) and G the banked W-lg1 window
     — the Gaussian kills the truncation bulk, so N-stability is the registered
     expectation (the raw channel grew ~N^(3/2), banked); reported per (a, N), and the
     punctuated ledger re-read with INF LIVE: full weight = Q_inf_soft(a) * (finite side,
     exact, banked: 0 through a = 2; 6*sqrt(6) at a = 3 on {inf,2,3}; 0 on {inf,2,3,5}).

BRANCHES, registered:
 (E-artifact)  sigma_max moves with calibrated shape/width beyond the N-stable digit
               tolerance — the deficit is the MODEL'S; the maximizing shape named; if any
               calibrated shape reaches 1 - 1e-3 the sharper sentence is recorded: an
               exact archimedean interleave exists in the right test class.
 (E-intrinsic) sigma_max is window-independent to the stated tolerance — the number is
               about R; its digits banked and the candidate comparison decides "closed
               form" vs "no closed form found".
 (E-third)     a third shape (e.g. two shape-classes with two distinct stable values) —
               filed openly as found.
LONGHAND EXPECTATION, said before the run: (E-artifact) in the width direction (wider
calibrated Gaussians should raise sigma_max toward but maybe not to 1), with the shape
question inside the fixed-width class the honest unknown.

FLOAT BENCH, declared. RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b25_attempt2_s11.py register | run
"""
import builtins
import math
import sys
import numpy as np

_FOLD = {"—": "--", "’": "'", "·": "*", "→": "->",
         "≤": "<=", "≥": ">=", "─": "-", "λ": "lambda",
         "σ": "sigma", "μ": "mu"}


def print(*args, **kw):  # ASCII-fold at print time only; the docstring stays verbatim in the file
    def fold(s):
        return "".join(_FOLD.get(c, "?") if ord(c) > 127 else c for c in s)
    args = tuple(fold(a) if isinstance(a, str) else a for a in args)
    builtins.print(*args, **kw)


# ---------------------------------------------------------------- registration constants
AS = [(1.3, "1.3"), (math.sqrt(2), "sqrt2"), (2.0, "2"), (3.0, "3")]
NS = [1023, 4095, 16383]
N_DENSE = 255
NS_M4 = [1023, 4095]
BANKED_SHAPE = "W-lg1"
BANKED_A_LABEL = "3"
POW_TOL = 1e-13          # relative change in the Rayleigh quotient
POW_MAXIT = 200000
RESTART_SEEDS = (0, 1, 2)
RESTART_TOL = 1e-11
DENSE_TOL = 1e-11
FFT_TOL = 1e-12
CURVE_TOL = 1e-6
POINT_DIGITS = 6

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    return bool(ok)


# ---------------------------------------------------------------- the grid and the DFT
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
    """

    def __init__(self, N):
        self.N = N
        c = (N - 1) // 2
        k = np.arange(N)
        self.p = np.exp(-2j * np.pi * c * k / N)
        self.pre = math.sqrt(N) * np.exp(2j * np.pi * c * c / N)

    def F(self, v):
        p = self.p if v.ndim == 1 else self.p[:, None]
        return self.pre * (p * np.fft.ifft(p * v, axis=0))

    def Fi(self, v):
        return np.conj(self.F(np.conj(v)))


# ---------------------------------------------------------------- the calibrated family
_WP_NORM = {}


def _wp_norm(beta):
    if beta not in _WP_NORM:
        t = max(0.0, 2.0 - 1.0 / beta)          # stationary point in t = u^2
        _WP_NORM[beta] = (1.0 + beta * t) * math.exp(-t / 2.0)
    return _WP_NORM[beta]


SHAPES = ["W-lgHALF", "W-lg1", "W-lg2", "W-fejer", "W-rcos", "W-wp1", "W-wp2"]


def shape_g(name, u):
    """u is the log coordinate ln|x|/ln(a); u = -inf at x = 0 (all shapes vanish there)."""
    fin = np.isfinite(u)
    uu = np.where(fin, u, 0.0)
    if name == "W-lgHALF":
        g = np.exp(-2.0 * uu ** 2)
    elif name == "W-lg1":
        g = np.exp(-uu ** 2 / 2.0)
    elif name == "W-lg2":
        g = np.exp(-uu ** 2 / 8.0)
    elif name == "W-fejer":
        g = np.maximum(0.0, 1.0 - np.abs(uu))
    elif name == "W-rcos":
        g = np.where(np.abs(uu) <= 1.0, (1.0 + np.cos(math.pi * uu)) / 2.0, 0.0)
    elif name in ("W-wp1", "W-wp2"):
        beta = 0.5 if name == "W-wp1" else 1.0
        g = (1.0 + beta * uu ** 2) * np.exp(-uu ** 2 / 2.0) / _wp_norm(beta)
    else:
        raise ValueError(name)
    return np.where(fin, g, 0.0)


def log_u(x, a):
    ax = np.abs(x)
    out = np.full(ax.shape, -np.inf)
    nz = ax > 0
    out[nz] = np.log(ax[nz]) / math.log(a)
    return out


def window(x, a, name):
    return shape_g(name, log_u(x, a))


# ---------------------------------------------------------------- sigma_max
def sigma_max_power(dft, g, seed):
    """power iteration on A^dag A, A f = g .* F(g .* f); returns (sigma, iters).

    The Rayleigh quotient lam_k increases monotonically to lambda_1 with a geometric
    tail of ratio r = (lambda_2/lambda_1)^2, so the REMAINING error is estimated as
    d_k * r/(1-r) with r read off the observed increments; the iteration runs until
    that bound is below POW_TOL*lam, or until the increments stagnate at the float
    floor (d_k <= 0 repeatedly) — no early stop on the raw increment alone, which is
    what a near-degenerate top pair (W-wp2 at a = 3) would otherwise fake.
    """
    N = dft.N
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    v = v / np.linalg.norm(v)
    lam_prev = -1.0
    d_prev = -1.0
    stall = 0
    it = 0
    for it in range(1, POW_MAXIT + 1):
        w = g * dft.Fi(g * (g * dft.F(g * v)))
        lam = float(np.real(np.vdot(v, w)))
        nw = np.linalg.norm(w)
        if nw == 0.0:
            return 0.0, it
        v = w / nw
        if lam_prev >= 0.0 and lam > 0.0:
            d = lam - lam_prev
            if d <= 0.0:
                stall += 1
            else:
                stall = 0
                if d_prev > 0.0:
                    r = min(max(d / d_prev, 0.0), 1.0 - 1e-15)
                    rem = d * r / (1.0 - r)
                    if rem <= POW_TOL * lam and it > 20:
                        lam_prev = lam
                        break
                d_prev = d
            if stall >= 5 and it > 20:
                lam_prev = max(lam, lam_prev)
                break
        lam_prev = max(lam, lam_prev) if lam_prev >= 0.0 else lam
    return math.sqrt(max(lam_prev, 0.0)), it


def sigma_max_restarts(dft, g, tag):
    vals = [sigma_max_power(dft, g, s)[0] for s in RESTART_SEEDS]
    spread = max(vals) - min(vals)
    check("restart-agreement %s" % tag, spread <= RESTART_TOL, "spread %.2e" % spread)
    return float(np.mean(vals)), spread


# ---------------------------------------------------------------- the scaling generator D
def GDG_frobenius(dft, x, g, block=128):
    """||G D G||_F exactly-as-float by a column sweep.

    D e_j = ((x + x_j)/2) .* (Ptil e_j),  Ptil e_j = F(x .* F^dag e_j);
    G D G e_j = g_j * (g .* D e_j).
    """
    N = dft.N
    tot = 0.0
    for j0 in range(0, N, block):
        j1 = min(N, j0 + block)
        E = np.zeros((N, j1 - j0), dtype=complex)
        E[np.arange(j0, j1), np.arange(j1 - j0)] = 1.0
        Pt = dft.F(x[:, None] * dft.Fi(E))
        col = ((x[:, None] + x[None, j0:j1]) / 2.0) * Pt
        col = (g[:, None] * col) * g[None, j0:j1]
        tot += float(np.sum(np.abs(col) ** 2))
    return math.sqrt(tot)


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
    e = float(np.linalg.norm(dft.Fi(v) - F.conj().T @ v))
    check("A2 FFT matvec vs dense F^dag (N=255)", e < FFT_TOL, "%.2e" % e)
    e = float(np.linalg.norm(dft.Fi(dft.F(v)) - v))
    check("A3 F^dag F = 1 on the matvec (N=255)", e < FFT_TOL, "%.2e" % e)
    P = np.zeros((N, N))
    idx = {mm: k for k, mm in enumerate(m)}
    for k, mm in enumerate(m):
        P[idx[-mm], k] = 1.0
    e = float(np.linalg.norm(dft.F(dft.F(v)) - P @ v))
    check("A4 F^2 = parity on the matvec (N=255)", e < FFT_TOL, "%.2e" % e)

    X = np.diag(x)
    Ptil = F @ X @ F.conj().T
    e = float(np.linalg.norm(dft.F(x * dft.Fi(v)) - Ptil @ v))
    check("A5 Ptil matvec vs dense F X F^dag (N=255)", e < FFT_TOL, "%.2e" % e)
    Dd = (X @ Ptil + Ptil @ X) / 2.0
    j = 77
    ej = np.zeros(N, dtype=complex)
    ej[j] = 1.0
    e = float(np.linalg.norm(((x + x[j]) / 2.0) * (Ptil @ ej) - Dd @ ej))
    check("A6 D column identity (N=255)", e < FFT_TOL, "%.2e" % e)

    # sigma_max: power iteration vs dense SVD, every (shape, a)
    print("  %-10s %-7s %-14s %-14s %-10s" % ("shape", "a", "dense SVD", "power iter", "|diff|"))
    for name in SHAPES:
        for a, alab in AS:
            g = window(x, a, name)
            A = (g[:, None] * F) * g[None, :]
            sd = float(np.linalg.svd(A, compute_uv=False)[0])
            sp, _ = sigma_max_power(dft, g, 0)
            d = abs(sd - sp)
            check("A7 dense-vs-power %s a=%s (N=255)" % (name, alab), d < DENSE_TOL, "%.2e" % d)
            print("  %-10s %-7s %-14.11f %-14.11f %-10.2e" % (name, alab, sd, sp, d))
    # M4 column sweep vs dense, W-lg1
    for a, alab in AS:
        g = window(x, a, BANKED_SHAPE)
        Q_dense = float(np.linalg.norm((g[:, None] * Dd) * g[None, :]))
        Q_sweep = GDG_frobenius(dft, x, g)
        d = abs(Q_dense - Q_sweep)
        check("A8 ||GDG||_F sweep vs dense a=%s (N=255)" % alab, d < 1e-9 * max(1.0, Q_dense),
              "%.2e" % d)
        print("  ||G D G||_F  a = %-7s dense %-16.10f sweep %-16.10f  |diff| %.2e"
              % (alab, Q_dense, Q_sweep, d))


# ---------------------------------------------------------------- helpers
def stable_digits(vals):
    """leading agreeing decimal digits across the N-sequence (relative)."""
    v = [x for x in vals if x == x]
    if len(v) < 2:
        return 0, 0.0
    ref = abs(np.mean(v))
    spread = max(v) - min(v)
    if ref == 0:
        return 0, spread
    rel = spread / ref
    if rel <= 0:
        return 15, 0.0
    return max(0, min(15, int(math.floor(-math.log10(rel))))), rel


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 11 — REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return

    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    # ---------------- verification block
    print("=" * 100)
    print("V. VERIFICATION AT N = 255 (dense matrix vs FFT operator) — before any measurement")
    print("=" * 100)
    verify_dense()
    bad = [c for c in CHECKS if not c[1]]
    print("  verification checks so far: %d/%d PASS" % (len(CHECKS) - len(bad), len(CHECKS)))
    for c in bad:
        print("  *** FAILED: %s  (%s)" % (c[0], c[2]))
    sys.stdout.flush()

    # ---------------- M1/M2
    print()
    print("=" * 100)
    print("M1/M2. sigma_max(shape, a) — the CALIBRATED SHAPE SPREAD, per N and converged")
    print("=" * 100)
    S = {}   # (shape, alab) -> {N: sigma}
    for name in SHAPES:
        for a, alab in AS:
            S[(name, alab)] = {}
    for N in NS:
        m, h, x = grid(N)
        dft = DFT(N)
        print("--- N = %d (odd), h = %.8f, grid extent |x| <= %.4f ---" % (N, h, abs(x).max()))
        print("  %-10s %-8s %-8s %-8s %-8s" % ("shape", "a=1.3", "a=sqrt2", "a=2", "a=3"))
        for name in SHAPES:
            row = []
            for a, alab in AS:
                g = window(x, a, name)
                s, sp = sigma_max_restarts(dft, g, "%s a=%s N=%d" % (name, alab, N))
                S[(name, alab)][N] = s
                row.append(s)
            print("  %-10s %-8.6f %-8.6f %-8.6f %-8.6f" % (name, row[0], row[1], row[2], row[3]))
            sys.stdout.flush()
        print()

    print("--- CONVERGED sigma_max (mean over N) with N-stable digit count [digits] ---")
    print("  %-10s %-20s %-20s %-20s %-20s" % ("shape", "a=1.3", "a=sqrt2", "a=2", "a=3"))
    conv = {}
    digs = {}
    for name in SHAPES:
        cells = []
        for a, alab in AS:
            vals = [S[(name, alab)][N] for N in NS]
            d, rel = stable_digits(vals)
            c = float(np.mean(vals))
            conv[(name, alab)] = c
            digs[(name, alab)] = d
            cells.append("%.9f [%d]" % (c, d))
        print("  %-10s %-20s %-20s %-20s %-20s" % (name, cells[0], cells[1], cells[2], cells[3]))

    print()
    print("--- THE SHAPE SPREAD AT FIXED a (M1) ---")
    print("  %-8s %-14s %-14s %-12s %-12s %-10s" %
          ("a", "min sigma_max", "max sigma_max", "spread", "min N-digits", "argmax"))
    spread_verdict = []
    for a, alab in AS:
        vals = [conv[(name, alab)] for name in SHAPES]
        dmin = min(digs[(name, alab)] for name in SHAPES)
        amax = SHAPES[int(np.argmax(vals))]
        sp = max(vals) - min(vals)
        tol = 10.0 ** (-dmin)
        spread_verdict.append((alab, sp, tol, amax, max(vals)))
        print("  %-8s %-14.9f %-14.9f %-12.3e %-12d %-10s" %
              (alab, min(vals), max(vals), sp, dmin, amax))
    print("  (the N-stable digit tolerance at each a is 10^-(min N-digits); a spread above it")
    print("   is a REAL shape dependence, not numerical noise.)")

    best_all = max(((conv[(n, al)], n, al) for n in SHAPES for a, al in AS))
    print()
    print("  global maximum over the calibrated family and the four a: sigma_max = %.9f"
          " at shape %s, a = %s" % best_all)
    reach = best_all[0] >= 1.0 - 1e-3
    print("  does ANY calibrated shape reach 1 - 1e-3 = 0.999 ?  %s (max = %.9f, deficit %.9f)"
          % ("YES" if reach else "NO", best_all[0], 1.0 - best_all[0]))

    # ---------------- M3
    print()
    print("=" * 100)
    print("M3. THE CANDIDATE COMPARISON at a = 3, W-lg1 (list FIXED in the registration; no fitting)")
    print("=" * 100)
    target = conv[(BANKED_SHAPE, BANKED_A_LABEL)]
    tdig = digs[(BANKED_SHAPE, BANKED_A_LABEL)]
    print("  measured sigma_max(a = 3, W-lg1) per N:")
    for N in NS:
        print("     N = %-7d %.12f" % (N, S[(BANKED_SHAPE, BANKED_A_LABEL)][N]))
    print("  converged value = %.12f   N-stable digits = %d" % (target, tdig))

    import mpmath
    sys.path.insert(0, __file__.rsplit("\\", 1)[0] if "\\" in __file__ else ".")
    import prolate_layer
    _, _, mu, _, _ = prolate_layer.prolate(700)
    lam0 = math.sqrt(float(mu[0]))
    mu1 = float(mu[1])
    mu2 = float(mu[2])
    si4 = float(mpmath.si(4 * math.pi))
    si4n = si4 / (4 * math.pi)
    print("  prolate substrate (prolate_layer, c = 2*pi, NQ = 700): mu_0 = %.12f, mu_1 = %.12f,"
          " mu_2 = %.12f" % (float(mu[0]), mu1, mu2))
    print("  Si(4pi) = %.12f, Si(4pi)/(4pi) = %.12f" % (si4, si4n))
    print()
    cands = [
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
    print("  %-26s %-16s %-14s %-14s %s" % ("candidate", "value", "|diff|", "digits agree", "match?"))
    hits = []
    for nm, val in cands:
        d = abs(val - target)
        ag = 0 if d == 0 else int(math.floor(-math.log10(d / abs(target)))) if d > 0 else 15
        ag = max(0, min(15, ag))
        ok = ag >= POINT_DIGITS
        if ok:
            hits.append((nm, val, d))
        print("  %-26s %-16.9f %-14.3e %-14d %s" % (nm, val, d, ag, "MATCH" if ok else "-"))
    print()
    if hits:
        print("  POINT VERDICT: closed-form match at >= %d digits: %s" %
              (POINT_DIGITS, ", ".join(h[0] for h in hits)))
    else:
        print("  POINT VERDICT: no closed form found (no candidate in the fixed list agrees"
              " to >= %d digits)." % POINT_DIGITS)

    print()
    print("--- parameter-free CURVE candidates, all four a-points at once, shape W-lg1 ---")
    def erf(z):
        return float(mpmath.erf(z))
    curves = [
        ("erf(ln a)", lambda a: erf(math.log(a))),
        ("tanh(ln a) = (a^2-1)/(a^2+1)", lambda a: (a * a - 1) / (a * a + 1)),
        ("1 - a^(-2)", lambda a: 1.0 - a ** -2),
        ("erf(ln(a)/sqrt(2))", lambda a: erf(math.log(a) / math.sqrt(2))),
    ]
    print("  measured W-lg1 curve: " +
          ", ".join("a=%s: %.9f" % (al, conv[(BANKED_SHAPE, al)]) for a, al in AS))
    print()
    print("  %-30s %-12s %-12s %-12s %-12s %-11s %s" %
          ("curve candidate", "a=1.3", "a=sqrt2", "a=2", "a=3", "max|diff|", "curve match?"))
    curve_hits = []
    for nm, f in curves:
        vals = [f(a) for a, al in AS]
        diffs = [abs(f(a) - conv[(BANKED_SHAPE, al)]) for a, al in AS]
        md = max(diffs)
        ok = md < CURVE_TOL
        if ok:
            curve_hits.append(nm)
        print("  %-30s %-12.9f %-12.9f %-12.9f %-12.9f %-11.3e %s" %
              (nm, vals[0], vals[1], vals[2], vals[3], md, "MATCH" if ok else "-"))
    print()
    if curve_hits:
        print("  CURVE VERDICT: curve match (max|diff| < %.0e) for: %s" % (CURVE_TOL, ", ".join(curve_hits)))
    else:
        print("  CURVE VERDICT: no closed form found (no parameter-free curve in the fixed list"
              " matches all four a-points to %.0e)." % CURVE_TOL)

    # ---------------- M4
    print()
    print("=" * 100)
    print("M4. Q_inf_soft(a) = ||G D G||_F, G = W-lg1, D = (X Ptil + Ptil X)/2 — exact column sweep")
    print("=" * 100)
    Q = {}
    for N in NS_M4:
        m, h, x = grid(N)
        dft = DFT(N)
        for a, alab in AS:
            g = window(x, a, BANKED_SHAPE)
            Q[(alab, N)] = GDG_frobenius(dft, x, g)
        print("  N = %-7d done" % N)
        sys.stdout.flush()
    print()
    print("  %-8s %-18s %-18s %-14s %-12s %s" %
          ("a", "N = %d" % NS_M4[0], "N = %d" % NS_M4[1], "rel change",
           "growth exp", "N-stable?"))
    m4_stable = True
    for a, alab in AS:
        q1, q2 = Q[(alab, NS_M4[0])], Q[(alab, NS_M4[1])]
        rel = abs(q2 - q1) / max(abs(q1), 1e-300)
        expo = math.log(q2 / q1) / math.log(NS_M4[1] / NS_M4[0]) if q1 > 0 and q2 > 0 else float("nan")
        st = rel < 1e-3
        m4_stable = m4_stable and st
        print("  %-8s %-18.10f %-18.10f %-14.3e %-12.4f %s"
              % (alab, q1, q2, rel, expo, "STABLE" if st else "MOVES"))
    print("  (growth exp = log(Q_2/Q_1)/log(N_2/N_1): the fitted power of N, reported because")
    print("   the raw channel's banked growth was ~N^(3/2); the raw Frobenius convention of b19")
    print("   is kept unchanged so the two channels are comparable.)")
    print("  (N-stability criterion registered as the expectation: relative change < 1e-3.)")
    print("  M4 VERDICT: %s" %
          ("Q_inf_soft is N-STABLE as registered — the Gaussian kills the truncation bulk."
           if m4_stable else
           "Q_inf_soft is NOT N-stable — the registered expectation did NOT land."))

    print()
    print("--- THE PUNCTUATED LEDGER RE-READ, INF LIVE (largest M4 N = %d) ---" % NS_M4[-1])
    print("    banked finite side (sitting 4, exact): 0 through a = 2; 6*sqrt(6) = %.9f at a = 3"
          % (6 * math.sqrt(6)))
    print("    on {inf,2,3}; 0 at a = 3 on {inf,2,3,5}.")
    print("  %-8s %-18s %-18s %-22s %s" %
          ("a", "Q_inf_soft", "finite {inf,2,3}", "FULL WEIGHT {inf,2,3}", "FULL WEIGHT {inf,2,3,5}"))
    for a, alab in AS:
        q = Q[(alab, NS_M4[-1])]
        fin23 = 6 * math.sqrt(6) if alab == "3" else 0.0
        fin235 = 0.0
        print("  %-8s %-18.10f %-18.9f %-22.9f %.9f" % (alab, q, fin23, q * fin23, q * fin235))
    print("    READ PLAINLY: the infinity channel is ALIVE (nonzero) at every a; the sawtooth's")
    print("    zeros on the finite side still annihilate the product wherever they sit. The")
    print("    per-channel ledger is the information; no promotion is made.")

    # ---------------- verdict
    print()
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    moves = any(sp > tol for (al, sp, tol, am, mx) in spread_verdict)
    # width direction specifically: the three log-Gaussians at fixed a
    width_moves = False
    for a, alab in AS:
        w = [conv[(n, alab)] for n in ("W-lgHALF", "W-lg1", "W-lg2")]
        dmin = min(digs[(n, alab)] for n in ("W-lgHALF", "W-lg1", "W-lg2"))
        if (max(w) - min(w)) > 10.0 ** (-dmin):
            width_moves = True
    for al, sp, tol, am, mx in spread_verdict:
        print("  a = %-7s shape spread %.3e  vs  N-stable tolerance %.1e  -> %s (argmax %s)" %
              (al, sp, tol, "MOVES" if sp > tol else "within tolerance", am))
    print("  width direction (W-lgHALF / W-lg1 / W-lg2) moves beyond tolerance: %s" %
          ("YES" if width_moves else "NO"))
    if moves:
        branch = "(E-artifact)"
        sent = ("sigma_max MOVES with the calibrated shape/width beyond the N-stable digit "
                "tolerance — the exactness deficit is the MODEL'S, not a constant of R.")
    else:
        branch = "(E-intrinsic)"
        sent = ("sigma_max is window-independent to the stated tolerance — the number is "
                "about R.")
    print()
    print("  BRANCH LANDED: %s" % branch)
    print("  %s" % sent)
    print("  maximizing calibrated shape at the largest a (a = 3): %s (sigma_max = %.9f)" %
          (spread_verdict[-1][3], spread_verdict[-1][4]))
    print("  any calibrated shape at 1 - 1e-3: %s" % ("YES" if reach else "NO"))
    if reach:
        print("  SHARPER SENTENCE RECORDED: an exact archimedean interleave exists in the right"
              " test class.")
    else:
        print("  NO sharper sentence: no calibrated shape reaches 1 - 1e-3; the deficit survives"
              " the whole registered family.")
    print("  closed form for the banked 0.87182 (a = 3, W-lg1): %s" %
          ("MATCH: " + ", ".join(h[0] for h in hits) if hits else "no closed form found"))
    print("  parameter-free curve: %s" %
          ("MATCH: " + ", ".join(curve_hits) if curve_hits else "no closed form found"))
    print("  the register is UNTOUCHED; this is bench-grade DATA about a constructed object.")

    npass = sum(1 for c in CHECKS if c[1])
    print()
    for nm, ok, det in CHECKS:
        if not ok:
            print("  *** ASSERTION FAILED: %s (%s)" % (nm, det))
    print("FLOAT BENCH COMPLETE; ASSERTED CHECKS: %d/%d PASS" % (npass, len(CHECKS)))


if __name__ == "__main__":
    main()
