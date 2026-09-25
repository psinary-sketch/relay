# -*- coding: utf-8 -*-
"""b520_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b520_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (7)'s, recomputed from the cells and the reach.
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


R = json.loads(read('b520_results.json') or '{}')
RE = json.loads(read('b520_reach.json') or '{}')
ROWS = sorted((json.loads(l) for l in read('b520_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
w = lambda v: 'HELD' if v else 'REFUTED'


def scores():
    q, x = R.get('q', {}), R.get('xi', {})
    cross = q.get('cross_minus_one')
    qcells = [c for c in ROWS if 'q' in c]
    return dict(
        n1=cross is not None and 20.0 <= cross <= 45.0,
        n2=cross is not None and q.get('growth_fraction_at_cross') is not None and q['growth_fraction_at_cross'] >= 0.5,
        n3=len(x.get('h2_pos') or []) == x.get('verified', -1),
        n4=(RE.get('reach', {}).get('q') or 0) >= 45.0,
        s1=cross is not None,
        s2=bool(ROWS) and all(c[o]['growth_fraction'] < 0.5 for c in ROWS for o in ('q', 'xi') if o in c),   # ### G is the window's, at the pair's delta: every width read
        s3=RE.get('reach', {}).get('q') == 60.0)


def components():
    L = ['=' * 132, 'b520 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    L += read('b520_report.txt').rstrip(NL).split(NL) + ['', '### THE REACH SCAN, EVERY WIDTH (error terms only):']
    for s in RE.get('scan', []):
        L.append('  a=%-5.0f ' % s['a'] + ' ; '.join('%s E_tail %.2e B` %.2e (%.1e) lamq %s' % (o, s[o]['Etail'], s[o]['Bprime'], s[o]['tail_over_Bprime'], s[o]['lamq_ok'])
                                                    for o in ('q', 'xi') if o in s))
    L += ['', '### A DECLARED POST-RUN READ OF A PRIOR BANK (defect (a)): b519`s variant-(B) Q0 cells, E_tail against B` at the ladder`s widths:']
    b19 = sorted((json.loads(l) for l in read('b519_cells_B.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
    over = [c['a'] for c in b19 if c['q']['Etail'] > c['q']['Eu'] + c['q']['Ek'] + c['q']['Eround']]
    L.append('  widths where E_tail > B` : %d of %d' % (len(over), len(b19)))
    for c in b19[::20] + b19[-1:]:
        x = c['q']
        bp = x['Eu'] + x['Ek'] + x['Eround']
        L.append('  a=%-10.6f E_tail %.2e ; B` %.2e ; ratio %.2e ; P - PR + A over B %.1e' % (c['a'], x['Etail'], bp, x['Etail'] / bp, x['h2'] / x['B']))
    L += ['', '### THE RUN LOG:'] + read('b520_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b520_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    q, x = R['q'], R['xi']
    L = ['=' * 104, 'b520 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- the narrowest read width where Q0`s pair ratio is <= -1 : %s (against [20, 45]).' % (w(sc['n1']), q['cross_minus_one'] or 'NONE'),
         '  **(N2)** ### **%s.** -- the realized fraction G / e^{delta L} at that width : %s (against 0.5).' % (w(sc['n2']), q['growth_fraction_at_cross'] or 'NO SUCH WIDTH'),
         '  **(N3)** ### **%s.** -- xi positive beyond B at %d of its %d VERIFIED-EST cells within reach%s.'
         % (w(sc['n3']), len(x['h2_pos']), x['verified'], (' ### VACUOUS: NO VERIFIED-EST xi CELL' if x['verified'] == 0 else '')),
         '  **(N4)** ### **%s.** -- Q0`s reach : %s (stopped at %s).' % (w(sc['n4']), RE['reach']['q'], RE['stop']['q']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the pair ratio reaches -1 first at %s.' % (w(sc['s1']), q['cross_minus_one'] or 'NO READ WIDTH'),
         '  **(S2)** ### **%s.** -- the largest realized fraction G / e^{delta L} at any width read : %.4f (G is the window`s, at the pair`s delta; the widths read are xi`s, Q0 having none).'
         % (w(sc['s2']), max((c[o]['growth_fraction'] for c in ROWS for o in ('q', 'xi') if o in c), default=float('nan'))),
         '  **(S3)** ### **%s.** -- Q0`s reach %s against 60.' % (w(sc['s3']), RE['reach']['q']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b520_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b520_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b520_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b520 — variant (B) widened past the ladder; (R129) entered'


def trail():
    sc = scores()
    q, x = R['q'], R['xi']
    body = """
%(h)s

**(R129) ratified.** (1) The design is settled and the missing dimension is width: the zero at the on-line point gives
the sign in every variant; notching costs more than it gains; edge mass realizes the growth (d) allows. **The record's
reading is entered: sign from a zero on the line; dominance from width, not from design.** (2) The window of (f)(i) is
variant (B), the edge-weighted plateau with the zero factor at γ₀, as banked at b519; its kernel statement runs after
this act. (3) The numerical lane opened for this act; the kernel lane reopens after it for (f)(i) on variant (B).

**COMPONENT 0 — the reach.** One pass in increasing width a = 15 … 60, the tail bound against the rest of the cell's
bound B′ = E_u + E_k + E_round, and Q0's prime-channel table to n = 4096: **Q0's reach %(rq)s (stopped at %(sq)s); ξ's
%(rx)s (stopped at %(sx)s)**. Past a reach nothing is banked but the error terms that stopped it. nv: none — the
transform is closed form. **Found here, by a declared read of b519's bank: Q0's tail bound exceeds the rest of the
cell's bound at every width of b519's ladder for variant (B), by 1.0e3 to 1.2e5, so b518's and b519's Q0
verifications were bounds dominated by the tail majorant** — valid upper bounds, the sign decided beyond them, but the
tail's and not the quadrature's. The reach reading this act registered could therefore read no Q0 cell at all.

**COMPONENT 1 — Q0 with variant (B)** at %(nq)d widths read. VERIFIED-EST at %(qv)d. P − PR + A negative beyond its bound
at %(qn)s. The pair's ratio to the rest reaches −1 first at %(cross)s; at the widest width read (a = %(wa)s) it is
%(wr)s.

**COMPONENT 2 — ξ** at 14.1347 on the same grid within its reach: VERIFIED-EST at %(xv)d of %(nx)d read, positive beyond its
bound at %(xp)d%(xvac)s.

**COMPONENT 3 — the reading, in (R127)(2)'s words:** %(reading)s. Nothing is claimed of the kernel either way.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The
numerical lane shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade
conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement
about RH.
""" % dict(h=HEADING, rq=RE['reach']['q'], sq=(RE['stop']['q'] or {}).get('a', 'none'), rx=RE['reach']['xi'], sx=(RE['stop']['xi'] or {}).get('a', 'none'),
           nq=q['cells'], qv=q['verified'], qn=(q['h2_neg'] or 'no width'), cross=(q['cross_minus_one'] or 'no width read'),
           wa=q['widest_a'], wr=('%+.4e' % q['widest_ratio']) if q['widest_ratio'] is not None else 'none',
           xv=x['verified'], nx=x['cells'], xp=len(x['h2_pos']), xvac=(' — VACUOUS, no verified cell' if x['verified'] == 0 else ''),
           reading=R['reading'], N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), N4=w(sc['n4']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b520_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
