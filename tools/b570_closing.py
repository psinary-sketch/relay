# -*- coding: utf-8 -*-
"""b570_closing.py -- THE CLOSING RECORD OF b570, UNDER (R180).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, and writes data/b570_closing.txt from the act's banks. It writes nothing else.
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
        'vendor-bulka-forward-b566', 'residue-discharge-b567', 'grh-weil-b567', 'grh-weil-b569', 'grh-weil-b569-held', 'grh-weil-b570']


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
    for tool, out in (('b307_handoff_census.py', 'b570_census_closing.txt'), ('b327_faces_census.py', 'b570_faces_census_closing.txt'),
                      ('b303_pins.py', 'b570_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b570'])
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
    pe, pr = g(K, 'rev-parse', 'v0.12^{}'), g(K, 'ls-remote', 'origin', 'refs/tags/v0.12^{}').split('\t')[0]
    heads.append('      %-32s peeled %s ; remote %s ; %s ; tags %s' % ('v0.12', pe[:12], pr[:12], 'AGREE' if pe == pr else '### DIFFER',
                                                                     g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    S = json.load(io.open(os.path.join(D, 'b570_scores.json'), encoding='utf-8'))
    pre, post = rd('b570_checks.txt'), rd('b570_checks_postpush.txt')
    L = ['=' * 104,
         'b570 -- THE CLOSING RECORD. ### **LANE TWO, ACT TEN: GRH-WEIL ACT FIVE -- THE WIDER STRIP, THE ODD CASE, THE PRIME AND Γ SIDES '
         'FOR χ, THE RECTANGLE IDENTITY; HELD AT FULLLINE`S FOLD; b570`S FOUR ITEMS; W-ORD-BULKA-GENERIC CLOSED, UNDER (R180).**', '=' * 104]
    L += ['    ' + l for l in rd('b570_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + '; '.join('%s %s' % (k, S[k][0]) for k in ('H22a', 'H22b', 'H22c')),
          '    ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b570_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b570_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b570_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b570_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    the held attempt : none at b570 (no statement failed) ; the worktree D:/b566-forward KEPT', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R180)(6)**: EF_lit_chi is HELD again, so act six at the frontier -- Zeta23`s FullLine for χ, its',
          '        fold restated with χ⁻¹ and the conductor (Λ`/Λ(1 − s, χ) = −(log N + Λ`/Λ(s, χ⁻¹))), then Horizontal, ZeroSumLimit,',
          '        the assembly and Main; the h2_sign_chi ⟺ GRH_chi composition after it. The author rules on the closing.',
          '    (b) ### **FOR THE AUTHOR**: (R180)(2)(g) is HELD at its form -- ch_iff_rh`s cell is FACES_LEDGER :497, which no supersession',
          '        form of the table reaches; the ruled line would make the row CONFLICT (data/b570_supersession.txt). A FACES_LEDGER',
          '        supersession form, or a FACES_LEDGER row in that ledger`s form, would carry the ruling.',
          '    (c) ### **FOR THE AUTHOR**: the class clause moves nine E0 readings, not two (N1) -- seven kernel lemmas carry the same',
          '        test-function binders (data/b570_class_survey.txt); no ledger cell moves.',
          '    (d) ### **FOR THE AUTHOR**: the hold is by the act`s extent (defect (d)), and rowgen cannot read a terminal named with ℝ',
          '        (defect (e), row 421).',
          '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping; this act`s closing push-out',
          '        bank gains the per-repository as-of lines after its push, and b571 commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b570_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-40:]))


if __name__ == '__main__':
    main()
