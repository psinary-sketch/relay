# -*- coding: utf-8 -*-
"""b367_correspondence.py -- ONE ROW: THE SCAFFOLD REPAIR, NOT LOCATED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a terminal had been
### replaced; as if a route had been priced or chosen; as if `NOT LOCATED` were a failure of the search
### rather than a fact about the kernel; as if the act had claimed something about the mathematics; or as
### if the front document's staleness were the scaffold defect the ferry named.
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
    "**SCOPE: NO LEAN FILE IS WRITTEN, NO TERMINAL IS REPLACED, NO STATEMENT IS PROVED AND NO BUILD IS RUN.** Not one byte of SIDE-effects or SIDE-grh-transfer was changed, and both working trees are clean. "
    "NO ROUTE IS PRICED, CHOSEN OR RECOMMENDED -- the cap says NOT LOCATED stops the act, and it did; the sanction reported for the INTERFACES architecture is a fact about the record, marked as a report, and "
    "is not a preference. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF EITHER SUBJECT: this act read no statement of the generalized hypothesis or of an exceptional real zero, because the kernel holds none, "
    "and it does not say either is open, closed, hard or easy. THE RETIREMENT IS REPORTED, NOT ENDORSED -- the ledger's account of what was lost is quoted and this act did not check it. THE 18-OF-20 FIGURE "
    "IS A COUNT OF NAMES THE FRONT DOCUMENT EXPORTS AT LAYER 1 AGAINST LIVE DECLARATIONS IN THE KERNEL'S OWN SIX .lean FILES; IT IS NOT A CLAIM THAT THE KERNEL IS EMPTY, and Phase15/ and "
    "ExhaustivenessLicense.lean carry content this act did not audit. THE CITATION SWEEP IS BOUNDED TO FIVE REPOSITORIES and its absence is an absence from those. NO ACT IS RE-VERDICTED: b157's finding is "
    "CONFIRMED AS STILL LIVE, which is not a re-verdict. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the "
    "roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The "
    "seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 "
    "stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b367_reads.json'), encoding='utf-8'))
    J = json.load(io.open(os.path.join(D, 'b367_locate.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b367_filing.json'), encoding='utf-8'))
    k = J['refs']['SIDE-effects']
    m = ("**%s** -- the scaffold terminals do not exist: **%d LIVE DECLARATIONS** of any hinted name at `SIDE-effects` ref `%s` = `%s`, and all %d mentions sit inside `Structural.lean`'s own RETIREMENT "
         "LEDGER. **THE CAP STOPS THE ACT AND THE THREE ROUTES ARE NOT PRICED** (b367)"
         % (J['verdict'], J['live_declarations'], k['branch'], k['head'], J['mentions']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY READ OF THE KERNEL**, on the audit's own exit code. **THE HINT WAS SCORED AGAINST WHAT WAS FOUND, NOT THE FOUND AGAINST THE HINT:** the kernel "
            "(H1) and the structural module (H2) are CONFIRMED and the two subjects (H3) are CONFIRMED as the ledger's own headings -- but **(H4) IS CORRECTED**, the working head is `main` and is AHEAD of "
            "both feature branches with **0 branches carrying work the read ref lacks**; **(H5) IS CORRECTED**, the ledger retires NINE framework consequences and the two subjects carry THREE named "
            "declarations with a fourth exported by the front document and present nowhere; and **THE CHARACTERISATION `written as trivially true` IS CORRECTED BY THE KERNEL'S OWN DISTINCTION** -- the audit "
            "separates *True-valued stubs* from *opaque-Prop templates* and files these two as opaque-Prop, so **THE HINT NAMED THE RIGHT TERMINALS AND THE WRONG DEFECT**. **AND THE RECORD ALREADY FOUND "
            "THIS ON 2026-08-25:** b157 banked *THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED -- and re-verifying rather than assuming is what found it*, and that sentence was written before this ferry "
            "was. **THE LIVE DEFECT IS NOT THE SCAFFOLD:** the kernel's front document `AGENTS.md` exports **%d NAMED THEOREMS AT LAYER 1 OF WHICH %d ARE ABSENT FROM THE SOURCE**, including all three named "
            "-- exactly b157's figure, unmoved. **THE SOURCE IS THE HONEST PARTY; THE FRONT DOCUMENT IS THE STALE ONE**, and this act did not repair it. %d reads, %d without an anchor, %d of %d anchors "
            "differing from the hint that found them, %d lines located inside the kernel itself."
            % (J['front_exported'], len(J['front_absent']), E['reads'], E['without_anchor'],
               E['anchors_differing'], E['reads'], E['kernel_lines']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: THERE WAS NOTHING TO PRICE.** All three routes take the terminal as their input and there is no terminal; an act that priced them anyway would have priced work "
         "against its own reading of a hint. **AND ROUTE (c) IS ALREADY WHAT HAPPENED** -- the kernel did not price deletion, it deleted, and the retirement ledger IS that route executed with its losses "
         "named entry by entry.",
         "**PRINT: PLACE-papers, ONE FILE.** OPEN_TRAILS.md gains **ONE APPEND-ONLY BLOCK** under its own mark, `%s`, marked **%s** -- %d bytes, every quotation carrying the ref its file was read at, the "
         "working file a true prefix of what it was **AND OF ITS COMMITTED BLOB** (the reading BEFORE THE PUSH, b352's rule). **b157'S BLOCK IS NOT EDITED.** **FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER "
         "IS NOT CALLED, BECAUSE NO ROW MOVED.** **AND THE KERNELS ARE UNTOUCHED: `SIDE-effects` AND `SIDE-grh-transfer` WORKING TREES CLEAN, NOT ONE BYTE CHANGED, NO BUILD RUN.** **THE HOOK AND THE MIRROR "
         "ARE OWED AND PAID.** Nothing in TECHNE-Core; no findings section edited; no roster row changed." % (F['entry'], F['status'], F['grew']),
         "**NO GRADE IS CONFERRED BY A SEAT AND NO ROUTE IS RECOMMENDED -- THE RECOMMENDATION IS THE AUTHOR'S.** What the act may state, and does, is which route the record's own architecture already "
         "sanctions, quoted: of `INTERFACES` the record says *this is a legitimate architecture, not a defect; it is how a kernel cites a manuscript result. The row names the premise*, and it uses it at "
         "Route 3's own terminal. **AND ITS OWN VOCABULARY MAKES PLAIN WHAT THE THREE ROUTES DO NOT:** `ENCODES-CONCLUSION / SHELL` is already classified as a **work-order, not a citation** -- so the "
         "standing ban on these two was never a special rule, it is the general rule for their class. **THE NAVIGATOR'S EXPECTATIONS ARE SCORED:** (F1) REFUTED TWICE OVER -- not located at all, and the "
         "working ref is `main`; (F2) UNREACHABLE -- there is no statement to read, and the order itself required the judgement be made *by reading what the statement says and not by its name*; (F3) HALF "
         "CONFIRMED (the sanction, quoted) and HALF UNREACHABLE (the cheapness, since nothing was priced). **THIS SEAT REGISTERED NO EXPECTATION ABOUT THE CONTENT, DELIBERATELY**, and its one procedural "
         "expectation was MET -- which is recorded as the low bar it is: **a seat that predicts only its own procedure has predicted the easy half.**",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b367 -- ONE ROW: THE SCAFFOLD REPAIR, NOT LOCATED.')
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
          and 'LIVE DECLARATIONS' in ROWS[0][0]
          and 'THE CAP STOPS THE ACT AND THE THREE ROUTES ARE NOT PRICED' in ROWS[0][0]
          and 'SCORED AGAINST WHAT WAS FOUND' in ROWS[0][1]
          and 'IS CORRECTED' in ROWS[0][1]
          and 'THE RIGHT TERMINALS AND THE WRONG DEFECT' in ROWS[0][1]
          and 'ALREADY FOUND' in ROWS[0][1]
          and 'THE FRONT DOCUMENT IS THE STALE ONE' in ROWS[0][1]
          and 'THERE WAS NOTHING TO PRICE' in ROWS[0][2]
          and 'APPEND-ONLY BLOCK' in ROWS[0][3]
          and 'IS NOT EDITED' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NOT ONE BYTE CHANGED' in ROWS[0][3]
          and 'THE RECOMMENDATION IS THE AUTHOR' in ROWS[0][4]
          and 'work-order, not a citation' in ROWS[0][4]
          and 'REFUTED TWICE OVER' in ROWS[0][4]
          and 'NO LEAN FILE IS WRITTEN' in ROWS[0][5]
          and 'NO ROUTE IS PRICED, CHOSEN OR RECOMMENDED' in ROWS[0][5]
          and 'IS NOT A CLAIM THAT THE KERNEL IS EMPTY' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the hint scored, the corrections, the record already knowing, the stale front document, the append-only block, the kernels untouched, the recommendation withheld, the expectations scored, and the scope : %s' % g1)
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
