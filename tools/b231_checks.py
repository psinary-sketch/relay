# -*- coding: utf-8 -*-
"""b231_checks.py -- the b231 gates, routed through the b217 harness.

### THIS ACT'S RISKS ARE FOUR, AND EACH HAS A GATE:
###   (1) that an (ABSENT) is filed on a CRASHED SEARCH -- which nearly happened here:
###       `grep -iF` aborts in this build (rc=134) and a killed grep looks exactly like a
###       clean absence. ### THE PAIR GATE RE-RUNS THE SEARCH IN-PROCESS, WITH A CONTROL.
###   (2) that the shadow COMPILES but does not PROVE (b227) -- the profile is the gate.
###   (3) that the verdict quietly upgrades (PARTIAL) to (DERIVED) by leaving the imports out.
###   (4) that the log p quarry is promoted while nobody is looking.
### Every needle below was grep-verified against every file it is used on BEFORE the gate
### was written, including for LINE-WRAPPING, which silently breaks an exact quotation.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b231_the_two.txt')
REG = os.path.join(D, 'b231_registration_2026-08-28.txt')
RUN = os.path.join(D, 'b231_evenness_run.txt')
B229 = os.path.join(D, 'b229_statement_adopted.txt')
B230 = os.path.join(D, 'b230_engine_statement_and_price.txt')

INSTR = os.path.join(ROOT, 'tools', 'e16', 'b38_act10.py')
ATLAS = os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py')
SHADOW = os.path.join(SGS, 'Core', 'FoldedMirrorShadow.lean')
PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')
GEN = os.path.join(SGS, 'AllPrints.lean')
CORRMD = os.path.join(SGS, 'CORRESPONDENCE.md')

# ### THE TWO-ENDED PAIR, IN EVERY NOTATION THE ACT TESTED.
PAIR_RE = re.compile(
    r'g\(\s*[-\u2212\u00b1]\s*log|g\(x\)\s*\+\s*g\(|g\(u\)\s*\+\s*g\(|'
    r'log n\)\s*\+\s*g|\+\s*g\(\s*[-\u2212]\s*log|f\(\s*[-\u2212]\s*log',
    re.I)

# ### THE CONTROL STRING: known to stand at 200+ occurrences. ### IF A SWEEP CANNOT FIND
# ### THIS, THE SWEEP IS BROKEN AND ITS ZEROS MEAN NOTHING (b220; and this act's own crash).
CONTROL_RE = re.compile(r'explicit formula', re.I)


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def both(path, a, b):
    return contains(path, a) and contains(path, b)


def count_lines(path):
    """### A MISSING FILE RETURNS -1, NEVER 0."""
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return sum(1 for _ in fh)


def count_sub(path, needle):
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return len(re.findall(re.escape(needle), fh.read(), re.I))


def sweep(rx, roots=(PLACE,), exts=('.md',)):
    """### IN-PROCESS SEARCH -- no subprocess to abort silently. Returns a HIT COUNT."""
    hits = 0
    for root in roots:
        for dirpath, _dirs, files in os.walk(root):
            if '.git' in dirpath:
                continue
            for fn in files:
                if not fn.endswith(exts):
                    continue
                try:
                    with open(os.path.join(dirpath, fn), encoding='utf-8',
                              errors='replace') as fh:
                        hits += len(rx.findall(fh.read()))
                except OSError:
                    continue
    return hits


