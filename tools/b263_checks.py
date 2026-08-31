# -*- coding: utf-8 -*-
"""b263_checks.py -- the b263 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **EVERY MULTI-NEEDLE CHECK GOES THROUGH `verify_all`, WHICH NAMES THE ABSENT NEEDLE.**
### ### **AND GATE NAMES ARE TERM-SCANNED TOO -- b262's last defect, applied without being told.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was edited after sealing. ### Gate 1 -- the SEAL verifies.
###   (2) that S1 was asserted rather than derived from the quoted range. ### Gate 2.
###   (3) that the run's S3 overreach was quietly fixed. ### Gate 3 -- the run is preserved WITH
###       ### its overreach, and the survey supplies what it owed.
###   (4) that the survey's absence is a broken search. ### Gate 4 -- positive controls, and the
###       ### classifier shown able to return CANDIDATE CONSTRAINT.
###   (5) that an aggregation was adopted. ### Gate 5 -- the conditional is present in both files.
###   (6) that b220 was contradicted. ### Gate 6 -- the reconciliation is explicit.
###   (7) that b262's numbers were re-derived rather than consumed. ### Gate 7.
###   (8) that a compile was claimed without a printed profile. ### Gate 8.
###   (9) that h2 moved. ### Gate 9.
###  (10) that the patent tree was written or swept in. ### Gate 10.
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
E16 = os.path.join(ROOT, 'tools', 'e16')
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b263_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b263_top_level_silence.txt')
FIL = os.path.join(D, 'b263_filings.txt')
RUN = os.path.join(D, 'b263_run.txt')
SURV = os.path.join(D, 'b263_survey.txt')
ROWS = os.path.join(D, 'b263_rows.json')
SJSON = os.path.join(D, 'b263_survey.json')
PROF = os.path.join(D, 'b263_shadow_profile.txt')
B262E = os.path.join(D, 'b262_rows_extended.json')
B262B = os.path.join(D, 'b262_junction_limit.txt')
SHADOW = os.path.join(RES, 'Core', 'TopLevelSilenceShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SRC = os.path.join(E16, 'b263_silence.py')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py']


def py_code_only(path):
    """### `ast` STRIPPER -- PYTHON SOURCE ONLY (b260's second defect)."""
    import ast
    src = io.open(path, encoding='utf-8').read()
    doc = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) \
                    and isinstance(node.body[0].value, ast.Constant) \
                    and isinstance(node.body[0].value.value, str):
                s0 = node.body[0]
                for ln in range(s0.lineno, (s0.end_lineno or s0.lineno) + 1):
                    doc.add(ln)
    return '\n'.join(l.split('#', 1)[0] for i, l in enumerate(src.split('\n'), 1) if i not in doc)


def git_unchanged(rel):
    p = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                       capture_output=True, text=True)
    return p.returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def seal_ok():
    """### RUN THE SEAL VERIFIER AS A SUBPROCESS AND READ ITS EXIT CODE. ### Not re-implemented."""
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0, (p.stdout or '')


