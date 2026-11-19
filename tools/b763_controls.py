# -*- coding: utf-8 -*-
"""tools/b763_controls.py -- (R373)(5): THE DISPATCH AND THE READ, carried from tools/b759_controls.py (b745's form, the repository a
parameter) by the Write tool, set for b763 before its first run: the items of (6), (7) and (8), each capped at its price table's upper
dispatch figure (data/b763_price.json), the kernel's cap the worklist's MAX_DISPATCHES, the planted cases, the remote heads of the form
push-b763-*, and the positive control of the targets reader at main a3aad4cc against b759's targets bank. b759's `--names` input dropped:
the build workflow at v0.41 takes `ref` and `target` alone (.github/workflows/build-module.yml :17-:21), each name printed coming from
print_targets.txt at the commit built.
No lean process runs on this host (N1); every build is the runner's, dispatched in the kernel's own build workflow at main with the commit to
build as its input, and every run is read by its run id from its downloaded artifact, the exit file governing, the axioms file read line by
line. Each dispatch row carries the free read before it, the disk read beside it and the commit of the author's word that licenses it
(standing.dispatchrows.licence: the clause of (R373) in data/b763_ferry.txt, committed at step zero). The caps: (R373) N1, "the dispatch
counts stay within the price table's upper figures": the kernel's at the worklist's MAX_DISPATCHES, each item's at its rows' upper figures;
none in SIDE-dirichlet-mod-24 ((5): "No kernel beyond SIDE-explicit-formula is written"). The kernel's remote is read from its own git config
at each call and its account printed masked; no account name is written by this tool, the rows naming each kernel by its key.

  control [--bank]                        the tool's own controls, planted and printed (data/b763_controls_control.txt with --bank)
  targets <ef> <rev>                      the whole tree's targets at rev: each line of print_targets.txt resolved to its one module
                                          (tools/b757_join.py's reader), written to data/b763_targets.json for --targets-json
  dispatch <ef|m24> <sha> <n> <item> <target ...> [--targets-json <file>]   the holds, the caps, the series, the licence, the commit a
                                          remote branch's tip, the targets modules of the tree at it; then gh workflow run; the row; the run
                                          id read back
  status <ef|m24> <run>                   the run's status and conclusion, read once (no waiting loop)
  download <ef|m24> <run>                 the run's artifacts into a new empty folder of its own under RUNS, the run completed
  read <ef|m24> <n> <run> [--new a,b]     a read row from the artifact: the exit file, the build log's errors, the axioms file line by line;
                                          with --new, each new name's axioms line read against the standard three
  errors <ef|m24> <run>                   the error blocks of the run's build.log
  axioms <ef|m24> <run>                   every axioms line of the run against the print targets: within the standard three, outside, missing
  bank                                    data/b763_controls.txt through standing.figbank: the controls first, the dispatches and reads after

  items: form ((6), push-b763-form), arith ((7)'s statements), arith_b and arith_a ((7)'s proof, FORM B and FORM A), and (8)'s squares,
         keiper, window and c1, each SIDE-explicit-formula's; none in SIDE-dirichlet-mod-24, its cap 0
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
import b763_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the two kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b763'
ROWS = os.path.join(D, 'b763_dispatch_rows.json')
BANK = os.path.join(D, 'b763_controls.txt')
CONTROL_BANK = os.path.join(D, 'b763_controls_control.txt')
ANSWERS = 'data/b763_ferry.txt'
PRICE = os.path.join(D, 'b763_price.json')
RUNS = 'D:/b763-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
KERNELS = dict(ef=dict(key=EF, path=CT.KERNELS[EF], workflow='build-module.yml', cap=K.MAX_DISPATCHES),
               m24=dict(key=M24, path=CT.KERNELS[M24], workflow='build-module.yml', cap=K.MAX_DISPATCHES_M24))
# ### each item: its kernel, the needle of its clause in the ferry bank (one line), and the price table's rows whose upper dispatch figures cap it
N6 = '(6) BUILD ONE: THE FINITE AND SIGNED PARTS OF THE FORM, on a branch push-b763-form made at main, v0.41.'
N7 = "(7) THE CENTRE: THE CONTROL'S FAILURE FROM ITS COEFFICIENTS, NO ZERO IN THE PROOF"
N8 = '(8) THE ORDERS PRICED BESIDE IT.'
ITEMS = {'form': ('ef', N6, ('(6) S1', '(6) S2', '(6) S3', '(6) S4', '(6) S5', '(6) targets', '(6) run')),
         'arith': ('ef', N7, ('(7) statements',)),
         'arith_b': ('ef', N7, ('(7) B',)),
         'arith_a': ('ef', N7, ('(7) A',)),
         'squares': ('ef', N8, ('(8) SQUARES-AT-24',)),
         'keiper': ('ef', N8, ('(8) KEIPER-FACE',)),
         'window': ('ef', N8, ('(8) WINDOW-CERTIFY',)),
         'c1': ('ef', N8, ('(8) EXPLICIT-FORMULA-C1',))}
TARGETS = os.path.join(D, 'b763_targets.json')
REMOTE_HEADS = re.compile(r'^refs/heads/(main|push-b763-[a-z0-9][a-z0-9-]*)$')
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")


def price_rows():
    return dict((r['key'], r) for r in json.load(io.open(PRICE, encoding='utf-8'))['rows'])


def item_caps(pr=None):
    """{item: the sum of its price rows' upper dispatch figures}, read from data/b763_price.json."""
    pr = pr or price_rows()
    return dict((it, sum(int(pr[k]['dispatches'][1]) for k in v[2])) for it, v in ITEMS.items())


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


def dispatch_refusal(k, item, n, rows, read, dk, caps=None):
    """why a dispatch is refused before anything is sent, or None (pure: the rows, the free read, the disk read and the item caps given)."""
    caps = caps if caps is not None else item_caps()
    if k not in KERNELS:
        return 'a kernel this tool does not dispatch in: %r (ef | m24)' % (k,)
    if item not in ITEMS:
        return 'an item (R373) does not order: %r' % (item,)
    if ITEMS[item][0] != k:
        return 'the item %s is %s`s, not %s`s' % (item, KERNELS[ITEMS[item][0]]['key'], KERNELS[k]['key'])
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    cap = KERNELS[k]['cap']
    if not 1 <= n <= cap:
        return 'dispatch %d past the act`s %d in %s ((R373) N1)' % (n, cap, KERNELS[k]['key'])
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == KERNELS[k]['key']]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d in %s rowed already' % (n, KERNELS[k]['key'])
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in %s`s series (%d rowed)' % (n, KERNELS[k]['key'], len(mine))
    of_item = [r for r in mine if r.get('item') == item]
    if len(of_item) + 1 > caps.get(item, 0):
        return 'the item %s`s dispatch %d past its price table`s upper figure %d ((R373) N1)' % (item, len(of_item) + 1, caps.get(item, 0))
    return None


def tip_refusal(full, heads):
    """None where `full` is the tip of a remote head of the act's forms (main, push-b763-*); `heads` [(sha, ref)] from one ls-remote."""
    if not re.match(r'^[0-9a-f]{40}$', full or ''):
        return 'no commit read: %r' % (full,)
    at = [ref for sha, ref in heads if sha == full and REMOTE_HEADS.match(ref)]
    return None if at else 'the commit %s is no remote branch`s tip of the forms main, push-b763-* (push it by tools/push_gated.sh first)' % full[:8]


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


