# -*- coding: utf-8 -*-
"""b722_coeffs.py -- -31 AND -55 ((R332)(3)) AND THE FOURTEEN CLASS-NUMBER-2 FIELDS ((R332)(4)), BY b711'S ROUTE THROUGH THE CUT 32532.
Written whole at b722 by the Write tool, after tools/b720_coeffs.py (read through the Read tool :1-:359; its wrapper form kept, its
controls replaced by (R332)(3)'s three).

### THE ROUTE, b711's: tools/b711_coeffs.py's recursion IMPORTED unedited (spf_table, factor, recursion, value, show) -- b_n = r_Q1(n)/2
### (b_1 = 1), c(n) = b_n log n - SUM_{d | n, 1 < d < n} c(d) b_{n/d}, each c(n) exact as a vector of rationals over the primes of n, its sign
### read from the ball SUM q_p log p; r_Q(n) by direct enumeration (tools/b716_genus_control.py counts, IMPORTED unedited, its box set by the
### module's DISC, set to the form's discriminant and restored, as b717's, b719's and b720's wrappers did). b(n) = c(n)/log n exactly; beside
### it the Omega derivation (tools/b718_classgroup.py log_coeffs, the ordered-factorization sum), the two to be equal.
### THE REGISTRATIONS, read unchanged: data/b721_registrations.txt, its bytes equal to its blob at e8c3dff4 (H-C3-31 :85-:89, H-C4-55
### :90-:96, falsifiers :98-:102) and the walk's rows :31-:48 with H-C2-WALK :62-:70 (committed at 15cb6cc4); the walk's n0 and value are
### read from the bank's rows by pattern, not typed here.
### THE CONTROLS ((R332)(3); `controls`, banked in data/b722_coeffs_controls.json before any figure):
### (C1) the recursion with b_n = 1 (zeta's series) returns von Mangoldt exactly at every n <= the cut;
### (C2) -23's banked n0 = 48 reproduced through the same cut by the same route: its closed form (-8) log 2 + (-2) log 3 and its count of
###      negative coefficients 1066 (data/b711_coeffs.txt :12, :14);
### (C3) a planted coefficient: -23's series with b_2 moved from r_Q(2)/2 = 0 to 1 (r_Q(2) planted 2) -- the reading, run as (C2) ran,
###      wanted NOT to return n0 48 with that closed form and count (failing as wanted).
### Routes: `controls [dry]` ; `pair [dry]` -> data/b722_coeffs.txt/.json ((R332)(3)) ; `walk [dry]` -> data/b722_walk.txt/.json ((R332)(4));
### each run route refused before the controls are banked as wanted, and before the free memory meets the hold.
"""
import ctypes
import io
import json
import os
import re
import subprocess
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import fmpq                # noqa: E402
import b711_coeffs as C11             # noqa: E402  ### b711's recursion, imported unedited
import b716_genus_control as G        # noqa: E402  ### b716's counts and kronecker, imported unedited
import b718_classgroup as CG          # noqa: E402  ### b718's class group, imported unedited

ACT = 'b722'
CUT = 32532
HOLD_MB = 2560
REG = 'b721_registrations.txt'
REG_COMMIT = 'e8c3dff4'
CTL = '%s_coeffs_controls.json' % ACT
C2_WANT = ((1, 1, 6), -23, 48, '(-8) log 2 + (-2) log 3', 1066, 'data/b711_coeffs.txt :12, :14')
# ### H-C3-31 and H-C4-55 (data/b721_registrations.txt :85-:101): the forms, n0, b, a, the pair sum; each checked against the bank's own line
PAIR = {-31: dict(forms=[(1, 1, 8), (2, -1, 4), (2, 1, 4)], n0=80, b='-2', a=4, pair=12, row='H-C3-31',
                  needle='(a) the table: n0 = 80 = 2^4 . 5'),
        -55: dict(forms=[(1, 1, 14), (2, -1, 7), (2, 1, 7), (4, 3, 4)], n0=224, b='-2', a=6, pair=20, row='H-C4-55',
                  needle='(a) the table: n0 = 224 = 2^5 . 7')}
