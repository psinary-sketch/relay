# -*- coding: utf-8 -*-
"""b502_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import io, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEADING = '### b502 — the ladder past sqrt(32) to sqrt(200): m(a) positive at every cell, a further minimum at 13.153; the lane shut'
R = json.loads(io.open(os.path.join(D, 'b502_results.json'), encoding='utf-8').read())
SC = json.loads(io.open(os.path.join(D, 'b502_scores.json'), encoding='utf-8').read())
w = lambda v: 'HELD' if v else 'REFUTED'
f = R['fits']
body = """
%(h)s

**COMPONENT 1 — THE LADDER EXTENDED.** b437's generator on **exact** a: boundaries `sqrt n` for the
42 prime powers in (32, 200] and 42 midpoints — **84 new cells**, a from 5.869808 to 14.106736, the
rounded a banked beside. At each: b492's recipe, the diagonal, the per-n prime terms (their sum equal
to PR within 1.4e-16), A, PR, the zero side, and the floor as **b501's bound computed at that cell by
b501's own tool** (the bound's base value equal to the chain's at every cell). Compute %(sec).0f s.

**COMPONENT 2 — THE TAIL.** Over all 119 cells: **m(a) is positive and above its floor at every
one**; no cell is within ten floors of zero; the smallest m/B is 2.47e+03. Past sqrt(32), m falls
steadily from 0.0352 to a **local minimum 0.000690365 at a = 13.152946** (the boundary of 173), then
rises to 0.001099 at the last cell. The extrema over the whole ladder are now three: the minimum at
4.061553, the maximum at 5.196152, and the minimum at 13.152946. **The new minimum is not explained
and is routed.**

**COMPONENT 3 — THE FITS, REGISTERED BEFORE THE RUN.** One-parameter least squares, RMS absolute
residual, on each set separately. New cells: (a) %(an).3e · (b) %(bn).3e · (c) %(cn).3e · **(d)
%(dn).3e**. Old: (a) %(ao).3e · (b) %(bo).3e · (c) %(co).3e · **(d) %(do).3e**. **(d) c/a^2 wins on
both.** A fit is a description of the chart and not a bound — and none of the four one-parameter
forms can describe the rise after 13.15.

**COMPONENT 4 — THE EPSTEIN CONTROL** (`W-ORD-EPSTEIN-ISOLATION`, priced at about five minutes, run).
The route reproduced b477 at a = 3.0 exactly. **Epstein margin negative at: NONE** — smallest
+0.302327 at a = 14.106736. **This is out of range, not a pass**: b334's crossings sit at widths 40
and 81, and the ladder stops at 14.1.

**(N1) %(n1)s · (N2) %(n2)s · (N3) %(n3)s.** The seat's own: **(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s.**

**THE NUMERICAL LANE IS SHUT AT THIS ACT'S CLOSE, under (R112).** No grade conferred; nothing
deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; **no cell of this
act is a statement about RH.**
""" % dict(h=HEADING, sec=R['seconds'], an=f['(a) c']['rms_new'], bn=f['(b) c/a']['rms_new'], cn=f['(c) c/log a']['rms_new'],
           dn=f['(d) c/a^2']['rms_new'], ao=f['(a) c']['rms_old'], bo=f['(b) c/a']['rms_old'], co=f['(c) c/log a']['rms_old'],
           do=f['(d) c/a^2']['rms_old'], n1=w(SC['n1']), n2=w(SC['n2']), n3=w(SC['n3']), s1=w(SC['s1']), s2=w(SC['s2']), s3=w(SC['s3']))
before = open(OT, 'rb').read()
if HEADING in before.decode('utf-8'):
    sys.exit('### ALREADY PRESENT')
open(OT, 'ab').write(body.encode('utf-8'))
after = open(OT, 'rb').read()
bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
out = dict(added=len(after) - len(before), prefix=after.startswith(before),
           removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
io.open(os.path.join(D, 'b502_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)
