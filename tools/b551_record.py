# -*- coding: utf-8 -*-
"""b551_record.py -- THE TOOLCHAINS: THE FEDERATION TOOLCHAIN CENSUS; THE INTERFACES PIN COMPLETED; SIDE-GLOBAL-SECTION TAGGED;
THE WEIL-SIDE ALIGNMENT TRIALLED ON A BRANCH: THE RECORD, UNDER (R161).
### `python tools/b551_record.py reads | census | toolchains | iface_cost | iface_read | tag_read | rows | spiral_row | idc_line |
### trial_setup | trial_read | trial_price | findings | components | desk | trail`
### The builds, the tag, the pushes and the branch commands are the seat`s; this file runs the census`s `--no-build` and
### `lake env lean` probes under the network guard, reads every bank back and writes the lines. This file deletes nothing.
"""
import ast, glob, io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
DD = 'D:' + os.sep
PP = os.path.join(DD, 'MY-DOwnloads', 'PLACE-papers')
GS = os.path.join(DD, 'SIDE-global-section')
LV = os.path.join(DD, 'SIDE-lv-conservation')
EF = os.path.join(DD, 'SIDE-explicit-formula')
ML = os.path.join(DD, 'mathlib4')
TRIAL = os.path.join(DD, 'trial-b551-lv')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
IDC = os.path.join(PP, 'phase2', 'method', 'THE_IDENTITY_CHAIN.md')
SPIRAL = os.path.join(PP, 'SPIRAL_MAP.md')
CORR = os.path.join(GS, 'CORRESPONDENCE.md')
SCR = os.path.join(os.environ.get('B551_SCRATCH') or os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'), 'b551_probes')
NL = chr(10)
GS_TIP = '2e43315'
TAG = 'v0.2.0'
IFACE4 = ['FiniteInstanceIdentity', 'GlobalSection', 'LocalLimit', 'RestrictedTensorLayer1']
MISSING_MOD = 'Mathlib.LinearAlgebra.TensorProduct.Finiteness'
GUARD = {'HTTP_PROXY': 'http://127.0.0.1:9', 'HTTPS_PROXY': 'http://127.0.0.1:9', 'ALL_PROXY': 'http://127.0.0.1:9',
         'http_proxy': 'http://127.0.0.1:9', 'https_proxy': 'http://127.0.0.1:9', 'all_proxy': 'http://127.0.0.1:9',
         'GIT_ALLOW_PROTOCOL': 'file'}
PRIV = 'TECHNE-Core'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    d = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(os.path.join(D, n), 'wb').write(d)


def put_txt(n, lines):
    d = (NL.join(lines) + NL).encode('utf-8')
    open(os.path.join(D, n), 'wb').write(d)


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def cite(L, path, a, z, what, text=None):
    t = (text if text is not None else rd(path)).split(NL)
    rel = os.path.relpath(path, PP) if path.startswith(PP) else (os.path.relpath(path, ROOT) if path.startswith(ROOT) else path)
    L.append('### %s:%d-%d -- %s' % (rel.replace(os.sep, '/'), a, min(z, len(t)), what))
    L.extend('  :%d %s' % (i + 1, t[i][:700]) for i in range(a - 1, min(z, len(t))))
    L.append('')


# ------------------------------------------------------------------------------ THE FORTY-FIVE NAMES (READING (1))
def literal(path, name):
    tree = ast.parse(rd(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return node, node.lineno, node.end_lineno
    raise KeyError(name)


def names():
    """### b542`s REPOS (PRIV resolved to its string) and b546`s EIGHT, read as literals from the tools` own text -- no import."""
    p542, p546 = os.path.join(T, 'b542_record.py'), os.path.join(T, 'b546_record.py')
    node, a, z = literal(p542, 'REPOS')
    reps = []
    for elt in node.value.elts:
        first = elt.elts[0]
        nm = PRIV if isinstance(first, ast.Name) else first.value
        cited = elt.elts[1].value if isinstance(elt.elts[1], ast.Constant) else None
        needle = elt.elts[2].value if isinstance(elt.elts[2], ast.Constant) else None
        reps.append(dict(name=nm, cited=cited, needle=needle, source='b542'))
    n2, a2, z2 = literal(p546, 'EIGHT')
    for elt in n2.value.elts:
        reps.append(dict(name=elt.value, cited=None, needle=None, source='b546'))
    return reps, (a, z), (a2, z2)


def repo_path(n):
    return os.path.join(DD, 'MY-DOwnloads', 'TECHNE-Core') if n == PRIV else os.path.join(DD, n)


# ------------------------------------------------------------------------------ STATIC FACTS (READING (2))
def manifest(p):
    f = os.path.join(p, 'lake-manifest.json')
    if not os.path.exists(f):
        return None
    return json.loads(rd(f))


def mathlib_entry(m):
    for pk in (m or {}).get('packages', []):
        if pk.get('name') == 'mathlib':
            return pk
    return None


def lakefile(p):
    for f in ('lakefile.lean', 'lakefile.toml'):
        if os.path.exists(os.path.join(p, f)):
            return f
    return None


def libs(p):
    """### every lean_lib: its name, its `roots`, its `globs` (submodule or `X.+` forms), as the lakefile writes them."""
    lf = lakefile(p)
    out = []
    if lf == 'lakefile.lean':
        t = rd(os.path.join(p, lf))
        t = re.sub(r'--[^\n]*', '', t)
        blocks = re.split(r'(?m)^(?=@\[|lean_lib|lean_exe|require|package)', t)
        for b in blocks:
            m = re.match(r'lean_lib\s+«?([\w.]+)»?', b)
            if not m:
                continue
            roots = re.findall(r'`([\w.]+)', (re.search(r'roots\s*:=\s*#\[([^\]]*)\]', b) or [None, ''])[1]) if re.search(r'roots\s*:=', b) else []
            globs = re.findall(r'\.submodules\s+`([\w.]+)', b) + re.findall(r'\.andSubmodules\s+`([\w.]+)', b)
            src = (re.search(r'srcDir\s*:=\s*"([^"]*)"', b) or [None, '.'])[1]
            out.append(dict(name=m.group(1), roots=roots, globs=globs, src=src))
    elif lf == 'lakefile.toml':
        t = rd(os.path.join(p, lf))
        for b in t.split('[[lean_lib]]')[1:]:
            b = b.split('[[')[0]
            nm = re.search(r'name\s*=\s*"([^"]+)"', b).group(1)
            roots = re.findall(r'"([\w.]+)"', (re.search(r'roots\s*=\s*\[([^\]]*)\]', b) or [None, ''])[1]) if 'roots' in b else []
            globs = [x[:-2] for x in re.findall(r'"([\w.]+\.\+)"', (re.search(r'globs\s*=\s*\[([^\]]*)\]', b) or [None, ''])[1])] if 'globs' in b else []
            src = (re.search(r'srcDir\s*=\s*"([^"]*)"', b) or [None, '.'])[1]
            out.append(dict(name=nm, roots=roots, globs=globs, src=src))
    return out


def modfile(p, src, mod):
    return os.path.join(p, src, *mod.split('.')) + '.lean'


def root_targets(p):
    """### READING (3): the roots each lib names, else its own name, when the file exists; a glob-only lib with no root file is
    ### probed through a scratch file importing every module its glob covers; a lib with neither is ROOT ABSENT."""
    out = []
    for lb in libs(p):
        roots = lb['roots'] or [lb['name']]
        have = [r for r in roots if os.path.exists(modfile(p, lb['src'], r))]
        if have:
            out += [dict(lib=lb['name'], kind='root', module=r, file=modfile(p, lb['src'], r)) for r in have]
        elif lb['globs']:
            mods = []
            for gl in lb['globs']:
                base = os.path.join(p, lb['src'], *gl.split('.'))
                for f in sorted(glob.glob(os.path.join(base, '**', '*.lean'), recursive=True)):
                    rel = os.path.relpath(f, os.path.join(p, lb['src']))[:-5]
                    mods.append(rel.replace(os.sep, '.'))
            out.append(dict(lib=lb['name'], kind='probe', module='%s (probe of %d glob modules)' % (lb['name'], len(mods)), mods=mods))
        else:
            out.append(dict(lib=lb['name'], kind='absent', module=roots[0]))
    return out


def checkouts():
    cands = [ML, os.path.join(DD, 'MY-DOwnloads', 'mathlib4'), os.path.join(DD, 'mathlib4-e960b84-tmp'),
             os.path.join(DD, 'MY-DOwnloads', '.lake', 'packages', 'mathlib')]
    cands += sorted(glob.glob(os.path.join(DD, 'SIDE-*', '.lake', 'packages', 'mathlib')))
    cands += sorted(glob.glob(os.path.join(DD, 'MY-DOwnloads', '*', '.lake', 'packages', 'mathlib')))
    out = []
    for c in cands:
        if os.path.isdir(c):
            out.append(dict(path=c, head=g(c, 'rev-parse', 'HEAD').strip(),
                            toolchain=(rd(os.path.join(c, 'lean-toolchain')).strip() if os.path.exists(os.path.join(c, 'lean-toolchain')) else '')))
    return out


def spiral_pin(rep, spiral_lines):
    if rep['source'] == 'b546':
        for i, l in enumerate(spiral_lines, 1):
            if l.startswith('| `%s` *(added by b546)*' % rep['name']):
                m = re.search(r'HEAD `([0-9a-f]{7})`', l)
                return dict(pin=m.group(1) if m else None, line=i, needle=l[:80])
        return dict(pin=None, line=None, needle=None)
    if not rep['cited']:
        return dict(pin=None, line=None, needle=rep['needle'])
    hit = [i for i, l in enumerate(spiral_lines, 1) if rep['needle'] and rep['needle'] in l]
    return dict(pin=rep['cited'], line=hit[0] if hit else None, needle=rep['needle'])


def static():
    reps, _, _ = names()
    sp = rd(SPIRAL).split(NL)
    cos = checkouts()
    rows = []
    for rep in reps:
        p = repo_path(rep['name'])
        m = manifest(p)
        me = mathlib_entry(m)
        imports = len([x for x in g(p, 'grep', '-l', '-E', r'^import Mathlib', 'HEAD', '--', '*.lean').split(NL) if x.strip()])
        tc = rd(os.path.join(p, 'lean-toolchain')).strip() if os.path.exists(os.path.join(p, 'lean-toolchain')) else 'NONE'
        head = g(p, 'rev-parse', 'HEAD').strip()
        rev = me['rev'] if me else None
        if rev:
            kind = 'MANIFEST'
        elif imports:
            kind = 'NO MANIFEST'
        else:
            kind = 'VANILLA'
        own = os.path.join(p, '.lake', 'packages', 'mathlib')
        own_head = g(own, 'rev-parse', 'HEAD').strip() if os.path.isdir(own) else ''
        declared = None
        if kind == 'NO MANIFEST' and rep['name'] == 'SIDE-global-section':
            rl = rd(os.path.join(p, 'README.md')).split(NL)
            li = [i for i, l in enumerate(rl, 1) if 'cecd0c4d56' in l]
            declared = dict(rev='cecd0c4d56', line=li[0] if li else None)
        want = rev or (declared or {}).get('rev')
        others = [c['path'] for c in cos if want and c['head'].startswith(want) and os.path.normcase(c['path']) != os.path.normcase(own)]
        pin = spiral_pin(rep, sp)
        at_pin = None
        if pin['pin'] and not head.startswith(pin['pin']):
            ref = pin['pin']
            ok = subprocess.run(['git', '-C', p, 'rev-parse', '--verify', '-q', ref + '^{commit}'], capture_output=True).returncode == 0
            if ok:
                ptc = g(p, 'show', '%s:lean-toolchain' % ref).strip() or 'NONE'
                pm = g(p, 'show', '%s:lake-manifest.json' % ref)
                try:
                    pme = mathlib_entry(json.loads(pm)) if pm.strip() else None
                except ValueError:
                    pme = None
                at_pin = dict(ref=ref, commit=g(p, 'rev-parse', ref + '^{commit}').strip(), toolchain=ptc, rev=(pme or {}).get('rev'))
            else:
                at_pin = dict(ref=ref, commit=None, toolchain=None, rev=None, note='the ref does not resolve locally')
        rows.append(dict(repo=rep['name'], source=rep['source'], path=p, head=head,
                         clean=g(p, 'status', '--porcelain', '--untracked-files=no').strip() == '',
                         toolchain=tc, kind=kind, rev=rev, declared=declared, mathlib_import_files=imports,
                         lakefile=lakefile(p), own_checkout=own_head, own_match=bool(rev) and own_head == rev, other_checkouts=others,
                         targets=[{k: v for k, v in t.items() if k != 'mods'} for t in root_targets(p)] if lakefile(p) else [],
                         spiral=pin, at_pin=at_pin, private=rep['name'] == PRIV))
    dirs = sorted(os.path.basename(x) for x in glob.glob(os.path.join(DD, 'SIDE-*')) if os.path.isdir(x))
    extra = sorted(set(dirs) - set(r['repo'] for r in rows))
    return rows, cos, dirs, extra


# ------------------------------------------------------------------------------ THE RUNS (READINGS (3)-(5))
RUNS = os.path.join(D, 'b551_census_runs.jsonl')


def done_keys():
    if not os.path.exists(RUNS):
        return set()
    return set(json.loads(l)['key'] for l in rd(RUNS).split(NL) if l.strip())


def classify(out):
    m = re.search(r"object file (\S+) of module ([\w.'«»]+) does not exist", out)
    if m:
        mod = m.group(2)
        return 'MISSING %s %s' % ('MATHLIB' if mod.startswith('Mathlib') else 'OWN', mod)
    if re.search(r'(?i)proxy|could not resolve|failed to connect|protocol .* is not allowed|transport .* not allowed', out):
        return 'FETCH REFUSED BY THE GUARD'
    m = re.search(r'(?m)^.*error.*$', out)
    return 'ERROR: %s' % m.group(0).strip()[:300] if m else 'NO ERROR LINE'


def run_one(key, cmd, cwd, private, timeout):
    env = dict(os.environ, **GUARD)
    t0 = time.time()
    try:
        r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, timeout=timeout)
        rc, out = r.returncode, (r.stdout + r.stderr).decode('utf-8', 'replace').replace(chr(13), '')
    except subprocess.TimeoutExpired as e:
        rc, out = 'TIMEOUT', ((e.stdout or b'') + (e.stderr or b'')).decode('utf-8', 'replace')
    rec = dict(key=key, cmd=cmd if not private else [c if not c.endswith('.lean') else '<a root of the private repository>' for c in cmd],
               cwd=cwd, rc=rc, secs=round(time.time() - t0, 1), guard=sorted(GUARD), cls=classify(out) if rc != 0 else 'OK',
               head=[] if private else out.split(NL)[:25], tail=[] if private else out.split(NL)[-25:],
               lines=len(out.split(NL)), ended=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    if private and rec['cls'].startswith(('ERROR', 'MISSING')):
        rec['cls'] = rec['cls'].split(' ')[0] + ' (private repository: detail withheld)'
    with open(RUNS, 'ab') as fh:
        fh.write((json.dumps(rec, ensure_ascii=False) + NL).encode('utf-8'))
        fh.flush()
        os.fsync(fh.fileno())
    print('  %-58s rc %-7s %7.1f s  %s' % (key[:58], rc, rec['secs'], rec['cls'][:90]), flush=True)
    return rec


def census():
    rows, cos, dirs, extra = static()
    put_json('b551_census_static.json', dict(rows=rows, checkouts=cos, side_dirs=dirs, extra=extra,
                                             taken=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    os.makedirs(SCR, exist_ok=True)
    have = done_keys()
    print('### static facts banked: %d rows ; %d SIDE-* directories ; not among the names: %s' % (len(rows), len(dirs), extra or 'NONE'), flush=True)
    for r in rows:
        if r['lakefile']:
            k = '%s | lake build --no-build' % r['repo']
            if k not in have:
                run_one(k, ['lake', 'build', '--no-build'], r['path'], r['private'], 1800)
    for r in rows:
        if not r['lakefile'] or r['kind'] == 'VANILLA':
            continue
        for t in root_targets(r['path']):
            k = '%s | lake env lean | %s | %s' % (r['repo'], t['lib'], t['module'])
            if k in have or t['kind'] == 'absent':
                continue
            if t['kind'] == 'probe':
                f = os.path.join(SCR, '%s__%s.lean' % (re.sub(r'\W', '_', r['repo']), t['lib']))
                io.open(f, 'w', encoding='utf-8', newline=NL).write(NL.join('import ' + m for m in t['mods']) + NL)
            else:
                f = t['file']
            run_one(k, ['lake', 'env', 'lean', f], r['path'], r['private'], 5400)
    print('### census runs complete', flush=True)


# ------------------------------------------------------------------------------ THE READS
def manifest_rev_line(p):
    f = os.path.join(p, 'lake-manifest.json')
    if not os.path.exists(f):
        return None
    t = rd(f).split(NL)
    for i, l in enumerate(t):
        if '"name": "mathlib"' in l:
            for j in range(max(0, i - 12), min(len(t), i + 12)):
                if '"rev"' in t[j]:
                    k = j
            return k + 1, t[k].strip()
    return None


def reads():
    L = ['b551 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    reps, (a, z), (a2, z2) = names()
    cite(L, os.path.join(T, 'b542_record.py'), a, z, 'b542`s enumeration: REPOS (PRIV = TECHNE-Core, :25)')
    cite(L, os.path.join(T, 'b546_record.py'), a2, z2, 'b546`s eight: EIGHT')
    L.append('### the forty-five names: %d (b542 %d, b546 %d)' % (len(reps), sum(r['source'] == 'b542' for r in reps), sum(r['source'] == 'b546' for r in reps)))
    st = jl('b551_census_static.json')
    L += ['### D:\\SIDE-* directories: %d ; not among the names: %s' % (len(st['side_dirs']), st['extra'] or 'NONE'), '',
          '### each repository`s lean-toolchain and lake-manifest mathlib rev line, at HEAD:']
    for r in st['rows']:
        p = r['path']
        mr = manifest_rev_line(p)
        L.append('  %-34s HEAD %s clean %s ; lean-toolchain:1 %s ; %s' % (
            r['repo'], r['head'][:10], r['clean'], r['toolchain'],
            ('lake-manifest.json:%d %s' % mr) if mr else ('lake-manifest.json: no mathlib entry' if os.path.exists(os.path.join(p, 'lake-manifest.json')) else 'no lake-manifest.json')))
    sp = rd(SPIRAL).split(NL)
    L += ['', '### SPIRAL_MAP`s pin lines, one per repository whose pin it cites:']
    for r in st['rows']:
        ln = r['spiral']['line']
        L.append('  %-34s %s' % (r['repo'], ('SPIRAL_MAP.md:%d pin %s -- %s' % (ln, r['spiral']['pin'], sp[ln - 1][:180])) if ln else 'NONE'))
    L.append('')
    cite(L, os.path.join(D, 'b550_defects.txt'), 1, 4, 'b550`s defect (a): the missing olean, the split run')
    for f in ('b550_iface_check.txt', 'b550_iface_check_a.txt', 'b550_iface_check_b.txt'):
        t = rd(os.path.join(D, f)).split(NL)
        L += ['### relay data/%s:1 %s' % (f, t[0][:200])] + ['  :%d %s' % (i + 1, l[:220]) for i, l in enumerate(t) if 'does not exist' in l or l.startswith('exit') or l.startswith('real')] + ['']
    cite(L, os.path.join(GS, 'AXIOM_PRINTS_INTERFACES.txt'), 1, 36, 'the Interfaces bank (RestrictedTensorLayer1`s section names v4.29.0 at :33)')
    cite(L, os.path.join(GS, 'README.md'), 26, 41, 'SIDE-global-section README: the Interfaces, the declared pin, the build path')
    L += ['### SIDE-global-section Interfaces/ holds: %s' % sorted(os.listdir(os.path.join(GS, 'Interfaces'))), '']
    cw = rd(os.path.join(T, 'corr_row.py')).split(NL)
    wl = [i + 1 for i, l in enumerate(cw) if l.startswith('def write_row(')][0]
    cite(L, os.path.join(T, 'corr_row.py'), wl, wl + 3, 'the correspondence writer: relay tools/corr_row.py write_row (committed; the tool b542 used for rows 388-390)')
    corr = rd(CORR).split(NL)
    rows = [i for i, l in enumerate(corr) if re.match(r'^\| *(8[0-9]|90) *\|', l)]
    L.append('### SIDE-global-section CORRESPONDENCE.md rows 80-90 (the module each names):')
    for i in rows:
        c = corr[i].split('|')
        mods = sorted(set(re.findall(r'(\w+Shadow)', c[2] + c[3]))) or sorted(set(re.findall(r'Interfaces/(\w+)', c[3])))
        L.append('  :%d row %s -- %s -- %s' % (i + 1, c[1].strip(), mods, c[2].strip()[:160]))
    L += ['### its highest row number: %d' % max(int(m) for m in re.findall(r'(?m)^\| *(\d+) *\|', rd(CORR))), '']
    cite(L, OT, 11203, 11213, 'OPEN_TRAILS: the bridge`s toolchain item (b550)')
    L.append('### the Mathlib checkouts on D: (git rev-parse HEAD):')
    L += ['  %-62s %s %s' % (c['path'], c['head'], c['toolchain']) for c in st['checkouts']] + ['']
    for k in (LV, EF):
        lf = lakefile(k)
        t = rd(os.path.join(k, lf)).split(NL)
        L += ['### %s/%s : its require line(s)' % (os.path.basename(k), lf)] + ['  :%d %s' % (i + 1, l) for i, l in enumerate(t) if 'require' in l or '@ "' in l or 'rev =' in l]
        L.append('  lean-toolchain:1 %s ; lake-manifest.json:%d %s' % ((rd(os.path.join(k, 'lean-toolchain')).strip(),) + manifest_rev_line(k)))
    put_txt('b551_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: THE TABLE
def runs():
    return [json.loads(l) for l in rd(RUNS).split(NL) if l.strip()] if os.path.exists(RUNS) else []


def iface():
    return jl('b551_iface.json')


def stale(run):
    """### the targets Lake names as failing (its `✖` lines), read from the run record; empty for the private repository."""
    ts = []
    for l in run.get('head', []) + run.get('tail', []):
        m = re.match(r'^✖ \[\d+/\d+\] Building ([\w.]+)', l)
        if m and m.group(1) not in ts:
            ts.append(m.group(1))
    return (' -- stale: %s (%s)' % (', '.join(ts), 'MATHLIB' if any(t.startswith('Mathlib') for t in ts) else 'OWN')) if ts else ''


def why(run):
    m = re.search(r"import ([\w.]+) failed, environment already contains '([^']+)' from ([\w.]+)", run['cls'])
    if m:
        return 'PROBE CLASH, no object file missing: %s and %s both declare %s and cannot be imported together' % (m.group(3), m.group(1), m.group(2))
    return run['cls'].replace(SCR.replace(os.sep, '/'), '<scratch>')[:300]


def cells(r, R):
    rv = r['rev'] or (r['declared'] or {}).get('rev')
    if r['kind'] == 'VANILLA':
        rev, co = 'VANILLA', 'n/a'
    elif r['kind'] == 'NO MANIFEST':
        rev = 'NO MANIFEST; declared %s (README.md:%s)' % (rv, r['declared']['line'])
        co = 'elsewhere: %s' % ', '.join(r['other_checkouts']) if r['other_checkouts'] else 'NONE'
    else:
        rev = rv[:12]
        co = 'yes (own .lake/packages)' if r['own_match'] else ('elsewhere: %s' % ', '.join(r['other_checkouts']) if r['other_checkouts'] else 'NONE')
    if r['kind'] == 'VANILLA':
        ol = 'n/a (VANILLA)'
    elif r['repo'] == 'SIDE-global-section':
        ic = iface()
        ol = 'census: %d missing (%s) ; after Component 2: %s' % (
            len(jl('b551_iface_cost.json').get('missing', [])), ', '.join(jl('b551_iface_cost.json').get('missing', [])) or '-',
            ('olean built %s ; %s' % (ic.get('olean_present'), ', '.join('%s %s' % (k, 'elaborates' if v['exit'] == 0 else 'FAILS') for k, v in ic.get('files', {}).items()))) if ic else 'PENDING')
    else:
        rr = [x for x in R if x['key'].startswith(r['repo'] + ' | lake env lean |')]
        ab = [t for t in r['targets'] if t['kind'] == 'absent']
        bad = [x for x in rr if x['rc'] != 0]
        if not rr and not ab:
            ol = 'NOT RUN'
        else:
            ol = ('COMPLETE (%d root%s)' % (len(rr), '' if len(rr) == 1 else 's')) if not bad else 'NOT COMPLETE BY THE PROBE: ' + ' ; '.join('%s -> %s' % (x['key'].split(' | ')[2], why(x)) for x in bad)
            if ab:
                ol += ' ; ROOT ABSENT: %s' % ', '.join('%s (%s.lean)' % (t['lib'], t['module']) for t in ab)
    if not r['lakefile']:
        cb = 'NO LAKEFILE'
    else:
        x = [x for x in R if x['key'] == r['repo'] + ' | lake build --no-build']
        cb = 'NOT RUN' if not x else ('YES' if x[0]['rc'] == 0 else 'NO (exit %s): %s%s' % (x[0]['rc'], x[0]['cls'], stale(x[0])))
    pin = r['spiral']['pin'] or 'NONE'
    if r['spiral']['line']:
        pin += ' (SPIRAL_MAP.md:%d)' % r['spiral']['line']
    ap = r.get('at_pin')
    if ap and ap.get('commit'):
        diff = []
        if ap['toolchain'] != r['toolchain']:
            diff.append('toolchain %s' % ap['toolchain'])
        if (ap['rev'] or None) != (r['rev'] or None):
            diff.append('mathlib %s' % ((ap['rev'] or 'none')[:12]))
        pin += ' ; at the pin: %s' % ('; '.join(diff) if diff else 'same toolchain and rev as HEAD')
    elif ap:
        pin += ' ; %s' % ap.get('note')
    return dict(repo=r['repo'] + (' (private)' if r['private'] else ''), toolchain=r['toolchain'], rev=rev, checkout=co, oleans=ol, cache=cb, pin=pin)


def toolchains():
    st, R = jl('b551_census_static.json'), runs()
    tab = [cells(r, R) for r in st['rows']]
    cols = ('repo', 'toolchain', 'rev', 'checkout', 'oleans', 'cache', 'pin')
    heads = ('repository', 'lean-toolchain', 'Mathlib rev', 'checkout on D:', 'oleans (lake env lean, roots)', 'lake build from cache', 'SPIRAL_MAP pin')
    L = ['b551 -- COMPONENT 1: THE FEDERATION TOOLCHAIN CENSUS (READINGS (1)-(6)), every repository at HEAD, every cell printed', '',
         '### the network guard on every lake run: %s' % ', '.join('%s=%s' % kv for kv in sorted(GUARD.items())), '',
         ' | '.join(heads)]
    for c in tab:
        L.append(' | '.join(c[k] for k in cols))
    groups = {}
    for r in st['rows']:
        if r['kind'] == 'VANILLA':
            continue
        rv = (r['rev'] or (r['declared'] or {}).get('rev'))[:10]
        groups.setdefault(rv, []).append(r['repo'] + (' (private)' if r['private'] else ''))
    nonv = [r for r in st['rows'] if r['kind'] != 'VANILLA']
    fails = [c['repo'] for c, r in zip(tab, st['rows']) if r['kind'] != 'VANILLA' and r['lakefile'] and c['cache'] != 'YES']
    nolf = [c['repo'] for c, r in zip(tab, st['rows']) if r['kind'] != 'VANILLA' and not r['lakefile']]
    vfails = [c['repo'] for c, r in zip(tab, st['rows']) if r['kind'] == 'VANILLA' and r['lakefile'] and c['cache'] != 'YES']
    L += ['', '### rows %d ; VANILLA %d ; non-VANILLA %d' % (len(tab), len(st['rows']) - len(nonv), len(nonv)),
          '### ### **DISTINCT MATHLIB REVS AMONG NON-VANILLA REPOSITORIES : %d**' % len(groups)]
    L += ['    %s : %s' % (k, ', '.join(v)) for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))]
    L += ['### non-VANILLA repositories whose `lake build --no-build` is not YES : %d -- %s' % (len(fails), '; '.join(fails) or 'NONE'),
          '### non-VANILLA with no lakefile (no cache build exists to run) : %s' % ('; '.join(nolf) or 'NONE'),
          '### VANILLA repositories whose `lake build --no-build` is not YES : %d -- %s' % (len(vfails), '; '.join(vfails) or 'NONE'),
          '### the runs: %d, the guard on every one %s' % (len(R), all(set(GUARD) == set(x['guard']) for x in R)),
          '### the older and newer Weil-side kernels: SIDE-lv-conservation %s ; SIDE-explicit-formula %s' % (
              [r for r in st['rows'] if r['repo'] == 'SIDE-lv-conservation'][0]['rev'][:12], [r for r in st['rows'] if r['repo'] == 'SIDE-explicit-formula'][0]['rev'][:12])]
    put_txt('b551_toolchains.txt', L)
    put_json('b551_toolchains.json', dict(table=tab, groups=groups, distinct=len(groups), fails=fails, nolakefile=nolf, vanilla_fails=vfails,
                                          runs=len(R), guarded=all(set(GUARD) == set(x['guard']) for x in R)))
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 2: THE INTERFACES PIN
def closure(ml, roots_):
    seen, stack = set(), list(roots_)
    while stack:
        m = stack.pop()
        if m in seen or not m.startswith('Mathlib'):
            continue
        seen.add(m)
        p = os.path.join(ml, *m.split('.')) + '.lean'
        if not os.path.exists(p):
            continue
        for l in open(p, encoding='utf-8', errors='replace'):
            mm = re.match(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([\w.]+)', l)
            if mm:
                stack.append(mm.group(1))
    return seen


def olean_of(ml, m):
    return os.path.join(ml, '.lake', 'build', 'lib', 'lean', *m.split('.')) + '.olean'


def iface_imports(files):
    out = []
    for f in files:
        out += [l.split()[1] for l in rd(os.path.join(GS, 'Interfaces', f + '.lean')).split(NL) if l.startswith('import Mathlib')]
    return sorted(set(out))


def own_imports(mod):
    return [m.group(1) for m in (re.match(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([\w.]+)', l)
                                 for l in rd(os.path.join(ML, *mod.split('.')) + '.lean').split(NL)) if m]


def iface_cost():
    four = iface_imports(IFACE4)
    six = iface_imports([f[:-5] for f in sorted(os.listdir(os.path.join(GS, 'Interfaces')))])
    c4, c6 = closure(ML, four), closure(ML, six)
    miss4 = sorted(m for m in c4 if not os.path.exists(olean_of(ML, m)))
    miss6 = sorted(m for m in c6 if not os.path.exists(olean_of(ML, m)))
    L = ['b551 -- COMPONENT 2 (a): THE COST, PRINTED BEFORE THE BUILD (READING (7))', '',
         '### D:\\mathlib4 HEAD %s ; toolchain %s ; tracked tree clean %s' % (g(ML, 'rev-parse', 'HEAD').strip(), rd(os.path.join(ML, 'lean-toolchain')).strip(),
                                                                          g(ML, 'status', '--porcelain', '--untracked-files=no').strip() == ''),
         '### the four files` Mathlib imports: %s' % four,
         '### their closure, read from source: %d modules ; with no olean: %d -- %s' % (len(c4), len(miss4), miss4),
         '### all six files` closure: %d modules ; with no olean: %d -- %s' % (len(c6), len(miss6), miss6),
         '### ### **THE COST: %d module%s to compile at cecd0c4 -- %s.**' % (len(miss4), '' if len(miss4) == 1 else 's', ', '.join(miss4) or 'none'),
         '### its own imports: %s' % own_imports(MISSING_MOD),
         '### each of them has an olean: %s' % all(os.path.exists(olean_of(ML, m)) for m in own_imports(MISSING_MOD) if m.startswith('Mathlib'))]
    put_txt('b551_iface_cost.txt', L)
    put_json('b551_iface_cost.json', dict(four=four, closure4=len(c4), missing=miss4, closure6=len(c6), missing6=miss6))
    print(NL.join(L))


def squash(t):
    return re.sub(r'\[([^\]]*)\]', lambda m: '[' + ' '.join(m.group(1).split()) + ']', t, flags=re.S)


def print_lines(t):
    return [l.strip() for l in squash(t).split(NL) if re.match(r"^'.+' (does not depend on any axioms|depends on axioms: \[)", l.strip())]


def bank_sections():
    out, cur = {}, None
    for l in rd(os.path.join(GS, 'AXIOM_PRINTS_INTERFACES.txt')).split(NL):
        m = re.match(r'^=== (\w+)', l)
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur and l.strip():
            out[cur].append(l.strip())
    return {k: print_lines(NL.join(v)) for k, v in out.items()}


def iface_read():
    bank = bank_sections()
    b = rd(os.path.join(D, 'b551_olean_build.txt'))
    files = {}
    for f in IFACE4:
        t = rd(os.path.join(D, 'b551_iface_%s.txt' % f))
        ex = re.search(r'(?m)^exit (\d+)', t)
        fresh = print_lines(t)
        errs = [l for l in t.split(NL) if re.search(r':\d+:\d+: error', l) or l.startswith('error:')]
        files[f] = dict(exit=int(ex.group(1)) if ex else None, header=t.split(NL)[0], fresh=fresh, bank=bank.get(f, []),
                        equal=fresh == bank.get(f, []), errors=errs[:5], real=[l for l in t.split(NL) if l.startswith('real')])
    olean = os.path.exists(olean_of(ML, MISSING_MOD))
    bex = re.search(r'(?m)^exit (\d+)', b)
    out = dict(olean_present=olean, build_exit=int(bex.group(1)) if bex else None, build_header=b.split(NL)[0],
               build_real=[l for l in b.split(NL) if l.startswith('real')], files=files,
               three_ok=all(files[f]['exit'] == 0 for f in IFACE4[:3]), rtl1=files['RestrictedTensorLayer1']['exit'] == 0,
               ml_head=g(ML, 'rev-parse', 'HEAD').strip(), ml_clean=g(ML, 'status', '--porcelain', '--untracked-files=no').strip() == '')
    L = ['b551 -- COMPONENT 2 (b)-(c): THE OLEAN BUILT, THE FOUR FILES ELABORATED AT cecd0c4 (READING (7))', '',
         '### the build: %s ; exit %s ; %s ; the olean now present: %s' % (out['build_header'], out['build_exit'], ' '.join(out['build_real']), olean),
         '### D:\\mathlib4 HEAD %s ; tracked tree clean %s' % (out['ml_head'], out['ml_clean']), '']
    for f in IFACE4:
        x = files[f]
        L += ['### %s : exit %s ; %s ; fresh prints %d ; bank prints %d ; LINE FOR LINE EQUAL %s' % (f, x['exit'], ' '.join(x['real']), len(x['fresh']), len(x['bank']), x['equal']),
              '    header: %s' % x['header']]
        L += ['    fresh: %s' % l for l in x['fresh']] + ['    bank : %s' % l for l in x['bank']] + ['    error: %s' % e[:300] for e in x['errors']]
    L += ['', '### RestrictedTensorLayer1 at cecd0c4: %s' % ('ELABORATES' if out['rtl1'] else 'DOES NOT ELABORATE -- a defect of the file`s declared pin; its v4.29.0 print stands'),
          '### the three other files elaborate: %s' % out['three_ok']]
    put_txt('b551_iface.txt', L)
    put_json('b551_iface.json', out)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 3: THE TAG, THE ROWS
def tag_read():
    t = rd(os.path.join(D, 'b551_tag.txt'))
    rem = dict((m.group(2), m.group(1)) for m in re.finditer(r'([0-9a-f]{40})\s+(refs/\S+)', t))
    before = re.search(r'### before: HEAD (\w+) ; status \(tracked\) \[(.*?)\]', t)
    after = re.search(r'### after: HEAD (\w+) ; status \(tracked\) \[(.*?)\]', t)
    local_peeled = re.search(r'peeled (\w+)', t).group(1)
    out = dict(remote_peeled=rem.get('refs/tags/%s^{}' % TAG), remote_tag=rem.get('refs/tags/' + TAG), remote_main=rem.get('refs/heads/main'),
               local_peeled=local_peeled, before_head=before.group(1), before_clean=before.group(2) == '', after_head=after.group(1),
               after_clean=after.group(2) == '', annotated=g(GS, 'cat-file', '-t', TAG).strip())
    out['n4'] = bool(out['remote_peeled']) and out['remote_peeled'].startswith(GS_TIP) and out['local_peeled'] == out['remote_peeled']
    put_json('b551_tag.json', out)
    print(json.dumps(out, indent=1))


AGG = 'AggregationCircularityShadow'


def agg_cells(num):
    ap = rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).split(NL)
    idx = [i + 1 for i, l in enumerate(ap) if l.startswith("'%s." % AGG)]
    names_ = [re.match(r"^'%s\.([^']+)'" % AGG, ap[i - 1]).group(1) for i in idx]
    allfree = all(ap[i - 1].endswith('does not depend on any axioms') for i in idx)
    tj = jl('b550_tiers.json')
    gr = {}
    for r in tj['rows']:
        if r['terminal'].startswith(AGG + '.'):
            gr[r['grade']] = gr.get(r['grade'], 0) + 1
    shell = [r['terminal'].split('.')[-1] for r in tj['rows'] if r['terminal'].startswith(AGG + '.') and r['grade'] == 'SHELL']
    first = g(GS, 'log', '--diff-filter=A', '--format=%h', '--', 'Core/%s.lean' % AGG).split()[-1]
    return [str(num),
            ('THE AGGREGATION’S FREEDOM, AND WHY C-WEIL CANNOT NARROW IT (b220; the row the ledger lacked, written at b551 under (R161)(4)): '
             'File E’s identity `T.value + Q.value = W.wInf - W.wPrimes` at a cell determines the quotient value uniquely; an aggregation '
             'satisfies C-WEIL iff it returns that forced value at every cell; such an aggregation exists; the proof that the identity '
             'holds for it is the C-WEIL hypothesis returned unchanged; without C-WEIL more than one aggregation is admitted, shown on Bool '
             'under XOR. ### **THE FILE DEFINES NO AGGREGATION** -- `agg` is a variable throughout and nothing is written into File E.'),
            '`Core/%s.lean` -- %d printed terminals: %s' % (AGG, len(names_), ', '.join('`%s`' % n for n in names_)),
            'all %d print *does not depend on any axioms* (%s) -- `AXIOM_PRINTS.txt` lines %d–%d, re-run from `AllPrints.lean` at b550 at HEAD `2e43315`, equal to the bank (relay `data/b550_allprints_run.txt`)'
            % (len(names_), 'every one' if allfree else 'NOT every one', idx[0], idx[-1]),
            ('no rubric grade is conferred by this row: b550 read these terminals in its tier table (relay `data/b550_tiers.txt`) as T2, '
             'ENCODES %d and SHELL %d (`%s`), in that table’s vocabulary' % (gr.get('ENCODES', 0), gr.get('SHELL', 0), '`, `'.join(shell))),
            ('Row written 2026-09-27 (b551) under (R161)(4), through `relay/tools/corr_row.py`. The module entered at b220 (`%s`) with no '
             'row; the Core shadows of rows 81–89 are the other eight modules (b550 defect (f)). Nothing re-proved, nothing re-graded.' % first)]


def rows_():
    import corr_row as CR
    have = CR.numbers_in(rd(CORR))
    num = max(have) + 1
    cells_ = agg_cells(num)
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells_, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = dict(number=num, cells=cells_, rc=r.returncode, stdout=r.stdout, rtl1_note=None)
    ic = iface()
    if ic and not ic.get('rtl1'):
        n2 = num + 1
        c2 = [str(n2), ('RESTRICTEDTENSORLAYER1 AT ITS DECLARED PIN (a note to row 80, b551 under (R161)(3)): the file does not elaborate '
                        'against mathlib4 `cecd0c4d56`, the pin README.md:29 declares for the Interfaces'),
              '`Interfaces/RestrictedTensorLayer1.lean` -- `Ftensor_sq`, `parityTensor_sq`, `tensorFactor` (row 80)',
              'the print banked at v4.29.0 (`AXIOM_PRINTS_INTERFACES.txt`:33-36) STANDS as its pin; the run at cecd0c4 is relay `data/b551_iface_RestrictedTensorLayer1.txt`',
              'unchanged from row 80; this row grades nothing', 'Written 2026-09-27 (b551). The pin is not moved to make the file pass.']
        r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + c2, capture_output=True, text=True, encoding='utf-8', errors='replace')
        out['rtl1_note'] = dict(number=n2, cells=c2, rc=r2.returncode, stdout=r2.stdout)
    put_json('b551_rows.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False)[:3000])


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def append_to(path, text):
    text = poss(text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    if live:
        sys.exit('### A BANNED STEM IN THE APPEND TO %s: %s' % (path, live))
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP).replace(os.sep, '/'), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, h):
    if poss(h).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


def line_of(path, head):
    ls = [i + 1 for i, l in enumerate(rd(path).split(NL)) if l.startswith(poss(head))]
    return ls[0] if ls else None


SPH = ('## 2C. SIDE-global-section pinned by b551 under (R161)(4) -- its first pin in this map (appended 2026-09-27; no byte above '
       'changes)')
IDL = '*Appended 2026-09-27 by b551, under the author`s ruling `(R161)`(4), to the tier block at :3170:*'
PRH = ('### `W-ORD-LI-WEIL-BRIDGE` -- THE TOOLCHAIN ITEM PRICED BY TRIAL (the item at :11203), appended 2026-09-27, b551, under the '
       'author`s ruling (R161)(5)')
FH = '## The toolchains: the federation census, the Interfaces pin completed, SIDE-global-section tagged, the Weil-side alignment trialled'
HEADING = ('### b551 — the toolchains under (R161): the federation census; the Interfaces pin completed; SIDE-global-section tagged '
           'v0.2.0; the Weil-side alignment trialled on a branch')


def spiral_row():
    guard_absent(SPIRAL, SPH)
    tg = jl('b551_tag.json')
    rw = jl('b551_rows.json')
    ic = iface()
    L = ['', '<!-- b551 (R161)(4) ROW, 2026-09-27 -->', '', SPH, '',
         '*Appended by b551 under the author`s ruling `(R161)`(4), the counterpart of `(R160)`(1). Before this block no line of this map '
         'cited a pin of SIDE-global-section (b550, relay `data/b550_reads.txt`). Adding a row confers no grade.*', '',
         '| Kernel | Pin | Subject (its README) | Note (b551) |', '|---|---|---|---|',
         '| `SIDE-global-section` *(pinned by b551)* | **`v0.2.0`** = `%s` (annotated; the peeled SHA read back from the remote) | the '
         'construction era’s verified Lean material for the global section (README.md:3) | Core vanilla at the toolchain `v4.29.1`; the '
         'Interfaces elaborate against mathlib4 `cecd0c4d56` (README.md:29), where the missing olean was built at b551 and %s; '
         'correspondence row %d (AggregationCircularityShadow) written after the tag |'
         % (tg['remote_peeled'][:7], ('all four of the order’s files elaborate' if ic.get('three_ok') and ic.get('rtl1') else
                                      'RestrictedTensorLayer1 does not elaborate there, its v4.29.0 print standing' if ic.get('three_ok') else 'see relay `data/b551_iface.txt`'),
            rw['number']), '', '*Filed by b551. No byte above this block changes.*', '']
    o = append_to(SPIRAL, NL.join(L))
    o['line'] = line_of(SPIRAL, SPH)
    put_json('b551_spiral.json', o)
    print('  SPIRAL_MAP :%s %s' % (o['line'], o))


def idc_line():
    guard_absent(IDC, IDL)
    rw = jl('b551_rows.json')
    corr = rd(CORR).split(NL)
    rows = []
    for l in corr:
        m = re.match(r'^\| *(8[1-9]) *\|', l)
        if m:
            c = l.split('|')
            mods = sorted(set(re.findall(r'(\w+Shadow)', c[2] + c[3])))
            rows.append((int(m.group(1)), mods))
    s = (IDL + ' the correspondence numbering, read from SIDE-global-section`s CORRESPONDENCE.md: %s. AggregationCircularityShadow, '
         'which had no row, is row %d (b551, written through `relay/tools/corr_row.py`). The "rows 81–89" of b550`s act entry '
         '(`FINDINGS.md`:5699) therefore carry eight modules, not nine. The repository is tagged `v0.2.0` at `2e43315`.'
         % ('; '.join('row %d %s' % (n, ' and '.join(ms)) for n, ms in rows), rw['number']))
    o = append_to(IDC, NL.join(['', s, '']))
    o['line'] = line_of(IDC, IDL)
    o['rows'] = rows
    put_json('b551_idc.json', o)
    print('  THE_IDENTITY_CHAIN :%s' % o['line'])
    print(poss(s))


# ------------------------------------------------------------------------------ COMPONENT 4: THE TRIAL
def trial_setup():
    """### writes the two files into the worktree the seat made: the newer kernel`s committed lean-toolchain bytes, and its committed
    ### manifest bytes with the top-level name line replaced by the older kernel`s. Then prints the diff against the branch point."""
    tc = subprocess.run(['git', '-C', EF, 'show', 'HEAD:lean-toolchain'], capture_output=True).stdout
    mf = subprocess.run(['git', '-C', EF, 'show', 'HEAD:lake-manifest.json'], capture_output=True).stdout.decode('utf-8')
    lvname = json.loads(subprocess.run(['git', '-C', LV, 'show', 'HEAD:lake-manifest.json'], capture_output=True).stdout.decode('utf-8'))['name']
    efname = json.loads(mf)['name']
    old = ' "name": "%s",' % efname
    assert mf.count(old) == 1, 'the name line'
    new_mf = mf.replace(old, ' "name": "%s",' % lvname).encode('utf-8')
    assert os.path.isdir(TRIAL) and g(TRIAL, 'rev-parse', '--abbrev-ref', 'HEAD').strip() == 'toolchain-trial-b551'
    open(os.path.join(TRIAL, 'lean-toolchain'), 'wb').write(tc)
    open(os.path.join(TRIAL, 'lake-manifest.json'), 'wb').write(new_mf)
    diff = g(TRIAL, 'diff', '--stat') + NL + g(TRIAL, 'diff')
    put_txt('b551_trial_diff.txt', ['b551 -- COMPONENT 4 (b): THE TRIAL BRANCH`S TWO FILES, AGAINST THE OLDER KERNEL`S MAIN (%s)' % g(LV, 'rev-parse', 'HEAD').strip(),
                                    '### the name kept: %s (the newer kernel`s was %s)' % (lvname, efname), ''] + diff.split(NL))
    print(diff[:6000])


def trial_read():
    t = rd(os.path.join(D, 'b551_trial_build.txt'))
    ex = re.search(r'(?m)^exit (\S+)', t)
    per = {}
    order = []
    for l in t.split(NL):
        m = re.search(r'error: (?:\./+)?([\w/\\.\-]+\.lean):(\d+):(\d+): (.*)', l)
        if m:
            f = m.group(1).replace('\\', '/').lstrip('./')
            if f not in per:
                per[f] = []
                order.append(f)
            per[f].append(l.strip())
    failed = re.findall(r'(?m)^[^\n]*✖ \[\d+/\d+\] Building ([\w.]+)', t)
    built_ml = re.findall(r'(?m)(?:✔|✖|Built|Building|Compiling)[^\n]*\b(Mathlib\.[\w.]+)', t)
    warn = [l.strip() for l in t.split(NL) if 'manifest out of date' in l or 'lake update' in l][:3]
    other = [l.strip() for l in t.split(NL) if l.strip().startswith('error:') and not re.search(r'\.lean:\d+:\d+:', l)][:10]
    mods_all = sorted('SIDELvConservation.' + os.path.relpath(f, os.path.join(TRIAL, 'SIDELvConservation'))[:-5].replace(os.sep, '.')
                      for f in glob.glob(os.path.join(TRIAL, 'SIDELvConservation', '**', '*.lean'), recursive=True))
    seen = set(re.findall(r'(?m)^[✔⚠✖] \[\d+/\d+\] (?:Built|Building|Replayed) (SIDELvConservation[\w.]*)', t))
    out_na = [m for m in mods_all if m not in seen]
    imp = {}
    for m in mods_all:
        f = os.path.join(TRIAL, *m.split('.')) + '.lean'
        imp[m] = [x.group(1) for x in (re.match(r'^\s*(?:public\s+)?import\s+([\w.]+)', l) for l in rd(f).split(NL)) if x]
    failed_mods = re.findall(r'(?m)^✖ \[\d+/\d+\] Building ([\w.]+)', t)

    def reaches(m, target, seen_=None):
        seen_ = seen_ or set()
        if m in seen_:
            return False
        seen_.add(m)
        return any(i == target or (i in imp and reaches(i, target, seen_)) for i in imp.get(m, []))
    downstream = sorted(m for m in out_na if any(reaches(m, fm) for fm in failed_mods))
    out = dict(exit=ex.group(1) if ex else None, header=t.split(NL)[0], real=[l for l in t.split(NL) if l.startswith('real')],
               lib_modules=len(mods_all), reported=sorted(seen), not_reported=out_na, downstream=downstream,
               modules=[dict(file=f, errors=len(per[f]), leading=per[f][0][:400]) for f in order], total=sum(len(v) for v in per.values()),
               failed_targets=failed, mathlib_compiled=sorted(set(built_ml)), warnings=warn, other_errors=other,
               lv_main=g(LV, 'rev-parse', 'main').strip(), lv_status=g(LV, 'status', '--porcelain', '--untracked-files=no').strip(),
               branch_tip=g(LV, 'rev-parse', 'toolchain-trial-b551').strip(),
               branch_files=sorted(x for x in g(LV, 'diff', '--name-only', 'main', 'toolchain-trial-b551').split(NL) if x.strip()))
    L = ['b551 -- COMPONENT 4 (c): THE TRIAL BUILD, READ (READING (10))', '', '### %s' % out['header'], '### exit %s ; %s' % (out['exit'], ' '.join(out['real'])),
         '### Lake`s warnings about the manifest: %s' % (out['warnings'] or 'NONE'),
         '### ### **ERRORS: %d IN %d MODULE%s.**' % (out['total'], len(order), '' if len(order) == 1 else 'S')]
    L += ['    %-60s %4d  %s' % (m['file'], m['errors'], m['leading']) for m in out['modules']]
    L += ['### failed build targets (Lake`s ✖ lines): %s' % (failed or 'NONE'),
          '### error lines without a source position: %s' % (other or 'NONE'),
          '### the library`s modules: %d ; reported by Lake (built, replayed or failed): %d ; NOT REPORTED (not attempted, or up to date and silent): %s'
          % (out['lib_modules'], len(out['reported']), out['not_reported'] or 'NONE'),
          '### of those, importing a failed module (transitively, by the library`s own import lines): %d -- %s ; the rest: %s' % (
              len(out['downstream']), out['downstream'] or 'NONE', sorted(set(out['not_reported']) - set(out['downstream'])) or 'NONE'),
          '### Mathlib modules Lake named as built or building: %d %s' % (len(out['mathlib_compiled']), out['mathlib_compiled'][:10]),
          '### the branch toolchain-trial-b551 at %s ; its files against main: %s' % (out['branch_tip'][:12], out['branch_files']),
          '### the older kernel`s main: %s ; tracked status [%s]' % (out['lv_main'], out['lv_status'])]
    put_txt('b551_trial.txt', L)
    put_json('b551_trial.json', out)
    print(NL.join(L))


def trial_price():
    guard_absent(OT, PRH)
    tr, st = jl('b551_trial.json'), jl('b551_toolchains.json')
    mods = tr['modules']
    L = ['', PRH, '',
         '**The toolchain item, priced by trial, not merged.** The older kernel, SIDE-lv-conservation (`lean-toolchain` `v4.29.1`, Mathlib '
         '`5e932f9`), was moved on a branch, `toolchain-trial-b551` (tip `%s`, pushed by name and HELD), to the newer kernel`s exact '
         '`lean-toolchain` and manifest -- SIDE-explicit-formula`s `v4.33.0-rc2` and Mathlib `51e6992`, 3421 Mathlib commits later '
         '(relay `data/b551_trial_revs.txt`) -- and `lake build` ran once (exit %s). No source line was edited; the lakefile still '
         'names `5e932f9`.' % (tr['branch_tip'][:7], tr['exit']), '',
         ('**The price: %d error%s in %d module%s** (relay `data/b551_trial.txt`):' % (tr['total'], '' if tr['total'] == 1 else 's', len(mods), '' if len(mods) == 1 else 's'))
         if mods else '**The price: no module errors** (relay `data/b551_trial.txt`); the build`s exit and its target lines are printed there.', '']
    L += ['- `%s`: %d -- the leading error: %s' % (m['file'], m['errors'], m['leading'].replace('`', '’').replace('|', '‖')[:300]) for m in mods]
    if tr.get('downstream'):
        L += ['', 'The count is a floor, not the whole price: %d of the library`s %d modules import the failed module and were not '
              'attempted (%s), so their errors, if any, are unmeasured. No Mathlib module was compiled; the copied packages were '
              'accepted as built.' % (len(tr['downstream']), tr['lib_modules'], ', '.join('`%s`' % d.split('.', 1)[1] for d in tr['downstream']))]
    L += ['', '*Appended beneath the toolchain item at :11203; nothing above changes. The merge is not done at this act; main of '
          'SIDE-lv-conservation is untouched.*', '']
    o = append_to(OT, NL.join(L))
    o['line'] = line_of(OT, PRH)
    put_json('b551_price.json', o)
    print('  OPEN_TRAILS price :%s' % o['line'])


# ------------------------------------------------------------------------------ COMPONENT 5: THE FINDINGS ENTRY
def findings():
    guard_absent(FIND, FH)
    st, ic, tg, rw, tr, pr, sp, idc = (jl('b551_toolchains.json'), iface(), jl('b551_tag.json'), jl('b551_rows.json'), jl('b551_trial.json'),
                                       jl('b551_price.json'), jl('b551_spiral.json'), jl('b551_idc.json'))
    L = ['', FH, '',
         '*Filed at b551 on the author`s ruling `(R161)`. The cascade pauses one act. Banks: relay `data/b551_toolchains.txt`, '
         '`data/b551_census_runs.jsonl`, `data/b551_iface_cost.txt`, `data/b551_iface.txt`, `data/b551_tag.txt`, `data/b551_trial.txt`.*', '',
         '**The census.** Forty-five repositories (b542`s thirty-six SIDE-* and TECHNE-Core, b546`s eight), read at HEAD, every cell '
         'printed in the bank. **%d distinct Mathlib revs** among the non-VANILLA repositories: %s.' % (
             st['distinct'], '; '.join('`%s` (%s)' % (k, ', '.join(v)) for k, v in sorted(st['groups'].items(), key=lambda kv: -len(kv[1])))), '',
         ('**Do not build from cache** (`lake build --no-build` under the network guard, not YES): %s. Every stale target Lake names '
          'is the repository`s own module; none is a Mathlib module, and no run attempted a fetch.' % ', '.join(st['fails']))
         if st['fails'] else '**Every non-VANILLA repository with a lakefile builds from cache.**',
         ('SIDE-global-section has no lakefile; its Core builds by `LEAN_PATH` and its Interfaces from a mathlib4 checkout (README.md:40).'
          if 'SIDE-global-section' in st['nolakefile'] else ''), '',
         '**The Interfaces pin, completed.** `%s` built at D:\\mathlib4 `cecd0c4` (exit %s); then, each file alone: %s. %s' % (
             MISSING_MOD, ic['build_exit'], '; '.join('%s %s (prints equal to the bank: %s)' % (f, 'elaborates' if v['exit'] == 0 else 'does NOT elaborate', v['equal'])
                                                      for f, v in ic['files'].items()),
             'RestrictedTensorLayer1`s declared pin is sound.' if ic['rtl1'] else 'RestrictedTensorLayer1 does not elaborate at its declared pin; its v4.29.0 print stands, noted at correspondence row %s.' % ((rw.get('rtl1_note') or {}).get('number'))), '',
         '**SIDE-global-section tagged.** `v0.2.0` at `%s`, annotated, the peeled SHA read back from the remote; SPIRAL_MAP.md:%s carries the pin; '
         'the AggregationCircularityShadow correspondence row is %d; the numbering note at THE_IDENTITY_CHAIN.md:%s.' % (
             tg['remote_peeled'][:7], sp.get('line'), rw['number'], idc.get('line')), '',
         '**The Weil-side alignment, trialled.** SIDE-lv-conservation on a branch at SIDE-explicit-formula`s toolchain and Mathlib: '
         '%s. Entered at OPEN_TRAILS.md:%s under the toolchain item at :11203; not merged.' % (
             ('%d error%s in %d module%s (%s); %d of the library`s %d modules import the failed module and were not attempted, so the '
              'count is a floor' % (tr['total'], '' if tr['total'] == 1 else 's', len(tr['modules']), '' if len(tr['modules']) == 1 else 's',
                                    ', '.join('`%s` %d' % (m['file'], m['errors']) for m in tr['modules']), len(tr.get('downstream', [])), tr.get('lib_modules', 0)))
             if tr['modules'] else 'no module errors, build exit %s' % tr['exit'], pr.get('line')), '',
         '**Next keystone:** THE_KEYSTONE_CENSUS.', '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited on any branch; nothing here is a statement about RH or about ζ’s zeros.*', '']
    o = append_to(FIND, NL.join(l for l in L if l is not None))
    o['line'] = line_of(FIND, FH)
    put_json('b551_findings.json', o)
    print('  FINDINGS :%s' % o['line'])


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE COMPONENTS, THE TRAIL
PRIOR_PP = '812cbe2'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md'}
MEMDIR = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'memory')
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def lean_changed_on_mains():
    out = {}
    for k, h in PRE_HEADS.items():
        p = os.path.join(DD, k)
        out[k] = sorted(x for x in g(p, 'diff', '--name-only', h, 'main').split(NL) if x.strip())
    return out


def scores():
    st, ic, tg, tr = jl('b551_toolchains.json'), iface(), jl('b551_tag.json'), jl('b551_trial.json')
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b551 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b551_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b551_')) if tk else None
    changed = lean_changed_on_mains()
    lean_on_mains = [(k, f) for k, v in changed.items() for f in v if f.endswith('.lean')]
    trial_lean = [f for f in tr.get('branch_files', []) if f.endswith('.lean')]
    gs_ok = set(changed.get('SIDE-global-section', [])) <= {'CORRESPONDENCE.md'}
    others_unmoved = all(not changed[k] for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula'))
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    files = ic.get('files', {})
    return dict(
        n1=st.get('distinct', 0) > 3,
        n2=len(st.get('fails', [])) >= 1,
        n3=bool(ic.get('olean_present')) and ic.get('build_exit') == 0 and bool(ic.get('three_ok')),
        n4=bool(tg.get('n4')),
        n5=len(tr.get('modules', [])) >= 1,
        n6=not lean_on_mains and not trial_lean and others_unmoved and gs_ok and not zen and tok == 0 and dep and all(pref.values()) and set(written) <= WRITE_OK,
        n6_literal_first_clause=not any(changed.values()),
        changed=changed, prefixes=pref, written=written, zen=zen, token=tok, deposit_clean=dep,
        s1=bool(files) and all(v['equal'] for v in files.values() if v['exit'] == 0),
        s2=bool(tg.get('remote_main')) and tg['remote_main'].startswith(GS_TIP),
        s3=bool(tr) and not tr.get('mathlib_compiled'))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    st, ic, tg, tr = jl('b551_toolchains.json'), iface(), jl('b551_tag.json'), jl('b551_trial.json')
    L = ['=' * 104, 'b551 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- distinct Mathlib revs among non-VANILLA repositories: %d -- %s.' % (
             w(sc['n1']), st['distinct'], '; '.join('%s (%d)' % (k, len(v)) for k, v in st['groups'].items())),
         '  **(N2)** ### **%s.** -- non-VANILLA repositories whose cache build is not YES: %s ; with no lakefile: %s.' % (
             w(sc['n2']), '; '.join(st['fails']) or 'NONE', '; '.join(st['nolakefile']) or 'NONE'),
         '  **(N3)** ### **%s.** -- the olean: build exit %s, present %s ; the three files other than RestrictedTensorLayer1: %s ; RestrictedTensorLayer1 (printed, not scored): %s.' % (
             w(sc['n3']), ic.get('build_exit'), ic.get('olean_present'), {f: ic['files'][f]['exit'] for f in IFACE4[:3]}, 'ELABORATES' if ic.get('rtl1') else 'DOES NOT ELABORATE'),
         '  **(N4)** ### **%s.** -- v0.2.0 at the remote: tag object %s, peeled %s ; local peeled %s.' % (w(sc['n4']), tg['remote_tag'], tg['remote_peeled'], tg['local_peeled']),
         '  **(N5)** ### **%s.** -- the trial: %d errors in %d modules ; %s.' % (
             w(sc['n5']), tr['total'], len(tr['modules']), '; '.join('%s %d: %s' % (m['file'], m['errors'], m['leading'][:140]) for m in tr['modules'][:6]) or 'build exit %s' % tr['exit']),
         '  **(N6)** ### **%s.** -- scored per READING (14): `.lean` changed on a kernel main NONE if %s ; the trial branch`s `.lean` paths %s ; mains moved %s '
         '(SIDE-global-section by CORRESPONDENCE.md only, ordered by (R161)(4)) ; nothing at Zenodo %s ; token %s ; deposit clean %s ; prefixes kept %s. '
         '### THE CONFLICT: its first clause read literally ("main of every repository unchanged") is %s.' % (
             w(sc['n6']), not any(f.endswith('.lean') for v in sc['changed'].values() for f in v), [f for f in tr.get('branch_files', []) if f.endswith('.lean')] or 'NONE',
             {k: v for k, v in sc['changed'].items() if v} or 'NONE', not sc['zen'], sc['token'], sc['deposit_clean'], sc['prefixes'], w(sc['n6_literal_first_clause'])),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- every elaborated Interfaces file against its bank section: %s.' % (w(sc['s1']), {f: v['equal'] for f, v in ic['files'].items() if v['exit'] == 0}),
         '  **(S2)** ### **%s.** -- the remote`s main of SIDE-global-section at the tag`s read-back: %s.' % (w(sc['s2']), tg['remote_main']),
         '  **(S3)** ### **%s.** -- Mathlib modules the trial build named as built: %d.' % (w(sc['s3']), len(tr.get('mathlib_compiled', []))),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b551_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b551_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b551_desk_notes.txt', L)
    put_json('b551_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b551 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b551_toolchains.txt', 'b551_iface_cost.txt', 'b551_iface.txt', 'b551_tag.txt', 'b551_trial_revs.txt', 'b551_trial_diff.txt', 'b551_trial.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b551_tag.json', 'b551_rows.json', 'b551_spiral.json', 'b551_idc.json', 'b551_price.json', 'b551_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['### THE BRANCHES : see data/b551_branches.txt', '=' * 132]
    put_txt('b551_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc, st, ic, tg, rw, tr, sp, idc, pr, fj = (scores(), jl('b551_toolchains.json'), iface(), jl('b551_tag.json'), jl('b551_rows.json'), jl('b551_trial.json'),
                                               jl('b551_spiral.json'), jl('b551_idc.json'), jl('b551_price.json'), jl('b551_findings.json'))
    body = ['', HEADING, '',
            '**(R161) ratified.** (1) The toolchains put in order once, before THE_KEYSTONE_CENSUS. (2) The census: forty-five '
            'repositories, seven columns, every cell printed. (3) The Interfaces pin completed at D:\\mathlib4 `cecd0c4`, not substituted. '
            '(4) SIDE-global-section tagged `v0.2.0` at `2e43315`; its SPIRAL_MAP row; the AggregationCircularityShadow row; the '
            'numbering note. (5) The Weil-side alignment trialled on `toolchain-trial-b551`, HELD, not merged. (6) THE_KEYSTONE_CENSUS next.', '',
            '**Entered:** FINDINGS.md:%s (the entry); SPIRAL_MAP.md:%s (the pin row); THE_IDENTITY_CHAIN.md:%s (the numbering line); '
            'OPEN_TRAILS.md:%s (the trial`s price under :11203); SIDE-global-section CORRESPONDENCE.md row %d.'
            % (fj['line'], sp['line'], idc['line'], pr['line'], rw['number']), '',
            '**The census:** %d distinct Mathlib revs among non-VANILLA repositories; not building from cache: %s. **The Interfaces:** the '
            'olean built (exit %s); %s. **The trial:** %s.' % (
                st['distinct'], ', '.join(st['fails']) or 'none', ic['build_exit'],
                ', '.join('%s %s' % (f, 'elaborates' if v['exit'] == 0 else 'does not elaborate') for f, v in ic['files'].items()),
                ('%d errors in %d modules' % (tr['total'], len(tr['modules']))) if tr['modules'] else 'no module errors, exit %s' % tr['exit']), '',
            '**CP-1:** open; the cascade resumes with THE_KEYSTONE_CENSUS.', '',
            '**Next:** THE_KEYSTONE_CENSUS.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane and no numerical lane opened at this act; one tag made; one trial branch held.** Nothing deposits; nothing at '
            'Zenodo written; no `.lean` file edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` '
            'where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b551_trail_notes.json', out)


rows = rows_


if __name__ == '__main__':
    fn = {k: v for k, v in globals().items() if callable(v) and k in (
        'reads', 'census', 'toolchains', 'iface_cost', 'iface_read', 'tag_read', 'rows', 'spiral_row', 'idc_line', 'trial_setup',
        'trial_read', 'trial_price', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(sorted(fn))))
    fn[sys.argv[1]]()
