# -*- coding: utf-8 -*-
"""b602_closing.py -- THE CLOSING RECORD OF b602, UNDER (R212).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, both kernel tags (the point tag v0.19.1 and v0.20) peeled at the remote, TECHNE-Core's
### local main against its remote-tracking main (private: not pushed), and writes data/b602_closing.txt from the act's banks. It
### writes nothing else. The template is b601_closing.py.
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
        'sign-window-b602']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
TAGS = ('v0.19.1', 'v0.20')
SCORE_KEYS = (('H36a', 'H36b', 'H36c', 'H36d', 'H36e'), ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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
    '    (a) ### **THE NEXT ACT, (R212)(6)**: b603, the family form over χ mod q, the research sequence`s fifth item; then the edition of',
    '        THE_FINDINGS_AS_THEY_STAND as a sieve table by cluster, on the author`s word (OPEN_TRAILS :12394).',
    '    (b) ### **FOR THE AUTHOR**: defect (b) -- an API stop of the harness, not of the act, after the scores (02:54:52Z) and before the',
    '        record`s first write; resumed 03:14:45Z with both ledgers read first: the Component 1 lines whole, the record not yet landed,',
    '        nothing cut back.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the index 15 over 10; the prior art SIDE-lv-conservation n_one_binding_instance cited, not',
    '        consumed -- its stale docstring and BALANCE_AND_POSITIVITY :400`s "OPEN" left for their next editions; the window under Schema/',
    '        and on the χ page, its pin moved from v0.17 to v0.20; no re-emission at the point tag; the E0 rule`s lexical reading of a width',
    '        parameter named h on three non-node declarations.',
    '    (d) THE WINDOW`S OBLIGATIONS, each a priced item for a later act, none started: ConvStep (the convolution step) and Smooth4 (C⁴ for',
    '        p ≥ 6), in WindowObligations.',
    '    (e) Branches left for the next act`s step zero, each merged: PLACE-papers push-b602; relay push-b602 and push-b602-closing.',
    '    (f) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b602_census_closing.txt'), ('b327_faces_census.py', 'b602_faces_census_closing.txt'),
                      ('b303_pins.py', 'b602_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b602'])
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
    for tag in TAGS:
        tl = g(K, 'rev-parse', tag + '^{commit}')
        tr = [l.split('\t')[0] for l in g(K, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
        heads.append('      %-32s tag %s peeled local %s ; remote %s ; %s' % ('SIDE-explicit-formula', tag, tl[:12], (tr[0] if tr else '')[:12],
                                                                                'AGREE' if tr and tl == tr[0] else '### DIFFER'))
    for b in KEPT:
        loc = g(K, 'rev-parse', 'refs/heads/' + b)
        rem = g(K, 'ls-remote', 'origin', 'refs/heads/' + b).split('\t')[0]
        heads.append('      %-32s local %s ; remote %s ; %s (kept)' % (b, loc[:12], rem[:12], 'AGREE' if loc and loc == rem else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED, NOT WRITTEN BY THIS ACT' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?'))
    S = json.load(io.open(os.path.join(D, 'b602_scores.json'), encoding='utf-8'))
    pre, post = rd('b602_checks.txt'), rd('b602_checks_postpush.txt')
    L = ['=' * 104,
         'b602 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWENTY-NINE: THE AUDIT FILE AT v0.19.1; THE SIGN OF λ_1; (E3)`S WINDOW, UNDER (R212).**', '=' * 104]
    L += ['    ' + l for l in rd('b602_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b602_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b602_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b602_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b602_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the kernel written by the point tag`s two lines and the tagged merge alone ; no worktree made or removed ; no keystone edited', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b602_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
