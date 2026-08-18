"""W-ATTEMPT-2, SITTING 12 (item 2) — THE INFINITY-WEIGHT IN THE HILBERT-SCHMIDT CONVENTION.

RELAY-ONLY. SUB-GATE (restated). THE CORRECTED STOP IN FORCE: measured properties of
constructed objects are DATA at bench grade; refused: any promotion to W_inf - Sum W_p at
complete roster, or register movement. TESTING CONTINUES; the register is untouched.

THE NAMED CANDIDATE, measured: Q_HS(a) = h * ||G D G||_F — the h-weighted (continuum
measure) Hilbert-Schmidt norm, the normalization the raw grid sum lacks (sitting 11's
raw Frobenius grew ~N^0.77 after Gaussian suppression; the banked unwindowed channel grew
~N^1.5). G = the log-Gaussian window (W-lg1, the banked shape); D = the scaling generator
(X Ptil + Ptil X)/2, Ptil = F X F^dagger.

THE REGISTERED LONGHAND, said against the candidate before the run: D is a first-order
(derivative-type) operator; its continuum kernel is delta'-supported on the diagonal, so
G D G is NOT Hilbert-Schmidt in the continuum — no h-weighting of a grid Frobenius sum
can converge; the predicted behaviour is residual growth Q_HS ~ N^(~1/4) (the h factor
removes N^(1/2) from the measured ~N^0.77). If that lands, the failure is the
CONVENTION'S CATEGORY, not the model's: the finite-place weight law Q(p,n) = ||S U S||_F
is built on the GROUP ELEMENT U (a bounded unitary), while the infinity channel has been
using the GENERATOR (unbounded). THE SECOND CANDIDATE, NAMED WITH ITS DERIVATION AND NOT
RUN THIS SITTING: the group-element convention — the infinity channel measured on a
bounded dilation U_lambda f(x) = lambda^(-1/2) f(x/lambda) (mirroring the finite places'
unitary U_p exactly), whose windowed h-weighted HS norm CONVERGES in the continuum
(h Sum -> integral of |g(lambda x) g(x)|^2 dx / lambda, finite — the composition-kernel
computation), with the grid representation of U_lambda (off-grid points; band-limited
interpolation) the declared implementation question for the sitting that runs it.

BRANCHES: (H-stable) Q_HS N-stable to >= 4 digits across N in {1023, 4095, 16383} — it
is a number; its value beside the finite weight laws and the punctuated ledger re-read
with infinity live. (H-fails) growth persists — the measured exponent banked; the
convention question FILED with the second candidate above; the ledger keeps its caveat.
LONGHAND EXPECTATION: (H-fails), by the delta'-kernel derivation.

FLOAT BENCH, declared. RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b28_attempt2_s12_hs.py register | run
"""

import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ======================================================================================
# REUSE.  Sitting 11's b25 is IMPORTED, NOT MODIFIED and NOT RE-DERIVED: the centered-DFT
# FFT matvec (DFT), the self-dual grid, the calibrated window family, and — the object of
# this sitting — the ||G D G||_F COLUMN SWEEP that b25 verified against the dense matrix
# at N = 255.  That verification is RE-ASSERTED here before any measurement (V below);
# nothing in b25 or b26 is touched by this file.
# ======================================================================================

from b25_attempt2_s11 import (AS, NS, N_DENSE, BANKED_SHAPE, DFT, GDG_frobenius,
                              dense_F, grid, window)

# ======================================================================================
# PURE-ASCII OUTPUT GUARD.  The banked registration docstring above is VERBATIM in the
# file; typographic characters are folded to ASCII at PRINT time only.
# ======================================================================================

_ASCII_FOLD = {0x2014: u"--", 0x2013: u"-", 0x2012: u"-", 0x2010: u"-", 0x2011: u"-",
               0x2018: u"'", 0x2019: u"'", 0x201c: u'"', 0x201d: u'"',
               0x2026: u"...", 0x00a0: u" ", 0x00d7: u"x", 0x2212: u"-",
               0x2192: u"->", 0x2264: u"<=", 0x2265: u">=", 0x00b7: u"*"}

