# -*- coding: utf-8 -*-
"""b766, (R376)(7): THE PLANTED CONTROLS OF THE THREE REPAIRS, ONE A KEY, in the form of tools/b765_repair_controls.py (its frame carried:
git, snapshot, probe, main). Each control reads the fault at the commit before the repair and reads clean at the repair's commit, both
printed. Read-only over the relay: each revision's files are taken by `git show <rev>:<path>` into a scratch folder of the system's
temporary directory (removed after), and each revision is probed in its own interpreter (`python -I`), so no module of one revision is read
by the other; the probe calls the revision's functions, writes nothing, runs no git command and prints one JSON line. [K23]'s control runs
each revision's tools/push_gated.sh under Git's bash over a scratch repository in that folder, its origin an address never contacted (the
existing-tag mode refuses at the clone before any remote is read), and prints counts, never a capture's line. [K24]'s probe reads each
revision's close order over data/standing_clauses_v5.txt, writes its planted mirror banks and export in a scratch folder of its own
(removed after), and reads b765's close export by data/b765_mirror.json, its digest alone, no member opened. --bank appends the
reading to data/b766_repair_controls.txt beneath a head naming the key and both commits; nothing else is written. The repair's commit must
have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b766_repair_controls.py <key> <before> <after> [--bank]
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
ACT = 'b766'
BANK = os.path.join(D, 'b766_repair_controls.txt')


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


# ================================================================================ [K22] THE KERNEL ROUTE FOR b766; push-b765-planted BY ITS NAME
K22_PATHS = ('tools/standing/commit.py', 'tools/standing/VERSION')
K22_VERSION = 'v1.38.22'
K22_PROBE = r'''
import ast, inspect, json, os, re, sys
snap = sys.argv[1]
src = open(os.path.join(snap, 'tools', 'standing', 'commit.py'), encoding='utf-8').read()
want = ('KERNELS', 'KERNEL_ACTS', 'NAMED_CONFLICTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'FORCED_DELETES', 'Refused', 'repo_refusal',
        'push_branch_ok', 'kernel_branch_refusal', 'merge_branch_refusal', 'conflict_refusal', 'ff_refusal', 'pushto_refusal',
        'pushto_name_refusal', 'rdelete_refusal', 'rdelete_plan', 'forced_name', 'kernel_delete_args')
tree = ast.parse(src)
nodes = [n for n in tree.body if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in want)
         or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
ns = dict(re=re)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'commit_k22', 'exec'), ns)
ns.setdefault('FORCED_DELETES', {})
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
PL, SECOND = 'push-b765-planted', 'push-b763-arith'
none = lambda v: v is None
R = ns['Refused']


def del_args(key, act, name, held, table=None):
    """the revision's local-delete arguments: its kernel_delete_args where it has one; else v1.38.21's kernel_write delete, its name
    refusal and its flag, read from the same source lines (kernel_branch_refusal, then -D where held or a control branch, else -d)."""
    f = ns.get('kernel_delete_args')
    if f:
        return f(key, act, name, held) if table is None else f(key, act, name, held, table=table)
    bad = ns['kernel_branch_refusal'](act, name)
    if bad:
        return bad, None
    return None, ['branch', '-D' if (held or name.startswith('push-%s-control' % act)) else '-d', name]


def dl(key, act, name, held, table=None):
    bad, a = del_args(key, act, name, held, table)
    return 'REFUSED' if bad else ' '.join(a[:2])


def plan(*a, forced=False):
    f = ns['rdelete_plan']
    try:
        if forced:
            if 'forced' not in inspect.signature(f).parameters:
                return 'NO FORCED FORM'
            return f(*a, forced=True)
        return f(*a)
    except R:
        return 'REFUSED'


M_, T_ = 'a' * 40, 'b' * 40
planted = {'b766': {EF: (PL, SECOND)}}   # ### the planted second name: FORCED_DELETES given push-b763-arith beside the one name
out = dict(
    open=none(ns['repo_refusal'](EF, 'b766')),
    ff=none(ns['ff_refusal'](EF, 'b766')),
    closed_m24=[none(ns['repo_refusal'](M24, 'b766')), none(ns['ff_refusal'](M24, 'b766'))],
    b765=[none(ns['repo_refusal'](EF, 'b765')), none(ns['ff_refusal'](EF, 'b765')), none(ns['repo_refusal'](M24, 'b765'))],
    other=[none(ns['repo_refusal'](EF, 'b767')), none(ns['ff_refusal'](EF, 'b767')), none(ns['repo_refusal']('SIDE-frobenius', 'b766'))],
    branch=[none(ns['kernel_branch_refusal']('b766', 'push-b766-proof')), none(ns['merge_branch_refusal']('b766', 'push-b766-proof')),
            none(ns['kernel_branch_refusal']('b766', 'main')), none(ns['merge_branch_refusal']('b766', 'main'))],
    named=none(ns['conflict_refusal']('b766', EF, ['print_targets.txt'])),
    pushto=none(ns['pushto_refusal'](EF, 'b766')),
    rdel=[none(ns['rdelete_refusal'](EF, 'b766', PL, kept=())), none(ns['rdelete_refusal'](EF, 'b766', SECOND, kept=())),
          none(ns['rdelete_refusal'](M24, 'b766', PL, kept=())), none(ns['rdelete_refusal'](EF, 'b766', 'main', kept=())),
          none(ns['rdelete_refusal'](EF, 'b766', PL, kept=(PL,))), none(ns['rdelete_refusal'](EF, 'b767', PL, kept=()))],
    plan=[plan(M_, T_, M_, T_, True), plan(M_, T_, M_, T_, False), plan(M_, T_, M_, T_, False, forced=True),
          plan(M_, '', M_, '', False, forced=True), plan(M_, T_, M_, '', False, forced=True), plan('', T_, '', T_, False, forced=True)],
    dele=[dl(EF, 'b766', PL, False), dl(EF, 'b766', SECOND, False), dl(EF, 'b766', SECOND, False, table=planted),
          dl(EF, 'b766', 'push-b766-proof', False), dl(EF, 'b766', 'push-b766-proof', True), dl(EF, 'b766', 'push-b766-control-x', False),
          dl(EF, 'b767', PL, False), dl(M24, 'b766', PL, False), dl(EF, 'b766', 'main', False)],
    rows=dict((t, sorted(ns[t])) for t in ('KERNEL_ACTS', 'FF_ACTS', 'PUSHTO_ACTS', 'RDELETE_ACTS', 'NAMED_CONFLICTS', 'FORCED_DELETES')),
    b766_rows=dict((t, list(ns[t].get('b766', ()))) for t in ('KERNEL_ACTS', 'FF_ACTS')),
    b766_named=dict((t, dict((k, list(v)) for k, v in (ns[t].get('b766') or {}).items())) for t in ('RDELETE_ACTS', 'FORCED_DELETES')))
print(json.dumps(out))
'''


def control_k22(before, after):
    """(R376)(7) [K22]: the kernel route opened for b766 at SIDE-explicit-formula, and push-b765-planted taken by its one name, read in each
    revision by commit.py's pure tables and functions (executed apart, nothing written, no git command run). FAULT: repo_refusal and
    ff_refusal refuse SIDE-explicit-formula for b766; the removal at the remote refuses push-b765-planted for b766 (RDELETE_ACTS names b759
    and b760); the local delete refuses it, not b766's push branch. CLEAN: b766 opened at SIDE-explicit-formula in both tables, SIDE-dirichlet-
    mod-24 and a third kernel refused, b765's opening unmoved, b767 refused; push-b766-proof admitted as the act's branch, main refused; no
    conflicted merge named, no push to a named branch; the removal admits push-b765-planted at SIDE-explicit-formula for b766 and refuses the
    planted second name push-b763-arith, the same name at SIDE-dirichlet-mod-24, main, the name on a kept list and the name for b767; the plan
    takes a merged tip, refuses an unmerged one unforced, takes it forced, and refuses forced a tip absent at the remote, a tip the clone lacks
    and a main not read; the local delete takes push-b765-planted with -D, refuses push-b763-arith and refuses it again with the second name
    planted in FORCED_DELETES (the table it is absent from, RDELETE_ACTS, governing), takes push-b766-proof with -d unmerged and -D held, a
    control branch with -D, and refuses the one name for b767, at SIDE-dirichlet-mod-24, and main; the only rows added b766's; VERSION
    v1.38.22."""
    L, res, rows = [], {}, {}
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b766k22_')
        try:
            got = snapshot(rev, K22_PATHS, tmp)
            j = probe(K22_PROBE, tmp)
            ver = version_of(tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b766k22_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        nn = lambda v: 'None' if v else 'REFUSED'
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (open)   repo_refusal(SIDE-explicit-formula, b766) %s ; (ff) ff_refusal %s' % (nn(j['open']), nn(j['ff'])))
        L.append('    (closed) SIDE-dirichlet-mod-24 for b766: repo %s, ff %s' % tuple(nn(v) for v in j['closed_m24']))
        L.append('    (b765)   SIDE-explicit-formula repo %s, ff %s ; SIDE-dirichlet-mod-24 repo %s' % tuple(nn(v) for v in j['b765']))
        L.append('    (other)  SIDE-explicit-formula for b767: repo %s, ff %s ; SIDE-frobenius for b766: %s' % tuple(nn(v) for v in j['other']))
        L.append('    (branch) push-b766-proof as branch %s, as HEAD for a commit %s ; main as branch %s, as HEAD %s' % tuple(nn(v) for v in j['branch']))
        L.append('    (named)  print_targets.txt in a conflicted merge for b766: %s ; (pushto) %s' % (nn(j['named']), nn(j['pushto'])))
        L.append('    (rdelete) push-b765-planted %s ; the second name push-b763-arith %s ; push-b765-planted at SIDE-dirichlet-mod-24 %s ; main %s ; '
                 'on a kept list %s ; for b767 %s' % tuple(nn(v) for v in j['rdel']))
        L.append('    (plan)   merged %s ; unmerged unforced %s ; unmerged forced %s ; forced, absent at the remote %s ; forced, not in the clone %s ; '
                 'forced, main not read %s' % tuple(j['plan']))
        L.append('    (delete) push-b765-planted %s ; push-b763-arith %s ; push-b763-arith PLANTED in FORCED_DELETES %s ; push-b766-proof unmerged %s, '
                 'held %s ; a control branch %s ; push-b765-planted for b767 %s, at SIDE-dirichlet-mod-24 %s ; main %s' % tuple(j['dele']))
        L.append('    (rows)   %s' % ' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['rows'].items())))
        L.append('    (b766)   %s ; %s' % (' ; '.join('%s %s' % (t, ', '.join(v) or 'none') for t, v in sorted(j['b766_rows'].items())),
                                           ' ; '.join('%s %s' % (t, json.dumps(v, sort_keys=True)) for t, v in sorted(j['b766_named'].items()))))
        fault = not j['open'] and not j['ff'] and j['rdel'][0] is False and j['dele'][0] == 'REFUSED'
        clean = (j['open'] and j['ff'] and not any(j['closed_m24']) and j['b765'] == [True, True, False] and not any(j['other'])
                 and j['branch'] == [True, True, False, False] and not j['named'] and not j['pushto']
                 and j['rdel'] == [True, False, False, False, False, False]
                 and j['plan'] == ['remove', 'REFUSED', 'remove', 'REFUSED', 'REFUSED', 'REFUSED']
                 and j['dele'] == ['branch -D', 'REFUSED', 'REFUSED', 'branch -d', 'branch -D', 'branch -D', 'REFUSED', 'REFUSED', 'REFUSED']
                 and j['b766_rows'] == {'KERNEL_ACTS': ['SIDE-explicit-formula'], 'FF_ACTS': ['SIDE-explicit-formula']}
                 and j['b766_named'] == {'RDELETE_ACTS': {'SIDE-explicit-formula': ['push-b765-planted']},
                                         'FORCED_DELETES': {'SIDE-explicit-formula': ['push-b765-planted']}}
                 and 'b766' not in j['rows']['PUSHTO_ACTS'] and 'b766' not in j['rows']['NAMED_CONFLICTS'] and ver == K22_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
        rows[name] = j['rows']
    diff_ok = None
    if 'BEFORE' in rows and 'AFTER' in rows:
        moved = dict((t, (sorted(set(rows['AFTER'][t]) - set(rows['BEFORE'][t])), sorted(set(rows['BEFORE'][t]) - set(rows['AFTER'][t]))))
                     for t in sorted(rows['AFTER']))
        want = ('KERNEL_ACTS', 'FF_ACTS', 'RDELETE_ACTS', 'FORCED_DELETES')
        diff_ok = all(moved[t] == ((['b766'], []) if t in want else ([], [])) for t in moved)
        L.append('  (diff)   the acts each table gains and loses, BEFORE to AFTER: %s -- %s' % (
            ' ; '.join('%s +%s -%s' % (t, ','.join(a) or 'none', ','.join(r) or 'none') for t, (a, r) in sorted(moved.items())),
            'b766 GAINED BY KERNEL_ACTS, FF_ACTS, RDELETE_ACTS AND FORCED_DELETES ALONE' if diff_ok else 'ANOTHER ROW MOVED'))
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and diff_ok is True


# ================================================================================ [K23] THE CAPTURES MASK THE ACCOUNT
K23_PATHS = ('tools/push_gated.sh', 'tools/standing/VERSION')
K23_VERSION = 'v1.38.23'
BASH = 'C:/Program Files/Git/bin/bash.exe'   # ### Git's bash, as tools/standing/v1230.py names it; the gated push runs under it
K23_PLANTED = 'planted-acct'
K23_LINES = ('To https://github.com/%s/relay.git' % K23_PLANTED, 'To git@github.com:%s/SIDE-explicit-formula.git' % K23_PLANTED,
             'remote:      https://github.com/%s/PLACE-papers/pull/new/push-b766-proof' % K23_PLANTED,
             'cloned to %s/PLACE-project-set' % K23_PLANTED, 'push_gated: DONE -- branch push-b766-proof pushed alone and read back')


def _k23_run(tmp):
    """push_gated.sh of the snapshot run over a scratch repository whose origin names the planted account (an address never contacted: the
    existing-tag mode refuses a tag the clone lacks, exit 10, before any remote is read), the capture named by PUSH_GATED_LOG under folders
    github.com/<planted>/PLACE-project-set, the tag's name github.com/<planted>/x; (exit, the capture's text)."""
    repo = os.path.join(tmp, 'repo')
    os.makedirs(repo)
    subprocess.run(['git', 'init', '-q', repo], capture_output=True)
    subprocess.run(['git', '-C', repo, 'remote', 'add', 'origin', 'https://github.com/%s/PLACE-project-set.git' % K23_PLANTED], capture_output=True)
    cdir = os.path.join(tmp, 'cap', 'github.com', K23_PLANTED, 'PLACE-project-set')
    os.makedirs(cdir)
    cap = os.path.join(cdir, 'push_out.txt')
    env = dict(os.environ, PUSH_GATED_LOG=cap.replace('\\', '/'))
    r = subprocess.run([BASH, os.path.join(tmp, 'tools', 'push_gated.sh').replace('\\', '/'), repo.replace('\\', '/'), '--existing-tag',
                        'github.com/%s/x' % K23_PLANTED], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env, timeout=120)
    text = io.open(cap, encoding='utf-8', errors='replace').read() if os.path.exists(cap) else ''
    return r.returncode, text, r.stdout + r.stderr


def _k23_expr(tmp):
    """the snapshot's mask expression (the one line `cap_mask='...'`), or None; applied by Git's sed to K23_LINES: (the lines out, exit)."""
    p = os.path.join(tmp, 'tools', 'push_gated.sh')
    m = [l for l in io.open(p, encoding='utf-8').read().split(NL) if l.strip().startswith("cap_mask='")]
    if len(m) != 1:
        return None, None
    expr = m[0].strip()[len("cap_mask='"):].rstrip("'")
    r = subprocess.run([BASH, '-c', 'sed -u -E "$1"', '_', expr], input=NL.join(K23_LINES) + NL, capture_output=True, text=True, encoding='utf-8',
                       errors='replace', timeout=60)
    return r.stdout.split(NL)[:len(K23_LINES)], r.returncode


def control_k23(before, after):
    """(R376)(7) [K23]: tools/push_gated.sh writes each capture with the account replaced by <account>. FAULT: the planted capture carries
    the planted account's name. CLEAN: it carries none, <account> in its place, the exit and the line count those of the run before; the
    script's expression masks a remote's address in each form (github.com/ and github.com:) and the trail's form, and leaves a line with
    no name unchanged; VERSION v1.38.23. The run reads no remote: the existing-tag mode refuses at the clone (exit 10)."""
    L, res, runs = [], {}, {}
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b766k23_')
        try:
            got = snapshot(rev, K23_PATHS, tmp)
            rc, text, both = _k23_run(tmp)
            lines_out, erc = _k23_expr(tmp)
            ver = version_of(tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b766k23_'):
                shutil.rmtree(tmp, ignore_errors=True)
        n_pl = text.count(K23_PLANTED)
        n_acc = text.count('<account>')
        n_lines = text.count(NL)
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)))
        L.append('    (run)    push_gated.sh --existing-tag over the planted repository: exit %d ; the capture %d lines ; the planted name %d ; <account> %d' % (
            rc, n_lines, n_pl, n_acc))
        if lines_out is None:
            L.append('    (expr)   no mask expression in the script')
        else:
            L.append('    (expr)   the script`s expression over the five planted lines (exit %s): %s' % (
                erc, ' | '.join(l.replace(K23_PLANTED, '<PLANTED>') for l in lines_out)))
        want_lines = ['To https://github.com/<account>/relay.git', 'To git@github.com:<account>/SIDE-explicit-formula.git',
                      'remote:      https://github.com/<account>/PLACE-papers/pull/new/push-b766-proof',
                      'cloned to <account>/PLACE-project-set', K23_LINES[4]]
        fault = rc == 10 and n_pl > 0 and lines_out is None
        clean = rc == 10 and n_pl == 0 and n_acc >= 2 and lines_out == want_lines and erc == 0 and ver == K23_VERSION
        runs[name] = (rc, n_lines)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    same = runs.get('BEFORE') == runs.get('AFTER')
    L.append('  (same)   the exit and the capture`s line count, BEFORE and AFTER: %s and %s -- %s' % (runs.get('BEFORE'), runs.get('AFTER'),
                                                                                                 'EQUAL' if same else 'DIFFER'))
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and same


# ================================================================================ [K24] THE PROJECT SET'S BUILD IN THE CLOSE'S ORDER
K24_PATHS = ('tools/standing/act.py', 'tools/standing/commit.py', 'tools/project_set.py', 'tools/act_close.py', 'tools/standing/VERSION')
K24_VERSION = 'v1.38.24'
K24_THREE = ('data/b999_project_set_build.json', 'data/b999_project_set_build.txt', 'data/b999_PLACE-project-set_push-b999-set_push_out.txt')
K24_MIRROR = tuple('data/b999_%s' % n for n in ('mirror.txt', 'mirror.json', 'mirror_build.json', 'mirror_root.json', 'mirror_verify.txt'))
K24_PROBE = r'''
import ast, hashlib, json, os, re, shutil, sys, tempfile
snap, v5, relay_data = sys.argv[1], sys.argv[2], sys.argv[3]
THREE = %r
MIRROR = %r
def defs(rel, want, ns):
    src = open(os.path.join(snap, *rel.split('/')), encoding='utf-8').read()
    tree = ast.parse(src)
    nodes = [n for n in tree.body if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in want)
             or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), rel, 'exec'), ns)
    return src, tree, sorted(getattr(n, 'name', None) or n.targets[0].id for n in nodes)
out = {}
A = dict(re=re, os=os, T=os.path.join(snap, 'tools'))
_s, _t, out['act_defs'] = defs('tools/standing/act.py', ('STEP_21', 'STEP_8A', 'STEP_23A', 'STEP_25_WORDS', 'CLOSE_COMMITS', 'close_order',
                                                         'close_dry', 'close_carried', 'project_set_banks'), A)
order = A['close_order'](open(v5, encoding='utf-8').read())
out['keys'] = [str(s[0]) for s in order]
out['words'] = dict((str(s[0]), s[1]) for s in order)
out['slot'] = [str(s[0]) for s in order if 'project_set_build' in s[2]]
if 'close_dry' in A:
    out['dry'] = A['close_dry']('b999', order)
    b = [s for s in order if str(s[0]) == '23a']
    rest = [s for s in order if str(s[0]) != '23a']
    i14 = [i for i, s in enumerate(rest) if s[0] == 14][0]
    out['dry_before_root'] = A['close_dry']('b999', rest[:i14] + b + rest[i14:])
    out['dry_no_25'] = A['close_dry']('b999', [s for s in order if s[0] != 25])
C = dict(re=re, os=os)
_s, _t, out['commit_defs'] = defs('tools/standing/commit.py', ('close_left_out',), C)
if 'close_left_out' in C and 'close_carried' in A:
    banks = A['close_carried']('b999')
    out['carried_has'] = [x in banks for x in THREE + MIRROR]
    allw = list(THREE + MIRROR)
    g = C['close_left_out']
    out['g_left'] = [x for x in allw if x in (g(banks, [], allw) or '')]
    out['g_staged'] = g(banks, allw, allw)
    out['g_none'] = g(banks, [], [])
    out['g_other'] = g(banks, [], ['data/b998_project_set_build.json', 'data/b998_mirror.json'])
    out['g_one'] = [x for x in allw if x in (g(banks, allw[:2] + allw[3:], allw) or '')]
P = dict(os=os, json=json, hashlib=hashlib, re=re, act=lambda: 'b999')
src, tree, out['ps_defs'] = defs('tools/project_set.py', ('close_export',), P)
mi = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'mirror']
out['mirror_own'] = bool(mi) and 'mirror_build.ps1' in (ast.get_source_segment(src, mi[0]) or '')
if 'close_export' in P:
    tmp = tempfile.mkdtemp(prefix='b766k24p_')
    try:
        dd, ee = os.path.join(tmp, 'data'), os.path.join(tmp, 'exports')
        os.makedirs(dd)
        os.makedirs(ee)
        zb = b'PK planted export of b999'
        open(os.path.join(ee, 'mirror-refresh-x-b999.zip'), 'wb').write(zb)
        good = dict(root_line='Act root: b999 0123abcd', clean=True, manifest_ok=True, zip='mirror-refresh-x-b999.zip',
                    zip_sha256=hashlib.sha256(zb).hexdigest())
        def case(rec):
            mp = os.path.join(dd, 'b999_mirror.json')
            if rec is None:
                if os.path.exists(mp):
                    os.remove(mp)
            else:
                open(mp, 'w', encoding='utf-8').write(json.dumps(rec))
            try:
                z, _r = P['close_export']('b999', data=dd, exports=ee)
                return 'RETURNED ' + os.path.basename(z)
            except SystemExit as e:
                return 'REFUSED' if str(e).startswith('###') else 'EXIT ' + str(e)[:60]
        out['x_none'] = case(None)
        out['x_other_root'] = case(dict(good, root_line='Act root: b998 0123abcd'))
        out['x_no_root'] = case(dict(good, root_line=''))
        out['x_not_clean'] = case(dict(good, clean=False))
        out['x_sha'] = case(dict(good, zip_sha256='0' * 64))
        out['x_good'] = case(good)
    finally:
        if os.path.basename(tmp).startswith('b766k24p_'):
            shutil.rmtree(tmp, ignore_errors=True)
    try:
        z, r = P['close_export']('b765', data=relay_data, exports='D:/MY-DOwnloads')
        out['x_b765'] = 'RETURNED %%s ; its root line names b765 %%s' %% (os.path.basename(z), (r.get('root_line') or '').startswith('Act root: b765 '))
    except SystemExit as e:
        out['x_b765'] = 'REFUSED ' + str(e)[:120]
print(json.dumps(out))
''' % (K24_THREE, K24_MIRROR)


def control_k24(before, after):
    """(R376)(7) [K24]: the Project set's build in the close's order. FAULT: the order holds no slot for the build, no tool refuses a commit
    leaving the builder's banks behind, the builder reads no export of the close's and its mirror route builds an export of its own. CLEAN:
    [23a] stands between [23] and [24], naming [23]'s export and [25], and [25] names [23a]'s banks, the order otherwise as before; the
    dry run of the order as printed leaves no bank of the builder outside a commit (written at [23a], carried at [25], none read by the
    root [14]), while a planted order with the build before the root reads its three banks outside a commit at the root, as b765's root
    part 1 did, and a planted order without [25] leaves them outside every commit; the one-call tool's guard refuses a commit leaving any
    of the close's banks untracked and unstaged, and no other; the builder takes the close's own export alone (a planted mirror bank with
    no root line, another act's, a verification not clean or a changed export refused; b765's close export read as the close's), and its
    mirror route builds nothing; VERSION v1.38.24."""
    L, res, got = [], {}, {}
    v5 = os.path.join(D, 'standing_clauses_v5.txt')
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b766k24_')
        try:
            files = snapshot(rev, K24_PATHS, tmp)
            r = probe(K24_PROBE, tmp, v5, D)
            ver = version_of(tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b766k24_'):
                shutil.rmtree(tmp, ignore_errors=True)
        got[name] = r
        L.append('  %s (relay %s, VERSION %s): the files %s' % (name, rev[:8], ver, ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in files)))
        if 'error' in r:
            L.append('    ### THE PROBE FAILED: %s' % r['error'])
            res[name] = 'NEITHER'
            continue
        k = r['keys']
        L.append('    (order)  %d steps: %s ; the build`s slot %s' % (len(k), ' '.join(k), r['slot'] or 'NONE'))
        L.append('    (words)  [23a] %r ; [25] %r' % (r['words'].get('23a', 'ABSENT')[:90], r['words'].get('25', 'ABSENT')[:90]))
        if 'dry' in r:
            for lab in ('dry', 'dry_before_root', 'dry_no_25'):
                d = r[lab]
                L.append('    (%s) slot %s ; carried at %s ; read by the root outside a commit %d %s ; outside every commit %d %s' % (
                    {'dry': 'dry, the order as printed', 'dry_before_root': 'dry, PLANTED: the build before the root [14]',
                     'dry_no_25': 'dry, PLANTED: the order without [25]'}[lab], d['slot'], d['carried_at'], len(d['at_root']),
                    d['at_root'] or '', len(d['outside']), d['outside'] or ''))
        else:
            L.append('    (dry)    no dry run of the close`s order in the tools (close_dry absent)')
        if 'g_left' in r:
            L.append('    (guard)  close_left_out: eight banks untracked, none staged -> names %d of 8 ; all staged -> %s ; none written -> %s ; '
                     'another act`s untracked -> %s ; the push capture alone unstaged -> names %s' % (
                         len(r['g_left']), r['g_staged'], r['g_none'], r['g_other'], [x.split('_', 1)[1] for x in r['g_one']]))
            L.append('    (banks)  close_carried holds the three of the build and the five of the mirror: %s' % r['carried_has'])
        else:
            L.append('    (guard)  no refusal of a commit leaving the close`s banks behind (close_left_out absent)')
        if 'x_good' in r:
            L.append('    (export) close_export: no mirror bank %s ; another act`s root line %s ; no root line %s ; not clean %s ; the export`s sha256 '
                     'not the bank`s %s ; the planted export as banked %s' % (r['x_none'], r['x_other_root'], r['x_no_root'], r['x_not_clean'],
                                                                              r['x_sha'], r['x_good']))
            L.append('    (record) b765`s close export by data/b765_mirror.json: %s' % r['x_b765'])
        else:
            L.append('    (export) the builder reads no export of the close`s (close_export absent)')
        L.append('    (mirror) the builder`s mirror route builds an export of its own (tools/mirror_build.ps1 in its body): %s' % r['mirror_own'])
        fault = (not r['slot']) and 'dry' not in r and 'g_left' not in r and 'x_good' not in r and r['mirror_own'] is True
        three = list(K24_THREE)
        clean = (r['slot'] == ['23a'] and k.index('23a') == k.index('23') + 1 and k[k.index('23a') + 1] == '24'
                 and '[23]' in r['words']['23a'][:90] and '[25]' in r['words']['23a'][:90] and '[23a]' in r['words']['25'][:90]
                 and r.get('dry') == dict(slot='23a', carried_at=25, at_root=[], outside=[])
                 and r['dry_before_root']['at_root'] == three and r['dry_before_root']['slot'] == '23a'
                 and r['dry_no_25']['outside'] == three
                 and len(r['g_left']) == 8 and r['g_staged'] is None and r['g_none'] is None and r['g_other'] is None
                 and r['g_one'] == [three[2]] and all(r['carried_has'])
                 and [r[x] for x in ('x_none', 'x_other_root', 'x_no_root', 'x_not_clean', 'x_sha')] == ['REFUSED'] * 5
                 and r['x_good'] == 'RETURNED mirror-refresh-x-b999.zip'
                 and r['x_b765'] == 'RETURNED mirror-refresh-2026-11-21-b765.zip ; its root line names b765 True'
                 and r['mirror_own'] is False and ver == K24_VERSION)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    same = None
    if 'keys' in got.get('BEFORE', {}) and 'keys' in got.get('AFTER', {}):
        b, a = got['BEFORE'], got['AFTER']
        kept = [x for x in a['keys'] if x != '23a'] == b['keys']
        moved = sorted(x for x in b['keys'] if b['words'].get(x) != a['words'].get(x))
        same = kept and moved == ['25']
        L.append('  (diff)   the order BEFORE to AFTER: steps gained %s ; the steps before otherwise in their order %s ; words changed at %s -- %s' % (
            sorted(set(a['keys']) - set(b['keys'])), kept, moved or 'none', '[23a] GAINED AND [25]`S WORDS ALONE MOVED' if same else 'ANOTHER STEP MOVED'))
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and same is True


CONTROLS = dict(K22=control_k22, K23=control_k23, K24=control_k24)


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
            'b766 -- THE PLANTED CONTROLS OF THE REPAIRS, (R376)(7), one section a key, each appended by tools/b766_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b766_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
