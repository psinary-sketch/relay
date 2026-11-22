# -*- coding: utf-8 -*-
"""tools/b766_registry_cells.py -- b766, (R376)(5)(a): THE REGISTRY'S ROWS READ FOR THE KEYSTONE SET. A reading and no build: no line of
REGISTRY, of the census or of a paper is written.

Carried from tools/b761_registry.py, its readers imported as committed (the document read at HEAD, its SUBJECT clause, its class line, its
headings, its newest tag, the identifiers and the protected word), and from tools/b755_census.py, its form (one mode that prints, one that
banks, each bank composed whole before it is written by a temporary file). Written by the Write tool at b766's Component 3 and committed
before its first run, dry included (N2).

  dry      the rows, the controls, the counts and the four lists printed; nothing written
  write    the same; where every control reads AS WANTED, data/b766_registry_cells.txt and .json

THE ROWS, at PLACE-papers HEAD (REGISTRY.md's working file equal to its bytes there): (i) EACH NUMBERED ROW ONCE: an id of b720's form in
a table row's first cell above b720's block (:1100), at its first row that is not a pointer row of b618's form (a cell opening
`REGISTRY.md:`), the lines of rule [Q] (3)'s section set aside; (ii) THE ROWS OF THE TABLES WHOSE ROWS CARRY NO NUMBER: the SUPPORT TIER,
INTERNAL, PHASE ROW and ANNEX tables, and the ratified public titles' rows whose id cell names no numbered row and whose document is no
numbered row's (the method layer's m5 rows among them); a public title's row naming a numbered row is that row's title and is not read
again. A row on a line rule [Q] protects (its section, and two lines either side of a line carrying the protected word, as the seat's
reader takes it) is counted and cited by its line and the line's sha256 alone, and not read. NOT REACHED by b720's block: a numbered row
the block does not name, or names as not yet read. A row's document: the first `.md` path its File cell names, at HEAD, or by its name where one tracked file carries that name; a
row outside the repository's tree (ANNEX) is named by its table and line alone.
THE PHASE BY SUBJECT ((R376)(5)(a)): the eight rows of Day 1, THE DAY 1 CLUSTER; 1.5a-1 to 1.5a-10 and 1.5g-1 to 1.5g-4, PHASE 1.2; the
other rows of 1.5A to 1.5G, PHASE 1.5; the rows of 1.5H and the rows under no phase heading, METHOD, PHASE 2 IN TIME; the rows of Phase 2,
PHASE 2; the support, internal and annex tables as they are headed. THE TABLE FILED UNDER: the heading above the row's first line, read as
the Day 1 table, a Phase 1.5 table (1.5A to 1.5H, or an addition naming Phase 1.5), a Phase 2 table (2A to 2G, or an addition naming Phase
2), SUPPORT, INTERNAL, ANNEX, or no phase heading; a row DIFFERS where its phase by subject is not the table's, a row of METHOD under no
phase heading not counted as differing.
THE KEYSTONE CELL, its clauses read in this order: APPARATUS for the canon, the taxonomy, the census, the six cluster syntheses of May and
CATALOGOS (by their files); WITHDRAWN OR SUPERSEDED where the row's Status cell says so; KEYSTONE where the document's head (before its first
'## ') declares Tier K or Tier KC on its document-class line, or the row is one of Day 1's eight, or is 1.5c-24, 1.5g-4, 1.5h-7 or 1.5h-9;
CLUSTER SYNTHESIS where it declares Tier C; SOURCE, NAMED IN <n> ROWS where a keystone of its cluster names it in its Correspondence table
or its table of papers (a table row under a heading carrying "Correspondence", or a row of a table whose header names papers, carrying the
row's id or its file's name); SOURCE, NOT NAMED where none does; UNPLACED for the rest. ITS CLUSTER: Day 1; the id's group 1.5a to 1.5h;
for a Phase 2 row the table 2A to 2G its first row stands under; a row of no such group has no cluster and reads UNPLACED where no earlier
clause takes it.
THE SUBJECT AND TO KC CELLS, in b761's form where the row has none: a row whose cells b761's block (:1265) or b720's block (:1100) holds,
read there and not "not yet read", is cited to that block's line; for the rest, b761's SUBJECT (its PURPOSE line, its abstract's first
sentence, or its opening's) and TO KC (the class line, the four headings, the newest kernel tag, the candidate word by b720's rule).
THE TITLE LINE: the document's first '# ' line in its first twenty; THE TITLE FLAG: a numeral, an ordinal or a number word in it, each
token printed; no title changed.
GUARDS: a line of day1/ONE_PAGE_PROOF.md or day1/ONE_PAGE_PROOF_v2_0.md at :3 is cited by line and digest alone; a text carrying the
protected word or an identifier is cited by line and digest alone; day1/Which_Structure_Confines_v2_5_0.md is never opened.
CONTROLS ((R376)(5)(a)): the eight rows of Day 1 read KEYSTONE; the canon reads APPARATUS; 1.5a-1 reads SOURCE, named by 1.5a-9; a planted
row reads UNPLACED. Beside them: the six cluster syntheses of May read; the identifiers, the protected word, a host folder and the two :3
lines 0 in the bank.

No PLACE-papers line is printed but the title lines and the clauses this tool composes; the protected word is never printed or stored; no
git write.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b761_registry as R61   # noqa: E402  ### b761's readers as committed

ACT, NL = 'b766', '\n'
PP = R61.PP
BANK = os.path.join(D, 'b766_registry_cells.txt')
BJSON = os.path.join(D, 'b766_registry_cells.json')
NAV_52 = 52   # ### (R376)(5)(a): the navigator's count of the numbered rows b720's block does not reach, printed as the navigator's
ONEPAGE = ('day1/ONE_PAGE_PROOF.md', 'day1/ONE_PAGE_PROOF_v2_0.md')
NEVER = ('day1/Which_Structure_Confines_v2_5_0.md',)
NAMED_KEYSTONES = ('1.5c-24', '1.5g-4', '1.5h-7', '1.5h-9')
P12 = set(['1.5a-%d' % i for i in range(1, 11)] + ['1.5g-%d' % i for i in range(1, 5)])
DAY1, P1_2, P1_5, METHOD, P2 = 'THE DAY 1 CLUSTER', 'PHASE 1.2', 'PHASE 1.5', 'METHOD, PHASE 2 IN TIME', 'PHASE 2'
SUP, INTL, ANX, NOPH = 'SUPPORT', 'INTERNAL', 'ANNEX', 'NO PHASE HEADING'
APP, WS, KEY, CS, SN, SNN, UNP = 'APPARATUS', 'WITHDRAWN OR SUPERSEDED', 'KEYSTONE', 'CLUSTER SYNTHESIS', 'SOURCE, NAMED', 'SOURCE, NOT NAMED', 'UNPLACED'
TIER = re.compile(r'DOCUMENT CLASS.*?\bTIER\s+(KC|K|C|N|E)\b')
NUMW = set(('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen '
            'nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion').split())
ORDW = set(('first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth twentieth hundredth '
            'thousandth').split())
UNNUM = (('## SUPPORT TIER', SUP), ('## INTERNAL', INTL), ('## PHASE ROW', NOPH), ('## ANNEX', ANX))
TITLES = '## RATIFIED PUBLIC TITLES'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(s):
    return hashlib.sha256(s.encode('utf-8') if isinstance(s, str) else s).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def q_section(L):
    """rule [Q] (3)'s section: its heading (found by digest at R61.QLINE) to the next heading of its level or higher."""
    lv = len(re.match(r'^(#+)', L[R61.QLINE - 1]).group(1))
    end = len(L)
    for k in range(R61.QLINE, len(L)):
        m = re.match(r'^(#+)\s', L[k])
        if m and len(m.group(1)) <= lv:
            end = k
            break
    return set(range(R61.QLINE, end + 1))


