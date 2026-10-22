# -*- coding: utf-8 -*-
"""b703_standing_figures.py -- (R313)(7), THE FOUR STANDING ARMS' FIGURES, on the author's word "add needed arms" (W-ORD-STANDING-ARMS-B703,
PLACE-papers OPEN_TRAILS :15456).

### Each figure a reading printed every act; its baseline b703's figure, banked by tools/b703_record.py `figures` as data/b703_standing_figures.json;
### the arm (tools/b703_checks.py and its successors) fails from b704 on a regression from the previous act's figure, not on the figure itself.
###   correspondence()  G-CORRESPONDENCE-CURRENCY -- every roster paper's Correspondence rows (relay data/b672_roster_read.json's tables, each read
###                     by its anchor through tools/correspondence_gen.py's own readers, imported unedited) against the kernel's current tag (its
###                     highest v-tag in the local clone) and the declaration's statement at the cited tag and at the current one: one line per
###                     paper -- current, behind, at a moved tag with a changed statement, unread; the figure the changed-statement count.
###   readme()          G-README-CURRENCY -- the PLACE-papers README's kernel tags read against each kernel's highest tag at its remote (one
###                     ls-remote per repository per run, b616_claims.remote_refs) and its kernel counts against the federation's clones; the
###                     figure the stale lines.
###   partners()        G-PARTNER-COPIES -- the lines differing between the two copies of each roster paper (difflib, autojunk off); the figure
###                     the total, until W-ORD-PAPER-PARTNER-COPIES's disposition at b706.
###   pins()            G-SISTER-PINS -- each kernel's lean-toolchain and Mathlib revision (its working tree's two files) beside the federation's
###                     (the most frequent pin); the figure the faces page's kernels whose pin differs from the baseline's.
### No figure is a verdict; every reader prints its rows. Written by the Write tool at b703; it writes nothing.
"""
import collections
import difflib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import correspondence_gen as CG   # noqa: E402  ### the generator's readers, imported unedited
import b616_claims as KC0         # noqa: E402  ### the one remote read per repository per run

PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = chr(10)
ROSTER = 'b672_roster_read.json'
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
VTAG = re.compile(r'^v(\d+(?:\.\d+)*)$')


def _g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def _read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except OSError:
        return ''


def _roster():
    try:
        return json.load(io.open(os.path.join(D, ROSTER), encoding='utf-8')).get('tables') or []
    except Exception:
        return []


def _vkey(tag):
    m = VTAG.match(tag)
    return tuple(int(x) for x in m.group(1).split('.')) if m else None


_HIGH = {}


def highest_local(kernel):
    """the kernel's highest v-tag in its local clone, or None."""
    if kernel not in _HIGH:
        p = 'D:/' + kernel
        tags = [t for t in _g(p, 'tag', '-l', 'v*')[1].split(NL) if _vkey(t.strip())] if os.path.isdir(p) else []
        _HIGH[kernel] = max(tags, key=lambda t: _vkey(t.strip())).strip() if tags else None
    return _HIGH[kernel]


_DECL = {}
DECL = r'^(@\[[^]]*\] *)?((private|protected|noncomputable|nonrec) +)*(theorem|lemma|def|abbrev|structure|class|inductive|instance) +%s([ :({[]|$)'   # ### POSIX ERE (git grep -E)


def decl_at(kernel, tag, short):
    """the declaration's header at the tag, whitespace collapsed: from its line to the first `:=` or ` where` (git grep at the tag over the
    kernel's *.lean, the first hit), or '' where it is not read."""
    key = (kernel, tag, short)
    if key not in _DECL:
        p = 'D:/' + kernel
        rc, out = _g(p, 'grep', '-n', '-E', DECL % re.sub(r'([.\[\]()*+?{}|^$\\])', r'\\\1', short), tag, '--', '*.lean')
        hit = next((l for l in out.split(NL) if l.count(':') >= 3), '')
        text = ''
        if hit:
            _t, f, ln, _rest = hit.split(':', 3)
            rc2, blob = _g(p, 'show', '%s:%s' % (tag, f))
            ls = blob.split(NL)
            i = int(ln) - 1
            buf = []
            for j in range(i, min(len(ls), i + 40)):
                buf.append(ls[j])
                if ':=' in ls[j] or re.search(r'\swhere\s*$', ls[j]):
                    break
            text = ' '.join(' '.join(buf).split(':=')[0].split())
        _DECL[key] = text
    return _DECL[key]


def correspondence():
    """per paper: the rows current, behind, at a moved tag with a changed statement, unread; the figure the changed-statement rows."""
    papers = []
    for t in _roster():
        path = os.path.join(PP, *t['path'].split('/'))
        lines = _read(path).split(NL)
        r = CG.find_table(lines, t)
        row = dict(paper=t['doc'], path=t['path'], current=0, behind=0, changed=0, unread=0, changed_rows=[], reason=None)
        if not isinstance(r, tuple):
            row['reason'] = r
            papers.append(row)
            continue
        j, e = r
        cols = CG.columns(lines[j])
        if cols['kernel'] is None or cols['terminal'] is None:
            row['reason'] = 'NOT IN THE GENERATOR`S SHAPE'
            papers.append(row)
            continue
        prev_k = None
        for i in range(j + 1, e):
            l = lines[i]
            if CG.SEP_ROW.match(l):
                continue
            sp = CG.spans(l)
            if len(sp) <= max(cols['kernel'], cols['terminal']):
                row['unread'] += 1
                continue
            kc, tc = CG.cell(l, sp[cols['kernel']]), CG.cell(l, sp[cols['terminal']])
            cl = CG.parse_kernel_cell(kc)
            k = (cl[0][0] if cl else None) or prev_k
            prev_k = k or prev_k
            ver = next((x for _s, _e, kind, x in (cl[0][1] if cl else []) if kind == 'ver'), None)
            m = CG.IDENT.search(tc)
            if not k or not ver or not m:
                row['unread'] += 1
                continue
            cur = highest_local(k)
            if cur is None:
                row['unread'] += 1
                continue
            if ver == cur:
                row['current'] += 1
                continue
            row['behind'] += 1
            short = m.group(1).split('.')[-1]
            d0, d1 = decl_at(k, ver, short), decl_at(k, cur, short)
            if d0 and d1 and d0 != d1:
                row['changed'] += 1
                row['changed_rows'].append(':%d %s %s -> %s %s' % (i + 1, k, ver, cur, short))
        papers.append(row)
    return sum(p['changed'] for p in papers), papers


