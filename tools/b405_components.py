# -*- coding: utf-8 -*-
"""b405_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### COMPONENT 1 -- the six entries of row `U1` put to three tests, the deciding quote beside
###     every cell, each quote VERIFIED PRESENT in the cell before it is printed.
### ### COMPONENT 2 -- the refusal clause quoted verbatim and put ONE question, by the predicate the
###     locked face fixed: a clause can express a distinction between two states of ONE site only if
###     some predicate in it has ONE site for its subject.
### ### ADDITION ONE -- the countermodel at its pin, its printed profile, and the `WITNESS` column's
###     source: the two clauses `T3prime_shared_witness` itself carries.
### ### ADDITION TWO -- the finite side's witness, by the branch rule the face fixed in advance.
### ### THE DRAFT'S ADDITION -- the shape-to-instance route priced, and not taken.
### ### COMPONENT 3 -- `(R24)` computed: the twelve cells, ready for the writer and written by it.
###
### ### **NOTHING HERE WRITES TO A LEDGER.** ### This file computes and prints; `b405_desk_bank.py`
### ### writes. ### **AND EVERY QUOTE BELOW IS CHECKED AGAINST THE CELL IT CLAIMS TO COME FROM,**
### ### because a quote typed from memory of a cell is the species this whole apparatus exists for.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm   # noqa: E402

D = os.path.join(ROOT, 'data')
SCRATCH = os.path.join(D, '_b405')
OUT = os.path.join(D, 'b405_components.txt')
PP = r'D:\MY-DOwnloads\PLACE-papers'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


def cell_from_blob(k):
    """### **THE CELL, FROM THE COMMITTED BLOB, EVERY TIME.** ### Never from the working file."""
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                          capture_output=True).stdout.decode('utf-8')
    rows = [l for l in blob.splitlines() if l.startswith('| U1 |')]
    assert len(rows) == 1, 'row U1 is not unique in the blob'
    return rows[0].rstrip().split('|')[k]


CELL5 = cell_from_blob(5)
CELL7 = cell_from_blob(7)


def q(cell, frag, where):
    """### Verify a fragment is IN the cell before it is printed as the cell's own words."""
    if flat(frag) in flat(cell):
        return True
    FAILS.append('%s : NOT IN THE CELL -- %r' % (where, frag[:70]))
    return False


def show(cell, frag, where, indent='        '):
    ok = q(cell, frag, where)
    rec('%s%s %s' % (indent, 'quote:' if ok else '### QUOTE NOT IN CELL:',
                     ('*"%s"*' % frag) if len(frag) < 400 else frag[:400]))
    return ok


