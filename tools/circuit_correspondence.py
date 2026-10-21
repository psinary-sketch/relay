# -*- coding: utf-8 -*-
"""circuit_correspondence.py -- CORRESPONDENCE-DOMINANCE, the eleventh reading of the circuit specification (relay data/b695_circuit_spec.txt
:53-:64), built at b698 under (R308)(3) and the author's two answers on the citation misses (data/b698_author_answers.txt).

### reads: the faces page's Correspondence row naming a faces kernel (the node list's @corr record, by line, and the row's line in the page);
### the kernel's compiled face as a statement; the clause h2_sign as a statement; both reduced to binders and a conclusion.
### compares: by statement identity after the two kernels' own namespaces are stripped and the binders aligned by position -- each binder's
### kind (explicit, implicit, instance, or an unnamed hypothesis) and its type, with every bound name replaced by its position (#1, #2, ...)
### in the types after it and in the conclusion, so that two statements differing in bound names alone read alike; whitespace runs collapsed.
### verdict: HOLDS-BY-CORRESPONDENCE where every binder and the conclusion AGREE; DIFFERS with the first differing binder named otherwise.
### The sources, as the author's answers order them: h2_sign's #print from the faces page's generator input (relay data/b643_probe_out_zeta.txt,
### SIDE-explicit-formula v0.26 = 82550e4), with each file defining a name that print carries shown byte-identical from v0.26 to v0.34, and the
### toolchain and the Mathlib manifest beside; SIDE-lv-conservation's face by a hosted print at v0.13.0 where the workflow at that tag can print
### it, else its SOURCE TEXT at v0.13.0 (git show) and the verdict qualified "source against print".
### Controls first: h2_sign against itself (HOLDS at every binder); a planted statement, h2_sign with one binder's type changed (DIFFERS at
### that binder). Then the real reading.
### Writes only data/b698_correspondence_dominance.txt (.json). `python -X utf8 tools/circuit_correspondence.py [dry]`.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EF, LV = 'D:/SIDE-explicit-formula', 'D:/SIDE-lv-conservation'
EF_PRINT_PIN, EF_TAG, LV_TAG = 'v0.26', 'v0.34', 'v0.13.0'
PROBE = 'b643_probe_out_zeta.txt'
NODES = 'b690_nodes_zeta.txt'
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
CLAUSE = 'SIDEExplicitFormula.B321.h2_sign'
LV_FILE, LV_NAME = 'SIDELvConservation/ZeroActingPartial.lean', 'residue_irreducible'
STRIP = {'SIDE-explicit-formula': ('SIDEExplicitFormula.B321.', 'SIDEExplicitFormula.', 'Zeta23.'),
         'SIDE-lv-conservation': ('SIDELvConservation.RegisterPentagon.', 'SIDELvConservation.')}
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


# ================================================================================ THE STATEMENT, AS BINDERS AND A CONCLUSION
OPEN, CLOSE = '({[⦃', ')}]⦄'
KIND = {'(': 'explicit', '{': 'implicit', '[': 'instance', '⦃': 'strict-implicit'}


def _top_split(s, sep):
    """split s at each top-level occurrence of sep (outside any bracket)."""
    out, depth, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c in OPEN:
            depth += 1
        elif c in CLOSE:
            depth -= 1
        if depth == 0 and s.startswith(sep, i):
            out.append(cur)
            cur, i = '', i + len(sep)
            continue
        cur += c
        i += 1
    out.append(cur)
    return out


def _groups(s):
    """the leading bracket groups of s: [(open, inner)], and the rest."""
    s, out = s.strip(), []
    while s and s[0] in OPEN:
        depth = 0
        for j, c in enumerate(s):
            if c in OPEN:
                depth += 1
            elif c in CLOSE:
                depth -= 1
                if depth == 0:
                    out.append((s[0], s[1:j].strip()))
                    s = s[j + 1:].strip()
                    break
        else:
            raise ValueError('an unclosed bracket in %r' % s[:80])
    return out, s


def _expand(groups):
    """binder groups to binders: [(kind, name, type)]; `{a b : T}` gives two."""
    out = []
    for o, inner in groups:
        if o == '[':
            nm, ty = (inner.split(' : ', 1) if ' : ' in inner else ('', inner))
            out.append((KIND[o], nm.strip(), ty.strip()))
            continue
        names, ty = inner.split(' : ', 1)
        for nm in names.split():
            out.append((KIND[o], nm, ty.strip()))
    return out


def from_pi(text):
    """a Prop as Lean prints it -- leading `∀ <groups>,` and then top-level arrows -- to binders and a conclusion."""
    t = ' '.join(text.split())
    binders = []
    while True:
        if t.startswith('∀ '):
            head, rest = _top_split(t[2:], ',')[0], ','.join(_top_split(t[2:], ',')[1:])
            gs, left = _groups(head)
            if left:
                raise ValueError('a binder of another shape: %r' % head[:80])
            binders += _expand(gs)
            t = rest.strip()
            continue
        parts = _top_split(t, ' → ')
        if len(parts) > 1:
            binders += [('hypothesis', '', p.strip()) for p in parts[:-1]]
            t = parts[-1].strip()
        return binders, t


def from_signature(text):
    """a theorem's signature as its source writes it -- `<groups> : <type>` -- to binders and a conclusion (the type read by from_pi)."""
    t = ' '.join(text.split())
    gs, rest = _groups(t)
    if not rest.startswith(': '):
        raise ValueError('no type after the binders: %r' % rest[:80])
    more, concl = from_pi(rest[2:])
    return _expand(gs) + more, concl


