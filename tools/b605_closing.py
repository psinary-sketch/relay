# -*- coding: utf-8 -*-
"""b605_closing.py -- THE CLOSING RECORD OF b605, UNDER (R215).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b605_closing.txt from the act's banks. It writes nothing else. The template is b604_closing.py.
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
SCORE_KEYS = (('H28a', 'H28b', 'H28c', 'H39a', 'H39b', 'H39c', 'H39d'), ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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
    '    (a) ### **THE NEXT ACT, (R215)(5)**: b606, CP-8 -- the monograph`s v6, the sieve table at v0.3 its spine and the eleven',
    '        ceiling uses of data/b584_ceiling_census.txt its work-list, by the form, in as many acts as its length prices.',
    '    (b) ### **FOR THE AUTHOR**: H39a refuted in its first clause by the Dedekind reading (RH-30), a route darkened at test 3 --',
    '        neither a statistic nor refuted at the Epstein configuration; its second clause holds (no DARK row is an identity,',
    '        census, method theorem or face), as (N1) does.',
    '    (c) ### **FOR THE AUTHOR**: H39c refuted -- one FINITE rung (liCoeff_one_pos) reads BRIGHT by test 4; "the forall_upto',
    '        window" names no row, the pair being faces and no declaration fixing one rung at a finite support length.',
    '    (d) ### **FOR THE AUTHOR`S STRIKE**: the χ and family forms in the located clause`s FACE group by the ruling`s letter and',
    '        h2_sign_cfg_iff_target beside them by its reason; the clause`s verdict named as decided by test 2; the Keiper face read',
    '        as keiperTaylorIdentity_of and λ₁`s closed form as the identity its rung reads; the density rows read as statistics; the',
    '        Dedekind reading kept a route -- each printed with its reason in data/b605_verdicts.txt.',
    '    (e) Fact corrections to the ferry`s letter, the navigator`s: the ζ page at its own pin v0.20; liCoeff_one_pos in',
    '        KeiperSign.lean, not Keiper.lean.',
    '    (f) Branches left for the next act`s step zero, each merged: PLACE-papers push-b605; relay push-b605 and push-b605-closing.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b605_census_closing.txt'), ('b327_faces_census.py', 'b605_faces_census_closing.txt'),
                      ('b303_pins.py', 'b605_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b605'])
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
    S = json.load(io.open(os.path.join(D, 'b605_scores.json'), encoding='utf-8'))
    pre, post = rd('b605_checks.txt'), rd('b605_checks_postpush.txt')
    L = ['=' * 104,
         'b605 -- THE CLOSING RECORD. ### **LANE THREE, ACT THIRTY-TWO: THE SIEVE TABLE AT v0.3 -- NOT A ROUTE AS A THIRD VERDICT, '
         'THE FACES OF ONE CLAUSE UNDER ONE VERDICT, UNDER (R215).**', '=' * 104]
    L += ['    ' + l for l in rd('b605_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b605_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b605_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b605_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b605_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; v0.2 and the current version unedited, '
          'v0.3 written beside them', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b605_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
