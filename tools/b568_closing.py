# -*- coding: utf-8 -*-
"""b568_closing.py -- THE CLOSING RECORD OF b568, UNDER (R178).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b568_closing.txt from the act's banks. It writes nothing else.
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
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567']


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
    for tool, out in (('b307_handoff_census.py', 'b568_census_closing.txt'), ('b327_faces_census.py', 'b568_faces_census_closing.txt'),
                      ('b303_pins.py', 'b568_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b568'])
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
    pe, pr = g(K, 'rev-parse', 'v0.10^{}'), g(K, 'ls-remote', 'origin', 'refs/tags/v0.10^{}').split('\t')[0]
    heads.append('      %-32s peeled %s ; remote %s ; %s ; tags %s' % ('v0.10', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                     g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b568_scores.json'), encoding='utf-8'))
    pre, post = rd('b568_checks.txt'), rd('b568_checks_postpush.txt')
    L = ['=' * 104,
         'b568 -- THE CLOSING RECORD. ### **LANE THREE, ACT ONE: CP-4, THE PAGE WITHOUT NARRATIVE, GENERATED FROM SIDE-explicit-formula v0.10; '
         'b567`S FOUR ITEMS; THE TAG MADE BY THE PUSH SCRIPT; THE SUITE`S AS-OF COMMIT, UNDER (R178).**', '=' * 104]
    L += ['    ' + l for l in rd('b568_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + '; '.join('%s %s' % (k, S[k][0]) for k in ('H20a', 'H20b', 'H20c', 'H20d')),
          '    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b568_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b568_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b568_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b568_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the old build tree : D:/b567-lake-51e6992e %s ; the worktree D:/b566-forward KEPT' % ('PRESENT' if os.path.exists('D:/b567-lake-51e6992e') else 'ABSENT'),
          '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R178)(8)**: b569, GRH-Weil act four -- EF_lit_chi`s proof on a branch from v0.10 by Zeta23`s route for',
          '        ζ, W-ORD-BULKA-GENERIC in front, H21a-H21d carried; push_gated.sh makes the tag (a hand-made tag is refused).',
          '    (b) ### **FOR THE AUTHOR**: H20b is REFUTED in its letter at two places -- Register4_positivity LiCoeff and Bulka`s',
          '        Taylor-coefficient positivity reach RiemannHypothesis by a compiled implication only; each converse is a short',
          '        composition of compiled pieces (rh_imp_li_nonneg, liCoeff_zero, li_coeff_eq_taylorCoeff) not stated at v0.10.',
          '    (c) ### **FOR THE AUTHOR**: b566 re-runs at 70 of 74 under the as-of commit; the four arms still failing read PLACE-papers at',
          '        HEAD, the kernel`s live refs and a clone b567 deleted -- outside the relay tree the ruling scoped. An as-of for them',
          '        needs each repository`s closing head in the push-out bank.',
          '    (d) ### **FOR THE AUTHOR**: the page`s tier cells apply the tier law mechanically -- T0 reads "DERIVES at the standard',
          '        three, no tier written in a record cell"; the law`s "compiled against a Mathlib statement" is not separately tested.',
          '    (e) The page`s name THE_CLAUSE_AND_ITS_COMPILED_FACES.md is strikeable at this closing, as (R178)(4) says.',
          '    (f) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
          '=' * 104]
    io.open(os.path.join(D, 'b568_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-40:]))


if __name__ == '__main__':
    main()
