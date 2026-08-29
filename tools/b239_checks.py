# -*- coding: utf-8 -*-
"""b239_checks.py -- the b239 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS:
###   (1) that the amendment moves CODE under cover of a docstring. ### Tested EXACTLY:
###       ### strip every comment and docstring and compare to the HEAD blob.
###   (2) that a compile is reported as a verification. ### b227 and b231 each shipped a file
###       ### that compiled clean and printed wrong. ### THE GATE READS THE PROFILE.
###   (3) that the ruling is executed WITHOUT its rider and its debt -- a definition taken and
###       its cost dropped. ### Both must appear, and the debt in the CORRESPONDENCE ROW.
###   (4) ### THAT A FACE-OFF IS RUN. With T.value defined and A - PR adopted, ONE instrument
###       ### call would produce both sides. ### b240 owns that, under its own registration.
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b239_ruling_executed.txt')
REG = os.path.join(D, 'b239_registration_2026-08-28.txt')
RP = os.path.join(D, 'b239_reprint_run.txt')
B237 = os.path.join(D, 'b237_left_side_assets.txt')
B238 = os.path.join(D, 'b238_imp1_budget.txt')

FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
CORR = os.path.join(SGS, 'CORRESPONDENCE.md')
COREPRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')


def _strip(src):
    out, i, depth = [], 0, 0
    while i < len(src):
        if src.startswith('/-', i):
            depth += 1
            i += 2
        elif src.startswith('-/', i) and depth:
            depth -= 1
            i += 2
        elif depth:
            i += 1
        else:
            out.append(src[i])
            i += 1
    keep = []
    for line in ''.join(out).splitlines():
        j = line.find('--')
        if j >= 0:
            line = line[:j]
        if line.strip():
            keep.append(' '.join(line.split()))
    return chr(10).join(keep)


def code_identical(repo, relpath):
    """### THE EXACT TEST: strip every comment and docstring from the HEAD blob and from the
    ### working file and compare what is left. ### A DOCSTRING EDIT MUST MOVE NO CODE."""
    try:
        r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + relpath], capture_output=True)
    except Exception:
        return False
    if r.returncode != 0:
        return False
    head = r.stdout.decode('utf-8', 'replace')
    work = io.open(os.path.join(repo, relpath), encoding='utf-8', errors='replace').read()
    return _strip(head) == _strip(work)


def unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def no_new_bench_run():
    """### NO FACE-OFF WAS RUN: no b239 run-file under data/ other than the re-print."""
    runs = [f for f in os.listdir(D) if f.startswith('b239') and f.endswith('_run.txt')]
    return runs == ['b239_reprint_run.txt']


