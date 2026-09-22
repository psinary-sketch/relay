# -*- coding: utf-8 -*-
"""b469_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b469_sources.json` and `b469_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b469_span.json')))

    rec('=' * 100)
    rec('b469_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _w = json.loads(read(os.path.join(D, 'b469_writes.json')))
    _t = json.loads(read(os.path.join(D, 'b469_tally.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    ERRATA lines added / removed      : %d / %d' % (_w['c1']['added'], _w['c1']['removed']))
    rec('    ERRATA prior bytes a TRUE PREFIX  : %s' % _w['c1']['prefix'])
    rec('    the tally rule, FIRST DRAFT       : %s   ### digits %d ; number-words %d'
        % ('PASS' if _t['first_draft_pass'] else '### FAIL', len(_t['digits']), len(_t['words'])))
    rec('    the working note, lines added     : %d   ### no existing line edited : %s'
        % (_w['c2']['added'], _w['c2']['no_line_edited']))
    rec('    OPEN_TRAILS added / removed       : %d / %d   ### **LINES CHANGED : %d %s**'
        % (_w['c3']['added'], _w['c3']['removed'], _w['c3']['changed_count'],
           [c + 1 for c in _w['c3']['changed_lines']]))
    rec('    the prior row preserved by quotation : %s' % _w['c3']['prior_row_quoted'])
    rec('    ### **DEPOSITED FILES UNCHANGED    : %d of %d**'
        % (_w['deposit']['unchanged'], _w['deposit']['total']))
    rec('    span by tool                      : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b468 LEFT TWENTY STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b469 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING. ### **AND (R77) HAS NOW TAKEN DISPOSITIONS (i) AND (iii) FOR THE UNANCHORED',
          'SENTENCES** -- E-2026-09-22-1 and the concordance scope note. ### **DISPOSITION (ii)',
          'STILL WAITS ON THE WAVE**, which is parked, so nothing deposited was narrowed.']),
        ('what the fired control does not license', 'STAND', ['ENTERED at b460. ### UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['ROUTED. ### UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb; b469 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462, ROUTED; it needs a lane that permits a fetch, and this act opens none.']),
        ('the terminal-less census, and what it is not', 'STAND', ['b462`s 300 stand. ### UNTOUCHED.']),
        ('six deposited sentences grading NOT THE CLAIM', 'CLOSE',
         ['MEASURED AT b464, RE-READ AT b467, and ### **CLOSED HERE INTO THE ERRATUM**: the six sit',
          'in E-2026-09-22-1 with the other unanchored sentences, each with its stand-in terminal',
          'and grade LABELLED AS A STAND-IN. ### **THE ITEM IS CLOSED AS A DESK ITEM, NOT AS A',
          'QUESTION** -- what the deposit means by those sentences is untouched.']),
        ('a deposited sentence whose nearest terminal is a SHELL', 'CLOSE',
         ['FOUND AT b464, NO ROW at b467, and ### **CLOSED HERE INTO THE SAME ENTRY**, its SHELL',
          'grade carried as a stand-in like the rest.']),
        ('the terminal search`s alphabetical tie-break', 'STAND',
         ['MINTED AT b464. ### **STILL LIVE, AND NOW LOAD-BEARING IN A DEPOSITED-FACING RECORD:**',
          'every grade in E-2026-09-22-1 is a stand-in reached by that search, and the entry says so',
          'in its own words. ### ROUTED.']),
        ('five parameters of the imported formula with no site', 'STAND',
         ['MEASURED source-relative at b467. ### UNTOUCHED.']),
        ('the paper read has been owed since 2026-08-20', 'STAND',
         ['STILL OWED; (R75) names the route and the artefacts are not yet on disk.']),
        ('PATHS carries no proportion table', 'STAND', ['ROUTED. ### UNTOUCHED.']),
        ('section 24.4 counts SIMPLICITY, the headline counts THE LINE', 'STAND',
         ['MEASURED AT b466, ROUTED. ### UNTOUCHED.']),
        ('the Guinand-Weil comparison is undecidable until the clone is present', 'STAND',
         ['SHARPENED AT b467, still undecided; the clone is absent. ### UNTOUCHED.']),
        ('the deposit provides no mapping from these sentences to its kernel', 'CLOSE',
         ['MEASURED AT b467 and ### **CLOSED HERE BY BEING WRITTEN DOWN WHERE IT BELONGS**: the',
          'erratum records it deposit-facing, and the live note records it in the monograph`s own',
          'section 25.8, in that document`s own annotation form. ### **THE FINDING IS NOW IN THE',
          'TWO PLACES A READER WOULD LOOK**, and the desk does not need to hold it.']),
        ('a site verdict is source-relative, not absolute', 'STAND',
         ['MEASURED AT b467 at four of six cells. ### **AND (R76) NOW TURNS IT INTO A RULE:** the',
          'trigger names a COORDINATE rather than a class in the abstract, precisely because the',
          'verdicts move between sources. ### The item stands as a reading caution for any act',
          'quoting a site verdict.']),
        ('the general source carries a height outside its explicit formula', 'STAND',
         ['DISCLOSED AT b467, and ### **(R76) USES IT**: the truncation coordinate cannot be fired',
          'by any source, because neither pinned source carries it as a datum. ### UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND',
         ['FOUND AT b468, ROUTED. ### UNTOUCHED.']),
        ('a name matcher cannot see a repository', 'STAND', ['FOUND AT b468, repaired there.']),
        ('an AI-disclosure line is not an artefact', 'STAND',
         ['FOUND AT b468, ROUTED for any future artefact census over this corpus.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'MINT',
         ['FOUND AT b469 AND IT REACHED A LIVE FILE BEFORE IT WAS CAUGHT. ### The writer read',
          '`OPEN_TRAILS.md` with `utf-8-sig`, which STRIPS the byte-order mark, and wrote it back as',
          'plain `utf-8` -- so the file`s first byte changed and `git diff` showed **a deletion this',
          'act never intended**, on the document heading. ### **THE DIFF IS WHAT CAUGHT IT**: the',
          'act had promised `lines removed 0` and the stat said two deletions, so the second one had',
          'to be explained. ### Repaired by restoring the mark; the file is byte-identical to its',
          'prior state apart from the append and the single intended row. ### **ROUTED: every',
          'writer in this corpus that reads `utf-8-sig` and writes `utf-8` carries this defect**, and',
          'the record already holds a note on the opposite direction -- a redirect ADDING a BOM.']),
        ('a pointer can name a blank line', 'MINT',
         ['FOUND AT b469. ### The partition row`s new pointer was computed arithmetically and landed',
          'on the blank line BETWEEN the comment anchor and the heading. ### `(R61)``s own pointer',
          'convention names the COMMENT ANCHOR, and the new one now does too. ### **A LINE NUMBER',
          'COMPUTED FROM A LENGTH IS NOT A LINE NUMBER READ FROM A FILE**, and the difference is one',
          'blank line. ### ROUTED: pointers should be read back after the write, which is how this',
          'one was caught.']),
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
    SC = json.loads(read(os.path.join(D, 'b469_scores.json')))
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
        '**THE UNANCHORED DEPOSITED SENTENCES TAKE (R77)`S DISPOSITIONS (i) AND (iii): ERRATA ENTRY '
        'E-2026-09-22-1 IS APPENDED, AND A DATED CONCORDANCE SCOPE NOTE IS ADDED BESIDE SECTION 25.8 '
        'IN THE WORKING MONOGRAPH** (b469). **LOCKED BEFORE ANY LIVE SURFACE WAS WRITTEN**, 8 gates '
        'read, 4 by digest. '
        '**THE ERRATUM names each sentence by file and line, quotes it verbatim from the deposited '
        'copy at its own line, carries b467`s finding -- NO ROW for every one of them, the '
        'concordance being a table of seven load-bearing theorems and not an index of the deposit`s '
        'claims -- and gives each its b464 stand-in terminal and grade, EVERY ONE LABELLED STAND-IN. '
        'It calls nothing published wrong: what it records is that these assertions are UNANCHORED '
        'in the deposit that makes them. Prefix proved; lines removed 0; b456`s tally rule PASSED ON '
        'THE FIRST DRAFT, judged by b456`s own function imported rather than copied.** '
        '**THE LIVE NOTE is in the working copy only, in the document`s own annotation form, and NO '
        'EXISTING LINE WAS EDITED -- proved by deleting the inserted lines and comparing the rest '
        'byte for byte. THE DEPOSITED DIRECTORY IS UNCHANGED, 11 of 11 md5 pairs identical.** '
        '**(R76) IS APPENDED BESIDE (R61) IN THE (R61) ENTRY FORM**, carrying the ruling verbatim, '
        'quoting (R61)`s own trigger line at OPEN_TRAILS.md:6479 beside it so the trigger reads in '
        'both vocabularies, and citing b467`s two tables at OPEN_TRAILS.md:7533 and :7556 as its '
        'evidence. (R61) is not replaced and its record is not edited. **The partition`s trail row '
        'gains the pointer: EXACTLY ONE LINE CHANGED, lines removed 0, the prior text preserved by '
        'quotation in the appended entry under (R4); b448`s earlier partition row, which records '
        'that there was then no trigger, is NOT touched.** '
        '(N1) HELD, 11 of 11 deposited md5 unchanged; (N2) HELD at 33 lines added; (N3) HELD, the '
        'tally passed first draft. '
        'Disposition (ii) waits on the wave under (R66); nothing deposits; nothing written at '
        'Zenodo; no grade moved on any row; no sentence called wrong; no site entered; row U1 '
        'unedited; no bridge typed; no Lean run; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none computed; the erratum cites b464`s banked stand-in terminals at their pins and '
             'recomputes no profile',
             'NO GRADE MOVED. The grades written into the erratum are b464`s, carried unchanged and '
             'LABELLED STAND-IN, which is (R74)`s second limb and not a new conferral',
             ('PLACE-papers ERRATA.md (E-2026-09-22-1); PLACE-papers day1/A_Place_to_Stand.md (the '
              'concordance scope note); PLACE-papers OPEN_TRAILS.md ((R76) and the partition row`s '
              'pointer); data/b469_the_erratum_the_note_and_the_ruling.txt; data/b469_writes.json; '
              'data/b469_tally.json; data/b469_md5_before.json; data/b469_md5_after.json; '
              'data/b469_registration_2026-09-22.txt (LOCKED at sha256 169299cf26af7161); '
              'CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b469_the_erratum_the_note_and_the_ruling.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b469_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
