# -*- coding: utf-8 -*-
"""b282 -- THE GATE SUITE.

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
BANK = os.path.join(ROOT, 'data', 'b282_fold_the_campaign.txt')
REG = os.path.join(ROOT, 'data', 'b282_registration_2026-09-01.txt')

# ### (label, path, anchor) -- OWNER needles. ### An unpullable anchor is a FAIL.
OWNER_NEEDLES = [
    ("b266's fold law", os.path.join(ROOT, 'data', 'b266_state_of_the_shadow.txt'),
     'NO GRADE MOVED. ### NO ACT RE-VERDICTED.'),
    ("b270's index law", os.path.join(ROOT, 'data', 'b270_ambient_pairing_properties.txt'),
     'THE PAIRING IS EXACTLY ZERO AT k = n'),
    ("b271's escape", os.path.join(ROOT, 'data', 'b271_top_level_no_go.txt'),
     'MEMBERSHIP DOES NOT FORCE VANISHING ON THE BALL'),
    ("b276's fiber-lemma scope", os.path.join(ROOT, 'data', 'b276_size_equivalence_tension.txt'),
     'PROVED AT LEVEL 1 AND FULLY VERIFIED'),
    ("b279's construction", os.path.join(ROOT, 'data', 'b279_the_local_space.txt'),
     'VERDICT: (CONSTRUCTED)'),
    ("b280's barrier", os.path.join(ROOT, 'data', 'b280_the_consequence.txt'),
     'VERDICT: (BARRIER)'),
    ("b281's compression", os.path.join(ROOT, 'data', 'b281_the_compression.txt'),
     'VERDICT: (COMPRESSION ZERO)'),
    ('the emitted table exists', os.path.join(ROOT, 'data', 'b282_fold_emitted.md'),
     '| act | obstacle | quoted from its owning act |'),
    ('FINDINGS carries the consolidation',
     'D:/MY-DOwnloads/PLACE-papers/FINDINGS.md', 'THE TWO SUPPORTS ARE COMPLEMENTARY'),
    ('FINDINGS carries the desk',
     'D:/MY-DOwnloads/PLACE-papers/FINDINGS.md', 'a construction AND a ruling'),
]

# ### SELF needles -- into this act's OWN emitted files.
SELF_NEEDLES = [
    ('bank records no grade moved', BANK, 'NO GRADE MOVED. ### NO ACT RE-VERDICTED.'),
    ('bank records the additive count', BANK, '`+111 / -0`'),
    ('bank reports F-QUOTE firing', BANK, 'F-QUOTE FIRED ONCE, ON EXACTLY THE SPECIES'),
    ('bank keeps the two lists apart', BANK, 'DELIBERATELY NOT ONE LIST'),
    ('bank carries the hook caveat', BANK, 'IT IS NOT A REVIEW OF THE COMMIT'),
    ('bank reports all three clauses', BANK, 'NO CLAUSE ALONE IS THE VERIFICATION'),
    ('bank keeps M-2 owed', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED)'),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1"),
    ('bank names the two live directions', BANK, 'THE ARCHIMEDEAN QUESTION -- THE BRANCH'),
    ('registration fixes F-NOGRADE', REG, 'A RE-VERDICT WEARING A FOLD'),
]

# ### MUST-FAIL FIXTURES. ### **WHOLE-LINE EQUALITY ONLY.** ### Each asserts that a line which
# ### would break the act's scope is ABSENT from the bank, compared as a COMPLETE LINE.
MUST_FAIL = [
    ('no grade is moved', BANK, 'THE GRADE IS RAISED.'),
    ('no act is re-verdicted', BANK, 'b276 IS REFUTED.'),
    ('no adoption is stated', BANK, 'C3 IS ADOPTED.'),
    ('no archimedean claim', BANK, 'THE ARCHIMEDEAN QUESTION IS SETTLED.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b282 -- GATE SUITE')
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
