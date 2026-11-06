# -*- coding: utf-8 -*-
"""tools/b743_sitting_greps.py -- (R353)(4)(A), THE AGENDA'S SOURCE: the seat's grep for "Epstein", "Z_Q", "off-line", "numerically located" over
PLACE-papers (git grep at HEAD, tracked files only) and every kernel's README.md (D:/SIDE-*/README.md at each kernel's HEAD, by git grep), each
term's count of lines printed per file, the lines themselves listed by path and line. Reads only; with --bank writes data/b743_sitting_greps.txt.

  python -X utf8 -u tools/b743_sitting_greps.py [--bank]
"""
import glob
import os
import subprocess
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
PP = 'D:/MY-DOwnloads/PLACE-papers'
TERMS = ('Epstein', 'Z_Q', 'off-line', 'numerically located')


def grep(repo, term, paths=()):
    r = subprocess.run(['git', '-C', repo, 'grep', '-n', '-F', '-I', term, 'HEAD', '--'] + list(paths), capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = []
    for l in r.stdout.split('\n'):
        if not l.startswith('HEAD:'):
            continue
        _h, path, ln, text = l.split(':', 3)
        out.append((path, int(ln), text))
    return out


def main(argv):
    L = ['b743 -- (R353)(4)(A): THE AGENDA`S SOURCE, THE SEAT`S GREP FOR %s OVER PLACE-papers AND THE KERNEL READMEs (%s)' % (
        ', '.join('"%s"' % t for t in TERMS), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### git grep -n -F at each repository`s HEAD, tracked files only; PLACE-papers at %s; each kernel`s README.md at its own HEAD' % subprocess.run(
             ['git', '-C', PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True, text=True).stdout.strip(), '']
    hits = {}
    for t in TERMS:
        for path, ln, text in grep(PP, t):
            hits.setdefault(('PLACE-papers', path), {}).setdefault(t, []).append((ln, text))
    kernels = sorted(d for d in glob.glob('D:/SIDE-*') if os.path.isdir(os.path.join(d, '.git')))
    for k in kernels:
        for t in TERMS:
            for path, ln, text in grep(k, t, ['README.md']):
                hits.setdefault((os.path.basename(k), path), {}).setdefault(t, []).append((ln, text))
    L += ['## THE COUNTS BY TERM (lines ; files)']
    for t in TERMS:
        files = [f for f, d in hits.items() if t in d]
        L.append('  %-22s %5d lines ; %4d files' % ('"%s"' % t, sum(len(hits[f][t]) for f in files), len(files)))
    L += ['', '## THE COUNTS BY FILE (repository path : ' + ' ; '.join(TERMS) + ')']
    for f in sorted(hits):
        L.append('  %s %s : %s' % (f[0], f[1], ' ; '.join(str(len(hits[f].get(t, []))) for t in TERMS)))
    L += ['', '## THE KERNEL READMEs READ: %d (%s)' % (len(kernels), ', '.join(os.path.basename(k) for k in kernels)), '',
          '## THE LINES (repository path :line | the terms on it | the line, first 220 characters)']
    for f in sorted(hits):
        lines = {}
        for t, rows in hits[f].items():
            for ln, text in rows:
                lines.setdefault(ln, [set(), text])[0].add(t)
        for ln in sorted(lines):
            ts, text = lines[ln]
            L.append('  %s %s :%d | %s | %s' % (f[0], f[1], ln, ', '.join(t for t in TERMS if t in ts), text.strip()[:220]))
    # ### THE CANDIDATES: the lines of the current doors (not the archives, the deposited outputs, the ledgers FINDINGS / OPEN_TRAILS /
    # ### VERIFICATION_LOOM, or a paper's superseded editions) that name the instance: "Z_Q" or "numerically located" on the line, or
    # ### "Epstein" and "off-line" together. "off-line" alone is the ζ vocabulary of the corpus and names no instance.
    OLD = ('archive/', 'outputs/', 'FINDINGS.md', 'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'day1/A_Place_to_Stand_v5', 'day1/Which_Structure_Confines.md',
           'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3',
           'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6')
    cand = []
    for f in sorted(hits):
        if f[0] == 'PLACE-papers' and (f[1].startswith(OLD) or 'THE_KEYSTONE_CENSUS_v0_' in f[1] and not f[1].endswith('v0_8_3.md')):
            continue
        lines = {}
        for t, rows in hits[f].items():
            for ln, text in rows:
                lines.setdefault(ln, [set(), text])[0].add(t)
        for ln in sorted(lines):
            ts, text = lines[ln]
            if 'Z_Q' in ts or 'numerically located' in ts or ('Epstein' in ts and 'off-line' in ts):
                cand.append('  %s %s :%d | %s | %s' % (f[0], f[1], ln, ', '.join(t for t in TERMS if t in ts), text.strip()[:300]))
    L += ['', '## THE CANDIDATES FOR (A): the current doors` lines naming the instance ("Z_Q" or "numerically located", or "Epstein" with "off-line"); '
          'the archives, deposited outputs, ledgers and superseded editions set aside; %d lines' % len(cand)] + cand
    tot = sum(len(v) for d in hits.values() for v in d.values())
    L += ['', '### ### **TERMS 4 ; FILES %d ; LINE HITS %d ; KERNEL READMEs READ %d ; CANDIDATES FOR (A) %d.**' % (len(hits), tot, len(kernels), len(cand))]
    print('\n'.join(L[-(len(cand) + 3):]))
    if '--bank' in argv:
        with open('D:/relay/data/b743_sitting_greps.txt', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(L) + '\n')
        print('written data/b743_sitting_greps.txt (%d lines)' % len(L))


if __name__ == '__main__':
    main(sys.argv[1:])
