# -*- coding: utf-8 -*-
"""b333_source.py -- THE CLASSICAL SOURCE, PINNED BY HASH BEFORE A WORD IS READ. ### b305's PIN, IMPORTED.

### ### **THE SOURCE:** ### Connes-Consani, *Weil positivity and trace formula, the archimedean place*,
### arXiv:2006.13771v1 -- whose Appendix B *"gather[s] different sources on the normalization of the
### archimedean contribution to the explicit formula"*, following its reference [7], and states the
### archimedean distribution three ways: (150) as a principal value on the real side, (151) through the
### logarithmic derivative of the Gamma factor against the Mellin transform, (152)-(153) through the
### digamma kernel `h_+`. ### The pin is b304/b305's (`sha256 b8e0b54a...`, 1213504 bytes); this act
### RE-VERIFIES it on a local copy before reading, and pins the text layer it reads (`b328_source_text.txt`)
### by its own sha256, so the extract step's file is itself a pinned artefact.
"""
import glob
import hashlib
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5  # noqa: E402

D = os.path.join(ROOT, 'data')
PIN = 'b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0'
PIN_BYTES = 1213504
TEXT = os.path.join(D, 'b328_source_text.txt')
OUT = os.path.join(D, 'b333_source.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    L = []
    rec = L.append
    rec('=' * 100)
    rec('b333_source.py -- THE CLASSICAL SOURCE, PINNED BY HASH BEFORE A WORD IS READ. ### b305 IMPORTED.')
    rec('=' * 100)
    rec('  source     : Connes-Consani, Weil positivity and trace formula, the archimedean place, arXiv:2006.13771v1')
    rec('  the pin    : %d bytes, sha256 %s (b304/b305, imported)' % (PIN_BYTES, PIN))
    cands = glob.glob(os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '*', 'tool-results', 'webfetch-*.pdf'))
    match = []
    for p in cands:
        try:
            if os.path.getsize(p) == PIN_BYTES and S5.sha256_file(p) == PIN:
                match.append(p)
        except OSError:
            pass
    rec('  local copies matching the pin, re-hashed now : %d' % len(match))
    for p in match[:3]:
        rec('      %s' % p)
    th = hashlib.sha256(io.open(TEXT, 'rb').read()).hexdigest()
    tb = os.path.getsize(TEXT)
    rec('  the text layer this act reads : %s, %d bytes, sha256 %s' % (os.path.basename(TEXT), tb, th))
    txt = io.open(TEXT, encoding='utf-8', errors='replace').read()
    frags = [('B (147) the Mellin transform', 'fpxqxs´1dx. (147)'),
             ('B (148) the explicit formula', 'Wvpfq, (148)'),
             ('B (149) the prime term', '. (149)'),
             ('B (150) the principal value', 'WRpfq :“p log 4π`γqfp1q`'),
             ('B (151) the Gamma form', '˜fpwqdw. (151)'),
             ('B (152) the digamma form', 'h`pτq ˜fpwqdτ'),
             ('B (153) h_+', 'h`pτq“´ logπ` ℜpλp1{4`iτ{2qq, λ pzq“ Γ1pzq{Γpzq. (153)'),
             ('(53) W_inf as a functional', 'fpρ´1qτpρqd˚ρ (53)')]
    miss = 0
    for lbl, f in frags:
        ok = f in txt
        miss += 0 if ok else 1
        rec('    %-34s located : %s' % (lbl, ok))
    rec('  ### FRAGMENTS NOT LOCATED : %d' % miss)
    rec('  ### THE TEXT LAYER IS A PDF EXTRACTION AND GARBLES ITS FORMULAS (b305): every equation is read')
    rec('  ### on the PAGE IMAGE as well, and quoted here in the transcription the record already carries.')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    print('\n'.join(L))
    return 0 if (match and not miss) else 1


if __name__ == '__main__':
    sys.exit(main())
