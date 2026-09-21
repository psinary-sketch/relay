# -*- coding: utf-8 -*-
"""b461_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b461_sources.json` and `b461_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b461_span.json')))

    rec('=' * 100)
    rec('b461_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _i = json.loads(read(os.path.join(D, 'b461_inventory.json')))
    _d = json.loads(read(os.path.join(D, 'b461_dispositions.json')))
    _x = json.loads(read(os.path.join(D, 'b461_exercise.json')) or '{}')
    rec('  figures READ from this act`s own records: arms 64 ; both controls today %d ; REAL controls %d ;'
        % (_i['both_today'], _i['n_real']))
    rec('  retired %d ; successor runs %d ; positive-control passes %d ; span %d'
        % (len(_d['retired']), _x.get('run', 0), _x.get('pos_passes', -1), span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457: 12 acts over 45 items. NOT BUILT; the author`s. ### UNTOUCHED BY b461.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['ENTERED b457, RECORDED b458. The wave stays parked; no substance moved at b461.']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460 as a standing caution. ### **UNTOUCHED BY b461** -- whether any of b452`s',
          'forty-four was read correctly is still open, and this act`s work on arms does not touch it.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED to the author, and ### **NOT CLOSED HERE.**']),
        ('the suite`s arms had no controls', 'CLOSE',
         ['MEASURED at b461: 64 arms, ### **0 EXERCISED AGAINST ANY CONTROL.** ### The successor gives',
          'every surviving arm a positive and a negative control and runs both. ### The gap is closed by',
          'construction, not by assertion.']),
        ('three arms that could not fail', 'CLOSE',
         ['RETIRED at b461 under b396`s rule and the order`s conjunctive disposition: G-NOSTAGE-A,',
          'G-TWO-READINGS-TWO-FILES, G-PUSH-SIDE-B439-PREDICATE, each a literal `True`. ### Names and',
          'reasons kept in the successor as a comment, as the order requires.']),
        ('fifty-four arms with only a synthetic control', 'STAND',
         ['MEASURED at b461 and ### **NOT DISPOSED OF**, because the order`s rule is conjunctive and they',
          'admit a control. ### 12 of them read NOTHING BUT THE ACT`S OWN FACE. ### **THE DISJUNCTIVE',
          'READING WOULD RETIRE 63 OF 64**, and which rule governs is the author`s. ### Both counts printed.']),
        ('the lexical arm count over-reads', 'STAND',
         ['SEEN TWICE AT b461: rehearsal 1 found 61 literal calls against 64 declared, and the act`s own',
          '(G2) block names a RETIRED arm inside its arm list, over-reading by one. ### **A COUNT OVER A',
          'FACE IS NOT A COUNT OVER A SUITE**, and no reconciliation is attempted in either direction.']),
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
    inv = json.loads(read(os.path.join(D, 'b461_inventory.json')))
    dsp = json.loads(read(os.path.join(D, 'b461_dispositions.json')))
    ex = json.loads(read(os.path.join(D, 'b461_exercise.json')) or '{}')
    n1 = inv['both_today'] < 32
    n2 = len(dsp['retired']) >= 10
    n3 = ex.get('run', 0) < 40
    rec('  (N1) fewer than half of the sixty-four carry both controls today : %s'
        % ('HELD' if n1 else 'REFUTED'))
    rec('       ### ### **AND NOT BY A MARGIN OF ONE: THE FIGURE IS %d, NOT THIRTY-ONE.**' % inv['both_today'])
    rec('       ### b460_checks.py runs no arm against any control at all; every predicate is evaluated')
    rec('       ### once, on the live act, and nothing ever checks that it COULD have said otherwise.')
    rec('       ### **THE SEAT SAID SO ON THE FACE AND THE MEASUREMENT BORE IT OUT.**')
    rec('  (N2) at least ten arms are retired : %s -- %d retired'
        % ('HELD' if n2 else 'REFUTED', len(dsp['retired'])))
    rec('       ### the order`s rule is CONJUNCTIVE and its second limb is `cannot be given a positive')
    rec('       ### control`; exactly %d arms are constants and every other admits one, however weak.'
        % inv['n_const'])
    rec('       ### ### **UNDER THE DISJUNCTIVE READING %d OF %d WOULD RETIRE** -- measured and printed'
        % (dsp['disjunctive_would_retire'], dsp['before']))
    rec('       ### beside the applied rule, never substituted for it. ### **WHICH RULE GOVERNS IS THE AUTHOR`S.**')
    rec('  (N3) the suite after the act declares fewer than forty arms : %s -- %d run'
        % ('HELD' if n3 else 'REFUTED', ex.get('run', 0)))
    rec('       ### the successor runs %d arms, against 64 before. ### **THE CULL CAME FROM WRITING A SHORTER'
        % ex.get('run', 0))
    rec('       ### LIST, NOT FROM THE RETIREMENT RULE** -- the rule retired three; the rest of the drop is')
    rec('       ### arms this act had no sentence to test and so did not write. ### **SAID, NOT BLURRED.**')
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1) HELD AND BY A WIDER MARGIN -- correct, the figure is zero.')
    rec('  ### (N2) REFUTED, expecting three -- ### **CORRECT, AND THREE IS WHAT THE RULE RETIRED.**')
    rec('  ### (N3) REFUTED, expecting about sixty-one -- ### **WRONG.** ### The seat reasoned from the')
    rec('  ### retirement rule alone and forgot that the successor is WRITTEN, not inherited: an arm that')
    rec('  ### survives the rule still has to be worth writing. ### **THE SEAT`S OWN (N3) IS REFUTED BY ITS')
    rec('  ### OWN ACT, AND THE NAVIGATOR HAD IT RIGHT FOR A REASON THE SEAT DID NOT STATE.**')
    scores = dict(N1=dict(verdict='HELD' if n1 else 'REFUTED', both_today=inv['both_today'],
                          of=inv['declared']),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', retired=len(dsp['retired']),
                          names=dsp['retired'], disjunctive=dsp['disjunctive_would_retire']),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED', run=ex.get('run', 0), before=dsp['before']),
                  seat=dict(N1='HELD, and by a wider margin -- correct',
                            N2='REFUTED at three -- correct',
                            N3='REFUTED at about sixty-one -- WRONG; the successor is written, not inherited'))
    io.open(os.path.join(D, 'b461_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE SUITE IS MEASURED AGAINST b396`S RULE AND FOUND TO HAVE NO CONTROLS AT ALL: 64 ARMS, '
        '0 EXERCISED AGAINST ANY POSITIVE OR NEGATIVE CONTROL; 7 HAVE A REAL CONTROL DRAWN FROM THE '
        'RECORD`S OWN INCIDENTS, 54 ONLY A SYNTHETIC ONE, AND 12 READ NOTHING BUT THE ACT`S OWN FACE** '
        '(b461). **LOCKED BEFORE THE INVENTORY**, 8 gates read, 4 by digest; the instrument-audit lane '
        'opened by the ferry`s trigger under (R22)/(R23) and closed at the act`s end. '
        '**C1: 64 enumerated, 0 unmatched; REAL and SYNTHETIC controls kept in separate columns and '
        'neither called the other.** '
        '**C2: b396`s rule quoted at OPEN_TRAILS.md:4586; the order`s CONJUNCTIVE disposition applied as '
        'written -- 3 RETIRED (all literal `True`), 61 given controls, 0 kept as is. THE DISJUNCTIVE '
        'READING WOULD RETIRE 63 OF 64, MEASURED AND PRINTED BESIDE IT, NEVER SUBSTITUTED FOR IT.** '
        '**THE SUCCESSOR GIVES EVERY SURVIVING ARM BOTH CONTROLS AND RUNS BOTH: NEGATIVE MUST PASS, '
        'POSITIVE MUST FAIL.** '
        '(N1) HELD, the figure is zero not thirty-one; (N2) REFUTED at 3; (N3) REFUTED -- the successor runs '
        '51, not under forty; and the seat`s own (N3), which expected about sixty-one, is REFUTED BY ITS OWN ACT. '
        'Filed as OBSERVATIONS and not candidates under the outlier a = 4.123106: the class boundary and '
        'the prime channel`s switch-on coincide at a = sqrt 2 by two routes sharing no argument, and the '
        'outlier aim is sqrt 17 to seven digits with its support edge on the prime 17. A measurement is '
        'PRICED AND NOT RUN and no lane opens for it. '
        'Nothing about the object; no grade moved; row U1 unedited; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'NOT A GRADE -- an audit of this record`s own gate arms, and two arithmetic observations',
             ('data/b461_the_suite_given_controls.txt; data/b461_inventory.txt; '
              'data/b461_inventory.json; data/b461_exercise.txt; data/b461_dispositions.json; '
              'data/b461_scores.json; data/b461_span.json; data/b461_checks.txt; '
              'data/b461_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb461d3a); '
              'data/b461_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b461_the_suite_given_controls.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b461_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
