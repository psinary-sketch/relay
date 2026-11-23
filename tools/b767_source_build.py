# -*- coding: utf-8 -*-
"""b767_source_build.py -- (R377)(5)(a) AND (b): THE READ OF THE TWO STOPPED RUNS AND OF KFast ON A RESTORED BUILD, NO DISPATCH; THE ROUTE.

Reads, as text and nothing else (no file of a run is run, imported or written), the downloaded artifacts of three runs of
SIDE-explicit-formula's build-module workflow under D:/b766-runs (tools/b766_controls.py RUNS): 45047352154 (b766's dispatch 15, the
closing build from source), 45051503982 (dispatch 16, its repeat), each stopped under the runner's memory hold, and 45027497489 (KFast
built on a restored build). For each: the commit and toolchain built (ref.txt), the build's exit (build_exit.txt), its start and end
(build_times.txt), the memory log's samples, its low and its time, its STOP line (mem.log), and the build log's job lines (build.log): the
highest job reached, the modules built, the Window modules built and not built, the heaviest modules by their seconds.
THE MODULES BUILDING AT THE STOP: the import graph of the kernel at the commit built, each file's import lines read by predicate through
`git cat-file --batch` (no line printed); the frontier is each kernel module not built in the log whose kernel imports are each built
there. Lake runs every ready job, so the frontier is the set of modules that were building, or ready to build, when lake was stopped.
ITS CONTROLS: each kernel module named in each log resolves to a file at the commit; each run's ref is the commit 3c67b8b5; the stopped
runs' memory logs carry a STOP line beneath the hold; the restored run's log builds KFast and its low equals data/b767_price.txt :21's
7565 MB; PLANTED: KFast taken as built in run 45047352154's set leaves the frontier, and the frontier gains only modules that import it.
THE ROUTE ((R377)(5)(b)): the seat's statement, in ROUTE below, written after the read and before the trial; `write` refuses while it
is empty.

  python -X utf8 -I -u tools/b767_source_build.py dry      the read and the controls printed; nothing written
  python -X utf8 -I -u tools/b767_source_build.py write    data/b767_source_build.txt
Refuses where this file differs from its blob at the relay's HEAD (committed before its run, N2). Written by the Write tool.
"""
import hashlib
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
SELF = 'tools/b767_source_build.py'
BANK = 'data/b767_source_build.txt'
RUNS = 'D:/b766-runs'
EF = 'D:/SIDE-explicit-formula'
COMMIT = '3c67b8b5'
HOLD = 2560
RESTORED_LOW = 7565   # ### data/b767_price.txt :21, KFast on a restored build
RUNSET = ((45047352154, 'dispatch 15 of b766, the closing build from source, the restore off'),
          (45051503982, 'dispatch 16 of b766, its repeat, the restore off'),
          (45027497489, 'KFast built on a restored build, the restore on'))
STOPPED = (45047352154, 45051503982)
PREFIXES = ('SIDEExplicitFormula', 'Zeta23', 'Lc', 'Hadamard', 'FunctionsOfOneComplexVariable')
SRC = (('SIDEExplicitFormula/', ''), ('Zeta23/', ''), ('Vendored/Bulka/', 'Vendored/Bulka/'))   # ### lakefile.toml :9-:20, the vendored library's srcDir :18
WINDOW = 'SIDEExplicitFormula.Window.'
KFAST = 'SIDEExplicitFormula.Window.KFast'
ROUTE = ()   # ### the seat's statement of (5)(b), set after the read and committed before the write


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _git(repo, *a, **kw):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, **kw)


def committed():
    here = open(os.path.join(ROOT, *SELF.split('/')), 'rb').read().replace(b'\r', b'')
    r = _git(ROOT, 'show', 'HEAD:' + SELF)
    if r.returncode != 0 or r.stdout.replace(b'\r', b'') != here:
        sys.exit('### %s DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR IS NOT COMMITTED -- NOTHING RUN' % SELF)
    return _git(ROOT, 'rev-parse', '--short=8', 'HEAD').stdout.decode().strip(), hashlib.sha256(here).hexdigest()


def art(run):
    return '%s/ef-%d/build-module-%d' % (RUNS, run, run)


def text(run, name):
    p = os.path.join(art(run), name)
    if not os.path.exists(p):
        return None
    return open(p, 'rb').read().decode('utf-8', 'replace').replace('\r', '')