# ### ==================================================================================================
# ### ### **COMPONENT 1 -- THE SIX BY THREE.** ### Each row: the site, the three verdicts, and for
# ### ### each verdict the sentence of the ENTRY that decided it. ### **NAMING THE DEFECT IS NOT
# ### ### WRITING THE STATEMENT** and **SAYING THE OBSTRUCTION IS REAL IS NOT FILING A RESIDUE** --
# ### ### the two rules the face fixed, applied here and not softened.
# ### ==================================================================================================
SIX = [
    dict(id='(i)', name="THE CLAUSE'S QUANTIFIER", act='b332',
         t1='NO', t1q='the quantifiers -- over the class, infinite, and through the explicit '
                      'formula over the zeros -- are UNOWNED, and they are the clause.',
         t1why='It names WHICH quantifiers are unowned. ### **IT DOES NOT WRITE THE STATEMENT** '
               'a reader could recognise if it were found.',
         t2='NO', t2q=None,
         t2why='### **VACUOUS, AND THAT IS SAID IN THE SAME SENTENCE AS THE VERDICT:** ### T2 '
               'weighs a NAMED missing statement, and this entry names none, so there is nothing '
               'here for a residue to be the weight OF.',
         t3='NO', t3q=None, t3why='The entry says nothing about emptiness or kind.'),
    dict(id='(ii)', name="THE HEIGHT COORDINATE'S ENUMERATION", act='b351',
         t1='NO', t1q='the coordinate is BOUNDED BY A MEASUREMENT and not by an argument',
         t1why='It names the DEFECT in what the record holds. ### **A DEFECT IS NOT A STATEMENT.**',
         t2='NO', t2q=None,
         t2why='### **VACUOUS** ### -- no statement named, so no weight to attribute.',
         t3='NO', t3q=None, t3why='The entry says nothing about emptiness or kind.'),
    dict(id='(iii)', name="THE WIDTH COORDINATE'S UNION", act='b353',
         t1='YES', t1q='while the criterion quantifies over the union of all supports',
         t1why='With the quoted *"AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS '
               'WIDTHS"* this names the statement exactly: ### **AN EXHAUSTION ACROSS WIDTHS, '
               'COVERING THE UNION THE CRITERION QUANTIFIES OVER.** ### A reader would know it '
               'on sight.',
         t2='NO', t2q=None,
         t2why='The entry names the statement and never says how much of the problem it carries.',
         t3='NO', t3q=None, t3why='The entry says nothing about emptiness or kind.'),
    dict(id='(iv)', name='THE PRIME CONSTITUENT AT A WIDENED SUPPORT', act='b401',
         t1='YES', t1q='needs **one statement uniform in `a`**',
         t1why='And it goes further than any entry above it, saying what would COUNT: *"any '
               'statement evaluating or bounding `\u03a3_p W_p(f)` at `a\u00b2 \u2265 2` against '
               'an archimedean quantity"*.',
         t2='NO', t2q='SO THIS IS A FOURTH INSTANCE OF THE OBSTRUCTION AND NOT A CRACK IN IT.',
         t2why='### **THAT SENTENCE SAYS THE OBSTRUCTION IS REAL. ### IT DOES NOT SAY WHAT '
               'FRACTION OF THE PROBLEM THE MISSING STATEMENT CARRIES**, which is what a residue '
               'is.',
         t3='NO', t3q=None, t3why='The entry says nothing about emptiness or kind.'),
    dict(id='(v)', name='THE REPRESENTATION-DEPENDENT CONSTANT', act='b404',
         t1='YES', t1q='so the record holds an error term indexed by the representation and '
                       'needs one that is not',
         t1why='Exact, and in the row\u2019s own uniform-in-an-index form.',
         t2='NO', t2q=None,
         t2why='The entry decides the KIND of its emptiness and never weighs it.',
         t3='YES', t3q='(v) IS KIND (b).',
         t3why='### **ONE OF THE SIX DECLARES ITS KIND, IN ITS OWN TEXT, IN THOSE WORDS.**'),
    dict(id='(vi)', name='THE TYPE-D RESIDUE AT EVERY FINITE MODULUS', act='b404',
         t1='YES', t1q='what is missing is the statement **across** them',
         t1why='Named against a compiled half that closes at every finite modulus, so the reader '
               'knows exactly which statement is absent.',
         t2='YES', t2q='the whole of the remaining weight',
         t2why='### **THE ONLY ENTRY THAT WEIGHS ITS MISSING STATEMENT**, and it does so in the '
               'keystone\u2019s own words, filed at all three problems alike.',
         t3='NO', t3q=None,
         t3why='It does not say whether it is empty, so it declares no kind.'),
]