_emit = print


def print(*args, **kw):  # noqa: A001  (deliberate module-scope shadow: ASCII guard)
    out = []
    for a in args:
        s = a if isinstance(a, str) else str(a)
        s = s.translate(_ASCII_FOLD)
        try:
            s.encode("ascii")
        except UnicodeEncodeError:
            s = s.encode("ascii", "backslashreplace").decode("ascii")
        out.append(s)
    _emit(*out, **kw)


# ======================================================================================
# THE LEDGER
# ======================================================================================

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print("  %s  %s%s" % ("PASS" if ok else "**FAIL**", name,
                          ("  [%s]" % detail) if detail else ""))
    sys.stdout.flush()
    return bool(ok)


# ======================================================================================
# CONSTANTS OF THIS RUN (fixed here, before any measurement)
# ======================================================================================

SWEEP_NS = list(NS)              # 1023, 4095, 16383 -- as registered
FFT_TOL = 1e-12                  # matvec-vs-dense absolute, N = 255
SWEEP_REL_TOL = 1e-11            # ||GDG||_F sweep-vs-dense RELATIVE, N = 255
STABLE_DIGITS = 4                # the registered (H-stable) criterion
STABLE_REL = 10.0 ** (-STABLE_DIGITS)


def h_of(N):
    """the self-dual spacing; grid() returns the same number."""
    return math.sqrt(2.0 * math.pi / N)


# ======================================================================================
# V.  THE N = 255 RE-ASSERTION -- b25's dense verification of the column sweep, re-run
#     here so that this file's central object is licensed inside this file.
# ======================================================================================

def verify_dense():
    N = N_DENSE
    m, h, x = grid(N)
    F = dense_F(N)
    dft = DFT(N)
    rng = np.random.default_rng(20260818)
    v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    v = v / np.linalg.norm(v)

    e = float(np.linalg.norm(dft.F(v) - F @ v))
    check("V1  FFT matvec == dense centered F (N = %d)" % N, e < FFT_TOL, "%.3e" % e)
    e = float(np.linalg.norm(dft.Fi(v) - F.conj().T @ v))
    check("V2  FFT matvec == dense F^dagger (N = %d)" % N, e < FFT_TOL, "%.3e" % e)

    X = np.diag(x)
    Ptil = F @ X @ F.conj().T
    e = float(np.linalg.norm(dft.F(x * dft.Fi(v)) - Ptil @ v))
    check("V3  Ptil matvec == dense F X F^dagger (N = %d)" % N, e < FFT_TOL, "%.3e" % e)

    Dd = (X @ Ptil + Ptil @ X) / 2.0
    j = 77
    ej = np.zeros(N, dtype=complex)
    ej[j] = 1.0
    e = float(np.linalg.norm(((x + x[j]) / 2.0) * (Ptil @ ej) - Dd @ ej))
    check("V4  the D column identity  D e_j = ((x + x_j)/2) .* (Ptil e_j)  (N = %d)" % N,
          e < FFT_TOL, "%.3e" % e)

    print()
    print("  the column sweep against the dense Frobenius norm, G = %s, all four a:"
          % BANKED_SHAPE)
    print("  %-8s %-20s %-20s %-12s %-12s" %
          ("a", "dense ||G D G||_F", "sweep ||G D G||_F", "|diff|", "rel"))
    worst = 0.0
    for a, alab in AS:
        g = window(x, a, BANKED_SHAPE)
        q_dense = float(np.linalg.norm((g[:, None] * Dd) * g[None, :]))
        q_sweep = GDG_frobenius(dft, x, g)
        d = abs(q_dense - q_sweep)
        rel = d / max(q_dense, 1e-300)
        worst = max(worst, rel)
        print("  %-8s %-20.12f %-20.12f %-12.3e %-12.3e" % (alab, q_dense, q_sweep, d, rel))
    print()
    check("V5  ||G D G||_F COLUMN SWEEP == DENSE at N = %d, all four a, relative "
          "agreement <= %.0e (b25's verification RE-ASSERTED here; worst rel = %.3e, "
          "i.e. ~1e-%d as banked)" % (N, SWEEP_REL_TOL, worst,
                                      int(math.floor(-math.log10(max(worst, 1e-300))))),
          worst <= SWEEP_REL_TOL, "worst rel %.3e" % worst)


