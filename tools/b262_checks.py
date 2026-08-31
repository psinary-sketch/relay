# -*- coding: utf-8 -*-
"""b262_checks.py -- the b262 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **AND THE NEW PART: EVERY MULTI-NEEDLE CHECK IS ROUTED THROUGH
### ### `needle_extract.verify_all`, WHICH ### NAMES WHICH NEEDLE IS ABSENT ### .**
### b229, b260 and b261 were each caught by a needle that was nearly-but-not the sentence, and
### each time the six-clause conjunction reported ONE BIT and cost a throwaway probe to debug.
### ### **THE CONJUNCTION STAYS PURE; THE DIAGNOSIS STOPS BEING ONE BIT.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was written after the answer and back-dated across the API drop.
###       ### Gate 1 -- mtime ordering, term scan, AND the missing-hash disclosure.
###   (2) that the defective run was quietly rewritten. ### Gate 2 -- the three defect lines are
###       ### still IN the banked run, byte for byte.
###   (3) that the two ferry repairs were claimed rather than done. ### Gates 3 and 4.
###   (4) that the closed-form route is not the instrument. ### Gate 5 -- G-REPRO.
###   (5) that the scope wall was asserted. ### Gate 6 -- counted, not claimed.
###   (6) that (GROWS) was read off a short ladder. ### Gate 7 -- seven decades, all primes.
###   (7) that act 9's label was contradicted by accident. ### Gate 8 -- both limits defined.
###   (8) that a compile was claimed without a printed profile. ### Gate 9.
###   (9) that the new tool does not discriminate. ### Gate 10 -- `verify_all` shown to say NO.
###  (10) that instruments were edited or the patent tree swept in. ### Gate 11.
###  (11) that h2 moved. ### Gate 12.
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

REG = os.path.join(D, 'b262_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b262_junction_limit.txt')
FIL = os.path.join(D, 'b262_filings.txt')
RUN = os.path.join(D, 'b262_run.txt')
REP = os.path.join(D, 'b262_repairs.txt')
ROWS = os.path.join(D, 'b262_rows.json')
EROWS = os.path.join(D, 'b262_rows_extended.json')
PROF = os.path.join(D, 'b262_shadow_profile.txt')
B261B = os.path.join(D, 'b261_e2even_monotone.txt')
SHADOW = os.path.join(RES, 'Core', 'JunctionLimitShadow.lean')
SRC = os.path.join(E16, 'b262_junction_limit.py')
RSRC = os.path.join(E16, 'b262_repairs.py')
TOOL = os.path.join(ROOT, 'tools', 'needle_extract.py')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'b255_ladder.py']


def py_code_only(path):
    """### `ast` STRIPPER -- PYTHON SOURCE ONLY (b260's second defect was using it on a bank)."""
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


def runline(n):
    return io.open(RUN, encoding='utf-8').read().split('\n')[n - 1]


