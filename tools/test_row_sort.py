# -*- coding: utf-8 -*-
"""test_row_sort.py -- THE TEST OF terminal_table.sort_corr_by_row, (R180)(2)(i), written at b570.

### (1) two CORRESPONDENCE cells written out of number order (row 419 at an earlier line than row 417) come back in number
###     order, in the places the CORRESPONDENCE cells held; (2) a non-CORRESPONDENCE cell between them keeps its place;
### (3) cells already in number order are unchanged; (4) a single cell is returned as given; (5) the live row map: rows
### 414-419 of SIDE-global-section`s CORRESPONDENCE.md are each present once and their numbers are not changed (the file is
### read, never written). Usage: python tools/test_row_sort.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    C = TT.CORR_LABEL
    lines = {417: 30, 418: 28, 419: 29}
    a = dict(ledger=C, line=29, grade='DERIVES', quote='419')
    f = dict(ledger='PLACE-papers/FINDINGS.md', line=5, grade='DERIVES', quote='F')
    b = dict(ledger=C, line=30, grade='DERIVES', quote='417')
    out = TT.sort_corr_by_row([a, f, b], lines)
    want('(1) out of number order (419 written before 417) -> 417 first (read %s)' % [c['quote'] for c in out],
         [c['quote'] for c in out] == ['417', 'F', '419'])
    want('(2) the FINDINGS cell between them keeps its place', out[1] is f)
    c1 = dict(ledger=C, line=28, grade='DERIVES', quote='418')
    out3 = TT.sort_corr_by_row([c1, a], lines)
    want('(3) already in number order -> unchanged', [c['quote'] for c in out3] == ['418', '419'])
    want('(4) a single cell -> as given', TT.sort_corr_by_row([a], lines) == [a])
    live = TT.corr_row_lines()
    want('(5) the live row map: rows 414-419 each present, numbers unchanged (%s)' % {n: live.get(n) for n in range(414, 420)},
         all(n in live for n in range(414, 420)) and len(set(live[n] for n in range(414, 420))) == 6)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
