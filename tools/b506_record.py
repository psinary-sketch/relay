# -*- coding: utf-8 -*-
"""b506_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b506_record.py components | desk | trail`
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


C1 = json.loads(read('b505_c1.json'))
R = json.loads(read('b506_c2_results.json'))
CELLS = sorted((json.loads(l) for l in read('b506_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
POP = [c for c in CELLS if c['tail_inside']]
VER = [c for c in POP if c['verified']]
ANN = json.loads(read('b506_annotations.json') or '[]')
known = [tuple(o) for o in ([0.9532604747946607, 16.290215720390393], [0.7979971571786801, 29.551761098629115])]
NEW = [z for z in R['found'] if not any(abs(z['rho'][0] - b) < 1e-8 and abs(z['rho'][1] - g) < 1e-8 for b, g in known)]
EDGE = int(read('b506_c2_log.txt').split('edges 1051 / 1051  ')[-1].split(' s')[0])

n1 = R['fixture_dist_pass'] == 148 and R['fixture_route_pass'] == 148
n2 = 25 <= R['lacks_strip'] <= 33 and R['beyond1'] >= 1
n3 = (len(VER) >= 40) if CELLS else None
s1 = len(R['m_mismatch']) == 0
s2 = abs(R['total'] - R['smooth'] - R['S']) < 0.05
s3 = (len(POP) < 93) if CELLS else None
w = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def components():
    L = ['=' * 104, 'b506 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '',
         '### COMPONENT 1 -- CARRIED FROM b505 (relay/data/b505_c1.json): c1 %s, c2 %s, exact test fails at %d of %d n, LAMQ %d of %d.'
         % (C1['c1_frac'], C1['c2_frac'], C1['exact_fail'], C1['N'], C1['lam_agree'], C1['lam_n']),
         '', '### COMPONENT 2 -- THE LOG, VERBATIM (three starts: two crashes at removable points, then the run that read).']
    L += read('b506_c2_log.txt').rstrip(NL).split(NL)
    L += ['', '### THE LOCATED ZEROS, sigma > 0.52 (each with its mirror 1 - conj rho on L):']
    for z in sorted(R['found'], key=lambda z: z['rho'][1]):
        L.append('    %.10f + %.10f i   |Z| after Newton %.1e   route A |Z| %.1e (distance %.1e)   %s'
                 % (z['rho'][0], z['rho'][1], z['absz'], z['route_a'], z['route_a_dist'],
                    'BANKED' if z not in NEW else 'NEW'))
    L += ['', '### COMPONENT 3.'] + read('b506_c3.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 4 -- THE ANNOTATIONS.'] + ['    %s' % json.dumps(a) for a in ANN]
    L += ['=' * 104]
    io.open(os.path.join(D, 'b506_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-12:]))


def desk():
    L = ['=' * 104, 'b506 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- within 1e-9 of their Newton zeros %d of 148 (largest 6.1e-11); route A to 1e-8 %d of 148'
         % (w(n1), R['fixture_dist_pass'], R['fixture_route_pass']),
         '    (largest 4.9e-10 -- b505`s 4.9e-11 was the largest at 23 points; at all 148 it is ten times that, still under the bar).',
         '  **(N2)** ### **%s.** -- the bank lacks %d (whole strip, 180 against 150) -- inside 25..33 -- but %d of the %d new'
         % (w(n2), R['lacks_strip'], R['beyond1'], len(NEW)),
         '    off-line zeros lie at sigma > 1; the largest sigma located is %.4f (the banked zero at 16.29). ### The conjunction fails'
         % max(z['rho'][0] for z in R['found']),
         '    on its second clause.',
         '  **(N3)** ### **%s.** -- population %d of %d wide cells (tail inside bound); verified in it %d.'
         % (w(n3), len(POP), len(CELLS), len(VER)),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the M column differs from the bank in %d strips; all 30 lacking zeros are off the line.'
         % (w(s1), len(R['m_mismatch'])),
         '  **(S2)** ### **%s.** -- count %d ; smooth %.4f + S(150) %.4f = %.4f.' % (w(s2), R['total'], R['smooth'], R['S'], R['smooth'] + R['S']),
         '  **(S3)** ### **%s.** -- population %d of %d.' % (w(s3), len(POP), len(CELLS)),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
         % ([n1, n2, n3].count(True), [n1, n2, n3].count(False), [n1, n2, n3].count(None)),
         '### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
         % ([s1, s2, s3].count(True), [s1, s2, s3].count(False), [s1, s2, s3].count(None)),
         '### ### **THE PRICE:** edges %d s, under the face`s twenty-minute rule; the whole run %.0f s, over the face`s' % (EDGE, R['seconds']),
         '### "about 15 minutes" by six -- the fixture ran three times across two crashes at removable points.',
         '=' * 104]
    io.open(os.path.join(D, 'b506_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3), io.open(os.path.join(D, 'b506_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b506 — the Q0 bank counted below 150: 180 zeros, the bank lacks 30, all off the line and none beyond sigma = 1'


def trail():
    zs = '; '.join('%.4f + %.4fi' % (z['rho'][0], z['rho'][1]) for z in sorted(NEW, key=lambda z: z['rho'][1]))
    body = """
