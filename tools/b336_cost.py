# -*- coding: utf-8 -*-
"""b336_cost.py -- THE COST CENSUS: A TYPED COST COLUMN ON THE FACES LEDGER, THROUGH ITS WRITER; THE SORTED VIEW;
ROW L2; THE ADDENDUM TO b328's BLOCK.

### ### **WHAT A COST IS HERE.** ### For each row of the ledger, what moving it ONE grade would take, typed as one
### of READ / IMPORT / MEASUREMENT / DERIVATION / CONSTRUCTION (the registration's (C), cheapest kind first), with
### the record's price quoted at its emitter where the record prices the step and `no price in the record`
### elsewhere. ### A cost is not a grade, not a plan, not a prediction. ### **NO GRADE MOVED**: the rows above are
### never rewritten; the census is an append-only block naming every row id (the ledger's own law), the new row
### L2 goes through `write_row` with its quotations verified, the addendum is a second block naming b328's update.
### ### Every write is idempotent; the sorted view is a relay data file; one run file, numbered on repeat writes.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
B327 = os.path.join(D, 'b327_the_faces_ledger.txt')
SORTED = os.path.join(D, 'b336_cost_sorted.txt')
MARK_C = '<!-- b336 cost census -->'
MARK_A = '<!-- b336 addendum to b328 -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TYPE_ORDER = ['READ', 'IMPORT', 'MEASUREMENT', 'DERIVATION', 'CONSTRUCTION']
NO_PRICE = 'no price in the record'

# ### the four prices, each a quotation at its emitter (located in the extract file first)
P_DOMAIN = "the unit's domain factor, b322: *\"a factor of `3.104e+02`\"* -- `X = 3.973e+04` required against `X = 128` reached, *\"AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS\"* one"
P_RATIO = "the exponent's ratio, b321: the two remainder copies *\"are apart by between one twenty-fourth and one fifth of\"* the instrument's own distance from the equality (0.000981080 against 0.023223882 at a = 1.3; 0.003993528 against 0.018807781 at a = 1.41)"
P_ACTS = "the instrument's act count, b321_run: the instrument imported from six acts (b316 instrument, b317 assembly, b318 square, b319 stable, b320 weil, b321 window)"
P_WIDTHS = "the crossing widths, b328: *\"SEES IT\"* at the even widths 40, 81, 160 and the odd widths 20, 40, 81, 160; b334: three aims, (a = 40, gamma = 16.290216), (a = 81, gamma = 16.290216), (a = 81, gamma = 46.960994)"

# ### (id, holds -> one grade up, type, what moving it one grade would take, the record's price)
COST = [
    ('R1', 'NAMED -> PROVED', 'CONSTRUCTION', "a proof of the universality hypothesis itself -- the face is the premise; *\"the hypothesis is load-bearing\"*", NO_PRICE),
    ('R2', 'PROVED one direction -> both directions', 'CONSTRUCTION', "the converse of `ConservationBridge.riemann_hypothesis` compiled; *\"the converse is not compiled and the face stays open\"*", NO_PRICE),
    ('R3', 'NAMED-ONLY -> compiled STRUCTURE', 'CONSTRUCTION', "the totality premise compiled as structure where the pentagon module lists it NOT-COMPILED, *\"its native shadow the T3 pinned sorry\"*", NO_PRICE),
    ('R4', 'PROVED to the finite range -> all n', 'DERIVATION', "the decomposition conjunct (Guinand-Weil) and the tail premise, which *\"remain named and open\"*; the certificate reaches *\"exactly to where discrimination would begin, and no further\"*", "the certificate's own reach only: `N_0(T) ~ 2T^2`; " + NO_PRICE + ' beyond it'),
    ('R5', 'PROVED, the distance -> a positive pairing', 'CONSTRUCTION', "a positive pairing over Q, which the deposit disclaims asserting; *\"no positive pairing is known\"*", NO_PRICE),
    ('F1', 'MEASURED as a control -> the Li family closed', 'MEASUREMENT', "`W-ORD-LI-FAMILY-CONTROL`: the formula closed on the Li family through the corpus's own channels, *\"priced and not run\"*", "L1: *\"priced at one act, not run\"*"),
    ('F2', 'MEASURED, the sign certified -> the size certified', 'MEASUREMENT', "the domain axis converged where b320 found it DRIFTING and b322 found it UNDER-RESOLVED; the exponent question closed by a measurement whose two copies part further than they sit from the equality", P_DOMAIN + '; ' + P_RATIO + '; ' + P_ACTS),
    ('F3', 'MEASURED to n = 300 -> all n', 'DERIVATION', "the all-n inequality, *\"which is the face R4 itself\"*", NO_PRICE),
    ('F4', 'NAMED-ONLY -> a space', 'CONSTRUCTION', "*\"the positive space on the zeros\"*, the wall's own object; the realization is disclaimed (R5)", NO_PRICE),
    ('F5', 'MEASURED and DERIVED at a finite place -> the archimedean place', 'DERIVATION', "a reading at the archimedean place where b311 found the finite side's question *\"does not parse -- a refusal, not a negative result\"*", NO_PRICE),
    ('F6', 'IMPORTED, the archimedean member -> constructed', 'CONSTRUCTION', "the archimedean family as an object, against the arc's standing boundary *\"NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`\"*", NO_PRICE),
    ('F7', 'MEASURED (DOES NOT SEE IT; SEES IT at seven of eight) -> the crossing located', 'MEASUREMENT', "the crossing region over aims and widths, charted by b334 at two widths and named as the negative control charted", P_WIDTHS),
    ('L1', 'IMPORTED and DERIVED -> the bridge', 'DERIVATION', "`W-ORD-LI-WEIL-BRIDGE`: *\"a relation between the compressed square on the Sonin family and the finite-place channel\"* on the Li family, *\"none is in the record\"*", NO_PRICE),
    ('S1', 'STATED; the softest pair K5, K6 at MEASURED-AT-COVERED-CELLS -> MEASURED-ON-FAMILIES', 'MEASUREMENT', "the square and the remainder reached on aimed families (b334: NOT REACHED at the wide widths, the eps evaluator and the frame measured); b334 charted the families and conferred nothing", P_DOMAIN + '; ' + P_ACTS),
    ('L2', 'STATED', 'ZERO', "nothing: the relation is stated from the record and nothing is owed on it; what is owed on the bridge is L1's", 'cost zero'),
]

L2 = dict(
    id='L2',
    cells=[
        "L2 -- the pole-constant relation between the Li and positivity faces: the deposit's archimedean channel on the Li family is the archimedean distribution plus the pole constant `1`; the Li margin and the Sonin margin are two evaluations of one distribution separated by the pole constant (b331's fold) and are not one functional (FINDINGS)",
        "the fourth, at two families -- a relation between the Li face (F3, L1) and the positivity face (F2, S1); STATED, cost zero",
        "INTERNAL -- relay `data/b327_the_faces_ledger.txt` (QUESTION ONE, the constituent quoted); `FINDINGS.md` (the fold's b327 entry: *\"plus the pole constant `1`\"*, *\"two evaluations of one distribution and are not one functional\"*); relay `data/b331_the_fold.txt` (*\"separated by the pole constant\"*); row L1 of this ledger (the derivation under b327's sealed bar). IMPORTED -- the source's *\"a contribution from the pole at s = 0\"* (Lagarias, arXiv:math/0404394v4, pinned at b327)",
        "STATED -- no proof here, no grade conferred, the relation as the record states it: b327, *\"the archimedean place PLUS the pole-at-zero constant -- 'log s' in the keystone's own split\"*; L1, *\"\u03bb_A(n) = S\u221e(n) + 1 for every n \u2265 1\"*; the fold at FINDINGS, *\"two evaluations of one distribution and are not one functional\"*; b331's bank, *\"separated by the pole constant\"*. COST ZERO: nothing is owed on the relation; what is owed on the bridge is L1's.",
        "166, 167 (b327); the b336 row",
        "none typed by this act. To L1: the same relation, there derived under a sealed bar and corroborated, here stated face to face. To F2 and F3: the fold's sentence, two evaluations of one distribution and not one functional, separated by the pole constant (b331); the bridge between the margins themselves (`W-ORD-LI-WEIL-BRIDGE`) stays owed at L1.",
    ],
    quotes=[
        (B327, "the archimedean place PLUS the pole-at-zero constant -- *\"log s\"* in the keystone's own split,", False),
        (B327, '*"a contribution from the pole at s = 0"* in the source.', False),
        (FINDINGS, 'the archimedean distribution on the Li family plus the pole constant', True),
        (FINDINGS, 'two evaluations of one distribution and are not one functional', True),
        (os.path.join(D, 'b331_the_fold.txt'), 'two evaluations of one distribution separated by the pole constant', True),
        (LEDGER, 'gives \u03bb_A(n) = S\u221e(n) + 1 for every n \u2265 1', False),
    ],
)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def sorted_rows():
    def key(r):
        rid, _h, typ, _w, price = r
        return (TYPE_ORDER.index(typ) if typ in TYPE_ORDER else -1, 0 if price not in (NO_PRICE, 'cost zero') and not price.startswith("the certificate's") else 1, rid)
    return sorted(COST, key=key)


def block_lines():
    L = ['', MARK_C, '',
         '## THE COST CENSUS \u2014 filed 2026-09-06 (b336): a typed cost column, keyed to the rows',
         '',
         "*Rows above are never rewritten; this block is the typed cost column the order asked for, one line per row id, through the writer's `append_block`. A cost is what moving the row ONE grade would take, typed as READ / IMPORT / MEASUREMENT / DERIVATION / CONSTRUCTION (cheapest kind first), with the record's price quoted at its emitter where the record prices the step. A cost is not a grade, not a plan, not a prediction (b322: a price is not a prediction). NO GRADE MOVED. The sorted view is relay `data/b336_cost_sorted.txt`.*",
         '',
         "| row | holds \u2192 one grade up | cost type | what moving it one grade would take | the record's price, quoted at its emitter |",
         '|:--|:--|:--|:--|:--|']
    for rid, holds, typ, what, price in COST:
        L.append('| **%s** | %s | %s | %s | %s |' % (rid, holds, typ, what, price))
    L.append('')
    L.append('*Filed by b336 (relay `data/b336_the_cost_census.txt`). Nothing about totality, h2, or the roster. M-2 unchanged under its cap.*')
    return L


def addendum_lines():
    return ['', MARK_A, '',
            "## ADDENDUM \u2014 filed 2026-09-06 (b336): to b328's update (the discriminating family), the phase rule refined",
            '',
            "*Rows and blocks above are never rewritten; an addendum names the block it bears on. Written through the writer's `append_block`.*",
            '',
            "| block / rule | as b328 stated it | as b334's map refines it, the chart's sign column cited |",
            '|:--|:--|:--|',
            "| **b328's update** (the discriminating family), the phase rule | *\"NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE\"* \u2014 stated where every phase measured sat near ninety degrees (88.10 to 89.39 at the four widths) | The quadruple's term is `4 \u2016G\u2016\u00b2 cos 2\u03c6`, negative only for 45\u00b0 < \\|\u03c6\\| < 135\u00b0. b334's chart (relay `data/b334_chart_run.txt`, the sign column: *\"the trailing sign is the quadruple's term S_4 = 4 \\|G\\|^2 cos 2 phi, negative only between 45 and 135 degrees\"*) counted 270 aims past the 45\u00b0 threshold, 170 with a negative term, 100 with the phase near 180\u00b0 and a positive term. The rule as b328 stated it is the condition at b328's own phases and is unaffected there; the refinement is the general condition. No grade moved; b328's block and bank are not edited. |",
            '',
            '*Filed by b336 (relay `data/b336_the_cost_census.txt`).*']


def main():
    fails = []
    rec('=' * 100)
    rec('b336 -- THE COST CENSUS. ### the typed column through the writer; the sorted view; row L2; the addendum to b328.')
    rec('=' * 100)
    types = set(t for _i, _h, t, _w, _p in COST) - {'ZERO'}
    rec('  rows typed %d (%s) ; types used %s ; every type one of the five : %s' % (len(COST), ' '.join(r[0] for r in COST), sorted(types), types <= set(TYPE_ORDER)))
    if not types <= set(TYPE_ORDER):
        fails.append('TYPES')
    priced = [r[0] for r in COST if r[4] not in (NO_PRICE, 'cost zero') and not r[4].startswith("the certificate's")]
    rec('  rows the record prices : %s ; rows with no price in the record : %s' % (priced, [r[0] for r in COST if r[4] == NO_PRICE]))
    # ### the sorted view, emitted first (a data file; overwritten only by a repeat run of this tool)
    S = ['=' * 100, 'b336 -- THE COST CENSUS, SORTED. ### cheapest kind first (READ < IMPORT < MEASUREMENT < DERIVATION < CONSTRUCTION); inside a type, the rows the record prices first; then by id.', '=' * 100,
         '  %-4s %-14s %-70s %s' % ('row', 'type', 'holds -> one grade up', 'the record\'s price (first words)')]
    for rid, holds, typ, _w, price in sorted_rows():
        S.append('  %-4s %-14s %-70s %s' % (rid, typ, holds[:70], price[:110]))
    S.append('  ### NO GRADE MOVED. ### A cost is not a grade, not a plan, not a prediction.')
    S.append('=' * 100)
    io.open(SORTED, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(S) + chr(10))
    rec('  sorted view written : %s (%d rows)' % (os.path.basename(SORTED), len(COST)))
    st, det = W.append_block(MARK_C, block_lines())
    rec('  FACES_LEDGER.md   cost census   %-16s %s' % (st, det))
    if st not in ('WRITTEN', 'DUPLICATE'):
        fails.append('BLOCK-COST')
    st2, det2 = W.write_row(L2)
    rec('  FACES_LEDGER.md   row L2        %-16s %s' % (st2, det2))
    if st2 not in ('WRITTEN', 'DUPLICATE'):
        fails.append('ROW-L2')
    st3, det3 = W.append_block(MARK_A, addendum_lines())
    rec('  FACES_LEDGER.md   addendum      %-16s %s' % (st3, det3))
    if st3 not in ('WRITTEN', 'DUPLICATE'):
        fails.append('BLOCK-ADDENDUM')
    txt = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    rec('  marks on disk : cost %d ; addendum %d ; row L2 %d' % (txt.count(MARK_C), txt.count(MARK_A), sum(1 for ln in txt.splitlines() if ln.startswith('| L2 | '))))
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b336_cost_run' if wrote else 'b336_cost_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
