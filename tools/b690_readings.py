# -*- coding: utf-8 -*-
"""b690_readings.py -- COMPONENT 2, (R300)(3): READING 3, EACH READING BY CODE WHERE A TOOL READS IT AND BY HAND WHERE NONE DOES, b680'S FIGURE
(READING 2) PRINTED BESIDE WHERE b680 TOOK THE SAME READING.

### THE METHOD IS b670'S AND b680'S CODE, NOT A COPY: the licensed table, the Correspondence, the ceiling, the orders, the methods and the lag
### import tools/b670_record.py, tools/b672_record.py and tools/b680_readings.py and run their own routes, their bank writers replaced in memory
### so that nothing of b670's, b672's or b680's is written; the captured lines are re-banked here. Where the method reads data that grew since
### b680 (the cut banks of b682, b684, b686, b688; the age of an order counted from 690), the growth is declared beside the figure. Readings b680
### did not take (the rules and arms census, the P3 grep, the one-copy re-read) are read as the ruling words them; each row says whether its
### value is the tool's or the seat's hand.
### Routes, one per reading, each one foreground process under the 600 s limit: licensed | corr | ceiling | orders | methods | lag | residues |
### rules | arms | p3 | onecopy | pair -> data/b690_r3_<name>.txt (.json); `bank` -> data/b690_reading3.txt (.json), the readings gathered
### with their hand rows, written after every route's bank. Written by the Write tool at b690; it writes only those banks.
"""
import collections
import glob
import importlib
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
ACT = 690


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def rdn(n):
    return rd(os.path.join(D, n))