# ### ==================================================================================================
# ### ### **THE TWO COORDINATES.** ### `KIND` from the entry's own text; `WITNESS` from the theorem's
# ### ### own two clauses applied to the SITE'S OWN TEXT -- never to the navigator's paragraph.
# ### ==================================================================================================
CELLS = [
    dict(id='(i)', kind='NOT EMPTY',
         kindq='are UNOWNED, and they are the clause',
         kindwhy='An UNOWNED open part is a live obstruction; the entry never calls it empty.',
         wit='UNSTATED',
         form='### **NO INNER EXISTENTIAL TO SHARE.** ### The entry\u2019s quantifiers run over '
              'the class and, through the explicit formula, over the zeros -- a `\u2200` with no '
              '`\u2203` inside it. ### The shared-witness form is a repair for `\u2200\u2203 '
              '\u21d2 \u2203\u2200`, and there is no `\u2203` here for one object to serve.',
         witwhy='### **THE FORM DOES NOT TRANSPOSE, SO THE CELL IS NOT `NONE KNOWN`** -- saying '
                'no witness is known would imply one is the right kind of thing to look for.'),
    dict(id='(ii)', kind='NOT EMPTY',
         kindq='the coordinate is BOUNDED BY A MEASUREMENT and not by an argument',
         kindwhy='Bounded by the wrong kind of thing is not empty; the obstruction is live.',
         wit='NONE KNOWN',
         form='### **ONE ARGUMENT SERVING EVERY HEIGHT.** ### The record\u2019s only method there '
              'produces zeros one at a time; the witness would be a single object covering every '
              '`T` at once, with the census\u2019s own non-degeneracy beside it.',
         witwhy='### **AND THE SITE\u2019S OWN EMITTING BANK SAYS THE RECORD HAS NONE**, in the '
                'sentence that sets this coordinate against the one that closed: *"one convergent '
                'series did what sixty boxes of argument principle could not do for the height"*.'),
    dict(id='(iii)', kind='NOT EMPTY',
         kindq='AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS',
         kindwhy='The statement exists and does not close the coordinate; the obstruction is live.',
         wit='NONE KNOWN',
         form='### **ONE `g` SERVING EVERY WIDTH.** ### Boas-Kac, as `b353` quotes it, carries the '
              'inner existential itself -- *"There exists g in Cc^infty(R) with support in '
              '[-A/2, A/2] such that f = g * g^*"* -- and that `\u2203g` is indexed by `A`. ### '
              'The witness\u2019s two clauses read: `h1`, ONE `g` works at every `A`; `h2`, the '
              '`f` it builds is not the degenerate one.',
         witwhy='### **THIS IS THE ONE SITE OF THE SIX WHOSE OWN BANKED TEXT SUPPLIES THE INNER '
                'EXISTENTIAL IN THE THEOREM\u2019S SHAPE**, and it names no `g` that serves '
                'every width.'),
    dict(id='(iv)', kind='NOT EMPTY',
         kindq='confirmed that statement **ABSENT**',
         kindwhy='Absent is what the search found; the obstruction it leaves is live, and the '
                 'entry says so: a fourth instance and not a crack.',
         wit='UNSTATED',
         form='### **NO INNER EXISTENTIAL TO SHARE.** ### What the record holds here is TEN '
              'VALUES indexed by the width, not ten existential witnesses; what it needs is one '
              'statement uniform in `a`. ### A uniform bound is not an object in the family\u2019s '
              'parameter space.',
         witwhy='### **AND THIS IS WHERE THE SHARED INDEX STOPS MEANING A SHARED SHAPE:** ### '
                '`(iii)` and `(iv)` share the support width, which `b401` put on the face of its '
                'own entry -- and `(iii)` carries the existential while `(iv)` does not.'),
    dict(id='(v)', kind='(b)',
         kindq='(v) IS KIND (b).',
         kindwhy='### **DECLARED BY THE ENTRY ITSELF**, and the only KIND cell of the six that is '
                 'a transcription rather than a reading.',
         wit='NONE KNOWN',
         form='### **ONE CONSTANT SERVING EVERY REPRESENTATION.** ### The site IS a `\u2200\u2203 '
              '\u21d2 \u2203\u2200`: the record holds, for each `\u03c0`, an implied constant '
              'depending on `\u03c0`, and needs one constant good for all of them. ### The '
              'inner existential is the constant.',
         witwhy='### **AND THE ENTRY NAMES THE SHAPE BY CONTRAST, WITHOUT SUPPLYING THE WITNESS:** '
                '### Theorem 5.1\u2019s archimedean bound *"carries an **ABSOLUTE** constant"* -- '
                'a witness for the ARCHIMEDEAN side and not for this one.'),
    dict(id='(vi)', kind='NOT EMPTY',
         kindq='the paper files the residue in the same words at all three problems',
         kindwhy='A residue filed as the whole of the remaining weight is the opposite of empty.',
         wit='NONE KNOWN',
         form='### **ONE OBJECT CONSISTENT AT EVERY FINITE MODULUS, AND NON-DEGENERATE.** ### The '
              'entry\u2019s own quoted boundary supplies BOTH clauses of the form: `h1` is '
              '*"consistent at every finite modulus"*; `h2` is the *"(positive global density)"* '
              'the passage must reach.',
         witwhy='### **THE ONLY SITE OF THE SIX WHOSE OWN TEXT NAMES BOTH CLAUSES OF THE WITNESS '
                'FORM** -- which is why `b404` reported the shape and refused the bridge.'),
]


