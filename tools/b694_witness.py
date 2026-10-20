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


def env(*a):
    """the instrument's libraries, by version; no term computed."""
    import flint
    import mpmath
    print('  python %s ; python-flint %s ; mpmath %s ; acb.integral %s ; acb.digamma %s' % (
        sys.version.split()[0], flint.__version__, mpmath.__version__, hasattr(flint.acb, 'integral'), hasattr(flint.acb, 'digamma')))
    return 0


if __name__ == '__main__':
    fn = {'zeros': zeros, 'env': env}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_witness.py zeros | env')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]))
