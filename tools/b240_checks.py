# -*- coding: utf-8 -*-
"""b240_checks.py -- the b240 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a bar was chosen to fit a residual. ### TESTED BY HASH AND BY MTIME: the
###       ### meanings file's sha256 appears inside the run's own output, and the meanings
###       ### file is OLDER than the run file on disk.
###   (2) that a meaning was invented after the numbers. ### The verdict's words must be the
###       ### banked words, and the gate matches them against the MEANINGS FILE, not the bank.
###   (3) that a diagnostic variant was quietly promoted to primary. ### The diagnostics file
###       ### must say it promoted none, and the primary reading must be the ruling's C2.
###   (4) that the ceiling was dropped once a branch existed. ### b14/b15 must appear in the
###       ### run's own table header, not only in the report.
###   (5) that the executor's registered expectation was quietly edited to match the outcome.
###       ### The gate checks the expectation is in the meanings file AND that the act reports
###       ### the half of it that was WRONG.
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')

MEAN = os.path.join(D, 'b240_meanings.txt')
RUN = os.path.join(D, 'b240_faceoff_run.txt')
DIAG = os.path.join(D, 'b240_diagnostics.txt')
BANK = os.path.join(D, 'b240_first_face_off.txt')
REG = os.path.join(D, 'b240_registration_2026-08-28.txt')
B238 = os.path.join(D, 'b238_imp1_budget.txt')
B239 = os.path.join(D, 'b239_ruling_executed.txt')


def sha_of(path):
    import hashlib
    return hashlib.sha256(io.open(path, encoding='utf-8').read().encode('utf-8')).hexdigest()


def meanings_precede_run():
    """### THE ORDER-OF-OPERATIONS GATE, BOTH LIMBS: the run carries the meanings file's OWN
    ### hash, and the meanings file is older on disk. ### EITHER LIMB ALONE IS FORGEABLE."""
    if not (os.path.exists(MEAN) and os.path.exists(RUN)):
        return False
    return (sha_of(MEAN) in io.open(RUN, encoding='utf-8').read()
            and os.path.getmtime(MEAN) < os.path.getmtime(RUN))


def diagnostics_follow_branch():
    """### AND THE SECOND ORDERING: the diagnostics are younger than the run."""
    if not (os.path.exists(RUN) and os.path.exists(DIAG)):
        return False
    return os.path.getmtime(RUN) < os.path.getmtime(DIAG)


