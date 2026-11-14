# -*- coding: utf-8 -*-
"""b755_coeffs.py -- (R365)(3): H-C3-LAW AT ITS FOURTEEN FIELDS OF CLASS NUMBER 3, BY b711'S ROUTE THROUGH THE BOUND 90000, -23 AND -31 THE
CONTROL ROWS; THE SECOND ROUTE TO THE THREE PRIMES BY A CUBIC; THE GROUP-RING MODEL'S READING, FORCED.
Carried from tools/b722_coeffs.py by tools/standing/carry.py (data/b755_carry_coeffs.txt: the substitution b722 -> b755 alone, 6 lines,
--shifted for the tool's own name at :2 and in the usage line), then written whole by the Write tool against (R365)(3) (data/b755_ferry.txt
:13). Kept from the carried tool unedited in their working: free_or_exit, rd, the blob check of the registration (reg_text), counts, coeffs,
b_of, principal, form_s, reading's route (b711's recursion, b716's counts, b718's Omega derivation and classes), the controls (C1)-(C3) and
the writer _put. Removed: the pair route of (R332)(3) and the class-number-2 walk's rows, which read b721's registration and no field here.

### THE THREE CHANGES (R365)(3) names, each by the carried line it replaces:
###   (i)   the bound 90000 in place of the cut 32532 (tools/b722_coeffs.py :46), the registered index being 32683 at -643, 83317 at -883
###         and 73853 at -907; the -23 control's count of negative coefficients read through 32532, where its banked 1066 stands;
###   (ii)  a field with three reduced forms accepted where the carried one exits (:345, `if h != 2`); any other count exits here;
###   (iii) the table's row reader takes the minus sign as typed there (U+2212) as well as the hyphen (the carried :104 read the hyphen alone).
### THE CONTROLS BEFORE ANY ROW ((R365)(3); `controls`, banked in data/b755_coeffs_controls.json before any figure):
###   (C1) the series with b_n = 1 at every n returns von Mangoldt's function exactly at every n <= 90000;
###   (C2) -23: the least negative index 48 and c(48) = (-8) log 2 + (-2) log 3 (data/b711_coeffs.txt :12), its count of negative
###        coefficients through 32532 equal to the banked 1066 (:14);
###   (C31) -31: the least negative index 80 (data/b722_coeffs.txt :13; the registration's control row :31);
###   (C3) a planted coefficient: -23's series with r_Q(2) planted 2 (b_2 = 1, the true 0), wanted NOT to reproduce (C2);
###   (CC) the second route's own control at -23: x^3 - x - 1 ((R365)(3)), mismatches 0 over the primes below 20000, and x^3 - 2 planted,
###        mismatches above 0 (failing as wanted);
###   (CM) the model's own control at -23 through the raised bound: n0 48 and b -2, and the class above 2 planted at the identity moving
###        it off 48 (failing as wanted).
### THE ROWS ((R365)(3); `walk`, banked in data/b755_walk.txt/.json): at each of the sixteen, the principal form x^2 + xy + ((1 - D)/4) y^2;
###   the class number as a count of reduced forms; the three least primes that split and that the principal form does not represent, from
###   its own enumeration (r_Q1(p) = 0), beside the row's three; the least n with b(n) < 0 and b there; the pattern; HELD or REFUTED on the
###   falsifier as registered (:54): the index or the value differing from its row. The second route and the model beside, no test.
### Routes: `parse` (the table read and printed, nothing computed) ; `selftest` (the root routine against a brute count, on cubics whose
### discriminant is none of the sixteen) ; `controls [dry]` ; `walk [dry]`. `controls` and `walk` refuse themselves while this file differs
### from its committed blob, before the free memory meets the hold, and `walk` before the controls are banked as wanted at this bound.
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

ACT = 'b755'
BOUND = 90000                         # ### (R365)(3), change (i): in place of the carried CUT = 32532
COUNT_CUT = 32532                     # ### the -23 control's count read through the banked cut (data/b711_coeffs.txt :14)
HOLD_MB = 2560
REG = 'b753_registrations.txt'
REG_COMMIT = '3f865479'               # ### the table's commit, after the rule's 4c86bf24 (relay git log of the bank)
SELF = 'tools/b755_coeffs.py'
CTL = '%s_coeffs_controls.json' % ACT
C2_WANT = ((1, 1, 6), -23, 48, '(-8) log 2 + (-2) log 3', 1066, 'data/b711_coeffs.txt :12, :14')
C31_WANT = ((1, 1, 8), -31, 80, '(-8) log 2 + (-2) log 5', '-2', 'data/b722_coeffs.txt :13')
WALK = (-59, -83, -107, -139, -211, -283, -307, -331, -379, -499, -547, -643, -883, -907)
CONTROL_ROWS = (-23, -31)
RULE_NEEDLE = 'Let D be a negative fundamental discriminant of class number 3'
FALSIFIER_NEEDLE = 'FALSIFIER: any of the fourteen where either differs from its row.'
PRIMES_BELOW = 20000
CUBIC_BOX = 12
CUBIC_23 = (0, -1, -1)                # ### x^3 - x - 1 ((R365)(3)), coefficients (a, b, c) of x^3 + a x^2 + b x + c
CUBIC_PLANT = (0, 0, -2)              # ### x^3 - 2, the plant
ROW = re.compile(r'^  ([−-])(\d+)\s+(\d+), (\d+), (\d+)\s+(\d+)\s+\((\d+(?:,\d+)*)\)\s+([−-])(\d+)(\s+CONTROL\b.*)?$')


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


def committed_or_exit(what):
    """this file tracked and equal to its blob at HEAD, before any figure ((R365)(3): committed before its run)."""
    tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', SELF], capture_output=True).returncode == 0
    clean = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', SELF], capture_output=True).returncode == 0
    head = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%h', '--', SELF], capture_output=True, text=True).stdout.strip()
    if not (tracked and clean):
        sys.exit('### %s IS NOT COMMITTED AS IT STANDS (tracked %s, equal to HEAD %s) -- %s NOT RUN' % (SELF, tracked, clean, what))
    return head


def rd(name):
    with io.open(os.path.join(D, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def reg_text():
    """the registration, refused unless its bytes are its blob at 3f865479 (read at its blob, (R365)(3))."""
    blob = subprocess.run(['git', '-C', ROOT, 'show', '%s:data/%s' % (REG_COMMIT, REG)], capture_output=True).stdout.replace(b'\r', b'')
    with open(os.path.join(D, REG), 'rb') as fh:
        now = fh.read().replace(b'\r', b'')
    if not blob or blob != now:
        sys.exit('### data/%s DIFFERS FROM ITS BLOB AT %s (or the blob is absent) -- NOTHING RUN' % (REG, REG_COMMIT))
    return now.decode('utf-8')


def reg_lines():
    """the rule's line and the falsifier's, each found once: {rule, falsifier}."""
    t = reg_text().split(NL)
    out = {}
    for k, nd in (('rule', RULE_NEEDLE), ('falsifier', FALSIFIER_NEEDLE)):
        hits = [i for i, l in enumerate(t, 1) if nd in l]
        if len(hits) != 1:
            sys.exit('### THE %s`S LINE FOUND %d TIMES IN data/%s, NOT ONCE -- NOTHING RUN' % (k.upper(), len(hits), REG))
        out[k] = hits[0]
    return out


def table_rows():
    """the table's sixteen rows (:29-:46), read by pattern: {D: dict(primes, n0, pattern, value, control, line, minus)}; change (iii):
    the minus sign as typed (U+2212) or the hyphen, each row's form kept."""
    out = {}
    for i, l in enumerate(reg_text().split(NL), 1):
        m = ROW.match(l)
        if not m:
            continue
        if m.group(1) != m.group(8):
            sys.exit('### THE ROW AT :%d CARRIES TWO MINUS FORMS -- NOTHING RUN' % i)
        D_ = -int(m.group(2))
        out[D_] = dict(primes=(int(m.group(3)), int(m.group(4)), int(m.group(5))), n0=int(m.group(6)),
                       pattern=tuple(int(x) for x in m.group(7).split(',')), value='-' + m.group(9), control=bool(m.group(10)), line=i,
                       minus='U+2212' if m.group(1) == '−' else 'hyphen')
    want = set(WALK) | set(CONTROL_ROWS)
    if set(out) != want or set(d_ for d_, r in out.items() if r['control']) != set(CONTROL_ROWS):
        sys.exit('### THE TABLE`S ROWS READ %s (controls %s), NOT THE FOURTEEN AND -23, -31 -- NOTHING RUN' % (
            sorted(out), sorted(d_ for d_, r in out.items() if r['control'])))
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


