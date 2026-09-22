# -*- coding: utf-8 -*-
"""b472_extract.py -- THE SURVEY. ### (R81)-as-amended's flags over this ferry, row U1's cells read by the
### cell reader (rehearsed on site (v) first, under (R70)), the indices and headings at b467's table,
### (R76)/(R78) at their lines, the E0 tables at their address, and the two external acts' banks.
### Banked before the seal. Reads only; writes b472_extract.txt and b472_survey.json.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L, MISSES = [], []
SITES = ('i', 'ii', 'iii', 'iv', 'v', 'vi')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def lines(p):
    return read(p).split(NL)


# ### THE CELL READER. ### It reads ONE site's labelled coordinate cell out of row U1's line: the text
# ### from "`(x)` — KIND:" up to the next site's cell or the tally. It returns the KIND value, the
# ### WITNESS value, and the cell's full text. Nothing else is read into it.
CELL = re.compile(r'### \*\*`\((i|ii|iii|iv|v|vi)\)` — KIND: (.+?)\. WITNESS: (.+?)\.\*\*')


def cell_reader(row, site):
    ms = list(CELL.finditer(row))
    for k, m in enumerate(ms):
        if m.group(1) == site:
            end = ms[k + 1].start() if k + 1 < len(ms) else row.index('### **THE TALLY', m.end())
            return dict(site=site, kind=m.group(2).strip('`'), witness=m.group(3).strip('`'),
                        cell=row[m.start():end].strip(), at=m.start())
    return None


# ### THE ENTRY READER. ### Each site's own entry: from its heading "**(x) TITLE**" to the next site's
# ### heading, or to the row's first structural block after it.
HEAD = re.compile(r'### \*\*\((i|ii|iii|iv|v|vi)\) ([^*]+?)\*\*')
STOPS = ('### **THE SHAPE, NAMED AND NOT PROVED', '### **THE ROW GAINS TWO COORDINATES')


def entries(row):
    hs = [m for m in HEAD.finditer(row)]
    seen, out = set(), {}
    firsts = []
    for m in hs:
        if m.group(1) not in seen:
            seen.add(m.group(1))
            firsts.append(m)
    for k, m in enumerate(firsts):
        end = firsts[k + 1].start() if k + 1 < len(firsts) else len(row)
        seg = row[m.start():end]
        for s in STOPS:
            j = seg.find(s)
            if j > 0:
                seg = seg[:j]
        out[m.group(1)] = dict(title=m.group(2).strip(), text=seg.strip())
    return out


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[*`#_]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def lcs(a, b):
    # ### longest common substring, word-aligned, by dynamic programming over words
    A, B = a.split(' '), b.split(' ')
    best, at = 0, 0
    prev = [0] * (len(B) + 1)
    for i in range(1, len(A) + 1):
        cur = [0] * (len(B) + 1)
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best, at = cur[j], i
        prev = cur
    return best, ' '.join(A[at - best:at])


def main():
    rec('=' * 104)
    rec('b472 -- THE SURVEY.')
    rec('=' * 104)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec('(P1) (R81) AS AMENDED -- EVERY FLAGGED WORD IN THIS FERRY, WHOSE TEXT, AND WHAT IT CARRIES.')
    rec('-' * 104)
    t = lines(os.path.join(D, 'b472_ferry.txt'))
    act = next(i for i, l in enumerate(t) if 'FERRY -> CLAUDE CODE' in l)
    flags = []
    for i, l in enumerate(t):
        for m in re.finditer(r'\b(first|never|only|ever)\b', l, re.I):
            tail = l[m.end():m.end() + 14]
            nxt = t[i + 1] if i + 1 < len(t) else ''
            lab = '[procedural]' if tail.lstrip().startswith('[procedural]') or \
                (tail.strip() == '' and nxt.lstrip().startswith('[procedural]')) else ''
            chk = 'record check' if re.search(r'\[record check', l[m.end():] + ' ' + nxt) else ''
            f = dict(line=i + 1, word=m.group(1), part='RULING (author)' if i < act else 'ACT (navigator)',
                     label=lab or chk or 'NONE', text=l.strip())
            flags.append(f)
            rec('    :%-3d %-16s %-6s %-14s %s' % (f['line'], f['part'], f['word'], f['label'], f['text']))
    nav = [f for f in flags if f['part'].startswith('ACT')]
    nav_bare = [f for f in nav if f['label'] == 'NONE']
    auth_bare = [f for f in flags if f['part'].startswith('RULING') and f['label'] == 'NONE']
    rec('  ### ### **FLAGGED : %d ; IN THE ACT : %d, BARE : %d ; IN THE RULINGS : %d, BARE : %d.**'
        % (len(flags), len(nav), len(nav_bare), len(flags) - len(nav), len(auth_bare)))
    for f in auth_bare:
        rec('    bare in the rulings : :%d %s -- in the line naming the rule`s own list of words' % (f['line'], f['word']))

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec('(P2) ROW U1 -- THE CELL READER, REHEARSED ON SITE (v) FIRST, UNDER (R70).')
    rec('-' * 104)
    fl = lines(os.path.join(PP, 'FACES_LEDGER.md'))
    row = fl[30]
    if not row.startswith('| U1 |'):
        MISSES.append(('FACES_LEDGER.md', 'row U1 at :31'))
    rec('    FACES_LEDGER.md:31 -- %d characters; begins %r' % (len(row), row[:40]))
    rv = cell_reader(row, 'v')
    rec('    ### REHEARSAL -- cell_reader(row U1, "v") RETURNS:')
    if rv:
        rec('      kind    : %r' % rv['kind'])
        rec('      witness : %r' % rv['witness'])
        rec('      at char : %d' % rv['at'])
        rec('      cell    : %s' % rv['cell'])
    else:
        rec('      None')
        MISSES.append(('cell reader', 'site (v)'))
    ok_rehearse = bool(rv) and rv['kind'] == '(b)' and rv['witness'] == 'NONE KNOWN'
    rec('    ### ### **REHEARSAL AGAINST THE LEDGER`S OWN UPDATE LINE (FACES_LEDGER.md:444, which says entry (v)`s')
    rec('    ### `KIND: (b)` and `WITNESS: NONE KNOWN` stand as they read): %s**' % ('AGREES' if ok_rehearse else 'DISAGREES'))

    rec('')
    rec('  THE SIX CELLS, READ BY THE SAME READER:')
    cells = {}
    for s in SITES:
        c = cell_reader(row, s)
        if not c:
            MISSES.append(('cell reader', s))
            continue
        cells[s] = c
        rec('    (%-3s) KIND %-12r WITNESS %-14r cell %d chars' % (s, c['kind'], c['witness'], len(c['cell'])))
    tally = re.search(r'THE TALLY, PRINTED SO NO READER HAS TO COUNT: ([^#]+?)\*\*', row)
    rec('    the row`s own tally : %s' % (tally.group(1).strip() if tally else 'NOT FOUND'))
    kinds = [cells[s]['kind'] for s in cells]
    wits = [cells[s]['witness'] for s in cells]
    rec('    ### the reader`s count : KIND NOT EMPTY %d, (b) %d ; WITNESS NONE KNOWN %d, UNSTATED %d'
        % (kinds.count('NOT EMPTY'), kinds.count('(b)'), wits.count('NONE KNOWN'), wits.count('UNSTATED')))

    rec('')
    rec('  THE SIX ENTRIES (the sites` own text, by heading):')
    ents = entries(row)
    for s in SITES:
        e = ents.get(s)
        if not e:
            MISSES.append(('entry reader', s))
            continue
        rec('    (%-3s) %s -- %d chars' % (s, e['title'], len(e['text'])))
    shape = re.search(r'THE SHAPE, NAMED AND NOT PROVED: ([^*]+?)\*\*', row)
    shape = shape.group(1).strip() if shape else ''
    if not shape:
        MISSES.append(('row U1', 'shape clause'))
    rec('    THE SHAPE CLAUSE : "%s"' % shape)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec('(P3) THE INDEX AND ITS HEADING -- b467`S TABLE AND (R76)/(R78), AT THEIR LINES.')
    rec('-' * 104)
    ot = lines(os.path.join(PP, 'OPEN_TRAILS.md'))
    idx = {}
    for n in range(7557, 7563):
        cols = [x.strip() for x in ot[n].strip().strip('|').split('|')]
        s = cols[0].strip('()')
        idx[s] = dict(index=cols[1], cc=cols[2], general=cols[3].strip('*'), line=n + 1)
        rec('    OPEN_TRAILS.md:%d  (%-3s) index %-15s CC(148) %-20s general %s'
            % (n + 1, s, cols[1], cols[2], cols[3]))
    if sorted(idx) != sorted(SITES):
        MISSES.append(('OPEN_TRAILS.md', 'b467 table at 7558-7563'))
    red = ot[7568]
    rec('    OPEN_TRAILS.md:7569  %s' % red[:400])
    heading = {}
    for s in ('i', 'iii', 'iv'):
        heading[s] = 'a condition on the test function'
    for s in ('v', 'vi'):
        heading[s] = 'a datum of the representation'
    heading['ii'] = 'the instrument`s truncation'
    if not ('(i), (iii), (iv) → *a condition on the test function*' in red
            and '(v), (vi) → *a datum of the representation*' in red
            and '(ii) → *the instrument' in red and 's truncation*' in red):
        MISSES.append(('OPEN_TRAILS.md:7569', 'the reduction'))
    r76 = ot[7633]
    r78 = ot[7790]
    rec('    OPEN_TRAILS.md:7634  (R76) %s' % r76[:700])
    rec('    OPEN_TRAILS.md:7791  (R78) %s' % r78[:600])
    if '(R76)' not in r76 or '(R78)' not in r78:
        MISSES.append(('OPEN_TRAILS.md', '(R76) at 7634 / (R78) at 7791'))

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec('(P4) THE E0 TABLES AT THEIR ADDRESS -- FINDINGS.md:3043 (kinds) AND :3058 (grades).')
    rec('-' * 104)
    fd = lines(os.path.join(PP, 'FINDINGS.md'))
    if not fd[3042].startswith('### The E0 gate') or not fd[3057].startswith('### The grades, one row per constituent'):
        MISSES.append(('FINDINGS.md', 'E0 headings at 3043/3058'))
    e0 = {}
    for n in list(range(3045, 3055)) + list(range(3059, 3070)):
        m = re.match(r'\| \*\*(K\d)\*\* ([^|]+)\|(.*)$', fd[n])
        if m:
            k = m.group(1)
            e0.setdefault(k, dict(name=m.group(2).strip(), kinds='', grades='', kline=0, gline=0))
            if n < 3057:
                e0[k]['kinds'], e0[k]['kline'] = m.group(3), n + 1
            else:
                e0[k]['grades'], e0[k]['gline'] = m.group(3), n + 1
    for k in sorted(e0):
        g = [x.strip() for x in e0[k]['grades'].split('|')]
        rec('    %s %-52s kinds :%d grades :%d  proved: %s | measured: %s | defined: %s'
            % (k, e0[k]['name'][:52], e0[k]['kline'], e0[k]['gline'], g[0][:70], g[1][:60], g[2][:30]))
    if len(e0) != 8:
        MISSES.append(('FINDINGS.md', 'E0 rows %d of 8' % len(e0)))
    rank = re.search(r'ordered `(.+?)`; the open part', read(os.path.join(PP, 'FINDINGS.md')))
    order = [x.strip(' `') for x in rank.group(1).split('<')] if rank else []
    rec('    the sealed grade order (softest first) : %s' % ' < '.join(order))

    rec('')
    rec('  ### THE MAPPING TEST, AS THE FACE WILL FIX IT: a site takes an E0 row only where the site`s OWN text')
    rec('  ### (entry + cell) and that row share a word-aligned run of at least 6 words. Yields printed for all 48.')
    maps = {}
    for s in SITES:
        stext = norm(ents.get(s, {}).get('text', '') + ' ' + cells.get(s, {}).get('cell', ''))
        best = []
        for k in sorted(e0):
            n_, run = lcs(stext, norm(e0[k]['name'] + ' ' + e0[k]['kinds'] + ' ' + e0[k]['grades']))
            best.append((n_, k, run))
        best.sort(reverse=True)
        maps[s] = [dict(k=k, words=n_, run=run) for n_, k, run in best]
        rec('    (%-3s) %s' % (s, ' ; '.join('%s:%d' % (k, n_) for n_, k, run in sorted(best, key=lambda x: x[1]))))
        rec('          longest : %s at %d words -- "%s"' % (best[0][1], best[0][0], best[0][2][:160]))

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec('(P5) THE TWO EXTERNAL ACTS` BANKS, AT THEIR ADDRESSES.')
    rec('-' * 104)
    b468 = lines(os.path.join(D, 'b468r_components.txt'))
    af = {}
    for n in range(82, 106):
        m = re.match(r'\s+\((i|ii|iii|iv|v|vi)\)\s+(\S+)\s+### \*\*(.+?)\*\*', b468[n])
        if m:
            af[m.group(1)] = dict(verdict=m.group(3), line=n + 1, why=b468[n + 1].strip())
            rec('    b468r_components.txt:%d  (%-3s) %-40s %s' % (n + 1, m.group(1), m.group(3), b468[n + 1].strip()[:110]))
    if sorted(af) != sorted(SITES):
        MISSES.append(('b468r_components.txt', 'read (b) at 84-101'))
    b470 = lines(os.path.join(D, 'b470_components.txt'))
    z = {}
    for n, l in enumerate(b470):
        if 'EF_lit_zetaZeroConfig (theorem)' in l and '###' in l:
            z['verdict_line'], z['verdict'] = n + 1, l.strip()
        if 'test-function class zeta23' in l:
            z['class_line'] = n + 1
            z['class'] = ' / '.join(x.strip() for x in b470[n:n + 3])
        if 'CONTAINS : 6' in l:
            z['tally_line'], z['tally'] = n + 1, l.strip()
        if "NOT `MATCHES`, BECAUSE" in l:
            z['why_line'] = n + 1
            z['why'] = ' '.join(x.strip(' #*') for x in b470[n:n + 2])
    for k in ('verdict', 'class', 'tally', 'why'):
        if k not in z:
            MISSES.append(('b470_components.txt', k))
        else:
            rec('    b470_components.txt:%d  %s' % (z[k + '_line'], z[k][:240]))
    iv_names_b321 = 'b321' in ents.get('iv', {}).get('text', '')
    b470_sites = sum(1 for l in b470 if re.search(r'\bsite\b|\(iv\)|\bU1\b', l))
    rec('    site (iv)`s own entry names b321 : %s' % iv_names_b321)
    rec('    lines of b470`s components bank naming a site of row U1 : %d' % b470_sites)

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b472_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    out = dict(flags=flags, act_flags=len(nav), act_bare=len(nav_bare), ruling_bare=len(auth_bare),
               rehearsal=dict(rv or {}, agrees=ok_rehearse), cells=cells,
               entries=ents, shape=shape, index=idx, heading=heading, e0=e0, order=order, maps=maps,
               af=af, z=z, iv_names_b321=iv_names_b321, b470_site_lines=b470_sites, misses=MISSES)
    s = json.dumps(out, indent=1, ensure_ascii=False)
    io.open(os.path.join(D, 'b472_survey.json'), 'w', encoding='utf-8', newline=NL).write(s)
    return 0


if __name__ == '__main__':
    sys.exit(main())
