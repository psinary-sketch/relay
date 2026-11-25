# -*- coding: utf-8 -*-
"""tools/b769_waves.py -- b769, (R379)(6): THE WAVES READ RECORD BY RECORD. A reading and no build: no line of REGISTRY, of the census or
of a paper is written; no git write; nothing fetched.

Written by the Write tool and committed before its run (N2). THE ROWS: each keystone row that list (1) of (4)(a) gives the Day 1 cluster,
Phase 1.2 and Phase 1.5 (data/b769_registry_block.json `keystones_by_phase`; 8, 6 and 6 at b766, data/b766_registry_cells.txt :170 and
:176), each read again KEYSTONE in its phase by b766's reading of the rows at the papers` repository's HEAD (tools/b769_registry_block.py
reading(), as committed). For each row, at that HEAD:
  (i)   its document's title line (b766's: the first line opening '# ' in its first twenty) and its version line (the first line of its head,
        before its first '## ', holding the word version with a dotted number after it, or opening with v and a dotted number);
  (ii)  the files under outputs/ holding a copy of it, in the form of tools/b764_rulings.py deposit as tools/b769_errata.py carries it: each
        file by its lines; a copy where it holds a quarter or more of the document's distinct lines of 40 characters or more; deposited where
        it stands under outputs/DEPOSITED; and the record REGISTRY names for it: the ids of seven to nine digits its row's line carries within
        40 characters after the word zenodo, record, concept, doi or deposit;
  (iii) the entries of ERRATA (each '## E-' heading to the next '## ' heading) and the fact items of OPEN_TRAILS (each line holding the words
        FACT ITEM) that name its file, by its path or its file's stem standing as a word (b766's names_it), counted, this act's among them
        (data/b769_ledgers_c3.json);
  (iv)  the orders whose status tools/standing/orders.py reads as other than CLOSED that name it: an order names a file where a line of
        OPEN_TRAILS naming the order, a roll line excepted, names the file;
  (v)   each kernel pin that its head or its SUBJECT and TO KC cells cite (b720's block, b761's block and b769's first table in REGISTRY, the
        rows that read it): a kernel's name, SIDE- and its words, beside a tag (v and its numbers) or a commit (seven to forty hex digits, a
        letter among them), or a tag before "of", "on" or "in" and the kernel's name; read beside the kernel's newest tag as its clone reads it
        (the clone's tags in creation order, the last): CURRENT where the pin is that tag or that tag's commit, STALE where it is an earlier
        tag of the clone or a commit behind that tag's; any other reading printed by its words;
  (vi)  the names its Correspondence tables give (b756's sections, every Correspondence heading to the next heading of its level; b589's
        names of each table row), joined to data/terminal_table.json as committed at the relay's HEAD by b766's rule (a name names a
        declaration where it equals its full name or a dot-suffix of it): the names; AT HEAD, those naming a declaration that the table
        carries at the kernel's head it read (present_at holding HEAD); NOT, the rest (naming none, or only declarations at a tag); b766's
        join's count of declarations named printed beside; and for each kernel named, the table's head beside the clone's HEAD now;
  (vii) its ratified public title (REGISTRY's table headed at :638, its row matched by the ID cell, else by the file cell) beside its title
        line, and its title flag (list (4)'s, b766's flag() over the title line).
THE COUNTS by wave at the bank's foot, and in all.

CONTROLS, each printed, all AS WANTED before the bank is written: list (1)'s ids 8, 6 and 6, each KEYSTONE in its phase at HEAD; a planted
row whose head pins SIDE-explicit-formula's first tag reads STALE, its newest tag CURRENT, the newest tag's commit CURRENT and that commit's
parent STALE ((6)'s first control, with three beside it); a planted row naming a declaration absent from the terminal table moves NOT by
one and AT HEAD by none ((6)'s second); the papers` repository at the act's last commit there before this component, its outputs/ clean;
the identifiers, the account and the protected word 0 in the bank.

  dry      prints the controls and the bank; writes nothing
  write    the same, then data/b769_waves.txt and .json

No PLACE-papers line is printed but titles, version lines and public titles, each where it carries no identifier and not the protected word
(else cited by line and digest), and the backticked names a Correspondence table gives that name no declaration at the table's head (six
at most a row); the protected word is derived in memory, never printed; a line rule [Q] protects is cited, never read.
"""
import json
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b769_rulings as RU              # noqa: E402  ### the act's helpers, as committed
import b769_errata as ER               # noqa: E402  ### outputs() and b764's copy rule, as committed
import b769_registry_block as R69      # noqa: E402  ### reading(), as committed
import b766_registry_cells as R66      # noqa: E402
import b761_registry as R61            # noqa: E402
import b756_constellation as B56       # noqa: E402  ### sections(), is_row(), terminal_names()
import b766_lean_join as J66           # noqa: E402  ### join()
import orders as OR                    # noqa: E402  ### tools/standing/orders.py

