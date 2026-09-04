# -*- coding: utf-8 -*-
"""b323_fold.py -- THE FOLD, b314-b322. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED.**

### ### **THE DESIGN POINT, CARRIED FROM b266, b282, b297, b307 AND b314:**
### ### **THE RESULT TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER ### EMITS ### THE
### ### MARKDOWN THE FOLD APPENDS.** ### A quotation that fails `F-QUOTE` never reaches
### `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE;
### ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**

### ### **AND THE EMITTER DISCIPLINE, WHICH IS b283's SCAR:** ### every quotation is checked against
### ### THE ACT THAT ORIGINATED IT ### , never against an act that quoted it. ### **A QUOTATION OF A
### ### QUOTATION IS NOT A SOURCE.**
### ### **THE MECHANICAL CHECK IS `in the originating file`; THE JUDGEMENT -- that the sentence is
### that act's OWN VOICE and not material it was itself quoting -- IS THE SEAT'S, AND IS DECLARED
### AS THE SEAT'S IN THE BANK.**

### ### ### **ONE THING IS NEW IN THIS FOLD AND IT IS NOT A PLEASANT ONE: ### A TABLE OF SEALED
### ### BARS FOUND DEFECTIVE.** ### Three acts in this arc sealed a bar before any value and then
### found the bar itself wrong -- b319's reach bar, and both of b322's. ### **A RECORD WHOSE
### ### REGISTRATIONS ARE ONLY EVER REPORTED AS HAVING WORKED IS A RECORD THAT HAS STOPPED READING
### ### THEM**, so the defects get their own table beside the corrections.
"""
import io
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
EMIT = os.path.join(D, 'b323_fold_emitted.md')
ROWS = os.path.join(D, 'b323_fold_rows.json')

ARC = ['b314', 'b315', 'b316', 'b317', 'b318', 'b319', 'b320', 'b321', 'b322']

SRC = {
    'b314': 'b314_the_fold_and_the_cold_clone.txt',
    'b315': 'b315_the_calibration_and_the_rate.txt',
    'b316': 'b316_the_archimedean_instrument.txt',
    'b317': 'b317_the_trace_on_the_object.txt',
    'b318': 'b318_the_forced_sign.txt',
    'b319': 'b319_the_stable_rank.txt',
    'b320': 'b320_the_lawful_function.txt',
    'b321': 'b321_the_window_opened.txt',
    'b322': 'b322_the_membership.txt',
}

