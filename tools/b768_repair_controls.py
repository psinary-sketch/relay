# -*- coding: utf-8 -*-
"""b768, (R378)(8): THE PLANTED CONTROLS OF THE THREE KEYS, [K26], [K27] and [K28], in the form of tools/b767_repair_controls.py (its frame
carried: git, snapshot, probe, version_of, main; [K25]'s probe set to the kernel route for b768). Each key's control is added to this tool
and committed before its first run. The control reads the fault at the commit before the repair and reads clean at the repair's commit,
both printed. Read-only over the relay: each revision's files are taken by `git show <rev>:<path>` into a scratch folder of the system's
temporary directory (removed after), and each revision is probed in its own interpreter (`python -I`), so no module of one revision is
read by the other; the probe executes the standing tool's pure tables and functions apart, runs no git command (the [K27] probe stubs the
cadence's two git readers) and prints one JSON line; it writes nothing outside its own snapshot folder ([K27]'s probe writes the banks of a
held part, and [K28]'s a planted send's mark, into that folder alone, removed with it). --bank appends the reading to data/b768_repair_controls.txt beneath a head naming the
key and both commits; nothing else is written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b768_repair_controls.py <K26|K27|K28> <before> <after> [--bank]
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = '\n'
ACT = 'b768'
BANK = os.path.join(D, 'b768_repair_controls.txt')


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def snapshot(rev, paths, dest):
    """the files `paths` at `rev` under dest, at their relay paths; [(path, present)]."""
    out = []
    for p in paths:
        rc, b = git('show', '%s:%s' % (rev, p))
        out.append((p, rc == 0))
        if rc == 0:
            q = os.path.join(dest, *p.split('/'))
            os.makedirs(os.path.dirname(q), exist_ok=True)
            with open(q, 'wb') as fh:
                fh.write(b)
    return out


def probe(code, snap, *args):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', code, snap] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    lines = [l for l in r.stdout.split(NL) if l.startswith('{')]
    if r.returncode != 0 or not lines:
        return dict(error='exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[-400:]))
    return json.loads(lines[-1])


def version_of(tmp):
    vp = os.path.join(tmp, 'tools', 'standing', 'VERSION')
    return io.open(vp, encoding='utf-8').read().strip() if os.path.exists(vp) else None


def two_revisions(paths, before, after, code, prefix):
    """[(name, rev, files, probe's json, VERSION)] for BEFORE and AFTER, each snapshot removed after its probe."""
    out = []
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix=prefix)
        try:
            got = snapshot(rev, paths, tmp)
            j = probe(code, tmp)
            ver = version_of(tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith(prefix):
                shutil.rmtree(tmp, ignore_errors=True)
        out.append((name, rev, got, j, ver))
    return out


# ================================================================================ [K26] THE KERNEL ROUTE FOR b768
K26_PATHS = ('tools/standing/commit.py', 'tools/standing/VERSION')
K26_VERSION = 'v1.38.26'
K26_PROBE = r'''
import ast, json, os, re, sys
snap = sys.argv[1]
src = open(os.path.join(snap, 'tools', 'standing', 'commit.py'), encoding='utf-8').read()
want = ('KERNELS', 'KERNEL_ACTS', 'NAMED_CONFLICTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'FORCED_DELETES', 'Refused', 'repo_refusal',
        'push_branch_ok', 'kernel_branch_refusal', 'merge_branch_refusal', 'conflict_refusal', 'ff_refusal', 'pushto_refusal',
        'pushto_name_refusal', 'rdelete_refusal', 'forced_name', 'kernel_delete_args')
tree = ast.parse(src)
nodes = [n for n in tree.body if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in want)
         or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
ns = dict(re=re)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'commit_k26', 'exec'), ns)
ns.setdefault('FORCED_DELETES', {})
EF, M24, THIRD = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24', 'SIDE-frobenius'
OWN, KEPT, KEPT2 = 'push-b768-proof', 'push-b767-proof', 'push-b766-proof'
none = lambda v: v is None


def dl(key, act, name, held, table=None):
    f = ns['kernel_delete_args']
    bad, a = f(key, act, name, held) if table is None else f(key, act, name, held, table=table)
    return 'REFUSED' if bad else ' '.join(a[:2])


planted = {'b768': {EF: (KEPT,)}}   # ### the planted name: FORCED_DELETES given push-b767-proof for b768, which RDELETE_ACTS does not name
out = dict(
    open=none(ns['repo_refusal'](EF, 'b768')),
    ff=none(ns['ff_refusal'](EF, 'b768')),
    second=[none(ns['repo_refusal'](M24, 'b768')), none(ns['ff_refusal'](M24, 'b768'))],   # ### the planted second kernel's name
    third=[none(ns['repo_refusal'](THIRD, 'b768')), none(ns['ff_refusal'](THIRD, 'b768'))],
    b767=[none(ns['repo_refusal'](EF, 'b767')), none(ns['ff_refusal'](EF, 'b767')), none(ns['repo_refusal'](M24, 'b767'))],
    other=[none(ns['repo_refusal'](EF, 'b769')), none(ns['ff_refusal'](EF, 'b769'))],
    branch=[none(ns['kernel_branch_refusal']('b768', OWN)), none(ns['merge_branch_refusal']('b768', OWN)),
            none(ns['kernel_branch_refusal']('b768', 'main')), none(ns['merge_branch_refusal']('b768', 'main')),
            none(ns['kernel_branch_refusal']('b768', KEPT)), none(ns['merge_branch_refusal']('b768', KEPT))],
    named=none(ns['conflict_refusal']('b768', EF, ['print_targets.txt'])),
    pushto=none(ns['pushto_refusal'](EF, 'b768')),
    rdel=[none(ns['rdelete_refusal'](EF, 'b768', KEPT, kept=())), none(ns['rdelete_refusal'](EF, 'b768', KEPT2, kept=())),
          none(ns['rdelete_refusal'](EF, 'b768', OWN, kept=())), none(ns['rdelete_refusal'](M24, 'b768', KEPT, kept=()))],
    dele=[dl(EF, 'b768', OWN, False), dl(EF, 'b768', OWN, True), dl(EF, 'b768', KEPT, False), dl(EF, 'b768', KEPT, True),
          dl(EF, 'b768', KEPT, False, table=planted), dl(EF, 'b768', 'main', False)],
    rows=dict((t, sorted(ns[t])) for t in ('KERNEL_ACTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'NAMED_CONFLICTS', 'FORCED_DELETES')),
    b768_rows=dict((t, list(ns[t].get('b768', ()))) for t in ('KERNEL_ACTS', 'FF_ACTS')),
    b768_named=dict((t, dict((k, list(v)) for k, v in (ns[t].get('b768') or {}).items())) for t in ('RDELETE_ACTS', 'FORCED_DELETES')))
print(json.dumps(out))
'''


def control_k26(before, after):
    """(R378)(8) [K26]: the kernel route opened for b768 at SIDE-explicit-formula, read in each revision by commit.py's pure tables and
    functions (executed apart, nothing written, no git command run). FAULT: repo_refusal and ff_refusal refuse SIDE-explicit-formula for
    b768. CLEAN: b768 opened at SIDE-explicit-formula in both tables; the planted second kernel's name, SIDE-dirichlet-mod-24, refused in
    both, and a third name refused; b767's opening unmoved; b769 refused; push-b768-proof admitted as the act's branch and as HEAD for a
    commit; main and push-b767-proof refused as both; no conflicted merge named; no push to a named branch; RDELETE_ACTS naming nothing
    for b768, so the removal at the remote refuses push-b767-proof, push-b766-proof, the act's own branch and the kernel beside; the local
    delete takes push-b768-proof with -d unmerged and -D held, and refuses push-b767-proof unmerged, held, and with it planted in
    FORCED_DELETES (RDELETE_ACTS governing), and main; the only rows added b768's in KERNEL_ACTS and FF_ACTS; VERSION v1.38.26."""
    L, res, rows = [], {}, {}
    for name, rev, got, j, ver in two_revisions(K26_PATHS, before, after, K26_PROBE, 'b768k26_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        nn = lambda v: 'None' if v else 'REFUSED'
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (open)   repo_refusal(SIDE-explicit-formula, b768) %s ; (ff) ff_refusal %s' % (nn(j['open']), nn(j['ff'])))
        L.append('    (second) the planted second kernel`s name, SIDE-dirichlet-mod-24, for b768: repo %s, ff %s' % tuple(nn(v) for v in j['second']))
        L.append('    (third)  SIDE-frobenius for b768: repo %s, ff %s' % tuple(nn(v) for v in j['third']))
        L.append('    (b767)   SIDE-explicit-formula repo %s, ff %s ; SIDE-dirichlet-mod-24 repo %s' % tuple(nn(v) for v in j['b767']))
        L.append('    (other)  SIDE-explicit-formula for b769: repo %s, ff %s' % tuple(nn(v) for v in j['other']))
        L.append('    (branch) push-b768-proof as branch %s, as HEAD for a commit %s ; main as branch %s, as HEAD %s ; push-b767-proof as branch %s, '
                 'as HEAD %s' % tuple(nn(v) for v in j['branch']))
        L.append('    (named)  print_targets.txt in a conflicted merge for b768: %s ; (pushto) %s' % (nn(j['named']), nn(j['pushto'])))
        L.append('    (rdelete) push-b767-proof %s ; push-b766-proof %s ; push-b768-proof %s ; push-b767-proof at SIDE-dirichlet-mod-24 %s'
                 % tuple(nn(v) for v in j['rdel']))
        L.append('    (delete) push-b768-proof unmerged %s, held %s ; push-b767-proof unmerged %s, held %s, PLANTED in FORCED_DELETES %s ; main %s'
                 % tuple(j['dele']))
        L.append('    (rows)   %s' % ' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['rows'].items())))
        L.append('    (b768)   %s ; %s' % (' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['b768_rows'].items())),
                                           ' ; '.join('%s %s' % (t, json.dumps(v, sort_keys=True)) for t, v in sorted(j['b768_named'].items()))))
        fault = not j['open'] and not j['ff']
        clean = (j['open'] and j['ff'] and not any(j['second']) and not any(j['third']) and j['b767'] == [True, True, False]
                 and not any(j['other']) and j['branch'] == [True, True, False, False, False, False] and not j['named'] and not j['pushto']
                 and not any(j['rdel'])
                 and j['dele'] == ['branch -d', 'branch -D', 'REFUSED', 'REFUSED', 'REFUSED', 'REFUSED']
                 and j['b768_rows'] == {'KERNEL_ACTS': ['SIDE-explicit-formula'], 'FF_ACTS': ['SIDE-explicit-formula']}
                 and j['b768_named'] == {'RDELETE_ACTS': {}, 'FORCED_DELETES': {}}
                 and 'b768' not in j['rows']['PUSHTO_ACTS'] and 'b768' not in j['rows']['NAMED_CONFLICTS'] and ver == K26_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
        rows[name] = j['rows']
    diff_ok = None
    if 'BEFORE' in rows and 'AFTER' in rows:
        moved = dict((t, (sorted(set(rows['AFTER'][t]) - set(rows['BEFORE'][t])), sorted(set(rows['BEFORE'][t]) - set(rows['AFTER'][t]))))
                     for t in sorted(rows['AFTER']))
        want = ('KERNEL_ACTS', 'FF_ACTS')
        diff_ok = all(moved[t] == ((['b768'], []) if t in want else ([], [])) for t in moved)
        L.append('  (diff)   the acts each table gains and loses, BEFORE to AFTER: %s -- %s' % (
            ' ; '.join('%s +%s -%s' % (t, ','.join(a) or 'none', ','.join(r) or 'none') for t, (a, r) in sorted(moved.items())),
            'b768 GAINED BY KERNEL_ACTS AND FF_ACTS ALONE' if diff_ok else 'ANOTHER ROW MOVED'))
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and diff_ok is True


# ================================================================================ [K27] THE CLOSE OF AN ACT THAT WRITES LEAN AND NO PAPER
K27_PATHS = ('tools/standing/cadence.py', 'tools/standing/prevdry.py', 'tools/standing/close.py', 'tools/standing/fold/checks.tpl',
             'tools/standing/VERSION', 'data/b768_wlist.json')   # ### tools/standing/ holds no __init__.py: a namespace package, read so in the probe
K27_VERSION = 'v1.38.27'
LEAN, PAPER = 'LEAN AND NO PAPER', 'PAPER'
QUARTERS = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d')
K27_PROBE = r'''
import ast, json, os, re, sys, types
snap = sys.argv[1]
sys.path.insert(0, os.path.join(snap, 'tools'))
sys.path.insert(1, os.path.join(snap, 'tools', 'standing'))
import standing
fake_l = types.ModuleType('standing.lsrread')
fake_l.verdict = lambda a, b: ('CLASSED', [])
def _exn(act, part, mode, tracked):
    if mode == 'prev':
        return '%s_prevrun_exercise_%s.json' % (act, part)
    if mode == 'mid':
        return '%s_mid_exercise_%s.json' % (act, part)
    n = '%s_exercise_%s.json' % (act, part)
    return '%s_exercise_%s_%s.json' % (act, part, act) if mode == 'prerun' and tracked(n) else n
fake_r = types.ModuleType('standing.repeat')
fake_r.exercise_name = _exn
sys.modules['standing.lsrread'], sys.modules['standing.repeat'] = fake_l, fake_r
standing.lsrread, standing.repeat = fake_l, fake_r
from standing import cadence as C
C._git = lambda *a: None
C._blob = lambda *a: None
QUARTERS = ('standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d')
MODES = ('prerun', 'prev', 'post-push', 'pre-push', 'mid', 'rerun')
wl = json.load(open(os.path.join(snap, 'data', 'b768_wlist.json'), encoding='utf-8'))['patterns']
has_kind = hasattr(C, 'kind_of')
out = dict(has_kind=has_kind)
PLANTS = dict(day1=wl + ['PLACE-papers/day1/A_Place_to_Stand.md'], glob=wl + ['PLACE-papers/*'],
              phase15=wl + ['PLACE-papers/phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'],
              nokernel=[p for p in wl if not p.startswith('SIDE-')], empty=[])
pk = None
if has_kind:
    kd = lambda patterns=None, act='b768': C.kind_of(act, snap, patterns=patterns)['kind']
    out['kinds'] = dict(b768=kd(), b767=kd(act='b767'), b769=kd(act='b769'), **dict((k, kd(v)) for k, v in PLANTS.items()))
    pk = C.kind_of('b768', snap, patterns=PLANTS['day1'])
def dec(part, mode, kind=None):
    if kind is None:
        return C.decide('b768', part, mode, snap, {})
    return C.decide('b768', part, mode, snap, {}, kind=kind)
out['four'] = dict(('%s %s' % (p, m), dec(p, m)['held']) for p in QUARTERS for m in MODES)
out['b3_post_together'] = 'together' in dec('standing-b3', 'post-push')['why']
if pk is not None:
    out['planted_four'] = dict(('%s %s' % (p, m), dec(p, m, pk)['held']) for p in QUARTERS for m in MODES)
    out['planted_b3_together'] = 'together' in dec('standing-b3', 'post-push', pk)['why']
import prevdry as PD
PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1') + QUARTERS + ('standing-b3', 'act')
def gate_read(kind=None):
    clear, L = PD.gate('b768', parts=PARTS) if kind is None else PD.gate('b768', parts=PARTS, kind=kind)
    got = {}
    for q in PARTS:
        ln = next((l for l in L if l.startswith('    %-14s' % q)), '')
        got[q] = 'HELD' if 'HELD, NOT RUN AT THIS ACT' in ln else ('ABSENT' if 'NOT RUN (data/' in ln else ln.strip()[:60])
    return got
out['gate'] = gate_read()
if pk is not None:
    out['planted_gate'] = gate_read(pk)
dd = os.path.join(snap, 'heldprobe')
os.makedirs(dd)
banks = {}
for part, mode, text in (('standing-b2a', 'pre-push', 'b768_checks_standing-b2a.txt'), ('standing-b2b', 'prerun', 'b768_arms_prerun_standing-b2b.txt'),
                         ('standing-b2c', 'mid', 'b768_checks_mid_standing-b2c.txt'), ('standing-b2d', 'prev', 'b768_prevrun_standing-b2d.txt')):
    d = dec(part, mode)
    if d['run']:
        banks[part] = 'RUNS'
        continue
    seen = set(os.listdir(dd))
    C.held(d, 'b768', snap, dd, text=text, ex_mode=mode, out=lambda *a: None)
    new = sorted(set(os.listdir(dd)) - seen)
    exn = [n for n in new if 'exercise' in n]
    ex = json.load(open(os.path.join(dd, exn[0]), encoding='utf-8')) if len(exn) == 1 else {}
    t = open(os.path.join(dd, text), encoding='utf-8').read() if text in new else ''
    banks[part] = dict(files=new, ex_mode=ex.get('mode'), run=ex.get('run'), foot=('ARMS 0 ;' in t and 'DECLARED EQ RUN NOTRUN' in t),
                       kind=(ex.get('cadence') or {}).get('kind'))
out['held'] = banks
src = open(os.path.join(snap, 'tools', 'standing', 'close.py'), encoding='utf-8').read()
nodes = [n for n in ast.parse(src).body if (isinstance(n, ast.FunctionDef) and n.name == 'part_declared')
         or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'PART_FOOT')]
ns = dict(re=re)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'close_k27', 'exec'), ns)
foot = '  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING 0 NONE ; NEGATIVE-CONTROL FAILURES 0 ; POSITIVE-CONTROL PASSES 0 NONE ; DECLARED EQ RUN %s ; 3 s'
if 'part_declared' in ns:
    out['declared'] = [bool(ns['part_declared'](ns['PART_FOOT'].search(foot % (p, n, n, v)))) for p, n, v in
                       (('standing-b2a', 0, 'NOTRUN'), ('standing-b2a', 3, 'NOTRUN'), ('act', 5, 'True'), ('act', 5, 'False'))]
tpl = open(os.path.join(snap, 'tools', 'standing', 'fold', 'checks.tpl'), encoding='utf-8').read()
out['tpl'] = dict(guard=tpl.count("_CAD.chain_quarters_run('⟪ACT⟫', ROOT)"), quarters=tpl.count("ha.get('quarters', True)"),
                  declared=tpl.count('STC.part_declared('), names=tpl.count('text=_part_name(base, PART)'))
i = tpl.index('def verify_ok(S):')
j = tpl.index('\ndef ', i + 1)
H = 'h' * 40
g = dict(gs=lambda *a: H, ROOT='R', ACT_NOW='b768',
         AC=types.SimpleNamespace(act_figures=lambda dd=None, roots_text=None, act=None: dict(range=list(range(624, 769)), range_last=768)),
         KS=types.SimpleNamespace(CHAIN_HALVES=(('b624', 'b658'), ('b659', 'b768'))))
exec(compile(tpl[i:j], 'verify_k27', 'exec'), g)
second = [('b%d' % k, 'AGREE', []) for k in range(659, 769)]
reads = {'b768': {'crlf': 0}, 'b680': {'corrected': 4}}
lean = dict(half_a=dict(head=H, acts=[], reads={}, boundary={}, quarters=False), ar_verify=second, ar_reads=reads, boundary=dict(equal=True, root='r1'))
paper = dict(half_a=dict(head=H, acts=[['b%d' % k, 'AGREE'] for k in range(624, 659)], reads={}, boundary=dict(equal=True, root='r1')),
             ar_verify=second, ar_reads=reads, boundary=dict(equal=True, root='r1'))
out['verify'] = dict(lean=bool(g['verify_ok'](lean)), paper=bool(g['verify_ok'](paper)), lean_neg=bool(g['verify_ok'](dict(lean, ar_verify=second[:-1]))),
                     lean_unequal=bool(g['verify_ok'](dict(lean, boundary=dict(equal=False, root='r1')))))
print(json.dumps(out))
'''
K27_HELD = {
    'standing-b2a': dict(files=['b768_checks_standing-b2a.txt', 'b768_exercise_standing-b2a.json', 'b768_lsr_standing-b2a.json'], ex_mode='pre-push'),
    'standing-b2b': dict(files=['b768_arm_seconds_standing-b2b.json', 'b768_arms_prerun_standing-b2b.txt', 'b768_exercise_standing-b2b.json',
                                'b768_lsr_prerun_standing-b2b.json'], ex_mode='prerun'),
    'standing-b2c': dict(files=['b768_checks_mid_standing-b2c.txt', 'b768_lsr_mid_standing-b2c.json', 'b768_mid_exercise_standing-b2c.json'], ex_mode='mid'),
    'standing-b2d': dict(files=['b768_prevrun_exercise_standing-b2d.json', 'b768_prevrun_standing-b2d.json', 'b768_prevrun_standing-b2d.txt'], ex_mode='prev')}


def control_k27(before, after):
    """(R378)(8) [K27]: the kind of an act that writes Lean and no paper, read in each revision in its own interpreter with git stubbed (no git
    command run; the held part's banks written into the probe's own snapshot folder alone, removed with it). FAULT: no kind, and b768's four
    chain parts standing-b2a to standing-b2d required (run) in the pre-push mode; G-ACTROOT-VERIFY's predicate refuses standing-b3's half
    alone; no reader of a NOTRUN footer. CLEAN: b768 of the kind LEAN AND NO PAPER from its (W) list; the planted acts of the other kind
    (a paper's path under day1/ or phase1.5/, a glob reaching one, a list with no kernel's files, an empty list), b767 (before the key) and
    an act whose list is not read each PAPER; b768's four NOT RUN in every mode of the suite, prerun, prev, post-push, pre-push, mid and
    rerun, and the planted act's four required in every mode; standing-b3's post-push group reduced to itself at b768 and the chain group
    whole at the planted act; the prev-mode dry's gate (the lock gate's read) holding the four at b768 and requiring them at the planted
    act, the other six parts read as before; held() writing each not-run part's banks under the mode's own names (pre-push, prerun, mid,
    prev), ARMS 0 and NOTRUN in the footer, the kind in the exercise bank; a NOTRUN footer of 0 arms read as declared and one of 3 arms not;
    the template carrying the kind at the b3 join, the arm's predicate, the held call and the combine; the predicate passing b768's second
    half with the boundary, a whole chain as before, and failing a dropped act or an unequal boundary; VERSION v1.38.27."""
    L, res = [], {}
    for name, rev, got, j, ver in two_revisions(K27_PATHS, before, after, K27_PROBE, 'b768k27_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (kind)    %s' % (' ; '.join('%s %s' % kv for kv in sorted(j['kinds'].items())) if j.get('has_kind') else 'NO KIND IN cadence.py'))
        fv = sorted(set(j['four'].values()))
        L.append('    (four)    b768`s standing-b2a to standing-b2d in the modes prerun, prev, post-push, pre-push, mid, rerun: %s ; pre-push %s' % (
            ', '.join(fv), ', '.join(j['four']['%s pre-push' % p] for p in QUARTERS)))
        if 'planted_four' in j:
            L.append('    (planted) the planted act of the other kind (a paper`s path under day1/), its four in the six modes: %s ; standing-b3`s '
                     'post-push group whole %s' % (', '.join(sorted(set(j['planted_four'].values()))), j['planted_b3_together']))
        L.append('    (b3)      b768`s standing-b3 in the post-push mode read with the chain group: %s' % j['b3_post_together'])
        L.append('    (gate)    the prev-mode dry`s gate at b768: %s' % ' ; '.join('%s %s' % (q, j['gate'][q]) for q in sorted(j['gate'])))
        if 'planted_gate' in j:
            L.append('    (gate)    at the planted act: the four %s' % ', '.join(j['planted_gate'][q] for q in QUARTERS))
        for p in QUARTERS:
            h = j['held'].get(p)
            L.append('    (held)    %s: %s' % (p, h if isinstance(h, str) else 'files %s ; exercise mode %s ; run %s ; footer ARMS 0 and NOTRUN %s ; kind %s' % (
                ', '.join(h['files']), h['ex_mode'], h['run'], h['foot'], h['kind'])))
        L.append('    (declared) a NOTRUN footer of 0 arms, of 3 arms, a True footer, a False footer: %s' % (j['declared'] if 'declared' in j else 'NO part_declared IN close.py'))
        L.append('    (tpl)     the kind at the b3 join %d, the predicate`s quarters %d, the combine`s declared %d, the held call`s names %d' % (
            j['tpl']['guard'], j['tpl']['quarters'], j['tpl']['declared'], j['tpl']['names']))
        L.append('    (verify)  G-ACTROOT-VERIFY`s predicate: b768`s second half with the boundary %s ; a whole chain %s ; an act dropped %s ; the '
                 'boundary unequal %s' % (j['verify']['lean'], j['verify']['paper'], j['verify']['lean_neg'], j['verify']['lean_unequal']))
        fault = (not j.get('has_kind') and all(j['four']['%s pre-push' % p] == 'run' for p in QUARTERS) and j['verify']['lean'] is False
                 and 'declared' not in j)
        held_ok = all(isinstance(j['held'].get(p), dict) and j['held'][p]['files'] == K27_HELD[p]['files'] and j['held'][p]['ex_mode'] == K27_HELD[p]['ex_mode']
                      and j['held'][p]['run'] == 0 and j['held'][p]['foot'] is True and j['held'][p]['kind'] == LEAN for p in QUARTERS)
        clean = (j.get('has_kind') and j['kinds'] == dict(b768=LEAN, b767=PAPER, b769=PAPER, day1=PAPER, glob=PAPER, phase15=PAPER, nokernel=PAPER, empty=PAPER)
                 and set(j['four'].values()) == {'not run'} and set(j.get('planted_four', {}).values()) == {'run'}
                 and j['b3_post_together'] is False and j.get('planted_b3_together') is True
                 and all(j['gate'][q] == ('HELD' if q in QUARTERS else 'ABSENT') for q in j['gate'])
                 and all(j['planted_gate'][q] == 'ABSENT' for q in j['planted_gate'])
                 and held_ok and j.get('declared') == [True, False, True, False]
                 and j['tpl']['guard'] >= 2 and j['tpl']['quarters'] >= 1 and j['tpl']['declared'] >= 1 and j['tpl']['names'] >= 1
                 and j['verify'] == dict(lean=True, paper=True, lean_neg=False, lean_unequal=False) and ver == K27_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K28] THE PREV-MODE DRY'S SECOND SEND
K28_PATHS = ('tools/standing/prevdry.py', 'tools/standing/cadence.py', 'tools/standing/VERSION', 'data/b768_wlist.json')
K28_VERSION = 'v1.38.28'
K28_PROBE = r'''
import contextlib, inspect, io, json, os, sys, types
snap = sys.argv[1]
sys.path.insert(0, os.path.join(snap, 'tools'))
sys.path.insert(1, os.path.join(snap, 'tools', 'standing'))
fake = types.ModuleType('b703_checks')
fake.free_mb = lambda: 6000
sys.modules['b703_checks'] = fake
import prevdry as PD
PD._cur = lambda: dict(act='b768', parts=['act'])
PART = 'standing-c'
TO = lambda lim: dict(ok=False, part=PART, err='TIMEOUT after %d s -- THE %d s GUARD HIT: LETTER IT AS A DEFECT WHEN IT HAPPENS ((R358)(3)(x))' % (lim, lim), line=None, blob='b')
OK = lambda: dict(ok=True, part=PART, err=None, line=None, n=3, secs=700.0, blob='b')
ERR = lambda: dict(ok=False, part=PART, err='KeyError: x', line=10, at='x', secs=5.0, blob='b')
SC = dict(guard_then_ok=lambda lim: TO(lim) if lim == 590 else OK(), ok=lambda lim: OK(), fails=lambda lim: ERR(), both=lambda lim: TO(lim))
out = dict(default=inspect.signature(PD.exercise).parameters['timeout'].default)
mk = os.path.join(snap, 'data', 'b768_prevdry_%s.running' % PART)
def go(name, plant=False):
    calls, banks = [], []
    def ex(act, part, module_text=None, timeout=590):
        calls.append(timeout)
        return SC[name](timeout)
    PD.exercise = ex
    PD.write_bank = lambda act, part, o: (banks.append(o), os.path.join(snap, 'data', 'x.json'))[1]
    if plant:
        with open(mk, 'w') as fh:
            fh.write('{}')
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc = PD.main(['run', PART])
    except SystemExit as e:
        rc = 'exit %s' % str(e)[:120]
    left = os.path.exists(mk)
    if plant and left:
        os.remove(mk)
    t = buf.getvalue()
    return dict(calls=calls, banks=len(banks), rc=rc, ok=[b.get('ok') for b in banks], first=['first_send' in b for b in banks],
                one_event=('ONE EVENT' in t and 'NO DEFECT' in t), author=('LETTER' in t and 'AUTHOR' in t), mark_left=left)
for n in ('guard_then_ok', 'ok', 'fails', 'both'):   # ### no scenario named 'error': the frame reads that key as the probe's failure
    out[n] = go(n)
out['planted'] = go('guard_then_ok', plant=True)
print(json.dumps(out))
'''


def control_k28(before, after):
    """(R378)(8) [K28]: the prev-mode dry's second send, read in each revision in its own interpreter, prevdry's run route driven with its
    exercise() and write_bank() replaced by recorders (no child sent, no bank of the act written), the memory reader and the act's file
    stubbed, the part standing-c (one that runs at b768's kind). FAULT: a first send ended at the 590 s guard banked as it fell, one send,
    exit 1. CLEAN: exercise()'s own limit still 590; a first send at the guard followed by one send under 900 s, the result banked once with
    the first send recorded beside it, exit 0, the pair printed as one event and no defect, the send's mark gone after; a send that passes,
    or fails with another error, sent once and banked once, no pair printed; a second send ending at 900 s banked once, exit 1, printed to be
    lettered and put to the author, no third send; a send's mark standing (a copy of the run still going, as where the harness moves the
    call to the background), nothing sent and nothing banked; VERSION v1.38.28."""
    L, res = [], {}
    for name, rev, got, j, ver in two_revisions(K28_PATHS, before, after, K28_PROBE, 'b768k28_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (guard)   exercise()`s own limit: %s s' % j['default'])
        for k, label in (('guard_then_ok', 'the first send at the 590 s guard, the second passing'), ('ok', 'a send that passes'),
                         ('fails', 'a send failing by another error'), ('both', 'both sends at their limits'),
                         ('planted', 'a send`s mark standing (a copy still going)')):
            s = j[k]
            L.append('    (%s) %s: sends %s ; banked %d (ok %s ; the first send recorded %s) ; exit %s ; one event, no defect printed %s ; lettered '
                     'and put to the author printed %s ; the mark left %s' % (k, label, s['calls'], s['banks'], s['ok'], s['first'], s['rc'],
                                                                             s['one_event'], s['author'], s['mark_left']))
        g, o, e, b, p = j['guard_then_ok'], j['ok'], j['fails'], j['both'], j['planted']
        fault = g['calls'] == [590] and g['rc'] == 1 and g['banks'] == 1
        clean = (j['default'] == 590
                 and g['calls'] == [590, 900] and g['banks'] == 1 and g['ok'] == [True] and g['first'] == [True] and g['rc'] == 0
                 and g['one_event'] is True and g['mark_left'] is False
                 and o['calls'] == [590] and o['banks'] == 1 and o['first'] == [False] and o['rc'] == 0 and o['one_event'] is False and o['mark_left'] is False
                 and e['calls'] == [590] and e['banks'] == 1 and e['rc'] == 1 and e['one_event'] is False and e['mark_left'] is False
                 and b['calls'] == [590, 900] and b['banks'] == 1 and b['ok'] == [False] and b['rc'] == 1 and b['author'] is True and b['mark_left'] is False
                 and p['calls'] == [] and p['banks'] == 0 and p['rc'] == 5 and ver == K28_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


CONTROLS = dict(K26=control_k26, K27=control_k27, K28=control_k28)


def main(argv):
    if len(argv) < 3 or argv[0] not in CONTROLS:
        sys.exit(__doc__ + '\nkeys: %s' % ', '.join(sorted(CONTROLS)))
    key, before, after = argv[0], argv[1], argv[2]
    rc, b = git('rev-parse', before)
    rc2, a = git('rev-parse', after)
    rc3, p = git('rev-parse', '%s^1' % after)
    if rc or rc2 or rc3:
        sys.exit('### A REVISION DOES NOT RESOLVE -- NOTHING READ')
    b, a, p = b.decode().strip(), a.decode().strip(), p.decode().strip()
    head = ['## [%s] THE PLANTED CONTROL (%s): BEFORE relay %s, THE REPAIR`S COMMIT relay %s, its first parent %s -- %s' % (
        key, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), b[:8], a[:8], p[:8], 'THE COMMIT BEFORE' if p == b else 'NOT THE COMMIT BEFORE')]
    L, ok = CONTROLS[key](b, a)
    ok = ok and p == b
    L = head + L + ['### ### **[%s] THE CONTROL %s: THE FAULT READ BEFORE AND CLEAN AFTER: %s.**' % (key, 'AS WANTED' if ok else 'NOT AS WANTED', ok), '']
    print(NL.join(L))
    if '--bank' in argv:
        prior = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
            'b768 -- THE PLANTED CONTROLS OF THE THREE KEYS, (R378)(8), appended by tools/b768_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b768_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
