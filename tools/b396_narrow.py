# -*- coding: utf-8 -*-
"""b396_narrow.py -- THE SHAPE-NARROW PREDICATE DETECTOR, AND ITS OWN FIXTURE.

### ### **THE ORDER'S FIRST INSTRUCTION IS THAT THIS FILE BE TESTED BEFORE IT IS BELIEVED**, and
### the reason is `b395`: an act swept for a defect with an instrument carrying the same defect.
### ### **A SWEEP FOR NARROW MATCHERS THAT IS ITSELF NARROW WOULD BE THE SPECIES INSIDE THE ACT
### ### THAT MEASURES IT.**
###
### ### **WHY A RAW `grep` FOR A BACKTICK IS NOT THE INSTRUMENT.** ### `823` of the `855` files in
### `tools/` contain a backtick. ### Almost every one is PROSE -- a `###` comment or a printed
### line -- and ### **A BACKTICK IN A SENTENCE IS NOT A BACKTICK IN A MATCHER.**
### So this reads by `ast` and keeps a string only where it is USED AS A TEST: an argument to an
### `re` call, to `.startswith`/`.endswith`, or a literal on either side of `in` / `==`.
### ### **`strip_prose` CANNOT DO THIS** -- it deletes string-span lines, which is the opposite of
### what is wanted here (`b387`'s lesson, applied in the other direction).
###
### ### **WHAT COUNTS AS NARROW, STATED BEFORE ANYTHING IS MEASURED:**
###   (a) the literal carries a ### **BACKTICK** ### -- the shape `b394` was deaf to;
###   (b) the literal is a regex with a ### **SINGLE-CASE CHARACTER CLASS** ### and no `re.I`;
###   (c) the literal is an ### **ANCHORED LEADING MARKER** ### (`^#`, `^\\|`, `^>`, `^ *###`);
###   (d) the literal is a ### **MARKER PREFIX** ### handed to `.startswith` / `.endswith`.
### ### **AND A NON-REGEX TEST IS AS NARROW AS A REGEX ONE** -- `'`' in tok`, `tok.islower()`,
### `line.startswith('### ')` are all shape tests, and a detector that only reads `re` calls would
### miss every one of them. ### **THAT IS THE THIRD FORM THE FIXTURE BELOW DEMANDS.**
"""
import ast
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ### **THE MATCHER CONTEXTS. ### A STRING OUTSIDE ONE OF THESE IS PROSE AND IS NOT READ.**
RE_FUNCS = {'compile', 'findall', 'search', 'match', 'sub', 'subn', 'split', 'finditer',
            'fullmatch'}
STR_TESTS = {'startswith', 'endswith', 'count', 'index', 'find', 'rfind', 'partition',
             'rpartition', 'split', 'rsplit', 'strip', 'lstrip', 'rstrip', 'replace'}
# ### the case-only predicates, which carry no string at all and would be invisible to a
# ### string-hunting detector.
CASE_METHODS = {'islower', 'isupper', 'lower', 'upper', 'casefold', 'title', 'capitalize'}

SINGLE_CASE = re.compile(r'\[\^?(?:[a-z0-9_\\\-]{2,})\]|\[\^?(?:[A-Z0-9_\\\-]{2,})\]')
BOTH_CASE = re.compile(r'\[\^?[^\]]*a-z[^\]]*A-Z[^\]]*\]|\[\^?[^\]]*A-Z[^\]]*a-z[^\]]*\]')
ANCHORED_MARKER = re.compile(r'^\^\s*(?:\\\||#|>|\\\*|###)')
MARKERY = ('###', '<!--', '| ', '> ', '#', '**', '`')