def strip_ns(s, kernel):
    for p in STRIP[kernel]:
        s = s.replace(p, '')
    return s


def normal(binders, concl, kernel):
    """namespaces stripped; each bound name replaced by its position in every later type and in the conclusion; whitespace collapsed."""
    out, names = [], []
    for i, (k, nm, ty) in enumerate(binders, 1):
        ty = strip_ns(ty, kernel)
        for j, n in names:
            ty = re.sub(r'(?<![\w.₀-₉\'])%s(?![\w₀-₉\'])' % re.escape(n), '#%d' % j, ty)
        out.append((k if k != 'hypothesis' else 'explicit', ' '.join(ty.split())))
        if nm:
            names.append((i, nm))
    c = strip_ns(concl, kernel)
    for j, n in names:
        c = re.sub(r'(?<![\w.₀-₉\'])%s(?![\w₀-₉\'])' % re.escape(n), '#%d' % j, c)
    return out, ' '.join(c.split())


def compare(a, b):
    """a, b: (binders, conclusion, kernel). Rows: (position, a's binder, b's binder, AGREE/DIFFERS, why); the first differing position."""
    na, ca = normal(a[0], a[1], a[2])
    nb, cb = normal(b[0], b[1], b[2])
    rows, first = [], None
    for i in range(max(len(na), len(nb))):
        x = a[0][i] if i < len(a[0]) else None
        y = b[0][i] if i < len(b[0]) else None
        if x is None or y is None:
            why = 'no binder at this position on the %s side' % ('first' if x is None else 'second')
            ok = False
        else:
            ok = na[i] == nb[i]
            why = 'kind and type equal up to bound names' if ok else ('kind %s against %s' % (na[i][0], nb[i][0]) if na[i][0] != nb[i][0] else '') + \
                ('; ' if na[i][0] != nb[i][0] and na[i][1] != nb[i][1] else '') + ('type %r against %r' % (na[i][1], nb[i][1]) if na[i][1] != nb[i][1] else '')
        rows.append((str(i + 1), x, y, 'AGREE' if ok else 'DIFFERS', why))
        if not ok and first is None:
            first = i + 1
    okc = ca == cb
    rows.append(('conclusion', a[1], b[1], 'AGREE' if okc else 'DIFFERS', 'equal up to bound names' if okc else '%r against %r' % (ca, cb)))
    verdict = 'HOLDS-BY-CORRESPONDENCE' if first is None and okc else 'DIFFERS at %s' % ('binder %d' % first if first else 'the conclusion')
    return rows, verdict


