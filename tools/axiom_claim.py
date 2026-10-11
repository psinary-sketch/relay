# -*- coding: utf-8 -*-
"""axiom_claim.py -- THE ARM G-AXIOM-CLAIM, a standalone tool under (R259)(2)(b), an arm of every suite from b649.

### Every docstring (`/-- -/`) and every module doc block (`/-! -/`) of every .lean file on every kernel's main (the kernels of
### tools/no_sorry_main.py) is read for a claim about axioms: a sentence carrying axiom, axioms, propext, Quot.sound, Classical.choice,
### "standard three", std3, "zero axioms", "no axioms", sorryAx or native_decide. Each claim is read for the profile it states:
###   EMPTY      -- "zero axioms", "no axioms", "axiom-free", "does not depend on any axioms" (not followed by beyond/other than/except);
###   LIST       -- an explicit bracketed list of axiom names: the print must lie within it;
###   STD3       -- "standard three", std3, or the three named together: the print must lie within [propext, Classical.choice, Quot.sound];
###   EXCLUDES   -- "no / without / free of" a named axiom (native_decide read as Lean.ofReduceBool): the print must not carry it;
###   REQUIRES   -- "depends on / carries / uses ... sorryAx": the print must carry sorryAx.
### A sentence carrying an axiom word and none of these is a MENTION: printed and not scored. The claim covers the declaration the docstring
### heads (a docstring heading no declaration covers none) and every declaration of the file for the module header, the `/-!` block at the
### file's head -- for a module declaring nothing (an AxiomCheck module), the declarations its `#print axioms` lines name; a `/-!` block after the head is neither and is out of scope, counted. Each covered declaration is looked up in the banked prints (`index()`): the compiler's lines
### `'Name' depends on axioms: [...]` and `'Name' does not depend on any axioms` in relay's tracked data banks (text, wrapped prints joined,
### and JSON strings read as tools/terminal_table.py reads them), the `Name: [...]` lines of relay data/b642_declarations.txt, and any
### captured print a kernel's main carries; for a name printed more than once the latest act's bank stands (the act read from the bank's
### name). A claim is CONTRADICTED when a covered declaration's print breaks it -- the arm FAILS, printing the claim, the declaration and
### the print; UNVERIFIABLE when no covered declaration has a banked print -- printed; VERIFIED otherwise, its printed and unprinted counts
### given. A name is matched exactly, else to the one banked name ending with it (an outer namespace unread); never to a different
### declaration that shares its last component.
###
### Usage:  python tools/axiom_claim.py [--bank data/<name>.txt] [kernel ...]
### Library: index(), claims_in(text), parse(sentence), classify_text(kernel, path, text, idx), run(kernels, idx)
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import no_sorry_main as NSM   # noqa: E402

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STD3 = frozenset(['propext', 'Classical.choice', 'Quot.sound'])
AXN = r'(?:propext|Classical\.choice|Quot\.sound|sorryAx|Lean\.ofReduceBool|Lean\.trustCompiler)'
AXIOM_WORD = re.compile(r'\baxioms?\b|\bpropext\b|\bQuot\.sound\b|\bClassical\.choice\b|standard three|\bstd3\b|zero axioms|no axioms|'
                        r'\bsorryAx\b|\bnative_decide\b', re.I)
EMPTY_RE = re.compile(r'\b(?:zero axioms|no axioms?|axiom[- ]free|does not depend on any axioms|0 axioms)\b'
                      r'(?![^.;]{0,30}\b(?:beyond|other than|besides|except|outside)\b)', re.I)
LIST_RE = re.compile(r'[\[{]\s*(%s(?:\s*,\s*%s)*)\s*[\]}]' % (AXN, AXN))
STD3_RE = re.compile(r'standard three|\bstd3\b|(?=[\s\S]*\bpropext\b)(?=[\s\S]*\bClassical\.choice\b)(?=[\s\S]*\bQuot\.sound\b)', re.I)
NEG_RE = re.compile(r'\b(?:no|without|free of|never)\b[^.;]{0,40}?\b(sorryAx|native_decide|Classical\.choice|propext|Quot\.sound|'
                    r'Lean\.ofReduceBool)\b|\b(sorryAx|native_decide)[- ]free\b')
POS_SORRY = re.compile(r'\b(?:depends on|carries|uses|includes|rests on)\b[^.;]{0,40}?\bsorryAx\b')
PRINT_LINE = re.compile(r"'([^'\s]+)'[ \t]+(does not depend on any axioms|depends on axioms:[ \t]*\[([^\]]*)\])")
B642 = 'data/b642_declarations.txt'
B642_LINE = re.compile(r"^\s+([A-Za-z_][\w.'’₀-₉]*): \[([^\]]*)\]\s*$", re.M)
ACT = re.compile(r'(?:^|/)_?b(\d{2,4})[_/]')
DECL = re.compile(r"^[ \t]*(?:@\[[^\]]*\][ \t]*)*(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped)[ \t]+)*"
                  r"(theorem|lemma|def|abbrev|instance|structure|class|inductive|axiom|opaque|example)\b[ \t]*([^\s:(\[{]*)", re.M)
NS = re.compile(r'^[ \t]*(namespace|section|end)\b[ \t]*([\w.]*)', re.M)


def _set(s):
    return frozenset(x.strip() for x in s.split(',') if x.strip())


def _act(path):
    m = ACT.search(path)
    return int(m.group(1)) if m else 0


def _git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def prints_in_text(t):
    """{name: set} from the compiler's print lines in a text, a print wrapped over lines joined."""
    t = re.sub(r'depends on axioms:[ \t]*\[([^\]]*)\]', lambda m: 'depends on axioms: [' + ' '.join(m.group(1).split()) + ']', t)
    out = {}
    for m in PRINT_LINE.finditer(t):
        out[m.group(1)] = frozenset() if m.group(2).startswith('does not') else _set(m.group(3))
    return out


