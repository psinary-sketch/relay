"""b313 FLIPPED COPY (NOT AN OWNER FILE) -- Q_eps AND THE OPERATOR LAYER — from the formulas supplied at content (Selecta).

Builds on prolate_layer.py, which is certified 15/15 against the banked prolate/eps rows.

FORMULAS AS SUPPLIED (arXiv-v1 / Selecta numbering):

  (b)  xi_n^an(x)     = (2/lam) int_0^1 xi_n(t) cos(2 pi t x) dt          [entire]
       (xi_n^an)'(x)  = -(4 pi/lam) int_0^1 t xi_n(t) sin(2 pi t x) dt
       zeta_n(x)      = [lam/sqrt(1-lam^2)] xi_n^an(x) for x >= 1, else 0

  (c)  eps(rho), their (85), rho >= 1:
       eps(rho) = sum_n [lam/sqrt(1-lam^2)] <xi_n | theta(rho^-1) zeta_n>
       integrand supported ONLY on u in [rho^-1, 1]   -> eps(1) = 0

  (d)  Qeps, their Prop 5.3 / eq (100), rho > 1:
       Qeps(rho) = sum_n [lam^2/(1-lam^2)] C_n(rho)
       C_n(rho) = rho^(1/2)  int_{rho^-1}^{1} [x (xi^an)'(x)][rho x (xi^an)'(rho x)] dx
                + rho^(-3/2) (xi^an)'(rho^-1) xi^an(1)
                - rho^(3/2)  xi^an(1) (xi^an)'(rho)
       Qeps(1) = 0 identically.  Truncation: first 11 terms uniform to 1e-11 (Lemma F.1).

  (e)  K_I kernel = Qeps(exp|v|)/(2 eps'(1+));  N_I = -2 eps'(1+) (Id - K_I)
       Toeplitz entries Qeps(q^|i-j|), reference omega/(2 eps'(1+)) vs 1.

  (f)  V = {eta : int e^{-t/2} eta(t) dt = 0};  xi = Y+ * eta, Y+(s) = e^{s/2} 1_{s>=0}
       Phi(eta) = <xi | N_I xi> + 2 sqrt2 log2 (eta * eta^*)(log 2)

THE SCALING OPERATOR. theta(a) f(x) = a^{1/2} f(x/a) is the convention forced by the
supplied support law: theta(rho^-1) zeta_n(u) = rho^{-1/2} zeta_n(rho u), nonzero for
u >= rho^-1, which against xi_n on [0,1] gives exactly the stated support [rho^-1, 1].

CONSEQUENCE DERIVED HERE, NOT ASSUMED: differentiating (85) at rho = 1 gives
eps'(1+) = sum_n [lam^2/(1-lam^2)] xi_n(1)^2 -- i.e. exactly the t(n) of CC Lemma 5.4,
which was inferred structurally in part 2 and is now derived from the supplied formula.
"""
import math
import numpy as np

import prolate_layer as PL

NTERM = 11          # Lemma F.1: first 11 terms uniform to 1e-11
_cache = {}


def layer(NQ=700):
    """xi_n samples on [-1,1] Gauss nodes, |lam|, and the analytic continuation maps."""
    if NQ in _cache:
        return _cache[NQ]
    x, w, mu, psi, psi1 = PL.prolate(NQ)
    lam2 = mu[0::2][:NTERM]                       # P1: even index only
    lam = np.sqrt(lam2)                           # sign cancels: C_n is even in xi^an
    xi = math.sqrt(2) * psi[:, 0::2][:, :NTERM]   # P2: half-line norm
    xi1 = math.sqrt(2) * psi1[0::2][:NTERM]
    # orient each xi_n so that xi_n(1) > 0 (fixes the arbitrary eigenvector sign)
    s = np.sign(xi1); s[s == 0] = 1.0
    xi = xi * s[None, :]
    xi1 = xi1 * s

    def an(X):
        """xi_n^an(X) for array X -> shape (len(X), NTERM). Even in t, so int_0^1 = half."""
        C = np.cos(2 * math.pi * np.outer(X, x))          # (len X, NQ)
        return (C * w) @ xi / lam

    def dan(X):
        """(xi_n^an)'(X). t*xi_n(t)*sin is even, so int_0^1 = half of int_-1^1."""
        S = np.sin(2 * math.pi * np.outer(X, x))
        return -2 * math.pi * ((S * (w * x)) @ xi) / lam

    out = (x, w, lam, lam2, xi, xi1, an, dan)
    _cache[NQ] = out
    return out


def Qeps(rho, NQ=700, NG=400):
    """Qeps at scalar or array rho, via eq (100)."""
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    a1 = an(np.array([1.0]))[0]                  # xi_n^an(1)
    out = np.empty(len(rho))
    gx, gw = np.polynomial.legendre.leggauss(NG)
    for k, r in enumerate(rho):
        lo, hi = 1.0 / r, 1.0
        if hi - lo <= 0:
            out[k] = 0.0
            continue
        t = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        jac = 0.5 * (hi - lo)
        d1 = dan(t)                               # (NG, NTERM)
        d2 = dan(r * t)
        integ = ((t[:, None] * d1) * (r * t[:, None] * d2) * (gw[:, None] * jac)).sum(0)
        C = (r ** 0.5) * integ \
            + (r ** -1.5) * dan(np.array([1.0 / r]))[0] * a1 \
            - (r ** 1.5) * a1 * dan(np.array([r]))[0]
        out[k] = float((lam2 / (1 - lam2) * C).sum())
    return out if out.size > 1 else float(out[0])


def eps(rho, NQ=700, NG=400):
    """eps at scalar or array rho, via (85) with theta(a)f(x) = a^{-1/2} f(x/a)."""
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    out = np.empty(len(rho))
    gx, gw = np.polynomial.legendre.leggauss(NG)
    # xi_n on [0,1] equals xi_n^an there; use the continuation for a common evaluator
    for k, r in enumerate(rho):
        lo, hi = 1.0 / r, 1.0
        if hi - lo <= 0:
            out[k] = 0.0
            continue
        u = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        jac = 0.5 * (hi - lo)
        I = ((an(u) * an(r * u)) * (gw[:, None] * jac)).sum(0)
        out[k] = float((lam2 / (1 - lam2) * (r ** 0.5) * I).sum())
    return out if out.size > 1 else float(out[0])


def epsprime1(NQ=700):
    """eps'(1+) = sum_n [lam^2/(1-lam^2)] xi_n(1)^2, derived from (85) at rho=1."""
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    return float((lam2 / (1 - lam2) * xi1 ** 2).sum())
