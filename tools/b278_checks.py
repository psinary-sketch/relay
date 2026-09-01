# -*- coding: utf-8 -*-
"""b278_checks.py -- M-2 CAMPAIGN, ACT 12. ### THE CONTROL SUITE.

### ### **EVERY OWNER NEEDLE IS PULLED; EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY OR
### ### AN EXACT VALUE, NEVER A SUBSTRING.** ### b277 shipped a fixture whose string was a
### SUBSTRING of the correct sentence, so it fired on correctness and refused a good check.
### `absent_exact` closes that species by comparing WHOLE LINES.

### WHAT THIS GATE FILE CANNOT SEE:
###  (1) whether some act it did not search DOES construct `S-bar_v`. ### That is
###      `W-ORD-SBAR-TOWER`, and the bank says so in its own words.
###  (2) which reading is the right one. ### Not a gate's business, and not this act's.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 11 -- it tokenizes.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains          # noqa: E402
from needle_pull import pull, present_exact, absent_exact   # noqa: E402

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b278_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b278_run.txt')
FIL = os.path.join(D, 'b278_space_level_barrier.txt')
SAT = os.path.join(D, 'audit_b278_reg_satisfiable.txt')
NEEDLES = os.path.join(D, 'b278_needles.json')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b278_space_barrier.py')
PULLER = os.path.join(ROOT, 'tools', 'needle_pull.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

NEEDLE_SPEC = [
    ('b21-foot', 'b21_2026-08-18.txt', 'nothing here constructs a limit object'),
    ('b21-Vn', 'b21_2026-08-18.txt', 'V_n = { f : supp f in p^(-n) Z_p'),
    ('b21-honest', 'b21_2026-08-18.txt', 'an honest finite-dimensional subspace of L^2(Q_p)'),
    ('b198-i4', 'b198_nonvanishing.txt', 'S-bar = the L^2-CLOSURE OF THE TOWER'),
    ('b198-i2', 'b198_nonvanishing.txt',
     'iota F-EQUIVARIANT, so each E_lam(S-bar) is the closure of its level tower'),
    ('b226-son', 'b226_stated_choice.txt', 'vanishing on a ball AND on its transform image'),
    ('b226-sbar', 'b226_stated_choice.txt', 'the L^2-closure of the tower'),
    ('b270-absorb', 'b270_ambient_pairing_properties.txt', 'EVERY SUMMAND CARRIES THE FACTOR'),
    ('b276-bound', 'b276_size_equivalence_tension.txt', 'EXACTLY QUADRATIC'),
    ('b277-block', 'b277_aggregation_stated.txt', 'NO WARRANT PLACES IT INSIDE'),
    ('spec1', 'b267_registration_2026-08-31.txt', '(SPEC-1) IT COUNTS FIRST LEVELS'),
    ('b15', 'b15_2026-08-18.txt', 'finite-place-set object at a finite cutoff'),
]

# ### MUST-FAIL FIXTURES, EACH A WHOLE LINE THAT MUST BE ABSENT. ### **NOT A SUBSTRING.**
ABSENT_LINES = [
    (RUN, '### **FIBER LEMMA FAILED**'),
    (FIL, '### THE BARRIER HOLDS, DERIVED, UNCONDITIONALLY.'),
    (FIL, '### THE CORPUS DEFINES S-bar_v OUTRIGHT.'),
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


def absent_exact_both_polarities():
    """### `absent_exact` CONTROLLED IN BOTH DIRECTIONS ON A REAL LINE FROM A REAL FILE.
    ### ### **THE NEGATIVE POLARITY IS b277's OWN INVERTED-FIXTURE STRING: A SUBSTRING OF A
    ### ### CORRECT SENTENCE, WHICH MUST COME BACK ABSENT AS A WHOLE LINE.**"""
    src = os.path.join(D, 'b277_aggregation_stated.txt')
    real = pull(src, 'NO WARRANT PLACES IT INSIDE')
    pos = present_exact(src, real)                      # ### the whole line IS present
    neg = absent_exact(src, 'PROVED THAT THE CANDIDATE LIES OUTSIDE')   # ### substring: ABSENT
    return pos, neg


def all_absent_hold():
    return all(absent_exact(f, ln) for f, ln in ABSENT_LINES)


