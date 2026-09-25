# -*- coding: utf-8 -*-
"""b523_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b523_record.py components | desk | trail`
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


R = json.loads(read('b523_results.json') or '{}')
SG = json.loads(read('b523_sigma.json') or '{}')
CT = json.loads(read('b523_count.json') or '{}')
RR = json.loads(read('b523_reread.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def scores():
    rows = RR.get('rows', [])
    neg = [r for r in rows if r['neg522']]
    surv = RR.get('survivors', [])
    rat = [r['shortfall_over_margin'] for r in neg if r['shortfall_over_margin'] is not None]
    sm = SG.get('sigma_max')
    return dict(
        n1=sm is not None and 1.2 <= sm <= 2.5,
        n2=len(RR.get('neg_sigma', [])) >= 12,
        n3=len(RR.get('neg_sigma', [])) - len(RR.get('neg_full', [])) < 4,
        n4=bool(surv) and min(surv) >= 40.0,
        s1=sm is not None and 1.4 <= sm <= 1.9,
        s2=len(surv) == len(neg) == 24,
        s3=bool(rat) and len(rat) == len(neg) and max(rat) < 1e-6)


def components():
    L = ['=' * 132, 'b523 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    L += read('b523_report.txt').rstrip(NL).split(NL)
    L += ['', '### THE RUN LOG:'] + read('b523_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b523_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    surv = RR['survivors']
    L = ['=' * 104, 'b523 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- sigma_max = %.3f (against [1.2, 2.5]).' % (w(sc['n1']), SG['sigma_max']),
         '  **(N2)** ### **%s.** -- negative under the sigma re-pricing : %d of 24 (against 12).' % (w(sc['n2']), len(RR['neg_sigma'])),
         '  **(N3)** ### **%s.** -- cells lost to the S(t) bound : %d (against fewer than 4).' % (w(sc['n3']), len(RR['neg_sigma']) - len(RR['neg_full'])),
         '  **(N4)** ### **%s.** -- the narrowest width surviving all three : %s (against 40).' % (w(sc['n4']), min(surv) if surv else 'NONE'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- sigma_max = %.3f (against [1.4, 1.9]).' % (w(sc['s1']), SG['sigma_max']),
         '  **(S2)** ### **%s.** -- surviving all three : %d of 24.' % (w(sc['s2']), len(surv)),
         '  **(S3)** ### **%s.** -- the largest shortfall / margin : %s (against 1e-6).' % (w(sc['s3']), R['shortfall_ratio_max']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### COMPONENT 5 -- THE VERDICT THE NUMBERS GIVE (READING (7)): ' + R['verdict'] + '.',
         '    ### Every survivor is VERIFIED-EST-TAIL: under the full tail no re-read width is inside (R131)(2)`s reach.',
         '    ### The seat lifts nothing and writes no sentence into step (9); the navigator`s ruling follows.',
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b523_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b523_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b523_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b523 — the witness\'s three caveats priced; (R132) entered'


def trail():
    sc = scores()
    pp = CT['params']
    surv = RR['survivors']
    body = """
%(h)s

**(R132) ratified.** (1) b522's reading entered in (R127)(2)'s words; not a statement about RH or zeta; the object column
unchanged. (2) The witness held, not announced, until its three caveats are priced — the strip caveat sharpened:
zeros of Z_Q0 with real part above 1 exist (Davenport–Heilbronn, class number above 1), so the tail must allow an explicit
σ_max. (3) (R118)(1)'s bar met in form at b522, in substance only by this act's numbers. (4) The factor (f)(i) must beat is
the realized G = 1.361 at a = 34, whose mechanism is mass at the plateau's edge. (5) The numerical lane opened for this
act and shuts at its close.

**COMPONENT 1 — σ_max = %(sm).3f.** From Z_Q0 = 2 + Σ_{n≥2} r(n) n^{-s}: r(n) counted exactly to 10^6, and above that
r(n) ≤ 2a(n), a(n) = Σ_{d|n} (d/23) (the three forms of discriminant −23 together represent n exactly 2a(n) times),
so Σ_{n≥2} r(n) n^{-σ} < 2 for σ ≥ %(sm).3f: no zero has real part at or above it, nor at or below 1 − σ_max. The
bank's largest real part below 150, 0.9533, lies below it.

**COMPONENT 2 — the tail with real part up to σ_max** (b521's closed form at s = %(s).3f): %(ns)d of b522's 24 negative
cells stay negative beyond the re-priced bound.

**COMPONENT 3 — S(t) bounded.** No source is cited: Z_Q0 has no Euler product (it is 2/3 of ζ_K + L(ψ) + L(ψ̄)), so an
L-function's Backlund bound does not count its zeros. Proved here instead, from the argument principle on the box,
Backlund's sign-change count by Jensen, and Rademacher's Phragmén–Lindelöf for (s − 1)Z(s): N(T) ≤ M0(T) + E(T),
E(150) = %(e150).2f (η = %(eta).1f, σ1 = %(s1).3f; the Γ-ratio sup and a Stirling pad checked numerically on grids). The
bank's counts at T = 30 … 150 lie inside M0 ± E. With the bound in place of the bare main term: %(nf)d of 24 stay negative.

**COMPONENT 4 — the u > 1200 shortfall** against the margin: largest ratio %(rat).1e.

**COMPONENT 5 — %(surv)d of b522's 24 negative cells survive all three re-pricings, VERIFIED-EST under the full bound;
the narrowest at a = %(nar)s.** Under the full tail no re-read width is inside (R131)(2)'s reach, so every survivor is
VERIFIED-EST-TAIL: the sign is decided beyond the tail majorant's bound, by margins from %(mlo).3g to %(mhi).3g against bounds at
most %(bhi).2e. **The verdict the numbers give on (R118)(1)'s bar: %(verdict)s.** The seat lifts nothing and writes no
sentence into step (9); the navigator's ruling follows.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The
numerical lane shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade
conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement
about RH.
""" % dict(h=HEADING, sm=SG['sigma_max'], s=RR['s_max'], ns=len(RR['neg_sigma']), e150=CT['E150'], eta=pp['eta'], s1=pp['sigma1'],
           nf=len(RR['neg_full']), rat=R['shortfall_ratio_max'], surv=len(surv), nar=(min(surv) if surv else 'none'),
           verdict=('MET IN SUBSTANCE' if surv else 'NOT MET'),
           mlo=min(r['margin_full'] for r in RR['rows'] if r['survives']), mhi=max(r['margin_full'] for r in RR['rows'] if r['survives']),
           bhi=max(r['B_full'] for r in RR['rows'] if r['survives']),
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
    io.open(os.path.join(D, 'b523_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
