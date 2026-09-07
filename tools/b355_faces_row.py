# -*- coding: utf-8 -*-
"""b355_faces_row.py -- ONE NEW FACES-LEDGER ROW, THROUGH ITS OWN WRITER.

### ### **THE WRITER IS `b327_faces_row.py`, IMPORTED AND NOT REIMPLEMENTED.** ### It refuses duplicates,
### guards notation, ### **VERIFIES EVERY QUOTATION AGAINST THE FILE THAT EMITS IT** ### before a line
### exists, and reads back after the write.
### ### **THE ROW: THE UNIFORMITY OBSTRUCTION** -- the shape common to the clause's quantifier, the height
### coordinate's enumeration, and the width coordinate's union.
### ### ### **AND NOTHING IS CLAIMED ABOUT THEIR EQUIVALENCE.** ### The deposit's own refusal to compile
### cross-register equivalence governs and is QUOTED IN THE ROW, because a ledger row naming three things
### that look alike is exactly where an equivalence would get compiled by accident.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W    # noqa: E402  ### THE WRITER, IMPORTED.
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


ROW = dict(
    id='U1',
    cells=[
        'U1 -- the uniformity obstruction: three places where the record needs a statement UNIFORM in an index and holds statements indexed by it',
        'not a register; a SHAPE observed across three faces, and named as one',
        'INTERNAL -- three acts, each quoted from its own emitting file: `data/b332_the_clause_stated.txt` (the quantifier), `data/b351_the_partition_question.txt` (the height), `data/b353_the_missing_statement.txt` (the width)',
        'NAMED-ONLY, and the three instances MEASURED by their own acts. ### **(i) THE CLAUSE\'S QUANTIFIER**, b332: *"the quantifiers -- over the class, infinite, and through the explicit formula over the zeros -- are UNOWNED, and they are the clause."* ### **(ii) THE HEIGHT COORDINATE\'S ENUMERATION**, b351: the record\'s only method there produces INSTANCES, and *"Running the census higher buys more instances"* while a class is not made of instances; the coordinate is BOUNDED BY A MEASUREMENT and not by an argument. ### **(iii) THE WIDTH COORDINATE\'S UNION**, b353: Boas-Kac exhausts the admissible class AT a support and *"AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS"*, while the criterion quantifies over the union of all supports. ### **THE SHAPE, NAMED AND NOT PROVED: in each, what the record holds is a family indexed by something, and what it needs is one statement uniform in that index.**',
        'CORRESPONDENCE.md rows 178 (b332), 199 (b351), 201 (b353)',
        'NONE TYPED, AND THE REFUSAL IS THE POINT. ### **NOTHING IS CLAIMED ABOUT THE EQUIVALENCE OF THE THREE**, and the deposit\'s own law governs: the register pentagon compiles the structure *"while deliberately **not** compiling the cross-register equivalences, since to compile \\"discharge one and you discharge all five\\" would be to compile RH-equivalence itself"*. ### **A ROW NAMING THREE THINGS THAT LOOK ALIKE IS EXACTLY WHERE AN EQUIVALENCE GETS COMPILED BY ACCIDENT**, so this row names a resemblance of SHAPE and types no bridge between the three, in either direction. ### Three separate obstructions that rhyme are three obstructions.',
    ],
    quotes=[
        (d('b332_the_clause_stated.txt'), 'the quantifiers -- over the class, infinite, and through the explicit formula over', False),
        (d('b351_the_partition_question.txt'), 'HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT MADE OF INSTANCES', False),
        (d('b353_the_missing_statement.txt'), 'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS', False),
        (MONO, 'not** compiling the cross-register equivalences', False),
    ])


def main():
    rec('=' * 100)
    rec('b355 -- ONE FACES-LEDGER ROW, THROUGH ITS OWN WRITER. ### THE UNIFORMITY OBSTRUCTION.')
    rec('=' * 100)
    rec('  writer : %s (IMPORTED, not reimplemented)' % os.path.basename(W.__file__))
    rec('  ### ### **THE WRITER VERIFIES EVERY QUOTATION AGAINST ITS EMITTER BEFORE A LINE EXISTS.**')
    rec('  quotations to verify : %d' % len(ROW['quotes']))
    for f, frag, flat in ROW['quotes']:
        rec('    %-46s | %s' % (os.path.basename(f), frag[:66]))
    rec('')
    st, det = W.write_row(ROW)
    rec('  ### FACES_LEDGER.md : %s' % st)
    rec('    %s' % det)
    rec('')
    rec('  ### ### **WHAT THIS ROW DOES NOT DO, AND THE ROW SAYS IT IN ITS OWN LAST CELL:**')
    rec('  ### ### **IT CLAIMS NOTHING ABOUT THE EQUIVALENCE OF THE THREE.** ### The deposit refuses to')
    rec('  ### ### compile cross-register equivalence, and the refusal is quoted IN the row rather than')
    rec('  ### ### remembered around it. ### **THREE SEPARATE OBSTRUCTIONS THAT RHYME ARE THREE**')
    rec('  ### ### **OBSTRUCTIONS.**')
    rec('  ### ### **AND THE GRADE IS `NAMED-ONLY`.** ### The shape is named by this act; the three')
    rec('  ### ### instances are MEASURED by their own acts and keep their own grades.')
    rec('=' * 100)
    p = run_clock.write(D, 'b355_faces_row_run', LINES)
    io.open(d('b355_faces_row.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        '{\n "status": "%s",\n "detail": "%s",\n "id": "U1",\n "quotes": %d,\n "run_file": "%s",\n "run_clock": "%s"\n}\n'
        % (st, det.replace('"', "'"), len(ROW['quotes']), os.path.basename(p), run_clock.read_stamp(p)))
    print('  written: %s' % os.path.basename(p))
    return 0 if st in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
