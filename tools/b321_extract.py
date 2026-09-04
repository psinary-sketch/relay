# -*- coding: utf-8 -*-
"""b321_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**

### ### **THE FINDER IS IMPORTED FROM `b317_extract.py`, NOT RE-IMPLEMENTED.** ### b317 lost four
### fragments to a normaliser it wrote itself; b318, b319 and b320 imported the repaired one, and
### this act does the same. ### **FOUR ACTS, ONE FINDER.**

### ### **WHAT THIS ACT NEEDS THAT b320 DID NOT.** ### b320 tested the instrument against ONE
### theorem. ### This act tests it against two more and then opens the window, which needs four
### things the paper states and this act may not supply from memory:
###   ### **THEOREM 4.7 / (83)** ### -- `Tr(ϑ(f) S) = W_infinity(f) + INT f(rho^-1) eps(rho) d*rho`,
###     ### **AN EQUALITY AND NOT AN INEQUALITY**, which is why it can close the exponent question
###     by measurement: b320's margin must be MINUS that integral, exactly.
###   ### **(1), THE RIEMANN-WEIL EXPLICIT FORMULA** ### -- the zero side against the places sum.
###   ### **(148) AND (149) IN APPENDIX B** ### -- ### **THE SAME FORMULA WRITTEN OUT WITH ITS SIGNS
###     ### AND ITS FINITE-PLACE TERM**, which is the only place in the paper that says what
###     `W_p(f)` IS. ### The act may not take the prime term's sign from the navigator.
###   ### **PROPOSITION C.1** ### -- ### **THE CRITERION ITSELF, VERBATIM.** ### Component 3 must
###     print what sign the criterion asks for beside what sign the finite instance has, and the
###     only honest source for the first is the paper's own sentence.

### ### **AND THE EXPONENT'S THREE SITES ARE RE-PULLED**, because Component 1 turns on which power
### of `rho` the remainder carries and b313 settled that by reading, not by fitting.
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

NOTES = os.path.join(ROOT, 'data', 'b321_extract_notes.txt')

SOURCE_FRAGMENTS = [
    # ### ---- THE SECOND THEOREM: an EQUALITY, and the remainder it names
    ('### THEOREM 4.7 / (83) -- THE EQUALITY, AND THE REMAINDER eps', 26,
     'Theorem4.7', 80, 1000),
    ('### (61) THE SCALING ACTION -- THE EXPONENT AT ITS DEFINING SITE', 22,
     'itsactionisgivenby', 220, 200),
    # ### ---- THE THIRD THEOREM: the explicit formula, and its signs
    ('### (1) THE RIEMANN-WEIL EXPLICIT FORMULA, AS THE PAPER OPENS WITH IT', 0,
     'equivalenttothenegativity', 140, 700),
    ('### (148) AND (149) -- THE SAME FORMULA WITH ITS SIGNS AND ITS FINITE PLACE', 49,
     'wherevrunsoverallplaces', 420, 560),
    ('### (9) L(f) = D(f) - W_infinity(f) -- THE SIGN CHAIN THE PAPER USES', 3,
     'thepositivityofthefollowingfunctional', 80, 420),
    # ### ---- THE CRITERION, VERBATIM
    ('### PROPOSITION C.1 -- THE POSITIVITY CRITERION ITSELF', 50,
     'PositivitycriterionWefollow', 80, 720),
    # ### ---- the statements b320 used, re-pulled so this act reads its own file
    ('THEOREM 1 -- THE THREE CONDITIONS ON g AND THE INEQUALITY', 2, 'Theorem 1 Let g', 60, 320),
    ('(53) W_infinity AND (54) THE VANISHING CONDITIONS', 16,
     'weinvestigatethefunctional', 260, 500),
    ('(38) THE PRINCIPAL VALUE, AND (39) THE KERNEL tau', 10, 'can be rewritten as', 60, 900),
    ('DEFINITION 3.1 -- POSITIVE DEFINITE', 16, 'positive definite when its Fourier', 120, 200),
]

CODE_FRAGMENTS = [
    ('### THE REMAINDER UNDER THE SOURCE EXPONENT -- b313 FLIPPED COPY, NOT THE OWNER',
     os.path.join('tools', 'e16', 'b313f_qeps_layer.py'), 98, 116),
    ('### AND THE CORPUS BANKED EXPONENT, THE SAME FUNCTION, FOR THE CONTRAST',
     os.path.join('tools', 'e16', 'b313r_qeps_layer.py'), 98, 116),
    ('THE SETTLED CHAIN -- the corpus own zero/pole/arch/prime channels',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 61, 82),
    ('### THE SIGN CONVENTION, IN THE ATLAS OWN HEADER',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 14, 25),
    ('THE TRUNCATION BOUND FOR THE ZERO SIDE',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 84, 91),
    ('THE ZERO LIBRARY -- independent of everything else in this act',
     os.path.join('tools', 'e16', 'zeta_ordinates.py'), 103, 116),
    ('THE ARCHIMEDEAN DISTRIBUTION -- b320, repaired and fixtured',
     os.path.join('tools', 'b320_weil.py'), 178, 196),
    ('THE PRODUCT AND THE SQUARE -- b318',
     os.path.join('tools', 'b318_square.py'), 113, 134),
]


def main(argv):
    good, arms = X7.self_test()
    lines = []

    def rec(s=''):
        lines.append(s)

    def flush(code):
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return code

    rec('=' * 100)
    rec("b321_extract.py -- THE EXTRACT STEP. ### **THE FINDER IS b317's, IMPORTED NOT COPIED.**")
    rec('=' * 100)
    rec('  finder source    : %s' % os.path.basename(X7.__file__))
    rec('  ### ITS FIXTURES, RUN HERE BEFORE IT IS TRUSTED : %s  %s'
        % (arms, 'PASS' if good else 'FAIL'))
    if not good:
        rec('  ### HARD FAILURE -- THE FINDER DOES NOT PASS ITS OWN FIXTURES. ### NOTHING READ.')
        return flush(1)
    if not argv:
        rec('  usage: python b321_extract.py <path-to-cc-pdf>')
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
    rec('  ### MATCHES THE PIN b304 SET AND b305/b317/b318/b320 RE-CHECKED : %s  %s'
        % (got == S5.EXPECT_SHA, 'YES' if got == S5.EXPECT_SHA else '### NO -- HARD FAILURE'))
    if got != S5.EXPECT_SHA:
        return flush(4)

    from pypdf import PdfReader
    pages = [p.extract_text() or '' for p in PdfReader(pdf).pages]
    rec('  pages     : %d' % len(pages))

    rec('')
    rec('-' * 100)
    rec('### THE SOURCE FRAGMENTS.')
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
    rec('### THE CODE FRAGMENTS. ### **THE INSTRUMENTS THIS ACT USES, READ THE SAME WAY.**')
    rec('-' * 100)
    cmissing = 0
    for label, rel, lo, hi in CODE_FRAGMENTS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            cmissing += 1
            rec('')
            rec('### ==== %s' % label)
            rec('###      %s | ### **NOT PRESENT**' % rel)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        rec('')
        rec('### ==== %s' % label)
        rec('###      %s | lines %d-%d' % (rel.replace(os.sep, '/'), lo, hi))
        for i in range(lo - 1, min(hi, len(body))):
            rec('    | %s' % body[i])
    rec('')
    rec('  ### ### **CODE FRAGMENTS NOT PRESENT : %d**' % cmissing)
    rec('')
    rec('  ### **AND THE ONE DISTINCTION THIS FILE EXISTS TO MAKE VISIBLE:** ### the two remainder')
    rec('  ### copies above differ in ONE character -- `r ** 0.5` against `r ** -0.5`. ### b313')
    rec('  ### settled which the SOURCE uses by reading three sites, and this act uses the flipped')
    rec('  ### copy on that ground and not because of any number it produces.')
    rec('=' * 100)
    return flush(0 if not (missing or cmissing) else 5)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
