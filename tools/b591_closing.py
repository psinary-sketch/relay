# -*- coding: utf-8 -*-
"""b591_closing.py -- THE CLOSING RECORD OF b591, UNDER (R201).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, reads the TECHNE-Core clone's HEAD against its remote-tracking main (not pushed, by the
### author's answer; no network read for it), and writes data/b591_closing.txt from the act's banks. It writes nothing else.
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
TE = 'D:/MY-DOwnloads/TECHNE-Core'
DOC_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'


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
    for tool, out in (('b307_handoff_census.py', 'b591_census_closing.txt'), ('b327_faces_census.py', 'b591_faces_census_closing.txt'),
                      ('b303_pins.py', 'b591_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b591'])
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
    heads.append('      %-32s latest tag %s (none made by this act)' % ('SIDE-explicit-formula', g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    th, to = g(TE, 'rev-parse', 'HEAD'), g(TE, 'rev-parse', 'origin/main')
    ahead = g(TE, 'rev-list', '--count', 'origin/main..HEAD')
    heads.append('      %-32s HEAD %s ; remote-tracking main %s ; ahead %s ; the document %s at the remote-tracking tree ; %s' % (
        'TECHNE-Core (local, NOT PUSHED)', th[:12], to[:12], ahead,
        'ABSENT' if not g(TE, 'ls-tree', '--name-only', 'origin/main', '--', DOC_REL) else '### PRESENT',
        'AS ANSWERED' if ahead == '1' and th != to else '### NOT AS ANSWERED'))
    S = json.load(io.open(os.path.join(D, 'b591_scores.json'), encoding='utf-8'))
    h = json.load(io.open(os.path.join(D, 'b591_h32.json'), encoding='utf-8'))
    pre, post = rd('b591_checks.txt'), rd('b591_checks_postpush.txt')
    L = ['=' * 104,
         'b591 -- THE CLOSING RECORD. ### **LANE THREE, ACT EIGHTEEN: THE LOCATED-CLAUSE METHOD DOCUMENT WRITTEN FROM THE LEDGERS, '
         'PLACED BESIDE THE b257 DRAFTS IN TECHNE-Core AND NOT PUSHED; THE WITNESS RATIO AS (E3); THE E0 RULE`S EXISTENTIAL-BINDER '
         'CLAUSE, UNDER (R201).**', '=' * 104]
    L += ['    ' + l for l in rd('b591_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('%s %s' % (k, S[k][0]) for k in ('H32a', 'H32b', 'H32c')) + ' ; ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b591_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b591_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b591_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b591_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written ; no worktree made or removed ; the TECHNE-Core commit local only', '']
    hk = rd('b591_housekeeping_push_out.txt')
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R201)(6)**: the RESIDUE edition by the form; the author rules on the closing.',
          '    (b) ### **ANSWERED BEFORE b591`s SEAL, THE AUTHOR**: the document at TECHNE-Core %s beside the b257 drafts, committed' % DOC_REL,
          '        alone and not pushed; (R201)(4)`s path and its "promotion later" clause struck as the navigator`s and recorded (OPEN_TRAILS',
          '        record); the ledgers carry the file`s name, word count (%d), sha256 (%s) and location, no body sentence.' % (h['body'], h['sha256'][:16]),
          '    (c) ### **FOR THE AUTHOR**: G-CHAIN-PAGE and G-CHAIN-PAGE-CHI fail as sealed (defect (a)) -- the zeta page`s Placement table',
          '        predates eleven editions that name its nodes, and the chi page`s banked probe output cannot resolve b590`s three Schema',
          '        declarations; the clause moves no page byte. H32b is scored by the ruling`s letter; the stricter non-blank figure is',
          '        printed beside it (defect (b)). (S1) and (S2) refuted: the pages, and one correction before the seal.',
          '    (d) %s' % ('The terminal table regenerated by the suite was committed as housekeeping before this closing (relay '
                          'data/b591_housekeeping_push_out.txt).' if hk else 'The terminal table regenerated by the suite: no housekeeping '
                                                                             'commit unless it changed (the diff json).'),
          '        This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
          '=' * 104]
    io.open(os.path.join(D, 'b591_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-44:]))


if __name__ == '__main__':
    main()
