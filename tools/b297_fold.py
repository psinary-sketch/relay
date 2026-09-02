# -*- coding: utf-8 -*-
"""b297_fold.py -- THE FOLD, b283-b296. ### THE RUN.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### AND NO KEYSTONE IS CREATED.** ### Every bar was fixed in
### `data/b297_registration_2026-09-02.txt`, SEALED `6f7de320...`, term-scanned and
### satisfiability-checked BEFORE the seal.

### ### **THE DESIGN POINT, CARRIED FROM b266 AND b282:**
### ### **THE RESULT TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER ### EMITS ###
### ### THE MARKDOWN THE FOLD APPENDS.** ### So a quotation that fails F-QUOTE never reaches
### `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE;
### ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**

### ### **AND THE EMITTER DISCIPLINE, WHICH IS b283's SCAR:** ### every quotation below is checked
### against ### THE ACT THAT ORIGINATED IT ### , never against an act that quoted it. ### b282's
### failure was a quotation typed from memory of THIS SEAT'S OWN QUOTATION of b270 and b271.
### ### **A QUOTATION OF A QUOTATION IS NOT A SOURCE.**
"""
import io
import json
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
EMIT = os.path.join(D, 'b297_fold_emitted.md')
ROWS = os.path.join(D, 'b297_rows.json')

ARC = ['b283', 'b284', 'b285', 'b286', 'b287', 'b288', 'b289',
       'b290', 'b291', 'b292', 'b293', 'b294', 'b295', 'b296']

SRC = {
    'b283': 'b283_the_tower_action.txt',
    'b284': 'b284_the_scalings_domain.txt',
    'b285': 'b285_archimedean_opening.txt',
    'b286': 'b286_the_cc_condition.txt',
    'b287': 'b287_the_two_papers.txt',
    'b288': 'b288_the_family_and_the_complement.txt',
    'b289': 'b289_consolidation.txt',
    'b290': 'b290_the_cross_pairing_read.txt',
    'b291': 'b291_the_involution.txt',
    'b292': 'b292_the_identification.txt',
    'b293': 'b293_the_finite_family.txt',
    'b294': 'b294_the_family_value.txt',
    'b295': 'b295_the_second_mechanism.txt',
    'b296': 'b296_the_asymmetry.txt',
}

