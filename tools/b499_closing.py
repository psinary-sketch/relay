# -*- coding: utf-8 -*-
"""b499_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R = json.loads(read(os.path.join(D, 'b499_results.json')))
SC = json.loads(read(os.path.join(D, 'b499_scores.json')))
G = json.loads(read(os.path.join(D, 'b499_guard.json')))
GF = json.loads(read(os.path.join(D, 'b499_guard_first.json')))
REPOS = [('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'),
         ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')]


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


rec('=' * 104)
rec('b499 -- THE CLOSING RECORD. ### **TEN EDITS AT ZENODO, THREE MATCHES; THE GUARD SCANS FOR THE TOKEN.**')
rec('=' * 104)
rec('')
rec('### (1) THE GUARD.')
rec('-' * 104)
rec('    limb (v) byte-identical in four repositories : %s ; digest %s' % (G['identical'], list(G['after'].values())[0][:16]))
for x in G['cases']:
    rec('      %-44s refused %-5s warned %-5s value printed %s' % (x['label'], x['refused'], x['warned'], x['leaked']))
rec('    ### the first exercise (`b499_guard_first.json`) : all as expected %s -- VOID, it ran the old guard' % GF.get('allok'))
rec('    ### ### **AND THE LIMB`S FIRST LIVE RUN: THE FOUR PUSHES OF THIS ACT, TOKEN SET, NO REFUSAL, NO WARNING.**')
rec('')
rec('### (2) THE WRITES.')
rec('-' * 104)
rec('    token length %d, prefix %s ; targets found once %d of 10 ; entity sites %s'
    % (R['c0']['length'], R['c0']['prefix'], R['c1']['once'], R['c1']['entities']))
for rid, c in R['c2']['records'].items():
    rec('    %s  edit %d  put %d  publish %d  %s  fetch-back %s…  raw equal %s'
        % (rid, c['edit'], c['put'], c['publish'], 'MATCH' if c['match'] else 'MISMATCH',
           c['fetchback_sha256'][:16], c['raw_same']))
rec('    ERRATA %s ; notes %s' % (R['c3']['errata_id'],
                                 {k: '%d notes + %d blanks' % (v['notes'], v['blanks']) for k, v in R['c3']['notes'].items()}))
rec('')
rec('### (3) THE EXPECTATIONS.')
rec('-' * 104)
rec('    (N1) %s ; (N2) %s ; (N3) %s ; (S1) %s ; (S2) %s ; (S3) %s'
    % tuple(w(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')))
rec('')
rec('### (4) THIS ACT`S OWN DEFECTS -- FOUR.')
rec('-' * 104)
rec('    (a) ### **THE FIRST GUARD EXERCISE WAS VOID.** ### `reset --hard` after its first case restored')
rec('        ### the committed old guard, so its negative and unset cases ran the OLD hook -- the negative')
rec('        ### "pass" proved nothing and the unset case could not warn. ### Caught because the unset')
rec('        ### case FAILED; had it been the only case that could fail, the void would have passed.')
rec('    (b) ### **THE GUARD TOOL`S EXERCISE-ONLY MODE FIRST FELL THROUGH TO ITS WRITE BLOCK** -- caught')
rec('        ### by reading it before running it, and gated.')
rec('    (c) ### **TWO SUITE ARMS FAILED LIVE ON THE SEAT`S OWN ARITHMETIC** -- a hand-shifted index one')
rec('        ### short, and a base read through a helper that strips the trailing newline. ### The corpus')
rec('        ### was right both times; both runs banked.')
rec('    (d) ### **A HEREDOC`S BACKSLASHES AND A MISSING PARENTHESIS** -- the shell-typed-code species,')
rec('        ### met again; the parenthesis was caught by the parser, not by an arm.')
rec('')
rec('### (5) THE COMMITS, THE MIRROR, THE CENSUSES.')
rec('-' * 104)
rec('    pre-push first run : %s' % lw(read(os.path.join(D, 'b499_checks_carried.txt')), 'LIVE FAILING'))
rec('    post-push          : %s' % lw(read(os.path.join(D, 'b499_checks_postpush.txt')), 'ARMS RUN :'))
for name, path in REPOS:
    loc, rem = git(path, 'rev-parse', 'HEAD'), (git(path, 'ls-remote', 'origin', 'main').split() or [''])[0]
    rec('      %-22s local %s ; remote %s ; ### **%s**' % (name, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
rec('    mirror : %s' % lw(read(os.path.join(D, 'b499_mirror.txt')), 'VERDICT:'))
rec('    censuses : %s / %s' % (lw(read(os.path.join(D, 'b499_census_closing.txt')), 'TOTAL MISSING'),
                               lw(read(os.path.join(D, 'b499_faces_census_closing.txt')), 'TOTAL MISSING')))
rec('    pins : %s' % lw(read(os.path.join(D, 'b499_pins_closing.txt')), 'REPOS HARD-FAILING'))
rec('')
rec('### (6) CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **b498`S LAUNCH LOG IS UNREAD** -- pid 14280 was absent from the process table at this')
rec('        ### act`s pre-flight; the next build act reads `data/b498_ef_build.log` behind b497`s gate.')
rec('    (b) ### **THE GUARD WARNS, IT DOES NOT REFUSE, WHEN ZENODO_TOKEN IS UNSET** -- the scan covers')
rec('        ### only pushes made from a shell that holds the token. ### Stated, not hidden.')
rec('    (c) ### **`corr_row.py` STILL VALIDATES AFTER IT WRITES** (b498) -- owed.')
rec('=' * 104)
io.open(os.path.join(D, 'b499_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print('  written: b499_closing.txt')
