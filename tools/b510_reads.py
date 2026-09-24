# -*- coding: utf-8 -*-
"""b510_reads.py -- COMPONENTS 3 AND 4. ### `python tools/b510_reads.py search | price`

### `search` -- the fifty-seven vendored modules scanned DECLARATION BY DECLARATION: every `theorem`/`lemma`/`def`
###             whose text (declaration line to `:=`) mentions a zero-location notion (`RiemannHypothesis`, `onLine`,
###             `re = 1 / 2`, `.re = 1/2`) AND a sign notion (`0 ≤`, `≥ 0`, `nonneg`, `Nonneg`), printed whole, and the
###             whole residue HAND-READ against the shape "zeros on the line -> zero side >= 0 for k = h * h~" or its
###             contrapositive. ### A second, wider pass prints every declaration naming `weilTest` with a sign notion.
###             ### The yields of both needles are printed, and a control: the needle set must find a known sign
###             statement planted in a fixture string.
### `price`  -- W-ORD-PL-CLASS: (a) each Mathlib lemma the sketch needs, searched in the kernel's own Mathlib by
###             `git grep` on `theorem|lemma|def <last segment>`, FOUND with its file or ABSENT; (b) the cost of
###             re-measuring the 119 cells in cell-seconds, SUMMED from b504's own per-cell `seconds`, with b506's Q0
###             per-cell seconds beside it for the joint act (R119)(2) names.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
ML = os.path.join(KER, '.lake', 'packages', 'mathlib')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev)\s+(\S+)', re.M)
LOC = re.compile(r'RiemannHypothesis|onLine|\bre = 1 ?/ ?2\b|\.re = 1 ?/ ?2|re = \(1 ?/ ?2')
SIGN = re.compile(r'0 ≤|≥ 0|\bnonneg\b|Nonneg')


def modules():
    out = []
    for dp, _d, fs in os.walk(os.path.join(KER, 'Zeta23')):
        for f in sorted(fs):
            if f.endswith('.lean'):
                out.append(os.path.join(dp, f))
    return sorted(out)


def decls(text):
    ms = list(DECL.finditer(text))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        body = text[m.start():end]
        j = body.find(':=')
        yield m.group(1), m.group(2), (body[:j] if j >= 0 else body[:800]).strip()


def search():
    mods = modules()
    loc_sign, weil_sign, n_decl = [], [], 0
    for p in mods:
        t = io.open(p, encoding='utf-8').read()
        for kind, name, st in decls(t):
            n_decl += 1
            rel = os.path.relpath(p, KER).replace(os.sep, '/')
            if LOC.search(st) and SIGN.search(st):
                loc_sign.append(dict(file=rel, kind=kind, name=name, statement=st))
            if 'weilTest' in st and SIGN.search(st):
                weil_sign.append(dict(file=rel, kind=kind, name=name, statement=st))
    fixture = 'theorem planted (hRH : ∀ ρ ∈ Z.carrier, ρ.re = 1 / 2) : 0 ≤ W f f'
    ctl = bool(LOC.search(fixture) and SIGN.search(fixture))
    L = ['=' * 104, 'b510 -- COMPONENT 3. ### THE DIRECTION THE VENDORED MODULES HOLD.', '=' * 104,
         '  modules scanned : %d ; declarations read : %d' % (len(mods), n_decl),
         '  control -- a planted "zeros on the line -> 0 <= W f f" is found by the needles : %s' % ctl,
         '  ### NEEDLE 1 (a zero-location notion AND a sign notion in one statement) : %d declarations' % len(loc_sign)]
    for d in loc_sign:
        L += ['    --- %(kind)s %(name)s  <%(file)s>' % d] + ['      ' + x for x in d['statement'].split(NL)]
    L += ['  ### NEEDLE 2 (`weilTest` AND a sign notion in one statement) : %d declarations' % len(weil_sign)]
    for d in weil_sign:
        L += ['    --- %(kind)s %(name)s  <%(file)s>' % d] + ['      ' + x for x in d['statement'].split(NL)]
    L += ['=' * 104]
    io.open(os.path.join(D, 'b510_search.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b510_search.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(modules=len(mods), decls=n_decl, control=ctl, needle1=loc_sign, needle2=weil_sign), indent=1, ensure_ascii=False) + NL)
    print(NL.join(L))
    return 0


# ### (a) the approximation sketch's needs, each with the Mathlib name the seat reads for it
NEEDS = [
    ('mollify: a smooth compactly supported approximate identity', 'ContDiffBump', 'structure'),
    ('the mollified k converges to k (uniformly on compacta, as the bump shrinks)', 'convolution_tendsto_right', None),
    ('the mollified k is C^2 (smoothness of a convolution with a smooth compact kernel)', 'contDiff_convolution_left', None),
    ('the mollified k keeps compact support', 'convolution', 'HasCompactSupport'),
    ('the transform of a convolution is the product of transforms', 'fourier_convolution', None),
    ('dominated convergence under the integral (A, P)', 'tendsto_integral_of_dominated_convergence', None),
    ('dominated convergence under the zero sum (Z)', 'tendsto_tsum_of_dominated_convergence', None),
    ('decay |h_k(r)| = O(|r|^-2) for a continuous piecewise-linear k', 'fourier_piecewiseLinear_isBigO', None),
]


def gitgrep(pattern):
    r = subprocess.run(['git', '-C', ML, 'grep', '-n', '-E', pattern, '--', 'Mathlib'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return [l for l in r.stdout.split(NL) if l.strip()]


def price():
    rows = []
    for what, last, kind in NEEDS:
        if kind == 'structure':
            hits = gitgrep(r'^structure %s\b' % re.escape(last))
        else:
            hits = gitgrep(r'^\s*(theorem|lemma|def)\s+([A-Za-z_.]*\.)?%s\b' % re.escape(last))
            if kind:
                hits = [h for h in hits if kind in h or ('namespace ' + kind) in h] or \
                       [h for h in hits if re.search(r'(theorem|lemma)\s+%s\.%s\b' % (re.escape(kind), re.escape(last)), h)]
        rows.append(dict(need=what, name=last, found=bool(hits), where=[h[:160] for h in hits[:3]]))
    b504 = [json.loads(l) for l in io.open(os.path.join(D, 'b504_cells.jsonl'), encoding='utf-8') if l.strip()]
    b506 = [json.loads(l) for l in io.open(os.path.join(D, 'b506_cells.jsonl'), encoding='utf-8') if l.strip()]
    xi_s = sum(c['seconds'] for c in b504)
    q_s = sum(c['seconds'] for c in b506)
    q_per = q_s / len(b506)
    res = dict(needs=rows, b504_cells=len(b504), b504_cell_seconds=xi_s, b506_cells=len(b506), b506_cell_seconds=q_s,
               b506_per_cell=q_per, joint_cell_seconds=xi_s + q_per * len(b504), under_one_hour_xi=xi_s < 3600)
    L = ['=' * 104, 'b510 -- COMPONENT 4. ### W-ORD-PL-CLASS PRICED; NEITHER DISPOSITION TAKEN.', '=' * 104,
         '### (a) P-PL BY A LIMIT OF C^2 APPROXIMANTS -- THE SKETCH, FIVE LINES:',
         '    1. k_e := k * phi_e, phi_e an even ContDiffBump of radius e: C^2, even, compactly supported, in EF_lit`s class.',
         '    2. EF_lit holds for each k_e (b509`s b321_identity, the even case).',
         '    3. P and PR: k_e -> k uniformly on a fixed compact set, and PR is a finite sum there; P is an integral of a compactly supported function.',
         '    4. A and Z: h_{k_e} = h_k * h_{phi_e} with |h_{phi_e}| <= 1, so |h_{k_e}(r)| <= |h_k(r)| = O(|r|^-2) dominates; A by dominated convergence on R, Z by dominated convergence over the zeros, summable against N(T) = O(T log T).',
         '    5. The limit e -> 0 gives EF_lit for k. ### THE ONE ANALYTIC INPUT NOT IN EF_lit`s CLASS: the O(|r|^-2) decay for piecewise-linear k.',
         '    %-78s %-44s %s' % ('need', 'name searched', 'in the kernel`s Mathlib')]
    for r in rows:
        L.append('    %-78s %-44s %s' % (r['need'][:78], r['name'], ('FOUND  ' + (r['where'][0].split(':')[0] if r['where'] else '')) if r['found'] else 'ABSENT'))
    L += ['', '### (b) A C^2 FAMILY INSIDE THE COMPILED CLASS:',
          '    the ladder`s seed g_a (three bumps, both moments vanishing) with each bump replaced by the cubic B-spline B_4 at the same',
          '    width: g_a is C^2 and compactly supported, and k_a = g_a * g_a~ is even, in K (h = g_a), and C^6 as a combination of',
          '    cross-correlations of cubic splines. ### ITS TRANSFORM: h_{k_a}(r) = |h_{g_a}(r)|^2, a combination of products of sinc^4 factors,',
          '    so |h_{k_a}(r)| = O(|r|^-8) -- against O(|r|^-2) for the piecewise-linear windows -- and it is exact in closed form, so',
          '    no piecewise-linear transform enters the chain.',
          '    ### THE COST, SUMMED FROM b504`S OWN PER-CELL SECONDS: %d cells, %.0f cell-seconds (%.1f cell-hours).' % (len(b504), xi_s, xi_s / 3600.0),
          '    ### with the Q0 control on the same 119 cells, at b506`s %.1f s a cell (93 cells, %.0f cell-seconds): %.0f cell-seconds jointly.'
          % (q_per, q_s, xi_s + q_per * len(b504)),
          '    ### (b) PRICES UNDER ONE HOUR OF COMPUTE, ON XI ALONE : %s.' % res['under_one_hour_xi'],
          '    ### the closed-form transform may make each cell cheaper than b504`s; that is not priced here, and the figure is b504`s.',
          '=' * 104]
    io.open(os.path.join(D, 'b510_price.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b510_price.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit({'search': search, 'price': price}[sys.argv[1]]())
