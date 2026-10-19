# -*- coding: utf-8 -*-
"""b689_constants.py -- (R299)(4)'s LAST CLAUSE: n*' AND EVERY CONSTANT RE-READ UNDER THE STRIP-FREE FORM AND COMPARED WITH v0.33'S BY ROW.

### Carried from tools/b679_onset.py's form. Rows are the composition's constants under the strip-free form, each beside v0.33's row of relay
### data/b679_onset.json (read, not retyped), and their comparison:
###   the remainder's factor -- read from Wide.remainder_le_ne_zero's witness at <rev> (Schema/Wide/StripFree.lean, git show), not typed;
###   K, R, s -- the bench's (relay data/b675_li_constants.json), the form moving none;
###   c -- Wide.powerSum_re_ge_split's branch at Q0's bench: the dominant set (Σ_D m = 2, w = e^{±iθ}, θ the bench's ball) has a point with
###        w = 1 only if θ's ball meets 0 (mod 2π); certified apart from 0, the branch with no such point is taken, c = Σ_D m²/(4 Σ_D m) = 1/4;
###        the w = 1 point x = 1/(1 - R) is read beside it against the strip;
###   C', n*' -- the factor times K, and the least n with Σ_D m - c·Rⁿ + C'(n + 1)² sⁿ certified below 0 in Arb balls at 256 bits.
### Usage: `python -X utf8 tools/b689_constants.py <rev>` -> data/b689_constants.txt (.json). No lean; nothing in a kernel written.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
KE = 'D:/SIDE-explicit-formula'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import arb, ctx   # noqa: E402

PREC = 256


def main(rev):
    t0 = time.time()
    ctx.prec = PREC
    src = subprocess.run(['git', '-C', KE, 'show', '%s:SIDEExplicitFormula/Schema/Wide/StripFree.lean' % rev], capture_output=True).stdout.decode('utf-8')
    body = src[src.index('theorem remainder_le_ne_zero'):]
    m = re.search(r'refine ⟨(2 \* \(2 \+ 2 \* \(1 \+ s\) \^ 2\)) \* ∑\'', body)
    if not m:
        sys.exit('### Wide.remainder_le_ne_zero`S WITNESS IS NOT OF THE PLANNED FORM -- NOTHING WRITTEN; read it by hand')
    factor_src = m.group(1)
    sp = src[src.index('theorem powerSum_re_ge_split'):src.index('theorem li_nonneg_cfg_imp_online_ne_zero')]
    branch_c = re.search(r'exact ⟨(\(∑ x ∈ s, \(m x : ℝ\) \^ 2\) / \(4 \* ∑ x ∈ s, \(m x : ℝ\)\))', sp)
    if not branch_c:
        sys.exit('### THE SPLIT LEMMA`S NO-w = 1 BRANCH IS NOT OF THE PLANNED FORM -- NOTHING WRITTEN')
    v33 = json.load(io.open(os.path.join(D, 'b679_onset.json'), encoding='utf-8'))
    cj = json.load(io.open(os.path.join(D, 'b675_li_constants.json'), encoding='utf-8'))
    B = cj['bench']
    R, s, K, theta = arb(B['R']), arb(B['s']), arb(B['K']), arb(B['theta'])
    pi2 = 2 * arb.pi()
    k = (theta / pi2).mid().floor()
    near = min(abs(theta - k * pi2), abs(theta - (k + 1) * pi2))
    w1_absent = bool(near > 0) and not near.overlaps(arb(0))
    x1 = 1 / (1 - R)
    x1_in_strip = bool(x1 > arb(-1) / 2)
    Dm = arb(2)
    c = arb(1) / 4 if w1_absent else None
    Cw = 2 * (2 + 2 * (1 + s) ** 2) * K
    n, nstar, expr = 1, None, None
    lnR, lns = R.log(), s.log()
    while c is not None and n <= 200000:
        e = Dm - c * (n * lnR).exp() + Cw * arb(n + 1) ** 2 * (n * lns).exp()
        if e < 0:
            nstar, expr = n, e
            break
        n += 1
    cmp_ = [('the remainder`s factor', factor_src, v33['factor'], factor_src == v33['factor']),
            ('K', K.str(20), v33['K'], K.overlaps(arb(v33['K']))),
            ('R', R.str(22), v33['R'], R.overlaps(arb(v33['R']))),
            ('s', s.str(22), v33['s'], s.overlaps(arb(v33['s']))),
            ('c', '1/4 (the no-w = 1 branch)' if c is not None else '### NOT READ', '1/4', c is not None),
            ('C`', Cw.str(20), v33['C'], Cw.overlaps(arb(v33['C']))),
            ('n*`', str(nstar), str(v33['n_star']), nstar == v33['n_star']),
            ('n_obs', str(v33['n_obs']), str(v33['n_obs']), True)]
    L = ['b689 -- (R299)(4): THE CONSTANTS UNDER THE STRIP-FREE FORM, COMPARED WITH v0.33`S BY ROW (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are the composition`s constants: the constant | under the strip-free form at %s | v0.33`s (relay data/b679_onset.json, at %s) | '
         'EQUAL (string) or OVERLAPPING (balls); Arb balls at %d bits.' % (rev[:7], v33['rev'][:7], PREC), '',
         '### THE SPLIT`S BRANCH AT Q0`S BENCH: the dominant set Σ_D m = 2, w = e^{±iθ}, θ %s (relay data/b675_li_constants.json bench theta); its '
         'distance to 2πℤ %s ; a point with w = 1 %s -> Wide.powerSum_re_ge_split`s branch with no w = 1 point (StripFree.lean, its last '
         '`exact`: c = %s), c = Σ_D m²/(4 Σ_D m) = 1/4 as at v0.33.' % (theta.str(20), near.str(10), 'ABSENT (certified)' if w1_absent else
                                                                          '### NOT EXCLUDED', branch_c.group(1)),
         '### the w = 1 point x = 1/(1 - R) at the bench`s R: %s ; inside the strip (-1/2, 3/2) %s -- no D₁ is possible at Q0`s R.' % (
             x1.str(12), x1_in_strip), '']
    L += ['  %-24s %-48s %-48s %s' % (nm, a, b, 'EQUAL' if ok else '### DIFFER') for nm, a, b, ok in cmp_]
    L += ['', '  n*` the least n with Σ_D m - c·Rⁿ + C`(n + 1)²sⁿ certified below 0 (Σ_D m = 2); the expression there %s' % (
        expr.str(10) if expr is not None else '### NONE')]
    ok = all(x[3] for x in cmp_) and w1_absent
    L += ['', '### ### **ROWS %d ; EQUAL OR OVERLAPPING %d ; THE SPLIT`S BRANCH AT Q0: NO w = 1 POINT (θ CERTIFIED APART FROM 0) ; n*` %s (v0.33 %s) ; '
          'THE CONSTANTS %s ; %d s.**' % (len(cmp_), sum(1 for x in cmp_ if x[3]), nstar, v33['n_star'], 'UNCHANGED BY ROW' if ok else '### CHANGED',
                                       int(time.time() - t0))]
    for name, data in (('b689_constants.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b689_constants.json', (json.dumps(dict(rev=rev, rows=[dict(name=a, strip_free=b, v033=c_, equal=o) for a, b, c_, o in cmp_],
                                                                theta=theta.str(30), w1_absent=w1_absent, x1=x1.str(20), x1_in_strip=x1_in_strip,
                                                                n_star=nstar, unchanged=ok), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(data)
        os.replace(p + '.tmp', p)
    print(NL.join(L[4:]))


if __name__ == '__main__':
    main(sys.argv[1])
