# -*- coding: utf-8 -*-
"""tools/b766_window_data.py -- (R376)(4)(c): THE WINDOW'S COEFFICIENTS ENTER THE KERNEL AS DATA. Written by the Write tool and committed
before its first run in any form.

From data/b765_window.json, read and checked by tools/b766_certificate.py window() (its sha256 less its final line end against
data/b765_window.txt :26, each (m, e) against its rational, the coefficients' sha256 against the bank's coef_sha), this tool writes
SIDEExplicitFormula/Window/Coeffs.lean in SIDE-explicit-formula: the 16,365 coefficients c_j, j from 16 to 16380, each held exactly as an
integer C_j over 10^E (tools/b766_certificate.py scaled(), carried from tools/b765_window.py unedited), in chunks of 256, its head naming
the bank's sha256 in both forms and the coefficients' sha256. No coefficient is printed; the window's frequency is read nowhere and the
file names none (no decimal literal, no barred word: tools/b766_controls.py's Lean text check).

THE CONTROL ((R376)(4)(c)): the coefficients read back from the file as written, each C_j / 10^E against the bank's rational, equal at
16,365 of 16,365; the head's three digests against the bank's; the chunks named in order in the list's line; and a planted digit, one
integer of the text moved in its last digit, read as one difference at its j (the j printed, no value).

  python -X utf8 -u tools/b766_window_data.py dry      compose in memory, the control over the composed text, nothing written
  python -X utf8 -u tools/b766_window_data.py write    write the file, read it back from the disk, the control; data/b766_window_data.txt
  python -X utf8 -u tools/b766_window_data.py control  the control over the file on the disk, printed
"""
import hashlib
import io
import os
import re
import sys
import time
from fractions import Fraction

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b766_certificate as C     # noqa: E402  (window(), scaled(): the bank read and checked; no bank of zeros imported)
import commit as CT              # noqa: E402  (KERNELS)

NL = '\n'
ACT = 'b766'
EF = 'SIDE-explicit-formula'
REL = 'SIDEExplicitFormula/Window/Coeffs.lean'
OUT = os.path.join(CT.KERNELS[EF], REL)
BANK = os.path.join(D, 'b766_window_data.txt')
J0, J1 = 16, 16380
CHUNK = 256
PLANT_INDEX = 8000         # ### the planted digit's index in the list (j = 8016)
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def bank():
    """(the coefficients as (j, Fraction) in the order of j, the integers C_j, E, the digests, the reader's lines)."""
    js, cm, L, dig = C.window()
    js_ = sorted(cm)
    if js_ != list(range(J0, J1 + 1)):
        sys.exit('### THE COEFFICIENTS` j ARE NOT 16 TO 16380 IN ORDER -- NOTHING DONE')
    rats = [(int(j), Fraction(str(r).strip())) for j, _me, r in js['coefficients']]
    if [j for j, _q in rats] != list(range(J0, J1 + 1)):
        sys.exit('### THE BANK`S COEFFICIENTS NOT IN THE ORDER OF j -- NOTHING DONE')
    Cs, S = C.scaled(cm, js['M'], J1)
    E = len(str(S)) - 1
    if 10 ** E != S:
        sys.exit('### THE SCALE IS NOT A POWER OF TEN -- NOTHING DONE')
    ints = [Cs[j] for j in range(J0, J1 + 1)]
    return rats, ints, E, dig, L


