# -*- coding: utf-8 -*-
"""b303_correspondence.py -- THE UNIFORM FAMILY'S ROW.

### ### **THIS ROW'S HAZARD IS THE OPPOSITE OF b302's.** ### There, a compiled terminal in a table
### of compiled statements risked reading as certifying the act. ### Here the terminal is small and
### ### **THE PROSE IS LARGE** -- a cross-place definition in a table of results reads as a result
### about all places at once. ### **IT IS A DEFINITION. ### THE STATEMENT CELL SAYS SO FIRST, AND
### THE GRADE CELL CARRIES THE DIVISION THAT IS THIS ACT'S ACTUAL FINDING: ### UNIFORM AS A FORM,
### NOT AS AN OBJECT.**

### ### **IDEMPOTENT: THE MARKER IS A LITERAL PREFIX OF THE STATEMENT WRITTEN.**
### ### **THE BLANK-CELL CHECK IS LINE-SCOPED** (b297's fix), and the checker is IMPORTED from
### b302's tool rather than copied.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C  # noqa: E402  ### the blank-cell audit is READ, never copied

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE TWO-RADIUS FAMILY ACROSS PLACES (b303)",

     "THE TWO-RADIUS FAMILY ACROSS PLACES (b303): **THIS ROW RECORDS A DEFINITION, NOT A RESULT.** "
     "A member is a choice, at every place `v`, of a pair of radii `(λ_v, μ_v)` — the first "
     "bounding where the function vanishes, the second where its transform does — with "
     "`Son_v(λ_v, μ_v) := { f in the local space at v : f vanishes on abs_v(x) ≤ λ_v, and (F_v f) "
     "vanishes on abs_v(y) ≤ μ_v }`, each of the local space, `abs_v` and `F_v` being that "
     "place's own. It restricts to b293's `Son(p,n;a,b)` at finite `p` (via b21's chart "
     "`x = p^{-n}m`, "
     "which is the CORPUS'S chart and not this act's) and to CC Definition 4.4's `S(λ,μ)` at "
     "`∞`. **THE CORPUS'S OBJECT IS THE EVERYWHERE-`(1,1)` MEMBER**, which at every place is the "
     "transform-fixed point of its own dilation orbit. **NO AGGREGATION IS STATED.**",

     "`Core/ValuationDivisibilityShadow.lean` — **12 TERMINALS, ALL ZERO-AXIOM**, and they "
     "certify **ONLY THE INDEX-SET HALF** of the diagonal identification: over `m < p^(2n)` at "
     "`(2,1) (2,2) (3,1) (3,2) (5,1)`, *the p-adic valuation of m is at least n* and *p^n divides "
     "m* agree at every `m`, the two predicates being defined separately (repeated division vs a "
     "single modulo) with neither calling the other. **THE COEFFICIENT HALF — the transform "
     "condition in `Q(ζ_N)` — IS NOT BUILT, because a finite coefficient ring would certify the "
     "stand-in and not the statement.** Polarity controls first, including a decided fuel guard "
     "and a not-dead arm. **VANILLA: 0 imports, 0 `native_decide`, 0 `sorry`, no float.**",

     "**461 PRINTS, 461 ZERO-AXIOM, 0 OTHERWISE (was 449/449/0)**, regenerated from source into "
     "memory and written as bytes; **the 449 pre-existing prints survive as a TRUE BYTE PREFIX "
     "against `git HEAD`**; no byte-order mark, read as bytes. The baseline arm ran first and "
     "reproduced the banked 30992 bytes exactly before anything changed. Separately, the finite "
     "half of the diagonal was **re-verified at content by `tools/b303_family.py`** — exact "
     "`Fraction` arithmetic, no float — vector by vector in both directions at all five cells, "
     "with an off-ball spike rejected and the collapsed condition checked against the actual "
     "transform in `Q(ζ_N)`: **0 cells failing**.",

     "**A DEFINITION, AND ITS HONEST GRADE IS A DIVISION: UNIFORM AS A FORM, NOT AS AN OBJECT.** "
     "One sentence covers all places because every term delegates to the place; the instances are "
     "structurally different **by a theorem** — the sub-level set is a compact open subgroup at "
     "`p` and provably not one at `∞` (b198). **A LATER ACT MAY QUOTE THE FORM AND MAY NOT "
     "QUANTIFY OVER THE OBJECTS AS THOUGH THEY WERE ONE KIND OF THING.** **SCOPE: THIS ROW STATES "
     "NO AGGREGATION, OPENS NO ROUTE, AND MOVES NO GRADE.** The annihilation criterion remains a "
     "statement about members at the finite places. `W-ORD-UNIFORM-FORM` stays "
     "UNBANKED-UNTIL-TESTED; promotion is the author's. **M-2 REMAINS (SPECIFIED-NOT-STATED), "
     "UNCHANGED. h2 stands exactly where the deposit left it.**",

     "current"),

    ("VON NEUMANN'S DEFINITION 3.3.1, READ AT SOURCE (b303)",

     "VON NEUMANN'S DEFINITION 3.3.1, READ AT SOURCE (b303): quoted whole from the page image — "
     "*\"A sequence `f_α`, `α ∈ I`, is a `C₀`-sequence, if and only if `f_α ∈ H_α` for all "
     "`α ∈ I`, and `Σ_{α∈I} \\| ‖f_α‖ − 1 \\|` converges.\"* **IT ASKS FOR MEMBERSHIP AND A "
     "CONVERGENT "
     "NORM SUM AND FOR NOTHING MORE**, and it makes **NO PARTITION OF `I`** — no clause "
     "distinguishes an archimedean index from a finite one. **VERDICT: CONFIRMS.** b302's "
     "execution of `RULE ARCH-UNIT` stands on the source's own words rather than on b197's report "
     "of them, and the conditional b302 wrote against itself is **DISCHARGED**.",

     "**NO TERMINAL. A READ IS NOT A COMPILE**, and nothing here is machine-checked. The evidence "
     "is the artefact and the cut: von Neumann, *On infinite direct products*, Compositio "
     "Mathematica 6 (1939) 1–77, `numdam` PDF, 78 pages, **sha256 "
     "`571060b596af58af35f09f077984a2b747e7acbc52ab6d107ba8b45c761ad0a3`**, page index 21, cut to "
     "`b303_vN_p21_def331.png` (sha256 `57636446d8a74f283f43900a453b6948…`) by "
     "`tools/b303_source.py`. **THE TOOL RUNS NO OCR AND READS NOTHING — THE QUOTATION IS A HUMAN "
     "READ OF THE EMITTED IMAGE**, which is why the artefact is hashed.",

     "**NO PRINT. NOTHING COMPILED FOR THIS ROW.** The measured facts are the artefact's: the "
     "PDF's OCR text layer drops every displayed formula, so Definition 3.3.1's text layer ends "
     "mid-sentence at *\"if and\"* and the next line is the page number — **the defect measured in "
     "the file rather than recalled from b197** — and the control holds: **the next page is not "
     "truncated**, so the finding is this page's.",

     "**AT CONTENT, THIS ACT'S OWN READ, BY A ROUTE INDEPENDENT OF b197's** — and the two agree "
     "word for word. **SCOPE: ONE DEFINITION.** Lemma 4.1.2, Definition 4.1.1 and Definition "
     "3.3.2 were NOT re-read and stand at b226's at-source grade. **A CONFIRMATION REMOVES AN "
     "EXPOSURE; IT DOES NOT ADD A RESULT** — Q4 stays withdrawn, the sector clause stays "
     "description, b214's `c = +1` stays at BENCH. **AND IT SETTLES ONE TYPING:** "
     "`W-ORD-PHI-MU-L2` is Definition 3.3.1's membership conjunct at `∞`, so it is a condition of "
     "the object. **M-2 UNCHANGED. NOTHING DEPOSITS.**",

     "current"),
]


def split_cells(line):
    """### SPLIT A TABLE ROW ON ITS ### UNESCAPED ### PIPES.

    ### ### **THIS FUNCTION EXISTS BECAUSE THIS TOOL'S FIRST RUN WROTE TWO ROWS THAT SPLIT INTO 12
    ### ### AND 8 CELLS INSTEAD OF 6.** ### The cell text carried `|x|_v` and `Σ | ... |` -- real
    ### mathematical notation whose bars are ### LITERAL PIPES ### , and a markdown table reads
    ### every one of them as a cell boundary. ### **THE READ-BACK CAUGHT IT, THE TABLE WAS RESTORED
    ### FROM `git`, AND THE FIX IS AN ESCAPE PLUS A GUARD RATHER THAN A REWORDED QUOTATION** --
    ### the quoted definition must stay verbatim, so it is the SPLITTER that learns about `\\|`.
    """
    out, cur, i = [], [], 0
    body = line.strip()
    if body.startswith('|'):
        body = body[1:]
    if body.endswith('|') and not body.endswith('\\|'):
        body = body[:-1]
    while i < len(body):
        if body[i] == '\\' and i + 1 < len(body) and body[i + 1] == '|':
            cur.append('|')
            i += 2
            continue
        if body[i] == '|':
            out.append(''.join(cur))
            cur = []
            i += 1
            continue
        cur.append(body[i])
        i += 1
    out.append(''.join(cur))
    return out


def split_fixture():
    """### **BOTH POLARITIES ON THE SPLITTER, AND THE ESCAPED CASE IS THE WHOLE REASON.**"""
    a = len(split_cells('| a | b | c |')) == 3
    b = len(split_cells('| a | x \\| y | c |')) == 3      # ### the escaped bar is NOT a boundary
    c = split_cells('| a | x \\| y | c |')[1].strip() == 'x | y'
    d = len(split_cells('| a | x | y | c |')) == 4        # ### a raw bar IS a boundary
    return a, b, c, d


