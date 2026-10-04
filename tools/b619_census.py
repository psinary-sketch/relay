# -*- coding: utf-8 -*-
"""b619_census.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R229)(3): THE_KEYSTONE_CENSUS AT v0.4.

### b610's resolvers (tools/b610_census.py) are IMPORTED, never copied, and pointed at this act's pins: REGISTRY.md, the documents,
### SPIRAL_MAP.md, the sieve's v0.5 and OPEN_TRAILS.md at PLACE-papers 9dbac4b (REGISTRY's blob is a939198's, b618's append); the
### mirror roster at relay db0aaa5b (this act's step zero); the remotes by `git ls-remote`, once per repository. This module writes
### nothing: `python tools/b619_census.py` runs the resolvers and prints; tools/b619_record.py banks.
### The readings v0.4 adds to b610's, each the seat's and strikeable:
###   R-1, WIDENED -- a dated row update's table of Version cells (its second cell a `REGISTRY.md:n` pointer, b618's of 2026-10-04 at
###     REGISTRY :978-:994) is a cell layer over the rows it points to, as the ratified-titles table is a title layer: printed, not counted.
###   R-2, BY ITS LETTER -- "a dated row addition lands in the cluster its heading names": a heading naming Phase 2B-2G places its rows
###     there, as a heading naming Phase 1.5A-H always did (b610's resolver read the 1.5 letters only; no Phase 2 heading stood then);
###     and a row whose own provenance names Phase 1.2 as its cluster (1.5a-9, the synthesis for cluster Phase 1.2; 1.5a-10, the spine
###     of the cluster of Phase 1.2) lands in Phase 1.2 beside 1.5a-1 to 1.5a-4, as `(R229)`(3) names 1.2's synthesis in its row.
###   R-6, THE UNPUSHED MARK -- a kernel's cell names, beside the remote's current tag, every tag its clone carries and its remote does
###     not, by name and peeled commit, marked unpushed (W-ORD-TAG-REMOTES, OPEN_TRAILS :12597).
###   R-9, A DATED APPEND -- a registry row's file, held at v0.3's commit (f374bba), that gained a dated append in its own form since is
###     named in its edition-state cell by the commit that appended it; an append is not an edition by the form, and a file created since
###     is not appended to.
###   R-10, THE SYNTHESES -- the six syntheses' rows name, in their keystones cell, the file read and its version as the document's
###     own version line gives it, and the tier its own class line gives (2D at its v0.2).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b610_census as C  # noqa: E402

NL = chr(10)
PP = C.PP
PRE_PP = '9dbac4b'
V03_PP = 'f374bba'          # ### the PLACE-papers commit that carried census v0.3 (c83c72b) and SPIRAL_MAP v0.7 to the remote
STEPZERO = 'db0aaa5b'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
SIEVE5 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md'
TAG_REMOTES = ('SIDE-bijection', 'SIDE-class-coupling', 'SIDE-coupling', 'SIDE-formation-arithmetic', 'SIDE-meta', 'SIDE-omega-b',
               'SIDE-orchestrator', 'SIDE-residual-bridge', 'SIDE-substrate-cluster')   # ### OPEN_TRAILS :12597, its nine kernels
SYN = {'1.5a-9': ('P12', 'b611'), '1.5e-7': ('15E', 'b612'), 'p2-36': ('2B', 'b613'), 'p2-37': ('2D', 'b614'), 'p2-38': ('2F', 'b615'),
       'p2-d10': ('2G', 'b616')}
P12_PROV = re.compile(r'the synthesis for cluster Phase 1\.2|the cluster of Phase 1\.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### b610's resolvers at this act's pins
C.PRE_PP = PRE_PP
C.STEPZERO = STEPZERO
C.SIEVE4 = SIEVE5
C.TRACKED = None
_show0 = C.show


def show(path, rev=None, repo=PP):
    return _show0(path, rev or C.PRE_PP, repo)


C.show = show
_rows0 = C.registry_rows
_place0 = C.place
REFS_UPDATE = []


def registry_rows(R=None):
    """### b610's population rule, R-1 widened: a row-update table's Version cells set apart as a cell layer."""
    rows, refs = _rows0(R)
    keep = []
    del REFS_UPDATE[:]
    for r in rows:
        c = C._cells(r['text'])
        if len(c) > 1 and re.match(r'^`REGISTRY\.md:\d+`$', c[1]):
            REFS_UPDATE.append(dict(line=r['line'], id=r['id'], points=c[1].strip('`')))
            continue
        keep.append(r)
    return keep, refs