def new_read(text, names):
    """each new name against the axioms file: {name: 'WITHIN' | 'OUTSIDE [..]' | 'NO AXIOMS LINE'}, and whether every one is WITHIN."""
    ax = axioms_of(text)
    out = {}
    for nm in names:
        a = ax.get(nm)
        out[nm] = 'NO AXIOMS LINE' if a is None else ('WITHIN' if set(a) <= set(STANDARD) else 'OUTSIDE [%s]' % ', '.join(a))
    return out, bool(names) and all(v == 'WITHIN' for v in out.values())


def axioms_print(text, ax):
    """the axioms print's own state: NOT RUN (the workflow's line), FAILED (error lines and no axioms line: the first error line given), RAN
    WITH ERRORS (axioms lines and error lines), RAN."""
    t = (text or '').strip()
    errs = [l for l in t.split(NL) if ': error' in l or l.startswith('error')]
    if t.startswith('NOT RUN'):
        return 'NOT RUN: %s' % t.split(NL)[0][:200]
    if errs and not ax['lines']:
        return 'FAILED, NO AXIOMS LINE: %s' % errs[0][:300]
    if errs:
        return 'RAN WITH ERRORS (%d error lines, the first: %s)' % (len(errs), errs[0][:200])
    return 'RAN' if ax['lines'] else 'EMPTY'


