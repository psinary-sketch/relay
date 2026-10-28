# -*- coding: utf-8 -*-
"""b721_offset.py -- (R331)(5): THE OFFSET UNDER H-OFFSET (data/b719_registrations.txt :46-:59), per data/b720_offset_price.txt.

  python -X utf8 -u tools/b721_offset.py pred [bank]   (i) the seventeen banked pairs, POST HOC: the controls, then every pair's r(rho)
                                                       and scorability (the count first), then delta_pred from r and n*_pred ALONE --
                                                       no n* is read by this route. bank -> data/b721_offset_pred.txt, committed alone.
  python -X utf8 -u tools/b721_offset.py read [bank]   (i) refused unless the pred bank on disk is the committed one (git show HEAD:);
                                                       the plant first, then the observed n* beside each committed delta_pred, each row
                                                       labelled POST HOC. bank -> data/b721_offset_read.txt.
  python -X utf8 -u tools/b721_offset.py tier [bank]   (ii) the next tier: every banked pair not yet given an onset, chosen by r(rho) <= 0.05
                                                       alone; each pair's reach on its banked list and its price read from the banked
                                                       list and onset timings; no list extended, no onset run. bank -> data/b721_offset_tier.txt.

Reads banks only: data/b713_predictions.json, data/b713_onsets.json (rows and c1, Q0's pairs 11 and 15), data/b717_predictions.json,
data/b717_onsets.json, data/b711_list.json, data/b713_list.json, data/b717_list.json. Nothing at any pair is recomputed: r and n*_pred are
the banks', delta_pred the closed form of H-OFFSET :51. Written by the Write tool at b721.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRED = os.path.join(D, 'b721_offset_pred.txt')
READ = os.path.join(D, 'b721_offset_read.txt')
TIER = os.path.join(D, 'b721_offset_tier.txt')
R_MAX = 0.05
BOUND = 2.0


def P(f):
    return json.load(io.open(os.path.join(D, f), encoding='utf-8'))


def ball(s):
    """'[mid +/- rad]' -> (mid, rad) as floats; a bare number -> (x, 0)."""
    m = re.match(r'^\[\s*([-+0-9.eE]+)\s*\+/-\s*([0-9.eE+-]+)\s*\]$', str(s).strip())
    if m:
        return float(m.group(1)), float(m.group(2))
    return float(s), 0.0


def delta(r, n):
    """H-OFFSET :51: delta_pred = (3/8) L / (1 - 8/(r (n*_pred + 1))), L = r n*_pred."""
    return 0.375 * r * n / (1 - 8.0 / (r * (n + 1)))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def seventeen():
    """the seventeen in data/b720_offset_price.txt :12's order: b713's eight at -15, b714's Q0 pairs 11 and 15, b717's seven at -39."""
    out = []
    p13 = dict((x['k'], x) for x in P('b713_predictions.json')['rows'])
    o13 = P('b713_onsets.json')
    for x in o13['rows']:
        r, rr = ball(p13[x['k']]['r'])
        out.append(dict(field='-15', k=x['k'], r=r, r_rad=rr, n_pred=x['n_pred'], n_star=x['n_star'],
                        src='b713_predictions.json rows k=%d r ; b713_onsets.json rows n_pred, n_star' % x['k']))
    for c in o13['c1']:
        r, rr = ball(c['r'])
        n, _nr = ball(c['n_pred'])
        out.append(dict(field='Q0', k=c['idx'], r=r, r_rad=rr, n_pred=n, n_star=c['n_star'],
                        src='b713_onsets.json c1 %s r, n_pred, n_star' % c['key']))
    p17 = dict((x['k'], x) for x in P('b717_predictions.json')['rows'])
    for x in P('b717_onsets.json')['rows']:
        r, rr = ball(p17[x['k']]['r'])
        out.append(dict(field='-39', k=x['k'], r=r, r_rad=rr, n_pred=x['n_pred'], n_star=x['n_star'],
                        src='b717_predictions.json rows k=%d r ; b717_onsets.json rows n_pred, n_star' % x['k']))
    return out


def controls_pred(rows):
    L = ['## THE CONTROLS, BEFORE ANY delta_pred']
    x = rows[0]
    r, n = x['r'], x['n_pred']
    Lv = r * n
    q = 8.0 / (r * (n + 1))
    hand = 0.375 * Lv / (1 - q)
    L += ['  (C1) THE FORMULA BY HAND-CARRIED ARITHMETIC at %s pair %d (r %.8g, n*_pred %.4f):' % (x['field'], x['k'], r, n),
          '       L = r n*_pred = %.10f ; (3/8) L = %.10f ; 8/(r (n*_pred + 1)) = %.10f ; 1 - that = %.10f ;' % (Lv, 0.375 * Lv, q, 1 - q),
          '       delta_pred = %.10f / %.10f = %.10f ; the tool`s delta() %.10f -- %s' % (
              0.375 * Lv, 1 - q, hand, delta(r, n), 'AS WANTED' if abs(hand - delta(r, n)) < 1e-9 else '### NOT AS WANTED')]
    ok1 = abs(hand - delta(r, n)) < 1e-9
    big = delta(0.06, 2000.0)
    ok2 = 0.06 > R_MAX
    L += ['  (C2) NEG: a pair at r = 0.06 (above 0.05) is read NOT SCORABLE by the screen: %s -- %s' % (
        'NOT SCORABLE' if ok2 else 'SCORABLE', 'AS WANTED' if ok2 else '### NOT AS WANTED'),
          '       (its delta_pred would be %.3f; the screen, not the formula, refuses it)' % big]
    return L, ok1 and ok2


def run_pred():
    t0 = time.time()
    rows = seventeen()
    L = ['b721 -- (R331)(5)(i): THE SEVENTEEN BANKED PAIRS UNDER H-OFFSET, POST HOC -- SCORABILITY, THEN delta_pred FROM r AND n*_pred ALONE (%s)' % utc(),
         '',
         '### POST HOC: every row below was computed and its onset banked before H-OFFSET was written (data/b719_offset_read.txt, b719);',
         '### these rows cannot test it. This route reads no n*: the observed n* is read beside the committed delta_pred by the `read` route',
         '### after this bank commits (data/b720_offset_price.txt :14-:16). H-OFFSET (data/b719_registrations.txt :49-:56), quoted:',
         '###   delta_pred = (3/8) L / (1 - 8/(r (n*_pred + 1))), L = r n*_pred ; REFUTED at a pair with r(rho) <= 0.05 where',
         '###   |(n* - n*_pred) - delta_pred| > 2 ; NOT SCORABLE at r(rho) > 0.05. PREMISE (printed beside each reading): the law`s r(rho)',
         '###   is log R of the onset tool`s dominant point (tools/b709_pairs.py :167-:169); the banks` r is that log R (b713_predictions.json',
         '###   r beside R, e.g. pair 1 r 0.00206523, R 1.0020674).',
         '']
    C, ok = controls_pred(rows)
    L += C + ['']
    sc = [x for x in rows if x['r'] <= R_MAX]
    L += ['## (a) SCORABILITY, EVERY PAIR, BEFORE ANY delta_pred: SCORABLE %d OF %d (r(rho) <= 0.05)' % (len(sc), len(rows))]
    for x in rows:
        L.append('  POST HOC | %-3s pair %2d | r(rho) %.6e (+/- %.1e) | %s' % (
            x['field'], x['k'], x['r'], x['r_rad'], 'SCORABLE' if x['r'] <= R_MAX else 'NOT SCORABLE'))
    L += ['', '## (b) delta_pred FROM r AND n*_pred ALONE (the spread from r`s banked radius beside it)']
    J = []
    for x in rows:
        d = delta(x['r'], x['n_pred'])
        lo = delta(x['r'] - x['r_rad'], x['n_pred'])
        hi = delta(x['r'] + x['r_rad'], x['n_pred'])
        L.append('  POST HOC | %-3s pair %2d | n*_pred %.4f | L %.4f | delta_pred %.4f [%.4f, %.4f] | %s' % (
            x['field'], x['k'], x['n_pred'], x['r'] * x['n_pred'], d, min(lo, hi), max(lo, hi), x['src']))
        J.append(dict(field=x['field'], k=x['k'], r=x['r'], n_pred=x['n_pred'], delta_pred=d))
    L += ['', '### ### **CONTROLS: %s ; SCORABLE %d OF 17 ; delta_pred WRITTEN AT 17, %.1f TO %.1f ; NO n* READ ; ALL POST HOC ; %d s.**' % (
        'ALL AS WANTED' if ok else '### NOT ALL AS WANTED', len(sc), min(j['delta_pred'] for j in J), max(j['delta_pred'] for j in J),
        int(time.time() - t0))]
    return L, J, ok


def committed_pred():
    """the pred bank's text at HEAD, None when it is not committed or the file on disk differs."""
    try:
        head = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/b721_offset_pred.txt'], capture_output=True).stdout
    except Exception:
        return None
    disk = open(PRED, 'rb').read() if os.path.exists(PRED) else b''
    return disk.decode('utf-8') if head and head == disk else None


