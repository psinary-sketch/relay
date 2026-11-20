# -*- coding: utf-8 -*-
"""tools/b764_controls.py -- (R374)(7): THE RUNNER ON A RESTORED BUILD, THE DISPATCH AND THE READ, carried from tools/b763_controls.py (b759's
form, b745's before it) by the Write tool and set for b764 before its first run. The three dispatches of (7), each of the tip of
push-b764-runner (38a57e02, its Lean files main's at v0.43), the workflow dispatched AT that branch (`gh workflow run --ref push-b764-runner`)
so that the run reads the branch's workflow file, its third input `restore` given:
  save       the input restore on, the runner's cache holding no build of the kernel: built from source, the build saved to the cache
  reference  the input restore off, sent after the save's read shows the build saved: built from source, the key held, nothing saved
  restore    the input restore on, sent after the save's read: the build restored from the cache, then built
Each item once, capped by its price row's upper dispatch figure (data/b764_price.json: (7) reference+save 2, (7) restore 1), the kernel's
cap the worklist's MAX_DISPATCHES 3; none in SIDE-dirichlet-mod-24 ((R374) N5). No lean process runs on this host (N1); each run is read by
its run id from its downloaded artifact, the exit file governing, the axioms file read line by line; the read adds the cache's record
(out/cache_kernel.txt), the build's start and end (out/build_times.txt), the run's minutes and the commit and branch the run read its
workflow at. `compare` reads two runs' axioms files against each other line for line; `trial` composes (7)'s verdict from the read rows
and the artifacts. Each dispatch row carries the free read before it, the disk read beside it and the commit of the ruling's clause that
licenses it (standing.dispatchrows.licence: (7) in data/b764_ferry.txt, committed at step zero). The kernel's remote is read from its own git
config at each call and its account printed masked; no account name is written by this tool, the rows naming each kernel by its key.

  control [--bank]                       the tool's own controls, planted and printed (data/b764_controls_control.txt with --bank)
  targets ef <rev>                       the whole tree's targets at rev (print_targets.txt, each line resolved to its one module by
                                         tools/b757_join.py's reader), written to data/b764_targets.json for --targets-json
  dispatch ef <sha> <n> <item> --targets-json <file>   the holds, the caps, the series and the order of (7), the licence, the commit the
                                         remote tip of push-b764-runner, its workflow carrying the cache steps, the targets modules of the
                                         tree at it; then gh workflow run at the branch with restore on or off; the row; the run id read back
  status ef <run>                        the run's status and conclusion, read once (no waiting loop)
  download ef <run>                      the run's artifacts into a new empty folder of its own under RUNS, the run completed
  read ef <n> <run>                      a read row from the artifact: the exit file, the build log's errors, the axioms file line by line, the
                                         cache's record, the minutes, the commit and branch of the workflow the run read
  errors ef <run>                        the error blocks of the run's build.log
  axioms ef <run>                        every axioms line of the run against the print targets
  compare <run_a> <run_b>                the two runs' axioms files line for line
  trial                                  (7)'s verdict from the read rows: REPRODUCES, DIFFERS, FAILS or NOT TRIED, with its fields
  bank                                   data/b764_controls.txt through standing.figbank: the controls, the dispatches and reads, the trial
"""
import calendar
import hashlib
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
import b764_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the two kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b764'
ROWS = os.path.join(D, 'b764_dispatch_rows.json')
BANK = os.path.join(D, 'b764_controls.txt')
CONTROL_BANK = os.path.join(D, 'b764_controls_control.txt')
ANSWERS = 'data/b764_ferry.txt'
PRICE = os.path.join(D, 'b764_price.json')
RUNS = 'D:/b764-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
RUNS_ROLE = 'RUNS'         # ### the name a row gives that folder (no host folder written into a bank)
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
BRANCH = 'push-b764-runner'
WF = '.github/workflows/build-module.yml'
KERNELS = dict(ef=dict(key=EF, path=CT.KERNELS[EF], workflow='build-module.yml', cap=K.MAX_DISPATCHES),
               m24=dict(key=M24, path=CT.KERNELS[M24], workflow='build-module.yml', cap=K.MAX_DISPATCHES_M24))
# ### each item: its kernel, the needle of its clause in the ferry bank (one line), its price row, and the input restore it sends
N7 = '(7) THE RUNNER ON A RESTORED BUILD, entered as W-ORD-RUNNER-CACHE by [C1].'
ITEMS = {'save': ('ef', N7, '(7) reference+save', 'on'),
         'reference': ('ef', N7, '(7) reference+save', 'off'),
         'restore': ('ef', N7, '(7) restore', 'on')}
AFTER_SAVE = ('reference', 'restore')   # ### each sent only after the save's read shows the build saved to the cache
TARGETS = os.path.join(D, 'b764_targets.json')
REMOTE_HEADS = re.compile(r'^refs/heads/(main|push-b764-[a-z0-9][a-z0-9-]*)$')
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")
CACHE_KEYS = (('input', 'restore input: '), ('key', 'key: '), ('hit', 'restore hit: '), ('files_before', 'files under .lake/build before the build: '),
              ('completed', 'build completed under the hold: '), ('present_before', 'key present before the save: '), ('save', 'save step: '))


