# -*- coding: utf-8 -*-
"""b694_witness.py -- THE WEIL-FACE WITNESS AT Q0, (R304)(4). ### `python tools/b694_witness.py zeros`
### Stage one (step zero): the `zeros` route alone -- b681's narrowed balls read (the gz's sha256 checked against its text hashes bank
### first), the off-line rows (kind OFF) banked as text, rows are zeros as balls. No term of the explicit formula is computed by this stage.
### Written by the Write tool at b694; this tool writes only the banks it names.
"""
import gzip
import hashlib
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
GZ = 'b681_epstein_zeros_narrowed.json.gz'
GZ_SHA = 'f6613564e9d7fcd534534d0c33e418229bf32dbc0567c951ee8750438b11eb5a'      # ### data/b681_epstein_zeros_narrowed_hashes.txt :3
JS_SHA = 'c3b54356a1144ee50618fb714900dd4f982fd25a546a94f3100a176371269ce8'      # ### :2
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _put(name, data):
    q = os.path.join(D, name)
    with open(q + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(q + '.tmp', q)


def balls():
    """b681's rows, the gz and its json checked against the hashes bank before any row is read."""
    gzb = open(os.path.join(D, GZ), 'rb').read()
    js = gzip.decompress(gzb)
    if hashlib.sha256(gzb).hexdigest() != GZ_SHA or hashlib.sha256(js).hexdigest() != JS_SHA:
        sys.exit('### b681`s gz or json differs from its hashes bank -- NOTHING READ')
    return json.loads(js.decode('utf-8'))


def zeros(*a):
    B = balls()
    off = [r for r in B['rows'] if r['kind'] == 'OFF']
    L = ['b694 -- THE OFF-LINE ZEROS OF Z_Q FROM b681`S NARROWED BALLS, READ AT STEP ZERO (%s)' % utc(), '',
         '### source: relay data/%s, gz sha256 %s and json sha256 %s EQUAL to data/b681_epstein_zeros_narrowed_hashes.txt :2-:3; the bank`s w %s,'
         ' prec %s. rows are zeros as balls: index | the reading | sigma (the centre) | t (the centre) | the half-width h of the square'
         ' | beta - 1/2 with the half-width beside it.' % (GZ, GZ_SHA, JS_SHA, B.get('w'), B.get('prec')), '']
    for r in off:
        L.append('  OFF %-3d | %-9s | sigma %s | t %s | h %s | beta - 1/2 = %s +- %s' % (
            int(r['idx']), r['reading'], r['re'], r['im'], r['h'], _minus_half(r['re']), r['h']))
    L += ['', '### ### **OFF-LINE ROWS %d ; EVERY ONE NARROWED %s ; THE BANK READ AFTER ITS HASHES.**' % (
        len(off), all(r['reading'] == 'NARROWED' for r in off))]
    _put('b694_witness_zeros.txt', (NL.join(L) + NL).encode('utf-8'))
    print(L[-1])
    return 0


def _minus_half(s):
    """sigma - 1/2 as a decimal string, exactly (the centre is a decimal string)."""
    from decimal import Decimal, getcontext
    getcontext().prec = 80
    return str(Decimal(s) - Decimal('0.5'))


G0 = '16.29021572039039079296317264519149437546'     # ### OFF 0's centre to 40 digits (data/b694_witness_zeros.txt :5)
DELTA0 = '0.4532604747946606862505090135672800242901'
LADDER = (16, 24, 32, 48, 64, 96, 128, 192)


def hhat_notched(z, L, g0):
    """b518's window in the kernel's transform: (g0^2 - z^2) (sinc((z - g0) L/6)^6 + sinc((z + g0) L/6)^6) / 2."""
    import mpmath as M
    s = lambda w: M.sinc(w) if w != 0 else M.mpf(1)   # noqa: E731
    return (g0 ** 2 - z ** 2) * (s((z - g0) * L / 6) ** 6 + s((z + g0) * L / 6) ** 6) / 2


def concentration(*a):
    """the author's answer 4 (data/b694_author_answers.txt): the row that sets the window's concentration at gamma_0, printed with its value
    before any term -- h^ on the line near gamma_0 (its value at gamma_0, its two flanking maxima), and h^ at the off-line point gamma_0 - i delta
    beside it. A property of the window; no P, PR or A computed."""
    import mpmath as M
    M.mp.dps = 30
    g0, dl = M.mpf(G0), M.mpf(DELTA0)
    L = ['b694 -- THE WINDOW`S CONCENTRATION AT gamma_0, PRINTED BEFORE ANY TERM ON THE AUTHOR`S ANSWER 4 (%s)' % utc(), '',
         '### the plan`s row (data/b694_witness_plan.txt (2)): h_a(u) = (gamma_0^2 + D^2)[cos(gamma_0 u) phi_a(u)]; THE CENTRE PARAMETER gamma_0 = %s,'
         ' the cosine`s frequency, placing the envelope phi_a^(z -+ gamma_0) at z = +-gamma_0; THE NOTCH FACTOR (gamma_0^2 - z^2), zero at z = gamma_0.'
         % G0, '### rows are widths: a | h^(gamma_0) on the line | the flanking maxima of |h^| on the line (position, value) | |h^(gamma_0 - i delta)|'
         ' at OFF 0 | arg of h^(gamma_0 - i delta)^2 in degrees (180 = a negative pair term). mpmath at 30 digits; no term of the formula.', '']
    for a_ in (14.106736,) + LADDER:
        Lw = M.log(a_)
        at0 = hhat_notched(g0, Lw, g0)
        f = lambda r: -abs(hhat_notched(r, Lw, g0))   # noqa: E731
        lo = M.findroot(lambda r: M.diff(lambda x: hhat_notched(x, Lw, g0), r), g0 - 2 / Lw)
        hi = M.findroot(lambda r: M.diff(lambda x: hhat_notched(x, Lw, g0), r), g0 + 2 / Lw)
        off = hhat_notched(M.mpc(g0, -dl), Lw, g0)
        z = M.mpc(g0, -dl)
        un = lambda w: (M.sinc((w - g0) * Lw / 6) ** 6 + M.sinc((w + g0) * Lw / 6) ** 6) / 2   # noqa: E731  ### the un-notched centring
        L.append('  a %-10s | h^(gamma_0) %s | maxima at %s (%s) and %s (%s) | |h^(gamma_0 - i delta)| %s | arg h^^2 %s | UN-NOTCHED: '
                 'h^(gamma_0) %s, arg h^(gamma_0 - i delta)^2 %s' % (
                     a_, M.nstr(at0, 3), M.nstr(lo, 8), M.nstr(-f(lo), 6), M.nstr(hi, 8), M.nstr(-f(hi), 6), M.nstr(abs(off), 6),
                     M.nstr(M.degrees(M.arg(off ** 2)), 6), M.nstr(M.re(un(g0)), 6), M.nstr(M.degrees(M.arg(un(z) ** 2)), 6)))
    L += ['', '### ### **THE CENTRE PARAMETER gamma_0 = %s PLACES THE ENVELOPE AT gamma_0 ; h^ ON THE LINE IS ZERO AT gamma_0 (THE NOTCH), ITS PEAKS'
          ' FLANKING IT ; h^ IS NOT PEAKED AT gamma_0 ON THE LINE.**' % G0[:12]]
    _put('b694_witness_concentration.txt', (NL.join(L) + NL).encode('utf-8'))
    print(NL.join(L[5:]))
    return 0


def env(*a):
    """the instrument's libraries, by version; no term computed."""
    import flint
    import mpmath
    print('  python %s ; python-flint %s ; mpmath %s ; acb.integral %s ; acb.digamma %s' % (
        sys.version.split()[0], flint.__version__, mpmath.__version__, hasattr(flint.acb, 'integral'), hasattr(flint.acb, 'digamma')))
    print('  acb: sinc %s, zeta_zero %s, zeta_zeros %s ; acb_poly: derivative %s, integral %s, __call__ %s ; arb: log %s, sqrt %s' % tuple(
        hasattr(o, m) for o, m in ((flint.acb, 'sinc'), (flint.acb, 'zeta_zero'), (flint.acb, 'zeta_zeros'), (flint.acb_poly, 'derivative'),
                                   (flint.acb_poly, 'integral'), (flint.acb_poly, '__call__'), (flint.arb, 'log'), (flint.arb, 'sqrt'))))
    return 0


if __name__ == '__main__':
    fn = {'zeros': zeros, 'env': env, 'concentration': concentration}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_witness.py zeros | env')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]))
