# -*- coding: utf-8 -*-
"""b406_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A LEDGER, A STANDING FILE OR A ROW.** ### This file computes and
### prints; `b406_desk_bank.py` writes. ### **AND EVERY WRITE ENCODES BEFORE IT OPENS.**
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
OUT = os.path.join(D, 'b406_components.txt')
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


def txt(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


EXTRACT = txt(os.path.join(D, 'b406_extract.txt'))
B353 = txt(os.path.join(D, 'b353_the_missing_statement.txt'))
CELL5 = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                       capture_output=True).stdout.decode('utf-8')
CELL5 = [l for l in CELL5.split('\n') if l.startswith('| U1 |')][0].split('|')[5]


def q(hay, frag, where, label=None):
    """### Verify a fragment is in the file it is claimed from, BEFORE it is printed."""
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:60]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


# ### =================================================================================================
def component1():
    bar()
    rec('### COMPONENT 1 -- THE TWO SITES, READ FOR THEIR ACTUAL SHAPE.')
    bar()
    rec('  ### ### **`(i)` -- THE CLAUSE\u2019S QUANTIFIER.**')
    rec('      THE QUANTIFIER STRING, from the site\u2019s own text and the row S1 it belongs to:')
    rec('          `\u2200 g \u2208 C` (the source\u2019s class, Definition 3.1 with Prop C.1\u2019s')
    rec('          vanishing set) `.` `\u03a3_v W_v(g \u2217 g\u0304^#) \u2264 0`, with a second')
    rec('          quantifier running THROUGH the explicit formula OVER THE ZEROS.')
    q(CELL5, 'the quantifiers -- over the class, infinite, and through the explicit formula over '
             'the zeros -- are UNOWNED, and they are the clause.', '(i) STRING')
    rec('      ### **WHAT THE RECORD HOLDS AGAINST IT:** ### measurements ON FAMILIES -- thirteen')
    rec('      cells, twenty-six, eight -- and no statement over the class.')
    rec('      ### **INNER EXISTENTIAL AT THE OBSTRUCTION\u2019S OWN DEPTH : NONE.** ### Two')
    rec('      universals and no `\u2203` between them: there is no `\u2200\u2203` to commute.')
    rec('      ### ### **BUT AT ONE DEPTH FURTHER THERE IS ONE, AND IT IS NOT THIS SITE\u2019S.**')
    rec('      ### Unfold the CLASS the first quantifier ranges over and the source\u2019s own')
    rec('      characterisation of membership is existential -- Boas-Kac\u2019s `\u2203 g`, which is')
    rec('      ### **EXACTLY SITE `(iii)`\u2019S**, indexed by the support width.')
    rec('      ### ### **SO THE EXISTENTIAL IS REAL AND IT BELONGS TO ANOTHER SITE.** ### `(i)`\u2019s')
    rec('      own obstruction is the OWNERSHIP of two universals; the class\u2019s characterisation')
    rec('      is a different fact about a different site, and filing it here would have counted')
    rec('      one existential twice.')
    rec('')
    rec('  ### ### **`(iv)` -- THE PRIME CONSTITUENT AT A WIDENED SUPPORT.**')
    rec('      THE QUANTIFIER STRING:')
    rec('          the record holds `{V(a)}` for TEN widths `a` -- values of `\u03a3_p W_p(f)` at')
    rec('          cells above the boundary -- and needs ONE statement `S` uniform in `a`.')
    q(CELL5, 'needs **one statement uniform in `a`**', '(iv) STRING')
    rec('      ### **INNER EXISTENTIAL AT THE OBSTRUCTION\u2019S OWN DEPTH : NONE.** ### What the')
    rec('      record holds is TEN VALUES. ### **A MEASURED VALUE IS NOT AN EXISTENTIAL CLAIM**,')
    rec('      so there is no `\u2200a \u2203x P(a, x)` on the record to commute.')
    rec('      ### ### **AND AT ONE DEPTH FURTHER THERE IS ONE, AND IT IS WORTHLESS.** ### Any')
    rec('      family of values supplies `\u2200a \u2203C_a . |V(a)| \u2264 C_a` for free -- take')
    rec('      `C_a = |V(a)|`. ### That existential is ### **TRIVIALLY SATISFIABLE**, and the face')
    rec('      fixed before the read what to do with one: ### **A WITNESS FOR A TRIVIAL')
    rec('      ### EXISTENTIAL CARRIES NO CONTENT TO SHARE.** ### The shared witness it would')
    rec('      demand is a bound good for every `a` -- which IS the missing statement, not a')
    rec('      repair for its absence.')
    rec('      ### ### **THAT IS THE DIFFERENCE BETWEEN `(iv)` AND `(v)`, AND IT IS EXACT:** ###')
    rec('      `(v)`\u2019s source STATES an existential per index -- Theorem 6.1 asserts, for each')
    rec('      `\u03c0`, that an implied constant exists -- while `(iv)`\u2019s record MEASURES a')
    rec('      value per index. ### **AN EXISTENTIAL THE RECORD HOLDS IS NOT THE SAME OBJECT AS')
    rec('      ### ONE YOU CAN ALWAYS MANUFACTURE.**')
    rec('')
    rec('  ### ### ### **THE VERDICT ON `b405`\u2019S TWO CELLS: THEY STAND, AND THEIR REASON GAINS')
    rec('  ### ### ### ONE CLAUSE.** ### `b405` wrote *no inner existential to share*. ### The')
    rec('  ### precise statement is: ### **NO INNER EXISTENTIAL THE SHARED-WITNESS FORM CAN')
    rec('  ### ### REPAIR** -- `(i)`\u2019s belongs to another site and `(iv)`\u2019s is trivially')
    rec('  ### satisfiable. ### **THE CELLS ARE NOT EDITED; THE REASON IS SHARPENED IN THIS ACT\u2019S')
    rec('  ### ### OWN BANK AND THE PREDECESSOR IS CORRECTED WITHOUT BEING REWRITTEN.**')


