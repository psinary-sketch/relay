# -*- coding: utf-8 -*-
"""b725_onset_mass.py -- H-ONSET-MASS, (R335)(4)(i), AS data/b725_registrations.txt (i) REGISTERED IT (:27-:68, committed alone at relay
22210d4b before any figure): "the control, then the rule output and predictions by their own commit, then onsets by b707's route, each zero's
price read from b723's timings".

### UNTRACKED WRITE: data/b725_onset_mass_units.jsonl (one unit per prediction, per onset term, per verdict; appended as each lands, resumable).
### THE READING, AS THE REGISTRATION FIXES IT (:32-:48):
###   the window: b707's C window at gamma_0 = gamma (b694's Window(w, 'C', g0), imported unedited), w = e^(a/2) to 60 digits, so a = 2 log w;
###   M(gamma; a) = SUM over the on-line rows of the certified list (extended_rows(U, top), names not beginning "off"), at +t and at -t, of
###     k^(t) = h^(t)^2, in balls; no zero above the list's top and no tail term;
###   A(gamma; a) = WB.a_int(window, 'q0', 0, 4000) + the unit ball of WB.arch_tail(window, 'q0', 4000) (terms707's A, :162-:164);
###   d(a) = (beta - 1/2) a - log(M / A); UNDEFINED where A > 0 or M / A > 0 is not certified;
###   a*_pred: a grid of 64 equal steps of (log 4, 2 log 192] (the point log 4 read as the bracket's foot only), the least grid point with
###     d >= 0 (its midpoint) whose left neighbour reads d < 0, then bisection on the midpoints to 1e-9 in a; the ball of d printed there.
###   the onset: tools/b723_support.py's route (b707's ladder, b709's fine grid), its helpers imported unedited, its units file rebound to
###     this tool's; the falsifier's tolerance is 0.05 (the registration's :58), not b723's 0.03.
### Routes (each its own foreground call):
###   control [--bank]          the five banked zeros POST HOC, (C2) the reverse sum and A against b707 units ; banks data/b725_onset_mass_control.txt
###   rule [--bank]             the rule printed first, then the walk ; banks data/b725_onset_mass_rule.txt (committed alone before any onset)
###   c1 [--workers n]          (C1): b723_support's c1 through this units file
###   price <zero>              (C3): b723's banked unit-seconds (data/b723_support.txt :15, :21) by the bracket a*_pred falls in
###   run <zero> [--workers n]  the onset (call again until it prints THE ONSET or BEYOND REACH)
###   bank                      data/b725_onset_mass.txt
### Written by the Write tool at b725; it writes its units file and the three banks above and nothing else. Every value a ball at 128 bits.
### Nothing here proves RH or GRH.
"""
import io
import json
import math
import os
import re
import sys
import time
from multiprocessing import Pool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b723_support as S          # noqa: E402  ### b723's onset route (b707's ladder, b709's fine grid): imported unedited, its UNITS rebound
from flint import acb, arb        # noqa: E402

O7, G9 = S.O7, S.G9
W, WB = O7.W, O7.WB
bs, bl, fmt = S.bs, S.bl, S.fmt
UNITS = os.path.join(D, 'b725_onset_mass_units.jsonl')
S.UNITS = UNITS                   # ### S.units, S.put_unit and S.c1 read the module global: this tool's units file
CONTROL_BANK = os.path.join(D, 'b725_onset_mass_control.txt')
RULE_BANK = os.path.join(D, 'b725_onset_mass_rule.txt')
MAIN_BANK = os.path.join(D, 'b725_onset_mass.txt')
R_INT = O7.R_INT
LOG4 = math.log(4)
TOP = 2 * math.log(192)
STEPS = 64
TOL_A = 1e-9
FALSIFIER = 0.05
MOST = 3
BUDGET = 540
POS, NEG = S.POS, S.NEG
# ### the five banked zeros (data/b725_registrations.txt :17-:21): the list row matched by (beta, gamma) as b723_support_rule.py :70 matches
FIVE = (('rho0', '0.9532604748', '16.29021', '6.838396011'), ('band', '0.7979971572', '29.551761', '10.38532711'),
        ('off12', '0.9515046580', '107.399291', '8.553331773'), ('off27', '0.9107626196', '218.700845', '9.866304749'),
        ('off52', '0.9109585427', '355.531957', None))
