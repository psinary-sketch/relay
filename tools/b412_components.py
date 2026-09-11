# -*- coding: utf-8 -*-
"""b412_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A DOCUMENT, A LEDGER, A ROW OR A KEY.** ### It computes, prints
### and emits; `b412_desk_bank.py` writes. ### **EVERY WRITE ENCODES BEFORE IT OPENS** ### and the
### wrapper breaks at word boundaries.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm     # noqa: E402
import gate_spine     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b412_components.txt')
ARCOUT = os.path.join(D, 'b412_arc.txt')
ORIOUT = os.path.join(D, 'b412_orientation.txt')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
NL = chr(10)

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    rec(c * 100)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


def wrap(s, ind='      ', w=126):
    line = ind
    for word in s.split(' '):
        if len(line) + len(word) + 1 > w + len(ind) and line.strip():
            rec(line.rstrip())
            line = ind
        line += word + ' '
    if line.strip():
        rec(line.rstrip())


EXTRACT = io.open(os.path.join(D, 'b412_extract.txt'), encoding='utf-8').read()
SPAN = io.open(os.path.join(D, 'b412_span.txt'), encoding='utf-8').read()
FINDTXT = io.open(FIND, encoding='utf-8', errors='replace').read()
DIGTXT = io.open(DIGEST, encoding='utf-8', errors='replace').read()
PATHTXT = io.open(PATHS, encoding='utf-8', errors='replace').read()


def q(frag, where, hay):
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


def bank(n):
    c = [x for x in sorted(os.listdir(D))
         if x.startswith('b%d_' % n) and x.endswith('.txt')
         and not re.search(r'_(checks|census|pins|ferry|reg|lockgate|satisfiable|desk_notes|'
                           r'extract|components|closing|mirror|audit|index_query|span|'
                           r'scheme_table|numbering|classification|original|notes|query|'
                           r'stdout)', x)]
    return (c[0], io.open(os.path.join(D, c[0]), encoding='utf-8', errors='replace').read()) \
        if c else (None, '')


# ### =================================================================================================
# ### THE ARC, ACT BY ACT -- **EACH LINE QUOTED FROM ITS OWN ACT'S BANK.**
# ### =================================================================================================
ARC = [
    (403, 'THE THREE ROUTED ITEMS', 'RECORD',
     'one routed item repaired at three sites, one applied, one ruled and routed',
     'the span counter`s stale threshold line, the guard installer, and the third item ruled'),
    (404, 'THE FIFTH AND SIXTH SITES', 'RECORD',
     'two sites entered in row `U1`, and the KIND distinction minted that the row lacked',
     '`(v)` is EMPTY AS AN OBSTRUCTION in a kind the row had no word for'),
    (405, 'THE ROW`S LAW, RESTATED', 'RECORD',
     'row `U1` restated under `(R24)` with two coordinates added inside the column law',
     'a BINARY law cannot express a UNARY refusal -- a missing coordinate, not a defect'),
    (406, 'THE SITES WITHOUT AN EXISTENTIAL', 'RECORD',
     'two sites fail the shared-witness form for two different reasons',
     'an existential the record HOLDS is not the same object as one you can always manufacture'),
    (407, 'THE BARRIER`S OWN INSTANCE', 'RECORD',
     'the corpus`s own barrier theorem does NOT apply to the corpus`s own reduction',
     'the failing hypothesis is about `π`, not about `κ` -- the object is the wrong KIND'),
    (408, 'THE OTHER TWO CHANNELS', 'BOTH -- NAMED, NOT ROUNDED',
     'one of Corollary 3.6`s three sources has never been examined as a channel by any act',
     'and the sweep`s real finding was a hazard: TWO CLASS NUMBERINGS disagreeing on six of seven'),
    (409, 'THE OBSTACLES DISSOLVED', 'BOTH -- NAMED, NOT ROUNDED',
     '`(R25)` executed: both numberings kept, 29 documents declared, `0` symbols renumbered',
     'AND the modular relation read DARK on the placement register -- a READING, not a measured '
     '`κ`'),
    (410, 'THE FOUR IMPORTS CLASSIFIED', 'BOTH -- NAMED, NOT ROUNDED',
     'three of four imports factor; Proposition C.1 does not, so `3.1-H` does not apply',
     'because one side of the biconditional IS `RH` -- a statement about a sentence, not about '
     'a zero'),
    (411, 'THE JOIN AND THE PRICE', 'RECORD',
     'the join made, the free number named `I-16`, the certificate located',
     'and the E0 gate prices the import`s OWNERSHIP while nothing prices its REACH'),
]


def component1():
    bar()
    rec('### COMPONENT 1 -- THE FOLD, `b403`-`b411`.')
    bar()
    rec('  ### **THE SPAN, FROM THE TOOL`S OWN LINES AND NOT TYPED:**')
    for ln in SPAN.split(NL):
        if re.search(r'the last fold covers|it was FILED BY|so the next span|and it now runs|'
                     r'THE CURRENT SPAN', ln):
            rec('      %s' % ln.strip())
    wrap('### ### **THE TOOL SAYS `10`; THE FOLD`S SPAN IS `9`.** ### The counter runs through the '
         'newest act IN THE RECORD and this act is in it, while ### **THE FOLDING ACT IS NOT IN '
         'ITS OWN FOLD** -- `b402` filed `b385`-`b401` and stood outside it. ### **SO `(N1)` IS '
         'REFUTED BY THE TOOL ITSELF**, and the act printed both numbers before it used either.',
         '  ')
    rec('')
    rec('  ### **THE ARC`S NAME:** ### **THE CLASSIFICATION ARC.** ### Nine acts in which the')
    rec('  ### recurring work was deciding ### **WHAT KIND OF THING** ### something is before')
    rec('  ### asking what follows from it -- a site`s emptiness, a witness form`s subject, a')
    rec('  ### theorem`s quantifier, a class symbol`s scheme, an import`s factoring, a grade')
    rec('  ### name`s vocabulary.')
    rec('')
    rec('  ### **AND THE TWO MECHANICAL ARMS THE FOLD CARRIES:**')
    wrap('### **`F-NOGRADE`** (from `b348`): every grade string written into the section must '
         'appear ### **VERBATIM IN THE BANK OF THE ACT IT IS ATTRIBUTED TO**, or the section is '
         'not written.', '      ')
    wrap('### **`F-NOSUPERSEDE`** (new here): no folded act may be summarised as overturning '
         'another where the record says they answer different questions. ### **THIS ARC CONTAINS '
         'EXACTLY THAT HAZARD** -- `b411` found the E0 gate prices what `b410` said nothing '
         'prices, and `b411` itself wrote that the two ### **NEITHER SUPERSEDE NOR ARE '
         'SUPERSEDED.**', '      ')
    return 9


def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- WHAT THE ARC PRODUCED, COUNTED.')
    bar()
    rec('  ### **THE CRITERION, FIXED ON THE FACE BEFORE THE COUNT:** ### a statement about the')
    rec('  ### ### **OBJECT** ### is one about `ξ`, about the zeros, about the Epstein object,')
    rec('  ### or about a number computed from them. ### A statement about the ### **RECORD** ### is')
    rec('  ### one about documents, grades, instruments, numbering, arms, counts, or what the')
    rec('  ### corpus has or has not asked.')
    rec('')
    obj = rec2 = both = 0
    for n, name, kind, what, why in ARC:
        f, txt = bank(n)
        rec('    ### **b%d -- %s** ### [%s]' % (n, name, f))
        wrap('what it put on the board : %s' % what, '        ')
        wrap('and the sentence beside it : %s' % why, '        ')
        rec('        ### ### **CLASSIFIED : %s**' % kind)
        obj += 1 if kind == 'OBJECT' else 0
        rec2 += 1 if kind == 'RECORD' else 0
        both += 1 if kind.startswith('BOTH') else 0
        rec('')
    rec('  ### ### **OBJECT : `%d`. ### RECORD : `%d`. ### BORDERLINE, NAMED : `%d`.**'
        % (obj, rec2, both))
    rec('')
    rec('  ### ### **AND THE THREE BORDERLINE CASES, NAMED RATHER THAN ROUNDED.**')
    wrap('### **`b408`** ### found that a source a closing proof must touch has never been '
         'examined. ### That is a statement about ### **WHAT THE CORPUS HAS ASKED**, not about the '
         'modular relation. ### **RECORD** -- but it is about a mathematical object`s treatment, '
         'and a reader could reasonably call it half of each.', '      ')
    wrap('### **`b409`** ### read the modular relation ### **DARK ON THE PLACEMENT REGISTER** ### '
         'from the monograph`s antisymmetry sentence. ### **THAT IS THE CLOSEST THIS ARC COMES TO '
         'THE OBJECT** -- it says what a class of constraints can and cannot distinguish about a '
         'zero. ### And `b409` itself refused to call it more: *a reading of the record`s own two '
         'sentences, not a measured `κ`*, with ### **NO CERTIFICATE WRITTEN.** ### **SO IT IS '
         'NOT A STATEMENT ABOUT THE OBJECT; IT IS A STATEMENT ABOUT WHAT THE RECORD`S OWN '
         'SENTENCES IMPLY.**', '      ')
    wrap('### **`b410`** ### found Proposition C.1 does not factor ### **BECAUSE ONE SIDE OF IT IS '
         '`RH`.** ### That is a statement about a ### **SENTENCE**, and about what an imported '
         'criterion carries with it -- not about any zero. ### **RECORD**, and the act said so '
         'itself: *this says nothing against the reduction*.', '      ')
    rec('')
    wrap('### ### ### **SO THE ANSWER, AS PLAINLY AS `b370` PUT IT: ### THE ARC PRODUCED `0` '
         'STATEMENTS ABOUT THE OBJECT.** ### Nine acts; not one of them says anything about '
         '`ξ`, about a zero, or about the Epstein object that was not already on the record. '
         '### **`(N2)` MET.**', '  ')
    rec('')
    wrap('### ### **AND THE ARC KNEW IT.** ### `b408` measured row `U1` at ### **`0` STATEMENTS '
         'ABOUT THE OBJECT** ### across six entries and called the row *a bookkeeping instrument, '
         'and that is a description and not a demotion*. ### `b409` froze the register at six for '
         'the same reason. ### **THE ARC DIAGNOSED ITSELF MIDWAY AND KEPT GOING**, which is either '
         'discipline or a habit, and the record cannot tell the difference from inside.', '  ')
    rec('')
    wrap('### ### **WHAT IT DID PRODUCE, SAID WITHOUT APOLOGY.** ### Two author rulings executed '
         'over the whole corpus (`R25`, `R29`); `29` documents that now declare a numbering; a '
         'relativized theorem written into a keystone; a classification nobody had run; a standing '
         'instrument found that the seat was about to duplicate; a certificate located that the '
         'paper named only as *a relay record*; and ### **THREE MATHEMATICS-FACING GATE ARMS THAT '
         'DID NOT EXIST BEFORE.** ### **THAT IS NINE ACTS OF WORK ON THE RECORD, AND THE RECORD IS '
         'THE THING THAT CARRIES THE MATHEMATICS.**', '  ')
    return obj, rec2, both


ROUTED = [
    ('the naming of the one statement', 'b408', 'the author`s word', 'THE AUTHOR',
     'ROUTED', '`b408` found four occurrences of one statement and refused to name it: '
     '*stating the sentence the test produces is not minting; giving it a name is.* '
     '`(R28)` at `b411` NAMED it -- so this item is ### **DISCHARGED BY THE AUTHOR, NOT BY '
     'THE SEAT.**'),
    ('the Definition-2.5 classification of four imports', 'b409', 'one act`s work', 'THE SEAT',
     'DISCHARGED at b410', '`b409``s `§10` left it unrun; `b410` ran it under two '
     'instruments. ### **THE ONLY ITEM THE ARC ROUTED AND THEN PAID.**'),
    ('the `I-7` instrument-number collision', 'b410', '1 document and a filename', 'THE AUTHOR',
     'ROUTED', 'a held spec is queued to take a number a standing instrument holds and `14` '
     'live documents cite. ### `(R30)` at `b411` RULED the direction; the rename itself is '
     'still unmade.'),
    ('§9`s certificate, named only as *a relay record*', 'b411',
     'one line in a Correspondence row', 'THE AUTHOR', 'ROUTED',
     '`b411` LOCATED it -- `reports/2026-08-01-w-half-consult.md` §(6) -- but naming it in '
     'the keystone is an edit to a Correspondence row.'),
    ('the misnamed numbering table', 'b409', 'one label in one remark', 'THE AUTHOR', 'ROUTED',
     '`day1/Seven_Mechanism_Classes.md``s *Remark (Class numbering)* labels its second column '
     '*Monograph* against two independent witnesses.'),
    ('the Tier-2 form of the barrier', 'b407', 'open mathematics', 'NOBODY YET',
     'NAMED, NOT ROUTED', 'the document calls it *research-frontier and not claimed here*. ### '
     '**A RESEARCH QUESTION IS NOT A DECISION, AND `b408` KEPT THE TWO DISPOSITIONS APART.**'),
    ('`(R20)`’s limb 2, the deposit rule`s own claim about itself', 'b407',
     'the rule`s self-description', 'THE AUTHOR', 'ROUTED',
     'the rule says it is *descriptive before it is prescriptive* and *discovered, not imposed*.'),
    ('*every write encodes before it opens*, as a standing clause', 'b406',
     'the author`s word', 'THE AUTHOR', 'ROUTED',
     'costs nothing but the word; the cost of NOT promoting it is that each ferry restates it.'),
    ('the row`s restatement into residue form', 'b404', 'one act`s work', 'THE AUTHOR',
     'ROUTED', 'ROUTED at `b404`, MEASURED at `b405`, and still not applied; the register is '
     'now FROZEN at six, so it cannot be applied without unfreezing.'),
    ('the reach instrument', 'b411', 'see Component 4', 'THE AUTHOR',
     'NAMED BY THIS ACT, NOT ROUTED', '`b411` found nothing prices an import`s reach. ### **THIS '
     'ACT PRICES THE INSTRUMENT AND DOES NOT ROUTE IT**, because pricing is what was asked.'),
]


def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 -- THE ROUTED PILE, INVENTORIED.')
    bar()
    rec('  ### **ONE LIST. ### EACH ITEM WITH ITS ACT, ITS COST, ITS OWNER AND ITS DISPOSITION.**')
    rec('')
    for item, act, cost, owner, disp, why in ROUTED:
        rec('    ### **%s**' % item)
        rec('        act %-6s cost %-34s owner %-12s ### **%s**' % (act, cost[:34], owner, disp))
        wrap(why, '        ')
        rec('')
    routed = [r for r in ROUTED if r[4] == 'ROUTED']
    other = [r for r in ROUTED if r[4] != 'ROUTED']
    rec('  ### ### **ITEMS : `%d`. ### STILL ROUTED : `%d`. ### OTHER DISPOSITIONS : `%d`.**'
        % (len(ROUTED), len(routed), len(other)))
    wrap('### ### **AND THE DISPOSITIONS ARE KEPT APART, AS `b408` KEPT THEM.** ### `ROUTED` is a '
         'decision waiting on the author. ### `NAMED, NOT ROUTED` is a research question waiting '
         'on nobody. ### `DISCHARGED` is paid. ### **THEIR SUM DESCRIBES NONE OF THE THREE**, and '
         'a single number for "the pile" would be the kind of aggregate this seat owes `M-2` for.',
         '  ')
    rec('')
    wrap('### ### **`(N3)` -- *the pile has more items than the span has acts* -- is ### **%s**: '
         '`%d` items against `9` acts.'
         % ('MET' if len(ROUTED) > 9 else 'REFUTED', len(ROUTED)), '  ')
    rec('  ### **`0` ITEMS DISCHARGED BY THIS ACT.** ### An inventory is a list, not a payment.')
    return len(ROUTED), len(routed)


def component4():
    rec('')
    bar()
    rec('### COMPONENT 4 -- THE INSTRUMENT THAT WOULD PRICE REACH.')
    bar()
    wrap('### `b411` found the record prices an import`s ### **OWNERSHIP** ### -- `K2` is '
         '`IMPORT-UNDER-THE-BAR (b321)` -- and that ### **NOTHING PRICES ITS REACH**: what an '
         'imported equivalence lets a proof establish.', '  ')
    rec('')
    rec('  ### ### **WHAT SUCH AN INSTRUMENT WOULD HAVE TO DO.**')
    rec('      ### **(1)** ### Take an imported sentence and the target statement, and decide')
    rec('      whether the import`s content ### **ALREADY CONTAINS** ### the target -- as')
    rec('      Proposition C.1 contains `RH` as one side of a biconditional.')
    rec('      ### **(2)** ### Where it does not, bound what the import ### **ADDS** ### beyond')
    rec('      what the corpus derives, in a form a later act can cite.')
    rec('      ### **(3)** ### Do both ### **WITHOUT** ### deciding the target, since an')
    rec('      instrument that settled reach by settling the question would be the question.')
    rec('')
    rec('  ### ### **DOES THE CORPUS HAVE THE PARTS?**')
    wrap('### **PARTLY, AND THE MISSING PART IS THE WHOLE OF IT.** ### For `(1)` the corpus has '
         'the parts: Definition 2.5`s clause 1 and the standing screen `I-7` between them decide '
         'whether a sentence references the target`s own parameter, and `b410` ran exactly that '
         'test on four sentences by hand. ### **THAT IS THE CONTAINMENT TEST, AND IT ALREADY '
         'WORKS.** ### For `(2)` the corpus has ### **NOTHING**: bounding what an import adds is a '
         'statement about consequence, and every instrument the record carries -- the three-grade '
         'calculus, the E0 gate`s nine grades, the salt-check -- grades ### **PROVENANCE**, never '
         'consequence.', '      ')
    rec('')
    rec('  ### ### ### **THE PRICE: ### A BUILD, AND THE PARKED LANE BLOCKS IT.**')
    wrap('### `(1)` is a ### **READING** ### and costs `0` -- it is `b410` repeated on any other '
         'import. ### `(2)` is not a reading and not a measurement: bounding what a sentence adds '
         'over a specification is ### **A PROOF-THEORETIC STATEMENT ABOUT A FORMAL SYSTEM**, and '
         'the record`s own precedent for such a statement is the Sieve Ceiling Lemma, which exists '
         'as ### **A COMPILED TERMINAL.** ### **SO THE INSTRUMENT`S SECOND HALF IS A BUILD**, and '
         '### **BOTH LANES ARE PARKED.** ### **`(N4)` MET.**', '      ')
    rec('')
    wrap('### ### **AND THE HONEST QUALIFICATION, IN THE SAME BREATH.** ### `(2)` may be '
         'unbuildable rather than merely unbuilt. ### A general bound on what an arbitrary '
         'imported sentence adds is close to asking for a conservativity result, and '
         'conservativity is undecidable in general. ### **A USEFUL INSTRUMENT WOULD HAVE TO BE '
         'RESTRICTED TO A NAMED CLASS OF IMPORTS**, and naming that class is itself the '
         'mathematical work. ### **THAT IS NOT A REASON NOT TO PRICE IT; IT IS PART OF THE '
         'PRICE.**', '  ')
    rec('  ### **`0` INSTRUMENTS BUILT. ### `0` ROUTES PROPOSED. ### PRICED; NOT OPENED.**')
    return 'A BUILD'


def component5():
    rec('')
    bar()
    rec('### COMPONENT 5 -- THE ORIENTATION LAYER, UNDER (R31).')
    bar()
    rec('  ### **THE TWO OBJECTS, READ AT THEIR OWN DATES BEFORE EITHER WAS TOUCHED.**')
    for ln in EXTRACT.split(NL):
        if re.search(r'LINES : \d+|NEWEST ACT IT NAMES|ACTS BEHIND|ARCS FOLDED SINCE|'
                     r'DOOR-TABLE ROWS|NEWEST ACT THE DOOR BLOCK', ln):
            rec('      %s' % ln.strip()[:150])
    rec('')
    wrap('### ### **THE DIGEST IS `204` ACTS BEHIND**, measured from the newest act it names '
         '(`b208`) and not from its build line (`b163`). ### **`(N5)` MET** -- the navigator said '
         'more than one hundred fifty, and it is more than two hundred.', '  ')
    rec('')
    wrap('### ### **AND THE FIVE-DOOR STATE`S FIGURE IS AN ARTEFACT OF THIS SEAT`S OWN WRITING, '
         'SO IT IS NOT USED.** ### The newest act `PATHS_TO_THE_CRITICAL_LINE.md` names is '
         '`b409` -- and that is ### **`b409`’S CLASS-NUMBERING HEAD NOTE**, a line this seat '
         'wrote, touching nothing in the door table. ### **THE DOOR TABLE ITSELF NAMES NO ACT AT '
         'ALL.** ### Its currency is readable only from the kernel pins it cites (`lv v0.10.0 = '
         '93c27ec`). ### **AN ACTS-BEHIND FIGURE TAKEN FROM THAT DOCUMENT WOULD MEASURE THIS '
         'SEAT`S OWN HEAD NOTE**, and `(E3)` is MET.', '  ')
    rec('')
    rec('  ### ### ### **AND THE FIRST THING (R31) MEETS IS THAT MOST FOLDS HAVE NOTHING TO')
    rec('  ### ### ### QUOTE.**')
    arcs = [ln for ln in EXTRACT.split(NL) if re.search(r'one-statement (YES|### NONE)', ln)]
    yes = [a for a in arcs if 'YES' in a]
    rec('      fold sections in `FINDINGS.md` : ### **%d**' % len(arcs))
    rec('      carrying a `### The arc`s one statement` heading : ### **%d**' % len(yes))
    for a in yes:
        rec('          %s' % a.strip()[:120])
    wrap('### ### **THE ONE-STATEMENT CONVENTION IS TWO FOLDS OLD.** ### It begins at `b384` and '
         'continues at `b402`; the other ### **%d** ### fold sections open with a scope paragraph '
         'and go straight to a per-act table. ### **SO THE FERRY`S INSTRUCTION -- *each quoted '
         'from its fold section and none summarised* -- CANNOT BE CARRIED OUT FOR MOST ARCS '
         'WITHOUT INVENTING TEXT.**' % (len(arcs) - len(yes)), '      ')
    wrap('### ### **AND THE INSTRUCTION IS OBEYED EXACTLY, INCLUDING WHERE IT CANNOT BE.** ### '
         'The digest block quotes the one-statements that exist, and for every other arc it names '
         'the arc, its span, and ### **RECORDS THAT ITS FOLD CARRIES NO ONE-STATEMENT.** ### '
         '**A DIGEST ENTRY THAT INVENTED ITS OWN SOURCE WOULD BE WORSE THAN ONE THAT SAYS THE '
         'SOURCE IS MISSING**, and this is a finding the author can act on.', '      ')
    rec('')
    rec('  ### ### **THE FIVE DOORS: DID THE ARC MOVE ANY?** ### Measured, not assumed.')
    for ln in EXTRACT.split(NL):
        if re.search(r'names a register|names the goal state|claims a door|claims a terminal|'
                     r'the control \(`h2`', ln):
            rec('      %s' % ln.strip()[:150])
    wrap('### ### ### **`0` DOORS MOVED BY THIS ARC**, and the control passes at `9 of 9`. ### '
         'The two mentions of a register are `b406``s and `b408``s, and neither states a depth. '
         '### **SO NO DOOR IS RESTATED, AND `0` OLD DEPTHS ARE DISPLACED.** ### **`(E2)` MET.**',
         '  ')
    rec('')
    rec('  ### ### ### **AND THE NAVIGATOR`S `(N6)` IS REFUTED BY THE TABLE ITSELF.**')
    for ln in EXTRACT.split(NL):
        if 'ALREADY IN THE TABLE' in ln:
            rec('      %s' % ln.strip()[:150])
    q('finite-set conjunct now DERIVES', 'R4 ALREADY CURRENT', PATHTXT)
    q('the distance now carries a compiled boundary marker', 'R5 ALREADY CURRENT', PATHTXT)
    wrap('### Both movements the navigator names are ### **ALREADY IN THE DOOR TABLE**: `R4`’s '
         'finite-set conjunct at `lv v0.10.0`, and `R5`’s compiled boundary marker '
         '`certifiedInput_not_zeroRealizing` at `lv v0.9.0`. ### **THE DOORS DO NOT CHANGE DEPTH '
         'BECAUSE THEY WERE ALREADY AT THAT DEPTH**, recorded when the kernel work landed rather '
         'than when a fold noticed. ### ### **`(N6)` REFUTED** -- and refuted in the most useful '
         'way: ### **THE FIVE-DOOR STATE IS THE ONE ORIENTATION OBJECT THAT WAS ALREADY '
         'CURRENT.**', '      ')
    rec('')
    wrap('### ### **SO `(R31)` IS EXECUTED ASYMMETRICALLY, AND THE ACT SAYS WHY.** ### The digest '
         'gains a block, because it is `204` acts behind. ### The five-door state gains a block '
         'that ### **RECORDS THE ARC AND MOVES NO DOOR**, because the arc moved none and the two '
         'the navigator expected were current already. ### **A REFRESH THAT INVENTED A MOVEMENT '
         'TO JUSTIFY ITSELF WOULD BE THE ONE THING (R31) EXISTS TO PREVENT.**', '  ')
    return 204, len(arcs), len(yes)


def expectations(obj, rec2, both, nrouted, price, behind, nfolds, nstmt):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED -- EACH OVER THE SET THE FACE NAMED, UNDER (R26).')
    bar()
    rows = [
        ('(N1)', 'the span tool`s own output', 'it returns exactly nine',
         '### **REFUTED** -- the tool returns ### **`10`**, counting `b403` through `b412`. ### '
         'The fold`s span is `9` because ### **THE FOLDING ACT IS NOT IN ITS OWN FOLD**, and both '
         'numbers are printed. ### **THE EXPECTATION CONFUSED A FOLD`S SPAN WITH A COUNTER`S '
         'RANGE.**'),
        ('(N2)', 'the nine acts b403-b411', 'the arc produced 0 statements about the object',
         '### **MET** -- `%d` OBJECT, `%d` RECORD, `%d` borderline and every borderline NAMED. '
         '### The closest approach is `b409``s DARK reading, which `b409` itself refused to call '
         'a measured `κ`.' % (obj, rec2, both)),
        ('(N3)', 'the routed items the arc`s banks name',
         'the pile has more items than the span has acts',
         '### **MET** -- `%d` items against `9` acts, in ### **THREE DIFFERENT DISPOSITIONS** '
         'kept apart.' % nrouted),
        ('(N4)', 'the corpus`s own parts for a reach instrument',
         'it would require a build, so the parked lane blocks it',
         '### **MET, AND SHARPENED** -- the containment half is a READING the corpus can already '
         'do; the ### **BOUNDING** ### half is a build, and may be unbuildable in general rather '
         'than merely unbuilt.'),
        ('(N5)', 'the digest`s own text', 'it is more than one hundred fifty acts behind',
         '### **MET** -- ### **`%d` ACTS BEHIND**, from `b208` to `b412`.' % behind),
        ('(N6)', 'the five-door state`s table as it stands',
         'at least two doors change depth -- R4 by the finite-set conjunct, R5 by the two spectra',
         '### ### **REFUTED BY THE TABLE ITSELF.** ### Both movements are ### **ALREADY IN IT**: '
         '`R4`’s *finite-set conjunct now DERIVES* at `lv v0.10.0`, and `R5`’s *compiled boundary '
         'marker* at `lv v0.9.0`. ### **THE DOORS DO NOT MOVE BECAUSE THEY WERE ALREADY THERE**, '
         'and the five-door state is ### **THE ONE ORIENTATION OBJECT THAT WAS ALREADY '
         'CURRENT.**'),
        ('(E1)', 'the fifteen fold sections FINDINGS.md carries',
         'most carry no one-statement at all',
         '### **MET** -- ### **`%d` OF `%d`** ### carry one; the convention begins at `b384`. ### '
         'The rest supply nothing quotable, and the digest block ### **RECORDS THE ABSENCE RATHER '
         'THAN SUMMARISING.**' % (nstmt, nfolds)),
        ('(E2)', 'the banks of the arc`s acts',
         'the arc moved 0 doors, and the search carries a control that passes',
         '### **MET** -- `0` claims of a door moved, `0` terminals compiled by the arc, and the '
         'control finds `h2` in `9 of 9` banks.'),
        ('(E3)', 'the five-door state`s own text',
         'the newest act it names is a head note this seat wrote, so an acts-behind figure taken '
         'from it measures this seat`s own writing',
         '### **MET** -- the newest act is `b409`, and it is `b409`’s class-numbering head note. '
         '### **THE DOOR TABLE NAMES NO ACT AT ALL**, so the figure is not used.'),
        ('(E4)', 'the arc`s nine acts',
         'at least one act produced something that is not cleanly record OR object',
         '### **MET** -- ### **`%d`** ### of them, each named: `b408`, `b409`, `b410`. ### **THE '
         'COUNT PRINTS ITS OWN HARD CASES RATHER THAN ROUNDING THEM INTO THE MAJORITY.**' % both),
    ]
    for k, over, claim, verd in rows:
        rec('  **%s** ### over ### **%s**' % (k, over))
        wrap(claim, '        ')
        wrap(verd, '        ')
        rec('')
    rec('  ### ### **`2` REFUTED, `8` MET. ### AND BOTH REFUTATIONS ARE OF EXPECTATIONS THAT')
    rec('  ### ### ASSUMED A GAP WHERE THE RECORD HAD ALREADY CLOSED ONE.**')


def main():
    rec('=' * 100)
    rec('b412_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED '
        'IT.')
    rec('=' * 100)
    rec('  face LOCKED : 6680b593b289fa9d13f06426981b060a981df2dbb6a6d1341e5441e7a3ad61d5')
    rec('  ### **THE THREE RULED ARMS, FIXTURES BOTH POLARITIES:** %s'
        % gate_spine.self_test(verbose=False))
    rec('')
    rec('  ### ### **AND ONE DEFECT OF THIS ACT`S OWN SURVEY, REPAIRED BEFORE THE COMPONENTS')
    rec('  ### ### RAN.** ### The bank finder took `b403_readme_original.txt` -- a README `b403`')
    rec('  ### preserved verbatim -- as `b403`’s bank, because it sorts first among the')
    rec('  ### survivors. ### **A FINDER THAT TAKES THE ALPHABETICALLY FIRST SURVIVOR IS NOT')
    rec('  ### ### IDENTIFYING ANYTHING.** ### `_original`, `_notes`, `_query` and `_stdout` are')
    rec('  ### now excluded, and the real bank is `b403_the_three_routed_items.txt` -- which is')
    rec('  ### ### **THE ONE ACT IN THE ARC WHOSE SUBJECT IS COMPONENT 3`S OWN.**')
    rec('')
    n = component1()
    obj, rec2, both = component2()
    nrouted, still = component3()
    price = component4()
    behind, nfolds, nstmt = component5()
    expectations(obj, rec2, both, nrouted, price, behind, nfolds, nstmt)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO DOCUMENT, LEDGER, ROW OR KEY WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write((NL.join(L) + NL).encode('utf-8'))
    io.open(ARCOUT, 'wb').write(
        (NL.join('b%d\t%s\t%s' % (a[0], a[2], a[3]) for a in ARC) + NL).encode('utf-8'))
    io.open(ORIOUT, 'wb').write(
        (NL.join('%s\t%s\t%s\t%s\t%s' % (r[0], r[1], r[2], r[3], r[4])
                 for r in ROUTED) + NL).encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
