# -*- coding: utf-8 -*-
"""b530_values.py -- COMPONENT 3`S NUMBERS: R AGAINST THE MEASURED REST AND THE PAIR, AT Q0`S B-SPLINE INSTANCE, a = 34.
### `python tools/b530_values.py`

### READING (7) of the sealed face. ### The instance is b522`s window, `b521_tail.PWindow(34.0, 'q', 7)`, IMPORTED (phi of
### integral 1, gamma_0 = 16.290216, L = log 34). ### R is the kernel`s `restR` TRANSCRIBED: 768 A0 A^2 e^L (gamma_0^2 + 1)^2
### SUM_m (1 + |m|)^{-3}, A = INT |g| + INT |g''''| (g = cos(gamma_0 u) phi(u), by trapezoid on a dense grid of [-L, L],
### g'''' from the instrument`s own `gcos_d`), SUM_m (1 + |m|)^{-3} = 2 zeta(3) - 1. ### A0 is NOT PROVED for Q0: it is
### the least A0 >= 1 with N(t, t + 1) <= A0 log(|t| + 3) on the bank (every zero below 150, both signs), read at t on a
### grid of step 0.01 with t + 1 <= 150. ### The measured rest: SUM |k^(gamma_rho)| over the banked zeros below 150
### outside the pair`s orbit (on-line 1/2 +- i gamma; each off-line zero`s four images), multiplicity one; the pair`s orbit
### term: the four images of b514`s PAIR. ### Also printed: G / e^{delta L}, e^{L} against e^{2 delta L}.
"""
import io
import json
import math
import os
import sys

import mpmath as mp
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b521_tail as B21     # noqa: E402
import b519_window as B19   # noqa: E402
import b514_window as B14   # noqa: E402
import b511_families as F   # noqa: E402

NL = chr(10)
A = 34.0
P = 7
TOP = 150.0
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def zeros():
    """### every banked zero of Q0 below 150, as complex numbers, both signs of the ordinate."""
    out = []
    for g in F.GQ:
        if g < TOP:
            out += [complex(0.5, g), complex(0.5, -g)]
    for b, gg in F.OFFQ:
        if abs(gg) < TOP:
            out += list(B14.images(b, gg))
    return out


def main():
    W = B21.PWindow(A, 'q', P)
    g0, L, delta = float(W.g0), float(W.L), float(B19.DELTA)
    u = np.linspace(-L, L, 400001)
    a0 = float(np.trapezoid(np.abs(W.gcos_d(u, 0)), u))
    a4 = float(np.trapezoid(np.abs(W.gcos_d(u, 4)), u))
    Aw = a0 + a4
    Z = zeros()
    ims = np.array(sorted(z.imag for z in Z))
    ts = np.arange(-TOP, TOP - 1.0, 0.01)
    cnt = np.searchsorted(ims, ts + 1.0, side='right') - np.searchsorted(ims, ts, side='right')
    A0 = max(1.0, float(np.max(cnt / np.log(np.abs(ts) + 3.0))))
    z3 = float(2 * mp.zeta(3) - 1)
    R = 768.0 * A0 * Aw ** 2 * math.exp(L) * (g0 ** 2 + 1.0) ** 2 * z3
    pair = B14.images(*B19.PAIR)
    orbit = [complex(r) for r in pair]
    near = lambda r: min(abs(r - o) for o in orbit) < 1e-9
    rest_terms = [abs(complex(W.khat(B14.gamma_of(r)))) for r in Z if not near(r)]
    pair_terms = [complex(W.khat(B14.gamma_of(r))) for r in orbit]
    rest = float(sum(rest_terms))
    pair_abs = float(sum(abs(t) for t in pair_terms))
    pair_signed = float(sum(t.real for t in pair_terms))
    G = float(W.phihat(1j * delta).real)
    out = dict(a=A, p=P, gamma0=g0, L=L, delta=delta, int_abs_g=a0, int_abs_g4=a4, windowA=Aw, zeros_banked=len(Z),
               A0_measured=A0, zeta3Sum=z3, R=R, rest_measured=rest, rest_terms=len(rest_terms),
               pair_orbit_abs=pair_abs, pair_orbit_signed=pair_signed, ratio_R_rest=R / rest, ratio_R_pair=R / pair_abs,
               exceeds_100=bool(R > 100.0 * rest), G=G, G_over_exp=G / math.exp(delta * L),
               exp_L=math.exp(L), exp_2dL=math.exp(2.0 * delta * L), two_delta=2.0 * delta,
               note='A0 measured on the bank below 150, not proved for Q0; the rest is the bank below 150 (b522`s tail above 150 at most 4.2e-8)')
    io.open(os.path.join(D, 'b530_values.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    print('### b530 -- R AGAINST THE MEASURED REST, Q0`s B-spline instance, a = %.0f, p = %d' % (A, P))
    print('  gamma_0 %.6f ; L %.6f ; delta %.5f' % (g0, L, delta))
    print('  INT |g| %.6e ; INT |g````| %.6e ; A = %.6e' % (a0, a4, Aw))
    print('  zeros banked below 150 (both signs, images) %d ; A0 measured %.4f (NOT PROVED for Q0)' % (len(Z), A0))
    print('  SUM_m (1 + |m|)^-3 = 2 zeta(3) - 1 = %.6f' % z3)
    print('  ### R = 768 A0 A^2 e^L (gamma_0^2 + 1)^2 SUM = %.4e' % R)
    print('  the measured rest (%d terms, outside the pair`s orbit) %.6f ; the pair`s orbit |.| %.6f (signed %.6f)'
          % (len(rest_terms), rest, pair_abs, pair_signed))
    print('  ### R / rest = %.4e ; R / pair = %.4e ; R > 100 x rest : %s' % (R / rest, R / pair_abs, R > 100.0 * rest))
    print('  G = %.6f ; e^{delta L} = %.6f ; G / e^{delta L} = %.4f' % (G, math.exp(delta * L), G / math.exp(delta * L)))
    print('  e^L = %.4f against e^{2 delta L} = %.4f ; 2 delta = %.5f < 1' % (math.exp(L), math.exp(2 * delta * L), 2 * delta))
    return 0


if __name__ == '__main__':
    sys.exit(main())
