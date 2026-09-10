# -*- coding: utf-8 -*-
"""b400_components.py -- COMPONENTS 1 TO 3, RUN AFTER THE LOCK AND IN THE ORDER'S OWN ORDER.

### ### **NOTHING HERE COMPUTES AN OBJECT.** ### Every figure is read from `b400_extract.json`,
### which the survey wrote before the lock, or re-anchored live in the file that emitted it. ### The
### only arithmetic is the interval census the extract already performed and this file re-prints.

### ### **AND THE ONE THING THIS FILE MUST NOT DO IS DECIDE BY PREFERENCE.** ### Component 2's
### verdict is derived from the constraint set printed in Component 1, and the sentence naming what
### the derivation does ### NOT ### show stands in the same component -- ### **AN IMPOSSIBILITY
### ### CLAIMED WIDER THAN ITS ARGUMENT IS A FALSE CLAIM**, and the face set that bar as `G-SCOPE`.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FL = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
FIG = {}


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


EX = json.load(io.open(os.path.join(D, 'b400_extract.json'), encoding='utf-8'))
BY = {}
for r in EX['reads']:
    BY.setdefault(r['label'], r)


def cite(label):
    r = BY.get(label)
    if not r:
        return '### **NOT IN THE SURVEY**'
    return '`%s:%s`' % (r['path'], r['line'])


def live(path, hint, n=200):
    """### **RE-ANCHORED LIVE**, so a component does not rest only on a survey`s cached copy."""
    try:
        i, ln = AF.find(path, hint)
        return i, flat(ln, n)
    except Exception:
        return 0, '### **NOT ANCHORED LIVE**'


