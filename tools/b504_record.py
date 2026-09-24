# -*- coding: utf-8 -*-
"""b504_record.py -- THE DESK AND THE TRAIL. ### `python tools/b504_record.py desk | trail`"""
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
R = json.loads(io.open(os.path.join(D, 'b504_results.json'), encoding='utf-8').read())
w = lambda v: 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')
n1 = R['verified'] >= 110
n2 = all(e['kind'] == 'VERIFIED' for e in R['eight']) and len(R['eight']) == 8
n3 = R['rise'] is True
n4 = None if all(R['eps'][q]['verified'] == 0 for q in ('325', 'd')) else all(R['eps'][q]['n4_fail'] == 0 for q in ('325', 'd'))
s1 = n2
s2 = R['eps']['325']['verified'] == 0 and R['eps']['d']['verified'] > 0
s3 = R['verified'] < 110


def desk():
    L = ['=' * 104, 'b504 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- *"at least 110 of 119 verify"* -- ### **%d** ; the unverified %d are ALL ESTIMATE-SHORT'
         % (w(n1), R['verified'], R['n'] - R['verified']),
         '    (within x2.6 of their bounds): b501`s estimate, not the transform and not the image.',
         '  **(N2)** ### **%s.** -- *"all eight cells from a = 13.637 verify"* -- %s'
         % (w(n2), ['%.3f %s' % (e['a'], e['kind']) for e in R['eight']]),
         '  **(N3)** ### **%s.** -- *"the rise after 13.153 stands"* -- %d verified cells after the minimum, m rising'
         % (w(n3), R['after13']),
         '    across all. ### **THE FIRST READING SAID False, AND WAS THE INSTRUMENT`S DEFECT**: the test counted the',
         '    minimum`s own cell (exact a 13.152946437...) as the first cell after it. ### b503`s tool carries the same',
         '    predicate; its True passed by 4e-10 against a rounded literal, and its count of five was four and the minimum.',
         '  **(N4)** ### **%s.** -- *"the Epstein margin positive and above its floor at every verified cell"* -- ### **NO' % w(n4),
         '    EPSTEIN CELL VERIFIES UNDER EITHER KERNEL, SO THE STATEMENT IS OVER AN EMPTY SET AND IS VACUOUS**, neither held',
         '    nor refuted. ### b325`s kernel misses by %.2f to %.2f; the derived kernel by %.1e to %.1e -- against'
         % (R['eps']['325']['min_abs_r'], R['eps']['325']['max_abs_r'], R['eps']['d']['min_abs_r'], R['eps']['d']['max_abs_r']),
         '    quadrature bounds near 1e-7, because the Epstein bank stops at 149.72 and its truncation is in no bound.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the eight cells verify.' % w(s1),
         '  **(S2)** ### **%s.** -- b325`s kernel verifies %d, as predicted; ### the derived kernel verifies %d, NOT the'
         % (w(s2), R['eps']['325']['verified'], R['eps']['d']['verified']),
         '    narrower cells the seat predicted -- its best residual is 4.5e-05, at the wide end, still far above its bound.',
         '  **(S3)** ### **%s.** -- fewer than 110 verify : %d.' % (w(s3), R['verified']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; VACUOUS %d.**' % ([n1, n2, n3, n4].count(True), [n1, n2, n3, n4].count(False), [n1, n2, n3, n4].count(None)),
         '### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**' % ([s1, s2, s3].count(True), [s1, s2, s3].count(False)),
         '=' * 104]
    io.open(os.path.join(D, 'b504_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, s2=s2, s3=s3),
              io.open(os.path.join(D, 'b504_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b504 — the chain on one transform: 109 of 119 verified, all eight wide cells among them; the Epstein control verifies at no cell'


def trail():
    body = """
%(h)s

**(R114) ratified.** One instrument, one transform: the chain's zero side, archimedean term and pole term all by
the exact transform (`b326_closure.hhat_exact`, `mellin_exact`); the trapezoid transform retired from the chain
and kept as a fixture; verification counts the consistent residual; b503's 86 is the count of record before this
act and its 64 is not cited. The grid follows the bank: nv the smallest value not below 8193 that puts the image
`2 pi / dv` above T + 200 = 10077.78.

**COMPONENT 1.** The fixture reproduced b503's consistent residual at a = 4.061553, 5.196152, 10.392193 to about
1e-15. The grid rule moved 17 cells above 8193, the largest to **nv 8492 at a = 14.107**, at 31 s a cell; no cell
reached the ceiling. Compute %(sec).0f s.

**COMPONENT 2.** **%(ver)d of 119 verify on the consistent residual**, the bound recomputed under the exact
transform by b501's rule. **All eight cells from a = 13.637 verify** — with the image above T + 200 the lobe copy
leaves the zero side as it already lay outside the archimedean term. The ten unverified are all ESTIMATE-SHORT,
within ×2.6 of their bounds. The three extrema — 4.061553, 5.196152, 13.152946 — are verified.

**COMPONENT 3.** On the verified set: minimum at 4.061553, maximum at 5.196152, minimum at 13.152946; **the rise
after 13.153 stands** across the %(after)d verified cells beyond it; c/a² has the least residual. The first reading of
the rise said False — the test counted the minimum's own cell (exact a 13.152946437…) as the first cell after
it; repaired, both banked. **b503's tool carries the same predicate**: its True passed by 4e-10 against a
rounded literal, and its count of five was four cells and the minimum. The minimum at 13.152946 and the
maximum at 5.196152 each sit within one cell of extrema of the terms of the lowest zero (14.1347) and the
fourth (30.4249); the minimum at 4.061553 of the fourth alone.

**COMPONENT 4 — THE EPSTEIN CONTROL, ONE TRANSFORM, TWO KERNELS.** Zero side by b326's route (146 on-line zeros
to 149.72 and the two off-line). **Under b325's kernel — the control of record, banked at b477 and re-run at
b502 — no cell verifies; its residual is 0.53 to 9.4 at every cell**, as b326 found. **Under b326's derived
kernel — exactly twice b325's — no cell verifies either**; its residual falls to 4.5e-05 at the wide end,
against quadrature bounds near 1e-7, because the Epstein bank stops at 149.72 and its truncation is in no
bound. Smallest margins: +0.302 (b325) and +0.831 (derived), both at a = 14.107. **The Epstein margins of b477
and b502 were read under a kernel that does not close the Epstein explicit formula; routed.**

**(N1) %(n1)s by one cell · (N2) %(n2)s · (N3) %(n3)s · (N4) %(n4)s** — no Epstein cell verified under either kernel.
The seat's own: **(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s.** **The numerical lane shuts at this act's close.** No grade
conferred; nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell
of this act is a statement about RH.
""" % dict(h=HEADING, sec=R['seconds'], ver=R['verified'], after=R['after13'], n1=w(n1), n2=w(n2), n3=w(n3), n4=w(n4),
           s1=w(s1), s2=w(s2), s3=w(s3))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b504_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'desk': desk, 'trail': trail}[sys.argv[1]]()
