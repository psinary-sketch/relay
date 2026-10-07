# -*- coding: utf-8 -*-
"""test_terminal_table_b637.py -- THE TEST OF tools/terminal_table.py's UPSTREAM EXCLUSION, (R247)(2), written at b637.

### (1) a kernel row the elaborated reader found in a module outside the kernel's roots: the upstream mark, the grade —, the kind upstream,
###     the provenance none, its grade and provenance before the exclusion kept in UPSTREAM;
### (2) a kernel row whose statement the generator's resolver finds in no file of the kernel and which the reader typed nowhere: the same;
### (3) a kernel row the reader typed in the kernel's own roots keeps its grade and provenance, no kind;
### (4) a row of a kernel the reader has not read, its statement unresolved: no kind, UNGRADED at none, as before;
### (5) the committed table at relay f3a2f6b2, every row passed through provenance(): the rows the upstream mark reached there and the five
###     Mathlib names (completedRiemannZeta₀_one, riemannZeta₀, riemannZeta₀_one, riemannZeta₁, riemannZeta₁_one) take the kind, and no other.
### The planted bank is written into a fresh temporary directory, its path printed; nothing of the table's files is written.
### Usage: python tools/test_terminal_table_b637.py
"""
import copy
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)
K = 'SIDE-explicit-formula'
PIN = 'f3a2f6b2'
FIVE = ('completedRiemannZeta₀_one', 'riemannZeta₀', 'riemannZeta₀_one', 'riemannZeta₁', 'riemannZeta₁_one')
BANK = NL.join(['### a planted elaborated-types bank (b637)', '',
                '### MODULE Mathlib/Planted/Up -- exit 0',
                'DECL Nat.up KIND theorem HEADER 1 TOTAL 1', 'MODULE Mathlib/Planted/Up Mathlib.Planted.Up', 'BINDER explicit n : ℕ',
                'CONCL n + 0 = n', 'END', '',
                '### MODULE SIDEExplicitFormula/Planted -- exit 0',
                'DECL K.own KIND theorem HEADER 1 TOTAL 1', 'MODULE SIDEExplicitFormula/Planted SIDEExplicitFormula.Planted',
                'BINDER explicit n : ℕ', 'CONCL n = n', 'END', ''])


def row(repo, name, statement, state):
    return dict(repo=repo, name=name, grade='UNGRADED', grade_cells=[], statement=statement, statement_state=state)


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-110s %s' % (label, 'PASS' if cond else '### FAIL'))

    d = tempfile.mkdtemp()
    bank = os.path.join(d, 'elab_b637.txt')
    open(bank, 'w', encoding='utf-8', newline=NL).write(BANK)
    print('  planted bank: %s' % bank)
    rows = [row(K, 'Nat.up', None, 'UNRESOLVED'), row(K, 'Planted.mathlibOnly', None, 'UNRESOLVED'),
            row(K, 'K.own', 'theorem own (n : ℕ) : n = n', 'RESOLVED'), row('SIDE-other', 'Other.unresolved', None, 'UNRESOLVED')]
    TT.UPSTREAM[:] = []
    TT.provenance(rows, set(), elab_path=bank)
    by = {(r['repo'], r['name']): r for r in rows}
    u = by[(K, 'Nat.up')]
    up_kept = dict(((x[0], x[1]), (x[2], x[3])) for x in TT.UPSTREAM)
    want('(1) the upstream mark`s row: %s at %s, kind %s, before the exclusion %s' % (u['grade'], u['provenance'], u.get('kind'), up_kept.get((K, 'Nat.up'))),
         (u['grade'], u['provenance'], u.get('kind'), u.get('mark')) == ('—', 'none', 'upstream', 'upstream') and up_kept.get((K, 'Nat.up')) == ('DERIVES', 'rule-elab'))
    m = by[(K, 'Planted.mathlibOnly')]
    want('(2) a kernel row no file declares and the reader typed nowhere: %s at %s, kind %s' % (m['grade'], m['provenance'], m.get('kind')),
         (m['grade'], m['provenance'], m.get('kind')) == ('—', 'none', 'upstream'))
    o = by[(K, 'K.own')]
    want('(3) a kernel row typed in its own roots: %s at %s, kind %s' % (o['grade'], o['provenance'], o.get('kind')),
         (o['grade'], o['provenance'], o.get('kind')) == ('DERIVES', 'rule', None) and o.get('mark') is None)
    x = by[('SIDE-other', 'Other.unresolved')]
    want('(4) another kernel`s unresolved row: %s at %s, kind %s' % (x['grade'], x['provenance'], x.get('kind')),
         (x['grade'], x['provenance'], x.get('kind')) == ('UNGRADED', 'none', None))
    T = json.loads(subprocess.run(['git', '-C', ROOT, 'show', '%s:data/terminal_table.json' % PIN], capture_output=True).stdout.decode('utf-8'))['rows']
    want_up = set((r['repo'], r['name']) for r in T if r.get('mark') == 'upstream') | set((K, n) for n in FIVE)
    R = copy.deepcopy(T)
    for r in R:
        if not r.get('grade_cells'):
            r['grade'], r['provenance'] = 'UNGRADED', 'none'
        r.pop('mark', None)
    TT._ELAB.clear()
    TT.UPSTREAM[:] = []
    TT.provenance(R, set())
    got_up = set((r['repo'], r['name']) for r in R if r.get('kind') == 'upstream')
    want('(5) the table at %s: %d rows take the kind, the %d the mark reached and the five Mathlib names (%d); others %s' % (
        PIN, len(got_up), len(want_up) - len(FIVE), len(want_up), sorted(got_up - want_up)[:5]),
         got_up == want_up and len(want_up) == 32 and all(r['grade'] == '—' and r['provenance'] == 'none' for r in R if r.get('kind') == 'upstream'))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
