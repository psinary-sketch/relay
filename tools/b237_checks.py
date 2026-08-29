# -*- coding: utf-8 -*-
"""b237_checks.py -- the b237 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS:
###   (1) that the NAMING INVERSION is carried silently -- the narrative's `LEFT` is the
###       ### LEDGER, and tabulating it as a left-side asset would commit the standing
###       ### clause's crime by a naming slip rather than by intent.
###   (2) that an INEQUALITY link is tabulated as a realization -- reading `<=` as `=`.
###   (3) that an asset is identified with a File E type BY RESEMBLANCE (b219's species).
###   (4) that an asset is graded by how well it AGREES with the right side (b229's clause).
###   (5) that the T.value dossier smuggles in a recommendation.
### ### NEEDLES WERE CHECKED AGAINST THE BANK BEFORE THE GATES WERE WRITTEN -- b236's two
### ### failures were both a needle written from memory rather than from the file.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

BANK = os.path.join(D, 'b237_left_side_assets.txt')
REG = os.path.join(D, 'b237_registration_2026-08-28.txt')
B227 = os.path.join(D, 'b227_the_trace.txt')
B10 = os.path.join(D, 'b10_2026-08-17.txt')
B236 = os.path.join(D, 'b236_comprehension_read.txt')
B233 = os.path.join(D, 'b233_the_arrangement.txt')

NARR = os.path.join(ROOT, 'reports',
                    '2026-08-18-global-section-acts-narrative-v0.15.md')
B38 = os.path.join(E16, 'b38_act10.py')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')


def unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def no_new_instrument():
    """### CORPUS-FIRST: NOTHING NEW WAS BUILT. ### The act may add its own CHECKS file and
    ### nothing else under tools/e16 -- no new instrument, no new operator."""
    return not any(f.startswith('b237') for f in os.listdir(E16))