SECTION = 'THE ARCHIMEDEAN INSTRUMENT ARC, b314\u2013b322 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE SCOPE SENTENCE)
RESULTS = [
    ('b314', 'the prior fold filed, and the kernel rebuilt by something that inherited nothing',
     'BYTE-FOR-BYTE EQUAL TO THE BANKED BLOB',
     'FILED \u2014 a filings act and a cold-clone certification; no grade moved',
     'The clone certifies that the profile regenerates from source under a pinned toolchain. It '
     'certifies nothing about whether the profile covers the corpus, and the same act found that '
     'it does not.'),
    ('b315', 'the calibration read, and the rate re-derived under the source\u2019s exponent',
     'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED',
     'CORRECTED AT THE READING \u2014 a reading corrected, no banked number called wrong',
     'One name had been carrying two objects. The correction is to the reading and not to any '
     'value; every banked number survived and the wording did not.'),
    ('b316', 'the archimedean instrument, built from the source\u2019s Definition 4.4 and nothing '
     'else',
     'THE INSTRUMENT EXISTS',
     'BUILT \u2014 an instrument and its controls; one negative result, no first-level value',
     'A computable truncation of `S(1,1)` at the source\u2019s own parameters. It is a finite '
     'section and the act does not claim the source\u2019s eigenspace has been computed.'),
    ('b317', 'the first archimedean trace computed on the object\u2019s own space',
     'THE NUMBER EXISTS',
     'MEASURED \u2014 the number exists; the registered prediction NOT confirmed',
     'The number is a trace on a truncated space at thirteen banked cells. The prediction it was '
     'measured against rests on a five-link chain and one link is measured false.'),
    ('b318', 'the sign of the trace side forced, and the corpus\u2019s window typed',
     'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT',
     'MEASURED, AND ONE DEFINITIONAL READING \u2014 no unit adopted, no act re-verdicted',
     'The nonnegativity is arithmetic \u2014 a sum of squares of floats with no subtraction \u2014 '
     'and is kept apart from any claim about the positivity of the operator.'),
    ('b319', 'the subspace by the source\u2019s eigenvalue-one characterization, and the '
     'kernel-coverage repair',
     'THE KERNEL-COVERAGE DEFECT IS DISCHARGED',
     'BUILT, AND ONE DEFECT DISCHARGED \u2014 a rank that holds still; no grade moved',
     'A rank that holds still is not convergence. The grid half of the reach is attained and the '
     'domain half is not, and the coverage repair proves nothing mathematical.'),
    ('b320', 'both sides of the source\u2019s Theorem 1, computed and checked where it covers',
     '27 OF 27 FRAMES',
     'HOLDS \u2014 the instrument certified against one theorem, at exactly that scope',
     'A control that holds certifies the INSTRUMENT and not the object. The sign of every margin '
     'is certified at every frame; the SIZE of none is.'),
    ('b321', 'two further theorems as controls, and the window opened on lawful objects',
     'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER',
     'HOLDS ON BOTH \u2014 three theorems now; the window reported and interpreted by nobody',
     'A finite window at a finite cutoff decides nothing global: 10000 ordinates, eleven primes, '
     'thirteen cells of one family, against a criterion that quantifies over every lawful `g`.'),
    ('b322', 'the unit\u2019s membership residual given a rate, and the leg priced',
     'THE RESIDUAL FALLS, AT EVERY STEP OF THE DOMAIN LADDER',
     'UNDER-RESOLVED, WITH ITS PRICE \u2014 no unit adopted or replaced',
     'A falling course at five frames is a falling course at five frames. The noise-floor gate '
     'refuses every step, so the DIRECTION is reported and the SIZE of no value on the ladder is.'),
]

# ### (act, THE OBSTACLE, QUOTED FROM THAT ACT)
OBSTACLES = [
    ('b314', 'MODULES SIT OUTSIDE THE CERTIFICATION FILE, ALL 25 ELABORATE, AND 91'),
    ('b315', "UNDER THE SOURCE'S EXPONENT THE ENVELOPE BECOMES A CONSTANT"),
    ('b316', "b300's MEMBERSHIP IS NOT CONFIRMED"),
    ('b317', 'A NUMBER THAT LANDS WHERE A BROKEN CHAIN SAID'),
    ('b318', "THE CORPUS'S WINDOW IS A CANDIDATE"),
    ('b319', 'THE BAR THIS ACT SEALED IS DEFECTIVE'),
    ('b320', "FIRST REPORTED VERDICT WAS `FAILS`"),
    ('b321', 'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE'),
    ('b322', "SO THE VERDICT IS `UNDER-RESOLVED`, AND IT CARRIES ITS PRICE"),
]

# ### (act, what was corrected, WHAT DID NOT MOVE)
CORRECTIONS = [
    ('b315', 'one name had been carrying two objects \u2014 the `E2` of the calibration bracket is '
     'not the archimedean remainder', 'no banked value; the correction is to a reading'),
    ('b317', 'the cancellation was read as the compression\u2019s and is the test function\u2019s '
     '\u2014 the same compression removes 98.6% of one bump and 55% of another',
     'the trace values, which stand at their own frames'),
    ('b318', 'the corpus\u2019s window was being offered as the source\u2019s test function; it is '
     'a candidate seed, not a candidate product',
     'no act re-verdicted; b317\u2019s numbers stand on b317\u2019s cut'),
    ('b320', 'b319\u2019s prose named `69` as a dimension where its own table calls it a rank \u2014 '
     'filed against that bank, not edited into it',
     'b319\u2019s table, its numbers, and its verdict'),
    ('b321', 'the window\u2019s non-positive count was on its way to being reported as arithmetic '
     'evidence; the act established it was forced by construction before printing it',
     'the numbers, which are exactly minus the zero side'),
    ('b322', 'b316\u2019s taper dichotomy was imported into a sealed bar as though it exhausted '
     'the possibilities', 'b316\u2019s diagnostic, which measures what it measures'),
]

