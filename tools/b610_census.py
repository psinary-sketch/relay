# -*- coding: utf-8 -*-
"""b610_census.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R220)(4): THE PHASE-STATE READING.

### Every cell is read here from a blob at a pin -- REGISTRY.md, the documents, SPIRAL_MAP.md, the sieve's v0.4 and OPEN_TRAILS.md at
### PLACE-papers 7055f04, the edition work-lists at relay 05ee3f9c -- or from a remote by `git ls-remote`, and none from recall. This
### module writes nothing: `python tools/b610_census.py` runs the resolvers and prints; tools/b610_record.py banks.
### The rules, each the seat's reading of (R220)(4) and strikeable:
###   POPULATION -- a REGISTRY row is a table row outside a code fence whose first cell is a registry ID (d1-n, 1.5x-n, p2-n, p2-dn,
###     m5-n) or whose first or second cell opens with a backticked document path, plus the one block entry naming a document outside
###     any table (the carrier specification, REGISTRY :117); the ratified-titles table (header `Internal file | ID | ...`) is a title
###     layer over rows that exist elsewhere and its rows are references, printed and not counted.
###   PLACEMENT -- a row lands in the census row of the REGISTRY heading it sits under; 1.5a-1 to 1.5a-4 land in Phase 1.2 by the
###     PHASE ATTRIBUTE's own words (REGISTRY :780); a dated `Row addition` lands in the cluster its heading names, else in the cluster its
###     own ID letter names (1.5c-n under 1.5C), else, for a p2 ID, in Phase 2's row of rows filed to no lettered cluster; the rows filed
###     under no phase heading (the m5 method rows, the REPARAMETERIZATION row, the carrier specification) take a row of their own.
###   TIER (R220)(3) -- read in this order: (1) the document's own class line under the standing taxonomy; (2) a sentence of the
###     document stating its tier; (3) a tier the author ruled by name (REGISTRY :669, THE_DOCUMENT_CLASS_TAXONOMY :39-:43) or the
###     registry's row; (4) the taxonomy's own presumptive class by name (:35 the cluster syntheses C, :36 the consults N); (5)
###     certification at a pin read from the cascade -- a CP-1 tier block with a terminal row at T0-T2 reads K; else NO TIER READ.
###     A keystone is a document read K, KC or C.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '7055f04'
STEPZERO = '05ee3f9c'
RELAY = ROOT.replace('\\', '/')
CENSUS, CENSUS3 = 'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
SPIRAL, SPIRAL7 = 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md'
SIEVE4 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'
M17 = 'day1/A_Place_to_Stand_v5_17.md'
ID_RE = re.compile(r'^(d1-\d+|1\.5[a-h]-\d+|p2-d?\d+|m5-\d+)$')
PATH_CELL = re.compile(r'^`([^`]+\.(?:md|py))`')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


TRACKED = None


def tracked():
    global TRACKED
    if TRACKED is None:
        TRACKED = set(x for x in g(PP, 'ls-tree', '-r', '--name-only', PRE_PP).split(NL) if x.strip())
    return TRACKED


# ================================================================================ THE CENSUS ROWS, IN REGISTRY ORDER
# key, label, the REGISTRY heading the row is read from (a needle; its line is printed at run time)
ROWS = [
    ('D1', 'Phase 1 / Day 1', '## DAY 1: The RH Proof Package'),
    ('P12', 'Phase 1.2 (filed under 1.5A by the phase attribute)', '| ### **`1.2`** |'),
    ('15A', '1.5A: Alternative Proof Presentations', '### 1.5A: Alternative Proof Presentations'),
    ('15B', '1.5B: Simplicity & Zero Structure', '### 1.5B: Simplicity & Zero Structure'),
    ('15C', '1.5C: Spectral & Structural Core', '### 1.5C: Spectral & Structural Core'),
    ('15D', '1.5D: GRH & Cascade', '### 1.5D: GRH & Cascade'),
    ('15E', '1.5E: Deep Structure', '### 1.5E: Deep Structure'),
    ('15F', '1.5F: Syntheses', '### 1.5F: Syntheses'),
    ('15G', '1.5G: R-Curve & Monotonicity', '### 1.5G: R-Curve & Monotonicity'),
    ('15H', '1.5H: SIDE Method Papers', '### 1.5H: SIDE Method Papers'),
    ('2A', '2A: Formation Calculus & κ Theory', '### 2A: Formation Calculus & κ Theory'),
    ('2B', '2B: Consciousness, Cognition, Philosophy', '### 2B: Consciousness, Cognition, Philosophy'),
    ('2C', '2C: Impossibility, Difficulty, Method', '### 2C: Impossibility, Difficulty, Method'),
    ('2D', '2D: Physics & Cosmology', '### 2D: Physics & Cosmology'),
    ('2E', '2E: Error Correction & Quantum', '### 2E: Error Correction & Quantum'),
    ('2F', '2F: Empirical & Competition', '### 2F: Empirical & Competition'),
    ('2G', '2G: Physics (Speculative — UNREVIEWED)', '### 2G: Physics (Speculative — UNREVIEWED)'),
    ('P2X', 'Phase 2, rows filed to no lettered cluster', '## Row addition — 2026-07-12 (O.10-tail placement'),
    ('SUP', 'SUPPORT: cluster syntheses and consults', '## SUPPORT TIER: Cluster Syntheses + Consults (clusters/)'),
    ('INT', 'INTERNAL: reference works', '## INTERNAL: Reference Works (not for publication)'),
    ('GS', 'The junction / global-section era (the phase row)', "## PHASE ROW — THE_GLOBAL_SECTION's era"),
    ('ANX', 'ANNEX: the download layer', '## ANNEX: Download-Layer (non-keystone, outside the repo tree)'),
    ('NOPH', 'Rows filed under no phase heading', '| `phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md` | m5-5 |'),
]
KEYS = [r[0] for r in ROWS]
LABEL = dict((k, l) for k, l, _n in ROWS)
P12_IDS = ('1.5a-1', '1.5a-2', '1.5a-3', '1.5a-4')


def registry():
    return lines_of(show('REGISTRY.md'))


def heading_lines(R):
    out = {}
    for k, _l, needle in ROWS:
        out[k] = next((i + 1 for i, l in enumerate(R) if l.startswith(needle)), None)
    return out


def _cells(l):
    return [c.strip() for c in l.strip().strip('|').split('|')]


def registry_rows(R=None):
    """### every REGISTRY row by the population rule, with its heading context; and the title-layer references, apart."""
    R = R or registry()
    rows, refs, fence, sec, sub, hdr = [], [], False, '', '', None
    for i, l in enumerate(R, 1):
        if l.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        if l.startswith('## '):
            sec, sub, hdr = l[3:].strip(), '', None
            continue
        if l.startswith('### '):
            sub, hdr = l[4:].strip(), None
            continue
        if not l.startswith('|'):
            if l.strip():
                hdr = None
            continue
        if re.match(r'^\|\s*:?-', l):
            hdr = _cells(R[i - 2])
            continue
        if i < len(R) and re.match(r'^\|\s*:?-', R[i]):
            continue
        c = _cells(l)
        ident = c[0] if ID_RE.match(c[0]) else (c[1] if len(c) > 1 and ID_RE.match(c[1]) and c[1].startswith('m5-') else None)
        p0 = PATH_CELL.match(c[0])
        p1 = PATH_CELL.match(c[1]) if len(c) > 1 else None
        if hdr and hdr[:2] == ['Internal file', 'ID']:
            refs.append(dict(line=i, cell=c[0], id=c[1]))
            continue
        if not (ident or p0 or (p1 and not re.match(r'^\d{4}-\d\d-\d\d$', c[0]))):
            continue
        files = re.findall(r'`([^`]+\.(?:md|py))`', l)
        path = (p0 or p1).group(1) if (p0 or p1) else next((f for f in files if '/' in f), None)
        rows.append(dict(line=i, id=ident or '', sec=sec, sub=sub, path=path, cells=c[:3], text=l))
    blk = next((i + 1 for i, l in enumerate(R) if l.startswith('**Carrier specification (paper):**')), None)
    if blk:
        m = re.search(r'`([^`]+\.md)`', R[blk - 1])
        rows.append(dict(line=blk, id='', sec='DAY 1: The RH Proof Package', sub='(a block entry, no table)', path=m.group(1), cells=['(block)'],
                         text=R[blk - 1]))
    rows.sort(key=lambda r: r['line'])
    return rows, refs


