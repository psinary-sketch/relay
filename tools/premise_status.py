# -*- coding: utf-8 -*-
"""premise_status.py -- THE PREMISE STATUS, A SHARED TOOL: the readers b639 wrote inside its record tool under (R249)(2), carried here whole so
the census and later acts read one source. ### Read-only: every function reads a kernel by git at a pin and returns; nothing here writes.

### A head's facts are read from the kernels its rows sit in, at the commit the terminal table read each row at: the declarations concluding
### the head (decls_concluding), its inline have / let / show constructions (inline_of), its own declaration and docstring (declaration_of).
### classify4 is (R249)(2)'s rule as the author answered before b639's seal: DISCHARGED IN KERNEL, DISCHARGED ELSEWHERE, CITED, OPEN, the first
### the head meets in that order.
"""
import collections  # noqa: F401
import io  # noqa: F401
import json  # noqa: F401
import os
import re
import subprocess

NL = chr(10)
SALT_MARK = 'SaltCheck'
STATUSES4 = ('DISCHARGED IN KERNEL', 'DISCHARGED ELSEWHERE', 'CITED', 'OPEN')
TIER_MARKS = r'\bT0\b|\bT1-open\b|\bT2\b|\bT3\b|\bT4\b'
DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|unsafe|partial)\s+)*(theorem|lemma|def|abbrev|instance|example)\b(.*)$")
OPEN_B, CLOSE_B = '({[⦃', ')}]⦄'
REL = re.compile(r'(↔|(?<![<>:=!])=(?![=>])|≤|<|≠)')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')


def strip_comments(t):
    """### block comments /- ... -/ (nested) and line comments -- blanked to spaces, every newline kept, so line numbers stand."""
    out, i, depth = [], 0, 0
    while i < len(t):
        if t.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            out.append('  ')
            i += 2
            continue
        if not depth and t.startswith('--', i):
            j = t.find(NL, i)
            j = len(t) if j < 0 else j
            out.append(' ' * (j - i))
            i = j
            continue
        ch = t[i]
        out.append(ch if (ch == NL or not depth) else ' ')
        i += 1
    return ''.join(out)


def _target(t):
    depth, cut = 0, 0
    for i, ch in enumerate(t):
        if ch in OPEN_B:
            depth += 1
        elif ch in CLOSE_B:
            depth -= 1
        elif ch == '→' and depth == 0:
            cut = i + 1
    return t[cut:].strip()


def conclusion(sig):
    """### the text after the last top-level ':' of a signature (before ':='), its last top-level '→' target, any ∀-prefix stripped."""
    depth, last = 0, -1
    for i, ch in enumerate(sig):
        if ch in OPEN_B:
            depth += 1
        elif ch in CLOSE_B:
            depth -= 1
        elif ch == ':' and depth == 0 and sig[i:i + 2] != ':=':
            last = i
    if last < 0:
        return ''
    t = _target(' '.join(sig[last + 1:].split()))
    for _ in range(4):
        m = re.match(r'^∀\s+[^,]*,\s*', t)
        if not m:
            break
        t = _target(t[m.end():])
    return t


def head_tok(t):
    m = re.match(r"([^\W\d][\w'₀-₉]*(?:\.[^\W\d][\w'₀-₉]*)*)", t.lstrip('( '))
    return m.group(1).split('.')[-1] if m else None


def hyp_binders(sig):
    """### the declaration's own hypotheses: every binder the rule types a Prop, instance binders apart."""
    import e0_rule as E
    hd = ' '.join(re.sub(r'^\S+', '', re.sub(r'^.*?\b(theorem|lemma|def|abbrev|instance|example)\b\s*', '', sig, count=1), count=1).split())
    try:
        return ['%s : %s' % (b['name'], b['type']) for b in E.binders_of(hd) if b['typing'] == 'prop' and b['kind'] != 'instance']
    except Exception as ex:
        return ['### UNREAD: %s' % ex]


