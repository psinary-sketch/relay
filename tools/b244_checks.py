# -*- coding: utf-8 -*-
"""b244_checks.py -- the b244 gates, routed through the amended b217 harness.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that an amendment moved code while claiming to move only docstrings.
###       ### Gate 2 strips every comment and docstring from File E and from its HEAD blob
###       ### and compares what remains -- and gate 3 is its must-fail twin on a file whose
###       ### code DID move, so the test is shown able to say no.
###   (2) that the loom was edited rather than appended to. ### Gate 5 requires ONE hunk,
###       ### ZERO deletions, and the pre-image preserved byte-for-byte as a prefix.
###   (3) that the profile was inferred from an exit code instead of read.
###       ### Gate 4 requires the printed line in the act's own artefacts.
###   (4) that a grade was promoted in transit. ### Gate 8: the filings must carry b242's
###       ### HELD and b243's bench-grade rider, in the words their own acts used.
###   (5) that the shrink was executed without disclosure. ### Gate 6 requires the direction
###       ### AND the no-orientation-closes-it exhibit in the amended file itself.
###   (6) that this act computed something. ### Gate 7: no left/right channel call appears in
###       ### any tool of this act, matched as identifiers over code.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')

REG = os.path.join(D, 'b244_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b244_serializing_close.txt')
B241 = os.path.join(D, 'b241_residual_ledger.txt')
B242 = os.path.join(D, 'b242_left_mode_axis.txt')
B243 = os.path.join(D, 'b243_imp1_envelope.txt')
FILE_E = os.path.join(SGS, 'Interfaces', 'FiniteInstanceIdentity.lean')
CORR = os.path.join(SGS, 'CORRESPONDENCE.md')
LOOM = os.path.join(PLACE, 'VERIFICATION_LOOM.md')
HANDOFF = os.path.join(ROOT, 'HANDOFF.md')

TOOLS = [os.path.join(ROOT, 'tools', f) for f in
         ('b244_loom_append.py', 'b244_handoff.py')]
CHANNEL_TOKENS = ('trace_modes', 'e2_of_grid', 'theta_quotient', 'left_side', 'eps_masked')


def _strip(src):
    """### THE LEAN COMMENT/DOCSTRING STRIPPER, CARRIED FROM b239 UNCHANGED so that the test
    ### this act passes is the SAME test b239's amendment passed, not a friendlier one."""
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
    keep = []
    for line in ''.join(out).splitlines():
        j = line.find('--')
        if j >= 0:
            line = line[:j]
        if line.strip():
            keep.append(' '.join(line.split()))
    return chr(10).join(keep)


def code_identical(repo, relpath, rev):
    r = subprocess.run(['git', '-C', repo, 'show', rev + ':' + relpath], capture_output=True)
    if r.returncode != 0:
        return None
    head = r.stdout.decode('utf-8', 'replace')
    work = io.open(os.path.join(repo, relpath), encoding='utf-8', errors='replace').read()
    return _strip(head) == _strip(work)


def loom_pure_append():
    """### ONE HUNK, ZERO DELETIONS, AND THE PRE-IMAGE STILL A PREFIX. ### THREE LIMBS,
    ### because b240 rewrote seven earlier lines with a repair that looked like a fix."""
    r = subprocess.run(['git', '-C', PLACE, 'diff', 'HEAD~1', '--numstat', '--',
                        'VERIFICATION_LOOM.md'], capture_output=True)
    line = r.stdout.decode('utf-8', 'replace').strip()
    if not line:
        return False
    add, dele = line.split()[0], line.split()[1]
    h = subprocess.run(['git', '-C', PLACE, 'diff', 'HEAD~1', '--', 'VERIFICATION_LOOM.md'],
                       capture_output=True).stdout.decode('utf-8', 'replace')
    hunks = h.count('\n@@')
    pre = subprocess.run(['git', '-C', PLACE, 'show', 'HEAD~1:VERIFICATION_LOOM.md'],
                         capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(LOOM, encoding='utf-8').read()
    return bool(dele == '0' and hunks == 1 and now.startswith(pre.rstrip()))


def code_only(path):
    import ast
    src = io.open(path, encoding='utf-8').read()
    doc = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) \
                    and isinstance(node.body[0].value, ast.Constant) \
                    and isinstance(node.body[0].value.value, str):
                s0 = node.body[0]
                for ln in range(s0.lineno, (s0.end_lineno or s0.lineno) + 1):
                    doc.add(ln)
    return '\n'.join(l.split('#', 1)[0] for i, l in enumerate(src.split('\n'), 1) if i not in doc)


