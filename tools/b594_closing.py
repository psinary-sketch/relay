# -*- coding: utf-8 -*-
"""b594_closing.py -- THE CLOSING RECORD OF b594, UNDER (R204).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b594_closing.txt from the act's banks. It writes nothing else.
### The template is b594_closing.py.
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
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590']
ED = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md'


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
    for tool, out in (('b307_handoff_census.py', 'b594_census_closing.txt'), ('b327_faces_census.py', 'b594_faces_census_closing.txt'),
                      ('b303_pins.py', 'b594_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b594'])
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
    heads.append('      %-32s latest tag %s (none made by this act)' % ('SIDE-explicit-formula', g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b594_scores.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b594_edition.json'), encoding='utf-8'))
    pre, post = rd('b594_checks.txt'), rd('b594_checks_postpush.txt')
    L = ['=' * 104,
         'b594 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWENTY-ONE: CP-7 ACT SIXTEEN -- THE EDITION OF FACES_OF_H2_AT_FINITE_INSTANCE BY '
         'THE FORM UNDER THE PRECEDENCE ORDER; THE THREE STANDING INSTRUCTIONS ENTERED, UNDER (R204).**', '=' * 104]
    L += ['    ' + l for l in rd('b594_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('%s %s' % (k, S[k][0]) for k in ('H28a', 'H28b', 'H28c')) + ' ; ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b594_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b594_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b594_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b594_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written ; no worktree made or removed', '']
    hk = rd('b594_housekeeping_push_out.txt')
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACTS, (R204)(5)**: b595, the DELIBERATION_TREE module (TECHNE-Core modules/2026-10/, private and unpushed);',
          '        then b596, W-ORD-SIMPLICITY-FACE, the first item of the research sequence; the author rules on the closing.',
          '    (b) ### **RESOLVED BY THE SEAT UNDER THE PRECEDENCE ORDER, FOR THE AUTHOR`S STRIKE** (no prompt put): five collisions; the',
          '        draft read as v0.1; two of the ruling`s readings placed in history lines beneath the dated section 4.',
          '    (e) ### **FOR THE AUTHOR**: defect (d) -- b547`s dated blocks cite the register census as FINDINGS :4787, a blank line;',
          '        the heading is :4788; carried under the history clause with no history line.',
          '    (c) The edition %s, sha256 %s; body %d against %d; back matter %d.' % (ED, E['sha256'][:16], E['n_body'], E['n_cur'], E['n_backmatter']),
          '    (d) %s' % ('The terminal table regenerated by the suite was committed as housekeeping before this closing (relay '
                          'data/b594_housekeeping_push_out.txt).' if hk else 'The terminal table regenerated by the suite: no housekeeping '
                                                                             'commit unless it changed (the diff json).'),
          '        This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
          '=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b594_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-46:]))


if __name__ == '__main__':
    main()
