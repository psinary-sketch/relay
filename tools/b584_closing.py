# -*- coding: utf-8 -*-
"""b584_closing.py -- THE CLOSING RECORD OF b584, UNDER (R194).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b584_closing.txt from the act's banks. It writes nothing else.
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
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573']


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
    for tool, out in (('b307_handoff_census.py', 'b584_census_closing.txt'), ('b327_faces_census.py', 'b584_faces_census_closing.txt'),
                      ('b303_pins.py', 'b584_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b584'])
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
    pe, pr = g(K, 'rev-parse', 'v0.15^{}'), g(K, 'ls-remote', 'origin', 'refs/tags/v0.15^{}').split('\t')[0]
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b584)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b584_scores.json'), encoding='utf-8'))
    pre, post = rd('b584_checks.txt'), rd('b584_checks_postpush.txt')
    L = ['=' * 104,
         'b584 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWELVE: CP-7 ACT NINE -- THE EDITION OF INVARIANCE_BARRIERS BY THE '
         'FORM; THE CEILING CENSUS; TWO WORK-ORDERS ENTERED, UNDER (R194).**', '=' * 104]
    L += ['    ' + l for l in rd('b584_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b584_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b584_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b584_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b584_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; no worktree made or removed ; D:/b566-forward KEPT', '']
    H = json.load(io.open(os.path.join(D, 'b584_h28.json'), encoding='utf-8'))
    C = json.load(io.open(os.path.join(D, 'b584_ceiling_census.json'), encoding='utf-8'))
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R194)(6)**: CP-7 act ten, b585 -- the edition of INDEX_ARITY_AT_THE_CRITICAL_LINE by the same form,',
          '        H28a-H28c scored; the author rules on the closing.',
          '    (b) ### **H28b, FINAL FORM**: the body +%d against %d (the credit and the version line); the back matter %d. H28a %s ; H28c %s.' % (
              H['body_dn'], H['allowed'], H['backmatter'], H['H28a'], H['H28c']),
          '    (c) ### **THE CEILING CENSUS**: top three %s ; the remaining editions %d live (the seven after this act %d) ; the roster %d.' % (
              C['top3'], C['rem8_live'], C['rem7_live'], C['total_live']),
          '    (d) ### **THE WORK-ORDERS**: W-ORD-SIMPLICITY-FACE and W-ORD-PNT-CHI entered, priced, NOT STARTED, trigger the author`s word;',
          '        SIMPLICITY_OF_RIEMANN_ZEROS` edition HELD behind the first.',
          '    (e) ### **FOR THE AUTHOR**: Face E / keyhole is not located in FINDINGS or OPEN_TRAILS (b454 read the same over 38 hits); the T3',
          '        Tier-1 scope is located at OPEN_TRAILS :6845 and credited. (N1) refuted: the census`s top three hold one spectral document.',
          '    (f) The edition does not deposit and does not replace v1.3; its promotion is CP-8`s. The terminal table did not change at',
          '        b584. This act`s closing push-out bank gains the as-of lines after its push; b585 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b584_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