def no_channel_called():
    for p in TOOLS:
        s = code_only(p)
        for t in CHANNEL_TOKENS:
            if re.search(r'\b%s\b' % re.escape(t), s):
                return False
    return True


def rows_have_six_cells():
    tail = io.open(CORR, encoding='utf-8').read().rstrip().split('\n')[-3:]
    for line in tail:
        cells = [c for c in line.strip().strip('|').split('|')]
        if len(cells) != 6 or any(not c.strip() for c in cells):
            return False
    return all(line.strip().startswith('| 9') for line in tail)


def main():
    h = Harness(ROOT, 'b244')

    h.run('registration-precedes-every-amendment',
          check=lambda: all(os.path.getmtime(REG) < os.path.getmtime(p)
                            for p in (FILE_E, CORR, LOOM, BANK)),
          fixture=lambda: os.path.getmtime(FILE_E) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 6000)

    # 2 -- ### THE CENTRAL CLAIM: A DOCSTRING EDIT MOVED NO CODE.
    h.run('file-E-code-identical-to-pre-amendment',
          check=lambda: code_identical(SGS, 'Interfaces/FiniteInstanceIdentity.lean',
                                       'HEAD~1') is True,
          # ### THE FIXTURE, REPLACED AFTER THE FIRST RUN AND THE REPLACEMENT IS THE POINT:
          # ### the original read `code_identical(...) is not True` -- ### THE EXACT NEGATION OF
          # ### ITS OWN CHECK. ### It failed whenever the check passed, so it demonstrated
          # ### NOTHING about whether the comparison can discriminate. ### **A FIXTURE THAT IS
          # ### THE NEGATION OF ITS CHECK IS NOT A MUST-FAIL FIXTURE; IT IS THE CHECK WEARING A
          # ### MINUS SIGN**, and the harness cannot tell the difference (its own header says so:
          # ### "IT CANNOT TELL A GOOD FIXTURE FROM A BAD ONE").
          # ### THIS ONE COMPARES File E's CODE TO A DIFFERENT LEAN FILE'S -- two real files whose
          # ### stripped code genuinely differs -- so the predicate is shown able to say NO.
          fixture=lambda: _strip(io.open(FILE_E, encoding='utf-8').read())
                          == _strip(io.open(os.path.join(SGS, 'Interfaces', 'GlobalSection.lean'),
                                            encoding='utf-8').read()),
          witness=lambda: contains(BANK, 'IDENTICAL: True'))

    # 3 -- ### AND THE STRIPPER ITSELF MUST BE SHOWN ABLE TO SEE A DIFFERENCE.
    h.run('stripper-detects-a-real-code-difference',
          check=lambda: _strip('def f := 1\n/- c -/\n') != _strip('def f := 2\n/- c -/\n'),
          fixture=lambda: _strip('def f := 1\n/- a -/\n') != _strip('def f := 1\n/- b -/\n'),
          witness=lambda: _strip('/- x -/\ndef f := 1\n') == 'def f := 1')

    h.run('profile-re-printed-not-inferred',
          check=lambda: (contains(BANK, 'depends on axioms:')
                         and contains(BANK, 'IT RAN THE PRINT')
                         and contains(CORR, 'RE-PRINTED THIS ACT')),
          fixture=lambda: contains(B241, 'RE-PRINTED THIS ACT'),
          witness=lambda: contains(BANK, 'lake env lean'))

    h.run('loom-pure-append-one-hunk-zero-deletions',
          check=loom_pure_append,
          # ### THE FIXTURE: the same three-limb test applied to a file this act REPLACED
          # ### content in -- HANDOFF's lead line -- where deletions are NOT zero.
          fixture=lambda: subprocess.run(
              ['git', '-C', ROOT, 'diff', '--numstat', '--', 'HANDOFF.md'],
              capture_output=True).stdout.decode('utf-8', 'replace').split()[1] == '0',
          witness=lambda: os.path.exists(LOOM))

    # 6 -- ### THE SHRINK IS DISCLOSED IN THE AMENDED FILE ITSELF, NOT ONLY IN THE REPORT.
    h.run('shrink-disclosed-in-file-E-and-the-rows',
          check=lambda: (contains(FILE_E, 'O1 SHRINKS THE RESIDUAL')
                         and contains(FILE_E, 'A RULING')
                         and contains(CORR, 'no orientation closes the separation')
                         and contains(BANK, 'THE RESIDUAL MOVEMENT IS NOT COMPUTED IN THIS ACT')),
          fixture=lambda: contains(B241, 'O1 SHRINKS THE RESIDUAL')
                          and contains(B241, 'RE-PRINTED THIS ACT'),
          witness=lambda: contains(FILE_E, 'SHRINKS THE RESIDUAL'))

    h.run('this-act-called-no-channel',
          check=no_channel_called,
          fixture=lambda: not any(
              re.search(r'\b%s\b' % t,
                        code_only(os.path.join(ROOT, 'tools', 'e16', 'b242_mode_axis.py')))
              for t in CHANNEL_TOKENS),
          witness=lambda: os.path.exists(TOOLS[0]))

    # 8 -- ### NO GRADE PROMOTED IN TRANSIT: the filings carry their own acts' riders.
    h.run('grades-transcribed-with-their-riders',
          check=lambda: (contains(BANK, 'VERIFIED-AT-BENCH IS A BENCH GRADE')
                         and contains(BANK, '`bar_L` MAY BE 2.4x-2.9x')
                         and contains(BANK, 'M-4 IS')
                         and contains(BANK, 'NOT PAID AT BENCH')
                         and contains(B242, 'M-4 IS **NOT** PAID AT BENCH')
                         and contains(B243, 'IT IS NOT A PROOF OF CC')),
          fixture=lambda: contains(B241, '`bar_L` MAY BE 2.4x-2.9x'),
          witness=lambda: contains(BANK, 'bar_L'))

    h.run('three-rows-six-cells-no-blanks',
          check=rows_have_six_cells,
          fixture=lambda: len([c for c in '| a | b |'.strip().strip('|').split('|')]) == 6,
          witness=lambda: os.path.exists(CORR))

    h.run('nine-filings-listed-and-reconciled',
          check=lambda: (contains(REG, 'W-ORD-STAGING-GUARD')
                         and contains(BANK, 'NINE FILED, NINE LISTED AT REGISTRATION')
                         and all(contains(BANK, w) for w in
                                 ('W-ORD-ORDINATE-CACHE', 'W-ORD-MODE-PRECISION',
                                  'W-ORD-STAGING-GUARD'))),
          fixture=lambda: contains(B242, 'NINE FILED, NINE LISTED AT REGISTRATION'),
          witness=lambda: contains(BANK, 'W-ORD-MODE-PRECISION'))

    h.run('b245-named-with-preconditions',
          check=lambda: (contains(BANK, 'THE ACT IS **b245**')
                         and contains(BANK, 'TWO GREEN, TWO AMBER, ONE OPEN-BY-DESIGN')
                         and contains(HANDOFF, 'NEXT IS b245, THE SECOND FACE-OFF')),
          fixture=lambda: contains(B243, 'THE ACT IS **b245**'),
          witness=lambda: contains(BANK, 'b245'))

    h.run('stale-working-copy-restated-not-widened-quietly',
          check=lambda: (contains(BANK, 'IT IS NOW STALE BY THREE')
                         and contains(BANK, 'never by drift')),
          fixture=lambda: contains(B241, 'IT IS NOW STALE BY THREE'),
          witness=lambda: contains(BANK, 'W-ORD-FILE-E-WORKING-COPY-STALE'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (REG, BANK)),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'DECIDES NOTHING GLOBAL'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
