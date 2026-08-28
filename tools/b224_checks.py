# -*- coding: utf-8 -*-
"""b224_checks.py -- the b224 gates, routed through the b217 harness.
### Each carries a must-fail fixture AND a must-pass witness over three distinct REAL states."""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e16'))
from check_harness import Harness   # noqa: E402
import b224_segre as B              # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
CELLS = os.path.join(D, 'b224_cells')
BANK = os.path.join(D, 'b224_segre_three_cells.txt')
REG = os.path.join(D, 'b224_registration_2026-08-28.txt')
B223 = os.path.join(D, 'b223_level_limit_two_places.txt')
PLACE = 'D:/MY-DOwnloads/PLACE-papers'


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def cell(p, n):
    f = os.path.join(CELLS, 'cell_%d_%d.json' % (p, n))
    if not os.path.isfile(f):
        return None
    return json.load(open(f))


def g_repro():
    """### G-REPRO: (2,2) MIXED-FORCED by THIS act's generalized instrument."""
    K = B.Cyc(2, 16)
    ell, g = B.find_ell_g(16)
    basis = B.e1_basis(K, 2, 2, 2, ell, g)
    if len(basis) != 2:
        return False
    mats = [B.schmidt_matrix(K, u, 2, 2) for _, _, u in basis]
    forms = B.quadrics(K, mats, 4)
    tgt = len(B.monomials(2, 2))
    r, _ = B.rank_incremental(K, B.quadric_rows(K, forms, 2, 2), tgt, target=tgt)
    return r == tgt


def g_repro_wrong_target():
    """### THE FIXTURE: the same computation asked for a rank ONE HIGHER than dim S_2.
    It must FAIL, and it fails for the reason the check measures -- an unattainable rank."""
    K = B.Cyc(2, 16)
    ell, g = B.find_ell_g(16)
    basis = B.e1_basis(K, 2, 2, 2, ell, g)
    mats = [B.schmidt_matrix(K, u, 2, 2) for _, _, u in basis]
    forms = B.quadrics(K, mats, 4)
    tgt = len(B.monomials(2, 2))
    r, _ = B.rank_incremental(K, B.quadric_rows(K, forms, 2, 2), tgt, target=tgt)
    return r == tgt + 1


def certified_none(p, n):
    c = cell(p, n)
    if c is None or c.get('verdict') != 'NONE':
        return False
    d = c['degrees'][-1]
    return d['rank'] == d['dim']


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
    h = Harness(ROOT, 'b224')

    # 1 -- ### G-REPRO before any open cell.
    h.run('g-repro-2-2-mixed-forced',
          check=g_repro,
          fixture=g_repro_wrong_target,
          witness=lambda: certified_none(5, 1))

    # 2 -- (5,1) certified NONE with rank == dim.
    h.run('cell-5-1-certified-none',
          check=lambda: certified_none(5, 1),
          fixture=lambda: certified_none(3, 2),     # genuinely UNDECIDED
          witness=lambda: certified_none(2, 3))

    # 3 -- (2,3) certified NONE with rank == dim.
    h.run('cell-2-3-certified-none',
          check=lambda: certified_none(2, 3),
          fixture=lambda: certified_none(3, 2),
          witness=lambda: certified_none(5, 1))

    # 4 -- ### (3,2) IS RECORDED UNDECIDED, NOT QUIETLY OMITTED.
    h.run('cell-3-2-recorded-undecided',
          check=lambda: (cell(3, 2) or {}).get('verdict') == 'UNDECIDED',
          fixture=lambda: (cell(5, 1) or {}).get('verdict') == 'UNDECIDED',
          witness=lambda: (cell(3, 2) or {}).get('obstruction') is not None)

    # 5 -- ### the one-directionality is stated in the bank, not left implicit.
    h.run('one-directional-caveat-stated',
          check=lambda: contains(BANK, 'ONE-DIRECTIONAL'),
          fixture=lambda: contains(B223, 'ONE-DIRECTIONAL'),
          witness=lambda: contains(REG, 'one-directional')
                          or contains(os.path.join(ROOT, 'tools', 'e16', 'b224_segre.py'),
                                      'ONE-DIRECTIONAL'))

    # 6 -- ### the G-RESUME shortfall is admitted, not reported as held.
    h.run('g-resume-shortfall-admitted',
          check=lambda: contains(BANK, 'PER-CELL ONLY'),
          fixture=lambda: contains(REG, 'PER-CELL ONLY'),
          witness=lambda: contains(os.path.join(CELLS, 'cell_3_2.json'), 'resume_shortfall'))

    # 7 -- ### PLACE-papers untouched by this act.
    h.run('PLACE-papers-untouched-by-this-act',
          check=lambda: repo_untouched(PLACE),
          fixture=lambda: repo_untouched('D:/nonexistent-repo-xyz'),
          witness=lambda: repo_untouched('D:/SIDE-kernel'))

    for row in h.rows:
        print('  %-40s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