ACT, NL, PP, D, RELAY = RU.ACT, RU.NL, RU.PP, RU.D, RU.RELAY
sha, git, utc, die, put, jload = RU.sha, RU.git, RU.utc, RU.die, RU.put, RU.jload
C4PP = '5111e451'   # ### the papers` repository's last commit before Component 4: ERRATA's four entries, [F2]-[F5] and [R3] (step 35, events (63))
BLOCK = os.path.join(D, 'b769_registry_block.json')
C3 = os.path.join(D, 'b769_ledgers_c3.json')
BANK, BJSON = os.path.join(D, 'b769_waves.txt'), os.path.join(D, 'b769_waves.json')
WAVES = (R66.DAY1, R66.P1_2, R66.P1_5)
WANT = {R66.DAY1: 8, R66.P1_2: 6, R66.P1_5: 6}
KROOT = 'D:/'   # ### the kernels' clones, each at the data volume's root by its name (tools/standing/commit.py KERNELS)
KN = r'(SIDE-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)'
REF = r'(v\d+(?:\.\d+)*|(?=[0-9]*[a-f])[0-9a-f]{7,40})(?![\w]|\.\d)'
PIN1 = re.compile(KN + r"`?(?:’s|'s)?[ \t]*(?:(?:,|@|=|\(|\bat\b|\btag\b)[ \t]*){0,2}`?" + REF)
PIN2 = re.compile(r'(?<![\w.])`?(v\d+(?:\.\d+)*)`?[ \t]+(?:of|on|in)[ \t]+`?' + KN + r'(?![A-Za-z0-9-])')
VER = re.compile(r'\bv?\d+(?:\.\d+)+[a-z]?\b')
PLANT_ROW = '| planted | `zz_b769_planted_decl` | SIDE-planted |'


def names_file(text, path):
    return bool(path) and (path in text or R66.names_it(text, None, path))


def safe(text, I, qw, acct):
    return sum(v for v in RU.idcount(text, I, acct).values() if v > 0) == 0 and ER.qcount(text, qw) == 0


# ================================================================================ THE KERNELS
_TAGS, _HEADS = {}, {}


def clone(k):
    p = KROOT + k
    return p if re.fullmatch(r'SIDE-[A-Za-z0-9-]+', k) and os.path.isdir(os.path.join(p, '.git')) else None


def tags_of(k):
    """[(name, peeled commit)] in creation order, as the clone reads them."""
    if k not in _TAGS:
        p = clone(k)
        out = []
        if p:
            t = git(p, 'for-each-ref', 'refs/tags', '--sort=creatordate', '--format=%(refname:short) %(objecttype) %(*objectname) %(objectname)')
            for l in t.split(NL):
                x = l.split()
                if len(x) == 4:
                    out.append((x[0], x[2]))
                elif len(x) == 3:
                    out.append((x[0], x[2]))
        _TAGS[k] = out
    return _TAGS[k]


def head_of(k):
    if k not in _HEADS:
        p = clone(k)
        _HEADS[k] = git(p, 'rev-parse', 'HEAD').strip() if p else None
    return _HEADS[k]


def read_pin(k, ref):
    p = clone(k)
    if not p:
        return 'NO CLONE', None
    tg = tags_of(k)
    if not tg:
        return 'THE CLONE CARRIES NO TAG', None
    newest, peeled = tg[-1]
    if ref.startswith('v'):
        if ref == newest:
            return 'CURRENT', newest
        if ref in [n for n, _c in tg]:
            return 'STALE', newest
        return 'NOT A TAG OF THE CLONE', newest
    r = subprocess.run(['git', '-C', p, 'rev-parse', '--verify', '--quiet', ref + '^{commit}'], capture_output=True)
    full = r.stdout.decode('utf-8', 'replace').strip()
    if r.returncode or not full:
        return 'NOT A COMMIT OF THE CLONE', newest
    if full == peeled:
        return 'CURRENT', newest
    a = subprocess.run(['git', '-C', p, 'merge-base', '--is-ancestor', full, peeled], capture_output=True).returncode
    return ('STALE', newest) if a == 0 else ('NEITHER THE NEWEST TAG`S COMMIT NOR BEHIND IT', newest)