def _why(s, ctx, flags_i):
    """### **THE FOUR NARROWNESS TESTS, EACH NAMED WHEN IT FIRES.**"""
    out = []
    if '`' in s:
        out.append('BACKTICK')
    if ctx == 're' and not flags_i and SINGLE_CASE.search(s) and not BOTH_CASE.search(s):
        out.append('SINGLE-CASE CLASS')
    if ctx == 're' and ANCHORED_MARKER.search(s):
        out.append('ANCHORED MARKER')
    if ctx in ('startswith', 'endswith') and any(s.startswith(m) or s == m for m in MARKERY):
        out.append('MARKER PREFIX')
    return out


class Walker(ast.NodeVisitor):
    """### Collects every string used as a TEST, with the context that makes it one."""

    def __init__(self):
        self.hits = []          # (lineno, context, literal, [why])
        self.case_hits = []     # (lineno, method) -- narrowness carrying no string at all

    def _add(self, node, ctx, s, flags_i=False):
        w = _why(s, ctx, flags_i)
        if w:
            self.hits.append((getattr(node, 'lineno', 0), ctx, s, w))

    def visit_Call(self, node):
        f = node.func
        name = getattr(f, 'attr', None) or getattr(f, 'id', None)
        if name in RE_FUNCS:
            # ### `re.I` anywhere in the call disarms the single-case test, and saying so is the
            # ### difference between a narrow matcher and a deliberate one.
            src = ast.dump(node)
            flags_i = ("attr='I'" in src or "attr='IGNORECASE'" in src or '(?i)' in src)
            for a in node.args:
                if isinstance(a, ast.Constant) and isinstance(a.value, str):
                    if '(?i)' in a.value:
                        flags_i = True
                    self._add(node, 're', a.value, flags_i)
        elif name in STR_TESTS:
            for a in node.args:
                if isinstance(a, ast.Constant) and isinstance(a.value, str):
                    self._add(node, name if name in ('startswith', 'endswith') else 'str', a.value)
                elif isinstance(a, (ast.Tuple, ast.List)):
                    for e in a.elts:
                        if isinstance(e, ast.Constant) and isinstance(e.value, str):
                            self._add(node, name if name in ('startswith', 'endswith') else 'str',
                                      e.value)
        elif name in CASE_METHODS and isinstance(f, ast.Attribute):
            self.case_hits.append((getattr(node, 'lineno', 0), name))
        self.generic_visit(node)

    def visit_Compare(self, node):
        # ### `'x' in line`, `line == '### '` -- a containment or equality test is a matcher.
        parts = [node.left] + list(node.comparators)
        ops = [type(o).__name__ for o in node.ops]
        if any(o in ('In', 'NotIn', 'Eq', 'NotEq') for o in ops):
            for p in parts:
                if isinstance(p, ast.Constant) and isinstance(p.value, str):
                    self._add(node, 'compare', p.value)
        self.generic_visit(node)


def scan_source(src):
    """### Returns (hits, case_hits) for one module's SOURCE TEXT. ### Raises on a syntax error."""
    tree = ast.parse(src)
    # ### **DOCSTRINGS ARE PROSE AND ARE DROPPED**, so a header quoting a regex is not a matcher.
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if (n.body and isinstance(n.body[0], ast.Expr)
                    and isinstance(n.body[0].value, ast.Constant)
                    and isinstance(n.body[0].value.value, str)):
                n.body = n.body[1:] or [ast.Pass()]
    w = Walker()
    w.visit(tree)
    return w.hits, w.case_hits


# ==================================================================================================
#  THE FIXTURE. ### **THE ORDER'S FIRST INSTRUCTION.**
# ==================================================================================================
# ### **ONE NARROW MATCHER, WRITTEN THREE WAYS. ### ALL THREE MUST BE FOUND.**
FIXTURE = '''
import re
NAMES = re.findall(r'`(SIDE-[a-z0-9-]+)`', txt)          # form 1: a raw-string regex
PAT = re.compile("\\\\|\\\\s*\\\\*\\\\*`([A-Z_]+)`")     # form 2: a double-quoted escaped regex
def form3(tok, line):                                     # form 3: NO REGEX AT ALL
    return line.startswith('### ') and '`' in tok and tok.islower()
'''