B723_SECS = dict(low=2677, high=7345)       # ### data/b723_support.txt :15 (off12, (64, 96]) and :21 (off27, (128, 192]), unit-seconds


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_txt(p, L):
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def workers_arg(a):
    global BUDGET
    a = list(a)
    if '--budget' in a:                         # ### seconds per call (default 540, the foreground's); the units file resumes either way
        i = a.index('--budget')
        BUDGET = int(a[i + 1])
        del a[i:i + 2]
    if '--workers' in a:
        i = a.index('--workers')
        n = int(a[i + 1])
        del a[i:i + 2]
        S.WORKERS = n
    return a


# ================================================================================ THE LIST
_LIST = {}


def the_list():
    """(on-line ordinates as balls, off-line rows {name: (beta ball, t ball)} with beta > 1/2, top, row count), read once."""
    if not _LIST:
        import b709_pairs as P9
        import b711_list as L11
        top = L11.top()
        rows = P9.extended_rows(L11.units(), top)[0]
        on = [tt for n, sg, tt in rows if not n.startswith('off')]
        off = dict((n, (sg, tt)) for n, sg, tt in rows if n.startswith('off') and float(sg.mid()) > 0.5)
        _LIST.update(on=on, off=off, top=top, rows=len(rows))
    return _LIST


def five():
    """the five banked zeros as list rows: {label: (row name, beta ball, t ball, banked a* or None)}; refused unless each matches once."""
    off = the_list()['off']
    out = {}
    for lab, b, g, a in FIVE:
        hit = [n for n, (sg, tt) in off.items() if abs(float(sg.mid()) - float(b)) < 5e-5 and abs(float(tt.mid()) - float(g)) < 5e-3]
        if len(hit) != 1 or (lab.startswith('off') and hit[0] != lab):
            sys.exit('### THE BANKED ZERO %s NOT MATCHED ONCE IN THE LIST (%s) -- REFUSED' % (lab, hit))
        sg, tt = off[hit[0]]
        out[lab] = (hit[0], sg, tt, a)
    return out


# ================================================================================ M, A AND d AT ONE RADIUS
def window_at(g0, a):
    w = (arb(repr(float(a))) / 2).exp().str(60, radius=False)
    return W.Window(w, 'C', g0=g0)


def mass(Wd, on, reverse=False):
    seq = list(reversed(on)) if reverse else on
    M = arb(0)
    for tt in seq:
        for t in (tt, -tt):
            M += Wd.khat(acb(t)).real
    return M


def arch(Wd):
    return WB.a_int(Wd, 'q0', 0, R_INT) + WB.unit_ball(WB.arch_tail(Wd, 'q0', R_INT))


def d_at(beta, tt, a):
    """M, A and d at radius a for the zero (beta, t): d = (beta - 1/2) a_ball - log(M / A), None where the log is not certified."""
    g0 = tt.mid().str(25, radius=False)
    Wd = window_at(g0, a)
    M = mass(Wd, the_list()['on'])
    A = arch(Wd)
    ab = 2 * Wd.L
    if not (A > 0) or not (M / A > 0):
        return dict(a=a, a_ball=ab, M=M, A=A, d=None)
    return dict(a=a, a_ball=ab, M=M, A=A, d=(beta - arb('0.5')) * ab - (M / A).log())


def predict(beta, tt):
    """a*_pred by the registration's grid and bisection; returns the record (strings) for the unit."""
    t0 = time.time()
    grid = [LOG4 + j * (TOP - LOG4) / STEPS for j in range(STEPS + 1)]
    G = []
    for a in grid:
        r = d_at(beta, tt, a)
        G.append(r)
    rows = [(r['a'], None if r['d'] is None else float(r['d'].mid())) for r in G]
    undefined = [r['a'] for r in G if r['d'] is None]
    j = next((j for j in range(1, STEPS + 1) if rows[j][1] is not None and rows[j][1] >= 0), None)
    rec = dict(grid=[(a, d) for a, d in rows], undefined=len(undefined), evals=len(G))
    if j is None:
        rec.update(kind='none', note='NO GRID POINT CARRIES THE INEQUALITY: NO a*_pred UNDER 2 log 192')
    elif rows[j - 1][1] is None:
        rec.update(kind='undefined_neighbour', a_pred=rows[j][0], note='THE LEAST GRID POINT WITH d >= 0 HAS AN UNDEFINED LEFT NEIGHBOUR: '
                   'a*_pred READ AT THE GRID POINT, NO BISECTION')
    elif j == 1 and rows[0][1] >= 0:
        rec.update(kind='foot', a_pred=LOG4, note='d >= 0 ALREADY AT log 4: a*_pred AT THE INTERVAL`S FOOT')
    else:
        lo, hi = rows[j - 1][0], rows[j][0]
        n = 0
        while hi - lo > TOL_A:
            mid = (lo + hi) / 2
            r = d_at(beta, tt, mid)
            n += 1
            if r['d'] is not None and float(r['d'].mid()) >= 0:
                hi = mid
            else:
                lo = mid
        r = d_at(beta, tt, hi)
        rec.update(kind='bisected', a_pred=hi, lo=lo, bisections=n + 1, d=bs(r['d']), M=bs(r['M']), A=bs(r['A']), evals=len(G) + n + 1)
    rec['seconds'] = round(time.time() - t0, 1)
    return rec


