# -*- coding: utf-8 -*-
"""b718_pin.py -- (R328)(8), THE FEDERATION PIN, LAST AND STOPPABLE: one branch per kernel of data/b716_federation_pin_price.txt (the twelve
below the target) carrying the bump to Mathlib de5ce8a9 (leanprover/lean4:v4.34.0-rc1), each build dispatched to the hosted runner and read by
its run id. No lean or lake process runs on this host (N1): the manifest is written from the target kernel's own (SIDE-explicit-formula at
its HEAD, which builds at the target, data/b716_federation_pin_price.txt (3b)), not by `lake update`. Nothing is repaired; no kernel's main
is touched (the bump commit is made with git's plumbing from main's tree, the working tree and main's ref unmoved); no tag is cut.

  plan                 per kernel: its checkout, HEAD, main, clean, toolchain, lakefile and its Mathlib require, manifest packages,
                       workflows with their triggers and inputs; writes nothing
  bump <kernel>        the bump commit on main's tree (three root files: lean-toolchain, the lakefile's Mathlib require, lake-manifest.json)
                       and the branch BRANCH at it; prints the diff; one ref written, nothing pushed
  runs <kernel>        the kernel's runs on the bump branch, by id
  bank                 writes data/b718_pin.txt and data/b718_pin.json from data/b718_pin_rows.json (the rows each read appends)
  read <kernel> <id>   one run read by id: status, conclusion, times, the failing step's opening error lines; appends its row
"""
import io
import json
import os
import re
import subprocess
import sys
import time

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KERNELS = ('SIDE-effects', 'SIDE-archimedean', 'SIDE-cosmo', 'SIDE-frobenius', 'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel',
           'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-spinor', 'SIDE-trivium')   # (R328)(8); b716's (3) :56-:138
TARGET_KERNEL = 'SIDE-explicit-formula'
TARGET_REV = 'de5ce8a9a66a'
TOOLCHAIN = 'leanprover/lean4:v4.34.0-rc1'
BRANCH = 'pin-b718-de5ce8a9'
OWNER = 'psinary-sketch'
ROWS = os.path.join(D_, 'b718_pin_rows.json')


def g(repo, *a, inp=None):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, input=inp)
    return r.returncode, r.stdout.decode('utf-8', 'replace'), r.stderr.decode('utf-8', 'replace')


def gs(repo, *a):
    return g(repo, *a)[1].strip()


def show(repo, rev, path):
    c, o, _e = g(repo, 'show', '%s:%s' % (rev, path))
    return o if c == 0 else None


def lakefile(repo, rev):
    for f in ('lakefile.lean', 'lakefile.toml'):
        t = show(repo, rev, f)
        if t is not None:
            return f, t
    return None, None


def plan():
    tgt = 'D:/' + TARGET_KERNEL
    tm = json.loads(show(tgt, 'HEAD', 'lake-manifest.json') or '{}')
    print('### THE TARGET KERNEL %s at %s: toolchain %s ; manifest packages %s' % (
        TARGET_KERNEL, gs(tgt, 'rev-parse', '--short=8', 'HEAD'), (show(tgt, 'HEAD', 'lean-toolchain') or '').strip(),
        [(p['name'], p.get('rev', '')[:12]) for p in tm.get('packages', [])]))
    for k in KERNELS:
        repo = 'D:/' + k
        if not os.path.isdir(repo):
            print('## %s : ABSENT at %s' % (k, repo))
            continue
        head = gs(repo, 'rev-parse', '--short=8', 'HEAD')
        main = gs(repo, 'rev-parse', '--short=8', 'main')
        br = gs(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        dirty = gs(repo, 'status', '--porcelain', '--untracked-files=no')
        lf, lt = lakefile(repo, 'main')
        req = [l.strip() for l in (lt or '').split(NL) if 'mathlib' in l.lower() or 'require' in l.lower() or 'rev' in l.lower()][:8]
        man = json.loads(show(repo, 'main', 'lake-manifest.json') or '{}')
        wfs = [f for f in gs(repo, 'ls-tree', '--name-only', 'main', '.github/workflows/').split(NL) if f.strip()]
        exists = gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH)
        print('## %s : HEAD %s on %s ; main %s ; tracked changes %s ; branch %s exists %s' % (k, head, br, main, bool(dirty), BRANCH, bool(exists)))
        print('   toolchain %s ; %s: %s' % ((show(repo, 'main', 'lean-toolchain') or '').strip(), lf, req))
        print('   manifest packages %s' % [(p['name'], p.get('rev', '')[:12], p.get('inherited')) for p in man.get('packages', [])])
        for w in wfs:
            t = show(repo, 'main', w) or ''
            on = re.search(r'(?ms)^on:\s*\n(.*?)^\S', t + '\nX')
            inputs = re.findall(r'^\s{6}(\w+):\s*$', on.group(1) if on else '', re.M)
            trig = re.findall(r'^\s{2}(\w+):', on.group(1) if on else '', re.M)
            print('   workflow %s : triggers %s ; inputs %s' % (w, trig, inputs))