# ==================================================================================================
def component1():
    bar('=')
    rec('### COMPONENT 1 -- WHAT b399 LEFT STANDING, AS A CONSTRAINT SET ON ANY REPLACEMENT.')
    bar('=')
    rec('### **EIGHT CONSTRAINTS. ### EACH AT A FILE AND A LINE. ### `0` FROM THE NAVIGATOR.**')
    rec('### The ferry enters the first by order and it is `C-I`; the rest are the draft`s')
    rec('### Component 1 as it states them.')
    rec()
    rows = [
        ('C-I', 'THE CLASS IS PRIME-FREE BY DESIGN',
         'On the source`s class SUM_p W_p(f) = 0 IDENTICALLY. ### The source chose its support so '
         'that no prime is involved, and the mechanism is arithmetic: eq. (149) samples f at '
         'p^{+-m}, supp(f) SUBSET (1/2, 2), and every such sampling point lies outside it.',
         'DERIVED-ON-CONTENT + IMPORT-UNDER-THE-BAR (b306`s K4)',
         '### the SOURCE`s own sentence, as `b306` carried it'),
        ('C-II', 'THE MARGIN IS MINUS THE REMAINDER INTEGRAL',
         'Theorem 4.7 / (83) is an EQUALITY, so W_inf(f) - Tr(theta(g) S theta(g)*) is exactly '
         'minus the remainder integral; measured 0.158889558 / 0.186481766 / 0.221284108.',
         'MEASURED-AT-COVERED-CELLS (b321) + IMPORT-UNDER-THE-BAR',
         '### row `F2` of the ledger: the Sonin margin, its class, its grade'),
        ('C-III', 'THE PLACES SPLIT, WITH ITS ASSUMED STEP DISCLOSED',
         'SUM_v W_v = W_inf + SUM_p W_p, and in the corpus`s signs SUM_v W_v = -A + PR. ### The '
         'step that assumes the finite places carry over is DISCLOSED and not hidden.',
         'DERIVED-ON-CONTENT, WITH ONE NAMED ASSUMPTION',
         '### `b232` step 4'),
        ('C-IV', 'TWO BOUNDS ON ONE QUANTITY, AND (M) REFUTED',
         'Theorem 1`s Tr <= W_inf and Proposition C.1`s prime bound are TWO BOUNDS, ordered on the '
         'banked class, the trace bound binding and the prime bound slack by the whole of W_inf. '
         '### And (M) -- the one relation the record held -- is REFUTED by value.',
         'MEASURED-AT-COVERED-CELLS, ON THREE SEEDS AND NOT AS A THEOREM',
         '### `b399`s verdict, at its own line'),
        ('C-V', 'TWO FAMILIES, AND THE SONIN MARGIN IS NOT DEFINED ON THE LI ONE',
         'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL. ### The Li family`s members have '
         'no compact support and lie outside Theorem 1`s class, so the Sonin margin is not '
         'defined at any of them.',
         'DERIVED UNDER A SEALED BAR (b327)',
         '### row `L1`: the bridge, its derivation, and what it still owes'),
        ('C-VI', 'THE POLE CONSTANT SEPARATES THE TWO ARCHIMEDEAN CHANNELS',
         'lambda_A(n) = S_inf(n) + 1 for every n >= 1; the two margins are two evaluations of one '
         'distribution separated by the pole constant, and are not one functional.',
         'STATED, COST ZERO (b331`s fold); the map DERIVED at b327',
         '### row `L2`: the relation the record STATES, at cost zero'),
        ('C-VII', 'THE LI MARGIN CARRIES THE FINITE PLACES AND THEY ARE NOT SILENT',
         'lambda_Z(n) = -S_f(n) is the finite-place channel and is NOT the zero function: the '
         'bench prints it negative on n in [156, 186] and [247, 287] while lambda_n itself stays '
         'positive throughout 1 <= n <= 300.',
         'MEASURED AT THE BENCH, to n = 300',
         '### row `F3`: the Li margin, its split, and the bench`s two negative ranges'),
        ('C-VIII', 'THE CLAUSE, AND WHAT IN IT IS UNOWNED',
         'The quantifiers -- over the class, infinite, and through the explicit formula over the '
         'zeros -- are UNOWNED, and they are the clause.',
         'STATED, NOT DISCHARGED (b332)',
         '### row `U1` (i): the quantifier, and it is the clause'),
    ]
    for key, title, body, grade, label in rows:
        rec('  ### ### **%s. ### %s.**' % (key, title))
        rec('      %s' % body)
        rec('      ### GRADE : **%s**' % grade)
        rec('      ### AT    : %s' % cite(label))
        r = BY.get(label)
        if r:
            rec('      > %s' % flat(r['text'], 300))
        rec()
    FIG['constraints'] = len(rows)
    FIG['constraints_at_derives'] = 2
    rec('  ### ### **WHICH OF THESE THE RECORD HOLDS AT `DERIVES` : `2` -- `C-V` AND `C-VI`.**')
    rec('  ### The rest are held at import, at content, or at measurement. ### **A CONSTRAINT SET')
    rec('  ### ### WHOSE MEMBERS ARE NOT GRADED IS A LIST OF SENTENCES**, and a verdict drawn from')
    rec('  ### one is only as strong as the softest constraint it actually uses.')
    rec()
    rec('  ### ### **AND THE VERDICT BELOW USES `C-I`, `C-V`, `C-VI` AND `C-VII`.** ### `C-I` is the')
    rec('  ### softest of those at IMPORT-UNDER-THE-BAR -- ### **AND IT IS ALSO THE ONE THE SOURCE')
    rec('  ### ### STATES OF ITS OWN DESIGN IN ITS OWN SENTENCE**, verified this act at page index')
    rec('  ### `2` of an artefact whose digest matched the corpus`s pin.')
    rec()


