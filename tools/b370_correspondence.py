# -*- coding: utf-8 -*-
"""b370_correspondence.py -- ONE ROW: THE FOLD, b361 THROUGH b369.

### ### **THE HAZARDS THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a fold were a finding;
### as if the span's two shape results were progress on the clause; as if the seven apparatus acts were;
### as if the desk had been confirmed; or as if the hook's durability had been fixed rather than priced.
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
    "**SCOPE: A FOLD PROVES NOTHING, DISCHARGES NOTHING AND MOVES NO GRADE.** No act in the span is re-verdicted; every grade below is its own act's, checked verbatim against that act's bank. **NOTHING IN "
    "THE FOLD IS NEW MATHEMATICS**, and the span produced none: its two results are about the clause's SHAPE and are left at the grades their own acts gave them, NOT PROMOTED HERE. **SEVEN OF THE NINE ACTS "
    "PRODUCED NO RESULT ABOUT THE OBJECT AT ALL** and the fold says so rather than letting them read as progress. **NO EXISTING SECTION OF FINDINGS.md IS EDITED** and no ledger row is moved. **NO DESK ITEM "
    "IS CLOSED**: a CONFIRMED-BY-FILE mark says a banked file MENTIONS the item, not that it was re-verified — and that same number with that same caveat has now been reported three acts running. **NO "
    "DURABLE HOOK FIX IS BUILT**: it is named and priced only, and `.git/hooks/` remains untracked so a fresh clone of any of the four repositories still starts with no hook. **NO REPOSITORY IS AUDITED, NO "
    "PUBLIC SURFACE IS READ FOR CORRECTNESS AND NO REPOSITORY IS GRADED**; Component 5 is NAMED and PRICED and the profile that would settle its first target is NOT OPENED. **NO .lean FILE IS TOUCHED, NO "
    "BUILD IS RUN, NO TECHNE MODULE IS PUSHED.** NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE "
    "OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; "
    "M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT "
    "LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b370_reads.json'), encoding='utf-8'))
    S = json.load(io.open(os.path.join(D, 'b370_span.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b370_fold.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b370_lore.json'), encoding='utf-8'))
    Q = json.load(io.open(os.path.join(D, 'b370_desk.json'), encoding='utf-8'))
    m = ("**THE FOLD, b%d THROUGH b%d — %d ACTS, THE SPAN COUNTED AND NOT TYPED, AND THE SECTION WRITTEN ONLY BECAUSE THE COUNT AGREED WITH THE RANGE IT NAMES** (b370)"
         % (S['span_starts_at'], S['this_act'], S['current_span']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code. **F-NOGRADE HELD: %d grade strings were not found verbatim in their own act's bank**, which is the "
            "condition under which the section gets written at all. **AND THE ATTRIBUTION WAS THE HARD HALF, NOT THE PRESENCE:** the grade word `SUPPORTED-BY-THE-SOURCE'S-APPLICATION` is b366's RULING and "
            "not b365's FINDING — b365's own bank says `SUPPORTED AT ζ, WITH A STATED CONSTANT`, and that is what b365's row carries. **%d obstacles are quoted, each located by the anchor tool in the bank of "
            "the act that ORIGINATED it** and never in a later act's summary of it. **THE FOLD IS PURELY ADDITIVE:** FINDINGS.md before is a true prefix of FINDINGS.md after (%s) and of its committed blob "
            "(%s), read BEFORE THE PUSH; %d lines appended, %d existing sections edited. **AND TWO FURTHER TABLES:** %d corrections the acts made to their own readings and to each other's — including b369 "
            "correcting b368's ledger SPLIT while b368's COUNT stands — and %d acts' DECLARED DEFECTS, present because the arc's claimed product is a record checkable by a reader who trusts none of it, and a "
            "record whose defects are declared only when convenient is not that. %d reads, %d without an anchor."
            % (F['grade_misses'], F['obstacles'], F['prefix_of_file'], F['prefix_of_blob'],
               F['lines_appended'], F['sections_edited'], F['corrections'], F['defects'],
               E['reads'], E['without_anchor']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND A FOLD HAS NONE TO HAVE.** No `.lean` file was touched, no build was run and nothing was compiled. The span's two shape results — the approximation register closed with its "
         "obstruction a RATE (b362), and the Li localization's archimedean half supported at `ζ` with a stated constant (b361, b365) — belong to their own acts at their own grades and are **NOT PROMOTED BY "
         "THIS ROW**.",
         "**PRINT: THREE REPOSITORIES.** `PLACE-papers/FINDINGS.md` gains **ONE FOLD SECTION, PURELY ADDITIVE** (%d bytes): the span table, the obstacles table, the corrections table, the declared-defects "
         "table and the arc statement. `TECHNE-Core` gains **%d MINTED MODULES** — `ONE_INCIDENT_IS_NOT_A_PARTITION`, `PREDICATE_ONE_SHAPE`, `DURABILITY_SPLIT` — **COMMITTED LOCALLY AT %s AND NOT PUSHED** "
         "(%s ahead of origin; %d modules now). `relay` gains this act's tools and **ONE REPAIRED OWNER INSTRUMENT**: `tools/b363_span.py`, which for two acts wrote a run file and a JSON under b363's own stem "
         "on every run, whoever ran it — **filed twice, fixed never, and it cost a revert both times.** It now **READS AND DOES NOT WRITE**; a caller who wants a record passes `--emit` and gets it **UNDER ITS "
         "OWN STEM**; its act number is read from the record instead of baked into the file; and **A FIXTURE PROVES IT IN BOTH POLARITIES** — a default run leaves the foreign pointer BYTE-IDENTICAL, and an "
         "`--emit` run DOES still write, because an arm that cannot fail is not an arm. **FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** **THE HOOK AND THE MIRROR ARE "
         "OWED AND PAID.**"
         % (F['grew'], L['minted'], L['techne_head'], L['commits_ahead_of_origin'], L['modules_now']),
         "**THE ARC AS ONE STATEMENT, AT THE GRADE THE ACTS SUPPORT: this span produced NO NEW MATHEMATICS about the clause.** It produced two results about the clause's SHAPE, and **ITS MAIN PRODUCT WAS "
         "NEITHER — it was making the record checkable by a reader who trusts none of it.** **SEVEN OF THE NINE ACTS PRODUCED NO RESULT ABOUT THE OBJECT AT ALL:** they built a needle helper and measured its "
         "reach against the banks rather than the draft that proposed it; diagnosed a failing suite instead of repairing it to pass; swept every arm in the record for a species one of them had just minted; and "
         "found, measured and repaired a front document exporting eighteen names its source does not declare. **A FOLD THAT LET THOSE SEVEN READ AS PROGRESS ON THE CLAUSE WOULD BE THE EXACT DEFECT THIS SPAN "
         "SPENT ITSELF FINDING ELSEWHERE.** **THE THREE MINTS, EACH WITH ITS MECHANIZABLE HALF STATED APART:** *one incident does not show you a partition* (**no mechanizable half at all, and the module says "
         "so first**); *a predicate that knows one shape finds one shape* — five incidents in nine acts, and **the sharp one was caught by RE-DERIVATION and NOT by any arm, because the gate would have been "
         "written by the same hand with the same predicate**; and *the durability split* — **the guards that have caught the most are the ones a fresh clone starts without**, mechanizable as a DURABLE / NOT "
         "DURABLE column and **not** mechanizable as a ranking by what a guard has caught. **THE DESK: %d items, %d CONFIRMED-BY-FILE, %d UNCONFIRMED, %d CLOSED — the third act running to report that number "
         "with that caveat.** **A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING**, and b369's draft asked for one item to be re-verified properly; this order did "
         "not carry it, **so it is carried forward again, which is itself the finding.** **COMPONENT 5 IS NAMED, PRICED AND NOT OPENED:** the federation currency audit enumerates **SURFACE KINDS and not "
         "repositories alone**, because the defect just repaired lived where b369's ranking could not look; its first target is the one confirmed live claim — the construction kernel's description naming a "
         "Core terminal count against a larger certified profile — **to be settled SCOPE-DEPENDENT or STALE by one read, and that read is precisely the one this act may not make.** **THE EXPECTATIONS ARE "
         "SCORED:** (E1) **MET**; (E2) **REFUTED** — the no-grade-moved arm reported zero misses because the check it mechanizes was run by hand one step earlier, and **a seat saying its own arm would have "
         "caught something it never saw is exactly the claim this record distrusts**, so the prediction is recorded as wrong with the seat unable to prove why."
         % (Q['items'], Q['confirmed'], Q['unconfirmed'], Q['items_closed']),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b370 -- ONE ROW: THE FOLD, b361 THROUGH b369.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (b303): %s %s %s %s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = ('THE SPAN COUNTED AND NOT TYPED' in ROWS[0][0]
          and 'F-NOGRADE HELD' in ROWS[0][1]
          and "b366's RULING" in ROWS[0][1]
          and 'ORIGINATED' in ROWS[0][1]
          and 'PURELY ADDITIVE' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'NOT PROMOTED BY' in ROWS[0][2]
          and 'NOT PUSHED' in ROWS[0][3]
          and 'READS AND DOES NOT WRITE' in ROWS[0][3]
          and 'BOTH POLARITIES' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NO NEW MATHEMATICS' in ROWS[0][4]
          and 'SEVEN OF THE NINE' in ROWS[0][4]
          and 'NOT by any arm' in ROWS[0][4]
          and 'NOBODY IS USING' in ROWS[0][4]
          and 'NAMED, PRICED AND NOT OPENED' in ROWS[0][4]
          and 'REFUTED' in ROWS[0][4]
          and 'MOVES NO GRADE' in ROWS[0][5]
          and 'NO DESK ITEM' in ROWS[0][5]
          and 'NO DURABLE HOOK FIX IS BUILT' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the counted span, F-NOGRADE with its hard half, the additive bar, no terminal, '
          'the repaired instrument with its two-polarity fixture, the arc statement, the three mints, '
          'the desk caveat, the next arc named and not opened, the expectations, and the scope : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
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
    print('  READ BACK : last row number is %d ; cells on disk %s (6 required, none blank)'
          % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