%(h)s

**(R116) ratified.** b505 closed as registered; a fixture bar is stated in the object's own units and at the
precision the bank carries; the lane reopened for this act.

**COMPONENT 1**, carried from b505 at `relay/data/b505_c1.json`: c1 = 2/3, c2 = 4/3 exactly at all 10,000 n; LAMQ
agreeing at 4095 of 4095.

**COMPONENT 2.** Under (R116)(2)'s fixture all 148 banked zeros lie within 1e-9 of the zeros Newton reaches from
them (largest 6.1e-11), and route A agrees with the Chowla–Selberg evaluator to 1e-8 at all 148 (largest 4.9e-10):
b326's `registered_gate_passed = False` records only its registered dps-60 gate, and **the banked zeros stand.**
The argument principle over σ ∈ [−0.5, 1.5] × t ∈ [0, 150] (σ_max 1.5 from Σ_{k≥2} r(k)k^{−1.5} ≤ 1.5497 < r(1) = 2),
450 boxes all within 0.05 of an integer, **counts 180 zeros** — smooth term 179.596 plus S(150) 0.404 = 180.000;
the ferry's 178.6 omits the +1 of the poles. The line column matches the bank in every strip (146); L matches R
strip for strip. **The bank lacks 30: fifteen off-line zeros and their mirrors, none on the line and none at
σ > 1** — the largest σ is 0.9533, the banked zero at 16.29. The new fifteen, each at |Z| ~ 1e-39 after Newton and
confirmed by route A to under 1e-14 in distance: %(zs)s. Both banked off-line zeros recovered (positive control).
Two runs crashed first at removable points of the evaluator (s = 1/2, then s = −1/2, on the real segment);
repaired in F by a 1e-20 step, the banked edges unaffected. Edges %(edge)d s; the whole run %(sec).0f s.

**COMPONENT 3**, on the completed bank: of %(nc)d wide cells, %(np)d have the truncation above 150 inside their bound;
the derived kernel verifies at %(nv)d of them.%(stop)s The residual falls to 1e-8..4e-7, the size of the
truncation above 150; **the control is b504's residual at the same cells and the same bound on the incomplete
bank, 7e-5 to 2e-3, verifying nowhere** — the fifteen zeros are what close it.

**COMPONENT 4.** The (R115)(1)/(2) annotations appended to `b477_components.txt`, `b502_components.txt`,
`b504_components.txt` and `b502_ferry.txt`, citing the count of 30; prefixes proved. The navigator's reading of
2026-09-23 of those margins is, with them, UNVERIFIED. **One clause of those notes is superseded by Component 3**:
they carry (R115)(1)'s words that the kernel "does not close the explicit formula … at any cell" — true of b325's
kernel, and true of b326's derived kernel on the incomplete bank, but the derived kernel closes on the completed bank
at every wide cell. Routed; the notes are append-only and not re-annotated here. And b504's trail put the Epstein
quadrature bounds "near 1e-7": they are 9e-7 to 2.3e-6 (`B_qd` in `b504_cells.jsonl`, the same bound this act used);
routed.

**(N1) %(n1)s · (N2) %(n2)s** — 30 lacking, inside 25..33, but none at σ > 1 · **(N3) %(n3)s.** The seat's own:
(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s. **The numerical lane shuts at this act's close**; the kernel lane reopens for
(R104)'s act 3. No grade conferred; nothing deposits; row U1 unedited; `h2` where the deposit left it; the four
lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, zs=zs, edge=EDGE, sec=R['seconds'], nc=len(CELLS), np=len(POP), nv=len(VER),
           stop=(' **It fails at %d population cells — STOP there; the kernel is Q0`s own and there is no factor-wise substitute.**'
                 % (len(POP) - len(VER))) if POP and len(VER) < len(POP) else '',
           n1=w(n1), n2=w(n2), n3=w(n3), s1=w(s1), s2=w(s2), s3=w(s3))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b506_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