def index():
    """{name: (set, source, act)} over relay's tracked data banks at HEAD, b642's declarations and the kernels' captured prints; and the
    count of names and banks each source gave."""
    import terminal_table as T
    idx, counts = {}, {}

    def put(n, s, src, act):
        if n not in idx or act >= idx[n][2]:
            idx[n] = (s, src, act)
    rc, out = _git(ROOT, 'grep', '-l', '-e', 'depends on axioms', '-e', 'does not depend on any axioms', 'HEAD', '--', 'data/')
    files = sorted(x.split(':', 1)[1] for x in out.split(NL) if ':' in x)
    nt = nj = 0
    for f in files:
        rc, t = _git(ROOT, 'show', 'HEAD:' + f)
        if rc:
            continue
        if f.endswith('.json'):
            try:
                pr = dict((n, (frozenset() if p.startswith('does not') else _set(p.split('[', 1)[1].rsplit(']', 1)[0])))
                          for n, p in T.profiles_from_obj(json.loads(t)).items())
            except Exception:
                pr = {}
            nj += bool(pr)
        else:
            pr = prints_in_text(t)
            nt += bool(pr)
        for n, s in pr.items():
            put(n, s, 'relay:' + f, _act(f))
    rc, t = _git(ROOT, 'show', 'HEAD:' + B642)
    b6 = dict((m.group(1), _set(m.group(2))) for m in B642_LINE.finditer(t or '')) if not rc else {}
    for n, s in b6.items():
        put(n, s, 'relay:' + B642, 642)
    nk = 0
    for k in NSM.kernels():
        fs, _src, outp = T.prints_at('D:/' + k, 'main')
        for n, d in outp.items():
            p = d['profile']
            put(n, frozenset() if p.startswith('does not') else _set(p.split('[', 1)[1].rsplit(']', 1)[0]), '%s@main:%s' % (k, d['file']), 10 ** 6)
            nk += 1
    counts = dict(text_banks=nt, json_banks=nj, b642_names=len(b6), kernel_prints=nk, names=len(idx))
    return idx, counts


def _short_map(idx):
    m = {}
    for n in idx:
        m.setdefault(n.split('.')[-1], []).append(n)
    return m


def lookup(idx, smap, qname):
    """the banked name for a declaration: its own qualified name, else the one banked name that ends with it (an outer namespace the
    source read did not see); never a different declaration sharing its last component."""
    if qname in idx:
        return qname, 'EXACT'
    c = [n for n in smap.get(qname.split('.')[-1], []) if n.endswith('.' + qname)]
    if len(c) == 1:
        return c[0], 'SUFFIX'
    return None, None


def doc_blocks(text):
    """[(opener, start offset, end offset, body)] for every top-level `/--` and `/-!` comment."""
    out = []
    i, n, depth, start, opener = 0, len(text), 0, None, None
    code = NSM.lean_code(text)
    while i < n:
        if depth == 0:
            if text.startswith('/-', i) and code[i] == ' ' and (i == 0 or code[i - 1] != '"'):
                depth, start, opener = 1, i, text[i:i + 3]
                i += 2
                continue
            if text.startswith('--', i):
                j = text.find(NL, i)
                i = n if j < 0 else j
                continue
            if text[i] == '"':
                j = i + 1
                while j < n and text[j] != '"':
                    j += 2 if text[j] == '\\' else 1
                i = j + 1
                continue
            i += 1
            continue
        if text.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if text.startswith('-/', i):
            depth -= 1
            i += 2
            if depth == 0 and opener in ('/--', '/-!'):
                out.append((opener, start, i, text[start + 3:i - 2]))
            continue
        i += 1
    return out