def secs(s):
    s = s.strip()
    m = re.fullmatch(r'([\d.]+)ms', s)
    if m:
        return float(m.group(1)) / 1000
    m = re.fullmatch(r'([\d.]+)s', s)
    if m:
        return float(m.group(1))
    m = re.fullmatch(r'(?:(\d+)m)?\s*(?:([\d.]+)s)?', s)
    if m and (m.group(1) or m.group(2)):
        return float(m.group(1) or 0) * 60 + float(m.group(2) or 0)
    return None


def read_log(run):
    """the build log's job lines: [(n, N, verb, module, seconds)]."""
    out = []
    for l in (text(run, 'build.log') or '').split(NL):
        m = re.match(r'^\S+ \[(\d+)/(\d+)\] (Built|Replayed|Building|Ran|Fetched|Compiled|Configured)\s+(\S+)(?:\s+\(([^)]*)\))?\s*$', l)
        if m:
            out.append((int(m.group(1)), int(m.group(2)), m.group(3), m.group(4), secs(m.group(5)) if m.group(5) else None))
    return out


def read_mem(run):
    t = text(run, 'mem.log') or ''
    samples = [(m.group(1), int(m.group(2))) for m in re.finditer(r'^(\S+Z) avail_mb=(\d+)\s*$', t, re.M)]
    stop = [l for l in t.split(NL) if l.startswith('STOP ')]
    return samples, stop


def graph(commit):
    """the kernel's modules at commit: {module: [kernel imports]}, by each file's import lines read by predicate (none printed)."""
    r = _git(EF, 'ls-tree', '-r', '--name-only', commit)
    paths = [p for p in r.stdout.decode('utf-8', 'replace').split() if p.endswith('.lean')]
    mods = {}
    for p in paths:
        for pre, strip in SRC:
            if p.startswith(pre):
                name = p[len(strip):-5].replace('/', '.')
                if name.split('.')[0] in PREFIXES:
                    mods[name] = p
    req = ''.join('%s:%s%s' % (commit, mods[m], NL) for m in sorted(mods)).encode('utf-8')
    r = subprocess.run(['git', '-C', EF, 'cat-file', '--batch'], input=req, capture_output=True)
    data, i, imports = r.stdout, 0, {}
    for m in sorted(mods):
        j = data.index(b'\n', i)
        head = data[i:j].split()
        size = int(head[2])
        body = data[j + 1:j + 1 + size].decode('utf-8', 'replace').replace('\r', '')
        i = j + 1 + size + 1
        imps = []
        for l in body.split(NL):
            mm = re.match(r'^(?:public\s+|private\s+)?(?:meta\s+)?import\s+(?:all\s+)?(.*)$', l)
            if mm:
                for tok in mm.group(1).split('--')[0].split():
                    if tok.split('.')[0] in PREFIXES:
                        imps.append(tok)
        imports[m] = imps
    return imports


def frontier(imports, built):
    return sorted(m for m, imps in imports.items() if m not in built and all(x in built for x in imps))


def reach(imports, roots):
    seen, todo = set(), list(roots)
    while todo:
        m = todo.pop()
        if m in seen or m not in imports:
            continue
        seen.add(m)
        todo.extend(imports[m])
    return seen


