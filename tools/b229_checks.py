# -*- coding: utf-8 -*-
"""b229_checks.py -- the b229 gates, routed through the b217 harness.
### AN ADOPTION ACT'S RISK IS THAT IT ADOPTS MORE THAN IT WAS GIVEN, or that a number
### slips in beside a freshly stated target. Each gate carries a must-fail fixture AND a
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

BANK = os.path.join(D, 'b229_statement_adopted.txt')
REG = os.path.join(D, 'b229_registration_2026-08-28.txt')
B228 = os.path.join(D, 'b228_ledger_cell_statement.txt')
B227 = os.path.join(D, 'b227_the_trace.txt')
B10 = os.path.join(D, 'b10_2026-08-17.txt')
B21 = os.path.join(D, 'b21_2026-08-18.txt')
INSTR = os.path.join(ROOT, 'tools', 'e16', 'b38_act10.py')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
SHADOW = os.path.join(SGS, 'Core', 'AggregationCircularityShadow.lean')
TRAILS = os.path.join(PLACE, 'OPEN_TRAILS.md')
NARR = os.path.join(ROOT, 'reports',
                    '2026-08-18-global-section-acts-narrative-v0.15.md')


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def count_re(path, pattern):
    """### A MISSING FILE RETURNS -1, NEVER 0."""
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
    h = Harness(ROOT, 'b229')

    # 1 -- ### THE ADOPTED FORMULA MATCHES THE INSTRUMENT IT CLAIMS AS PROVENANCE.
    h.run('adopted-formula-matches-instrument',
          check=lambda: contains(INSTR, '2.0 * math.log(p) / math.sqrt(p ** k)')
                        and contains(BANK, '2 log p / p^{k/2}'),
          fixture=lambda: contains(FILE_E, '2.0 * math.log(p)'),
          witness=lambda: contains(B228, '2 log p / p^{k/2}'))

    # 2 -- ### wInf IS *NOT* ADOPTED, and the bank says so in terms.
    h.run('wInf-held-to-prime-side',
          check=lambda: contains(BANK, 'HELD TO THE PRIME SIDE'),
          fixture=lambda: contains(B228, 'HELD TO THE PRIME SIDE'),
          witness=lambda: contains(REG, 'HELD TO THE PRIME SIDE'))

    # 3 -- ### THE SIGN IS SHOWN UNFIXED: BOTH act-12 readings are carried, not just one.
    # ### THE FIRST FIXTURE HERE WAS `contains(FILE_E, 'act-12')` AND THE HARNESS REFUSED THE
    # ### CHECK, because File E's docstring DOES say "the act-12 dictionary" -- so the fixture
    # ### PASSED and could not discriminate. ### THAT IS b217's FIRST GUARD, and the repair is
    # ### to test for BOTH READINGS, which File E genuinely carries neither of.
    def names_both_readings(path):
        return contains(path, 'atlas') and contains(path, 'CC dict')

    h.run('both-act12-readings-carried',
          check=lambda: names_both_readings(BANK),
          fixture=lambda: names_both_readings(FILE_E),
          witness=lambda: names_both_readings(NARR))

    # 4 -- ### THE STANDING CLAUSE IS IN THE BANK VERBATIM.
    h.run('standing-clause-carried-verbatim',
          check=lambda: contains(BANK, 'may NEVER define, calibrate, or tune the left side'),
          fixture=lambda: contains(B228, 'may NEVER define, calibrate, or tune'),
          witness=lambda: contains(REG, 'may NEVER define, calibrate, or tune the left side'))

    # 5 -- ### THE NAMED CRIME HAS A COMPILED WITNESS whose proof term is the hypothesis.
    h.run('named-crime-has-compiled-witness',
          check=lambda: contains(SHADOW, 'cweil_is_the_assumption'),
          fixture=lambda: contains(INSTR, 'cweil_is_the_assumption'),
          witness=lambda: contains(BANK, 'cweil_is_the_assumption'))

    # 6 -- b10's grade travels with its quotation: "no promotion either way".
    h.run('b10-grade-travels-with-the-quote',
          check=lambda: contains(BANK, 'no promotion either way'),
          fixture=lambda: contains(B227, 'no promotion either way'),
          witness=lambda: contains(B10, 'no promotion either way'))

    # 7 -- ### THE HAAR CONFLATION IS NAMED, NOT USED.
    h.run('haar-conflation-named-as-double-name',
          check=lambda: contains(BANK, 'DOUBLE-NAME SPECIES') and contains(BANK, 'self-dual Haar'),
          fixture=lambda: contains(B21, 'DOUBLE-NAME SPECIES'),
          witness=lambda: contains(B21, 'self-dual Haar'))

    # 8 -- ### THE ENGINE ITEM'S PRICE IS RECORDED ABSENT, not invented.
    h.run('engine-price-recorded-absent',
          check=lambda: contains(BANK, 'NO PRICE TO QUOTE')
                        and count_re(TRAILS, r'derivative-level engine') == 1,
          fixture=lambda: count_re(TRAILS, r'derivative-level engine') == 0,
          witness=lambda: contains(REG, 'NOT ON THE RECORD'))

    # 9 -- ### NO NUMBER WAS COMPUTED, with a target now stated.
    h.run('no-number-computed-in-this-act',
          check=lambda: contains(BANK, 'NO NUMBER, NO COMPUTATION, NO COMPARISON'),
          fixture=lambda: contains(B10, 'NO NUMBER, NO COMPUTATION, NO COMPARISON'),
          witness=lambda: contains(REG, 'NO NUMBER IS COMPUTED IN THIS ACT'))

    # 10 -- ### THE KERNEL IS UNTOUCHED: this act adopts a statement, it builds nothing.
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