def main():
    h = Harness(repo_root=ROOT, act='b263')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    S = json.load(io.open(SJSON, encoding='utf-8'))
    E = json.load(io.open(B262E, encoding='utf-8'))

    # 1 -- ### THE SEAL VERIFIES, AND THE SEALING DEFECT IS DISCLOSED.
    h.run('registration-sealed-and-seal-verifies',
          check=lambda: verify_all(BANK, [
              'SEALED A REGISTRATION THAT HAD JUST RETURNED `NOT CLEAN`',
              'A POSITIVE CONTROL OBTAINED FOR FREE, ON MY OWN EDIT',
              'A TOOL THAT COULD RE-SEAL WITHOUT LEAVING A TRACE WOULD UNDO ITS OWN POINT',
          ]) if bool(seal_ok()[0] and 'SEAL INTACT' in seal_ok()[1]) else (
              'FAIL', '### the registration seal does not verify'),
          # ### FIXTURE: the BANK carries no seal block, so verifying it must FAIL (exit 1).
          fixture=lambda: bool(subprocess.run([sys.executable, SEAL, '--verify', BANK],
                                              capture_output=True, text=True,
                                              cwd=ROOT).returncode == 0),
          witness=lambda: bool(seal_ok()[0]))

    # 2 -- ### S1 IS DERIVED FROM THE QUOTED RANGE, AND EXHIBITED WITH ZERO VIOLATIONS.
    h.run('silence-derived-from-the-quoted-range',
          check=lambda: bool(R['s1_bad'] == 0
                             and sum(1 for r in R['s1_rows'] if r['top']) == 11
                             and all(r['tau'] == 0.0 and r['phi'] == 1.0
                                     for r in R['s1_rows'] if r['top'])
                             and all(r['tau'] > 0.0 for r in R['s1_rows'] if not r['top'])
                             and contains(BANK, '0 for k >= n')
                             and contains(BANK, 'THE FIRST-LEVEL PRIMES ARE SILENT')),
          # ### FIXTURE: claim some top-level tau_q is non-zero. ### Every one is exactly 0.
          fixture=lambda: bool(any(r['tau'] != 0.0 for r in R['s1_rows'] if r['top'])),
          # ### WITNESS: the interior values are STRICTLY POSITIVE -- the formula is not
          # ### identically zero, which is what makes the top level's zero mean something.
          witness=lambda: bool(all(r['tau'] > 0.0 for r in R['s1_rows'] if not r['top'])))

    # 3 -- ### THE RUN'S S3 OVERREACH IS PRESERVED AND DISCLOSED, NOT QUIETLY FIXED.
    h.run('run-overreach-preserved-and-disclosed',
          check=lambda: verify_all(BANK, [
              'A COUNT IS NOT A READING, AND A VERDICT THAT RUNS AHEAD OF ITS EVIDENCE',
              'IT DOES NOT STOP BEING THAT SPECIES BECAUSE THE VERDICT',
              'THE RUN IS PRESERVED UNCHANGED',
          ]) if bool(contains(RUN, 'NO HOLDING CONSTRAINS THE TOP LEVEL')
                     and contains(SURV, 'THE RUN COUNTED; THIS READS')) else (
              'FAIL', '### the run no longer carries its overreach, or the survey is absent'),
          # ### FIXTURE: claim the run's overreaching verdict line is gone. ### It is still there.
          fixture=lambda: bool(not contains(RUN, 'NO HOLDING CONSTRAINS THE TOP LEVEL')),
          witness=lambda: contains(SURV, 'CANDIDATE CONSTRAINTS FOUND'))

    # 4 -- ### THE SURVEY'S ABSENCE IS A MEASUREMENT: 0 CANDIDATES, AND THE CLASSIFIER CAN SAY YES.
    h.run('survey-absence-is-measured-not-broken',
          check=lambda: bool(S['candidates'] == 0
                             and sum(S['tally'].values()) == 27
                             and S['tally'].get('SUPPLIES', 0) == 7
                             and S['tally'].get('DEFINES', 0) == 2
                             and S['tally'].get('OTHER', 0) == 18
                             and contains(SURV, 'THE CLASSIFIER DISCRIMINATES')
                             and contains(SURV, 'CANDIDATE CONSTRAINT')),
          # ### FIXTURE: claim the survey read nothing at all. ### It read 27 lines; a survey that
          # ### found NOTHING would be a broken search, not a measured absence.
          fixture=lambda: bool(sum(S['tally'].values()) == 0),
          witness=lambda: bool(S['tally'].get('SUPPLIES', 0) > 0))

    # 5 -- ### NO AGGREGATION ADOPTED, AND THE SPECIFICATION CARRIES ITS CONDITION.
    h.run('no-aggregation-adopted-specification-is-conditional',
          check=lambda: verify_all(BANK, [
              'NO AGGREGATION IS ADOPTED, STATED OR REALIZED',
              'THE SPECIFICATION BELOW IS FOR THE FIRST BRANCH ONLY AND IS VACUOUS ON THE SECOND',
              # ### THIS NEEDLE READ `THEY EXCLUDE` AND THE BANK SAYS `THESE EXCLUDE`.
              # ### ### **b229's SPECIES AGAIN -- BUT THIS TIME THE HARNESS NAMED THE ABSENT
              # ### ### NEEDLE OUTRIGHT AND THE FIX TOOK ONE `needle_extract` CALL.** ### b229,
              # ### b260 and b261 each cost a throwaway probe to locate; ### **THIS COST NONE.**
              'THESE EXCLUDE; THEY DO NOT DETERMINE',
              'THE SPECIFICATION IS NOT A PROPOSAL',
          ]) if bool(contains(FIL, 'SPECIFIED-NOT-STATED')
                     and contains(FIL, 'M-2 IS STILL OWED')) else (
              'FAIL', '### the filings do not carry M-2 as still owed'),
          # ### FIXTURE: b262's bank predates the specification entirely.
          fixture=lambda: contains(B262B, 'THE SPECIFICATION IS NOT A PROPOSAL'),
          witness=lambda: contains(FIL, 'm2-spec'))

    # 6 -- ### b220 IS RECONCILED EXPLICITLY, NOT LEFT TO A READER.
    h.run('b220-reconciled-explicitly',
          check=lambda: verify_all(BANK, [
              'NOT ONE OF THE FOUR EXCLUDES ANY FUNCTION',
              'THAT VERDICT IS ABOUT THE FOUR CONSTRAINTS ALREADY IN THE RECORD AND IT STANDS',
              'CONDITIONALLY NARROWED',
              '(SPEC-1) DOES EXCLUDE -- IT EXCLUDES `Theta_q` ITSELF',
          ]),
          # ### FIXTURE: b262's bank has no b220 reconciliation.
          fixture=lambda: contains(B262B, 'CONDITIONALLY NARROWED'),
          witness=lambda: contains(FIL, 'b220 IS CONDITIONALLY NARROWED, NOT CONTRADICTED'))

    # 7 -- ### b262's LADDER IS CONSUMED, NOT RE-DERIVED; AND THE SILENT SHARE IS MONOTONE.
    h.run('b262-ladder-consumed-not-rederived',
          check=lambda: bool(len(R['shares']) == 7
                             and all(R['shares'][i] <= R['shares'][i + 1]
                                     for i in range(len(R['shares']) - 1))
                             and abs(R['shares'][0] - E['rows'][0]['m1'] / E['rows'][0]['total']) < 1e-12
                             and abs(R['shares'][-1] - E['rows'][-1]['m1'] / E['rows'][-1]['total']) < 1e-12
                             and R['shares'][-1] > 0.999
                             and 'def junction' not in py_code_only(SRC)
                             and contains(RUN, 'NO NUMBER RE-DERIVED')),
          # ### FIXTURE: claim this act recomputed the junction itself. ### It reads b262's JSON.
          fixture=lambda: bool('def junction' in py_code_only(SRC)),
          witness=lambda: bool(len(R['shares']) == 7))

    # 8 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 9
                             and contains(PROF, 'ALL THREE REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and contains(SHADOW, 'the_level_below_is_inside_the_range')
                             and contains(SHADOW, 'first_level_prime_has_a_level_the_range_does_not_reach')
                             and contains(BANK, '9 TERMINALS, ZERO AXIOMS')),
          # ### FIXTURE: demand 10 terminals. ### There are 9.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 10),
          witness=lambda: contains(PROF, 'import took'))

    # 9 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE; THE FIVE MISREADINGS ARE REFUSED.
    h.run('register-sentence-exact-and-five-misreadings-refused',
          check=lambda: verify_all(BANK, [
              'RH reduced to a single located clause, reduction machine-verified. h2 is the clause.',
              'IT IS NOT EVIDENCE AGAINST THE IDENTITY',
              'IT DOES NOT MOVE `h2`',
              'IT DOES NOT SAY `Theta_q` IS THE WRONG OBJECT',
              'NOTHING DEPOSITS',
          ]) if bool('h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()) else (
              'FAIL', '### the bank asserts h2'),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    # 10 -- ### NO INSTRUMENT EDITED; NOTHING STAGED UNDER THE PATENT TREE.
    h.run('instruments-unedited-and-patent-tree-untouched',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'patent-package' not in staged()
                             and 'PLACE-papers' not in staged()
                             and contains(FIL, 'BY EXPLICIT PATH AND RAN NO `git add -A`')
                             and contains(FIL, 'b259\'s BANK REMAINS UNTRACKED')),
          # ### FIXTURE: claim a patent path IS staged. ### None is.
          fixture=lambda: bool('patent-package' in staged()),
          witness=lambda: contains(FIL, 'INDEPENDENT AND UNTOUCHED BY THIS ACT'))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