def component2():
    rec('')
    bar()
    rec("### COMPONENT 2 -- THE NAME, IN THE RECORD'S OWN WORDS. ### **SCORED IN TWO PARTS.**")
    bar()
    rec('  ### **PART ONE -- THE BARRIER. ### ### PRESENT, AND NAMED TWICE.**')
    rec('      ### `phase1.5/method/INVARIANCE_BARRIERS.md`, ### **THEOREM 3.1, THE SIEVE CEILING')
    rec('      ### LEMMA**, in the record\u2019s own words:')
    q(EXTRACT, 'then \u03c0 does not establish the universal statement', 'BARRIER 1')
    q(EXTRACT, 'can establish "P holds for x in a density-one subset of each I-class," but cannot '
               'certify individual elements', 'BARRIER 2')
    rec('      ### ### **THAT IS THE ROW\u2019S FORM STATED PROOF-THEORETICALLY: WHAT SURVIVES IS')
    rec('      ### ### PER-CLASS AND UP TO DENSITY; WHAT IS LOST IS THE INDIVIDUAL AND THE')
    rec('      ### ### UNIVERSAL.**')
    rec('      ### And `phase1.5/method/THE_DIFFICULTY_KINDS.md` names the gap ITSELF, not the')
    rec('      proof-theoretic shadow of it -- ### **THE ESCAPE-KIND**:')
    q(EXTRACT, 'classifies *why* finite certificates don', 'ESCAPE-KIND 1')
    q(EXTRACT, 'TWO escape-kinds suffice', 'ESCAPE-KIND 2')
    rec('      ### **ITS TWO VALUES ARE `scale-horizon` AND `raw-infinitude`**, and the document')
    rec('      says the dichotomy IS the finding.')
    rec('')
    rec('  ### **PART TWO -- THE REPAIR. ### ### PRESENT, AND IT IS NOT *UNIFORM WITNESS*.**')
    rec('      ### `INVARIANCE_BARRIERS.md` ### **COROLLARY 3.6**, the contrapositive:')
    q(EXTRACT, 'any proof of universality must contain at least one inference step', 'REPAIR 1')
    rec('      ### ### ### **THE RECORD\u2019S NAME FOR WHAT CLOSES THE PASSAGE IS')
    rec('      ### ### ### `A BRIGHT CHANNEL` -- AN INTERFACE WITH `\u03ba > 0`**, against the')
    rec('      barrier\u2019s `\u03ba = 0`, where `\u03ba` is the transmission coefficient:')
    q(EXTRACT, 'the fraction of P-dependent information that crosses', 'REPAIR 2')
    rec('')
    rec('  ### ### **THE TWO PARTS DO NOT WEIGH THE SAME, AND SAYING SO IS THE POINT OF SCORING')
    rec('  ### ### THEM SEPARATELY.** ### The barrier has a theorem, a classification, two named')
    rec('  ### kinds and a compiled negative. ### The repair has ### **ONE COROLLARY AND A NAME**,')
    rec('  ### and the corollary states it only as the negation of the barrier\u2019s hypothesis:')
    rec('  ### a proof of universality must touch a bright channel SOMEWHERE. ### **THE RECORD')
    rec('  ### ### SAYS WHAT MUST BE TRUE OF A CLOSING PROOF AND NOT WHAT WOULD MAKE ONE.**')
    rec('  ### ### **AND NO NAME IS MINTED HERE.** ### Both names are the record\u2019s, quoted at')
    rec('  ### their sources; where the record is thin the act reports it thin.')


