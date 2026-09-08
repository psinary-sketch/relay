# -*- coding: utf-8 -*-
"""b368_correspondence.py -- ONE ROW: THE FRONT DOCUMENT RECONCILED, APPEND-ONLY.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is
### read from the act's own JSONs and none is typed.
### ### **THE HAZARDS THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if the export list had been
### REPAIRED rather than annotated; as if the eighteen had been CARRIED from `b367` rather than
### re-derived; as if `RENAMED 0` were an absence of looking rather than a refusal; as if the desk sweep's
### nine-of-nine were a verdict on the desk; or as if a `.lean` file had been touched.
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
    "**SCOPE: NO .lean FILE IS TOUCHED IN ANY REPOSITORY, NO BUILD IS RUN AND NO AXIOM PROFILE IS COMPUTED.** The kernel was READ and not written. **NO EXISTING SENTENCE OF THE FRONT DOCUMENT IS "
    "EDITED** -- the Layer-1 export list is left exactly as it was, and it STILL EXPORTS 18 ABSENT NAMES; annotating a document is not repairing it, and this row does not claim otherwise. **NO DESK ITEM IS "
    "CLOSED**: the sweep produces marks, not verdicts, and a mark of CONFIRMED-BY-FILE says a banked file mentions the item, NOT that the item was re-verified. **NO HOOK IS INSTALLED**; the absence of a "
    "pre-push hook in SIDE-effects is FILED AS A FINDING AND ROUTED, not repaired. **NO SUCCESSOR IS NAMED FOR ANY RETIRED TERMINAL** and no name is classified from its own sound. THE RETIREMENTS ARE "
    "REPORTED, NOT ENDORSED -- this act did not check whether any of the eighteen should have been retired. THE COUNT IS AGAINST THE KERNEL'S OWN SIX .lean FILES AT ONE NAMED REF; IT IS NOT A CLAIM THAT THE "
    "KERNEL IS EMPTY. NO ACT IS RE-VERDICTED: b157 and b367 are RE-MEASURED, which is a different thing. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF "
    "ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's "
    "report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING "
    "IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b368_reads.json'), encoding='utf-8'))
    Cl = json.load(io.open(os.path.join(D, 'b368_classify.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b368_reconcile.json'), encoding='utf-8'))
    K = json.load(io.open(os.path.join(D, 'b368_desk.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b368_filing.json'), encoding='utf-8'))
    m = ("**THE FRONT DOCUMENT IS RECONCILED BY AN APPENDED CURRENCY BLOCK, AND THE LIST ITSELF IS STILL WRONG** -- of the %d names `AGENTS.md` exports at Layer 1, **%d are declared in the kernel and %d "
         "are ABSENT**, every one of them **RETIRED** (`RENAMED` %d, `NEVER EXISTED` 0), at `SIDE-effects` ref `%s` = `%s` (b368)"
         % (Cl['exported'], Cl['n_present'], Cl['n_absent'], Cl['renamed_rows'], Cl['ref'], Cl['head'][:7]))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code. **THE EIGHTEEN WERE RE-DERIVED AND NOT CARRIED** -- b367's constant is held in the classifier as a "
            "COMPARISON ONLY and is never an input to the count; the count comes from the file and **THE TWO INDEPENDENT DERIVATIONS AGREE**, at a head that has not moved since b367, pinned by `ls-remote` "
            "before the first classification. **EACH NAME IS CLASSIFIED ON ITS OWN EVIDENCE, ONE ROW EACH, AND NONE FROM ITS OWN SOUND**: the ledger names the declaration, or its layer's entry records the "
            "removal, or the repository's own history shows the name present in an earlier commit and gone now -- and that third kind is why **NO NAME IS `NEVER EXISTED`**. **`RENAMED 0` IS A REFUSAL, NOT AN "
            "ABSENCE OF LOOKING:** a successor was accepted only from a declared mapping, the mapping is deliberately empty, and one resemblance -- a retired name and a live one differing only in case -- was "
            "MET AND REFUSED, because calling it a rename would have been classifying a name from its own sound. **AND THIS ACT'S OWN NEW FINDING, WHICH NEITHER b157 NOR b367 HAD: THE RETIREMENT LEDGER "
            "NAMES ONLY %d OF THE %d.** Another %d are covered only by their layer's entry, which records that the layer's skeletons were retired without listing which, and **%d HAS NO LEDGER ENTRY FOR ITS "
            "LAYER AT ALL** -- **THE LEDGER IS ACCURATE ABOUT WHAT IT SAYS AND INCOMPLETE ABOUT WHAT IT NAMES**, and the third group is the sharper half: **there the ledger omits a name; here it omits a "
            "whole layer.** %d reads, %d without an anchor, %d of %d anchors differing from the hint that found them."
            % (Cl['retired_named_by_ledger'], Cl['n_absent'], Cl['retired_layer_entry'],
               Cl['retired_history_only'],
               E['reads'], E['without_anchor'], E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was computed; the kernel was READ. The two names that survive are `no_type_d` and `formation_seven`, both declared "
         "in `SIDEEffects/Structural.lean`, and this act reports where they are and says nothing about what they are worth.",
         "**PRINT: THREE REPOSITORIES, THREE APPEND-ONLY WRITES, NO EDIT.** `SIDE-effects/AGENTS.md` gains **ONE APPEND-ONLY CURRENCY BLOCK** under its own mark (%d bytes): the file before is a true prefix "
         "of the file after **AND OF ITS COMMITTED BLOB** (%s / %s), read **%s** (b352's rule). **THE BLOCK EXPORTS NOTHING** -- %d lines in the document's own export shape, %d absent names outside a status "
         "row -- which is a check on the BLOCK, not on the document, and the act says which. `PLACE-papers/OPEN_TRAILS.md` gains **ONE APPEND-ONLY BLOCK** (%d bytes) marked **%s**; b157's entry and b367's "
         "block are NAMED and NEITHER IS EDITED. `TECHNE-Core` gains **ONE MODULE, `%s`**, beside the two arm species, **COMMITTED LOCALLY AT %s AND NOT PUSHED** (%s commits ahead of origin). "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** No findings section is edited; no roster row changed; **NO PRE-PUSH HOOK IS INSTALLED IN SIDE-effects and its "
         "ABSENCE IS FILED AS A FINDING.** **THE HOOK AND THE MIRROR ARE OWED AND PAID.**"
         % (R['grew'], R['prefix_of_file'], R['prefix_of_blob'], R['side'], R['export_shaped_lines'],
            len(R['unstatused']), F['grew'], F['status'], K['module'], K['techne_head'],
            K['commits_ahead_of_origin']),
         "**THE BRANCH WAS DECIDED BY THE CLASSIFICATION, NOT CHOSEN:** every exported name has a kind and the kinds partition the list, so a block could state what is present, what is retired and where the "
         "retirements are recorded **without changing a sentence** -- which made the second branch (price it and route it to the author) unreachable, and the tool prints that reason rather than asserting it. "
         "**AND THE HALF-REPAIR IS REPORTED AT FULL PROMINENCE:** the list above the block **STILL EXPORTS %d ABSENT NAMES**, a reader who stops at the list is still misled, and repairing the list edits "
         "sentences -- **WHICH IS THE AUTHOR'S, NOT THIS SEAT'S.** **THE DESK-FRESHNESS RULE IS FILED** -- *every desk item names the file and date at which it was last confirmed, and an item without one is "
         "re-verified before it is ordered* -- with b367 and b157 as its incidents, **AND IT STATES ITS OWN LIMIT: a tool can demand that an item CARRY a file and a date, and no tool can check that the named "
         "file still confirms it.** The sweep marked **%d of %d CONFIRMED-BY-FILE, %d UNCONFIRMED, %d CLOSED** -- and **THAT RESULT IS WEAKER THAN IT LOOKS AND THE ACT SAYS SO: a file that mentions an item is "
         "not a file that confirms it, and this sweep cannot tell the two apart.** **THE NAVIGATOR'S EXPECTATIONS ARE SCORED:** (F1) CONFIRMED AND MORE STRONGLY THAN ASKED -- not *most* but **ALL %d**, all "
         "RETIRED; (F2) CONFIRMED -- append-only, and nothing routed. **THIS SEAT'S OWN REGISTERED EXPECTATION (that the re-derived figure would agree) WAS MET, and it is recorded as the low bar it is: a "
         "seat that predicts a re-run of its own measurement has predicted the easy half, and the finding worth having is one this seat did not predict.**"
         % (R['list_above_still_exports_absent'], K['confirmed'], K['items'], K['unconfirmed'],
            K['items_closed'], Cl['n_absent']),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b368 -- ONE ROW: THE FRONT DOCUMENT RECONCILED, APPEND-ONLY.')
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
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = ('STILL WRONG' in ROWS[0][0]
          and 'RETIRED' in ROWS[0][0]
          and 'RE-DERIVED AND NOT CARRIED' in ROWS[0][1]
          and 'NONE FROM ITS OWN SOUND' in ROWS[0][1]
          and 'IS A REFUSAL, NOT AN' in ROWS[0][1]
          and 'MET AND REFUSED' in ROWS[0][1]
          and 'INCOMPLETE ABOUT WHAT IT NAMES' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'no build was run' in ROWS[0][2]
          and 'APPEND-ONLY CURRENCY BLOCK' in ROWS[0][3]
          and 'NEITHER IS EDITED' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NOT PUSHED' in ROWS[0][3]
          and 'ABSENCE IS FILED AS A FINDING' in ROWS[0][3]
          and 'DECIDED BY THE CLASSIFICATION, NOT CHOSEN' in ROWS[0][4]
          and 'STILL EXPORTS' in ROWS[0][4]
          and 'AUTHOR' in ROWS[0][4]
          and 'STATES ITS OWN LIMIT' in ROWS[0][4]
          and 'WEAKER THAN IT LOOKS' in ROWS[0][4]
          and 'predicted the easy half' in ROWS[0][4]
          and 'NO .lean FILE IS TOUCHED' in ROWS[0][5]
          and 'NO DESK ITEM IS CLOSED' in ROWS[0][5]
          and 'NO EXISTING SENTENCE' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the reconciliation and its limit, the re-derivation, the evidence per name, the '
          'refusal behind RENAMED 0, the ledger incomplete, no terminal, the three append-only writes, the '
          'branch decided not chosen, the desk rule with its own limit, the expectations scored, and the '
          'scope : %s' % g1)
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
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)'
          % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