def heading_of(L):
    h, cur = {}, (0, '')
    for k, l in enumerate(L, 1):
        if re.match(r'^#+\s', l):
            cur = (k, l)
        h[k] = cur
    return h


def table_of(L, k):
    """the table holding line k: its first line and its header's cells."""
    a = k
    while a > 1 and L[a - 2].startswith('|'):
        a -= 1
    return a, [x.strip() for x in L[a - 1].split('|')]


def filed(h):
    if re.match(r'^##\s+DAY 1\b', h):
        return DAY1
    if re.match(r'^###\s+1\.5[A-H]:', h) or re.search(r'\(Phase 1\.5', h):
        return P1_5
    if re.match(r'^###\s+2[A-G]:', h) or re.search(r'\(Phase 2', h):
        return P2
    for pre, ph in UNNUM:
        if h.startswith(pre) and ph != NOPH:
            return ph
    return NOPH


def phase(rid, table_phase):
    if rid.startswith('d1-'):
        return DAY1
    if rid in P12:
        return P1_2
    if re.match(r'^1\.5[a-g]-', rid):
        return P1_5
    if rid.startswith('1.5h-'):
        return METHOD
    if rid.startswith('p2-'):
        return P2
    return table_phase if table_phase in (SUP, INTL, ANX) else METHOD


def cluster(rid, h):
    if rid.startswith('d1-'):
        return 'd1'
    m = re.match(r'^(1\.5[a-h])-', rid)
    if m:
        return m.group(1)
    if rid.startswith('p2-'):
        mm = re.match(r'^###\s+(2[A-G]):', h) or re.search(r'\(Phase (2[A-G])\b', h)
        return mm.group(1) if mm else None
    return None