README_TAG = re.compile(r'(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)(?:(?!SIDE-)[^|\n]){0,80}?(?<![\w.])\*{0,2}`?(v\d+(?:\.\d+)+)`?')   # ### a read stops at the next kernel's name
README_COUNT = re.compile(r'\b(\d+)\s+(?:Lean\s+)?kernels\b')


def readme(remote=None):
    """the README's lines naming a kernel's tag, each against the kernel's highest tag at its remote, and its kernel counts against the
    federation's clones; the figure the stale lines."""
    remote = remote or KC0.remote_refs
    rows = []
    t = _read(os.path.join(PP, 'README.md')).split(NL)
    feds = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    for n, l in enumerate(t, 1):
        for m in README_TAG.finditer(l):
            k, v = m.group(1), m.group(2)
            if not os.path.isdir('D:/' + k):
                rows.append(dict(line=n, kernel=k, cited=v, highest=None, state='UNREAD'))
                continue
            tags = [r[len('refs/tags/'):] for r in remote('D:/' + k) if r.startswith('refs/tags/') and not r.endswith('^{}')]
            hi = max((x for x in tags if _vkey(x)), key=_vkey, default=None)
            rows.append(dict(line=n, kernel=k, cited=v, highest=hi, state='CURRENT' if hi == v else ('STALE' if hi else 'UNREAD')))
        for m in README_COUNT.finditer(l):
            rows.append(dict(line=n, kernel='(the count)', cited=m.group(1), highest=str(len(feds)),
                             state='CURRENT' if m.group(1) == str(len(feds)) else 'STALE'))
    stale_lines = sorted(set(r['line'] for r in rows if r['state'] == 'STALE'))
    return len(stale_lines), rows


def partners():
    """per roster paper with a partner copy: the lines differing between the two copies' Correspondence tables -- the unit of
    W-ORD-PAPER-PARTNER-COPIES and of reading 4's 131 lines (relay data/b700_reading4.txt :66-:76) -- each table found by its anchor in each
    copy (tools/correspondence_gen.py's find_table), difflib over its lines, autojunk off, each non-equal opcode counted at the larger side; a
    copy whose table is not found counted apart. The figure the total."""
    out = []
    for t in _roster():
        a, b = t.get('path'), t.get('partner')
        if not a or not b or a == b:
            continue
        x = _read(os.path.join(PP, *a.split('/'))).split(NL)
        y = _read(os.path.join(PP, *b.split('/'))).split(NL)
        rx, ry = CG.find_table(x, t), CG.find_table(y, t)
        if not isinstance(rx, tuple) or not isinstance(ry, tuple):
            out.append(dict(paper=t['doc'], path=a, partner=b, differing=None, reason='%s ; %s' % (rx if not isinstance(rx, tuple) else 'found',
                                                                                                  ry if not isinstance(ry, tuple) else 'found')))
            continue
        tx, ty = x[rx[0]:rx[1]], y[ry[0]:ry[1]]
        n = sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tx, ty, autojunk=False).get_opcodes() if tag != 'equal')
        out.append(dict(paper=t['doc'], path=a, partner=b, differing=n, reason=None))
    return sum(r['differing'] or 0 for r in out), out


def _pin(kernel):
    p = 'D:/' + kernel
    lean = _read(os.path.join(p, 'lean-toolchain')).strip()
    man = _read(os.path.join(p, 'lake-manifest.json'))
    try:
        pk = json.loads(man).get('packages') or []
        ml = next((x.get('rev') for x in pk if x.get('name') == 'mathlib'), None)
    except Exception:
        ml = None
    return lean or None, ml


def faces_kernels():
    return sorted(set(re.findall(r'\b(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)\b', _read(os.path.join(PP, FACES_PAGE)))))


def pins(baseline=None):
    """each kernel's Lean version and Mathlib revision beside the federation's (the most frequent pair); the figure the faces page's kernels
    whose pin differs from the baseline's (b703's figure, data/b703_standing_figures.json, at b703 itself and each act after)."""
    feds = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    rows = dict((k, _pin(k)) for k in feds)
    fed = collections.Counter(v for v in rows.values() if v[0]).most_common(1)
    fk = faces_kernels()
    base = dict((k, tuple(v)) for k, v in (baseline or {}).items())
    moved = [k for k in fk if k in rows and k in base and tuple(rows[k]) != base[k]]
    return len(moved), dict(rows=rows, federation=fed[0][0] if fed else None, faces=fk, moved=moved)


def all_figures(baseline=None, remote=None):
    c, cr = correspondence()
    r, rr = readme(remote)
    p, pr = partners()
    s, sr = pins(baseline)
    return dict(correspondence=dict(figure=c, papers=cr), readme=dict(figure=r, rows=rr), partners=dict(figure=p, rows=pr),
                pins=dict(figure=s, rows=sr['rows'], federation=sr['federation'], faces=sr['faces'], moved=sr['moved']))
