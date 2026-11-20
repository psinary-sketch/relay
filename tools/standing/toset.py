# -*- coding: utf-8 -*-
"""standing/toset.py -- v1.38.1, (R374)(5) [K1]: THE VALUE NOT YET SET.

b763's probe of the act part (2026-11-20T06:23:04Z, data/b763_events.txt :723-:729) failed G-DIFFERS-ERRATA on the worklist's CORR_LINE,
which the carry had left at None (tools/b763_worklist.py :445 at the commit before 6dc04ffb) where b762's worklist set its own; nothing
printed that the arm read a value the act had still to set, and its failure read like any other (b763 defect (g) of the same class; (R372)(11)
on the carry's constants; b761 (a), (b) and (l)). The same line stood again at b764 (tools/b764_worklist.py :464 at relay 8720475f), its one
comment naming (R374)(1) for WEIGHT_LINE beside CORR_LINE: a constant still to set and one the ruling leaves empty, told apart by nothing.

THE RULE, written here and enforced by the suite's part runner (tools/standing/fold/checks.tpl, before its arm loop) and read by the combine
and the seal (tools/standing/close.py combine_tally and neg_shown):
  (i)   EMPTY: a top-level constant of the act's worklist whose last assignment binds it to None, to an empty string, tuple, list, set or
        dict, or to a carried stub (`_Carried(...)`), read from the worklist's text and not by importing it;
  (ii)  LEFT EMPTY: an empty constant whose assignment's comment names it as the ruling's, in the words `LEFT EMPTY BY (Rnnn)(k)` -- after
        its name where the line assigns two or more (`WEIGHT_LINE LEFT EMPTY BY (R374)(1)`), alone where it assigns one; every other empty
        constant is STILL TO SET, whatever else its comment says;
  (iii) before a part runs its arms, in every mode but the run on the previous act's banks, each arm is read for the worklist constants its
        code names (the predicate's code objects and, three calls deep, those of the suite's functions it names); an arm that names a
        constant still to set is not run: the part prints each with its constants, its row reads WITHHELD, NOT RUN: STILL TO SET <names>,
        it is counted neither among the passes nor among the failures, and the combine counts it among the withheld;
  (iv)  the seal reads such an arm in the pre-run's exercise bank as HELD, neither shown failing nor refused, and prints it with its
        constants; the seal's withheld field does not take it.

  python -X utf8 -u tools/standing/toset.py <act>        the act's worklist read: each constant still to set, each left empty with its clause
"""
import ast
import os
import re
import sys
import types

CLAUSE = r'\(R\d{3}\)\(\d+\)(?:\([ivx]+\))?'
MARK = re.compile(r'LEFT EMPTY BY (' + CLAUSE + ')')
NAME = re.compile(r'^[A-Z][A-Z0-9_]*$')


def _comment(line):
    """the line's comment: the text after the first '#' outside a one-line string."""
    q, k = None, 0
    while k < len(line):
        c = line[k]
        if q:
            if c == '\\':
                k += 2
                continue
            if c == q:
                q = None
        elif c in '\'"':
            q = c
        elif c == '#':
            return line[k + 1:]
        k += 1
    return ''


def _empty(v):
    """True where the expression is None, an empty literal or a carried stub."""
    if isinstance(v, ast.Constant):
        return v.value is None or v.value == ''
    if isinstance(v, (ast.Tuple, ast.List, ast.Set)):
        return not v.elts
    if isinstance(v, ast.Dict):
        return not v.keys
    if isinstance(v, ast.Call):
        f = v.func
        return (isinstance(f, ast.Name) and f.id in ('_Carried', 'Carried')) or (isinstance(f, ast.Attribute) and f.attr == 'Carried')
    return False


def classify_text(text):
    """{name: (state, word)} for every top-level constant of the worklist's text whose last assignment is empty: ('EMPTY', the clause)
    where its comment names it LEFT EMPTY BY a clause, ('TO SET', its comment) otherwise; a constant last bound to a value is absent."""
    text = (text or '').replace('\r', '')
    ls = text.split('\n')
    last = {}
    for node in ast.parse(text).body:
        if not isinstance(node, ast.Assign):
            continue
        cm = ' '.join(_comment(ls[i - 1]) for i in range(node.lineno, (node.end_lineno or node.lineno) + 1)).strip()
        for t in node.targets:
            if isinstance(t, ast.Name) and NAME.match(t.id):
                pairs, one = [(t.id, node.value)], True
            elif isinstance(t, (ast.Tuple, ast.List)):
                names = [e.id if isinstance(e, ast.Name) else None for e in t.elts]
                vals = node.value.elts if isinstance(node.value, (ast.Tuple, ast.List)) and len(node.value.elts) == len(names) else [None] * len(names)
                pairs, one = [(n, v) for n, v in zip(names, vals) if n and NAME.match(n)], False
            else:
                continue
            for n, v in pairs:
                if v is None or not _empty(v):
                    last[n] = None
                    continue
                m = re.search(r'\b' + re.escape(n) + r' ' + MARK.pattern, cm) or (MARK.search(cm) if one else None)
                last[n] = ('EMPTY', m.group(1)) if m else ('TO SET', cm[:120])
    return dict((n, s) for n, s in last.items() if s)


def _codes(obj):
    c = getattr(obj, '__code__', None)
    return [c] if c is not None else []


def code_names(code, g, depth=3, seen=None):
    """the names an arm's code reads: its code object's names and its nested code objects', and, `depth` calls deep, those of every
    module-level function of `g` it names."""
    seen = set() if seen is None else seen
    if id(code) in seen:
        return set()
    seen.add(id(code))
    names = set(code.co_names)
    for c in code.co_consts:
        if isinstance(c, types.CodeType):
            names |= code_names(c, g, depth, seen)
    if depth > 0:
        for n in list(names):
            f = g.get(n)
            if isinstance(f, types.FunctionType):
                for c in _codes(f):
                    names |= code_names(c, g, depth - 1, seen)
    return names


def held(arms, worklist_path, g):
    """{arm: [the constants still to set it names]} over the part's arms [(name, reads, pred, pos)], the act's worklist read from its file,
    `g` the suite's globals."""
    with open(worklist_path, encoding='utf-8') as fh:
        toset = set(n for n, (s, _w) in classify_text(fh.read()).items() if s == 'TO SET')
    out = {}
    if not toset:
        return out
    for a in arms:
        hit = sorted(set().union(set(), *[code_names(c, g) for c in _codes(a[2])]) & toset)
        if hit:
            out[a[0]] = hit
    return out


def main(argv):
    if len(argv) != 1 or not re.match(r'^b\d{3}$', argv[0]):
        sys.exit(__doc__)
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '%s_worklist.py' % argv[0])
    with open(p, encoding='utf-8') as fh:
        c = classify_text(fh.read())
    ts = [(n, w) for n, (s, w) in sorted(c.items()) if s == 'TO SET']
    em = [(n, w) for n, (s, w) in sorted(c.items()) if s == 'EMPTY']
    print('### THE CONSTANTS STILL TO SET (tools/%s_worklist.py, empty and not named LEFT EMPTY BY a clause): %d' % (argv[0], len(ts)))
    for n, w in ts:
        print('  TO SET  %-28s %s' % (n, w[:110]))
    print('### THE CONSTANTS LEFT EMPTY BY A RULING`S CLAUSE: %d' % len(em))
    for n, w in em:
        print('  EMPTY   %-28s %s' % (n, w))


if __name__ == '__main__':
    main(sys.argv[1:])