def substring_fixtures_in_self():
    """### F-FIXTURE, MECHANIZED. ### Counts `fixture=` bodies that call `contains(` -- the
    ### substring primitive. ### **THIS ACT'S MUST-FAIL FIXTURES MUST USE `absent_exact` OR AN
    ### EXACT VALUE, SO THIS COUNT MUST BE ZERO.**"""
    src = io.open(SELF, encoding='utf-8').read()
    n = 0
    for m in re.finditer(r'fixture=lambda:(.*?)(?:witness=|\)\))', src, re.S):
        if 'contains(' in m.group(1):
            n += 1
    return n


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
    h = Harness(ROOT, 'b278')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '763f29ea19e73ca505ddcf08becbff4fd459412beeb27b47')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(absent_exact(SAT, 'JOINTLY SATISFIABLE') is False
                               and absent_exact(SAT, '  VERDICT          : ### NOT SATISFIABLE')
                               is False),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    h.run('F-NEEDLE-and-F-SELFNEEDLE-pulled-not-typed',
          check=lambda: bool(needles_unpullable() == 0
                             and len(NEEDLE_SPEC) == 12
                             and banked_needles_match()
                             and 'pull_self' in io.open(PULLER, encoding='utf-8').read()),
          fixture=lambda: bool(needles_unpullable() > 0),
          witness=lambda: bool(os.path.isfile(NEEDLES)))

    # ### THE TOOLING DISCHARGE, CONTROLLED IN BOTH POLARITIES.
    h.run('F-FIXTURE-absent-exact-both-polarities-and-no-substring-fixtures',
          check=lambda: bool(absent_exact_both_polarities() == (True, True)
                             and substring_fixtures_in_self() == 0
                             and all_absent_hold()),
          fixture=lambda: bool(substring_fixtures_in_self() > 0),
          witness=lambda: bool(len(ABSENT_LINES) == 3))

    h.run('component-0-in-the-path',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')),
          fixture=lambda: bool(absent_exact(RUN, '  gate verdict : EXACT')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    h.run('tower-ABSENT-with-a-positive-control-on-the-absence',
          check=lambda: bool(contains(RUN, 'lines in data/ mentioning')
                             and contains(RUN, 'NOT ONE OF THEM DEFINES THE TOWER')
                             and contains(RUN, 'nothing here constructs a limit object')
                             and contains(FIL, 'A CITATION CHAIN THAT TERMINATES IN AN UNFILLED')),
          fixture=lambda: bool(absent_exact(FIL,
                               '### THE CORPUS DEFINES S-bar_v OUTRIGHT.') is False),
          witness=lambda: bool(contains(RUN, 'DEFINITION-SHAPED')))

    h.run('F-BALL-son-ball-equals-absorption-set-as-sets',
          check=lambda: bool(contains(RUN, 'THE SAME SET AT EVERY CELL')
                             and contains(RUN, 'NOT from the name `ball`')
                             and contains(FIL, 'BOTH HALVES')),
          # ### WHOLE-LINE, NOT A SUBSTRING: the exact line the runner emits if they differ.
          fixture=lambda: bool(absent_exact(RUN,
                               '### **BALL IDENTITY VERDICT: ### THE BALLS DIFFER -- '
                               'THE DERIVATION HALTS HERE ###**') is False),
          witness=lambda: bool(contains(RUN, "|Son's ball|")))

    h.run('F-BIVALENT-both-readings-derived-and-neither-picked',
          check=lambda: bool(contains(RUN, 'THE BARRIER HOLDS UNDER')
                             and contains(RUN, 'THE BARRIER IS REFUTED')
                             and contains(RUN, 'OPPOSITE ANSWERS')
                             and contains(FIL, 'THAT BIVALENCE IS THIS ACT')),
          fixture=lambda: bool(absent_exact(FIL,
                               '### THE BARRIER HOLDS, DERIVED, UNCONDITIONALLY.') is False),
          witness=lambda: bool(contains(RUN, '4(N-q)')))

    h.run('F-NOASSERT-conditional-barrier-refused-with-a-reason',
          check=lambda: bool(contains(FIL, 'WHY (UNDECIDED) AND NOT (BARRIER-CONDITIONAL)')
                             and contains(FIL, 'DRESSED AS A CONDITION')
                             and contains(FIL, 'REFUSE IT RATHER THAN FORMAT IT')),
          fixture=lambda: bool(absent_exact(FIL,
                               '### THE BARRIER HOLDS, DERIVED, UNCONDITIONALLY.') is False),
          witness=lambda: bool(contains(FIL, 'not caution')))

    h.run('F-CONSOL-five-acts-as-instances-with-banks-untouched',
          check=lambda: bool(contains(RUN, 'FIVE INSTANCES OF ONE THEOREM')
                             and contains(FIL, 'IT DOES NOT CORRECT ANYTHING INSIDE')
                             and git_unchanged('data/b270_ambient_pairing_properties.txt')
                             and git_unchanged('data/b273_spec2_range.txt')
                             and git_unchanged('data/b275_the_rule_stated.txt')
                             and git_unchanged('data/b277_aggregation_stated.txt')
                             and git_unchanged('data/b21_2026-08-18.txt')),
          fixture=lambda: bool(git_unchanged('data/b277_aggregation_stated.txt') is False),
          witness=lambda: bool(contains(FIL, 'ADDS A SENTENCE ABOVE THEM')))

    h.run('scope-C2-C3-untouched-and-no-overclaim-about-the-space',
          check=lambda: bool(contains(FIL, 'NOTHING ABOUT C2 OR C3')
                             and contains(FIL, 'NO CLAIM THAT `S-bar_v` CANNOT BE DEFINED')
                             and contains(FIL, 'W-ORD-SBAR-TOWER')),
          fixture=lambda: bool(absent_exact(FIL,
                               '### S-bar_v CANNOT BE DEFINED.') is False),
          witness=lambda: bool(contains(FIL, 'BINDING')))

    h.run('no-float-no-shadow-fixtures-clean-no-or',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and new_lean_files() == 0
                             and contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')
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
    print('  absent_exact both polarities (present, absent) : %s'
          % (absent_exact_both_polarities(),))
    print('  substring-based must-fail fixtures : %d' % substring_fixtures_in_self())
    print('  float tokens in the deciding runner : %d' % float_tokens_in_runner())
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or`: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