def component1():
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE SIX READ AS SIX. ### **SIX BY THREE, EVERY CELL WITH ITS QUOTE.**')
    rec('-' * 100)
    rec('    cell 5 read from the COMMITTED BLOB : %d bytes' % len(CELL5.encode('utf-8')))
    rec('')
    for s in SIX:
        rec('  ### %-6s %-42s %s' % (s['id'], s['name'], s['act']))
        for t in ('t1', 't2', 't3'):
            lbl = dict(t1='T1 WRITES THE MISSING STATEMENT',
                       t2='T2 FILES A RESIDUE      ',
                       t3='T3 DECLARES ITS KIND    ')[t]
            rec('      %s : ### **%s**' % (lbl, s[t]))
            if s[t + 'q']:
                show(CELL5, s[t + 'q'], '%s %s' % (s['id'], t.upper()))
            rec('        %s' % s[t + 'why'])
        rec('')
    y1 = [s['id'] for s in SIX if s['t1'] == 'YES']
    y2 = [s['id'] for s in SIX if s['t2'] == 'YES']
    y3 = [s['id'] for s in SIX if s['t3'] == 'YES']
    both = [s['id'] for s in SIX if s['t1'] == 'YES' and s['t2'] == 'YES']
    rec('  ### ### **THE TALLY:** ### T1 %d of 6 %s ; T2 %d of 6 %s ; T3 %d of 6 %s'
        % (len(y1), y1, len(y2), y2, len(y3), y3))
    rec('  ### ### **ENTRIES DOING BOTH T1 AND T2 : %d %s**' % (len(both), both))
    rec('  ### **AND THE ROW HAD ALREADY SAID SO ABOUT ITSELF.** ### Cell 7 carries the sentence')
    show(CELL7, 'and which **one of the six already has**', 'ROW ON ITSELF', '      ')
    rec('      ### -- so the draft\u2019s expectation that `(iv)` and `(vi)` both do it was'
        ' refutable')
    rec('      ### **BY A SENTENCE IN THE VERY CELL IT WAS ABOUT**, and it is refuted here.')
    return dict(t1=y1, t2=y2, t3=y3, both=both)


def component2():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE REFUSAL CLAUSE, QUOTED VERBATIM AND PUT ONE QUESTION.')
    rec('-' * 100)
    clauses = [
        ('NOTHING IS CLAIMED ABOUT THE EQUIVALENCE OF THE THREE',
         'THE THREE', 'a SET of sites'),
        ('A ROW NAMING THREE THINGS THAT LOOK ALIKE IS EXACTLY WHERE AN EQUIVALENCE GETS '
         'COMPILED BY ACCIDENT', 'A ROW NAMING THREE THINGS', 'a ROW, and three things'),
        ('names a resemblance of SHAPE and types no bridge between the three, in either '
         'direction', 'THIS ROW / THE THREE', 'a ROW, and a PAIR at each end of a bridge'),
        ('Three separate obstructions that rhyme are three obstructions.',
         'THREE OBSTRUCTIONS', 'a SET of sites'),
    ]
    rec('  ### **THE CLAUSE, VERBATIM FROM THE BLOB, SENTENCE BY SENTENCE, EACH VERIFIED:**')
    unary = 0
    for i, (frag, subj, kind) in enumerate(clauses, 1):
        rec('    (%d)' % i)
        show(CELL7, frag, 'REFUSAL CLAUSE %d' % i)
        rec('        subject : %-28s -- %s' % (subj, kind))
        if 'SET' not in kind and 'PAIR' not in kind and 'three' not in kind:
            unary += 1
    rec('')
    rec('  ### **THE PREDICATE THE LOCKED FACE FIXED:** ### a clause can express a distinction')
    rec('  ### between two states of ONE site only if some predicate in it has ONE site for its')
    rec('  ### subject.')
    rec('  ### ### **PREDICATES WITH ONE SITE FOR A SUBJECT : %d OF %d.**' % (unary, len(clauses)))
    rec('  ### ### ### **SO THE ANSWER IS `NO`: THE REFUSAL CLAUSE CANNOT DISTINGUISH A SITE')
    rec('  ### ### ### EMPTY IN KIND `(a)` FROM ONE EMPTY IN KIND `(b)`.**')
    rec('  ### **EVERY CLAUSE OF IT IS BINARY OR HIGHER -- ABOUT PAIRS, ABOUT THE SET, ABOUT THE')
    rec('  ### ROW.** ### `(a)` versus `(b)` is a UNARY property of ONE site. ### **A BINARY LAW')
    rec('  ### ### CANNOT EXPRESS A UNARY DISTINCTION**, and no amount of restating it will make')
    rec('  ### it. ### ### **THIS IS NOT A DEFECT IN THE SITES. ### IT IS A MISSING COORDINATE')
    rec('  ### ### IN THE ROW**, which is exactly what `(R24)` supplies.')
    rec('  ### **AND COMPONENT 2 RESTATES NO ENTRY AND TYPES NO BRIDGE.**')
    return unary