def no_instrument_in_meanings():
    """### THE MEANINGS SCRIPT IMPORTS NO INSTRUMENT. ### A meanings file that could compute is
    ### a meanings file that might have."""
    src = io.open(os.path.join(ROOT, 'tools', 'e16', 'b240_meanings.py'),
                  encoding='utf-8').read()
    bad = ('import carto_atlas', 'import b38_act10', 'import b37_act9', 'import qeps_layer',
           'import numpy')
    return not any(b in src for b in bad)


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b240')

    # 1 -- ### THE MEANINGS PRECEDE THE NUMBERS, BY HASH **AND** BY MTIME.
    h.run('meanings-precede-the-run',
          check=meanings_precede_run,
          fixture=lambda: sha_of(MEAN) in io.open(B238, encoding='utf-8').read(),
          witness=lambda: os.path.exists(MEAN) and os.path.getsize(MEAN) > 4000)

    # 2 -- ### THE DIAGNOSTICS FOLLOW THE BRANCH, and the tool itself refuses otherwise.
    h.run('diagnostics-follow-the-branch',
          check=lambda: (diagnostics_follow_branch()
                         and contains(os.path.join(ROOT, 'tools', 'e16', 'b240_diagnostics.py'),
                                      'REFUSING: diagnostics never precede the branch')),
          fixture=lambda: os.path.getmtime(DIAG) < os.path.getmtime(MEAN),
          witness=lambda: os.path.exists(DIAG))

    # 3 -- ### THE MEANINGS SCRIPT COULD NOT HAVE COMPUTED ANYTHING.
    h.run('meanings-script-imports-no-instrument',
          check=no_instrument_in_meanings,
          # ### THE FIXTURE IS THE SAME TEST APPLIED TO THE RUN SCRIPT, WHICH DOES IMPORT THE
          # ### INSTRUMENTS -- so the test is shown able to FAIL, on a real file, this run.
          fixture=lambda: not any(
              b in io.open(os.path.join(ROOT, 'tools', 'e16', 'b240_faceoff.py'),
                           encoding='utf-8').read()
              for b in ('import carto_atlas', 'import b38_act10', 'import numpy')),
          witness=lambda: contains(os.path.join(ROOT, 'tools', 'e16', 'b240_faceoff.py'),
                                   'import numpy as np'))

    # 4 -- ### THE FOUR BRANCH MEANINGS ARE IN THE MEANINGS FILE, IN THE FERRY'S OWN WORDS.
    h.run('four-branch-meanings-banked-first',
          check=lambda: all(contains(MEAN, s) for s in
                            ('(CONSONANT)', '(DISSONANT)', '(INDETERMINATE)', '(HALT)',
                             'MEASURED-NOT-CERTIFIED')),
          fixture=lambda: all(contains(B239, s) for s in
                              ('(CONSONANT)', '(DISSONANT)', '(INDETERMINATE)', '(HALT)')),
          witness=lambda: contains(MEAN, '(DISSONANT)'))

    # 5 -- ### THE INDICTMENT ORDER IS BANKED IN ADVANCE, FOUR SUSPECTS, FORM LAST.
    h.run('indictment-order-banked-form-last',
          check=lambda: all(contains(MEAN, s) for s in
                            ('SUSPECT 1 -- THE UNCERTIFIED ENVELOPE',
                             'THE THREE-NORMALIZATIONS SPECIES',
                             'SUSPECT 3 -- THE ASSEMBLY CONVENTIONS',
                             'SUSPECT 4, AND ONLY LAST',
                             'never which is GUILTY')),
          fixture=lambda: contains(B239, 'SUSPECT 4, AND ONLY LAST'),
          witness=lambda: contains(MEAN, 'SUSPECT 4, AND ONLY LAST'))

    # 6 -- ### THE CEILING IS IN THE RUN'S OWN TABLE HEADER, not only in the report.
    h.run('ceiling-printed-in-the-table-header',
          check=lambda: both(RUN, 'FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING',
                             'THE FACE-OFF TABLE'),
          fixture=lambda: contains(B238, 'THE FACE-OFF TABLE'),
          witness=lambda: contains(RUN, 'THE FACE-OFF TABLE'))

    # 7 -- ### THE VERDICT USES THE BANKED WORD, AND THE WORD IS IN THE MEANINGS FILE.
    h.run('verdict-word-is-a-banked-word',
          check=lambda: (contains(RUN, "THE ACT'S BRANCH, BY THE RULE BANKED BEFORE THE RUN: (DISSONANT)")
                         and contains(MEAN, '### (DISSONANT) -- a residual beyond the combined bar')),
          fixture=lambda: contains(B239, "THE ACT'S BRANCH, BY THE RULE BANKED BEFORE THE RUN"),
          witness=lambda: contains(RUN, '(DISSONANT)'))

    # 8 -- ### G-INDEP WAS RUN FROM SOURCE, NOT ASSERTED, AND IT PASSED.
    h.run('g-indep-run-from-source',
          check=lambda: both(RUN, "G-INDEP GATE: PASS", "READ FROM THE INSTRUMENTS' OWN SOURCE"),
          fixture=lambda: contains(B238, "G-INDEP GATE: PASS"),
          witness=lambda: contains(RUN, 'G-INDEP GATE'))

    # 9 -- ### G-STAB: BOTH SIDES AT A REGISTERED REFINEMENT, SPREADS QUOTED.
    h.run('g-stab-both-sides-spreads-quoted',
          check=lambda: all(contains(RUN, s) for s in
                            ('G-STAB.', '|dL| (NV)', '|dL| (mode)', '|dR| (NV)', 'bar_L', 'bar_R')),
          fixture=lambda: contains(B239, '|dL| (mode)'),
          witness=lambda: contains(RUN, 'G-STAB.'))

    # 10 -- ### NO VARIANT WAS PROMOTED TO PRIMARY, AND THE PRIMARY IS THE RULING'S C2.
    h.run('primary-is-C2-no-variant-promoted',
          check=lambda: (contains(RUN, 'L := T.value + Q.value := (Tr_full + E2 + Delta_-) + Theta_q')
                         and contains(DIAG, 'did not promote a')
                         and contains(DIAG, 'NONE OF THEM IS PROMOTED TO PRIMARY')),
          fixture=lambda: contains(B239, 'NONE OF THEM IS PROMOTED TO PRIMARY'),
          witness=lambda: contains(DIAG, 'NONE OF THEM IS PROMOTED TO PRIMARY'))

    # 11 -- ### THE EXPECTATION WAS REGISTERED **AND** THE HALF THAT WAS WRONG IS REPORTED.
    # ### An expectation that only ever turns out right is an expectation written late.
    h.run('expectation-registered-and-its-error-reported',
          check=lambda: (contains(MEAN, "SUSPECT 2's FIRST LIMB")
                         and contains(DIAG, 'ACCOUNTS FOR ONLY')
                         and contains(BANK, 'THE EXECUTOR WAS PARTLY WRONG')),
          fixture=lambda: contains(B239, 'THE EXECUTOR WAS PARTLY WRONG'),
          witness=lambda: contains(MEAN, "SUSPECT 2's FIRST LIMB"))

    # 12 -- ### THE CLOSEST CELL'S MARGIN IS REPORTED, NOT SMOOTHED. a^2=2 clears D=10 by 8%.
    h.run('closest-cell-margin-reported',
          check=lambda: both(BANK, '10.85', 'HAD THE FACTOR BEEN 12'),
          fixture=lambda: contains(B238, 'HAD THE FACTOR BEEN 12'),
          witness=lambda: contains(BANK, '10.85'))

    # 13 -- ### THE LEFT SIDE'S OWN LIMIT IS NAMED: its bar is SIX ORDERS above the right's, and
    # ### its mode-axis spread is estimated from ONE step of a possibly slow series.
    h.run('left-side-mode-axis-limit-named',
          check=lambda: both(BANK, 'W-ORD-LEFT-MODE-AXIS',
                             'ONE STEP OF A SERIES WHOSE TAIL IS NOT BOUNDED'),
          fixture=lambda: contains(B238, 'W-ORD-LEFT-MODE-AXIS'),
          witness=lambda: contains(BANK, 'W-ORD-LEFT-MODE-AXIS'))

    # 14 -- ### NOTHING MOVED THAT THE SCOPE FORBIDS: no grade, no kernel, no deposit.
    h.run('no-grade-no-kernel-moved',
          check=lambda: (unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/SIDE-global-section', 'Core')
                         and unmodified('D:/SIDE-global-section', 'CORRESPONDENCE.md')
                         and contains(BANK, 'NO GRADE MOVED')),
          # ### THE FIXTURE: a path this act DID write must read as modified, or `unmodified`
          # ### is answering yes to everything and gate 14 proves nothing.
          fixture=lambda: unmodified('D:/relay', 'data/b240_faceoff_run.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    # 15 -- ### h2 AND THE REGISTER SENTENCE ARE UNTOUCHED, SAID IN THE ACT'S OWN WORDS.
    h.run('h2-untouched-said-plainly',
          check=lambda: (contains(BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT')
                         and contains(RUN, 'h2')
                         and contains(MEAN, 'NO BRANCH OF THIS ACT MAY DO')),
          fixture=lambda: contains(B238, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
          witness=lambda: contains(MEAN, 'h2'))

    for row in h.rows:
        print('  %-46s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