def place(r):
    """### the placement rule (module docstring); returns (census key, the reason in words)."""
    i, sec, sub = r['id'], r['sec'], r['sub']
    if i in P12_IDS:
        return 'P12', 'the phase attribute names 1.5a-1..4 as Phase 1.2 (REGISTRY :780)'
    if sub == '(a block entry, no table)':
        return 'NOPH', 'a block entry under no table and no phase heading of its own (a phase2/method document sitting in the Day-1 section)'
    if sec.startswith('DAY 1') and i.startswith('d1-'):
        return 'D1', 'the Day-1 table'
    m = re.match(r'^1\.5([A-H]):', sub)
    if m:
        return '15' + m.group(1), 'its table, under ### %s' % sub
    m = re.match(r'^2([A-G]):', sub)
    if m:
        return '2' + m.group(1), 'its table, under ### %s' % sub
    if sec.startswith('Row addition'):
        m = re.search(r'\(Phase 1\.5([A-H])\b', sec)
        if m:
            return '15' + m.group(1), 'the row addition`s heading names Phase 1.5%s' % m.group(1)
        m = re.match(r'^1\.5([a-h])-', i)
        if m:
            return '15' + m.group(1).upper(), 'the row addition names no cluster; its ID`s letter is %s' % m.group(1)
        if i.startswith('p2-'):
            return 'P2X', 'the row addition names no lettered cluster; a Phase 2 ID'
    if sec.startswith('SUPPORT TIER'):
        return 'SUP', 'the support tier`s table'
    if sec.startswith('INTERNAL'):
        return 'INT', 'the internal reference works` table'
    if sec.startswith('PHASE ROW'):
        return 'GS', 'the phase row (its own era, REGISTRY :352)'
    if sec.startswith('ANNEX'):
        return 'ANX', 'the annex`s table'
    if sec.startswith('RATIFIED PUBLIC TITLES'):
        return 'NOPH', 'a row in the titles section, under no phase heading'
    return None, 'NO RULE REACHES IT'