HELD = {
    'SIDE-frobenius': 'no workflow on main (no build-module.yml): no dispatch is possible without a workflow edit, which is a repair',
    'SIDE-cosmo': 'lean_action_ci.yml runs on every push (any branch) with docgen-action and pages: write -- a branch push may publish '
                  'its pages (N5); not pushed',
}


def target_manifest():
    tgt = 'D:/' + TARGET_KERNEL
    return gs(tgt, 'rev-parse', '--short=8', 'HEAD'), json.loads(show(tgt, 'HEAD', 'lake-manifest.json'))


def full_rev(tm):
    m = [p for p in tm['packages'] if p['name'] == 'mathlib'][0]
    assert m['rev'].startswith(TARGET_REV), m['rev']
    return m['rev']


def bump_lakefile(lf, text, rev):
    """The Mathlib require's rev set to `rev`; every other byte kept. Returns (new text, count of replacements)."""
    if lf == 'lakefile.toml':
        parts = re.split(r'(?m)^(?=\[\[)', text)
        n = 0
        for i, p in enumerate(parts):
            if p.startswith('[[require]]') and re.search(r'(?m)^name\s*=\s*"mathlib"', p):
                p2, k = re.subn(r'(?m)^(rev\s*=\s*)"[^"]*"', lambda m: m.group(1) + '"%s"' % rev, p)
                parts[i], n = p2, n + k
        return ''.join(parts), n
    return re.subn(r'(require\s+(?:«mathlib»|mathlib)\b[^@]*?@\s*)"[^"]*"', lambda m: m.group(1) + '"%s"' % rev, text, flags=re.S)


def bump_manifest(km, tm, rev):
    """The kernel's manifest with its own top-level fields and its own mathlib entry (url, scope) at `rev`; the other packages the
    target's, in the target's order."""
    out = dict(km)
    pk = []
    for p in tm['packages']:
        if p['name'] == 'mathlib':
            own = [q for q in km.get('packages', []) if q['name'] == 'mathlib']
            q = dict(own[0] if own else p)
            q['rev'], q['inputRev'] = rev, rev
            pk.append(q)
        else:
            pk.append(dict(p))
    out['packages'] = pk
    return json.dumps(out, indent=1, ensure_ascii=False) + NL


def default_targets(lf, text):
    if lf == 'lakefile.toml':
        m = re.search(r'(?m)^defaultTargets\s*=\s*\[(.*?)\]', text)
        return re.findall(r'"([^"]+)"', m.group(1)) if m else []
    return [n.strip('«»') for n in re.findall(r'@\[default_target\]\s*lean_lib\s+(«[^»]+»|\S+)', text)]


def blob(repo, data):
    c, o, e = g(repo, 'hash-object', '-w', '--stdin', inp=data.encode('utf-8'))
    assert c == 0, e
    return o.strip()


def bump(k):
    repo = 'D:/' + k
    if k in HELD:
        print('## %s HELD: %s' % (k, HELD[k]))
        return
    if gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH):
        sys.exit('## %s: branch %s exists; nothing written' % (k, BRANCH))
    tshort, tm = target_manifest()
    rev = full_rev(tm)
    lf, lt = lakefile(repo, 'main')
    nlt, n = bump_lakefile(lf, lt, rev)
    if n != 1:
        sys.exit('## %s: the Mathlib require replaced %d times in %s (want 1); nothing written' % (k, n, lf))
    km = json.loads(show(repo, 'main', 'lake-manifest.json'))
    nm = bump_manifest(km, tm, rev)
    new = {'lean-toolchain': blob(repo, TOOLCHAIN + NL), lf: blob(repo, nlt), 'lake-manifest.json': blob(repo, nm)}
    rows, seen = [], set()
    for l in gs(repo, 'ls-tree', 'main').split(NL):
        meta, name = l.split('\t', 1)
        mode, typ, sha = meta.split()
        if name in new:
            sha, seen = new[name], seen | {name}
        rows.append('%s %s %s\t%s' % (mode, typ, sha, name))
    assert seen == set(new), seen
    c, tree, e = g(repo, 'mktree', inp=(NL.join(rows) + NL).encode('utf-8'))
    assert c == 0, e
    msg = ('b718 under (R328)(8): the federation pin\'s bump -- lean-toolchain to %s; the Mathlib require of %s and lake-manifest.json to '
           '%s, the manifest\'s other packages those of %s at %s; nothing else changed, nothing repaired' % (TOOLCHAIN, lf, rev, TARGET_KERNEL, tshort))
    c, cm, e = g(repo, 'commit-tree', tree.strip(), '-p', 'main', '-m', msg)
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = g(repo, 'branch', BRANCH, cm)
    assert c == 0, e
    print('## %s : %s at %s (parent main %s) ; default targets %s' % (k, BRANCH, cm[:10], gs(repo, 'rev-parse', '--short=8', 'main'),
                                                                   default_targets(lf, lt)))
    print(g(repo, 'diff', '--stat', 'main', cm)[1].rstrip())
    print(g(repo, 'diff', 'main', cm, '--', 'lean-toolchain', lf)[1].rstrip())


