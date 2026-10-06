# -*- coding: utf-8 -*-
"""test_chain_page_b632.py -- THE TEST OF THE PROVENANCE CELL b632 ADDED TO tools/chain_page.py, under (R242)(3) and the author's answer
before b632's seal (relay data/b632_author_answers.txt, prompt 2).

### Every input is read at its own pin (OPEN_TRAILS, the test-pin line of b632): the ζ list and probe of b630 (relay data/b630_nodes_zeta.txt,
### data/b630_probe_out.txt) and the table at relay af38a0c3 are given to the generator by swapping its table reader; nothing else of the
### generator is swapped. At that pin no Correspondence row of the ζ page is graded by the rule (b630's rule rows are the list's nodes), so
### ONE ROW IS PLANTED: the first Correspondence name the unplanted page prints, its provenance set to rule in the swapped rows alone.
### (1) every Correspondence row the swapped rows grade by the rule -- the planted one -- carries "; provenance: rule" in its tier cell;
### (2) no Correspondence row graded by ledger cells carries it;
### (3) the page with the mark struck is the page generated from the same rows with their provenance removed, byte for byte -- the edit
###   adds the mark and nothing else;
### (4) the marks counted equal the rule rows in the Correspondence, and there is at least one.
### Usage: python tools/test_chain_page_b632.py
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PIN = 'af38a0c3'
D = os.path.join(ROOT, 'data')
MARK = '; provenance: rule'


def rows_at_pin(strip=False, planted=None):
    t = json.loads(subprocess.run(['git', '-C', ROOT, 'show', '%s:data/terminal_table.json' % PIN], capture_output=True).stdout.decode('utf-8'))
    out = {r['name']: dict(r) for r in t.get('rows', []) if r.get('repo') == 'SIDE-explicit-formula'}
    if planted in out:
        out[planted]['provenance'] = 'rule'
    if strip:
        for r in out.values():
            r.pop('provenance', None)
    return out


def corr_of(pg):
    out = {}
    for l in pg.split('\n'):
        m = re.match(r'^\| `([^`]+)` \| [^|]+ \| ([A-Z][A-Z-]*) \| (.*) \|$', l)
        if m:
            out[m.group(1)] = m.group(3)
    return out


def page(strip, planted=None):
    real = C.record_rows
    C.record_rows = lambda: rows_at_pin(strip, planted)
    try:
        rc, pg, _m, log = C.build(os.path.join(D, 'b630_nodes_zeta.txt'), tempfile.mkdtemp(), os.path.join(D, 'b630_probe_out.txt'))
    finally:
        C.record_rows = real
    return rc, pg or '', log


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-112s %s' % (label, 'PASS' if cond else '### FAIL'))

    rcu, pu, _l = page(False)
    planted = sorted(corr_of(pu))[:1]
    planted = planted[0] if planted else None
    rows = rows_at_pin(False, planted)
    rc1, p1, log1 = page(False, planted)
    rc0, p0, log0 = page(True, planted)
    corr = corr_of(p1)
    rule = [n for n in corr if (rows.get(n) or {}).get('provenance') == 'rule']
    print('  ### the planted row: %s ; the unplanted page carries the mark %d times' % (planted, pu.count(MARK)))
    cell = [n for n in corr if (rows.get(n) or {}).get('provenance') == 'cell']
    want('(1) every rule-graded Correspondence row carries the mark (%d rows; exits %s %s)' % (len(rule), rc1, rc0),
         rc1 == 0 and rc0 == 0 and bool(rule) and all(corr[n].endswith(MARK) for n in rule))
    want('(2) no cell-graded Correspondence row carries it (%d rows)' % len(cell), bool(cell) and not any(MARK in corr[n] for n in cell))
    want('(3) the page with the mark struck is the page from the same rows without provenance, byte for byte',
         rc1 == 0 and rc0 == 0 and p1.replace(MARK, '') == p0 and p1 != p0)
    want('(4) the marks counted (%d) equal the rule rows in the Correspondence (%d)' % (p1.count(MARK), len(rule)), p1.count(MARK) == len(rule) > 0)
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
