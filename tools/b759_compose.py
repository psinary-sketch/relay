# -*- coding: utf-8 -*-
"""tools/b759_compose.py -- (R369)(8): THE DOCUMENT ENTERED, phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, A NEW FILE BESIDE v0.1,
WHICH IS NOT EDITED. Composed from: v0.1's title line; BLOCK A; v0.1's :21 to :218 (and its blank :219) with BLOCK B's seven replacements;
BLOCK C with (7)'s fields (data/b759_fields.json, tools/b759_fields.py), its marker lines removed, (6)'s outcome applied; no other text.

ITS CONTROLS, printed before the commit ((8)):
  (i)   each OLD of BLOCK B stands once in v0.1 at its line (PLACE-papers HEAD's blob); where one does not, the tool stops there, nothing composed
  (ii)  v0.1's sha256 equal before and after (the blob and the working copy), the ruling's opening figure read against them
  (iii) section 9.9's notes byte-equal to v0.1's :3 to :19
  (iv)  each path-and-line cite of a Lean name read at the pin (SIDE-explicit-formula; SIDE-dirichlet-mod-24 and Mathlib at the revisions the
        cite names), each relay and PLACE-papers cite read at HEAD; a Lean cite holds where each of its names stands on a cited line; a relay
        or PLACE-papers cite holds where each decimal figure of its clause that its file carries stands on a cited line; a missed line number
        corrected where the name (the figure) stands once in the named file, and listed where it does not; the misses printed, 0 wanted
        THE READER, repaired before its first run on the act's fields (relay data/b759_events.txt (37)): an implied cite naming a Lean name
        read against the last Lean file cited, and, where its names do not stand there, at each Lean file the document cited before; a Lean
        file named without lines sets that context; a bare file name several files carry read as the one cited before, else the one in the
        last Lean file's directory; a backticked span a name only where it is one identifier (a field's signature its name, after "the
        structure of" its type); a relay bank named without data/; a one-word alias of the last relay bank ("notes :3"); a plain decimal
        figure standing where a decimal of the line rounds to it; a figure correction decided by the figures standing once in the file
        HAND: the residue the reader cannot place, each read by hand and entered below with its verdict, BLOCK B's lines checked by the tool
  (v)   the banned stems 0 (tools/banned_terms.py --new over the composed file)
  (vi)  the brackets left, by name
PLACE-papers lines are printed by path, line and sha256 (16 hex) alone, never by their words.
THE WRITE: refused where (i) stops, where (ii), (iii) or (v) is not as wanted, or where a cite stands NOT READ with no hand verdict; a LISTED
miss does not refuse it ((8): "listed where it does not"), each printed with its reason and carried to the closing.

  control   the planted controls, printed
  dry       composed in memory and every control run (the stems over a temporary copy, removed after); nothing written
  write     the same, then the file written into PLACE-papers and data/b759_compose.txt banked; refused where the file stands already
"""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K       # noqa: E402  (PP, PP_NEW)
import b759_controls as C       # noqa: E402  (the kernels' folders)
import figbank as FB            # noqa: E402

NL = '\n'
ACT = 'b759'
TEXT = os.path.join(D, 'b759_text.txt')
FERRY = os.path.join(D, 'b759_ferry.txt')
FIELDS = os.path.join(D, 'b759_fields.json')
BANK = os.path.join(D, 'b759_compose.txt')
V01 = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
V02 = K.PP_NEW[0]
EFP = C.KERNELS['ef']['path']
M24P = C.KERNELS['m24']['path']
MATHLIB = os.path.join(EFP, '.lake', 'packages', 'mathlib')
LBR, RBR = '‹', '›'
PPDOCS = {'FINDINGS': 'FINDINGS.md', 'INSTRUMENTS': 'phase1.5/method/INSTRUMENTS.md', 'INSTRUMENTS.md': 'phase1.5/method/INSTRUMENTS.md',
          'ERRATA.md': 'ERRATA.md', 'REGISTRY': 'REGISTRY.md', 'REGISTRY.md': 'REGISTRY.md', 'FINDINGS.md': 'FINDINGS.md', 'Faces Ledger': 'FACES_LEDGER.md',
          '*The Findings As They Stand* v0.7': 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md'}
LS = r':\d+(?:\s*[-–]\s*:\d+)?(?:(?:,\s*|\s+and\s+):\d+(?:\s*[-–]\s*:\d+)?)*'
# ### the reader's repairs before its first run on the act's fields (events (37)): a relay bank named without data/ (b740_..._notes.txt), and
# ### FINDINGS.md and REGISTRY.md with their extension, read as the cites they are
TOK = re.compile(r'(?P<lean>(?<![\w/.])(?:[A-Za-z][\w]*/)*[A-Za-z][\w]*\.lean)|(?P<relay>(?<![\w/])(?:data/[\w.\-]+|b\d{3}_[\w.\-]+)\.(?:txt|json))|'
                 r'(?P<pp>\*The Findings As They Stand\* v0\.7|(?<![\w/])phase[\w./\-]+\.md|\bFINDINGS(?:\.md)?(?![\w])|\bINSTRUMENTS(?:\.md)?\b|\bERRATA\.md|'
                 r'\bREGISTRY(?:\.md)?(?![\w])|Faces Ledger)')
LSR = re.compile(r'(?<![\w:])' + LS)
DECL = r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|opaque|axiom)\s+(?:[\w.]*\.)?%s(?![\w])'


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def _lines(p):
    return io.open(p, encoding='utf-8').read().replace('\r', '').split(NL)


