# -*- coding: utf-8 -*-
"""b486_desk_bank.py -- THE DESK, THE ROW, THE BANK. ### **NO EXPECTATIONS ARE SCORED: NONE WERE
### REGISTERED.** ### Every figure is read from this act's own records.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
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
    span = json.loads(read(os.path.join(D, 'b486_span.json')))
    SV = json.loads(read(os.path.join(D, 'b486_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b486_results.json')))

    rec('=' * 100)
    rec('b486_desk_bank.py -- THE DESK, THE ROW, THE BANK. ### THE FOLD.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the span : ### **%d BY FILING** ### ; the tool, by NUMBER order, reads ### **%d**'
        % (SV['count'], span['current_span']))
    rec('      ### the tool`s figure counts b486 ITSELF; the filing figure is the acts filed BEFORE')
    rec('      ### it. ### **NEITHER IS WRONG AND THE TOOL IS NOT EDITED.**')
    rec('    digest clauses, all cited : ### **%d** ### ; cited from outside the span : ### **%d**'
        % (len(RES['digest']), sum(1 for d in RES['digest'] if d[2])))
    rec('    rulings in the span : ### **%d** ### (twelve in ferries, one banked otherwise)'
        % RES['rulings'])
    rec('    acts whose closing records a defect of their own : ### **%d of %d**'
        % (RES['seat'], SV['count']))
    rec('')
    rec('-' * 100)
    rec('### THE DESK AT THE FOLD.')
    rec('-' * 100)
    rec('  ### ### **b479 LEFT FIFTY-SEVEN ITEMS, FIFTY-SIX STANDING.** ### A fold does not sweep')
    rec('  ### them one by one -- ### **IT SAYS WHAT THE SPAN DID TO THE DESK** -- and the standing')
    rec('  ### items carry forward unchanged into the next span.')
    rec('')
    closed = [
        ('a gate waits on a job the record does not carry', 'b483', '(R90) struck the trigger'),
        ('a face names each tool`s write pattern, not each file', 'b483', '(R91) stem glob'),
        ('one live currency claim contradicts REGISTRY', 'b484', '(R92) executed'),
        ('the bar on the deposited records is capability, not permission', 'b485',
         '(R94) supplied the route, not a ruling'),
        ('a drafted note eighty-six acts old is written nowhere', 'b485',
         'written to ERRATA.md -- and the id collided'),
        ('the compression register, opened as a lane and empty', 'b483',
         'run, closed, NO GRADE'),
        ('an order cited across three sealed faces with no bank behind it', 'b479',
         '(R96) re-issued it'),
    ]
    rec('  ### ### **CLOSED IN THE SPAN : %d.**' % len(closed))
    for n, a, why in closed:
        rec('    %-58s %-6s %s' % (n[:58], a, why))
    rec('')
    minted = [
        ('a batch FOR block stamps one time on every line', 'b480'),
        ('a gate waits on a job the record does not carry', 'b481'),
        ('the bar is capability, not permission', 'b481'),
        ('the gate`s fifth site is not locatable at this seat', 'b481'),
        ('a priced resolving size that the arithmetic forbids', 'b483'),
        ('a bound the chain reports is not the bound it achieves', 'b483'),
        ('the seat read its own expectation backwards', 'b483'),
        ('two unrelated tests single out sqrt(17)', 'b483'),
        ('a search that can see its own report will always confirm it', 'b484'),
        ('a matcher that counts co-occurrence is not counting a claim', 'b484'),
        ('REGISTRY`s own history table disagrees with the records', 'b485'),
        ('a frozen ledger cannot be repaired without breaking its own law', 'b485'),
        ('an index-query gate fires on an arm`s own name', 'b485'),
        ('a tool that can crash after a write needs a guard before it', 'b485'),
        ('a statement posed is not a result', 'b482'),
        ('a terminal named for mathematics can state arithmetic', 'b482'),
        ('a claim can propagate across sealed faces without a carrier', 'b479'),
        ('a def and a theorem do not mean the same thing by `:=`', 'b479'),
        ('five of seven classes reach the form only through their docstrings', 'b479'),
    ]
    rec('  ### ### **MINTED IN THE SPAN : %d.**' % len(minted))
    for n, a in minted:
        rec('    %-62s %s' % (n[:62], a))
    rec('')
    rec('  ### ### **AND ONE MINTED BY THIS FOLD, ABOUT AN ACT IT FOLDS:**')
    rec('    ### **an ERRATA id was minted without checking the ledger** -- b485 appended')
    rec('    ### `E-2026-09-22-1`, which b469 had already filed under (R77). ### **TWO ENTRIES SHARE')
    rec('    ### ONE ID.** ### The fold REPORTS it and does NOT renumber it: ERRATA is append-only')
    rec('    ### and its ids are cited elsewhere. ### **ROUTED TO A RULING.**')
    rec('')
    rec('  ### ### **THE SHAPE OF THE SPAN, IN ONE LINE.** ### Eleven acts; ### **SEVEN OF THEM')
    rec('  ### RECORD A DEFECT OF THEIR OWN INSTRUMENTS** -- not of the corpus -- and every one of')
    rec('  ### those was caught by an arm, a control, or a rehearsal this record already had.')
    rec('  ### ### **THE SPAN`S MATHEMATICS MOVED LITTLE AND ITS BOOKKEEPING MOVED A GREAT DEAL.**')

    rec('')
    rec('-' * 100)
    rec('### THE EXPECTATIONS.')
    rec('-' * 100)
    rec('  ### ### **NONE REGISTERED BY THIS ACT, AND NONE INVENTED.**')

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE FOLD OF ELEVEN ACTS FILED SINCE b474, IN FILING ORDER** (b486, under (R96)). '
        '**THE SPAN, BY FILING: b475, b478, b476, b480, b477, b481, b483, b484, b485, b482, b479. '
        'ELEVEN. The span tool reads 12 by NUMBER order because it counts b486 itself and cannot '
        'place an act filed out of number order; BOTH READINGS ARE PRINTED AND THE TOOL IS NOT '
        'EDITED.** '
        '**EVERY VERDICT IN THIS FOLD IS QUOTED FROM THE ACT THAT REACHED IT. A FOLD DECIDES '
        'NOTHING NEW, and no verdict is re-scored or invented.** '
        '**THE (R31) DIGEST BLOCK, ONE DATED BLOCK, SIX CLAUSES, EACH WITH THE ACT IT IS CITED '
        'FROM. All six are said by a cited act -- checked needle by needle over EVERY banked file '
        'before the block was written. TWO REST ONLY ON ACTS OLDER THAN THE SPAN: the class '
        'boundary at a = sqrt 2 at b110, and the eight unanchored sentences at b469 from b464. The '
        'block names which.** '
        '**AND THE CHECK`S FIRST RUN WAS WRONG OVER THE WRONG POPULATION: it searched the span '
        'plus five acts and would have struck those two clauses as unsupported. A HALT PROVED OVER '
        'THE WRONG POPULATION IS NOT A HALT. The corpus was widened before anything was written or '
        'struck, and the needles` own yields are printed -- five discriminate (4 to 61 acts), five '
        'are permissive (85 to 264), and the block rests on the discriminating ones.** '
        '**THE LEDGERS. THIRTEEN rulings in the span, not twelve: (R88) is named separately '
        'because it was banked as b477_r88_standing_order.txt and a count over ferry files alone '
        'would have dropped it silently. SEVEN of the eleven acts record a defect of their OWN '
        'instruments -- not of the corpus -- and every one was caught by an arm, a control or a '
        'rehearsal this record already had.** '
        '**AND ONE FINDING THIS FOLD MAKES ABOUT AN ACT IT FOLDS: ERRATA.md carries E-2026-09-22-1 '
        'TWICE. b469 filed it under (R77); b485 appended a second entry under the same id, and '
        'b485`s suite had no arm that would have looked. THE FOLD REPORTS IT AND DOES NOT RENUMBER '
        'IT -- ERRATA is append-only and its ids are cited elsewhere, so a renumber is a ruling`s '
        'business. ROUTED.** '
        '**And one row that is not a defect of any act: the b479 closing reached the navigator '
        'TRUNCATED. That is a delivery failure, not a fault in the act -- its bank is whole on '
        'disk and its trail record is whole. A MESSAGE THAT DID NOT ARRIVE IS NOT A RECORD THAT '
        'WAS NOT MADE.** '
        'No expectations registered and none invented. Nothing compiled; no grade moved; no ERRATA '
        'line written or renumbered; row U1 unedited; the four lists OPEN; h2 where the deposit '
        'left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'nothing compiled and nothing run; every figure read from a banked file',
             ('NO CORPUS GRADE MOVED AND NO VERDICT RE-SCORED; a fold closes a span and decides '
              'nothing new'),
             ('data/b486_components.txt; data/b486_the_fold.txt; data/b486_extract.txt; '
              'data/b486_survey.json; data/b486_results.json; data/b486_desk_notes.txt; '
              'data/b486_registration_2026-09-22.txt (LOCKED at sha256 8c701ea1aea0ec7b); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    MARK = 'THE FOLD OF ELEVEN ACTS FILED SINCE b474'
    if MARK in before:
        rec('  ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER; IT IS NOT APPENDED AGAIN.**')
        code, out = 0, ['    (guard) row already present; nothing appended']
    else:
        code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    ncells = len(last.strip().strip('|').split('|'))
    rec('  READ BACK : last row %s ; cells %d' % (rowid, ncells))
    rec('  ### %s' % ('PASS' if ncells == 6 else '### FAIL'))
    rec('=' * 100)
    rec('  ### ROW %s. ### SPAN %d BY FILING, %d BY THE TOOL.'
        % (rowid, SV['count'], span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b486_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
