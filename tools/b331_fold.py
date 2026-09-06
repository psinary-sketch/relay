# -*- coding: utf-8 -*-
"""b331_fold.py -- THE FOLD, b323-b330. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED. ### TECHNE IS NOT TOUCHED.**

### ### **THE DESIGN POINT, CARRIED FROM b266, b282, b297, b307, b314 AND b323:** ### the result table
### below is the single source of truth and this runner EMITS the markdown the fold appends. ### A
### quotation that fails `F-QUOTE` never reaches `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER
### THE WRITING CAN ONLY REPORT A PARAPHRASE; ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**
### ### **THE EMITTER DISCIPLINE (b283):** ### every quotation is checked against THE ACT THAT
### ORIGINATED IT, never against an act that quoted it. ### The mechanical check is `in the
### originating file`; the judgement -- that the sentence is that act's OWN VOICE -- is the seat's,
### declared in the bank.
### ### **IDEMPOTENT (b323's first defect):** ### a second run finds the section and writes nothing.
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
EMIT = os.path.join(D, 'b331_fold_emitted.md')
ROWS = os.path.join(D, 'b331_fold_rows.json')

ARC = ['b323', 'b324', 'b325', 'b326', 'b327', 'b328', 'b329', 'b330']

SRC = {
    'b323': 'b323_the_fold.txt',
    'b324': 'b324_the_keystones_reread.txt',
    'b325': 'b325_the_negative_control.txt',
    'b326': 'b326_the_reach.txt',
    'b327': 'b327_the_faces_ledger.txt',
    'b328': 'b328_the_discriminating_family.txt',
    'b329': 'b329_the_finite_side_seal.txt',
    'b330': 'b330_the_techne_extraction.txt',
}

SECTION = 'THE DISCRIMINATING-FAMILY ARC, b323\u2013b330 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE SCOPE SENTENCE)
RESULTS = [
    ('b323', 'the prior fold filed, and the sealed-bars-found-defective table filed for the first time',
     'A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD',
     'FILED \u2014 a filings act; no grade moved',
     'A fold is a summary of its acts at their own grades. It proves nothing, and the table it added '
     'records bars that were wrong, not results that were.'),
    ('b324', 'the keystones re-read against the arc: the wall, the margin, the provenance',
     'THE WALL: ### DIFFERENT. ### (F1) IS REFUTED, AND BOTH ITS HALVES FALL.',
     'READ \u2014 DIFFERENT on the wall, UNDECIDED on the margin; no grade moved',
     'The arc built a different object from the keystone\u2019s, inside a source the keystone had '
     'already graded as stalling at the realization clause; the bridge between the two margins is '
     'withheld by the deposit\u2019s own design, and the act typed it as owed.'),
    ('b325', 'the negative control run at the arc\u2019s cells on the corpus\u2019s own counterexample',
     'NEGATIVE AT ALL THIRTEEN CELLS',
     'DOES NOT SEE IT \u2014 at the arc\u2019s cells; the positive control fired on a scope-bound constant',
     'The form represents nothing between 1 and 4, so the finite channel is identically zero until '
     '`a = 2`; a null at these widths is a matter of reach, and the price the act attached to the '
     'reach was withdrawn by the next act.'),
    ('b326', 'the reach: twenty-six cells to `a = 400`, the zero library built, the closure decided',
     "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT.",
     'DOES NOT SEE IT \u2014 to `a = 400`, under the derived kernel; the priced crossing withdrawn',
     'b325\u2019s kernel was half the derived one and the explicit formula\u2019s closure decided it; '
     '146 zeros on the line and 17 off, the count closing. What would see the failure is a family, '
     'not a longer library, and that family was priced and not built.'),
    ('b327', 'the faces ledger built, and the Li-to-Weil bridge read under the import bar',
     'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.',
     'DIFFERENT on both questions \u2014 the ledger filed, certifying nothing; the bridge still owed',
     'The deposit\u2019s archimedean channel is the archimedean distribution on the Li family plus the '
     'pole constant `1`; the two margins are two evaluations of one distribution and are not one '
     'functional. No face is promoted and no equivalence is compiled.'),
    ('b328', 'the discriminating family derived, built, and run as the negative control',
     'SEES IT -- AT SEVEN OF EIGHT CELLS.',
     'SEES IT \u2014 on this family, at this reach, with zeta holding at all eight; three sealed bars defective',
     'A lawful seed\u2019s four-term sum at an off-line quadruple is negative only past forty-five '
     'degrees of phase, and an even seed reaches it; the verdict is on this family, on this '
     'instrument, at this reach, and says nothing about the method or about zeta.'),
    ('b329', 'the finite side compiled: the decomposition and the scaling part general, the compact part per cell',
     "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS",
     'BUILT \u2014 24 terminals, every one zero-axiom; general and per-cell stated in the header',
     'What is compiled is the arithmetic of the model and the counting form of the trace; the '
     'identification with the source\u2019s trace is b310\u2019s derivation and is not. Coprimality '
     'is replaced by equations with witnesses and primality is used nowhere.'),
    ('b330', 'the arc\u2019s methods extracted into TECHNE\u2019s private core, and the kernel\u2019s line endings cured',
     "THE ARC'S METHODS ARE CLAIM-SHAPED MODULE DRAFTS IN TECHNE'S PRIVATE CORE, WITH THEIR",
     'FILED \u2014 twenty modules, local, NOT PUSHED; method only, no grade conferred',
     'Nothing about the programme\u2019s objects enters TECHNE, and nothing from TECHNE is public until '
     'its provisionals are filed. The August files are untouched; the two-clone divergence is read, '
     'not resolved.'),
]

# ### (act, THE OBSTACLE, QUOTED FROM THAT ACT)
OBSTACLES = [
    ('b323', 'IN NO CASE WAS THE SEALED FILE EDITED.'),
    ('b324', 'THE DEPOSIT DELIBERATELY WITHHOLDS IT'),
    ('b325', 'A CONTROL WHOSE CORRECT ANSWER IS KNOWN IN ADVANCE HAD GIVEN THE WRONG'),
    ('b326', 'THE PRICED CROSSING WAS AN ARTEFACT, AND THE CLOSURE DECIDED IT.'),
    ('b327', 'The ledger certifies nothing and says so before its purpose does.'),
    ('b328', 'IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES.'),
    ('b329', "IT DOES NOT SAY THE COMPACT PART'S SILENCE IS PROVED IN GENERAL."),
    ('b330', 'IT DOES NOT SAY ANY METHOD IS NOVEL IN LAW.'),
]

# ### (act, what was corrected, WHAT DID NOT MOVE)
CORRECTIONS = [
    ('b324', 'the reason (F2) registered for the missing bridge \u2014 that the register map does not '
     'yet supply it \u2014 is replaced by the deposit\u2019s own: it withholds the bridge by design',
     'the direction of (F2), which is confirmed; every keystone, which is read and not edited'),
    ('b326', 'b325\u2019s priced crossing at `a = 22` \u2014 an artefact of an archimedean kernel that '
     'was half the derived one; the explicit formula\u2019s closure decided it',
     'b325\u2019s verdict at the arc\u2019s cells, which stands; b325\u2019s sealed file, which is not '
     'edited'),
    ('b327', 'the bench\u2019s literature dictionary disagrees with the balance keystone\u2019s '
     'literature column at `n = 3` and `n = 5` \u2014 a typed fixture, filed against the bench',
     'the computation, which matches the keystone\u2019s column to fourteen digits; the keystone, '
     'which is not edited'),
    ('b328', 'the act\u2019s first diagnosis of its failing route bar (a second-order grid term) was '
     'refuted by its own doubling ratio and replaced by the correct one (a quadrature straddling a '
     'kink on the native nodes)',
     'the first diagnosis, kept on disk under its own name beside the corrected one'),
    ('b329', 'three registered bars written in the library\u2019s coprimality vocabulary are not met '
     'in that form, because the library\u2019s lemmas carry an axiom the audit bar forbids; the '
     'statements are equations with witnesses',
     'the theorems\u2019 mathematics; the sealed registration; nothing sorried, nothing weakened silently'),
    ('b330', 'the order named `modules/INDEX.md` and the August index sits at `modules/2026-08/INDEX.md`; '
     'a top-level index was created and the reading declared before the write',
     'the August files, byte-identical and still untracked as b257 left them'),
]

# ### (act, the bar, what was wrong with it, what the act did about it)
DEFECTIVE_BARS = [
    ('b325', 'every bar written after the instrument had run', 'the seat ran ahead of its own execution '
     'block, so its own bars could have been fitted to values already seen',
     'sealed the registration with that as its section (0) and marked every bar `[ORDER]` or '
     '`[SEAT, POST-HOC]`, so a reader may discount the second class entirely'),
    ('b326', 'three of its own registered estimates', 'a precision sixty digits short of the cancellation; '
     'a truncation list missing the archimedean `u`-range; a closure tool whose first run aliased the '
     'high ordinates', 'caught each before it reached a verdict and kept each on disk under its own name'),
    ('b328', '`(B1)`, `(B4)`, and `(B6)`\u2019s archimedean arm', 'a relative tolerance measured against a '
     'discretized object; a quadrature that straddles a kink in every triple on the native nodes; a '
     'route arm on one class of cells', 'ran each, measured the miss, named the mechanism, edited none, '
     'and showed the signs rest on gates that hold'),
    ('b329', '`(T1.4)`, `(T1.6)`, `(T2.1)` in their registered form', 'written in the library\u2019s '
     'coprimality vocabulary, whose lemmas carry `propext`; the audit bar is zero axioms',
     'declared each not met in its registered form, compiled the same mathematics as equations with '
     'witnesses, and let primality go unused rather than borrow the word'),
    ('b330', '`(F8)`, the bare word \u201cclaim\u201d outside the header sentence', 'two modules carry '
     'the word where it means an assertion \u2014 a hedge audit\u2019s own vocabulary and an ordinary verb '
     '\u2014 and the local commit\u2019s cap was one', 'declared, not edited, not re-committed; the arm '
     'asserts the declared state and no claim language anywhere'),
]

# ### (act, the seat's own defects, declared)
DEFECTS = [
    ('b323', 'a generator with no idempotence guard that filed the arc twice before commit; a sentence '
     'asserting a byte difference its own measurement showed was zero'),
    ('b325', 'the seat ran ahead of its own execution block; the constant that bit was scope-bound and '
     'its scope had never been written down'),
    ('b326', 'three estimates failing their own gates (precision, truncation list, aliasing), each '
     'caught before a verdict'),
    ('b327', 'a mis-typed pin fragment refused by the row-writer\u2019s quotation guard; the bench\u2019s '
     'literature dictionary disagreeing with the keystone at two indices'),
    ('b328', 'zero-byte cell records left by a JSON dump that raised; a lore marker without its '
     'escaped apostrophe; a two-path writer that overwrote its first record; three sealed bars defective'),
    ('b329', 'a first draft whose general theorems carried `propext` (no profile written from it); a '
     'docstring regex that swallowed a section comment; an index location typed before its rows '
     'existed; a kernel tool not idempotent as written; the post-push gate firing on autocrlf\u2019s rewrite'),
    ('b330', 'a quotation check that compared wrapped quotations raw; a tool name carrying a research '
     'stem; two quotations re-anchored; the struck-clause sweep run only after the local commit; a '
     'literal bar not met on two modules'),
]

# ### THE LORE THIS ARC LEAVES. ### (rule, the incident, MECHANIZED or JUDGEMENT, the TECHNE module)
LORE = [
    ('A constant is scope-bound and its scope is written down; a tuple that was ample where it was '
     'born is a tuple, not a law.',
     'b325\u2019s positive control returned a value b321\u2019s own theorem forbids, because a prime '
     'tuple copied from the atlas was carried to a width where it missed almost every prime in range; '
     'b326 generated the set to the reach and put the scope in the header.', 'MECHANIZED',
     'SCOPE_BOUND_CONSTANT.md'),
    ('A lawful test function\u2019s four-term sum at an off-line quadruple is `4 Re(G_e^2 - G_o^2)`: an '
     'even seed sees the zero only past forty-five degrees of phase, an odd component only below it.',
     'b326\u2019s two families both came out positive at the first off-line quadruple, at phases '
     'between \u22125 and 24 degrees; b328 derived the condition and built a seed at 89.', 'MECHANIZED',
     'NEGATIVE_CONTROL_PROTOCOL.md'),
    ('General and per-cell are stated in the module header, never averaged.',
     'b329 compiled the law b309\u2019s header had called uncompiled, without letting the per-cell arm '
     'borrow the word; a header gate fires on an averaging header.', 'MECHANIZED',
     'GENERAL_AND_PER_CELL.md'),
    ('A sealed bar found defective by running it is measured and tabled, never edited.',
     'b328 tabled three; b329 three registered forms; b330 one literal bar \u2014 none edited, each '
     'measured, the first wrong diagnosis kept where there was one.', 'MECHANIZED',
     'SEALED_BARS_FOUND_DEFECTIVE.md'),
    ('Disk bytes must equal blob bytes; a raw byte comparison on a clean tree is otherwise git\u2019s '
     'artifact.',
     'b329\u2019s post-push gate fired on the registration\u2019s raw hash and on file times rewritten '
     'by the checkout; b330 gave the kernel repository the papers repository\u2019s `.gitattributes` '
     'and verified the profile equal to its blob raw.', 'MECHANIZED',
     'COLD_CLONE_CERTIFICATION.md'),
    ('Method crosses into the private core; research content does not.',
     'b330\u2019s research-vocabulary sweep fired on this seat\u2019s own writing \u2014 a generator named '
     'by a research stem \u2014 and the line was rephrased.', 'MECHANIZED',
     'EXTRACT_TO_DISK.md'),
    ('A null is attributed to the family, the reach, or the library, in that order, before it is '
     'read as a finding.',
     'b325 attributed its null to reach and priced it; b326 withdrew the price and priced the family; '
     'b328 built the family and the instrument said no.', 'JUDGEMENT', ''),
    ('A price attached to a reach is withdrawn by the measurement that could not be made when it was '
     'attached, and the attaching act is not re-verdicted.',
     'b326 withdrew b325\u2019s priced crossing by the closure b325 could not run.', 'JUDGEMENT', ''),
    ('A bench fixture that disagrees with a keystone is filed against the bench, not edited into it.',
     'b327\u2019s literature dictionary at `n = 3` and `n = 5`.', 'JUDGEMENT', ''),
    ('A registered bar written in a library\u2019s vocabulary can be unmet for the toolchain\u2019s '
     'reason and not the mathematics\u2019; register bars in mathematical form.',
     'b329\u2019s three coprimality bars.', 'JUDGEMENT', ''),
    ('A quotation of a quotation is not a source, and the judgement that a sentence is an act\u2019s '
     'own voice is the seat\u2019s and is declared.',
     'carried from b283 through every fold; declared again here.', 'JUDGEMENT', ''),
]

# ### (tool, what it catches, the incident)
SUITE = [
    ('`b327_faces_row.py` + `b327_faces_census.py`', 'a ledger row whose quotation is not in its emitter; '
     'a duplicate row; a face missing from the ledger', 'the writer refused b327\u2019s own R4 row on a '
     'mis-typed pin fragment; the census licenses the phrase the strike removed.'),
    ('`b328_family.py` (fixtures)', 'a seed that does not reach the phase condition',
     'both polarities in its fixtures (60 degrees negative, 30 positive; the odd part the other way round).'),
    ('`b329_header_gate.py`', 'a kernel module header that averages general and per-cell',
     'fires on an averaging header, quiet on `FiniteSideSeal.lean`\u2019s; in the lore\u2019s self-test.'),
    ('`b329_kernel.py` + `b329_axiom_probe.py`', 'a terminal depending on an axiom; a profile that is '
     'not the old one plus the act\u2019s prints; a library lemma carrying `propext`',
     'the probe measured 36 of 85 prints carrying axioms and the module was rewritten before any '
     'profile was written.'),
    ('`b330_modules_check.py`', 'a method module carrying research vocabulary, a provenance line with '
     'no emitter, a quotation not in the extract file, a module missing from the index',
     'it refused twice before the modules passed, and fired on this seat\u2019s own tool name.'),
    ('`b330_eol.py`', 'a tracked working copy whose line endings differ from its blob',
     '21 of 123 before the attributes file; 0 of 124 after; the profile equal to its blob raw.'),
    ('`b330_techne_state.py`', 'a TECHNE push; an August file changed; the second clone touched',
     'the remote tip read before and after; the August files hashed before and after.'),
    ('`noise_floor.py` at every sign', 'a sign read off a value at the floor',
     'every places-side sign in b325, b326 and b328 went through it at two grids.'),
    ('the extract step (`bNNN_extract.py`)', 'a needle typed from memory',
     'b331\u2019s own first run refused one anchor that spanned two lines; it was narrowed to the emitted line.'),
]

# ### (item, its state, what it needs)
DESK = [
    ('**`M-2`**', '`(SPECIFIED-NOT-STATED)`, unchanged across all eight acts, under b310\u2019s cap',
     'no act in this arc states it and no aggregation is stated.'),
    ('**The object\u2019s three conditions**', 'each typed \u2014 a premise, a ruling, a construction',
     '**a condition discharged is not the object constructed.**'),
    ('**The exponent\u2019s ratio**', '`0.393` \u2014 the instrument\u2019s residual falls as `X^-1.324` '
     'against the unit\u2019s `X^-0.520` (b323, from b321/b322)',
     'the resolving power priced twice and both prices beyond reach; unchanged by this arc.'),
    ('**The Li-to-Weil bridge**', 'OWED \u2014 `W-ORD-LI-WEIL-BRIDGE` on the trails; the map derived, '
     'the bridge read DIFFERENT on both questions (b327)',
     'a formula carrying the archimedean margin at a lawful test function to the Li margin at an '
     'index, or a proof that none exists.'),
    ('**The Li bench versus the keystone**', 'the bench\u2019s literature dictionary disagrees with the '
     'balance keystone\u2019s column at `n = 3` and `n = 5` (b327)',
     'a typed fixture, filed and not edited; the computation matches the keystone to fourteen digits; '
     'the author\u2019s to reconcile.'),
    ('**The August TECHNE files, and the two clones**', 'the nine August files untracked as b257 left '
     'them; `TECHNE-Core` at a local commit one ahead of the remote, `TECHNE_Core` diverged',
     '**both the author\u2019s:** whether to commit the August files, and whether to reconcile the clones.'),
    ('**The compact part beyond the cells**', 'PROVED-AT-CELLS \u2014 seven cells decided; the general '
     'zero is orthogonality to the valuation shells, not vanilla-decidable',
     'a certification beyond cells would be new mathematics under the arc\u2019s rule and is not this '
     'seat\u2019s to add.'),
    ('**The discharge-statement and the aim-map**', 'NAMED AS THE NEXT TWO RESEARCH ACTS, by the order',
     '**neither is the discharge.** A statement of what would discharge the open clause, and a map of '
     'where the corpus aims at it, are a statement and a map.'),
    ('**The reconciliation wave**', 'the author\u2019s; b324\u2019s candidate list typed, not ranked',
     'four `[NEW]` items (the certified archimedean instrument; the measured identity along the '
     'domain ladder; the balance non-positive by construction; the resolving-power rule and its two '
     'prices), one `[REFINEMENT-OF-DEPOSITED]` (the instrument sits inside the first named classical '
     'face of h2), one `[REFINEMENT-OF-INTERNAL]` (the wall\u2019s grading of the source, now '
     'accompanied by a measured instrument); this arc adds the negative control that said no, '
     'typed here as a candidate and not a recommendation.'),
    ('**The seam\u2019s debt, item 1**', 'STILL UNPAID', 'restated, not discharged.'),
    ('**The patent receipts**', 'UNCONFIRMED on this seat\u2019s record; the handoff carries them '
     'pending on the ferry\u2019s word, three days past both dates as of its last bringing-current',
     '**the one item on this desk with a date;** carried on the patent seat\u2019s report.'),
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
    sep = os.path.join(r'D:\MY-DOwnloads\TECHNE-Core', 'modules', '2026-09')
    missing = [m for _r, _i, k, m in LORE if k == 'MECHANIZED' and not os.path.exists(os.path.join(sep, m))]
    rec('  F-MODULES: every mechanized rule names a TECHNE module on disk : %s %s' % (not missing, missing if missing else ''))
    return not missing


def emit_markdown():
    L = []

    def A(s=''):
        L.append(s)

    A('## %s' % SECTION)
    A('')
    A('**Eight acts, 2026-09-04 to 2026-09-06.** A filings section: **no grade moves here, no act is '
      're-verdicted, and nothing below is new mathematics.** Each entry carries its grade as *its own '
      'act* left it and its own scope sentence, and every quotation was checked verbatim against the act '
      'that **originated** it before this section was emitted.')
    A('')
    A('### The eight')
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
    A('**The prior fold opened this table with three bars in nine acts. This arc adds five rows in '
      'eight.** In no case was a sealed file edited; in every case the defect was found by running the '
      'bar and reading what came back.')
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
    A('At the grade these eight acts support, and no higher: **the instrument can say no.** Run on the '
      'corpus\u2019s own counterexample \u2014 a function with zeros off the line \u2014 it said no on '
      'the arc\u2019s family at every reach tried (b325, b326), and the reason was named from the numbers: '
      'the family, not the library. A condition on the family was derived from the source\u2019s own '
      'formula \u2014 the four-term sum at an off-line quadruple is negative only past forty-five '
      'degrees of phase \u2014 and a seed built to it made the instrument say no at seven of eight cells '
      'while **the zeta window held at all eight** (b328). **So the zeta window is a passed test for the '
      'discriminating family at this reach**, and for the arc\u2019s family b326\u2019s verdict stands '
      'unmoved. **The finite side is compiled** (b329): the decomposition and the scaling part general '
      'over every base, level, power and index, the compact part per cell at the seven banked cells, '
      'the two scopes stated in the module\u2019s own header and never averaged, every terminal '
      'zero-axiom. **The two margins are two evaluations of one distribution separated by the pole** '
      '(b324, b327): the deposit\u2019s archimedean channel is the archimedean distribution on the Li '
      'family plus the constant `1`, and the arc\u2019s margin is the same distribution on the '
      'arc\u2019s family minus a compressed square \u2014 one distribution on two families, not one '
      'functional, with the bridge between them owed. **The object\u2019s archimedean unit is in its '
      'space by derivation and priced at bench** \u2014 the derivation b300\u2019s, the price b322\u2019s, '
      'unchanged by this arc. **And the clause has not moved:** no act in the arc claims otherwise, '
      'and the keystone re-read found the arc\u2019s source already graded as stalling at exactly the '
      'clause the arc\u2019s instrument stalls at.')
    A('')
    A('**Scope, printed beside it.** This is a summary of eight acts at their own grades. **No theorem '
      'is proved here and none was proved by any act in the arc.** The instrument\u2019s no is a verdict '
      'on one family, on one instrument, at one reach, and says nothing about the method or about '
      'zeta; the passed test is passed *for that family*. The compiled finite side certifies the '
      'model\u2019s arithmetic and the counting form of the trace, not the identification of that count '
      'with the source\u2019s trace, and not the compact part beyond the cells. The two margins\u2019 '
      'relation is a reading under an import bar, with the bridge owed on the trails by ID. **Nothing '
      'about the identity, `h2`, or the complete roster follows from any of it. `M-2` is owed and no '
      'aggregation is stated. Nothing about the register sentence moves.**')
    A('')
    A('### The lore this arc leaves, with the incident that bought each rule and its TECHNE module')
    A('')
    A('**Mechanized** \u2014 a gate, a fixture or a tool enforces it; the TECHNE module b330 wrote for '
      'it is named beside it (private, local, not pushed):')
    A('')
    for rule, inc, kind, mod in LORE:
        if kind == 'MECHANIZED':
            A('- **%s** *Incident:* %s *Module:* `modules/2026-09/%s`' % (rule, inc, mod))
    A('')
    A('**Judgement** \u2014 no mechanism enforces it and a seat must apply it:')
    A('')
    for rule, inc, kind, _mod in LORE:
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
    rec('b331 -- THE FOLD, b323-b330. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)
    text_by_act = {}
    for act in ARC:
        text_by_act[act] = io.open(os.path.join(D, SRC[act]), encoding='utf-8', errors='replace').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)' % len(text_by_act))
    q_ok = fquote(text_by_act, rec)
    c_ok = fcount(rec)
    m_ok = fmodules(rec)
    rec('  ### **THE JUDGEMENT THE MECHANISM DOES NOT MAKE:** ### that each sentence is that act\'s OWN')
    rec('  ### VOICE and not material it was itself quoting. ### **THAT IS THIS SEAT\'S** and the bank declares it.')
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
    delta = len(before.encode('utf-8')) - len(blob.encode('utf-8'))
    rec('    ### the two %s' % ('DIFFER BY %+d BYTES, which is git\'s line endings and not the record' % delta if delta else 'are the same length here (the papers repository carries `eol=lf`)'))
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
    base = 'b331_fold_run'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(OUT) + '\n')
    sys.exit(code)
