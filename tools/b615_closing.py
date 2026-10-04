# -*- coding: utf-8 -*-
"""b615_closing.py -- THE CLOSING RECORD OF b615, UNDER (R225).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b615_closing.txt from the act's banks. It writes nothing else. The template is b612_closing.py.
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
         'SIDE-bsd-multiplicity']
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H49a', 'H49b', 'H49c', 'H49d'),
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
    '    (a) ### **THE NEXT ACT, (R225)(6)**: b616, the synthesis for 2G, the sequence`s last, priced on the trail record (census R17:',
    '        seven papers in phase2/physics-speculative and two simulators; QUATERNIONIC names TECHNE once); the author rules on the closing.',
    '    (b) ### **FOR THE AUTHOR**: the 2F papers` findings on the trail record -- ZERO_SIMPLICITY :18`s ξ without s(s − 1)/2, :26`s unit',
    '        circle and absolute convergence, :28`s digamma zeros, :93`s Dyson table, :64 against :106, :80`s attribution; BSD_TRANSFER :210`s',
    '        seven against four; BSD_VIA_FORMATION_TRANSFER :64 and :267`s placeholder name, :325-:370`s listing, :374`s toolchain, :127`s',
    '        three places; b614`s trail record`s doubled percent signs.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the load-bearing reading of each certifying row; 2D`s v0.2 by the ruling`s letter, its',
    '        Placement and Version history carried unedited; the transfer to the elliptic L-function read as a route at RH-60; the computed',
    '        range NOT A ROUTE at RH-58; PRIME_ORDER`s stretch from 137 to 337 entered beside the ruling`s; the suite committed as it stood',
    '        before its edit, so the edit`s diff stands in the record.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b615; relay push-b615 and push-b615-closing.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
    '    (f) Kept runs, each claim tested directly before a re-run alone: the run after the suite edit with two defective positive',
    '        controls (data/b615_checks_after_edit_attempt1.txt, defect (a)); the run after the repair that met a transient network',
    '        failure, each failed read retried once alone (data/b615_checks_after_edit_attempt2.txt). The closing reads each repository`s',
    '        remote refs once (the standing line of (R225)(4)).',
]
_REMOTE = {}


def remote_refs(p):
    """### (R225)(4): one ls-remote per repository for the closing, retried once alone when it fails"""
    if p not in _REMOTE:
        out = g(p, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(p, 'ls-remote', 'origin')
        _REMOTE[p] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[p]


def main():
    for tool, out in (('b307_handoff_census.py', 'b615_census_closing.txt'), ('b327_faces_census.py', 'b615_faces_census_closing.txt'),
                      ('b303_pins.py', 'b615_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b615'])
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
    S = json.load(io.open(os.path.join(D, 'b615_scores.json'), encoding='utf-8'))
    pre, post = rd('b615_checks.txt'), rd('b615_checks_postpush.txt')
    L = ['=' * 104,
         'b615 -- THE CLOSING RECORD. ### **LANE THREE, ACT FORTY-TWO: THE SYNTHESIS FOR CLUSTER 2F; THE KC TIER`S LOAD-BEARING CLAUSE '
         'AND THE RE-READ OF THE EARLIER TIER LINES; THE 2D FINDINGS AND TWO ERRATA; THE SUITE`S REMOTE READS ONE PER RUN, UNDER (R225).**', '=' * 104]
    L += ['    ' + l for l in rd('b615_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b615_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b615_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b615_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b615_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; the 2F and 2D papers, the four syntheses` '
          'current versions, the census and REGISTRY unedited ; the synthesis written in the cluster`s folder and 2D`s v0.2 beside its v0.1 ; '
          'ERRATA appended with two entries, committed alone ; the suite edit committed alone ; no mirror built', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b615_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