# ### THE RESULT TABLE. ### (act, what it is, the QUOTATION, the grade as its act left it)
# ### ### **EVERY QUOTATION IS CHECKED VERBATIM AGAINST `SRC[act]` BEFORE IT IS EMITTED.**
RESULTS = [
    ('b283', 'the tower map, named for what it is',
     'THE TOWER SUPPLIES A FILTRATION, NOT AN ACTION.',
     '**(DOUBLE-NAME)** -- and the act stops there; C3 keeps its original price'),
    ('b283', 'what the inclusion is not',
     '`iota` IS NOT MULTIPLICATION BY `p`.',
     'a naming error corrected, **not** a verdict moved'),

    ('b284', 'the scaling, in both directions',
     'VERDICT: (FAILS) -- IN BOTH DIRECTIONS, AND DUALLY.',
     '**(FAILS)** -- each direction preserves one condition and breaks the other'),
    ('b284', 'the leftover set, the same both times',
     'THE UNITS `Z_p^x = Z_p \\ p Z_p`',
     'the same set in both directions; b293 later named it the shell between adjacent members'),
    ('b284', 'the entailment, at exactly its scope',
     'C3-VIA-SCALING IS CLOSED.',
     '**scoped** -- and the act says in its own voice that this is *not* "C3 is closed"'),

    ('b285', 'the archimedean space, as the corpus holds it',
     'VERDICT ON THE SPACE: (NAMED-NOT-CONSTRUCTED).',
     '**(NAMED-NOT-CONSTRUCTED)** -- an explicit open mark in the corpus\u2019s own register'),
    ('b285', 'the typing question, answered plainly',
     'NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`.',
     '**the arc\u2019s standing boundary** -- carried by every act after it'),

    ('b286', 'the condition, supplied by the source itself',
     'VERDICT ON `N-OPEN-A`: (SUPPLIED BY SOURCE).',
     '**(SUPPLIED BY SOURCE)** -- an import, graded as one'),
    ('b286', 'the space and its cutoff, read at content',
     'THE SPACE IS `L^2(R)_ev`.',
     'two conditions, cutoff `[-1,1]` at `Lambda = 1`; **nothing adopted**'),
    ('b286', 'the sentence nobody went looking for',
     'the scaling action `theta` DOES NOT RESTRICT to this subspace',
     'the source records at `\u221e` the structural fact b284 derived independently at `p`'),

    ('b287', 'the two descriptions',
     'VERDICT: (SAME SPACE), DERIVED -- TO WITHIN ONE NAMED AND GRADED LINK.',
     '**(SAME SPACE)** -- derived from the source\u2019s own section 4, not from the shared name'),

    ('b288', 'the archimedean family under dilation',
     'COMPONENT 1 -- VERDICT: THE PRODUCT IS INVARIANT.',
     '**INVARIANT** -- the dilation is a flow on the product\u2019s level sets'),
    ('b288', 'what non-preservation actually says',
     'STABILIZER IS TRIVIAL',
     'a **stabilizer** statement, not the absence of an action'),

    ('b289', 'the verification layer, audited',
     "THE ARC'S OWN SHADOWS WERE COMPILED AND WERE NOT IN THE STANDING PROFILE.",
     '**a correction to a fact about the kernel**, not to any act\u2019s verdict'),
    ('b289', 'the repair, as a count any later act can re-run',
     'CORE PRINTS 404 -> 426, ALL 426 ZERO-AXIOM.',
     '**REPAIRED** -- and `W-ORD-PRINT-COVERAGE` filed for the 25 modules still outside'),

    ('b290', 'the first obligation, undischarged',
     'FIRST READ -- VERDICT: (ABSENT), WITH A RELATED-BUT-DIFFERENT FACT QUOTED.',
     '**(ABSENT)** -- the absence put on the record rather than left unsearched'),
    ('b290', 'the second, and why it did not promote',
     'SECOND READ -- VERDICT: (PARTIAL).',
     '**(PARTIAL)** -- the swap needs a step the source *uses* and does not *state*'),

    ('b291', 'the step b290 could not reach, in the source\u2019s own words',
     'In `L^2(R)_ev` the Fourier transform `F_eR` is its own inverse.',
     '**stated in plain English**, where b290\u2019s search looked for symbols'),
    ('b291', 'the reflection, promoted',
     '`F_eR : S(lambda,mu) -> S(mu,lambda)`',
     '**DERIVES-on-IMPORT** -- the import being the source\u2019s own sentence above'),
    ('b291', 'the object\u2019s own member',
     "(ii) THE CORPUS'S ARCHIMEDEAN MEMBER IS SELF-DUAL.",
     'immediate from the reflection at `lambda = mu = 1`'),
    ('b291', 'the second paired family',
     'COMPONENT 3 -- THE CROSS-PAIRING: ### (REFUTED).',
     '**(REFUTED)** -- it is not in the Sonin space'),

    ('b292', 'the identification',
     'VERDICT: (SAME OBJECT), UP TO A NONZERO SCALAR',
     '**(SAME OBJECT)** -- two defining equations that are one equation in two notations'),
    ('b292', 'what the identification carries into the corpus',
     '`zeta_n` IS NOT IN `S(1,1)`',
     'b291\u2019s refutation reaches the corpus\u2019s own instruments'),
    ('b292', 'and what it does not carry',
     'AND NO MEASUREMENT IS DISTURBED.',
     '**no measurement disturbed** -- the vectors sit outside the space, and every number stands'),

    ('b293', 'the finite family',
     'THE FAMILY IS CONSTRUCTED.',
     '**CONSTRUCTED** in the corpus\u2019s own `p`-adic terms'),
    ('b293', 'its dimension law',
     'DIMENSION `(p^n - p^a)(p^n - p^b)`, DERIVED AND VERIFIED WITH ZERO MISMATCHES.',
     '**DERIVED**, and at `a = b = 0` it is the keystone\u2019s own `(p^n-1)^2`'),
    ('b293', 'the object as the family\u2019s diagonal',
     'CHECKED VECTOR BY VECTOR',
     'set equality **both directions**, with a negative control that rejects an off-ball spike'),
    ('b293', 'the invariant under scaling',
     'THE SUM `a+b` IS INVARIANT',
     '**DERIVED** from the corpus\u2019s own conditions; the archimedean analogue is named, never used'),
    ('b293', 'and the standing sentence the act put on itself',
     'THE FAMILY EXISTS.',
     'a family existing is **not** a route existing; **M-2 untouched**'),

    ('b294', 'the grid, computed',
     "THE BARRIER'S ZERO IS A PROPERTY OF A SUB-FAMILY, NOT OF THE WHOLE FAMILY.",
     '**the twenty measurements stand and are reproduced exactly at b295.** '
     'Its *member-level reading* of them was corrected at b295 -- '
     '**a correction to a fact, not a re-verdict**'),

    ('b295', 'the level split',
     'AT LEVEL 1 IT GIVES ZERO AND HERE IS THE MECHANISM',
     '**DERIVED** at level 1; above it there was no zero to explain'),
    ('b295', 'the criterion, as sufficiency',
     '`a >= 0`  ###  OR  ###  `b >= n - 1`',
     '**DERIVED** -- vanishing as a *form*, both slots, at every finite place and level'),

    ('b296', 'the threshold, and where it comes from',
     'THE THRESHOLD FALLS OUT',
     '**DERIVED, not fitted** -- measured with no reference to `b`, both polarities, 6 of 6 cells'),
    ('b296', 'the asymmetry, as one rule returning two numbers',
     'EACH THRESHOLD IS THE DISTANCE FROM',
     'distance `0` on the function side, `n-1` on the transform side; '
     '**b281\u2019s `A != A^T` turned into a number**'),
    ('b296', 'the criterion, closed',
     'IF AND ONLY IF',
     '**EQUIVALENCE** -- necessity witnessed by one vector per cell'),
    ('b296', 'the consequence for the object\u2019s own space',
     'THE ANNIHILATION IS ONE-SIDED',
     'the function-side condition does the work at every level; **above level 1 the '
     'object\u2019s second condition contributes nothing to this pairing**'),
]

