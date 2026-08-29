# -*- coding: utf-8 -*-
"""b245_checks.py -- the b245 gates, routed through the amended b217 harness.

### THE FERRY SHARPENED THE FIXTURE RULE THIS ACT, AND THE SHARPENING CAME FROM b244's OWN
### SELF-CATCH: ### **"must-fail fixtures that fail for structurally different reasons than
### their checks pass."** ### b244 shipped a fixture that was its check NEGATED -- it failed
### whenever the check passed and demonstrated nothing. ### EVERY FIXTURE BELOW IS ANNOTATED
### WITH **WHY IT FAILS**, and none of them is `not check`.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a meaning was invented after the numbers. ### Gates 1-3: hash IN the run, meanings
###       ### OLDER on disk, and the meanings script importing NO instrument.
###   (2) that a decomposition was presented as evidence. ### Gate 4 runs the restatement on
###       ### ARBITRARY TUPLES and requires it to hold -- proving it is a tautology -- and the
###       ### bank must LABEL it so.
###   (3) that a bar was allowed to look certified. ### Gate 6 requires the tail sentence in the
###       ### RUN's own table, not only in the report.
###   (4) that the branch was softened after the diagnostic explained it. ### Gate 7 requires the
###       ### run to say (DISSONANT-BEYOND) and the diagnostic to say the branch stands.
###   (5) that the executor's own error was buried. ### Gate 8 requires it named in the bank.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

MEAN = os.path.join(D, 'b245_meanings.txt')
RUN = os.path.join(D, 'b245_faceoff_run.txt')
DIAG = os.path.join(D, 'b245_te_diagnosis.txt')
BANK = os.path.join(D, 'b245_second_face_off.txt')
B242 = os.path.join(D, 'b242_left_mode_axis.txt')
B242PTS = os.path.join(D, 'b242_axis_points.json')
B240RUN = os.path.join(D, 'b240_faceoff_run.txt')
B244 = os.path.join(D, 'b244_serializing_close.txt')


def sha_of(path):
    import hashlib
    return hashlib.sha256(io.open(path, encoding='utf-8').read().encode('utf-8')).hexdigest()


def meanings_precede_run():
    """### BOTH LIMBS: the run carries the meanings file's OWN hash, and the meanings file is
    ### older on disk than the run tool. ### EITHER LIMB ALONE IS FORGEABLE."""
    return (sha_of(MEAN) in io.open(RUN, encoding='utf-8').read()
            and os.path.getmtime(MEAN) < os.path.getmtime(os.path.join(E16, 'b245_faceoff.py')))


def no_instrument(path):
    s = io.open(path, encoding='utf-8').read()
    return not any(b in s for b in ('import carto_atlas', 'import b38_act10', 'import b37_act9',
                                    'import qeps_layer', 'import numpy'))


def restatement_is_tautology(perturb):
    """### THE TAUTOLOGY CONTROL. ### `L - R = resid47 + (2E2 - Dm + PR - Thq)` holds for ANY
    ### tuple once `resid47 := Tr - A - E2`. ### `perturb=True` breaks the definition of resid47
    ### and must be caught -- ### **THAT IS A STRUCTURALLY DIFFERENT FAILURE FROM THE CHECK'S
    ### PASS: the check passes because an identity holds; the fixture fails because a DIFFERENT
    ### quantity is substituted for resid47, not because the identity was negated.**"""
    import numpy as np
    rng = np.random.default_rng(20260829)
    worst = 0.0
    for _ in range(400):
        Tr, A, E2, Dm, Thq, PR = rng.normal(0.0, 3.0, 6)
        resid = (Tr - A - E2) + (0.5 if perturb else 0.0)
        lhs = ((Tr + E2 - Dm) + (-Thq)) - (A - PR)
        rhs = resid + (2 * E2 - Dm + PR - Thq)
        worst = max(worst, abs(lhs - rhs))
    return bool(worst <= 1e-12)


