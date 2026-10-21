# -*- coding: utf-8 -*-
"""b700_readings.py -- COMPONENT 2, (R310)(3): READING 4, EACH READING BY CODE WHERE A TOOL READS IT AND BY HAND WHERE NONE DOES, b680'S
(READING 2) AND b690'S (READING 3) FIGURES PRINTED BESIDE WHERE THEY TOOK THE SAME READING; AND THE FIVE READINGS (R310)(3) ADDS.

### THE METHOD IS b670'S, b672'S, b680'S AND b690'S CODE, NOT A COPY: tools/b690_readings.py is IMPORTED and its routes run with their bank
### writer captured in memory (its own imports of b670_record, b672_record and b680_readings carried with it, their writers captured as b690
### captured them), so that nothing of b670's, b672's, b680's or b690's is written; the captured figures are re-banked here beside b680's
### (data/b680_<name>.json) and b690's (data/b690_r3_<name>.json). Where the method reads data that grew since b690 (the cut banks of b691,
### b693, b695, b697, b699; the age of an order counted from 700; the rules banks to b699; the faces to b699), the growth is declared beside
### the figure. The five added readings are this tool's own routes: defects (a), roster (b), tags and tagsread (c), circuit (d),
### regularity (e). Each route one foreground process under the 600 s limit; `tags <kernel>` reads ONE repository's tags by ONE ls-remote
### per call, the calls made in sequence, an empty read re-read alone (data/b674_rules.txt row (1)).
### Routes -> data/b700_r4_<name>.txt (.json): licensed | corr | ceiling | orders | methods | lag | residues | rules | arms | p3 | faces |
### onecopy | pair | defects | roster | tags <kernel> | tagsread | circuit | regularity. Written by the Write tool at b700; it writes only
### those banks. data/b700_reading4.txt, the readings gathered with their hand rows, is the seat's, by the Write tool, after every route's bank.
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
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b690_readings as R3    # noqa: E402  ### reading 3's routes, imported unedited; their writer captured per route
import b700_worklist as K     # noqa: E402

ACT = 700
utc, rd, rdn, jn, g, verdict = R3.utc, R3.rd, R3.rdn, R3.jn, R3.g, R3.verdict
HEAD = ('### READING 4 (b700, under (R310)(3)). b690 took reading 3 (tools/b690_readings.py, its banks data/b690_r3_<name>.txt), b680 reading 2 '
        '(data/b680_<name>.txt), b670 reading 1. Each figure below is the tool`s where a tool reads it, the seat`s hand where none does, and says which.')


def put(name, lines, obj):
    R3.put('b700_r4_' + name, lines, obj)


def run3(fn):
    """run one of b690's routes with its bank writer captured: returns {bank name: (lines, obj)}; nothing of b690's is written."""
    store = {}
    keep = R3.put
    R3.put = lambda name, lines, obj: store.__setitem__(name, (lines, obj))
    try:
        fn()
    finally:
        R3.put = keep
    return store


def b90(name):
    return jn('b690_r3_%s.json' % name)


# ================================================================================ (1) THE LICENSED TABLE, BY b670'S METHOD (b690's route)
# ### the kernels cut since b690, each by its cut bank's verdict line, added to b690's map; the needle checked on its line and the figure after
# ### parsed from it, as b690's route does
CUTS_SINCE_690 = {
    'SIDE-rcurve': ('data/b691_cut.txt', 33, 'SIDE-rcurve RE-CUT: THE DISTANCE BEFORE 2, AFTER 0', r'AFTER (\d+)'),
    'SIDE-archimedean': ('data/b693_cut.txt', 28, 'SIDE-archimedean RE-CUT: THE DISTANCE BEFORE 2, AFTER 0', r'AFTER (\d+)'),
    'SIDE-interfaces': ('data/b695_cut.txt', 24, 'SIDE-interfaces RE-CUT: THE DISTANCE BEFORE 1, AFTER 0', r'AFTER (\d+)'),
    'SIDE-simplicity': ('data/b697_cut.txt', 21, 'SIDE-simplicity RE-CUT: THE DISTANCE BEFORE 1, AFTER 0', r'AFTER (\d+)'),
    'SIDE-substrate-cluster': ('data/b699_cut.txt', 40, 'SIDE-substrate-cluster RE-CUT: THE DISTANCE BEFORE 1, AFTER 0', r'AFTER (\d+)'),
}


def licensed(*a):
    R3.CUTS.update(CUTS_SINCE_690)
    s = run3(R3.licensed)
    lines, obj = s['b690_r3_licensed']
    rows = obj['agenda']
    r90 = dict((r['doc'], r['now']) for r in b90('licensed').get('agenda', []))
    r80 = dict((r['doc'], r['now']) for r in jn('b680_licensed.json').get('agenda', []))
    roster = [l for l in lines if l.startswith('  ') and ' constellation ' in l]
    L = ['b700 -- COMPONENT 2 (1), (R310)(3): THE LICENSED TABLE OVER THE ROSTER AND THE AGENDA, READING 4, BY b670`S METHOD (%s)' % utc(), '', HEAD,
         '### the method: b690`s route `licensed` (tools/b690_readings.py :105-:145), itself b670`s `licensed` and `agenda` by import, run here by',
         '### import with its writer captured; b690`s map of the kernels cut since b670 extended by the five cut since b690 (THE GROWTH SINCE b690,',
         '### DECLARED), each read from its cut bank`s verdict line:'] + ['    %s : %s :%d "%s"' % (k, v[0], v[1], v[2]) for k, v in CUTS_SINCE_690.items()] + [
         '### the route`s own growth lines:'] + ['    ' + x for x in obj.get('growth', [])] + [
         '    the cuts named and not found on the agenda: %s' % (obj.get('unused') or 'NONE'), '',
         '### A. PER ROSTER TABLE (b670`s route`s own lines): constellation [actionable, provenance, external, historical] ; rowgen diff [checked,',
         '### present, STALE, unmapped]'] + roster + ['', obj.get('roster_verdict', ''), '',
         '### B. PER AGENDA DOCUMENT: b648 -> b680 -> b690 -> b700 (rows outside LICENSED or CITED), the bank that gives b700`s figure:']
    for r in rows:
        L.append('  %-62s %4d -> %4s -> %4s -> %4d   [%s]' % (r['doc'][:62], r['b648'], r80.get(r['doc'], '-'), r90.get(r['doc'], '-'), r['now'], r['by']))
    moved = [(r['doc'], r90.get(r['doc']), r['now']) for r in rows if r90.get(r['doc']) is not None and r90.get(r['doc']) != r['now']]
    L += ['', '### THE DOCUMENTS MOVED SINCE b690 (b690 -> b700): %s' % ('; '.join('%s %s -> %d' % m for m in moved) or 'NONE'),
          '', '### ### **AGENDA DOCUMENTS %d ; ROWS OUTSIDE LICENSED OR CITED %d (b690 %s, b680 %s) ; DOCUMENTS AT ZERO %d (b690 %s, b680 %s).**' % (
              len(rows), obj['total'], b90('licensed').get('total'), obj.get('b680'), obj['zero'], b90('licensed').get('zero'), obj.get('zero_b680'))]
    put('licensed', L, dict(at=utc(), total=obj['total'], zero=obj['zero'], b690=b90('licensed').get('total'), b680=obj.get('b680'),
                            zero_b690=b90('licensed').get('zero'), zero_b680=obj.get('zero_b680'), docs=len(rows), agenda=rows, moved=moved,
                            roster_verdict=obj.get('roster_verdict')))
    print(L[-1])


# ================================================================================ (2) THE CORRESPONDENCE: b670'S METHOD, THE GENERATOR'S COUNT, BY HAND
def corr(*a):
    """three readings: b670's method by b690's route (b672's anchored re-read and b670's heading reader, by import, writers captured); the
    generator's own count after b691's scope repair -- the repaired generator's dry over the roster at the pages as they stand (its kernel
    cells behind at the leading clause, local tags, nothing written); and by hand, the seat's sort of b670's BEHIND rows by b691's scope
    categories (data/b691_behind.txt :855-:860's cause), each row's category read by code from the anchored re-read and the fresh dry."""
    import correspondence_gen as CG
    import b672_record as B2
    s = run3(R3.corr)
    lines, obj = s['b690_r3_corr']
    st = R3.captured(B2)
    B2.after()
    af = st['b672_correspondence_after.json']
    ro = json.load(io.open(CG.ROSTER, encoding='utf-8'))
    tags, _tl = CG.read_tags(CG.kernels_of(ro), remote=False)
    banks, _bl = CG.read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=CG.read_grades(), present=CG.present)
    gen = {}
    for t in ro['tables']:
        _nb, res = CG.regen_bytes(open(os.path.join(PP, t['path']), 'rb').read(), t, ctx, t['doc'])
        gen[t['doc']] = dict(status=res.get('status'), span=res.get('span'), rows=set(r['line'] for r in res['rows']),
                             kernel=sorted(set(c['line'] for c in res['changes'] if c['column'] == 'kernel')),
                             changes=[(c['line'], c['column'], c['kernel']) for c in res['changes']],
                             held=set(h['line'] for h in res.get('carry_held', [])), withheld=bool(t.get('withheld')))
    claim = sum(len(v['kernel']) for v in gen.values())
    cells = sum(len(v['changes']) for v in gen.values())
    rows, cat = [], collections.Counter()
    for d in af['tables']:
        G = gen.get(d['doc']) or {}
        for r in d['rows']:
            if r['reading'] != 'BEHIND':
                continue
            ln = r['line']
            if G.get('withheld'):
                c = 'WITHHELD (the document withheld; its table not in the generator`s shape)'
            elif G.get('status') != 'SHAPED':
                c = 'NOT A GENERATOR ROW: THE TABLE %s' % G.get('status')
            elif ln not in G['rows']:
                c = 'NOT A GENERATOR ROW: PAST THE TABLE PROPER'
            elif ln in G['kernel']:
                c = 'THE GENERATOR`S CLAIM: THE LEADING CLAUSE BEHIND ITS TAG'
            elif ln in G['held']:
                c = 'A GENERATOR ROW HELD: CARRIED AT, VERSION DIFFERS'
            else:
                c = 'A GENERATOR ROW NOT CLAIMED: THE LEADING CLAUSE AT ITS TAG, A COMMIT BEHIND IN CARRIED PROSE'
            rows.append(dict(doc=d['doc'], line=ln, cause672=r.get('cause'), category=c))
            cat[c] += 1
    b80 = jn('b680_correspondence.json')
    L = ['b700 -- COMPONENT 2 (2), (R310)(3): THE CORRESPONDENCE ROWS BEHIND, READING 4 -- BY b670`S METHOD, BY THE GENERATOR`S COUNT AFTER b691`S '
         'SCOPE REPAIR, AND BY HAND (%s)' % utc(), '', HEAD,
         '### b670`S METHOD (b690`s route `corr`, :149-:178, by import, writers captured): every backticked commit in a row against its kernel`s',
         '### local tag, a row BEHIND if any one is (tools/b672_record.py :490-:557). Its lines re-banked:',
         '    ' + [l for l in lines if l.startswith('### BY b670`S HEADING-TEXT READER')][0],
         '    ' + [l for l in lines if l.startswith('### BY THE STABLE ANCHORS')][0],
         '### THE GENERATOR`S COUNT, AFTER b691`S SCOPE REPAIR (the cause b691 found, data/b691_behind.txt: b670`s method reads every commit in a row over',
         '### a wider span; the generator the leading clause of the kernel cell in the shaped table proper, against the clause`s own kernel`s highest',
         '### tag): the repaired generator`s dry (tools/correspondence_gen.py regen_bytes, local tags, nothing written) over the roster',
         '### data/b672_roster_read.json at the pages at PLACE-papers HEAD %s: KERNEL CELLS BEHIND AT THE LEADING CLAUSE %d ; CELLS IT WOULD CHANGE %d.' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), claim, cells),
         '### THE GENERATOR`S CELLS BY LINE: %s' % ('; '.join('%s :%d %s %s' % (doc, ln, col, k) for doc, v in gen.items() for ln, col, k in v['changes']) or 'NONE'),
         '', '### BY HAND (the seat`s sort, b691`s categories): each of b670`s BEHIND rows with its category, read by code from the anchored re-read',
         '### and the fresh dry. Rows are BEHIND rows: document :line | b672`s cause | the category:']
    L += ['  %-44s :%-5s | %-60s | %s' % (r['doc'][:44], r['line'], (r['cause672'] or '')[:60], r['category']) for r in rows]
    L += ['', '### THE CATEGORIES (the difference`s cause):'] + ['    %-100s %d' % kv for kv in sorted(cat.items())]
    L += ['', '### ### **BEHIND BY b670`S METHOD %s (b690 %s, b680 %s) ; BY THE GENERATOR`S COUNT %d (b690`s figure at the claim, read from the 2026-10-16 '
          'bank, %s) ; THE DIFFERENCE %s, ITS CAUSE SCOPE: %s.**' % (
              obj.get('behind'), b90('corr').get('behind'), b80.get('behind'), claim, b90('corr').get('claim'),
              (obj.get('behind') or 0) - claim, ', '.join('%s %d' % (k.split(' (')[0], v) for k, v in sorted(cat.items())))]
    put('corr', L, dict(at=utc(), behind=obj.get('behind'), heading_reader=obj.get('heading_reader'), generator=claim, generator_cells=cells,
                        b690=dict(behind=b90('corr').get('behind'), claim=b90('corr').get('claim')), b680=dict(behind=b80.get('behind')),
                        rows=rows, categories=dict(cat)))
    print(L[-1])


# ================================================================================ (3) THE CEILING, BY b680'S ROUTE (b690's)
def ceiling(*a):
    s = run3(R3.ceiling)
    lines, obj = s['b690_r3_ceiling']
    L = ['b700 -- COMPONENT 2 (3), (R310)(3): THE CEILING`S SITES AND THE SUCCESSOR`S, READING 4, BY b680`S ROUTE THROUGH b690`S (%s)' % utc(), '', HEAD] + \
        lines[3:-1] + ['', '### ### **THE SUCCESSOR EQUAL AT ITS SITES %s (b690 %s, b680 %s).**' % (
            obj.get('successor_equal'), b90('ceiling').get('successor_equal'), jn('b680_ceiling.json').get('successor_equal'))]
    put('ceiling', L, dict(at=utc(), ceiling=obj.get('ceiling'), successor_equal=obj.get('successor_equal'), b690=b90('ceiling').get('successor_equal')))
    print(L[-1])


# ================================================================================ (4) THE ORDERS, BY b670'S QUEUE READER (b690's predicate, age from 700)
def orders(*a):
    import b670_record as B
    store = R3.captured(B)
    Q = B.orders()
    if Q is None:
        Q = store['b670_work_orders.json']['orders']
    for o in Q:
        o['age'] = ACT - int(o['act'][1:]) if o['act'] else -1
    op = [o for o in Q if o['open']]
    ns = [o for o in Q if o['status'] == 'NOT STATED']
    span = [o for o in Q if o['act'] and 691 <= int(o['act'][1:]) <= 699]
    disc = [o for o in Q if re.search(r'DISCHARGED', o['status'] or '', re.I)]
    old = [o for o in op if o['age'] > 10 and not re.match(r'(?i)^(its )?trigger met$|^re-dated$', o['status'])]
    o90 = b90('orders')
    names90 = set(o90.get('unsteady_names') or [])
    retired = [o for o in Q if re.search(r'RETIRED|STRUCK|SUPERSEDED', o['status'] or '', re.I)]
    L = ['b700 -- COMPONENT 2 (4), (R310)(3): THE ORDERS AT OPEN_TRAILS, READING 4, BY b670`S QUEUE READER (%s)' % utc(), '', HEAD,
         '### the method: tools/b670_record.py `read_queue` and `orders` (:862-:964), run by import over OPEN_TRAILS at HEAD (b680`s and b690`s way); b690`s',
         '### counts and its steadiness predicate (b670`s :926) carried, the age counted from 700 (b690 from 690 -- declared). Rows are orders.', '',
         '  %-44s %-7s %-6s %-5s %-16s %s' % ('order', 'entry', 'act', 'age', 'status', 'at')]
    L += ['  %-44s :%-6d %-6s %-5d %-16s %s' % (o['name'], o['line'], o['act'] or '-', o['age'], o['status'],
                                              (':%d' % o['status_line']) if o['status_line'] else ':%d' % o['last_line']) for o in Q]
    L += ['', '### ENTERED THIS SPAN (b691 through b699, by the entry act): %s' % (', '.join('%s (%s)' % (o['name'], o['act']) for o in span) or 'NONE'),
          '### DISCHARGED (the status word naming it): %d -- %s' % (len(disc), ', '.join(o['name'] for o in disc) or 'NONE'),
          '### RETIRED, STRUCK OR SUPERSEDED (the status word naming it): %d -- %s' % (len(retired), ', '.join(o['name'] for o in retired) or 'NONE'),
          '### OPEN AND OLDER THAN TEN ACTS WITHOUT A TRIGGER MET OR A RE-DATING: %d ; newly so since b690: %s' % (
              len(old), ', '.join(o['name'] for o in old if o['name'] not in names90) or 'NONE'),
          '', '### ### **ORDERS %d (b690 %s, b680 %s) ; OPEN %d (b690 %s) ; DONE %d (b690 %s) ; NO STATUS %d (b690 %s) ; DISCHARGED %d (b690 %s) ; ENTERED '
              'b691-b699 %d ; RETIRED %d ; OPEN AND OLDER THAN TEN ACTS WITHOUT A TRIGGER MET OR A RE-DATING %d (b690 %s).**' % (
              len(Q), o90.get('total'), (o90.get('b680') or {}).get('total'), len(op), o90.get('open'), len(Q) - len(op) - len(ns), o90.get('done'),
              len(ns), o90.get('no_status'), len(disc), o90.get('discharged'), len(span), len(retired), len(old), o90.get('unsteady'))]
    put('orders', L, dict(at=utc(), total=len(Q), open=len(op), done=len(Q) - len(op) - len(ns), no_status=len(ns), discharged=len(disc),
                          discharged_names=[o['name'] for o in disc], retired=[o['name'] for o in retired], unsteady=len(old),
                          unsteady_names=[o['name'] for o in old], span=[o['name'] for o in span], b690=o90))
    print(L[-1])


# ================================================================================ (5) THE METHODS AND (6) THE KEYSTONE LAG, BY b680'S ROUTES (b690's)
def methods(*a):
    s = run3(R3.methods)
    lines, obj = s['b690_r3_methods']
    L = ['b700 -- COMPONENT 2 (5), (R310)(3): THE METHODS CENSUS, READING 4, BY b680`S ROUTE THROUGH b690`S (%s)' % utc(), '', HEAD] + \
        [l for l in lines[3:-1]] + ['', '### ### **BY b670`S CODE READY %s OF 12 ; WITH THE HAND-READ CELLS READY %s OF 12 -- b690 %s AND %s ; b680 %s AND %s.**' % (
            obj.get('ready_code'), obj.get('ready'), b90('methods').get('ready_code'), b90('methods').get('ready'),
            (obj.get('b680') or {}).get('ready_code'), (obj.get('b680') or {}).get('ready'))]
    put('methods', L, dict(at=utc(), ready_code=obj.get('ready_code'), ready=obj.get('ready'), b690=dict(ready_code=b90('methods').get('ready_code'),
                                                                                                     ready=b90('methods').get('ready'))))
    print(L[-1])


def lag(*a):
    s = run3(R3.lag)
    lines, obj = s['b690_r3_lag']
    r90 = dict((r.get('table') or r.get('doc') or r.get('keystone'), r.get('lag')) for r in b90('lag').get('rows', []))
    L = ['b700 -- COMPONENT 2 (6), (R310)(3): THE KEYSTONE LAG PER KEYSTONE, READING 4, BY b680`S ROUTE THROUGH b690`S (%s)' % utc(), '', HEAD,
         '### the method: tools/b680_readings.py `lag` (:327-:362) through b690`s route, by import, writers captured. Rows are keystones, b690`s lag beside:']
    for r in obj['rows']:
        k = r.get('table') or r.get('doc') or r.get('keystone')
        L.append('  %-48s lag %-5s (b690 %s) ; %s' % (str(k)[:48], r.get('lag'), r90.get(k, '-'), ' ; '.join('%s %s' % (x, r.get(x)) for x in r if x not in ('table', 'doc', 'keystone', 'lag'))[:200]))
    L += ['', '### ### **KEYSTONES %d ; LAGGING %s ; THE MEDIAN %s (b690 %s, b680 %s) ; THE MAXIMUM %s (b690 %s, b680 %s).**' % (
        len(obj['rows']), obj.get('lagging'), obj.get('median'), b90('lag').get('median'), (obj.get('b680') or {}).get('median'), obj.get('maximum'),
        b90('lag').get('maximum'), (obj.get('b680') or {}).get('maximum'))]
    put('lag', L, dict(at=utc(), rows=obj['rows'], median=obj.get('median'), maximum=obj.get('maximum'), lagging=obj.get('lagging'),
                       b690=dict(median=b90('lag').get('median'), maximum=b90('lag').get('maximum')), b680=obj.get('b680')))
    print(L[-1])


# ================================================================================ (7) THE RESIDUES CENSUS (by hand, each row's needle checked by code)
# ### b690's seven rows carried (R3.RESIDUES) and the residues the cut banks since b690 name, each by its bank line; (id, kernel, what, state,
# ### bank, line, needle, trigger). A row's state the latest bank's that names it.
RESIDUES_SINCE_690 = [
    ('b691 R-1', 'SIDE-rcurve', 'README.md :3', 'CARRIED (a README line outside the docstring rows the cut reaches)', 'data/b691_cut.txt', 15, 'R-1  README.md :3 | CARRIED',
     'the next re-cut of SIDE-rcurve or a README pass'),
    ('b691 R-2', 'SIDE-rcurve', 'README.md :9', 'CARRIED (as R-1)', 'data/b691_cut.txt', 16, 'R-2  README.md :9 | CARRIED', 'the next re-cut of SIDE-rcurve or a README pass'),
    ('b691 R-3', 'SIDE-rcurve', 'README.md :11', 'CARRIED (as R-1)', 'data/b691_cut.txt', 17, 'R-3  README.md :11 | CARRIED', 'the next re-cut of SIDE-rcurve or a README pass'),
    ('b691 R-4', 'SIDE-rcurve', 'README.md :19', 'CARRIED (as R-1)', 'data/b691_cut.txt', 18, 'R-4  README.md :19 | CARRIED', 'the next re-cut of SIDE-rcurve or a README pass'),
    ('b691 R-K1', 'SIDE-kernel', 'PATHS_TO_THE_CRITICAL_LINE_v0_7.md :301, v1.8 against the carry v1.3 = 0bc21c0', 'CARRIED (held as CARRIED AT: VERSION DIFFERS; '
     'read again at b693)', 'data/b693_cut.txt', 25, 'CARRIED, held by the generator as CARRIED AT: VERSION DIFFERS',
     'the next re-cut act after b691 or W-ORD-CORRESPONDENCE-BEHIND-SCOPE'),
    ('b693 R-1', 'SIDE-archimedean', 'README.md :15', 'CARRIED (a README line quoting the removed headline docstring)', 'data/b693_cut.txt', 17,
     'R-1  README.md :15 | CARRIED', 'the next re-cut of SIDE-archimedean or a README pass'),
    ('b693 R-2', 'SIDE-archimedean', 'README.md :19', 'CARRIED (a README line quoting the removed header)', 'data/b693_cut.txt', 18, 'R-2  README.md :19 | CARRIED',
     'the next re-cut of SIDE-archimedean or a README pass'),
    ('b693 R-3', 'SIDE-archimedean', 'SIDEArchimedean/Reflection.lean :39', 'CARRIED AS IT STANDS (the kept line, a MATCHES row, not a quote)', 'data/b693_cut.txt',
     19, 'R-3  SIDEArchimedean/Reflection.lean :39 | CARRIED AS IT STANDS', 'none named -- carried as it stands'),
    ('b695 R-1', 'SIDE-interfaces', 'Interfaces/ConnectionRequiresStructure.lean :9', 'CARRIED AS IT STANDS (the def`s own body)', 'data/b695_cut.txt', 17,
     'R-1  Interfaces/ConnectionRequiresStructure.lean :9 | CARRIED AS IT STANDS', 'none named -- carried as it stands'),
    ('b695 R-2', 'SIDE-interfaces', 'Interfaces/ConnectionRequiresStructure.lean :20', 'CARRIED AS IT STANDS (the theorem`s own hypothesis)', 'data/b695_cut.txt', 18,
     'R-2  Interfaces/ConnectionRequiresStructure.lean :20 | CARRIED AS IT STANDS', 'none named -- carried as it stands'),
    ('b695 R-3', 'SIDE-interfaces', 'Interfaces/InterfaceSplit.lean :13', 'CARRIED AS IT STANDS (a different claim, a MATCHES row)', 'data/b695_cut.txt', 19,
     'R-3  Interfaces/InterfaceSplit.lean :13 | CARRIED AS IT STANDS', 'none named -- carried as it stands'),
    ('b695 R-4', 'SIDE-interfaces', 'README.md :59', 'CARRIED AS IT STANDS (the theorem`s own reach; outside the docstring rows)', 'data/b695_cut.txt', 20,
     'R-4  README.md :59 | CARRIED AS IT STANDS', 'none named -- carried as it stands'),
    ('b697 R-1', 'SIDE-simplicity', 'README.md :9', 'APPLIED at b698 (v0.1.2)', 'data/b698_readme_cut.txt', 15,
     'SIDE-simplicity README :9 RE-CUT: THE ACTION APPLIED True', 'none -- applied'),
]


def residues(*a):
    rows = []
    for rid, k, what, state, bank, ln, nd, trig in list(R3.RESIDUES) + RESIDUES_SINCE_690:
        Lb = rdn(os.path.basename(bank)).split(NL)
        ok = nd in (Lb[ln - 1] if len(Lb) >= ln else '')
        rows.append(dict(id=rid, kernel=k, what=what, state=state, bank=bank, line=ln, read=ok, trigger=trig,
                         word='ACTION APPLIED' if state.startswith('APPLIED') else 'CARRIED'))
    b699 = 'b699`s cut: REMOVED OR CHANGED LINES 2 ; QUOTING LINES 0 (data/b699_cut.txt :17) -- no residue' if 'QUOTING LINES 0' in (
        rdn('b699_cut.txt').split(NL) + [''] * 17)[16] else '### b699`s CUT LINE NOT AS READ'
    car = [r for r in rows if r['word'] == 'CARRIED']
    L = ['b700 -- COMPONENT 2 (7), (R310)(3): THE RESIDUES CENSUS, READING 4 (%s)' % utc(), '', HEAD,
         '### by hand: every residue the cut banks name, b690`s seven (data/b690_r3_residues.txt) and those of the cuts since (b691, b693, b695, b697, b699),',
         '### each with ACTION APPLIED (its tag) or CARRIED (its reason) and its trigger; by code: each row`s needle read on its bank line. Rows are residues:']
    L += ['  %-10s %-24s %-15s %s | %s :%d (needle %s) | %s | trigger: %s' % (r['id'], r['kernel'], r['word'], r['state'], r['bank'], r['line'], r['read'],
                                                                           r['what'], r['trigger']) for r in rows]
    L += ['', '### %s' % b699,
          '', '### ### **RESIDUES %d (b690 7, b680 5) ; ACTION APPLIED %d ; CARRIED %d ; EVERY NEEDLE READ %s.**' % (
              len(rows), len(rows) - len(car), len(car), all(r['read'] for r in rows))]
    put('residues', L, dict(at=utc(), rows=rows, carried=[r['id'] for r in car], applied=[r['id'] for r in rows if r['word'] != 'CARRIED']))
    print(L[-1])


# ================================================================================ (8) THE RULES CENSUS, b674 THROUGH b699
# ### b690's map carried (R3.HAND_ARMS, R3.HAND_SORT) and extended to the rules banked since: each rule's arm by code where tools/rule_arms.py
# ### names its bank row; by hand where a suite arm reads it; else its sort in data/b683_arms_sort.txt's own words (:3-:9: SORT TRACEABLE or
# ### PROSE ; STATE LIVE, DECLARATION-ONLY or SUPERSEDED), an arm on a DECLARATION-ONLY trace reading VACUOUS.
HAND_ARMS_SINCE = {('b694', 1): ('G-DELETES-ONE-BRANCH', 'act-local at every act since b694 (tools/b699_checks.py :1244, its reads naming data/b694_rules.txt row (1))'),
                   ('b698', 2): ('G-READ-RULE', 'act-local at b698 and b699 (tools/b699_checks.py :1286, its reads naming data/b698_rules.txt row (2))')}
HAND_SORT_SINCE = {
    ('b690', 3): ('SORT TRACEABLE ; STATE LIVE', 'the ferry bank of each act (data/bNNN_ferry.txt) shows a quoted line broken by a hard wrap; no arm reads it -- '
                  'G-RULE-HEAD-LINE-QUOTED reads the head line alone'),
    ('b692', 1): ('SORT TRACEABLE ; STATE LIVE', 'an amended, rebased or rewritten commit after the seal shows in the remote against the capture; no arm reads it -- '
                  'the N5 scorer`s amend reading (b698_record._amended_after) reads it at each close, a score and not an arm'),
    ('b698', 1): ('SORT TRACEABLE ; STATE LIVE', 'a kernel tag move and the Correspondence cells naming the kernel at that act or the next show in the cut and '
                  'dry banks; no standing arm -- b699`s act arms G-TAG-CELLS-RAISED and G-ARCH-CELLS-REGENERATED read its one case'),
}


def rules(*a):
    import rule_arms as RA
    banks = sorted(f for f in os.listdir(D) if re.match(r'^b6(7[4-9]|8\d|9\d)_rules\.txt$', f))
    arm_of = {}
    for nm, reads, *_r in RA.ARMS:
        for m in re.finditer(r'\b(b6\d\d) row \(?(\d+)\)?', reads):
            arm_of.setdefault((m.group(1), int(m.group(2))), []).append(nm)
    # ### b690's sorts carried, each rewritten in data/b683_arms_sort.txt's own words (the ruling's order); its reason kept
    WORDS = {'TRACEABLE, LIVE': 'SORT TRACEABLE ; STATE LIVE', 'PROSE': 'SORT PROSE',
             'TRACEABLE, VACUOUS': 'SORT TRACEABLE ; STATE LIVE (its arm would read VACUOUS: no case since)'}
    HA, HS = dict(R3.HAND_ARMS), dict((k, (WORDS.get(v[0], v[0]), v[1])) for k, v in R3.HAND_SORT.items())
    HA.update(HAND_ARMS_SINCE)
    HS.update(HAND_SORT_SINCE)
    sort_words = rdn('b683_arms_sort.txt').split(NL)[2:9]
    s90 = dict(('%s row (%d)' % (r['act'], r['row']), r['sort']) for r in b90('rules').get('rows', []))
    rows = []
    yields = [0, 0]
    for f in banks:
        act = f[:4]
        BL = rdn(f).split(NL)
        for i, l in enumerate(BL, 1):
            yields[0] += 1 if R3.RULE_ROW.match(l) else 0
            # ### the second shape (b700): a row's number alone, its head joined across its continuation lines to the first full stop --
            # ### b690's pattern wants the stop on the row's first line and misses a wrapped head (b694 row (1), b698 row (1))
            m0 = re.match(r'^  \((\d+)\) (.*)$', l)
            if not m0:
                continue
            j = i
            while j < len(BL) and BL[j].startswith('      ') and not re.match(r'^  \(\d+\) ', BL[j]):
                j += 1
            joined = ' '.join(x.strip() for x in [m0.group(2)] + BL[i:j])
            m = re.match(r'^(\d+)\) (.+?)\.(?: |$)', '%s) %s' % (m0.group(1), joined))
            if not m:
                continue
            yields[1] += 1
            k = (act, int(m.group(1)))
            if k in arm_of:
                arm, how, sort = ', '.join(arm_of[k]), 'by code (tools/rule_arms.py, the arm`s reads-line naming %s row %d)' % k, 'ARMED'
            elif k in HA:
                arm, how, sort = HA[k][0], 'by hand: %s' % HA[k][1], 'ARMED'
            else:
                arm, how, sort = 'NONE', 'by hand: %s' % HS.get(k, ('UNSORTED', 'no sort recorded'))[1], HS.get(k, ('UNSORTED',))[0]
            rows.append(dict(act=act, row=k[1], head=m.group(2)[:110], bank='data/%s :%d' % (f, i), arm=arm, how=how, sort=sort,
                             b690=s90.get('%s row (%d)' % k, '-')))
    c = collections.Counter(r['sort'] for r in rows)
    armed = [r for r in rows if r['sort'] == 'ARMED']
    L = ['b700 -- COMPONENT 2 (8), (R310)(3): THE RULES CENSUS OVER EVERY RULES BANK b674 THROUGH b699 (%s)' % utc(), '', HEAD,
         '### the banks: %s (%d; no rules bank at the other ten acts). Each rule`s arm by code where tools/rule_arms.py names its bank row, by hand' % (
             ', '.join(banks), len(banks)),
         '### where a suite arm reads it, else its sort in the sort rule`s own words, data/b683_arms_sort.txt :3-:9, verbatim:'] + ['###   ' + x for x in sort_words] + [
         '### THE MATCHERS` YIELDS: b690`s RULE_ROW (the head`s stop on the row`s first line) %d ; the second shape (the head joined across its' % yields[0],
         '### continuation lines) %d -- the second shape`s rows are the census.' % yields[1],
         '### Rows are rules: act row | head | bank | sort | arm | how | b690`s sort:']
    L += ['  %s row (%d) %-110s | %s | %s | %s | %s | b690: %s' % (r['act'], r['row'], r['head'], r['bank'], r['sort'], r['arm'], r['how'], r['b690'])
          for r in rows]
    L += ['', '### ### **RULES %d (b690 21 over b674-b690) ; WITH AN ARM %d (BY CODE %d, BY HAND %d) ; WITHOUT AN ARM %d: %s ; ARMS NAMED %d.**' % (
        len(rows), len(armed), sum(1 for r in armed if r['how'].startswith('by code')), sum(1 for r in armed if r['how'].startswith('by hand')),
        len(rows) - len(armed), ', '.join('%s %d' % kv for kv in sorted(c.items()) if kv[0] != 'ARMED'),
        len(set(x.strip() for r in armed for x in r['arm'].split(','))))]
    put('rules', L, dict(at=utc(), rows=rows, counts=dict(c), armed=len(armed), arms=sorted(set(x.strip() for r in armed for x in r['arm'].split(',')))))
    print(L[-1])


# ================================================================================ (9) THE ARMS CENSUS, STANDING AND ACT-LOCAL BY ACT; SECONDS BY PART
def arms(*a):
    rows = []
    for n in range(674, 700):
        faces = sorted(glob.glob(os.path.join(D, 'b%d_registration_*.txt' % n)))
        try:
            W = importlib.import_module('b%d_worklist' % n)
            act_arms = list(getattr(W, 'ACT_ARMS', ()) or ())
        except Exception:
            act_arms = None
        if not faces:
            continue
        dec = R3._g2(faces[-1])
        aa = sorted(set(act_arms or []) & set(dec)) if act_arms is not None else None
        rows.append(dict(act='b%d' % n, face=os.path.basename(faces[-1]), declared=len(dec), act_local=len(aa) if aa is not None else None,
                         standing=(len(dec) - len(aa)) if aa is not None else None))
    j = jn('b699_arm_seconds.json')
    runs = j.get('run_secs') or {}
    ph = j.get('phases') or {}
    chain = [(p, h, v) for p, d in ph.items() for h, v in d.items() if h == 'the act-root chain`s half']
    halves = dict(zip(('b624-b658', 'b659-b699'), [(p, v) for p, h, v in chain if v]))
    slow = j.get('rows') or []
    r90 = dict((r['act'], r) for r in b90('arms').get('rows', []))
    L = ['b700 -- COMPONENT 2 (9), (R310)(3): THE ARMS CENSUS, STANDING AND ACT-LOCAL BY ACT, THE STANDING ARMS` SECONDS BY PART, THE CHAIN HALVES (%s)' % utc(),
         '', HEAD, '### by code: each act`s sealed face`s (G2) block counted (b690`s _g2), its act-local arms its worklist`s ACT_ARMS present on the face,',
         '### the standing the rest. Rows are acts:']
    L += ['  %s  %-38s declared %3d ; act-local %s ; standing %s' % (r['act'], r['face'], r['declared'], r['act_local'] if r['act_local'] is not None else '-',
                                                                   r['standing'] if r['standing'] is not None else '-') for r in rows]
    L += ['', '### THE STANDING ARMS` SECONDS BY PART AT b699`S PRE-RUN, THE LATEST CLOCKED (relay data/b699_arm_seconds.json, written by tools/b699_checks.py):',
          '    ' + ' | '.join('%s %s s' % kv for kv in runs.items()),
          '### THE THREE SLOWEST STANDING ARMS: %s' % ', '.join('%s (%s, %.3f s)' % (r['arm'], r['part'], r['secs']) for r in slow[:3]),
          '### THE CHAIN HALVES` SECONDS (the phase "the act-root chain`s half" of the part that carries it): %s' % (
              '; '.join('%s in %s %s s' % (k, p, v) for k, (p, v) in halves.items()) or 'UNREAD'),
          '', '### ### **ACTS READ %d ; AT b699 DECLARED %s, STANDING %s, ACT-LOCAL %s (b690 at b689: standing %s, act-local %s) ; THE SLOWEST PART %s ; THE '
              'THREE SLOWEST STANDING ARMS %s ; THE CHAIN HALVES %s.**' % (
              len(rows), rows[-1]['declared'] if rows else '-', rows[-1]['standing'] if rows else '-', rows[-1]['act_local'] if rows else '-',
              (r90.get('b689') or {}).get('standing'), (r90.get('b689') or {}).get('act_local'),
              max(((v, p) for p, v in runs.items()), default=('-', '-'))[1] + ' %s s' % max(runs.values(), default='-'),
              ', '.join(r['arm'] for r in slow[:3]), ', '.join('%s %s s' % (k, v) for k, (p, v) in halves.items()))]
    put('arms', L, dict(at=utc(), rows=rows, run_secs=runs, slowest=slow[:3], halves=halves))
    print(L[-1])


# ================================================================================ (10) P3 ACROSS THE CORPUS (b690's route) AND (11) THE FACES PAGE'S HEADER TAG
def p3(*a):
    s = run3(R3.p3)
    lines, obj = s['b690_r3_p3']
    L = ['b700 -- COMPONENT 2 (10), (R310)(3): P3`S STATUS ACROSS EVERY LINE IN THE CORPUS NAMING T-COUNT, "the local count assumed" OR "stated, not',
         'proved" AT Q0, READING 4, BY b690`S ROUTE (%s)' % utc(), '', HEAD] + lines[4:-1] + [
         '', '### ### **GREP HITS %d (b690 %s) ; AT Q0 NAMING P3 %d (b690 %s) -- OUTSIDE THE LEDGERS %d (STILL READING STATED %d, DERIVED %d, NAMED %d ; '
             'b690 %s, STATED %s) ; IN THE LEDGERS %d.**' % (
             len(obj['hits']), len(b90('p3').get('hits') or []), obj['named'], b90('p3').get('named'), obj['outside'], obj['stated'], obj['derived'],
             obj['named_only'], b90('p3').get('outside'), b90('p3').get('stated'), obj['ledger'])]
    put('p3', L, dict(obj, at=utc(), b690=dict(named=b90('p3').get('named'), outside=b90('p3').get('outside'), stated=b90('p3').get('stated'))))
    print(L[-1])


def faces(*a):
    page = os.path.join(PP, K.FACES_PAGE)
    l3 = (rd(page).split(NL) + [''] * 3)[2]
    m = re.search(r'SIDE-explicit-formula (v[\d.]+) = `([0-9a-f]{7})`', l3)
    tags = jn('b700_r4_tags.json').get('kernels') or {}
    ef = tags.get('SIDE-explicit-formula') or {}
    L = ['b700 -- COMPONENT 2 (11), (R310)(3): THE FACES PAGE`S HEADER TAG AGAINST THE KERNEL`S TAG, READING 4 (%s)' % utc(), '', HEAD,
         '### the page: PLACE-papers %s :3, verbatim: %s' % (K.FACES_PAGE, l3.strip()),
         '### the kernel`s highest tag: read from ls-remote by this tool`s `tags` route (data/b700_r4_tags.json): %s = %s' % (ef.get('highest'), (ef.get('commit') or '')[:7]),
         '### b690`s reading (data/b690_reading3.txt row (20)): the page names v0.26 = 82550e4 as its generation tag, the kernel at v0.34; the',
         '### generator`s source for it the node list`s "# pin: v0.26" line; carried to a regeneration with a fresh probe (a lean run, not on this host).',
         '', '### ### **THE PAGE`S HEADER TAG %s = %s ; THE KERNEL`S %s = %s ; CARRIED (THE SAME) %s.**' % (
             m.group(1) if m else '### UNREAD', m.group(2) if m else '-', ef.get('highest'), (ef.get('commit') or '')[:7],
             bool(m) and m.group(1) == ef.get('highest'))]
    put('faces', L, dict(at=utc(), page_tag=m.group(1) if m else None, page_commit=m.group(2) if m else None, kernel_tag=ef.get('highest'),
                         kernel_commit=ef.get('commit'), carried=bool(m) and m.group(1) == ef.get('highest')))
    print(L[-1])


# ================================================================================ (12) W-ORD-ONE-COPY BY LINE, EVERY PARTNER PAIR, EACH LINE`S CAUSE
CAUSE_WORDS = (('a regenerated cell', re.compile(r'(?i)generator|correspondence_gen|regenerat|cells? (written|refreshed)')),
               ('a re-cut', re.compile(r'(?i)re-?cut')),
               ('an archive-split artefact', re.compile(r'(?i)archive|split|ledger-split|move[sd]? .* to archive')))


def _blame(path, lines):
    """the last commit touching each line of a file at PLACE-papers HEAD: {line: (sha7, subject)}; one git blame per file."""
    out = {}
    if not lines:
        return out
    args = ['blame', '--porcelain'] + sum((['-L', '%d,%d' % (n, n)] for n in sorted(lines)), []) + ['HEAD', '--', path]
    cur, subj = None, {}
    for l in g(PP, *args).split(NL):
        m = re.match(r'^([0-9a-f]{40}) \d+ (\d+)', l)
        if m:
            cur = (m.group(1), int(m.group(2)))
            out[cur[1]] = cur[0]
        elif l.startswith('summary ') and cur:
            subj[cur[0]] = l[8:]
    return dict((n, (h[:7], subj.get(h) or g(PP, 'log', '-1', '--format=%s', h).strip())) for n, h in out.items())


def _cause(sa, sb, x, y):
    """the cause from the two sides' commits' subjects; a line on one side alone read the same way, its one-sidedness said beside (b700: a
    one-sided line is not an archive-split artefact unless a commit says so -- the first run's label, corrected on the hand's reading)."""
    side = ' (the line on one side alone)' if x is None or y is None else ''
    # ### each subject's head alone (its first 100 characters, where a commit names its own operation): b588's subject names "the archived
    # ### landing" deep in its body and read as an archive split on the whole subject (the second run, corrected on the hand's reading)
    # ### the generator's own pattern on the whole subject (its five commits hand-read: every one a generator write, b686's and b699's naming
    # ### the generator past their first 100 characters); the re-cut and archive patterns on the head alone
    for word, pat in CAUSE_WORDS:
        n = None if word == 'a regenerated cell' else 100
        if pat.search(sa[1][:n]) or pat.search(sb[1][:n]):
            return word + side
    return 'a hand edit' + side


def onecopy(*a):
    import correspondence_gen as CG
    ro = json.load(io.open(os.path.join(D, 'b672_roster_read.json'), encoding='utf-8'))
    pairs = [t for t in ro['tables'] if t.get('partner')]
    out, total, causes = [], 0, collections.Counter()
    for t in pairs:
        A = rd(os.path.join(PP, t['path'])).split(NL)
        B = rd(os.path.join(PP, t['partner'])).split(NL)
        fa, fb = CG.find_table(A, t), CG.find_table(B, t)
        if isinstance(fa, str) or isinstance(fb, str):
            out.append(dict(doc=t['doc'], path=t['path'], partner=t['partner'], status='TABLE NOT FOUND: %s / %s' % (fa if isinstance(fa, str) else 'found',
                                                                                                               fb if isinstance(fb, str) else 'found'), rows=[]))
            continue
        ta, tb = A[fa[0]:fa[1]], B[fb[0]:fb[1]]
        rows = []
        for i in range(max(len(ta), len(tb))):
            x = ta[i] if i < len(ta) else None
            y = tb[i] if i < len(tb) else None
            if x != y:
                rows.append((fa[0] + 1 + i if x is not None else None, fb[0] + 1 + i if y is not None else None, x, y))
        ba = _blame(t['path'], [r[0] for r in rows if r[0]])
        bb = _blame(t['partner'], [r[1] for r in rows if r[1]])
        rr = []
        for la, lb, x, y in rows:
            sa, sb = ba.get(la, ('-', '')), bb.get(lb, ('-', ''))
            c = _cause(sa, sb, x, y)
            causes[c.split(' (')[0]] += 1
            rr.append(dict(roster=la, partner=lb, cause=c, roster_commit=sa[0], roster_subject=sa[1][:120], partner_commit=sb[0], partner_subject=sb[1][:120]))
        total += len(rr)
        out.append(dict(doc=t['doc'], path=t['path'], partner=t['partner'], status='READ', stored=t.get('partner_lines_differing'), rows=rr))
    L = ['b700 -- COMPONENT 2 (12), (R310)(3): W-ORD-ONE-COPY READ BY LINE, EVERY PARTNER PAIR b672`S ROSTER NAMES, EACH LINE`S CAUSE (%s)' % utc(), '', HEAD,
         '### by code: each pair`s two tables found by correspondence_gen.find_table at PLACE-papers HEAD %s and compared line by line (b690`s and'
         % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
         '### b699`s reading); each differing line`s last commit on each side by git blame; the cause read from the two commits` subjects -- A REGENERATED',
         '### CELL (a generator run), A RE-CUT, AN ARCHIVE-SPLIT ARTEFACT (an archive or split commit, or the line on one side alone), else A HAND EDIT --',
         '### the reading printed with both commits so the hand checks it. Rows are differing lines: roster :line | partner :line | cause | the',
         '### roster side`s commit and subject | the partner side`s.']
    for p in out:
        L += ['', '=== %s : %s against %s -- %s ; the roster`s stored field %s ; DIFFERING %d' % (p['doc'], p['path'], p['partner'], p['status'],
                                                                                              p.get('stored'), len(p['rows']))]
        L += ['  :%-5s | :%-5s | %-62s | %s %s | %s %s' % (r['roster'], r['partner'], r['cause'], r['roster_commit'], r['roster_subject'], r['partner_commit'],
                                                         r['partner_subject']) for r in p['rows']]
    bycommit = collections.Counter()
    for p in out:
        for r in p['rows']:
            bycommit[(r['cause'].split(' (')[0], r['roster_commit'], r['roster_subject'][:110])] += 1
    L += ['', '### THE ROSTER SIDE`S COMMITS BY CAUSE, EACH WITH ITS LINES (for the hand`s reading of the sort -- every commit printed):']
    L += ['  %-28s %s %-112s %d' % (c, h, s_, n) for (c, h, s_), n in sorted(bycommit.items(), key=lambda kv: (kv[0][0], -kv[1]))]
    L += ['', '### THE CAUSE COUNTS: ' + ' ; '.join('%s %d' % kv for kv in sorted(causes.items())),
          '', '### ### **PARTNER PAIRS %d ; DIFFERING LINES %d (%s) ; BY CAUSE: %s.**' % (
              len(out), total, ', '.join('%s %d' % (p['doc'], len(p['rows'])) for p in out), ', '.join('%s %d' % kv for kv in sorted(causes.items())))]
    put('onecopy', L, dict(at=utc(), pairs=out, total=total, causes=dict(causes)))
    print(L[-1])


# ================================================================================ (13) THE PAIR-RULE READINGS, IN b680'S FORM (b690's)
def pair(*a):
    r1 = rdn('b670_rules.txt').split(NL)
    rule = ' '.join(' '.join(r1[4:7]).split())
    lic, cor, cei, ords = jn('b700_r4_licensed.json'), jn('b700_r4_corr.json'), jn('b700_r4_ceiling.json'), jn('b700_r4_orders.json')
    p90 = b90('pair')
    b90v = dict(licensed=b90('licensed').get('total'), corr=b90('corr').get('behind'), ceiling=b90('ceiling').get('successor_equal'),
                orders=b90('orders').get('unsteady'))
    now = dict(licensed=lic.get('total'), corr=cor.get('behind'), ceiling=cei.get('successor_equal'), orders=ords.get('unsteady'))
    COND = (('licensed', 'rows outside LICENSED or CITED across the agenda, the condition 0', lambda v: v == 0),
            ('corr', 'Correspondence rows behind (b670`s method), the condition 0', lambda v: v == 0),
            ('ceiling', 'the ceiling sentence byte-identical at its placements, the condition True', lambda v: v is True),
            ('orders', 'open orders older than ten acts without a trigger met or re-dated, the condition 0', lambda v: v == 0))
    rows = [(k, w, b90v[k], now[k], f(b90v[k]), f(now[k])) for k, w, f in COND]
    both = sum(1 for r in rows if r[4] and r[5])
    L = ['b700 -- COMPONENT 2 (13), (R310)(3): THE PAIR-RULE READINGS, IN b680`S FORM (%s)' % utc(), '', HEAD,
         '### the rule, verbatim from relay data/b670_rules.txt :5-:7: %s' % rule,
         '### b690`s figure (reading 3) beside b700`s (reading 4), each from its route`s bank, the rule`s own condition read at each; rows are readings:']
    L += ['  %-9s %-92s b690 %-6s b700 %-6s ; met at b690 %-5s ; met at b700 %s' % (k, w, a_, b_, x, y) for k, w, a_, b_, x, y in rows]
    L += ['', '### ### **THE PAIR RULE`S FOUR CONDITIONS MET AT BOTH b690 AND b700 %d OF 4 (%s) (b690: %s OF 4 AT b680 AND b690).**' % (
        both, ', '.join('%s %s' % (k, 'MET' if x and y else 'NOT MET') for k, _w, _a, _b, x, y in rows), p90.get('both'))]
    put('pair', L, dict(at=utc(), rule=rule, rows=[list(r[:1]) + list(r[2:]) for r in rows], both=both, b690=p90.get('both')))
    print(L[-1])


# ================================================================================ (a) THE DEFECTS BANKS b673 THROUGH b699, BY CLASS AND ACT
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")
# ### the seat's hand sort, written after the rows were printed (`defects list`, 185 rows): class -> its defects, every defect under one class
_SORT = {
    'A READ OUTSIDE THE READ TOOL (a shell filter, a pipe, a grep, an interpreter`s print, a whole read, a drive walk)':
        'b675 k ; b690 a ; b691 a ; b692 a ; b692 l ; b693 d ; b693 e ; b694 a ; b697 b ; b698 b ; b699 a ; b699 b',
    'sed IN ANY FORM': 'b682 e ; b684 a ; b684 e ; b686 b ; b687 a ; b689 e',
    'A REDIRECT OF A STREAM': 'b676 f ; b689 a ; b691 b ; b693 c',
    'A DELETE OUT OF THE HOUSE FORM (several in one message, in parallel, a glob, a chained half)': 'b674 h ; b677 i ; b678 a ; b682 a ; b693 f ; b699 c',
    'A GIT WRITE OUT OF THE HOUSE FORM (two in one call or message, a piped push, a push outside the tool, a capture misnamed)':
        'b673 k ; b674 l ; b678 b ; b688 a ; b691 c ; b691 d ; b692 i ; b694 l',
    'A FILE WRITTEN OUTSIDE THE EDIT AND WRITE TOOLS (cp, an interpreter`s write, git`s own option)': 'b679 d ; b680 f ; b692 e',
    'A FOREGROUND RUN PASSED TO THE BACKGROUND OR RUN WITHOUT ITS GUARD': 'b680 b ; b682 b ; b682 d ; b684 d ; b687 g ; b688 e',
    'A FIGURE, LINE OR CITE NOT READ FROM ITS BANK (memory, a draft, a remembered shape, no recount)':
        'b674 i ; b674 k ; b675 i ; b676 a ; b676 i ; b686 a ; b687 h ; b688 b ; b688 d ; b688 f ; b689 b ; b698 a',
    'A TOOL`S OR ROUTE`S FIRST FORM WRONG, CAUGHT BY ITS OWN RUN BEFORE THE SEAL':
        'b673 a ; b673 f ; b673 j ; b673 l ; b673 m ; b673 p ; b674 e ; b674 f ; b674 j ; b675 h ; b675 l ; b676 g ; b676 h ; b677 e ; b677 f ; '
        'b677 g ; b677 h ; b683 a ; b684 c ; b685 f ; b688 c ; b690 b ; b690 c ; b690 d ; b690 g ; b691 e ; b691 f ; b691 g ; b691 i ; b691 j ; '
        'b691 k ; b692 b ; b692 c ; b692 d ; b692 f ; b692 g ; b692 h ; b693 g ; b694 b ; b694 i ; b695 b ; b695 d ; b696 d ; b697 a',
    'A STEP OUT OF ITS ORDER OR NOT TAKEN (a closing, a suite, a check, a standing rule, the pace)': 'b674 m ; b680 c ; b680 g ; b681 a ; b685 d ; b695 a ; b697 c',
    'THE ROOT`S BANKS AND ORDER': 'b680 d ; b680 h ; b698 d',
    'A MID-ACT CHECK READING SEVERAL ANSWERS OR THE WRONG SCOPE': 'b674 g ; b675 j ; b676 b ; b691 h',
    'A SEALED TOOL`S DEFECT FOUND AFTER THE SEAL, LEFT AS IT STANDS': 'b689 d ; b692 m ; b693 h ; b694 k ; b699 d',
    'A FACE OR GATE DECLARATION WRONG (arms failing undeclared, a count read as a prediction, multi-arm words, hashes in words)':
        'b673 n ; b673 o ; b675 m ; b698 c',
    'A NAMESAKE FOLLOWED (a local binder read as a kernel declaration)': 'b673 i ; b679 e',
    'A STATE FOUND CHANGED AT STEP ZERO': 'b693 a',
    'THE NAVIGATOR`S: A CITE, PATH, NAME OR COUNT THE BANKS DO NOT CARRY':
        'b673 b ; b673 e ; b674 b ; b674 e\' ; b675 d ; b675 e ; b675 f ; b675 g ; b677 c ; b677 d ; b679 b ; b680 a ; b682 c ; b685 a ; '
        'b685 b ; b685 c ; b687 b ; b687 c ; b687 d ; b693 b ; b694 c ; b694 e ; b696 a ; b696 b',
    'THE NAVIGATOR`S: A PLAN, ORDER OR WORDING THAT CANNOT MEET ITS OWN TEST':
        'b673 c ; b673 d ; b673 g ; b673 h ; b674 a ; b674 c ; b674 d ; b675 a ; b675 b ; b675 c ; b676 c ; b676 d ; b676 e ; b677 a ; b677 b ; '
        'b679 a ; b679 c ; b680 e ; b684 b ; b685 e ; b687 e ; b687 f ; b689 c ; b690 e ; b690 f ; b692 j ; b692 k ; b694 d ; b694 f ; b694 g ; '
        'b694 h ; b694 j ; b695 c ; b696 c',
}
CLASS_OF = dict(((x.split()[0], x.split()[1]), c) for c, s in _SORT.items() for x in s.split(' ; '))
# ### class -> (the rule or tool that answered it, the act it answered from); "recurred after" read against that act
CLASS_ANSWER = {
    'A READ OUTSIDE THE READ TOOL (a shell filter, a pipe, a grep, an interpreter`s print, a whole read, a drive walk)':
        ('data/b690_rules.txt row (1) with G-RULE-POSTSEAL-READ, then data/b698_rules.txt row (2) with G-READ-RULE', 690),
    'sed IN ANY FORM': ('data/b685_rules.txt row (2) with G-EDIT-ROUTE`s sed reading (b687`s repair)', 685),
    'A REDIRECT OF A STREAM': ('data/b690_rules.txt row (1) ("with no redirect") and the command bank`s redirect readings', 690),
    'A DELETE OUT OF THE HOUSE FORM (several in one message, in parallel, a glob, a chained half)': ('data/b694_rules.txt row (1) with G-DELETES-ONE-BRANCH', 694),
    'A GIT WRITE OUT OF THE HOUSE FORM (two in one call or message, a piped push, a push outside the tool, a capture misnamed)':
        ('data/b673_rules.txt row (3) with G-RULE-ONE-GIT-WRITE', 673),
    'A FILE WRITTEN OUTSIDE THE EDIT AND WRITE TOOLS (cp, an interpreter`s write, git`s own option)': ('(R265)(4), standing from b655, with G-EDIT-ROUTE', 655),
    'A FOREGROUND RUN PASSED TO THE BACKGROUND OR RUN WITHOUT ITS GUARD': ('data/b685_rules.txt row (1) with G-RULE-SUITE-PART-CALLS and the command bank`s '
                                                                       'detached-run reading', 685),
    'A FIGURE, LINE OR CITE NOT READ FROM ITS BANK (memory, a draft, a remembered shape, no recount)': ('data/b686_rules.txt row (1) (a scorer reads banks) '
                                                                                                    'with G-SCORER-READS-BANKS', 686),
    'A TOOL`S OR ROUTE`S FIRST FORM WRONG, CAUGHT BY ITS OWN RUN BEFORE THE SEAL': ('data/b675_rules.txt row (1) with G-RULE-CLOSING-DRY and data/b672_rules.txt '
                                                                                 'row (3) with G-RULE-SCORES-BEFORE-SEAL', 675),
    'A STEP OUT OF ITS ORDER OR NOT TAKEN (a closing, a suite, a check, a standing rule, the pace)': ('data/b675_rules.txt row (1) with G-RULE-CLOSING-DRY', 675),
    'THE ROOT`S BANKS AND ORDER': ('G-ROOT-BANKS-COMMITTED, standing from (R291)(4)', 681),
    'A MID-ACT CHECK READING SEVERAL ANSWERS OR THE WRONG SCOPE': ('tools/b682_citation.py`s answer route, one answer per check', 682),
    'A SEALED TOOL`S DEFECT FOUND AFTER THE SEAL, LEFT AS IT STANDS': ('data/b692_rules.txt row (1): left as it stands, entered by the next act`s corrigendum '
                                                                    '-- an answer to its handling, not to its cause', 692),
    'A FACE OR GATE DECLARATION WRONG (arms failing undeclared, a count read as a prediction, multi-arm words, hashes in words)':
        ('G-NOTHING-RAN-AHEAD read against section (0) by hash (b699)', 699),
    'A NAMESAKE FOLLOWED (a local binder read as a kernel declaration)': ('data/b673_rules.txt row (4) (the walk`s reach into local binders, PROSE)', 673),
    'THE NAVIGATOR`S: A CITE, PATH, NAME OR COUNT THE BANKS DO NOT CARRY': ('the citation check, a gate step at step zero, standing from b662', 662),
    'THE NAVIGATOR`S: A PLAN, ORDER OR WORDING THAT CANNOT MEET ITS OWN TEST': ('the citation check and the prompt at step zero (standing from b662); '
                                                                             'data/b690_rules.txt row (3) for a ferry`s wraps', 662),
}


def _defect_rows():
    import b700_record as REC
    rows = []
    for n in range(673, 700):
        act = 'b%d' % n
        L = rdn('%s_defects.txt' % act).split(NL)
        for i, l in enumerate(L):
            m = DEFECT_ROW.match(l)
            if m:
                rows.append(dict(act=act, letter=m.group(1), line=i + 1, head=REC.read_defect_row(L, i) or l.strip()[:160], source='data/%s_defects.txt' % act))
        if n == 699:
            for row, src in REC.closing_defects('b699'):
                mm = re.match(r"^\(([a-z])\) ", row)
                rows.append(dict(act=act, letter=mm.group(1), line=None, head=row, source=src))
    return rows


def defects(*a):
    rows = _defect_rows()
    if a and a[0] == 'list':
        for r in rows:
            print('  %s (%s) %s' % (r['act'], r['letter'], r['head'][:200]))
        print('### ### **DEFECTS %d IN %d ACTS.**' % (len(rows), len(set(r['act'] for r in rows))))
        return
    miss = [r for r in rows if (r['act'], r['letter']) not in CLASS_OF]
    if miss:
        sys.exit('### %d DEFECTS WITHOUT A CLASS (%s) -- NOTHING WRITTEN' % (len(miss), ', '.join('%s (%s)' % (r['act'], r['letter']) for r in miss[:12])))
    for r in rows:
        r['class'] = CLASS_OF[(r['act'], r['letter'])]
    by = collections.defaultdict(list)
    for r in rows:
        by[r['class']].append(r)
    acts = ['b%d' % n for n in range(673, 700)]
    series = [(a_, sum(1 for r in rows if r['act'] == a_)) for a_ in acts]
    L = ['b700 -- COMPONENT 2 (a), (R310)(3)(a): THE DEFECTS BANKS b673 THROUGH b699 READ BY CLASS AND ACT (%s)' % utc(), '', HEAD,
         '### by code: every lettered row of every defects bank b673-b699 (relay data/bNNN_defects.txt, b698_record`s row pattern) and b699`s (d) from its',
         '### closing`s (g) line (the author`s answer at b700); by hand: each defect`s class, the seat`s sort, every defect under one class. A class`s',
         '### recurrence lag: the gaps in acts between its consecutive acts. A class in non-adjacent acts: a STANDING SOURCE, named with the rule or tool',
         '### that answered it and whether it recurred after; a class in adjacent acts alone: CARRIED REPAIR.', '',
         '### THE DEFECTS BY CLASS (class | acts | the recurrence lag | the defects, act (letter)):']
    out = []
    for c in sorted(by, key=lambda c: (-len(by[c]), c)):
        ns = sorted(set(int(r['act'][1:]) for r in by[c]))
        gaps = [b - a_ for a_, b in zip(ns, ns[1:])]
        standing = any(gp > 1 for gp in gaps)
        ans = CLASS_ANSWER.get(c, ('NONE NAMED', None))
        after = None
        if ans[1]:
            after = [n for n in ns if n > ans[1]]
        out.append(dict(cls=c, n=len(by[c]), acts=ns, gaps=gaps, standing=standing, answer=ans[0], answered_at=ans[1], after=after))
        L += ['  %-58s n %-3d acts %s ; lag %s ; %s' % (c, len(by[c]), ','.join(str(x) for x in ns), gaps or '-',
                                                       ('STANDING SOURCE -- answered by %s%s ; recurred after %s' % (
                                                           ans[0], ' (b%d)' % ans[1] if ans[1] else '', ('YES at %s' % ','.join('b%d' % x for x in after))
                                                           if after else ('NO' if ans[1] else 'NOT READ: no answering act named')))
                                                        if standing else ('CARRIED REPAIR (adjacent acts alone)' if len(ns) > 1 else 'ONE ACT'))]
        L += ['      ' + '; '.join('%s (%s) %s' % (r['act'], r['letter'], r['head'][:90]) for r in by[c])]
    L += ['', '### THE PER-ACT TOTALS AS A SERIES: ' + ' '.join('%s:%d' % s_ for s_ in series),
          '### THE SUMS: by class %d ; by act %d ; the banks` rows %d.' % (sum(o['n'] for o in out), sum(v for _a, v in series), len(rows)),
          '', '### ### **DEFECTS %d IN %d CLASSES ; STANDING SOURCES %d (%s) ; CARRIED REPAIRS %d ; ONE-ACT CLASSES %d ; EVERY DEFECT UNDER ONE CLASS %s.**' % (
              len(rows), len(out), sum(1 for o in out if o['standing']), ', '.join(o['cls'] for o in out if o['standing']),
              sum(1 for o in out if not o['standing'] and len(o['acts']) > 1), sum(1 for o in out if len(o['acts']) == 1),
              sum(o['n'] for o in out) == len(rows) == sum(v for _a, v in series))]
    put('defects', L, dict(at=utc(), rows=rows, classes=out, series=series))
    print(L[-1])


# ================================================================================ (b) THE ROSTER-CURRENCY ROWS
KCITE = re.compile(r'\bSIDE-[a-z][a-z0-9-]+ (?:v\d+(?:\.\d+)+|=?\s*`?[0-9a-f]{7}`?)|\bSIDE-[a-z][a-z0-9-]+[^|\n]{0,40}`[0-9a-f]{7}`')


def roster(*a):
    z = zipfile.ZipFile(K.MIRROR_ZIP)
    man = [n for n in z.namelist() if n.endswith('MANIFEST.md')]
    mt = z.read(man[0]).decode('utf-8', 'replace') if man else ''
    papers = sorted(set(m.group(1) for m in re.finditer(r'(?:^|[\s`|(])((?:[\w.-]+/)*[\w.-]+\.md)\b', mt)))
    ro = json.load(io.open(os.path.join(D, 'b672_roster_read.json'), encoding='utf-8'))
    inr = set()
    for t in ro['tables']:
        inr.add(t['path'])
        if t.get('partner'):
            inr.add(t['partner'])
    names_in = set(os.path.basename(p) for p in inr)
    rows = []
    tracked = set(g(PP, 'ls-files', '*.md').split(NL))
    for p in papers:
        # ### the MANIFEST names basenames alone; the frozen deposit copies under outputs/ share them and are not the mirror's -- set apart
        cands = [x for x in tracked if (x == p or x.endswith('/' + p) or os.path.basename(x) == os.path.basename(p)) and not x.startswith('outputs/')]
        for q in sorted(set(cands)):
            if q in inr or q.startswith('archive/') or os.path.basename(q) in ('FINDINGS.md', 'OPEN_TRAILS.md', 'MANIFEST.md'):
                continue
            lines = [(i + 1, l) for i, l in enumerate(rd(os.path.join(PP, q)).split(NL)) if KCITE.search(l)]
            if lines:
                rows.append(dict(path=q, lines=[n for n, _l in lines], first=' '.join(lines[0][1].split())[:160],
                                 kernels=sorted(set(re.findall(r'SIDE-[a-z][a-z0-9-]+', ' '.join(l for _n, l in lines))))))
    two = [r for r in rows if 'THE_TWO_THREE_SUBSTRATE' in r['path']]
    L = ['b700 -- COMPONENT 2 (b), (R310)(3)(b): THE ROSTER-CURRENCY ROWS -- EVERY PAPER IN THE MIRROR ROSTER CARRYING A KERNEL CITATION AND ABSENT FROM '
         'b672`S GENERATOR ROSTER (%s)' % utc(), '', HEAD,
         '### the mirror roster: %s, its %s (read by zipfile), %d .md names; each resolved to the files PLACE-papers tracks at HEAD of that name' % (
             K.MIRROR_ZIP, man[0] if man else '### NO MANIFEST', len(papers)),
         '### (the ledgers and archive/ copies set apart); the generator roster: relay data/b672_roster_read.json, %d tables and their partners (%d files).' % (
             len(ro['tables']), len(inr)),
         '### a kernel citation: a line naming SIDE-<kernel> with a version tag vN.N or a seven-hex commit (the pattern beside). Rows are papers:',
         '### pattern: %s' % KCITE.pattern]
    L += ['  %-92s lines citing %3d (%s%s) ; kernels %s ; first: %s' % (r['path'], len(r['lines']), ', '.join(':%d' % n for n in r['lines'][:8]),
                                                                      ', ...' if len(r['lines']) > 8 else '', ' '.join(r['kernels'][:6]), r['first'])
          for r in rows]
    L += ['', '### THE MANIFEST`S .md NAMES AS READ (%d): %s' % (len(papers), ' '.join(papers))]
    L += ['', '### THE_TWO_THREE_SUBSTRATE AMONG THEM: %s' % ('; '.join('%s (%d lines)' % (r['path'], len(r['lines'])) for r in two) or 'NOT FOUND'),
          '', '### ### **PAPERS OUTSIDE THE ROSTER CARRYING A KERNEL CITATION %d ; LINES CITING %d ; THE_TWO_THREE_SUBSTRATE AMONG THEM %s.**' % (
              len(rows), sum(len(r['lines']) for r in rows), bool(two))]
    put('roster', L, dict(at=utc(), manifest=man[0] if man else None, papers=len(papers), rows=rows, two_three=[r['path'] for r in two]))
    print(L[-1])


# ================================================================================ (c) THE KERNEL TAGS MOVED SINCE b690, BY ls-remote, AGAINST THE PAPERS
TAGS_NAMED = (('SIDE-explicit-formula', 'v0.34'), ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'), ('SIDE-rcurve', None),
              ('SIDE-archimedean', 'v0.1.1'), ('SIDE-interfaces', 'v0.2.1'), ('SIDE-simplicity', 'v0.1.2'), ('SIDE-substrate-cluster', 'v0.4.1'))


def _vkey(t):
    return tuple(int(x) for x in re.findall(r'\d+', t))


def tags(*a):
    """ONE repository's tags by ONE ls-remote (data/b674_rules.txt row (1)); appended to data/b700_r4_tags.json under the kernel's name."""
    k = a[0] if a else ''
    if k not in dict(TAGS_NAMED):
        sys.exit('### usage: tags <kernel>, one of %s' % ', '.join(x for x, _ in TAGS_NAMED))
    r = subprocess.run(['git', '-C', 'D:/' + k, 'ls-remote', '--tags', 'origin'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = r.stdout
    peel = {}
    for l in out.split(NL):
        m = re.match(r'^([0-9a-f]{40})\s+refs/tags/(v[\d.]+)(\^\{\})?$', l)
        if m:
            if m.group(3) or m.group(2) not in peel:
                peel[m.group(2)] = m.group(1)
    j = jn('b700_r4_tags.json') or dict(kernels={})
    if not peel:
        j['kernels'][k] = dict(at=utc(), empty=True, rc=r.returncode, reads=j['kernels'].get(k, {}).get('reads', 0) + 1)
        print('  %s: EMPTY READ (exit %d) -- re-read alone' % (k, r.returncode))
    else:
        hi = max(peel, key=_vkey)
        j['kernels'][k] = dict(at=utc(), highest=hi, commit=peel[hi], tags=sorted(peel, key=_vkey), named=dict(TAGS_NAMED)[k], empty=False)
        print('  %s: %d tags ; the highest %s = %s ; the ruling names %s' % (k, len(peel), hi, peel[hi][:7], dict(TAGS_NAMED)[k] or '(none)'))
    p = os.path.join(D, 'b700_r4_tags.json')
    open(p + '.tmp', 'wb').write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def tagsread(*a):
    j = jn('b700_r4_tags.json').get('kernels') or {}
    miss = [k for k, _t in TAGS_NAMED if not (j.get(k) or {}).get('highest')]
    if miss:
        sys.exit('### NOT READ BY ls-remote: %s -- NOTHING WRITTEN' % ', '.join(miss))
    rows, tot = [], collections.Counter()
    for k, named in TAGS_NAMED:
        hi = j[k]['highest']
        pat = r'%s v[0-9]+(\.[0-9]+)+' % re.escape(k)
        out = g(PP, 'grep', '-n', '-E', pat, 'HEAD', '--', '*.md')
        for l in out.split(NL):
            m = re.match(r'^HEAD:([^:]+):(\d+):(.*)$', l)
            if not m:
                continue
            f, ln, text = m.group(1), int(m.group(2)), m.group(3)
            vs = [x.group(1) for x in re.finditer(r'%s (v[0-9]+(?:\.[0-9]+)+)' % re.escape(k), text)]
            ledger = f in ('FINDINGS.md', 'OPEN_TRAILS.md') or f.startswith('archive/')
            behind = [v for v in vs if _vkey(v) < _vkey(hi)]
            st = 'BEHIND' if behind and not any(_vkey(v) >= _vkey(hi) for v in vs) else ('MIXED' if behind else 'AT THE TAG')
            rows.append(dict(kernel=k, file=f, line=ln, versions=vs, state=st, ledger=ledger))
            tot[(k, st, ledger)] += 1
    L = ['b700 -- COMPONENT 2 (c), (R310)(3)(c): THE KERNEL TAGS MOVED SINCE b690, EACH READ FROM ls-remote, AGAINST EVERY PAPER LINE NAMING THE '
         'KERNEL`S TAG (%s)' % utc(), '', HEAD,
         '### the tags: one `git ls-remote --tags origin` per repository, one call each, in sequence (this tool`s `tags` route, data/b700_r4_tags.json):']
    L += ['    %-24s the highest %-8s = %s ; the ruling names %s ; read at %s' % (k, j[k]['highest'], j[k]['commit'][:7], named or '(none)', j[k]['at'])
          for k, named in TAGS_NAMED]
    L += ['### the lines: git grep -n -E "<kernel> v<N.N...>" at PLACE-papers HEAD over *.md; a line BEHIND names only versions below the highest, MIXED',
          '### one below and one at it, AT THE TAG none below; the ledgers (FINDINGS, OPEN_TRAILS, archive/) records at their acts, counted apart.',
          '### THE LINES BEHIND OUTSIDE THE LEDGERS, by kernel, file and line:']
    for k, _n in TAGS_NAMED:
        bh = [r for r in rows if r['kernel'] == k and r['state'] != 'AT THE TAG' and not r['ledger']]
        L += ['  %-24s %d: %s' % (k, len(bh), '; '.join('%s :%d [%s %s]' % (r['file'], r['line'], r['state'], ','.join(r['versions'])) for r in bh) or 'NONE')]
    L += ['', '### THE LINES BEHIND OUTSIDE THE LEDGERS BY FILE (kernel ; file ; lines ; the versions named), for the hand`s reading of pins against claims:']
    for k, _n in TAGS_NAMED:
        byf = collections.defaultdict(list)
        for r in rows:
            if r['kernel'] == k and r['state'] != 'AT THE TAG' and not r['ledger']:
                byf[r['file']].append(r)
        L += ['  %-24s %-84s %4d ; %s' % (k, f, len(v), ','.join(sorted(set(x for r in v for x in r['versions']), key=_vkey)))
              for f, v in sorted(byf.items(), key=lambda kv: -len(kv[1]))]
    L += ['', '### THE COUNTS (kernel ; outside the ledgers BEHIND / MIXED / AT THE TAG ; in the ledgers BEHIND / MIXED / AT THE TAG):']
    L += ['  %-24s %d / %d / %d ; %d / %d / %d' % ((k,) + tuple(tot[(k, s_, False)] for s_ in ('BEHIND', 'MIXED', 'AT THE TAG')) +
                                               tuple(tot[(k, s_, True)] for s_ in ('BEHIND', 'MIXED', 'AT THE TAG'))) for k, _n in TAGS_NAMED]
    nb = sum(v for (k, s_, led), v in tot.items() if s_ != 'AT THE TAG' and not led)
    # ### a superseded copy: a file whose stem carries a version (_vN_N...) with a sibling in its directory of the same stem and a higher version,
    # ### or the bare stem beside it -- its lines are the record of its date; the rest are current files
    tracked = [x for x in g(PP, 'ls-files', '*.md').split(NL) if x]
    stems = collections.defaultdict(list)
    for x in tracked:
        m = re.match(r'^(.*?)(?:_v(\d+(?:_\d+)*))?\.md$', x)
        stems[m.group(1)].append(tuple(int(y) for y in m.group(2).split('_')) if m.group(2) else None)

    def superseded(f):
        m = re.match(r'^(.*?)(?:_v(\d+(?:_\d+)*))?\.md$', f)
        if not m.group(2):
            return False
        v = tuple(int(y) for y in m.group(2).split('_'))
        return any(o is not None and o > v for o in stems[m.group(1)])
    out_rows = [r for r in rows if r['state'] != 'AT THE TAG' and not r['ledger']]
    sup = [r for r in out_rows if superseded(r['file'])]
    cur = [r for r in out_rows if not superseded(r['file'])]
    L += ['', '### OUTSIDE THE LEDGERS, BY THE FILE`S STANDING: in a superseded versioned copy (a sibling of the same stem at a higher version) %d lines'
              ' in %d files ; in a current file %d lines in %d files:' % (len(sup), len(set(r['file'] for r in sup)), len(cur), len(set(r['file'] for r in cur)))]
    L += ['  %-24s %s' % (k, '; '.join('%s (%d)' % (f, n) for f, n in collections.Counter(r['file'] for r in cur if r['kernel'] == k).most_common()) or 'NONE')
          for k, _n in TAGS_NAMED]
    L += ['', '### ### **KERNELS READ BY ls-remote %d ; PAPER LINES NAMING A TAG %d ; BEHIND OR MIXED OUTSIDE THE LEDGERS %d (IN SUPERSEDED COPIES %d, IN '
          'CURRENT FILES %d) ; IN THE LEDGERS %d.**' % (len(TAGS_NAMED), len(rows), nb, len(sup), len(cur),
                                                       sum(v for (k, s_, led), v in tot.items() if s_ != 'AT THE TAG' and led))]
    put('tagsread', L, dict(at=utc(), tags=j, rows=rows, behind_outside=nb, superseded=len(sup), current=len(cur),
                            current_rows=[dict(kernel=r['kernel'], file=r['file'], line=r['line'], versions=r['versions']) for r in cur]))
    print(L[-1])


# ================================================================================ (d) THE CIRCUIT INSTRUMENT'S READINGS AS CENSUS ROWS
CIRCUIT = (
    ('CLAUSE-DOMINANCE by closure', 'b694_circuit_dominance.txt', r'CLAUSE-DOMINANCE (\d+ OF \d+) FACES KERNELS'),
    ('CLAUSE-DOMINANCE by correspondence', 'b698_correspondence_dominance.txt', r'(DIFFERS at binder \d+)[^;]*BY CORRESPONDENCE'),
    ('WIDTH, SIDE-explicit-formula v0.34.1', 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt', r'WIDTH: (SAME-TYPE THEOREM PAIRS \d+, AT OR UNDER FEW = 5: \d+)'),
    ('WIDTH, SIDE-lv-conservation v0.13.0', 'b694_circuit_SIDE-lv-conservation_v0.13.0.txt', r'WIDTH: (SAME-TYPE THEOREM PAIRS \d+, AT OR UNDER FEW = 5: \d+)'),
    ('LOAD`s three highest, SIDE-explicit-formula', 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt', r'LOAD`S THREE HIGHEST (.+?)\.\*\*'),
    ('LOAD`s three highest, SIDE-lv-conservation', 'b694_circuit_SIDE-lv-conservation_v0.13.0.txt', r'LOAD`S THREE HIGHEST (.+?)\.\*\*'),
    ('SHORTS, SIDE-explicit-formula v0.34.1', 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt', r'(SHORTS \d+)'),
    ('SHORTS, SIDE-lv-conservation v0.13.0', 'b694_circuit_SIDE-lv-conservation_v0.13.0.txt', r'(SHORTS \d+)'),
    ('SHORTS, the planted control (b692)', 'b692_circuit_shorts_branch.txt', r'(SHORTS \d+) \(RECORDS CARRYING sorryAx\)'),
    ('READFIRST-CLOSURE against this act`s hand list', 'b700_readfirst_diff.txt', r'(LINES DIFFERING \d+ \(HAND ONLY \d+, OF WHICH IN THE CLOSURE \d+ ; TEXT ONLY \d+\))'),
    ('SUITE-LOAD`s factor (b692)', 'b692_suite_load.txt', r'(THE FACTOR \d+\.\d+)'),
)


def circuit(*a):
    rows = []
    for what, bank, pat in CIRCUIT:
        L0 = rdn(bank).split(NL)
        hit = [(i + 1, re.search(pat, l)) for i, l in enumerate(L0) if l.startswith('### ### **') and re.search(pat, l)]
        rows.append(dict(reading=what, bank='data/' + bank, line=hit[-1][0] if hit else None, value=hit[-1][1].group(1) if hit else '### UNREAD'))
    L = ['b700 -- COMPONENT 2 (d), (R310)(3)(d): THE CIRCUIT INSTRUMENT`S READINGS AS CENSUS ROWS (%s)' % utc(), '', HEAD,
         '### by code: each reading`s value from its bank`s verdict line (the instrument`s own print, b692-b698; READFIRST-CLOSURE this act`s), by the',
         '### pattern beside. No instrument is re-run: no lean and no runner this act (N1). Rows are readings: reading | value | bank :line:']
    L += ['  %-48s | %-90s | %s :%s' % (r['reading'], r['value'], r['bank'], r['line']) for r in rows]
    L += ['', '### ### **CIRCUIT READINGS %d, READ %d ; CLAUSE-DOMINANCE %s BY CLOSURE, %s BY CORRESPONDENCE ; SUITE-LOAD %s.**' % (
        len(rows), sum(1 for r in rows if r['line']), rows[0]['value'], rows[1]['value'], rows[-1]['value'])]
    put('circuit', L, dict(at=utc(), rows=rows))
    print(L[-1])


# ================================================================================ (e) THE REGULARITY BANK BESIDE THE BRIDGE PLAN'S PRICE
def regularity(*a):
    ru = rdn('b698_regularity_uses.txt').split(NL)
    pl = rdn('b699_bridge_plan.txt').split(NL)
    uses, path, verd = ru[84].strip(), ru[85].strip(), ru[86].strip()
    pr = [(i + 1, l.strip()) for i, l in enumerate(pl) if 'PRICE: 1 dispatch' in l]
    L = ['b700 -- COMPONENT 2 (e), (R310)(3)(e): THE REGULARITY BANK`S PER-CLASS COUNTS BESIDE THE BRIDGE PLAN`S PRICE, THE TWO INPUTS TO b701`S WORD (%s)'
         % utc(), '', HEAD,
         '### re-printed verbatim, by line:',
         '  relay data/b698_regularity_uses.txt :85  %s' % uses,
         '  relay data/b698_regularity_uses.txt :86  %s' % path,
         '  relay data/b698_regularity_uses.txt :87  %s' % verd,
         '  relay data/b699_bridge_plan.txt :%d  %s' % (pr[0] if pr else (0, '### UNREAD')),
         '### the slate priced from them at step zero: relay data/b700_slate.txt (classK to W1 ∪ W3: 10 uses and 4 path leaves RE-PROVED, 1 dispatch in',
         '### b689`s form ; the bridge 1 dispatch).',
         '', '### ### **REGULARITY: %s ; THE BRIDGE: PRICE 1 DISPATCH.**' % re.sub(r'^###\s+the uses, 17 rows:\s+', 'USES ', uses)]
    put('regularity', L, dict(at=utc(), uses=uses, path=path, verdict=verd, price=pr[0] if pr else None))
    print(L[-1])


ROUTES = {'licensed': licensed, 'corr': corr, 'ceiling': ceiling, 'orders': orders, 'methods': methods, 'lag': lag, 'residues': residues,
          'rules': rules, 'arms': arms, 'p3': p3, 'faces': faces, 'onecopy': onecopy, 'pair': pair, 'defects': defects, 'roster': roster,
          'tags': tags, 'tagsread': tagsread, 'circuit': circuit, 'regularity': regularity}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b700_readings.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
