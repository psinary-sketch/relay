# -*- coding: utf-8 -*-
"""tools/b757_controls.py -- (R367)(3): THE DISPATCH AND THE READ, carried from tools/b745_controls.py with the repository a parameter.
No lean process runs on this host (N1); every build is the runner's, dispatched in the kernel's own build workflow at main with the commit to
build as its input, and every run is read by its run id from its downloaded artifact, the exit file governing, the axioms file read line by
line. Each dispatch row carries the free read before it, the disk read beside it and the commit of the author's word that licenses it
(standing.dispatchrows.licence: the clause of (R367) in data/b757_ferry.txt, committed at step zero). The caps are the worklist's, set from
(R367)(10): at most 14 dispatches in SIDE-explicit-formula and 4 in SIDE-dirichlet-mod-24. The kernel's remote is read from its own git
config at each call and its account printed masked; no account name is written by this tool, the rows naming each kernel by its key.

  control [--bank]                        the tool's own controls, planted and printed (data/b757_controls_control.txt with --bank)
  dispatch <ef|m24> <sha> <n> <item> <target ...> [--names a,b]   the holds, the cap, the series, the licence, the commit a remote branch's
                                          tip, the targets modules of the tree at it; then gh workflow run; the row; the run id read back
  status <ef|m24> <run>                   the run's status and conclusion, read once (no waiting loop)
  download <ef|m24> <run>                 the run's artifacts into a new empty folder of its own under RUNS, the run completed
  read <ef|m24> <n> <run>                 a read row from the artifact: the exit file, the build log's errors, the axioms file line by line
  errors <ef|m24> <run>                   the error blocks of the run's build.log
  axioms <ef|m24> <run>                   every axioms line of the run against the print targets: within the standard three, outside, missing
  bank                                    data/b757_controls.txt through standing.figbank: the controls first, the dispatches and reads after

  items: join, join-repair, T0, T1, wide (SIDE-explicit-formula); workflow, mod24 (SIDE-dirichlet-mod-24)
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b757_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the two kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b757'
ROWS = os.path.join(D, 'b757_dispatch_rows.json')
BANK = os.path.join(D, 'b757_controls.txt')
CONTROL_BANK = os.path.join(D, 'b757_controls_control.txt')
ANSWERS = 'data/b757_ferry.txt'
RUNS = 'D:/b757-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
KERNELS = dict(ef=dict(key=EF, path=CT.KERNELS[EF], workflow='build-module.yml', cap=K.MAX_DISPATCHES),
               m24=dict(key=M24, path=CT.KERNELS[M24], workflow='build-module.yml', cap=K.MAX_DISPATCHES_M24))
# ### each item: its kernel and the needle of its clause in the ferry bank, one line each (ferry :15, :17, :21, :23)
ITEMS = {'join': ('ef', '(4) THE JOIN OF THE FOUR BRANCHES'), 'join-repair': ('ef', '(4) THE JOIN OF THE FOUR BRANCHES'),
         'T0': ('ef', '(5) T0 AND T1'), 'T1': ('ef', '(5) T0 AND T1'), 'wide': ('ef', '(7) THE ONE DIRECTION OVER THE WIDER STRIP'),
         'workflow': ('m24', '(6) THE MODULUS-24 MODULE'), 'mod24': ('m24', '(6) THE MODULUS-24 MODULE')}
REMOTE_HEADS = re.compile(r'^refs/heads/(main|zq-b730|push-b757-[a-z0-9][a-z0-9-]*)$')
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def remote(k):
    """(owner/name, owner) from the kernel's own origin; the owner used only to mask prints and to call gh, never written."""
    u = git(KERNELS[k]['path'], 'remote', 'get-url', 'origin').strip()
    m = re.search(r'github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$', u)
    if not m or m.group(2) != KERNELS[k]['key']:
        sys.exit('### THE REMOTE OF %s NOT READ AS ITS OWN GITHUB REPOSITORY -- nothing done' % KERNELS[k]['key'])
    return '%s/%s' % (m.group(1), m.group(2)), m.group(1)


