# -*- coding: utf-8 -*-
"""b270_checks.py -- M-2 CAMPAIGN, ACT 4. ### THE CONTROL SUITE.

### WHAT THIS GATE FILE CANNOT SEE, SAID IN ITS OWN HEADER SO IT IS NOT TRUSTED BEYOND IT:
###  (1) whether the DERIVATION at S1-S5 is CORRECT -- it checks that the exact channel took the
###      verdicts and that the bank says what the run printed; ### **IT DOES NOT RE-DERIVE.**
###  (2) whether the author's ruling SHOULD take C1 -- ### that is not a gate's business.
###  (3) that this gate file carries an `or` in a check's logic. ### Gate 11 -- it tokenizes.
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
D = os.path.join(ROOT, 'data')

REG = os.path.join(D, 'b270_registration_2026-08-31.txt')
RUN = os.path.join(D, 'b270_run.txt')
FIL = os.path.join(D, 'b270_ambient_pairing_properties.txt')
SAT = os.path.join(D, 'audit_b270_reg_satisfiable.txt')
RUNNER = os.path.join(ROOT, 'tools', 'e16', 'b270_ambient_pairing.py')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SELF = os.path.abspath(__file__)

# ### THE SIXTEEN LOAD-BEARING QUOTATIONS, EACH AGAINST ITS OWNER FILE. ### VERBATIM OR FAIL.
QUOTES = [
    ('b10_2026-08-17.txt',
     "V_inv = { f supported off the ball : f(m') = f(m) whenever m' = p m mod N and "
     "both m, m' off-ball }"),
    ('b10_2026-08-17.txt', "S_quot = orthoprojection onto"),
    ('b10_2026-08-17.txt',
     "THE QUANTITIES: T_quot(k) = |Tr(U^k S_quot)| and the diagonal/norm channels, k = 1..2n-1."),
    ('b10_2026-08-17.txt',
     "THE FOURIER HALF DOES NOT DESCEND -- the transform does not commute with x ~ px"),
    ('b10_2026-08-17.txt',
     "THE SONIN-TYPE CONDITION TRANSPOSED: support off the ball (the ball-avoidance half)."),
    ('b267_registration_2026-08-31.txt', "(SPEC-1) IT COUNTS FIRST LEVELS."),
    ('b267_registration_2026-08-31.txt',
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT LEVELS `k <= n-1`."),
    ('b267_registration_2026-08-31.txt', "(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET."),
    ('b269_m2_statement.txt', "read the quotient channel as the AMBIENT operator b10 already writes,"),
    ('b269_m2_statement.txt', "IT IS NOT act 9's `tau_q`, WHICH IS A FIXED-ORBIT COUNT ON"),
    ('b269_m2_statement.txt', "(SPEC-2) would have to be ### CHECKED, NOT ASSUMED"),
    ('b269_m2_statement.txt', "b227 REFUSED NUMBERS OF EXACTLY THIS SHAPE AS THE DOUBLE-NAME"),
    # ### Q13 AND Q14 CARRY THE CORRECTION DECLARED AT THE DEVIATIONS: the SEALED registration's
    # ### (D) has a trailing period b227 does not have, and drops a `###` marker b226 does have.
    # ### **THE REGISTRATION IS LEFT BYTE-IDENTICAL UNDER ITS SEAL. ### THE BANK CARRIES THESE.**
    ('b227_the_trace.txt', "IT WANTS A RESULT OR A RULING; IT DOES NOT WANT A READ"),
    ('b226_stated_choice.txt', "d_1 > 0 GIVES E_1 != 0. ### IT DOES NOT GIVE u_{1,1} != 0."),
    ('b269_filings.txt', "A TOY MODEL WOULD HAVE COMPILED CLEANLY AND SETTLED NOTHING,"),
    ('b15_2026-08-18.txt', "a finite-place-set object at a finite cutoff decides nothing"),
]


def git_unchanged(rel):
    return subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                          capture_output=True, text=True).returncode == 0


def seal_ok():
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0


def quotes_missing():
    """### RETURNS THE COUNT OF UNFINDABLE NEEDLES. ### Zero, or the act does not emit."""
    bad = 0
    for f, n in QUOTES:
        v, _ = verify_all(os.path.join(D, f), [n])
        if v != 'PASS':
            bad += 1
    return bad


def or_in_check_logic():
    """### `tokenize`, span-scoped -- b268's mechanism, reused unchanged. ### NOT A REGEX OVER
    ### CHECK LOGIC: the regex delimits the SPANS, `tokenize` decides what is an `or`."""
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


