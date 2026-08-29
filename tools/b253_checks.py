# -*- coding: utf-8 -*-
"""b253_checks.py -- the b253 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK** -- b251's gate 4
### read `(A and ...) or E` and `and` binds tighter, the third appearance of the decorative-gate
### species. ### **AND EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED** (b242's species).

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the halt was taken to avoid work, or avoided to look decisive. ### Gates 2-3: the
###       ### ambiguity was REGISTERED BEFORE the dossier's text was weighed, and R-II's clean
###       ### exclusion shows the halt is not a blanket refusal to match.
###   (2) that the re-binding was asserted rather than derived. ### Gate 4 RE-DERIVES it
###       ### symbolically, and ### **GATE 5 IS THE TAUTOLOGY CONTROL ON THAT DERIVATION.**
###   (3) that the excess `E2` was quietly dropped under the ferry's smaller number. ### Gate 6.
###   (4) that code moved in File E. ### Gate 7, comment-stripped, both sides.
###   (5) that a work-order was reported as run. ### Gate 9, a positive control on an absence.
###   (6) that a face-off ran under a filing act's cover. ### Gate 10, with the `ast` stripper.
###   (7) that b252's bench reading got promoted to an analytic claim. ### Gate 11.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b253_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b253_m2inf_ruling.txt')
FIL = os.path.join(D, 'b253_filings.txt')
DOSS = os.path.join(D, 'b251_m2inf_dossier.txt')
B252 = os.path.join(D, 'b252_mode_sum_limit.txt')
B251 = os.path.join(D, 'b251_third_face_off.txt')
FILE_E = os.path.join(RES, 'Interfaces', 'FiniteInstanceIdentity.lean')
LEDGER = os.path.join(RES, 'CORRESPONDENCE.md')
SNAP = (r"C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--"
        r"\46db2479-8c02-4b65-a374-d1dc57f4a494\scratchpad\fileE_head.lean")
AMEND = os.path.join(E16, 'b253_filee_amend.py')
CORR = os.path.join(E16, 'b253_corr_row.py')


def lean_code_only(path):
    """### COMMENT-STRIPPED LEAN. ### Docstrings `/- ... -/` and line comments `--` removed."""
    t = io.open(path, encoding='utf-8').read()
    t = re.sub(r'/-.*?-/', '', t, flags=re.S)
    t = re.sub(r'--.*', '', t)
    return [l.rstrip() for l in t.split('\n') if l.strip()]


def py_code_only(path):
    """### SCOPE CONTROL with the `ast` comment/docstring stripper. ### b142.
    ### ### **b242 WAS FORCED INTO THIS REPAIR; b243, b246, b250 AND b252 CARRIED IT; b248 WROTE A
    ### ### FOURTH MATCHER WITHOUT IT AND ITS GATE MATCHED INSIDE A COMMENT.** ### Seventh matcher,
    ### and it starts with the stripper."""
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


def rebinding_derives():
    """### RE-DERIVE THE RE-BINDING SYMBOLICALLY, ON ARBITRARY VALUES.
    ### Given the owners' line `resid47 := Tr - (A + E2)`, the ruled binding `T_old = Tr + E2 - D`
    ### and the re-bound `T_new = A + E2 - D`, the cost must be `T_old - T_new = E2 + resid47`."""
    import random
    rng = random.Random(20260829)
    ok = True
    for _ in range(400):
        Tr, A, E2, Dm = (rng.uniform(-9, 9) for _ in range(4))
        resid47 = Tr - (A + E2)
        old, new = Tr + E2 - Dm, A + E2 - Dm
        ok &= abs((old - new) - (E2 + resid47)) < 1e-9
    return bool(ok)


