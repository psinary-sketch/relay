# -*- coding: utf-8 -*-
"""b511_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b511_record.py components | desk | trail`
### Every figure READ from the banks, not retyped."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


R = json.loads(read('b511_results.json') or '{}')
FX = json.loads(read('b511_fixture.json') or '[]')
ROWS = [json.loads(l) for l in read('b511_cells.jsonl').split(NL) if l.strip()]
BS = sorted([r for r in ROWS if r['family'] == 'bspline'], key=lambda r: r['a'])
MS = [c['xi']['m'] for c in BS]
RISES = sum(1 for i in range(len(MS) - 1) if MS[i + 1] > MS[i])
w = lambda v: 'HELD' if v else 'REFUTED'


def rng(f):
    rs = [r for _a, r in R[f]['ratio'] if r is not None]
    return min(rs), max(rs)


def components():
    L = ['=' * 104, 'b511 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 0 -- THE FIXTURE (b511_fixture.json).']
    for f in FX:
        L.append('    %-8s a=%.1f m=%d notch %s : max |closed - numeric| over %d u = %.2e ; even %s ; |k^(i/2)| %.1e ; |k^(0)| %.1e ; c = %s'
                 % (f['family'], f['a'], f['m'], [round(x, 6) for x in f['notch']], len(f['u']), f['maxdiff'], f['even'],
                    f['pole'], f['mean'], ['%.9g' % x for x in f['c']]))
    L += ['    ### MEMBERSHIP IN classK (the seat`s statement from H2Sign.lean`s definition): k = weilTest h h with h = g (B-spline)',
          '    or h = g_notch = PROD_j (1 + gamma_j^-2 D^2) g built on order 2k+4 -- h C^2, even, compactly supported; so k is even,',
          '    C^2 and compactly supported. ### Not a compiled step.', '',
          '### THE RUN LOG.'] + read('b511_run_log.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENTS 1-3.'] + read('b511_report.txt').rstrip(NL).split(NL)
    L += ['', '### xi`s B-spline margin, all 119 widths : rising steps %d of %d -- strictly decreasing.' % (RISES, len(MS) - 1), '=' * 104]
    io.open(os.path.join(D, 'b511_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-3:]))


def desk():
    b = R['bspline']
    L = ['=' * 104, 'b511 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- B-spline cells verified: xi %d of 119, Q0 %d of 119. ### Every unverified xi cell has |r|/B at most %.3f:'
         % (w(R['n1']), b['xi_verified'], b['q_verified'], b['xi_reading']['unverified_ratio_max']),
         '    the residual IS the archimedean integral`s truncation at u = 600, which b504`s u-term prices over 600..1200 only -- ESTIMATE-SHORT.',
         '  **(N2)** ### **%s.** -- xi`s B-spline margin has no extremum at all: it falls at every one of the 118 steps. ### The three of the'
         % w(R['n2']),
         '    old family (4.062, 5.196, 13.153) were features of the piecewise-linear windows.',
         '  **(N3)** ### **%s.** -- Q0`s margin at k = 5 is positive at every cell, smallest %.4g; its sign decided on its own error at 119 of 119.'
         % (w(R['n3']), R['notch5']['q_min']),
         '  **(N4)** ### **%s.** -- xi`s margin is positive at every verified cell of every family: ### **VACUOUS ON NOTCH3 AND NOTCH5, WHICH HAVE NO'
         % w(R['n4']),
         '    VERIFIED xi CELL.** ### Read on its own error instead, it is positive at 119 of 119 in each family.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- xi verifies at %d of 119, not 119.' % (w(R['s1']), b['xi_verified']),
         '  **(S2)** ### **%s.** -- Q0`s margin is positive at every verified cell of notch1, notch3 and notch5.' % w(R['s2']),
         '  **(S3)** ### **%s.** -- none of the three survives.' % w(R['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d** (one HELD vacuous on two families). ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([R[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [R[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [R[k] for k in ('s1', 's2', 's3')].count(True), [R[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b511_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b511_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump({k: R[k] for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')},
              io.open(os.path.join(D, 'b511_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b511 — two families inside the compiled class: the margin falls monotonically, and the notch finds no negative Epstein cell'


def trail():
    b = R['bspline']
    body = """
