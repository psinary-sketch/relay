# -*- coding: utf-8 -*-
"""b590_closing.py -- THE CLOSING RECORD OF b590, UNDER (R200).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b590_closing.txt from the act's banks. It writes nothing else.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPOS = ['relay', 'MY-DOwnloads/PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo',
         'SIDE-grh-transfer', 'SIDE-rcurve']
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590']


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def g(repo, *a):
    return run(['git', '-C', repo] + list(a))[1].strip()


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def verdict(text, pat):
    m = re.search(pat, text)
    return m.group(0) if m else '### NOT FOUND'


def main():
    for tool, out in (('b307_handoff_census.py', 'b590_census_closing.txt'), ('b327_faces_census.py', 'b590_faces_census_closing.txt'),
                      ('b303_pins.py', 'b590_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b590'])
        io.open(os.path.join(D, out), 'w', encoding='utf-8', newline=NL).write(o.replace(chr(13), ''))
    heads = []
    for r in REPOS:
        p = 'D:/' + r
        loc = g(p, 'rev-parse', 'main')
        rem = g(p, 'ls-remote', 'origin', 'refs/heads/main').split('\t')[0]
        heads.append('      %-32s main %s ; remote %s ; %s' % (r.split('/')[-1], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    K = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K, 'rev-parse', 'refs/heads/' + b)
        rem = g(K, 'ls-remote', 'origin', 'refs/heads/' + b).split('\t')[0]
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    pe, pr = g(K, 'rev-parse', 'v0.16^{}'), g(K, 'ls-remote', 'origin', 'refs/tags/v0.16^{}').split('\t')[0]
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (made by the push script at b590)' % ('v0.16', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b590_scores.json'), encoding='utf-8'))
    pre, post = rd('b590_checks.txt'), rd('b590_checks_postpush.txt')
    L = ['=' * 104,
         'b590 -- THE CLOSING RECORD. ### **LANE TWO, ACT FOURTEEN: THE EPSTEIN NEGATIVE CONTROL -- THE DETECTOR THEOREM, THE '
         'EPSTEIN INSTANCE AT INTERFACES, THE WITNESS AGAINST THE BENCH; THE SWEEP`S COLUMN; THE DAY-1 SECTION, UNDER (R200).**', '=' * 104]
    L += ['    ' + l for l in rd('b590_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('%s %s' % (k, S[k][0]) for k in ('H31a', 'H31b', 'H31c')) + ' ; ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b590_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b590_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b590_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b590_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the kernel built one module per call on epstein-b590, main fast-forwarded, v0.16 by the push script ; no worktree made or removed ; D:/b566-forward KEPT', '']
    W = json.load(io.open(os.path.join(D, 'b590_witness_vs_bench.json'), encoding='utf-8'))
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R200)(6)**: b591, the located-clause method document -- a new document, explicitly asked, written',
          '        from the ledgers as the method as it was done on the zeta-leg, placed beside the b257 drafts, its title naming the',
          '        object; then the editions resume at RESIDUE.',
          '    (b) ### **STANDING, THE AUTHOR`S LINE (before b590`s seal)**: claim-family text travels in a separate local-only paste from',
          '        now on; the navigator`s placement of it in b590`s published ferry is recorded as the navigator`s (OPEN_TRAILS record).',
          '    (c) ### **FOR THE AUTHOR**: H31a refuted in its letter at the power -- the detector names its base and not its power, the',
          '        power drawn from a limit with no rate (b559`s H9a, again). The witness bench: D = %d, the half-width at least %s,' % (
              W['D'], W['half_pre'][:10]),
          '        %s times ln 33.19; the dominant orbit at the base width is the 16.29 orbit, rhoE`s at %s of it. The shared E0 rule' % (
              ('%.4g' % float(W['ratio'])), W['rhoE_score'][:6]),
          '        reads the salt-check`s membership_load_bearing INTERFACES on the binder inside its existential -- a reading of the',
          '        rule`s text, no grade moved. rowgen`s prefix rule flagged `detector` (baseWidth := 1 / ...), the README`s definition',
          '        applied in this act`s tool (defect (e)).',
          '    (d) The terminal table gained the act`s declarations (29 rows added, 0 grade cells moved); it was committed as housekeeping',
          '        before this closing (relay data/b590_housekeeping_push_out.txt). This act`s closing push-out bank gains the as-of lines',
          '        after its push; b591 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b590_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
