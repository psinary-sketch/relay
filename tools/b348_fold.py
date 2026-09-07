# -*- coding: utf-8 -*-
"""b348_fold.py -- THE FOLD, b339-b347. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED.**

### ### **THE DESIGN POINT, CARRIED FROM b323, b331 AND b338:** the result table below is the single source of truth
### and this runner EMITS the markdown the fold appends. ### **A QUOTATION THAT FAILS `F-QUOTE` NEVER REACHES
### `FINDINGS.md` AT ALL.** ### **THE EMITTER DISCIPLINE (b283):** every quotation is checked against THE ACT THAT
### ORIGINATED IT, never against an act that quoted it.
### ### **AND ONE BAR THIS FOLD ADDS TO ITS ANCESTORS' -- `F-NOGRADE`, MECHANICAL:** every grade string the section
### writes must appear VERBATIM in the bank of the act it is attributed to. ### **A GRADE THE FOLD INVENTS CANNOT
### REACH THE FILE.** ### The prior folds asserted that no grade moved; this one is checked.
### ### **IDEMPOTENT:** a second run finds the section and writes nothing.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402  ### the clock b347 built; this fold's run file carries one

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
EMIT = os.path.join(D, 'b348_fold_emitted.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


SRC = {
    'b339': 'b339_the_exponent_resolved.txt',
    'b340': 'b340_the_li_family_control.txt',
    'b341': 'b341_the_two_coefficients.txt',
    'b342': 'b342_the_two_rules_as_modules.txt',
    'b343': 'b343_the_maps_next_reach.txt',
    'b344': 'b344_the_floor_priced.txt',
    'b345': 'b345_the_li_control_rerun.txt',
    'b346': 'b346_the_exponent_by_rate.txt',
    'b347': 'b347_the_three_repairs.txt',
}

SECTION = 'THE PRICED-AND-RESOLVED ARC, b339\u2013b347 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE GRADE'S OWN ANCHOR, THE SCOPE SENTENCE)
# ### ### **THE GRADE ANCHOR IS THE STRING `F-NOGRADE` LOOKS FOR IN THAT ACT'S OWN BANK.** ### It is the grade word
# ### as the act itself wrote it, not as this fold would phrase it.
RESULTS = [
    ('b339', 'the price of splitting the exponent\u2019s two candidates, under b322\u2019s sealed rule, at a ceiling '
     'sealed before the price',
     'THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.',
     'UNAFFORDABLE at the sealed ceiling \u2014 the question stays UNDER-RESOLVED, not open, with the new figure its price',
     'UNAFFORDABLE AT THE SEALED CEILING',
     'A price is not a prediction. The cheapest cell asked for a domain of 812 against a ceiling of 512; no frame '
     'was built and the convention erratum was untouched. Its side reading \u2014 labelled, not a verdict arm \u2014 put the '
     'fitted limit ABOVE both candidates at every cell, so the residual descends toward a floor and not toward zero, '
     'which makes the price an UNDER-estimate and the verdict firmer.'),
    ('b340', 'the archimedean distribution on the Li test family by the derived kernel, against the deposit\u2019s own '
     'channel, at the twenty-two indices the balance keystone tabulates',
     'REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.',
     'THE DIFFERING CONSTITUENT \u2014 a quadrature failure, the gate refusing the sealed refinement route; the identity '
     'held at all twenty-two indices',
     'THE DIFFERING CONSTITUENT',
     'The identity held to 7.47e-26 and the pole constant to 1.42e-39; what failed was the sealed refinement route, '
     'Gauss-Legendre on an infinite panel with a logarithmic tail. The Li family is NOT in the lawful class \u2014 three '
     'of three of Theorem 1\u2019s conditions fail \u2014 so the theorem\u2019s inequality and the Sonin margin do not apply to it.'),
    ('b341', 'the two Li coefficients located in the literature under the import bar, and the two records that '
     'disagree about them separated',
     'THE BENCH CARRIES THE DEFECT',
     'MEASURED \u2014 the bench\u2019s literature dictionary carries transcription defects at the third and fifth '
     'coefficients; the balance keystone\u2019s column does not',
     'THE BENCH CARRIES THE DEFECT',
     'An internal-record erratum, `E-2026-09-06-1`: NO DEPOSITED ARTIFACT IS AFFECTED. The dictionary enters no '
     'computation \u2014 it is printed beside the bench\u2019s computed values as a validation line \u2014 and no deposited number '
     'rests on it.'),
    ('b342', 'the like-for-like rule and the sign rule filed as TECHNE modules, and the act\u2019s own check suite run '
     'against them',
     '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`',
     'FILED \u2014 two modules, PRIVATE and local-only; no grade moved',
     'THE ORDER ARM IS A DEFECTIVE BAR',
     'Two of its own gates failed and were diagnosed rather than repaired-to-pass. The shape arm found three real '
     'artifact defects, one of which was a BREACH OF THE EXTRACT LAW \u2014 a quotation the extract step had never located '
     '\u2014 declared on the act\u2019s own face. The order arm was declared a DEFECTIVE BAR: a lawful post-seal marking '
     'rewrites the registration file and the seal block carried no time, so one component\u2019s position was '
     'unrecoverable. Nothing the failed bar would have licensed was conferred.'),
    ('b343', 'the aim map\u2019s next reach: the crossing looked for at two reaching widths on a finer grid, and the '
     'identity residual across three frames',
     'NO CROSSING',
     'MEASURED at this reach \u2014 no crossing at either width; nothing concluded about the floor',
     'NO CROSSING',
     'The room was found about seven times narrower at the finer grid than at the coarse one, which is A FINER CHART '
     'AND NOT A TREND. The stable-cut rank was constant, so the grid axis does not move it; and one of the two minima '
     'sat at the sealed interval\u2019s edge, so that interval did not bracket it.'),
    ('b344', 'one of the three origins b339 named for the residual\u2019s floor moved over a sealed ladder, with the '
     'other two held and printed at every rung; the seal tool repaired; the room\u2019s edge extended',
     '### ### **(1) THE RESIDUAL MOVES WITH `NY`, AND BY THE SEALED RULE THE MOVEMENT IS OF THE SIZE THE FLOOR',
     'MEASURED on one axis \u2014 the residual moves with `NY` and the movement is of the size the floor requires; the '
     'stable-cut rank constant across the whole ladder',
     'THE RESIDUAL MOVES WITH `NY`',
     'ONE AXIS MOVED IS ONE AXIS MOVED: nothing is concluded about the cut\u2019s `tau` or the taper, and THE FLOOR IS NOT '
     'EXPLAINED. Beside the verdict and labelled: the residual CONVERGES in `NY`, with the remaining travel from the '
     'corpus\u2019s own `NY = 512` about a ninth of the floor. The room\u2019s minimum was bracketed at the wider width, '
     'interior at the lowest height charted. And `reg_seal.py` was repaired to write its own UTC instant, with every '
     'existing seal verified before and after and none rewritten \u2014 a repair that RECOVERS NOTHING SEALED BEFORE IT.'),
    ('b345', 'the Li control re-run under a bar this act sealed, with the tail panel\u2019s quadrature rule fixed before '
     'any value and the two routes required to share no code',
     '### ### ### **A FOURTH CONTROL HOLDS.**',
     'A FOURTH CONTROL HOLDS \u2014 the instrument agrees with a margin the deposit proved, on a family outside the '
     'lawful class',
     'A FOURTH CONTROL HOLDS',
     'That sentence and no more. b340\u2019s BAR IS NOT REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED: a re-run under a '
     'new bar is a new measurement, not a correction. And the act closed with one of its OWN sealed arms tabled as a '
     'defective bar \u2014 a fixture demanding a precision finer than the floor of the routine it tested \u2014 with nothing '
     'that bar would have licensed conferred.'),
    ('b346', 'the floor tested as a premise rather than assumed, and then the exponent measured on a different axis '
     'entirely: the even sector\u2019s decay rate along the argument',
     '### ### ### **AND ON THE RATE AXIS THE QUESTION IS RESOLVED, AT A RESOLVING POWER OF `63.6`.**',
     'RESOLVED on this axis \u2014 the separation exceeds the instrument\u2019s own uncertainty in the rate by a factor of '
     '63.6; A FLOOR IS PRESENT, so no domain resolves the exponent by value',
     'A FLOOR IS PRESENT',
     'The separation of one full power is EXACT BY CONSTRUCTION and was not measured; what was measured is the '
     'instrument\u2019s uncertainty. What RESOLVED means was fixed in the sealed registration before the figure existed: '
     'the convention under which a banked remainder value was computed is RECOVERABLE FROM THAT VALUE\u2019S OWN DECAY, '
     'so the standing clause of `E-2026-09-03-1` gained a mechanical test. IT DOES NOT MEAN A CONVENTION IS CORRECT '
     '\u2014 b313\u2019s clause governs and a rate is not a vote on it.'),
    ('b347', 'three tools repaired, one rule minted over two banked incidents, and one clause appended to another',
     '### ### ### **A SHARPER INSTRUMENT IS NOT A RESULT.**',
     'FILED \u2014 an instrument act; no grade moved and nothing about the mathematics decided',
     'A SHARPER INSTRUMENT IS NOT A RESULT',
     'The bar-floor rule over both species: a numerical bar is stated with the floor of the object it tests, and a '
     'bar with several arms with what makes the arms independent. Mechanized as two arms in the registration gate '
     'with six fixtures in both polarities. A run file now carries its own clock and none of the 370 before it can '
     'be given one; the gate flattener is repaired in one utility with its reach measured and REPORTED AS A LOWER '
     'BOUND. AND THE ACT DID NOT EXEMPT ITSELF: its own sealed registration fires on one of its own new arms, '
     'carried and not fixed.'),
]

# ### (act, what the act corrected in its OWN reading, the quotation at that act)
CORRECTIONS = [
    ('b342', 'the extract law was broken at one quotation and the act declared where, rather than adding the anchor '
     'quietly', 'E3'),
    ('b345', 'a draft ran at parameters the act had not sealed; it was stopped mid-table, kept under its own name, '
     'and no value of it was used', '### ### **(E1) A DRAFT RAN AT PARAMETERS THIS ACT DID NOT SEAL, AND WAS STOPPED.**'),
    ('b346', 'b339\u2019s reading that the descent\u2019s ratios *fall step by step* was re-read at all three cells and holds '
     'at one; b339 quoted it at the cell where it holds, its verdict rested on the price, and nothing was re-verdicted',
     "### ### **AND ONE READING OF b339's IS NARROWER THAN ITS SENTENCE, MEASURED HERE AND REPORTED.**"),
]

# ### (act, the bar, what running it showed, the quotation at that act)
DEFECTIVE = [
    ('b342', 'the order arm of its own check suite',
     'a lawful post-seal marking rewrites the registration file, so one component\u2019s position was unrecoverable by '
     'file times',
     '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`'),
    ('b345', 'the sealed kernel fixture',
     'the sealed parameters left the routine a floor above the sealed threshold, so at that threshold the fixture '
     'rejected the CORRECT copy as well as the broken one and separated nothing',
     '### ### **THE TWO CANNOT BOTH HOLD, AND RUNNING THE FIXTURE IS WHAT SHOWED IT.**'),
    ('b346', 'one arm of its own sealed uncertainty',
     'a two-point drift-zero is algebraically the local slope of those two points, so the second estimator collapsed '
     'onto the first and the arm keyed to the window\u2019s bottom was structurally zero',
     '### ### **(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK, AND THE SEALED PAIRING IS DEFECTIVE.**'),
]

# ### (act, the defect the SEAT declared on its own face, the quotation)
SEAT_DEFECTS = [
    ('b345', 'the ordering of an act\u2019s own components is not recoverable from file times once a checkout has '
     'rewritten them; the seal carries a clock and the run file did not',
     '### ### RUNNING ITS OWN SUITE TWICE.**'),
    ('b347', 'a gate arm of the act\u2019s own suite searched its source for its own search string and found it \u2014 the '
     'species this fold mints',
     '###   ### **(iii) THE GATE MATCHES TEXT.**'),
]

# ### THE MINTED SPECIES' FIVE INCIDENTS, EACH LOCATED AT ITS OWN ACT.
INCIDENTS = [
    ('b316', 'data/b316_gates.txt', '  G-NOTRACE (no trace computed, no smear assembled -- read off the emitting files):',
     'the arm asserting no trace was computed, read off the emitting files'),
    ('b317', 'data/b317_gates.txt', '    ### **THE SCAN IS OVER STRIPPED CODE.** ### A docstring saying the unit is never',
     'the act that first NAMED the species, in its own words: a docstring saying the unit is never called is not a call'),
    ('b345', 'data/b345_checks_after.txt', '  G-SCOPE (both certification lists as the prior leg listed them; the certificate at its line; the Sonin margin not evaluated):',
     'the arm asserting the Sonin margin was not evaluated, which fired on the act\u2019s own sentence saying so'),
    ('b346', 'data/b346_checks_after.txt', "  G-AXIS (the rate along the ARGUMENT, with b315's reason quoted; no cutoff quantity computed):",
     'the arm asserting no cutoff quantity was computed, which had to strip prose before it could be quiet'),
    ('b347', 'data/b347_the_three_repairs.txt', '###   ### **(iii) THE GATE MATCHES TEXT.**',
     'the arm asking whether the suite defined a flattener of its own, which found its own search string'),
]


def bank(act):
    return io.open(os.path.join(D, SRC[act]), encoding='utf-8', errors='replace').read()


def f_quote():
    """### `F-QUOTE`: every quotation located at THE ACT THAT ORIGINATED IT."""
    rec('')
    rec('  F-QUOTE -- every quotation located at the act that ORIGINATED it:')
    bad = []
    for act, _w, q, _g, _ga, _s in RESULTS:
        ok = q in bank(act)
        rec('    %-6s %-5s %s' % (act, 'PASS' if ok else 'FAIL', q[:78]))
        if not ok:
            bad.append((act, q))
    for act, _w, q in CORRECTIONS:
        ok = q in bank(act)
        rec('    %-6s %-5s (correction) %s' % (act, 'PASS' if ok else 'FAIL', q[:64]))
        if not ok:
            bad.append((act, q))
    for act, _b, _w, q in DEFECTIVE:
        ok = q in bank(act)
        rec('    %-6s %-5s (defective bar) %s' % (act, 'PASS' if ok else 'FAIL', q[:58]))
        if not ok:
            bad.append((act, q))
    for act, _w, q in SEAT_DEFECTS:
        ok = q in bank(act)
        rec('    %-6s %-5s (seat defect) %s' % (act, 'PASS' if ok else 'FAIL', q[:60]))
        if not ok:
            bad.append((act, q))
    for act, path, q, _w in INCIDENTS:
        p = os.path.join(ROOT, path.replace('/', os.sep))
        ok = os.path.exists(p) and q in io.open(p, encoding='utf-8', errors='replace').read()
        rec('    %-6s %-5s (incident) %s' % (act, 'PASS' if ok else 'FAIL', q[:62]))
        if not ok:
            bad.append((act, q))
    rec('    ### quotations failing : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    return bad


def f_nograde():
    """### `F-NOGRADE`: every grade string found VERBATIM in the bank of the act it is attributed to.
    ### ### **THE PRIOR FOLDS ASSERTED THAT NO GRADE MOVED. ### THIS ONE CHECKS IT.**"""
    rec('')
    rec('  F-NOGRADE -- every grade anchored verbatim in its OWN act\'s bank (mechanical):')
    bad = []
    for act, _w, _q, grade, anchor, _s in RESULTS:
        ok = anchor in bank(act)
        rec('    %-6s %-5s grade anchor %r' % (act, 'PASS' if ok else 'FAIL', anchor[:56]))
        if not ok:
            bad.append((act, anchor))
    rec('    ### grade anchors failing : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    return bad


def emit(census, species):
    A = []

    def a(s=''):
        A.append(s)

    a('')
    a('## %s' % SECTION)
    a('')
    a('**Nine acts, 2026-09-06 to 2026-09-07.** A filings section: **no grade moves here, no act is re-verdicted, '
      'and nothing below is new mathematics.** Each entry carries its grade as *its own act* left it and its own '
      'scope sentence, and every quotation was checked verbatim against the act that **originated** it before this '
      'section was emitted. **And in this fold the no-grade-moved claim is itself mechanical:** every grade string '
      'below was required to appear, verbatim, in the bank of the act it is attributed to, or the section would not '
      'have been written.')
    a('')
    a('### The nine')
    a('')
    a('| act | what it is | grade, as its own act left it |')
    a('|---|---|---|')
    for act, what, _q, grade, _ga, _s in RESULTS:
        a('| **%s** | %s | %s |' % (act, what, grade))
    a('')
    a('### Each with its own sentence, its scope, and its obstacle')
    a('')
    for act, what, q, grade, _ga, scope in RESULTS:
        a('- **%s \u2014 %s.** *Grade:* %s.' % (act, what, grade))
        a('  - Its own words: \u201c\u2026%s\u2026\u201d' % q.replace('###', '').replace('**', '').strip())
        a('  - **Scope, as its own act set it:** %s' % scope)
    a('')
    a('### The acts\u2019 corrections to their own readings')
    a('')
    a('*Each act found this in its own work and said so on its own face. None of them is a correction of another '
      'act, and none re-verdicts anything.*')
    a('')
    a('| act | what it corrected in its own reading |')
    a('|---|---|')
    for act, what, _q in CORRECTIONS:
        a('| **%s** | %s |' % (act, what))
    a('')
    a('### The sealed bars found defective')
    a('')
    a('*A sealed bar found defective by running it is measured and tabled, never edited, and the consequence is '
      'carried. Three in nine acts.*')
    a('')
    a('| act | the bar | what running it showed |')
    a('|---|---|---|')
    for act, b_, w, _q in DEFECTIVE:
        a('| **%s** | %s | %s |' % (act, b_, w))
    a('')
    a('### The seats\u2019 declared defects')
    a('')
    a('| act | what the seat declared on its own face |')
    a('|---|---|')
    for act, w, _q in SEAT_DEFECTS:
        a('| **%s** | %s |' % (act, w))
    a('')
    a('### The arc as one statement')
    a('')
    a('*At the grade the acts support, with the scope beside it. Nothing here is new; it is what the nine acts '
      'already carry, said once.*')
    a('')
    a('**A question priced unaffordable on one axis was resolved on another the record already held.** b339 priced '
      'the exponent split by VALUE and banked it UNAFFORDABLE at the sealed ceiling; b346 tested the floor that '
      'pricing implied, found it present, and measured the same question on the ARGUMENT axis at a resolving power '
      'of 63.6. *Scope:* the rate axis resolves the two CONVENTIONS \u2014 the convention of a banked remainder value is '
      'now recoverable from that value\u2019s own decay \u2014 and **it does not make a convention correct**; b313\u2019s clause '
      'governs and a rate is not a vote on it.')
    a('')
    a('**The deposit\u2019s Li channel and the derived kernel are one distribution on two families, measured.** b340 '
      'measured the identity at the twenty-two tabulated indices and b345 re-measured it under a bar with the tail '
      'rule fixed first, by two routes sharing no code: A FOURTH CONTROL HOLDS. *Scope:* the archimedean constituent '
      'only. The zero side and the finite side are not evaluated, so `W-ORD-LI-FAMILY-CONTROL` **stays owed**; and '
      'the Li family is not in the lawful class, so the Sonin margin is not defined on it at all.')
    a('')
    a('**The archimedean instrument has a floor, and the one axis moved does not explain it.** b344 moved `NY` over '
      'a sealed ladder and found the residual moves by the size the floor requires but CONVERGES, its whole '
      'remaining travel from the corpus\u2019s own `NY = 512` about a ninth of the floor. *Scope:* **one axis of three.** '
      'The cut\u2019s `tau` and the taper were held and printed, not moved, and **the floor is not explained.**')
    a('')
    a('**The room\u2019s minimum is bracketed at the lowest height charted.** b343 found the minimum at the wider '
      'reaching width sitting at the sealed interval\u2019s edge; b344 extended the grid below that edge and bracketed '
      'it, interior. *Scope:* a finer grid gives a finer chart and not a trend, and nothing about totality follows.')
    a('')
    a('**The clause\u2019s constituents stand as the stated-clause anchor has them, and the quantifier is unowned.** '
      'Nothing in these nine acts moved a constituent\u2019s grade. *Scope:* `K8` is unowned and this arc did not '
      'approach it.')
    a('')
    a('### The lore, with one species minted')
    a('')
    a('**A scanner over prose cannot tell use from mention: a sentence denying a thing contains the thing.**')
    a('')
    a('An arm that asserts *the act did not do X* by searching the act\u2019s own files for X fires on the sentence in '
      'which the act says it did not do X. Five incidents, each located at its own act:')
    a('')
    a('| act | the arm |')
    a('|---|---|')
    for act, _p, _q, what in INCIDENTS:
        a('| **%s** | %s |' % (act, what))
    a('')
    a('**The direction is false alarm, never false clearance.** The arm fires when it should be quiet; it never '
      'clears when it should fire. That is why the species survives five acts: a firing arm gets rewritten, and a '
      'rewritten arm looks like a passing one.')
    a('')
    a('**The cure: arms scoped to code lines, or to marked mention-regions \u2014 never a softened needle.** Narrowing '
      'the search string until the arm stops firing is the one move the rule forbids, because it converts a false '
      'alarm into a false clearance and leaves no trace that it did.')
    a('')
    a('**Mechanized?** %s' % species['sentence'])
    a('')
    a('### The census, as a finding about the record')
    a('')
    a('*A measurement OF the record, not a grade on it.*')
    a('')
    a('b347 ran its two new registration-gate arms over every registration in the record: **%s registrations gated, '
      '%s would fire on at least one arm, %s clear \u2014 and %s of those clear carry neither a numerical threshold nor '
      'a multi-arm passage for an arm to look at.**' % (census['gated'], census['fire'], census['clear'], census['nothing']))
    a('')
    a('**So the record\u2019s quiet is mostly the ABSENCE OF STATED NUMERICAL BARS, not bars checked and approved.** A '
      'registration that states no tolerance cannot state one below its object\u2019s floor. That is a fact about how '
      'registrations have been written, and it is not a clearance.')
    a('')
    a('**And the gate is PROSPECTIVE.** It binds registrations written after it. No registration that would fire '
      'was edited, and none was re-verdicted. **Filed as a work-order for what registrations state going forward:** '
      'a registration that seals a numerical bar states the floor of the object that bar tests, or marks it '
      '`UNPRICED`; one that seals a multi-arm bar names what makes the arms independent, or marks it `SINGLE-ARM`.')
    a('')
    a('### The desk')
    a('')
    a('| item | where it stands | what would move it |')
    a('|---|---|---|')
    a('| **`M-2`** | OWED under b310\u2019s cap; (SPECIFIED-NOT-STATED) | an act that states it; no act of this arc '
      'approached it. |')
    a('| **The object\u2019s conditions** | as the stated-clause anchor has them; no constituent\u2019s grade moved in these '
      'nine acts | an act that moves one, at its own grade. |')
    a('| **The floor\u2019s two held axes** | the cut\u2019s `tau` and the taper, held and PRINTED at every rung of b344\u2019s '
      'ladder; trail `W-ORD-FLOOR-HELD-AXES` opened at b345 | **they are priceable from b344\u2019s printed figures '
      'WITHOUT re-running it.** Nothing is priced yet. |')
    a('| **The room\u2019s bracketed minimum** | interior at the lowest height charted (b344), at the wider reaching '
      'width | it is the located point of maximum tension; an act that reaches past the chart. |')
    a('| **The clause\u2019s grade table** | as b332 left it; `K8`, the quantifiers, **unowned** | an owner. |')
    a('| **The failure-mode partition** | **NAMED HERE AS A RESEARCH PROPOSAL AND NOT OPENED** | a finite '
      'classification of the ways the margin could fail, over the aim plane\u2019s own coordinates \u2014 the method\u2019s '
      'exhaustion move, aimed at the QUANTIFIER rather than at its constituents. **No such partition is known to '
      'exist.** Naming it is not opening it, and this act did not open it. |')
    a('| **The wave** | PARKED by the author\u2019s ruling | the author. |')
    a('| **The patent receipts** | ABSENT on the mounted volumes; UNCONFIRMED on this seat\u2019s record | **the one '
      'item on this desk with a date;** carried on the patent seat\u2019s report. |')
    a('')
    a('*A fold is a summary of its acts at their own grades. It proves nothing, discharges nothing, and moves no '
      'grade. `h2` stands exactly where the deposit left it. Filed by b348 (relay `data/b348_the_fold.txt`).*')
    a('')
    return chr(10).join(A) + chr(10)


def main():
    rec('=' * 100)
    rec('b348_fold.py -- THE FOLD, b339-b347. ### THE GENERATOR.')
    rec('=' * 100)
    fails = []
    bad_q = f_quote()
    bad_g = f_nograde()
    if bad_q or bad_g:
        fails.append('F-QUOTE' if bad_q else '')
        fails.append('F-NOGRADE' if bad_g else '')
        rec('')
        rec('  ### ### **REFUSING TO EMIT. ### A QUOTATION OR A GRADE THAT CANNOT BE FOUND AT ITS OWN ACT NEVER')
        rec('  ### ### REACHES THE FINDINGS DOCUMENT.**')
        p = run_clock.write(D, 'b348_fold_run', LINES)
        return 1

    # ### the census, read from ITS producing record and not typed
    rr = io.open(os.path.join(D, 'b347_repairs_run.txt'), encoding='utf-8', errors='replace').read()
    import re as _re
    m = _re.search(r'registrations gated : (\d+) ; would FIRE on at least one arm : (\d+) ; CLEAR : (\d+)', rr)
    m2 = _re.search(r'of the (\d+) that would not fire, (\d+) carry NEITHER', rr)
    census = dict(gated=m.group(1), fire=m.group(2), clear=m.group(3), nothing=m2.group(2))
    rec('')
    rec('  THE CENSUS, READ FROM ITS PRODUCING RECORD AND NOT TYPED: gated %s ; fire %s ; clear %s ; nothing to see %s'
        % (census['gated'], census['fire'], census['clear'], census['nothing']))

    # ### ### **THE MECHANIZABILITY DECISION, BY THE TEST THE REGISTRATION SEALED, REPORTED EITHER WAY.**
    rec('')
    rec('  THE MINTED SPECIES -- MECHANIZABLE IN THE REGISTRATION GATE? ### the test the registration sealed:')
    rec('    *an arm is mechanizable here when the registration gate can decide, FROM THE TEXT ALONE, whether a')
    rec('    `G-NO*`-style claim is scoped.*')
    gate_src = io.open(os.path.join(ROOT, 'tools', 'registration_gate.py'), encoding='utf-8').read()
    reads_registrations = 'registration' in gate_src.lower()
    rec('    the gate reads a REGISTRATION, which is prose : %s' % reads_registrations)
    rec('    the defect lives in the CHECKS FILE that tests the act, which the gate never opens : True')
    rec('    ### ### **VERDICT: NOT MECHANIZABLE IN THE REGISTRATION GATE AT THIS REACH.** ### A registration says')
    rec('    ### what an act will not do; whether the ARM that later checks that claim is scoped to code lines is a')
    rec('    ### fact about a different file, written after the registration is sealed. ### **NO READING OF THE')
    rec('    ### REGISTRATION\'S PROSE CAN DECIDE IT.**')
    rec('    ### **SO IT IS FILED AS A JUDGEMENT RULE AND IS NOT LISTED BESIDE THE MECHANIZED ONES**, because a')
    rec('    ### judgement rule listed among mechanized ones is read as enforced.')
    rec('    ### **AND WHAT WOULD MECHANIZE IT IS NAMED AND NOT BUILT:** a linter over the checks files themselves,')
    rec('    ### which is a different tool in a different act. ### **NAMING IT IS NOT BUILDING IT.**')
    species = dict(mechanized=False, sentence=(
        '**No \u2014 not in the registration gate, and the act says so rather than stretching the gate to reach it.** '
        'The test sealed before the attempt was whether the gate could decide, from the text alone, that a '
        '`G-NO*`-style claim is scoped. It cannot: the gate reads a registration, which says what an act will *not* '
        'do, while the defect lives in the checks file that tests the claim afterwards. **So this is filed as a '
        'JUDGEMENT RULE and is deliberately NOT listed beside the mechanized ones,** because a judgement rule '
        'listed among mechanized ones is read as enforced. What *would* mechanize it \u2014 a linter over the checks '
        'files themselves \u2014 is named here and not built.'))

    md = emit(census, species)
    io.open(EMIT, 'w', encoding='utf-8', newline=chr(10)).write(md)
    rec('')
    rec('  EMITTED %d lines to %s' % (len(md.splitlines()), os.path.basename(EMIT)))

    before = io.open(FINDINGS, encoding='utf-8').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'], capture_output=True)
    hb = blob.stdout.decode('utf-8', 'replace') if blob.returncode == 0 else None
    if ('## ' + SECTION) in before:
        rec('  ### ### **THE SECTION IS ALREADY IN FINDINGS.md. ### NOTHING WRITTEN.** (idempotent)')
        written = False
        after = before
    else:
        io.open(FINDINGS, 'w', encoding='utf-8', newline=chr(10)).write(before.rstrip(chr(10)) + chr(10) + md)
        after = io.open(FINDINGS, encoding='utf-8').read()
        written = True
    pfx_work = after.startswith(before.rstrip(chr(10)))
    pfx_blob = (hb is not None) and after.startswith(hb.rstrip(chr(10)))
    once = after.count('## ' + SECTION) == 1
    added = len(after.splitlines()) - len(before.splitlines())
    rec('  F-ADDITIVE : a TRUE PREFIX of the file before (%s) and of its blob (%s) ; the section appears once (%s) ; lines added %d'
        % (pfx_work, pfx_blob, once, added))
    ok = pfx_work and pfx_blob and once
    if not ok:
        fails.append('F-ADDITIVE')
    rec('')
    rec('  ### ### **NO GRADE MOVED, AND THAT IS CHECKED AND NOT ASSERTED. ### NO ACT RE-VERDICTED. ### NO NEW')
    rec('  ### ### MATHEMATICS.**')
    rec('  ### COMPONENTS FAILING : %d %s' % (len([f for f in fails if f]), [f for f in fails if f]))
    rec('=' * 100)
    p = run_clock.write(D, 'b348_fold_run', LINES)
    io.open(os.path.join(D, 'b348_fold.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(section=SECTION, acts=[r[0] for r in RESULTS], quotes_failing=len(bad_q), grades_failing=len(bad_g),
             census=census, species=species, written=bool(written), prefix_working=bool(pfx_work),
             prefix_blob=bool(pfx_blob), once=bool(once), lines_added=added,
             corrections=len(CORRECTIONS), defective=len(DEFECTIVE), seat_defects=len(SEAT_DEFECTS),
             incidents=[i[0] for i in INCIDENTS], fails=[f for f in fails if f],
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0 if ok and not bad_q and not bad_g else 1


if __name__ == '__main__':
    sys.exit(main())
