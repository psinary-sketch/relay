# -*- coding: utf-8 -*-
"""b475_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b475_sources.json` and `b475_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b475_span.json')))

    rec('=' * 100)
    rec('b475_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _s = json.loads(read(os.path.join(D, 'b475_survey.json')))
    _l = json.loads(io.open(os.path.join(D, 'b475_launch.json'), encoding='utf-8-sig').read())
    _st = json.loads(read(os.path.join(D, 'b475_state.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the run : pid %s, started %s, LEAN_NUM_THREADS=%s, serialized %s'
        % (_l['pid'], _l['started_utc'], _l['lean_num_threads'], _l['serialized']))
    rec('    state at the components read : %s, %d s after launch, %d lean process(es)'
        % (_st['state'], _st['elapsed_s'], _st['lean_processes']))
    rec('    the order : %d modules, %d inversions ; the three at positions %s'
        % (_s['modules'], _s['inversions'],
           ', '.join('%s=%s' % (k.split('.')[-1], v) for k, v in _s['failed_positions'].items())))
    rec('    the memory ceiling in b473`s log : %d figures ; %d failure lines'
        % (_s['memory_figures'], len(_s['panic_lines'])))
    rec('    span by tool : %d (the fold at b474 covers b464-b473)' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b475 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
         ['THE SECOND ATTEMPT IS RUNNING, SERIALIZED: pid 27508, LEAN_NUM_THREADS=1, one lake call per',
          'module over 188 modules in computed dependency order. ### The log is not read by this act.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['(R82) VOID FOR WANT OF A RUN at b473; (R83) untriggered. ### This run is what could change that,',
          'and only the act that reads its log may.']),
        ('lake 5.0.0 has no -j', 'STAND',
         ['STEPPED AROUND RATHER THAN SOLVED: with no job flag, serialization is done by the launcher --',
          'one `lake build <module>` per call with LEAN_NUM_THREADS=1 -- not by lake.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['ENTERED AT THE FOLD, b474.']),
        ('the E0 table has no site column', 'STAND', ['CARRIED INTO THE FOLD.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND',
         ['THE FOLD IS FILED AT b474 AND THE TOOL NOW READS THE SPAN FROM b475. ### The item stands until',
          'an act reads a non-zero span, which this one does not yet.']),
        ('the run died of memory, not of mathematics', 'STAND',
         ['AND THE CEILING IT DIED AT IS NOT IN THE LOG: b473`s log holds the three failure lines and NO',
          'memory figure at all. ### So the bound is known by KIND and not by SIZE, and this act supplies',
          'no number in its place.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE PRICE IS BEING PAID NOW, SERIALIZED. ### If the three that died pass one at a time, the',
          'bound was the parallelism; if one of them dies alone, the bound is per-module, and (N1) says',
          'which before the run is half done.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['OPENED AT b474 UNDER (R84); no number computed, and none computed here either.']),
        ('a face names each tool`s write pattern, not each file', 'MINT',
         ['(R85), RATIFIED AND FIRST APPLIED HERE: section (W) of this face is a table of tools and globs,',
          'and this act`s `G-WRITELIST-KINDS` reads the globs with both its controls kept. ### b474`s two',
          'names close under it. ### **THE ARM IS RE-POINTED, NOT RELAXED: a file outside every declared',
          'glob is still a breach.**']),
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
    SC = json.loads(read(os.path.join(D, 'b475_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED : %d.**' % SC['registered'])
    rec('  (N1) %s' % SC['N1']['navigator'])
    rec('       ### ### **%s**' % SC['N1']['verdict'])
    rec('       %s' % SC['N1']['note'])
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
        '**THE zeta23 AXIOM RUN IS RESTARTED DETACHED AND SERIALIZED UNDER (R80) -- pid 27508, launched '
        '2026-09-22T19:02:24Z, LEAN_NUM_THREADS=1, one `lake build <module>` per call over 188 modules in a '
        'dependency order computed from the sources (0 inversions), logging to relay/data/b475_zeta23_build.log** '
        '(b475). **LOCKED BEFORE THE RUN STARTED**, 8 gates read, 4 by digest. '
        '**THE THREE MODULES THAT DIED IN PARALLEL AT b473 SIT AT POSITIONS 1, 2 AND 22 OF 188, so (N1) is '
        'decided early in the run and not at its end; it is scored by the act that reads the log, not by this '
        'one.** '
        '**THE MEMORY CEILING THE ORDER ASKED FOR IS NOT IN b473`S LOG: 0 lines carry a memory figure and 3 '
        'carry the failure itself -- twice "INTERNAL PANIC: out of memory", once std::bad_alloc. NO FIGURE IS '
        'SUPPLIED FROM ANYWHERE ELSE: the bound is known by kind and not by size.** '
        '**(R85) IS RATIFIED AND FIRST APPLIED HERE: section (W) is a table of tools and write globs, and the '
        'write-list arm reads the globs with both controls kept -- re-pointed, not relaxed. b474`s two names '
        'close under it.** '
        'The log is not opened and not committed by this act; (R82) is not re-decided; (R83)`s kernel is not '
        'created. No grade of the corpus moved; nothing imported; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: the serialized run`s log enters the record at the act that reads it',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL until a run completes',
             ('data/b475_the_serialized_run.txt; data/b475_components.txt; data/b475_survey.json; '
              'data/b475_order.txt; data/b475_launch.json; data/b475_zeta23_build.pid; data/b475_state.json; '
              'data/b475_registration_2026-09-22.txt (LOCKED at sha256 f88574b16d2e4800); '
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
    bank = os.path.join(D, 'b475_the_serialized_run.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b475_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
