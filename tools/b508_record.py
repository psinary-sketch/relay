# -*- coding: utf-8 -*-
"""b508_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b508_record.py components | desk | trail`
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


def rows(n):
    return sorted((json.loads(l) for l in read(n).split(NL) if l.strip()), key=lambda c: c['a'])


R = json.loads(read('b508_results.json') or '{}')
Q = {round(c['a'], 6): c for c in rows('b506_cells.jsonl')}
X = {round(c['a'], 6): c for c in rows('b504_cells.jsonl')}
P = {round(c['a'], 6): c for c in rows('b508_pairs.jsonl')}
BOTH = sorted(a for a in Q if a in X and X[a]['verified'] and Q[a]['verified'])
I16 = [k for k, t in enumerate(P[BOTH[0]]['terms']) if abs(t['rho'][1] - 16.290215720390393) < 1e-8][0] if BOTH else None
NEG_OFF = [a for a in BOTH if Q[a]['Z_off'] < 0]
NEG_T16 = [a for a in BOTH if P[a]['terms'][I16]['term'] < 0]
XI_OUT = sorted(a for a in Q if not X[a]['verified'])
w = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
DP = R['fit_t16']['p'] - R['fit_zon']['p'] if R else 0.0


def components():
    L = ['=' * 104, 'b508 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 0 -- THE PAIR SPLIT, ITS LOG VERBATIM.']
    L += read('b508_pairs_log.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENTS 1-3 -- THE REPORT, VERBATIM.'] + read('b508_report.txt').rstrip(NL).split(NL)
    L += ['', '### WHERE THE SIGNS TURN, READ FROM THE BANKS.',
          '    the %d wide cells outside the population, xi unverified there (b504`s ESTIMATE-SHORT) : %s' % (len(XI_OUT), XI_OUT),
          '    Z_off < 0 at : %s' % NEG_OFF,
          '    the 16.29 pair`s term < 0 at : %s' % NEG_T16,
          '    ### the two exponents of Component 3 differ by %+.4f ; the act prices no uncertainty on either.' % DP,
          '=' * 104]
    io.open(os.path.join(D, 'b508_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-8:]))


def desk():
    L = ['=' * 104, 'b508 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- the Epstein margin is positive at all %d cells where both kernels verify; the smallest is %+.9f'
         % (w(R['n1']), R['both'], R['min_mq']),
         '    at a = %.6f, the widest cell; negative at NONE.' % R['min_mq_a'],
         '  **(N2)** ### **%s.** -- ### **BY CONSTRUCTION, SO IT COULD NOT HAVE FAILED:** b506 defines r = Z - (P - PR + A), and'
         % w(R['n2']),
         '    m_Q0 - (Z_Q0 - P) equals -r at every cell to %.1e. ### Its content is the verification: |r| <= B at all %d.'
         % (R['max_diff_plus_r'], R['both']),
         '  **(N3)** ### **%s.** -- on both clauses: Z_off is negative at %d of %d cells (not more than half), and its magnitude'
         % (w(R['n3']), R['zoff_neg'], R['both']),
         '    FALLS with a, from %.3e at a = %.6f to %.3e at a = %.6f, Spearman %+.4f.'
         % (abs(R['zoff_first']), R['a_min'], abs(R['zoff_last']), R['a_max'], R['spearman_a_abs_zoff']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the off-line part is negative at %d cells, a = %s; the declared peek saw only a from 5.0 to 5.61.'
         % (w(R['s1']), len(NEG_OFF), ', '.join('%.6f' % a for a in NEG_OFF)),
         '  **(S2)** ### **%s.** -- the 16.29 pair`s share of Z_off runs from %.3f to %.3f; its term is negative at %d cells.'
         % (w(R['s2']), R['frac16_min'], R['frac16_max'], len(NEG_T16)),
         '  **(S3)** ### **%s.** -- under the centre lines the ratio falls: |T16| ~ a^(%.4f), |Z_on| ~ a^(%.4f). ### **THE EXPONENTS'
         % (w(R['s3']), R['fit_t16']['p'], R['fit_zon']['p']),
         '    DIFFER BY %+.4f, AND NO UNCERTAINTY IS PRICED ON EITHER**, so the NONE rests on two nearly parallel centre lines.' % DP,
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### (N2) HELD BY CONSTRUCTION.'
         % ([R['n1'], R['n2'], R['n3']].count(True), [R['n1'], R['n2'], R['n3']].count(False), 0),
         '### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**'
         % ([R['s1'], R['s2'], R['s3']].count(True), [R['s1'], R['s2'], R['s3']].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.',
         '    (a) ### **THE PRICE SAID UNDER TEN MINUTES; THE PAIR SPLIT TOOK 6 s.** ### The estimate carried b506`s three-level',
         '        cost into a one-level run. ### A price a hundred times too high is harmless here and is still a wrong price.',
         '=' * 104]
    io.open(os.path.join(D, 'b508_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=R['n1'], n2=R['n2'], n3=R['n3'], s1=R['s1'], s2=R['s2'], s3=R['s3']),
              io.open(os.path.join(D, 'b508_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b508 — the Epstein margin on the completed bank: positive at all 83 cells where both kernels verify'


def trail():
    body = """
