# -*- coding: utf-8 -*-
"""tools/b769_registry_block.py -- b769, (R379)(4)(a): THE REGISTRY'S BLOCK, under [X1] (OPEN_TRAILS :19263).

Carried from tools/b766_registry_cells.py, its readers imported as committed there (the rows read above b720's block, the phase by
subject, the table filed under, the keystone cell, each document read at HEAD), and from tools/b761_registry.py, its cells() (the SUBJECT
and TO KC cells in b761's form) and its write with the guards before it. Written by the Write tool at b769's Component 2 and committed
before its first run, dry included (N2).

  dry      the reading, the controls, the guards, the counts and the block printed; nothing written
  write    the same; where every control reads AS WANTED and every guard holds, the block appended at REGISTRY's end in PLACE-papers, and
           data/b769_registry_block.txt and .json banked

THE BLOCK, one at the file's end in the form of b761's (REGISTRY :1265), no row above it edited and none moved between tables: (i) for
each numbered row that neither b720's block (:1100) nor b761's reads (52 at b766, data/b766_registry_cells.txt :9-:13), its SUBJECT and
TO KC cells in b761's form; a numbered row on a line rule [Q] protects is cited there by its line and the line's sha256 and read by
nothing; (ii) for each row read (151 at b766), THE PHASE BY SUBJECT, with the table it is filed under where that differs, and THE KEYSTONE
CELL, as (R376)(5)(a) rules them. One sentence says the author struck nothing from the four lists of data/b766_registry_cells.txt
:175-:180, so each stands as read at this head; 1.5h-8 and p2-3, which name one document, are printed as one keystone in two rows; no
title is changed.
CONTROLS ((R379)(4)(a): b766's six): the eight rows of Day 1 read KEYSTONE; the canon reads APPARATUS; 1.5a-1 reads SOURCE, named by
1.5a-9; a planted row reads UNPLACED; the six cluster syntheses of May read APPARATUS; the identifiers, the protected word, a host folder
and the two :3 lines 0 in the bank and in the block.
THE WRITE'S GUARDS (b761's, with the block's own heading): the file's bytes at HEAD a prefix of its new bytes; rule [Q] (3)'s heading by its
digest at :374 before and after, no line above it changing; each table row's cells three and each line's backticks even; each SUBJECT's
cited line read back carrying its clause; the block's heading once in the new file and b720's and b761's headings each once, outside it.
Beside them, printed and no guard: the SUBJECT clauses naming zeta, RH, GRH or Weil, by row, for the seat's hand read (N3).

No PLACE-papers line is printed but the clauses this tool composes; the protected word is never printed or stored; no git write.
"""
import hashlib
import json
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b761_registry as R61          # noqa: E402  ### b761's readers and cells(), as committed
import b766_registry_cells as R66    # noqa: E402  ### b766's reading, as committed

ACT, NL = 'b769', '\n'
PP, REG = R61.PP, R61.REG
BANK = os.path.join(D, 'b769_registry_block.txt')
BJSON = os.path.join(D, 'b769_registry_block.json')
B766_NOT_READ, B766_ROWS = 52, 151
ONE_DOC = ('1.5h-8', 'p2-3')
BLOCK_HEAD = '## THE PHASE BY SUBJECT AND THE KEYSTONE CELL OF EACH ROW READ, WITH THE SUBJECT / TO-KC CELLS OF THE ROWS NO EARLIER BLOCK READS'
B720_HEAD, B761_HEAD = '## SUBJECT / TO-KC ATTRIBUTE', '## SUBJECT / TO-KC CELLS OF PHASE 1.5'
N3_WORDS = re.compile(r'(?i)\b(zeta|ζ|RH|GRH|Riemann Hypothesis|Weil)\b')


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


