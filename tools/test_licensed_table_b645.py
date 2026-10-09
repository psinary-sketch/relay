# -*- coding: utf-8 -*-
"""test_licensed_table_b645.py -- THE PLANTED TESTS OF tools/licensed_table.py, (R255)(3): one per verdict, and a HAND row lacking its
citation (expected refused), run before any real row is read. Each case prints `  (n) ... PASS|FAIL`; the last line the count."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import licensed_table as LT  # noqa: E402

ROWS = {'foo': ('P.foo', 'DERIVES'), 'bar': ('P.bar', 'INTERFACES'), 'baz': ('P.baz', 'DEF')}


def lookup(n):
    return ROWS.get(n.split('.')[-1])


def tlook(n):
    h = ROWS.get(n.split('.')[-1])
    return (h[0], h[1], 'theorem %s : X' % h[0], 'pin0001') if h else None


CASES = []


def case(desc, got, want):
    CASES.append((desc, got == want, got, want))


# (1) MATCHES: a plain docstring on a DERIVES declaration, generated
r1 = LT.docstring_row('d1', 'kernel@82550e4:P.foo', 'The identity, both directions.', 'P.foo', 'theorem', 'X ↔ Y', 'DERIVES', 'rule', [], lookup)
case('a plain docstring on a DERIVES theorem reads MATCHES and the table takes it', (r1['verdict'], LT.check(r1)), ('MATCHES', []))
# (2) UNDERSTATES: a docstring calling a DERIVES declaration open, generated; refused until its re-cut sentence is written
r2 = LT.docstring_row('d2', 'P/File.lean:12', 'The seam `foo` stays open here.', None, 'module', 'foo DERIVES', None, None, [], lookup, module=True)
r2c = LT.recut(r2, 'The seam `foo` is compiled (DERIVES at the standard three).')
case('a module line calling a DERIVES name open reads UNDERSTATES, refused without its re-cut, taken with it',
     (r2['verdict'], bool(LT.check(r2)), LT.check(r2c)), ('UNDERSTATES', True, []))
# (3) OVERREACHES: an unconditional marker on an INTERFACES declaration, generated
r3 = LT.docstring_row('d3', 'kernel@82550e4:P.bar', 'The bound, unconditionally.', 'P.bar', 'theorem', 'B', 'INTERFACES', 'rule', ['h : Prem'], lookup)
case('an unconditional docstring on an INTERFACES theorem reads OVERREACHES', r3['verdict'], 'OVERREACHES')
# (4) UNLICENSED: a statement-grade claim asserted as established, by the intake mapping, retired to ERRATA
v4 = LT.map_intake('statement-grade', 'established')
r4 = dict(id='m4', source='day1/A.md:10', stated='The catalogue is complete.', licensed='no terminal and no citation reaches it', by='HAND',
          cited=['day1/A.md:10', 'relay@bd1387be:data/terminal_table.md:7'], verdict=v4, action='RETIRE TO ERRATA: asserted without licence')
case('a statement-grade claim stated as established reads UNLICENSED and the table takes its retirement', (v4, LT.check(r4)), ('UNLICENSED', []))
# (5) a HAND row lacking its citation: refused, and the whole table refused with it
r5 = dict(id='h5', source='day1/A.md:11', stated='S', licensed='L', by='HAND', cited=[], verdict='MATCHES', action='none')
c5, f5 = LT.table([r1, r5])
case('a HAND row without its citation is refused, and the table with it', (bool(LT.check(r5)), c5, 'h5' in f5), (True, None, True))
# (6) a MATCHES row carrying an action is refused; a verdict outside the four is refused
r6 = dict(r1, id='d6', action='RE-CUT: x')
r6b = dict(r1, id='d6b', verdict='PARTLY')
case('MATCHES with an action, or a fifth verdict, is refused', (bool(LT.check(r6)), bool(LT.check(r6b))), (True, True))
# (7) a terminal-naming claim generated against the terminal's row: DERIVES claimed of an INTERFACES row OVERREACHES
r7 = LT.terminal_row('t7', 'P/MAP.md:24', 'bar DERIVES', 'bar', 'DERIVES', tlook)
case('a claim naming a terminal at a grade above its row reads OVERREACHES', r7['verdict'], 'OVERREACHES')
# (8) an intake pair outside the mapping raises (nothing guessed)
try:
    LT.map_intake('kernel-verified', 'open')
    got8 = 'no raise'
except KeyError:
    got8 = 'raised'
case('an intake pair outside the printed mapping raises', got8, 'raised')
# (9) the counts: a clean table counts each verdict once
c9, f9 = LT.table([r1, r2c, LT.recut(r3, 'The bound, on the premise h.'), r4])
case('a clean table of four rows counts one of each verdict', (dict(c9) if c9 else None, f9),
     ({'MATCHES': 1, 'UNDERSTATES': 1, 'OVERREACHES': 1, 'UNLICENSED': 1}, {}))

ok = 0
for i, (desc, good, got, want) in enumerate(CASES, 1):
    ok += good
    print('  (%d) %s -- got %r -- %s' % (i, desc, got, 'PASS' if good else 'FAIL (wanted %r)' % (want,)))
print('### ### **%d of %d cases as wanted -- %s**' % (ok, len(CASES), 'PASS' if ok == len(CASES) else 'FAIL'))
sys.exit(0 if ok == len(CASES) else 1)
