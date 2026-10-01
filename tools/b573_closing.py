# -*- coding: utf-8 -*-
"""b573_closing.py -- THE CLOSING RECORD OF b573, UNDER (R183).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b573_closing.txt from the act's banks. It writes nothing else.
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
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570', 'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573']


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
    for tool, out in (('b307_handoff_census.py', 'b573_census_closing.txt'), ('b327_faces_census.py', 'b573_faces_census_closing.txt'),
                      ('b303_pins.py', 'b573_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b573'])
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
    heads.append('      %-32s peeled %s ; remote %s ; %s ; tags %s' % ('v0.15', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                     g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b573_scores.json'), encoding='utf-8'))
    pre, post = rd('b573_checks.txt'), rd('b573_checks_postpush.txt')
    L = ['=' * 104,
         'b573 -- THE CLOSING RECORD. ### **LANE TWO, ACT THIRTEEN: GRH-WEIL ACT EIGHT -- THE GENERIC SCHEMA FROM THE LEMMA LIST, ζ AND '
         'χ AS INSTANCES, LANDED; THE CEILING`S SUCCESSOR SENTENCE; THE PAGE AT THE DIRICHLET INSTANCE, UNDER (R183).**', '=' * 104]
    L += ['    ' + l for l in rd('b573_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + '; '.join('%s %s' % (k, S[k][0]) for k in ('H25a', 'H25b', 'H25c')),
          '    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b573_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b573_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b573_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b573_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the held attempt : none at b573 (the three modules compiled) ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R183)(6)**: the schema landed (h2_sign_cfg_iff_target, v0.15), so the next act is CP-5 -- the',
          '        deposit reconciliation carrying Anomaly 1, E-2026-09-25-1 through -6, E-2026-09-27-1 and the (R110) description edit.',
          '    (b) ### **FOR THE AUTHOR**: H25b and (N2) are refuted by one proof -- the assembly`s EF use (b321_identity, b321Norm, one_mul)',
          '        became one rewrite by the ef field; 7 of the 11 statement-naming lemmas re-targeted by substitution alone, the two Prop',
          '        wrappers zeroSideNeg and zeroSideNeg_holds were not restated.',
          '    (c) ### **FOR THE AUTHOR**: the χ page`s node list gained two schema nodes after first generation (defect (d)) so that the',
          '        page regenerates after this act`s table housekeeping; the FINDINGS entry`s node count is corrected by append at :6370.',
          '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping; this act`s closing push-out',
          '        bank gains the per-repository as-of lines after its push, and b574 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b573_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-40:]))


if __name__ == '__main__':
    main()
