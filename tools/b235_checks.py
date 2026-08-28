# -*- coding: utf-8 -*-
"""b235_checks.py -- the b235 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THEY ARE THE SHARPEST YET BECAUSE THE ACT EDITS A STATED OBJECT:
###   (1) that a DEPOSITED artifact gets touched. ### The deposit is frozen, errata-only.
###   (2) that the working file gets quoted AS deposit-voice. ### The tree's `DEPOSITED`
###       snapshot is v5.4, not the deposit -- the exact trap the registration named.
###   (3) that a NUMBER decides the sign. ### b229's standing clause; the ruling itself says
###       "no number consulted".
###   (4) that File E's RELATION moves under cover of a docstring edit.
### ### EVERY ABSENCE CARRIES A POSITIVE CONTROL, per the EXECUTION line.
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
METHOD = os.path.join(PLACE, 'phase2', 'method')
D = os.path.join(ROOT, 'data')

BANK = os.path.join(D, 'b235_phase11_conventions.txt')
REG = os.path.join(D, 'b235_registration_2026-08-28.txt')
B232 = os.path.join(D, 'b232_sign_of_A.txt')
B233 = os.path.join(D, 'b233_the_arrangement.txt')

ATLAS = os.path.join(METHOD, 'SIGN_ARRANGEMENT_RECONCILIATION.md')
CHAIN = os.path.join(METHOD, 'THE_IDENTITY_CHAIN.md')
REGISTRY = os.path.join(PLACE, 'REGISTRY.md')
MONO = os.path.join(PLACE, 'day1', 'A_Place_to_Stand.md')
SNAP = os.path.join(PLACE, 'outputs', 'DEPOSITED', 'A_Place_to_Stand.DEPOSITED.md')
BALANCE = os.path.join(PLACE, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')


def unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def _strip_lean_comments(src):
    """### REMOVE `/- ... -/` BLOCKS AND `--` LINE COMMENTS, THEN NORMALIZE WHITESPACE."""
    out, i, depth = [], 0, 0
    while i < len(src):
        if src.startswith('/-', i):
            depth += 1
            i += 2
        elif src.startswith('-/', i) and depth:
            depth -= 1
            i += 2
        elif depth:
            i += 1
        else:
            out.append(src[i])
            i += 1
    txt = ''.join(out)
    keep = []
    for line in txt.splitlines():
        j = line.find('--')
        if j >= 0:
            line = line[:j]
        if line.strip():
            keep.append(' '.join(line.split()))
    return chr(10).join(keep)


def code_identical(repo, relpath):
    """### THE EXACT TEST, NOT A HEURISTIC: strip every comment and docstring from the
    ### HEAD blob and from the working file, and compare what is left.
    ### ### THE FIRST DRAFT COUNTED 'lines that look like code' AND FAILED ON DOCSTRING
    ### ### CONTINUATION LINES -- a heuristic where an exact comparison was available.
    ### ### THE GATE FAILED AND SAID SO, which is the harness doing its job."""
    try:
        r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + relpath],
                           capture_output=True)
    except Exception:
        return False
    if r.returncode != 0:
        return False
    head = r.stdout.decode('utf-8', 'replace')
    work = io.open(os.path.join(repo, relpath), encoding='utf-8', errors='replace').read()
    return _strip_lean_comments(head) == _strip_lean_comments(work)


def has_mnt():
    return os.path.isdir('/mnt')


def host_roots_resolve():
    """### THE POSITIVE CONTROL ON THE /mnt ABSENCE: the check can see real roots."""
    return os.path.isdir('D:/') and os.path.isdir('C:/')


