# -*- coding: utf-8 -*-
"""test_terminal_table_b636.py -- THE TEST OF tools/terminal_table.py's b636 EDIT, under (R246)(4): the elaborated reading extended to
SIDE-structural-error-correction -- its rows no ledger cell grades take the rule's grade of their elaborated type, provenance rule-elab where
the textual reading differs or defers, else rule.

### Planted rows and planted types banks in a fresh temporary directory, and one read of the reader's own bank; nothing is written.
###   (1) a row of the kernel, textual DERIVES and elaborated INTERFACES, reads INTERFACES at provenance rule-elab;
###   (2) a row of the kernel whose two readings agree reads at provenance rule;
###   (3) a row of the kernel with no statement that the reader typed (a def) reads DEF at provenance rule-elab;
###   (4) the upstream mark by the kernel's own roots: a declaration in SIDEStructuralErrorCorrection is not marked, one elsewhere is;
###   (5) a row of the explicit-formula kernel reads that kernel's bank and not this one's, the same name planted in both;
###   (6) a cell-graded row of the kernel keeps its cell's grade at provenance cell;
###   (7) the generator's bank for the kernel is the reader's, relay data/b636_elab_sec.txt, and reads d_eff_eq_five DERIVES and
###       DeAlignment.Line.Proper DEF from it.
### Usage: python tools/test_terminal_table_b636.py
"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = chr(10)
SEC, EF = 'SIDE-structural-error-correction', TT.ELAB_KERNEL

BANK_SEC = NL.join([
    'DECL S.prem KIND theorem HEADER 2 TOTAL 2', 'MODULE S.prem SIDEStructuralErrorCorrection.Planted',
    'BINDER explicit n : ℕ', 'BINDER explicit hP : PlantedPremiseB636 0', 'CONCL n = n', 'END',
    'DECL S.agree KIND theorem HEADER 1 TOTAL 1', 'BINDER explicit n : ℕ', 'CONCL n + 0 = n', 'END',
    'DECL S.defn KIND def HEADER 1 TOTAL 1', 'BINDER explicit n : ℕ', 'CONCL Prop', 'END',
    'DECL S.up KIND theorem HEADER 1 TOTAL 1', 'MODULE S.up Mathlib.Planted', 'BINDER explicit n : ℕ', 'CONCL n = n', 'END',
    'DECL Both.name KIND theorem HEADER 1 TOTAL 1', 'BINDER explicit hQ : PlantedPremiseB636 1', 'CONCL True', 'END',
    'DECL S.cell KIND theorem HEADER 1 TOTAL 1', 'BINDER explicit hQ : PlantedPremiseB636 2', 'CONCL True', 'END', ''])
BANK_EF = NL.join(['DECL Both.name KIND theorem HEADER 1 TOTAL 1', 'BINDER explicit n : ℕ', 'CONCL n = n', 'END', ''])


def row(repo, name, statement=None, cells=None, grade='UNGRADED'):
    return dict(repo=repo, name=name, statement=statement, grade=grade, grade_cells=cells or [], conflict=None, mark=None)


def main():
    d = tempfile.mkdtemp()
    bs, be = os.path.join(d, 'sec_types.txt'), os.path.join(d, 'ef_types.txt')
    open(bs, 'w', encoding='utf-8', newline=NL).write(BANK_SEC)
    open(be, 'w', encoding='utf-8', newline=NL).write(BANK_EF)
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    rows = [row(SEC, 'S.prem', 'theorem prem (n : ℕ) : n = n'),
            row(SEC, 'S.agree', 'theorem agree (n : ℕ) : n + 0 = n'),
            row(SEC, 'S.defn', None),
            row(SEC, 'S.up', 'theorem up (n : ℕ) : n = n'),
            row(EF, 'Both.name', 'theorem name (n : ℕ) : n = n'),
            row(SEC, 'S.cell', 'theorem cell (hQ : PlantedPremiseB636 2) : True', cells=[dict(grade='DERIVES')], grade='DERIVES')]
    TT.provenance(rows, set(), elab_paths={SEC: bs, EF: be})
    by = {(r['repo'], r['name']): r for r in rows}
    p = by[(SEC, 'S.prem')]
    want('(1) textual DERIVES, elaborated INTERFACES: read %s at %s' % (p['grade'], p['provenance']), (p['grade'], p['provenance']) == ('INTERFACES', 'rule-elab'))
    a = by[(SEC, 'S.agree')]
    want('(2) the two readings agreeing: read %s at %s' % (a['grade'], a['provenance']), (a['grade'], a['provenance']) == ('DERIVES', 'rule'))
    f = by[(SEC, 'S.defn')]
    want('(3) a statement-less row the reader typed: read %s at %s' % (f['grade'], f['provenance']), (f['grade'], f['provenance']) == ('DEF', 'rule-elab'))
    u = by[(SEC, 'S.up')]
    want('(4) upstream marked %s ; a row in the kernel`s roots marked %s' % (u.get('mark'), p.get('mark')), u.get('mark') == 'upstream' and p.get('mark') is None)
    e = by[(EF, 'Both.name')]
    want('(5) the explicit-formula row reads its own bank: %s at %s' % (e['grade'], e['provenance']), (e['grade'], e['provenance']) == ('DERIVES', 'rule'))
    c = by[(SEC, 'S.cell')]
    want('(6) a cell-graded row: read %s at %s' % (c['grade'], c['provenance']), (c['grade'], c['provenance']) == ('DERIVES', 'cell'))
    r1 = TT.elab_reading('SIDEStructuralErrorCorrection.d_eff_eq_five', TT.ELAB_BANKS[SEC])
    r2 = TT.elab_reading('DeAlignment.Line.Proper', TT.ELAB_BANKS[SEC])
    want('(7) the reader`s bank %s: d_eff_eq_five %s ; Line.Proper %s' % (os.path.basename(TT.ELAB_BANKS[SEC]), r1, r2),
         os.path.basename(TT.ELAB_BANKS[SEC]) == 'b636_elab_sec.txt' and r1 is not None and r1[0] == 'DERIVES' and r2 is not None and r2[0] == 'DEF')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