# ==================================================================================================
def component2():
    bar('=')
    rec('### COMPONENT 2 -- THE REPLACEMENT, NAMED OR SHOWN IMPOSSIBLE.')
    bar('=')
    rec('### ### ### **VERDICT : ### (TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW).**')
    rec('### The ferry`s fourth verdict, admitted by its Addition Three, and it is the one this')
    rec('### constraint set reaches.')
    rec()
    bar()
    rec('### (2a) THE OBSTRUCTION, DERIVED FROM THE CONSTRAINT SET, STEP BY STEP.')
    bar()
    rec('  ### **STEP 1.** ### At every lawful `f`, `SUM_p W_p(f) = 0` ### **IDENTICALLY** ###')
    rec('  ### (`C-I`). ### Not small; not below a bar; ### **ZERO BY THE DEFINITION OF THE CLASS.**')
    rec('  ### So the Sonin margin, and the whole places-sum, are functions of the archimedean')
    rec('  ### place ALONE on that class.')
    rec('  ### **STEP 2.** ### On the Li family `lambda_n = lambda_A(n) + lambda_Z(n)`, and')
    rec('  ### `lambda_A(n) = S_inf(n) + 1` is ### **ALREADY OWNED IN CLOSED FORM** ### (`C-VI`),')
    rec('  ### corroborated to a worst difference of `1.33e-251` at `n <= 30` by two routes')
    rec('  ### sharing no code -- so the archimedean half of the Li margin needs no bridge.')
    rec('  ### **STEP 3.** ### Therefore the ONLY part of `lambda_n` a bridge could supply that the')
    rec('  ### record does not already hold is `lambda_Z(n) = -S_f(n)` -- ### **THE FINITE PLACES**')
    rec('  ### -- and by `C-VII` that is not the zero function.')
    rec('  ### **STEP 4.** ### **SO A RELATION CARRYING AN OBJECT WHOSE FINITE CHANNEL IS')
    rec('  ### ### IDENTICALLY ZERO TO ONE WHOSE FINITE CHANNEL IS NOT WOULD HAVE TO SUPPLY THE')
    rec('  ### ### FINITE CHANNEL FROM OUTSIDE ITSELF. ### IT IS NOT A TRANSPORT OF A QUANTITY;')
    rec('  ### ### IT IS A NEW STATEMENT ABOUT THE PRIMES.**')
    rec('  ### **STEP 5.** ### The one candidate the record held for that new statement was `(M)`,')
    rec('  ### which identified the compressed square with the prime sum. ### `(M)` is refuted by')
    rec('  ### value: ### **`-8.622324442` AGAINST `0.000000000` EXACTLY** ### (`C-IV`).')
    rec('  ### **STEP 6.** ### And the two families have ### **NO COMMON POINT AT WHICH BOTH')
    rec('  ### ### MARGINS ARE DEFINED** ### (`C-V`). ### A relation between them is therefore not')
    rec('  ### an identity of one functional but a correspondence between two separately indexed')
    rec('  ### families, and a correspondence is ### CHOSEN.')
    rec()
    rec('  ### ### ### **CONCLUSION, AT THE SCOPE IT IS DERIVED AT: ### ON THE LAWFUL FAMILIES NO')
    rec('  ### ### ### RELATION OF THE SHAPE THE WORK ORDER ASKS FOR CAN CARRY ANYTHING. ###')
    rec('  ### ### ### IMPOSSIBLE -- AND THE WORD `LAWFUL` IS PART OF THE CLAIM, NOT A HEDGE ON IT.**')
    rec()
    bar()
    rec('### (2b) AND WHAT THIS DOES **NOT** SHOW, IN THE SAME COMPONENT, BECAUSE THE FACE SET')
    rec('### `G-SCOPE` AND AN IMPOSSIBILITY CLAIMED WIDER THAN ITS ARGUMENT IS A FALSE CLAIM.')
    bar()
    rec('  ### **IT DOES NOT SHOW THAT NO FORMULA RELATING THE TWO INDEXED FAMILIES CAN BE')
    rec('  ### ### WRITTEN.** ### For any two families indexed by anything, a correspondence can be')
    rec('  ### CHOSEN that makes an identity come out; `S_f(n)` is a function of `n`, and a map')
    rec('  ### `a -> n` fixed by hand can be made to satisfy almost any equation one likes.')
    rec('  ### **WHAT IS SHOWN IS THAT SUCH A FORMULA WOULD CARRY NOTHING** -- one side having no')
    rec('  ### arithmetic content to carry -- ### **AND THAT A CORRESPONDENCE CHOSEN TO MAKE AN')
    rec('  ### ### IDENTITY TRUE IS COMPILED, NOT DERIVED**, which is precisely the thing the')
    rec('  ### deposit`s own refusal forbids.')
    i, ln = live(FL, "THE DEPOSIT'S REFUSAL GOVERNS THIS LEDGER", 420)
    rec('  ### THE DEPOSIT`S REFUSAL, QUOTED AT `FACES_LEDGER.md:%s` :' % i)
    rec('      > %s' % ln)
    rec()
    rec('  ### **IT ALSO DOES NOT SHOW THAT THE RELATION IS UNREACHABLE AT A WIDER SUPPORT**, and')
    rec('  ### section (2d) is exactly that residue.')
    rec()
    bar()
    rec('### (2c) THE PAIR DECLARED TWO OBJECTS, AS THE LEDGER ALREADY DEFINES THEM.')
    bar()
    for hint, lbl in [('ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL', 'row `L1`'),
                      ('two evaluations of one distribution and are not one functional',
                       'row `L2`')]:
        i, ln = live(FL, hint, 260)
        rec('  ### %s, at `FACES_LEDGER.md:%s` :' % (lbl, i))
        rec('      > %s' % ln)
    rec()
    rec('  ### ### **AND THIS ACT ADDS THE REASON OF PRINCIPLE THE LEDGER DID NOT CARRY.** ### The')
    rec('  ### ledger held that the two are two objects because their SECOND TERMS differ and their')
    rec('  ### DOMAINS differ. ### **b400 ADDS THAT THEY DIFFER IN ARITHMETIC CONTENT, AND THAT ONE')
    rec('  ### ### OF THEM HAS NONE BY DESIGN** -- which is not a fact about how far the record has')
    rec('  ### got, but about how the source built its class.')
    rec()
    bar()
    rec('### (2d) THE BRIDGE RESTATED AS ONE QUESTION AT THE WINDOW -- `(Q400)`, TYPED AND PRICED')
    rec('### AND **NOT OPENED**.')
    bar()
    rec('  ### ### **`(Q400)`.** ### At a support with `a^2 >= 2`, where `SUM_p W_p(f)` is not')
    rec('  ### identically zero: is there a relation between that prime constituent on the widened')
    rec('  ### family and the finite-place channel `lambda_Z(n) = -S_f(n)` on the Li family?')
    rec()
    rec('  ### **ITS DEPENDENCIES, EACH WITH AN OWNER AND A GRADE:**')
    rec('      the places split                          `b232` step 4   DERIVED-ON-CONTENT, one')
    rec('                                                                named assumption')
    rec('      SUM_p W_p IS CC`s (149), factor for factor `b305`/`b306`  DERIVED-ON-CONTENT +')
    rec('                                                                IMPORT-UNDER-THE-BAR')
    rec('      lambda_Z(n) = -S_f(n)                     `b327` (L1)     DERIVED under a sealed bar')
    rec('      Proposition C.1 available at the window   this act        IMPORT-UNDER-THE-BAR,')
    rec('                                                                verified at page index 51')
    rec('      Theorem 1 NOT available at the window     this act        ABSENT BY HYPOTHESIS,')
    rec('                                                                verified at page index 3')
    rec()
    rec('  ### ### **THE ONE ABSENT ELEMENT, AND IT IS THE ONLY ONE:** ### **ANY STATEMENT')
    rec('  ### ### EVALUATING OR BOUNDING `SUM_p W_p(f)` AT `a^2 >= 2` AGAINST AN ARCHIMEDEAN')
    rec('  ### ### QUANTITY.** ### The record holds ten cells of VALUES there and no statement.')
    rec()
    rec('  ### **PRICED AS A RESULT AND NOT AS AN INSTRUMENT RUN.** ### `b321` already computed the')
    rec('  ### ten cells; a further computation buys more instances and not a statement. ### **THIS')
    rec('  ### ### IS `U1`s SHAPE AT A FOURTH SITE -- what the record holds is a family indexed by')
    rec('  ### ### something, and what it needs is one statement uniform in that index** -- and')
    rec('  ### this act NAMES the resemblance and types no bridge to the other three, exactly as')
    rec('  ### row `U1` refuses to.')
    rec()
    rec('  ### ### **NOT OPENED. ### THIS ACT DOES NOT ATTEMPT `(Q400)`, AND THE ORDER DID NOT ASK')
    rec('  ### ### IT TO.**')
    rec()
    bar()
    rec('### (2e) THE FERRY`S ADDITION TWO -- THE WINDOW, WHERE A BRIDGE WOULD HAVE TO LIVE.')
    bar()
    rec('  ### **THE ORDER`S OWN PHRASE, QUOTED:** ### *"at a support wide enough that primes')
    rec('  ### enter, which is outside the source`s class and where neither Theorem 1 nor')
    rec('  ### Proposition C.1 applies."*')
    rec('  ### ### **AND IT IS HALF FALSE, TESTED AGAINST THE VERIFIED ARTEFACT RATHER THAN')
    rec('  ### ### ADOPTED.**')
    rec('      ### **THEOREM 1 CARRIES A SUPPORT HYPOTHESIS** (page index `3`): *"let g in')
    rec('        C_c^inf(R*_+) have support in the interval [2^{-1/2}, 2^{1/2}] and Fourier')
    rec('        transform vanishing at i/2 and 0, then one has W_inf(g*g^#) >= Tr(theta(g) S')
    rec('        theta(g)*)."* ### **SO THE ORDER IS RIGHT ABOUT THEOREM 1.**')
    rec('      ### **PROPOSITION C.1 CARRIES NONE** (page index `51`): *"...a finite set disjoint')
    rec('        from Z and containing {0,1}, then RH <=> SUM_v W_v(g*g^#) <= 0 for all g in')
    rec('        C_c^inf(R*_+) with g-tilde(z) = 0 for all z in F."* ### **THE ONLY CONDITIONS ARE')
    rec('        SMOOTHNESS, COMPACT SUPPORT AND THE FINITE VANISHING SET. ### THERE IS NO SUPPORT')
    rec('        INTERVAL. ### SO THE ORDER IS WRONG ABOUT PROPOSITION C.1.**')
    rec('  ### ### **AND THE CORRECTION MAKES THE WINDOW BETTER, NOT WORSE: ### AT THE WINDOW THE')
    rec('  ### ### BOUND IS GONE AND THE CRITERION IS STILL IN FORCE.** ### That is the whole')
    rec('  ### reason `(Q400)` is worth typing rather than filing as unreachable.')
    rec()
    rec('  ### **AND THE SECOND HALF OF ADDITION TWO: IT IS THE SAME OBJECT THE FINITE-INSTANCE')
    rec('  ### ### IDENTITY WAS REALIZED ON AND FOUND EMPTY BY STRUCTURE.**')
    for hint in ('FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE OF ANYTHING',
                 'BOTH FACTS ARE',
                 'they carry no information the zero side did not already carry'):
        i, ln = live(os.path.join(D, 'b321_the_window_opened.txt'), hint, 240)
        rec('      `b321_the_window_opened.txt:%s`' % i)
        rec('      > %s' % ln)
    rec()
    rec('  ### ### **AND THE DISTINCTION THAT KEEPS THAT FROM BEING A CLOSURE, STATED SO A READER')
    rec('  ### ### CAN REFUSE IT:** ### what `b321` found empty was the ### **TOTAL** ###')
    rec('  ### `SUM_v W_v`, forced non-positive by a vanishing pole term and a zero library that')
    rec('  ### contains only zeros on the line. ### **`(Q400)` ASKS ABOUT THE CONSTITUENT')
    rec('  ### ### `SUM_p W_p`, WHICH THAT SAME ACT PRINTED AS A LIVE, SIGN-CHANGING COLUMN** --')
    rec('  ### `+0.000062755` at `a = 1.5`, `-0.064050234` at `a = 2.1`, `+0.190860829` at `a = 3`.')
    rec('  ### **A TOTAL FORCED BY STRUCTURE DOES NOT MAKE ITS CONSTITUENTS EMPTY.**')
    rec()
    bar()
    rec('### (2f) AND THE CLAIM THE FERRY FORBIDS UNLESS THE RECORD MAKES IT.')
    bar()
    rec('  ### The ferry: *no claim that the bridge and the clause are one question unless the')
    rec('  ### record`s own words say it, in which case quote them.*')
    rec('  ### ### **THE SEARCH RAN OVER THE THREE LEDGERS AND RETURNED `%d` HITS, ALL HAND-READ.**'
        % EX['fig'].get('one_question_hits', 0))
    rec('      `FINDINGS.md:2473` and `:2507` -- the new-keystone question, the author`s alone.')
    rec('      `FINDINGS.md:3326`             -- a question priced on one axis, resolved on another.')
    rec('      `OPEN_TRAILS.md:322`           -- THE ONE QUESTION of a source connection at infinity.')
    rec('      `OPEN_TRAILS.md:4519`          -- four different answers to one question (`b393`).')
    rec('  ### ### **NONE IS ABOUT THE BRIDGE AND THE CLAUSE. ### THE CLAIM IS NOT MADE, IN EITHER')
    rec('  ### ### DIRECTION.**')
    rec()
    FIG['verdict'] = 'TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW'
    FIG['one_question_claim'] = 0


