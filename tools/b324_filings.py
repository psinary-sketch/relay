# -*- coding: utf-8 -*-
"""b324_filings.py -- APPEND-ONLY CROSS-REFERENCE LINES. ### **ORIGINALS VISIBLE, DEPOSIT UNTOUCHED.**

### ### **TWO KEYSTONES ARE TOUCHED AND BOTH ARE INTERNAL.** ### `THE_RESIDUE_OF_RH.md` and
### `BALANCE_AND_POSITIVITY.md`, both under `phase1.5/`. ### **NO FILE UNDER
### ### `outputs/DEPOSITED-v1.1.2/` IS WRITTEN, AND THE TOOL REFUSES TO WRITE ONE**: the deposit
### path is checked against every target before anything is opened for writing.

### ### **THE APPEND IS THE ONLY EDIT.** ### Each keystone's pre-append bytes must be a
### ### **TRUE BYTE PREFIX** ### of its post-append bytes, checked against the working file AND the
### blob at `HEAD` -- b309's trap is that `core.autocrlf` makes those differ on a clean tree.
### ### **AND THE TOOL IS IDEMPOTENT**, because b323 learned the hard way that the closing rule
### re-runs everything after the push and a one-shot writer cannot satisfy it.

### ### ### **WHAT THE LINES SAY IS CONSTRAINED BY WHAT THE ACT FOUND.** ### The wall verdict came
### back DIFFERENT and the margin verdict UNDECIDED, so ### **NEITHER LINE MAY CLAIM A CONNECTION
### ### THE ACT REFUSED.** ### They name the fold section and the arc, record the verdict, and stop.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT_DIR = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = '<!-- b324 cross-reference -->'

TARGETS = [
    (os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'),
     'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
     [
         '',
         MARK,
         '',
         '---',
         '',
         '**Cross-reference, appended 2026-09-04 (b324). Nothing above this line is edited.**',
         '',
         'The archimedean instrument arc **b314–b322** is folded at `FINDINGS.md` § *THE '
         'ARCHIMEDEAN INSTRUMENT ARC, b314–b322 — THE FOLD*, with its own keystone at the relay '
         '(`data/b323_the_fold.txt`).',
         '',
         '**b324 read this record against that arc and found the two objects DIFFERENT.** This '
         'record\'s space is *"the positive space on the zeros"* — defined by the requirement that '
         'a self-adjoint operator\'s spectrum realize the ζ-zeros. The arc\'s constructed space is '
         'Connes–Consani\'s `S(1,1)`, defined by two homogeneous vanishing conditions on a '
         'function and its transform, **with no operator and no zeros in the definition at all**. '
         'They differ at the first constituent walked — the ambient — and at every one after it.',
         '',
         '**So the arc did not move the wall this record names, and b324 does not claim it did.** '
         'The arc built an instrument *inside* a source this record had already graded: its '
         'realization-candidate map places *"Connes–Consani (reduces RH to a Weil positivity left '
         'open)"* among the routes that stall at the realization clause. That grading stands '
         'unchanged.',
         '',
         '*Filed by b324. No grade moved; no claim of this record altered.*',
     ]),
    (os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md'),
     'phase1.5/spectral/BALANCE_AND_POSITIVITY.md',
     [
         '',
         MARK,
         '',
         '---',
         '',
         '**Cross-reference, appended 2026-09-04 (b324). Nothing above this line is edited.**',
         '',
         'The archimedean instrument arc **b314–b322** is folded at `FINDINGS.md` § *THE '
         'ARCHIMEDEAN INSTRUMENT ARC, b314–b322 — THE FOLD*.',
         '',
         'The arc computed an **archimedean margin** — `W_∞(f) − Tr(θ(g) S θ(g)*)`, equal by '
         'Connes–Consani\'s Theorem 4.7 to minus a remainder integral — positive at the three '
         'cells the source\'s Theorem 1 covers and growing toward the boundary.',
         '',
         '**b324 asked whether that margin and this record\'s `M(n) := λ_Z(n) + λ_A(n) = λ_n` are '
         'one object in two registers, and the answer is UNDECIDED.** The two are indexed '
         'differently (a test-function width against a coefficient index), decompose differently '
         '(archimedean-minus-square against zero-plus-archimedean), and **only this record\'s '
         'margin contains the zeros**. The monograph names *positivity of the Weil functional* and '
         '*λ_n ≥ 0* as two classical faces of the one obligation h2 — but it also records that the '
         'register pentagon **deliberately does not compile the cross-register equivalences**, '
         '"since to compile \'discharge one and you discharge all five\' would be to compile '
         'RH-equivalence itself."',
         '',
         '**The bridging statement is therefore owed and is filed as the arc\'s most valuable open '
         'item:** *a formula carrying the archimedean margin at a lawful test function to the Li '
         'margin at an index n, or a proof that no such formula exists.* Equivalence of the '
         'obligations is not equivalence of the margins.',
         '',
         '*Filed by b324. No grade moved; no claim of this record altered.*',
     ]),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    fails = []
    rec('=' * 100)
    rec('b324 -- THE FILINGS. ### APPEND-ONLY CROSS-REFERENCE LINES.')
    rec('=' * 100)

    # ### **THE REFUSAL, CHECKED BEFORE ANYTHING IS OPENED FOR WRITING.**
    rec('  ### THE DEPOSIT REFUSAL, CHECKED FIRST:')
    for path, rel, _ in TARGETS:
        inside = os.path.abspath(path).startswith(os.path.abspath(DEPOSIT_DIR))
        rec('    %-46s under outputs/DEPOSITED-v1.1.2/ : %s' % (rel, inside))
        if inside:
            fails.append('REFUSED -- deposited path targeted: ' + rel)
    if fails:
        rec('  ### ### **REFUSING TO WRITE. ### NO DEPOSITED TEXT IS TOUCHED, EVER.**')
        return 1
    rec('  ### ### **NO TARGET IS A DEPOSITED FILE.** ### Both are INTERNAL keystones under')
    rec('  ### `phase1.5/`, and the deposit is not opened by this tool at all.')

    for path, rel, block in TARGETS:
        rec('')
        rec('  ### ---- **%s**' % rel)
        if not os.path.exists(path):
            fails.append('missing: ' + rel)
            rec('    ### **NOT PRESENT -- HARD FAILURE**')
            continue
        before = io.open(path, encoding='utf-8', errors='replace').read()
        blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel],
                              capture_output=True).stdout.decode('utf-8', 'replace')
        rec('    working file : %d bytes, %d lines' % (len(before.encode('utf-8')),
                                                       len(before.splitlines())))
        rec('    blob at HEAD : %d bytes, %d lines' % (len(blob.encode('utf-8')),
                                                       len(blob.splitlines())))
        if MARK in before:
            rec('    ### ### **ALREADY FILED. ### NOTHING WRITTEN.** (idempotent)')
            rec('    ### The prefix check below still runs against the blob.')
            norm = before.replace('\r\n', '\n')
            nb = blob.replace('\r\n', '\n')
            rec('    the blob is still a TRUE PREFIX of the file : %s'
                % norm.startswith(nb.rstrip('\n')))
            continue
        new = before.rstrip('\n') + '\n' + '\n'.join(block) + '\n'
        open(path + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(path + '.tmp', path)
        after = io.open(path, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip('\n'))
        norm = after.replace('\r\n', '\n')
        nb = blob.replace('\r\n', '\n')
        pb = norm.startswith(nb.rstrip('\n'))
        added = len(after.splitlines()) - len(before.splitlines())
        rec('    lines appended : %+d' % added)
        rec('    the pre-append working file is a TRUE PREFIX : %s' % pw)
        rec('    the blob at HEAD is a TRUE PREFIX (normalised): %s' % pb)
        rec('    ### ### **APPEND-ONLY : %s**' % (pw and pb))
        if not (pw and pb):
            fails.append('NOT APPEND-ONLY: ' + rel)

    # ### **AND THE MECHANICAL PROOF THAT THE DEPOSIT DID NOT MOVE.**
    rec('')
    rec('  ### THE DEPOSIT, CHECKED AFTER THE WRITES:')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain',
                         'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('    git status over outputs/DEPOSITED-v1.1.2 : %r' % st)
    rec('    ### ### **THE DEPOSIT IS BYTE-UNCHANGED : %s**' % (not st))
    if st:
        fails.append('DEPOSIT MOVED')

    rec('')
    rec('=' * 100)
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    # ### ### **b323's FOURTH DEFECT, MET AGAIN AND FIXED STRUCTURALLY THIS TIME.**
    # ### b323 found that its generator rewrote its own run file on EVERY invocation, so obeying the
    # ### closing rule -- re-run the suite after the push -- replaced the record of the WRITE with
    # ### the record of a run that wrote nothing. ### **THIS TOOL HAD THE SAME SHAPE AND THE SAME
    # ### ### THING HAPPENED HERE, ONE ACT LATER.** ### The fix is not care; it is that the two
    # ### paths write to two files, so no re-run can destroy the record of the write.
    already = any('ALREADY FILED' in x for x in LINES)
    name = 'b324_filings_rerun.txt' if already else 'b324_filings_run.txt'
    io.open(os.path.join(D, name), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
