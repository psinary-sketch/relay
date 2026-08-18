"""B13 — THE TENSOR CHECK (held since B7's rider; RELEASED by the author).

Relay-only. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE QUESTION AND THE LONGHAND DERIVATION, REGISTERED BEFORE ANY NUMBER
======================================================================
Does S_p on the local model factor as S_1 (x) S_1 under the coordinate chart
m = a + p^n b, (a, b) in (Z/p^n)^2?  (The chart is a SET bijection, not a ring
decomposition; the DFT kernel couples the factors -- e(aa'/p^{2n}) -- so a tensor
factorization of Son is a FINDING, not a formality.)

LONGHAND (this registration's own derivation, to be certified below):
  * the ball {p^n | m} is exactly {a = 0}, so  f|_B = 0  <=>  f(0, b) = 0 for all b
    <=>  f in V_1 (x) L^2,  V_1 = {v : v(0) = 0},  dim p^n - 1.
  * f-hat(0, b') = c * Sum_a e(ab'/p^n) * (Sum_b f(a, b)) -- the a'=0 Fourier rows see
    only the b-MARGINALS; vanishing for all b' <=> every b-slice sums to zero
    <=>  f in L^2 (x) W_1,  W_1 = {w : Sum w = 0},  dim p^n - 1.
  * the intersection of V_1 (x) L^2 and L^2 (x) W_1 is V_1 (x) W_1 exactly.  Hence
        Son(p, n) = V_1 (x) W_1,     S = P_1 (x) Q_1,
    P_1 = diag(0,1,...,1) (position-vanishing at 0), Q_1 = I - mean projector
    (frequency-vanishing at 0).  dim = (p^n - 1)^2 -- the first law EXPLAINED.
  * THE TWO FACTORS ARE FOURIER-DUAL one-point-vanishing conditions: position side
    and frequency side of the SAME condition -- a self-product-in-miniature whose
    factors are exchanged by the transform.

REGISTERED VERDICTS:
  T1  SELF-PRODUCT-STRUCTURE: operator-Schmidt rank of S (reshaped (aa'),(bb')) = 1
      and the factors match P_1, Q_1 to machine precision, at every cell.  Filed at
      question grade, OURS: the finite place holds a self-product in miniature -- the
      local shadow of "what supplies the leaves" -- cross-linked to column (vi) and
      Road A's absence.  NO PROMOTION: a local tensor square is not a global
      self-product, said on the face.
  T2  NOT-A-TENSOR: Schmidt rank > 1 somewhere -- the derivation above is then WRONG
      and is withdrawn with the failing cell named; the square is a coincidence.
  T3  third shape, filed openly.

Usage:  python b13_tensor.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8

CELLS = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1), (5, 2)]


def check(p, n):
    N, K = B8.sonin_basis(p, n)
    S = K @ K.conj().T
    pn = p ** n
    # reshape S_{(m),(m')} with m = a + pn*b  ->  M_{(a,a'),(b,b')}
    S4 = S.reshape(pn, pn, pn, pn)          # indices (b, a, b', a')?  m = a + pn*b -> row-major: m index = a + pn*b
    # numpy reshape of index m into (x, y) with m = x*pn + y gives x = b? m = a + pn*b -> m = pn*b + a: first index b, second a
    Sr = S4.transpose(1, 3, 0, 2).reshape(pn * pn, pn * pn)   # (a, a', b, b') -> rows (a,a'), cols (b,b')
    sv = np.linalg.svd(Sr, compute_uv=False)
    rank = int((sv > sv[0] * 1e-10).sum())
    # extract rank-1 factors and compare to P1, Q1
    U, s, Vh = np.linalg.svd(Sr)
    A = (U[:, 0] * np.sqrt(s[0])).reshape(pn, pn)
    Bf = (Vh[0, :] * np.sqrt(s[0])).reshape(pn, pn)
    P1 = np.diag(np.array([0.0] + [1.0] * (pn - 1)))
    Q1 = np.eye(pn) - np.ones((pn, pn)) / pn
    # fix sign/scale: A ~ c*P1, B ~ Q1/c
    c = A[1, 1] if pn > 1 else 1.0
    errA = np.linalg.norm(A / c - P1)
    errB = np.linalg.norm(Bf * c - Q1)
    return N, S.shape[0], rank, sv[0], (sv[1] if len(sv) > 1 else 0.0), errA, errB


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("B13 — THE TENSOR CHECK · REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("  %-4s %-4s %-8s %-7s %-12s %-12s %-12s %-12s"
          % ("p", "n", "N", "SchmidtRk", "sv[0]", "sv[1]", "|A-P1|", "|B-Q1|"))
    for p, n in CELLS:
        N, dim, rank, s0, s1, eA, eB = check(p, n)
        print("  %-4d %-4d %-8d %-7d %-12.4e %-12.4e %-12.3e %-12.3e"
              % (p, n, N, rank, s0, s1, eA, eB))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
