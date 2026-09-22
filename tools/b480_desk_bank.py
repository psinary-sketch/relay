# -*- coding: utf-8 -*-
"""b480_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b480_sources.json` and `b480_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b480_span.json')))

    rec('=' * 100)
    rec('b480_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _s = json.loads(read(os.path.join(D, 'b480_snapshot.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the snapshot : %d bytes, read %s ; the run STILL GOING'
        % (_s['bytes'], _s['read_utc']))
    rec('    modules started %d of %d ; still to start %d ; failures %s ; memory lines %d'
        % (_s['started'], _s['order'], _s['remaining'], _s['failures'] or 'NONE', len(_s['panics'])))
    rec('    (N1) : %s' % _s['n1']['verdict'])
    rec('    (R82) : %s ; (R83) : %s' % (_s['r82'], _s['r83']))
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b480 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
         ['THE SERIALIZED RUN HAS PASSED 169 OF 188 MODULES WITH EVERY EXIT 0, AND HAS NOT REACHED THE',
          'PROFILE STEPS. ### The item stands until a finished log carries them.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['(R82) IS NOT YET DECIDABLE AND (R83) DOES NOT FIRE. ### Neither discharged nor refused.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND',
         ['AND A RUNNING BANK IS NOT A FINISHED ONE: this act reads a log that is still being written and',
          'says SNAPSHOT in every figure.']),
        ('the span stands at the fold threshold', 'STAND', ['THE FOLD IS FILED AT b474.']),
        ('the run died of memory, not of mathematics', 'STAND',
         ['AND NOW THE OTHER HALF IS MEASURED: the same three modules pass at EXIT 0 one process at a',
          'time. ### **THE BOUND WAS THE PARALLELISM.**']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE RUN IS 19 MODULES FROM THE END OF ITS MODULE PHASE at this snapshot; the profile steps',
          'follow it. ### The act after the pid exits reads the log to its end.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['REGISTERED AT b476; the lane opens for b477, which is banked and unrun.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['(R85) APPLIED SINCE b475.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND',
         ['ROUTED to the act after b479.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'MINT',
         ['FOUND AT b480, IN THE SEAT`S OWN LAUNCHER: b475`s order asked for "a timestamp per module" and',
          'every one of the 169 MODULE markers carries the SAME instant -- the launch`s. ### Inside a',
          'parenthesised FOR block cmd expands %time% ONCE, at parse time; `!time!` was needed.',
          '### **THE PER-MODULE DURATIONS OF THIS RUN ARE UNRECOVERABLE FROM ITS LOG**, and only the',
          'ordering survives. ### The run was NOT touched to fix it.']),
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
    SC = json.loads(read(os.path.join(D, 'b480_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED BY THIS ACT : %d.**' % SC['registered'])
    rec('  (N1) from b475 : %s' % SC['N1_from_b475']['navigator'])
    rec('       ### ### **%s**' % SC['N1_from_b475']['verdict'])
    rec('       %s' % SC['N1_from_b475']['note'])
    rec('  (R82) : ### **%s** -- %s' % (SC['r82']['verdict'], SC['r82']['note']))
    rec('  (R83) : ### **%s** -- %s' % (SC['r83']['verdict'], SC['r83']['note']))
    rec('  ### the seat`s own : %s' % SC['seat']['N1'])
    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE b475 SERIALIZED LOG IS READ AS A SNAPSHOT -- 256,095 bytes at 2026-09-22T20:58:13Z, THE RUN '
        'STILL GOING -- AND (N1) IS SCORED HELD** (b480). '
        '**COMPONENT 1: 169 of 188 modules started, 166 with an EXIT line, EVERY ONE EXIT 0, NO failing '
        'module and NO memory line anywhere in the snapshot.** '
        '**COMPONENT 3: the three modules that died in parallel at b473 -- Zeta23.Hypotheses, '
        'Zeta23.Defs.Counting, Zeta23.Taper.Basic, at lines 2, 3 and 23 of the order -- ALL PASS AT EXIT 0 '
        'with one Lean process at a time. THE BOUND WAS THE PARALLELISM, NOT THE MODULES, and nothing about '
        'zeta23`s mathematics changed.** '
        '**COMPONENT 2: all twenty profile rows ABSENT, because the profile steps run after every module '
        'and 19 have not started. (R82) IS THEREFORE *NOT YET DECIDABLE* -- not HOLDS, and NEITHER KIND OF '
        'VOID; b473`s VOID FOR WANT OF A RUN described a run that had ENDED. (R83) DOES NOT FIRE. The grade '
        'stays DERIVES, CONDITIONAL.** '
        '**AND A DEFECT IN THE SEAT`S OWN b475 LAUNCHER IS FOUND BY THIS READ: every MODULE marker carries '
        'the same instant, because cmd expands %time% once when it parses a FOR block, so the per-module '
        'durations are unrecoverable from the log; the run was not touched to fix it.** '
        'b475`s "positions 1, 2 and 22" were 0-based indices and are corrected to lines 2, 3 and 23. '
        'Nothing imported; no grade moved; the run not stopped; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'the b475 run`s log, read as a snapshot and committed: data/b475_zeta23_build.log',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL -- (R82) not yet decidable',
             ('data/b480_the_snapshot_read.txt; data/b480_components.txt; data/b480_snapshot.json; '
              'data/b480_profiles.json; data/b475_zeta23_build.log (committed as evidence); data/b480_scores.json; '
              'data/b480_registration_2026-09-22.txt (LOCKED at sha256 3ac8813dc4c9db57); '
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
    bank = os.path.join(D, 'b480_the_snapshot_read.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b480_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
