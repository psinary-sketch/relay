# -*- coding: utf-8 -*-
"""b612_closing.py -- THE CLOSING RECORD OF b612, UNDER (R222).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b612_closing.txt from the act's banks. It writes nothing else. The template is b611_closing.py.
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
         'SIDE-grh-transfer', 'SIDE-rcurve', 'SIDE-frobenius', 'SIDE-class-number-anomaly', 'SIDE-dirichlet-mod-24', 'SIDE-substrate-cluster',
         'SIDE-bijection', 'SIDE-trivium', 'SIDE-spinor']
KEPT = ['detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563', 'grh-weil-b564', 'vendor-bulka-backport-b566',
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570',
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596', 'product-b600', 'doubling-keiper-b601',
        'sign-window-b602', 'family-b603']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
SCORE_KEYS = (('H46a', 'H46b', 'H46c', 'H46d'),
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
    '    (a) ### **THE NEXT ACT, (R222)(4)**: b613, the synthesis act for 2B, priced on the trail record.',
    '    (b) ### **FOR THE AUTHOR**: the valence-7 congruence (TRIVIUM_FINDINGS :171, CONSTANCE :2216: ±1 mod 24, where the argument gives',
    '        1 mod 24); (ST)³ = I written as checked where ST_cubed compiles −1 in SL₂(ℤ) (FROBENIUS :75, :93; TRIVIUM_IDENTITY_SUBSPACE :174);',
    '        the mod-24 isomorphism stated as verified where no declaration states it (CLASS_NUMBER_ANOMALY :53, :130, :134); CONSTANCE :1315`s',
    '        79981 = 11 × 661 (= 7271) against :2469; CONSTANCE`s dropped superscripts and :2667`s SL₃(ℤ); TRIVIUM_FINDINGS :255 against :257;',
    '        CONSTANCE synthesised as the census row lists it, its reclassification noted.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the pin-resolution rule; the dirichlet-mod-24 row at argument-supported; the routes` verdicts,',
    '        six listed for the sieve`s next version; the tier read from the rows, KC.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b612; relay push-b612 and push-b612-closing.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b612_census_closing.txt'), ('b327_faces_census.py', 'b612_faces_census_closing.txt'),
                      ('b303_pins.py', 'b612_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b612'])
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
    S = json.load(io.open(os.path.join(D, 'b612_scores.json'), encoding='utf-8'))
    pre, post = rd('b612_checks.txt'), rd('b612_checks_postpush.txt')
    L = ['=' * 104,
         'b612 -- THE CLOSING RECORD. ### **LANE THREE, ACT THIRTY-NINE: THE SYNTHESIS FOR CLUSTER 1.5E -- ONE DOCUMENT FROM THE CLUSTER`S '
         'SIX PAPERS, EVERY CLAIM GRADED BY ITS PAPER`S OWN TEXT, THE ROUTES READ BY THE FIVE TESTS, UNDER (R222).**', '=' * 104]
    L += ['    ' + l for l in rd('b612_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b612_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b612_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b612_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b612_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; the six papers, the census and REGISTRY '
          'unedited ; the synthesis written in the cluster`s folder', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b612_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
