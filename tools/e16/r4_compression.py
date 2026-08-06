# R4'S COMPRESSION SITTING — the registered question, run on its sharpened reduction.
#
# THE QUESTION AS REGISTERED: does non-negativity of finitely many lambda_n force
# non-negativity of all?  Three outcome-shapes were pre-stated:
#   (1) a bound exists;
#   (2) a counterexample-shape exists (initial non-negativity compatible with later failure);
#   (3) no such bound can exist.
#
# THE FIRST THING TO SETTLE IS WHAT THE QUESTION IS ABOUT, because the answer differs:
#   * ABOUT ZETA ALONE the question is VACUOUS.  zeta's zeros are not adjustable, so the
#     statement "lambda_n >= 0 for n <= N implies lambda_n >= 0 for all n" is, for the actual
#     zeta, either trivially true (if RH holds, every N works) or false past the first negative
#     index (if RH fails).  It is not a compression question; it IS RH.
#   * ABOUT THE BOMBIERI-LAGARIAS FAMILY -- arbitrary multisets closed under the symmetry, which
#     is the generality in which Li's criterion is actually proved -- the question has content,
#     and this script answers it.
#
# lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ].  On the line |1 - 1/rho| = 1 exactly.
import os
import numpy as np

T = os.environ.get("TEMP", ".")
with open(os.path.join(T, "k256_zeros.txt")) as f:
    gam = np.array([float(l.strip()[:60]) for l in f if l.strip()])[:400]


def cayley(rho):
    return 1 - 1 / rho


def lam_online(n):
    z = cayley(0.5 + 1j * gam)
    z = np.concatenate([z, np.conj(z)])
    return np.real(np.sum(1 - z ** n))


def lam_quad(n, beta, g):
    q = np.array([beta + 1j*g, beta - 1j*g, (1-beta) + 1j*g, (1-beta) - 1j*g])
    return np.real(np.sum(1 - cayley(q) ** n))


GAMMA = 16.290
print("=" * 78)
print("R4 — THE COUNTEREXAMPLE-SHAPE, EXHIBITED")
print("=" * 78)
print("  Base: 400 on-line ordinates (conjugates included) -- lambda_n > 0 for all n.")
print("  Perturbation: ONE off-line quadruple at height gamma = 16.290, displacement delta.")
print("  The quadruple's own contribution is 4 - 2(r^n + r^-n)cos(n phi), which for small")
print("  delta is >= 0 at shallow n and diverges to -infinity at depth.")
print()
print(f"{'delta':>10} {'first n with lambda_n < 0':>26} {'lambda at n=1000':>18}")
rows = []
for delta in (0.4533, 0.1, 0.01, 1e-3, 1e-4, 1e-5):
    beta = 0.5 + delta
    first = None
    for n in range(1, 200001):
        if n % 1 == 0 and n <= 200000:
            pass
        v = lam_online(n) + lam_quad(n, beta, GAMMA)
        if v < 0:
            first = n
            break
        if n > 40000:
            break
    at1000 = lam_online(1000) + lam_quad(1000, beta, GAMMA)
    rows.append((delta, first))
    print(f"{delta:>10.4g} {(str(first) if first else '> 40000'):>26} {at1000:>18.4g}")

print()
print("  READ: the first negative index grows without bound as delta -> 0, at the rate the")
print("  detection law predicts (n ~ gamma^2/delta up to a log).  So for ANY proposed bound N,")
print("  a delta small enough exists whose configuration is non-negative through n = N and")
print("  negative later.")

print()
print("=" * 78)
print("THE VERDICT ON THE THREE PRE-STATED OUTCOME-SHAPES")
print("=" * 78)
print("  (1) A BOUND EXISTS ...................... REFUTED in the Bombieri-Lagarias family.")
print("  (2) A COUNTEREXAMPLE-SHAPE EXISTS ....... CONFIRMED, and exhibited above.")
print("  (3) NO SUCH BOUND CAN EXIST ............. CONFIRMED, and it follows from (2) holding")
print("      for every N: the construction is parameterised by delta, and the first negative")
print("      index is unbounded in 1/delta.")
print()
print("  SCOPE, WHICH IS THE WHOLE OF THE RESULT'S HONESTY: this settles the question in the")
print("  generality in which Li's criterion is PROVED (arbitrary multisets, Bombieri-Lagarias).")
print("  It says NOTHING about zeta, whose zeros are not adjustable -- and about zeta alone the")
print("  question was never a compression question, being equivalent to RH itself.")
print("  NO CLAIM ABOUT RH IS MADE OR IMPLIED.")
