# -*- coding: utf-8 -*-
"""b577_test_rerun.py -- THE TEST OF b576's SUITE READING THE (R177)(3)(g) ADDENDUM FORM, (R187)(4), committed with the edit.

### Cases on the form (tools/addenda.py) and on b576's G-WRITELIST-KINDS predicate itself, each printed with its verdict:
### the ruled line, citing (R186)(5), read against b576's banked paste; a control line citing (R187)(4), whose clause names
### the file, read against b577's banked paste; and the arm, handed a written list carrying relay/tools/mirror_prevbuild.json,
### PASSING only when an accepted addendum carries that basename and FAILING on a stray no addendum carries.
### Writes data/b577_test_rerun.txt and nothing else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import addenda as ADD          # noqa: E402
import b576_checks as C        # noqa: E402

D = os.path.join(ROOT, 'data')
PASTE = ADD.paste_reader(D)
L, OUT = [], []
RULED = 'WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R186)(5)'
CONTROL = 'WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R187)(4)'


def case(name, got, want):
    ok = got == want
    OUT.append(ok)
    s = '  %-86s got %-5s want %-5s %s' % (name, got, want, 'OK' if ok else '### WRONG')
    L.append(s)
    print(s)


def verdict(line):
    a = ADD.writelist_addenda(line, PASTE)
    return a[0] if a else {}


r, c = verdict(RULED), verdict(CONTROL)
L.append('  the ruled line : %s -> %s' % (RULED, r.get('why')))
L.append('  the control    : %s -> %s' % (CONTROL, c.get('why')))
case('(1) the ruled line, (R186)(5): ACCEPTED', r.get('accepted'), False)
case('(2) the control, (R187)(4): ACCEPTED', c.get('accepted'), True)
glob = ['relay/data/b576_*']
written = ['relay/data/b576_x.txt', 'relay/tools/mirror_prevbuild.json']
case('(3) b576`s arm, no addendum carrying the file', C.wl_ok(dict(written=written, globs=glob, wl_add=set())), False)
case('(4) b576`s arm, an accepted addendum carrying mirror_prevbuild.json', C.wl_ok(dict(written=written, globs=glob,
                                                                                       wl_add={'mirror_prevbuild.json'})), True)
case('(5) b576`s arm, the addendum carrying it and a stray it does not', C.wl_ok(dict(written=written + ['relay/tools/x.py'], globs=glob,
                                                                                    wl_add={'mirror_prevbuild.json'})), False)
L.append('  ### ### **%d of %d cases as wanted -- %s**' % (sum(OUT), len(OUT), 'PASS' if all(OUT) else 'FAIL'))
print(L[-1])
io.open(os.path.join(D, 'b577_test_rerun.txt'), 'w', encoding='utf-8', newline='\n').write(
    'b577 -- THE TEST OF b576`S SUITE READING THE ADDENDUM FORM, (R187)(4)\n\n' + '\n'.join(L) + '\n')
sys.exit(0 if all(OUT) else 1)
