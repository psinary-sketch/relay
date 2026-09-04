# -*- coding: utf-8 -*-
"""b314_correspondence.py -- TWO ROWS: THE ARC FOLDED, AND THE KERNEL FROM A COLD CLONE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE IS A FILING, AND A FILING ROW IN A TABLE OF RESULTS READS AS A RESULT.** ### It
###     is not one: every entry carries the grade ITS OWN ACT left it, and the additivity is
###     MEASURED rather than asserted.
###   ### **ROW TWO REPORTS NINETY-ONE UNCERTIFIED TERMINALS, AND A NUMBER LIKE THAT READS AS AN
###     ### ACCUSATION AGAINST THE KERNEL.** ### It is not: the certified profile reproduced
###     BYTE-FOR-BYTE from a clone that inherited nothing, and the uncertified terminals are a
###     COVERAGE fact about a hand-maintained import list.
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
    ("THE INSTRUMENT ARC FOLDED (b314)",

     "THE INSTRUMENT ARC FOLDED (b314): seven acts \u2014 b307 through b313 \u2014 filed into "
     "`PLACE-papers/FINDINGS.md` as **THE INSTRUMENT ARC, b307\u2013b313 \u2014 THE FOLD**, "
     "emitted by `tools/b314_fold.py`. **14 QUOTATIONS, 0 UNFINDABLE, EVERY ONE CHECKED AGAINST "
     "THE ACT THAT ORIGINATED IT BEFORE EMISSION**, with a discrimination arm that feeds an "
     "ALTERED quotation to the same matcher and requires it back unfindable. Each entry carries "
     "its grade **as its own act left it**, its own scope sentence, and its obstacle quoted. "
     "**`FINDINGS.md` +100 / \u22120.** Also folded: the arc's four corrections to its own "
     "readings, and \u2014 as ONE row, because the shape repeats \u2014 **three sealed "
     "predictions that each got the count or the object right and the normalizing factor wrong** "
     "(b309's operator, b310's factor, b312's registered expectation). The author's CONVENTION "
     "ERRATUM ruling was executed: **`ERRATA.md` entry `E-2026-09-03-1`**, internal record, "
     "+28 / \u22120.",

     "**NO TERMINAL. A FILING IS NOT A COMPILE.** The five falsifiers all DID NOT FIRE: `F-QUOTE` "
     "(every quotation verbatim in its originating act, with its discrimination arm), `F-COUNT` "
     "(results and obstacles each cover all seven acts exactly), `F-NOGRADE` (**measured by "
     "`git diff --numstat`** \u2014 a fold that deletes a line is a fold that moved a grade), "
     "`F-NOKEYSTONE`, and `F-NOSHADOW` (`.lean` files touched in either tracked repository: "
     "**zero**). **THE GENERATOR IS THE DOCUMENT'S AUTHOR, NOT ITS REVIEWER** \u2014 a quotation "
     "failing `F-QUOTE` never reaches `FINDINGS.md` at all.",

     "**NO PRINT. NOTHING COMPILED BY THE FILING** \u2014 the profile stands at 475. **THE OWNER "
     "INSTRUMENT FILES STAY BYTE-IDENTICAL**, checked before the errata entry was written and "
     "again after: the entry's central claim is that they are untouched, and a tool that wrote "
     "that claim while they were modified would be writing a falsehood. The entry follows the "
     "**`E1` precedent** (`E-2026-08-31-1`), where the sites carrying a superseded clause were "
     "left byte-identical and not rewritten, because **the record does not silently overwrite "
     "itself**; and it carries a standing clause \u2014 **a banked remainder value is quotable "
     "only with its convention named** \u2014 written into the entry so that it travels with the "
     "record rather than with any act's memory.",

     "**A FILINGS ACT.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: NO GRADE MOVES HERE, "
     "NO ACT IS RE-VERDICTED, AND NOTHING IN THE SECTION IS NEW MATHEMATICS.** The arc's one "
     "statement is a summary of seven acts at their own grades: at a finite place the source's "
     "construction returns the test function at one point times a dimension and carries no "
     "arithmetic; the mechanism producing that silence **does not type** at the archimedean "
     "place; and the corpus's remainder is **not** the source's function, differing by a factor "
     "of `\u03c1` whose correction accounts for 8% to 19% of the residue **and no more**. "
     "**NOTHING ABOUT THE IDENTITY, `h2`, OR THE COMPLETE ROSTER FOLLOWS FROM IT.** The "
     "vectors-outside-the-object hypothesis is **named as a hypothesis** and is tested by no act "
     "in the arc. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED under "
     "b310's cap. h2 stands exactly where the deposit left it.",

     "current"),

    ("THE KERNEL FROM A COLD CLONE, AND THE COVERAGE ANSWER (b314)",

     "THE KERNEL FROM A COLD CLONE, AND THE COVERAGE ANSWER (b314): the kernel repository was "
     "cloned FRESH from origin at its current pin onto a path outside the corpus, by the tool "
     "itself, and rebuilt from source. **`build/` IS `.gitignore`d, SO THE CLONE ARRIVED WITH "
     "ZERO COMPILED ARTEFACTS \u2014 THERE WAS NO CACHE TO BE STALE.** `elan` resolved "
     "**v4.29.1 INSIDE the clone against v4.33.1 OUTSIDE it**, which is what makes the pin "
     "observable at all. **84 MODULES ELABORATED FROM SOURCE IN DEPENDENCY ORDER, 0 FAILURES**, "
     "`AllPrints.lean` re-run, and the regenerated profile compared against the banked blob at "
     "`HEAD`: **RAW BYTE EQUALITY \u2014 33195 bytes each, 475 prints, 475 zero-axiom, 0 "
     "differing lines, no byte-order mark and no CRLF on either side.**",

     "**NO NEW TERMINAL. THE KERNEL IS EXERCISED AT ITS FULL EXTENT AND NOT EXTENDED BY ONE "
     "LINE**, and the profile it produced was REQUIRED to be the profile already banked. The "
     "comparison is on **RAW bytes as well as normalised**, both printed \u2014 b298 lost a day "
     "to a byte-order mark that passed two checks which could not see it, and b309 lost one to "
     "`core.autocrlf`. **AND THE COVERAGE QUESTION THE RECORD HAS CARRIED HAS AN ANSWER, AND THE "
     "ANSWER IS *FOUND*: 25 Core modules sit outside `AllPrints.lean`, all 25 elaborate, and 91 "
     "`#print axioms` targets in them are NOT IN THE CERTIFICATION PROFILE AT ALL.** The "
     "`AxiomCheck*` wrappers are redundant \u2014 their targets are certified through the parent "
     "modules \u2014 but eight shadow modules are not, together with `M4EnvelopeShadow` through "
     "its own checker.",

     "**THE PROFILE DOES NOT MOVE AND NO MODULE IS ADDED TO THE CERTIFICATION FILE.** The reason "
     "for the coverage finding is structural, not accidental: **`AllPrints.lean` IS A "
     "HAND-MAINTAINED IMPORT LIST, AND NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF "
     "IT** \u2014 the profile simply does not mention the module, and a profile that does not "
     "mention a module looks exactly like a profile for a corpus that does not have one. **AND "
     "THE FIRST RUN OF THIS SWEEP CARRIED TWO DEFECTS, BOTH THIS ACT'S OWN AND BOTH DECLARED**: "
     "it swept alphabetically, so it reported a module as FAILING when its dependency had simply "
     "not been built yet, and it counted an empty output stream as one emitted line. **A SWEEP "
     "THAT TESTS A MODULE BEFORE ITS DEPENDENCY EXISTS REPORTS A DEFECT IN THE SWEEP AS A DEFECT "
     "IN THE CORPUS**, which is the worst direction for a report to be wrong in. Both repaired; "
     "the run of record is a single fresh-clone run.",

     "**A CERTIFICATION TEST, AND NOTHING IS REPAIRED BY IT.** **SCOPE, AND IT IS THE WHOLE OF "
     "THE ROW'S HONESTY: A COLD CACHE AND A COLD CHECKOUT ARE NOT A COLD MACHINE.** One "
     "repository was rebuilt on one machine, sharing that machine's `elan` toolchain store, "
     "operating system and CPU; **this is not evidence that the corpus reproduces from a clone in "
     "general.** **IT DOES NOT CONCLUDE THAT THE UNCERTIFIED TERMINALS ARE WRONG, OR RIGHT** \u2014 "
     "the sweep elaborates them and reports what they print, and **a terminal that elaborates "
     "with zero axioms is not thereby a terminal worth certifying**; whether they belong in the "
     "profile is a question for the act that would add them, under its own registration. **NO "
     "`.lean` FILE IS CREATED OR EDITED AND NO MODULE IS ADDED TO THE CERTIFICATION FILE**, both "
     "at cap zero. NO GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). "
     "h2 stands exactly where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b314 -- THE FOLD\'S ROW, AND THE COLD CLONE\'S.')
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
    g1 = ('NO GRADE MOVES HERE' in r1[4] and 'NOTHING ABOUT THE IDENTITY' in r1[4]
          and 'named as a hypothesis' in r1[4])
    g2 = ('NOT A COLD MACHINE' in r2[4] and 'NOTHING IS REPAIRED BY IT' in r2[4]
          and 'not thereby a terminal worth certifying' in r2[4])
    print('  row 1 refuses the result reading and bounds the summary : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 bounds the certification and refuses the accusation : %s  %s'
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