# ================================================================================ UNITS
def units():
    return S.units()


def pred_unit(U, name, beta, tt):
    k = ('pred', name, '', '', 'q0')
    if k not in U:
        rec = predict(beta, tt)
        rec.update(route='pred', fam=name, kind='', point='', obj='q0', beta=bs(beta), t=bs(tt))
        S.put_unit(rec)
        U[k] = rec
    return U[k]


def pred_line(name, beta, tt, u):
    b = float(beta.mid())
    if u.get('a_pred') is None:
        return '  %-6s beta %.10f gamma %11.6f  beta-1/2 %.10f  a*_pred NONE -- %s ; undefined grid points %d ; %.0f s' % (
            name, b, float(tt.mid()), b - 0.5, u['note'], u['undefined'], u['seconds'])
    tail = (' ; d at a*_pred %s ; M %s ; A %s' % (fmt(bl(u['d']), 6), fmt(bl(u['M']), 8), fmt(bl(u['A']), 8))) if u['kind'] == 'bisected' else (' ; ' + u['note'])
    return '  %-6s beta %.10f gamma %11.6f  beta-1/2 %.10f  a*_pred %.9f%s ; undefined grid points %d ; %d evaluations, %.0f s' % (
        name, b, float(tt.mid()), b - 0.5, u['a_pred'], tail, u['undefined'], u['evals'], u['seconds'])


