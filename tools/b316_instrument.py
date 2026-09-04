# -*- coding: utf-8 -*-
"""b316_instrument.py -- A COMPUTABLE TRUNCATION OF THE OBJECT'S ARCHIMEDEAN SPACE.

### ### **THE FOUR NORMALIZATIONS, WRITTEN ONCE HERE AND USED EVERYWHERE**, each with the source's
### own equation number, because ### **EVERY NUMBER THIS INSTRUMENT PRINTS DEPENDS ON ALL FOUR AND
### ### THE LAST THREE ACTS EACH LOST A DAY TO ONE OF THEM:**
###   ### **(N1) THE INNER PRODUCT, eq. (16):**
###     ### `<eta|xi> := (1/2) INT_R eta xi dx = INT_0^inf eta xi dx`
###     ### **SO THE HALF-LINE PICTURE AND THE FULL-LINE PICTURE ARE THE SAME INNER PRODUCT**, and
###     the instrument is built on the half line because the source says the two agree.
###   ### **(N2) THE TRANSFORM, eq. (24):** ### `F(xi)(y) := INT_R xi(x) e^{-2 pi i x y} dx`,
###     which for an EVEN function is ### `2 INT_0^inf xi(x) cos(2 pi x y) dx` ### -- real, and
###     unitary on `L^2(R)_ev`.
###   ### **(N3) THE SCALING ACTION, eq. (61):** ### `(theta(lam) xi)(v) := lam^{-1/2} xi(lam^{-1} v)`
###     -- unitary, obtained by conjugating a unitary representation.
###   ### **(N4) THE SPACE, Definition 4.4 / eq. (72):**
###     ### `S(a,b) := { xi in L^2(R)_ev : xi(q) = 0 for |q| <= a, and F(xi)(p) = 0 for |p| <= b }`
###     ### and this instrument builds `S(1,1)`.

### ### ### **WHAT `TRUNCATION` MEANS HERE, STATED BEFORE ANYTHING IS CLAIMED.** ### The space is
### infinite-dimensional -- the source says so in as many words. ### **THIS INSTRUMENT IS A FINITE
### ### SECTION OF IT: EVEN FUNCTIONS ON `[0, X]` SAMPLED AT `N` MIDPOINTS, WITH BOTH CONDITIONS
### ### IMPOSED ON THAT GRID.** ### It is not the space and does not claim to be.

### ### **AND THE ONE EXACT FACT THIS INSTRUMENT HAS, KEPT APART FROM THE REST:** ### a function
### supported in `[0,1]` is orthogonal to every element of the space ### **BY DISJOINT SUPPORT**,
### and that is exact arithmetic on any grid whatever. ### **EVERYTHING ELSE HERE IS DOUBLE
### ### PRECISION AND IS DECLARED AS SUCH.**
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, E16)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE SOURCE'S EQUATION NUMBERS, CARRIED WITH THE CONSTANTS THEY NAME.
EQ_INNER, EQ_TRANSFORM, EQ_SCALING, EQ_SPACE = '(16)', '(24)', '(61)', '(72)'
ALPHA = 1.0   # ### Definition 4.4's `a`, at the source's own `S(1,1)`
BETA = 1.0    # ### Definition 4.4's `b`
MU_SONIN = '-20.48057322913694697'   # ### b214's printed first even NEGATIVE eigenvalue


class Frame(object):
    """### **THE TRUNCATION.** ### Even functions on `[0, X]`, `N` midpoints, spacing `h = X/N`.

    ### **MIDPOINTS RATHER THAN ENDPOINTS**, so that no node sits at `x = 0` (where an even
    ### function's derivative information is degenerate) and so that the quadrature weight is the
    ### same at every node -- which makes the inner product `(N1)` a plain scaled dot product and
    ### keeps orthonormality in the free coordinates equivalent to orthonormality in the space.
    """

    def __init__(self, N, X, NY=None):
        self.N, self.X = int(N), float(X)
        self.h = self.X / self.N
        self.x = (np.arange(self.N) + 0.5) * self.h
        self.w = np.full(self.N, self.h)
        # ### ### **THE TRANSFORM GETS ITS OWN GRID, AND THAT IS NOT A CONVENIENCE.**
        # ### The first version of this frame set `y = x`. ### That ties the number of
        # ### CONSTRAINTS -- the rows with `y <= 1` -- to `1/h`, while the number of FREE
        # ### coordinates grows like `X/h`. ### **SO THE SECOND CONDITION GETS WEAKER AND WEAKER
        # ### AS THE DOMAIN LENGTHENS, AND AT `X = 64` IT WAS WEAK ENOUGH TO ADMIT A VECTOR b292
        # ### DERIVED IS NOT IN THE SPACE.** ### `NY` samples `(0, 1]` independently of `X`.
        self.NY = int(NY) if NY else max(64, self.N // 8)
        self.hy = BETA / self.NY
        self.y = (np.arange(self.NY) + 0.5) * self.hy

    # ---------------------------------------------------------------- (N1)
    def inner(self, u, v):
        """### `<u|v>` OF eq. (16), ON THE HALF LINE."""
        return float(np.dot(self.w * u, v))

    def norm(self, u):
        return math.sqrt(max(self.inner(u, u), 0.0))

    # ---------------------------------------------------------------- (N2)
    def transform_matrix(self):
        """### eq. (24) FOR AN EVEN FUNCTION: ### `2 INT_0^inf xi(x) cos(2 pi x y) dx`."""
        return 2.0 * np.cos(2.0 * math.pi * np.outer(self.y, self.x)) * self.w[None, :]

    # ---------------------------------------------------------------- (N4)
    def masks(self):
        """### THE TWO CONDITIONS AS INDEX SETS. ### `lo_x` is forced to zero; EVERY `y` row
        ### constrains, because the `y` grid is built inside `[0, BETA]` and nowhere else."""
        return self.x <= ALPHA, self.y <= BETA

    def subspace(self, T=None):
        """### **THE CONSTRAINED SUBSPACE, AS A PROJECTOR ON THE FREE COORDINATES.**

        ### Condition one kills the coordinates with `x <= 1` outright. ### Condition two is
        ### `C f = 0` with `C = T[lo_y][:, hi_x]`, and the space is that null space.
        ### **THE PROJECTOR IS BUILT FROM AN ORTHONORMAL BASIS OF THE ROW SPACE, NOT OF THE NULL
        ### SPACE**, because the row space has the small dimension and the arithmetic is cheaper
        ### and better conditioned that way.
        """
        if T is None:
            T = self.transform_matrix()
        lo_x, lo_y = self.masks()
        hi_x = ~lo_x
        C = T[lo_y][:, hi_x]
        # ### `Q` spans the ROW space of `C`; the space is what `Q` misses.
        U, s, Vt = np.linalg.svd(C, full_matrices=False)
        tol = max(C.shape) * (s[0] if s.size else 0.0) * np.finfo(float).eps
        rank = int((s > tol).sum())
        Q = Vt[:rank].T                       # ### (free coords) x rank, orthonormal columns
        return dict(hi=hi_x, lo_x=lo_x, lo_y=lo_y, C=C, Q=Q, rank=rank,
                    free=int(hi_x.sum()), dim=int(hi_x.sum()) - rank, sing=s)

    def project(self, sub, f):
        """### `S f` -- the component of `f` INSIDE the space (free coordinates only)."""
        g = f[sub['hi']].copy()
        return g - sub['Q'] @ (sub['Q'].T @ g)

    def outside(self, sub, f):
        """### `(1 - S) f` -- the component that is NOT in the space."""
        g = f[sub['hi']]
        return sub['Q'] @ (sub['Q'].T @ g)

    def embed(self, sub, g):
        """### A free-coordinate vector back onto the whole grid, zero on `[0,1]`."""
        f = np.zeros(self.N)
        f[sub['hi']] = g
        return f

    # ---------------------------------------------------------------- (N3)
    def scaling(self, lam, f):
        """### eq. (61): ### `(theta(lam) f)(v) = lam^{-1/2} f(lam^{-1} v)`, by interpolation.

        ### **OUTSIDE THE DOMAIN THE VALUE IS TAKEN AS ZERO, AND THAT IS THE TRUNCATION SHOWING.**
        ### For `lam >= 1` the argument `v/lam` stays inside `[0, X]`, so no extrapolation happens
        ### and the only error is interpolation.
        """
        arg = self.x / lam
        return (lam ** -0.5) * np.interp(arg, self.x, f, left=0.0, right=0.0)


