# -*- coding: utf-8 -*-
"""b603_closing.py -- THE CLOSING RECORD OF b603, UNDER (R213).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, the kernel tag v0.21 peeled at the remote, TECHNE-Core's local main against its
### remote-tracking main (private: not pushed), and writes data/b603_closing.txt from the act's banks. It writes nothing
### else. The template is b602_closing.py.
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
TAGS = ('v0.21',)
SCORE_KEYS = (('H37a', 'H37b', 'H37c', 'H37d'), ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5'))


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
    '    (a) ### **THE NEXT ACT, (R213)(5)**: b604, the edition of THE_FINDINGS_AS_THEY_STAND by the form, reorganised as the sieve',
    '        table by cluster -- each conclusion with its quantifier shape (FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY), its register, the',
    '        test that decided bright or dark and the instrument by pin, act numbers in the Correspondence back matter.',
    '    (b) ### **FOR THE AUTHOR**: defect (b) -- an API stop of the harness, not of the act, in Component 0 before the seal',
    '        (03:51:17Z to 04:01:00Z); on the resume the repositories` status and the files written were printed first, neither the',
    '        suite nor the record tool existed, both were written whole, nothing sealed, built or committed was touched.',
    '    (c) ### **FOR THE AUTHOR**: G-PAGES-COMMITTED-ALONE refuted in its letter, pre-push and post-push -- the χ page in two commits',
    '        (PLACE-papers 9567591 and the correction 19d4ac3), the second forced by the housekeeping commit`s graded row',
    '        finsetSum_insert (defect (i)); the same species the author ruled a letter refutation at b597.',
    '    (d) ### **FOR THE AUTHOR`S STRIKE**: the family indexed by the non-trivial characters mod q at their primitive inducers; q = 3,',
    '        the ruling`s q = 5 count corrected (three, not two); (R213)(2)`s two lists read distributively, the addendum a new file',
    '        beside b558`s work-list and the lv list opened in relay; the Dedekind reading at FINDINGS :7026; the ζ page re-emitted from',
    '        b602`s list at its own pin.',
    '    (e) THE DEDEKIND OBSTRUCTIONS, named and not priced: TrivialSummandPremise and EulerFactorPremise, joined in DedekindPremises.',
    '    (f) Branches left for the next act`s step zero, each merged: PLACE-papers push-b603; relay push-b603 and push-b603-closing.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b603_census_closing.txt'), ('b327_faces_census.py', 'b603_faces_census_closing.txt'),
                      ('b303_pins.py', 'b603_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b603'])
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
    S = json.load(io.open(os.path.join(D, 'b603_scores.json'), encoding='utf-8'))
    pre, post = rd('b603_checks.txt'), rd('b603_checks_postpush.txt')
    L = ['=' * 104,
         'b603 -- THE CLOSING RECORD. ### **LANE THREE, ACT THIRTY: THE FAMILY FORM OVER χ MOD q, UNDER (R213).**', '=' * 104]
    L += ['    ' + l for l in rd('b603_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b603_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b603_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b603_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b603_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the kernel written by the tagged merge alone ; no worktree made or removed ; no keystone edited', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b603_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
