# -*- coding: utf-8 -*-
"""b227_checks.py -- the b227 gates, routed through the b217 harness.
### THIS ACT'S CENTRAL CLAIMS ARE ABOUT WHAT IS *NOT* THERE -- no numbers, no adopted
### aggregation, no target comparison -- which is the kind that passes by accident.
### Each gate therefore carries a must-fail fixture AND a must-pass witness over three
### distinct REAL files or paths."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b227_the_trace.txt')
REG = os.path.join(D, 'b227_registration_2026-08-28.txt')
B226 = os.path.join(D, 'b226_stated_choice.txt')
B221 = os.path.join(D, 'b221_cell_level_assembly.txt')
PRINT = os.path.join(D, 'b227_core_remeasured.txt')
PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')
PRINTS_IF = os.path.join(SGS, 'AXIOM_PRINTS_INTERFACES.txt')
ALLP = os.path.join(SGS, 'AllPrints.lean')
CORR = os.path.join(SGS, 'CORRESPONDENCE.md')
SHADOW = os.path.join(SGS, 'Core', 'TraceFactorizationShadow.lean')
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


def main():
    h = Harness(ROOT, 'b227')

    # 1 -- ### NO sorryAx ANYWHERE in the shadow's print. (The first draft had one.)
    h.run('shadow-print-carries-no-sorryax',
          check=lambda: no_axiom_bearing(PRINT) and not contains(PRINT, 'sorryAx'),
          fixture=lambda: no_axiom_bearing(PRINTS_IF),     # 29 real axiom-bearing lines
          witness=lambda: no_axiom_bearing(PRINTS))

    # 2 -- ### THE GENERATOR REPRODUCES THE BANK: 390 both sides (b221's lesson).
    h.run('generator-reproduces-390',
          check=lambda: profile_count(PRINT) == 390 and profile_count(PRINTS) == 390,
          fixture=lambda: profile_count(PRINTS_IF) == 390,
          witness=lambda: contains(ALLP, 'TraceFactorizationShadow'))

    # 3 -- the TAIL joint's defining clause is carried into the bank verbatim.
    h.run('tail-joint-defining-clause-carried',
          check=lambda: contains(BANK, 'DEFINED BY EXACTLY THIS'),
          fixture=lambda: contains(B226, 'DEFINED BY EXACTLY THIS'),
          witness=lambda: contains(REG, 'DEFINED BY EXACTLY THIS'))

    # 4 -- ### THE SPACE MISMATCH IS NAMED, not glossed: b10's own sentence.
    h.run('fourier-half-does-not-descend-carried',
          check=lambda: contains(BANK, 'FOURIER HALF DOES NOT DESCEND'),
          fixture=lambda: contains(B226, 'FOURIER HALF DOES NOT DESCEND'),
          witness=lambda: contains(REG, 'FOURIER HALF DOES NOT DESCEND'))

    # 5 -- ### NO NUMBERS WERE COMPUTED, and the bank says so in terms.
    h.run('no-numbers-computed-said-in-terms',
          check=lambda: contains(BANK, 'NO NUMBERS WERE COMPUTED'),
          fixture=lambda: contains(B226, 'NO NUMBERS WERE COMPUTED'),
          witness=lambda: contains(REG, 'THE NUMBERS WILL NOT BE COMPUTED'))

    # 6 -- ### NO TARGET COMPARISON. b221's (UNDEFINED) is why, and it is cited.
    # ### The witness is 'NO COMPARISON TO ANY TARGET' and not 'REFUSED BY NAME': the
    # ### registration line-wraps the latter as "REFUSED BY / NAME", so it is not a
    # ### contiguous string there. ### THE HARNESS'S WITNESS GUARD CAUGHT THAT AND REFUSED
    # ### the check rather than running it against a witness that could not pass.
    h.run('no-target-comparison-refused-by-name',
          check=lambda: contains(BANK, 'REFUSED BY NAME'),
          fixture=lambda: contains(B226, 'NO COMPARISON TO ANY TARGET'),
          witness=lambda: contains(REG, 'NO COMPARISON TO ANY TARGET'))

    # 7 -- ### TERM 2 UNTOUCHED: File E byte-identical to HEAD.
    h.run('file-E-byte-identical-to-HEAD',
          check=lambda: unchanged_vs_head(SGS, FILE_E),
          fixture=lambda: unchanged_vs_head(SGS, 'AXIOM_PRINTS.txt'),   # genuinely modified
          witness=lambda: unchanged_vs_head(SGS, 'Core/QuotientLemmaShadow.lean'))

    # 8 -- correspondence row 88 written by the tool.
    h.run('correspondence-row-88-written',
          check=lambda: contains(CORR, 'TraceFactorizationShadow'),
          fixture=lambda: contains(PRINTS_IF, 'TraceFactorizationShadow'),
          witness=lambda: contains(ALLP, 'TraceFactorizationShadow'))

    # 9 -- the shadow declares its Int stand-in rather than implying an order on C.
    h.run('shadow-declares-its-stand-in',
          check=lambda: contains(SHADOW, 'No ordering of'),
          fixture=lambda: contains(B221, 'No ordering of'),
          witness=lambda: contains(BANK, 'NO ORDERING OF C IS USED OR IMPLIED'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
