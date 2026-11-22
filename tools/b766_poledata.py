# -*- coding: utf-8 -*-
"""tools/b766_poledata.py -- (R376)(4)(d) L8, ITS DATA HALF: THE INTEGRAL OF THE WINDOW'S SPLINE AS THE CERTIFICATE'S intH. Written by the
Write tool and committed before its first run in any form; its form carried from tools/b766_window_data.py.

From data/b765_window.json, read and checked through tools/b766_window_data.py bank() (tools/b766_certificate.py window() and scaled(),
imported as committed; no bank of zeros imported), this tool writes SIDEExplicitFormula/Window/PoleData.lean in SIDE-explicit-formula:
  intHNum, the sum of the integer numerators coeffInt j, j from 16 to 16380, so that the integral of the spline H over y > 1, (1/16) times
  the sum of the c_j (Pole.lean integral_splineH), is intHNum / (16 * 10 ^ coeffScale).
The Lean (PoleSum.lean, by hand) proves the sum by the kernel's evaluation of the coefficient tree's halving sum (KFast.lean sumDC and aGet)
and its equality with the sum over j by sumDC_eq and aGet_eq; the file is data and its truth is the Lean's. No value is printed; the file
names no frequency (no decimal literal, no barred word: tools/b766_controls.py's Lean text check).

THE CONTROL: Coeffs.lean as it stands in the kernel read back (tools/b766_window_data.py read_back), its scale and its integers equal to
the bank's; intHNum the sum of those integers; intHNum / (16 * 10^E) equal exactly to data/b766_certificate.json's intH, the certificate's
window M 16 and its coef_sha the bank's; the halving sum of the Lean's check modelled (sumDC over aGet, the length 16,365 within 2^14) equal
to intHNum; the literal read back from the text equal to intHNum; the head's three digests the bank's; a planted literal, moved by one, read
as a difference against the certificate; no decimal literal and no barred word.

  python -X utf8 -u tools/b766_poledata.py dry      compose in memory, the control over the composed text, nothing written
  python -X utf8 -u tools/b766_poledata.py write    write the file, read it back from the disk, the control; data/b766_poledata.txt
  python -X utf8 -u tools/b766_poledata.py control  the control over the file on the disk, printed
"""
import hashlib
import io
import json
import os
import re
import sys
import time
from fractions import Fraction

T_ = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T_)
D_ = os.path.join(RELAY, 'data')
for p_ in (T_, os.path.join(T_, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b766_window_data as WD    # noqa: E402  (bank(), read_back(): the bank read and checked; its writes under its main guard)
import commit as CT              # noqa: E402  (KERNELS)

NL = '\n'
ACT = 'b766'
EF = 'SIDE-explicit-formula'
REL = 'SIDEExplicitFormula/Window/PoleData.lean'
COEFFS = 'SIDEExplicitFormula/Window/Coeffs.lean'
OUT = os.path.join(CT.KERNELS[EF], REL)
BANK = os.path.join(D_, 'b766_poledata.txt')
CERT = os.path.join(D_, 'b766_certificate.json')
J0, J1 = 16, 16380
M_WANT = 16
DEPTH = 14                 # ### the Lean's sumDC depth: 16,365 <= 2^14
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')
LIT = re.compile(r'^def intHNum : ℤ := (-?\d+)$', re.M)


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def sum_dc(f, lo, ln, d):
    """KFast.lean's sumDC, read as the kernel reads it."""
    if d == 0 or ln <= 1:
        return 0 if ln == 0 else f(lo)
    h = ln // 2
    return sum_dc(f, lo, h, d - 1) + sum_dc(f, lo + h, ln - h, d - 1)


def compose(n_int, dig):
    out = ['/-!',
           '# The integral of the window`s spline, as data',
           '',
           '`intHNum` is the sum of the integer numerators `coeffInt j`, `j` from %d to %d, of the window banked at relay' % (J0, J1),
           'data/b765_window.json, so that the integral of its spline over `y > 1` is `intHNum / (16 * 10 ^ coeffScale)`, the',
           'certificate`s intH (relay data/b766_certificate.json). Written by relay tools/b766_poledata.py under (R376)(4)(d); edited by no',
           'hand.',
           '',
           'The bank`s sha256, less its final line end: %s' % dig['text_sha'],
           'The bank`s sha256, the file whole: %s' % dig['file_sha'],
           'The coefficients` sha256, as the bank`s own field coef_sha: %s' % dig['coef_sha'],
           '-/', '',
           'namespace SIDEExplicitFormula',
           'namespace Window', '',
           '/-- The sum of the integer numerators of the window`s coefficients, `j` from %d to %d. -/' % (J0, J1),
           'def intHNum : ℤ := %d' % n_int, '',
           'end Window',
           'end SIDEExplicitFormula', '']
    return NL.join(out)


def facts():
    rats, ints, E, dig, RL = WD.bank()
    cpath = os.path.join(CT.KERNELS[EF], COEFFS)
    ctext = io.open(cpath, encoding='utf-8', newline='').read()
    E2, ints2, _d, _o, heads = WD.read_back(ctext)
    with io.open(CERT, encoding='utf-8') as f:
        cert = json.load(f)
    return dict(rats=rats, ints=ints, E=E, dig=dig, RL=RL, E2=E2, ints2=ints2, heads=heads, cert=cert)


def control(text, F):
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))
    ints, E, dig, cert = F['ints'], F['E'], F['dig'], F['cert']
    n_int = sum(ints)
    c('Coeffs.lean as it stands in the kernel read back: its scale and its integers against the bank`s (no value printed)',
      'scale 10^%s against 10^%d ; integers %d of %d equal ; its head`s digests the bank`s %s' % (
          F['E2'], E, sum(1 for x, y in zip(F['ints2'], ints) if x == y), len(ints), F['heads'] == (dig['text_sha'], dig['file_sha'], dig['coef_sha'])),
      F['E2'] == E and F['ints2'] == ints and len(ints) == J1 - J0 + 1 and F['heads'] == (dig['text_sha'], dig['file_sha'], dig['coef_sha']))
    w = cert.get('window', {})
    c('the certificate`s window: M and coef_sha', 'M %s ; coef_sha %s against the bank`s %s' % (w.get('M'), w.get('coef_sha'), dig['coef_sha']),
      w.get('M') == M_WANT and w.get('coef_sha') == dig['coef_sha'])
    eq = Fraction(n_int, M_WANT * 10 ** E) == Fraction(str(cert.get('intH')).strip())
    c('intHNum / (16 * 10^E) against data/b766_certificate.json`s intH, exactly', 'EQUAL' if eq else 'DIFFER', eq)

    def get(m):
        return ints[m - J0] if J0 <= m <= J1 else 0
    ln = J1 - J0 + 1
    dc = sum_dc(get, J0, ln, DEPTH)
    c('THE LEAN`S CHECK MODELLED: sumDC aGet %d %d %d against intHNum, the length within 2^%d' % (J0, ln, DEPTH, DEPTH),
      '%s ; %d <= %d %s' % ('EQUAL' if dc == n_int else 'DIFFER', ln, 2 ** DEPTH, ln <= 2 ** DEPTH), dc == n_int and ln <= 2 ** DEPTH)
    m = LIT.search(text)
    got = int(m.group(1)) if m else None
    c('the literal read back from the text, once, against intHNum', '%s ; lines matching %d' % (
        'EQUAL' if got == n_int else 'DIFFER', len(LIT.findall(text))), got == n_int and len(LIT.findall(text)) == 1)
    hs = (re.search(r'less its final line end: ([0-9a-f]{64})$', text, re.M), re.search(r'the file whole: ([0-9a-f]{64})$', text, re.M),
          re.search(r'own field coef_sha: ([0-9a-f]{16})$', text, re.M))
    hs = tuple(h.group(1) if h else None for h in hs)
    c('the head`s three digests against the bank`s', tuple((h or '')[:16] for h in hs), hs == (dig['text_sha'], dig['file_sha'], dig['coef_sha']))
    pl = LIT.sub('def intHNum : ℤ := %d' % (n_int + 1), text)
    pm = LIT.search(pl)
    pd = Fraction(int(pm.group(1)), M_WANT * 10 ** E) != Fraction(str(cert.get('intH')).strip()) if pm else False
    c('PLANTED: the literal moved by one, read as a difference against the certificate', 'DIFFER' if pd else 'NOT READ', pd)
    nd, nb = len(DECIMAL.findall(text)), len(BARRED.findall(text))
    c('no decimal literal and no barred word in the text (tools/b766_controls.py`s Lean text check)', 'decimal %d ; barred %d' % (nd, nb), nd == 0 and nb == 0)
    return L, ok