def decls(text):
    """[(offset, kind, qualified name)] of the file's declarations, the namespace read from the code."""
    code = NSM.lean_code(text)
    events = [(m.start(), 'ns', m.group(1), m.group(2)) for m in NS.finditer(code)]
    events += [(m.start(), 'decl', m.group(1), m.group(2)) for m in DECL.finditer(code)]
    events.sort()
    stack, out = [], []
    for off, ev, a, b in events:
        if ev == 'ns':
            if a == 'namespace':
                stack.append(('ns', b))
            elif a == 'section':
                stack.append(('sec', b))
            elif stack:
                stack.pop()
            continue
        name = b.strip()
        if not name or a == 'example':
            out.append((off, a, None))
            continue
        if name.startswith('_root_.'):
            q = name[len('_root_.'):]
        else:
            q = '.'.join([x for t, x in stack if t == 'ns' and x] + [name])
        out.append((off, a, q))
    return out


SPLIT = re.compile(r'(?<=[.;:])\s+(?=[A-Z`(*\[])|\n\s*\n|\n\s*(?:[-*•]|\d+[.)])\s')


def claims_in(body):
    return [' '.join(s.split()) for s in SPLIT.split(body) if s and AXIOM_WORD.search(s)]


def parse(s):
    """(allowed or None, forbidden, required, kind) the sentence states; kind MENTION when it states none."""
    allowed, forb, req, kinds = None, set(), set(), []
    if EMPTY_RE.search(s):
        allowed, kinds = frozenset(), ['EMPTY']
    else:
        lm = LIST_RE.search(s)
        if lm:
            allowed, kinds = _set(lm.group(1)), ['LIST']
        elif STD3_RE.search(s):
            allowed, kinds = STD3, ['STD3']
    for m in NEG_RE.finditer(s):
        x = m.group(1) or m.group(2)
        forb.add('Lean.ofReduceBool' if x == 'native_decide' else x)
    if forb:
        kinds.append('EXCLUDES')
    if POS_SORRY.search(s) and 'sorryAx' not in forb:
        req.add('sorryAx')
        kinds.append('REQUIRES')
    return allowed, frozenset(forb), frozenset(req), ('+'.join(kinds) if kinds else 'MENTION')


def breaks(p, allowed, forb, req):
    return bool((allowed is not None and (p - allowed)) or (forb & p) or (req - p))


def classify_text(kernel, path, text, idx, smap=None):
    """the claim rows of one file: [dict(kernel, file, line, block, sentence, kind, covered, printed, verdict, contradicted)]."""
    smap = smap if smap is not None else _short_map(idx)
    ds = decls(text)
    blocks = doc_blocks(text)
    first_decl = ds[0][0] if ds else len(text)
    bangs = [b for b in blocks if b[0] == '/-!']
    rows = []
    for op, s, e, body in blocks:
        cs = claims_in(body)
        if not cs:
            continue
        if op == '/--':
            nxt = [d for d in ds if d[0] >= e]
            gap = text[e:nxt[0][0]] if nxt else 'x'
            cov = [nxt[0][2]] if nxt and not re.sub(r'@\[[^\]]*\]', '', gap).strip() and nxt[0][2] else []
            blk = 'docstring'
        elif s < first_decl and bangs and bangs[0][1] == s:
            cov, blk = [d[2] for d in ds if d[2]], 'header'
            if not cov:
                # ### a module that declares nothing and prints (an AxiomCheck module): its header covers the declarations it prints
                cov = re.findall(r"^[ \t]*#print[ \t]+axioms[ \t]+([^\s]+)", NSM.lean_code(text), re.M)
        else:
            # ### a `/-!` block after the file's head is neither a docstring nor the module header: out of the ruling's scope, counted
            rows.append(dict(kernel=kernel, file=path, line=text.count(NL, 0, s) + 1, block='section', sentence='', kind='OUT OF SCOPE',
                             covered=0, printed=0, contradicted=[], verdict='OUT OF SCOPE', claims=len(cs)))
            continue
        line = text.count(NL, 0, s) + 1
        for c in cs:
            allowed, forb, req, kind = parse(c)
            row = dict(kernel=kernel, file=path, line=line, block=blk, sentence=c[:300], kind=kind, covered=len(cov), printed=0,
                       contradicted=[], verdict='MENTION')
            if kind == 'MENTION':
                rows.append(row)
                continue
            for q in cov:
                hit, how = lookup(idx, smap, q)
                if not hit:
                    continue
                row['printed'] += 1
                p, src, _a = idx[hit]
                if breaks(p, allowed, forb, req):
                    row['contradicted'].append(dict(decl=q, matched=hit, how=how, print=sorted(p), source=src))
            row['verdict'] = 'CONTRADICTED' if row['contradicted'] else ('VERIFIED' if row['printed'] else 'UNVERIFIABLE')
            rows.append(row)
    return rows


