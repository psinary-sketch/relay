# -*- coding: utf-8 -*-
"""b268_checks.py -- the b268 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK'S LOGIC.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **AND b267's (D4) IS NOT REPEATED: the check bodies are scanned for `or` by gate 11.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was sealed unscanned or unsatisfiable. ### Gate 1.
###   (2) that an owner sentence was paraphrased. ### Gate 2 -- positive-controlled.
###   (3) ### THE ACT'S CENTRAL RISK: that a float decided a vanishing. ### Gate 3 -- the exact
###       ### tester, positive-controlled on a known zero AND a known nonzero.
###   (4) that the support formula does not reproduce b226's six measured cells. ### Gate 4.
###   (5) that the result was claimed from the table rather than derived. ### Gate 5 --
###       ### unmeasured places must be present, and the bank must say which is which.
###   (6) that a support was read as a contribution, i.e. (SPEC-1) claimed. ### Gate 6.
###   (7) that p = 2 was folded into the odd result. ### Gate 7 -- the hinge and its foil.
###   (8) that a compile was claimed without a printed profile. ### Gate 8.
###   (9) that b226's or b267's verdicts were re-graded rather than cited. ### Gate 9.
###  (10) that h2 moved, or an owner's bank was edited. ### Gate 10.
###  (11) that this gate file repeated b267's `or` defect. ### Gate 11 -- it scans itself.
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
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b268_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b268_generator_nonvanishing.txt')
FIL = os.path.join(D, 'b268_filings.txt')
RUN = os.path.join(D, 'b268_run.txt')
ROWS = os.path.join(D, 'b268_rows.json')
PROF = os.path.join(D, 'b268_shadow_profile.txt')
SAT = os.path.join(D, 'audit_b268_reg_satisfiable.txt')
SHADOW = os.path.join(RES, 'Core', 'GeneratorSupportShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

OWNERS = ['b223_level_limit_two_places', 'b226_stated_choice', 'b227_the_trace',
          'b237_left_side_assets', 'b263_top_level_silence', 'b267_aggregation_source']


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


def main():
    h = Harness(repo_root=ROOT, act='b268')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    rows = R['rows']

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
                             and R['control_quote'] is True
                             and contains(RUN, 'F-QUOTE DID NOT FIRE')),
          # ### FIXTURE: claim a quotation was unfindable. ### 0 of 12 were.
          fixture=lambda: bool(R['unfindable'] > 0),
          witness=lambda: bool(R['control_quote'] is True))

    # 3 -- ### THE CENTRAL RISK: NO FLOAT DECIDES A VANISHING.
    h.run('no-float-decides-a-vanishing',
          check=lambda: bool(R['f_exact'] is True
                             and contains(RUN, 'reported ZERO (must be zero)')
                             and contains(RUN, 'reported NONZERO (must be nonzero)')
                             and contains(RUN, 'NO FLOATING POINT ENTERS ANY CELL')
                             and contains(BANK, 'NO FLOATING POINT ENTERS ANY d_1.')),
          # ### FIXTURE: claim the exact tester failed its control. ### It reported a known
          # ### zero as zero AND a known nonzero as nonzero; a tester that cannot say both
          # ### is not a tester.
          fixture=lambda: bool(R['f_exact'] is False),
          witness=lambda: bool(R['f_exact'] is True))

    # 4 -- ### THE DERIVATION REPRODUCES b226's SIX MEASURED CELLS.
    h.run('reproduces-b226-six-measured-cells',
          check=lambda: bool(R['b226_agree'] is True
                             and R['all_agree'] is True
                             and len([r for r in rows if r['banked'] is not None]) == 6
                             and all(r['support'] == r['target'] for r in rows)),
          # ### FIXTURE: claim a cell disagrees with b226's banked support. ### All six match.
          fixture=lambda: bool(R['b226_agree'] is False),
          witness=lambda: bool(len([r for r in rows if r['banked'] is not None]) == 6))

    # 5 -- ### THE RESULT IS THE DERIVATION'S, NOT THE TABLE'S.
    h.run('result-is-derived-table-is-a-control',
          check=lambda: bool(len([r for r in rows if r['banked'] is None]) == 2
                             and R['all_nonzero'] is True
                             and contains(BANK, 'A CHECK ON THE DERIVATION, NEVER ITS EVIDENCE')
                             and contains(RUN, 'NEVER ITS EVIDENCE')
                             and contains(BANK, 'gcd(q+2, q^2) = 1')),
          # ### FIXTURE: claim no unmeasured place was run. ### p = 17 and p = 19 were run,
          # ### so the control is not confined to the cells the formula was first seen on.
          fixture=lambda: bool(len([r for r in rows if r['banked'] is None]) == 0),
          witness=lambda: bool(R['all_nonzero'] is True))

    # 6 -- ### A SUPPORT IS NOT A CONTRIBUTION. ### (SPEC-1) IS NOT CLAIMED.
    h.run('support-is-not-a-contribution-spec1-untouched',
          check=lambda: verify_all(BANK, [
              'A SUPPORT IS NOT A CONTRIBUTION',
              'M-2 REMAINS SPECIFIED-NOT-STATED',
              'NO AGGREGATION IS ADOPTED, STATED OR REALIZED',
          ]) if bool(contains(FIL, '(SPEC-1) IS NOT TOUCHED')
                     and 'IT COMPILES NO GENERATOR' in
                     io.open(SHADOW, encoding='utf-8').read()) else (
              'FAIL', '### the act does not carry its (SPEC-1) boundary'),
          # ### FIXTURE: claim the bank asserts SPEC-1 is met. ### It says the opposite.
          fixture=lambda: bool(contains(BANK, '(SPEC-1) IS MET')),
          witness=lambda: contains(BANK, 'b226\'s STEP IS PAID; (SPEC-1) IS NOT TOUCHED'))

    # 7 -- ### p = 2 IS NOT FOLDED IN, AND THE HINGE CARRIES ITS FOIL.
    h.run('place-two-separate-with-the-hinge-and-its-foil',
          check=lambda: bool(contains(BANK, 'gcd(6, 16) = 2')
                             and contains(BANK, 'AT EVERY ODD `p` AT LEVEL 1, AND AT `p = 2`')
                             and contains(SHADOW, 'hinge_fails_at_q_four')
                             and contains(SHADOW, 'hinge_holds_at_odd_places')
                             and bool([r for r in rows if r['p'] == 2][0]['level'] == 2)),
          # ### FIXTURE: claim p = 2 was computed at level 1. ### It is computed at level 2,
          # ### because d_1(2,1) = 0 and there is no unit at level 1 to build from.
          fixture=lambda: bool([r for r in rows if r['p'] == 2][0]['level'] == 1),
          witness=lambda: contains(SHADOW, 'place_two_still_lands_on_the_count'))

    # 8 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 9
                             and contains(PROF, 'ALL FOUR REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and 'sorryAx' not in io.open(PROF, encoding='utf-8').read()
                             and contains(SHADOW, 'the_count_vanishes_at_q_one')),
          # ### FIXTURE: demand 10 terminals. ### There are 9.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 10),
          witness=lambda: contains(PROF, 'import took'))

    # 9 -- ### b226 AND b267 ARE CITED, NOT RE-GRADED.
    h.run('owners-cited-not-re-graded',
          check=lambda: verify_all(BANK, [
              'b226 IS NOT RE-VERDICTED BY THIS',
              'A LATER ACT SUPPLIED THE DERIVATION\n### ### ### IT DECLINED TO ASSERT',
              'b267\'s VERDICT IS NOT RE-GRADED BY THIS ACT',
          ]) if bool(contains(FIL, 'THE AUTHOR RULES WHETHER b267')) else (
              'FAIL', '### an owner was re-graded, or the routing is absent'),
          # ### FIXTURE: claim the bank overwrites b267's verdict. ### It routes it instead.
          fixture=lambda: bool(contains(BANK, 'b267 IS RE-GRADED')),
          witness=lambda: contains(FIL, 'PAID'))

    # 10 -- ### h2 UNMOVED; OWNERS UNEDITED; NO FOREIGN TREE STAGED.
    h.run('h2-unmoved-and-owners-unedited',
          check=lambda: bool(all(git_unchanged('data/%s.txt' % o) for o in OWNERS)
                             and 'patent-package' not in staged()
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()
                             and contains(BANK, 'RH reduced to a single located clause, '
                                                'reduction machine-verified. h2 is the clause.')
                             and contains(BANK, 'NOTHING DEPOSITS')),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: bool(all(git_unchanged('data/%s.txt' % o) for o in OWNERS)))

    # 11 -- ### THIS FILE DOES NOT REPEAT b267's (D4). ### IT SCANS ITS OWN CHECK BODIES.
    # ### ### **b267 SHIPPED AN `or` IN A FILE DECLARING IT HAD NONE. ### THE ANSWER IS NOT TO
    # ### ### DECLARE HARDER; IT IS TO CHECK.**
    def or_in_check_logic():
        """### ### **EXACT, NOT REGEX-GUESSY.** ### `tokenize` distinguishes a NAME token `or`
        ### -- the operator -- from the letters `or` inside a STRING or a COMMENT, which a regex
        ### cannot, and which is what made the first draft of this gate report two false hits.
        ### ### **AND IT IS SCOPED TO THE `check=` BODIES**, because `(p.stdout or '')` in a
        ### helper is a Python idiom and not a gate's logic.
        ### ### **b267 SHIPPED AN `or` IN A CHECK'S LOGIC UNDER A HEADER DENYING IT. ### THE
        ### ### ANSWER IS NOT TO DECLARE HARDER; IT IS TO CHECK, AND TO CHECK EXACTLY.**"""
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

    h.run('this-gate-file-has-no-or-in-its-logic',
          check=lambda: bool(or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 11
                             and contains(FIL, 'DOUBLE-NAME ERROR RUN BACKWARDS')),
          # ### FIXTURE: claim a check body carries an `or` in its logic. ### None does --
          # ### and b267's did, which is why this gate exists rather than a louder header.
          fixture=lambda: bool(or_in_check_logic()[0] > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 11))

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
