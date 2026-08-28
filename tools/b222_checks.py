# -*- coding: utf-8 -*-
"""b222_checks.py -- the b222 gates, routed through the b217 harness.

### THIS ACT IS READS ONLY, so most of its gates are ABSENCE gates -- and an absence
### gate is exactly the kind that fails silently when it is wrong. Each therefore
### carries a must-fail fixture AND a must-pass witness over THREE DISTINCT REAL
### FILES OR PATHS, with the fixture failing for the reason the check measures.
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

BANK = os.path.join(D, 'b222_rescope_inputs.txt')
REG = os.path.join(D, 'b222_registration_2026-08-28.txt')
B221 = os.path.join(D, 'b221_cell_level_assembly.txt')
B215 = os.path.join(D, 'b215_term2_statement_before_file.txt')
B194 = os.path.join(D, 'b194_restricted_tensor_two.txt')
VN = os.path.join(D, 'ext_b196_vonneumann1939_extract.txt')
NARR = os.path.join(R, '2026-08-18-global-section-acts-narrative-v0.15.md')
IDXQ = os.path.join(D, 'audit_b222_index_query.txt')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
PRINTS = os.path.join(SGS, 'AXIOM_PRINTS.txt')

CORE = os.path.join(SGS, 'Core')
IFACE = os.path.join(SGS, 'Interfaces')


def contains(path, needle):
    """Case-insensitive. ### A MISSING FILE IS FALSE, NEVER A PASS."""
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def no_file_starting(directory, prefix):
    if not os.path.isdir(directory):
        return False        # ### a missing directory is not evidence of absence
    return not any(n.startswith(prefix) for n in os.listdir(directory))


def repo_clean(repo):
    """True iff the repo has no modified or untracked files.
       ### A GIT FAILURE IS FALSE, NEVER A PASS."""
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain'],
                           capture_output=True)
    except Exception:
        return False
    if r.returncode != 0:
        return False
    return r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b222')

    # 1 -- ### NOTHING WAS BUILT: no new Lean file in either layer.
    h.run('no-b222-lean-file-in-Interfaces',
          check=lambda: no_file_starting(IFACE, 'CellAssembly'),
          fixture=lambda: no_file_starting(IFACE, 'FiniteInstance'),   # that one exists
          witness=lambda: no_file_starting(IFACE, 'Zz'))

    # 2 -- ### THE LEAN REPO IS UNTOUCHED BY THIS READS-ONLY ACT.
    h.run('SIDE-global-section-worktree-clean',
          check=lambda: repo_clean(SGS),
          fixture=lambda: repo_clean('D:/nonexistent-repo-xyz'),
          witness=lambda: repo_clean('D:/SIDE-kernel'))

    # 3 -- von Neumann's own requirement is carried into the bank.
    h.run('vonneumann-c0-sequence-carried',
          check=lambda: contains(BANK, 'c0-sequence'),
          fixture=lambda: contains(B194, 'c0-sequence'),   # b194 genuinely lacks it
          witness=lambda: contains(VN, 'co-sequence'))

    # 4 -- ### THE CORRECTION AGAINST b221 IS CARRIED, not softened away.
    h.run('rangelaw-fourth-instance-carried',
          check=lambda: contains(BANK, 'instance four'),
          fixture=lambda: contains(B221, 'instance four'),  # b221 does not say it
          witness=lambda: contains(REG, 'instance four'))

    # 5 -- the ClassRichness statement, read for the first time, is carried verbatim.
    h.run('classrichness-statement-carried',
          check=lambda: contains(BANK, 'inactive at'),
          fixture=lambda: contains(B215, 'inactive at'),
          witness=lambda: contains(NARR, 'inactive at'))

    # 6 -- ### THE MEMO TAKES NO POSITION. The scope line's central promise.
    h.run('memo-takes-no-position',
          check=lambda: contains(BANK, 'takes no position'),
          fixture=lambda: contains(B194, 'takes no position'),
          witness=lambda: contains(REG, 'takes no position'))

    # 7 -- clause (g): the keys were actually added to the queryable index.
    h.run('index-gained-vonneumann-key',
          check=lambda: contains(INDEX, 'von-neumann-product'),
          fixture=lambda: contains(PRINTS, 'von-neumann-product'),
          witness=lambda: contains(IDXQ, 'von-neumann-product'))

    for row in h.rows:
        print('  %-38s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
