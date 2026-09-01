# -*- coding: utf-8 -*-
"""b275_checks.py -- M-2 CAMPAIGN, ACT 9. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE:
###  (1) whether the rule SHOULD be adopted -- ### that is not a gate's business.
###  (2) whether b273's `v` is equivalent to b226's sequence -- `W-ORD-EQUIV-CLASS`.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 10 -- it tokenizes.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b275_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b275_run.txt')
FIL = os.path.join(D, 'b275_the_rule_stated.txt')
SAT = os.path.join(D, 'audit_b275_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b275_the_rule_stated.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

QUOTES = [
    ('b274_straddle_generally.txt',
     "SO UNDER THE RULED CHOICE THE ONLY CELL IN THE WHOLE AGGREGATION WITH ANY (SPEC-2)"),
    ('b272_escape_class.txt',
     "`g_c(0) = 2` FOR EVERY `c != 0` AND `2q + 2` AT `c = 0`. ### AND `0` IS IN THE BALL."),
    ('b272_escape_class.txt', "SO `<u, g_0> = 0` EXACTLY, AT EVERY PLACE."),
    ('b271_top_level_no_go.txt',
     "THEY AGREE, SO `S g = q g`. ### VERIFIED EXACTLY AT ALL EIGHT CELLS."),
    ('b273_spec2_range.txt', "(ATTAINABLE), AT `(2,2)`, `k = 1`, IN THE AMBIENT `E_1`."),
    ('b268_generator_nonvanishing.txt',
     "SO THE ZERO SET IS EXACTLY THE `q` MULTIPLES OF `q`, AND `support(u_p) = N - q`."),
    ('b226_stated_choice.txt', "ell(p) := 2 if p = 2, else 1"),
    ('b226_stated_choice.txt',
     "THEREFORE SUM_v | ||u_v|| - 1 | = SUM_v 0 = ### **0**, which converges."),
    ('b226_stated_choice.txt',
     "THE CANONICITY OF THIS CHOICE IS ### **A DEFINITION MADE BY RULING, NOT A THEOREM.**"),
    ('b226_stated_choice.txt',
     'the incomplete products for DIFFERENT classes are "MUTUALLY ORTHOGONAL".'),
    ('b226_stated_choice.txt', "Two C0-sequences ... are ### EQUIVALENT ... if and only if"),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b15_2026-08-18.txt', "a finite-place-set object at a finite cutoff decides nothing"),
]

FIXTURE_NEEDLES = [
    ('T1 FAILED', RUNNER),
    ('UNEXPECTEDLY AGREES', RUNNER),
    ('FAILED ###', RUNNER),
]


def git_unchanged(rel, root=ROOT):
    return subprocess.run(['git', '-C', root, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def seal_ok():
    return subprocess.run([sys.executable, SEAL, '--verify', REG],
                          capture_output=True, text=True, cwd=ROOT).returncode == 0


def quotes_missing():
    return sum(1 for f, n in QUOTES if verify_all(os.path.join(D, f), [n])[0] != 'PASS')


def canonical_oracle():
    """### AN INDEPENDENT RE-DERIVATION OF THE CANONICAL INDEX. ### The gate recomputes the
    ### fixed-point sets itself rather than reading the run's table. ### Returns
    ### (cells, scaling-sets-that-are-not-{0}, Pi-sets-that-are-not-{0})."""
    cells = [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]
    bad_scal = 0
    pi_multi = 0
    for p, ell in cells:
        N = (p ** ell) ** 2
        if [m for m in range(N) if (p * m) % N == m] != [0]:
            bad_scal += 1
        if [m for m in range(N) if (-m) % N == m] != [0]:
            pi_multi += 1
    return len(cells), bad_scal, pi_multi


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
    h = Harness(ROOT, 'b275')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '6257f01aeef834ad378b87b6b80197ad22c11ea480ee764b')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    h.run('thirteen-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 13),
          fixture=lambda: bool(verify_all(os.path.join(D, 'b272_escape_class.txt'),
                                          ['THE RULE IS ADOPTED'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 13))

    h.run('component-0-in-the-path',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')),
          fixture=lambda: bool(contains(RUN, 'gate verdict : AT_FLOOR')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    # ### THE GATE RE-DERIVES CANONICITY ITSELF RATHER THAN READING THE RUN'S TABLE.
    h.run('F-CANON-index-derived-and-the-weaker-argument-shown-to-fail',
          check=lambda: bool(canonical_oracle()[1] == 0
                             and canonical_oracle()[2] > 0
                             and contains(RUN, 'THAT FORCES c = 0')
                             and contains(FIL, 'Pi` DOES NOT SINGLE OUT `0` THERE')),
          fixture=lambda: bool(canonical_oracle()[1] > 0),
          witness=lambda: bool(canonical_oracle()[0] == 8))

    h.run('the-rule-written-whole-with-owners',
          check=lambda: bool(contains(RUN, "u'_p := 4q P_1 e_0")
                             and contains(RUN, 'EVERY CONSTITUENT UNFOLDED TO ITS OWNER')
                             and contains(RUN, '4q P_1 = (q + S)(1 + Pi)')),
          fixture=lambda: bool(contains(RUN, 'CONSTITUENT WITHOUT AN OWNER')),
          witness=lambda: bool(contains(RUN, 'arrival depth')))

    h.run('T1-spec-1-derived-and-controlled',
          check=lambda: bool(contains(RUN, 'SPEC-1 holds under the rule at every cell')
                             and contains(RUN, 'NONZERO AT EVERY PLACE, BY ARITHMETIC AND NOT BY')
                             and contains(FIL, '48, 24, 80, 168, 440, 624, 1088, 1368')),
          fixture=lambda: bool(contains(RUN, 'T1 FAILED')),
          witness=lambda: bool(contains(RUN, 'MATCHES')))

    h.run('T2-vacuity-named-and-the-rule-fails-at-2-2',
          check=lambda: bool(contains(RUN, 'A VACUITY AND NOT A TRIUMPH')
                             and contains(RUN, 'FAILS, as registered')
                             and contains(FIL, 'THEY ARE DIFFERENT VECTORS')
                             and contains(FIL, 'MUST BE ### PIECEWISE ###')),
          fixture=lambda: bool(contains(RUN, 'UNEXPECTEDLY AGREES')),
          witness=lambda: bool(contains(RUN, 'R(g_0) = 3/10')))

    h.run('T3-T4-pass-with-the-level-exception-attributed',
          check=lambda: bool(contains(RUN, 'CONFIRMED at all cells')
                             and contains(RUN, "THE CORPUS'S OWN")
                             and contains(RUN, 'd_1(2,1) = 0')
                             and contains(FIL, 'the same standard b226 met')),
          fixture=lambda: bool(contains(FIL, 'G-NORM IS NOT MET')),
          witness=lambda: bool(contains(RUN, 'SUM_v 0 = 0')))

    # ### THE ACT'S SHARPEST CLAIM, AND ITS HONESTY GATE.
    h.run('equivalence-settled-negatively-and-not-conflated-with-the-work-order',
          check=lambda: bool(contains(RUN, 'MUTUALLY ORTHOGONAL')
                             and contains(FIL, 'IT IS SETTLED, AND')
                             and contains(FIL, 'W-ORD-EQUIV-CLASS` IS NOT CLOSED BY THIS')
                             and contains(FIL, 'A DIFFERENT VECTOR AND A DIFFERENT QUESTION')),
          fixture=lambda: bool(contains(FIL, 'THE OBJECTS ARE EQUIVALENT')),
          witness=lambda: bool(contains(FIL, 'THE ACT FOLLOWED THE')))

    h.run('F-NOTADOPT-and-dossier-routed-and-no-shadow',
          check=lambda: bool(contains(FIL, 'NOTHING IS ADOPTED')
                             and contains(FIL, 'M-2 REMAINS OWED')
                             and contains(FIL, 'MAKES NO RECOMMENDATION, IN ANY DIRECTION')
                             and contains(FIL, 'A UNIT RULE IS NOT AN AGGREGATION')
                             and new_lean_files() == 0
                             and float_tokens_in_runner() == 0),
          fixture=lambda: bool(contains(FIL, 'Q.value = u_prime')),
          witness=lambda: bool(contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')))

    h.run('owners-intact-fixtures-reachable-no-or-in-logic',
          check=lambda: bool(git_unchanged('data/b274_straddle_generally.txt')
                             and git_unchanged('data/b272_escape_class.txt')
                             and git_unchanged('tools/e16/b272_escape_class.py')
                             and len(unreachable_fixtures()) == 0
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
    n, bs, pm = canonical_oracle()
    print('  canonical oracle : %d cells; scaling-fixed != {0} in %d; Pi-fixed != {0} in %d'
          % (n, bs, pm))
    print('  float tokens in the deciding runner : %d' % float_tokens_in_runner())
    print('  unreachable fixture needles : %d of %d'
          % (len(unreachable_fixtures()), len(FIXTURE_NEEDLES)))
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or`: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
