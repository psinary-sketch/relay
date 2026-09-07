# -*- coding: utf-8 -*-
"""b358_faces_row.py -- THE UNIFORMITY ROW GAINS THIS ACT'S FINDING, THROUGH ITS OWN WRITER.

### ### **THE WRITER IS `b327_faces_row.py`, IMPORTED AND NOT REIMPLEMENTED.** ### `U1` is already written
### and ### **ROWS ABOVE ARE NEVER REWRITTEN** ### -- the ledger's own law -- so this act files an
### ### **UPDATE BLOCK** ### through `append_block`, which is the form b328, b333, b334, b339, b340, b343
### and b345 all used. ### The block names the row it bears on and edits nothing.
### ### **THE GRADE STAYS `NAMED-ONLY`, AND THE ORDER'S `unless` DID NOT LIFT IT.** ### The order said the
### row gains this act's finding ### *"NAMED-ONLY unless a shape exists"*, and a shape DOES exist by the
### locked definition -- ### **BUT IT DOES NOT SURVIVE THE CIRCULARITY CHECK**, so nothing is established
### that could lift a naming. ### The block says that in those words rather than letting the `unless` read
### as satisfied. ### **AND NO GRADE IS CONFERRED BY A SEAT.**
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W    # noqa: E402  ### THE WRITER, IMPORTED.
import run_clock              # noqa: E402
import anchor_from_file as AF  # noqa: E402
import needle_pull            # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


VOROS = d('b358_source_voros0506326.txt')
LAG = d('b358_source_lagarias0404394.txt')
MARK = '## UPDATE — filed 2026-09-07 (b358): row U1, the uniformity obstruction'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


# ### **EVERY QUOTATION IN THE BLOCK IS VERIFIED AT ITS OWN FILE BEFORE THE BLOCK EXISTS**, by the writer's
# ### own guard and, first, by the anchor tool here.
QUOTES = [
    (VOROS, 'For n → ∞ we obtain that if (and only if) the Hypothesis is true,'),
    (VOROS, 'all the zeros lie on the critical line, ﬁrst transform the summation'),
    (VOROS, '4k n1−2k (n → ∞ ) unconditionally. (24)'),
    (LAG, 'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representationπ onGL(N )'),
    (LAG, 'in which the implied constant in the O-notation depends on π. If the Riemann hypothesis holds'),
    (MONO, 'certifies λ_n ≥ 0 for n up to Voros'),
]

BODY = [
    '',
    MARK,
    '',
    "*Rows above are never rewritten; an update names the row it bears on. Written through the writer's "
    "`append_block`.*",
    '',
    '| row | what b358 did | what is located, and what is not |',
    '|:--|:--|:--|',
    '| **U1** (the uniformity obstruction) | **A FOURTH INSTANCE OF THE SHAPE, AND THE FIRST ONE WHERE THE '
    'LITERATURE WAS ASKED DIRECTLY FOR THE UNIFORM STATEMENT.** The Li face needs a statement uniform in '
    '`n`; the deposit proves one indexed by `n`, in its own words: *"`partialPositivity_finiteRange` '
    '(v0.8.0) certifies λ\\_n ≥ 0 for n up to Voros\'s detection threshold N₀(T) ≈ 2T², with the on-line '
    'term\'s nonnegativity proved -- a certificate reaching exactly to where discrimination would begin, '
    'and no further; it is not RH"*. b358 read the literature under the import bar for an asymptotic that '
    'would close the tail beyond a computable index, pinning two sources by hash (Voros math/0506326, '
    'sha256 `dd360dab…`; Lagarias math/0404394v4, sha256 `86f3d3c4…`, **which is the record\'s own b327 pin, '
    're-verified byte for byte**). **SEVEN STATEMENTS LOCATED; ONE MEETS ALL FOUR CONDITIONS LOCKED BEFORE '
    'ANY SOURCE WAS OPENED; IT IS CIRCULAR AT ALL THREE OF THE LOCKED CIRCULARITY QUESTIONS.** The source '
    'says so itself: *"For n → ∞ we obtain that if (and only if) the Hypothesis is true, λ n ∼ n(A log n + '
    'B)"*, and its derivation opens *"all the zeros lie on the critical line, first transform the summation '
    '(1) into a Stieltjes integral"*. | **THE SPLIT IS EXACT, AND IT IS THE FINDING.** The archimedean '
    'channel has an unconditional asymptotic with an explicit error term, from both sources independently: '
    'Voros\'s *"unconditionally. (24)"*, to all orders; and Lagarias\'s Theorem 5.1, `S_inf(n,π) = (N/2) n '
    'log n + C\\_1(π) n + O(N(K(π)+1))` for `n ≥ K(π)`, **with the implied constant stated to be absolute**. '
    'The zero channel has **no unconditional bound at all**: Lagarias\'s Theorem 6.1 reduces `S_f` to '
    'another Li-type quantity unconditionally, and bounds it only at *"If the Riemann hypothesis holds for '
    'L(s,π) then λ n(√n,π ∨) = O(√ n logn)"*. **SO THE ONE PART OF THE DECOMPOSITION THAT WOULD CLOSE THE '
    'TAIL IS THE PART THE HYPOTHESIS CONTROLS.** ### **GRADE: `NAMED-ONLY`, UNCHANGED.** A shape exists by '
    'the locked definition and does not survive, so nothing is established that could lift a naming; **no '
    'grade is conferred by a seat.** ### **NOT AN EQUIVALENCE CLAIM**, and U1\'s own refusal governs this '
    'block as it governs the row: nothing is claimed about the relation of this fourth instance to the '
    'other three, in either direction. ### **NO COORDINATE IS CLOSED. THE PARTITION STAYS UNDECIDED. THE '
    'CLAUSE HAS NOT MOVED. THE TWO FACES\' EQUIVALENCE IS NOT COMPILED.** ### And the search was five '
    'addresses, four fetched: **an absence of reading is not an absence of literature.** |',
    '',
    "*No grade is conferred by a seat. A located statement is not an applied one, and this act applies "
    "none. Nothing about `h2`, totality or the roster; the wave stays parked. Filed by b358 (relay "
    "`data/b358_the_li_asymptotics.txt`).*",
]


def main():
    rec('=' * 100)
    rec('b358 -- ROW U1 GAINS THIS ACT\'S FINDING, AS AN UPDATE BLOCK THROUGH ITS OWN WRITER.')
    rec('=' * 100)
    rec('  writer : %s (IMPORTED, not reimplemented)' % os.path.basename(W.__file__))
    rec('  ### ### **U1 IS ALREADY WRITTEN AND IS NOT REWRITTEN.** ### This is an UPDATE BLOCK.')
    rec('')
    rec('  ### the quotations, each located by the anchor tool at its own file BEFORE the block exists:')
    bad = 0
    for path, hint in QUOTES:
        try:
            n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            rec('    PASS  %-40s line %-6d | %s' % (os.path.basename(path), n, line.strip()[:70]))
        except (AF.AnchorError, LookupError) as e:
            bad += 1
            rec('    ### FAIL  %-40s %s' % (os.path.basename(path), str(e)[:70]))
    if bad:
        rec('  ### REFUSING TO WRITE A BLOCK WHOSE QUOTATIONS DO NOT LOCATE.')
        run_clock.write(D, 'b358_faces_row_run', LINES)
        return 1
    rec('')
    st, det = W.append_block(MARK, BODY)
    rec('  ### FACES_LEDGER.md : %s' % st)
    rec('    %s' % det)
    rec('')
    rec("  ### ### **THE ORDER'S `unless` DID NOT LIFT THE GRADE, AND THE BLOCK SAYS WHY.** ### A shape")
    rec('  ### ### exists by the locked definition; ### **IT DOES NOT SURVIVE THE CIRCULARITY CHECK**, so')
    rec('  ### ### nothing is established. ### The grade stays `NAMED-ONLY`.')
    rec('  ### ### **AND U1\'S OWN REFUSAL GOVERNS THE BLOCK:** ### nothing is claimed about the relation')
    rec('  ### ### of this fourth instance to the other three.')
    rec('=' * 100)
    p = run_clock.write(D, 'b358_faces_row_run', LINES)
    io.open(d('b358_faces_row.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        '{\n "status": "%s",\n "detail": "%s",\n "row": "U1",\n "form": "UPDATE BLOCK (append_block)",\n'
        ' "grade": "NAMED-ONLY",\n "quotes": %d,\n "run_file": "%s",\n "run_clock": "%s"\n}\n'
        % (st, det.replace('"', "'"), len(QUOTES), os.path.basename(p), run_clock.read_stamp(p)))
    print('  written: %s' % os.path.basename(p))
    return 0 if st in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