# ### (act, the bar, what was wrong with it, what the act did about it)
DEFECTIVE_BARS = [
    ('b319', '`(B3)`, the reach bar', 'it required the rank CONSTANT on BOTH axes, which on the '
     'domain axis is unsatisfiable by the nature of the object \u2014 a longer domain is a bigger '
     'space',
     'reported the reach EMPTY under the bar as written, named the defect, and proposed the fix '
     'as a PROPOSAL for the next act rather than editing a sealed file'),
    ('b322', '`(B2)`, the edge diagnostic', 'the two labels it imported do not partition the '
     'possibilities \u2014 the taper smooths the discontinuity at the domain\u2019s end and does '
     'not restore the mass beyond it',
     'reported the verdict as the bar computes it and named the defect beside it'),
    ('b322', '`(B5)`, the branch rule', 'its branches are not mutually exclusive \u2014 two fired '
     'at once and the seal did not order them, so the runner\u2019s `if/elif` chain imposed an '
     'ordering the registration never stated',
     'took the WEAKER of the two branches, on the ground that between two branches a defective '
     'rule licenses equally an act may not help itself to the stronger one'),
]

# ### THE LORE. ### (rule, the incident that bought it, MECHANIZED or JUDGEMENT)
LORE = [
    ('Check normalizations before counts.',
     'three sealed predictions in the prior arc each got the object right and the normalizing '
     'factor wrong; b313\u2019s order put the check first and it found something.', 'MECHANIZED'),
    ('A check evaluated at a zero cannot see a factor.',
     'the archimedean control was passing at a point where both sides vanish.', 'MECHANIZED'),
    ('One identity, two conventions, one file.',
     'b313 built flipped COPIES of three instruments rather than editing the owners, and b322 '
     'could therefore still read both.', 'MECHANIZED'),
    ('A computation that matters gets a second route sharing no code before its first number is '
     'banked.',
     'b320 built the archimedean distribution by one route with good fixtures; TWO defects passed '
     'TWO rounds of those fixtures, the first producing a FAILS verdict and the second `1.9e9` in '
     'a data table.', 'MECHANIZED'),
    ('Two quadratures over one integrand are a limit, not a corroboration \u2014 and must be '
     'called one before the value exists.',
     'b322 declared it in `(B1d)`: there is exactly one implementation of the source\u2019s (84) '
     'in this corpus, so `9.1e-08` confirms the quadrature and not the remainder.', 'JUDGEMENT'),
    ('Verify against the stored blob, not the working copy.',
     '`core.autocrlf` makes a working file CRLF after any checkout while the blob stays LF; b309 '
     'lost a comparison to it and b319\u2019s repair compared to the blob and passed.',
     'MECHANIZED'),
    ('A re-implementation that cannot reproduce its original is an overwrite.',
     'b321\u2019s channels are a re-implementation of the atlas\u2019s; fixture (i) feeds them the '
     'atlas\u2019s OWN bump and requires every channel back to `1.006e-16`.', 'MECHANIZED'),
    ('A question is under-resolved, not open, when the candidates sit closer together than the '
     'instrument\u2019s distance from the answer \u2014 and the price is the ratio.',
     'b321\u2019s identity control HELD and still could not tell two exponent copies apart; b322 '
     'applied the rule deliberately and priced its own question.', 'JUDGEMENT'),
    ('When a defective rule licenses two branches equally, take the weaker.',
     'b322\u2019s `(B5)` fired twice at once; the stronger branch was a positive claim about the '
     'object and the weaker was a claim about the resolution.', 'JUDGEMENT'),
    ('A dichotomy that is not a partition cannot be read either way.',
     'b322\u2019s `(B2)` imported two labels that leave the truncation unexpressible.',
     'JUDGEMENT'),
    ('A ranker does not know what causes what.',
     'b322\u2019s `(B6)` named `CONDITION TWO` as the first differing constituent; the ladder had '
     'already shown it is what `THE DOMAIN` produces.', 'JUDGEMENT'),
    ('A run file may not carry a claim the act declined.',
     'b322\u2019s gate caught that the run alone printed `DIFFERENT VECTORS` with no sign the act '
     'had taken the weaker reading; the run was rewritten, not the gate.', 'MECHANIZED'),
    ('The ceiling is where the evaluator fails, not the last place it works.',
     'carried from the prior arc and unchanged by this one.', 'JUDGEMENT'),
    ('A gate arm that greps raw source fires on the act\u2019s own sentence saying the thing was '
     'not done.',
     'b317\u2019s `G-NOUNIT` fired on its own docstring; every gate since strips comments and '
     'strings first.', 'MECHANIZED'),
]

