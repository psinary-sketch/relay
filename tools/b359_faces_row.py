# -*- coding: utf-8 -*-
"""b359_faces_row.py -- ROW U1 GAINS b358's FINDING, THROUGH ITS OWN WRITER.

### ### **THE WRITER IS `b327_faces_row.py`, IMPORTED AND NOT REIMPLEMENTED.** ### `U1` is written and
### ### **ROWS ABOVE ARE NEVER REWRITTEN** ### -- the ledger's own law -- so this is an ### **UPDATE
### ### BLOCK** ### through `append_block`, naming the row it bears on.
### ### **THE ORDER'S OWN WORDS FOR WHAT THE ROW GAINS:** ### *"the countable face's tail bound exists and
### asserts the hypothesis; the conditionality localized to the zero channel while the archimedean channel
### is unconditional with an explicit error term; the index distance recorded as measured -- NAMED-ONLY,
### nothing compiled, the deposit's refusal quoted as the row already quotes it."*
### ### **AND b358'S BLOCK ALREADY CARRIES THE READING.** ### This one carries what the order asked to be
### ### **LOCALIZED AND RECORDED**, and says plainly that it adds no new reading: the figures are b358's,
### quoted from b358's bank at their lines.
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


BANK358 = d('b358_the_li_asymptotics.txt')
MARK = '## UPDATE — filed 2026-09-07 (b359): row U1, the uniformity obstruction — the tail bound localized'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


QUOTES = [
    (BANK358, 'THE ARCHIMEDEAN HALF IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY'),
    (BANK358, 'THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL'),
    (BANK358, 'THE RATIO, ONE LABELLED DIVISION OF TWO BANKED COUNTS'),
    (BANK358, 'THE ONE PART OF THE DECOMPOSITION THAT WOULD CLOSE THE'),
    (MONO, 'not** compiling the cross-register equivalences'),
]

BODY = [
    '',
    MARK,
    '',
    "*Rows above are never rewritten; an update names the row it bears on. Written through the writer's "
    "`append_block`.*",
    '',
    '| row | what b359 records | what is localized, and what is not |',
    '|:--|:--|:--|',
    '| **U1** (the uniformity obstruction) | **THE COUNTABLE FACE\'S TAIL BOUND EXISTS, AND IT ASSERTS THE '
    'HYPOTHESIS.** b358 located it and pinned it; this block records where the conditionality SITS, which '
    'is the part a later reader needs and which a verdict word alone does not carry. **THE CONDITIONALITY '
    'IS LOCALIZED TO THE ZERO CHANNEL.** On the decomposition the record already holds, `λ\\_n = S\\_∞(n) − '
    'S\\_f(n) + 1` (b327, from the pinned source), b358 found that **the archimedean channel is '
    'unconditional WITH AN EXPLICIT ERROR TERM, from two sources independently** — *"THE ARCHIMEDEAN HALF '
    'IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY"* — Voros\'s (24) carrying the word '
    '*unconditionally* on its own line and holding *to all orders*, and Lagarias\'s Theorem 5.1 giving '
    '`O(N(K(π)+1))` for `n ≥ K(π)` **with the implied constant stated to be ABSOLUTE**. Against that, '
    '*"THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL"*: Theorem 6.1 reduces `S\\_f` to another Li-type '
    'quantity unconditionally and bounds it only under the Riemann hypothesis for `L(s,π)`. **THE INDEX '
    'DISTANCE, RECORDED AS MEASURED AND NOT AS A PRICE:** the corpus has computed its channels to `n = '
    '300` and a violating zero could first register at about `n = 1e+18` (Voros\'s threshold, which the '
    'deposit repeats), *"THE RATIO, ONE LABELLED DIVISION OF TWO BANKED COUNTS"* giving `3.33e+15`. | '
    '**GRADE: `NAMED-ONLY`, UNCHANGED.** b358\'s shape does not survive its own circularity check, so '
    'nothing is established that could lift a naming, and **no grade is conferred by a seat.** ### **THE '
    'DISTANCE IS A DISTANCE IN INDEX AND NOTHING ELSE** — not a price in wall time, memory or precision, '
    'because the record prints no cost per index for this channel. ### **NOTHING IS COMPILED, AND U1\'S '
    'OWN REFUSAL GOVERNS THIS BLOCK AS IT GOVERNS THE ROW:** the deposit compiles the register structure '
    '*"while deliberately **not** compiling the cross-register equivalences, since to compile \\"discharge '
    'one and you discharge all five\\" would be to compile RH-equivalence itself"*, and **nothing is '
    'claimed here about the relation of this instance to the other three, in either direction.** ### **NO '
    'NEW READING IS ADDED BY THIS BLOCK.** Every figure and every quotation above is b358\'s, quoted from '
    'b358\'s bank at its own line; what b359 adds is the LOCALIZATION, on the author\'s order. ### **NO '
    'COORDINATE IS CLOSED. THE PARTITION STAYS UNDECIDED. THE CLAUSE HAS NOT MOVED. NO ACT IS '
    'RE-VERDICTED.** |',
    '',
    "*No grade is conferred by a seat. A located statement is not an applied one. Nothing about `h2`, "
    "totality or the roster; the wave stays parked. Filed by b359 (relay `data/b359_the_currency_pass.txt`; "
    "the reading is b358's, relay `data/b358_the_li_asymptotics.txt`).*",
]


def main():
    rec('=' * 100)
    rec("b359 -- ROW U1 GAINS b358'S FINDING, LOCALIZED, AS AN UPDATE BLOCK THROUGH ITS OWN WRITER.")
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
            rec('    PASS  %-34s line %-6d | %s' % (os.path.basename(path), n, line.strip()[:66]))
        except (AF.AnchorError, LookupError) as e:
            bad += 1
            rec('    ### FAIL  %-34s %s' % (os.path.basename(path), str(e)[:70]))
    if bad:
        rec('  ### REFUSING TO WRITE A BLOCK WHOSE QUOTATIONS DO NOT LOCATE.')
        run_clock.write(D, 'b359_faces_row_run', LINES)
        return 1
    rec('')
    st, det = W.append_block(MARK, BODY)
    rec('  ### FACES_LEDGER.md : %s' % st)
    rec('    %s' % det)
    rec('')
    rec('  ### ### **WHAT THIS BLOCK ADDS AND WHAT IT DOES NOT.** ### It adds the LOCALIZATION the order')
    rec('  ### ### asked for -- WHERE the conditionality sits -- and the index distance as a measured')
    rec('  ### ### number. ### **IT ADDS NO NEW READING:** every figure is b358\'s, quoted at its line.')
    rec('  ### ### **THE GRADE STAYS `NAMED-ONLY` AND NOTHING IS COMPILED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b359_faces_row_run', LINES)
    io.open(d('b359_faces_row.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        '{\n "status": "%s",\n "detail": "%s",\n "row": "U1",\n "form": "UPDATE BLOCK (append_block)",\n'
        ' "grade": "NAMED-ONLY",\n "quotes": %d,\n "run_file": "%s",\n "run_clock": "%s"\n}\n'
        % (st, det.replace('"', "'"), len(QUOTES), os.path.basename(p), run_clock.read_stamp(p)))
    print('  written: %s' % os.path.basename(p))
    return 0 if st in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