# ### THE CORRECTIONS THIS ARC MADE TO ITS OWN EARLIER READINGS.
# ### ### **EACH IS A CORRECTION TO A FACT. ### NONE IS A RE-VERDICT, AND THE COLUMN SAYS SO.**
CORRECTIONS = [
    ('b290 -> b291', 'the search FORM, not the search depth',
     'b290 searched for the involutivity in symbolic forms and recorded it used-not-stated; '
     'the source says it in one plain English sentence, immediately after equation (69).',
     'b290\u2019s **(PARTIAL)** stands. What changed is that the missing step was **found**.'),
    ('b294 -> b295', 'a reading of its own measurement',
     'b294 answered "does this member give zero?" from `<A v, v>` on one basis and reported ZERO '
     'on 10 of 10. The form is neither Hermitian nor symmetric (b281), so a diagonal on a basis '
     'does not decide a span: `Son(2,2; -1,0)` contains a vector with value `4/3`.',
     '**b294\u2019s twenty measurements are reproduced exactly.** Only the step from '
     '"every basis vector pairs to zero" to "the member gives zero" is corrected.'),
    ('the arc -> b289', 'a fact about the verification layer',
     'Two shadows built and printed by their own acts were never imported by `AllPrints.lean`, '
     'so the certification file had never carried them.',
     'No act\u2019s verdict moved. **The kernel\u2019s print count did: 404 to 426.**'),
    ('b289 -> b293', 'a filings tool that could not be re-run safely',
     'b289\u2019s correspondence tool held the whole arc\u2019s rows, so re-running it appended '
     'all nine again and the table went to 113 rows with 95-103 duplicated.',
     'Caught on the read-back, restored from `git`, and every tool since carries an '
     '**idempotence guard**. `W-ORD-CORRESPONDENCE-IDEMPOTENCE`.'),
]