def pins_of(texts):
    """texts: [(where, text)]; the pins in reading order, each (kernel, ref, where) once by (kernel, ref)."""
    out, seen = [], set()
    for where, t in texts:
        hits = [(m.start(), m.group(1), m.group(2)) for m in PIN1.finditer(t)] + [(m.start(), m.group(2), m.group(1)) for m in PIN2.finditer(t)]
        for _s, k, ref in sorted(hits):
            if (k, ref) not in seen:
                seen.add((k, ref))
                out.append((k, ref, where))
    return out


# ================================================================================ THE TERMINAL TABLE
def ttable():
    b = git(RELAY, 'show', 'HEAD:data/terminal_table.json', raw=True)
    if not b:
        die('THE TERMINAL TABLE NOT READ AT THE RELAY`S HEAD')
    blob = git(RELAY, 'rev-parse', 'HEAD:data/terminal_table.json').strip()
    J = json.loads(b.decode('utf-8'))
    decls, seen, heads = [], {}, {}
    for x in J['rows']:
        heads.setdefault(x['repo'], set()).add(x.get('head'))
        k = (x['repo'], x['name'])
        pa = list(x.get('present_at') or [])
        if k in seen:
            d = decls[seen[k]]
            d['present_at'] = sorted(set(d['present_at']) | set(pa))
            continue
        seen[k] = len(decls)
        decls.append(dict(repo=x['repo'], name=x['name'], present_at=pa))
    ix = {}
    for i, d in enumerate(decls):
        parts = d['name'].split('.')
        for j in range(len(parts)):
            ix.setdefault('.'.join(parts[j:]), set()).add(i)
    return dict(decls=decls, ix=ix, heads=heads, rows=len(J['rows']), blob=blob[:16], sha=sha(b)[:16])


def corr_names(Dl):
    secs = B56.sections(Dl)
    names, seen = [], set()
    for a, b in secs:
        for i in range(a, b + 1):
            if i in seen or i - 1 >= len(Dl):
                continue
            seen.add(i)
            if B56.is_row(Dl[i - 1]):
                for n in B56.terminal_names(Dl[i - 1]):
                    if n not in names:
                        names.append(n)
    return names, secs


def join6(names, TT):
    decls, ix = TT['decls'], TT['ix']
    at, tag, absent = [], [], []
    for n in names:
        s = ix.get(n, set())
        if not s:
            absent.append(n)
        elif any('HEAD' in decls[i]['present_at'] for i in s):
            at.append(n)
        else:
            tag.append(n)
    P = J66.join(decls, names, [])['P'] if names else set()
    kern = sorted(set(decls[i]['repo'] for n in names for i in ix.get(n, set())))
    return dict(names=len(names), at_head=len(at), not_=len(tag) + len(absent), tag_only=len(tag), absent=len(absent), declared=len(P),
                kernels=kern, absent_names=absent[:6], tag_names=tag[:6])


# ================================================================================ THE REGISTRY'S CELLS AND TITLES
def cell_lines(L, P, info):
    """{id: [REGISTRY line]} over b720's block, b761's block and b769's first table: the rows that read it."""
    h69 = [k for k, l in enumerate(L, 1) if l.startswith(R69.BLOCK_HEAD)]
    if len(h69) != 1:
        die('b769`S BLOCK NOT READ ONCE (%s)' % h69)
    sec2 = next((k for k in range(h69[0], len(L) + 1) if L[k - 1].startswith('| row | THE PHASE BY SUBJECT')), None)
    if not sec2:
        die('b769`S SECOND TABLE NOT READ')
    out, prot = {}, []
    for a, b in ((info['stop'], info['b761'] - 1), (info['b761'], h69[0] - 1), (h69[0], sec2 - 1)):
        for k in range(a, b + 1):
            m = re.match(r'^\| (?:### \*\*)?`([^`]+)`', L[k - 1])
            if not m or R61.NYR.match(L[k - 1]):
                continue
            if k in P:
                prot.append(k)
                continue
            out.setdefault(m.group(1), []).append(k)
    return out, prot, h69[0]


