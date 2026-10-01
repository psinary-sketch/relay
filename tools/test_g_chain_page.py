# -*- coding: utf-8 -*-
"""test_g_chain_page.py -- THE TEST OF THE ARM G-CHAIN-PAGE (tools/g_chain_page.py), written at b568 under (R178)(4).

### ### On a banked probe output (no lean call), the arm against a supplied "committed" page:
###   (1) the generated page itself               -> PASS
###   (2) the page with one sentence appended     -> FAIL (a sentence beyond the ceiling is caught)
###   (3) the page with one statement altered     -> FAIL, the first differing line named
###   (4) the regeneration made to fail           -> FAIL, never a skip (a node's block removed from the output)
###   (5) no committed page at all                -> FAIL
### Usage: python tools/test_g_chain_page.py <nodes.txt> <probe_out.txt> <page.md>
"""
import io
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import g_chain_page as G   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main(argv):
    nodes, out_path, page_path = argv[0], argv[1], argv[2]
    page = open(page_path, 'rb').read()
    tmp = tempfile.mkdtemp()
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-90s %s' % (label, 'PASS' if cond else '### FAIL'))

    r = G.arm(nodes, tmp, out_path, committed=page)
    want('(1) the generated page: the arm PASSES (regeneration exit %d)' % r['rc'], r['ok'])
    r = G.arm(nodes, tmp, out_path, committed=page + 'This line says what the chain means.\n'.encode('utf-8'))
    want('(2) one sentence appended: the arm FAILS (first differing line %s)' % r['first_diff'], not r['ok'])
    alt = page.replace('h2_sign ↔ RiemannHypothesis'.encode('utf-8'), 'h2_sign → RiemannHypothesis'.encode('utf-8'), 1)
    want('(3) mutation applied: one statement altered', alt != page)
    r = G.arm(nodes, tmp, out_path, committed=alt)
    want('(3) the arm FAILS and names a line (read %s)' % r['first_diff'], not r['ok'] and r['first_diff'] is not None)
    out = io.open(out_path, encoding='utf-8').read().replace('\r', '')
    v = 'SIDEExplicitFormula.B321.h2_sign_iff_rh'
    cut = re.sub(r'^@@BEGIN %s\n.*?^@@END %s\n' % (re.escape(v), re.escape(v)), '', out, flags=re.M | re.S)
    p = os.path.join(tmp, 'cut.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(cut)
    r = G.arm(nodes, tmp, p, committed=page)
    want('(4) the regeneration made to fail: the arm FAILS (regeneration exit %d)' % r['rc'], not r['ok'] and r['rc'] != 0)
    ok, at = G.compare(None, page)
    want('(5) no committed page: FAIL', not ok)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
