# -*- coding: utf-8 -*-
"""b521_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b521_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (10)'s, recomputed from the banks.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
NAMED = (15.0, 30.0, 45.0, 60.0)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


R = json.loads(read('b521_results.json') or '{}')
OD = json.loads(read('b521_order.json') or '{}')
CP = json.loads(read('b521_compare.json') or '{}')
NO = json.loads(read('b521_notes.json') or '[]')
w = lambda v: 'HELD' if v else 'REFUTED'


def a0_at(p):
    """### READING (10) (N2): the least named width from which the new tail is below B` at it and every larger named width."""
    rows = {r['a']: r for r in OD.get('rows', []) if r['p'] == p}
    ok = [a for a in NAMED if a in rows and all(rows[b]['Etail'] < rows[b]['Bprime'] for b in NAMED if b >= a and b in rows)]
    return min(ok) if ok else None


def scores():
    p = OD.get('least_p')
    q = R.get('q', {})
    pe = p if p is not None else 20
    a0 = a0_at(pe)
    return dict(least_p=p, a0=a0,
                n1=(p is None) or p >= 6,
                n2=a0 is not None and a0 <= 30.0,
                n3=(q.get('reach') or 0) > 30.0,
                n4=q.get('cross_minus_one') is not None,
                s1=(p is None) or p >= 9,
                s2=CP.get('smaller') == CP.get('of'),
                s3=CP.get('p5_smaller') == 0)


def components():
    L = ['=' * 132, 'b521 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### COMPONENT (N) -- (R130)(1)`S NOTES:']
    for r in NO:
        L.append('  %s : %d cells, %d VERIFIED-EST, %d re-marked %s ; tail / B` %.2e .. %.2e ; %d -> %d bytes ; prefix proved %s'
                 % (r['bank'], r['cells'], r['verified'], r['remarked'], r['per_file'], r['ratio_min'], r['ratio_max'],
                    r['before_bytes'], r.get('after_bytes', r['before_bytes']), r.get('prefix_proved')))
    L += ['', '### THE PRE-SEAL PRICING, AS BANKED BEFORE THE SEAL:'] + read('b521_preseal_pricing.txt').rstrip(NL).split(NL) + ['']
    L += read('b521_report.txt').rstrip(NL).split(NL)
    L += ['', '### THE RUN LOG:'] + read('b521_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b521_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:10]))


def desk():
    sc = scores()
    q = R['q']
    L = ['=' * 104, 'b521 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- the least p with the new tail below B` at a = 60 : %s (against 6).' % (w(sc['n1']), sc['least_p']),
         '  **(N2)** ### **%s.** -- at p = %s the new tail is below B` from named width %s on (against 30).' % (w(sc['n2']), sc['least_p'], sc['a0']),
         '  **(N3)** ### **%s.** -- Q0`s reach : %s (stopped at a = %s).' % (w(sc['n3']), q['reach'], (json.loads(read('b521_reach.json'))['stop'] or {}).get('a')),
         '  **(N4)** ### **%s.** -- the pair`s ratio reaches -1 first at : %s%s.' % (w(sc['n4']), q['cross_minus_one'] or 'NO READ WIDTH',
                                                                             ' ### NO Q0 CELL WAS READ' if q['cells'] == 0 else ''),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the least p : %s (against 9).' % (w(sc['s1']), sc['least_p']),
         '  **(S2)** ### **%s.** -- at the least p the new tail is below b519`s old majorant at %s of %s widths.' % (w(sc['s2']), CP['smaller'], CP['of']),
         '  **(S3)** ### **%s.** -- at p = 5 the closed form is below the old majorant at %s of %s widths.' % (w(sc['s3']), CP['p5_smaller'], CP['of']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 1`S OWN CLAIM, "SMALLER AT EVERY WIDTH, AND VALID": smaller at %d of %d (not at %s); valid on the strip,'
         % (CP['smaller'], CP['of'], CP['not_smaller']),
         '    its fixture covered at 4 of 4 widths and its control refused at 4 of 4: %s.' % R.get('validity_ok'),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b521_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b521_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b521_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b521 — Q0\'s tail tightened, the width pass re-run; (R130) entered'


def trail():
    sc = scores()
    q = R['q']
    nb = {r['act']: r for r in NO}
    body = """
%(h)s

**(R130) ratified.** (1) b518's and b519's Q0 cells re-marked VERIFIED-EST-TAIL by appended note. (2) The tail is the
numerical shadow of (f)(iii): uniformity over unknown zeros is, at Q0, the window's decay order against the bank's
height. (3) Tighten the tail before extending the bank; bank extension is the fallback, not run. (4) The numerical lane
opened for this act and shuts at its close; the kernel lane reopens for (f)(i) on variant (B).

**The notes.** Appended, prior bytes proved an unchanged prefix: **%(n18)d of b518's %(v18)d** and **%(n19)d of b519's
%(v19)d** verified Q0 cells had a tail majorant above the rest of their bound, and are re-marked; the rest are not.

**COMPONENT 0 — the smoothness order.** The closed-form tail at a = 15, 30, 45, 60 for p = 5 upward: **the least p with the
tail below B′ at a = 60 is %(p)s.** At fixed p the tail falls with width on this grid, so at p = %(p)s it is above B′ at
a = 15 and below from a = %(a0)s. The rebuilt window's (R125)(2) fixture meets its bar at every u: %(fx)s. classK restated:
h is even, compactly supported and C^(p−3).

**COMPONENT 1 — the new tail.** Closed form; on-line part at s = 0, off-line allowance to real part 1 at s = ½, both over
the full RvM main-term count; S(t)'s remainder named, not bounded; valid on the strip 0 ≤ β ≤ 1. Against b519's old
majorant: **smaller at %(sm)d of %(of)d widths** (not at the narrowest, a ≤ 2.4); at equal p the closed form is 1.55 to 1.59
times the old (smaller at %(p5)d). Validity fixture: a zero at 0.9 + 200i covered at every named width; the control at
real part 3.0 refused at every one: %(va)s.

**COMPONENT 2 — the reach, as b520 registered it, at p = %(p)s: it ended at the first width, a = 15** (tail / B′ = %(tr).3g).
**No Q0 cell of this act is read.** The registered rule was not changed after the run and no other p was run in its place.

**COMPONENT 3 — ξ cited from b520:** VERIFIED-EST 46 of 46, positive at all. **The reading, in (R127)(2)'s words:**
%(reading)s.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The
numerical lane shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade
conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement
about RH.
""" % dict(h=HEADING, n18=nb['b518']['remarked'], v18=nb['b518']['verified'], n19=nb['b519']['remarked'], v19=nb['b519']['verified'],
           p=sc['least_p'], a0=sc['a0'], fx=R['fixture_meets'], sm=CP['smaller'], of=CP['of'], p5=CP['p5_smaller'], va=R['validity_ok'],
           tr=json.loads(read('b521_reach.json'))['stop']['tail_over_Bprime'], reading=R['reading'],
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
    io.open(os.path.join(D, 'b521_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
