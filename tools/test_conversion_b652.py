# -*- coding: utf-8 -*-
"""test_conversion_b652.py -- THE PLANTED CASES OF THE ONE CONVERSION, (R262)(2), b652.

### A head carrying a backtick possessive is landed in a scratch ledger through tools/b652_record.py's append_to and found by its line_of at
### the line it landed on; b551_record's look-up (the straight conversion b651's suite and trail route used) is read beside it as the control
### that misses. No ledger of PLACE-papers is touched: the scratch ledger lives in a temporary directory removed at the end.
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b652_record as R   # noqa: E402
import b551_record as OLD  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEAD = '### b999 — lane three, a planted act: the largest kernel`s docstrings, the author`s word'
BODY = '\n' + HEAD + ': a planted line, landed for the look-up and nothing else.\n'
res = []


def case(n, what, ok):
    res.append(ok)
    print('  (%d) %s -- %s' % (n, what, 'PASS' if ok else 'FAIL'))


d = tempfile.mkdtemp(prefix='b652_conv_')
try:
    led = os.path.join(d, 'LEDGER.md')
    open(led, 'wb').write('# a scratch ledger\n\nline three\n'.encode('utf-8'))
    case(1, 'conv writes a backtick possessive typographic (kernel`s -> %s ; (R262)`s -> %s)' % (R.conv('kernel`s'), R.conv('(R262)`s')),
         R.conv('kernel`s') == 'kernel’s' and R.conv('(R262)`s') == '(R262)’s')
    case(2, 'conv leaves a code span and a ruling citation alone and changes nothing applied twice',
         R.conv('`(R262)`(2) and `conv`') == '`(R262)`(2) and `conv`' and R.conv(R.conv(HEAD)) == R.conv(HEAD))
    r = R.append_to(led, BODY)
    lines = open(led, encoding='utf-8').read().split('\n')
    want = [i + 1 for i, l in enumerate(lines) if l.startswith('### b999')]
    case(3, 'the planted head landed once, at :%s, its bytes appended to the ledger unchanged above (prefix %s)' % (want, r['prefix']),
         want == [5] and r['prefix'])
    got = R.line_of(led, HEAD)
    case(4, 'the look-up by conv finds the landed line (:%s)' % got, got == 5)
    old = OLD.line_of(led, HEAD)
    case(5, 'CONTROL: the straight conversion of b551_record (the look-up of b651`s suite and trail route) misses it (:%s)' % old, old is None)
    try:
        R.guard_absent(led, HEAD)
        refused = False
    except SystemExit:
        refused = True
    case(6, 'the guard by conv refuses a second landing of the same head', refused)
    plain = '### b999 a head with no possessive'
    R.append_to(led, '\n' + plain + '\n')
    case(7, 'a head with no backtick passes conv unchanged and is found (:%s)' % R.line_of(led, plain),
         R.conv(plain) == plain and R.line_of(led, plain) == 7)
finally:
    shutil.rmtree(d)

n = sum(res)
print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
sys.exit(0 if n == len(res) else 1)