# ================================================================================ THE CONTROL, POST HOC, AND (C2)
def control(*a):
    write = '--bank' in a
    f = S.free_mb()
    print('  free MB %d ; the control runs on one process ; hold %d -- %s' % (f, S.HOLD_MB, 'MET' if f >= S.HOLD_MB else 'REFUSED'), flush=True)
    if f < S.HOLD_MB:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED')
    U = units()
    Lst = the_list()
    F = five()
    L = ['b725 -- (R335)(4)(i): H-ONSET-MASS`S CONTROL, LABELLED POST HOC, AND THE SEAT`S (C2), BEFORE ANY TEST ZERO IS NAMED (%s)' % utc(), '',
         '### by tools/b725_onset_mass.py `control`; the reading fixed by data/b725_registrations.txt (i) :32-:48 (relay 22210d4b). POST HOC:',
         '### the five chose nothing in the reading and none can falsify it (:49-:52). The list: complete to %s, %d rows, %d on-line ordinates' % (
             Lst['top'], Lst['rows'], len(Lst['on'])),
         '### summed at +t and -t; %d off-line rows with beta > 1/2.' % len(Lst['off']), '']
    L.append('## THE FIVE, POST HOC: a*_pred BESIDE THE BANKED a*, THE RATIO a*/a*_pred, AND M, A, d AT THE BANKED a*')
    t0 = time.time()
    for lab, (row, sg, tt, abk) in F.items():
        if time.time() - t0 > BUDGET:
            print('### THE CALL`S BUDGET REACHED BEFORE %s -- CALL AGAIN TO RESUME' % lab)
            return
        u = pred_unit(U, lab, sg, tt)
        L.append(pred_line('%s' % lab, sg, tt, u) + ' (list row %s)' % row)
        ap = u.get('a_pred')
        if abk is None:
            L.append('    banked: positive to 2 log 192, a* > %.9f ; ratio a*/a*_pred > %s' % (TOP, '%.5f' % (TOP / ap) if ap else 'n/a (no a*_pred)'))
            at = TOP
        else:
            L.append('    banked a* %s ; ratio a*/a*_pred %s' % (abk, '%.5f (a*/a*_pred - 1 = %+.5f)' % (float(abk) / ap, float(abk) / ap - 1) if ap else 'n/a (no a*_pred)'))
            at = float(abk)
        r = d_at(sg, tt, at)
        L.append('    at a = %.9f: M %s ; A %s ; d %s' % (at, fmt(r['M'], 10), fmt(r['A'], 10), fmt(r['d'], 10) if r['d'] is not None else 'UNDEFINED'))
        for l in L[-3:]:
            print(l, flush=True)
    L.append('')
    # ---- (C2)
    ok_all = True
    L.append('## (C2) THE SEAT`S: M SUMMED IN THE LIST`S ORDER AND IN REVERSE AT ONE WINDOW ; A AGAINST b707 UNITS AT THE SAME (gamma, a)')
    row, sg, tt, abk = F['rho0']
    Wd = window_at(tt.mid().str(25, radius=False), float(abk))
    m1, m2 = mass(Wd, Lst['on']), mass(Wd, Lst['on'], reverse=True)
    ok = m1.overlaps(m2)
    ok_all &= ok
    L.append('  rho0 at a = %s: M forward %s ; reverse %s ; %s' % (abk, fmt(m1, 14), fmt(m2, 14), 'AS WANTED' if ok else 'NOT AS WANTED'))
    U7 = O7.units()
    found = 0
    for (route, freq, kind, rung, obj), u in sorted(U7.items()):
        if kind == 'C' and obj == 'q0' and rung == '32' and freq in ('rho0', 'band') and 'A' in u:
            Wd = O7.window('C', rung, dict(O7.FREQS)[freq])
            A = arch(Wd)
            ok = A.overlaps(bl(u['A']))
            ok_all &= ok
            found += 1
            L.append('  %s rung %s (b707 route %s): A here %s ; b707`s %s ; %s' % (freq, rung, route, fmt(A, 14), fmt(bl(u['A']), 14), 'AS WANTED' if ok else 'NOT AS WANTED'))
    if not found:
        ok_all = False
        L.append('  NO b707 C unit at rung 32 found -- NOT AS WANTED')
    L.append('### (C2) %s' % ('AS WANTED' if ok_all else 'NOT AS WANTED'))
    L.append('')
    secs = [U[('pred', lab, '', '', 'q0')]['seconds'] for lab in F]
    L.append('THE PRICE OF ONE a*_PRED, MEASURED HERE: %s s (mean %.0f s) on one process' % (', '.join('%.0f' % s for s in secs), sum(secs) / len(secs)))
    L.append('')
    L.append('### ### **H-ONSET-MASS CONTROL (POST HOC): FIVE READ ; (C2) %s ; TEST ZEROS NAMED 0 ; ONSETS COMPUTED 0.**' % ('AS WANTED' if ok_all else 'NOT AS WANTED'))
    for l in L[-6:]:
        print(l)
    S.put_unit(dict(route='c2verdict', fam='', kind='', point='', obj='', ok=bool(ok_all)))
    if write:
        put_txt(CONTROL_BANK, L)
        print('written data/b725_onset_mass_control.txt')


# ================================================================================ THE RULE AND ITS OUTPUT
RULE = [
    'THE RULE (data/b725_registrations.txt :53-:57), printed before any test zero is named:',
    "  Q0's certified off-line zeros not among the five, in decreasing beta - 1/2, whose predicted a* lies under the ladder's top 2 log 192, at",
    "  most three. Read as written: the list's off-line rows with beta > 1/2, the five excluded by name, walked in decreasing beta - 1/2, each",
    "  one's a*_pred computed in that order until three lie under 2 log 192 or the list ends; no other condition.",
]


