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

# (10) the second shape: "NOT PROVED" attached to a theorem is no proof claim and no open claim against its grade (b645's PairTerm read)
r10 = LT.docstring_row('d10', 'P/F.lean:3', 'THE FAR FACTOR AS A NAMED HYPOTHESIS, NOT PROVED (`bar`, `foo`).', None, 'module', 's', None, None, [],
                       lookup, module=True)
case('"NOT PROVED" beside theorem names reads MATCHES (negation guarded, no open claim against a grade)', r10['verdict'], 'MATCHES')
# (11) (D3): a DISCHARGED premise head called open UNDERSTATES; an OPEN head called proved OVERREACHES
ST = {'Prem': 'DISCHARGED', 'Open': 'OPEN'}
r11 = LT.docstring_row('d11', 'P/F.lean:4', 'The seam premise `Prem` stays open here.', None, 'module', 's', None, None, [], lookup, module=True,
                       status=ST.get)
r11b = LT.docstring_row('d11b', 'P/F.lean:5', 'Its hypothesis Open_x aside, `Open` is proved.', None, 'module', 's', None, None, [], lookup,
                        module=True, status=ST.get)
case('(D3) a DISCHARGED premise called open reads UNDERSTATES, an OPEN premise called proved OVERREACHES',
     (r11['verdict'], r11b['verdict']), ('UNDERSTATES', 'OVERREACHES'))
# (12) a bare dotted name resolves through the lookup: "P.bar is proved outright" OVERREACHES its INTERFACES row
r12 = LT.docstring_row('d12', 'P/F.lean:6', 'Hence P.bar is proved outright.', None, 'module', 's', None, None, [], lookup, module=True)
case('a bare dotted name read through the lookup: P.bar called proved reads OVERREACHES', r12['verdict'], 'OVERREACHES')

# (13) (D4): a first sentence claiming an equivalence over a one-direction statement OVERREACHES; over an ↔ statement MATCHES
r13 = LT.docstring_row('d13', 'kernel@82550e4:P.foo', 'The two are equivalent. Proof by cases.', 'P.foo', 'theorem', '(h : A) ⊢ B', 'DERIVES',
                       'rule', [], lookup)
r13b = LT.docstring_row('d13b', 'kernel@82550e4:P.foo', 'The two are equivalent.', 'P.foo', 'theorem', '⊢ A ↔ B', 'DERIVES', 'rule', [], lookup)
case('(D4) an equivalence claimed of a one-direction statement reads OVERREACHES, of an ↔ statement MATCHES',
     (r13['verdict'], r13b['verdict']), ('OVERREACHES', 'MATCHES'))

# (14) (D5), the PlateauRamp shape: a claim about Mathlib's scope at the pin is flagged and refused until read by hand; the hand row is taken
doc14 = 'O1 `ConvStep`, the convolution theorem (Mathlib at the pin holds it for Schwartz functions only, `fourier_convolution`).'
r14 = LT.docstring_row('d14', 'P/F.lean:19', doc14, None, 'module', 's', None, None, [], lookup, module=True)
r14h = dict(r14, by='HAND', cited=['mathlib4@de5ce8a9:Mathlib/Analysis/Fourier/Convolution.lean:119'], verdict='UNDERSTATES',
            action='RE-CUT: Mathlib at the pin holds it for integrable functions at real frequency.')
case('(D5) a Mathlib-scope claim is flagged and refused as generated, taken as a cited HAND row',
     (bool(r14.get('hand_needed')), bool(LT.check(r14)), LT.check(r14h)), (True, True, []))

# (15) (D6): a Prop's definition called NOT PROVED while a binder-free theorem concludes it UNDERSTATES; with no such theorem MATCHES
pb = {'P.seam': 'theorem P.seam_holds : P.seam (F.lean :84)'}.get
r15 = LT.docstring_row('d15', 'kernel@82550e4:P.seam', 'The seam, a Prop, NOT PROVED: from the strip to RH.', 'P.seam', 'def', 'Prop', 'DEF',
                       'rule', [], lookup, proved_by=pb)
r15b = LT.docstring_row('d15b', 'kernel@82550e4:P.other', 'Another Prop, NOT PROVED.', 'P.other', 'def', 'Prop', 'DEF', 'rule', [], lookup,
                        proved_by=pb)
case('(D6) a Prop called NOT PROVED that a theorem concludes reads UNDERSTATES; one no theorem concludes MATCHES',
     (r15['verdict'], r15b['verdict']), ('UNDERSTATES', 'MATCHES'))
# (16) (D5) does not read "holds if and only if" as a scope claim
r16 = LT.docstring_row('d16', 'P/F.lean:77', 'Mathlib`s `RiemannHypothesis` holds if and only if the coefficients are nonnegative.', None, 'module', 's',
                       None, None, [], lookup, module=True)
case('(D5) "holds if and only if" is no Mathlib-scope claim', bool(r16.get('hand_needed')), False)

ok = 0
for i, (desc, good, got, want) in enumerate(CASES, 1):
    ok += good
    print('  (%d) %s -- got %r -- %s' % (i, desc, got, 'PASS' if good else 'FAIL (wanted %r)' % (want,)))
print('### ### **%d of %d cases as wanted -- %s**' % (ok, len(CASES), 'PASS' if ok == len(CASES) else 'FAIL'))
sys.exit(0 if ok == len(CASES) else 1)
