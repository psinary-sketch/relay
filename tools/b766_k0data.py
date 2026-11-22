# -*- coding: utf-8 -*-
"""tools/b766_k0data.py -- (R376)(4)(d) L9, ITS FIRST DATUM: THE WINDOW'S AUTOCORRELATION AT 0, k(0), AS THE CERTIFICATE'S k0. Written by
the Write tool and committed before its first run in any form; its form carried from tools/b766_poledata.py (its import line among it,
defect (k)).

From data/b765_window.json, read and checked through tools/b766_kdata.py bank() (tools/b766_certificate.py window() and scaled(), imported
as committed; no bank of zeros imported), this tool writes SIDEExplicitFormula/Window/ArchData.lean in SIDE-explicit-formula:
  k0Num, Kt(1): the strided sum of KFast.lean at n = 1, so that k(0) = windowK 0 = k0Num / (80640 * 10^34) by KFast.lean's
  windowK_log_eq_Kt at n = 1.
The Lean (Arch.lean, by hand) proves KtFast 1 = k0Num by the kernel's evaluation, and windowK 0 from it; the file is data and its truth is
the Lean's. No value is printed; the file names no frequency (no decimal literal, no barred word: tools/b766_controls.py's Lean text check).

THE CONTROL: Kt(1) by the F table's strided sum (tools/b766_kdata.py kt_fast, the form KtFast reads) equal to the direct double sum over
the coefficients (kt_direct); Kt(1) / (80640 * 10^34) equal exactly to data/b766_certificate.json's k0; the halving's length at n = 1,
16,365, within 2^14; the literal read back from the text, once, equal to Kt(1); the head's three digests the bank's; a planted literal,
moved by one, read as a difference against the certificate; no decimal literal and no barred word; the file opening with its import.

  python -X utf8 -u tools/b766_k0data.py dry      compose in memory, the control over the composed text, nothing written
  python -X utf8 -u tools/b766_k0data.py write    write the file, read it back from the disk, the control; data/b766_k0data.txt
  python -X utf8 -u tools/b766_k0data.py control  the control over the file on the disk, printed
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
import b766_kdata as KD          # noqa: E402  (bank(), ftable(), kt_fast(), kt_direct(), mtop(); its writes under its main guard)
import commit as CT              # noqa: E402  (KERNELS)

NL = '\n'
ACT = 'b766'
EF = 'SIDE-explicit-formula'
REL = 'SIDEExplicitFormula/Window/ArchData.lean'
OUT = os.path.join(CT.KERNELS[EF], REL)
BANK = os.path.join(D_, 'b766_k0data.txt')
CERT = os.path.join(D_, 'b766_certificate.json')
J0 = 16
DEN = 80640 * 10 ** 34     # ### windowK_log_eq_Kt at n = 1: 80640 n^4 10^34
DEPTH = 14
IMPORT = 'import Mathlib.Data.Real.Basic'
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')
LIT = re.compile(r'^def k0Num : ℤ := (-?\d+)$', re.M)


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def compose(n_int, dig):
    out = [IMPORT, '',
           '/-!',
           '# The window`s autocorrelation at 0, as data',
           '',
           '`k0Num` is the strided sum `Kt 1` of KFast.lean for the window banked at relay data/b765_window.json, so that the',
           'autocorrelation at 0 is `k0Num / (80640 * 10 ^ 34)`, the certificate`s k0 (relay data/b766_certificate.json). Written by relay',
           'tools/b766_k0data.py under (R376)(4)(d); edited by no hand.',
           '',
           'The bank`s sha256, less its final line end: %s' % dig['text_sha'],
           'The bank`s sha256, the file whole: %s' % dig['file_sha'],
           'The coefficients` sha256, as the bank`s own field coef_sha: %s' % dig['coef_sha'],
           '-/', '',
           'namespace SIDEExplicitFormula',
           'namespace Window', '',
           '/-- The strided sum of the window`s autocorrelation at `n = 1`. -/',
           'def k0Num : ℤ := %d' % n_int, '',
           'end Window',
           'end SIDEExplicitFormula', '']
    return NL.join(out)


def facts():
    a, dig, _csha, _K, _ksha, _clist, RL = KD.bank()
    F = KD.ftable(a)
    with io.open(CERT, encoding='utf-8') as f:
        cert = json.load(f)
    return dict(a=a, dig=dig, RL=RL, kt1=KD.kt_fast(a, F, 1), kd1=KD.kt_direct(a, 1), cert=cert)


def control(text, F):
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))
    kt1, dig, cert = F['kt1'], F['dig'], F['cert']
    c('Kt(1) by the F table`s strided sum (the form KtFast reads) against the direct double sum over the coefficients',
      'EQUAL' if kt1 == F['kd1'] else 'DIFFER', kt1 == F['kd1'])
    w = cert.get('window', {})
    c('the certificate`s window: coef_sha', 'coef_sha %s against the bank`s %s' % (w.get('coef_sha'), dig['coef_sha']), w.get('coef_sha') == dig['coef_sha'])
    eq = Fraction(kt1, DEN) == Fraction(str(cert.get('k0')).strip())
    c('Kt(1) / (80640 * 10^34) against data/b766_certificate.json`s k0, exactly', 'EQUAL' if eq else 'DIFFER', eq)
    ln = KD.mtop(1) + 1 - J0
    c('THE LEAN`S HALVING AT n = 1: its length mtop 1 + 1 - 16 within 2^%d' % DEPTH, '%d <= %d' % (ln, 2 ** DEPTH), ln <= 2 ** DEPTH)
    m = LIT.search(text)
    got = int(m.group(1)) if m else None
    c('the literal read back from the text, once, against Kt(1)', '%s ; lines matching %d' % (
        'EQUAL' if got == kt1 else 'DIFFER', len(LIT.findall(text))), got == kt1 and len(LIT.findall(text)) == 1)
    hs = (re.search(r'less its final line end: ([0-9a-f]{64})$', text, re.M), re.search(r'the file whole: ([0-9a-f]{64})$', text, re.M),
          re.search(r'own field coef_sha: ([0-9a-f]{16})$', text, re.M))
    hs = tuple(h.group(1) if h else None for h in hs)
    c('the head`s three digests against the bank`s', tuple((h or '')[:16] for h in hs), hs == (dig['text_sha'], dig['file_sha'], dig['coef_sha']))
    pl = LIT.sub('def k0Num : ℤ := %d' % (kt1 + 1), text)
    pm = LIT.search(pl)
    pd = Fraction(int(pm.group(1)), DEN) != Fraction(str(cert.get('k0')).strip()) if pm else False
    c('PLANTED: the literal moved by one, read as a difference against the certificate', 'DIFFER' if pd else 'NOT READ', pd)
    nd, nb = len(DECIMAL.findall(text)), len(BARRED.findall(text))
    c('no decimal literal and no barred word in the text (tools/b766_controls.py`s Lean text check)', 'decimal %d ; barred %d' % (nd, nb), nd == 0 and nb == 0)
    first = text.split(NL)[0]
    c('the file opens with its import, so that the integers` notation resolves (defect (k))', first, first == IMPORT)
    return L, ok


def main(cmd):
    F = facts()
    text = compose(F['kt1'], F['dig'])
    H = ['%s -- (R376)(4)(d) L9, ITS FIRST DATUM: THE WINDOW`S AUTOCORRELATION AT 0 AS THE CERTIFICATE`S k0, SIDE-explicit-formula %s (%s, %s)' % (
        ACT, REL, cmd, _now()), ''] + F['RL'] + [
        '', '## THE FILE COMPOSED',
        '  k0Num = Kt(1), the strided sum at n = 1 over %d places ; its digits %d ; no value printed' % (KD.mtop(1) + 1 - J0, len(str(abs(F['kt1'])))),
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
