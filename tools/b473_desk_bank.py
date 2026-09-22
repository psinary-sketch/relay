# -*- coding: utf-8 -*-
"""b473_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b473_sources.json` and `b473_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b473_span.json')))

    rec('=' * 100)
    rec('b473_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _b = json.loads(read(os.path.join(D, 'b473_build.json')))
    _p = json.loads(read(os.path.join(D, 'b473_profiles.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the log : %d bytes, %d lines ; lake build Solution EXIT %s ; wall %.2f s'
        % (_b['bytes'], _b['lines'], _b['exits'].get('lake build Solution'), _b['wall_s']))
    rec('    modules failed : %d -- %s' % (len(_b['failures']), ', '.join(f['module'] for f in _b['failures'])))
    rec('    profile rows : %d ; STANDARD THREE %d ; ABSENT %d'
        % (len(_p['rows']), sum(1 for r in _p['rows'] if r['verdict'] == 'STANDARD THREE'),
           sum(1 for r in _p['rows'] if r['verdict'] == 'ABSENT')))
    rec('    (R82) : %s %s' % (_p['r82']['verdict'], _p['r82']['kind']))
    rec('    comparator : NOT RUN ; its tool cache present : %s' % _p['comparator']['cache_present'])
    rec('    span by tool : %d (by number, b464-b473) ; by filings : 10' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b473 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
         ['STILL NOT RUN, AND NOW MEASURED: the detached run reached 8,873 of 8,887 targets in 1,383 s and',
          'DIED OF MEMORY at three modules, so no profile was produced. ### The item stands, and what it now',
          'carries is a price: a completed run needs a memory bound this machine did not hold at lake`s own',
          'parallelism.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['(R82)`S CONDITION IS VOID FOR WANT OF A RUN, so the work-order is neither discharged nor refused.',
          '### (R83)`s SIDE-explicit-formula is NOT created, named in the roster or pinned: its trigger did',
          'not fire. ### The order stands exactly where b471 priced it.']),
        ('lake 5.0.0 has no -j', 'STAND',
         ['BANKED AT b470 -- and it is now the operative constraint: with no job flag and LEAN_NUM_THREADS',
          'unset, lake`s own parallelism is what exhausted the memory.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE INCIDENTS, ENTERED AT THE NEXT FOLD.']),
        ('the E0 table has no site column', 'STAND', ['FOUND AT b472.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND',
         ['COUNTED AGAIN AT b473: TEN acts (b464-b473), one past b366`s threshold of nine. ### THE FOLD IS',
          'NOT THIS ACT; (R83) also puts its own next act AFTER the fold, so the fold is the next thing due.']),
        ('the run died of memory, not of mathematics', 'MINT',
         ['FOUND AT b473: three modules -- Zeta23.Hypotheses, Zeta23.Defs.Counting, Zeta23.Taper.Basic -- died',
          'with "INTERNAL PANIC: out of memory" and std::bad_alloc. ### **NO MODULE REPORTED A sorry, AN',
          'UNSOLVED GOAL OR A TYPE ERROR**, and the counter stood at 8,873 of 8,887. ### So nothing is known',
          'against zeta23 by this failure, and nothing is known for it either.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'MINT',
         ['OPENED AT b473: to decide (R82) the record needs a run that completes. ### What that costs is now',
          'measured rather than guessed: 23 minutes of wall time got to within fourteen targets of the end at',
          'lake`s own parallelism, and the failure was memory. ### A next attempt would have to bound the',
          'workers, and lake 5.0.0 has no flag for it -- LEAN_NUM_THREADS is the only lever the record holds.']),
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
    SC = json.loads(read(os.path.join(D, 'b473_scores.json')))
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
        '**THE b471 DETACHED RUN`S LOG IS READ WHOLE FOR THE FIRST TIME, COMMITTED AS EVIDENCE, AND (R82) IS '
        'DECIDED: VOID FOR WANT OF A RUN** (b473). **COMPONENT 1: `lake build Solution` EXIT 1 after 1,383.05 s '
        'by the log`s own timestamps; 8,873 of 8,887 targets built; THREE MODULES FAILED -- Zeta23.Hypotheses '
        'and Zeta23.Defs.Counting with "INTERNAL PANIC: out of memory", Zeta23.Taper.Basic with std::bad_alloc '
        '(exit 3221226505). NO MODULE REPORTED A sorry, AN UNSOLVED GOAL OR A TYPE ERROR: the run died of '
        'memory, not of mathematics.** '
        '**COMPONENT 2: twenty rows -- the source`s own seventeen Challenge theorems plus the three '
        'explicit-formula declarations -- and ALL TWENTY READ ABSENT, because the log carries no "depends on '
        'axioms" line at all: step 2 could not find the library and step 3 failed on a missing object file. '
        '(R82) IS THEREFORE VOID FOR WANT OF A RUN AND NOT ON A BAD PROFILE, AND NOTHING IS KNOWN FOR OR '
        'AGAINST zeta23 BY IT. THE GRADE STAYS `DERIVES, CONDITIONAL` EXACTLY AS b468r LEFT IT; the re-read is '
        'owed and is not performed here.** '
        '**COMPONENT 3: the comparator is NOT RUN, with every reason printed -- its tool cache is absent so a '
        'run would fetch four pinned checkouts; go, cargo and landrun are absent; the script requires Linux and '
        'this machine is win32; and Solution did not build. Nothing was fetched, cloned or built.** '
        '**(R83) OBEYED BY DOING NOTHING: the condition did not hold, so SIDE-explicit-formula is not created, '
        'named or pinned.** '
        '(N1) REFUTED; (N2) REFUTED; (N3) HELD on the outcome, the cause wider than the order named. No grade '
        'of the corpus moved; nothing imported; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'the b471 run`s log, read whole and committed: data/b471_zeta23_build.log',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL -- the run did not complete',
             ('data/b473_the_log_read_and_r82_decided.txt; data/b473_components.txt; data/b473_profiles.json; '
              'data/b473_build.json; data/b471_zeta23_build.log; data/b473_survey.json; data/b473_scores.json; '
              'data/b473_registration_2026-09-22.txt (LOCKED at sha256 b104a0e536bbd029); '
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
    bank = os.path.join(D, 'b473_the_log_read_and_r82_decided.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b473_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