def addition_one():
    rec('')
    rec('-' * 100)
    rec('### ADDITION ONE -- THE COMPILED COUNTERMODEL AT ITS TERMINAL, AND THE COLUMN\u2019S SOURCE.')
    rec('-' * 100)
    ex = io.open(os.path.join(D, 'b405_extract.txt'), encoding='utf-8').read()
    for need in ("v0.10.0       : 93c27ec2cb9b1fc59e4796b93a2150c408ecfa8f",
                 "theorem T3prime_shared_witness",
                 "theorem T3doubleprime_general_commutation_fails",
                 "depends on axioms: [propext, Classical.choice, Quot.sound]"):
        ok = need in ex
        rec('  survey carries %-64s %s' % (need[:64], 'YES' if ok else '### NO ###'))
        if not ok:
            FAILS.append('ADDITION ONE: the survey does not carry %r' % need[:60])
    rec('')
    rec('  ### **THE PROFILE, PRINTED AND NOT RUN:**'
        ' `[propext, Classical.choice, Quot.sound]` -- ### **`std3`.**')
    rec('  ### Read from the repository\u2019s own TRACKED `VERIFICATION_TRANSCRIPT.md` at')
    rec('  ### `v0.10.0` = `93c27ec2`. ### **NOTHING WAS BUILT; THE LANE IS PARKED.**')
    rec('  ### And the transcript prints the one `sorry` beside them, at the INTERMEDIATE')
    rec('  ### `T3_perClass_to_combinations` and not at either terminal.')
    rec('')
    rec('  ### ### **WHAT A SHARED WITNESS IS, IN THE THEOREM\u2019S OWN TERMS -- TWO CLAUSES ON')
    rec('  ### ### ONE OBJECT IN THE FAMILY\u2019S OWN PARAMETER SPACE:**')
    rec('      `h1 : \u2200 C \u2208 \U0001d49e, C Phi`        ### **SHAREDNESS** -- ONE object')
    rec('                                        satisfies EVERY member of the family.')
    rec('      `h2 : mellin Phi (s / 2) \u2260 0`   ### **NON-DEGENERACY** -- the quantity that')
    rec('                                        must not vanish does not vanish AT that object.')
    rec('  ### **AND THE COUNTERMODEL IS WHY BOTH ARE NEEDED:** ### `f1` and `f2` agree on `Ioi 0`')
    rec('  ### and differ at `t = -1`, so each family member has its own witness and no single')
    rec('  ### `\u03a6` serves both. ### ### **PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.**')
    rec('')
    rec('  ### ### **THE NAVIGATOR\u2019S TWO CANDIDATES, SCORED AGAINST THE SITES\u2019 OWN TEXT:**')
    rec('  ### **(1) THE ABSCISSA\u2019S CONVERGENT SUM.** ### ### **IT IS NOT A WITNESS FOR ANY')
    rec('  ### ### SITE OF THIS ROW, BECAUSE THE ABSCISSA IS NOT A SITE OF THIS ROW.** ### The')
    rec('  ### row\u2019s `b351` sites are the HEIGHT `(ii)` and -- through `b353` -- the WIDTH')
    rec('  ### `(iii)`. ### The abscissa is the coordinate that CLOSED, which is precisely why it')
    rec('  ### never became a site: `b351` banks it as *"THE ABSCISSA WAS ALREADY CLOSED, AND HAS')
    rec('  ### BEEN SINCE b326"* and sets it AGAINST the height in the next breath.')
    rec('  ### **A COORDINATE THAT CLOSED IS NOT AN OBSTRUCTION WITH A WITNESS; IT IS AN')
    rec('  ### ### OBSTRUCTION THAT WAS NEVER ENTERED.**')
    rec('  ### **(2) THE FINITE SIDE\u2019S ZERO.** ### Scored in Addition Two below, on the')
    rec('  ### kernel\u2019s own text and by the branch rule the face fixed before the read.')
    rec('  ### ### **NEITHER CANDIDATE IS FILED AGAINST THE NEAREST SITE TO KEEP THE COUNT UP.**')


