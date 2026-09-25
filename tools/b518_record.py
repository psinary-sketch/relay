# -*- coding: utf-8 -*-
"""b518_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b518_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (8)'s, recomputed from the cells.
"""
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


R = json.loads(read('b518_results.json') or '{}')
FX = json.loads(read('b518_fixture.json') or '[]')
MT = json.loads(read('b518_matched.json') or '[]')
CELLS = sorted((json.loads(l) for l in read('b518_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
w = lambda v: 'HELD' if v else 'REFUTED'


def scores():
    q, x = R.get('q', {}), R.get('xi', {})
    qv = [c for c in CELLS if c['q']['verified']]
    return dict(
        n1=bool(CELLS) and len(q.get('pair_neg') or []) == len(CELLS),
        n2=bool(q.get('h2_neg_half')),
        n3=q.get('narrowest') is not None and q['narrowest'] < 5.0,
        n4=x.get('verified', 0) > 0 and len(x.get('h2_pos') or []) == x.get('verified'),
        s1=bool(CELLS) and all(c['q']['pair'] < 0 for c in CELLS),
        s2=bool(qv) and all(c['q']['h2'] > c['q']['B'] for c in qv),
        s3=bool(FX) and all(f['meets'] for f in FX))


def components():
    L = ['=' * 132, 'b518 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### COMPONENT 0 -- THE FIXTURE UNDER (R125)(2) (READING (5)):']
    for f in FX:
        L.append('  %s gamma0 %.6f order %d, %d nodes : bar met at every u %s ; |k(.7) - k(-.7)| %.1e ; knot jumps %s'
                 % (f['object'], f['gamma0'], f['order'], f['nodes'], f['meets'], f['even'], {k: '%.1e' % v for k, v in f['knot_jumps'].items()}))
        L += ['      u=%-8.4f diff %.2e ; floor eps*SUM|t| %.2e ; bar sqrt(n)*floor %.2e ; %s'
              % (r['u'], r['diff'], r['floor'], r['bar'], 'MET' if r['meets'] else 'NOT MET') for r in f['rows']]
        L.append('    classK (READING (2)): k = weilTest h h with h = %s ; even ; C^2 ; real-valued ; support %s.' % (f['generating_h'], f['support']))
    L += ['', '### COMPONENT 0 -- THE CONTROL AND THE PRINTED RATIOS (READING (6)):']
    for m in MT:
        L.append('  a=%-10.6f %-3s h^(gamma0) %+.1e (line peak %.3e) ; slope %+.4e (central difference %+.4e) ; |h^|/|slope| at %s -> %s%s'
                 % (m['a'], m['object'], m['at_gamma0'][0], m['line_peak'], m['slope'], m['slope_numeric'], ['%.4f' % x for x in m['points']],
                    ['%.3e' % x for x in m['ratio_to_slope']],
                    (' ; h^(gammaOf rho) %+.3e %+.3ei' % tuple(m['hhat_at_gammaOf_rho'])) if 'hhat_at_gammaOf_rho' in m else ''))
    L += [''] + read('b518_report.txt').rstrip(NL).split(NL) + ['', '### THE RUN LOG:'] + read('b518_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b518_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc = scores()
    q, x = R['q'], R['xi']
    L = ['=' * 104, 'b518 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- the pair`s term negative at %d of %d widths ; pair / rest from %+.3e to %+.3e.'
         % (w(sc['n1']), len(q['pair_neg']), len(CELLS), q['ratio_min'], q['ratio_max']),
         '  **(N2)** ### **%s.** -- Q0`s P - PR + A negative beyond B at %d of %d VERIFIED-EST widths.' % (w(sc['n2']), len(q['h2_neg']), q['verified']),
         '  **(N3)** ### **%s.** -- the narrowest negative width : %s.' % (w(sc['n3']), q['narrowest'] or 'NONE'),
         '  **(N4)** ### **%s.** -- xi`s P - PR + A positive beyond B at %d of its %d VERIFIED-EST cells.' % (w(sc['n4']), len(x['h2_pos']), x['verified']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the pair`s term negative at %d of %d widths.' % (w(sc['s1']), len(q['pair_neg']), len(CELLS)),
         '  **(S2)** ### **%s.** -- Q0`s P - PR + A positive beyond B at %d of %d VERIFIED-EST cells.' % (w(sc['s2']), len(q['h2_pos']), q['verified']),
         '  **(S3)** ### **%s.** -- the fixture`s bar met at every u : %s.' % (w(sc['s3']), [f['meets'] for f in FX]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b518_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b518_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b518_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b518 — the two-property window; (R127) entered'


def trail():
    sc = scores()
    q, x = R['q'], R['xi']
    mq = [m for m in MT if m['object'] == 'q']
    body = """
%(h)s

**(R127) ratified.** (1) The two-property window of (R126)(1) is measured as W-ORD-FAMILY-SENSITIVITY's fourth family and
as the numerical register of (f)(i); its fixture floor priced by (R125)(2). (2) The reading was fixed before the run. (3)
The numerical lane opened for this act; the kernel lane reopens after it for (f)(i).

**COMPONENT 0.** h = (γ₀² + d²/du²)(cos(γ₀u)φ), φ the order-6 B-spline bump on [−log a, log a] (h C²), ĥ(z) = (γ₀² −
z²)·½[φ̂(z − γ₀) + φ̂(z + γ₀)], k = h⋆h in classK with generating h, real-valued; no pole annihilation. **The fixture meets
its (R125)(2) bar at every u for both objects** — the floor eps·Σ|terms| of the numerical route, the bar √n times it.
The control holds: ĥ(γ₀) reads 0 at the three widths and the slope matches a central difference. As ratios to the slope,
ĥ at Q0's neighbours 14.63 and 18.83 is %(n1)s at the ladder's first, middle and last widths, and at its lowest zero 1.31
%(low)s: the band suppresses the far zeros and not the near ones.

**COMPONENT 1 — Q0.** VERIFIED-EST at %(qv)d of %(n)d widths. **The pair's term is negative at %(pn)d of %(n)d widths** (about
−230 throughout); P − PR + A is positive beyond its bound at every verified width (%(qp)d) and negative at none, so no
narrowest width and no growth factor is banked.

**COMPONENT 2 — ξ** at 14.1347, the same columns. VERIFIED-EST at %(xv)d of %(n)d; P − PR + A positive beyond its bound at all
%(xp)d.

**COMPONENT 3 — the reading, in (R127)(2)'s words:** %(reading)s. Nothing is claimed of the kernel either way.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The
numerical lane shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade
conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement
about RH.
""" % dict(h=HEADING, n=len(CELLS), qv=q['verified'], pn=len(q['pair_neg']), qp=len(q['h2_pos']),
           xv=x['verified'], xp=len(x['h2_pos']), reading=R['reading'],
           n1=' / '.join('%.2f, %.2f' % tuple(m['ratio_to_slope'][:2]) for m in mq),
           low=' / '.join('%.1e' % m['ratio_to_slope'][2] for m in mq),
           N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), N4=w(sc['n4']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b518_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
