# -*- coding: utf-8 -*-
"""b635_elab.py -- THE ELABORATED READER, CARRIED FROM tools/b634_elab.py BY SUBSTITUTION UNDER (R245): the grading reader for
### SIDE-explicit-formula from b635 ((R245)(2)); its rebuild and declaration compare pointed at the cascade of (R245)(4).
### b634's text follows, its bank names now b635's. W-ORD-GATE-FROM-ELABORATOR (OPEN_TRAILS :13000).

### For SIDE-explicit-formula at v0.25 = 8c51431: for each module of the kernel that a table row's statement lives in, a Lean file is
### generated that imports THAT MODULE ALONE, opens the namespaces of the declarations it reads, and runs a MetaM program printing,
### for each declaration the table names there:
###     DECL <the table's name> KIND <theorem|def|axiom|opaque|inductive|constructor|recursor|quot> HEADER <k> TOTAL <t>
###     BINDER <explicit|implicit|strict-implicit|instance> <name> : <type>      (one per header binder; a hygienic name marked ✝)
###     CONCL <the rest of the type>
###     END
### or `MISSING <name>` when the environment has no such constant. THE HEADER is the forall telescope up to the first EXPLICIT binder
### whose name is anonymous or hygienic -- how an arrow written in a conclusion elaborates -- so an arrow the text writes after its
### colon stays in the conclusion; TOTAL is the whole telescope. Section variables enter as Lean included them; auto-bound implicits
### appear under their names. Types print at full width, newlines joined.
### A table row with no statement is read in the first module (by path order) whose source at the pin names its last component by
### `git grep -w`; a name no module names is printed MISSING without a call.
### THE DRIVER (`run`) runs the calls one after another, each `lake env lean <file>` in the kernel's directory: the free-memory reading
### printed before each, none started beneath the hold (it waits, reads again every 30 s, and stops after ten minutes beneath it,
### banked); during a call the free memory is sampled every 2 s and the lowest kept; every call's exit, seconds and lowest reading
### banked in data/b635_elab_runs.json AS IT LANDS, so a stopped driver resumes at the first module not yet read. `join` writes
### data/b635_elab_types.txt from the calls' outputs. It writes nothing in the kernel; the generated files and logs are the scratchpad's.
### Usage: python tools/b635_elab.py plan | run | join | test
"""
import collections
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b635_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/89dd14e7-e119-4cf8-b592-ceaac809eff2/scratchpad'
WORK = os.path.join(SP, 'b635_elab')
RUNS = os.path.join(D, 'b635_elab_runs.json')
TYPES = os.path.join(D, 'b635_elab_types.txt')
WAIT_S, WAIT_MAX_S, SAMPLE_S = 30, 600, 2
VENDOR = 'Vendored/Bulka/'     # ### the vendored library's srcDir at the pin (lakefile.toml, b566)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRELUDE = r'''import Lean
open Lean Meta

def b635BinderKind : BinderInfo → String
  | .default => "explicit"
  | .implicit => "implicit"
  | .strictImplicit => "strict-implicit"
  | .instImplicit => "instance"

def b635Kind : ConstantInfo → String
  | .thmInfo _ => "theorem"
  | .defnInfo _ => "def"
  | .axiomInfo _ => "axiom"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"
  | .quotInfo _ => "quot"

def b635Flat (f : Format) : String :=
  " ".intercalate (((f.pretty 1000000).replace "\n" " ").splitOn " " |>.filter (· ≠ ""))

partial def b635Header : Expr → Nat → Nat
  | .forallE n _ b bi, k =>
    if bi == .default && (n.isAnonymous || n.hasMacroScopes) then k else b635Header b (k + 1)
  | _, k => k

partial def b635Total : Expr → Nat → Nat
  | .forallE _ _ b _, k => b635Total b (k + 1)
  | _, k => k

def b635Name (n : Name) : String :=
  if n.hasMacroScopes then toString n.eraseMacroScopes ++ "✝" else toString n

def b635N (xs : List String) : Name := xs.foldl Name.mkStr .anonymous

def b635Dump (label : String) (n : Name) : MetaM Unit := do
  match (← getEnv).find? n with
  | none => IO.println s!"MISSING {label}"
  | some ci =>
    let k := b635Header ci.type 0
    IO.println s!"DECL {label} KIND {b635Kind ci} HEADER {k} TOTAL {b635Total ci.type 0}"
    IO.println s!"MODULE {label} {(← findModuleOf? n).getD `this_file}"
    forallBoundedTelescope ci.type (some k) fun xs body => do
      for x in xs do
        let d ← x.fvarId!.getDecl
        IO.println s!"BINDER {b635BinderKind d.binderInfo} {b635Name d.userName} : {b635Flat (← ppExpr d.type)}"
      IO.println s!"CONCL {b635Flat (← ppExpr body)}"
    IO.println "END"