TARGETS = {'SIDE-kernel': 'Kernel Bridge MetaKernel',     # its build.yml's three libraries, b653's dispatch at ee8d21a
           'SIDE-interfaces': 'Kernel Interfaces'}         # its default target is an executable; its two libraries
MAX_DISPATCH = 12
DL = os.path.join(os.environ.get('TEMP', ROOT), 'b718_pin_artifacts')   # downloaded run artifacts: outside the relay, read as data


def free_mb():
    import ctypes

    class MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ullAvailPhys // (1024 * 1024)


HOLD_MB = 2560


def hold_or_exit(what):
    fm = free_mb()
    if fm < HOLD_MB:
        sys.exit('### free memory %d MB beneath the %d MB hold: %s refused; nothing done' % (fm, HOLD_MB, what))
    return fm


def procs():
    """The host's largest processes by working set, and any lean or lake process (N1); prints, writes nothing, stops nothing."""
    r = subprocess.run(['powershell', '-NoProfile', '-Command', 'Get-Process | Sort-Object WorkingSet64 -Descending'
                        ' | Select-Object -First 10 Name,Id,@{n="MB";e={[int]($_.WorkingSet64/1MB)}} | Format-Table -AutoSize | Out-String -Width 200'],
                       capture_output=True)
    print('### free memory %d MB (hold %d)' % (free_mb(), HOLD_MB))
    print(r.stdout.decode('utf-8', 'replace').rstrip())
    r = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True)
    names = sorted(set(l.split(',')[0].strip('"').lower() for l in r.stdout.decode('utf-8', 'replace').splitlines() if l.strip()))
    print('### lean or lake processes: %s' % ([n for n in names if n.startswith('lean') or n.startswith('lake')] or 'NONE'))


def gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace'), r.stderr.decode('utf-8', 'replace')


def rows_load():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def rows_add(row):
    rs = rows_load() + [row]
    t = json.dumps(rs, indent=1, ensure_ascii=False)
    io.open(ROWS + '.tmp', 'w', encoding='utf-8', newline='\n').write(t + NL)
    os.replace(ROWS + '.tmp', ROWS)


def target_of(k):
    if k in TARGETS:
        return TARGETS[k]
    lf, lt = lakefile('D:/' + k, 'main')
    return ' '.join(default_targets(lf, lt))