def gaussian(fr):
    """### **THE POSITIVE CONTROL FOR THE TRANSFORM.** ### `e^{-pi x^2}` is its own transform under
    ### eq. (24), so recovering it is a check on the discretization and NOT on the corpus."""
    return np.exp(-math.pi * fr.x ** 2)


def sonin_unit(fr, dps=25, ncoef=60, nsteps_per_unit=40, order=12, mu_str=None):
    """### **b300's `u_inf`, ON THIS GRID, FROM THE CORPUS'S OWN SOLVER.**

    ### `u_inf` is `phi_mu` at the first even NEGATIVE eigenvalue, normalized in `L^2`: the unique
    ### even solution that is ZERO on `[-1,1]` and agrees with the radial solution beyond it.
    ### **CONDITION ONE IS THEREFORE EXACT BY CONSTRUCTION AND CONDITION TWO IS THE ONE TO
    ### ### MEASURE.**
    ### The Frobenius series is valid to about `x = 2.5`; beyond that the corpus's own marcher
    ### carries it, and both come from `b205_prolate.py` rather than from anything written here.
    """
    from mpmath import mp, mpf
    import b205_prolate as P
    mp.dps = dps
    mu, tau = mpf(mu_str or MU_SONIN), 2 * mp.pi
    XS = mpf('2.5')
    out = np.zeros(fr.N)
    inner = [j for j in range(fr.N) if 1.0 < fr.x[j] <= float(XS)]
    for j in inner:
        y, _dy = P.yI_eval(mu, tau, mpf(float(fr.x[j])), ncoef)
        out[j] = float(y)
    y, dy = P.yI_eval(mu, tau, XS, ncoef)
    cur = XS
    for j in range(fr.N):
        if fr.x[j] <= float(XS):
            continue
        tgt = mpf(float(fr.x[j]))
        ns = max(2, int(nsteps_per_unit * float(tgt - cur)) + 2)
        y, dy = P.integrate_in(mu, tau, cur, tgt, y, dy, ns, order)
        cur = tgt
        out[j] = float(y)
    n = fr.norm(out)
    return (out / n) if n > 0 else out