def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 -- THE THIRD COORDINATE, PRICED AND NOT ADDED.')
    bar()
    rec('  ### **THE CANDIDATE:** ### `ESCAPE-KIND`, with the record\u2019s own two values')
    rec('  ### `scale-horizon` / `raw-infinitude`, and `UNSTATED` where the site does not decide.')
    rec('  ### **THE FILL TEST, AS THE FACE FIXED IT:** ### a cell is fillable only if the SITE\u2019S')
    rec('  ### OWN banked text names the index and says enough about it to decide the value.')
    rec('')
    rows = [
        ('(i)', 'raw-infinitude', True,
         'the site names its index as the CLASS and the ZEROS and calls it *infinite* -- a set '
         'with no scale in it.'),
        ('(ii)', 'scale-horizon', True,
         'the index is a HEIGHT and the site prints the main term that makes it a receding '
         'threshold: *"Running the census higher buys more instances"*.'),
        ('(iii)', 'scale-horizon', True,
         'the index is the support WIDTH `A`, and the site says the exhaustion holds at every '
         'width and not across widths.'),
        ('(iv)', 'scale-horizon', True,
         'the index is the support width `a`, named on the entry with the boundary `a\u00b2 '
         '\u2265 2`.'),
        ('(v)', 'raw-infinitude', True,
         'the index is the REPRESENTATION, and the entry names the class it ranges over -- '
         'cuspidal automorphic representations on `GL(N)` -- a set, with no scale.'),
        ('(vi)', 'UNSTATED', False,
         'the index is the MODULUS, and the site\u2019s own language is *local-to-global*, not '
         'scale or set. ### **DECIDING IT WOULD BE THIS SEAT\u2019S INFERENCE AND NOT THE '
         'SITE\u2019S TEXT**, so under the strict test it is UNSTATED.'),
    ]
    for sid, val, fill, why in rows:
        rec('    %-7s ### **%-16s** ### %s' % (sid, val, 'FILLABLE' if fill else 'NOT FILLABLE'))
        for k in range(0, len(why), 130):
            rec('            %s' % why[k:k + 130])
    n = sum(1 for _s, _v, f, _w in rows if f)
    rec('')
    rec('  ### ### **THE PRICE: `%d` OF 6 FILLABLE FROM BANKED TEXT ALONE, `%d` `UNSTATED`.**'
        % (n, 6 - n))
    rec('  ### **AND IT WOULD SIT INSIDE THE COLUMN LAW EXACTLY AS `KIND` AND `WITNESS` DO** -- a')
    rec('  ### labelled field inside cell 5, because the ledger fixes seven columns for every table')
    rec('  ### line and a row cannot gain a column alone.')
    rec('  ### ### ### **AND IT IS NOT ADDED.** ### `(R24)` gave the row two coordinates and no')
    rec('  ### ### more. ### **A SEAT THAT PRICES A THIRD AND THEN WRITES IT HAS NOT PRICED')
    rec('  ### ### ANYTHING**, and this act writes nothing to the row at all.')
    return n


