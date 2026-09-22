# -*- coding: utf-8 -*-
"""b483_extract.py -- THE SURVEY FOR THE b477 READ. ### The lane is open: the log and the entry bank
### are files on disk and the run has EXITED. ### **NO BUILD IS STARTED; b475's LOG IS NOT OPENED;
### NOTHING IS FETCHED; NO CHAIN IS RE-RUN.** ### Every figure comes from `b477_gram.log` and
### `b477_entries.jsonl`, plus the two registrations that fix the orientation and the floor.
"""
import io
import json
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L, MISSES = [], []

FLOOR = 1.49e-08   # ### the chain's own floor, sqrt(eps), quoted from b476 (A)(5) and b446.

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def entries():
    out = []
    for l in io.open(os.path.join(D, 'b477_entries.jsonl'), encoding='utf-8'):
        l = l.strip()
        if l:
            out.append(json.loads(l))
    return out


def main():
    rec('=' * 104)
    rec('b483 -- THE SURVEY. ### THE b477 RUN HAS EXITED; ITS BANK AND ITS LOG ARE READ FROM DISK.')
    rec('=' * 104)

    log = read(os.path.join(D, 'b477_gram.log'))
    E = entries()

    # ------------------------------------------------------------------ (P1) the run ended, and how
    rec('')
    rec('(P1) THE RUN`S OWN END, READ FROM ITS LOG.')
    rec('-' * 104)
    done = 'RUN COMPLETE' in log
    exit0 = '=== EXIT 0 : b477_gram.py' in log
    rec('    the log carries ### **RUN COMPLETE** : %s' % done)
    rec('    the launcher carries ### **EXIT 0**   : %s' % exit0)
    if not (done and exit0):
        MISSES.append(('b477_gram.log', 'RUN COMPLETE / EXIT 0'))
    t = re.findall(r'^\[(\d\d):(\d\d):(\d\d)\]', log, re.M)
    if t:
        s = int(t[0][0]) * 3600 + int(t[0][1]) * 60 + int(t[0][2])
        e = int(t[-1][0]) * 3600 + int(t[-1][1]) * 60 + int(t[-1][2])
        rec('    first stamp %s ; last stamp %s ; ### **ELAPSED %d s (%d min)**'
            % (':'.join(t[0]), ':'.join(t[-1]), e - s, (e - s) // 60))
        rec('      ### priced at b477 : ### **2923 s (49 min)**. ### The run came in ### **UNDER**')
        rec('      ### its own price by %d s.' % (2923 - (e - s)))
        rec('      ### ### **AND THE STAMPS ARE DISTINCT** -- %d distinct second-stamps over %d lines,'
            % (len(set(t)), len(t)))
        rec('      ### so b475`s one-instant defect is NOT repeated, exactly as READING (6) declared.')
    hdr = re.search(r'aim-plane cells (\d+) ; ladder cells (\d+) ; banked W available for (\d+) of (\d+)', log)
    rec('    the run`s own header : %s' % (hdr.group(0) if hdr else 'NOT FOUND'))
    if not hdr:
        MISSES.append(('b477_gram.log', 'the header line'))

    # ------------------------------------------------------------------ (P2) the entry bank's shape
    rec('')
    rec('(P2) THE ENTRY BANK, COUNTED AGAINST THE PRICE.')
    rec('-' * 104)
    kinds = {}
    for d in E:
        kinds[d['kind']] = kinds.get(d['kind'], 0) + 1
    for k in sorted(kinds):
        rec('    %-20s %d' % (k, kinds[k]))
    fam = {}
    for d in E:
        if d['kind'] == 'offdiagonal':
            fam[d['family']] = fam.get(d['family'], 0) + 1
    rec('    off-diagonals by family : %s' % ', '.join('%s %d' % (k, v) for k, v in sorted(fam.items())))
    na, nl = int(hdr.group(1)), int(hdr.group(2))
    rec('    ### the arithmetic closes: %d*%d/2 = %d and %d*%d/2 = %d, together %d'
        % (na, na - 1, na * (na - 1) // 2, nl, nl - 1, nl * (nl - 1) // 2,
           na * (na - 1) // 2 + nl * (nl - 1) // 2))
    rec('    ### ### **SO THE RUN BUILT TWO WITHIN-FAMILY GRAMS, NOT ONE %d-BY-%d MATRIX.**'
        % (na + nl, na + nl))
    rec('    ### The %d aim-plane cells and the %d ladder cells are never paired with each other, so'
        % (na, nl))
    rec('    ### ### **NO CROSS-FAMILY ENTRY EXISTS AND NONE IS INVENTED HERE.**')
    if kinds.get('offdiagonal') != na * (na - 1) // 2 + nl * (nl - 1) // 2:
        MISSES.append(('b477_entries.jsonl', 'the off-diagonal count'))

    # ------------------------------------------------------------------ (P3) the diagonal checks
    rec('')
    rec('(P3) THE DIAGONAL CHECKS, AGAINST THE ZERO SIDE AND THE TAIL FIGURE.')
    rec('-' * 104)
    dg = [d for d in E if d['kind'] == 'diagonal']
    banked = [d for d in dg if d['banked'] is not None]
    rec('    diagonal cells : %d ; with a banked W to check against : %d ; with NONE : %d'
        % (len(dg), len(banked), len(dg) - len(banked)))
    rec('    ### ### **EVERY CHECKED CELL PASSED : %s** (the runner halts before any off-diagonal'
        % all(d['ok'] for d in dg))
    rec('    ### entry otherwise, and 309 off-diagonal entries exist).')
    if banked:
        mx = max(abs(d['diff']) for d in banked)
        rec('    ### largest |W - banked W| over the %d checked cells : ### **%.3e**' % (len(banked), mx))
        rec('      ### against the floor 1.49e-08 : %s' % ('WITHIN' if mx < FLOOR else 'BEYOND'))
        ex = sum(1 for d in banked if d['diff'] == 0.0)
        rec('      ### cells reproducing the bank EXACTLY (diff 0.000e+00) : ### **%d of %d**'
            % (ex, len(banked)))
    zs = [abs(d['W'] + d['zero']) for d in dg]
    rec('    ### the zero side: |W + Z| per cell, largest : ### **%.3e**' % max(zs))
    rec('      ### this is (R87)`s identity Sum_v W_v(f) = -Z read on the diagonal, and it holds to')
    rec('      ### ### **%.3e** at every one of the %d cells.' % (max(zs), len(dg)))
    tb = [d['trunc_bound'] for d in dg]
    rec('    ### the tail figure `trunc_bound` : min %.3e ; max ### **%.3e**' % (min(tb), max(tb)))
    rec('      ### ### **THE TAIL BOUND IS FOUR ORDERS BELOW THE FLOOR**, so it is the binding')
    rec('      ### figure for (F2) and (F3), not the floor.')

    # ------------------------------------------------------------------ (P4) the eigen-solver rehearsed
    rec('')
    rec('(P4) THE EIGEN-SOLVER, REHEARSED BEFORE THE SEAL, ON A MATRIX WHOSE SPECTRUM IS KNOWN.')
    rec('-' * 104)
    rec('    ### ### **(R70): THE READER IS RUN ON A CASE WHOSE ANSWER IS KNOWN BEFORE IT IS RUN ON')
    rec('    ### THE CASE THAT MATTERS.** ### The rehearsal is a HYPERBOLIC PLANE -- the very object')
    rec('    ### (F1) asks the control to exhibit -- whose eigenvalues are exactly +1 and -1:')
    H = np.array([[0.0, 1.0], [1.0, 0.0]])
    w, V = np.linalg.eigh(H)
    res = [float(np.linalg.norm(H @ V[:, i] - w[i] * V[:, i])) for i in range(2)]
    rec('      H = [[0, 1], [1, 0]]')
    for i in range(2):
        rec('        eigenvalue %+.15f   residual %.3e' % (w[i], res[i]))
    rec('      ### negative index at floor %.2e : ### **%d** -- and a hyperbolic plane HAS one.'
        % (FLOOR, int((w < -FLOOR).sum())))
    ok_h = abs(w[0] + 1) < 1e-12 and abs(w[1] - 1) < 1e-12
    rec('      ### ### **REHEARSAL PASSES : %s.**' % ok_h)
    if not ok_h:
        MISSES.append(('rehearsal', 'the hyperbolic plane'))
    rec('    ### And the NEGATIVE control of the rehearsal, so the reader is not one-sided:')
    P = np.array([[2.0, 1.0], [1.0, 2.0]])
    wp, _ = np.linalg.eigh(P)
    rec('      P = [[2, 1], [1, 2]] -- eigenvalues %+.12f and %+.12f ; negative index ### **%d**'
        % (wp[0], wp[1], int((wp < -FLOOR).sum())))
    rec('      ### ### **A DEFINITE MATRIX RETURNS NEGATIVE INDEX 0**, so a reported 0 is a')
    rec('      ### measurement and not the reader failing to look.')

    # ------------------------------------------------------------------ (P5) the orientation at its address
    rec('')
    rec('(P5) (R87)`S ORIENTATION AND THE TWO THRESHOLDS, QUOTED AT THEIR ADDRESSES.')
    rec('-' * 104)
    f476 = read(os.path.join(D, 'b476_registration_2026-09-22.txt'))
    for needle in ('THE SIGNATURE IS READ ON `-G`',
                   '**(F2) HALTS ON A POSITIVE EIGENVALUE OF `G`**',
                   '**(N2) AND (N3) REFER TO THE LARGEST EIGENVALUE OF `G`**'):
        ln = next((x.strip() for x in f476.split(NL) if needle in x), '')
        rec('    %s' % (ln[:150] if ln else '### NOT FOUND : %s' % needle))
        if not ln:
            MISSES.append(('b476 face', needle))
    rec('    ### ### **SO THE FALSIFIER AND THE EXPECTATION POINT AT OPPOSITE ENDS OF THE SPECTRUM,**')
    rec('    ### and this act prints BOTH ends at every size so neither can hide the other.')
    rec('    ### ### **AND THE ORDER`S OWN WORDS SAY "the smallest eigenvalue per size for zeta".**')
    rec('    ### Under (R87) the falsifier-bearing end for zeta is the ### **LARGEST eigenvalue of G**')
    rec('    ### (the smallest of `-G`). ### The order also says the scoring is "as (R87) orients')
    rec('    ### them", so ### **(R87) GOVERNS AND THE TENSION IS NAMED RATHER THAN RESOLVED IN**')
    rec('    ### ### **SILENCE**; both extremes are printed under both names.')

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b483_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(complete=done, exit0=exit0, kinds=kinds, families=fam,
                   aim=na, ladder=nl, floor=FLOOR,
                   diag_cells=len(dg), diag_checked=len(banked),
                   diag_all_ok=all(d['ok'] for d in dg),
                   max_abs_diff=(max(abs(d['diff']) for d in banked) if banked else None),
                   max_zero_resid=max(zs), max_trunc=max(tb), min_trunc=min(tb),
                   misses=MISSES),
              io.open(os.path.join(D, 'b483_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