def sha16(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()[:16]


# ### ---------------------------------------------------------------- the parts of the composition
def block_b(text):
    """BLOCK B's seven: [(key, line, old, new)], read from the text block; a part not in its form is None."""
    out = []
    for i, l in enumerate(text):
        m = re.match(r'^@@ (B\d) \| :(\d+)$', l)
        if m:
            o, n = text[i + 1] if i + 1 < len(text) else '', text[i + 2] if i + 2 < len(text) else ''
            out.append((m.group(1), int(m.group(2)), o[5:] if o.startswith('OLD: ') else None, n[5:] if n.startswith('NEW: ') else None))
    return out


def apply_b(v1, B, fill):
    """each OLD read once at its line in v0.1 as it stands and in the line as the earlier replacements left it; [(key, line, in v0.1, now, ok)]."""
    lines, checks = list(v1), []
    for key, ln, old, new in B:
        if old is None or new is None or not 0 < ln <= len(v1):
            checks.append((key, ln, 0, 0, False))
            continue
        n0, n1 = v1[ln - 1].count(old), lines[ln - 1].count(old)
        ok = n0 == 1 and n1 == 1
        checks.append((key, ln, n0, n1, ok))
        if ok:
            lines[ln - 1] = lines[ln - 1].replace(old, fill(new), 1)
    return lines, checks


def fill_inline(s, F, ln):
    for k in ('DATE', 'LAWSUM', 'PIN', 'WEILNAME', 'F1', 'F2', 'MD5'):
        tag = LBR + k + RBR
        if tag in s and F.get(k) is not None:
            s = s.replace(tag, F[k])
    tag = LBR + 'AX' + RBR
    if tag in s and ln is not None and (F.get('AX') or {}).get(str(ln)) is not None:
        s = s.replace(tag, F['AX'][str(ln)])
    return s


def fill_whole(s, F):
    """a whole-line field: (lines to enter) or None where the line is not one; an empty field enters nothing; an unfilled one stays bracketed."""
    for k in ('WEILROW', 'LAWROW', 'V041', 'HISTORY'):
        if s.strip() == LBR + k + RBR:
            v = F.get(k)
            if v is None:
                return [s]
            if isinstance(v, list):
                return list(v)
            return [] if v == '' else [v]
    return None


def compose(text, v1b, v1, F):
    """[(line, origin)] for v0.2; origin ('text', n), ('v01', n) or None."""
    out = [(v1[0], ('v01', 1)), ('', None)]
    for n in (5, 6, 7):
        out.append((fill_inline(text[n - 1], F, n), ('text', n)))
    out.append(('', None))
    for n in range(21, 220):
        out.append((fill_inline(v1b[n - 1], F, None), ('v01', n)))
    c0 = [i for i, l in enumerate(text) if l.startswith('@@ BLOCK C')][0]
    c1 = [i for i, l in enumerate(text) if l.startswith('@@ BLOCK D')][0]
    alt = [i for i, l in enumerate(text) if l == '@@ ALT8 BEGIN'], [i for i, l in enumerate(text) if l == '@@ ALT8 END']
    law, mode = F.get('LAW'), None
    for i in range(c0 + 2, c1):
        l, n = text[i], i + 1
        if l.startswith('@@'):
            if l == '@@ LAW BEGIN':
                mode = 'law'
                if law == 'OBSERVED':
                    for j in range(alt[0][0] + 1, alt[1][0]):
                        out.append((fill_inline(text[j], F, j + 1), ('text', j + 1)))
            elif l == '@@ APPENDIX BEGIN':
                mode = 'app'
            elif l in ('@@ LAW END', '@@ APPENDIX END'):
                mode = None
            continue
        if (mode == 'law' and law == 'OBSERVED') or (mode == 'app' and law != 'THEOREM'):
            continue
        if law != 'THEOREM' and l.startswith('3. **The pattern table of Appendix A.**'):
            continue
        w = fill_whole(l, F)
        if w is not None:
            out += [(x, ('text', n) if x == l else ('field', n)) for x in w]
            continue
        out.append((fill_inline(l, F, n), ('text', n)))
    while out and not out[-1][0].strip():
        out.pop()
    return out


# ### ---------------------------------------------------------------- the cites
def expand(spec):
    ns = []
    for a, b in re.findall(r':(\d+)(?:\s*[-–]\s*:(\d+))?', spec):
        a = int(a)
        ns += list(range(a, min(int(b), a + 400) + 1)) if b else [a]
    return ns


def figures(clause):
    """the clause's decimal figures: [(label, regex)]: a x 10^b with a decimal mantissa, and plain decimals of three places or more."""
    out, spans = [], []
    for m in re.finditer(r'(\d+\.\d+)\s*×\s*10\^\(?([−-]?)(\d+)\)?', clause):
        neg = m.group(2) != ''
        pat = re.escape(m.group(1)) + r'\d*[eE]' + ('-' if neg else r'\+?') + '0*' + m.group(3) + r'(?!\d)'
        out.append((m.group(0), r'(?<![\d.])' + pat))
        spans.append(m.span())
    for m in re.finditer(r'(?<![\d.])(\d+\.\d{3,})(?![\d])', clause):
        if any(a <= m.start() < b for a, b in spans):
            continue
        out.append((m.group(1), ('dec', m.group(1))))
    return out


def _dec_on(fig, line):
    """a plain decimal figure stands on a line where a decimal of the line, rounded half-even to the figure's places, equals it (the banked
    figure a printed rounding of its generator: 0.798 for 0.79799715718)."""
    import decimal
    q = decimal.Decimal(fig)
    for x in re.findall(r'(?<![\d.])\d+\.\d+(?![\d])', line):
        d = decimal.Decimal(x)
        if len(x.split('.')[1]) >= len(fig.split('.')[1]) and d.quantize(q, rounding=decimal.ROUND_HALF_EVEN) == q:
            return True
    return False


def fig_on(pat, line):
    """a figure's pattern on a line: a plain decimal by its rounding (_dec_on), every other form by its regular expression."""
    return _dec_on(pat[1], line) if isinstance(pat, tuple) else bool(re.search(pat, line))


def figure_lines(src, pat):
    return [i + 1 for i, l in enumerate(src) if fig_on(pat, l)]


def respec(spec, ns):
    dash = '–' if '–' in spec else '-'
    ns = sorted(set(ns))
    return ':%d' % ns[0] if len(ns) == 1 else ':%d%s:%d' % (ns[0], dash, ns[-1])


def parse_line(s):
    """the cites of one line: [(kind, path or None, spec, start, end, spec_start, clause_start)], in order; a path named without lines enters as
    ('ctx', path) for REGISTRY and the Faces Ledger alone."""
    out, used = [], []
    for m in TOK.finditer(s):
        kind = m.lastgroup
        rest = s[m.end():]
        mm = re.match(r'`?\s*(?:,\s*)?(' + LS + r')', rest)
        if mm:
            st = m.end() + mm.start(1)
            out.append((kind, m.group(0), mm.group(1), m.start(), st + len(mm.group(1)), st))
            used.append((m.start(), st + len(mm.group(1))))
        elif kind == 'pp':
            out.append(('ctx', m.group(0), None, m.start(), m.end(), None))
        elif kind == 'lean':
            out.append(('lctx', m.group(0), None, m.start(), m.end(), None))   # ### a Lean file named without lines sets the Lean context (events (37))
    for m in LSR.finditer(s):
        if any(a <= m.start() < b for a, b in used):
            continue
        pre = s[:m.start()].rstrip()
        if pre.endswith('(') or pre.endswith(';') or pre.endswith(',') or re.search(r'\bused at$|\bat$|\bthe structure of$', pre) or pre.endswith('`'):
            out.append(('implied', None, m.group(0), m.start(), m.end(), m.start()))
            continue
        w = re.search(r'(?:\(|;\s|,\s)([a-z]+)$', pre)
        if w:
            out.append(('word', w.group(1), m.group(0), m.start(), m.end(), m.start()))   # ### a one-word alias, resolved in cites() against the last relay bank
            continue
        out.append(('unparsed', None, m.group(0), m.start(), m.end(), m.start()))
    return sorted(out, key=lambda x: x[3])


def lean_names(s, start):
    """the Lean names a cite at start names: backticked names in its parenthetical part (from the last '(' or ';' before it), else the
    backticked name standing just before that parenthesis."""
    struct = s[:start].rstrip().endswith('the structure of')
    op = max(s.rfind('(', 0, start), s.rfind(';', 0, start))
    part = s[op + 1:start] if op >= 0 else s[:start]

    def ident(x):
        """the name a backticked span carries: the span where it is one identifier; a field's signature `name : type` its name, or after
        "the structure of" its type's head; a list, an axioms line or an expression none (events (37))."""
        if x.endswith('.lean') or re.match(r'^[0-9a-f]{7,40}$', x):
            return None
        sig = re.match(r'^([^\s:\[\]()`]+)\s+:\s+([^\s\[\]()]+)', x)
        if sig:
            return sig.group(2) if struct else sig.group(1)
        return x if re.match(r'^[^\s\[\]()]+$', x) else None
    nm = [y for y in (ident(x) for x in re.findall(r'`([^`]+)`', part)) if y]
    if nm:
        return nm
    if struct:
        sp = re.findall(r'`([^`]+)`', s[:start])
        y = ident(sp[-1]) if sp else None
        return [y] if y else []
    if op >= 0 and s[op] == '(':
        mm = re.search(r'`([^`]+)`\s*$', s[:op])
        y = ident(mm.group(1)) if mm else None
        if y:
            return [y]
    return []


def name_on(seg, line):
    return re.search(r'(?<![\w])' + re.escape(seg) + r'(?![\w])', line) is not None


class Tree(object):
    def __init__(self, repo, rev):
        self.repo, self.rev = repo, rev
        self.files = [f for f in git(repo, 'ls-tree', '-r', '--name-only', rev).split(NL) if f.endswith('.lean')]
        self.cache = {}

    def resolve(self, p):
        p = p[len('SIDEExplicitFormula/'):] if p.startswith('SIDEExplicitFormula/') and self.repo == EFP else p
        return [f for f in self.files if f == p or f.endswith('/' + p)]

    def src(self, f):
        if f not in self.cache:
            self.cache[f] = git(self.repo, 'show', '%s:%s' % (self.rev, f)).replace('\r', '').split(NL)
        return self.cache[f]


def lean_check(tree, cands, names, ns, ctx_full, seen=()):
    """(verdict, the file, corrected lines or None, why): HOLDS, CORRECTED, LISTED or LINES EXIST. A bare file name several files carry: the one
    holding the names, else the context's, else one the document cited before by its full place (most recent first), else the one in the
    directory of the last Lean file cited (events (37)); otherwise LISTED."""
    if not cands:
        return 'LISTED', None, None, 'no such file at %s' % tree.rev[:8]
    segs = [n.split('.')[-1] for n in names]

    def holds(f):
        src = tree.src(f)
        return all(any(0 < k <= len(src) and name_on(sg, src[k - 1]) for k in ns) for sg in segs)
    how = ''
    if len(cands) > 1:
        h = [f for f in cands if segs and holds(f)]
        f = h[0] if len(h) == 1 else (ctx_full if ctx_full in cands else None)
        if f is None:
            f = next((x for x in seen if x in cands), None)
            how = ' (a bare name of %d files read as %s, cited before)' % (len(cands), f) if f else ''
        if f is None and seen:
            dd = [x for x in cands if os.path.dirname(x) == os.path.dirname(seen[0])]
            f = dd[0] if len(dd) == 1 else None
            how = ' (a bare name of %d files read as %s, in the directory of the last Lean file cited)' % (len(cands), f) if f else ''
        if f is None:
            return 'LISTED', None, None, 'the file names %d files: %s' % (len(cands), ', '.join(cands))
    else:
        f = cands[0]
    if how:
        v, f2, new, why = lean_check(tree, [f], names, ns, None)
        return v, f2, new, (why + how).strip()
    src = tree.src(f)
    if not segs:
        return ('LINES EXIST' if ns and max(ns) <= len(src) else 'LISTED'), f, None, 'no name in the cite; %d lines' % len(src)
    if holds(f):
        return 'HOLDS', f, None, ''
    if len(segs) == 1 and len(ns) == 1:
        d = [i + 1 for i, l in enumerate(src) if re.search(DECL % re.escape(segs[0]), l)]
        if len(d) == 1:
            return 'CORRECTED', f, d, 'the name declared once, at :%d' % d[0]
        return 'LISTED', f, None, 'the name declared %d times in the file' % len(d)
    return 'LISTED', f, None, 'not every name on the cited lines, the cite not one line and one name'


def fig_check(src, clause, ns):
    figs = [(lab, figure_lines(src, pat)) for lab, pat in figures(clause)]
    counted = [(lab, fl) for lab, fl in figs if fl]
    if not ns or max(ns) > len(src):
        return 'LISTED', None, 'the lines beyond the file`s %d' % len(src), figs
    if not counted:
        return 'LINES EXIST', None, 'no figure of the clause in the file', figs
    if all(any(k in ns for k in fl) for _lab, fl in counted):
        return 'HOLDS', None, '', figs
    if all(len(fl) == 1 for _lab, fl in counted):
        return 'CORRECTED', [fl[0] for _lab, fl in counted], 'each figure stands once in the file', figs
    # ### the figures standing once in the file decide the lines where those lines lie within ten of each other; a figure standing at more
    # ### lines does not decide and is printed with its lines (events (37))
    once = sorted(set(fl[0] for _lab, fl in counted if len(fl) == 1))
    many = [(lab, fl) for lab, fl in counted if len(fl) > 1]
    if once and once[-1] - once[0] <= 10:
        return 'CORRECTED', once, 'the figures standing once in the file stand at %s; %s at more lines (%s), not deciding' % (
            respec(':0', once), ', '.join(lab for lab, _fl in many), '; '.join(', '.join(':%d' % k for k in fl[:6]) for _lab, fl in many)), figs
    return 'LISTED', None, 'a figure off the cited lines stands more than once in the file, the figures standing once not deciding (%s)' % '; '.join(
        '%s at %s' % (lab, ', '.join(':%d' % k for k in fl[:6])) for lab, fl in counted), figs


def cites(lines, pin_rev, v038):
    """every cite of the composed lines read; returns (rows, corrections {(line index): [(spec_start, spec_end, new)]})."""
    ef_pin, ef_38 = Tree(EFP, pin_rev), Tree(EFP, v038)
    m24 = {}
    ml = Tree(MATHLIB, 'de5ce8a9') if os.path.isdir(MATHLIB) else None
    rows, corr = [], {}
    ctx = None              # ### the last path cited with lines: (kind, path, full file or None)
    ctx_lean = None         # ### the last Lean file cited with lines
    ctx_relay = None        # ### the last relay bank cited with lines
    seen = []               # ### the Lean files the document cites, resolved, most recent first
    sec6 = [i for i, (l, _o) in enumerate(lines) if l.startswith('## 6. ')]
    sec6 = sec6[0] if sec6 else len(lines)
    tbl = [i for i, (l, _o) in enumerate(lines) if l.startswith('| § | What it says | Lean statement |')]
    for i, (s, _o) in enumerate(lines):
        if tbl and i > tbl[0] + 1 and s.startswith('| ') and i < tbl[0] + 60 and '.lean' in s:
            cells = [x.strip() for x in s.strip().strip('|').split('|')]
            names = [x for x in re.findall(r'`([^`]+)`', cells[2])]
            pm = re.search(r'((?:[A-Za-z]\w*/)*[A-Za-z]\w*\.lean)\s*(' + LS + ')', cells[3])
            if not pm:
                continue
            if 'SIDE-dirichlet-mod-24' in cells[3]:
                rv = re.findall(r'`([0-9a-f]{8})`', cells[3])
                tr = m24.setdefault(rv[0], Tree(M24P, rv[0])) if rv else None
            else:
                tr = ef_pin
            ns = expand(pm.group(2))
            pairs = list(zip(names, ns)) if len(names) == len(ns) and len(ns) > 1 else [(None, None)]
            base = s.index(cells[3]) + pm.start(2)
            for nm, k in pairs:
                v, f, new, why = lean_check(tr, tr.resolve(pm.group(1)) if tr else [], [nm] if nm else names, [k] if k else ns, None)
                sp = pm.group(2) if not k else ':%d' % k
                if v == 'CORRECTED' and new:
                    mo = re.search(re.escape(sp) + r'(?!\d)', pm.group(2))
                    if mo:
                        corr.setdefault(i, []).append((base + mo.start(), base + mo.end(), ':%d' % new[0]))
                        why = '%s -> :%d' % (why, new[0])
                rows.append(('lean', i + 1, f or pm.group(1), tr.rev[:8] if tr else '?', sp, nm and [nm] or names, v, why, None))
            continue
        for kind, path, spec, a, b, sst in parse_line(s):
            if kind == 'ctx':
                ctx = ('pp', PPDOCS.get(path, path), None)
                continue
            if kind == 'lctx':
                cl = ef_pin.resolve(path)
                fl = cl[0] if len(cl) == 1 else next((x for x in seen if x in cl), None)
                if fl is None and seen:
                    dd = [x for x in cl if os.path.dirname(x) == os.path.dirname(seen[0])]
                    fl = dd[0] if len(dd) == 1 else None
                if fl:
                    ctx = ctx_lean = ('lean', fl, fl)
                    seen = [fl] + [x for x in seen if x != fl]
                continue
            if kind == 'word':
                # ### a one-word alias of the last relay bank cited ("notes :3" after data/b742_offlinezero_notes.txt), else read by hand
                if ctx_relay and os.path.basename(ctx_relay[1]).rsplit('.', 1)[0].endswith('_' + path):
                    kind = 'implied'
                    ctx = ctx_relay
                else:
                    rows.append(('unparsed', i + 1, None, '-', spec, [], 'NOT READ', 'the word %r before it no alias of the last relay bank: read by hand' % path, None))
                    continue
            if kind == 'unparsed':
                rows.append(('unparsed', i + 1, None, '-', spec, [], 'NOT READ', 'no path before it in a cite`s form: read by hand', None))
                continue
            ns = expand(spec)
            implied = kind == 'implied'
            if implied:
                # ### an implied cite naming a Lean name takes the last Lean file cited; one naming none, the last path cited (events (37))
                use = ctx_lean if (lean_names(s, a) and ctx_lean) else ctx
                if use is None:
                    rows.append(('implied', i + 1, None, '-', spec, [], 'LISTED', 'no path cited before it', None))
                    continue
                kind, path, full = use
            else:
                full = None
            if kind == 'lean':
                if path.startswith('Mathlib/'):
                    tr = ml
                else:
                    tr = ef_pin
                names = lean_names(s, a)
                cands = tr.resolve(path) if tr else []
                prev = ctx_lean[2] if ctx_lean else None
                v, f, new, why = lean_check(tr, cands, names, ns, full or prev, seen) if tr else ('LISTED', None, None, 'no tree', )
                if implied and names and v != 'HOLDS' and tr is not None:
                    # ### the implied cite's names read at each Lean file the document cites before, most recent first: the first holding
                    # ### them on the cited lines is the file the text means; printed as such (events (37))
                    for alt in seen:
                        if alt != f and lean_check(tr, [alt], names, ns, None)[0] == 'HOLDS':
                            why = 'implied: the last Lean file cited (%s) not holding the names; read at %s, cited before' % (f, alt)
                            v, f, new = 'HOLDS', alt, None
                            path = alt
                            break
                at38 = None
                if tr is ef_pin and i < sec6 and f:
                    v38 = lean_check(ef_38, ef_38.resolve(f), names, ns, f)
                    at38 = v38[0]
                rows.append(('lean', i + 1, f or path, tr.rev[:8] if tr else '?', spec, names, v, why, at38))
                ctx = ('lean', path, f)
                ctx_lean = ctx
                if f and tr is ef_pin:
                    seen = [f] + [x for x in seen if x != f]
            else:
                if kind == 'relay':
                    rel = path if path.startswith('data/') else 'data/' + path   # ### a relay bank named without data/ (events (37))
                else:
                    rel = PPDOCS.get(path, path)
                if kind == 'relay':
                    p = os.path.join(RELAY, *rel.split('/'))
                    src = io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '').split(NL) if os.path.exists(p) else None
                else:
                    src = git(K.PP, 'show', 'HEAD:%s' % rel).replace('\r', '').split(NL)
                    src = src if len(src) > 1 else None
                prev_end = max([x[4] for x in parse_line(s) if x[4] <= a] or [0])
                clause = s[prev_end:a]
                if src is None:
                    v, new, why, figs = 'LISTED', None, 'the file not read at HEAD', []
                else:
                    v, new, why, figs = fig_check(src, clause, ns)
                digs = [sha16(src[k - 1]) for k in ns if src and 0 < k <= len(src)][:4] if kind == 'pp' else None
                rows.append((kind, i + 1, rel, 'HEAD', spec, [f for f, _l in figs], v, why, digs))
                ctx = (kind, rel, None)
                if kind == 'relay':
                    ctx_relay = ctx
            if v == 'CORRECTED' and new:
                corr.setdefault(i, []).append((sst, sst + len(spec), respec(spec, new)))
                r = rows[-1]
                rows[-1] = r[:7] + ('%s -> %s' % (r[7], respec(spec, new)),) + r[8:]
    return rows, corr