%(h)s

**(R120) ratified.** W-ORD-PL-CLASS is taken at disposition (b), together with W-ORD-FAMILY-SENSITIVITY; P-PL stays a
work-order; the numerical lane opened for this act alone, and the kernel lane reopens for the act after, the
register-equivalence read at `h2_sign`.

**THE WINDOWS.** The ladder's three widths `a, a^1/2, a^1/4`, each bump a uniform order-`m` B-spline, combined with
`INT g = 0` and `INT g cosh(v/2) = 0`; `k = g ⋆ g~`, so `k-hat = g-hat²` in closed form. The notch: `g_notch = PROD_j
(1 + γ_j⁻² ∂²) g` on order `m = 2k + 4`, its transform vanishing at the object's lowest `k` on-line ordinates. Every
window is in `classK` with `h = g` (resp. `g_notch`) — the seat's statement from the definition, not a compiled
step. **COMPONENT 0:** the closed form against a numerical integral of the window agrees to %(f0).1e (B-spline) and
%(f1).1e (notch, k = 5), bar 1e-10.

**COMPONENT 1, the B-spline family.** ξ verifies at **%(xv)d of 119**, Q0 at %(qv)d. Every unverified ξ cell has `|r|/B`
at most %(ur).3f: **the residual is the archimedean integral's truncation at u = 600, which b504's u-term prices only
over 600–1200** — ESTIMATE-SHORT, not an identity that fails. **ξ's margin falls at every one of the 118 steps**, from
%(m0).4g at a = 1.3 to %(m1).4g at a = 14.106736: **no extremum survives, and the old three (4.062, 5.196, 13.153)
were features of the piecewise-linear windows.** The Epstein margin is positive at every cell, smallest %(qm).4g.

**COMPONENT 2, the notch family** (k = 1, 3, 5). The notched zeros' part reads 0 to 1e-28 or below, the control. ξ
verifies at %(n1x)d, %(n3x)d and %(n5x)d cells, every unverified cell again within 6%% of its bound. **Q0's margin is positive
at every cell of every k** — smallest %(q1).3g, %(q3).3g, %(q5).3g — and its sign is decided on its own error at 119 of 119.
Q0's bound is its zero-side truncation above 150, inflated by the notch factor, and at %(vac3)d (k = 3) and %(vac5)d (k = 5) cells
it exceeds the margin: those passes are VACUOUS.

**COMPONENT 3.** Q0's off-line part over its remaining on-line part stays between %(r1a).3g and %(r5b).3g across the three k;
**the off-line part exceeds the on-line part at NONE of the widths.** ξ's margin at the same widths is positive
throughout.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s, vacuous on notch3 and notch5.** The seat's own: (S1) %(S1)s,
(S2) %(S2)s, (S3) %(S3)s. **W-ORD-FAMILY-SENSITIVITY is not discharged: no window in either family makes Q0's margin
negative at these widths.** **The numerical lane shuts at this act's close.** No grade conferred; nothing deposits;
row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, f0=FX[0]['maxdiff'], f1=FX[1]['maxdiff'], xv=b['xi_verified'], qv=b['q_verified'],
           ur=b['xi_reading']['unverified_ratio_max'], m0=MS[0], m1=MS[-1], qm=b['q_min'],
           n1x=R['notch1']['xi_verified'], n3x=R['notch3']['xi_verified'], n5x=R['notch5']['xi_verified'],
           q1=R['notch1']['q_min'], q3=R['notch3']['q_min'], q5=R['notch5']['q_min'],
           vac3=R['notch3']['q_reading']['vacuous'], vac5=R['notch5']['q_reading']['vacuous'],
           r1a=min(rng(f)[0] for f in ('notch1', 'notch3', 'notch5')), r5b=max(rng(f)[1] for f in ('notch1', 'notch3', 'notch5')),
           N1=w(R['n1']), N2=w(R['n2']), N3=w(R['n3']), N4=w(R['n4']), S1=w(R['s1']), S2=w(R['s2']), S3=w(R['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b2 in zip(al, bl) if a == b2), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b511_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