def resolve(cell, tracked):
    m = re.search(r'`([^`]+?\.md)`', cell)
    if not m:
        return None, 'no document'
    p = m.group(1).strip()
    if p in NEVER:
        return p, 'NOT OPENED'
    if p in tracked:
        return p, 'AT HEAD'
    base = p.split('/')[-1]
    hits = [t for t in tracked if t.split('/')[-1] == base]
    if len(hits) == 1 and hits[0] not in NEVER:
        return hits[0], 'AT HEAD BY ITS NAME'
    return p, 'ABSENT' if not hits else 'ITS NAME ON %d FILES' % len(hits)


def apparatus(p):
    b = (p or '').split('/')[-1]
    return bool(p) and (p.endswith('THE_METHOD_CANON.md') or p.endswith('THE_DOCUMENT_CLASS_TAXONOMY.md') or b.startswith('THE_KEYSTONE_CENSUS')
                        or (p.startswith('clusters/') and '_CLUSTER_SYNTHESIS_2026-05-' in p) or 'CATALOGOS' in b)


def flag(title):
    toks = [m.group(0) for m in re.finditer(r'\d+(?:st|nd|rd|th)?', title)]
    toks += [w for w in re.findall(r'[A-Za-z]+', title) if w.lower() in NUMW or w.lower() in ORDW]
    toks += [m.group(0) for m in re.finditer(r'\b[IVX]{2,}\b', title)]
    return toks


def naming_rows(Dl):
    """the rows of the keystone's Correspondence tables and of its tables of papers, as (line, text)."""
    rows = set()
    for k, l in enumerate(Dl):
        m = re.match(r'^(#+)\s', l)
        if m and re.search(r'(?i)correspondence', l):
            lv, j = len(m.group(1)), k + 1
            while j < len(Dl):
                mj = re.match(r'^(#+)\s', Dl[j])
                if mj and len(mj.group(1)) <= lv:
                    break
                if Dl[j].startswith('|') and not re.match(r'^\|[\s:|-]+\|?\s*$', Dl[j]):
                    rows.add((j + 1, Dl[j]))
                j += 1
    k = 0
    while k < len(Dl):
        if Dl[k].startswith('|'):
            j = k
            while j < len(Dl) and Dl[j].startswith('|'):
                j += 1
            if re.search(r'(?i)\bpapers?\b', Dl[k]):
                rows.update((i + 1, Dl[i]) for i in range(k + 2, j))
            k = j
        else:
            k += 1
    return sorted(rows)


def names_it(text, rid, path):
    if rid and re.search(r'(?<![0-9A-Za-z.])' + re.escape(rid) + r'(?![0-9A-Za-z])', text):
        return True
    if path:
        stem = path.split('/')[-1][:-3]
        if len(stem) >= 6 and re.search(r'(?<![A-Za-z0-9_])' + re.escape(stem) + r'(?![A-Za-z0-9_])', text):
            return True
    return False


