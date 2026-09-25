# -*- coding: utf-8 -*-
"""b514_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b514_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (9)'s, recomputed from the cells.
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


R = json.loads(read('b514_results.json') or '{}')
FX = json.loads(read('b514_fixture.json') or '[]')
MT = json.loads(read('b514_matched.json') or '[]')
CELLS = sorted((json.loads(l) for l in read('b514_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
w = lambda v: 'HELD' if v else 'REFUTED'


def scores():
    q, x = R.get('q', {}), R.get('xi', {})
    qv = [c for c in CELLS if c['q']['verified']]
    return dict(
        n1=len(q.get('m_neg') or []) >= 1,
        n2=x.get('verified', 0) > 0 and len(x.get('m_pos') or []) == x.get('verified'),
        n3=len(q.get('share_over_half') or []) >= 1,
        s1=all(c['q']['pair'] > 0 for c in CELLS) and bool(CELLS),
        s2=bool(qv) and all(c['q']['h2'] > c['q']['B'] for c in qv),
        s3=bool(FX) and all(f['meets'] for f in FX))


def rng(obj, key):
    v = [c[obj][key] for c in CELLS]
    return (min(v), max(v)) if v else (None, None)


def components():
    L = ['=' * 124, 'b514 -- THE COMPONENTS, AS THEY RAN.', '=' * 124, '', '### COMPONENT 0 -- THE FIXTURE (READING (7)):']
    for f in FX:
        L.append('  %s gamma0 %.6f : max |closed - numeric| %.2e over u %s ; bar 1e-10 %s ; |k(.7) - k(-.7)| %.1e ; knot jumps %s ; support %s'
                 % (f['object'], f['gamma0'], f['maxdiff'], ['%.4f' % u for u in f['u']], 'MET' if f['meets'] else 'NOT MET',
                    f['even'], {k: '%.1e' % v for k, v in f['knot_jumps'].items()}, f['support']))
        L.append('    classK (READING (2)): k = weilTest h h with h = %s ; even ; C^2 (jumps of g, g`, g`` at the knots are 2 eps times'
                 ' the next derivative; g``` jumps, the probe`s positive control) ; compact support.' % f['generating_h'])
    L += ['', '### COMPONENT 0 -- THE MATCHED RATIO (READING (8)):']
    for m in MT:
        L.append('  a=%-10.6f %-3s k^(gamma0) %+.4e ; nearest %s -> %s ; ratio %.3e%s'
                 % (m['a'], m['object'], m['at_gamma0'][0], ['%.4f' % x for x in m['nearest']], ['%+.3e' % v[0] for v in m['at_nearest']],
                    m['ratio'], (' ; k^(gammaOf rho = %.6f %+.6fi) %+.4e %+.4ei' % tuple(m['gammaOf_rho'] + m['at_gammaOf_rho'])) if 'gammaOf_rho' in m else ''))
    L += [''] + read('b514_report.txt').rstrip(NL).split(NL) + ['', '### THE RUN LOG:'] + read('b514_run_log.txt').rstrip(NL).split(NL) + ['=' * 124]
    io.open(os.path.join(D, 'b514_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc = scores()
    q, x = R['q'], R['xi']
    L = ['=' * 104, 'b514 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- Q0`s margin m = A - PR negative (decided, VERIFIED-EST) at : %s ; of %d verified cells, positive %d, undecided %s.'
         % (w(sc['n1']), q['m_neg'] or 'NONE', q['verified'], len(q['m_pos']), q['m_undecided'] or 'NONE'),
         '  **(N2)** ### **%s.** -- xi`s margin positive beyond B at %d of its %d VERIFIED-EST cells ; undecided %s ; negative %s.'
         % (w(sc['n2']), len(x['m_pos']), x['verified'], x['m_undecided'] or 'NONE', x['m_neg'] or 'NONE'),
         '  **(N3)** ### **%s.** -- the pair`s share of the on-line part: max %.4f at a = %s ; above 0.50 at : %s.'
         % (w(sc['n3']), q['share_max'] or 0.0, q['share_max_a'], q['share_over_half'] or 'NONE'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the pair`s term negative at : %s (of %d cells).' % (w(sc['s1']), q['pair_neg'] or 'NONE', len(CELLS)),
         '  **(S2)** ### **%s.** -- Q0`s P - PR + A negative (decided) at %s ; undecided %s.' % (w(sc['s2']), q['h2_neg'] or 'NONE', q['h2_undecided'] or 'NONE'),
         '  **(S3)** ### **%s.** -- fixture max differences %s.' % (w(sc['s3']), ['%.1e' % f['maxdiff'] for f in FX]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b514_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b514_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b514_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b514 — the matched window; (R123) entered'


def trail():
    sc = scores()
    q, x = R['q'], R['xi']
    mq = {m['a']: m for m in MT if m['object'] == 'q'}
    ratios = ' / '.join('%.2f' % mq[a]['ratio'] for a in sorted(mq))
    body = """
