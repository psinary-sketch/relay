# -*- coding: utf-8 -*-
"""b519_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b519_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (9)'s, recomputed from the cells.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
VARIANTS = ('A', 'B', 'C')
NAMES = dict(A='NOTCHED', B='EDGE-WEIGHTED', C='BOTH')
DELTA = 0.9532604747946607 - 0.5
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


R = json.loads(read('b519_results.json') or '{}')
FX = json.loads(read('b519_fixture.json') or '[]')
MT = json.loads(read('b519_matched.json') or '[]')
R518 = json.loads(read('b518_results.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def cells(v):
    return sorted((json.loads(l) for l in read('b519_cells_%s.jsonl' % v).split(NL) if l.strip()), key=lambda c: c['a'])


def g518(a):
    """### READING (7): b518's realized growth, its order-6 B-spline in closed form."""
    x = DELTA * (2.0 * math.log(a) / 6.0) / 2.0
    return (math.sinh(x) / x) ** 6


def xi_short(v):
    return max(abs(c['xi']['r']) / c['xi']['B'] for c in cells(v))


def xi_margin(v):
    return min(c['xi']['h2'] / c['xi']['B'] for c in cells(v))


def scores():
    cb = cells('B')
    widest = cb[-1] if cb else None
    gB = widest['q']['growth'] if widest else None
    ratioG = gB / g518(widest['a']) if widest else None
    return dict(
        n1=bool(R.get('C', {}).get('q', {}).get('h2_neg')),
        n2=not R.get('A', {}).get('q', {}).get('h2_neg', ['x']),
        n3=ratioG is not None and ratioG > 10.0,
        n4=all(len(R[v]['xi']['h2_pos']) == R[v]['xi']['verified'] for v in VARIANTS),   # ### READING (9) as registered: vacuous where none verify
        s1=ratioG is not None and ratioG < 10.0,
        s2=abs(R['A']['q']['widest_ratio']) > abs(R518['q']['widest_ratio']),
        s3=bool(FX) and all(f['meets'] for f in FX)), ratioG, gB, (widest['a'] if widest else None)


