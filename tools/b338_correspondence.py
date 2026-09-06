# -*- coding: utf-8 -*-
"""b338_correspondence.py -- TWO ROWS: THE FOLD b331-b334, A FILING; THE ARC AS ONE STATEMENT, A SUMMARY AND NOT A VERDICT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The section's numbers are read
### from the generator's rows record, never typed. ### **THE HAZARD:** a row that reads as if the fold were a verdict.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE_TAIL = ("**SCOPE: A FOLD -- A SUMMARY OF FOUR ACTS AT THEIR OWN GRADES, PURELY ADDITIVE, NO GRADE MOVED.** The wave's candidate list "
              "restated as the desk's first item is typed, not ranked, and the wave is the author's; the housekeeping's state beside it is b337's "
              "as b337 stated it. Nothing about the quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS "
              "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent "
              "seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. NOTHING DEPOSITS.")


def rows():
    r = json.load(io.open(os.path.join(D, 'b338_fold_rows.json'), encoding='utf-8'))
    m1 = "THE FOLD, b331 THROUGH b334, FOUR ACTS, UNDER THE FOLD'S OWN RULES -- ONE SECTION APPENDED TO FINDINGS.md, PURELY ADDITIVE, THE WAVE'S CANDIDATE LIST RESTATED AS THE DESK'S FIRST ITEM WITH THE HOUSEKEEPING'S STATE BESIDE IT (b338, leg 3 of the sortie)"
    m2 = "THE STATED-CLAUSE ARC AS ONE STATEMENT, AT THE GRADE FOUR ACTS SUPPORT AND NO HIGHER: THE CLAUSE STATED WHOLE AND NOT DISCHARGED; ITS SOFTEST CONSTITUENT DERIVED UNDER THE IMPORT BAR; THE ROOM CHARTED OVER AIMS; THE CLAUSE NOT MOVED (b338)"
    return [
        (m1,
         m1 + ": the section `%s` (+%d lines, %d -> %d) emitted by a committed generator from a result table that is the single "
         "source of truth: F-QUOTE %s at every quotation against the act that originated it with the discrimination arm firing; F-COUNT %s, the "
         "arc exactly; F-MODULES %s, every rule by module on disk under modules/2026-09 and every rule by tool a committed tool; the pre-append "
         "working file and the blob at HEAD true prefixes of the result (%s / %s). Four results at their own grades (FILED; STATED; DERIVES-ON-IMPORTS "
         "for K5 with MEASURED-ON-FAMILIES not conferred; MEASURED on a grid at this reach), four obstacles quoted, four corrections, three sealed "
         "bars found defective and tabled, the seats' defects declared, the lore typed by what enforces it, the suite this arc added, and the desk "
         "-- its first item b324's candidate list restated with b331's addition and this arc's typed candidates, the wave the author's, and the "
         "housekeeping's state as b337 stated it beside it. **A FILING, NOT A RESULT.**"
         % (r['section'], r['lines_added'], r['lines_before'], r['lines_after'], r['fquote'], r['fcount'], r['fmodules'], r['prefix_working'], r['prefix_blob']),
         "**NO TERMINAL, AND THE REASON: A FILING ACT** -- nothing here is a statement about the mathematics beyond what the four acts already carry at their own grades.",
         "**NO PRINT.** One section appended to FINDINGS.md; nothing edited; TECHNE not touched.",
         "**NO GRADE MOVED.** Every grade word in the section is its owning act's; the no-grade-moved check is the prefix test, mechanical.",
         SCOPE_TAIL, "current"),
        (m2,
         m2 + ": the open clause is stated, whole, in the arc's vocabulary, and it is not discharged (b332) -- every constituent unfolded to its "
         "owner, the quantifiers unowned and the clause itself; its softest constituent, the archimedean distribution, is derived from the "
         "classical term under the import bar (b333) -- the corpus's channel is the source's W_inf = -W_R in the orientation the calibration fixed, "
         "four routes agreeing on the bump, the act's own sealed bar found to pair the bump with another function's table and left unmet; the room "
         "the arithmetic leaves is charted over aims (b334) -- for zeta a passed test over a grid at this reach and nothing more, for the Epstein "
         "function the negative control charted at three aims at off-line zeros' heights, the softest pair softening apart; and the clause has not "
         "moved. **A SUMMARY AND NOT A VERDICT.**",
         "**NO TERMINAL, AND THE REASON: A SUMMARY OF FOUR ACTS AT THEIR OWN GRADES**; nothing here is decided that the acts did not decide.",
         "**NO PRINT.** The paragraph in the section, with its scope printed beside it.",
         "**NO GRADE MOVED.** A statement, a derivation and a chart are a statement, a derivation and a chart; a chart is not a proof.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b338 -- THE FOLD, b331-b334. ### THE ROWS.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'A FILING, NOT A RESULT' in ROWS[0][1] and 'A SUMMARY AND NOT A VERDICT' in ROWS[1][1] and all('NO GRADE MOVED' in r[4] for r in ROWS)
    print('  both rows say NO TERMINAL with the reason, a filing and a summary, no grade moved : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; rows to append : %d and %d' % (max(nums), start, start + 1))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tails = back.rstrip(chr(10)).split(chr(10))[-2:]
    cells = [G.split_cells(t) for t in tails]
    ok = (got[-1] == start + 1 and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