# ### **AND A WIDE ONE, WHICH MUST NOT BE FOUND.** ### Without this the fixture proves only that
# ### the detector fires, not that it discriminates -- `b393`'s and `b395`'s control rule.
FIXTURE_WIDE = '''
import re
NAMES = re.findall(r'(SIDE-[A-Za-z0-9-]+)', txt)
ALSO = re.findall(r'(?i)(side-[a-z0-9-]+)', txt)
def widecheck(tok, line):
    return 'SIDE-' in tok
'''


def fixture():
    """### Returns (per-form found?, wide clean?, detail). ### **RUN BEFORE ANY SWEEP.**"""
    hits, case_hits = scan_source(FIXTURE)
    byline = {}
    for ln, ctx, s, why in hits:
        byline.setdefault(ln, []).append((ctx, s, why))
    for ln, m in case_hits:
        byline.setdefault(ln, []).append(('case', m, ['CASE TEST']))
    # ### form 1 sits on line 3, form 2 on line 4, form 3 on lines 5-6 of the fixture.
    f1 = any(any('BACKTICK' in w for _c, _s, w in v) for k, v in byline.items() if k == 3)
    f2 = any(any('BACKTICK' in w for _c, _s, w in v) for k, v in byline.items() if k == 4)
    f3 = any(any(w2 in ('BACKTICK', 'MARKER PREFIX', 'CASE TEST')
                 for _c, _s, w in v for w2 in w) for k, v in byline.items() if k >= 5)
    wh, wc = scan_source(FIXTURE_WIDE)
    wide_clean = not wh and not wc
    return (f1, f2, f3), wide_clean, byline


# ### **WHAT THIS SWEEP IS DEAF TO -- STATED IN THE INSTRUMENT, NOT ONLY IN THE BANK.**
DEAF = [
    'a narrowness built from a VARIABLE rather than a literal -- `pat = mark + NAME` is assembled '
    'at run time and this detector reads literals',
    'a narrowness that lives in the DATA a tool reads rather than in the tool -- a roster file '
    'listing only backticked names would narrow every act that imports it',
    'a matcher passed in from ANOTHER module by name, where the literal sits in the caller',
    'a shape restriction with no string and no case method -- a length test, an index, a slice',
    'whether a narrow matcher is WRONG. ### **NARROW IS NOT A DEFECT; NARROW UNDER A NEGATIVE '
    'FINDING IS A RISK**, and this file measures the shape, never the verdict',
]


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    (f1, f2, f3), wide_clean, byline = fixture()
    print('=' * 100)
    print('b396_narrow.py -- THE DETECTOR AND ITS FIXTURE. ### RUN, NOT CLAIMED.')
    print('=' * 100)
    print('  ### **ONE NARROW MATCHER, WRITTEN THREE WAYS:**')
    print('    form 1  a raw-string regex, backtick-delimited       FOUND : %s' % f1)
    print('    form 2  a double-quoted escaped regex                FOUND : %s' % f2)
    print('    form 3  ### **NO REGEX AT ALL** -- startswith + `in` + islower()   FOUND : %s' % f3)
    print('  ### **ALL THREE FOUND : %s**' % (f1 and f2 and f3))
    print('  ### **AND THE WIDE FIXTURE IS CLEAN (the detector discriminates) : %s**' % wide_clean)
    for ln in sorted(byline):
        for ctx, s, why in byline[ln]:
            print('      line %-3d %-11s %-46s %s' % (ln, ctx, repr(s)[:46], ','.join(why)))
    print()
    print('  ### **WHAT THIS SWEEP IS DEAF TO:**')
    for d in DEAF:
        print('    -- %s' % d)
    print('=' * 100)
    return 0 if (f1 and f2 and f3 and wide_clean) else 1


if __name__ == '__main__':
    sys.exit(main())
