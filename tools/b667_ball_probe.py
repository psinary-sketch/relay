# -*- coding: utf-8 -*-
"""b667_ball_probe.py -- THE SEGMENT ENCLOSURE'S SECOND OBSTRUCTION, MEASURED: acb.bessel_k ON A BALL IN THE ORDER, AND THE EXPLICIT
DERIVATIVE BOUND THAT WOULD REPLACE ITS PROPAGATION.

### The plan (relay data/b667_epstein_plan.txt section 5) encloses Z_Q on a segment by the route of section 2 evaluated on the segment's ball.
### A scratch smoke test (no banked point) found the result's radius 10^19-10^43 times r·|Z'| on balls of radius r about 0.7 + 40.25i and
### 0.7 + 140.25i: acb.bessel_k propagates a radius in its order ν by a bound that does not see K's e^{−π|t|/2} cancellation.
### THE BOUND MEASURED HERE (derived in the plan's section 14 if the author takes it): K_ν(x) = ½ ∫_ℝ e^{−x cosh u − νu} du (DLMF 10.32.9, even
### in u), so ∂_ν K_ν(x) = −½ ∫_ℝ u e^{−x cosh u − νu} du; shifting ℝ to ℝ − iθ with θ t > 0, |θ| < π/2 (Cauchy; Re(x cosh(u − iθ)) =
### x cosh u cos θ > 0), with ν = μ + it: |e^{−x cosh(u−iθ) − ν(u−iθ)}| = e^{−x cos θ cosh u − μu − tθ}, |u − iθ| ≤ |u| + |θ|, and
### e^{−μu} ≤ e^{|μ||u|}, |u| e^{|μ||u|} ≤ e^{−1} e^{(|μ|+1)|u|}, ∫_ℝ e^{−a cosh u + λ|u|} du = 2 ∫_0^∞ e^{−a cosh u + λu} du ≤ 4 K_λ(a):
###   |∂_ν K_ν(x)| ≤ 2 e^{−|t|·|θ|} ( |θ| K_{|μ|}(a) + e^{−1} K_{|μ|+1}(a) ),  a = x cos θ,
### uniform over a ball of ν when |t| is its least |Im ν| and |μ| its largest |Re ν| (θ = 0 where the ball meets Im ν = 0). Then
### K(ν-ball) ⊂ K(ν_mid) + [ |ν − ν_mid| sup |∂_ν K| ] (the mean value inequality along the segment from ν_mid). θ = sign(t)(π/2 − 1/max(|t|, 1)).
### This tool measures, at s = 0.7 + i t for t ∈ {40.25, 140.25} and r ∈ {1e-12, 1e-6, 1e-3, 1e-2}: Arb's own ball radius for T3 and the radius
### by the bound, each against r·|Z'| (|Z'| by a difference quotient at the point); and the radii of T1, T2 and the prefactor on the ball.
### No banked zero is read. Usage: `python -X utf8 tools/b667_ball_probe.py` -> data/b667_ball_obstruction.txt. Written by the Write tool.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, acb, ctx   # noqa: E402
import b667_epstein_certify as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def dK_bound(x, nu_ball):
    """the bound above on sup |∂_ν K_ν(x)| over the ball nu_ball (an acb), x an arb."""
    t_lo = min(abs(float(nu_ball.imag.lower())), abs(float(nu_ball.imag.upper())))
    straddle = nu_ball.imag.contains(0)
    mu = max(abs(nu_ball.real.lower()).upper(), abs(nu_ball.real.upper()).upper(), key=lambda a: a.upper())
    th = arb(0) if straddle else arb.pi() / 2 - 1 / arb(max(t_lo, 1.0))
    a = x * th.cos()
    k0 = acb(a).bessel_k(acb(mu)).real
    k1 = acb(a).bessel_k(acb(mu + 1)).real
    return 2 * (-arb(t_lo) * th).exp() * (th * k0 + (-arb(1)).exp() * k1)


def t3_both(s, prec=200):
    """T3 on the ball s: (Arb's own ball, the ball by the bound)."""
    ctx.prec = prec
    half = arb(1) / 2
    pi, sq = arb.pi(), arb(23).sqrt()
    s_mid = acb(s.mid())
    nu, nu_mid = s - half, s_mid - half
    pre = 8 * acb(pi) ** s * s.rgamma()
    rnu = s.rad()
    M = C.M_of(C._tmax(s), prec)
    A, B = acb(0), acb(0)
    for m in range(1, M + 1):
        divs = [k for k in range(1, m + 1) if m % k == 0]
        dsum = sum((acb(k) ** nu * acb(sq * (m // k) / 2) ** (-nu) for k in divs), acb(0))
        ctx.prec = 600                                  # ### x formed at the Bessel call's own precision, both ways
        x = arb.pi() * arb(23).sqrt() * m
        ka = acb(x).bessel_k(nu)
        kb_mid = acb(x).bessel_k(nu_mid)
        e = (rnu * dK_bound(x, nu)).upper()
        ctx.prec = prec
        kb = kb_mid + acb(arb(0, e), arb(0, e))
        sg = 1 if m % 2 == 0 else -1
        A += sg * dsum * ka
        B += sg * dsum * kb
    return pre * A, pre * B


def zq_bound(s, prec=200):
    """Z_Q at a point by the route, T3's Bessel factors at 600 bits with x formed there (T4 omitted: below 1e-80 at these points)."""
    ctx.prec = prec
    half = arb(1) / 2
    T1 = 2 * (2 * s).zeta()
    T2 = 2 * arb.pi().sqrt() * (s - half).gamma() * s.rgamma() * acb(arb(23).sqrt() / 2) ** (1 - 2 * s) * (2 * s - 1).zeta()
    _a, tb = t3_both(s, prec)
    ctx.prec = prec
    return T1 + T2 + tb


def main():
    t0 = time.time()
    L = ['b667 -- THE SEGMENT ENCLOSURE`S SECOND OBSTRUCTION, MEASURED (%s): rows are (t, r) -- a ball of radius r about 0.7 + i t; Arb`s '
         'own radius for T3 on it, the radius by the explicit derivative bound, the radii of T1, T2 and the prefactor, each over r·|Z`|.'
         % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '']
    for t in ('40.25', '140.25'):
        ctx.prec = 200
        s = acb(arb(0.7), arb(float(t)))          # ### exact binary inputs: radius 0, so zq takes the point path at every m
        eps = arb(2) ** -100
        z0 = zq_bound(s)
        dz = abs((zq_bound(s + eps) - z0) / eps)
        L.append('  t %s : |Z_Q| %s ; |Z_Q`| %s (difference quotient at the point)' % (t, abs(z0.mid()).str(4, radius=False), dz.str(4, radius=False)))
        for r in ('1e-12', '1e-6', '1e-3', '1e-2'):
            ctx.prec = 200
            b = acb(arb('0.7', r), arb(t, r))
            ta, tb = t3_both(b)
            ctx.prec = 200
            half = arb(1) / 2
            T1 = 2 * (2 * b).zeta()
            T2 = 2 * arb.pi().sqrt() * (b - half).gamma() * b.rgamma() * acb(arb(23).sqrt() / 2) ** (1 - 2 * b) * (2 * b - 1).zeta()
            den = arb(r) * dz
            L.append('    r %-6s : T3 Arb`s ball %s ; T3 by the bound %s ; T1 %s ; T2 %s   (each rad / (r |Z`|))' % (
                r, (ta.rad() / den).str(3, radius=False), (tb.rad() / den).str(3, radius=False), (T1.rad() / den).str(3, radius=False),
                (T2.rad() / den).str(3, radius=False)))
    L += ['', '### ### **A RATIO NEAR ONE IS AN ENCLOSURE THE SEGMENT TEST CAN ACCEPT; ARB`S OWN T3 BALL IS NOT ONE. %.0f s.**' % (time.time() - t0)]
    p = os.path.join(D, 'b667_ball_obstruction.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    main()