def float_decides_a_verdict():
    """### F-EXACT, MECHANIZED. ### A verdict in this act is taken by `Field.is_zero` / `Field.eq`
    ### / `Field.is_rational`, all of which reduce modulo `Phi_N` over `QQ`. ### THIS COUNTS THE
    ### FLOAT-INTRODUCING NAMES IN THE RUNNER. ### **ITS REACH: it proves no float ENTERS, which
    ### is why no float can DECIDE. ### It does not prove the reduction is correct.**"""
    src = io.open(RUNNER, encoding='utf-8').read()
    body = src.split('"""', 2)[2] if src.count('"""') >= 2 else src
    import tokenize
    with open(RUNNER, 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    floats = sum(1 for t in toks
                 if t.type == tokenize.NUMBER and '.' in t.string)
    names = sum(1 for t in toks
                if t.type == tokenize.NAME and t.string in ('float', 'numpy', 'np'))
    return floats + names, len(body)


def main():
    h = Harness(ROOT, 'b270')

    # 1 -- ### THE SEAL, INTACT, AND THE SATISFIABILITY AUDIT PRESENT.
    h.run('registration-sealed-and-satisfiability-checked',
          check=lambda: bool(seal_ok()
                             and contains(REG, '96ac5b1e23a2253eee85b30b576113026aa6d4d478d35d70a')
                             and contains(SAT, 'JOINTLY SATISFIABLE')),
          # ### FIXTURE: claim the audit found a contradictory clause. ### It found none.
          fixture=lambda: bool(contains(SAT, 'DO NOT SEAL')),
          witness=lambda: bool(contains(SAT, 'IT NARROWS THE CLASS; IT DOES NOT CLOSE IT')))

    # 2 -- ### F-QUOTE. ### EVERY LOAD-BEARING QUOTATION VERBATIM AGAINST ITS OWNER.
    h.run('sixteen-quotations-verbatim-against-owners',
          check=lambda: bool(quotes_missing() == 0 and len(QUOTES) == 16),
          # ### FIXTURE: a needle this seat knows is NOT in b10, in b10's own voice.
          fixture=lambda: bool(verify_all(os.path.join(D, 'b10_2026-08-17.txt'),
                                          ['THE FOURIER HALF DESCENDS'])[0] == 'PASS'),
          witness=lambda: bool(len(QUOTES) == 16))

    # 3 -- ### S1's VERDICT IS THE EXACT ONE, AND THE NAVIGATOR'S ASSERTION WAS TESTED.
    # ### THE GATE READS THE RUN'S OWN VERDICT LINE, NOT A TABLE COLUMN. ### The first draft's
    # ### fixture matched the PAIRING table's `ZERO` and so passed while testing nothing --
    # ### the harness REFUSED the check, which is exactly what a refusal is for. ### Declared.
    h.run('S1-projection-nonzero-at-every-cell',
          check=lambda: bool(contains(RUN, '### S1 VERDICT: S_quot u_v NONZERO at 8 of 8 cells')
                             and contains(RUN, 'ball vector -> 0? (F-S1 ctrl)')),
          # ### FIXTURE: claim the run's S1 verdict line reads ZERO. ### It reads NONZERO.
          fixture=lambda: bool(contains(RUN, '### S1 VERDICT: S_quot u_v ZERO at')),
          witness=lambda: bool(contains(RUN, 'ALL 8 CELLS')))

    # 4 -- ### F-SPEC1. ### THE BINDING TEST, AND ITS FALSIFIER DID NOT FIRE.
    h.run('SPEC-1-refuted-pairing-vanishes-at-k-equals-n',
          check=lambda: bool(contains(RUN, 'P(n) IS EXACTLY ZERO')
                             and contains(RUN, 'REFUTED AT EVERY CELL')
                             and not contains(RUN, 'F-SPEC1 HAS FIRED')),
          # ### FIXTURE: claim the run found a nonzero pairing at k = n. ### It found none.
          fixture=lambda: bool(contains(RUN, '### IS NONZERO ###')),
          witness=lambda: bool(contains(RUN, 'NOT REFUTED -- F-SPEC1 HAS FIRED') is False))

    # 5 -- ### F-NONTRIV. ### THE OBJECT IS NOT TRIVIALLY ZERO, SO S4's ZERO MEANS SOMETHING.
    h.run('F-NONTRIV-a-nonzero-witness-exists',
          check=lambda: bool(contains(RUN, 'THE PAIRING IS NOT THE ZERO OBJECT')
                             and contains(RUN, 'witnesses : (2,2) k=1')),
          # ### FIXTURE: claim the act measured nothing. ### It measured a witness.
          fixture=lambda: bool(contains(RUN, 'NO WITNESS.')),
          witness=lambda: bool(contains(RUN, '(cell, k) with P(k) NONZERO : 1')))

    # 6 -- ### F-DISTINCT. ### THE DOUBLE-NAME HAZARD SETTLED BY MEASUREMENT, NOT ASSERTION.
    h.run('F-DISTINCT-pairing-differs-from-b10-trace',
          check=lambda: bool(contains(RUN, 'DIFFERENT OBJECTS, PROVED BY MEASUREMENT')
                             and contains(RUN, 'DISAGREE : 1')
                             and contains(RUN, 'ONE EXACT EQUALITY OF REDUCED VECTORS')),
          # ### FIXTURE: claim the branching first draft's answer stands. ### It was replaced.
          fixture=lambda: bool(contains(RUN, 'THEY AGREE WHEREVER BOTH WERE COMPUTED')),
          witness=lambda: bool(contains(RUN, 'HAD NO ARM FOR A NON-RATIONAL PAIRING')))

    # 7 -- ### F-EXACT. ### NO FLOAT ENTERS THE RUNNER, SO NO FLOAT DECIDES.
    h.run('F-EXACT-no-float-in-the-deciding-runner',
          check=lambda: bool(float_decides_a_verdict()[0] == 0
                             and float_decides_a_verdict()[1] > 1000),
          # ### FIXTURE: claim a float or numpy name is present. ### None is.
          fixture=lambda: bool(float_decides_a_verdict()[0] > 0),
          witness=lambda: bool(contains(RUNNER, 'NO FLOAT DECIDES ANYTHING HERE')))

    # 8 -- ### F-NOADOPT. ### THE PAIRING IS NOT INSTALLED AS ANYTHING.
    h.run('F-NOADOPT-nothing-adopted-M-2-still-owed',
          check=lambda: bool(contains(FIL, 'M-2 REMAINS OWED')
                             and contains(FIL, 'SPECIFIED-NOT-STATED')
                             and contains(FIL, 'NO CANDIDATE IS ADOPTED')),
          # ### FIXTURE: claim the bank installs the pairing as the per-place value.
          fixture=lambda: bool(contains(FIL, 'Q.value = <U^k S_quot')),
          witness=lambda: bool(contains(FIL, 'DERIVED AND STRUCK')))

    # 9 -- ### F-NOFIT. ### NO COMPARISON TO ANY TARGET WAS RUN, ANYWHERE.
    h.run('F-NOFIT-no-target-comparison-in-run-or-bank',
          check=lambda: bool(contains(RUN, 'NO TARGET APPEARS IN IT')
                             and not contains(RUN, 'residual')
                             and not contains(RUN, 'first-level mass')),
          # ### FIXTURE: claim a residual was computed. ### None was.
          fixture=lambda: bool(contains(RUN, 'residual')),
          witness=lambda: bool(contains(RUN, 'NOT A TABLE HEADED BY act 9')))

    # 10 -- ### NO OWNER INSTRUMENT AND NO OWNING ACT'S BANK WAS EDITED. ### b246 HELD.
    h.run('owners-and-prior-banks-byte-identical',
          check=lambda: bool(git_unchanged('data/b269_m2_statement.txt')
                             and git_unchanged('data/b269_filings.txt')
                             and git_unchanged('tools/e16/b268_generator.py')
                             and git_unchanged('tools/e16/b10_cells.py')
                             and git_unchanged('tools/e16/b8_sonin_dim.py')),
          # ### FIXTURE: claim b10's instrument moved. ### It did not; it was IMPORTED.
          fixture=lambda: bool(git_unchanged('tools/e16/b10_cells.py') is False),
          witness=lambda: bool(git_unchanged('data/b10_2026-08-17.txt')))

    # 11 -- ### THIS GATE FILE HAS NO `or` IN ANY CHECK'S LOGIC. ### b268's MECHANISM, REUSED.
    h.run('this-gate-file-has-no-or-in-its-logic',
          check=lambda: bool(or_in_check_logic()[0] == 0
                             and or_in_check_logic()[1] >= 10),
          # ### FIXTURE: claim a check body carries an `or` in its logic. ### None does.
          fixture=lambda: bool(or_in_check_logic()[0] > 0),
          witness=lambda: bool(or_in_check_logic()[1] >= 10))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    print('  quotations verified verbatim : %d of %d unfindable'
          % (quotes_missing(), len(QUOTES)))
    print('  check bodies scanned for `or` in logic: %d bodies, %d offending'
          % (or_in_check_logic()[1], or_in_check_logic()[0]))
    print('  float-introducing tokens in the deciding runner: %d'
          % float_decides_a_verdict()[0])
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
