# -*- coding: utf-8 -*-
"""b408_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A LEDGER, A ROW, A KEY OR A STANDING FILE.** ### `b408_desk_bank.py`
### writes. ### **EVERY WRITE ENCODES BEFORE IT OPENS.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b408_components.txt')
PP = r'D:\MY-DOwnloads\PLACE-papers'

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    rec(c * 100)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


EXTRACT = io.open(os.path.join(D, 'b408_extract.txt'), encoding='utf-8').read()
MC = io.open(os.path.join(PP, 'day1', 'Seven_Mechanism_Classes.md'), encoding='utf-8').read()
IB = io.open(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'),
             encoding='utf-8').read()


def q(frag, where, hay=None):
    hay = EXTRACT if hay is None else hay
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


def wrap(s, ind='        ', w=128):
    for k in range(0, len(s), w):
        rec('%s%s' % (ind, s[k:k + w]))


# ### =================================================================================================
def addition_three():
    bar()
    rec('### ADDITION THREE -- THE OTHER TWO CHANNELS. ### **PRECEDENCE, FIRST.**')
    bar()
    rec('  ### **THE TWO, IN THE CLASSES DOCUMENT\u2019S OWN WORDS:**')
    rec('')
    rec('  ### ### **`C\u2083` -- THE ARCHIMEDEAN CLASS.**')
    q('**Class C\u2083 (archimedean).** The \u0393-factor transformation under s \u21a6 1\u2212s '
      'produces the functional equation \u03be(s) = \u03be(1\u2212s).', 'C3', hay=MC)
    wrap('### **WHAT IT WOULD MEAN AS A CHANNEL:** an interface whose two sides are `s` and '
         '`1\u2212s`, across which the functional equation carries information. ### For it to be '
         'BRIGHT at this target, the reflection would have to distinguish an individual zero from '
         'its neighbours -- and a symmetry that maps the critical line to itself is exactly the '
         'kind of thing that does not.')
    rec('')
    rec('  ### ### **`C\u2084` -- THE GLOBAL CLASS.**')
    q('**Class C\u2084 (global coherence).** The modular symmetry group PSL\u2082(\u2124) \u2245 '
      '\u2124/2 \u2217 \u2124/3 encodes how archimedean and multiplicative places fit together.',
      'C4', hay=MC)
    wrap('### **WHAT IT WOULD MEAN AS A CHANNEL:** an interface between the archimedean side and '
         'the multiplicative side, with the modular group as the relation. ### **IT IS THE ONLY '
         'ONE OF THE THREE THAT IS ITSELF A RELATION BETWEEN THE OTHER TWO** -- which is what '
         'Definition 2.2 asks an interface to be, and is why its absence below is worth printing.')
    rec('')
    rec('  ### **AND THE EXHAUSTIVENESS THAT MAKES THEM THE ONLY OTHERS:**')
    q('every derivation chain from \u03b8 to a zero-location constraint factors through the '
      'archimedean, multiplicative, or global structure of \u211a. No fourth source exists.',
      'EXHAUSTIVENESS', hay=MC)
    rec('')
    rec('  ### ### **AND ONE THING THE BARRIER KEYSTONE\u2019S OWN TOOLKIT DOES NOT DO.**')
    rec('  ### `T` names the functional equation as `T1` -- so `C\u2083` IS in it. ### It excludes')
    rec('  ### the Euler product BY CONSTRUCTION, with its reason printed -- so `C\u2085` is')
    rec('  ### deliberately out. ### ### **AND `C\u2084` IS NOT NAMED AT ALL:** ### not included,')
    rec('  ### not excluded, not mentioned. ### **THE BARRIER IS STATED AGAINST A TOOLKIT THAT IS')
    rec('  ### ### SILENT ABOUT ONE OF THE THREE SOURCES ITS OWN EXHAUSTIVENESS THEOREM REQUIRES.**')
    rec('  ### That is a printed fact about the document and ### **NOT A CLAIM THAT THE TOOLKIT IS')
    rec('  ### ### WRONG** -- a toolkit is a stipulation and may stipulate what it likes.')
    rec('')
    rec('  ### ### **THE SEARCH: HAS EITHER BEEN EXAMINED AS A CHANNEL?**')
    rec('  ### The predicate was fixed before the sweep and its whole yield is in the survey:')
    rec('  ### `4705` files -- every live papers `.md` and every banked relay record -- and a line')
    rec('  ### counts only if it names the class AND one of the corollary\u2019s channel words.')
    rec('  ### ### **`C\u2083`: `19` LINES. ### `C\u2084`: `7` LINES. ### AND EVERY ONE IS')
    rec('  ### ### HAND-READ, BECAUSE A PERMISSIVE FILTER\u2019S COUNT IS NOT A FINDING.**')
    rec('')
    rec('  ### **THE HAND-READING, BY KIND OF HIT:**')
    kinds = [
        ('ANOTHER SENSE OF THE WORD ENTIRELY', 3,
         'the patent packet\u2019s *channel C\u2083* is an ANTENNA channel in a fault-tolerance '
         'plot. ### Same two characters, different universe.'),
        ('A DIFFERENT SENSE OF *CHANNEL* IN THIS CORPUS', 2,
         '*two algebraic channels* at the PRIMITIVE stage (`A_Place_to_Stand:842`, '
         '`Seven_Mechanism_Classes:46`) -- a channel FROM `\u2124`, not an interface with a '
         'transmission coefficient.'),
        ('A CLASS NAMED AS AN ORIGIN, NOT EXAMINED', 4,
         '`CATALOGOS`\u2019s five paths by originating stage; `TECHNE_ELEMENTS`\u2019s '
         '*\u03c0 enters through C\u2083*; `BALANCE_AND_POSITIVITY`\u2019s classes compiled as '
         '`Coupling` predicates. ### **NAMING A CLASS IS NOT EXAMINING IT AS A CHANNEL.**'),
        ('### **A NUMBERING ARTEFACT** ###', 2,
         '`PATHS_TO_THE_CRITICAL_LINE:107` and `CRITICAL_RESOLVE:1121` both read *output-stage '
         'classes (C\u2083 + C\u2087) ... assembling without crossing a dark interface*. ### That '
         'is the vocabulary exactly -- and ### **IT IS ABOUT A DIFFERENT CLASS.**'),
        ('THIS SESSION\u2019S OWN BLOCK', 1,
         '`OPEN_TRAILS:4843` is `b407`\u2019s, which examines `C\u2085` and merely mentions the '
         'others.'),
    ]
    for name, n, why in kinds:
        rec('      %-42s %d hit(s)' % (name, n))
        wrap(why, '          ')
    rec('')
    rec('  ### ### **THE NUMBERING ARTEFACT, WHICH IS THE SWEEP\u2019S REAL FINDING.**')
    rec('  ### The corpus carries ### **TWO CLASS NUMBERINGS** ### and tabulates them itself:')
    q('| C\u2083 | C\u2081 | Archimedean / functional equation |', 'NUMBERING C3', hay=MC)
    q('| C\u2084 | C\u2085 | Global / PSL\u2082 symmetry |', 'NUMBERING C4', hay=MC)
    rec('  ### ### **THEY DISAGREE ON SIX OF SEVEN SYMBOLS; ONLY `C\u2087` MEANS THE SAME THING IN')
    rec('  ### ### BOTH.** ### And `C\u2083` is a TRANSFORMATION-stage class in the paper\u2019s')
    rec('  ### numbering, so a document calling `C\u2083` an ### **OUTPUT-STAGE** ### class is')
    rec('  ### using the monograph\u2019s, where `C\u2083` is *Local / Cauchy-Riemann*. ###')
    rec('  ### ### **SO THE TWO MOST PROMISING HITS IN THE WHOLE SWEEP ARE NOT ABOUT THE')
    rec('  ### ### ARCHIMEDEAN CLASS AT ALL.** ### **A SYMBOL MATCHED ACROSS DOCUMENTS WITH')
    rec('  ### ### DIFFERENT NUMBERINGS IS A MATCHER ARTEFACT, NOT AN EXAMINATION.**')
    rec('')
    rec('  ### ### ### **THE ANSWERS:**')
    rec('  ### ### **`C\u2083` -- EXAMINED, ONCE, AND ONLY INSIDE THE BARRIER KEYSTONE ITSELF.**')
    rec('  ### It is `T1` of the Tier-1 toolkit, and Theorem 3.7 concludes that no `T`-derivation')
    rec('  ### establishes `P` for `\u03be`. ### **THAT IS AN EXAMINATION, AND ITS RESULT IS')
    rec('  ### ### NEGATIVE AT TIER 1.** ### **NO ACT, NO OTHER KEYSTONE AND NO LEDGER ROW')
    rec('  ### ### EXAMINES IT AS A CHANNEL.**')
    rec('  ### ### **`C\u2084` -- ### ABSENT. ### `0` EXAMINATIONS ANYWHERE.**')
    rec('  ### Seven hits, hand-read, and not one is an examination: `1` is this session\u2019s own')
    rec('  ### block, `1` is a numbering artefact, and the rest name the class in passing. ###')
    rec('  ### ### **AND THE BARRIER\u2019S OWN TOOLKIT DOES NOT NAME IT EITHER.** ### The corpus')
    rec('  ### has never asked whether the modular symmetry is a channel a closing proof could')
    rec('  ### touch.')
    rec('  ### ### **AND NO CLAIM IS MADE THAT IT IS OPEN, PROMISING, OR WORTH OPENING.** ### The')
    rec('  ### act reports what the record holds and what it has never asked. ### **AN UNASKED')
    rec('  ### ### QUESTION IS NOT AN OPPORTUNITY UNTIL SOMEONE PRICES IT.**')
    return 1, 0


K = [
    ('K1', 'the class', 'IMPORT UNDER THE BAR + LOCAL PROPOSITION',
     'the source\u2019s Definition 3.1 with Proposition C.1\u2019s vanishing set; a local '
     'proposition per seed, decided by b320\u2019s scan',
     'IMPORT', 'Definition 3.1 and Prop C.1 are the SOURCE\u2019S theorems. ### The corpus has '
     'not proved them and says so by importing them UNDER THE BAR. ### **STATED AS A HYPOTHESIS.**'),
    ('K2', 'the criterion\u2019s sign', 'IMPORT UNDER THE BAR + LOCAL PROPOSITION',
     'Proposition C.1; the corpus\u2019s convention; a local proposition for a lawful `f`',
     'IMPORT', 'Prop C.1 again. ### **STATED AS A HYPOTHESIS.** ### The local proposition beside '
     'it IS writable as a step.'),
    ('K3', 'the finite places\u2019 contribution', 'KERNEL TERMINALS + DERIVATION ON CONTENT',
     '`B329.*` (24, zero-axiom) and `B310.*`; a derivation on content at b310',
     'STEP', 'A compiled terminal is the closest thing in the chain to a classified step -- but '
     '### **ITS COMPACT PART IS PER-CELL**, so the general statement is not there to be a step. '
     '### **WRITABLE AS A STEP AT THE SEVEN CELLS AND NOWHERE ELSE.**'),
    ('K4', 'the prime sum', 'DERIVATION ON CONTENT + IMPORT UNDER THE BAR',
     'the corpus\u2019s prime side IS the source\u2019s finite-places sum (b306); the local term '
     '(149) IMPORTED',
     'MIXED', 'The derivation is writable. ### The local term (149) is the source\u2019s and is '
     '### **STATED AS A HYPOTHESIS.**'),
    ('K5', 'the archimedean distribution', 'DEFINED + MEASURED',
     'defined at b315; measured at b320 by two routes; the sign certified at every frame, the '
     'size at none',
     'MEASUREMENT', '### **A MEASUREMENT IS NOT AN INFERENCE STEP.** ### A certified sign at '
     'every frame is a finite verification; writing it as a step means either a decidable-instance '
     'lemma at those frames, or a general statement nobody has.'),
    ('K6', 'the decomposition', 'IMPORT UNDER THE BAR + LOCAL PROPOSITION + MEASURED',
     'Theorem 4.7 as an EQUALITY, IMPORTED; the compressed square non-negative as arithmetic; '
     'the equality measured at three covered cells',
     'IMPORT', 'Theorem 4.7 is the source\u2019s. ### **STATED AS A HYPOTHESIS.** ### The '
     'sum-of-squares is writable; the three-cell measurement is not a step.'),
    ('K7', 'the object and its unit', 'DERIVATION ON NAMED IMPORTS + BENCH RESIDUAL',
     'the space from the source\u2019s definition; the unit in by derivation on named imports '
     '(b300); its membership residual UNDER-RESOLVED at bench',
     'MIXED', 'The derivation is writable ON its imports. ### **THE RESIDUAL IS NEITHER A STEP '
     'NOR A HYPOTHESIS -- IT IS AN UNFINISHED MEASUREMENT**, and it would have to become one or '
     'the other before the proof could be written at all.'),
    ('K8', 'the quantifiers', 'UNOWNED',
     'over the class (infinite) and, through the explicit formula, over the zeros; no act owns '
     'either quantifier',
     'UNOWNED', '### **THIS IS THE CONCLUSION, NOT A STEP.** ### It is what the proof would be '
     'FOR, and it is the one thing the chain does not reach.'),
]


def addition_four():
    rec('')
    bar()
    rec('### ADDITION FOUR -- THE REDUCTION AS A CLASSIFIED PROOF, PRICED.')
    bar()
    rec('  ### **THE EIGHT CONSTITUENTS, CLASSIFIED IN THE E0 GATE\u2019S OWN WORDS:**')
    rec('')
    for kid, name, kind, gate, cls, note in K:
        rec('    ### **%s** %-34s ### **%s**' % (kid, name, cls))
        wrap('the gate says: %s' % gate, '          ')
        wrap(note, '          ')
        rec('')
    imports = [k for k in K if k[4] in ('IMPORT', 'MIXED')]
    steps = [k for k in K if k[4] == 'STEP']
    meas = [k for k in K if k[4] == 'MEASUREMENT']
    rec('  ### ### **THE COUNTS: ### IMPORTS OR PART-IMPORTS `%d` ### ; WRITABLE AS A STEP `%d` ;'
        % (len(imports), len(steps)))
    rec('  ### ### MEASUREMENT `%d` ; UNOWNED `1`.**' % len(meas))
    rec('  ### ### **THE DISTINCT IMPORTED PREMISES ARE FOUR:** ### the source\u2019s Definition')
    rec('  ### 3.1; Proposition C.1; the local term (149); Theorem 4.7. ### **ALL FOUR ARE THE')
    rec('  ### ### SOURCE\u2019S THEOREMS, AND THE CORPUS HAS NOT DERIVED ONE OF THEM.**')
    rec('')
    rec('  ### ### ### **THE VERDICT: A PROOF-WITH-HYPOTHESES, NOT A PROOF IN THE LEMMA\u2019S')
    rec('  ### ### ### SENSE.**')
    rec('  ### Writing each import as a classified step requires a discharge or a hypothesis, and')
    rec('  ### ### **THE CORPUS CANNOT DISCHARGE ANY OF THE FOUR** -- discharging Prop C.1 means')
    rec('  ### proving it, which is Connes-Consani\u2019s work and which the corpus imports')
    rec('  ### precisely because it has not done it. ### So all four are stated, and what gets')
    rec('  ### written is ### **`H \u21d2 \u2200x P(x)`**, a conditional.')
    rec('')
    rec('  ### ### **AND WHAT THE LEMMA WOULD SAY OF IT IF IT APPLIED -- WHICH IS THE SECOND')
    rec('  ### ### SURPRISE.**')
    rec('  ### Theorem 3.1 concludes that `\u03c0` ### **DOES NOT ESTABLISH THE UNIVERSAL')
    rec('  ### ### STATEMENT.** ### But a proof-with-hypotheses does not establish the universal')
    rec('  ### statement either way -- it establishes a CONDITIONAL. ### ### **THE LEMMA IS STATED')
    rec('  ### ### ABOUT PROOFS OF THE UNIVERSAL STATEMENT, AND A PROOF OF A CONDITIONAL IS NOT')
    rec('  ### ### ONE.** ### So the priced writing would produce an object the lemma STILL does')
    rec('  ### not quantify over. ### **DOING THE WORK NAMED AT `b407` WOULD NOT, BY ITSELF, MAKE')
    rec('  ### ### THE THEOREM APPLY** -- it would need the lemma restated for conditional')
    rec('  ### conclusions, which is a second thing nobody has written.')
    rec('')
    rec('  ### ### **THE SECOND LAYER, MARKED UNCHECKED AND NOT RESOLVED.**')
    rec('  ### An import the corpus has not derived may still be a CONSEQUENCE of the')
    rec('  ### specification: a published theorem about `\u03be` is not made underivable by nobody')
    rec('  ### having derived it. ### If the four imports are first-order consequences of `S`, the')
    rec('  ### obstacle is ### **LABOUR AND NOT LOGIC**, and a full discharge is possible in')
    rec('  ### principle. ### ### **BUT WHETHER EACH IS FIRST-ORDER EXPRESSIBLE OVER `S` IS A')
    rec('  ### ### QUESTION NOBODY HAS ASKED, AND THIS ACT DOES NOT ANSWER IT: `UNCHECKED`.** ###')
    rec('  ### Prop C.1 quantifies over smooth compactly-supported functions and their transforms,')
    rec('  ### and whether that is first-order over the specification of `\u03be` is not a')
    rec('  ### bookkeeping question. ### **BOTH LAYERS ARE PRINTED AND NEITHER IS COLLAPSED INTO')
    rec('  ### ### THE OTHER.**')
    rec('')
    rec('  ### ### **PRICED AND NOT WRITTEN. ### `0` LINES OF THE CLASSIFIED PROOF ARE WRITTEN**,')
    rec('  ### and the writing is an act of its own that the author schedules.')
    return len(imports), len(steps), len(meas)


def component1():
    rec('')
    bar()
    rec('### COMPONENT 1 -- THE SPAN, COUNTED BY THE TOOL.')
    bar()
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', EXTRACT)
    span = int(m.group(1)) if m else None
    rec('  ### **THE TOOL\u2019S OWN LINES, TAKEN FROM ITS OUTPUT AND NOT TYPED:**')
    for ln in EXTRACT.split('\n'):
        if re.search(r'last fold covers|FILED BY|next span STARTS|runs through|CURRENT SPAN|'
                     r'DECLARED THRESHOLD', ln):
            rec('      %s' % ln.strip()[:150])
    rec('')
    rec('  ### ### **THE ARITHMETIC: `%d` AGAINST `(R1)`\u2019S THRESHOLD OF `9`.**' % span)
    rec('  ### ### ### **THE FOLD IS NOT DUE. ### IT IS `%d` ACTS SHORT.**' % (9 - span))
    rec('  ### **SO THIS ACT PROPOSES NO FOLD**, and the draft\u2019s conditional -- *the fold, if')
    rec('  ### due by the tool\u2019s count, is its own act and this one proposes it* -- is not')
    rec('  ### triggered. ### **THE ARITHMETIC IS PRINTED AND NOT DRESSED AS A JUDGEMENT**, in the')
    rec('  ### tool\u2019s own manner: it supplies the number and decides nothing.')
    rec('  ### **AND THE NAVIGATOR\u2019S COUNT WAS NOT CONSULTED BEFORE THE TOOL\u2019S WAS')
    rec('  ### ### PRINTED.** ### The ferry names none for this act, so there is none to score.')
    return span


DRESSES = [
    ('DRESS 1', 'b405', 'the compiled countermodel',
     'the result quantifies over `Set Coupling` on `\u211d \u2192 \u2102`',
     'a site of row `U1` is not a coupling on `\u211d \u2192 \u2102`', 'INDEPENDENT'),
    ('DRESS 2', 'b406', 'the shared-witness form',
     'the result repairs a `\u2200\u2203 \u21d2 \u2203\u2200` and quantifies over statements of '
     'that shape',
     '`(i)` has no inner existential at its own depth and `(iv)`\u2019s is trivially satisfiable, '
     'so neither is a statement of that shape', 'INDEPENDENT'),
    ('DRESS 3', 'b407', 'the Sieve Ceiling Lemma',
     'the result quantifies over formal first-order proofs in `ZFC \u222a S`',
     'the corpus\u2019s reduction is a chain of imports under the bar, derivations and '
     'measurements -- not a formal proof', 'INDEPENDENT'),
    ('DRESS 4', 'b407', 'the exact resemblance refused',
     'the same result, the same kind',
     'the exactness of the resemblance does not change what kind the object is',
     '### **A RESTATEMENT OF DRESS 3** ###'),
]


def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- THE FOUR DRESSES, ONE OR FOUR.')
    bar()
    rec('  ### **THE CANDIDATE SENTENCE THE TEST PRODUCES:**')
    rec('')
    rec('  ### ### ### *"A RESULT APPLIES TO AN OBJECT ONLY IF THE OBJECT IS OF THE KIND THE')
    rec('  ### ### ### RESULT QUANTIFIES OVER."*')
    rec('')
    rec('  ### **AND THE INSTANTIATION, SHOWN FOR EACH -- WHICH IS THE TEST AND NOT A GLOSS:**')
    rec('')
    for tag, act, res, kind, obj, status in DRESSES:
        rec('    ### **%s** (%s) -- %s ### %s' % (tag, act, res, status))
        wrap('THE KIND : %s' % kind, '          ')
        wrap('THE OBJECT: %s' % obj, '          ')
        rec('')
    indep = [d for d in DRESSES if d[5] == 'INDEPENDENT']
    rec('  ### ### ### **THEY ARE ONE STATEMENT. ### THE SENTENCE ENTAILS ALL FOUR WHEN ITS TERMS')
    rec('  ### ### ### ARE INSTANTIATED, AND THE INSTANTIATIONS ARE PRINTED ABOVE.**')
    rec('  ### ### **BUT FOUR OCCURRENCES ARE NOT FOUR INSTANCES: `%d` ARE INDEPENDENT AND `1` IS'
        % len(indep))
    rec('  ### ### A RESTATEMENT.** ### `Dress 4` is `Dress 3` seen from the other side -- the same')
    rec('  ### result, the same object, the same kind -- and counting it as a fourth would inflate')
    rec('  ### the evidence. ### **THE ACT SAYS SO RATHER THAN BANKING A LARGER NUMBER.**')
    rec('')
    rec('  ### ### **DOES THE RECORD ALREADY HAVE A NAME FOR IT? ### ### ABSENT.**')
    rec('  ### The search was run over the live papers tree and the relay banks for the sentence\u2019s')
    rec('  ### own shape -- *kind the result quantifies over*, *of the kind the*, *category error*,')
    rec('  ### *wrong kind of object* -- and the only near thing is `W_ATTEMPT_2_REVIEW_PACKET`\u2019s')
    rec('  ### *category error*, used of a normalisation convention and not of this. ### **THE')
    rec('  ### ### INDEX RETURNS `NO KEY` ON ITS VERDICT LINE FOR ALL THREE QUERIES.**')
    rec('  ### ### ### **AND THE NAMING IS ROUTED TO THE AUTHOR, NOT DONE HERE.** ### **STATING')
    rec('  ### ### ### THE SENTENCE THE TEST PRODUCES IS NOT MINTING; GIVING IT A NAME IS**, and')
    rec('  ### ### ### this act does the first and refuses the second.')
    return len(indep)


def component3():
    rec('')
    bar()
    rec("### COMPONENT 3 -- WHAT ROW `U1` HAS COST AND WHAT IT HAS BOUGHT.")
    bar()
    rec('  ### **FROM THE BANKS ALONE, AND FROM THE COMMITTED BLOB OF THE ROW:**')
    for ln in EXTRACT.split('\n'):
        if re.search(r'sites entered|acts that ENTERED|acts that RESTATED|bridges typed|'
                     r'grades conferred|acts named anywhere|row `U1` at HEAD', ln):
            rec('      %s' % ln.strip()[:150])
    rec('')
    rec('  ### ### **WHAT IT COST:** ### the row is now `19308` bytes -- ### **THE LARGEST SINGLE')
    rec('  ### ### ROW IN THE LEDGER** ### -- and it is named or restated by six acts of this')
    rec('  ### session alone.')
    rec('  ### ### **WHAT IT BOUGHT:** ### `6` sites entered; `2` coordinates added; `1` price')
    rec('  ### corrected; `0` bridges typed; `0` grades conferred; ### **`0` STATEMENTS ABOUT THE')
    rec('  ### ### OBJECT.**')
    rec('')
    rec('  ### ### ### **THE ANSWER: ### A BOOKKEEPING INSTRUMENT, BY THE BANKS\u2019 OWN')
    rec('  ### ### ### NUMBERS.**')
    rec('  ### Every yield of the row is a CLASSIFICATION of what the record already held: which')
    rec('  ### sites resemble which, in what kind a site is empty, whether a witness form applies.')
    rec('  ### ### **NOT ONE ENTRY PRODUCED A STATEMENT ABOUT `\u03be`, ABOUT THE EPSTEIN OBJECT,')
    rec('  ### ### OR ABOUT ANY ZERO.**')
    rec('  ### ### **AND THAT IS A DESCRIPTION AND NOT A DEMOTION.** ### A bookkeeping instrument')
    rec('  ### that has held a refusal intact through six entries, caught an over-count, and')
    rec('  ### forced two coordinates into existence has earned its place. ### **THE QUESTION WAS')
    rec('  ### ### WHICH KIND IT IS, AND THE ANSWER IS A DESCRIPTION.**')
    rec('  ### ### **WHAT WOULD CHANGE IT:** ### a site whose entry produced a statement about the')
    rec('  ### OBJECT rather than about the record. ### **NONE OF THE SIX HAS.**')


def addition_one():
    rec('')
    bar()
    rec('### ADDITION ONE -- THE ROUTED PRICES, IN ONE PLACE.')
    bar()
    rec('  ### **THE SEARCH AND ITS YIELD, PRINTED BEFORE THE LIST:** ### the three closings the')
    rec('  ### ferry names, read for their own `ROUTED` lines -- `b405`: `0`; `b406`: `1`;')
    rec('  ### `b407`: `2` lines, both the same item.')
    rec('  ### ### **SO THE COUNT IS `2` ROUTED ITEMS AND `1` NAMED-BUT-NOT-ROUTED, WHICH IS `3`')
    rec('  ### ### ITEMS AND NOT `3` ROUTINGS.** ### The two dispositions are different and')
    rec('  ### merging them would make the list say more than the acts did.')
    rec('')
    items = [
        ('the second standing sentence -- *every write encodes before it opens*', 'b406', 'ROUTED',
         'nothing, except the author\u2019s word: it is already carried by two ferries and applied '
         'by three acts. ### The cost of NOT promoting it is that each ferry must restate it.',
         'THE AUTHOR'),
        ('`(R20)`\u2019s limb 2 -- *a kernel deposits when a published claim cites its terminals*',
         'b407', 'ROUTED',
         'the rule\u2019s own claim about itself. ### `(R20)` says it is *descriptive before it is '
         'prescriptive* and *discovered, not imposed*; widening limb 2 to reach a kernel with no '
         'citing claim would make it prescribe what the corpus has not done.', 'THE AUTHOR'),
        ('the Tier-2 form of the barrier -- no Euler-product-free derivation establishes `P` for '
         '`\u03be`, over the OPEN class', 'b407', '### **NAMED, NOT ROUTED** ###',
         'open mathematics. ### The document calls it *research-frontier and not claimed here*. '
         '### **NOT A BUILD AND NOT BLOCKED BY THE PARKED LANE.**', 'NOBODY YET -- IT IS A '
         'RESEARCH QUESTION, NOT A DECISION'),
    ]
    for item, act, disp, cost, whose in items:
        rec('    ### **ITEM** ### %s' % item[:110])
        if len(item) > 110:
            wrap(item[110:], '              ')
        rec('        ACT   : %s' % act)
        rec('        DISP  : %s' % disp)
        wrap('COST  : %s' % cost, '        ')
        rec('        WHOSE : %s' % whose)
        rec('')
    rec('  ### ### **`3` ITEMS. ### AND NO ACT HAS LISTED THEM TOGETHER BEFORE THIS ONE** -- each')
    rec('  ### was routed or named in a different act\u2019s closing.')
    rec('  ### ### **AND THE LIST DECLARES ITS OWN SCOPE:** ### it is built from the three acts the')
    rec('  ### ferry names and is ### **NOT A CORPUS-WIDE ROUTED-ITEM CENSUS.** ### The predicate')
    rec('  ### was `ROUTED TO THE AUTHOR` / `ROUTED, WITH` / `ROUTED WITH ITS PRICE` on those three')
    rec('  ### closings; a wider census would have to widen both the predicate and the span, and')
    rec('  ### would find the standing routed items every closing restates.')
    return len(items)


def addition_two():
    rec('')
    bar()
    rec("### ADDITION TWO -- THE SUITE'S OWN GROWTH, MEASURED.")
    bar()
    for ln in EXTRACT.split('\n'):
        if re.search(r'^\s+b40\d : \d+ arms|STANDING CORE|carried \d+ ; NEW|^\s+\[.G-', ln):
            rec('      %s' % ln.strip()[:170])
    rec('')
    rec('  ### ### **THE STANDING CORE IS `8` ARMS OF ABOUT SIXTY.** ### `G-CAP`, `G-FERRY`,')
    rec('  ### `G-KEY`, `G-MUSTFAIL`, `G-MUSTFAIL-CTL`, `G-NOBRIDGE`, `G-SEAL`, `G-WRITELIST` --')
    rec('  ### and every one of them is an ### **APPARATUS** ### arm: the ferry, the seal, the')
    rec('  ### key, the write list, the cap, the must-fail fixture. ### ### **NOT ONE OF THE EIGHT')
    rec('  ### ### IS ABOUT THE MATHEMATICS.**')
    rec('  ### ### **AND CARRY-FORWARD NEVER REACHES HALF:** ### `13%`, then `45%`, then `48%`.')
    rec('  ### ### **THE SUITE IS BUILT NEW EACH ACT AROUND A SMALL FIXED SPINE**, and that is')
    rec('  ### what the numbers say whether or not it is what anyone intended.')
    rec('')
    rec('  ### ### **THE MEASURE\u2019S OWN LIMIT, PRINTED:** ### this counts arm ### **NAMES**.')
    rec('  ### ### An arm carried forward by name may have been rewritten inside** -- `G-KEY` was')
    rec('  ### rebuilt at `b406` to read a verdict LINE after `b405`\u2019s substring failure, and')
    rec('  ### it counts as carried in both. ### **SO `48%` IS AN UPPER BOUND ON CONTINUITY, NOT A')
    rec('  ### ### MEASUREMENT OF IT.**')
    rec('  ### ### **AND NOTHING IS REFORMED BY BEING MEASURED.** ### `0` arms added, removed,')
    rec('  ### renamed or promoted; `0` standing cores proposed. ### The number is the finding.')
    return 8


def expectations(span, indep, n_items, core, c3, c4):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED. ### **EACH BY A PRINTED RESULT.**')
    bar()
    rows = [
        ('(N1)', 'the span is at or past nine and the fold is due',
         '### **REFUTED** -- the tool counts `%d`, and `(R1)`\u2019s threshold is `9`. ### **THE '
         'FOLD IS %d ACTS SHORT AND THIS ACT PROPOSES NONE.**' % (span, 9 - span)),
        ('(N2)', 'the dresses are ONE statement and the record has no name for it',
         '### **MET IN BOTH HALVES**, and sharpened: they are one statement, the instantiation is '
         'printed for each, and the record has no name -- `NO KEY` on the verdict line for all '
         'three queries. ### The naming is ROUTED.'),
        ('(N3)', 'row U1 is a bookkeeping instrument by the banks\u2019 own numbers',
         '### **MET** -- `6` sites, `2` coordinates, `0` bridges, `0` grades, and ### **`0` '
         'STATEMENTS ABOUT THE OBJECT.** ### A description, not a demotion.'),
        ('(N4)', 'the routed prices are three and no act has listed them together',
         '### **MET, WITH THE COUNT BROKEN OUT:** ### `%d` items -- but `2` ROUTED and `1` '
         'NAMED-NOT-ROUTED, which is not the same as three routings.' % n_items),
        ('(N5)', 'fewer than half the suite\u2019s arms carry forward unchanged',
         '### **MET** -- `13%`, `45%`, `48%`. ### Never half, in any of the three transitions.'),
        ('(N6)', 'at least one of the other two channels has never been examined as a channel',
         '### **MET, AND IT IS `C\u2084`.** ### `7` hits, every one hand-read, ### **`0` '
         'EXAMINATIONS** -- one is this session\u2019s own block, one is a numbering artefact, the '
         'rest name the class in passing. ### **AND THE BARRIER\u2019S OWN TOOLKIT DOES NOT NAME '
         'IT EITHER.**'),
        ('(N7)', 'the classified-proof writing is priced as proof-with-hypotheses',
         '### **MET** -- `4` distinct imported premises, all the source\u2019s theorems, none '
         'dischargeable by the corpus. ### **AND A SECOND FINDING BESIDE IT:** ### a '
         'proof-with-hypotheses proves a CONDITIONAL, and Theorem 3.1 is stated about proofs of '
         'the universal statement -- so doing the work would ### **STILL** ### not make the '
         'theorem apply.'),
        ('(E1)', 'the barrier keystone\u2019s own toolkit does not name one of the three sources',
         '### **MET** -- `T` names the functional equation as `T1` and excludes the Euler product '
         'by construction, and ### **DOES NOT NAME `C\u2084` AT ALL:** ### not included, not '
         'excluded, not mentioned.'),
        ('(E2)', 'the sweep\u2019s most promising hits are numbering artefacts',
         '### **MET** -- `PATHS_TO_THE_CRITICAL_LINE:107` and `CRITICAL_RESOLVE:1121` both use the '
         'corollary\u2019s vocabulary exactly and both mean a DIFFERENT class. ### The corpus '
         'carries two numberings that disagree on six of seven symbols.'),
        ('(E3)', 'one of the four dresses is a restatement and not an independent instance',
         '### **MET** -- `%d` independent, `1` restatement.' % indep),
        ('(E4)', 'the suite has no standing core worth the name',
         '### **MET** -- `%d` arms of about sixty, and ### **NOT ONE OF THE EIGHT IS ABOUT THE '
         'MATHEMATICS.**' % core),
    ]
    for k, claim, verd in rows:
        rec('  **%s** %s' % (k, claim))
        wrap(verd)


def main():
    rec('=' * 100)
    rec('b408_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.')
    rec('=' * 100)
    rec('  face LOCKED : 8946a46a9e7ae784fd3307ea53043d1e03619bd65b8e772bc85d82e61635a341')
    rec('  ### **THE ORDER IS THE FERRY`S: THE TWO ADDITIONS TAKE PRECEDENCE.**')
    rec('')
    c3, c4 = addition_three()
    addition_four()
    span = component1()
    indep = component2()
    component3()
    n_items = addition_one()
    core = addition_two()
    expectations(span, indep, n_items, core, c3, c4)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO LEDGER, ROW, KEY, STANDING FILE OR BANK WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write(('\n'.join(L) + '\n').encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