# ================================================================================ TIER (R220)(3)
CLASS_RE = re.compile(r'DOCUMENT CLASS — THE STANDING TAXONOMY \(K/C/N/E, author-ruled 2026-07-28\): (?:### )?(TIER (?:KC|K|C|N|E)|NOT PLACED)')
SENT_RE = re.compile(r'[Tt]his document (?:stays|is|remains) (?:\*\*)?Tier (KC|K|C|N|E)\b')
RULED = {   # ### a tier the author ruled by name, with its address
    'phase1.5/method/THE_METHOD_CANON.md': ('K', 'REGISTRY :669, m5-1 K'),
    'phase1.5/method/THE_SECOND_EXEMPLAR.md': ('K', 'REGISTRY :669, m5-2 K'),
    'phase1.5/method/THE_SUBSTRATE.md': ('K', 'REGISTRY :669, m5-3 K; THE_DOCUMENT_CLASS_TAXONOMY :43'),
    'phase1.5/method/CONCLUSIONS_OF_RECORD.md': ('C', 'REGISTRY :669, m5-4 C; THE_DOCUMENT_CLASS_TAXONOMY :42'),
    'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md': ('K', 'REGISTRY :669, m5-5 K'),
    'internal/CATALOGOS.md': ('C', 'THE_DOCUMENT_CLASS_TAXONOMY :40, author-ruled: CATALOGOS C'),
    'phase2/formation/UNIVERSALITY.md': ('K', 'THE_DOCUMENT_CLASS_TAXONOMY :41, author-ruled: UNIVERSALITY K, with the C-scope note'),
    'heritage/PRIME_CORE_READER.md': ('N', 'REGISTRY :582, its own row: TIER N'),
    'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md': ('N', 'REGISTRY :687, its own row: Tier N'),
}
TIERBLOCK_RE = re.compile(r'^#### \*{0,2}THE CASCADE, ACT [A-Z]+ -- THE CORRESPONDENCE TIERED')
TROW_RE = re.compile(r'\|\s*(T0|T1|T1-lit|T2|T2-INTERFACES)\s*\|\s*$')