def price_rows():
    return dict((r['key'], r) for r in json.load(io.open(PRICE, encoding='utf-8'))['rows'])


def row_caps(pr=None):
    """{price row: its upper dispatch figure} for the rows the items name, read from data/b764_price.json."""
    pr = pr or price_rows()
    return dict((v[2], int(pr[v[2]]['dispatches'][1])) for v in ITEMS.values())


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _epoch(utc):
    return calendar.timegm(time.strptime(utc, '%Y-%m-%dT%H:%M:%SZ'))


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


# ================================================================================ the cache's record, the minutes, the axioms comparison
def cache_record(text):
    """out/cache_kernel.txt read: its seven fields, and restored (the input on, an exact hit, files under .lake/build before the build),
    saved (the build completed, the key not held before the save, the save step succeeded) and from_source (no file under .lake/build before
    the build); read False where a field is missing."""
    f = {}
    for l in (text or '').replace('\r', '').split(NL):
        for k, pre in CACHE_KEYS:
            if l.startswith(pre) and k not in f:
                f[k] = l[len(pre):].strip()
    f['read'] = all(k in f for k, _ in CACHE_KEYS)
    nb = int(f['files_before']) if str(f.get('files_before', '')).isdigit() else -1
    f['restored'] = f['read'] and f['input'] == 'on' and f['hit'] == 'true' and nb > 0
    f['saved'] = f['read'] and f['completed'] == 'true' and f['present_before'] != 'true' and f['save'] == 'success'
    f['from_source'] = f['read'] and nb == 0 and f['hit'] != 'true'
    return f


def build_minutes(text):
    """the build step's minutes from out/build_times.txt (`build start <utc>`, `build end <utc>`), or None."""
    s = re.search(r'^build start (\S+)$', text or '', re.M)
    e = re.search(r'^build end (\S+)$', text or '', re.M)
    try:
        return round((_epoch(e.group(1)) - _epoch(s.group(1))) / 60.0, 1) if s and e else None
    except ValueError:
        return None


def run_minutes(created, updated):
    try:
        return round((_epoch(updated) - _epoch(created)) / 60.0, 1)
    except (ValueError, TypeError):
        return None


def axioms_compare(a, b):
    """two axioms files line for line (carriage returns set aside, the final newline not a line): the lines of each, the positions equal,
    the first line that differs (1-based, or None), and equal (the same lines in the same order, the same count)."""
    la = (a or '').replace('\r', '').rstrip('\n').split(NL) if (a or '').strip() else []
    lb = (b or '').replace('\r', '').rstrip('\n').split(NL) if (b or '').strip() else []
    same = sum(1 for x, y in zip(la, lb) if x == y)
    first = next((i + 1 for i, (x, y) in enumerate(zip(la, lb)) if x != y), None)
    if first is None and len(la) != len(lb):
        first = min(len(la), len(lb)) + 1
    return dict(lines_a=len(la), lines_b=len(lb), equal_positions=same, first_diff=first, equal=bool(la) and la == lb)


def wf_predicates(text):
    """the workflow file's predicates for (7): the third input restore, a choice of off and on, off where absent; the restore step at the input
    on; the key read once from lean-toolchain and lake-manifest.json; the probe, lookup-only; the save where the key is not held; the cache's
    record and the build's times written into out/."""
    t = text or ''
    return dict(
        input_restore=bool(re.search(r'^      restore:\n(?:        .*\n)*?        default: "off"$', t, re.M)) and '          - "off"\n          - "on"' in t,
        restore_step="if: inputs.restore == 'on'\n        uses: actions/cache/restore@v4" in t,
        key_once="hashFiles('lean-toolchain', 'lake-manifest.json')" in t and t.count('hashFiles(') == 1,
        probe='lookup-only: true' in t,
        save_step="uses: actions/cache/save@v4" in t and "steps.probe.outputs.cache-hit != 'true'" in t,
        records='out/cache_kernel.txt' in t and 'out/build_times.txt' in t)


# ================================================================================ the refusals
def dispatch_refusal(k, item, n, rows, read, dk, caps=None):
    """why a dispatch is refused before anything is sent, or None (pure: the rows, the free read, the disk read and the row caps given)."""
    caps = caps if caps is not None else row_caps()
    if k not in KERNELS:
        return 'a kernel this tool does not dispatch in: %r (ef | m24)' % (k,)
    if item not in ITEMS:
        return 'an item (R374)(7) does not order: %r (save | reference | restore)' % (item,)
    if ITEMS[item][0] != k:
        return 'the item %s is %s`s, not %s`s' % (item, KERNELS[ITEMS[item][0]]['key'], KERNELS[k]['key'])
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    cap = KERNELS[k]['cap']
    if not 1 <= n <= cap:
        return 'dispatch %d past the act`s %d in %s ((R374) N1)' % (n, cap, KERNELS[k]['key'])
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == KERNELS[k]['key']]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d in %s rowed already' % (n, KERNELS[k]['key'])
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in %s`s series (%d rowed)' % (n, KERNELS[k]['key'], len(mine))
    if any(r.get('item') == item for r in mine):
        return 'the item %s dispatched already: each of (7)`s three once' % item
    of_row = [r for r in mine if ITEMS.get(r.get('item'), (None, None, None))[2] == ITEMS[item][2]]
    if len(of_row) + 1 > caps.get(ITEMS[item][2], 0):
        return 'the price row %s`s dispatch %d past its upper figure %d ((R374) N1)' % (ITEMS[item][2], len(of_row) + 1, caps.get(ITEMS[item][2], 0))
    if item in AFTER_SAVE:
        sv = [r for r in mine if r.get('item') == 'save']
        rd = [r for r in rows if r.get('kind') == 'read' and sv and int(r.get('run', 0)) == int(sv[0].get('run', -1))]
        if not sv or not rd:
            return 'the %s sent before the save`s read: (7)`s order is the save, read, then the reference and the restore' % item
        if not (rd[0].get('cache') or {}).get('saved'):
            return 'the %s sent where the save`s read shows the build not saved to the cache (%s)' % (item, (rd[0].get('cache') or {}).get('save'))
    return None


