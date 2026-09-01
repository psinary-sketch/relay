# -*- coding: utf-8 -*-
"""b273_checks.py -- M-2 CAMPAIGN, ACT 7. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE, SAID IN ITS OWN HEADER:
###  (1) whether the intermediate-value argument is SOUND -- it checks the two straddling values
###      and the two order comparisons; ### **THE ANALYSIS ITSELF IS NOT MECHANIZED HERE.**
###  (2) whether the second cell's targets are attainable -- ### that is `W-ORD-ORDER-CHANNEL`.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 14 -- it tokenizes.
### ### **LORE IS NOT A GUARD, AND NEITHER IS THIS FILE.**
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402
import noise_floor as NF                      # noqa: E402

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')

REG = os.path.join(D, 'b273_registration_2026-09-01.txt')
RUN = os.path.join(D, 'b273_run.txt')
FIL = os.path.join(D, 'b273_spec2_range.txt')
SAT = os.path.join(D, 'audit_b273_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b273_spec2_range.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

QUOTES = [
    ('b272_escape_class.txt', "MEMBERS OF THE SPANNING FAMILY SATISFYING (SPEC-2): ### 0 OF 16."),
    ('b272_escape_class.txt', "an exact statement about `N` NAMED VECTORS, taken by reduction"),
    ('b272_escape_class.txt',
     "THAT IS A DIFFERENT CHANNEL FROM REDUCTION MODULO `Phi_N`, IT IS NOT WHAT THIS ACT'S SEAL "
     "AUTHORIZES, AND IT IS NOT OPENED HERE. ### FILED, NOT FUDGED."),
    ('b272_escape_class.txt',
     "`g_c := 4q P_1 e_c`,  `g_c(m) = q([m = c] + [m = -c]) + zeta^{mc} + zeta^{-mc}`."),
    ('b272_escape_class.txt',
     "`<u, g_c> = q(u(c) + u(-c)) + (S u)(c) + (S u)(-c) = 2q(u(c) + u(-c))`"),
    ('b270_ambient_pairing_properties.txt', "EVERY SUMMAND CARRIES THE FACTOR"),
    ('b270_ambient_pairing_properties.txt', "P(1) * 2^{1/2} = (64/3)(1 + 2^{1/2})"),
    ('b267_aggregation_source.txt',
     "tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1) ### for 1 <= k <= n-1, 0 for k >= n. QED"),
    ('b223_level_limit_two_places.txt',
     "2   2     4       16          9                 32          2          2     YES"),
    ('b226_stated_choice.txt', "4q P_1   = (q + S)(1 + Pi)"),
    ('b226_stated_choice.txt',
     "S        = the DFT-like operator (S f)(m) = SUM_{m'} f(m') zeta_N^{m m'},  N = q^2"),
    ('b267_registration_2026-08-31.txt', "(SPEC-1) IT COUNTS FIRST LEVELS."),
    ('b267_registration_2026-08-31.txt',
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT LEVELS `k <= n-1`."),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b15_2026-08-18.txt', "a finite-place-set object at a finite cutoff decides nothing"),
]

# ### EVERY RUN-BASED FIXTURE NEEDLE, WITH THE FILE THAT MUST BE ABLE TO EMIT IT (gate 13).
FIXTURE_NEEDLES = [
    ('FAILED -- NO NUMBER HERE MAY BE BELIEVED', RUNNER),
    ('NOT POSITIVE', RUNNER),
    ('NO STRADDLE AMONG THE CANDIDATES', RUNNER),
]


def git_unchanged(rel, root=ROOT):
    return subprocess.run(['git', '-C', root, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def seal_ok():
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0


def quotes_missing():
    bad = 0
    for f, n in QUOTES:
        v, _ = verify_all(os.path.join(D, f), [n])
        if v != 'PASS':
            bad += 1
    return bad


def float_tokens_in_runner():
    """### F-NOFLOAT, MECHANIZED. ### Counts float-introducing tokens in the DECIDING runner."""
    import tokenize
    with open(RUNNER, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    floats = sum(1 for t in toks if t.type == tokenize.NUMBER and '.' in t.string)
    names = sum(1 for t in toks
                if t.type == tokenize.NAME and t.string in ('float', 'numpy', 'np'))
    return floats + names


def sign_rule_arms_exhaustive():
    """### THE SIGN RULE'S ARMS, EXERCISED OVER EVERY SIGN PATTERN. ### `W-ORD-PREDICATE-ARM`
    ### applied to this act's own helper: ### **A RULE WITH A MISSING ARM IS A FALSE VERDICT.**
    ### Returns (patterns_covered, disagreements) against an independent rational oracle."""
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
    from b273_spec2_range import sign_in_Qsqrt2
    from fractions import Fraction as Fr
    vals = [Fr(-3), Fr(-1), Fr(0), Fr(1), Fr(3), Fr(7, 5), Fr(-7, 5)]
    seen = set()
    bad = 0
    for a in vals:
        for b in vals:
            s = sign_in_Qsqrt2(a, b)
            seen.add((1 if a > 0 else (-1 if a < 0 else 0),
                      1 if b > 0 else (-1 if b < 0 else 0)))
            # ### INDEPENDENT ORACLE: compare a^2 with 2 b^2 by rational arithmetic, with the
            # ### sign of `a` deciding the branch. ### NO DECIMAL ANYWHERE.
            if a == 0 and b == 0:
                truth = 0
            elif b == 0:
                truth = 1 if a > 0 else -1
            elif a == 0:
                truth = 1 if b > 0 else -1
            elif a > 0 and b > 0:
                truth = 1
            elif a < 0 and b < 0:
                truth = -1
            else:
                lhs = a * a
                rhs = 2 * b * b
                dom_a = lhs > rhs
                if a > 0:
                    truth = 1 if dom_a else (-1 if lhs < rhs else 0)
                else:
                    truth = -1 if dom_a else (1 if lhs < rhs else 0)
            if s != truth:
                bad += 1
    return len(seen), bad


def unreachable_fixtures():
    bad = []
    for needle, src in FIXTURE_NEEDLES:
        if needle not in io.open(src, encoding='utf-8').read():
            bad.append(needle)
    return bad


def new_lean_files():
    p = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                       capture_output=True, text=True)
    return sum(1 for ln in (p.stdout or '').splitlines() if ln.strip().endswith('.lean'))


