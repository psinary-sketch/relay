# -*- coding: utf-8 -*-
"""b528_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b528_record.py components | desk | trail`
### Every figure READ from the banks; the scores are the report`s, recounted by the suite.
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


R = json.loads(read('b528_results.json') or '{}')
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def components():
    L = ['=' * 150, 'b528 -- THE COMPONENTS, AS THEY RAN.', '=' * 150, ''] + read('b528_report.txt').rstrip(NL).split(NL)
    L += ['', '### THE RUN LOG (it prints OUT widths` values: defect D2):'] + read('b528_run_log.txt').rstrip(NL).split(NL) + ['=' * 150]
    io.open(os.path.join(D, 'b528_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:6]))


def fx_line():
    F = R['fixture']
    return ('%d of %d z scored at each of %d width-object pairs, every scored z within its bar (worst diff/bar %.3f); z = gamma_0 NOT SCORABLE, '
            'route 2 being identically zero there' % (F[0]['scored'], F[0]['of'], len(F), max(f['worst'] for f in F)))


def desk():
    sc, Q, X = R['scores'], R['q'], R['xi']
    L = ['=' * 104, 'b528 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- xi on the kernel`s plateau: IN %d of %d, VERIFIED-EST %d, positive beyond its estimated bound %d, negative %s.'
         % (W(sc['n1']), len(X['within']), X['cells'], X['verified'], len(X['pos']), X['neg'] or 'none'),
         '  **(N2)** ### **%s.** -- Q0 on the kernel`s plateau: IN %d of %d (tail ESTIMATE / B` %.1e .. %.1e), negative beyond its estimated bound at %s.'
         % (W(sc['n2']), len(Q['within']), Q['cells'], Q['tail_over_Bprime_min'], Q['tail_over_Bprime_max'], Q['neg'] or 'NONE'),
         '  **(N3)** ### **%s.** -- the narrowest read Q0 width with ratio <= -1 : %s ; G there %s beside 1.361 (READING (8): REFUTED if none).'
         % (W(sc['n3']), Q['cross'] or 'NONE', Q['G_at_cross']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- Q0`s reach on the kernel`s function: %d IN.' % (W(sc['s1']), len(Q['within'])),
         '  **(S2)** ### **%s.** -- xi IN %d and VERIFIED-EST %d of 46.' % (W(sc['s2']), len(X['within']), X['verified']),
         '  **(S3)** ### **%s.** -- the fixture: %s. "At every z", as worded, is not met.' % (W(sc['s3']), fx_line()),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('n1', 'n2', 'n3')].count(None),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b528_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b528_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b528_scores.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(sc, indent=1) + NL)
    print(NL.join(L))


HEADING = '### b528 — both objects on the kernel\'s plateau; every tail an ESTIMATE; (R138) entered'


def trail():
    sc, Q, X, C = R['scores'], R['q'], R['xi'], R['check']
    body = [
        '', HEADING, '',
        '**(R138) ratified.** (1) b527 entered; a stop the seat causes is an attempt, a stop the host causes is not. (2) Both objects',
        'measured on the kernel\'s function, the transform numerical and fixtured by two quadratures, the tail above each bank an',
        'ESTIMATE; W-ORD-SMOOTH-TAIL filed by the author (a rigorous tail on this φ needs high-order derivative norms of',
        'smoothTransition). (3) The form re-derived from this act alone. (4) The numerical lane opened for this act.',
        '',
        '**COMPONENT 0.** φ at %d points against the kernel\'s definition (b527\'s mpmath bank): max %.1e. The transform: %s.'
        % (C['n'], C['max_chain'], fx_line()),
        '',
        '**COMPONENT 1 — Q0** at 16.290216 on the kernel\'s plateau, a = 15 … 60: **%d of %d widths IN**; the tail ESTIMATE over '
        'B′ runs %.1e … %.1e. Negative beyond its estimated bound at %s; the narrowest negative width %s; G at a crossing: %s.'
        % (len(Q['within']), Q['cells'], Q['tail_over_Bprime_min'], Q['tail_over_Bprime_max'], Q['neg'] or 'none',
           Q['narrowest_neg'] or 'NONE', Q['G_at_cross'] or 'none read'),
        'The pre-seal price declared this on the face: the exp(−1/x) ramp\'s transform near t = 150 is orders above the order-7',
        'B-spline\'s, so its tail swamps b522\'s B′. OUT widths are banked as their error terms and not read.',
        '',
        '**COMPONENT 2 — ξ** at 14.1347, the same widths: IN %d of %d, VERIFIED-EST %d, positive beyond its estimated bound at %d,'
        % (len(X['within']), X['cells'], X['verified'], len(X['pos'])),
        'negative at %s. G over the widths %.4f … %.4f (a property of φ alone).' % (X['neg'] or 'none', X['G_range'][0], X['G_range'][1]),
        '',
        '**COMPONENT 3 — the form of words:** ' + R['form'],
        '',
        '**(N1) %s · (N2) %s · (N3) %s**; the seat\'s own: (S1) %s, (S2) %s, (S3) %s. Defects: the fixture\'s z = γ₀ degenerate'
        % (W(sc['n1']), W(sc['n2']), W(sc['n3']), W(sc['s1']), W(sc['s2']), W(sc['s3'])),
        'for route 2 (NOT SCORABLE, no second bar minted); the run\'s progress line printed OUT widths\' values (declared).',
        '**The numerical lane shuts at this act\'s close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no',
        'grade conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a',
        'statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b528_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