WALK = (-24, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267, -403, -427)
WALK_CONTROL = -15
GRADE_ALL = ('the value law at the least negative index holds at all eighteen imaginary quadratic fields of class number 2, by exhaustion over '
             'the list Baker (1971) and Stark (1975) proved complete -- that completeness cited and not compiled -- and over exact rational '
             'arithmetic in Python, not compiled.')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


class _MS(ctypes.Structure):
    _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]


def free_or_exit(what):
    m = _MS()
    m.dwLength = ctypes.sizeof(_MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    mb = m.ullAvailPhys // 2 ** 20
    print('### FREE MEMORY BEFORE %s: %d MB (the hold %d MB) -- %s' % (what, mb, HOLD_MB, 'MET' if mb >= HOLD_MB else 'NOT MET, NOTHING RUN'))
    if mb < HOLD_MB:
        sys.exit(1)
    return mb


def rd(name):
    with io.open(os.path.join(D, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def reg_text():
    """the registrations bank, refused unless its bytes are its blob at e8c3dff4 (read unchanged)."""
    blob = subprocess.run(['git', '-C', ROOT, 'show', '%s:data/%s' % (REG_COMMIT, REG)], capture_output=True).stdout.replace(b'\r', b'')
    with open(os.path.join(D, REG), 'rb') as fh:
        now = fh.read().replace(b'\r', b'')
    if not blob or blob != now:
        sys.exit('### data/%s DIFFERS FROM ITS BLOB AT %s (or the blob is absent) -- NOTHING RUN' % (REG, REG_COMMIT))
    return now.decode('utf-8')


def walk_rows():
    """the walk's rows of the registrations bank (:31-:48): {D: (n0, value, line)}."""
    out = {}
    for i, l in enumerate(reg_text().split(NL), 1):
        m = re.match(r'^  (-\d+)\s+n0 (\d+) = \S.*?\s+b (-2|-1/2)\s+shape ', l)
        if m:
            out[int(m.group(1))] = (int(m.group(2)), m.group(3), i)
    want = set(WALK) | {WALK_CONTROL}
    if set(out) != want:
        sys.exit('### THE WALK`S ROWS READ %s, NOT THE FOURTEEN AND -15 -- NOTHING RUN' % sorted(out))
    return out


def pair_lines():
    t = reg_text().split(NL)
    out = {}
    for D_, spec in PAIR.items():
        hits = [i for i, l in enumerate(t, 1) if spec['needle'] in l]
        hd = [i for i, l in enumerate(t, 1) if l.startswith('  %s (D = %d;' % (spec['row'], D_))]
        fa = [i for i, l in enumerate(t, 1) if l.startswith('  FALSIFIER %s:' % spec['row'])]
        if len(hits) != 1 or len(hd) != 1 or len(fa) != 1:
            sys.exit('### %s`S LINES NOT FOUND ONCE IN data/%s -- NOTHING RUN' % (spec['row'], REG))
        if ('a(%d) = %d, the pair sum %d, b(%d) = %s' % (spec['n0'], spec['a'], spec['pair'], spec['n0'], spec['b'])) not in t[hits[0]] + ' ' + t[hits[0] - 1] + ' ' + t[hits[0] + 1]:
            sys.exit('### %s`S FIGURES (a, pair, b) NOT AS THE BANK READS -- NOTHING RUN' % spec['row'])
        out[D_] = dict(head=hd[0], table=hits[0], falsifier=fa[0])
    return out


def counts(f, disc, n_max):
    """b716's counts with its box set by the form's own discriminant (b716's DISC restored after)."""
    keep = G.DISC
    G.DISC = disc
    try:
        return G.counts(f, n_max)
    finally:
        G.DISC = keep


def coeffs(r, N, spf):
    b = [fmpq(0)] + [fmpq(r[k], 2) for k in range(1, N + 1)]
    c = C11.recursion(b, N, spf)
    neg, undecided, vals = [], [], {}
    for n in range(2, N + 1):
        if not c[n]:
            continue
        x = C11.value(c[n])
        if x < 0:
            neg.append(n)
            vals[n] = x
        elif not x > 0:
            undecided.append(n)
    return b, c, neg, undecided, vals


def b_of(c, n, spf):
    """b(n) = c(n)/log n exactly, when c(n) is (b . e_p) log p over n's primes p^e_p; '0' when c(n) is zero; None otherwise."""
    fac = C11.factor(n, spf)
    v = c[n]
    if not v:
        return '0'
    ratios = set(v.get(p, fmpq(0)) / e for p, e in fac.items())
    return str(list(ratios)[0]) if len(ratios) == 1 and set(v) <= set(fac) else None


def principal(D_):
    return (1, 1, (1 - D_) // 4) if D_ % 4 == 1 or D_ % 4 == -3 else (1, 0, -D_ // 4)


def form_s(f):
    a, b, c = f
    return '%dx^2 %s %dxy + %dy^2' % (a, '+' if b >= 0 else '-', abs(b), c) if b else '%dx^2 + %dy^2' % (a, c)


def _c23(N, spf, plant):
    f, disc, n_want, v_want, cnt_want, src = C2_WANT
    r = counts(f, disc, N)
    if plant:
        r = list(r)
        r[2] = 2
    _b, c, negl, und, _v = coeffs(r, N, spf)
    n0 = negl[0] if negl else None
    return dict(n=n0, value=C11.show(c[n0]) if n0 else None, count=len(negl), undecided=len(und), n_want=n_want, v_want=v_want,
                count_want=cnt_want, src=src, reproduced=(n0 == n_want and C11.show(c[n0]) == v_want and len(negl) == cnt_want),
                planted_r2=r[2])


def controls(*a):
    pair_lines()
    walk_rows()
    free_or_exit('THE COEFFICIENT CONTROLS THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = C11.recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = C11.factor(n, spf)
        if cz[n] != ({next(iter(f)): fmpq(1)} if len(f) == 1 else {}):
            bad1.append(n)
    c2 = _c23(N, spf, False)
    c3 = _c23(N, spf, True)
    j = dict(at=utc(), cut=N, c1=not bad1, bad1=bad1[:20], c2=c2, c3=c3, seconds=int(time.time() - t0))
    j['ok'] = j['c1'] and c2['reproduced'] and not c3['reproduced']
    for l in control_lines(j):
        print(l)
    if 'dry' in a:
        return
    _put(CTL, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print('written data/%s' % CTL)


def control_lines(j):
    N = j['cut']
    c2, c3 = j['c2'], j['c3']
    return ['### (C1) the recursion with b_n = 1 (zeta`s series) returns von Mangoldt exactly at every n <= %d: mismatches %d %s -- %s' % (
                N, len(j['bad1']), j['bad1'][:5], 'AS WANTED' if j['c1'] else '### NOT AS WANTED'),
            '### (C2) -23, Q = x^2 + xy + 6y^2, through %d: the least negative n = %s, c = %s, negatives %d (wanted %d, %s, %d ; %s) -- %s' % (
                N, c2['n'], c2['value'], c2['count'], c2['n_want'], c2['v_want'], c2['count_want'], c2['src'],
                'REPRODUCED, AS WANTED' if c2['reproduced'] else '### NOT REPRODUCED'),
            '### (C3) the planted coefficient: -23`s series with r_Q(2) planted %d (b_2 = 1, the true 0): the least negative n = %s, c = %s, '
            'negatives %d -- %s' % (c3['planted_r2'], c3['n'], c3['value'], c3['count'],
                                    'FAILS TO REPRODUCE, AS WANTED' if not c3['reproduced'] else '### REPRODUCES -- NOT AS WANTED'),
            '### THE CONTROLS: C1 %s ; C2 %s ; C3 (failing) %s ; %d s' % (j['c1'], c2['reproduced'], not c3['reproduced'], j['seconds'])]


def reading(D_, forms, N, spf, P):
    q1 = principal(D_)
    if q1 not in forms:
        sys.exit('### THE PRINCIPAL FORM %s OF %d NOT AMONG ITS REDUCED FORMS %s -- NOTHING RUN' % (q1, D_, forms))
    r1 = counts(q1, D_, N)
    b, c, neg, undecided, vals = coeffs(r1, N, spf)
    out = dict(D=D_, Q1=form_s(q1), negatives=len(neg), first=neg[:10], undecided=len(undecided),
               nonzero=sum(1 for n in range(2, N + 1) if c[n]), rnz=sum(1 for n in range(1, N + 1) if r1[n]))
    n0 = neg[0] if neg else None
    out['n0'] = n0
    if not n0:
        return out
    fac = C11.factor(n0, spf)
    a_int = [0] + [r1[k] // 2 for k in range(1, N + 1)]
    a_int[1] = 1
    bo, _Om = CG.log_coeffs(a_int, n0, P)
    _F, e, Tb, _ok = CG.group(D_)
    reps = {}
    for p in fac:
        rp = [f for f in forms if counts(f, D_, p)[p]]
        t, g = CG.prime_class(D_, p)
        reps[p] = dict(kind=t, cls=form_s(g) if g else None, order=CG.order(g, e, Tb) if g else None, forms=[form_s(f) for f in rp],
                       by_q1=(q1 in rp))
    pair = CG.pair_sum(a_int, n0)
    out.update(fac=sorted(fac.items()), closed=C11.show(c[n0]), ball=vals[n0].str(15), b=b_of(c, n0, spf), b_omega=str(bo[n0]),
               a=a_int[n0], pair=pair, k3=CG.ordered_factorizations(a_int, n0), a_half=str(Fraction(a_int[n0]) - Fraction(pair, 2)),
               divs=[(d, a_int[d]) for d in range(2, n0) if n0 % d == 0 and a_int[d]], reps=reps)
    return out


def reading_lines(r, N):
    L = ['## D = %d, Q1 = %s: nonzero c(n) %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (
        r['D'], r['Q1'], r['nonzero'], N - 1, r['rnz'], N, r['undecided'])]
    if not r['n0']:
        return L + ['  NO n <= %d WITH c(n) < 0' % N, '']
    return L + ['  THE LEAST n WITH c(n) < 0: n0 = %d = %s ; c(n0) = %s = %s' % (
                    r['n0'], ' . '.join(('%d^%d' % (p, k)) if k > 1 else '%d' % p for p, k in r['fac']), r['closed'], r['ball']),
                '  b(n0) = c(n0)/log n0 = %s ; by the Omega derivation %s ; EQUAL %s' % (r['b'], r['b_omega'], r['b'] == r['b_omega']),
                '  the decomposition: a(n0) %d ; the ordered pair sum %d ; k >= 3 factorizations %d ; a - pair/2 = %s' % (
                    r['a'], r['pair'], r['k3'], r['a_half']),
                '  the proper divisors with nonzero a: ' + (', '.join('%d (%d)' % dv for dv in r['divs']) or 'NONE'),
                '  each prime of n0: ' + ' ; '.join('%d %s, a prime ideal above it in the class of %s (order %s), represented by %s, by Q1: %s' % (
                    p, x['kind'], x['cls'], x['order'], ', '.join(x['forms']) or 'NO FORM', x['by_q1']) for p, x in sorted(r['reps'].items())),
                '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, r['negatives'], r['first']), '']


def _ctl_or_exit():
    ctl = json.load(io.open(os.path.join(D, CTL), encoding='utf-8')) if os.path.exists(os.path.join(D, CTL)) else {}
    if not ctl.get('ok'):
        sys.exit('### THE CONTROLS ARE NOT BANKED AS WANTED (data/%s) -- NOTHING RUN' % CTL)
    return ctl


def pair(*a):
    pl = pair_lines()
    ctl = _ctl_or_exit()
    mb = free_or_exit('THE COEFFICIENTS AT -31 AND -55 THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    R, rows = {}, []
    for D_, spec in PAIR.items():
        if sorted(CG.reduced_forms(D_)) != sorted(spec['forms']):
            sys.exit('### THE REDUCED FORMS OF %d ARE %s, NOT THE REGISTRATION`S -- NOTHING RUN' % (D_, CG.reduced_forms(D_)))
        r = R[D_] = reading(D_, spec['forms'], N, spf, P)
        if not r['n0']:
            rows.append((spec['row'], D_, 'NOT SCORABLE', 'no n <= %d with b(n) < 0' % N))
            continue
        rep = [p for p, x in r['reps'].items() if x['by_q1']]
        figs = r['n0'] == spec['n0'] and r['b'] == spec['b'] and r['a'] == spec['a']
        word = 'HELD' if figs and not rep else 'REFUTED'
        rows.append((spec['row'], D_, word, 'computed n0 %d, b(n0) %s, a(n0) %d, the pair sum %d ; registered %d, %s, %d, %d ; the prime '
                     'clause: primes of n0 the principal form represents %s' % (r['n0'], r['b'], r['a'], r['pair'], spec['n0'], spec['b'],
                                                                                  spec['a'], spec['pair'], rep or 'NONE')))
    L = ['%s -- (R332)(3): -31 AND -55 THROUGH %d BY b711`S ROUTE, UNDER e8c3dff4, EACH HYPOTHESIS READ HELD OR REFUTED WITH ITS PRIME CLAUSE (%s)' % (
        ACT, N, utc()), '',
         '### rows are readings of c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), exact for n <= %d, each a vector of rationals' % N,
         '### over the primes of n (c(n) = SUM q_p log p); a(n) = b_n = r_Q1(n)/2 (b_1 = 1); b(n) = c(n)/log n, the coefficient of log(Z_Q1/2).',
         '### THE REGISTRATIONS, committed before: data/%s at %s, read unchanged -- H-C3-31 :%d (the table :%d, falsifier :%d), H-C4-55 :%d (the table '
         ':%d, falsifier :%d). FREE MEMORY %d MB against the hold %d.' % (REG, REG_COMMIT, pl[-31]['head'], pl[-31]['table'], pl[-31]['falsifier'],
                                                                           pl[-55]['head'], pl[-55]['table'], pl[-55]['falsifier'], mb, HOLD_MB),
         '### THE CONTROLS FIRST (data/%s, %s):' % (CTL, ctl['at'])]
    L += control_lines(ctl) + ['']
    for D_ in (-31, -55):
        L += reading_lines(R[D_], N)
    L += ['### THE ROWS, EACH ON ITS OWN CLAUSES (data/%s, H-C3-31 and H-C4-55 with their falsifiers):' % REG]
    L += ['  %-8s %-5d %-12s %s' % x for x in rows]
    L += ['', '### ### **n0(-31) = %s, b = %s ; n0(-55) = %s, b = %s ; H-C3-31 %s ; H-C4-55 %s ; %d s.**' % (
        R[-31]['n0'], R[-31].get('b'), R[-55]['n0'], R[-55].get('b'), rows[0][2], rows[1][2], int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put('%s_coeffs.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    _put('%s_coeffs.json' % ACT, (json.dumps(dict(at=utc(), cut=N, controls_at=ctl['at'], registrations=dict(bank='data/' + REG, commit=REG_COMMIT),
                                                  readings=dict((str(k), v) for k, v in R.items()),
                                                  rows=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in rows]),
                                             indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8'))
    print('written data/%s_coeffs.txt, .json' % ACT)


def walk(*a):
    W = walk_rows()
    ctl = _ctl_or_exit()
    mb = free_or_exit('THE WALK AT THE FOURTEEN FIELDS AND -15 THROUGH %d' % CUT)
    t0 = time.time()
    N = CUT
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    R, rows = {}, []
    for D_ in (WALK_CONTROL,) + WALK:
        forms = sorted(CG.reduced_forms(D_))
        F, _e, _Tb, ok = CG.group(D_)
        h = len(forms)
        r = R[D_] = reading(D_, forms, N, spf, P)
        r['h'], r['group_axioms'] = h, all(ok.values())
        wn, wv, wl = W[D_]
        name = 'CONTROL -15' if D_ == WALK_CONTROL else 'H-C2-WALK'
        if h != 2:
            sys.exit('### %d CARRIES %d REDUCED FORMS, NOT 2 -- NOTHING BANKED' % (D_, h))
        if not r['n0']:
            rows.append((name, D_, 'NOT SCORABLE', 'no n <= %d with b(n) < 0 (the walk`s row :%d)' % (N, wl)))
            continue
        rep = [p for p, x in r['reps'].items() if x['by_q1']]
        word = 'HELD' if (r['n0'] == wn and r['b'] == wv and not rep) else 'REFUTED'
        rows.append((name, D_, word, 'computed n0 %d, b(n0) %s (Omega %s) ; the walk`s n0 %d, value %s (:%d) ; primes of n0 the principal form '
                     'represents %s' % (r['n0'], r['b'], r['b_omega'], wn, wv, wl, rep or 'NONE')))
    tests = [x for x in rows if x[0] == 'H-C2-WALK']
    held = sum(1 for x in tests if x[2] == 'HELD')
    ref = sum(1 for x in tests if x[2] == 'REFUTED')
    ctl_row = rows[0]
    grade = (GRADE_ALL if held == 14 and ctl_row[2] == 'HELD' else
             'the value law at the least negative index holds at %d of the fourteen fields read here; %d REFUTED, each printed with its figure, '
             'standing; %d NOT SCORABLE; exact rational arithmetic in Python, not compiled.' % (held, ref, len(tests) - held - ref))
    L = ['%s -- (R332)(4): THE FOURTEEN CLASS-NUMBER-2 FIELDS UNDER H-C2-WALK THROUGH %d BY b711`S ROUTE, -15 THE CONTROL ROW (%s)' % (ACT, N, utc()), '',
         '### rows as data/%s_coeffs.txt`s; the walk`s n0 and value read from data/%s`s rows by pattern, its bytes its blob at %s (H-C2-WALK :62-:70,' % (ACT, REG, REG_COMMIT),
         '### its rows :31-:48 committed at 15cb6cc4). FREE MEMORY %d MB against the hold %d. THE CONTROLS FIRST (data/%s, %s):' % (mb, HOLD_MB, CTL, ctl['at'])]
    L += control_lines(ctl)
    L += ['### (C-WALK) the control row -15 (banked n0 24, -2, data/b713_coeffs.txt :13): %s -- %s' % (
        ctl_row[3], 'AS WANTED' if ctl_row[2] == 'HELD' else '### NOT AS WANTED'), '']
    for D_ in (WALK_CONTROL,) + WALK:
        L += reading_lines(R[D_], N)
    L += ['### THE ROWS, EACH ON ITS OWN CLAUSES (H-C2-WALK: n0, b(n0), the prime clause; the falsifier :68-:69):']
    L += ['  %-12s %-5d %-12s %s' % x for x in rows]
    L += ['', '### THE GRADE: ' + grade, '',
          '### ### **H-C2-WALK: %d OF 14 HELD, REFUTED %d, NOT SCORABLE %d ; THE CONTROL ROW -15 %s ; %d s.**' % (
              held, ref, len(tests) - held - ref, ctl_row[2], int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put('%s_walk.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    _put('%s_walk.json' % ACT, (json.dumps(dict(at=utc(), cut=N, controls_at=ctl['at'], held=held, refuted=ref, grade=grade,
                                                readings=dict((str(k), v) for k, v in R.items()),
                                                rows=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in rows]),
                                           indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8'))
    print('written data/%s_walk.txt, .json' % ACT)


def _put(name, data):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(controls=controls, pair=pair, walk=walk).get(route)
    if fn is None:
        sys.exit('usage: b722_coeffs.py controls [dry] | pair [dry] | walk [dry]')
    fn(*sys.argv[2:])