def tier_block(text):
    ls = lines_of(text)
    i = next((n for n, l in enumerate(ls) if TIERBLOCK_RE.match(l)), None)
    if i is None:
        return None
    rows = 0
    for l in ls[i + 1:i + 80]:
        if l.startswith('#### ') or l.startswith('<!-- b55'):
            break
        if l.startswith('| :') and TROW_RE.search(l):
            rows += 1
    return dict(line=i + 1, terminal_rows=rows)


def latest(path):
    """### the document's newest version file at the pin: an edition by the form beside it, else the registry's file."""
    eds = editions(path)
    return eds[-1] if eds else path


def _vkey(p):
    m = re.search(r'_v(\d+(?:_\d+)*)\.md$', p)
    return tuple(int(x) for x in m.group(1).split('_')) if m else ()


def editions(path):
    if not path or not path.endswith('.md'):
        return []
    d, f = os.path.split(path)
    base = re.sub(r'_v\d+(?:_\d+)*$', '', f[:-3])
    pat = re.compile(r'^%s_v\d+(?:_\d+)*\.md$' % re.escape(base))
    out = [p for p in tracked() if os.path.dirname(p) == d and pat.match(os.path.basename(p)) and p != path]
    return sorted(out, key=_vkey)


def tier_of(path):
    """### (tier, source) by the read order of (R220)(3), read at the pin."""
    if not path or path not in tracked():
        return None, 'the file is not tracked at %s' % PRE_PP
    lp = latest(path)
    t = show(lp) or ''
    head = lines_of(t)[:20]
    for n, l in enumerate(head, 1):
        m = CLASS_RE.search(l)
        if m:
            v = m.group(1)
            if v == 'NOT PLACED':
                return 'NOT PLACED', '%s :%d, its class line' % (lp, n)
            return v.split()[1], '%s :%d, its class line' % (lp, n)
    ms = [(n, m) for n, l in enumerate(lines_of(t), 1) for m in SENT_RE.finditer(l)]
    if ms:
        n, m = ms[-1]
        return m.group(1), '%s :%d, its own tier sentence' % (lp, n)
    if path in RULED:
        return RULED[path][0], RULED[path][1]
    b = os.path.basename(path)
    if path.startswith('clusters/') and '_CLUSTER_SYNTHESIS' in b:
        return 'C', 'THE_DOCUMENT_CLASS_TAXONOMY :35, the cluster syntheses presumptive C, named by the standard'
    if path.startswith('clusters/') and b.endswith('_SIDE_CONSULT.md'):
        return 'N', 'THE_DOCUMENT_CLASS_TAXONOMY :36, the consults presumptive N, named by the standard'
    tb = tier_block(t)
    if tb and tb['terminal_rows']:
        return 'K', '%s :%d, a CP-1 tier block with %d terminal row(s) at T0-T2 (certification at a pin)' % (lp, tb['line'], tb['terminal_rows'])
    return None, 'NO TIER READ: no class line, no tier sentence, no ruled tier, no presumptive name, no tier block with a terminal row'


def certification(path):
    """### printed beside the tier: the cascade's tier block, the certification read, whatever the tier's source."""
    if not path or path not in tracked():
        return None
    return tier_block(show(latest(path)) or '')


KEYSTONE_TIERS = ('K', 'KC', 'C')


# ================================================================================ EDITION STATE
def edition_state(path, ot_lines):
    eds = editions(path)
    b = os.path.basename(path or '')
    base = re.sub(r'_v\d+(?:_\d+)*$', '', b[:-3]) if b.endswith('.md') else b
    wl = os.path.exists(os.path.join(ROOT, 'data', 'b558_editions', base + '.txt'))
    if eds:
        e = eds[-1]
        n = next((i + 1 for i, l in enumerate(ot_lines) if e in l), None)
        v = re.search(r'_v(\d+(?:_\d+)*)\.md$', e).group(1).replace('_', '.')
        return 'EDITED', 'v%s (`%s`, entered OPEN_TRAILS :%s)' % (v, e, n)
    if wl:
        return 'WORK-LIST', 'relay `data/b558_editions/%s.txt`, no edition' % base
    return 'NEITHER', '—'


