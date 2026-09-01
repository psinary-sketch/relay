# -*- coding: utf-8 -*-
"""b272_checks.py -- M-2 CAMPAIGN, ACT 6. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE, SAID IN ITS OWN HEADER SO IT IS NOT TRUSTED BEYOND IT:
###  (1) whether the CHARACTERIZATION is correct -- it checks that the exact channel took the
###      verdicts and that the bank says what the run printed; ### **IT DOES NOT RE-DERIVE.**
###  (2) whether some NON-FAMILY element of `E_1` satisfies (SPEC-2) -- ### that is the named
###      resistance, and no gate here bears on it.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 14 -- it tokenizes.
### ### **AND ONE THING IT NOW CAN SEE, WHICH TWO PRIOR ACTS COULD NOT: ### WHETHER A FIXTURE
### ### IS REACHABLE AT ALL.** ### b270 and b271 each shipped a fixture that could never fire.
### Gate 13 mechanizes that lesson: every run-based fixture needle must appear as a literal in
### the file that emits the run. ### **LORE IS NOT A GUARD, AND NEITHER IS THIS FILE.**
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

REG = os.path.join(D, 'b272_registration_2026-08-31.txt')
RUN = os.path.join(D, 'b272_run.txt')
FIL = os.path.join(D, 'b272_escape_class.txt')
SAT = os.path.join(D, 'audit_b272_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b272_escape_class.py')
FLOOR = os.path.join(ROOT, 'tools', 'noise_floor.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

QUOTES = [
    ('b271_top_level_no_go.txt',
     "VERDICT: (ESCAPE). ### `E_1` MEMBERSHIP DOES NOT FORCE VANISHING ON THE BALL."),
    ('b271_top_level_no_go.txt',
     "`g := 4q P_1 e_0 = 2q e_0 + 2 * 1`, i.e. `g(m) = 2q [m = 0] + 2`."),
    ('b271_top_level_no_go.txt',
     "THEY AGREE, SO `S g = q g`. ### VERIFIED EXACTLY AT ALL EIGHT CELLS."),
    ('b271_top_level_no_go.txt', "IT DOES NOT SURVEY THE CLASS."),
    ('b226_stated_choice.txt',
     "THEREFORE SUM_v | ||u_v|| - 1 | = SUM_v 0 = ### **0**, which converges."),
    ('b226_stated_choice.txt', "the demand is that SUM_v | ||f_v|| - 1 | CONVERGE."),
    ('b226_stated_choice.txt', "u_v in E_1(Son(v, ell(v))) lies in E_1(S-bar_v)."),
    ('b226_stated_choice.txt', "IT IS A PREMISE HERE, NOT A THEOREM OF THIS ACT."),
    ('b226_stated_choice.txt', "Two C0-sequences ... are ### EQUIVALENT ... if and only if"),
    ('b226_stated_choice.txt',
     'the incomplete products for DIFFERENT classes are "MUTUALLY ORTHOGONAL".'),
    ('b226_stated_choice.txt',
     "A DIFFERENT CHOICE COULD GIVE AN ORTHOGONAL OBJECT, NOT AN ISOMORPHIC ONE."),
    ('b226_stated_choice.txt',
     "THE CANONICITY OF THIS CHOICE IS ### **A DEFINITION MADE BY RULING, NOT A THEOREM.**"),
    ('b226_stated_choice.txt', "4q P_1   = (q + S)(1 + Pi)"),
    ('b226_stated_choice.txt',
     "S        = the DFT-like operator (S f)(m) = SUM_{m'} f(m') zeta_N^{m m'},  N = q^2"),
    ('b268_generator_nonvanishing.txt',
     "SO THE ZERO SET IS EXACTLY THE `q` MULTIPLES OF `q`, AND `support(u_p) = N - q`."),
    ('b270_ambient_pairing_properties.txt',
     "`S_quot` IS MULTIPLICATION BY THE OFF-BALL INDICATOR"),
    ('b270_ambient_pairing_properties.txt', "EVERY SUMMAND CARRIES THE FACTOR"),
    ('b267_registration_2026-08-31.txt', "(SPEC-1) IT COUNTS FIRST LEVELS."),
    ('b267_registration_2026-08-31.txt',
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT LEVELS `k <= n-1`."),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b264_run.txt', "EIGENFUNCTIONS ARE ARBITRARY VECTORS IN A NEAR-DEGENERATE NOISE SUBSPACE,"),
]

# ### THE EIGHT REGISTERED CLOSED-FORM NORMS `(2q+2)^2 + 4(N-1)`, HELD INDEPENDENTLY OF THE RUN
# ### SO AGREEMENT IS A COMPARISON AND NOT A RE-READING.
EXPECTED_NORMS = ['160', '96', '240', '448', '1056', '1456', '2448', '3040']

# ### EVERY RUN-BASED FIXTURE NEEDLE, WITH THE FILE THAT MUST BE ABLE TO EMIT IT.
# ### ### **GATE 13 CHECKS THESE ARE REACHABLE. ### b270 AND b271 EACH SHIPPED ONE THAT WAS
# ### ### NOT, AND IN BOTH CASES THE GATE PASSED WHILE TESTING NOTHING.**
FIXTURE_NEEDLES = [
    ('CHARACTERIZATION FAILED', RUNNER),
    ('K2 NORM MISMATCH', RUNNER),
    ('K3 ORTHOGONALITY FAILED', RUNNER),
    ('K5 IS SATISFIED BY SOME MEMBER', RUNNER),
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


def floor_arms():
    """### COMPONENT 0's FOUR ARMS, EXERCISED DIRECTLY. ### Returns the four verdicts."""
    m7 = NF.classify(2.178442e-08, 2.178442e-08 * (1 + 2.74e-02))[0]
    low = NF.classify(1.0e-12, 1.0e-12)[0]
    good = NF.classify(5.240859e-01, 5.240859e-01 * (1 + 2.14e-13))[0]
    exact = NF.classify(0, None, exact=True)[0]
    return m7, low, good, exact