# ================================================================================ THE ROWS
def collect(L, Q, P, H, tracked):
    b720 = [k for k, l in enumerate(L, 1) if l.startswith('## SUBJECT / TO-KC ATTRIBUTE')]
    b761 = [k for k, l in enumerate(L, 1) if l.startswith('## SUBJECT / TO-KC CELLS OF PHASE 1.5')]
    if len(b720) != 1 or len(b761) != 1:
        die('b720`S OR b761`S BLOCK NOT READ ONCE (%s, %s)' % (b720, b761))
    stop = b720[0]
    rows, seen, prot = [], set(), []
    for k, l in enumerate(L[:stop - 1], 1):
        m = R61.ROW_ID.match(l)
        if not m:
            continue
        c = [x.strip() for x in l.split('|')]
        if any(x.startswith('`REGISTRY.md:') for x in c[2:4]) or m.group(1) in seen:
            continue
        rid = m.group(1)
        seen.add(rid)
        if k in P:
            prot.append((k, sha(l)[:16], 'a numbered row'))
            continue
        a, hdr = table_of(L, k)
        si = next((i for i, x in enumerate(hdr) if x.lower() == 'status'), None)
        fi = next((i for i, x in enumerate(hdr) if x.lower() == 'file'), 3)
        hk, hl = H[k]
        fc = c[fi] if fi < len(c) and '.md`' in c[fi] else next((x for x in c[2:5] if '.md`' in x), '')
        path, where = resolve(fc, tracked)
        rows.append(dict(id=rid, line=k, table=a, head=hk, htext=hl, filed=filed(hl), cluster=cluster(rid, hl), path=path, where=where,
                         status=(c[si] if si is not None and si < len(c) else ''), numbered=True))
    docs = set(r['path'] for r in rows if r['path'])
    skipped = []
    for pre, ph in UNNUM:
        hs = [k for k, l in enumerate(L[:stop - 1], 1) if l.startswith(pre) and k not in Q]
        if len(hs) != 1:
            die('THE TABLE HEADED %s NOT READ ONCE (%s)' % (pre, hs))
        k = hs[0] + 1
        while k <= len(L) and not L[k - 1].startswith('|') and not re.match(r'^#+\s', L[k - 1]):
            k += 1
        a = k
        while k <= len(L) and L[k - 1].startswith('|'):
            k += 1
        hdr = [x.strip() for x in L[a - 1].split('|')]
        fi = next((i for i, x in enumerate(hdr) if 'file' in x.lower()), 1)
        for i in range(a + 2, k):
            c = [x.strip() for x in L[i - 1].split('|')]
            if i in P:
                prot.append((i, sha(L[i - 1])[:16], 'a row of the table headed %s' % pre[3:].split(':')[0].split(' —')[0].strip()))
                continue
            if ph == ANX:
                path, where = None, 'OUTSIDE THE TREE, NOT READ'
            else:
                path, where = resolve(c[fi] if fi < len(c) else '', tracked)
            rows.append(dict(id='%s :%d' % (pre[3:].split(':')[0].split(' —')[0].strip(), i), line=i, table=a, head=hs[0], htext=L[hs[0] - 1],
                             filed=ph, cluster=None, path=path, where=where, status='', numbered=False))
    th = [k for k, l in enumerate(L[:stop - 1], 1) if l.startswith(TITLES)]
    if len(th) != 1:
        die('THE RATIFIED PUBLIC TITLES NOT READ ONCE (%s)' % th)
    tend = next((k for k in range(th[0] + 1, stop) if re.match(r'^##\s', L[k - 1])), stop)
    for i in range(th[0] + 1, tend):
        l = L[i - 1]
        if not l.startswith('|') or re.match(r'^\|[\s:|-]+\|?\s*$', l):
            continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 3 or not re.search(r'`[^`]+?\.md`', c[1]):
            continue
        if i in P:
            prot.append((i, sha(l)[:16], 'a row of the public titles'))
            continue
        idc = c[2].strip('`* ')
        path, where = resolve(c[1], tracked)
        if idc in seen or (path in docs):
            skipped.append(i)
            continue
        rid = idc if re.match(r'^m\d+-\d+$', idc) else 'PUBLIC TITLES :%d' % i
        rows.append(dict(id=rid, line=i, table=table_of(L, i)[0], head=th[0], htext=L[th[0] - 1], filed=NOPH, cluster=None, path=path,
                         where=where, status='', numbered=False))
    return rows, dict(stop=stop, b761=b761[0], skipped=skipped, prot=prot)


def block_cells(L, Q, start, end):
    """the rows of a SUBJECT / TO-KC block: id -> its line, where the row is read (not `not yet read`)."""
    out = {}
    for k in range(start, end + 1):
        if k in Q:
            continue
        m = re.match(r'^\| (?:### \*\*)?`([^`]+)`', L[k - 1])
        if m and not R61.NYR.match(L[k - 1]):
            out.setdefault(m.group(1), k)
    return out


def subject_tokc(d, path, I, qw):
    """b761's two cells for a document read (tools/b761_registry.py cells(), its parts as committed there)."""
    if not d['k']:
        subj = 'no %s sentence read' % d['src']
    else:
        cl_, cut = R61.clause_of(d['line'])
        j2 = next((x for x in range(d['k'], d['j'] + 1) if cl_ in R61.span_text(d['D'], d['k'], x)), d['j'])
        where = '%s :%d' % (d['src'], d['k']) + ('-:%d' % j2 if j2 > d['k'] else '')
        if qw.lower() in cl_.lower() or R61.idcount(cl_, I) or (path in ONEPAGE and d['k'] <= 3 <= j2):
            subj = 'its %s line cited by line and digest alone: :%d (sha256 %s)' % (d['src'], d['k'], sha(d['D'][d['k'] - 1])[:16])
        else:
            subj = '"%s%s" (%s)' % (cl_, ' ...' if cut else '', where)
    parts = ['class %s (:%d)' % (d['cls'][1], d['cls'][0]) if d['cls'] else 'no class line']
    parts.append('; '.join('%s %s' % (n, ', '.join(':%d' % x for x in ks[:4]) + (' and %d more' % (len(ks) - 4) if len(ks) > 4 else ''))
                           for n, ks in d['heads']) if d['heads'] else 'none of Correspondence, Glossary, References or Bibliography, Errata')
    parts.append('SIDE-explicit-formula `%s` %s (:%d)' % (d['tag'][0], d['tag'][2], d['tag'][3]) if d['tag'] else 'names no tag')
    tier = d['cls'][1] if d['cls'] else ''
    if re.fullmatch(r'TIER (K|C)', tier) or d['kc']:
        parts.append('candidate (%s)' % ('Tier %s declared' % tier[-1] if tier else 'names itself a keystone candidate, :%d' % d['kc'][0]))
    else:
        parts.append('not a candidate by b720`s rule')
    return subj, ' / '.join(parts)


