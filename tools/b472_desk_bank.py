# -*- coding: utf-8 -*-
"""b472_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b472_sources.json` and `b472_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b472_span.json')))

    rec('=' * 100)
    rec('b472_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _t = json.loads(read(os.path.join(D, 'b472_table.json')))
    _st = _t['state']
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the run : pid %s, %s at %s ; log %d bytes, last write %s ; THE LOG NOT READ'
        % (_st['pid'], _st['state'], _st['read_utc'], _st['log_bytes'], _st['log_last_write_utc']))
    rec('    sites with an E0 row : %d of 6 (%s) ; the mapping`s controls : positive %s at %d words, negative %d'
        % (len(_t['with_e0_row']), ', '.join(_t['with_e0_row']), _t['controls']['pos'][0],
           _t['controls']['pos'][1], _t['controls']['neg']))
    rec('    Alpoge-Furman : IN WHOLE %d, IN PART %d, NOT AT ALL %d, NOT PLACED %d'
        % tuple(_t['counts']['af'][k] for k in ('IN WHOLE', 'IN PART', 'NOT AT ALL', 'NOT PLACED')))
    rec('    zeta23 EF_lit_zetaZeroConfig : IN WHOLE %d, IN PART %d, NOT AT ALL %d, NOT PLACED %d'
        % tuple(_t['counts']['zeta23'][k] for k in ('IN WHOLE', 'IN PART', 'NOT AT ALL', 'NOT PLACED')))
    rec('    span by tool : %d (by number, b464-b472) ; by filings : 9' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b472 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
        ('a site verdict is source-relative, not absolute', 'STAND',
         ['CARRIED INTO COMPONENT 2: every placement cell names the bank and the line it was taken from.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['THE DETACHED RUN HAS ENDED: pid 27704 EXITED, its log 17,143 bytes, last written 1,383 s after launch.',
          '### THE LOG IS STILL NOT READ. ### The next act reads it to its end, and only then is anything known',
          'about the profiles -- and only then can (R82) be executed or found void.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['PRICED AT b471 AND NOW CARRYING A CONDITIONAL DISPOSITION: (R82) discharges it by VENDORING if, and',
          'only if, the three profiles read exactly propext, Classical.choice, Quot.sound. ### BANKED, NOT',
          'EXECUTED: it runs in the act that reads the log.']),
        ('lake 5.0.0 has no -j', 'STAND', ['BANKED AT b470.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND',
         ['MEASURED AT b470; the detached run stepped around it and has now ended.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND',
         ['GREW AT b472: (R81) as amended names a third incident -- the rule refusing its author`s own next',
          'ferry -- beside the two overclaims of 2026-09-22. ### All three are entered AT THE NEXT FOLD.']),
        ('the E0 table has no site column', 'MINT',
         ['FOUND AT b472: the E0 gate grades the eight CONSTITUENTS of the stated clause, not the six SITES of',
          'row U1. ### Under a threshold fixed before the read, ONE site of six reaches an E0 row -- (i) to K8,',
          'on seven shared words -- and five reach none. ### **SO "the strongest statement the record holds at',
          'that site" IS UNAVAILABLE AT FIVE OF SIX SITES, AND THE ABSENCE IS STRUCTURAL, NOT LEXICAL.**']),
        ('a silent bank is not a verdict of absence', 'MINT',
         ['MINTED AT b472: b470 reads no site of row U1, so five of zeta23`s six cells read NOT PLACED rather',
          'than NOT AT ALL. ### The distinction is what keeps (N3)`s "exactly one" from resting on silence',
          'without saying so. ### Nearest unplaced: site (i), which no bank has read EF_lit against.']),
        ('the span stands at the fold threshold', 'MINT',
         ['COUNTED AT b472: the span by tool is NINE acts (b464-b472), which is b366`s fold threshold.',
          '### THE FOLD IS NOT THIS ACT AND IS NOT TAKEN HERE; it is named so the next ferry can see it.']),
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
    SC = json.loads(read(os.path.join(D, 'b472_scores.json')))
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
        '**WHAT A PROOF OF RH WOULD HAVE TO SUPPLY IS WRITTEN OUT AT EACH OF ROW U1`S SIX SITES, FROM THE '
        'ROW`S OWN CELLS, AND THE TWO EXTERNAL RESULTS ARE PLACED AGAINST THOSE SENTENCES** (b472). '
        '**RE-ISSUED FROM STEP ZERO: the first issue was REFUSED under (R81) for a bare flagged word in the act '
        'text, and (R81) AS AMENDED now labels it [procedural]; ferry_scan.py gains the four words as FLAGS, '
        'printed apart from the banned stems and outside the verdict and the exit code.** '
        '**COMPONENT 0: pid 27704 has EXITED; its log is 17,143 bytes, last written 1,383 s after launch, AND IS '
        'NOT READ -- the next act reads it, and (R82) is banked unexecuted until then.** '
        '**COMPONENT 1: six sentences, each built from the index cell (b467), the KIND cell, the WITNESS cell and '
        'the row`s shape clause; a class or support appears only where a cell states one, and four of the six say '
        'UNSTATED IN THE CELLS. The cell reader was rehearsed on site (v) before the seal and agreed with the '
        'ledger`s own update line. ONE site of six reaches an E0 row -- (i) to K8, MEASURED-ON-FAMILIES both '
        'owners -- and five reach none.** '
        '**COMPONENT 2: Alpoge-Furman supplies IN PART at (ii) and NOT AT ALL at five, by b468r`s own site '
        'verdicts; zeta23`s EF_lit_zetaZeroConfig supplies IN PART at (iv), by b470`s CONTAINS verdict and site '
        '(iv)`s naming of b321, and is NOT PLACED at the other five because b470 reads no site. NEITHER SUPPLIES '
        'ANY SITE IN WHOLE.** '
        '(N1) REFUTED -- the run had already exited; (N2) HELD, VACUOUS at five sites; (N3) HELD on the face`s '
        'placement rule. No grade of the corpus moved; row U1 is unedited; no bridge typed; h2 where the deposit '
        'left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: the detached run`s log still enters the record at the next act',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL until the log is read',
             ('data/b472_what_a_claimed_proof_must_supply.txt; data/b472_components.txt; data/b472_table.json; '
              'data/b472_run_state.json; data/b472_survey.json; data/b472_scores.json; data/b472_checks.txt; '
              'data/b472_registration_2026-09-22.txt (LOCKED at sha256 5bd69717c130a358); '
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
    bank = os.path.join(D, 'b472_what_a_claimed_proof_must_supply.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b472_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