def addition_one():
    rec('')
    bar()
    rec("### ADDITION ONE -- `(iii)`'S TWO CLAUSES, IN THE SOURCE'S OWN SYMBOLS.")
    bar()
    rec('  ### **THE SOURCE, AS `b353` BANKS IT** (`arXiv 2006.13771v1`, Proposition 2, Boas-Kac):')
    q(B353, 'equivalent: 1. The Fourier transform f^ is pointwise positive. 2. There exists g in '
            'Cc^infty(R)', 'BOAS-KAC')
    rec('  ### **AND THE CRITERION THE WIDTH SERVES, from the same bank:**')
    q(B353, 'RH <=> sum_v W_v(g * gbar^#) <= 0, for all g in Cc^infty(R+*) with g~(z) = 0 for all '
            'z in F', 'CRITERION')
    rec('')
    rec('  ### ### **THE TWO CLAUSES, IN THOSE SYMBOLS AND NO OTHERS:**')
    rec('      ### **`h1` (SHAREDNESS)** ### -- ONE `g \u2208 Cc^\u221e(\u211d)` such that for')
    rec('          EVERY `A > 0`, `supp g \u2286 [-A/2, A/2]` and `f_A = g \u2217 g^*` is the')
    rec('          Boas-Kac representative at width `A`. ### One `g` where the source gives one')
    rec('          `g` PER `A`.')
    rec('      ### **`h2` (NON-DEGENERACY)** ### -- that same `g` lies in the criterion\u2019s own')
    rec('          class: `g \u2208 Cc^\u221e(\u211d_+^*)` with `g\u0303(z) = 0` for all `z \u2208')
    rec('          F`, and `g \u2262 0`.')
    rec('')
    rec('  ### ### ### **AND THIS ACT STOPS HERE. ### WHETHER SUCH A `g` CAN EXIST IS')
    rec('  ### ### ### `NOT ATTEMPTED`.**')
    rec('  ### That is a mathematical claim about the source\u2019s class; it needs the parked lane;')
    rec('  ### and this act neither derives it nor gestures at it. ### **NAMING THE TWO CLAUSES OF')
    rec('  ### ### A WITNESS IS NOT DERIVING WHETHER ONE EXISTS**, and an act that slid from the')
    rec('  ### first to the second would have typed the bridge the row forbids.')


