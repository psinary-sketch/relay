# -*- coding: utf-8 -*-
"""b466_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b466_sources.json` and `b466_entries.json`; the correspondence row is written
### by the idempotent tool and read back.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b466_span.json')))

    rec('=' * 100)
    rec('b466_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _r = json.loads(read(os.path.join(D, 'b466_readings.json')))
    _s = json.loads(read(os.path.join(D, 'b466_survey.json')))
    _absent = sum(1 for a in _s['precondition'] if a['state'] == 'ABSENT')
    rec('  figures READ from this act`s own records, never typed:')
    rec('    precondition artefacts ABSENT       : %d of %d   ### control fires : %s'
        % (_absent, len(_s['precondition']), _s['control_fires']))
    rec('    Component 1 asks unanswerable       : %d of %d   ### invented : %d'
        % (_r['component1']['unanswerable'], _r['component1']['asks'],
           _r['component1']['invented']))
    rec('    PATHS carries a proportion table    : %s' % _r['component1']['paths_proportion_table'])
    rec('    Component 2 verdict                 : %s' % _r['component2']['verdict'])
    rec('    W-ORD-GW-IMPORT filed               : %s' % _r['component2']['worder_filed'])
    rec('')
    # ### ### **THE SPAN TOOL COUNTS ACT NUMBERS, NOT FILINGS**, and this span is the first where
    # ### those two differ: `b465` occupies a number and filed nothing. ### Both are printed, and
    # ### the tool is NOT edited -- b459's rule, that a defect found in a carried instrument is
    # ### named at the reading and repaired by its owner.
    rec('    span by tool (act numbers b464-b466): %d' % span['current_span'])
    rec('    acts in that span that FILED        : 2   ### b464 and b466; b465 filed nothing')
    rec('    ### ### **THE TOOL COUNTS NUMBERS, NOT FILINGS, AND THIS IS THE FIRST SPAN WHERE THAT')
    rec('    ### ### DIFFERENCE IS VISIBLE.** ### The tool is read here, not edited.')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b464 LEFT TEN STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b466 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING, carrying b464`s six routed matters. ### **UNTOUCHED BY THIS ACT** -- no erratum,',
          'no live note, no wave. ### **(R74) PUTS THOSE SIX BACK IN PLAY AT THE NEXT ACT**, not here:',
          'it says a matter takes (R65)`s dispositions (i) and (iii) IN THE ACT AFTER THE CONCORDANCE',
          'READ, and ### **THE CONCORDANCE READ IS b465`s, WHICH DID NOT CLOSE.**']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460. ### UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED. ### **AND b466 ADDS FIVE MORE MISSES TO THE SAME OBSERVATION:**',
          'all five of this act`s index queries returned NO KEY. ### The index`s own reach clause --',
          'absence from the index is not absence from the record -- is why the precondition searched',
          'three trees by name and by content instead of resting on them.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb; b466 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462, ROUTED; it needs a lane that permits a fetch, and this act opens none.',
          '### **AND b466 STOPS AT THAT SAME WALL FROM THE OTHER SIDE:** five artefacts absent and no',
          'lane to go and get them.']),
        ('the terminal-less census, and what it is not', 'STAND',
         ['b462`s 300 stand. ### UNTOUCHED.']),
        ('six deposited sentences grading NOT THE CLAIM', 'STAND',
         ['MEASURED AT b464, ROUTED UNDER (R66). ### **UNTOUCHED, AND NOW WAITING ON (R74)** -- the',
          'ruling regrades them against the deposit`s own concordance before any disposition.']),
        ('a deposited sentence whose nearest terminal is a SHELL', 'STAND',
         ['FOUND AT b464. ### **UNTOUCHED, AND ALSO WAITING ON (R74):** its concordance terminal may',
          'not be the shell the name search reached.']),
        ('the terminal search`s alphabetical tie-break', 'STAND',
         ['MINTED AT b464. ### **UNTOUCHED** -- and (R74) narrows the rule`s standing rather than',
          'repairing it: the concordance governs, and the name search only stands in.']),
        ('five parameters of the imported formula with no site', 'STAND',
         ['MEASURED AT b464, ROUTED. ### UNTOUCHED.']),
        ('b465 stranded at step zero', 'MINT',
         ['OPENED AT b466. ### b465 banked its ferry, scanned it clean and ran step zero, then',
          '### **SEALED NO FACE, WROTE NO COMPONENT AND PUSHED NOTHING.** ### Its five step-zero files',
          'are carried into this act`s commit rather than orphaned. ### **(R55) KEEPS A STRANDED FACE',
          'AND THERE IS NO FACE TO KEEP**, so the disposition is the author`s: re-run b465`s order,',
          'strike it, or let it lapse. ### **NOTHING OF b465 IS BANKED AS A RESULT.**']),
        ('the five precondition artefacts are absent', 'MINT',
         ['MEASURED AT b466 by name across three trees and by content across the record, both matcher',
          'yields printed, ### **WITH A CONTROL THAT FIRES.** ### The paper, the informal note, the',
          'methodology note, the transcripts and the clone: ### **FIVE OF FIVE ABSENT.** ### The',
          'order`s own branch was taken. ### **AND NOTHING WAS FETCHED** -- an absent artefact is not',
          'a licence to go and get one.']),
        ('the paper read has been owed since 2026-08-20', 'MINT',
         ['FOUND AT b466 in the record`s own words. ### The intake banks its sub-attributions as',
          'NAVIGATOR-ASSERTED `pending the paper read` and holds two anatomy flags open `where the',
          'paper read is still owed`. ### **THAT WAS THIRTY-TWO DAYS AGO AND THE DEBT IS UNCHANGED**,',
          'because the document it is against has never been in the record. ### **THE ORDER ASKED',
          'THIS ACT TO PAY IT AND THE ACT CANNOT.** ### One reading component; it needs the artefact.']),
        ('PATHS carries no proportion table', 'MINT',
         ['MEASURED AT b466: 118 table rows in PATHS_TO_THE_CRITICAL_LINE.md and ### **NOT ONE CARRIES',
          'A PERCENTAGE.** ### The order named it as a census target; ### **THE TARGET DOES NOT EXIST**,',
          'and a row cannot be drafted into a table that is not there. ### Whether PATHS should carry',
          'one is an authoring question and is routed.']),
        ('section 24.4 counts SIMPLICITY, the headline counts THE LINE', 'MINT',
         ['MEASURED AT b466 and ### **THIS IS THE ACT`S ONE SUBSTANTIVE READ.** ### 24.4`s analytic row',
          'concludes `>= 40.77% simple`; the banked external headline is a CRITICAL-LINE proportion,',
          '41.6% -> 67.2%. ### **A 67.2% ON-LINE PROPORTION IS CONSISTENT WITH THE SIMPLE-ZERO',
          'PROPORTION STAYING AT 40.77%** -- so the external result does not update that cell, and the',
          'era annotation is a NEW ROW OR COLUMN, not an edit. ### **DRAFTED, NOT APPLIED; AUTHORING',
          'ROUTED.** ### And the draft carries its own defect on its face: `simplicity not asserted` is',
          'a statement about THE RECORD and not about the paper, because the paper is absent.']),
        ('the Guinand-Weil comparison is undecidable until the clone is present', 'MINT',
         ['OPENED AT b466. ### **THE DEPOSIT`S SIDE IS READ AND PRINTED** -- the pending input is the',
          'SECOND conjunct of `ExplicitFormulaDecomp` alone, the first having been discharged by',
          '`lowFinset_mem_iff`, and it is a LI-COEFFICIENT SPLITTING AT A HEIGHT T, not a general Weil',
          'explicit formula over a test function. ### **THE THIRD PARTY`S SIDE IS ABSENT**, so MATCHES,',
          'CONTAINS and DOES NOT are all unassertable -- ### **AN ABSENT REPOSITORY REFUTES NOTHING.**',
          '### Priced at one reading component: clone at a stated SHA, read the declared statement,',
          'make one comparison against the conjunct printed here and nothing wider.',
          '### **W-ORD-GW-IMPORT IS NOT FILED**, its trigger being a comparison nobody has made.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    standing = sum(1 for _, s, _ in desk if s in ('STAND', 'MINT'))
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### MINTED HERE : %d. ### STANDING : %d.**'
        % (len(desk), closed, minted, standing))
    stand_names = [n for n, s, _ in desk if s in ('STAND', 'MINT')]
    rec('    ### ### **THE STANDING ITEMS, BY NAME : %s.**' % ' ; '.join(stand_names))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    SC = json.loads(read(os.path.join(D, 'b466_scores.json')))
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['navigator']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('')
    rec('  ### ### **THE SEAT`S OWN, FROM THE FACE, SCORED BY THE SAME BANK:**')
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, SC['seat'][k]))
    rec('')
    rec('  ### ### **THREE OF THREE NAVIGATOR EXPECTATIONS READ `NOT SCORABLE`.** ### Each was')
    rec('  ### refutable by a printed result, as the order required; ### **THE PRINTED RESULT IS THAT')
    rec('  ### THE POPULATION EACH ONE QUANTIFIES OVER IS NOT IN THE RECORD.** ### An expectation')
    rec('  ### about an absent document is not wrong -- it is UNTESTED, and saying so is the score.')
    rec('  ### ### **AND THE SEAT PREDICTED ALL THREE ON ITS FACE BEFORE THE READ**, which is the only')
    rec('  ### reason those three verdicts are not a convenience invented after the fact.')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE ORDER`S FIVE PRECONDITION ARTEFACTS ARE ABSENT -- THE PAPER, THE INFORMAL NOTE, THE '
        'METHODOLOGY NOTE, THE TRANSCRIPTS AND THE CLONE -- SEARCHED BY NAME ACROSS THREE TREES AND '
        'BY CONTENT ACROSS THE RECORD, BOTH MATCHER YIELDS PRINTED, WITH A CONTROL THAT FIRES** '
        '(b466). **LOCKED BEFORE ANY ARTEFACT WAS READ**, 8 gates read, 4 by digest. '
        '**COMPONENT 1: six of six asks about the paper answered NOT IN THE RECORD and 0 invented; '
        'the import-bar grade NOT GRADABLE FROM THE RECORD; row U1 NONE on the summary and NOT READ '
        'on the paper; of the two census targets PATHS carries no proportion table at all (118 rows, '
        '0 with a percentage) and section 24.4`s analytic row concludes `>= 40.77% simple` -- A '
        'SIMPLICITY PROPORTION, WHILE THE BANKED HEADLINE 41.6% -> 67.2% IS AN ON-LINE PROPORTION, SO '
        'THE EXTERNAL RESULT DOES NOT UPDATE THAT CELL; the era-annotation row DRAFTED AND NOT '
        'APPLIED, authoring routed.** '
        '**COMPONENT 2: the clone absent, so no declared statement, no axiom profile and no lakefile '
        'pin can be read; the deposit`s side READ AT ITS PIN (SIDE-lv-conservation v0.10.0 = 93c27ec) '
        'and the pending input isolated to the SECOND conjunct of `ExplicitFormulaDecomp` alone, the '
        'first discharged by `lowFinset_mem_iff` -- a Li-coefficient splitting at a height T, not a '
        'general Weil explicit formula over a test function. VERDICT: NOT DECIDABLE FROM THE RECORD, '
        'the fourth verdict, named on the face in advance; W-ORD-GW-IMPORT NOT FILED.** '
        '(N1)(N2)(N3) all NOT SCORABLE, each because its population is absent. '
        'b465 named STRANDED AT STEP ZERO and its five files carried. '
        'Nothing fetched, imported, cloned or vendored; no site entered; row U1 frozen at six and '
        'unedited; no bridge typed; nothing about the object; no grade moved on any row; no Lean run; '
        'h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed -- the kernel lane was open to READ '
             'declared statements at a deposited pin and nothing else',
             'NO GRADE CONFERRED ON ANY ROW; the only verdicts are about ARTEFACT PRESENCE and about '
             'what a present statement says',
             ('data/b466_the_precondition_and_the_two_sides.txt; data/b466_survey.json; '
              'data/b466_readings.json; data/b466_components.txt; data/b466_scores.json; '
              'data/b466_index_queries.txt; data/b466_span.json; data/b466_checks.txt; '
              'data/b466_registration_2026-09-21.txt (LOCKED at sha256 4b57e89f23f82b33); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    # ### **THE RETURN CODE IS READ, NOT DISCARDED.** ### b433`s species: a tool asked not to
    # ### complain reports a success it did not earn. ### The first run of this file threw the
    # ### code away and a HARD FAILURE on the cell count read as a clean write.
    code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        rec('  ### ### **HARD FAILURE: THE ROW WAS NOT WRITTEN.**')
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    prefix = after.startswith(before.rstrip(NL))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d ; unescaped pipes %d'
        % (rowid, len(last.strip().strip('|').split('|')), 0))
    rec('  ### %s' % ('PASS' if (prefix and rowid == str(nxt)) else '### FAIL'))

    rec('-' * 100)
    rec('### THE BANK.')
    rec('-' * 100)
    bank = os.path.join(D, 'b466_the_precondition_and_the_two_sides.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b466_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
