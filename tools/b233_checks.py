# -*- coding: utf-8 -*-
"""b233_checks.py -- the b233 gates, routed through the b217 harness.

### THIS ACT'S RISKS ARE THREE:
###   (1) that the ARRANGEMENT gets settled on a number. ### The narrative supplies one --
###       "the dictated direction also fails numerically in BOTH conventions" -- and using it
###       would pick the branch that makes an assembly close, which is b229's named crime.
###   (2) that the BENCH gets tuned until it agrees. ### N was registered at 1000 BEFORE the
###       first number; every other N is a varied axis and is reported as one.
###   (3) that an ABSENCE is filed on a search that could not have found anything.
### ### EVERY ABSENCE BELOW CARRIES A POSITIVE CONTROL, per the EXECUTION line.

### THE `contains()` HELPER IS THE b232-REPAIRED ONE: both sides decoded and lowercased as
### TEXT. ### The inherited version lowercased the haystack as BYTES and the needle as a
### STRING, so any non-ASCII quotation could never match -- latent across three acts.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
METHOD = os.path.join(PLACE, 'phase2', 'method')
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

BANK = os.path.join(D, 'b233_the_arrangement.txt')
REG = os.path.join(D, 'b233_registration_2026-08-28.txt')
RUN = os.path.join(D, 'b233_imp1_bench_run.txt')
B231 = os.path.join(D, 'b231_the_two.txt')
B232 = os.path.join(D, 'b232_sign_of_A.txt')

CHAIN = os.path.join(METHOD, 'THE_IDENTITY_CHAIN.md')
SIGNARR = os.path.join(METHOD, 'SIGN_ARRANGEMENT_RECONCILIATION.md')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
ATLAS = os.path.join(E16, 'carto_atlas.py')
B38 = os.path.join(E16, 'b38_act10.py')
BENCH = os.path.join(E16, 'b233_imp1_bench.py')
NARR = os.path.join(ROOT, 'reports',
                    '2026-08-18-global-section-acts-narrative-v0.15.md')


def contains(path, needle):
    """### THE b232-REPAIRED HELPER: both sides as TEXT, not bytes-vs-string."""
    if not os.path.isfile(path):
        return False
    with io.open(path, encoding='utf-8', errors='replace') as fh:
        return needle.lower() in fh.read().lower()


def both(path, a, b):
    return contains(path, a) and contains(path, b)


def count_sub(path, needle):
    if not os.path.isfile(path):
        return -1
    with io.open(path, encoding='utf-8', errors='replace') as fh:
        return len(re.findall(re.escape(needle), fh.read(), re.I))


