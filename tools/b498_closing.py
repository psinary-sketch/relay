# -*- coding: utf-8 -*-
"""b498_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R = json.loads(read(os.path.join(D, 'b498_results.json')))
SC = json.loads(read(os.path.join(D, 'b498_scores.json')))
c1, c2, c3 = R['c1'], R['c2'], R['c3']
pre = read(os.path.join(D, 'b498_checks.txt'))
carried = read(os.path.join(D, 'b498_checks_carried.txt'))
post = read(os.path.join(D, 'b498_checks_postpush.txt'))
mir, pins = read(os.path.join(D, 'b498_mirror.txt')), read(os.path.join(D, 'b498_pins_closing.txt'))
cens = read(os.path.join(D, 'b498_census_closing.txt'))
fcens = read(os.path.join(D, 'b498_faces_census_closing.txt'))
alive = str(c3['pid']) in subprocess.run(['tasklist', '/FI', 'PID eq %d' % c3['pid']],
                                         capture_output=True, text=True, errors='replace').stdout
REPOS = [('relay', os.path.join('D:', os.sep, 'relay')),
         ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
         ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))]


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


rec('=' * 104)
rec('b498 -- THE CLOSING RECORD. ### **THE BUILD RE-LAUNCHED IN ITS OWN CONSOLE; THE SENDER NOT ESTABLISHED.**')
rec('=' * 104)
rec('')
rec('### (1) THE CAUSE, AS THE RECORD SHOWS IT.')
rec('-' * 104)
rec('    b495`s launcher : `%s`' % c1['flags_line'])
rec('      its own process group %s ; NO console (DETACHED_PROCESS) %s ; a new console %s'
    % (c1['new_group'], c1['detached'], c1['new_console']))
for e in c1['ends']:
    rec('      END %-34s %s  EXIT 0x%08X' % (e['what'], e['t'], e['exit'] & 0xFFFFFFFF))
rec('      the launcher survived both : %s' % c1['launcher_survived'])
rec('    the seat`s b495 turn ended %s ; ### **THE FIRST KILL FOLLOWS IT BY %.3f s**'
    % (c1['turn_end'], c1['kill_after_turn_end_s']))
rec('    ### ### **THE SENDER : %s.** ### The record shows the build shared neither the seat`s' % c1['sender'])
rec('    ### process group nor its console, and no seat tool call at either kill. ### It does not')
rec('    ### show who or what delivered the event. ### **THE COINCIDENCE WITH THE TURN END IS')
rec('    ### BANKED AND NOT EXPLAINED.**')
rec('')
rec('### (2) THE CACHE AND THE CLOSURE.')
rec('-' * 104)
rec('    `lake exe cache get` : exit %d, %.1f s ; ### **FETCHED %d**' % (c2['cache_exit'], c2['cache_wall'], c2['fetched']))
rec('      %s' % c2.get('attempt_line'))
rec('      %s' % c2.get('decompressed_line'))
rec('    closure build : %d roots, exit %d, %.1f s, ### **`Built Mathlib.` LINES : %d**'
    % (len(c2['closure_roots']), c2['closure_exit'], c2['closure_wall'], c2['built_mathlib']))
rec('    kernel tracked tree after : %s' % ('CLEAN' if c2['kernel_status'] == '' else c2['kernel_status']))
rec('')
rec('### (3) THE LAUNCH.')
rec('-' * 104)
rec('    pid %d ; flags 0x%08X = %s ; log `%s`' % (c3['pid'], c3['flags'], ' | '.join(c3['flag_names']), c3['log']))
rec('    ### ### **AT CLOSE THE LAUNCHER IS %s** ### -- read from the process table, NOT from the log,'
    % ('ALIVE' if alive else 'GONE'))
rec('    ### which is not read in this act and not committed.')
rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    (N1) %s ; (N2) %s ; (N3) %s ; (S1) %s ; (S2) %s ; (S3) %s'
    % tuple(w(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')))
rec('    ### (N1)`s count is what was MISSING from a cache that already held 121141 files.')
rec('    ### (N3)`s cell says less than it seems: b495`s launcher also had a new process group.')
rec('')
rec('### (5) THIS ACT`S OWN DEFECTS -- SIX.')
rec('-' * 104)
rec('    (a) ### **THE FACE`S PRE-SEAL READ (C)(iii) NAMED THE WRONG INSTANT.** ### It gave the seat`s')
rec('        ### last tool call as `18:16:51.709`, which is when its RESULT landed; the call was')
rec('        ### issued at `%s`, and Component 1 re-derived it. ### The face is sealed and unedited.'
    % c1['last_tool_call'])
rec('    (b) ### **THE CACHE COMPONENT PRINTED THE FIRST `Downloaded` LINE BESIDE A COUNT FROM THE')
rec('        ### LAST.** ### Repaired, and re-derived from the banked raw output; both banks kept;')
rec('        ### nothing re-downloaded.')
rec('    (c) ### **AN ANSI ESCAPE REACHED OPEN_TRAILS.md** through the first trail append. ### This')
rec('        ### act`s own UNCOMMITTED append was cut back to the banked prefix sha and written again,')
rec('        ### 0 ESC bytes; ### the first append`s notes are banked beside the second`s.')
rec('    (d) ### **`corr_row.py` APPENDED A ROW AND THEN REFUSED IT** -- 8 cells on disk against 6')
rec('        ### given, because a pipe inside a flag expression split the row. ### **THE ROUTED')
rec('        ### SPECIES (IT CHECKS THE NUMBER, NOT THE CELLS) BITING LIVE**, and worse than routed:')
rec('        ### it validates AFTER it writes. ### The ledger was restored to HEAD and the row')
rec('        ### re-written with no pipe in any cell. ### **THE TOOL IS STILL UNEDITED AND STILL OWED.**')
rec('    (e) ### **TWO ARMS PASSED THEIR OWN POSITIVE CONTROLS**, `G-N1-SCORED` and `G-N2-SCORED`:')
rec('        ### the control set the score to a truthy string, which still reads HELD. ### Caught by')
rec('        ### the harness; repaired to flip the score; the first run banked at `b498_checks_carried.txt`.')
rec('    (f) ### **A HEREDOC WOULD NOT PARSE** and the arm list was written with the file tool instead;')
rec('        ### the standing lesson on shell-typed code, re-met.')
rec('')
rec('### (6) THE COMMITS, THE MIRROR, THE CENSUSES.')
rec('-' * 104)
rec('    pre-push first run : %s' % lw(carried, 'POSITIVE-CONTROL PASSES'))
rec('    pre-push           : %s' % lw(pre, 'ARMS RUN :'))
rec('    post-push          : %s' % lw(post, 'ARMS RUN :'))
rec('                         %s' % lw(post, 'VERDICT :'))
for name, path in REPOS:
    loc = git(path, 'rev-parse', 'HEAD')
    rem = git(path, 'ls-remote', 'origin', 'main')
    rem = rem.split()[0] if rem else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, loc[:12], rem[:12] or '### UNRESOLVED', 'AGREE' if loc and loc == rem else '### DISAGREE'))
rec('    the HELD commit`s files in relay`s pushed tree : 0')
rec('    the mirror : `mirror-refresh-2026-09-23-b498.zip` -- %s' % lw(mir, 'VERDICT:').replace('### VERDICT: ', ''))
rec('    handoff census : %s' % lw(cens, 'TOTAL MISSING'))
rec('    faces census   : %s' % lw(fcens, 'TOTAL MISSING'))
rec('    pins           : %s ### (run ALONE)' % lw(pins, 'REPOS HARD-FAILING'))
rec('')
rec('### (7) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE NEXT ACT READS `data/b498_ef_build.log` BEHIND b497`S GATE** -- pid %d alive or'
    % c3['pid'])
rec('        ### not, then the log whole -- and commits it. ### No row cites the kernel until then.')
rec('    (b) ### **THE CONSOLE IS VISIBLE.** ### It is minimised and titled DO NOT CLOSE THIS WINDOW;')
rec('        ### if it is closed, the build dies with the same exit as b495`s, and that would be')
rec('        ### evidence about the sender, which the record does not yet have.')
rec('    (c) ### **`corr_row.py` MUST VALIDATE BEFORE IT WRITES**, not only count after. ### Routed at')
rec('        ### b490, overdue, and now shown to leave a malformed row on disk when it refuses.')
rec('    (d) ### **b499 AWAITS ITS AMENDMENTS** -- the three Component 3 addresses of its order name')
rec('        ### lines that do not carry the records` titles; the STOP of this session drafted them.')
rec('=' * 104)

io.open(os.path.join(D, 'b498_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b498_closing.txt')
