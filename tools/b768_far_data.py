# -*- coding: utf-8 -*-
"""tools/b768_far_data.py -- (R378)(4)(b): L9c2'S DATA, THE FAR SUM'S COEFFICIENT OF EACH log n AND ITS CONSTANT, FROM THE KERNEL'S OWN FILES.

The far sum, collected by lag (far_lags of SIDEExplicitFormula/Window/FarLags.lean), reads the convolution sums autoD against farK; each
term of farK is lamT k at an integer shift c >= 0, which FarClosed.lean writes as lA k c log(1 + c) + lB k c log c + lG k c (lamT_at).
lA, lB and lG are polynomials in c: lamW's rows (SIDEExplicitFormula/Window/ArchLam.lean, read from the kernel's working tree, its blob
read equal at the branch's base and at HEAD) against fA, fB and fG (FarClosed.lean, their definition lines read equal to the forms this
tool computes). This tool writes them with one common denominator farDEN as integer polynomials pA, pB and pG, and the coefficient of
log n times 6 farDEN, farW n, read at the window of autoD from the place 16360 + n, n = 0 to 16369, and the constant's terms gW c,
c = 0 to 16368; the kernel checks each place by winOK (WinCheck.lean) in groups of 4,096. The convolution sums are those of
tools/b768_packed_data.py's full_data over Coeffs.lean (its blob read equal at the base and at HEAD), the list the kernel's autoD
flattens. Nothing of the window is printed: counts, lengths in decimal digits, truth values and sha256 digests alone. Each generated
Lean file is written into the kernel's working tree and edited by no hand; this tool commits nothing and dispatches nothing.

  dry | write   SIDEExplicitFormula/Window/FarPoly.lean (farDEN, pA, pB, pG, lA_poly, lB_poly, lG_poly), FarNum0.lean to FarNum3.lean
                and FarG0.lean to FarG3.lean (the data in chunks of 256, each group of 16 chunks checked by winOK at the window of autoD
                by decide +kernel, with its length), FarJoin.lean (the joined lists, their lengths and the joined checks)
  control       the tool's own controls, planted and printed
"""
import ast
import hashlib
import io
import os
import re
import sys
import time
from fractions import Fraction
from math import lcm

T = os.path.dirname(os.path.abspath(__file__))
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
import b768_packed_data as PD     # noqa: E402  (read_coeffs, full_data, text_checks, lean_list, the kernel's folder and base)

NL = '\n'
KPATH = PD.KPATH
ARCHLAM = 'SIDEExplicitFormula/Window/ArchLam.lean'
FARCLOSED = 'SIDEExplicitFormula/Window/FarClosed.lean'
DIR = 'SIDEExplicitFormula/Window/'
W0 = 16360          # ### the window of farW n opens at the place 16360 + n of autoD (aKM k m + n - 1 = 16360 + n + (3 + m - k))
N_NUM = 16370       # ### n = 0 to 16369: the far sum's log n, n <= 32730 - aKM k m - 1 + 1 at aKM >= 16361
N_GAM = 16369       # ### c = 0 to 16368: the constant's terms, the shift padded to 16369 places
GROUP = 4096        # ### 16 chunks of 256 a kernel evaluation, within the seat's 4,100 (KT_CAP)
CHUNK = 256
BW = [1, -4, 6, -4, 1]   # ### KappaClosed.lean's bw, read against its definition line by the control
FORMS = {   # ### FarClosed.lean's definition lines this tool computes, read equal before any write
    'fA': 'noncomputable def fA (l : ℕ) (c : ℝ) : ℝ := (1 - (-c) ^ (l + 1)) / ((l : ℝ) + 1)',
    'fB': 'noncomputable def fB (l : ℕ) (c : ℝ) : ℝ := (-c) ^ (l + 1) / ((l : ℝ) + 1)',
    'fG': '  -(∑ m ∈ Finset.range (l + 1), (-c) ^ m / (((l + 1 : ℕ) : ℝ) - m)) / ((l : ℝ) + 1)',
    'lA': 'noncomputable def lA (k : ℕ) (c : ℝ) : ℝ := ∑ l : Fin 7, lamW k c l * fA l c',
    'lB': 'noncomputable def lB (k : ℕ) (c : ℝ) : ℝ := ∑ l : Fin 7, lamW k c l * fB l c',
    'lG': 'noncomputable def lG (k : ℕ) (c : ℝ) : ℝ := ∑ l : Fin 7, lamW k c l * fG l c',
    'aKM': 'def aKM (k m : ℕ) : ℕ := 16364 + m - k',
}
BW_LINES = ['def bw : ℕ → ℤ', '  | 0 => 1', '  | 1 => -4', '  | 2 => 6', '  | 3 => -4', '  | 4 => 1', '  | _ => 0']


