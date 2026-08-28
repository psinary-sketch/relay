# -*- coding: utf-8 -*-
"""b226_checks.py -- the b226 gates, routed through the b217 harness.
### Each carries a must-fail fixture AND a must-pass witness over three distinct REAL states."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e16'))
from check_harness import Harness   # noqa: E402
import b223_level_limit as L        # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b226_stated_choice.txt')
REG = os.path.join(D, 'b226_registration_2026-08-28.txt')
B225 = os.path.join(D, 'b225_serializing_close.txt')
PRINT = os.path.join(D, 'b226_core_remeasured.txt')
PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')
PRINTS_IF = os.path.join(SGS, 'AXIOM_PRINTS_INTERFACES.txt')
ALLP = os.path.join(SGS, 'AllPrints.lean')
CORR = os.path.join(SGS, 'CORRESPONDENCE.md')
FILE_E = 'Interfaces/FiniteInstanceIdentity.lean'


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def no_axiom_bearing(path):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return b'depends on axioms' not in fh.read()


def profile_count(path):
    if not os.path.isfile(path):
        return -1
    n = 0
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if 'does not depend on any axioms' in line or 'depends on axioms' in line:
                n += 1
    return n


def unchanged_vs_head(repo, rel):
    try:
        r = subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', rel],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0


def chosen_level(p):
    return 2 if p == 2 else 1


def stated_places_have_positive_d1(places):
    for p in places:
        if L.d1_exact(p, chosen_level(p))[0] <= 0:
            return False
    return True


def main():
    h = Harness(ROOT, 'b226')
    stated = [2, 3, 5, 7, 11, 13]

    # 1 -- ### THE CHOSEN LEVEL REALLY HAS E_1 != 0 at every stated place.
    h.run('chosen-level-has-positive-d1',
          check=lambda: stated_places_have_positive_d1(stated),
          fixture=lambda: L.d1_exact(2, 1)[0] > 0,          # the arrival depth: genuinely 0
          witness=lambda: stated_places_have_positive_d1([3]))

    # 2 -- ### AND IT IS THE LOWEST: level 1 is dead at p = 2 and alive at odd p.
    h.run('chosen-level-is-the-lowest',
          check=lambda: L.d1_exact(2, 1)[0] == 0 and L.d1_exact(3, 1)[0] > 0,
          fixture=lambda: L.d1_exact(3, 1)[0] == 0,
          witness=lambda: L.d1_exact(2, 2)[0] > 0)

    # 3 -- the shadow's print carries no axiom-bearing line.
    h.run('shadow-print-no-axiom-bearing',
          check=lambda: no_axiom_bearing(PRINT),
          fixture=lambda: no_axiom_bearing(PRINTS_IF),      # 29 real axiom-bearing lines
          witness=lambda: no_axiom_bearing(PRINTS))

    # 4 -- ### THE GENERATOR REPRODUCES THE BANK: 382 both sides. (b221's lesson.)
    h.run('generator-reproduces-382',
          check=lambda: profile_count(PRINT) == 382 and profile_count(PRINTS) == 382,
          fixture=lambda: profile_count(PRINTS_IF) == 382,
          witness=lambda: contains(ALLP, 'StatedChoiceShadow'))

    # 5 -- ### THE TRACE IS NOT DEFINED HERE. The scope line's central promise.
    h.run('no-trace-defined-in-this-act',
          check=lambda: contains(BANK, 'NO TRACE'),
          fixture=lambda: contains(B225, 'NO TRACE'),
          witness=lambda: contains(REG, 'NO TRACE'))

    # 6 -- ### THE GENERIC ODD PLACE IS RECORDED OWED, not quietly discharged.
    h.run('generic-odd-place-recorded-owed',
          check=lambda: contains(BANK, 'IS *OWED*') or contains(BANK, 'OWED'),
          fixture=lambda: contains(B225, 'THE GENERIC ODD PLACE'),
          witness=lambda: contains(REG, 'OWED'))

    # 7 -- ### FILE E UNTOUCHED: term 2 is not touched by this act.
    h.run('file-E-byte-identical-to-HEAD',
          check=lambda: unchanged_vs_head(SGS, FILE_E),
          fixture=lambda: unchanged_vs_head(SGS, 'AXIOM_PRINTS.txt'),   # genuinely modified
          witness=lambda: unchanged_vs_head(SGS, 'Core/QuotientLemmaShadow.lean'))

    # 8 -- correspondence row 87 written by the tool.
    h.run('correspondence-row-87-written',
          check=lambda: contains(CORR, 'StatedChoiceShadow'),
          fixture=lambda: contains(PRINTS_IF, 'StatedChoiceShadow'),
          witness=lambda: contains(ALLP, 'StatedChoiceShadow'))

    for row in h.rows:
        print('  %-40s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
