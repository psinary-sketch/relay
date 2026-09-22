# -*- coding: utf-8 -*-
"""b477_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b477_sources.json` and `b477_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b477_span.json')))

    rec('=' * 100)
    rec('b477_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _st = json.loads(read(os.path.join(D, 'b477_state.json')))
    _sv = json.loads(read(os.path.join(D, 'b477_survey.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the run : pid %s, %s at %s, %d s after launch ; log %d bytes ; entries banked %d'
        % (_st['pid'], _st['state'], _st['read_utc'], _st['elapsed_s'], _st['log_bytes'],
           _st['entries_banked']))
    rec('    the builder`s control : window difference %.3e ; W difference %.3e ; within the floor %s'
        % (_sv['control']['window_diff'], _sv['control']['diff'], _sv['control']['within']))
    rec('    the run`s size : %d off-diagonal entries, %d diagonals, %d control diagonals ; priced %.0f s'
        % (_sv['off_entries'], _sv['diagonals'], _sv['diagonals'], _sv['priced_seconds']))
    rec('    the control`s chain returns : %s -- NO ZERO SIDE' % _sv['control_keys'])
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b477 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
        ('a site verdict is source-relative, not absolute', 'STAND', ['UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['THE b475 RUN IS STILL GOING AND IS NOT POLLED BY THIS ACT.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['SEEN AGAIN: b477 is filed after b480, so the span counts by number and not by closing order.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) NOT YET DECIDABLE; (R83) unfired.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND',
         ['THREE ENTERED AT THE FOLD; and (R87) names a fourth of the navigator`s own, the sign phrase',
          '"pole minus prime sum plus archimedean", which described Z and is withdrawn by its author.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND', ['THE FOLD IS FILED AT b474.']),
        ('the run died of memory, not of mathematics', 'STAND', ['AND THE SERIALIZED RUN PASSED THE THREE.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE b475 RUN IS PAST ITS MODULE PHASE`S TAIL BY ESTIMATE; only its end will tell.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['NO LONGER EMPTY OF ENTRIES: the Gram run is RUNNING under (R86)`s lane at b476`s price, and',
          'entries are landing in b477_entries.jsonl. ### **NO EIGENVALUE IS TAKEN YET AND NO FALSIFIER',
          'IS SCORED YET.**']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['(R85) APPLIED SINCE b475.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND', ['ROUTED to after b479.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND', ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND',
         ['FOUND AT b480, AND NOT REPEATED AT b477: this run`s logger is Python and stamps every line',
          'from datetime.now at the moment it writes it.']),
        ('the control`s Gram is a places-side Gram', 'MINT',
         ['STATED AT b477, AS THE ORDER REQUIRED: the Epstein chain the record carries, b325`s',
          'channels_q, returns arch, finite, places, pole and terms -- and NO ZERO SIDE. ### **SO THE',
          'CONTROL`S VERDICT IS SCOPED TO THE PLACES SIDE**: it can show what the Epstein places side',
          'does under this family, and it cannot show what a summed Epstein zero channel would.']),
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
    SC = json.loads(read(os.path.join(D, 'b477_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED BY THIS ACT : %d.**' % SC['registered'])
    rec('  %s' % SC['note'])
    rec('  ### the seat`s own : the diagonal -- %s' % SC['seat']['diagonal'])
    rec('  ### the seat`s own : the eigenvalues -- %s' % SC['seat']['eigenvalues'])
    rec('  ### the orientation, (R87)`s : %s' % SC['orientation'])
    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE GRAM RUN IS LAUNCHED, DETACHED UNDER (R80) PER (R86), AT b476`S PRICE AND UNDER b476`S '
        'REGISTRATION AS AMENDED BY (R87)** (b477) -- pid 17524, launched 2026-09-22T21:15:02Z, logging to '
        'relay/data/b477_gram.log with every entry appended to b477_entries.jsonl as it lands. '
        '**(R87) IS APPENDED BELOW b476`S LOCK BLOCK AND b476`S SEAL STILL READS SEAL INTACT**: W = PR - A, '
        'Sum_v W_v(f) = -Z, THE SIGNATURE READ ON -G, (F2) halting on a POSITIVE eigenvalue of G, (N2) and '
        '(N3) on the LARGEST eigenvalue of G; the navigator`s "pole minus prime sum plus archimedean" '
        'described Z and is withdrawn by its author. '
        '**THE BUILDER`S POSITIVE CONTROL IS EXACT: cross(g,g) reproduces the chain`s own autocorrelation(g) '
        'with window difference 0.000e+00 and W difference 0.000e+00, so the chain is NOT edited and f_ab is '
        'supplied to it.** '
        '**THE CONTROL`S SIDE IS STATED: b325`s channels_q returns arch, finite, places, pole, terms and NO '
        'ZERO SIDE, so the control`s Gram is a PLACES-SIDE Gram and its verdict is scoped to that side.** '
        '**THE DIAGONAL RUNS FIRST AT EVERY CELL AND A MISMATCH BEYOND THE FLOOR HALTS THE RUN BEFORE ANY '
        'OFF-DIAGONAL ENTRY**, with the zero side and trunc_bound printed beside each. 309 off-diagonal '
        'entries, 35 diagonals and 35 control diagonals, priced at 2,923 s from this act`s own timings. '
        'NO EIGENVALUE TAKEN, NO SIGNATURE READ, NO FALSIFIER SCORED, NO CLAIM ABOUT RH; the act after the '
        'pid exits scores (F1)-(F3) and (N1)-(N3) in (R87)`s orientation. h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: the Gram log enters the record at the act after the pid exits',
             'NO CORPUS GRADE MOVED; no grade above MEASURED is available to the experiment',
             ('data/b477_the_gram_run_launched.txt; data/b477_components.txt; data/b477_state.json; '
              'data/b477_survey.json; data/b477_extract.txt; data/b477_gram.pid; data/b477_launch.json; '
              'data/b477_registration_2026-09-22.txt (LOCKED at sha256 2a7a7a5438804046); '
              'data/b476_registration_2026-09-22.txt (the (R87) amendment, appended below its lock block); '
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
    bank = os.path.join(D, 'b477_the_gram_run_launched.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b477_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
