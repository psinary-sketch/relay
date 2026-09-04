# -*- coding: utf-8 -*-
"""b322_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**

### ### **THE FINDER IS IMPORTED FROM `b317_extract.py`, NOT RE-IMPLEMENTED.** ### Five acts, one
### finder.

### ### ### **AND THIS ACT'S READS ARE MOSTLY NOT AT THE SOURCE, WHICH IS THE POINT OF IT.** ### The
### question is which of TWO REALIZATIONS the derivation was about, so the reads are at the OWNERS
### that hold each constituent, and ### **b283's LAW GOVERNS EVERY ONE: ### A NEEDLE IS PULLED FROM
### ### THE FILE THAT EMITTED THE SENTENCE, NEVER FROM A FILE THAT QUOTES IT.**
###   ### **CM LEMMA 3.1** ### is pulled from `data/b202_sum_test.txt`, which names
###     `arXiv:2112.05500v1` in its own header and is the file that read it. ### **NOT FROM b300**,
###     which quotes it.
###   ### **b211's (C3) CHAIN** ### from `data/b211_alternation_derived.txt`.
###   ### **b203's FENCE** ### -- *`F phi = xi` is NOT `F phi = phi`* -- from
###     `data/b203_transform_convention.txt`. ### **THIS ONE MATTERS MORE THAN ITS LENGTH SUGGESTS**:
###     the derivation of condition two would be circular if that fence had been crossed, and the
###     act has to read the fence rather than trust that it held.
###   ### **b300's VERDICT (b)** ### from `data/b300_the_archimedean_leg.txt`, the deriving act.
###   ### **b319's RESIDUAL TABLE** ### and ### **b321's INSTRUMENT LADDER** ### from their banks,
###     because Component 1 compares two courses and must quote both from their own acts.
### ### **THE CC FRAGMENTS ARE STILL PULLED FROM THE PINNED PDF**, because the space, the transform
### and the inner product are the source's and not the corpus's.
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

NOTES = os.path.join(ROOT, 'data', 'b322_extract_notes.txt')

SOURCE_FRAGMENTS = [
    ('### DEFINITION 4.4 / (72) -- THE SPACE S(a,b), THE TWO CONDITIONS', 24,
     'Definition4.4For', 20, 320),
    ('### (16) -- THE INNER PRODUCT AND ITS NORMALIZATION', 6, 'inL2pRqevasfollows', 40, 220),
    ('### (24) -- THE TRANSFORM ON EVEN FUNCTIONS', 7, 'itdefinestheunitary', 60, 220),
    ('(61) -- THE SCALING ACTION', 22, 'itsactionisgivenby', 220, 140),
]

# ### **THE CORPUS READS. ### EACH AT THE FILE THAT EMITTED THE SENTENCE.**
CORPUS_FRAGMENTS = [
    ('### CM LEMMA 3.1 -- CONDITION ONE, AND THE EVENNESS. ### EMITTER: b202',
     os.path.join('data', 'b202_sum_test.txt'), 13, 34),
    ("### b211's (C3) -- THE EIGENRELATION CONDITION TWO RESTS ON. ### EMITTER: b211",
     os.path.join('data', 'b211_alternation_derived.txt'), 188, 200),
    ("### b203's FENCE -- `F phi = xi` IS NOT `F phi = phi`. ### EMITTER: b203",
     os.path.join('data', 'b203_transform_convention.txt'), 140, 152),
    ("### b300's VERDICT (b) -- THE DERIVATION UNDER TEST. ### EMITTER: b300",
     os.path.join('data', 'b300_the_archimedean_leg.txt'), 283, 300),
    ("### b319's RESIDUAL TABLE -- BOTH CUTS, EIGHT FRAMES. ### EMITTER: b319",
     os.path.join('data', 'b319_the_stable_rank.txt'), 295, 313),
    ("### b321's INSTRUMENT LADDER -- THE RATE THIS ACT COMPARES AGAINST. ### EMITTER: b321",
     os.path.join('data', 'b321_the_window_opened.txt'), 12, 24),
]

CODE_FRAGMENTS = [
    ('### THE INSTRUMENT REALIZATION -- b316 `sonin_unit`, WHOLE',
     os.path.join('tools', 'b316_instrument.py'), 149, 181),
    ("### THE SOURCE'S TRANSFORM AND INNER PRODUCT, AS THE FRAME HOLDS THEM",
     os.path.join('tools', 'b316_instrument.py'), 70, 92),
    ('### THE TWO CONDITIONS AS INDEX SETS, AND THE PROJECTOR',
     os.path.join('tools', 'b316_instrument.py'), 93, 124),
    ('### THE EDGE DIAGNOSTIC -- b316 `taper`',
     os.path.join('tools', 'b316_instrument.py'), 183, 195),
    ('### AND THE DECAY DIAGNOSTIC -- b316 `asymptotics`',
     os.path.join('tools', 'b316_instrument.py'), 197, 220),
    ('### THE SPACE AS THE STABLE-RANK SCHEME SELECTS IT -- b319',
     os.path.join('tools', 'b319_stable.py'), 71, 96),
    ('### THE BASE OBJECT -- the corpus radial solver both realizations bottom out in',
     os.path.join('tools', 'e16', 'b205_prolate.py'), 1, 22),
]


def main(argv):
    good, arms = X7.self_test()
    lines = []

    def rec(s=''):
        lines.append(s)

    def flush(code):
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return code

    def block(label, rel, lo, hi):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            rec('')
            rec('### ==== %s' % label)
            rec('###      %s | ### **NOT PRESENT**' % rel.replace(os.sep, '/'))
            return 1
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        rec('')
        rec('### ==== %s' % label)
        rec('###      %s | lines %d-%d' % (rel.replace(os.sep, '/'), lo, hi))
        for i in range(lo - 1, min(hi, len(body))):
            rec('    | %s' % body[i])
        return 0

    rec('=' * 100)
    rec("b322_extract.py -- THE EXTRACT STEP. ### **THE FINDER IS b317's, IMPORTED NOT COPIED.**")
    rec('=' * 100)
    rec('  finder source    : %s' % os.path.basename(X7.__file__))
    rec('  ### ITS FIXTURES, RUN HERE BEFORE IT IS TRUSTED : %s  %s'
        % (arms, 'PASS' if good else 'FAIL'))
    if not good:
        rec('  ### HARD FAILURE -- THE FINDER DOES NOT PASS ITS OWN FIXTURES. ### NOTHING READ.')
        return flush(1)
    if not argv:
        rec('  usage: python b322_extract.py <path-to-cc-pdf>')
        return flush(2)
    pdf = argv[0]

    rec('')
    rec('-' * 100)
    rec('### THE PIN. ### **BEFORE A WORD OF THE ARTEFACT IS READ.**')
    rec('-' * 100)
    if not os.path.exists(pdf):
        rec('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        return flush(3)
    got = S5.sha256_file(pdf)
    rec('  artefact  : %s' % os.path.basename(pdf))
    rec('  cite      : %s' % S5.SOURCE_CITE)
    rec('  sha256    : %s' % got)
    rec('  ### MATCHES THE PIN b304 SET AND EVERY ACT SINCE RE-CHECKED : %s  %s'
        % (got == S5.EXPECT_SHA, 'YES' if got == S5.EXPECT_SHA else '### NO -- HARD FAILURE'))
    if got != S5.EXPECT_SHA:
        return flush(4)

    from pypdf import PdfReader
    pages = [p.extract_text() or '' for p in PdfReader(pdf).pages]
    rec('  pages     : %d' % len(pages))

    rec('')
    rec('-' * 100)
    rec("### (A) THE SOURCE FRAGMENTS. ### **THE SPACE, THE TRANSFORM, THE INNER PRODUCT.**")
    rec('-' * 100)
    missing = 0
    for label, page, anchor, before, after in SOURCE_FRAGMENTS:
        raw = pages[page] if page < len(pages) else ''
        try:
            txt, off = X7.window(raw, anchor, before, after)
        except LookupError:
            missing += 1
            rec('')
            rec('### ==== %s' % label)
            rec('###      page index %d | anchor %r | ### **NOT FOUND**' % (page, anchor))
            continue
        rec('')
        rec('### ==== %s' % label)
        rec('###      page index %d (printed page %d) | anchor %r | char offset %d'
            % (page, page + 1, anchor, off))
        for ln in txt.splitlines():
            rec('    | %s' % ln)
    rec('')
    rec('  ### ### **SOURCE FRAGMENTS NOT FOUND : %d**' % missing)

    rec('')
    rec('-' * 100)
    rec('### (B) THE CORPUS READS, EACH AT THE FILE THAT EMITTED THE SENTENCE.')
    rec('-' * 100)
    cmissing = sum(block(*f) for f in CORPUS_FRAGMENTS)
    rec('')
    rec('  ### ### **CORPUS FRAGMENTS NOT PRESENT : %d**' % cmissing)

    rec('')
    rec('-' * 100)
    rec("### (C) THE CODE FRAGMENTS. ### **THE INSTRUMENT'S REALIZATION, UNFOLDED.**")
    rec('-' * 100)
    kmissing = sum(block(*f) for f in CODE_FRAGMENTS)
    rec('')
    rec('  ### ### **CODE FRAGMENTS NOT PRESENT : %d**' % kmissing)
    rec('')
    rec('  ### **AND THE ONE THING THIS FILE EXISTS TO PUT SIDE BY SIDE:** ### CM Lemma 3.1 defines')
    rec('  ### `phi_mu` on the WHOLE half-line -- *"zero on `[-1,1]` and agrees with `f_mu(x)` for')
    rec('  ### `x > 1`"* -- and `b316.sonin_unit` builds it on `[0, X]` for a FINITE `X`.')
    rec('  ### **WHETHER THAT IS THE DIFFERENCE IS COMPONENT 1\'S TO DECIDE FROM NUMBERS**, and')
    rec('  ### this file only makes the two statements readable in one place.')
    rec('=' * 100)
    return flush(0 if not (missing or cmissing or kmissing) else 5)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