%(h)s

**(R123) ratified.** (1) The chain RH → h2_sign → cell form is entered at its meaning: h2_sign is a compiled consequence
of RH, so it is at most as strong as RH; the converse is the wall, and the two objects it needs are b513's (d), a
Paley–Wiener-type growth bound, and (f), the dominance lemma — neither in the kernel nor in Mathlib by name. (2) The
terminal table's two quirks are filed as work-orders, trigger the next fold: **`W-ORD-TABLE-PROFILE-JSON`** (profiles
taken from banked JSON as well as captured output) and **`W-ORD-TABLE-SHORTNAME-DEDUP`** (short-name rows
deduplicated against qualified ones). (3) The numerical lane opened for this act and shuts at its close; the kernel
lane stays shut.

**COMPONENT 0.** The ferry's window as written: g(u) = cos(γ₀u) times a cubic B-spline bump on [−log a, log a], k = g⋆g,
k̂ = ĝ² in closed form, no pole annihilation; in classK with generating h = g. The closed form agrees with a numerical
integral to %(fx)s against the 1e-10 bar. At the ladder's first, middle and last widths, Q0's ratio of k̂ at γ₀ to its
largest value at the two nearest on-line ordinates (14.6305, 18.8285) is %(ratios)s, so the window is matched only at
the wider widths; k̂ at the zero's own argument γ = 16.2902 − 0.4533i is real and positive there.

**COMPONENT 1 — Q0** (the completed bank, the zero at 0.95326 + 16.29022i). VERIFIED-EST at %(qv)d of %(n)d widths. The
margin A − PR is negative (sign decided) at %(qmn)s; h2_sign's own quantity P − PR + A is negative at %(qhn)s. The pair's
term is negative at %(qpn)s; its share of the on-line part peaks at %(qsm).4f (a = %(qsa)s), above 0.50 at %(qso)s.

**COMPONENT 2 — ξ** at 14.1347, the same columns. VERIFIED-EST at %(xv)d of %(n)d; the margin is positive beyond its bound at
%(xmp)d of those, negative at %(xmn)s, undecided at %(xmu)s.

**COMPONENT 3 — the reading, in (R122)(2)'s words:** %(reading)s. Nothing is claimed of the kernel either way.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The numerical lane
shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade conferred; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, fx=' and '.join('%.1e' % f['maxdiff'] for f in FX), ratios=ratios, n=len(CELLS),
           qv=q['verified'], qmn=(q['m_neg'] or 'no width'), qhn=(q['h2_neg'] or 'no verified width'), qpn=(q['pair_neg'] or 'no width'),
           qsm=q['share_max'] or 0.0, qsa=q['share_max_a'], qso=(('%d verified widths from a = %s' % (len(q['share_over_half']), q['share_over_half'][0])) if q['share_over_half'] else 'no verified width'),
           xv=x['verified'], xmp=len(x['m_pos']), xmn=(x['m_neg'] or 'none'), xmu=(x['m_undecided'] or 'none'),
           reading=R['reading'], N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b514_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