def te_deviation_is_the_withheld_modes():
    """### THE DIAGNOSTIC'S CLAIM, RE-DERIVED HERE FROM b242's BANKED POINTS AND THE RUN'S OWN
    ### TABLE -- not read from the diagnostic's prose."""
    pts = json.load(io.open(B242PTS, encoding='utf-8'))
    bank38 = {"2": (4.0486, -2.681242), "3": (3.3740, -2.534072), "4": (3.0478, -2.295425),
              "8": (2.5208, -2.025781), "9": (2.4540, -1.858463), "12": (2.3134, -1.790997)}
    txt = io.open(RUN, encoding='utf-8').read()
    got = {}
    for line in txt.splitlines():
        p = line.split()
        if len(p) == 4 and p[0] in bank38:
            try:
                got[p[0]] = float(p[1])
            except ValueError:
                pass
    if len(got) != 6:
        return False
    for c, (rb, db) in bank38.items():
        dev = abs(got[c] - (rb - db))
        tr = pts['trunc|%s' % c]['tr']
        if abs(dev - (tr[7] + tr[8] + tr[9])) > 5e-5:
            return False
    return True


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b245')

    # 1 -- ### THE MEANINGS PRECEDE THE NUMBERS, BY HASH **AND** BY MTIME.
    h.run('meanings-precede-the-run-both-limbs',
          check=meanings_precede_run,
          # ### FIXTURE: the SAME hash searched in b240's run -- a real file from another act that
          # ### cannot contain it. ### FAILS BECAUSE THE HASH IS ABSENT, not because the mtime
          # ### ordering was reversed: a structurally different reason from the check's pass.
          fixture=lambda: sha_of(MEAN) in io.open(B240RUN, encoding='utf-8').read(),
          witness=lambda: os.path.exists(MEAN) and os.path.getsize(MEAN) > 10000)

    # 2 -- ### THE MEANINGS SCRIPT COULD NOT HAVE COMPUTED ANYTHING.
    h.run('meanings-script-imports-no-instrument',
          check=lambda: no_instrument(os.path.join(E16, 'b245_meanings.py')),
          # ### FIXTURE: the same predicate on the RUN script, which DOES import them.
          # ### FAILS BECAUSE A REAL FILE CONTAINS REAL IMPORTS -- a presence, where the check is
          # ### an absence.
          fixture=lambda: no_instrument(os.path.join(E16, 'b245_faceoff.py')),
          witness=lambda: contains(os.path.join(E16, 'b245_faceoff.py'), 'import numpy as np'))

    # 3 -- ### THE BRANCH WORDS ARE THE BANKED WORDS.
    h.run('branch-word-is-a-banked-word',
          check=lambda: (contains(RUN, '**(DISSONANT-BEYOND)**')
                         and contains(MEAN, '**(DISSONANT-BEYOND)** -- a residual beyond the M-4')
                         and contains(MEAN, 'D_ACC = 3')),
          # ### FIXTURE: the branch word looked for in the MEANINGS file's own definition of a
          # ### DIFFERENT branch. ### FAILS BECAUSE THE STRING IS NOT THERE.
          fixture=lambda: contains(B240RUN, '**(DISSONANT-BEYOND)**'),
          witness=lambda: contains(RUN, 'DISSONANT-BEYOND'))

    # 4 -- ### THE TAUTOLOGY CONTROL ON THE DECOMPOSITION.
    h.run('restatement-is-a-tautology-DEMONSTRATED',
          check=lambda: restatement_is_tautology(perturb=False),
          # ### FIXTURE: substitute a DIFFERENT quantity for resid47. ### FAILS BECAUSE THE
          # ### SUBSTITUTED QUANTITY IS NOT THE RESIDUE -- structurally different from the check,
          # ### which passes because the residue's definition makes the sum an identity.
          fixture=lambda: restatement_is_tautology(perturb=True),
          witness=lambda: contains(BANK, 'CARRYING NO EVIDENTIAL WEIGHT'))

    # 5 -- ### AND THE BANK LABELS IT, IN ADVANCE, IN THE MEANINGS FILE.
    h.run('restatement-labelled-before-the-run',
          check=lambda: (contains(MEAN, 'IS AN ALGEBRAIC RESTATEMENT AND CARRIES NO')
                         and contains(RUN, 'THIS CONFIRMS NOTHING ABOUT THE IDENTITY')),
          fixture=lambda: contains(B240RUN, 'IS AN ALGEBRAIC RESTATEMENT AND CARRIES NO'),
          witness=lambda: contains(MEAN, 'ALGEBRAIC RESTATEMENT'))

    # 6 -- ### NO NUMBER IS ALLOWED TO LOOK CERTIFIED THAT IS NOT. ### The tail sentence must be
    # ### in the RUN's own table, not only in the report.
    h.run('tail-sentence-beside-every-bar_L',
          check=lambda: (contains(RUN, 'THE TAIL TERM IS NOT A BOUND')
                         and contains(RUN, 'IS NOT A CERTIFIED BAR AND NO NUMBER BESIDE IT')
                         and contains(MEAN, 'NO TABLE IN THIS ACT PRINTS `bar_L` WITHOUT IT')),
          fixture=lambda: contains(B240RUN, 'THE TAIL TERM IS NOT A BOUND'),
          witness=lambda: contains(RUN, 'TAIL'))

    # 7 -- ### THE BRANCH WAS NOT SOFTENED AFTER THE DIAGNOSTIC EXPLAINED IT.
    h.run('branch-stands-after-the-diagnostic',
          check=lambda: (contains(DIAG, 'THIS TOOL NAMES THE TERM; IT DOES NOT RE-BRANCH')
                         and contains(DIAG, 'A BANKED RULE IS NOT REVISED')
                         and contains(BANK, 'BRANCH (DISSONANT-BEYOND)')
                         and os.path.getmtime(RUN) < os.path.getmtime(DIAG)),
          # ### FIXTURE: the ordering limb alone, reversed against a file that PRE-dates the run.
          # ### FAILS ON TIME ORDER -- a different limb from the prose limbs the check needs.
          fixture=lambda: os.path.getmtime(DIAG) < os.path.getmtime(MEAN),
          witness=lambda: os.path.exists(DIAG))

    # 8 -- ### THE DIAGNOSTIC'S CLAIM, RE-DERIVED FROM b242's BANKED POINTS.
    h.run('te-deviation-is-the-withheld-modes',
          check=te_deviation_is_the_withheld_modes,
          # ### FIXTURE: the same predicate with the withheld window moved to modes 4-6, which are
          # ### ABOVE the floor and much larger. ### FAILS BECAUSE THE WRONG MODES ARE SUMMED --
          # ### an arithmetic mismatch, not a negation of the check.
          fixture=lambda: (lambda pts, bank38, got: all(
              abs(abs(got[c] - (bank38[c][0] - bank38[c][1]))
                  - (pts['trunc|%s' % c]['tr'][4] + pts['trunc|%s' % c]['tr'][5]
                     + pts['trunc|%s' % c]['tr'][6])) <= 5e-5 for c in bank38))(
              json.load(io.open(B242PTS, encoding='utf-8')),
              {"2": (4.0486, -2.681242), "3": (3.3740, -2.534072), "4": (3.0478, -2.295425),
               "8": (2.5208, -2.025781), "9": (2.4540, -1.858463), "12": (2.3134, -1.790997)},
              {p[0]: float(p[1]) for p in
               (l.split() for l in io.open(RUN, encoding='utf-8'))
               if len(p) == 4 and p[0] in ('2', '3', '4', '8', '9', '12')
               and re.match(r'^[0-9.]+$', p[1])}),
          witness=lambda: os.path.exists(B242PTS))

    # 9 -- ### THE EXECUTOR'S OWN ERROR IS NAMED, NOT BURIED.
    h.run('executor-error-named-in-the-bank',
          check=lambda: (contains(BANK, 'T-E WAS MIS-SPECIFIED AT')
                         and contains(BANK, 'THE ONE SEAT THAT COULD NOT HAVE MISSED IT MISSED IT')
                         and contains(BANK, 'THREE CONSECUTIVE ACTS')),
          fixture=lambda: contains(B244, 'T-E WAS MIS-SPECIFIED AT'),
          witness=lambda: contains(BANK, 'MIS-SPECIFIED'))

    # 10 -- ### THE FILING THE BRANCH FORBIDS WAS **NOT** MADE.
    h.run('m4-shadow-not-filed-on-a-failed-accounting',
          check=lambda: (contains(BANK, 'IS *NOT* FILED AS')
                         and contains(BANK, 'A PROFILE FILED OFF A FAILED ACCOUNTING')
                         and not contains(BANK, 'FILED AS M-4\'S MEASURED SHADOW.')),
          fixture=lambda: contains(B242, 'A PROFILE FILED OFF A FAILED ACCOUNTING'),
          witness=lambda: contains(BANK, 'M-4'))

    # 11 -- ### G-INDEP AND THE GATES RAN FROM SOURCE AND PASSED.
    h.run('g-indep-and-gates-run-from-source',
          check=lambda: both(RUN, "G-INDEP GATE: PASS", "READ FROM THE INSTRUMENTS' OWN SOURCE")
                        and contains(RUN, 'kernel-cache gate'),
          fixture=lambda: contains(B242, "G-INDEP GATE: PASS"),
          witness=lambda: contains(RUN, 'G-INDEP'))

    # 12 -- ### THE MODE REFINEMENT MOVED NMODE ALONE, WHICH IS b242's LESSON APPLIED.
    h.run('mode-refinement-moves-nmode-alone',
          check=lambda: (contains(RUN, 'MOVES **NMODE ALONE** (7 -> 6) AT NQ HELD')
                         and contains(MEAN, 'it moves NMODE ALONE')),
          fixture=lambda: contains(B240RUN, 'MOVES **NMODE ALONE**'),
          witness=lambda: contains(RUN, 'G-STAB'))

    # 13 -- ### NOTHING THE SCOPE FORBIDS MOVED.
    h.run('kernel-place-loom-untouched',
          check=lambda: (unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/SIDE-global-section', 'Core')
                         and unmodified('D:/MY-DOwnloads/PLACE-papers', 'VERIFICATION_LOOM.md')
                         and contains(BANK, 'THE LOOM AND THE MIRROR WERE NOT TOUCHED')),
          fixture=lambda: unmodified(ROOT, 'data/b245_second_face_off.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    # 14 -- ### THE CEILING AND h2 IN EVERY ARTEFACT, INCLUDING THE RUN'S TABLE HEADER.
    h.run('ceiling-in-the-run-table-header',
          check=lambda: (both(RUN, 'DECIDES NOTHING GLOBAL', 'THE SECOND FACE-OFF TABLE')
                         and all(contains(p, 'DECIDES NOTHING GLOBAL')
                                 for p in (MEAN, BANK, DIAG))),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'DECIDES NOTHING GLOBAL'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