def main():
    h = Harness(ROOT, 'b235')

    # 1 -- ### THE GATE-1 PIN MATCHES REGISTRY ON EVERY FIELD.
    h.run('fetch-pin-matches-registry',
          check=lambda: (all(contains(BANK, s) for s in
                             ('v1.1.2', '2026-07-24', '10.5281/zenodo.21539167', '19675355'))
                         and contains(REGISTRY, 'Zenodo v1.1.2')),
          fixture=lambda: contains(B233, '10.5281/zenodo.21539167'),
          witness=lambda: contains(REGISTRY, '10.5281/zenodo.21539167'))

    # 2 -- ### NO DEPOSITED ARTIFACT WAS TOUCHED. ### The frozen voice stays frozen.
    h.run('deposited-artifacts-untouched',
          check=lambda: all(unmodified(PLACE, p) for p in
                            ('day1', 'outputs/DEPOSITED', 'ERRATA.md')),
          fixture=lambda: unmodified(PLACE, 'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md'),
          witness=lambda: unmodified(PLACE, 'ERRATA.md'))

    # 3 -- ### THE ATLAS COMPLETES THE EXISTING DOCUMENT; NO NEW DOCUMENT WAS CREATED.
    h.run('atlas-completes-existing-document',
          check=lambda: (contains(ATLAS, 'THE SIGN ATLAS')
                         and contains(ATLAS, 'THE TWO ARRANGEMENTS, WRITTEN SIDE BY SIDE')),
          fixture=lambda: contains(CHAIN, 'THE TWO ARRANGEMENTS, WRITTEN SIDE BY SIDE'),
          witness=lambda: contains(ATLAS, 'THE SIGN ATLAS'))

    # 4 -- ### THE DECIDING SENTENCE IS A REAL SUPPORT-VOICE QUOTATION, FOUND AT ITS SOURCE.
    # ### IF THIS IS NOT IN THE MONOGRAPH, THE EXECUTION RESTED ON NOTHING.
    h.run('deciding-sentence-found-at-source',
          check=lambda: (contains(MONO, 'the sign of `W_∞ − W_2`')
                         and contains(ATLAS, 'the sign of `W_∞ − W_2`')
                         and contains(CHAIN, 'the sign of `W_∞ − W_2`')),
          fixture=lambda: contains(SNAP, 'the sign of `W_∞ − W_2`'),
          witness=lambda: contains(MONO, 'the sign of `W_∞ − W_2`'))

    # 5 -- ### THE `DEPOSITED` SNAPSHOT IS **NOT** THE DEPOSIT, AND THE ACT SAYS SO.
    h.run('deposited-snapshot-finding-recorded',
          check=lambda: (contains(SNAP, 'v5.4') and not contains(SNAP, 'v5.10.2')
                         and contains(BANK, 'IS NOT THE DEPOSIT')),
          fixture=lambda: contains(MONO, 'IS NOT THE DEPOSIT'),
          witness=lambda: contains(SNAP, 'v5.4'))

    # 6 -- ### THE FINDING IS **NOT** FILED TO ERRATA, and the act states the reason.
    h.run('finding-not-misfiled-to-errata',
          check=lambda: (unmodified(PLACE, 'ERRATA.md')
                         and contains(BANK, 'NOT filed to ERRATA')),
          fixture=lambda: contains(B232, 'NOT filed to ERRATA'),
          witness=lambda: unmodified(PLACE, 'ERRATA.md'))

    # 7 -- ### FILE E: BOTH ORIGINALS VISIBLE, AND THE RELATION UNMOVED.
    h.run('file-E-originals-visible-relation-unmoved',
          check=lambda: (contains(FILE_E, 'THE ORIGINAL READ')
                         and contains(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes')
                         and code_identical(SGS, 'Interfaces/FiniteInstanceIdentity.lean')),
          fixture=lambda: contains(B233, 'THE ORIGINAL READ'),
          witness=lambda: contains(FILE_E, 'T.value + Q.value = W.wInf - W.wPrimes'))

    # 8 -- ### THE RE-SIGN IS IN THE CHAIN WITH ITS ORIGINALS TABLE.
    h.run('chain-resign-with-originals',
          check=lambda: both(CHAIN, 'wInf(a) := +A(a)', 'as filed (b232'),
          fixture=lambda: both(ATLAS, 'wInf(a) := +A(a)', 'as filed (b232'),
          witness=lambda: contains(CHAIN, 'wInf(a) := +A(a)'))

    # 9 -- ### NO NUMBER CONSULTED, and the excluded sources are NAMED, not merely denied.
    h.run('no-number-consulted-sources-named',
          check=lambda: all(contains(BANK, s) for s in
                            ('NO NUMBER WAS CONSULTED', 'ten-digit closure',
                             'residual collapse')),
          # ### THE FIRST FIXTURE WAS b233's BANK AND THE HARNESS REFUSED THE CHECK:
          # ### b233 genuinely says 'no number was consulted', so it could not
          # ### discriminate. ### b217's FIRST GUARD. Repaired to a file that lacks it.
          fixture=lambda: contains(REGISTRY, 'NO NUMBER WAS CONSULTED'),
          witness=lambda: contains(CHAIN, 'no number was consulted'))

    # 10 -- ### THE HAZARD REPAIR IS ADDITIVE: the ORIGINAL SENTENCE SURVIVES BESIDE IT.
    h.run('hazard-repair-additive-original-survives',
          check=lambda: both(BALANCE, 'the positive archimedean term dominates',
                             'pole-plus-archimedean'),
          fixture=lambda: both(ATLAS, 'the positive archimedean term dominates',
                               'ERA ANNOTATION (2026-08-28'),
          witness=lambda: contains(BALANCE, 'the positive archimedean term dominates'))

    # 11 -- ### THE /mnt ABSENCE CARRIES ITS POSITIVE CONTROL IN THE SAME GATE.
    h.run('mnt-absent-with-positive-control',
          check=lambda: (not has_mnt()) and host_roots_resolve() and contains(BANK, 'NO `/mnt`'),
          fixture=lambda: has_mnt(),
          witness=lambda: host_roots_resolve())

    # 12 -- ### EVERY OUTPUT NAMES ITS VOICE, per the standing ruling.
    h.run('voices-named-in-outputs',
          check=lambda: all(contains(BANK, v) for v in
                            ('DEPOSIT-VOICE', 'SUPPORT-VOICE', 'PROGRAM-VOICE')),
          fixture=lambda: all(contains(B233, v) for v in
                              ('DEPOSIT-VOICE', 'SUPPORT-VOICE', 'PROGRAM-VOICE')),
          witness=lambda: all(contains(ATLAS, v) for v in
                              ('DEPOSIT-VOICE', 'SUPPORT-VOICE', 'PROGRAM-VOICE')))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
