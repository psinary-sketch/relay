# -*- coding: utf-8 -*-
"""standing/deletefree.py -- v1.35.2, (R366)(6), the carried fault (9) of relay data/b755_carried_faults.txt (5 acts by data/b756_faults.txt:
b714, b720, b746, b754, b755): G-DELETE-FREE READ A TEMPORARY FOLDER'S CLEANUP AS A DELETE. The arm (tools/b703_checks.py no_delete,
checks.tpl :1813) fails on any delete word in the act's tools, and the act's lock gate, carried act to act, removes the folder its own
control made by tempfile.mkdtemp (tools/b756_lockgate.py :60-:64, :83, :97): the act deleted nothing of the record, and the arm failed at
b754 and b755 on that line alone (b755 declared it carried on its face). A temporary cleanup is read by the code, not by its words: a call of
os.remove, os.unlink, os.rmdir or shutil.rmtree (a Path's .unlink always counts) whose first argument is a name the same file bound from tempfile (mkdtemp,
mkstemp, TemporaryDirectory, NamedTemporaryFile, gettempdir joined), or a parameter of a function every call of which in the file passes
such a name. Every other delete word counts as before; the shell's words (rm -rf, Remove-Item, a branch's -D, a tag's -d, a worktree's
remove) always count.

  temp_cleanups(src) -> {stripped line text}        ok(S) -> no_delete with the temporary cleanups set apart        found(S) -> [(file, line)]
"""
import ast
import os
import re

WORDS = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
         'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
         'tag' + ' -' + 'd' + r'\b']   # ### tools/b703_checks.py no_delete :1335-:1337, the words as they stand
PAT = re.compile(r'(' + '|'.join(WORDS) + r')')
TEMP_FUNCS = ('mkdtemp', 'mkstemp', 'TemporaryDirectory', 'NamedTemporaryFile', 'gettempdir')
DELETE_FUNCS = (('os', 'remove'), ('os', 'unlink'), ('os', 'rmdir'), ('shutil', 'rmtree'))


def _is_temp_call(node):
    """a call of tempfile.<f>, or os.path.join(tempfile.gettempdir(), ...)."""
    if not isinstance(node, ast.Call):
        return False
    f = node.func
    if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == 'tempfile' and f.attr in TEMP_FUNCS:
        return True
    if isinstance(f, ast.Attribute) and f.attr == 'join' and node.args:
        return _is_temp_call(node.args[0])
    return False


def _delete_call(node):
    """the first argument of a delete call, or None."""
    if not isinstance(node, ast.Call) or not node.args:
        return None
    f = node.func
    if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and (f.value.id, f.attr) in DELETE_FUNCS:
        return node.args[0]
    return None


def temp_cleanups(src):
    """the stripped text of each line of `src` that is a temporary cleanup; an unparseable source sets none apart."""
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return set()
    temps = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and _is_temp_call(node.value):
            temps.update(t.id for t in node.targets if isinstance(t, ast.Name))
        if isinstance(node, (ast.With, ast.AsyncWith)):
            for it in node.items:
                if _is_temp_call(it.context_expr) and isinstance(it.optional_vars, ast.Name):
                    temps.add(it.optional_vars.id)
    funcs = dict((n.name, n) for n in ast.walk(tree) if isinstance(n, ast.FunctionDef))
    calls = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in funcs:
            calls.setdefault(node.func.id, []).append(node)
    temp_params = set()
    for name, fn in funcs.items():
        params = [a.arg for a in fn.args.args]
        cs = calls.get(name) or []
        for i, p in enumerate(params):
            if cs and all(len(c.args) > i and isinstance(c.args[i], ast.Name) and c.args[i].id in temps for c in cs):
                temp_params.add((name, p))
    lines = src.split('\n')
    out = set()
    for fname, fn in [(None, tree)] + list(funcs.items()):
        for node in ast.walk(fn):
            a = _delete_call(node)
            if a is None or not isinstance(a, ast.Name):
                continue
            if a.id in temps or (fname is not None and (fname, a.id) in temp_params):
                out.add(lines[node.lineno - 1].strip())
    return out


def found(S, read=None):
    """[(file, line)] each delete word the arm reads, the temporary cleanups set apart."""
    read = read or (lambda p: open(p, encoding='utf-8', errors='replace').read())
    out = []
    for f, t in (S.get('tooltext') or {}).items():
        try:
            apart = set(x.split('#')[0].strip() for x in temp_cleanups(read(f))) if os.path.isfile(f) else set()
        except OSError:
            apart = set()
        for l in t.split('\n'):
            if PAT.search(l) and l.split('#')[0].strip() not in apart:   # ### the arm's text is cut at '#' (strip_prose); the source line likewise
                out.append((f, l.strip()[:120]))
    return out


def ok(S, read=None):
    return bool(S.get('tooltext')) and not found(S, read)