def tip_refusal(full, heads):
    """None where `full` is the tip of the remote push-b764-runner, the branch the workflow is dispatched at, so that the run reads that commit's
    workflow file; `heads` [(sha, ref)] from one ls-remote."""
    if not re.match(r'^[0-9a-f]{40}$', full or ''):
        return 'no commit read: %r' % (full,)
    at = [ref for sha, ref in heads if sha == full and ref == 'refs/heads/' + BRANCH]
    return None if at else 'the commit %s is not the remote tip of %s (push it by tools/push_gated.sh --branch first)' % (full[:8], BRANCH)


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


# ================================================================================ the trial's verdict
def trial_verdict(ref, save, rest, ax_ref, ax_rest):
    """(R374)(7)'s verdict from the three read rows (each a dict or None) and the two axioms files: REPRODUCES where the restoring run exits 0
    with its build restored, the reference exits 0 built from source with the restore off, both at the same commit with their axioms print
    run, and the two axioms files are equal line for line; DIFFERS where both exit 0 and the files differ; FAILS otherwise; NOT TRIED where
    no restoring run is read. Its fields: n (the lines equal), m and M (the restoring run's and the reference's minutes), the runs, where."""
    if not rest:
        return dict(verdict='NOT TRIED', where='no restoring run read', n=None, m=None, M=None, runs=[])
    runs = [int(r['run']) for r in (save, ref, rest) if r]
    cmp_ = axioms_compare(ax_ref, ax_rest)
    base = dict(n=cmp_['equal_positions'], m=rest.get('run_min'), M=(ref or {}).get('run_min'), runs=runs, compare=cmp_,
                m_build=rest.get('build_min'), M_build=(ref or {}).get('build_min'))
    where = []
    if not ref:
        where.append('no reference read')
    else:
        if ref.get('build_exit') != '0':
            where.append('the reference`s exit file %s' % ref.get('build_exit'))
        if ref.get('restore_input') != 'off' or not (ref.get('cache') or {}).get('from_source'):
            where.append('the reference not a from-source run with the restore off')
        if not str(ref.get('axioms_print') or '').startswith('RAN'):
            where.append('the reference`s axioms print %s' % ref.get('axioms_print'))
    if rest.get('build_exit') != '0':
        where.append('the restoring run`s exit file %s' % rest.get('build_exit'))
    if not (rest.get('cache') or {}).get('restored'):
        where.append('the restoring run`s build not restored (hit %s, files before the build %s)' % ((rest.get('cache') or {}).get('hit'), (rest.get('cache') or {}).get('files_before')))
    if not str(rest.get('axioms_print') or '').startswith('RAN'):
        where.append('the restoring run`s axioms print %s' % rest.get('axioms_print'))
    if ref and (ref.get('built_ref') != rest.get('built_ref') or not ref.get('built_equal') or not rest.get('built_equal')):
        where.append('the two runs not built at the one dispatched commit')
    if where:
        return dict(base, verdict='FAILS', where='; '.join(where))
    if not cmp_['equal']:
        return dict(base, verdict='DIFFERS', where='the axioms files differ: %d and %d lines, %d positions equal, the first difference at line %s' % (
            cmp_['lines_a'], cmp_['lines_b'], cmp_['equal_positions'], cmp_['first_diff']))
    return dict(base, verdict='REPRODUCES', where='')


def _read_of(rows, item):
    d = [r for r in rows if r.get('kind') == 'dispatch' and r.get('item') == item]
    if not d:
        return None
    rd = [r for r in rows if r.get('kind') == 'read' and int(r.get('run', 0)) == int(d[0]['run'])]
    return rd[0] if rd else None


def trial_now(rows=None):
    rows = rows if rows is not None else _rows()
    ref, save, rest = _read_of(rows, 'reference'), _read_of(rows, 'save'), _read_of(rows, 'restore')
    ax_ref = _f(_art('ef', ref['run']), 'axioms.txt') if ref else ''
    ax_rest = _f(_art('ef', rest['run']), 'axioms.txt') if rest else ''
    return trial_verdict(ref, save, rest, ax_ref, ax_rest)