# ================================================================================ THE READING, b766's as committed
def reading():
    base = R61.at_head()
    L = base.split(NL)[:-1]
    qw = R61.qword(L)
    I = R61.ids()
    TG = R61.tags()
    Q = R66.q_section(L)
    WL = [k for k, l in enumerate(L, 1) if re.search(r'\b%s\b' % re.escape(qw), l, re.I)]
    P = Q | set(x for w in WL for x in range(max(1, w - 2), min(len(L), w + 2) + 1))   # ### rule [Q] as the seat's reader takes it
    H = R66.heading_of(L)
    out, _rc = R61.git(PP, 'ls-tree', '-r', '--name-only', 'HEAD')
    tracked = set(x for x in out.split(NL) if x)
    head = R61.git(PP, 'rev-parse', '--short=8', 'HEAD')[0].strip()
    rows, info = R66.collect(L, Q, P, H, tracked)
    rows = R66.read_rows(rows, L, P, I, qw, TG, info)
    rows, ks = R66.classify(rows)
    for r in rows:
        r['phase'] = R66.phase(r['id'], r['filed']) if r['numbered'] else (r['filed'] if r['filed'] in (R66.SUP, R66.INTL, R66.ANX) else R66.METHOD)
        r['differs'] = r['phase'] != r['filed'] and not (r['filed'] == R66.NOPH and r['phase'] == R66.METHOD)
    num = [r for r in rows if r['numbered']]
    c720 = R66.block_cells(L, P, info['stop'], info['b761'] - 1)
    c720_any = set(m.group(1) for k in range(info['stop'], info['b761']) if k not in P
                   for m in [re.match(r'^\| (?:### \*\*)?`([^`]+)`', L[k - 1])] if m)
    not720 = [r['id'] for r in num if r['id'] not in c720_any]
    nyr720 = [r['id'] for r in num if r['id'] in c720_any and r['id'] not in c720]
    c761 = R66.block_cells(L, P, info['b761'], len(L))
    neither = [x for x in not720 + nyr720 if x not in c761]
    prot = info['prot']
    prot_num = [(k, d) for k, d, w in prot if w == 'a numbered row' and k not in Q]
    return dict(base=base, L=L, qw=qw, I=I, TG=TG, Q=Q, P=P, head=head, rows=rows, ks=ks, info=info, num=num, not720=not720, nyr720=nyr720,
                neither=neither, prot=prot, prot_num=prot_num, c720=c720, c761=c761)


def cells69(r, I, qw, TG):
    """b761's two cells for one row, in b761's form: tools/b761_registry.py cells() :294-:319 carried, its strings as committed there, with
    b766's guard for the one-page proof's :3 (tools/b766_registry_cells.py :338). The document is b766's reading of the row (its File cell
    resolved against HEAD's tree, :173-:186), where b761's matcher took a file cell under phase*/ alone and read a row with no such cell
    as a kernel row: p2-26 names heritage/, and p2-d8 and p2-d9 name no document."""
    k = r['line']
    if r['sw']:
        w = 'withdrawn' if 'WITHDRAWN' in r['status'].upper() else 'superseded'
        return dict(kind=w, subject='%s, as its row reads (REGISTRY :%d); no text read' % (w, k), tokc='%s; no text read' % w)
    if not r['path']:
        return dict(kind='no document', subject='no document, as its row reads (REGISTRY :%d); no text read' % k, tokc='no document; no text read')
    path = r['path']
    d = R61.read_doc(path, I, qw, TG) if r['where'].startswith('AT HEAD') else None
    if d is None:
        return dict(kind='absent', path=path, subject='absent at HEAD, as its row names it (REGISTRY :%d, `%s`); no text read' % (k, path),
                    tokc='absent; no text read')
    j2 = None
    marker = False
    if not d['k']:
        subj, cl_, cut = 'no %s sentence read (`%s`)' % (d['src'], path), '', False
    else:
        # ### the corpus's `### ` marker read off the source's end as plain() reads it before a space: plain() strips the source first, so a
        # ### PURPOSE group ending `— ### ` before a bold annotation kept `###` (p2-16, the dry of 19:46:52Z, its read-back guard holding)
        src_ = d['line']
        if re.search(r'(?:^|\s)#{3}$', src_):
            src_, marker = re.sub(r'(?:^|\s)#{3}$', '', src_).rstrip(), True
        cl_, cut = R61.clause_of(src_)
        j2 = next((x for x in range(d['k'], d['j'] + 1) if cl_ in R61.span_text(d['D'], d['k'], x)), d['j'])
        where = '%s :%d' % (d['src'], d['k']) + ('–:%d' % j2 if j2 > d['k'] else '')
        if qw.lower() in cl_.lower() or R61.idcount(cl_, I) or (path in R66.ONEPAGE and d['k'] <= 3 <= j2):
            subj = 'its %s line cited by line and digest alone: :%d (sha256 %s)' % (d['src'], d['k'], sha(d['D'][d['k'] - 1])[:16])
            cl_ = ''
        else:
            subj = '“%s%s” (%s)' % (cl_.replace('|', '\\|'), ' …' if cut else '', where)
    parts = ['class %s (:%d)' % (d['cls'][1], d['cls'][0]) if d['cls'] else 'no class line']
    parts.append('; '.join('%s %s' % (n, ', '.join(':%d' % x for x in ks[:4]) + (' and %d more' % (len(ks) - 4) if len(ks) > 4 else '')) for n, ks in d['heads'])
                 if d['heads'] else 'none of Correspondence, Glossary, References or Bibliography, Errata')
    parts.append('SIDE-explicit-formula `%s` %s (:%d)' % (d['tag'][0], d['tag'][2], d['tag'][3]) if d['tag'] else 'names no tag')
    tier = d['cls'][1] if d['cls'] else ''
    if re.fullmatch(r'TIER (K|C)', tier) or d['kc']:
        parts.append('**candidate** (%s)' % ('Tier %s declared' % tier[-1] if tier else 'names itself a keystone candidate, :%d' % d['kc'][0]))
    elif tier == 'TIER KC':
        parts.append('declares Tier KC whole, where b720’s rule gives the word to a head declaring one half (Tier K or Tier C), so the word is not given here; `%s` :69 names no candidate' % R61.TAXONOMY)
    else:
        parts.append('not a candidate by b720’s rule')
    return dict(kind='read', path=path, src=d['src'], k=d['k'], j=j2, clause=cl_, cut=cut, subject=subj, tokc=' · '.join(parts),
                cls=d['cls'], heads=d['heads'], tag=d['tag'][:2] if d['tag'] else None, marker=marker,
                line_text=NL.join(d['D'][d['k'] - 1:j2]) if d['k'] else '')


