# -*- coding: utf-8 -*-
"""b535_tokenscan.py -- READING (9): THE TOKEN IN NO FILE, LOG, BANK, COMMIT OR TAG. ### `python tools/b535_tokenscan.py`

### The token is read from `os.environ['ZENODO_TOKEN']` here and compared against bytes; it is never printed, and nothing
### derived from it except COUNTS is written. Scanned: every `relay/data/b535_*` and `relay/tools/b535_*` file, the corpus files
### this act writes, the tag object `v0.1`, and the patch and message of every commit of this act (subject beginning `b535`) in
### four repositories, plus any uncommitted change there.
"""
import glob
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
REPOS = [ROOT, PP, SIDE, KER]
CORPUS = [os.path.join(PP, f) for f in ('FINDINGS.md', 'ERRATA.md', 'README.md', 'REGISTRY.md', 'OPEN_TRAILS.md',
                                         os.path.join('phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md'))] + [
    os.path.join(SIDE, 'CORRESPONDENCE.md')] + glob.glob(os.path.join(D, 'terminal_table*'))
NL = chr(10)


def git_bytes(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout


def main():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        print('### THE TOKEN IS NOT SET -- THE SCAN CANNOT RUN; SAID, NOT SKIPPED.')
        json.dump(dict(set=False), io.open(os.path.join(D, 'b535_tokenscan.json'), 'w', encoding='utf-8'))
        return 2
    files = sorted(set(glob.glob(os.path.join(D, 'b535_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b535_*')) + CORPUS))
    files = [f for f in files if not f.endswith('b535_tokenscan.json')]
    hits = {}
    for f in files:
        b = open(f, 'rb').read()
        if t in b:
            hits[os.path.relpath(f, 'D:\\')] = b.count(t)
    commits = 0
    for repo in REPOS:
        log = git_bytes(repo, 'log', '--pretty=%H %s', '-40').decode('utf-8', 'replace').split(NL)
        for l in log:
            if l.strip() and l.split(' ', 1)[-1].startswith('b535'):
                commits += 1
                b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                if t in b:
                    hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
        b = git_bytes(repo, 'diff', 'HEAD')
        if t in b:
            hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
    tagb = git_bytes(KER, 'cat-file', 'tag', 'v0.1')
    if t in tagb:
        hits['tag v0.1'] = tagb.count(t)
    push_logs = [f for f in files if os.path.basename(f).startswith('b535_') and 'push' in os.path.basename(f)]
    warnings = [os.path.basename(f) for f in push_logs if b'WARNING' in open(f, 'rb').read()]
    res = dict(set=True, files_scanned=len(files), commits_scanned=commits, tag_scanned=bool(tagb), hits=hits,
               hits_total=sum(hits.values()), push_logs=[os.path.basename(f) for f in push_logs], warnings=warnings)
    json.dump(res, io.open(os.path.join(D, 'b535_tokenscan.json'), 'w', encoding='utf-8'), indent=1)
    print('  files scanned %d ; commits of this act scanned %d ; tag scanned %s ; ### **TOKEN HITS : %d** ; push logs %s ; '
          'limb WARNINGs %s' % (len(files), commits, bool(tagb), res['hits_total'], res['push_logs'], warnings or 'NONE'))
    return 0 if res['hits_total'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