def main(cmd):
    F = facts()
    n_int = sum(F['ints'])
    text = compose(n_int, F['dig'])
    H = ['%s -- (R376)(4)(d) L8, ITS DATA HALF: THE INTEGRAL OF THE WINDOW`S SPLINE AS THE CERTIFICATE`S intH, SIDE-explicit-formula %s (%s, %s)' % (
        ACT, REL, cmd, _now()), ''] + F['RL'] + [
        '', '## THE FILE COMPOSED',
        '  intHNum the sum of %d integers over 10^%d ; its digits %d ; no value printed' % (len(F['ints']), F['E'], len(str(abs(n_int)))),
        '  lines %d ; bytes %d ; sha256 %s' % (len(text.split(NL)) - 1, len(text.encode('utf-8')), hashlib.sha256(text.encode('utf-8')).hexdigest()[:16])]
    if cmd == 'dry':
        L, ok = control(text, F)
        print(NL.join(H + ['', '## THE CONTROL OVER THE COMPOSED TEXT (nothing written)'] + L + [
            '', '### ### **THE CONTROL %d OF %d ; NOTHING WRITTEN.**' % (sum(ok), len(ok))]))
        return
    if cmd == 'write':
        if os.path.exists(OUT):
            sys.exit('### %s STANDS ALREADY -- nothing written (the file is written once; read it by `control`)' % REL)
        with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    if cmd not in ('write', 'control'):
        sys.exit(__doc__)
    if not os.path.exists(OUT):
        sys.exit('### %s ABSENT -- nothing read' % REL)
    disk = io.open(OUT, encoding='utf-8', newline='').read()
    L, ok = control(disk, F)
    eq = disk == text
    out = H + ['', '## THE FILE ON THE DISK, READ BACK',
               '  %s: bytes %d ; sha256 %s ; carriage returns %d ; equal to the composed text: %s' % (
                   REL, len(disk.encode('utf-8')), hashlib.sha256(disk.encode('utf-8')).hexdigest()[:16], disk.count('\r'), eq),
               '', '## THE CONTROL OVER THE FILE AS WRITTEN'] + L + [
        '', '### ### **THE DATA FILE %s ; THE CONTROL %d OF %d %s ; NO VALUE PRINTED.**' % (
            'WRITTEN AND READ BACK' if cmd == 'write' else 'READ', sum(ok), len(ok), 'AS WANTED' if all(ok) and eq else 'NOT AS WANTED')]
    print(NL.join(out))
    if cmd == 'write':
        s = NL.join(out) + NL
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(s)
        print('written data/%s' % os.path.basename(BANK))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '')
