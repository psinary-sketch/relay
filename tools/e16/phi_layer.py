"""THE eta-COORDINATE LAYER — Phi on V, the negative fractions, and the delta/L curve.

Formulas as supplied (Selecta (103)/(105) and the eta reformulation):

    V     = { eta : int e^{-t/2} eta(t) dt = 0 }
    xi    = Y+ * eta,      Y+(s) = e^{s/2} 1_{s>=0}
    K_I   kernel = Qeps(exp|v|) / (2 eps'(1+))
    N_I   = -2 eps'(1+) (Id - K_I)
    Phi(eta) = <xi | N_I xi> + 2 sqrt(2) log 2 (eta * eta^*)(log 2)

Sitting 11's reading, used verbatim here:
    offenders = directions where Phi > 0 = NEGATIVE eigenvalues of G, with
    Phi <= 0  <=>  eta^T G eta >= 0.     So G = -(matrix of Phi).

NOTE RIDING EVERY log-3 ROW: their Prop 5.5 states window length <= log 2. The log-3
use is the sitting-11/12 EXTENSION and carries the Lemma 5.2 (1,3] re-derivation debt.
"""
import math
import numpy as np
import qeps_layer as Q

_qcache = {}


def _qvals(omega, nmax, NG=300):
    key = (round(omega, 12), nmax, NG)
    if key in _qcache:
        return _qcache[key]
    ks = np.arange(nmax + 1)
    rho = np.exp(omega * ks)
    v = np.array([0.0] + [Q.Qeps(float(r), 700, NG) for r in rho[1:]])
    _qcache[key] = v
    return v


def phi_matrix(L, omega, NG=300):
    """Symmetric matrix of Phi in the eta coordinate, restricted to V."""
    e1 = Q.epsprime1()
    ell = math.log(L)
    M = int(round(ell / omega))
    t = (np.arange(M) + 0.5) * omega

    # Y+ * eta  (lower triangular, trapezoid-free midpoint rule)
    d = t[:, None] - t[None, :]
    Y = np.where(d >= 0, np.exp(d / 2.0), 0.0) * omega

    # K_I on the same grid
    qv = _qvals(omega, M, NG)
    K = qv[np.abs(np.arange(M)[:, None] - np.arange(M)[None, :])] * (omega / (2 * e1))

    # <xi | N_I xi> with N_I = -2 eps'(1+) (Id - K_I); inner product carries one omega
    N = -2 * e1 * (np.eye(M) - K)
    A = omega * (Y.T @ N @ Y)

    # 2 sqrt2 log2 (eta * eta^*)(log 2): autocorrelation at lag log 2
    k = int(round(math.log(2) / omega))
    B = np.zeros((M, M))
    if 0 < k < M:
        idx = np.arange(M - k)
        B[idx + k, idx] = 1.0
        B = 0.5 * (B + B.T) * omega
    A = A + 2 * math.sqrt(2) * math.log(2) * B
    A = 0.5 * (A + A.T)

    # restrict to V = {eta : int e^{-t/2} eta = 0}
    c = np.exp(-t / 2.0) * omega
    c = c / np.linalg.norm(c)
    Pb = np.eye(M) - np.outer(c, c)
    # orthonormal basis of V
    _, _, Vt = np.linalg.svd(Pb)
    B0 = Vt[:M - 1].T
    return B0.T @ A @ B0, M


def negative_fraction(L, omega, NG=300):
    """Fraction of directions in V on which Phi > 0 (sitting 11's 'offenders')."""
    A, M = phi_matrix(L, omega, NG)
    ev = np.linalg.eigvalsh(A)
    npos = int((ev > 0).sum())          # Phi > 0  <=>  negative eigenvalue of G = -A
    return npos, len(ev), npos / len(ev), M