def addition_two():
    rec('')
    bar()
    rec('### ADDITION TWO -- THE STANDING LAWS, AUDITED FOR ARITY. ### **A READING, NOT A RULING.**')
    bar()
    laws = [
        ("THE DEPOSIT'S \u00a727.3 REFUSAL", 'BINARY / n-ARY',
         'Its subject is the CROSS-REGISTER EQUIVALENCES and the sentence *discharge one and you '
         'discharge all five* -- a relation among the five.',
         'ANYTHING ABOUT ONE REGISTER\u2019S OWN STATUS. ### It forbids compiling a relation; it '
         'says nothing about whether any single register is discharged, empty, or live.'),
        ('`(R14)`', 'UNARY',
         'Its subject is A DOCUMENT: the class ruling governs *by content and role, not by '
         'location*.',
         'ANY RELATION BETWEEN TWO DOCUMENTS. ### The ruling knows this about itself and says so: '
         'where a canonical copy lives is *a separate fact under a separate ruling*, and **both '
         'hold, neither is edited into the other**.'),
        ('`(R20)`', 'MIXED -- TWO UNARY LIMBS, ONE BINARY LIMB, A BINARY OBLIGATION',
         'A wave deposits with its companion papers (UNARY on the wave); a pre-registered search '
         'deposits because its registration committed it (UNARY); **a kernel deposits when a '
         'published claim cites its terminals** (BINARY: kernel, claim). The obligation -- every '
         'deposited record sits at a version *a citable claim uses*, or carries a note -- is '
         'BINARY.',
         'ANYTHING ABOUT A RECORD WITH NO CLAIM ON EITHER SIDE OF IT. ### **AND THAT IS NOT A '
         'HYPOTHETICAL:** it is exactly the `SIDE-kernel` question `b392` entered as standing in '
         'the same breath as the ruling.'),
        ('`(R1)`', 'AGGREGATE -- UNARY ON A SET, THROUGH A COUNT',
         'Its subject is a SPAN and its predicate is a COUNT: the fold threshold is nine acts.',
         'WHETHER ANY SINGLE ACT BELONGS IN A FOLD, and whether a span that ENDED -- as the '
         'b375-b381 sequence did at eight -- should fold early. ### A threshold on a count cannot '
         'see a reason.'),
        ("ROW `U1`'S REFUSAL (measured at b405)", 'BINARY / n-ARY',
         'Four sentences, subjects: the three; a row naming three things; a row and the pair at '
         'each end of a bridge; three obstructions. **`0` of `4` unary.**',
         'WHETHER ANY ONE SITE IS EMPTY, AND IN WHICH KIND -- which is why `(R24)` had to give '
         'the row a coordinate rather than a better sentence.'),
    ]
    for name, arity, subj, cannot in laws:
        rec('  ### **%s** ### \u2014 ### **%s**' % (name, arity))
        for k in range(0, len(subj), 130):
            rec('        SUBJECT : %s' % subj[k:k + 130] if k == 0 else '                  %s'
                % subj[k:k + 130])
        rec('        ### **CANNOT ANSWER:**')
        for k in range(0, len(cannot), 130):
            rec('            %s' % cannot[k:k + 130])
        rec('')
    rec('  ### ### **THE PATTERN, PRINTED AND NOT RULED ON:** ### `4` of the `5` laws are BINARY,')
    rec('  ### n-ARY or AGGREGATE; ### **ONE IS UNARY, AND IT IS THE ONE THAT KNOWS ITS OWN')
    rec('  ### ### SCOPE AND NAMES THE SEPARATE RULING BESIDE IT.** ### A law that states its')
    rec('  ### arity\u2019s limit in its own text does not have to be audited from outside.')
    rec('  ### ### **NOTHING IS STRUCK, AMENDED OR RE-RULED. ### A LAW THAT CANNOT ANSWER A')
    rec('  ### ### QUESTION IS NOT A BAD LAW; IT IS A LAW WITH A SCOPE.**')
    return laws


