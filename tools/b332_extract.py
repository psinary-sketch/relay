# -*- coding: utf-8 -*-
"""b332_extract.py -- THE EXTRACT STEP FOR THE CLAUSE STATED. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The deposit's own words on `h2` and its five registers, and
### its refusal to compile the cross-register equivalences; the register sentence; the source's class
### (Definition 3.1) and its criterion (Proposition C.1, the sign of the places sum) in the pinned text
### layer; every constituent's owner and grade at the act that emitted it -- the finite side (b329,
### b310), the prime sum (b306, b305), the archimedean distribution and its digamma witness (b320), the
### decomposition and the identity (b321), the square's nonnegativity (b318), the sign conventions
### (b321, b326's tool), the discriminating seeds inside the class (b328); the ledger's positivity row
### and the keystone the statement is cross-referenced from. ### b283's law: every quotation located
### at its emitting file and its line before it is written anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
KEY = os.path.join(PP, 'phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md')
FACESK = os.path.join(PP, 'phase2', 'method', 'FACES_OF_H2_AT_FINITE_INSTANCE.md')
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b332_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


WANTED = [
    # ### ---- the deposit: h2, the five registers, the refusal
    ('deposit -- what remains, exactly: h2', DEP, 'and h2 \u2014 nonvanishing of the transform at the point in question.'),
    ('### the five registers, first', DEP, 'First: the *universality hypothesis* carried by the Universal Silence Theorem.'),
    ('### the fourth register: balance and positivity', DEP, 'Fourth: the distance between *balance* and *positivity* at the multiplicative place.'),
    ('### its sharpest form', DEP, 'the premise is the inequality \u03bb_Z(n) \u2265 \u2212\u03bb_A(n) between two independently computable channels.'),
    ('### one premise in five registers', DEP, 'These are one premise in five registers: kernel-theoretic, formal-interface, category-shaped, analytic, and spectral-geometric.'),
    ('### the refusal to compile the equivalences', DEP, 'while deliberately **not** compiling the cross-register equivalences, since to compile "discharge one and you discharge all five" would be to compile RH-equivalence itself.'),
    ('### the finite-range certificate', DEP, "certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold"),
    # ### ---- the register sentence, at the faces-of-h2 keystone
    ('the register sentence', FACESK, 'THE REGISTER SENTENCE, UNTOUCHED BY EVERY WORD BELOW: `h2` IS THE SINGLE OPEN PREMISE.'),
    ('### R4 the one face with sign-content', FACESK, 'YES \u2014 the one face with sign-content'),
    # ### ---- the source, pinned text layer (b328's pin of the same source): the class and the criterion
    ('source -- Definition 3.1, positive definite', d('b328_source_text.txt'), 'positive de\ufb01nite when its Fourier transform is pointwise positive'),
    ('### the criterion, Proposition C.1', d('b328_source_text.txt'), 'Proposition C.1 Let Z \u0102 C be the set of non-trivial zeros of the Riemann zeta function and'),
    ('### RH iff the places sum is non-positive, for every g with the vanishing conditions', d('b328_source_text.txt'), 'Wvpg\u02da \u00afg7q\u010f 0, @gPC8'),
    ('### the negativity of the right-hand side of (1)', d('b328_source_text.txt'), 'it is enough to prove the negativity of the right-hand side of (1) for'),
    ('### the pin', d('b328_source.txt'), 'sha256'),
    # ### ---- the class as the corpus applies it, and the seeds inside it
    ('b320 -- Definition 3.1 applied: f-hat >= 0 pointwise', d('b320_the_lawful_function.txt'), '`f-hat >= 0` pointwise'),
    ('### the window fails, its square passes', d('b320_the_lawful_function.txt'), 'the window fails Definition 3.1, and its square passes at every cell.'),
    ('b328 -- the seeds lawful', d('b328_the_discriminating_family.txt'), '(F2) IS MET.'),
    ('### two lawful seeds, the places sum computed without any zero', d('b328_the_discriminating_family.txt'), 'two lawful seeds under which the finite-instance places sum, computed without any'),
    # ### ---- the places sum and its sign, from the owners
    ('b321 -- the pole term vanishes for a lawful f', d('b321_the_window_opened.txt'), 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
    ('### the places sum is minus the zero side', d('b321_the_window_opened.txt'), '`SUM_v W_v(f) = - Z`.**'),
    ('### Z cannot be negative', d('b321_the_window_opened.txt'), 'AND `Z` CANNOT BE NEGATIVE.'),
    ('### the count forced by the shape', d('b321_the_window_opened.txt'), 'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE OF ANYTHING.'),
    ("b326_windows -- the tool's sign convention", t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1'),
    ('### the sign through the gate', t('b326_windows.py'), 'the gate, then the sign: RESOLVED and |value| > SIGN_MARGIN x drift.'),
    # ### ---- the finite side
    ('b329 -- the finite side compiled', d('b329_the_finite_side_seal.txt'), "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS"),
    ('### never averaged', d('b329_the_finite_side_seal.txt'), 'FOR THE COMPACT PART, NEVER AVERAGED.**'),
    ('### the counting form compiled, the identification not', d('b329_the_finite_side_seal.txt'), "IT DOES NOT SAY THE SOURCE'S TRACE IS COMPILED."),
    ('b310 -- the source construction returns one term', d('b310_the_smear_collapses.txt'), 'THE SOURCE\'S CONSTRUCTION, AT A FINITE PLACE, RETURNS ONE TERM AND THERE IS NO'),
    ('### the test function read at one point times a dimension', d('b310_the_smear_collapses.txt'), 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION'),
    ('### not a claim the finite side contributes nothing', d('b310_the_smear_collapses.txt'), 'IT IS NOT A CLAIM THAT THE FINITE SIDE CONTRIBUTES NOTHING.'),
    # ### ---- the prime sum identified with the source's local term
    ("b306 -- the corpus's prime side is the source's finite-places sum", d('b306_the_difference.txt'), "IS THE CORPUS'S PRIME SIDE THE SOURCE'S FINITE-PLACES SUM? ### **YES -- AND THE TWO OPEN"),
    ('### factor for factor', d('b306_the_difference.txt'), "`k`-th term of `W_p` under CC's own `\u2206`-normalization, factor for factor."),
    # ### ---- the archimedean distribution and its digamma witness
    ('b320 -- the sign certified, the size not', d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ('### the digamma kernel, a second route', d('b320_the_lawful_function.txt'), 'against the digamma kernel `Re psi(1/4 + i u/2) - log pi`, read from the corpus\'s own'),
    ('### the archimedean term defined', d('b315_the_calibration_and_the_rate.txt'), 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    # ### ---- the decomposition: the compressed square plus the remainder
    ("b321 -- Theorem 4.7 is an equality", d('b321_the_window_opened.txt'), 'Theorem 4.7 / (83) is an ### **EQUALITY**, not'),
    ('### the identity', d('b321_the_window_opened.txt'), '`Tr(theta(f) S) = W_infinity(f) + INT f(rho^-1) eps(rho) d*rho`'),
    ("### b320's margin is minus the remainder", d('b321_the_window_opened.txt'), "that makes b320's margin exactly minus the remainder integral."),
    ('b318 -- the square is nonnegative at every cell and frame', d('b318_the_forced_sign.txt'), 'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT.'),
    ('b320 -- the margin measured, 27 of 27', d('b320_the_lawful_function.txt'), '27 OF 27 FRAMES'),
    ('b322 -- under-resolved with its price', d('b322_the_membership.txt'), 'VERDICT: ### UNDER-RESOLVED, WITH ITS PRICE.'),
    ('b300 -- the unit in by derivation, on imports', d('b300_the_archimedean_leg.txt'), 'GRADE: ### **DERIVES-on-IMPORTS**'),
    # ### ---- the arc's verdicts the statement's open part rests beside
    ("b326 -- does not see it on the arc's family", d('b326_the_reach.txt'), "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
    ('b328 -- sees it at seven of eight', d('b328_the_discriminating_family.txt'), 'SEES IT -- AT SEVEN OF EIGHT CELLS.'),
    ('### 146 on the line, 17 off', d('b326_the_reach.txt'), 'THE EPSTEIN ZEROS: 146 ON THE LINE TO `T = 150`, 17 OFF IT, AND THE COUNT'),
    # ### ---- the ledger and the keystone the statement is placed in
    ("the ledger's positivity row", os.path.join(PP, 'FACES_LEDGER.md'), '| R4 | R4 -- the distance between balance and positivity at the multiplicative place'),
    ("### the ledger's identity row", os.path.join(PP, 'FACES_LEDGER.md'), '| F1 | F1 -- the finite-instance identity: the explicit formula Z = P'),
    ("### the ledger's F5 row after b329", os.path.join(PP, 'FACES_LEDGER.md'), 'PROVED-GENERAL (the scaling part'),
    ('the arc keystone -- its placement section', KEY, '## \u00a78 \u2014 Placement'),
    ('### cross-references appended and not rewritten', KEY, '**Cross-references, appended and not rewritten:**'),
    ('### it states grades and confers none', KEY, '*The results above are their owning acts\u2019. This document states grades and confers none.*'),
    ("b331 -- the fold's desk names the two next acts", d('b331_the_fold.txt'), 'NEXT, BY THE ORDER: THE DISCHARGE-STATEMENT AND THE AIM-MAP -- AND NEITHER IS THE DISCHARGE.'),
    ("FINDINGS -- the b327 anchor's form", os.path.join(PP, 'FINDINGS.md'), '<a id="faces-ledger"></a>*Stable anchor: `faces-ledger`'),
    ('### the last section before this act', os.path.join(PP, 'FINDINGS.md'), '## THE DISCRIMINATING-FAMILY ARC, b323'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b332_extract.py -- THE CLAUSE STATED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    fl = os.path.join(PP, 'FINDINGS.md')
    txt = io.open(fl, encoding='utf-8', errors='replace').read()
    rec('### ==== FINDINGS.md before the append : %d lines, %d bytes, %d sections' % (len(txt.splitlines()), len(txt.encode('utf-8')), len([x for x in txt.splitlines() if x.startswith('## ')])))
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