# ---------------------------------------------------------------- polynomials in c with rational coefficients

def padd(p, q):
    r = dict(p)
    for d, v in q.items():
        r[d] = r.get(d, 0) + v
    return {d: v for d, v in r.items() if v != 0}


def pmul(p, q):
    r = {}
    for d1, v1 in p.items():
        for d2, v2 in q.items():
            r[d1 + d2] = r.get(d1 + d2, 0) + v1 * v2
    return {d: v for d, v in r.items() if v != 0}


def pconst(v):
    v = Fraction(v)
    return {0: v} if v != 0 else {}


def pscale(p, s):
    return {d: v * s for d, v in p.items() if v * s != 0}


def ppow(p, n):
    r = pconst(1)
    for _ in range(n):
        r = pmul(r, p)
    return r


X = {1: Fraction(1)}
NEGX = {1: Fraction(-1)}


def peval(p, x):
    return sum(v * Fraction(x) ** d for d, v in p.items())


def ev_ast(node):
    """an entry of lamW's rows: integers, c, +, -, *, / by a constant, ^ by a natural, unary minus; anything else refused"""
    if isinstance(node, ast.Expression):
        return ev_ast(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return pconst(node.value)
    if isinstance(node, ast.Name) and node.id == 'c':
        return dict(X)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return pscale(ev_ast(node.operand), -1)
    if isinstance(node, ast.BinOp):
        a = ev_ast(node.left)
        if isinstance(node.op, ast.Pow):
            if not (isinstance(node.right, ast.Constant) and isinstance(node.right.value, int) and node.right.value >= 0):
                raise ValueError('a power not by a natural')
            return ppow(a, node.right.value)
        b = ev_ast(node.right)
        if isinstance(node.op, ast.Add):
            return padd(a, b)
        if isinstance(node.op, ast.Sub):
            return padd(a, pscale(b, -1))
        if isinstance(node.op, ast.Mult):
            return pmul(a, b)
        if isinstance(node.op, ast.Div):
            if set(b) - {0} or not b:
                raise ValueError('a division by a non-constant')
            return pscale(a, 1 / b[0])
    raise ValueError('a form outside the grammar: %s' % type(node).__name__)


def kgit(*a):
    return PD.git(*a)


def read_lamw():
    """lamW's four rows from ArchLam.lean, the blob read equal at the base and at HEAD; the lines of the definition printed"""
    p = os.path.join(KPATH, ARCHLAM)
    blob = kgit('hash-object', p)
    at_base = kgit('rev-parse', '%s:%s' % (PD.BASE_REV, ARCHLAM))
    at_head = kgit('rev-parse', 'HEAD:%s' % ARCHLAM)
    text = open(p, 'rb').read().decode('utf-8').replace('\r\n', '\n')
    lines = text.split('\n')
    start = next((i for i, l in enumerate(lines) if l.startswith('noncomputable def lamW : ℕ → ℝ → Fin 7 → ℝ')), None)
    end = next((i for i in range(start or 0, len(lines)) if lines[i].strip() == '| _, _ => fun _ => 0'), None) if start is not None else None
    rows = {}
    if start is not None and end is not None:
        block = ' '.join(l.strip() for l in lines[start + 1:end])
        for k, body in re.findall(r'\|\s*(\d)\s*,\s*c\s*=>\s*!\[(.*?)\]', block):
            ents = [e.strip() for e in body.split(',')]
            rows[int(k)] = [ev_ast(ast.parse(e.replace('^', '**'), mode='eval')) for e in ents]
    rep = dict(blob=blob, equal=(blob == at_base == at_head), start=(start + 1 if start is not None else None),
               end=(end + 1 if end is not None else None), rows=sorted(rows), widths=[len(rows[k]) for k in sorted(rows)])
    return rows, rep


def read_forms():
    """FarClosed.lean's definition lines and KappaClosed.lean's bw, each read equal to the form this tool computes"""
    fc = open(os.path.join(KPATH, FARCLOSED), 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
    kc = open(os.path.join(KPATH, DIR + 'KappaClosed.lean'), 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
    got = dict((k, v in fc) for k, v in FORMS.items())
    got['bw'] = any(kc[i:i + len(BW_LINES)] == BW_LINES for i in range(len(kc)))
    return got


def fAp(l):
    return pscale(padd(pconst(1), pscale(ppow(NEGX, l + 1), -1)), Fraction(1, l + 1))


def fBp(l):
    return pscale(ppow(NEGX, l + 1), Fraction(1, l + 1))


def fGp(l):
    s = {}
    for m in range(l + 1):
        s = padd(s, pscale(ppow(NEGX, m), Fraction(1, (l + 1) - m)))
    return pscale(s, Fraction(-1, l + 1))


def polys(rows):
    out = {}
    for name, f in (('A', fAp), ('B', fBp), ('G', fGp)):
        for k in range(4):
            acc = {}
            for l in range(7):
                acc = padd(acc, pmul(rows[k][l], f(l)))
            out[(name, k)] = acc
    den = 1
    for p in out.values():
        for v in p.values():
            den = lcm(den, v.denominator)
    ip = {}
    for key, p in out.items():
        q = pscale(p, den)
        assert all(v.denominator == 1 for v in q.values())
        ip[key] = [int(q.get(d, 0)) for d in range(max(q) + 1)] if q else [0]
    return out, den, ip


def horner_eval(cs, x):
    v = 0
    for a in reversed(cs):
        v = v * x + a
    return v


def lit(v):
    return str(v) if v >= 0 else '(%d)' % v


def horner_text(cs):
    while len(cs) > 1 and cs[-1] == 0:
        cs = cs[:-1]
    s = lit(cs[-1])
    for a in reversed(cs[:-1]):
        s = '(%s) * x + %s' % (s, lit(a))
    return s


# ---------------------------------------------------------------- the data

def windows(D, ip):
    get = lambda i: D[i] if 0 <= i < len(D) else 0

    def sm(o, base):
        return sum(BW[m] * get(base + o + m) for m in range(5))

    def farW(n):
        base = W0 + n
        nm1 = n - 1 if n >= 1 else 0
        return sum(horner_eval(ip[('A', k)], nm1) * sm(3 - k, base) + horner_eval(ip[('B', k)], n) * sm(4 - k, base) for k in range(4))

    def gW(c):
        base = W0 + c
        return sum(horner_eval(ip[('G', k)], c) * sm(4 - k, base) for k in range(4))

    def farD(n):   # ### the direct reading at aKM k m = 16364 + m - k, n >= 1
        return sum(BW[m] * (horner_eval(ip[('A', k)], n - 1) * get(16364 + m - k + n - 1) + horner_eval(ip[('B', k)], n) * get(16364 + m - k + n))
                   for k in range(4) for m in range(5))

    def gD(c):
        return sum(BW[m] * horner_eval(ip[('G', k)], c) * get(16364 + m - k + c) for k in range(4) for m in range(5))
    num = [farW(n) for n in range(N_NUM)]
    gam = [gW(c) for c in range(N_GAM)]
    chk = dict(num_direct=all(num[n] == farD(n) for n in range(1, N_NUM)),
               gam_direct=all(gam[c] == gD(c) for c in range(N_GAM)),
               past_list=(W0 + N_NUM - 1 + 8 >= len(D)),
               lengths=(len(num) == N_NUM and len(gam) == N_GAM))
    return num, gam, chk


def groups(xs):
    return [xs[g:g + GROUP] for g in range(0, len(xs), GROUP)]


def win_expr(g):
    e = '(autoD.drop %d)' % W0
    for _ in range(g):
        e = '(%s.drop %d)' % (e, GROUP)
    return e


def n_expr(g):
    return '0' if g == 0 else '(%s)' % ' + '.join(['0'] + [str(GROUP)] * g)


def _ns(body):
    return ['namespace SIDEExplicitFormula', 'namespace Window', ''] + body + ['end Window', 'end SIDEExplicitFormula', '']


def head(doc, blob):
    return ['/-!', doc, '', 'Written by relay tools/b768_far_data.py from the kernel`s own files (ArchLam.lean`s blob %s and Coeffs.lean`s);' % blob[:16],
            'edited by no hand.', '-/', '']


def texts(den, ip, num, gam, blob):
    out = {}
    P = ['/-- The common denominator of the coefficients of `lA`, `lB` and `lG`. -/', 'def farDEN : ℕ := %d' % den, '']
    for nm, doc in (('A', 'lA'), ('B', 'lB'), ('G', 'lG')):
        P += ['/-- `farDEN * %s k c` as a polynomial in `c` with integer coefficients. -/' % doc, 'def p%s : ℕ → ℤ → ℤ' % nm]
        for k in range(4):
            P.append('  | %d, x => %s' % (k, horner_text(ip[(nm, k)])))
        P += ['  | _, _ => 0', '']
    for nm, doc, f in (('A', 'lA', 'fA'), ('B', 'lB', 'fB'), ('G', 'lG', 'fG')):
        P += ['theorem %s_poly (k : ℕ) (hk : k ≤ 3) (c : ℕ) : %s k (c : ℝ) = (p%s k (c : ℤ) : ℝ) / (farDEN : ℝ) := by' % (doc, doc, nm),
              '  interval_cases k <;>',
              '    simp only [%s, lamW, %s, p%s, farDEN, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero,' % (doc, f, nm),
              '      Matrix.cons_val_succ, Fin.val_zero, Fin.val_succ, Finset.sum_range_succ, Finset.sum_range_zero] <;>',
              '    push_cast <;>', '    ring', '']
    out['FarPoly'] = (['import SIDEExplicitFormula.Window.FarClosed', ''] +
                      head('# L9c2: the closed forms` coefficients `lA`, `lB` and `lG` as integer polynomials over one denominator', blob) + _ns(P))
    for letter, data, fn, chk, base in (('Num', num, 'farW', 'far_ok', 'farNG'), ('G', gam, 'gW', 'gam_ok', 'farGG')):
        for g, part in enumerate(groups(data)):
            L = []
            cks = [part[i:i + CHUNK] for i in range(0, len(part), CHUNK)]
            pre = 'fn' if letter == 'Num' else 'fg'
            for j, c in enumerate(cks):
                lo = g * GROUP + j * CHUNK
                L += PD.lean_list('%sD%d%02d' % (pre, g, j), 'The places %d to %d.' % (lo, lo + len(c) - 1), c)
            L += ['/-- The places %d to %d. -/' % (g * GROUP, g * GROUP + len(part) - 1),
                  'def %s%d : List ℤ := %s' % (base, g, ' ++ '.join('%sD%d%02d' % (pre, g, j) for j in range(len(cks)))), '',
                  'theorem %s%d_len : %s%d.length = %d := by decide +kernel' % (base, g, base, g, len(part)), '',
                  'set_option maxHeartbeats 0 in',
                  'theorem %s%d : winOK %s %s %s %s%d = true := by decide +kernel' % (chk, g, fn, win_expr(g), n_expr(g), base, g), '']
            what = 'the coefficient of `log n` times `6 * farDEN`' if letter == 'Num' else 'the constant`s terms times `6 * farDEN`'
            out['Far%s%d' % (letter, g)] = (['import SIDEExplicitFormula.Window.FarWin', 'import SIDEExplicitFormula.Window.AutoConv', ''] +
                                            head('# L9c2: %s, the places %d to %d, checked at the window of `autoD`' % (what, g * GROUP, g * GROUP + len(part) - 1), blob) + _ns(L))
    J = []
    for nm, base, fn, chk, n, gl in (('farNumL', 'farNG', 'farW', 'far_ok', N_NUM, groups(num)), ('farGL', 'farGG', 'gW', 'gam_ok', N_GAM, groups(gam))):
        lens = [len(x) for x in gl]
        J += ['/-- The joined list, %d places. -/' % n, 'def %s : List ℤ := %s0 ++ (%s1 ++ (%s2 ++ %s3))' % (nm, base, base, base, base), '',
              'theorem %s_len : %s.length = %d := by' % (nm, nm, n), '  unfold %s' % nm,
              '  simp only [List.length_append, %s]' % ', '.join('%s%d_len' % (base, g) for g in range(4)), '',
              'theorem %s_all : winOK %s (autoD.drop %d) 0 %s = true := by' % (nm, fn, W0, nm), '  unfold %s' % nm,
              '  rw [winOK_append, winOK_append, winOK_append, %s, %s]' % (', '.join('%s%d_len' % (base, g) for g in range(3)),
                                                                      ', '.join('%s%d' % (chk, g) for g in range(4))),
              '  all_goals rfl', '']
        assert sum(lens) == n
    out['FarJoin'] = (['import SIDEExplicitFormula.Window.FarNum%d' % g for g in range(4)] + ['import SIDEExplicitFormula.Window.FarG%d' % g for g in range(4)] + [''] +
                      head('# L9c2: the joined lists of the far sum`s data and their checks at the window of `autoD`', blob) + _ns(J))
    return dict((k, NL.join(v)) for k, v in out.items())


def decl_lines(t):
    out = []
    for i, l in enumerate(t.split(NL), 1):
        m = re.match(r'(theorem|def) (\w+)', l)
        if m and not re.match(r'f[ng]D\d{3}$', m.group(2)):
            out.append('%s:%d' % (m.group(2), i))
    return out


def build(verbose=True):
    rows, lrep = read_lamw()
    forms = read_forms()
    lists, crep = PD.read_coeffs()
    if verbose:
        print('  ArchLam.lean: blob %s, equal at the base and HEAD %s ; lamW at :%s-:%s, rows %s of widths %s' % (
            lrep['blob'][:12], lrep['equal'], lrep['start'], lrep['end'], lrep['rows'], lrep['widths']))
        print('  FarClosed.lean`s and KappaClosed.lean`s definition lines read equal to the forms computed: %s' % ' ; '.join('%s %s' % kv for kv in forms.items()))
        print('  Coeffs.lean: blob %s, EQUAL %s ; lists %d ; numerators %d' % (crep['blob'][:12], crep['equal'], crep['chunks'], crep['total']))
    ok_in = (lrep['equal'] and lrep['rows'] == [0, 1, 2, 3] and lrep['widths'] == [7, 7, 7, 7] and all(forms.values())
             and crep['equal'] and crep['chunks'] == 64 and crep['total'] == PD.N_ALL)
    if not ok_in:
        return None
    out, den, ip = polys(rows)
    t0 = time.time()
    fd, fchk = PD.full_data(lists)
    num, gam, wchk = windows(fd['D'], ip)
    pchk = dict(integer=all(isinstance(v, int) for cs in ip.values() for v in cs),
                degrees=max(len(cs) - 1 for cs in ip.values()),
                at_points=all(Fraction(horner_eval(ip[key], x), den) == peval(out[key], x) for key in ip for x in (0, 1, 2, 7, 16368)))
    if verbose:
        print('  the polynomials: 12, integer %s, the largest degree %d, read against the rational forms at five points %s ; farDEN %d digits' % (
            pchk['integer'], pchk['degrees'], pchk['at_points'], len(str(den))))
        print('  the convolution sums` checks (%.1f s): %s' % (time.time() - t0, ' ; '.join('%s %s' % kv for kv in fchk.items())))
        print('  the windows` checks: %s ; the largest place %d digits (log n) and %d digits (the constant)' % (
            ' ; '.join('%s %s' % kv for kv in wchk.items()), max(len(str(abs(v))) for v in num), max(len(str(abs(v))) for v in gam)))
    ok = all(fchk.values()) and all(wchk.values()) and pchk['integer'] and pchk['at_points']
    return dict(ok=ok, den=den, ip=ip, num=num, gam=gam, blob=lrep['blob'], out=out, fd=fd)


def cmd_gen(mode):
    b = build()
    if b is None:
        sys.exit('### NOT WRITTEN: a source file is not read as the base holds it')
    tx = texts(b['den'], b['ip'], b['num'], b['gam'], b['blob'])
    ok = b['ok']
    for k in sorted(tx):
        tc = PD.text_checks(tx[k])
        good = not tc['decimal'] and not tc['barred'] and tc['import_first'] and tc['longest_list'] <= CHUNK
        ok = ok and good
        print('  %s.lean: lines %d, bytes %d, sha256 %s ; decimal literals %d ; barred words %d ; imports first %s ; the longest list %d -> %s' % (
            k, tc['lines'], tc['bytes'], tc['sha256'], tc['decimal'], tc['barred'], tc['import_first'], tc['longest_list'], 'OK' if good else 'REFUSED'))
        print('    declarations (name:line), the data chunks left out: %s' % ', '.join(decl_lines(tx[k])))
    if not ok:
        sys.exit('### NOT WRITTEN: a check failed')
    if mode != 'write':
        print('### DRY: nothing written')
        return
    for k, t in sorted(tx.items()):
        out = os.path.join(KPATH, DIR + k + '.lean')
        with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(t)
        back = open(out, 'rb').read()
        print('### WRITTEN %s%s.lean: %d bytes, sha256 %s, read back EQUAL %s' % (DIR, k, len(back), hashlib.sha256(back).hexdigest()[:16],
                                                                             back == t.encode('utf-8')))


def cmd_control():
    res = []

    def c(name, got, ok):
        res.append(ok)
        print('  (%d) %s: %s -> %s' % (len(res), name, got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    e = ev_ast(ast.parse('(3 / 2) * c ^ 2 + (-1)'.replace('^', '**'), mode='eval'))
    c('the entry grammar on a planted entry: (3 / 2) c^2 - 1 read at c = 2', peval(e, 2) == 5, peval(e, 2) == 5)
    try:
        ev_ast(ast.parse('c / c', mode='eval'))
        refused = False
    except ValueError:
        refused = True
    c('A PLANTED FAULT: a division by c, refused by the grammar', refused, refused)
    c('fA, fB and fG at l = 0: 1 + c, -c and -1, the forms of fPiece 0', (fAp(0), fBp(0), fGp(0)),
      fAp(0) == {0: 1, 1: 1} and fBp(0) == {1: -1} and fGp(0) == {0: -1})
    c('fG at l = 1 read at c = 0: -1/4, the value fG_zero gives (-1 / (l + 1)^2)', peval(fGp(1), 0), peval(fGp(1), 0) == Fraction(-1, 4))
    c('Horner`s text read back: the planted integer polynomial 5 - 3x + 2x^2 at x = 4', horner_eval([5, -3, 2], 4) == 25 and horner_text([5, -3, 2]) == '((2) * x + (-3)) * x + 5',
      horner_eval([5, -3, 2], 4) == 25 and horner_text([5, -3, 2]) == '((2) * x + (-3)) * x + 5')
    c('the windows` expressions as the assembly rewrites them', (win_expr(2), n_expr(2)),
      win_expr(2) == '(((autoD.drop 16360).drop 4096).drop 4096)' and n_expr(2) == '(0 + 4096 + 4096)')
    b = build(verbose=False)
    c('the sources read as the base holds them, the checks before a write (the direct readings at aKM, the polynomials at five points)',
      b is not None and b['ok'], b is not None and b['ok'])
    if b is not None:
        num2 = list(b['num'])
        num2[777] += 1
        D = b['fd']['D']
        get = lambda i: D[i] if 0 <= i < len(D) else 0
        direct = sum(BW[m] * (horner_eval(b['ip'][('A', k)], 776) * get(16364 + m - k + 776) + horner_eval(b['ip'][('B', k)], 777) * get(16364 + m - k + 777))
                     for k in range(4) for m in range(5))
        c('A PLANTED FAULT: one place of the log n data moved by 1, the direct reading at aKM reads it', num2[777] == direct, num2[777] != direct)
        tx = texts(b['den'], b['ip'], b['num'], b['gam'], b['blob'])
        tcs = [PD.text_checks(tx[k]) for k in sorted(tx)]
        c('the ten texts (no decimal literal, no barred word, imports first, lists of 256 at most)',
          (len(tx), sum(t['decimal'] + t['barred'] for t in tcs), all(t['import_first'] for t in tcs), max(t['longest_list'] for t in tcs)),
          len(tx) == 10 and not sum(t['decimal'] + t['barred'] for t in tcs) and all(t['import_first'] for t in tcs) and max(t['longest_list'] for t in tcs) <= CHUNK)
        c('the groups: 4 of the log n data (4,096 x 3 and 4,082) and 4 of the constant (4,096 x 3 and 4,081)',
          ([len(x) for x in groups(b['num'])], [len(x) for x in groups(b['gam'])]),
          [len(x) for x in groups(b['num'])] == [4096, 4096, 4096, 4082] and [len(x) for x in groups(b['gam'])] == [4096, 4096, 4096, 4081])
    print('### THE TOOL`S CONTROLS: %d OF %d AS WANTED' % (sum(res), len(res)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        cmd_control()
    elif a[:1] in (['dry'], ['write']):
        cmd_gen(a[0])
    else:
        sys.exit('usage: b768_far_data.py control | dry | write')