# ================================================================================ the routes
def cmd_dispatch(k, sha, n, item, *rest):
    rest = list(rest)
    if rest[:1] != ['--targets-json'] or len(rest) != 2:
        sys.exit('### usage: dispatch ef <sha> <n> <item> --targets-json <file> -- the targets from a bank this tool wrote, nothing typed beside it')
    tjson = rest[1]
    read, dk, rows = DR.free(), disk(), _rows()
    why = dispatch_refusal(k, item, int(n), rows, read, dk)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    kd = KERNELS[k]
    slug, owner = remote(k)
    full = git(kd['path'], 'rev-parse', sha).strip()
    tj = json.load(io.open(os.path.join(RELAY, tjson), encoding='utf-8')) if os.path.exists(os.path.join(RELAY, tjson)) else {}
    if tj.get('rev') != full or tj.get('refused') or not tj.get('modules'):
        sys.exit('### NOT DISPATCHED: the targets file %r read rev %s against the commit %s, refused %s, modules %d' % (
            tjson, str(tj.get('rev'))[:8], full[:8], tj.get('refused'), len(tj.get('modules') or [])))
    target = ' '.join(tj['modules'])
    print('  the targets from %s: %d modules, read at %s' % (tjson, len(tj['modules']), tj['rev'][:8]))
    wp = wf_predicates(git(kd['path'], 'show', '%s:%s' % (full, WF)))
    if not all(wp.values()):
        sys.exit('### NOT DISPATCHED: the workflow at %s lacks (7)`s steps: %s' % (full[:8], sorted(x for x, v in wp.items() if not v)))
    heads = [tuple(l.split('\t')) for l in subprocess.run(['git', '-C', kd['path'], 'ls-remote', '--heads', 'origin'], capture_output=True, text=True,
                                                          encoding='utf-8', errors='replace').stdout.split(NL) if '\t' in l]
    why = tip_refusal(full, heads)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    bad = DR.targets_refused(target, module_files(kd['path'], full))
    if bad:
        sys.exit('### NOT DISPATCHED: targets not modules of the tree at %s: %s' % (full[:8], bad))
    try:
        lic = DR.licence(ANSWERS, ITEMS[item][1], by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    mode = ITEMS[item][3]
    print('  %s dispatch %s, %s (restore %s) at %s, the workflow at %s ; the licence %s :%d, committed %s ; free %d MB at %s, the hold %d ; volumes %s, the floor %d' % (
        kd['key'], n, item, mode, full[:8], BRANCH, lic['commit'][:8], lic['line'], lic['committed_at'], read[0], read[1], DR.HOLD, dk, FLOOR))
    at0 = _now()
    cmd = ['gh', 'workflow', 'run', kd['workflow'], '--repo', slug, '--ref', BRANCH, '-f', 'ref=' + full, '-f', 'target=' + target, '-f', 'restore=' + mode]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip())
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel=kd['key'], item=item, n=int(n), sha=full, target=target, at=at0, restore=mode,
                           at_ref=BRANCH, error=mask(r.stderr or '', owner)[:300]))
    else:
        m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
        rid = m.group(1) if m else ''
        for _ in range(8):
            if rid:
                break
            time.sleep(5)
            lst = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', slug, '--workflow', kd['workflow'], '--event', 'workflow_dispatch', '--branch', BRANCH,
                                             '--limit', '5', '--json', 'databaseId,createdAt'], capture_output=True, text=True, encoding='utf-8').stdout or '[]')
            new = sorted((x['createdAt'], x['databaseId']) for x in lst if x['createdAt'] >= at0)
            rid = str(new[0][1]) if new else ''
        if not rid:
            sys.exit('### DISPATCHED, NO RUN ID READ BACK in 40 s -- no row written; read `gh run list` by hand and row it before any other dispatch')
        rows.append(DR.row('dispatch', read, kernel=kd['key'], item=item, n=int(n), workflow=kd['workflow'], at_ref=BRANCH, restore=mode, sha=full,
                           target=target, run=int(rid), at=at0, licence=lic, disk_mb=dk, tree=module_files(kd['path'], full)))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'kernel', 'item', 'n', 'restore', 'sha', 'run', 'free_mb', 'at')))


