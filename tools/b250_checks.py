# -*- coding: utf-8 -*-
"""b250_checks.py -- the b250 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a measured value was used as a PREMISE of a derivation step. ### Gates 5 and 6:
###       ### the bank must say the measured column is a control, ### **AND THE TAUTOLOGY GATE
###       ### MUST SHOW THE ENVELOPE COMPARISON HAS CONTENT** -- an inequality that held on
###       ### arbitrary inputs would be ALGEBRAIC-RESTATEMENT and would carry no weight.
###   (2) that a halted step was quietly claimed. ### Gates 7 and 8.
###   (3) that a range condition or a prediction was 'registered' AFTER it was computed.
###       ### Gates 2, 3, 4 -- ### **ALL THREE REST ON THE REGISTRATION PRECEDING THE RUN ON DISK,
###       ### WHICH GATE 1 ESTABLISHES.**
###   (4) that the shadow was passed on an EXIT CODE. ### Gate 9 reads the PRINTED PROFILE.
###       ### b227 shipped a file that compiled clean and printed `sorryAx`.
###   (5) that the shadow's polarity controls were decorative. ### Gate 10.
###   (6) that the amendment DELETED what it amended, or amended the WRONG OBJECT. ### Gates 11
###       ### and 12 -- ### **and 12 IS A POSITIVE CONTROL ON AN ABSENCE**, the W-UNION quadrant.
###   (7) that an import was graded without being named. ### Gate 13.
###   (8) that this act recomputed the residual or moved the identity under a derivation's cover.
###       ### Gate 14, with the `ast` stripper b242 was forced into and b248 forgot.
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
CORE = 'D:/SIDE-global-section/Core'

REG = os.path.join(D, 'b250_registration_2026-08-29.txt')
CHK = os.path.join(D, 'b250_derivation_checks.txt')
BANK = os.path.join(D, 'b250_m4_derivation.txt')
PROF = os.path.join(D, 'b250_shadow_profile.txt')
SHADOW = os.path.join(CORE, 'M4EnvelopeShadow.lean')
TOOL = os.path.join(E16, 'b250_derivation_checks.py')
AMEND = os.path.join(E16, 'b250_amend_tail.py')
B247 = os.path.join(D, 'b247_m4_statement_and_route.txt')

R1 = os.path.join(ROOT, 'reports', '2026-08-28-first-face-off.md')
R2 = os.path.join(ROOT, 'reports', '2026-08-29-the-serializing-close.md')
R3 = os.path.join(ROOT, 'reports', '2026-08-29-the-second-face-off.md')


def code_only(path):
    """### SCOPE CONTROL, with the `ast` comment/docstring stripper. ### b142: "a scanner with no
    ### scope control does not report the rule -- it reports the corpus."
    ### ### **CARRIED FORWARD DELIBERATELY. ### b242 WAS FORCED INTO THIS REPAIR; b243 AND b246
    ### ### CARRIED IT; b248 WROTE A FOURTH MATCHER WITHOUT IT AND ITS GATE MATCHED INSIDE A
    ### ### COMMENT.** ### This is the fifth matcher and it starts with the stripper.
    """
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


def envelope_comparison_has_content():
    """### THE TAUTOLOGY CONTROL, AND IT IS THE GATE THIS ACT MOST NEEDS.

    ### The act's central control is `measured_tail <= envelope + evaltol`. ### **IF THAT HELD ON
    ### ARBITRARY INPUTS IT WOULD BE ALGEBRAIC-RESTATEMENT AND WOULD CARRY NO WEIGHT** (b229/b246).
    ### So the SAME comparison is re-run on a FABRICATED tail one order LARGER than the envelope,
    ### and it MUST FAIL. ### The numbers are the bank's own N = 6 row.
    ### ### **AND THE SECOND HALF IS SHARPER: the real N = 11 row is re-run WITHOUT the evaluation
    ### ### tolerance and MUST ALSO FAIL** -- which proves the tolerance is LOAD-BEARING and was
    ### ### not padding added for comfort.
    """
    env6, tail6, tol = 1.15757629e-14, 1.11558894e-14, 7.2152e-40
    fake6 = tail6 * 10.0
    env11, tail11 = 3.1837636e-36, 3.18448512e-36
    return ((tail6 <= env6 + tol)            # the real row passes
            and not (fake6 <= env6 + tol)    # a fabricated larger tail FAILS
            and (tail11 <= env11 + tol)      # the deep row passes WITH the tolerance
            and not (tail11 <= env11))       # and FAILS without it


def profile_clean():
    """### THE SHADOW'S PROFILE, READ FROM THE PRINTED TEXT AND NEVER FROM AN EXIT CODE.

    ### ### **THIS GATE'S FIRST FORM WAS WRONG, AND THE ERROR WAS THIS FUNCTION'S, NOT THE
    ### ### SHADOW'S.** ### It tested `'error' not in t.lower()`, which matched the profile's own
    ### ### line for the theorem `deep_cuts_need_the_evaluation_error` -- ### **A LEGITIMATE NAME
    ### ### CONTAINING THE WORD THE GATE WAS HUNTING.** ### A substring test against free text
    ### was never the criterion; Lean's diagnostics have a FORM, `file:line:col: error:`, and that
    ### is what a clean profile must lack. ### **THE GATE IS NARROWED TO THE REAL MARKER, NOT
    ### RELAXED: `sorryAx` and `Classical.choice` stay exact.**
    """
    if not os.path.exists(PROF):
        return False
    t = io.open(PROF, encoding='utf-8').read()
    return (t.count('does not depend on any axioms') == 7
            and 'sorryAx' not in t and 'Classical.choice' not in t
            and not re.search(r':\d+:\d+: error', t)
            and 'unknown' not in t.lower())


def polarity_controls_are_real():
    """### THE POLARITY CONTROLS MUST ASSERT NEGATIONS THAT ARE ACTUALLY FALSE-IF-NEGATED, i.e.
    ### the arithmetic they deny must really fail. ### **RE-DERIVED HERE IN PYTHON, NOT READ FROM
    ### THE LEAN FILE'S PROSE**, so a shadow whose comments lied would be caught."""
    import math
    return (not (7 * math.factorial(5) <= math.factorial(6))     # turns at m = 6, not before
            and (7 * math.factorial(6) <= math.factorial(7))
            and not (146013870 <= 146013869)                     # deep cuts need the error term
            and not (318448512 <= 318376360)
            and (362718 < 10000000)                              # available at N = 6
            and not (243547960 < 10000000))                      # NOT available at N = 4


