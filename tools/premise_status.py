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