def b635Resolve (label : String) (n : Name) (home : Name) : MetaM Unit := do
  let env ← getEnv
  if (env.find? n).isSome then
    b635Dump label n
  else
    let last := n.componentsRev.head?
    let homeIdx := env.getModuleIdx? home
    let mut exact : Array Name := #[]
    let mut inMod : Array Name := #[]
    for (k, _) in env.constants.map₁.toList do
      let u := (privateToUserName? k).getD k
      if u.componentsRev.head? == last then
        if u == n then
          exact := exact.push k
        else if homeIdx.isSome && env.getModuleIdxFor? k == homeIdx then
          inMod := inMod.push k
    let c := if exact.size > 0 then exact else inMod
    let how := if exact.size > 0 then "private" else "module"
    if c.size == 1 then
      IO.println s!"RESOLVED {label} AS {c[0]!} BY {how}"
      b635Dump label c[0]!
    else
      IO.println s!"UNRESOLVED {label} CANDIDATES {c.size} {c.toList.take 5}"
      IO.println s!"MISSING {label}"
'''


def _lean_str(s):
    return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"')


def gen(module, names, path, opens=True, extra='', resolve=False):
    """### the Lean file for one module: its import, the prelude, the namespaces opened, any extra source, the dump of each name --
    ### with `resolve`, each name looked up as given, else as a private name's user name, else by its last component among the
    ### module's own constants when one alone matches (printed RESOLVED ... AS ... BY private|module)."""
    ns = set()
    for n in names:
        parts = n.split('.')
        for i in range(1, len(parts)):
            ns.add('.'.join(parts[:i]))
    lines = ['import %s' % module] + PRELUDE.split(NL)
    if opens and ns:
        lines.append('open %s' % ' '.join(sorted(ns, key=lambda x: (x.count('.'), x))))
    if extra:
        lines += extra.split(NL)
    lines.append('#eval show MetaM Unit from do')
    home = '(b635N [%s])' % ', '.join(_lean_str(p) for p in module.split('.'))
    for n in names:
        nm = '(b635N [%s])' % ', '.join(_lean_str(p) for p in n.split('.'))
        lines.append(('  b635Resolve %s %s %s' % (_lean_str(n), nm, home)) if resolve else ('  b635Dump %s %s' % (_lean_str(n), nm)))
    lines.append('')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline=NL).write(NL.join(lines))
    return path


def parse(text):
    """### the dump read back: {name: dict(kind, header, total, binders=[dict(kind, name, type)], concl, missing)}."""
    out, cur, res = {}, None, None
    for l in (text or '').replace(chr(13), '').split(NL):
        m = re.match(r'^DECL (\S+) KIND (\S+) HEADER (\d+) TOTAL (\d+)$', l)
        if m:
            cur = dict(kind=m.group(2), header=int(m.group(3)), total=int(m.group(4)), binders=[], concl='', missing=False, resolved_as=res)
            out[m.group(1)] = cur
            res = None
            continue
        m = re.match(r'^MISSING (\S+)$', l)
        if m:
            out[m.group(1)] = dict(kind=None, header=0, total=0, binders=[], concl='', missing=True, resolved_as=None)
            cur = None
            continue
        m = re.match(r'^RESOLVED (\S+) AS (\S+) BY (\S+)$', l)
        if m:
            res = (m.group(2), m.group(3))
            continue
        m = re.match(r'^UNRESOLVED (\S+) CANDIDATES (\d+)', l)
        if m:
            continue
        if cur is None:
            continue
        m = re.match(r'^MODULE (\S+) (\S+)$', l)
        if m:
            cur['module'] = m.group(2)
            continue
        m = re.match(r'^BINDER (explicit|implicit|strict-implicit|instance) (\S+) : (.*)$', l)
        if m:
            cur['binders'].append(dict(kind=m.group(1), name=m.group(2), type=m.group(3)))
        elif l.startswith('CONCL '):
            cur['concl'] = l[6:]
        elif l == 'END':
            cur = None
    return out


def load_bank():
    return parse(io.open(TYPES, encoding='utf-8').read()) if os.path.exists(TYPES) else {}


def free_mb():
    import chain_page as CP
    return CP.free_mb()


def _git(*a):
    r = subprocess.run(['git', '-C', K.KER] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def plan():
    """### the calls: {module: [names]} in path order, and the names no module names."""
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    E = [r for r in T if r['repo'] == K.KERNEL]
    mods = set(f[:-5] for f in _git('ls-tree', '-r', '--name-only', K.KER_PIN).split(NL)
               if f.endswith('.lean') and (f.startswith('SIDEExplicitFormula/') or f.startswith('Zeta23/') or f.startswith(VENDOR)))
    calls, missing, via = collections.OrderedDict(), [], {}
    for r in E:
        f = (r.get('statement_file') or '').split(':')[0]
        m = f[:-5] if f.endswith('.lean') else None
        if m is None or m not in mods:
            short = r['name'].split('.')[-1]
            hits = sorted(set(x.split(':', 2)[1][:-5] for x in _git('grep', '-l', '-w', '-F', short, K.KER_PIN, '--', '*.lean').split(NL)
                              if x.count(':') >= 1 and x.split(':', 2)[1][:-5] in mods))
            if not hits:
                missing.append(r['name'])
                continue
            m = hits[0]
            via[r['name']] = 'named by git grep in %s' % m
        calls.setdefault(m, []).append(r['name'])
    calls = collections.OrderedDict(sorted(calls.items()))
    return calls, missing, via, len(E)


def _module_name(m):
    """### a module's path at the pin to its Lean name; the vendored library's srcDir (lakefile.toml) is not part of the name."""
    return (m[len(VENDOR):] if m.startswith(VENDOR) else m).replace('/', '.')


def _runs():
    return json.load(io.open(RUNS, encoding='utf-8')) if os.path.exists(RUNS) else dict(calls=[], stopped=None)


def _put_runs(J):
    b = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(RUNS + '.tmp', 'wb').write(b)
    os.replace(RUNS + '.tmp', RUNS)


def call(module, names, tag, opens=True, extra='', resolve=False):
    """### ONE call: the free memory read before it (waiting beneath the hold), the lean process sampled until it exits."""
    fm = free_mb()
    waited = 0
    while 0 <= fm < K.HOLD_MB and waited < WAIT_MAX_S:
        print('  %s: free memory %d MB beneath the hold %d -- waiting' % (module, fm, K.HOLD_MB), flush=True)
        time.sleep(WAIT_S)
        waited += WAIT_S
        fm = free_mb()
    if 0 <= fm < K.HOLD_MB:
        return dict(module=module, tag=tag, free_before=fm, started=False, rc=None, seconds=0, low=None, waited=waited)
    src = gen(_module_name(module), names, os.path.join(WORK, tag + '.lean'), opens=opens, extra=extra, resolve=resolve)
    out = os.path.join(WORK, tag + '.out')
    print('  %s: free memory before the call %d MB (hold %d); %d names' % (module, fm, K.HOLD_MB, len(names)), flush=True)
    t0, low = time.time(), fm
    with open(out, 'wb') as fo:
        p = subprocess.Popen(['lake', 'env', 'lean', src.replace('/', os.sep)], cwd=K.KER, stdout=fo, stderr=subprocess.STDOUT)
        while p.poll() is None:
            time.sleep(SAMPLE_S)
            f = free_mb()
            if f >= 0:
                low = min(low, f)
    secs = int(time.time() - t0)
    text = open(out, 'rb').read().decode('utf-8', 'replace')
    got = parse(text)
    return dict(module=module, tag=tag, free_before=fm, started=True, rc=p.returncode, seconds=secs, low=low, waited=waited, opens=opens,
                names=len(names), read=sum(1 for n in names if n in got), out=out.replace('\\', '/'), resolve=resolve,
                resolved=sum(1 for n in names if n in got and not got[n]['missing']))


def resolve_missing(*a):
    """### the second pass: each module whose call printed a name MISSING called again for those names alone, each name resolved as
    ### `gen` with `resolve` reads it; every call banked beside the first pass's (resolve true), the first pass's kept."""
    calls, missing, via, n = plan()
    J = _runs()
    first = {}
    for c in J['calls']:
        if not c.get('superseded') and not c.get('resolve') and c.get('started'):
            first[c['module']] = c
    done = set(c['module'] for c in J['calls'] if c.get('resolve') and c.get('rc') == 0)
    for i, (m, names) in enumerate(calls.items(), 1):
        c0 = first.get(m)
        if not c0 or m in done:
            continue
        got = parse(open(c0['out'], 'rb').read().decode('utf-8', 'replace'))
        miss = [x for x in names if x not in got or got[x]['missing']]
        if not miss:
            continue
        c = call(m, miss, 'r%03d_%s' % (i, re.sub(r'[^A-Za-z0-9]+', '_', m)), opens=c0.get('opens', True), resolve=True)
        J['calls'].append(c)
        _put_runs(J)
        print('  resolve %s exit %s ; %s s ; low %s MB ; resolved %s of %s' % (m, c.get('rc'), c.get('seconds'), c.get('low'), c.get('resolved'),
                                                                         c.get('names')), flush=True)
        if not c.get('started'):
            print('### STOPPED beneath the hold before %s' % m, flush=True)
            return 3
    return 0


def run(*a):
    calls, missing, via, n = plan()
    J = _runs()
    done = set(c['module'] for c in J['calls'] if c.get('rc') == 0 and c.get('read') == c.get('names'))
    print('### b635_elab: %d rows of %s in %d calls; %d named by no module; %d calls already read' % (n, K.KERNEL, len(calls), len(missing), len(done)), flush=True)
    for i, (m, names) in enumerate(calls.items(), 1):
        if m in done:
            continue
        tag = 'm%03d_%s' % (i, re.sub(r'[^A-Za-z0-9]+', '_', m))
        c = call(m, names, tag)
        if c.get('started') and (c['rc'] != 0 or c['read'] != c['names']):
            J['calls'].append(dict(c, superseded=True))
            _put_runs(J)
            c = call(m, names, tag + '_noopen', opens=False)     # ### the namespaces' opening dropped once, the first call kept
        J['calls'].append(c)
        _put_runs(J)
        print('  [%d/%d] %s exit %s ; %d s ; low %s MB ; read %s of %s' % (i, len(calls), m, c.get('rc'), c.get('seconds'), c.get('low'),
                                                                     c.get('read'), c.get('names')), flush=True)
        if not c.get('started'):
            J['stopped'] = 'beneath the hold for ten minutes before %s' % m
            _put_runs(J)
            print('### STOPPED: %s' % J['stopped'], flush=True)
            return 3
    J['stopped'] = None
    J['missing_without_call'] = missing
    J['via_grep'] = via
    J['plan'] = dict(rows=n, calls=len(calls))
    _put_runs(J)
    return 0


def join(*a):
    calls, missing, via, n = plan()
    J = _runs()
    L = ['b635 -- COMPONENT 3: THE ELABORATED TYPES OF %s AT %s = %s, ONE MODULE`S DECLARATIONS PER CALL (%s)' % (
        K.KERNEL, K.KER_TAG, K.KER_PIN, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows of the kernel in the table %d ; calls planned %d ; named by no module %d' % (n, len(calls), len(missing)), '']
    final, second = {}, {}
    for c in J['calls']:
        if c.get('resolve'):
            if c.get('started'):
                second[c['module']] = c
        elif not c.get('superseded'):
            final[c['module']] = c
    seen = set()
    for m, names in calls.items():
        c = final.get(m)
        if not c or not c.get('started'):
            L.append('### MODULE %s -- ### NOT READ' % m)
            continue
        got = parse(open(c['out'], 'rb').read().decode('utf-8', 'replace'))
        L.append('### MODULE %s -- exit %s, %d s, free %d MB before, lowest %s MB, namespaces opened %s' % (
            m, c['rc'], c['seconds'], c['free_before'], c['low'], c.get('opens')))
        c2 = second.get(m)
        if c2:
            g2 = parse(open(c2['out'], 'rb').read().decode('utf-8', 'replace'))
            L.append('### SECOND PASS %s -- exit %s, %d s, free %d MB before, lowest %s MB ; resolved %s of %s' % (
                m, c2['rc'], c2['seconds'], c2['free_before'], c2['low'], c2.get('resolved'), c2.get('names')))
            for k, v in g2.items():
                if (k not in got or got[k]['missing']) and not v['missing']:
                    got[k] = v
        for nm in names:
            if nm in seen:
                continue
            seen.add(nm)
            e = got.get(nm)
            if e is None:
                L.append('MISSING %s' % nm)
                L.append('    ### the call printed nothing for this name')
                continue
            if e['missing']:
                L.append('MISSING %s' % nm)
                continue
            if e.get('resolved_as'):
                L.append('RESOLVED %s AS %s BY %s' % (nm, e['resolved_as'][0], e['resolved_as'][1]))
            L.append('DECL %s KIND %s HEADER %d TOTAL %d' % (nm, e['kind'], e['header'], e['total']))
            L += ['BINDER %s %s : %s' % (b['kind'], b['name'], b['type']) for b in e['binders']]
            L += ['CONCL %s' % e['concl'], 'END']
            if nm in via:
                L.append('    ### %s' % via[nm])
        L.append('')
    for nm in missing:
        L.append('MISSING %s' % nm)
        L.append('    ### no module of the kernel names it at the pin (git grep -w)')
    B = load_bank_text(NL.join(L))
    L.insert(3, '### ### **DECLARATIONS WITH A TYPE : %d ; MISSING : %d ; OF %d ROWS.**' % (
        sum(1 for v in B.values() if not v['missing']), sum(1 for v in B.values() if v['missing']), n))
    b = (NL.join(L) + NL).encode('utf-8')
    open(TYPES + '.tmp', 'wb').write(b)
    os.replace(TYPES + '.tmp', TYPES)
    print(L[3])


def load_bank_text(text):
    return parse(text)


# ================================================================================ b635: THE PASSES OF (R245)(2)-(3) AND THE STABLE BANK
B634_TYPES = os.path.join(D, 'b634_elab_types.txt')
STABLE = os.path.join(D, 'elab_types.txt')       # ### the generator's input after its edit (the author's first answer before b635's seal)
PASSES = os.path.join(D, 'b635_elab_passes.json')
LSERIES = ('LSeries_eq_mul_integral', 'Mathlib.NumberTheory.LSeries.SumCoeff')   # ### the one upstream name, its Mathlib module (git grep)


def _b634_plan_modules():
    """### b634's own plan: each kernel row's module of reading (its statement's file, else the first module naming it)."""
    calls, missing, via, n = plan()
    of = {}
    for m, names in calls.items():
        for x in names:
            of.setdefault(x, m)
    return of


def _passes():
    return json.load(io.open(PASSES, encoding='utf-8')) if os.path.exists(PASSES) else dict(calls=[])


def _put_passes(J):
    b = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(PASSES + '.tmp', 'wb').write(b)
    os.replace(PASSES + '.tmp', PASSES)


def _run_pass(kind, groups):
    """### one call per (import line, names) group, each banked as it lands in data/b635_elab_passes.json under `kind`."""
    J = _passes()
    done = set((c['kind'], c['module']) for c in J['calls'] if c.get('rc') == 0 and c.get('read') == c.get('names'))
    for i, (mod, names) in enumerate(groups, 1):
        if (kind, mod) in done:
            continue
        c = call(mod, names, '%s%03d_%s' % (kind, i, re.sub(r'[^A-Za-z0-9]+', '_', mod))[:120], resolve=True)
        c['kind'] = kind
        J['calls'].append(c)
        _put_passes(J)
        print('  %s %s exit %s ; %s s ; low %s MB ; read %s of %s ; typed %s' % (kind, mod, c.get('rc'), c.get('seconds'), c.get('low'),
                                                                            c.get('read'), c.get('names'), c.get('resolved')), flush=True)
        if not c.get('started'):
            print('### STOPPED beneath the hold before %s' % mod, flush=True)
            return 3
    return 0


def upstream(*a):
    """### (R245)(2), the author's second answer: the 35 statement-less rows b634's reader typed, read again with each constant's
    ### defining module printed, one call per module of b634's plan."""
    B = parse(io.open(B634_TYPES, encoding='utf-8').read())
    T = [r for r in json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'] if r['repo'] == K.KERNEL]
    names = [r['name'] for r in T if not r.get('statement') and r['name'] in B and not B[r['name']]['missing']]
    of = _b634_plan_modules()
    groups = collections.OrderedDict()
    for x in names:
        groups.setdefault(of[x], []).append(x)
    print('### b635 upstream pass: %d names in %d calls' % (len(names), len(groups)), flush=True)
    return _run_pass('upstream', [(_module_name(m), ns) for m, ns in groups.items()])


def rerun11(*a):
    """### (R245)(2): the elaborated reader on the eleven alone, ONE call importing their modules (data/b635_elab_rerun11.txt)."""
    of = _b634_plan_modules()
    mods = sorted(set(_module_name(of[x]) for x in K.ELEVEN))
    rc = _run_pass('rerun11', [('\nimport '.join(mods), list(K.ELEVEN))])
    J = _passes()
    c = [x for x in J['calls'] if x['kind'] == 'rerun11' and x.get('started')][-1]
    text = open(c['out'], 'rb').read().decode('utf-8', 'replace')
    open(os.path.join(D, 'b635_elab_rerun11.txt'), 'wb').write(('### b635 -- THE ELABORATED READER ON THE ELEVEN, ONE CALL (%s): imports %s ; exit %s ; '
                                                              '%s s ; free %s MB before, lowest %s MB%s' % (
                                                                  time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), mods, c['rc'], c['seconds'],
                                                                  c['free_before'], c['low'], NL) + text.replace(chr(13), '')).encode('utf-8'))
    return rc


def phantom_types(*a):
    """### (R245)(3): the full names the re-point map names, read in the module whose source at the pin declares each (git grep), and the
    ### upstream name in its Mathlib module; data/b635_phantom_types.json counts them."""
    RP = json.load(io.open(os.path.join(D, 'table_repoint.json'), encoding='utf-8'))['repoint']
    groups = collections.OrderedDict()
    for x in RP:
        short = x['new'].split('.')[-1]
        hits = sorted(set(h.split(':', 2)[1][:-5] for h in _git('grep', '-l', '-w', '-F', short, K.KER_PIN, '--', 'SIDEExplicitFormula/*.lean',
                                                                  'Zeta23/*.lean').split(NL) if h.count(':') >= 1))
        groups.setdefault(_module_name(hits[0]) if hits else 'SIDEExplicitFormula', []).append(x['new'])
    groups.setdefault(LSERIES[1], []).append(LSERIES[0])
    rc = _run_pass('phantom', list(groups.items()))
    J = _passes()
    got = {}
    for c in J['calls']:
        if c['kind'] == 'phantom' and c.get('started'):
            got.update({k: v for k, v in parse(open(c['out'], 'rb').read().decode('utf-8', 'replace')).items() if not v['missing']})
    want = [x['new'] for x in RP] + [LSERIES[0]]
    out = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), of=len(want), typed=sum(1 for w in want if w in got),
               missing=[w for w in want if w not in got], groups={k: v for k, v in groups.items()})
    open(os.path.join(D, 'b635_phantom_types.json'), 'wb').write((json.dumps(out, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print('### the re-pointed and upstream names typed: %d of %d %s' % (out['typed'], out['of'], out['missing'] or ''))
    return rc


def stable(*a):
    """### data/elab_types.txt, the generator's elaborated input: b634's types for every row it typed, each pass's later reading of a name
    ### taking its place (the module printed), keyed by the name the table carries after the re-point; a header naming kernel and pin."""
    B = parse(io.open(B634_TYPES, encoding='utf-8').read())
    J = _passes()
    for kind in ('upstream', 'rerun11', 'phantom'):
        for c in J['calls']:
            if c['kind'] == kind and c.get('started'):
                for k, v in parse(open(c['out'], 'rb').read().decode('utf-8', 'replace')).items():
                    if not v['missing']:
                        B[k] = v
    L = ['### ELABORATED TYPES -- %s at %s = %s, read by lake env lean (relay tools/b634_elab.py, tools/b635_elab.py); written %s by b635 under '
         '(R245)(2)-(3) and the author`s answers before its seal; the terminal table reads it for this kernel`s rows without a ledger cell.' % (
             K.KERNEL, K.KER_TAG, K.KER_PIN, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '### KERNEL %s' % K.KERNEL, '### MODULE ROOTS OF THE KERNEL: SIDEExplicitFormula Zeta23 Lc Hadamard FunctionsOfOneComplexVariable', '']
    n = 0
    for k in sorted(B):
        e = B[k]
        if e['missing']:
            continue
        n += 1
        L.append('DECL %s KIND %s HEADER %d TOTAL %d' % (k, e['kind'], e['header'], e['total']))
        if e.get('module'):
            L.append('MODULE %s %s' % (k, e['module']))
        L += ['BINDER %s %s : %s' % (b['kind'], b['name'], b['type']) for b in e['binders']]
        L += ['CONCL %s' % e['concl'], 'END']
    open(STABLE + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(STABLE + '.tmp', STABLE)
    print('### data/elab_types.txt: %d declarations typed, %d with their module printed' % (n, sum(1 for e in B.values() if not e['missing'] and e.get('module'))))


STALE = list(K.CASCADE)   # ### (R245)(4): the cascade of b634's rebuild, SaltCheckDoubling and Schema/SaltCheckFamily
REBUILD = os.path.join(D, 'b635_rebuild.json')
DECLS_LEAN = r'''import Lean
open Lean