def _view(k, run):
    slug, owner = remote(k)
    v = subprocess.run(['gh', 'run', 'view', str(run), '--repo', slug, '--json', 'status,conclusion,createdAt,updatedAt,headSha,headBranch,event'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if v.returncode != 0:
        sys.exit('### THE RUN NOT READ: %s' % mask(v.stderr, owner)[:300])
    return json.loads(v.stdout), slug, owner


def cmd_status(k, run):
    v, _s, _o = _view(k, run)
    print('  %s run %s: %s, %s ; created %s ; updated %s ; event %s ; the workflow at %s %s ; minutes so far %s' % (
        KERNELS[k]['key'], run, v['status'], v['conclusion'] or '-', v['createdAt'], v['updatedAt'], v['event'], v['headBranch'], v['headSha'][:8],
        run_minutes(v['createdAt'], v['updatedAt'] if v['status'] == 'completed' else _now())))


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
    art = _art(k, run)
    if not os.path.exists(os.path.join(art, 'build_exit.txt')):
        sys.exit('### NO build_exit.txt IN THE RUN`S FOLDER -- nothing written (download the run first)')
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
    cr = cache_record(_f(art, 'cache_kernel.txt'))
    rows.append(DR.row('read', DR.free(), kernel=KERNELS[k]['key'], n=int(n), run=int(run), item=d[0].get('item'), restore_input=d[0].get('restore'),
                       status=v['status'], conclusion=v['conclusion'], workflow_branch=v['headBranch'], workflow_sha=v['headSha'],
                       workflow_at_dispatched=v['headSha'] == d[0]['sha'] and v['headBranch'] == BRANCH,
                       built_ref=ref[0] if ref else None, built_equal=bool(ref) and ref[0] == d[0]['sha'], toolchain=ref[-1] if len(ref) > 1 else None,
                       build_exit=ex, verdict=verdict, stop=stop[:3], errors=errs[:40], sorry_warnings=len(warn_sorry), targets=len(targets),
                       axiom_lines=ax['lines'], axiom_within=ax['within'], axiom_outside=dict((a, list(b)) for a, b in ax['outside'].items()),
                       axiom_missing=ax['missing'][:60], axiom_missing_n=len(ax['missing']), sorryAx=ax['sorryAx'],
                       axioms_refused=_f(art, 'axioms_refused.txt')[:300], axioms_print=axp,
                       axioms_file_lines=len(axt.replace('\r', '').rstrip('\n').split(NL)) if axt.strip() else 0,
                       axioms_sha256=hashlib.sha256(axt.replace('\r', '').encode('utf-8')).hexdigest(),
                       cache=cr, build_min=build_minutes(_f(art, 'build_times.txt')), run_min=run_minutes(v['createdAt'], v['updatedAt']),
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'],
                       artifact='%s/%s-%s/build-module-%s' % (RUNS_ROLE, k, run, run)))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('kernel', 'n', 'run', 'item', 'restore_input', 'conclusion', 'workflow_at_dispatched', 'built_ref', 'built_equal', 'build_exit',
                                   'verdict', 'sorry_warnings', 'targets', 'axiom_lines', 'axiom_within', 'axiom_missing_n', 'sorryAx', 'axioms_file_lines',
                                   'build_min', 'run_min', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
    print('  THE AXIOMS PRINT: %s ; the file`s sha256 %s' % (axp, r['axioms_sha256'][:16]))
    print('  THE CACHE`S RECORD: %s' % dict((x, cr.get(x)) for x in ('read', 'input', 'hit', 'files_before', 'completed', 'present_before', 'save', 'restored', 'saved', 'from_source')))
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


def cmd_compare(run_a, run_b):
    c = axioms_compare(_f(_art('ef', run_a), 'axioms.txt'), _f(_art('ef', run_b), 'axioms.txt'))
    print('  the axioms files of runs %s and %s: lines %d and %d ; positions equal %d ; the first difference at line %s ; EQUAL LINE FOR LINE %s' % (
        run_a, run_b, c['lines_a'], c['lines_b'], c['equal_positions'], c['first_diff'], c['equal']))


def trial_sentence(t):
    if t['verdict'] == 'REPRODUCES':
        return ('A dispatch of SIDE-explicit-formula on a restored build prints the axioms file of the from-source build at the same commit, %d lines equal, '
                'in %s minutes against %s (runs %s); a tag is cut on a from-source run alone' % (t['n'], t['m'], t['M'], ', '.join(str(x) for x in t['runs'])))
    if t['verdict'] in ('DIFFERS', 'FAILS'):
        return ("A dispatch of SIDE-explicit-formula on a restored build did not reproduce the from-source build: %s; the workflow's change stays on its branch "
                'and main is not moved; builds stay from source' % t['where'])
    return 'NO SENTENCE: the trial not tried (%s)' % t['where']


def cmd_trial():
    t = trial_now()
    print('### THE TRIAL OF (R374)(7): %s ; %s' % (t['verdict'], t['where'] or 'every condition met'))
    print('  fields: n %s ; m %s (build %s) ; M %s (build %s) ; runs %s ; compare %s' % (t['n'], t['m'], t.get('m_build'), t['M'], t.get('M_build'), t['runs'], t.get('compare')))
    print('  THE SENTENCE: ' + trial_sentence(t))


def targets_of(rev):
    """(the full sha, the modules, the names resolved to no one module, the names) of print_targets.txt at rev, each line resolved to the one
    module declaring it by tools/b757_join.py's reader (imported through tools/b758_presend.py, both unchanged)."""
    import b758_presend as P_
    full = P_.J.g('rev-parse', rev).strip()
    t = P_.J.targets_at(full)
    bad = sorted(n for n, v in t.items() if v[0] is None)
    return full, sorted(set(v[0] for v in t.values() if v[0])), bad, len(t)


def cmd_targets(k, rev):
    """data/b764_targets.json: the whole tree's targets at rev for --targets-json; nothing written where a name resolves to no one module or a
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
    pr = price_rows()
    caps = row_caps(pr)
    c('each price row`s cap, its upper dispatch figure (data/b764_price.json)', caps, caps == {'(7) reference+save': 2, '(7) restore': 1})
    kcap = sum(caps.values())
    c('the kernel`s cap (the worklist`s MAX_DISPATCHES) against (7)`s rows` upper figures, and SIDE-dirichlet-mod-24`s 0',
      (K.MAX_DISPATCHES, kcap, K.MAX_DISPATCHES_M24), (K.MAX_DISPATCHES, K.MAX_DISPATCHES_M24) == (kcap, 0) and kcap == 3)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    sv = dict(kind='dispatch', kernel=EF, n=1, item='save', run=11)
    sv_read_ok = dict(kind='read', kernel=EF, run=11, cache=dict(saved=True, save='success'))
    sv_read_no = dict(kind='read', kernel=EF, run=11, cache=dict(saved=False, save='skipped'))
    rf = dict(kind='dispatch', kernel=EF, n=2, item='reference', run=12)
    plants = [('m24', 'save', 1, [], good, dk), ('ef', 'form', 1, [], good, dk), ('ef', 'save', 4, [], good, dk), ('ef', 'save', 2, [], good, dk),
              ('ef', 'save', 1, [], (2000, _now()), dk), ('ef', 'save', 1, [], good, {'C:/': 4000, 'D:/': 20000}), ('SIDE-kernel', 'save', 1, [], good, dk),
              ('ef', 'reference', 1, [dict(kind='dispatch', kernel=EF, n=1, item='restore', run=9)], good, dk),
              ('ef', 'save', 2, [sv, sv_read_ok], good, dk), ('ef', 'reference', 1, [], good, dk), ('ef', 'restore', 2, [sv], good, dk),
              ('ef', 'restore', 2, [sv, sv_read_no], good, dk)]
    got = [dispatch_refusal(*p, caps=caps) for p in plants]
    c('twelve planted dispatches refused (an item in SIDE-dirichlet-mod-24, b763`s item, past the kernel`s cap of 3, out of series, under the hold, '
      'under the floor, a third kernel, rowed already, the save twice, the reference before the save, the restore before the save`s read, the '
      'restore where the save`s read shows nothing saved)', [bool(x) for x in got], all(got))
    passes = [dispatch_refusal('ef', 'save', 1, [], good, dk, caps=caps),
              dispatch_refusal('ef', 'reference', 2, [sv, sv_read_ok], good, dk, caps=caps),
              dispatch_refusal('ef', 'restore', 2, [sv, sv_read_ok], good, dk, caps=caps),
              dispatch_refusal('ef', 'restore', 3, [sv, sv_read_ok, rf], good, dk, caps=caps)]
    c('four planted dispatches taken (the save first ; the reference after the save`s read showing the build saved ; the restore after it ; the '
      'restore third, after the reference)', passes, passes == [None] * 4)
    over = dispatch_refusal('ef', 'reference', 2, [sv, sv_read_ok], good, dk, caps={'(7) reference+save': 1, '(7) restore': 1})
    c('the price row`s cap read: with (7) reference+save planted at 1, the reference after the save refused at the row`s upper figure', over,
      bool(over) and 'upper figure 1' in over)
    lic = {}
    try:
        x = DR.licence(ANSWERS, N7)
        lic = (x['commit'][:8], x['line'])
    except DR.Refused as e:
        lic = str(e)[:60]
    c('(7)`s licence at the committed ferry bank, the commit and the line', lic, isinstance(lic, tuple) and lic[1] == 26)
    try:
        DR.licence(ANSWERS, '(15) A CLAUSE THE RULING DOES NOT HAVE')
        miss = False
    except DR.Refused:
        miss = True
    c('a needle the ferry does not carry refused', miss, miss)
    rm = {}
    for k in ('ef', 'm24'):
        slug, owner = remote(k)
        rm[k] = (mask(slug, owner), bool(owner) and owner not in mask('https://github.com/%s/x/actions/runs/1' % slug, owner))
    c('each kernel`s remote read from its own config, printed masked', rm, all(v[0].startswith('<account>/') and v[1] for v in rm.values()))
    tree = module_files(KERNELS['ef']['path'], K.RUNNER_COMMIT)
    t1 = DR.targets_refused('SIDEExplicitFormula.Schema.Detector', tree)
    t2 = DR.targets_refused('SIDEExplicitFormula.Schema.NoSuchModule', tree)
    t3 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', tree)
    t4 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', DR.tree_files(KERNELS['ef']['path'], K.RUNNER_COMMIT))
    c('targets at the branch tip 38a57e02: a module taken, a name with no file refused, a vendored module under its srcDir taken (refused by the tree '
      'alone)', (t1, len(t2), t3, len(t4)), t1 == [] and len(t2) == 1 and t3 == [] and len(t4) == 1)
    pl = [axioms_print("out/Axioms.lean:1:0: error: import X failed, environment already contains 'Y' from Z", axioms_read("out/Axioms.lean:1:0: error: x", ['a'])),
          axioms_print("NOT RUN: the build did not complete under the hold", axioms_read('', ['a'])),
          axioms_print("'a' depends on axioms: [propext]", axioms_read("'a' depends on axioms: [propext]", ['a']))]
    c('the axioms print`s state on three planted files (an import failure, the NOT RUN line, a clean print)', [x[:24] for x in pl],
      pl[0].startswith('FAILED, NO AXIOMS LINE') and pl[1].startswith('NOT RUN') and pl[2] == 'RAN')
    lic_j = DR.licence(ANSWERS, N7)
    rr = []
    for kw in (dict(tree=module_files(KERNELS['ef']['path'], K.RUNNER_COMMIT)), dict(repo=KERNELS['ef']['path'])):
        try:
            DR.row('dispatch', (5000, _now()), kernel=EF, item='save', n=1, sha=K.RUNNER_COMMIT, target='Lc.LiCriterion.ReverseDirection', run=1, at=_now(),
                   licence=lic_j, **kw)
            rr.append(None)
        except DR.Refused as e:
            rr.append(str(e)[:60])
    c('the row`s own target check on a planted dispatch row of the vendored module: given the srcDir-aware list, taken ; given the kernel`s '
      'folder alone, refused', rr, rr[0] is None and bool(rr[1]))
    heads = [('a' * 40, 'refs/heads/' + BRANCH), ('b' * 40, 'refs/heads/push-b764-other'), ('c' * 40, 'refs/heads/main'), ('e' * 40, 'refs/heads/push-b763-form')]
    tp = (tip_refusal('a' * 40, heads), bool(tip_refusal('b' * 40, heads)), bool(tip_refusal('c' * 40, heads)), bool(tip_refusal('d' * 40, heads)),
          bool(tip_refusal('', heads)), bool(tip_refusal('e' * 40, heads)))
    c('the remote tip: push-b764-runner`s tip taken ; another push-b764-* branch`s refused ; main`s refused (the run must read the branch`s '
      'workflow) ; no tip refused ; no commit refused ; b763`s push branch refused', tp, tp == (None, True, True, True, True, True))
    tf, tm, tb, tn = targets_of(K.EF_BASE_B763)
    bj = json.load(io.open(os.path.join(D, 'b759_targets.json'), encoding='utf-8'))
    c('THE POSITIVE CONTROL: the targets reader at a3aad4cc against b759`s targets bank (data/b759_targets.json: %d modules for %d names, '
      '%d refused)' % (len(bj['modules']), bj['names'], len(bj['refused']) if isinstance(bj['refused'], list) else bj['refused']),
      (tf[:8], len(tm), tn, len(tb)), tf == bj['rev'] and tm == sorted(bj['modules']) and tn == bj['names'] and not tb)
    wn = wf_predicates(git(KERNELS['ef']['path'], 'show', '%s:%s' % (K.RUNNER_COMMIT, WF)))
    wo = wf_predicates(git(KERNELS['ef']['path'], 'show', '%s:%s' % (K.EF_BASE, WF)))
    c('the workflow`s predicates for (7): each true at the branch tip 38a57e02 ; THE PLANTED FAULT, main`s workflow at 819e4a83, each false',
      (sum(wn.values()), len(wn), sum(wo.values())), all(wn.values()) and not any(wo.values()))
    recs = [cache_record('restore input: on\nkey: kernel-build-x\nrestore hit: none\nfiles under .lake/build before the build: 0\n'
                         'build completed under the hold: true\nkey present before the save: none\nsave step: success\n'),
            cache_record('restore input: on\nkey: kernel-build-x\nrestore hit: true\nfiles under .lake/build before the build: 4120\n'
                         'build completed under the hold: true\nkey present before the save: true\nsave step: skipped\n'),
            cache_record('restore input: off\nkey: kernel-build-x\nrestore hit: none\nfiles under .lake/build before the build: 0\n'
                         'build completed under the hold: true\nkey present before the save: true\nsave step: skipped\n'),
            cache_record('restore input: on\nkey: kernel-build-x\nrestore hit: true\n')]
    rv = [(r['read'], r['restored'], r['saved'], r['from_source']) for r in recs]
    c('the cache`s record on four planted files (the save run, the restoring run, the reference, a record cut short): (read, restored, saved, '
      'from source)', rv, rv == [(True, False, True, True), (True, True, False, False), (True, False, False, True), (False, False, False, False)])
    ax3 = "'a' depends on axioms: [propext]\n'b' does not depend on any axioms\n'c' depends on axioms: [propext, Quot.sound]\n"
    cm = [axioms_compare(ax3, ax3), axioms_compare(ax3, ax3.replace("'b' does not depend on any axioms", "'b' depends on axioms: [propext]")),
          axioms_compare(ax3, ax3.rsplit("'c'", 1)[0]), axioms_compare('', '')]
    c('the axioms comparison on four planted pairs (equal ; line 2 differing ; one line short ; both empty): (positions equal, first difference, equal)',
      [(x['equal_positions'], x['first_diff'], x['equal']) for x in cm],
      [(x['equal_positions'], x['first_diff'], x['equal']) for x in cm] == [(3, None, True), (2, 2, False), (2, 3, False), (0, None, False)])
    mn = (build_minutes('build start 2026-11-20T22:00:00Z\nbuild end 2026-11-20T23:33:30Z\n'), build_minutes('build start 2026-11-20T22:00:00Z\n'),
          run_minutes('2026-11-20T22:00:00Z', '2026-11-20T22:12:06Z'))
    c('the minutes on planted times (a build of 93.5 min ; a build with no end ; a run of 12.1 min)', mn, mn == (93.5, None, 12.1))
    base = dict(build_exit='0', axioms_print='RAN', built_ref='a' * 40, built_equal=True)
    p_ref = dict(base, run=2, restore_input='off', cache=recs[2], run_min=95.0, build_min=80.0)
    p_sav = dict(base, run=1, restore_input='on', cache=recs[0], run_min=99.0, build_min=82.0)
    p_rst = dict(base, run=3, restore_input='on', cache=recs[1], run_min=11.0, build_min=1.5)
    tv = [trial_verdict(p_ref, p_sav, p_rst, ax3, ax3), trial_verdict(p_ref, p_sav, p_rst, ax3, ax3.replace("[propext]", "[propext, sorryAx]", 1)),
          trial_verdict(p_ref, p_sav, dict(p_rst, build_exit='1'), ax3, ax3), trial_verdict(p_ref, p_sav, dict(p_rst, cache=recs[0]), ax3, ax3),
          trial_verdict(p_ref, p_sav, None, ax3, '')]
    c('the trial`s verdict on five planted readings (all met ; the axioms differing ; the restoring run exiting 1 ; its build not restored ; no '
      'restoring run read)', [t['verdict'] for t in tv],
      [t['verdict'] for t in tv] == ['REPRODUCES', 'DIFFERS', 'FAILS', 'FAILS', 'NOT TRIED'] and tv[0]['n'] == 3 and (tv[0]['m'], tv[0]['M']) == (11.0, 95.0)
      and tv[0]['runs'] == [1, 2, 3] and 'not restored' in tv[3]['where'])
    c('the sentence of REPRODUCES with its fields filled, and of DIFFERS', (trial_sentence(tv[0])[:60], trial_sentence(tv[1])[-60:]),
      trial_sentence(tv[0]).endswith('3 lines equal, in 11.0 minutes against 95.0 (runs 1, 2, 3); a tag is cut on a from-source run alone')
      and 'did not reproduce the from-source build: the axioms files differ' in trial_sentence(tv[1]) and trial_sentence(tv[1]).endswith('builds stay from source'))
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b764_controls.py`s OWN CONTROLS, (R374)(7), BEFORE ITS OPENING DISPATCH (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R374)(7): THE RUNNER ON A RESTORED BUILD, THE DISPATCHES AND THE READS, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    for k in ('ef', 'm24'):
        kd = KERNELS[k]
        disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == kd['key']]
        reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == kd['key'])
        refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == kd['key']]
        out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (kd['key'], len(disp), kd['cap'], len(refused)))
        for r in disp:
            rd = reads.get(int(r['run']), {})
            cr = rd.get('cache') or {}
            out.append('  %d | %-9s | restore %s | sha %s at %s | run %s | free %d MB | licence %s :%s | %s, exit %s, built %s, the workflow at the dispatched commit %s, '
                       '%d errors, sorry warnings %s, targets %s, axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, axioms file %s lines sha256 %s, '
                       'runner low %s MB, minutes %s (build %s)' % (
                           r['n'], r['item'], r.get('restore'), r['sha'][:8], r.get('at_ref'), r['run'], r['free_mb'], r['licence']['commit'][:8], r['licence']['line'],
                           rd.get('verdict', 'UNREAD'), rd.get('build_exit'), rd.get('built_equal'), rd.get('workflow_at_dispatched'), len(rd.get('errors') or []),
                           rd.get('sorry_warnings'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}),
                           rd.get('axiom_missing_n'), rd.get('sorryAx'), rd.get('axioms_file_lines'), str(rd.get('axioms_sha256'))[:16], rd.get('runner_low_mb'),
                           rd.get('run_min'), rd.get('build_min')))
            if rd:
                out.append('      the axioms print: %s ; the cache`s record: input %s, hit %s, files before the build %s, completed %s, key present before the save %s, '
                           'save %s -> restored %s, saved %s, from source %s' % (rd.get('axioms_print'), cr.get('input'), cr.get('hit'), cr.get('files_before'),
                                                                                cr.get('completed'), cr.get('present_before'), cr.get('save'), cr.get('restored'),
                                                                                cr.get('saved'), cr.get('from_source')))
        out.append('')
    t = trial_now(rows)
    out.append('## THE TRIAL OF (R374)(7)')
    out.append('  the verdict: %s ; %s' % (t['verdict'], t['where'] or 'every condition met'))
    out.append('  the fields: lines equal %s ; the restoring run`s minutes %s (its build %s) ; the reference`s %s (its build %s) ; runs %s ; the comparison %s' % (
        t['n'], t['m'], t.get('m_build'), t['M'], t.get('M_build'), t['runs'], t.get('compare')))
    out.append('  THE SENTENCE: ' + trial_sentence(t))
    out.append('')
    nd = sum(1 for r in rows if r.get('kind') == 'dispatch')
    nk = sum(1 for r in rows if r.get('kind') == 'read' and r.get('verdict') == 'KERNEL')
    out.append('### ### **DISPATCHES %d (SIDE-explicit-formula %d OF %d, SIDE-dirichlet-mod-24 %d OF %d) ; READ KERNEL (THE BUILD EXITING 0) %d ; THE TRIAL %s ; '
               'THE TOOL`S CONTROLS %d OF %d.**' % (
                   nd, sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF), K.MAX_DISPATCHES,
                   sum(1 for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == M24), K.MAX_DISPATCHES_M24, nk, t['verdict'], sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b764_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'targets': cmd_targets, 'dispatch': cmd_dispatch, 'status': cmd_status, 'download': cmd_download, 'read': cmd_read,
          'errors': cmd_errors, 'axioms': cmd_axioms, 'compare': cmd_compare, 'trial': cmd_trial, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
