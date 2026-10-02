# -*- coding: utf-8 -*-
"""b596_closing.py -- THE CLOSING RECORD OF b596, UNDER (R206).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, the kernel's tag v0.17 peeled at the remote, TECHNE-Core's local main against its
### remote-tracking main (private: not pushed), and writes data/b596_closing.txt from the act's banks. It writes nothing else.
### The template is b595_closing.py.
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
        'grh-weil-b571', 'grh-weil-b572', 'grh-weil-b573', 'epstein-b590', 'simplicity-b596']
TE = 'D:/MY-DOwnloads/TECHNE-Core'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'


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
    for tool, out in (('b307_handoff_census.py', 'b596_census_closing.txt'), ('b327_faces_census.py', 'b596_faces_census_closing.txt'),
                      ('b303_pins.py', 'b596_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b596'])
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
    tl = g(K, 'rev-parse', 'v0.17^{commit}')
    tr = [l.split('\t')[0] for l in g(K, 'ls-remote', 'origin', 'refs/tags/v0.17^{}').split(NL) if l.strip()]
    heads.append('      %-32s tag v0.17 peeled local %s ; remote %s ; %s (made by this act through push_gated.sh)' % (
        'SIDE-explicit-formula', tl[:12], (tr[0] if tr else '')[:12], 'AGREE' if tr and tr[0] == tl else '### DIFFER'))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED (the tree`s one sentence, alone: %s)' % (
        'TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?',
        g(TE, 'log', '-1', '--format=%h', '--', TREE_REL)))
    S = json.load(io.open(os.path.join(D, 'b596_scores.json'), encoding='utf-8'))
    pre, post = rd('b596_checks.txt'), rd('b596_checks_postpush.txt')
    L = ['=' * 104,
         'b596 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWENTY-THREE: W-ORD-SIMPLICITY-FACE -- THE PROPORTION WALKED, THE CLAUSE AS A '
         'SALT-CHECKED PROP AT v0.17, THE FACES` SILENCE ON THE PAGE, SIMPLICITY READ FOR ITS EDITION, UNDER (R206).**', '=' * 104]
    L += ['    ' + l for l in rd('b596_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('%s %s' % (k, S[k][0]) for k in ('H29a', 'H29b', 'H29c')) + ' ; ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b596_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+'),
          '    ### the two failing arms are G-ANSWERS-BANKED (a third prompt) and G-GEN-EDIT (the entry-tag line), each refuted in its',
          '    ### letter by the author`s third answer (data/b596_author_answers.txt), the cause the navigator`s; every control behaves.']
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b596_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b596_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b596_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    one kernel written by new files, merged and tagged ; no worktree made or removed', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R206)(5)**: b597, SIMPLICITY_OF_RIEMANN_ZEROS` edition by the form from its tier block, its',
          '        work-list and the b596 addendum (data/b596_simplicity_reading.txt), released from HELD (OPEN_TRAILS :12272, H29b held);',
          '        then one CP-1b act over SILENCE_STAGES and REPARAMETERIZATION; then the research sequence from REMAINDER 5.',
          '    (b) ### **ANSWERED BY THE AUTHOR** (data/b596_author_answers.txt, verbatim with options and marks): the faces` line through',
          '        the generator`s backmatter channel; the 2,560 MB hold kept; a structure`s entry tag added to the generator commit.',
          '    (c) ### **FOR THE AUTHOR**: H29a REFUTED -- the vendored set holds the simple-on-the-line statement only as the Prop',
          '        ThmB_statement at 1/2; the theorem at 2/3 is Zeta23.thmB0_mult, upstream at FinalMult.lean :350, premised at v0.17 as',
          '        SimpleProportion (the fact correction to the work-order in data/b596_lemmas.txt (8)). H29c REFUTED in its letter: the',
          '        proportion moves the Abstract`s :24, outside the tier block; the tier block`s :505 and :509 are moved by the Prop and the',
          '        faces` silence. The pages` reaper stop (defect (c)) cost one re-run; nothing was written by the stopped run.',
          '    (d) SIDE-explicit-formula v0.17 = %s; the branch simplicity-b596 kept; TECHNE-Core not pushed.' % tl[:7],
          '    (e) The terminal table regenerated by the suite (15 rows added, 0 grade cells moved): a housekeeping commit.',
          '        This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
          '=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b596_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
