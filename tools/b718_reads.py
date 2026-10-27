# -*- coding: utf-8 -*-
"""b718_reads.py -- (R328)(6): the spans the two reads quote, printed from the kernels' git trees at the named commits; writes nothing (the
banks data/b718_join_premise.txt and data/b718_composition.txt are written by the Write tool from this print).
Routes: `join` -- SIDE-lv-conservation's RegisterPentagon.lean :140-:160 at the deposit 93c27ec, and at SIDE-explicit-formula's tag v0.37
the declaration li_coeff_eq_taylorCoeff and the definitions it names (LiCoeff's, liCoeff's), each with its file and lines;
`find <repo> <rev> <needle>` -- the files and lines of a needle at a revision (git grep, a kernel's source tree, row (4)).
"""
import os
import re
import subprocess
import sys

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def span(repo, rev, path, lo, hi):
    L = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
    print('---- %s %s:%s :%d-:%d (blob %s)' % (os.path.basename(repo), rev, path, lo, hi, g(repo, 'rev-parse', '%s:%s' % (rev, path)).strip()[:8]))
    for i in range(lo, min(hi, len(L)) + 1):
        print('  %5d  %s' % (i, L[i - 1]))


def find(repo, rev, needle):
    out = g(repo, 'grep', '-n', '-F', needle, rev, '--', '*.lean')
    rows = [l for l in out.split(NL) if l.strip()]
    for l in rows[:40]:
        print('  ' + l[:220])
    return rows


def decl_span(repo, rev, needle, before=3, after=25):
    rows = find(repo, rev, needle)
    for l in rows:
        m = re.match(r'^[^:]+:([^:]+):(\d+):', l)
        if m and ('theorem ' + needle.split()[-1] in l or 'def ' in l or 'lemma ' in l or needle in l):
            p, n = m.group(1), int(m.group(2))
            span(repo, rev, p, max(1, n - before), n + after)
            return p, n
    return None, None


def join():
    LV, EF = 'D:/SIDE-lv-conservation', 'D:/SIDE-explicit-formula'
    files = [f for f in g(LV, 'ls-tree', '-r', '--name-only', '93c27ec').split(NL) if f.endswith('RegisterPentagon.lean')]
    print('### RegisterPentagon.lean at 93c27ec: %s' % files)
    for f in files:
        span(LV, '93c27ec', f, 140, 160)
    print('### li_coeff_eq_taylorCoeff at v0.37:')
    decl_span(EF, 'v0.37', 'theorem li_coeff_eq_taylorCoeff', 12, 20)
    print('### the definitions it names at v0.37:')
    for nd in ('def liCoeff', 'def LiCoeff', 'def taylorCoeff', 'def logXiTaylor'):
        print('## %s' % nd)
        decl_span(EF, 'v0.37', nd, 4, 10)


def locate(needle, roots):
    """Every line holding `needle` (case folded) in the text banks under each root (*.txt, *.md), path:line and the line's head."""
    n, nf = 0, needle.lower()
    for root in roots:
        walk = [(os.path.dirname(root), [], [os.path.basename(root)])] if os.path.isfile(root) else os.walk(root)
        if os.path.isfile(root):
            root = os.path.dirname(root)
        for dp, dn, fn in walk:
            dn[:] = [d for d in dn if d not in ('.git', '.lake', 'archive', 'node_modules')]
            for f in sorted(fn):
                if not f.endswith(('.txt', '.md', '.py', '.json', '.sh')):
                    continue
                p = os.path.join(dp, f)
                try:
                    L = open(p, encoding='utf-8', errors='replace').read().split(NL)
                except OSError:
                    continue
                for i, l in enumerate(L, 1):
                    if nf in l.lower():
                        n += 1
                        if n <= 80:
                            j = l.lower().index(nf)
                            print('  %s:%d  ...%s...' % (os.path.relpath(p, root), i, l[max(0, j - 90):j + 130]))
    print('### LOCATE %r: %d lines' % (needle, n))


def probe_ex(act, rev):
    """the replay's object (4)-(5) inputs at a commit, keys, modes and sizes only: each part's exercise bank and its run on the previous
    act's banks (data/<act>_exercise_<part>.json, data/<act>_prevrun_exercise_<part>.json)."""
    import json
    parts = ['standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act']
    for p in parts:
        for nm in ('%s_exercise_%s.json' % (act, p), '%s_prevrun_exercise_%s.json' % (act, p)):
            raw = subprocess.run(['git', '-C', 'D:/relay', 'show', '%s:data/%s' % (rev, nm)], capture_output=True)
            if raw.returncode:
                print('  %-44s at %s: NOT TRACKED' % (nm, rev[:8]))
                continue
            try:
                j = json.loads(raw.stdout.decode('utf-8'))
            except ValueError as e:
                print('  %-44s at %s: %d bytes, NOT JSON (%s)' % (nm, rev[:8], len(raw.stdout), str(e)[:60]))
                continue
            print('  %-44s at %s: %d bytes ; keys %s ; mode %s ; exercise rows %d' % (
                nm, rev[:8], len(raw.stdout), sorted(j)[:8], j.get('mode'), len(j.get('exercise') or {})))


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r == 'join':
        join()
    elif r == 'probe_ex' and len(sys.argv) == 4:
        probe_ex(sys.argv[2], sys.argv[3])
    elif r == 'locate' and len(sys.argv) >= 4:
        locate(sys.argv[2], sys.argv[3:])
    elif r == 'find' and len(sys.argv) == 5:
        find(*sys.argv[2:5])
    elif r == 'span' and len(sys.argv) == 7:
        span(sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]))
    else:
        sys.exit('usage: b718_reads.py join | find <repo> <rev> <needle> | span <repo> <rev> <path> <lo> <hi>')
