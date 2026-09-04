# -*- coding: utf-8 -*-
"""b324_correspondence.py -- TWO ROWS: THE WALL, AND THE MARGIN.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### ### **ROW ONE SAYS THE ARC'S SPACE AND THE KEYSTONE'S WALL ARE DIFFERENT OBJECTS, AND
###     ### THAT READS AS THE ARC DEMOTED.** ### It is not. ### The arc never claimed to have built
###     the Hilbert-Polya object and said at every step that no theorem was proved. ### **THE ARC'S
###     ### OWN SCOPE SENTENCES AND THIS VERDICT AGREE EXACTLY**, and the row must say so.
###   ### ### **ROW TWO SAYS A BRIDGE IS OWED, AND THAT READS AS AN OVERSIGHT FOUND.** ### The deposit
###     records that it withholds the cross-register equivalences ### DELIBERATELY ### , because
###     compiling them would be compiling RH-equivalence. ### **THE BRIDGE IS ABSENT BY DESIGN, NOT
###     ### BY OVERSIGHT**, and a row that reported it as an oversight would be misreading the
###     deposit in the deposit's own favour's opposite direction.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE WALL: THE KEYSTONE'S SPACE AND THE ARC'S ARE DIFFERENT OBJECTS, AT SEVEN OF SEVEN (b324)",

     "THE WALL: THE KEYSTONE'S SPACE AND THE ARC'S ARE DIFFERENT OBJECTS, AT SEVEN OF SEVEN "
     "(b324): the residue keystone's object is **the positive space on the zeros** -- *\"positivity "
     "has no zeros, the operator has no space, and the space is exactly what neither supplies. The "
     "space is the wall.\"* Its defining requirement is that a self-adjoint operator's spectrum "
     "REALIZE the zeta-zeros. The arc's constructed space is Connes-Consani's `S(1,1)`: two "
     "homogeneous vanishing conditions on a function and its transform, **with no operator and no "
     "zeros in the definition at all**. Walked in the sealed link order they differ at the FIRST "
     "constituent -- the ambient -- and at every one after it. **VERDICT: DIFFERENT, seven of "
     "seven. (F1) IS REFUTED and both its halves fall**; the second does not even arise, since an "
     "arc that did not build the keystone's object cannot have moved the wall that object IS.",

     "**NO TERMINAL, AND THE VERDICT RESTS ON NO SHARED WORD.** The order refused resemblance BY "
     "NAME -- \"space\", \"wall\", \"margin\", \"room\", \"silence\" -- and the registration "
     "supplied the operational test: *if the argument would survive replacing one side's technical "
     "term with a synonym the other side does not use, it was a resemblance argument.* **BOTH "
     "RECORDS WRITE \"SPACE\"; THE VERDICT DOES NOT REST ON IT.** It rests on seven constituents, "
     "of which the decisive one is that one space is defined by a spectrum realizing the zeros and "
     "the other by two vanishing conditions.",

     "**AND THE KEYSTONE HAD ALREADY PLACED THE ARC'S SOURCE**, which is sharper than the verdict: "
     "its realization-candidate map grades *\"Connes-Consani (reduces RH to a Weil positivity left "
     "open)\"* among the routes that **stall at the realization clause**. The arc built an "
     "instrument INSIDE a source the keystone had already put on the near side of the wall, and "
     "that grading stands unchanged. **A PROVENANCE FINDING RIDES WITH IT AND IS MEASURED, NOT "
     "ASSUMED: \"the space is the wall\", \"the positive space\" and \"Sonin\" -- the name of the "
     "arc's entire space -- EACH APPEAR ZERO TIMES IN THE DEPOSITED MONOGRAPH.** The deposit is ms "
     "v5.10.2; the wall's naming is v5.13 and INTERNAL. That is why no contact here is typed "
     "REFINEMENT-OF-DEPOSITED on the wall.",

     "**A DIFFERENT VERDICT ON TWO OBJECTS IS NOT A CONFLICT BETWEEN TWO RECORDS.** **SCOPE: this "
     "act decided what two documents are about, and nothing about whether either is right.** "
     "**NOTHING IN THE ARC IS WEAKENED BY IT** -- the arc never claimed the Hilbert-Polya object, "
     "and its own scope sentences and this verdict agree exactly. NO GRADE MOVES. NO ACT IS "
     "RE-VERDICTED. NO KEYSTONE IS EDITED beyond an appended cross-reference block with every "
     "original visible, and **NO FILE UNDER `outputs/DEPOSITED-v1.1.2/` IS WRITTEN AT ALL** -- "
     "`git status` over that path returns empty. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly where the deposit left it. "
     "NOTHING DEPOSITS.",

     "current"),

    ("THE MARGIN: UNDECIDED, AND THE DEPOSIT WITHHOLDS THE BRIDGE DELIBERATELY (b324)",

     "THE MARGIN: UNDECIDED, AND THE DEPOSIT WITHHOLDS THE BRIDGE DELIBERATELY (b324): the balance "
     "keystone's margin is `M(n) := lambda_Z(n) + lambda_A(n) = lambda_n`, positive throughout "
     "1 <= n <= 300, minimum at n = 1 (lambda_1 = 0.0230957089661), growing like (n/2) ln n. The "
     "arc's is `W_8(f) - Tr(theta(g) S theta(g)*)`, equal by Theorem 4.7 to minus a remainder "
     "integral: +0.271444634, +0.285510313, +0.309777648, growing toward the boundary. **THEY "
     "DIFFER AT SIX OF SEVEN CONSTITUENTS** -- different index, different decomposition, and **only "
     "the keystone's margin contains the zeros**. The seventh keeps the question alive: the "
     "monograph names *positivity of the Weil functional* and *lambda_n >= 0* as classical faces of "
     "ONE obligation h2. **VERDICT: UNDECIDED.**",

     "**NO TERMINAL. EQUIVALENCE OF THE OBLIGATIONS IS NOT EQUIVALENCE OF THE MARGINS.** Two "
     "quantities can be faces of one RH-equivalent obligation and still be different numbers with "
     "different indices, different decompositions, and only one containing the zeros -- **exactly "
     "the error the resemblance ban exists to prevent, and it would have been easy to make.** And "
     "the reason the bridge is absent is stronger than the registered expectation supposed: the "
     "deposit records that the register pentagon compiles the five faces' structure *\"while "
     "**deliberately not** compiling the cross-register equivalences, since to compile 'discharge "
     "one and you discharge all five' would be to compile RH-equivalence itself.\"* **ABSENT BY "
     "DESIGN, NOT BY OVERSIGHT.** (F2)'s direction is confirmed; its account of why is replaced.",

     "**THE BRIDGING STATEMENT IS TYPED AND FILED AS THE ARC'S MOST VALUABLE OPEN ITEM**, on the "
     "order's own ground -- a margin the deposit already proved positive and growing would then be "
     "the arc's margin under another name: *a formula carrying the archimedean margin at a lawful "
     "test function to the Li margin at an index n, or a proof that no such formula exists.* **AND "
     "ITS HONEST PRICE IS STATED WITH IT**: the keystone's margin is positive and growing AT THE "
     "BENCH to n = 300, with lambda_Z measured NEGATIVE across n = 156..186 and 247..287, and "
     "Voros's threshold says no computation below n ~ 10^18 can bear on RH. A bridge would carry "
     "the arc's margin into a register whose own positivity is measured, not proved, in the "
     "computed range.",

     "**A QUESTION LEFT UNDECIDED IS NOT A QUESTION AVOIDED.** **SCOPE: this act decided that the "
     "two margins are not shown to be one object, and typed what would show it.** The seven "
     "contacts across the support texts come out 3 CORROBORATED, 4 UNTOUCHED, **0 IN TENSION -- "
     "and the zero is reported as a measurement, not a relief**, since three of the four UNTOUCHED "
     "are the arc never reaching the text at all. Five insights those texts hold and the arc did "
     "not use are listed as CANDIDATES WITH NO PROMOTION, the sharpest being the Epstein "
     "discrimination test the confinement keystone already describes. The wave's candidate list is "
     "TYPED, NOT RANKED; **the wave is the author's**. NO GRADE MOVED. NO AGGREGATION IS STATED; "
     "M-2 REMAINS (SPECIFIED-NOT-STATED). The seam's debt item 1 restated, still unpaid. h2 stands "
     "exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b324 -- THE KEYSTONES RE-READ.")
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

    r1, r2 = ROWS[0], ROWS[1]
    # ### **THE TWO GUARDS THAT MATTER FOR THESE TWO ROWS**, and they are guards against the two
    # ### readings the rows most invite: that a class test everything passes says something, and
    # ### that a control which HOLDS is a result about the object.
    g1 = ('DIFFERENT' in r1[1]
          and 'REFUTED' in r1[1]
          and 'resemblance' in r1[2].lower())
    g2 = ('UNDECIDED' in r2[1]
          and 'deliberately' in r2[2]
          and 'MOST VALUABLE OPEN ITEM' in r2[3]
          and 'NOTHING DEPOSITS' in r2[4])
    print('  row 1 carries DIFFERENT, the refuted expectation, and the resemblance ban : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 carries UNDECIDED, the deliberate withholding, and the owed bridge : %s  %s'
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
