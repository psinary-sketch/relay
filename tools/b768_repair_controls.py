# -*- coding: utf-8 -*-
"""b768, (R378)(8): THE PLANTED CONTROLS OF THE THREE KEYS, [K26], [K27] and [K28], in the form of tools/b767_repair_controls.py (its frame
carried: git, snapshot, probe, version_of, main; [K25]'s probe set to the kernel route for b768). Each key's control is added to this tool
and committed before its first run. The control reads the fault at the commit before the repair and reads clean at the repair's commit,
both printed. Read-only over the relay: each revision's files are taken by `git show <rev>:<path>` into a scratch folder of the system's
temporary directory (removed after), and each revision is probed in its own interpreter (`python -I`), so no module of one revision is
read by the other; the probe executes the standing tool's pure tables and functions apart, writes nothing, runs no git command and prints
one JSON line. --bank appends the reading to data/b768_repair_controls.txt beneath a head naming the key and both commits; nothing else is
written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b768_repair_controls.py <K26> <before> <after> [--bank]
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


CONTROLS = dict(K26=control_k26)


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
