# -*- coding: utf-8 -*-
"""b266_checks.py -- the b266 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **EVERY MULTI-NEEDLE CHECK GOES THROUGH `verify_all`, WHICH NAMES THE ABSENT NEEDLE.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was sealed while unsatisfiable or unscanned. ### Gate 1.
###   (2) that an obstacle was paraphrased. ### Gate 2 -- F-QUOTE, and the emitted table.
###   (3) that the fold moved a grade or deleted a line. ### Gate 3 -- purely additive.
###   (4) that the arc silently skipped an act. ### Gate 4.
###   (5) that a lore rule arrived without its incident. ### Gate 5.
###   (6) that a judgement rule was filed as though it were a mechanism. ### Gate 6.
###   (7) that the act quietly formalized something under a filings-only ferry. ### Gate 7.
###   (8) that TECHNE-Core was pushed against its local-only scope. ### Gate 8.
###   (9) that the branch was decided rather than stated. ### Gate 9.
###  (10) that h2 moved, or an owner's bank was edited. ### Gate 10.
###  (11) that a registered expectation that came out WRONG was quietly dropped. ### Gate 11.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
TC = 'D:/MY-DOwnloads/TECHNE-Core'

REG = os.path.join(D, 'b266_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b266_state_of_the_shadow.txt')
FIL = os.path.join(D, 'b266_filings.txt')
RUN = os.path.join(D, 'b266_run.txt')
ROWS = os.path.join(D, 'b266_rows.json')
SAT = os.path.join(D, 'audit_b266_reg_satisfiable.txt')
EMIT = os.path.join(D, 'b266_fold_emitted.md')
LORE = os.path.join(TC, 'modules/2026-08/HARNESS_LORE.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'prolate_layer.py',
               'b36_act8.py', 'b261_e2even.py']
BANKS = ['b256_contribution_map', 'b257_methodology_sweep', 'b258_history_inventory',
         'b259_blob_sensitivity', 'b260_junction_sign', 'b261_e2even_monotone',
         'b262_junction_limit', 'b263_top_level_silence', 'b264_eps_even_decay',
         'b265_nq_ceiling_sweep']


def git_unchanged(repo, rel):
    p = subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', rel],
                       capture_output=True, text=True)
    return p.returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def seal_ok():
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0, (p.stdout or '')


def main():
    h = Harness(repo_root=ROOT, act='b266')
    R = json.load(io.open(ROWS, encoding='utf-8'))

    # 1 -- ### SEALED, AND SATISFIABILITY-CHECKED AND TERM-SCANNED BEFORE THE SEAL.
    h.run('sealed-after-scan-and-satisfiability',
          check=lambda: verify_all(BANK, [
              'TERM-SCANNED AND',
              'JOINT-SATISFIABILITY-CHECKED ### BEFORE ### SEALING',
          ]) if bool(seal_ok()[0] and 'SEAL INTACT' in seal_ok()[1]
                     and os.path.exists(SAT)
                     and contains(SAT, 'JOINTLY SATISFIABLE')) else (
              'FAIL', '### the seal does not verify, or no satisfiability audit exists'),
          # ### FIXTURE: the BANK carries no seal block, so verifying IT must FAIL (exit 1).
          fixture=lambda: bool(subprocess.run([sys.executable, SEAL, '--verify', BANK],
                                              capture_output=True, text=True,
                                              cwd=ROOT).returncode == 0),
          witness=lambda: contains(SAT, 'JOINTLY SATISFIABLE'))

    # 2 -- ### NO OBSTACLE PARAPHRASED, AND THE TABLE WAS EMITTED RATHER THAN TYPED.
    h.run('obstacles-verbatim-and-table-emitted',
          check=lambda: bool(R['f_quote'] is True
                             and R['unfindable'] == 0
                             and R['n_obstacles'] >= 12
                             and R['control_discriminates'] is True
                             and os.path.exists(EMIT)
                             and contains(FINDINGS, 'DERIVES BY TERMWISE DOMINATION')
                             and contains(BANK, 'ONE THAT\nGENERATES THE WRITING CANNOT EMIT ONE')),
          # ### FIXTURE: claim some quotation was unfindable. ### 0 of 12 were.
          fixture=lambda: bool(R['unfindable'] > 0),
          # ### WITNESS: the checker is shown able to MISS -- an altered quotation is reported
          # ### unfindable. ### A matcher that never misses is not matching.
          witness=lambda: bool(R['control_discriminates'] is True))

    # 3 -- ### THE FOLD IS PURELY ADDITIVE. ### NO GRADE MOVED.
    h.run('fold-purely-additive-no-grade-moved',
          check=lambda: bool(R['findings_removed'] == 0
                             and R['findings_added'] > 0
                             and R['f_nograde'] is True
                             and contains(BANK, 'NO GRADE MOVED')
                             and contains(FINDINGS, 'NO GRADE MOVES IN THIS FOLD')),
          # ### FIXTURE: claim a line was deleted or retagged. ### -0 against HEAD.
          fixture=lambda: bool(R['findings_removed'] > 0),
          witness=lambda: bool(R['findings_added'] > 0))

    # 4 -- ### THE ARC RECONCILES: TEN ACTS, CONTIGUOUS, EVERY ONE REPRESENTED.
    h.run('arc-reconciles-ten-acts-contiguous',
          check=lambda: bool(R['f_count'] is True
                             and len(R['arc']) == 10
                             and len(R['acts_covered']) == 10
                             and R['arc'][0] == 'b256' and R['arc'][-1] == 'b265'
                             and contains(FINDINGS, '0-ter. THE J-ARC')),
          # ### FIXTURE: demand eleven acts. ### There are ten, b256..b265.
          fixture=lambda: bool(len(R['arc']) == 11),
          witness=lambda: bool(len(R['acts_covered']) == 10))

    # 5 -- ### EVERY LORE RULE CARRIES ITS INCIDENT.
    h.run('every-lore-rule-carries-its-incident',
          check=lambda: bool(R['f_incident'] is True
                             and R['n_rules'] == 21
                             and len(R['rules_missing_incident']) == 0
                             and contains(LORE, 'RULES 11')),
          # ### FIXTURE: demand 22 rules. ### There are 21 -- ten prior plus this act's eleven.
          fixture=lambda: bool(R['n_rules'] == 22),
          witness=lambda: bool(R['n_rules'] == 21))

    # 6 -- ### A JUDGEMENT RULE IS NOT FILED AS A MECHANISM, AND THE CAUTION IS REPEATED.
    h.run('judgement-rules-named-and-caution-repeated',
          check=lambda: verify_all(BANK, [
              'JUDGEMENT RULES ARE NAMED AS JUDGEMENT RULES',
              'LORE IS NOT A GUARD',
              'A JUDGEMENT RULE FILED AS THOUGH IT\n### WERE A MECHANISM',
          ]) if bool(contains(LORE, 'LORE IS NOT A GUARD')
                     and contains(FIL, 'FASTER THAN IT HAS GROWN GUARDS')) else (
              'FAIL', '### the caution is absent, or judgement rules are not distinguished'),
          # ### FIXTURE: claim the lore file dropped its caution. ### It repeats it.
          fixture=lambda: bool(not contains(LORE, 'LORE IS NOT A GUARD')),
          witness=lambda: contains(LORE, 'MECHANIZABLE'))

    # 7 -- ### NOTHING WAS FORMALIZED UNDER A FILINGS-ONLY FERRY, AND THE ABSENCE IS CHECKED.
    h.run('nothing-formalized-and-the-absence-is-checked',
          check=lambda: bool(R['f_noshadow'] is True
                             and R['lean_moved'] == 0
                             and contains(BANK, 'AN ABSENCE THAT IS\n### CHECKED IS A DIFFERENT '
                                                'THING FROM AN ABSENCE THAT IS ASSUMED')),
          # ### FIXTURE: claim a .lean file moved. ### Zero did, across all three repos.
          fixture=lambda: bool(R['lean_moved'] > 0),
          witness=lambda: bool(R['f_noshadow'] is True))

    # 8 -- ### TECHNE-Core WAS NOT PUSHED, AND ITS SCOPE WAS CARRIED IN ADVANCE.
    h.run('techne-core-not-pushed-scope-carried-in-advance',
          check=lambda: bool(subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                                            capture_output=True, text=True).stdout.strip()
                             == '22739c9'
                             and contains(REG, 'LOCAL-ONLY, AS SCOPED')
                             and contains(FIL, '`TECHNE-Core` WAS NOT PUSHED')),
          # ### FIXTURE: claim TECHNE-Core's HEAD moved. ### It is still 22739c9.
          fixture=lambda: bool(subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                                              capture_output=True, text=True).stdout.strip()
                               != '22739c9'),
          witness=lambda: contains(REG, 'LOCAL-ONLY, AS SCOPED'))

    # 9 -- ### THE BRANCH IS STATED, NOT DECIDED.
    h.run('branch-stated-never-decided',
          check=lambda: verify_all(BANK, [
              'THE BRANCH IS NOT DECIDED',
              'IS ### NOT ### "THE ARCHIMEDEAN SIDE"',
              'NOTHING IN THIS ARC EXCLUDES ONE',
          ]) if bool(contains(FINDINGS, 'THE BRANCH IS NOT DECIDED')
                     and contains(FINDINGS, 'W-ORD-TQ-IDENTIFY')) else (
              'FAIL', '### the fold does not carry the branch as undecided'),
          # ### FIXTURE: claim the bank decides the branch. ### It says the opposite, twice.
          fixture=lambda: bool(contains(BANK, 'THE BRANCH IS DECIDED.')),
          witness=lambda: contains(FINDINGS, 'branch-not-decided'))

    # 10 -- ### h2 UNMOVED; NO OWNER BANK OR INSTRUMENT EDITED; NO FOREIGN TREE STAGED.
    h.run('h2-unmoved-and-owners-unedited',
          check=lambda: bool(all(git_unchanged(ROOT, 'tools/e16/' + f) for f in INSTRUMENTS)
                             and all(git_unchanged(ROOT, 'data/%s.txt' % b) for b in BANKS)
                             and 'patent-package' not in staged()
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()
                             and contains(BANK, 'RH reduced to a single located clause, '
                                                'reduction machine-verified. h2 is the clause.')
                             and contains(BANK, 'NOTHING DEPOSITS')),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: bool(all(git_unchanged(ROOT, 'data/%s.txt' % b) for b in BANKS)))

    # 11 -- ### THE REGISTERED EXPECTATION THAT CAME OUT WRONG IS REPORTED WRONG, AND DEFLATED.
    # ### ### **THIS GATE EXISTS BECAUSE AN ACT WHOSE PREDICTION "PASSED" HAS EVERY INCENTIVE TO
    # ### ### BANK IT AS A PASS RATHER THAN ASK WHY IT PASSED.**
    h.run('wrong-expectation-reported-and-not-flattered',
          check=lambda: verify_all(BANK, [
              'S1 -- ### WRONG',
              'I EXTRACTED EVERY QUOTATION',
              'WHICH MAKES IT A WEAK PREDICTION RATHER THAN A PASSED ONE',
          ]) if bool(contains(FIL, 'THE PREDICTION WAS ABOUT A METHOD I THEN DID NOT USE')) else (
              'FAIL', '### the failed expectation is not reported, or is reported as a pass'),
          # ### FIXTURE: claim the bank scores S1 CONFIRMED. ### It scores it WRONG and then
          # ### deflates the reason rather than taking credit for the clean pass.
          fixture=lambda: bool(contains(BANK, 'S1 -- ### CONFIRMED')),
          witness=lambda: contains(BANK, 'FOUR CONFIRMED') is False)

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