def mask(text, owner):
    return text.replace(owner, '<account>') if owner else text


def disk():
    return dict((v, int(shutil.disk_usage(v).free // (1024 * 1024))) for v in ('C:/', 'D:/'))


def dispatch_refusal(k, item, n, rows, read, dk):
    """why a dispatch is refused before anything is sent, or None (pure: the rows, the free read and the disk read given)."""
    if k not in KERNELS:
        return 'a kernel this tool does not dispatch in: %r (ef | m24)' % (k,)
    if item not in ITEMS:
        return 'an item (R367) does not order: %r' % (item,)
    if ITEMS[item][0] != k:
        return 'the item %s is %s`s, not %s`s' % (item, KERNELS[ITEMS[item][0]]['key'], KERNELS[k]['key'])
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    cap = KERNELS[k]['cap']
    if not 1 <= n <= cap:
        return 'dispatch %d past the act`s %d in %s ((R367)(10))' % (n, cap, KERNELS[k]['key'])
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == KERNELS[k]['key']]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d in %s rowed already' % (n, KERNELS[k]['key'])
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in %s`s series (%d rowed)' % (n, KERNELS[k]['key'], len(mine))
    return None


def tip_refusal(full, heads):
    """None where `full` is the tip of a remote head of the act's forms (main, zq-b730, push-b757-*); `heads` [(sha, ref)] from one ls-remote."""
    if not re.match(r'^[0-9a-f]{40}$', full or ''):
        return 'no commit read: %r' % (full,)
    at = [ref for sha, ref in heads if sha == full and REMOTE_HEADS.match(ref)]
    return None if at else 'the commit %s is no remote branch`s tip of the forms main, zq-b730, push-b757-* (push it by tools/push_gated.sh first)' % full[:8]


def module_files(repo, sha):
    """the tree's files at sha, with each file under a lean_lib's srcDir (lakefile.toml at sha) also named relative to it, as Lake names its
    module (b722's carry-time repair, data/b722_tool_repairs.txt row (1)); for standing.dispatchrows.targets_refused."""
    tree = DR.tree_files(repo, sha)
    toml = git(repo, 'show', '%s:lakefile.toml' % sha)
    sds = [s.rstrip('/') for s in re.findall(r'^srcDir\s*=\s*"([^"]+)"', toml, re.M)]
    return tree + [f[len(sd) + 1:] for sd in sds for f in tree if f.startswith(sd + '/')]


def axioms_of(text):
    """{name: (axioms...)} from a #print axioms output; a wrapped line read whole; () for a name depending on none."""
    out = {}
    for m in AX_DEP.finditer(text or ''):
        out[m.group(1)] = tuple(x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip())
    for m in AX_NONE.finditer(text or ''):
        out[m.group(1)] = ()
    return out


def axioms_read(text, targets):
    """the axioms file against the print targets: (lines, within, outside {name: axioms}, missing [names], sorryAx)."""
    ax = axioms_of(text)
    outside = dict((n, a) for n, a in ax.items() if not set(a) <= set(STANDARD))
    missing = [t for t in targets if t not in ax]
    return dict(lines=len(ax), within=len(ax) - len(outside), outside=outside, missing=missing, sorryAx='sorryAx' in (text or ''))


def _art(k, run):
    return os.path.join(RUNS, '%s-%s' % (k, run), 'build-module-%s' % run)


def _f(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def _targets(art):
    return [l.strip() for l in _f(art, 'print_targets.txt').replace('\r', '').split(NL) if l.strip()]


def cmd_dispatch(k, sha, n, item, *rest):
    rest = list(rest)
    names = ''
    if '--names' in rest:
        i = rest.index('--names')
        names = rest[i + 1] if i + 1 < len(rest) else ''
        del rest[i:i + 2]
    tjson = None
    if '--targets-json' in rest:
        i = rest.index('--targets-json')
        tjson = rest[i + 1] if i + 1 < len(rest) else ''
        del rest[i:i + 2]
    target = ' '.join(rest)
    read, dk, rows = DR.free(), disk(), _rows()
    why = dispatch_refusal(k, item, int(n), rows, read, dk)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    kd = KERNELS[k]
    slug, owner = remote(k)
    full = git(kd['path'], 'rev-parse', sha).strip()
    if tjson is not None:
        # ### the targets read from a bank a committed tool wrote (tools/b757_join.py bank), bound to the commit dispatched
        tj = json.load(io.open(os.path.join(RELAY, tjson), encoding='utf-8')) if tjson and os.path.exists(os.path.join(RELAY, tjson)) else {}
        if target or tj.get('rev') != full or tj.get('refused') or not tj.get('modules'):
            sys.exit('### NOT DISPATCHED: the targets file %r read rev %s against the commit %s, refused %s, modules %d, targets typed beside it %s' % (
                tjson, str(tj.get('rev'))[:8], full[:8], tj.get('refused'), len(tj.get('modules') or []), bool(target)))
        target = ' '.join(tj['modules'])
        print('  the targets from %s: %d modules, read at %s, its union %s, its merges %s' % (tjson, len(tj['modules']), tj['rev'][:8], tj.get('union_ok'), tj.get('merges_ok')))
    heads = [tuple(l.split('\t')) for l in subprocess.run(['git', '-C', kd['path'], 'ls-remote', '--heads', 'origin'], capture_output=True, text=True,
                                                          encoding='utf-8', errors='replace').stdout.split(NL) if '\t' in l]
    why = tip_refusal(full, heads)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    bad = DR.targets_refused(target, module_files(kd['path'], full))
    if bad or not target:
        sys.exit('### NOT DISPATCHED: targets not modules of the tree at %s: %s' % (full[:8], bad or 'NONE GIVEN'))
    try:
        lic = DR.licence(ANSWERS, ITEMS[item][1], by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    print('  %s dispatch %s, %s at %s ; the licence %s :%d, committed %s ; free %d MB at %s, the hold %d ; volumes %s, the floor %d' % (
        kd['key'], n, item, full[:8], lic['commit'][:8], lic['line'], lic['committed_at'], read[0], read[1], DR.HOLD, dk, FLOOR))
    at0 = _now()
    cmd = ['gh', 'workflow', 'run', kd['workflow'], '--repo', slug, '--ref', 'main', '-f', 'ref=' + full, '-f', 'target=' + target]
    if names:
        cmd += ['-f', 'names=' + names]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip())
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel=kd['key'], item=item, n=int(n), sha=full, target=target, at=at0,
                           error=mask(r.stderr or '', owner)[:300]))
    else:
        m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
        rid = m.group(1) if m else ''
        for _ in range(8):
            if rid:
                break
            time.sleep(5)
            lst = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', slug, '--workflow', kd['workflow'], '--event', 'workflow_dispatch', '--limit', '5',
                                             '--json', 'databaseId,createdAt'], capture_output=True, text=True, encoding='utf-8').stdout or '[]')
            new = sorted((x['createdAt'], x['databaseId']) for x in lst if x['createdAt'] >= at0)
            rid = str(new[0][1]) if new else ''
        if not rid:
            sys.exit('### DISPATCHED, NO RUN ID READ BACK in 40 s -- no row written; read `gh run list` by hand and row it before any other dispatch')
        # ### the row's own target check given the srcDir-aware list (tree=): b757 dispatch 1's row, given repo=, read the tree alone and
        # ### refused the vendored module after the send (run 43818699881, rowed by `rowsent`)
        rows.append(DR.row('dispatch', read, kernel=kd['key'], item=item, n=int(n), workflow=kd['workflow'], at_ref='main', sha=full, target=target,
                           names=names or None, run=int(rid), at=at0, licence=lic, disk_mb=dk, tree=module_files(kd['path'], full)))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'kernel', 'item', 'n', 'sha', 'run', 'free_mb', 'at')))


