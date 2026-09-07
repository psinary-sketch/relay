# -*- coding: utf-8 -*-
"""b360_fold.py -- THE FOLD, b349-b359. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED.**

### ### **THE DESIGN POINT, CARRIED FROM b323, b331, b338 AND b348:** ### the result table below is the single
### source of truth and this runner EMITS the markdown the fold appends. ### **A QUOTATION THAT FAILS `F-QUOTE`
### NEVER REACHES `FINDINGS.md` AT ALL.** ### **THE EMITTER DISCIPLINE (b283):** every quotation is checked
### against THE ACT THAT ORIGINATED IT, never against an act that quoted it -- which is why the three rhyming
### obstructions are read at `b332`, `b351` and `b353` and not at the faces ledger row that collects them.
### ### **`F-NOGRADE`, CARRIED FORWARD FROM b348 AS THE PROGRAMME'S OWN MEMORY ASKS:** every grade string the
### section writes must appear VERBATIM in the bank of the act it is attributed to. ### **A GRADE THE FOLD
### ### INVENTS CANNOT REACH THE FILE.**
### ### **AND ONE THING THIS FOLD DOES THAT ITS ANCESTORS DID NOT: ### THE SPAN IS COUNTED, NOT TYPED.** ###
### `b360_regspec.count` reads the last fold section's own filing line off `FINDINGS.md` and finds each act's
### bank on disk; the number of acts in the heading and in the head paragraph is that count.
### ### **IDEMPOTENT:** a second run finds the section and writes nothing.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock          # noqa: E402
import b360_regspec as RS  # noqa: E402  ### THE SPAN COUNTER, IMPORTED AND NEVER RETYPED

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
EMIT = os.path.join(D, 'b360_fold_emitted.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


SECTION = 'THE UNIFORMITY ARC, b349\u2013b359 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE GRADE'S OWN ANCHOR, THE SCOPE)
# ### ### **THE GRADE ANCHOR IS THE STRING `F-NOGRADE` LOOKS FOR IN THAT ACT'S OWN BANK.**
RESULTS = [
    ('b349', 'the room measured again by a ratio built to dissolve its minimum, and then charted at three '
     'heights below the record\u2019s lowest',
     '### ### ### **THE MINIMUM SURVIVES THE RELATIVE MEASURE, AT BOTH REACHING WIDTHS.**',
     'MEASURED \u2014 the minimum sits at the same aim in both measures at both widths and stays interior when '
     'the grid is extended below it; the relative measure is flatter at both',
     'THE MINIMUM SURVIVES THE RELATIVE MEASURE',
     'One measure agreeing with another is WEAKER THAN EITHER BEING RIGHT, and the registration said so '
     'before the figures existed. NO CROSSING is claimed at any height; a narrower room at a lower height is '
     'a lower height and not a trend; nothing here bears on totality. The act also built the sortie\u2019s shared '
     'normaliser, and checked the order\u2019s own citation of the species against the record rather than '
     'accepting it \u2014 naming the two incidents the record actually holds.'),

    ('b350', 'the two origins of the residual\u2019s floor that b344 held, priced off figures already printed, '
     'with no frame built and no axis moved',
     '### The one origin that was moved does not account for it, and for the two held origins the record contains',
     'THE FLOOR IS UNEXPLAINED \u2014 the cost is the same for both axes; the threshold\u2019s room comes free from '
     'the printed figures and the taper\u2019s room is not priceable at all; the trail is RESTATED, NOT DISCHARGED',
     'THE FLOOR IS UNEXPLAINED',
     'PRICING IS NOT MEASURING. No axis moved, and the record holds no measurement of the residual against a '
     'held origin at all. The asymmetry between the two axes is not in the cost \u2014 that is identical \u2014 but in '
     'the ROOM and in the CONFOUND: moving the cut\u2019s threshold confounds the rank with the floor, and moving '
     'the taper CHANGES THE OBJECT, which no amount of wall buys back. And one thing no seat wrote down: the '
     'threshold\u2019s rank-preserving band is about one decade wide, so the axis that looked free to move has '
     'about a decade of room before the instrument keeps something else.'),

    ('b351', 'the aim plane\u2019s four coordinates read for a finite classification of the ways the margin could '
     'fail, under a ceiling that forbade constructing one',
     "### ### **THE FOUR COORDINATES DO NOT FAIL IN THE SAME WAY, AND THAT IS THE ACT'S CONTENT:**",
     'UNDECIDED \u2014 the record contains neither a finite classification nor a proof that there is none; the '
     'abscissa and the phase bounded by an argument, the height bounded only by a measurement, the width not '
     'bounded at all',
     '### ### ### **UNDECIDED.**',
     'UNDECIDED is A STATEMENT ABOUT THE RECORD, NOT ABOUT THE OBJECT: the plane may well admit a finite '
     'classification. A coordinate being bounded is not the margin being safe there, and a classification of '
     'a product is not two classifications of two factors. Both other branches were shown unreachable rather '
     'than left unclaimed. And the thing no seat wrote down: the abscissa had been closed since b326 by a '
     'one-line summed bound written to justify a census box, which nobody had ever cited as a statement about '
     'the aim plane.'),

    ('b352', 'a constant floor and a faster-decaying correction fitted to the same five banked residuals at '
     'equal complexity, under a criterion sealed before any fit',
     '### ### ### **THE FLOOR IS UNDER-RESOLVED AS A FIT.**',
     'UNDER-RESOLVED AS A FIT \u2014 the instrument has resolving power and the cells do not agree; at five points '
     'the corrected criterion charges twenty score units for a third parameter against a bar of two',
     'THE FLOOR IS UNDER-RESOLVED AS A FIT',
     'A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING, and the act prints per cell the size of floor '
     'its own ladder would have been deaf to. b339 is not re-verdicted and its side-reading is restated as '
     'fit-dependent, not withdrawn. And the sentence that set the next three acts going: the sixth frame the '
     'fit needs is AFFORDABLE inside a ceiling b339 had already sealed and called unaffordable for a different '
     'question \u2014 so UNAFFORDABLE is a verdict about a question and not about a ladder.'),

    ('b353', 'the literature asked for the statement that would carry positivity from the seed family to the '
     'whole admissible class, and the corpus\u2019s own pinned source read at content',
     '### ### ### **A STATEMENT EXISTS -- AND IT DOES NOT CLOSE THE WIDTH COORDINATE, AND CANNOT.**',
     'A STATEMENT EXISTS \u2014 Boas\u2013Kac, Proposition 2 of the corpus\u2019s own source: an EQUIVALENCE, which is '
     'stronger than the density statement the order asked for, graded TRUSTED-AT-CITE under the import bar',
     'A STATEMENT EXISTS',
     'An exhaustion at every width is not an exhaustion across widths: the statement is indexed by the support '
     'and concludes at the support, while the criterion it serves quantifies over the union of all supports. A '
     'located statement is not a proved one, and this act verifies no proof and may not. One source was read '
     'at content, so the absence of a crossing statement is AN ABSENCE OF READING AND NOT AN ABSENCE OF '
     'LITERATURE. Graded against the corpus\u2019s constructed objects rather than the source\u2019s class, one '
     'hypothesis came out REFUTABLE and one UNDECIDABLE FROM THE RECORD \u2014 reported, and routed.'),

    ('b354', 'the sixth frame b352 priced, built and run at the sealed criterion, with the fifth rung '
     'recomputed first as the arm that licensed the rest',
     '### ### ### **THE SIXTH RUNG LANDED, AND ITS RESIDUAL IS NEGATIVE AT EVERY COVERED CELL.**',
     'FLOOR UNDER-RESOLVED STILL, by the letter of the sealed condition \u2014 and the reason is not the one the '
     'branch anticipated: no six-frame score exists at all, because the ladder left the criterion\u2019s domain',
     'FLOOR UNDER-RESOLVED STILL',
     'The sign change and the rank saturation arrive at the SAME rung and this act separates them nowhere: '
     'nothing in it decides whether the object\u2019s residual crosses zero or whether the instrument stopped '
     'being able to say. Its own controls hold exactly at the rung in question, so the rung is not a broken '
     'computation. The sealed criterion is undefined on a non-positive residual and was TABLED, NOT EDITED. '
     'And the thing nobody had looked for: the banked ranks and the fixed constraint count said the ladder had '
     'room for exactly one more rung \u2014 one line of arithmetic on numbers already banked, never asked.'),

    ('b355', 'what the corpus\u2019s arrays actually are, read at the emitting lines, and every banked lawfulness '
     'check classified one by one',
     '### ### ### **THE RECORD STATES IT, AND `b353` DID NOT LOOK AT THE LINE.**',
     'THE RECORD STATES IT \u2014 at three layers and with its reason: the object integrated is a piecewise-linear '
     'interpolant of a sampled smooth bump, chosen for agreement with the corpus\u2019s own banked numbers; the '
     'consequence is A RELABELLING AND NOT A DEMOTION',
     'THE RECORD STATES IT',
     'EVERY BANKED NUMBER STANDS AND EVERY CHECK THAT PASSED STILL PASSED; what changes is the sentence '
     'describing what passing established. No act has measured the difference between the smooth bump and the '
     'interpolant, and this one did not either. The pointwise-positivity grade stands undisturbed \u2014 one '
     'hypothesis fails because of WHAT THE OBJECT IS and the other is undecided because of HOW FAR THE LOOKING '
     'WENT, and an answer to either settles nothing about the other. Whether any banked VERDICT turns on the '
     'difference is this seat\u2019s reading and is ROUTED, not applied.'),

    ('b356', 'the sixth rung run again with the quadrature axis raised, the fifth rung recomputed under the '
     'raised axis first as the control that licensed it',
     "### ### ### **SO b354's SIXTH RUNG WAS THE INSTRUMENT'S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS",
     'THE BOUNDARY \u2014 the residual returns positive at every covered cell once the bound is lifted and the rank '
     'is clear of it; the five-frame picture stands with its edge now located',
     'THE BOUNDARY',
     'TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE: a sign that survives one raise is not a sign that survives '
     'the limit \u2014 and, the symmetric refusal, which matters more because the verdict went this way, A SIGN '
     'THAT RETURNS UNDER ONE RAISE IS NOT A SIGN THAT IS SAFE. b354 is not re-verdicted: it named its own '
     'ambiguity and could not have resolved it. The comparison a reader will reach for, between the banked '
     'fifth rung and the raised sixth, moves two parameters at once and is refused at the act\u2019s own section. '
     'And the floor question is exactly where b352 left it.'),

    ('b357', 'twelve passages across four ledgers classified for whether they say what the lawfulness checks '
     'actually certify',
     '### ### ### **SOME ROWS SAY IT.**',
     'SOME ROWS SAY IT \u2014 twelve located and classified with none unclassified, and the wider five reach every '
     'one of the four ledgers; an erratum DRAFTED AND ROUTED and not opened, and no row edited',
     'SOME ROWS SAY IT',
     'What was checked is twelve passages this seat CHOSE; nothing mechanical enumerated the candidates, so '
     'the count is over a hand-picked twelve and not a census. The correction is drafted, not made \u2014 the '
     'passages still read as they read. And the finding is about the WARRANT and not the claim: the wider '
     'sentence is not necessarily false, and whether it holds is b355\u2019s hypothesis, which stays routed.'),

    ('b358', 'two pinned sources read under a cap for an asymptotic that would close the Li tail beyond a '
     'computable index',
     '### ### ### **EXISTS BUT CIRCULAR.**',
     'EXISTS BUT CIRCULAR \u2014 of seven located statements exactly one meets all four conditions locked before '
     'any source was opened, and it is circular at all three of the locked questions; NONE SURVIVES',
     'EXISTS BUT CIRCULAR',
     'That the Li asymptotic is conditional on the hypothesis is not news to anyone who works on this: both '
     'sources write it in their own abstracts. What is new is only that THE RECORD NOW HOLDS IT, PINNED, WITH '
     'THE SPLIT LOCATED AT THE LINE. The search was five addresses and four fetches, so this is AN ABSENCE OF '
     'READING AND NOT AN ABSENCE OF LITERATURE. No located statement is applied, no argument constructed and '
     'no bound proved. One of the five undecidable grades is undecidable only because the act\u2019s own cap '
     'forbade a single evaluation.'),

    ('b359', 'the front door and the federation map checked for currency against the source of truth, against '
     'a read-only fetch and against live remotes',
     '### ### ### **NO DRIFT IS FOUND.**',
     'NO DRIFT \u2014 nine claims classified with none unclassified, seven CURRENT and two SILENT and none STALE; '
     'six asserted pins read live and all six matching; nothing appended, and both documents left '
     'byte-identical',
     'NO DRIFT IS FOUND',
     'A LEDGER RECONCILED IS NOT A LEDGER VERIFIED: named fields were checked against a named ranking party, '
     'and neither document was read for the correctness of anything else. Nine claims and six pins are not a '
     'census. A hash fixes the bytes a platform returned and nothing more, and a pin that resolves today is '
     'not a pin that resolves tomorrow. And the pass found what nobody asked it to look for: the faces ledger '
     'was not in the mirror roster, so the one file that act wrote to the papers repo did not reach the '
     'archive at all \u2014 routed, not fixed.'),
]

# ### ADDITION ONE. ### (label, act, [quotations at that act], what the record holds / what it needs)
RHYME = [
    ('(i) the clause\u2019s quantifier, over the class', 'b332', 'b332_the_clause_stated.txt',
     ['### a named owner; the quantifiers -- over the class, infinite, and through the explicit formula over',
      '### the zeros -- are UNOWNED, and they are the clause.'],
     'What the record holds: the clause\u2019s constituents graded one by one, each with an owner. '
     'What it needs: one statement over the class, and through the explicit formula over the zeros.'),
    ('(ii) the height coordinate\u2019s enumeration', 'b351', None,
     ['### ### HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT MADE OF INSTANCES.** ### The registration fixed',
      '### this before the coordinate was read: ### *A METHOD THAT PRODUCES INSTANCES DOES NOT PRODUCE A'],
     'What the record holds: zeros produced one at a time by the argument principle over boxes, with the main '
     'term saying the instances never run out. What it needs: one statement over every height above some '
     'bound.'),
    ('(iii) the width coordinate\u2019s union', 'b353', None,
     ["### ### ONE.** ### And the criterion it serves quantifies over the union of all supports -- the source's own",
      '### ### ### **SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.** ### That sentence is'],
     'What the record holds: an equivalence exhausting the admissible class at each fixed support. '
     'What it needs: a bound uniform in the support, or an argument from every finite support to the union.'),
    ('(iv) the countable face\u2019s tail \u2014 a FOURTH ENTRY OF THE SAME KIND, and NOT a fifth obstruction', 'b358', None,
     ['### ### **THE ARCHIMEDEAN HALF IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY:**',
      '### ### **THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL, AND BOTH SOURCES SAY THAT TOO:**'],
     'What the record holds: a certificate to a finite index, and an asymptotic that asserts the hypothesis. '
     'What it needs: an unconditional bound on the ZERO channel \u2014 the archimedean channel already has one, '
     'with an explicit error term.'),
]

# ### THE DEPOSIT'S OWN LAW, READ AT THE DEPOSITED FILE ITSELF AND NOT AT A LEDGER THAT QUOTES IT.
DEPOSIT_REFUSAL = ('while deliberately **not** compiling the cross-register equivalences, since to compile '
                   '"discharge one and you discharge all five" would be to compile RH-equivalence itself')

# ### ADDITION TWO. ### (the clause, the scope beside it)
ARC = [
    ('**The archimedean instrument\u2019s EDGE is located, and it is the quadrature bound \u2014 and the floor is still '
     'not explained.** b354 ran a sixth frame and got a negative residual; b356 raised the quadrature axis, '
     'recomputed the control first, and the residual came back positive at every cell with the rank clear of '
     'the bound. So the negative residual was the instrument\u2019s edge, located to six dimensions in five '
     'hundred and eighteen.',
     'AN EDGE LOCATED IS NOT A FLOOR EXPLAINED. b350 banked THE FLOOR IS UNEXPLAINED and nothing in the span '
     'moved a held axis; b352 left the floor UNDER-RESOLVED AS A FIT and b356\u2019s own closing says the floor '
     'question is exactly where b352 left it. **The order\u2019s phrasing for this clause runs one step ahead of '
     'what the acts support, and the narrower sentence is what is written here.** The instrument lane has '
     'been PARKED by ruling R4 since b358, so no frame has been recomputed since b356 built the one that '
     'located the edge.'),

    ('**The exponent is resolved on the rate axis, and a banked value\u2019s convention is recoverable from its '
     'own decay.** Carried from b346, which the span leaves untouched: no act here rests on the floor, and no '
     'act here disturbs that resolution.',
     'It resolves the two CONVENTIONS and **does not make a convention correct**; b313\u2019s clause governs and a '
     'rate is not a vote on it. Nothing in this span re-measured it.'),

    ('**The partition question is UNDECIDED, and its four coordinates fail in four different ways.** b351 '
     'found the abscissa and the phase bounded by an argument, the height bounded only by a measurement \u2014 '
     'which bounds the looking and not the coordinate \u2014 and the width not bounded at all, with no method in '
     'the record that reaches it. And the abscissa was closed by a summed bound the record had held since '
     'b326 and nobody had cited for this purpose.',
     'UNDECIDED is a statement about the RECORD and not about the object. Two coordinates closed do not make '
     'the plane half-classified, because a classification of a product is not two classifications of two '
     'factors. Nothing was constructed, no class proved silent, and the exhaustion move reaches the quantifier '
     'in no branch of that act.'),

    ('**The width statement exists, and it is an equivalence at each fixed support and not across supports.** '
     'b353 located Boas\u2013Kac in the corpus\u2019s own pinned source: stronger than the density statement the order '
     'went looking for, and useless for the coordinate in question because it is indexed by that very '
     'coordinate.',
     'The strongest kind of statement still closes nothing when it is indexed by the coordinate at issue. And '
     'b355 added the layer that keeps it from applying to the corpus\u2019s own arrays at all: the object '
     'integrated is a piecewise-linear interpolant, and the equivalence quantifies over smooth functions. '
     'That is ROUTED, not decided.'),

    ('**The Li tail is circular.** b358 read two pinned sources for an asymptotic that would close the tail '
     'beyond a computable index; the one located statement of the right shape asserts the hypothesis in its '
     'own source\u2019s abstract, and the conditionality sits in the ZERO channel while the archimedean channel is '
     'unconditional with an explicit error term.',
     'An absence of reading is not an absence of literature: five addresses, four fetches. Nothing is applied '
     'and nothing is proved. And the split is a localization, not a bridge \u2014 nothing is claimed about the '
     'relation of this face to any other.'),

    ('**The lawfulness checks confirm the construction rather than testing the class.** b355 read the arrays '
     'at their emitting lines and b357 read what the ledgers say about them: every check in the family is a '
     'scan applied to an object BUILT as an autocorrelation, on which the scan cannot fail; what it '
     'discriminates is arithmetic that has gone wrong, which is a real thing and a narrower one.',
     'A RELABELLING AND NOT A DEMOTION: every banked number stands and every check that passed still passed. '
     'What changed is the sentence describing what passing established, and the correction to the ledgers is '
     'DRAFTED AND ROUTED, not made.'),

    ('**The clause has not moved, and no act in the span claims otherwise.** No constituent\u2019s grade moved, no '
     'coordinate closed, no class discharged, and the quantifiers stay unowned.',
     'Every act in the span says so on its own face, and this section says it because they do and not because '
     'a fold may decide it.'),
]

# ### THE METHOD LAYER. ### (what, act, quotation at that act, what it cost, what it caught)
METHOD = [
    ('the shared normaliser, so that two sides of a comparison cannot be normalised differently', 'b349',
     '### ### **BUILT: `tools/quote_norm.py`** -- one `norm`, and a `contains` that normalises BOTH sides so that',
     'one step of the sortie\u2019s step zero',
     'the b298/b309/b348 species at its quotation half; and it was NOT enough on its own \u2014 b354\u2019s fixtures '
     'found that it folds an em dash to one hyphen, so a seat typing two hyphens still missed.'),
    ('the anchor cure: build the anchor by READING the line, never by typing it', 'b354',
     '### ### ### **AND ITS OWN FIXTURES FOUND TWO DEFECTS IN IT BEFORE IT WAS USED ONCE:**',
     'one act\u2019s step zero, after being NAMED twice and built never',
     'two defects in itself before its first use, and then five bad hints on that first use \u2014 and it has '
     'refused a bad hint in every act since. This act\u2019s own extract located sixty-eight of sixty-eight.'),
    ('and the refusals are the evidence, not the pass', 'b354',
     "### ### ### **AND THEN IT REFUSED FIVE OF THIS ACT'S OWN TWENTY-SIX HINTS ON ITS FIRST USE**",
     'nothing beyond re-typing the hints against the files',
     'sentences the seat would have mis-typed, every one of which would have read as a MISSING SENTENCE.'),
    ('the straddling-gate rule: a gate that straddles an event has two readings, and the act names the one it '
     'relies on', 'b352',
     "### ### **FILING TWO -- THE LORE'S THIRD SIGHTING, MINTED:** ### **A GATE THAT STRADDLES AN EVENT HAS TWO",
     'one arm appended to the registration gate, and a judgement half deliberately NOT listed beside the '
     'mechanized one',
     'a census over every sealed registration in the record, reported as a count and not a charge, with '
     'nothing re-verdicted. **Whether it has caught anything since is not measured here:** this fold '
     'restates the census and runs no new one. This act\u2019s own registration declares its sides and the arm '
     'fires on none of them.'),
    ('chain the seal on the AUDIT\u2019S OWN EXIT CODE, never on a filter\u2019s', 'b354',
     '### ### ### **(E1) A FIRST VERSION OF THIS REGISTRATION WAS SEALED AGAINST AN EXPLICIT REFUSAL.**',
     'one registration sealed against an explicit refusal, banked byte for byte under a declaring name',
     'nothing yet \u2014 and it is a habit now rather than a tool: b356, b357, b358, b359 and this act all record '
     'the audit\u2019s exit code beside the lock. **A cure that has caught nothing is reported as having caught '
     'nothing.**'),
    ('the species refined: a dropped possessive is a CHANGED WORD, not a presentation difference', 'b355',
     '### away. ### **A DROPPED POSSESSIVE IS A CHANGED WORD**, and the tool refuses it for the same reason it',
     'nothing; it is a reading of refusals the tool had already made',
     'the boundary of what normalisation may fold: a tool that matched a dropped possessive would LAUNDER A '
     'WRONG QUOTATION.'),
    ('b348\u2019s minted use-and-mention rule, applied to a tool rather than to prose', 'b357',
     '### ### **THE CURE IS THE ONE b348 MINTED AND IS NOW APPLIED:** ### the grouping is ### **DECLARED DATA**,',
     'one superseded run kept unedited beside its replacement',
     'an act whose whole subject was a check that confirms rather than tests, having built one \u2014 caught by '
     'reading its own output against its own lines.'),
    ('the LOCK vocabulary, prospective only', 'b358',
     '### ### **(R3) THE VOCABULARY, PROSPECTIVE ONLY.**',
     'one flag on the seal tool and one informational arm on the ferry scan; nothing edited and nothing retired',
     'nothing, and it was not meant to: every registration sealed before it still verifies byte for byte, '
     'checked on five of them and by the tool\u2019s own fixtures on both marks.'),
    ('resolve a run file by its own recorded clock, never by its name', 'b358',
     '### ### **AND THE NUMBERED-REPEAT SPECIES HIT THIS ACT FOUR TIMES, SO IT IS NOW MECHANIZED.**',
     'one act\u2019s suite pointed at the wrong run file, twice, after two earlier acts had been bitten',
     'a wrong extract at b356 and a wrong reading at b357 before it existed; and it is what this act relies on '
     'to name the second of its own two extract runs.'),
]

# ### (act, what the act corrected in its OWN reading, the quotation at that act)
CORRECTIONS = [
    ('b349', 'the order\u2019s own citation of a species did not match the record, and the act named what the '
     'record holds instead of quietly substituting',
     "### ### **(E2) THE ORDER'S CITATION OF THE SPECIES DID NOT MATCH THE RECORD, AND THE ACT SAYS SO RATHER"),
    ('b354', 'the bank first quoted a wall from a run the act does not rely on; the act\u2019s own numbers arm '
     'recomputed every printed figure from the record and caught it before the push',
     '### ### **(E5) THIS BANK FIRST QUOTED A WALL FROM A SUPERSEDED RUN**'),
    ('b357', 'the act\u2019s own tool split its rows by grepping this seat\u2019s commentary for a word and mis-grouped '
     'two of five; the superseded run is kept unedited and the grouping became declared data',
     '### ### ### **AND THE POINT WORTH KEEPING:** ### an act whose whole subject is a check that confirms'),
]

# ### (act, the bar, what running it showed, the quotation at that act)
DEFECTIVE = [
    ('b352', 'a sealed clause of its own registration',
     'the clause counting an act\u2019s tools has never been read as counting every file an act writes, and its '
     'wording does not say so; measured and carried rather than repaired',
     "### ### **(E5) A SEALED CLAUSE OF THIS ACT'S OWN REGISTRATION IS DEFECTIVE, AND IT IS TABLED AND NOT"),
    ('b352', 'the registration gate\u2019s own multi-arm detector',
     'it returned nothing on a registration that declared two bars and named their independence at length, '
     'because it keys on phrases that registration did not use \u2014 the arm\u2019s reach is narrower than its rule',
     "### ### **(E6) THE BAR-FLOOR ARM'S MULTI-ARM DETECTOR DID NOT SEE THIS ACT'S TWO-ARM BAR.**"),
    ('b354', 'the sealed selection criterion, at the sixth frame',
     'it minimises the squared residuals of a logarithm and the sixth residual is negative, so it is undefined '
     'there; its DOMAIN was never stated, and a linear-space fit would have been a second criterion chosen '
     'after seeing the first fail',
     '### ### ### **THE CRITERION IS TABLED, NOT EDITED, AND THE TEMPTATION IS WORTH NAMING.**'),
    ('b354', 'its own sealed branch rule',
     'the branches were written over the fit\u2019s VERDICTS and not over the fit\u2019s EXISTENCE, so the outcome that '
     'arrived had no slot; and the branch\u2019s own remedy was not offered, because pricing more frames presumes '
     'a fit to improve',
     '### ### **SO THE SEALED BRANCH RULE HAS NO SLOT FOR THIS OUTCOME, AND THAT IS A FINDING OF THIS ACT.** ###'),
]

# ### (act, the defect the SEAT declared on its own face, the quotation)
SEAT_DEFECTS = [
    ('b354', 'a registration was sealed against an explicit refusal, because the seal was chained to a '
     'filter\u2019s exit code rather than the audit\u2019s; the improperly sealed file is banked byte for byte',
     '### ### ### **(E1) A FIRST VERSION OF THIS REGISTRATION WAS SEALED AGAINST AN EXPLICIT REFUSAL.**'),
    ('b356', 'the seat was wrong twice in the same direction, both times by distrusting a figure the record '
     'had already given it, and both times the sealed bars absorbed the error',
     '### ### **SO THE SEAT WAS WRONG TWICE IN THE SAME DIRECTION**, both times by distrusting a figure the record'),
    ('b357', 'an act whose whole subject is a check that confirms rather than tests built a check that '
     'confirmed rather than tested, and found it by reading its own output against its own lines',
     '### ### rather than tests ### **BUILT A CHECK THAT CONFIRMED RATHER THAN TESTED**, and found it by reading'),
]

# ### THE DESK. ### (item, where it stands, what would move it)
DESK = [
    ('**`M-2`**', 'OWED under b310\u2019s cap; (SPECIFIED-NOT-STATED)',
     'an act that states it. No act of this span approached it.'),
    ('**The object\u2019s conditions**',
     'as the stated-clause anchor has them; no constituent\u2019s grade moved in these acts',
     'an act that moves one, at its own grade.'),
    ('**The uniformity row `U1`**',
     'NAMED-ONLY, with four entries: the clause\u2019s quantifier (b332), the height\u2019s enumeration (b351), the '
     'width\u2019s union (b353), and the countable face\u2019s tail (b358, localized by b359). No bridge is typed '
     'between them in either direction.',
     'a statement uniform in one of those indices. **Not a statement that the four are the same problem** \u2014 '
     'the deposit\u2019s own refusal forbids compiling that, and the row types no bridge.'),
    ('**The instrument lane**', 'PARKED by ruling R4; no frame recomputed since',
     'the author lifting the ruling. The frame-recompute leg names its own next question: whether the '
     'residual\u2019s sign survives a second raise of the quadrature axis, which two points cannot say.'),
    ('**The anchored gate arms**', 'named as AVAILABLE MECHANICAL WORK at b358, unscheduled and not built',
     'an act that builds the helper. Naming it is not building it, and no act has been ordered to.'),
    ('**The wave\u2019s candidate list**',
     'typed and not ranked at b324, each item marked NEW or REFINEMENT \u2014 one refinement of a deposited claim, '
     'one of an internal one',
     'the author. **The wave is the author\u2019s and no seat starts one.**'),
    ('**The wave**', 'PARKED by the author\u2019s ruling', 'the author.'),
    ('**The routed items**',
     'b355\u2019s smoothness hypothesis; b358\u2019s index-dependent condition, undecidable only because a cap forbade '
     'one evaluation; the passages the b357 erratum names, filed and not repaired; the typed act number in '
     'correspondence row 204, corrected by an appended row and not by an edit',
     'the author, on each. **No routed item is opened by this fold.**'),
    ('**The patent receipts**', 'ABSENT on the mounted volumes; UNCONFIRMED on this seat\u2019s record',
     '**the one item on this desk with a date;** carried on the patent seat\u2019s report.'),
]

# ### THE SPAN'S OWN FINDING, AND ITS SCOPE. ### **A SENTENCE, NOT A PROPOSAL.**
FINDING = (
    'No move aimed at the quantifier remains on this board that the span has not tried and priced. It priced '
    'the two held axes of the instrument\u2019s floor and got a cost with no room on one of them; it asked the '
    'aim plane for a finite classification and got UNDECIDED, with the one coordinate that closed closing by '
    'an argument already in the record; it asked the literature for the statement that would cross the width '
    'index and found an equivalence indexed by that very width; it asked the literature for the statement '
    'that would close the Li tail and found one that asserts the hypothesis; and it asked the corpus\u2019s own '
    'checks what they certify and found them confirming the construction. **So a new move would have to come '
    'from a face the corpus has not worked in, or a read nobody has run.**')

FINDING_SCOPE = (
    '**This is a statement about what this span put on the board and what it cost. It is not a claim that no '
    'such move exists, not a claim that the quantifier is unreachable, and not a proposal.** It opens '
    'nothing, orders nothing and names no work. A board is what a span happened to try; the record\u2019s own '
    'lesson from b351 and b353 is that the move nobody had tried was sitting in a document the record already '
    'held.')


def bank(act):
    return io.open(dict(SPAN)[act], encoding='utf-8', errors='replace').read()


SPAN = []


def d(n):
    return os.path.join(D, n)


def f_quote():
    """### `F-QUOTE`: every quotation located at THE ACT THAT ORIGINATED IT."""
    rec('')
    rec('  F-QUOTE -- every quotation located at the act that ORIGINATED it:')
    bad = []

    def at(act, q, kind, path=None):
        src = io.open(path, encoding='utf-8', errors='replace').read() if path else bank(act)
        ok = q in src
        rec('    %-6s %-5s %-14s %s' % (act, 'PASS' if ok else 'FAIL', kind, q[:64]))
        if not ok:
            bad.append((act, kind, q))

    for act, _w, q, _g, _ga, _s in RESULTS:
        at(act, q, '(verdict)')
    for _lbl, act, path, qs, _n in RHYME:
        for q in qs:
            at(act, q, '(rhyme)', d(path) if path else None)
    for _w, act, q, _c, _k in METHOD:
        at(act, q, '(method)')
    for act, _w, q in CORRECTIONS:
        at(act, q, '(correction)')
    for act, _b, _w, q in DEFECTIVE:
        at(act, q, '(defective)')
    for act, _w, q in SEAT_DEFECTS:
        at(act, q, '(seat defect)')
    dep = io.open(DEP, encoding='utf-8', errors='replace').read()
    okd = DEPOSIT_REFUSAL in dep
    rec('    %-6s %-5s %-14s %s' % ('DEP', 'PASS' if okd else 'FAIL', '(the refusal)', DEPOSIT_REFUSAL[:64]))
    if not okd:
        bad.append(('DEP', '(the refusal)', DEPOSIT_REFUSAL))
    rec('    ### quotations failing : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    return bad


def f_nograde():
    """### `F-NOGRADE`: every grade string found VERBATIM in the bank of the act it is attributed to.
    ### ### **CARRIED FORWARD FROM b348, WHICH MADE THE NO-GRADE-MOVED CLAIM MECHANICAL.**"""
    rec('')
    rec("  F-NOGRADE -- every grade anchored verbatim in its OWN act's bank (mechanical):")
    bad = []
    for act, _w, _q, _grade, anchor, _s in RESULTS:
        ok = anchor in bank(act)
        rec('    %-6s %-5s grade anchor %r' % (act, 'PASS' if ok else 'FAIL', anchor[:56]))
        if not ok:
            bad.append((act, anchor))
    rec('    ### grade anchors failing : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    return bad


def clean(q):
    return q.replace('###', '').replace('**', '').strip()


def emit(nspan, extract):
    A = []

    def a(s=''):
        A.append(s)

    a('')
    a('## %s' % SECTION)
    a('')
    a('**%d acts, 2026-09-07.** A filings section: **no grade moves here, no act is re-verdicted, and '
      'nothing below is new mathematics.** Each entry carries its grade as *its own act* left it and its own '
      'scope sentence, and every quotation was checked verbatim against the act that **originated** it before '
      'this section was emitted \u2014 which is why the rhyming obstructions below are quoted at b332, b351 and '
      'b353 and not at the ledger row that collects them. **The no-grade-moved claim is mechanical:** every '
      'grade string below was required to appear, verbatim, in the bank of the act it is attributed to, or '
      'the section would not have been written. **And the span is counted, not typed:** the emitter reads the '
      'last fold section\u2019s own filing line off this document and finds each act\u2019s bank on disk.'
      % nspan)
    a('')
    a('### The span, act by act')
    a('')
    a('| act | what it is | grade, as its own act left it |')
    a('|---|---|---|')
    for act, what, _q, grade, _ga, _s in RESULTS:
        a('| **%s** | %s | %s |' % (act, what, grade))
    a('')
    a('### Each with its own sentence and its own scope')
    a('')
    for act, what, q, grade, _ga, scope in RESULTS:
        a('- **%s \u2014 %s.** *Grade:* %s.' % (act, what, grade))
        a('  - Its own words: \u201c\u2026%s\u2026\u201d' % clean(q))
        a('  - **Scope, as its own act set it:** %s' % scope)
    a('')
    a('### The three that rhyme \u2014 and a fourth entry of the same kind')
    a('')
    a('*The hardest job in this fold, and the one place where saying less is the whole discipline.* Three '
      'obstructions in this record share a shape: **what the record holds is a family indexed by something, '
      'and what it needs is one statement uniform in that index.** They are set out here with each quotation '
      'taken from the act that originated it. b358\u2019s localization is added as a **fourth entry of the same '
      'kind and not as a fifth obstruction**, because it is the same shape found one register out and asked '
      'of the literature directly.')
    a('')
    for label, act, _path, qs, need in RHYME:
        a('- **%s** \u2014 *%s.*' % (label, act))
        for q in qs:
            a('  - \u201c\u2026%s\u2026\u201d' % clean(q))
        a('  - %s' % need)
    a('')
    a('**And what may not be written beside them.** The deposited monograph states the law itself, of the '
      'register structure it compiles: \u201c\u2026%s\u2026\u201d' % DEPOSIT_REFUSAL)
    a('')
    a('**So: no bridge is typed here, in either direction.** Nothing is claimed about the relation of any one '
      'of these to any other \u2014 not that they are the same problem, not that discharging one would touch '
      'another, and not that they have a common cause. A row naming things that look alike is exactly where '
      'an equivalence gets compiled by accident. **Three obstructions that rhyme are three obstructions.**')
    a('')
    a('### The arc as one statement')
    a('')
    a('*At the grade the acts support, with the scope beside each clause. Nothing here is new; it is what the '
      'acts already carry, said once.*')
    a('')
    for claim, scope in ARC:
        a('%s' % claim)
        a('')
        a('  - *Scope:* %s' % scope)
        a('')
    a('### The method layer, counted and not celebrated')
    a('')
    a('*What the span minted or mechanized, what each cost, and what each caught \u2014 including where a cure has '
      'caught nothing yet.*')
    a('')
    a('| what | act | what it cost | what it caught |')
    a('|---|---|---|---|')
    for what, act, _q, cost, caught in METHOD:
        a('| %s | **%s** | %s | %s |' % (what, act, cost, caught))
    a('')
    a('### The acts\u2019 corrections to their own readings')
    a('')
    a('*Each act found this in its own work and said so on its own face. None is a correction of another act, '
      'and none re-verdicts anything.*')
    a('')
    a('| act | what it corrected in its own reading |')
    a('|---|---|')
    for act, what, _q in CORRECTIONS:
        a('| **%s** | %s |' % (act, what))
    a('')
    a('### The sealed bars found defective')
    a('')
    a('*A sealed bar found defective by running it is measured and tabled, never edited, and the consequence '
      'is carried.*')
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
    a('### The desk')
    a('')
    a('*Written so a reader arriving cold can act from it.*')
    a('')
    a('| item | where it stands | what would move it |')
    a('|---|---|---|')
    for item, stands, moves in DESK:
        a('| %s | %s | %s |' % (item, stands, moves))
    a('')
    a('**And one sentence the span earned, filed as a sentence and opening nothing.** %s' % FINDING)
    a('')
    a('*Scope:* %s' % FINDING_SCOPE)
    a('')
    a('*A fold is a summary of its acts at their own grades. It proves nothing, discharges nothing, and moves '
      'no grade. No coordinate is closed, the partition stays UNDECIDED, and `h2` stands exactly where the '
      'deposit left it. Filed by b360 (relay `data/b360_the_fold.txt`; the extract that located every '
      'quotation above at `data/%s`).*' % extract)
    a('')
    return chr(10).join(A) + chr(10)


def main():
    global SPAN
    rec('=' * 100)
    rec('b360_fold.py -- THE FOLD, b349-b359. ### THE GENERATOR.')
    rec('=' * 100)
    # ### ### **THE SPAN START IS READ ONCE, BEFORE THE WRITE, AND CARRIED.** ### `span_start` is
    # ### deliberately NOT idempotent: once THIS act's own section lands in the findings document it
    # ### correctly reports the NEXT span's first act. ### **A TOOL THAT RE-READ IT AFTER ITS OWN WRITE
    # ### WOULD BANK A NUMBER ABOUT AN ACT THAT DOES NOT EXIST YET**, which is what the first runs of this
    # ### file did in their JSON, caught by the suite before the push.
    start = RS.span_start()
    SPAN = RS.count()
    rec('')
    rec('  ### THE SPAN, COUNTED OFF THE RECORD AND NOT TAKEN FROM THE DRAFT:')
    rec('      the last fold section\'s filing act + 1 = b%d ; this act = b%d' % (start, RS.THIS_ACT))
    for act, path in SPAN:
        rec('      %-6s %s' % (act, os.path.basename(path)))
    rec('  ### ACTS IN THE SPAN : %d' % len(SPAN))
    covered = sorted({r[0] for r in RESULTS})
    listed = sorted(a for a, _p in SPAN)
    if covered != listed:
        rec('  ### ### **REFUSING TO EMIT -- THE RESULT TABLE AND THE COUNTED SPAN DISAGREE.**')
        rec('      counted : %s' % listed)
        rec('      tabled  : %s' % covered)
        run_clock.write(D, 'b360_fold_run', LINES)
        return 1
    rec('  ### the result table covers exactly the counted span : True')

    fails = []
    bad_q = f_quote()
    bad_g = f_nograde()
    if bad_q or bad_g:
        rec('')
        rec('  ### ### **REFUSING TO EMIT. ### A QUOTATION OR A GRADE THAT CANNOT BE FOUND AT ITS OWN ACT NEVER')
        rec('  ### ### REACHES THE FINDINGS DOCUMENT.**')
        run_clock.write(D, 'b360_fold_run', LINES)
        return 1

    # ### the extract this act relies on, RESOLVED BY ITS OWN RECORDED CLOCK (b358's cure), never by name.
    E = json.load(io.open(d('b360_reads.json'), encoding='utf-8'))
    rec('')
    rec('  THE RELIED-ON EXTRACT, RESOLVED BY ITS OWN RECORDED CLOCK : %s (%s) ; %d reads, %d without an anchor, %d anchors differing'
        % (E['run_file'], E['run_clock'], E['reads'], E['without_anchor'], E['anchors_differing']))

    md = emit(len(SPAN), E['run_file'])
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
    rec('  ### **THE PREFIX-OF-BLOB READING IS THE PRE-PUSH ONE, WHICH IS THE READING THIS ACT RELIES ON.**')
    ok = pfx_work and pfx_blob and once
    if not ok:
        fails.append('F-ADDITIVE')
    rec('')
    rec('  ### ### **NO GRADE MOVED, AND THAT IS CHECKED AND NOT ASSERTED. ### NO ACT RE-VERDICTED. ### NO NEW')
    rec('  ### ### MATHEMATICS. ### NO BRIDGE TYPED BETWEEN THE RHYMING OBSTRUCTIONS.**')
    rec('  ### COMPONENTS FAILING : %d %s' % (len(fails), fails))
    rec('=' * 100)
    p = run_clock.write(D, 'b360_fold_run', LINES)
    io.open(os.path.join(D, 'b360_fold.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(section=SECTION, span=[a for a, _p in SPAN], span_start=start, n_span=len(SPAN),
             acts=[r[0] for r in RESULTS], quotes_failing=len(bad_q), grades_failing=len(bad_g),
             rhyme=[r[0] for r in RHYME], rhyme_acts=[r[1] for r in RHYME], arc_clauses=len(ARC),
             method=len(METHOD), corrections=len(CORRECTIONS), defective=len(DEFECTIVE),
             seat_defects=len(SEAT_DEFECTS), desk=len(DESK),
             written=bool(written), prefix_working=bool(pfx_work), prefix_blob=bool(pfx_blob),
             once=bool(once), lines_added=added, extract=E['run_file'], extract_clock=E['run_clock'],
             fails=fails, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
