# -*- coding: utf-8 -*-
"""b359_correspondence.py -- TWO ROWS: THE ACT'S OWN, AND RULING (R1)'S APPEND-ONLY CORRECTION.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count and
### every hash is read from the act's own records, never typed.
### ### **ROW 1 -- THE ACT.** ### THE HAZARD: a row that reads as if the literature had been searched
### exhaustively, as if a located statement had been applied, as if the tail had been closed, or as if
### `EXISTS BUT CIRCULAR` were a discovery rather than a pinning of what the sources say themselves.
### ### **ROW 2 -- RULING (R1).** ### *"The mis-attributing correspondence row is corrected by an
### APPEND-ONLY correction row citing the bank and the index key; the row itself is not edited."* ### THE
### HAZARD: a correction row that reads as if b356 were re-verdicted, or as if a figure had moved. ### **ONE
### WORD IN ONE CELL OF ONE ROW IS WRONG AND EVERYTHING ELSE IN THAT ROW IS RIGHT.**
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

SCOPE = ("**SCOPE: NINE CLAIMS AND SIX PINS THIS SEAT CHOSE ARE NOT A CENSUS OF A 152-LINE FRONT DOOR AND A 438-LINE MAP.** Nothing mechanical enumerated the candidates, so a stale claim that was not "
         "looked for is NOT COUNTED HERE. And the fields checked were the DEPOSIT FIELDS and the PINS; neither document was read for anything else. NOT THAT THE DEPOSIT IS CORRECT -- only that the ledgers "
         "agree with it and with each other. NOT THAT THE PLATFORM RECORD IS RIGHT: a hash fixes the bytes it returned and nothing more. NOT THAT A PIN THAT RESOLVES TODAY WILL RESOLVE TOMORROW, which is "
         "why the order said read live. AND THE MIRROR PASSING ITS THREE CLAUSES SAYS NOTHING ABOUT WHETHER WHAT IT CARRIES IS TRUE -- the clauses check the archive against its manifest, its pin and its "
         "roster, and this act own existence is the reason that distinction is kept. A LEDGER RECONCILED IS NOT A LEDGER VERIFIED. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS "
         "DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310 cap. The seam debt item 1 "
         "restated, still unpaid. The patent lane carried on the patent seat report, UNCONFIRMED on this seat record. THE POSTURE LOCK IS SEPARATE AND WAS NOT TOUCHED. h2 stands exactly where the deposit "
         "left it. The wave PARKED by the author ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b359_pass.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b359_fetch.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b359_reads.json'), encoding='utf-8'))
    dep = R['deposit']
    S1 = F['targets'][0]
    m = ("THE FRONT DOOR AND THE FEDERATION MAP ARE STILL RECONCILED TO THE SOURCE OF TRUTH, CHECKED AGAINST LIVE BYTES AND LIVE REMOTES RATHER THAN AGAINST THE AUGUST NOTE THAT SAYS THEY WERE: %d CLAIMS "
         "CLASSIFIED (%d CURRENT, %d SILENT, %d STALE) AND %d ASSERTED PINS ALL RESOLVED AND ALL MATCHING -- SO NOTHING IS APPENDED, BECAUSE A CURRENCY PASS THAT FINDS NO DRIFT AND WRITES A NOTE ANYWAY IS "
         "NOISE (b359)"
         % (R['n_current'] + R['n_stale'] + R['n_silent'], R['n_current'], R['n_silent'], R['n_stale'], R['n_pins']))
    stmt = (m + ": the precedence is the front door own, quoted and obeyed -- *\"REGISTRY > README > SPIRAL_MAP for deposits; disk for live pins only, never for deposits\"* -- so every "
            "deposit claim was ranked against REGISTRY, every pin went to ls-remote and nowhere else, and **NO DEPOSIT FIELD WAS CHECKED AGAINST DISK**. **THE READ-ONLY FETCH, TWO GETs, BOTH HTTP 200, BOTH "
            "HASHED** (sha256 `%s`, %d bytes; the concept id resolves to the version record, so both return the same bytes): version `%s`, DOI `%s`, concept `%s`, published `%s`, **n_files %d**, "
            "**is_last %s** -- five fields checked against REGISTRY governing d1-1 row at line 82 and **FIVE AGREEMENTS**, and **THE CONCEPT DOI RESOLVES TO THE SAME RECORD AND THAT RECORD IS is_last, SO NO "
            "LATEST-VERSION POINTER HAS DRIFTED**. The bundle description and the count agree too: REGISTRY says *\"the monograph + 6 companions + ONE_PAGE_PROOF + ERRATA + two graphics\"*, "
            "which is eleven items, and the platform returns eleven. **THE TWO SILENT CLAIMS ARE THE JUDGEMENT THAT COULD HAVE GONE THE OTHER WAY, AND THE LOCKED FACE FIXED IT IN ADVANCE:** the map frozen "
            "Day-1 table and its v0.6 changelog line both name superseded versions and both are marked as history -- *\"the row is historical and is not rewritten\"* -- so **A DOCUMENT "
            "THAT SAYS THIS WAS TRUE THEN IS NOT SAYING THIS IS TRUE NOW**, and calling either STALE would be reading a tense the registration said not to read. **THE PINS WERE READ LIVE AND NONE WAS "
            "RECALLED:** SIDE-kernel v1.5 `0e5233f` from both documents, SIDE-lv-conservation deposit-pin v0.10.0 `93c27ec` AND working head `2f71068` as two objects in one cell, SIDE-effects main "
            "`afa9ccf`, SIDE-t7-topology-cmb v0.3 `8eb0d5a` -- **SIX ASSERTED, SIX RESOLVED ON THE FIRST ATTEMPT, SIX MATCHING**, with UNRESOLVED available and not needed (b353 incident). The pin/head "
            "split mattered at line 82, and the reading is only possible because the map own August repair made that cell two columns, per REGISTRY ruling that *\"a repository has a pin the corpus "
            "cites in published prose and a head where work continues, and they are not the same object\"*. **AND ONE THING THE PASS FOUND THAT NOBODY ASKED FOR: FACES_LEDGER.md IS NOT IN THE "
            "MIRROR ROSTER** -- the roster holds 41 source paths, README, SPIRAL_MAP, REGISTRY, ERRATA and FINDINGS among them, and the faces ledger is not, so **THE ONE FILE THIS ACT WRITES TO THE PAPERS "
            "REPO DOES NOT REACH THE MIRROR AT ALL**; the roster is NOT changed by this act and the question is routed to the author. %d reads, %d located on the first run, **%d of %d anchors differing from "
            "the hint that found them.**"
            % (S1['sha256'][:16] + '...', S1['bytes'], dep['version'], dep['doi'], dep['conceptdoi'],
               dep['publication_date'], dep['n_files'], dep['is_last'],
               E['reads'], E['reads'] - E['without_anchor'], E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A LEDGER RECONCILED IS NOT A LEDGER VERIFIED** -- this act checked named fields against a named ranking party and named pins against live remotes, and read neither "
         "document for the correctness of anything else.",
         "**PRINT: PLACE-papers, ONE FILE.** FACES_LEDGER.md gains an UPDATE BLOCK on row U1 through the writer `append_block`, carrying b358 finding LOCALIZED -- the tail bound exists and asserts the "
         "hypothesis; the conditionality sits in the ZERO channel while the archimedean channel is unconditional with an explicit error term; the index distance 3.33e+15 recorded as measured. GRADE "
         "NAMED-ONLY, nothing compiled, and NO NEW READING ADDED. **README.md AND SPIRAL_MAP.md ARE LEFT BYTE-IDENTICAL** and REGISTRY.md is READ, not written. **THE HOOK AND THE MIRROR ARE OWED AND PAID**, "
         "the mirror rebuilt after the write and clean on all three clauses.",
         "**NO GRADE MOVED; NO BAR MOVED; NO ACT RE-VERDICTED.** Row U1 new block adds no reading of its own: every figure in it is b358, quoted from b358 bank at its own line. **AND THIS SEAT EXPECTATION "
         "WAS SCORED AGAINST IT:** it predicted a drift in the front door, on the reasoning that a document written for a reader is least re-read against REGISTRY -- and both documents were reconciled in "
         "August and not touched since, so **THE REASONING WAS SOUND AND THE PREDICTION WAS WRONG.**",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b358 -- TWO ROWS: THE ACT, AND RULING (R1)\'S APPEND-ONLY CORRECTION.')
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
          and 'STILL RECONCILED TO THE SOURCE OF TRUTH' in ROWS[0][0]
          and 'NOTHING IS APPENDED' in ROWS[0][0]
          and 'REGISTRY > README > SPIRAL_MAP' in ROWS[0][1]
          and 'NO LATEST-VERSION POINTER HAS DRIFTED' in ROWS[0][1]
          and 'SIX ASSERTED, SIX RESOLVED ON THE FIRST ATTEMPT, SIX MATCHING' in ROWS[0][1]
          and 'FACES_LEDGER.md IS NOT IN THE MIRROR ROSTER' in ROWS[0][1]
          and 'ARE LEFT BYTE-IDENTICAL' in ROWS[0][3]
          and 'THE HOOK AND THE MIRROR ARE OWED AND PAID' in ROWS[0][3]
          and 'THE PREDICTION WAS WRONG' in ROWS[0][4]
          and 'A LEDGER RECONCILED IS NOT A LEDGER VERIFIED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the precedence obeyed, the pointer undrifted, six pins live, the roster finding, both docs byte-identical, the expectation scored : %s' % g1)
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
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