# ### (tool, what it catches, the incident)
SUITE = [
    ('`ferry_scan.py`', 'struck clauses and banned stems in an order or a registration, before the '
     'act runs', 'b319 sealed a registration with a banned stem in it and had to re-seal; b321 '
     'caught two stems in its own prose before the push.'),
    ('`reg_seal.py` + `reg_satisfiable.py`', 'a registration edited after a value was seen, and a '
     'set of caps whose demands exceed them', 'every act since b320 carries its seal hash as a '
     'literal in its own gate suite, so a re-seal cannot be hidden.'),
    ('`needle_pull.py`', 'a claim in a bank with no anchor in an emitting file',
     'six acts lost runs to anchors that wrapped mid-phrase; the practice is now to verify every '
     'anchor against its file BEFORE the gate is written.'),
    ('`noise_floor.py`', 'a point verdict taken from an axis that has not resolved',
     'it has REFUSED on the domain axis in every act from b317 to b322, and every one of those '
     'acts reported a direction and not a size.'),
    ('`hedge_audit.py`', 'a graded hedge \u2014 a claim softened without its grade moving',
     'run over every file each act writes.'),
    ('`b306_stem_scope.py`', 'a stem in a shared target outside the act\u2019s own files',
     'two pre-existing hits in `CORRESPONDENCE.md` rows 2 and 101 are whitelisted and everything '
     'else is a failure.'),
    ('`b307_handoff_census.py`', 'an act or a work-order missing from the ledger',
     'it counts NAMES in ONE ledger and says so in its own output.'),
    ('`b315_coverage_gate.py`', 'a `#print axioms` target compiled but never certified',
     'it fired for sixteen acts and b319 discharged it: 475 \u2192 566 prints, the old profile a '
     'literal byte prefix of the new one, 0 axiom-bearing terminals among the 91 newly certified.'),
    ('`mirror_verify.py`', 'a mirror archive that is internally consistent and stale',
     'at b182 a build verified CLEAN on both then-existing clauses at 33 files WITHOUT THE FILE IN '
     'IT; clause 3 was added because it is the only one that can see that.'),
    ('the pre-push hook', 'a push to `main` from a branch that is not `push-*` or `repair-*`, a '
     'HELD ancestry, or a HELD carrier artifact by name',
     'installed in all three repositories at b304; `.git/hooks/` is untracked, so it must be '
     'reinstalled after any clone.'),
]

