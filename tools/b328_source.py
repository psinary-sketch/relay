# -*- coding: utf-8 -*-
"""b328_source.py -- THE SOURCE'S EXPLICIT FORMULA, ITS POLE TERMS AND ITS CRITERION, PINNED AND LOCATED.

### ### **THE FLATTENER AND THE HASH CHECK ARE IMPORTED FROM `b305_source.py`, NEVER COPIED**, and the
### PIN is the corpus's own (`b305_source.EXPECT_SHA`, banked b304 and re-computed b305): the artefact
### is Connes-Consani, arXiv:2006.13771v1, re-acquired by fetch in this session and matched to that pin
### before a word of it was read. ### **A RE-ACQUISITION THAT MATCHES THE PIN IS THE PINNED ARTEFACT.**

### ### **WHAT THIS ACT QUOTES FROM IT, AND WHY.** ### The order says: *the criterion evaluated as the
### source states it, with pole terms handled as the source handles them and quoted.* ### That is the
### source's Appendix B -- (147) the Mellin transform, `f^7(x) := x^{-1} f(x^{-1})`, (148) the explicit
### formula whose two pole terms are `INT f dx` and `INT f^7 dx`, (149) the prime term -- and its Appendix
### C, Proposition C.1: RH iff `SUM_v W_v(g * g^7) <= 0` for every `g` whose Mellin transform vanishes on
### a finite set `F` containing `{0, 1}` -- ### **THE POLE TERMS ARE HANDLED BY REQUIRING THE SEED'S
### TRANSFORM TO VANISH AT 0 AND 1, AND THAT IS WHAT THIS ACT REQUIRES OF ITS SEEDS.** ### Also the
### vanishing conditions (54), Theorem 1's own conditions, and the sentence isolating the zeros.

### ### **WHAT IT DOES NOT DO: IT DOES NOT READ.** ### It locates; a fragment absent is loud; a fragment
### present is not thereby the right fragment.
"""
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OUT = os.path.join(ROOT, 'data', 'b328_source.txt')
TEXT = os.path.join(ROOT, 'data', 'b328_source_text.txt')
EXPECT_SHA = S5.EXPECT_SHA
EXPECT_BYTES = 1213504
CACHE_GLOB = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '*', 'tool-results', 'webfetch-*.pdf')

FRAGMENTS = [
    ('B1 (147) the Mellin transform, as the appendix defines it', 'one defines the Mellin transform of a function', 'f P C8'),
    ('B2 the involution f^7 and the explicit formula (148)', 'the explicit formula takes the form', None),
    ('B3 ### the two pole terms are the integrals of f and f^7, the places subtracted', 'where v runs over all places', 'the sum on the left hand side is over all complex'),
    ('B4 (149) the prime term', 'and for v', 'p logpq'),
    ('B5 (150) the archimedean distribution as a principal value', 'The archimedean distribution is defined as', None),
    ('C1 Proposition C.1, the positivity criterion', 'Positivity criterion', 'We follow'),
    ('C2 ### RH iff the places sum is non-positive on g conv g^7 with the transform vanishing on F', 'be the set of non-trivial zeros of the Riemann zeta function', 'a finite set disjoint from Z and containing'),
    ('C3 ### the pole terms handled by the hypothesis {0,1} in F', 'follows from the explicit formula (148) and the hypothesis', None),
    ('V1 (54) the vanishing conditions', 'we assume the vanishing conditions', None),
    ('V2 ### what they isolate', 'to isolate on the left hand side of the explicit formula the contribution of the zeros', None),
    ('T1 Theorem 1: support and the two vanishing conditions on g', 'have support in the interval', 'Fourier transform'),
    ('T2 ### vanishing at i/2 and 0', 'vanishing at i', 'and 0. Then one has'),
    ('W1 Weil\'s inequality, the change of sign noted', 'note the change of sign', None),
    ('W2 ### W_inf := -W_R', 'W8pfq', 'whereW8'),
]


def locate_pdf():
    hits = []
    for p in glob.glob(CACHE_GLOB):
        try:
            if os.path.getsize(p) == EXPECT_BYTES and S5.sha256_file(p) == EXPECT_SHA:
                hits.append(p)
        except OSError:
            pass
    return hits


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s)

    rec('=' * 100)
    rec('b328_source.py -- THE SOURCE\'S EXPLICIT FORMULA AND CRITERION, PINNED AND LOCATED. ### b305\'s PIN AND FLATTENER, IMPORTED.')
    rec('=' * 100)
    ok = bool(S5.self_test(verbose=False))
    rec('  b305 flattener self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        return 2
    rec('  source   : Connes-Consani, Weil positivity and trace formula, the archimedean place, arXiv:2006.13771v1')
    rec('  the pin  : %d bytes, sha256 %s (b304/b305, imported)' % (EXPECT_BYTES, EXPECT_SHA))
    found = locate_pdf()
    rec('  copies matching the pin in this machine\'s fetch caches : %d' % len(found))
    for p in found:
        rec('      %s' % p)
    if not found:
        rec('  ### HARD FAILURE -- NO COPY MATCHES THE PIN; RE-FETCH AND COMPARE, A MISMATCH IS A DIFFERENT DOCUMENT.')
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 2
    import pypdf
    reader = pypdf.PdfReader(found[0])
    pages = [(pg.extract_text() or '') for pg in reader.pages]
    full = '\n'.join('=== PAGE %d ===\n%s' % (i + 1, t) for i, t in enumerate(pages))
    io.open(TEXT, 'w', encoding='utf-8', newline='\n').write(full)
    rec('  pages    : %d ; text layer written to data/%s (%d chars)' % (len(pages), os.path.basename(TEXT), len(full)))
    flat_pages = [S5.flatten(t) for t in pages]
    rec('')
    rec('  ### THE FRAGMENTS, EACH SEARCHED FLATTENED ON BOTH SIDES; A MISS IS LOUD.')
    missing = 0
    for lbl, a, b in FRAGMENTS:
        fa, fb = S5.flatten(a), (S5.flatten(b) if b else None)
        where = [i + 1 for i, fp in enumerate(flat_pages) if fa in fp and (fb is None or fb in fp)]
        if not where:
            missing += 1
        rec('    %-92s pages %s %s' % (lbl[:92], where if where else '-', '' if where else '### NOT LOCATED ###'))
    rec('')
    rec('  ### FRAGMENTS NOT LOCATED : %d' % missing)
    rec('  ### **THIS TOOL LOCATES. ### IT DOES NOT READ.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not missing else 5


if __name__ == '__main__':
    sys.exit(main())
