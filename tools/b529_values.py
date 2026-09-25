# -*- coding: utf-8 -*-
"""b529_values.py -- COMPONENT 3`S NUMBER: THE NAMED HYPOTHESIS AT Q0`S B-SPLINE INSTANCE, a = 34. ### `python tools/b529_values.py`

### READING (7) of the sealed face. ### The instance is b522`s: `b521_tail.PWindow(34.0, 'q', 7)` -- the order-7 B-spline
### plateau, IMPORTED from the tool that generated `b522_cells.jsonl`, never copied -- at gamma_0 = 16.290216 (the window`s
### ordinate, b519`s `G0['q']`) and delta = beta - 1/2 of b514`s `PAIR`. ### Its `phihat` is normalized (`phihat(0) = 1`, so
### INT phi = 1) and even; the kernel`s `paperFT` of an even real phi agrees with it at every z (e^{izu} against e^{-izu}).
### ### PRINTED: the near factor N = phi^(i delta) = INT phi cosh(delta u); the far factor F = phi^(2 gamma_0 - i delta);
### eps_delta = |F| / N (the ferry`s hypothesis, `farSmall` at delta); eps_zero = |phi^(2 gamma_0)| / phi^(0) (`farSmall` at 0,
### which the slope needs); eps = the larger; the kernel`s `pairEps eps delta gamma_0` and c - eps` from their Lean definitions,
### transcribed; the right-hand side -(c - eps`) delta^2 |slope|^2 G^2 beside the instrument`s own pair term (b522`s banked
### `pair` counts the four images; the kernel`s `pairTwo` is two of them, half of it). ### G and the pair are cross-checked
### against b522`s bank at a = 34, row for row.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b521_tail as B21   # noqa: E402
import b519_window as B19  # noqa: E402

NL = chr(10)
A = 34.0
P = 7
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def pair_eps(eps, delta, g0):
    """### the kernel`s `pairEps`, transcribed: pairConst - (2 (1 - (2 eps + eps^2)) - delta^2 / (2 gamma_0^2) (1 + (2 eps + eps^2))) / (1 + eps)^2."""
    e1 = 2.0 * eps + eps * eps
    return 2.0 - (2.0 * (1.0 - e1) - delta * delta / (2.0 * g0 * g0) * (1.0 + e1)) / (1.0 + eps) ** 2


def main():
    W = B21.PWindow(A, 'q', P)
    g0, delta = float(W.g0), float(B19.DELTA)
    rho = B19.PAIR
    S = complex(W.phihat(0.0)).real
    N = complex(W.phihat(1j * delta)).real
    Nm = complex(W.phihat(-1j * delta)).real
    F = complex(W.phihat(2.0 * g0 - 1j * delta))
    F0 = complex(W.phihat(2.0 * g0))
    eps_d = abs(F) / N
    eps_0 = abs(F0) / S
    eps = max(eps_d, eps_0)
    G = N / S
    slope = W.slope()
    ep = pair_eps(eps, delta, g0)
    c = 2.0
    rhs = -(c - ep) * delta ** 2 * slope ** 2 * G ** 2
    # ### the kernel`s Component 1, near and far, evaluated on the instrument (two images) against the instrument`s khat
    w = delta ** 2 + 2j * g0 * delta
    two_formula = (w * (N + F) / 2.0) ** 2 + (np.conj(w) * (N + np.conj(F)) / 2.0) ** 2
    two_khat = complex(W.khat(g0 - 1j * delta)) + complex(W.khat(g0 + 1j * delta))
    near_pair = N ** 2 * delta ** 2 * (delta ** 2 - 4.0 * g0 ** 2) / 2.0
    bank = [json.loads(l) for l in io.open(os.path.join(D, 'b522_cells.jsonl'), encoding='utf-8')]
    row = [r for r in bank if r['a'] == A and r['p'] == P][0]
    out = dict(a=A, p=P, gamma0=g0, delta=delta, rho=[rho[0], rho[1]], S=S, N=N, N_minus=Nm, F=[F.real, F.imag], absF=abs(F),
               F0=[F0.real, F0.imag], absF0=abs(F0), eps_delta=eps_d, eps_zero=eps_0, eps=eps, below_0_1=bool(eps < 0.1),
               below_0_1_at_delta=bool(eps_d < 0.1), G=G, bank_growth=row['growth'], G_diff=abs(G - row['growth']),
               slope=slope, pairEps=ep, c=c, c_minus_eps=c - ep, pairEps_le_c=bool(ep <= c), rhs=rhs,
               pairTwo_formula=[two_formula.real, two_formula.imag], pairTwo_khat=[two_khat.real, two_khat.imag],
               formula_vs_khat=abs(two_formula - two_khat), bank_pair_four=row['pair'], bank_pair_half=row['pair'] / 2.0,
               near_pair=near_pair, bound_holds_on_instance=bool(two_khat.real <= rhs),
               note='the instance is the order-7 B-spline of b522 (C^5, even, >= 0, INT = 1); not a kernel object (W-ORD-BSPLINE-INSTANCE)')
    io.open(os.path.join(D, 'b529_values.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    print('### b529 -- THE NAMED HYPOTHESIS AT Q0`S B-SPLINE INSTANCE, a = %.0f, p = %d' % (A, P))
    print('  gamma_0 %.6f ; the pair`s zero %.5f + %.5f i ; delta %.5f' % (g0, rho[0], rho[1], delta))
    print('  S = phi^(0) %.15f ; N = phi^(i delta) %.10f ; phi^(-i delta) %.10f (even: equal)' % (S, N, Nm))
    print('  F = phi^(2 gamma_0 - i delta) = %.4e %+.4e i ; |F| %.4e' % (F.real, F.imag, abs(F)))
    print('  phi^(2 gamma_0) = %.4e %+.4e i ; |.| %.4e' % (F0.real, F0.imag, abs(F0)))
    print('  ### eps_delta = |F| / N = %.4e ; eps_zero = |phi^(2 gamma_0)| / S = %.4e ; eps = %.4e ; BELOW 0.1 : %s'
          % (eps_d, eps_0, eps, eps < 0.1))
    print('  G = N / S %.10f ; b522`s banked growth %.10f ; |diff| %.1e' % (G, row['growth'], abs(G - row['growth'])))
    print('  slope (the instrument`s, -2 gamma_0 C(gamma_0)) %.10f' % slope)
    print('  pairEps(eps, delta, gamma_0) = %.6f ; c = %.0f ; c - eps` = %.6f ; eps` <= c : %s' % (ep, c, c - ep, ep <= c))
    print('  ### the bound -(c - eps`) delta^2 slope^2 G^2 = %.4f' % rhs)
    print('  the pair`s term, two images: Component 1`s near/far formula %.10f %+.1e i ; the instrument`s khat %.10f %+.1e i ; |diff| %.1e'
          % (two_formula.real, two_formula.imag, two_khat.real, two_khat.imag, abs(two_formula - two_khat)))
    print('  b522`s banked pair (four images) %.10f ; half %.10f ; the near-factor product alone %.4f'
          % (row['pair'], row['pair'] / 2.0, near_pair))
    print('  ### the pair`s term <= the bound on this instance : %s' % (two_khat.real <= rhs))
    return 0


if __name__ == '__main__':
    sys.exit(main())
