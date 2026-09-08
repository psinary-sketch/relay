# -*- coding: utf-8 -*-
"""b361_faces_row.py -- ROW U1 GAINS THE INDEX CONDITION, DECIDED, THROUGH ITS OWN WRITER.

### ### **THE WRITER IS `b327_faces_row.py`, IMPORTED AND NOT REIMPLEMENTED.** ### `U1` is written and
### ### **ROWS ABOVE ARE NEVER REWRITTEN** ### -- the ledger's own law -- so this is an ### **UPDATE
### ### BLOCK** ### through `append_block`, naming the row it bears on.
### ### **AND IT IS WRITTEN ONLY BECAUSE THE DECISION MOVED THE ROW**, which the order made the condition:
### *"the Li row updated through the ledger's writer if and only if the decision moves it."* ### The row
### said the archimedean bound holds for `n >= K(pi)`; after this act the record holds that the condition
### is VACUOUS for the corpus's object and the error term is a constant. ### **THAT IS NEW TO THE ROW.**
### ### **WHAT IT IS NOT:** ### no grade is conferred, nothing is compiled, no bridge is typed, and the
### tail stands exactly where `b358` left it.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W     # noqa: E402  ### THE WRITER, IMPORTED.
import run_clock               # noqa: E402
import anchor_from_file as AF  # noqa: E402
import needle_pull             # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


BANK358 = d('b358_the_li_asymptotics.txt')
SRC = d('b358_source_lagarias0404394.txt')
MARK = ('## UPDATE \u2014 filed 2026-09-07 (b361): row U1, the uniformity obstruction \u2014 '
        'the index condition decided')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


QUOTES = [
    (BANK358, 'THE RECORD ALREADY HOLDS. ### DETERMINED IS NOT COMPUTED**, the cap forbids this act'),
    (BANK358, '`H-CUSP` (`\u03c0` cuspidal on `GL(N)`): the corpus'),
    (SRC, 'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    (SRC, 'the quantities S\u221e(n,\u03c0 ) are real-valued. There is a constant K(\u03c0) such that for n'),
    (SRC, 'and the implied constant in the O-notation is absolute.'),
    (SRC, 'using Q(\u03c0triv) = 1.'),
    (SRC, '\u039b(s,\u03c0 triv ) = \u03c0\u2212 s'),
    (SRC, 'that for all n \u2265 1,'),
    (SRC, 'and the implied constant in the O(1) term depends on \u03c0. Here'),
    (MONO, 'not** compiling the cross-register equivalences'),
]

BODY = [
    '',
    MARK,
    '',
    "*Rows above are never rewritten; an update names the row it bears on. Written through the writer's "
    "`append_block`.*",
    '',
    '| row | what b361 decides | what it does not decide |',
    '|:--|:--|:--|',
    '| **U1** (the uniformity obstruction) | **THE INDEX CONDITION ON THE ARCHIMEDEAN CHANNEL IS VACUOUS '
    'FOR THE CORPUS\u2019S OBJECT.** b358 recorded that Lagarias\u2019s Theorem 5.1 gives `O(N(K(\u03c0)+1))` '
    'for `n \u2265 K(\u03c0)` with the implied constant ABSOLUTE, and left `K(\u03c0)` '
    '`UNDECIDABLE-FROM-THE-RECORD` under its own cap \u2014 *"DETERMINED IS NOT COMPUTED, the cap forbids '
    'this act from computing it"*. **b361 DECIDES IT FROM THE SOURCE\u2019S OWN DISPLAYED FORMULAE**, under '
    'the import bar, with the definition located at content in the source b358 pinned: (2.2) the '
    'archimedean factor is a product of `\u0393_R(s + \u03ba_j(\u03c0))`; (2.3) `\u0393_R(s) := '
    '\u03c0^(\u2212s/2) \u0393(s/2)`; (5.3) `K(\u03c0)` is the maximum over `j` of the squared modulus of '
    '`\u03ba_j(\u03c0)`. The source states its own completed L-function for the trivial representation, '
    '`\u039b(s,\u03c0_triv) = \u03c0^(\u2212s/2) \u0393(s/2) \u03b6(s)`, and states its conductor: *"using '
    'Q(\u03c0triv) = 1."* At `N = 1` these force `\u03ba_1(\u03c0_triv) = 0`, hence **`K(\u03c0_triv) = 0`** '
    '\u2014 so the condition reads `n \u2265 0`, is satisfied at every index the corpus computes, and the '
    'error term collapses to `O(1)` with an ABSOLUTE implied constant. **AND WHAT NEITHER SEAT HAD PUT SIDE '
    'BY SIDE:** the source\u2019s own introduction already gives the same asymptotic *"that for all n '
    '\u2265 1,"* at (1.12) \u2014 but there *"the implied constant in the O(1) term depends on \u03c0"*. **THE '
    'INDEX CONDITION BELONGS ONLY TO THE ABSOLUTE-CONSTANT VERSION**, and that is the version this row '
    'carries. | **GRADE: `NAMED-ONLY`, UNCHANGED, AND NO GRADE IS CONFERRED BY A SEAT.** A vacuous index '
    'condition establishes nothing that could lift a naming. ### **THE VALUE IS NOT QUOTED FROM THE '
    'SOURCE:** it is an IDENTIFICATION of two of the source\u2019s own displayed formulae, and the source '
    'writes neither `\u03ba_1(\u03c0_triv)` nor `K(\u03c0_triv)` anywhere; b361 prints the route step by '
    'step and prints what the route is deaf to. ### **AND IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT:** '
    'Theorem 5.1 is stated *"For any irreducible cuspidal (unitary) automorphic representation"* and the '
    'trivial representation of `GL(1)` is the one the source itself marks as the exception \u2014 the only '
    'one whose completed L-function is not entire. b358 graded that question `MET` on the corpus axis '
    '(*"the corpus\u2019s object is \u03b6, the N = 1, Q = 1 case"*) and **this act stands on that grade and '
    'confers none; if `H-CUSP` moved, this decision would move with it.** ### **THE TAIL IS UNTOUCHED AND '
    'THE CIRCULARITY FINDING STANDS:** the tail is closed by the ZERO channel, which has no unconditional '
    'bound at all, and nothing here changes that. ### **NOTHING IS COMPILED, AND U1\u2019S OWN REFUSAL '
    'GOVERNS THIS BLOCK AS IT GOVERNS THE ROW:** the deposit compiles the register structure *"while '
    'deliberately **not** compiling the cross-register equivalences, since to compile \\"'
    'discharge one and you discharge all five\\" would be to compile RH-equivalence itself"*, and **nothing '
    'is claimed here about the relation of this instance to the other three, in either direction.** ### **NO '
    'COORDINATE IS CLOSED. THE PARTITION STAYS UNDECIDED. THE CLAUSE HAS NOT MOVED. NO ACT IS '
    'RE-VERDICTED.** |',
    '',
    "*No grade is conferred by a seat. A decided index condition is not a closed tail. Nothing about `h2`, "
    "totality or the roster; the instrument lane and the wave stay parked. Filed by b361 (relay "
    "`data/b361_the_held_item.txt`; the reading at `data/b361_read5.txt`; the source pinned at b358, "
    "`data/b358_source_lagarias0404394.txt`).*",
]


def main():
    rec('=' * 100)
    rec('b361 -- ROW U1 GAINS THE INDEX CONDITION, DECIDED, AS AN UPDATE BLOCK THROUGH ITS OWN WRITER.')
    rec('=' * 100)
    rec('  writer : %s (IMPORTED, not reimplemented)' % os.path.basename(W.__file__))
    rec('  ### ### **U1 IS ALREADY WRITTEN AND IS NOT REWRITTEN.** ### This is an UPDATE BLOCK.')
    rec('  ### ### **AND IT IS WRITTEN ONLY BECAUSE THE DECISION MOVED THE ROW**, which is the order\'s')
    rec('  ### ### own condition.')
    rec('')
    rec('  ### the quotations, each located by the anchor tool at its own file BEFORE the block exists:')
    bad = 0
    for path, hint in QUOTES:
        try:
            n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            rec('    PASS  %-34s line %-6d | %s' % (os.path.basename(path), n, line.strip()[:66]))
        except (AF.AnchorError, LookupError) as e:
            bad += 1
            rec('    ### FAIL  %-34s %s' % (os.path.basename(path), str(e)[:70]))
    if bad:
        rec('  ### REFUSING TO WRITE A BLOCK WHOSE QUOTATIONS DO NOT LOCATE.')
        run_clock.write(D, 'b361_faces_row_run', LINES)
        return 1
    rec('')
    st, det = W.append_block(MARK, BODY)
    rec('  ### FACES_LEDGER.md : %s' % st)
    rec('    %s' % det)
    rec('')
    rec('  ### ### **WHAT THIS BLOCK ADDS:** ### that the index condition on the archimedean channel is')
    rec('  ### ### VACUOUS for the corpus\'s object, that the error term is therefore a constant with an')
    rec('  ### ### ABSOLUTE implied constant, and that the source always held a second statement without')
    rec('  ### ### the condition and with a weaker constant.')
    rec('  ### ### **WHAT IT DOES NOT ADD:** ### no grade, no compilation, no bridge, and nothing about')
    rec('  ### ### the tail, which is closed by a channel with no unconditional bound at all.')
    rec('=' * 100)
    p = run_clock.write(D, 'b361_faces_row_run', LINES)
    io.open(d('b361_faces_row.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        '{\n "status": "%s",\n "detail": "%s",\n "row": "U1",\n "form": "UPDATE BLOCK (append_block)",\n'
        ' "grade": "NAMED-ONLY, UNCHANGED",\n "quotes": %d,\n "run_file": "%s",\n "run_clock": "%s"\n}\n'
        % (st, det.replace('"', "'"), len(QUOTES), os.path.basename(p), run_clock.read_stamp(p)))
    print('  written: %s' % os.path.basename(p))
    return 0 if st in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
