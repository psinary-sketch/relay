# -*- coding: utf-8 -*-
"""b577_closing.py -- THE CLOSING RECORD OF b577, UNDER (R187).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b577_closing.txt from the act's banks. It writes nothing else.
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
         'SIDE-effects', 'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo']
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
    for tool, out in (('b307_handoff_census.py', 'b577_census_closing.txt'), ('b327_faces_census.py', 'b577_faces_census_closing.txt'),
                      ('b303_pins.py', 'b577_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b577'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b577)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b577_scores.json'), encoding='utf-8'))
    pre, post = rd('b577_checks.txt'), rd('b577_checks_postpush.txt')
    L = ['=' * 104,
         'b577 -- THE CLOSING RECORD. ### **LANE THREE, ACT FIVE: CP-7 ACT TWO -- THE PURPOSE STATEMENT APPENDED TO FINDINGS; THE '
         'OBSERVATION DOCUMENT IDENTIFIED; THE WRITE-LIST ADDENDUM; THE EDITION ORDER AND FORM, UNDER (R187).**', '=' * 104]
    L += ['    ' + l for l in rd('b577_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b577_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b577_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b577_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b577_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R187)(7)**: CP-7 act three, b578 -- the edition of PATHS_TO_THE_CRITICAL_LINE by the form entered at',
          '        OPEN_TRAILS :11864, H28a-H28c scored, on the author`s ruling of the order (data/b577_edition_order.txt).',
          '    (b) ### **FOR THE AUTHOR, THE ADDENDUM**: written as ruled, it is REFUSED by its own form -- (R186)(5) does not name',
          '        tools/mirror_prevbuild.json; (R187)(4) does. b576`s suite, wired to read the form, re-run at b576`s push: 68 of 69.',
          '    (c) ### **FOR THE AUTHOR, THE ORDER**: PATHS 29, FOUNDATIONS 16, AMC 13, then four at 10 by census position; the monograph',
          '        (31), BALANCE_AND_POSITIVITY (14) and FACES_OF_H2 (1) sit outside the keystone class and await placement.',
          '    (d) The purpose statement is at FINDINGS :6448, appended; the head placement was struck by the author before the seal.',
          '    (e) The worktree D:\\b577-rerun-b576 (at 2eae0499) is kept, as D:\\b566-forward is.',
          '    (f) The terminal table did not change at b577: no housekeeping commit. This act`s closing push-out bank gains the',
          '        per-repository as-of lines after its push, and b578 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b577_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