def read_rows(rows, L, Q, I, qw, TG, info):
    c720 = block_cells(L, Q, info['stop'], info['b761'] - 1)
    c761 = block_cells(L, Q, info['b761'], len(L))
    for r in rows:
        r.update(tier=None, tier_line=None, title=None, title_line=None, title_cite=None, flag=[], subject=None, tokc=None, kdoc=None)
        r['sw'] = bool(re.search(r'\b(SUPERSEDED|WITHDRAWN)\b', r['status'].upper()))
        if r['path'] and r['where'].startswith('AT HEAD'):
            d = R61.read_doc(r['path'], I, qw, TG)
            if d is not None:
                Dl = d['D']
                h2 = next((k for k, l in enumerate(Dl, 1) if l.startswith('## ')), len(Dl) + 1)
                tl = [(k, m.group(1)) for k, l in enumerate(Dl[:h2 - 1], 1) for m in [TIER.search(l)] if m]
                if tl:
                    r['tier_line'], r['tier'] = tl[0]
                ti = next((k for k, l in enumerate(Dl[:20], 1) if l.lstrip('﻿').startswith('# ')), None)   # ### a byte-order mark read past
                if ti:
                    t = R61.plain(Dl[ti - 1].lstrip('﻿').lstrip('#').strip())
                    r['title_line'] = ti
                    r['flag'] = flag(t)
                    if (r['path'] in ONEPAGE and ti == 3) or qw.lower() in t.lower() or R61.idcount(t, I):
                        r['title_cite'] = 'cited by line and digest alone: :%d (sha256 %s)' % (ti, sha(Dl[ti - 1])[:16])
                    else:
                        r['title'] = t
                if r['id'] in c761:
                    r['subject'] = r['tokc'] = 'in b761`s block (REGISTRY :%d)' % c761[r['id']]
                elif r['id'] in c720:
                    r['subject'] = r['tokc'] = 'in b720`s block (REGISTRY :%d)' % c720[r['id']]
                else:
                    r['subject'], r['tokc'] = subject_tokc(d, r['path'], I, qw)
                r['kdoc'] = Dl
        if r['subject'] is None:
            r['subject'] = r['tokc'] = 'no text read (%s)' % r['where']
    return rows


def classify(rows):
    for r in rows:
        if apparatus(r['path']):
            r['cell'] = APP
        elif r['sw']:
            r['cell'] = WS
        elif r['tier'] in ('K', 'KC') or r['id'].startswith('d1-') or r['id'] in NAMED_KEYSTONES:
            r['cell'] = KEY
        elif r['tier'] == 'C':
            r['cell'] = CS
        else:
            r['cell'] = None
    ks = {}
    for r in rows:
        if r['cell'] == KEY and r['cluster']:
            ks.setdefault(r['cluster'], []).append(r)
    for r in rows:
        if r['cell'] is not None:
            continue
        if not r['cluster']:
            r['cell'], r['named'] = UNP, []
            continue
        named = []
        for k in ks.get(r['cluster'], []):
            if k['id'] == r['id'] or not k['kdoc']:
                continue
            for ln, text in naming_rows(k['kdoc']):
                if names_it(text, r['id'], r['path']):
                    named.append((k['id'], ln))
        r['named'] = named
        r['cell'] = SN if named else SNN
        r['ks_in_cluster'] = len(ks.get(r['cluster'], []))
    return rows, ks


def cell_text(r):
    if r['cell'] == SN:
        by = {}
        for kid, ln in r['named']:
            by.setdefault(kid, []).append(ln)
        return 'SOURCE, NAMED IN %d ROWS (%s)' % (len(r['named']), '; '.join('by %s at :%s' % (k, ', :'.join(str(x) for x in v[:4])) for k, v in by.items()))
    if r['cell'] == SNN:
        return 'SOURCE, NOT NAMED (its cluster %s, keystones in it %d)' % (r['cluster'], r.get('ks_in_cluster', 0))
    return r['cell']


