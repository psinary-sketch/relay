# -*- coding: utf-8 -*-
"""tools/b770_names.py -- b770, (R380)(3): THE NAMES CLASSED, a reading at step zero with no repair ordered on it. Written by the Write
tool and committed before its run (N2); no git write, nothing fetched, no line of a module printed but its names.

Each top-level name of tools/b769_worklist.py and of tools/acts/b769.py, classed:
  READ      its value taken from git or from a bank at run time: its value (a def's body) calls a reader -- open, io.open, json.load,
            subprocess, os.listdir, os.scandir, os.walk, os.stat, os.path.exists, isfile, isdir, getsize or getmtime, glob, or a function
            whose name has a part git, read, load, jload, show, blob, sha, fsha, bank, rows or rd -- or names a top-level name read so (to a
            fixed point); and, counted apart, the worklist's stage-one values (tools/standing/carry.py STAGE_ONE), set from git and the banks
            at step zero by the seat's script;
  RULED     not READ, and a clause of a ruling sets it: its value differs from b768's value of the same name in the like file after the act
            names' substitution (b768 -> b769, b767 -> b768, R378 -> R379, R377 -> R378), or the name is new at b769, or its lines or the
            comment block directly above them cite b769's ruling (R379); each counted by which;
  STANDING  neither.
The worklist read by its syntax tree (its module level, the bodies of a top-level if, try or with among it); the act module, a sections file
read as text and not imported, by its lines at the left margin inside a SECTION or OVERRIDE block, outside a triple-quoted string, each
statement to its brackets' close (a def to the next line of code at the margin), keyed by its tool and its name. The three counts and the
names classed RULED banked as data/b770_names.txt.

CONTROLS, each printed, all AS WANTED before the bank is written: a planted worklist pair and a planted sections pair (a previous act's text
and the act's), each name of each class read as planted, a name inside a docstring and an indented name read as no top-level name.

  control  prints the controls; writes nothing
  dry      the controls and the bank printed; writes nothing
  write    the same, then data/b770_names.txt (refused where it stands)
  again    the same over a standing bank, the earlier bank named in the new one's head by its digest, its time and its totals
"""
import ast
import io
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ACT, SUBJ, PREV, RULING = 'b770', 'b769', 'b768', 'R379'
SUBS = (('b768', 'b769'), ('b767', 'b768'), ('R378', 'R379'), ('R377', 'R378'))
FILES = (('tools/b769_worklist.py', 'tools/b768_worklist.py', 'tree'), ('tools/acts/b769.py', 'tools/acts/b768.py', 'text'))
BANK = os.path.join(D, 'b770_names.txt')
NL = chr(10)
PRIM = re.compile(r'^(open|io\.open|json\.load|subprocess\.\w+|os\.(listdir|scandir|walk|stat)|os\.path\.(exists|isfile|isdir|getsize|getmtime)|glob\.\w+)$')
SEG = {'git', 'read', 'load', 'jload', 'show', 'blob', 'sha', 'fsha', 'sha256', 'bank', 'rows', 'rd'}
SEC = re.compile(r'^#⟪(SECTION|OVERRIDE)\s+(\S+)')
ASSIGN = re.compile(r'^([A-Za-z_]\w*)\s*(?::[^=\n]+)?=(?!=)')
DEFN = re.compile(r'^(def|class)\s+([A-Za-z_]\w*)')
CALL = re.compile(r'([A-Za-z_][\w.]*)\s*\(')
ONE = re.compile(r"'(?:[^'\\\n]|\\.)*'|\"(?:[^\"\\\n]|\\.)*\"")


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def subst(s, subs):
    for a, b in subs:
        s = s.replace(a, b)
    return s


def reader_call(d):
    """True where a dotted callee is a reader: a primitive, or a last name with a part of SEG."""
    last = d.rsplit('.', 1)[-1]
    return bool(PRIM.match(d)) or bool(set(last.lower().split('_')) & SEG)


# ### THE WORKLIST, BY ITS SYNTAX TREE
def dotted(n):
    if isinstance(n, ast.Name):
        return n.id
    if isinstance(n, ast.Attribute):
        b = dotted(n.value)
        return (b + '.' + n.attr) if b else n.attr
    return ''


