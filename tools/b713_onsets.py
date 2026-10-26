# -*- coding: utf-8 -*-
"""b713_onsets.py -- THE ONSETS AT -15, (R323)(5)(iii): "the onsets, each ratio to six places, each falsifier HELD or REFUTED (window
[0.99, 1.01])", after data/b713_predictions.txt is committed alone (relay be4db146). The law and its falsifier: data/b712_registrations.txt (ii)
:41-:48, read unchanged.

### UNTRACKED WRITE: data/b713_onsets_units* -- data/b713_onsets_units.jsonl, one unit per (route, key), appended, resumable (b709's form).

### THE ROUTE: tools/b709_pairs.py's constants_for709 IMPORTED UNEDITED, its onset resumable per call (budget 400 s, b711's), on b709's
### configuration (every on-line zero of the list and the one pair, dom = ref<k>) -- at -15 through tools/b713_list.py (the engine at sqrt(15),
### Q1's list, data/b713_list.json) with T0' 199 and each pair's cap from the predictions bank (1.25 x n*_pred).
### THE CONTROL BEFORE ANY -15 ONSET (registration (ii) (C1), :49): `c1` -- in a process of its own that imports tools/b711_list.py and NOT
### tools/b713_list.py (b667's engine at sqrt(23), b709's and b711's Q0 units, read only), the route recomputes Q0's pairs 11 and 15 on b711's
### list at T0' 415 and 445 with b711's caps, each n* against b711's (data/b711_pairs.txt :12-:13: 12275906, 14748557) and each ratio n*/F2
### against b711's (0.998460, 0.998079); beside them the registered law's own n*_pred (C from the same call) and n*/n*_pred, and a NEG control
### (the law with its 4 log(4C) term struck) wanted OUTSIDE the window. Nothing of b711's is written: constants_for709 writes no unit; this tool
### writes only its own units file and banks.
### Routes: `c1` ; `pair <k>` (k with a prediction; refused before c1 is banked or while the predictions bank differs from be4db146's) ;
### `status` ; `bank [dry]` -> data/b713_onsets.txt, data/b713_onsets.json. Written by the Write tool at b713.
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

ACT = 'b713'
UNITS = os.path.join(D, '%s_onsets_units.jsonl' % ACT)
PRED_COMMIT = 'be4db146'
WINDOW = (0.99, 1.01)
BUDGET = 400
Q0 = {11: dict(T0=415, cap=15368546, n=12275906, F2=12294837.0, ratio='0.998460'),
      15: dict(T0=445, cap=18471175, n=14748557, F2=14776939.6, ratio='0.998079')}   # ### data/b711_pairs.txt :12-:13 ; data/b710_registrations.txt :40


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _membrane(p):
    import act_membrane as MEM
    import b713_record as REC
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


# ================================================================================ (C1) AT Q0, IN ITS OWN PROCESS
def c1(*a):
    if 'b713_list' in sys.modules:
        sys.exit('### tools/b713_list.py IS IMPORTED IN THIS PROCESS -- (C1) RUNS ON b667`S ENGINE AT sqrt(23) ALONE -- NOTHING RUN')
    import b711_list as L11
    P9 = L11.P9
    B, P5 = P9.B, P9.P5
    U = units()
    R0 = B.reps()
    t_call = time.time()
    for idx, q in Q0.items():
        key = ('c1', '%d@%d' % (idx, q['T0']))
        u = U.get(key) or dict(route='c1', key=key[1], idx=idx, T0=q['T0'], cap=q['cap'], n_start=1, done=False, seconds=0)
        if not u.get('done'):
            if time.time() - t_call > 60 and u['n_start'] == 1:
                print('### THE CALL`S BUDGET REACHED BEFORE PAIR %d -- call again' % idx)
                return
            rows_all, _a, _b = P9.extended_rows(L11.units(), q['T0'])
            rows = [x for x in rows_all if x[0].startswith('on') or x[0] in ('off%d' % idx, 'ref%d' % idx)]
            t0 = time.time()
            c = P9.constants_for709(B.terms(rows), 'ref%d' % idx, q['T0'], q['cap'], n_start=u['n_start'], budget=BUDGET)
            off = [x for x in R0 if x[0] == 'off%d' % idx][0]
            r = P5.r_of(off[1], off[2])
            u.update(seconds=u['seconds'] + int(time.time() - t0), r=r.str(30, radius=True), C=c.get('C'), points=2 * len(rows))
            if c['done']:
                u.update(done=True, n_star=c['n_star'])
                C = P9._arb(c['C'])
                u['n_pred'] = law(C, r).str(20, radius=True)
                u['n_pred_struck'] = law(C, r, strike=True).str(20, radius=True)
            else:
                u['n_start'] = c['n_last']
            put_unit(u)
            if not u['done']:
                print('    (C1) pair %d at T0` %d: PARTIAL at n = %d ; %d s -- call again' % (idx, q['T0'], u['n_start'], u['seconds']), flush=True)
                return
        _c1_print(u, q)


def _c1_print(u, q):
    from flint import arb
    np_ = float(arb(u['n_pred'].strip('[]').split(' +/-')[0]))
    ns_ = float(arb(u['n_pred_struck'].strip('[]').split(' +/-')[0]))
    rf2 = u['n_star'] / q['F2']
    print('    (C1) Q0 pair %d at T0` %d: n* %s (b711`s %d, EQUAL %s) ; n*/F2 %.6f (b711`s %s, EQUAL %s) ; the law`s n*_pred %.1f, ratio %.6f ; NEG (4 log 4C struck) %.1f, ratio %.6f %s ; %d s' % (
        u['idx'], u['T0'], u['n_star'], q['n'], u['n_star'] == q['n'], rf2, q['ratio'], '%.6f' % rf2 == q['ratio'], np_, u['n_star'] / np_, ns_, u['n_star'] / ns_,
        'OUTSIDE as wanted' if not (WINDOW[0] <= u['n_star'] / ns_ <= WINDOW[1]) else '### WITHIN, NOT AS WANTED', u['seconds']), flush=True)


def _c1_ok(U):
    out = []
    for idx, q in Q0.items():
        u = U.get(('c1', '%d@%d' % (idx, q['T0'])))
        out.append(bool(u and u.get('done') and u.get('n_star') == q['n']))
    return all(out)


# ================================================================================ THE -15 PAIRS
def _pred_unchanged():
    """the predictions bank's blobs at be4db146 equal to the files now."""
    ok = True
    for n in ('%s_predictions.txt' % ACT, '%s_predictions.json' % ACT):
        a = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:data/%s' % (PRED_COMMIT, n)], capture_output=True, text=True).stdout.strip()
        b = subprocess.run(['git', '-C', ROOT, 'hash-object', 'data/%s' % n], capture_output=True, text=True).stdout.strip()
        ok = ok and bool(a) and a == b
    return ok


