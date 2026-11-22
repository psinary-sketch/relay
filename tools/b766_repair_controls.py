# -*- coding: utf-8 -*-
"""b766, (R376)(7): THE PLANTED CONTROLS OF THE THREE REPAIRS, ONE A KEY, in the form of tools/b765_repair_controls.py (its frame carried:
git, snapshot, probe, main). Each control reads the fault at the commit before the repair and reads clean at the repair's commit, both
printed. Read-only over the relay: each revision's files are taken by `git show <rev>:<path>` into a scratch folder of the system's
temporary directory (removed after), and each revision is probed in its own interpreter (`python -I`), so no module of one revision is read
by the other; the probe calls the revision's functions, writes nothing, runs no git command and prints one JSON line. [K23]'s control runs
each revision's tools/push_gated.sh under Git's bash over a scratch repository in that folder, its origin an address never contacted (the
existing-tag mode refuses at the clone before any remote is read), and prints counts, never a capture's line. --bank appends the
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


CONTROLS = dict(K22=control_k22, K23=control_k23)


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
