# -*- coding: utf-8 -*-
"""b616_closing.py -- THE CLOSING RECORD OF b616, UNDER (R226).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b616_closing.txt from the act's banks. It writes nothing else. The template is b612_closing.py.
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
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium', 'SIDE-residual-bridge',
         'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants', 'SIDE-simplicity', 'SIDE-bsd-formation-transfer',
         'SIDE-bsd-multiplicity', 'SIDE-t7-topology-cmb', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector']
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H50a', 'H50b', 'H50c', 'H50d'),
              ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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
    '    (a) ### **THE NEXT ACT, (R226)(5)**: b617, the sieve`s v0.5, the consolidation`s first act, taking the conclusions of',
    '        data/b616_routes_for_sieve.txt as rows read through the five tests; the author rules on the closing.',
    '    (b) ### **FOR THE AUTHOR**: the 2G papers` findings on the trail record -- SYMMETRY_FILTER`s bins table against its 439 and five,',
    '        :96 against :112, :141 against :127; the −0.66 called a Spearman ρ; LOCAL_COSMIC :12 and :90 against its table, :98`s 0.96;',
    '        T7_CMB :106 and :199`s eigenvalues, :12`s circles and pairs; the diagonal`s stabilizer; FORMATION_DISTANCE :77; THEORY_SPACE :65,',
    '        :20 and :218; the simulators` anticommutation, Toffoli and transversal T, no bank holding a run.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the kernel legs read as pins with no terminal; the T-seven run read on its bank; the',
    '        simulators graded by their text; the routes for the sieve read as the rows whose sieve column names no row, deduplicated by',
    '        the step each argues; the consolidation addressed to the sequence`s form; the correction line appended at the ledger`s end.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b616; relay push-b616 and push-b616-closing.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (f) Kept run: a suite run before the PLACE-papers commit read that remote twice, its first read failing and retried once alone',
    '        (data/b616_checks_attempt1.txt, 89 of 90, G-LSREMOTE-ONE-PER-REPO); the remote answered three direct reads and the pre-push',
    '        suite ran alone after the push. The closing reads each repository`s remote refs once (the standing line at OPEN_TRAILS :12703).',
]
_REMOTE = {}


def remote_refs(p):
    """### (R226)(4): one ls-remote per repository for the closing, retried once alone when it fails"""
    if p not in _REMOTE:
        out = g(p, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(p, 'ls-remote', 'origin')
        _REMOTE[p] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[p]


def main():
    for tool, out in (('b307_handoff_census.py', 'b616_census_closing.txt'), ('b327_faces_census.py', 'b616_faces_census_closing.txt'),
                      ('b303_pins.py', 'b616_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b616'])
        b = o.replace(chr(13), '').encode('utf-8')
        p = os.path.join(D, out)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
    heads = []
    for r in REPOS:
        p = 'D:/' + r
        loc = g(p, 'rev-parse', 'main')
        rem = remote_refs(p).get('refs/heads/main', '')
        heads.append('      %-32s main %s ; remote %s ; %s' % (r.split('/')[-1], loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    K = 'D:/SIDE-explicit-formula'
    for b in KEPT:
        loc = g(K, 'rev-parse', 'refs/heads/' + b)
        rem = remote_refs(K).get('refs/heads/' + b, '')
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = json.load(io.open(os.path.join(D, 'b616_scores.json'), encoding='utf-8'))
    pre, post = rd('b616_checks.txt'), rd('b616_checks_postpush.txt')
    L = ['=' * 104,
         'b616 -- THE CLOSING RECORD. ### **LANE THREE, ACT FORTY-THREE: THE SYNTHESIS FOR CLUSTER 2G, THE SEQUENCE`S LAST; THE SEQUENCE '
         'CLOSED AND THE CONSOLIDATION ENTERED, UNDER (R226).**', '=' * 104]
    L += ['    ' + l for l in rd('b616_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b616_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b616_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b616_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b616_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; the 2G papers and simulators, the five '
          'syntheses` current versions, the census, REGISTRY and ERRATA unedited ; the synthesis written in the cluster`s folder ; the routes '
          'for the sieve banked in relay ; no mirror built', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b616_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
