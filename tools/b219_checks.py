# -*- coding: utf-8 -*-
"""b219_checks.py -- the b219 gates, routed through the b217 harness.

### EVERY CHECK CARRIES A MUST-FAIL FIXTURE **AND** A MUST-PASS WITNESS, and the three
### states (check / fixture / witness) are ### THREE DISTINCT REAL STATES, never the same
### call twice.

### AND ONE DELIBERATE IMPROVEMENT ON b217's OWN FIRST DAY OF SERVICE. b217's report
### recorded, against itself: "three of the four fixtures are the same trivial shape
### (must_contain='### never'), which fails for a reason unrelated to what the check
### measures. ### THAT IS EXACTLY LIMIT (1) IN THE TOOL'S HEADER."
### ### HERE THE STRING-PRESENCE FIXTURES GREP **THE SAME STRING** IN **A REAL FILE THAT
### ### GENUINELY LACKS IT**, so the fixture fails for the reason the check measures --
### ### absence of that string from that file -- and not because the string is nonsense.
### ### THE LIMIT IS NOT CLOSED BY THIS (the harness still cannot tell WHY a fixture
### ### failed); it is ### NARROWED BY CONSTRUCTION, and only that is claimed.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b219_what_sigma_even_weights.txt')
REG = os.path.join(D, 'b219_registration_2026-08-27.txt')
B199 = os.path.join(D, 'b199_archimedean_nonvanishing.txt')
B109 = os.path.join(D, 'b109_apportionment_derivation.txt')


# ---------------------------------------------------------------- primitives
def contains(path, needle):
    """True iff the file holds the string. ### A MISSING FILE IS FALSE, NEVER A PASS --
       b216's empty-stdout species in file form."""
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.encode('utf-8', 'replace') in fh.read()


def absent_in_dir(directory, prefix):
    """True iff NO file in `directory` starts with `prefix`."""
    if not os.path.isdir(directory):
        return False          # ### a missing directory is not evidence of absence
    return not any(n.startswith(prefix) for n in os.listdir(directory))


def even_share(terms):
    """terms: list of (index, value). Returns the even-index share."""
    tot = sum(v for _, v in terms)
    ev = sum(v for i, v in terms if i % 2 == 0)
    return ev / tot


# the banked t(n), b35 (c). ### NOT RE-MEASURED; QUOTED.
T_BANKED = [(0, 11.9719), (1, 8.77574), (2, 2.20528), (3, 0.0433983), (4, 0.000125459)]
SIGMA_BANKED = 0.6165
TOL = 5e-5

# ### a synthetic state whose even share IS sigma_even by construction -- the WITNESS,
# ### and a genuinely different state from the banked one.
T_WITNESS = [(0, 0.6165), (1, 0.3835)]

# ### a perturbed state -- the FIXTURE. t(0) is moved, so the share must move off 0.6165.
T_FIXTURE = [(0, 1.0), (1, 8.77574), (2, 2.20528), (3, 0.0433983), (4, 0.000125459)]

QUOTE = 'ORTHOGONAL TO S(1,1)'
LICENCE = 'NOT LICENSED BY THE READ'


def main():
    h = Harness(ROOT, 'b219')

    # 1 -- the arithmetic read-check on banked numbers.
    h.run('sigma-even-reproduces-from-banked-t',
          check=lambda: abs(even_share(T_BANKED) - SIGMA_BANKED) < TOL,
          fixture=lambda: abs(even_share(T_FIXTURE) - SIGMA_BANKED) < TOL,
          witness=lambda: abs(even_share(T_WITNESS) - SIGMA_BANKED) < TOL)

    # 2 -- the source sentence that decides the act is IN the bank.
    #      fixture: the same string in a real owner that genuinely lacks it.
    h.run('orthogonality-quote-carried-into-bank',
          check=lambda: contains(BANK, QUOTE),
          fixture=lambda: contains(B109, QUOTE),
          witness=lambda: contains(B199, QUOTE))

    # 3 -- the licence line is present and is the deliverable.
    h.run('computation-declared-not-licensed',
          check=lambda: contains(BANK, LICENCE),
          fixture=lambda: contains(B109, LICENCE),
          witness=lambda: contains(REG, 'not licensed by the read'))

    # 4 -- ### NO INSTRUMENT WAS OPENED: no b219 file exists under tools/e16.
    #      fixture: the same test for b210, which DOES exist, so absence must fail.
    e16 = os.path.join(ROOT, 'tools', 'e16')
    h.run('no-b219-instrument-was-built',
          check=lambda: absent_in_dir(e16, 'b219'),
          fixture=lambda: absent_in_dir(e16, 'b210'),
          witness=lambda: absent_in_dir(e16, 'b999'))

    # 5 -- the registration names an index sidecar; it must exist.
    idx = os.path.join(D, 'audit_b219_index_query.txt')
    h.run('index-query-sidecar-exists',
          check=lambda: os.path.isfile(idx),
          fixture=lambda: os.path.isfile(os.path.join(D, 'audit_b219_nonexistent.txt')),
          witness=lambda: os.path.isfile(REG))

    print(h.report() if hasattr(h, 'report') else '')
    for row in h.rows:
        print('  %-38s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