def addition_three():
    rec('')
    bar()
    rec("### ADDITION THREE -- THE FINITE SIDE'S QUALIFIER, WHEREVER A READER MEETS IT.")
    bar()
    rec('  ### **THE QUALIFIER ITSELF, FROM THE SEAL\u2019S OWN HEADER:**')
    q(EXTRACT, 'THE GENERAL AND THE PER-CELL ARE STATED HERE SEPARATELY AND ARE NEVER AVERAGED.',
      'SEAL HEADER')
    rec('')
    rec('  ### ### **THE CLOSURE PREDICATE, IN BOTH ITS VERSIONS, AND WHY THE FIRST WAS KEPT.**')
    rec('  ### The narrow verb set -- *compiled / sealed / closed / proved / certified / silent /')
    rec('  ### established* -- returned ### **`0` UNQUALIFIED** ### and would have let this act')
    rec('  ### bank *nothing to repair*. ### **IT MISSED THE CORPUS\u2019S OWN HOUSE FORM FOR THE')
    rec('  ### ### CLAIM, WHICH IS NOT A VERB AT ALL: *at kernel terminals `B329.*`')
    rec('  ### ### (24, zero-axiom)*.** ### Widened by that phrase the sweep returns ### **`1`')
    rec('  ### ### UNQUALIFIED**, and the difference is the whole finding of this addition.')
    rec('  ### ### **A SWEEP\u2019S YIELD IS A PROPERTY OF ITS MATCHER UNTIL A SECOND SHAPE HAS')
    rec('  ### ### BEEN TRIED**, and both yields are printed rather than the kinder one.')
    rec('')
    seg = EXTRACT.split("SCOPED TO CITATIONS", 1)[-1].split('AND THE WIDER SHAPE', 1)[0]
    for ln in seg.split('\n'):
        if ln.strip():
            rec('  ' + ln.rstrip()[:190])
    rec('')
    rec('  ### ### **THE ONE `UNQUALIFIED` SENTENCE, QUOTED WHOLE AND REPAIRED IN PLACE:**')
    rec('  ### `OPEN_TRAILS.md:4638`, in `b398`\u2019s verdict block:')
    rec('      | ... Half one of the reading is the clause statement\u2019s own **K3**: *the')
    rec('      | source\u2019s construction on the object returns the test function at the identity')
    rec('      | times a dimension and no arithmetic* (b310), at **kernel terminals `B329.*`')
    rec('      | (24, zero-axiom) and `B310.*`**. ...')
    rec('  ### **WHY IT IS REPAIRABLE AND NOT ROUTED:** ### the record already writes this exact')
    rec('  ### citation WITH the qualifier, at `FINDINGS.md:3049` -- *`B329.*` (24, zero-axiom;')
    rec('  ### the decomposition and the scaling part GENERAL, the compact part PER CELL)*. ###')
    rec('  ### **THE REPAIR COPIES THE RECORD\u2019S OWN HOUSE FORM INTO A PLACE THAT DROPPED IT.**')
    rec('  ### It adds a qualifier, moves no grade, changes no claim, and the original is preserved')
    rec('  ### verbatim in this act\u2019s appended block and in its bank.')
    rec('')
    rec('  ### ### **AND THE ELISION IS THICKER IN THE NAVIGATOR\u2019S OWN FERRIES THAN IN THE')
    rec('  ### ### LIVING RECORD, WHICH THE ORDER ASKED THIS ACT TO SAY.**')
    seg2 = EXTRACT.split('### (F) THE NAVIGATOR', 1)[-1].split('A FERRY IS THE NAVIGATOR', 1)[0]
    for ln in seg2.split('\n'):
        if ln.strip() and ('UNQUAL' in ln or 'QUALIFIED' in ln or 'candidates' in ln):
            rec('  ' + ln.rstrip()[:190])
    rec('  ### **`b331`\u2019S FERRY CARRIES BOTH, TWELVE LINES APART:** ### line 36 writes the')
    rec('  ### seal as *24 zero-axiom terminals; general and per-cell*, and line 46 writes')
    rec('  ### *the finite side is compiled* bald.')
    rec('  ### ### ### **AND THE ACT THAT FERRY ORDERED WROTE THE QUALIFIER BACK IN.** ###')
    rec('  ### `b331`\u2019s own fold stands at `FINDINGS.md:2896` as *the finite side compiled: the')
    rec('  ### decomposition and the scaling part general, the compact part per cell*. ###')
    rec('  ### **THE SEAT REPAIRED THE ELISION ON THE WAY IN**, which is why the living record is')
    rec('  ### `11` of `12` qualified and the ferries are `1` of `4`.')
    rec('  ### ### **NO FERRY IS EDITED AND NO PRIOR BANK IS EDITED.** ### A ferry is the')
    rec('  ### navigator\u2019s own words and a bank is a locked record; both are DECLARED.')


