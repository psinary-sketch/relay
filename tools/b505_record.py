# -*- coding: utf-8 -*-
"""b505_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL, CLOSING AS REGISTERED UNDER (R116)(1).

### `python tools/b505_record.py components | desk | trail`
### Component 1 banked; Component 2 REFUSED AT ITS FIXTURE, the count unread; Component 3 not run; the
### (R115)(1)/(2) annotations NOT executed here -- they wait for b506`s measured count.
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


C1 = json.loads(read('b505_c1.json'))
LOG = read('b505_c2_log.txt')
DIAG = read('b505_c2_fixture_diagnosis.txt')
REFUSED = '### FIXTURE FAILED ; no count read' in LOG and not os.path.exists(os.path.join(D, 'b505_c2_results.json'))
n1 = (C1['c1_frac'] == '2/3' and C1['c2_frac'] == '4/3' and C1['exact_fail'] == 0 and C1['lam_agree'] == C1['lam_n'] == 4095)


def components():
    L = ['=' * 104, 'b505 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 1.'] + read('b505_c1.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 2 -- THE LOG, VERBATIM.'] + LOG.rstrip(NL).split(NL)
    L += ['', '### ### **COMPONENT 2 REFUSED AT ITS FIXTURE, AS REGISTERED: %s.** ### No edge was computed, no box' % REFUSED,
          '### wound, no count read; `b505_edges.jsonl` and `b505_c2_results.json` do not exist.',
          '### The diagnosis, run after the refusal and reading only |Z| at the banked zeros (no count):']
    L += ['    ' + x for x in DIAG.rstrip(NL).split(NL)]
    L += ['### ### **REGISTERED GATE RE-EXAMINED : NOT REACHED** -- the re-examination was the fixture, and the fixture',
          '### refused. What it read: 146 of 148 banked zeros at |Z| < 1e-10; the two above it, at t = 149.343 and 149.718,',
          '### lie 4.6e-11 and 3.8e-11 from zeros Newton reaches at |Z| 1e-38. ### The bank`s ordinates are good to 6.1e-11;',
          '### the bar was finer than |Z`| times that. ### **THE BAR WAS THE SEAT`S, AND IT WAS WRONG; THE REFUSAL WAS CORRECT.**',
          '', '### COMPONENT 3 -- NOT RUN: its tool refuses unless Component 2 closed the bank, and Component 2 read nothing.',
          '### COMPONENT 4 -- DEFERRED by the order. ### THE ANNOTATIONS OF (R115)(1)/(2) -- NOT EXECUTED, under (R116)(1).',
          '=' * 104]
    io.open(os.path.join(D, 'b505_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-14:]))


def desk():
    L = ['=' * 104, 'b505 -- THE DESK. ### **CLOSED AS REGISTERED UNDER (R116)(1).**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- c1 = %s, c2 = %s, the exact test failing at %d of 10000 n; LAMQ agreeing at %d of %d,'
         % ('HELD' if n1 else 'REFUTED', C1['c1_frac'], C1['c2_frac'], C1['exact_fail'], C1['lam_agree'], C1['lam_n']),
         '    largest disagreement %.1e at n = %d.' % (C1['lam_worst'], C1['lam_worst_n']),
         '  **(N2)** ### **NOT SCORABLE.** -- Component 2 refused at its fixture; no count was read.',
         '  **(N3)** ### **NOT SCORABLE.** -- Component 3 did not run; the bank was not shown complete.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **NOT SCORABLE.** -- the M column was never counted.',
         '  **(S2)** ### **NOT SCORABLE.** -- the whole-strip count was never read.',
         '  **(S3)** ### **NOT SCORABLE.** -- no tail was computed against a bound.',
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 2.**' % (int(n1), int(not n1)),
         '### ### **THE SEAT`S : REGISTERED 3 ; HELD 0 ; REFUTED 0 ; NOT SCORABLE 3.**',
         '### ### **THE SEAT`S OWN DEFECT: the fixture bar |Z| < 1e-10 was finer than the bank carries (|Z`| x 6.1e-11).**',
         '=' * 104]
    io.open(os.path.join(D, 'b505_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2='NOT SCORABLE', n3='NOT SCORABLE', s1='NOT SCORABLE', s2='NOT SCORABLE', s3='NOT SCORABLE'),
              io.open(os.path.join(D, 'b505_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b505 — the Epstein control for Q0: the decomposition holds exactly; the completeness count refused at its own fixture'


def trail():
    body = """
%(h)s

**(R115) ratified**, as amended a second time: every Epstein margin of record UNVERIFIED; the control of
record Q0 = x² + xy + 6y², discriminant −23, class number 3; the kernel tested only on a bank shown complete
to its own height; an explicit formula pairs one function's zeros with its own places side; premises read
from the files they name. **(R116)(1)** closes this act as registered.

**COMPONENT 1.** r_Q0(n) = (2/3)·A(n) + (4/3)·a(n) exactly at all 10,000 n — A the coefficients of
ζ(s)L(s, χ₋₂₃), a those of η(z)η(23z) — least squares returning 0.666666666666667 and 1.333333333333339.
The coefficients of −Z0′/Z0 formed from the decomposition by an exact Dirichlet inverse agree with b325's
LAMQ at 4095 of 4095 n, largest difference %(worst).1e at n = %(wn)d.

**COMPONENT 2 — REFUSED AT ITS FIXTURE, AS REGISTERED.** The seat's evaluator (Chowla–Selberg, after a
factor-2 error in its first version was found and declared before the seal) agrees with route A to 4.9e-11.
The registered bar, |Z| < 1e-10 at every banked zero, failed at 2 of 148 — t = 149.343 and 149.718, |Z| 4.9e-10 —
whose ordinates lie 4.6e-11 and 3.8e-11 from zeros Newton reaches at |Z| 1e-38. The bar was finer than |Z′| times
the bank's ordinate precision: **the seat's defect, and the refusal was correct.** No count was read.
**COMPONENT 3** did not run; **COMPONENT 4** deferred; the (R115)(1)/(2) annotations wait for b506's count.

**(N1) HELD · (N2) NOT SCORABLE · (N3) NOT SCORABLE**; the seat's three NOT SCORABLE. **The numerical lane
shuts at this act's close** and reopens for b506 under (R116)(3). No grade conferred; nothing deposits; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, worst=C1['lam_worst'], wn=C1['lam_worst_n'])
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b505_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
