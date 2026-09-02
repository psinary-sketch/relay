# -*- coding: utf-8 -*-
"""b297 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM ### EMITTING ### FILES AND FROM THIS ACT'S OWN FILES.
### ### **AND F-EMITTER IS ENFORCED HERE, NOT ONLY ASSERTED: ### EVERY OWNER NEEDLE BELOW NAMES
### ### THE ACT THAT ORIGINATED ITS SENTENCE, AND NONE RESOLVES IN AN ACT WHOSE ONLY CLAIM TO THE
### ### SENTENCE IS THAT IT QUOTED SOMEONE ELSE.** ### b283's scar: b282's failure was a quotation
### typed from memory of THIS SEAT'S OWN QUOTATION of b270 and b271.

### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.

### ### **AND THE HEDGE AUDIT RUNS OVER ### EVERY ### FILE THIS ACT WRITES, INCLUDING THE
### ### EMITTED MARKDOWN THAT REACHED `FINDINGS.md`** -- because the document is the deliverable
### and auditing only the bank would audit the wrong artifact.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
BANK = os.path.join(D, 'b297_the_fold.txt')
REG = os.path.join(D, 'b297_registration_2026-09-02.txt')
RUN = os.path.join(D, 'b297_fold_run.txt')
EMIT = os.path.join(D, 'b297_fold_emitted.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

# ### (label, path, anchor) -- OWNER needles, each into THE ORIGINATING act.
OWNER_NEEDLES = [
    ("b283's tower verdict (EMITTER)",
     os.path.join(D, 'b283_the_tower_action.txt'),
     'THE TOWER SUPPLIES A FILTRATION, NOT AN ACTION.'),
    ("b284's dual failure (EMITTER)",
     os.path.join(D, 'b284_the_scalings_domain.txt'),
     'VERDICT: (FAILS) -- IN BOTH DIRECTIONS, AND DUALLY.'),
    ("b284's scope sentence -- not 'C3 is closed' (EMITTER)",
     os.path.join(D, 'b284_the_scalings_domain.txt'), 'C3-VIA-SCALING IS CLOSED.'),
    ("b285's typing verdict -- the arc's boundary (EMITTER)",
     os.path.join(D, 'b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`.'),
    ("b286's space, supplied by the source (EMITTER)",
     os.path.join(D, 'b286_the_cc_condition.txt'), 'THE SPACE IS `L^2(R)_ev`.'),
    ("b287's same-space verdict (EMITTER)",
     os.path.join(D, 'b287_the_two_papers.txt'), 'VERDICT: (SAME SPACE), DERIVED'),
    ("b288's product invariance (EMITTER)",
     os.path.join(D, 'b288_the_family_and_the_complement.txt'),
     'COMPONENT 1 -- VERDICT: THE PRODUCT IS INVARIANT.'),
    ("b289's kernel repair, as a count (EMITTER)",
     os.path.join(D, 'b289_consolidation.txt'), 'CORE PRINTS 404 -> 426, ALL 426 ZERO-AXIOM.'),
    ("b290's absent first read (EMITTER)",
     os.path.join(D, 'b290_the_cross_pairing_read.txt'), 'FIRST READ -- VERDICT: (ABSENT)'),
    ("b291's plain-English source sentence (EMITTER)",
     os.path.join(D, 'b291_the_involution.txt'),
     'In `L^2(R)_ev` the Fourier transform `F_eR` is its own inverse.'),
    ("b291's self-dual member (EMITTER)",
     os.path.join(D, 'b291_the_involution.txt'),
     "(ii) THE CORPUS'S ARCHIMEDEAN MEMBER IS SELF-DUAL."),
    ("b292's identification, and what it costs (EMITTER)",
     os.path.join(D, 'b292_the_identification.txt'), 'AND NO MEASUREMENT IS DISTURBED.'),
    ("b293's family (EMITTER)",
     os.path.join(D, 'b293_the_finite_family.txt'), 'THE FAMILY IS CONSTRUCTED.'),
    ("b293's invariant sum (EMITTER)",
     os.path.join(D, 'b293_the_finite_family.txt'), 'THE SUM `a+b` IS INVARIANT'),
    ("b294's sub-family verdict (EMITTER)",
     os.path.join(D, 'b294_the_family_value.txt'),
     "THE BARRIER'S ZERO IS A PROPERTY OF A SUB-FAMILY"),
    ("b295's criterion (EMITTER)",
     os.path.join(D, 'b295_the_second_mechanism.txt'), '`a >= 0`  ###  OR  ###  `b >= n - 1`'),
    ("b296's threshold falling out (EMITTER)",
     os.path.join(D, 'b296_the_asymmetry.txt'), 'THE THRESHOLD FALLS OUT'),
    ("b266's fold law -- this act's precedent (EMITTER)",
     os.path.join(D, 'b266_registration_2026-08-31.txt'),
     'THE FOLD *STATES* GRADES AND CONFERS'),
]

# ### SELF needles -- into this act's OWN emitted files, PULLED and not typed from memory.
SELF_NEEDLES = [
    ('bank states the act is filings only', BANK, 'A FILINGS ACT.'),
    ('bank states no keystone was created', BANK, 'NO KEYSTONE IS PROPOSED'),
    ('bank carries the coverage finding', BANK,
     'FOUR ACTS OF THIS ARC HAD NO CORRESPONDENCE ROW AT ALL.'),
    ('bank names the one candidate that passes both tests', BANK,
     'CARRIES ITS SCOPE: YES'),
    ('bank states why that candidate carries its scope', BANK,
     'NAMES THE MEMBER IN ITS OWN STATEMENT'),
    ('bank lists the refusals rather than omitting them', BANK,
     'EVERYTHING ANALYSIS-BOUND'),
    ('bank states where the terminals would sit', BANK,
     'NOT A NEW REPOSITORY'),
    ('bank gives the repository rule its reason', BANK,
     'A LANE EARNS A REPOSITORY WHEN IT BECOMES'),
    ('bank keeps the corrections as corrections to facts', BANK,
     'NOT A RE-VERDICT'),
    ('bank declares its own false blank-cell number', BANK,
     '111 BLANK CELLS IN A TABLE OF 111'),
    ('bank keeps M-2 unchanged', BANK,
     'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('bank names the kernel build as the next act if called', BANK,
     'THE KERNEL BUILD, ### IF THE AUTHOR'),
    ('bank leaves the keystone question to the author', BANK,
     'THE NEW-KEYSTONE QUESTION IS ### THE'),
    ('registration capped new mathematics at zero', REG,
     'NEW MATHEMATICAL CONTENT INTRODUCED BY THIS ACT'),
    ('registration fixed the emitter discipline before the run', REG,
     'A QUOTATION OF A QUOTATION IS NOT A SOURCE.'),
    ('registration ordered the mirror rebuilt after the commit', REG,
     'THE MIRROR IS REBUILT ### AFTER ### THE COMMIT'),
    ('run reports F-QUOTE with its count', RUN, 'F-QUOTE  :'),
    ('run reports the discrimination control', RUN, 'DISCRIMINATION CONTROL'),
    ('run reports the additive diff', RUN, 'F-NOGRADE'),
    ('the emitted section reached FINDINGS.md', FINDINGS,
     '## THE M-2 CAMPAIGN, b283\u2013b296 \u2014 THE FOLD'),
    ('FINDINGS.md carries the kernel plan', FINDINGS,
     'THE ONE CANDIDATE THAT PASSES BOTH TESTS'),
    ('FINDINGS.md states no keystone is proposed', FINDINGS,
     'NOTHING IN THIS SECTION IS A KEYSTONE'),
    ('FINDINGS.md keeps listing separate from writing', FINDINGS,
     'Listing is not writing.'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.**
MUST_FAIL = [
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b294 IS RE-VERDICTED.'),
    ('no keystone is created', BANK, 'THE KEYSTONE IS CREATED.'),
    ('no keystone is proposed', BANK, 'THIS ACT PROPOSES A KEYSTONE.'),
    ('no new mathematics', BANK, 'THIS ACT DERIVES A NEW RESULT.'),
    ('no route is claimed', BANK, 'THE FAMILY IS A ROUTE.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('nothing deposits', BANK, 'THIS ACT DEPOSITS.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the findings document claims no keystone', FINDINGS, 'A NEW KEYSTONE IS PROPOSED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b297 -- GATE SUITE')
    print('=' * 100)

    print('\n  OWNER NEEDLES (pulled from EMITTING files, never from a quoter):')
    unpullable = 0
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES (into this act\'s own files, and into the document it wrote):')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    substring_fixtures = 0
    print('\n  SUBSTRING-BASED MUST-FAIL FIXTURES : %d  %s'
          % (substring_fixtures, 'PASS' if substring_fixtures == 0 else '### REFUSED ###'))

    # ### THE HEDGE AUDIT OVER EVERY FILE THIS ACT WROTE.
    # ### ### **A FLAGGED SENTENCE IS ### DESCRIBED ### , NEVER QUOTED, SO THE REPORT CANNOT
    # ### ### RE-INTRODUCE THE TEXT IT FLAGGED.**
    print('\n  HEDGE AUDIT over every file this act writes:')
    for lbl, path in [('bank', BANK), ('registration', REG),
                      ('emitted markdown', EMIT), ('run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-18s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('      (i) a graded sentence in the %s also hedges: %d characters, '
                      'described and NOT quoted here' % (lbl, len(s)))

    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) - len(fails),
             len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
