# -*- coding: utf-8 -*-
"""b396_figures.py -- FROM A NARROW MATCHER TO THE FIGURE IT PRODUCED.

### ### **AN INSTRUMENT COUNT IS NOT A FINDINGS LIST, AND THIS FILE EXISTS BECAUSE THE FIRST TWO
### ### FILTERS THIS ACT TRIED WERE VACUOUS.** ### `374` of `407` narrow instruments print some
### word like `no` or `not` somewhere, and `350` of `380` have their act's name mentioned in a
### ledger. ### **A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER**, and both were
### thrown out before the lock rather than reported as a result.
###
### ### **A FINDING IS A FIGURE AN ACT BANKED, NOT A REGEX AN ACT WROTE.** ### So the unit here
### is the triple ### **(narrow literal, the name its yield is bound to, the line that REPORTS
### ### that name's count)** ### -- and a finding is AT RISK when that reported count is an
### ### **ABSENCE**: a zero, a `none`, or a phrase saying the thing was not found.
###
### ### **AND THE ABSENCE TEST READS THE REPORT'S OWN TEXT, NOT THE MODULE'S PROSE.** ### The
### report must name the bound variable and carry the absence in the same literal, which is what
### makes it a claim about that measurement rather than a sentence that happens to contain `no`.
"""
import ast
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b396_narrow as NAR   # noqa: E402

# ### **THE ABSENCE SHAPES, IN A REPORT'S OWN LITERAL.**
ABSENCE = re.compile(r'(?i)(:\s*0\b|\b0\b\s*(?:of|found|hits|rows|instances|matches)|'
                     r'\bnone\b|\bNO [A-Z]|\bnot (?:found|present|on|in|among|reachable)\b|'
                     r'\bunreachable\b|\bcarries none\b|\bis absent\b|\bno \w+ (?:is|are|was|were)'
                     r'\b|\bMISSING\b|\bUNASSIGNED\b)')
COUNTY = re.compile(r'%d|%s|\{[^}]*\}|len\(')


def _fn_of(tree):
    """### map: node -> enclosing function name, so a report is tied to its own matcher."""
    owner = {}
    for fn in ast.walk(tree):
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Module)):
            nm = getattr(fn, 'name', '<module>')
            for n in ast.walk(fn):
                owner.setdefault(id(n), nm)
    return owner


def _reports(tree):
    """### Every printed/recorded call, with its literals and the names it interpolates."""
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and (getattr(n.func, 'id', None) in ('print', 'rec')
                                        or getattr(n.func, 'attr', None) in ('append', 'write')):
            lits = [a.value for a in ast.walk(n)
                    if isinstance(a, ast.Constant) and isinstance(a.value, str)]
            names = set()
            for a in ast.walk(n):
                if isinstance(a, ast.Name):
                    names.add(a.id)
                if isinstance(a, ast.Attribute):
                    names.add(a.attr)
            out.append((getattr(n, 'lineno', 0), lits, names))
    return out


def figures(src):
    """### Returns the (matcher, bound name, report) triples, and which report an ABSENCE."""
    tree = ast.parse(src)
    hits, case_hits = NAR.scan_source(src)
    if not hits and not case_hits:
        return []
    owner = _fn_of(tree)
    reports = _reports(tree)

    # ### which names are bound to a call that CONTAINS a narrow literal, and where.
    narrow_lines = {ln for ln, _c, _s, _w in hits} | {ln for ln, _m in case_hits}
    bound = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            lines = {getattr(c, 'lineno', -1) for c in ast.walk(n)}
            if not (lines & narrow_lines):
                continue
            tgs = n.targets if isinstance(n, ast.Assign) else [n.target]
            for tg in tgs:
                if isinstance(tg, ast.Name):
                    bound[tg.id] = (getattr(n, 'lineno', 0), owner.get(id(n), '<module>'))
        # ### a comprehension or a return can carry the yield with no assignment at all.
        if isinstance(n, ast.Return):
            lines = {getattr(c, 'lineno', -1) for c in ast.walk(n)}
            if lines & narrow_lines:
                bound.setdefault('<return>', (getattr(n, 'lineno', 0),
                                              owner.get(id(n), '<module>')))

    out = []
    for name, (bl, fn) in bound.items():
        for rl, lits, names in reports:
            if name not in names:
                continue
            for lit in lits:
                if not COUNTY.search(lit):
                    continue
                if ABSENCE.search(lit):
                    why = [w for ln, _c, _s, ws in hits if ln in narrow_lines for w in ws]
                    lit0 = [s for ln, _c, s, _w in hits][:1]
                    out.append(dict(name=name, bound_line=bl, func=fn, report_line=rl,
                                    report=' '.join(lit.split())[:150],
                                    literal=(repr(lit0[0])[:70] if lit0 else ''),
                                    why=sorted(set(why))))
                    break
    # ### one entry per (name, report line)
    seen, uniq = set(), []
    for o in out:
        k = (o['name'], o['report_line'])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(o)
    return uniq


# ==================================================================================================
#  THE FIXTURE. ### **THIS FILTER IS TESTED BEFORE IT IS BELIEVED, LIKE THE ONE ABOVE IT.**
# ==================================================================================================
FIX_POS = '''
import re
def survey(txt):
    names = re.findall(r'`(SIDE-[a-z0-9-]+)`', txt)
    print('  ### repositories it names : %d ; NONE on the drive' % len(names))
    return names
'''
FIX_NEG = '''
import re
def survey(txt):
    names = re.findall(r'`(SIDE-[a-z0-9-]+)`', txt)
    print('  ### repositories it names : %d ; all resolve' % len(names))
    return names
'''
FIX_WIDE = '''
import re
def survey(txt):
    names = re.findall(r'(?i)(side-[a-z0-9-]+)', txt)
    print('  ### repositories it names : %d ; NONE on the drive' % len(names))
    return names
'''


def fixture():
    """### positive fires ; a non-absence report does NOT ; a wide matcher does NOT."""
    return (len(figures(FIX_POS)) == 1, len(figures(FIX_NEG)) == 0,
            len(figures(FIX_WIDE)) == 0)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    a, b, c = fixture()
    print('  narrow matcher + absence report      FIRES     : %s' % a)
    print('  narrow matcher + ordinary report     QUIET     : %s' % b)
    print('  wide matcher + absence report        QUIET     : %s' % c)
    print('  ### **THE FILTER DISCRIMINATES ON BOTH AXES : %s**' % (a and b and c))
    sys.exit(0 if (a and b and c) else 1)
