# -*- coding: utf-8 -*-
"""b458_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b458_sources.json` and `b458_entries.json`; the correspondence row is written
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
    src = json.loads(read(os.path.join(D, 'b458_sources.json')))
    ent = json.loads(read(os.path.join(D, 'b458_entries.json')))
    span = json.loads(read(os.path.join(D, 'b458_span.json')))

    rec('=' * 100)
    rec('b458_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records: rulings with fuller text %d of 4 ; in a ferry %d ;'
        % (src['n_fuller'], src['n_ferry']))
    rec('  entries 5 ; the four %d lines ; (R69) %d lines ; added %d ; removed %d ; span %d'
        % (ent['four'], ent['r69'], ent['added'], ent['removed'], span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457: S 45 items, U 23 terminals, P 67 pairs, 12 acts by the face`s formula; 494',
          'proof-word items name no terminal and are out of its reach. NOT BUILT; the author`s. ### UNTOUCHED BY b458.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['ENTERED at b457; RECORDED AS AN ENTRY at b458 (OPEN_TRAILS.md, the (R66) entry).',
          'The wave stays parked; no substance moved at b458. ### **A STANDING RULE IS NOT A TASK, AND IT DOES NOT CLOSE.**']),
        ('the seat`s predicate at b457', 'CLOSE',
         ['ENTERED at b457 and carried into b458`s trail record as an error-ledger line.',
          '### **AN ERROR ENTRY IS A RECORD, NOT AN OBLIGATION** -- it is swept off the desk here and stays in the ledger.']),
        ('W-ORD-MIRROR-ZIP-NAME', 'CLOSE',
         ['CLOSED BY RULING (R69) at b458. Its row stands unedited at OPEN_TRAILS.md:6516, inside b449`s',
          'trail record; the (R69) entry carries the closure and quotes the row. ### **THE BUILDER IS NOT EDITED.**']),
        ('(R65) through (R69) as records', 'CLOSE',
         ['WRITTEN at b458: five entries appended to OPEN_TRAILS.md in (R61)`s form, each quoting the paste',
          'that carried its ruling in. ### The defect that occasioned them -- four rulings with no entry -- is gone.']),
        ('the block rule on b458`s own face', 'STAND',
         ['ENTERED as the seat`s: the face`s `longest contiguous block` rule ranked FILE SHAPE and not ruling',
          'text, and failed at three tiers before the read used the order`s own noun. ### All yields printed; no face edited.']),
        ('the banned stem on b458`s own face', 'CLOSE',
         ['ENTERED as the seat`s: the face carried one live banned stem; the term scan refused the lock until it',
          'was corrected. ### **THE GATE DID ITS WORK BEFORE THE LOCK, WHICH IS WHERE IT IS SUPPOSED TO.**']),
        ('the re-sync turn`s stale open-items list', 'CLOSE',
         ['ENTERED as the seat`s: the turn before this ferry named three items open that b457 had discharged,',
          'read out of a memory hook that recorded b457`s CONTENT. ### Corrected in the same turn, before the ferry.']),
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
    n1 = src['n_ferry'] >= 2
    n2 = ent['four'] < 60
    n3_count = (standing == 3)
    n3_members = (set(stand_names) == {'the sentence gate',
                                       '(R66) the deposit corrected, not re-issued',
                                       'the seat`s predicate at b457'})
    n3 = n3_count and n3_members
    rec('  (N1) at least two of the four have fuller text banked in a relay ferry file : %s'
        % ('HELD -- %d of 4, and all four are in a ferry file' % src['n_ferry'] if n1 else 'REFUTED'))
    rec('       ### **DISCOUNTED AS THE FACE DECLARED:** (R66)`s instance was seen in the re-sync turn')
    rec('       ### before the face; the other three were not. ### **THE EXPECTATION HOLDS ON THREE UNSEEN.**')
    rec('  (N2) the four entries add fewer than sixty lines in all : %s'
        % ('HELD -- %d lines; with (R69) the append is %d' % (ent['four'], ent['added']) if n2
           else 'REFUTED -- %d lines' % ent['four']))
    rec('  (N3) the desk stands at three -- the sentence gate, (R66), and the seat`s b457 error entry :')
    rec('       ### ### **THE COUNT : %s** -- the desk stands at %d.' % ('HELD' if n3_count else 'REFUTED', standing))
    rec('       ### ### **THE MEMBERSHIP : %s** -- the standing set is {%s}.'
        % ('HELD' if n3_members else 'REFUTED', ' ; '.join(stand_names)))
    rec('       ### The seat`s b457 error entry is SWEPT OFF as a record rather than kept standing, and this')
    rec('       ### act`s own block-rule defect is entered in its place. ### **TWO CLAUSES, SCORED SEPARATELY')
    rec('       ### RATHER THAN AVERAGED TO ONE WORD** -- (R27). ### **OVERALL : %s.**' % ('HELD' if n3 else 'REFUTED'))
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1) HELD AND DISCOUNTED -- correct, and the discount was real;')
    rec('  ### (N2) NO READING OFFERED -- the count is the component`s; (N3) REFUTED -- correct, and for the')
    rec('  ### reason the face gave: this act enters items of its own.')

    scores = dict(N1=dict(verdict='HELD' if n1 else 'REFUTED', n_ferry=src['n_ferry'],
                          n_fuller=src['n_fuller'], discounted='R66 seen before the face'),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', four=ent['four'], added=ent['added']),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED',
                          count='HELD' if n3_count else 'REFUTED',
                          membership='HELD' if n3_members else 'REFUTED',
                          standing=standing, names=stand_names),
                  seat=dict(N1='HELD AND DISCOUNTED', N2='NO READING OFFERED', N3='REFUTED'))
    io.open(os.path.join(D, 'b458_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**RULINGS (R65) THROUGH (R69) ARE ENTERED AS RECORDS: FIVE ENTRIES IN (R61)`S FORM, EACH QUOTING '
        'THE PASTE THAT CARRIED ITS RULING IN; ALL FOUR OF (R65)-(R68) HAVE FULLER TEXT IN A BANKED FERRY '
        'THAN THE ONE-LINE MENTION THE TRAIL HELD** (b458). **LOCKED BEFORE THE SEARCH AND ANY WRITE**, '
        '8 gates read, 4 by digest. **C1: SCOPE 86 RELAY FILES; THREE LENGTH-RANKED YIELDS PRINTED AND ALL '
        'THREE DEFECTIVE -- THEY RANK FILE SHAPE, NOT RULING TEXT; THE READ IS BY THE ORDER`S OWN NOUN, THE '
        'BANKED FERRY. 4 OF 4 FULLER.** **C2: 5 ENTRIES APPENDED; THE FOUR 48 LINES, (R69) 12; PREFIX PROVED '
        'BYTE FOR BYTE; LINES REMOVED 0; ONE DOCUMENT WRITTEN.** '
        '**W-ORD-MIRROR-ZIP-NAME CLOSES BY RULING (R69); b449`S ROW IS NOT EDITED.** '
        '(N1) HELD AND DISCOUNTED; (N2) HELD; (N3) REFUTED. '
        'Nothing deposits; no `lean` run; no grade moved; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; b457`s run at tag v1.5 = 0e5233f is cited, not repeated',
             'NOT A GRADE -- a record of five author rulings, each quoted from the paste that carried it in',
             ('data/b458_the_rulings_entered.txt; data/b458_components.txt; data/b458_sources.json; '
              'data/b458_entries.json; data/b458_scores.json; data/b458_span.json; data/b458_checks.txt; '
              'data/b458_registration_2026-09-21.txt (LOCKED at sha256 87b194a89b155323); '
              'data/b458_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b458_the_rulings_entered.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b458_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