def run_read():
    rows, ctl = {}, []
    imports = graph(COMMIT)
    target = reach(imports, [m for m in imports if m.startswith('SIDEExplicitFormula.') or m.startswith('Zeta23.')])
    importers = dict((m, sorted(x for x, imps in imports.items() if m in imps)) for m in imports)
    for run, role in RUNSET:
        ref = (text(run, 'ref.txt') or '').split()
        ex = (text(run, 'build_exit.txt') or '').strip()
        bt = text(run, 'build_times.txt') or ''
        b0 = re.search(r'build start (\S+)', bt)
        b1 = re.search(r'build end (\S+)', bt)
        log = read_log(run)
        samples, stop = read_mem(run)
        low = min(samples, key=lambda s: s[1]) if samples else None
        built = set(m for _n, _N, v, m, _s in log if v in ('Built', 'Replayed', 'Compiled'))
        kern_named = sorted(set(m for _n, _N, _v, m, _s in log if m.split('.')[0] in PREFIXES))
        unresolved = [m for m in kern_named if m not in imports]
        heavy = sorted(((s, m) for _n, _N, v, m, s in log if v == 'Built' and s is not None and m.split('.')[0] in PREFIXES), reverse=True)[:12]
        win_built = [(m, s) for _n, _N, v, m, s in log if v == 'Built' and m.startswith(WINDOW)]
        win_all = sorted(m for m in imports if m.startswith(WINDOW))
        fr = frontier(dict((m, imports[m]) for m in target), built) if run in STOPPED else []
        rows[run] = dict(role=role, ref=ref, ex=ex, b0=b0.group(1) if b0 else None, b1=b1.group(1) if b1 else None, log=log, samples=samples,
                         stop=stop, low=low, built=built, unresolved=unresolved, heavy=heavy, win_built=win_built,
                         win_not=[m for m in win_all if m not in set(x for x, _s in win_built)], fr=fr, kern_named=len(kern_named))
        ctl.append(('run %d: each kernel module its log names resolves to a file at %s' % (run, COMMIT),
                    'named %d, unresolved %d' % (len(kern_named), len(unresolved)), not unresolved))
        ctl.append(('run %d: the commit built is %s' % (run, COMMIT), (ref[0][:8] if ref else 'none'), bool(ref) and ref[0].startswith(COMMIT)))
        if run in STOPPED:
            ctl.append(('run %d: the memory log carries a STOP line beneath the hold %d' % (run, HOLD), stop[0] if stop else 'none',
                        bool(stop) and 'beneath the hold %d' % HOLD in stop[0]))
    rr = rows[45027497489]
    kf = [(m, s) for m, s in rr['win_built'] if m == KFAST]
    ctl.append(('run 45027497489: its log builds KFast, and its low equals %d MB (data/b767_price.txt :21)' % RESTORED_LOW,
                'KFast %s ; low %s' % ('%.1f s' % kf[0][1] if kf and kf[0][1] is not None else 'absent', rr['low'][1] if rr['low'] else 'none'),
                bool(kf) and bool(rr['low']) and rr['low'][1] == RESTORED_LOW))
    r15 = rows[45047352154]
    tgt = dict((m, imports[m]) for m in target)
    planted = frontier(tgt, r15['built'] | {KFAST})
    gained = sorted(set(planted) - set(r15['fr']))
    ctl.append(('PLANTED: KFast taken as built in run 45047352154`s set: it leaves the frontier, and the frontier gains only modules importing it',
                'KFast in it %s ; gained %s' % (KFAST in planted, ', '.join(x.replace('SIDEExplicitFormula.', '') for x in gained) or 'none'),
                KFAST in r15['fr'] and KFAST not in planted and bool(gained) and all(KFAST in imports[g] for g in gained)))
    return rows, ctl, imports, importers, target