HAND = {
    (('v01', 58), ':31'): ('LISTED', 'v0.1`s own line :31, the forms Q1 and Q1⁻¹, which stands at v0.2 :17, v0.1 :21-:218 entering v0.2 fourteen '
                           'lines higher: a cite into the document itself, its number left as v0.1 wrote it, the sentence not among BLOCK B`s seven and '
                           '(8) composing v0.1 :21-:218 unchanged but for them', None),
    (('text', 293), ':27, :33, :58, :73, :119'): ('HOLDS', 'v0.1`s lines, BLOCK B`s keys at them', 'blockb'),
    (('text', 293), ':214'): ('HOLDS', 'v0.1`s line, BLOCK B`s key at it', 'blockb'),
}


def hand(rows, lines, ch):
    """each NOT READ row with a hand verdict in HAND (keyed by the line's origin and the spec) given it; BLOCK B's lines checked against the
    keys' lines (ch); a row with none stays NOT READ and refuses the write."""
    bl = set(ln for _k, ln, _a, _b, _ok in ch)
    out = []
    for r in rows:
        if r[6] == 'NOT READ':
            h = HAND.get((lines[r[1] - 1][1], r[4]))
            if h:
                v, why, chk = h
                if chk == 'blockb':
                    v = 'HOLDS' if set(expand(r[4])) <= bl else 'LISTED'
                r = ('hand', r[1], 'v0.1' if chk == 'blockb' or r[4] == ':31' else None, '-', r[4], [], v, 'read by hand: ' + why, None)
        out.append(r)
    return out


