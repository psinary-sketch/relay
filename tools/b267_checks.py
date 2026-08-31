# -*- coding: utf-8 -*-
"""b267_checks.py -- the b267 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was sealed unscanned or unsatisfiable. ### Gate 1.
###   (2) that an owner sentence was paraphrased. ### Gate 2 -- F-QUOTE, positive-controlled.
###   (3) that TEST 1's zero was asserted rather than evaluated. ### Gate 3.
###   (4) ### THE ACT'S CENTRAL RISK: that `d_1 > 0` (a SECTOR statement) was read as
###       ### b226's generator being nonzero. ### Gate 4 -- the (PARTIAL) verdict must stand
###       ### and b226's owed sentence must be carried.
###   (5) that `p = 2`'s exceptionality was stated without its consequence for SPEC-3. ### Gate 5.
###   (6) that TEST 3's absence was claimed from an untested matcher. ### Gate 6.
###   (7) that an aggregation was adopted, stated or realized. ### Gate 7 -- the whole scope.
###   (8) that a compile was claimed without a printed profile. ### Gate 8.
###   (9) that a class was claimed from b223's two-place table. ### Gate 9.
###  (10) that h2 moved, or an owner's bank was edited. ### Gate 10.
###  (11) that the search design's weakness was hidden. ### Gate 11.
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
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b267_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b267_aggregation_source.txt')
FIL = os.path.join(D, 'b267_filings.txt')
RUN = os.path.join(D, 'b267_run.txt')
ROWS = os.path.join(D, 'b267_rows.json')
PROF = os.path.join(D, 'b267_shadow_profile.txt')
SAT = os.path.join(D, 'audit_b267_reg_satisfiable.txt')
SHADOW = os.path.join(RES, 'Core', 'AggregationSourceShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')

OWNERS = ['b220_aggregation_freedom', 'b223_level_limit_two_places', 'b226_stated_choice',
          'b227_the_trace', 'b237_left_side_assets', 'b260_junction_sign',
          'b262_junction_limit', 'b263_top_level_silence']
INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'prolate_layer.py']


def git_unchanged(repo, rel):
    return subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def seal_ok():
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0, (p.stdout or '')


def main():
    h = Harness(repo_root=ROOT, act='b267')
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

    # 2 -- ### EVERY OWNER SENTENCE VERBATIM, AND THE CHECKER SHOWN ABLE TO MISS.
    h.run('owner-sentences-verbatim-checker-can-miss',
          check=lambda: bool(R['f_quote'] is True
                             and R['unfindable'] == 0
                             and R['control'] is True
                             and contains(RUN, 'F-QUOTE DID NOT FIRE')),
          # ### FIXTURE: claim a quotation is still unfindable. ### 0 of 21 are, after the fix.
          fixture=lambda: bool(R['unfindable'] > 0),
          witness=lambda: bool(R['control'] is True))

    # 3 -- ### TEST 1's ZERO IS EVALUATED, NOT ASSERTED, AND THE FOIL IS CARRIED.
    h.run('test1-zero-evaluated-with-its-foil',
          check=lambda: bool(R['f_t1'] is True
                             and R['t1_kn_all_zero'] is True
                             and R['t1_kgt_all_neg'] is True
                             and len(R['t1']) >= 24
                             and contains(BANK, 'AN ARITHMETIC ZERO CANNOT')
                             and contains(BANK, 'OVERRIDING CONVENTION')),
          # ### FIXTURE: claim the expression is NOT zero at k = n somewhere. ### It is zero at
          # ### every one of the 30 tested cells, on exact fractions.
          fixture=lambda: bool(R['t1_kn_all_zero'] is False),
          # ### WITNESS: the foil is real -- at k > n the expression is strictly negative, which
          # ### is what makes the k = n zero mean something.
          witness=lambda: bool(R['t1_kgt_all_neg'] is True))

    # 4 -- ### THE ACT'S CENTRAL RISK: SECTOR vs GENERATOR. ### THE VERDICT MUST STAY (PARTIAL).
    h.run('sector-is-not-the-generator-verdict-stays-partial',
          check=lambda: verify_all(BANK, [
              'd_1 > 0 GIVES E_1 != 0. ### IT DOES NOT GIVE u_{1,1} != 0.',
              'THIS ACT DID NOT PERFORM IT AND DOES\n### ### NOT CLAIM IT.',
              'CALLING THIS (SUPPORTED) WOULD BE THIS ACT',
          ]) if bool(contains(BANK, 'VERDICT: (PARTIAL)')
                     and contains(FIL, '(PARTIAL)')) else (
              'FAIL', '### TEST 2 is not carried as (PARTIAL), or b226\'s limit is absent'),
          # ### FIXTURE: claim the bank grades TEST 2 (SUPPORTED). ### It grades it (PARTIAL)
          # ### precisely because b226 reserves the generator's nonvanishing as owed.
          fixture=lambda: bool(contains(BANK, 'TEST 2 -- THE OBJECT\'S OWN FACTOR. ### **VERDICT: '
                                              '(SUPPORTED)')),
          witness=lambda: contains(BANK, 'WHAT IS MISSING, NAMED'))

    # 5 -- ### p = 2's EXCEPTIONALITY CARRIES ITS CONSEQUENCE FOR SPEC-3.
    h.run('place-two-exceptional-with-its-spec3-consequence',
          check=lambda: bool(R['two_is_zero'] is True
                             and R['odd_all_nonzero'] is True
                             and contains(BANK, 'REQUIRES A CANDIDATE TO CARRY')
                             and contains(BANK, 'THE ARRIVAL DEPTH IS WHY ell(2) = 2 AND NOT 1.')
                             and contains(BANK, 'THE (2,1) DEATH IS ISOLATED AND DOES NOT '
                                                'PROPAGATE.')),
          # ### FIXTURE: claim d_1(2,1) is nonzero. ### The place-2 law gives 2*(2-2) = 0.
          fixture=lambda: bool(R['two_is_zero'] is False),
          witness=lambda: bool(R['odd_all_nonzero'] is True))

    # 6 -- ### TEST 3's ABSENCE RESTS ON A MATCHER SHOWN ABLE TO FIND SOMETHING.
    h.run('absence-from-a-matcher-shown-able-to-find',
          check=lambda: bool(R['f_t3_control'] is True
                             and len(R['t3_present_hits']) > 0
                             and R['t3_files_searched'] > 100
                             and contains(BANK, 'THE MATCHER READS')
                             and contains(BANK, 'A GREP OVER ONE DIRECTORY IS NOT A PROOF')),
          # ### FIXTURE: claim the positive control found nothing. ### It found b227's own
          # ### product formula; had it not, TEST 3 would be VOID (lore rule 4).
          fixture=lambda: bool(R['f_t3_control'] is False),
          witness=lambda: bool(R['t3_files_searched'] > 100))

    # 7 -- ### NO AGGREGATION ADOPTED, STATED OR REALIZED. ### THE WHOLE SCOPE.
    h.run('no-aggregation-adopted-stated-or-realized',
          check=lambda: verify_all(BANK, [
              'NO FUNCTION SATISFYING (SPEC-1)-(SPEC-3)\n### IS EXHIBITED',
              'M-2 IS OWED',
              'SPECIFIED-NOT-STATED ### . ### UNCHANGED. ### NO ADOPTION',
          ]) if bool(contains(FIL, 'NO AGGREGATION WAS ADOPTED, STATED OR REALIZED')
                     and 'IT COMPILES NO AGGREGATION' in
                     io.open(SHADOW, encoding='utf-8').read()) else (
              'FAIL', '### the act does not carry its own no-adoption clause'),
          # ### FIXTURE: claim the bank moved M-2's status. ### It is UNCHANGED.
          fixture=lambda: bool(contains(BANK, 'M-2 IS DISCHARGED')),
          witness=lambda: contains(BANK, 'THE SPECIFICATION STILL EXCLUDES AND DOES NOT'))

    # 8 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 9
                             and contains(PROF, 'ALL FOUR REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and 'sorryAx' not in io.open(PROF, encoding='utf-8').read()
                             and contains(SHADOW, 'numerator_does_not_vanish_above_top')
                             and contains(SHADOW, 'the_two_laws_disagree_at_first_level')),
          # ### FIXTURE: demand 10 terminals. ### There are 9.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 10),
          witness=lambda: contains(PROF, 'import took'))

    # 9 -- ### NO CLASS CLAIMED FROM A TWO-PLACE TABLE.
    h.run('generality-is-the-kernels-not-the-tables',
          # ### ### **DEFECT (D4), DECLARED: this check first read
          # ### ### `(X is False) or Y and Z and W` -- ### AN `or` ### , in a file whose own
          # ### ### header says "NO `or` APPEARS IN ANY CHECK". ### THAT IS LORE RULE 2's EXACT
          # ### ### SPECIES (b251: a gate that passes on one disjunct asserts only that
          # ### ### disjunct), COMMITTED TWO ACTS AFTER THIS SEAT CONSOLIDATED RULE 2.**
          # ### ### **REPAIRED TO A PURE CONJUNCTION.**
          check=lambda: bool(contains(RUN, 'THE KERNEL GENERALIZES')
                             and contains(REG, 'A TWO-PLACE TABLE IS NOT A CLASS.')
                             and contains(FIL, 'the odd-`p` generality is the KERNEL')
                             and contains(BANK, 'kernel-general')),
          # ### FIXTURE: claim the registration lacks the resolution clause. ### It carries it
          # ### at (A), fixed before any owner was read for a verdict.
          fixture=lambda: bool(not contains(REG, 'A TWO-PLACE TABLE IS NOT A CLASS.')),
          witness=lambda: contains(RUN, 'THE KERNEL GENERALIZES'))

    # 10 -- ### h2 UNMOVED; OWNERS UNEDITED; NO FOREIGN TREE STAGED.
    h.run('h2-unmoved-and-owners-unedited',
          check=lambda: bool(all(git_unchanged(ROOT, 'data/%s.txt' % o) for o in OWNERS)
                             and all(git_unchanged(ROOT, 'tools/e16/' + f) for f in INSTRUMENTS)
                             and 'patent-package' not in staged()
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()
                             and contains(BANK, 'RH reduced to a single located clause, '
                                                'reduction machine-verified. h2 is the clause.')
                             and contains(BANK, 'NOTHING DEPOSITS')),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: bool(all(git_unchanged(ROOT, 'data/%s.txt' % o) for o in OWNERS)))

    # 11 -- ### THE SEARCH DESIGN'S WEAKNESS IS DISCLOSED, NOT HIDDEN.
    # ### ### **AN ACT THAT REPORTS AN ABSENCE HAS EVERY INCENTIVE TO LET ITS SEARCH LOOK
    # ### ### STRONGER THAN IT WAS.**
    h.run('search-design-weakness-disclosed',
          check=lambda: verify_all(BANK, [
              'A NEEDLE DRAWN FROM THE SENTENCE THAT NAMES AN ABSENCE WILL ALWAYS',
              'THE HITS ARE ALL SELF-HITS',
              'THE ABSENCE IS b237',
          ]) if bool(contains(FIL, 'THE TEST-3 SEARCH DESIGN IS WEAKER THAN IT LOOKS')) else (
              'FAIL', '### the search design\'s limit is not disclosed'),
          # ### FIXTURE: claim the act presents the grep as the source of the verdict.
          # ### It says outright the verdict is b237's and the grep is corroboration.
          fixture=lambda: bool(contains(BANK, 'THE VERDICT IS THIS ACT\'S GREP')),
          witness=lambda: contains(RUN, 'SELF-HITS'))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
