# -*- coding: utf-8 -*-
"""b344_extract.py -- THE EXTRACT STEP FOR THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE.
### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The ferry's two additions and the executor's draft it adopts as written,
### both banked on disk so *as the draft wrote it* is checkable at a line; b339's floor with the three candidate
### origins it named, and its verdict; b343's measurement on the grid axis -- the rank held constant, the residual's
### movement, and the sealed rule that forbade a conclusion -- and b343's room at the wider reaching width, its
### minimum at the sealed interval's edge and the narrowing as measured; b342's declaration that the order arm is a
### defective bar and why; the three candidate axes at their emitters, so the one moved can be chosen against the
### other two by what the record says of each; the seal tool's own block and the function that writes it; the TECHNE
### index's standing conditions and a module's shape; the object b339's floor was measured on and its separation.
### ### b283's law: every quotation located at its emitting file and its line before it is written anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TC = r'D:\MY-DOwnloads\TECHNE-Core'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b344_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b344_ferry_2026-09-06.txt')
DRAFT = d('b344_executor_draft_2026-09-06.txt')
RULING = d('b344_ruling_2026-09-06.txt')
B339, B342, B343 = d('b339_the_exponent_resolved.txt'), d('b342_the_two_rules_as_modules.txt'), d('b343_the_maps_next_reach.txt')
B321 = d('b321_the_window_opened.txt')
MODIDX = os.path.join(TC, 'modules', 'INDEX.md')
NOISE = os.path.join(TC, 'modules', '2026-09', 'NOISE_FLOOR_GATE.md')

WANTED = [
    # ### ---- the order: the ferry's two additions, and the draft it adopts
    ('the ferry -- the draft adopted as written', FERRY, 'THE FLOOR PRICED, THE SEAL\'S OWN CLOCK, AND THE ROOM\'S EDGE'),
    ('### addition one, the axis named before any value', FERRY, 'ADDITION ONE, to Component 1: the axis moved is chosen and'),
    ('### with the reason it was chosen over the other two', FERRY, 'named in the registration BEFORE any value, with the reason it'),
    ('### the other two printed at every rung', FERRY, 'was chosen over the other two stated there; and whichever axis'),
    ("### addition two, the room's edge", FERRY, "ADDITION TWO, a new Component 2b \u2014 THE ROOM'S EDGE: b343's"),
    ('### extend downward at that width only', FERRY, 'Extend'),
    ('### a finer chart and not a trend', FERRY, 'grid is a finer chart and not a trend, and that nothing about'),
    ('### everything else stands as the draft wrote it', FERRY, "Everything else \u2014 Component 1's ladder and gates, Component 2's"),
    ('the draft -- component 1, the floor priced', DRAFT, "COMPONENT 1 \u2014 THE FLOOR PRICED: b339 found the identity residual's limit"),
    ('### the three candidate origins', DRAFT, 'for that floor \u2014 the fixed NY = 512, the cut\'s tau, the taper. b343 moved'),
    ('### move ONE with the others held', DRAFT, 'Move ONE of the three named candidates at a covered cell, with the other'),
    ('### the ladder and what is printed', DRAFT, 'two and the domain held: NY over a sealed ladder at the reference frame,'),
    ('### and whether the movement is of the size the floor requires', DRAFT, 'size b339\'s floor requires \u2014 or that it is not, which is equally a finding.'),
    ("### component 2, the seal's own clock", DRAFT, "COMPONENT 2 \u2014 THE SEAL'S OWN CLOCK: b342's G-ORDER was declared a"),
    ('### repair the instrument, not the past', DRAFT, 'defective bar because a lawful post-seal marking rewrites the registration'),
    ('### record the UTC instant inside the block', DRAFT, 'past: have reg_seal.py record the seal\'s UTC instant inside the seal block'),
    ('### and what it does not recover', DRAFT, "the repair does NOT do: it does not recover b342's lost timestamp."),
    ('### component 3, the scope sentences', DRAFT, 'COMPONENT 3 \u2014 WHAT IT SAYS AND DOES NOT: one axis moved is one axis'),
    ('### the expectations', DRAFT, "DRAFT \u2014 NAVIGATOR EDITS. Expectations, registered here: (G1) the residual"),
    ('### the bank path', DRAFT, 'Bank: data/b344_the_floor_priced.txt. Deviation rule standing.'),
    ("### the EXECUTION block's seal clause", DRAFT, 'runs AND the seal gated on the satisfiability verdict; extract-to-disk for'),
    ("the ruling -- this act's number", RULING, 'OPTION 1. b344 = THE FLOOR PRICED, THE SEAL\'S OWN CLOCK, AND'),
    ('### the earlier sortie slides', RULING, 'that ferry wrote them, their order unchanged and their content'),
    # ### ---- b339's floor and its candidates
    ("b339 -- the floor, and the three candidates named", B339, "### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut's `tau`, the"),
    ('### the verdict unaffordable', B339, '### ### **(1) THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.** ### No'),
    ('### the limit above both candidates', B339, '### `10.9 s` and `11.9 s` at `a = 1.3`, `4.3 s` and `5.3 s` at `1.35`, `1.6 s` and `2.6 s` at `1.41` (the'),
    ("b321 -- the separation at a = 1.41", B321, '    1.41   0.221284108      0.217290580      0.003993528    0.018807781      PASSES'),
    # ### ---- b343: the grid axis moved, and the room's edge
    ('b343 -- the rank held constant on the grid axis', B343, '### ### **THE AXIS THE DRAFT NAMES HOLDS THE RANK FIXED:** the stable-cut rank is `69` at all three'),
    ("### the residual's movement and the sealed rule's refusal", B343, '### SIZE IS REPORTED AND NOTHING IS CONCLUDED**, as the rule directs.'),
    ('### the movement measured', B343, '### the two doublings. ### It changed, by `1.242e-03` relative under the source\'s convention and `1.260e-03`'),
    ("### the room's minimum at the interval's edge", B343, '### **AND ONE OF THE TWO MINIMA SITS AT THE INTERVAL\'S EDGE:** at `a = 40` it is interior (`gamma = 2.0`'),
    ('### the sealed interval does not bracket it', B343, '### lower boundary, so ### **THE SEALED INTERVAL DOES NOT BRACKET THE MINIMUM AT a = 81** and the room may'),
    ('### the narrowing, as measured', B343, '### `+0.000090027`. ### Both are about seven times narrower than b334\'s coarse-grid minimum, which stood at'),
    ('### no crossing, both widths', B343, '### ### **(1) THE FINER GRID, THIRTEEN HEIGHTS AT TWO WIDTHS: NO CROSSING at a = 40 ; NO CROSSING at a = 81.**'),
    # ### ---- b342's defective bar, which component 2 repairs the instrument for
    ('b342 -- the order arm is a defective bar', B342, '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`'),
    ('### the marking rewrites the file and no time is recorded', B342, '### **A LAWFUL POST-SEAL MARKING'),
    ('### the order not gate-established', B342, "### GATE-ESTABLISHED for this act**; it rests on the session's own sequence, which a gate did not check."),
    # ### ---- the three candidate axes at their emitters
    ('the taper -- b316 ALPHA', t('b316_instrument.py'), "ALPHA = 1.0   # ### Definition 4.4's `a`, at the source's own `S(1,1)`"),
    ('### b316 BETA', t('b316_instrument.py'), 'BETA = 1.0    # ### Definition 4.4\'s `b`'),
    ("the cut -- b319's TAU", t('b319_stable.py'), 'TAU = 1e-6'),
    ('### the argument for it, never from a computed spectrum', t('b319_stable.py'), '# ### magnitude above double precision, so it separates the space from the first prolate mode without'),
    ('### 57 times inside the separation', t('b319_stable.py'), '# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of'),
    ("NY -- b317's fixed value, one axis at a time", t('b317_smear.py'), 'NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing'),
    ('### and why NY exists at all', t('b316_instrument.py'), '# ### DERIVED IS NOT IN THE SPACE.** ### `NY` samples `(0, 1]` independently of `X`.'),
    ('### the cut itself', t('b319_stable.py'), 'def both_subspaces(fr, tau=TAU, T=None):'),
    ('### the square', t('b318_square.py'), 'def square_trace(fr, sub, f, block=None):'),
    ('### the object b339 measured the floor on', t('b317_smear.py'), 'def mean_zero_variant(a):'),
    # ### ---- the seal tool, and the TECHNE shape component 2 files into
    ("reg_seal -- the block's marker", t('reg_seal.py'), "MARK = '### THE REGISTRATION SEAL (emitted by tools/reg_seal.py; do not retype).'"),
    ('### the hash line it writes', t('reg_seal.py'), "PREFIX = '### sha256 of every byte ABOVE this block : '"),
    ('### the function that writes the block', t('reg_seal.py'), 'def cmd_seal(path):'),
    ('### and the one that checks it', t('reg_seal.py'), 'def cmd_verify(path):'),
    ('TECHNE -- no module confers a grade', MODIDX, '- ### **No module confers a grade on the results it cites.** Each states the grade its owning act'),
    ('### private, not pushed', MODIDX, '- ### **TECHNE-Core is PRIVATE and was NOT pushed by the act that wrote these files.** Local-only,'),
    ("### a module's header line", NOISE, '*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b330) \u00b7 **PRIVATE, TECHNE-Core, local-only**. Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*'),
    ("### a module's sections", NOISE, '## WHAT IT REFUSES'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec("b344_extract.py -- THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE.")
    rec('### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
