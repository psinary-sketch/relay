# -*- coding: utf-8 -*-
"""b683_epstein_map_angle.py -- THE DETECTION MAP IN THE ANGLE FORM OVER THE b681 BALLS (h = 1e-30), under (R293)(3)-(4): b677's map,
IMPORTED UNCHANGED (tools/b677_epstein_map_angle.py, sha256 b21f6926..., the text its bank data/b677_map.txt names), run by the same
part 1 over the narrowed bank of b681.

### THE CHANGES, EACH NAMED IN THE PLAN (data/b683_map_plan.txt section 1), AND NONE IN A COMPUTATION LINE:
###   (i)   the balls: the tool's Q0_CERT pointed at relay data/b681_epstein_zeros_narrowed.json(.gz) -- the one changed line OPEN_TRAILS :14714
###         prices ("a copy whose one changed line is the bank's name"), made here as an assignment on the imported module;
###   (ii)  the banks: the tool's own writes (_put, _putj) renamed b677_ -> b683_, and the first line of each bank prefixed with this act's
###         name, so no b677 bank is touched;
###   (iii) the rung forced at Q0: the tool re-reads a cell at 400 bits only when the 200-bit reading triggers it; over the new balls no
###         trigger is expected, so the 400-bit rows of b671's list (data/b671_tie_diagnostic.txt :89-:129) would go unread -- the 200-bit
###         cell's trigger list carries one named entry, "FORCED RUNG (R293) N3", and the tool's own rung code runs as written;
###   (iv)  the hypotheses: `hyp` reads (R293)(4)'s H1-H5 from this act's banks and b677's (data/b683_map_h.txt), in place of b677's own.
### Routes, each one foreground part under 540 s: `chain` -> data/b683_chain.txt (the hash chain verified before any ball is read);
### `part1` -> data/b683_map.txt (.json), data/b683_map_run.txt (refuses unless the chain re-verifies in the same process); `hyp` ->
### data/b683_map_h.txt (.json). No lean; no kernel file read; the b667 and b677 maps unedited (their sha256 printed before and after).
### Written by the Write tool at b683.
"""
import hashlib
import gzip
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b683_worklist as K                  # noqa: E402
B677_TOOL = os.path.join(T, 'b677_epstein_map_angle.py')
B667_TOOL = os.path.join(T, 'b667_epstein_map_balls.py')
B677_SHA = 'b21f6926056461a39cd19299ca23433ce3819748bb7739491c765ecbcc52176f'
B667_SHA = '011bbe47d528eb170ffcbca6f1ef500d09a517933071fe2313e5719072afe275'
FORCED = 'FORCED RUNG (R293) N3: the 400-bit rows of b671`s list read (data/b671_tie_diagnostic.txt :89-:129)'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _bank_line(name, needle):
    t = io.open(os.path.join(D, name), encoding='utf-8').read()
    return next((l for l in t.split(NL) if needle in l), '')


