# -*- coding: utf-8 -*-
"""b338_fold.py -- THE FOLD, b331-b334. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED. ### TECHNE IS NOT TOUCHED.**

### ### **THE DESIGN POINT, CARRIED FROM b323 AND b331:** ### the result table below is the single source of truth
### and this runner EMITS the markdown the fold appends. ### A quotation that fails `F-QUOTE` never reaches
### `FINDINGS.md` at all. ### **THE EMITTER DISCIPLINE (b283):** every quotation is checked against THE ACT THAT
### ORIGINATED IT, never against an act that quoted it. ### The judgement -- that the sentence is that act's OWN
### VOICE -- is the seat's, declared in the bank. ### **IDEMPOTENT:** a second run finds the section and writes nothing.
### ### **THE DESK'S FIRST ITEM IS THE WAVE'S CANDIDATE LIST RESTATED, WITH THE HOUSEKEEPING'S STATE BESIDE IT** --
### the order's clause for this leg; the wave is the author's and nothing here is a recommendation.
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
EMIT = os.path.join(D, 'b338_fold_emitted.md')
ROWS = os.path.join(D, 'b338_fold_rows.json')
MODULES = os.path.join(r'D:\MY-DOwnloads\TECHNE-Core', 'modules', '2026-09')

ARC = ['b331', 'b332', 'b333', 'b334']

SRC = {
    'b331': 'b331_the_fold.txt',
    'b332': 'b332_the_clause_stated.txt',
    'b333': 'b333_the_archimedean_term_derived.txt',
    'b334': 'b334_the_aim_map.txt',
}

SECTION = 'THE STATED-CLAUSE ARC, b331\u2013b334 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE SCOPE SENTENCE)
RESULTS = [
    ('b331', 'the fold of b323\u2013b330 filed, purely additive, with the desk restated',
     'AND IT IS PURELY ADDITIVE, MEASURED AND NOT PROMISED.',
     'FILED \u2014 a filings act; no grade moved',
     'A fold is a summary of its acts at their own grades; it proves nothing, and the desk it restates '
     'names the discharge-statement and the aim-map as the next two research acts with the sentence that '
     'neither is the discharge.'),
    ('b332', 'the open clause stated whole in the arc\u2019s vocabulary, every constituent graded by its owner, '
     'the ranking under a rule sealed before the table',
     "THE CLAUSE IS STATED, WHOLE, IN THE ARC'S VOCABULARY, AND IT IS NOT DISCHARGED.",
     'STATED \u2014 no proof attempted, no grade conferred; the quantifiers K8 unowned',
     'The statement is one face of the obligation and not its compiled equivalence; the E0 gate halts at '
     'the quantifiers and at nothing else; the ranking under the sealed rule put the archimedean '
     'distribution softest, which neither seat expected, and the rule was reported and not adjusted.'),
    ('b333', 'the archimedean distribution derived from the classical term under the import bar; a third route; '
     'the sealed bar found to pair the bump with a table made for another function',
     "THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED.",
     'DERIVES-ON-IMPORTS for K5, the derivation\u2019s own; MEASURED-ON-FAMILIES not conferred; the '
     'tool\u2019s verdict MISMATCH at (L3), diagnosed as the sealed bar\u2019s own defect',
     'The corpus\u2019s archimedean channel is the source\u2019s `W_\u221e = \u2212W_R` in the orientation the '
     'calibration fixed; four routes agree on the bump and that certifies the routes, not the size; '
     'the sealed bar as sealed is not met and is not rewritten; K5 and K6 tie at the softest rank.'),
    ('b334', 'the aim-map: the room the arithmetic leaves charted over aims for zeta and for the Epstein '
     'function, the softest pair\u2019s behaviour measured',
     'FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN AT EVERY AIM AT THIS REACH -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE.',
     'MEASURED on a grid at this reach \u2014 no grade conferred; the softest pair gains a behaviour over aims',
     'A chart is not a proof; the Epstein crossing is the negative control charted, at three aims all at '
     'off-line zeros\u2019 heights; K5 and K6 soften apart; the sealed threshold rule is not the sign condition '
     'and the chart says so; the quantifier stays unowned.'),
]

OBSTACLES = [
    ('b331', 'IT DOES NOT SAY EITHER NEXT ACT IS THE DISCHARGE.'),
    ('b332', 'IT DOES NOT SAY THE RANKING IS A VERDICT ON THE CLAUSE.'),
    ('b333', 'IT DOES NOT SAY THE SEALED BAR WAS MET.'),
    ('b334', 'IT DOES NOT SAY A CHART IS A PROOF.'),
]

# ### (act, what was corrected, WHAT DID NOT MOVE)
CORRECTIONS = [
    ('b331', 'one extract anchor that spanned two lines of its emitter, narrowed to the emitted line before '
     'the notes were used', 'the fold\u2019s rules, inherited from b323 and held; the section, purely additive'),
    ('b332', 'the first emission carried a sentence the computed ranking contradicted \u2014 the file was restored '
     'from its blob and the generator made to read the ranking it computes; and this seat\u2019s sealed '
     'expectation (the remainder softest) was wrong about its own sealed rule',
     'the sealed rule, reported and not adjusted; the ranking, computed and not chosen; the expectations, '
     'scored NOT MET'),
    ('b333', 'the sealed bar paired the third route on the atlas\u2019s bump with b320\u2019s table, which b320 '
     'computed for its own function; diagnosed like for like by a new tool, the record\u2019s numbers standing',
     'the sealed bar, not met and not rewritten; the record\u2019s archimedean numbers; the grade '
     'MEASURED-ON-FAMILIES, not conferred'),
    ('b334', 'the sealed threshold rule (the phase past forty-five degrees) counted a hundred aims whose '
     'quadruple term is positive, the phase near a hundred and eighty; the chart carries the term\u2019s sign '
     'beside every verdict', 'the sealed rule\u2019s verdict column, kept as sealed; b328\u2019s own phases near ninety'),
]

# ### (act, the bar, what was wrong with it, what the act did about it)
DEFECTIVE_BARS = [
    ('b333', 'the third route inside `2e-4` of b320\u2019s two banked routes at the thirteen arc cells',
     'the route ran on the atlas\u2019s bump and the table it was measured against was computed for '
     'b320\u2019s own function, `autocorrelation(mean_zero_variant(a))`; no route satisfies it',
     'reported the tool\u2019s MISMATCH first, at full prominence; diagnosed it by a new tool that pairs '
     'each function with its own routes (the bump against the atlas and b320\u2019s routes applied to the '
     'bump, within `1.9e-6`; the source\u2019s (150) on b320\u2019s function against b320\u2019s table, within '
     '`2.7e-5`); the bar left unmet and unedited; the measurement grade not conferred'),
    ('b334', 'the two transform routes within `1e-10` relative at every aim',
     'Simpson on the seed\u2019s own nodes against the closed form parts by up to `1.14e-4` at the highest '
     'aims, growing with the height', 'reported as measured, the bar not moved; the phases unaffected at the degree'),
    ('b334', 'REACHED iff the phase exceeds forty-five degrees',
     'b328\u2019s rule, stated where every phase sat near ninety; the quadruple\u2019s term is negative only '
     'between forty-five and a hundred and thirty-five degrees, and a hundred of the aims counted sit near '
     'a hundred and eighty', 'kept the verdict column as sealed and printed the term\u2019s sign beside it at '
     'every aim; b336 filed the refinement as an addendum to b328\u2019s block'),
]

# ### (act, the seat's own defects, declared)
DEFECTS = [
    ('b331', 'one extract anchor spanning two lines of its emitter, narrowed before use'),
    ('b332', 'three extract anchors typed from memory; the artifact-count counter fired on a measured fact and '
     'was rephrased, not fought; the first emission contradicting the computed ranking, restored and '
     're-emitted; the seat\u2019s expectation wrong about its own sealed rule; a self-needle wrapped in the '
     'sealed registration'),
    ('b333', 'the sealed bar pairing the bump with another function\u2019s table; the derivation tool\u2019s re-rank '
     'conferring a grade ahead of its verdict, superseded by a separate tool; its (152) evaluation '
     'under-resolved by quadrature; the diagnostic\u2019s first run dying on the record\u2019s cell keys; one '
     'anchor wrapped in its emitter; the seat\u2019s expectation for the third route not met'),
    ('b334', 'the sealed threshold rule not the sign condition; the chart mode extended before its first run to '
     'print the term\u2019s sign; the four instrument modes launched in parallel and killed for memory, the '
     'legs re-run two at a time; the transform-route bar exceeded as measured; the seat\u2019s expectations '
     'for the covered leg\u2019s phases and for the sign of the archimedean term not met'),
]

# ### THE LORE THIS ARC LEAVES. ### (rule, the incident, MODULE / TOOL / JUDGEMENT, the module or tool)
LORE = [
    ('A comparator is named with the function it was computed for; a bar sealed against a banked table '
     'names the table\u2019s function, and a comparison whose two sides name different functions is refused.',
     'b333\u2019s sealed bar measured the bump against a table made for another function and the tool printed '
     'MISMATCH; b334 carried every quantity as a named pair and its comparison function raises on a mismatch.',
     'TOOL', 'tools/b334_aimmap.py'),
    ('A threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.',
     'b328\u2019s rule counted a hundred of b334\u2019s aims whose quadruple term is positive; the chart prints the '
     'term\u2019s sign beside every verdict.', 'TOOL', 'tools/b334_aimmap.py'),
    ('A ranking is computed from the table before an expectation about it is written.',
     'both seats expected the remainder softest at b332; the rule both had sealed put the archimedean '
     'distribution softest, and the expectation was scored NOT MET rather than the rule adjusted.',
     'JUDGEMENT', ''),
    ('When a tool\u2019s verdict is not the expected one it is the bank\u2019s first sentence, and the diagnosis '
     'follows it; the diagnosis lives in a new tool and the sealed bar is not rewritten.',
     'b333\u2019s bank opens with the tool\u2019s MISMATCH and diagnoses it second; the bar stays unmet.',
     'JUDGEMENT', ''),
    ('A sealed bar found defective by running it is measured and tabled, never edited.',
     'b323\u2019s rule, held again: b333 tabled one bar and b334 two, none edited, each measured.',
     'MODULE', 'SEALED_BARS_FOUND_DEFECTIVE.md'),
    ('Every quantity by two routes sharing no code; three or four routes agreeing certify the routes, not the size.',
     'b333 put a third route beside the record\u2019s two and the like-for-like diagnostic a fourth; b334 carried '
     'two routes for every quantity and a principal-value witness for the archimedean term.',
     'MODULE', 'TWO_ROUTES.md'),
    ('The noise-floor gate sits in the path of every sign, at two resolutions.',
     'b334 passed every places-side sign through the gate at refine one against four; none refused.',
     'MODULE', 'NOISE_FLOOR_GATE.md'),
    ('Instrument legs run two at a time on this machine, never four.',
     'b334\u2019s four modes launched together were killed for memory; two at a time completed.',
     'JUDGEMENT', ''),
]

# ### (tool, what it catches, the incident that put it there)
SUITE = [
    ('`b332_statement.py` (F-QUOTE / F-GRADES, the sealed ranking rule)', 'a quotation not in its originating bank; a grade word '
     'not in its owner\u2019s bank; a ranking typed rather than computed', 'the first emission carried a sentence the ranking contradicted.'),
    ('`b333_derive.py` + `b333_diagnose.py`', 'a derivation link without its quotation; a factor of two in a Gamma factor; a '
     'comparator paired with another function\u2019s table', 'the sealed bar\u2019s pairing, diagnosed like for like.'),
    ('`b333_rerank.py`', 'a grade conferred ahead of its verdict', 'the derivation tool\u2019s re-rank had added MEASURED-ON-FAMILIES unconditionally.'),
    ('`b334_aimmap.py` (`compare`, the gate, the sign column)', 'a comparison across functions; a sign at the floor; a phase '
     'past the threshold read as a negative term', 'b333\u2019s species, b326\u2019s gate, b328\u2019s rule refined.'),
    ('the extract step (`bNNN_extract.py`)', 'a needle typed from memory; an anchor spanning a line wrap',
     'b331, b332 and b333 each refused one or more anchors before the notes were used.'),
]

# ### THE DESK. ### (item, its state, what it needs) -- the FIRST item is the wave's candidate list, restated
DESK = [
    ('**The reconciliation wave \u2014 the candidate list, restated**',
     '**b324\u2019s list, typed and not ranked:** `[NEW]` the archimedean instrument, certified against three of the '
     'source\u2019s theorems; `[NEW]` the identity `W_\u221e(f) \u2212 Tr(\u03b8(f) S) = \u2212\u222b f(\u03c1\u207b\u00b9) \u03b5(\u03c1) d*\u03c1`, '
     'measured along the domain ladder; `[NEW]` the window\u2019s balance non-positive by construction; `[NEW]` the '
     'resolving-power rule and its two prices; `[REFINEMENT-OF-DEPOSITED]` the instrument sits inside the '
     'monograph\u2019s first named classical face of h2; `[REFINEMENT-OF-INTERNAL]` the wall\u2019s grading of the '
     'source, now accompanied by a measured instrument. **b331\u2019s addition:** the negative control that said '
     'no (b328), a candidate and not a recommendation. **This arc\u2019s additions, typed as candidates and not '
     'recommendations:** the open clause stated whole (b332); the archimedean distribution derived from the '
     'classical term under the import bar (b333); the aim-map\u2019s chart of the room over aims (b334). '
     '**Beside it, the housekeeping\u2019s state as b337 left it:** the read-only fetch agrees with REGISTRY on '
     'every field, the loom and the trails CURRENT, ERRATA\u2019s head DRIFT repaired by an appended note; ERRATA '
     'partitioned by one appended header line, entries unmoved; the nine August TECHNE files committed to '
     'the canonical local clone, not pushed; the patent receipts ABSENT ON THE MOUNTED VOLUMES with `F:` not '
     'mounted, nothing concluded about the reply.',
     '**The wave is the author\u2019s. The list is typed, not ranked, and no seat starts one.**'),
    ('**`M-2`**', '`(SPECIFIED-NOT-STATED)`, unchanged across all four acts, under b310\u2019s cap',
     'no act in this arc states it and no aggregation is stated.'),
    ('**The clause\u2019s softest pair, K5 and K6**', 'tied at `MEASURED-AT-COVERED-CELLS` after b333\u2019s re-rank; a behaviour over '
     'aims after b334: the distribution\u2019s convergence worsens with height, the decomposition\u2019s does not, and '
     'the square sits far from its identity at every aimed seed', 'what would move each is typed at the cost census (b336): '
     'a MEASUREMENT priced by the unit\u2019s domain factor and the instrument\u2019s act count; a chart is not a proof.'),
    ('**The object\u2019s three conditions**', 'each typed \u2014 a premise, a ruling, a construction', '**a condition discharged is not the object constructed.**'),
    ('**The exponent\u2019s ratio**', 'the two remainder copies apart by a twenty-fourth to a fifth of the distance to the equality '
     '(b321); now a typed price on the faces ledger (b336)', 'the resolving power priced and beyond reach; unchanged by this arc.'),
    ('**The Li-to-Weil bridge**', 'OWED at L1 \u2014 `W-ORD-LI-WEIL-BRIDGE`; the pole-constant relation between the two faces '
     'stated at L2, cost zero (b336)', 'a relation between the compressed square on the Sonin family and the finite-place '
     'channel on the Li family, or a proof that none exists.'),
    ('**The Li bench versus the keystone**', 'the bench\u2019s literature dictionary disagrees with the balance keystone\u2019s '
     'column at `n = 3` and `n = 5` (b327)', 'a typed fixture, filed and not edited; the author\u2019s to reconcile.'),
    ('**The compact part beyond the cells**', 'PROVED-AT-CELLS (b329); the general zero is orthogonality to the valuation shells, '
     'not vanilla-decidable', 'a certification beyond cells would be new mathematics and is not this seat\u2019s to add.'),
    ('**The standing clauses and the STOP format**', 'filed at b335: `FERRY_STANDING.md` VERSION 1 with the scan checking the citation; '
     'Rule 6, the executor\u2019s STOP ending in a DRAFT the navigator edits', 'a ferry cites the file at its current version; the draft binds nothing.'),
    ('**The two TECHNE clones**', 'the August files committed to the canonical clone at b337, not pushed; `TECHNE_Core` diverged and untouched',
     '**the reconcile is the author\u2019s**; nothing is pushed until the four provisionals are filed.'),
    ('**The seam\u2019s debt, item 1**', 'STILL UNPAID', 'restated, not discharged.'),
    ('**The patent receipts**', 'ABSENT ON THE MOUNTED VOLUMES for both applications (b337); `F:` not mounted this session; UNCONFIRMED on this '
     'seat\u2019s record', '**the one item on this desk with a date;** carried on the patent seat\u2019s report; the mounted volumes '
     'enumerated before any absence was concluded.'),
]


def fquote(text_by_act, rec):
    """### **F-QUOTE, WITH ITS DISCRIMINATION ARM.** ### An ALTERED quotation must come back unfindable."""
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
    altered = q0.replace('ADDITIVE', 'ADDITIVEE')
    disc = altered not in text_by_act[act0]
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fcount(rec):
    covered = sorted({a for a, _w, _q, _g, _s in RESULTS}, key=lambda s: int(s[1:]))
    obs = sorted({a for a, _q in OBSTACLES}, key=lambda s: int(s[1:]))
    ok = (covered == ARC) and (obs == ARC)
    rec('  F-COUNT  : results cover %d, obstacles cover %d, arc %d, exact match : %s' % (len(covered), len(obs), len(ARC), ok))
    return ok