def decls_concluding(repo, pin, head):
    files = [l.split(':', 1)[1] for l in g(repo, 'grep', '-l', '-w', head, pin, '--', '*.lean').split(NL) if ':' in l]
    out = []
    for f in files:
        src = strip_comments(g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')).split(NL)
        i = 0
        while i < len(src):
            m = DECL.match(src[i])
            if not m:
                i += 1
                continue
            j, buf = i, []
            while j < len(src) and j < i + 40:
                buf.append(src[j])
                if ':=' in src[j] or re.search(r'\bwhere\s*$', src[j]) or (j > i and src[j].startswith('  |')):
                    break
                j += 1
            sig = ' '.join(' '.join(buf).split(':=')[0].split())
            sig = re.sub(r'\s+where\s*$', '', sig)
            sig = re.sub(r'\s\|\s.*$', '', sig)
            c = conclusion(sig)
            if head_tok(c) == head:
                out.append(dict(file=f, line=i + 1, kind=m.group(1), conclusion=c[:200], text=sig[:240], hyps=hyp_binders(sig),
                                salt=(SALT_MARK in f), relation=bool(REL.search(c))))
            i = j + 1
    return out


def inline_of(repo, pin, head):
    out = []
    pat = r'((have|let)\b[^:=]*:\s*\(?([A-Za-z_][A-Za-z0-9_]*\.)*%s\b)|(\bshow\s+\(?([A-Za-z_][A-Za-z0-9_]*\.)*%s\b)' % (re.escape(head), re.escape(head))
    for l in g(repo, 'grep', '-n', '-E', pat, pin, '--', '*.lean').split(NL):
        if l.count(':') >= 3:
            _p, f, ln, t = l.split(':', 3)
            src = strip_comments(g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')).split(NL)
            live = int(ln) <= len(src) and re.search(pat, src[int(ln) - 1]) is not None
            out.append(dict(file=f, line=int(ln), text=' '.join(t.split())[:200], salt=(SALT_MARK in f), iff=('↔' in t), live=live))
    return out


def declaration_of(repo, pin, head):
    hits = g(repo, 'grep', '-n', '-E', r'^\s*(structure|class|def|abbrev|inductive|noncomputable def)\s+([A-Za-z_.]*\.)?%s(\s|$|:)' % re.escape(head),
             pin, '--', '*.lean')
    for h in [x for x in hits.split(NL) if x.count(':') >= 3]:
        _pin, f, ln, _t = h.split(':', 3)
        src = g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '').split(NL)
        k = int(ln) - 2
        doc = []
        if k >= 0 and src[k].rstrip().endswith('-/'):
            while k >= 0:
                doc.insert(0, src[k])
                if src[k].lstrip().startswith('/-'):
                    break
                k -= 1
        return dict(file=f, line=int(ln), text=_t.strip()[:200], doc=NL.join(doc))
    return None


def cited_whole(doc):
    """### every field cited: the docstring carries T1-lit and no other tier mark."""
    lines = [l.strip() for l in (doc or '').split(NL) if re.search(r'T1[- ]?lit', l)]
    others = sorted(set(re.findall(TIER_MARKS, doc or '')))
    return bool(lines) and not others, lines, others


def classify4(dik, elsewhere, cited):
    """### (R249)(2) as answered before b639's seal: the first status of four the head meets."""
    meets = [s for s, ok in zip(STATUSES4[:3], (dik, elsewhere, cited)) if ok] or ['OPEN']
    return meets[0], meets


# ================================================================================ b640, (R250)(3): FIVE STATUSES, READ FROM THE USE SITE
# ### As the author answered before b640's seal: DOMAIN is a predicate of Mathlib's (its declaration outside every kernel) that every row resting
# ### on it applies to a variable the row's statement quantifies -- not a premise, removed to the domain-condition list with its variable named;
# ### DISCHARGED, a construction outside the SaltCheck files that a proof consumes (an inline have / let / show inside a proof, or a declaration
# ### concluding the head with no Prop hypothesis whose name another declaration uses, the consumer outside SaltCheck and AxiomCheck files and
# ### not itself a witness); CITED, every field T1-lit; WITNESSED, constructions outside the salt checks and none consumed; OPEN otherwise, a
# ### head constructed inside salt checks alone among them. Each head takes the first it meets in that order.
STATUSES5 = ('DOMAIN', 'DISCHARGED', 'CITED', 'WITNESSED', 'OPEN')
WITNESS_NAME = re.compile(r'nonvacuous|inhabited|toy|empty|witness|example', re.I)
_TOK = re.compile(r"[^\W\d][\w'₀-₉]*(?:\.[^\W\d][\w'₀-₉]*)*")


def classify5(f):
    """### the five-status rule over a head's facts, pure: f carries upstream, domain_vars (one list per row, the quantified variables the head is
    ### applied to; empty where none), consumed (constructions outside the salt checks some non-witness proof uses), inline (inline constructions
    ### outside the salt checks), standalone (constructions outside the salt checks), cited. RETURN (status, the tests it meets)."""
    rowsd = f.get('domain_vars') or []
    tests = [('DOMAIN', bool(f.get('upstream')) and bool(rowsd) and all(rowsd)),
             ('DISCHARGED', bool(f.get('consumed')) or bool(f.get('inline'))),
             ('CITED', bool(f.get('cited'))),
             ('WITNESSED', bool(f.get('standalone')))]
    meets = [s for s, ok in tests if ok] or ['OPEN']
    return meets[0], meets


def domain_vars(h, hd, pb, binders):
    """### the variables the row's statement quantifies that its premise binder on h applies h to (dot form p.Prime read with p)."""
    bound = set()
    for b in binders:
        for n in re.split(r'\s+', b.get('name') or ''):
            if n and n != '→':
                bound.add(n)
    out = []
    for b in pb:
        t = ' '.join(b['type'].split())
        m = re.search(r'(?<![\w.])((?:[\w.]*\.)?)%s\b' % re.escape(h), t)
        if not m:
            continue
        rest = t[m.end():]
        dotted = [x for x in m.group(1).rstrip('.').split('.') if x]
        qv = set(x for s in re.findall(r'∀\s+([^,:]+)', t) for x in s.split())
        out += sorted((set(_TOK.findall(rest)) | set(dotted)) & (bound | qv) - {h})
    return sorted(set(out))


def enclosing_decl(src_lines, line):
    for i in range(min(line, len(src_lines)) - 1, -1, -1):
        m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|instance|example)\s*([^\s({\[:]*)',
                     src_lines[i])
        if m:
            return m.group(2) or m.group(1)
    return ''


def consumers(repo, pin, name, own_file, own_line):
    """### every line at the pin naming the construction outside its own declaration, outside SaltCheck and AxiomCheck files, and outside a
    ### declaration whose name marks a witness: RETURN [(file:line, enclosing declaration)]."""
    short = name.split('.')[-1]
    if not short or WITNESS_NAME.search(short):
        return []
    out, cache = [], {}
    for l in g(repo, 'grep', '-n', '-w', short, pin, '--', '*.lean').split(NL):
        if l.count(':') < 3:
            continue
        _p, f, ln, t = l.split(':', 3)
        ln = int(ln)
        if SALT_MARK in f or os.path.basename(f).startswith('AxiomCheck') or '#print' in t or '#check' in t:
            continue
        if f == own_file and ln == own_line:
            continue
        if f not in cache:
            cache[f] = strip_comments(g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')).split(NL)
        if ln <= len(cache[f]) and not re.search(r'\b%s\b' % re.escape(short), cache[f][ln - 1]):
            continue
        enc = enclosing_decl(cache[f], ln)
        if enc.split('.')[-1] == short or WITNESS_NAME.search(enc):
            continue
        out.append(('%s:%d' % (f, ln), enc))
    return out
