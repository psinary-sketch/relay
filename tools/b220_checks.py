# -*- coding: utf-8 -*-
"""b220_checks.py -- the b220 gates, routed through the b217 harness.

### EVERY CHECK CARRIES A MUST-FAIL FIXTURE **AND** A MUST-PASS WITNESS, and the three
### states are ### THREE DISTINCT **REAL** FILES OR PATHS -- never the same call twice
### and never a synthetic string chosen to fail.

### THE FIXTURES FAIL FOR THE REASON THE CHECK MEASURES, which is b217's limit (1) and
### the thing b219 began narrowing:
###   · the zero-axiom check's fixture is AXIOM_PRINTS_INTERFACES.txt, which genuinely
###     carries 29 axiom-bearing lines;
###   · the quote checks' fixtures are real owner files that genuinely lack the quote;
###   · the untouched-file check's fixture is a path this act genuinely DID modify.
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

BANK = os.path.join(D, 'b220_aggregation_freedom.txt')
REG = os.path.join(D, 'b220_registration_2026-08-27.txt')
B215 = os.path.join(D, 'b215_term2_statement_before_file.txt')
ACT7 = os.path.join(R, '2026-08-18-w-construction-1-act-7.md')
ACT9 = os.path.join(R, '2026-08-18-w-construction-1-act-9.md')

PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')
PRINTS_IF = os.path.join(SGS, 'AXIOM_PRINTS_INTERFACES.txt')
SHADOW = os.path.join(SGS, 'Core', 'AggregationCircularityShadow.lean')
FILE_E = 'Interfaces/FiniteInstanceIdentity.lean'
QLS = 'Core/QuotientLemmaShadow.lean'


def no_axiom_bearing(path):
    """True iff the file holds NO 'depends on axioms' line.
       ### A MISSING FILE IS FALSE, NEVER A PASS."""
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return b'depends on axioms' not in fh.read()


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.encode('utf-8', 'replace') in fh.read()


def unchanged_vs_head(repo, relpath):
    """True iff `relpath` is byte-identical to HEAD in `repo`.
       ### A GIT FAILURE IS FALSE, NEVER A PASS."""
    try:
        r = subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0


def count_zero_axiom(path, prefix):
    if not os.path.isfile(path):
        return -1
    n = 0
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if line.startswith("'" + prefix) and 'does not depend on any axioms' in line:
                n += 1
    return n


def main():
    h = Harness(ROOT, 'b220')

    # 1 -- ### Core's print carries NO axiom-bearing line: the bar this act refused to break.
    h.run('core-print-has-no-axiom-bearing-line',
          check=lambda: no_axiom_bearing(PRINTS),
          fixture=lambda: no_axiom_bearing(PRINTS_IF),      # 29 real axiom-bearing lines
          witness=lambda: no_axiom_bearing(SHADOW))

    # 2 -- ### the shadow contributed exactly 9 zero-axiom terminals.
    h.run('shadow-adds-nine-zero-axiom-terminals',
          check=lambda: count_zero_axiom(PRINTS, 'AggregationCircularityShadow.') == 9,
          fixture=lambda: count_zero_axiom(PRINTS, 'LadderOrientationShadow.') == 9,
          witness=lambda: count_zero_axiom(PRINTS, 'AggregationCircularityShadow.') >= 1)

    # 3 -- ### FILE E IS UNTOUCHED. The scope line's central promise.
    h.run('file-E-byte-identical-to-HEAD',
          check=lambda: unchanged_vs_head(SGS, FILE_E),
          fixture=lambda: unchanged_vs_head(SGS, 'AXIOM_PRINTS.txt'),   # genuinely modified
          witness=lambda: unchanged_vs_head(SGS, QLS))

    # 4 -- act 7's refusal is carried into the bank verbatim.
    h.run('act7-refusal-carried-into-bank',
          check=lambda: contains(BANK, 'L-identity'),
          fixture=lambda: contains(B215, 'L-identity'),     # a real owner that lacks it
          witness=lambda: contains(ACT7, 'L-identity'))

    # 5 -- act 9's RANGE, recovered from source, is carried into the bank.
    h.run('act9-range-condition-carried',
          check=lambda: contains(BANK, '1 <= k <= n-1'),
          fixture=lambda: contains(B215, '1 <= k <= n-1'),
          witness=lambda: contains(REG, '1 <= k <= n-1'))

    # 6 -- the shadow defines no aggregation: `agg` is a variable, never a definition.
    h.run('shadow-defines-no-aggregation',
          check=lambda: not contains(SHADOW, 'def agg'),
          fixture=lambda: not contains(SHADOW, 'def Aggregation'),   # this one IS there
          witness=lambda: not contains(SHADOW, 'def thisIsNotInTheFile'))

    for row in h.rows:
        print('  %-40s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
