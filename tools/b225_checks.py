# -*- coding: utf-8 -*-
"""b225_checks.py -- the b225 gates, routed through the b217 harness.
### A FILING ACT'S GATES ARE MOSTLY ABOUT WHAT IS AND IS NOT ON THE PAGE, which is the kind
### that passes by accident; each therefore carries a must-fail fixture AND a must-pass
### witness over three distinct REAL files."""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
PLACE = 'D:/MY-DOwnloads/PLACE-papers'

BANK = os.path.join(D, 'b225_serializing_close.txt')
REG = os.path.join(D, 'b225_registration_2026-08-28.txt')
B223 = os.path.join(D, 'b223_level_limit_two_places.txt')
B224 = os.path.join(D, 'b224_segre_three_cells.txt')
B222 = os.path.join(D, 'b222_rescope_inputs.txt')
CHAIN = os.path.join(PLACE, 'phase2', 'method', 'THE_IDENTITY_CHAIN.md')
FIND = os.path.join(PLACE, 'FINDINGS.md')
LOOM = os.path.join(PLACE, 'VERIFICATION_LOOM.md')
KEY15 = os.path.join(PLACE, 'phase1.5', 'proofs', 'INDEX_ARITY_AT_THE_CRITICAL_LINE.md')


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def unchanged_vs_head(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'diff', '--quiet', 'HEAD', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0


def cellv(p, n):
    f = os.path.join(D, 'b224_cells', 'cell_%d_%d.json' % (p, n))
    return json.load(open(f))['verdict'] if os.path.isfile(f) else None


def main():
    h = Harness(ROOT, 'b225')

    # 1 -- the ruling is quoted VERBATIM in the chain, not paraphrased.
    key = 'DECIDED-BY-RE-SCOPE'
    h.run('ruling-quoted-verbatim-in-the-chain',
          check=lambda: contains(CHAIN, key) and contains(CHAIN, 'STATED CHOICE'),
          fixture=lambda: contains(B222, key),          # b222 predates the ruling
          witness=lambda: contains(BANK, key))

    # 2 -- ### THE STATED CHOICE IS NOT RUN: the bank says so in terms.
    h.run('stated-choice-explicitly-not-run',
          check=lambda: contains(BANK, 'IT IS NOT STATED'),
          fixture=lambda: contains(B223, 'IT IS NOT STATED'),
          witness=lambda: contains(REG, 'IT IS NOT STATED'))

    # 3 -- ### b194 IS NOT REPEALED, and the filing says so.
    h.run('b194-retirement-not-repealed',
          check=lambda: contains(CHAIN, 'is NOT repealed') or contains(CHAIN, 'not repealed'),
          fixture=lambda: contains(B223, 'not repealed'),
          witness=lambda: contains(BANK, 'NOT REPEALED'))

    # 4 -- ### THE TWO QUARTER-DENSITY GRADES ARE UNFUSED, said on the page.
    h.run('quarter-density-grades-unfused',
          check=lambda: contains(FIND, 'not shown to be the same quarter'),
          fixture=lambda: contains(B222, 'not shown to be the same quarter'),
          witness=lambda: contains(BANK, 'NOT SHOWN TO BE THE SAME QUARTER'))

    # 5 -- ### THE CURIO IS FILED AS A CURIO, with its non-promotion stated.
    h.run('curio-filed-as-curio-not-finding',
          check=lambda: contains(FIND, 'A CURIO, NOT A FINDING'),
          fixture=lambda: contains(B223, 'A CURIO, NOT A FINDING'),
          witness=lambda: contains(BANK, 'AS A CURIO, NOT A FINDING'))

    # 6 -- ### THE WANTED POSTER IS LEFT STANDING, not marked answered.
    h.run('wanted-poster-left-standing',
          check=lambda: contains(FIND, 'LEFT STANDING') and not contains(FIND,
                                                                        'answered-by-the-arc'),
          fixture=lambda: contains(B223, 'LEFT STANDING'),
          witness=lambda: contains(BANK, 'LEFT STANDING'))

    # 7 -- ### 1.5a-7 IS NOT EDITED by this act, as the ferry requires.
    h.run('keystone-1-5a-7-not-edited',
          check=lambda: (not os.path.isfile(KEY15)) or unchanged_vs_head(PLACE,
                        'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md'),
          fixture=lambda: unchanged_vs_head(PLACE, 'no/such/path/at/all.md') is False,
          witness=lambda: unchanged_vs_head(PLACE, 'FINDINGS.md'))

    # 8 -- (3,2) is serialized UNDECIDED, not quietly upgraded.
    h.run('cell-3-2-serialized-undecided',
          check=lambda: cellv(3, 2) == 'UNDECIDED' and contains(CHAIN, 'UNDECIDED'),
          fixture=lambda: cellv(5, 1) == 'UNDECIDED',
          witness=lambda: cellv(2, 3) == 'NONE')

    for row in h.rows:
        print('  %-40s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
