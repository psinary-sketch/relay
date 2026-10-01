# -*- coding: utf-8 -*-
"""b579_closing.py -- THE CLOSING RECORD OF b579, UNDER (R189).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b579_closing.txt from the act's banks. It writes nothing else.
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
    for tool, out in (('b307_handoff_census.py', 'b579_census_closing.txt'), ('b327_faces_census.py', 'b579_faces_census_closing.txt'),
                      ('b303_pins.py', 'b579_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b579'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b579)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b579_scores.json'), encoding='utf-8'))
    pre, post = rd('b579_checks.txt'), rd('b579_checks_postpush.txt')
    L = ['=' * 104,
         'b579 -- THE CLOSING RECORD. ### **LANE THREE, ACT SEVEN: CP-7 ACT FOUR -- THE EDITION OF FOUNDATIONS_OF_THE_SIDE_PROGRAMME '
         'BY THE FORM; H28b RESTATED ON THE BODY; THE STEM CLAUSE STANDING; b576`S RE-RUN CLOSED, UNDER (R189).**', '=' * 104]
    L += ['    ' + l for l in rd('b579_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b579_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b579_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b579_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b579_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; no worktree made or removed ; D:/b566-forward KEPT', '']
    H = json.load(io.open(os.path.join(D, 'b579_h28.json'), encoding='utf-8'))
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R189)(6)**: CP-7 act five, b580 -- the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY by the same form,',
          '        H28a-H28c scored; the author rules on the closing.',
          '    (b) ### **FOR THE AUTHOR, H28b AS RESTATED**: the body grows by %+d against a bound of %d (CREDIT 0 + removals 0 + the ruled' % (H['body_dn'], H['allowed']),
          '        history line); the second sentence is the v0.2.5 version line the author ruled, which is not a citation. The back',
          '        matter %d, excluded and printed. H28a %s ; H28c %s.' % (H['backmatter'], H['H28a'], H['H28c']),
          '    (c) ### **FOR THE AUTHOR, PATHS v0.7**: its version line inserted above :19 moves every later line two down; its own',
          '        Correspondence column and relay data/b578_edition_PATHS.txt cite the lines as b578 wrote them, and the appended section says so.',
          '    (d) The navigator`s reading recorded: the ceiling clause; the stem, ceiling and history clauses stand at the form (OPEN_TRAILS',
          '        :11904-:11908), H28b restated at :11902.',
          '    (e) The edition does not deposit and does not replace v0.2.4; its promotion is CP-8`s.',
          '    (f) The terminal table did not change at b579: no housekeeping commit. This act`s closing push-out bank gains the',
          '        per-repository as-of lines after its push, and b580 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b579_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