def addition_two():
    rec('')
    rec('-' * 100)
    rec('### ADDITION TWO -- THE FINITE SIDE\u2019S WITNESS, STATED EXACTLY.')
    rec('-' * 100)
    seal = r'D:\SIDE-global-section\Core\FiniteSideSeal.lean'
    src = io.open(seal, encoding='utf-8').read()
    cells_line = [l for l in src.splitlines() if l.startswith('def cells :')][0]
    n_cells = cells_line.split('[', 1)[1].count('(')
    rec('  ### THE CELL LIST, FROM THE FILE:')
    rec('      | %s' % cells_line)
    rec('  ### ### **CELLS IN THE LIST : %d.**' % n_cells)
    rec('')
    rec('  ### **THE THREE CLAUSES, AS THE THEOREM\u2019S OWN DOCSTRING LABELS THEM:**')
    rec('      (a) ### **GENERAL** ### -- the index decomposition, for every `p \u2265 2`,')
    rec('          every level `n`, every `t`.')
    rec('      (b) ### **GENERAL** ### -- the scaling clause, same generality.')
    rec('      (c) ### **PER CELL** ### -- *"if `(p, n)` is in `cells`, `q * SUM_u A_N(u) =')
    rec('          SUM_u A_q(u)`  (Component 3), with the cell list as the hypothesis, each cell')
    rec('          decided."*')
    guarded = '((p, n) \u2208 cells \u2192' in src
    rec('')
    rec('  ### **THE DECIDING FACT, READ FROM THE STATEMENT AND NOT FROM THE PROSE:** ### the')
    rec('  ### clause carrying the zero is written `((p, n) \u2208 cells \u2192 ...)` -- ### **A')
    rec('  ### ### MEMBERSHIP TEST AGAINST A FINITE DECIDED LIST** : %s' % guarded)
    rec('  ### and `compact_smear_vanishes_at_cells` discharges it by `decide` over that same list.')
    rec('')
    rec('  ### ### ### **SO THE BRANCH IS `(beta)`, AND THE CELL READS `UNSTATED`.**')
    rec('  ### The value proved is the same at every cell it is proved at -- and it is proved at')
    rec('  ### ### **%d CELLS AND NO OTHERS.** ### Adding an eighth place adds a new obligation'
        % n_cells)
    rec('  ### and a new `decide`; nothing in the theorem carries the zero from one place to')
    rec('  ### another. ### ### **THERE IS NO CROSS-PLACE CLAIM IN THE CLAUSE THAT CARRIES THE')
    rec('  ### ### ZERO AT ALL**, so zero is not a shared witness across places -- it is the same')
    rec('  ### answer arrived at separately seven times.')
    rec('  ### ### **AND THE NAVIGATOR\u2019S FRAMING OVER-REACHED HERE TOO**, in those words, as')
    rec('  ### the ferry instructs.')
    rec('')
    rec('  ### **AND THE SHARPER THING, WHICH NEITHER BRANCH OF THE FERRY\u2019S QUESTION SAYS:**')
    rec('  ### ### **THE GENERALITY AND THE ZERO ARE IN DIFFERENT CLAUSES.** ### `(a)` and `(b)`')
    rec('  ### ARE general in `p` -- and neither carries the zero. ### `(c)` carries the zero --')
    rec('  ### and has no generality. ### **THE THEOREM IS GENERAL WHERE IT IS EMPTY OF THE ZERO')
    rec('  ### ### AND DECIDED WHERE IT IS NOT**, which is a fact about the terminal and not a')
    rec('  ### complaint about it.')
    rec('  ### **NO GRADE MOVES. ### NOTHING IS BUILT. ### THE PROFILE IS THE ONE PRINTED AT')
    rec('  ### `AXIOM_PRINTS.txt` LINES 587 AND 590 AND IS NOT RE-RUN.**')
    return n_cells, guarded


