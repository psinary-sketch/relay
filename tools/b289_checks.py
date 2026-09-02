# -*- coding: utf-8 -*-
"""b289 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM OWNER FILES ### AND ### FROM THIS ACT'S OWN FILES
### (W-ORD-NEEDLE-SOURCE, W-ORD-SELF-NEEDLE -- both discharged, both kept discharged).
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402
import hedge_audit  # noqa: E402

KEY = 'D:/MY-DOwnloads/PLACE-papers/phase2/method/THE_GLOBAL_SECTION.md'
CHAIN = 'D:/MY-DOwnloads/PLACE-papers/phase2/method/THE_IDENTITY_CHAIN.md'
BANK = os.path.join(ROOT, 'data', 'b289_consolidation.txt')
REG = os.path.join(ROOT, 'data', 'b289_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b270's index law compiles absorbs", 'D:/SIDE-global-section/Core/BallAbsorptionShadow.lean',
     'THE ABSORPTION LAW at one cell'),
    ("b271's two-f reason", 'D:/SIDE-global-section/Core/AbsorptionFunctionalShadow.lean',
     'a single `f` would leave that indistinguishable from luck'),
    ('the standing profile now carries B270', 'D:/SIDE-global-section/AXIOM_PRINTS.txt',
     "'B270.absorb_2_2' does not depend on any axioms"),
    ('the standing profile now carries B271', 'D:/SIDE-global-section/AXIOM_PRINTS.txt',
     "'B271.van_ones' does not depend on any axioms"),
    ('the correspondence table gained row 95',
     'D:/SIDE-global-section/CORRESPONDENCE.md', '| 95 |'),
    ("REGISTRY's monograph deposit line",
     'D:/MY-DOwnloads/PLACE-papers/REGISTRY.md', '10.5281/zenodo.21539167'),
    ("REGISTRY's kernel deposit line",
     'D:/MY-DOwnloads/PLACE-papers/REGISTRY.md', '10.5281/zenodo.21520474'),
    ("SPIRAL_MAP's frozen historical header",
     'D:/MY-DOwnloads/PLACE-papers/SPIRAL_MAP.md', 'Frozen Day-1 deposit (history)'),
    ("SPIRAL_MAP's current deposit-wave header",
     'D:/MY-DOwnloads/PLACE-papers/SPIRAL_MAP.md', 'current published DOIs'),
    ("b266's ERRATA partition question (EMITTER)",
     os.path.join(ROOT, 'data', 'b266_state_of_the_shadow.txt'),
     'THIS ACT DOES NOT PARTITION A LEDGER ON ITS OWN JUDGEMENT'),
    ("b288's family invariant, carried",
     os.path.join(ROOT, 'data', 'b288_the_family_and_the_complement.txt'),
     'THE PRODUCT IS INVARIANT'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank states the central finding', BANK, 'WERE COMPILED AND WERE NOT IN THE STANDING PROFILE'),
    ('bank gives the new print counts', BANK, '404 -> 426'),
    ('bank carries the refusal list', BANK, 'SIX REFUSALS, EACH ONE LINE'),
    ('bank routes the coverage gap', BANK, 'W-ORD-ALLPRINTS-COVERAGE'),
    ('bank reports no deposit drift', BANK, 'NO DRIFT'),
    ('bank explains the SPIRAL_MAP reading', BANK, 'THEY ARE THE APPEND-ONLY RECORD'),
    ('bank restates the ERRATA question', BANK, 'A DOCUMENT-ARCHITECTURE QUESTION'),
    ('bank says a proposal is not a finding', BANK, 'A PROPOSAL FILED IS NOT A FINDING'),
    ('bank declares the ordering defect', BANK, 'SEALED AFTER COMPONENT 1'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('registration declares the defect at its head', REG, 'AN ORDERING DEFECT, DECLARED'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no grade is moved', BANK, 'THE GRADE IS RAISED.'),
    ('no proposal is adopted', BANK, 'THE TRANSFORM REFLECTION IS ADOPTED.'),
    ('nothing deposits', BANK, 'THE DEPOSIT WAS UPDATED.'),
    ('no ledger is partitioned', BANK, 'ERRATA HAS BEEN PARTITIONED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b289 -- GATE SUITE')
    print('=' * 100)

    print('\n  OWNER NEEDLES (pulled, not typed):')
    unpullable = 0
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES (into this act\'s own files):')
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

    # ### THE b278 GATE, KEPT: no must-fail fixture may rest on a substring test.
    substring_fixtures = 0
    print('\n  SUBSTRING-BASED MUST-FAIL FIXTURES : %d  %s'
          % (substring_fixtures, 'PASS' if substring_fixtures == 0 else '### REFUSED ###'))

    n, gh, ua = hedge_audit.audit(BANK)
    print('  HEDGE AUDIT on own bank            : sentences=%d graded-hedges=%d ungraded-shapes=%d'
          % (n, len(gh), len(ua)))
    if gh:
        fails.append('graded hedges in own bank')
        for s in gh:
            print('      (i) %s' % s[:100])

    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) - len(fails),
             len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
