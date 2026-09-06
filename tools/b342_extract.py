# -*- coding: utf-8 -*-
"""b342_extract.py -- THE EXTRACT STEP FOR THE TWO RULES AS MODULES. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The executor's draft as banked (component 1, the two rules and the re-typing);
### the two rules at their emitters -- b333's like-for-like readings and b334's comparator by name, b328's phase condition
### and b334's sign column with b336's addendum; the fold's lore typing them TOOL with their incidents; the TECHNE index's
### shape, its standing conditions and a module's header; the August lore rules the modules extend; the sortie ferry's
### leg-4 sentence. ### b283's law: every quotation located at its emitting file and its line before it is written
### anywhere else.
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

NOTES = os.path.join(D, 'b342_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def m(n):
    return os.path.join(TC, 'modules', n)


DRAFT = d('b342_executor_draft_2026-09-06.txt')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
FERRY = d('b342_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the executor's draft, banked
    ("the draft -- component 1", DRAFT, 'COMPONENT 1 \u2014 THE TWO RULES AS TECHNE MODULES: the like-for-like rule (a'),
    ('### the comparator named', DRAFT, 'comparator is named with the function it was computed for; a bar sealed'),
    ("### the table's function; the sign rule", DRAFT, "against a banked table names the table's function) and the sign rule (a"),
    ('### stated with its sign condition', DRAFT, 'threshold rule is stated with its sign condition), each a claim-shaped'),
    ('### under modules/2026-09, incidents from b333 and b334', DRAFT, 'method module under modules/2026-09 with its incident quoted from b333'),
    ('### committed locally, not pushed; the lore re-typed', DRAFT, "and b334, committed locally, not pushed; the fold's lore re-typed from"),
    ('### by an appended block, nothing edited', DRAFT, 'TOOL to MODULE by an appended block, nothing edited.'),
    ('### the modules bind nothing', DRAFT, 'COMPONENT 3 \u2014 WHAT IT SAYS AND DOES NOT: the modules bind nothing; a'),
    # ### ---- the like-for-like rule at its emitters
    # ### THE TWO ANCHORS ADDED ON THE SECOND RUN, AFTER b342's GATE SUITE FOUND THE MODULES QUOTING SENTENCES THIS
    # ### STEP HAD NOT LOCATED. ### The order violation (a quotation written before it was located) is declared in the
    # ### bank as a defect of this seat; the sentences were at their emitters all along, and are now here with their lines.
    ("b333 -- the tool did what the seal ordered", d('b333_the_archimedean_term_derived.txt'), '### derivation tool did exactly what the seal ordered and printed `MISMATCH`, with the corpus\'s `A` as the'),
    ("b334 -- the quadruple's term, in the bank's words", d('b334_the_aim_map.txt'), "### quadruple's term `4 |G|^2 cos 2 phi` is negative only between `45` and `135` degrees. ### By the sealed"),
    ("b333 -- diagnosed like for like", d('b333_the_archimedean_term_derived.txt'), '### `tools/b333_diagnose.py` (`data/b333_diagnose_run.txt`), like for like:'),
    ("### the record's numbers not touched", d('b333_the_archimedean_term_derived.txt'), "### ### ### **THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED.** ### Diagnosed by a new tool,"),
    ("### the bar not met, the readings readings", d('b333_the_archimedean_term_derived.txt'), '### carried. ### The like-for-like readings live in a new tool and are readings.'),
    ("### the seat read the table's a column as the bump's cells", d('b333_the_archimedean_term_derived.txt'), "### read b320's table's `a` column as the bump's cells without reading b320's tool for the function behind"),
    ("b334 -- what the like-for-like rule is for", d('b334_the_aim_map.txt'), "### seed's is the aimed seed's, which is what the like-for-like rule is for. ### Every sign RESOLVED"),
    ('### the comparator in code, by name', t('b334_aimmap.py'), '### ### **THE LIKE-FOR-LIKE RULE, ENFORCED BY NAME:** every quantity is a `Q(name, value)`; `compare` raises on'),
    ('### the only comparison', t('b334_aimmap.py'), '    """### the only comparison in this file; it raises when the two sides name different functions."""'),
    ('### it raises', t('b334_aimmap.py'), "        raise ValueError('LIKE-FOR-LIKE REFUSED: %r against %r' % (a.name, b.name))"),
    # ### ---- the sign rule at its emitters
    ('b328 -- negative exactly past forty-five', d('b328_the_discriminating_family.txt'), "### for an even seed `4 |G|^2 cos(2 phi)`, ### **NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE**; an"),
    ('### the refinement, 45 to 135', d('b328_the_discriminating_family.txt'), '### ### **`S_4 = 4 |G(c)|^2 cos(2 phi)`, NEGATIVE EXACTLY WHEN `45 deg < |phi| < 135 deg`.** ### The'),
    ('### the odd component below forty-five', d('b328_the_discriminating_family.txt'), "### - G_o^2]`: an even seed needs phase past forty-five; an odd component needs phase BELOW it; both add."),
    ('b334 -- the sealed threshold rule is not the sign condition', d('b334_the_aim_map.txt'), '### ### **(6) THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.** ### The rule'),
    ('### the counts', d('b334_the_aim_map.txt'), '### rule 270 of 392 aims are REACHED; with a negative term 170 (165 on the reaching leg, 5 on the'),
    ("### the sign beside the verdict, in code", t('b334_aimmap.py'), "            # ### the quadruple's sign beside the threshold verdict: past 135 degrees the term is positive again"),
    ('### the chart legend', t('b334_aimmap.py'), "    rec('  (* = the phase exceeds %g deg at that beta: REACHED ; the trailing sign is the quadruple\\'s term S_4 = 4 |G|^2 cos 2 phi, negative only between 45 and 135 degrees)' % THRESHOLD_DEG)"),
    ("b336 -- the addendum to b328's block", LEDGER, "| **b328's update** (the discriminating family), the phase rule | *\"NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE\"*"),
    # ### ---- the fold's lore, typed TOOL
    ('FINDINGS -- mechanized by a tool', FINDINGS, '**Mechanized by a tool** \u2014 a committed tool of this arc enforces the rule; no module carries it yet, and the next extraction\u2019s desk holds it:'),
    ('### the like-for-like rule, typed TOOL', FINDINGS, '- **A comparator is named with the function it was computed for; a bar sealed against a banked table names the table\u2019s function, and a comparison whose two sides name different functions is refused.**'),
    ('### the sign rule, typed TOOL', FINDINGS, '- **A threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.** *Incident:* b328\u2019s rule counted a hundred of b334\u2019s aims whose quadruple term is positive; the chart prints the term\u2019s sign beside every verdict. *Tool:* `tools/b334_aimmap.py`'),
    ('### mechanized by a module', FINDINGS, '**Mechanized by a module** \u2014 a TECHNE module (private, local, not pushed) carries the rule and a gate enforces it:'),
    # ### ---- TECHNE: the index, its conditions, a module's header, the August rules
    ('TECHNE -- the index table head', m('INDEX.md'), '| module | family | what it fixes | cross-reference to August |'),
    ('### the noise-floor row', m('INDEX.md'), '| `2026-09/NOISE_FLOOR_GATE.md` | VACUITY | the drift arm; the magnitude cut as a must-fail fixture | extends `HARNESS_LORE.md` rule 11 |'),
    ('### the standing condition: no grade conferred', m('INDEX.md'), '- ### **No module confers a grade on the results it cites.** Each states the grade its owning act'),
    ('### private, not pushed', m('INDEX.md'), '- ### **TECHNE-Core is PRIVATE and was NOT pushed by the act that wrote these files.** Local-only,'),
    ("### a module's header line", m(os.path.join('2026-09', 'NOISE_FLOOR_GATE.md')), '*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b330) \u00b7 **PRIVATE, TECHNE-Core, local-only**. Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*'),
    ("### a module's sections", m(os.path.join('2026-09', 'NOISE_FLOOR_GATE.md')), '## WHAT IT REFUSES'),
    ('August lore -- rule 11', m(os.path.join('2026-08', 'HARNESS_LORE.md')), "## 11. ### A falsifier's verdict is bounded by its instrument's resolution"),
    ('### rule 19', m(os.path.join('2026-08', 'HARNESS_LORE.md')), '## 19. ### Scope statements travel with results'),
    ('### rule 21', m(os.path.join('2026-08', 'HARNESS_LORE.md')), "## 21. ### A check's scope is stated as precisely as its finding"),
    # ### ---- the sortie ferry, leg 4
    ('the sortie -- leg 4', FERRY, 'LEG 4 (b342) \u2014 THE TWO RULES AS MODULES and the b328 phase-rule'),
    ('### carried into the sign-rule module', FERRY, 'refinement carried into the TECHNE module for the sign rule \u2014'),
    ('### as the draft states them, local, not pushed', FERRY, "as the executor's draft states them, committed locally, not"),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b342_extract.py -- THE TWO RULES AS MODULES. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
