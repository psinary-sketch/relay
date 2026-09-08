# -*- coding: utf-8 -*-
"""b362_faces_row.py -- ONE NEW ROW: THE APPROXIMATION REGISTER. ### THROUGH THE LEDGER'S OWN WRITER.

### ### **THE WRITER IS `b327_faces_row.py`, IMPORTED AND NOT REIMPLEMENTED.** ### It refuses a duplicate,
### guards the cells, verifies every quotation against its emitter BEFORE writing, and reads the file back.
### ### **THE GRADE WAS FIXED IN THE LOCKED REGISTRATION BEFORE THE READING**, and it is split so that a
### reader cannot take one half for the other: ### **`IMPORTED (TRUSTED-AT-CITE)` FOR THE LOCATED
### ### STATEMENTS, AND `NAMED-ONLY` FOR EVERYTHING ABOUT THE CORPUS'S OWN HOLDINGS** -- because the corpus
### has never entered this register and a row naming one may not carry a grade about holdings that do not
### exist.
### ### **THE REGISTER IS NOT ADOPTED AND NO FACE IS PROMOTED.** ### **NO BRIDGE IS TYPED**, and the
### deposit's own refusal is quoted inside the row.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W     # noqa: E402  ### THE WRITER, IMPORTED.
import run_clock               # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


S1 = d('b362_source_baezduarte0202141.txt')
S3 = d('b362_source_burnol0103058.txt')
S5 = d('b362_source_baezduarte0205003.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


# ### THE NEXT CORRESPONDENCE ROW, READ FROM THE TABLE AND NOT TYPED.
_tbl = io.open(os.path.join(SIDE, 'CORRESPONDENCE.md'), encoding='utf-8').read()
NEXTROW = str(max(int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', _tbl, re.M)) + 1)

ROW = dict(
    id='N1',
    cells=[
        'N1 -- the approximation register: the Riemann hypothesis as the statement that a fixed indicator '
        'lies in the closed span of a family of dilations of the fractional part, equivalently that a '
        'Hilbert-space distance tends to zero -- **LOCATED AND PINNED, NOT ADOPTED**',
        'not a register of the corpus; **A REGISTER THE CORPUS HAS NEVER ENTERED**, read once under a cap '
        'and named here so that a later reader finds it read rather than unread',
        'IMPORTED -- Nyman and Beurling as stated by J.-F. Burnol, *A lower bound in an approximation '
        'problem involving the zeros of the Riemann zeta function*, arXiv:math/0103058 (rendering pinned at '
        'relay `data/b362_source_burnol0103058.txt`); the variant restricting the family to the naturals '
        'from L. Baez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis*, '
        'arXiv:math/0202141 (relay `data/b362_source_baezduarte0202141.txt`), with its sequel '
        'arXiv:math/0205003; every source fetched, hashed and extracted at relay `data/b362_locate_run.txt`',
        '**IMPORTED (TRUSTED-AT-CITE) FOR THE LOCATED STATEMENTS; NAMED-ONLY FOR EVERYTHING ABOUT THE '
        'CORPUS\u2019S OWN HOLDINGS, WHICH ARE NONE.** The criterion: *"Theorem 1.1 (Nyman, Beurling) The '
        'Riemann Hypothesis holds if and only if"* the indicator lies in the closure of the union of the '
        'finite linear combinations of the dilations, in `L2(]0, inf[, dt)`; the variant: *"Theorem 1.1. '
        'The Riemann hypothesis is equivalent to the statement that"* the same indicator lies in the '
        'closure of *"The much smaller subspace Bnat of natural Beurling functions"*. **AND THE SPACE IS '
        'NOT THE ORIGINAL ONE, WHICH THE SOURCE ITSELF FLAGS:** the criterion is quoted in a *"modified '
        'form [4] (the original formulation is related to L2(0, 1))"*. ### **THE STRUCTURAL FINDING, WHICH '
        'IS WHY THE ROW EXISTS: A FINITE INSTANCE HERE IS AN UNCONDITIONAL UPPER BOUND** -- the quantity is '
        'a distance from an indicator to a span of dilations of the fractional part, its definition '
        'mentions no zero and no hypothesis, and an infimum over a subset is at least the infimum over the '
        'whole. **SO THIS REGISTER DOES NOT CARRY THE SHORTFALL THE WINDOW ACT FOUND IN THE POSITIVITY '
        'REGISTER** (b321: an instrument standing further from the answer than the difference it was asked '
        'to resolve) -- there is no residual between instrument and answer for a signal to hide under. '
        '### **AND THE SHORTFALL IT CARRIES INSTEAD, WHICH IS THE RATE:** the criterion is a statement '
        'about a LIMIT, and an UNCONDITIONAL theorem bounds the finite side away from zero at every reach '
        '-- Baez-Duarte, Balazard, Landreau and Saias, quoted inside Burnol, on the liminf of the distance '
        'times the square root of the log, with Burnol\u2019s own note that *"If the Riemann Hypothesis '
        'fails this result is true but trivial"*. **AGAINST IT THE UPPER BOUND IS CONDITIONAL AND IS '
        'MARKED AS SUCH:** the sequel shows *"under the Riemann hypothesis"* a distance *"of order (log '
        'log n)"* to a power. ### **SO WHAT IS UNCONDITIONAL HERE IS THE OBSTRUCTION AND WHAT WOULD BE '
        'PROGRESS IS CONDITIONAL.** ### **THE CORPUS HOLDS NO VALUE IN THIS REGISTER, NO CONTROL AND NO '
        'FIXTURE**, and b362 evaluated no distance at any index. ### **VERDICT: LOCATED BUT NOT WORTH '
        'OPENING** at the reach the record can afford; the register is NOT adopted and no face is promoted',
        'CORRESPONDENCE.md row ' + NEXTROW + ' (b362)',
        '**NONE TYPED, AND THE REFUSAL IS THE POINT.** ### The uniformity obstruction REAPPEARS here and '
        'takes a different shape -- **A RATE**: what a record would hold is a family indexed by a reach and '
        'what the criterion needs is a statement about the limit, and this register is the one place that '
        'QUANTIFIES how slowly the family can approach it. ### **NOTHING IS CLAIMED ABOUT THE RELATION OF '
        'THIS INSTANCE TO THE THREE U1 ALREADY NAMES OR TO THE FOURTH**, in either direction -- not that '
        'they are the same problem, not that discharging one would touch another, not that they have a '
        'common cause. ### The deposit\u2019s own law governs this row as it governs U1: the register '
        'pentagon is compiled *"while deliberately **not** compiling the cross-register equivalences, '
        'since to compile \\"discharge one and you discharge all five\\" would be to compile '
        'RH-equivalence itself"*. ### **THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, AND A FOURTH '
        'THAT RHYMES IS A FOURTH.** ### To the positivity face: **STATED NON-COMPARISON** -- b362 says '
        'only that the two registers differ in which shortfall they carry, and types no relation between '
        'their objects.',
    ],
    quotes=[
        (S3, 'Theorem 1.1 (Nyman [14], Beurling [3]) The Riemann Hypothesis holds if and only if', False),
        (S3, 'If the Riemann Hypothesis fails this result is true but trivi al', False),
        (S1, 'Theorem 1.1. The Riemann hypothesis is equivalent to the statement that', False),
        (S1, 'The much smaller subspace Bnat of natural Beurling functions is generated', False),
        (S1, 'form [4] (the original formulation is related to L2(0, 1)), that the', False),
        (S5, 'ers from the ' + chr(64257) + 'rst in showing that under the Riemann', False),
        (MONO, 'not** compiling the cross-register equivalences', False),
    ],
)


def main():
    rec('=' * 100)
    rec('b362 -- ONE NEW ROW: N1, THE APPROXIMATION REGISTER. ### THROUGH THE LEDGER\'S OWN WRITER.')
    rec('=' * 100)
    rec('  writer : %s (IMPORTED, not reimplemented)' % os.path.basename(W.__file__))
    rec('  the correspondence row this cell names, READ FROM THE TABLE : %s' % NEXTROW)
    rec('  ### ### **THE GRADE WAS FIXED IN THE LOCKED REGISTRATION BEFORE THE READING, AND IT IS SPLIT:**')
    rec('  ### **IMPORTED (TRUSTED-AT-CITE) FOR THE LOCATED STATEMENTS; NAMED-ONLY FOR EVERYTHING ABOUT')
    rec('  ### THE CORPUS\'S OWN HOLDINGS, WHICH ARE NONE.**')
    rec('')
    st, det = W.write_row(ROW)
    rec('  ### FACES_LEDGER.md : %s' % st)
    rec('    %s' % det)
    rec('')
    rec('  ### ### **WHAT THIS ROW DOES:** ### it makes a register the corpus has never entered findable,')
    rec('  ### with its statements pinned, its finite side\'s status decided, and its obstruction named in')
    rec('  ### its own terms.')
    rec('  ### ### **WHAT IT DOES NOT DO:** ### **THE REGISTER IS NOT ADOPTED. ### NO FACE IS PROMOTED.**')
    rec('  ### **NO BRIDGE IS TYPED**, and the deposit\'s own refusal is quoted inside the row rather than')
    rec('  ### remembered.')
    rec('=' * 100)
    p = run_clock.write(D, 'b362_faces_row_run', LINES)
    io.open(d('b362_faces_row.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(status=st, detail=det, row='N1', form='NEW ROW (write_row)',
             grade='IMPORTED (TRUSTED-AT-CITE) for the located statements; NAMED-ONLY for the corpus',
             quotes=len(ROW['quotes']), corr_row=NEXTROW, adopted=False, face_promoted=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if st in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
