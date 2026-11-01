# -*- coding: utf-8 -*-
"""standing/reportdry.py -- v1.9.0, (R339)(2)(ii): `report dry` A PRE-LOCK STEP OF THE CLOSE'S ORDER, A SECTION NAMING AN UNDEFINED NAME FAILING IT.

b728's report section defined sc2 and sl2, the template appended sk, and `report bank` crashed with NameError after the root's prompt (b728 event (6)). Here
the report tool as the fold renders it is read without running it: every name lines() loads must be bound in lines(), at the module's head or among the
builtins. The registration gate runs this before the lock (step [5a]) and refuses CLEAR on a name undefined; the seal refuses where the bank is absent or failing.

  undefined(src) -> [names]       read(act) -> dict(undefined, lines, tools)       bank(act) -> (ok, lines)   writes data/<act>_report_dry.txt
  v1.12.0, (R342)(2)(i): unbound(src) -> (live, dead), every scope of a rendered tool; rendered(act, secs, ovs) over the seven; the bank fails on a live name in any of them.
"""
import ast
import builtins
import os
import symtable
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402


def undefined(src):
    """the names the function lines() of a report tool's source loads and nothing binds, in order of their first line."""
    tree = ast.parse(src)
    fn = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'lines'), None)
    if fn is None:
        return ['### NO lines() IN THE TOOL']
    mod = set(dir(builtins))
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            mod.add(n.name)
        for s in ast.walk(n) if not isinstance(n, (ast.FunctionDef, ast.ClassDef)) else ():
            if isinstance(s, ast.Name) and isinstance(s.ctx, ast.Store):
                mod.add(s.id)
            elif isinstance(s, (ast.Import, ast.ImportFrom)):
                mod.update((a.asname or a.name).split('.')[0] for a in s.names)
    bound, loads = set(a.arg for a in fn.args.args), []
    for s in ast.walk(fn):
        if isinstance(s, ast.Name):
            (bound.add(s.id) if isinstance(s.ctx, ast.Store) else loads.append((s.lineno, s.id)))
        elif isinstance(s, (ast.Import, ast.ImportFrom)):
            bound.update((a.asname or a.name).split('.')[0] for a in s.names)
        elif isinstance(s, (ast.FunctionDef, ast.Lambda)):
            bound.update(a.arg for a in s.args.args)
    out = []
    for _n, name in sorted(loads):
        if name not in bound and name not in mod and name not in out:
            out.append(name)
    return out


def _globals(table, out):
    for s in table.get_symbols():
        if s.is_global() and s.is_referenced() and not s.is_assigned():
            out.add(s.get_name())
    for c in table.get_children():
        _globals(c, out)
    return out


def unbound(src):
    """v1.12.0, (R342)(2)(i): every name any scope of a rendered tool reads as a global and nothing binds, by the compiler's own symbol table. (live, dead): a name read only inside top-level functions nothing
    else in the tool reads is a dead route's, printed and not failing; a name read by an arm, a lambda or the module's own lines is live. b731's module at its lock: live ['research_reproduces_ok']."""
    top = symtable.symtable(src, 'rendered', 'exec')
    bound = set(s.get_name() for s in top.get_symbols() if s.is_assigned() or s.is_imported() or s.is_namespace()) | set(dir(builtins)) | set(('__file__',))
    names = sorted(n for n in _globals(top, set()) if n not in bound)
    if not names:
        return [], []
    tree = ast.parse(src)
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    loads = dict((f.name, set(s.id for s in ast.walk(f) if isinstance(s, ast.Name))) for f in fns)
    outside = set(s.id for n in tree.body if not isinstance(n, ast.FunctionDef) for s in ast.walk(n) if isinstance(s, ast.Name))
    reached = set(f for f in loads if f in outside or any(f in v for k, v in loads.items() if k != f))
    live, dead = [], []
    for n in names:
        (dead if not (n in outside or any(n in loads[f] for f in reached)) else live).append(n)
    return live, dead


def source(act):
    import fold as F
    return F.render(act, 'report')


def rendered(act, secs=None, ovs=None):
    """{tool: (live, dead, lines)} over the seven as the fold renders them, the act's module or the sections passed."""
    import fold as F
    out = {}
    for tool in F.TOOLS:
        src = F.render(act, tool, secs, ovs)
        out[tool] = unbound(src) + (src.count('\n') + 1,)
    return out


def read(act):
    src = source(act)
    return dict(undefined=undefined(src), lines=src.count('\n') + 1, tools=rendered(act))


def bank(act):
    r = read(act)
    live = [(t, x) for t, v in r['tools'].items() for x in v[0]]
    ok = not r['undefined'] and not live
    L = ['%s -- report dry, step [5a], (R339)(2)(ii), widened by (R342)(2)(i): the report tool and the six beside it as rendered, read without running them (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '  lines of the rendered report tool %d ; names lines() loads that nothing binds: %s' % (r['lines'], r['undefined'] or 'NONE')]
    L += ['  %-9s lines %-7d names read and bound by nothing, on a live route: %s ; on a dead route, printed and not failing: %s' % (t, v[2], v[0] or 'NONE', v[1] or 'NONE') for t, v in r['tools'].items()]
    L += ['### ### **REPORT DRY: %s.**' % ('CLEAN' if ok else 'A SECTION NAMES AN UNDEFINED NAME')]
    p = os.path.join(A.D, '%s_report_dry.txt' % act)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(('\n'.join(L) + '\n').encode('utf-8'))
    os.replace(p + '.tmp', p)
    return ok, L


def stands(act):
    """the seal's reading: the bank present and clean."""
    return '**REPORT DRY: CLEAN.**' in (A.rd('%s_report_dry.txt' % act) or '')
