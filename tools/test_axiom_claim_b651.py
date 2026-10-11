# -*- coding: utf-8 -*-
"""test_axiom_claim_b651.py -- THE PLANTED TEST OF tools/axiom_claim.py's re-binding, under (R261)(4) and the author's answer before the seal.

### Planted files and a planted print index, written here and drawn from no bank; the kernel map built by the resolver's own kernel_map.
###   (1) b649's row 2 in shape: a docstring whose parenthesis says "no axioms" of a module of the kernel (TraceSilence) is re-bound to that
###       module's declarations (BOUND-TO) and graded by their prints -- here printed empty, so VERIFIED, not CONTRADICTED;
###   (2) b649's row 5 in shape: "the same conclusion ... with the finiteness assumption deleted ... depends on no axioms" reads UNBOUND;
###   (3) a docstring saying "no axioms" of its own declaration, which uses an axiom, is CONTRADICTED, not re-bound;
###   (4) a docstring naming another declaration as its subject ("`Q.Other.uses` depends on no axioms"), which uses an axiom, is re-bound and
###       CONTRADICTED -- the case that keeps the rule from hiding a real claim behind another name;
###   (5) b649's row 1 in shape: a parenthesis holding only axiom names, "(no Classical.choice)", re-binds nothing.
###   (6) KLSilence :86 in shape: "(kept axiom-free; the List-semantics ...)" -- the name sits in another clause; the claim stays bound.
###   (7) Voice7 :124 in shape: a backticked name just before the parenthesis, "`Q.Other.uses`** (axiom-free, DERIVES; ...)", is the
###       object the parenthesis glosses: re-bound to it, an all-capital word never taken for a name.
### Usage: python tools/test_axiom_claim_b651.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import axiom_claim as A   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STD3 = frozenset(['propext', 'Classical.choice', 'Quot.sound'])
HOST = '''import Mathlib
namespace P
/-- The general-`p` core: the banked `p = 2, 3` instances (TraceSilence, no axioms) are its shadows. -/
theorem cell : True := trivial
/-- A theorem with a variant noted.
    The same conclusion, from the same two hypotheses with the finiteness assumption deleted and no imports at all, compiles and depends on no axioms. -/
theorem ost : True := trivial
/-- Depends on no axioms. -/
theorem own : True := trivial
/-- `Q.Other.uses` depends on no axioms. -/
theorem host : True := trivial
/-- Proved by decide, axioms {propext, Quot.sound} (no Classical.choice). -/
theorem one : True := trivial
/-- the count as its own recursion (kept axiom-free; the List-semantics identification is below) -/
theorem kept : True := trivial
/-- it was compiled as `Q.Other.uses`** (axiom-free, DERIVES; a note) -/
theorem gloss : True := trivial
end P
'''
TRACE = '''namespace Q.TraceSilence
theorem inst2 : True := trivial
theorem inst3 : True := trivial
end Q.TraceSilence
'''
OTHER = '''namespace Q.Other
theorem uses : True := trivial
end Q.Other
'''
IDX = {'P.cell': (STD3, 'scratch', 1), 'P.ost': (frozenset(['propext', 'Quot.sound']), 'scratch', 1), 'P.own': (STD3, 'scratch', 1),
       'P.host': (frozenset(), 'scratch', 1), 'P.one': (STD3, 'scratch', 1), 'P.kept': (frozenset(), 'scratch', 1), 'P.gloss': (STD3, 'scratch', 1),
       'Q.TraceSilence.inst2': (frozenset(), 'scratch', 1), 'Q.TraceSilence.inst3': (frozenset(), 'scratch', 1),
       'Q.Other.uses': (frozenset(['propext']), 'scratch', 1)}


def main():
    kmap = A.kernel_map([('P.lean', HOST), ('Q/TraceSilence.lean', TRACE), ('Q/Other.lean', OTHER)])
    rows = A.classify_text('PLANTED', 'P.lean', HOST, IDX, None, kmap)
    by = {}
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    line = dict((n, HOST.split('\n').index(next(l for l in HOST.split('\n') if l.startswith('theorem %s ' % n))) + 1) for n in
                ('cell', 'ost', 'own', 'host', 'one', 'kept', 'gloss'))
    head = dict((n, max(k for k in by if k < line[n])) for n in line if any(k < line[n] for k in by))
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    r1 = [r for r in by.get(head['cell'], []) if r['kind'] != 'MENTION']
    want('(1) row 2`s shape: re-bound to the module TraceSilence and graded by its prints, VERIFIED',
         len(r1) == 1 and r1[0].get('bound_to') == 'TraceSilence' and r1[0]['verdict'] == 'VERIFIED'
         and sorted(r1[0]['bound_names']) == ['Q.TraceSilence.inst2', 'Q.TraceSilence.inst3'])
    r2 = [r for r in by.get(head['ost'], []) if r['kind'] != 'MENTION']
    want('(2) row 5`s shape: the hypothetical variant reads UNBOUND', len(r2) == 1 and r2[0]['verdict'] == 'UNBOUND')
    r3 = by.get(head['own'], [])
    want('(3) "no axioms" said of its own declaration, which uses an axiom: CONTRADICTED, not re-bound',
         len(r3) == 1 and r3[0]['verdict'] == 'CONTRADICTED' and not r3[0].get('bound_to'))
    r4 = by.get(head['host'], [])
    want('(4) another declaration as subject, which uses an axiom: re-bound and CONTRADICTED',
         len(r4) == 1 and r4[0].get('bound_to') == 'Q.Other.uses' and r4[0]['verdict'] == 'CONTRADICTED')
    r5 = by.get(head['one'], [])
    want('(5) row 1`s shape: a parenthesis of axiom names re-binds nothing, the claim CONTRADICTED on its own declaration',
         len(r5) >= 1 and all(not r.get('bound_to') for r in r5) and any(r['verdict'] == 'CONTRADICTED' for r in r5))
    r6 = by.get(head['kept'], [])
    want('(6) KLSilence`s shape: the name in another clause of the parenthesis; the claim stays bound, VERIFIED on its own declaration',
         len(r6) == 1 and not r6[0].get('bound_to') and r6[0]['verdict'] == 'VERIFIED')
    r7 = by.get(head['gloss'], [])
    want('(7) Voice7`s shape: the backticked name before the parenthesis takes the claim; re-bound and CONTRADICTED by its print',
         len(r7) == 1 and r7[0].get('bound_to') == 'Q.Other.uses' and r7[0]['verdict'] == 'CONTRADICTED')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
