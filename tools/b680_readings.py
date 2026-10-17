# -*- coding: utf-8 -*-
"""b680_readings.py -- COMPONENT 2, (R290)(4): READING 2 OF 2 UNDER THE PAIR RULE (relay data/b670_rules.txt row 1), EACH READING BY b670'S
METHOD, b670'S FIGURE PRINTED BESIDE b680'S IN EVERY BANK.

### THE METHOD IS b670'S CODE, NOT A COPY: readings (i)-(v) import tools/b670_record.py (and, for (ii), tools/b672_record.py, the re-read of
### (ii) after the generator, whose stable anchors b670's state line names for b680) and run its own routes, their bank writers replaced in
### memory so that nothing of b670's or b672's is written; the captured banks are re-printed here beside b670's figure. Where b670's method
### reads data that grew since (the cut banks of b674, b676, b678; the age of an order counted from the reading act), the growth is declared
### beside the figure. Readings (vi)-(ix) b670 did not make: each is read as the ruling words it, and its b670 column is NOT COMPARABLE --
### b670 made no such reading -- with the reason printed (N2).
### Routes, one per reading, each one foreground process under the 600 s limit: licensed | corr | ceiling | orders | methods | kernels9 |
### residues | lag | outside -> data/b680_<name>.txt (.json). Written by the Write tool at b680; it writes only those banks.
"""
import collections
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def rdn(n):
    return rd(os.path.join(D, n))


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def put(name, lines, obj):
    for n, b in ((name + '.txt', (NL.join(lines) + NL).encode('utf-8')), (name + '.json', (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, n)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)


def captured(mod):
    """b670's (or b672's) bank writers replaced in memory: each bank the route would write is kept here and not written."""
    store = {}
    mod.put_txt = lambda name, lines: store.__setitem__(name, lines)
    mod.put_json = lambda name, obj: store.__setitem__(name, obj)
    return store


def verdict(lines):
    v = [l for l in lines if l.startswith('### ### **')]
    return v[-1] if v else '### NO VERDICT LINE'


HEAD = ('### THE PAIR RULE (relay data/b670_rules.txt :5-:7): two consecutive reading acts agreeing on the four readings; b670 reading 1 of 2, '
        'this act reading 2. Each reading below prints b670`s figure beside b680`s, by b670`s method, the method cited by line.')


# ================================================================================ (i) THE LICENSED TABLE
NEW_CUTS = {   # ### the kernels cut since b670 (b674, b676, b678): each cut bank prints b670`s distance before and after; the figure after stands
    'SIDE-window': ('data/b674_cut.txt', 'THE DISTANCE BEFORE 5, AFTER 1'),
    'SIDE-trivium': ('data/b676_cut.txt', 'THE DISTANCE BEFORE 5, AFTER 1'),
    'SIDE-silence-principle': ('data/b678_cut.txt', 'THE DISTANCE BEFORE 4, AFTER 1'),
}


def licensed(*a):
    import b670_record as B
    store = captured(B)
    B.licensed()
    T0 = store['b670_licensed_table.txt']
    J = store['b670_licensed_table.json']
    rows, ext = [], []
    for r in J['agenda']:
        m = re.match(r'(SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)', r['doc'])
        if m and m.group(1) in NEW_CUTS:
            cb, nd = NEW_CUTS[m.group(1)]
            t = rd(os.path.join(ROOT, cb))
            ln = [i + 1 for i, l in enumerate(t.split(NL)) if nd in l]
            if not ln:
                sys.exit('### %s DOES NOT CARRY %r -- NOTHING WRITTEN' % (cb, nd))
            after = int(re.search(r'AFTER (\d+)', nd).group(1))
            ext.append('%s : %s :%d "%s" (b670 read it at %d)' % (m.group(1), cb, ln[0], nd, r['now']))
            r = dict(r, now=after, by='%s :%d (cut, %s)' % (cb, ln[0], nd))
        rows.append(r)
    tot = sum(r['now'] for r in rows)
    b670 = re.search(r'ROWS OUTSIDE LICENSED OR CITED (\d+)', rdn('b670_licensed_table.txt').split(NL)[122]).group(1)
    A = [l for l in T0 if l.startswith('  ') and 'constellation [' not in l and ' constellation ' in l]
    L = ['b680 -- COMPONENT 2 (i), (R290)(4)(i): THE LICENSED TABLE OVER THE ROSTER, READING 2 OF 2, BY b670`S METHOD (%s)' % utc(), '', HEAD,
         '### the method: tools/b670_record.py `licensed` (:587-:655) and `agenda` (:550-:584), run here by import; the count outside LICENSED or',
         '### CITED is OVERREACHES + UNLICENSED per agenda document of relay data/b648_recut_order.txt, a cut bank`s line replacing a document cut',
         '### since its read (b670`s CUT_BANKS, :521-:530). THE GROWTH SINCE b670, DECLARED: three kernels cut since, each cut bank printing b670`s',
         '### distance before and after; the figure after stands for each:'] + ['    ' + x for x in ext] + [
         '', '### A. PER ROSTER TABLE (b670`s route`s own lines): constellation [actionable, provenance, external, historical] ; rowgen diff [checked,',
         '### present, STALE, unmapped]'] + A + ['', verdict([l for l in T0 if 'ROSTER TABLES' in l]), '',
         '### B. PER AGENDA DOCUMENT: b648 -> b670 -> b680 (rows outside LICENSED or CITED), the bank that gives b680`s figure:']
    b70 = dict((r['doc'], r['now']) for r in json.loads(rdn('b670_licensed_table.json') or '{"agenda": []}').get('agenda', [])) if os.path.exists(os.path.join(D, 'b670_licensed_table.json')) else {}
    for r in rows:
        L.append('  %-62s %4d -> %4s -> %4d   [%s]%s' % (r['doc'][:62], r['b648'], b70.get(r['doc'], '-'), r['now'], r['by'], ('  ### ' + r['moved']) if r['moved'] else ''))
    zero = sum(1 for r in rows if r['now'] == 0)
    L += ['', '### ### **AGENDA DOCUMENTS %d ; ROWS OUTSIDE LICENSED OR CITED %d AGAINST b670`S %s (relay data/b670_licensed_table.txt :123) ; DOCUMENTS '
          'AT ZERO %d ; THE DISTANCE FROM THE PAIR`S BAR %d.**' % (len(rows), tot, b670, zero, tot)]
    put('b680_licensed', L, dict(at=utc(), total=tot, b670=int(b670), zero=zero, agenda=rows, growth=ext))
    print(NL.join(L[-1:]))


# ================================================================================ (ii) THE CORRESPONDENCE DISTANCE
def corr(*a):
    import b670_record as B
    import b672_record as B2
    s1 = captured(B)
    B.corr()
    v1 = verdict(s1['b670_correspondence.txt'])
    s2 = captured(B2)
    B2.after()
    T2 = s2['b672_correspondence_after.txt']
    vv = [l for l in T2 if l.startswith('### ### **')]
    m1 = re.search(r'BEHIND (\d+)', v1)
    m2 = re.search(r'ROWS WITH A COMMIT (\d+) .*? BEHIND (\d+) \(b670', vv[-2]) if len(vv) >= 2 else None
    m3 = re.search(r'AT THE LEADING CLAUSE \(THE GENERATOR`S CLAIM\) (\d+)', vv[-1]) if vv else None
    L = ['b680 -- COMPONENT 2 (ii), (R290)(4)(ii): THE CORRESPONDENCE DISTANCE, READING 2 OF 2, BY b670`S METHOD AND BY THE GENERATOR`S CLAIM (%s)' % utc(), '',
         HEAD,
         '### the methods: b670`s (tools/b670_record.py `corr`, :678-:784), run by import, the tables re-found by their heading text as b670 read',
         '### them; and b672`s re-read of the same method after the generator (tools/b672_record.py `after`, :490-:610), the tables found by their',
         '### stable anchors (relay data/b672_roster_read.json), which b670`s state line names for this reading (relay data/b670_state.txt :26-),',
         '### its generator readings and shapes those b672 banked (relay data/b672_correspondence_diff.json) -- declared: the generator`s shape',
         '### status of each table is b672`s, the rows, commits and tags read now.', '',
         '### BY b670`S HEADING-TEXT READER: ' + v1,
         '### BY THE STABLE ANCHORS (b672`s re-read): ' + (vv[-2] if len(vv) >= 2 else '### UNREAD'),
         '### THE GENERATOR`S CLAIM: ' + (vv[-1] if vv else '### UNREAD'), '',
         '### ### **BEHIND BY b670`S METHOD %s AGAINST 54 (relay data/b672_correspondence_after.txt :181) ; AT THE GENERATOR`S CLAIM %s AGAINST 0 (:182) ; '
         'BY b670`S HEADING-TEXT READER %s AGAINST b670`S 90.**' % (m2.group(2) if m2 else '### UNREAD', m3.group(1) if m3 else '### UNREAD',
                                                                   m1.group(1) if m1 else '### UNREAD'), '',
         '### THE ANCHORED RE-READ, WHOLE:'] + T2
    put('b680_correspondence', L, dict(at=utc(), b670_reader=v1, anchored=vv, behind=int(m2.group(2)) if m2 else None,
                                       claim=int(m3.group(1)) if m3 else None, heading_reader=int(m1.group(1)) if m1 else None))
    print(L[13])


# ================================================================================ (iii) THE CEILING AND ITS SUCCESSOR
def ceiling(*a):
    import hashlib
    import b670_record as B
    import b674_record as B4
    store = captured(B)
    B.ceiling()
    T1 = store['b670_ceiling.txt']
    fl = json.loads(rdn('b674_record_lines_c2.json') or '{}').get('lines') or []
    fline = fl[0]['line'] if fl else None
    rows = []
    for f, n in (('README.md', 127), ('REGISTRY.md', 962), ('FINDINGS.md', fline)):
        _l, s, h = B4._placement(f, n)
        rows.append(('%s :%s' % (f, n), len(s.encode('utf-8')) if s else None, h))
    eq = len(set(h for _p, _b, h in rows if h)) == 1 and all(h for _p, _b, h in rows)
    L = ['b680 -- COMPONENT 2 (iii), (R290)(4)(iii): THE CEILING`S THREE SITES AND THE SUCCESSOR`S THREE, READING 2 OF 2, BY b670`S CEILING ROUTE (%s)' % utc(),
         '', HEAD,
         '### the method: tools/b670_record.py `ceiling` (:798-:843), run by import, each placement`s sentence by its own delimiters and hashed alone;',
         '### the successor (the (R284)(3) sentence placed at b674) by the same delimiters through b674`s `_placement` (tools/b674_record.py `ceilingdiff`,',
         '### :306-:338), the FINDINGS placement at relay data/b674_record_lines_c2.json`s line.', '', '### THE (R183)(3) SENTENCE (b670`s route`s own rows):'] + \
        [l for l in T1 if l.startswith('  ')] + ['', '### THE SUCCESSOR, ROWS ARE SITES:'] + ['  %-22s bytes %s ; sha256 %s' % r for r in rows] + [
        '', '### ### **THE CEILING SENTENCE %s ; b670: EQUAL AT THREE PLACEMENTS, ONE HASH (relay data/b670_ceiling.txt :25) ; THE SUCCESSOR BYTE-EQUAL AT ITS THREE '
        'SITES %s.**' % (verdict(T1).replace('### ### **', '').rstrip('*').rstrip('.'), eq)]
    put('b680_ceiling', L, dict(at=utc(), ceiling=verdict(T1), successor=[list(r) for r in rows], successor_equal=eq))
    print(L[-1])


# ================================================================================ (iv) THE ORDERS CENSUS
def orders(*a):
    import b670_record as B
    store = captured(B)
    Q = B.orders()
    if Q is None:
        Q = store['b670_work_orders.json']['orders']
    for o in Q:
        o['age'] = 680 - int(o['act'][1:]) if o['act'] else -1
    op = [o for o in Q if o['open']]
    ns = [o for o in Q if o['status'] == 'NOT STATED']
    old = [o for o in op if o['age'] > 10 and not re.match(r'(?i)^(its )?trigger met$|^re-dated$', o['status'])]
    L = ['b680 -- COMPONENT 2 (iv), (R290)(4)(iv): THE ORDERS CENSUS, READING 2 OF 2, BY b670`S QUEUE READER (%s)' % utc(), '', HEAD,
         '### the method: tools/b670_record.py `read_queue` and `orders` (:862-:964), run by import over OPEN_TRAILS at HEAD; the age counted from',
         '### the reading act (680 less the entry act; b670 counted from 670 -- declared). Rows are orders; every no-status row named beneath.', '',
         '  %-44s %-7s %-6s %-5s %-16s %s' % ('order', 'entry', 'act', 'age', 'status', 'at')]
    L += ['  %-44s :%-6d %-6s %-5d %-16s %s' % (o['name'], o['line'], o['act'] or '-', o['age'], o['status'],
                                              (':%d' % o['status_line']) if o['status_line'] else ':%d' % o['last_line']) for o in Q]
    LL = rd(OT).split(NL)
    L += ['', '### EVERY ORDER WHOSE STATUS THE READER CANNOT FIND, BY NAME, at its last line naming it:']
    for o in ns:
        l = LL[o['last_line'] - 1]
        i = l.find(o['name'])
        L.append('  %-44s :%-6d %s' % (o['name'], o['last_line'], ' '.join(l[max(0, i - 40):i + 120].split())))
    L += ['', '### ### **ORDERS %d ; OPEN %d ; DONE %d ; NO STATUS %d -- AGAINST b670`S 34 / 46 / 69 (relay data/b670_work_orders.txt :250) ; OPEN AND OLDER '
          'THAN TEN ACTS WITHOUT A TRIGGER MET OR A RE-DATING %d (b670: 33).**' % (len(Q), len(op), len(Q) - len(op) - len(ns), len(ns), len(old))]
    put('b680_orders', L, dict(at=utc(), total=len(Q), open=len(op), done=len(Q) - len(op) - len(ns), no_status=[o['name'] for o in ns], old=len(old)))
    print(L[-1])


# ================================================================================ (v) THE METHODS' READINESS
def methods(*a):
    import b670_record as B
    store = captured(B)
    B.methods()
    T1 = store['b670_methods.txt']
    L = ['b680 -- COMPONENT 2 (v), (R290)(4)(v): THE METHODS` READINESS, READING 2 OF 2, BY b670`S TABLE (%s)' % utc(), '', HEAD,
         '### the method: tools/b670_record.py `methods` (:1012-:1061) and its twelve rows METHODS (:972-:1009), run by import over relay data/ now;',
         '### relay data/b670_rules.txt row 2 the criteria. b670`s figure: "AT b671: METHODS 12 ; READY 11" (relay data/b670_methods.txt :88).', ''] + \
        [l for l in T1 if l.startswith('===') or l.startswith('    ')]
    v = verdict(T1)
    m = re.search(r'READY (\d+)', v)
    code = int(m.group(1)) if m else None
    rows = dict((x.split(' -- ')[0][4:], x.split(' -- ')[-1]) for x in T1 if x.startswith('==='))
    # ### the cells read by hand, as b670`s table reads its defect cells (:1048-:1049) and as b671`s dated line read its two rows
    # ### (relay data/b670_methods.txt :76-:88); each hand-read cell checked against its bank line here
    hand = []
    for meth, bank, ln, needle in (('the consumers section', 'b671_defects.txt', 22, '(d) '),
                                   ('the argument-principle certification', 'b671_defects.txt', 35, '(f) '),
                                   ('the ζ-naming walk (the declaration closure counted for ζ objects)', 'b679_defects.txt', 22, "(e) THE SEAT'S: A NAMESAKE THE CARRIED WALK FOLLOWED")):
        ok = needle in (rdn(bank).split(NL)[ln - 1] if len(rdn(bank).split(NL)) >= ln else '')
        hand.append((meth, rows.get(meth), 'data/%s :%d' % (bank, ln), ok))
    walk_acts = sorted(set(f[:4] for f in os.listdir(D) if re.search(r'^b572_lemmas\.txt$|_zeta_walk\.txt$', f)))
    after = dict(rows)
    for meth, _was, _c, ok in hand:
        if ok:
            after[meth] = 'READY'
    nready = sum(1 for x in after.values() if x == 'READY')
    L += ['', '### THE HAND-READ CELLS, by the table`s own criteria (relay data/b670_rules.txt row 2):',
          '    the two rows b671 read at their second act (relay data/b670_methods.txt :76-:88), their defect cells at the lines below;',
          '    the ζ-naming walk: acts %s (its banks by b670`s pattern), and now a lettered defect naming a failure of it -- b679`s (e), the' % ' '.join(walk_acts),
          '    carried walk following a namesake:'] + [
        '    %-70s by b670`s code %-20s ; the cell %s read %s -> %s' % (meth, was, cite, ok, 'READY' if ok else was) for meth, was, cite, ok in hand]
    L += ['', '### ### **BY b670`S CODE READY %s OF 12 (b670: 9, relay data/b670_methods.txt :74) ; WITH THE HAND-READ CELLS READY %d OF 12 AGAINST b670`S '
          '11 OF 12 (b671`s dated line, :88).**' % (code, nready)]
    put('b680_methods', L, dict(at=utc(), verdict=v, ready_code=code, ready=nready, hand=[list(x) for x in hand]))
    print(L[-1])


# ================================================================================ (vi) THE NINE-KERNELS ITEM
NINE = ('SIDE-archimedean', 'SIDE-bsd-formation-transfer', 'SIDE-compression', 'SIDE-frobenius', 'SIDE-rcurve', 'SIDE-silence-principle',
        'SIDE-simplicity', 'SIDE-spinor', 'SIDE-yang-mills-formation')
RECUT = ('SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle')


def kernels9(*a):
    import correspondence_gen as CG
    ks = sorted(set(NINE) | set(RECUT))
    tags, tlog = CG.read_tags(ks, remote=False)
    banks, blog = CG.read_banks(tags)
    rows = []
    for k in ks:
        t = tags.get(k)
        runner = sorted(f for f in os.listdir(D) if re.match(r'^b\d+_axioms_%s_(after|before)\.txt$' % re.escape(k), f))
        at_tag = []
        for f in runner:
            rb = rd(os.path.join(D, f.replace('_axioms_', '_runner_')))
            m = re.search(r'the ref input ([0-9a-f]{40})', rb) or re.search(r'the ref built \(out/ref\.txt\): ([0-9a-f]{40})', rb)
            if t and m:
                full = m.group(1)
                ok = full == t[1] or (g('D:/' + k, 'merge-base', '--is-ancestor', full, t[1]) == '' and
                                      not [x for x in g('D:/' + k, 'diff', '--name-only', full, t[1], '--', '*.lean').split(NL) if x.strip()])
                at_tag.append((f, full[:7], ok))
        gen = banks.get(k)
        rows.append(dict(kernel=k, tag=t[0] if t else 'NO TAG', in_nine=k in NINE, generator=(gen['file'] if gen else None),
                         runner=[list(x) for x in at_tag], held=bool(gen) or any(ok for _f, _c, ok in at_tag)))
    held = [r for r in rows if r['held']]
    L = ['b680 -- COMPONENT 2 (vi), (R290)(4)(vi): THE NINE-KERNELS ITEM, THE KERNELS NOW HOLDING A PRINT BANK AT A TAG (%s)' % utc(), '', HEAD,
         '### b670 made no such reading: its b670 column is NOT COMPARABLE (b670 made no reading of print banks at tags); the item is b672`s',
         '### (OPEN_TRAILS :14440, nine kernels whose tag no relay print bank reached). Two readers, each printed: the generator`s (tools/',
         '### correspondence_gen.py read_tags locally and read_banks, its bank names `bNNN_runner_SIDE-x[_runN].txt`), and the re-cut acts`',
         '### runner banks `bNNN_axioms_SIDE-x_after.txt` with their runner bank`s ref, at the tag where the ref is the tag`s commit or an ancestor',
         '### with no .lean file differing. Rows are kernels:']
    L += ['  %-30s tag %-8s in b672`s nine %-5s ; the generator`s reader %s ; the runner banks %s ; %s' % (
        r['kernel'], r['tag'], r['in_nine'], r['generator'] or 'NO PRINT BANK', '; '.join('%s built %s at the tag %s' % tuple(x) for x in r['runner']) or 'NONE',
        'HOLDS A PRINT BANK AT ITS TAG' if r['held'] else 'STILL WITHOUT') for r in rows]
    still = [r['kernel'] for r in rows if r['in_nine'] and not r['held']]
    L += ['', '### of b672`s nine, still without: %s' % (', '.join(still) or 'NONE'),
          '### holding one now: %s' % ', '.join('%s %s' % (r['kernel'], r['tag']) for r in held),
          '### the generator`s reader sees: %s' % (', '.join(r['kernel'] for r in rows if r['generator']) or 'NONE -- its bank names do not match the runner banks`'),
          '', '### ### **b680: PRINT BANKS AT A TAG %d OF %d KERNELS READ (THE NINE %d HOLDING, %d STILL WITHOUT) ; b670: NOT COMPARABLE ; b672: 0 OF 9.**' % (
              len(held), len(rows), sum(1 for r in rows if r['in_nine'] and r['held']), len(still))]
    put('b680_kernels9', L, dict(at=utc(), rows=rows, still=still))
    print(L[-1])


# ================================================================================ (vii) THE RESIDUES OF THE RE-CUT ACTS
RESIDUES = [
    ('b674', 'SIDE-window', 'data/b674_cut.txt', 28, 'the marker at :17', 'SIDEWindow/Sawtooth.lean :17, "(a) ... S_k acts on each class as the adjacency matrix of a PATH GRAPH on its members. ← COMBINATORIAL, COMPILED HERE"'),
    ('b676', 'SIDE-trivium', 'data/b676_cut.txt', 38, 'correspond', 'Trivium/Bijection.lean :8, the introduction`s "correspond exactly"'),
    ('b676', 'SIDE-trivium', 'data/b676_cut.txt', 39, 'seven nontrivial elements', 'Trivium/Bijection.lean :23, "The seven discriminants are exactly the seven nontrivial elements of (ℤ/2)³"'),
    ('b678', 'SIDE-silence-principle', 'data/b678_cut.txt', 43, 'In coupled systems', 'SIDESilencePrinciple/Basic.lean :7-:12, the introduction`s statement of the principle'),
    ('b678', 'SIDE-silence-principle', 'data/b678_cut.txt', 55, 'Silence yields Protection', 'SIDESilencePrinciple/Basic.lean :412, the bold title "(Silence yields Protection)" of Theorem 8.1'),
]


def residues(*a):
    rows = []
    for act, k, bank, ln, nd, what in RESIDUES:
        L_ = rdn(os.path.basename(bank)).split(NL)
        win = ' '.join(L_[ln - 2:ln + 1])
        rows.append((act, k, bank, ln, nd in win, what))
    by = collections.Counter(k for _a, k, _b, _l, _o, _w in rows)
    L = ['b680 -- COMPONENT 2 (vii), (R290)(4)(vii): THE RESIDUES OF THE RE-CUT ACTS b674, b676, b678, BY DOCUMENT (%s)' % utc(), '', HEAD,
         '### b670 made no such reading: its b670 column is NOT COMPARABLE (the re-cut acts came after it). The residue of a cut is the sentence',
         '### its ACTION, applied verbatim and not extended, did not reach, as the cut bank names it; rows are sentences with the bank line that',
         '### names them (the needle read within a line of it):']
    L += ['  %-5s %-24s %s :%d (needle %s) -- %s' % (act, k, bank, ln, ok, what) for act, k, bank, ln, ok, what in rows]
    L += ['', '### by document: %s' % ', '.join('%s %d' % kv for kv in sorted(by.items())),
          '', '### ### **RESIDUES %d SENTENCES IN %d DOCUMENTS (%s) ; EVERY NEEDLE READ %s ; b670: NOT COMPARABLE.**' % (
              len(rows), len(by), ', '.join('%s %d' % kv for kv in sorted(by.items())), all(r[4] for r in rows))]
    put('b680_residues', L, dict(at=utc(), rows=[list(r) for r in rows], by=dict(by)))
    print(L[-1])


# ================================================================================ (viii) THE KEYSTONE LAG
def lag(*a):
    import b670_record as B
    cor = rdn('b586_corroboration.txt').split(NL)
    meta = dict((l.split('|')[1].strip(), [x.strip() for x in l.split('|')]) for l in cor if l.startswith('| ') and not l.startswith('| document'))
    rows = []
    for n, p in B.roster():
        t = rd(os.path.join(PP, p)).split(NL)
        acts = [(int(m.group(1)), i + 1) for i, l in enumerate(t) for m in re.finditer(r'\bb(\d{3})\b', l)]
        carried = max(acts) if acts else None
        ks = [k.strip() for k in meta[n][5].split(',') if k.strip().startswith('SIDE-')]
        touched = []
        for k in ks:
            kd = 'D:/' + k
            if not os.path.isdir(os.path.join(kd, '.git')):
                continue
            for s in g(kd, 'log', '--format=%h %s', 'main').split(NL):
                m = re.search(r'\bb(\d{3})\b', s)
                if m:
                    touched.append((int(m.group(1)), k, s.split(' ', 1)[0]))
                    break
        last = max(touched) if touched else None
        lagv = (last[0] - carried[0]) if (last and carried) else None
        rows.append(dict(doc=n, path=p, carried=carried, kernels=ks, touched=last, lag=lagv))
    L = ['b680 -- COMPONENT 2 (viii), (R290)(4)(viii): THE KEYSTONE LAG OVER THE ROSTER (%s)' % utc(), '', HEAD,
         '### b670 made no such reading: its b670 column is NOT COMPARABLE. The roster: the 19 tables of relay data/b586_corroboration.txt :34. For',
         '### each: the last act whose finding its text carries (the highest bNNN its text names, with the line), the last act that touched its',
         '### object (the newest commit on main of each kernel b586 lists for it whose subject names a bNNN, with the kernel and commit), and the',
         '### lag in acts between them (positive: the object moved after the text`s last act).', '']
    for r in rows:
        L.append('  %-36s text b%s :%s ; object %s ; lag %s' % (r['doc'], r['carried'][0] if r['carried'] else '-', r['carried'][1] if r['carried'] else '-',
                                                           ('b%d %s %s' % r['touched']) if r['touched'] else 'NO bNNN COMMIT ON ITS KERNELS` MAINS', r['lag'] if r['lag'] is not None else '-'))
    lags = [r['lag'] for r in rows if r['lag'] is not None]
    L += ['', '### ### **KEYSTONES 19 ; WITH A LAG READ %d ; LAGGING (OBJECT MOVED AFTER THE TEXT) %d ; THE LARGEST LAG %s ; THE MEDIAN %s ; b670: NOT COMPARABLE.**' % (
        len(lags), sum(1 for x in lags if x > 0), max(lags) if lags else '-', sorted(lags)[len(lags) // 2] if lags else '-')]
    put('b680_lag', L, dict(at=utc(), rows=rows))
    print(L[-1])


# ================================================================================ (ix) THE OUTSIDE-READER TEST
ENTRIES = (('b673', 8819), ('b674', 8851), ('b675', 8881), ('b676', 8913), ('b677', 8943), ('b678', 9022), ('b679', 9050))
CLAIM = re.compile(r'^(?!\*|##|$).{80,}')
CERT = re.compile(r'(?i)\b(DERIVES|run \d{8,}|certified|relay `?data/|byte for byte|read back)\b')
REFUTE = re.compile(r'(?i)\b(refut\w*|would (?:stand against|refute|fail)|REFUTED|against the bound|a line against)\b')


def outside(*a):
    F = rd(FIND).split(NL)
    rows = []
    for act, e in ENTRIES:
        end = next((i for i in range(e, len(F)) if F[i].startswith('## ')), len(F))
        body = list(enumerate(F[e - 1:end], e))
        c = next(((i, l) for i, l in body[1:] if CLAIM.match(l)), None)
        ce = next(((i, l) for i, l in body[1:] if CERT.search(l)), None)
        rf = next(((i, l) for i, l in body[1:] if REFUTE.search(l)), None)
        rows.append(dict(act=act, entry=e, end=end, claim=c[0] if c else None, cert=ce[0] if ce else None, refute=rf[0] if rf else None,
                         refute_word=REFUTE.search(rf[1]).group(1) if rf else None))
    L = ['b680 -- COMPONENT 2 (ix), (R290)(4)(ix): THE OUTSIDE-READER TEST OVER THE FINDINGS ENTRIES OF b673 THROUGH b679 (%s)' % utc(), '', HEAD,
         '### b670 made no such reading: its b670 column is NOT COMPARABLE. Rows are entries: for each, does its text answer what is claimed (the',
         '### first line of its body not a heading, an italic filing line or blank, 80 characters or more: its result sentence), what certifies it',
         '### (a line naming a derivation, a run, a certified figure, a relay bank or a read-back), and what would refute it (a line naming a',
         '### refutation, a REFUTED reading or what would stand against it) -- each a YES with the line or a NO. The matchers are printed above',
         '### the rows; every YES line and every NO hand-read in the closing`s dry run.', '',
         '### the matchers: claim %r ; certifies %r ; refutes %r' % (CLAIM.pattern, CERT.pattern, REFUTE.pattern), '']
    for r in rows:
        L.append('  %-5s FINDINGS :%-5d claimed %-9s certified %-9s refuted %s' % (
            r['act'], r['entry'], ('YES :%d' % r['claim']) if r['claim'] else 'NO', ('YES :%d' % r['cert']) if r['cert'] else 'NO',
            ('YES :%d ("%s")' % (r['refute'], r['refute_word'])) if r['refute'] else 'NO'))
    yes = lambda k: sum(1 for r in rows if r[k])   # noqa: E731
    L += ['', '### ### **ENTRIES 7 ; CLAIMED YES %d ; CERTIFIED YES %d ; REFUTATION NAMED YES %d ; ALL THREE %d ; b670: NOT COMPARABLE.**' % (
        yes('claim'), yes('cert'), yes('refute'), sum(1 for r in rows if r['claim'] and r['cert'] and r['refute']))]
    put('b680_outside', L, dict(at=utc(), rows=rows))
    print(NL.join(L[-9:]))


ROUTES = {'licensed': licensed, 'corr': corr, 'ceiling': ceiling, 'orders': orders, 'methods': methods, 'kernels9': kernels9,
          'residues': residues, 'lag': lag, 'outside': outside}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b680_readings.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
