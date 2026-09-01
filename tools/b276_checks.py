# -*- coding: utf-8 -*-
"""b276_checks.py -- M-2 CAMPAIGN, ACT 10. ### THE CONTROL SUITE.

### ### **EVERY OWNER NEEDLE IN THIS FILE IS PULLED FROM ITS EMITTING FILE BY `needle_pull.py`,
### ### NOT RETYPED** (`W-ORD-NEEDLE-SOURCE`). ### b273, b274 and b275 each lost a gate to a
### needle typed from memory; ### **THIS FILE CANNOT MAKE THAT ERROR BECAUSE IT NEVER TYPES ONE.**

### WHAT THIS GATE FILE CANNOT SEE:
###  (1) whether the level-1 PROOF of the fiber lemma is valid -- it checks the 185-vector
###      control and that the proof is stated; ### **THE PROSE PROOF IS NOT MECHANIZED HERE.**
###  (2) whether b262's target is right -- ### that is b262's, quoted and not re-derived.
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
REG = os.path.join(D, 'b276_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b276_run.txt')
FIL = os.path.join(D, 'b276_size_equivalence_tension.txt')
SAT = os.path.join(D, 'audit_b276_reg_satisfiable.txt')
NEEDLES = os.path.join(D, 'b276_needles.json')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b276_size_equivalence.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

# ### THE OWNER NEEDLES, AS (label, file, ANCHOR). ### The anchor is short; the NEEDLE is what
# ### the file emitted, and it is pulled at run time.
NEEDLE_SPEC = [
    ('vN-332', 'b226_stated_choice.txt', 'Two C0-sequences'),
    ('vN-411', 'b226_stated_choice.txt', 'MUTUALLY ORTHOGONAL'),
    ('b272-orth', 'b272_escape_class.txt', 'EXACTLY, AT EVERY PLACE'),
    ('b273-s2', 'b273_spec2_range.txt', 's^2 = -8/11'),
    ('b274-R', 'b274_straddle_generally.txt', '(q-1)/(2(q+1)) < (q - p^k)/(q - 1)'),
    ('b275-orth', 'b275_the_rule_stated.txt', 'MUTUALLY ORTHOGONAL'),
    ('b262-div', 'b262_junction_limit.txt', 'THE JUNCTION DIVERGES ALONG THE CUTOFF LIMIT'),
    ('b262-carry', 'b262_junction_limit.txt', 'THOSE PRIMES CARRY THE WHOLE GROWTH'),
    ('b262-notagainst', 'b262_junction_limit.txt', 'IT IS NOT EVIDENCE AGAINST THE IDENTITY'),
    ('spec1', 'b267_registration_2026-08-31.txt', '(SPEC-1) IT COUNTS FIRST LEVELS'),
    ('b15', 'b15_2026-08-18.txt', 'finite-place-set object at a finite cutoff'),
]

FIXTURE_NEEDLES = [
    ('FIBER LEMMA FAILED', RUNNER),
    ('### NO ###', RUNNER),
]


def pulled():
    """### PULL EVERY OWNER NEEDLE FROM ITS EMITTING FILE. ### Raises loudly if one is gone."""
    return {lbl: pull(os.path.join(D, f), a) for lbl, f, a in NEEDLE_SPEC}


def needles_unpullable():
    bad = 0
    for lbl, f, a in NEEDLE_SPEC:
        try:
            pull(os.path.join(D, f), a)
        except LookupError:
            bad += 1
    return bad


