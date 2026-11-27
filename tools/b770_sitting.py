# -*- coding: utf-8 -*-
"""tools/b770_sitting.py -- b770, (R380)(7): THE SITTING OF THE TENTH ACT IN THE LIGHT FORM (Canon XXIII (C), THE_METHOD_CANON.md :374; the
author's ruling of 2026-11-26 amending (R371)(5), [A5] (i)). Carried from tools/b761_sitting.py (b761's agenda, question and inputs
routes), committed before its run, dry included.

  agenda dry|write             data/b770_sitting_agenda.txt and .json: one item for each FINDINGS entry from b761's to b769's that is no
                               corrigendum, each with its cluster, its keystone and its reading as b761's tool gives them
  question dry|write           data/b770_question.json, for `rootprompt.py put b770`: the items reading CLUSTERED and no other, passed whole or
                               struck by number; where no item reads CLUSTERED no question is composed and the tool says so
  inputs dry|write [--struck n,...]
                               data/b770_recut_inputs.txt: for each keystone the passed items it does not carry; the answer read from
                               data/b770_author_answers.txt (`fold.py record answers --act b770`, as b761's was), the struck numbers given by the
                               seat from the answer and each read in it

THE ITEMS: one for each FINDINGS heading (`## `) after `## Corrigendum to b760` that is no corrigendum, each the act whose corrigendum is the
next after it, b761 to b769, in the entries' order, numbered: its heading by line and sha256 (no line of a paper quoted in a relay bank) and
its names as tools/standing/linematch.py reads them; its cluster and that cluster's keystone, read from REGISTRY's rows and SPIRAL_MAP's
cluster table (its head the one line opening `| Cluster |`, found at run time and printed) at the papers` repository's HEAD; for each name,
whether the keystone's text at HEAD carries it; and the item's reading, one of three:
  SYNTHESISED                                   the keystone carries a name of the entry
  CLUSTERED, AN INPUT OF THAT KEYSTONE'S RE-CUT  the cluster names a keystone that carries none
  BANKED, NO SEAT                               the maps name no cluster
THE CLUSTER by b761's four rules (R1)-(R4), each item printing the rule that placed it (tools/b761_sitting.py :18-:22). b761's orders section
and the navigator's recommendation are not carried: the light form asks the author about the second reading's items alone.
THE SECOND SHAPE (b770, the agenda's first dry, 01:44:40Z: the maps' rules read all nine items BANKED, NO SEAT, five of whose own
INTEGRATION lines name the cluster The Epstein instance, its keystone and the stage CLUSTERED; the rules read a heading alone and seat no
entry whose banks no map row or keystone yet names): each item's own INTEGRATION line read for its cluster, keystone and stage beside the
maps' reading, which stays the reading as b761's tool gives it; the items CLUSTERED by either shape are the ones put to the author, the two
readings' conflict named in the question; a planted heading and a planted own line show that the second reading can fire.

No keystone, map or FINDINGS line is written; no line of the papers` repository is printed but the names, the cluster's label and the stage
words; the protected word neither printed nor stored; no git write.
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
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import linematch as LM      # noqa: E402
import b761_registry as RG  # noqa: E402
import b770_worklist as K   # noqa: E402

ACT, NL = 'b770', '\n'
PP = K.PP
AGENDA = os.path.join(D, 'b770_sitting_agenda.txt')
AJSON = os.path.join(D, 'b770_sitting_agenda.json')
QJSON = os.path.join(D, 'b770_question.json')
INPUTS = os.path.join(D, 'b770_recut_inputs.txt')
ANSWERS = 'data/b770_author_answers.txt'
ACTS = tuple('b%d' % n for n in range(761, 770))
FROM = '## Corrigendum to b760'
CT_MARK = '| Cluster |'
Q_OPEN = 'The sitting of the tenth act under (R380)(7)'
PASS, STRIKE = 'Passed whole', 'Strike by number'
READINGS = ('SYNTHESISED', 'CLUSTERED, AN INPUT OF THAT KEYSTONE`S RE-CUT', 'BANKED, NO SEAT')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def show(path):
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + path], capture_output=True)
    if r.returncode:
        die('%s NOT AT HEAD' % path)
    t = r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL)
    return t[:-1] if t and t[-1] == '' else t


def relay_lines(rel):
    with open(os.path.join(RELAY, rel), encoding='utf-8') as f:
        return f.read().replace('\r', '').split(NL)


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


STEM = re.compile(r'([A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+)(?:\.md)?')


def stems(cell):
    out = []
    for m in STEM.finditer(cell):
        s = re.sub(r'(_v\d+(?:_\d+)*)$', '', m.group(1))
        if len(s) > 6 and s not in out:
            out.append(s)
    return out


def needles(h):
    nm = LM.names(h)
    up = [x for x in dict.fromkeys(re.findall(r'\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b', h)) if len(x) > 3]
    ker = list(dict.fromkeys(re.findall(r'\b(SIDE-[a-z0-9-]*[a-z0-9]|zq-b\d+)', h)))
    rid = list(dict.fromkeys(re.findall(r'(?<![\w.])(\d\.\d[a-z]-\d+|d1-\d+|p2-\d+)\b', h)))
    return nm, up, ker, rid


def table_at(S):
    """(head line, first row, last row) of SPIRAL_MAP's cluster table: the one line opening `| Cluster |`, its rows the lines after its
    rule line that open `|`."""
    hd = [k for k, l in enumerate(S, 1) if l.startswith(CT_MARK)]
    if len(hd) != 1:
        die('SPIRAL_MAP CARRIES %d CLUSTER-TABLE HEADS (%s), NOT ONE' % (len(hd), hd))
    k = hd[0] + 2
    while k <= len(S) and S[k - 1].startswith('|'):
        k += 1
    return hd[0], hd[0] + 2, k - 1


def cluster_table(S, first, last):
    files = [f for f in subprocess.run(['git', '-C', PP, 'ls-files'], capture_output=True).stdout.decode('utf-8').split(NL)
             if f and not f.startswith('archive/')]   # ### an archived copy is no keystone

    def resolve(x):
        if x.endswith('.md'):
            return [x] if x in files else [f for f in files if f.rsplit('/', 1)[-1] == x.rsplit('/', 1)[-1]]
        s = re.sub(r'(_v\d+(?:_\d+)*)$', '', x)
        return [f for f in files if f.endswith('.md') and re.sub(r'(_v\d+(?:_\d+)*)$', '', f.rsplit('/', 1)[-1][:-3]) == s]
    out = []
    for k in range(first, last + 1):
        l = S[k - 1]
        m = re.match(r'^\| \*\*([^*]+)\*\*', l)
        if not m:
            continue
        c = l.split('|')
        kcell, scell = (c[2] if len(c) > 2 else ''), (c[3] if len(c) > 3 else '')
        anchor = re.search(r'ANCHOR\b[^`]*`([\w./\-]+)`', kcell)
        named = [anchor.group(1)] if anchor else (re.findall(r'`([\w./\-]+\.md)`', kcell) or stems(kcell))
        keys = [f for x in named for f in resolve(x)]
        ids = list(dict.fromkeys(re.findall(r'(?<![\w.])(\d\.\d[a-z]-\d+|p2-\d+|d1-\d+)\b', l)))
        out.append(dict(line=k, name=m.group(1).strip(), text=l, stems=stems(kcell + ' ' + scell), keys=list(dict.fromkeys(keys)), ids=ids))
    return out


def reg_rows(R):
    out = []
    for k, l in enumerate(R, 1):
        m = RG.ROW_ID.match(l)
        if m:
            c = [x.strip() for x in l.split('|')]
            out.append((m.group(1), k, c[3] if len(c) > 3 else ''))
    return out


def place(h, ct, rr, ktexts):
    nm, up, ker, rid = needles(h)
    hl = h.lower()
    found = []
    for row in ct:
        why = []
        a = [x for x in nm + up + ker + rid if x in row['text']]
        if a:
            why.append('R1 (the row carries %s)' % ', '.join(a))
        b = [s for s in row['stems'] if s.lower() in hl or s.replace('_', ' ').lower() in hl]
        if b:
            why.append('R2 (the heading carries %s)' % ', '.join(b))
        nd = nm + up + [x for x in ker if not x.startswith('SIDE-')]
        via = [(i, k) for i, k, f in rr if (i in rid) or any(x in f for x in nd)]
        c = sorted(set(i for i, _k in via if i in row['ids']))
        if c:
            ns = sorted(set(x for i, _k, f in rr if i in c for x in nd if x in f))
            why.append('R3 (REGISTRY rows %s, by %s, named by the row)' % (', '.join(c), ', '.join(ns) or 'their ids'))
        kn = set()
        for kp in row['keys']:
            kn |= set(ktexts[kp][1])
        d = [x for x in nm if x in kn]
        if d:
            why.append('R4 (its keystone carries %s)' % ', '.join(d))
        if why:
            found.append((row, why))
    return found


def carried(name, KL):
    at = [k for k, l in enumerate(KL, 1) if name in LM.names(l)]
    occ = r'(?<![\w`.-])`?' + re.escape(name) + r'`?(?![\w-])'
    pth = r'/' + re.escape(name) + r'\.[a-z]'
    path = bool(at) and all(len(re.findall(pth, KL[k - 1])) == len(re.findall(occ, KL[k - 1])) for k in at)
    return at, path


OWN = re.compile(r'^INTEGRATION: cluster (.+?) ; keystone (.+?) ; stage (.+?)\s*$')


def reads_of(htext, ct, rr, ktexts):
    """the item's reads by b761's rules: [dict(cluster, row, why, keys, per, reading, path_only)], and the reading the highest of them gives."""
    nm = LM.names(htext)
    reads = []
    for row, why in place(htext, ct, rr, ktexts):
        keys = row['keys']
        per = [(kp, [(x,) + carried(x, ktexts[kp][0]) for x in nm]) for kp in keys]
        hit = [(kp, x, at, p) for kp, rows in per for x, at, p in rows if at]
        rd = 'CLUSTERED, NO KEYSTONE NAMED' if not keys else ('SYNTHESISED' if hit else READINGS[1])
        reads.append(dict(cluster=row['name'], row=row['line'], why=why, keys=keys, per=per, reading=rd,
                          path_only=bool(hit) and all(p for _k, _x, _a, p in hit)))
    if not reads:
        return reads, READINGS[2], None
    cl = sorted(reads, key=lambda r: 0 if r['reading'] == 'SYNTHESISED' else 1)[0]
    return reads, cl['reading'], cl


def own_reading(line, nm, ct, ktexts):
    """THE SECOND SHAPE, printed beside the maps' reading and deciding nothing by itself (b770, the agenda's first dry, 01:44:40Z: the maps'
    rules read all nine items BANKED, five of whose own INTEGRATION lines name the cluster The Epstein instance and its keystone at stage
    CLUSTERED): the entry's own line's cluster, keystone and stage; the cluster found among the table's rows by name, the line's keystone
    among that row's keystones; the keystone's text read for the entry's names; its reading by the line's stage, SYNTHESISED where the
    keystone carries a name of the entry."""
    m = OWN.match(line or '')
    if not m:
        return None
    cn, kp, stg = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
    rows = [r for r in ct if r['name'].strip().lower() == cn.lower()]
    row = rows[0] if len(rows) == 1 else None
    kt = ktexts.get(kp)
    at = [x for x in nm if kt and carried(x, kt[0])[0]]
    if stg.startswith('CLUSTERED') and row and kp in row['keys']:
        rd = 'SYNTHESISED' if at else READINGS[1]
    elif stg.startswith('SYNTHESISED') and at:
        rd = 'SYNTHESISED'
    else:
        rd = READINGS[2]
    return dict(cluster=cn, keystone=kp, stage=stg, row=row['line'] if row else None, key_of_row=bool(row) and kp in row['keys'],
                carried=at, reading=rd)


def headings(F):
    """(the corrigendum to b760's lines, the item headings, their acts): the non-corrigendum `## ` headings after `## Corrigendum to b760`,
    each the act whose corrigendum is the next after it."""
    c0 = [k for k, l in enumerate(F, 1) if l.startswith(FROM)]
    if not c0:
        return c0, [], []
    s = c0[0]
    hs = [k for k in range(s + 1, len(F) + 1) if F[k - 1].startswith('## ') and not F[k - 1].startswith('## Corrigendum')]
    cs = [(k, m.group(1)) for k in range(s + 1, len(F) + 1) for m in [re.match(r'^## Corrigendum to (b\d+)', F[k - 1])] if m]
    return c0, hs, [next((a for k, a in cs if k > h), None) for h in hs]


# ================================================================================ THE AGENDA
def agenda(mode):
    F, S, R = show('FINDINGS.md'), show('SPIRAL_MAP.md'), show('REGISTRY.md')
    I = RG.ids()
    qw = RG.qword(R)
    head = subprocess.run(['git', '-C', PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True).stdout.decode().strip()
    c0, hs, acts = headings(F)
    cth, ctf, ctl_ = table_at(S)
    ct = cluster_table(S, ctf, ctl_)
    rr = reg_rows(R)
    ktexts = {}
    for row in ct:
        for kp in row['keys']:
            if kp not in ktexts:
                KL = show(kp)
                ktexts[kp] = (KL, LM.names(NL.join(KL)))
    items = []
    for n, (h, a) in enumerate(zip(hs, acts), 1):
        nxt = min([k for k in hs if k > h] or [len(F) + 1])
        il = next((k for k in range(h + 1, nxt) if F[k - 1].startswith('INTEGRATION:')), None)
        st = re.search(r'stage ([A-Z]+(?: \([^)]*\))?(?:, [A-Z]+ \([^)]*\))?)\s*$', F[il - 1]) if il else None
        nm = LM.names(F[h - 1])
        reads, reading, cl = reads_of(F[h - 1], ct, rr, ktexts)
        own = own_reading(F[il - 1] if il else '', nm, ct, ktexts)
        items.append(dict(n=n, act=a, line=h, sha=sha(F[h - 1]), names=nm, iline=il, isha=sha(F[il - 1]) if il else None,
                          istage=(st.group(1) if st else ('a tally, no stage word' if il else 'none')), reads=reads, reading=reading,
                          cluster=cl['cluster'] if cl else None, crow=cl['row'] if cl else None, keys=cl['keys'] if cl else [],
                          path_only=cl['path_only'] if cl else False, several=len(reads) > 1, own=own,
                          differ=bool(own) and own['reading'] != reading))
    cnt = dict((r, sum(1 for i in items if i['reading'].startswith(r))) for r in ('SYNTHESISED', 'CLUSTERED', 'BANKED'))
    P = ['%s -- (R380)(7): THE SITTING OF THE TENTH ACT IN THE LIGHT FORM, ITS AGENDA BANKED BEFORE ANY QUESTION IS PUT (%s)' % (ACT, utc()), '',
         '### tools/b770_sitting.py agenda %s; the papers` repository at HEAD %s; REGISTRY, SPIRAL_MAP`s cluster table (:%d, its rows :%d-:%d),' % (
             mode, head, cth, ctf, ctl_),
         '### FINDINGS and the keystones read at HEAD; each heading by its line and sha256, no line of a paper quoted; the names as',
         '### tools/standing/linematch.py reads them; the cluster by b761`s rules R1-R4 (tools/b761_sitting.py :18-:22), the rule that placed each',
         '### item printed; a row`s keystone the documents its keystone cell names by path, else by stem, copies under archive/ set aside, and',
         '### where the cell names its ANCHOR the anchor alone; no keystone, map or FINDINGS line written at this sitting.', '',
         '## THE CLUSTER TABLE (SPIRAL_MAP :%d-:%d): cluster rows %d; the keystones it names by path or by stem read: %s' % (
             cth, ctl_, len(ct), ', '.join('%s (%d lines, %d names)' % (k, len(v[0]), len(v[1])) for k, v in ktexts.items()) or 'none'), '',
         '## THE ITEMS (FINDINGS entries b761 to b769 that are no corrigendum, in their order; the corrigendum to b760 at FINDINGS :%s)' % (
             ', :'.join(str(k) for k in c0) or 'none')]
    item_at = {}
    for i in items:
        item_at[i['n']] = len(P) + 1
        P.append('  [%d] %s, FINDINGS :%d (sha256 %s): names %s' % (i['n'], i['act'], i['line'], i['sha'], ', '.join(i['names']) or 'none (the heading carries no name of the reader`s form)'))
        P.append('      its line as written: FINDINGS :%s (sha256 %s), stage %s' % (i['iline'], i['isha'], i['istage']))
        if not i['reads']:
            P.append('      cluster: no rule places it -- no seat in the cluster table ; keystone none yet')
        for r in i['reads']:
            P.append('      cluster: %s (SPIRAL_MAP :%d), by %s ; keystone %s' % (r['cluster'], r['row'], '; '.join(r['why']), ', '.join(r['keys']) or 'none named'))
            for kp, rows_ in r['per']:
                for x, at, p in rows_:
                    P.append('        %s: %s' % (x, ('carried at %s%s' % (', '.join(':%d' % k for k in at[:8]) + (' and %d more' % (len(at) - 8) if len(at) > 8 else ''),
                                                                         ', inside a relay path alone' if p else '')) if at else 'not carried'))
        note = ''
        if i['path_only']:
            note = ' -- carried as a relay path alone (a bank`s or a tool`s), which canon XXIV sends out of the paper at its re-cut'
        elif i['reading'].startswith('CLUSTERED') and not i['names']:
            note = ' -- the heading names the keystone`s own work and carries no name the reader takes'
        if i['several']:
            note += ' -- placed in %d clusters, the highest reading taken' % len(i['reads'])
        P.append('      READING: %s%s%s' % (i['reading'], (' (%s)' % ', '.join(i['keys'])) if i['reading'] == 'SYNTHESISED' else '', note))
        o = i['own']
        P.append('      BY ITS OWN LINE (the second shape, printed beside): %s' % (
            ('cluster %s (%s), keystone %s (%s), stage %s, its names carried by that keystone %s -> %s ; the maps` reading %s' % (
                o['cluster'], ('SPIRAL_MAP :%d' % o['row']) if o['row'] else 'not a row of the table', o['keystone'],
                'the row`s keystone' if o['key_of_row'] else 'not the row`s keystone', o['stage'], o['carried'] or 'none', o['reading'],
                'DIFFERS' if i['differ'] else 'AGREES')) if o else 'its line not of the form INTEGRATION: cluster ; keystone ; stage'))
    P.append('')
    clu = [i for i in items if i['reading'].startswith('CLUSTERED')]
    dif = [i for i in items if i['differ']]
    diff_at = len(P) + 1
    P.append('## THE TWO READINGS DIFFER AT %d ITEM(S): %s' % (len(dif), ', '.join('[%d] %s (the maps %s, its own line %s, %s)' % (
        i['n'], i['act'], i['reading'].split(',')[0], i['own']['reading'].split(',')[0], i['own']['cluster']) for i in dif) or 'none'))
    ask = [i for i in items if i['reading'].startswith('CLUSTERED') or (i['differ'] and i['own']['reading'].startswith('CLUSTERED'))]
    P.append('## THE ITEMS OF THE SECOND READING BY EITHER SHAPE, PUT TO THE AUTHOR AT ONE PROMPT ((R380)(7)), the readings` conflict named in it: %s' % (
        ', '.join('[%d] %s' % (i['n'], i['act']) for i in ask) or 'none -- no prompt is put'))
    P.append('')
    ep = [v for k, v in ktexts.items() if 'EPSTEIN' in k]
    ek = [k for k in ktexts if k.endswith('THE_EPSTEIN_CONTROL_OBJECT_v0_2.md')]
    pl_reads, pl_reading, pl_cl = reads_of('## b999_planted_x read for THE_EPSTEIN_CONTROL_OBJECT', ct, rr, ktexts)
    pl_own = own_reading('INTEGRATION: cluster %s ; keystone %s ; stage CLUSTERED' % (
        next((r['name'] for r in ct if ek and ek[0] in r['keys']), 'none'), ek[0] if ek else 'none'), ['b999_planted_x'], ct, ktexts)
    ctl = [('the corrigendum to b760 found once (FINDINGS :%s)' % (c0 or 'none'), len(c0) == 1),
           ('the headings: the non-corrigendum headings after it (%d), each before its act`s corrigendum, the acts b761 to b769 each at least once '
            'and in order (%s)' % (len(hs), ', '.join(a or '?' for a in acts)),
            bool(hs) and all(a in ACTS for a in acts) and set(acts) == set(ACTS) and acts == sorted(acts, key=lambda a: int(a[1:]))),
           ('each item`s own line found (%d of %d)' % (sum(1 for i in items if i['iline']), len(items)), all(i['iline'] for i in items)),
           ('the cluster table read: its head found once (:%d), rows %d (at least 9), the Epstein instance`s keystone read at HEAD' % (cth, len(ct)),
            len(ct) >= 9 and any(k.endswith('THE_EPSTEIN_CONTROL_OBJECT_v0_2.md') for k in ktexts)),
           ('the match`s positive control: pc_online read carried by the Epstein keystone, a planted name b999_planted not',
            any(carried('pc_online', v[0])[0] for v in ep) and not any(carried('b999_planted', v[0])[0] for v in ktexts.values())),
           ('the placement`s planted control: a heading naming nothing of the maps (b999_planted_bank) placed nowhere',
            not place('## b999_planted_bank read', ct, rr, ktexts)),
           ('THE SECOND READING CAN FIRE: a planted heading carrying the Epstein keystone`s stem placed by R2 in its row and read %s ; a planted '
            'own line naming that row and keystone at stage CLUSTERED read %s' % (pl_reading, pl_own['reading'] if pl_own else None),
            pl_reading == READINGS[1] and bool(pl_cl) and ek and ek[0] in pl_cl['keys'] and bool(pl_own) and pl_own['reading'] == READINGS[1]),
           ('each item`s own line read in the form INTEGRATION: cluster ; keystone ; stage (%d of %d)' % (
               sum(1 for i in items if i['own']), len(items)), all(i['own'] for i in items)),
           ('each item read one of the three readings (%s)' % (', '.join('[%d] %s' % (i['n'], i['reading']) for i in items
                                                                     if i['reading'] not in READINGS) or 'none outside them'),
            all(i['reading'] in READINGS for i in items))]
    text = NL.join(P)
    ctl.append(('the identifiers 0 and the protected word 0 in the bank', RG.idcount(text, I) == 0 and qw.lower() not in text.lower()))
    ok = all(o for _w, o in ctl)
    P.append('## THE CONTROLS')
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    ocnt = dict((r, sum(1 for i in items if i['own'] and i['own']['reading'].startswith(r))) for r in ('SYNTHESISED', 'CLUSTERED', 'BANKED'))
    P += ['', '### ### **THE AGENDA: ITEMS %d ; BY THE MAPS SYNTHESISED %d ; CLUSTERED, AN INPUT OF A RE-CUT %d ; BANKED, NO SEAT %d ; BY THEIR OWN '
          'LINES %d, %d, %d ; DIFFERING %d ; PUT TO THE AUTHOR %s ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(items), cnt['SYNTHESISED'], cnt['CLUSTERED'], cnt['BANKED'], ocnt['SYNTHESISED'], ocnt['CLUSTERED'], ocnt['BANKED'], len(dif),
              len(ask) or 'NONE', sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    foot_at = len(P)
    text = NL.join(P) + NL
    print(text)
    if mode == 'write':
        if not ok:
            die('A CONTROL NOT AS WANTED')
        put(AGENDA, text)
        put(AJSON, json.dumps(dict(at=utc(), act=ACT, pp_head=head, table=[cth, ctf, ctl_], items=[dict((k, v) for k, v in i.items() if k != 'reads') | dict(
            reads=[dict(cluster=r['cluster'], row=r['row'], why=r['why'], keys=r['keys'], reading=r['reading'], path_only=r['path_only'],
                        names=[[x, at, p] for _kp, rows_ in r['per'] for x, at, p in rows_]) for r in i['reads']]) for i in items],
            counts=cnt, own_counts=ocnt, item_at=item_at, foot_at=foot_at, diff_at=diff_at, clustered=[i['n'] for i in clu],
            differ=[i['n'] for i in dif], ask=[i['n'] for i in ask],
            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
        print('written %s (%d lines) and %s' % (os.path.relpath(AGENDA, RELAY).replace(os.sep, '/'), len(P),
                                               os.path.relpath(AJSON, RELAY).replace(os.sep, '/')))


# ================================================================================ THE QUESTION
def question(mode):
    A = json.load(open(AJSON, encoding='utf-8'))
    L = relay_lines('data/b770_sitting_agenda.txt')
    it = A['items']
    c, fa = A['counts'], A['foot_at']
    ask = [i for i in it if i['n'] in A['ask']]
    if not ask:
        print('### NO ITEM READS CLUSTERED BY EITHER SHAPE (data/b770_sitting_agenda.txt :%d): NO QUESTION IS COMPOSED AND NO PROMPT IS PUT ((R380)(7))' % fa)
        return
    oc, da = A['own_counts'], A['diff_at']
    by_maps = [i for i in ask if i['reading'].startswith('CLUSTERED')]
    keys = list(dict.fromkeys(k for i in ask for k in (i['keys'] if i in by_maps else [i['own']['keystone']])))
    cls = list(dict.fromkeys((i['cluster'] if i in by_maps else i['own']['cluster']) for i in ask))
    lst = ', '.join('%d %s' % (i['n'], i['act']) for i in ask)
    why = (' The maps seat none of them because no map row or keystone yet names their banks.' if not by_maps else '')
    q = ('The sitting of the tenth act under (R380)(7), in the light form: the agenda is banked whole (data/b770_sitting_agenda.txt :%d), %d items, '
         'one for each FINDINGS heading of b761 to b769 that is no corrigendum. By the four rules of b761`s tool, which read each heading against '
         'the cluster table of SPIRAL_MAP, REGISTRY and the keystones` text at the papers` repository`s HEAD, %d read SYNTHESISED, %d CLUSTERED and '
         '%d BANKED with no seat (data/b770_sitting_agenda.txt :%d). By their own INTEGRATION lines %d read CLUSTERED, and the two readings differ '
         'at %d items (data/b770_sitting_agenda.txt :%d). You are asked about the items CLUSTERED by either reading and no other: items %s, of the '
         'cluster %s, the keystone %s.%s Passed, each is an input of that keystone`s re-cut at the tip, listed in the inputs bank; struck, it stands '
         'banked with no seat and the re-cut does not list it. No keystone is written at this sitting. Pass these items whole, or strike items by '
         'number (name them in your note).') % (
        fa, len(it), c['SYNTHESISED'], c['CLUSTERED'], c['BANKED'], fa, oc['CLUSTERED'], len(A['differ']), da, lst, ', '.join(cls),
        ', '.join(keys), why)
    q = q.replace('`', '’')
    opts = [dict(label=PASS, description=('Each item named stands as an input of its keystone’s re-cut at the tip, and the inputs bank lists it '
                                          'for that keystone.')),
            dict(label=STRIKE, description=('Items struck by number, named in your note: a struck item stands banked with no seat, as the maps '
                                            'read it, with your word beside it; the rest pass.'))]
    Q = dict(questions=[dict(header='Sitting', multiSelect=False, question=q, options=opts)])
    I = RG.ids()
    qw = RG.qword(show('REGISTRY.md'))
    blob = json.dumps(Q, ensure_ascii=False)
    ctl = [('the agenda`s foot line at :%d, as its JSON gives it' % fa, L[fa - 1].startswith('### ### **THE AGENDA:')),
           ('the items asked %d, those the agenda names for the prompt (%s), the differing line at :%d' % (len(ask), A['ask'], da),
            [i['n'] for i in ask] == A['ask'] and L[da - 1].startswith('## THE TWO READINGS DIFFER AT')),
           ('no clause naming the act`s FINDINGS record by the word the composer reads as about it', not re.search(r'\bentry\b', blob, re.I)),
           ('the question opens with its words for the inputs route`s read of the answer', q.startswith(Q_OPEN)),
           ('the identifiers 0 and the protected word 0', RG.idcount(blob, I) == 0 and qw.lower() not in blob.lower())]
    ok = all(o for _w, o in ctl)
    print(json.dumps(Q, ensure_ascii=False, indent=1))
    for w, o in ctl:
        print('  %-120s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED'))
    print('### ### **THE QUESTION: COMPOSED, %d CHARACTERS, %d OPTIONS ; CONTROLS %d OF %d ; %s.**' % (
        len(q), len(opts), sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY') if ok else 'HELD'))
    if mode == 'write':
        if not ok:
            die('A CONTROL NOT AS WANTED')
        put(QJSON, json.dumps(Q, ensure_ascii=False, indent=1) + NL)
        print('written data/b770_question.json')


# ================================================================================ THE INPUTS BANK
def answer(it):
    """(the option chosen, the RESULT line's number, its text): the one RESULT line of the answers bank answering the sitting's question."""
    W = relay_lines(ANSWERS)
    res = [(k, l) for k, l in enumerate(W, 1) if l.startswith('RESULT (') and Q_OPEN.replace('`', '’') in l]
    if len(res) != 1:
        return None, [k for k, _l in res], ''
    k, l = res[0]
    ch = [lab for lab in (PASS, STRIKE) if ('"="%s"' % lab) in l]
    return (ch[0] if len(ch) == 1 else None), k, l


def inputs(mode, struck):
    A = json.load(open(AJSON, encoding='utf-8'))
    it = A['items']
    clu = [i for i in it if i['n'] in A['ask']]
    tracked = set(subprocess.run(['git', '-C', RELAY, 'ls-files', 'data/'], capture_output=True).stdout.decode('utf-8').split(NL))
    ctl = []
    if clu:
        chosen, rk, rl = answer(it)
        ctl.append(('the answer read: one RESULT line answering the sitting`s question (%s :%s), the option chosen %s' % (ANSWERS, rk, chosen),
                    chosen in (PASS, STRIKE)))
        if chosen == STRIKE:
            ctl.append(('the struck numbers %s each a CLUSTERED item and each standing in the answer' % (struck or 'none'),
                        bool(struck) and all(n in [i['n'] for i in clu] and re.search(r'(?<!\d)%d(?!\d)' % n, rl) for n in struck)))
        else:
            ctl.append(('no number struck where the items pass whole (struck %s)' % (struck or 'none'), not struck))
    else:
        chosen, rk = None, None
        ctl.append(('no item reads CLUSTERED, so no prompt was put and no answer is read; no number struck (%s)' % (struck or 'none'), not struck))
    final = []
    for i in it:
        r, ks = i['reading'], i['keys']
        if i['n'] in struck:
            r = 'STRUCK BY THE AUTHOR, BANKED'
        elif i['n'] in A['ask']:
            r = READINGS[1]
            if not i['reading'].startswith('CLUSTERED'):
                ks = [i['own']['keystone']]   # ### an item asked by its own line: the keystone its line names
        final.append(dict(i, final=r, keys=ks))

    def banks(i):
        b = sorted(f for x in i['names'] for f in tracked if f.startswith('data/' + x + '.'))
        if b:
            return list(dict.fromkeys(b)), ''
        c = 'data/%s_closing.txt' % i['act']
        return ([c] if c in tracked else []), ' (its heading names no bank: the act`s closing bank)'
    keys = list(dict.fromkeys(k for i in final for k in i['keys']))
    P = ['%s -- (R380)(7): THE INPUTS BANK, FOR EACH KEYSTONE THE PASSED ITEMS IT DOES NOT CARRY (%s)' % (ACT, utc()), '',
         '### tools/b770_sitting.py inputs %s; from data/b770_sitting_agenda.json as committed and the author`s answer (%s); each item by its' % (
             mode, ('%s :%s, the option chosen: %s' % (ANSWERS, rk, chosen)) if clu else 'none read: no item read CLUSTERED and no prompt was put'),
         '### FINDINGS line (its heading`s, by sha256, no line of a paper quoted) and its bank, tracked files alone; no keystone written.', '']
    n_in, miss = 0, []
    for kp in keys:
        ins = [i for i in final if kp in i['keys'] and i['final'].startswith('CLUSTERED')]
        P.append('## %s: %d input(s) of its re-cut' % (kp, len(ins)))
        for i in ins:
            b, why = banks(i)
            if not b:
                miss.append(i['n'])
            n_in += 1
            P.append('  [%d] %s, FINDINGS :%d (sha256 %s), its line as written FINDINGS :%s; its bank%s: %s' % (
                i['n'], i['act'], i['line'], i['sha'], i['iline'], why, ', '.join(b) or 'NONE FOUND'))
        side = [i for i in final if kp in i['keys'] and i['final'] == 'SYNTHESISED' and i['path_only']]
        if side:
            P.append('  beside the inputs, not counted: carried by relay paths alone, which canon XXIV sends out of the paper at its re-cut: %s' % (
                ', '.join('[%d] %s (FINDINGS :%d)' % (i['n'], i['act'], i['line']) for i in side)))
        P.append('')
    nseat = [i for i in final if i['final'].startswith('BANKED') or i['final'].startswith('STRUCK')]
    P.append('## NO KEYSTONE (banked with no seat, or struck by the author): %s' % (', '.join('[%d] %s' % (i['n'], i['act']) for i in nseat) or 'none'))
    P.append('')
    cnt = dict((w, sum(1 for i in final if i['final'].startswith(w))) for w in ('SYNTHESISED', 'CLUSTERED', 'BANKED', 'STRUCK'))
    passed = [i['n'] for i in clu if i['n'] not in struck]
    s5 = dict(n=len(final), k=cnt['SYNTHESISED'], c=cnt['CLUSTERED'], b=cnt['BANKED'] + cnt['STRUCK'], asked=[i['n'] for i in clu],
              passed=passed, struck=list(struck), maps=[A['counts']['SYNTHESISED'], A['counts']['CLUSTERED'], A['counts']['BANKED']])
    P.append('## FOR [S5], after the author`s answer: items %d ; SYNTHESISED %d ; an input of a keystone`s re-cut %d ; banked with no seat %d ; '
             'put to the author %s (%s) ; passed %s ; struck %s ; by the maps` rules alone SYNTHESISED %d, CLUSTERED %d, BANKED %d' % (
                 s5['n'], s5['k'], s5['c'], s5['b'], len(clu) or 'none', ', '.join(str(i['n']) for i in clu) or 'none',
                 ', '.join(map(str, passed)) or 'none', ', '.join(map(str, struck)) or 'none', *s5['maps']))
    I = RG.ids()
    qw = RG.qword(show('REGISTRY.md'))
    ctl += [('every input read not carried: none of its names carried by its keystone, by the maps` read and by its own line`s (VACUOUS for the '
             '%d whose heading names none)' % sum(1 for i in final if i['final'].startswith('CLUSTERED') and not i['names']), all(
                not at for i in final if i['final'].startswith('CLUSTERED') for r in i['reads'] for _x, at, _p in r['names']) and all(
                not (i['own'] or {}).get('carried') for i in final if i['final'].startswith('CLUSTERED'))),
            ('every input`s bank found among the tracked files (misses %s)' % (miss or 'none'), not miss),
            ('the inputs %d, the CLUSTERED items passed %d' % (n_in, cnt['CLUSTERED']), n_in == cnt['CLUSTERED'] == len(passed)),
            ('the counts summing to the items (%d)' % len(final), sum(cnt.values()) == len(final))]
    text = NL.join(P)
    ctl.append(('the identifiers 0 and the protected word 0', RG.idcount(text, I) == 0 and qw.lower() not in text.lower()))
    ok = all(o for _w, o in ctl)
    P += ['', '## THE CONTROLS'] + ['  %-130s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '### ### **THE INPUTS: KEYSTONES %d ; INPUTS %d ; NO KEYSTONE %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
        len(keys), n_in, len(nseat), sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    text = NL.join(P) + NL
    print(text)
    if mode == 'write':
        if not ok:
            die('A CONTROL NOT AS WANTED')
        put(INPUTS, text)
        put(INPUTS[:-4] + '.json', json.dumps(dict(at=utc(), act=ACT, answer=[ANSWERS, rk, chosen], s5=s5, inputs=dict(
            (kp, [i['n'] for i in final if kp in i['keys'] and i['final'].startswith('CLUSTERED')]) for kp in keys),
            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
        print('written data/b770_recut_inputs.txt (%d lines) and data/b770_recut_inputs.json' % len(P))


if __name__ == '__main__':
    a = sys.argv[1:]
    struck = []
    if len(a) == 4 and a[0] == 'inputs' and a[2] == '--struck':
        struck = [int(x) for x in a[3].split(',') if x.strip()]
        a = a[:2]
    if len(a) != 2 or a[0] not in ('agenda', 'question', 'inputs') or a[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    if a[0] == 'inputs':
        inputs(a[1], struck)
    else:
        dict(agenda=agenda, question=question)[a[0]](a[1])
