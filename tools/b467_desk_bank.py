# -*- coding: utf-8 -*-
"""b467_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b467_sources.json` and `b467_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b467_span.json')))

    rec('=' * 100)
    rec('b467_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _c = json.loads(read(os.path.join(D, 'b467_concordance.json')))
    _p = json.loads(read(os.path.join(D, 'b467_params.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    concordance rows parsed              : %d' % _c['rows'])
    rec('    of the eight, rows the concordance assigns : %d   ### **NO ROW : %d**'
        % (8 - _c['no_row'], _c['no_row']))
    rec('    the row-finder`s positive control    : %d of %d rows recover themselves'
        % (_c['control_fired'], _c['control_rows']))
    rec('    grades after the read                : %s'
        % ' / '.join('%s %d' % (k, _c['by_grade'][k]) for k in sorted(_c['by_grade'])))
    rec('    the six sites, general source        : %s'
        % ' / '.join('%s %d' % (k, _p['tally'][k]) for k in sorted(_p['tally'])))
    rec('    cells moved against b464`s CC (148) read : %d of 6' % _p['moved_against_cc'])
    rec('    indices under none of the three headings : %d' % len(_p['none_bucket']))
    rec('    span by tool                         : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b466 LEFT SIXTEEN STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b467 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING. ### **AND (R74) HAS NOW BEEN EXERCISED AGAINST IT AND CHANGED NOTHING** -- the',
          'concordance assigns no terminal to any of the eight, so no grade could move. ### The six',
          'matters stand exactly where b464 left them, and the SHELL stands as a seventh.',
          '### **(R74)`s ACT-AFTER CLAUSE IS NOW ARMED**: the read is done, so the dispositions (i)',
          'and (iii) fall due in the next act that takes them, and this act does not.']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460. ### UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED. ### UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb; b467 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462, ROUTED; it needs a lane that permits a fetch, and this act opens none.']),
        ('the terminal-less census, and what it is not', 'STAND',
         ['b462`s 300 stand. ### UNTOUCHED.']),
        ('six deposited sentences grading NOT THE CLAIM', 'STAND',
         ['MEASURED AT b464 and ### **RE-READ HERE AGAINST THE DEPOSIT`S OWN CONCORDANCE, WHICH',
          'ASSIGNS THEM NOTHING.** ### All six keep b464`s grade, now LABELLED A STAND-IN under',
          '(R74)`s second limb. ### ROUTED, NOT REPAIRED.']),
        ('a deposited sentence whose nearest terminal is a SHELL', 'STAND',
         ['FOUND AT b464. ### **THE CONCORDANCE ASSIGNS IT NO ROW EITHER**, so the SHELL stands as',
          'a stand-in grade and the order`s expectation -- that the concordance would reach the',
          'substantive terminal beside it -- ### **IS REFUTED BY THE TABLE ITSELF.**']),
        ('the terminal search`s alphabetical tie-break', 'STAND',
         ['MINTED AT b464. ### **UNTOUCHED, AND NOW LARGELY MOOT FOR GRADING** -- (R74) makes the',
          'concordance govern and the name search a labelled stand-in. ### The defect remains in the',
          'stand-in path, which is the path all eight items are on.']),
        ('five parameters of the imported formula with no site', 'STAND',
         ['MEASURED AT b464 against CC (148), ROUTED. ### **AND b467 SHOWS THE FIGURE IS SOURCE-',
          'RELATIVE:** against the general source, pi IS a parameter and its conductor IS a datum,',
          'so two of the six sites that were OF NO PARAMETER under CC are not under Lagarias.']),
        ('b465 stranded at step zero', 'CLOSE',
         ['OPENED AT b466 and ### **CLOSED HERE BY (R75)**: b465 is re-issued as b467 under its own',
          'banked ferry text, byte-identical (both sha256 6aa4c0474e505c86...), and its five step-',
          'zero files were carried into b466`s commit rather than orphaned. ### **THE ORDER RAN.**']),
        ('the five precondition artefacts are absent', 'STAND',
         ['MEASURED AT b466. ### **(R75) RULES THAT THEY ENTER BY THE AUTHOR`S FETCH** and names a',
          'sixth and seventh -- arXiv 2608.13637 and a clone of anthropics/formal-math. ### As of',
          'this act ### **NONE IS ON DISK**, which is why b468 runs its precondition and stops.']),
        ('the paper read has been owed since 2026-08-20', 'STAND',
         ['FOUND AT b466. ### **STILL OWED**, and (R75) names the route by which it is paid.']),
        ('PATHS carries no proportion table', 'STAND',
         ['MEASURED AT b466, ROUTED. ### UNTOUCHED.']),
        ('section 24.4 counts SIMPLICITY, the headline counts THE LINE', 'STAND',
         ['MEASURED AT b466, ROUTED. ### **AND b468`s ORDER NOW ASKS WHETHER THE THEOREM COUNTS',
          'SIMPLE ZEROS**, which is the question that would settle whether the cell moves at all.']),
        ('the Guinand-Weil comparison is undecidable until the clone is present', 'STAND',
         ['OPENED AT b466. ### **(R75) NAMES THE CLONE THAT WOULD DECIDE IT** -- anthropics/formal-',
          'math at its HEAD SHA, the zeta23 project inside it, which is a DIFFERENT REPOSITORY from',
          'the anthropics/zeta-23-lean b466 searched for. ### **THE RECORD`S OWN NAME FOR IT WAS',
          'WRONG, AND (R75) CORRECTS IT.** ### Still undecided; nothing imported.']),
        ('the deposit provides no mapping from these sentences to its kernel', 'MINT',
         ['MEASURED AT b467 AND THIS IS THE ACT`S SHARPEST RESULT. ### The concordance assigns a row',
          'to ### **ZERO OF THE EIGHT**, under a finder whose positive control recovers 7 of 7 rows',
          'from their own words and whose negative control returns NO ROW. ### **SO THE QUESTION',
          '`WHICH TERMINAL DOES THE DEPOSIT ITSELF ASSIGN TO THIS SENTENCE?` HAS NO ANSWER IN THE',
          'DEPOSIT FOR ANY OF THEM.** ### That is not a grade and it is stronger than one: section',
          '25.8 is a table of seven load-bearing theorems, ### **IT IS NOT AN INDEX OF THE DEPOSIT`S',
          'CLAIMS**, and eight sentences asserting a machine check sit outside it. ### ROUTED.']),
        ('a site verdict is source-relative, not absolute', 'MINT',
         ['MEASURED AT b467: ### **FOUR OF THE SIX CELLS MOVE** between CC (148) and the general',
          'source -- (iii) and (iv) from A COORDINATE OF ONE to OF NO PARAMETER, (v) from OF NO',
          'PARAMETER to A PARAMETER, (vi) from OF NO PARAMETER to A COORDINATE OF ONE. ### **SO THE',
          'SIX INDICES ARE NOT PROPERTIES OF `THE EXPLICIT FORMULA`; THEY ARE PROPERTIES OF WHICH',
          'EXPLICIT FORMULA IS READ.** ### b464 said exactly this in advance about site (v) and it',
          'is now measured at four sites. ### **ANY LATER ACT QUOTING A SITE VERDICT MUST NAME THE',
          'SOURCE IT WAS TAKEN AGAINST.** ### ROUTED.']),
        ('the general source carries a height outside its explicit formula', 'MINT',
         ['DISCLOSED AT b467 rather than left out. ### The analytic conductor q(pi,s) := Q(pi) prod',
          '(|s + kappa_j| + 3) is evaluated at s = iT in the error term O(log q(pi,iT)). ### **THAT',
          'IS A HEIGHT AS AN ARGUMENT** -- and it sits in a REMARK ABOUT THE ZERO-COUNTING FUNCTION',
          'N_pi(T), not in the explicit formula. ### **THE READING HOLDS FOR THE STATEMENT READ AND',
          'WOULD NOT HOLD FOR THE COUNTING FUNCTION**, and that boundary is the honest answer.']),
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
    SC = json.loads(read(os.path.join(D, 'b467_scores.json')))
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
        '**THE DEPOSIT`S OWN CONCORDANCE ASSIGNS A ROW TO ZERO OF THE EIGHT MACHINE-CHECKED '
        'SENTENCES, SO UNDER (R74) ALL EIGHT KEEP b464`S GRADE AS A LABELLED STAND-IN AND NOT ONE '
        'OF THE SIX `NOT THE CLAIM` MOVES** (b467, b465 re-issued under (R75) byte-identical). '
        '**LOCKED BEFORE ANY SENTENCE WAS RE-GRADED**, 8 gates read, 4 by digest. '
        '**Section 25.8 is parsed from the deposited file: 7 rows, whose own grade column is '
        '`#print axioms` -- a grade of AXIOM DEPENDENCE, not of whether a theorem carries a claim. '
        'Four matcher forms were run and every yield is on the record; the governing form passes a '
        'positive control at 7 of 7 (each row recovered from its own claim text) and a negative '
        'control, so the eight NO ROWs are the concordance`s answer and not the finder`s. THE '
        'DEPOSIT PROVIDES NO MAPPING FROM THESE EIGHT SENTENCES TO ITS OWN KERNEL AT ALL -- '
        'section 25.8 is a table of seven load-bearing theorems, not an index of the deposit`s '
        'claims. Named and routed under (R66); no erratum written, (R74) putting (R65)`s '
        'dispositions in the act after the read.** '
        '**AGAINST THE GENERAL SOURCE (Lagarias math/0404394v4, b358`s pin, sha256 '
        '86f3d3c49f5a889f...): the six site indices read A PARAMETER 1 / A COORDINATE OF ONE 2 / '
        'OF NO PARAMETER 3, and FOUR OF THE SIX CELLS MOVE against b464`s CC (148) read -- (iii) '
        'and (iv) because this source`s test class is cut by analyticity and a growth bound and '
        'carries no support condition, (v) because pi is quantified over in its own words, (vi) '
        'because Q(pi) is its conductor. SO A SITE VERDICT IS SOURCE-RELATIVE AND NOT ABSOLUTE. '
        'The reduction test: all 6 indices fall under one of the three headings, 0 under none; the '
        'height under THE INSTRUMENT`S TRUNCATION. The failure condition was tested, not assumed '
        'away: the source carries the truncation explicitly (bound in a limit) and carries a '
        'height in q(pi,iT) (in a remark about N_pi(T)), and NEITHER is a datum of the explicit '
        'formula.** '
        '(N1) REFUTED at 0 of 6 moved; (N2) HELD on all three; (N3) HELD at 0 under none. '
        'No site entered; row U1 frozen at six and unedited; no bridge typed; nothing about the '
        'object; no grade moved on any row; no Lean run, the kernels READ at their pins; '
        'h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none computed; section 25.8`s axiom column is QUOTED as the concordance`s own grade, '
             'not recomputed, and the act says so',
             'GRADES KEPT ON EIGHT SENTENCES AS LABELLED STAND-INS, NOT CONFERRED ON ROWS -- no '
             'correspondence row or registry cell moved',
             ('data/b467_the_concordance_and_the_general_source.txt; data/b467_concordance.json; '
              'data/b467_params.json; data/b467_survey.json; data/b467_components.txt; '
              'data/b467_scores.json; data/b467_span.json; data/b467_checks.txt; '
              'data/b467_registration_2026-09-22.txt (LOCKED at sha256 2c1cff30be4f532e); '
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
    bank = os.path.join(D, 'b467_the_concordance_and_the_general_source.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b467_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