def place(r):
    """### b610's placement rule, R-2 read by its letter for Phase 2 headings and for a provenance naming Phase 1.2."""
    sec = r['sec']
    if sec.startswith('Row addition') and P12_PROV.search(r['text']):
        return 'P12', 'its own provenance names Phase 1.2 as its cluster, filed under 1.5A as the phase attribute files 1.5a-1..4 (REGISTRY :780)'
    if sec.startswith('Row addition'):
        m = re.search(r'\(Phase 2([A-G])\b', sec)
        if m:
            return '2' + m.group(1), 'the row addition`s heading names Phase 2%s' % m.group(1)
    return _place0(r)


C.registry_rows = registry_rows
C.place = place


# ================================================================================ VERSION LINES (b618's finder, imported)
def vline(path):
    import b618_record as R8
    return R8.vline(path, PRE_PP)


# ================================================================================ THE DATED APPENDS SINCE v0.3 (R-9)
def appended(path):
    """### the commits since v0.3's commit that changed a registry row's file, each an append in its own form: [(sha, act)]"""
    if not path or path not in C.tracked():
        return []
    if subprocess.run(['git', '-C', PP, 'cat-file', '-e', '%s:%s' % (V03_PP, path)], capture_output=True).returncode != 0:
        return []      # ### a file v0.3's commit did not hold was created since, not appended to
    out = []
    for l in C.g(PP, 'log', '--reverse', '--format=%h %s', '%s..%s' % (V03_PP, PRE_PP), '--', path).split(NL):
        if l.strip():
            h, s = l.split(' ', 1)
            out.append((h, s.split(' ', 1)[0]))
    return out


# ================================================================================ THE CELLS (b610's renderers, R-6, R-9, R-10)
def _short(r):
    return r['id'] or os.path.basename(r['path'] or '?')


def ks_cell(rs):
    by = {}
    for r in rs:
        if r['tier'] in C.KEYSTONE_TIERS:
            if r['id'] in SYN:
                lp = C.latest(r['path'])
                v = vline(lp)
                by.setdefault(r['tier'], []).append('%s (`%s` %s)' % (r['id'], lp, v[1]))
            else:
                by.setdefault(r['tier'], []).append(_short(r))
    out = ['%s: %s' % (t, ', '.join(by[t])) for t in ('K', 'KC', 'C') if t in by]
    rest = {}
    for r in rs:
        if r['tier'] not in C.KEYSTONE_TIERS:
            rest.setdefault(r['tier'] or 'no tier read', []).append(_short(r))
    out += ['%s: %s' % (t, ', '.join(v)) for t, v in sorted(rest.items(), key=lambda x: str(x[0]))]
    return out


def ed_cell(rs):
    e = []
    for r in rs:
        if r['edition'][0] == 'EDITED':
            x = '%s %s' % (_short(r), r['edition'][1].split(' (')[0])
            if r['path'] == 'phase2/method/THE_KEYSTONE_CENSUS.md':
                x += ' (v0.4 this edition, beside it)'
            e.append(x)
    w = [_short(r) for r in rs if r['edition'][0] == 'WORK-LIST']
    n = sum(1 for r in rs if r['edition'][0] == 'NEITHER')
    out = ['edited by the form: %s' % (', '.join(e) or 'none')]
    if w:
        out.append('work-list alone: %s' % ', '.join(w))
    out.append('neither: %d' % n)
    mv = [_short(r) for r in rs if r['edition'][0] == 'MOVED']
    if mv:
        out.append('a moved row: %s' % ', '.join(mv))
    ap = ['%s %s (%s)' % (_short(r), ', '.join(h for h, _a in r['appended']), ', '.join(sorted(set(a for _h, a in r['appended']))))
          for r in rs if r.get('appended')]
    if ap:
        out.append('a dated append since v0.3: %s' % ', '.join(ap))
    return out


def sieve_cell(links):
    if not links:
        return ['none (no SPIRAL_MAP §4A cluster holds a member here)']
    return ['%s %s: %d row%s (via %s)' % (n, p, c, '' if c == 1 else 's', ', '.join(ms)) if p != '--' else '%s: 0 rows (the sieve carries none; via %s)' % (n, ', '.join(ms))
            for n, p, c, ms in links]


def ker_cell(kern, remotes):
    out = []
    for k in sorted(kern):
        rt = remotes.get(k) or {}
        if not rt.get('ok'):
            out.append('%s: not read (%s)' % (k, rt.get('err') or 'no read'))
            continue
        un = ''
        if rt.get('local_only'):
            un = ' (unpushed by name: %s)' % ', '.join('%s = %s' % tuple(t) for t in rt['local_only'])
        if not rt.get('current'):
            out.append('%s: no tag%s' % (k, un))
        else:
            dep = (' ; deposit ' + C.KERNEL_DEPOSITS[k]) if k in C.KERNEL_DEPOSITS else ''
            out.append('%s %s = %s%s%s' % (k, rt['current'], rt['remote_peel'][:7], un, dep))
    return out or ['none named']