# ================================================================================ THE SIEVE ROWS, BY SPIRAL_MAP §4A's MEMBERS
# ### each SPIRAL_MAP cluster's members as its refreshed table (b388) names them -- by REGISTRY ID or by file -- each token a needle the
# ### resolver finds in that row's own cells at the pin; the sieve's prefix for the cluster.
SPIRAL_CLUSTERS = [
    ('Methodology', 'MT', ['1.5h-1', '1.5h-4', '1.5h-6'], ['A_Place_to_Stand.md', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', 'THE_GLOBAL_SECTION.md']),
    ('Foundations', 'FD', ['1.5d-2', '1.5d-3', '1.5f-4', '1.5h-8', 'p2-4'], ['GAUGE_AND_INVARIANT.md', 'SILENCE_STAGES_DEALIGNMENT.md']),
    ('Simplicity / RH cascade', 'RH', ['1.5b-1', '1.5b-2', '1.5b-3', '1.5b-4', '1.5b-5', '1.5b-6', '1.5c-1', '1.5c-2', '1.5c-5', '1.5c-11', '1.5g-1',
                                      '1.5g-2', '1.5g-3', '1.5c-16', '1.5d-4'], ['THE_RESIDUE_OF_RH', 'R_CURVE_CRITERION.md', 'PATHS_TO_THE_CRITICAL_LINE.md']),
    ('Cubit / Trivium', 'CT', ['1.5e-1', '1.5e-2', '1.5e-3', '1.5e-4', '1.5e-5', '1.5e-6', 'p2-13', 'p2-17', 'p2-18', 'p2-23'], []),
    ('Matter / cosmology', 'MC', ['p2-8', 'p2-9', 'p2-10', 'p2-15', 'p2-25', 'p2-d1', 'p2-d2', 'p2-d3', 'p2-d4', 'p2-d5', 'p2-d6', 'p2-d7'],
     ['FANO_DERIVATION_OF_LAMBDA.md']),
    ('Philosophy / cognition / interfaces', '--', ['p2-2', 'p2-14', 'p2-21', 'p2-24', 'p2-28'], []),
    ('theory-space', '--', [], ['CONSTANCE.md', 'STRUCTURAL_FRACTION.md']),
    ('cross-domain', '--', [], ['FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md', 'INTERFACE_CONSERVATION.md']),
]
# ### a range the cell writes as `a`–`b` is expanded to its members, and its two ends are the needles
RANGES = {'1.5b-2': '1.5b-1', '1.5b-3': '1.5b-1', '1.5b-4': '1.5b-1', '1.5b-5': '1.5b-1', '1.5g-2': '1.5g-1', '1.5e-2': '1.5e-1', '1.5e-3': '1.5e-1',
          '1.5e-4': '1.5e-1', '1.5e-5': '1.5e-1', 'p2-d2': 'p2-d1', 'p2-d3': 'p2-d1', 'p2-d4': 'p2-d1', 'p2-d5': 'p2-d1', 'p2-d6': 'p2-d1',
          '1.5c-2': '1.5c-1/2/5', '1.5c-5': '1.5c-1/2/5', '1.5c-1': '1.5c-1/2/5', '1.5g-1': '1.5g-1/2/3', '1.5g-3': '1.5g-1/2/3'}
RANGES['1.5g-2'] = '1.5g-1/2/3'
REFRESH_HEAD = '**REFRESHED CLUSTER TABLE — 2026-09-09 (b388), under RULING (R17).**'


def spiral_rows(S=None):
    """### SPIRAL_MAP's refreshed cluster table at the pin: {cluster: (line, row text, its federation kernels)}."""
    S = S or lines_of(show(SPIRAL))
    h = next(i for i, l in enumerate(S) if l.startswith(REFRESH_HEAD))
    out = {}
    for i in range(h, h + 20):
        l = S[i]
        if not l.startswith('| **'):
            continue
        c = _cells(l)
        name = re.sub(r'\*\*', '', c[0]).replace(' (emergent)', '').strip()
        kern = sorted(set(re.findall(r'`(SIDE-[A-Za-z0-9-]+)`', c[3])))
        out[name] = (i + 1, l, kern)
    return out


def resolve_spiral(S=None):
    """### every member token found in its own cluster's row (a range by its ends): [(cluster, token, ok)]."""
    sr = spiral_rows(S)
    out = []
    for name, _p, ids, files in SPIRAL_CLUSTERS:
        row = sr.get(name, (0, '', []))[1]
        for t in ids:
            needle = RANGES.get(t, t)
            out.append((name, t, ('`%s`' % needle) in row))
        for f in files:
            out.append((name, f, f in row))
    return out


def sieve_counts():
    """### the sieve's v0.4 cluster headings: {prefix: rows}."""
    t = lines_of(show(SIEVE4))
    out = {}
    for name, p, _i, _f in SPIRAL_CLUSTERS:
        h = next((l for l in t if l.startswith('## %s — ' % name)), None)
        if h:
            out[p] = (int(re.search(r'— (\d+) rows?', h).group(1)), name, t.index(h) + 1)
    return out


def member_index(rows):
    """### REGISTRY ID or file basename -> census key."""
    ix = {}
    for r in rows:
        k = r['census']
        if r['id']:
            ix[r['id']] = k
        if r['path']:
            ix.setdefault(os.path.basename(r['path']), k)
            ix.setdefault(os.path.basename(r['path'])[:-3], k)
    return ix


def sieve_of(rows):
    """### {census key: [(spiral cluster, prefix, n rows, [members that link])]}"""
    ix = member_index(rows)
    sc = sieve_counts()
    out = {k: [] for k in KEYS}
    for name, p, ids, files in SPIRAL_CLUSTERS:
        by = {}
        for t in ids + files:
            k = ix.get(t)
            if k:
                by.setdefault(k, []).append(t)
        for k, ms in by.items():
            out[k].append((name, p, sc.get(p, (0,))[0], ms))
    return out


# ================================================================================ KERNELS
KER_RE = re.compile(r'\b(SIDE-[a-z0-9][a-z0-9-]*[a-z0-9])\b')
# ### prose tokens of the SIDE- shape that name no repository, each read in its row: "SIDE-method exploratory consult" (REGISTRY
# ### :326-:329), "Phase-66 SIDE-closure" (:213), the `SIDE-bsd-*` wildcard
NOT_REPO = {'SIDE-bsd', 'SIDE-door', 'SIDE-method', 'SIDE-closure'}


def kernels_named(text):
    return sorted(set(k for k in KER_RE.findall(text) if k not in NOT_REPO and not k.endswith('-')))


def kernels_of(rows, sieve, sr):
    """### {census key: {kernel: [sources]}} -- the kernels its REGISTRY rows name, the frozen Phase 1.2 table's for Phase 1.2
    ### (REGISTRY :713-:718), and the federation column of every SPIRAL cluster whose members it holds."""
    out = {k: {} for k in KEYS}
    for r in rows:
        for k in kernels_named(r['text']):
            out[r['census']].setdefault(k, []).append('REGISTRY :%d' % r['line'])
    R = registry()
    for i, l in enumerate(R, 1):
        if l.startswith('| 1.2-') or l.startswith('| ### **1.2-'):
            for k in kernels_named(l):
                out['P12'].setdefault(k, []).append('REGISTRY :%d (the frozen Phase 1.2 table)' % i)
    for ck, links in sieve.items():
        for name, _p, _n, _ms in links:
            ln, _t, kern = sr.get(name, (0, '', []))
            for k in kern:
                out[ck].setdefault(k, []).append('SPIRAL_MAP :%d (%s)' % (ln, name))
    return out


def remote_tags(repo):
    """### the remote's tags by ls-remote: the local clone's origin when D:/<repo> is a clone, else the org URL unauthenticated."""
    local = 'D:/' + repo
    if os.path.isdir(os.path.join(local, '.git')):
        r = subprocess.run(['git', '-C', local, 'ls-remote', '--tags', 'origin'], capture_output=True, timeout=60)
        via = 'origin of %s' % local
    else:
        r = subprocess.run(['git', 'ls-remote', '--tags', 'https://github.com/psinary-sketch/%s.git' % repo], capture_output=True, timeout=60,
                           env=dict(os.environ, GIT_TERMINAL_PROMPT='0'))
        via = 'https://github.com/psinary-sketch/%s.git, unauthenticated' % repo
    if r.returncode != 0:
        return dict(repo=repo, via=via, ok=False, err=r.stderr.decode('utf-8', 'replace').strip()[:160], tags={})
    tags = {}
    for l in r.stdout.decode('utf-8', 'replace').split(NL):
        if '\trefs/tags/' in l:
            sha, ref = l.split('\t', 1)
            name = ref[len('refs/tags/'):]
            if name.endswith('^{}'):
                tags.setdefault(name[:-3], {})['peeled'] = sha
            else:
                tags.setdefault(name, {})['obj'] = sha
    return dict(repo=repo, via=via, ok=True, err='', tags={k: v.get('peeled', v.get('obj')) for k, v in tags.items()})


def _tkey(t):
    nums = re.findall(r'\d+', t)
    return (1 if re.match(r'^v?\d', t) else 0, tuple(int(x) for x in nums), t)


def current_tag(rt):
    if not rt['tags']:
        return None
    return sorted(rt['tags'], key=_tkey)[-1]


def local_peel(repo, tag):
    local = 'D:/' + repo
    if not os.path.isdir(os.path.join(local, '.git')):
        return None
    r = subprocess.run(['git', '-C', local, 'rev-parse', tag + '^{}'], capture_output=True)
    return r.stdout.decode().strip() if r.returncode == 0 else ''


def local_only_tags(repo, rt):
    """### the clone's tags the remote does not carry, each with its peeled commit."""
    local = 'D:/' + repo
    if not os.path.isdir(os.path.join(local, '.git')) or not rt['ok']:
        return []
    out = []
    for t in sorted(x for x in g(local, 'tag', '-l').split(NL) if x.strip()):
        if t not in rt['tags']:
            out.append((t, (local_peel(repo, t) or '')[:7]))
    return out


# ================================================================================ DEPOSIT STATE
DEPOSIT_DIR = 'outputs/DEPOSITED-v1.1.2/'
DEPOSIT_RECORD = ('21539167', 'REGISTRY :77 and :419, the Day-1 record v1.1.2; its files at `outputs/DEPOSITED-v1.1.2/` (REGISTRY :83)')
KERNEL_DEPOSITS = {'SIDE-kernel': 'record 21520474 at v1.5 = 0e5233f (REGISTRY :97)',
                   'SIDE-lv-conservation': 'record 21539068 at v0.10.0 = 93c27ec (REGISTRY :102)',
                   'SIDE-t7-topology-cmb': 'the registered search, record 21436282 (REGISTRY :107)'}


def mirror_roster():
    t = show('tools/mirror_roster.json', STEPZERO, RELAY)
    return [p.replace('\\', '/') for p in json.loads(t)['files']]


def deposit_state(path, roster):
    if not path:
        return 'NEITHER', '—'
    b = os.path.basename(path)
    if path.startswith('day1/') and (DEPOSIT_DIR + b) in tracked():
        return 'DEPOSITED', 'record %s (`%s%s`)' % (DEPOSIT_RECORD[0], DEPOSIT_DIR, b)
    if path in roster:
        return 'MIRROR', 'the mirror roster (relay `tools/mirror_roster.json` slot %d)' % (roster.index(path) + 1)
    return 'NEITHER', '—'


# ================================================================================ THE SECOND READER'S ADDENDUM, (R220)(2)
ADD_RE = re.compile(r'(?=[^.]*\bEuler\b)(?=[^.]*(?:C₂|C_2|C2_euler|\bC2\b|enumerat|seven (?:mechanism )?classes|mechanism class))[^.]*'
                    r'\b(?:uses?|using|requires?|requiring|carr(?:y|ies|ied|ying))\b[^.]*')


def addendum_hits(path, cut=None):
    ls = lines_of(show(path))
    if cut:
        ls = ls[:cut]
    return [(i + 1, m.group(0).strip()) for i, l in enumerate(ls) for m in ADD_RE.finditer(l)]


# ================================================================================ THE BUILD
def build(read_remotes=False):
    R = registry()
    rows, refs = registry_rows(R)
    ot = lines_of(show('OPEN_TRAILS.md'))
    roster = mirror_roster()
    for r in rows:
        r['census'], r['why'] = place(r)
        r['tracked'] = bool(r['path']) and r['path'] in tracked()
        r['pointer'] = any('*moved*' in c for c in r['cells'][1:])
        r['tier'], r['tier_src'] = tier_of(r['path'])
        if r['pointer']:
            r['tier'], r['tier_src'] = None, 'a moved row: the document it points at is read on its own row (REGISTRY :%d)' % r['line']
            r['edition'] = ('MOVED', 'a moved row; its document`s edition is read on its own row')
            r['deposit'] = ('MOVED', 'a moved row; its document`s deposit state is read on its own row')
            r['cert'] = None
            continue
        r['cert'] = certification(r['path'])
        r['edition'] = edition_state(r['path'], ot) if r['tracked'] else ('NEITHER', 'the file the row names is not tracked at %s' % PRE_PP)
        r['deposit'] = deposit_state(r['path'], roster)
    sr = spiral_rows()
    sieve = sieve_of(rows)
    kern = kernels_of(rows, sieve, sr)
    remotes = {}
    if read_remotes:
        for k in sorted(set(x for v in kern.values() for x in v)):
            rt = remote_tags(k)
            ct = current_tag(rt) if rt['ok'] else None
            rt['current'] = ct
            rt['remote_peel'] = rt['tags'].get(ct) if ct else None
            rt['local_peel'] = local_peel(k, ct) if ct else None
            rt['local_only'] = local_only_tags(k, rt)
            remotes[k] = rt
    return dict(R=R, rows=rows, refs=refs, heads=heading_lines(R), sr=sr, sieve=sieve, kern=kern, remotes=remotes, sc=sieve_counts())


def keystone_less(B):
    out = []
    for k in KEYS:
        rs = [r for r in B['rows'] if r['census'] == k]
        if rs and not any(r['tier'] in KEYSTONE_TIERS for r in rs):
            out.append(k)
    return out


def main():
    B = build(read_remotes='--remotes' in sys.argv)
    rows = B['rows']
    print('### REGISTRY at %s: %d rows by the population rule ; %d title-layer references, not counted' % (PRE_PP, len(rows), len(B['refs'])))
    un = [r for r in rows if not r['census']]
    print('### unplaced: %d %s' % (len(un), [(r['line'], r['id'], r['path']) for r in un]))
    for k in KEYS:
        rs = [r for r in rows if r['census'] == k]
        ks = [(r['id'] or os.path.basename(r['path'] or '?'), r['tier']) for r in rs]
        print('%-5s %-48s heading :%-4s rows %2d  keystones %s' % (k, LABEL[k][:48], B['heads'][k], len(rs), [x for x in ks if x[1] in KEYSTONE_TIERS]))
        for r in rs:
            print('      :%-4d %-8s %-62s %-10s %-9s %-9s %s' % (r['line'], r['id'], (r['path'] or '')[:62], r['tier'], r['edition'][0], r['deposit'][0],
                                                          r['tier_src'][:90]))
        print('      sieve: %s' % [(n, p, c, ms) for n, p, c, ms in B['sieve'][k]])
        print('      kernels: %s' % sorted(B['kern'][k]))
    print('### keystone-less clusters: %s' % keystone_less(B))
    print('### spiral member needles: %s' % [x for x in resolve_spiral() if not x[2]] or 'ALL FOUND')
    print('### sieve counts: %s' % B['sc'])
    print('### title-layer references: %s' % [(r['line'], r['id']) for r in B['refs']])
    if B['remotes']:
        for k, rt in sorted(B['remotes'].items()):
            print('  %-40s %-6s current %-24s remote %s local %s  local-only %s %s' % (k, rt['ok'], rt.get('current'), (rt.get('remote_peel') or '')[:10],
                                                                   (rt.get('local_peel') or '')[:10], rt.get('local_only'), rt['err'][:60]))


if __name__ == '__main__':
    main()