# ### THE SECOND ROUTE: a monic cubic x^3 + a x^2 + b x + c with |a|, |b|, |c| <= 12 and discriminant D; its roots modulo p by the
# ### powers of x modulo the cubic and the gcd with x^p - x (the number of roots is that gcd's degree, x^p - x splitting with no square)

def cubic_disc(a, b, c):
    return a * a * b * b - 4 * b ** 3 - 4 * a ** 3 * c - 27 * c * c + 18 * a * b * c


def cubic_s(f):
    a, b, c = f
    s = 'x^3'
    for k, t in ((a, 'x^2'), (b, 'x'), (c, '')):
        if k:
            s += ' %s %s%s' % ('+' if k > 0 else '-', '' if abs(k) == 1 and t else abs(k), t)
    return s


def _int_root(f):
    a, b, c = f
    if c == 0:
        return True
    ds = [d for d in range(1, abs(c) + 1) if c % d == 0]
    return any(r ** 3 + a * r * r + b * r + c == 0 for d in ds for r in (d, -d))


def cubic_search(D_):
    """every monic cubic in the box with discriminant D_ and no integer root, in the order (|a|, |b| + |c|, a, b, c)."""
    R = range(-CUBIC_BOX, CUBIC_BOX + 1)
    out = [(a, b, c) for a in R for b in R for c in R if cubic_disc(a, b, c) == D_ and not _int_root((a, b, c))]
    return sorted(out, key=lambda t: (abs(t[0]), abs(t[1]) + abs(t[2]), t[0], t[1], t[2]))