def _art(k, run):
    return os.path.join(RUNS, '%s-%s' % (k, run), 'build-module-%s' % run)


def _f(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def _targets(art):
    return [l.strip() for l in _f(art, 'print_targets.txt').replace('\r', '').split(NL) if l.strip()]


def cmd_dispatch(k, sha, n, item, *rest):
    rest = list(rest)
    if '--names' in rest:
        sys.exit('### NOT DISPATCHED: --names is b759`s; the workflow at v0.41 takes ref and target alone, the names from print_targets.txt')
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
        # ### the targets read from a bank a committed tool wrote (this tool's `targets`), bound to the commit dispatched
        tj = json.load(io.open(os.path.join(RELAY, tjson), encoding='utf-8')) if tjson and os.path.exists(os.path.join(RELAY, tjson)) else {}
        if target or tj.get('rev') != full or tj.get('refused') or not tj.get('modules'):
            sys.exit('### NOT DISPATCHED: the targets file %r read rev %s against the commit %s, refused %s, modules %d, targets typed beside it %s' % (
                tjson, str(tj.get('rev'))[:8], full[:8], tj.get('refused'), len(tj.get('modules') or []), bool(target)))
        target = ' '.join(tj['modules'])
        print('  the targets from %s: %d modules, read at %s' % (tjson, len(tj['modules']), tj['rev'][:8]))
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
        rows.append(DR.row('dispatch', read, kernel=kd['key'], item=item, n=int(n), workflow=kd['workflow'], at_ref='main', sha=full, target=target,
                           run=int(rid), at=at0, licence=lic, disk_mb=dk, tree=module_files(kd['path'], full)))
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
                       run=int(run), at=v['createdAt'], licence=lic, disk_mb_at_row=disk(), tree=module_files(kd['path'], full),
                       rowed_after_send='the row refused after the send; rowed by rowsent'))
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