# ### (item, its state, what it needs)
DESK = [
    ('**`M-2`**', '`(SPECIFIED-NOT-STATED)`, unchanged across all nine acts, under b310\u2019s cap',
     'the space it may be stated in has narrowed but no act in this arc states it.'),
    ('**The object\u2019s three conditions**',
     'each typed \u2014 a premise, a ruling, a construction',
     '**a condition discharged is not the object constructed.** The archimedean leg is derived '
     'and under-resolved at bench.'),
    ('**The archimedean leg**',
     'IN by b300\u2019s derivation at `DERIVES-on-IMPORTS`; UNDER-RESOLVED at bench',
     'the residual falls as `X^-0.5199` and would need `X = 3.973e+04` to reach `0.01` \u2014 a '
     'factor of `3.104e+02` beyond the domain reached.'),
    ('**The exponent**', 'settled by b313\u2019s READING of three source sites; UNDER-RESOLVED at '
     'bench',
     'b321\u2019s identity control held and the two copies were `0.000981` to `0.003994` apart '
     'where the instrument sat `0.018808` to `0.023224` from the answer.'),
    ('**`W-ORD-PHI-MU-L2`**', 'OPEN', 'no owner states `phi_mu` in `L^2(R)`, and the instrument '
     'cannot see the question because a finite array is square-summable whatever lies behind it.'),
    ('**`W-ORD-ARCH-MEMBERSHIP`**', 'OPEN', 'priced by b322 and not closed.'),
    ('**`W-ORD-WINDOW-CLASS`**', 'OPEN', 'b321 opened the window and decided no class.'),
    ('**The window ruling, applied at the instrument**',
     'the balance is computed and interpreted by nobody',
     'its sign is inherited from a library of zeros on the line, so it cannot come out positive '
     'and the act said so before counting.'),
    ('**The absolute-path order**', 'standing', 'carried unchanged.'),
    ('**The artifact-count counter**',
     'lexical, and it produced a FALSE POSITIVE on a statement of measured fact in three '
     'consecutive acts',
     '**its repair or its retirement is the author\u2019s**, not a seat\u2019s; acts rephrase '
     'around it.'),
    ('**The keystone re-read**', 'NAMED AS NEXT', 'the order sequences it after this fold.'),
    ('**The reconciliation wave**', 'the author\u2019s',
     'the arc\u2019s results are of the kind a wave would carry; no seat starts one.'),
    ('**The seam\u2019s debt, item 1**', 'STILL UNPAID', 'restated, not discharged.'),
    ('**The patent lane**', 'carried on the patent seat\u2019s report',
     '**unconfirmed on this seat\u2019s record.**'),
]


def fquote(text_by_act, rec):
    """### **F-QUOTE, WITH ITS DISCRIMINATION ARM.** ### A matcher that never misses is not
    matching, so an ALTERED quotation is fed to the same matcher and must come back unfindable."""
    bad = []
    for act, _w, quote, _g, _s in RESULTS:
        if quote not in text_by_act[act]:
            bad.append((act, 'RESULT', quote))
    for act, quote in OBSTACLES:
        if quote not in text_by_act[act]:
            bad.append((act, 'OBSTACLE', quote))
    n = len(RESULTS) + len(OBSTACLES)
    rec('  F-QUOTE  : %d quotations, %d unfindable' % (n, len(bad)))
    for act, kind, quote in bad:
        rec('      ### UNFINDABLE  %s %s -- %r' % (act, kind, quote[:74]))
    act0, _w, q0, _g, _s = RESULTS[0]
    altered = q0.replace('BANKED', 'BANKEDD')
    disc = altered not in text_by_act[act0]
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fcount(rec):
    covered = sorted({a for a, _w, _q, _g, _s in RESULTS}, key=lambda s: int(s[1:]))
    obs = sorted({a for a, _q in OBSTACLES}, key=lambda s: int(s[1:]))
    ok = (covered == ARC) and (obs == ARC)
    rec('  F-COUNT  : results cover %d, obstacles cover %d, arc %d, exact match : %s'
        % (len(covered), len(obs), len(ARC), ok))
    if not ok:
        rec('      ### results missing  : %s' % [a for a in ARC if a not in covered])
        rec('      ### obstacles missing: %s' % [a for a in ARC if a not in obs])
    return ok