def fquote(text_by_act, rec):
    """### **F-QUOTE, WITH ITS DISCRIMINATION ARM.** ### A matcher that never misses is not
    ### matching, so an ALTERED quotation is fed to the same matcher and must come back
    ### unfindable."""
    bad = []
    for act, what, quote, _grade in RESULTS:
        if quote not in text_by_act[act]:
            bad.append((act, what, quote))
    rec('  F-QUOTE  : %d quotations, %d unfindable' % (len(RESULTS), len(bad)))
    for act, what, quote in bad:
        rec('      ### UNFINDABLE  %s -- %s' % (act, quote[:70]))
    # ### THE DISCRIMINATION CONTROL.
    act0, _w, q0, _g = RESULTS[0]
    altered = q0.replace('FILTRATION', 'FILTRATIONN')
    disc = altered not in text_by_act[act0]
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fcount(rec):
    covered = sorted({a for a, _w, _q, _g in RESULTS}, key=lambda s: int(s[1:]))
    ok = covered == ARC
    rec('  F-COUNT  : acts covered %d, arc %d, exact match : %s' % (len(covered), len(ARC), ok))
    if not ok:
        rec('      ### covered : %s' % covered)
        rec('      ### arc     : %s' % ARC)
        rec('      ### missing : %s' % [a for a in ARC if a not in covered])
        rec('      ### extra   : %s' % [a for a in covered if a not in ARC])
    return ok


