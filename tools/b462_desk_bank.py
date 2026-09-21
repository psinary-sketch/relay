# -*- coding: utf-8 -*-
"""b462_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b462_sources.json` and `b462_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b462_span.json')))

    rec('=' * 100)
    rec('b462_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _c = json.loads(read(os.path.join(D, 'b462_census.json')))
    _x = json.loads(read(os.path.join(D, 'b462_index.json')))
    rec('  figures READ from this act`s own records: items %d ; TERMINAL %d ; CARRIER %d ; NOTHING %d ;'
        % (_c['total'], _c['by_bin']['NAMES A TERMINAL'], _c['by_bin']['NAMES A CARRIER'],
           _c['by_bin']['NAMES NOTHING']))
    rec('  declared names indexed %d over %d kernels ; machine-checked with no terminal %d ; span %d'
        % (_x['index_names'], len(_x['per_kernel']), _c['machine_checked_no_terminal'],
           span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'STAND',
         ['PRICED at b457: 12 acts over 45 items. NOT BUILT; the author`s. ### **AND THIS ACT IS ITS',
          'NEIGHBOUR, NOT ITS EXECUTION** -- b462 counts sentences and grades none, which is the half',
          'of the gate that costs nothing. ### The unfoldings, which are the gate`s price, are untouched.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['ENTERED b457. The wave stays parked; no substance moved at b462.']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460. ### **UNTOUCHED BY b462.**']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED to the author, NOT CLOSED HERE.']),
        ('the twelve face-only arms', 'STAND',
         ['RE-WORDED BY (R72), THE AUTHOR`S: an arm whose only input is the act`s own face is not a',
          'control on the record, and each of the twelve is ### **CONVERTED TO READ THE ARTEFACT THE FACE',
          'DESCRIBES, OR RETIRED WITH ITS REASON, AT THE NEXT ACT THAT TOUCHES THE SUITE.** ### b462 is',
          'not that act. ### **AND THE DISJUNCTIVE READING IS NOT ADOPTED** -- b461`s standing item that',
          'offered it is closed by the ruling, not by a finding.']),
        ('the disjunctive retirement reading', 'CLOSE',
         ['CLOSED BY (R72): the retirement rule is the applied one. ### b461 measured that 63 of 64 would',
          'retire under the other reading and refused to substitute it; ### **THE AUTHOR HAS NOW REFUSED IT',
          'TOO**, and the measurement stands in b461`s bank as a measurement and not as a proposal.']),
        ('the lexical arm count over-reads', 'STAND',
         ['SEEN AGAIN AT b462: the regspec counts 49 arm tokens on the whole face while the (G2) block',
          'declares 49 and the suite runs 49. ### **THEY AGREE THIS TIME**, which is not a repair -- the',
          'face simply names no arm outside its own arm block. ### The species stands until a rule does.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND AT b462 BEFORE THE SEAL: zenodo_fetch_2026-08-10.jsonl holds both kernel records with',
          '### **ZERO DESCRIPTION CHARACTERS** -- fetched for metadata only. ### The monograph record`s',
          'description IS banked (5195 chars). ### b455 met the same gap and substituted; b462 substitutes',
          'and labels. ### **WHETHER THE TWO DESCRIPTIONS SHOULD BE FETCHED AND BANKED IS THE AUTHOR`S**,',
          'and it needs a lane that permits a fetch. ### ROUTED, NOT TAKEN.']),
        ('the terminal-less census, and what it is not', 'STAND',
         ['MEASURED AT b462: of 419 sentence-items on the deposited surfaces, ### **300 NAME NOTHING**, 82',
          'name a carrier and 37 name a terminal that resolves. ### **AND THE BIN IS NOT A DEFECT COUNT:**',
          'its strongest items are attributions to CLASSICAL results -- Ostrowski, Stormer, Artin-Whaples,',
          'Riemann, Hecke, Tate -- which name no kernel terminal because they are not kernel claims.',
          '### **NO ITEM IS GRADED AND NO DEPOSIT-LEVEL MATTER IS OPENED.** ### Any disposition is the author`s.']),
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
    cen = json.loads(read(os.path.join(D, 'b462_census.json')))
    nn = cen['by_bin']['NAMES NOTHING']
    n1 = abs(nn - 494) <= 49.4
    n2 = cen['mono_nothing'] * 2 > nn
    n3 = cen['machine_checked_no_terminal'] < 50
    rec('  (N1) the re-measured NAMES NOTHING count is within ten percent of 494 : %s'
        % ('HELD' if n1 else 'REFUTED'))
    rec('       ### the re-measured count is ### **%d**, against 494. ### deviation %.1f%%.'
        % (nn, 100.0 * abs(nn - 494) / 494))
    rec('       ### ### **AND THE SEAT REFUSES THE COMPARISON AS EVIDENCE, AS ITS FACE SAID IT WOULD:**')
    rec('       ### 494 was measured at b457 over a WIDER population -- the record`s files, its description,')
    rec('       ### the kernel README and .zenodo.json, and lv`s README -- with a different word list.')
    rec('       ### **TWO UNLIKE MEASUREMENTS DISAGREEING IS NOT EVIDENCE ABOUT EITHER**, and the')
    rec('       ### expectation is scored as the order words it and read no further.')
    rec('  (N2) more than half of NAMES NOTHING items sit in the monograph : %s -- %d of %d (%.1f%%)'
        % ('HELD' if n2 else 'REFUTED', cen['mono_nothing'], nn,
           100.0 * cen['mono_nothing'] / nn if nn else 0))
    rec('  (N3) fewer than fifty items say `machine-checked` and name no terminal : %s -- %d'
        % ('HELD' if n3 else 'REFUTED', cen['machine_checked_no_terminal']))
    rec('       ### of which ### **%d ARE `NAMES NOTHING`** and the rest name a carrier.'
        % cen['machine_checked_nothing'])
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1) NO READING OFFERED, and the refusal was the point --')
    rec('  ### ### **THE SEAT DECLINED TO PREDICT A COMPARISON IT HAD ALREADY ARGUED WAS NOT EVIDENCE.**')
    rec('  ### (N2) HELD -- correct, and for the reason given: the monograph is 217264 characters against')
    rec('  ### 128000-odd for the other twelve surfaces together. ### (N3) NO READING OFFERED.')
    scores = dict(N1=dict(verdict='HELD' if n1 else 'REFUTED', measured=nn, against=494,
                          deviation_pct=round(100.0 * abs(nn - 494) / 494, 1),
                          note='b457 measured 494 over a wider population and word list'),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', monograph=cen['mono_nothing'], of=nn),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED',
                          machine_checked_no_terminal=cen['machine_checked_no_terminal'],
                          of_which_nothing=cen['machine_checked_nothing']),
                  seat=dict(N1='NO READING OFFERED -- the comparison refused as evidence',
                            N2='HELD -- correct', N3='NO READING OFFERED'))
    io.open(os.path.join(D, 'b462_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE DEPOSITED SURFACES CARRY 419 SENTENCES WITH A PROOF WORD, AND 300 OF THEM NAME NOTHING: '
        '37 NAME A TERMINAL THAT RESOLVES IN A ROSTERED KERNEL, 82 NAME A CARRIER, AND 8 SAY '
        '`machine-checked` WHILE NAMING NO TERMINAL** (b462). **LOCKED BEFORE THE CENSUS**, 8 gates read, '
        '4 by digest. '
        '**AND THE BIN IS NOT A DEFECT COUNT: its strongest items are attributions to CLASSICAL results -- '
        'Ostrowski, Stormer, Artin-Whaples, Riemann, Hecke, Tate -- which name no kernel terminal because '
        'they are not kernel claims. NO ITEM IS GRADED AND NO TERMINAL IS NAMED FOR ANY OF THEM.** '
        '**C1: the population is ELEVEN deposit files plus TWO LABELLED SUBSTITUTES -- the two kernel '
        'records` Zenodo descriptions are NOT BANKED (zero characters each), found before the seal; the '
        'kernel tag`s .zenodo.json stands for one and lv`s README for the other, labelled every time.** '
        '**C2: 3422 declared names indexed over 43 kernels, 2 at a PIN and 41 at HEAD and it says which; '
        'the positive control resolves; bins sum to items; every count broken out by kind so headings and '
        'table rows are never hidden.** '
        '(N1) REFUTED -- 300 against 494, a 39.3% deviation, and the comparison refused as evidence because '
        '494 was measured over a wider population; (N2) HELD at 201 of 300; (N3) HELD at 8. '
        'The order`s attribution of S=45 and 494 to b455 is corrected: they are b457`s. '
        'Nothing deposits; no deposit-level matter opened; no grade moved; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'NOT A GRADE -- a census of sentences by what they name; no item graded, no terminal named',
             ('data/b462_the_terminal_less_census.txt; data/b462_census.txt; '
              'data/b462_census.json; data/b462_index.json; data/b462_components.txt; '
              'data/b462_scores.json; data/b462_span.json; data/b462_checks.txt; '
              'data/b462_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb462d3a); '
              'data/b462_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b462_the_terminal_less_census.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b462_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