def apply_corr(lines, corr):
    out = list(lines)
    for i, cs in corr.items():
        s = out[i][0]
        for a, b, new in sorted(cs, reverse=True):
            s = s[:a] + new + s[b:]
        out[i] = (s, out[i][1])
    return out


def pp_kinds(kind):
    return kind


# ### ---------------------------------------------------------------- the controls
def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    v1 = ['t', 'a b c', 'x y x']
    lines, ch = apply_b(v1, [('B1', 2, 'b', 'B'), ('B2', 3, 'x', 'X'), ('B3', 2, 'q', 'Q')], lambda x: x)
    c('BLOCK B: an OLD once at its line replaced; twice refused; absent refused', ([x[4] for x in ch], lines[1]),
      [x[4] for x in ch] == [True, False, False] and lines[1] == 'a B c' and lines[2] == 'x y x')
    pats = dict(figures('is 1.2972 × 10^11 and 6.2 × 10^(−4) at γ = 16.2902, 6 × 10^(−13)'))
    dec = dict(figures('is 0.798'))['0.798']
    c('the figures: a x 10^b against e-notation, a negative exponent, a decimal prefix; an integer mantissa not taken; a plain decimal by '
      'its rounding (0.798 on 0.79799715718, not on 0.799)', sorted(pats), fig_on(pats['1.2972 × 10^11'], '= 1.2972e+11 ;')
      and fig_on(pats['6.2 × 10^(−4)'], 'is 6.2e-04 relative') and fig_on(pats['16.2902'], 'gamma 16.29021572')
      and not fig_on(pats['16.2902'], '116.2902') and len(pats) == 3 and fig_on(dec, 'at 0.79799715718.') and not fig_on(dec, 'at 0.799'))
    s = 'the form `q` (Schema/X.lean :3-:5), its `r` (:7); the bank (relay data/b1.txt :2–:4; FINDINGS :10), and REGISTRY rows (:8)'
    got = [(k, p, sp) for k, p, sp, _a, _b, _s in parse_line(s)]
    c('the cites of a planted line: a Lean path, an implied line, a relay bank, a ledger, a ledger named without lines', got,
      got == [('lean', 'Schema/X.lean', ':3-:5'), ('implied', None, ':7'), ('relay', 'data/b1.txt', ':2–:4'), ('pp', 'FINDINGS', ':10'),
              ('ctx', 'REGISTRY', None), ('implied', None, ':8')])
    c('the names of a cite: inside its part, and just before its parenthesis', (lean_names(s, s.find(':3-')), lean_names(s, s.find(':7'))),
      lean_names(s, s.find(':3-')) == ['q'] and lean_names(s, s.find(':7')) == ['r'])

    class P(Tree):
        def __init__(self):
            self.rev, self.files, self.cache, self.repo = 'planted0', ['A/X.lean', 'B/X.lean'], {
                'A/X.lean': ['', 'theorem foo : True := by', '', 'theorem bar : True := by'], 'B/X.lean': ['theorem foo : True']}, 'x'
    tp = P()
    r = [lean_check(tp, ['A/X.lean'], ['foo'], [2], None)[0], lean_check(tp, ['A/X.lean'], ['Ns.bar'], [2], None)[:3],
         lean_check(tp, ['A/X.lean', 'B/X.lean'], ['foo'], [1], None)[:2], lean_check(tp, ['A/X.lean'], ['baz'], [2], None)[0]]
    c('a Lean cite: holds; a missed line corrected where the name is declared once; two files resolved by the line; an absent name listed', r,
      r == ['HOLDS', ('CORRECTED', 'A/X.lean', [4]), ('HOLDS', 'B/X.lean'), 'LISTED'])
    src = ['a', 'g = 14.13 : 4.3908e+09', 'g = 16.29 : 1.2972e+11', 'x 6.2e-04', 'y 6.2e-04']
    fr = [fig_check(src, 'is 1.2972 × 10^11', [2])[:2], fig_check(src, 'is 1.2972 × 10^11', [3])[0],
          fig_check(src, 'was 6.2 × 10^(−4)', [1])[0], fig_check(src, 'no figure', [2])[0], fig_check(src, 'x', [9])[0]]
    c('a relay cite: a figure off its line corrected where it stands once; on its line holds; twice listed; none; beyond the end', fr,
      fr == [('CORRECTED', [3]), 'HOLDS', 'LISTED', 'LINES EXIST', 'LISTED'])
    c('a corrected line in the cite`s own dash', (respec(':134', [135]), respec(':137–:138', [139]), respec(':1-:2', [3, 5])),
      (respec(':134', [135]), respec(':137–:138', [139]), respec(':1-:2', [3, 5])) == (':135', ':139', ':3-:5'))
    F = {'WEILROW': '', 'V041': None, 'HISTORY': ['*a*', '', '*b*'], 'PIN': 'the tag v9 (x)', 'AX': {'4': 'std, run 1'}}
    c('the fields: an empty row enters nothing, an unfilled one stays bracketed, a list enters its lines; inline and by line',
      (fill_whole(LBR + 'WEILROW' + RBR, F), fill_whole(LBR + 'V041' + RBR, F), fill_whole(LBR + 'HISTORY' + RBR, F),
       fill_inline('at %sPIN%s | %sAX%s' % (LBR, RBR, LBR, RBR), F, 4)),
      fill_whole(LBR + 'WEILROW' + RBR, F) == [] and fill_whole(LBR + 'V041' + RBR, F) == [LBR + 'V041' + RBR]
      and fill_whole(LBR + 'HISTORY' + RBR, F) == ['*a*', '', '*b*'] and fill_inline('at %sPIN%s | %sAX%s' % (LBR, RBR, LBR, RBR), F, 4) == 'at the tag v9 (x) | std, run 1')
    # ### (9) the reader's repairs (events (37)), each on a planted line
    s2 = 'read (b742_x_notes.txt :3; REGISTRY.md :5; notes :9); `c : ZQC` the structure of :80; `foo` :12; Tail.lean (`baz`, :160)'
    g2 = [(k, p, sp) for k, p, sp, _a, _b, _s in parse_line(s2)]
    s3, s4 = 'the sum `a + b` (:7)', 'the field `zeros : Set ℂ` (:9)'
    nm = (lean_names(s2, s2.find(':80')), lean_names(s2, s2.find(':12')), lean_names(s2, s2.find(':160')), lean_names(s3, s3.find(':7')),
          lean_names(s4, s4.find(':9')))
    bare = (lean_check(tp, ['A/X.lean', 'B/X.lean'], [], [1], None, ['A/X.lean'])[:2], lean_check(tp, ['A/X.lean', 'B/X.lean'], [], [1], None, ['B/Y.lean'])[:2],
            lean_check(tp, ['A/X.lean', 'B/X.lean'], [], [1], None)[0])
    src2 = ['a', 'g 14.1347 : 4.3908e+09', 'b', 'g 14.1347 h 6.6263e+04', 'x']
    f2 = fig_check(src2, 'is 6.6263 × 10^4 at 14.1347', [1])[:2]
    c('the reader`s repairs: a relay bank without data/, REGISTRY.md, a one-word alias, "the structure of :N", "`name` :N", a Lean file named '
      'without lines; a signature`s type after "the structure of", a name before ":N", an expression none, a field`s name; a bare file name '
      'read as the one cited before and as the one in the last Lean file`s directory, else listed; the figures standing once deciding',
      (g2, nm, bare, f2),
      g2 == [('relay', 'b742_x_notes.txt', ':3'), ('pp', 'REGISTRY.md', ':5'), ('word', 'notes', ':9'), ('implied', None, ':80'),
             ('implied', None, ':12'), ('lctx', 'Tail.lean', None), ('implied', None, ':160')]
      and nm == (['ZQC'], ['foo'], ['baz'], [], ['zeros'])
      and bare == (('LINES EXIST', 'A/X.lean'), ('LINES EXIST', 'B/X.lean'), 'LISTED') and f2 == ('CORRECTED', [4]))
    return L, ok