def titles(L, P):
    th = [k for k, l in enumerate(L, 1) if l.startswith(R66.TITLES)]
    if len(th) != 1:
        die('THE RATIFIED PUBLIC TITLES NOT READ ONCE (%s)' % th)
    end = next((k for k in range(th[0] + 1, len(L) + 1) if re.match(r'^##\s', L[k - 1])), len(L) + 1)
    out, prot = [], []
    for i in range(th[0] + 1, end):
        l = L[i - 1]
        if not l.startswith('|') or re.match(r'^\|[\s:|-]+\|?\s*$', l):
            continue
        if i in P:
            prot.append(i)
            continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 5 or c[1].lower().startswith('internal file'):
            continue
        out.append(dict(line=i, file=c[1].strip('`* '), id=c[2].strip('`* '), title=c[3]))
    return out, prot, th[0]


def version(Dl):
    h2 = next((k for k, l in enumerate(Dl, 1) if l.startswith('## ')), len(Dl) + 1)
    for k in range(1, min(h2, 81)):
        p = R61.plain(Dl[k - 1])
        m = re.search(r'(?i)\bversion\b', p)
        if m:
            v = VER.search(p[m.end():])
            if v:
                return k, v.group(0), p
        elif re.match(r'^v\d+(?:\.\d+)+\b', p):
            return k, VER.match(p).group(0), p
    return None


def record_ids(line):
    ids = []
    for m in re.finditer(r'(?<![\w.])(\d{7,9})(?![\w])', line):
        ctx = line[max(0, m.start() - 40):m.start()].lower()
        if any(w in ctx for w in ('zenodo', 'record', 'concept', 'doi', 'deposit')) and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


# ================================================================================ ONE ROW
def read_row(r, wave, X):
    Dl, path = r['kdoc'] or [], r['path']
    I, qw, acct, L, P = X['I'], X['qw'], X['acct'], X['L'], X['P']
    o = dict(id=r['id'], wave=wave, path=path, reg_line=r['line'])
    # (i)
    o['title_line'] = r['title_line']
    o['title'] = r['title']
    o['title_cite'] = r['title_cite']
    v = version(Dl)
    if v and safe(v[2], I, qw, acct):
        o['version'] = dict(line=v[0], number=v[1], text=v[2][:160])
    elif v:
        o['version'] = dict(line=v[0], number=v[1], text='cited by line and digest alone (sha256 %s)' % sha(Dl[v[0] - 1])[:16])
    else:
        o['version'] = None
    # (ii)
    keys = set(l.strip() for l in Dl if len(l.strip()) >= 40)
    held = dict((rel, len(keys & X['FS'][rel])) for rel in X['files'])
    copies = [rel for rel in X['files'] if keys and held[rel] >= ER.COPY_SHARE * len(keys)]
    o['keys'] = len(keys)
    o['deposited'] = [(rel, held[rel]) for rel in copies if rel.startswith(ER.DEP)]
    o['other_copies'] = [(rel, held[rel]) for rel in copies if not rel.startswith(ER.DEP)]
    o['record_ids'] = record_ids(L[r['line'] - 1]) if r['line'] not in P else None
    # (iii)
    ents = [(h, eid) for h, eid, txt in X['entries'] if names_file(txt, path)]
    facts = [k for k in X['facts'] if names_file(X['OL'][k - 1], path)]
    o['errata'] = [eid for _h, eid in ents]
    o['errata_act'] = [eid for h, eid in ents if h in X['act_e']]
    o['facts'] = facts
    o['facts_act'] = [k for k in facts if k in X['act_f']]
    # (iv)
    o['orders'] = sorted(set(n for _k, ns, l in X['olines'] if names_file(l, path) for n in ns))
    # (v)
    h2 = next((k for k, l in enumerate(Dl, 1) if l.startswith('## ')), len(Dl) + 1)
    texts = [('its head :%d' % k, Dl[k - 1]) for k in range(1, h2)] + [('REGISTRY :%d' % k, L[k - 1]) for k in X['cells'].get(r['id'], [])]
    pins = []
    for k, ref, where in pins_of(texts):
        st, newest = read_pin(k, ref)
        pins.append(dict(kernel=k, ref=ref, where=where, state=st, newest=newest))
    o['pins'] = pins
    o['cells_at'] = X['cells'].get(r['id'], [])
    # (vi)
    names, secs = corr_names(Dl)
    j = join6(names, X['TT'])
    o['corr'] = dict(sections=len(secs), **dict((k, v) for k, v in j.items()))
    o['kernel_heads'] = []
    for k in j['kernels']:
        th = sorted(x for x in X['TT']['heads'].get(k, set()) if x)
        now = head_of(k)
        rel = 'NO CLONE' if not now else ('EQUAL' if any(now.startswith(x) for x in th) else 'DIFFERS')
        if rel == 'DIFFERS' and len(th) == 1:
            a = subprocess.run(['git', '-C', clone(k), 'merge-base', '--is-ancestor', th[0], now], capture_output=True).returncode
            rel = 'THE TABLE`S HEAD BEHIND THE CLONE`S' if a == 0 else 'DIFFERS, NOT BEHIND'
        o['kernel_heads'].append(dict(kernel=k, table=th, clone=(now or '')[:12], reading=rel))
    # (vii)
    t = [x for x in X['titles'] if x['id'] == r['id']] or [x for x in X['titles'] if path and x['file'] == path.split('/')[-1]]
    if t and safe(t[0]['title'], I, qw, acct):
        pt = t[0]['title']
        eq = r['title'] is not None and re.sub(r'[\s*_~]+', ' ', pt).strip().lower() == re.sub(r'[\s*_~]+', ' ', r['title']).strip().lower()
        o['public'] = dict(line=t[0]['line'], title=pt[:240], by='its ID cell' if t[0]['id'] == r['id'] else 'its file cell', equal=eq, rows=len(t))
    elif t:
        o['public'] = dict(line=t[0]['line'], title='cited by line and digest alone (sha256 %s)' % sha(L[t[0]['line'] - 1])[:16], by='', equal=None, rows=len(t))
    else:
        o['public'] = None
    o['flag'] = list(r['flag'] or [])
    return o