def raw_pipes(text):
    """### COUNT ### UNESCAPED ### pipes in a cell's text. ### **A CELL MAY CONTAIN NONE.**"""
    n, i = 0, 0
    while i < len(text):
        if text[i] == '\\' and i + 1 < len(text) and text[i + 1] == '|':
            i += 2
            continue
        if text[i] == '|':
            n += 1
        i += 1
    return n


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    print('=' * 100)
    print('b303 -- THE UNIFORM FAMILY\'S ROW, AND THE SOURCE READ\'S ROW.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302_correspondence, re-run here):')
    print('    counts a real blank cell: %-5s   stays quiet on full rows: %-5s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    if not (pos and neg):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    sa, sb, sc, sd = split_fixture()
    print('  SPLITTER FIXTURE : plain=%s  escaped-bar-not-a-boundary=%s  content=%s  raw-bar-is=%s'
          '  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (sa and sb and sc and sd):
        return 1

    # ### THE PRE-WRITE GUARD. ### **REFUSE ANY CELL CARRYING AN UNESCAPED PIPE, BEFORE WRITING.**
    # ### The first run of this tool wrote first and found out afterwards; the read-back caught it
    # ### and `git` restored the table. ### **A GUARD THAT ONLY FIRES AFTER THE WRITE IS A REPAIR,
    # ### NOT A GUARD.**
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if raw_pipes(str(c))]
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
        print('  ### **THE READ-BACK ARMS STILL RUN** (b302 D8).')
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

    # ### THE ROW-SPECIFIC GATES. ### **EACH ROW MUST CARRY THE THING ITS OWN HAZARD NEEDS.**
    # ### Row 1 has a terminal and must name the module AND the before/after counts AND must say
    # ### what the terminal does NOT certify. ### Row 2 has NO terminal and must SAY SO.
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('ValuationDivisibilityShadow.lean' in r1[2]
          and 'was 449/449/0' in r1[3]
          and 'IS NOT BUILT' in r1[2])
    g2 = ('NO TERMINAL' in r2[2] and 'NO PRINT' in r2[3])
    print('  row 1 names its module, its before/after counts, and what it does NOT build : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 declares NO TERMINAL and NO PRINT rather than leaving them implied : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    # ### THE NO-OVERSTATEMENT GATE. ### **BOTH GRADE CELLS MUST CARRY A SCOPE REFUSAL AND M-2.**
    over = [i for i, r in enumerate(ROWS)
            if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
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
    cellcounts = [len(split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
