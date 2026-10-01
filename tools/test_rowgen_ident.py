# -*- coding: utf-8 -*-
"""test_rowgen_ident.py -- THE TEST OF rowgen.py`s IDENTIFIER READ, (R181)(3), written at b571.

### (1) row 421 of SIDE-global-section`s CORRESPONDENCE.md, read live, now yields its terminal
###     `SIDEExplicitFormula.GRHWeil.norm_logDeriv_Gammaℝ_le_wide` through rowgen.diff (b570`s banked record of it);
### (2) the old ASCII pattern (rowgen.py :135 at relay 96daad63, quoted here) reads no cited name of that terminal on the same row;
### (3) an ASCII name is still read (row 422, `norm_logDeriv_gammaFactor_le`);
### (4) a backticked statement span with a colon is not read as a name;
### (5) Lean`s own boundaries: λ (U+03BB), Π (U+03A0) and Σ (U+03A3) are not letter-like, so a name carrying one is not read
###     whole; a subscript (₁) and a prime continue a name and may not begin one; α, ℝ and 𝔽 begin and continue a name.
### Usage: python tools/test_rowgen_ident.py
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
import rowgen as RG   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORR = 'D:/SIDE-global-section/CORRESPONDENCE.md'
NS = 'SIDEExplicitFormula.GRHWeil.'
OLD = r'`([A-Za-z_][A-Za-z0-9_\.]*)`'


def full(s):
    return re.fullmatch(RG.LEAN_NAME, s) is not None


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    recs = json.load(io.open(os.path.join(ROOT, 'data', 'b570_e0.json'), encoding='utf-8'))['rowgen']
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    lines = io.open(CORR, encoding='utf-8').read().replace(chr(13), '').split(chr(10))
    r421 = [l for l in lines if l.startswith('| 421 |')]
    r422 = [l for l in lines if l.startswith('| 422 |')]
    out = RG.diff(recs, chr(10).join(r421))
    want('(1) row 421 read: rowgen.diff yields %s' % out, [x[0] for x in out] == [NS + 'norm_logDeriv_Gammaℝ_le_wide'])
    old = [c for c in re.findall(OLD, ' '.join(r421)) if 'Gamma' in c]
    want('(2) the old ASCII pattern reads no cited Gammaℝ name on row 421 (read %s)' % old, old == [])
    out2 = RG.diff(recs, chr(10).join(r422))
    want('(3) an ASCII name still read: row 422 yields %s' % out2, [x[0] for x in out2] == [NS + 'norm_logDeriv_gammaFactor_le'])
    span = re.findall('`(' + RG.LEAN_NAME + ')`', '`SIDEExplicitFormula.GRHWeil.foo : ∀ x, x = x`')
    want('(4) a statement span with a colon is not read as a name (read %s)' % span, span == [])
    want('(5a) λ, Π, Σ are not letter-like: fλ, fΠ, fΣ not names', not any(full(x) for x in ('fλ', 'fΠ', 'fΣ')))
    want('(5b) a subscript and a prime continue a name: x₁, h₂', full('x₁') and full("h'") and full('h₂'))
    want('(5c) a subscript may not begin a name: ₁x', not full('₁x'))
    want('(5d) α, ℝ, 𝔽 begin and continue a name: αβ, ℝx, 𝔽_q, Gammaℝ', all(full(x) for x in ('αβ', 'ℝx', '𝔽_q', 'Gammaℝ')))
    want('(5e) a hierarchical name with a Unicode component: A.Gammaℝ.b', full('A.Gammaℝ.b') and not full('A..b'))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