# ### ---------------------------------------------------------------- the run
def run(write):
    L, ok = controls()
    out = ['%s -- (R369)(8): THE DOCUMENT ENTERED AT v0.2, ITS COMPOSITION AND ITS CONTROLS (%s, tools/b759_compose.py %s)' % (
        ACT, _now(), 'write' if write else 'dry'), '', '## THE PLANTED CONTROLS'] + L + ['  controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    if not all(ok):
        print(NL.join(out))
        sys.exit('### THE PLANTED CONTROLS NOT AS WANTED -- nothing composed')
    ferry = _lines(FERRY)
    c8 = [l for l in ferry if l.startswith('(8) ')][0]
    v01sha = re.findall(r'v0\.1\'s sha256 equal before and after, opening ([0-9a-f]{16})', c8)
    v038 = re.findall(r'v0\.38 to ([0-9a-f]{8})', ferry[2])
    sent = re.findall(r'THE SENTENCE: "([^"]+)"', c8)
    if not os.path.exists(FIELDS):
        sys.exit('### data/b759_fields.json ABSENT -- nothing composed')
    F = json.load(io.open(FIELDS, encoding='utf-8'))
    if F.get('F1_SENTENCE') != 'STANDS':
        sys.exit('### F1`S SENTENCE READS %r: ITS CUT FORM IS NOT COMPOSED BY THIS TOOL -- nothing composed' % F.get('F1_SENTENCE'))
    text = _lines(TEXT)
    hb0 = git(K.PP, 'show', 'HEAD:%s' % V01, raw=True)
    wb0 = io.open(os.path.join(K.PP, *V01.split('/')), 'rb').read()
    v1 = hb0.decode('utf-8').split(NL)
    out.append('## (i) BLOCK B AGAINST v0.1 (PLACE-papers HEAD`s blob, %d lines, sha256 %s)' % (len(v1), sha16(hb0)))
    B = block_b(text)
    v1b, ch = apply_b(v1, B, lambda x: fill_inline(x, F, None))
    for key, ln, n0, n1, okb in ch:
        out.append('  %s at v0.1 :%d: its OLD %d time(s) in v0.1`s line, %d in the line as composed -> %s' % (key, ln, n0, n1, 'STANDS ONCE' if okb else 'STOP'))
    if len(B) != 7 or not all(x[4] for x in ch):
        print(NL.join(out))
        sys.exit('### AN OLD OF BLOCK B DOES NOT STAND ONCE AT ITS LINE (or BLOCK B not seven) -- the act stops here, nothing composed')
    lines = compose(text, v1b, v1, F)
    pin_rev = re.findall(r'\(([0-9a-f]{8})\)', F['PIN'])
    rows, corr = cites(lines, pin_rev[0], v038[0])
    rows = hand(rows, lines, ch)
    lines = apply_corr(lines, corr)
    body = [l for l, _o in lines]
    doc = (NL.join(body) + NL).encode('utf-8')
    out += ['', '## THE COMPOSITION', '  v0.2: %d lines, %d bytes, sha256 %s ; v0.1`s title line, BLOCK A, v0.1 :21-:219 with BLOCK B`s seven, BLOCK C with the fields; '
            'the law %s, the appendix %s' % (len(body), len(doc), sha16(doc), F.get('LAW'), 'ENTERED' if F.get('LAW') == 'THEOREM' else 'NOT ENTERED')]
    # ### (iv) the cites
    out += ['', '## (iv) THE CITES (Lean at the pin %s, and §1-§5`s also at v0.38 %s; relay and PLACE-papers at HEAD; PLACE-papers lines by sha256 alone)' % (
        pin_rev[0], v038[0])]
    tally = {}
    for kind, ln, path, rev, spec, what, v, why, extra in rows:
        tally[(kind, v)] = tally.get((kind, v), 0) + 1
        x = ''
        if kind == 'lean' and extra:
            x = ' ; at v0.38 %s' % extra
        if kind == 'pp' and extra:
            x = ' ; the lines` sha256 %s' % ', '.join(extra)
        out.append('  v0.2 :%d %s %s %s at %s [%s] -> %s%s%s' % (ln, kind, path, spec, rev, ', '.join(what)[:120], v, (' (%s)' % why) if why else '', x))
    listed = [r for r in rows if r[6] == 'LISTED']
    corrected = [r for r in rows if r[6] == 'CORRECTED']
    out.append('  THE CITES READ %d ; %s ; CORRECTED %d ; LISTED (THE MISSES) %d, 0 WANTED' % (
        len(rows), ' ; '.join('%s %s %d' % (k, v, n) for (k, v), n in sorted(tally.items())), len(corrected), len(listed)))
    # ### (iii) 9.9's notes
    hi = [i for i, l in enumerate(body) if l.startswith('v0.2 (') and 'The dated notes of v0.1 follow, as written.' in l]
    notes = body[hi[0] + 2:hi[0] + 19] if len(hi) == 1 else []
    eq99 = notes == v1[2:19]
    out += ['', '## (iii) SECTION 9.9`S NOTES AGAINST v0.1 :3-:19: %s (%d lines, sha256 %s against %s)' % (
        'BYTE-EQUAL' if eq99 else 'NOT EQUAL', len(notes), sha16(NL.join(notes)), sha16(NL.join(v1[2:19])))]
    # ### (vi) the brackets left
    left = sorted(set(re.findall(LBR + r'([^' + RBR + r']+)' + RBR, NL.join(body))))
    out.append('## (vi) THE BRACKETS LEFT: %d%s' % (len(left), (' -- ' + ', '.join(left)) if left else ''))
    # ### (v) the banned stems, over a temporary copy
    tmp = tempfile.mkdtemp(prefix='b759compose')
    try:
        tp = os.path.join(tmp, 'THE_EPSTEIN_CONTROL_OBJECT_v0_2.md')
        with open(tp, 'wb') as fh:
            fh.write(doc)
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'banned_terms.py'), '--new', tp], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', cwd=RELAY)
        vl = [l for l in (r.stdout or '').split(NL) if 'VERDICT' in l]
        live = re.findall(r'live uses\s*:\s*(\d+)', (r.stdout or ''))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    out.append('## (v) THE BANNED STEMS (tools/banned_terms.py --new over a temporary copy, exit %d): live uses %s ; %s' % (
        r.returncode, live[0] if live else '?', (vl or ['### NO VERDICT LINE'])[0].strip()[:200]))
    stems_ok = r.returncode == 0 and bool(vl) and live == ['0']
    # ### (ii) v0.1 after
    hb1 = git(K.PP, 'show', 'HEAD:%s' % V01, raw=True)
    wb1 = io.open(os.path.join(K.PP, *V01.split('/')), 'rb').read()
    eqv1 = hb0 == hb1 and wb0 == wb1
    out += ['## (ii) v0.1`S sha256: the blob %s before, %s after ; the working copy %s before, %s after ; EQUAL %s ; the ruling`s opening %s matches %s' % (
        sha16(hb0), sha16(hb1), sha16(wb0), sha16(wb1), eqv1, v01sha[0] if v01sha else '?',
        'the blob' if v01sha and sha16(hb0) == v01sha[0] else 'the working copy' if v01sha and sha16(wb0) == v01sha[0] else 'NEITHER')]
    unread = [r for r in rows if r[6] == 'NOT READ']
    good = eqv1 and eq99 and stems_ok and not unread and bool(v01sha) and v01sha[0] in (sha16(hb0), sha16(wb0))
    f_left = len(left)
    s = (sent[0] if sent else '').replace('<pin>', F['PIN']).replace('<Appendix A | no appendix>', 'Appendix A' if F.get('LAW') == 'THEOREM' else 'no appendix').replace('<f>', str(f_left))
    out += ['', '## THE SENTENCE OF (8), ITS FIELDS FILLED', '  %s' % s, '',
            '### ### **v0.2 %s: %d LINES ; BLOCK B %d OF 7 ; CITES %d, CORRECTED %d, LISTED %d ; 9.9 %s ; BRACKETS LEFT %d ; THE STEMS %s ; v0.1 %s ; CONTROLS %d OF %d.**' % (
                'COMPOSED' if good else 'COMPOSED, A CONTROL NOT AS WANTED', len(body), sum(1 for x in ch if x[4]), len(rows), len(corrected), len(listed),
                'BYTE-EQUAL' if eq99 else 'NOT EQUAL', f_left, 'CLEAN' if stems_ok else 'NOT CLEAN', 'UNCHANGED' if eqv1 else 'CHANGED', sum(ok), len(ok))]
    print(NL.join(out))
    if not write:
        return
    if not good:
        sys.exit('### A CONTROL NOT AS WANTED -- nothing written')
    dst = os.path.join(K.PP, *V02.split('/'))
    if os.path.exists(dst):
        sys.exit('### %s STANDS ALREADY -- nothing written' % V02)
    with open(dst, 'wb') as fh:
        fh.write(doc)
    back = io.open(dst, 'rb').read()
    out.append('written PLACE-papers %s: %d bytes, sha256 %s, read back %s' % (V02, len(back), sha16(back), 'EQUAL' if back == doc else 'NOT EQUAL'))
    rr = FB.write(BANK, NL.join(out))
    print(out[-1])
    print('written data/b759_compose.txt ; figbank: %s' % rr['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['dry']:
        run(False)
    elif a[:1] == ['write']:
        run(True)
    else:
        sys.exit(__doc__)
