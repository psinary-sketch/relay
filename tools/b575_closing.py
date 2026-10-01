# -*- coding: utf-8 -*-
"""b575_closing.py -- THE CLOSING RECORD OF b575, UNDER (R185).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b575_closing.txt from the act's banks. It writes nothing else.
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
    for tool, out in (('b307_handoff_census.py', 'b575_census_closing.txt'), ('b327_faces_census.py', 'b575_faces_census_closing.txt'),
                      ('b303_pins.py', 'b575_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b575'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b575)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b575_scores.json'), encoding='utf-8'))
    pre, post = rd('b575_checks.txt'), rd('b575_checks_postpush.txt')
    L = ['=' * 104,
         'b575 -- THE CLOSING RECORD. ### **LANE THREE, ACT THREE: CP-5 -- THE RECONCILING EDITS AS RULED: THE MIRROR AT THE '
         'DEPOSITED BYTES, ANOMALY 1 AS A PAIR OF PINS, THE THREE FACTS IN REGISTRY, THE DESCRIPTION BY THE (R110) ROUTE WITH '
         'FETCH-BACK, THE lv RECORD READ, UNDER (R185). CP-5 %s.**' % S['cp5'], '=' * 104]
    L += ['    ' + l for l in rd('b575_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b575_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b575_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b575_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b575_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R185)(4)**: CP-7 act one -- the observation document`s purpose statement, drafted by the seat',
          '        from the ledgers in the author`s own sentences (the register sentence, the ceiling`s seven sentences, the three layers',
          '        of (R153)) and printed for ruling, no edition written; and at the same boundary the memory and mirror refresh per',
          '        (R157)(6), carrying v0.2 through v0.15 and the two pages.',
          '    (b) ### **FOR THE AUTHOR, THE lv DESCRIPTION**: record 21539068 still carries the two sentences E-2026-09-25-3 reads as',
          '        resting on the false clause, as b499 fetched them; (R150)(1)`s separate ruling on that description has not been taken',
          '        (data/b575_zenodo_lv.txt).',
          '    (c) ### **FOR THE AUTHOR, SPIRAL_MAP**: :43`s annotation cites E-2026-07-13-1 for "no partition of the tree yields 83";',
          '        that erratum says it of 65 and finds 83 exact for Kernel/ + Bridge/ (re-counted, data/b575_facts.txt). And :18, :41,',
          '        :257, :268, :443 differ from the citation rule in letter, each historical (data/b575_kernel_lines.txt). Not edited.',
          '    (d) ### **FOR THE AUTHOR, THE CARRIED ROUTE**: b535`s files-unchanged predicate, carried, compares the deposition API`s bare',
          '        checksums with the records API`s md5:-prefixed ones and reads False on identical files (defect (c)); read like for like,',
          '        the files are unchanged (data/b575_files_same.txt).',
          '    (e) The terminal table did not change at b575: no housekeeping commit. This act`s closing push-out bank gains the',
          '        per-repository as-of lines after its push, and b576 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b575_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
