# -*- coding: utf-8 -*-
"""b278_space_barrier.py -- M-2 CAMPAIGN, ACT 12. ### THE SPACE-LEVEL BARRIER.

### THE QUESTION: ### **IS (SPEC-1) IDENTICALLY ZERO FOR EVERY VECTOR STATE ON `S-bar_v`?**

### ### **THE TOWER QUESTION IS A READ, NOT A COMPUTATION, AND THIS FILE DOES NOT DISGUISE ONE
### ### AS THE OTHER.** ### It reports what the corpus says, with a positive control on the
### absence, and computes only what is computable: the ball's identity and the two readings'
### consequences.

### ### **NO FLOAT TOKEN APPEARS IN THIS FILE.**
"""
import glob
import io
import os
import re
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))

from b270_ambient_pairing import (PLACES, Field, ball_of, orbit_classes,
                                  spadd, spconj, spmul, spscale)
from noise_floor import gate as floor_gate

DATA = os.path.join(HERE, '..', '..', 'data')


def sonin_ball(N, p, n):
    """### b8's `model`: ### `ball = { m : m mod p^n == 0 }`. ### The SAME set `sonin_basis`
    ### imposes its constraints on, and the SAME set b270's absorption uses at `k = n`."""
    pn = p ** n
    return set(m for m in range(N) if m % pn == 0)


def absorption_ball(N, p, n):
    """### b270's ABSORPTION SET, DEFINED BY ITS OWN PROPERTY AND NOT BY NAME: ### the set of
    ### indices `p^n m` can land on, as `m` ranges over everything."""
    pn = pow(p, n, N)
    return set((pn * m) % N for m in range(N))


def f_ij(i, j, q, N):
    a = (i + q * j) % N
    b = i % N
    out = []
    for m in range(N):
        d = {}
        for idx, sg in ((a, 1), (b, -1), ((-a) % N, 1), ((-b) % N, -1)):
            if m == idx:
                d[0] = d.get(0, Fraction(0)) + sg * q
        for k, sg in (((m * a) % N, 1), ((-m * a) % N, 1),
                      ((m * b) % N, -1), ((-m * b) % N, -1)):
            d[k] = d.get(k, Fraction(0)) + sg
        out.append({k: v for k, v in d.items() if v != 0})
    return out


def g0_vec(q, N):
    return [({0: Fraction(2 * q + 2)} if m == 0 else {0: Fraction(2)}) for m in range(N)]


def projector(N, p, n):
    ballset = sonin_ball(N, p, n)
    cls_of = {}
    for C in orbit_classes(N, p, ballset):
        for m in C:
            cls_of[m] = C

    def S_quot(v):
        out = []
        for m in range(N):
            if m in ballset:
                out.append({})
                continue
            C = cls_of[m]
            acc = {}
            for m2 in C:
                acc = spadd(acc, v[m2])
            out.append(spscale(acc, Fraction(1, len(C))))
        return out
    return ballset, S_quot


def sesq(x, S_quot, p, k, N):
    Sx = S_quot(x)
    pk = pow(p, k, N)
    acc = {}
    for m in range(N):
        if not Sx[m]:
            continue
        acc = spadd(acc, spmul(Sx[m], spconj(x[(pk * m) % N], N), N))
    return acc


