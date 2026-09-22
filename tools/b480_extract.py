# -*- coding: utf-8 -*-
"""b480_extract.py -- THE SURVEY. ### The b475 run's STATE and the log's METADATA, and what b473's two
### components require of a log. ### **THE LOG'S CONTENTS ARE NOT READ HERE** -- registration before
### components; Component 1 reads it after the seal.
"""
import datetime
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
LOG = os.path.join(D, 'b475_zeta23_build.log')
NL = chr(10)
L, MISSES = [], []

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


def main():
    rec('=' * 104)
    rec('b480 -- THE SURVEY. ### THE LOG`S CONTENTS ARE NOT READ HERE.')
    rec('=' * 104)

    rec('')
    rec('(P1) THE RUN`S STATE, FROM THE PROCESS TABLE.')
    rec('-' * 104)
    la = json.loads(io.open(os.path.join(D, 'b475_launch.json'), encoding='utf-8-sig').read())
    pid = int(la['pid'])
    tl = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/FO', 'CSV', '/NH'],
                        capture_output=True, text=True, errors='replace').stdout.strip()
    alive = tl.startswith('"') and ('"%d"' % pid) in tl
    counts = {}
    for n in ('lean', 'lake', 'cmd'):
        out = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq %s.exe' % n, '/FO', 'CSV', '/NH'],
                             capture_output=True, text=True, errors='replace').stdout
        counts[n] = sum(1 for l in out.splitlines() if l.startswith('"%s.exe"' % n))
    now = datetime.datetime.now(datetime.timezone.utc)
    t0 = datetime.datetime.strptime(la['started_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(
        tzinfo=datetime.timezone.utc)
    size = os.path.getsize(LOG)
    mt = datetime.datetime.fromtimestamp(os.path.getmtime(LOG), datetime.timezone.utc)
    rec('    pid %d : ### **%s**' % (pid, 'RUNNING' if alive else 'EXITED'))
    rec('    launched %s ; read %s ; elapsed %d s'
        % (la['started_utc'], now.strftime('%Y-%m-%dT%H:%M:%SZ'), int((now - t0).total_seconds())))
    rec('    processes now : lean %d ; lake %d ; cmd %d' % (counts['lean'], counts['lake'], counts['cmd']))
    rec('    log : %d bytes ; last write %s ; %d s before this read'
        % (size, mt.strftime('%Y-%m-%dT%H:%M:%SZ'), int((now - mt).total_seconds())))
    rec('    ### ### **THE RUN IS STILL GOING, AND AT MOST ONE lean PROCESS IS ALIVE -- WHICH IS WHAT')
    rec('    ### THE SERIALIZATION WAS FOR.**' if alive and counts['lean'] <= 1 else
        '    ### the run`s state is as printed above.')

    rec('')
    rec('(P2) WHAT THE ORDER ASKS, AND WHAT THE RUN`S STATE ALLOWS.')
    rec('-' * 104)
    rec('    the order : run b473`s Components 1 and 2 against this log ; score (N1) ; decide (R82) ;')
    rec('      (R83) fires or does not.')
    rec('    (R80), quoted from b471_ferry.txt: *"The run`s output enters the record only when the seat')
    rec('      reads the log at its end."* ### And b475`s own face: *"the act that follows the pid`s')
    rec('      exit reads it to its end"*.')
    rec('    ### ### **THE PID HAS NOT EXITED, SO THE LOG HAS NO END TO READ. ### WHAT THIS ACT CAN')
    rec('    ### HONESTLY DO IS READ IT AS A SNAPSHOT, AT A NAMED BYTE COUNT AND A NAMED TIME.**')
    rec('    ### What a snapshot CAN decide: (N1) -- the three modules that died in parallel sit at')
    rec('    ### positions 1, 2 and 22 of 188, so their exit lines are early and are either in the')
    rec('    ### snapshot or not.')
    rec('    ### What a snapshot CANNOT decide: (R82) -- the three profiles are printed by the steps')
    rec('    ### that run AFTER all 188 modules, so a log that has not reached them carries neither a')
    rec('    ### profile nor a failure. ### **THAT IS NEITHER `HOLDS` NOR EITHER KIND OF `VOID`.**')

    rec('')
    rec('(P3) b473`S TWO COMPONENTS, AND THE SHAPES THEY READ.')
    rec('-' * 104)
    c473 = read(os.path.join(D, 'b473_components.txt'))
    rec('    b473`s Component 1 read : the launcher`s markers and EXIT lines, the wall time from the')
    rec('      log`s own timestamps, every failing module with its stderr, and the last forty lines.')
    rec('    b473`s Component 2 read : the seventeen Challenge theorems and the three (R82) names, each')
    rec('      row carrying its `#print axioms` line verbatim or ABSENT.')
    rec('    b473_components.txt on disk : %d bytes ; carries "VOID FOR WANT OF A RUN" : %s'
        % (len(c473), 'VOID FOR WANT OF A RUN' in c473))
    names = json.loads(read(os.path.join(D, 'b473_survey.json')) or '{}')
    rec('    the seventeen + three, from b473`s own survey : %d + %d'
        % (len(names.get('seventeen', [])), len(names.get('ef', []))))
    if len(names.get('seventeen', [])) != 17 or len(names.get('ef', [])) != 3:
        MISSES.append(('b473_survey.json', 'name lists'))

    rec('')
    rec('(P4) THE ORDER FILE THE RUN IS WALKING.')
    rec('-' * 104)
    order = [l for l in read(os.path.join(D, 'b475_order.txt')).split(NL) if l.strip()]
    rec('    b475_order.txt : %d modules ; first three %s ; last %s'
        % (len(order), ', '.join(order[:3]), order[-1]))
    for m in ('Zeta23.Hypotheses', 'Zeta23.Defs.Counting', 'Zeta23.Taper.Basic'):
        rec('      %-24s position %d of %d' % (m, order.index(m) + 1, len(order)))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b480_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(pid=pid, alive=alive, state='RUNNING' if alive else 'EXITED',
                   processes=counts, read_utc=now.strftime('%Y-%m-%dT%H:%M:%SZ'),
                   launched=la['started_utc'], elapsed_s=int((now - t0).total_seconds()),
                   log_bytes=size, log_last_write=mt.strftime('%Y-%m-%dT%H:%M:%SZ'),
                   order_modules=len(order),
                   positions={m: order.index(m) + 1 for m in
                              ('Zeta23.Hypotheses', 'Zeta23.Defs.Counting', 'Zeta23.Taper.Basic')},
                   seventeen=names.get('seventeen', []), ef=names.get('ef', []), misses=MISSES),
              io.open(os.path.join(D, 'b480_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
