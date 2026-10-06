# -*- coding: utf-8 -*-
"""test_chain_page_b630.py -- THE TEST OF THE PROBE HOLD, under (R240)(5), W-ORD-PROBE-HOLD.

### tools/chain_page.py's probe reads free memory before the lean call and refuses beneath the hold (since b568, relay 3b3152f4); b630
### makes it print the reading on its own output at every start. Here the reading is PLANTED by swapping the generator's free_mb, and the
### probe itself is swapped for a stub that records its call, so no lean process starts.
### (1)-(3) A LOW READING (1000 MB): the build exits 4; the probe is never called; the reading is printed with REFUSED.
### (4)-(6) A HIGH READING (99999 MB): the build passes the hold and calls the probe (the stub); the reading is printed with started; the
###   log carries the reading line as before.
### (7) THE HOLD is 2560 MB.
### The node list is relay data/b630_nodes_zeta.txt (pin v0.24); the kernel's checkout must be at its pin, as for every probe.
### Usage: python tools/test_chain_page_b630.py
"""
import contextlib
import io
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NODES = os.path.join(ROOT, 'data', 'b630_nodes_zeta.txt')


def run(reading):
    calls = []
    saved = (C.free_mb, C.run_probe)
    C.free_mb = lambda: reading
    C.run_probe = lambda d, text: (calls.append(1), (9, ''))[1]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc, page, meta, log = C.build(NODES, tempfile.mkdtemp(), None)
    finally:
        C.free_mb, C.run_probe = saved
    return rc, calls, buf.getvalue(), log or []


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    rc, calls, out, log = run(1000)
    want('(1) a planted reading of 1000 MB: the build exits 4 (read %s)' % rc, rc == 4)
    want('(2) and the probe is never called', calls == [])
    want('(3) and the reading is printed with REFUSED', 'chain_page: free memory before the lean call: 1000 MB (hold 2560) -- REFUSED' in out)
    rc, calls, out, log = run(99999)
    want('(4) a planted reading of 99999 MB: the build passes the hold and calls the probe (exit %s, calls %d)' % (rc, len(calls)), rc != 4 and calls == [1])
    want('(5) and the reading is printed with started', 'chain_page: free memory before the lean call: 99999 MB (hold 2560) -- started' in out)
    want('(6) and the log carries the reading line as before', 'free memory before the lean call: 99999 MB (hold 2560)' in log)
    want('(7) the hold is 2560 MB', C.HOLD_MB == 2560)
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