def dep_cell(rs):
    d = [_short(r) for r in rs if r['deposit'][0] == 'DEPOSITED']
    m = [_short(r) for r in rs if r['deposit'][0] == 'MIRROR']
    n = sum(1 for r in rs if r['deposit'][0] == 'NEITHER')
    out = []
    if d:
        out.append('deposited at record %s: %s' % (C.DEPOSIT_RECORD[0], ', '.join(d)))
    if m:
        out.append('in the mirror alone: %s' % ', '.join(m))
    out.append('neither: %d' % n)
    mv = [_short(r) for r in rs if r['deposit'][0] == 'MOVED']
    if mv:
        out.append('a moved row: %s' % ', '.join(mv))
    return out


def cell(s):
    return s.replace('|', '¦')


def docs_cell(row):
    return '; '.join(('`%s` %s (:%d)' % (x['id'], os.path.basename(x['path'] or '') or 'no file', x['line'])) if x['id'] else
                     ('%s (:%d)' % (os.path.basename(x['path'] or '') or 'no file', x['line'])) for x in row['rows'])


def table_line(row):
    return '| %s | %s (REGISTRY :%s) | %s | %s | %s | %s | %s | %s |' % (
        row['n'], cell(row['label']), row['heading'], cell(docs_cell(row)), cell(' ; '.join(row['keystones'])), cell(' ; '.join(row['editions'])),
        cell(' ; '.join(row['sieve'])), cell(' ; '.join(row['kernels'])), cell(' ; '.join(row['deposit'])))


COLS = ('documents', 'keystones', 'editions', 'sieve', 'kernels', 'deposit')


def v03_cells(rev=PRE_PP):
    """### census v0.3's §1 rows at the pin, each split to its eight cells: {R01: {col: text}}"""
    out = {}
    for l in C.lines_of(show(CEN3, rev)):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if not m or not l.endswith(' |'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split(' | ')]
        if len(c) != 8:
            continue
        out[m.group(1)] = dict(line=l, label=c[1], documents=c[2], keystones=c[3], editions=c[4], sieve=c[5], kernels=c[6], deposit=c[7])
    return out


# ================================================================================ THE BUILD
def build(read_remotes=True):
    B = C.build(read_remotes=read_remotes)
    for r in B['rows']:
        r['appended'] = appended(r['path']) if not r.get('pointer') else []
    J = []
    for i, k in enumerate(C.KEYS, 1):
        rs = [r for r in B['rows'] if r['census'] == k]
        J.append(dict(n='R%02d' % i, key=k, label=C.LABEL[k], heading=B['heads'][k],
                      rows=[dict(line=r['line'], id=r['id'], path=r['path'], tier=r['tier'], tier_src=r['tier_src'], edition=r['edition'],
                                 deposit=r['deposit'], appended=r.get('appended') or [], why=r['why']) for r in rs],
                      keystones=ks_cell(rs), editions=ed_cell(rs), sieve=sieve_cell(B['sieve'][k]), kernels=ker_cell(B['kern'][k], B['remotes']),
                      kernel_src={x: v for x, v in B['kern'][k].items()}, deposit=dep_cell(rs),
                      has_keystone=any(r['tier'] in C.KEYSTONE_TIERS for r in rs)))
    for row in J:
        row['documents'] = docs_cell(row)
        row['table_line'] = table_line(row)
    B['J'] = J
    B['refs_update'] = list(REFS_UPDATE)
    return B


def syn_facts():
    """### each synthesis's own head at the pin: path read, version line, class-line tier -- what H53a reads the census against"""
    out = {}
    R = C.registry()
    rows, _refs = C.registry_rows(R)
    for r in rows:
        if r['id'] in SYN:
            lp = C.latest(r['path'])
            v = vline(lp)
            t, src = C.tier_of(r['path'])
            out[r['id']] = dict(base=r['path'], path=lp, version=v[1], vline=v[0], tier=t, tier_src=src, line=r['line'], key=SYN[r['id']][0])
    return out


def main():
    B = build(read_remotes='--remotes' in sys.argv)
    old = v03_cells()
    print('### REGISTRY at %s: %d rows ; %d title-layer references ; %d row-update cell references' % (PRE_PP, len(B['rows']), len(B['refs']),
                                                                                                     len(B['refs_update'])))
    print('### unplaced: %s' % [(r['line'], r['id']) for r in B['rows'] if not r['census']])
    for row in B['J']:
        diff = [c for c in COLS if (' ; '.join(row[c]) if isinstance(row[c], list) else row[c]) != old.get(row['n'], {}).get(c)]
        print('%s %-44s rows %2d keystone %-5s changed %s' % (row['n'], row['label'][:44], len(row['rows']), row['has_keystone'], diff))
    print('### keystone-less: %s' % [r['n'] for r in B['J'] if not r['has_keystone']])
    print('### syntheses: %s' % syn_facts())


if __name__ == '__main__':
    main()