def dispatch(k):
    repo = 'D:/' + k
    done = [r for r in rows_load() if r.get('kind') == 'dispatch']
    if len(done) >= MAX_DISPATCH:
        sys.exit('dispatches %d: the ruling\'s twelve reached; nothing dispatched' % len(done))
    if [r for r in done if r['kernel'] == k]:
        sys.exit('## %s already dispatched; nothing dispatched' % k)
    sha = gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
    c, o, e = g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)
    if not o.startswith(sha):
        sys.exit('## %s: origin %s is %r, not the local %s; nothing dispatched' % (k, BRANCH, o.strip()[:12], sha[:12]))
    tgt = target_of(k)
    fm = hold_or_exit('the dispatch of ' + k)
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print('### free memory %d MB (hold %d) ; dispatching %s at main, ref %s, target %s' % (fm, HOLD_MB, k, sha[:12], tgt))
    c, o, e = gh('workflow', 'run', 'build-module.yml', '-R', '%s/%s' % (OWNER, k), '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + tgt)
    print('   gh workflow run: exit %d %s %s' % (c, o.strip(), e.strip()))
    if c != 0:
        sys.exit('dispatch refused; no row')
    rid = None
    for _i in range(12):
        time.sleep(5)
        c, o, e = gh('run', 'list', '-R', '%s/%s' % (OWNER, k), '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '-L', '5',
                     '--json', 'databaseId,createdAt,status')
        new = [r for r in json.loads(o or '[]') if r['createdAt'] >= t0]
        if new:
            rid = new[-1]['databaseId']
            break
    print('   run id %s (created at or after %s)' % (rid, t0))
    rows_add({'kind': 'dispatch', 'kernel': k, 'sha': sha, 'target': tgt, 'at': t0, 'run': rid, 'free_mb': free_mb()})


def stop():
    """The author's word at b718 (Option 2): C5 stopped where it stands, as (R328)(8) allows. Appends one row per kernel not dispatched --
    HELD with its reason, or CARRIED to b719 with its local branch tip (unpushed); the dispatched kernels' rows stand."""
    rs = rows_load()
    if [r for r in rs if r.get('kind') in ('held', 'carried')]:
        sys.exit('stop rows already banked; nothing written')
    disp = set(r['kernel'] for r in rs if r.get('kind') == 'dispatch')
    for k in KERNELS:
        if k in disp:
            continue
        repo = 'D:/' + k
        if k in HELD:
            rows_add({'kind': 'held', 'kernel': k, 'reason': HELD[k]})
            print('  %-22s HELD: %s' % (k, HELD[k]))
            continue
        sha = gs(repo, 'rev-parse', 'refs/heads/' + BRANCH)
        remote = g(repo, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)[1].strip()
        rows_add({'kind': 'carried', 'kernel': k, 'sha': sha, 'pushed': bool(remote), 'to': 'b719',
                  'reason': 'C5 stopped by the author\'s word (Option 2) on the free-memory hold; the local branch unpushed, carried'})
        print('  %-22s CARRIED to b719: local %s at %s ; on origin %s' % (k, BRANCH, sha[:10], bool(remote)))


def opening_errors(text, n=12):
    L = text.replace('\r', '').split(NL)
    idx = [i for i, l in enumerate(L) if re.search(r'(^|\s)error(:|\b)', l)]
    out = []
    for i in idx:
        out.extend(L[i:i + 3])
        if len(out) >= n:
            break
    return out[:n]


def read(k, rid):
    fm = hold_or_exit('the read of %s run %s' % (k, rid))
    print('### free memory %d MB (hold %d) ; reading %s run %s' % (fm, HOLD_MB, k, rid))
    R = '%s/%s' % (OWNER, k)
    c, o, e = gh('run', 'view', str(rid), '-R', R, '--json', 'status,conclusion,createdAt,updatedAt,headSha,event,url,jobs')
    v = json.loads(o) if c == 0 else {}
    print('   status %s conclusion %s ; %s -> %s ; event %s' % (v.get('status'), v.get('conclusion'), v.get('createdAt'), v.get('updatedAt'), v.get('event')))
    row = {'kind': 'read', 'kernel': k, 'run': rid, 'free_mb': fm, 'status': v.get('status'), 'conclusion': v.get('conclusion'),
           'created': v.get('createdAt'), 'updated': v.get('updatedAt'),
           'steps': [(s.get('name'), s.get('conclusion')) for j in v.get('jobs', []) for s in j.get('steps', [])]}
    if v.get('status') != 'completed':
        print('   not completed; no row')
        return
    d = os.path.join(DL, '%s_%s' % (k, rid))
    if not os.path.isdir(d):
        os.makedirs(d)
        c, o, e = gh('run', 'download', str(rid), '-R', R, '-D', d)
        print('   artifact download: exit %d %s' % (c, e.strip()[:200]))
    f = {}
    for root, _ds, fs in os.walk(d):
        for n in fs:
            f[n] = os.path.join(root, n)

    def txt(n):
        return io.open(f[n], encoding='utf-8', errors='replace').read() if n in f else None
    ref, ex, log, mem, ax = txt('ref.txt'), txt('build_exit.txt'), txt('build.log') or '', txt('mem.log') or '', txt('axioms.txt') or ''
    low = re.findall(r'^LOW (\S+)', mem, re.M)
    stop = re.findall(r'^STOP .*$', mem, re.M)
    errs = opening_errors(log)
    row.update({'ref': (ref or '').split(), 'build_exit': (ex or '').strip(), 'mem_low_mb': low[-1] if low else None, 'stops': stop,
                'error_lines': errs, 'log_lines': log.count(NL), 'sorry_warnings': len(re.findall(r'declaration uses .sorry.', log)),
                'axioms_lines': [l for l in ax.replace('\r', '').split(NL) if l.strip()][:80]})
    verdict = 'BUILDS' if row['build_exit'] == '0' and not stop else ('HELD (BREAKS)' if row['build_exit'] not in ('', None) else 'NO EXIT READ')
    row['verdict'] = verdict
    print('   ref %s ; build exit %r ; memory low %s MB ; stops %d ; log lines %d ; sorry warnings %d ; VERDICT %s' % (
        row['ref'], row['build_exit'], row['mem_low_mb'], len(stop), row['log_lines'], row['sorry_warnings'], verdict))
    for l in errs:
        print('     | ' + l[:220])
    rows_add(row)


def bank():
    rs = rows_load()
    disp = [r for r in rs if r['kind'] == 'dispatch']
    reads = {}
    for r in rs:
        if r['kind'] == 'read':
            reads[r['kernel']] = r
    out = ['b718 -- (R328)(8): THE FEDERATION PIN, LAST AND STOPPABLE -- one branch per kernel at Mathlib %s (%s), each build dispatched to the '
           'hosted runner and read by its run id (%s)' % (TARGET_REV, TOOLCHAIN, time.strftime('%Y-%m-%d', time.gmtime())), '',
           '### Written by tools/b718_pin.py bank from data/b718_pin_rows.json (the rows its dispatch and read routes appended). The bump commits made',
           '### by git plumbing on main\'s tree (lean-toolchain, the lakefile\'s Mathlib require, lake-manifest.json from %s\'s); no kernel\'s main' % TARGET_KERNEL,
           '### touched, no tag cut, nothing repaired; no lean or lake process on this host.', '',
           'DISPATCHES %d (of twelve at most) ; READ %d ; BUILDS %d ; HELD (BREAKS) %d ; HELD WITHOUT DISPATCH %d ; NOT READ %d' % (
               len(disp), len(reads), sum(1 for r in reads.values() if r['verdict'] == 'BUILDS'),
               sum(1 for r in reads.values() if r['verdict'].startswith('HELD')), len(HELD), len(disp) - len(reads)), '']
    for k in KERNELS:
        if k in HELD:
            out.append('  %-22s HELD WITHOUT DISPATCH: %s' % (k, HELD[k]))
            continue
        d = [r for r in disp if r['kernel'] == k]
        if not d:
            cr = [r for r in rs if r['kind'] == 'carried' and r['kernel'] == k]
            out.append('  %-22s CARRIED to b719: %s' % (k, ('local %s at %s, on origin %s -- %s' % (
                BRANCH, cr[0]['sha'][:10], cr[0]['pushed'], cr[0]['reason'])) if cr else 'not dispatched this act'))
            continue
        d = d[0]
        r = reads.get(k)
        if not r:
            out.append('  %-22s run %s at %s (target %s): NOT READ, carried' % (k, d['run'], d['sha'][:10], d['target']))
            continue
        out.append('  %-22s run %s at %s (target %s): %s %s ; build exit %s ; memory low %s MB ; sorry warnings %d ; host free %d MB at the read ; %s' % (
            k, r['run'], d['sha'][:10], d['target'], r['status'], r['conclusion'], r['build_exit'], r['mem_low_mb'], r['sorry_warnings'],
            r['free_mb'], r['verdict']))
        for l in r['error_lines']:
            out.append('      | ' + l[:220])
    t = NL.join(out) + NL
    j = json.dumps({'dispatch': disp, 'read': list(reads.values()), 'held': HELD}, indent=1, ensure_ascii=False) + NL
    io.open(os.path.join(D_, 'b718_pin.txt'), 'w', encoding='utf-8', newline='\n').write(t)
    io.open(os.path.join(D_, 'b718_pin.json'), 'w', encoding='utf-8', newline='\n').write(j)
    print(t)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['plan']:
        plan()
    elif len(a) == 2 and a[0] == 'bump' and a[1] in KERNELS:
        bump(a[1])
    elif len(a) == 2 and a[0] == 'dispatch' and a[1] in KERNELS and a[1] not in HELD:
        dispatch(a[1])
    elif len(a) == 3 and a[0] == 'read' and a[1] in KERNELS:
        read(a[1], a[2])
    elif a == ['bank']:
        bank()
    elif a == ['procs']:
        procs()
    elif a == ['stop']:
        stop()
    else:
        sys.exit(__doc__)
