# -*- coding: utf-8 -*-
"""b308_correspondence.py -- TWO ROWS: THE INSTRUMENT BUILT, AND THE ARTIFACT RETIRED FOR IT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED** -- from
### `b303_correspondence.py` and `b302_correspondence.py`. ### **AND THIS ACT NEEDED THE GUARD MORE
### THAN ITS ANCESTORS DID:** ### its whole subject is a radius written as an absolute value, and
### the absolute-value bars are the character a markdown table reads as a column break. ### The rows
### below say ### **"absolute value at most `p^e`"** ### in words for exactly that reason, and the
### guard checks it BEFORE anything is written rather than after.

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE RECORDS AN INSTRUMENT, AND AN INSTRUMENT IN A TABLE OF RESULTS READS AS A
###     RESULT.** ### It is not one. ### **EVERY NUMBER IT PRINTS IS A BANKED NUMBER RECOMPUTED OR A
###     CONTROL**, and the grade cell says so before it says anything else.
###   ### **ROW TWO RECORDS A RETIREMENT, AND A RETIREMENT READS AS A GENERAL ONE.** ### It is not:
###     ### **THE ARTIFACT IS RETIRED FOR ONE INSTRUMENT AND FOR NOTHING ELSE**, and the row names
###     what it does not retire in the same sentence.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402  ### the blank-cell audit, READ not copied
import b303_correspondence as G   # noqa: E402  ### the notation guard, READ not copied

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE LOCAL-FIELD INSTRUMENT, ACT ONE (b308)",

     "THE LOCAL-FIELD INSTRUMENT, ACT ONE (b308): the corpus's finite model ties two radii to one "
     "level index — b21's `V_n` is `p^(-n)Z_p / p^n Z_p = Z/p^(2n)`, one `n` governing both the "
     "**support radius** and the **constancy radius**. **THIS ACT UNTIES THEM AND CHANGES NOTHING "
     "ELSE.** A frame is a pair `(r,s)`: support in `p^{-r}Z_p`, constant on cosets of `p^s Z_p`, "
     "b21's chart `x = p^{-r} m`, b21's Haar giving each cell mass `p^{-s}`. **THE MODEL IS THE "
     "POINT `r = s = n` AND THE INSTRUMENT IS THE PLANE.** The consequence is the whole point: the "
     "transform carries `(r,s)` to `(s,r)`, and the scaling part of the multiplicative group acts as "
     "`theta(p^k) : V(r,s) → V(r−k, s+k)` — **BOTH RADII MOVE, THEIR SUM DOES NOT, AND ON CHART "
     "INDICES THE MAP IS THE IDENTITY.** That is the direction the model drops.",

     "**NO TERMINAL. AN INSTRUMENT IS NOT A STATEMENT.** `tools/b308_local_field.py` (the frame, the "
     "transform, the two conditions, the dilation, the exposure arm) and "
     "`tools/b308_reproduction.py` (the components). Exact `Fraction`, `int` and cyclotomic "
     "reduction; **zero float tokens in any deciding path.** Every operation carries a positive "
     "control in **both polarities before it is used**: b21's geometric-sum identity verified over "
     "**every** residue at seven frames before the inversion runs on it; the collapse of the second "
     "condition checked against the literal condition in the cyclotomic field, both directions, with "
     "a non-member spike rejected by **both**; an off-ball spike moved by the projection at every "
     "cell.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** — the profile stands unchanged at 470, 0 `.lean` files "
     "touched. **THE REPRODUCTION, WHICH IS THE GATE ON THE BUILD AND NOT AN APPENDIX TO IT:** the "
     "family recovered as **SET EQUALITY BOTH DIRECTIONS** at every radius pair in range at five "
     "cells, 0 disagreeing; the dimension law and the keystone's own `(p^n−1)^2` at the diagonal, 0 "
     "disagreeing; `Tr(Pi)` equal to the constrained dimension at six cells (1, 9, 4, 64, 16, 36); "
     "the compact-part smear zero at all six **with its mechanism re-derived on the instrument's own "
     "shells**; the annihilation criterion at **80 members reached, 0 disagreeing, 50 forced zeros "
     "confirmed**, with the form nonzero elsewhere so the zeros are not a dead instrument's; and "
     "b295's two registered witnesses re-valued at their banked `4/3` and `4/7`.",

     "**AN INSTRUMENT BUILT AND CHECKED. ### NOT A RESULT.** All three registered falsifiers **DID "
     "NOT FIRE**. **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: EVERY NUMBER HERE IS A BANKED "
     "NUMBER RECOMPUTED OR A CONTROL, AND TWO INSTRUMENTS AGREEING IS A CHECK ON THE INSTRUMENTS, "
     "NOT A PROMOTION OF ANY RESULT.** No grade moves; no act is re-verdicted; no new mathematics; "
     "**no first-level value is computed at any cell or member the record does not already carry** — "
     "that is a later act under its own registration, and what it may compute is named in the bank "
     "and left uncomputed. **UNTYING THE RADII REMOVES THE WRAPAROUND; IT DOES NOT REMOVE THE "
     "TRUNCATION.** One difference the reproduction found is filed as a note and not a correction. "
     "**NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the "
     "deposit left it.**",

     "current"),

    ("THE ESCAPED-MASS ARTIFACT, RETIRED FOR ONE INSTRUMENT (b308)",

     "THE ESCAPED-MASS ARTIFACT, RETIRED FOR ONE INSTRUMENT (b308): b21 named it — *`U` maps `V_n` "
     "INTO `V_(n+1)` and ESCAPES `V_n`* — and *THE MODEL'S mod-N WRAPAROUND IS EXACTLY THIS ESCAPED "
     "MASS FOLDED BACK IN*. b284 met it and wrote *THE DERIVATION STANDS BECAUSE IT IS ON `Q_p`, "
     "WHERE THERE IS NOTHING TO FOLD.* **THIS ACT MAKES THAT SENTENCE A COUNT.** The model must read "
     "`theta(p^k) f` back in the frame it left, which on chart indices is `m → p^k m mod N`; the "
     "instrument moves the frame instead, and on chart indices that is the identity. **THE MODEL'S "
     "COLLIDED ORDERED PAIRS ARE `N(p^k − 1)`, NONZERO AT EVERY CELL AND EVERY DIRECTION TESTED, BY "
     "TWO ROUTES. ### THE INSTRUMENT'S ARE ZERO, BY THE SAME TWO ROUTES.**",

     "**NO TERMINAL. A COUNT IS NOT A COMPILE**, and this one is finite-decidable at a cell while "
     "the sentence it supports is not. The escaped mass itself is exhibited on a vector of the "
     "object's own space: b21's `U` sends it to `V(n+1, n−1)`, its smallest containing ball is "
     "`p^{-(n+1)}Z_p` at every cell — **b21's own support law, recomputed** — and the escaped Haar "
     "mass is an exact nonzero rational at every cell. b21's *unitary on L^2(Q_p)* is checked as an "
     "identity of rationals: the normalizing scalar comes out **exactly 1**.",

     "**NO PRINT.** The exposure arm scans call paths for a **non-unit pushforward site** — a line "
     "reducing the product of a grid index with a power of the residue characteristic modulo the "
     "grid size. **THIS ACT'S OWN TWO FILES: 5 SITES, ALL DECLARED CARRIERS (two exhibit the model's "
     "collapse so it can be counted, two are the arm's own control strings, one is prose quoting a "
     "line in order to rule on it), AND 0 UNDECLARED SITES IN THE INSTRUMENT'S OPERATIONAL PATH.** "
     "In the owners: `b303_family`, `b304_smearing`, `b293_finite_family`, `b295_second_mechanism` "
     "and `b294_family_value` at 0; `b281_compression` at 2 and `b270_ambient_pairing` at 4, each "
     "ruled and each reason printed.",

     "**RETIRED FOR THIS INSTRUMENT, AND FOR NOTHING ELSE.** **SCOPE, AND THE ROW STATES IT IN THE "
     "SAME BREATH AS THE RETIREMENT: IT IS NOT RETIRED FOR THE MODEL** — the model's column is "
     "nonzero everywhere and any later act scaling on `Z/p^{2n}` meets it again — **NOR FOR b284**, "
     "whose exposure is declared, stands, and is not re-verdicted here. It retires neither "
     "`W-ORD-FIBER-GENERAL`, nor the barrier's scope limit, nor the range law, nor the truncation. "
     "**AND THE ARM'S LIMIT IS PART OF THE ROW: IT FINDS A SHAPE AND CANNOT TELL A REGROUPING OF AN "
     "EXACT FINITE SUM FROM A REPRESENTATION OF A FUNCTION THAT LEFT ITS LEVEL** — that judgement is "
     "this seat's, is stated as this seat's, and no tool made it. **NO AGGREGATION IS STATED. M-2 "
     "REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.**",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b308 -- THE INSTRUMENT\'S ROW, AND THE ARTIFACT\'S.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    print('  ### **AND THIS ACT IS THE ONE MOST LIKELY TO CARRY ONE**: its subject is a radius')
    print('  ### written as an absolute value, and the rows say so IN WORDS for that reason.')
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    # ### THE ROW-SPECIFIC GATES. ### **EACH ROW MUST CARRY THE REFUSAL ITS OWN HAZARD NEEDS.**
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('NOT A RESULT' in r1[4] and 'NO TERMINAL' in r1[2] and 'NO PRINT' in r1[3]
          and 'A CONTROL' in r1[4])
    g2 = ('FOR NOTHING ELSE' in r2[4] and 'NOT RETIRED FOR THE MODEL' in r2[4]
          and 'NO TERMINAL' in r2[2])
    print('  row 1 declares no terminal/print and refuses to be read as a result : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 bounds the retirement it records, in the same cell : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