def rule(*a):
    write = '--bank' in a
    for l in RULE:
        print(l, flush=True)
    f = S.free_mb()
    print('  free MB %d ; one process ; hold %d -- %s' % (f, S.HOLD_MB, 'MET' if f >= S.HOLD_MB else 'REFUSED'), flush=True)
    if f < S.HOLD_MB:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED')
    U = units()
    Lst = the_list()
    F = five()
    excl = set(row for row, *_ in F.values())
    rest = sorted(((n, sg, tt) for n, (sg, tt) in Lst['off'].items() if n not in excl), key=lambda z: -float(z[1].mid()))
    L = ['b725 -- (R335)(4)(i): H-ONSET-MASS`S RULE AND ITS OUTPUT, EACH a*_pred, BY A COMMIT OF THEIR OWN BEFORE ANY ONSET (%s)' % utc(), '',
         '### by tools/b725_onset_mass.py `rule`; the reading fixed by data/b725_registrations.txt (i) (relay 22210d4b), the control banked before.',
         '### No onset computed.', ''] + RULE + ['']
    L.append('THE LIST READ: complete to %s ; rows %d ; off-line rows with beta > 1/2: %d ; the five excluded by name: %s' % (
        Lst['top'], Lst['rows'], len(Lst['off']), ', '.join('%s (row %s)' % (lab, F[lab][0]) for lab in F)))
    L.append('')
    L.append('THE WALK, IN DECREASING beta - 1/2:')
    t0 = time.time()
    sel = []
    walked = 0
    for name, sg, tt in rest:
        if len(sel) >= MOST:
            break
        if ('pred', name, '', '', 'q0') not in U and time.time() - t0 > BUDGET:
            print('### THE CALL`S BUDGET REACHED BEFORE %s -- CALL AGAIN TO RESUME' % name)
            return
        u = pred_unit(U, name, sg, tt)
        walked += 1
        ap = u.get('a_pred')
        under = ap is not None and ap < TOP
        line = pred_line(name, sg, tt, u) + ('  SELECTED' if under else '  NOT UNDER 2 log 192')
        L.append(line)
        print(line, flush=True)
        if under:
            sel.append((name, sg, tt, ap))
    ended = len(sel) < MOST
    L.append('  walked %d of %d ; selected %d%s' % (walked, len(rest), len(sel), ' ; THE LIST ENDED' if ended else ''))
    L.append('')
    L.append('THE SELECTION, EACH a*_pred:')
    for i, (name, sg, tt, ap) in enumerate(sel, 1):
        b = float(sg.mid())
        L.append('  (%d) Q0 %s = %.10f + %.6fi ; beta - 1/2 = %.10f ; a*_pred = %.9f ; falsified where |a*/a*_pred - 1| > 0.05, i.e. a* outside [%.6f, %.6f]' % (
            i, name, b, float(tt.mid()), b - 0.5, ap, 0.95 * ap, 1.05 * ap))
    L.append('')
    L.append('### ### **H-ONSET-MASS`S RULE: WALKED %d ; SELECTED %d ; ONSETS COMPUTED 0.**' % (walked, len(sel)))
    for l in L[-(len(sel) + 3):]:
        print(l)
    if write:
        put_txt(RULE_BANK, L)
        print('written data/b725_onset_mass_rule.txt')


def selected():
    """the rule's selection, read from its committed bank and checked against the list read afresh: {name: (beta ball, t ball, a_pred)}."""
    txt = io.open(RULE_BANK, encoding='utf-8').read()
    sel = re.findall(r'\((\d)\) Q0 (off\d+) = ([0-9.]+) \+ ([0-9.]+)i ; beta - 1/2 = [0-9.]+ ; a\*_pred = ([0-9.]+)', txt)
    off = the_list()['off']
    out = {}
    for _i, name, b, g, ap in sel:
        sg, tt = off[name]
        assert abs(float(sg.mid()) - float(b)) < 1e-9 and abs(float(tt.mid()) - float(g)) < 1e-5, name
        out[name] = (sg, tt, float(ap))
    return out


# ================================================================================ (C1), THE PRICE AND ONE ZERO
def c1(*a):
    workers_arg(a)
    S.c1()


def _bracket(ap):
    for lo, hi in zip(S.LADDER, S.LADDER[1:]):
        if ap <= 2 * math.log(float(O7.arb(S.WIDTH[hi]).mid())):
            return lo, hi
    return S.LADDER[-2], S.LADDER[-1]


def price(zero, *a):
    sg, tt, ap = selected()[zero]
    lo, hi = _bracket(ap)
    us = B723_SECS['low'] if hi in ('32', '48', '64', '96') else B723_SECS['high']
    print('PRICE %s: beta %.10f gamma %.6f a*_pred %.9f ; the bracket the prediction falls in (%s, %s] ; b723`s banked unit-seconds for an onset '
          'in such a bracket %d (data/b723_support.txt %s) ; about %d s (%.2f h) with %d workers, more where the onset falls above the bracket' % (
              zero, float(sg.mid()), float(tt.mid()), ap, lo, hi, us, ':15' if us == B723_SECS['low'] else ':21', us / S.WORKERS, us / S.WORKERS / 3600, S.WORKERS))
    return us