def jn(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def put(name, lines, obj):
    for n, b in ((name + '.txt', (NL.join(lines) + NL).encode('utf-8')), (name + '.json', (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, n)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)


def captured(mod):
    store = {}
    mod.put_txt = lambda name, lines: store.__setitem__(name, lines)
    mod.put_json = lambda name, obj: store.__setitem__(name, obj)
    return store


def r80():
    """b680's readings tool, its own bank writer captured: nothing of b680's is written."""
    import b680_readings as R
    store = {}
    R.put = lambda name, lines, obj: store.__setitem__(name, (lines, obj))
    return R, store


def verdict(lines):
    v = [l for l in lines if l.startswith('### ### **')]
    return v[-1] if v else '### NO VERDICT LINE'


HEAD = ('### READING 3 (b690, under (R300)(3)). b680 took reading 2 (tools/b680_readings.py, its banks data/b680_<name>.txt); b670 reading 1. '
        'Each figure below is the tool`s where a tool reads it, the seat`s hand where none does, and says which.')


# ================================================================================ (i) THE LICENSED TABLE, BY b670'S METHOD
# ### the kernels cut since b670, each by the bank line that carries its standing figure after its last cut (read, not typed: each needle is
# ### checked on its line and the figure after is parsed from it)
CUTS = {
    'SIDE-window': ('data/b684_cut.txt', 78, 'SIDE-window before 1 (relay data/b674_cut.txt) ; after 0', r'after (\d+)'),
    'SIDE-trivium': ('data/b684_cut.txt', 78, 'SIDE-trivium before 1 (relay data/b676_cut.txt) ; after 0', r'trivium before 1 \(relay data/b676_cut.txt\) ; after (\d+)'),
    'SIDE-silence-principle': ('data/b684_cut.txt', 79, 'SIDE-silence-principle before 1 (relay data/b678_cut.txt) ; after 0', r'after (\d+)'),
    'SIDE-bijection': ('data/b682_cut.txt', 55, 'THE DISTANCE BEFORE 4, AFTER 0', r'AFTER (\d+)'),
    'SIDE-class-number-anomaly': ('data/b684_cut.txt', 44, 'THE DISTANCE BEFORE 3, AFTER 0', r'AFTER (\d+)'),
    'SIDE-spinor': ('data/b688_residue_actions.txt', 49, "distance by b670's method 1 -> 0", r'method \d+ -> (\d+)'),
    'SIDE-li-map': ('data/b688_cut.txt', 68, 'THE DISTANCE BEFORE 3, AFTER 0', r'AFTER (\d+)'),
}


def licensed(*a):
    import b670_record as B
    store = captured(B)
    B.licensed()
    T0 = store['b670_licensed_table.txt']
    J = store['b670_licensed_table.json']
    rows, ext, used = [], [], set()
    for r in J['agenda']:
        m = re.match(r'(SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)', r['doc'])
        if m and m.group(1) in CUTS:
            cb, ln, nd, pat = CUTS[m.group(1)]
            line = (rd(os.path.join(ROOT, cb)).split(NL) + [''] * ln)[ln - 1]
            if nd not in line:
                sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (cb, ln, nd))
            after = int(re.search(pat, line[line.index(nd):]).group(1))
            ext.append('%s : %s :%d "%s" (b670`s route read it at %d)' % (m.group(1), cb, ln, nd, r['now']))
            r = dict(r, now=after, by='%s :%d (cut, %s)' % (cb, ln, nd))
            used.add(m.group(1))
        rows.append(r)
    unused = sorted(set(CUTS) - used)
    tot = sum(r['now'] for r in rows)
    b680 = jn('b680_licensed.json')
    A = [l for l in T0 if l.startswith('  ') and ' constellation ' in l]
    zero = sum(1 for r in rows if r['now'] == 0)
    L = ['b690 -- COMPONENT 2 (i), (R300)(3): THE LICENSED TABLE OVER THE ROSTER AND THE AGENDA, READING 3, BY b670`S METHOD (%s)' % utc(), '', HEAD,
         '### the method: tools/b670_record.py `licensed` (:587-:655) and `agenda` (:550-:584), run here by import (b680`s way); the count outside',
         '### LICENSED or CITED is OVERREACHES + UNLICENSED per agenda document of relay data/b648_recut_order.txt, a cut bank`s line replacing a',
         '### document cut since its read. THE GROWTH SINCE b680, DECLARED: the kernels cut since b670, each by the bank line carrying its figure',
         '### after its last cut:'] + ['    ' + x for x in ext] + ['    the cuts named and not found on the agenda: %s' % (unused or 'NONE'),
         '', '### A. PER ROSTER TABLE (b670`s route`s own lines): constellation [actionable, provenance, external, historical] ; rowgen diff [checked,',
         '### present, STALE, unmapped]'] + A + ['', verdict([l for l in T0 if 'ROSTER TABLES' in l]), '',
         '### B. PER AGENDA DOCUMENT: b648 -> b680 -> b690 (rows outside LICENSED or CITED), the bank that gives b690`s figure:']
    b80 = dict((r['doc'], r['now']) for r in b680.get('agenda', []))
    for r in rows:
        L.append('  %-62s %4d -> %4s -> %4d   [%s]%s' % (r['doc'][:62], r['b648'], b80.get(r['doc'], '-'), r['now'], r['by'],
                                                       ('  ### ' + r['moved']) if r['moved'] else ''))
    L += ['', '### ### **AGENDA DOCUMENTS %d ; ROWS OUTSIDE LICENSED OR CITED %d AGAINST b680`S %s (relay data/b680_licensed.txt) ; DOCUMENTS AT ZERO %d '
          'AGAINST b680`S %s.**' % (len(rows), tot, b680.get('total'), zero, b680.get('zero'))]
    put('b690_r3_licensed', L, dict(at=utc(), total=tot, b680=b680.get('total'), zero=zero, zero_b680=b680.get('zero'), docs=len(rows), agenda=rows,
                                    growth=ext, unused=unused, roster_verdict=verdict([l for l in T0 if 'ROSTER TABLES' in l])))
    print(L[-1])


# ================================================================================ (ii) THE CORRESPONDENCE, BY b670'S METHOD AND THE GENERATOR'S CLAIM
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
    b80 = jn('b680_correspondence.json')
    held = 'WRITTEN 0 ; HELD 5' in rdn('b688_correspondence_dry_2.txt')
    L = ['b690 -- COMPONENT 2 (ii), (R300)(3): THE CORRESPONDENCE CELLS, READING 3, BY b670`S METHOD AND BY THE GENERATOR`S CLAIM, THE HAND COUNT BESIDE (%s)' % utc(),
         '', HEAD,
         '### the methods: b670`s (tools/b670_record.py `corr`) by its heading-text reader, and b672`s re-read over the stable anchors (tools/',
         '### b672_record.py `after`), each run by import, their writers captured (b680`s and b686`s way).', '',
         '### BY b670`S HEADING-TEXT READER: ' + v1,
         '### BY THE STABLE ANCHORS (b672`s re-read): ' + (vv[-2] if len(vv) >= 2 else '### UNREAD'),
         '### THE GENERATOR`S CLAIM: ' + (vv[-1] if vv else '### UNREAD'),
         '### THE HAND COUNT (the seat`s, from the banks): the cells held unwritten under W-ORD-CORRESPONDENCE-CARRIED-AT -- five, "WRITTEN 0 ; HELD 5"',
         '### in relay data/b688_correspondence_dry_2.txt: %s; no Correspondence cell written since b686 (data/b688_cut.txt, the held five).' % held, '',
         '### ### **BEHIND BY b670`S METHOD %s AGAINST b680`S %s ; AT THE GENERATOR`S CLAIM %s AGAINST b680`S %s ; BY THE HEADING-TEXT READER %s AGAINST '
         'b680`S %s ; HELD BY HAND 5.**' % (m2.group(2) if m2 else '### UNREAD', b80.get('behind'), m3.group(1) if m3 else '### UNREAD', b80.get('claim'),
                                           m1.group(1) if m1 else '### UNREAD', b80.get('heading_reader')), '', '### THE ANCHORED RE-READ, WHOLE:'] + T2
    put('b690_r3_corr', L, dict(at=utc(), behind=int(m2.group(2)) if m2 else None, claim=int(m3.group(1)) if m3 else None,
                                heading_reader=int(m1.group(1)) if m1 else None, held_hand=5 if held else None, b680=b80))
    print(L[12])


# ================================================================================ (iii) THE CEILING, BY b680'S ROUTE
def ceiling(*a):
    R, store = r80()
    R.ceiling()
    lines, obj = store['b680_ceiling']
    b80 = jn('b680_ceiling.json')
    same = obj.get('ceiling') == b80.get('ceiling') and obj.get('successor_equal') == b80.get('successor_equal')
    L = ['b690 -- COMPONENT 2 (iii), (R300)(3): THE CEILING`S SITES AND THE SUCCESSOR`S, READING 3, BY b680`S ROUTE (%s)' % utc(), '', HEAD,
         '### the method: tools/b680_readings.py `ceiling` (:155-:178), run by import, its writer captured; its lines re-banked whole:'] + \
        ['    ' + l for l in lines] + ['', '### ### **%s ; THE SUCCESSOR EQUAL AT ITS SITES %s ; AS b680 READ THEM %s.**' % (
            obj.get('ceiling', '').replace('### ### **', '').rstrip('*').rstrip('.'), obj.get('successor_equal'), same)]
    put('b690_r3_ceiling', L, dict(at=utc(), ceiling=obj.get('ceiling'), successor_equal=obj.get('successor_equal'), same_as_b680=same))
    print(L[-1])


# ================================================================================ (iv) THE ORDERS, BY b670'S QUEUE READER
def orders(*a):
    import b670_record as B
    store = captured(B)
    Q = B.orders()
    if Q is None:
        Q = store['b670_work_orders.json']['orders']
    for o in Q:
        o['age'] = ACT - int(o['act'][1:]) if o['act'] else -1
    op = [o for o in Q if o['open']]
    ns = [o for o in Q if o['status'] == 'NOT STATED']
    span = [o for o in Q if o['act'] and 681 <= int(o['act'][1:]) <= 689]
    disc = [o for o in Q if re.search(r'DISCHARGED', o['status'] or '', re.I)]
    b80 = jn('b680_orders.json')
    rv = verdict(store.get('b670_work_orders.txt') or [])
    # ### b670's steadiness predicate (tools/b670_record.py :926, b680's :192), the age from 690
    old = [o for o in op if o['age'] > 10 and not re.match(r'(?i)^(its )?trigger met$|^re-dated$', o['status'])]
    L = ['b690 -- COMPONENT 2 (iv), (R300)(3): THE ORDERS AT OPEN_TRAILS, READING 3, BY b670`S QUEUE READER (%s)' % utc(), '', HEAD,
         '### b670`s route`s own verdict, re-banked (its age counted from 670, tools/b670_record.py :898): ' + rv,
         '### b670`s steadiness predicate (:926) with the age from 690 (b680 the same from 680, tools/b680_readings.py :192): the open orders',
         '### older than ten acts whose status is neither a trigger met nor a re-dating %d.' % len(old),
         '### the method: tools/b670_record.py `read_queue` and `orders` (:862-:964), run by import over OPEN_TRAILS at HEAD (b680`s way); the age',
         '### counted from 690 (b680 counted from 680 -- declared). Rows are orders.', '',
         '  %-44s %-7s %-6s %-5s %-16s %s' % ('order', 'entry', 'act', 'age', 'status', 'at')]
    L += ['  %-44s :%-6d %-6s %-5d %-16s %s' % (o['name'], o['line'], o['act'] or '-', o['age'], o['status'],
                                              (':%d' % o['status_line']) if o['status_line'] else ':%d' % o['last_line']) for o in Q]
    L += ['', '### ENTERED THIS SPAN (b681 through b689, by the entry act): %s' % (', '.join('%s (%s)' % (o['name'], o['act']) for o in span) or 'NONE'),
          '### DISCHARGED (the status word naming it): %d' % len(disc),
          '', '### ### **ORDERS %d ; OPEN %d ; DONE %d ; NO STATUS %d ; DISCHARGED %d ; ENTERED b681-b689 %d ; OPEN AND OLDER THAN TEN ACTS WITHOUT A '
              'TRIGGER MET OR A RE-DATING %d -- AGAINST b680`S %s / %s / %s / %s AND %s.**' % (
              len(Q), len(op), len(Q) - len(op) - len(ns), len(ns), len(disc), len(span), len(old), b80.get('total'), b80.get('open'), b80.get('done'),
              len(b80.get('no_status') or []),
              (re.search(r'WITHOUT A TRIGGER MET OR A RE-DATING (\d+)', rdn('b680_orders.txt')) or re.search('(-)', '-')).group(1))]
    put('b690_r3_orders', L, dict(at=utc(), total=len(Q), open=len(op), done=len(Q) - len(op) - len(ns), no_status=len(ns), discharged=len(disc),
                                  unsteady=len(old), unsteady_names=[o['name'] for o in old],
                                  span=[o['name'] for o in span], b680=dict(total=b80.get('total'), open=b80.get('open'), done=b80.get('done'),
                                                                            no_status=len(b80.get('no_status') or []))))
    print(L[-1])


# ================================================================================ (v) THE METHODS, BY b680'S ROUTE
def methods(*a):
    R, store = r80()
    R.methods()
    lines, obj = store['b680_methods']
    b80 = jn('b680_methods.json')
    L = ['b690 -- COMPONENT 2 (v), (R300)(3): THE METHODS CENSUS, READING 3, BY b680`S ROUTE (b670`s table and its hand-read cells) (%s)' % utc(), '',
         HEAD, '### the method: tools/b680_readings.py `methods` (:212-:247), run by import, its writer captured; its lines re-banked whole and',
         '### unindented, as b680`s bank carries them, so the readers of "the latest methods bank" (tools/rule_arms.py :127-:135) read its rows:'] + \
        list(lines) + ['', '### ### **BY b670`S CODE READY %s OF 12 ; WITH THE HAND-READ CELLS READY %s OF 12 -- AGAINST b680`S %s AND %s.**' % (
            obj.get('ready_code'), obj.get('ready'), b80.get('ready_code'), b80.get('ready'))]
    put('b690_r3_methods', L, dict(at=utc(), ready_code=obj.get('ready_code'), ready=obj.get('ready'), b680=dict(ready_code=b80.get('ready_code'), ready=b80.get('ready'))))
    print(L[-1])


# ================================================================================ (vi) THE KEYSTONE LAG, BY b680'S ROUTE
def lag(*a):
    R, store = r80()
    R.lag()
    lines, obj = store['b680_lag']
    rows = obj['rows']
    lags = sorted(r['lag'] for r in rows if r['lag'] is not None)
    med = lags[len(lags) // 2] if lags else None
    b80 = jn('b680_lag.json').get('rows') or []
    b80l = sorted(r['lag'] for r in b80 if r['lag'] is not None)
    L = ['b690 -- COMPONENT 2 (vi), (R300)(3): THE KEYSTONE LAG PER KEYSTONE, READING 3, BY b680`S ROUTE (%s)' % utc(), '', HEAD,
         '### the method: tools/b680_readings.py `lag` (:327-:362), run by import, its writer captured: for each of the 19 roster tables the last act',
         '### its text names, the last act that touched a kernel b586 lists for it, the lag in acts between. Rows are keystones:'] + \
        ['    ' + l for l in lines if l.startswith('  ')] + [
         '', '### ### **KEYSTONES %d ; WITH A LAG READ %d ; LAGGING %d ; THE MEDIAN %s ; THE MAXIMUM %s -- AGAINST b680`S MEDIAN %s, MAXIMUM %s, LAGGING %d.**' % (
             len(rows), len(lags), sum(1 for x in lags if x > 0), med, lags[-1] if lags else '-', b80l[len(b80l) // 2] if b80l else '-',
             b80l[-1] if b80l else '-', sum(1 for x in b80l if x > 0))]
    put('b690_r3_lag', L, dict(at=utc(), rows=rows, median=med, maximum=lags[-1] if lags else None, lagging=sum(1 for x in lags if x > 0),
                               b680=dict(median=b80l[len(b80l) // 2] if b80l else None, maximum=b80l[-1] if b80l else None)))
    print(L[-1])


# ================================================================================ (vii) THE RESIDUES CENSUS (by hand, each row`s needle checked on its bank line by code)
RESIDUES = [
    ('R1', 'SIDE-window', 'SIDEWindow/Sawtooth.lean :17 marker', 'APPLIED at b684 (v0.5.2)', 'data/b684_cut.txt', 58, 'R1: the :17 marker', 'none -- applied'),
    ('R2', 'SIDE-trivium', 'Trivium/Bijection.lean :8 and :23', 'APPLIED at b684 (v0.1.2)', 'data/b684_cut.txt', 63, 'R2: :6-:10 and :23-:27', 'none -- applied'),
    ('R3a', 'SIDE-silence-principle', 'SIDESilencePrinciple/Basic.lean :412, Theorem 8.1`s title', 'APPLIED at b684 (v0.2.2)', 'data/b684_cut.txt', 68,
     'R3a: the title at :412', 'none -- applied'),
    ('R3b', 'SIDE-silence-principle', 'SIDESilencePrinciple/Basic.lean :7-:12, the introduction`s statement of the principle', 'CARRIED (its row`s reason '
     'does not reach it)', 'data/b686_cut.txt', 49, 'R3b  SIDESilencePrinciple/Basic.lean:1 (header) introduction :7-:12   CARRIED',
     'the next re-cut of SIDE-silence-principle, or a reading census that names an ACTION for it'),
    ('R4', 'SIDE-spinor', 'SIDESpinor/SpinorLeg.lean :21 "(salt-checked)"', 'APPLIED at b688 (v0.1.2)', 'data/b688_residue_actions.txt', 49,
     'R4 APPLIED, v0.1.2', 'none -- applied'),
    ('LM-i', 'SIDE-li-map', 'PrimeLedgerPositivity.lean :29-:31, the survey note`s quotation of a removed line of LiLinearMap.lean', 'CARRIED (the '
     'ACTIONs applied verbatim, not extended)', 'data/b688_cut.txt', 60, 'PrimeLedgerPositivity.lean :29-:31', 'the next re-cut of SIDE-li-map; from b691 '
     'data/b690_rules.txt row (2) would have found it at the cut'),
    ('LM-ii', 'SIDE-li-map', 'PrimeLedgerPositivity.lean :51-:54, NonnegStream`s docstring naming the real-valued Λ as an instance of an integer stream',
     'CARRIED (the ACTIONs applied verbatim, not extended)', 'data/b688_cut.txt', 64, 'PrimeLedgerPositivity.lean :51-:54', 'the next re-cut of SIDE-li-map'),
]


def residues(*a):
    rows = []
    for rid, k, what, state, bank, ln, nd, trig in RESIDUES:
        Lb = rdn(os.path.basename(bank)).split(NL)
        ok = nd in (Lb[ln - 1] if len(Lb) >= ln else '')
        rows.append(dict(id=rid, kernel=k, what=what, state=state, bank=bank, line=ln, read=ok, trigger=trig))
    b689 = 'b689 cut nothing: its Lean was a new file beside Wide`s (data/b689_landing.txt), no re-cut, so no residue' if os.path.exists(
        os.path.join(D, 'b689_landing.txt')) and not os.path.exists(os.path.join(D, 'b689_cut.txt')) else '### b689 CUT BANK PRESENT -- READ IT'
    car = [r for r in rows if r['state'].startswith('CARRIED')]
    L = ['b690 -- COMPONENT 2 (vii), (R300)(3): THE RESIDUES CENSUS, READING 3 (%s)' % utc(), '', HEAD,
         '### by hand: the residues the cut banks name, each with its state (APPLIED with its tag, or CARRIED with its reason) and its trigger; by',
         '### code: each row`s needle read on its bank line. b680`s census (data/b680_residues.txt, five sentences in three documents, all then',
         '### carried) is the row set R1-R3b; R4 entered at b686; LM-i and LM-ii at b688. Rows are residues:']
    L += ['  %-5s %-24s %s | %s :%d (needle %s) | %s | trigger: %s' % (r['id'], r['kernel'], r['state'], r['bank'], r['line'], r['read'], r['what'],
                                                                     r['trigger']) for r in rows]
    L += ['', '### any residue b689 left: %s' % b689,
          '', '### ### **RESIDUES %d ; APPLIED %d ; CARRIED %d (%s) ; EVERY NEEDLE READ %s ; b680: 5 SENTENCES CARRIED (data/b680_residues.txt).**' % (
              len(rows), len(rows) - len(car), len(car), ', '.join(r['id'] for r in car), all(r['read'] for r in rows))]
    put('b690_r3_residues', L, dict(at=utc(), rows=rows, carried=[r['id'] for r in car], b689=b689))
    print(L[-1])


# ================================================================================ (viii) THE RULES CENSUS, b674 THROUGH b690
RULE_ROW = re.compile(r'^  \((\d+)\) (.+?)\.(?: |$)')
# ### the arms the harness carries outside tools/rule_arms.py, each beside the rule its predicate reads -- the seat's map, by hand, each arm's
# ### own docstring or reads-line naming the rule's bank where one does
HAND_ARMS = {('b681', 1): ('G-ACTROOT-VERIFY', 'standing: the chain read through the corrigendum row'),
             ('b681', 2): ('G-ANSWERS-BANKED', 'standing: a call after the lock named on the face'),
             ('b681', 3): ('G-ROOT-BANKS-COMMITTED', 'standing from (R291)(4)'),
             ('b685', 2): ('G-EDIT-ROUTE', 'standing: sed in any form read beside edit_route.py`s arms (b687`s repair)'),
             ('b686', 1): ('G-SCORER-READS-BANKS, G-ENTRY-SCORES-EQUAL', 'act-local at every act since b686')}
HAND_SORT = {('b680', 1): ('TRACEABLE, LIVE', 'a binary bank beside its text hashes bank -- the root`s items show it at every act; no arm reads it'),
             ('b682', 1): ('PROSE', 'the author`s word ordering arms for the traceable rules; done by b683`s twenty arms'),
             ('b685', 1): ('TRACEABLE, LIVE', 'one call per suite part, each its own message -- the command capture shows it at every act; no arm reads it'),
             ('b687', 1): ('PROSE', 'the author`s amendment of a landing criterion; it orders a reading, not an act a bank shows'),
             ('b688', 1): ('TRACEABLE, VACUOUS', 'a band priced from b667`s run record before it runs -- a plan bank`s row would show it; no band counted '
                           'by the argument principle since b688, so an arm would read VACUOUS until one is')}
B690_RULES = (('b690', 1, 'AFTER THE SEAL, THE ENTRY, THE DRY ENTRY AND THE TRAIL READ THROUGH THE READ TOOL OR THE RECORD TOOL`S PRINT'),
              ('b690', 2, 'AT A RE-CUT, EACH LINE THE CUT REMOVES OR CHANGES SEARCHED ACROSS THE KERNEL`S SOURCE TREE'),
              ('b690', 3, 'THE NAVIGATOR`S: A FERRY ON LONG LINES, NO QUOTED LINE BROKEN BY A HARD WRAP'))


def rules(*a):
    import rule_arms as RA
    banks = sorted(f for f in os.listdir(D) if re.match(r'^b6(7[4-9]|8\d|90)_rules\.txt$', f))
    arm_of = {}
    for nm, reads, *_r in RA.ARMS:
        for m in re.finditer(r'\b(b6\d\d) row \(?(\d+)\)?', reads):
            arm_of.setdefault((m.group(1), int(m.group(2))), []).append(nm)
    rows = []
    for f in banks:
        act = f[:4]
        for i, l in enumerate(rdn(f).split(NL), 1):
            m = RULE_ROW.match(l)
            if m:
                k = (act, int(m.group(1)))
                if act == 'b690':
                    rows.append(dict(act=act, row=k[1], head=m.group(2)[:110], bank='data/%s :%d' % (f, i), arm='NONE',
                                     how=('by hand: the ruling (R300)(5) -- its arm sorted at b691 by data/b683_arms_sort.txt`s rule, not added this '
                                          'act' if k[1] in (1, 2) else 'by hand: the ruling (R300)(5) -- the navigator`s rule on the ferry, binding '
                                          'from b690; no sort ordered, no arm'),
                                     sort='NOT SORTED (b691)' if k[1] in (1, 2) else 'NOT SORTED (the ruling sorts (1) and (2) alone)'))
                    continue
                if k in arm_of:
                    arm, how, sort = ', '.join(arm_of[k]), 'by code (tools/rule_arms.py, the arm`s reads-line naming %s row %d)' % k, 'ARMED'
                elif k in HAND_ARMS:
                    arm, how, sort = HAND_ARMS[k][0], 'by hand: %s' % HAND_ARMS[k][1], 'ARMED'
                else:
                    arm, how, sort = 'NONE', 'by hand: %s' % HAND_SORT.get(k, ('UNSORTED', 'no sort recorded'))[1], HAND_SORT.get(k, ('UNSORTED',))[0]
                rows.append(dict(act=act, row=int(m.group(1)), head=m.group(2)[:110], bank='data/%s :%d' % (f, i), arm=arm, how=how, sort=sort))
    for act, n, h in (B690_RULES if not any(r['act'] == 'b690' for r in rows) else ()):
        rows.append(dict(act=act, row=n, head=h, bank='data/b690_rules.txt (to be banked at Component 3)', arm='NONE',
                         how=('by hand: the ruling (R300)(5) -- its arm sorted at b691 by data/b683_arms_sort.txt`s rule, not added this act' if n in (1, 2)
                              else 'by hand: the ruling (R300)(5) -- the navigator`s rule on the ferry, binding from b690; no sort ordered, no arm'),
                         sort='NOT SORTED (b691)' if n in (1, 2) else 'NOT SORTED (the ruling sorts (1) and (2) alone)'))
    c = collections.Counter(r['sort'] for r in rows)
    L = ['b690 -- COMPONENT 2 (viii), (R300)(3): THE RULES CENSUS OVER EVERY RULES BANK b674 THROUGH b690 (%s)' % utc(), '', HEAD,
         '### the banks: %s (no rules bank at b676, b679, b683 or b689); b690`s three rules from (R300)(5), banked at Component 3. Each rule`s arm' % ', '.join(banks),
         '### by code where tools/rule_arms.py names its bank row; by hand where a harness arm reads it (HAND_ARMS) or none does (HAND_SORT, the sort',
         '### of data/b683_arms_sort.txt :3-:8, its SORT TRACEABLE or PROSE and its STATE LIVE or DECLARATION-ONLY, an arm reading VACUOUS). The',
         '### ruling`s words, "each rule`s arm or its PROSE/VACUOUS sort": an unarmed rule is PROSE, or TRACEABLE and VACUOUS; a TRACEABLE rule',
         '### whose trace is LIVE and that has no arm fits neither word, and is named so below. Rows are rules:']
    L += ['  %s row (%d) %-110s | %s | %s | %s | %s' % (r['act'], r['row'], r['head'], r['bank'], r['sort'], r['arm'], r['how']) for r in rows]
    armed = [r for r in rows if r['sort'] == 'ARMED']
    live = [r for r in rows if r['sort'] == 'TRACEABLE, LIVE']
    L += ['', '### TRACEABLE, LIVE AND WITHOUT AN ARM -- neither PROSE nor VACUOUS in the ruling`s words: %s' % (
        ', '.join('%s row (%d)' % (r['act'], r['row']) for r in live) or 'NONE'),
          '', '### ### **RULES %d ; WITH AN ARM %d (BY CODE %d, BY HAND %d) ; PROSE %d ; TRACEABLE AND VACUOUS %d ; TRACEABLE, LIVE AND WITHOUT AN ARM %d ; '
          'NOT YET SORTED %d.**' % (
        len(rows), len(armed), sum(1 for r in armed if r['how'].startswith('by code')), sum(1 for r in armed if r['how'].startswith('by hand')),
        c['PROSE'], c['TRACEABLE, VACUOUS'], len(live), sum(v for k, v in c.items() if k.startswith('NOT SORTED')) + c['UNSORTED'])]
    put('b690_r3_rules', L, dict(at=utc(), rows=rows, counts=dict(c), armed=len(armed)))
    print(L[-1])


# ================================================================================ (ix) THE ARMS CENSUS, STANDING AND ACT-LOCAL BY ACT
def _g2(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def arms(*a):
    rows = []
    for n in range(674, 690):
        faces = sorted(glob.glob(os.path.join(D, 'b%d_registration_*.txt' % n)))
        try:
            W = importlib.import_module('b%d_worklist' % n)
            act_arms = list(getattr(W, 'ACT_ARMS', ()) or ())
        except Exception:
            act_arms = None
        if not faces:
            continue
        dec = _g2(faces[-1])
        aa = sorted(set(act_arms or []) & set(dec)) if act_arms is not None else None
        rows.append(dict(act='b%d' % n, face=os.path.basename(faces[-1]), declared=len(dec), act_local=len(aa) if aa is not None else None,
                         standing=(len(dec) - len(aa)) if aa is not None else None))
    parts = {}
    for p in ('standing-a', 'standing-c', 'standing-b', 'act'):
        m = re.search(r'### PART %s : ARMS (\d+) ; [^\n]*? (\d+) s' % p, rdn('b689_checks_postpush_%s.txt' % p))
        parts[p] = (int(m.group(1)), int(m.group(2))) if m else None
    L = ['b690 -- COMPONENT 2 (ix), (R300)(3): THE ARMS CENSUS, STANDING AND ACT-LOCAL BY ACT, AND THEIR RUNTIME BY PART (%s)' % utc(), '', HEAD,
         '### by code: each act`s sealed face`s (G2) block counted, its act-local arms its worklist`s ACT_ARMS present on the face, the standing the',
         '### rest. Rows are acts:']
    L += ['  %s  %-38s declared %3d ; act-local %s ; standing %s' % (r['act'], r['face'], r['declared'], r['act_local'] if r['act_local'] is not None else '-',
                                                                   r['standing'] if r['standing'] is not None else '-') for r in rows]
    L += ['', '### THE RUNTIME BY PART, AT HEAD AT b689`S POST-PUSH RUN (data/b689_checks_postpush_<part>.txt, each part`s own footer): %s' % (
        '; '.join('%s %s arms %s s' % (p, v[0], v[1]) if v else '%s ### UNREAD' % p for p, v in parts.items())),
          '### THE PER-ARM SECONDS OF THE STANDING ARMS AT HEAD: read by this act`s suite at its pre-run (Component 4, tools/b690_checks.py`s per-arm',
          '### clock, banked as data/b690_arm_seconds.json) and appended beneath this census then, the three slowest named. b689`s parts bank',
          '### their PHASES in seconds, not their arms: standing-b`s phase line (data/b689_checks_postpush_standing-b.txt :5), verbatim:',
          '    ' + (rdn('b689_checks_postpush_standing-b.txt').split(NL) + [''] * 5)[4].strip(),
          '', '### ### **ACTS READ %d ; STANDING AT b689 %s ; ACT-LOCAL AT b689 %s ; THE SLOWEST PART AT b689 %s.**' % (
              len(rows), rows[-1]['standing'] if rows else '-', rows[-1]['act_local'] if rows else '-',
              max(((v[1], p) for p, v in parts.items() if v), default=('-', '-'))[1])]
    put('b690_r3_arms', L, dict(at=utc(), rows=rows, parts=parts))
    print(L[-1])


# ================================================================================ (x) P3 ACROSS THE CORPUS
P3_PAT = r'T-COUNT|the local count assumed|stated, not proved'
P3_NEAR = re.compile(r'Q0|P3|T-COUNT|Epstein|Z_Q|Q0Count|x² \+ xy \+ 6y²')
KERNELS = ('SIDE-explicit-formula', 'SIDE-li-map', 'SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-global-section')
LEDGERS = ('FINDINGS.md', 'OPEN_TRAILS.md')


def _reading(text):
    t = text.lower()
    if re.search(r'assumed|stated, not proved|not proved|not derived', t):
        return 'STATED'
    if re.search(r'\bderive[sd]?\b|\bproved\b', t):
        return 'DERIVED'
    return 'NAMED'


TCOUNT = re.compile(r'(?<![A-Za-z])T-COUNT')
P3_WORD = re.compile(r'\bP3\b|\bHCount\b|\bQ0Count\b|the local count')
Q0_AT = re.compile(r'\bQ0|Epstein|Z_Q|D = [−-]23')


def p3(*a):
    hits = []
    ks = sorted(os.path.basename(p) for p in glob.glob('D:/SIDE-*') if os.path.isdir(os.path.join(p, '.git')))
    for repo, name, spec in ((PP, 'PLACE-papers', ['--', '*.md']),) + tuple(('D:/' + k, k, ['--', '*.lean']) for k in ks):
        if not os.path.isdir(repo):
            continue
        out = g(repo, 'grep', '-n', '-E', P3_PAT, 'HEAD', *spec)
        for l in out.split(NL):
            m = re.match(r'^HEAD:([^:]+):(\d+):(.*)$', l)
            if not m:
                continue
            f, ln, text = m.group(1), int(m.group(2)), m.group(3)
            q0 = bool(Q0_AT.search(text)) or 'EpsteinQ0' in f
            names = bool(TCOUNT.search(text) or P3_WORD.search(text))
            wrap = None
            if q0 and not names and ln > 1:
                prev = (g(repo, 'show', 'HEAD:' + f).replace(chr(13), '').split(NL) + [''] * ln)[ln - 2]
                if TCOUNT.search(prev) or P3_WORD.search(prev):
                    names, wrap = True, ':%d-:%d, the sentence wrapped from :%d (%s)' % (ln - 1, ln, ln - 1, ' '.join(prev.split())[:160])
                    text = prev + ' ' + text
            hits.append(dict(repo=name, file=f, line=ln, text=' '.join(text.split())[:420], at_q0=q0, p3=names, wrap=wrap,
                             reading=_reading(text) if names else 'NAMED', ledger=f in LEDGERS or f.startswith('archive/')))
    import b690_record as REC
    for h in hits:
        REC.read_p3_row(h)
    sub = [h for h in hits if h['at_q0'] and h['p3']]
    nl = [h for h in sub if not h['ledger']]
    c = collections.Counter(h['reading'] for h in nl)
    cl = collections.Counter(h['reading'] for h in sub if h['ledger'])
    st = rdn('b687_p3_status.txt').split(NL)
    L = ['b690 -- COMPONENT 2 (x), (R300)(3): P3`S STATUS ACROSS EVERY LINE IN THE CORPUS NAMING T-COUNT, "the local count assumed" OR "stated, not',
         'proved" AT Q0 (%s)' % utc(), '', HEAD,
         '### P3`s status, the bank of record: relay data/b687_p3_status.txt :35, verbatim: %s' % st[34].strip(),
         '### by code: git grep -n -E %r at HEAD over PLACE-papers` *.md (the papers, the faces page, the keystones, the two ledgers) and over the' % P3_PAT,
         '### kernels` *.lean (every D:/SIDE-* repository, %d: %s), bounded to each source tree. Every hit is listed; each is marked AT Q0 (the' % (
             len(ks), ', '.join(ks)),
         '### line names Q0, Epstein, Z_Q, Q0Count or D = −23, or the file is EpsteinQ0.lean) and P3 (the line names T-COUNT as a word -- POINT-COUNT',
         '### is not it -- or P3, HCount, Q0Count or the local count). A P3 line`s reading by its own words: STATED (assumed, stated, not proved, not',
         '### derived -- read first), DERIVED (derived, derives, proved), NAMED (neither); a line not naming P3 is read NAMED, its phrase another',
         '### premise`s -- unless the line before it, joined, names P3 (a sentence hard-wrapped through the grep`s line), then read as one sentence',
         '### and its row says so. The ledger lines (FINDINGS, OPEN_TRAILS and their archive/ copies) are records at their acts, appended and never',
         '### edited: listed and counted apart. Rows are hits: repository file :line [reading] AT-Q0 P3 wording.',
         '### THE WRAPPED READS: %s' % ('; '.join('%s %s %s' % (h['repo'], h['file'], h['wrap']) for h in hits if h['wrap']) or 'NONE')]
    for h in sorted(hits, key=lambda h: (h['ledger'], not (h['at_q0'] and h['p3']), h['repo'], h['file'], h['line'])):
        L.append('  %-22s %s :%d [%s] %s %s%s %s' % (h['repo'], h['file'], h['line'], h['reading'], 'Q0' if h['at_q0'] else '--', 'P3' if h['p3'] else '--',
                                                   ' (ledger)' if h['ledger'] else '', h['text']))
    L += ['', '### ### **GREP HITS %d ; AT Q0 NAMING P3 %d -- OUTSIDE THE LEDGERS %d (STILL READING STATED %d, DERIVED %d, NAMED %d), IN THE LEDGERS %d '
          '(STATED %d, DERIVED %d, NAMED %d).**' % (len(hits), len(sub), len(nl), c['STATED'], c['DERIVED'], c['NAMED'], len(sub) - len(nl), cl['STATED'],
                                                   cl['DERIVED'], cl['NAMED'])]
    put('b690_r3_p3', L, dict(at=utc(), pattern=P3_PAT, hits=hits, named=len(sub), outside=len(nl), stated=c['STATED'], derived=c['DERIVED'],
                              named_only=c['NAMED'], ledger=len(sub) - len(nl), status=st[34].strip()))
    print(L[-1])


# ================================================================================ (xi) W-ORD-ONE-COPY RE-READ, BY b686'S PARTNER ROUTE (its reading, not its write)
def onecopy(*a):
    import correspondence_gen as G
    t = [x for x in json.load(io.open(os.path.join(D, 'b672_roster_read.json'), encoding='utf-8'))['tables'] if x['doc'] == 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME'][0]
    A = rd(os.path.join(PP, t['path'])).split(NL)
    B = rd(os.path.join(PP, t['partner'])).split(NL)
    fa, fb = G.find_table(A, t), G.find_table(B, t)
    ta, tb = A[fa[0]:fa[1]], B[fb[0]:fb[1]]
    rows = []
    for i in range(max(len(ta), len(tb))):
        x = ta[i] if i < len(ta) else None
        y = tb[i] if i < len(tb) else None
        if x != y:
            rows.append((fa[0] + 1 + i if x is not None else None, fb[0] + 1 + i if y is not None else None))
    L = ['b690 -- COMPONENT 2 (xi), (R300)(3): W-ORD-ONE-COPY RE-READ, BY b686`S PARTNER ROUTE (%s)' % utc(), '', HEAD,
         '### the method: tools/b686_record.py `partner` (:725-:757), its reading carried here and its write not -- the roster`s FOUNDATIONS table',
         '### (%s) against its one-copy partner (%s), both found by correspondence_gen.find_table at PLACE-papers HEAD %s; rows are the table' % (
             t['path'], t['partner'], g(PP, 'rev-parse', '--short', 'HEAD').strip()),
         '### lines that differ, by line in each:'] + ['  ROSTER :%s | PARTNER :%s' % r for r in rows] + [
         '', '### ### **PARTNER TABLE LINES DIFFERING %d AGAINST b686`S 13 (data/b686_correspondence_diff.txt :151) ; THE COUNT %s.**' % (
             len(rows), 'UNCHANGED' if len(rows) == 13 else 'CHANGED')]
    put('b690_r3_onecopy', L, dict(at=utc(), differing=len(rows), b686=13, rows=rows))
    print(L[-1])


# ================================================================================ (xii) THE PAIR-RULE READINGS, IN b680'S FORM
def pair(*a):
    r1 = rdn('b670_rules.txt').split(NL)
    rule = ' '.join(' '.join(r1[4:7]).split())
    lic, cor, cei, ords = jn('b690_r3_licensed.json'), jn('b690_r3_corr.json'), jn('b690_r3_ceiling.json'), jn('b690_r3_orders.json')
    m80 = re.search(r'WITHOUT A TRIGGER MET OR A RE-DATING (\d+)', rdn('b680_orders.txt'))
    b80 = dict(licensed=jn('b680_licensed.json').get('total'), corr=jn('b680_correspondence.json').get('behind'),
               ceiling=jn('b680_ceiling.json').get('successor_equal'), orders=int(m80.group(1)) if m80 else None)
    now = dict(licensed=lic.get('total'), corr=cor.get('behind'), ceiling=cei.get('successor_equal'), orders=ords.get('unsteady'))
    COND = (('licensed', 'rows outside LICENSED or CITED across the agenda, the rule`s condition 0', lambda v: v == 0),
            ('corr', 'Correspondence rows behind their kernel`s current tag (b670`s method), the condition 0', lambda v: v == 0),
            ('ceiling', 'the ceiling sentence byte-identical at its placements, the condition True', lambda v: v is True),
            ('orders', 'open orders older than ten acts without a trigger met or re-dated, the condition 0', lambda v: v == 0))
    rows = [(k, w, b80[k], now[k], f(b80[k]), f(now[k])) for k, w, f in COND]
    L = ['b690 -- COMPONENT 2 (xii), (R300)(3): THE PAIR-RULE READINGS, IN b680`S FORM (%s)' % utc(), '', HEAD,
         '### the rule, verbatim from relay data/b670_rules.txt :5-:7: %s' % rule,
         '### b680`s form (FINDINGS :9080, data/b680_ceiling.txt :3): each reading by b670`s method, the prior act`s figure printed beside. Here',
         '### b680`s figure (reading 2) beside b690`s (reading 3), each from its route`s bank above, and the rule`s own condition read at each act;',
         '### rows are readings:']
    L += ['  %-9s %-104s b680 %-6s b690 %-6s ; met at b680 %-5s ; met at b690 %s' % (k, w, a_, b_, x, y) for k, w, a_, b_, x, y in rows]
    both = sum(1 for r in rows if r[4] and r[5])
    L += ['', '### ### **THE PAIR RULE`S FOUR CONDITIONS MET AT BOTH b680 AND b690 %d OF 4 (%s) -- THE CORPUS NOT YET READ CONSISTENT ENOUGH FOR '
          'EXTRACTION PASSES BY THE RULE.**' % (both, ', '.join('%s %s' % (k, 'MET' if x and y else 'NOT MET') for k, _w, _a, _b, x, y in rows))
          if both < 4 else '### ### **THE PAIR RULE`S FOUR CONDITIONS MET AT BOTH b680 AND b690.**']
    put('b690_r3_pair', L, dict(at=utc(), rule=rule, rows=[list(r[:1]) + list(r[2:]) for r in rows], both=both))
    print(L[-1])


ROUTES = {'licensed': licensed, 'corr': corr, 'ceiling': ceiling, 'orders': orders, 'methods': methods, 'lag': lag, 'residues': residues,
          'rules': rules, 'arms': arms, 'p3': p3, 'onecopy': onecopy, 'pair': pair}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b690_readings.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