def show_binder(b):
    if b is None:
        return '--'
    k, nm, ty = b
    o, c = {'explicit': '()', 'implicit': '{}', 'instance': '[]', 'strict-implicit': '⦃⦄'}.get(k, ('', ''))
    return ('%s%s : %s%s' % (o, nm, ty, c)) if nm else ('%s (unnamed hypothesis)' % ty)


# ================================================================================ THE SOURCES
def probe_cell(name):
    L = rd(os.path.join(D, PROBE)).split(NL)
    a = L.index('@@BEGIN %s' % name)
    b = L.index('@@END %s' % name)
    st = L.index('@@STMT', a)
    ax = L.index('@@AXIOMS', a)
    return a + 1, b + 1, NL.join(L[st + 1:ax])


def h2_print():
    a, b, stmt = probe_cell(CLAUSE)
    head, value = stmt.split(':=', 1)
    return a, b, stmt, value.strip()


def ef_names_reading():
    """answer 2's further reading: every programme name h2_sign's print carries, resolved to the file that defines it at v0.34, each file
    compared byte for byte from v0.26 to v0.34; the toolchain and the Mathlib manifest beside."""
    _a, _b, stmt, _v = h2_print()
    names = sorted(set(re.findall(r'SIDEExplicitFormula\.B321\.(\w+)', stmt)))
    rows = []
    for n in names:
        rc, out = git(EF, 'grep', '-n', '-E', r'^(noncomputable )?(def|theorem|abbrev|structure) %s\b' % n, EF_TAG, '--', '*.lean')
        hit = out.strip().split(NL)[0] if out.strip() else ''
        f = hit.split(':')[1] if hit.count(':') >= 2 else ''
        same = bool(f) and git(EF, 'diff', '--quiet', EF_PRINT_PIN, EF_TAG, '--', f)[0] == 0
        rows.append((n, f, hit.split(':')[2] if hit.count(':') >= 2 else '', same))
    pins = [(f, git(EF, 'diff', '--quiet', EF_PRINT_PIN, EF_TAG, '--', f)[0] == 0) for f in ('lean-toolchain', 'lake-manifest.json')]
    return rows, pins


def lv_dispatch_reading():
    """answer 1: whether a hosted run at v0.13.0 can print the face's #print sig -- the workflow at the tag read for a print step naming it;
    the closure step on main read for a statement output."""
    _rc, wf = git(LV, 'show', '%s:.github/workflows/build-module.yml' % LV_TAG)
    prints = re.findall(r'^\s*#print (?:axioms )?([\w.]+)', wf, re.M)
    sig_step = any(LV_NAME in p for p in prints) or '#print sig' in wf
    has_cc = git(LV, 'cat-file', '-e', '%s:CircuitClosure.lean' % LV_TAG)[0] == 0
    return dict(prints=prints, sig_step=sig_step, closure_file_at_tag=has_cc)


def lv_source():
    _rc, src = git(LV, 'show', '%s:%s' % (LV_TAG, LV_FILE))
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s' % LV_NAME))
    j = next(k for k in range(i, len(L)) if L[k].rstrip().endswith(':='))
    sig = NL.join(L[i:j + 1])
    sig = sig[len('theorem %s' % LV_NAME):].rstrip()
    sig = sig[:-2].rstrip()
    return i + 1, j + 1, sig


def corr_row():
    nz = rd(os.path.join(D, NODES)).split(NL)
    k = next(i for i, l in enumerate(nz) if l.startswith('@corr SIDE-lv-conservation |'))
    page = rd(os.path.join(PP, FACES_PAGE)).split(NL)
    p = next(i for i, l in enumerate(page) if l.startswith('| `%s` | SIDE-lv-conservation |' % LV_NAME))
    return k + 1, nz[k], p + 1, page[p]


