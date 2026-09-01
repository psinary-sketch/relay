# -*- coding: utf-8 -*-
"""b274_checks.py -- M-2 CAMPAIGN, ACT 8. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE:
###  (1) whether the low-side ALGEBRA is valid -- it RE-DERIVES the inequality independently and
###      checks the proof's steps are stated; ### **THE PROSE PROOF IS NOT MECHANIZED HERE.**
###  (2) whether the high side is true where it is UNCERTIFIED -- that is
###      `W-ORD-ORDER-CHANNEL`, and no gate here bears on it.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 11 -- it tokenizes.
"""
import io
import os
import re
import subprocess
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b274_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b274_run.txt')
FIL = os.path.join(D, 'b274_straddle_generally.txt')
SAT = os.path.join(D, 'audit_b274_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b274_straddle_generally.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

QUOTES = [
    ('b273_spec2_range.txt', "R(g_0) = 3/10"),
    ('b273_spec2_range.txt', "`R(w) = (1 + 2^{1/2})/3`"),
    ('b273_spec2_range.txt', "(ATTAINABLE), AT `(2,2)`, `k = 1`, IN THE AMBIENT `E_1`."),
    ('b273_spec2_range.txt', "(SPEC-3) NOT TESTED AT ALL"),
    ('b273_spec2_range.txt', "HERE `<u, w> != 0`, VERIFIED EXACTLY"),
    ('b272_escape_class.txt',
     "`g_c := 4q P_1 e_c`,  `g_c(m) = q([m = c] + [m = -c]) + zeta^{mc} + zeta^{-mc}`."),
    ('b270_ambient_pairing_properties.txt', "EVERY SUMMAND CARRIES THE FACTOR"),
    ('b267_aggregation_source.txt',
     "tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1) ### for 1 <= k <= n-1, 0 for k >= n. QED"),
    ('b223_level_limit_two_places.txt',
     "2   2     4       16          9                 32          2          2     YES"),
    ('b226_stated_choice.txt', "4q P_1   = (q + S)(1 + Pi)"),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b15_2026-08-18.txt', "a finite-place-set object at a finite cutoff decides nothing"),
]

FIXTURE_NEEDLES = [
    ('S1 CLOSED FORM FAILED', RUNNER),
    ('LOW SIDE FAILED', RUNNER),
]


def git_unchanged(rel, root=ROOT):
    return subprocess.run(['git', '-C', root, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def seal_ok():
    return subprocess.run([sys.executable, SEAL, '--verify', REG],
                          capture_output=True, text=True, cwd=ROOT).returncode == 0


def quotes_missing():
    return sum(1 for f, n in QUOTES
               if verify_all(os.path.join(D, f), [n])[0] != 'PASS')


def low_side_oracle():
    """### AN INDEPENDENT RE-DERIVATION OF THE LOW-SIDE INEQUALITY, OVER THE GATE'S OWN SWEEP.
    ### **THE GATE DOES NOT READ THE RUN'S ANSWER HERE. ### A GATE THAT RE-READ THE RUN WOULD BE
    ### CHECKING THAT A FILE SAYS WHAT IT SAYS.**"""
    bad = 0
    tot = 0
    for p in (2, 3, 5, 7, 11, 13, 37, 101):
        for n in range(2, 10):
            q = p ** n
            for k in range(1, n):
                tot += 1
                if not (Fraction(q - 1, 2 * (q + 1)) < Fraction(q - p ** k, q - 1)):
                    bad += 1
    return tot, bad


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
    h = Harness(ROOT, 'b274')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '3abf4af92a283b01d9cb82b4cd952638ce616959d233d786')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    h.run('twelve-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 12),
          fixture=lambda: bool(verify_all(os.path.join(D, 'b273_spec2_range.txt'),
                                          ['THE STRADDLE IS GENERAL'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 12))

    h.run('component-0-in-the-path',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')),
          fixture=lambda: bool(contains(RUN, 'gate verdict : AT_FLOOR')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    h.run('S1-closed-form-derived-and-controlled',
          check=lambda: bool(contains(RUN, 'R(g_0) = 4q(q-1)')
                             and contains(RUN, 'banked 3/10 : CONFIRMED')
                             and contains(RUN, 'the closed form holds exactly')),
          fixture=lambda: bool(contains(RUN, 'S1 CLOSED FORM FAILED')),
          witness=lambda: bool(contains(RUN, 'INDEPENDENT OF k')))

    h.run('low-side-independently-re-derived-by-the-gate',
          check=lambda: bool(low_side_oracle()[1] == 0
                             and low_side_oracle()[0] >= 250
                             and contains(RUN, 'term failed in : 0 cases')
                             and contains(FIL, '3q - 1 > 0')),
          fixture=lambda: bool(low_side_oracle()[1] > 0),
          witness=lambda: bool(low_side_oracle()[0] >= 250))

    h.run('S2-family-in-Son-and-uncertified-not-false',
          check=lambda: bool(contains(RUN, 'w_c LIES IN Son(p,n)')
                             and contains(RUN, 'UNCERTIFIED ### : 7 OF 7')
                             and contains(RUN, 'IS NOT SHOWN TO FAIL EITHER')
                             and contains(FIL, 'NOT THE SAME AS FALSE')),
          fixture=lambda: bool(contains(FIL, 'THE FAMILY IS REFUTED')),
          witness=lambda: bool(contains(RUN, 'ESCAPE CLASS')))

    h.run('level-1-vacuity-and-the-ruled-choice-observation',
          check=lambda: bool(contains(RUN, 'VACUOUS')
                             and contains(RUN, 'THE ONLY CELL WITH ANY (SPEC-2) CONTENT AT ALL IS')
                             and contains(FIL, 'DOUBLE-NAME SPECIES AT THE LEVEL OF CELLS')),
          fixture=lambda: bool(contains(FIL, 'EVERY CELL CARRIES SPEC-2 CONTENT')),
          witness=lambda: bool(contains(RUN, 'LEVEL 1, STATED AND NOT SKIPPED')))

    h.run('SPEC-3-status-and-attainability-distinguished',
          check=lambda: bool(contains(FIL, 'NOT ADVANCED BY THIS ACT')
                             and contains(FIL, 'AN ATTAINABLE RANGE IS NOT A STATED AGGREGATION')
                             and contains(FIL, 'W-ORD-EQUIV-CLASS')),
          fixture=lambda: bool(contains(FIL, 'SPEC-3 IS SATISFIED')),
          witness=lambda: bool(contains(FIL, 'THAT IS THE WHOLE DISTANCE STILL TO GO')))

    # ### THE DEVIATION GATE. ### The exploration produced numbers that do not exist, and the
    # ### bank must say so without softening.
    h.run('D1-truncated-print-misread-declared-without-softening',
          check=lambda: bool(contains(FIL, 'NUMBERS THAT DO')
                             and contains(FIL, 'LUCK, NOT ACCURACY')
                             and contains(FIL, 'A PRINT WIDTH IS NOT A DATUM')
                             and contains(FIL, 'AND THE NUMBERS DID NOT')),
          fixture=lambda: bool(contains(FIL, 'THE EXPLORATION WAS CORRECT THROUGHOUT')),
          witness=lambda: bool(contains(FIL, 'THE SEALED REGISTRATION IS NOT')))

    h.run('F-NOFLOAT-and-no-shadow-and-owners-intact',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and new_lean_files() == 0
                             and contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')
                             and git_unchanged('data/b273_spec2_range.txt')
                             and git_unchanged('tools/e16/b273_spec2_range.py')),
          fixture=lambda: bool(float_tokens_in_runner() > 0),
          witness=lambda: bool(contains(FIL, 'RESIDUES ENUMERATED')))

    h.run('every-fixture-needle-reachable-and-no-or-in-logic',
          check=lambda: bool(len(unreachable_fixtures()) == 0
                             and or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 10),
          fixture=lambda: bool(len(unreachable_fixtures()) > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 10))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  quotations verified verbatim : %d of %d unfindable' % (quotes_missing(), len(QUOTES)))
    t, b = low_side_oracle()
    print('  low-side oracle : %d triples re-derived independently, %d failures' % (t, b))
    print('  float tokens in the deciding runner : %d' % float_tokens_in_runner())
    print('  unreachable fixture needles : %d of %d'
          % (len(unreachable_fixtures()), len(FIXTURE_NEEDLES)))
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or`: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
