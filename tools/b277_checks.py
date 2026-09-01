# -*- coding: utf-8 -*-
"""b277_checks.py -- M-2 CAMPAIGN, ACT 11. ### THE CONTROL SUITE.

### ### **EVERY OWNER NEEDLE IS PULLED FROM ITS EMITTING FILE** (`needle_pull.py`, standing).

### WHAT THIS GATE FILE CANNOT SEE:
###  (1) whether the tower whose closure is `S-bar_v` really is the `Son` tower -- ### that is
###      `W-ORD-SBAR-TOWER`, and the act's own bank says the block rests on an INFERENCE.
###  (2) whether the author should rule the block away. ### Not a gate's business.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 10 -- it tokenizes.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_pull import pull                  # noqa: E402

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b277_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b277_run.txt')
FIL = os.path.join(D, 'b277_aggregation_stated.txt')
SAT = os.path.join(D, 'audit_b277_reg_satisfiable.txt')
NEEDLES = os.path.join(D, 'b277_needles.json')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b277_aggregation_stated.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

NEEDLE_SPEC = [
    ('b198-i2', 'b198_nonvanishing.txt',
     'iota F-EQUIVARIANT, so each E_lam(S-bar) is the closure of its level tower'),
    ('b198-i4', 'b198_nonvanishing.txt', 'S-bar = the L^2-CLOSURE OF THE TOWER'),
    ('b198-goal', 'b198_nonvanishing.txt', 'IS NONZERO AT THE TOWER'),
    ('b226-c0i', 'b226_stated_choice.txt', '(i) a vector at every place'),
    ('b226-ell', 'b226_stated_choice.txt', 'ell(p) := 2 if p = 2'),
    ('b275-absent', 'b275_the_rule_stated.txt', 'NOT A WEAKENED PREMISE BUT AN ABSENT ONE'),
    ('b273-s2', 'b273_spec2_range.txt', 's^2 = -8/11'),
    ('b276-verdict', 'b276_size_equivalence_tension.txt',
     'THE DEMAND FORCES AN ORTHOGONAL OBJECT'),
    ('b262-div', 'b262_junction_limit.txt', 'THE JUNCTION DIVERGES ALONG THE CUTOFF LIMIT'),
    ('spec1', 'b267_registration_2026-08-31.txt', '(SPEC-1) IT COUNTS FIRST LEVELS'),
    ('b15', 'b15_2026-08-18.txt', 'finite-place-set object at a finite cutoff'),
]

FIXTURE_NEEDLES = [
    ('T1 FAILED', RUNNER),
    ('### NO ###', RUNNER),
    ('DOES NOT EQUAL act 9', RUNNER),
]


def needles_unpullable():
    bad = 0
    for lbl, f, a in NEEDLE_SPEC:
        try:
            pull(os.path.join(D, f), a)
        except LookupError:
            bad += 1
    return bad


def banked_needles_match():
    if not os.path.isfile(NEEDLES):
        return False
    banked = json.load(io.open(NEEDLES, encoding='utf-8'))
    for lbl, f, a in NEEDLE_SPEC:
        if banked.get(lbl) != pull(os.path.join(D, f), a):
            return False
    return True


def git_unchanged(rel, root=ROOT):
    return subprocess.run(['git', '-C', root, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def seal_ok():
    return subprocess.run([sys.executable, SEAL, '--verify', REG],
                          capture_output=True, text=True, cwd=ROOT).returncode == 0


def float_tokens_in_runner():
    import tokenize
    with open(RUNNER, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    return (sum(1 for t in toks if t.type == tokenize.NUMBER and '.' in t.string)
            + sum(1 for t in toks if t.type == tokenize.NAME
                  and t.string in ('float', 'numpy', 'np')))


def unreachable_fixtures():
    return [n for n, s in FIXTURE_NEEDLES if n not in io.open(s, encoding='utf-8').read()]


def new_lean_files():
    p = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                       capture_output=True, text=True)
    return sum(1 for ln in (p.stdout or '').splitlines() if ln.strip().endswith('.lean'))


def or_in_check_logic():
    import tokenize
    src = io.open(SELF, encoding='utf-8').read()
    spans = []
    for m in re.finditer(r'check=lambda:(.*?)fixture=', src, re.S):
        spans.append((src[:m.start(1)].count(chr(10)) + 1, src[:m.end(1)].count(chr(10)) + 1))
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
    h = Harness(ROOT, 'b277')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '6fd57ecde991a23964c460c963e26ae936af26cf50ebd370')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    h.run('F-NEEDLE-owner-needles-pulled-not-retyped',
          check=lambda: bool(needles_unpullable() == 0
                             and len(NEEDLE_SPEC) == 11
                             and banked_needles_match()),
          fixture=lambda: bool(needles_unpullable() > 0),
          witness=lambda: bool(os.path.isfile(NEEDLES)))

    h.run('component-0-in-the-path',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')),
          fixture=lambda: bool(contains(RUN, 'gate verdict : AT_FLOOR')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    h.run('rule-and-aggregation-written-whole-with-owners',
          check=lambda: bool(contains(RUN, 'EVERY CONSTITUENT UNFOLDED TO ITS OWNER')
                             and contains(RUN, 'Q_p(k) := <U^k S_quot')
                             and contains(RUN, '4q P_1 = (q + S)(1 + Pi)')),
          fixture=lambda: bool(contains(RUN, 'CONSTITUENT WITHOUT AN OWNER')),
          witness=lambda: bool(contains(RUN, 'd_1(2,1) = 0')))

    h.run('stated-value-closed-form-and-p2-under-its-own-branch',
          check=lambda: bool(contains(RUN, 'HOLDS AT EVERY ODD PLACE : CONFIRMED')
                             and contains(RUN, '63/199')
                             and contains(FIL, 'IS A NUMBER AT EVERY PLACE')
                             and contains(FIL, 'NOT INHERITED FROM THE ODD ONE')),
          fixture=lambda: bool(contains(RUN, 'T1 FAILED')),
          witness=lambda: bool(contains(RUN, 'closed form')))

    h.run('T1-T2-T3-T4a-all-pass',
          check=lambda: bool(contains(RUN, 'SPEC-1 holds at every odd place')
                             and contains(RUN, 'A VACUITY AND NOT A TRIUMPH')
                             and contains(RUN, 'THE AGGREGATION EQUALS act 9')
                             and contains(RUN, 'divided by its own norm')),
          fixture=lambda: bool(contains(RUN, 'DOES NOT EQUAL act 9')),
          witness=lambda: bool(contains(RUN, 'numerator - term * denominator = 0')))

    # ### THE BLOCK GATE.
    h.run('F-C0-block-located-and-quoted-at-its-owner',
          check=lambda: bool(contains(RUN, 'f_alpha in')
                             and contains(RUN, 'THE TOWER IS THE')
                             and contains(RUN, 'CLAUSE (i) IS UNWARRANTED')
                             and contains(FIL, 'THE FAILING CONDITION IS von Neumann')),
          fixture=lambda: bool(contains(FIL, 'CLAUSE (i) IS SATISFIED')),
          witness=lambda: bool(contains(RUN, 'in Son(p, ell(p))?')))

    h.run('F-STRENGTH-absent-warrant-not-proved-exclusion',
          check=lambda: bool(contains(FIL, 'IT IS NOT PROVED THAT')
                             and contains(FIL, 'NO WARRANT PLACES IT INSIDE')
                             and contains(FIL, 'MISSING ### , not false')
                             and contains(FIL, 'W-ORD-SBAR-TOWER')),
          # ### FIXTURE: the bank has DROPPED its qualification. ### A first draft looked for
          # ### 'PROVED THAT THE CANDIDATE LIES OUTSIDE' -- ### **WHICH IS A SUBSTRING OF THE
          # ### CORRECT SENTENCE 'IT IS NOT PROVED THAT ...', SO IT FIRED ON THE RIGHT TEXT.**
          # ### This one fires exactly when the negation is missing.
          fixture=lambda: bool(contains(FIL, 'IT IS NOT PROVED') is False),
          witness=lambda: bool(contains(FIL, 'A GOOD ONE, AND STILL AN INFERENCE')))

    h.run('F-NORECIP-prior-acts-stand-and-C2-C3-untouched',
          check=lambda: bool(contains(FIL, 'AND THAT IS NOT A RE-VERDICT OF THOSE ACTS')
                             and contains(FIL, 'NONE OF THEM WAS')
                             and contains(FIL, 'THEY BOTH WORK')),
          fixture=lambda: bool(contains(FIL, 'b271 WAS WRONG')),
          witness=lambda: bool(contains(FIL, 'never leave')))

    h.run('F-NOFIT-size-control-no-fit-and-imports-restated',
          check=lambda: bool(contains(RUN, 'NO FIT IS MADE AND NONE IS BANKED')
                             and contains(FIL, 'THE AGGREGATE DIVERGES')
                             and contains(FIL, 'IMPORTS, NOT HELD RESULTS')
                             and not contains(RUN, 'residual')),
          fixture=lambda: bool(contains(RUN, 'residual')),
          witness=lambda: bool(contains(FIL, 'still an object with no warranted home')))

    h.run('no-float-no-shadow-owners-intact-fixtures-reachable-no-or',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and new_lean_files() == 0
                             and contains(FIL, 'NOTHING DEPOSITS')
                             and git_unchanged('data/b276_size_equivalence_tension.txt')
                             and git_unchanged('data/b198_nonvanishing.txt')
                             and len(unreachable_fixtures()) == 0
                             and or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 10),
          fixture=lambda: bool(float_tokens_in_runner() > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 10))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  owner needles PULLED : %d ; unpullable : %d'
          % (len(NEEDLE_SPEC), needles_unpullable()))
    print('  banked pulls still match live owners : %s' % banked_needles_match())
    print('  float tokens in the deciding runner : %d' % float_tokens_in_runner())
    print('  unreachable fixture needles : %d of %d'
          % (len(unreachable_fixtures()), len(FIXTURE_NEEDLES)))
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or`: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
