# -*- coding: utf-8 -*-
"""test_build_watch_b647.py -- THE TEST OF THE WATCHDOG ON THE PROCESS TREE, tools/build_watch.py, W-ORD-HOLD-FOOTPRINT acted under
(R257)(5), written at b647.

### "A child process allocating past the driver's own footprint, the tree's peak expected above the driver's." Each case runs the watchdog in
### the foreground over a planted python driver (no lean), its log and peaks bank in a temporary directory; nothing in relay is written.
###   (1) THE PLANTED TREE: the driver starts a grandchild that holds 400 MB for several samples; the tree's peak reads above the driver's own
###       peak by more than 300 MB, the EXIT line prints the tree's peak beside the host's low, the peaks bank carries the attempt's row;
###   (2) THE CONTROL: a driver with no child -- the tree's peak within 50 MB of the driver's, no stop, exit 0;
###   (3) the hold rule unchanged: b644's planted test (tools/test_build_watch_b644.py) run whole and passing.
### Usage: python tools/test_build_watch_b647.py
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, 'tools', 'build_watch.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

GRANDCHILD = "import time; b = bytearray(400 * 1024 * 1024); b[::4096] = b'x' * len(b[::4096]); time.sleep(12)"
DRIVER = "import subprocess,sys; p = subprocess.Popen([sys.executable, '-c', %r]); p.wait()" % GRANDCHILD
ALONE = "import time; time.sleep(6)"


def run(code):
    d = tempfile.mkdtemp()
    log, peaks = os.path.join(d, 'w.log'), os.path.join(d, 'peaks.json')
    r = subprocess.run([sys.executable, W, '--hold', '0', '--interval', '2', '--module', 'Planted.Tree', '--peaks', peaks, d, log,
                        sys.executable, '-c', code], capture_output=True, text=True, timeout=300)
    text = open(log, encoding='utf-8').read() if os.path.exists(log) else ''
    rows = json.load(open(peaks, encoding='utf-8'))['rows'] if os.path.exists(peaks) else []
    return r.returncode, text, rows


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  (%d) %-118s %s' % (len(res), label, 'PASS' if cond else '### FAIL'))

    rc, text, rows = run(DRIVER)
    ex = [l for l in text.split('\n') if l.startswith('### EXIT')]
    m = re.search(r' peak (\d+) MB low (\d+) MB free \d+ MB tree peak (\d+) MB', ex[0]) if ex else None
    dp, tp = (int(m.group(1)), int(m.group(3))) if m else (-1, -1)
    want('THE PLANTED TREE: exit %d ; driver peak %d MB ; tree peak %d MB ; host low %s MB ; peaks rows %s' % (
         rc, dp, tp, m.group(2) if m else '?', [(r['driver_peak'], r['tree_peak'], r['host_low']) for r in rows]),
         rc == 0 and bool(m) and tp > dp + 300 and len(rows) == 1 and rows[0]['tree_peak'] == tp and rows[0]['driver_peak'] == dp
         and rows[0]['module'] == 'Planted.Tree' and 'tree working set' in text)
    rc, text, rows = run(ALONE)
    ex = [l for l in text.split('\n') if l.startswith('### EXIT')]
    m = re.search(r' peak (\d+) MB low (\d+) MB free \d+ MB tree peak (\d+) MB', ex[0]) if ex else None
    dp, tp = (int(m.group(1)), int(m.group(3))) if m else (-1, -1)
    want('THE CONTROL, no child: exit %d ; driver peak %d MB ; tree peak %d MB ; stopped %s' % (rc, dp, tp, 'STOPPED' in text),
         rc == 0 and bool(m) and 0 <= tp - dp <= 50 and 'STOPPED' not in text and len(rows) == 1)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_build_watch_b644.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=600)
    last = [l for l in r.stdout.split('\n') if l.startswith('### ###')]
    want('THE HOLD RULE UNCHANGED: tools/test_build_watch_b644.py exit %d ; %s' % (r.returncode, last[-1:] or 'no verdict line'),
         r.returncode == 0 and bool(last) and 'PASS' in last[-1])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