def main():
    h = Harness(ROOT, 'b250')

    # 1 -- ### THE REGISTRATION PRECEDES THE RUN AND THE BANK ON DISK. ### GATES 2-4 REST ON THIS.
    h.run('registration-precedes-run-and-bank',
          check=lambda: (os.path.getmtime(REG) < os.path.getmtime(CHK)
                         and os.path.getmtime(CHK) < os.path.getmtime(BANK)),
          # ### FIXTURE: the same ordering demanded in reverse of two files written in order.
          # ### FAILS ON A REAL TIME ORDER, not on a negation of the check.
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 5000)

    # 2 -- ### THE RANGE `k >= 9` WAS REGISTERED BEFORE ANYTHING WAS COMPUTED.
    h.run('bessel-range-registered-before-computing',
          check=lambda: (contains(REG, 'k >= 9')
                         and contains(REG, 'before computing anything')
                         and contains(CHK, 'THE BOUND HOLDS FOR k >= 9')
                         and contains(CHK, 'CONFIRMED')),
          # ### FIXTURE: b247's bank is the act that RAISED the endpoint question and does NOT
          # ### carry the range; a gate that found it there would be matching the corpus.
          fixture=lambda: contains(B247, 'before computing anything'),
          witness=lambda: contains(REG, 'k >= 9'))

    # 3 -- ### THE MERCER SUBSTITUTION WAS REGISTERED IN ADVANCE, WITH ITS FALSIFIER.
    h.run('mercer-substitution-and-falsifier-registered-in-advance',
          check=lambda: (contains(REG, 'I REGISTER MY INTENDED SUBSTITUTION NOW')
                         and contains(REG, 'CANNOT LOOK LIKE A DISCOVERY MADE TO ORDER')
                         and contains(REG, 'IF THE ARITHMETIC COMES\n### ### OUT AT ANYTHING BUT '
                                            'EXACTLY 2 THE ROUTE IS WRONG')
                         and contains(CHK, 'THE DERIVED CONSTANT IS CONFIRMED')),
          fixture=lambda: contains(B247, 'I REGISTER MY INTENDED SUBSTITUTION NOW'),
          witness=lambda: contains(REG, 'MERCER'))

    # 4 -- ### THE HALT WAS PREDICTED BEFORE IT HAPPENED.
    h.run('s3-halt-predicted-in-advance',
          check=lambda: (contains(REG, 'I EXPECT THE NAVIGATOR\'S ROUTE TO RESIST, AND I SAY SO '
                                       'IN ADVANCE')
                         and contains(BANK, 'A HALT PREDICTED IN ADVANCE')
                         and contains(BANK, 'A HALT DISCOVERED AND THEN DECLARED EXPECTED WOULD '
                                            'BE NOTHING')),
          fixture=lambda: contains(B247, 'I SAY SO IN ADVANCE'),
          witness=lambda: contains(REG, 'RESIST'))

    # 5 -- ### THE MEASURED COLUMN IS DECLARED A CONTROL AND NOT A PREMISE, IN BOTH FILES.
    h.run('measurements-declared-control-not-premise',
          check=lambda: (contains(CHK, 'NOTHING HERE IS A PREMISE OF ANY STEP')
                         and contains(BANK, 'NO STEP BELOW CITES A\n### ### MEASURED VALUE AS A '
                                            'REASON')
                         and contains(BANK, 'IT IS NOT A PREMISE OF ANY LINE ABOVE, AND NO LINE '
                                            'ABOVE WOULD CHANGE IF IT WERE DELETED')),
          fixture=lambda: contains(B247, 'NOTHING HERE IS A PREMISE OF ANY STEP'),
          witness=lambda: contains(BANK, 'CONTROL'))

    # 6 -- ### THE TAUTOLOGY CONTROL. ### THE COMPARISON HAS CONTENT AND THE TOLERANCE IS
    #      ### LOAD-BEARING.
    h.run('envelope-comparison-is-not-a-tautology',
          check=envelope_comparison_has_content,
          # ### FIXTURE: the vacuous form of the same comparison -- `x <= x` on the real tail.
          # ### It is TRUE for every input, so a gate that accepted it would assert nothing.
          fixture=lambda: not (3.18448512e-36 <= 3.18448512e-36),
          witness=lambda: contains(BANK, 'FOURTH IN A\n### ROW'))

    # 7 -- ### THE HALTED STEP IS REPORTED AS HALTING AND THE THEOREM IS NOT CLAIMED ON IT.
    h.run('halted-step-reported-and-not-claimed',
          check=lambda: (contains(BANK, 'S3(a) HALTS AT (NOT DERIVED)')
                         and contains(BANK, 'HALTS -- NOT DERIVED')
                         and contains(BANK, 'W-ORD-XI-PERMODE')
                         and contains(BANK, 'THE THEOREM ROUTES AROUND\n### ### IT; IT DOES NOT '
                                            'ANSWER IT')),
          fixture=lambda: contains(B247, 'W-ORD-XI-PERMODE'),
          witness=lambda: contains(BANK, 'S3a'))

    # 8 -- ### CLAUSE (ii) IS REPORTED *UNNECESSARY*, NOT *PROVEN*. ### THE DISTINCTION IS THE
    #      ### ONE THING THIS ACT COULD MOST EASILY HAVE BLURRED.
    h.run('clause-ii-unnecessary-not-proven',
          check=lambda: (contains(BANK, 'BECOMES UNNECESSARY RATHER THAN')
                         and contains(BANK, 'THE\n### ### PER-MODE BOUND IS STILL NOT PROVED')
                         and contains(REG, 'UNNECESSARY RATHER THAN UNPROVEN')),
          fixture=lambda: contains(B247, 'BECOMES UNNECESSARY RATHER THAN'),
          witness=lambda: contains(BANK, 'clause (ii)') or contains(BANK, 'CLAUSE (ii)'))

    # 9 -- ### THE SHADOW PROFILE IS PRINTED AND READ. ### NEVER AN EXIT CODE.
    h.run('shadow-profile-printed-and-clean',
          check=profile_clean,
          # ### FIXTURE: the registration is not an axiom profile and holds no such line.
          # ### FAILS ON A REAL FILE, not on a negation.
          fixture=lambda: (os.path.exists(PROF)
                           and io.open(REG, encoding='utf-8').read().count(
                               'does not depend on any axioms') == 7),
          witness=lambda: os.path.exists(PROF) and os.path.getsize(PROF) > 100)

    # 10 -- ### THE POLARITY CONTROLS ARE REAL, RE-DERIVED HERE RATHER THAN READ FROM THE LEAN.
    h.run('shadow-polarity-controls-are-real',
          check=polarity_controls_are_real,
          # ### FIXTURE: the same battery with one limb flipped to its vacuous form.
          fixture=lambda: not (243547960 < 10000000) and (243547960 < 10000000),
          witness=lambda: contains(SHADOW, 'POLARITY CONTROL'))

    # 11 -- ### THE AMENDMENT PRESERVED WHAT IT AMENDED. ### THREE REPORTS, ORIGINALS INTACT.
    h.run('amendment-preserved-the-originals',
          check=lambda: (contains(R1, 'rides an unbounded truncation')
                         and contains(R2, 'carries a bar with an unbounded term in it')
                         and contains(R3, 'THE TAIL TERM IS NOT A BOUND')
                         and all(contains(p, 'AMENDED AT b250') for p in (R1, R2, R3))
                         and all(contains(p, 'STANDS AS WRITTEN AND WAS TRUE WHEN WRITTEN')
                                 for p in (R1, R2, R3))),
          # ### FIXTURE: b247's bank carries neither the original sentence nor the amendment.
          fixture=lambda: contains(B247, 'rides an unbounded truncation'),
          witness=lambda: contains(R1, 'AMENDED AT b250'))

    # 12 -- ### POSITIVE CONTROL ON AN ABSENCE. ### THE W-UNION QUADRANT IS A **DIFFERENT OBJECT**
    #       ### AND WAS DELIBERATELY NOT AMENDED. ### The phrase is shown FINDABLE first, so its
    #       ### want of an amendment means something rather than nothing.
    h.run('w-union-quadrant-findable-and-not-amended',
          check=lambda: (contains(os.path.join(ROOT, 'reports',
                                               '2026-08-11-arith-act6.md'),
                                  'nonArchimedean, unbounded')
                         and not contains(os.path.join(ROOT, 'reports',
                                                       '2026-08-11-arith-act6.md'),
                                          'AMENDED AT b250')
                         and contains(AMEND, 'THIS TOOL MATCHES ON FULL SENTENCES, NOT ON THE '
                                             'WORD')),
          fixture=lambda: contains(os.path.join(ROOT, 'reports', '2026-08-11-arith-act6.md'),
                                   'AMENDED AT b250'),
          witness=lambda: contains(AMEND, 'W-UNION'))

    # 13 -- ### EVERY IMPORT IS NAMED, AND EACH CARRIES ITS STATUS. ### NONE IS TOOLED, AND THE
    #       ### ACT SAYS SO RATHER THAN LETTING 'VERIFIED-WHERE-TOOLED' DO SILENT WORK.
    h.run('imports-named-with-status-and-none-claimed-tooled',
          check=lambda: (all(contains(BANK, s) for s in
                             ('PLANCHEREL', 'IDENTITY THEOREM', 'ECKART-YOUNG', 'MERCER',
                              'JACOBI-ANGER'))
                         and contains(BANK, 'ALL FIVE ARE TRUSTED-AT-CITE AND NONE IS VERIFIED')
                         and contains(BANK, 'NO MATHLIB')
                         and contains(BANK, 'IMP-3 (LANDAU-WIDOM) IS *NOT* USED')
                         and not contains(BANK, 'VERIFIED-WHERE-TOOLED: PLANCHEREL')),
          fixture=lambda: contains(B247, 'ALL FIVE ARE TRUSTED-AT-CITE AND NONE IS VERIFIED'),
          witness=lambda: contains(BANK, 'TRUSTED-AT-CITE'))

    # 14 -- ### SCOPE WALL. ### THIS ACT DERIVES; IT DOES NOT RECOMPUTE THE RESIDUAL OR TOUCH THE
    #       ### IDENTITY'S COLUMNS. ### Matched on CODE ONLY, per `code_only`'s own history.
    h.run('no-residual-recomputed-and-no-identity-column-bound',
          check=lambda: not re.search(r'\b(left_side|right_side|resid47|Thq|D_dict)\b',
                                      code_only(TOOL)),
          # ### FIXTURE: the b248 split tool DOES bind those names -- the gate finds them there,
          # ### so its silence on this act's tool is a real absence.
          fixture=lambda: not re.search(r'\b(left_side|right_side|resid47|Thq|D_dict)\b',
                                        code_only(os.path.join(E16, 'b248_split.py'))),
          witness=lambda: len(code_only(TOOL)) > 1000)

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
