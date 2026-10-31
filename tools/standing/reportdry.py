# -*- coding: utf-8 -*-
"""standing/reportdry.py -- v1.9.0, (R339)(2)(ii): `report dry` A PRE-LOCK STEP OF THE CLOSE'S ORDER, A SECTION NAMING AN UNDEFINED NAME FAILING IT.

b728's report section defined sc2 and sl2, the template appended sk, and `report bank` crashed with NameError after the root's prompt (b728 event (6)). Here
the report tool as the fold renders it is read without running it: every name lines() loads must be bound in lines(), at the module's head or among the
builtins. The registration gate runs this before the lock (step [5a]) and refuses CLEAR on a name undefined; the seal refuses where the bank is absent or failing.

  undefined(src) -> [names]       read(act) -> dict(undefined, lines)       bank(act) -> (ok, lines)   writes data/<act>_report_dry.txt
"""
import ast
import builtins
import os
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


def source(act):
    import fold as F
    return F.render(act, 'report')


def read(act):
    src = source(act)
    return dict(undefined=undefined(src), lines=src.count('\n') + 1)


def bank(act):
    r = read(act)
    ok = not r['undefined']
    L = ['%s -- report dry, step [5a], (R339)(2)(ii): the report tool as rendered read without running it (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '  lines of the rendered tool %d ; names lines() loads that nothing binds: %s' % (r['lines'], r['undefined'] or 'NONE'),
         '### ### **REPORT DRY: %s.**' % ('CLEAN' if ok else 'A SECTION NAMES AN UNDEFINED NAME')]
    p = os.path.join(A.D, '%s_report_dry.txt' % act)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(('\n'.join(L) + '\n').encode('utf-8'))
    os.replace(p + '.tmp', p)
    return ok, L


def stands(act):
    """the seal's reading: the bank present and clean."""
    return '**REPORT DRY: CLEAN.**' in (A.rd('%s_report_dry.txt' % act) or '')