def cmd_read(k, n, run, *rest):
    rest = list(rest)
    new = []
    if '--new' in rest:
        i = rest.index('--new')
        new = [x for x in (rest[i + 1] if i + 1 < len(rest) else '').split(',') if x]
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
    axp = axioms_print(axt, ax)
    nr, nok = new_read(axt, new)
    rows.append(DR.row('read', DR.free(), kernel=KERNELS[k]['key'], n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'],
                       built_ref=ref[0] if ref else None, built_equal=bool(ref) and ref[0] == d[0]['sha'], toolchain=ref[-1] if len(ref) > 1 else None,
                       build_exit=ex, verdict=verdict, stop=stop[:3], errors=errs[:40], sorry_warnings=len(warn_sorry), targets=len(targets),
                       axiom_lines=ax['lines'], axiom_within=ax['within'], axiom_outside=dict((a, list(b)) for a, b in ax['outside'].items()),
                       axiom_missing=ax['missing'][:60], axiom_missing_n=len(ax['missing']), sorryAx=ax['sorryAx'],
                       axioms_refused=_f(art, 'axioms_refused.txt')[:300], axioms_print=axp, new_names=nr, new_all_within=nok,
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact=art.replace('\\', '/')))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('kernel', 'n', 'run', 'conclusion', 'built_ref', 'built_equal', 'build_exit', 'verdict', 'sorry_warnings', 'targets',
                                   'axiom_lines', 'axiom_within', 'axiom_missing_n', 'sorryAx', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
    print('  THE AXIOMS PRINT: %s' % axp)
    for nm, s in nr.items():
        print('  NEW NAME %s: %s' % (nm, s))
    if new:
        print('  THE NEW NAMES: %d, ALL WITHIN THE STANDARD THREE %s' % (len(new), nok))
    for l in (r['axioms_refused'] or '').split(NL):
        if l.strip():
            print('  REFUSED BY THE WORKFLOW`S GRAMMAR: %s' % l.strip())
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


def targets_of(rev):
    """(the full sha, the modules, the names resolved to no one module, the names) of print_targets.txt at rev, each line resolved to the one
    module declaring it by tools/b757_join.py's reader (imported through tools/b758_presend.py, both unchanged)."""
    import b758_presend as P_
    full = P_.J.g('rev-parse', rev).strip()
    t = P_.J.targets_at(full)
    bad = sorted(n for n, v in t.items() if v[0] is None)
    return full, sorted(set(v[0] for v in t.values() if v[0])), bad, len(t)


def cmd_targets(k, rev):
    """data/b763_targets.json: the whole tree's targets at rev for --targets-json; nothing written where a name resolves to no one module or a
    module is not of the tree."""
    if k != 'ef':
        sys.exit('### the targets of SIDE-explicit-formula alone (ef) -- nothing written')
    full, mods, bad, n = targets_of(rev)
    nt = DR.targets_refused(' '.join(mods), module_files(KERNELS[k]['path'], full))
    print('  print_targets.txt at %s: names %d ; modules %d ; resolved to no one module %d %s ; modules not of the tree %d %s' % (
        full[:8], n, len(mods), len(bad), bad[:4], len(nt or []), (nt or [])[:4]))
    if bad or nt or not mods:
        sys.exit('### THE TARGETS REFUSED -- nothing written')
    s = json.dumps(dict(rev=full, names=n, modules=mods, refused=bad, at=_now(),
                        reader='tools/b757_join.py targets_at, through tools/b758_presend.py, both unchanged'), indent=1) + NL
    with io.open(TARGETS, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('written data/%s: %d modules for %d names at %s' % (os.path.basename(TARGETS), len(mods), n, full[:8]))


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
    nr = [new_read("'a' depends on axioms: [propext, Quot.sound]\n'b' does not depend on any axioms", ['a', 'b']),
          new_read("'a' depends on axioms: [propext, sorryAx]", ['a']), new_read("'a' depends on axioms: [propext]", ['a', 'z']), new_read('', [])]
    c('the new names on four planted files (two within, one with sorryAx, one with no line, none given)', [x[1] for x in nr],
      [x[1] for x in nr] == [True, False, False, False])
    pr = price_rows()
    caps = item_caps(pr)
    want_caps = dict(form=17, arith=1, arith_b=50, arith_a=66, squares=2, keiper=10, window=13, c1=14)
    c('each item`s cap, its price rows` upper dispatch figures (data/b763_price.json)', caps, caps == want_caps)
    kcap = sum(int(pr[k_]['dispatches'][1]) for k_ in ITEMS['form'][2] + ITEMS['arith'][2])
    c('the kernel`s cap (the worklist`s MAX_DISPATCHES) against (6)`s and (7)`s statements` upper figures, and SIDE-dirichlet-mod-24`s 0',
      (K.MAX_DISPATCHES, kcap, K.MAX_DISPATCHES_M24), (K.MAX_DISPATCHES, K.MAX_DISPATCHES_M24) == (kcap, 0) and kcap == 18)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    one_arith = [dict(kind='dispatch', kernel=EF, n=1, item='arith')]
    plants = [('m24', 'form', 1, [], good, dk), ('ef', 'weil', 1, [], good, dk), ('ef', 'e2', 1, [], good, dk), ('ef', 'form', 19, [], good, dk),
              ('ef', 'form', 2, [], good, dk), ('ef', 'form', 1, [], (2000, _now()), dk), ('ef', 'form', 1, [], good, {'C:/': 4000, 'D:/': 20000}),
              ('SIDE-kernel', 'form', 1, [], good, dk), ('ef', 'form', 1, [dict(kind='dispatch', kernel=EF, n=1)], good, dk),
              ('ef', 'arith', 2, one_arith, good, dk)]
    got = [bool(dispatch_refusal(*p, caps=caps)) for p in plants]
    c('ten planted dispatches refused (an EF item in SIDE-dirichlet-mod-24, b759`s item, E2-SEPARATION, which (12) bars, past the kernel`s '
      'cap of 18, out of series, under the hold, under the floor, a third kernel, rowed already, (7)`s statements past their upper figure of 1)',
      got, all(got))
    seventeen = [dict(kind='dispatch', kernel=EF, n=i, item='form') for i in range(1, 18)]
    passes = [dispatch_refusal('ef', 'form', 1, [], good, dk, caps=caps),
              dispatch_refusal('ef', 'arith', 2, [dict(kind='dispatch', kernel=EF, n=1, item='form')], good, dk, caps=caps),
              dispatch_refusal('ef', 'arith', 18, seventeen, good, dk, caps=caps)]
    c('three planted dispatches taken (the first, (7)`s statement after one of (6), the eighteenth at the kernel`s cap after (6)`s seventeen)',
      passes, passes == [None] * 3)
    over = dispatch_refusal('ef', 'form', 18, seventeen, good, dk, caps=caps)
    c('(6)`s eighteenth refused at its own upper figure of 17 though the kernel`s cap is 18', over, bool(over) and 'upper figure 17' in over)
    lic = {}
    for need in (N6, N7, N8):
        try:
            x = DR.licence(ANSWERS, need)
            lic[need[:3]] = (x['commit'][:8], x['line'])
        except DR.Refused as e:
            lic[need[:3]] = str(e)[:60]
    c('each clause`s licence at the committed ferry bank, the commit and the line', lic, all(isinstance(v, tuple) for v in lic.values())
      and sorted(v[1] for v in lic.values()) == [19, 21, 23])
    try:
        DR.licence(ANSWERS, '(14) A CLAUSE THE RULING DOES NOT HAVE')
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
    c('targets at main a3aad4cc: a module taken, a name with no file refused, a vendored module under its srcDir taken (refused by the tree '
      'alone)', (t1, len(t2), t3, len(t4)), t1 == [] and len(t2) == 1 and t3 == [] and len(t4) == 1)
    pl = [axioms_print("out/Axioms.lean:1:0: error: import X failed, environment already contains 'Y' from Z", axioms_read("out/Axioms.lean:1:0: error: x", ['a'])),
          axioms_print("NOT RUN: the build did not complete under the hold", axioms_read('', ['a'])),
          axioms_print("'a' depends on axioms: [propext]", axioms_read("'a' depends on axioms: [propext]", ['a']))]
    c('the axioms print`s state on three planted files (an import failure, the NOT RUN line, a clean print)', [x[:24] for x in pl],
      pl[0].startswith('FAILED, NO AXIOMS LINE') and pl[1].startswith('NOT RUN') and pl[2] == 'RAN')
    lic_j = DR.licence(ANSWERS, N6)
    rr = []
    for kw in (dict(tree=module_files(KERNELS['ef']['path'], K.EF_BASE)), dict(repo=KERNELS['ef']['path'])):
        try:
            DR.row('dispatch', (5000, _now()), kernel=EF, item='form', n=1, sha=K.EF_BASE, target='Lc.LiCriterion.ReverseDirection', run=1, at=_now(),
                   licence=lic_j, **kw)
            rr.append(None)
        except DR.Refused as e:
            rr.append(str(e)[:60])
    c('the row`s own target check on a planted dispatch row of the vendored module: given the srcDir-aware list, taken ; given the kernel`s '
      'folder alone, refused', rr, rr[0] is None and bool(rr[1]))
    heads = [('a' * 40, 'refs/heads/push-b763-form'), ('b' * 40, 'refs/heads/feature'), ('c' * 40, 'refs/heads/main'), ('e' * 40, 'refs/heads/push-b759-weil')]
    tp = (tip_refusal('a' * 40, heads), bool(tip_refusal('b' * 40, heads)), tip_refusal('c' * 40, heads), bool(tip_refusal('d' * 40, heads)),
          bool(tip_refusal('', heads)), bool(tip_refusal('e' * 40, heads)))
    c('the remote tip: a push-b763-* tip taken, another branch`s refused, main`s taken, no tip refused, no commit refused, b759`s push branch refused',
      tp, tp == (None, True, None, True, True, True))
    tf, tm, tb, tn = targets_of(K.EF_BASE)
    bj = json.load(io.open(os.path.join(D, 'b759_targets.json'), encoding='utf-8'))
    c('THE POSITIVE CONTROL: the targets reader at main a3aad4cc against b759`s targets bank (data/b759_targets.json: %d modules for %d names, '
      '%d refused)' % (len(bj['modules']), bj['names'], len(bj['refused']) if isinstance(bj['refused'], list) else bj['refused']),
      (tf[:8], len(tm), tn, len(tb)), tf == bj['rev'] and tm == sorted(bj['modules']) and tn == bj['names'] and not tb)
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b763_controls.py`s OWN CONTROLS, (R373)(5), BEFORE ITS OPENING DISPATCH (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R373)(5): THE DISPATCHES AND THE READS, BY THE RUNNER, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    for k in ('ef', 'm24'):
        kd = KERNELS[k]
        disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == kd['key']]
        reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == kd['key'])
        refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == kd['key']]
        out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (kd['key'], len(disp), kd['cap'], len(refused)))
        for r in disp:
            rd = reads.get(int(r['run']), {})
            out.append('  %d | %-8s | sha %s | run %s | free %d MB | licence %s :%s | %s, exit %s, built %s, %d errors, sorry warnings %s, targets %s, '
                       'axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, new names %s, all within %s, runner low %s MB' % (
                           r['n'], r['item'], r['sha'][:8], r['run'], r['free_mb'], r['licence']['commit'][:8], r['licence']['line'], rd.get('verdict', 'UNREAD'),
                           rd.get('build_exit'), rd.get('built_equal'), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('targets'),
                           rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}),
                           rd.get('axiom_missing_n', len(rd.get('axiom_missing') or [])),
                           rd.get('sorryAx'), len(rd.get('new_names') or {}), rd.get('new_all_within'), rd.get('runner_low_mb')))
            if rd:
                out.append('      the axioms print: %s' % (rd.get('axioms_print') or 'NOT READ BY THIS FIELD'))
        out.append('')
    nd = sum(1 for r in rows if r.get('kind') == 'dispatch')
    nk = sum(1 for r in rows if r.get('kind') == 'read' and r.get('verdict') == 'KERNEL')
    npr = sum(1 for r in rows if r.get('kind') == 'read' and r.get('verdict') == 'KERNEL' and str(r.get('axioms_print') or '').startswith('RAN'))
    out.append('### ### **DISPATCHES %d (SIDE-explicit-formula %d OF %d, SIDE-dirichlet-mod-24 %d OF %d) ; READ KERNEL (THE BUILD EXITING 0) %d, OF THEM WITH '
               'THE AXIOMS PRINT RUN %d ; THE TOOL`S CONTROLS %d OF %d.**' % (
                   nd, sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF), K.MAX_DISPATCHES,
                   sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == M24), K.MAX_DISPATCHES_M24, nk, npr, sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b763_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'targets': cmd_targets, 'dispatch': cmd_dispatch, 'rowsent': cmd_rowsent, 'status': cmd_status, 'download': cmd_download, 'read': cmd_read,
          'errors': cmd_errors, 'axioms': cmd_axioms, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
