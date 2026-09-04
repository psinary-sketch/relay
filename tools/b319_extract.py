# -*- coding: utf-8 -*-
"""b319_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**

### ### **THE FINDER IS IMPORTED FROM `b317_extract.py`, NOT RE-IMPLEMENTED** -- b317 lost four
### fragments to a normaliser it wrote itself, b318 imported the repaired one instead, and this act
### does the same. ### **THREE ACTS, ONE FINDER.**

### ### **WHAT THIS ACT NEEDS THAT NO EARLIER ACT DID: ### THE SANDWICH AND ITS SPECTRUM.** ### b318
### located the eigenvalue-one characterization and filed a scheme from it. ### Building that scheme
### needs three more things the paper states and this act may not invent:
###   ### the two projections in the source's own normalization, so the sandwich is the source's;
###   ### the SPECTRAL DECOMPOSITION of `P P-hat P`, whose eigenvalues are the `lambda(n)^2`;
###   ### and the bandwidth parameter that fixes which prolate eigenvalues those are.
### ### **TOGETHER THEY ARE THE ARGUMENT FOR THE THRESHOLD**, which the registration fixes before
### any spectrum of this act's own is seen.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5    # noqa: E402
import b317_extract as X7   # noqa: E402  ### the finder, IMPORTED never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(ROOT, 'data', 'b319_extract_notes.txt')

SOURCE_FRAGMENTS = [
    # ### ---- the normalizations, quoted once and used again
    ('(16) THE INNER PRODUCT', 6, 'inL2pRqevasfollows', 40, 200),
    ('(24) THE TRANSFORM', 7, 'itdefinestheunitary', 60, 200),
    ('DEFINITION 4.4 / (72) THE SPACE S(a,b)', 24, 'Definition4.4For', 20, 300),
    # ### ---- NEW, AND THEY ARE THE ACT
    ('### (61) AND THE TWO PROJECTIONS, IN THE SOURCE OWN NORMALIZATION', 22,
     'The projection P', 120, 320),
    ('### THE SPECTRAL DECOMPOSITION (81) OF THE SANDWICH', 25,
     'The spectral decomposition of the positive operator', 220, 420),
    ('### THE EIGENVALUE-ONE CHARACTERIZATION OF S(1,1)', 27, 'is the eigenspace of', 220, 120),
    ('### THE PROLATE FUNCTIONS AND THE BANDWIDTH PARAMETER', 23,
     'with bandwidth parameter', 200, 200),
    ('THEOREM 4.7 -- (83)', 26, 'Theorem4.7', 60, 300),
]

CODE_FRAGMENTS = [
    ('THE GRID SCHEME THIS ACT REPLACES -- b316 subspace, and its moving tolerance',
     os.path.join('tools', 'b316_instrument.py'), 93, 113),
    ('THE TRANSFORM MATRIX the sandwich is built from',
     os.path.join('tools', 'b316_instrument.py'), 83, 86),
    ('THE SQUARE this act reproduces at stable rank',
     os.path.join('tools', 'b318_square.py'), 139, 160),
    ('THE AUTOCORRELATION whose smear the square must equal',
     os.path.join('tools', 'b318_square.py'), 120, 134),
    ('THE COMPRESSED TRACE, b317 own',
     os.path.join('tools', 'b317_smear.py'), 289, 312),
]


def main(argv):
    good, arms = X7.self_test()
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b319_extract.py -- THE EXTRACT STEP. ### **THE FINDER IS b317\'s, IMPORTED NOT COPIED.**')
    rec('=' * 100)
    rec('  finder source    : %s' % os.path.basename(X7.__file__))
    rec('  ### ITS FIXTURES, RUN HERE BEFORE IT IS TRUSTED : %s  %s'
        % (arms, 'PASS' if good else 'FAIL'))
    if not good:
        rec('  ### HARD FAILURE -- THE FINDER DOES NOT PASS ITS OWN FIXTURES. ### NOTHING READ.')
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 1
    if not argv:
        rec('  usage: python b319_extract.py <path-to-cc-pdf>')
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 2
    pdf = argv[0]

    rec('')
    rec('-' * 100)
    rec('### THE PIN. ### **BEFORE A WORD OF THE ARTEFACT IS READ.**')
    rec('-' * 100)
    if not os.path.exists(pdf):
        rec('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 3
    got = S5.sha256_file(pdf)
    rec('  artefact  : %s' % os.path.basename(pdf))
    rec('  cite      : %s' % S5.SOURCE_CITE)
    rec('  sha256    : %s' % got)
    rec('  ### MATCHES THE PIN b304 SET AND b305, b317, b318 RE-CHECKED : %s  %s'
        % (got == S5.EXPECT_SHA, 'YES' if got == S5.EXPECT_SHA else '### NO -- HARD FAILURE'))
    if got != S5.EXPECT_SHA:
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 4

    from pypdf import PdfReader
    r = PdfReader(pdf)
    rec('  pages     : %d' % len(r.pages))

    rec('')
    rec('-' * 100)
    rec('### THE SOURCE FRAGMENTS, LOCATED BY PAGE INDEX.')
    rec('### ### **EVERY WINDOW BELOW IS RAW. ### THE READING OF IT IS THE AUTHOR\'S.**')
    rec('-' * 100)
    missing = 0
    for label, pg, anchor, before, after in SOURCE_FRAGMENTS:
        raw = r.pages[pg].extract_text() or ''
        text, off = X7.window(raw, anchor, before, after)
        rec('')
        rec('### ==== %s' % label)
        rec('###      page index %d (printed page %d) | anchor %r | char offset %s'
            % (pg, pg + 1, anchor, off if off >= 0 else 'NOT FOUND'))
        if text is None:
            rec('### ### **NOT FOUND ON THAT PAGE.** ### HARD failure for this fragment.')
            missing += 1
            continue
        for ln in text.splitlines():
            rec('    | %s' % ln)
    rec('')
    rec('### SOURCE FRAGMENTS NOT FOUND : %d' % missing)

    rec('')
    rec('-' * 100)
    rec('### THE CODE FRAGMENTS, BY FILE AND LINE RANGE. ### **1-INDEXED, INCLUSIVE.**')
    rec('-' * 100)
    cmissing = 0
    for label, rel, lo, hi in CODE_FRAGMENTS:
        path = os.path.join(ROOT, rel)
        rec('')
        rec('### ==== %s' % label)
        rec('###      %s : lines %d-%d' % (rel.replace(os.sep, '/'), lo, hi))
        if not os.path.exists(path):
            rec('### ### **FILE NOT FOUND.**')
            cmissing += 1
            continue
        src = io.open(path, encoding='utf-8').read().splitlines()
        for i in range(lo - 1, min(hi, len(src))):
            rec('  %5d | %s' % (i + 1, src[i]))
    rec('')
    rec('### CODE FRAGMENTS NOT FOUND : %d' % cmissing)
    rec('')
    rec('=' * 100)

    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('b319_extract: wrote %s  (%d bytes, %d lines)'
          % (os.path.basename(NOTES), os.path.getsize(NOTES), len(lines)))
    print('  source fragments missing : %d' % missing)
    print('  code fragments missing   : %d' % cmissing)
    return 0 if (missing == 0 and cmissing == 0) else 5


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