def taper(fr, u, frac=8.0):
    """### **THE EDGE DIAGNOSTIC.** ### Replace the hard cut at `X` with a raised-cosine over the
    ### last `1/frac` of the domain. ### **IF THE VIOLATION OF CONDITION TWO IS THE STEP AT THE END
    ### OF THE DOMAIN, THIS MOVES IT; IF IT IS THE VECTOR, THIS DOES NOT.** ### The tapered vector
    ### is NOT `u_inf` and is used for nothing but this comparison."""
    x0 = fr.X * (1.0 - 1.0 / float(frac))
    w = np.ones(fr.N)
    m = fr.x > x0
    w[m] = 0.5 * (1.0 + np.cos(math.pi * (fr.x[m] - x0) / (fr.X - x0)))
    v = u * w
    n = fr.norm(v)
    return (v / n) if n > 0 else v


def asymptotics(fr, u, x_lo=2.0):
    """### **WHAT `x u(x)` DOES FAR OUT.** ### b300's `u_inf` should go like `sin(2 pi x)/x`, so
    ### `x u` should be BOUNDED and should change sign twice per unit. ### Returns the bound, the
    ### sign-change count, and what `sin(2 pi x)` would give on the same interval.
    ### **THIS MEASURES THE DECAY AND THE FREQUENCY. ### IT DOES NOT MEASURE THE EIGENVALUE, AND
    ### THE CALLER IS OBLIGED TO SAY SO.**"""
    m = fr.x > float(x_lo)
    xu = fr.x[m] * u[m]
    sgn = np.sign(xu)
    sgn = sgn[sgn != 0]
    changes = int(np.sum(sgn[1:] != sgn[:-1]))
    # ### the zeros of `sin(2 pi x)` sit at the half-integers; count the ones the NODES
    # ### actually straddle, not the ones the nominal domain would contain.
    expect = int(math.floor(2.0 * float(fr.x[m][-1]))) - int(math.floor(2.0 * float(x_lo)))
    return (float(np.max(xu)), float(np.min(xu)), changes, expect, int(np.sum(m)))


