# -*- coding: utf-8 -*-
"""b522_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b522_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (8)'s, recomputed from the banks.
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


R = json.loads(read('b522_results.json') or '{}')
RE = json.loads(read('b522_reach.json') or '{}')
CS = sorted((json.loads(l) for l in read('b522_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
w = lambda v: 'HELD' if v else 'REFUTED'


def scores():
    q = R.get('q', {})
    within = set(RE.get('within', []))
    cross = q.get('cross_minus_one')
    return dict(
        n1=all(float(a) in within for a in range(30, 61)),
        n2=cross is not None,
        n3=cross is not None and q.get('growth_fraction_at_cross') is not None and q['growth_fraction_at_cross'] >= 0.5,
        s1=bool(CS) and all(c['ratio'] > -1.0 for c in CS),
        s2=any(a < 30.0 for a in within),
        s3=bool(CS) and all(c['verified'] and c['h2'] > c['B'] for c in CS))


def components():
    L = ['=' * 132, 'b522 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    L += read('b522_report.txt').rstrip(NL).split(NL)
    L += ['', '### THE RUN LOG:'] + read('b522_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b522_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    q = R['q']
    within = RE['within']
    L = ['=' * 104, 'b522 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- widths of a = 30..60 IN : %d of 31 ; OUT among them : %s.'
         % (w(sc['n1']), sum(1 for a in range(30, 61) if float(a) in within), [a for a in range(30, 61) if float(a) not in within] or 'NONE'),
         '  **(N2)** ### **%s.** -- the pair`s ratio reaches -1 first at : %s ; most negative ratio read %s.'
         % (w(sc['n2']), q['cross_minus_one'] or 'NO READ WIDTH', q['ratio_min']),
         '  **(N3)** ### **%s.** -- G / e^{delta L} at the crossing : %s (against 1/2).' % (w(sc['n3']), q['growth_fraction_at_cross'] or 'NO CROSSING'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the ratio above -1 at every read width ; most negative %s.' % (w(sc['s1']), q['ratio_min']),
         '  **(S2)** ### **%s.** -- IN widths below 30 : %s.' % (w(sc['s2']), [a for a in within if a < 30.0] or 'NONE'),
         '  **(S3)** ### **%s.** -- VERIFIED-EST %d of %d read, positive beyond bound %d.' % (w(sc['s3']), q['verified'], q['cells'], len(q['h2_pos'])),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in read('b522_defects.txt').rstrip(NL).split(NL) if l] or ['    NONE FOUND.']) + ['=' * 104]
    io.open(os.path.join(D, 'b522_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b522_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b522 — variant (B) at p = 7, the reach read per width; (R131) entered'


def trail():
    sc = scores()
    q = R['q']
    body = """
%(h)s

**(R131) ratified.** (1) b521's result stands. The tail falls with width on a = 15 … 60 at every order scanned, so
**(R130)(2)'s claim that the majorant grows like e^{L/2} on this grid is refuted by the record, and is so marked here**;
the increasing-width stop rule, which stops at the narrowest width where the tail is largest, **is retired**. (2) The
reach is read per width: a width is within reach iff E_tail ≤ B′ at that width. (3) Choice (B): variant (B) at p = 7
under (2); p = 9 not run. (4) The numerical lane opened for this act and shuts at its close; the kernel lane takes
(f)(i) on variant (B) after it.

**COMPONENT 0 — the reach table.** a = 15 … 60, every width computed: **%(nin)d of 46 within reach**; out at %(out)s.
Out widths are banked as error terms only.

**COMPONENT 1 — Q0 with variant (B) at p = 7**, γ₀ = 16.290216, at every width within reach: VERIFIED-EST at %(qv)d of
%(nq)d; P − PR + A negative beyond its bound at %(qn)s; the tail's share of the bound at most %(ts)s. The pair's ratio to
the rest reaches −1 first at %(cross)s; its most negative value read is %(rmin)s; at the widest cell read (a = %(wa)s)
it is %(wr)s.

**COMPONENT 2 — ξ cited from b520:** VERIFIED-EST 46 of 46, positive at all. **COMPONENT 3 — the reading, in
(R127)(2)'s words:** %(reading)s.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The numerical lane
shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade conferred; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, nin=len(RE['within']), out=(RE['outside'] or 'no width'), qv=q['verified'], nq=q['cells'],
           qn=(q['h2_neg'] or 'no width'), ts=('%.3f' % q['tail_share_max']) if q['tail_share_max'] is not None else 'none',
           cross=(q['cross_minus_one'] or 'no width read'), rmin=('%+.4f' % q['ratio_min']) if q['ratio_min'] is not None else 'none',
           wa=q['widest_a'], wr=('%+.4e' % q['widest_ratio']) if q['widest_ratio'] is not None else 'none', reading=R['reading'],
           N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b522_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
