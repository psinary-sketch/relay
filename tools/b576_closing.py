# -*- coding: utf-8 -*-
"""b576_closing.py -- THE CLOSING RECORD OF b576, UNDER (R186).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b576_closing.txt from the act's banks. It writes nothing else.
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
    for tool, out in (('b307_handoff_census.py', 'b576_census_closing.txt'), ('b327_faces_census.py', 'b576_faces_census_closing.txt'),
                      ('b303_pins.py', 'b576_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b576'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; latest tag %s (no tag made at b576)' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                                              g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b576_scores.json'), encoding='utf-8'))
    pre, post = rd('b576_checks.txt'), rd('b576_checks_postpush.txt')
    L = ['=' * 104,
         'b576 -- THE CLOSING RECORD. ### **LANE THREE, ACT FOUR: CP-7 ACT ONE -- THE PURPOSE STATEMENT DRAFTED FOR RULING; '
         'THE lv DESCRIPTION ANSWERED BY APPEND; SPIRAL_MAP :43 CORRECTED BENEATH; THE MEMORY AND MIRROR REFRESH, UNDER (R186).**', '=' * 104]
    L += ['    ' + l for l in rd('b576_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b576_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b576_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b576_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b576_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel built, no branch made in a kernel, no tag ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R186)(6)**: CP-7 act two on the author`s ruling of the purpose statement -- the editions in the',
          '        order the author gives, each from its tier table and its CP-1b work-list, the page as its spine.',
          '    (b) ### **FOR THE AUTHOR, THE PURPOSE STATEMENT**: two drafts (data/b576_purpose_drafts.txt), 96 and 92 words, every author',
          '        fragment located at its line, the seat`s connective words bracketed (31, 27). Notes: (R153) names no observation document',
          '        (its working name is the author`s; Tier K with a Correspondence table); the three layers are (R157)(1)`s; README :113',
          '        qualifies the register sentence draft A quotes; "a tracking document" is (R186)(4)`s own word. The 17 work-lists follow.',
          '    (c) ### **FOR THE AUTHOR, THE MIRROR**: D:\\MY-DOwnloads\\mirror-refresh-2026-10-01.zip -- 44 files with both pages (the roster',
          '        gained them, 0ff04077), MANIFEST md5 5c3d6afd23e377efcda7357f8c448d37, source 192077f, CLEAN on all three clauses.',
          '    (d) ### **THE SUITE READS 68 OF 69, NOT CLEAN**: G-WRITELIST-KINDS fails on relay tools/mirror_prevbuild.json, the builder`s',
          '        second write, which the sealed face`s write list omitted (defect (d)); the face is not edited.',
          '    (e) The terminal table did not change at b576: no housekeeping commit. This act`s closing push-out bank gains the',
          '        per-repository as-of lines after its push, and b577 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b576_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