def ladder(zero, *a):
    """(R335)(8): a zero carried, not computed -- b707's seven rungs alone (both forms), its coarse bracket printed; no fine grid."""
    workers_arg(a)
    U = units()
    if not S._c1_ok(U):
        sys.exit('### C1 NOT READ AS WANTED -- NO FIGURE AT A NAMED ZERO')
    sg, tt, ap = selected()[zero]
    g0 = tt.mid().str(25, radius=False)
    S.guard('ladder ' + zero)
    with Pool(S.WORKERS) as pool:
        for obj in ('zeta', 'q0'):
            S._compute(pool, U, [(g0, r, kd, obj) for r in S.LADDER for kd in G9.KINDS], 'coarse', zero, lambda t: t[1])
    rq = dict((r, S._read(U, 'coarse', zero, r, 'q0')) for r in S.LADDER)
    for r in S.LADDER:
        print('  %s coarse %-4s q0 lambda_min %s | %s' % (zero, r, fmt(bl(rq[r]['lmin']), 10), rq[r]['reading']), flush=True)
    negs = [r for r in S.LADDER if rq[r]['reading'] == NEG]
    if negs:
        hi = negs[0]
        lo = S.LADDER[S.LADDER.index(hi) - 1] if hi != S.LADDER[0] else None
        a_lo = 2 * math.log(float(O7.arb(S.WIDTH[lo]).mid())) if lo else 0.0
        a_hi = 2 * math.log(float(O7.arb(S.WIDTH[hi]).mid()))
        beyond = a_lo / ap - 1 >= 0.05 or a_hi / ap - 1 < -0.05     # ### the claim only when the whole bracket lies outside the tolerance
        print('### %s CARRIED: THE COARSE BRACKET (%s, %s], a in (%.6f, %.6f] ; a*/a*_pred - 1 in (%+.4f, %+.4f] -- %s' % (
            zero, lo, hi, a_lo, a_hi, a_lo / ap - 1, a_hi / ap - 1,
            'every onset in it beyond 0.05' if beyond else 'THE BRACKET MEETS THE 0.05 TOLERANCE: NO READING WITHOUT THE FINE GRID'))
        S.put_unit(dict(route='bracket', fam=zero, kind='', point='', obj='q0', lo=lo, hi=hi, a_lo=a_lo, a_hi=a_hi))
    else:
        print('### %s CARRIED: POSITIVE TO 2 log 192 -- BEYOND REACH' % zero)
        S.put_unit(dict(route='bracket', fam=zero, kind='', point='', obj='q0', beyond=True))


