# -*- coding: utf-8 -*-
"""b574_closing.py -- THE CLOSING RECORD OF b574, UNDER (R184).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b574_closing.txt from the act's banks. It writes nothing else.
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
    for tool, out in (('b307_handoff_census.py', 'b574_census_closing.txt'), ('b327_faces_census.py', 'b574_faces_census_closing.txt'),
                      ('b303_pins.py', 'b574_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b574'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b574)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b574_scores.json'), encoding='utf-8'))
    pre, post = rd('b574_checks.txt'), rd('b574_checks_postpush.txt')
    L = ['=' * 104,
         'b574 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWO: CP-5 -- THE DEPOSIT READ WITH NO WRITE AT ZENODO, THE DIFFERENCE LISTS, '
         'ANOMALY 1 FROM THE FETCH, THE ERRATA LOCATED, THE DESCRIPTION EDIT DRAFTED; THE ζ PAGE`S GENERATOR REPAIRED; W-ORD-GRH-WEIL '
         'CLOSED AT ITS LANDING, UNDER (R184).**', '=' * 104]
    L += ['    ' + l for l in rd('b574_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + '; '.join('%s %s' % (k, S[k][0]) for k in ('H26a', 'H26b', 'H26c', 'H26d')),
          '    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b574_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b574_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b574_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b574_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R184)(6)**: the lists are not empty, so the next act is the reconciling edits and the description',
          '        edit, as the author rules them at this closing.',
          '    (b) ### **FOR THE AUTHOR, THE LISTS**: (1) A_Place_to_Stand.md and ERRATA.md under outputs/DEPOSITED-v1.1.2 are held',
          '        LF-normalized by git; the deposit and the working tree hold CRLF; the content is equal (data/b574_pins.txt) -- whether the',
          '        corpus copy should carry the deposited bytes (a .gitattributes -text rule) is the author`s. (2) Anomaly 1: the kernel`s',
          '        tags stand at v1.7 against the record`s v1.5; no deposit carries v1.6 or v1.7. (3) Three facts REGISTRY does not state:',
          '        SPIRAL_MAP :41 (the v1.1 record`s "83 files"), :140 (SIDE-t7-topology-cmb v0.3 = 8eb0d5a), :533 (SIDE-silence-principle',
          '        v0.2.0 = 667c254) -- none contradicts it (data/b574_ledgers.txt).',
          '    (c) ### **FOR THE AUTHOR, THE DRAFT**: three sentences quoted from REGISTRY :956, :958, :960 (data/b574_description_draft.txt);',
          '        the second ends "The criterion for χ is not yet composed", which the third supersedes; which the edit carries is ruled.',
          '    (d) ### **FOR THE AUTHOR, THE ERRATA**: only E-2026-09-25-1 was ordered into a description, and it is there; -3 faces the',
          '        SIDE-lv-conservation record 21539068, which this act did not fetch (the order named two reads); -4, -5, -6 are drafts',
          '        not filed.',
          '    (e) The terminal table did not change at b574: no housekeeping commit. This act`s closing push-out bank gains the',
          '        per-repository as-of lines after its push, and b575 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b574_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
