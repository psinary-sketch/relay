# -*- coding: utf-8 -*-
"""b623_test_count.py -- THE TEST OF THE RECORD TOOL'S CASE COUNTER, (R233)(3), b623. ### THE STANDING REPAIR'S TEST.

### The record tool counts a test's cases by the test's own case pattern and never by its summary lines. Each case below plants a
### summary line ("### ALL PASS", a "N of N checks" line, a "### CASES :" line) beside the case lines and expects the count unchanged.
### The same cases are run against the SEALED form of `count_cases` (relay tools/b623_record.py as committed at the seal, read from git),
### which counts every line ending in PASS or FAIL: the sealed form must fail at least one case -- the positive control -- and the
### repaired form must pass every case. Nothing is written; the record tool's `count_test` banks the output.
"""
import os
import re
import subprocess
import sys
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = chr(10)
SEALED_SUBJECT = 'b623 (R233)(3): the record tool as sealed'


def sealed_module():
    """### tools/b623_record.py at the relay commit whose subject opens with SEALED_SUBJECT, executed as a module of its own."""
    log = subprocess.run(['git', '-C', ROOT, 'log', '--format=%H %s', '--', 'tools/b623_record.py'], capture_output=True, text=True).stdout
    h = [l.split(' ', 1)[0] for l in log.split(NL) if l.strip() and l.split(' ', 1)[1].startswith(SEALED_SUBJECT)]
    if len(h) != 1:
        return None, h
    src = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/b623_record.py' % h[0]], capture_output=True).stdout.decode('utf-8')
    m = types.ModuleType('b623_record_sealed')
    m.__file__ = os.path.join(ROOT, 'tools', 'b623_record_sealed.py')
    exec(compile(src, m.__file__, 'exec'), m.__dict__)
    return m, h


PUSH_TEXT = NL.join(['### CASE A -- x', '  A exit : wanted 0 ; got 0 ; PASS', '  A tag made : wanted yes ; got yes ; PASS',
                     '### CASE B -- y', '  B exit : wanted 4 ; got 3 ; ### FAIL', '### ### **2 of 3 checks as wanted -- FAIL**'])
PY_TEXT = NL.join(['  (1) the first : PASS', '  (2) the second : PASS', '', '### CASES : 2 ; PASSING : 2 ; FAILING : 0'])
PLANT = '### ALL PASS'


def cases(count, R):
    """### (label, got, wanted) for one counter."""
    return [
        ('a push_gated test, three check lines and its own summary line', count(PUSH_TEXT, R.PUSH_CASE), (3, 2)),
        ('the same with "### ALL PASS" planted: the count unchanged', count(PUSH_TEXT + NL + PLANT, R.PUSH_CASE), (3, 2)),
        ('a numbered test, two case lines and its CASES line', count(PY_TEXT, R.COUNT_CASE), (2, 2)),
        ('the same with "### ALL PASS" planted: the count unchanged', count(PY_TEXT + NL + PLANT, R.COUNT_CASE), (2, 2)),
        ('a failing numbered case is a case, not a pass', count(PY_TEXT + NL + '  (3) the third : FAIL' + NL + PLANT, R.COUNT_CASE), (3, 2)),
        ('a text with no case line counts nothing, its planted line included', count(PLANT + NL + '### ### **0 of 0 -- PASS**', R.COUNT_CASE), (0, 0)),
    ]


def main():
    import b623_record as R
    sealed, h = sealed_module()
    print('test_count: the repaired counter tools/b623_record.py (working file); the sealed form at relay %s' % (h[0][:8] if sealed else 'NOT FOUND %s' % h))
    rep = cases(R.count_cases, R)
    n_pass = 0
    for i, (label, got, want) in enumerate(rep, 1):
        ok = got == want
        n_pass += ok
        print('  (%d) %s : wanted %s ; got %s ; %s' % (i, label, want, got, 'PASS' if ok else 'FAIL'))
    print('### CASES : %d ; PASSING : %d ; FAILING : %d' % (len(rep), n_pass, len(rep) - n_pass))
    refuted = None
    if sealed is not None:
        sc = cases(sealed.count_cases, R)
        bad = [i for i, (_l, got, want) in enumerate(sc, 1) if got != want]
        refuted = bool(bad)
        print('### THE SEALED FORM (the positive control): %s -- it fails cases %s' % ('REFUTED' if refuted else 'NOT REFUTED', bad or 'none'))
    else:
        print('### THE SEALED FORM (the positive control): NOT FOUND')
    ok = n_pass == len(rep) and refuted is True
    print('### ALL PASS' if ok else '### NOT ALL PASS')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