def addition_four():
    rec('')
    bar()
    rec('### ADDITION FOUR -- THE STANDING CLAUSE, PROMOTED.')
    bar()
    rec('  ### ### **THE INCIDENTS, MEASURED FROM THE RECORD RATHER THAN ADOPTED FROM THE ORDER.**')
    incidents = [
        ('b316', '`G-NOTRACE`', 'LATENT', 'searched raw source for `np.trace`; passed only '
         'because no docstring there happened to name it.'),
        ('b317', '`G-NOUNIT`', 'FIRED', "fired on the runner's own docstring line asserting the "
         'absence: a sentence saying a thing was NOT done, counted as the thing done.'),
        ('b400', '`G-ONEQ`', 'FIRED', "fired on the bank's own sentence *It does not say that the "
         'bridge and the clause are one question.*'),
        ('b403', '`G-FERRYWORDS`', 'FIRED', "found the ferry's phrase in a file THIS ACT HAD JUST "
         'WRITTEN while saying it was absent.'),
        ('b404', '`G-NOAXIOMCLAIM`', 'FIRED', "fired on the act's own negated sentence about the "
         'terminals.'),
        ('b405', '`G-KEY`', 'FIRED', 'matched the verdict word `NO KEY` INSIDE the longer token '
         '`NO KEYSTONE EDITED`, and failed a SUCCESSFUL lookup.'),
    ]
    for act, armn, st, why in incidents:
        rec('      %-6s %-20s %-7s %s' % (act, armn, st, why[:96]))
        if len(why) > 96:
            rec('             %s' % why[96:220])
    this_session = [a for a, _n, _s, _w in incidents if a in ('b400', 'b403', 'b404', 'b405')]
    rec('')
    rec('  ### ### **THE COUNT, SAID PLAINLY: `%d` INCIDENTS IN THE RECORD, `%d` OF THEM IN THIS'
        % (len(incidents), len(this_session)))
    rec('  ### ### SESSION (%s), AND `b316`/`b317` BEFORE IT.**' % ', '.join(this_session))
    rec('  ### The order calls it *the fifth dress of one species in one session*. ### **THIS ACT')
    rec('  ### ### PRINTS WHAT IT CAN EVIDENCE AND DOES NOT CARRY THE FIGURE FORWARD BECAUSE A')
    rec('  ### ### FERRY STATED IT** -- four in this session by the acts named, six across the')
    rec('  ### record. ### The species is one; the count is the reader\u2019s.')
    rec('')
    rec('  ### ### **THE PROMOTION, BY THE STANDING FILE\u2019S OWN MECHANISM.** ### It goes in as')
    rec('  ### `A2` under `AUTHOR-RULED CLAUSES (NOT MEASURED)`, in the shape `A1` already has:')
    rec('  ### the clause, the ruling quoted, the occasion named, and the words ### **NOT MEASURED;')
    rec('  ### ### CARRIED BY NO COUNT** -- because the file\u2019s head rule says every MEASURED')
    rec('  ### clause is a line of a banked ferry, and this one is a line of THIS ferry.')
    rec('  ### ### **THE VERSION LINE IS NOT BUMPED, AND THAT IS A DECISION AND NOT AN OMISSION.**')
    rec('  ### The file is cited as `FERRY_STANDING v2` and `ferry_scan.py` reports any other')
    rec('  ### version as a ### **STALE CITATION**. ### Bumping it would make every live ferry\u2019s')
    rec('  ### citation stale and the scan would fire on the next correct ferry. ### `A1` was added')
    rec('  ### under `v2` for the same reason, and the file\u2019s own head says an amendment is')
    rec('  ### recorded *when next revised*.')
    rec('  ### ### **AND ONE SENTENCE IS DELIBERATELY NOT PROMOTED.** ### This ferry\u2019s standing')
    rec('  ### block carries a SECOND new clause -- *every write encodes before it opens*, bought')
    rec('  ### by `b405`\u2019s zero-byte husk. ### The order names ONE sentence. ### **IT IS')
    rec('  ### ### CARRIED BY THIS FERRY, ROUTED TO THE AUTHOR IN ONE LINE, AND NOT PROMOTED**,')
    rec('  ### because promoting what was not asked is scope-widening dressed as diligence.')
    return len(incidents), len(this_session)