# ================================================================================ THE BANK
def block(o):
    out = ['## %s (%s) %s, REGISTRY :%d' % (o['id'], o['wave'], o['path'], o['reg_line'])]
    tl = ('title :%d "%s"' % (o['title_line'], o['title'])) if o['title'] else ('title %s' % o['title_cite'] if o['title_cite'] else 'no title line read')
    vl = ('version :%d %s, the line "%s"' % (o['version']['line'], o['version']['number'], o['version']['text'])) if o['version'] else 'no version line in its head'
    out.append('  (i)   %s ; %s' % (tl, vl))
    dp = '; '.join('%s (%d of %d)' % (rel, h, o['keys']) for rel, h in o['deposited']) or 'none'
    oc = '; '.join('%s (%d of %d)' % (rel, h, o['keys']) for rel, h in o['other_copies']) or 'none'
    ri = ('the record REGISTRY names for it %s (its row`s line)' % (', '.join(o['record_ids']) if o['record_ids'] else 'none named on its row`s line')
          if o['record_ids'] is not None else 'its row`s line protected, not read')
    out.append('  (ii)  deposited copies %d: %s ; copies outside the DEPOSITED folders %d (a reading): %s ; %s' % (
        len(o['deposited']), dp, len(o['other_copies']), oc, ri))
    out.append('  (iii) ERRATA entries naming its file %d%s, this act`s %d%s ; fact items %d%s, this act`s %d' % (
        len(o['errata']), (' (%s)' % ', '.join(o['errata'])) if o['errata'] else '', len(o['errata_act']),
        (' (%s)' % ', '.join(o['errata_act'])) if o['errata_act'] else '', len(o['facts']),
        (' (OPEN_TRAILS :%s)' % ', :'.join(str(k) for k in o['facts'])) if o['facts'] else '', len(o['facts_act'])))
    out.append('  (iv)  orders not closed naming it %d%s' % (len(o['orders']), (': ' + ', '.join(o['orders'])) if o['orders'] else ''))
    if o['pins']:
        out.append('  (v)   kernel pins %d (cells read at %s): %s' % (len(o['pins']), ', '.join('REGISTRY :%d' % k for k in o['cells_at']) or 'no cell row',
                   '; '.join('%s %s (%s) %s beside %s' % (p['kernel'], p['ref'], p['where'], p['state'], p['newest']) for p in o['pins'])))
    else:
        out.append('  (v)   kernel pins 0 (cells read at %s)' % (', '.join('REGISTRY :%d' % k for k in o['cells_at']) or 'no cell row'))
    c = o['corr']
    kh = '; '.join('%s: the table read %s, the clone`s HEAD %s, %s' % (x['kernel'], '/'.join(y[:12] for y in x['table']), x['clone'], x['reading'])
                   for x in o['kernel_heads']) or 'no kernel named'
    out.append('  (vi)  Correspondence sections %d: names %d ; AT HEAD %d ; NOT %d (naming none %d%s, at a tag only %d%s) ; declarations named by '
               'b766`s join %d ; %s' % (c['sections'], c['names'], c['at_head'], c['not_'], c['absent'],
                                         (' %s' % ', '.join('`%s`' % n for n in c['absent_names'])) if c['absent_names'] else '', c['tag_only'],
                                         (' %s' % ', '.join('`%s`' % n for n in c['tag_names'])) if c['tag_names'] else '', c['declared'], kh))
    pb = o['public']
    pt = ('"%s" (REGISTRY :%d, by %s; %s)' % (pb['title'], pb['line'], pb['by'], 'EQUAL to its title line' if pb['equal'] else 'DIFFERS from its title line')
          if pb and pb['by'] else ('%s (REGISTRY :%d)' % (pb['title'], pb['line']) if pb else 'no row of the table'))
    out.append('  (vii) ratified public title %s ; title flag %s' % (pt, ', '.join(o['flag']) if o['flag'] else 'none'))
    return out


