# -*- coding: utf-8 -*-
"""b595_closing.py -- THE CLOSING RECORD OF b595, UNDER (R205).

### Runs the closing censuses and pins (each banked by its own tool's output), reads every repository's main and the kept
### branches at the remote by ls-remote, reads TECHNE-Core's local main against its remote-tracking main (private: not pushed),
### and writes data/b595_closing.txt from the act's banks. It writes nothing else. The template is b594_closing.py.
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
DOC_REL = 'modules/2026-10/DELIBERATION_TREE.md'
EXT_REL = 'modules/2026-10/DELIBERATION_TREE_nodes.json'


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
    for tool, out in (('b307_handoff_census.py', 'b595_census_closing.txt'), ('b327_faces_census.py', 'b595_faces_census_closing.txt'),
                      ('b303_pins.py', 'b595_pins_closing.txt')):
        rc, o = run([sys.executable, os.path.join(T, tool), 'b595'])
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
    heads.append('      %-32s latest tag %s (none made by this act)' % ('SIDE-explicit-formula', g(K, 'tag', '--sort=creatordate').split(NL)[-1]))
    te_loc, te_trk = g(TE, 'rev-parse', 'main'), g(TE, 'rev-parse', 'origin/main')
    ab = g(TE, 'rev-list', '--left-right', '--count', 'origin/main...main').split()
    heads.append('      %-32s main %s ; remote-tracking %s ; ahead %s, behind %s -- PRIVATE, NOT PUSHED (the document and its extraction, '
                 'each alone: %s, %s)' % ('TECHNE-Core', te_loc[:12], te_trk[:12], ab[1] if len(ab) == 2 else '?', ab[0] if len(ab) == 2 else '?',
                                          g(TE, 'log', '-1', '--format=%h', '--', DOC_REL), g(TE, 'log', '-1', '--format=%h', '--', EXT_REL)))
    S = json.load(io.open(os.path.join(D, 'b595_scores.json'), encoding='utf-8'))
    H = json.load(io.open(os.path.join(D, 'b595_h33.json'), encoding='utf-8'))
    pre, post = rd('b595_checks.txt'), rd('b595_checks_postpush.txt')
    L = ['=' * 104,
         'b595 -- THE CLOSING RECORD. ### **LANE THREE, ACT TWENTY-TWO: THE DELIBERATION TREE MODULE WRITTEN FROM THE PROMPTS AS A NEW '
         'DOCUMENT IN TECHNE-Core, PRIVATE AND NOT PUSHED; THE b547 CITATION SETTLED BY HISTORY LINES, UNDER (R205).**', '=' * 104]
    L += ['    ' + l for l in rd('b595_components.txt').split(NL)[2:] if l.strip()]
    L += ['    ' + ' '.join('%s %s' % (k, S[k][0]) for k in ('H33a', 'H33b', 'H33c', 'H33d')) + ' ; ' + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5')) + ' ; '
          + ' '.join('(%s) %s' % (k, S[k][0]) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), '']
    L += ['### THIS ACT`S OWN DEFECTS (the desk).'] + rd('b595_defects.txt').rstrip(NL).split(NL) + ['']
    L += ['### THE COMMITS, THE CENSUSES.',
          '    pre-push : %s' % verdict(pre, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    pre-push : %s' % verdict(pre, r'VERDICT : [A-Z ]+'),
          '    post-push : %s' % verdict(post, r'ARMS RUN : \d+\. ### LIVE PASSING : \d+\. ### LIVE FAILING : \d+[^*]*'),
          '    post-push : %s' % verdict(post, r'VERDICT : [A-Z ]+')]
    L += heads
    L += ['    censuses : %s / %s' % (verdict(rd('b595_census_closing.txt'), r'TOTAL MISSING : \d+'),
                                       verdict(rd('b595_faces_census_closing.txt'), r'TOTAL MISSING : \d+')),
          '    pins : %s' % verdict(rd('b595_pins_closing.txt'), r'REPOS HARD-FAILING : \d+'),
          '    no kernel written ; no worktree made or removed', '']
    L += ['### CARRIED FORWARD.',
          '    (a) ### **THE NEXT ACT, (R205)(5)**: b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY`s edition, H29a-H29c',
          '        as (R194)(3) fixed them; the author rules on the closing.',
          '    (b) ### **ANSWERED BEFORE THE SEAL** (data/b595_author_answers.txt, verbatim with options and marks): the node source (the',
          '        session transcripts; the extraction private beside the document; H33a in its letter on the relay banks; the standing line,',
          '        OPEN_TRAILS :12246); the relayed mark (the prose form); the history lines` place (beneath each block`s end; BALPOS re-pinned).',
          '    (c) ### **FOR THE AUTHOR**: H33a REFUTED (relay banks: %d with the question verbatim, %d with options; the transcripts: %d);' % (
              len(H['q_verbatim']), len(H['opts_verbatim']), H['nodes']),
          '        H33b REFUTED (%s, divergent nodes %s; the navigator`s head block had no recommended option and the ENUMERA cap' % (
              '%d of %d' % (round(H['rate'] * 41), 41), H['divergent']),
          '        matched); H33d REFUTED in its letter by the table`s verbatim quotations only (ceiling %d, stems %d; the body 0 and 0);' % (
              H['ceiling_table'], H['stems_table']),
          '        (N5) REFUTED by the author`s third answer (BALPOS v0.9.5 written). Defects (a) and (b) are counts in the seat`s own prompts.',
          '    (d) The document %s, sha256 %s, %d nodes, body %d words outside the tables; TECHNE-Core is not pushed.' % (
              DOC_REL, H['sha256'][:16], H['nodes'], H['body_words']),
          '    (e) The terminal table regenerated by the suite: no housekeeping commit unless it changed (the diff json).',
          '        This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
          '=' * 104]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b595_closing.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[-48:]))


if __name__ == '__main__':
    main()
