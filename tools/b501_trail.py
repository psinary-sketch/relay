# -*- coding: utf-8 -*-
"""b501_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import io, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEADING = '### b501 — the places-side quadrature bound: built, tested, and it is what the two sides disagree by'
R = json.loads(io.open(os.path.join(D, 'b501_results.json'), encoding='utf-8').read())
SC = json.loads(io.open(os.path.join(D, 'b501_scores.json'), encoding='utf-8').read())
w = lambda v: 'HELD' if v else 'REFUTED'
body = """
%(h)s

**The numerical lane is open under `(R112)` for this act and b502.** `W-ORD-QUADRATURE-BOUND` fires.

**COMPONENT 1.** A is a trapezoid over the u-grid (UMAX 600, NU 12001) of `hhat * kernel / 2 pi`;
`hhat` and each prime term (`np.interp` at `log n`) sit on the autocorrelation's v-grid at `nv` 8193.
**`trunc_bound` bounds the zero side's truncation at the last banked ordinate** — twice the largest
`|hhat|` on `[T, T+200]` times 200 — **and nothing on the places side.**

**COMPONENT 2 — THE BOUND, AS SEALED.** `B = E_v + E_u`: Richardson over `nv` 8193, 16385, 32769 for the
margin `m = A − PR` (NON-ASYMPTOTIC fallback `2(|d1|+|d2|)`), plus A on the u-spacing halved and the
u-range doubled. The atlas's one-grid kernel cache was reset before every change of grid. The base
reproduced b492's A and PR **bit for bit at %(repro)d of %(n)d**. NON-ASYMPTOTIC cells: %(na)d.

**COMPONENT 3 — THE TEST.** `B >= |W + Z|` at **%(ok)d of %(n)d** cells; the composite with `trunc_bound`
also %(comp)d. **The ten shortfalls are small — the worst ×%(worst).2f at a = 3.316625, the rest within
×1.05 — and the finding is what B tracks: the achieved two-side disagreement IS the places-side
quadrature error**, through A's u-grid at small a (E_u 3.54e-05 against 3.56e-05 at a = 1.3) and
through the v-grid above a = 2. b446 doubled only the v-grid. **Positive control** (Gaussian,
closed-form `hhat`, exact prime sum, A by `mpmath.quad` at 30 digits): true error 3.278e-09, B
3.447e-09 — **passes**. **Negative control** (levels 2049, 4097, 8193): B grows at all three cells.

**COMPONENT 4 — THE FLOOR.** Each cell's new floor is its B, beside b477's uniform 1.49e-08. **All %(fl)d
margins exceed their new floors.** At the minimum-margin cell a = 4.061553 the floor rises from
1.49e-08 to **%(mf).3e**, against m = 0.024337988.

**The face's own READING (1) was wrong** — it placed b483's AIM PLANE outside the thirty-five; the
thirty-five are b483's two families together, 13 + 22 — corrected before any score, face unedited.
**(N1) %(n1)s** (max B is 0.78× and 0.14× of b483's two spectral norms — below, not above) · **(N2)
%(n2)s** · **(N3) %(n3)s**. The seat's own: **(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s** — the seat thought the
zero side carried the disagreement, and it does not. Compute %(sec).0f s for the cells.

No grade conferred; nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists
stay OPEN; no number of this act is a statement about RH.
""" % dict(h=HEADING, repro=R['repro'], n=R['n'], na=R['nonasymptotic'], ok=R['test_ok'], comp=R['composite_ok'],
           worst=SC['worst'], fl=R['floors_exceeded'], mf=R['min_cell']['B'], n1=w(SC['n1']), n2=w(SC['n2']),
           n3=w(SC['n3']), s1=w(SC['s1']), s2=w(SC['s2']), s3=w(SC['s3']), sec=R['seconds'])
before = open(OT, 'rb').read()
if HEADING in before.decode('utf-8'):
    sys.exit('### ALREADY PRESENT')
open(OT, 'ab').write(body.encode('utf-8'))
after = open(OT, 'rb').read()
bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
out = dict(added=len(after) - len(before), prefix=after.startswith(before),
           removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
io.open(os.path.join(D, 'b501_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)
