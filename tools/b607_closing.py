# -*- coding: utf-8 -*-
"""b607_closing.py -- THE CLOSING RECORD OF b607, UNDER (R217).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b607_closing.txt from the act's banks. It writes nothing else. The template is b605_closing.py.
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
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H28a', 'H28b', 'H28c', 'H41a', 'H41b', 'H41c', 'H41d'), ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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


CARRIED = [
    '    (a) ### **THE NEXT ACT, (R217)(5)**: b608, CP-8 act three -- the remaining chapters by the b558 work-list where one exists and',
    '        by the ceiling and stem clauses otherwise, §25.8 re-pinned, the whole-document figure as its bound; priced on the trail record.',
    '    (b) ### **FOR THE AUTHOR**: H41b, H41c, H41d and N2, N3, N4 refuted by their letter -- the table has rows the sieve does not row,',
    '        §27.3 took more corrections than the bound, and the scope held fewer of the 171 than the bound; each printed in the banks.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: readings R-1 to R-11 and collisions C1-C6 in the edition`s back matter; ERRATA`s three',
    '        lines appended at the ledger`s end, each addressed to its entry.',
    '    (d) A fact correction to the ruling`s letter, the navigator`s: §27.3`s registers stand as E-2026-09-25-6`s replacements left them.',
    '    (e) Branches left for the next act`s step zero, each merged: PLACE-papers push-b607; relay push-b607 and push-b607-closing.',
    '    (f) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b607_census_closing.txt'), ('b327_faces_census.py', 'b607_faces_census_closing.txt'),
                      ('b303_pins.py', 'b607_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b607'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(D, out)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
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
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = json.load(io.open(os.path.join(D, 'b607_scores.json'), encoding='utf-8'))
    pre, post = rd('b607_checks.txt'), rd('b607_checks_postpush.txt')
    L = ['=' * 104,
         'b607 -- THE CLOSING RECORD. ### **LANE THREE, ACT THIRTY-FOUR: CP-8 ACT TWO -- CHAPTERS 21 AND 22, §24.4 AND §27.3 OF THE '
         'MONOGRAPH READ AGAINST THE COMPILED FACES, THE DOUBLING COROLLARY AND THE SIEVE, UNDER (R217).**', '=' * 104]
    L += ['    ' + l for l in rd('b607_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b607_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b607_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b607_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b607_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; v5.14 and v5.13 unedited, '
          'v5.15 written beside v5.14', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b607_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
