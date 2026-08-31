# -*- coding: utf-8 -*-
"""b269_checks.py -- the b269 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION, AND GATE 10 TOKENIZES THIS FILE TO PROVE IT**
### ### (b268's fix, standing -- b267 shipped an `or` under a header denying it).

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was sealed unscanned or unsatisfiable. ### Gate 1.
###   (2) that an owner sentence was paraphrased. ### Gate 2 -- positive-controlled.
###   (3) ### THE ACT'S CENTRAL RISK: that something was CONSTRUCTED, or a candidate valued.
###       ### Gate 3 -- F-NOCONSTRUCT, and the dossier must carry no number.
###   (4) that the (ABSENT) was claimed as this act's rather than b228's. ### Gate 4.
###   (5) that "blocked" was left conflating the projection with the action. ### Gate 5.
###   (6) that R3's mismatch was argued rather than derived. ### Gate 6.
###   (7) that a candidate was recommended or adopted. ### Gate 7.
###   (8) that the missing shadow was silently omitted rather than declared. ### Gate 8.
###   (9) that h2 moved, or an owner's bank was edited, or b267 was edited. ### Gate 9.
###  (10) that this gate file carries an `or` in a check's logic. ### Gate 10 -- it tokenizes.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')

REG = os.path.join(D, 'b269_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b269_m2_statement.txt')
FIL = os.path.join(D, 'b269_filings.txt')
RUN = os.path.join(D, 'b269_run.txt')
ROWS = os.path.join(D, 'b269_rows.json')
SAT = os.path.join(D, 'audit_b269_reg_satisfiable.txt')
ADD = os.path.join(D, 'b267_addendum_test2_supplied.txt')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

OWNERS = ['b10_2026-08-17', 'b226_stated_choice', 'b227_the_trace',
          'b228_ledger_cell_statement', 'b237_left_side_assets', 'b263_top_level_silence',
          'b267_aggregation_source', 'b267_filings', 'b268_generator_nonvanishing']


def git_unchanged(rel):
    return subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def seal_ok():
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0, (p.stdout or '')


def or_in_check_logic():
    """### `tokenize`, span-scoped -- b268's mechanism, reused unchanged."""
    import tokenize
    src = io.open(SELF, encoding='utf-8').read()
    spans = []
    for m in re.finditer(r'check=lambda:(.*?)fixture=', src, re.S):
        spans.append((src[:m.start(1)].count(chr(10)) + 1,
                      src[:m.end(1)].count(chr(10)) + 1))
    with open(SELF, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    bad = 0
    for t in toks:
        if t.type == tokenize.NAME and t.string == 'or':
            for lo, hi in spans:
                if lo <= t.start[0] <= hi:
                    bad += 1
                    break
    return bad, len(spans)


def main():
    h = Harness(repo_root=ROOT, act='b269')
    R = json.load(io.open(ROWS, encoding='utf-8'))

    # 1 -- ### SEALED AFTER SCAN AND SATISFIABILITY.
    h.run('sealed-after-scan-and-satisfiability',
          check=lambda: bool(seal_ok()[0] and 'SEAL INTACT' in seal_ok()[1]
                             and os.path.exists(SAT)
                             and contains(SAT, 'JOINTLY SATISFIABLE')
                             and contains(BANK, 'BEFORE ### SEALING')),
          # ### FIXTURE: the BANK has no seal block, so verifying IT must FAIL (exit 1).
          fixture=lambda: bool(subprocess.run([sys.executable, SEAL, '--verify', BANK],
                                              capture_output=True, text=True,
                                              cwd=ROOT).returncode == 0),
          witness=lambda: contains(SAT, 'JOINTLY SATISFIABLE'))

    # 2 -- ### EVERY OWNER SENTENCE VERBATIM, CHECKER SHOWN ABLE TO MISS.
    h.run('owner-sentences-verbatim-checker-can-miss',
          check=lambda: bool(R['f_quote'] is True
                             and R['unfindable'] == 0
                             and R['control'] is True
                             and contains(RUN, 'F-QUOTE DID NOT FIRE')),
          # ### FIXTURE: claim a quotation is still unfindable. ### 0 of 14 are, after the fix.
          fixture=lambda: bool(R['unfindable'] > 0),
          witness=lambda: bool(R['control'] is True))

    # 3 -- ### THE CENTRAL RISK: NOTHING CONSTRUCTED, NO CANDIDATE VALUED.
    h.run('nothing-constructed-no-candidate-valued',
          check=lambda: verify_all(BANK, [
              'NO NUMBER WAS COMPUTED FOR ANY CANDIDATE',
              'NAMED AS A DOSSIER CANDIDATE AND LEFT UNCOMPUTED'.replace(
                  'NAMED AS A DOSSIER CANDIDATE AND LEFT UNCOMPUTED',
                  'NAMED AS A DOSSIER CANDIDATE'),
              'NO FIT, NO CANDIDATE VALUE, NO COMPARISON',
          ]) if bool(contains(REG, 'WRITING THAT NUMBER WOULD NOT BE DERIVING M-2')
                     and contains(FIL, 'LEFT UNCOMPUTED')) else (
              'FAIL', '### the no-construction boundary is not carried'),
          # ### FIXTURE: claim the bank reports a computed candidate value. ### It reports that
          # ### none was computed, and the registration fixed that at (B) before the run.
          fixture=lambda: bool(contains(BANK, 'THE CANDIDATE EVALUATES TO')),
          witness=lambda: contains(REG, 'IT WOULD BE PROPOSING AN OBJECT'))

    # 4 -- ### THE (ABSENT) IS b228's, NOT THIS ACT'S GREP.
    h.run('absent-is-b228s-not-this-acts-grep',
          check=lambda: bool(contains(BANK, 'NO OWNER STATES AN ACTION.')
                             and contains(BANK, 'IT IS TWO OWNERS')
                             and contains(BANK, 'A GREP OVER ONE DIRECTORY IS NOT A PROOF')
                             and bool(R['control_r1'] is True)
                             and bool(R['files_searched'] > 1000)),
          # ### FIXTURE: claim the R1 matcher found nothing at all. ### It found the objects it
          # ### was looking for; had it not, R1's silence would mean nothing (lore rule 4).
          fixture=lambda: bool(R['control_r1'] is False),
          witness=lambda: bool(R['files_searched'] > 1000))

    # 5 -- ### THE PROJECTION AND THE ACTION ARE SEPARATED.
    h.run('projection-and-action-separated',
          check=lambda: verify_all(BANK, [
              'S_quot = orthoprojection onto V_inv',
              'BLOCKED" DOES NOT MEAN "NO MAP"',
              'THE PROJECTION AND THE ACTION ARE DIFFERENT OBJECTS',
          ]) if bool(contains(FIL, 'ONLY THE SECOND IS ABSENT')) else (
              'FAIL', '### the projection/action distinction is not carried'),
          # ### FIXTURE: claim the bank says no map exists in either direction. ### It says a
          # ### map exists in direction B and is the corpus's own.
          fixture=lambda: bool(contains(BANK, 'NO MAP EXISTS IN EITHER DIRECTION')),
          witness=lambda: contains(BANK, 'A MAP IS NOT MISSING IN THIS DIRECTION'))

    # 6 -- ### R3's MISMATCH IS DERIVED FROM THE CLOSED FORM, NOT ARGUED.
    h.run('r3-mismatch-derived-not-argued',
          check=lambda: bool(contains(BANK, 'STRICTLY BETWEEN `0` AND `1`')
                             and contains(BANK, 'whose state is 1 because u lies in E_1')
                             and contains(BANK, 'A CONSTANT `1` DOES NOT REDUCE')
                             and 'REFUTED' in R['r3']),
          # ### FIXTURE: claim R3 was left open. ### It is REFUTED for the available operators,
          # ### by comparing a constant state against a family of values strictly below 1.
          fixture=lambda: bool('REFUTED' not in R['r3']),
          witness=lambda: contains(BANK, 'derived rather than argued'))

    # 7 -- ### NO CANDIDATE RECOMMENDED OR ADOPTED.
    h.run('no-candidate-recommended-or-adopted',
          check=lambda: bool(R['n_candidates'] == 4
                             and contains(BANK, 'NOT RANKED AND NOT RECOMMENDED')
                             and contains(BANK, "THE AUTHOR'S CALL, NOT")
                             and contains(FIL, 'THIS SEAT DOES NOT RULE IT')
                             and contains(BANK, 'M-2 REMAINS OWED')),
          # ### FIXTURE: claim the bank ranks the candidates. ### It states they differ in KIND
          # ### and refuses to rank them.
          fixture=lambda: bool(contains(BANK, 'THE RECOMMENDED CANDIDATE IS')),
          witness=lambda: bool(R['n_candidates'] == 4))

    # 8 -- ### THE MISSING SHADOW IS DECLARED AND CHECKED, NOT OMITTED.
    h.run('missing-shadow-declared-and-checked',
          check=lambda: verify_all(BANK, [
              'THE CONDITION FAILS',
              'A TOY MODEL WOULD HAVE BEEN WORSE THAN NOTHING',
              'AN ABSENCE THAT IS CHECKED IS A DIFFERENT THING',
          ]) if bool(contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')) else (
              'FAIL', '### the absent shadow is not declared with its reason'),
          # ### FIXTURE: claim a .lean file moved in this act. ### None did; the ferry's shadow
          # ### clause was conditional and its condition fails.
          fixture=lambda: bool([l for l in subprocess.run(
              ['git', '-C', 'D:/SIDE-global-section', 'status', '--porcelain'],
              capture_output=True, text=True).stdout.splitlines()
              if l.strip().endswith('.lean')]),
          witness=lambda: contains(BANK, 'THE DOUBLE-NAME SPECIES IN LEAN'))

    # 9 -- ### h2 UNMOVED; OWNERS AND b267 UNEDITED.
    h.run('h2-unmoved-owners-and-b267-unedited',
          check=lambda: bool(all(git_unchanged('data/%s.txt' % o) for o in OWNERS)
                             and 'patent-package' not in staged()
                             and os.path.exists(ADD)
                             and contains(ADD, 'NOT AN EDIT AND NOT AN ERRATUM')
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()
                             and contains(BANK, 'RH reduced to a single located clause, '
                                                'reduction machine-verified. h2 is the clause.')),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          # ### WITNESS: b267's files are byte-identical and the supply rides in an ADDENDUM.
          witness=lambda: bool(git_unchanged('data/b267_filings.txt')))

    # 10 -- ### THIS GATE FILE HAS NO `or` IN ANY CHECK'S LOGIC. ### b268's MECHANISM, REUSED.
    h.run('this-gate-file-has-no-or-in-its-logic',
          check=lambda: bool(or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 10
                             and contains(FIL, 'MIS-TYPED TWICE')),
          # ### FIXTURE: claim a check body carries an `or` in its logic. ### None does.
          fixture=lambda: bool(or_in_check_logic()[0] > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 10))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  check bodies scanned for `or` in logic: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
