# -*- coding: utf-8 -*-
"""test_addenda_writelist.py -- THE TEST OF (R177)(3)(g)'S WRITE-LIST ADDENDUM FORM (b567), committed with it.

### Cases on the reader (tools/addenda.py) and on b566's G-WRITELIST-KINDS arm itself, each printed with its verdict:
### the b566 line ACCEPTED; a file no ruling clause names REFUSED (the mutation (N1) asks for); a clause cited that does not
### name the file REFUSED; a ruling not banked REFUSED; a line not of the form REFUSED; and the arm, handed b566's real stray
### set, PASSES only with the accepted addendum and FAILS with a stray the addendum does not carry.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import addenda as ADD

D = os.path.join(ROOT, 'data')
PASTE = ADD.paste_reader(D)
OUT = []


def case(name, got, want):
    ok = got == want
    OUT.append(ok)
    print('  %-74s got %-5s want %-5s %s' % (name, got, want, 'OK' if ok else '### WRONG'))


def acc(line):
    r = ADD.writelist_addenda(line, PASTE)
    print('    %s -> %s' % (line, r[0]['why'] if r else 'NOT READ'))
    return bool(r) and r[0]['accepted']


def main():
    print('### test_addenda_writelist -- (R177)(3)(g)')
    c3 = ADD.clause(PASTE('R176'), 'R176', 3)
    print('  (R176)(3) read: %d chars, opens "%s"' % (len(c3), c3[:60]))
    case('the clause (R176)(3) is found in the banked paste', bool(c3), True)
    case('b566 line: Vendored/Bulka/LICENSE carried by (R176)(3)', acc('WRITE-LIST ADDENDUM: Vendored/Bulka/LICENSE, carried by (R176)(3)'), True)
    case('MUTATION: Vendored/Bulka/README.md carried by (R176)(3) -- no clause names it',
         acc('WRITE-LIST ADDENDUM: Vendored/Bulka/README.md, carried by (R176)(3)'), False)
    case('MUTATION: b471_someone_elses_bank.txt carried by (R176)(3)',
         acc('WRITE-LIST ADDENDUM: data/b471_someone_elses_bank.txt, carried by (R176)(3)'), False)
    case('MUTATION: LICENSE carried by (R176)(7), a clause that does not name it',
         acc('WRITE-LIST ADDENDUM: Vendored/Bulka/LICENSE, carried by (R176)(7)'), False)
    case('MUTATION: LICENSE carried by (R9999)(1), a ruling not banked', acc('WRITE-LIST ADDENDUM: Vendored/Bulka/LICENSE, carried by (R9999)(1)'), False)
    case('MUTATION: a line not of the form', acc('WRITE-LIST ADDENDUM: Vendored/Bulka/LICENSE carried by R176 3'), False)
    names_all = [ADD.names(ADD.clause(PASTE('R176'), 'R176', k), 'README.md')[0] for k in range(1, 8)]
    case('MUTATION: README.md is named by NO clause (1)-(7) of (R176)', any(names_all), False)

    # ### the arm itself, on b566's real stray set: the face's globs, the act's kinds as the suite read them ('LICENSE' the stray)
    import b566_checks as C
    arm = [a for a in C.ARMS if a[0] == 'G-WRITELIST-KINDS'][0]
    face = C.read(C.FACE)
    globs = C.globs_of(face)
    import fnmatch
    print('  the face`s (W) globs cover LICENSE: %s' % any(fnmatch.fnmatch('LICENSE', g) for g in globs))
    real = ADD.accepted_bases(C.read(os.path.join(D, 'b566_writelist_addendum.txt')), PASTE)
    print('  the addendum bank`s accepted basenames: %s' % sorted(real))
    S = dict(face=face, kinds={'LICENSE', 'b566_ferry.txt'}, wl_add=real)
    case('ARM: the real stray LICENSE with the accepted addendum -> PASS', bool(arm[2](S)), True)
    case('ARM: the real stray LICENSE with NO addendum -> FAIL', bool(arm[2](dict(S, wl_add=set()))), False)
    # ### the mutation's file must be a TRUE stray: no (W) glob covers it (README.md is covered -- b566 wrote the kernel README)
    mut = 'CHANGELOG.md'
    case('the mutation`s file %s is covered by NO (W) glob' % mut, any(fnmatch.fnmatch(mut, g) for g in globs), False)
    case('the mutation`s file %s is named by NO clause (1)-(7) of (R176)' % mut,
         any(ADD.names(ADD.clause(PASTE('R176'), 'R176', k), mut)[0] for k in range(1, 8)), False)
    case('ARM MUTATION: a stray %s no clause names, beside the addendum -> FAIL' % mut,
         bool(arm[2](dict(S, kinds=S['kinds'] | {mut}))), False)
    case('ARM MUTATION: an addendum REFUSED (%s by (R176)(3)) does not carry it -> FAIL' % mut,
         bool(arm[2](dict(S, kinds=S['kinds'] | {mut},
                          wl_add=real | ADD.accepted_bases('WRITE-LIST ADDENDUM: Vendored/Bulka/%s, carried by (R176)(3)' % mut, PASTE)))), False)
    case('ARM: its own positive control still FAILS', bool(arm[2](arm[3](dict(S)))), False)
    print('### %d of %d cases as wanted -- %s' % (sum(OUT), len(OUT), 'PASS' if all(OUT) else '### FAIL'))
    return 0 if all(OUT) else 1


if __name__ == '__main__':
    sys.exit(main())