def emit_markdown():
    L = []
    A = L.append
    A('## THE M-2 CAMPAIGN, b283\u2013b296 \u2014 THE FOLD')
    A('')
    A('*Filed b297, 2026-09-02. Fourteen acts. ### **NO GRADE MOVED. NO ACT RE-VERDICTED. NO NEW')
    A('MATHEMATICS. NO KEYSTONE CREATED.** Every result below is a **quotation**, verified verbatim')
    A('against its owning act\u2019s own file by the runner that **generated this table** \u2014')
    A('`relay/tools/b297_fold.py`. A check that runs after the writing can only report a')
    A('paraphrase; one that generates the writing cannot emit one. ### **%d quotations, 0'
      % len(RESULTS))
    A('unfindable, and the checker discriminates:** a deliberately altered quotation is reported')
    A('unfindable, because a matcher that never misses is not matching. ### **Every quotation is')
    A('checked against the act that ORIGINATED it, never against an act that quoted it** \u2014')
    A('b283\u2019s scar, and a quotation of a quotation is not a source.*')
    A('')
    A('### The arc, as one statement')
    A('')
    A('### **THE OBJECT\u2019S TWO DEFINING CONDITIONS ARE NOT READ THE SAME WAY BY THE OPERATOR')
    A('THAT ANNIHILATES IT.** The first-level pairing reads its second slot by pointwise')
    A('evaluation on the ball, and its first slot only through fiber sums one step coarser than')
    A('pointwise. So the pairing vanishes identically on `Son(p,n; a,b)` **if and only if**')
    A('`a >= 0` **or** `b >= n-1` \u2014 the function-side threshold fixed at the object\u2019s own')
    A('radius, the transform-side threshold moving with the level. ### **ON THE OBJECT\u2019S OWN')
    A('SPACE THE ANNIHILATION IS THEREFORE ONE-SIDED: above level 1 its second condition')
    A('contributes nothing to this pairing.**')
    A('')
    A('**The scope, printed beside it and not beneath it:**')
    A('')
    A('- ### **FINITE PLACES ONLY, AND THE BOUNDARY IS THE ARC\u2019S OWN FINDING.** b285:')
    A('  *"NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`."* The archimedean space is')
    A('  **(NAMED-NOT-CONSTRUCTED)** in the corpus\u2019s own register. ### **NOTHING ABOVE')
    A('  REACHES IT.**')
    A('- ### **THIS IS A STATEMENT ABOUT ONE PAIRING** \u2014 b273\u2019s `A` at `k = n`, at one')
    A('  level. It says nothing about what the object\u2019s second condition does for any other')
    A('  purpose, of which this arc tested none.')
    A('- ### **NO ROUTE IS CLAIMED, AND THE FAMILY IS NOT ONE.** b293: *"THE FAMILY EXISTS."* \u2014')
    A('  and a family existing is not a route existing. Every member carrying a nonzero value')
    A('  **weakens the object\u2019s FIRST condition**, and every witness has **mass on the ball**,')
    A('  which that condition forbids outright. ### **THE NONZERO LIVES IN THE PART THAT IS NOT')
    A('  THE OBJECT.**')
    A('- ### **C3-VIA-SCALING IS CLOSED (b284) \u2014 WHICH IS NOT "C3 IS CLOSED".** C3 remains')
    A('  open by every route that act did not test.')
    A('- ### **M-2 REMAINS (SPECIFIED-NOT-STATED).** Untouched by all fourteen acts.')
    A('- b15\u2019s standing clause governs: *"a finite-place-set object at a finite cutoff decides')
    A('  nothing"* globally.')
    A('')
    A('### The results, quoted')
    A('')
    A('| act | result | quoted from its owning act | grade as its act left it |')
    A('|:--|:--|:--|:--|')
    for act, what, quote, grade in RESULTS:
        A('| **%s** | %s | *"%s"* | %s |' % (act, what, quote.replace('|', '\\|'), grade))
    A('')
    A('### The corrections this arc made to its own readings')
    A('')
    A('*### **EACH IS A CORRECTION TO A FACT. ### NONE IS A RE-VERDICT.** The distinction is the')
    A('whole of this table: a measurement that stands, with a sentence about it that did not.*')
    A('')
    A('| where | what kind | what was corrected | what did **not** move |')
    A('|:--|:--|:--|:--|')
    for where, kind, what, notmoved in CORRECTIONS:
        A('| **%s** | %s | %s | %s |' % (where, kind, what, notmoved))
    A('')
    A('### The kernel plan \u2014 filed, and NOT built')
    A('')
    A('*Two tests, and a candidate must pass **both**: is it **finite-decidable**, and can a')
    A("terminal's own statement **carry its own scope**? ### **A TRUE STATEMENT IS NOT COMPILED")
    A('WHEN THE MEDIUM CANNOT HOLD THE SENTENCE THAT BOUNDS IT.** `0` `.lean` files moved by this')
    A('act.*')
    A('')
    A('| candidate | finite-decidable? | carries its own scope? | verdict |')
    A('|:--|:--|:--|:--|')
    A('| the family\u2019s definition and dimension law (b293) | **yes** \u2014 exact rank arithmetic '
      'at a named cell | **no** \u2014 a terminal certifying `dim = (p^n-p^a)(p^n-p^b)` at one cell '
      'reads as the law, which is a statement over all levels | **REFUSED** |')
    A('| the diagonal identification as set equality, both directions (b293) | **yes** \u2014 a '
      'membership test with a negative control | **no** \u2014 it would certify that a rational test '
      'agrees with itself at one cell, not that the object is the family\u2019s diagonal | '
      '**REFUSED** |')
    A('| the function-side annihilation, as the index-landing argument (b270, b280) | **yes** at a '
      'cell; the argument itself is **not** \u2014 it quantifies over all levels and places | '
      '**partly** \u2014 the index-landing step is self-contained, and it is **already compiled** '
      '(`BallAbsorptionShadow`, imported and printing since b289) | **ALREADY BUILT; nothing to '
      'add** |')
    A('| the transform-side annihilation, as the fiber-sum collapse (b293, b296) | **yes** at a '
      'cell | **no** \u2014 a terminal reading "the smallest modulus is `p^{2n-1}`" would sit in the '
      'kernel looking like a statement about the operator at every level | **REFUSED** |')
    A('| **the existence statement on a relaxed member** \u2014 that `Son(2,2; -1,0)` contains a '
      'vector of value `4/3` (b295, b296) | **yes** \u2014 one membership test and one exact '
      'rational | ### **YES, AND IT IS THE ONLY ONE THAT DOES** \u2014 a terminal that **names the '
      'member in its own statement** carries the scope inherently, whereas a bare value does not | '
      '**THE ONE CANDIDATE THAT PASSES BOTH TESTS.** Filed, not built. |')
    A('')
    A('**The refusals, with their reasons \u2014 listed, not omitted:**')
    A('')
    A('- ### **EVERYTHING ANALYSIS-BOUND.** b280\u2019s `S2` closure step \u2014 that ball-vanishing')
    A('  survives the `L\u00b2` closure because it is `ker P_{Z_p}` \u2014 is standard analysis and')
    A('  is **not** machine-verified. It is the chain\u2019s one uncompiled link, and it is')
    A('  unchanged by this arc.')
    A('- ### **EVERYTHING EXPOSED TO THE MODEL\u2019S ESCAPED-MASS ARTIFACT.** b284 established')
    A('  that one scaling direction\u2019s genuine image **escapes the level**, and that the')
    A('  model\u2019s wraparound is exactly that escaped mass folded back in. b293 met it a second')
    A('  time. ### **A COMPILED TERMINAL OVER THE TRUNCATED MODEL WOULD CERTIFY THE TRUNCATION')
    A('  AND CARRY THE OBJECT\u2019S NAME.** Refused on that ground alone.')
    A('- ### **EVERY STATEMENT QUANTIFYING OVER ALL LEVELS AND PLACES**, which is most of the')
    A('  arc\u2019s content, including the equivalence itself.')
    A('')
    A('**Where these terminals would sit, if the author calls the build:**')
    A('')
    A('### **INSIDE THE EXISTING KERNEL\u2019S `Core`, WITH CORRESPONDENCE ROWS LINKING THEM TO THE')
    A('BARRIER TERMINALS \u2014 NOT A NEW REPOSITORY.** The reason is a rule and not a preference:')
    A('### **A LANE EARNS A REPOSITORY WHEN IT BECOMES INDEPENDENT, AND THIS LANE IS THE IDENTITY')
    A('CHAIN\u2019S OWN.** Any new module would be imported by `AllPrints.lean` in the same commit')
    A('that creates it \u2014 b289\u2019s scar, where two shadows sat outside the certification file')
    A('for eleven acts.')
    A('')
    A('### The keystone material \u2014 assembled, and NOT written')
    A('')
    A('### **NOTHING IN THIS SECTION IS A KEYSTONE, AND NO KEYSTONE IS PROPOSED.** The')
    A('new-keystone question is **the author\u2019s**. What follows is material for that decision')
    A('and nothing else: no title is named, no draft exists, and no register row is written.')
    A('')
    A('**The objects this arc produced that are not amendments to existing statements:**')
    A('')
    A('| object | owning act | the sentence that places it |')
    A('|:--|:--|:--|')
    A('| the finite two-radius family `Son(p,n; a,b)`, with its dimension law and its verified '
      'diagonal | b293 | A corpus object with a derived law. **It sits under the register '
      'sentence and below the deposit\u2019s ceiling: it decides nothing about `h2`, and a family '
      'existing is not a route existing.** |')
    A('| the annihilation criterion as an equivalence, with its threshold derived from the '
      'operator\u2019s reading scale | b295, b296 | A statement about **one pairing of one shape at '
      'the finite places**. **It sits under the register sentence and below the deposit\u2019s '
      'ceiling: it adds an obstruction and removes none.** |')
    A('| the one-sidedness of the annihilation on the object\u2019s own space | b296 | A '
      'consequence of the above, **measured** on two spaces built outside the family\u2019s index '
      'range. **Same ceiling; it says nothing about the object beyond this pairing.** |')
    A('| the identification of the corpus\u2019s archimedean instrument vectors with the '
      'source\u2019s, and their exclusion from the object\u2019s space | b291, b292 | An import and '
      'a derivation on it. **No measurement is disturbed**, and **b285\u2019s typing verdict means '
      'no finite-side fact travels there.** |')
    A('')
    A('**The cross-reference rows existing keystones would gain \u2014 listed, and NOT written:**')
    A('')
    A('- `THE_GLOBAL_SECTION.md` \u2014 a row against its `Son(p,n)` clause noting that the space')
    A('  is the **diagonal member** of a two-radius family (b293), and that its two conditions are')
    A('  **not symmetric** for the first-level pairing (b296).')
    A('- `THE_IDENTITY_CHAIN.md` \u2014 a row against the barrier terminals noting that the')
    A('  criterion is now an **equivalence** (b295, b296), and that the barrier\u2019s zero belongs')
    A('  to a sub-family (b294, as corrected at b295).')
    A('- ### **NEITHER ROW IS WRITTEN BY THIS ACT.** Listing is not writing.')
    A('')
    A('### **THE STANDING SENTENCE, RESTATED BECAUSE IT GOVERNS WHATEVER THE AUTHOR DECIDES:**')
    A('support-voice documents are **amended with the originals visible**; deposited texts move')
    A('**only by errata and a new version**. ### **NOTHING HERE DEPOSITS, AND NOTHING HERE')
    A('CIRCULATES.**')
    A('')
    A('### The desk')
    A('')
    A('- ### **M-2 \u2014 SPECIFIED-NOT-STATED.** Unchanged by all fourteen acts. C3 remains open')
    A('  by every route b284 did not test; **C3-via-scaling is closed and that is not the same')
    A('  sentence.**')
    A('- ### **THE TWO LIVE DIRECTIONS.** (1) **The kernel build** \u2014 one candidate passes both')
    A('  tests (the existence statement on a relaxed member); the author\u2019s call. (2) **The')
    A('  new-keystone question** \u2014 material assembled above; **the author\u2019s alone.**')
    A('- ### **`W-ORD-PRINT-COVERAGE` \u2014 STILL FILED, STILL NOT RUN.** 25 `Core` modules sit')
    A('  outside the certification file. The risk is not the labour but that a sweep may find a')
    A('  terminal sitting uncertified whose print is not zero axioms. **b289 found exactly that')
    A('  species twice.**')
    A('- `W-ORD-READING-SCALE-GENERAL` \u2014 the reading scale `2n-1` is derived and measured at')
    A('  six cells; the two are **not shown to agree outside them**.')
    A('- `W-ORD-DIAGONAL-VS-FORM-SWEEP` \u2014 three named per-basis-vector checks (b284, b288,')
    A('  b293) have **not** been re-read on the full form.')
    A('- `W-ORD-FAMILY-REOPENING` \u2014 criterion (i) met at b293; (ii) and (iii) **unmet**.')
    A('  **Unbanked-until-tested.**')
    A('- `W-ORD-CC-LOCAL-COPY` \u2014 a local copy of the source exists as a tool artifact outside')
    A('  the repositories. **Not copied in; a third-party paper is not ours to redistribute.**')
    A('  Where it should live is the author\u2019s ruling.')
    A('- `W-ORD-FIBER-GENERAL`; `W-ORD-TQ-IDENTIFY`; `W-ORD-CN-LAW`; b262\u2019s PNT-plus-saddle')
    A('  \u2014 carried, unpaid, untouched by this arc.')
    A('- **The seam\u2019s debt item 1** \u2014 **still unpaid.** Restated, not discharged, not')
    A('  renegotiated.')
    A('- The **ERRATA partition question** (b266) \u2014 open.')
    A('- The **REGISTRY / README / SPIRAL_MAP reconciliation** \u2014 open.')
    A('- The **patent lane** \u2014 carried on the patent seat\u2019s report, not here.')
    A('')
    A('### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**')
    A('')
    return '\n'.join(L)


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b297 -- THE FOLD, b283-b296. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)

    text_by_act = {}
    for act in ARC:
        p = os.path.join(D, SRC[act])
        text_by_act[act] = io.open(p, encoding='utf-8').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)'
        % len(text_by_act))

    ok_q = fquote(text_by_act, rec)
    ok_c = fcount(rec)

    # ### F-NOSHADOW -- nothing is built by a filings act.
    lean = subprocess.run(['git', '-C', ROOT, 'status', '--short', '--', '*.lean'],
                          capture_output=True, text=True).stdout.strip()
    ok_s = (lean == '')
    rec('  F-NOSHADOW: `.lean` files touched : %d' % (0 if ok_s else len(lean.splitlines())))

    if not (ok_q and ok_c):
        rec('')
        rec('  ### ### **NOTHING EMITTED. ### A GATE FIRED AND THE DOCUMENT IS NOT WRITTEN.**')
        rec('=' * 100)
        return 1

    md = emit_markdown()
    io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md)
    rec('  emitted markdown : %s  (%d lines)' % (EMIT, len(md.splitlines())))

    # ### APPEND TO FINDINGS.md -- ADDITIVELY, AND NOTHING ABOVE IT IS TOUCHED.
    cur = io.open(FINDINGS, encoding='utf-8').read()
    if 'THE M-2 CAMPAIGN, b283\u2013b296' in cur:
        rec('  ### SECTION ALREADY PRESENT -- FINDINGS.md NOT WRITTEN (idempotence guard).')
    else:
        io.open(FINDINGS, 'w', encoding='utf-8', newline='\n').write(
            cur.rstrip('\n') + '\n\n' + md)
        rec('  FINDINGS.md : section appended')

    # ### F-NOGRADE -- PURELY ADDITIVE, MEASURED AND NOT ASSERTED.
    p = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', 'FINDINGS.md'],
                       capture_output=True, text=True)
    added = removed = 0
    if p.stdout.strip():
        parts = p.stdout.split()
        added, removed = int(parts[0]), int(parts[1])
    ok_g = (removed == 0)
    rec('  FINDINGS.md vs HEAD : ### **+%d / -%d**' % (added, removed))
    rec('  ### ### **F-NOGRADE %s**'
        % ('DID NOT FIRE -- no line deleted, no tag rewritten; the change is PURELY ADDITIVE.'
           if ok_g else 'FIRED. ### A LINE WAS DELETED OR REWRITTEN.'))

    # ### F-NOKEYSTONE -- count files written under any keystone path.
    ks = subprocess.run(['git', '-C', PP, 'status', '--short'],
                        capture_output=True, text=True).stdout.strip().splitlines()
    kpaths = [l for l in ks if 'keystone' in l.lower() or '/method/' in l.replace('\\', '/')]
    ok_k = (len(kpaths) == 0)
    rec('  F-NOKEYSTONE: files touched under a keystone path : %d  %s'
        % (len(kpaths), 'PASS' if ok_k else '### FAIL ### %s' % kpaths))

    rec('')
    rec('=' * 100)
    rec('  F-QUOTE      (results verbatim)   : ### **%s**' % ('DID NOT FIRE' if ok_q else 'FIRED'))
    rec('  F-COUNT      (arc reconciles)     : ### **%s**' % ('DID NOT FIRE' if ok_c else 'FIRED'))
    rec('  F-NOGRADE    (purely additive)    : ### **%s**' % ('DID NOT FIRE' if ok_g else 'FIRED'))
    rec('  F-NOKEYSTONE (no keystone made)   : ### **%s**' % ('DID NOT FIRE' if ok_k else 'FIRED'))
    rec('  F-NOSHADOW   (nothing built)      : ### **%s**' % ('DID NOT FIRE' if ok_s else 'FIRED'))
    rec('=' * 100)

    json.dump(dict(arc=ARC, results=len(RESULTS), corrections=len(CORRECTIONS),
                   findings_added=added, findings_removed=removed,
                   f_quote=ok_q, f_count=ok_c, f_nograde=ok_g,
                   f_nokeystone=ok_k, f_noshadow=ok_s),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    with io.open(os.path.join(D, 'b297_fold_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if (ok_q and ok_c and ok_g and ok_k and ok_s) else 1


if __name__ == '__main__':
    sys.exit(main())
