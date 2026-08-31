# -*- coding: utf-8 -*-
"""b271_checks.py -- M-2 CAMPAIGN, ACT 5. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE, SAID IN ITS OWN HEADER SO IT IS NOT TRUSTED BEYOND IT:
###  (1) whether the DERIVATION at S1/S2 is CORRECT -- it checks that the exact channel took the
###      verdicts and that the bank says what the run printed; ### **IT DOES NOT RE-DERIVE.**
###  (2) whether the ESCAPE CLASS contains anything useful -- ### that is `W-ORD-ESCAPE-SURVEY`,
###      filed OPEN, and no gate here bears on it.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 12 -- it tokenizes.
### ### **EVERY PREDICATE BELOW IS A DIRECT BOOLEAN OVER AN EXACT TEST, WITH NO BRANCHING ARMS**
### -- `W-ORD-PREDICATE-ARM` was b270's own incident and this file is written against it.
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

ROOT = 'D:/relay'
SIDE = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')

REG = os.path.join(D, 'b271_registration_2026-08-31.txt')
RUN = os.path.join(D, 'b271_run.txt')
FIL = os.path.join(D, 'b271_top_level_no_go.txt')
SAT = os.path.join(D, 'audit_b271_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b271_top_level_no_go.py')
SHADOW = os.path.join(SIDE, 'Core', 'AbsorptionFunctionalShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

# ### THE SEVENTEEN LOAD-BEARING QUOTATIONS, EACH AGAINST ITS OWNER FILE. ### VERBATIM OR FAIL.
QUOTES = [
    ('b226_stated_choice.txt',
     "S        = the DFT-like operator (S f)(m) = SUM_{m'} f(m') zeta_N^{m m'},  N = q^2"),
    ('b226_stated_choice.txt',
     "Pi       = the involution (Pi f)(m) = f(-m);  S^2 = q^2 Pi, so M := S/q has M^4 = 1"),
    ('b226_stated_choice.txt',
     "P_1      = (1 + M + M^2 + M^3)/4, the projector onto the +1 sector E_1"),
    ('b226_stated_choice.txt', "4q P_1   = (q + S)(1 + Pi)"),
    ('b226_stated_choice.txt',
     "Son(p,n) = the vectors on Z/p^{2n} vanishing on a ball AND on its transform image,"),
    ('b226_stated_choice.txt', "f_{i,j}  = e_{i+qj} - e_i,  i,j in [1,q)"),
    ('b226_stated_choice.txt',
     "u = 4q P_1 f IS IN E_1 **BY CONSTRUCTION** -- it is a projector image"),
    ('b226_stated_choice.txt', "d_1 > 0 GIVES E_1 != 0. ### IT DOES NOT GIVE u_{1,1} != 0."),
    ('b268_generator_nonvanishing.txt',
     "SO THE ZERO SET IS EXACTLY THE `q` MULTIPLES OF `q`, AND `support(u_p) = N - q`."),
    ('b270_ambient_pairing_properties.txt',
     "`u_v` VANISHES ON THE BALL. ### EVERY SUMMAND CARRIES THE FACTOR"),
    ('b270_ambient_pairing_properties.txt',
     "THEREFORE `Tr(U^n S_quot) = 0` AS WELL -- AND IT IS 0 AT ALL EIGHT CELLS, MEASURED."),
    ('b267_aggregation_source.txt',
     "tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1) ### for 1 <= k <= n-1, 0 for k >= n. QED"),
    ('b267_aggregation_source.txt', "AT `k = n`: THE EXPRESSION RETURNS `0` AT EVERY CELL."),
    ('b267_registration_2026-08-31.txt', "(SPEC-1) IT COUNTS FIRST LEVELS."),
    ('b267_registration_2026-08-31.txt',
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT LEVELS `k <= n-1`."),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b15_2026-08-18.txt', "a finite-place-set object at a finite cutoff decides nothing"),
]

# ### THE EIGHT REGISTERED CLOSED-FORM VALUES `4(N - q)`, ONE PER CELL. ### The gate holds them
# ### independently of the run so that agreement is a COMPARISON and not a re-reading.
EXPECTED_PAIR = ['48', '24', '80', '168', '440', '624', '1088', '1368']


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


def lean_profile():
    """### THE SHADOW'S PROFILE, RE-PRINTED RATHER THAN CLAIMED (b227's standard).
    ### **THIS GATE EXISTS BECAUSE OF THIS ACT'S OWN (D1): a first draft compiled with every
    ### terminal resting on `sorryAx`, and only the PRINTED PROFILE showed it.**
    ### Returns (exit_code, n_axiom_free, n_sorry, n_other_axioms)."""
    p = subprocess.run(['lake', 'env', 'lean', 'Core/AbsorptionFunctionalShadow.lean'],
                       capture_output=True, text=True, cwd=SIDE)
    out = (p.stdout or '') + (p.returncode and (p.stderr or '') or '')
    free = out.count('does not depend on any axioms')
    sor = out.count('sorryAx')
    other = out.count('depends on axioms')
    return p.returncode, free, sor, other