def banked_needles_match():
    """### THE ACT BANKED ITS PULLS. ### They must still match what the owners emit TODAY."""
    if not os.path.isfile(NEEDLES):
        return False
    banked = json.load(io.open(NEEDLES, encoding='utf-8'))
    live = pulled()
    return all(banked.get(k) == v for k, v in live.items())


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
    h = Harness(ROOT, 'b276')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, 'a600dd93ed798bd63d3a358b94494536791ca9c6763c4f29')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    # ### W-ORD-NEEDLE-SOURCE, DISCHARGED AND GATED.
    h.run('F-NEEDLE-every-owner-needle-pulled-not-retyped',
          check=lambda: bool(needles_unpullable() == 0
                             and len(NEEDLE_SPEC) == 11
                             and banked_needles_match()
                             and contains(FIL, 'DISCHARGED BY DOING IT')),
          fixture=lambda: bool(needles_unpullable() > 0),
          witness=lambda: bool(os.path.isfile(NEEDLES)))

    h.run('component-0-in-the-path',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')),
          fixture=lambda: bool(contains(RUN, 'gate verdict : AT_FLOOR')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    h.run('S1-parameterization-derived-not-posited',
          check=lambda: bool(contains(RUN, 'E_1(Son) IS PRECISELY THE BALL-VANISHING PART OF E_1')
                             and contains(FIL, 'not a choice of form but')),
          fixture=lambda: bool(contains(FIL, 'WE POSIT THE FORM')),
          witness=lambda: bool(contains(RUN, 'THE SIZE IS')))

    # ### THE LOAD-BEARING GATE.
    h.run('F-LEMMA-fiber-lemma-verified-and-proved-at-level-1',
          check=lambda: bool(contains(RUN, 'W(b) = 0 EVERYWHERE')
                             and contains(RUN, '185 ball-vanishing vectors tested')
                             and contains(FIL, 'EVERY `pr` IS A MULTIPLE OF `p`, HENCE A BALL')
                             and contains(FIL, 'FULLY VERIFIED AT `(2,2)`')),
          fixture=lambda: bool(contains(RUN, 'FIBER LEMMA FAILED')),
          witness=lambda: bool(contains(RUN, 'SCOPE, PRINTED NOT ELIDED')))

    h.run('F-CONTROL-b273-and-b275-recovered-exactly',
          check=lambda: bool(contains(RUN, 'REDUCES TO 48 <= 160')
                             and contains(RUN, 'CONFIRMED')
                             and contains(FIL, 'three acts\' arithmetic')),
          fixture=lambda: bool(contains(RUN, '### FAILED ###')),
          witness=lambda: bool(contains(RUN, 'NEVER ITS EVIDENCE')))

    h.run('F-SPLIT-argument-from-summability-not-boundedness',
          check=lambda: bool(contains(RUN, 'A CONVERGENT')
                             and contains(RUN, 'HOWEVER MANY TERMS THE WINDOW HOLDS')
                             and contains(FIL, 'IT MAKES THEM ### SUMMABLE ###')
                             and contains(FIL, 'WHICH IS STRICTLY')),
          fixture=lambda: bool(contains(FIL, 'A MERELY BOUNDED CONTRIBUTION SUFFICES')),
          witness=lambda: bool(contains(FIL, 'THIS ACT\'S CENTRAL CARE')))

    h.run('F-TARGET-b262-quoted-never-refitted',
          check=lambda: bool(contains(FIL, 'QUOTED, NEVER RE-DERIVED HERE, AND NEVER FITTED TO')
                             and contains(FIL, 'ZERO FITS AND ZERO RESIDUALS')
                             and not contains(RUN, 'residual')),
          fixture=lambda: bool(contains(RUN, 'residual')),
          witness=lambda: bool(contains(FIL, 'THE JUNCTION DIVERGES')))

    h.run('F-SCOPE-not-a-refutation-and-C2-C3-untouched',
          check=lambda: bool(contains(FIL, 'IT IS NOT A REFUTATION OF THE IDENTITY')
                             and contains(FIL, 'C2 and C3 are not vector states')
                             and contains(FIL, 'IT DOES NOT SAY NO SEQUENCE SUPPLIES THE MASS')),
          fixture=lambda: bool(contains(FIL, 'THE IDENTITY IS REFUTED')),
          witness=lambda: bool(contains(FIL, 'MUTUALLY EXCLUSIVE')))

    h.run('selection-note-promoted-with-its-scope',
          check=lambda: bool(contains(FIL, 'PROMOTES FROM PATTERN GRADE TO A')
                             and contains(FIL, 'THE SCOPE IS THE WHOLE OF THE PROMOTION')
                             and contains(FIL, 'IT IS NOT DERIVED FOR C2 OR C3')),
          fixture=lambda: bool(contains(FIL, 'THE NOTE IS NOW PROVED IN GENERAL')),
          witness=lambda: bool(contains(FIL, 'FORCED, NOT CHOSEN')))

    h.run('no-float-no-shadow-owners-intact-fixtures-reachable-no-or',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and new_lean_files() == 0
                             and contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')
                             and git_unchanged('data/b275_the_rule_stated.txt')
                             and git_unchanged('data/b262_junction_limit.txt')
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
    print('  owner needles PULLED from emitting files : %d ; unpullable : %d'
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
