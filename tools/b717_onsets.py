# -*- coding: utf-8 -*-
"""b717_onsets.py -- THE ONSETS AT -39, (R327)(4)(iii): "the onsets, each ratio to six places within the window [0.99, 1.01], each falsifier
HELD or REFUTED, and the additive offset onset - prediction beside each ratio", after data/b717_predictions.txt is committed alone (relay
f47d8ab5). The law, its falsifier and its controls: data/b716_registrations.txt (iii) :60-:80, read unchanged from dc5e808f.

### UNTRACKED WRITE: data/b717_onsets_units* -- data/b717_onsets_units.jsonl, one unit per (route, key), appended, resumable (b709's form).

### CARRIED FROM tools/b713_onsets.py (read through the Read tool :1-:200, :200-:269) by the Write tool: the act's names b713 -> b717, the
### list and predictions tools b717's (the engine at sqrt(39), Q1's list of -39, data/b717_list.json, T0' 200), PRED_COMMIT f47d8ab5.
### THE ROUTE UNCHANGED: tools/b709_pairs.py's constants_for709 IMPORTED UNEDITED, its onset resumable per call (budget 400 s, b711's), on
### b709's configuration (every on-line zero of the list and the one pair, dom = ref<k>), each pair's cap from the predictions bank.
### THE CONTROLS, CHANGED FROM b713's WHERE REGISTRATION (iii) NAMES ITS OWN (:76-:79), BOTH BEFORE ANY -39 ONSET:
### (C1) `c1` -- in a process of its own that imports tools/b713_list.py and tools/b713_predict.py and NOT tools/b717_list.py (b667's engine
###      carried to sqrt(15), b713's list data/b713_list.json, read only), the route recomputes -15's eight pairs with b713's caps
###      (data/b713_predictions.json), each n* against b713's (data/b713_onsets.json) and each ratio n*/n*_pred to six places against b713's;
###      a NEG beside it (the law with its 4 log(4C) term struck) wanted OUTSIDE the window. constants_for709 writes no unit.
### (C2) `c2` -- the identity of (i) (data/b716_genus_control.txt): r_Q1(n) by direct enumeration read equal to the three lines' through
###      the act's coefficient cut 32532 ((R327)(4)(iv)) -- the trivial line r_Q1 + r_Q3 + 2 r_Q2 = 2 sum chi_-39(d), the genus line
###      r_Q1 + r_Q3 - 2 r_Q2 = 2 sum chi_-3(d) chi_13(n/d), r_Q2 = r_Q2', and the quartic pair's a(n) = (r_Q1 - r_Q3)/2 on the Hecke laws --
###      by b716's functions imported unedited (counts, kronecker, reduced_forms, hecke_laws), the divisor sums by a sieve (b716's
###      divisors() is quadratic at the cut). THE SEAT'S READING of "the route's input": the onset route reads Q1 through the engine and its
###      list, not through r_Q1; the identity is read at the act's one coefficient cut, the cut b717_coeffs.py's route takes.
### THE RESIDUAL, an observation and not a falsifier (:78-:79): the additive offset n* - n*_pred printed beside each ratio with b714's -15 and
### Q0 offsets (data/b714_residual.txt :16-:25, 44.9 to 137.3, positive at 10 of 10).
### THE ORDER ((N2)): the bank prints whether the predictions commit is an ancestor of HEAD, its commit time, the first -39 onset unit's time,
### and whether the predictions bank's blobs at that commit equal the files.
### Routes: `c1` ; `c2` ; `pair <k>` (k with a prediction; refused before c1 and c2 are banked as wanted or while the predictions bank
### differs from f47d8ab5's) ; `status` ; `bank [dry]` -> data/b717_onsets.txt, data/b717_onsets.json. Written by the Write tool at b717.
"""
import hashlib
import io
import json
import math
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b717'
UNITS = os.path.join(D, '%s_onsets_units.jsonl' % ACT)
PRED_COMMIT = 'f47d8ab5'
WINDOW = (0.99, 1.01)
BUDGET = 400
CUT = 32532                         # ### (R327)(4)(iv): the coefficients through cut 32532
RESIDUAL_B714 = ((-15, 1, 45.1081), (-15, 2, 44.9145), (-15, 3, 58.6552), (-15, 4, 70.2544), (-15, 5, 65.2456), (-15, 6, 64.2773),
                 (-15, 7, 64.7637), (-15, 8, 137.3047), ('Q0', 11, 59.4338), ('Q0', 15, 60.6945))   # ### data/b714_residual.txt :16-:25


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _membrane(p):
    import act_membrane as MEM
    import b717_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['key'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    _membrane(UNITS)
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def law(C, r, strike=False):
    from flint import arb, ctx
    ctx.prec = 256
    a = arb(0) if strike else 4 * (4 * C).log()
    n = (a if not strike else arb(8)) / r
    for _ in range(300):
        n2 = (a + 8 * (n + 1).log()) / r
        if abs(n2 - n) < arb('1e-30'):
            return n2
        n = n2
    return n


def _mid(s):
    from flint import arb
    return float(arb(s.strip('[]').split(' +/-')[0]))


# ================================================================================ (C1) AT -15, IN ITS OWN PROCESS
def _b713():
    pj = json.load(io.open(os.path.join(D, 'b713_predictions.json'), encoding='utf-8'))
    oj = json.load(io.open(os.path.join(D, 'b713_onsets.json'), encoding='utf-8'))
    return pj, dict((r['k'], r) for r in oj['rows'])


def c1(*a):
    if 'b717_list' in sys.modules:
        sys.exit('### tools/b717_list.py IS IMPORTED IN THIS PROCESS -- (C1) RUNS ON b713`S ENGINE AT sqrt(15) ALONE -- NOTHING RUN')
    import b713_list as L13
    import b713_predict as PR13
    P9 = L13.P9
    B, P5 = P9.B, P9.P5
    pj, ob = _b713()
    U = units()
    T0p, on, pairs, _j = PR13.list_rows()
    t_call = time.time()
    for k in sorted(ob):
        pr = [r for r in pj['rows'] if r['k'] == k][0]
        key = ('c1', '-15:%d@%d' % (k, T0p))
        u = U.get(key) or dict(route='c1', key=key[1], k=k, T0=T0p, cap=pr['cap'], n_start=1, done=False, seconds=0)
        if not u.get('done'):
            if time.time() - t_call > 300 and u['n_start'] == 1:
                print('### THE CALL`S BUDGET REACHED BEFORE -15 PAIR %d -- call again' % k)
                return
            _k, off, ref = [p for p in pairs if p[0] == k][0]
            t0 = time.time()
            c = P9.constants_for709(B.terms(on + [off, ref]), 'ref%d' % k, T0p, pr['cap'], n_start=u['n_start'], budget=BUDGET)
            r = P5.r_of(off[1], off[2])
            u.update(seconds=u['seconds'] + int(time.time() - t0), r=r.str(30, radius=True), C=c.get('C'))
            if c['done']:
                u.update(done=True, n_star=c['n_star'])
                C = P9._arb(c['C'])
                u['n_pred'] = law(C, r).str(20, radius=True)
                u['n_pred_struck'] = law(C, r, strike=True).str(20, radius=True)
            else:
                u['n_start'] = c['n_last']
            put_unit(u)
            if not u['done']:
                print('    (C1) -15 pair %d: PARTIAL at n = %d ; %d s -- call again' % (k, u['n_start'], u['seconds']), flush=True)
                return
        print('    ' + _c1_line(u, pr, ob[k]), flush=True)


def _c1_line(u, pr, o):
    np_, ns_ = _mid(u['n_pred']), _mid(u['n_pred_struck'])
    q = u['n_star'] / pr['n_pred_float']
    return '(C1) -15 pair %d: n* %d (b713`s %d, EQUAL %s) ; ratio %.6f (b713`s %.6f, EQUAL %s) ; the law`s n*_pred from the onset call`s C ball, its printed midpoint, %.1f (b713`s committed %.1f, the ratio`s) ; NEG (4 log 4C struck) ratio %.6f %s ; %d s' % (
        u['k'], u['n_star'], o['n_star'], u['n_star'] == o['n_star'], q, o['ratio'], '%.6f' % q == '%.6f' % o['ratio'], np_, pr['n_pred_float'],
        u['n_star'] / ns_, 'OUTSIDE as wanted' if not (WINDOW[0] <= u['n_star'] / ns_ <= WINDOW[1]) else '### WITHIN, NOT AS WANTED', u['seconds'])


def _c1_ok(U):
    pj, ob = _b713()
    out = []
    for k, o in ob.items():
        u = [v for (r_, k_), v in U.items() if r_ == 'c1' and v.get('k') == k]
        out.append(bool(u and u[-1].get('done') and u[-1].get('n_star') == o['n_star']))
    return len(out) == 8 and all(out)


# ================================================================================ (C2) THE IDENTITY OF (i) THROUGH THE CUT
def _sieve_line(chi_d, chi_nd, n_max):
    """2 sum_{d | n} chi_d(d) chi_nd(n/d) for 1 <= n <= n_max by a sieve over d."""
    s = [0] * (n_max + 1)
    cd = [0] + [chi_d(d) for d in range(1, n_max + 1)]
    cn = [0] + [chi_nd(e) for e in range(1, n_max + 1)]
    for d in range(1, n_max + 1):
        if cd[d] == 0:
            continue
        for e in range(1, n_max // d + 1):
            s[d * e] += cd[d] * cn[e]
    return [2 * x for x in s]


def c2(*a):
    import b716_genus_control as G
    t0 = time.time()
    G.DISC = -39
    F = G.reduced_forms(-39)
    r1, r2, r2i, r3 = (G.counts(f, CUT) for f in ((1, 1, 10), (2, 1, 5), (2, -1, 5), (3, 3, 4)))
    triv = _sieve_line(lambda d: G.kronecker(-39, d), lambda e: 1, CUT)
    gen = _sieve_line(lambda d: G.kronecker(-3, d), lambda e: G.kronecker(13, e), CUT)
    miss_t = [n for n in range(1, CUT + 1) if r1[n] + r3[n] + 2 * r2[n] != triv[n]]
    miss_g = [n for n in range(1, CUT + 1) if r1[n] + r3[n] - 2 * r2[n] != gen[n]]
    miss_i = [n for n in range(1, CUT + 1) if r2[n] != r2i[n] or (r1[n] - r3[n]) % 2]
    aq = [0] + [(r1[n] - r3[n]) // 2 for n in range(1, CUT + 1)]
    bad_mult, bad_rec = G.hecke_laws(aq, CUT)
    # ### the sieve against b716's own quadratic divisor sums through 400 (b716's N), and the NEG: Q0 = (1, 1, 6) in Q1's place
    r1_400 = G.counts((1, 1, 10), 400)
    sieve_eq = all(triv[n] == 2 * sum(G.kronecker(-39, d) for d in G.divisors(n)) for n in range(1, 401)) and \
        all(gen[n] == 2 * sum(G.kronecker(-3, d) * G.kronecker(13, n // d) for d in G.divisors(n)) for n in range(1, 401))
    r0 = G.counts((1, 1, 6), 400)
    neg = [n for n in range(1, 401) if r0[n] + r3[n] + 2 * r2[n] != triv[n]]
    ok = (F == [(1, 1, 10), (2, -1, 5), (2, 1, 5), (3, 3, 4)] and not miss_t and not miss_g and not miss_i and not bad_mult and not bad_rec
          and sieve_eq and len(neg) > 0 and r1_400 == r1[:401])
    u = dict(route='c2', key='identity@%d' % CUT, done=True, ok=ok, forms=F, miss_trivial=miss_t[:20], miss_genus=miss_g[:20],
             miss_inverse_parity=miss_i[:20], hecke_mult_off=len(bad_mult), hecke_rec_off=len(bad_rec), sieve_eq_400=sieve_eq,
             neg_q0_misses_400=len(neg), r_Q1_sum=sum(r1), seconds=int(time.time() - t0))
    put_unit(u)
    print('    ' + _c2_line(u))


def _c2_line(u):
    return '(C2) the identity of (i) through n = %d: forms %s ; trivial line misses %d ; genus line misses %d ; r_Q2 = r_Q2` and parity off %d ; Hecke laws off %d coprime, %d prime powers ; the sieve equal to b716`s divisor sums through 400 %s ; NEG (Q0 in Q1`s place) misses %d through 400 %s ; %s ; %d s' % (
        CUT, u['forms'], len(u['miss_trivial']), len(u['miss_genus']), len(u['miss_inverse_parity']), u['hecke_mult_off'], u['hecke_rec_off'],
        u['sieve_eq_400'], u['neg_q0_misses_400'], 'FAILING as wanted' if u['neg_q0_misses_400'] else '### NOT FAILING', 'AS WANTED' if u['ok'] else '### NOT AS WANTED', u['seconds'])


def _c2_ok(U):
    u = U.get(('c2', 'identity@%d' % CUT))
    return bool(u and u.get('ok'))


# ================================================================================ THE -39 PAIRS
def _pred_unchanged():
    """the predictions bank's blobs at f47d8ab5 equal to the files now."""
    ok = True
    for n in ('%s_predictions.txt' % ACT, '%s_predictions.json' % ACT):
        a = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:data/%s' % (PRED_COMMIT, n)], capture_output=True, text=True).stdout.strip()
        b = subprocess.run(['git', '-C', ROOT, 'hash-object', 'data/%s' % n], capture_output=True, text=True).stdout.strip()
        ok = ok and bool(a) and a == b
    return ok


def pair(k, *a):
    k = int(k)
    U = units()
    if not _c1_ok(U) or not _c2_ok(U):
        sys.exit('### (C1) AND (C2) ARE NOT BOTH BANKED AS WANTED -- THE CONTROLS BEFORE THE FIGURES -- NOTHING RUN')
    if not _pred_unchanged():
        sys.exit('### THE PREDICTIONS BANK IS NOT f47d8ab5`S -- NOTHING RUN')
    if 'b713_list' in sys.modules:
        sys.exit('### tools/b713_list.py IS IMPORTED IN THIS PROCESS -- NOTHING RUN')
    import b717_list as LST
    import b717_predict as PR
    P9 = LST.P9
    B = P9.B
    pj = json.load(io.open(os.path.join(D, '%s_predictions.json' % ACT), encoding='utf-8'))
    pr = [r for r in pj['rows'] if r['k'] == k][0]
    if pr.get('reach'):
        sys.exit('### PAIR %d IS BEYOND REACH AT T0` %d (the predictions bank) -- NOTHING RUN' % (k, pj['T0']))
    LST._free('THE ONSET OF PAIR %d' % k)
    key = ('pair', '%d@%d' % (k, pj['T0']))
    u = U.get(key) or dict(route='pair', key=key[1], k=k, T0=pj['T0'], cap=pr['cap'], n_start=1, done=False, seconds=0)
    if not u.get('done'):
        T0p, on, pairs, _j = PR.list_rows()
        _k, off, ref = [p for p in pairs if p[0] == k][0]
        t0 = time.time()
        c = P9.constants_for709(B.terms(on + [off, ref]), 'ref%d' % k, T0p, pr['cap'], n_start=u['n_start'], budget=BUDGET)
        u.update(seconds=u['seconds'] + int(time.time() - t0), C=c.get('C'), R=c.get('R'), s=c.get('s'))
        if c['done']:
            u.update(done=True, n_star=c['n_star'], expr=c.get('expr_at_n_star'), reach=c.get('reach'))
        else:
            u['n_start'] = c['n_last']
        put_unit(u)
    if not u['done']:
        print('  pair %d: PARTIAL at n = %d ; %d s -- call again' % (k, u['n_start'], u['seconds']))
        return
    _pair_print(u, pr)


def _verdict(u, pr):
    if not u.get('n_star'):
        return None, 'NO ONSET BELOW THE CAP %d' % u['cap']
    q = u['n_star'] / pr['n_pred_float']
    return q, ('HELD' if WINDOW[0] <= q <= WINDOW[1] else 'REFUTED')


def _pair_print(u, pr):
    q, v = _verdict(u, pr)
    print('  pair %d: n* %s ; n*_pred %.1f ; ratio %s ; offset n* - n*_pred %s ; C at the onset %s (the prediction`s %s, EQUAL %s) ; %s ; %d s' % (
        u['k'], u.get('n_star'), pr['n_pred_float'], '%.6f' % q if q else '-', '%.4f' % (u['n_star'] - pr['n_pred_float']) if u.get('n_star') else '-',
        (u.get('C') or '')[:16], pr['C'][:16], u.get('C') == pr['C'], v, u['seconds']))


def status(*a):
    U = units()
    for (r, k), u in sorted(U.items()):
        print('  %s %s: done %s ; n* %s ; n_start %s ; %d s' % (r, k, u.get('done'), u.get('n_star'), u.get('n_start'), u.get('seconds', 0)))


def _git(*args):
    return subprocess.run(['git', '-C', ROOT] + list(args), capture_output=True, text=True)


def bank(*a):
    U = units()
    pj = json.load(io.open(os.path.join(D, '%s_predictions.json' % ACT), encoding='utf-8'))
    p13, ob = _b713()
    pc = _git('show', '-s', '--format=%H %cI', PRED_COMMIT).stdout.strip()
    anc = _git('merge-base', '--is-ancestor', PRED_COMMIT, 'HEAD').returncode == 0
    head = _git('rev-parse', 'HEAD').stdout.strip()
    first = min([u['at'] for u in U.values() if u['route'] == 'pair'] or ['none'])
    pc_utc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(_git('show', '-s', '--format=%ct', PRED_COMMIT).stdout.strip() or 0)))
    L = ['%s -- (R327)(4)(iii): THE ONSETS AT -39 AGAINST THE PREDICTIONS COMMITTED BEFORE THEM, EACH RATIO TO SIX PLACES, THE OFFSET BESIDE (%s)' % (ACT, utc()), '',
         '### THE ORDER, BY ANCESTRY: the predictions committed alone at %s (%s UTC) ; an ancestor of HEAD %s: %s ; the first -39 onset' % (pc, pc_utc, head[:8], anc),
         '### unit at %s, after the commit: %s ; the predictions bank`s blobs at %s equal to the files: %s.' % (first, first > pc_utc, PRED_COMMIT, _pred_unchanged()),
         '### THE ROUTE: b709`s constants_for709 imported unedited, on b709`s configuration over Q1`s list (data/b717_list.txt, the counts certified',
         '### and the off-line points located, T0` %d); the window [0.99, 1.01] of n*_pred (data/b716_registrations.txt :74); the falsifier a computed' % pj['T0'],
         '### pair outside it (:75). THE OFFSET n* - n*_pred beside each ratio, an observation and not a falsifier (:78-:79).', '',
         '### THE CONTROLS, BEFORE ANY -39 ONSET (:76-:78):']
    c1_rows = sorted((v for (r_, k_), v in U.items() if r_ == 'c1'), key=lambda v: v['k'])
    for u in c1_rows:
        pr13 = [r for r in p13['rows'] if r['k'] == u['k']][0]
        L.append('  ' + (_c1_line(u, pr13, ob[u['k']]) if u.get('done') else '(C1) -15 pair %d: ### NOT DONE' % u['k']))
    L.append('  (C1) %s: %d of 8 -15 pairs reproduced at b713`s n* (their first unit at %s)' % (
        'AS WANTED' if _c1_ok(U) else '### NOT AS WANTED', sum(1 for u in c1_rows if u.get('done') and u.get('n_star') == ob[u['k']]['n_star']),
        min([u['at'] for u in c1_rows] or ['none'])))
    u2 = U.get(('c2', 'identity@%d' % CUT))
    L.append('  ' + (_c2_line(u2) + ' (at %s)' % u2['at'] if u2 else '(C2) ### NOT RUN'))
    L += ['', '### THE -39 PAIRS:']
    held = ref = 0
    rows = []
    for pr in pj['rows']:
        if pr.get('reach'):
            L.append('  pair %2d | rho %s + %s i | beyond reach at %d: the rule needs T0` > %.1f | not computed' % (
                pr['k'], pr['re'].strip('[]').split(' ')[0][:10], pr['im'].strip('[]').split(' ')[0][:12], pj['T0'], pr['needs_T0_above'] or float('nan')))
            continue
        u = U.get(('pair', '%d@%d' % (pr['k'], pj['T0']))) or {}
        if not u.get('done'):
            L.append('  pair %2d | ### NOT COMPUTED' % pr['k'])
            continue
        q, v = _verdict(u, pr)
        held += v == 'HELD'
        ref += v == 'REFUTED'
        off = (u['n_star'] - pr['n_pred_float']) if u.get('n_star') else None
        rows.append(dict(k=pr['k'], n_star=u.get('n_star'), n_pred=pr['n_pred_float'], ratio=q, offset=off, verdict=v, C_equal=u.get('C') == pr['C'],
                         seconds=u['seconds']))
        L.append('  pair %2d | rho %s + %s i | n* %s | n*_pred %.1f | ratio %s | offset %s | %s' % (
            pr['k'], pr['re'].strip('[]').split(' ')[0][:10], pr['im'].strip('[]').split(' ')[0][:12], u.get('n_star'), pr['n_pred_float'],
            '%.6f' % q if q else '-', '%+.4f' % off if off is not None else '-', v))
    offs = [r['offset'] for r in rows if r['offset'] is not None]
    L += ['', '### THE RESIDUAL BESIDE IT (b714`s, data/b714_residual.txt :16-:25): ' + ' ; '.join('%s pair %d %+.1f' % x for x in RESIDUAL_B714),
          '### the -39 offsets: %s ; positive at %d of %d.' % ('%+.1f to %+.1f' % (min(offs), max(offs)) if offs else 'none', sum(1 for o in offs if o > 0), len(offs)),
          '', '### ### **PAIRS COMPUTED %d ; HELD %d ; REFUTED %d ; BEYOND REACH AT %d: %d ; THE DETECTION LAW %s AT %d OF %d PAIRS ; THE PREDICTIONS BEFORE THE ONSETS BY ANCESTRY %s.**' % (
              len(rows), held, ref, pj['T0'], sum(1 for p in pj['rows'] if p.get('reach')), 'MET' if rows and not ref else 'REFUTED', held, len(rows),
              anc and first > pc_utc)]
    print(NL.join(L))
    if 'dry' in a:
        return
    for name, data in (('%s_onsets.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                       ('%s_onsets.json' % ACT, (json.dumps(dict(at=utc(), pred_commit=pc, ancestor=anc, first_onset=first, rows=rows, held=held, refuted=ref,
                                                                   c1=c1_rows, c2=u2), indent=1) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        _membrane(p)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(p + '.tmp', p)
        print('  %s  data/%s' % (hashlib.sha256(data).hexdigest(), name))


ROUTES = dict(c1=c1, c2=c2, pair=pair, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b717_onsets.py c1 | c2 | pair <k> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