def run(zero, *a):
    workers_arg(a)
    U = units()
    if not S._c1_ok(U):
        sys.exit('### C1 NOT READ AS WANTED -- NO ONSET AT A NAMED ZERO (the control before the figure)')
    sg, tt, ap = selected()[zero]
    g0 = tt.mid().str(25, radius=False)
    S.guard('run ' + zero)
    t0 = time.time()
    LADDER = S.LADDER
    with Pool(S.WORKERS) as pool:
        tasks = [(g0, r, kd, 'zeta') for r in LADDER for kd in G9.KINDS]
        S._compute(pool, U, tasks, 'coarse', zero, lambda t: t[1])
        rz = dict((r, S._read(U, 'coarse', zero, r, 'zeta')) for r in LADDER)
        for r in LADDER:
            print('  %s coarse %-4s zeta lambda_min %s | %s' % (zero, r, fmt(bl(rz[r]['lmin']), 10), rz[r]['reading']), flush=True)
        bad = [r for r in LADDER if rz[r]['reading'] != POS]
        if bad:
            sys.exit('### THE ZETA FORM NOT POSITIVE DEFINITE AT RUNG(S) %s -- NO Q0 FIGURE ON THE LADDER' % bad)
        tasks = [(g0, r, kd, 'q0') for r in LADDER for kd in G9.KINDS]
        S._compute(pool, U, tasks, 'coarse', zero, lambda t: t[1])
        rq = dict((r, S._read(U, 'coarse', zero, r, 'q0')) for r in LADDER)
        for r in LADDER:
            print('  %s coarse %-4s q0   lambda_min %s | %s' % (zero, r, fmt(bl(rq[r]['lmin']), 10), rq[r]['reading']), flush=True)
        negs = [r for r in LADDER if rq[r]['reading'] == NEG]
        if not negs:
            print('### %s: NO NEGATIVE DIRECTION ON b707`S LADDER TO 2 log 192 -- BEYOND REACH' % zero)
            S.put_unit(dict(route='onset', fam=zero, kind='', point='', obj='q0', beyond=True, seconds=int(time.time() - t0)))
            return
        hi = negs[0]
        if hi == LADDER[0]:
            print('### %s: NEGATIVE AT a = log 2, THE LADDER`S FOOT' % zero)
            S.put_unit(dict(route='onset', fam=zero, kind='', point='log2', obj='q0', foot=True, seconds=int(time.time() - t0)))
            return
        lo = LADDER[LADDER.index(hi) - 1]
        undec = [r for r in LADDER[:LADDER.index(hi)] if rq[r]['reading'] != POS]
        print('  %s THE COARSE BRACKET (%s, %s] ; rungs below it not POSITIVE: %s' % (zero, lo, hi, undec or 'none'), flush=True)
        S.register(zero, g0, lo, hi)
        pts = G9.grid(zero)
        inner = pts[1:]
        for j in range(0, len(inner), S.BATCH):
            if time.time() - t0 > BUDGET:
                print('### THE CALL`S BUDGET REACHED BEFORE POINT %d of %d -- CALL AGAIN TO RESUME' % (inner[j]['i'], len(pts) - 1))
                return
            if j % (S.BATCH * 10) == 0:
                S.guard('%s point %d' % (zero, inner[j]['i']))
            batch = inner[j:j + S.BATCH]
            tasks = [(zero, g0, lo, hi, p, kd, 'zeta') for p in batch for kd in G9.KINDS]
            S._compute(pool, U, tasks, 'fine', zero, lambda t: t[4]['name'])
            for p in batch:
                r = S._read(U, 'fine', zero, p['name'], 'zeta')
                if r['reading'] != POS:
                    sys.exit('### THE ZETA FORM AT %s %s READS %s -- NO Q0 FIGURE AT THIS POINT' % (zero, p['name'], r['reading']))
            tasks = [(zero, g0, lo, hi, p, kd, 'q0') for p in batch for kd in G9.KINDS]
            S._compute(pool, U, tasks, 'fine', zero, lambda t: t[4]['name'])
            for p in batch:
                r = S._read(U, 'fine', zero, p['name'], 'q0')
                a_p = U[('fine', zero, 'C', p['name'], 'q0')]['a_radius']
                if p['i'] % 40 == 1 or r['reading'] != POS:
                    print('  %s %4d %-16s a %s | lambda_min %s | %s' % (zero, p['i'], p['name'], fmt(bl(a_p), 10), fmt(bl(r['lmin']), 10), r['reading']), flush=True)
                if r['reading'] == NEG:
                    a_on = float(bl(a_p).mid())
                    dev = a_on / ap - 1
                    print('### %s: THE ONSET at %s, a = %s ; a*_pred %.9f ; a*/a*_pred - 1 = %+.5f ; %s' % (
                        zero, p['name'], fmt(bl(a_p), 10), ap, dev, 'WITHIN 0.05' if abs(dev) <= FALSIFIER else 'BEYOND 0.05: THE FALSIFIER FIRES'))
                    S.put_unit(dict(route='onset', fam=zero, kind='', point=p['name'], obj='q0', i=p['i'], a=a_p, lmin=r['lmin'], lo=lo, hi=hi,
                                    points=len(pts), seconds=int(time.time() - t0)))
                    return
        print('### %s: NO GRID POINT NEGATIVE IN (%s, %s] -- A DEFECT: the coarse rung %s read NEGATIVE' % (zero, lo, hi, hi))


