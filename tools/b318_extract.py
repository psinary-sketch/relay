# -*- coding: utf-8 -*-
"""b318_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**

### ### **THE FINDER IS IMPORTED FROM `b317_extract.py`, NOT RE-IMPLEMENTED.** ### b317 lost four
### fragments to a normaliser it had written itself without the `NFKD` step that
### `b305_source.flatten` already carried, and its bank named the duplication as the cause. ### **AN
### ### ACT THAT COPIED THAT FINDER AGAIN WOULD BE REPEATING THE DEFECT IT WAS TOLD ABOUT**, so this
### file imports `window`, `fold_anchor` and the finder's own fixtures and adds only its own
### fragment list.

### ### **WHAT THIS ACT NEEDS FROM THE SOURCE, AND WHY IT IS MORE THAN b317 NEEDED.** ### b317
### assembled the trace. ### This act asks whether the corpus's window is in the class the source's
### POSITIVITY attaches to, and that class is stated in four separate places in the paper -- the
### definition of positive-definite, the square form the functional is evaluated on, the interval the
### source's own `g` must live in, and the counterexample the source itself gives. ### **ALL FOUR ARE
### ### LOCATED HERE BEFORE ANY OF THEM IS USED**, and the eigenvalue-one characterization is located
### with them because Component 3's refinement scheme is specified from it.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5    # noqa: E402  ### the pin, READ never copied
import b317_extract as X7   # noqa: E402  ### the finder, IMPORTED never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(ROOT, 'data', 'b318_extract_notes.txt')

# ### ==============================================================================================
# ### THE SOURCE FRAGMENTS THIS ACT NEEDS. ### **NAMED BEFORE THEY ARE READ.**
# ### `(label, page_index, anchor, before, after)`.
# ### ==============================================================================================
SOURCE_FRAGMENTS = [
    # ### ---- carried from b317, because the normalizations are quoted once and used here again
    ('(53) W_infinity AND (54) THE VANISHING CONDITIONS', 16,
     'weinvestigatethefunctional', 260, 700),
    ('(61) THE SCALING ACTION', 22, 'itsactionisgivenby', 220, 280),
    ('DEFINITION 4.4 / (72) THE SPACE S(a,b)', 24, 'Definition4.4For', 20, 380),
    ('THEOREM 4.7 -- (83)', 26, 'Theorem4.7', 120, 500),
    # ### ---- NEW, AND THEY ARE THE ACT
    ('### THE SOURCE OWN DEFINITION OF POSITIVE-DEFINITE', 16,
     'positive definite when its Fourier', 120, 260),
    ('### THE SQUARE FORM, IN THE SOURCE OWN VOICE', 1, 'when evaluated on', 260, 340),
    ('### THE QUADRATIC FORM Q_W AND ITS VECTOR SPACE V', 1,
     'positivity of the quadratic form', 60, 480),
    ('### THEOREM 3 -- THE FUNCTIONAL IS POSITIVE', 5, 'Theorem 3 The functional', 60, 420),
    ('### THEOREM 1 -- THE INTERVAL THE SOURCE OWN g MUST LIVE IN', 2,
     'Theorem 1 Let g', 60, 420),
    ('### THE AUTOCORRELATION FORM, IN THE INTRODUCTION', 0, 'gpxyqgpyqdy', 260, 120),
    ('### f-hat = |g-hat|^2, THE LINK BETWEEN THE TWO', 16, 'shows that f is positive', 240, 200),
    ('### THE SOURCE OWN COUNTEREXAMPLE: (54) HOLDS AND W_infinity IS NEGATIVE', 16,
     'but for which', 200, 260),
    ('### THE EIGENVALUE-ONE CHARACTERIZATION OF S(1,1)', 27, 'is the eigenspace of', 200, 160),
]

# ### ==============================================================================================
# ### THE CODE FRAGMENTS. ### `(label, relative path, first line, last line)`, 1-INDEXED INCLUSIVE.
# ### ==============================================================================================
CODE_FRAGMENTS = [
    ('THE VARIANT -- how b317 built the mean-zero test function this act judges',
     os.path.join('tools', 'b317_smear.py'), 165, 207),
    ('THE KERNEL -- b317 assembly of theta(f), which this act squares',
     os.path.join('tools', 'b317_smear.py'), 227, 246),
    ('THE COMPRESSED TRACE -- b317 smear column, recomputed by this act',
     os.path.join('tools', 'b317_smear.py'), 289, 312),
    ('THE PROJECTOR -- b316 subspace, whose RANK is printed beside every number',
     os.path.join('tools', 'b316_instrument.py'), 93, 113),
    ('THE CORPUS BUMP -- its emitting file',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 43, 52),
]


def main(argv):
    good, arms = X7.self_test()
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b318_extract.py -- THE EXTRACT STEP. ### **THE FINDER IS b317\'s, IMPORTED NOT COPIED.**')
    rec('=' * 100)
    rec('  finder source    : %s' % os.path.basename(X7.__file__))
    rec('  ### ITS FIXTURES, RUN HERE BEFORE IT IS TRUSTED : %s  %s'
        % (arms, 'PASS' if good else 'FAIL'))
    rec('  ### **ARMS 6-8 ARE THE ONES b317 ADDED AND THIS ACT DEPENDS ON:** ### an ASCII anchor')
    rec('  ### finds a ligatured page, an absent anchor is still refused, and the printed window')
    rec('  ### still carries the ligature the source actually set.')
    if not good:
        rec('  ### HARD FAILURE -- THE FINDER DOES NOT PASS ITS OWN FIXTURES. ### NOTHING READ.')
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 1

    if not argv:
        rec('  usage: python b318_extract.py <path-to-cc-pdf>')
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
    rec('  url       : %s' % S5.SOURCE_URL)
    rec('  bytes     : %d' % os.path.getsize(pdf))
    rec('  sha256    : %s' % got)
    rec('  ### MATCHES THE VALUE b304 PINNED, b305 RE-COMPUTED AND b317 RE-CHECKED : %s  %s'
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
    rec('### **THE TEXT LAYER RENDERS PARENTHESES AS `p`/`q` AND BREAKS WORDS ACROSS LINES.**')
    rec('### ### **EVERY WINDOW BELOW IS RAW. ### THE READING OF IT IS THE AUTHOR\'S, NOT THIS')
    rec('### ### TOOL\'S, AND THE BANK MARKS IT SO.**')
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
            rec('### ### **NOT FOUND ON THAT PAGE.** ### The fragment the act names is not where')
            rec('### ### the act says it is, and that is a HARD failure for this fragment.')
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
    print('b318_extract: wrote %s  (%d bytes, %d lines)'
          % (os.path.basename(NOTES), os.path.getsize(NOTES), len(lines)))
    print('  source fragments missing : %d' % missing)
    print('  code fragments missing   : %d' % cmissing)
    return 0 if (missing == 0 and cmissing == 0) else 5


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