def lean_files(path):
    rc, main = _git(path, 'rev-parse', 'main')
    main = main.strip()
    rc, out = _git(path, 'ls-tree', '-r', '--name-only', main)
    return main, [f for f in out.split(NL) if f.endswith('.lean') and not f.startswith('.lake/')]


def run(names, idx):
    smap = _short_map(idx)
    rows, per = [], {}
    for k in names:
        p = 'D:/' + k
        main, fs = lean_files(p)
        n0 = len(rows)
        for f in fs:
            rc, t = _git(p, 'show', '%s:%s' % (main, f))
            if not rc:
                rows += classify_text(k, f, t, idx, smap)
        per[k] = dict(main=main[:12], files=len(fs), claims=len(rows) - n0)
    return rows, per


def report(rows, per, counts):
    from collections import Counter
    c = Counter(r['verdict'] for r in rows)
    L = ['axiom_claim.py -- THE ARM G-AXIOM-CLAIM ((R259)(2)(b)): every claim about axioms in every docstring and module doc block of every '
         'kernel`s main, against the banked prints (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the banked prints read: %s' % ', '.join('%s %d' % kv for kv in counts.items()), '',
         '### kernel | main | .lean files | claims']
    L += ['  %-34s %s %4d %5d' % (k, v['main'], v['files'], v['claims']) for k, v in per.items()]
    L += ['', '### EVERY CONTRADICTED CLAIM, IN FULL (the claim, the declaration, the print and its bank):']
    for r in rows:
        if r['verdict'] == 'CONTRADICTED':
            L += ['  %s %s:%d (%s, %s): %s' % (r['kernel'], r['file'], r['line'], r['block'], r['kind'], r['sentence'])]
            L += ['      %s (%s %s) prints %s -- %s' % (x['decl'], x['how'], x['matched'], x['print'], x['source']) for x in r['contradicted'][:12]]
            if len(r['contradicted']) > 12:
                L.append('      ... and %d more declarations' % (len(r['contradicted']) - 12))
    L += ['', '### EVERY UNVERIFIABLE CLAIM (no covered declaration has a banked print):']
    L += ['  %s %s:%d (%s, %s, covers %d): %s' % (r['kernel'], r['file'], r['line'], r['block'], r['kind'], r['covered'], r['sentence'][:200])
          for r in rows if r['verdict'] == 'UNVERIFIABLE']
    L += ['', '### EVERY VERIFIED CLAIM (printed of covered):']
    L += ['  %s %s:%d (%s, %s, %d of %d): %s' % (r['kernel'], r['file'], r['line'], r['block'], r['kind'], r['printed'], r['covered'], r['sentence'][:160])
          for r in rows if r['verdict'] == 'VERIFIED']
    L += ['', '### EVERY MENTION (an axiom word, no profile stated), not scored: %d' % c['MENTION']]
    L += ['  %s %s:%d (%s): %s' % (r['kernel'], r['file'], r['line'], r['block'], r['sentence'][:160]) for r in rows if r['verdict'] == 'MENTION']
    ok = c['CONTRADICTED'] == 0
    oos = [r for r in rows if r['verdict'] == 'OUT OF SCOPE']
    L += ['', '### `/-!` BLOCKS AFTER A FILE`S HEAD, OUT OF SCOPE (neither a docstring nor the module header): %d blocks, %d sentences with an '
              'axiom word' % (len(oos), sum(r['claims'] for r in oos))]
    L += ['  %s %s:%d (%d sentences)' % (r['kernel'], r['file'], r['line'], r['claims']) for r in oos]
    n = len(rows) - len(oos)
    L += ['', '### ### **CLAIMS %d ; CONTRADICTED %d ; UNVERIFIABLE %d ; VERIFIED %d ; MENTIONS %d ; VERDICT : %s**' % (
        n, c['CONTRADICTED'], c['UNVERIFIABLE'], c['VERIFIED'], c['MENTION'], 'PASS' if ok else 'FAIL')]
    return ok, L


def main(argv):
    bank = argv[argv.index('--bank') + 1] if '--bank' in argv else None
    names = [a for a in argv if not a.startswith('--') and a != bank] or NSM.kernels()
    idx, counts = index()
    rows, per = run(names, idx)
    ok, L = report(rows, per, counts)
    if bank:
        for p, b in ((bank, (NL.join(L) + NL).encode('utf-8')),
                     (os.path.splitext(bank)[0] + '.json', (json.dumps(dict(ok=ok, counts=counts, per=per, rows=rows), indent=1,
                                                                       ensure_ascii=False) + NL).encode('utf-8'))):
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
    print(L[2])
    print(L[-1])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