def counts(rows):
    c = dict(rows=len(rows), with_deposited=sum(1 for o in rows if o['deposited']), deposited=sum(len(o['deposited']) for o in rows),
             errata=sum(len(o['errata']) for o in rows), errata_act=sum(len(o['errata_act']) for o in rows),
             facts=sum(len(o['facts']) for o in rows), facts_act=sum(len(o['facts_act']) for o in rows),
             orders_sum=sum(len(o['orders']) for o in rows), orders=len(set(n for o in rows for n in o['orders'])),
             current=sum(1 for o in rows for p in o['pins'] if p['state'] == 'CURRENT'), stale=sum(1 for o in rows for p in o['pins'] if p['state'] == 'STALE'),
             pins_other=sum(1 for o in rows for p in o['pins'] if p['state'] not in ('CURRENT', 'STALE')),
             names=sum(o['corr']['names'] for o in rows), at_head=sum(o['corr']['at_head'] for o in rows), not_=sum(o['corr']['not_'] for o in rows),
             public=sum(1 for o in rows if o['public']), flagged=sum(1 for o in rows if o['flag']))
    return c


def count_line(name, c):
    return ('  %-18s rows %d ; deposited copies %d (rows with one %d) ; ERRATA entries naming them %d (this act`s %d) and fact items %d (this act`s %d), '
            'together %d ; orders not closed naming them %d (by row %d) ; kernel pins CURRENT %d, STALE %d, other %d ; declarations named %d, AT HEAD %d, '
            'NOT %d ; ratified public titles read beside title lines %d, flagged %d') % (
        name, c['rows'], c['deposited'], c['with_deposited'], c['errata'], c['errata_act'], c['facts'], c['facts_act'], c['errata'] + c['facts'],
        c['orders'], c['orders_sum'], c['current'], c['stale'], c['pins_other'], c['names'], c['at_head'], c['not_'], c['public'], c['flagged'])