def main():
    h = Harness(ROOT, 'b231')

    # 1 -- ### THE EVENNESS IS STRUCTURAL: the bump depends on t only through t**2,
    # ### on a grid symmetric about zero. ### BOTH HALVES, IN THE OWNER'S OWN FILE.
    h.run('bump-is-even-through-t-squared',
          check=lambda: both(ATLAS, 't[m] ** 2', 'np.linspace(-L, L, NV)'),
          fixture=lambda: both(INSTR, 't[m] ** 2', 'np.linspace(-L, L, NV)'),
          witness=lambda: both(BANK, 't[m] ** 2', 'np.linspace(-L, L, NV)'))

    # 2 -- ### THE INSTRUMENT WRITES A CONVOLUTION AND NEVER A CORRELATION.
    # ### THIS IS THE FACT b229 RELIED ON WITHOUT CHECKING, AND IT IS THE ACT'S SHARPEST FIND.
    h.run('instrument-writes-convolve-not-correlate',
          check=lambda: (contains(INSTR, 'np.convolve(w, w, mode="full")')
                         and not contains(INSTR, 'np.correlate')),
          fixture=lambda: (contains(ATLAS, 'np.convolve(w, w, mode="full")')
                           and not contains(ATLAS, 'np.correlate')),
          witness=lambda: (contains(BANK, 'np.convolve(w, w, mode="full")')
                           and not contains(B229, 'np.correlate')))

    # 3 -- ### THE k-RANGE IS ONE-SIDED, which is the shape a fold produces.
    # ### THE FIRST FIXTURE HERE WAS `carto_atlas.py` AND THE HARNESS REFUSED THE CHECK,
    # ### because that file carries its OWN one-sided k-loop at lines 70/79 -- so the
    # ### fixture PASSED and could discriminate nothing. ### THAT IS b217's FIRST GUARD,
    # ### CATCHING THIS EXECUTOR FOR THE THIRD ACT RUNNING. ### The repair is a file that
    # ### genuinely has no k-loop at all. ### AND THE REFUSAL TAUGHT SOMETHING TRUE: THE
    # ### ONE-SIDED STAIRCASE OCCURS TWICE IN THE INSTRUMENT LAYER, NOT ONCE.
    h.run('k-range-is-one-sided',
          check=lambda: both(INSTR, 'k = 1', 'k += 1'),
          fixture=lambda: both(B230, 'k = 1', 'k += 1'),
          witness=lambda: both(BANK, 'k = 1', 'k += 1'))

    # 4 -- ### THE OWNER'S PAIR IS (ABSENT), AND THE SWEEP THAT SAYS SO IS SHOWN ABLE TO HIT.
    # ### THE FIXTURE IS THE CONTROL: it looks for a string that IS there, so a sweep that
    # ### returns zero for everything fails the fixture and the gate is REFUSED, not passed.
    h.run('owner-pair-absent-on-a-working-sweep',
          check=lambda: sweep(PAIR_RE) == 0 and contains(BANK, '(ABSENT)'),
          fixture=lambda: sweep(CONTROL_RE) == 0,
          witness=lambda: sweep(CONTROL_RE) > 0)

    # 5 -- ### THE SHADOW PROVED, NOT MERELY COMPILED: 404 lines, ZERO axiom-bearing.
    h.run('core-profile-is-zero-axiom-at-404',
          check=lambda: (count_lines(PRINTS) == 404
                         and count_sub(PRINTS, 'depends on axioms') == 0),
          fixture=lambda: count_sub(os.path.join(SGS, 'AXIOM_PRINTS_INTERFACES.txt'),
                                    'depends on axioms') == 0,
          witness=lambda: count_lines(PRINTS) == 404)

    # 6 -- ### THE PRINTS ARE REPRODUCIBLE FROM THE COMMITTED GENERATOR (b221's lesson).
    h.run('prints-reproducible-from-generator',
          check=lambda: count_sub(GEN, '#print axioms') == count_lines(PRINTS) == 404,
          fixture=lambda: count_sub(BANK, '#print axioms') == 404,
          witness=lambda: count_sub(GEN, '#print axioms') == 404)

    # 7 -- ### BOTH POLARITY CONTROLS ARE IN THE SHADOW. ### A file with only the positive
    # ### half would prove that convolution is ALWAYS even, which is FALSE.
    h.run('shadow-carries-both-polarity-controls',
          check=lambda: (contains(SHADOW, 'conv_not_even_witness')
                         and contains(SHADOW, 'fold_fails_for_fBad')),
          fixture=lambda: (contains(B229, 'conv_not_even_witness')
                           and contains(B229, 'fold_fails_for_fBad')),
          witness=lambda: (contains(PRINTS, 'conv_not_even_witness')
                           and contains(PRINTS, 'fold_fails_for_fBad')))

    # 8 -- ### THE CORRESPONDENCE ROW WAS WRITTEN BY THE TOOL AND SURVIVED.
    h.run('correspondence-row-carries-the-terminals',
          check=lambda: both(CORRMD, 'FoldedMirrorShadow', 'IMPORT-DEPENDENT'),
          fixture=lambda: both(PRINTS, 'FoldedMirrorShadow', 'IMPORT-DEPENDENT'),
          witness=lambda: contains(CORRMD, 'FoldedMirrorShadow'))

    # 9 -- ### THE VERDICT IS (PARTIAL) AND THE IMPORTS ARE LISTED. ### AN UNLISTED IMPORT
    # ### IS HOW (PARTIAL) BECOMES (DERIVED) WITHOUT ANYONE DECIDING TO DO IT.
    h.run('verdict-partial-with-imports-listed',
          check=lambda: both(BANK, '(PARTIAL)', 'IMPORT 1'),
          fixture=lambda: both(B230, '(PARTIAL)', 'IMPORT 1'),
          witness=lambda: contains(REG, '(PARTIAL)'))

    # 10 -- ### THE log p QUARRY IS UNTOUCHED: b10's grade travels with its quotation.
    h.run('log-p-quarry-carried-not-promoted',
          check=lambda: both(BANK, 'promotion either way', 'MATCH-IN-SHAPE'),
          fixture=lambda: both(B230, 'promotion either way', 'MATCH-IN-SHAPE'),
          witness=lambda: contains(REG, 'no promotion either way'))

    # 11 -- ### THE RUN'S OWN VERDICT LINE SAID `NO` AND IS CARRIED UNEDITED.
    # ### THE TEMPTATION WAS TO ADD A TOLERANCE UNTIL IT SAID YES. ### IT WAS NOT ADDED.
    h.run('refuting-run-carried-unedited',
          check=lambda: contains(RUN, 'EXACTLY (bit-for-bit): NO'),
          fixture=lambda: contains(BANK, 'EXACTLY (bit-for-bit): YES'),
          witness=lambda: contains(RUN, 'the test has content'))

    # 12 -- ### THE SEED IS FILED AND NOT OPENED; THE SIGN DOSSIER IS UNTOUCHED.
    h.run('seed-not-opened-and-sign-untouched',
          check=lambda: both(BANK, 'NOT OPENED', 'UNTOUCHED'),
          fixture=lambda: both(INSTR, 'NOT OPENED', 'UNTOUCHED'),
          witness=lambda: contains(BANK, 'NO SIGN IS CHOSEN'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
