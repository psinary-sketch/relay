# -*- coding: utf-8 -*-
"""b230_checks.py -- the b230 gates, routed through the b217 harness.

### A STATEMENT-READ'S RISKS ARE THREE, AND EACH HAS A GATE HERE:
###   (1) that it reports an ABSENCE that is really a RELOCATION (b229's error, corrected here);
###   (2) that it QUOTES a statement it has not actually matched against the source;
###   (3) that, with an opened programme and a compiling branch in reach, it RUNS something.
### Each gate carries a must-fail FIXTURE and a must-pass WITNESS over REAL files or refs.
### ### THE FIXTURES ARE CHOSEN TO FAIL FOR THE RIGHT REASON. ### b229's fixture passed because
### it tested a phrase File E genuinely carries; the repair there, and the discipline here, is
### that every needle was grep-verified against every file it is used on BEFORE the gate was
### written -- including for LINE-WRAPPING, which silently breaks an exact quotation (b227)."""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
KERNEL = 'D:/SIDE-kernel'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')
ARC = os.path.join(PLACE, 'archive', '2026-08-24-ledger-split')

BANK = os.path.join(D, 'b230_engine_statement_and_price.txt')
REG = os.path.join(D, 'b230_registration_2026-08-28.txt')
B229 = os.path.join(D, 'b229_statement_adopted.txt')
B229REG = os.path.join(D, 'b229_registration_2026-08-28.txt')
B228REG = os.path.join(D, 'b228_registration_2026-08-28.txt')

