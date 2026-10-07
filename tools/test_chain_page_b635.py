# -*- coding: utf-8 -*-
"""test_chain_page_b635.py -- THE TEST OF b635's EDIT TO tools/chain_page.py's PROVENANCE CELL, under the author's answer after b635's
seal (the page-mark prompt, relay data/b635_author_answers.txt): a row at any provenance but the ledger cells' prints it as itself.

### Inputs read at b632's test pin as test_chain_page_b632.py reads them (the ζ list and probe of b630, the table at relay af38a0c3), the
### generator's table reader swapped and nothing else. TWO ROWS ARE PLANTED: the first Correspondence name the unplanted page prints at
### provenance "rule-elab", the second at a made-up value "planted-future".
### (1) the rule-elab row's tier cell ends "; provenance: rule-elab";
### (2) the made-up value prints as itself, "; provenance: planted-future";
### (3) no cell-graded row carries a provenance mark;
### (4) the page with the two marks struck is the page from the same rows with the two plants removed, byte for byte.
### Usage: python tools/test_chain_page_b635.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import test_chain_page_b632 as T2   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def page(plants):
    real = T2.rows_at_pin

    def rows(strip=False, planted=None):
        out = real(strip, None)
        for n, v in plants.items():
            if n in out:
                out[n]['provenance'] = v
        return out
    T2.rows_at_pin = rows
    try:
        return T2.page(False)
    finally:
        T2.rows_at_pin = real


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-112s %s' % (label, 'PASS' if cond else '### FAIL'))

    rcu, pu, _l = page({})
    names = sorted(T2.corr_of(pu))[:2]
    plants = {names[0]: 'rule-elab', names[1]: 'planted-future'}
    print('  ### planted: %s' % plants)
    rc1, p1, _l1 = page(plants)
    corr = T2.corr_of(p1)
    rows = T2.rows_at_pin(False, None)
    cell = [n for n in corr if (rows.get(n) or {}).get('provenance') == 'cell' and n not in plants]
    want('(1) the rule-elab row: %s' % corr.get(names[0]), rc1 == 0 and corr.get(names[0], '').endswith('; provenance: rule-elab'))
    want('(2) a made-up value as itself: %s' % corr.get(names[1]), corr.get(names[1], '').endswith('; provenance: planted-future'))
    want('(3) no cell-graded row carries a mark (%d rows)' % len(cell), bool(cell) and not any('; provenance: ' in corr[n] for n in cell))
    struck = p1.replace('; provenance: rule-elab', '').replace('; provenance: planted-future', '')
    want('(4) the page with the two marks struck is the unplanted page, byte for byte', rcu == 0 and struck == pu and p1 != pu)
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
