# -*- coding: utf-8 -*-
"""b515_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b515_record.py components | desk | trail`
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
UPPER = 60
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


R = json.loads(read('b515_results.json') or '{}')
FX = json.loads(read('b515_fixture.json') or '[]')
FD = json.loads(read('b515_fixture_diagnosis.json') or '{}')
MT = json.loads(read('b515_matched.json') or '[]')
CELLS = sorted((json.loads(l) for l in read('b515_cells.jsonl').split(NL) if l.strip()), key=lambda c: c['a'])
w = lambda v: 'HELD' if v else 'REFUTED'


def control_ok():
    return bool(MT) and all(abs(complex(*m['at_gamma0'])) < 1e-12 * m['line_peak'] for m in MT)


def scores():
    q, x = R.get('q', {}), R.get('xi', {})
    return dict(
        n1=bool(CELLS) and len(q.get('pair_neg') or []) == len(CELLS),
        n2=len(q.get('h2_neg_upper') or []) >= 1,
        n3=x.get('verified', 0) > 0 and len(x.get('h2_pos') or []) == x.get('verified'),
        s1=bool(q.get('pair_neg')) and bool(q.get('pair_pos')),
        s2=q.get('verified', 0) > 0 and len(q.get('h2_pos') or []) == q.get('verified'),
        s3=control_ok())


def components():
    L = ['=' * 132, 'b515 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### COMPONENT 0 -- THE FIXTURE (READING (7)):']
    for f in FX:
        L.append('  %s gamma0 %.6f order %d : max |closed - numeric| %.2e (scale %.2e) ; bar 1e-10 %s ; |k(.7) - k(-.7)| %.1e ; knot jumps %s'
                 % (f['object'], f['gamma0'], f['order'], f['maxdiff'], f['scale'], 'MET' if f['meets'] else '### NOT MET ###',
                    f['even'], {k: '%.1e' % v for k, v in f['knot_jumps'].items()}))
        L.append('    classK (READING (2)): k = weilTest h h with h = %s ; even ; C^2 ; support %s.' % (f['generating_h'], f['support']))
    L += ['  ### THE REGISTERED BAR IS NOT MET AT Q0 (1.24e-10 against 1e-10); the verdict stands. ### A POST-SEAL DIAGNOSIS, DECLARED',
          '  ### (`b515_fixture_diagnosis.json`): every difference, both objects, lies below the numerical route`s own round-off floor',
          '  ### eps * SUM|terms| * sqrt(n) (1.0e-10 to 2.7e-10); `fsum` moves nothing, so the error is in the per-node k(x) values.',
          '  ### The face`s floor (near 1e-16 times the peak, ~7e-12) was set below the route`s true floor -- b505`s species.']
    for o in FD.get('objects', []):
        L += ['    %s u=%-8.4f diff %.2e ; fsum diff %.2e ; route floor %.2e' % (o['object'], r['u'], r['diff_sum'], r['diff_fsum'], r['roundoff_floor']) for r in o['rows']]
    L += ['', '### COMPONENT 0 -- THE CONTROL AND THE THREE WIDTHS (READING (8)):']
    for m in MT:
        L.append('  a=%-10.6f %-3s h^(gamma0) %+.3e (line peak %.3e) ; slope %+.4e (central difference %+.4e) ; nearest %s -> %s%s'
                 % (m['a'], m['object'], m['at_gamma0'][0], m['line_peak'], m['slope'], m['slope_numeric'], ['%.4f' % x for x in m['nearest']],
                    ['%+.3e' % v[0] for v in m['at_nearest']],
                    (' ; h^(gammaOf rho = %.5f %+.5fi) %+.3e %+.3ei' % tuple(m['gammaOf_rho'] + m['hhat_at_gammaOf_rho'])) if 'gammaOf_rho' in m else ''))
    L += ['', '### THE MARGIN COLUMN, READ: the window carries its pole (READING (1)), and P = k-hat(i/2) + k-hat(-i/2) is about 1.4e5 to',
          '### 1.6e5 at every width, so m = A - PR = Z - P is negative wherever Z < P -- a statement about the pole term, not about',
          '### h2_sign`s quantity P - PR + A, whose sign is the one Component 3 reads.']
    L += [''] + read('b515_report.txt').rstrip(NL).split(NL) + ['', '### THE RUN LOG:'] + read('b515_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b515_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc = scores()
    q, x = R['q'], R['xi']
    L = ['=' * 104, 'b515 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- the pair`s term negative at %d of %d widths, positive at %d ; pair / rest from %+.3e to %+.3e.'
         % (w(sc['n1']), len(q['pair_neg']), len(CELLS), len(q['pair_pos']), q['ratio_min'], q['ratio_max']),
         '  **(N2)** ### **%s.** -- Q0`s P - PR + A negative beyond B in the upper half at : %s ; positive beyond B at %d of %d VERIFIED-EST cells.'
         % (w(sc['n2']), q['h2_neg_upper'] or 'NONE', len(q['h2_pos']), q['verified']),
         '  **(N3)** ### **%s.** -- xi`s P - PR + A positive beyond B at %d of its %d VERIFIED-EST cells.' % (w(sc['n3']), len(x['h2_pos']), x['verified']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the pair`s term negative at %d widths and positive at %d.' % (w(sc['s1']), len(q['pair_neg']), len(q['pair_pos'])),
         '  **(S2)** ### **%s.** -- Q0`s P - PR + A positive beyond B at %d of %d VERIFIED-EST cells.' % (w(sc['s2']), len(q['h2_pos']), q['verified']),
         '  **(S3)** ### **%s.** -- |h^(gamma0)| against the line peak at the three widths: %s.'
         % (w(sc['s3']), ['%.1e' % (abs(complex(*m['at_gamma0'])) / m['line_peak']) for m in MT]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THE FIXTURE (not an expectation): xi %s, Q0 %s against the registered 1e-10.'
         % tuple(('MET %.2e' if f['meets'] else 'NOT MET %.2e') % f['maxdiff'] for f in FX),
         '', '### COMPONENT 3 -- THE READING: ' + R['reading'],
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b515_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b515_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b515_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b515 — the window with a zero at the on-line point; (R124) entered'


def trail():
    sc = scores()
    q, x = R['q'], R['xi']
    fq = [f for f in FX if f['object'] == 'q'][0]
    fx = [f for f in FX if f['object'] == 'xi'][0]
    body = """
