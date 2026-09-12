# -*- coding: utf-8 -*-
"""b434_reg_gate.py -- THE REGISTRATION GATE, RUN BEFORE THE LOCK. ### ALL THREE ARMS.

### ### **THE GATE MODULE IS IMPORTED, NEVER COPIED**, and its own fixtures are run here in both
### polarities before its verdict is trusted -- `b347`'s bar-floor arms and `b359`'s straddle arm.
### ### **AND THE RECORD IS WRITTEN BY THIS FILE AND NOT BY A SHELL PIPE**, because a shell pipe on this
### machine prepends a UTF-8 BOM (`b298`, `b305`) and a later arm reading the record would meet a byte
### the writer never wrote.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import registration_gate as RG   # noqa: E402

D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b434_registration_2026-09-12.txt')
OUT = os.path.join(D, 'b434_reg_gate.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b434 -- THE REGISTRATION GATE, RUN BEFORE THE LOCK.')
    rec('=' * 100)
    # ### **`RG.check` RETURNS `(code, lines)`; IT DOES NOT PRINT.** ### The first version of this driver
    # ### tested the TUPLE for truth -- and a non-empty tuple is always true, so the arm would have
    # ### passed on a HARD FAILURE. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM** (`b363`'s species,
    # ### committed here by assuming a shape instead of reading it).
    rec('--- INDEX-QUERY GATE (b185) ---')
    code, lines = RG.check(REG)
    for ln in lines:
        rec(ln)
    ok_index = (code == 0)
    rec('  ### index-query arm exit code : %d ### -- PASS only on `0`' % code)
    txt = io.open(REG, encoding='utf-8').read()
    bf = RG.bar_floor_self_test(False)
    st = RG.straddle_self_test(False)
    rec('')
    rec('  bar-floor fixtures both polarities : %s ; straddle fixtures both polarities : %s' % (bf, st))
    floor_misses, arm_misses, n_thr, n_multi = RG.bar_floor_check(txt)
    misses, n_repo = RG.straddle_check(txt)
    rec('  thresholds %d FLOOR MISSES %d %s' % (n_thr, len(floor_misses), floor_misses or []))
    rec('  multi-arm  %d ARM MISSES   %d %s' % (n_multi, len(arm_misses), arm_misses or []))
    rec('  arm+repo-state paragraphs %d UNDECLARED %d %s' % (n_repo, len(misses), misses or []))
    clear = bool(ok_index) and bf and st and not floor_misses and not arm_misses and not misses
    rec('  ### ### **GATE VERDICT : %s**' % ('CLEAR' if clear else 'NOT CLEAR'))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0 if clear else 1


if __name__ == '__main__':
    sys.exit(main())
