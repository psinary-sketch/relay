# -*- coding: utf-8 -*-
"""test_terminal_table_b635.py -- THE TEST OF tools/terminal_table.py's b635 EDIT, under (R245)(2)-(3) and the author's two answers before
b635's seal: the elaborated reading grades SIDE-explicit-formula; the upstream mark; the re-point map; the retire list.

### Planted rows and a planted types bank in a fresh temporary directory; no bank of relay is read or written.
###   (1) an elaborated header is graded by the shared rule: a premise binder reads INTERFACES, its module returned;
###   (2) a kernel row no cell grades, textual DERIVES and elaborated INTERFACES, reads INTERFACES at provenance rule-elab;
###   (3) a kernel row whose two readings agree reads at provenance rule;
###   (4) a kernel row whose textual reading defers (a type_of% conclusion) takes the elaborated grade at rule-elab;
###   (5) a kernel row whose declaration lives outside the kernel's roots carries the mark upstream; one inside does not;
###   (6) a row of another kernel takes the textual reading, the bank unread for it;
###   (7) a kernel row with no statement that the reader typed takes the elaborated grade at rule-elab;
###   (8) a row a ledger cell grades keeps its cell's grade at provenance cell;
###   (9) the re-point map moves a name to its new name and the retire list removes a row;
###   (10) a textual reading that defers with no elaborated type leaves the row at provenance none, no DEFERRED grade written.
### Usage: python tools/test_terminal_table_b635.py
"""
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = chr(10)
K = TT.ELAB_KERNEL

BANK = NL.join([
    'DECL K.prem KIND theorem HEADER 2 TOTAL 2', 'MODULE K.prem SIDEExplicitFormula.Planted',
    'BINDER explicit n : ℕ', 'BINDER explicit hP : PlantedPremiseB635 0', 'CONCL n = n', 'END',
    'DECL K.agree KIND theorem HEADER 1 TOTAL 1', 'MODULE K.agree SIDEExplicitFormula.Planted', 'BINDER explicit n : ℕ', 'CONCL n + 0 = n', 'END',
    'DECL K.defer KIND theorem HEADER 1 TOTAL 1', 'MODULE K.defer SIDEExplicitFormula.Planted', 'BINDER explicit n : ℕ', 'CONCL n = n', 'END',
    'DECL Nat.up KIND theorem HEADER 2 TOTAL 2', 'MODULE Nat.up Mathlib.Planted', 'BINDER explicit n : ℕ', 'BINDER explicit m : ℕ', 'CONCL n + m = m + n', 'END',
    'DECL K.cell KIND theorem HEADER 1 TOTAL 1', 'MODULE K.cell SIDEExplicitFormula.Planted', 'BINDER explicit hQ : PlantedPremiseB635 0', 'CONCL True', 'END', ''])


def row(repo, name, statement=None, cells=None, grade='UNGRADED'):
    return dict(repo=repo, name=name, statement=statement, grade=grade, grade_cells=cells or [], conflict=None, mark=None)


def main():
    d = tempfile.mkdtemp()
    bank = os.path.join(d, 'elab_types.txt')
    open(bank, 'w', encoding='utf-8', newline=NL).write(BANK)
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    r1 = TT.elab_reading('K.prem', bank)
    want('(1) the elaborated header graded by the rule: %s, module %s' % r1, r1 == ('INTERFACES', 'SIDEExplicitFormula.Planted'))
    rows = [row(K, 'K.prem', 'theorem prem (n : ℕ) : n = n'),
            row(K, 'K.agree', 'theorem agree (n : ℕ) : n + 0 = n'),
            row(K, 'K.defer', 'theorem defer (n : ℕ) : type_of% (@Other.thing n)'),
            row(K, 'Nat.up', None),
            row('SIDE-other', 'K.prem', 'theorem prem (n : ℕ) : n = n'),
            row(K, 'K.cell', 'theorem cell (hQ : PlantedPremiseB635 0) : True', cells=[dict(grade='DERIVES')], grade='DERIVES'),
            row(K, 'K.nodefer', 'theorem nodefer (n : ℕ) : type_of% (@Other.thing n)')]
    TT.provenance(rows, set(), elab_path=bank)
    by = {(r['repo'], r['name']): r for r in rows}
    p = by[(K, 'K.prem')]
    want('(2) textual DERIVES, elaborated INTERFACES: read %s at %s' % (p['grade'], p['provenance']), (p['grade'], p['provenance']) == ('INTERFACES', 'rule-elab'))
    a = by[(K, 'K.agree')]
    want('(3) the two readings agreeing: read %s at %s' % (a['grade'], a['provenance']), (a['grade'], a['provenance']) == ('DERIVES', 'rule'))
    f = by[(K, 'K.defer')]
    want('(4) the textual reading deferring: read %s at %s' % (f['grade'], f['provenance']), (f['grade'], f['provenance']) == ('DERIVES', 'rule-elab'))
    u = by[(K, 'Nat.up')]
    want('(5) upstream marked %s ; a kernel row marked %s' % (u.get('mark'), p.get('mark')), u.get('mark') == 'upstream' and p.get('mark') is None)
    o = by[('SIDE-other', 'K.prem')]
    want('(6) another kernel`s row: read %s at %s' % (o['grade'], o['provenance']), (o['grade'], o['provenance']) == ('DERIVES', 'rule'))
    want('(7) a statement-less kernel row the reader typed: read %s at %s' % (u['grade'], u['provenance']), (u['grade'], u['provenance']) == ('DERIVES', 'rule-elab'))
    c = by[(K, 'K.cell')]
    want('(8) a cell-graded row: read %s at %s' % (c['grade'], c['provenance']), (c['grade'], c['provenance']) == ('DERIVES', 'cell'))
    pop = {'old.name': {'HEAD': 1}, 'keep': {'HEAD': 2}, 'gone.ns': {'HEAD': 3}}
    pop, moved, gone = TT.repoint_and_retire(K, pop, rmap={(K, 'old.name'): 'old.nameℝ_full'}, rset={(K, 'gone.ns')})
    want('(9) re-pointed %s ; retired %s ; the population %s' % (moved, gone, sorted(pop)),
         moved == [('old.name', 'old.nameℝ_full')] and gone == ['gone.ns'] and sorted(pop) == ['keep', 'old.nameℝ_full'])
    nd = by[(K, 'K.nodefer')]
    want('(10) deferring with no elaborated type: read %s at %s' % (nd['grade'], nd['provenance']), (nd['grade'], nd['provenance']) == ('UNGRADED', 'none'))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