def cmd_rowsent(k, sha, n, item, run, free_mb, free_at, *rest):
    """the row of a dispatch already sent whose row was refused after the send: the free read printed before that send, the run read by
    its id (a workflow_dispatch created after that read), the licence read at that read's time, the targets from the same file."""
    rest = list(rest)
    if rest[:1] != ['--targets-json'] or len(rest) != 2:
        sys.exit('### usage: rowsent <ef|m24> <sha> <n> <item> <run> <free_mb> <free_at> --targets-json <file>')
    read = (int(free_mb), free_at)
    rows = _rows()
    kd = KERNELS[k]
    why = dispatch_refusal(k, item, int(n), rows, read, disk())
    if why:
        sys.exit('### NOT ROWED: %s' % why)
    if any(int(r.get('run') or 0) == int(run) for r in rows):
        sys.exit('### NOT ROWED: run %s rowed already' % run)
    full = git(kd['path'], 'rev-parse', sha).strip()
    tj = json.load(io.open(os.path.join(RELAY, rest[1]), encoding='utf-8'))
    if tj.get('rev') != full or tj.get('refused') or not tj.get('modules'):
        sys.exit('### NOT ROWED: the targets file read at %s against %s' % (str(tj.get('rev'))[:8], full[:8]))
    v, _slug, _owner = _view(k, run)
    if v['event'] != 'workflow_dispatch' or v['createdAt'] < free_at:
        sys.exit('### NOT ROWED: run %s is %s, created %s, against the read at %s' % (run, v['event'], v['createdAt'], free_at))
    lic = DR.licence(ANSWERS, ITEMS[item][1], by=free_at)
    target = ' '.join(tj['modules'])
    rows.append(DR.row('dispatch', read, kernel=kd['key'], item=item, n=int(n), workflow=kd['workflow'], at_ref='main', sha=full, target=target,
                       names=None, run=int(run), at=v['createdAt'], licence=lic, disk_mb_at_row=disk(), tree=module_files(kd['path'], full),
                       rowed_after_send='the row refused after the send by the row`s own target check (the tree alone); rowed by rowsent'))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'kernel', 'item', 'n', 'sha', 'run', 'free_mb', 'free_at', 'at')), 'targets', len(tj['modules']))