# ======================================================================================
# THE MEASUREMENT
# ======================================================================================

def fit_exponent(Ns, Qs):
    """least-squares slope of log Q against log N over ALL points, reported as measured."""
    lx = np.log(np.array(Ns, dtype=float))
    ly = np.log(np.array(Qs, dtype=float))
    A = np.vstack([lx, np.ones_like(lx)]).T
    sol, _, _, _ = np.linalg.lstsq(A, ly, rcond=None)
    return float(sol[0])


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 12 (item 2) -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return

    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    t_start = time.time()

    print("=" * 100)
    print("V.  VERIFICATION AT N = %d (dense matrix vs the FFT column sweep) -- before any "
          "measurement" % N_DENSE)
    print("=" * 100)
    verify_dense()
    print()
    sys.stdout.flush()

    print("=" * 100)
    print("M.  Q_HS(a) = h * ||G D G||_F,  h = sqrt(2 pi / N),  G = %s,  "
          "D = (X Ptil + Ptil X)/2" % BANKED_SHAPE)
    print("=" * 100)
    print("    ROUTE: b25's exact column sweep (blocks of 128 columns; each block is one")
    print("    F^dagger and one F on a 128-column bundle, so the N = 16383 sweep is 16383")
    print("    matvecs carried as 128 blocked FFT pairs).  NOTHING IS SUBSAMPLED: every one")
    print("    of the N^2 entries of G D G enters the sum.")
    print()

    RAW = {}
    QHS = {}
    for N in SWEEP_NS:
        m, h, x = grid(N)
        dft = DFT(N)
        t0 = time.time()
        for a, alab in AS:
            g = window(x, a, BANKED_SHAPE)
            fr = GDG_frobenius(dft, x, g)
            RAW[(alab, N)] = fr
            QHS[(alab, N)] = h * fr
        print("    N = %-6d h = %.10f   sweep done for all four a  [%.1f s]"
              % (N, h, time.time() - t0))
        sys.stdout.flush()
    print()

    print("--- THE TABLE, per (a, N) ---")
    print("  %-8s %-8s %-20s %-14s %-20s" %
          ("a", "N", "raw ||G D G||_F", "h", "Q_HS = h * ||.||_F"))
    print("  " + "-" * 74)
    for a, alab in AS:
        for N in SWEEP_NS:
            print("  %-8s %-8d %-20.10f %-14.10f %-20.10f"
                  % (alab, N, RAW[(alab, N)], h_of(N), QHS[(alab, N)]))
        print("  " + "-" * 74)
    print()

    print("--- THE RATIO BETWEEN SUCCESSIVE N, and the exponent it implies ---")
    print("    (N steps by a factor of almost exactly 4: %d -> %d -> %d; a converged"
          % (SWEEP_NS[0], SWEEP_NS[1], SWEEP_NS[2]))
    print("     quantity would show ratio 1.0000 in both steps.)")
    print("  %-8s %-14s %-14s %-14s %-14s %-14s"
          % ("a", "Q(4095)/Q(1023)", "exp", "Q(16383)/Q(4095)", "exp", "fitted exp (3 pts)"))
    print("  " + "-" * 84)
    fitted = {}
    raw_fitted = {}
    for a, alab in AS:
        q = [QHS[(alab, N)] for N in SWEEP_NS]
        r1 = q[1] / q[0]
        r2 = q[2] / q[1]
        e1 = math.log(r1) / math.log(SWEEP_NS[1] / float(SWEEP_NS[0]))
        e2 = math.log(r2) / math.log(SWEEP_NS[2] / float(SWEEP_NS[1]))
        ef = fit_exponent(SWEEP_NS, q)
        fitted[alab] = ef
        raw_fitted[alab] = fit_exponent(SWEEP_NS, [RAW[(alab, N)] for N in SWEEP_NS])
        print("  %-8s %-14.6f %-14.6f %-14.6f %-14.6f %-14.6f"
              % (alab, r1, e1, r2, e2, ef))
    print("  " + "-" * 84)
    print("    THE EXPONENTS ARE REPORTED AS MEASURED, NOT AS A CLAIM: they are the slope")
    print("    of log Q_HS against log N on the three registered grid sizes, nothing more.")
    print("    No asymptotic law is asserted from three points.")
    print()

    print("--- THE RAW (UNWEIGHTED) FROBENIUS, for the record beside sitting 11's ~N^0.77 ---")
    print("  %-8s %-22s %-22s" % ("a", "fitted exp of raw", "fitted exp of Q_HS"))
    for a, alab in AS:
        print("  %-8s %-22.6f %-22.6f" % (alab, raw_fitted[alab], fitted[alab]))
    print("    (h = sqrt(2 pi / N) contributes exactly -1/2 to the exponent; the two")
    print("     columns differ by 0.500000 by construction, and are printed so the")
    print("     arithmetic is visible rather than asserted.)")
    print()

    print("--- N-STABILITY, the registered (H-stable) criterion: >= %d agreeing digits ---"
          % STABLE_DIGITS)
    print("  %-8s %-20s %-20s %-14s %-10s"
          % ("a", "min Q_HS", "max Q_HS", "rel spread", "digits"))
    print("  " + "-" * 74)
    all_stable = True
    digits = {}
    for a, alab in AS:
        q = [QHS[(alab, N)] for N in SWEEP_NS]
        spread = max(q) - min(q)
        rel = spread / abs(float(np.mean(q)))
        dg = 15 if rel <= 0 else max(0, min(15, int(math.floor(-math.log10(rel)))))
        digits[alab] = dg
        st = rel < STABLE_REL
        all_stable = all_stable and st
        print("  %-8s %-20.10f %-20.10f %-14.3e %-10d %s"
              % (alab, min(q), max(q), rel, dg, "STABLE" if st else "MOVES"))
    print("  " + "-" * 74)
    print()

    # ---------------------------------------------------------------- the branch
    print("=" * 100)
    print("THE BRANCH")
    print("=" * 100)
    if all_stable:
        print("  BRANCH LANDED: (H-stable)")
        print("  Q_HS is N-stable to >= %d digits across N in {%s}.  It is a number."
              % (STABLE_DIGITS, ", ".join(str(N) for N in SWEEP_NS)))
        print()
        print("  ITS VALUE, beside the banked finite side (sitting 4, exact: 0 through")
        print("  a = 2; 6*sqrt(6) = %.9f at a = 3 on {inf,2,3}; 0 at a = 3 on {inf,2,3,5}):"
              % (6 * math.sqrt(6)))
        print("  %-8s %-20s %-20s %-22s %s"
              % ("a", "Q_HS (converged)", "finite {inf,2,3}", "FULL {inf,2,3}",
                 "FULL {inf,2,3,5}"))
        for a, alab in AS:
            qc = float(np.mean([QHS[(alab, N)] for N in SWEEP_NS]))
            fin23 = 6 * math.sqrt(6) if alab == "3" else 0.0
            print("  %-8s %-20.10f %-20.9f %-22.9f %.9f"
                  % (alab, qc, fin23, qc * fin23, 0.0))
        print("  THE PUNCTUATED LEDGER RE-READ WITH INFINITY LIVE: the infinity channel is")
        print("  a finite number at every a; the finite side's zeros still annihilate the")
        print("  product wherever they sit.  NO PROMOTION IS MADE; the register is untouched.")
    else:
        print("  BRANCH LANDED: (H-fails)")
        print("  The h-weighting does NOT make the infinity channel converge: growth")
        print("  persists across N in {%s} at every a."
              % ", ".join(str(N) for N in SWEEP_NS))
        print()
        print("  THE MEASURED EXPONENT, BANKED (three-point least-squares slope of")
        print("  log Q_HS against log N; measured, not claimed):")
        print("  %-8s %-18s %-18s %s"
              % ("a", "fitted exponent", "step exponents", "registered longhand"))
        for a, alab in AS:
            q = [QHS[(alab, N)] for N in SWEEP_NS]
            e1 = math.log(q[1] / q[0]) / math.log(SWEEP_NS[1] / float(SWEEP_NS[0]))
            e2 = math.log(q[2] / q[1]) / math.log(SWEEP_NS[2] / float(SWEEP_NS[1]))
            print("  %-8s %-18.6f %-18s ~1/4 = 0.250000"
                  % (alab, fitted[alab], "%.6f / %.6f" % (e1, e2)))
        mean_fit = float(np.mean([fitted[alab] for a, alab in AS]))
        print()
        print("  mean fitted exponent over the four a: %.6f  (the registered longhand said"
              % mean_fit)
        print("  ~1/4 = 0.250000, from removing N^(1/2) off sitting 11's measured ~N^0.77;")
        print("  the difference between the two is recorded as measured, with no fitting")
        print("  of anything else and no claim about the true asymptotics.)")
        print()
        print("  THE FAILURE'S CATEGORY, as registered in advance: this is the CONVENTION'S")
        print("  category, not the model's.  G D G is not Hilbert-Schmidt in the continuum")
        print("  because D is a first-order operator with a delta'-supported diagonal")
        print("  kernel, so no h-weighting of a grid Frobenius sum can converge.  The")
        print("  finite-place weight law Q(p,n) = ||S U S||_F is built on the GROUP ELEMENT")
        print("  U (bounded unitary); the infinity channel has been using the GENERATOR")
        print("  (unbounded).  The two are not the same convention.")
        print()
        print("  FILED WITH THE SECOND CANDIDATE (named and derived in the registration,")
        print("  NOT RUN THIS SITTING): the group-element convention -- the infinity")
        print("  channel measured on the bounded dilation U_lambda f(x) = lambda^(-1/2)")
        print("  f(x/lambda), mirroring U_p exactly, whose windowed h-weighted HS norm")
        print("  CONVERGES in the continuum (h Sum -> integral |g(lambda x) g(x)|^2 dx /")
        print("  lambda, finite).  Its declared implementation question, also filed: the")
        print("  grid representation of U_lambda at off-grid points (band-limited")
        print("  interpolation).  THE LEDGER KEEPS ITS CAVEAT: no infinity weight is")
        print("  promoted, and the register is untouched.")
    print()
    print("  LONGHAND EXPECTATION said before the run: (H-fails).  LANDED: %s.  %s"
          % ("(H-stable)" if all_stable else "(H-fails)",
             "The registered expectation did NOT land." if all_stable
             else "The registered expectation LANDED."))
    print()

    print("=" * 100)
    print("SCOPE, said plainly: this is a FLOAT BENCH on a CONSTRUCTED FINITE-GRID object.")
    print("It is DATA at bench grade.  No promotion to W_inf - Sum W_p at complete roster")
    print("is made, and no register line moves.")
    print("=" * 100)
    print()
    npass = sum(1 for c in CHECKS if c[1])
    for nm, ok, det in CHECKS:
        if not ok:
            print("  *** ASSERTION FAILED: %s (%s)" % (nm, det))
    print("TOTAL RUNTIME: %.1f s" % (time.time() - t_start))
    print()
    print("FLOAT BENCH COMPLETE; ASSERTED CHECKS: %d/%d PASS" % (npass, len(CHECKS)))


if __name__ == "__main__":
    main()