# ================================================================================ THE BANK
def bank(*a):
    U = units()
    Z = selected() if os.path.exists(RULE_BANK) else {}
    L = ['b725 -- (R335)(4)(i): H-ONSET-MASS`S ONSETS ON THE ZEROS ITS RULE NAMED, BY b707`S ROUTE ON b709`S LADDER (%s)' % utc(), '',
         '### by tools/b725_onset_mass.py (tools/b723_support.py`s route, imported unedited); the registration data/b725_registrations.txt (i)',
         '### (relay 22210d4b), the control data/b725_onset_mass_control.txt and the rule`s output data/b725_onset_mass_rule.txt committed before',
         '### any onset. Units: data/b725_onset_mass_units.jsonl (untracked). The falsifier: |a*/a*_pred - 1| > 0.05.', '']
    c1ok = S._c1_ok(U)
    v = U.get(('c2verdict', '', '', '', ''))
    L.append('## (C1) THE BANKED ONSETS THROUGH THIS CODE PATH: %s ; (C2) %s' % ('AS WANTED' if c1ok else 'NOT AS WANTED',
                                                                            'AS WANTED' if (v and v.get('ok')) else 'NOT AS WANTED'))
    for fam, B in S.BANKED.items():
        u = U.get(('c1', 'c1_' + fam, 'C', B['onset'], 'q0'))
        L.append('  %-4s onset %s at a = %s (banked %s)' % (fam, B['onset'], fmt(bl(u['a_radius']), 10) if u else '### NOT RUN', B['a']))
    L.append('')
    L.append('## THE ZEROS, IN THE RULE`S ORDER')
    res = []
    for name, (sg, tt, ap) in Z.items():
        o = next((u for k, u in U.items() if k[0] == 'onset' and k[1] == name), None)
        cz = [(r, S._read(U, 'coarse', name, r, 'q0')) for r in S.LADDER]
        L.append('  %s: beta %.10f ; gamma0 %s ; a*_pred %.9f' % (name, float(sg.mid()), tt.mid().str(25, radius=False), ap))
        L.append('    the ladder (q0): ' + ' ; '.join('%s %s' % (r, ('%s %s' % (fmt(bl(x['lmin']), 6), 'POS' if x['reading'] == POS else ('NEG' if x['reading'] == NEG else 'UND'))) if x else 'not run')
                                                    for r, x in cz))
        if o is None:
            bk = U.get(('bracket', name, '', '', 'q0'))
            if bk and bk.get('beyond'):
                L.append('    CARRIED, NOT COMPUTED ((R335)(8)): the ladder positive to 2 log 192 -- beyond reach')
            elif bk:
                L.append('    CARRIED, NOT COMPUTED ((R335)(8)): the coarse bracket (%s, %s], a in (%.6f, %.6f] ; were the onset computed, a*/a*_pred - 1 in (%+.4f, %+.4f]' % (
                    bk['lo'], bk['hi'], bk['a_lo'], bk['a_hi'], bk['a_lo'] / ap - 1, bk['a_hi'] / ap - 1))
            else:
                L.append('    NOT RUN')
            res.append((name, None))
            continue
        if o.get('beyond') or o.get('foot'):
            L.append('    %s' % ('BEYOND REACH: no negative direction on the ladder to 2 log 192 = %.6f; no onset computed; were the onset above it, '
                                 'a*/a*_pred - 1 > %+.5f' % (TOP, TOP / ap - 1) if o.get('beyond') else 'NEGATIVE AT THE LADDER`S FOOT'))
            res.append((name, 'beyond' if o.get('beyond') else 'foot'))
            continue
        a_on = float(bl(o['a']).mid())
        dev = a_on / ap - 1
        res.append((name, dev))
        nu = [u for k, u in U.items() if k[0] in ('coarse', 'fine') and k[1] == name]
        L.append('    THE ONSET: %s (grid point %d of %d in (%s, %s]) at a = %s, lambda_min %s ; a*/a*_pred - 1 = %+.5f -- %s ; units %d, their seconds summed %d' % (
            o['point'], o['i'], o['points'] - 1, o['lo'], o['hi'], fmt(bl(o['a']), 10), fmt(bl(o['lmin']), 10), dev,
            'WITHIN 0.05' if abs(dev) <= FALSIFIER else 'BEYOND 0.05', len(nu), sum(u.get('seconds', 0) for u in nu)))
    run_ = [d for _n, d in res if isinstance(d, float)]
    fired = [n for n, d in res if isinstance(d, float) and abs(d) > FALSIFIER]
    beyond = [n for n, d in res if d == 'beyond']
    notrun = [n for n, d in res if d is None]
    L.append('')
    L.append('THE FALSIFIER (a computed onset with |a*/a*_pred - 1| > 0.05 at a test zero): %s' % ('FIRED at %s' % fired if fired else ('NOT FIRED on %d zeros' % len(run_))))
    L.append('BEYOND REACH, NO ONSET COMPUTED: %s ; NOT RUN (carried with its price): %s' % (beyond or 'none', notrun or 'none'))
    verdict = 'REFUTED' if fired else ('HELD' if run_ else 'NOT SCORABLE')
    L.append('THE HYPOTHESIS (HELD, REFUTED or NOT SCORABLE): %s' % verdict)
    L.append('')
    L.append('### ### **H-ONSET-MASS: C1 %s ; ZEROS %d ; ONSETS COMPUTED %d ; WITHIN 0.05 %d ; BEYOND REACH %d ; NOT RUN %d ; THE HYPOTHESIS %s.**' % (
        'AS WANTED' if c1ok else 'NOT AS WANTED', len(Z), len(run_), len(run_) - len(fired), len(beyond), len(notrun), verdict))
    put_txt(MAIN_BANK, L)
    for l in L:
        print(l)
    print('written data/b725_onset_mass.txt')


ROUTES = dict(control=control, rule=rule, c1=c1, price=price, ladder=ladder, run=run, bank=bank)

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ROUTES:
        print('usage: b725_onset_mass.py ' + ' | '.join(ROUTES))
        sys.exit(2)
    ROUTES[sys.argv[1]](*sys.argv[2:])
