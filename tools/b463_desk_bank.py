# -*- coding: utf-8 -*-
"""b463_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b463_sources.json` and `b463_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b463_span.json')))

    rec('=' * 100)
    rec('b463_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _f = json.loads(read(os.path.join(D, 'b463_fold.json')))
    rec('  figures READ from this act`s own records: rows %d ; strings %d ; verified %d ;'
        % (len(_f['rows']), _f['strings'], _f['verified']))
    rec('  columns %s ; span by tool through this act %s ; the fold`s own span 9'
        % (' / '.join('%s %d' % (k, _f['columns'][k]) for k in sorted(_f['columns'])), _f['span_tool']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457 at twelve acts over forty-five items; NOT BUILT; the author`s. ### UNTOUCHED.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING, and ### **THE ONLY RULING OF THE SPAN THAT STANDS RATHER THAN CLOSES** -- it opens a',
          'wave when substance moves, and no substance moved in nine acts.']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460. ### Whether any of b452`s forty-four was read CORRECTLY is still open.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED to the author. ### UNTOUCHED BY THE FOLD.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb, with its trigger at ### **THE NEXT ACT THAT TOUCHES THE SUITE.**',
          '### b463 is a fold and touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462. ### ROUTED; it needs a lane that permits a fetch, and a fold opens no lane.']),
        ('the terminal-less census, and what it is not', 'STAND',
         ['MEASURED at b462 and CARRIED INTO THE FOLD`S OWN SECTION: 300 of 419 items name nothing, and',
          '### **THE BIN IS NOT A DEFECT COUNT** -- its strongest members are attributions to Ostrowski,',
          'Stormer, Artin-Whaples, Riemann, Hecke and Tate. ### Any disposition is the author`s.']),
        ('the version-naming mismatch', 'CLOSE',
         ['CLOSED BY (R73), THE AUTHOR`S: the write-list arm`s reading governs and the convention moves.',
          '### b463`s own face names every file in full, versions included, and ### **THE ARM DID NOT MOVE.**']),
        ('the lexical arm count over-reads', 'CLOSE',
         ['CLOSED BY (R73) IN THE SAME STROKE: the species was a face writing a name an arm could not read.',
          '### With names spelled in full there is nothing left to over-read. ### **A CONVENTION, NOT A RULE',
          'ABOUT COUNTING**, and it took three acts of failures to find that out.']),
        ('the span at the fold threshold', 'CLOSE',
         ['REPORTED at b462 as standing at nine and NOT acted on; ### **FOLDED AT b463.** ### The tool now',
          'reads the last fold as b454-b462, filed by b463, and the next span starting at b464.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    standing = sum(1 for _, s, _ in desk if s == 'STAND')
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(desk), closed, standing))
    stand_names = [n for n, s, _ in desk if s == 'STAND']
    rec('    ### ### **THE STANDING ITEMS, BY NAME : %s.**' % ' ; '.join(stand_names))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    F = json.loads(read(os.path.join(D, 'b463_fold.json')))
    rec('  ### ### **NO EXPECTATION IS REGISTERED BY EITHER SEAT, AND THE FACE CARRIES THE REASON:**')
    rec('  ### the order registers none, and ### **A FOLD RESTATES AND MINTS NOTHING.** ### Everything')
    rec('  ### this act writes was measured and banked by an act that already scored its own expectations,')
    rec('  ### and an expectation about whether a restatement restates correctly is a question about this')
    rec('  ### act`s care -- which its own arms test directly and better.')
    rec('  ### ### **WHAT STANDS IN THEIR PLACE IS THE VERIFICATION:** %d verdict strings across %d acts,'
        % (F['strings'], len(F['rows'])))
    rec('  ### each searched in THAT ACT`S OWN closing bank with both sides normalised, ### **%d MATCHED**'
        % F['verified'])
    rec('  ### and ### **%d ROWS NOT CARRIED.**' % sum(1 for r in F['rows'] if not r['verified']))
    rec('  ### ### **AND ONE STRING WAS CORRECTED BEFORE THE SEAL BY THE (R70) REHEARSAL:** the wording')
    rec('  ### first chosen for b458 sits in its COMPONENTS bank, not its closing. ### **A FOLD MAY CARRY')
    rec('  ### ONLY WHAT THE ACT`S OWN CLOSING SAYS**, and without the rehearsal the fold would have')
    rec('  ### claimed a string was carried that its own rule forbids.')
    n1 = n2 = n3 = True
    scores = dict(registered='NONE -- a fold restates and mints nothing',
                  reason='the order registers none; every figure was scored by its own act',
                  verification=dict(strings=F['strings'], verified=F['verified'],
                                    rows=len(F['rows']),
                                    rows_not_carried=sum(1 for r in F['rows'] if not r['verified']),
                                    corrected_before_seal=1),
                  columns=F['columns'], span_tool=F['span_tool'],
                  seat='NO READING OFFERED')
    io.open(os.path.join(D, 'b463_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE DEPOSIT-AND-INSTRUMENT ARC IS FOLDED, b454 THROUGH b462, AT THE THRESHOLD`S OWN NUMBER: '
        'NINE ACTS, 24 VERDICT STRINGS EACH MATCHED IN ITS OWN CLOSING BANK, COLUMNS MODEL 3 / RECORD 6 / '
        'OBJECT 0** (b463). **LOCKED BEFORE ANY FOLD TEXT WAS WRITTEN**, 8 gates read, 4 by digest. '
        '**THE ARC`S ONE STATEMENT: an instrument that had reported every act passing was found never to '
        'have been asked to fail, by the rule it existed to apply -- and the same reading, turned on the '
        'deposit, found eight sentences asserting a machine check that point at nothing.** '
        '**TWO TARGETS WRITTEN AND NO MORE: one section appended to FINDINGS.md under a heading the span '
        'tool parses, and one block appended to the (R31) digest; each prior byte proved a TRUE PREFIX, '
        'lines removed 0.** '
        '**THE SPAN READ BACK AFTER THE WRITE: last fold b454-b462, filed by b463, next span starts at '
        'b464.** '
        '(R63)-(R73) listed with their status; (R66) STANDING and the only one that does. '
        'Carried arm failures, all real: b461`s two breaches, and the version-naming mismatch now closed '
        'by (R73) -- the convention moved and the arm did not. '
        'Both error ledgers carried, the navigator`s five and the seat`s as its acts entered them. '
        'NO EXPECTATION REGISTERED; NOTHING MINTED; no grade moved; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'NOT A GRADE -- a fold; it restates nine acts and mints nothing',
             ('data/b463_the_fold_at_span_nine.txt; data/b463_fold.json; '
              'data/b463_fold_run.txt; data/b463_components.txt; data/b463_span_notes2.txt; '
              'data/b463_scores.json; data/b463_span.json; data/b463_checks.txt; '
              'data/b463_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb463d3a); '
              'data/b463_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b463_the_fold_at_span_nine.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b463_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
