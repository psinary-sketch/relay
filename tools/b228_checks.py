# -*- coding: utf-8 -*-
"""b228_checks.py -- the b228 gates, routed through the b217 harness.
### THIS ACT'S CLAIMS ARE ABOUT WHAT THE RECORD DOES AND DOES NOT CONTAIN, which is
### the kind that passes by accident. Each gate carries a must-fail fixture AND a
### must-pass witness over three distinct REAL files or paths."""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b228_ledger_cell_statement.txt')
REG = os.path.join(D, 'b228_registration_2026-08-28.txt')
B227 = os.path.join(D, 'b227_the_trace.txt')
B221 = os.path.join(D, 'b221_cell_level_assembly.txt')
B10 = os.path.join(D, 'b10_2026-08-17.txt')
INSTR = os.path.join(ROOT, 'tools', 'e16', 'b38_act10.py')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
GLOBAL = os.path.join(SGS, 'Interfaces', 'GlobalSection.lean')
CONS = os.path.join(PLACE, 'archive', '2026-08-27-trim-backfill',
                    'CONSERVATION_OF_SPECTRA_REFINED.md')


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def count_re(path, pattern):
    """### A MISSING FILE RETURNS -1, NEVER 0 -- an absent file must not read as an absence."""
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return len(re.findall(pattern, fh.read(), re.I))


def repo_untouched(repo):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain'], capture_output=True)
    except Exception:
        return False
    if r.returncode != 0:
        return False
    for line in r.stdout.decode('utf-8', 'replace').splitlines():
        if line.strip() and not (line.startswith('??') and 'patent-package' in line):
            return False
    return True


def main():
    h = Harness(ROOT, 'b228')

    # 1 -- ### THE INSTRUMENT REALLY CARRIES THE PRIME-SIDE WEIGHT. The act's central find.
    h.run('instrument-carries-2logp-over-sqrt',
          check=lambda: contains(INSTR, '2.0 * math.log(p) / math.sqrt(p ** k)'),
          fixture=lambda: contains(FILE_E, '2.0 * math.log(p)'),   # the kernel has no such code
          witness=lambda: contains(BANK, '2 log p / p^{k/2}'))

    # 2 -- ### AND THE CUTOFF IS b17's STAIRCASE, character for character.
    h.run('instrument-cutoff-is-the-staircase',
          check=lambda: contains(INSTR, 'while p ** k <= a * a'),
          fixture=lambda: contains(FILE_E, 'while p ** k <= a * a'),
          witness=lambda: contains(BANK, "b17's STAIRCASE"))

    # 3 -- ### FILE E CARRIES ONLY THE TYPE: no definition of wInf/wPrimes in the kernel.
    h.run('file-E-carries-only-the-type',
          check=lambda: contains(FILE_E, 'wPrimes : ℝ') and not contains(FILE_E, 'math.log'),
          fixture=lambda: contains(INSTR, 'wPrimes'),      # the instrument has no such field
          witness=lambda: contains(FILE_E, 'wInf : ℝ'))

    # 4 -- ### GlobalSection.lean carries NO Weil interface (read whole this act).
    h.run('globalsection-has-no-weil-interface',
          check=lambda: not contains(GLOBAL, 'weil'),
          fixture=lambda: not contains(FILE_E, 'weil'),    # File E genuinely does
          witness=lambda: not contains(GLOBAL, 'wPrimes'))

    # 5 -- ### JUNCTION READ 2 IS MEASURED, NOT ASSERTED: zero intertwin, zero x~px.
    h.run('conservation-doc-has-no-intertwining',
          check=lambda: count_re(CONS, r'intertwin') == 0 and count_re(CONS, r'scaling quotient') == 0,
          fixture=lambda: count_re(B10, r'intertwin|orbit space') == 0,   # b10 genuinely has one
          witness=lambda: count_re(CONS, r's-dark') > 0)

    # 6 -- b10's non-descent sentence is carried into the bank.
    h.run('non-descent-sentence-carried',
          check=lambda: contains(BANK, 'FOURIER HALF DOES NOT DESCEND'),
          fixture=lambda: contains(B221, 'FOURIER HALF DOES NOT DESCEND'),
          witness=lambda: contains(B227, 'FOURIER HALF DOES NOT DESCEND'))

    # 7 -- ### THE DOUBLE-NAME HAZARD ON "local factor" IS NAMED, not built on.
    h.run('local-factor-double-name-named',
          check=lambda: contains(BANK, 'DOUBLE-NAME SPECIES'),
          fixture=lambda: contains(B221, 'local factor'),  # b221 uses it without the hazard
          witness=lambda: contains(REG, 'DOUBLE-NAME SPECIES'))

    # 8 -- ### NO NUMBER WAS COMPUTED: b227's refusal is carried forward.
    h.run('no-number-computed-refusal-carried',
          check=lambda: contains(BANK, 'NO NUMBER'),
          fixture=lambda: contains(B221, 'NO COMPUTATION, NO COMPARISON, NO NUMBER'),
          witness=lambda: contains(REG, 'NO NUMBER'))

    # 9 -- ### THE KERNEL IS UNTOUCHED: this act is reads and a statement only.
    h.run('kernel-untouched-by-this-act',
          check=lambda: repo_untouched(SGS),
          fixture=lambda: repo_untouched('D:/nonexistent-repo-xyz'),
          witness=lambda: repo_untouched('D:/SIDE-kernel'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
