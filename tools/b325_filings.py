# -*- coding: utf-8 -*-
"""b325_filings.py -- ONE APPEND-ONLY CROSS-REFERENCE BLOCK. ### **ORIGINAL VISIBLE, DEPOSIT UNTOUCHED.**

### ### **ONE KEYSTONE IS TOUCHED AND IT IS THE INTERNAL COPY.** ### `Which_Structure_Confines.md`
### exists twice in PLACE-papers: at `day1/` (internal, 20140 bytes) and at
### `outputs/DEPOSITED-v1.1.2/` (deposited, 13125 bytes). ### **ONLY THE `day1/` COPY IS WRITTEN.**
### The deposit path is checked against the target before anything is opened for writing, and the
### deposited twin's md5 is measured BEFORE and AFTER against the value the extract step verified.

### ### **THE APPEND IS THE ONLY EDIT.** ### The keystone's pre-append bytes must be a
### ### **TRUE BYTE PREFIX** ### of its post-append bytes, checked against the working file AND the
### blob at `HEAD` (normalised -- b309's trap is that `core.autocrlf` makes those differ).
### ### **THE TOOL IS IDEMPOTENT, AND ITS TWO PATHS WRITE TWO DIFFERENTLY NAMED RUN FILES** --
### b323's fourth defect, met again at b324, is structural here: no re-run can destroy the record
### of the write.

### ### ### **WHAT THE BLOCK SAYS IS CONSTRAINED BY WHAT THE ACT FOUND.** ### The verdict was
### DOES NOT SEE IT at the arc's cells, structural in its reason and priced in its reach, so
### ### **THE BLOCK MAY NOT CLAIM THE INSTRUMENT SAW THE FAILURE, AND MAY NOT CLAIM IT CANNOT.**
### It names the arc, records the verdict at its scope, the reason, the price, and stops. ### The
### keystone's own finding is the PREMISE of the test and is not touched.
"""
import hashlib
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT_DIR = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
DEPOSITED_TWIN = os.path.join(DEPOSIT_DIR, 'Which_Structure_Confines.md')
TWIN_MD5 = '6b18d69bcf9e619d3b2fb22376ccc432'   # ### verified at the extract step, from the local deposit copy

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = '<!-- b325 cross-reference -->'

TARGETS = [
    (os.path.join(PP, 'day1', 'Which_Structure_Confines.md'),
     'day1/Which_Structure_Confines.md',
     [
         '',
         MARK,
         '',
         '---',
         '',
         '**Cross-reference, appended 2026-09-04 (b325). Nothing above this line is edited.**',
         '',
         'The archimedean instrument arc **b314–b322** (folded at `FINDINGS.md` § *THE ARCHIMEDEAN '
         'INSTRUMENT ARC, b314–b322 — THE FOLD*) was aimed at this record\'s Epstein case as a '
         '**negative control**: does an instrument that computed the Weil-positivity places sum for '
         'ζ see a hypothesis that fails? The object is this record\'s principal form `x² + xy + 6y²` '
         '(disc −23, h = 3), whose argument-principle census banks two zeros off the line.',
         '',
         '**At the arc\'s thirteen cells it does not see it.** The Epstein places sum '
         '`Σ_v W_v = PR_Q − A_Q` is negative at every cell (−16.069614947 down to −2.243190916); the '
         'forbidden positive sign appears nowhere. The reason is structural: the form represents '
         'nothing between 1 and 4 (`r_Q(2) = r_Q(3) = 0`), so the finite channel is identically zero '
         'until `a = 2` and still three orders below the archimedean channel at `a = 3`. **The reach '
         'is priced, not verdicted:** beyond the arc\'s cells the sign crosses to positive at '
         '`a ≈ 22`, but the order\'s *sees-it* verdict needs the zero side as corroboration, and the '
         'on-line Epstein zeros are not owned (the census began at σ = 0.52).',
         '',
         '**This record\'s finding is the premise of that test, not its subject.** *"The functional '
         'equation illuminates the critical line; it does not confine zeros to it"* stands unchanged; '
         'b325 used it as the known answer against which the instrument was measured. The '
         'archimedean factor `(√23/2π)^s Γ(s)` this record\'s census states is what made the '
         'arc\'s ζ-kernel non-transferable, and the Epstein kernel was built from it.',
         '',
         '*Filed by b325 (relay `data/b325_the_negative_control.txt`). No grade moved; no claim of '
         'this record altered; the deposited copy at `outputs/DEPOSITED-v1.1.2/` is not touched.*',
     ]),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def main():
    fails = []
    rec('=' * 100)
    rec('b325 -- THE FILING. ### ONE APPEND-ONLY CROSS-REFERENCE BLOCK, AT THE INTERNAL COPY.')
    rec('=' * 100)

    # ### **THE REFUSAL, CHECKED BEFORE ANYTHING IS OPENED FOR WRITING.**
    rec('  ### THE DEPOSIT REFUSAL, CHECKED FIRST:')
    for path, rel, _ in TARGETS:
        inside = os.path.abspath(path).startswith(os.path.abspath(DEPOSIT_DIR))
        rec('    %-40s under outputs/DEPOSITED-v1.1.2/ : %s' % (rel, inside))
        if inside:
            fails.append('REFUSED -- deposited path targeted: ' + rel)
    if fails:
        rec('  ### ### **REFUSING TO WRITE. ### NO DEPOSITED TEXT IS TOUCHED, EVER.**')
        return 1
    rec('  ### ### **THE TARGET IS NOT A DEPOSITED FILE.** ### It is the INTERNAL copy under `day1/`;')
    rec('  ### the deposited twin is opened READ-ONLY, for its md5, and for nothing else.')
    before_twin = md5(DEPOSITED_TWIN)
    rec('    deposited twin md5 BEFORE : %s  (verified value %s)  %s'
        % (before_twin, TWIN_MD5, 'MATCH' if before_twin == TWIN_MD5 else '### MISMATCH ###'))
    if before_twin != TWIN_MD5:
        fails.append('DEPOSITED TWIN NOT AT ITS VERIFIED md5 BEFORE THE WRITE')
        return 1

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
            rec('    the block appears exactly once             : %s' % (before.count(MARK) == 1))
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
    rec('  ### THE DEPOSIT, CHECKED AFTER THE WRITE:')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain',
                         'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('    git status over outputs/DEPOSITED-v1.1.2 : %r' % st)
    after_twin = md5(DEPOSITED_TWIN)
    rec('    deposited twin md5 AFTER  : %s  %s'
        % (after_twin, 'MATCH' if after_twin == TWIN_MD5 else '### MISMATCH ###'))
    rec('    ### ### **THE DEPOSIT IS BYTE-UNCHANGED : %s**' % (not st and after_twin == TWIN_MD5))
    if st or after_twin != TWIN_MD5:
        fails.append('DEPOSIT MOVED')

    rec('')
    rec('=' * 100)
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    # ### ### **TWO PATHS, TWO FILES -- THE FOLD'S RECURRING DEFECT, STRUCTURAL SINCE b324.**
    already = any('ALREADY FILED' in x for x in LINES)
    name = 'b325_filings_rerun.txt' if already else 'b325_filings_run.txt'
    io.open(os.path.join(D, name), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
