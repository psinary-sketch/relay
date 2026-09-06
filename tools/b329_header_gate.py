# -*- coding: utf-8 -*-
"""b329_header_gate.py -- THE GATE FOR "GENERAL AND PER-CELL ARE STATED IN THE MODULE HEADER, NEVER AVERAGED".

### ### **WHAT IT CHECKS, LEXICALLY AND NO MORE:** ### a kernel module's leading `/- ... -/` header must
### carry BOTH scope words -- `GENERAL` and `PER CELL` -- each as a statement of its own (a line that
### begins with the word after optional whitespace), plus the `UNAVAILABLE` arm and the sentence of
### what it does not certify; and it must carry NO averaging phrase (a claim that the whole is general).
### ### **BOTH POLARITIES:** ### `fixtures()` returns (fires, quiet): fires on a header that carries one
### scope word only and an averaging phrase; quiet on `FiniteSideSeal.lean`'s own header.
### ### **WHAT IT CANNOT DO:** ### read whether a theorem IS general. ### That is the profile's and the
### reader's; this is a check that the header SAYS which is which.
"""
import io
import os
import re
import sys

SIDE = r'D:\SIDE-global-section'
MODULE = os.path.join(SIDE, 'Core', 'FiniteSideSeal.lean')

AVERAGING = [r'(?i)\b(entirely|fully|all)\s+general\b', r'(?i)in full generality',
             r'(?i)\bone general theorem of the finite side\b', r'(?i)\bproved in general at every cell\b']


def header_of(text):
    m = re.search(r'/-(.*?)-/', text, re.S)
    return m.group(1) if m else ''


def check(text):
    """### (ok, reasons) over a module's SOURCE TEXT; the header is its first block comment."""
    h = header_of(text)
    reasons = []
    if not h:
        return False, ['no header block']
    if not re.search(r'^\s*GENERAL\b', h, re.M):
        reasons.append('no line stating GENERAL as its own scope')
    if not re.search(r'^\s*PER CELL\b', h, re.M):
        reasons.append('no line stating PER CELL as its own scope')
    if 'UNAVAILABLE' not in h:
        reasons.append('no UNAVAILABLE arm named')
    if 'WHAT IT DOES NOT CERTIFY' not in h:
        reasons.append('no statement of what it does not certify')
    for pat in AVERAGING:
        if re.search(pat, h):
            reasons.append('averaging phrase: %r' % pat)
    return (not reasons), reasons


FIRING = """/-
  A MODULE. Vanilla Lean.
  GENERAL: the finite side's silence, proved for every prime and level -- and the
  compact part's zero is proved in general at every cell, so the whole file is
  entirely general.
  WHAT IT DOES NOT CERTIFY: nothing is excluded.
-/
namespace X
end X
"""


def fixtures():
    fires = not check(FIRING)[0]
    quiet = check(io.open(MODULE, encoding='utf-8').read())[0] if os.path.exists(MODULE) else False
    return fires, quiet


def main():
    ok, reasons = check(io.open(MODULE, encoding='utf-8').read())
    f, q = fixtures()
    print('b329_header_gate.py -- fires on the averaging fixture: %s ; quiet on FiniteSideSeal.lean: %s' % (f, q))
    print('  FiniteSideSeal.lean header : %s %s' % ('PASS' if ok else '### FAIL ###', reasons if reasons else ''))
    return 0 if (ok and f and q) else 1


if __name__ == '__main__':
    sys.exit(main())