def tops(body):
    for st in body:
        if isinstance(st, (ast.If, ast.Try, ast.With)):
            sub = list(st.body) + list(getattr(st, 'orelse', [])) + list(getattr(st, 'finalbody', [])) + [x for h in getattr(st, 'handlers', []) for x in h.body]
            for x in tops(sub):
                yield x
        else:
            yield st


def bound(st):
    if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return [st.name], 'def'
    if isinstance(st, ast.Assign):
        return [n.id for t in st.targets for n in ast.walk(t) if isinstance(n, ast.Name)], 'assign'
    if isinstance(st, (ast.AnnAssign, ast.AugAssign)):
        return ([st.target.id] if isinstance(st.target, ast.Name) else []), 'assign'
    if isinstance(st, (ast.Import, ast.ImportFrom)):
        return [(a.asname or a.name).split('.')[0] for a in st.names], 'import'
    return [], ''


def tree_names(src):
    """{name: [(line, kind, dump, node, cite text)]} of a module's top-level names."""
    L = src.replace('\r', '').split(NL)
    out = {}
    for st in tops(ast.parse(src).body):
        names, kind = bound(st)
        k = st.lineno - 2
        while k >= 0 and L[k].lstrip().startswith('#'):
            k -= 1
        cite = NL.join(L[k + 1:st.end_lineno])
        v = st if kind != 'assign' else st.value
        for nm in names:
            out.setdefault(nm, []).append((st.lineno, kind, ast.dump(v) if v is not None else '', v, cite))
    return out


def tree_reads(node, readers):
    for x in ast.walk(node):
        if isinstance(x, ast.Call):
            d = dotted(x.func)
            if d and (reader_call(d) or d in readers):
                return True
        if isinstance(x, ast.Name) and x.id in readers:
            return True
    return False


# ### THE ACT MODULE, A SECTIONS FILE READ AS TEXT
def scan(s, tq):
    """(the bracket depth's change, the open triple quote after) over one line."""
    d, k = 0, 0
    while k < len(s):
        if tq:
            e = s.find(tq, k)
            if e < 0:
                return d, tq
            k, tq = e + 3, ''
            continue
        if s.startswith('"""', k) or s.startswith("'''", k):
            tq, k = s[k:k + 3], k + 3
            continue
        c = s[k]
        if c in '\'"':
            m = ONE.match(s, k)
            k = m.end() if m else k + 1
            continue
        if c == '#':
            break
        d += 1 if c in '([{' else (-1 if c in ')]}' else 0)
        k += 1
    return d, tq