def neither_cells(R):
    """b761's two cells for each numbered row no earlier block reads, in the order b766's reading gives them."""
    by = dict((r['id'], r) for r in R['num'])
    out = []
    for rid in R['neither']:
        r = by[rid]
        cc = cells69(r, R['I'], R['qw'], R['TG'])
        cc.update(id=rid, row=r['line'])
        out.append(cc)
    return out


def cell_block(r):
    """THE KEYSTONE CELL as the block prints it: b766's cell, the lines of a naming row given as the keystone document's own."""
    if r['cell'] == R66.SN:
        by = {}
        for kid, ln in r['named']:
            by.setdefault(kid, []).append(ln)
        t = 'SOURCE, NAMED IN %d ROWS (%s)' % (len(r['named']), '; '.join('by %s at its document’s :%s' % (k, ', :'.join(str(x) for x in v[:4]))
                                                                       for k, v in by.items()))
    elif r['cell'] == R66.SNN:
        t = 'SOURCE, NOT NAMED (its cluster %s, keystones in it %d)' % (r['cluster'], r.get('ks_in_cluster', 0))
    else:
        t = r['cell']
    if r['tier'] and r['cell'] in (R66.KEY, R66.CS):
        t += ' (Tier %s declared at its :%d)' % (r['tier'], r['tier_line'])
    if r['id'] in ONE_DOC and r['cell'] == R66.KEY:
        t += '; one keystone in two rows with `%s`, the one document' % [x for x in ONE_DOC if x != r['id']][0]
    return t


def phase_block(r):
    return r['phase'] + ((', filed under %s' % r['filed']) if r['differs'] else '')


