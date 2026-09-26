# -*- coding: utf-8 -*-
"""b548_record.py -- THE BENCH AT Q0 AND XI: THE REST-TERM INTERFERENCE AND THE FUNCTIONAL SWEPT IN WIDTH AND ORDER; THE FIELD
ENTRY`S SOURCES: THE RECORD, UNDER (R158).
### `python tools/b548_record.py reads | interference <a_lo> <a_hi> | interference_report | sweep <q|xi> <p> <a_lo> <a_hi> |
### sweep_report | field | findings | components | desk | trail`

### The cell is b521`s `cell_q(a, p)`, IMPORTED; the xi cell is b519`s xi branch on b521`s `PWindow(a, 'xi', p)`, line for line.
### Every cell appends to its bank as it completes. FINDINGS three appends; OPEN_TRAILS one. This file deletes nothing.
"""
import io, json, math, os, re, subprocess, sys, time
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b521_tail as B21
import b519_window as B19
import b514_window as B14
import b511_families as F
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
ORDERS = [3, 5, 7, 9, 11]
GRID = list(range(10, 61))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def jsonl(n):
    p = os.path.join(D, n)
    return [json.loads(l) for l in rd(p).split(NL) if l.strip()] if os.path.exists(p) else []


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def put_txt(n, lines):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def append_line(n, obj):
    with io.open(os.path.join(D, n), 'a', encoding='utf-8', newline=NL) as fh:
        fh.write(json.dumps(obj) + NL)


