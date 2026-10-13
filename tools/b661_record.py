# -*- coding: utf-8 -*-
"""b661_record.py -- THE ACT'S RECORD TOOL, b661 under (R271).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b661's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b659_record.py (the landing and its screens, the readers' form, the record lines); the routes of the later
### components are added to this file by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b661_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b661_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B661_STANDIN'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'H1', 'H2', 'H3', 'H4')
    return {
        'b661_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b661_findings.json': dict(entry_line=99999, title='stand-in'),
        'b661_trail.json': dict(line=99999),
        'b661_act_root.json': dict(root='0' * 64, previous='c147a36e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b661's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b661_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
def read_score_row(k, v):
    """a scores row: key N1..N5 or H1..H4, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|H[1-4])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS = ('read_score_row', 'read_head')


# ================================================================================ COMPONENT 1: THE RECORD LINE, (R271)(1)
WH = ('*Appended 2026-10-13 by b661 to b660’s entry (:8461), under `(R271)`(1) -- b660 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b660_closing.txt):*')


def _weight():
    return ('\n' + WH + ' the ten acts b650–b659 read as one (relay data/b660_ten_acts.txt) -- 63 defects, the seat’s 48 in 11 kinds with 9 '
            'recurring, CONVERSION closed by rule and 8 recurring kinds OPEN, TEXT and ROUTE closed; the navigator’s 14 of one kind, both seats’ '
            'sentences banked side by side; the lanes (relay data/b660_lanes.txt) -- 4 kernels merged covering 205 of 266 OVERREACHES, 15 '
            'remaining with 61, SIDE-lv-conservation’s 13 UNRESOLVED rows and its cell refreshes owed, 14 work-orders and items at 3 DISCHARGED, '
            '2 ACTED, 9 PRICED; the author’s word -- Q1 and Q5 RETIRED, Q2 and Q3 STAYS, Q4 WORK-ORDER standing, W-ORD-CITATION-CHECK a gate '
            'step at b662, W-ORD-VERDICT-INSTRUMENT and W-ORD-PLAIN-COMMENT-ARM DISCHARGED, the research order Epstein, Keiper, χ-Li after b661, '
            'the Project loop CLOSED; relay 2e439312, PLACE-papers 2e07a61, FINDINGS :8459 and :8461, OPEN_TRAILS :14092, the root c147a36e… '
            'over 18 banks; the suite 72 of 77, the four act-shaped failures and the carried row declared; three defects the seat’s, (c) outside '
            'the root in the closing. No tool file changed. Nothing deposited.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight())]
    land(items, 'b661_record_lines.json', 'c1', entry=K.B660_ENTRY,
         check=[('FINDINGS.md', K.B660_ENTRY, '## The reading act: ten acts b650–b659'),
                ('OPEN_TRAILS.md', K.B660_TRAIL, '### b660 — lane three, act eighty-seven')],
         dry='dry' in a)


ROUTES = {'c1': c1}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        print('usage: b661_record.py <%s> [dry]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    ROUTES[sys.argv[1]](*sys.argv[2:])
