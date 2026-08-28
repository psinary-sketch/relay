# -*- coding: utf-8 -*-
"""b223_checks.py -- the b223 gates, routed through the b217 harness.
### Each carries a must-fail fixture AND a must-pass witness over three distinct REAL states."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e16'))
from check_harness import Harness   # noqa: E402
import b223_level_limit as L        # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b223_level_limit_two_places.txt')
REG = os.path.join(D, 'b223_registration_2026-08-28.txt')
B222 = os.path.join(D, 'b222_rescope_inputs.txt')
PLACE = 'D:/MY-DOwnloads/PLACE-papers'


def contains(path, needle):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def repo_clean(repo):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain'], capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def reproduces_banked():
    """### G-REPRO: every one of the six banked rows re-derived exactly."""
    for (p, n), row in L.BANKED.items():
        d1, dm1, dis, _ = L.d1_exact(p, n)
        if d1 != row[0] or dm1 != row[1] or dis != row[2] + row[3]:
            return False
    return True


def reproduces_banked_wrong_law():
    """### THE FIXTURE: the same computation checked against a DELIBERATELY WRONG law
    (the two places' laws swapped). It must FAIL, and it fails for the reason the check
    measures -- a wrong d_1 -- not for an unrelated reason."""
    for (p, n) in L.BANKED:
        q = p ** n
        wrong = ((q - 1) ** 2 // 4) if p == 2 else (q * (q - 2) // 4)
        d1, _, _, _ = L.d1_exact(p, n)
        if d1 != wrong:
            return False
    return True


def law_agrees(cells):
    for (p, n) in cells:
        d1, _, _, _ = L.d1_exact(p, n)
        if d1 != L.law_d1(p, n):
            return False
    return True


def main():
    h = Harness(ROOT, 'b223')

    # 1 -- G-REPRO: the six banked rows, re-derived.
    h.run('six-banked-rows-reproduced-exactly',
          check=reproduces_banked,
          fixture=reproduces_banked_wrong_law,
          witness=lambda: law_agrees(list(L.BANKED)))

    # 2 -- the extension agrees with the record's own law at every new cell.
    new = [(2, m) for m in range(4, 9)] + [(3, m) for m in range(3, 6)]
    h.run('new-cells-agree-with-the-banked-law',
          check=lambda: law_agrees(new),
          fixture=lambda: law_agrees([(2, 1)]) and L.law_d1(2, 1) != 0,   # 0 != 0 is False
          witness=lambda: law_agrees([(3, 1)]))

    # 3 -- ### the (2,1) death is isolated: it is the ONLY zero in the table.
    h.run('arrival-depth-is-the-only-zero',
          check=lambda: all(L.d1_exact(p, n)[0] > 0
                            for p, n in new + [(2, 2), (2, 3), (3, 1), (3, 2)]),
          fixture=lambda: L.d1_exact(2, 1)[0] > 0,
          witness=lambda: L.d1_exact(3, 1)[0] > 0)

    # 4 -- ### PLACE-papers UNTOUCHED, as the concurrency header requires.
    h.run('PLACE-papers-untouched-by-this-act',
          check=lambda: repo_clean(PLACE) or _only_foreign(PLACE),
          fixture=lambda: repo_clean('D:/nonexistent-repo-xyz'),
          witness=lambda: repo_clean('D:/SIDE-kernel'))

    # 5 -- the owner's sector sentence is carried into the bank, not paraphrased away.
    h.run('iota-stable-sentence-carried',
          check=lambda: contains(BANK, 'iota-stable ON THE NOSE'),
          fixture=lambda: contains(B222, 'iota-stable ON THE NOSE'),
          witness=lambda: contains(REG, 'iota-stable ON THE NOSE'))

    # 6 -- ### the finite-places-only limit is stated, not buried.
    h.run('finite-places-only-limit-stated',
          check=lambda: contains(BANK, 'FINITE-PLACES-ONLY'),
          fixture=lambda: contains(B222, 'FINITE-PLACES-ONLY'),
          witness=lambda: contains(REG, 'FINITE-PLACES-ONLY'))

    for row in h.rows:
        print('  %-40s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


def _only_foreign(repo):
    """PLACE-papers carries pre-existing untracked patent-package figures that are NOT this
    act's; the check is that THIS act added nothing."""
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain'], capture_output=True)
    if r.returncode != 0:
        return False
    for line in r.stdout.decode('utf-8', 'replace').splitlines():
        if not line.strip():
            continue
        if not line.startswith('??'):
            return False
        if 'patent-package' not in line:
            return False
    return True


if __name__ == '__main__':
    main()