# ------------------------------------------------------------------------------ THE READS
def reads():
    L = ['b548 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    for p, a, z, what in [(os.path.join(T, 'b521_tail.py'), 44, 128, 'PWindow and cell_q -- the window and the cell, verbatim'),
                          (os.path.join(T, 'b519_window.py'), 185, 245, 'b519`s cell, the xi branch'),
                          (os.path.join(T, 'b511_families.py'), 36, 56, 'the banks'),
                          (os.path.join(T, 'b326_closure.py'), 116, 146, 'hhat_exact'),
                          (os.path.join(T, 'b522_reach.py'), 1, 55, 'b522`s run'),
                          (OT, 10173, 10178, '(R125)'), (OT, 10344, 10350, '(R131)'), (OT, 10388, 10394, 'b523`s verdict'),
                          (FIND, 5529, 5531, 'the detection-geometries entry'), (FIND, 5575, 5580, 'the field entry')]:
        t = rd(p).split(NL)
        L.append('### %s:%d-%d -- %s' % (os.path.relpath(p, ROOT if p.startswith(ROOT) else PP).replace(os.sep, '/'), a, z, what))
        L += ['  :%d %s' % (i + 1, t[i][:500]) for i in range(a - 1, min(z, len(t)))] + ['']
    W = B21.PWindow(34.0, 'q', 7)
    L += ['### the window at a = 34, p = 7, its own note: ' + W.order_note, '### the xi bank: tools/e16/zeta_ordinates.npy, first %d ordinates, last %.6f' % (len(F.GAM), F.GAM[-1]),
          '### the Q0 bank: %d on-line ordinates (last %.6f), %d off-line zeros' % (len(F.GQ), F.GQ[-1], len(F.OFFQ))]
    L += ['', '### relay data/b522_run_log.txt (the per-width cost)'] + ['  ' + l for l in rd(os.path.join(D, 'b522_run_log.txt')).split(NL) if l.strip()]
    put_txt('b548_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ THE CELLS
def cell_xi(a, p):
    """### b519`s xi branch (tools/b519_window.py cell, obj == 'xi'), line for line, on b521`s PWindow(a, 'xi', p)."""
    W = B21.PWindow(a, 'xi', p)
    kz = 'z'
    Hb, Hh, Hw = W.khat(F.U_BASE).real, W.khat(F.U_HALF).real, W.khat(F.U_WIDE).real
    A = F.arch(Hb, F.U_BASE, F.KER[kz + '_base'])
    Eu = abs(F.arch(Hh, F.U_HALF, F.KER[kz + '_half']) - A) + abs(F.arch(Hw, F.U_WIDE, F.KER[kz + '_wide']) - A)
    PR, PRabs = F.prime_channel_xi(W, B19.QL)
    PR2, _ = F.prime_channel_xi(W, B19.QH)
    G = F.GAM
    zt = 2.0 * W.khat(G).real
    Zon = float(np.sum(zt))
    ip = int(np.argmin(np.abs(G - B19.G0['xi'])))
    pair = float(zt[ip])
    Etail = B19.tail(W, float(G[-1]), 'xi')
    dk = np.abs(2.0 * (W.khat(G * (1 + F.DELTA_XI)).real - W.khat(G).real))
    P = float((W.khat(0.5j) + W.khat(-0.5j)).real)
    Z = Zon
    r = Z - (P - PR + A)
    Ek = abs(PR - PR2)
    Aabs = float(np.trapezoid(np.abs(Hb * F.KER[kz + '_base']), F.U_BASE) / (2.0 * math.pi))
    Eround = 4.0 * F.EPS * (float(np.sum(np.abs(zt))) + Aabs + PRabs) + float(np.sum(dk))
    B = Eu + Ek + Etail + Eround
    return dict(a=a, p=p, A=A, PR=PR, P=P, Z=Z, pair=pair, rest=Z - pair, h2=P - PR + A, r=r, B=B, Bprime=Eu + Ek + Eround, Eu=Eu, Ek=Ek,
                Etail=Etail, Eround=Eround, verified=bool(abs(r) <= B))


def classify(c):
    sign = 'NEGATIVE' if c['h2'] < -c['B'] else ('POSITIVE' if c['h2'] > c['B'] else 'UNDECIDED')
    reach = 'IN' if c['Etail'] <= c['Bprime'] else 'OUT'
    status = ('VERIFIED-EST' if reach == 'IN' else 'VERIFIED-EST-TAIL') if (c['verified'] and sign != 'UNDECIDED') else ('VERIFIED-EST' if c['verified'] else 'UNVERIFIED')
    return sign, reach, status


def slim(c):
    keys = ('a', 'p', 'A', 'PR', 'P', 'Z', 'pair', 'rest', 'h2', 'r', 'B', 'Bprime', 'Eu', 'Ek', 'Etail', 'Eround', 'verified')
    out = {k: (float(c[k]) if isinstance(c[k], (float, np.floating)) else c[k]) for k in keys}
    out['sign'], out['reach'], out['status'] = classify(out)
    return out


def sweep():
    obj, p, lo, hi = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    bank = 'b548_sweep_%s.jsonl' % obj
    done = {(c['p'], c['a']) for c in jsonl(bank)}
    t0 = time.time()
    for a in range(lo, hi + 1):
        if (p, float(a)) in done:
            print('  %s p=%d a=%d already banked' % (obj, p, a))
            continue
        c = slim(B21.cell_q(float(a), p) if obj == 'q' else cell_xi(float(a), p))
        c['object'] = obj
        c['seconds'] = round(time.time() - t0, 1)
        append_line(bank, c)
        print('[%s] %s p=%-2d a=%-3d h2 %+.6e B %.2e %-9s %-4s %s ; %.0f s' % (time.strftime('%H:%M:%S'), obj, p, a, c['h2'], c['B'], c['sign'],
                                                                          c['reach'], c['status'], time.time() - t0), flush=True)


# ------------------------------------------------------------------------------ COMPONENT 1: THE INTERFERENCE
def contributions(a, p=7):
    W = B21.PWindow(a, 'q', p)
    on = [(float(g), float(2.0 * W.khat(np.array([g])).real[0])) for g in F.GQ]
    off = []
    for b, gg in F.OFFQ:
        t = float(sum(W.khat(B14.gamma_of(r)).real for r in B14.images(b, gg)))
        off.append(((float(b), float(gg)), t))
    return on, off


def interference():
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    banked = {c['a']: c for c in jsonl('b522_cells.jsonl')}
    t0 = time.time()
    done = {c['a'] for c in jsonl('b548_interference.jsonl')}
    for a in range(lo, hi + 1):
        if float(a) in done:
            continue
        c = B21.cell_q(float(a), 7)
        on, off = contributions(float(a))
        pairkey = (float(B19.PAIR[0]), float(B19.PAIR[1]))
        pair_t = next(t for k, t in off if abs(k[0] - pairkey[0]) < 1e-12 and abs(k[1] - pairkey[1]) < 1e-9)
        rest_terms = [('on', g, t) for g, t in on] + [('off', k[1], t) for k, t in off if not (abs(k[0] - pairkey[0]) < 1e-12 and abs(k[1] - pairkey[1]) < 1e-9)]
        row = dict(a=float(a), h2=float(c['h2']), Z=float(c['Z']), pair=float(c['pair']), rest=float(c['rest']), B=float(c['B']), Eround=float(c['Eround']),
                   Etail=float(c['Etail']), r=float(c['r']), pair_check=float(pair_t), rest_check=float(sum(t for _, _, t in rest_terms)),
                   banked_h2=banked.get(float(a), {}).get('h2'), banked_pair=banked.get(float(a), {}).get('pair'),
                   terms=[[k, g, t] for k, g, t in rest_terms], seconds=round(time.time() - t0, 1))
        append_line('b548_interference.jsonl', row)
        print('[%s] a=%d h2 %+.6e banked %s pair %+.6e rest %+.6e ; %.0f s' % (time.strftime('%H:%M:%S'), a, row['h2'],
              ('%+.6e' % row['banked_h2']) if row['banked_h2'] is not None else 'NONE', row['pair'], row['rest'], time.time() - t0), flush=True)


def kstar(row):
    pos = sorted([t for _, _, t in row['terms'] if t > 0], reverse=True)
    excess = row['rest'] - abs(row['pair'])
    if excess <= 0:
        return 0, excess
    cum = 0.0
    for k, t in enumerate(pos, 1):
        cum += t
        if row['rest'] - cum - abs(row['pair']) <= 0:
            return k, excess
    return None, excess


def interference_report():
    rows = {r['a']: r for r in jsonl('b548_interference.jsonl')}
    L = ['b548 -- READING ONE: THE REST-TERM INTERFERENCE AT Q0, p = 7 (H1 of (R158)(2)); every row READING', '',
         '### (a)-(b) the recomputed quantity against b522, and the split. floor = E_round ((R125)(2)); B the full bound.',
         '  a    h2 (recomputed)     h2 (b522)          |diff|      floor(E_round)  match   pair              rest              pair+rest         B          sign']
    match = {}
    for a in sorted(rows):
        r = rows[a]
        d = abs(r['h2'] - r['banked_h2']) if r['banked_h2'] is not None else None
        match[a] = d is not None and d <= r['Eround']
        sign = 'NEG' if r['h2'] < -r['B'] else ('POS' if r['h2'] > r['B'] else 'UND')
        L.append('  %-4.0f %+.10e  %s  %s  %.3e       %-6s  %+.10e  %+.10e  %+.10e  %.2e  %s' % (
            a, r['h2'], ('%+.10e' % r['banked_h2']) if r['banked_h2'] is not None else 'NONE', ('%.3e' % d) if d is not None else '--',
            r['Eround'], 'YES' if match[a] else 'NO', r['pair'], r['rest'], r['pair'] + r['rest'], r['B'], sign))
    L += ['', '### (c) the rest`s contributors at 36-38, the ten largest by magnitude (a contributor: one on-line ordinate or one off-line orbit)']
    ks = {}
    for a in (36.0, 37.0, 38.0):
        r = rows.get(a)
        if not r:
            continue
        top = sorted(r['terms'], key=lambda x: -abs(x[2]))[:10]
        k, ex = kstar(r)
        ks[a] = k
        L.append('  a = %.0f : pair %+.6e ; rest %+.6e ; excess (rest - |pair|) %+.6e ; k* = %s' % (a, r['pair'], r['rest'], ex, k))
        L += ['      %-3s ordinate %12.6f  contribution %+.6e' % (kind, g, t) for kind, g, t in top]
    # ### the peak test: each of the k* contributors larger at 36-38 than at 34-35 and 39-41
    peak = {}
    for a in (36.0, 37.0, 38.0):
        r = rows.get(a)
        k = ks.get(a)
        if not r or not k:
            continue
        pos = sorted([x for x in r['terms'] if x[2] > 0], key=lambda x: -x[2])[:k]
        ok = True
        for kind, g, t in pos:
            for b in (34.0, 35.0, 39.0, 40.0, 41.0):
                if b in rows:
                    tb = next((x[2] for x in rows[b]['terms'] if x[0] == kind and abs(x[1] - g) < 1e-9), None)
                    if tb is not None and tb >= t:
                        ok = False
        peak[a] = ok
    pr = {a: rows[a]['pair'] for a in sorted(rows)}
    c1 = all(rows[a]['rest'] > 0 and rows[a]['rest'] > abs(rows[a]['pair']) for a in (36.0, 37.0, 38.0) if a in rows)
    c1b = all(not (rows[a]['rest'] > abs(rows[a]['pair'])) for a in (34.0, 35.0, 39.0, 40.0, 41.0) if a in rows)
    c2 = all(ks.get(a) is not None and ks[a] <= 5 for a in (36.0, 37.0, 38.0))
    c3 = all(peak.get(a, False) for a in (36.0, 37.0, 38.0))
    ref1 = len(set(np.sign([pr[a] for a in (36.0, 37.0, 38.0) if a in pr]))) > 1 or any(pr[a] > 0 for a in (36.0, 37.0, 38.0) if a in pr)
    ref3 = not all(match.get(a, False) for a in (36.0, 37.0, 38.0))
    L += ['', '### (d) H1, clause by clause',
          '  H1.1  at 36-38 the rest is positive and exceeds |pair|                      : %s' % ('HOLDS' if c1 else 'FAILS'),
          '  H1.2  at 34-35 and 39-41 the rest does not exceed |pair|                    : %s' % ('HOLDS' if c1b else 'FAILS'),
          '  H1.3  the excess at 36-38 carried by at most five zeros (k* <= 5)           : %s  (k* %s)' % ('HOLDS' if c2 else 'FAILS', ks),
          '  H1.4  those zeros` contributions peak at 36-38 (above 34-35 and 39-41)      : %s  (%s)' % ('HOLDS' if c3 else 'FAILS', peak),
          '  REFUTER 1  the pair changes sign (or is positive) in 36-38                  : %s' % ('FIRES' if ref1 else 'does not fire'),
          '  REFUTER 2  the excess spread over more than five zeros, none dominant       : %s' % ('FIRES' if not c2 else 'does not fire'),
          '  REFUTER 3  pair + rest fails to reproduce the banked quantity to the floor  : %s' % ('FIRES' if ref3 else 'does not fire'),
          '  ### H1 %s' % ('HOLDS' if (c1 and c1b and c2 and c3 and not ref1 and not ref3) else 'IS REFUTED OR FAILS IN PART, AS THE ROWS SAY')]
    # ### the swing, printed beside the scored clauses (READING; it scores nothing): the contributors whose values move most across 34-41
    ws = [b for b in (34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0) if b in rows]
    keyed = {}
    for b in ws:
        for kind, g, t in rows[b]['terms']:
            keyed.setdefault((kind, round(g, 6)), {})[b] = t
    movers = sorted(keyed.items(), key=lambda kv: -(max(kv[1].values()) - min(kv[1].values())))[:6]
    L += ['', '### the swing across 34-41 (READING, printed beside the clauses; it scores nothing): the six contributors that move most',
          '  kind ordinate     ' + ''.join('%11.0f' % b for b in ws)]
    L += ['  %-4s %11.6f ' % (k[0], k[1]) + ''.join('%+11.3f' % v.get(b, float('nan')) for b in ws) for k, v in movers]
    L += ['  the rest       ' + ''.join('%+11.3f' % rows[b]['rest'] for b in ws), '  the pair       ' + ''.join('%+11.3f' % rows[b]['pair'] for b in ws),
          '  ### a caveat on H1.3, printed with it: the excess at 36-38 is 4-7 % of the rest, below the largest single contributor, so '
          'k* = 1 follows from the excess being small, not from one zero carrying it.']
    res = dict(match=match, kstar=ks, peak=peak, pair_sign=pr, movers=[[list(k), v] for k, v in movers], H1=dict(c1=c1, c1b=c1b, c2=c2, c3=c3, ref1=ref1, ref2=not c2, ref3=ref3),
               all_match=all(match.values()) and len(match) == 16)
    put_json('b548_interference.json', res)
    put_txt('b548_interference.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 2: THE SWEEP, REPORTED
def monotone(v):
    d = np.diff(v)
    return bool(np.all(d >= 0) or np.all(d <= 0))


def sweep_report():
    res = {}
    for obj, name, title in (('xi', 'b548_sweep_xi', 'XI (the chain bank, 10,000 ordinates)'), ('q', 'b548_sweep_q0', 'Q0 (the 180-zero bank with its tail estimate)')):
        R = {(c['p'], c['a']): c for c in jsonl('b548_sweep_%s.jsonl' % obj)}
        L = ['b548 -- READING TWO: F(a, n) = P - PR + A AT %s, n in {3, 5, 7, 9, 11}, a = 10..60; every row READING' % title, '',
             '### a cell: VERIFIED-EST iff |r| <= B; NEGATIVE iff F < -B, POSITIVE iff F > B, else UNDECIDED; floor = E_round ((R125)(2));',
             '### reach IN iff E_tail <= B` ((R131)(2)); status VERIFIED-EST-TAIL when decided outside the reach. dF/da = F(a+1) - F(a).', '']
        per = {}
        for p in ORDERS:
            S = [R[(p, float(a))] for a in GRID if (p, float(a)) in R]
            F_ = np.array([c['h2'] for c in S])
            A_ = np.array([c['a'] for c in S])
            dF = np.diff(F_)
            ch = [int(A_[i + 1]) for i in range(len(dF) - 1) if np.sign(dF[i]) != np.sign(dF[i + 1])]
            L += ['### n = %d : %d cells' % (p, len(S)),
                  '  a    F                  dF/da          B          floor      r/B       sign       reach status']
            for i, c in enumerate(S):
                L.append('  %-4.0f %+.10e  %s  %.2e   %.2e   %7.3f   %-9s  %-4s  %s' % (
                    c['a'], c['h2'], ('%+.6e' % dF[i]) if i < len(dF) else '     --     ', c['B'], c['Eround'], abs(c['r']) / c['B'], c['sign'], c['reach'], c['status']))
            neg = [c for c in S if c['sign'] == 'NEGATIVE']
            below_floor = [c for c in S if c['h2'] < -c['Eround']]
            imin = int(np.argmin(F_))
            beyond20 = F_[A_ >= 20]
            st = {}
            for c in S:
                st[c['status']] = st.get(c['status'], 0) + 1
            per[p] = dict(n=len(S), argmin=float(A_[imin]), fmin=float(F_[imin]), min_at_largest=bool(imin == len(F_) - 1), monotone_beyond_20=monotone(beyond20),
                          negative=[c['a'] for c in neg], below_floor=[c['a'] for c in below_floor], smallest_negative=(neg[0]['a'] if neg else None),
                          smallest_negative_in_reach=next((c['a'] for c in neg if c['reach'] == 'IN'), None), dF_sign_changes=ch,
                          status=st, undecided=[c['a'] for c in S if c['sign'] == 'UNDECIDED'], rB_max=float(max(abs(c['r']) / c['B'] for c in S)))
            L += ['  ### n = %d : min F %+.6e at a = %.0f ; at the largest a %s ; monotone beyond a = 20 %s ; NEGATIVE cells %d ; F < -floor at %d cells'
                  % (p, per[p]['fmin'], per[p]['argmin'], 'YES' if per[p]['min_at_largest'] else 'NO', 'YES' if per[p]['monotone_beyond_20'] else 'NO', len(neg), len(below_floor)),
                  '  ### n = %d : smallest NEGATIVE width %s (in reach %s) ; statuses %s ; max |r|/B %.3f' % (p, per[p]['smallest_negative'], per[p]['smallest_negative_in_reach'], st, per[p]['rB_max']),
                  '  ### n = %d : dF/da sign changes at a = %s (READING; no stationary point is called a finding)' % (p, ch), '']
        res[obj] = per
        if obj == 'xi':
            L += ['### the xi table`s own caveat: at n = 3 every cell is UNVERIFIED -- |r| exceeds B by a factor %.3f to %.3f, r positive throughout,'
                  % (min(abs(R[(3, float(a))]['r']) / R[(3, float(a))]['B'] for a in GRID), per[3]['rB_max']),
                  '### and B is led by E_u (the arch quadrature`s half/wide comparison): the order-3 transform decays as u^-3 and the comparison',
                  '### underprices the quadrature error. The sign is not in doubt (least F / |r| over n = 3 is %.1e) but the cells are not VERIFIED-EST.'
                  % min(R[(3, float(a))]['h2'] / abs(R[(3, float(a))]['r']) for a in GRID)]
        put_txt(name + '.txt', L)
    xi, q = res['xi'], res['q']
    # ### H2, clause by clause
    x1 = all(not xi[p]['below_floor'] for p in ORDERS)
    x1v = all(not xi[p]['negative'] for p in ORDERS)
    x2 = {p: xi[p]['min_at_largest'] or xi[p]['monotone_beyond_20'] for p in ORDERS}
    q1 = {p: bool(q[p]['negative']) for p in (7, 9, 11)}
    sn = [q[p]['smallest_negative'] for p in ORDERS]
    sn7 = [q[p]['smallest_negative'] for p in (7, 9, 11)]
    q2 = all(sn7[i] is not None and sn7[i + 1] is not None and sn7[i + 1] < sn7[i] for i in range(2))
    q3 = {p: bool(q[p]['negative']) for p in (3, 5)}
    L = ['b548 -- H2 OF (R158)(3), CLAUSE BY CLAUSE (every row READING)', '',
         '  H2.xi.1  at xi, F >= 0 at every cell above its floor (no F < -E_round), every n      : %s  (F < -floor at %s ; NEGATIVE %s)'
         % ('HOLDS' if x1 else 'FAILS', {p: len(xi[p]['below_floor']) for p in ORDERS}, {p: len(xi[p]['negative']) for p in ORDERS}),
         '  H2.xi.2  at xi, min over a at the largest a, or monotone beyond a = 20, per n         : %s  (%s)'
         % ('HOLDS' if all(x2.values()) else 'FAILS', ' ; '.join('n=%d min at a=%.0f, largest %s, monotone %s' % (p, xi[p]['argmin'], xi[p]['min_at_largest'], xi[p]['monotone_beyond_20']) for p in ORDERS)),
         '  H2.q.1   at Q0, for each n >= 7 the minimum over a is negative beyond its floor         : %s  (%s)'
         % ('HOLDS' if all(q1.values()) else 'FAILS', ' ; '.join('n=%d min %+.3f at a=%.0f' % (p, q[p]['fmin'], q[p]['argmin']) for p in (7, 9, 11))),
         '  H2.q.2   at Q0, the smallest negative width decreases as n increases (n = 7, 9, 11)     : %s  (smallest NEGATIVE width per n %s)'
         % ('HOLDS' if q2 else 'FAILS', dict(zip(ORDERS, sn))),
         '  REFUTER 1  xi shows a negative cell above its floor                                  : %s' % ('does not fire' if x1 else 'FIRES'),
         '  REFUTER 2  Q0`s smallest negative width does not decrease with n                    : %s' % ('does not fire' if q2 else 'FIRES'),
         '  REFUTER 3  n = 3 or 5 shows negativity at Q0                                        : %s  (NEGATIVE cells n=3 %d, n=5 %d ; statuses n=3 %s, n=5 %s)'
         % ('FIRES' if any(q3.values()) else 'does not fire', len(q[3]['negative']), len(q[5]['negative']), q[3]['status'], q[5]['status']),
         '  ### H2 %s' % ('HOLDS' if (x1 and all(x2.values()) and all(q1.values()) and q2 and not any(q3.values())) else 'IS REFUTED, AS THE ROWS SAY'),
         '',
         '  ### Q0`s smallest NEGATIVE width per n : ' + ' ; '.join('n=%d a=%s (in reach %s)' % (p, q[p]['smallest_negative'], q[p]['smallest_negative_in_reach']) for p in ORDERS),
         '  ### caveat printed with REFUTER 3: every Q0 cell at n = 3 and 5 lies outside the reach (E_tail > B`), so their NEGATIVE signs are',
         '  ### decided under the tail ESTIMATE (VERIFIED-EST-TAIL), as b522`s order-7 cells beyond a = 34 were before b523 priced them.',
         '  ### caveat printed with H2.xi.1: at n = 3 xi`s cells are UNVERIFIED (|r| > B by at most %.3f x); positive beyond B at all 51.' % xi[3]['rB_max']]
    H2 = dict(x1=x1, x1_negative_none=x1v, x2=x2, q1=q1, q2=q2, q3=q3, ref1=not x1, ref2=not q2, ref3=any(q3.values()), smallest_negative=dict(zip(map(str, ORDERS), sn)))
    put_txt('b548_h2.txt', L)
    put_json('b548_sweep.json', dict(xi={str(k): v for k, v in xi.items()}, q={str(k): v for k, v in q.items()}, H2=H2))
    print(NL.join(L))


# ------------------------------------------------------------------------------ THE APPENDS
def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def append_to(path, text):
    text = poss(text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, h):
    if poss(h).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


def hline(path, h):
    return rd(path).split(NL).index(poss(h)) + 1


FIELDH = ('## The field entry`s sources, repaired: Zhu`s abstract quoted, the Liu record`s provenance, the two Zenodo records completed '
          '(to FINDINGS.md:5575)')
ACTH = '## The bench at Q0 and ξ: the rest-term interference at widths 36–38 and the functional swept in width and order'
PTR = '*Appended at b548 to the detection-geometries entry (`FINDINGS.md`:5529):'
HEADING = ('### b548 — the bench under (R158): the rest-term interference at Q0 (H1) and the functional swept in width and order at Q0 '
           'and ξ (H2); the field entry`s sources repaired')


def field():
    guard_absent(FIND, FIELDH)
    fs = jl('b548_field_sources.json')
    z, li, zn = fs['zhu'], fs['liu'], fs['zenodo']
    L = ['', FIELDH, '',
         '*Filed at b548 on the author`s ruling `(R158)`(4), appended to the field entry at `FINDINGS.md`:5575 (whose text is unchanged). '
         'Field-context layer (R157)(1). Bank: relay `data/b548_field_sources.json`.*', '',
         '**The peer-venue reference for the restricted-window line, heading the entry.** %s, *"%s"*, arXiv:2608.24827 (%s; %s). '
         'Its claim sentence, verbatim from the abstract: **"%s"** Its scope sentence, verbatim: **"%s"** The abstract opens: "%s" '
         '(Fetched 2026-09-26 as the fetch tool rendered the abstract page; not checked against the PDF.)'
         % (z['author'], z['title'], z['url'], z['dates'], z['claim_sentence'], z['scope_sentence'], z['first_sentence']), '',
         '**The Liu preprint the navigator read.** %s (given there as %s, "%s", submitted %s). **NAVIGATOR-READ** at that URL: the '
         'identifier is not an arXiv number and the venue hosts non-arXiv preprints, so the record carries no more weight than the '
         'navigator`s reading of it; the seat did not fetch it. This corrects the entry at :5575, whose search by the title the ruling '
         'then gave found no record.' % (li['url'], li['author'], li['affiliation'], li['submitted']), '',
         '**The two Zenodo records, completed from their public metadata pages** (title, author, date; read without the token; nothing '
         'written): %s.' % '; '.join('record %s, %s, *"%s"*, %s' % (r['record'], r['author'], r['title'], r['date']) for r in zn) +
         ' Neither is engaged beyond these three fields.', '',
         '*Nothing deposits; nothing at Zenodo written; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = hline(FIND, FIELDH)
    put_json('b548_field.json', out)
    print('  FINDINGS field :%d %s' % (out['heading_line'], out))


def findings():
    guard_absent(FIND, ACTH)
    ij, sj, fd = jl('b548_interference.json'), jl('b548_sweep.json'), jl('b548_field.json')
    rows = {r['a']: r for r in jsonl('b548_interference.jsonl')}
    H1, H2 = ij['H1'], sj['H2']
    xi, q = sj['xi'], sj['q']
    hd = lambda v: 'HOLDS' if v else 'FAILS'
    fr = lambda v: 'FIRES' if v else 'does not fire'
    sn = H2['smallest_negative']
    L = ['', ACTH, '',
         '*Filed at b548 on the author`s ruling `(R158)`. Graded READING throughout: readings of the benches, not theorems. Banks: relay '
         '`data/b548_interference.txt`, `data/b548_sweep_q0.txt`, `data/b548_sweep_xi.txt`, `data/b548_h2.txt`, `data/b548_sweep.json` '
         '(cells in `data/b548_sweep_q.jsonl`, `data/b548_sweep_xi.jsonl`). The family is b522`s: `tools/b521_tail.py` `PWindow(a, obj, p)`, '
         'an indicator of [−W, W] convolved with the order-p B-spline, its transform in closed form; the Q0 bank is the 180-zero bank '
         'below 150 with its tail estimate, the ξ bank the first 10,000 ordinates. A cell is NEGATIVE iff F < −B, POSITIVE iff F > B; '
         'VERIFIED-EST iff |r| ≤ B; the floor is E_round ((R125)(2)); the reach is E_tail ≤ B′ ((R131)(2)). '
         '**Nothing about ζ’s zeros is claimed.**', '',
         '**Reading one: the rest-term interference at Q0, order 7 (H1).** Recomputed at widths 30–45, the quantity matches b522`s bank '
         'with difference 0 at all 16 widths. The pair term (the orbit of the off-line zero at γ₀ = 16.290216) is negative at every '
         'width, −387.6 at a = 30 to −444.1 at a = 45; the rest is positive throughout. At 36, 37, 38 the rest (%+.1f, %+.1f, %+.1f) exceeds '
         '|pair| (%.1f, %.1f, %.1f); at 34–35 and 39–41 it does not. The excess is 4–7 %% of the rest, so removing its largest '
         'contributor clears it (k* = 1 at each width) -- a consequence of the excess being small, not of one zero carrying it. The '
         'contributor that swings most across 34–41 is the off-line zero at t = 29.551761 (σ = 0.798): −44.8, −21.1, +17.6, +53.7, +74.0, '
         '+73.0, +53.4, +23.3 at a = 34…41.'
         % (rows[36.0]['rest'], rows[37.0]['rest'], rows[38.0]['rest'], abs(rows[36.0]['pair']), abs(rows[37.0]['pair']), abs(rows[38.0]['pair'])), '',
         '| H1 clause | reading | score |', '|:--|:--|:--|',
         '| H1.1 | at 36–38 the rest is positive and exceeds the pair`s magnitude | %s |' % hd(H1['c1']),
         '| H1.2 | at 34–35 and 39–41 it does not | %s |' % hd(H1['c1b']),
         '| H1.3 | the excess at 36–38 is carried by at most five zeros | %s (k* = 1, 1, 1) |' % hd(H1['c2']),
         '| H1.4 | those zeros’ transforms peak at 36–38 | %s (at %s) |' % (hd(H1['c3']), ', '.join('%.0f' % float(a) for a, v in ij['peak'].items() if not v) or 'none'),
         '| refuter | the pair changes sign in 36–38 | %s |' % fr(H1['ref1']),
         '| refuter | the excess is spread over more than five zeros, none dominant | %s |' % fr(H1['ref2']),
         '| refuter | pair and rest fail to reproduce the bank to the floor | %s |' % fr(H1['ref3']), '',
         '**H1 is not refuted; its peak clause fails at two of the three widths.**', '',
         '**Reading two: F(a, n) = P − PR + A swept for n ∈ {3, 5, 7, 9, 11}, a = 10…60 (H2).** 255 cells at each object. At ξ every cell is '
         'POSITIVE beyond its bound; the cells are VERIFIED-EST at n = 5, 7, 9, 11, and UNVERIFIED at n = 3, where |r| exceeds B by a '
         'factor 1.12–1.17 (B is led by the arch quadrature`s estimate, which the order-3 transform`s slow decay outruns). At every order '
         'the minimum over a at ξ is at a = 38 (n = 3: %+.3f; n = 11: %+.2f) -- the width at which Q0`s positive interval 36–38 closes. At Q0 '
         'the smallest NEGATIVE width is %s at n = 3, 5, 7, 9, 11; every Q0 cell at n = 3 and 5 is outside the reach (VERIFIED-EST-TAIL, '
         'decided under the tail estimate), the n = 7 cells below a = 28 likewise, and n = 11 is in reach at all 51. The finite differences '
         'dF/da change sign at a list printed per n in the banks; no stationary point is called a finding.'
         % (xi['3']['fmin'], xi['11']['fmin'], ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11'))), '',
         '| H2 clause | reading | score |', '|:--|:--|:--|',
         '| ξ.1 | F ≥ 0 at every cell above its floor, every n | %s (no cell below −E_round) |' % hd(H2['x1']),
         '| ξ.2 | the minimum over a is at the largest a, or F is monotone beyond a = 20 | %s (minimum at a = 38 for every n) |' % hd(all(H2['x2'].values())),
         '| Q0.1 | for n ≥ 7 the minimum over a is negative beyond its floor | %s (%s) |' % (hd(all(H2['q1'].values())), '; '.join(
             'n = %s: %+.1f at a = %.0f' % (k, q[k]['fmin'], q[k]['argmin']) for k in ('7', '9', '11'))),
         '| Q0.2 | the smallest negative width decreases with n | %s (26, 26, 42 at n = 7, 9, 11) |' % hd(H2['q2']),
         '| refuter | ξ shows a negative cell above its floor | %s |' % fr(H2['ref1']),
         '| refuter | Q0`s smallest negative width does not decrease with n | %s |' % fr(H2['ref2']),
         '| refuter | n = 3 or 5 shows negativity at Q0 | %s (%d and %d NEGATIVE cells, all VERIFIED-EST-TAIL) |' % (fr(H2['ref3']), len(q['3']['negative']), len(q['5']['negative'])), '',
         '**H2 is refuted by two of its refuters.** On this bank the order-7 threshold is not an artefact-free feature of order 7: the lower '
         'orders go negative at smaller widths, under the tail estimate; the highest order computed goes negative latest. The route`s '
         'prediction that a higher order detects at a smaller base width is not borne out on this family at these widths.', '',
         '**The field entry`s sources**, repaired at `FINDINGS.md`:%d (Zhu quoted; Liu NAVIGATOR-READ with provenance; the two Zenodo '
         'records completed). **Next keystone:** THE_RESIDUE_OF_RH.' % fd['heading_line'], '',
         '*Nothing deposits; nothing at Zenodo written; no kernel edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = hline(FIND, ACTH)
    guard_absent(FIND, PTR)
    ptr = (PTR + ' its bench is the sweep of the act at `FINDINGS.md`:%d (relay `data/b548_sweep_q0.txt`, `data/b548_sweep_xi.txt`) -- '
           'F(a, n) at Q0 and ξ for n ∈ {3, 5, 7, 9, 11}, a = 10…60; the smallest negative width at Q0 is %s at n = 3, 5, 7, 9, 11, so on '
           'this family the width at which the Weil side detects does not fall with the order. READING.*'
           % (out['heading_line'], ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11'))))
    out2 = append_to(FIND, NL.join(['', ptr, '']))
    out2['line'] = [i + 1 for i, l in enumerate(rd(FIND).split(NL)) if l.startswith(poss(PTR))][0]
    put_json('b548_findings.json', dict(write=out, pointer=out2))
    print('  FINDINGS act :%d ; pointer :%d' % (out['heading_line'], out2['line']))


PRIOR_PP = '2549901'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md'}
MEMDIR = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'memory')


def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    ij, sj = jl('b548_interference.json'), jl('b548_sweep.json')
    rows = jsonl('b548_interference.jsonl')
    H2 = sj.get('H2', {})
    committed = gitc(PP, 'log', '-1', '--pretty=%s').startswith('b548 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in gitc(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in gitc(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b548_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b548_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == ''
               for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section')}
    fin = rd(FIND)
    fs = jl('b548_field_sources.json')
    q = sj.get('q', {})
    sn = H2.get('smallest_negative', {})
    n4 = (sn.get('7') is not None and sn.get('9') is not None and sn.get('11') is not None and sn['11'] < sn['9'] < sn['7']
          and not q.get('3', {}).get('negative') and not q.get('5', {}).get('negative'))
    return dict(
        n1=bool(ij.get('all_match')),
        n2=bool(ij.get('H1', {}).get('c1')) and bool(ij.get('H1', {}).get('c2')),
        n3=all(not v['negative'] for v in sj.get('xi', {}).values()) and len(sj.get('xi', {})) == 5,
        n4=bool(n4),
        n5=fs.get('zhu', {}).get('claim_sentence', '@@') in fin and fs.get('zhu', {}).get('scope_sentence', '@@') in fin
        and fs.get('liu', {}).get('url', '@@') in fin and 'NAVIGATOR-READ' in fin,
        n6=all(pref.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= WRITE_OK,
        prefixes=pref, written=written, zen=zen, token=tok, kernels=kernels,
        s1=len(rows) == 16 and all(r['banked_h2'] is not None and r['h2'] == r['banked_h2'] for r in rows),
        s2=all(r['pair'] < 0 < r['rest'] for r in rows if r['a'] in (36.0, 37.0, 38.0)) and any((v or 0) > 5 for v in ij.get('kstar', {}).values()),
        s3=not q.get('3', {}).get('negative'))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    sj = jl('b548_sweep.json')
    sn = sj['H2']['smallest_negative']
    L = ['=' * 104, 'b548 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- the order-7 recomputation against b522 at 30-45: difference 0 at all 16 (relay data/b548_interference.txt).' % w(sc['n1']),
         '  **(N2)** ### **%s.** -- at 36-38 the rest exceeds |pair| with the opposite sign; k* = 1 at each (the excess is 4-7 %% of the rest).' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- xi NEGATIVE cells: none at any order; n = 3`s cells UNVERIFIED (|r|/B up to %.3f) but positive beyond B.'
         % (w(sc['n3']), sj['xi']['3']['rB_max']),
         '  **(N4)** ### **%s.** -- Q0 smallest NEGATIVE width %s at n = 3, 5, 7, 9, 11; n = 3 and 5 NEGATIVE at %d and %d cells (VERIFIED-EST-TAIL).'
         % (w(sc['n4']), ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11')), len(sj['q']['3']['negative']), len(sj['q']['5']['negative'])),
         '  **(N5)** ### **%s.** -- Zhu`s claim and scope sentences quoted verbatim in FINDINGS; the alphaXiv URL recorded NAVIGATOR-READ with its provenance.' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- prefixes kept %s ; files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n6']), sc['prefixes'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the difference is exactly 0 at every width 30-45.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- the pair negative and the rest positive at 36-38, but k* = 1 at all three, not above five.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- Q0 at p = 3 is NEGATIVE from a = 24 (37 cells), under the tail estimate.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b548_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b548_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b548_desk_notes.txt', L)
    put_json('b548_scores.json', sc)
    print(NL.join(L))


def components():
    q = jsonl('b548_sweep_q.jsonl')
    x = jsonl('b548_sweep_xi.jsonl')
    L = ['=' * 132, 'b548 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### THE COST, ESTIMATED BEFORE RUNNING (the face, READING (6)): about 950 s per object and order, about 9,500 s for the sweep.',
         '### THE CELLS BANKED : Q0 %d ; xi %d ; Component 1 %d' % (len(q), len(x), len(jsonl('b548_interference.jsonl'))),
         '### THE CALLS : every sweep call foreground and under 600 s; the per-cell cumulative seconds are in each jsonl row (`seconds`).', '']
    L += ['### COMPONENT 1 -- data/b548_interference.txt'] + ['  ' + l for l in rd(os.path.join(D, 'b548_interference.txt')).rstrip(NL).split(NL)[-30:]]
    L += ['', '### COMPONENT 2 -- data/b548_h2.txt'] + ['  ' + l for l in rd(os.path.join(D, 'b548_h2.txt')).rstrip(NL).split(NL)]
    for n in ('b548_field.json', 'b548_findings.json', 'b548_field_sources.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['### THE BRANCHES : see data/b548_branches.txt', '=' * 132]
    put_txt('b548_components.txt', L)
    print(NL.join(L[:8]))


def trail():
    sc, fdj, fnd = scores(), jl('b548_field.json'), jl('b548_findings.json')
    sj = jl('b548_sweep.json')
    sn = sj['H2']['smallest_negative']
    body = ['', HEADING, '',
            '**(R158) ratified.** (1) A bench act, graded READING throughout, on b522`s window family and the Q0 and ξ banks. (2) Reading '
            'one, H1 fixed before computation: the rest-term interference at Q0, order 7, widths 36–38. (3) Reading two, H2 fixed before '
            'computation: F(a, n) = P − PR + A swept for n ∈ {3, 5, 7, 9, 11}, a = 10…60, at ξ and at Q0, with ∂F/∂a banked. (4) The field '
            'entry`s sources repaired: Zhu`s abstract quoted, the alphaXiv record NAVIGATOR-READ, the two Zenodo records completed from '
            'their public metadata. (5) THE_RESIDUE_OF_RH next.', '',
            '**Entered:** FINDINGS.md:%d (the sources), :%d (the act, READING), :%d (the pointer from :5529).'
            % (fdj['heading_line'], fnd['write']['heading_line'], fnd['pointer']['line']), '',
            '**H1:** not refuted -- the recomputation matches b522 with difference 0 at 30–45; at 36–38 the rest exceeds |pair| and k* = 1; '
            'the peak clause fails at 36 and 37. **H2:** refuted -- ξ has no negative cell (order 3`s cells UNVERIFIED, positive beyond B), '
            'the ξ minimum sits at a = 38 at every order; Q0`s smallest negative width is %s at n = 3, 5, 7, 9, 11, and orders 3 and 5 are '
            'negative under the tail estimate.' % ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11')), '',
            '**CP-1:** open; the cascade continues with THE_RESIDUE_OF_RH.', '',
            '**Next:** THE_RESIDUE_OF_RH.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**The numerical lane opened for this act and shuts at its close; no kernel lane.** Nothing deposits; nothing at Zenodo written; '
            'no kernel edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit '
            'left it; the four lists stay OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b548_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'interference': interference, 'interference_report': interference_report, 'sweep': sweep, 'sweep_report': sweep_report,
          'field': field, 'findings': findings, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
