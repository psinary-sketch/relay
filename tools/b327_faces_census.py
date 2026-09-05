# -*- coding: utf-8 -*-
"""b327_faces_census.py -- THE LEDGER CENSUS, EXTENDED TO THE NEW LEDGER. ### **WHAT IS MISSING FROM
### `FACES_LEDGER.md`, COUNTED.**

### ### **THE MATCHER IS b307's, IMPORTED** (`b307_handoff_census.present`: a word-boundary match for
### ids, a plain one otherwise) -- the same mechanical rule that licenses a phrase about `HANDOFF.md`
### now counts, for the faces ledger: ### (1) the rows the order named, by id; ### (2) the faces by the
### names the order used; ### (3) the three trail IDs the cascades owe; ### (4) the cascade section and
### its pair count `N(N-1)/2`.
### ### **THE LIMITS ARE b307's:** ### it counts NAMES, not understanding; it is about ONE ledger; the
### lists are this act's and are declared here so a reader can disagree with the scope, not the number.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b307_handoff_census as H  # noqa: E402

LEDGER = r'D:\MY-DOwnloads\PLACE-papers\FACES_LEDGER.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

IDS = ['R1', 'R2', 'R3', 'R4', 'R5', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'L1']
NAMES = ['universality', 'ConservationHypothesis', 'totality', 'balance', 'spectral-realization',
         'finite-instance identity', 'Sonin margin', 'Li margin', 'The space is the wall',
         'fixed-point silence', 'two-radius family', 'Epstein negative control', 'Li-to-Weil bridge']
TRAILS = ['W-ORD-LI-WEIL-BRIDGE', 'W-ORD-DISCRIMINATING-FAMILY', 'W-ORD-LI-FAMILY-CONTROL']
MARK = '<!-- b327 cascades -->'


def main(argv):
    label = argv[0] if argv else 'CENSUS'
    print('=' * 100)
    print('b327_faces_census.py -- %s. ### WHAT IS MISSING FROM `FACES_LEDGER.md`, COUNTED.' % label)
    print('=' * 100)
    ok = H.self_test(verbose=False)
    print('  b307 matcher self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        return 2
    if not os.path.exists(LEDGER):
        print('  ### HARD FAILURE -- THE LEDGER IS NOT AT %s' % LEDGER)
        return 2
    text = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    rows = [ln for ln in text.splitlines() if ln.startswith('| ') and ln.split('|')[1].strip() in IDS]
    mi = [i for i in IDS if not any(ln.split('|')[1].strip() == i for ln in rows)]
    mn = [n for n in NAMES if not H.present(text, n)]
    mt = [t for t in TRAILS if not H.present(text, t)]
    pairs = len(re.findall(r'^\| [RFL]\d+–[RFL]\d+ \|', text, re.M))
    expect = len(IDS) * (len(IDS) - 1) // 2
    print('  ledger        : %s' % os.path.basename(LEDGER))
    print('  bytes / lines : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print()
    print('  ### (1) THE ROWS THE ORDER NAMED, BY ID -- %d checked, %d MISSING %s' % (len(IDS), len(mi), mi if mi else ''))
    print('  ### (2) THE FACES, BY NAME          -- %d checked, %d MISSING %s' % (len(NAMES), len(mn), mn if mn else ''))
    print('  ### (3) THE OWED TRAILS, BY ID      -- %d checked, %d MISSING %s' % (len(TRAILS), len(mt), mt if mt else ''))
    print('  ### (4) THE CASCADES                -- section present : %s ; pair lines %d of N(N-1)/2 = %d'
          % (MARK in text, pairs, expect))
    total = len(mi) + len(mn) + len(mt) + (0 if (MARK in text and pairs == expect) else 1)
    print()
    print('  ### ### **TOTAL MISSING : %d**' % total)
    if total == 0:
        print('  ### ### **THE CENSUS HAS COUNTED WHAT IS MISSING AND FOUND NOTHING -- FOR THIS LEDGER AND NO OTHER.**')
    print('  ### It counts NAMES rather than understanding. ### A ledger naming every face in one row each')
    print('  ### passes this census and its grades are still its owning acts\' to defend.')
    print('=' * 100)
    return 0 if total == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
