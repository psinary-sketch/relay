# -*- coding: utf-8 -*-
"""b364_correspondence.py -- ONE ROW: THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a verdict had been
### withdrawn; as if an arm had been repaired; as if `b357`'s finding were in doubt; as if a dated arm were
### the wrong-arm species under another name; or as if this act had audited the other suites.
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
    "**SCOPE: NO VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED.** b357's verdict was true when it was banked; what this act records is that RE-RUNNING that suite today no longer reproduces it, and why. "
    "NO ARM IS REPAIRED AND NO SUITE, BANK, INDEX OR RUN FILE IS EDITED -- the order's own phrase, DIAGNOSE DO NOT REPAIR-TO-PASS, is a bar and not a preference, and every file the diagnosis reads is proved "
    "byte-identical to its committed blob at both ends. b357's FINDING IS UNTOUCHED: which passages say what, and the 5 wider / 6 narrower / 1 silent split, rest on the half of the arm that still holds at "
    "every one of the twelve rows. NO CURE IS PROPOSED: the filing names the author's choices and prefers none. A DATED ARM IS NOT b363's WRONG ARM -- a wrong arm was wrong the day it was written and a dated "
    "arm was right the day it was written, and they need different cures. THE OTHER FIVE SUITES WERE NOT AUDITED FOR ARMS OF THIS SHAPE and are not claimed clean. THE ABSOLUTE-PATH WORK-ORDER IS NOT "
    "RESTATED, because this is not its incident. NOTHING WAS COMPUTED ABOUT THE OBJECT: no frame, no seed, no transform, no quadrature, no fit, no score, no series. Nothing about the quantifier, h2, totality "
    "or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NO AGGREGATION IS "
    "STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b364_reads.json'), encoding='utf-8'))
    J = json.load(io.open(os.path.join(D, 'b364_diagnose.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b364_filing.json'), encoding='utf-8'))
    m = ("THE COPY WAS INNOCENT AND THE BRANCH IS **%s**: the banked suite `tools/b357_checks.py`, run **AT ITS OWN LOCATION, UNEDITED**, reports the same `GATES FAILING : %d %s` the copy reported, so a "
         "banked verdict rests on an arm that no longer holds -- **AND THE ARM IS NOT WRONG, IT IS DATED** (b364)" % (J['branch'], J['home_failing'], J['home_names']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY READ OF THE SUITE AND BEFORE ANY RUN OF IT**, on the audit's own exit code, and **THE THREE BRANCHES WERE FIXED IN GENUINE IGNORANCE OF WHICH WAY "
            "THE DIAGNOSIS WOULD GO** -- what the arm checks, what it found in the copy and what it finds at home were all unread when the branch test was written down. **THE PREDICATE IS QUOTED FROM ITS OWN "
            "SUITE AND NOT PARAPHRASED** (%d predicate lines located by the anchor tool at `tools/b357_checks.py`), because a paraphrased predicate is a seat's reading of an arm and not the arm. **THE ARM "
            "CERTIFIES TWO THINGS AND ONLY ONE HAS FAILED. (a) THAT EVERY ROW b357 CLASSIFIED IS STILL FINDABLE AT ITS OWN LEDGER, NOW** -- located by the row's own TEXT, which is why it is robust: *%s*. "
            "**(b) THAT ANY ROW WHOSE LINE NUMBER HAS MOVED IS DECLARED IN b357's OWN BANK, WITH BOTH NUMBERS** -- and **THIS HALF CANNOT HOLD AND CANNOT BE MADE TO**, because it compares a number computed "
            "NOW against a literal in a bank written ONCE, in an append-only file that may never be edited. %d rows have moved: %s. **b357 DECLARED TWO OF THESE MOVEMENTS ITSELF** -- the ones its own index "
            "append caused, printed under its own straddle declaration -- and could not declare the rest, because the acts that produced those numbers had not yet run. **SO b357 PREDICTED THE SHAPE AND WAS "
            "RIGHT ABOUT IT; IT COULD NOT PREDICT THE ARITHMETIC OF THE FUTURE, AND NOTHING COULD.** **THE SPECIES IS NAMED: A DATED ARM** -- an arm whose pass condition is a literal in a frozen file, "
            "compared against a quantity recomputed at every run, is dated by construction; it does not become wrong, it becomes old, and the moment of its expiry is set by the next act that moves a line. "
            "**AND THE DRIFT REACHES THE PROSE, NOT ONLY THE GATE:** b357's own answer section prints `FACES_LEDGER.md : 140` as text and that row is now at `141`, and no gate arm anywhere protects a number "
            "printed in prose. %d reads, %d without an anchor, %d of %d anchors differing from the hint that found them."
            % (E['predicate_lines'],
               re.search(r'rows re-located at their ledgers : \d+ of \d+ ; unclassified : \d+', J['home_section']).group(0),
               len(F['moved']), '; '.join('%s %d to %d' % (a, b, c) for a, b, c in F['moved']),
               E['reads'], E['without_anchor'], E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A DIAGNOSIS IS NOT A CURE.** This act read a predicate, ran a copy, ran the banked suite where it lives, proved nothing it read was written, and filed one finding. It "
         "repaired nothing and decided nothing that was the author's to decide.",
         "**PRINT: PLACE-papers, ONE FILE.** OPEN_TRAILS.md gains **ONE APPEND-ONLY BLOCK** under its own mark, `%s` -- %d bytes, both quotations built by the anchor tool from `tools/b357_checks.py` itself "
         "with the scaffolding equality checked under the shared normaliser, the working file a true prefix of what it was **AND OF ITS COMMITTED BLOB** (the reading BEFORE THE PUSH, which by b352's "
         "straddling rule is the one that carries). **NO ROW ABOVE TOUCHED.** **IT IS NOT AN ERRATA ENTRY** -- ERRATA is for defects in deposited text, and nothing deposited is wrong here. "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** **NO BANKED SUITE, BANK, INDEX OR RUN FILE WAS EDITED**, proved byte-for-byte against six committed blobs "
         "before and after, with line endings normalised and nothing else (b309's trap). **THE HOOK AND THE MIRROR ARE OWED AND PAID.** Nothing in TECHNE-Core; no findings section edited; no roster row "
         "changed." % (F['entry'], F['grew']),
         "**NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.** **AND BOTH SEATS' EXPECTATIONS ARE REFUTED BY THE SAME RUN.** The navigator's was *(L1) ENVIRONMENTAL*; this seat's, registered before "
         "the run, was ENVIRONMENTAL on the reasoning that b357 had predicted the shape and that an arm reading a moved line is not a broken arm. **EVERY CLAUSE OF THAT REASONING IS TRUE AND THE CONCLUSION "
         "DOES NOT FOLLOW:** ENVIRONMENTAL was not a claim about WHY the arm fails, it was defined by the order as a claim about WHERE it fails, and this seat answered the question it found easier to answer. "
         "**THE LOCKED REGISTRATION SAW IT COMING AND SAID SO BEFORE THE RUN** -- that this seat's expectation was worth less than the navigator's, since this seat wrote b363's report of the incident and was "
         "predicting its own earlier reading. **AND THE CREDIT FOR THE FINDING BELONGS TO THE ORDER'S OWN BRANCH TEST -- RUN IT WHERE IT LIVES -- AND NOT TO THE SEAT THAT RAN IT**, since the cheapest thing "
         "available was to run the copy again, see the same failure, and call it a property of copying.",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b364 -- ONE ROW: THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED.')
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
          and 'THE COPY WAS INNOCENT' in ROWS[0][0]
          and 'IT IS DATED' in ROWS[0][0]
          and 'AT ITS OWN LOCATION, UNEDITED' in ROWS[0][0]
          and 'FIXED IN GENUINE IGNORANCE' in ROWS[0][1]
          and 'NOT PARAPHRASED' in ROWS[0][1]
          and 'ONLY ONE HAS FAILED' in ROWS[0][1]
          and 'CANNOT HOLD AND CANNOT BE MADE TO' in ROWS[0][1]
          and 'THE SPECIES IS NAMED: A DATED ARM' in ROWS[0][1]
          and 'APPEND-ONLY BLOCK' in ROWS[0][3]
          and 'NOT AN ERRATA ENTRY' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NO BANKED SUITE, BANK, INDEX OR RUN FILE WAS EDITED' in ROWS[0][3]
          and 'BOTH SEATS' in ROWS[0][4] and 'REFUTED' in ROWS[0][4]
          and 'NO VERDICT IS WITHDRAWN' in ROWS[0][5]
          and 'NO ARM IS REPAIRED' in ROWS[0][5]
          and 'A DATED ARM IS NOT' in ROWS[0][5]
          and 'WERE NOT AUDITED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the copy innocent, the branch fixed in ignorance, the predicate quoted, one half failed, the species named, the append-only block, not an ERRATA, nothing edited, both expectations refuted, no cure proposed : %s' % g1)
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
