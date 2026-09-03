# -*- coding: utf-8 -*-
"""b304_correspondence.py -- TWO ROWS: THE DISCHARGED CONDITION, AND THE COMPRESSED ANALOGUE.

### ### **THE NOTATION GUARD IS IMPORTED FROM `b303_correspondence.py`, NEVER COPIED.** ### b303's
### first run wrote two rows that split into 12 and 8 cells because the cell text carried real
### mathematical bars, and ### **A MARKDOWN TABLE READS EVERY ONE OF THEM AS A CELL BOUNDARY.**
### The splitter and the PRE-WRITE guard it built are read from that file here, so the two tools
### cannot drift.

### ### **THE HAZARD OF THESE TWO ROWS IN PARTICULAR:**
###   ### **ROW ONE RECORDS A DISCHARGE**, and a discharged condition in a table of results reads
###     as the object being finished. ### **IT IS NOT: THREE CONDITIONS REMAIN**, and the grade
###     cell says so before it says anything else.
###   ### **ROW TWO RECORDS A ZERO**, and a zero in this table reads as a barrier. ### **IT IS NOT
###     A BARRIER**: it is one test function's value on the part of the group the model can carry,
###     and the grade cell says which part was refused.
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
    ("THE ARCHIMEDEAN UNIT'S SQUARE-INTEGRABILITY (b304)",

     "THE ARCHIMEDEAN UNIT'S SQUARE-INTEGRABILITY (b304): the corpus's `u_inf` is `φ_μ` at the "
     "first even negative eigenvalue, normalized. **IT LIES IN `L²(ℝ)`, BY TWO INDEPENDENT ROUTES, "
     "BOTH FROM THE OWNERS' OWN DEFINITIONS.** ROUTE A — `φ_μ` is an eigenvector of `Wsa`, which "
     "CM defines as the restriction of `Wmax` to a subspace with an explicit `Dom Wsa`, and an "
     "eigenvector lies in its operator's domain by the definition of *eigenvector*; the ambient "
     "space is `L²(ℝ)` in CM's own words. **SO MEMBERSHIP IS DEFINITIONAL, NOT A DECAY STATEMENT.** "
     "ROUTE B — CM Corollary 3.2 puts `φ_μ` in the Sonin space, and CC defines that space as a "
     "subspace of the Hilbert space `L²(ℝ)_ev`. **THE HYPOTHESIS WAS CHECKED, NOT CARRIED ON THE "
     "COROLLARY'S NAME: Corollary 3.2 needs `μ` negative and b214's printed `μ` is "
     "−20.48057322913694697.**",

     "**NO TERMINAL. A READ AND A DERIVATION ARE NOT A COMPILE.** The evidence is two pinned "
     "artefacts: CM, *Prolate spheroidal operator and Zeta*, `arXiv:2112.05500v1`, sha256 "
     "`426114ae0d3e28e5caf722afb4a1050a85c2732d0b04b7b861ec9ff70c346303`; and CC "
     "`arXiv:2006.13771`, sha256 "
     "`b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0`. Both text layers are "
     "intact — these are typeset PDFs, not the 1939 scan — **so no page image was needed and none "
     "is pretended to.**",

     "**NO PRINT. NOTHING COMPILED FOR THIS ROW.** The separately-built shadow of this act "
     "(`Core/IndexRangeShadow.lean`, 9 zero-axiom terminals) certifies the shape of two integer "
     "ranges and **is not evidence for this row.**",

     "**AT CONTENT, THIS ACT'S OWN READ OF BOTH SOURCES.** `W-ORD-PHI-MU-L2` — filed at b300 as "
     "*stated by no owner* — is **DISCHARGED**; an owner does state it, twice, and what was "
     "missing was the read and not the mathematics. **SCOPE, AND IT IS THE WHOLE OF THE ROW'S "
     "HONESTY: THE OBJECT STILL STANDS ON THREE CONDITIONS** — the level-limit premise, "
     "`W-ORD-ARCH-NORM-READING`, and C9/`N-OPEN-B` — and **A CONDITION DISCHARGED IS NOT THE "
     "OBJECT CONSTRUCTED.** It does NOT put `u_inf` in the sector (b201's BRANCH (NO EXHIBIT) "
     "stands) and does NOT touch which inner product the normalization is. **NO GRADE MOVES. M-2 "
     "REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.**",

     "current"),

    ("THE FINITE ANALOGUE OF THE SCALING-TRACE, COMPRESSED (b304)",

     "THE FINITE ANALOGUE OF THE SCALING-TRACE, COMPRESSED (b304): from CC's own description of "
     "its move — *one can associate to a test function `f` the trace `Tr(θ(f) S)`* — the finite "
     "analogue is `T(f) := Tr(θ(f) Π)` with `θ(t)e_j = e_{tj}` on `ℤ/N`, `N = p^{2n}`, and `Π` the "
     "orthogonal projection onto `Son(p,n)`. **DECIDED BY DEFINITIONS BEFORE ANY NUMBER: THE "
     "BARRIER DOES NOT REACH IT.** The barrier's operator is a functional of the unit's "
     "restriction TO the ball — precisely where every element of `S̄_p` vanishes — while the "
     "smeared operator's matrix elements are supported OFF the ball, precisely where `S̄_p` lives. "
     "**THE BARRIER IS NOT WEAKENED BY THIS: an operator it does not reach is not a counterexample "
     "to it.**",

     "**NO TERMINAL FOR THIS ROW.** The computation is `tools/b304_smearing.py` — exact `Fraction` "
     "arithmetic, **no float token anywhere** — with `Π` built once per cell by Gram-Schmidt over "
     "`ℚ` and each trace read off as `Σ_m Π[t⁻¹m][m]`. Controls both polarities: `Tr(Π) = dim Son "
     "= (p^n−1)²` at every cell (**the instrument is not dead**); an off-ball spike is MOVED by "
     "`Π`; `Π` idempotent, symmetric, fixing its basis; and each `θ(t)`'s fixed-point count "
     "checked against `gcd(t−1, N)` — **two routes to one integer**.",

     "**NO PRINT.** The measured values, at `(2,1) (2,2) (3,1) (3,2) (5,1) (7,1)`: `dim Son` = 1, "
     "9, 4, 64, 16, 36, matching the owner's law at every cell; individual `Tr(θ(t)Π)` NONZERO at "
     "2/2, 8/8, 3/6, 27/54, 5/20, 7/42 units; and **the smeared value against the constant test "
     "function on the units is EXACTLY 0 AT ALL SIX CELLS, including every one-level place.** "
     "**AND THE ZERO IS DERIVED, NOT ONLY MEASURED:** `Σ_t θ(t) = \\|U\\|·Q` onto the "
     "unit-invariants, "
     "which are spanned by valuation shells, and every `Son` vector is orthogonal to every shell — "
     "by vanishing on the ball above the level, and by fiber sums below it. Both limbs checked at "
     "every cell.",

     "**A COMPUTATION ON THE PART OF THE GROUP THE MODEL CAN CARRY, AND THE REST WAS REFUSED.** "
     "`ℚ_p^× = p^ℤ × ℤ_p^×`. The `ℤ_p^×` part acts by permutations of `ℤ/N` — **verified at every "
     "`t` used, not assumed** — so nothing escapes the level. The `p^ℤ` part is b21's escaped-mass "
     "artifact, met at b284, and **WAS NOT COMPUTED: the model would return the genuine object "
     "with its escaped mass folded back onto the ball.** **SCOPE: THE REFUSED PART IS THE PART "
     "WITH AN ARCHIMEDEAN COUNTERPART**, so this zero is not *the finite analogue's value*. **IT "
     "IS NOT A BARRIER AND NOT A ROUTE**; for a general test function the value is `Σ_t f(t) "
     "Tr(θ(t)Π)` and those traces are not all zero. **NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED), UNCHANGED.**",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b304 -- THE DISCHARGED CONDITION\'S ROW, AND THE COMPRESSED ANALOGUE\'S ROW.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    # ### THE PRE-WRITE NOTATION GUARD (b303's D8). ### **CHECKED BEFORE WRITING, NOT AFTER.**
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

    # ### THE ROW-SPECIFIC GATES. ### **EACH ROW MUST CARRY THE REFUSAL ITS OWN HAZARD NEEDS.**
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('THREE CONDITIONS' in r1[4] and 'NO TERMINAL' in r1[2] and 'NO PRINT' in r1[3])
    g2 = ('NOT A BARRIER AND NOT A ROUTE' in r2[4] and 'WAS NOT COMPUTED' in r2[4])
    print('  row 1 says the object still stands on three conditions, and declares no terminal : %s'
          '  %s' % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses barrier and route, and names what was NOT computed : %s  %s'
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