def chain_rows():
    """the hash chain: the b681 bank's .gz and JSON against its hashes bank; the b671 bank's against b671's hashes bank and against the b681
    hashes bank's `chains from` line. Rows: (what, read, banked, equal)."""
    gz = os.path.join(D, K.BALLS + '.gz')
    raw = open(gz, 'rb').read()
    js = gzip.decompress(raw)
    o = os.path.join(D, 'b671_epstein_zeros_narrowed.json.gz')
    oraw = open(o, 'rb').read()
    ojs = gzip.decompress(oraw)
    h81 = 'b681_epstein_zeros_narrowed_hashes.txt'
    h71 = 'b671_epstein_zeros_narrowed_hashes.txt'
    cf = _bank_line(h81, 'chains from:')
    R = [('b681 JSON (inside the .gz)', hashlib.sha256(js).hexdigest(), _bank_line(h81, 'narrowed.json (inside').split('sha256 ')[1].split()[0]),
         ('b681 .gz', hashlib.sha256(raw).hexdigest(), _bank_line(h81, 'narrowed.json.gz sha256').split('sha256 ')[1].split()[0]),
         ('b671 .gz (b671`s hashes bank :3)', hashlib.sha256(oraw).hexdigest(), _bank_line(h71, 'narrowed.json.gz sha256').split('sha256 ')[1].split()[0]),
         ('b671 JSON (b671`s hashes bank :2)', hashlib.sha256(ojs).hexdigest(), _bank_line(h71, 'narrowed.json (inside').split('sha256 ')[1].split()[0]),
         ('b671 .gz (the b681 bank`s chains-from line)', hashlib.sha256(oraw).hexdigest(), cf.split('sha256 ')[1].split(',')[0].strip()),
         ('b671 JSON (the b681 bank`s chains-from line)', hashlib.sha256(ojs).hexdigest(), cf.split('its JSON ')[1].split()[0]),
         ('b681 .gz (the worklist`s constant)', hashlib.sha256(raw).hexdigest(), K.BALLS_GZ_SHA)]
    d = json.loads(js.decode('utf-8'))
    rows = d['rows']
    shape = (len(rows) == 163 and sum(r['kind'] == 'ON' for r in rows) == 146 and sum(r['kind'] == 'OFF' for r in rows) == 17
             and all(r['count'] == 1 and r['h'] == '1e-30' for r in rows))
    return [(w, a, b, a == b) for w, a, b in R], shape, len(rows)


def chain(*a):
    R, shape, n = chain_rows()
    ok = all(x[3] for x in R) and shape
    L = ['b683 -- THE HASH CHAIN OF THE b681 BANK, VERIFIED BEFORE ANY BALL IS READ ((R293)(3), N2) (%s): rows are files -- what, the sha256 read '
         'now, the sha256 banked, EQUAL or DIFFERS.' % utc(), '']
    L += ['  %-46s read %s ; banked %s ; %s' % (w, x, y, 'EQUAL' if e else 'DIFFERS') for w, x, y, e in R]
    L += ['', '### the rows: %d ; 146 ON and 17 OFF, every count 1 and every half-width 1e-30: %s' % (n, shape),
          '', '### ### **THE CHAIN %s ; FILES %d EQUAL %d ; THE BANK`S SHAPE %s.**' % ('VERIFIED' if ok else 'NOT VERIFIED', len(R), sum(x[3] for x in R), shape)]
    io.open(os.path.join(D, 'b683_chain.txt'), 'w', encoding='utf-8', newline='\n').write(NL.join(L) + NL)
    print(NL.join(L))
    return ok


def _module():
    if sha(B677_TOOL) != B677_SHA or sha(B667_TOOL) != B667_SHA:
        sys.exit('### THE b677 OR b667 MAP IS NOT THE TEXT b677 RAN -- NOTHING READ, NOTHING WRITTEN')
    import b677_epstein_map_angle as M
    M.Q0_CERT = K.BALLS                                                      # ### change (i)
    put0 = M._put

    def _put(name, text):                                                    # ### change (ii)
        nm = name.replace('b677_', 'b683_')
        if nm == name:
            sys.exit('### A WRITE NOT UNDER THE b677_ NAME (%s) -- STOPPED' % name)
        L = text.split(NL)
        if L and L[0].startswith('b677 -- '):
            L[0] = ('b683 -- (R293)(4), BY tools/b677_epstein_map_angle.py IMPORTED UNCHANGED THROUGH tools/b683_epstein_map_angle.py, OVER relay '
                    'data/%s.gz (h = 1e-30); THE TOOL`S OWN TITLE: ' % K.BALLS) + L[0][len('b677 -- '):]
        put0(nm, NL.join(L))
    M._put = _put
    cell0 = M.cell

    def cell(name, base, online, offline, prec, i4, **kw):                    # ### change (iii)
        r = cell0(name, base, online, offline, prec, i4, **kw)
        if name == 'Q0 AT qE0' and prec == M.PREC and 'rung_note' not in kw:
            r['triggers'] = list(r.get('triggers') or []) + [FORCED]
        return r
    M.cell = cell
    return M