def components():
    sc, ratioG, gB, wa = scores()
    L = ['=' * 132, 'b519 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### COMPONENT 0 -- THE FIXTURES UNDER (R125)(2) (READING (5)):']
    for f in FX:
        L.append('  (%s) %s gammas %s, %d nodes : bar met at every u %s ; |k(.7) - k(-.7)| %.1e (scale %.1e) ; knot jumps %s'
                 % (f['variant'], f['object'], ['%.4f' % g for g in f['gammas']], f['nodes'], f['meets'], f['even'], f['scale'],
                    {k: '%.1e' % v for k, v in f['knot_jumps'].items()}))
        L += ['      u=%-8.4f diff %.2e ; floor %.2e ; bar %.2e ; %s' % (r['u'], r['diff'], r['floor'], r['bar'], 'MET' if r['meets'] else 'NOT MET')
              for r in f['rows']]
        L.append('    classK (READING (2)): k = weilTest h h with h = %s ; even ; C^2 ; real-valued ; support %s.' % (f['generating_h'], f['support']))
    L += ['', '### COMPONENT 0 -- THE CONTROL, THE PRINTED RATIOS AND THE REALIZED GROWTH (READINGS (6), (7)):']
    for m in MT:
        L.append('  (%s) a=%-10.6f %-3s h^(g0) %+.1e (peak %.2e) ; slope %+.4e (num %+.4e) ; |h^|/|slope| at %s -> %s ; G %.4f of e^{dL} %.4f (%.3f)'
                 % (m['variant'], m['a'], m['object'], m['at_gamma0'][0], m['line_peak'], m['slope'], m['slope_numeric'],
                    ['%.3f' % x for x in m['points']], ['%.2e' % x for x in m['ratio_to_slope']], m['growth'], m['growth_bound'], m['growth_fraction']))
    L += ['', '### (N3)`S COMPARISON (READING (7)): at the widest cell a = %s, (B)`s G = %.6f, b518`s G = %.6f, ratio %.6f.'
          % (wa, gB, g518(wa), ratioG)]
    L += [''] + read('b519_report.txt').rstrip(NL).split(NL) + ['', '### THE RUN LOGS:'] + read('b519_fixture_log.txt').rstrip(NL).split(NL) \
        + read('b519_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b519_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:10]))


def desk():
    sc, ratioG, gB, wa = scores()
    L = ['=' * 104, 'b519 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- variant (C): Q0`s P - PR + A negative beyond B at %s.' % (w(sc['n1']), R['C']['q']['h2_neg'] or 'NONE'),
         '  **(N2)** ### **%s.** -- variant (A): Q0`s P - PR + A negative beyond B at %s.' % (w(sc['n2']), R['A']['q']['h2_neg'] or 'NONE'),
         '  **(N3)** ### **%s.** -- at the widest cell (B)`s G over b518`s G is %.4f, against 10.' % (w(sc['n3']), ratioG),
         '  **(N4)** ### **%s.** -- xi positive beyond B at every VERIFIED-EST cell: %s.'
         % (w(sc['n4']), ' ; '.join('(%s) %d of %d' % (v, len(R[v]['xi']['h2_pos']), R[v]['xi']['verified']) for v in VARIANTS))
         + ((' ### VACUOUS ON %s: NO VERIFIED-EST xi CELL THERE -- every such cell short of its bound by at most %.2fx, and P - PR + A above B by at least %.0fx at every cell, verified or not.'
             % (', '.join('(%s)' % v for v in VARIANTS if R[v]['xi']['verified'] == 0), max(xi_short(v) for v in VARIANTS if R[v]['xi']['verified'] == 0),
                min(xi_margin(v) for v in VARIANTS))) if any(R[v]['xi']['verified'] == 0 for v in VARIANTS) else ''),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- (N3) refuted: the ratio is %.4f, e^{delta L} at the widest cell %.4f.' % (w(sc['s1']), ratioG, math.exp(DELTA * math.log(wa))),
         '  **(S2)** ### **%s.** -- (A)`s widest pair ratio %+.4e against b518`s %+.4e.' % (w(sc['s2']), R['A']['q']['widest_ratio'], R518['q']['widest_ratio']),
         '  **(S3)** ### **%s.** -- every fixture`s bar met at every u : %s.' % (w(sc['s3']), [(f['variant'], f['object'], f['meets']) for f in FX]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 3 -- THE READING PER VARIANT:'] + ['    (%s) %s : %s' % (v, NAMES[v], R[v]['q']['reading']) for v in VARIANTS] + [
         '    THE WITNESS AT Q0 : %s' % (', '.join(R['witness']) or 'NONE'),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b519_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b519_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(sc, growth_ratio_B_over_b518=ratioG), io.open(os.path.join(D, 'b519_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b519 — three variants of the two-property window; (R128) entered'


def trail():
    sc, ratioG, gB, wa = scores()
    per = NL.join('- **(%s) %s:** Q0 VERIFIED-EST at %d; negative beyond its bound at %s; the pair negative at %d of %d widths; its ratio to the rest '
                  'at the widest cell %+.4e. ξ positive at %d of %d verified. Reading: %s.'
                  % (v, NAMES[v], R[v]['q']['verified'], R[v]['q']['h2_neg'] or 'no width', len(R[v]['q']['pair_neg']), R[v]['q']['cells'],
                     R[v]['q']['widest_ratio'], len(R[v]['xi']['h2_pos']), R[v]['xi']['verified'], R[v]['q']['reading']) for v in VARIANTS)
    body = """
%(h)s

**(R128) ratified.** (1) **h2_sign is Weil's positivity criterion on classK, and the record says so in those words**: the
Prop the kernel holds is the classical criterion restricted to even C² compactly supported functions of the form h ⋆ h~;
the compiled direction RH → h2_sign is the criterion's easy direction; the direction the deposit's Route 3 takes as a
named premise, h2 → RH, is Weil's theorem of 1952 for the full class and is not compiled for classK. The deposit's own
words at §37.2 — "an equivalence, classical, and not ours" — govern, and the programme's contribution is three things and
no fourth: the identification of its registers with the criterion; the formalization in progress; and the instruments.
(2) **`W-ORD-H2-BRIDGE`** is filed at the head of the K1 programme: SIDE-kernel's ConservationHypothesis and h2_sign are not
yet one object; until it closes, no sentence of the corpus says "the clause" of one kernel and means the other. (3) The
window's growth is set by where its mass sits — entered beside this act's growth figures below. (4) The numerical lane
opened for this act; the kernel lane reopens after it for (f)(i) with the window this act selects.

**COMPONENT 0.** Three variants of h = Π(γⱼ² + D²)(cos(γ₀u)φ), each in classK with generating h named, real: (A) notched
at the object's two nearest on-line ordinates, φ an order-10 B-spline; (B) edge-weighted, φ a plateau (ramp fraction
0.25, inner order 5); (C) both, inner order 9. The fixtures meet their (R125)(2) bars: %(fx)s. The control ĥ(γ₀) reads
0 in every variant. **The realized growth G = ∫φ cosh(δu) du at the widest cell: (B) %(gB).4f against b518's %(g518).4f, a
ratio of %(ratioG).3f** — bounded above by (d)'s e^{δL} there, so a factor of ten was never available to a unit-mass φ.

**COMPONENTS 1–2.**
%(per)s

**COMPONENT 3 — the witness at Q0:** %(wit)s. Nothing is claimed of the kernel either way.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s%(vac)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The
numerical lane shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade
conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement
about RH.
""" % dict(h=HEADING, fx=', '.join('(%s) %s %s' % (f['variant'], f['object'], 'met' if f['meets'] else 'NOT MET') for f in FX),
           gB=gB, g518=g518(wa), ratioG=ratioG, per=per, wit=(', '.join(R['witness']) or 'NONE — no variant is yet the witness'),
           vac=(' — VACUOUS on ' + ', '.join('(%s)' % v for v in VARIANTS if R[v]['xi']['verified'] == 0) + ', where no ξ cell verifies') if any(R[v]['xi']['verified'] == 0 for v in VARIANTS) else '',
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
    io.open(os.path.join(D, 'b519_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