def emit_markdown():
    L = []

    def A(s=''):
        L.append(s)

    A('## %s' % SECTION)
    A('')
    A('**Nine acts, 2026-09-03 to 2026-09-04.** A filings section: **no grade moves here, no act '
      'is re-verdicted, and nothing below is new mathematics.** Each entry carries its grade as '
      '*its own act* left it and its own scope sentence, and every quotation was checked verbatim '
      'against the act that **originated** it before this section was emitted.')
    A('')
    A('### The nine')
    A('')
    A('| act | what it is | grade, as its own act left it |')
    A('|---|---|---|')
    for act, what, _q, grade, _s in RESULTS:
        A('| **%s** | %s | %s |' % (act, what, grade))
    A('')
    A('### Each with its own sentence, its scope, and its obstacle')
    A('')
    obs = dict(OBSTACLES)
    for act, what, quote, grade, scope in RESULTS:
        A('- **%s \u2014 %s.** *Grade:* %s.' % (act, what, grade))
        A('  - Its own words: \u201c\u2026%s\u2026\u201d' % quote)
        A('  - **Scope, as its own act set it:** %s' % scope)
        A('  - **Obstacle, quoted:** \u201c\u2026%s\u2026\u201d' % obs[act])
    A('')
    A('### The arc\u2019s corrections to its own readings')
    A('')
    A('| act | what was corrected | **what did not move** |')
    A('|---|---|---|')
    for act, what, notmoved in CORRECTIONS:
        A('| **%s** | %s | %s |' % (act, what, notmoved))
    A('')
    A('### Sealed bars found defective, by the acts that sealed them')
    A('')
    A('**This table is new to this fold and it is not a comfortable one.** Three times in nine '
      'acts, a bar was sealed before any value and the bar itself turned out to be wrong. **In no '
      'case was the sealed file edited.** A record whose registrations are only ever reported as '
      'having worked is a record that has stopped reading them.')
    A('')
    A('| act | the bar | what was wrong with it | what the act did |')
    A('|---|---|---|---|')
    for act, bar, wrong, did in DEFECTIVE_BARS:
        A('| **%s** | %s | %s | %s |' % (act, bar, wrong, did))
    A('')
    A('**And the thing worth more than the table:** in all three the defect was found *by running '
      'the sealed bar and reading what came back*, not by revising it. b319 reported an empty '
      'reach under a bar it knew to be unsatisfiable; b322 reported a verdict its own broken rule '
      'computed and then took the weaker of the two branches that rule licensed.')
    A('')
    A('### The arc as one statement')
    A('')
    A('At the grade these nine acts support, and no higher: **the finite-instance explicit formula '
      'is realized on lawful objects, on an instrument now certified against three of the '
      'source\u2019s own theorems.** Its archimedean side splits, by the source\u2019s Theorem '
      '4.7, as the object\u2019s compressed square plus a remainder \u2014 and **that remainder '
      '*is* the margin b320 measured**, confirmed along the domain ladder to within a residual '
      'falling by a factor of two to three at every step. **The prime sum sits inside the margin '
      'at every one of the thirteen cells.** The zero side\u2019s sign is inherited from a library '
      'of zeros *on the critical line*, so **the window\u2019s balance cannot come out positive**, '
      'and the act that opened it established that before it counted. The object\u2019s '
      'archimedean unit is **in its space by derivation** and **under-resolved at bench by a '
      'stated factor**: its membership residual falls as `X^-0.5199`, which a second route '
      'sharing no code predicts from the vector\u2019s own `1/x` decay, and reaching `0.01` would '
      'cost a factor of `3.104e+02` in domain. **The clause lives at totality, and this arc names '
      'the mechanism by which no finite instrument reaches it:** every quantity here is a '
      'truncation whose error the arc can now measure, and measuring it is what shows the '
      'distance.')
    A('')
    A('**Scope, printed beside it.** This is a summary of nine acts at their own grades. **No '
      'theorem is proved here and none was proved by any act in the arc** \u2014 the source proved '
      'all three, and what the controls certify is the *instrument*, at exactly the scope of the '
      'control. **The window decides nothing:** 10000 ordinates, eleven primes, thirteen cells of '
      'one family, against a criterion that quantifies over every lawful `g`. **The SIZE of no '
      'margin on the domain axis is certified anywhere in this arc** \u2014 the noise-floor gate '
      'refused it in every act that measured it, and every one of those acts reported a direction '
      'instead. **Nothing about the identity, `h2`, or the complete roster follows from any of '
      'it.** **`M-2` is owed and no aggregation is stated.** **Nothing about the register sentence '
      'moves.**')
    A('')
    A('### The lore this arc leaves, with the incident that bought each rule')
    A('')
    A('**Mechanized** \u2014 a gate, a fixture or a tool enforces it:')
    A('')
    for rule, inc, kind in LORE:
        if kind == 'MECHANIZED':
            A('- **%s** *Incident:* %s' % (rule, inc))
    A('')
    A('**Judgement** \u2014 no mechanism enforces it and a seat must apply it:')
    A('')
    for rule, inc, kind in LORE:
        if kind == 'JUDGEMENT':
            A('- **%s** *Incident:* %s' % (rule, inc))
    A('')
    A('### The instrument suite, and what each piece catches')
    A('')
    A('| tool | what it catches | the incident that put it there |')
    A('|---|---|---|')
    for tool, catches, inc in SUITE:
        A('| %s | %s | %s |' % (tool, catches, inc))
    A('')
    A('**The archimedean instrument\u2019s certifications, and its limits.** It is certified '
      'against three of the source\u2019s theorems:')
    A('')
    A('| theorem | where checked | result |')
    A('|---|---|---|')
    A('| **Theorem 1** (b320) | the three cells its support condition covers, `a = 1.3, 1.35, '
      '1.41` | holds, margins `+0.271444634`, `+0.285510313`, `+0.309777648`, and at **27 of 27** '
      'instrument frames |')
    A('| **Theorem 4.7** (b321) | the same three cells | holds as an **equality**; the residual '
      'along the domain ladder falls `0.896557, 0.306328, 0.112555, 0.047182, 0.023224` |')
    A('| **The explicit formula (148)** (b321) | **all thirteen cells** | holds, residuals `2.2e-09` '
      'to `3.6e-05` against the atlas\u2019s own sealed `TOL = 1e-03` |')
    A('')
    A('**And its limits, stated as measurements.** The domain axis has never converged: its rate '
      'is now known \u2014 the instrument\u2019s own residual falls as `X^-1.324` while the '
      'unit\u2019s falls as `X^-0.520`, a ratio of `0.393`. **The resolving power has been priced '
      'twice**, once for the exponent question and once for the membership question, and both '
      'prices are beyond what the instrument reaches.')
    A('')
    A('### The desk')
    A('')
    A('| item | state | what it needs |')
    A('|---|---|---|')
    for item, state, needs in DESK:
        A('| %s | %s | %s |' % (item, state, needs))
    A('')
    A('### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**')
    A('')
    return '\n'.join(L)


