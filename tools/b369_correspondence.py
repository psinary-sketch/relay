# -*- coding: utf-8 -*-
"""b369_correspondence.py -- ONE ROW: THE LIST REPAIRED, THE ROSTER MENDED, THE PASS PRICED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is
### read from the act's own JSONs and none is typed.
### ### **THE HAZARDS THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if the front document were
### now CORRECT (its count claim stands); as if the preservation were an append (it is a bounded EDIT);
### as if `b368` had been re-verdicted (its COUNT stands, its SPLIT is corrected); as if the pass had
### been RUN; or as if the hook install were as durable as the roster mend.
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
    "**SCOPE: NO .lean FILE IS TOUCHED IN ANY REPOSITORY, NO BUILD IS RUN AND NO AXIOM PROFILE IS COMPUTED.** The kernel was READ and its front document edited. **THE FRONT DOCUMENT IS NOT NOW CORRECT:** the "
    "paragraph above the repaired list still asserts a count of framework consequences and THIS ACT DID NOT TOUCH IT, because the order said the LIST is corrected and a count is not a name. **NO REPOSITORY "
    "IS AUDITED, NO PUBLIC SURFACE IS READ FOR CORRECTNESS AND NO REPOSITORY IS GRADED** -- `audit nothing` is the order's own cap; a count-SHAPED string is not a claim and an age is not a staleness. **NO "
    "RETIREMENT REASON IS SUPPLIED** beyond what the kernel's own record carries (R5), and NO SUCCESSOR IS NAMED. **NO SENTENCE OF b368's BLOCK IS EDITED**: it is named and marked superseded. **NO ACT IS "
    "RE-VERDICTED** -- b368's COUNT stands and is confirmed a third time; its SPLIT is corrected, which is a measurement replaced by a better measurement, not a verdict withdrawn by a seat. **NO DESK ITEM IS "
    "CLOSED**: the sweep produces marks, not verdicts, and a CONFIRMED-BY-FILE mark says a banked file MENTIONS the item, not that it was re-verified. **THE HOOK INSTALL IS NOT DURABLE**: `.git/hooks/` is "
    "untracked and a fresh clone still has none; only the roster mend survives a clone. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. "
    "NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS "
    "UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED "
    "on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND "
    "NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b369_reads.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b369_repair.json'), encoding='utf-8'))
    K = json.load(io.open(os.path.join(D, 'b369_hygiene.json'), encoding='utf-8'))
    P = json.load(io.open(os.path.join(D, 'b369_pass.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b369_filing.json'), encoding='utf-8'))
    Q = json.load(io.open(os.path.join(D, 'b369_desk.json'), encoding='utf-8'))
    m = ("**THE LAYER-1 LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED VERBATIM IN THE SAME FILE** -- %d export rows quoted, verified byte-for-byte, and only then replaced by %d; the repaired list "
         "carries **%d** of the names the classification calls absent, by a content predicate; at `SIDE-effects` ref `%s` = `%s` (b369, ruling (R4))"
         % (R['rows_replaced'], R['rows_written'], len(R['still_absent']), R['ref'], R['head'][:7]))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code. **THE EDIT IS BOUNDED AND THE BOUND IS MEASURED, NOT ASSERTED:** every byte above the rows is its committed "
            "blob's (%s) and every byte below them up to the appended note is too (%s), both read BEFORE THE PUSH -- **an edit is not an append, and this act does not claim a prefix arm it cannot have.** "
            "**THE CLASSIFICATION WAS RE-DERIVED FOR THE THIRD TIME AND AGREES FOR THE THIRD TIME:** of %d names, %d declared and %d absent, b368's figure held as a COMPARISON ONLY and never an input. **AND "
            "THE RE-DERIVATION IS WHAT CAUGHT THE FINDING NOBODY REGISTERED: b368's SHARPER CLAIM IS WRONG.** b368 reported one retired name as having NO LEDGER ENTRY FOR ITS LAYER AT ALL and called that the "
            "sharper half of its finding; **the ledger carries an entry HEADED BY THAT DECLARATION'S OWN NAME.** b368's predicate required a backtick or a slash before a name and the ledger names that one as "
            "a bare heading -- **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, which is b368's own sentence about AGENTS.md turned on b368. Re-derived from the ledger's own entry headings the split is "
            "**%d named outright, %d named only by its slash abbreviation (kept apart, because reading an abbreviation as naming its expansions is a judgement, not a string match), %d covered only by a layer "
            "entry, and %d not covered at all** -- **every retired name is reached by the ledger.** %d reads, %d without an anchor."
            % (R['bar3_above'], R['bar3_below'], R['exported'], R['n_present'], R['n_absent'],
               R['n_named'], R['n_by_abbr'], R['n_layer_only'], R['n_silent'],
               E['reads'], E['without_anchor']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was computed. The two names the repaired list still exports are `no_type_d` and `formation_seven`, both declared in "
         "`SIDEEffects/Structural.lean`; this act reports where they are and says nothing about what they are worth.",
         "**PRINT: FOUR REPOSITORIES.** `SIDE-effects/AGENTS.md` -- **THE LIST REPAIRED IN PLACE** plus ONE appended note carrying the original verbatim and marking two of b368's sentences SUPERSEDED (they are "
         "NOT edited). `PLACE-papers/OPEN_TRAILS.md` -- ONE append-only block (%d bytes) marked **%s**; b157's entry and b367's and b368's blocks are named and none is edited. `relay` -- **TWO OWNER "
         "INSTRUMENTS EDITED, BOTH NAMED ON THE REGISTRATION'S FACE BEFORE THE EDIT**: the pins roster and the hook exerciser's roster now name the exclusion kernel (%s), and the prose that counted them was "
         "mended in the same pass by %d exact string pairs, never a pattern -- **a tool that sweeps four repositories while announcing three is a dated arm in its own prose.** `SIDE-effects/.git/hooks/pre-push` "
         "-- **INSTALLED, byte-identical to the one tracked source (%s), and exercised in BOTH POLARITIES across every rostered repository with %d failing.** **FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS "
         "NOT CALLED, BECAUSE NO ROW MOVED.** No findings section; no TECHNE file; no module pushed. **THE HOOK AND THE MIRROR ARE OWED AND PAID.**"
         % (F['grew'], F['status'], ', '.join(K['rosters']['b303_pins.py']),
            sum(K['wording_pairs'].values()), K['hook_identical'], K['repos_failing']),
         "**THE REFINEMENT PASS IS PRICED AND NOT RUN: %d REPOSITORIES AUDITED, %d SURFACES READ FOR CORRECTNESS, %d REPOSITORIES GRADED.** The account was enumerated LIVE -- %d repositories, %d of them "
         "programme material -- because **a federation list typed from memory is the species DESK_FRESHNESS was minted against**. Surfaces listed and not read: %d descriptions, %d READMEs, %d front documents, "
         "%d `.lean` files. **THE PRICE SPLITS, AND THE SPLIT IS THE PART A PRICE USUALLY HIDES:** the mechanical half (does a surface exist; does it carry a count-shaped string; which identifiers does it name; "
         "do those have declarations) is ONE ACT and b368's classifier already does all four; **the read half does not scale and nothing in this pass makes it cheaper** -- b367 and b368 spent two whole acts on "
         "one front document against one kernel. **HIGHEST EXPOSURE by the order's own criterion, printed before the ranking so it can be disagreed with: %s** -- and **it is a ranking of EXPOSURE, NOT OF "
         "ERROR.** **AND WHAT THE RANKING CANNOT SEE IS REPORTED BECAUSE IT IS SHARP: `SIDE-effects` IS NOT ON IT**, since its description carries no count shape and the claim lived in its front document -- **a "
         "criterion is only as wide as the surface it reads.** **THE HINT IS SCORED AGAINST WHAT WAS FOUND:** (H1) **%s** -- exactly one description on the account uses the word *construction* and it carries "
         "the shape `%s`; (H2) **%s** -- deciding whether a count predates a profile requires reading the profile, which is the audit the cap forbids, and NOT LOCATED is an answer, not a failure. **THE DESK WAS "
         "SWEPT ONCE MORE UNDER b368's RULE, WHICH THIS ACT USED RATHER THAN RESTATED: %d items, %d CONFIRMED-BY-FILE, %d UNCONFIRMED, %d CLOSED** -- and **the same caveat is printed a second time because it "
         "has not changed: a file that mentions an item is not a file that confirms it.** **A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING**, and the draft asks the "
         "next act to re-verify one item properly. **THE EXPECTATIONS ARE SCORED:** (F1) **CONFIRMED** -- one bounded edit, and all %d original rows survive verbatim; (F2) **PARTLY SCORED, and the unreachable "
         "half was registered in advance** -- %d public repositories carry a count SHAPE, so the *more than one* half is confirmed for shapes, but whether any is OLDER than its kernel's state is the audit. This "
         "seat's own (E1) was **MET**, and is recorded as the low bar it is: **a seat that predicts the limits of its own cap has predicted the easy half**, and the finding worth having is one nobody registered."
         % (P['repositories_audited'], P['surfaces_read_for_correctness'], P['repositories_graded'],
            P['repos_on_account'], P['programme'], P['descriptions'], P['readmes'],
            P['front_documents'], P['lean_files'],
            ', '.join('`%s`' % x for x in P['highest_risk']),
            P['h1'].split(' --')[0],
            next((x['count_shapes'][0] for x in P['rows']
                  if x['name'] in P['construction_candidates'] and x['count_shapes']), '?'),
            P['h2'], Q['items'], Q['confirmed'], Q['unconfirmed'], Q['items_closed'],
            R['rows_replaced'], len(P['highest_risk'])),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b369 -- ONE ROW: THE LIST REPAIRED, THE ROSTER MENDED, THE PASS PRICED.')
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
    g1 = ('REPAIRED IN PLACE' in ROWS[0][0] and 'PRESERVED VERBATIM' in ROWS[0][0]
          and 'an edit is not an append' in ROWS[0][1]
          and 'RE-DERIVED FOR THE THIRD TIME' in ROWS[0][1]
          and "b368's SHARPER CLAIM IS WRONG" in ROWS[0][1]
          and 'ONE SHAPE FINDS ONE SHAPE' in ROWS[0][1]
          and 'not covered at all' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'no build was run' in ROWS[0][2]
          and 'SUPERSEDED' in ROWS[0][3]
          and 'NOT edited' in ROWS[0][3]
          and 'BOTH POLARITIES' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'PRICED AND NOT RUN' in ROWS[0][4]
          and 'EXPOSURE, NOT OF' in ROWS[0][4]
          and 'CANNOT SEE' in ROWS[0][4]
          and 'NOBODY IS USING' in ROWS[0][4]
          and 'predicted the easy half' in ROWS[0][4]
          and 'NO .lean FILE IS TOUCHED' in ROWS[0][5]
          and 'IS NOT NOW CORRECT' in ROWS[0][5]
          and 'NO DESK ITEM IS CLOSED' in ROWS[0][5]
          and 'NOT DURABLE' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the repair and its bound, the third re-derivation, b368 corrected with its '
          'reason, no terminal, the four prints, the pass priced with its ranking and its limit, the '
          'desk caveat, the expectations, and the scope : %s' % g1)
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