def floor_selftest_ok():
    ok, _ = NF.self_test(verbose=False)
    return ok


def runner_calls_floor():
    return 'noise_floor' in io.open(RUNNER, encoding='utf-8').read()


def unreachable_fixtures():
    """### GATE 13's MECHANISM. ### A fixture needle that the emitting file cannot produce is a
    ### fixture that can never fire, and a gate whose fixture never fires TESTED NOTHING."""
    bad = []
    for needle, src in FIXTURE_NEEDLES:
        if needle not in io.open(src, encoding='utf-8').read():
            bad.append(needle)
    return bad


def norms_present():
    hay = io.open(RUN, encoding='utf-8').read()
    return sum(1 for v in EXPECTED_NORMS if v in hay)


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


def float_tokens_in_runner():
    import tokenize
    with open(RUNNER, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    floats = sum(1 for t in toks if t.type == tokenize.NUMBER and '.' in t.string)
    names = sum(1 for t in toks
                if t.type == tokenize.NAME and t.string in ('float', 'numpy', 'np'))
    return floats + names


def main():
    h = Harness(ROOT, 'b272')

    # 1 -- ### THE SEAL, INTACT, AND THE SATISFIABILITY AUDIT PRESENT.
    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '63a35ca7081def2651f55e9d6ebff6b9ab9990a9fab27a88')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    # 2 -- ### F-QUOTE. ### EVERY LOAD-BEARING QUOTATION VERBATIM AGAINST ITS OWNER.
    h.run('twentyone-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 21),
          fixture=lambda: bool(verify_all(os.path.join(D, 'b226_stated_choice.txt'),
                                          ['THE ESCAPE CLASS IS CANONICAL'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 21))

    # 3 -- ### COMPONENT 0. ### THE SELF-TEST, AND ALL FOUR ARMS FIRING.
    h.run('component-0-selftest-and-four-arms',
          check=lambda: bool(floor_selftest_ok()
                             and floor_arms() == (NF.DRIFTING, NF.AT_FLOOR,
                                                  NF.RESOLVED, NF.EXACT)),
          # ### FIXTURE: THE NAIVE GATE. ### Claim b264's mode 7 is RESOLVED -- which is exactly
          # ### what a magnitude-only gate would have said, since 2.178e-8 sits ABOVE sqrt(eps).
          # ### **THIS FIXTURE IS THE TOOL THAT WOULD HAVE SHIPPED AND CAUGHT NOTHING.**
          fixture=lambda: bool(floor_arms()[0] == NF.RESOLVED),
          witness=lambda: bool(NF.DEFAULT_FLOOR < 2.178442e-08))

    # 4 -- ### COMPONENT 0 IS IN THIS ACT'S PATH, NOT MERELY SHIPPED.
    h.run('component-0-in-the-path-and-returned-a-verdict',
          check=lambda: bool(runner_calls_floor()
                             and contains(RUN, 'gate verdict : EXACT')
                             and contains(RUN, 'IT WAS NOT')),
          # ### FIXTURE: claim the runner never imports the gate. ### It does, on line one of (0).
          fixture=lambda: bool(runner_calls_floor() is False),
          witness=lambda: bool(contains(RUN, 'a verdict, not a bypass')))

    # 5 -- ### THE CHARACTERIZATION. ### A SPANNING SET INSIDE THE ESCAPE CLASS.
    h.run('characterization-spanning-family-inside-escape-class',
          check=lambda: bool(contains(RUN, 'CHARACTERIZATION VERDICT: spanning family entirely '
                                           'inside the escape class at 8 of 8 cells')
                             and contains(RUN, 'ESCAPING IS GENERIC')),
          fixture=lambda: bool(contains(RUN, 'CHARACTERIZATION FAILED')),
          witness=lambda: bool(contains(RUN, 'membership scope')))

    # 6 -- ### K2. ### THE NORMS MATCH THE CLOSED FORM REGISTERED BEFORE THEY WERE COMPUTED.
    h.run('K2-norms-match-registered-closed-form',
          check=lambda: bool(norms_present() == 8
                             and contains(RUN, 'K2 VERDICT: norms rational and matching')),
          fixture=lambda: bool(contains(RUN, 'K2 NORM MISMATCH')),
          witness=lambda: bool(norms_present() == 8))

    # 7 -- ### K3. ### THE ORTHOGONALITY, AND ITS OTHER POLARITY LIVE.
    h.run('K3-orthogonality-exact-and-other-polarity-live',
          check=lambda: bool(contains(RUN, 'K3 VERDICT: <u, g_0> = 0 exactly at 8 of 8 cells')
                             and contains(RUN, 'the other polarity is live at 8 of 8')
                             and contains(FIL, 'MUTUALLY ORTHOGONAL')),
          fixture=lambda: bool(contains(RUN, 'K3 ORTHOGONALITY FAILED')),
          witness=lambda: bool(contains(RUN, '4q u(c)')))

    # 8 -- ### K5. ### NO MEMBER OF THE SPANNING FAMILY SATISFIES (SPEC-2).
    h.run('K5-no-family-member-satisfies-spec-2',
          check=lambda: bool(contains(RUN, 'K5 VERDICT: no member of the spanning family '
                                           'satisfies SPEC-2 -- 0 of 16 members satisfy it')
                             and contains(RUN, 'NOT SETTLED, AND NOT ATTEMPTED')),
          fixture=lambda: bool(contains(RUN, 'K5 IS SATISFIED BY SOME MEMBER')),
          witness=lambda: bool(contains(RUN, 'SIGNATURE')))

    # 9 -- ### F-CLASSMEM. ### THE BANK NEVER STATES A MEMBER'S PROPERTY OF THE CLASS.
    h.run('F-CLASSMEM-class-and-member-kept-apart',
          check=lambda: bool(contains(FIL, 'A CLASS IS NOT A MEMBER')
                             and contains(FIL, 'THIS ACT DOES NOT SETTLE IT')
                             and contains(FIL, 'A FACT ABOUT `g_0`, NOT ABOUT THE CLASS')),
          fixture=lambda: bool(contains(FIL, 'THE CLASS IS ORTHOGONAL TO b226')),
          witness=lambda: bool(contains(FIL, 'THE RESISTANCE')))

    # 10 -- ### F-NOADOPT AND F-PATTERN. ### NOTHING ADOPTED, THE NOTE STAYS AT PATTERN GRADE.
    h.run('F-NOADOPT-and-selection-note-at-pattern-grade',
          check=lambda: bool(contains(FIL, 'M-2 REMAINS OWED')
                             and contains(FIL, 'SPECIFIED-NOT-STATED')
                             and contains(FIL, 'PATTERN GRADE')
                             and contains(FIL, 'PROMOTION CRITERION')
                             and contains(FIL, 'UNMET')),
          fixture=lambda: bool(contains(FIL, 'Q.value = g_0')),
          witness=lambda: bool(contains(FIL, 'NO RECOMMENDATION')))

    # 11 -- ### NO OWNER INSTRUMENT AND NO OWNING ACT'S BANK WAS EDITED. ### b246 HELD.
    h.run('owners-and-prior-banks-byte-identical',
          check=lambda: bool(git_unchanged('data/b271_top_level_no_go.txt')
                             and git_unchanged('data/b270_ambient_pairing_properties.txt')
                             and git_unchanged('data/b226_stated_choice.txt')
                             and git_unchanged('tools/e16/b268_generator.py')
                             and git_unchanged('tools/e16/b271_top_level_no_go.py')),
          fixture=lambda: bool(git_unchanged('tools/e16/b271_top_level_no_go.py') is False),
          witness=lambda: bool(git_unchanged('data/b268_generator_nonvanishing.txt')))

    # 12 -- ### THE SHADOW DECISION, CHECKED NOT ASSUMED. ### NOTHING WAS BUILT.
    h.run('shadow-condition-checked-and-nothing-built',
          check=lambda: bool(new_lean_files() == 0
                             and contains(FIL, '0 `.lean` FILES MOVED, CHECKED NOT ASSUMED')
                             and contains(FIL, 'THE CANDIDATE RESIDUES, ENUMERATED')),
          fixture=lambda: bool(new_lean_files() > 0),
          witness=lambda: bool(contains(FIL, 'BUILD NOTHING')))

    # 13 -- ### EVERY RUN-BASED FIXTURE NEEDLE IS REACHABLE. ### b270's AND b271's LESSON,
    # ### MECHANIZED RATHER THAN REMEMBERED.
    h.run('every-fixture-needle-is-reachable',
          check=lambda: bool(len(unreachable_fixtures()) == 0
                             and len(FIXTURE_NEEDLES) >= 4),
          fixture=lambda: bool(len(unreachable_fixtures()) > 0),
          witness=lambda: bool(len(FIXTURE_NEEDLES) >= 4))

    # 14 -- ### THIS GATE FILE HAS NO `or` IN ANY CHECK'S LOGIC. ### b268's MECHANISM.
    h.run('this-gate-file-has-no-or-in-its-logic',
          check=lambda: bool(or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 13),
          fixture=lambda: bool(or_in_check_logic()[0] > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 13))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  quotations verified verbatim : %d of %d unfindable' % (quotes_missing(), len(QUOTES)))
    print('  registered closed-form norms present in run : %d of 8' % norms_present())
    print('  COMPONENT 0 arms (mode7, below-floor, good, exact) : %s' % (floor_arms(),))
    print('  COMPONENT 0 self-test : %s' % ('PASSED' if floor_selftest_ok() else 'FAILED'))
    print('  unreachable fixture needles : %d of %d'
          % (len(unreachable_fixtures()), len(FIXTURE_NEEDLES)))
    print('  new .lean files in SIDE : %d' % new_lean_files())
    print('  check bodies scanned for `or` in logic: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    print('  float-introducing tokens in the deciding runner: %d' % float_tokens_in_runner())
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