def _view(k, run):
    slug, owner = remote(k)
    v = subprocess.run(['gh', 'run', 'view', str(run), '--repo', slug, '--json', 'status,conclusion,createdAt,updatedAt,headSha,event'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if v.returncode != 0:
        sys.exit('### THE RUN NOT READ: %s' % mask(v.stderr, owner)[:300])
    return json.loads(v.stdout), slug, owner


def cmd_status(k, run):
    v, _s, _o = _view(k, run)
    print('  %s run %s: %s, %s ; created %s ; updated %s ; event %s' % (KERNELS[k]['key'], run, v['status'], v['conclusion'] or '-', v['createdAt'], v['updatedAt'], v['event']))


def cmd_download(k, run):
    v, slug, owner = _view(k, run)
    if v['status'] != 'completed':
        sys.exit('### THE RUN IS %s -- nothing downloaded (no waiting loop: read its status again later)' % v['status'])
    dst = os.path.join(RUNS, '%s-%s' % (k, run))
    if os.path.exists(dst):
        sys.exit('### %s STANDS ALREADY -- nothing downloaded (one new empty folder a run)' % dst)
    os.makedirs(dst)
    r = subprocess.run(['gh', 'run', 'download', str(run), '--repo', slug, '--dir', dst], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip() or '(gh printed nothing)')
    for base, _dirs, files in os.walk(dst):
        for f in sorted(files):
            p = os.path.join(base, f)
            print('  %s %d bytes' % (os.path.relpath(p, dst).replace('\\', '/'), os.path.getsize(p)))
    if r.returncode != 0:
        sys.exit('### gh run download exit %d' % r.returncode)


def cmd_read(k, n, run):
    art = _art(k, run)
    if not os.path.exists(os.path.join(art, 'build_exit.txt')):
        sys.exit('### NO build_exit.txt IN %s -- nothing written (download the run first)' % art)
    v, _slug, _owner = _view(k, run)
    rows = _rows()
    d = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == KERNELS[k]['key'] and r.get('n') == int(n)]
    if not d or int(d[0]['run']) != int(run):
        sys.exit('### DISPATCH %s IN %s IS NOT RUN %s BY ITS ROW -- nothing written' % (n, KERNELS[k]['key'], run))
    if any(r.get('kind') == 'read' and r.get('kernel') == KERNELS[k]['key'] and int(r.get('run', 0)) == int(run) for r in rows):
        sys.exit('### RUN %s READ ALREADY -- nothing written' % run)
    ex = _f(art, 'build_exit.txt').strip()
    log = _f(art, 'build.log')
    mem = _f(art, 'mem.log')
    ref = _f(art, 'ref.txt').strip().split()
    errs = [l for l in log.split(NL) if l.startswith('error: ') or ': error' in l]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    stop = [l for l in mem.split(NL) if l.startswith('STOP ')]
    axt = _f(art, 'axioms.txt')
    targets = _targets(art)
    ax = axioms_read(axt, targets)
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', mem)]
    verdict = 'STOPPED UNDER THE HOLD' if stop else 'KERNEL' if ex == '0' else 'BREAKS'
    rows.append(DR.row('read', DR.free(), kernel=KERNELS[k]['key'], n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'],
                       built_ref=ref[0] if ref else None, built_equal=bool(ref) and ref[0] == d[0]['sha'], toolchain=ref[-1] if len(ref) > 1 else None,
                       build_exit=ex, verdict=verdict, stop=stop[:3], errors=errs[:40], sorry_warnings=len(warn_sorry), targets=len(targets),
                       axiom_lines=ax['lines'], axiom_within=ax['within'], axiom_outside=dict((a, list(b)) for a, b in ax['outside'].items()),
                       axiom_missing=ax['missing'][:60], sorryAx=ax['sorryAx'], axioms_refused=_f(art, 'axioms_refused.txt')[:300],
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact=art.replace('\\', '/')))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('kernel', 'n', 'run', 'conclusion', 'built_ref', 'built_equal', 'build_exit', 'verdict', 'sorry_warnings', 'targets',
                                   'axiom_lines', 'axiom_within', 'sorryAx', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
    for nm, a in sorted(ax['outside'].items()):
        print('  OUTSIDE THE STANDARD THREE: %s [%s]' % (nm, ', '.join(a)))
    for nm in ax['missing'][:40]:
        print('  NO AXIOMS LINE: %s' % nm)
    for l in errs[:20]:
        print('  ERR', l[:300])


def cmd_errors(k, run):
    log = _f(_art(k, run), 'build.log').split(NL)
    out, keep = [], 0
    for l in log:
        if re.search(r'^(error|warning: .*sorry)', l) or ': error' in l:
            keep = 16
        if keep:
            out.append(l)
            keep -= 1
    print(NL.join(out[:300]))
    print('### LOG LINES %d ; ERROR HEADS %d' % (len(log), len([l for l in log if l.startswith('error') or ': error' in l])))


def cmd_axioms(k, run):
    art = _art(k, run)
    targets = _targets(art)
    ax = axioms_of(_f(art, 'axioms.txt'))
    for t in targets:
        a = ax.get(t)
        print('  %-80s %s' % (t, 'NO AXIOMS LINE' if a is None else '[%s]%s' % (', '.join(a), '' if set(a) <= set(STANDARD) else '  OUTSIDE')))
    s = axioms_read(_f(art, 'axioms.txt'), targets)
    print('### TARGETS %d ; AXIOM LINES %d ; WITHIN THE STANDARD THREE %d ; OUTSIDE %d ; MISSING %d ; sorryAx %s' % (
        len(targets), s['lines'], s['within'], len(s['outside']), len(s['missing']), s['sorryAx']))


# ================================================================================ the tool's own controls
def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    std = axioms_of("'x' depends on axioms: [propext,\n Classical.choice, Quot.sound]").get('x')
    c('the axioms reader on a wrapped standard line', std, std == STANDARD)
    c('on an axiom-free line', axioms_of("'y' does not depend on any axioms").get('y'), axioms_of("'y' does not depend on any axioms").get('y') == ())
    c('on a name with a prime', axioms_of("'h_b'' depends on axioms: [propext]").get("h_b'"), axioms_of("'h_b'' depends on axioms: [propext]").get("h_b'") == ('propext',))
    s = axioms_read("'a' depends on axioms: [propext, sorryAx]\n'b' does not depend on any axioms", ['a', 'b', 'c'])
    c('a planted sorryAx line and a target with no line', 'outside %s ; missing %s ; sorryAx %s' % (sorted(s['outside']), s['missing'], s['sorryAx']),
      list(s['outside']) == ['a'] and s['missing'] == ['c'] and s['sorryAx'] and s['within'] == 1)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    plants = [('m24', 'join', 1, [], good, dk), ('ef', 'mod24', 1, [], good, dk), ('ef', 'join', 15, [], good, dk), ('m24', 'mod24', 5, [], good, dk),
              ('ef', 'join', 2, [], good, dk), ('ef', 'join', 1, [], (2000, _now()), dk), ('ef', 'join', 1, [], good, {'C:/': 4000, 'D:/': 20000}),
              ('SIDE-kernel', 'join', 1, [], good, dk), ('ef', 'join', 1, [dict(kind='dispatch', kernel=EF, n=1)], good, dk)]
    got = [bool(dispatch_refusal(*p)) for p in plants]
    c('nine planted dispatches refused (cross-kernel twice, past each cap, out of series, under the hold, under the floor, a third kernel, rowed '
      'already)', got, all(got))
    passes = [dispatch_refusal('ef', 'join', 1, [], good, dk), dispatch_refusal('m24', 'workflow', 1, [], good, dk),
              dispatch_refusal('ef', 'join-repair', 2, [dict(kind='dispatch', kernel=EF, n=1), dict(kind='dispatch', kernel=M24, n=1)], good, dk),
              dispatch_refusal('m24', 'mod24', 4, [dict(kind='dispatch', kernel=M24, n=i) for i in (1, 2, 3)], good, dk)]
    c('four planted dispatches taken (each kernel`s first, the second beside the other kernel`s row, the fourth at the mod-24 cap)', passes, passes == [None] * 4)
    caps = (K.MAX_DISPATCHES, K.MAX_DISPATCHES_M24)
    ferry = io.open(os.path.join(RELAY, ANSWERS), encoding='utf-8').read()
    c('the caps against (R367)(10)`s words', caps, caps == (14, 4) and 'At most 14 dispatches in SIDE-explicit-formula and 4 in SIDE-dirichlet-mod-24' in ferry)
    lic = {}
    for item in sorted(set(v[1] for v in ITEMS.values())):
        try:
            x = DR.licence(ANSWERS, item)
            lic[item] = (x['commit'][:8], x['line'])
        except DR.Refused as e:
            lic[item] = str(e)[:60]
    c('each clause`s licence at the committed ferry bank, the commit and the line', lic, all(isinstance(v, tuple) for v in lic.values())
      and sorted(v[1] for v in lic.values()) == [15, 17, 21, 23])
    try:
        DR.licence(ANSWERS, '(12) A CLAUSE THE RULING DOES NOT HAVE')
        miss = False
    except DR.Refused:
        miss = True
    c('a needle the ferry does not carry refused', miss, miss)
    rm = {}
    for k in ('ef', 'm24'):
        slug, owner = remote(k)
        rm[k] = (mask(slug, owner), bool(owner) and owner not in mask('https://github.com/%s/x/actions/runs/1' % slug, owner))
    c('each kernel`s remote read from its own config, printed masked', rm, all(v[0].startswith('<account>/') and v[1] for v in rm.values()))
    tree = module_files(KERNELS['ef']['path'], K.EF_BASE)
    t1 = DR.targets_refused('SIDEExplicitFormula.Schema.Detector', tree)
    t2 = DR.targets_refused('SIDEExplicitFormula.Schema.NoSuchModule', tree)
    t3 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', tree)
    t4 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', DR.tree_files(KERNELS['ef']['path'], K.EF_BASE))
    c('targets at main 8fbab45d: a module taken, a name with no file refused, a vendored module under its srcDir taken (refused by the tree '
      'alone)', (t1, len(t2), t3, len(t4)), t1 == [] and len(t2) == 1 and t3 == [] and len(t4) == 1)
    lic_j = DR.licence(ANSWERS, ITEMS['join'][1])
    rr = []
    for kw in (dict(tree=module_files(KERNELS['ef']['path'], K.EF_BASE)), dict(repo=KERNELS['ef']['path'])):
        try:
            DR.row('dispatch', (5000, _now()), kernel=EF, item='join', n=1, sha=K.EF_BASE, target='Lc.LiCriterion.ReverseDirection', run=1, at=_now(),
                   licence=lic_j, **kw)
            rr.append(None)
        except DR.Refused as e:
            rr.append(str(e)[:60])
    c('the row`s own target check on a planted dispatch row of the vendored module: given the srcDir-aware list, taken ; given the kernel`s '
      'folder alone (dispatch 1`s form), refused', rr, rr[0] is None and bool(rr[1]))
    heads = [('a' * 40, 'refs/heads/push-b757-join'), ('b' * 40, 'refs/heads/feature'), ('c' * 40, 'refs/heads/main')]
    tp = (tip_refusal('a' * 40, heads), bool(tip_refusal('b' * 40, heads)), tip_refusal('c' * 40, heads), bool(tip_refusal('d' * 40, heads)), bool(tip_refusal('', heads)))
    c('the remote tip: a push-b757-* tip taken, another branch`s refused, main`s taken, no tip refused, no commit refused', tp, tp == (None, True, None, True, True))
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b757_controls.py`s OWN CONTROLS, (R367)(3), BEFORE ITS OPENING DISPATCH (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R367)(3)-(7): THE DISPATCHES AND THE READS, BY THE RUNNER, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    for k in ('ef', 'm24'):
        kd = KERNELS[k]
        disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == kd['key']]
        reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == kd['key'])
        refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == kd['key']]
        out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (kd['key'], len(disp), kd['cap'], len(refused)))
        for r in disp:
            rd = reads.get(int(r['run']), {})
            out.append('  %d | %-11s | sha %s | run %s | free %d MB | licence %s :%s | %s, exit %s, built %s, %d errors, sorry warnings %s, targets %s, '
                       'axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, runner low %s MB' % (
                           r['n'], r['item'], r['sha'][:8], r['run'], r['free_mb'], r['licence']['commit'][:8], r['licence']['line'], rd.get('verdict', 'UNREAD'),
                           rd.get('build_exit'), rd.get('built_equal'), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('targets'),
                           rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}), len(rd.get('axiom_missing') or []),
                           rd.get('sorryAx'), rd.get('runner_low_mb')))
        out.append('')
    nd = sum(1 for r in rows if r.get('kind') == 'dispatch')
    nk = sum(1 for r in rows if r.get('kind') == 'read' and r.get('verdict') == 'KERNEL')
    out.append('### ### **DISPATCHES %d (SIDE-explicit-formula %d OF %d, SIDE-dirichlet-mod-24 %d OF %d) ; READ KERNEL %d ; THE TOOL`S CONTROLS %d OF %d.**' % (
        nd, sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF), K.MAX_DISPATCHES,
        sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == M24), K.MAX_DISPATCHES_M24, nk, sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b757_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'dispatch': cmd_dispatch, 'rowsent': cmd_rowsent, 'status': cmd_status, 'download': cmd_download, 'read': cmd_read,
          'errors': cmd_errors, 'axioms': cmd_axioms, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
