# -*- coding: utf-8 -*-
"""test_banned_terms_backmatter.py -- THE TEST OF banned_terms.py's BACK-MATTER READ (b586, under (R196)(2)).

### Two fixtures, written (never deleted) as relay data/b586_scanner_fixture_listed.md and
### data/b586_scanner_fixture_mutant.md, each scanned by the scanner as a subprocess:
###   LISTED -- a body line carrying the stem as a name and a body line carrying a dated stem, both listed
###             in the back matter (one name row, one carried-by-history row): both read EXCEPTED, the
###             verdict CLEAN.
###   MUTANT -- the same file with one more body line carrying the stem that no back-matter row lists:
###             that use reads LIVE and the verdict NOT CLEAN.
### Exit 0 only when both polarities hold.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SCANNER = os.path.join(ROOT, 'tools', 'banned_terms.py')
NL = chr(10)
STEM = 'g' + 'ap'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BODY = ['# Fixture edition', '',
        'The prime %s problem is named as its literature names it.' % STEM,
        'The v0.1 entry: a %s at the step, recorded as dated.' % STEM, '']
MUTANT_LINE = 'An unlisted sentence speaks of a %s in the argument.' % STEM
TAIL = ['<!-- b586 (R196) THE v0.2 EDITION`S BACK MATTER, 2026-10-01 -->', '',
        '| this edition’s line | Status |', '|:--|:--|',
        '| :3 | excepted, the object’s own name |',
        '| :8 | the v0.1 entry | :4, carried-by-history | carried |', '']


def write(name, lines):
    p = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    return p


def scan(p):
    r = subprocess.run([sys.executable, SCANNER, '--new', p], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    live = int(re.search(r'live uses\s*:\s*(\d+)', r.stdout).group(1))
    exc = re.search(r'excepted \(back matter\): names (\d+) ; carried-by-history (\d+)', r.stdout)
    v = re.search(r'^\s*VERDICT\s*: (.+)$', r.stdout, re.M).group(1).strip()
    return r.returncode, live, (int(exc.group(1)), int(exc.group(2))) if exc else None, v


def main():
    listed = write('b586_scanner_fixture_listed.md', BODY + TAIL)
    mutant = write('b586_scanner_fixture_mutant.md', BODY[:4] + [MUTANT_LINE] + TAIL)
    ok = True
    rc, live, exc, v = scan(listed)
    a = (rc == 0 and live == 0 and exc == (1, 1) and v == 'CLEAN')
    print('LISTED  exit %d ; live %d ; excepted names/history %s ; verdict %s ; %s' % (rc, live, exc, v, 'HELD' if a else '### FAILED'))
    ok = ok and a
    rc, live, exc, v = scan(mutant)
    b = (rc == 1 and live == 1 and exc == (1, 1) and v == 'NOT CLEAN')
    print('MUTANT  exit %d ; live %d ; excepted names/history %s ; verdict %s ; %s' % (rc, live, exc, v, 'HELD' if b else '### FAILED'))
    if b:
        print('MUTANT NOT CLEAN -- the unlisted stem reads live')
    ok = ok and b
    print('TEST %s' % ('HELD' if ok else '### FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