# ================================================================================ THE RUN
def run(mode):
    at = utc()
    head = git(PP, 'rev-parse', 'HEAD').strip()
    rhead = git(RELAY, 'rev-parse', 'HEAD').strip()
    B = jload(BLOCK)
    KP = B['keystones_by_phase']
    R = R69.reading()
    L, P, info, I, qw = R['L'], R['P'], R['info'], R['I'], R['qw']
    acct = RU.account()
    byid = dict((r['id'], r) for r in R['rows'])
    files, FL = ER.outputs()
    FS = dict((rel, set(l.strip() for l in FL[rel])) for rel in files)
    out_clean = git(PP, 'status', '--porcelain', '--', 'outputs').strip() == ''
    EL = ER.show('HEAD', 'ERRATA.md') or []
    eh = [k for k, l in enumerate(EL, 1) if l.startswith('## E-')]
    entries = []
    for h in eh:
        e = next((k for k in range(h + 1, len(EL) + 1) if EL[k - 1].startswith('## ')), len(EL) + 1)
        entries.append((h, EL[h - 1][3:].split()[0], NL.join(EL[h - 1:e - 1])))
    OL = OR.trail('HEAD')
    facts = [k for k, l in enumerate(OL, 1) if 'FACT ITEM' in l]
    c3 = jload(C3)['entered']
    act_e = set(v[1] for k, v in c3.items() if v[0] == 'ERRATA')
    act_f = set(v[1] for k, v in c3.items() if v[0] == 'OPEN_TRAILS' and k.startswith('F'))
    ordrows = OR.read(OL)
    notclosed = set(n for n, o in ordrows if o['status'] != 'CLOSED')
    olines = []
    for k, l in enumerate(OL, 1):
        if l.lstrip().startswith(OR.ROLL):
            continue
        ns = set(OR.NAME.findall(l)) & notclosed
        if ns:
            olines.append((k, ns, l))
    cells, cprot, h69 = cell_lines(L, P, info)
    TI, tprot, th = titles(L, P)
    TT = ttable()
    X = dict(I=I, qw=qw, acct=acct, L=L, P=P, files=files, FS=FS, entries=entries, OL=OL, facts=facts, act_e=act_e, act_f=act_f, olines=olines,
             cells=cells, titles=TI, TT=TT)
    rows = []
    for w in WAVES:
        for rid in KP.get(w, []):
            r = byid.get(rid)
            if r is None:
                die('THE KEYSTONE %s NOT AMONG THE ROWS READ AT HEAD' % rid)
            rows.append(read_row(r, w, X))
    # ### THE CONTROLS
    ks_now = [(w, rid, byid[rid]['cell'], byid[rid]['phase']) for w in WAVES for rid in KP.get(w, [])]
    c1 = all(len(KP.get(w, [])) == WANT[w] for w in WAVES) and all(cell == R66.KEY and ph == w for w, _rid, cell, ph in ks_now)
    ef = tags_of('SIDE-explicit-formula')
    parent = git(clone('SIDE-explicit-formula'), 'rev-parse', ef[-1][1] + '~1').strip() if ef else ''
    plant = ['# Planted', 'Pinned to SIDE-explicit-formula at %s.' % ef[0][0], 'Beside it `SIDE-explicit-formula` %s.' % ef[-1][0],
             'Its commit SIDE-explicit-formula @ %s.' % ef[-1][1][:8], 'Its parent SIDE-explicit-formula @ %s.' % parent[:8], '## body']
    pp_ = pins_of([('planted :%d' % k, plant[k - 1]) for k in range(1, 6)])
    pst = [read_pin(k, ref)[0] for k, ref, _w in pp_]
    c2 = pst == ['STALE', 'CURRENT', 'CURRENT', 'STALE']
    host = next((o for o in rows if o['corr']['names'] and o['corr']['sections']), None)
    if host:
        Dl = byid[host['id']]['kdoc']
        a = B56.sections(Dl)[0][0]
        Dp = Dl[:a] + [PLANT_ROW] + Dl[a:]
        j0, j1 = join6(corr_names(Dl)[0], TT), join6(corr_names(Dp)[0], TT)
        c3_ = (j1['not_'] - j0['not_'], j1['at_head'] - j0['at_head'], j1['names'] - j0['names'], j1['absent'] - j0['absent']) == (1, 0, 1, 1)
        c3t = 'in %s`s first Correspondence section (:%d): NOT %d to %d, AT HEAD %d to %d, names %d to %d' % (
            host['id'], a, j0['not_'], j1['not_'], j0['at_head'], j1['at_head'], j0['names'], j1['names'])
    else:
        c3_, c3t = False, 'no keystone with a Correspondence table to plant in'
    ctl = [('list (1)`s ids 8, 6 and 6, each KEYSTONE in its phase at HEAD: %s' % ', '.join('%s %d' % (w, len(KP.get(w, []))) for w in WAVES), c1),
           ('a planted head pinning SIDE-explicit-formula at %s, %s, its commit %s and that commit`s parent %s reads %s' % (
               ef[0][0], ef[-1][0], ef[-1][1][:8], parent[:8], pst), c2),
           ('a planted row naming a declaration absent from the terminal table moves NOT by one and AT HEAD by none: %s' % c3t, c3_),
           ('the papers` repository at HEAD %s, the act`s last commit there before this component %s; its outputs/ clean against HEAD (%s, files %d)' % (
               head[:8], C4PP, out_clean, len(files)), head.startswith(C4PP) and out_clean),
           ('the terminal table read at the relay`s HEAD %s by git show (blob %s, sha256 %s, rows %d, declarations %d), the working file not read' % (
               rhead[:8], TT['blob'], TT['sha'], TT['rows'], len(TT['decls'])), TT['rows'] > 0)]
    # ### THE BANK
    lines = ['b769 -- (R379)(6): THE WAVES READ RECORD BY RECORD, a reading and no build (%s)' % at, '',
             '### tools/b769_waves.py %s; the papers` repository at HEAD %s; the relay at HEAD %s; the keystones of list (1) of (4)(a) from' % (mode, head[:8], rhead[:8]),
             '### data/b769_registry_block.json, each read again at HEAD by b766`s reading; no line of REGISTRY, of the census or of a paper written;',
             '### the lines of ERRATA, OPEN_TRAILS and REGISTRY read in memory, none printed but titles, version lines and public titles; rule [Q]`s lines',
             '### cited, never read: %d cell rows and %d title rows on protected lines (%s).' % (
                 len(cprot), len(tprot), ', '.join(':%d' % k for k in cprot + tprot) or 'none'), '',
             '## THE CONTROLS']
    for t, ok in ctl:
        lines.append('  %-150s %s' % (t, 'AS WANTED' if ok else 'NOT AS WANTED'))
    lines += ['', '## THE KERNELS NAMED, their newest tags as the clones read them']
    kk = sorted(set(p['kernel'] for o in rows for p in o['pins']) | set(x['kernel'] for o in rows for x in o['kernel_heads']))
    for k in kk:
        tg = tags_of(k)
        lines.append('  %s: %s ; tags %d ; HEAD %s' % (k, ('newest %s at %s' % (tg[-1][0], tg[-1][1][:8])) if tg else 'no tag or no clone', len(tg), (head_of(k) or 'no clone')[:8]))
    for w in WAVES:
        lines += ['', '# %s' % w]
        for o in rows:
            if o['wave'] == w:
                lines += block(o)
    C = dict((w, counts([o for o in rows if o['wave'] == w])) for w in WAVES)
    C['ALL'] = counts(rows)
    lines += ['', '## THE COUNTS BY WAVE']
    for w in WAVES + ('ALL',):
        lines.append(count_line(w if w != 'ALL' else 'IN ALL', C[w]))
    n = sum(1 for _t, ok in ctl if ok)
    lines += ['', '### ### **THE WAVES READ: ROWS %d (%s) ; DEPOSITED COPIES %d ; ERRATA ENTRIES AND FACT ITEMS NAMING THEM %d ; ORDERS NOT CLOSED %d ; '
              'PINS CURRENT %d, STALE %d ; DECLARATIONS %d, AT HEAD %d, NOT %d ; PUBLIC TITLES %d, FLAGGED %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
                  C['ALL']['rows'], ', '.join(str(C[w]['rows']) for w in WAVES), C['ALL']['deposited'], C['ALL']['errata'] + C['ALL']['facts'],
                  C['ALL']['orders'], C['ALL']['current'], C['ALL']['stale'], C['ALL']['names'], C['ALL']['at_head'], C['ALL']['not_'],
                  C['ALL']['public'], C['ALL']['flagged'], n, len(ctl), 'DRY, NOTHING WRITTEN' if mode == 'dry' else 'WRITTEN')]
    text = NL.join(lines) + NL
    J = dict(at=at, act=ACT, pp_head=head, relay_head=rhead, terminal_table=dict(blob=TT['blob'], sha=TT['sha'], rows=TT['rows'], decls=len(TT['decls'])),
             rows=rows, counts=C, controls=[[t, ok] for t, ok in ctl], protected=dict(cells=cprot, titles=tprot))
    jt = json.dumps(J, indent=1, ensure_ascii=False) + NL
    bad = [k for k, v in RU.idcount(text + jt, I, acct).items() if v > 0]
    if bad or ER.qcount(text + jt, qw) != 0:
        die('AN IDENTIFIER (%s) OR THE PROTECTED WORD IN THE COMPOSED BANK' % (', '.join(bad) or 'the protected word'))
    print(text)
    if mode == 'write':
        if n != len(ctl):
            die('CONTROLS %d OF %d' % (n, len(ctl)))
        put(BANK, text)
        put(BJSON, jt)
        print('written data/b769_waves.txt and .json')


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m not in ('dry', 'write'):
        sys.exit(__doc__)
    run(m)