def part1(*a):
    if not chain():
        sys.exit('### THE CHAIN DOES NOT VERIFY -- NO BALL READ, NOTHING WRITTEN')
    M = _module()
    t0 = time.time()
    M.part1()
    print('### b683 part 1: the b677 map sha256 %s after (%s) ; the b667 map %s (%s) ; %d s' % (
        sha(B677_TOOL), 'EQUAL' if sha(B677_TOOL) == B677_SHA else 'CHANGED', sha(B667_TOOL), 'EQUAL' if sha(B667_TOOL) == B667_SHA else 'CHANGED',
        int(time.time() - t0)))


# ================================================================================ THE HYPOTHESES OF (R293)(4) (change (iv))
def _rd(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def hyp(*a):
    m, m77 = _rd('b683_map.json'), _rd('b677_map.json')
    bar = K.BAR
    rows = m['rows']
    q = m['q0']
    # ### H1: every control b671 or b677 read INSTRUMENT reads PASS now
    was77 = set((x['cell'], x['bits'], x['j']) for x in m77['rows'] if x['word'] == 'INSTRUMENT')
    was = [x for x in rows if x['b671'] == 'INSTRUMENT' or (x['cell'], x['bits'], x['j']) in was77]
    h1_bad = [x for x in was if x['word'] != 'PASS']
    h1 = not h1_bad and len(rows) == 123
    allpass = sum(x['word'] == 'PASS' for x in rows)
    # ### H2: the radius at j = 64 below the bar for every tie
    q64 = [x for x in rows if x['cell'] == 'Q0 AT qE0' and x['j'] == 64]
    big = max(q64, key=lambda x: x['rad']) if q64 else None
    h2 = bool(q64) and all(x['rad'] < bar for x in q64)
    # ### H3: b663 :131 -- every hypothesis certifies by name and hrate holds at some j0 <= D + 40
    certs = q.get('certs') or []
    notc = [c[0] for c in certs if c[1] != 'CERTIFIED']
    j0 = (q.get('zero_side') or {}).get('j0')
    rdg = q.get('reading') or ''
    h3 = not notc and rdg.startswith('j₀') and j0 is not None and j0 <= (q.get('D') or 24) + 40
    # ### H4: b667 :124-:125 -- j0 = 38 and a zero side below zero, each with its ball; SCORABLE when a j0 is read
    zs = q.get('zero_side')
    h4s = 'SCORABLE' if (zs and j0 is not None) else 'NOT SCORABLE'
    h4 = h4s == 'SCORABLE' and j0 == K_H4_J0 and bool(zs.get('held'))
    hq = q.get('hqtie') or [None, None]
    # ### H5: b677's instrument-side row (hQtie from coeffs_exist and the orbit identity) against the ball reading, by j
    lab = (m77['q0'].get('labelled') or {})
    lh = dict((h[0], h[1]) for h in lab.get('hrate') or [])
    bh = dict((h[0], h[1]) for h in (q.get('hrate') or []))
    both = sorted(set(lh) & set(bh))
    dis = [(j, lh[j], bh[j]) for j in both if lh[j] != bh[j]]
    lz = (m77['q0'].get('labelled') or {}).get('zero_side') or {}
    h5 = bool(both) and not dis and lz.get('j0') == j0 and bool(lz.get('held')) == bool((zs or {}).get('held'))
    L = ['b683 -- THE HYPOTHESES OF (R293)(4), READ ON THE RUN (data/b683_map_h.txt) (%s): rows are the hypotheses with their reading and the '
         'rows that decide them.' % utc(), '',
         '  H1 %s -- of the %d controls b671 or b677 read INSTRUMENT (data/b671_tie_diagnostic.txt :66-:88, :107-:129; data/b677_map.txt), %d read '
         'PASS over the b681 balls and %d do not%s; of all %d rows of b671`s list, PASS %d (data/b683_map.txt).' % (
             'HELD' if h1 else 'REFUTED', len(was), len(was) - len(h1_bad), len(h1_bad),
             (' (' + ', '.join('%d bits j %d %s' % (x['bits'], x['j'], x['word']) for x in h1_bad[:6]) + ')') if h1_bad else '', len(rows), allpass),
         '  H2 %s -- the residual radius at j = 64: %s against the bar %.6e; the largest %.3e (%d bits), its ratio to the bar %.3e (data/b683_map.txt).' % (
             'HELD' if h2 else 'REFUTED', ', '.join('%d bits %.3e' % (x['bits'], x['rad']) for x in q64), bar, big['rad'] if big else float('nan'),
             big['bits'] if big else 0, (big['rad'] / bar) if big else float('nan')),
         '  H3 %s -- as data/b663_epstein_plan.txt :131 states it: the map reads %s; hypotheses not certified %s; hQtie controls %s of %s%s '
         '(data/b683_map_run.txt).' % ('HELD' if h3 else 'REFUTED', rdg, notc or 'NONE', hq[0], hq[1],
                                       (', j₀ = %d ≤ D + 40 = %d' % (j0, (q.get('D') or 24) + 40)) if h3 else ''),
         '  H4 %s, %s -- as data/b667_epstein_plan.txt :124-:125 states it ("prints j₀ = 38 and a zero side below zero, each with its ball"): '
         'j₀ %s ; the zero side %s (%s) ; hQtie %s of %s.' % (
             h4s, ('HELD' if h4 else 'REFUTED') if h4s == 'SCORABLE' else 'unread', j0, (zs or {}).get('zero_side'),
             'BELOW 0' if (zs or {}).get('held') else 'NOT BELOW 0', hq[0], hq[1]),
         '  H5 %s -- b677`s instrument-side row (data/b677_map_h.txt :9; hrate by j from data/b677_map.json, j₀ %s, the zero side %s) against the '
         'ball reading at the %d j where both exist (%s): disagreements %s; j₀ %s against %s.' % (
             'HELD' if h5 else 'REFUTED', lz.get('j0'), lz.get('zero_side'), len(both), ('%d-%d' % (both[0], both[-1])) if both else '-',
             dis or 'NONE', lz.get('j0'), j0), '',
         '### ### **H1 %s ; H2 %s ; H3 %s ; H4 %s ; H5 %s.**' % ('HELD' if h1 else 'REFUTED', 'HELD' if h2 else 'REFUTED', 'HELD' if h3 else 'REFUTED',
                                                               h4s + ((' ' + ('HELD' if h4 else 'REFUTED')) if h4s == 'SCORABLE' else ''),
                                                               'HELD' if h5 else 'REFUTED')]
    io.open(os.path.join(D, 'b683_map_h.txt'), 'w', encoding='utf-8', newline='\n').write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b683_map_h.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(dict(
        at=utc(), H1=h1, H2=h2, H3=h3, H4=h4s, H4_held=h4, H5=h5, j0=j0, hqtie=hq, rad64=[(x['bits'], x['rad']) for x in q64],
        h1_bad=[(x['bits'], x['j'], x['word']) for x in h1_bad], h5_disagree=dis, h5_both=both, pass_all=allpass, rows=len(rows)),
        indent=1, ensure_ascii=False) + NL)
    print(NL.join(L))


K_H4_J0 = 38            # ### H4's j₀ (data/b667_epstein_plan.txt :125)

if __name__ == '__main__':
    fn = {'chain': chain, 'part1': part1, 'hyp': hyp}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b683_epstein_map_angle.py chain | part1 | hyp')
        sys.exit(2)
    fn(*sys.argv[2:])
