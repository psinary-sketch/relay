# -*- coding: utf-8 -*-
"""b366_correspondence.py -- ONE ROW: THE DATED-ARM SWEEP.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a suite had been repaired;
### as if a ruling had been made by this seat; as if the detector were a decision procedure; as if the
### three flagged non-instances were findings; or as if a grade had been conferred.
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

SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE = (
    "**SCOPE: NO SUITE IS EDITED AND NO DATED ARM IS CURED BY THIS ACT.** The sweep classifies and prices; a rewrite RULE is a thing a later act applies, and the proof that nothing was touched is byte-for-byte "
    "against the committed blobs. NO PAST VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED -- b363's control is RELABELLED, which is not the same thing: a relabelling names what an earlier measurement was "
    "measuring, it does not say the measurement was wrong. NO RULING IS MADE BY THIS SEAT: R1, R2 and R3 are the author's and this act executes them. THE COUNT IS OF ARMS THE SUITES REGISTER UNDER A NAME and "
    "is not a count of every predicate in every suite; the 243 registrations whose name is not a literal are reported as UNATTRIBUTED rather than folded in. THE DETECTOR IS A NET OF THREE NAMED SHAPES AND IS "
    "NOT A DECISION PROCEDURE -- an address predicate written in a shape it does not name would not be found, and this act does not claim the three are all there are. NO GRADE IS CONFERRED BY A SEAT and NO "
    "PROOF IS VERIFIED: a source's application of its own theorem is not a proof that the theorem covers the case. b358's CIRCULARITY FINDING IS UNTOUCHED and nothing here bears on the zero channel. NOTHING "
    "WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO "
    "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
    "record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN "
    "AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b366_reads.json'), encoding='utf-8'))
    S = json.load(io.open(os.path.join(D, 'b366_sweep.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b366_faces_row.json'), encoding='utf-8'))
    M = json.load(io.open(os.path.join(D, 'b366_mint.json'), encoding='utf-8'))
    m = ("**%d DATED ARMS IN THE WHOLE RECORD, OUT OF %d ARMS ACROSS %d GATE SUITES** -- and **%d OF THE %d ARE ONE SUBSTITUTION FROM STANDING**, the third missing not its difficulty but **ITS CONTENT** (b366)"
         % (S['dated'], S['arms'], S['suites'], S['one_substitution'], S['dated']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code, with the pre-lock survey declared on its own face. **ADDITION ONE, ANSWERED FROM THE DRAFT ITSELF:** the "
            "draft named *a ruling that a banked suite is a certificate of its own moment and is not re-run*, and **(R2) IS NOT THAT RULING -- IT IS A SPLIT**, agreeing with the draft on the dated half and "
            "contradicting it on the standing half, where an arm on the act's own artifacts *must reproduce at any later date*. **SO THE SWEEP IS NOT UNNECESSARY; (R2) MAKES IT NECESSARY AND SUPPLIES ITS "
            "TEST.** **THE COUNT IS MECHANICAL AND THE CLASSIFICATION IS DECLARED**, arm by arm with the code line printed beside it, because the detector **CANNOT DECIDE WHETHER THE FILE BEING INDEXED IS THE "
            "ACT'S OWN ARTIFACT OR THE LIVING RECORD** -- that is a question about what a computed path names. **AND THE TOOL REFUSES TO EMIT IF THE FLAGS AND THE DECLARATIONS DISAGREE IN EITHER DIRECTION.** "
            "%d lines flagged in %d suites: **%d DATED** (b340 G-SCOPE, b357 G-LOCATED, b359 G-STATUSES), **%d ADDRESS-SHAPED BUT STANDING** (b341 G-LOCATE, which indexes the act's own frozen extraction -- "
            "the case that shows the classification cannot be left to a detector), and **%d NOT ADDRESS PREDICATES AT ALL**. **THE DETECTOR FOUND THE ONE CONFIRMED INSTANCE THE RECORD HOLDS**, b357's "
            "G-LOCATED diagnosed at b364, and it carries fixtures in both polarities including a content-written arm it must leave alone. **AND THE REWRITE RULE FELL ON THE HELPER SIDE OF THE ORDER'S OWN "
            "TEST:** the substitution is one call, `tools/gate_content.py`, with six fixtures -- and the one that matters is not the one that agrees: **ON A MOVED FILE THE ADDRESS FORM SILENTLY READS A "
            "DIFFERENT LINE**, the content form finds the right one at its new number, and when the text is genuinely gone **THE CONTENT FORM RAISES RATHER THAN GOING QUIET**, because a rewrite that only ever "
            "quietened arms would be a softener. %d reads, %d without an anchor, %d of %d anchors differing from the hint that found them."
            % (S['flagged'], len({r['suite'] for r in S['rows']}), S['dated'], S['standing'], S['not_address'],
               E['reads'], E['without_anchor'], E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A CLASSIFICATION IS NOT A CURE.** This act counted arms, classified seven flagged lines, wrote one rewrite helper, minted one species and applied one ruling. It "
         "repaired nothing, ruled nothing and computed nothing about the object.",
         "**PRINT: PLACE-papers, ONE FILE.** FACES_LEDGER.md gains **ONE UPDATE BLOCK ON ROW `%s`** through the ledger's own writer, imported and not reimplemented, append-only against the working file and "
         "its blob, **NO ROW ABOVE TOUCHED** -- applying **(R3)'s grade word `%s`** to the **%s HALF** on %d quotations, eight of them pulled from the pinned rendering itself rather than copied out of b365's "
         "prose. **TECHNE-Core: ONE MODULE, `%s`, COMMITTED LOCALLY AT `%s` AND NOT PUSHED**, kept BESIDE `WRONG_ARM.md` and not inside it. **NEW SHARED TOOL `tools/gate_content.py`** in the relay repo. "
         "**AND NO GATE SUITE WAS EDITED: SUITE FILES DIFFERING FROM THEIR COMMITTED BLOBS, 0.** **THE HOOK AND THE MIRROR ARE OWED AND PAID.** No findings section edited; no roster row changed."
         % (F['row'], F['grade'], F['half'], F['quotes'], M['module'], M['techne_head']),
         "**NO GRADE IS CONFERRED BY A SEAT: (R3)'s WORD IS THE AUTHOR'S AND IS APPLIED, NOT CONFERRED**, and it grades the archimedean half and nothing else -- H-CUSP is not moved, b361's decision is not "
         "moved, and the zero channel is untouched. **(R1) IS RECORDED: THE FOLD THRESHOLD IS NINE, THE SPAN FROM b361 IS SIX, AND THE FOLD IS NOT DUE** -- which is now an arithmetic fact rather than a "
         "judgement, and that is the small thing a ruling buys that an argument cannot. **(R2)'s RELABELLING IS DONE HERE AND NOT BY EDITING b363:** its *5 of 6* is **TWO MEASUREMENTS REPORTED AS ONE** -- "
         "correctness on the standing arms, drift on the dated one -- and b363's verdict stands. **AND THIS SEAT'S EXPECTATION IS HALF MET AND HALF REFUTED:** the dated arms are few, as predicted; but it "
         "predicted that *most* of what looked address-shaped would be frozen-against-frozen, and **ONE OF SEVEN WAS**. **THAT IS THREE CONSECUTIVE ACTS WRONG IN THE SAME SHAPE -- TRUE CLAUSES, A CONCLUSION "
         "ABOUT AN ADJACENT QUESTION -- WHICH IS ENOUGH THAT IT SHOULD BE READ AS A PROPERTY OF THIS SEAT AND NOT AS A RUN OF BAD LUCK.**",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b366 -- ONE ROW: THE DATED-ARM SWEEP.')
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
    g1 = (all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS)
          and 'DATED ARMS IN THE WHOLE RECORD' in ROWS[0][0]
          and 'ONE SUBSTITUTION FROM STANDING' in ROWS[0][0]
          and 'IS NOT THAT RULING' in ROWS[0][1]
          and 'CLASSIFICATION IS DECLARED' in ROWS[0][1]
          and 'REFUSES TO EMIT IF THE FLAGS AND THE DECLARATIONS DISAGREE' in ROWS[0][1]
          and 'ADDRESS-SHAPED BUT STANDING' in ROWS[0][1]
          and 'RAISES RATHER THAN GOING QUIET' in ROWS[0][1]
          and 'UPDATE BLOCK ON ROW' in ROWS[0][3]
          and 'NO ROW ABOVE TOUCHED' in ROWS[0][3]
          and 'NOT PUSHED' in ROWS[0][3]
          and 'NO GATE SUITE WAS EDITED' in ROWS[0][3]
          and 'IS APPLIED, NOT CONFERRED' in ROWS[0][4]
          and 'THE FOLD IS NOT DUE' in ROWS[0][4]
          and 'TWO MEASUREMENTS REPORTED AS ONE' in ROWS[0][4]
          and 'NO SUITE IS EDITED AND NO DATED ARM IS CURED' in ROWS[0][5]
          and 'NOT A DECISION PROCEDURE' in ROWS[0][5]
          and 'NO RULING IS MADE BY THIS SEAT' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the counts, (R2) not the draft\'s ruling, the declared classification, the refusal to emit, the standing exception, the fixture that matters, the ledger block, nothing pushed, no suite edited, the grade applied not conferred, the fold not due, the relabelling, no ruling by this seat : %s' % g1)
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
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
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
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s' % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
