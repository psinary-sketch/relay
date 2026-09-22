# -*- coding: utf-8 -*-
"""b477_components.py -- THE RUN, AS LAUNCHED, AND WHAT IT WILL DO. ### Run after the seal
### (sha256 `2a7a7a5438804046...`, locked 2026-09-22T21:14:45Z) and after the launch.
### ### **THE GRAM LOG IS NOT OPENED; the process table and the file system are read.**
"""
import datetime
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
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


S = json.loads(read(os.path.join(D, 'b477_survey.json')))
LA = json.loads(io.open(os.path.join(D, 'b477_launch.json'), encoding='utf-8-sig').read())


def state(label):
    pid = int(LA['pid'])
    tl = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/FO', 'CSV', '/NH'],
                        capture_output=True, text=True, errors='replace').stdout.strip()
    alive = tl.startswith('"') and ('"%d"' % pid) in tl
    now = datetime.datetime.now(datetime.timezone.utc)
    t0 = datetime.datetime.strptime(LA['started_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(
        tzinfo=datetime.timezone.utc)
    log, ent = os.path.join(D, 'b477_gram.log'), os.path.join(D, 'b477_entries.jsonl')
    nent = 0
    if os.path.exists(ent):
        nent = sum(1 for _ in io.open(ent, encoding='utf-8', errors='replace'))
    return dict(label=label, pid=pid, state='RUNNING' if alive else 'EXITED',
                read_utc=now.strftime('%Y-%m-%dT%H:%M:%SZ'), launched=LA['started_utc'],
                elapsed_s=int((now - t0).total_seconds()),
                log_bytes=os.path.getsize(log) if os.path.exists(log) else -1,
                entries_banked=nent,
                how='process table and file sizes only; neither the log nor the entries file was read')


def main():
    st = state('components')
    rec('=' * 104)
    rec('COMPONENT 1 -- THE GRAM RUN, AS LAUNCHED.')
    rec('=' * 104)
    rec('    ### ### **PID : %s**   (relay/data/b477_gram.pid)' % LA['pid'])
    rec('    ### ### **LOG : %s** -- NOT OPENED BY THIS ACT' % LA['log'])
    rec('    entries file : %s -- appended and flushed as each entry lands' % LA['entries'])
    rec('    started      : %s   (the face locked at 2026-09-22T21:14:45Z)' % LA['started_utc'])
    rec('    launcher     : %s -- Start-Process, hidden, detached' % LA['launcher'])
    rec('    runner       : %s -- PYTHON, so every line carries its own real timestamp' % LA['runner'])
    rec('    ### ### **STATE AT THIS READING : %s ; %d s after launch ; log %d bytes ; entries banked %d**'
        % (st['state'], st['elapsed_s'], st['log_bytes'], st['entries_banked']))
    rec('    (%s)' % st['how'])

    rec('')
    rec('  ### (1a) WHAT THE RUN DOES, IN ITS OWN ORDER.')
    rec('    1. the seeds, once per cell, for both families')
    rec('    2. ### **THE DIAGONAL AT EVERY CELL** -- G(a,a) by the chain`s own autocorrelation, against')
    rec('       b321`s banked W (aim plane) and b437`s sum_v (ladder), within the floor 1.49e-08, with')
    rec('       ### **THE ZERO SIDE AND trunc_bound PRINTED BESIDE EACH**')
    rec('       ### ### **A MISMATCH BEYOND THE FLOOR HALTS THE RUN BEFORE ANY OFF-DIAGONAL ENTRY.**')
    rec('    3. the aim plane`s off-diagonals (%d), then the ladder`s (%d)'
        % (S['aim'] * (S['aim'] - 1) // 2, S['ladder'] * (S['ladder'] - 1) // 2))
    rec('    4. the control`s own diagonal, on the Epstein chain')
    rec('    ### every entry appended to b477_entries.jsonl as it lands, and flushed')

    rec('')
    rec('  ### (1b) THE BUILDER, AND ITS CONTROL -- FROM THE SURVEY, BEFORE THE LOCK.')
    c = S['control']
    rec('    cross(g, g) against the chain`s own autocorrelation(g) at a = 1.5 :')
    rec('      max |window difference| : %.3e' % c['window_diff'])
    rec('      W from the chain        : %+.12f' % c['W_autocorr'])
    rec('      W from the builder      : %+.12f' % c['W_cross'])
    rec('      ### ### **|DIFFERENCE| %.3e ; WITHIN THE FLOOR %.2e : %s**'
        % (c['diff'], c['floor'], c['within']))
    rec('    ### ### **THE BUILDER REDUCES TO THE CHAIN`S OWN CONSTRUCTION ON THE DIAGONAL.** ### The')
    rec('    ### chain is NOT edited; f_ab is built outside it and supplied to it, as (R86) requires.')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE CONTROL`S SIDE, STATED AS THE ORDER REQUIRES.')
    rec('=' * 104)
    rec('    zeta`s entry    : b321_window.channels -> W = PR - A, the places sum')
    rec('    the control`s   : ### **b325_epstein.channels_q -- THE EPSTEIN OBJECT`S OWN FINITE CHANNEL')
    rec('      AND ITS OWN ARCHIMEDEAN KERNEL**, returning %s' % S['control_keys'])
    rec('    ### ### **THERE IS NO ZERO SIDE IN THAT RETURN.** ### So the control`s Gram is a')
    rec('    ### PLACES-SIDE GRAM, and ### **ITS VERDICT IS SCOPED TO THE PLACES SIDE**: it can show what')
    rec('    ### the Epstein places side does under this family, and it cannot show what a summed Epstein')
    rec('    ### zero channel would.')
    rec('    one sample entry from the survey : G(%g, %g) = %+.12f ; the control at the same f_ab = %+.12f'
        % (S['sample']['a'], S['sample']['b'], S['sample']['G'], S['sample']['control_places']))

    rec('')
    rec('=' * 104)
    rec('COMPONENT 3 -- (R87)`S ORIENTATION, CARRIED INTO WHAT THE NEXT ACT WILL READ.')
    rec('=' * 104)
    rec('    W = PR - A ; Sum_v W_v(f) = -Z ; ### **THE SIGNATURE IS READ ON -G.**')
    rec('    under RH : -G positive semidefinite ; an off-line pair contributes a hyperbolic plane to -G')
    rec('    ### ### **(F2) HALTS ON A POSITIVE EIGENVALUE OF G** beyond the floor, for zeta')
    rec('    ### ### **(N2) AND (N3) REFER TO THE LARGEST EIGENVALUE OF G**')
    rec('    the amendment is appended BELOW b476`s lock block, and b476`s seal still reads SEAL INTACT.')
    rec('    ### ### **NO EIGENVALUE IS TAKEN BY THIS ACT. ### NO FALSIFIER IS SCORED BY THIS ACT.**')
    rec('    ### The act after the pid exits reads the log, forms the Gram at each nested family size,')
    rec('    ### prints the solver`s residual beside every eigenvalue, reads an eigenvalue below the')
    rec('    ### floor in magnitude as zero, and scores (F1)-(F3) and (N1)-(N3) in this orientation.')

    io.open(os.path.join(D, 'b477_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b477_state.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(st, indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
