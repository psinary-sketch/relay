# -*- coding: utf-8 -*-
"""b713_reg_gate.py -- THE REGISTRATION GATE, RUN BEFORE THE LOCK. ### ALL THREE ARMS, THE DRY-RUN STEP AND THE CLOSING'S DRY RUN.

### ### **THE GATE MODULE IS IMPORTED, NEVER COPIED**, and its own fixtures are run here in both
### polarities before its verdict is trusted -- `b347`'s bar-floor arms and `b359`'s straddle arm.
### ### **AND THE RECORD IS WRITTEN BY THIS FILE AND NOT BY A SHELL PIPE**, because a shell pipe on this
### machine prepends a UTF-8 BOM (`b298`, `b305`) and a later arm reading the record would meet a byte
### the writer never wrote. ### Carried from b712_reg_gate.py by the Write tool, the act's names changed; the closing dry-run step as
### b675's rules bank row 1 orders it (relay data/b675_rules.txt); the dry-run step's trail Defects line AND Resolved line read against the
### defects bank inside the record tool's drycheck (the ferry's Component 5).
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import registration_gate as RG   # noqa: E402

D = os.path.join(ROOT, 'data')
REG = os.path.join(D, 'b713_registration_2026-10-25.txt')
OUT = os.path.join(D, 'b713_reg_gate.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b713 -- THE REGISTRATION GATE, RUN BEFORE THE LOCK.')
    rec('=' * 100)
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
    import subprocess
    rec('')
    rec('--- THE DRY-RUN STEP ((R267)(2)): the entry and the trail record through their guards, the face`s needles, the trail`s Defects and Resolved lines ---')
    dr = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'b713_record.py'), 'drycheck', REG, 'standin'], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    for ln in ((dr.stdout or '') + (dr.stderr or '')).rstrip(chr(10)).split(chr(10)):
        rec('  ' + ln)
    dry_clean = dr.returncode == 0 and 'DRY-RUN STEP : CLEAN' in (dr.stdout or '')
    rec('  ### ### **THE DRY-RUN STEP : %s** (exit %d)' % ('CLEAN' if dry_clean else 'NOT CLEAN', dr.returncode))
    rec('')
    rec('--- THE CLOSING DRY-RUN STEP (b675 rules row 1): the closing tool run dry, its readings ---')
    cr = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'b713_closing.py'), 'dry'], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    for ln in ((cr.stdout or '') + (cr.stderr or '')).rstrip(chr(10)).split(chr(10)):
        rec('  ' + ln)
    closing_clean = cr.returncode == 0 and 'THE CLOSING DRY-RUN : READ' in (cr.stdout or '')
    rec('  ### ### **THE CLOSING DRY-RUN STEP : %s** (exit %d)' % ('CLEAN' if closing_clean else 'NOT CLEAN', cr.returncode))
    clear = bool(ok_index) and bf and st and not floor_misses and not arm_misses and not misses and dry_clean and closing_clean
    rec('  ### ### **GATE VERDICT : %s**' % ('CLEAR' if clear else 'NOT CLEAR'))
    rec('=' * 100)
    with io.open(OUT, 'w', encoding='utf-8', newline=chr(10)) as fh:
        fh.write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0 if clear else 1


if __name__ == '__main__':
    sys.exit(main())