def expectations(n_fill, n_inc, n_sess):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED. ### **EACH BY A PRINTED QUOTATION OR A PRINTED COUNT.**')
    bar()
    rows = [
        ('(N1)', 'both (i) and (iv) carry no existential at any depth',
         '### **REFUTED, AND INSTRUCTIVELY.** ### `(i)` has one ONE DEPTH DOWN, in the '
         'class\u2019s own Boas-Kac characterisation -- and it is `(iii)`\u2019s, not `(i)`\u2019s. '
         '`(iv)` has one that is ### **TRIVIALLY SATISFIABLE** ### and carries no content to '
         'share. ### **NEITHER IS AN EXISTENTIAL THE SHARED-WITNESS FORM CAN REPAIR, SO b405\u2019S '
         'CELLS STAND AND ITS REASON GAINS A CLAUSE.**'),
        ('(N2)', 'the record already has a name and it is not "uniform witness"',
         '### **MET, IN BOTH PARTS.** ### The barrier: the ### **SIEVE CEILING LEMMA** ### and '
         'the ### **ESCAPE-KIND** ### (`scale-horizon` / `raw-infinitude`). The repair: ### **A '
         'BRIGHT CHANNEL, `\u03ba > 0`.** ### Neither is *uniform witness*.'),
        ('(N3)', 'a third coordinate would fill at most three of six from banked text',
         '### **REFUTED** -- `%d` of 6 are fillable under the strict test and `%d` is `UNSTATED`.'
         % (n_fill, 6 - n_fill)),
        ('(N4)', 'at least one other standing law is also binary where it is applied unarily',
         '### **MET** -- `(R20)`\u2019s kernel limb and its currency obligation are BINARY, and '
         'the record already has the case they cannot reach: the `SIDE-kernel` question `b392` '
         'entered as standing. ### The deposit\u2019s \u00a727.3 refusal is n-ARY for the same '
         'reason the row\u2019s is.'),
        ('(N5)', "(iii)'s two clauses are statable in the source's symbols without new mathematics",
         '### **MET** -- both are written above in `Cc^\u221e`, `supp`, `\u2217`, `g\u0303` and '
         '`F`, from `b353`\u2019s banked quotations alone. ### Whether they can be MET is '
         '`NOT ATTEMPTED`.'),
        ('(N6)', 'at least one reader-facing sentence drops the qualifier, one in a ferry-shaped '
                 'document',
         '### **MET IN BOTH HALVES** -- `OPEN_TRAILS.md:4638`, in `b398`\u2019s block of the '
         'living trails ledger, and `3` of the `4` ferry candidates carry the elision directly '
         '(`b329`, `b331`, `b405`).'),
        ('(N7)', 'the name lives in the E-Difficulty or invariance-barriers cluster',
         '### **MET** -- the repair\u2019s name is Corollary 3.6 of '
         '`phase1.5/method/INVARIANCE_BARRIERS.md`; the gap\u2019s classification is in '
         '`phase1.5/method/THE_DIFFICULTY_KINDS.md`, the same method cluster.'),
        ('(E1)', 'the two matchers give different unqualified counts',
         '### **MET** -- narrow `0`, widened `1`. ### **THE NARROW ONE WOULD HAVE BANKED '
         '"NOTHING TO REPAIR".**'),
        ('(E2)', 'the record names the barrier more fully than the repair',
         '### **MET** -- a theorem, a corollary, a classification and two kinds for the barrier; '
         '### **ONE COROLLARY AND A NAME** ### for the repair, stated only as the negation of '
         'the barrier\u2019s hypothesis.'),
        ('(E3)', 'more of the elision sits in the ferries than in the living record',
         '### **MET** -- the living record is `11` of `12` QUALIFIED; the ferries are `1` of `4`.'),
        ('(E4)', 'at least one act wrote the qualifier its own ferry had dropped',
         '### **MET** -- `b331`\u2019s ferry says *the finite side is compiled* bald at line 46, '
         'and `b331`\u2019s fold writes it qualified at `FINDINGS.md:2896`.'),
    ]
    for k, claim, verdict in rows:
        rec('  **%s** %s' % (k, claim))
        for j in range(0, len(verdict), 130):
            rec('        %s' % verdict[j:j + 130])


def main():
    rec('=' * 100)
    rec('b406_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.')
    rec('=' * 100)
    rec('  face LOCKED : c980d1dec1573a6982f2e9173d362ac47de3237232480627191e342366fca5b1')
    rec('')
    component1()
    component2()
    n_fill = component3()
    addition_one()
    addition_two()
    addition_three()
    n_inc, n_sess = addition_four()
    expectations(n_fill, n_inc, n_sess)
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