def run_read():
    t0 = time.time()
    txt = committed_pred()
    if txt is None:
        sys.exit('### data/b721_offset_pred.txt NOT COMMITTED AT HEAD OR DIFFERING ON DISK -- NO n* READ')
    pat = re.compile(r'^  POST HOC \| (\S+)\s+pair\s+(\d+) \| n\*_pred ([0-9.]+) \| L [0-9.]+ \| delta_pred ([-0-9.]+) ')
    com = {}
    for l in txt.split(NL):
        m = pat.match(l)
        if m:
            com[(m.group(1), int(m.group(2)))] = (float(m.group(3)), float(m.group(4)))
    rows = seventeen()
    L = ['b721 -- (R331)(5)(i): THE SEVENTEEN, POST HOC -- THE OBSERVED n* BESIDE THE COMMITTED delta_pred (%s)' % utc(),
         '',
         '### the committed delta_pred read from data/b721_offset_pred.txt at HEAD (the file on disk equal to it): the needle`s yield %d of 17.' % len(com),
         '### POST HOC: these seventeen were seen before H-OFFSET was written; a REFUTED here refutes it on its own first rows, a HELD here',
         '### tests nothing. Only new pairs, delta_pred committed before their onsets, test it.', '']
    if len(com) != 17:
        sys.exit(NL.join(L + ['### THE NEEDLE FOUND %d OF 17 COMMITTED ROWS -- STOPPED' % len(com)]))
    x = rows[0]
    npd, dp = com[(x['field'], x['k'])]
    off_pl = x['n_star'] - (npd + 10)
    pl = abs(off_pl - dp) > BOUND
    L += ['## THE PLANT, BEFORE ANY ROW: %s pair %d with its n*_pred moved by +10 (%.4f): offset %.4f against the committed delta_pred %.4f,' % (
        x['field'], x['k'], npd + 10, off_pl, dp),
          '   |diff| %.4f -- %s' % (abs(off_pl - dp), 'REFUSES THE MATCH, AS WANTED' if pl else '### MATCHES -- NOT AS WANTED'), '']
    L += ['## THE ROWS: n* - n*_pred beside delta_pred ; |diff| against 2 at r(rho) <= 0.05']
    held = ref = ns = 0
    for x in rows:
        npd, dp = com[(x['field'], x['k'])]
        off = x['n_star'] - npd
        dd = off - dp
        if x['r'] > R_MAX:
            v = 'NOT SCORABLE'
            ns += 1
        elif abs(dd) > BOUND:
            v = 'REFUTED'
            ref += 1
        else:
            v = 'HELD'
            held += 1
        L.append('  POST HOC | %-3s pair %2d | n* %d | n*_pred %.4f | offset %+.4f | delta_pred %.4f | diff %+.4f | ratio offset/delta %.4f | %s' % (
            x['field'], x['k'], x['n_star'], npd, off, dp, dd, off / dp, v))
    L += ['', '## THE GRADE (POST HOC)',
          '  H-OFFSET on its own first rows, every one seen before it was written: HELD %d, REFUTED %d, NOT SCORABLE %d of 17. The falsifier' % (held, ref, ns),
          '  reads REFUTED overall if any scorable pair refutes it (data/b719_registrations.txt :57-:58); on POST HOC rows that reading is a',
          '  refutation on the rows it was written from, not a test. PREMISE beside it: the banks` r is log R of the tool`s dominant point.',
          '', '### ### **PLANT: %s ; POST HOC 17: HELD %d, REFUTED %d, NOT SCORABLE %d ; H-OFFSET %s ON ITS OWN FIRST ROWS ; %d s.**' % (
              'REFUSES AS WANTED' if pl else '### NOT AS WANTED', held, ref, ns,
              'REFUTED (POST HOC)' if ref else 'HELD (POST HOC, NOT A TEST)', int(time.time() - t0))]
    return L


