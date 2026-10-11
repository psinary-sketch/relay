# -*- coding: utf-8 -*-
"""test_axiom_claim.py -- THE PLANTED TEST OF tools/axiom_claim.py, under (R259)(2)(b).

### A scratch file and a scratch print index, written here and drawn from no bank: (1) a docstring claiming the standard three over a
### declaration whose print names sorryAx is CONTRADICTED; (2) the true claim over a declaration printed at the standard three is VERIFIED;
### (3) a claim over a declaration with no banked print is UNVERIFIABLE; (4) the module header claiming the standard three over the file is
### CONTRADICTED by the two declarations printed outside it (sorryAx; Lean.ofReduceBool); (5) a sentence naming an axiom with no profile is a MENTION, unscored; (6) "no axioms beyond the
### standard three" reads STD3, not EMPTY; (7) "without native_decide" over a print carrying Lean.ofReduceBool is CONTRADICTED; (8) a
### compiler print wrapped over two lines is read whole; (9) b642's `Name: [...]` line is read; (10) a different declaration sharing the
### last component is not matched; (11) a `/-!` block after the head is out of scope; (12) an AxiomCheck module's header covers the
### declarations it prints.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import axiom_claim as A   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STD3 = frozenset(['propext', 'Classical.choice', 'Quot.sound'])
TEXT = '''/-! Planted module. Every theorem here is at the standard three. -/
import Mathlib
namespace P
/-- Proved at the standard three [propext, Classical.choice, Quot.sound]. -/
theorem bad : True := trivial
/-- Proved at the standard three. -/
theorem good : True := trivial
/-- Depends on no axioms. -/
theorem unbanked : True := trivial
/-- This is not an axiom of the theory; it is a definition. -/
def mentioned : Nat := 0
/-- No axioms beyond the standard three. -/
theorem beyond : True := trivial
/-- Checked without native_decide. -/
theorem native : True := trivial
/-- Depends on no axioms. -/
theorem other.leaf : True := trivial
/-! A later section: these are zero axioms. -/
theorem late : True := trivial
end P
'''
IDX = {'P.bad': (frozenset(['propext', 'sorryAx']), 'scratch', 1), 'P.good': (STD3, 'scratch', 1), 'P.mentioned': (frozenset(), 'scratch', 1),
       'P.beyond': (STD3, 'scratch', 1), 'P.native': (frozenset(['propext', 'Lean.ofReduceBool']), 'scratch', 1),
       'Q.leaf': (STD3, 'scratch', 1), 'P.late': (STD3, 'scratch', 1)}


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    rows = A.classify_text('PLANTED', 'P.lean', TEXT, IDX)
    by = {}
    for r in rows:
        by.setdefault((r['block'], r['line']), []).append(r)
    v = lambda line, blk='docstring': [r['verdict'] for r in by.get((blk, line), [])]   # noqa: E731
    want('(1) the standard three claimed over a print naming sorryAx: CONTRADICTED %s' % v(4), v(4) == ['CONTRADICTED'])
    want('(2) the true claim over a declaration printed at the standard three: VERIFIED %s' % v(6), v(6) == ['VERIFIED'])
    want('(3) a claim over a declaration with no banked print: UNVERIFIABLE %s' % v(8), v(8) == ['UNVERIFIABLE'])
    hdr = by.get(('header', 1), [])
    want('(4) the module header over the file: CONTRADICTED by the two declarations outside the three %s' % [
        (r['verdict'], [x['decl'] for x in r['contradicted']]) for r in hdr],
         any(r['verdict'] == 'CONTRADICTED' and [x['decl'] for x in r['contradicted']] == ['P.bad', 'P.native'] for r in hdr))
    want('(5) an axiom word with no profile stated: MENTION %s' % v(10), v(10) == ['MENTION'])
    b = by.get(('docstring', 12), [])
    want('(6) "no axioms beyond the standard three" reads STD3 and VERIFIES %s' % [(r['kind'], r['verdict']) for r in b],
         [(r['kind'], r['verdict']) for r in b] == [('STD3', 'VERIFIED')])
    want('(7) "without native_decide" over a print carrying Lean.ofReduceBool: CONTRADICTED %s' % v(14), v(14) == ['CONTRADICTED'])
    pr = A.prints_in_text("'X.y' depends on axioms: [propext,\n Classical.choice, Quot.sound]\n'X.z' does not depend on any axioms\n")
    want('(8) a wrapped print read whole, an empty one read empty: %s' % pr, pr == {'X.y': STD3, 'X.z': frozenset()})
    b6 = dict((m.group(1), A._set(m.group(2))) for m in A.B642_LINE.finditer('  SIDEExplicitFormula.Keiper.binomBeta: [propext, Quot.sound]\n'))
    want('(9) b642`s `Name: [...]` line read: %s' % b6, b6 == {'SIDEExplicitFormula.Keiper.binomBeta': frozenset(['propext', 'Quot.sound'])})
    want('(10) P.other.leaf not matched to Q.leaf, a different declaration: UNVERIFIABLE %s' % v(16), v(16) == ['UNVERIFIABLE'])
    want('(11) a `/-!` block after the head: OUT OF SCOPE %s' % [r['verdict'] for r in by.get(('section', 18), [])],
         [r['verdict'] for r in by.get(('section', 18), [])] == ['OUT OF SCOPE'])
    chk = '/-! Each is expected to reduce to the standard base (`propext`, `Classical.choice`, `Quot.sound`), with no `sorryAx`. -/\n' \
          'import P\n#print axioms P.good\n#print axioms P.bad\n'
    rc = A.classify_text('PLANTED', 'AxiomCheckP.lean', chk, IDX)
    want('(12) a module declaring nothing covers what it prints: CONTRADICTED by P.bad %s' % [
        (r['verdict'], r['covered'], [x['decl'] for x in r['contradicted']]) for r in rc],
         [(r['verdict'], r['covered'], [x['decl'] for x in r['contradicted']]) for r in rc] == [('CONTRADICTED', 2, ['P.bad'])])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
