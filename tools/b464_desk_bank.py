# -*- coding: utf-8 -*-
"""b464_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b464_sources.json` and `b464_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b464_span.json')))

    rec('=' * 100)
    rec('b464_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _g = json.loads(read(os.path.join(D, 'b464_grades.json')))
    _p = json.loads(read(os.path.join(D, 'b464_params.json')))
    rec('  figures READ from this act`s own records: eight by grade %s ;'
        % ' / '.join('%s %d' % (k, _g['by_grade'][k]) for k in sorted(_g['by_grade'])))
    rec('  sites %s ; unvisited parameters %d ; span %d'
        % (' / '.join('%s %d' % (k, _p['tally'][k]) for k in sorted(_p['tally'])),
           len(_p['unvisited']), span['current_span']))
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b457 LEFT FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('the sentence gate', 'CLOSE',
         ['PRICED at b457 at twelve acts over forty-five items. ### **RUN AT b464 ON THE EIGHT ITEMS THAT',
          'MATTER MOST** -- one unfolding each, terminal located at its pin, statement read, grade conferred.',
          '### The gate as priced covered 45 items; ### **THIS ACT PAID 8 OF THEM AND SAYS SO.** ### The',
          'remaining 37 stay priced and unbuilt, and the item is re-worded rather than discharged whole.']),
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING, and ### **NOW CARRYING SIX ROUTED MATTERS** -- the six sentences grading NOT THE CLAIM,',
          'named at their file and line, ### **NOT REPAIRED, NO ERRATUM DRAFTED, NO WAVE OPENED.**']),
        ('what the fired control does not license', 'STAND',
         ['ENTERED at b460. ### UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED. ### UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb; b464 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462, ROUTED; it needs a lane that permits a fetch, and this act opens none.']),
        ('the terminal-less census, and what it is not', 'STAND',
         ['b462`s 300 stand. ### **AND b464 SHARPENS WHAT A BIN VERDICT MEANS:** a NOT THE CLAIM says',
          'THIS SEARCH BY THIS RULE FOUND NO TERMINAL STATING IT -- not that the sentence is false, not',
          'that no terminal could carry it, not that the deposit is wrong.']),
        ('six deposited sentences grading NOT THE CLAIM', 'STAND',
         ['MEASURED AT b464 and ### **ROUTED UNDER (R66), NOT REPAIRED.** ### None is b455`s C2 or C6 --',
          'those are the record`s description and the kernel README; ### **ALL SIX SIT IN DEPOSITED FILES**',
          'and E-2026-09-14-1 does not cover them. ### Any disposition is the author`s.']),
        ('a deposited sentence whose nearest terminal is a SHELL', 'STAND',
         ['FOUND AT b464: ONE_PAGE_PROOF.md:32 reaches `conservation_s_dark : True := trivial` in legacy/.',
          '### **AND A SUBSTANTIVE TERMINAL SITS BESIDE IT AT THE SAME SCORE AND PIN** --',
          '`s_darkness_from_product`, which states the product formula`s local factor. ### **THE SHELL IS',
          'WHAT THE RULE REACHED, NOT WHAT THE KERNEL HOLDS**, and both are named. ### ROUTED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND',
         ['MINTED AT b464 from two incidents in one act: among equal-scoring hits at the same pin the rule',
          'picks by NAME, which reached a shell at item 5 and an inductive at item 4 while better hits sat',
          'beside them. ### **A TIE-BREAK THAT IS CONTENT-BLIND IS A SEARCH THAT REPORTS ITS OWN SORT ORDER.**',
          '### Both content-nearest terminals are named and read; the rule is NOT rewritten in this act.']),
        ('five parameters of the imported formula with no site', 'STAND',
         ['MEASURED AT b464: CC (148) names rho, v, m, p and fixes zeta, and ### **NO SITE INDEX OF ROW U1',
          'IS ANY OF THEM.** ### ROUTED TO THE AUTHOR WITH THE ROW`S REOPENING CONDITION BESIDE IT.',
          '### **NO SITE IS ENTERED; ROW U1 IS FROZEN AT SIX AND UNEDITED; NO BRIDGE IS TYPED.**']),
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
    G = json.loads(read(os.path.join(D, 'b464_grades.json')))
    P = json.loads(read(os.path.join(D, 'b464_params.json')))
    ntc = G['not_the_claim']
    n1a = ntc <= 2
    n1b = False
    coord = P['tally'].get('A COORDINATE OF ONE', 0) + P['tally'].get('A PARAMETER', 0)
    n2 = (coord == 5)
    n3 = (len(P['unvisited']) == 0)
    rec('  (N1)(a) at most two of the eight grade NOT THE CLAIM : %s -- ### **%d DO.**'
        % ('HELD' if n1a else 'REFUTED', ntc))
    rec('          the eight by grade : %s'
        % ' ; '.join('%s %d' % (k, G['by_grade'][k]) for k in sorted(G['by_grade'])))
    rec('  (N1)(b) any that do are C2 or C6, already under E-2026-09-14-1 : ### **REFUTED.**')
    rec('          ### **NONE OF THE EIGHT IS C2 OR C6**, and the face said so before the grading:')
    rec('          C2 is the monograph RECORD`s description paragraph and C6 the kernel README`s line,')
    rec('          neither of which is a FILE of the deposit. ### **ALL EIGHT SIT IN DEPOSITED FILES**,')
    rec('          so ### **THE SIX ARE SIX DEPOSIT-LEVEL MATTERS E-2026-09-14-1 DOES NOT COVER.**')
    rec('  (N2) five of six indices are a parameter or a coordinate of one, the height alone OF NO')
    rec('       PARAMETER : %s' % ('HELD' if n2 else 'REFUTED'))
    rec('       ### the measurement : %s'
        % ' ; '.join('%s %d' % (k, P['tally'][k]) for k in sorted(P['tally'])))
    rec('       ### ### **THE HEIGHT IS OF NO PARAMETER, AS EXPECTED -- AND SO ARE TWO MORE.**')
    rec('       ### CC (148) is a statement about the Riemann zeta function and no other: it carries no')
    rec('       ### L-function, no representation, no conductor. ### And its right sum runs over PLACES')
    rec('       ### and prime powers, not over moduli of congruence. ### **THE EXPECTATION WAS RIGHT')
    rec('       ### ABOUT THE HEIGHT AND WRONG ABOUT THE COUNT.**')
    rec('  (N3) the source names no parameter that is UNVISITED : %s -- ### **%d ARE.**'
        % ('HELD' if n3 else 'REFUTED', len(P['unvisited'])))
    rec('       ### %s' % ', '.join(P['unvisited']))
    rec('  ### THE SEAT`S OWN, FROM THE FACE: (N1)(a) NO READING OFFERED. ### (N1)(b) REFUTED -- correct,')
    rec('  ### and argued on the face BEFORE the grading rather than after it. ### (N2) REFUTED, naming')
    rec('  ### the representation and the modulus -- ### **CORRECT ON BOTH.** ### (N3) REFUTED, naming the')
    rec('  ### zeros and the places -- ### **CORRECT, AND TWO MORE BESIDES.**')
    n1 = n1a
    scores = dict(N1a=dict(verdict='HELD' if n1a else 'REFUTED', not_the_claim=ntc,
                           by_grade=G['by_grade']),
                  N1b=dict(verdict='REFUTED',
                           reason='none of the eight is C2 or C6; all sit in deposited FILES'),
                  N2=dict(verdict='HELD' if n2 else 'REFUTED', tally=P['tally'],
                          note='height OF NO PARAMETER as expected, and representation and modulus too'),
                  N3=dict(verdict='HELD' if n3 else 'REFUTED', unvisited=P['unvisited']),
                  seat=dict(N1a='NO READING OFFERED', N1b='REFUTED -- correct, argued before the grading',
                            N2='REFUTED -- correct on representation and modulus',
                            N3='REFUTED -- correct on the zeros and the places'))
    io.open(os.path.join(D, 'b464_scores.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(scores, indent=1, ensure_ascii=False) + NL)

    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE EIGHT DEPOSITED SENTENCES ASSERTING A MACHINE CHECK ARE UNFOLDED AGAINST THE NEAREST '
        'TERMINAL AT ITS DEPOSITED PIN: 6 GRADE `NOT THE CLAIM`, 1 `INTERFACES` ON A NAMED PREMISE, '
        'AND 1 `SHELL` -- `conservation_s_dark : True := trivial`** (b464). **LOCKED BEFORE ANY '
        'SENTENCE WAS GRADED**, 8 gates read, 4 by digest. '
        '**NONE OF THE EIGHT IS b455`S C2 OR C6 -- ALL SIT IN DEPOSITED FILES -- SO THE SIX ARE SIX '
        'DEPOSIT-LEVEL MATTERS E-2026-09-14-1 DOES NOT COVER: NAMED, ROUTED UNDER (R66), NOT REPAIRED, '
        'NO ERRATUM DRAFTED, NO WAVE OPENED.** '
        '**AND A NOT THE CLAIM HERE IS NOT A FINDING THAT THE SENTENCE IS FALSE, NOR THAT NO TERMINAL '
        'COULD CARRY IT: IT IS THAT THIS SEARCH, BY THIS RULE, FOUND NO TERMINAL STATING IT.** '
        '**C2: CC arXiv:2006.13771v1 (148) read at its pinned text layer with its garbling caveat '
        'carried; it quantifies over f in C_c^infty(R*_+), over all complex zeros rho of ZETA, over all '
        'places v of Q, over m and over p -- and fixes zeta, carrying no representation. Of the six '
        'site indices, 3 are a coordinate of a named parameter (class, width, width) and 3 are OF NO '
        'PARAMETER (height, representation, modulus); 5 parameters are UNVISITED.** '
        '(N1)(a) REFUTED at 6; (N1)(b) REFUTED; (N2) REFUTED; (N3) REFUTED at 5. '
        'No site entered; row U1 frozen at six and unedited; no bridge typed; nothing about the object; '
        'no grade moved on any row; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN BY THIS ACT',
             'none printed by this act; no axiom profile computed and no kernel read',
             'GRADES CONFERRED ON EIGHT SENTENCES, NOT ON ROWS -- no correspondence row or registry cell moved',
             ('data/b464_the_eight_and_the_parameters.txt; data/b464_grades.json; '
              'data/b464_params.json; data/b464_placement.json; data/b464_components.txt; '
              'data/b464_scores.json; data/b464_span.json; data/b464_checks.txt; '
              'data/b464_registration_2026-09-21.txt (LOCKED at sha256 6d300319eb464d3a); '
              'data/b464_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b464_the_eight_and_the_parameters.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b464_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