def main():
    h = Harness(ROOT, 'b239')

    # 1 -- ### THE AMENDMENT MOVED NO CODE. ### Exact, not by eye.
    h.run('amendment-moved-no-code',
          check=lambda: (code_identical(SGS, 'Interfaces/FiniteInstanceIdentity.lean')
                         and contains(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes')),
          fixture=lambda: not code_identical(SGS, 'Interfaces/FiniteInstanceIdentity.lean'),
          witness=lambda: contains(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes'))

    # 2 -- ### THE DEFINITION, THE RIDER AND THE ORIGINAL ARE ALL IN THE FILE.
    # ### A DEFINITION TAKEN WITHOUT ITS COST WOULD PASS A LOOSER GATE THAN THIS.
    h.run('definition-rider-and-original-in-file',
          check=lambda: all(contains(FILE_E, s) for s in
                            ('value := Tr_full + E2 + Δ₋',
                             'PER-CELL AT BENCH, STANDING UNTIL M-4 CLOSES',
                             'THE ORIGINAL DOCSTRING READ, IN FULL')),
          fixture=lambda: all(contains(B237, s) for s in
                              ('value := Tr_full + E2 + Δ₋',
                               'PER-CELL AT BENCH, STANDING UNTIL M-4 CLOSES',
                               'THE ORIGINAL DOCSTRING READ, IN FULL')),
          witness=lambda: contains(FILE_E, 'value := Tr_full + E2 + Δ₋'))

    # 3 -- ### THE DEBT IS IN THE CORRESPONDENCE ROW, where the next reader meets it --
    # ### not only in a bank the executor wrote.
    h.run('debt-named-in-correspondence-row',
          check=lambda: contains(CORR,
                                 'DEFINED-BY-RULING (C2), REALIZED PER-CELL AT BENCH, '
                                 'OPEN DEBT M-4'),
          fixture=lambda: contains(BANK,
                                   'no cell of the correspondence row names the debt'),
          witness=lambda: contains(CORR, 'OPEN DEBT M-4'))

    # 4 -- ### THE RE-PRINT MATCHED EVERY TERMINAL, AND THE COUNTS AGREE.
    h.run('reprint-29-of-29-matched',
          check=lambda: (contains(RP, 'terminals printed : 29')
                         and contains(RP, 'matched to bank : 29')
                         and contains(RP, 'differing         : 0')),
          fixture=lambda: contains(B238, 'matched to bank : 29'),
          witness=lambda: contains(RP, 'matched to bank : 29'))

    # 5 -- ### BOTH PINS WERE USED, because the bank itself records two toolchains.
    # ### ONE PIN FOR BOTH WOULD CALL A TOOLCHAIN DIFFERENCE A FINDING.
    h.run('reprint-used-both-declared-pins',
          check=lambda: both(RP, 'v4.30.0-rc1', 'v4.29.0'),
          fixture=lambda: both(B238, 'v4.30.0-rc1', 'v4.29.0'),
          witness=lambda: contains(RP, 'v4.30.0-rc1'))

    # 6 -- ### FILE E's OWN PROFILE IS UNCHANGED ACROSS TWO AMENDMENTS, AND IT WAS PRINTED.
    h.run('file-E-profile-printed-and-unchanged',
          check=lambda: (contains(RP, 'FiniteInstanceIdentity.finiteInstanceIdentity')
                         and contains(RP, 'MATCH')
                         and contains(BANK, 'IT RAN THE PRINT')),
          fixture=lambda: contains(B237, 'IT RAN THE PRINT'),
          witness=lambda: contains(RP, 'FiniteInstanceIdentity.finiteInstanceIdentity'))

    # 7 -- ### CORE WAS NOT RE-RUN, AND THE ACT SAYS SO rather than letting a reader assume
    # ### the whole layer was re-verified.
    h.run('core-not-rerun-and-said-so',
          check=lambda: (unmodified(SGS, 'AXIOM_PRINTS.txt')
                         and unmodified(SGS, 'Core')
                         and contains(RP, 'CORE WAS NOT TOUCHED BY THIS ACT')),
          fixture=lambda: not unmodified(SGS, 'Core'),
          witness=lambda: unmodified(SGS, 'AXIOM_PRINTS.txt'))

    # 8 -- ### NO FACE-OFF WAS RUN. ### The largest temptation this arc has carried.
    h.run('no-faceoff-run-no-number-crossed',
          check=lambda: no_new_bench_run() and contains(BANK, 'NO FACE-OFF WAS RUN'),
          fixture=lambda: not no_new_bench_run(),
          witness=lambda: contains(REG, 'NO FACE-OFF. NO NUMBER CROSSING BETWEEN'))

    # 9 -- ### THE IDIOM WAS CHOSEN **AND SHOWN**, with the refused alternative named.
    h.run('idiom-chosen-and-shown-with-reason',
          check=lambda: both(BANK, 'DOCUMENTED BINDING',
                             'REALIZATION INVENTED'),
          fixture=lambda: both(B238, 'DOCUMENTED BINDING', 'REALIZATION INVENTED'),
          witness=lambda: contains(REG, 'DOCUMENTED-BINDING'))

    # 10 -- ### THE CHECKLIST IS FINAL AND THE AMBER IS NAMED, not smoothed to green.
    h.run('checklist-final-amber-named',
          check=lambda: both(BANK, 'THREE GREEN AND ONE AMBER', 'MEASURED, NOT CERTIFIED'),
          fixture=lambda: both(B237, 'THREE GREEN AND ONE AMBER', 'MEASURED, NOT CERTIFIED'),
          witness=lambda: contains(B238, 'measured but not yet certified'))

    # 11 -- ### M-1 IS STRUCK AND THE OTHER FOUR STAND.
    h.run('m1-struck-four-remain',
          check=lambda: all(contains(BANK, s) for s in
                            ('~~**M-1 [RULING]', 'M-2 [RESULT or RULING]',
                             'M-5 [CONSTRUCTION]', 'FOUR OPEN')),
          fixture=lambda: contains(B237, '~~**M-1 [RULING]'),
          witness=lambda: contains(BANK, 'FOUR OPEN'))

    # 12 -- ### THE PER-CELL REASON FOR (2) IS STATED, not assumed -- and its price with it.
    h.run('m2-exemption-reasoned-and-priced',
          check=lambda: both(BANK, 'THE RIDER\'S WHOLE CONTENT IS PER-CELL REALIZATION',
                             'PER-CELL statement and not a structural one'),
          fixture=lambda: contains(B237, 'THE RIDER\'S WHOLE CONTENT IS PER-CELL REALIZATION'),
          witness=lambda: contains(BANK, 'PER-CELL statement and not a structural one'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
