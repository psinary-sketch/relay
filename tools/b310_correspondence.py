# -*- coding: utf-8 -*-
"""b310_correspondence.py -- TWO ROWS: THE COLLAPSE, AND THE FIXED-POINT SENTENCE WITH ITS BEARING.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS, AND THE SECOND IS THE MOST DANGEROUS ROW THIS SEAT HAS
### ### WRITTEN:**
###   ### **ROW ONE RECORDS THAT A CONSTRUCTION RETURNS ALMOST NOTHING**, and that reads as a
###     verdict on the construction. ### **IT IS NOT: IT IS WHAT THE CONSTRUCTION RETURNS AT A
###     FINITE PLACE, ON THIS OBJECT, IN THIS COMPRESSION** -- and the source works at the
###     archimedean place, where none of the derivation applies.
###   ### **ROW TWO TOUCHES A BRANCH NOBODY HAS SETTLED AND A SPECIFICATION THE CORPUS OWES.** ###
###     A row that narrows one property of `M-2`'s specification reads as a verdict on `M-2` and as
###     a vote for the archimedean branch. ### **IT IS NEITHER, AND THE GRADE CELL SAYS SO BEFORE IT
###     SAYS ANYTHING ELSE.**
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
    ("THE SMEAR COLLAPSES (b310)",

     "THE SMEAR COLLAPSES (b310): the source's own construction — *\"one can associate to a test "
     "function `f in C_c^infinity(R*_+)` the trace `Tr(theta(f) S)`\"* — assembled on the b308 "
     "instrument. **AT A FINITE PLACE THE SCALING PART OF `Q_p^x` IS `p^Z`, WHICH IS DISCRETE**, so "
     "the source's integral over it is a SUM over the powers of the prime with the test function "
     "evaluated at those powers: `T(w) = SUM over k of w_k Tr(theta(p^k) Pi)`. The weight is "
     "SYMBOLIC — no bump is chosen, so no class question arises and no price is paid — and the sum "
     "is finite because the source's test functions are compactly supported. **WITH b309's ZEROS "
     "AT EVERY NONZERO POWER, EXACTLY ONE TERM SURVIVES: `T(w) = w_0 (p^n − 1)^2`.** Seven cells, "
     "every carried power, **0 TERMS SURVIVING AWAY FROM THE IDENTITY.**",

     "**TWO TERMINALS, BOTH ZERO AXIOMS**, `Core/SmearCollapseShadow.lean`, vanilla Lean, no "
     "imports, no `native_decide`, no `sorry`: `B310.signed_count_at_the_identity_is_the_dimension` "
     "and `B310.identity_term_survives_alone` — the second carrying **BOTH ARMS in one statement**, "
     "because the vanishing arm alone is satisfied by a count that is zero everywhere and *alone* "
     "is a claim about both. **EACH RANGES OVER AN EXPLICIT LIST NAMED IN ITS OWN STATEMENT.** "
     "**AND WHAT THEY CERTIFY IS ARITHMETIC AND NOT THE COLLAPSE**: the step to `T(w) = w_0 "
     "(p^n − 1)^2` is the bank's derivation and is UNCOMPILED, said in the module's own header.",

     "**THE PROFILE MOVED 473 → 475 PRINTS, ALL ZERO-AXIOM**, the baseline regenerated "
     "BYTE-IDENTICALLY before anything was added and the banked profile is a TRUE BYTE PREFIX of "
     "the new one. The zeros are **NOT SUBSTITUTED IN** — every term is formed and added, so the "
     "collapse is something the sum DOES. **AND THE ARM THAT MAKES IT MEAN SOMETHING: two weights "
     "agreeing at the identity and differing at EVERY carried power give the SAME value, while two "
     "differing AT the identity give DIFFERENT values.** Both arms, at all seven cells. `Tr(Pi)` is "
     "nonzero at every cell, so the surviving term is not itself zero.",

     "**A COMPUTATION AND A DERIVATION, GENERAL IN `p`, `n` AND THE WEIGHT, WITH THE SEVEN-CELL "
     "TABLE AS THE CHECK AND NOT THE PROOF.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: "
     "this is what the construction returns AT A FINITE PLACE, ON THIS OBJECT, IN THIS "
     "COMPRESSION.** **THE SOURCE WORKS AT THE ARCHIMEDEAN PLACE, WHERE THE GROUP IS CONTINUOUS AND "
     "NONE OF THIS DERIVATION APPLIES** — the contrast is NAMED and NOT derived, and b285's "
     "boundary stands. b309's zero is CARRIED, not re-derived, and its scope travels with it. **ONE "
     "CLAUSE OF THIS ACT'S OWN SEALED PREDICTION WAS REFUTED BY ITS OWN RUN** — the normalizing "
     "factor, not the count. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 "
     "stands exactly where the deposit left it.",

     "current"),

    ("THE FIXED-POINT SENTENCE, AND ITS BEARING (b310)",

     "THE FIXED-POINT SENTENCE, AND ITS BEARING (b310): b304 computed the COMPACT part of the local "
     "multiplicative group and found its smear over the units zero; b309 computed the SCALING part "
     "and found it zero at every nonzero power. **THOSE ARE ONE STATEMENT: `Tr(theta(t) Pi)` IS A "
     "SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO CONGRUENCES THE OBJECT'S TWO "
     "CONDITIONS IMPOSE, WEIGHTED BY THE EMBEDDING'S HAAR FACTOR.** At `t = 1` every off-ball point "
     "is fixed and the count is `(p^n − 1)^2`; at `t = p^k` with `k` nonzero NOTHING off the ball "
     "is fixed, because `p^k − 1` is a unit, and the only point it fixes is the one place the "
     "object must vanish. **AT A UNIT OTHER THAN 1 THE COUNT IS GENERALLY NONZERO — b304's zero is "
     "the SUM over the units, not a per-unit vanishing, and the two halves are NOT the same kind of "
     "zero.**",

     "**NO TERMINAL FOR THE SENTENCE ITSELF** — it quantifies over the whole multiplicative group "
     "at every place and every level. The formula is checked against **b304's OWN `trace_scaled` at "
     "every unit** (nonzero at many of them, so the agreement is not an agreement about zeros) "
     "**and against b309's reduced sum at every carried power**, at all seven cells, 0 disagreeing. "
     "**AND A CLAUSE OF THE SEALED PREDICTION IS REFUTED HERE**: it named the factor *the modulus "
     "of `t`*; the factor is the embedding's Haar weight `p^{-max(k,0)}`, which agrees with the "
     "modulus at every unit and every POSITIVE power and differs at every NEGATIVE one. Under b21's "
     "unitary normalization it becomes symmetric. **THE COUNT IS THE CONTENT; THE FACTOR IS WHAT "
     "THE PREDICTION GOT WRONG, AND IT CHANGES NO VALUE THIS ACT REPORTS — WHICH IS WHY IT WAS "
     "CHECKED ON ITS OWN.** *(The absolute-value bars are written out in words here: the notation "
     "guard fired on them BEFORE this row was written, which is the third act running that it has "
     "caught this act's own notation.)*",

     "**NO PRINT BEYOND ROW 132's.** The reading, at exactly its scope: **at a finite place the "
     "source's construction carries NO ARITHMETIC** — the surviving term has no `log p` and samples "
     "the weight only at the identity. **THE PRIME'S CONTRIBUTION IS NOT MISSING FROM THE PLACE; IT "
     "IS SOMEWHERE ELSE**: in the local distribution the source integrates AGAINST, `W_p(f) = "
     "(log p) SUM_{m>=1} ( f(p^m) + f#(p^m) )`, eq. (149), read at content by b305 — which carries "
     "the `log p` AND samples at exactly the powers this trace does not read.",

     "**A BEARING, NEVER A DECISION.** The bearing is one sentence: **the finite side cannot supply "
     "the first-level mass THROUGH THE OBJECT**, because the functional's coefficient at `p^1` is "
     "exactly zero. On b263's three properties, for candidates of THIS CLASS: **(SPEC-1) CANNOT be "
     "met** — the one place it demands weight is exactly where the zero sits; **(SPEC-3) CAN be "
     "met** — the derivation is general in `p`; **(SPEC-2) IS NOT DECIDED BY THIS ACT**, the "
     "functional having no level index to compare. **SCOPE, AND IT IS THE WHOLE OF THE ROW'S "
     "HONESTY: THIS IS NOT A DECISION ON b262's BRANCH** — b262's own sentence is that the "
     "archimedean side MUST absorb a divergent quantity *if* the identity holds along that "
     "direction, and b262 attaches that this is **not a claim that it fails to do it**; the "
     "disjunction is b263's FORMULATION, not b262's wording. **IT IS NOT A VERDICT ON M-2**, which "
     "remains (SPECIFIED-NOT-STATED) — b263's own refusal governs: *these exclude; they do not "
     "determine.* **IT IS NOT A CLAIM THAT THE FINITE SIDE CONTRIBUTES NOTHING** — a distribution "
     "is not a trace on a space. **AND IT IS NOT AN ARGUMENT FOR THE ARCHIMEDEAN BRANCH**, where "
     "this act derives nothing. NO AGGREGATION IS STATED. h2 stands exactly where the deposit left "
     "it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b310 -- THE COLLAPSE\'S ROW, AND THE FIXED-POINT SENTENCE\'S.')
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
    g1 = ('NONE OF THIS DERIVATION APPLIES' in r1[4] and 'AS THE CHECK AND NOT THE PROOF' in r1[4]
          and 'ARITHMETIC AND NOT THE COLLAPSE' in r1[2])
    g2 = ('NEVER A DECISION' in r2[4] and 'NOT A VERDICT ON M-2' in r2[4]
          and 'NOT AN ARGUMENT FOR THE ARCHIMEDEAN BRANCH' in r2[4]
          and "b263's FORMULATION" in r2[4])
    print('  row 1 keeps the archimedean place out and the sweep from being a proof : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the branch, the M-2 verdict and the attribution slip : %s  %s'
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