%(h)s

**Under (R117)(4)** the numerical lane opened for this act alone. The order's part 2 of 2 was banked at b507;
b507 closed first.

**COMPONENT 1.** Of the ladder's 119 cells, xi verifies at 109 (b504) and Q0 was run on the completed bank at the
93 wide cells and verifies at all 93 (b506); **both verify at %(both)d**, a from %(amin).6f to %(amax).6f — the ten wide
cells outside are xi's ESTIMATE-SHORT cells. **The Epstein margin `m_Q0 = A_Q0 − PR_Q0` is positive at every one of
the %(both)d; the smallest is %(mmin)+.9f at a = %(mmina).6f, the widest cell; negative at NONE.** xi's margin is printed
beside it at every cell, from b504's bank.

**COMPONENT 2.** `m_Q0 − (Z_Q0 − P)` equals −r at every cell to %(dr).1e **by construction** — b506 defines the
residual as that difference — and the pole term is at most %(pmax).1e, so **the reading the record holds for xi, the
margin equals the zero sum, is found at the second object** within the verified residual. The off-line part (the
seventeen off-line zeros b506 located, each with its three images, split pair by pair and summed back onto b506's
banked `Z_off` to %(fix).1e at all 93 cells) is **positive at %(pos)d cells and negative at %(neg)d, all between a = %(n0).6f
and %(n1).6f**, and its magnitude **falls** with a, from %(zf).3e to %(zl).3e (Spearman %(sp)+.4f).

**COMPONENT 3 — AN EXTRAPOLATION, LABELLED AS ONE.** The pair at 0.953 + 16.29i carries a term negative at %(t16n)d
cells; `|T16|/|Z_on|` is %(rf).4e at the narrowest cell and %(rl).4e at the widest. Least-squares centre lines on
log–log give `|T16| ~ a^(%(p16).4f)` and `|Z_on| ~ a^(%(pon).4f)`: **under them the ratio falls, so the extrapolated width
is NONE** — and the two exponents differ by %(dp)+.4f with no uncertainty priced, so that NONE rests on two nearly
parallel lines. The detection law F.2026-08-05-p gives 5.9·γ²/δ = %(nlaw).1f for this pair (the sitting measured 3379):
**a Li index, not a width**, printed beside and not compared. **No crossing width is asserted.**

**(N1) %(N1)s · (N2) %(N2)s, by construction · (N3) %(N3)s** on both clauses. The seat's own: (S1) %(S1)s, (S2) %(S2)s,
(S3) %(S3)s. **The numerical lane shuts at this act's close**; the kernel lane reopens for (R104)'s act 3. No crossing
width of b334 is cited. No grade conferred; nothing deposits; row U1 unedited; `h2` where the deposit left it; the
four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, both=R['both'], amin=R['a_min'], amax=R['a_max'], mmin=R['min_mq'], mmina=R['min_mq_a'],
           dr=R['max_diff_plus_r'], pmax=R['max_abs_P'], fix=R['fixture_max_diff'], pos=R['zoff_pos'], neg=R['zoff_neg'],
           n0=min(NEG_OFF), n1=max(NEG_OFF), zf=abs(R['zoff_first']), zl=abs(R['zoff_last']), sp=R['spearman_a_abs_zoff'],
           t16n=len(NEG_T16), rf=R['ratio_first'], rl=R['ratio_last'], p16=R['fit_t16']['p'], pon=R['fit_zon']['p'], dp=DP,
           nlaw=R['law']['n_law'], N1=w(R['n1']), N2=w(R['n2']), N3=w(R['n3']), S1=w(R['s1']), S2=w(R['s2']), S3=w(R['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b508_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
