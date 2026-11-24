# -*- coding: utf-8 -*-
"""tools/b768_band_data.py -- (R378)(4)(b): L9c3'S DATA, THE BAND'S COEFFICIENT OF EACH log n AND ITS CONSTANT, FROM THE KERNEL'S OWN FILES.

The band of archJ_basis_local (SIDEExplicitFormula/Window/ArchBandLocal.lean) is the sum over the pairs i, j of the window's indices
within three knots of coeff i * coeff j * lgI i (i - j). ArchClosed.lean writes lgI a d, d = 0 to 3, as sums of its vectors bandV k d
against fPiece l (k + a) (lgI_closed_zero to lgI_closed_three) and lgI a (-d) as lgI (a + d) d (lgI_neg); FarClosed.lean writes
fPiece l c, c > 0, as fA l c log (1 + c) + fB l c log c + fG l c (fPiece_form_pos). So the band is sixteen blocks, block b reading the
pair i, i + bD b - 3 against bVec (bVi b) at i + bS b. This tool reads the ten vectors from ArchClosed.lean (its blob read equal at
the branch's base and at HEAD, each vector read against the product of the two cubic pieces pieceP k * pieceP (k + d) of the same
file, and the four closed forms and lgI_neg read present at their statements), writes bVec v against fA, fB and fG over one
denominator bandDEN as integer polynomials bpA, bpB and bpG, and the coefficient of log n times bandDEN and the square of the
numerators' scale, bandW n, read at the window of coeffPad (twenty zeros, then the numerators of Coeffs.lean, its blob read equal at
the base and HEAD) from its place n, n = 0 to 16384, and the constant's terms gWb c, c = 0 to 16383. Each place is read again
directly, pair by pair, from lgI's closed forms and lgI_neg, with no block, no window and no padding; the two readings are equal at
every place before any write. The kernel checks each place by winOK (WinCheck.lean), each chunk of 64 places its own declaration (some
thirty polynomials and products a place, against the far sum's twelve: half the far sum's chunk), the chunks joined by winOK_chunk at
literal places, a group of 4,096 a file (4,097 the last of the log n data). Nothing of the window is printed: counts, lengths in
decimal digits, truth values and sha256 digests alone. Each generated Lean file is written into the kernel's working tree and edited
by no hand; this tool commits nothing and dispatches nothing.

  dry | write   SIDEExplicitFormula/Window/BandPoly.lean (bVec, bqA, bqB, bqG, bandDEN, bpA, bpB, bpG, bqA_poly, bqB_poly, bqG_poly),
                BandWin.lean (coeffPad, coeffPad_eq, bD, bS, bVi, band_table, bandW, gWb, bandW_eq, gWb_eq), BandNum0.lean to
                BandNum3.lean and BandG0.lean to BandG3.lean (the data in chunks of 64, each chunk checked by winOK at its window of
                coeffPad by its own decide +kernel, each group joined by winOK_chunk, with its length), BandJoin.lean (the joined
                lists, their lengths and the joined checks); at `write`, print_targets.txt given the generated theorems after
                far_final
  control       the tool's own controls, planted and printed
"""
import ast
import hashlib
import io
import os
import re
import sys
import time
from collections import Counter
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
import b768_packed_data as PD     # noqa: E402  (read_coeffs, text_checks, lean_list, the kernel's folder and base)
import b768_far_data as FD        # noqa: E402  (the polynomials, fA/fB/fG and their forms, Horner's text, rjoin, the option's order)

NL = '\n'
KPATH = PD.KPATH
ARCHCLOSED = 'SIDEExplicitFormula/Window/ArchClosed.lean'
ARCHBAND = 'SIDEExplicitFormula/Window/ArchBandLocal.lean'
DIR = FD.DIR
N_NUM = 16385       # ### n = 0 to 16384: c = i + s <= 16380 + 3 = 16383, and log (1 + c) read at n = c + 1
N_GAM = 16384       # ### c = 0 to 16383
GROUP = 4096        # ### a file's places: 64 chunks (65 the last of the log n data, its last chunk one place)
CHUNK = 64          # ### one kernel evaluation a declaration: 64 places
PAD = 20            # ### coeffPad: twenty zeros, then coeffList, so coeffPad[m + 4] = coeffInt m for every m
ANCHOR = 'SIDEExplicitFormula.Window.far_final'   # ### print_targets.txt: the generated theorems entered after this line
VORDER = ['03', '02', '12', '01', '11', '21', '00', '10', '20', '30']   # ### bVec v = bandV<k><d>, v = 0 to 9
CLOSED = {   # ### lgI a d, d = 0 to 3: (the shift k of fPiece l (k + a), the vector), as lgI_closed_zero to lgI_closed_three read
    0: [(0, '00'), (1, '10'), (2, '20'), (3, '30')],
    1: [(0, '01'), (1, '11'), (2, '21')],
    2: [(0, '02'), (1, '12')],
    3: [(0, '03')],
}
FORMS = [   # ### ArchClosed.lean's statement lines that CLOSED and lgI_neg's use read, each read present before any write
    'lgI a 0 = (∑ l : Fin 7, bandV00 l * fPiece l a) + (∑ l : Fin 7, bandV10 l * fPiece l (1 + a)) +',
    '(∑ l : Fin 7, bandV20 l * fPiece l (2 + a)) + ∑ l : Fin 7, bandV30 l * fPiece l (3 + a) := by',
    'lgI a 1 = (∑ l : Fin 7, bandV01 l * fPiece l a) + (∑ l : Fin 7, bandV11 l * fPiece l (1 + a)) +',
    '∑ l : Fin 7, bandV21 l * fPiece l (2 + a) := by',
    'lgI a 2 = (∑ l : Fin 7, bandV02 l * fPiece l a) + ∑ l : Fin 7, bandV12 l * fPiece l (1 + a) := by',
    'lgI a 3 = ∑ l : Fin 7, bandV03 l * fPiece l a := by',
    'theorem lgI_neg (a d : ℝ) : lgI a (-d) = lgI (a + d) d := by',
]
BAND_FORM = 'coeff i * coeff j * lgI i ((i : ℝ) - j)) -'   # ### archJ_basis_local's band, read present in ArchBandLocal.lean
TABLE = [(0, 0, 0), (1, 0, 1), (1, 1, 2), (2, 0, 3), (2, 1, 4), (2, 2, 5), (3, 0, 6), (3, 1, 7), (3, 2, 8), (3, 3, 9),
         (4, 1, 3), (4, 2, 4), (4, 3, 5), (5, 2, 1), (5, 3, 2), (6, 3, 0)]   # ### (bD, bS, bVi) of each block, the plan's table