def pair(k, *a):
    k = int(k)
    U = units()
    if not _c1_ok(U):
        sys.exit('### (C1) IS NOT BANKED AS WANTED -- THE CONTROL BEFORE THE FIGURES -- NOTHING RUN')
    if not _pred_unchanged():
        sys.exit('### THE PREDICTIONS BANK IS NOT be4db146`S -- NOTHING RUN')
    import b713_list as LST
    import b713_predict as PR
    P9 = LST.P9
    B, P5 = P9.B, P9.P5
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
    print('  pair %d: n* %s ; n*_pred %.1f ; ratio %s ; C at the onset %s (the prediction`s %s, EQUAL %s) ; %s ; %d s' % (
        u['k'], u.get('n_star'), pr['n_pred_float'], '%.6f' % q if q else '-', (u.get('C') or '')[:16], pr['C'][:16], u.get('C') == pr['C'], v, u['seconds']))


def status(*a):
    U = units()
    for (r, k), u in sorted(U.items()):
        print('  %s %s: done %s ; n* %s ; n_start %s ; %d s' % (r, k, u.get('done'), u.get('n_star'), u.get('n_start'), u.get('seconds', 0)))


def bank(*a):
    U = units()
    pj = json.load(io.open(os.path.join(D, '%s_predictions.json' % ACT), encoding='utf-8'))
    pc = subprocess.run(['git', '-C', ROOT, 'show', '-s', '--format=%H %cI', PRED_COMMIT], capture_output=True, text=True).stdout.strip()
    first = min([u['at'] for u in U.values() if u['route'] == 'pair'] or ['none'])
    L = ['%s -- (R323)(5)(iii): THE ONSETS AT -15 AGAINST THE PREDICTIONS COMMITTED BEFORE THEM, EACH RATIO TO SIX PLACES (%s)' % (ACT, utc()), '',
         '### THE ORDER: the predictions committed alone at %s ; the first -15 onset unit at %s ; the predictions bank unchanged since: %s.' % (
             pc, first, _pred_unchanged()),
         '### THE ROUTE: b709`s constants_for709 imported unedited, on b709`s configuration over Q1`s list (data/b713_list.txt, T0` %d); the' % pj['T0'],
         '### window [0.99, 1.01] of n*_pred (data/b712_registrations.txt :46); the falsifier a computed pair outside it (:48).', '',
         '### (C1), BEFORE ANY -15 ONSET (b667`s engine at sqrt(23), b711`s list, its own process):']
    for idx, q in Q0.items():
        u = U.get(('c1', '%d@%d' % (idx, q['T0']))) or {}
        if u.get('done'):
            from flint import arb
            np_ = float(arb(u['n_pred'].strip('[]').split(' +/-')[0]))
            ns_ = float(arb(u['n_pred_struck'].strip('[]').split(' +/-')[0]))
            L.append('  Q0 pair %d at T0` %d: n* %d (b711`s %d, EQUAL %s) ; n*/F2 %.6f (b711`s %s) ; the law`s n*_pred %.1f, ratio %.6f ; NEG (4 log 4C struck) ratio %.6f %s' % (
                idx, q['T0'], u['n_star'], q['n'], u['n_star'] == q['n'], u['n_star'] / q['F2'], q['ratio'], np_, u['n_star'] / np_, u['n_star'] / ns_,
                'OUTSIDE as wanted' if not (WINDOW[0] <= u['n_star'] / ns_ <= WINDOW[1]) else '### WITHIN'))
        else:
            L.append('  Q0 pair %d: ### NOT BANKED' % idx)
    L += ['', '### THE -15 PAIRS:']
    held = ref = 0
    rows = []
    for pr in pj['rows']:
        if pr.get('reach'):
            L.append('  pair %2d | BEYOND REACH at T0` %d (needs > %.1f) | not computed' % (pr['k'], pj['T0'], pr['needs_T0_above'] or float('nan')))
            continue
        u = U.get(('pair', '%d@%d' % (pr['k'], pj['T0']))) or {}
        if not u.get('done'):
            L.append('  pair %2d | ### NOT COMPUTED' % pr['k'])
            continue
        q, v = _verdict(u, pr)
        held += v == 'HELD'
        ref += v == 'REFUTED'
        rows.append(dict(k=pr['k'], n_star=u.get('n_star'), n_pred=pr['n_pred_float'], ratio=q, verdict=v, C_equal=u.get('C') == pr['C'], seconds=u['seconds']))
        L.append('  pair %2d | rho %s + %s i | n* %s | n*_pred %.1f | ratio %s | %s' % (
            pr['k'], pr['re'].strip('[]').split(' ')[0][:10], pr['im'].strip('[]').split(' ')[0][:12], u.get('n_star'), pr['n_pred_float'],
            '%.6f' % q if q else '-', v))
    L += ['', '### ### **PAIRS COMPUTED %d ; HELD %d ; REFUTED %d ; BEYOND REACH %d ; THE LAW %s AT %d OF %d PAIRS.**' % (
        len(rows), held, ref, sum(1 for p in pj['rows'] if p.get('reach')), 'MET' if rows and not ref else 'REFUTED', held, len(rows))]
    print(NL.join(L))
    if 'dry' in a:
        return
    for name, data in (('%s_onsets.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                       ('%s_onsets.json' % ACT, (json.dumps(dict(at=utc(), pred_commit=pc, first_onset=first, rows=rows, held=held, refuted=ref,
                                                                   c1=[U.get(('c1', '%d@%d' % (i, q['T0']))) for i, q in Q0.items()]), indent=1) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        _membrane(p)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(p + '.tmp', p)
        print('  %s  data/%s' % (hashlib.sha256(data).hexdigest(), name))


ROUTES = dict(c1=c1, pair=pair, status=status, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b713_onsets.py c1 | pair <k> | status | bank [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
