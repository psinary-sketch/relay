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


CONTROLS = dict(K31=control_k31)


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
