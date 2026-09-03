# -*- coding: utf-8 -*-
"""b309_correspondence.py -- TWO ROWS: THE TRACE COMPUTED, AND THE MECHANISM DERIVED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED** -- from
### `b303_correspondence.py` and `b302_correspondence.py`.

### ### **THE HAZARD OF THESE TWO ROWS, AND IT IS SHARPER THAN b308's:**
###   ### **ROW ONE RECORDS A ZERO, AND A ZERO IN A TABLE OF RESULTS READS AS AN OBSTRUCTION.**
###     ### It is not one. ### It is the vanishing of ONE trace of ONE map against ONE projection,
###     and the grade cell says what it is not before it says anything else.
###   ### **ROW TWO RECORDS A DERIVATION WITH A TERMINAL BESIDE IT, AND A TERMINAL BESIDE A
###     ### DERIVATION READS AS A CERTIFICATION OF IT.** ### **IT IS NOT: THE TERMINALS CERTIFY
###     ### ARITHMETIC AND THE STEP TO THE VANISHING IS UNCOMPILED**, and the terminal cell says so.
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
    ("THE SCALING TRACE, COMPUTED (b309)",

     "THE SCALING TRACE, COMPUTED (b309): `Tr(theta(p^k) Pi)` for `k != 0` — the compression of the "
     "SCALING part of the local multiplicative group against the projection onto the object's own "
     "space. **b304 COMPUTED THE COMPACT PART AND REFUSED THIS ONE** — *this file computes the "
     "`Z_p^x` part exactly and refuses the `p^Z` part* — because in the model `theta(p^k)` folds. "
     "b308 built the frame where it does not fold and named this computation without performing it. "
     "**THE FIRST THING THE ACT ESTABLISHES IS THAT THE TRACE IS NOT DEFINED UNTIL AN AMBIENT IS "
     "NAMED:** `theta(p^k)` carries `V(n,n)` to `V(n−k, n+k)`, so the composed map is no frame's "
     "endomorphism, and the smallest frame containing both is `V(max(n,n−k), max(n,n+k))`. "
     "**THE VALUE: EXACTLY ZERO AT EVERY NONZERO POWER IN `[−2n, 2n]` AT ALL SEVEN BANKED CELLS.**",

     "**NO TERMINAL FOR THE TRACE ITSELF** — it quantifies over levels and places and a terminal at "
     "one cell would sit in the kernel looking like the general statement (b299's own refusal "
     "reason). **THREE TERMINALS WERE BUILT FOR THE ARITHMETIC BESIDE IT** and they are row 131's. "
     "`tools/b309_scaling_trace.py` and `tools/b309_components.py`: exact `Fraction` and `int`, "
     "**zero float literals in the deciding runner**. **TWO INDEPENDENT ROUTES — 34 cell/power "
     "pairs by both, 10 by the reduced route only where the ambient exceeds 1024 chart points and "
     "the bound is PRINTED rather than the second route quietly dropped. 0 DISAGREEING.**",

     "**THE PROFILE MOVED 470 → 473** (row 131). The controls, in both polarities, BEFORE any "
     "scaling value was read: the known-NONZERO case `k = 0` returns b304's not-dead witness "
     "`(p^n−1)^2` at every cell; a known-ZERO unit is exhibited where one exists. **AND THE "
     "`UNAVAILABLE` ARM, WHICH IS NOT A PASS: at level 1 the overlapping regime is EMPTY, so its "
     "not-dead witness CANNOT EXIST and is reported as unavailable** — b280's own shape. **THE "
     "STRONGEST CONTROL IS THE COMPRESSION ITSELF: in regime B it is a LIVE operator (10 of 9² "
     "entries at (2,2), 144 of 64² at (3,2)) WHOSE TRACE IS EXACTLY ZERO.** A dead operator "
     "reporting a zero trace would have shown nothing.",

     "**A COMPUTATION, AND ITS VALUE IS ZERO. ### NOT AN OBSTRUCTION THEOREM.** **SCOPE, AND IT IS "
     "THE WHOLE OF THE ROW'S HONESTY: this is ONE trace of ONE map against ONE projection, at the "
     "cells and powers listed, in the smallest ambient containing source and target — a different "
     "ambient is a different number.** It says nothing about any other functional on the "
     "instrument, and **nothing about the source's own functional, which smears against a test "
     "function over the whole group: a vanishing of every individual term is a statement about "
     "terms.** **IT IS NEITHER A ROUTE NOR AN ANTI-ROUTE** — the order forbids reading a nonzero as "
     "a route and this act adds that the converse reading is forbidden too. **NOTHING ABOUT THE "
     "ARCHIMEDEAN PLACE** (b285's boundary stands). **b273's `A` at `k = n` IS A DIFFERENT "
     "OPERATOR: the barrier and the compression are neither extended nor weakened here.** NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the "
     "deposit left it.",

     "current"),

    ("THE MECHANISM: NO OFF-BALL FIXED POINT (b309)",

     "THE MECHANISM: NO OFF-BALL FIXED POINT (b309): **TWO REGIMES, TWO MECHANISMS.** ABOVE THE "
     "LEVEL (`abs(k) >= n`) the object's support and its image's are DISJOINT — the object vanishes "
     "on the ball, so its support sits at absolute values `p^1 .. p^n` and the image's at "
     "`p^(1+k) .. p^(n+k)` — and **the compression is the ZERO OPERATOR**, measured. BELOW IT "
     "(`1 <= abs(k) <= n−1`) **THE SUPPORTS GENUINELY MEET AND THE TRACE IS STILL ZERO**, and the "
     "reason is arithmetic: against the projector's closed form the trace is a sum over `t` off the "
     "ball of two congruence indicators in `(p^j − 1) t`, and **`p^j − 1` IS A UNIT**. Each "
     "congruence therefore forces `t = 0` modulo the grid and modulo the ball's own modulus — "
     "**AND BOTH OF THOSE SETS ARE EXACTLY THE BALL, WHICH THE SUM EXCLUDES.** In one sentence: "
     "**the scaling map fixes nothing off the ball, and the only thing it fixes is the one place "
     "the object is required to vanish.**",

     "**THREE TERMINALS, ALL PRINTING ZERO AXIOMS**, `Core/ScalingTraceShadow.lean`, vanilla Lean, "
     "no imports, no `native_decide` (which would add an axiom), no `sorry`: "
     "`B309.frame_arithmetic`, `B309.support_ranges_split_at_the_level` (**BOTH ARMS — the meeting "
     "arm keeps the disjoint arm from reading as vacuous**), and "
     "`B309.no_offball_fixed_point_of_scaling`. **EACH RANGES OVER AN EXPLICIT LIST NAMED IN ITS "
     "OWN STATEMENT, SO NONE CAN BE READ AS A LAW ABOUT ALL `p`, `n`, `k`.** **AND WHAT THEY "
     "CERTIFY IS ARITHMETIC AND NOT THE BARRIER: the step from these counts to the vanishing of "
     "the trace is the bank's derivation and IS UNCOMPILED**, said in the module's own header.",

     "**THE PROFILE: 470 → 473 PRINTS, ALL ZERO-AXIOM, AND THE BANKED PROFILE IS A TRUE BYTE PREFIX "
     "OF THE NEW ONE** — a build that adds terminals must leave every existing print line exactly "
     "where it was, and a print count alone would not show a line that moved. Checked byte-wise, "
     "not line-wise (b298's incident). The baseline was regenerated BYTE-IDENTICALLY from the "
     "unchanged file BEFORE anything was added, and **that was done at step zero, before the cap "
     "permitting a build was written** — a cap permitting a build nobody has shown can run is a "
     "promise, not a permission.",

     "**A DERIVATION, GENERAL IN `p`, `n` AND `k`, WITH A FINITE SWEEP AS ITS CHECK — AND THE ACT "
     "SAYS WHICH IS WHICH.** No step of the derivation mentions a cell: the projector's closed form "
     "is built from the object's TWO CONDITIONS, the reduction is frame algebra, and `p^j − 1` is "
     "coprime to `p` for every prime and every `j >= 1`. **A SWEEP OVER SEVEN CELLS IS NOT A PROOF "
     "OVER ALL OF THEM, AND THE TERMINALS DO NOT MAKE IT ONE.** **SCOPE: the barrier statement is "
     "about this map, these frames, and this projection. Nothing about the archimedean place, the "
     "identity, h2, or the complete roster.** **AND ONE CLAUSE OF THE ACT'S OWN SEALED PREDICTION "
     "WAS REFUTED BY ITS OWN RUN** — it said the COMPOSED operator is identically zero above the "
     "level; it is the COMPRESSION that vanishes, the image being orthogonal to the space rather "
     "than absent. The content survived, the wording did not, and the seal is not edited. NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b309 -- THE TRACE\'S ROW, AND THE MECHANISM\'S.')
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

    # ### THE ROW-SPECIFIC GATES. ### **EACH ROW MUST CARRY THE REFUSAL ITS OWN HAZARD NEEDS.**
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('NOT AN OBSTRUCTION THEOREM' in r1[4] and 'NEITHER A ROUTE NOR AN ANTI-ROUTE' in r1[4]
          and 'NO TERMINAL FOR THE TRACE ITSELF' in r1[2])
    g2 = ('ARITHMETIC AND NOT THE BARRIER' in r2[2] and 'IS UNCOMPILED' in r2[2]
          and 'IS NOT A PROOF' in r2[4])
    print('  row 1 refuses the obstruction reading and the route reading : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 says the terminals certify arithmetic and not the barrier : %s  %s'
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
