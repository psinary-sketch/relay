# -*- coding: utf-8 -*-
"""b526_bump.py -- COMPONENT 2`S HALT, PROVED. ### `python tools/b526_bump.py`

### The kernel`s `plateau F L` is `⇑(plateauBump F L ...)`, a `ContDiffBump (0 : ℝ)`, whose function is
### `(someContDiffBumpBase ℝ).toFun (rOut / rIn) (rIn⁻¹ • x)`; `someContDiffBumpBase E := Nonempty.some hb.out` with
### `HasContDiffBump` a `Prop` class -- a base chosen by `Classical.choice`, fixed by the axioms and by NO definition. ###
### The kernel therefore names no specific function: its plateau is determined only by the properties it proves.
### ### POSITIVE CONTROL (non-uniqueness): two functions satisfying every field of `ContDiffBumpBase` on a grid --
### A = Mathlib`s `ofInnerProductSpace` base, `smoothTransition ((R - |x|) / (R - 1))`, and B = `smoothTransition` applied
### twice -- and the two DIFFER, pointwise and in the transform the window would cite. ### NEGATIVE CONTROL: a candidate
### violating a field (support to 2, not R) is REJECTED by the same field checks.
"""
import io
import json
import math
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
ML = os.path.join('D:', os.sep, 'SIDE-explicit-formula', '.lake', 'packages', 'mathlib', 'Mathlib')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula', 'SIDEExplicitFormula', 'TwoPropertyWindow.lean')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

QUOTES = [
    ('Analysis/Calculus/BumpFunction/Basic.lean', r'class HasContDiffBump .*: Prop where'),
    ('Analysis/Calculus/BumpFunction/Basic.lean', r'^  out : Nonempty \(ContDiffBumpBase E\)'),
    ('Analysis/Calculus/BumpFunction/Basic.lean', r'^  Nonempty\.some hb\.out'),
    ('Analysis/Calculus/BumpFunction/Basic.lean', r'\(someContDiffBumpBase E\)\.toFun \(f\.rOut / f\.rIn\)'),
    ('Analysis/Calculus/BumpFunction/InnerProduct.lean', r'toFun R x := smoothTransition'),
    ('Analysis/Calculus/BumpFunction/InnerProduct.lean', r'instance \(priority := 100\) hasContDiffBump_of_innerProductSpace'),
]


def smooth_transition(x):
    x = np.asarray(x, dtype=float)
    a = np.where(x > 0, np.exp(-1.0 / np.maximum(x, 1e-300)), 0.0)
    b = np.where(1 - x > 0, np.exp(-1.0 / np.maximum(1 - x, 1e-300)), 0.0)
    return a / (a + b)


def base_A(R, x):
    return smooth_transition((R - np.abs(x)) / (R - 1))


def base_B(R, x):
    return smooth_transition(smooth_transition((R - np.abs(x)) / (R - 1)))


def base_bad(R, x):
    return smooth_transition((2.0 - np.abs(x)) / (2.0 - 1))


def fields(f, R):
    """### the fields of ContDiffBumpBase on a grid: values in [0,1]; symmetric; = 1 on |x| <= 1; support = (-R, R)."""
    x = np.linspace(-3.0, 3.0, 60001)
    v = f(R, x)
    # ### b526`s defect: the first form compared v with v[::-1] exactly, and a float linspace is not exactly symmetric; the
    # ### symmetry is now tested by evaluating at -x itself.
    return dict(in_unit=bool(np.all((v >= 0) & (v <= 1))), symmetric=bool(np.max(np.abs(v - f(R, -x))) == 0.0),
                one_inside=bool(np.all(v[np.abs(x) <= 1] == 1.0)),
                # ### positivity inside tested 0.1 in from the edge: B`s double exponential underflows to 0.0 in floats nearer
                # ### the edge, which is a property of the floats and not of B (exp(-1/exp(-1/y)) > 0 for every y > 0).
                support=bool(np.all(v[np.abs(x) >= R] == 0.0) and np.all(v[(np.abs(x) < R - 0.1)] > 0)))


def main():
    quotes = []
    for f, pat in QUOTES:
        t = io.open(os.path.join(ML, f), encoding='utf-8').read().split(NL)
        hit = [(i + 1, l.rstrip()) for i, l in enumerate(t) if re.search(pat, l)]
        quotes.append(dict(file='Mathlib/' + f, pattern=pat, hits=hit))
    ker = io.open(KER, encoding='utf-8').read()
    kq = [l for l in ker.split(NL) if l.startswith('def plateau') or l.strip().startswith('⇑(plateauBump')]
    R = 4.0 / 3.0                                   # ### rOut / rIn at the b519 values: 1 / (1 - 1/4)
    fa, fb, fbad = fields(base_A, R), fields(base_B, R), fields(base_bad, R)
    x = np.linspace(-R, R, 20001)
    diff = float(np.max(np.abs(base_A(R, x) - base_B(R, x))))
    xm = float(x[np.argmax(np.abs(base_A(R, x) - base_B(R, x)))])
    # ### the transform the window would cite: phi-hat at the Q0 target, a = 34 (L = log 34, rIn = 3L/4), for both bases
    L = math.log(34.0)
    u = np.linspace(-L, L, 200001)
    du = u[1] - u[0]
    out = {}
    for name, f in (('A', base_A), ('B', base_B)):
        phi = f(R, u / (0.75 * L))
        out[name] = dict(integral=float(np.sum(phi) * du), at_0=float(np.sum(phi) * du),
                         at_gamma0=float(np.sum(phi * np.cos(16.290216 * u)) * du),
                         growth=float(np.sum(phi * np.cosh(0.4532604747946607 * u)) / np.sum(phi)))
    res = dict(quotes=quotes, kernel_lines=kq, R=R, fields_A=fa, fields_B=fb, fields_bad=fb and fbad,
               both_pass=all(fa.values()) and all(fb.values()), bad_rejected=not all(fbad.values()),
               max_pointwise_diff=diff, at_x=xm, transforms=out,
               halt='the kernel`s plateau is Mathlib`s ContDiffBump over someContDiffBumpBase = Nonempty.some (Classical.choice): '
                    'no specific function to evaluate')
    io.open(os.path.join(D, 'b526_bump.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    for q in quotes:
        print('  %s : %s' % (q['file'], q['hits']))
    print('  kernel : %s' % kq)
    print('  fields A %s ; B %s ; bad %s' % (fa, fb, fbad))
    print('  ### both bases pass every field : %s ; the bad candidate rejected : %s' % (res['both_pass'], res['bad_rejected']))
    print('  ### A and B differ : max %.4f at x = %.4f (unit ball scale) ; transforms at a = 34 : %s' % (diff, xm, out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
