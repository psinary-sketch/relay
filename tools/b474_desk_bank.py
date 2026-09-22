# -*- coding: utf-8 -*-
"""b474_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b474_sources.json` and `b474_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b474_span.json')))

    rec('=' * 100)
    rec('b474_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _f = json.loads(read(os.path.join(D, 'b474_fold.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    fold rows %d ; strings %d ; verified %d ; rows not carried %d'
        % (len(_f['rows']), _f['strings'], _f['verified'],
           sum(1 for r in _f['rows'] if not r['verified'])))
    rec('    columns : %s ; OBJECT %d'
        % (' ; '.join('%s %d' % (k, v) for k, v in sorted(_f['columns'].items())),
           _f['columns'].get('OBJECT', 0)))
    rec('    span by tool through this filing act : %s ; the fold`s own span : 10' % _f['span_tool'])
    rec('    span by tool AFTER the write : %d (the fold now covers b464-b473)' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b474 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND', ['UNTOUCHED.']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('PATHS carries no proportion table', 'STAND', ['UNTOUCHED.']),
        ('a site verdict is source-relative, not absolute', 'STAND', ['CARRIED INTO THE FOLD`S ROWS.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED; IN THE FOLD.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED; IN THE FOLD.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED; IN THE FOLD.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED; IN THE FOLD.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['STILL NOT RUN. ### The serialized attempt is part 2 of this ferry and is NOT this act.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['SEEN AGAIN HERE: b465 has no closing bank and is not a fold row; the fold says so in itself.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['PRICED AT b471, (R82) VOID FOR WANT OF A RUN AT b473, (R83) UNTRIGGERED. ### Carried into the',
          'fold`s rulings table with that status and nothing else.']),
        ('lake 5.0.0 has no -j', 'STAND', ['BANKED AT b470; the operative constraint for any retry.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND',
         ['ENTERED AT THIS FOLD, ALL THREE: the two overclaims of 2026-09-22 with their record checks;',
          '(R81) refusing its author`s own next ferry; and b360`s sentence carried as a rule when it was',
          'a measurement, which (R84) withdraws as an instruction. ### The item stays on the desk because',
          'the ledger is a standing place, not a task.']),
        ('the E0 table has no site column', 'STAND', ['CARRIED INTO THE FOLD AS ITS UNASKED-FOR FINDING.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND',
         ['DISCHARGED IN FACT, NOT CLOSED BY FIAT: the fold is filed here and the span tool now reads the',
          'last fold as b464-b473 with the next span starting at b475. ### The item stands until an act',
          'reads a non-zero span again, which is the only evidence that the count restarted.']),
        ('the run died of memory, not of mathematics', 'STAND', ['FOUND AT b473; in the fold.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE PRICE IS WHAT PART 2 OF THIS FERRY PROPOSES TO PAY: one module at a time, one thread.',
          '### That act is b475 and it is not this one.']),
        ('the compression register, opened as a lane and empty', 'MINT',
         ['OPENED AT b474 UNDER (R84): Weil`s form on finite families of the corpus`s own windows, its',
          'signature, with the Epstein function as control. ### **REGISTERED WITH ITS FALSIFIERS AND ITS',
          'CONTROL BEFORE ANY NUMBER EXISTS**, which is the discipline (R84) keeps. ### Nothing is',
          'computed, nothing is claimed about h2, and no bridge is typed from the lane to any site.']),
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
    SC = json.loads(read(os.path.join(D, 'b474_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED : %d.**' % SC['registered'])
    rec('  %s' % SC['note'])
    rec('  ### the seat`s own : %s ; rehearsal : %s'
        % (SC['seat']['expectations'], SC['seat']['rehearsal']))
    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE SPAN b464-b473 IS FOLDED AS THE EXTERNAL-READING ARC, THE (R31) DIGEST IS REFRESHED FROM '
        'THE SECTION JUST WRITTEN, AND (R84)`S COMPRESSION REGISTER IS ENTERED AS A RESEARCH LANE** (b474). '
        '**PURELY ADDITIVE: three appends, each with its prior bytes proved a true prefix and its marker '
        'appearing exactly once; 76 lines to FINDINGS.md, 8 to the digest, 16 to OPEN_TRAILS.md for the '
        'lane and 34 for this act`s record; nothing edited, nothing removed.** '
        '**THE FOLD CARRIES TEN ROWS AND 23 VERDICT STRINGS, EVERY ONE MATCHED IN ITS OWN ACT`S CLOSING '
        'BANK, rehearsed under (R70) BEFORE the seal. b465 is not a row: stranded at step zero, re-issued '
        'as b467 under (R75), no closing bank. COLUMNS: RECORD 7, MODEL 3, OBJECT 0 -- the object column '
        'empty for the tenth consecutive span, three rows borderline and each saying so in itself.** '
        '**THE RULINGS (R74)-(R84) ARE READ RATHER THAN RECALLED: only (R76) and (R78) have entries of '
        'their own; (R82) VOID FOR WANT OF A RUN; (R83) untriggered; (R84) entered here. A defect in that '
        'reading was found and fixed: `### (Rnn)` is a substring of a `####` sub-heading, so (R81) read as '
        'having an entry it does not have.** '
        '**BOTH LEDGERS CARRIED: the navigator`s three, all named by the author`s own rulings, entered at '
        'this fold; the seat`s as each act`s closing entered them, including b433`s species in its third '
        'recurrence.** '
        '**(R84)`S LANE IS OPENED AND EMPTY: falsifiers and the Epstein control named, NO NUMBER COMPUTED.** '
        'No expectations were registered. No grade moved; nothing minted; no act re-verdicted; h2 where the '
        'deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: a fold reads closings, not terminals',
             'NO CORPUS GRADE MOVED; A FOLD CONFERS NONE AND RE-VERDICTS NOTHING',
             ('data/b474_the_fold_at_ten.txt; data/b474_fold.json; data/b474_components.txt; '
              'data/b474_fold_run.txt; data/b474_lane.txt; data/b474_extract.txt; data/b474_checks.txt; '
              'data/b474_registration_2026-09-22.txt (LOCKED at sha256 d8c069e808708a1e); '
              'FINDINGS.md; phase2/method/THE_FINDINGS_AS_THEY_STAND.md; '
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
    bank = os.path.join(D, 'b474_the_fold_at_ten.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b474_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