def fmodules(rec):
    missing_m = [m for _r, _i, k, m in LORE if k == 'MODULE' and not os.path.exists(os.path.join(MODULES, m))]
    missing_t = [m for _r, _i, k, m in LORE if k == 'TOOL' and not os.path.exists(os.path.join(ROOT, m.replace('/', os.sep)))]
    nm = sum(1 for _r, _i, k, _m in LORE if k == 'MODULE')
    nt = sum(1 for _r, _i, k, _m in LORE if k == 'TOOL')
    rec('  F-MODULES: %d rules by module, all on disk : %s %s ; %d rules by tool, all on disk : %s %s' % (nm, not missing_m, missing_m or '', nt, not missing_t, missing_t or ''))
    return not missing_m and not missing_t and nm > 0 and nt > 0


def emit_markdown():
    L = []

    def A(s=''):
        L.append(s)

    A('## %s' % SECTION)
    A('')
    A('**Four acts, 2026-09-06.** A filings section: **no grade moves here, no act is re-verdicted, and nothing '
      'below is new mathematics.** Each entry carries its grade as *its own act* left it and its own scope '
      'sentence, and every quotation was checked verbatim against the act that **originated** it before this '
      'section was emitted.')
    A('')
    A('### The four')
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
    A('### Sealed bars found defective, by the acts that sealed them \u2014 the table continued')
    A('')
    A('**The prior folds opened this table and carried it to eight rows. This arc adds three in four acts.** In no '
      'case was a sealed file edited; in every case the defect was found by running the bar and reading what came back.')
    A('')
    A('| act | the bar | what was wrong with it | what the act did |')
    A('|---|---|---|---|')
    for act, bar, wrong, did in DEFECTIVE_BARS:
        A('| **%s** | %s | %s | %s |' % (act, bar, wrong, did))
    A('')
    A('### The seats\u2019 own defects, declared by the acts that made them')
    A('')
    A('| act | declared |')
    A('|---|---|')
    for act, what in DEFECTS:
        A('| **%s** | %s |' % (act, what))
    A('')
    A('### The arc as one statement')
    A('')
    A('At the grade these four acts support, and no higher: **the open clause is stated, whole, in the arc\u2019s '
      'vocabulary, and it is not discharged** (b332) \u2014 for every function in the source\u2019s class the places '
      'sum of the explicit formula keeps the criterion\u2019s sign \u2014 with every constituent unfolded to its '
      'owner and the quantifiers, over the class and over the zeros, unowned: they are the clause. **Its '
      'softest constituent is now derived from the classical term under the import bar** (b333): the '
      'corpus\u2019s archimedean channel is the source\u2019s `W_\u221e = \u2212W_R` in the orientation the '
      'calibration fixed, the factor-of-two hazard one identity, four routes agreeing on the bump \u2014 and '
      'the act\u2019s own sealed bar was found to pair the bump with a table made for another function, so the '
      'measurement grade was not conferred and the record\u2019s numbers stand untouched. **The room the '
      'arithmetic leaves is charted over aims** (b334): for zeta the prime sum stays inside the margin at '
      'every aim at this reach, a passed test over a grid and nothing more; for the Epstein function the '
      'crossing sits at three aims, every one at an off-line zero\u2019s height, the negative control charted; '
      'the softest pair, K5 and K6, tied by the re-rank, soften apart \u2014 the distribution\u2019s convergence '
      'worsens with height and the decomposition\u2019s does not, and the square on the stable cut sits far '
      'from its identity at every aimed seed. **And the clause has not moved:** no act in the arc claims '
      'otherwise; a statement, a derivation and a chart are a statement, a derivation and a chart.')
    A('')
    A('**Scope, printed beside it.** This is a summary of four acts at their own grades. **No theorem is proved '
      'here and none was proved by any act in the arc.** The statement is one face of the obligation and not '
      'its compiled equivalence; the derivation settles one constituent\u2019s provenance and nothing about the '
      'quantifier; the chart is a finite-reach chart over a grid, interpreted by nobody, and a chart is not a '
      'proof. **Nothing about the identity, `h2`, or the complete roster follows from any of it. `M-2` is owed '
      'and no aggregation is stated. Nothing about the register sentence moves.**')
    A('')
    A('### The lore this arc leaves, with the incident that bought each rule and what enforces it')
    A('')
    A('**Mechanized by a module** \u2014 a TECHNE module (private, local, not pushed) carries the rule and a gate enforces it:')
    A('')
    for rule, inc, kind, mod in LORE:
        if kind == 'MODULE':
            A('- **%s** *Incident:* %s *Module:* `modules/2026-09/%s`' % (rule, inc, mod))
    A('')
    A('**Mechanized by a tool** \u2014 a committed tool of this arc enforces the rule; no module carries it yet, and the next extraction\u2019s desk holds it:')
    A('')
    for rule, inc, kind, tool in LORE:
        if kind == 'TOOL':
            A('- **%s** *Incident:* %s *Tool:* `%s`' % (rule, inc, tool))
    A('')
    A('**Judgement** \u2014 no mechanism enforces it and a seat must apply it:')
    A('')
    for rule, inc, kind, _m in LORE:
        if kind == 'JUDGEMENT':
            A('- **%s** *Incident:* %s' % (rule, inc))
    A('')
    A('### The instrument suite, what this arc added, and what each piece catches')
    A('')
    A('| tool | what it catches | the incident that put it there |')
    A('|---|---|---|')
    for tool, catches, inc in SUITE:
        A('| %s | %s | %s |' % (tool, catches, inc))
    A('')
    A('### The desk \u2014 its first item the wave\u2019s candidate list, restated, with the housekeeping\u2019s state beside it')
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
    rec('b338 -- THE FOLD, b331-b334. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)
    text_by_act = {}
    for act in ARC:
        text_by_act[act] = io.open(os.path.join(D, SRC[act]), encoding='utf-8', errors='replace').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)' % len(text_by_act))
    q_ok = fquote(text_by_act, rec)
    c_ok = fcount(rec)
    m_ok = fmodules(rec)
    rec("  ### **THE JUDGEMENT THE MECHANISM DOES NOT MAKE:** ### that each sentence is that act's OWN")
    rec("  ### VOICE and not material it was itself quoting. ### **THAT IS THIS SEAT'S** and the bank declares it.")
    if not (q_ok and c_ok and m_ok):
        rec('  ### ### **REFUSING TO EMIT. ### NOTHING IS WRITTEN TO FINDINGS.md.**')
        return 1
    before = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    md = emit_markdown()
    if ('## ' + SECTION) in before:
        rec('')
        rec('  ### ### **THE SECTION IS ALREADY IN FINDINGS.md. ### NOTHING WRITTEN.** (idempotent)')
        nsec = len([x for x in before.splitlines() if x.startswith('## ')])
        rec('  section present on disk : True ; sections total : %d' % nsec)
        io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md + '\n')
        rec('=' * 100)
        rec('  ### ### **FOLD GATES : ALL PASS**')
        rec('=' * 100)
        return 0
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    rec('')
    rec('  ### THE BASELINE, TAKEN BEFORE THE WRITE:')
    rec('    working file : %d bytes, %d lines' % (len(before.encode('utf-8')), len(before.splitlines())))
    rec('    blob at HEAD : %d bytes, %d lines' % (len(blob.encode('utf-8')), len(blob.splitlines())))
    new = before.rstrip('\n') + '\n\n' + md
    open(FINDINGS + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(FINDINGS + '.tmp', FINDINGS)
    after = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    pfx_work = after.startswith(before.rstrip('\n'))
    norm = lambda s: s.replace('\r\n', '\n')  # noqa: E731
    pfx_blob = norm(after).startswith(norm(blob).rstrip('\n'))
    added = len(after.splitlines()) - len(before.splitlines())
    rec('')
    rec('  ### THE NO-GRADE-MOVED CHECK, MECHANICAL:')
    rec('    the pre-append working file is a TRUE PREFIX of the result : %s' % pfx_work)
    rec('    the blob at HEAD is a TRUE PREFIX of the result (normalised): %s' % pfx_blob)
    rec('    lines added : %+d   sections before : %d   after : %d' % (added, len([x for x in before.splitlines() if x.startswith('## ')]), len([x for x in after.splitlines() if x.startswith('## ')])))
    rec('    ### ### **PURELY ADDITIVE : %s**' % (pfx_work and pfx_blob))
    io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md + '\n')
    payload = dict(arc=ARC, results=[list(r) for r in RESULTS], obstacles=[list(o) for o in OBSTACLES],
                   corrections=[list(c) for c in CORRECTIONS], defective_bars=[list(b) for b in DEFECTIVE_BARS],
                   defects=[list(x) for x in DEFECTS], lore=[list(x) for x in LORE], suite=[list(x) for x in SUITE],
                   desk=[list(x) for x in DESK], fquote=bool(q_ok), fcount=bool(c_ok), fmodules=bool(m_ok),
                   prefix_working=bool(pfx_work), prefix_blob=bool(pfx_blob), lines_added=added, section=SECTION,
                   lines_before=len(before.splitlines()), lines_after=len(after.splitlines()))
    open(ROWS + '.tmp', 'wb').write((json.dumps(payload, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
    os.replace(ROWS + '.tmp', ROWS)
    rec('')
    rec('  emitted markdown : %s  (%d lines)' % (os.path.basename(EMIT), len(md.splitlines())))
    rec('  rows json        : %s' % os.path.basename(ROWS))
    rec('=' * 100)
    ok = q_ok and c_ok and m_ok and pfx_work and pfx_blob
    rec('  ### ### **FOLD GATES : %s**' % ('ALL PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    code = main()
    base = 'b338_fold_run'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(OUT) + '\n')
    sys.exit(code)