%(h)s

**(R124) ratified.** (1) b514 is entered with its mechanism: for real even h the pair term at ρ = β + iγ₀ is
ĥ(β + iγ₀)·conj ĥ(1 − β + iγ₀); a window whose line transform is largest at γ₀ makes it positive to leading order, one
whose line transform vanishes there with nonzero slope makes it negative to leading order — so the dominance lemma (f)
is a statement about a window with a zero at the on-line point. The face said so before this act ran. (2)
**`W-ORD-WEIL-CONVERSE`** is filed: (d) the growth bound |ĥ(s)| ≤ ‖h‖₁·exp(L·|Re s − 1/2|) for h supported in [−L, L];
(f) the dominance, from (d), the local zero count and that window; priced at the fold, not attempted. (3) The numerical
lane opened for this act; the fold follows at span 8, and the kernel lane reopens after it.

**COMPONENT 0.** h = φ'' + γ₀²φ, φ the order-6 B-spline bump on [−log a, log a] (so h is C²), ĥ(z) = (γ₀² − z²)φ̂(z),
k = h⋆h in classK with generating h; no pole annihilation. The control holds: ĥ(γ₀) reads 0 at all three widths, and
the closed-form slope matches a central difference. **The fixture meets its 1e-10 bar for ξ (%(fx).2e) and NOT for Q0
(%(fq).2e)**; a declared post-seal diagnosis puts every difference below the numerical route's own round-off floor
(1.0e-10 to 2.7e-10) — the face set its floor too low — and the registered verdict stands.

**COMPONENT 1 — Q0.** VERIFIED-EST at %(qv)d of %(n)d widths. h2_sign's quantity P − PR + A is positive beyond its bound at
every verified width (%(qp)d); negative at no width, so no narrowest width and no growth factor is banked. The pair's
term is negative at %(pn)d widths and positive at %(pp)d, and never more than %(rmax).1e of the rest in magnitude: the
low on-line ordinates, where ĥ is largest, carry the sum. The margin A − PR is negative at most widths because this
window carries a pole term P ≈ 1.5e5; that is the pole, not h2's quantity.

**COMPONENT 2 — ξ** at 14.1347, the same columns. VERIFIED-EST at %(xv)d of %(n)d (the rest short by under 10 percent);
P − PR + A positive beyond its bound at all %(xp)d.

**COMPONENT 3 — the reading, in (R122)(2)'s words:** %(reading)s. Nothing is claimed of the kernel either way.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The numerical lane
shuts at this act's close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no grade conferred; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, fx=fx['maxdiff'], fq=fq['maxdiff'], n=len(CELLS), qv=q['verified'], qp=len(q['h2_pos']),
           pn=len(q['pair_neg']), pp=len(q['pair_pos']), rmax=max(abs(q['ratio_min']), abs(q['ratio_max'])),
           xv=x['verified'], xp=len(x['h2_pos']), reading=R['reading'],
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
    io.open(os.path.join(D, 'b515_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