# ================================================================================ THE BLOCK
def compose(R, nc, date):
    rows, info = R['rows'], R['info']
    kc = {}
    for r in rows:
        kc[r['cell']] = kc.get(r['cell'], 0) + 1
    kp = {}
    for r in rows:
        if r['cell'] == R66.KEY:
            kp.setdefault(r['phase'], []).append(r['id'])
    tables = sorted(set(r['table'] for r in rows))
    differs = [r for r in rows if r['differs']]
    unplaced = [r for r in rows if r['cell'] == R66.UNP]
    flagged = [r for r in rows if r['flag']]
    one = [r for r in rows if r['id'] in ONE_DOC and r['cell'] == R66.KEY]
    one_doc = one[0]['path'] if len(one) == 2 and one[0]['path'] == one[1]['path'] else None
    kdocs = len(set(r['path'] for r in rows if r['cell'] == R66.KEY))
    protl = '; '.join(':%d (sha256 %s)' % (k, d) for k, d, _w in R['prot']) or 'none'
    out = ['<!-- b769 (R379)(4)(a) THE REGISTRY’S BLOCK, %s -->' % date, '',
           '%s *(added %s, b769, under the author’s ruling `(R379)`(4)(a), by `(R376)`(5)(a); in the form of b761’s block (:%d), which is not edited, as b720’s (:%d) is not)*' % (
               BLOCK_HEAD, date, info['b761'], info['stop']), '',
           '**Two tables, read at this repository’s HEAD by b766’s reading of the rows, carried; no row above is edited and none is moved between tables. '
           'The first gives each numbered row that neither b720’s block nor b761’s reads its two cells in b761’s form: `SUBJECT`, one clause quoted '
           'from the document’s own text — its PURPOSE line where its head carries one, else its abstract’s first sentence, else its opening’s — cut '
           'at its first semicolon, its lines cited; `TO KC`, the class its standing class line declares, which of the headings Correspondence, '
           'Glossary, References or Bibliography, and Errata it carries, the newest tag of SIDE-explicit-formula its text carries, and the word '
           '`candidate` by b720’s rule. The second gives each row read THE PHASE BY SUBJECT — the eight rows of Day 1, the Day 1 cluster; 1.5a-1 to '
           '1.5a-10 and 1.5g-1 to 1.5g-4, Phase 1.2; the other rows of 1.5A to 1.5G, Phase 1.5; the rows of 1.5H and the rows under no phase heading, '
           'method, Phase 2 in time; the rows of Phase 2, Phase 2; the support, internal and annex tables as they are headed — with the table it is '
           'filed under where that differs, and THE KEYSTONE CELL — APPARATUS for the canon, the taxonomy, the census, the six cluster syntheses of '
           'May and CATALOGOS; WITHDRAWN OR SUPERSEDED where the row’s Status cell says so; KEYSTONE where the document’s head declares Tier K or '
           'Tier KC, or the row is one of Day 1’s eight, or is 1.5c-24, 1.5g-4, 1.5h-7 or 1.5h-9; CLUSTER SYNTHESIS where it declares Tier C; '
           'SOURCE, NAMED IN <n> ROWS where a keystone of its cluster names it in its Correspondence table or its table of papers, those rows’ '
           'lines in the keystone’s document cited; SOURCE, NOT NAMED where none does; UNPLACED for the rest. The author struck nothing from the '
           'four lists of b766’s reading (relay data/b766_registry_cells.txt :175-:180): the keystones by phase, the rows filed under a table other '
           'than their phase by subject, the rows reading UNPLACED and the titles carrying a number, so each stands as it is read here. 1.5h-8 and '
           'p2-3 name one document%s and are one keystone in two rows. No title is changed here, a flagged one among them. The rows on lines that '
           'rule [Q] protects are cited by line and digest alone and read by nothing: %s.**' % (
               (', `%s`,' % one_doc) if one_doc else '', protl), '',
           '| row | `SUBJECT` | `TO KC` |', '|:--|:--|:--|']
    for c in nc:
        out.append('| `%s` | %s | %s |' % (c['id'], c['subject'], c['tokc']))
    for k, d in R['prot_num']:
        out.append('| `REGISTRY :%d` | a numbered row on a line rule [Q] protects, cited by its line and the line’s sha256 alone (%s); not read | not read |' % (k, d))
    out += ['', '| row | THE PHASE BY SUBJECT | THE KEYSTONE CELL |', '|:--|:--|:--|']
    for r in rows:
        out.append('| `%s` | %s | %s |' % (r['id'], phase_block(r), cell_block(r)))
    nread = len(nc) + len(R['prot_num'])
    counted = ('> **COUNTED:** %d rows of %d tables read at this repository’s HEAD %s (numbered %d; of the tables whose rows carry no number %d); the public '
               'titles’ rows naming a numbered row, not read again, %d; on lines rule [Q] protects, cited by line and digest and read by nothing, %d. '
               'THE KEYSTONE CELL: KEYSTONE %d (%d documents), CLUSTER SYNTHESIS %d, APPARATUS %d, SOURCE, NAMED %d, SOURCE, NOT NAMED %d, WITHDRAWN '
               'OR SUPERSEDED %d, UNPLACED %d. The keystones by phase: the Day 1 cluster %d, Phase 1.2 %d, Phase 1.5 %d, method %d, Phase 2 %d. The '
               'numbered rows no earlier block reads: %d (by neither block %d, on protected lines %d), beside b766’s %d. Rows filed under a table '
               'other than their phase by subject %d; rows reading UNPLACED %d; titles carrying a number %d.') % (
        len(rows), len(tables), R['head'], len(R['num']), len(rows) - len(R['num']), len(info['skipped']), len(R['prot']),
        kc.get(R66.KEY, 0), kdocs, kc.get(R66.CS, 0), kc.get(R66.APP, 0), kc.get(R66.SN, 0), kc.get(R66.SNN, 0), kc.get(R66.WS, 0), kc.get(R66.UNP, 0),
        len(kp.get(R66.DAY1, [])), len(kp.get(R66.P1_2, [])), len(kp.get(R66.P1_5, [])), len(kp.get(R66.METHOD, [])), len(kp.get(R66.P2, [])),
        nread, len(nc), len(R['prot_num']), B766_NOT_READ, len(differs), len(unplaced), len(flagged))
    out += ['', counted, '', '<!-- b769 (R379)(4)(a) THE REGISTRY’S BLOCK END, %s -->' % date, '',
            '*Appended by b769. No row above is edited; b720’s and b761’s blocks stand as written. Nothing deposits.*']
    figs = dict(rows=len(rows), tables=len(tables), numbered=len(R['num']), kc=kc, kp=kp, kdocs=kdocs, nread=nread, neither=len(nc),
                prot_num=len(R['prot_num']), differs=[[r['id'], r['phase'], r['filed']] for r in differs], unplaced=[r['id'] for r in unplaced],
                flagged=[[r['id'], r['flag']] for r in flagged], one_doc=one_doc)
    return NL.join(out), figs