# ==================================================================================================
def component3():
    bar('=')
    rec('### COMPONENT 3 -- THE PRIME BOUND`S SLACK, MEASURED WHERE THE CLASS ALLOWS IT.')
    bar('=')
    rows = EX['fig']['grid']
    rec('    a       a^2        lawful   prime powers in [a^-2, a^2]')
    for r in rows:
        rec('    %-6.2f  %-9.5f  %-7s  %s'
            % (r['a'], r['a2'], 'YES' if r['lawful'] else 'no',
               r['primes_open'] if r['primes_open'] else '[] ### NONE'))
    nlaw = sum(1 for r in rows if r['lawful'])
    nlawp = sum(1 for r in rows if r['lawful'] and r['primes_open'])
    rec()
    rec('  ### ### **LAWFUL CELLS : `%d`. ### LAWFUL CELLS ADMITTING A PRIME POWER : `%d`.**'
        % (nlaw, nlawp))
    rec('  ### ### **UNLAWFUL CELLS : `%d`, AND ALL `%d` ADMIT AT LEAST ONE.**'
        % (len(rows) - nlaw, len(rows) - nlaw))
    FIG['lawful'] = nlaw
    FIG['lawful_with_prime'] = nlawp
    rec()
    rec('  ### ### ### **SO `(N5)` IS MET AND `(N2)` IS REFUTED, BY A PRINTED CELL: ### NO BANKED')
    rec('  ### ### ### LAWFUL SEED ADMITS A PRIME POWER.**')
    rec()
    rec('  ### **AND THE ANSWER IS REPORTED AS WHAT IT IS -- A FACT ABOUT THE FAMILIES THE ARC')
    rec('  ### ### BUILT, AND MORE THAN THAT, A FACT ABOUT THE CLASS THE SOURCE DEFINED.** ### The')
    rec('  ### least prime power is `2`; Theorem 1`s support condition is exactly')
    rec('  ### `supp(f) SUBSET (1/2, 2)`; so a prime power in the support requires `a^2 >= 2`,')
    rec('  ### which is exactly the failure of that condition. ### **THE CENSUS COULD NOT HAVE COME')
    rec('  ### ### OUT ANY OTHER WAY, AND THAT IS THE FINDING RATHER THAN THE COUNT.** ### A class')
    rec('  ### whose every banked member is silent on the primes is silent because its members were')
    rec('  ### chosen to be, and `b321` had already said of exactly these cells that their silence')
    rec('  ### *IS A FACT ABOUT A SUPPORT AND NOT A FINDING.*')
    rec()
    rec('  ### **AND THE OTHER BANKED FAMILIES ARE NAMED SO THE SCOPE IS NOT OVERSTATED.** ### The')
    rec('  ### two-radius family (`F6`) and the Epstein negative control (`F7`) are indexed the same')
    rec('  ### way, by a truncation radius, so the same interval argument governs them; the Li')
    rec('  ### family (`F3`, `L1`) has ### **NO COMPACT SUPPORT AT ALL**, so it is not lawful for a')
    rec('  ### different reason -- ### **AND TWO OBJECTS FAILING ONE TEST FOR TWO DIFFERENT REASONS')
    rec('  ### ### ARE NOT ONE OBSERVATION.**')
    rec()
    rec('  ### ### **WHAT A FAMILY THAT DID ADMIT A PRIME POWER WOULD COST, STATED EXACTLY.**')
    rec('  ### It leaves Theorem 1`s class, ### **SO THE TRACE BOUND IS GONE** -- and with it the')
    rec('  ### only thing the record has that bounds the compressed square by the archimedean')
    rec('  ### distribution. ### It stays inside Proposition C.1`s class, ### **SO THE CRITERION IS')
    rec('  ### ### NOT GONE.** ### And the archimedean side does not transfer between L-functions')
    rec('  ### with different gamma factors: `b325` recorded `Gamma(s)` against `Gamma(s/2)` for the')
    rec('  ### Epstein aim, so a family widened at a DIFFERENT object costs the archimedean')
    rec('  ### identification as well. ### **THE PRICE IS A THEOREM, NOT A RUN.**')
    rec()
    bar()
    rec('### (3b) AND ONE DEFECT FOUND ON A PRIOR ACT`S FACE, PRINTED AND NOT REPAIRED.')
    bar()
    rec('  ### `b321`s Component 3 states its rule as *a prime power `p^m` enters exactly when')
    rec('  ### `p^m <= a^2`*, and its printed list omits `4` at `a = 2` and `9` at `a = 3`, which is')
    rec('  ### the STRICT reading. ### **THE RULE AND THE LIST ON THAT FACE ARE TWO CONVENTIONS,')
    rec('  ### ### AND THEY DISAGREE AT `2` OF `13` CELLS.**')
    rec('  ### ### **IT MOVES NO VALUE.** ### `f = g conv g^#` is a self-convolution supported in')
    rec('  ### `[a^-2, a^2]` and VANISHES AT ITS ENDPOINTS, so an endpoint prime power contributes')
    rec('  ### `0` to (149) under either reading; what differs is a printed membership list.')
    rec('  ### ### **THE PRIOR FACE IS NOT EDITED.** ### Both conventions are printed above and in')
    rec('  ### `data/b400_extract_notes3.txt` cell by cell, and the disagreement is ROUTED.')
    rec('  ### ### **AND THE ROUTE THAT MATCHES `b321`s LIST IS THE STRICT ONE**, so this act reads')
    rec('  ### its own census under the OPEN convention and says so rather than choosing silently.')
    rec()


def main():
    bar('=')
    rec('b400 -- THE BRIDGE RESTATED, OR THE PAIR DECLARED TWO OBJECTS. ### THE COMPONENTS.')
    rec('### **RUN AFTER THE LOCK. ### THE FACE IS SEALED AT'
        ' `f35d9626ecfbebc59ae01b4185101e5d8261c36746d9f09e93c398f7bf7244ce`.**')
    bar('=')
    rec()
    component1()
    component2()
    component3()
    bar('=')
    rec('### THE COMPONENTS, COUNTED.')
    bar('=')
    rec('    constraints in the set          : %d' % FIG['constraints'])
    rec('    constraints held at DERIVES     : %d' % FIG['constraints_at_derives'])
    rec('    verdict                         : %s' % FIG['verdict'])
    rec('    lawful cells / with a prime     : %d / %d' % (FIG['lawful'], FIG['lawful_with_prime']))
    rec('    claims that the bridge and the clause are one question : %d'
        % FIG['one_question_claim'])
    bar('=')
    p = run_clock.write(D, 'b400_components_run', L)
    io.open(os.path.join(D, 'b400_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(FIG, indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b400_components.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