def or_in_check_logic():
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


def main():
    h = Harness(ROOT, 'b273')

    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '70ec942f8e4c940b2ca90100e9b29d3e4f1fac7ceae289f7')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    h.run('fifteen-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 15),
          fixture=lambda: bool(verify_all(os.path.join(D, 'b272_escape_class.txt'),
                                          ['THE SPANNING FAMILY ATTAINS 2/3'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 15))

    # ### THE MOST IMPORTANT GATE IN THIS FILE. ### A reader will think this act contradicts b272.
    h.run('F-B272-no-contradiction-stated-first',
          check=lambda: bool(contains(FIL, 'A SWEEP OF A SPANNING FAMILY IS NOT A SWEEP OF THE '
                                           'SPACE')
                             and contains(FIL, 'THAT STATEMENT IS TRUE AND THIS ACT '
                                               'RE-CONFIRMS IT')
                             and contains(FIL, 'NO PRIOR ACT IS RE-VERDICTED')),
          fixture=lambda: bool(contains(FIL, 'b272 WAS WRONG')),
          witness=lambda: bool(contains(FIL, 'IT WAS FILED CORRECTLY AND IT IS NOW PAID')))

    h.run('component-0-in-the-path-and-returned-a-verdict',
          check=lambda: bool(contains(RUN, 'gate verdict : EXACT')
                             and contains(RUN, 'NO SPECTRUM TO SIT AT A FLOOR')),
          fixture=lambda: bool(contains(RUN, 'gate verdict : AT_FLOOR')),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    h.run('two-dimensions-printed-and-not-conflated',
          check=lambda: bool(contains(RUN, 'dim E_1 = 5')
                             and contains(RUN, 'd_1(2,2) = 2')
                             and contains(FIL, 'TWO DIMENSIONS, TWO SPACES, NEITHER IS THE OTHER')),
          fixture=lambda: bool(contains(RUN, 'dim E_1 = 2')),
          witness=lambda: bool(contains(RUN, 'dim Son(2,2) = 9')))

    h.run('form-decided-neither-hermitian-nor-symmetric',
          check=lambda: bool(contains(RUN, 'SO THE FORM IS NEITHER HERMITIAN NOR')
                             and contains(RUN, 'a RATIONAL matrix')),
          fixture=lambda: bool(contains(RUN, 'THE FORM IS HERMITIAN')),
          witness=lambda: bool(contains(FIL, 'RATHER THAN ASSUMING THE CONVENIENT CASE')))

    # ### F-CONTROL: b272's own number, recovered.
    h.run('F-CONTROL-b272-value-recovered',
          check=lambda: bool(contains(RUN, 'R(g_0) = 3/10 : CONFIRMED')),
          fixture=lambda: bool(contains(RUN, 'FAILED -- NO NUMBER HERE MAY BE BELIEVED')),
          witness=lambda: bool(contains(RUN, '<A g_0, g_0> = 48')))

    h.run('F-STRADDLE-two-exact-values-both-comparisons-rational',
          check=lambda: bool(contains(RUN, 'w := g_2 - g_6')
                             and contains(RUN, 'SO 3/10 < 2/3 < (1+sqrt2)/3')
                             and contains(RUN, 'because sqrt2 > 1 because 2 > 1')
                             and contains(RUN, '(zeta^2 + zeta^{-2})^2 = 2` verified exactly : '
                                               'YES')),
          fixture=lambda: bool(contains(RUN, 'ORDER COMPARISON TAKEN FROM A DECIMAL')),
          witness=lambda: bool(contains(RUN, 'PURE RATIONAL')))

    h.run('F-EXHIBIT-attaining-vector-exact-and-field-stated',
          check=lambda: bool(contains(RUN, 'ALL THREE CROSS TERMS VANISH')
                             and contains(RUN, 'VERIFY a0 + a2 s^2 = 0 EXACTLY : YES')
                             and contains(RUN, 'POSITIVE -- so s is REAL')
                             and contains(RUN, 'REQUIRES A QUADRATIC EXTENSION OF Q(zeta_16)')),
          fixture=lambda: bool(contains(RUN, 'NOT POSITIVE')),
          witness=lambda: bool(contains(RUN, 's^2 = -8/11 + 8/11 sqrt2')))

    h.run('F-K-each-condition-answered-yes-or-no',
          check=lambda: bool(contains(RUN, 'K1  S v = q v          : YES')
                             and contains(RUN, 'K2  normalizable       : YES')
                             and contains(RUN, '<u, g_0> = 0 : YES')
                             and contains(FIL, 'HERE `<u, w> != 0`, VERIFIED EXACTLY')
                             and contains(RUN, 'ESCAPE CLASS -- IT HAS A NONZERO BALL VALUE')),
          fixture=lambda: bool(contains(FIL, 'K3 is presumably satisfied')),
          witness=lambda: bool(contains(RUN, '(SPEC-1) AT k = n')))

    h.run('second-cell-run-and-its-limit-named',
          check=lambda: bool(contains(RUN, '94 candidates searched')
                             and contains(RUN, 'NO STRADDLE AMONG THE CANDIDATES')
                             and contains(FIL, 'THE VERDICT\'S SCOPE IS THEREFORE ONE CELL')
                             and contains(FIL, 'W-ORD-ORDER-CHANNEL')),
          fixture=lambda: bool(contains(FIL, 'THE SECOND CELL CONFIRMS THE VERDICT')),
          witness=lambda: bool(contains(FIL, 'A LIMIT OF THE CERTIFICATION, NAMED')))

    h.run('F-NOFLOAT-and-sign-rule-arms-exhaustive',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and sign_rule_arms_exhaustive()[1] == 0
                             and sign_rule_arms_exhaustive()[0] == 9),
          fixture=lambda: bool(float_tokens_in_runner() > 0),
          witness=lambda: bool(sign_rule_arms_exhaustive()[0] == 9))

    h.run('F-NOADOPT-and-scope-stated',
          check=lambda: bool(contains(FIL, 'M-2 REMAINS OWED')
                             and contains(FIL, 'NO UNIT IS ADOPTED')
                             and contains(FIL, 'THIS SEAT RANKS NOTHING AND ADOPTS NOTHING')
                             and contains(FIL, '(SPEC-3) NOT TESTED AT ALL')),
          fixture=lambda: bool(contains(FIL, 'Q.value = v')),
          witness=lambda: bool(contains(FIL, 'v` IS AN EXHIBITION')))

    h.run('owners-and-prior-banks-byte-identical-and-no-shadow',
          check=lambda: bool(git_unchanged('data/b272_escape_class.txt')
                             and git_unchanged('data/b270_ambient_pairing_properties.txt')
                             and git_unchanged('data/b223_level_limit_two_places.txt')
                             and git_unchanged('tools/e16/b272_escape_class.py')
                             and new_lean_files() == 0
                             and contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')),
          fixture=lambda: bool(new_lean_files() > 0),
          witness=lambda: bool(contains(FIL, 'RESIDUES ENUMERATED')))

    h.run('every-fixture-needle-is-reachable-and-no-or-in-logic',
          check=lambda: bool(len(unreachable_fixtures()) == 0
                             and or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 13),
          fixture=lambda: bool(len(unreachable_fixtures()) > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 13))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  quotations verified verbatim : %d of %d unfindable' % (quotes_missing(), len(QUOTES)))
    print('  float-introducing tokens in the deciding runner : %d' % float_tokens_in_runner())
    pat, bad = sign_rule_arms_exhaustive()
    print('  sign-rule sign patterns covered : %d ; disagreements with the oracle : %d'
          % (pat, bad))
    print('  unreachable fixture needles : %d of %d'
          % (len(unreachable_fixtures()), len(FIXTURE_NEEDLES)))
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or` in logic: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
