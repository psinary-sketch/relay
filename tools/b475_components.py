# -*- coding: utf-8 -*-
"""b475_components.py -- COMPONENTS 1 AND 2. ### Run after the seal (sha256 `f88574b16d2e4800...`,
### locked 2026-09-22T19:02:02Z) and after the detached launch.
### ### **THE NEW LOG IS NOT OPENED. ### b473'S LOG IS READ ONLY FOR THE THREE PANIC LINES IT ALREADY
### PUT ON THE RECORD.**
"""
import datetime
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
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


S = json.loads(read(os.path.join(D, 'b475_survey.json')))
LA = json.loads(io.open(os.path.join(D, 'b475_launch.json'), encoding='utf-8-sig').read())


def state(label):
    pid = int(LA['pid'])
    tl = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/FO', 'CSV', '/NH'],
                        capture_output=True, text=True, errors='replace').stdout.strip()
    alive = tl.startswith('"') and ('"%d"' % pid) in tl
    lean = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq lean.exe', '/FO', 'CSV', '/NH'],
                          capture_output=True, text=True, errors='replace').stdout
    now = datetime.datetime.now(datetime.timezone.utc)
    t0 = datetime.datetime.strptime(LA['started_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(
        tzinfo=datetime.timezone.utc)
    log = os.path.join(D, 'b475_zeta23_build.log')
    return dict(label=label, pid=pid, state='RUNNING' if alive else 'EXITED',
                read_utc=now.strftime('%Y-%m-%dT%H:%M:%SZ'), launched_utc=LA['started_utc'],
                elapsed_s=int((now - t0).total_seconds()),
                lean_processes=sum(1 for l in lean.splitlines() if l.startswith('"lean.exe"')),
                log_bytes=os.path.getsize(log) if os.path.exists(log) else -1,
                how='process table and file size only; the log was not opened')


def main():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE SERIALIZED DETACHED RUN, AS LAUNCHED.')
    rec('=' * 104)
    st = state('component1')
    rec('    pid              : %s   (relay/data/b475_zeta23_build.pid)' % LA['pid'])
    rec('    started          : %s   (the face locked at 2026-09-22T19:02:02Z)' % LA['started_utc'])
    rec('    launcher         : %s -- Start-Process, hidden, detached' % LA['launcher'])
    rec('    log              : %s' % LA['log'])
    rec('    LEAN_NUM_THREADS : %s ; serialized : %s' % (LA['lean_num_threads'], LA['serialized']))
    rec('    order file       : %s -- %d modules, read by the launcher, not typed into it'
        % (LA['order_file'], S['modules']))
    rec('    steps, in order  : one `lake build <module>` per module, each with its own timestamp and')
    rec('                       exit code ; then `lake build Solution` ; then scripts\\PrintAxioms.lean')
    rec('                       as shipped ; then the seat`s named file for the three (R82) declarations')
    rec('    at launch        : the process was alive after 8 s and the log file existed')
    rec('    ### ### **STATE AT THIS READING : %s ; %d s after launch ; %d lean process(es) alive ;'
        % (st['state'], st['elapsed_s'], st['lean_processes']))
    rec('    ### log %d bytes** -- read from the process table and the file system, %s'
        % (st['log_bytes'], st['how']))
    rec('    ### ### **AT MOST ONE LEAN PROCESS IS THE POINT OF THIS RUN**, and the count above is the')
    rec('    ### first evidence of it; the act that reads the log will see the rest.')
    rec('    ### ### **THE LOG IS NOT OPENED BY THIS ACT AND IS NOT COMMITTED BY IT.**')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- WHAT THE RECORD KNOWS ABOUT THE BOUND.')
    rec('=' * 104)
    rec('  ### (2a) THE MEMORY CEILING, ASKED FOR AND NOT IN THE LOG.')
    rec('    lines in b473`s log carrying a memory FIGURE : %d' % S['memory_figures'])
    rec('    lines carrying the failure ITSELF : %d, quoted verbatim:' % len(S['panic_lines']))
    for p in S['panic_lines']:
        rec('      | %s' % p)
    rec('    ### ### **NO MEMORY CEILING IS RECORDED IN THAT LOG, SO NONE IS PRINTED HERE.** ### The')
    rec('    ### order`s own condition is *"if the log holds it"*, and it does not. ### **NO FIGURE IS')
    rec('    ### TAKEN FROM THE MACHINE, FROM A LATER RUN, OR FROM ANYWHERE ELSE.**')
    rec('    ### What the next reader has instead of a ceiling: the failure`s KIND (an allocation that')
    rec('    ### could not be served, twice as Lean`s own panic and once as the C++ allocator`s), the')
    rec('    ### PARALLELISM it happened under (lake`s own workers, LEAN_NUM_THREADS unset), and the')
    rec('    ### fact that this run moves exactly that one variable.')

    rec('')
    rec('  ### (2b) THE ORDER, AND WHERE THE THREE SIT IN IT.')
    rec('    modules in the order : %d ; inversions (a module before one of its own imports) : %d'
        % (S['modules'], S['inversions']))
    for m, p in S['failed_positions'].items():
        rec('      %-24s position %s of %d' % (m, p, S['modules']))
    rec('    ### ### **ALL THREE SIT IN THE FIRST TWENTY-TWO**, so (N1) is decided early in the run and')
    rec('    ### not at its end. ### The first five of the order: %s' % ', '.join(S['order'][:5]))

    rec('')
    rec('  ### (2c) WHAT IS HELD FIXED, SO THAT (N1) READS AS ONE VARIABLE.')
    rec('    fixed   : the clone at fbdc36bb, toolchain v4.33.0-rc2, Mathlib 51e6992e, the shipped')
    rec('              PrintAxioms.lean, and the three (R82) declarations in the seat`s scratchpad file')
    rec('    changed : LEAN_NUM_THREADS unset -> 1 ; one call for the library -> one call per module')
    rec('    ### ### **NOTHING IN THE CLONE IS EDITED; NOTHING IS COPIED, IMPORTED OR VENDORED.**')

    io.open(os.path.join(D, 'b475_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b475_state.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(st, indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
