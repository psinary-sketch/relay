# -*- coding: utf-8 -*-
"""b599_closing.py -- THE CLOSING RECORD OF b599, UNDER (R209).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, TECHNE-Core's local main against its remote-tracking main (private: not pushed), and
### writes data/b599_closing.txt from the act's banks. It writes nothing else. The template is b598_closing.py.
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
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596']
TE = 'D:/MY-DOwnloads/TECHNE-Core'


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
    for tool, out in (('b307_handoff_census.py', 'b599_census_closing.txt'), ('b327_faces_census.py', 'b599_faces_census_closing.txt'),
                      ('b303_pins.py', 'b599_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b599'])
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
    S = json.load(io.open(os.path.join(D, 'b599_scores.json'), encoding='utf-8'))
    pre, post = rd('b599_checks.txt'), rd('b599_checks_postpush.txt')
    L = ['=' * 104,
         'b599 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWENTY-SIX: CP-7 ACTS EIGHTEEN AND NINETEEN -- THE EDITIONS OF '
         'SILENCE_STAGES_DEALIGNMENT AND REPARAMETERIZATION_BARRIERS FROM THEIR b598 BANKS, UNDER (R209).**', '=' * 104]
    L += ['    ' + l for l in rd('b599_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b599_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b599_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b599_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b599_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written ; no worktree made or removed ; both current versions unedited', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R209)(5)**: b600, REMAINDER 5 -- the product lemma -- the research sequence`s second item,',
          '        priced at OPEN_TRAILS :12136.',
          '    (b) ### **FOR THE AUTHOR`S STRIKE**: the collisions of both editions as listed in their back matter; the alias put on',
          '        silence_principle (the terminal named for the principle; SILENCE_FORMAL :6 names silence_universal as the compiled',
          '        universal form, cited in the history line); SILENCE :198`s fact correction (the Steane rows pinned at SIDE-cosmo), a',
          '        fifth fact correction beyond the ruled ones; the sentences read and left in each back matter.',
          '    (c) (N2) refuted in its letter (SILENCE`s fact clause made five corrections against at most four); (N4) refuted (neither',
          '        page gained a Placement row: the generator lists files naming a page node, and neither edition names one).',
          '    (d) Recorded as the navigator`s: (R209)(2)(ii)`s "beneath :4540" -- the history line appended at the end, addressed, by',
          '        the author`s answer before the seal.',
          '    (e) W-ORD-SEC-AXIOM-ARTEFACT priced, not started (OPEN_TRAILS :12330), the author`s word its trigger.',
          '    (f) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
          '=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b599_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-52:]))


if __name__ == '__main__':
    main()