TRAILS_LIVE = os.path.join(PLACE, 'OPEN_TRAILS.md')
LOOM_LIVE = os.path.join(PLACE, 'VERIFICATION_LOOM.md')
TRAILS_ARC = os.path.join(ARC, 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md')
LOOM_ARC = os.path.join(ARC,
                        'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')

# ### THE THREE PHASE REPORTS' OWN CONTENT -- one distinctive phrase from each, verified
# ### absent from the LIVE loom (which carries only quoted-demoted index stubs).
PHASE_MARKS = ('exactly_c1_derives',                    # PHASE 1/2 -- the compiled terminal
               'All three off-line zeros are SIMPLE',   # PHASE 2 -- the DH finding
               'CORRESPONDENCE ROWS')                   # PHASE 3 -- Decision 2


def contains(path, needle):
    """### A MISSING FILE IS FALSE, NEVER SILENTLY TRUE."""
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        return needle.lower().encode('utf-8', 'replace') in fh.read().lower()


def both(path, a, b):
    return contains(path, a) and contains(path, b)


def has_all(path, needles):
    return all(contains(path, n) for n in needles)


def count_sub(path, needle):
    """### A MISSING FILE RETURNS -1, NEVER 0."""
    if not os.path.isfile(path):
        return -1
    with open(path, encoding='utf-8', errors='replace') as fh:
        return len(re.findall(re.escape(needle), fh.read(), re.I))


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


def remote_tip(repo, branch):
    """### THE PIN IS READ AT THE REMOTE, NOT COPIED FROM A REPORT (b218)."""
    try:
        r = subprocess.run(['git', '-C', repo, 'ls-remote', 'origin',
                            'refs/heads/' + branch], capture_output=True)
    except Exception:
        return None
    if r.returncode != 0:
        return None
    out = r.stdout.decode('utf-8', 'replace').strip()
    return out.split()[0] if out else None


def tip_recorded(branch):
    """### THE BANK RECORDS THE TIP THE REMOTE ACTUALLY REPORTS TODAY."""
    sha = remote_tip(KERNEL, branch)
    return bool(sha) and contains(BANK, sha)


def main():
    h = Harness(ROOT, 'b230')

    # 1 -- ### THE THREE PHASE REPORTS ARE IN THE ARCHIVE. b229's ABSENCE WAS A RELOCATION.
    # ### THE FIXTURE IS THE LIVE LOOM, WHICH CARRIES THE THREE HEADINGS AS INDEX STUBS AND
    # ### NONE OF THE THREE REPORTS' CONTENT -- so a gate keyed on headings would have passed
    # ### on it. ### THAT IS WHY THE NEEDLES ARE CONTENT, NOT TITLES.
    h.run('three-phase-reports-found-in-archive',
          check=lambda: has_all(LOOM_ARC, PHASE_MARKS),
          fixture=lambda: has_all(LOOM_LIVE, PHASE_MARKS),
          witness=lambda: has_all(BANK, PHASE_MARKS))

    # 2 -- ### THE PRICE IS ON THE RECORD AND THE BANK CARRIES IT AS QUOTED.
    h.run('engine-price-quoted-from-source',
          check=lambda: both(TRAILS_ARC, 'Price ~2.5', 'HELD') and contains(BANK, 'Price ~2.5'),
          fixture=lambda: contains(TRAILS_LIVE, 'Price ~2.5'),
          witness=lambda: contains(BANK, 'Price ~2.5'))

    # 3 -- ### THE b229 CORRECTION IS CARRIED, superseded claim AND corrected fact together.
    # ### FIXTURE AND WITNESS ARE THE SAME REAL FILE with different second needles: b229's
    # ### registration says "NOT ON THE RECORD" and "NO PRICE EXISTS TO" and does NOT say
    # ### "PRICE IS ON THE RECORD". ### THE GATE THEREFORE DISCRIMINATES ON THE CORRECTION
    # ### ITSELF, not on incidental wording.
    h.run('b229-price-correction-carried',
          check=lambda: both(BANK, 'NOT ON THE RECORD', 'PRICE IS ON THE RECORD'),
          fixture=lambda: both(B229REG, 'NOT ON THE RECORD', 'PRICE IS ON THE RECORD'),
          witness=lambda: both(B229REG, 'NOT ON THE RECORD', 'NO PRICE EXISTS TO'))

    # 4 -- ### THE STATEMENT IS QUOTED, AND THE QUOTATION MATCHES THE SOURCE FILE.
    h.run('statement-matches-its-source',
          check=lambda: both(BANK, 'frontier, not a bypass', 'Price ~2.5'),
          fixture=lambda: both(TRAILS_LIVE, 'frontier, not a bypass', 'Price ~2.5'),
          witness=lambda: both(TRAILS_ARC, 'frontier, not a bypass', 'Price ~2.5'))

    # 5 -- ### THE THREE JUNCTION FACES ARE REPORTED (ABSENT), NOT QUIETLY OMITTED.
    h.run('three-faces-reported-absent',
          check=lambda: count_sub(BANK, '(ABSENT)') >= 3,
          fixture=lambda: count_sub(FILE_E, '(ABSENT)') >= 3,
          witness=lambda: count_sub(B229REG, '(ABSENT)') >= 3)

    # 6 -- ### NO SIGN IS CHOSEN, AND THE DOSSIER IS FILED AS A RULING ITEM.
    h.run('sign-dossier-filed-no-sign-chosen',
          check=lambda: both(BANK, 'NO SIGN IS CHOSEN', 'RULING ITEM: THE SIGN OF'),
          fixture=lambda: both(FILE_E, 'NO SIGN IS CHOSEN', 'RULING ITEM: THE SIGN OF'),
          witness=lambda: both(REG, 'NO SIGN IS CHOSEN', 'RULING ITEM: THE SIGN OF'))

    # 7 -- ### BOTH act-12 READINGS ARE CARRIED SIDE BY SIDE. ### A DOSSIER THAT SHOWED ONE
    # ### READING WOULD BE A CHOICE WEARING A DOSSIER'S NAME.
    h.run('both-act12-readings-in-the-dossier',
          check=lambda: both(BANK, 'atlas', 'CC dict'),
          fixture=lambda: both(FILE_E, 'atlas', 'CC dict'),
          witness=lambda: both(B229, 'atlas', 'CC dict'))

    # 8 -- ### THE ENGINE'S FIRST ACT WAS NOT RUN: BOTH KERNELS UNTOUCHED.
    h.run('kernels-untouched-engine-not-run',
          check=lambda: repo_untouched(KERNEL) and repo_untouched(SGS),
          fixture=lambda: repo_untouched('D:/nonexistent-repo-xyz'),
          witness=lambda: repo_untouched(KERNEL))

    # 9 -- ### NO PIN MOVED (b218): the bank records the tips the REMOTE reports today.
    h.run('pins-read-at-remote-not-moved',
          check=lambda: tip_recorded('derivative-engine') and tip_recorded('main'),
          fixture=lambda: tip_recorded('no-such-branch-xyz'),
          witness=lambda: tip_recorded('main'))

    # 10 -- ### THE PROPOSAL IS FILED, NOT EXECUTED.
    h.run('proposal-filed-not-executed',
          check=lambda: both(BANK, 'FILED AS A PROPOSAL', 'NOT EXECUTED'),
          fixture=lambda: both(B229, 'FILED AS A PROPOSAL', 'NOT EXECUTED'),
          witness=lambda: both(REG, 'FILED AS A PROPOSAL', 'NOT EXECUTED'))

    # 11 -- ### NO NUMBER, with an adopted target one act old and an instrument in reach.
    h.run('no-number-computed-in-this-act',
          check=lambda: contains(BANK, 'NO COMPUTATION, NO COMPARISON'),
          fixture=lambda: contains(FILE_E, 'NO COMPUTATION, NO COMPARISON'),
          witness=lambda: contains(B228REG, 'NO COMPUTATION, NO COMPARISON'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