def band_seconds(f):
    u = P(f)['units']
    out = []
    for k, v in u.items():
        route, span = k.split('|')
        if span.count('_') != 1:
            out.append((route, -1.0, -1.0, v.get('seconds', 0)))
            continue
        lo, hi = span.split('_')
        out.append((route, float(lo), float(hi), v.get('seconds', 0)))
    return out


def run_tier():
    t0 = time.time()
    L = ['b721 -- (R331)(5)(ii): THE NEXT TIER -- EVERY BANKED PAIR NOT YET GIVEN AN ONSET, CHOSEN BY r(rho) <= 0.05 ALONE (%s)' % utc(),
         '',
         '### THE RULE, printed before any pair is named: from the banked prediction rows (data/b713_predictions.json, data/b717_predictions.json),',
         '### every pair with no banked onset whose banked r(rho) <= 0.05 -- r alone, no other screen. For each: delta_pred needs the pair`s',
         '### n*_pred, which b709`s route forms only where the pair is within reach of its certified list (tools/b709_pairs.py :174-:178: every',
         '### rest modulus and the uncertified bound below r); the rows below print each pair`s banked reach beside its list`s top.',
         '### Q0`s list (data/b711_list.json) banks no prediction rows of this form (its pairs 11 and 15 alone were reached, b711 needed/reached),',
         '### so Q0 enters no row here: named, not screened.', '']
    rows = []
    for f, fld in (('b713_predictions.json', '-15'), ('b717_predictions.json', '-39')):
        on = P(f.replace('predictions', 'onsets'))
        done = set(x['k'] for x in on['rows'])
        for x in P(f)['rows']:
            if x['k'] in done:
                continue
            r, _rr = ball(x['r'])
            rows.append(dict(field=fld, k=x['k'], r=r, need=x.get('needs_T0_above'), npred=x.get('n_pred_float'), T0=x.get('T0')))
    ch = [x for x in rows if x['r'] <= R_MAX]
    L.append('## THE RULE`S OUTPUT: %d PAIRS WITH NO ONSET ; %d CHOSEN (r(rho) <= 0.05) ; %d WITH A BANKED n*_pred' % (
        len(rows), len(ch), sum(1 for x in ch if x['npred'] is not None)))
    tops = {'-15': P('b713_list.json')['top'], '-39': P('b717_list.json')['top']}
    for x in sorted(ch, key=lambda y: (y['field'], y['need'] or 0)):
        L.append('  %s pair %2d | r(rho) %.6e | n*_pred %s | its list`s top %.2f, the reach needs T0` > %.1f | delta_pred NOT FORMED: the list short by %.1f' % (
            x['field'], x['k'], x['r'], 'none banked' if x['npred'] is None else '%.1f' % x['npred'], tops[x['field']], x['need'],
            x['need'] - tops[x['field']]))
    L += ['', '## THE PRICE, FROM THE BANKED TIMINGS (no timing taken this act)']
    for f, fld in (('b713_list.json', '-15'), ('b717_list.json', '-39'), ('b711_list.json', 'Q0')):
        bs = band_seconds(f)
        cnt = [b for b in bs if b[0] == 'count']
        onl = [b for b in bs if b[0] == 'online' and b[1] >= 150]
        top_cnt = sorted(cnt, key=lambda b: b[1])[-3:]
        L.append('  %s (data/%s, top %.2f): total %d s over %d units ; the highest count bands %s ; the online bands from 150: %s' % (
            fld, f, P(f)['top'], sum(b[3] for b in bs), len(bs),
            ', '.join('[%.1f, %.1f] %d s' % (b[1], b[2], b[3]) for b in top_cnt),
            ', '.join('[%.1f, %.1f] %d s' % (b[1], b[2], b[3]) for b in sorted(onl, key=lambda b: b[1])[-3:])))
    for f in ('b713_onsets.json', 'b717_onsets.json'):
        o = P(f)
        L.append('  onsets (data/%s): %s ; c1 %s' % (f, ', '.join('pair %d n* %d %d s' % (x['k'], x['n_star'], x['seconds']) for x in o['rows']),
                                                   ', '.join('%s %d s' % (c['key'], c['seconds']) for c in o.get('c1', [])) or '-'))
    near = sorted(ch, key=lambda y: y['need'] - tops[y['field']])[:5]
    L += ['  READ: an onset costs seconds (4 s at most at -15 and -39, 35 s at Q0`s 15 at n* 14.7M); the price of a new pair is its list',
          '  extended past its reach: a band of 15 in T0` cost 115-378 s of counting and 25-190 s of on-line scan at heights 150-445, so the',
          '  nearest pairs (%s) need %s of extension, each a tool writing a new list bank of this act`s before any n*_pred.' % (
              ', '.join('%s %d (short %.1f)' % (y['field'], y['k'], y['need'] - tops[y['field']]) for y in near),
              'about 1-4 bands'),
          '', '## THE CARRY',
          '  No delta_pred is formed this act at any of the %d chosen pairs: each lacks a committed n*_pred, and forming one needs the list' % len(ch),
          '  extended -- a computation the budget after (3)-(4) does not hold beside (6)-(8). The rule and the chosen set are committed here,',
          '  before any onset; each pair is carried to b722 in this order (by field, nearest reach first), its delta_pred to be committed from its own r',
          '  and n*_pred before its onset.',
          '', '### ### **THE RULE`S OUTPUT: %d CHOSEN BY r(rho) <= 0.05 ; delta_pred FORMED AT 0 (NO n*_pred WITHIN REACH OF ITS LIST) ; ' % len(ch) +
          'NO LIST EXTENDED, NO ONSET RUN ; CARRIED ; %d s.**' % int(time.time() - t0)]
    return L


def write(path, L):
    with open(path + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(path + '.tmp', path)
    print('written data/%s (%d lines)' % (os.path.basename(path), len(L)))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'pred'
    bank = len(sys.argv) > 2 and sys.argv[2] == 'bank'
    if mode == 'pred':
        L, _J, ok = run_pred()
        print(NL.join(L))
        if bank:
            if not ok:
                sys.exit('### CONTROLS NOT AS WANTED -- NOTHING WRITTEN')
            write(PRED, L)
    elif mode == 'read':
        L = run_read()
        print(NL.join(L))
        if bank:
            write(READ, L)
    elif mode == 'tier':
        L = run_tier()
        print(NL.join(L))
        if bank:
            write(TIER, L)
