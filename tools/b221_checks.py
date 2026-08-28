# -*- coding: utf-8 -*-
"""b221_checks.py -- the b221 gates, routed through the b217 harness.

### EVERY CHECK CARRIES A MUST-FAIL FIXTURE **AND** A MUST-PASS WITNESS, and the three
### states are ### THREE DISTINCT **REAL** FILES OR PATHS.
### The fixtures fail for the reason the check measures -- the zero-axiom fixture is the
### Interfaces print, which genuinely carries 29 axiom-bearing lines; the untouched-file
### fixture is AllPrints.lean, which this act genuinely DID modify.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
D = os.path.join(ROOT, 'data')
R = os.path.join(ROOT, 'reports')

BANK = os.path.join(D, 'b221_cell_level_assembly.txt')
B215 = os.path.join(D, 'b215_term2_statement_before_file.txt')
PURITY = os.path.join(R, '2026-08-19-e1-unit-purity.md')
CORE_RM = os.path.join(D, 'b221_core_remeasured.txt')
IFACE = os.path.join(D, 'b221_interfaces_print.txt')

PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')
PRINTS_IF = os.path.join(SGS, 'AXIOM_PRINTS_INTERFACES.txt')
ALLPRINTS = os.path.join(SGS, 'AllPrints.lean')
IFACE_DIR = os.path.join(SGS, 'Interfaces')

FILE_E = 'Interfaces/FiniteInstanceIdentity.lean'
QLS = 'Core/QuotientLemmaShadow.lean'
AP = 'AllPrints.lean'


def read_bytes(path):
    if not os.path.isfile(path):
        return None
    with open(path, 'rb') as fh:
        return fh.read()


def no_axiom_bearing(path):
    """True iff the file holds NO 'depends on axioms' line.
       ### A MISSING FILE IS FALSE, NEVER A PASS."""
    b = read_bytes(path)
    return False if b is None else (b'depends on axioms' not in b)


def profile_count(path):
    b = read_bytes(path)
    if b is None:
        return -1
    n = 0
    for line in b.decode('utf-8', 'replace').splitlines():
        if 'does not depend on any axioms' in line or 'depends on axioms' in line:
            n += 1
    return n


def contains(path, needle):
    b = read_bytes(path)
    return False if b is None else (needle.encode('utf-8', 'replace') in b)


def unchanged_vs_head(repo, relpath):
    """True iff `relpath` is byte-identical to HEAD. ### A GIT FAILURE IS FALSE."""
    try:
        r = subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0


def no_file_starting(directory, prefix):
    if not os.path.isdir(directory):
        return False           # ### a missing directory is not evidence of absence
    return not any(n.startswith(prefix) for n in os.listdir(directory))


def main():
    h = Harness(ROOT, 'b221')

    # 1 -- G-OLEAN half 1: the re-measured Core print carries no axiom-bearing line.
    h.run('core-remeasure-has-no-axiom-bearing-line',
          check=lambda: no_axiom_bearing(CORE_RM),
          fixture=lambda: no_axiom_bearing(IFACE),        # 29 real axiom-bearing lines
          witness=lambda: no_axiom_bearing(PRINTS))

    # 2 -- G-OLEAN half 1: the count is 375, matching the bank.
    h.run('core-remeasure-is-375',
          check=lambda: profile_count(CORE_RM) == 375,
          fixture=lambda: profile_count(PRINTS_IF) == 375,
          witness=lambda: profile_count(PRINTS) == 375)

    # 3 -- G-OLEAN half 2: 29 Interfaces profiles.
    h.run('interfaces-print-is-29',
          check=lambda: profile_count(IFACE) == 29,
          fixture=lambda: profile_count(PRINTS) == 29,
          witness=lambda: profile_count(PRINTS_IF) == 29)

    # 4 -- ### FILE E IS UNTOUCHED. The scope line's central promise.
    h.run('file-E-byte-identical-to-HEAD',
          check=lambda: unchanged_vs_head(SGS, FILE_E),
          fixture=lambda: unchanged_vs_head(SGS, AP),     # genuinely modified this act
          witness=lambda: unchanged_vs_head(SGS, QLS))

    # 5 -- ### NOTHING WAS BUILT: no CellAssembly file exists.
    h.run('no-CellAssembly-file-was-written',
          check=lambda: no_file_starting(IFACE_DIR, 'CellAssembly'),
          fixture=lambda: no_file_starting(IFACE_DIR, 'FiniteInstance'),   # that one exists
          witness=lambda: no_file_starting(IFACE_DIR, 'Zz'))

    # 6 -- the purity verdict that decides the act is carried into the bank.
    h.run('purity-verdict-carried-into-bank',
          check=lambda: contains(BANK, 'MIXED-FORCED'),
          fixture=lambda: contains(B215, 'MIXED-FORCED'),  # a real owner that lacks it
          witness=lambda: contains(PURITY, 'MIXED-FORCED'))

    # 7 -- the b220 generator defect is REPAIRED: AllPrints names the module.
    h.run('allprints-generator-includes-b220-module',
          check=lambda: contains(ALLPRINTS, 'AggregationCircularityShadow'),
          fixture=lambda: contains(PRINTS_IF, 'AggregationCircularityShadow'),
          witness=lambda: contains(PRINTS, 'AggregationCircularityShadow'))

    for row in h.rows:
        print('  %-44s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