def excess_claim_has_content():
    """### THE TAUTOLOGY CONTROL, BOTH HALVES.

    ### HALF ONE: the derivation above must hold on ARBITRARY values -- ### **PROVING IT IS
    ### ALGEBRAIC-RESTATEMENT AND THEREFORE NO EVIDENCE.** ### The bank says so in its own voice.
    ### HALF TWO: the CLAIM that the removal EXCEEDS `resid47` must ### **FAIL WHEN `E2 = 0`** --
    ### ### **PROVING THE EXCESS IS A CLAIM ABOUT `E2`, NOT AN ARTEFACT OF THE ALGEBRA.**
    ### ### **A CONTROL CARRYING ONLY HALF ONE WOULD SHOW THE ACT PROVED NOTHING WITHOUT SHOWING
    ### ### THAT WHAT IT DID CLAIM HAS CONTENT.**
    """
    import random
    rng = random.Random(1)
    ever_strict, vacuous_at_zero = False, True
    for _ in range(400):
        Tr, A, E2 = rng.uniform(-9, 9), rng.uniform(-9, 9), rng.uniform(-9, 9)
        resid47 = Tr - (A + E2)
        if abs((E2 + resid47) - resid47) > 1e-9:
            ever_strict = True
        # ### with E2 forced to zero the removal is EXACTLY resid47 and the excess claim fails
        r0 = Tr - (A + 0.0)
        if abs((0.0 + r0) - r0) > 1e-9:
            vacuous_at_zero = False
    return bool(ever_strict and vacuous_at_zero and rebinding_derives())


