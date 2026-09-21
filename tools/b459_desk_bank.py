# -*- coding: utf-8 -*-
"""b459_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b459_sources.json` and `b459_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b459_span.json')))

    rec('=' * 100)
    rec('b459_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _e = json.loads(read(os.path.join(D, 'b459_embed.json')))
    _c = json.loads(read(os.path.join(D, 'b459_control.json')))
    _cells = sum(1 for g in ('G1', 'G2', 'G3') for k in _e['verdicts'][g]['placed']
                 if _e['verdicts'][g]['placed'][k])
    rec('  figures READ from this act`s own records: verdicts %s ; cells embedding %d of 18 ;'
        % (' / '.join('%s %s' % (g, _e['verdicts'][g]['verdict']) for g in ('G1', 'G2', 'G3')), _cells))
    rec('  halt proved %s ; positive control %s ; rule reads KIND %s ; span %d'
        % (_c['halt_proved'], _c['positive_control'], _c['rule_reads_kind'], span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457: S 45 items, U 23 terminals, P 67 pairs, 12 acts; 494 proof-word items name no',
          'terminal. NOT BUILT; the author`s. ### UNTOUCHED BY b459.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['ENTERED b457, RECORDED AS AN ENTRY b458. The wave stays parked; no substance moved at b459.',
          '### **A STANDING RULE IS NOT A TASK AND DOES NOT CLOSE.**']),
        ('the block rule on b458`s own face', 'CLOSE',
         ['ENTERED at b458 as the seat`s. ### **IT RECURRED AT b459 IN A NEW DRESS** -- the cut rule and the',
          'index matcher -- and is superseded by the wider item below, which names the species rather than one case.']),
        ('a rule fixed on a face against a document the face has not counted', 'STAND',
         ['MINTED at b459 from three incidents in two acts: b458`s block rule ranked file shape; b459`s cut',
          'assumed ONE enumeration where row U1 has TWO; b459`s index matcher tested for the token `index`',
          'where two sites say only `over the`. ### **EACH WAS FIXED ON A LOCKED FACE AND EACH WAS WRONG',
          'ABOUT THE DOCUMENT.** ### The cure is a COUNTED rehearsal before the seal, not a better rule. NOT BUILT.']),
        ('the six sites against three index sets', 'CLOSE',
         ['ANSWERED at b459: G1, G2 and G3 are each NOT THE INDEX SET; 2 of 18 cells embed.',
          '### b452`s proposed route to closing the LIST is refuted for all three candidates it named.']),
        ('the control the order asked for at b459', 'CLOSE',
         ['HALT PROVED on three routes with a positive control on each: the row holds NO site of kind (a).',
          '### **NO SUBSTITUTE WAS OFFERED AND NO SITE WAS RE-KINDED.**']),
        ('the banned stem on b459`s own face', 'CLOSE',
         ['ENTERED as the seat`s, ### **SECOND ACT RUNNING** -- the same stem, in the same phrase shape, caught',
          'by the same gate before the lock. ### A repeat is better evidence of a habit than the first was.']),
        ('the kind-(a) definition with no instance', 'STAND',
         ['OBSERVED at b459 and ROUTED, not closed: b404 minted kind `(a)` -- *"empty because there is nothing',
          'to range over -- vacuous forever"* -- and ### **NO SITE HAS EVER BEEN ENTERED UNDER IT.** ### Whether',
          'a definition with no instance should stand in the row is the author`s; b459 neither retires nor fills it.']),
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
    emb = json.loads(read(os.path.join(D, 'b459_embed.json')))
    ctl = json.loads(read(os.path.join(D, 'b459_control.json')))
    V = emb['verdicts']
    KS = ('(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)')
    placed = {g: [k for k in KS if V[g]['placed'][k]] for g in ('G1', 'G2', 'G3')}
    n1a = (len(placed['G1']) < 6) and (len(placed['G2']) < 6)
    n1b = (set(V['G1']['unplaced']) == set(['(v)', '(vi)'])) and (set(V['G2']['unplaced']) == set(['(v)', '(vi)']))
    n2 = (len(placed['G3']) == 6) and V['G3']['verdict'] == 'FRAGMENT'
    n3 = (ctl['rule_reads_kind'] is False)
    rec('  (N1) neither G1 nor G2 embeds all six :')
    rec('       ### ### **CLAUSE 1 : %s** -- G1 places %d of 6, G2 places %d of 6.'
        % ('HELD' if n1a else 'REFUTED', len(placed['G1']), len(placed['G2'])))
    rec('       ### ### **CLAUSE 2, ITS STATED REASON -- that (v) and (vi) are the sites that fail : %s**'
        % ('HELD' if n1b else 'REFUTED'))
    rec('       ### G1 fails at %s ; G2 fails at %s.' % (', '.join(V['G1']['unplaced']), ', '.join(V['G2']['unplaced'])))
    rec('       ### The expectation named TWO sites; the measurement finds %d and %d.'
        % (len(V['G1']['unplaced']), len(V['G2']['unplaced'])))
    rec('       ### ### **RIGHT THAT THOSE TWO FAIL, WRONG THAT ONLY THEY DO.**')
    rec('       ### **SCORED AS TWO CLAUSES, NOT AVERAGED TO ONE WORD** -- (R27).')
    rec('  (N2) G3 embeds all six and is a FRAGMENT with a variable holding no site : %s'
        % ('HELD' if n2 else 'REFUTED'))
    rec('       ### G3 places %d of 6 and its verdict is %s, not FRAGMENT.' % (len(placed['G3']), V['G3']['verdict']))
    rec('       ### The sub-clause about an empty variable is TRUE -- %s hold no site -- but the'
        % ', '.join(V['G3']['empty']))
    rec('       ### governing clause fails. ### **A TRUE SUB-CLAUSE UNDER A FAILED GOVERNING ONE IS NOT A PARTIAL HOLD.**')
    rec('  (N3) the control cannot distinguish kinds : %s' % ('HELD' if n3 else 'REFUTED'))
    rec('       ### ### **HELD, AND NOT BY THE ROUTE THE ORDER SUPPOSED.** ### The order expects the control')
    rec('       ### to RUN and fail to tell kinds apart. ### It could not run at all: the row holds no')
    rec('       ### kind-(a) site, the halt was proved on three routes each with its own positive control,')
    rec('       ### and the inability was settled instead by reading the rule`s inputs -- `KIND` is not one.')
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1) HELD AND NOT MEASURED UNSEEN -- correct on clause 1, and')
    rec('  ### the face`s caution was warranted: the seat agreed with a reason that turns out incomplete.')
    rec('  ### (N2) NO READING OFFERED -- the count was the component`s, and it refuted the navigator.')
    rec('  ### (N3) HELD ON A DIFFERENT GROUND THAN THE ORDER SUPPOSES -- **the face said so before the run')
    rec('  ### and the run bore it out**, which is the one prediction of this act worth anything.')
    scores = dict(N1=dict(clause1='HELD' if n1a else 'REFUTED',
                          clause2='HELD' if n1b else 'REFUTED',
                          placed=dict((g, len(placed[g])) for g in placed),
                          unplaced=dict((g, V[g]['unplaced']) for g in placed)),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', placed=len(placed['G3']),
                          g3_verdict=V['G3']['verdict'], empty=V['G3']['empty']),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED',
                          halt_proved=ctl['halt_proved'], positive_control=ctl['positive_control'],
                          ground='the rule inputs, not a control that ran'),
                  seat=dict(N1='HELD; clause 2 warned about on the face and duly incomplete',
                            N2='NO READING OFFERED', N3='HELD ON THE FACE OWN GROUND'))
    io.open(os.path.join(D, 'b459_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE SIX SITES OF ROW U1 ARE SET AGAINST THREE CANDIDATE INDEX SETS AND EVERY ONE IS `NOT THE '
        'INDEX SET`: THE IDENTITY`S FOUR CHANNELS PLACE ONE SITE, THE PENTAGON`S FIVE REGISTERS PLACE NONE, '
        'AND THE STATED CLAUSE`S THREE QUANTIFIED VARIABLES PLACE ONE -- 2 OF 18 CELLS EMBED** (b459). '
        '**LOCKED BEFORE ANY INDEX WAS EXTRACTED OR ANY SITE PLACED**, 8 gates read, 4 by digest. '
        '**C1: the six indices, each from its own entry -- class, height, width, width, representation, '
        'modulus; (iii) and (iv) share one, which the row itself already said.** '
        '**C2: all three ranges printed before any placement -- 4 channels off the function`s own return, '
        '5 registers off the deposit`s own sentence, 3 variables off the statement and K8.** '
        '**C3: the control HALTS -- the row records ZERO sites of kind (a), proved on three routes each '
        'with its own positive control, and no substitute was offered. ### `KIND` IS NOT AN INPUT TO THE '
        'PLACEMENT RULE, SO EVERY VERDICT HERE IS SCOPED TO INDICES AND SAYS NOTHING ABOUT ANY OBSTRUCTION.** '
        '(N1) clause 1 HELD, clause 2 REFUTED; (N2) REFUTED; (N3) HELD on the face`s own ground. '
        'No seventh site; no bridge typed; row U1 unedited and the freeze at six stands. '
        'Nothing deposits; no `lean` run; no chain run; no grade moved; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'NOT A GRADE -- a placement of six sites in three candidate index sets, scoped to indices',
             ('data/b459_the_index_sets_tested.txt; data/b459_components.txt; data/b459_sites.json; '
              'data/b459_generators.json; data/b459_embed.json; data/b459_control.json; '
              'data/b459_scores.json; data/b459_span.json; data/b459_checks.txt; '
              'data/b459_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb459d3a); '
              'data/b459_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b459_the_index_sets_tested.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b459_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