def compose(ints, E, dig):
    n = len(ints)
    chunks = [ints[i:i + CHUNK] for i in range(0, n, CHUNK)]
    names = ['coeffChunk%02d' % k for k in range(len(chunks))]
    out = ['import Mathlib.Data.Real.Basic', '',
           '/-!',
           '# The window`s coefficients, as data',
           '',
           'The %d coefficients `c_j`, `j` from %d to %d, of the window banked at relay data/b765_window.json, each held exactly as an' % (n, J0, J1),
           'integer over `10 ^ coeffScale`. Written by relay tools/b766_window_data.py from that bank under (R376)(4)(c); edited by no hand.',
           '',
           'The bank`s sha256, less its final line end: %s' % dig['text_sha'],
           '(relay data/b765_window.txt :26 gives its first sixteen).',
           'The bank`s sha256, the file whole: %s' % dig['file_sha'],
           'The coefficients` sha256, as the bank`s own field coef_sha: %s' % dig['coef_sha'],
           '-/', '',
           'namespace SIDEExplicitFormula',
           'namespace Window', '',
           '/-- The power of ten under every coefficient. -/',
           'def coeffScale : ℕ := %d' % E, '']
    for k, (nm, ch) in enumerate(zip(names, chunks)):
        a = J0 + k * CHUNK
        out.append('/-- The integer numerators for `j` from %d to %d. -/' % (a, a + len(ch) - 1))
        out.append('def %s : List ℤ := [' % nm)
        rows = [ch[i:i + 16] for i in range(0, len(ch), 16)]
        for i, r in enumerate(rows):
            out.append('  ' + ', '.join(str(x) for x in r) + (',' if i < len(rows) - 1 else ''))
        out.append(']')
        out.append('')
    out.append('/-- The %d integer numerators in the order of `j`, from %d to %d. -/' % (n, J0, J1))
    out.append('def coeffList : List ℤ :=')
    for i in range(0, len(names), 8):
        out.append('  ' + ' ++ '.join(names[i:i + 8]) + (' ++' if i + 8 < len(names) else ''))
    out += ['',
            '/-- The integer numerator of `c_j`; `0` outside `%d ≤ j ≤ %d`. -/' % (J0, J1),
            'def coeffInt (j : ℕ) : ℤ := if %d ≤ j ∧ j ≤ %d then coeffList.getD (j - %d) 0 else 0' % (J0, J1, J0), '',
            '/-- The window`s coefficient `c_j = coeffInt j / 10 ^ coeffScale`. -/',
            'noncomputable def coeff (j : ℕ) : ℝ := (coeffInt j : ℝ) / 10 ^ coeffScale', '',
            'end Window',
            'end SIDEExplicitFormula', '']
    return NL.join(out), names


def read_back(text):
    """(E, the integers in order, the chunk names in the list's line, the head's three digests) read from a file's text."""
    m = re.search(r'^def coeffScale : ℕ := (\d+)$', text, re.M)
    E = int(m.group(1)) if m else None
    chunks = re.findall(r'^def (coeffChunk\d+) : List ℤ := \[\n(.*?)\n\]$', text, re.M | re.S)
    ints = []
    for _nm, body in chunks:
        ints += [int(x) for x in re.findall(r'-?\d+', body)]
    lst = re.search(r'^def coeffList : List ℤ :=\n((?:  .*\n)+)', text, re.M)
    order = re.findall(r'coeffChunk\d+', lst.group(1)) if lst else []
    heads = (re.search(r'less its final line end: ([0-9a-f]{64})$', text, re.M), re.search(r'the file whole: ([0-9a-f]{64})$', text, re.M),
             re.search(r'own field coef_sha: ([0-9a-f]{16})$', text, re.M))
    return E, ints, [nm for nm, _b in chunks], order, tuple(h.group(1) if h else None for h in heads)


def differences(text, rats):
    E, ints, defined, order, _h = read_back(text)
    if E is None or len(ints) != len(rats):
        return None
    S = 10 ** E
    return [j for (j, q), x in zip(rats, ints) if Fraction(x, S) != q]


def plant(text):
    """the text with the PLANT_INDEX-th integer of the chunks moved in its last digit."""
    starts = [mm.end() for mm in re.finditer(r'^def coeffChunk\d+ : List ℤ := \[\n', text, re.M)]
    pos = []
    for s in starts:
        e = text.index('\n]', s)
        pos += [(s + mm.start(), s + mm.end()) for mm in re.finditer(r'-?\d+', text[s:e])]
    a, b = pos[PLANT_INDEX]
    d = text[b - 1]
    return text[:b - 1] + str((int(d) + 1) % 10) + text[b:]