# ================================================================================ THE RUN
def run(mode):
    R = reading()
    L, base, I, qw, rows = R['L'], R['base'], R['I'], R['qw'], R['rows']
    nc = neither_cells(R)
    date = time.strftime('%Y-%m-%d', time.gmtime())
    block, F = compose(R, nc, date)
    new = base + NL + block + NL
    NLn = new.split(NL)[:-1]
    first = len(L) + 2
    # ### THE CONTROLS, b766's six
    d1 = [r for r in rows if r['id'].startswith('d1-')]
    canon = [r for r in rows if (r['path'] or '').endswith('THE_METHOD_CANON.md')]
    a1 = [r for r in rows if r['id'] == '1.5a-1']
    planted = dict(id='zz-99', numbered=True, path=None, sw=False, tier=None, cluster=None, kdoc=None, status='', where='planted')
    pr, _pk = R66.classify([planted])
    may = [r for r in rows if (r['path'] or '').startswith('clusters/') and '_CLUSTER_SYNTHESIS_2026-05-' in (r['path'] or '')]
    ctl = [('the eight rows of Day 1 read KEYSTONE: %d rows, %s' % (len(d1), [(r['id'], r['cell']) for r in d1]),
            len(d1) == 8 and all(r['cell'] == R66.KEY for r in d1)),
           ('the canon reads APPARATUS: %s' % [(r['id'], r['cell']) for r in canon], len(canon) == 1 and canon[0]['cell'] == R66.APP),
           ('1.5a-1 reads SOURCE, named by 1.5a-9: %s' % [(r['cell'], r.get('named', [])[:3]) for r in a1],
            len(a1) == 1 and a1[0]['cell'] == R66.SN and any(k == '1.5a-9' for k, _ln in a1[0]['named'])),
           ('a planted row (zz-99, no document, no cluster) reads UNPLACED: %s' % pr[0]['cell'], pr[0]['cell'] == R66.UNP),
           ('the six cluster syntheses of May read APPARATUS: %d' % len(may), len(may) == 6 and all(r['cell'] == R66.APP for r in may))]
    # ### THE WRITE'S GUARDS
    back = []
    for c in nc:
        if c.get('kind') == 'read' and c.get('clause'):
            Dl, _rc = R61.git(PP, 'show', 'HEAD:' + c['path'])
            Dl = Dl.replace('\r', '').split(NL)
            back.append((c['id'], '%s-%s' % (c['k'], c['j']), c['clause'] in R61.span_text(Dl, c['k'], c['j']) and NL.join(Dl[c['k'] - 1:c['j']]) == c['line_text']))
    bl = block.split(NL)
    tbl = [l for l in bl if l.startswith('| `')]
    cellbad = [l[:16] for l in tbl if len(re.split(r'(?<!\\)\|', l)) != 5]
    ticks = [k for k, l in enumerate(bl, 1) if l.count('`') % 2]
    qb = [k for k, l in enumerate(L, 1) if sha(l)[:16] == R61.QHEAD]
    qa = [k for k, l in enumerate(NLn, 1) if sha(l)[:16] == R61.QHEAD]
    hb = [k for k, l in enumerate(NLn, 1) if l.startswith(BLOCK_HEAD)]
    h720 = [k for k, l in enumerate(NLn, 1) if l.startswith(B720_HEAD)]
    h761 = [k for k, l in enumerate(NLn, 1) if l.startswith(B761_HEAD)]
    grd = [('the file`s bytes at HEAD a prefix of its new bytes (%d lines to %d, the block from :%d)' % (len(L), len(NLn), first), new.startswith(base)),
           ('rule [Q] (3)`s heading by its digest at :%d before and after (%s -> %s), no line above it changing' % (R61.QLINE, qb, qa),
            qb == [R61.QLINE] and qa == [R61.QLINE] and NLn[:R61.QLINE] == L[:R61.QLINE]),
           ('each table row three cells (off %s) and each line`s backticks even (off %s); table rows %d' % (cellbad, ticks, len(tbl)), not cellbad and not ticks),
           ('each SUBJECT`s cited line read back carrying its clause: %d of %d; the first %s' % (sum(1 for x in back if x[2]), len(back), back[:1]),
            all(x[2] for x in back)),
           ('the block`s heading once in the new file (%s), at or after :%d; b720`s (%s) and b761`s (%s) each once, before it' % (hb, first, h720, h761),
            len(hb) == 1 and hb[0] >= first and len(h720) == 1 and len(h761) == 1 and h720[0] < first and h761[0] < first)]
    n3 = [(c['id'], m.group(1)) for c in nc for m in [N3_WORDS.search(c.get('clause') or '')] if m]
    kc, kp = F['kc'], F['kp']
    P = ['%s -- (R379)(4)(a): THE REGISTRY`S BLOCK, UNDER [X1] (%s)' % (ACT, utc()), '',
         '### tools/b769_registry_block.py %s; PLACE-papers HEAD %s, REGISTRY.md %d lines; the kernel clone`s tags %d (the newest %s). The block`s' % (
             mode, R['head'], len(L), len(R['TG']), R['TG'][-1][0]),
         '### words stand in REGISTRY alone; here each row by its id and its cells` sources; the protected word neither printed nor stored.', '',
         '## THE ROWS READ: %d of %d tables (numbered %d ; of the tables whose rows carry no number %d), beside b766`s %d ; the public titles` rows '
         'naming a numbered row, not read again, %d ; on a line rule [Q] protects %d' % (
             F['rows'], F['tables'], F['numbered'], F['rows'] - F['numbered'], B766_ROWS, len(R['info']['skipped']), len(R['prot'])),
         '## THE NUMBERED ROWS NO EARLIER BLOCK READS: b720`s block (:%d) names %d as not yet read and does not name %d ; of those, b761`s (:%d) reads '
         '%d ; by neither %d, with the numbered rows on protected lines outside rule [Q]`s section %d: %d, beside b766`s %d (%s)' % (
             R['info']['stop'], len(R['nyr720']), len(R['not720']), R['info']['b761'], len(R['not720']) + len(R['nyr720']) - len(R['neither']),
             len(R['neither']), len(R['prot_num']), F['nread'], B766_NOT_READ, 'EQUAL' if F['nread'] == B766_NOT_READ else 'DIFFERING'),
         '  by neither block: %s' % (', '.join(R['neither']) or 'none'),
         '## THE ROWS ON A LINE RULE [Q] PROTECTS, each by its line and the line`s sha256 alone: %s' % (
             '; '.join(':%d %s (%s)' % x for x in R['prot']) or 'none'), '',
         '## THE CELLS OF THE ROWS NO EARLIER BLOCK READS: id | its row | kind | the SUBJECT`s source and lines | the clause`s sha256 | class | the newest tag | candidate',
         '  the corpus`s ### marker read off a clause source`s end (b769, the read-back guard of the dry of 19:46:52Z): %s' % (
             ', '.join(c['id'] for c in nc if c.get('marker')) or 'none')]
    for c in nc:
        if c.get('kind') == 'read':
            P.append('  %s | :%d | read | %s :%s-%s | %s%s | %s | %s | %s' % (
                c['id'], c['row'], c['src'], c['k'], c['j'], sha(c['clause'])[:16] if c['clause'] else 'by digest', ' (cut)' if c.get('cut') else '',
                ('%s :%d' % (c['cls'][1], c['cls'][0])) if c.get('cls') else 'none', ('%s %s' % tuple(c['tag'])) if c.get('tag') else 'none',
                'candidate' if '**candidate**' in c['tokc'] else '-'))
        else:
            P.append('  %s | :%d | %s | - | - | - | - | -' % (c['id'], c['row'], c['kind']))
    P += ['', '## THE ROWS READ: id | THE PHASE BY SUBJECT | the table filed under | THE KEYSTONE CELL']
    for r in rows:
        P.append('  %s | %s | %s | %s' % (r['id'], r['phase'], r['filed'], cell_block(r)))
    P += ['', '## THE COUNTS',
          '  by the keystone cell: %s' % ' ; '.join('%s %d' % (c, kc.get(c, 0)) for c in (R66.KEY, R66.CS, R66.APP, R66.SN, R66.SNN, R66.WS, R66.UNP)),
          '  the keystones by phase: %s' % ' ; '.join('%s %d' % (p, len(kp.get(p, []))) for p in (R66.DAY1, R66.P1_2, R66.P1_5, R66.METHOD, R66.P2, R66.SUP, R66.INTL, R66.ANX)),
          '  the keystone rows` documents: %d distinct of %d rows ; 1.5h-8 and p2-3 one document: %s' % (F['kdocs'], kc.get(R66.KEY, 0), F['one_doc'] or 'NOT READ SO'),
          '  THE FOUR LISTS AS READ AT THIS HEAD (the author`s strikes none): (1) %s ; (2) %d rows ; (3) %d rows ; (4) %d rows' % (
              ' ; '.join('%s: %s' % (p, ', '.join(kp.get(p, [])) or 'none') for p in (R66.DAY1, R66.P1_2, R66.P1_5, R66.METHOD, R66.P2)),
              len(F['differs']), len(F['unplaced']), len(F['flagged'])),
          '  (3) THE ROWS READING UNPLACED: %s' % (', '.join(F['unplaced']) or 'none'),
          '  (4) THE ROWS CARRYING A TITLE FLAG: %s' % ('; '.join('%s (%s)' % (i, ', '.join(f)) for i, f in F['flagged']) or 'none'),
          '  THE SUBJECT CLAUSES NAMING zeta, RH, GRH OR WEIL (N3; quoted clauses of the documents, read by the seat`s hand): %s' % (
              '; '.join('%s (%s)' % x for x in n3) or 'none'), '']
    text = NL.join(P)
    lines3 = []
    for op in R66.ONEPAGE:
        raw, rc = R61.git(PP, 'show', 'HEAD:' + op)
        if not rc and raw:
            l3 = raw.replace('\r', '').split(NL)[2:3]
            if l3 and l3[0].strip():
                lines3.append(l3[0].strip())
    host = os.path.basename(os.path.dirname(R61.PP.rstrip('/')))   # ### the host folder read from b761's constant, never written here
    both = text + NL + block
    bad = R61.idcount(both, I) + (1 if qw.lower() in both.lower() else 0) + sum(both.count(x) for x in (host, 'Users\\', 'Users/', ':\\'))
    ctl.append(('the identifiers, the protected word, a host folder and the two :3 lines 0 in the bank and the block (%d ; the :3 lines read %d, present %d)' % (
        bad, len(lines3), sum(1 for x in lines3 if x in both)), bad == 0 and bool(host) and not any(x in both for x in lines3)))
    ok_c = all(o for _w, o in ctl)
    ok_g = all(o for _w, o in grd)
    P += ['## THE CONTROLS ((R379)(4)(a): b766`s six)'] + ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['## THE WRITE`S GUARDS (b761`s)'] + ['  %-150s %s' % (w, 'HOLDS' if o else 'DOES NOT HOLD') for w, o in grd]
    failed = [w.split(':')[0] for w, o in ctl if not o] + [w.split(' (')[0] for w, o in grd if not o]
    x4 = ('REGISTRY :%d, rows read %d of %d tables, KEYSTONE %d, the keystones by phase the Day 1 cluster %d, Phase 1.2 %d, Phase 1.5 %d, method %d, '
          'Phase 2 %d, the SUBJECT and TO KC cells of %d rows that no earlier block reads, the author`s strikes on the four lists none, no row above '
          'the block edited and no title changed') % (
        first, F['rows'], F['tables'], kc.get(R66.KEY, 0), len(kp.get(R66.DAY1, [])), len(kp.get(R66.P1_2, [])), len(kp.get(R66.P1_5, [])),
        len(kp.get(R66.METHOD, [])), len(kp.get(R66.P2, [])), F['nread'])
    P += ['', '## [X4]`S FIELDS: %s' % (x4 if ok_c and ok_g else 'NOT WRITTEN: %s read other than wanted' % '; '.join(failed)), '',
          '### ### **THE REGISTRY`S BLOCK: %d ROWS OF %d TABLES READ ; KEYSTONE %d ; NOT READ BY AN EARLIER BLOCK %d ; CONTROLS %d OF %d AS WANTED ; GUARDS %d OF %d ; %s.**' % (
              F['rows'], F['tables'], kc.get(R66.KEY, 0), F['nread'], sum(1 for _w, o in ctl if o), len(ctl), sum(1 for _w, o in grd if o), len(grd),
              ('WRITTEN AT REGISTRY :%d' % first if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok_c and ok_g else 'HELD, NOTHING WRITTEN')]
    final = NL.join(P) + NL
    if R61.idcount(final, I) or qw.lower() in final.lower():
        die('AN IDENTIFIER OR THE PROTECTED WORD IN THE PRINT')
    print(final, end='')
    if mode == 'dry':
        if ok_c and R61.idcount(block, I) == 0 and qw.lower() not in block.lower():
            print(NL + '### THE BLOCK AS COMPOSED (the dry run`s print alone, %d lines):' % len(bl))
            print(block)
        return 0 if ok_c and ok_g else 1
    if not (ok_c and ok_g):
        die('A CONTROL OR A GUARD NOT AS WANTED')
    with open(os.path.join(PP, REG), 'wb') as f:
        f.write(new.encode('utf-8'))
    with open(os.path.join(PP, REG), 'rb') as f:
        if f.read() != new.encode('utf-8'):
            die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(BANK, final)
    put(BJSON, json.dumps(dict(at=utc(), act=ACT, date=date, pp_head=R['head'], registry_lines_before=len(L), registry_lines_after=len(NLn),
                               block_first_line=first, block_lines=len(bl), block_sha256=sha(block)[:16], file_sha_before=sha(base)[:16],
                               file_sha_after=sha(new)[:16], rows=F['rows'], tables=F['tables'], numbered=F['numbered'], counts=kc, keystones_by_phase=kp,
                               keystone_documents=F['kdocs'], one_document=F['one_doc'], not_read_by_an_earlier_block=F['nread'], by_neither=R['neither'],
                               protected=[[k, d, w] for k, d, w in R['prot']], differs=F['differs'], unplaced=F['unplaced'], flagged=F['flagged'],
                               n3_clauses=n3, x4=x4, controls=[[w, o] for w, o in ctl], guards=[[w, o] for w, o in grd],
                               cells=[dict(id=c['id'], row=c['row'], kind=c['kind'], src=c.get('src'), line=c.get('k'), line_end=c.get('j'),
                                           clause_sha256=sha(c['clause'])[:16] if c.get('clause') else None, candidate='**candidate**' in c['tokc'])
                                      for c in nc]), ensure_ascii=False, indent=1) + NL)
    print('written REGISTRY.md (%d lines to %d, the block from :%d); data/b769_registry_block.txt and .json' % (len(L), len(NLn), first))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write']):
        sys.exit(__doc__)
    sys.exit(run(a[0]))