# ================================================================================ THE RUN
def run(mode):
    base = R61.at_head()
    L = base.split(NL)[:-1]
    qw = R61.qword(L)
    I = R61.ids()
    TG = R61.tags()
    Q = q_section(L)
    WL = [k for k, l in enumerate(L, 1) if re.search(r'\b%s\b' % re.escape(qw), l, re.I)]
    P = Q | set(x for w in WL for x in range(max(1, w - 2), min(len(L), w + 2) + 1))   # ### rule [Q] as the seat's reader takes it
    H = heading_of(L)
    out, _rc = R61.git(PP, 'ls-tree', '-r', '--name-only', 'HEAD')
    tracked = set(x for x in out.split(NL) if x)
    head = R61.git(PP, 'rev-parse', '--short=8', 'HEAD')[0].strip()
    rows, info = collect(L, Q, P, H, tracked)
    rows = read_rows(rows, L, P, I, qw, TG, info)
    rows, ks = classify(rows)
    for r in rows:
        r['phase'] = phase(r['id'], r['filed']) if r['numbered'] else (r['filed'] if r['filed'] in (SUP, INTL, ANX) else METHOD)
        r['differs'] = r['phase'] != r['filed'] and not (r['filed'] == NOPH and r['phase'] == METHOD)
    num = [r for r in rows if r['numbered']]
    c720 = block_cells(L, P, info['stop'], info['b761'] - 1)
    c720_any = set(m.group(1) for k in range(info['stop'], info['b761']) if k not in P
                   for m in [re.match(r'^\| (?:### \*\*)?`([^`]+)`', L[k - 1])] if m)
    not720 = [r['id'] for r in num if r['id'] not in c720_any]
    nyr720 = [r['id'] for r in num if r['id'] in c720_any and r['id'] not in c720]
    c761 = block_cells(L, P, info['b761'], len(L))
    neither = [x for x in not720 + nyr720 if x not in c761]
    prot = info['prot']
    prot_num = [k for k, _d, w in prot if w == 'a numbered row' and k not in Q]
    scoped = [(r['id'], 'SCOPE-DROPPED' if re.search(r'(?i)scope-drop', r['status']) else 'RECLASSIFIED', cell_text(r)) for r in rows
              if not r['sw'] and re.search(r'(?i)scope-drop|reclassified', r['status'])]
    # ### THE CONTROLS
    d1 = [r for r in rows if r['id'].startswith('d1-')]
    canon = [r for r in rows if (r['path'] or '').endswith('THE_METHOD_CANON.md')]
    a1 = [r for r in rows if r['id'] == '1.5a-1']
    planted = dict(id='zz-99', numbered=True, path=None, sw=False, tier=None, cluster=None, kdoc=None, status='', where='planted')
    pr, _pk = classify([planted])
    may = [r for r in rows if (r['path'] or '').startswith('clusters/') and '_CLUSTER_SYNTHESIS_2026-05-' in (r['path'] or '')]
    tables = sorted(set(r['table'] for r in rows))
    counts = {}
    for r in rows:
        counts[r['cell']] = counts.get(r['cell'], 0) + 1
    kp = {}
    for r in rows:
        if r['cell'] == KEY:
            kp.setdefault(r['phase'], []).append(r['id'])
    differs = [r for r in rows if r['differs']]
    unplaced = [r for r in rows if r['cell'] == UNP]
    flagged = [r for r in rows if r['flag']]
    P = ['%s -- (R376)(5)(a): THE REGISTRY`S ROWS READ FOR THE KEYSTONE SET (%s)' % (ACT, utc()), '',
         '### tools/b766_registry_cells.py %s; PLACE-papers HEAD %s, REGISTRY.md %d lines; the kernel clone`s tags %d (the newest %s); a reading:' % (
             mode, head, len(L), len(TG), TG[-1][0]),
         '### no line of REGISTRY, of the census or of a paper written; each title line and clause composed here from the document at HEAD; the',
         '### protected word neither printed nor stored. One row a registry row: its id or its table and line | its document | its title line |',
         '### THE PHASE BY SUBJECT | the table filed under | SUBJECT | TO KC | THE KEYSTONE CELL | THE TITLE FLAG.', '',
         '## THE ROWS READ: numbered %d ; of the tables whose rows carry no number %d ; %d rows of %d tables ; the public titles` rows naming a '
         'numbered row, not read again, %d ; on a line rule [Q] protects, cited by line and digest alone and not read, %d (below)' % (
             len(num), len(rows) - len(num), len(rows), len(tables), len(info['skipped']), len(prot)),
         '## b720`S BLOCK (:%d) AND THE NUMBERED ROWS READ: it reads %d of the %d, names %d as not yet read and does not name %d: NOT REACHED %d ; '
         'the navigator`s count of the rows it does not reach %d, printed as the navigator`s' % (
             info['stop'], len(num) - len(not720) - len(nyr720), len(num), len(nyr720), len(not720), len(nyr720) + len(not720), NAV_52),
         '  named as not yet read: %s' % (', '.join(nyr720) or 'none'),
         '  not named: %s' % (', '.join(not720) or 'none'),
         '  of the %d not reached, read by b761`s block (:%d) %d, by neither %d; with the %d numbered rows on protected lines outside rule [Q]`s '
         'section (:%s), by neither %d, beside the navigator`s %d: %s' % (
             len(not720) + len(nyr720), info['b761'], len(not720) + len(nyr720) - len(neither), len(neither), len(prot_num),
             ', :'.join(str(k) for k in prot_num) or '-', len(neither) + len(prot_num), NAV_52,
             'EQUAL' if len(neither) + len(prot_num) == NAV_52 else 'DIFFERING'),
         '  by neither block: %s' % (', '.join(neither) or 'none'),
         '## THE ROWS ON A LINE RULE [Q] PROTECTS (its section from :%d, and two lines either side of a line carrying the word, as the seat`s '
         'reader takes it), each by its line and the line`s sha256 alone: %s' % (
             R61.QLINE, '; '.join(':%d %s (%s)' % (k, d, w) for k, d, w in prot) or 'none'), '']
    for r in rows:
        P.append('  %s | %s | %s | %s | filed under %s (:%d) | SUBJECT %s | TO KC %s | %s | %s' % (
            r['id'], ('%s (%s)' % (r['path'], r['where'])) if r['path'] else r['where'],
            ('title "%s" (:%d)' % (r['title'], r['title_line'])) if r['title'] else ('title %s' % r['title_cite'] if r['title_cite'] else 'no title line read'),
            r['phase'], r['filed'], r['head'], r['subject'], r['tokc'], cell_text(r) + (' (Tier %s at :%d)' % (r['tier'], r['tier_line']) if r['tier'] else ''),
            ('flag %s' % ', '.join(r['flag'])) if r['flag'] else 'no flag'))
    P += ['', '## THE COUNTS',
          '  by the keystone cell: %s' % ' ; '.join('%s %d' % (c, counts.get(c, 0)) for c in (KEY, CS, APP, SN, SNN, WS, UNP)),
          '  the keystones by phase: %s' % ' ; '.join('%s %d' % (p, len(kp.get(p, []))) for p in (DAY1, P1_2, P1_5, METHOD, P2, SUP, INTL, ANX)),
          '  the keystone rows` documents: %d distinct of %d rows%s' % (
              len(set(r['path'] for r in rows if r['cell'] == KEY)), counts.get(KEY, 0),
              ''.join(' ; %s under %s' % (p_, ', '.join(r['id'] for r in rows if r['cell'] == KEY and r['path'] == p_))
                      for p_ in sorted(set(r['path'] for r in rows if r['cell'] == KEY and r['path']))
                      if sum(1 for r in rows if r['cell'] == KEY and r['path'] == p_) > 1)),
          '  the four rows (R376)(5)(a) names KEYSTONE read: %s' % ' ; '.join('%s %s' % (r['id'], cell_text(r)) for r in rows if r['id'] in NAMED_KEYSTONES),
          '  the keystones` clusters: %s' % ' ; '.join('%s %d (%s)' % (c, len(v), ', '.join(x['id'] for x in v)) for c, v in sorted(ks.items())), '',
          '## THE FOUR LISTS, FOR THE AUTHOR`S STRIKE AT THE ROOT',
          '  (1) THE KEYSTONES BY PHASE: %s' % ' ; '.join('%s: %s' % (p, ', '.join(kp.get(p, [])) or 'none') for p in (DAY1, P1_2, P1_5, METHOD, P2, SUP, INTL, ANX)),
          '  (2) THE ROWS WHOSE PHASE BY SUBJECT DIFFERS FROM THE TABLE FILED UNDER (%d): %s' % (
              len(differs), '; '.join('%s %s under %s' % (r['id'], r['phase'], r['filed']) for r in differs)),
          '  (3) THE ROWS READING UNPLACED (%d): %s' % (len(unplaced), ', '.join(r['id'] for r in unplaced)),
          '  (4) THE ROWS CARRYING A TITLE FLAG (%d): %s' % (len(flagged), '; '.join('%s (%s)' % (r['id'], ', '.join(r['flag'])) for r in flagged)),
          '  BESIDE THEM, THE ROWS WHOSE STATUS READS SCOPE-DROPPED OR RECLASSIFIED, not WITHDRAWN OR SUPERSEDED by the rule`s words (%d): %s' % (
              len(scoped), '; '.join('%s %s, read %s' % x for x in scoped) or 'none'), '']
    ctl = [('the eight rows of Day 1 read KEYSTONE: %d rows, %s' % (len(d1), [(r['id'], r['cell']) for r in d1]),
            len(d1) == 8 and all(r['cell'] == KEY for r in d1)),
           ('the canon reads APPARATUS: %s' % [(r['id'], r['cell']) for r in canon], len(canon) == 1 and canon[0]['cell'] == APP),
           ('1.5a-1 reads SOURCE, named by 1.5a-9: %s' % [(r['cell'], r.get('named', [])[:3]) for r in a1],
            len(a1) == 1 and a1[0]['cell'] == SN and any(k == '1.5a-9' for k, _ln in a1[0]['named'])),
           ('a planted row (zz-99, no document, no cluster) reads UNPLACED: %s' % pr[0]['cell'], pr[0]['cell'] == UNP),
           ('the six cluster syntheses of May read APPARATUS: %d' % len(may), len(may) == 6 and all(r['cell'] == APP for r in may))]
    text = NL.join(P)
    lines3 = []
    for op in ONEPAGE:
        raw, rc = R61.git(PP, 'show', 'HEAD:' + op)
        if not rc and raw:
            l3 = raw.replace('\r', '').split(NL)[2:3]
            if l3 and l3[0].strip():
                lines3.append(l3[0].strip())
    host = os.path.basename(os.path.dirname(R61.PP.rstrip('/')))   # ### the host folder read from b761's constant, never written here
    bad = R61.idcount(text, I) + (1 if qw.lower() in text.lower() else 0) + sum(text.count(x) for x in (host, 'Users\\', 'Users/', ':\\'))
    ctl.append(('the identifiers, the protected word, a host folder and the two :3 lines 0 in the bank (%d ; the :3 lines read %d, present %d)' % (
        bad, len(lines3), sum(1 for x in lines3 if x in text)), bad == 0 and not any(x in text for x in lines3)))
    ok = all(o for _w, o in ctl)
    P += ['## THE CONTROLS'] + ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    sentence = ('%d rows of %d tables (relay data/b766_registry_cells.txt); KEYSTONE %d, CLUSTER SYNTHESIS %d, APPARATUS %d, SOURCE NAMED %d, '
                'SOURCE NOT NAMED %d, WITHDRAWN OR SUPERSEDED %d, UNPLACED %d; the keystones by phase: the Day 1 cluster %d, Phase 1.2 %d, Phase 1.5 %d, '
                'method %d, Phase 2 %d; %d rows filed under a table other than their phase by subject; %d titles flagged') % (
        len(rows), len(tables), counts.get(KEY, 0), counts.get(CS, 0), counts.get(APP, 0), counts.get(SN, 0), counts.get(SNN, 0), counts.get(WS, 0),
        counts.get(UNP, 0), len(kp.get(DAY1, [])), len(kp.get(P1_2, [])), len(kp.get(P1_5, [])), len(kp.get(METHOD, [])), len(kp.get(P2, [])),
        len(differs), len(flagged))
    P += ['', '## [X1]`S FIELDS: %s' % sentence, '',
          '### ### **THE REGISTRY`S ROWS: %d ROWS OF %d TABLES READ ; KEYSTONE %d ; UNPLACED %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(rows), len(tables), counts.get(KEY, 0), counts.get(UNP, 0), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD, NOTHING WRITTEN')]
    final = NL.join(P) + NL
    if R61.idcount(final, I) or qw.lower() in final.lower():
        die('AN IDENTIFIER OR THE PROTECTED WORD IN THE PRINT')
    print(final, end='')
    if mode != 'write' or not ok:
        return 0 if ok else 1
    J = dict(at=utc(), act=ACT, pp_head=head, registry_lines=len(L), rows=len(rows), tables=len(tables), numbered=len(num), not_in_b720=not720,
             not_yet_read_in_b720=nyr720, not_reached=len(not720) + len(nyr720), by_neither_block=neither, nav_52=NAV_52, protected=[[k, d, w] for k, d, w in prot],
             scoped=[list(x) for x in scoped], counts=counts, keystones_by_phase=kp, differs=[[r['id'], r['phase'], r['filed']] for r in differs],
             unplaced=[r['id'] for r in unplaced], flagged=[[r['id'], r['flag']] for r in flagged], sentence=sentence,
             controls=[[w, o] for w, o in ctl],
             cells=[dict(id=r['id'], line=r['line'], path=r['path'], where=r['where'], phase=r['phase'], filed=r['filed'], cell=r['cell'],
                         tier=r['tier'], named=r.get('named', []), flag=r['flag']) for r in rows])
    put(BANK, final)
    put(BJSON, json.dumps(J, ensure_ascii=False, indent=1) + NL)
    print('written data/b766_registry_cells.txt (%d lines) and .json' % len(final.split(NL)))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write']):
        sys.exit(__doc__)
    sys.exit(run(a[0]))