def _mulmod(u, v, f, p):
    a, b, c = f
    w = [0] * 5
    for i in range(3):
        if u[i]:
            for j in range(3):
                w[i + j] += u[i] * v[j]
    for k in (4, 3):
        t = w[k]
        if t:
            w[k] = 0
            w[k - 1] -= t * a
            w[k - 2] -= t * b
            w[k - 3] -= t * c
    return [w[0] % p, w[1] % p, w[2] % p]


def _trim(u):
    while u and u[-1] == 0:
        u.pop()
    return u


def _pmod(u, v, p):
    u = _trim([x % p for x in u])
    dv = len(v) - 1
    inv = pow(v[-1], p - 2, p) if p > 2 else 1
    while u and len(u) - 1 >= dv:
        k, q = len(u) - 1 - dv, u[-1] * inv % p
        for i in range(len(v)):
            u[k + i] = (u[k + i] - q * v[i]) % p
        _trim(u)
    return u


def roots_mod(f, p):
    """the number of roots of the monic cubic f modulo the prime p: the degree of gcd(f, x^p - x) over F_p."""
    a, b, c = f
    r, base, e = [1, 0, 0], [0, 1 % p, 0], p
    while e:
        if e & 1:
            r = _mulmod(r, base, f, p)
        base = _mulmod(base, base, f, p)
        e >>= 1
    g = _trim([r[0] % p, (r[1] - 1) % p, r[2] % p])
    if not g:
        return 3
    u, v = _trim([c % p, b % p, a % p, 1]), g
    while v:
        u, v = v, _pmod(u, v, p)
    return len(u) - 1


def cubic_reading(D_, f, r1, below=PRIMES_BELOW):
    """the primes below `below` not dividing D_: those where f has no root, against those that split and that Q1 does not represent."""
    A, B, n = set(), set(), 0
    for p in CG.primes_upto(below - 1):
        if D_ % p == 0:
            continue
        n += 1
        if roots_mod(f, p) == 0:
            A.add(p)
        if CG.kron(D_, p) == 1 and r1[p] == 0:
            B.add(p)
    mm = sorted(A ^ B)
    return dict(cubic=cubic_s(f), coeffs=list(f), disc=cubic_disc(*f), compared=n, no_root=len(A), split_nonprincipal=len(B),
                mismatches=len(mm), first=mm[:10])


# ### FORCED, no test: the group-ring model (tools/b718_abstract.py) through tools/b720_predict.py, imported unedited, its CUT (:34) and its
# ### primes P (:35) raised to the bound at run time, as (R365)(3) orders ("its bound at :34 raised the same way")

_PR = []


def model_module():
    if not _PR:
        import b720_predict as PR   # noqa: E402
        PR.CUT = BOUND
        PR.P = CG.primes_upto(BOUND)
        _PR.append(PR)
    return _PR[0]


def model(D_, override=None):
    PR = model_module()
    S = PR.setup(D_)
    r = PR.predict(S, override)
    return dict(n=r['n'], b=str(r['b']) if r.get('b') is not None else 'NONE', shape=r.get('shape') or 'NONE', nbad=r['nbad'],
                axioms=all(S['ok'].values()), cut=PR.CUT)


def _c23(N, spf, plant):
    f, disc, n_want, v_want, cnt_want, src = C2_WANT
    r = counts(f, disc, N)
    if plant:
        r = list(r)
        r[2] = 2
    _b, c, negl, und, _v = coeffs(r, N, spf)
    n0 = negl[0] if negl else None
    cnt = sum(1 for n in negl if n <= COUNT_CUT)
    return dict(n=n0, value=C11.show(c[n0]) if n0 else 'NONE', count=cnt, count_bound=len(negl), undecided=len(und), n_want=n_want,
                v_want=v_want, count_want=cnt_want, src=src, reproduced=(n0 == n_want and C11.show(c[n0]) == v_want and cnt == cnt_want),
                planted_r2=r[2])