#eval show CoreM Unit from do
  let env ← getEnv
  for m in [MODS] do
    match env.getModuleIdx? m with
    | none => IO.println s!"NOMODULE {m}"
    | some idx =>
      let mut out : Array String := #[]
      for (n, ci) in env.constants.map₁.toList do
        if env.getModuleIdxFor? n == some idx then
          out := out.push s!"CONST {m} {n} {hash ci.type}"
      for l in out.qsort (· < ·) do
        IO.println l
'''


def _proc_watch(args, cwd, log, stop_below=None):
    """### a process run with its output to `log`, the free memory sampled every 2 s and the lowest kept; with `stop_below`, a
    ### reading beneath it stops the process tree (a crossing). RETURN (rc, seconds, lowest, crossed)."""
    t0, low, crossed = time.time(), free_mb(), False
    with open(log, 'wb') as fo:
        p = subprocess.Popen(args, cwd=cwd, stdout=fo, stderr=subprocess.STDOUT)
        while p.poll() is None:
            time.sleep(SAMPLE_S)
            f = free_mb()
            if f >= 0:
                low = min(low, f)
                if stop_below is not None and f < stop_below and not crossed:
                    crossed = True
                    subprocess.run(['taskkill', '/T', '/F', '/PID', str(p.pid)], capture_output=True)
    return p.returncode, int(time.time() - t0), low, crossed


def decls(tag, *a):
    """### the constants each of the three modules defines, with each type's hash, read by ONE Lean call importing the three
    ### (data/b635_decls_<tag>.txt)."""
    mods = ', '.join('`' + _module_name(m) for m in STALE)
    src = os.path.join(WORK, 'decls_%s.lean' % tag)
    os.makedirs(WORK, exist_ok=True)
    open(src, 'w', encoding='utf-8', newline=NL).write(NL.join('import %s' % _module_name(m) for m in STALE) + NL + DECLS_LEAN.replace('MODS', mods))
    fm = free_mb()
    if 0 <= fm < K.HOLD_MB:
        print('### BENEATH THE HOLD (%d MB) -- NOT STARTED' % fm)
        return 3
    print('  free memory before the call: %d MB (hold %d)' % (fm, K.HOLD_MB), flush=True)
    log = os.path.join(WORK, 'decls_%s.out' % tag)
    rc, secs, low, _c = _proc_watch(['lake', 'env', 'lean', src.replace('/', os.sep)], K.KER, log)
    text = open(log, 'rb').read().decode('utf-8', 'replace').replace(chr(13), '')
    rows = [l for l in text.split(NL) if l.startswith('CONST ') or l.startswith('NOMODULE ')]
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['b635 -- THE DECLARATION LISTS OF THE THREE MODULES, %s (%s); exit %d ; %d s ; free %d MB before, lowest %d MB' % (
        tag.upper(), stamp, rc, secs, fm, low), ''] + rows
    q = os.path.join(D, 'b635_decls_%s.txt' % tag)
    open(q + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print('  %s: exit %d ; %d s ; constants %d' % (tag, rc, secs, sum(1 for l in rows if l.startswith('CONST '))))
    return rc


def _olean(m):
    return os.path.join(K.KER, '.lake', 'build', 'lib', 'lean', *(m + '.olean').split('/'))


def rebuild(*a):
    """### the author's word: each of the three rebuilt by the standing route of OPEN_TRAILS :13167 -- lake once, retried once, a
    ### second crossing of the hold sending it to the direct compile -- one module per call, the free memory read before each;
    ### every call banked as it lands (data/b635_rebuild.json), lake's built targets read from its log."""
    J = json.load(io.open(REBUILD, encoding='utf-8')) if os.path.exists(REBUILD) else dict(calls=[])
    for m in STALE:
        if any(c['module'] == m and c.get('done') for c in J['calls']):
            continue
        before = os.path.getmtime(_olean(m)) if os.path.exists(_olean(m)) else None
        crossings = 0
        for attempt in ('lake', 'lake-retry', 'direct'):
            if attempt == 'direct' and crossings < 2:
                break
            fm = free_mb()
            if 0 <= fm < K.HOLD_MB:
                J['calls'].append(dict(module=m, route=attempt, free_before=fm, started=False))
                J['stopped'] = 'beneath the hold before %s (%s)' % (m, attempt)
                _put(J)
                print('### STOPPED: %s' % J['stopped'], flush=True)
                return 3
            log = os.path.join(WORK, 'rebuild_%s_%s.log' % (re.sub(r'\W+', '_', m), attempt))
            os.makedirs(WORK, exist_ok=True)
            print('  %s by %s: free memory before %d MB (hold %d)' % (m, attempt, fm, K.HOLD_MB), flush=True)
            if attempt == 'direct':
                il = _olean(m)[:-6] + '.ilean'
                args = ['lake', 'env', 'lean', '-o', _olean(m), '-i', il, os.path.join(K.KER, *(m + '.lean').split('/'))]
            else:
                args = ['lake', 'build', _module_name(m)]
            rc, secs, low, crossed = _proc_watch(args, K.KER, log, stop_below=K.HOLD_MB)
            text = open(log, 'rb').read().decode('utf-8', 'replace').replace(chr(13), '')
            built = re.findall(r'(?:✔|Built|Building)\s*(?:\[\d+/\d+\])?\s*(?:Built\s+)?([A-Za-z0-9_.]+)', text)
            after = os.path.getmtime(_olean(m)) if os.path.exists(_olean(m)) else None
            c = dict(module=m, route=attempt, free_before=fm, started=True, rc=rc, seconds=secs, low=low, crossed=crossed,
                     built=sorted(set(b for b in built if '.' in b)), olean_rewritten=(after is not None and after != before),
                     log=log.replace('\\', '/'), tail=text.rstrip(NL).split(NL)[-6:])
            c['done'] = (rc == 0 and not crossed and c['olean_rewritten'])
            J['calls'].append(c)
            _put(J)
            print('  %s by %s: exit %s ; %d s ; lowest %d MB ; crossed %s ; olean rewritten %s ; built %s' % (
                m, attempt, rc, secs, low, crossed, c['olean_rewritten'], c['built'][:8]), flush=True)
            if c['done']:
                break
            crossings += 1 if crossed else 0
            if not crossed and attempt != 'lake':
                break
    J['stopped'] = None
    _put(J)
    return 0


def _put(J):
    b = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(REBUILD + '.tmp', 'wb').write(b)
    os.replace(REBUILD + '.tmp', REBUILD)


def compare(*a):
    """### the old and rebuilt declaration lists side by side, per module: names gained, lost, and types whose hash moved
    ### (data/b635_rebuild.txt)."""
    def rows(tag):
        out = collections.defaultdict(dict)
        p = os.path.join(D, 'b635_decls_%s.txt' % tag)
        for l in (io.open(p, encoding='utf-8').read() if os.path.exists(p) else '').split(NL):
            x = l.split()
            if len(x) == 4 and x[0] == 'CONST':
                out[x[1]][x[2]] = x[3]
        return out
    o, n = rows('old'), rows('new')
    J = json.load(io.open(REBUILD, encoding='utf-8')) if os.path.exists(REBUILD) else dict(calls=[])
    L = ['b635 -- THE THREE MODULES REBUILT BY THE STANDING ROUTE UNDER THE AUTHOR`S WORD, THEIR DECLARATION LISTS OLD AGAINST NEW (%s)' %
         time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '', '### THE CALLS (data/b635_rebuild.json):']
    for c in J['calls']:
        L.append('    %-40s %-10s exit %s ; %s s ; free %s MB before, lowest %s MB ; crossed %s ; olean rewritten %s ; lake built %s' % (
            c['module'], c['route'], c.get('rc'), c.get('seconds'), c.get('free_before'), c.get('low'), c.get('crossed'),
            c.get('olean_rewritten'), c.get('built')))
    tot = 0
    for m in STALE:
        mn = _module_name(m)
        a, b = o.get(mn, {}), n.get(mn, {})
        gained, lost = sorted(set(b) - set(a)), sorted(set(a) - set(b))
        moved = sorted(x for x in set(a) & set(b) if a[x] != b[x])
        tot += len(gained) + len(lost) + len(moved)
        L += ['', '### %s: old %d constants, new %d ; gained %d, lost %d, type hash moved %d' % (mn, len(a), len(b), len(gained), len(lost), len(moved))]
        L += ['    + %s' % x for x in gained] + ['    - %s' % x for x in lost] + ['    ~ %s' % x for x in moved]
    L += ['', '### ### **DIFFERENCES ACROSS THE THREE : %d.**' % tot]
    q = os.path.join(D, 'b635_rebuild.txt')
    open(q + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(L[-1])


def probe(k, *a):
    """### the author's answer to b635's Pages prompt: ONE fresh probe for page `k` with the list in force (b632's), run by the page
    ### generator itself inside this process (meant to run detached), the free memory read before it and sampled every 2 s by a
    ### watcher thread; its raw output banked as data/b635_probe_out_<k>.txt, the run as data/b635_probe_<k>.json. No page is written here."""
    import threading
    import chain_page as CP
    fm = free_mb()
    print('  probe %s: free memory before the call %d MB (hold %d)' % (k, fm, K.HOLD_MB), flush=True)
    if 0 <= fm < K.HOLD_MB:
        print('### BENEATH THE HOLD -- NOT STARTED', flush=True)
        return 4
    state = dict(low=fm, done=False, out=None)

    def watch():
        while not state['done']:
            time.sleep(SAMPLE_S)
            f = free_mb()
            if f >= 0:
                state['low'] = min(state['low'], f)
    th = threading.Thread(target=watch, daemon=True)
    th.start()
    real = CP.run_probe

    def capture(d, text):
        rc, out = real(d, text)
        state['out'] = out
        return rc, out
    CP.run_probe = capture
    t0 = time.time()
    try:
        rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(WORK, 'probe_%s' % k), None)
    finally:
        CP.run_probe = real
        state['done'] = True
    secs = int(time.time() - t0)
    outp = os.path.join(D, 'b635_probe_out_%s.txt' % k)
    if state['out'] is not None:
        open(outp + '.tmp', 'wb').write(state['out'].encode('utf-8'))
        os.replace(outp + '.tmp', outp)
    J = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), page=k, nodes=K.NODES[k], rc=rc, seconds=secs, free_before=fm, low=state['low'],
             banked=os.path.basename(outp) if state['out'] is not None else None, log=log)
    open(os.path.join(D, 'b635_probe_%s.json' % k), 'wb').write((json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print('  probe %s: generator exit %s ; %d s ; lowest %d MB ; output banked %s' % (k, rc, secs, state['low'], J['banked']), flush=True)
    return 0 if rc == 0 else rc


def test(*a):
    """### tools/test_elab_reader_b635.py run and counted by the numbered case pattern (data/b635_elab_test.txt and its json)."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_elab_reader_b635.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    cases = [l for l in out.split(NL) if re.match(r'^  \(\d+\) ', l)]
    p = sum(1 for l in cases if l.rstrip().endswith('PASS'))
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['b635 -- tools/test_elab_reader_b635.py RUN AND COUNTED (%s); exit %d' % (stamp, r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (len(cases), p, len(cases) - p)]
    for name, b in (('b635_elab_test.txt', (NL.join(L) + NL).encode('utf-8')),
                    ('b635_elab_test.json', (json.dumps(dict(at=stamp, rc=r.returncode, cases=len(cases), passing=p), indent=1) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(b)
        os.replace(q + '.tmp', q)
    print(L[-1])
    return r.returncode


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'plan':
        c, mi, v, n = plan()
        print('rows %d ; calls %d ; named by no module %s ; by grep %d' % (n, len(c), mi, len(v)))
        for m, ns in c.items():
            print('  %-60s %d' % (m, len(ns)))
    elif cmd == 'probe':
        sys.exit(probe(sys.argv[2]))
    elif cmd in ('upstream', 'rerun11', 'phantom_types', 'stable'):
        sys.exit(globals()[cmd]() or 0)
    elif cmd == 'run':
        sys.exit(run())
    elif cmd == 'join':
        join()
    elif cmd == 'test':
        sys.exit(test())
    elif cmd == 'resolve':
        sys.exit(resolve_missing())
    elif cmd == 'decls':
        sys.exit(decls(sys.argv[2]))
    elif cmd == 'rebuild':
        sys.exit(rebuild())
    elif cmd == 'compare':
        compare()
    else:
        print('usage: b635_elab.py plan | run | join')
        sys.exit(2)