def file_unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b233')

    # 1 -- ### FILE E's THREE TEXTS ARE QUOTED, INCLUDING THE OPERATOR AS WRITTEN.
    h.run('file-E-texts-quoted-with-operator',
          check=lambda: both(BANK, 'T.value + Q.value = W.wInf - W.wPrimes', 'CC convention'),
          fixture=lambda: both(ATLAS, 'T.value + Q.value = W.wInf - W.wPrimes', 'CC convention'),
          witness=lambda: both(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes', 'CC convention'))

    # 2 -- ### BRANCH (iii): NO ARRANGEMENT IS CHOSEN AND THE STATEMENT IS MARKED.
    h.run('arrangement-routed-none-chosen',
          check=lambda: both(BANK, 'NO ARRANGEMENT CHOSEN', 'ONE-RULING-FROM-COMPLETE'),
          fixture=lambda: both(B232, 'NO ARRANGEMENT CHOSEN', 'ONE-RULING-FROM-COMPLETE'),
          witness=lambda: contains(REG, 'ONE-RULING-FROM-COMPLETE'))

    # 3 -- ### THE NUMERICAL HALF OF THE NARRATIVE'S SENTENCE IS NAMED **AS INADMISSIBLE**.
    # ### THE CORPUS OFFERS A NUMBER THAT WOULD DECIDE THE BRANCH; THE GATE CHECKS IT WAS REFUSED.
    h.run('numerical-evidence-named-inadmissible',
          # ### THE FIRST WITNESS ASKED THE NARRATIVE FOR THE WHOLE PHRASE AND THE HARNESS
          # ### REFUSED THE CHECK: the source carries it LINE-WRAPPED ("fails numerically" /
          # ### "in BOTH conventions"), so the exact substring is absent THERE though present
          # ### in the bank's own quotation. ### b227's SPECIES, THIRD ACT RUNNING -- and the
          # ### needle is now the longest fragment that survives the wrap at the SOURCE.
          check=lambda: both(BANK, 'fails numerically', 'INADMISSIBLE'),
          fixture=lambda: both(NARR, 'fails numerically', 'INADMISSIBLE'),
          witness=lambda: contains(NARR, 'fails numerically'))

    # 4 -- ### THE (i)-ABSENCE CARRIES ITS POSITIVE CONTROL IN THE SAME BREATH.
    h.run('intent-absence-with-positive-control',
          check=lambda: both(BANK, '(ABSENT)', 'POSITIVE CONTROL ON THAT ABSENCE'),
          fixture=lambda: both(FILE_E, '(ABSENT)', 'POSITIVE CONTROL ON THAT ABSENCE'),
          witness=lambda: contains(BANK, 'POSITIVE CONTROL ON THAT ABSENCE'))

    # 5 -- ### THE b232 QUALIFICATION IS FILED WITH THE DOCSTRING'S OWN BRACKET.
    h.run('b232-qualification-with-the-bracket',
          check=lambda: both(BANK, 'sign fixed BY the E2 calibration', 'committed before any answer'),
          fixture=lambda: both(SIGNARR, 'sign fixed BY the E2 calibration',
                               'committed before any answer'),
          witness=lambda: contains(ATLAS, 'sign fixed BY the E2 calibration'))

    # 6 -- ### THE BENCH USED b38 UNMODIFIED AND mpmath ZEROS, NOT THE BANKED ORDINATES.
    h.run('bench-imports-b38-and-computes-zeros',
          check=lambda: (contains(BENCH, 'B38.left_side') and contains(BENCH, 'zetazero')),
          fixture=lambda: (contains(B38, 'B38.left_side') and contains(B38, 'zetazero')),
          witness=lambda: contains(RUN, 'mpmath.zetazero'))

    # 7 -- ### THE ZEROS CONTROL RAN AND PASSED: fresh vs banked ordinates.
    # ### WITHOUT THIS, EVERY NUMBER BELOW IS UNGROUNDED.
    h.run('zeros-control-fresh-vs-banked',
          check=lambda: contains(RUN, 'CONTROL PASSES'),
          fixture=lambda: contains(B232, 'CONTROL PASSES'),
          witness=lambda: contains(RUN, 'CONTROL vs banked'))

    # 8 -- ### THE REGISTERED TRUNCATION WAS FIXED BEFORE THE FIRST NUMBER, AND SAYS SO.
    h.run('truncation-registered-in-advance',
          check=lambda: (contains(REG, 'N registered in advance at 1000')
                         and contains(RUN, 'N REGISTERED AT 1000')),
          fixture=lambda: contains(B231, 'N registered in advance at 1000'),
          witness=lambda: contains(REG, 'N registered in advance at 1000'))

    # 9 -- ### THE TAIL BOUND IS QUOTED, NOT ASSUMED, AND THE VERDICT IS KEYED TO IT.
    h.run('tail-bound-quoted-and-binding',
          check=lambda: both(RUN, 'tail bound', 'THE TRUNCATION TAIL, NOT THE'),
          fixture=lambda: both(B232, 'tail bound', 'THE TRUNCATION TAIL, NOT THE'),
          witness=lambda: contains(BENCH, 'BOUNDED AND QUOTED'))

    # 10 -- ### AXES VARIED AND REPORTED (the floor-axis law), NOT TUNED.
    h.run('axes-varied-and-reported',
          check=lambda: count_sub(RUN, 'AXIS ') >= 5,
          fixture=lambda: count_sub(B232, 'AXIS ') >= 5,
          witness=lambda: contains(RUN, 'NO AXIS WAS TUNED'))

    # 11 -- ### THE CORPUS'S LEFT SIDE APPEARS NOWHERE IN THE BENCH.
    h.run('left-side-absent-from-the-bench',
          check=lambda: (contains(BENCH, 'LEFT SIDE (T, Q) APPEARS NOWHERE')
                         and not contains(BENCH, 'QuotientTrace')
                         and not contains(BENCH, 'ArchimedeanE1Trace')),
          fixture=lambda: (contains(FILE_E, 'LEFT SIDE (T, Q) APPEARS NOWHERE')
                           and not contains(FILE_E, 'QuotientTrace')),
          witness=lambda: contains(RUN, 'LEFT SIDE (T, Q) APPEARS NOWHERE'))

    # 12 -- ### THE DIAGONAL a^2 SPECIES IS SAID AT EVERY USE (b221's divergence).
    h.run('diagonal-a2-species-said-at-every-use',
          check=lambda: both(BANK, 'DIAGONAL a', 'diagonal a'),
          fixture=lambda: contains(ATLAS, 'DIAGONAL a'),
          witness=lambda: contains(RUN, 'DIAGONAL a^2 CELLS'))

    # 13 -- ### THE LEDGER GAINED ITS VERIFICATION COLUMN AND BOTH IMPORTS ARE GRADED.
    h.run('import-ledger-has-verification-column',
          check=lambda: (contains(CHAIN, 'VERIFIED-AT-BENCH')
                         and contains(CHAIN, 'TRUSTED-AT-CITE')),
          fixture=lambda: (contains(SIGNARR, 'VERIFIED-AT-BENCH')
                           and contains(SIGNARR, 'TRUSTED-AT-CITE')),
          witness=lambda: (contains(BANK, 'VERIFIED-AT-BENCH')
                           and contains(BANK, 'TRUSTED-AT-CITE')))

    # 14 -- ### FILE E IS QUOTED, NOT EDITED. ### THE WHOLE ACT TURNS ON NOT AMENDING IT.
    h.run('file-E-unedited-by-this-act',
          check=lambda: file_unmodified(SGS, 'Interfaces/FiniteInstanceIdentity.lean'),
          fixture=lambda: file_unmodified(PLACE, 'phase2/method/THE_IDENTITY_CHAIN.md'),
          witness=lambda: file_unmodified(SGS, 'Core/FoldedMirrorShadow.lean'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