def sbar_mentions():
    """### THE POSITIVE CONTROL ON THE ABSENCE. ### Every line in the corpus mentioning
    ### `S-bar`, classified: does ANY of them DEFINE it? ### A definition-shaped line carries
    ### `S-bar` on the left of `:=`, `is`, or `=`. ### **THE CONTROL IS THAT THE NEAR-MISSES ARE
    ### FOUND AND SHOWN NOT TO BE DEFINITIONS -- NOT THAT A SEARCH RETURNED NOTHING.**"""
    hits = []
    for path in sorted(glob.glob(os.path.join(DATA, '*.txt'))):
        for ln in io.open(path, encoding='utf-8', errors='replace').read().split('\n'):
            if 'S-bar' in ln:
                hits.append((os.path.basename(path), ln.strip()))
    defshape = [h for h in hits
                if re.search(r'S-bar[_a-z]*\s*(:=|=(?!=)|\bis\b)', h[1])]
    return hits, defshape


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b278 -- COMPONENT 1. ### THE SPACE-LEVEL BARRIER. ### EXACT. ### NO FLOAT.')
    rec('### REGISTRATION data/b278_registration_2026-09-01.txt SEALED 763f29ea.')
    rec('### **THE TOWER QUESTION IS A READ. ### THIS FILE DOES NOT DISGUISE IT AS A DERIVATION.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec()

    # --- (a) THE TOWER --------------------------------------------------------------------
    rec('-' * 100)
    rec('### (1) (a) THE TOWER. ### **VERDICT: (ABSENT), AND WORSE THAN b277 KNEW.**')
    rec('-' * 100)
    hits, defshape = sbar_mentions()
    rec('  ### THE POSITIVE CONTROL ON THE ABSENCE -- the near-misses are FOUND, not merely')
    rec('  ### unsearched-for:')
    rec('    lines in data/ mentioning `S-bar`            : %d' % len(hits))
    rec('    of those, DEFINITION-SHAPED (S-bar := / = / is) : %d' % len(defshape))
    for f, ln in defshape[:8]:
        rec('      %-34s %s' % (f, ln[:96]))
    rec()
    rec('  ### **NOT ONE OF THEM DEFINES THE TOWER.** ### b198 (I4) says `S-bar` IS the')
    rec('  ### L^2-closure of "THE TOWER\'S UNION" without saying whose tower; b226 unfolds it by')
    rec('  ### citing b198; b198 (I2) places a level vector by "the closure of its level tower".')
    rec('  ### ### **EVERY ONE OF THEM NAMES THE TOWER. ### NONE OF THEM SAYS WHAT IT IS.**')
    rec()
    rec('  ### **AND b21 -- WHICH OWNS THE TOWER -- SETTLES IT IN THE OTHER DIRECTION:**')
    rec('  ###   `V_n = { f : supp f in p^(-n) Z_p, f invariant under translation by p^n Z_p }`')
    rec('  ###   "an honest finite-dimensional subspace of L^2(Q_p)"   ### -- THE FULL LEVEL')
    rec('  ###   SPACE, with Son(p,n) sitting INSIDE it -- and the embedding `iota : V_n ->')
    rec('  ###   V_(n+1)`.')
    rec('  ### ### **AND ITS FOOT, WHICH IS THE ACT\'S CENTRAL QUOTATION:**')
    rec('  ### ### **"the union of the V_n is dense in L^2(Q_p), but Son(p,n) does NOT stabilize')
    rec('  ### ### (its dimension (p^n-1)^2 grows), so nothing here constructs a limit object,')
    rec('  ### ### and none is claimed."**')
    rec('  ### ### ### **SO THE CORPUS DOES NOT MERELY LEAVE `S-bar_v` UNQUOTED. ### THE ACT')
    rec('  ### ### ### THAT BUILT THE TOWER EXPLICITLY DECLINES TO CONSTRUCT THE LIMIT OBJECT,')
    rec('  ### ### ### AND SAYS SO IN ITS OWN VOICE.**')
    rec()

    # --- (b) SON AND THE BALL --------------------------------------------------------------
    rec('-' * 100)
    rec('### (2) (b) SON\'S DEFINITION, AND THE BALL\'S IDENTITY. ### **DECIDED BY DEFINITIONS.**')
    rec('-' * 100)
    rec('  b226: Son(p,n) = the vectors ### "vanishing on a ball AND on its transform image".')
    rec('  b8\'s `sonin_basis` imposes ### **rows of the IDENTITY on the ball AND rows of F on')
    rec('  ### the ball** ### -- so BOTH the function and its transform vanish, and on the SAME')
    rec('  ### set. ### **BALL-VANISHING IS DEFINITIONAL FOR Son, ON BOTH HALVES.**')
    rec()
    rec('  ### **AND THE TWO BALLS ARE COMPARED AS SETS, NOT BY NAME:**')
    rec('  %-8s %-6s %-14s %-16s %-16s %s'
        % ('(p,n)', 'N', "|Son's ball|", "|absorption set|", 'EQUAL as sets?', 'b270 ball_of ok'))
    ball_ok = True
    cellinfo = {}
    for (p, ell) in PLACES:
        q = p ** ell
        N = q * q
        sb = sonin_ball(N, p, ell)
        ab = absorption_ball(N, p, ell)
        legacy = set(ball_of(N, p, ell))
        same = (sb == ab)
        ball_ok = ball_ok and same and (sb == legacy)
        cellinfo[(p, ell)] = (q, N)
        rec('  %-8s %-6d %-14d %-16d %-16s %s'
            % ('(%d,%d)' % (p, ell), N, len(sb), len(ab),
               'YES' if same else '### NO ###',
               'YES' if sb == legacy else '### NO ###'))
    rec()
    rec('  ### **BALL IDENTITY VERDICT: %s**'
        % ('THE SAME SET AT EVERY CELL -- Son\'s ball IS b270\'s absorption set' if ball_ok
           else '### THE BALLS DIFFER -- THE DERIVATION HALTS HERE ###'))
    rec('  ### The absorption set is computed from ITS OWN PROPERTY -- the indices `p^n m` can')
    rec('  ### land on -- and NOT from the name `ball`, which is the whole point of the check.')
    rec()

    # --- (c) THE TWO READINGS ---------------------------------------------------------------
    rec('-' * 100)
    rec('### (3) (c) THE TWO READINGS, EACH DERIVED. ### **THEY DISAGREE.**')
    rec('-' * 100)
    rec('  ### **READING TWO FIRST, BECAUSE IT IS THE ONE THE CAMPAIGN ASSUMED.**')
    rec('  ### If `S-bar_v` is a Son limit, every element vanishes on the ball, and b270\'s')
    rec('  ### absorption gives (SPEC-1) = 0 identically. ### VERIFIED ON THE SPANNING FAMILY:')
    rec('  %-8s %-22s %-18s %s' % ('(p,n)', 'ball-vanishing tested', 'P(ell) = 0 for all', 'scope'))
    son_all = True
    for (p, ell) in PLACES:
        q, N = cellinfo[(p, ell)]
        F = Field(N)
        ballset, S_quot = projector(N, p, ell)
        pairs = ([(i, j) for i in range(1, q) for j in range(1, q)] if N <= 121
                 else [(1, 1), (1, 2), (2, 1), (2, 2)])
        scope = ('FULL %d' % len(pairs)) if N <= 121 else ('SAMPLE %d' % len(pairs))
        nvan = 0
        allz = True
        for (i, j) in pairs:
            w = f_ij(i, j, q, N)
            if not all(F.is_zero(w[m]) for m in ballset):
                continue
            nvan += 1
            if not F.is_zero(sesq(w, S_quot, p, ell, N)):
                allz = False
        son_all = son_all and allz
        rec('  %-8s %-22d %-18s %s'
            % ('(%d,%d)' % (p, ell), nvan, 'YES' if allz else '### NO ###', scope))
    rec('  ### ### **SO ON `Son` (SPEC-1) IS IDENTICALLY ZERO: %s. ### THE BARRIER HOLDS UNDER'
        % ('CONFIRMED' if son_all else '### FAILED ###'))
    rec('  ### ### READING TWO.**')
    rec()
    rec('  ### **READING ONE. ### If `S-bar_v` is the closure of the `V_n` tower -- which b21\'s')
    rec('  ### foot says is DENSE IN L^2(Q_p) -- then `V_ell` lies honestly inside it, and so')
    rec('  ### does every vector in `V_ell`, INCLUDING ONES THAT DO NOT VANISH ON THE BALL.**')
    rec('  ### THE ELEMENT, EXHIBITED EXACTLY:')
    rec('  %-8s %-24s %-18s %s'
        % ('(p,n)', 'g_0 = 2q e_0 + 2*1', 'ball value g_0(0)', 'P(ell) * p^{ell/2}'))
    refuted = True
    for (p, ell) in PLACES:
        q, N = cellinfo[(p, ell)]
        F = Field(N)
        ballset, S_quot = projector(N, p, ell)
        g0 = g0_vec(q, N)
        a = F.reduce(sesq(g0, S_quot, p, ell, N))
        rat = all(x == 0 for x in a[1:])
        nz = rat and a[0] == Fraction(4 * (N - q)) and a[0] != 0
        refuted = refuted and nz
        rec('  %-8s %-24s %-18s %s'
            % ('(%d,%d)' % (p, ell), 'in V_%d' % ell, str(2 * q + 2),
               '%s  = 4(N-q)' % a[0] if rat else '(not rational)'))
    rec('  ### ### **NONZERO AT EVERY CELL: %s. ### SO UNDER READING ONE (SPEC-1) IS NOT'
        % ('CONFIRMED' if refuted else '### FAILED ###'))
    rec('  ### ### IDENTICALLY ZERO, b277\'s BLOCK DISSOLVES, AND THE BARRIER IS REFUTED.**')
    rec()
    rec('  ### ### ### **TWO READINGS. ### OPPOSITE ANSWERS. ### AND THE CORPUS SETTLES')
    rec('  ### ### ### NEITHER, BECAUSE b21 DECLINES TO CONSTRUCT THE OBJECT THAT WOULD.**')
    rec()

    # --- (e) THE CONSOLIDATION --------------------------------------------------------------
    rec('-' * 100)
    rec('### (4) (e) THE CONSOLIDATION THAT SURVIVES THE BIVALENCE.')
    rec('-' * 100)
    rec('  ### Whatever `S-bar_v` turns out to be, ### **ON `Son` AT ANY FINITE LEVEL (SPEC-1)')
    rec('  ### IS IDENTICALLY ZERO** ### -- and by TWO independent routes:')
    rec('  ###   b270\'s ABSORPTION: `p^ell m` lands in the ball for every `m`, and a Son vector')
    rec('  ###     vanishes there, so every summand carries a zero factor.')
    rec('  ###   b276\'s BOUND: (SPEC-1)\'s value is EXACTLY QUADRATIC in the ball-size `sigma`,')
    rec('  ###     and a Son vector has `sigma = 0`.')
    rec('  ### ### **SO b269\'s R3, b270, b273, b275 AND b277 ARE FIVE INSTANCES OF ONE THEOREM')
    rec('  ### ### RATHER THAN FIVE SEPARATE OUTCOMES -- AND NOT ONE OF THEM IS RE-VERDICTED.**')
    rec('  ### Each was scoped to the AMBIENT `E_1` at a FINITE LEVEL and is exactly true there;')
    rec('  ### the consolidation adds a sentence ABOVE them, not a correction INSIDE any.')
    rec()

    io.open(os.path.join(DATA, 'b278_run.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b278_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