OUT = []


def main():
    def rec(s=''):
        OUT.append(s)
        print(s)

    rec('=' * 100)
    rec('b323 -- THE FOLD, b314-b322. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)

    text_by_act = {}
    for act in ARC:
        p = os.path.join(D, SRC[act])
        text_by_act[act] = io.open(p, encoding='utf-8', errors='replace').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)'
        % len(text_by_act))

    q_ok = fquote(text_by_act, rec)
    c_ok = fcount(rec)
    rec('  ### **THE JUDGEMENT THE MECHANISM DOES NOT MAKE:** ### that each sentence is that')
    rec('  ### act\'s OWN VOICE and not material it was itself quoting. ### **THAT IS THIS SEAT\'S**')
    rec('  ### and the bank declares it as this seat\'s.')
    if not (q_ok and c_ok):
        rec('  ### ### **REFUSING TO EMIT. ### NOTHING IS WRITTEN TO FINDINGS.md.**')
        return 1

    before = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    # ### ### **IDEMPOTENT, AND THIS ACT LEARNED WHY THE HARD WAY.** ### The write is an APPEND, so
    # ### a second run files the arc TWICE -- which happened once here before this guard existed.
    # ### **THE CLOSING RULE REQUIRES THE WHOLE SUITE RE-RUN AFTER THE PUSH**, and a generator that
    # ### can only be run once cannot satisfy it.
    if ('## ' + SECTION) in before:
        rec('')
        rec('  ### ### **THE SECTION IS ALREADY IN FINDINGS.md. ### NOTHING WRITTEN.** (idempotent)')
        rec('  ### The gates above still ran, and the read-back below still runs.')
        present = ('## ' + SECTION) in before
        nsec = len([x for x in before.splitlines() if x.startswith('## ')])
        rec('  section present on disk : %s ; sections total : %d' % (present, nsec))
        io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(emit_markdown() + '\n')
        rec('=' * 100)
        rec('  ### ### **FOLD GATES : %s**'
            % ('ALL PASS' if (q_ok and c_ok and present) else '### FAIL ###'))
        rec('=' * 100)
        return 0 if (q_ok and c_ok and present) else 1
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    rec('')
    rec('  ### THE BASELINE, TAKEN BEFORE THE WRITE:')
    rec('    working file : %d bytes, %d lines' % (len(before.encode('utf-8')),
                                                   len(before.splitlines())))
    rec('    blob at HEAD : %d bytes, %d lines' % (len(blob.encode('utf-8')),
                                                   len(blob.splitlines())))
    delta = len(before.encode('utf-8')) - len(blob.encode('utf-8'))
    if delta:
        rec('    ### **THE TWO DIFFER BY %+d BYTES**, which is `core.autocrlf` and NOT the record.'
            % delta)
    else:
        rec('    ### **THE TWO ARE THE SAME LENGTH HERE**, so `core.autocrlf` has not bitten this')
        rec('    ### file on this checkout. ### **THAT IS A MEASUREMENT AND NOT A GUARANTEE**, and')
        rec('    ### it is why the prefix test below runs against BOTH rather than against either:')
        rec('    ### b309 lost a comparison to exactly this difference on a clean tree.')

    md = emit_markdown()
    new = before.rstrip('\n') + '\n\n' + md
    open(FINDINGS + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(FINDINGS + '.tmp', FINDINGS)

    after = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    pfx_work = after.startswith(before.rstrip('\n'))
    norm = lambda s: s.replace('\r\n', '\n')
    pfx_blob = norm(after).startswith(norm(blob).rstrip('\n'))
    added = len(after.splitlines()) - len(before.splitlines())
    rec('')
    rec('  ### THE NO-GRADE-MOVED CHECK, MECHANICAL:')
    rec('    the pre-append working file is a TRUE PREFIX of the result : %s' % pfx_work)
    rec('    the blob at HEAD is a TRUE PREFIX of the result (normalised): %s' % pfx_blob)
    rec('    lines added : %+d   sections before : %d   after : %d'
        % (added, len([x for x in before.splitlines() if x.startswith('## ')]),
           len([x for x in after.splitlines() if x.startswith('## ')])))
    rec('    ### ### **PURELY ADDITIVE : %s**' % (pfx_work and pfx_blob))
    rec('    ### **A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD**, and this is the measurement')
    rec('    ### rather than the promise.')

    io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md + '\n')
    payload = dict(arc=ARC, results=[list(r) for r in RESULTS],
                   obstacles=[list(o) for o in OBSTACLES],
                   corrections=[list(c) for c in CORRECTIONS],
                   defective_bars=[list(b) for b in DEFECTIVE_BARS],
                   lore=[list(x) for x in LORE], suite=[list(x) for x in SUITE],
                   desk=[list(x) for x in DESK],
                   fquote=bool(q_ok), fcount=bool(c_ok),
                   prefix_working=bool(pfx_work), prefix_blob=bool(pfx_blob),
                   lines_added=added, section=SECTION)
    d = (json.dumps(payload, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(ROWS + '.tmp', 'wb').write(d)
    os.replace(ROWS + '.tmp', ROWS)

    rec('')
    rec('  emitted markdown : %s  (%d lines)' % (os.path.basename(EMIT), len(md.splitlines())))
    rec('  rows json        : %s' % os.path.basename(ROWS))
    rec('=' * 100)
    ok = q_ok and c_ok and pfx_work and pfx_blob
    rec('  ### ### **FOLD GATES : %s**' % ('ALL PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(D, 'b323_fold_run.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(OUT) + '\n')
    sys.exit(code)