def far_bound(fr, u, x_lo=8.0):
    """### **THE DISCRIMINATION ARM FOR `asymptotics`**: the same bound measured deeper out, so it
    ### can be compared across values of `mu`. ### **IF NON-EIGENVALUES GIVE THE SAME NUMBER, THE
    ### CONTROL CANNOT FIRE AND MUST BE REPORTED AS NOT-A-CHECK** (b308's law)."""
    m = fr.x > float(x_lo)
    return float(np.max(np.abs(fr.x[m] * u[m])))


def self_test():
    """### **FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    fr = Frame(256, 8.0)
    # ### (i) the inner product is eq. (16)'s, and it is a scaled dot product.
    u = np.ones(fr.N)
    ok.append(abs(fr.inner(u, u) - fr.X) < 1e-12)
    # ### (ii) the transform recovers the Gaussian -- and FAILS on a wrong normalization.
    T = fr.transform_matrix()
    g = gaussian(fr)
    gy = np.exp(-math.pi * fr.y ** 2)   # ### the Gaussian AT THE TRANSFORM'S OWN NODES
    good = float(np.max(np.abs(T @ g - gy)))
    bad = float(np.max(np.abs((T / 2.0) @ g - gy)))
    ok.append(good < 1e-8)
    ok.append(bad > 1e-3)
    # ### (iii) the scaling action is unitary in the inner product, for `lam >= 1`, ON A FUNCTION
    # ### WHOSE IMAGE STAYS INSIDE THE DOMAIN -- and NOT on one whose image leaves it. ### **THE
    # ### SECOND ARM IS THE ONE THAT MATTERS: IT SHOWS THE TRUNCATION IS VISIBLE RATHER THAN
    # ### SILENT.**
    v = np.exp(-8.0 * (fr.x - 1.5) ** 2)
    ok.append(abs(fr.norm(fr.scaling(2.0, v)) - fr.norm(v)) < 1e-3)
    far = np.exp(-8.0 * (fr.x - 6.0) ** 2)
    ok.append(abs(fr.norm(fr.scaling(2.0, far)) - fr.norm(far)) > 1e-2)
    # ### (iv) the subspace's projector is idempotent and its complement is orthogonal to it.
    sub = fr.subspace(T)
    f = np.zeros(fr.N)
    f[sub['hi']] = np.random.default_rng(0).standard_normal(sub['free'])
    p = fr.project(sub, f)
    ok.append(float(np.max(np.abs(fr.project(sub, fr.embed(sub, p)) - p))) < 1e-9)
    ok.append(abs(float(np.dot(p, fr.outside(sub, f)))) < 1e-9)
    # ### (v) a vector supported in [0,1] projects to EXACTLY zero -- disjoint support.
    s = np.zeros(fr.N)
    s[fr.x <= 1.0] = 1.0
    ok.append(float(np.max(np.abs(fr.project(sub, s)))) == 0.0)
    # ### (vi) the taper is near-identity on a vector already small at the edge, and NOT on one
    # ### that is not -- so a null result from it is a real null result.
    quiet = np.exp(-2.0 * (fr.x - 2.0) ** 2)
    loud = np.ones(fr.N) / math.sqrt(fr.X)
    ok.append(float(np.max(np.abs(taper(fr, quiet) - quiet / fr.norm(quiet)))) < 1e-6)
    ok.append(float(np.max(np.abs(taper(fr, loud) - loud))) > 1e-2)
    # ### (vii) the sign counter is EXACT on a function whose sign changes are known, and gives
    # ### the WRONG count on one at twice the frequency -- so it counts frequency, not noise.
    right = np.sin(2.0 * math.pi * fr.x) / fr.x
    twice = np.sin(4.0 * math.pi * fr.x) / fr.x
    a1 = asymptotics(fr, right)
    a2 = asymptotics(fr, twice)
    ok.append(a1[2] == a1[3])
    ok.append(a2[2] != a2[3])
    return all(ok), ok


if __name__ == '__main__':
    good, arms = self_test()
    print('b316_instrument self-test : %s  %s' % (arms, 'PASS' if good else 'FAIL'))
    sys.exit(0 if good else 1)