# ---------------------------------------------------------------- the sources

def const(e):
    """a vector's entry: a rational constant by the far tool's grammar, anything with c refused"""
    p = FD.ev_ast(ast.parse(e.replace('^', '**'), mode='eval'))
    if set(p) - {0}:
        raise ValueError('a vector entry not constant')
    return Fraction(p.get(0, 0))


def blob_equal(path):
    blob = FD.kgit('hash-object', os.path.join(KPATH, path))
    return blob, blob == FD.kgit('rev-parse', '%s:%s' % (PD.BASE_REV, path)) == FD.kgit('rev-parse', 'HEAD:%s' % path)


def read_band():
    """the ten vectors bandV k d and the four pieces pieceP m of ArchClosed.lean, its blob read equal at the base and at HEAD; the
    closed forms' statement lines and archJ_basis_local's band read present"""
    blob, equal = blob_equal(ARCHCLOSED)
    lines = open(os.path.join(KPATH, ARCHCLOSED), 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
    vec = {}
    for l in lines:
        m = re.match(r'noncomputable def bandV(\d)(\d) : Fin 7 → ℝ := !\[(.*)\]$', l)
        if m:
            vec[m.group(1) + m.group(2)] = [const(e.strip()) for e in m.group(3).split(',')]
    piece = {}
    start = next((i for i, l in enumerate(lines) if l.startswith('noncomputable def pieceP : ℕ → ℝ → ℝ')), None)
    if start is not None:
        for l in lines[start + 1:start + 6]:
            m = re.match(r'\s*\|\s*(\d), s => (.*)$', l)
            if m:
                body = re.sub(r'\bs\b', 'c', m.group(2)).replace('^', '**')
                piece[int(m.group(1))] = FD.ev_ast(ast.parse(body, mode='eval'))
    band_blob, band_equal = blob_equal(ARCHBAND)
    bl = open(os.path.join(KPATH, ARCHBAND), 'rb').read().decode('utf-8')
    rep = dict(blob=blob, equal=equal, vectors=sorted(vec), widths=sorted(set(len(v) for v in vec.values())), pieces=sorted(piece),
               forms=[any(f in l for l in lines) for f in FORMS], band_form=(BAND_FORM in bl), band_equal=band_equal)
    return vec, piece, rep


def products_ok(vec, piece):
    """each vector bandV k d read against pieceP k * pieceP (k + d), coefficient by coefficient"""
    out = {}
    for k in range(4):
        for d in range(4 - k):
            nm = '%d%d' % (k, d)
            v = vec.get(nm)
            want = dict((i, x) for i, x in enumerate(v) if x != 0) if v else None
            out[nm] = v is not None and len(v) == 7 and FD.pmul(piece[k], piece[k + d]) == want
    return out


def blocks(closed=CLOSED):
    """(D, s, v): the pair i, i + D - 3 has i - j = 3 - D; lgI i d for d >= 0 by its closed form at i + k, and lgI i (-e) = lgI (i + e) e
    (lgI_neg) at i + e + k"""
    out = []
    for D in range(7):
        d = 3 - D
        e = abs(d)
        for k, nm in closed[e]:
            out.append((D, k + (e if d < 0 else 0), VORDER.index(nm)))
    return out


def table_ok(blks):
    return len(blks) == 16 and all(s <= 3 and s <= D <= s + 3 and v <= 9 for D, s, v in blks)


# ---------------------------------------------------------------- the polynomials

def polys(vec):
    out = {}
    for name, f in (('A', FD.fAp), ('B', FD.fBp), ('G', FD.fGp)):
        for v, nm in enumerate(VORDER):
            acc = {}
            for l in range(7):
                acc = FD.padd(acc, FD.pscale(f(l), vec[nm][l]))
            out[(name, v)] = acc
    den = 1
    for p in out.values():
        for x in p.values():
            den = lcm(den, x.denominator)
    ip = {}
    for key, p in out.items():
        q = FD.pscale(p, den)
        assert all(x.denominator == 1 for x in q.values())
        ip[key] = [int(q.get(d, 0)) for d in range(max(q) + 1)] if q else [0]
    return out, den, ip


def name_polys(vec, den):
    """den times each vector against fA, fB and fG, by the vector's own name (the direct reading's polynomials, no bVec order)"""
    ipn = {}
    for name, f in (('A', FD.fAp), ('B', FD.fBp), ('G', FD.fGp)):
        for nm, V in vec.items():
            acc = {}
            for l in range(7):
                acc = FD.padd(acc, FD.pscale(f(l), V[l] * den))
            assert all(x.denominator == 1 for x in acc.values())
            ipn[(name, nm)] = [int(acc.get(d, 0)) for d in range(max(acc) + 1)] if acc else [0]
    return ipn


# ---------------------------------------------------------------- the data

def tables(blks):
    """each vector's window products, grouped: v -> Counter of the sorted index pairs, for log (1 + c) (A) and for log c (B)"""
    A = dict((v, Counter()) for v in range(10))
    B = dict((v, Counter()) for v in range(10))
    for D, s, v in blks:
        A[v][tuple(sorted((3 - s, D - s)))] += 1
        B[v][tuple(sorted((4 - s, D - s + 1)))] += 1
    return A, B


def padded(flat, pad=PAD):
    return [0] * pad + list(flat)


def windows(flat, ip, blks, pad=PAD):
    """bandW n and gWb c at the window of coeffPad from n (resp. c), grouped as the Lean text writes them; and the ungrouped block form
    bandW_eq states, read equal at every place"""
    P = padded(flat, pad)
    g = lambda i: P[i] if 0 <= i < len(P) else 0
    A, B = tables(blks)
    pv = dict(((nm, v), [FD.horner_eval(ip[(nm, v)], x) for x in range(N_NUM)]) for nm in 'ABG' for v in range(10))

    def prod(cnt, n):
        return sum(k * g(n + a) * g(n + b) for (a, b), k in cnt.items())
    num = []
    for n in range(N_NUM):
        m1 = n - 1 if n >= 1 else 0
        num.append(sum(pv[('A', v)][m1] * prod(A[v], n) + pv[('B', v)][n] * prod(B[v], n) for v in range(10)))
    gam = [sum(pv[('G', v)][c] * prod(B[v], c) for v in range(10)) for c in range(N_GAM)]

    def blockW(n):
        m1 = n - 1 if n >= 1 else 0
        return sum(g(n + 3 - s) * g(n + D - s) * pv[('A', v)][m1] + g(n + 4 - s) * g(n + D - s + 1) * pv[('B', v)][n] for D, s, v in blks)

    def blockG(c):
        return sum(g(c + 4 - s) * g(c + D - s + 1) * pv[('G', v)][c] for D, s, v in blks)
    chk = dict(grouped_num=all(num[n] == blockW(n) for n in range(N_NUM)), grouped_gam=all(gam[c] == blockG(c) for c in range(N_GAM)))
    return num, gam, chk


def direct(flat, ipn):
    """each place read pair by pair: lgI (i, i - j) = lgI (max (i, j), |i - j|) (lgI_neg), lgI (a, d) the sum over k <= 3 - d of
    bandV k d against fPiece l (k + a) (the closed forms), fPiece l c = fA log (1 + c) + fB log c + fG; no block, no window, no padding"""
    ci = lambda m: flat[m - 16] if 16 <= m <= 16380 else 0
    pre = {}
    for key, cs in ipn.items():
        pre[key] = [FD.horner_eval(cs, c) if 16 <= c else 0 for c in range(N_GAM)]
    num = [0] * N_NUM
    gam = [0] * N_GAM
    for i in range(16, 16381):
        for j in range(max(16, i - 3), min(16380, i + 3) + 1):
            w = ci(i) * ci(j)
            if not w:
                continue
            a, d = max(i, j), abs(i - j)
            for k in range(4 - d):
                nm, c = '%d%d' % (k, d), a + k
                num[c + 1] += w * pre[('A', nm)][c]
                num[c] += w * pre[('B', nm)][c]
                gam[c] += w * pre[('G', nm)][c]
    return num, gam


def band_groups(xs):
    """four groups of 4,096, the last taking the rest"""
    return [xs[0:GROUP], xs[GROUP:2 * GROUP], xs[2 * GROUP:3 * GROUP], xs[3 * GROUP:]]


def chain_rows(start, part, size):
    """(a, n, k) for each piece of a list from the place `start`: its window's place in coeffPad, its first place, its length"""
    return [(start + i, start + i, len(part[i:i + size])) for i in range(0, len(part), size)]


def chain_ok(rows, start, total):
    a, n, s = start, start, 0
    for ra, rn, k in rows:
        if ra != a or rn != n or k <= 0:
            return False
        a, n, s = a + k, n + k, s + k
    return s == total


def chain_proof(fn, base, names, rows, last):
    """the tactic lines joining the pieces' checks by winOK_chunk at literal places, the last piece's check closing it"""
    L = []
    for nm, (a, n, k), ck in zip(names[:-1], rows[:-1], last[:-1]):
        L.append('  refine winOK_chunk %s %s %s _ %d %d %d %d %d %s (by norm_num) (by norm_num) %s ?_' % (
            fn, base, nm, a, n, k, a + k, n + k, '(by decide +kernel)' if ck[1] is None else ck[1], ck[0]))
    L.append('  exact %s' % last[-1][0])
    return L


# ---------------------------------------------------------------- the texts

def head(doc, blob):
    return ['/-!', doc, '', 'Written by relay tools/b768_band_data.py from the kernel`s own files (ArchClosed.lean`s blob %s and Coeffs.lean`s);' % blob[:16],
            'edited by no hand.', '-/', '']


def wterm(cnt):
    ts = []
    for (a, b), k in sorted(cnt.items()):
        t = 'w.getD %d 0 * w.getD %d 0' % (a, b)
        ts.append(('%d * (%s)' % (k, t)) if k > 1 else t)
    return '(' + ' + '.join(ts) + ')'


def texts(den, ip, blks, num, gam, blob):
    out = {}
    vecs = ', '.join('bandV%s' % nm for nm in sorted(VORDER))
    P = ['/-- The band`s ten vectors of `ArchClosed.lean`, in the order its blocks read them (`bVi`). -/',
         'noncomputable def bVec : ℕ → Fin 7 → ℝ'] + ['  | %d => bandV%s' % (v, nm) for v, nm in enumerate(VORDER)] + ['  | _ => fun _ => 0', '']
    for nm, f in (('A', 'fA'), ('B', 'fB'), ('G', 'fG')):
        P += ['/-- `bVec v` against `%s`. -/' % f, 'noncomputable def bq%s (v : ℕ) (c : ℝ) : ℝ := ∑ l : Fin 7, bVec v l * %s l c' % (nm, f), '']
    P += ['/-- The common denominator of the coefficients of `bqA`, `bqB` and `bqG`. -/', 'def bandDEN : ℕ := %d' % den, '']
    for nm in 'ABG':
        P += ['/-- `bandDEN * bq%s v c` as a polynomial in `c` with integer coefficients. -/' % nm, 'def bp%s : ℕ → ℤ → ℤ' % nm]
        P += ['  | %d, x => %s' % (v, FD.horner_text(ip[(nm, v)])) for v in range(10)] + ['  | _, _ => 0', '']
    for nm, f in (('A', 'fA'), ('B', 'fB'), ('G', 'fG')):
        P += ['theorem bq%s_poly (v : ℕ) (hv : v ≤ 9) (c : ℕ) : bq%s v (c : ℝ) = (bp%s v (c : ℤ) : ℝ) / (bandDEN : ℝ) := by' % (nm, nm, nm),
              '  interval_cases v <;>',
              '    simp only [bq%s, bVec, %s, %s, bp%s, bandDEN, Fin.sum_univ_succ, Fin.sum_univ_zero,' % (nm, vecs, f, nm),
              '      Matrix.cons_val_zero, Matrix.cons_val_succ, Fin.val_zero, Fin.val_succ, Finset.sum_range_succ, Finset.sum_range_zero] <;>',
              '    push_cast <;>', '    ring', '']
    out['BandPoly'] = (['import SIDEExplicitFormula.Window.FarClosed', ''] +
                       head('# L9c3: the band`s vectors against `fA`, `fB` and `fG` as integer polynomials over one denominator', blob) + FD._ns(P))
    A, B = tables(blks)
    W = ['/-- The numerators of `Coeffs.lean` after twenty zeros, joined to the right, so that `coeffPad[m + 4] = coeffInt m`. -/',
         'def coeffPad : List ℤ := List.replicate 20 0 ++ (%s)' % FD.rjoin(['coeffChunk%02d' % i for i in range(64)]), '',
         'theorem coeffPad_eq : coeffPad = List.replicate 20 0 ++ coeffList := by', '  unfold coeffPad coeffList',
         '  simp only [List.append_assoc]', '']
    for nm, idx, doc in (('bD', 0, 'The block`s pair: `i, i + bD b - 3`.'), ('bS', 1, 'The block`s shift: its vector read at `i + bS b`.'),
                         ('bVi', 2, 'The block`s vector: `bVec (bVi b)`.')):
        W += ['/-- %s -/' % doc, 'def %s : ℕ → ℕ' % nm] + ['  | %d => %d' % (b, blk[idx]) for b, blk in enumerate(blks)] + ['  | _ => 0', '']
    W += ['theorem band_table (b : ℕ) (hb : b < 16) : bS b ≤ 3 ∧ bS b ≤ bD b ∧ bD b ≤ bS b + 3 ∧ bVi b ≤ 9 := by',
          '  interval_cases b <;> first | decide | (simp only [bS, bD, bVi]; done) | (simp only [bS, bD, bVi]; omega)', '']
    W += ['/-- The coefficient of `log n` in the band, times `bandDEN` and the square of the numerators` scale, read at the window `w`. -/',
          'def bandW (n : ℕ) (w : List ℤ) : ℤ :=']
    W += [' +\n'.join('  bpA %d ((n - 1 : ℕ) : ℤ) * %s + bpB %d (n : ℤ) * %s' % (v, wterm(A[v]), v, wterm(B[v])) for v in range(10)), '']
    W += ['/-- The band`s constant`s term at the place `c`, times `bandDEN` and the square of the numerators` scale, read at the window `w`. -/',
          'def gWb (c : ℕ) (w : List ℤ) : ℤ :=']
    W += [' +\n'.join('  bpG %d (c : ℤ) * %s' % (v, wterm(B[v])) for v in range(10)), '']
    W += ['theorem bandW_eq (n : ℕ) (w : List ℤ) :',
          '    bandW n w = ∑ b ∈ Finset.range 16, (w.getD (3 - bS b) 0 * w.getD (bD b - bS b) 0 * bpA (bVi b) ((n - 1 : ℕ) : ℤ) +',
          '      w.getD (4 - bS b) 0 * w.getD (bD b - bS b + 1) 0 * bpB (bVi b) (n : ℤ)) := by',
          '  simp only [bandW, Finset.sum_range_succ, Finset.sum_range_zero, zero_add, bS, bD, bVi]', '  ring', '',
          'theorem gWb_eq (c : ℕ) (w : List ℤ) :',
          '    gWb c w = ∑ b ∈ Finset.range 16, w.getD (4 - bS b) 0 * w.getD (bD b - bS b + 1) 0 * bpG (bVi b) (c : ℤ) := by',
          '  simp only [gWb, Finset.sum_range_succ, Finset.sum_range_zero, zero_add, bS, bD, bVi]', '  ring', '']
    out['BandWin'] = (['import SIDEExplicitFormula.Window.BandPoly', 'import SIDEExplicitFormula.Window.WinCheck',
                       'import SIDEExplicitFormula.Window.Coeffs', ''] +
                      head('# L9c3: the band`s blocks, its coefficient of `log n` and its constant`s terms, read at a window of `coeffPad`', blob) + FD._ns(W))
    for letter, data, fn, chk, base, pre in (('Num', num, 'bandW', 'band_ok', 'bandNG', 'bn'), ('G', gam, 'gWb', 'bgam_ok', 'bandGG', 'bg')):
        for g, part in enumerate(band_groups(data)):
            L = []
            cks = [part[i:i + CHUNK] for i in range(0, len(part), CHUNK)]
            rows = chain_rows(g * GROUP, part, CHUNK)
            assert chain_ok(rows, g * GROUP, len(part)) and len(rows) == len(cks)
            names = ['%sD%d%02d' % (pre, g, j) for j in range(len(cks))]
            for j, c in enumerate(cks):
                lo = g * GROUP + j * CHUNK
                L += PD.lean_list(names[j], 'The places %d to %d.' % (lo, lo + len(c) - 1), c)
                L += ['set_option maxHeartbeats 0 in',
                      '/-- The places %d to %d checked at the window of `coeffPad` from its place %d. -/' % (lo, lo + len(c) - 1, rows[j][0]),
                      'theorem %s%d_%02d : winOK %s (coeffPad.drop %d) %d %s = true := by decide +kernel' % (chk, g, j, fn, rows[j][0], rows[j][1], names[j]), '']
            L += ['/-- The places %d to %d. -/' % (g * GROUP, g * GROUP + len(part) - 1),
                  'def %s%d : List ℤ := %s' % (base, g, FD.rjoin(names)), '',
                  'theorem %s%d_len : %s%d.length = %d := by decide +kernel' % (base, g, base, g, len(part)), '',
                  'theorem %s%d : winOK %s (coeffPad.drop %d) %d %s%d = true := by' % (chk, g, fn, g * GROUP, g * GROUP, base, g),
                  '  unfold %s%d' % (base, g)]
            L += chain_proof(fn, 'coeffPad', names, rows, [('%s%d_%02d' % (chk, g, j), None) for j in range(len(cks))]) + ['']
            what = 'the coefficient of `log n` times `bandDEN`' if letter == 'Num' else 'the constant`s terms times `bandDEN`'
            out['Band%s%d' % (letter, g)] = (['import SIDEExplicitFormula.Window.BandWin', ''] +
                                             head('# L9c3: %s, the places %d to %d, checked at the window of `coeffPad`' % (what, g * GROUP, g * GROUP + len(part) - 1), blob) + FD._ns(L))
    J = []
    for nm, base, fn, chk, n, gl in (('bandNumL', 'bandNG', 'bandW', 'band_ok', N_NUM, band_groups(num)), ('bandGL', 'bandGG', 'gWb', 'bgam_ok', N_GAM, band_groups(gam))):
        lens = [len(x) for x in gl]
        grows = [(g * GROUP, g * GROUP, lens[g]) for g in range(4)]
        assert chain_ok(grows, 0, n) and sum(lens) == n
        gnames = ['%s%d' % (base, g) for g in range(4)]
        J += ['/-- The joined list, %d places. -/' % n, 'def %s : List ℤ := %s' % (nm, FD.rjoin(gnames)), '',
              'theorem %s_len : %s.length = %d := by' % (nm, nm, n), '  unfold %s' % nm,
              '  simp only [List.length_append, %s] <;> norm_num' % ', '.join('%s%d_len' % (base, g) for g in range(4)), '',
              'theorem %s_all : winOK %s (coeffPad.drop 0) 0 %s = true := by' % (nm, fn, nm), '  unfold %s' % nm]
        J += chain_proof(fn, 'coeffPad', gnames, grows, [('%s%d' % (chk, g), '%s%d_len' % (base, g)) for g in range(4)]) + ['']
    out['BandJoin'] = (['import SIDEExplicitFormula.Window.BandNum%d' % g for g in range(4)] + ['import SIDEExplicitFormula.Window.BandG%d' % g for g in range(4)] + [''] +
                       head('# L9c3: the joined lists of the band`s data and their checks at the window of `coeffPad`', blob) + FD._ns(J))
    return dict((k, NL.join(v)) for k, v in out.items())


def target_names(num, gam):
    W = 'SIDEExplicitFormula.Window.'
    out = [W + x for x in ('bqA_poly', 'bqB_poly', 'bqG_poly', 'coeffPad_eq', 'band_table', 'bandW_eq', 'gWb_eq')]
    for chk, base, data in (('band_ok', 'bandNG', num), ('bgam_ok', 'bandGG', gam)):
        for g, part in enumerate(band_groups(data)):
            out += [W + '%s%d_%02d' % (chk, g, j) for j in range(len(chain_rows(0, part, CHUNK)))]
            out += [W + '%s%d_len' % (base, g), W + '%s%d' % (chk, g)]
    out += [W + x for x in ('bandNumL_len', 'bandNumL_all', 'bandGL_len', 'bandGL_all')]
    return out


def targets_text(old, names, anchor=ANCHOR):
    """print_targets.txt with the names not yet in it entered after the anchor, its newline kept"""
    nl = '\r\n' if '\r\n' in old else '\n'
    lines = old.split(nl)
    have = set(lines)
    i = lines.index(anchor)
    new = [x for x in names if x not in have]
    return nl.join(lines[:i + 1] + new + lines[i + 1:]), len(new), i + 1


def decl_lines(t):
    out, chunks = [], 0
    for i, l in enumerate(t.split(NL), 1):
        m = re.match(r'(theorem|def|noncomputable def) (\w+)', l)
        if not m:
            continue
        name = m.group(2)
        if re.match(r'(band_ok|bgam_ok)\d_\d{2}$', name):
            chunks += 1
        elif not re.match(r'b[ng]D\d{3}$', name):
            out.append('%s:%d' % (name, i))
    return out + (['the chunks` checks %d' % chunks] if chunks else [])


# ---------------------------------------------------------------- the build

def build(verbose=True):
    vec, piece, rep = read_band()
    forms = FD.read_forms()
    lists, crep = PD.read_coeffs()
    prods = products_ok(vec, piece) if rep['pieces'] == [0, 1, 2, 3] and len(vec) == 10 else {}
    blks = blocks()
    if verbose:
        print('  ArchClosed.lean: blob %s, equal at the base and HEAD %s ; vectors %d of widths %s ; pieces %s ; the closed forms` and lgI_neg`s '
              'statement lines present %s ; ArchBandLocal.lean equal %s, its band`s line present %s' % (
                  rep['blob'][:12], rep['equal'], len(rep['vectors']), rep['widths'], rep['pieces'], rep['forms'], rep['band_equal'], rep['band_form']))
        print('  each vector against pieceP k * pieceP (k + d): %s' % ' ; '.join('%s %s' % kv for kv in sorted(prods.items())))
        print('  FarClosed.lean`s fA, fB and fG read equal to the forms computed: %s' % ' ; '.join('%s %s' % (k, forms[k]) for k in ('fA', 'fB', 'fG')))
        print('  the blocks from the closed forms and lgI_neg: %d, equal to the plan`s table %s, the table`s bounds %s' % (len(blks), blks == TABLE, table_ok(blks)))
        print('  Coeffs.lean: blob %s, EQUAL %s ; lists %d ; numerators %d' % (crep['blob'][:12], crep['equal'], crep['chunks'], crep['total']))
    ok_in = (rep['equal'] and rep['band_equal'] and rep['vectors'] == sorted(VORDER) and rep['widths'] == [7] and rep['pieces'] == [0, 1, 2, 3]
             and all(rep['forms']) and rep['band_form'] and all(forms[k] for k in ('fA', 'fB', 'fG')) and len(prods) == 10
             and all(prods.values()) and blks == TABLE and table_ok(blks) and crep['equal'] and crep['chunks'] == 64 and crep['total'] == PD.N_ALL)
    if not ok_in:
        return None
    out, den, ip = polys(vec)
    ipn = name_polys(vec, den)
    flat = [x for l in lists for x in l]
    P = padded(flat)
    coeff_int = lambda m: flat[m - 16] if 16 <= m <= 16380 else 0
    pad_ok = all((P[m + 4] if m + 4 < len(P) else 0) == coeff_int(m) for m in range(16400))
    t0 = time.time()
    num, gam, wchk = windows(flat, ip, blks)
    dnum, dgam = direct(flat, ipn)
    chk = dict(pad_map=pad_ok, grouped_num=wchk['grouped_num'], grouped_gam=wchk['grouped_gam'], num_direct=(num == dnum),
               gam_direct=(gam == dgam), lengths=(len(num) == N_NUM and len(gam) == N_GAM), first_zero=(num[0] == 0))
    pchk = dict(integer=all(isinstance(v, int) for cs in ip.values() for v in cs), degrees=max(len(cs) - 1 for cs in ip.values()),
                at_points=all(Fraction(FD.horner_eval(ip[key], x), den) == FD.peval(out[key], x) for key in ip for x in (0, 1, 2, 7, 16383)),
                by_name=all(ipn[(nm, VORDER[v])] == ip[(nm, v)] for nm in 'ABG' for v in range(10)))
    if verbose:
        print('  the polynomials: 30, integer %s, the largest degree %d, read against the rational forms at five points %s, equal to the '
              'direct reading`s by name %s ; bandDEN %d digits' % (pchk['integer'], pchk['degrees'], pchk['at_points'], pchk['by_name'], len(str(den))))
        print('  the windows` checks (%.1f s): %s ; the largest place %d digits (log n) and %d digits (the constant)' % (
            time.time() - t0, ' ; '.join('%s %s' % kv for kv in chk.items()), max(len(str(abs(v))) for v in num), max(len(str(abs(v))) for v in gam)))
    ok = all(chk.values()) and all(pchk[k] for k in ('integer', 'at_points', 'by_name'))
    return dict(ok=ok, den=den, ip=ip, ipn=ipn, num=num, gam=gam, blob=rep['blob'], blks=blks, flat=flat, vec=vec, piece=piece)


def cmd_gen(mode):
    b = build()
    if b is None:
        sys.exit('### NOT WRITTEN: a source file is not read as the base holds it')
    tx = texts(b['den'], b['ip'], b['blks'], b['num'], b['gam'], b['blob'])
    ok = b['ok']
    for k in sorted(tx):
        tc = PD.text_checks(tx[k])
        dbo = FD.doc_before_option(tx[k])
        good = not tc['decimal'] and not tc['barred'] and tc['import_first'] and tc['longest_list'] <= CHUNK and dbo == 0
        ok = ok and good
        print('  %s.lean: lines %d, bytes %d, sha256 %s ; decimal literals %d ; barred words %d ; imports first %s ; the longest list %d ; doc comments above an option %d -> %s' % (
            k, tc['lines'], tc['bytes'], tc['sha256'], tc['decimal'], tc['barred'], tc['import_first'], tc['longest_list'], dbo, 'OK' if good else 'REFUSED'))
        print('    declarations (name:line), the data chunks left out: %s' % ', '.join(decl_lines(tx[k])))
    tpath = os.path.join(KPATH, 'print_targets.txt')
    told = io.open(tpath, 'r', encoding='utf-8', newline='').read()
    names = target_names(b['num'], b['gam'])
    tnew, nadd, at = targets_text(told, names)
    print('  print_targets.txt: the generated theorems %d (each once %s), of them not yet listed %d, entered after %s at :%d ; lines %d to %d' % (
        len(names), len(set(names)) == len(names), nadd, ANCHOR.split('.')[-1], at, told.count('\n'), tnew.count('\n')))
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
    with io.open(tpath, 'w', encoding='utf-8', newline='') as f:
        f.write(tnew)
    back = open(tpath, 'rb').read()
    print('### WRITTEN print_targets.txt: %d bytes, read back EQUAL %s' % (len(back), back == tnew.encode('utf-8')))


def cmd_control():
    res = []

    def c(name, got, ok):
        res.append(ok)
        print('  (%d) %s: %s -> %s' % (len(res), name, got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    c('a vector`s entry by the grammar: -1 / 4 and 17 / 36', (const('-1 / 4'), const('17 / 36')),
      const('-1 / 4') == Fraction(-1, 4) and const('17 / 36') == Fraction(17, 36))
    try:
        const('c / 2')
        refused = False
    except ValueError:
        refused = True
    c('A PLANTED FAULT: an entry with c, refused as not constant', refused, refused)
    c('the blocks: sixteen, equal to the plan`s table, each within its bounds', (len(blocks()), blocks() == TABLE, table_ok(blocks())),
      blocks() == TABLE and table_ok(blocks()))
    moved = dict(CLOSED)
    moved[1] = [(0, '01'), (2, '11'), (2, '21')]
    c('A PLANTED FAULT: one shift of lgI a 1 moved, the blocks read unequal to the table', blocks(moved) == TABLE, blocks(moved) != TABLE)
    A, B = tables(TABLE)
    c('the grouped products: each vector of v < 6 two blocks of one pair (the factor 2), v >= 6 one block of a square',
      (sorted(A[0].items()), sorted(B[9].items())),
      all(len(A[v]) == 1 and list(A[v].values()) == [2] and len(B[v]) == 1 and list(B[v].values()) == [2] for v in range(6))
      and all(list(A[v].values()) == [1] and list(A[v])[0][0] == list(A[v])[0][1] for v in range(6, 10)))
    rows = chain_rows(4096, list(range(150)), CHUNK)
    mv = [rows[0], (rows[1][0] + 1, rows[1][1], rows[1][2]), rows[2]]
    c('the chunks` places: 150 places from 4096 in pieces of 64, (4096, 4096, 64), (4160, 4160, 64), (4224, 4224, 22)', rows,
      rows == [(4096, 4096, 64), (4160, 4160, 64), (4224, 4224, 22)] and chain_ok(rows, 4096, 150))
    c('A PLANTED FAULT: the second piece`s window moved by one place, read as not joining', chain_ok(mv, 4096, 150), not chain_ok(mv, 4096, 150))
    pl = chain_proof('bandW', 'coeffPad', ['x0', 'x1'], [(0, 0, 64), (64, 64, 5)], [('ok0', None), ('ok1', None)])
    c('the join`s tactic lines on two planted pieces at the window of coeffPad', pl,
      pl == ['  refine winOK_chunk bandW coeffPad x0 _ 0 0 64 64 64 (by decide +kernel) (by norm_num) (by norm_num) ok0 ?_', '  exact ok1'])
    tt, nn, at = targets_text('a\nSIDEExplicitFormula.Window.far_final\n', ['SIDEExplicitFormula.Window.band_ok0_00', 'a'])
    c('print_targets.txt`s entry on a planted file whose anchor is its last line: one new name after it, one present left out', (tt, nn, at),
      tt == 'a\nSIDEExplicitFormula.Window.far_final\nSIDEExplicitFormula.Window.band_ok0_00\n' and nn == 1 and at == 2)
    b = build(verbose=False)
    c('the sources read as the base holds them; the checks before a write (the pad`s map, the grouped and block forms, each place read '
      'again pair by pair, the polynomials at five points and by name)', b is not None and b['ok'], b is not None and b['ok'])
    if b is not None:
        vec2 = dict(b['vec'])
        vec2['11'] = list(vec2['11'])
        vec2['11'][3] += Fraction(1, 36)
        p2 = products_ok(vec2, b['piece'])
        c('A PLANTED FAULT: one entry of bandV11 moved by 1/36, read against pieceP 1 * pieceP 2', p2['11'], not p2['11'])
        n19, g19, _ = windows(b['flat'], b['ip'], b['blks'], pad=19)
        c('A PLANTED FAULT: the window read with nineteen zeros, read unequal to the direct reading', (n19 == b['num'], g19 == b['gam']),
          n19 != b['num'] and g19 != b['gam'])
        t2 = list(b['blks'])
        t2[11] = (4, 1, 4)
        n2, g2, _ = windows(b['flat'], b['ip'], t2)
        c('A PLANTED FAULT: one block`s shift moved (block 11 at s = 1), read unequal to the direct reading', n2 == b['num'], n2 != b['num'])
        tx = texts(b['den'], b['ip'], b['blks'], b['num'], b['gam'], b['blob'])
        tcs = [PD.text_checks(tx[k]) for k in sorted(tx)]
        c('the eleven texts (no decimal literal, no barred word, imports first, lists of %d at most, no doc comment above an option)' % CHUNK,
          (len(tx), sum(t['decimal'] + t['barred'] for t in tcs), all(t['import_first'] for t in tcs), max(t['longest_list'] for t in tcs),
           sum(FD.doc_before_option(tx[k]) for k in tx)),
          len(tx) == 11 and not sum(t['decimal'] + t['barred'] for t in tcs) and all(t['import_first'] for t in tcs)
          and max(t['longest_list'] for t in tcs) <= CHUNK and sum(FD.doc_before_option(tx[k]) for k in tx) == 0)
        c('the groups: 4 of the log n data (4,096 x 3 and 4,097) and 4 of the constant (4,096 x 4)',
          ([len(x) for x in band_groups(b['num'])], [len(x) for x in band_groups(b['gam'])]),
          [len(x) for x in band_groups(b['num'])] == [4096, 4096, 4096, 4097] and [len(x) for x in band_groups(b['gam'])] == [4096] * 4)
        tn = target_names(b['num'], b['gam'])
        c('the generated theorems: 7, 257 + 256 chunks` checks, 16 of the groups and 4 of the joins, each name once', (len(tn), len(set(tn))),
          len(tn) == 540 and len(set(tn)) == 540)
    print('### THE TOOL`S CONTROLS: %d OF %d AS WANTED' % (sum(res), len(res)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        cmd_control()
    elif a[:1] in (['dry'], ['write']):
        cmd_gen(a[0])
    else:
        sys.exit('usage: b768_band_data.py control | dry | write')