def _c31(N, spf):
    f, disc, n_want, v_want, b_want, src = C31_WANT
    r = counts(f, disc, N)
    _b, c, negl, _und, _v = coeffs(r, N, spf)
    n0 = negl[0] if negl else None
    b = b_of(c, n0, spf) if n0 else 'NONE'
    return dict(n=n0, value=C11.show(c[n0]) if n0 else 'NONE', b=b, n_want=n_want, v_want=v_want, b_want=b_want, src=src,
                reproduced=(n0 == n_want and C11.show(c[n0]) == v_want and b == b_want))


def controls(*a):
    table_rows()
    reg_lines()
    head = committed_or_exit('THE CONTROLS')
    free_or_exit('THE COEFFICIENT CONTROLS THROUGH %d' % BOUND)
    t0 = time.time()
    N = BOUND
    spf = C11.spf_table(N)
    one = [fmpq(0)] + [fmpq(1)] * N
    cz = C11.recursion(one, N, spf)
    bad1 = []
    for n in range(2, N + 1):
        f = C11.factor(n, spf)
        if cz[n] != ({next(iter(f)): fmpq(1)} if len(f) == 1 else {}):
            bad1.append(n)
    del cz, one
    c2 = _c23(N, spf, False)
    c31 = _c31(N, spf)
    c3 = _c23(N, spf, True)
    r23 = counts(C2_WANT[0], -23, PRIMES_BELOW)
    cc = cubic_reading(-23, CUBIC_23, r23)
    cp = cubic_reading(-23, CUBIC_PLANT, r23)
    m23 = model(-23)
    mpl = model(-23, override={2: (0,)})
    j = dict(at=utc(), bound=N, count_cut=COUNT_CUT, tool_commit=head, c1=not bad1, bad1=bad1[:20], c2=c2, c31=c31, c3=c3, cc=cc, cp=cp,
             cm=m23, cmp=mpl, seconds=int(time.time() - t0))
    j['cc_ok'] = cc['mismatches'] == 0 and cc['disc'] == -23 and cp['mismatches'] > 0
    j['cm_ok'] = m23['n'] == 48 and m23['b'] == '-2' and m23['axioms'] and mpl['n'] != 48
    j['ok'] = j['c1'] and c2['reproduced'] and c31['reproduced'] and not c3['reproduced'] and j['cc_ok'] and j['cm_ok']
    for l in control_lines(j):
        print(l)
    if 'dry' in a:
        return
    _put(CTL, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print('written data/%s' % CTL)


def control_lines(j):
    N = j['bound']
    c2, c31, c3, cc, cp, cm, cmp_ = j['c2'], j['c31'], j['c3'], j['cc'], j['cp'], j['cm'], j['cmp']
    return ['### (C1) the series with b_n = 1 at every n returns von Mangoldt`s function exactly at every n <= %d: mismatches %d %s -- %s' % (
                N, len(j['bad1']), j['bad1'][:5], 'AS WANTED' if j['c1'] else '### NOT AS WANTED'),
            '### (C2) -23, Q = x^2 + xy + 6y^2, through %d: the least negative n = %s, c = %s, negatives through %d %d (wanted %d, %s, %d ; %s) ; '
            'negatives through %d %d -- %s' % (
                N, c2['n'], c2['value'], j['count_cut'], c2['count'], c2['n_want'], c2['v_want'], c2['count_want'], c2['src'], N, c2['count_bound'],
                'REPRODUCED, AS WANTED' if c2['reproduced'] else '### NOT REPRODUCED'),
            '### (C31) -31, Q = x^2 + xy + 8y^2, through %d: the least negative n = %s, c = %s, b = %s (wanted %d, %s, %s ; %s) -- %s' % (
                N, c31['n'], c31['value'], c31['b'], c31['n_want'], c31['v_want'], c31['b_want'], c31['src'],
                'REPRODUCED, AS WANTED' if c31['reproduced'] else '### NOT REPRODUCED'),
            '### (C3) the planted coefficient: -23`s series with r_Q(2) planted %d (b_2 = 1, the true 0): the least negative n = %s, c = %s, '
            'negatives through %d %d -- %s' % (c3['planted_r2'], c3['n'], c3['value'], j['count_cut'], c3['count'],
                                               'FAILS TO REPRODUCE, AS WANTED' if not c3['reproduced'] else '### REPRODUCES -- NOT AS WANTED'),
            '### (CC) the second route at -23: %s (discriminant %d), over %d primes below %d not dividing 23: no root at %d, split and not '
            'represented by Q1 at %d, mismatches %d ; %s planted (discriminant %d): mismatches %d -- %s' % (
                cc['cubic'], cc['disc'], cc['compared'], PRIMES_BELOW, cc['no_root'], cc['split_nonprincipal'], cc['mismatches'], cp['cubic'],
                cp['disc'], cp['mismatches'], 'AS WANTED, THE PLANT FAILING' if j['cc_ok'] else '### NOT AS WANTED'),
            '### (CM) the model at -23 through %d (tools/b720_predict.py, its CUT and primes raised at run time): n0 %s, b %s, shape %s, the '
            'group`s axioms %s ; the class above 2 planted at the identity: n0 %s, b %s -- %s' % (
                cm['cut'], cm['n'], cm['b'], cm['shape'], 'ALL HOLD' if cm['axioms'] else 'FAIL', cmp_['n'], cmp_['b'],
                'AS WANTED, THE PLANT FAILING' if j['cm_ok'] else '### NOT AS WANTED'),
            '### THE CONTROLS: C1 %s ; C2 %s ; C31 %s ; C3 (failing) %s ; CC %s ; CM %s ; %d s ; the tool at %s' % (
                j['c1'], c2['reproduced'], c31['reproduced'], not c3['reproduced'], j['cc_ok'], j['cm_ok'], j['seconds'], j['tool_commit'])]


def reading(D_, forms, N, spf, P):
    q1 = principal(D_)
    if q1 not in forms:
        sys.exit('### THE PRINCIPAL FORM %s OF %d NOT AMONG ITS REDUCED FORMS %s -- NOTHING RUN' % (q1, D_, forms))
    r1 = counts(q1, D_, N)
    b, c, neg, undecided, vals = coeffs(r1, N, spf)
    three = []
    for p in P:
        if CG.kron(D_, p) == 1 and r1[p] == 0:
            three.append(p)
            if len(three) == 3:
                break
    out = dict(D=D_, Q1=form_s(q1), negatives=len(neg), first=neg[:10], undecided=len(undecided),
               nonzero=sum(1 for n in range(2, N + 1) if c[n]), rnz=sum(1 for n in range(1, N + 1) if r1[n]), three=three)
    n0 = neg[0] if neg else None
    out['n0'] = n0
    if not n0:
        return out, r1
    fac = C11.factor(n0, spf)
    a_int = [0] + [r1[k] // 2 for k in range(1, N + 1)]
    a_int[1] = 1
    bo, _Om = CG.log_coeffs(a_int, n0, P)
    _F, e, Tb, _ok = CG.group(D_)
    reps = {}
    for p in fac:
        rp = [f for f in forms if counts(f, D_, p)[p]]
        t, g = CG.prime_class(D_, p)
        reps[p] = dict(kind=t, cls=form_s(g) if g else 'NONE', order=CG.order(g, e, Tb) if g else 'NONE', forms=[form_s(f) for f in rp],
                       by_q1=(q1 in rp))
    pair = CG.pair_sum(a_int, n0)
    out.update(fac=sorted(fac.items()), closed=C11.show(c[n0]), ball=vals[n0].str(15), b=b_of(c, n0, spf), b_omega=str(bo[n0]),
               a=a_int[n0], pair=pair, k3=CG.ordered_factorizations(a_int, n0), a_half=str(Fraction(a_int[n0]) - Fraction(pair, 2)),
               divs=[(d, a_int[d]) for d in range(2, n0) if n0 % d == 0 and a_int[d]], reps=reps,
               pattern=tuple(sorted(fac.values(), reverse=True)),
               n0_on_three=all(p in three for p in fac))
    return out, r1


def reading_lines(r, N):
    L = ['## D = %d, Q1 = %s, h = %d (reduced forms %s): nonzero c(n) %d of %d (r_Q1(n) nonzero at %d n <= %d) ; signs undecided %d' % (
        r['D'], r['Q1'], r['h'], ', '.join(r['forms']), r['nonzero'], N - 1, r['rnz'], N, r['undecided']),
         '  THE THREE LEAST PRIMES THAT SPLIT AND THAT Q1 DOES NOT REPRESENT (r_Q1(p) = 0): %s ; the row`s %s (:%d) ; EQUAL %s' % (
             ', '.join(str(p) for p in r['three']), ', '.join(str(p) for p in r['row_primes']), r['row_line'], list(r['three']) == list(r['row_primes']))]
    if not r['n0']:
        return L + ['  NO n <= %d WITH c(n) < 0' % N, '']
    return L + ['  THE LEAST n WITH c(n) < 0: n0 = %d = %s ; c(n0) = %s = %s' % (
                    r['n0'], ' . '.join(('%d^%d' % (p, k)) if k > 1 else '%d' % p for p, k in r['fac']), r['closed'], r['ball']),
                '  b(n0) = c(n0)/log n0 = %s ; by the Omega derivation %s ; EQUAL %s' % (r['b'], r['b_omega'], r['b'] == r['b_omega']),
                '  the pattern (%s) ; the row`s (%s) ; n0`s primes among the three %s' % (
                    ','.join(str(x) for x in r['pattern']), ','.join(str(x) for x in r['row_pattern']), r['n0_on_three']),
                '  the decomposition: a(n0) %d ; the ordered pair sum %d ; k >= 3 factorizations %d ; a - pair/2 = %s' % (
                    r['a'], r['pair'], r['k3'], r['a_half']),
                '  the proper divisors with nonzero a: ' + (', '.join('%d (%d)' % dv for dv in r['divs']) or 'NONE'),
                '  each prime of n0: ' + ' ; '.join('%d %s, a prime ideal above it in the class of %s (order %s), represented by %s, by Q1: %s' % (
                    p, x['kind'], x['cls'], x['order'], ', '.join(x['forms']) or 'NO FORM', x['by_q1']) for p, x in sorted(r['reps'].items())),
                '  THE COUNT OF NEGATIVE COEFFICIENTS through %d: %d ; the first ten %s' % (N, r['negatives'], r['first']), '']


def _ctl_or_exit():
    ctl = json.load(io.open(os.path.join(D, CTL), encoding='utf-8')) if os.path.exists(os.path.join(D, CTL)) else {}
    if not ctl.get('ok') or ctl.get('bound') != BOUND:
        sys.exit('### THE CONTROLS ARE NOT BANKED AS WANTED AT THE BOUND %d (data/%s) -- NOTHING RUN' % (BOUND, CTL))
    return ctl


def walk(*a):
    W = table_rows()
    RL = reg_lines()
    ctl = _ctl_or_exit()
    head = committed_or_exit('THE WALK')
    mb = free_or_exit('THE WALK AT THE FOURTEEN FIELDS AND -23, -31 THROUGH %d' % BOUND)
    t0 = time.time()
    N = BOUND
    spf = C11.spf_table(N)
    P = CG.primes_upto(N)
    R, rows, CU, MO = {}, [], {}, {}
    for D_ in CONTROL_ROWS + WALK:
        t1 = time.time()
        forms = sorted(CG.reduced_forms(D_))
        h = len(forms)
        if h != 3:
            sys.exit('### %d CARRIES %d REDUCED FORMS, NOT 3 -- NOTHING BANKED' % (D_, h))   # ### change (ii): three accepted, any other exits
        _F, _e, _Tb, ok = CG.group(D_)
        r, r1 = reading(D_, forms, N, spf, P)
        w = W[D_]
        r.update(h=h, forms=[form_s(f) for f in forms], group_axioms=all(ok.values()), row_primes=w['primes'], row_line=w['line'],
                 row_pattern=w['pattern'], row_n0=w['n0'], row_value=w['value'], minus=w['minus'])
        cs = cubic_search(D_)
        CU[D_] = dict(found=len(cs), first=cubic_s(cs[0]) if cs else 'NOT FOUND', reading=cubic_reading(D_, cs[0], r1) if cs else None)
        del r1
        MO[D_] = model(D_)
        r['seconds'] = int(time.time() - t1)
        R[D_] = r
        name = 'CONTROL' if D_ in CONTROL_ROWS else 'H-C3-LAW'
        if not r['n0']:
            rows.append((name, D_, 'NOT SCORABLE', 'no n <= %d with b(n) < 0 (the row :%d)' % (N, w['line'])))
            continue
        word = 'HELD' if (r['n0'] == w['n0'] and r['b'] == w['value']) else 'REFUTED'
        rows.append((name, D_, word, 'computed n0 %d, b(n0) %s (Omega %s), pattern (%s) ; the row`s n0 %d, value %s, pattern (%s) (:%d)' % (
            r['n0'], r['b'], r['b_omega'], ','.join(str(x) for x in r['pattern']), w['n0'], w['value'], ','.join(str(x) for x in w['pattern']), w['line'])))
        print('  %s %d %s (%d s)' % (name, D_, word, r['seconds']))
    tests = [x for x in rows if x[0] == 'H-C3-LAW']
    held = sum(1 for x in tests if x[2] == 'HELD')
    ref = sum(1 for x in tests if x[2] == 'REFUTED')
    ctl_rows = dict((x[1], x[2]) for x in rows if x[0] == 'CONTROL')
    three_eq = sum(1 for D_ in R if list(R[D_]['three']) == list(R[D_]['row_primes']))
    cu_found = sum(1 for D_ in CU if CU[D_]['reading'])
    cu_mm = sum(CU[D_]['reading']['mismatches'] for D_ in CU if CU[D_]['reading'])
    mo_eq = sum(1 for D_ in MO if R[D_]['n0'] and MO[D_]['n'] == R[D_]['n0'] and MO[D_]['b'] == R[D_]['b'])
    minus = dict((k, sum(1 for w in W.values() if w['minus'] == k)) for k in ('U+2212', 'hyphen'))
    grade = ('the coefficient law at the least negative index holds at the fourteen fields of the registration`s table (data/%s :32-:45) and at '
             'its two control rows, read through %d over exact rational arithmetic in Python, not compiled; whether these sixteen are every '
             'field of class number 3 is not said here (the registration :57-:59, the literature bank).' % (REG, N)
             if held == 14 and all(v == 'HELD' for v in ctl_rows.values()) else
             'the coefficient law at the least negative index holds at %d of the fourteen fields read here; %d REFUTED, each printed with its '
             'figure, standing; %d NOT SCORABLE; exact rational arithmetic in Python through %d, not compiled.' % (held, ref, len(tests) - held - ref, N))
    L = ['%s -- (R365)(3): H-C3-LAW AT ITS FOURTEEN FIELDS THROUGH %d BY b711`S ROUTE, -23 AND -31 THE CONTROL ROWS (%s)' % (ACT, N, utc()), '',
         '### rows: c(n), Q1`s log-derivative coefficients (-Z_Q1`/Z_Q1 = SUM c(n) n^-s), exact for n <= %d, each a vector of rationals over the' % N,
         '### primes of n (c(n) = SUM q_p log p); a(n) = b_n = r_Q1(n)/2 (b_1 = 1); b(n) = c(n)/log n, the coefficient of log(Z_Q1/2).',
         '### THE REGISTRATION, read at its blob: data/%s, its bytes equal to its blob at %s (the rule :%d-:16, the table :29-:46, the falsifier' % (REG, REG_COMMIT, RL['rule']),
         '### :%d); each row`s primes, n0, pattern and value read from the table by pattern, the minus sign as typed there (U+2212 at %d rows, the' % (RL['falsifier'], minus['U+2212']),
         '### hyphen at %d). THE BOUND %d at every row, in place of the carried 32532: step zero priced the walk under two hours (data/%s_stepzero.txt),' % (minus['hyphen'], N, ACT),
         '### so no row runs to its registered index and one tenth alone. THE TOOL tools/%s_coeffs.py at %s, committed before its run. FREE MEMORY' % (ACT, head),
         '### %d MB against the hold %d. THE CONTROLS FIRST (data/%s, %s):' % (mb, HOLD_MB, CTL, ctl['at'])]
    L += control_lines(ctl) + ['']
    for D_ in CONTROL_ROWS + WALK:
        L += reading_lines(R[D_], N)
    L += ['### THE ROWS, EACH ON THE FALSIFIER AS REGISTERED (:%d, the index or the value differing from its row); the primes and the pattern '
          'printed beside, no part of the verdict:' % RL['falsifier']]
    L += ['  %-9s %-5d %-12s %s' % x for x in rows]
    L += ['', '### THE SECOND ROUTE TO THE THREE PRIMES, a control of the enumeration and no test of the law ((R365)(3)): a monic cubic with '
          'integer coefficients of absolute value at most %d and discriminant D, found by search (the first in the order |a|, |b| + |c|, a, b, '
          'c, none with an integer root); the primes below %d not dividing D where it has no root, against those that split and that Q1 does '
          'not represent:' % (CUBIC_BOX, PRIMES_BELOW)]
    for D_ in CONTROL_ROWS + WALK:
        cu = CU[D_]
        if not cu['reading']:
            L += ['  %-5d NOT FOUND (no cubic in the box with that discriminant)' % D_]
            continue
        x = cu['reading']
        L += ['  %-5d %s (of %d found) ; primes compared %d ; no root %d ; split, not by Q1 %d ; MISMATCHES %d%s' % (
            D_, cu['first'], cu['found'], x['compared'], x['no_root'], x['split_nonprincipal'], x['mismatches'],
            (' ; the first %s' % x['first']) if x['mismatches'] else '')]
    L += ['', '### FORCED, and no test ((R365)(3); data/%s :55-:56): the group-ring model`s reading of the same fields from their classes alone '
          '(tools/b718_abstract.py through tools/b720_predict.py, imported unedited, its CUT (:34) and primes (:35) raised to %d at run time):' % (REG, N)]
    for D_ in CONTROL_ROWS + WALK:
        m = MO[D_]
        L += ['  %-5d the model`s n0 %s, b %s, shape %s ; bad primes %d ; the axioms %s ; beside the computed n0 %s, b %s: %s' % (
            D_, m['n'], m['b'], m['shape'], m['nbad'], 'ALL HOLD' if m['axioms'] else 'FAIL', R[D_]['n0'], R[D_].get('b', 'NONE'),
            'AGREE' if (R[D_]['n0'] and m['n'] == R[D_]['n0'] and m['b'] == R[D_]['b']) else 'DIFFER')]
    L += ['', '### THE GRADE: ' + grade, '',
          '### ### **H-C3-LAW: %d OF 14 HELD, REFUTED %d, NOT SCORABLE %d ; THE CONTROL ROWS -23 %s, -31 %s ; THE THREE PRIMES AS THE ROW`S AT %d '
          'OF 16 ; THE SECOND ROUTE: A CUBIC AT %d OF 16, MISMATCHES %d ; THE MODEL (FORCED) AGREEING AT %d OF 16 ; THROUGH %d ; %d s.**' % (
              held, ref, len(tests) - held - ref, ctl_rows.get(-23), ctl_rows.get(-31), three_eq, cu_found, cu_mm, mo_eq, N, int(time.time() - t0))]
    print(NL.join(L))
    if 'dry' in a:
        return
    _put('%s_walk.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    _put('%s_walk.json' % ACT, (json.dumps(dict(at=utc(), bound=N, tool_commit=head, controls_at=ctl['at'], held=held, refuted=ref,
                                                not_scorable=len(tests) - held - ref, controls=ctl_rows, three_equal=three_eq,
                                                cubic=dict((str(k), v) for k, v in CU.items()), model=dict((str(k), v) for k, v in MO.items()),
                                                grade=grade, readings=dict((str(k), v) for k, v in R.items()),
                                                rows=[dict(row=n, D=d, verdict=v, why=w) for n, d, v, w in rows]),
                                           indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8'))
    print('written data/%s_walk.txt, .json' % ACT)


def parse(*a):
    """the table read and printed; nothing computed."""
    W = table_rows()
    RL = reg_lines()
    print('### data/%s at %s: the rule :%d, the falsifier :%d ; rows %d' % (REG, REG_COMMIT, RL['rule'], RL['falsifier'], len(W)))
    for D_ in CONTROL_ROWS + WALK:
        w = W[D_]
        print('  :%d  %-5d primes %s n0 %d pattern %s value %s minus %s%s' % (w['line'], D_, w['primes'], w['n0'], w['pattern'], w['value'],
                                                                         w['minus'], ' CONTROL' if w['control'] else ''))


def selftest(*a):
    """roots_mod against a brute count over every residue, on the cubics of the box |a|, |b|, |c| <= 3 whose discriminant is none of the
    sixteen rows', at the primes below 60; and cubic_disc against the product of the root differences' squares at three cubics with
    integer roots."""
    keep = set(WALK) | set(CONTROL_ROWS)
    bad, n = [], 0
    for a_ in range(-3, 4):
        for b_ in range(-3, 4):
            for c_ in range(-3, 4):
                if cubic_disc(a_, b_, c_) in keep:
                    continue
                for p in CG.primes_upto(59):
                    n += 1
                    brute = sum(1 for x in range(p) if (x ** 3 + a_ * x * x + b_ * x + c_) % p == 0)
                    if roots_mod((a_, b_, c_), p) != brute:
                        bad.append(((a_, b_, c_), p))
    dd = []
    for rs in ((1, 2, 3), (0, -1, 4), (-2, -2, 5)):
        r1_, r2_, r3_ = rs
        a_, b_, c_ = -(r1_ + r2_ + r3_), r1_ * r2_ + r1_ * r3_ + r2_ * r3_, -(r1_ * r2_ * r3_)
        dd.append(cubic_disc(a_, b_, c_) == ((r1_ - r2_) * (r1_ - r3_) * (r2_ - r3_)) ** 2)
    print('### SELFTEST: roots_mod against the brute count at %d cases, mismatches %d %s ; cubic_disc against the root differences %s -- %s' % (
        n, len(bad), bad[:5], dd, 'AS WANTED' if not bad and all(dd) else '### NOT AS WANTED'))


def _put(name, data):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(parse=parse, selftest=selftest, controls=controls, walk=walk).get(route)
    if fn is None:
        sys.exit('usage: b755_coeffs.py parse | selftest | controls [dry] | walk [dry]')
    fn(*sys.argv[2:])
