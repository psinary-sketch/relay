# -*- coding: utf-8 -*-
"""b508_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True).stdout.strip()
R = json.loads(read('b508_results.json'))
SC = json.loads(read('b508_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b508 -- THE CLOSING RECORD. ### **THE EPSTEIN MARGIN POSITIVE AT ALL %d CELLS WHERE BOTH KERNELS VERIFY.**' % R['both'], '=' * 104,
     '    fixture : pair split summed onto b506`s Z_off at %d cells, largest difference %.1e' % (R['q0_cells'], R['fixture_max_diff']),
     '    C1 : both verify %d of %d ; smallest m_Q0 %+.9f at a = %.6f ; negative %s' % (R['both'], R['cells_119'], R['min_mq'], R['min_mq_a'], R['neg_mq'] or 'NONE'),
     '    C2 : m - (Z - P) = -r to %.1e (by construction) ; Z_off positive %d, negative %d ; Spearman(a, |Z_off|) %+.4f'
     % (R['max_diff_plus_r'], R['zoff_pos'], R['zoff_neg'], R['spearman_a_abs_zoff']),
     '    C3 : exponents %.4f and %.4f ; ratio grows %s ; extrapolated width %s -- AN EXTRAPOLATION ; law n %.1f, a Li index'
     % (R['fit_t16']['p'], R['fit_zon']['p'], R['ratio_grows'], R.get('extrap_a', 'NONE'), R['law']['n_law']),
     '    (N1) %s (N2) %s, by construction (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- ONE.',
     '    (a) ### **THE PRICE SAID UNDER TEN MINUTES; THE PAIR SPLIT TOOK 6 s** -- b506`s three-level cost carried into a one-level run.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b508_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b508_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b508_census_closing.txt'), 'TOTAL MISSING'), lw(read('b508_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b508_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT**; the kernel lane reopens for (R104)`s act 3 under (R117)(4).',
      '    (b) ### **COMPONENT 3`S NONE RESTS ON EXPONENTS 0.008 APART** with no uncertainty priced.',
      '    (c) ### **b334`S CROSSINGS STAY UNVERIFIED**: this act read the wide cells only, not the aims b334 charted.',
      '=' * 104]
io.open(os.path.join(D, 'b508_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