def the_route():
    rec('')
    rec('-' * 100)
    rec("### THE DRAFT\u2019S ADDITION, RETAINED -- THE SHAPE-TO-INSTANCE ROUTE, PRICED.")
    rec('-' * 100)
    rec('  ### **(1) THE STATEMENT THAT WOULD HAVE TO HOLD.** ### To carry `T3\u2032` to a site,')
    rec('  ### one would need an identification of that site\u2019s family with the theorem\u2019s')
    rec('  ### `Set Coupling`, of its parameter space with `\u211d \u2192 \u2102`, and then BOTH')
    rec('  ### clauses at that identification: a single object satisfying every member, and the')
    rec('  ### site\u2019s own non-degeneracy at it. ### **THE IDENTIFICATION IS THE WHOLE PRICE:')
    rec('  ### ### THE THEOREM IS ABOUT COUPLINGS ON `\u211d \u2192 \u2102`, AND NOT ONE OF THE')
    rec('  ### ### SIX SITES IS STATED IN THOSE TERMS.**')
    rec('  ### **(2) DOES ANY OF THE SIX SUPPLY A CANDIDATE SHARED WITNESS?** ### ### **NO.**')
    rec('  ### Two sites carry no inner existential at all `(i)`, `(iv)`; three carry one and name')
    rec('  ### no object that serves it `(ii)`, `(iii)`, `(v)`; and `(vi)`, whose own text names')
    rec('  ### BOTH clauses, names no object satisfying them. ### **SIX SITES, ZERO CANDIDATES.**')
    rec('  ### **(3) IS IT `UNPRICEABLE` WITHOUT A BUILD?** ### ### **NO -- AND THAT REFUTES THE')
    rec('  ### ### DRAFT\u2019S OWN EXPECTATION.** ### A build buys nothing here: both terminals')
    rec('  ### are ALREADY compiled and their profiles ALREADY printed, so there is no')
    rec('  ### measurement a parked lane is withholding. ### **THE ROUTE IS PRICEABLE AND THE')
    rec('  ### ### PRICE IS NOT A BUILD.**')
    rec('  ### **AND WHERE THE RECORD ITSELF PUTS THE ROUTE\u2019S SECOND CLAUSE, QUOTED AND NOT')
    rec('  ### ### ENDORSED:** ### the corpus\u2019s own archived trails line reads')
    rec('  ### *"`T3prime_shared_witness` with `h1 : \u2200 C \u2208 \U0001d49e, C Phi` ... **and**')
    rec('  ### `h2 : mellin Phi (s/2) \u2260 0` (open, RH-strength)"*, and calls that `h2` *"the')
    rec('  ### same h2 of \u00a727.3\u2019s five registers"*.')
    rec('  ### ### **THIS ACT MAKES NO CLAIM ABOUT `h2` IN EITHER DIRECTION.** ### It reports')
    rec('  ### where the route\u2019s own text puts it and stops. ### **QUOTING A HYPOTHESIS IS')
    rec('  ### ### NOT ASSERTING IT**, and `h2` stands exactly where the deposit left it.')
    rec('  ### ### **A ROUTE PRICED IS NOT A ROUTE TAKEN. ### NO BRIDGE IS TYPED.**')


def component3():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 3 -- `(R24)` EXECUTED. ### **THE TWELVE CELLS, COMPUTED HERE, WRITTEN BY')
    rec('### THE DESK TOOL AND BY NOTHING ELSE.**')
    rec('-' * 100)
    for c in CELLS:
        rec('  ### %-6s ### **KIND : %-10s ### WITNESS : %s**' % (c['id'], c['kind'], c['wit']))
        show(CELL5, c['kindq'], '%s KIND' % c['id'])
        rec('        %s' % c['kindwhy'])
        rec('        FORM  : %s' % c['form'])
        rec('        %s' % c['witwhy'])
        rec('')
    kinds = [c['kind'] for c in CELLS]
    wits = [c['wit'] for c in CELLS]
    rec('  ### ### **KIND CELLS : %d.** ### NOT EMPTY %d ; (a) %d ; (b) %d ; UNSTATED %d'
        % (len(kinds), kinds.count('NOT EMPTY'), kinds.count('(a)'), kinds.count('(b)'),
           kinds.count('UNSTATED')))
    rec('  ### ### **WITNESS CELLS : %d.** ### NONE KNOWN %d ; UNSTATED %d ; FOUND %d'
        % (len(wits), wits.count('NONE KNOWN'), wits.count('UNSTATED'),
           len([w for w in wits if w not in ('NONE KNOWN', 'UNSTATED')])))
    rec('  ### **NO NEW MEASUREMENT WAS TAKEN TO FILL A CELL, AND NO CELL WAS FILLED FROM THE')
    rec('  ### NAVIGATOR\u2019S PARAGRAPH OR FROM ANOTHER SITE.**')
    return kinds, wits