def control(text, rats, ints, E, dig):
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))
    E2, ints2, defined, order, heads = read_back(text)
    df = differences(text, rats)
    c('the coefficients read back from the text, each C_j / 10^E against the bank`s rational (no value printed)',
      'read %d of %d, the scale 10^%s, differences %s' % (len(ints2), len(rats), E2, 'NONE' if df == [] else (len(df) if df else df)),
      E2 == E and len(ints2) == len(rats) == J1 - J0 + 1 and df == [])
    c('the integers read back equal to those composed', sum(1 for x, y in zip(ints2, ints) if x == y), ints2 == ints)
    c('the head`s three digests against the bank`s (less its final line end, the file whole, coef_sha)',
      tuple((h or '')[:16] for h in heads), heads == (dig['text_sha'], dig['file_sha'], dig['coef_sha']))
    c('the chunks defined, and named in the list`s line in order', '%d defined, %d named' % (len(defined), len(order)),
      defined == order == ['coeffChunk%02d' % k for k in range(len(defined))] and len(defined) == -(-(J1 - J0 + 1) // CHUNK))
    pd = differences(plant(text), rats)
    c('PLANTED: one integer of the text moved in its last digit, read as one difference at its j', pd, pd == [J0 + PLANT_INDEX])
    nd, nb = len(DECIMAL.findall(text)), len(BARRED.findall(text))
    c('no decimal literal and no barred word in the text (tools/b766_controls.py`s Lean text check)', 'decimal %d ; barred %d' % (nd, nb), nd == 0 and nb == 0)
    return L, ok


def main(cmd):
    rats, ints, E, dig, RL = bank()
    text, names = compose(ints, E, dig)
    H = ['%s -- (R376)(4)(c): THE WINDOW`S COEFFICIENTS ENTER THE KERNEL AS DATA, SIDE-explicit-formula %s (%s, %s)' % (ACT, REL, cmd, _now()), ''] + RL + [
        '', '## THE FILE COMPOSED',
        '  coefficients %d, j from %d to %d ; each an integer over 10^%d ; the largest integer %d digits ; zeros %d ; chunks %d of %d' % (
            len(ints), J0, J1, E, max(len(str(abs(x))) for x in ints), sum(1 for x in ints if x == 0), len(names), CHUNK),
        '  lines %d ; bytes %d ; sha256 %s' % (len(text.split(NL)) - 1, len(text.encode('utf-8')), hashlib.sha256(text.encode('utf-8')).hexdigest()[:16])]
    if cmd == 'dry':
        L, ok = control(text, rats, ints, E, dig)
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
    L, ok = control(disk, rats, ints, E, dig)
    eq = disk == text
    out = H + ['', '## THE FILE ON THE DISK, READ BACK',
               '  %s: bytes %d ; sha256 %s ; carriage returns %d ; equal to the composed text: %s' % (
                   REL, len(disk.encode('utf-8')), hashlib.sha256(disk.encode('utf-8')).hexdigest()[:16], disk.count('\r'), eq),
               '', '## THE CONTROL OVER THE FILE AS WRITTEN'] + L + [
        '', '### ### **THE DATA FILE %s ; THE CONTROL %d OF %d %s ; NO COEFFICIENT PRINTED.**' % (
            'WRITTEN AND READ BACK' if cmd == 'write' else 'READ', sum(ok), len(ok), 'AS WANTED' if all(ok) and eq else 'NOT AS WANTED')]
    print(NL.join(out))
    if cmd == 'write':
        s = NL.join(out) + NL
        with io.open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write(s)
        print('written data/%s' % os.path.basename(BANK))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '')
