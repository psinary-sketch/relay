# -*- coding: utf-8 -*-
"""b289_correspondence.py -- BRING THE CORRESPONDENCE TABLE CURRENT WITH THE ARC.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **THE POINT OF THIS FILE, AND THE REASON IT IS A COMMITTED TOOL RATHER THAN A HAND EDIT:**
### ### **THE ROW TABLE BELOW IS THE SINGLE SOURCE OF TRUTH AND THIS RUNNER WRITES THE MARKDOWN.**
### ### **AND NO CELL MAY BE BLANK.** ### A statement with no terminal carries the honest cell
### ### "no terminal, and why" -- drawn from the refusal list, with its reason and its owning act.
### ### **A BLANK CELL WOULD READ AS "NOT YET DONE"; A REFUSAL READS AS "DECIDED AND WHY".**
"""
import io
import os
import re
import sys

ROOT = r'D:\relay'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

# ### (statement, terminal-or-refusal, axiom-print cell, grade AS ITS OWNER LEFT IT, status)
# ### ### **THE REFUSAL REASONS ARE THE DELIVERABLE, NOT AN APOLOGY FOR A MISSING ROW.**
ROWS = [
    ("THE AMBIENT PAIRING'S DEATH AT `k = n` (b270): the top-level operator's index law -- "
     "`p^n*m` lands in the ball for every column -- and the empty-orbit law beside it. "
     "### **THE INDEX CORE OF EVERY BARRIER STATEMENT IN THIS ARC.**",
     "`BallAbsorptionShadow` (15 terminals: `absorb_*` at six cells, `empty_*` at four, "
     "`live_2_2_k1` the not-dead witness, and four `refuse_*` polarity controls)",
     "each `does not depend on any axioms` -- **and this act is the one that put them IN the "
     "standing profile**: the module was never imported by `AllPrints.lean`, so its terminals "
     "were compiled at b270 and absent from `AXIOM_PRINTS.txt` ever since. Core prints 404 -> 426",
     "**REFUTED** -- C1 struck (b270's own verdict, transcribed)",
     "current"),

    ("THE FUNCTIONAL CONSEQUENCE AND ITS CONVERSE POLARITY (b271): a ball-vanishing `g` kills "
     "`SUM_m f(m) * g(p^n*m mod N)` for TWO different `f` -- because the lemma places no "
     "hypothesis on `f` at all -- and a NON-vanishing `g` gives a nonzero value.",
     "`AbsorptionFunctionalShadow` (7 terminals: `van_ones`, `van_wild`, `gVan_vanishes`, "
     "`wit_ones_ne`, `wit_wild_ne`, `gWit_not_vanishes`, `absorbed_indices_in_ball`)",
     "each `does not depend on any axioms` -- **likewise brought into the standing profile by "
     "this act**; `gWit(0) = 8` is `g_0`'s ball value `2q+2` at `(3,1)`, so the not-dead witness "
     "and the arc's escape vector are the same object",
     "**(ESCAPE)** -- scoped to ambient `E_1`, one finite level (b271's own verdict)",
     "current"),

    ("THE LOCAL SPACE CONSTRUCTED (b279): `S-bar_p` is the `L^2(Q_p)`-closure of "
     "`UNION_n iota(Son(p,n))`, the tower named by the keystone's own sentence; finite places "
     "only, `infinity` specified separately.",
     "**NO TERMINAL, AND WHY:** a completion of a directed union of subspaces is **ANALYSIS** -- "
     "there is no finite object to `decide`. The tower's one decidable instance is "
     "`TowerInstance` at `(2,1)`, which pre-dates this arc.",
     "`TowerInstance.support_ball_vanish` / `hat_ball_vanish` / `iota_isometry_integer` each "
     "`does not depend on any axioms` (banked print, `relay/data/b227_core_remeasured.txt`)",
     "**(CONSTRUCTED)** (b279's own verdict)",
     "current"),

    ("THE SPACE-LEVEL BARRIER (b280): on `S-bar_p`, at every finite place and every level, the "
     "ambient pairing's first-level value is exactly zero, so (SPEC-1) is unsatisfiable by any "
     "vector state there.",
     "**NO TERMINAL, AND WHY:** the load-bearing step `S2` -- that ball-vanishing survives the "
     "`L^2` closure because it is `ker P_{Z_p}`, the kernel of a bounded operator -- is "
     "**ANALYSIS OVER AN INFINITE-DIMENSIONAL SPACE** and is not `decide`-able. Its finite-level "
     "half is the index core two rows above.",
     "n/a -- the row's terminal cell is a refusal, not a compile",
     "**(BARRIER) at grade DERIVES**, with `S2` named as the chain's one uncompiled link "
     "(b280's own verdict and its own words)",
     "current"),

    ("THE COMPRESSION (b281): `P_S A P_S = 0` on `S-bar_p`, and the stronger `P_S A = 0` -- the "
     "left projection alone kills the operator; C2 closed by measurement, C3 the surviving shape.",
     "**NO NEW TERMINAL, AND WHY:** the decidable content IS the index core (rows above), "
     "**ALREADY COMPILED AT b270/b271**; building it again would add terminals and no knowledge. "
     "The general statement quantifies over an infinite-dimensional space.",
     "carried by `BallAbsorptionShadow` + `AbsorptionFunctionalShadow`, now in the standing "
     "profile",
     "**(COMPRESSION ZERO) at grade DERIVES** (b281's own verdict)",
     "current"),

    ("THE TOWER'S ACTION (b283): `iota` is the inclusion `V_n subset V_(n+1)` and on functions "
     "is the IDENTITY -- a filtration, not an action; it is not multiplication by `p`.",
     "**NO TERMINAL, AND WHY:** the content is a **NEGATIVE** -- that `iota` is NOT a scaling -- "
     "and a negative about the identity of two maps is not a `decide`. The positive half "
     "(`iota`'s isometry and image) is `TowerInstance`, pre-dating this arc.",
     "n/a -- refusal",
     "**(DOUBLE-NAME)** (b283's own verdict)",
     "current"),

    ("THE SCALING'S DOMAIN (b284): the genuine scaling preserves `S-bar_p` in NEITHER direction; "
     "each direction keeps one of `Son`'s two conditions and breaks the other, with the units "
     "`Z_p^x` the gap set both times. C3-via-scaling closed.",
     "**NO TERMINAL, AND WHY:** the model's realization of the scaling **IS THE ARTIFACT** -- "
     "identically zero at level 1, mostly collapsed at level 2, and wrong on one side because "
     "the wraparound folds escaped mass back in. **A COMPILE WOULD CERTIFY THE ARTIFACT AND NOT "
     "THE DERIVATION.** b284's own refusal, restated here unchanged.",
     "n/a -- refusal",
     "**(FAILS) in both directions** (b284's own verdict)",
     "current"),

    ("THE ARCHIMEDEAN OPENING AND THE SOURCE READS (b285, b286, b287): the `infinity` local space "
     "is `L^2(R)_ev` with CC's Definition 4.4's TWO conditions at cutoff `[-1,1]`, `Lambda = 1`; "
     "no finite-arc result types at `infinity`; the corpus's two banked descriptions pick out one "
     "space.",
     "**NO TERMINAL, AND WHY:** these are **READS OF AN IMPORT**. The statements are "
     "Connes-Consani's, not the corpus's, and **AN IMPORT IS NOT OURS TO COMPILE** -- a terminal "
     "would assert as kernel-verified a statement whose owner is another author.",
     "n/a -- refusal",
     "**(NAMED-NOT-CONSTRUCTED)** at b285, **(SUPPLIED BY SOURCE)** at b286, **(SAME SPACE)** at "
     "b287 to within one `TRUSTED-AT-CITE` link (each act's own verdict)",
     "current"),

    ("THE FAMILY'S INVARIANT (b288): dilation carries `S(lambda,mu)` to `S(lambda/a, a*mu)`, so "
     "the product `lambda*mu` is invariant and `S(1,1)`'s non-preservation is a statement about a "
     "TRIVIAL STABILIZER, not the absence of an action.",
     "**NO TERMINAL, AND WHY:** the parameter arithmetic IS finite-decidable -- and a terminal "
     "reading `(+1)+(-1)=0` **CERTIFIES INTEGER ADDITION AND NOTHING ABOUT THE FAMILY**, whose "
     "content is which radii those exponents name. **REFUSED ON ITS OWN MERITS**, b288's own "
     "words, not for want of decidability.",
     "n/a -- refusal",
     "**THE PRODUCT IS INVARIANT** (b288's own verdict); the reopening is filed "
     "**UNBANKED-UNTIL-TESTED** and is not a result",
     "current"),
    ("THE FINITE TWO-RADIUS FAMILY (b293): `Son(p,n; a,b)` defined in the corpus's own p-adic "
     "terms, with dimension `(p^n - p^a)(p^n - p^b)` derived; the corpus's existing space is the "
     "diagonal member `(0,0)`; dilation moves `(a,b) -> (a+1, b-1)` so the SUM is invariant; and "
     "`S` carries `(a,b)` to `(b,a)` by the corpus's own `S^2 = q^2 Pi`.",
     "**NO TERMINAL, AND WHY:** the diagonal identification and the radius arithmetic ARE "
     "finite-decidable -- and a terminal would certify the membership TEST and integer addition, "
     "not the family. **AND THE PART THAT WOULD MATTER -- the transform's behaviour -- IS THE "
     "PART THE TRUNCATION CORRUPTS**, so compiling it would certify the artifact. Refused on its "
     "own merits, not for want of decidability.",
     "n/a -- refusal. The E0 gate ran in exact rational arithmetic instead: 0 dimension "
     "mismatches at five cells, diagonal verified vector by vector in both directions with a "
     "negative control, and the collapsed condition compared to the actual transform both ways",
     "**CONSTRUCTED** (b293's own verdict). **NOTHING ABOUT THE BARRIER, THE COMPRESSION OR M-2 "
     "FOLLOWS -- a family existing is not a route existing**",
     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b289 -- THE CORRESPONDENCE TABLE, BROUGHT CURRENT.')
    print('=' * 100)
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    # ### NO BLANK CELLS -- CHECKED BEFORE ANYTHING IS WRITTEN.
    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells       : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    # ### EVERY REFUSAL MUST CARRY A REASON.
    refusals = [r for r in ROWS if 'NO TERMINAL' in r[1] or 'NO NEW TERMINAL' in r[1]]
    without = [r for r in refusals if 'AND WHY' not in r[1]]
    print('  refusal rows      : %d, of which without a stated reason: %d  %s'
          % (len(refusals), len(without), 'PASS' if not without else '### FAIL ###'))
    if without:
        return 1

    lines = []
    for k, (stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    io.open(TABLE, 'w', encoding='utf-8').write(new)

    # ### READ BACK -- the tool does not trust its own write.
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    ok = got[-len(ROWS):] == list(range(start, start + len(ROWS)))
    print('  READ BACK         : last %d row numbers are %s  %s'
          % (len(ROWS), got[-len(ROWS):], 'PASS' if ok else '### FAIL ###'))
    print('  table rows now    : %d' % len(got))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