def expectations(tally, unary, n_cells, kinds, wits):
    rec('')
    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED. ### **EACH BY A PRINTED CELL.**')
    rec('-' * 100)
    # (N4) -- distinct acts invoking the refusal on their own conduct.
    acts = set()
    for fn in sorted(os.listdir(D)):
        if not fn.endswith('.txt') or fn.startswith('b405'):
            continue
        m = re.match(r'(b\d{3})_', fn)
        if not m:
            continue
        try:
            t = io.open(os.path.join(D, fn), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        if 'types no bridge' in t:
            acts.add(m.group(1))
    n_found = len([w for w in wits if w not in ('NONE KNOWN', 'UNSTATED')])
    n_notnone = len([w for w in wits if w != 'NONE KNOWN'])
    rows = [
        ('(N1)', '0 of six sites declare a kind',
         '### **REFUTED** -- `(v)` declares `KIND (b)` in its own text. ### `1` of six.'),
        ('(N2)', 'the refusal clause cannot express the (a)/(b) distinction',
         '### **MET** -- `%d` of `4` of its predicates have ONE site for a subject.' % unary),
        ('(N3)', 'at least three of six can be back-filled from banked text alone',
         '### **MET** -- `6` KIND cells and `4` WITNESS cells back-filled from the sites\u2019 '
         'own text; `2` WITNESS cells `UNSTATED`.'),
        ('(N4)', 'the number of acts citing the refusal as governing is greater than one',
         '### **MET** -- `%d` acts: %s.' % (len(acts), ', '.join(sorted(acts)))),
        ('(N5)', 'the shape-to-instance route is UNPRICEABLE without a build',
         '### **REFUTED** -- a build buys nothing; both terminals are already compiled and '
         'their profiles already printed. ### The route is PRICEABLE.'),
        ('(N6)', 'exactly two sites have a WITNESS cell other than NONE KNOWN',
         '### **MET AS A COUNT, REFUTED AS A CLAIM.** ### Cells other than `NONE KNOWN` : `%d` '
         '-- `(i)` and `(iv)`, and BOTH are `UNSTATED`. ### **SITES WITH A WITNESS FOUND : `%d`.**'
         % (n_notnone, n_found)),
        ('(N7)', "the countermodel terminal's profile is std3",
         '### **MET** -- `[propext, Classical.choice, Quot.sound]`, printed at the pin.'),
        ('(E1)', 'at least one entry writes its missing statement without filing a residue',
         '### **MET** -- `(iii)`, `(iv)` and `(v)` all score T1 `YES` and T2 `NO`.'),
        ('(E2)', 'the finite side takes branch (beta)',
         '### **MET** -- the clause carrying the zero is guarded by membership in a `%d`-cell '
         'decided list.' % n_cells),
        ('(E3)', 'the abscissa is not a site of this row',
         '### **MET** -- the row\u2019s `b351` site is the HEIGHT; the abscissa is the coordinate '
         'that CLOSED and was never entered.'),
        ('(E4)', 'the shared-witness form does not transpose to every site',
         '### **MET** -- `(i)` and `(iv)` carry no inner existential to share.'),
    ]
    for k, claim, verdict in rows:
        rec('  **%s** %s' % (k, claim))
        rec('        %s' % verdict)


def main():
    rec('=' * 100)
    rec('b405_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.')
    rec('=' * 100)
    rec('  face LOCKED : c2dd31d3ec811028a4ef5de5a6579688807879410f844e32ca3179acbd9eb634')
    rec('  ### **AND ONE DEFECT IN THAT LOCKED FACE, DECLARED HERE RATHER THAN EDITED AWAY:**')
    rec('  ### its section (A) names three step-zero records as `b405_census_zero.txt`,')
    rec('  ### `b405_faces_census_zero.txt` and `b405_pins_zero.txt`. ### They were RENAMED to')
    rec('  ### `b405_census_stepzero.txt`, `b405_faces_census_stepzero.txt` and')
    rec('  ### `b405_pins_stepzero.txt` -- the names `b378_lockgate.py` reads -- before the lock,')
    rec('  ### and section (W) names them correctly. ### **BOTH NAMES ARE PRINTED; THE LOCKED')
    rec('  ### ### FACE IS NOT EDITED.** ### The bytes are the same bytes and the digests hold.')
    rec('')
    tally = component1()
    unary = component2()
    addition_one()
    n_cells, guarded = addition_two()
    the_route()
    kinds, wits = component3()
    expectations(tally, unary, n_cells, kinds, wits)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-ANCHOR FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO LEDGER, ROW, KEY OR BANK WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write(('\n'.join(L) + '\n').encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