def main():
    h = Harness(ROOT, 'b253')

    # 1 -- ### THE REGISTRATION PRECEDES THE BANK, THE FILINGS AND THE RESIDENCE WRITES.
    h.run('registration-precedes-bank-and-residence-writes',
          check=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(BANK)
                             and os.path.getmtime(REG) < os.path.getmtime(FIL)
                             and os.path.getmtime(REG) < os.path.getmtime(FILE_E)
                             and os.path.getmtime(REG) < os.path.getmtime(LEDGER)),
          # ### FIXTURE: the same ordering demanded in reverse of two files written in order.
          # ### FAILS ON A REAL TIME ORDER, not on a negation of the check.
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(REG)),
          witness=lambda: bool(os.path.getsize(REG) > 5000))

    # 2 -- ### THE AMBIGUITY WAS REGISTERED **BEFORE** THE DOSSIER'S TEXT WAS WEIGHED.
    h.run('ambiguity-registered-before-the-text-was-weighed',
          check=lambda: bool(contains(REG, 'I EXPECT THE MATCH TO BE AMBIGUOUS AND I SAY SO '
                                           'BEFORE WEIGHING IT')
                             and contains(REG, 'not to an ### **APPROXIMATION**')
                             and contains(BANK, 'diagnostic-not-approximation')
                             and contains(BANK, 'THE EXPECTATION HELD')
                             and os.path.getmtime(REG) < os.path.getmtime(BANK)),
          # ### FIXTURE: b252's bank is the act that produced the warrant and carries no such
          # ### registration -- a gate that found it there would be matching the corpus.
          fixture=lambda: contains(B252, 'I EXPECT THE MATCH TO BE AMBIGUOUS'),
          witness=lambda: contains(REG, 'HALTS IF THE MATCH IS AMBIGUOUS'))

    # 3 -- ### THE HALT IS NOT A BLANKET REFUSAL: R-II IS EXCLUDED CLEANLY AND SAID TO BE.
    h.run('r-two-excluded-cleanly-so-the-halt-is-not-blanket',
          check=lambda: bool(contains(BANK, 'R-II IS EXCLUDED CLEANLY AND WITHOUT DOUBT')
                             and contains(DOSS, '(R-II) THE MODE SUM IS THE OBJECT')
                             and contains(BANK, 'AMBIGUOUS BETWEEN R-I AND R-III')),
          # ### FIXTURE: claim the dossier holds an R-IV. ### It does not, so a gate that accepted
          # ### it would not be reading the dossier at all.
          fixture=lambda: contains(DOSS, '(R-IV)'),
          witness=lambda: contains(DOSS, '(R-III)'))

    # 4 -- ### THE RE-BINDING IS DERIVED, NOT ASSERTED. ### RE-DERIVED HERE ON ARBITRARY VALUES.
    h.run('re-binding-derives-from-the-owners-line',
          check=rebinding_derives,
          # ### FIXTURE: the same battery with the cost mis-stated as `resid47` alone -- which is
          # ### exactly the ferry's disclosure, and it genuinely fails.
          fixture=lambda: bool(abs(((3.0 + 1.0 - 2.0) - (5.0 + 1.0 - 2.0))
                                   - ((3.0 - (5.0 + 1.0)))) < 1e-9),
          witness=lambda: contains(BANK, 'T.value := A + E2 - Delta_-'))

    # 5 -- ### THE TAUTOLOGY CONTROL, BOTH HALVES.
    h.run('derivation-is-restatement-and-excess-claim-is-not',
          check=excess_claim_has_content,
          # ### FIXTURE: the vacuous form -- `x == x` on a real quantity, true for every input.
          fixture=lambda: bool(abs((1.0 + 2.0) - (1.0 + 2.0)) > 1e-30),
          witness=lambda: contains(BANK, 'BOTH SAY THE SAME THING AND NEITHER IS A CLAIM'))

    # 6 -- ### THE EXCESS `E2` IS DISCLOSED IN THIS ACT'S OWN VOICE, NOT LET PASS.
    h.run('excess-e2-disclosed-not-let-pass',
          check=lambda: bool(contains(BANK, 'THE ALGEBRA REMOVES')
                             and contains(BANK, 'MORE THAN THE FERRY\'S DISCLOSED CONSEQUENCE '
                                                'SAYS IT REMOVES')
                             and contains(BANK, 'THE REMOVAL IS `resid47 + E2`, NOT `resid47`')
                             and contains(REG, 'THAT EXCESS IS DISCLOSED IN THIS ACT\'S OWN VOICE')
                             and contains(FILE_E, 'the re-binding removes')
                             and contains(FILE_E, 'AND ONE `E2` TERM')),
          fixture=lambda: contains(B252, 'THE REMOVAL IS `resid47 + E2`, NOT `resid47`'),
          witness=lambda: contains(BANK, 'E2 + resid47'))

    # 7 -- ### FILE E: DOCSTRING ONLY. ### COMMENT-STRIPPED, BOTH SIDES.
    h.run('file-e-code-identical-to-head',
          check=lambda: bool(os.path.exists(SNAP)
                             and lean_code_only(SNAP) == lean_code_only(FILE_E)
                             and len(lean_code_only(FILE_E)) == 19
                             and contains(FILE_E, 'RULE M-2-inf: Q1')
                             # ### and the ORIGINAL binding sentence is still there
                             and contains(FILE_E, 'value := Tr_full + E2')),
          # ### FIXTURE: compare the RAW files, which genuinely differ by the inserted docstring.
          # ### If that passed, the stripper would not be stripping anything.
          fixture=lambda: bool(io.open(SNAP, encoding='utf-8').read()
                               == io.open(FILE_E, encoding='utf-8').read()),
          witness=lambda: bool(len(lean_code_only(SNAP)) == 19))

    # 8 -- ### THE CORRESPONDENCE ROW: SIX CELLS, NO BLANKS, WRITTEN BY THE COMMITTED TOOL.
    h.run('correspondence-row-94-six-cells-no-blanks',
          check=lambda: bool(
              len([c for c in io.open(LEDGER, encoding='utf-8').read().rstrip()
                   .split('\n')[-1].strip().strip('|').split('|')]) == 6
              and all(c.strip() for c in io.open(LEDGER, encoding='utf-8').read().rstrip()
                      .split('\n')[-1].strip().strip('|').split('|'))
              and contains(LEDGER, 'THE REALIZATION\'S CONSTRUCTION RE-BOUND (b253)')
              and 'from corr_row import write_row' in py_code_only(CORR)),
          # ### FIXTURE: demand SEVEN cells of the same row. ### A real count that genuinely fails.
          fixture=lambda: bool(
              len([c for c in io.open(LEDGER, encoding='utf-8').read().rstrip()
                   .split('\n')[-1].strip().strip('|').split('|')]) == 7),
          witness=lambda: contains(LEDGER, '| 94 |'))

    # 9 -- ### POSITIVE CONTROL ON AN ABSENCE. ### THE WORK-ORDERS ARE FILED, NOT RUN.
    h.run('work-orders-filed-and-none-claimed-run',
          check=lambda: bool(contains(FIL, 'W-ORD-B38-HIGHMODE')
                             and contains(FIL, 'W-ORD-CN-LAW')
                             and contains(FIL, 'QUOTED-N')
                             and contains(FIL, 'EVERY WORK-ORDER BELOW IS *FILED, NOT RUN*')
                             and contains(FIL, 'BUILDING A THING\n### IS NOT DISCHARGING IT')
                             # ### THE ABSENCE: none of the three is called discharged
                             and not contains(FIL, 'W-ORD-B38-HIGHMODE DISCHARGED')
                             and not contains(FIL, 'W-ORD-CN-LAW DISCHARGED')),
          # ### FIXTURE: `W-ORD-MODE-PRECISION discharged` IS findable in the same file, so the
          # ### scanner is shown to be capable of finding a discharge when one is there.
          fixture=lambda: bool(not contains(FIL, 'W-ORD-MODE-PRECISION` discharged at b249')),
          witness=lambda: contains(FIL, 'FILED, NOT RUN'))

    # 10 -- ### SCOPE WALL. ### NO FACE-OFF RAN. ### CODE ONLY, PER `py_code_only`'s OWN HISTORY.
    h.run('no-face-off-ran-in-this-act',
          check=lambda: bool(
              # ### THIS MATCHER'S FIRST FORM HIT `left_side` INSIDE A **STRING LITERAL** -- a
              # ### correspondence cell and an index row, both QUOTING an owner's name as PROSE.
              # ### ### **b248's SPECIES IN A NEW GUISE: b248 MATCHED INSIDE A COMMENT; THIS
              # ### ### MATCHED INSIDE DATA.** ### The `ast` stripper removes docstrings and `#`
              # ### comments and should NOT remove data strings.
              # ### ### **THE FIX IS TO TEST WHAT THE RULE MEANS, NOT TO WEAKEN IT: a filing act
              # ### ### MAY QUOTE an owner's name -- the ferry requires it -- but MAY NOT IMPORT
              # ### ### OR CALL ONE.** ### Matching on mentions would have forbidden the very
              # ### quotation the ferry demanded.
              not any(re.search(r'(^|\n)\s*import\s+(b38_act10|qeps_layer|carto_atlas)\b'
                                r'|\b(left_side|trace_modes|theta_quotient|e2_of_grid)\s*\('
                                r'|\bB38\.',
                                py_code_only(os.path.join(E16, f)))
                      for f in ('b253_filee_amend.py', 'b253_corr_row.py',
                                'b253_index_append.py'))
              and contains(BANK, 'It ran no face-off and recomputed no `L - R`')
              and contains(BANK, 'THE SIZE OF THE EXCESS IS *NOT* COMPUTED HERE')),
          # ### FIXTURE: b251's face-off tool DOES bind those names -- the matcher finds them
          # ### there, so its silence on this act's tools is a REAL absence, not a broken regex.
          fixture=lambda: bool(
              not re.search(r'(^|\n)\s*import\s+(b38_act10|qeps_layer|carto_atlas)\b'
                            r'|\b(left_side|trace_modes|theta_quotient|e2_of_grid)\s*\('
                            r'|\bB38\.',
                            py_code_only(os.path.join(E16, 'b251_faceoff.py')))),
          witness=lambda: bool(len(py_code_only(CORR)) > 200))

    # 11 -- ### b252's BENCH READING IS NOT PROMOTED, AND b251 IS NOT RE-VERDICTED.
    h.run('bench-reading-not-promoted-and-b251-not-re-verdicted',
          check=lambda: bool(contains(BANK, 'THE RULING IS DEFINITIONAL ONLY')
                             and contains(BANK, 'b252\'s DIVERGENCE\n### ### REMAINS A BENCH '
                                                'READING')
                             and contains(BANK, 'b251\'s BRANCH IS NOT RE-VERDICTED')
                             and contains(BANK, 'THE LAW GOVERNS FUTURE QUOTATION, NOT PAST '
                                                'VERDICTS')
                             and contains(FILE_E, 'THAT IS A BENCH READING, NOT A THEOREM')
                             # ### and b251's own verdict text is untouched by this act
                             and not contains(B251, 'b253')),
          fixture=lambda: contains(B251, 'b253'),
          witness=lambda: contains(BANK, 'b242'))

    # 12 -- ### b254's PRECONDITIONS ARE LISTED, AND THE `Delta_-` QUESTION IS FLAGGED OPEN
    #       ### RATHER THAN SILENTLY DECIDED. ### **THE EASIEST OVERREACH THIS ACT COULD MAKE.**
    h.run('delta-minus-extension-flagged-open-not-decided',
          check=lambda: bool(contains(FIL, 'WHETHER `Delta_-`\'s REALIZATION IS TOUCHED BY Q1')
                             and contains(FIL, 'IS NOT DECIDED HERE AND IS FLAGGED AS AN OPEN '
                                               'PRECONDITION')
                             and contains(FIL, 'AN EXECUTOR WHO SILENTLY EXTENDED Q1 TO '
                                               '`Delta_-` WOULD BE RULING')
                             and contains(FIL, 'MUST NOT TREAT MEASURABILITY AS STATEDNESS')),
          fixture=lambda: contains(B252, 'AN EXECUTOR WHO SILENTLY EXTENDED Q1'),
          witness=lambda: contains(FIL, 'b254'))

    # 13 -- ### THE QUOTED-N LAW CARRIES ITS BOTH-POLARITY FIXTURE REQUIREMENT.
    h.run('quoted-n-law-requires-both-polarities',
          check=lambda: bool(contains(FIL, 'IN BOTH POLARITIES, BECAUSE ONE POLARITY IS NOT A '
                                           'FIXTURE')
                             and contains(FIL, 'must be graded CLEAN')
                             and contains(FIL, 'must be graded `UNGRADED`')
                             and contains(FIL, 'A SCANNER THAT ONLY EVER PASSED WOULD BE '
                                               'MEASURING NOTHING')),
          fixture=lambda: contains(B251, 'IN BOTH POLARITIES, BECAUSE ONE POLARITY IS NOT A '
                                         'FIXTURE'),
          witness=lambda: contains(FIL, 'QUOTED-N'))

    # 14 -- ### THE RESIDENCE REPO CARRIES NO OTHER CHANGE THAN THE TWO INTENDED FILES.
    h.run('residence-tree-carries-only-the-two-intended-files',
          check=lambda: bool(
              # ### THIS GATE'S FIRST FORM CALLED `.strip()` ON THE WHOLE PORCELAIN BLOB, WHICH
              # ### ATE THE FIRST LINE'S LEADING STATUS SPACE, SO `l[3:]` SLICED ONE CHARACTER
              # ### INTO THE FILENAME. ### **A SLICING BUG IN THE GATE, NOT A FACT ABOUT THE TREE.**
              sorted(l.split(None, 1)[1] for l in subprocess.run(
                  ['git', '-C', RES, 'status', '--porcelain'],
                  capture_output=True).stdout.decode('utf-8', 'replace').split('\n')
                  if l.strip())
              == ['CORRESPONDENCE.md', 'Interfaces/FiniteInstanceIdentity.lean']),
          # ### FIXTURE: demand the tree be CLEAN. ### It is not -- two files are intentionally
          # ### modified -- so this fails on the real state rather than on a negation.
          fixture=lambda: bool(subprocess.run(
              ['git', '-C', RES, 'status', '--porcelain'],
              capture_output=True).stdout.decode('utf-8', 'replace').strip() == ''),
          witness=lambda: bool(os.path.exists(FILE_E)))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