# ================================================================================ THE READING
def main(*a):
    L = ['b698 -- CORRESPONDENCE-DOMINANCE BUILT AND READ, (R308)(3): THE CLAUSE`S REACH INTO SIDE-lv-conservation THROUGH THE FACES PAGE`S '
         'CORRESPONDENCE ROW, BY STATEMENT IDENTITY (%s)' % utc(), '',
         '### the reader: relay tools/circuit_correspondence.py (spec: relay data/b695_circuit_spec.txt :53-:64). Rows are binders aligned by position:',
         '### position | h2_sign`s binder | the face`s binder | AGREE or DIFFERS | why (namespaces stripped, bound names read by position).', '']
    a1, b1, stmt, value = h2_print()
    h2 = from_pi(value) + ('SIDE-explicit-formula',)
    # ### the controls, before the real reading
    L += ['== THE CONTROLS, PRINTED BEFORE THE REAL READING']
    rows, v = compare(h2, h2)
    L += ['  (C1) h2_sign against itself (relay data/%s :%d-:%d): %s' % (PROBE, a1, b1, v)]
    L += ['       %-10s | %-40s | %-40s | %s' % (r[0], show_binder(r[1]) if r[0] != 'conclusion' else r[1][:40], show_binder(r[2]) if r[0] != 'conclusion' else r[2][:40], r[3]) for r in rows]
    c1_ok = v == 'HOLDS-BY-CORRESPONDENCE' and all(r[3] == 'AGREE' for r in rows)
    planted = (list(h2[0]), h2[1], h2[2])
    planted[0][0] = (planted[0][0][0], planted[0][0][1], 'ℝ → ℝ')
    rows2, v2 = compare(h2, tuple(planted))
    L += ['  (C2) h2_sign against a planted statement, binder 1`s type ℝ → ℂ changed to ℝ → ℝ: %s' % v2]
    L += ['       %-10s | %-40s | %-40s | %s' % (r[0], show_binder(r[1]) if r[0] != 'conclusion' else r[1][:40], show_binder(r[2]) if r[0] != 'conclusion' else r[2][:40], r[3]) for r in rows2]
    c2_ok = v2 == 'DIFFERS at binder 1' and [r[3] for r in rows2] == ['DIFFERS'] + ['AGREE'] * (len(rows2) - 1)
    L += ['  ### ### **CONTROLS: C1 HOLDS AT EVERY BINDER %s ; C2 DIFFERS AT THE PLANTED BINDER (1) AND THERE ALONE %s.**' % (c1_ok, c2_ok), '']
    # ### the sources of the real reading
    names, pins = ef_names_reading()
    disp = lv_dispatch_reading()
    nk, nrow, pk, prow = corr_row()
    li, lj, sig = lv_source()
    lv = from_signature(sig) + ('SIDE-lv-conservation',)
    L += ['== THE SOURCES',
          '  the Correspondence row: relay data/%s :%d -- %s' % (NODES, nk, nrow),
          '                          PLACE-papers %s :%d (the row`s line in the page)' % (FACES_PAGE, pk),
          '  h2_sign: its #print at SIDE-explicit-formula %s = 82550e4, the faces page`s generator input, relay data/%s :%d-:%d (the author`s '
          'answer 2, option 1); the further reading -- every programme name the print carries, the file defining it at %s, that file byte for '
          'byte from %s to %s:' % (EF_PRINT_PIN, PROBE, a1, b1, EF_TAG, EF_PRINT_PIN, EF_TAG)]
    L += ['      %-10s %s :%s -- identical %s' % (n, f, ln, same) for n, f, ln, same in names]
    L += ['      %-10s identical %s' % (f, same) for f, same in pins]
    ef_ok = all(x[3] for x in names) and all(s for _f, s in pins) and bool(names)
    L += ['      ### EVERY FILE IDENTICAL %s: %s' % (ef_ok, 'the probe`s print stands for v0.34' if ef_ok else 'A FILE DIFFERS -- a hosted print at v0.34 is wanted (answer 2, option 3)')]
    L += ['  SIDE-lv-conservation`s face: %s at %s = %s, %s :%d-:%d' % (LV_NAME, LV_TAG, git(LV, 'rev-parse', '--short', LV_TAG + '^{commit}')[1].strip(), LV_FILE, li, lj),
          '      the dispatch reading (answer 1): the workflow at %s prints %s by #print axioms alone ; a step printing %s`s signature %s ; '
          'CircuitClosure.lean at the tag %s (main`s closure step banks names, not statements) -- A HOSTED RUN AT %s CANNOT PRINT IT: the '
          'fallback, SOURCE TEXT at %s (git show), the verdict qualified SOURCE AGAINST PRINT; no runner dispatched' % (
              LV_TAG, ', '.join(p.split('.')[-1] for p in disp['prints']) or 'nothing', LV_NAME, disp['sig_step'], disp['closure_file_at_tag'], LV_TAG, LV_TAG), '']
    if disp['sig_step']:
        sys.exit('### THE WORKFLOW AT THE TAG CAN PRINT THE FACE -- dispatch first (answer 1); NOTHING WRITTEN')
    # ### the real reading
    rows3, v3 = compare(h2, lv)
    L += ['== THE READING: h2_sign (SIDE-explicit-formula, PRINT) AGAINST %s (SIDE-lv-conservation, SOURCE TEXT) -- binders %d against %d' % (
        LV_NAME, len(h2[0]), len(lv[0]))]
    for r in rows3:
        if r[0] == 'conclusion':
            L += ['  conclusion | h2_sign: %s' % r[1], '             | %s: %s' % (LV_NAME, r[2]), '             | %s | %s' % (r[3], r[4])]
        else:
            L += ['  binder %-3s | h2_sign: %s' % (r[0], show_binder(r[1])), '             | %s: %s' % (LV_NAME, show_binder(r[2])), '             | %s | %s' % (r[3], r[4])]
    nag = sum(1 for r in rows3 if r[3] == 'AGREE')
    fd = next((r for r in rows3 if r[3] == 'DIFFERS'), None)
    if fd is not None and fd[0] != 'conclusion':
        v3 = '%s: h2_sign`s %s against %s`s %s' % (v3, show_binder(fd[1]), LV_NAME, show_binder(fd[2]))
    L += ['', '### the summary follows the rows: AGREE %d ; DIFFERS %d of %d rows (binders and the conclusion).' % (nag, len(rows3) - nag, len(rows3)),
          '### ### **CORRESPONDENCE-DOMINANCE, SIDE-lv-conservation: %s (SOURCE AGAINST PRINT) ; CONTROLS C1 %s, C2 %s ; CLAUSE-DOMINANCE: 1 OF 2 BY '
          'CLOSURE ; %s BY CORRESPONDENCE.**' % (v3, c1_ok, c2_ok, '2 OF 2' if v3 == 'HOLDS-BY-CORRESPONDENCE' else v3)]
    if 'dry' in a:
        print(NL.join(L))
        return
    for name, data in (('b698_correspondence_dominance.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b698_correspondence_dominance.json', (json.dumps(dict(at=utc(), verdict=v3, controls=dict(c1=c1_ok, c2=c2_ok), ef_identical=ef_ok,
                                                                               dispatch=disp, rows=[[r[0], show_binder(r[1]) if r[0] != 'conclusion' else r[1],
                                                                                                     show_binder(r[2]) if r[0] != 'conclusion' else r[2], r[3], r[4]]
                                                                                                    for r in rows3]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    main(*sys.argv[1:])
