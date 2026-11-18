# -*- coding: utf-8 -*-
"""tools/b761_sitting.py -- b761, (R371)(5): THE SYNTHESIS SITTING: THE AGENDA BANKED BEFORE THE QUESTION, THE ONE QUESTION COMPOSED FROM IT.

Written by the Write tool at b761's Component 4 and committed before its first run, dry included (b761 defect (h)).

  agenda dry|write     data/b761_sitting_agenda.txt and .json: the sixteen items and the orders section; writes nothing else
  question dry|write   data/b761_question.json, the one question composed from the agenda's bank, for `rootprompt.py put b761`

THE ITEMS ((R371)(5)): one for each FINDINGS entry from b745's to b760's that is no corrigendum, in the entries' order, numbered: its heading
by line and sha256 (no line of a paper quoted in a relay bank) and its names as tools/standing/linematch.py reads them (the heading's
lower-case underscore names alone, linematch.py :9-:10); its cluster and that cluster's keystone, read from REGISTRY's rows and SPIRAL_MAP's
cluster table (:266-:276) at PLACE-papers HEAD; for each name, whether the keystone's text at HEAD carries it, by its lines, a name carried
only inside a relay bank's path marked so; and the item's reading:
  SYNTHESISED                                   the keystone carries a name of the entry, the edition named
  CLUSTERED, AN INPUT OF THAT KEYSTONE'S RE-CUT  the cluster names a keystone that carries none
  BANKED, NO SEAT                               the maps name no cluster
THE CLUSTER, by four rules, each item printing the rule that placed it: (R1) a cluster row carries a needle of the heading (a linematch name,
an upper-case document stem, a kernel's or branch's name, a REGISTRY id); (R2) the heading carries a document stem of the row's keystone or
sibling-anchor cell, its version suffix cut, underscores read as spaces, case ignored; (R3) a REGISTRY row whose File cell carries a needle of
the heading (a kernel's name aside, a kernel serving many rows), or whose id is one, is a row the cluster row names by id; (R4) the cluster
row's keystone text carries a linematch name of the entry. A heading no rule places reads BANKED, NO SEAT, keystone none yet.
THE ORDERS (the author's words of 2026-11-18, data/b761_author_words_preseal.txt :2 (3) and :5): every order tools/standing/orders.py reads
OPEN at PLACE-papers HEAD, each in one class by the seat's reading of its trigger as last written (b724's triage, data/b724_orders_triage.txt;
b756's trigger written again, data/b756_orders_read.txt; or its own line in OPEN_TRAILS where b724 did not read it), the line cited and read
back carrying the order's name: MET (each taken up at b762 or the act its ruling names), THE AUTHOR'S WORD (listed to the author), NO
TRIGGER WRITTEN (carried by name to the next ruling, which gives one or retires it; the seat writes neither), WRITTEN, NOT READ AS MET.
No trigger is written and no order is retired, entered or closed by this tool.
THE QUESTION: the agenda whole, passed whole or struck by number, the navigator's recommendation (b752, b753, b754 BANKED) its own option, and
the option (5) gives where the author strikes the clause itself; composed from the agenda's JSON, its figures cited to the agenda's lines.

No keystone, map or FINDINGS line is written; no PLACE-papers line is printed but the names, the cluster's label and the stage words; the
protected word neither printed nor stored; no git write.
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
import orders as OR         # noqa: E402
import b761_registry as RG  # noqa: E402

ACT, NL = 'b761', '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
AGENDA = os.path.join(D, 'b761_sitting_agenda.txt')
AJSON = os.path.join(D, 'b761_sitting_agenda.json')
QJSON = os.path.join(D, 'b761_question.json')
HEADS = (14027, 14147, 14259, 14387, 14496, 14627, 14747, 14868, 15009, 15208, 15296, 15370, 15436, 15500, 15560, 15620)
ACTS = tuple('b%d' % n for n in range(745, 761))
NAV = ('b752', 'b753', 'b754')     # ### (R371)(5): the navigator's recommendation, BANKED
CT_HEAD, CT_FIRST, CT_LAST = 266, 268, 276
B724, B756 = 'data/b724_orders_triage.txt', 'data/b756_orders_read.txt'
OT = 'OPEN_TRAILS.md'
TAKEN = 'b762, the act after this one, the ruling for it naming it (data/b761_author_words_preseal.txt :5)'
BUILD = 'met at b724`s reading, placed with the build at b756, not taken up since'
# ### THE ORDERS, the seat's reading of each trigger as last written (class, cites [(bank or OT, line)], the seat's own words)
ORDERS = [
    ('W-ORD-KEIPER-FACE', 'M', [(B724, 333), (B756, 17)], BUILD),
    ('W-ORD-E2-SEPARATION', 'M', [(B724, 345), (B756, 36)], BUILD),
    ('W-ORD-BESSEL-BOUND-TIGHTEN', 'M', [(B724, 353), (B756, 49)], BUILD),
    ('W-ORD-B518-FLOAT', 'M', [(B724, 369), (B756, 75)], BUILD),
    ('W-ORD-EXPLICIT-FORMULA-C1', 'M', [(B724, 373), (B756, 81)], BUILD),
    ('W-ORD-MECHANISM-TABLE', 'M', [(OT, 16589), (OT, 17094)], 'its trigger read at b725, its work begun at b726 and carried at b732'),
    ('W-ORD-VISIBILITY', 'M', [(OT, 16590), (OT, 16893)], 'its trigger met, its work read not clean at b728 and carried at b729'),
    ('W-ORD-LATE-BANKS', 'M', [(B724, 463)], 'its trigger the next finding after a seal: b760`s findings after its lock, entered at this act (data/b761_events.txt (20)-(35)); b724 graded it on the author`s word'),
    ('W-ORD-MATCHER-SHAPE', 'M', [(B724, 415)], 'its trigger the next act that matches a header, a document name or a version by pattern: this act`s cells tool does (tools/b761_registry.py); b724 graded it on the author`s word'),
    ('W-ORD-CORRESPONDENCE-BEHIND-SCOPE', 'M', [(B724, 365), (B756, 68)], 'its trigger as b756 wrote it again, the next re-cut act of a document carrying a Correspondence table: b760`s edition of Which Structure Confines at v2.5.0 carries one, read as met where an edition is such an act'),
    ('W-ORD-P2-9-RESYNC', 'A', [(B724, 204)], 'the author schedules it'),
    ('W-ORD-LI-WEIL-BRIDGE', 'A', [(B724, 207)], 'the author`s word'),
    ('W-ORD-E0-RANK-PROPAGATION', 'A', [(B724, 210)], 'the author`s word on moving a grade inside a table'),
    ('W-ORD-GW-IMPORT', 'A', [(B724, 216)], 'the author`s ruling on importing a third party`s terminal'),
    ('W-ORD-STRICT-BOUND', 'A', [(B724, 423)], 'the author`s word, or the next act citing a cell count in a keystone'),
    ('W-ORD-SEAM-UPSTREAM', 'A', [(B724, 219)], 'the author`s word'),
    ('W-ORD-WINDOW-CERTIFY', 'A', [(B724, 225)], 'the author`s word'),
    ('W-ORD-PNT-CHI', 'A', [(B724, 234)], 'the author`s word'),
    ('W-ORD-VENDOR-FINALMULT', 'A', [(B724, 237)], 'the author`s word'),
    ('W-ORD-ZETA23-SERIAL-BUILD', 'A', [(B724, 240)], 'the author`s word'),
] + [('W-ORD-PREMISE-' + n, 'A', [(B724, k)], 'the author`s word (the open premises, one order each)') for n, k in (
    ('BOUNDPREMISES', 243), ('DEALIGNED', 246), ('DEALIGNEDAT', 249), ('IDEMPOTENTADD', 252), ('ISEVENFN', 255), ('ISEXPANSION', 258),
    ('ISSIGNEDCOMPLETION', 261), ('ISTRIVIALPOINT', 264), ('NONTRIVIALZEROEXISTSINSTRIP', 267), ('NOTDIV', 270), ('PERCLASSEXCLUDES', 273),
    ('PROPER', 276), ('REGISTER4-CHANNELINEQUALITY', 279), ('REGISTER4-POSITIVITY', 282), ('SELFDUALFE', 285), ('ZEROACTINGPAIRING', 288),
    ('IDENTITY', 291), ('IS-XI-ZERO', 294))] + [
    ('W-ORD-STATEMENT-PIN', 'A', [(B724, 297)], 'the next new load-bearing declaration, acted on the author`s word'),
    ('W-ORD-H2-PI1', 'A', [(B724, 459)], 'the author`s word before the census`s opening at v0.7 is written'),
    ('W-ORD-TABLE-SHAPE', 'A', [(B724, 306)], 'the author`s strike on each table`s form'),
    ('W-ORD-EPSTEIN-COUNT-LEAN', 'A', [(B724, 321)], 'the author`s word, as its own programme'),
    ('W-ORD-ADMISSIBLE-CONE', 'A', [(OT, 16591)], 'the author`s word, priced from b709`s grid timings'),
    ('W-ORD-ZQ-FAMILY', 'A', [(OT, 17716)], 'the author`s word'),
    ('W-ORD-SQUARES-AT-24', 'A', [(OT, 18503)], 'the author`s word'),
    ('W-ORD-BIBLIOGRAPHY-LINK', 'A', [(OT, 18631)], 'the author`s word'),
    ('W-ORD-IMP2-TAU', 'N', [(B724, 399)], 'none written, as b724 read it'),
    ('W-ORD-EXACT-SUPPORT', 'N', [(B724, 419)], 'none written, as b724 read it'),
    ('W-ORD-MOVES-BY-LOCUS', 'N', [(B724, 487)], 'none written, as b724 read it'),
    ('W-ORD-DETECTION-REGION', 'N', [(B724, 222)], 'its last line names a grade and a queue and no event'),
    ('W-ORD-ROUTE-DE-EQUIV', 'W', [(B724, 201)], 'before a paper cites a Route D or Route E equivalence'),
    ('W-ORD-LI-FAMILY-CONTROL', 'W', [(B724, 407)], 'an act asserting or depending on the explicit formula closing on the Li family'),
    ('W-ORD-FLOOR-HELD-AXES', 'W', [(B724, 213)], 'an act that moves either axis'),
    ('W-ORD-POWER-SWEEP', 'W', [(B724, 228)], 'the self-convolution family built as a ladder window class passing its positive control'),
    ('W-ORD-STORMER-CLASH', 'W', [(B724, 329), (B756, 10)], 'the next SIDE-kernel tag'),
    ('W-ORD-DEPRECATIONS', 'W', [(B724, 231)], 'the next Mathlib move of SIDE-explicit-formula'),
    ('W-ORD-READER-COMPREHENSION', 'W', [(B724, 300)], 'the next reader run'),
    ('W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE', 'W', [(B724, 341), (B756, 29)], 'the next act editing tools/chain_page.py or the node lists it reads'),
    ('W-ORD-CLOSE-PAIR-BENCH', 'W', [(B724, 303)], 'after the re-cuts'),
    ('W-ORD-ROOT-BINARY-BANK', 'W', [(B724, 349), (B756, 42)], 'the next act that banks a binary file'),
    ('W-ORD-GRADE-MOVED', 'W', [(B724, 309)], 'the document`s next re-cut act'),
    ('W-ORD-PRINT-TARGETS', 'W', [(B724, 312)], 'the kernel`s next runner build'),
    ('W-ORD-ABSENT-DECLARATIONS', 'W', [(B724, 315)], 'the document`s next re-cut act'),
    ('W-ORD-PROSE-PINS', 'W', [(B724, 318)], 'the document`s next re-cut act'),
    ('W-ORD-CHAIN-PAGE-B638-CASES', 'W', [(B724, 357), (B756, 55)], 'the next act editing tools/chain_page.py or the node lists it reads'),
    ('W-ORD-KEYSTONE-HEADS', 'W', [(B724, 479), (OT, 15496)], 'the re-cut act after the widening, the Epstein count and the closure join have landed'),
    ('W-ORD-QUASI-RH-FIELD-WATCH', 'W', [(B724, 324)], 'a reviewed or Mathlib-merged form'),
    ('W-ORD-DETECTION-DUAL', 'W', [(OT, 16592)], 'lambda_2`s branch landed; its landing not read by the seat at this act'),
    ('W-ORD-SIDE-DIAGNOSTIC', 'W', [(OT, 16594)], 'W-ORD-MECHANISM-TABLE landed'),
    ('W-ORD-CHAIN-PAGE-LLM-LINE', 'W', [(OT, 16754)], 'the generator`s next run'),
    ('W-ORD-LI-ARITH', 'W', [(OT, 17714), (OT, 0)], 'the act after the re-cut of One Page, the author`s word at this act'),
    ('W-ORD-LI-INDEX', 'W', [(OT, 18627)], 'before either figure enters a keystone'),
    ('W-ORD-CAPACITY-ATTRIBUTION', 'W', [(OT, 18629)], 'CAPACITY`s next edition'),
    ('W-ORD-EPSTEIN-SECTIONS-3-4', 'W', [(OT, 18633)], 'the Epstein document`s v0.3'),
    ('W-ORD-WSC-TITCHMARSH', 'W', [(OT, 18701)], 'that document`s next edition'),
    ('W-ORD-RECUT-QUOTE-W4', 'W', [(OT, 18703)], 'the next edition of each document named'),
    ('W-ORD-RECUT-QUOTE-W8', 'W', [(OT, 18705)], 'the next edition of each document named'),
    ('W-ORD-RECUT-QUOTE-W9', 'W', [(OT, 18707)], 'the next edition of each document named'),
    ('W-ORD-RECUT-QUOTE-C4', 'W', [(OT, 18709)], 'the next edition of each document named'),
]
CLASSES = (('M', 'TRIGGERS MET, EACH TAKEN UP AT ' + TAKEN.split(',')[0].upper() + ' OR THE ACT ITS RULING NAMES'),
           ('A', 'WAITING ON THE AUTHOR`S WORD, LISTED TO THE AUTHOR'),
           ('N', 'NO TRIGGER WRITTEN, EACH CARRIED BY NAME TO THE NEXT RULING, WHICH GIVES ONE OR RETIRES IT; THE SEAT WRITES NEITHER'),
           ('W', 'A TRIGGER WRITTEN, NOT READ AS MET AT THIS ACT'))


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


def cluster_table(S):
    if not S[CT_HEAD - 1].startswith('| Cluster |'):
        die('SPIRAL_MAP :%d IS NOT THE CLUSTER TABLE`S HEAD' % CT_HEAD)
    files = subprocess.run(['git', '-C', PP, 'ls-files'], capture_output=True).stdout.decode('utf-8').split(NL)
    out = []
    for k in range(CT_FIRST, CT_LAST + 1):
        l = S[k - 1]
        m = re.match(r'^\| \*\*([^*]+)\*\*', l)
        if not m:
            continue
        c = l.split('|')
        kcell, scell = (c[2] if len(c) > 2 else ''), (c[3] if len(c) > 3 else '')
        keys = []
        for x in re.findall(r'`([\w./\-]+\.md)`', kcell):
            keys += [x] if x in files else [f for f in files if f.rsplit('/', 1)[-1] == x.rsplit('/', 1)[-1]]
        if not re.findall(r'`([\w./\-]+\.md)`', kcell):
            for s in stems(kcell):
                keys += [f for f in files if f.endswith('.md') and re.sub(r'(_v\d+(?:_\d+)*)$', '', f.rsplit('/', 1)[-1][:-3]) == s]
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
    path = bool(at) and all(re.findall(r'(?<![\w`.-])`?' + re.escape(name) + r'`?(?![\w-])', KL[k - 1]) and
                            len(re.findall(r'data/' + re.escape(name) + r'\.', KL[k - 1])) == len(re.findall(r'(?<![\w`.-])`?' + re.escape(name) + r'`?(?![\w-])', KL[k - 1]))
                            for k in at)
    return at, path


# ================================================================================ THE AGENDA
def agenda(mode):
    F, S, R = show('FINDINGS.md'), show('SPIRAL_MAP.md'), show('REGISTRY.md')
    O = show(OT)
    I = RG.ids()
    qw = RG.qword(R)
    head = subprocess.run(['git', '-C', PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True).stdout.decode().strip()
    hs = [k for k in range(14000, len(F) + 1) if F[k - 1].startswith('## ') and not F[k - 1].startswith('## Corrigendum')]
    cs = [(k, m.group(1)) for k in range(14000, len(F) + 1) for m in [re.match(r'^## Corrigendum to (b\d+)', F[k - 1])] if m]
    acts = [next((a for k, a in cs if k > h), None) for h in hs]
    ct = cluster_table(S)
    rr = reg_rows(R)
    ktexts = {}
    for row in ct:
        for kp in row['keys']:
            if kp not in ktexts:
                KL = show(kp)
                ktexts[kp] = (KL, LM.names(NL.join(KL)))
    items = []
    for n, (h, a) in enumerate(zip(hs, acts), 1):
        nxt = min([k for k in hs + [x for x, _a in cs] if k > h] or [len(F) + 1])
        il = next((k for k in range(h + 1, nxt) if F[k - 1].startswith('INTEGRATION:')), None)
        st = re.search(r'stage ([A-Z]+(?: \([^)]*\))?(?:, [A-Z]+ \([^)]*\))?)\s*$', F[il - 1]) if il else None
        nm = LM.names(F[h - 1])
        found = place(F[h - 1], ct, rr, ktexts)
        reads = []
        for row, why in found:
            keys = row['keys']
            per = []
            for kp in keys:
                KL = ktexts[kp][0]
                per.append((kp, [(x,) + carried(x, KL) for x in nm]))
            hit = [(kp, x, at, p) for kp, rows in per for x, at, p in rows if at]
            if not keys:
                rd = 'CLUSTERED, NO KEYSTONE NAMED'
            elif hit:
                rd = 'SYNTHESISED'
            else:
                rd = 'CLUSTERED, AN INPUT OF THAT KEYSTONE`S RE-CUT'
            reads.append(dict(cluster=row['name'], row=row['line'], why=why, keys=keys, per=per, reading=rd,
                              path_only=bool(hit) and all(p for _k, _x, _a, p in hit)))
        if not reads:
            reading, cl = 'BANKED, NO SEAT', None
        else:
            r0 = sorted(reads, key=lambda r: 0 if r['reading'] == 'SYNTHESISED' else 1)[0]
            reading, cl = r0['reading'], r0
        items.append(dict(n=n, act=a, line=h, sha=sha(F[h - 1]), names=nm, iline=il, isha=sha(F[il - 1]) if il else None,
                          istage=(st.group(1) if st else ('a tally, no stage word' if il else 'none')), reads=reads, reading=reading,
                          cluster=cl['cluster'] if cl else None, crow=cl['row'] if cl else None, keys=cl['keys'] if cl else [],
                          path_only=cl['path_only'] if cl else False, several=len(reads) > 1))
    # ### the orders
    rows = OR.read(O)
    st = dict((n, d) for n, d in rows)
    opn = [n for n, d in rows if d['status'] == 'OPEN']
    li = [k for k in range(18771, len(O) + 1) if 'W-ORD-LI-ARITH' in O[k - 1]]
    orders, cite_bad = [], []
    rl = {B724: relay_lines(B724), B756: relay_lines(B756)}
    for name, c, cites, words in ORDERS:
        cc = []
        for src, k in cites:
            if src == OT and k == 0:
                k = li[0] if li else 0
            line = (O[k - 1] if src == OT else rl[src][k - 1]) if k else ''
            ok = bool(k) and name in line
            if not ok:
                cite_bad.append('%s %s :%d' % (name, src, k))
            cc.append('%s :%d' % ('OPEN_TRAILS' if src == OT else src, k))
        orders.append(dict(name=name, cls=c, cites=cc, words=words, entry=st.get(name, {}).get('entry'), status=st.get(name, {}).get('status')))
    names = [o['name'] for o in orders]
    by = dict((c, [o for o in orders if o['cls'] == c]) for c, _t in CLASSES)
    kh = dict((n, st.get(n, {}).get('status')) for n in ('W-ORD-EPSTEIN-COUNT', 'W-ORD-LV-CLOSURE-JOIN'))
    # ### the counts
    cnt = dict((r, sum(1 for i in items if i['reading'].startswith(r))) for r in ('SYNTHESISED', 'CLUSTERED', 'BANKED'))
    rec = dict(cnt)
    for i in items:
        if i['act'] in NAV and not i['reading'].startswith('BANKED'):
            rec['BANKED'] += 1
            rec['SYNTHESISED' if i['reading'].startswith('SYNTHESISED') else 'CLUSTERED'] -= 1
    # ### the bank
    P = ['%s -- (R371)(5): THE SYNTHESIS SITTING`S AGENDA, BANKED BEFORE THE QUESTION IS PUT (%s)' % (ACT, utc()), '',
         '### tools/b761_sitting.py agenda %s; PLACE-papers HEAD %s; REGISTRY, SPIRAL_MAP`s cluster table (:%d-:%d), FINDINGS and the keystones read at HEAD;' % (mode, head, CT_HEAD, CT_LAST),
         '### each heading by its line and sha256, no line of a paper quoted; the names as tools/standing/linematch.py reads them (the heading`s lower-case',
         '### underscore names alone, linematch.py :9-:10); the cluster by rules R1-R4 (the tool`s docstring), the rule that placed each item printed;',
         '### no keystone, map or FINDINGS line written at this sitting ((R371)(5), canon XXIV).', '',
         '## THE CLUSTER TABLE (SPIRAL_MAP :%d-:%d): cluster rows %d; the keystones it names by path or by stem read: %s' % (
             CT_HEAD, CT_LAST, len(ct), ', '.join('%s (%d lines, %d names)' % (k, len(v[0]), len(v[1])) for k, v in ktexts.items()) or 'none'), '',
         '## THE ITEMS (FINDINGS entries b745 to b760 that are no corrigendum, in their order)']
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
                                                                         ', inside a relay bank`s path alone' if p else '')) if at else 'not carried'))
        note = ''
        if i['path_only']:
            note = ' -- carried as a relay bank`s path alone, which canon XXIV sends out of the paper at its re-cut (the navigator`s (vi))'
        elif i['reading'].startswith('CLUSTERED') and not i['names']:
            note = ' -- the heading names the keystone`s own work and carries no name the reader takes (data/b761_misses.txt (1))'
        if i['act'] in NAV:
            note += ' -- the navigator recommends BANKED'
        if i['several']:
            note += ' -- placed in %d clusters, the highest reading taken' % len(i['reads'])
        P.append('      READING: %s%s%s' % (i['reading'], (' (%s)' % ', '.join(i['keys'])) if i['reading'] == 'SYNTHESISED' else '', note))
    P += ['', '## THE NAVIGATOR`S RECOMMENDATION ((R371)(5), data/b761_ferry.txt :17): items %s (%s), reads of the record`s own documents, take no keystone and' % (
        ', '.join(str(i['n']) for i in items if i['act'] in NAV), ', '.join(NAV)),
        '## stand BANKED; with it, SYNTHESISED %d, CLUSTERED (an input of a re-cut) %d, BANKED %d' % (rec['SYNTHESISED'], rec['CLUSTERED'], rec['BANKED']), '']
    orders_at = len(P) + 1
    P.append('## THE OPEN ORDERS BY THEIR TRIGGERS (the author`s words of 2026-11-18, data/b761_author_words_preseal.txt :2 (3) and :5): OPEN %d at HEAD by' % len(opn))
    P.append('## tools/standing/orders.py; each in one class by the seat`s reading of its trigger as last written, the line cited and read back carrying its name;')
    P.append('## the words after each are the seat`s, no line of a paper quoted; no trigger written and no order retired, entered or closed here')
    for c, t in CLASSES:
        P.append('  (%s) %s: %d' % (c, t, len(by[c])))
        for o in by[c]:
            P.append('      %s (entry OPEN_TRAILS :%s) -- %s [%s]' % (o['name'], o['entry'], o['words'], '; '.join(o['cites'])))
    P.append('      W-ORD-KEYSTONE-HEADS`s conditions as the roster reads them: %s' % ', '.join('%s %s' % kv for kv in kh.items()))
    P.append('')
    ctl = [('the sixteen headings: the non-corrigendum headings of FINDINGS from :14000 (%d), at the lines wanted, each before its act`s corrigendum (%s)' % (
                len(hs), ', '.join(a or '?' for a in acts)), tuple(hs) == HEADS and tuple(acts) == ACTS),
           ('each item`s own line found (%d of %d)' % (sum(1 for i in items if i['iline']), len(items)), all(i['iline'] for i in items)),
           ('the cluster table read: rows %d (at least 9), the Epstein instance`s keystone read at HEAD' % len(ct),
            len(ct) >= 9 and any(k.endswith('THE_EPSTEIN_CONTROL_OBJECT_v0_2.md') for k in ktexts)),
           ('the match`s positive control: pc_online read carried by the Epstein keystone, a planted name b999_planted not', any(
               carried('pc_online', v[0])[0] for k, v in ktexts.items() if 'EPSTEIN' in k) and not any(carried('b999_planted', v[0])[0] for v in ktexts.values())),
           ('the placement`s planted control: a heading naming nothing of the maps (b999_planted_bank) placed nowhere',
            not place('## b999_planted_bank read', ct, rr, ktexts)),
           ('the orders: the hand table`s %d names each once and equal to the %d OPEN at HEAD' % (len(names), len(opn)),
            len(set(names)) == len(names) and set(names) == set(opn)),
           ('each order`s cited lines read back carrying its name (misses %s); W-ORD-LI-ARITH`s line of this act %s' % (cite_bad or 'none', li[:1]),
            not cite_bad and bool(li)),
           ('the four classes %s, summing to %d' % (', '.join('%s %d' % (c, len(by[c])) for c, _t in CLASSES), len(orders)),
            sum(len(v) for v in by.values()) == len(orders))]
    text = NL.join(P)
    ctl.append(('the identifiers 0 and the protected word 0 in the bank', RG.idcount(text, I) == 0 and qw.lower() not in text.lower()))
    ok = all(o for _w, o in ctl)
    P.append('## THE CONTROLS')
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '### ### **THE AGENDA: ITEMS %d ; SYNTHESISED %d ; CLUSTERED, AN INPUT OF A RE-CUT %d ; BANKED, NO SEAT %d ; WITH THE NAVIGATOR`S RECOMMENDATION %d, %d, %d ; '
          'ORDERS OPEN %d: MET %d, THE AUTHOR`S WORD %d, NO TRIGGER %d, WRITTEN NOT MET %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(items), cnt['SYNTHESISED'], cnt['CLUSTERED'], cnt['BANKED'], rec['SYNTHESISED'], rec['CLUSTERED'], rec['BANKED'], len(opn),
              len(by['M']), len(by['A']), len(by['N']), len(by['W']), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    foot_at = len(P)
    text = NL.join(P) + NL
    print(text)
    if mode == 'write':
        if not ok:
            die('A CONTROL NOT AS WANTED')
        put(AGENDA, text)
        put(AJSON, json.dumps(dict(at=utc(), act=ACT, pp_head=head, items=[dict((k, v) for k, v in i.items() if k != 'reads') | dict(
            reads=[dict(cluster=r['cluster'], row=r['row'], why=r['why'], keys=r['keys'], reading=r['reading'], path_only=r['path_only'],
                        names=[[x, at, p] for _kp, rows_ in r['per'] for x, at, p in rows_]) for r in i['reads']]) for i in items],
            counts=cnt, recommended=rec, nav=list(NAV), item_at=item_at, orders_at=orders_at, foot_at=foot_at,
            orders=dict((c, [o['name'] for o in by[c]]) for c, _t in CLASSES), controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
        print('written %s (%d lines) and %s' % (os.path.relpath(AGENDA, RELAY), len(P), os.path.relpath(AJSON, RELAY)))


# ================================================================================ THE QUESTION
def question(mode):
    A = json.load(open(AJSON, encoding='utf-8'))
    L = relay_lines('data/b761_sitting_agenda.txt')
    it = A['items']
    c, r = A['counts'], A['recommended']
    fa, oa = A['foot_at'], A['orders_at']

    def nums(pred):
        return ', '.join('%d %s' % (i['n'], i['act']) for i in it if pred(i))
    syn_names = nums(lambda i: i['reading'] == 'SYNTHESISED' and not i['path_only'])
    syn_path = nums(lambda i: i['reading'] == 'SYNTHESISED' and i['path_only'])
    clu = nums(lambda i: i['reading'].startswith('CLUSTERED'))
    ban = nums(lambda i: i['reading'].startswith('BANKED'))
    nav = ', '.join(str(i['n']) for i in it if i['act'] in NAV)
    om = A['orders']
    q = ('The synthesis sitting of b761 under (R371)(5): the agenda is banked whole (data/b761_sitting_agenda.txt :%d), %d items, one for each FINDINGS heading of b745 to '
         'b760 that is no corrigendum, each read from REGISTRY, the cluster table of SPIRAL_MAP and the keystone`s text at PLACE-papers HEAD. As the maps read them: '
         '%d SYNTHESISED (items %s by names the Epstein document v0.2 carries in its prose; items %s by relay bank paths alone, which canon XXIV sends out of the paper '
         'at its re-cut); %d CLUSTERED, each an input of the Epstein document`s re-cut (items %s); %d BANKED with no seat (items %s). No keystone is written at this '
         'sitting. The navigator recommends that items %s (b752, b753, b754), reads of the record`s own documents, take no keystone and stand BANKED; with it %d read '
         'SYNTHESISED, %d an input of a re-cut and %d banked (data/b761_sitting_agenda.txt :%d). The agenda also lists the open orders by their triggers '
         '(data/b761_sitting_agenda.txt :%d): %d met, each to be taken up at b762 or the act its ruling names; %d waiting on your word; %d with no trigger written, '
         'carried by name to the next ruling; %d written and not met. Pass the agenda whole, pass it with the navigator`s recommendation, or strike items by number '
         '(name them in your note): a struck item stands as the maps read it, with your word beside it.') % (
        fa, len(it), c['SYNTHESISED'], syn_names or 'none', syn_path or 'none', c['CLUSTERED'], clu or 'none', c['BANKED'], ban or 'none', nav,
        r['SYNTHESISED'], r['CLUSTERED'], r['BANKED'], fa, oa, len(om['M']), len(om['A']), len(om['N']), len(om['W']))
    q = q.replace('`', '’')
    opts = [dict(label='With the recommendation (Recommended)',
                 description=('The agenda passed with the navigator’s recommendation: items %s stand BANKED, so %d read SYNTHESISED, %d an input of the Epstein '
                              'document’s re-cut and %d banked with no seat; the inputs bank written for that keystone.') % (nav, r['SYNTHESISED'], r['CLUSTERED'], r['BANKED'])),
            dict(label='Passed whole',
                 description=('Every item stands as the agenda reads it: %d SYNTHESISED, %d an input of the Epstein document’s re-cut, %d banked with no seat; '
                              'the inputs bank written for that keystone.') % (c['SYNTHESISED'], c['CLUSTERED'], c['BANKED'])),
            dict(label='Strike by number',
                 description='Items struck by number, named in your note: each struck item stands as the maps read it with your word beside it, and the rest pass.'),
            dict(label='Sitting not held',
                 description='The amendment of (5) struck: the sitting is not held and the agenda stays banked; the act’s sentence reads that the agenda is banked, not put, your word on its form awaited.')]
    Q = dict(questions=[dict(header='Sitting', multiSelect=False, question=q, options=opts)])
    I = RG.ids()
    qw = RG.qword(show('REGISTRY.md'))
    blob = json.dumps(Q, ensure_ascii=False)
    ctl = [('the agenda`s foot line at :%d and its orders head at :%d, as its JSON gives them' % (fa, oa),
            L[fa - 1].startswith('### ### **THE AGENDA:') and L[oa - 1].startswith('## THE OPEN ORDERS')),
           ('no clause naming the act`s FINDINGS record by the word the composer reads as about it', not re.search(r'\bentry\b', blob, re.I)),
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
        print('written data/b761_question.json')


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) != 2 or a[0] not in ('agenda', 'question') or a[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    (agenda if a[0] == 'agenda' else question)(a[1])