def or_in_check_logic():
    """### `tokenize`, span-scoped -- b268's mechanism, reused unchanged."""
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
    """### F-EXACT, MECHANIZED. ### Counts float-introducing tokens in the deciding runner."""
    import tokenize
    with open(RUNNER, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    floats = sum(1 for t in toks if t.type == tokenize.NUMBER and '.' in t.string)
    names = sum(1 for t in toks
                if t.type == tokenize.NAME and t.string in ('float', 'numpy', 'np'))
    return floats + names


def pair_values_present():
    """### EVERY ONE OF THE EIGHT REGISTERED VALUES APPEARS IN THE RUN. ### An exhaustive count,
    ### not a spot check, and not a branch."""
    hay = io.open(RUN, encoding='utf-8').read()
    return sum(1 for v in EXPECTED_PAIR if v in hay)


def main():
    h = Harness(ROOT, 'b271')

    # 1 -- ### THE SEAL, INTACT, AND THE SATISFIABILITY AUDIT PRESENT.
    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '3e2469d0467a622fa970b30689d680dccbd2dd111e03c18d')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          # ### FIXTURE: claim the audit found a contradictory clause. ### It found none.
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    # 2 -- ### F-QUOTE. ### EVERY LOAD-BEARING QUOTATION VERBATIM AGAINST ITS OWNER.
    h.run('seventeen-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 17),
          # ### FIXTURE: a needle this seat knows is NOT in b226, in b226's own vocabulary.
          fixture=lambda: bool(verify_all(os.path.join(D, 'b226_stated_choice.txt'),
                                          ['E_1 FORCES VANISHING ON THE BALL'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 17))

    # 3 -- ### F-CTRL. ### BOTH POLARITIES OF BOTH TESTS, AT EVERY CELL.
    h.run('controls-bite-in-both-polarities-at-all-eight-cells',
          check=lambda: bool(contains(RUN, 'ALL SIX CONTROLS BEHAVE AS REQUIRED AT ALL 8 CELLS: YES')
                             and contains(RUN, 'A TEST THAT ONLY EVER SAYS YES IS NOT A')),
          # ### FIXTURE: claim the instrument was not trusted. ### It passed every control.
          fixture=lambda: bool(contains(RUN, 'THE INSTRUMENT IS NOT TRUSTED')),
          witness=lambda: bool(contains(RUN, 'want NO')))

    # 4 -- ### S1. ### THE LEMMA HELD IN BOTH POLARITIES, WITH TWO UNRELATED `f`.
    # ### THE GATE READS THE RUN'S OWN VERDICT LINE, NOT A TABLE ROW. ### The first draft's
    # ### fixture demanded a header line followed immediately by a `(3,1)` row, but the first
    # ### row is `(2,2)` -- ### **SO IT COULD NEVER FIRE AND THE GATE PASSED WITHOUT TESTING
    # ### ITS POLARITY.** ### b270's (D6) species, second occurrence. ### Declared.
    h.run('S1-lemma-holds-and-its-hypothesis-is-load-bearing',
          check=lambda: bool(contains(RUN, '### S1 VERDICT: lemma holds in BOTH polarities at 8 of 8 cells')
                             and contains(RUN, 'THE SUM IS ZERO TERMWISE, NOT BY CANCELLATION')
                             and contains(FIL, 'NO HYPOTHESIS IS PLACED ON `f` AT ALL')),
          # ### FIXTURE: claim the run's S1 verdict line reports a polarity failure. ### The
          # ### runner emits that exact wording ONLY when a cell fails, so this CAN fire -- and
          # ### it carries no `###` marker, because `check_harness.norm` STRIPS those and a
          # ### marker-based fixture therefore cannot discriminate. ### THAT IS HOW THE SECOND
          # ### DEAD FIXTURE WAS FOUND.
          fixture=lambda: bool(contains(RUN, 'S1 VERDICT: LEMMA POLARITY FAILED at')),
          witness=lambda: bool(contains(RUN, 'f=u_v, g=u_v (0?)')))

    # 5 -- ### F-BARRIER. ### THE BARRIER IS REFUTED, AND THE WITNESS IS IN `E_1`.
    h.run('F-BARRIER-refuted-witness-in-E1-nonzero-on-ball',
          check=lambda: bool(contains(RUN, 'THE BARRIER IS REFUTED FOR THE AMBIENT `E_1`')
                             and contains(RUN, 'VANISHES NOWHERE AT ALL, SO IT IS NOT A NEAR MISS')
                             and contains(FIL, 'VERIFIED EXACTLY AT ALL EIGHT CELLS')),
          # ### FIXTURE: claim no witness was found and the barrier stands.
          fixture=lambda: bool(contains(RUN, 'THE BARRIER STANDS ON THIS AXIS')),
          witness=lambda: bool(contains(RUN, 'M g = g?')))

    # 6 -- ### S2b. ### THE ESCAPE IS MATERIAL, AND EVERY REGISTERED VALUE IS PRESENT.
    h.run('escape-material-all-eight-closed-form-values-match',
          check=lambda: bool(pair_values_present() == 8
                             and contains(RUN, 'THE ESCAPE IS MATERIAL')
                             and contains(RUN, 'MATCHES THE CLOSED FORM REGISTERED BEFORE IT WAS')),
          # ### FIXTURE: claim the escape is formal only. ### It is not.
          fixture=lambda: bool(contains(RUN, 'THE ESCAPE IS FORMAL ONLY')),
          witness=lambda: bool(pair_values_present() == 8))

    # 7 -- ### THE ESCAPE CLASS IS NAMED, AND ITS UNSURVEYED-NESS IS ON THE RECORD.
    h.run('escape-class-named-and-declared-unsurveyed',
          check=lambda: bool(contains(RUN, 'THE CLASS THAT ESCAPES IS `E_1` MINUS `Son`')
                             and contains(RUN, 'IT DOES NOT SURVEY THE CLASS')
                             and contains(FIL, 'W-ORD-ESCAPE-SURVEY')),
          # ### FIXTURE: claim the bank presents the witness as a candidate.
          fixture=lambda: bool(contains(FIL, 'THE WITNESS IS ADOPTED')),
          witness=lambda: bool(contains(FIL, 'A WITNESS TO A CLASS, NOT A CANDIDATE')))

    # 8 -- ### THE SHADOW'S PROFILE, RE-PRINTED. ### THIS ACT'S (D1) IS WHY THIS GATE EXISTS.
    h.run('shadow-profile-reprinted-seven-terminals-zero-axioms',
          check=lambda: bool(lean_profile()[0] == 0
                             and lean_profile()[1] == 7
                             and lean_profile()[2] == 0
                             and lean_profile()[3] == 0),
          # ### FIXTURE: claim a terminal rests on an axiom. ### None does.
          fixture=lambda: bool(lean_profile()[2] + lean_profile()[3] > 0),
          witness=lambda: bool(lean_profile()[1] == 7))

    # 9 -- ### F-EXACT. ### NO FLOAT ENTERS THE DECIDING RUNNER, SO NO FLOAT DECIDES.
    h.run('F-EXACT-no-float-in-the-deciding-runner',
          check=lambda: bool(float_tokens_in_runner() == 0
                             and contains(RUNNER, 'NO FLOAT DECIDES ANYTHING HERE')),
          # ### FIXTURE: claim a float or numpy name is present. ### None is.
          fixture=lambda: bool(float_tokens_in_runner() > 0),
          witness=lambda: bool(contains(RUNNER, 'Q(zeta_N)')))

    # 10 -- ### F-NOADOPT AND F-NOSPEC23 AND F-NOFIT, THE THREE BOUNDARY ASSERTIONS.
    h.run('nothing-adopted-specs-2-3-untested-no-target-compared',
          check=lambda: bool(contains(FIL, 'M-2 REMAINS OWED')
                             and contains(FIL, 'SPECIFIED-NOT-STATED')
                             and contains(FIL, 'WERE NOT TESTED FOR ANY OBJECT THIS ACT EXHIBITS')
                             and contains(RUN, 'NOT A TABLE HEADED BY act 9')
                             and not contains(RUN, 'residual')),
          # ### FIXTURE: claim the bank installs the witness as the per-place value.
          fixture=lambda: bool(contains(FIL, 'Q.value = 4q P_1 e_0')),
          witness=lambda: bool(contains(FIL, 'NO RULING WAS TAKEN')))

    # 11 -- ### NO OWNER INSTRUMENT AND NO OWNING ACT'S BANK WAS EDITED. ### b246 HELD.
    h.run('owners-and-prior-banks-byte-identical',
          check=lambda: bool(git_unchanged('data/b270_ambient_pairing_properties.txt')
                             and git_unchanged('data/b269_m2_statement.txt')
                             and git_unchanged('data/b226_stated_choice.txt')
                             and git_unchanged('tools/e16/b268_generator.py')
                             and git_unchanged('tools/e16/b270_ambient_pairing.py')
                             and git_unchanged('Core/BallAbsorptionShadow.lean', SIDE)),
          # ### FIXTURE: claim b270's runner moved. ### It was IMPORTED, not edited.
          fixture=lambda: bool(git_unchanged('tools/e16/b270_ambient_pairing.py') is False),
          witness=lambda: bool(git_unchanged('data/b10_2026-08-17.txt')))

    # 12 -- ### THIS GATE FILE HAS NO `or` IN ANY CHECK'S LOGIC. ### b268's MECHANISM, REUSED.
    h.run('this-gate-file-has-no-or-in-its-logic',
          check=lambda: bool(or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 11),
          # ### FIXTURE: claim a check body carries an `or` in its logic. ### None does.
          fixture=lambda: bool(or_in_check_logic()[0] > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 11))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  quotations verified verbatim : %d of %d unfindable'
          % (quotes_missing(), len(QUOTES)))
    print('  registered closed-form values present in run : %d of 8' % pair_values_present())
    rc, free, sor, oth = lean_profile()
    print('  shadow re-printed: exit=%d  axiom-free=%d  sorryAx=%d  other-axioms=%d'
          % (rc, free, sor, oth))
    print('  check bodies scanned for `or` in logic: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    print('  float-introducing tokens in the deciding runner: %d' % float_tokens_in_runner())
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
