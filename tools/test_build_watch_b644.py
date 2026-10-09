# -*- coding: utf-8 -*-
"""test_build_watch_b644.py -- THE TEST OF THE WATCHDOG STOP, tools/build_watch.py, W-ORD-WATCHDOG-STOP under (R254)(3), written at b644.

### "Tested on a planted run with the hold set above the host's free memory." Each case runs the watchdog in the foreground over a planted
### python child (no lean), its log and bank in a temporary directory; nothing in relay is written.
###   (1) THE PLANTED RUN: the hold set above the host's free memory (the start check set to 0 so it starts) -- the run is stopped by PID at
###       its first sample, retried once after the host is freed, stopped again, recorded RUN-BENEATH-HOLD with its low and the module name in
###       the log and the bank, exit 75; the child and its grandchild are gone;
###   (2) THE CONTROL: the hold at 0 -- the same watchdog lets a short child finish, exit 0, no stop, its low printed on EXIT;
###   (3) a host beneath the start check: both attempts REFUSED, nothing started, RUN-BENEATH-HOLD recorded, exit 75.
### Usage: python tools/test_build_watch_b644.py
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, 'tools', 'build_watch.py')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import build_watch as BW   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = 'b644plantedwatch'
CHILD = ("import subprocess,sys,time; subprocess.Popen([sys.executable,'-c','import time; time.sleep(90) # %s']); time.sleep(90) # %s"
         % (MARK, MARK))


def run(args):
    d = tempfile.mkdtemp()
    log, bank = os.path.join(d, 'w.log'), os.path.join(d, 'rbh.json')
    r = subprocess.run([sys.executable, W] + args[:-1] + ['--bank', bank, d, log] + args[-1], capture_output=True, text=True, timeout=300)
    text = open(log, encoding='utf-8').read() if os.path.exists(log) else ''
    rows = json.load(open(bank, encoding='utf-8'))['rows'] if os.path.exists(bank) else []
    return r.returncode, text, rows


def alive():
    return [p for p, v in BW.processes().items() if MARK in v[2] and 'test_build_watch' not in v[2]]


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  (%d) %-118s %s' % (len(res), label, 'PASS' if cond else '### FAIL'))

    fm = BW.free_mb()
    hold = fm + 1000000
    rc, text, rows = run(['--hold', str(hold), '--start-hold', '0', '--interval', '2', '--free-wait', '1', '--module', 'Planted.Module',
                          [sys.executable, '-c', CHILD]])
    stops = text.count('### STOPPED-BENEATH-HOLD')
    rbh = [l for l in text.split('\n') if l.startswith('### RUN-BENEATH-HOLD')]
    left = alive()
    want('THE PLANTED RUN (hold %d MB above free %d MB): exit %d ; stopped %d times ; %s ; bank rows %s ; tree lines %d ; left alive %s' % (
         hold, fm, rc, stops, rbh[:1], [(x['module'], x['low']) for x in rows], text.count('### STOP pid'), left),
         rc == 75 and stops == 2 and len(rbh) == 1 and 'module Planted.Module low ' in rbh[0] and len(rows) == 1 and
         rows[0]['module'] == 'Planted.Module' and isinstance(rows[0]['low'], int) and text.count('### STOP pid') >= 4 and
         text.count('### START attempt') == 2 and '### HOST FREED' in text and not left)
    rc, text, rows = run(['--hold', '0', '--interval', '1', '--module', 'Control.Module', [sys.executable, '-c', 'print("control ran")']])
    ex = [l for l in text.split('\n') if l.startswith('### EXIT')]
    want('THE CONTROL (hold 0): exit %d ; %s ; stopped %d ; bank rows %d' % (rc, ex, text.count('STOPPED-BENEATH-HOLD'), len(rows)),
         rc == 0 and 'control ran' in text and len(ex) == 1 and ' low ' in ex[0] and 'STOPPED' not in text and not rows)
    rc, text, rows = run(['--hold', str(hold), '--interval', '1', '--free-wait', '1', '--module', 'Refused.Module',
                          [sys.executable, '-c', 'print("must not run")']])
    want('a host beneath the start check: exit %d ; refused %d ; started %d ; %s' % (
         rc, text.count('### REFUSED'), text.count('### START'), [x['module'] for x in rows]),
         rc == 75 and text.count('### REFUSED') == 2 and '### START' not in text and 'must not run' not in text and
         [x['module'] for x in rows] == ['Refused.Module'])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
