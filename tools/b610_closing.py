# -*- coding: utf-8 -*-
"""b610_closing.py -- THE CLOSING RECORD OF b610, UNDER (R220).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b610_closing.txt from the act's banks. It writes nothing else. The template is b609_closing.py.
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
SCORE_KEYS = (('H28a-CENSUS', 'H28b-CENSUS', 'H28c-CENSUS', 'H28a-SPIRAL', 'H28b-SPIRAL', 'H28c-SPIRAL', 'H44a', 'H44b', 'H44c', 'H44d'),
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
    '    (a) ### **THE NEXT ACT, (R220)(6)**: b611, the synthesis act for the census`s opening-listed cluster (R02, Phase 1.2);',
    '        the sequence`s acts named one per cluster on the trail record; W-ORD-QUANTIFIER-COLUMN`s generator follows the sequence.',
    '    (b) ### **FOR THE AUTHOR**: "Tier E errata-class" is the navigator`s wording (the taxonomy :20, filing-facing); nine kernels carry',
    '        local tags their remotes do not (data/b610_census.txt, Part C); REGISTRY :787 and :333 on internal/; the annex`s act.',
    '    (c) ### **FOR THE AUTHOR`S STRIKE**: the census`s readings R-1 to R-8, SPIRAL_MAP`s R-1 to R-3; the addendum banked beside',
    '        b609`s seed, relay data/b610_residue_addendum.txt.',
    '    (d) Branches left for the next act`s step zero, each merged: PLACE-papers push-b610; relay push-b610 and push-b610-closing.',
    '    (e) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
]


def main():
    for tool, out in (('b307_handoff_census.py', 'b610_census_closing.txt'), ('b327_faces_census.py', 'b610_faces_census_closing.txt'),
                      ('b303_pins.py', 'b610_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b610'])
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
    S = json.load(io.open(os.path.join(D, 'b610_scores.json'), encoding='utf-8'))
    pre, post = rd('b610_checks.txt'), rd('b610_checks_postpush.txt')
    L = ['=' * 104,
         'b610 -- THE CLOSING RECORD. ### **LANE THREE, ACT THIRTY-SEVEN: THE PHASE-STATE READING -- THE_KEYSTONE_CENSUS AT v0.3 ONE '
         'ROW PER PHASE AND CLUSTER; THE KEYSTONE TEST RULED; SPIRAL_MAP AT v0.7 POINTING TO THE ROWS, UNDER (R220).**', '=' * 104]
    L += ['    ' + l for l in rd('b610_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' ; '.join(' '.join('(%s) %s' % (k, S[k][0]) for k in ks) for ks in SCORE_KEYS), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b610_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b610_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b610_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b610_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written, tagged or branched ; no Lean call ; no worktree made or removed ; THE_KEYSTONE_CENSUS.md and '
          'SPIRAL_MAP.md unedited, v0.3 and v0.7 written beside them', '']
    L += ['### CARRIED FORWARD.'] + CARRIED + ['=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b610_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-62:]))


if __name__ == '__main__':
    main()
