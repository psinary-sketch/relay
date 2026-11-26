# -*- coding: utf-8 -*-
"""b770, (R380)(8): THE PLANTED CONTROLS OF THE THREE KEYS, [K31], [K32] and [K33], in the form of tools/b769_repair_controls.py (its frame
carried: git, snapshot, probe, version_of, two_revisions, main; b765's (R375)(4) probe of commit.py's pure tables carried as [K31]'s, set to
b770). Each key's control is added to this tool and committed before its first run. The control reads the fault at the commit before the
repair and reads clean at the repair's commit, both printed. Read-only over the relay: each revision's files are taken by
`git show <rev>:<path>` into a scratch folder of the system's temporary directory (removed after), and each revision is probed in its own
interpreter (`python -I`), so no module of one revision is read by the other; the probe executes the standing tool's pure tables and
functions apart, runs no git command and prints one JSON line; it writes nothing outside its own snapshot folder. AFTER may be the word
WORKTREE: the working tree's copies of the key's files are read in place of a commit's, for the reading before the repair's commit; that
reading is printed and never banked. --bank appends the reading to data/b770_repair_controls.txt beneath a head naming the key and both
commits; nothing else is written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b770_repair_controls.py <K31|K32|K33> <before> <after|WORKTREE> [--bank]

[K32]'s and [K33]'s controls are added before their first runs, each committed before it.
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
ACT = 'b770'
BANK = os.path.join(D, 'b770_repair_controls.txt')
WORKTREE = 'WORKTREE'


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def snapshot(rev, paths, dest):
    """the files `paths` at `rev` (or the working tree's copies where rev is WORKTREE) under dest, at their relay paths; [(path, present)]."""
    out = []
    for p in paths:
        if rev == WORKTREE:
            src = os.path.join(ROOT, *p.split('/'))
            ok = os.path.isfile(src)
            b = open(src, 'rb').read() if ok else b''
            rc = 0 if ok else 1
        else:
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


# ================================================================================ [K31] THE KERNEL ROUTE FOR b770
K31_PATHS = ('tools/standing/commit.py', 'tools/standing/VERSION')
K31_VERSION = 'v1.38.31'
K31_PROBE = r'''
import ast, json, os, re, sys
snap = sys.argv[1]
src = open(os.path.join(snap, 'tools', 'standing', 'commit.py'), encoding='utf-8').read()
want = ('KERNELS', 'KERNEL_ACTS', 'NAMED_CONFLICTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'FORCED_DELETES', 'repo_refusal', 'push_branch_ok',
        'kernel_branch_refusal', 'merge_branch_refusal', 'conflict_refusal', 'ff_refusal', 'pushto_refusal', 'pushto_name_refusal', 'rdelete_refusal',
        'forced_name', 'kernel_delete_args')
tree = ast.parse(src)
nodes = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in want) or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
ns = dict(re=re)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'commit_k31', 'exec'), ns)
EF, M24, PLANT = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24', 'SIDE-frobenius'
none = lambda v: v is None
ns['KERNELS'] = dict(ns['KERNELS'])
planted = dict(ns['KERNELS'], **{PLANT: 'X:/' + PLANT})
def with_kernels(k, f):
    old = ns['KERNELS']
    ns['KERNELS'] = k
    try:
        return f()
    finally:
        ns['KERNELS'] = old
da = ns['kernel_delete_args']
out = dict(
    open=none(ns['repo_refusal'](EF, 'b770')),
    ff=none(ns['ff_refusal'](EF, 'b770')),
    closed_m24=[none(ns['repo_refusal'](M24, 'b770')), none(ns['ff_refusal'](M24, 'b770'))],
    planted=[none(with_kernels(planted, lambda: ns['repo_refusal'](PLANT, 'b770'))), none(with_kernels(planted, lambda: ns['ff_refusal'](PLANT, 'b770'))),
             none(ns['repo_refusal'](PLANT, 'b770'))],
    b768=[none(ns['repo_refusal'](EF, 'b768')), none(ns['ff_refusal'](EF, 'b768')), none(ns['repo_refusal'](M24, 'b768'))],
    b769=[none(ns['repo_refusal'](EF, 'b769')), none(ns['ff_refusal'](EF, 'b769'))],
    other=[none(ns['repo_refusal'](EF, 'b771')), none(ns['ff_refusal'](EF, 'b771'))],
    branch=[none(ns['kernel_branch_refusal']('b770', 'push-b770-proof')), none(ns['merge_branch_refusal']('b770', 'push-b770-proof')),
            none(ns['kernel_branch_refusal']('b770', 'push-b768-proof')), none(ns['kernel_branch_refusal']('b770', 'main')),
            none(ns['merge_branch_refusal']('b770', 'main'))],
    named=none(ns['conflict_refusal']('b770', EF, ['print_targets.txt'])),
    holds=[none(ns['pushto_refusal'](EF, 'b770')), none(ns['rdelete_refusal'](EF, 'b770', 'push-b768-proof', kept=())),
           none(ns['rdelete_refusal'](EF, 'b770', 'push-b767-proof', kept=())), none(ns['rdelete_refusal'](EF, 'b770', 'push-b766-proof', kept=()))],
    forced=[ns['forced_name'](EF, 'b770', n) for n in ('push-b768-proof', 'push-b767-proof', 'push-b766-proof')],
    deletes=[da(EF, 'b770', 'push-b768-proof', True)[0] is not None, da(EF, 'b770', 'push-b770-proof', False)[1]],
    rows=dict((t, sorted(ns[t])) for t in ('KERNEL_ACTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'NAMED_CONFLICTS', 'FORCED_DELETES')),
    b770_rows=dict((t, list(ns[t].get('b770', ()))) for t in ('KERNEL_ACTS', 'FF_ACTS')),
    kernels=sorted(ns['KERNELS']))
print(json.dumps(out))
'''
K31_ROWS_BEFORE = ['b757', 'b758', 'b759', 'b763', 'b764', 'b765', 'b766', 'b767', 'b768']


def control_k31(before, after):
    """(R380)(8) [K31]: the kernel route for b770, read in each revision by commit.py's pure refusals (its tables and refusal functions
    executed apart, nothing written, no git command run). FAULT: repo_refusal and ff_refusal refuse SIDE-explicit-formula for b770, so
    push-b770-proof, its commits and the local main after the gated push are refused before anything is read. CLEAN: both None for b770 at
    SIDE-explicit-formula; THE PLANTED SECOND KERNEL: SIDE-dirichlet-mod-24 refused for b770 in both tables, and a planted kernel's name
    (SIDE-frobenius, added to the kernels in the probe alone) refused for b770 in both tables and refused as no repository without the plant;
    b768's opening unmoved; b769 and b771 refused; push-b770-proof admitted as the act's branch and as HEAD for a commit, push-b768-proof and
    main refused; no conflicted merge named; the push to a named branch refused for b770 and the removal at a remote refused for
    push-b768-proof, push-b767-proof and push-b766-proof ("RDELETE_ACTS names nothing for b770"), none forced; the local delete of
    push-b768-proof refused and of push-b770-proof taken by -d; the only rows added b770's, each SIDE-explicit-formula alone; the kernels two;
    VERSION v1.38.31."""
    L, res = [], {}
    for name, rev, got, j, ver in two_revisions(K31_PATHS, before, after, K31_PROBE, 'b770k31_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        nn = lambda v: 'None' if v else 'REFUSED'
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (open)    repo_refusal(SIDE-explicit-formula, b770) %s ; (ff) ff_refusal %s' % (nn(j['open']), nn(j['ff'])))
        L.append('    (closed)  SIDE-dirichlet-mod-24 for b770: repo %s, ff %s' % tuple(nn(v) for v in j['closed_m24']))
        L.append('    (planted) THE PLANTED SECOND KERNEL SIDE-frobenius for b770, added to the kernels in the probe: repo %s, ff %s ; without the '
                 'plant: %s' % tuple(nn(v) for v in j['planted']))
        L.append('    (b768)    SIDE-explicit-formula repo %s, ff %s ; SIDE-dirichlet-mod-24 repo %s' % tuple(nn(v) for v in j['b768']))
        L.append('    (other)   SIDE-explicit-formula for b769: repo %s, ff %s ; for b771: repo %s, ff %s' % tuple(nn(v) for v in j['b769'] + j['other']))
        L.append('    (branch)  push-b770-proof as branch %s, as HEAD for a commit %s ; push-b768-proof %s ; main as branch %s, as HEAD %s' % tuple(
            nn(v) for v in j['branch']))
        L.append('    (named)   print_targets.txt in a conflicted merge for b770: %s ; (holds) pushto %s ; rdelete push-b768-proof %s, push-b767-proof '
                 '%s, push-b766-proof %s' % ((nn(j['named']),) + tuple(nn(v) for v in j['holds'])))
        L.append('    (deletes) forced %s ; the local delete of push-b768-proof refused %s ; of push-b770-proof %s' % (
            j['forced'], j['deletes'][0], ' '.join(j['deletes'][1] or ['REFUSED'])))
        L.append('    (rows)    %s ; b770: %s ; the kernels %s' % (
            ' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['rows'].items())),
            ' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['b770_rows'].items())), ', '.join(j['kernels'])))
        fault = not j['open'] and not j['ff']
        clean = (j['open'] and j['ff'] and not any(j['closed_m24']) and not any(j['planted']) and j['b768'] == [True, True, False]
                 and not any(j['b769']) and not any(j['other']) and j['branch'] == [True, True, False, False, False] and not j['named']
                 and not any(j['holds']) and not any(j['forced']) and j['deletes'] == [True, ['branch', '-d', 'push-b770-proof']]
                 and j['b770_rows'] == {'KERNEL_ACTS': ['SIDE-explicit-formula'], 'FF_ACTS': ['SIDE-explicit-formula']}
                 and j['rows']['KERNEL_ACTS'] == K31_ROWS_BEFORE + ['b770'] and j['rows']['FF_ACTS'] == [r for r in K31_ROWS_BEFORE if r != 'b757'] + ['b770']
                 and 'b770' not in j['rows']['PUSHTO_ACTS'] and 'b770' not in j['rows']['RDELETE_ACTS']
                 and 'b770' not in j['rows']['NAMED_CONFLICTS'] and 'b770' not in j['rows']['FORCED_DELETES']
                 and j['kernels'] == ['SIDE-dirichlet-mod-24', 'SIDE-explicit-formula'] and ver == K31_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K32] THE HOST'S FOLDERS MASKED AT THE SOURCE
K32_PATHS = ('tools/standing/hostmask.py', 'tools/standing/act.py', 'tools/standing/components.py', 'tools/standing/prevdry.py',
             'tools/standing/hook.py', 'tools/standing/fold/checks.tpl', 'tools/standing/fold/record.tpl', 'tools/standing/fold/closing.tpl',
             'tools/push_gated.sh', 'tools/standing/VERSION')
K32_VERSION = 'v1.38.32'
# ### the probe: in the revision's snapshot, the papers` repository's path and its parent folder taken from the snapshot's act.py REPOS['pp']
# ### (never typed), planted lines built from them at run time with two planted names of an archive's shape (no archive's own), each sent
# ### through the revision's own writers -- the checks template's rec, the record template's put_json and put_txt (each function's text
# ### taken from the template and run with its neighbours stubbed), tools/standing/components.py's banks_of (git stubbed),
# ### tools/standing/prevdry.py's write_bank (into the snapshot's data/), tools/standing/hook.py's refuse (its row into the snapshot) and
# ### tools/push_gated.sh's capture pipeline (its cap_mask line and the filters inside its exec line, run by bash on planted capture lines,
# ### the tee left out) -- and counted after: the folder's forms, its name alone and the names of an archive's shape. Only counts and
# ### booleans are printed; no line's text. The writers the probe does not run (the gate banks' runb, the closing template's two) are
# ### read by their calls of the mask.
K32_PROBE = r'''
import datetime, importlib.util, json, os, re, subprocess, sys
snap = sys.argv[1]
S = os.path.join(snap, 'tools', 'standing')
NL = '\n'
def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m
A = load('k32_act', os.path.join(S, 'act.py'))
PP = os.path.normpath(A.REPOS['pp'])
PAR = os.path.dirname(PP)
BASE = os.path.basename(PAR)
def forms(p):
    p = p.replace('\\', '/').rstrip('/')
    out = {p, p.replace('/', '\\'), p.replace('/', '\\\\')}
    if len(p) > 2 and p[1] == ':':
        out.add('/' + p[0] + p[2:])
    return sorted(out, key=len, reverse=True)
LOW = [f.lower() for f in forms(PAR)]
ASH = re.compile(r'(?<![A-Za-z0-9_])[A-Z0-9_]{16,}\.zip(?![A-Za-z0-9_])')
BRE = re.compile(r'(?<![a-z0-9_])%s(?![a-z0-9_])' % re.escape(BASE.lower()))
def cnt(s):
    s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    low = s.lower()
    return sum(low.count(f) for f in LOW) + len(BRE.findall(low)) + len(ASH.findall(s))
def block(text, head):
    m = re.search(r'^%s.*\n(?:[ \t].*\n|[ \t]*\n)*' % re.escape(head), text, re.M)
    return m.group(0) if m else None
ARCH, ARCH2 = 'ZZ_PLANTED_ARCHIVE_OF_THE_CONTROL_01.zip', 'ZZ_PLANTED_ARCHIVE_OF_THE_CONTROL_02.zip'
PLANT = 'a planted line: %s ; %s ; %s alone ; %s' % (PP, PAR.replace('\\', '/'), BASE.upper(), ARCH)
CLEAN = 'a clean line: data/b770_events.txt at relay HEAD'
HAS = os.path.isfile(os.path.join(S, 'hostmask.py'))
HM = load('k32_hostmask', os.path.join(S, 'hostmask.py')) if HAS else None
os.makedirs(os.path.join(snap, 'data'), exist_ok=True)
out = dict(root=len(PAR.replace('\\', '/').rstrip('/')) <= 2, hostmask=HAS, plant=cnt(PLANT))
class Stub(object):
    pass
ck = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
printed = []
ns = dict(L=[], print=lambda *a, **k: printed.append(' '.join(str(x) for x in a)))
if HM:
    ns['HMK'] = HM
exec(block(ck, 'def rec('), ns)
ns['rec'](PLANT)
ns['rec'](CLEAN)
out['rec'] = [cnt(ns['L'][0]), cnt(printed[0]), ns['L'][1] == CLEAN]
rt = open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
got = {}
mem, r_ = Stub(), Stub()
mem.guard, r_.ROOT_EXCLUDE = (lambda *a, **k: None), None
ns = dict(MEM=mem, R=r_, ACT='b770', _lock_guard=lambda n: None, _hash_record=lambda n: None,
          _put_json0=lambda n, o: got.__setitem__('json', o), _put_txt0=lambda n, l: got.__setitem__('txt', l))
if HM:
    ns['HMK'] = HM
exec(block(rt, 'def put_json('), ns)
exec(block(rt, 'def put_txt('), ns)
ns['put_json']('b770_k32_probe.json', {PP: 1, 'out': PLANT})
ns['put_txt']('b770_k32_probe.txt', [PLANT, CLEAN])
out['record'] = [cnt(got['json']), cnt(got['txt']), got['txt'][1] == CLEAN]
C = load('k32_components', os.path.join(S, 'components.py'))
C.A.gs = lambda repo, *a: NL.join(['FINDINGS.md', 'clusters/lean-archive-november-2026/' + ARCH, 'clusters/lean-archive-november-2026/' + ARCH2,
                                   'clusters/lean-archive-november-2026/MANIFEST.txt'])
b_ = C.banks_of('b770', 'pp', 'x')
out['components'] = [cnt(b_), len(b_), len(set(b_)), any(x.endswith('MANIFEST.txt') for x in b_), C.banks_of('b770', 'relay', 'x') == []]
P = load('k32_prevdry', os.path.join(S, 'prevdry.py'))
pth = P.write_bank('b770', 'k32probe', dict(ok=False, err=PLANT, line=None))
out['prevdry'] = [cnt(open(pth, encoding='utf-8').read()), os.path.dirname(os.path.abspath(pth)) == os.path.abspath(os.path.join(snap, 'data'))]
hk = open(os.path.join(S, 'hook.py'), encoding='utf-8').read()
rows_p = os.path.join(snap, 'data', 'k32_refusals.txt')
ns = dict(os=os, json=json, datetime=datetime, ROWS={'READ': 'a planted row'}, refusals_path=lambda relay=None: rows_p, RELAY=snap,
          __file__=os.path.join(S, 'hook.py'))
exec(block(hk, 'def refuse('), ns)
ns['refuse']('READ', 'a planted detail naming ' + PAR, 'Read', {'file_path': PP + '/FINDINGS.md'})
out['hook'] = [cnt(open(rows_p, encoding='utf-8').read()), os.path.getsize(rows_p) > 0]
pg = open(os.path.join(snap, 'tools', 'push_gated.sh'), encoding='utf-8').read()
cm = re.search(r"^[ \t]*cap_mask='[^'\n]*'[ \t]*$", pg, re.M)
ex = re.search(r'^[ \t]*exec > >\((.*) \| tee -a "\$cap"\) 2>&1[ \t]*$', pg, re.M)
cap = 'push_gated: repo %s ; branch push-b770-planted\nFrom github.com/planted-account/PLACE-project-set\n%s\n' % (PP, CLEAN)
if cm and ex:
    script = cm.group(0).strip() + NL + "hm_dir='%s'" % os.path.join(snap, 'tools').replace('\\', '/') + NL + ex.group(1) + NL
    r = subprocess.run(['bash', '-c', script], input=cap.encode('utf-8'), capture_output=True)
    g_ = r.stdout.decode('utf-8', 'replace')
    out['capture'] = [cnt(cap), cnt(g_), '<account>' in g_ and 'planted-account' not in g_, CLEAN in g_, r.returncode, len([l for l in g_.split(NL) if l])]
else:
    out['capture'] = None
cl = open(os.path.join(S, 'fold', 'closing.tpl'), encoding='utf-8').read()
out['needles'] = dict(record=rt.count('HMK.'), closing=cl.count('HMK.'), checks=ck.count('HMK.'),
                      imports=[t.count('from standing import hostmask as HMK') for t in (rt, ck, cl)],
                      prevdry=open(os.path.join(S, 'prevdry.py'), encoding='utf-8').read().count('_hmk()'),
                      push=pg.count('hostmask.py" filter'))
print(json.dumps(out))
'''


def control_k32(before, after):
    """[K32]: BEFORE (the commit before the repair) the planted folder, its name and the planted archives' names survive each writer and the
    capture -- THE FAULT READ; AFTER (the repair's commit) each writer and the capture read 0 of them, each role in place, a clean line
    unchanged, two archives two, the writers the probe does not run reading their calls of the mask, VERSION v1.38.32 -- CLEAN."""
    L, res = [], {}
    for name, rev, got, j, ver in two_revisions(K32_PATHS, before, after, K32_PROBE, 'b770k32_'):
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (plant)      the planted line carries %d of the folder`s forms, its name and an archive`s shape ; the parent a volume`s root %s ; '
                 'tools/standing/hostmask.py %s' % (j['plant'], j['root'], 'present' if j['hostmask'] else 'ABSENT'))
        L.append('    (rec)        the checks template`s rec: the banked line %d, the printed line %d ; a clean line unchanged %s' % tuple(j['rec']))
        L.append('    (record)     the record template`s put_json %d and put_txt %d ; a clean line unchanged %s' % tuple(j['record']))
        L.append('    (components) banks_of over the papers` repository: %d in %d entries, %d distinct, the manifest kept %s ; the relay`s list unread %s' % tuple(j['components']))
        L.append('    (prevdry)    write_bank: %d in the bank written ; written in the snapshot`s data/ %s' % tuple(j['prevdry']))
        L.append('    (hook)       refuse: %d in the refusal row ; the row written %s' % tuple(j['hook']))
        c = j['capture']
        L.append('    (capture)    the gated push`s capture pipeline on planted lines: %s' % (
            'THE PIPELINE NOT READ' if c is None else '%d before, %d after ; the account masked %s ; a clean line kept %s ; exit %d ; lines %d' % tuple(c)))
        n = j['needles']
        L.append('    (needles)    the mask`s calls: record.tpl %d, closing.tpl %d, checks.tpl %d ; the import in record, checks, closing %s ; prevdry.py %d ; '
                 'push_gated.sh`s filter %d' % (n['record'], n['closing'], n['checks'], n['imports'], n['prevdry'], n['push']))
        fault = j['plant'] >= 4 and not j['root'] and j['rec'][0] > 0 and j['record'][0] > 0 and c is not None and c[1] > 0
        clean = (j['plant'] >= 4 and not j['root'] and j['hostmask'] and j['rec'] == [0, 0, True] and j['record'] == [0, 0, True]
                 and j['components'] == [0, 4, 4, True, True] and j['prevdry'] == [0, True] and j['hook'] == [0, True]
                 and c is not None and c[0] >= 1 and c[1] == 0 and c[2] and c[3] and c[4] == 0 and c[5] == 3
                 and n['record'] >= 3 and n['closing'] >= 2 and n['checks'] >= 4 and n['imports'] == [1, 1, 1] and n['prevdry'] >= 2
                 and n['push'] == 1 and ver == K32_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


CONTROLS = dict(K31=control_k31, K32=control_k32)


def main(argv):
    if len(argv) < 3 or argv[0] not in CONTROLS:
        sys.exit(__doc__ + '\nkeys: %s' % ', '.join(sorted(CONTROLS)))
    key, before, after = argv[0], argv[1], argv[2]
    wt = after == WORKTREE
    if wt and '--bank' in argv:
        sys.exit('### THE WORKTREE READING IS NEVER BANKED -- NOTHING READ')
    rc, b = git('rev-parse', before)
    rc2, a = (0, WORKTREE.encode()) if wt else git('rev-parse', after)
    rc3, p = (0, b) if wt else git('rev-parse', '%s^1' % after)
    if rc or rc2 or rc3:
        sys.exit('### A REVISION DOES NOT RESOLVE -- NOTHING READ')
    b, a, p = b.decode().strip(), a.decode().strip(), p.decode().strip()
    head = ['## [%s] THE PLANTED CONTROL (%s): BEFORE relay %s, THE REPAIR`S COMMIT %s, its first parent %s -- %s' % (
        key, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), b[:8], 'THE WORKING TREE' if wt else 'relay ' + a[:8], 'not read' if wt else p[:8],
        'THE WORKING TREE, READ BEFORE THE REPAIR`S COMMIT, NOT BANKED' if wt else ('THE COMMIT BEFORE' if p == b else 'NOT THE COMMIT BEFORE'))]
    L, ok = CONTROLS[key](b, WORKTREE if wt else a)
    ok = ok and p == b
    L = head + L + ['### ### **[%s] THE CONTROL %s: THE FAULT READ BEFORE AND CLEAN AFTER: %s.**' % (key, 'AS WANTED' if ok else 'NOT AS WANTED', ok), '']
    print(NL.join(L))
    if '--bank' in argv:
        prior = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
            'b770 -- THE PLANTED CONTROLS OF THE THREE KEYS, (R380)(8), appended by tools/b770_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b770_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
