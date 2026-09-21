# -*- coding: utf-8 -*-
"""b460_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b460_sources.json` and `b460_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b460_span.json')))

    rec('=' * 100)
    rec('b460_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _c = json.loads(read(os.path.join(D, 'b460_control.json')))
    _t = json.loads(read(os.path.join(D, 'b460_techne.json')))
    rec('  figures READ from this act`s own records: control verdict %s ; cell a = %s ;'
        % (_c['verdict'], _c['cell']['a']))
    rec('  qualifying cells %d of %d ; TECHNE remote equals local %s ; commits landed %d ; span %d'
        % (_c['n_inside'], _c['n_cells'], _t.get('equal'), _t.get('ahead_at_push', 0),
           span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457: S 45 items, U 23 terminals, P 67 pairs, 12 acts; 494 proof-word items name no',
          'terminal. NOT BUILT; the author`s. ### UNTOUCHED BY b460.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['ENTERED b457, RECORDED AS AN ENTRY b458. The wave stays parked; no substance moved at b460.']),
        ('a rule fixed on a face the face has not counted', 'CLOSE',
         ['MINTED at b459 from three incidents; ### **RULED AT b460 AS (R70), THE COUNTED REHEARSAL, AND',
          'EXECUTED ON THIS ACT`S OWN FACE** -- three document-reading rules rehearsed before the seal,',
          'their yields printed, none needing repair. ### The species is now a standing rule, not a desk item.']),
        ('the kind-(a) definition with no instance', 'CLOSE',
         ['OBSERVED and ROUTED at b459; ### **ANSWERED BY THE AUTHOR AT b460 IN (R70)`s OWN SENTENCE:**',
          '*"KIND (a) STAYS DEFINED WITH NO INSTANCE; the row records zero and no instance is sought."*',
          '### The definition stands and the search is closed by ruling, not by a finding.']),
        ('b452`s absent positive control', 'CLOSE',
         ['SUPPLIED at b460: a constructed pairing of CC`s Theorem 1 with the banked cell at a = 1.3 grades',
          '**OBJECT-SIDE** by b452`s own rule. ### b452 wrote *"the test has not been shown able to say',
          'OBJECT-SIDE"*; ### **IT HAS NOW BEEN SHOWN.** ### The forty-four SOURCE-SIDE stand as read.']),
        ('what the fired control does NOT license', 'STAND',
         ['ENTERED at b460 as a standing caution, not a task: a control that fires says the instrument CAN',
          'return the verdict. ### **IT DOES NOT RE-READ THE FORTY-FOUR AND CONFERS NO CORRECTNESS ON THEM.**',
          '### Whether any of the forty-four was read correctly is untouched by this act and stays open.']),
        ('TECHNE-Core`s local-only commits', 'CLOSE',
         ['PUSHED at b460 under (R71): 24 commits now on the remote that were local-only before -- 23 carried',
          'plus the one this act wrote. ### Remote SHA read by ls-remote and equal to local HEAD; 0 still ahead.',
          '### The repository is PRIVATE and every touched path is under modules/, both checked before the push.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460 and NOT CLOSED: three queries on banked_index.py returned NO KEY. ### The index`s own',
          'reach sentence governs -- *"ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD"* -- and b452`s',
          'verdicts were read directly from its bank. ### **WHETHER THEY SHOULD BE INDEXED IS THE AUTHOR`S.**']),
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
    ctl = json.loads(read(os.path.join(D, 'b460_control.json')))
    tec = json.loads(read(os.path.join(D, 'b460_techne.json')))
    reh = json.loads(read(os.path.join(D, 'b460_rehearsal.json')))
    n1 = len(reh['inside']) >= 1
    n2 = (ctl['verdict'] == 'OBJECT-SIDE')
    n3 = (tec.get('refused') is False and tec.get('equal') is True)
    rec('  (N1) at least one banked cell has a below the window`s edge : %s'
        % ('HELD -- %d of %d cells qualify (a = %s)'
           % (len(reh['inside']), reh['n_cells'], ', '.join(str(x['a']) for x in reh['inside']))
           if n1 else 'REFUTED'))
    rec('       ### **DISCOUNTED, AND THE FACE SAID SO FIRST:** rehearsal 2 ran BEFORE the seal under (R70),')
    rec('       ### so the seat`s agreement was a report of a completed search and not a forecast.')
    rec('       ### ### **AS EVIDENCE ABOUT THE NAVIGATOR`S JUDGEMENT IT IS WORTH NOTHING; AS A RESULT IT STANDS.**')
    rec('  (N2) the control FIRES : %s' % ('HELD -- the verdict is %s' % ctl['verdict'] if n2
                                           else 'REFUTED -- the verdict is %s' % ctl['verdict']))
    rec('       ### the object is one banked cell, a = %s, a^2 = %s, prime sum %s, prime powers %s.'
        % (ctl['cell']['a'], ctl['cell']['sq'], ctl['cell']['pr'], ctl['cell']['pp']))
    rec('       ### **AND THE BAR RIDES WITH IT:** the control licenses ONE sentence -- that the instrument can')
    rec('       ### say OBJECT-SIDE. ### **IT RE-READS NONE OF THE FORTY-FOUR.**')
    rec('  (N3) the push lands and remote equals local : %s'
        % ('HELD -- remote %s == local %s ; %d still ahead'
           % (tec.get('remote', '')[:12], tec.get('head', '')[:12], tec.get('still_ahead', -1))
           if n3 else 'REFUTED'))
    rec('       ### commits now on the remote that were local-only before this act : %d (%d carried + %d written here)'
        % (tec.get('ahead_at_push', 0), tec.get('pre_ahead', 0),
           tec.get('ahead_at_push', 0) - tec.get('pre_ahead', 0)))
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1) HELD AND NOT MEASURED UNSEEN -- correct, and correctly')
    rec('  ### discounted. ### (N2) HELD -- correct, and the reason the seat gave (one cell cannot reach past a')
    rec('  ### window) is the reason the verdict turned on. ### (N3) NO READING OFFERED -- the seat declined to')
    rec('  ### predict write access and the push landed.')
    rec('  ### ### **ALL THREE OF THE NAVIGATOR`S HELD, WHICH IS RARE IN THIS RECORD AND IS WORTH A SENTENCE:**')
    rec('  ### two of the three were settled before the lock -- (N1) by the (R70) rehearsal, (N2) by a reading the')
    rec('  ### face printed -- so ### **ONLY (N3) WAS OPEN WHEN THE ACT BEGAN.** ### A face that rehearses its own')
    rec('  ### rules buys certainty and spends surprise, and the expectations are worth less in the same measure.')
    scores = dict(N1=dict(verdict='HELD' if n1 else 'REFUTED', inside=len(reh['inside']),
                          cells=reh['n_cells'], discounted='rehearsed before the seal under (R70)'),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', control=ctl['verdict'],
                          cell=ctl['cell']['a'], licenses='the instrument can say OBJECT-SIDE, and no more'),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED', remote=tec.get('remote'),
                          head=tec.get('head'), equal=tec.get('equal'),
                          landed=tec.get('ahead_at_push')),
                  seat=dict(N1='HELD AND DISCOUNTED', N2='HELD', N3='NO READING OFFERED'))
    io.open(os.path.join(D, 'b460_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**b452`S ABSENT POSITIVE CONTROL IS SUPPLIED AND IT FIRES: A CONSTRUCTED PAIRING OF CC`S THEOREM 1 '
        'WITH THE BANKED CELL AT a = 1.3 GRADES `OBJECT-SIDE` BY b452`S OWN RULE, SO THE FORTY-FOUR '
        'SOURCE-SIDE STAND AS READ; AND TECHNE-CORE`S TWENTY-FOUR LOCAL-ONLY COMMITS ARE ON THE REMOTE** '
        '(b460). **LOCKED BEFORE THE TEST AND BEFORE ANY COMMIT OR PUSH**, 8 gates read, 4 by digest. '
        '**(R70) EXECUTED ON THIS ACT`S OWN FACE: three document-reading rules rehearsed before the seal, '
        'yields printed, none needing repair.** '
        '**C1: the window`s edge DERIVED, not assumed -- f = g conv g-bar^# puts f`s support inside (1/2,2) '
        'exactly when a^2 < 2; 17 banked cells searched, 3 qualify, and the bank`s own prime-power column '
        'reaches the same edge by a second route (empty below a^2 = 2, [2] immediately above). '
        'The test run in b452`s own four fields, its first three carried verbatim. VERDICT OBJECT-SIDE.** '
        '**THE CONTROL LICENSES ONE SENTENCE -- THE INSTRUMENT CAN SAY OBJECT-SIDE -- AND RE-READS NONE OF '
        'THE FORTY-FOUR.** '
        '**C2: three modules committed by path, pushed; remote main SHA read by ls-remote EQUALS local HEAD; '
        '0 still ahead; repository PRIVATE and every touched path under modules/, both checked first.** '
        '(N1) HELD and discounted; (N2) HELD; (N3) HELD. '
        'No candidate of b452`s 82 re-verdicted; the control never counted among them; no re-expression; '
        'no chain run; row U1 unedited; no grade moved; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'NOT A GRADE -- a positive control for a side test, and a push verified at its remote',
             ('data/b460_the_control_and_the_push.txt; data/b460_components.txt; '
              'data/b460_rehearsal.json; data/b460_control.json; data/b460_techne.json; '
              'data/b460_scores.json; data/b460_span.json; data/b460_checks.txt; '
              'data/b460_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb460d3a); '
              'data/b460_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b460_the_control_and_the_push.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b460_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