def main():
    h = Harness(ROOT, 'b237')

    # 1 -- ### THE NAMING INVERSION IS REPORTED, NOT CARRIED SILENTLY.
    h.run('naming-inversion-reported',
          check=lambda: both(BANK, 'THE NARRATIVE\'S "LEFT" IS FILE E\'s "RIGHT"',
                             'DOUBLE-NAME'),
          fixture=lambda: both(B236, 'THE NARRATIVE\'S "LEFT" IS FILE E\'s "RIGHT"',
                               'DOUBLE-NAME'),
          witness=lambda: contains(REG, 'THE NARRATIVE\'S "LEFT" IS FILE E\'s "RIGHT"'))

    # 2 -- ### THE LINKS ARE INEQUALITIES, AND THE ACT SAYS SO IN TERMS.
    h.run('links-are-inequalities-not-realizations',
          check=lambda: both(BANK, 'READING `≤` AS `=`', 'A BOUND ON the object'),
          fixture=lambda: both(B236, 'READING `≤` AS `=`', 'A BOUND ON the object'),
          witness=lambda: contains(REG, 'READING `≤` AS `=`'))

    # 3 -- ### THE COUNTS ARE STATED, AND THE HEADLINE COUNT IS **ZERO**.
    # ### AN ASSET TABLE THAT FOUND A REALIZATION WOULD BE THE ACT'S BIGGEST CLAIM; IT FOUND NONE.
    h.run('asset-counts-zero-realizes',
          check=lambda: both(BANK, 'REALIZES: 0', 'PARTIALLY REALIZES: 4'),
          fixture=lambda: both(B233, 'REALIZES: 0', 'PARTIALLY REALIZES: 4'),
          witness=lambda: contains(BANK, 'PARTIALLY REALIZES: 4'))

    # 4 -- ### BOTH SPECIES SAID AT EVERY USE (b221's divergence, b219's double-name).
    h.run('cell-and-space-species-said',
          check=lambda: all(contains(BANK, s) for s in
                            ('DIAGONAL a', 'LOCAL (p,n)', 'V_inv', 'S̄_v')),
          fixture=lambda: all(contains(B38, s) for s in
                              ('DIAGONAL a', 'LOCAL (p,n)', 'V_inv', 'S̄_v')),
          witness=lambda: contains(BANK, 'LOCAL (p,n)'))

    # 5 -- ### THE NARROWING IS REPORTED WITH **BOTH** HALVES: what confirmed, what refuted.
    # ### A REGISTERED EXPECTATION THAT CAME OUT HALF-RIGHT MUST SHOW BOTH HALVES.
    h.run('narrowing-reports-both-halves',
          check=lambda: both(BANK, 'CONFIRMED:', 'REFUTED:'),
          fixture=lambda: both(B236, 'CONFIRMED:', 'REFUTED:'),
          witness=lambda: contains(BANK, 'REFUTED:'))

    # 6 -- ### THE JUNCTION IS QUOTED FROM ITS OWNERS, and the quotes are real AT SOURCE.
    h.run('junction-quoted-from-its-owners',
          check=lambda: (contains(BANK, 'THE FOURIER HALF DOES NOT DESCEND')
                         and contains(B10, 'THE FOURIER HALF DOES NOT DESCEND')
                         and contains(BANK, 'THE FIRST IS NOT IN THE RECORD')
                         and contains(B227, 'THE FIRST IS NOT IN THE RECORD')),
          fixture=lambda: contains(B236, 'THE FOURIER HALF DOES NOT DESCEND'),
          witness=lambda: contains(B10, 'THE FOURIER HALF DOES NOT DESCEND'))

    # 7 -- ### §18's JOINT 1 IS QUOTED AT ITS SOURCE -- the sentence that refuted the wider
    # ### narrowing. ### WITHOUT IT THE 'REFUTED' HALF WOULD REST ON MY WORD.
    h.run('section18-joint-quoted-at-source',
          check=lambda: (contains(BANK, 'the restricted-product trace is DEFINED BY EXACTLY')
                         and contains(NARR, 'the restricted-product trace is defined by exactly')),
          fixture=lambda: contains(B233, 'the restricted-product trace is DEFINED BY EXACTLY'),
          witness=lambda: contains(NARR, 'the restricted-product trace is defined by exactly'))

    # 8 -- ### THE MISSING STEPS ARE A SPECIES-TAGGED LIST, not a frontier.
    h.run('missing-steps-species-tagged',
          check=lambda: all(contains(BANK, s) for s in
                            ('M-1 [RULING]', 'M-3 [RESULT]', 'M-5 [CONSTRUCTION]')),
          fixture=lambda: all(contains(B236, s) for s in
                              ('M-1 [RULING]', 'M-3 [RESULT]', 'M-5 [CONSTRUCTION]')),
          witness=lambda: contains(BANK, 'M-5 [CONSTRUCTION]'))

    # 9 -- ### THE T.VALUE DOSSIER NAMES FOUR CANDIDATES AND **CHOOSES NONE**.
    h.run('tvalue-dossier-chooses-none',
          check=lambda: (all(contains(BANK, c) for c in ('(C1)', '(C2)', '(C3)', '(C4)'))
                         and contains(BANK, 'CHOOSES NONE')),
          fixture=lambda: contains(B236, 'CHOOSES NONE'),
          witness=lambda: contains(BANK, 'CHOOSES NONE'))

    # 10 -- ### NO ASSET GRADED BY AGREEMENT WITH THE RIGHT SIDE (b229's standing clause).
    h.run('no-asset-graded-by-agreement',
          # ### FAILED ON THE FIRST RUN: `never from a residual` is the REGISTRATION's
          # ### sentence, not the bank's -- the needle was right about the act and wrong about
          # ### which file carries it. ### THE GATE WAS WRONG, NOT THE RECORD. Each half is now
          # ### tested against the file that actually carries it.
          check=lambda: (contains(BANK, 'NO ASSET IS GRADED BY AGREEMENT')
                         and contains(REG, 'never from a residual')),
          fixture=lambda: contains(B236, 'NO ASSET IS GRADED BY AGREEMENT'),
          witness=lambda: contains(REG, 'never from a residual'))

    # 11 -- ### CORPUS-FIRST: NOTHING NEW WAS BUILT. ### No new instrument under tools/e16,
    # ### and the kernel is untouched.
    h.run('nothing-new-built-kernel-untouched',
          check=lambda: no_new_instrument() and unmodified(SGS, 'Interfaces') ,
          fixture=lambda: not no_new_instrument(),
          witness=lambda: unmodified(SGS, 'Interfaces'))

    # 12 -- ### THE INTERFACES RE-PRINT IS DISCLOSED A THIRD TIME rather than accumulating
    # ### into a claim by silence.
    h.run('interfaces-reprint-disclosed-again',
          check=lambda: both(BANK, 'STILL RIDING THE NEXT KERNEL-TOUCHING ACT',
                             'a third time'),
          fixture=lambda: both(B233, 'STILL RIDING THE NEXT KERNEL-TOUCHING ACT',
                               'a third time'),
          witness=lambda: contains(REG, 'STILL RIDING THE NEXT KERNEL-TOUCHING ACT'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