def code_of(text):
    """the text with its strings and comments taken out, for the reader's calls and the comparison."""
    t = re.sub(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', '""', text)
    t = ONE.sub("''", t)
    return ' '.join(re.sub(r'#.*$', '', l) for l in t.split(NL)).split()


def opening(L, i):
    """the quote a block opens inside: '' where its triple quotes close from a closed start; else the triple quote that closes them from
    an open one (a block the template opens inside a docstring, its closing quote among its lines -- b770's residue, record 34)."""
    j = i + 1
    while j < len(L) and not L[j].startswith('#⟪'):
        j += 1
    for q in ('', '"""', "'''"):
        tq = q
        for k in range(i + 1, j):
            tq = scan(L[k], tq)[1]
        if not tq:
            return q
    return ''


def text_names(src):
    """{tool:name: [(line, kind, code, None, cite text)]} of a sections file's names at the left margin."""
    L = src.replace('\r', '').split(NL)
    out, tool, tq, i = {}, None, '', 0
    while i < len(L):
        l = L[i]
        m = SEC.match(l)
        if m:
            tool, tq, i = m.group(2), opening(L, i), i + 1
            continue
        if l.startswith('#⟪'):
            tool = None if l.startswith('#⟪END') else tool
            i += 1
            continue
        mm = None if (tool is None or tq) else (DEFN.match(l) or ASSIGN.match(l))
        if not mm:
            if tool is not None:
                tq = scan(l, tq)[1]
            i += 1
            continue
        kind = 'def' if DEFN.match(l) else 'assign'
        name = mm.group(2) if kind == 'def' else mm.group(1)
        j, depth, tq2 = i, 0, ''
        while j < len(L) and not L[j].startswith('#⟪'):
            if j > i:
                s = L[j]
                if kind == 'assign' and depth <= 0 and not tq2 and not L[j - 1].rstrip().endswith('\\'):
                    break
                if kind == 'def' and not tq2 and s.strip() and not s[0].isspace() and not s.startswith('#'):
                    break
            dd, tq2 = scan(L[j], tq2)
            depth += dd
            j += 1
        k = i - 1
        while k >= 0 and L[k].lstrip().startswith('#') and not L[k].startswith('#⟪'):
            k -= 1
        out.setdefault('%s:%s' % (tool, name), []).append((i + 1, kind, ' '.join(code_of(NL.join(L[i:j]))), None, NL.join(L[k + 1:j])))
        i = j
    return out


def margin(cur, R):
    """the second shape: (the lines inside a block at the margin of an assignment's or a def's shape, the distinct tool:names on them,
    those of them the reader read), with no string or statement read."""
    L = io.open(os.path.join(ROOT, *cur.split('/')), encoding='utf-8').read().replace('\r', '').split(NL)
    tool, n, names = None, 0, set()
    for l in L:
        m = SEC.match(l)
        if m:
            tool = m.group(2)
            continue
        if l.startswith('#⟪'):
            tool = None if l.startswith('#⟪END') else tool
            continue
        mm = tool and (DEFN.match(l) or ASSIGN.match(l))
        if mm:
            n += 1
            names.add('%s:%s' % (tool, mm.group(2) if DEFN.match(l) else mm.group(1)))
    return n, len(names), len(names & set(R))


def text_reads(code, refs, tool):
    """True where the code calls a reader or names a name of its own tool read so (refs: {tool: one pattern of those names})."""
    if any(reader_call(c) for c in CALL.findall(code)):
        return True
    return bool(refs.get(tool) and refs[tool].search(code))


def ref_patterns(readers):
    by = {}
    for r in readers:
        t, n = r.split(':', 1)
        by.setdefault(t, []).append(re.escape(n))
    return dict((t, re.compile(r'(?<![\w.])(?:%s)(?!\w)' % '|'.join(sorted(ns, key=len, reverse=True)))) for t, ns in by.items())


# ### THE CLASSES
def classify(cur, prev, form, subs, ruling, stage_one):
    """{name: (class, why, line)} for the act's text against the previous act's."""
    C = tree_names(cur) if form == 'tree' else text_names(cur)
    P = tree_names(subst(prev, subs)) if form == 'tree' else text_names(subst(prev, subs))
    readers, grew = set(), True
    while grew:
        grew = False
        refs = ref_patterns(readers) if form == 'text' else None
        for nm, es in C.items():
            if nm in readers or all(e[1] == 'import' for e in es):
                continue
            if form == 'tree':
                hit = any(e[3] is not None and tree_reads(e[3], readers) for e in es)
            else:
                hit = any(text_reads(e[2], refs, nm.split(':', 1)[0]) for e in es)
            if hit:
                readers.add(nm)
                grew = True
    cite = re.compile(r'\(%s\)|%s\)\(' % (re.escape(ruling), re.escape(ruling)))
    out = {}
    for nm, es in C.items():
        line = es[0][0]
        if nm in readers:
            out[nm] = ('READ', 'run time', line)
            continue
        if form == 'tree' and nm in stage_one:
            out[nm] = ('READ', 'step zero', line)
            continue
        cited = any(cite.search(e[4]) for e in es)
        if nm not in P:
            out[nm] = ('RULED', 'new' + (', cited' if cited else ''), line)
        elif sorted(set(e[2] for e in es)) != sorted(set(e[2] for e in P[nm])):   # ### as sets: a line repeated (an import the carry wrote twice) is no move
            out[nm] = ('RULED', 'moved' + (', cited' if cited else ''), line)
        elif cited:
            out[nm] = ('RULED', 'cited', line)
        else:
            out[nm] = ('STANDING', 'import' if all(e[1] == 'import' for e in es) else '', line)
    return out


PW0 = ['import json', "A = json.load(open('data/x.json'))", 'def _rows():', "    return open('data/y.txt').read()", '', '', 'B = _rows()', 'CAP = 0',
       'NL = chr(10)', "DATE = '2026-11-25'", 'Z = 1', "T = 'b998 tag'"]
PW1 = ['import json'] + PW0[:7] + ['CAP = 40', 'NL = chr(10)', "DATE = '2026-11-26'", '# ### (R999)(9): set by the ruling', 'Z = 1', "T = 'b999 tag'", "W = 'new'"]
WANT_W = dict(json='STANDING', A='READ', _rows='READ', B='READ', CAP='RULED', NL='STANDING', DATE='READ', Z='RULED', T='STANDING', W='RULED')
PS0 = ['#⟪SECTION record 1⟫', 'CAP2 = 0', 'NL2 = chr(10)', "R2 = io.open('data/z.txt').read()", 'R3 = R2[:4]', "T2 = 'b998 x'", 'def f2():', '    """a docstring',
       'FAKE = 1', '    """', '    return 1', '    INNER = 3', '#⟪END⟫']
PS1 = ['#⟪SECTION record 1⟫', 'CAP2 = (36,', '        0)', 'NL2 = chr(10)   # ### (R998) a cite of an older ruling', "R2 = io.open('data/z.txt').read()",
       'R3 = R2[:4]', "T2 = 'b999 x'", 'def f2():', '    """a docstring', 'FAKE = 1', '    """', '    return 1', '    INNER = 3', '#⟪END⟫']
PS_IN = ['#⟪SECTION record 2⟫', '    the end of a docstring the template opened."""', 'G2 = 1', '#⟪END⟫']   # ### a block opening inside a string
PS0, PS1 = PS0 + PS_IN, PS1 + PS_IN
WANT_S = {'record:CAP2': 'RULED', 'record:NL2': 'STANDING', 'record:R2': 'READ', 'record:R3': 'READ', 'record:T2': 'STANDING', 'record:f2': 'STANDING',
          'record:G2': 'STANDING'}


def controls():
    w = classify(NL.join(PW1) + NL, NL.join(PW0) + NL, 'tree', (('b998', 'b999'),), 'R999', ('DATE',))
    s = classify(NL.join(PS1) + NL, NL.join(PS0) + NL, 'text', (('b998', 'b999'),), 'R999', ())
    gw = dict((k, v[0]) for k, v in w.items())
    gs = dict((k, v[0]) for k, v in s.items())
    return [('a planted worklist pair: %s' % ' ; '.join('%s %s' % (k, gw.get(k, 'ABSENT')) for k in sorted(WANT_W)), gw == WANT_W and w['DATE'][1] == 'step zero'),
            ('a planted sections pair: %s ; names read %d (FAKE in a docstring and INNER indented read as none; G2 after a block`s opening inside a string read)' % (
                ' ; '.join('%s %s' % (k.split(':')[1], gs.get(k, 'ABSENT')) for k in sorted(WANT_S)), len(gs)), gs == WANT_S)]


def guard_ids(text):
    import b770_address_scan as SC
    import project_set as PS
    I = (SC.author_name(), SC.author_orcid(), SC.previous_address(), 'github.com/', PS.owner() or '')
    low = text.lower()
    return sum(low.count(x.lower()) for x in I if x)


def run(mode):
    ctl = controls()
    for t, ok in ctl:
        print('  %-150s %s' % (t, 'AS WANTED' if ok else 'NOT AS WANTED'))
    n_ok = sum(1 for _t, ok in ctl if ok)
    if mode == 'control':
        print('### CONTROLS %d OF %d AS WANTED' % (n_ok, len(ctl)))
        return
    import carry as CA
    at = utc()
    res = []
    for cur, prev, form in FILES:
        src = io.open(os.path.join(ROOT, *cur.split('/')), encoding='utf-8').read()
        psrc = io.open(os.path.join(ROOT, *prev.split('/')), encoding='utf-8').read()
        res.append((cur, prev, form, classify(src, psrc, form, SUBS, RULING, CA.STAGE_ONE if form == 'tree' else ())))
    L = ['b770 -- STEP ZERO, (R380)(3): THE NAMES CLASSED, a reading with no repair ordered on it (%s)' % at, '',
         '### tools/b770_names.py %s: each top-level name of tools/b769_worklist.py (its syntax tree) and of tools/acts/b769.py (a sections file, its' % mode,
         '### names at the left margin keyed by tool) classed READ (its value from git or a bank at run time, or a stage-one value set so at step',
         '### zero, counted apart), RULED (else, its value differing from b768`s after the substitution, new at b769, or cited to (R379)) or',
         '### STANDING (neither); the predicate is the tool`s docstring; no line of either module printed but its names.', '', '## THE CONTROLS']
    if mode == 'again':   # ### the earlier bank named in this one's head, by its digest, its time and its totals
        import hashlib
        ob = open(BANK, 'rb').read()
        ot = ob.decode('utf-8').split(NL)
        last = [x for x in ot if x.startswith('### ### ')]
        L[6:6] = ['### WRITTEN AGAIN over the earlier bank (sha256 %s, written %s), whose residue was read by hand after it was written: its' % (
                      hashlib.sha256(ob).hexdigest()[:16], (re.findall(r'\((\d{4}-[\d-]+T[\d:]+Z)\)$', ot[0]) or ['at no time read'])[0]),
                  '### sections reader read a block that opens inside a docstring (record 34) as opening a string, so the names after that block`s',
                  '### closing quote went unread; its totals: %s' % (last[-1][8:].strip('*') if last else 'none')]
    L += ['  %-150s %s' % (t, 'AS WANTED' if ok else 'NOT AS WANTED') for t, ok in ctl]
    L += ['', '## THE COUNTS']
    tot = dict(READ=0, RULED=0, STANDING=0)
    for cur, prev, form, R in res:
        c = dict((k, sum(1 for v in R.values() if v[0] == k)) for k in tot)
        for k in tot:
            tot[k] += c[k]
        sub = lambda k, w: sum(1 for v in R.values() if v[0] == k and v[1].startswith(w))
        L.append('  %s against %s: names %d ; READ %d (at run time %d, at step zero %d) ; RULED %d (moved %d, new %d, cited alone %d ; cited to (R379) %d) ; '
                 'STANDING %d (imports %d)' % (cur, prev, len(R), c['READ'], sub('READ', 'run'), sub('READ', 'step'), c['RULED'], sub('RULED', 'moved'),
                                                sub('RULED', 'new'), sub('RULED', 'cited'), sum(1 for v in R.values() if v[0] == 'RULED' and 'cited' in v[1]),
                                                c['STANDING'], sub('STANDING', 'import')))
        if form == 'text':
            tools = sorted(set(k.split(':')[0] for k in R))
            L.append('    the sections reader`s yield by tool: %s' % ' ; '.join('%s %d' % (t, sum(1 for k in R if k.startswith(t + ':'))) for t in tools))
            L.append('    the second shape beside it: lines inside a block at the margin opening an assignment or a def %d, distinct names on them %d, '
                     'read as names %d (the rest inside a triple-quoted string or a statement`s continuation)' % margin(cur, R))
    L.append('  IN ALL: names %d ; READ %d ; RULED %d ; STANDING %d' % (sum(tot.values()), tot['READ'], tot['RULED'], tot['STANDING']))
    for cur, prev, form, R in res:
        rr = sorted((v[2], k, v[1]) for k, v in R.items() if v[0] == 'RULED')
        L += ['', '## THE NAMES CLASSED RULED, %s (%d), by line: the name -- why' % (cur, len(rr))]
        L += ['  :%d %s -- %s' % x for x in rr]
    L += ['', '### ### **THE NAMES CLASSED: NAMES %d ; READ %d ; RULED %d ; STANDING %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
        sum(tot.values()), tot['READ'], tot['RULED'], tot['STANDING'], n_ok, len(ctl), 'DRY, NOTHING WRITTEN' if mode == 'dry' else ('WRITTEN AGAIN' if mode == 'again' else 'WRITTEN'))]
    text = NL.join(L) + NL
    if guard_ids(text):
        die('AN IDENTIFIER IN THE COMPOSED BANK')
    print(text)
    if mode in ('write', 'again'):
        if n_ok != len(ctl):
            die('CONTROLS %d OF %d' % (n_ok, len(ctl)))
        if os.path.exists(BANK) and mode == 'write':
            die('data/b770_names.txt STANDS')
        if mode == 'again' and not os.path.exists(BANK):
            die('`again` WITH NO BANK STANDING')
        import act_membrane as MEM
        try:
            import b770_record as REC
            ex = REC.R.ROOT_EXCLUDE
        except Exception:
            ex = None
        MEM.guard_path(ACT, BANK, ex)
        with open(BANK + '.tmp', 'wb') as f:
            f.write(text.encode('utf-8'))
        os.replace(BANK + '.tmp', BANK)
        print('written data/b770_names.txt: %d lines' % len(L))


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m not in ('control', 'dry', 'write', 'again'):
        sys.exit(__doc__)
    run(m)
