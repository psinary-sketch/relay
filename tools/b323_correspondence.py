# -*- coding: utf-8 -*-
"""b323_correspondence.py -- TWO ROWS: THE FOLD FILED, AND THE DEFECTIVE-BARS TABLE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE SAYS NINE ACTS ARE NOW ONE SECTION, AND THAT READS AS THE ARC CONCLUDED.** ###
###     It is a FILING. ### No grade moved, no act was re-verdicted, and every number in the
###     section was already banked. ### The row must carry that the additivity was MEASURED as a
###     byte prefix and not asserted, and that `F-QUOTE` carries a discrimination arm.
###   ### ### **ROW TWO FILES A TABLE OF THIS RECORD'S OWN SEALED BARS FOUND DEFECTIVE, AND THAT IS
###     ### THE ROW THAT MATTERS.** ### A record whose registrations are only ever reported as
###     having worked is a record that has stopped reading them. ### **AND THE ROW MUST SAY THAT NO
###     ### SEALED FILE WAS EDITED IN ANY OF THE THREE CASES** -- a defect named in a sealed bar is
###     evidence; a sealed bar quietly rewritten is not.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("NINE ACTS FOLDED INTO ONE SECTION, GENERATED RATHER THAN REVIEWED (b323)",

     "NINE ACTS FOLDED INTO ONE SECTION, GENERATED RATHER THAN REVIEWED (b323): b314 through b322 "
     "become `THE ARCHIMEDEAN INSTRUMENT ARC, b314-b322 -- THE FOLD` in `FINDINGS.md`, **+154 "
     "lines, its sixteenth section, 2709 to 2863 lines**. Each entry carries its grade AS ITS OWN "
     "ACT LEFT IT, its own scope sentence, and an obstacle quoted verbatim. **THE WRITE IS PURELY "
     "ADDITIVE AND THAT IS MEASURED, NOT PROMISED**: the pre-append working file is a TRUE BYTE "
     "PREFIX of the result, and so is the blob at `HEAD` on normalised bytes -- both, because "
     "b309's trap is that `core.autocrlf` makes the two differ on a clean tree. `F-QUOTE` passes "
     "at **18 of 18** and `F-COUNT` at **9 results, 9 obstacles, the arc exactly**.",

     "**NO TERMINAL, AND NO NEW MATHEMATICS.** Every number in the section was already banked by "
     "the act that owns it. **THE GATE IS A GENERATOR AND NOT A REVIEWER**: a quotation that fails "
     "`F-QUOTE` never reaches `FINDINGS.md` at all, because **A CHECK THAT RUNS AFTER THE WRITING "
     "CAN ONLY REPORT A PARAPHRASE; ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.** And it "
     "carries its DISCRIMINATION arm: an ALTERED quotation fed to the same matcher comes back "
     "UNFINDABLE, because a matcher that never misses is not matching. **THE JUDGEMENT THE "
     "MECHANISM DOES NOT MAKE IS DECLARED AS THIS SEAT'S**: `F-QUOTE` checks that a sentence is IN "
     "its originating file and cannot check that it is that act's OWN VOICE rather than material "
     "the act was itself quoting.",

     "**THREE DEFECTS IN THIS ACT'S OWN GENERATOR ARE DECLARED, NONE OF THEM IN THE FILED "
     "SECTION.** The first version had no idempotence guard and **RAN TWICE AND FILED THE ARC "
     "TWICE**, undone by `git checkout` before any commit -- and the closing rule is what makes "
     "that a defect rather than a habit, since the whole suite is re-run after the push and a "
     "generator that can run once cannot satisfy it. The second: the tool printed *THE TWO DIFFER "
     "BY +0 BYTES* in a line reporting no difference, **A PROSE-VS-VALUE DEFECT OF EXACTLY THE "
     "SPECIES b320 FILED AGAINST b319's BANK**, this time in this act's own tool. The third: the "
     "runner's log list was local to `main` while `__main__` wrote it, so its own run file was "
     "EMPTY after two runs. All three fixed, all three declared.",

     "**A FOLD IS A FILING AND NOT A CONCLUSION.** **SCOPE: nine acts at their own grades, "
     "rearranged and not added to.** **NO GRADE MOVES. NO ACT IS RE-VERDICTED. NO NEW "
     "MATHEMATICS.** The arc's one statement is filed with its scope printed beside it: no theorem "
     "is proved by any act in it, the window decides nothing, and the SIZE of no margin on the "
     "domain axis is certified anywhere in the arc. `W-ORD-ARCH-MEMBERSHIP`, `W-ORD-PHI-MU-L2` and "
     "`W-ORD-WINDOW-CLASS` all stay OPEN. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly where the deposit left it. "
     "NOTHING DEPOSITS.",

     "current"),

    ("SEALED BARS FOUND DEFECTIVE, FILED AS THEIR OWN TABLE FOR THE FIRST TIME (b323)",

     "SEALED BARS FOUND DEFECTIVE, FILED AS THEIR OWN TABLE FOR THE FIRST TIME (b323): the fold "
     "carries a table this record has never filed before. **THREE TIMES IN NINE ACTS A BAR WAS "
     "SEALED BEFORE ANY VALUE AND THE BAR ITSELF TURNED OUT WRONG** -- b319's `(B3)` reach bar, "
     "which required the rank constant on BOTH axes when the domain axis cannot deliver it; "
     "b322's `(B2)`, whose two labels do not partition the possibilities; and b322's `(B5)`, whose "
     "branches are not mutually exclusive and fired twice at once. **IN NO CASE WAS THE SEALED "
     "FILE EDITED.** And the thing worth more than the table: in all three the defect was found "
     "**by running the sealed bar and reading what came back**, not by revising it.",

     "**NO TERMINAL. A DEFECT NAMED IN A SEALED BAR IS EVIDENCE; A SEALED BAR QUIETLY REWRITTEN IS "
     "NOT.** b319 reported an EMPTY reach under a bar it had already shown unsatisfiable and left "
     "the fix as a PROPOSAL for the next act. b322 reported the verdict its own broken rule "
     "computed and then **TOOK THE WEAKER OF THE TWO BRANCHES THAT RULE LICENSED**, on the ground "
     "that between two branches a defective rule licenses equally an act may not help itself to "
     "the stronger one. **A RECORD WHOSE REGISTRATIONS ARE ONLY EVER REPORTED AS HAVING WORKED IS "
     "A RECORD THAT HAS STOPPED READING THEM**, which is why the table exists.",

     "**THE LORE IS CONSOLIDATED WITH ITS INCIDENTS AND SPLIT BY WHAT ENFORCES IT**: nine rules "
     "MECHANIZED -- a gate, a fixture or a tool fires whether or not a seat remembers -- and five "
     "JUDGEMENT, which fire only if a seat applies them. **THE SUITE IS INVENTORIED AT TEN "
     "PIECES**, each with what it catches and the incident that put it there, and the archimedean "
     "instrument's three certifications are tabled with their cells and margins: Theorem 1 at 27 "
     "of 27 frames, Theorem 4.7 as an EQUALITY with its residual ladder, the explicit formula at "
     "all thirteen cells. **ITS LIMITS ARE STATED AS MEASUREMENTS**: the domain axis's rate on "
     "both ladders, and a resolving power priced twice, both prices beyond what it reaches.",

     "**A TABLE OF ONE'S OWN DEFECTS IS NOT A RESULT EITHER.** **SCOPE: this row files what three "
     "acts already declared; it discovers nothing.** The desk carries fourteen items with their "
     "states, including that **the artifact-count counter's repair or retirement is the AUTHOR'S** "
     "after three consecutive false positives on statements of measured fact, that **the keystone "
     "re-read is named as next**, and that **the reconciliation wave is the AUTHOR'S** -- the "
     "arc's results are of the kind a wave would carry and naming that is not starting one. The "
     "seam's debt item 1 is restated and STILL UNPAID. The patent lane is carried on the patent "
     "seat's report, UNCONFIRMED on this seat's record. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. "
     "NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands "
     "exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b323 -- THE FOLD.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    r1, r2 = ROWS[0], ROWS[1]
    # ### **THE TWO GUARDS THAT MATTER FOR THESE TWO ROWS**, and they are guards against the two
    # ### readings the rows most invite: that a class test everything passes says something, and
    # ### that a control which HOLDS is a result about the object.
    g1 = ('PURELY ADDITIVE' in r1[1]
          and 'NO GRADE MOVES' in r1[4]
          and 'DISCRIMINATION' in r1[2])
    g2 = ('SEALED BARS FOUND DEFECTIVE' in r2[1]
          and 'IN NO CASE WAS THE SEALED FILE EDITED' in r2[1]
          and 'A SEALED BAR QUIETLY REWRITTEN IS' in r2[2]
          and 'NOTHING DEPOSITS' in r2[4])
    print('  row 1 carries the additivity, the discrimination arm and no-grade-moved : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 files the defective-bars table and that no seal was edited : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