def lines(rows, ctl, imports, importers, target, commit, sha):
    L = ['b767 -- THE BUILD FROM SOURCE: THE READ OF THE TWO STOPPED RUNS AND OF KFast ON A RESTORED BUILD, (R377)(5)(a), AND THE ROUTE, (5)(b); '
         'no dispatch (%s)' % utc(), '',
         '### the tool %s, sha256 %s, committed at relay %s before its run; the artifacts read as text under the data volume`s run folder of' % (
             SELF, sha[:16], commit),
         '### b766 (tools/b766_controls.py :77), nothing of them run; the kernel`s import graph at %s read by predicate through git cat-file, no' % COMMIT,
         '### line of a kernel file printed; the hold %d MB (the workflow`s HOLD_MB, .github/workflows/build-module.yml :161 at 3c67b8b5)' % HOLD, '',
         '## THE KERNEL AT %s: %d modules in the libraries` folders, %d reached from SIDEExplicitFormula and Zeta23 (lakefile.toml :9-:20); the '
         'Window folder %d modules' % (COMMIT, len(imports), len(target), len([m for m in imports if m.startswith(WINDOW)])),
         '  KFast`s importers: %s' % ', '.join(x.replace('SIDEExplicitFormula.', '') for x in importers.get(KFAST, [])),
         '  KFast`s kernel imports: %s' % ', '.join(x.replace('SIDEExplicitFormula.', '') for x in imports.get(KFAST, []))]
    for run, role in RUNSET:
        r = rows[run]
        mins = None
        if r['b0'] and (r['b1'] or r['samples']):
            t0 = time.mktime(time.strptime(r['b0'], '%Y-%m-%dT%H:%M:%SZ'))
            t1 = time.mktime(time.strptime(r['b1'] or r['samples'][-1][0], '%Y-%m-%dT%H:%M:%SZ'))
            mins = (t1 - t0) / 60
        top = max((n for n, _N, _v, _m, _s in r['log']), default=0)
        tot = max((N for _n, N, _v, _m, _s in r['log']), default=0)
        L += ['', '## RUN %d -- %s' % (run, role),
              '  built %s at %s ; the exit file %s ; the build %s to %s, %s min' % (
                  (r['ref'][0][:8] if r['ref'] else 'none'), (r['ref'][-1] if len(r['ref']) > 1 else 'none'), r['ex'] or 'none', r['b0'], r['b1'],
                  '%.1f' % mins if mins is not None else '-'),
              '  THE MEMORY LOG: %d samples, the first %s MB at %s ; THE LOW %s MB at %s ; %s' % (
                  len(r['samples']), r['samples'][0][1] if r['samples'] else '-', r['samples'][0][0] if r['samples'] else '-',
                  r['low'][1] if r['low'] else '-', r['low'][0] if r['low'] else '-', r['stop'][0] if r['stop'] else 'no STOP line'),
              '  THE BUILD LOG: the highest job %d of %d ; modules built or replayed %d ; kernel modules named %d' % (top, tot, len(r['built']), r['kern_named']),
              '  the Window modules built (%d): %s' % (len(r['win_built']), ', '.join('%s %s' % (m.replace(WINDOW, ''), '%.1fs' % s if s is not None else '')
                                                                                      for m, s in r['win_built'])),
              '  the Window modules not built (%d): %s' % (len(r['win_not']), ', '.join(m.replace(WINDOW, '') for m in r['win_not']) or 'none'),
              '  the heaviest kernel modules built, by their seconds: %s' % ', '.join('%s %.0fs' % (m.replace('SIDEExplicitFormula.', ''), s)
                                                                                      for s, m in r['heavy'])]
        if run in STOPPED:
            win = [m for m in r['fr'] if m.startswith(WINDOW)]
            out = [m for m in r['fr'] if not m.startswith(WINDOW)]
            L += ['  THE MODULES BUILDING, OR READY, AT THE STOP (%d): in the Window folder %s ; outside it (%d) %s' % (
                len(r['fr']), ', '.join(m.replace(WINDOW, '') for m in win) or 'none', len(out),
                ', '.join(m.replace('SIDEExplicitFormula.', '') for m in out) or 'none')]
    L += ['', '## THE NAVIGATOR`S READING, CHECKED AGAINST THE READ ((R377)(5)(b))',
          '  "CQValues, PoleSum and Arch each import KFast": KFast`s importers read %s' % ', '.join(
              x.replace(WINDOW, '') for x in importers.get(KFAST, [])),
          '  "so KFast built beside modules outside the Window folder": at the stop of run 45047352154 the frontier outside the Window folder '
          'holds %d modules ; of run 45051503982, %d' % tuple(len([m for m in rows[r_]['fr'] if not m.startswith(WINDOW)]) for r_ in STOPPED)]
    L += ['', '## THE CONTROLS']
    L += ['  %s: %s -- %s' % (n, g, 'AS WANTED' if ok else '### NOT AS WANTED') for n, g, ok in ctl]
    L += ['', '## THE ROUTE, (R377)(5)(b), THE SEAT`S STATEMENT BEFORE THE TRIAL'] + (['  ' + x for x in ROUTE] if ROUTE else ['  ### NOT YET STATED'])
    allok = all(c[2] for c in ctl)
    L += ['', '### ### **THE READ %s: %d OF %d CONTROLS AS WANTED ; THE ROUTE %s.**' % (
        'MADE' if allok else 'WITH A CONTROL FAILED', sum(1 for c in ctl if c[2]), len(ctl), 'STATED' if ROUTE else 'NOT YET STATED')]
    return L, allok


def main(argv):
    if not argv or argv[0] not in ('dry', 'write'):
        sys.exit(__doc__)
    commit, sha = committed()
    rows, ctl, imports, importers, target = run_read()
    L, allok = lines(rows, ctl, imports, importers, target, commit, sha)
    print(NL.join(L[5:]))
    if argv[0] == 'write':
        if not ROUTE:
            sys.exit('### THE ROUTE IS NOT STATED -- NOTHING WRITTEN')
        p = os.path.join(ROOT, *BANK.split('/'))
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('written', BANK)
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