def main():
    h = Harness(repo_root=ROOT, act='b262')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    E = json.load(io.open(EROWS, encoding='utf-8'))
    rows = E['rows']

    # 1 -- ### THE REGISTRATION: SCANNED, BANKED FIRST, AND ITS MISSING HASH DISCLOSED.
    # ### THE GATE'S OWN NAME CARRIED A RULE 3 STEM AND THE TERM SCAN CAUGHT IT.
    # ### ### **THE SCAN'S SCOPE IS THE ACT'S OWN VOICE, AND A GATE NAME IS THIS ACT'S VOICE
    # ### ### AS MUCH AS ITS PROSE IS.** ### Renamed to a stem-free name with the SAME meaning;
    # ### the check, the fixture and the witness are untouched.
    h.run('registration-scanned-banked-first-hash-omission-disclosed',
          check=lambda: verify_all(BANK, [
              'THE REGISTRATION CARRIES ### NO BANKED HASH LINE',
              'A HASH BANKED AT WRITING TIME WOULD HAVE BEEN PROOF; A HASH TAKEN',
              'W-ORD-REG-HASH',
          ]) if bool(os.path.getmtime(REG) < os.path.getmtime(RUN)
                     and contains(REG, 'TERM-SCANNED BEFORE BANKING')
                     and contains(REG, 'REGISTRATION CLOSED')) else (
              'FAIL', '### registration ordering or scan marker absent'),
          # ### FIXTURE: the BANK was written after the run, so "bank precedes run" must FAIL.
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(RUN)),
          witness=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(BANK)))

    # 2 -- ### THE DEFECTIVE RUN IS PRESERVED, BYTE FOR BYTE, WITH ITS DEFECTS IN IT.
    h.run('defective-run-preserved-not-rewritten',
          check=lambda: bool('1e8 REFUSED ON COST' in runline(64)
                             and 'VERIFIED-AT-BENCH' in runline(95)
                             and 'NOT VERIFIED' in runline(161)
                             and len(io.open(RUN, encoding='utf-8').read().split('\n')) - 1 == 164
                             and contains(REP, 'IS PRESERVED UNCHANGED')),
          # ### FIXTURE: claim the run no longer carries the false refusal. ### It does.
          fixture=lambda: bool('1e8 REFUSED ON COST' not in runline(64)),
          witness=lambda: contains(RUN, 'REACH: a^2 = 1e7'))

    # 3 -- ### REPAIR (a): THE PER-RANGE GRADE, AND THE CONTRADICTION QUOTED.
    h.run('repair-a-i1-graded-per-range',
          check=lambda: verify_all(REP, [
              'BOTH CANNOT BE TRUE. ### ONE BANKED FILE, TWO OPPOSITE GRADES FOR ONE IMPORT',
              'THE CORRECTED GRADE, AND IT IS THE ONE THE NUMBERS SUPPORT',
              'THE BAR WAS NOT MOVED AND THE CELL WAS NOT DROPPED',
          ]) if bool(E['i1_failed'] == [100] and 1000 in E['i1_verified']
                     and 10 ** 7 in E['i1_verified']) else (
              'FAIL', '### I-1 range wrong: verified=%s failed=%s'
                      % (E['i1_verified'], E['i1_failed'])),
          # ### FIXTURE: claim I-1 passed at every cell. ### It failed at 1e2, and the bar
          # ### was fixed in the registration before any value existed.
          fixture=lambda: bool(E['i1_failed'] == []),
          witness=lambda: bool(len(E['i1_verified']) == 5))

    # 4 -- ### REPAIR (b) AND THE TWO DEFECTS FOUND WHILE REPAIRING, ALL FOUR DISCLOSED.
    h.run('repair-b-priced-and-all-four-defects-disclosed',
          check=lambda: verify_all(BANK, [
              'A REFUSAL THAT WAS ASSERTED RATHER THAN PRICED',
              'A REFUSAL INVENTED TO LOOK DISCIPLINED IS THE SAME CRIME WEARING THE OPPOSITE COAT',
              'THE PRINTED OUTPUT AND THE BANKED FILE DISAGREED',
              'A "DISCRIMINATOR" THAT WAS A THEOREM',
              'THE ESTIMATE WAS SOUND',
          ]) if bool(E['afford_1e8'] and rows[-1]['a2'] == 10 ** 8) else (
              'FAIL', '### 1e8 not priced-then-run'),
          # ### FIXTURE: claim the ladder stops at 1e7. ### The repair extended it after pricing.
          fixture=lambda: bool(rows[-1]['a2'] == 10 ** 7),
          witness=lambda: bool(E['afford_1e8']))

    # 5 -- ### THE CLOSED FORM IS THE INSTRUMENT. ### RUN BEFORE ANY ALL-PRIMES VALUE EXISTED.
    h.run('closed-form-is-the-instrument',
          check=lambda: bool(E['worst_grepro'] < 1e-12
                             and E['worst_grepro'] > 0.0
                             and contains(RUN, 'THE CLOSED FORM ### IS ### THE INSTRUMENT')
                             and contains(RUN, 'EVERY NUMBER BELOW IS VOID')),
          # ### FIXTURE: claim the two routes disagree beyond 1e-12. ### They agree to 2.6e-14.
          fixture=lambda: bool(E['worst_grepro'] > 1e-12),
          witness=lambda: bool(E['worst_grepro'] > 0.0))

    # 6 -- ### THE SCOPE WALL, COUNTED RATHER THAN CLAIMED.
    h.run('scope-wall-counted-not-claimed',
          check=lambda: verify_all(BANK, [
              'THE FAMILY THAT DECIDES J3 IS ABSENT FROM ### EVERY ### CELL',
              'THIS IS NOT A DEFECT IN b255, b260 OR b261',
              'THEY DECLARED THE WALL; THIS ACT MEASURES WHAT IS ON THE OTHER SIDE OF IT',
          ]) if bool(contains(RUN, 'THE SCOPE WALL, MEASURED')
                     and contains(SHADOW, 'eleven_is_in_the_top_family')
                     and contains(SHADOW, 'bench_primes_are_not_in_the_top_family')) else (
              'FAIL', '### scope-wall evidence missing from run or shadow'),
          # ### FIXTURE: b261's bank predates this finding entirely.
          fixture=lambda: contains(B261B, 'THE FAMILY THAT DECIDES J3'),
          witness=lambda: contains(RUN, 'ZERO ### n_p = 1 PRIMES'))

    # 7 -- ### (GROWS): SEVEN DECADES, ALL PRIMES, m=1 DOMINANT AT EVERY CELL.
    h.run('grows-across-seven-decades-with-m1-dominant',
          check=lambda: bool(len(rows) == 7
                             and all(rows[i + 1]['total'] > rows[i]['total']
                                     for i in range(len(rows) - 1))
                             and all(r['m1'] >= r['m2'] and r['m1'] >= r['m3plus']
                                     for r in rows[1:])
                             and all(rows[i + 1]['fixed'] < rows[i]['fixed']
                                     for i in range(len(rows) - 1))
                             and bool(E['grows']) and bool(E['m1dom'])
                             and contains(BANK, 'THE VERDICT: ### (GROWS)')),
          # ### FIXTURE: claim T_fixed grows too. ### It DECAYS, from 0.090425 to 0.004814 --
          # ### which is S2's derivation confirmed, and a gate that missed it would miss the
          # ### act's own internal consistency.
          fixture=lambda: bool(any(rows[i + 1]['fixed'] >= rows[i]['fixed']
                                   for i in range(len(rows) - 1))),
          witness=lambda: bool(len(rows) == 7))

    # 8 -- ### THE LABEL SETTLED BY DEFINITIONS, WITH BOTH LIMITS WRITTEN OUT.
    h.run('label-settled-by-definitions',
          check=lambda: verify_all(BANK, [
              'act 9\'s LEVEL LIMIT:** ### FIX `p`. ### FIX `k`. ### LET `n -> inf`',
              'THIS ACT\'S CUTOFF LIMIT:** ### LET `a^2 -> inf`',
              'DISTINCT OBJECTS WITH A STATED RELATION. ### NOT A DOUBLE-NAME',
              'THE LABEL IS CONFIRMED HERE, NOT CONTRADICTED',
              'DOUBLE-*LIMIT* ERROR',
          ]),
          # ### FIXTURE: b261's bank has no label section at all.
          fixture=lambda: contains(B261B, 'DISTINCT OBJECTS WITH A STATED RELATION'),
          witness=lambda: contains(FIL, 'double-limit-species'))

    # 9 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 11
                             and contains(PROF, 'ALL THREE REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and contains(SHADOW, 'fixed_level_bound_is_sharp')
                             and contains(SHADOW, 'top_level_fraction_is_one')
                             and contains(BANK, '11 TERMINALS, ZERO AXIOMS')),
          # ### FIXTURE: demand 12 terminals. ### There are 11. ### b261's defect -- an appended
          # ### summary restating the counted string -- was avoided and this gate proves it.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 12),
          witness=lambda: contains(PROF, 'import took'))

    # 10 -- ### THE NEW TOOL IS BUILT, USED, AND SHOWN ABLE TO SAY NO.
    h.run('needle-extract-built-used-and-discriminates',
          check=lambda: bool(os.path.isfile(TOOL)
                             and 'def verify_all' in py_code_only(TOOL)
                             and 'def extract' in py_code_only(TOOL)
                             # ### THE TOOL SAYS NO ON AN ABSENT NEEDLE, AND NAMES IT:
                             and verify_all(BANK, ['THIS SENTENCE IS NOT IN THE BANK'])[0] == 'FAIL'
                             and 'ABSENT' in verify_all(BANK, ['NOT IN THE BANK'])[1]
                             # ### AND SAYS YES ON A PRESENT ONE:
                             and verify_all(BANK, ['THE VERDICT: ### (GROWS)'])[0] == 'PASS'
                             and contains(FIL, 'W-ORD-NEEDLE-EXTRACT')),
          # ### FIXTURE: claim the tool passes an absent needle. ### It refuses it by name.
          fixture=lambda: bool(verify_all(BANK, ['THIS SENTENCE IS NOT IN THE BANK'])[0] == 'PASS'),
          witness=lambda: bool(verify_all(BANK, ['NOTHING DEPOSITS'])[0] == 'PASS'))

    # 11 -- ### NO INSTRUMENT EDITED; NOTHING STAGED UNDER THE PATENT TREE.
    h.run('instruments-unedited-and-patent-tree-untouched',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'def theta_quotient' not in py_code_only(SRC)
                             and 'import b38_act10' in py_code_only(SRC)
                             and 'patent-package' not in staged()
                             and 'PLACE-papers' not in staged()
                             and contains(FIL, 'BY EXPLICIT PATH AND RAN NO `git add -A`')),
          # ### FIXTURE: claim the run script redefines the instrument. ### It imports it.
          fixture=lambda: bool('def theta_quotient' in py_code_only(SRC)),
          witness=lambda: bool('def junction' in py_code_only(SRC)))

    # 12 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE, AND THE MEANING'S REACH IS BOUNDED.
    h.run('register-sentence-exact-and-meaning-bounded',
          check=lambda: verify_all(BANK, [
              'RH reduced to a single located clause, reduction machine-verified. h2 is the clause.',
              'IT IS NOT EVIDENCE AGAINST THE IDENTITY',
              'IT DOES NOT MOVE `h2`',
              'NOT A CLAIM THAT IT FAILS TO DO IT',
              'NOTHING DEPOSITS',
          ]) if bool('h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()) else (
              'FAIL', '### the bank asserts h2'),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
