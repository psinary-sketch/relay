# -*- coding: utf-8 -*-
"""b569_closing.py -- THE CLOSING RECORD OF b569, UNDER (R179).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b569_closing.txt from the act's banks. It writes nothing else.
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
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held']


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
    for tool, out in (('b307_handoff_census.py', 'b569_census_closing.txt'), ('b327_faces_census.py', 'b569_faces_census_closing.txt'),
                      ('b303_pins.py', 'b569_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b569'])
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
    pe, pr = g(K, 'rev-parse', 'v0.11^{}'), g(K, 'ls-remote', 'origin', 'refs/tags/v0.11^{}').split('\t')[0]
    heads.append('      %-32s peeled %s ; remote %s ; %s ; tags %s' % ('v0.11', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                     g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b569_scores.json'), encoding='utf-8'))
    pre, post = rd('b569_checks.txt'), rd('b569_checks_postpush.txt')
    L = ['=' * 104,
         'b569 -- THE CLOSING RECORD. ### **LANE TWO, ACT NINE: GRH-WEIL ACT FOUR -- THE EXPLICIT FORMULA FOR χ BY THE ζ ROUTE TO ITS GOOD '
         'HEIGHTS, HELD AT VERTICALLINE`S ODD Γ FACTOR; THE PAGE`S TWO CONVERSES; THE AS-OF LINES; THE TIER KEY; THE TABLE CHECK; '
         'BULKA`S MODULES READ, UNDER (R179).**', '=' * 104]
    L += ['    ' + l for l in rd('b569_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + '; '.join('%s %s' % (k, S[k][0]) for k in ('H20b', 'H21a', 'H21b', 'H21c', 'H21d')),
          '    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b569_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b569_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b569_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b569_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the held attempt : grh-weil-b569-held, not on main ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R179)(7)**: EF_lit_chi is HELD, so GRH-Weil act five at the frontier -- the χ-analogue of',
          '        Zeta23`s WeilEF/VerticalLine, beginning at the odd Γ factor`s log-derivative bound (digamma growth past Re w = 1);',
          '        VerticalLine`s prime side (Mathlib`s LSeries_twist_vonMangoldt_eq) not yet attempted. The author rules on the closing.',
          '    (b) ### **FOR THE AUTHOR**: the as-of line gained a third form, `present at close`, for a directory that is not a',
          '        repository (b567`s old build tree) -- defect (d); the sealed face named two forms.',
          '    (c) ### **FOR THE AUTHOR**: the E0 rule reads two χ declarations as carrying a premise (IsCompact; ContDiff and',
          '        HasCompactSupport of the test function) -- defect (f); the rule is not edited.',
          '    (d) ### **FOR THE AUTHOR**: under the tier key ch_iff_rh`s page tier reads T0 (its record grade no longer lifts it) --',
          '        defect (g); H21b is NOT SCORABLE (its population, the consumed strip bounds, is empty) and N5 is scored on its second',
          '        clause with the first VACUOUS.',
          '    (e) CORRESPONDENCE rows 414-419 read 414, 415, 416, 418, 419, 417 -- defect (i); no line removed.',
          '    (f) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed; this act`s',
          '        closing push-out bank gains the per-repository as-of lines (tools/asof_lines.py) after its push, and b570 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b569_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-40:]))


if __name__ == '__main__':
    main()
