# -*- coding: utf-8 -*-
"""b404_components.py -- COMPONENTS 1 TO 3 AND BOTH ADDITIONS, RUN AFTER THE LOCK.

### ### **NOTHING HERE COMPUTES AND NOTHING IS BUILT.** ### Every figure is read from
### `b404_extract.json` or re-anchored live in the file that emitted it.
### ### **AND EVERY CLAIM QUOTED FROM ANOTHER DOCUMENT IS QUOTED WITH THE SENTENCE THAT SCOPES
### ### IT** -- which is the defect this act is reporting, and an act that committed it while
### reporting it would have nothing to say.
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
SE = os.path.join('D:', os.sep, 'SIDE-effects')
SG = os.path.join('D:', os.sep, 'SIDE-global-section')
FL = os.path.join(PP, 'FACES_LEDGER.md')
CONS = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
SERM = os.path.join(SE, 'README.md')
M1 = os.path.join(SE, 'SIDEEffects', 'Phase15', 'Module1.lean')
FS = os.path.join(SG, 'Core', 'FiniteSideSeal.lean')
AP = os.path.join(SG, 'AXIOM_PRINTS.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
FIG = {}
EX = json.load(io.open(os.path.join(D, 'b404_extract.json'), encoding='utf-8'))


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=220):
    return ' '.join(s.split())[:n]


def live(path, hint, n=260):
    try:
        i, ln = AF.find(path, hint)
        return i, flat(ln, n)
    except Exception:
        return 0, '### **NOT ANCHORED LIVE**'


def cite(path, hint, label, n=260):
    i, ln = live(path, hint, n)
    rec('      %s  ### `%s:%s`' % (label, os.path.basename(path), i))
    rec('      > %s' % ln)
    return i, ln


# ==================================================================================================
def component1():
    bar('=')
    rec('### COMPONENT 1 -- THE FIFTH SITE, ON ITS CONTENT.')
    bar('=')
    rec('### ### ### **VERDICT : ### ENTERED AS `(v)`.**')
    rec()
    rec('  ### **WHAT EACH CONSTANT IS ALLOWED TO DEPEND ON, FROM THE SOURCE AT CONTENT.**')
    rec('      ### **THEOREM 6.1** (the finite places), page index `26`: *there holds*')
    rec('      ### `S_f(n, pi) = lambda_n(n, pi) + O(n log n)`, ### *in which the implied constant')
    rec('      ### in the O-notation ### **DEPENDS ON `pi`.***')
    rec('      ### **THEOREM 5.1** (the archimedean place), page index `18`: the same shape, and')
    rec('      ### *the implied constant in the O notation is ### **ABSOLUTE.***')
    rec('      ### ### **SO ONE CHANNEL`S ERROR IS ALLOWED TO KNOW WHICH REPRESENTATION IT IS')
    rec('      ### ### LOOKING AT AND THE OTHER`S IS NOT.**')
    rec()
    rec('  ### **DOES THE RECORD NEED A STATEMENT UNIFORM IN `pi`? ### THE ROW`S OWN TEST, ASKED')
    rec('  ### ### AND NOT ASSUMED.** ### The row`s shape: *what the record holds is a family')
    rec('  ### indexed by something, and what it needs is one statement uniform in that index.*')
    rec('      the record holds : a finite-place bound whose constant is indexed by `pi`')
    rec('      the record needs : one whose constant is not')
    rec('      ### ### **IT FITS.**')
    rec()
    cite(os.path.join(D, 'b401_the_absent_element_searched.txt'),
         'ADDITION ONE : ### UNIFORM -- AND VACUOUSLY',
         '### `b401` found it and did not enter it')
    rec()
    rec('  ### ### **AND THE FERRY`S CORRECTION IS CARRIED HERE, WHERE THE ENTRY IS MADE.** ### The')
    rec('  ### `b403` ferry called the window a fifth site; ### **THE WINDOW IS THE ROW`S FOURTH**,')
    rec('  ### entered by `b401`, and `b403` said so and entered nothing. ### **THE DISTINCT FIFTH')
    rec('  ### ### IS THIS ONE**, and the navigator`s own correction records it. ### **A MISCOUNT')
    rec('  ### ### CORRECTED BY THE PARTY THAT MADE IT IS RECORDED, NOT ABSORBED.**')
    FIG['c1'] = 'ENTERED AS (v)'
    rec()


def component2():
    bar('=')
    rec('### COMPONENT 2 -- WHAT `pi`-UNIFORMITY WOULD BUY, PRICED AND NOT SOUGHT.')
    bar('=')
    rec('### **THE ORDER`S SHARPENING:** ### *uniformity in the representation is uniformity ACROSS')
    rec('### L-functions, and a corpus studying one L-function has nothing across which to be')
    rec('### uniform.* ### **THE PREMISE IS CHECKED BEFORE THE CONCLUSION IS DRAWN.**')
    rec()
    rec('  ### **(2a) IS THIS A ONE-L-FUNCTION CORPUS? ### NO, AND THE SECOND ONE IS IN THE')
    rec('  ### ### LEDGER.**')
    cite(FL, 'a positive Li ledger with RH false',
         '### row `F7`, the Epstein negative control at `Z_Q`', 460)
    rec('      ### ### **A SECOND L-FUNCTION, ALREADY AIMED AT AND ALREADY MEASURED.**')
    rec()
    rec('  ### **(2b) AND THE RECORD HAS ALREADY MEASURED A TRANSFER FAILURE ACROSS THE TWO.**')
    cite(os.path.join(D, 'b325_the_negative_control.txt'),
         'THE ARCHIMEDEAN DISTRIBUTION DOES NOT TRANSFER',
         '### `b325`, at its own line', 300)
    cite(os.path.join(D, 'b326_the_reach.txt'),
         'do not: Theorem 1 and Theorem 4.7 are stated for',
         '### and `b326` naming which hypothesis fails', 320)
    rec('      ### ### **SO THERE IS SOMETHING TO BE UNIFORM ACROSS, AND `(N2)`S PREMISE IS')
    rec('      ### ### FALSE.**')
    rec()
    rec('  ### **(2c) AND YET `pi`-UNIFORMITY STILL BUYS THE CORPUS NOTHING, FOR A REASON THE')
    rec('  ### ### PREMISE NEVER REACHED.** ### Theorem 6.1 quantifies over ### *any irreducible')
    rec('  ### cuspidal unitary automorphic representation on `GL(N)`* ### -- and the corpus`s')
    rec('  ### second object is ### **NOT ESTABLISHED TO BE ONE.** ### The record`s own `H-CUSP`')
    rec('  ### grade is the evidence: even `zeta` sits in that class only under the source`s stated')
    rec('  ### convention, graded by `b358`, INHERITED by `b361`, and undecided since.')
    cite(os.path.join(D, 'b361_the_held_item.txt'), 'IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT',
         '### the grade, still inherited', 300)
    rec('      ### ### **A UNIFORMITY OVER A CLASS THAT DOES NOT CONTAIN YOUR SECOND OBJECT IS NOT')
    rec('      ### ### A UNIFORMITY YOU CAN SPEND.**')
    rec()
    rec('  ### **(2d) SO THE EMPTINESS IS NAMED BY KIND, WHICH IS WHAT THE ORDER ASKED FOR.**')
    rec('      ### **KIND (a) -- EMPTY BECAUSE THERE IS NOTHING TO RANGE OVER.** ### A site whose')
    rec('      ### index has one value. ### **VACUOUS FOREVER**; nothing could ever make it bite.')
    rec('      ### **KIND (b) -- EMPTY BECAUSE THE AVAILABLE UNIFORMITY RANGES OVER A CLASS THAT')
    rec('      ### ### DOES NOT CONTAIN YOUR OTHER OBJECT.** ### The obstruction is REAL and the')
    rec('      ### instrument is AIMED ELSEWHERE. ### **A DIFFERENT STATEMENT COULD BITE.**')
    rec('      ### ### ### **`(v)` IS KIND (b).**')
    rec('  ### ### **AND THE DISTINCTION IS THE COMPONENT`S PRODUCT, NOT A HEDGE ON ITS VERDICT:**')
    rec('  ### a site empty in kind (a) should never have been entered; a site empty in kind (b)')
    rec('  ### is entered and its emptiness is a fact about the available instrument. ### **THE ROW')
    rec('  ### ### HAS NEVER HAD TO DRAW IT AND WILL NEED IT AGAIN.**')
    rec('  ### ### **AND NOTHING IS OPENED.** ### What a `pi`-uniform bound over the right class')
    rec('  ### would cost is not priced here, because naming the class it would have to range over')
    rec('  ### is itself the open work.')
    FIG['c2'] = 'NOT EMPTY IN KIND (a); EMPTY IN KIND (b)'
    rec()


def addition_one():
    bar('=')
    rec('### ADDITION ONE -- THE SIXTH CANDIDATE: THE TYPE-D RESIDUE.')
    bar('=')
    rec('### ### ### **VERDICT : ### ENTERED AS `(vi)`.**')
    rec()
    rec('  ### **(A1a) THE BOUNDARY PARAGRAPH, READ AT CONTENT AND QUOTED.**')
    cite(CONS, 'The boundary is a local-to-global interchange',
         '### the keystone`s own sentence', 900)
    rec()
    rec('  ### **(A1b) THE ROW`S TESTS, ASKED OF IT.**')
    rec('      ### **DOES IT CLOSE AT EVERY INSTANCE?** ### YES -- the paper`s compiled half is')
    rec('      ### exhaustiveness at every finite modulus, and the modulus is the index.')
    rec('      ### **IS IT MISSING ACROSS INSTANCES?** ### YES -- and the paper says so three')
    rec('      ### times, once per problem, in the same words each time:')
    for hint, lbl in (('the density lower bound is the whole of the remaining weight',
                       'twin primes (M3)'),
                      ('the representation lower bound is the whole of the remaining weight',
                       'Goldbach (M4)'),
                      ('the sieve density bound is the whole of the remaining weight',
                       'Sophie Germain (M5)')):
        i, ln = live(CONS, hint, 240)
        rec('          %-22s `:%s`  > %s' % (lbl, i, ln[-150:]))
    rec('      ### ### **THE SHAPE FITS, AND IT FITS MORE SHARPLY THAN THE EXISTING ENTRIES**,')
    rec('      ### because the keystone names the interchange itself rather than leaving it to be')
    rec('      ### inferred from a measurement.')
    rec()
    rec('  ### **(A1c) AND THE PARAGRAPH CARRIES SOMETHING THE ROW HAS NEVER CITED.**')
    rec('      The same sentence reports the programme has this shape ### **COMPILED**: ### the')
    rec('      unrestricted commutation of the two quantifiers is ### **FALSE AS A THEOREM** ###')
    rec('      (an explicit countermodel), and it ### **CLOSES ONLY UNDER A SHARED WITNESS.**')
    rec('      ### ### **A COMPILED NEGATIVE RESULT ABOUT THE ROW`S OWN SHAPE, SITTING IN THE')
    rec('      ### ### RECORD, UNCITED BY THE ROW.**')
    rec('      ### ### **AND IT IS REPORTED AND NOT TYPED AS A BRIDGE.** ### A theorem about a')
    rec('      ### SHAPE is not a theorem about any instance of it; the row`s law forbids the')
    rec('      ### crossing and this act does not make it. ### **WHAT IT DOES IS SAY THE THING IS')
    rec('      ### ### THERE.**')
    rec()
    rec('  ### **(A1d) THE FILING THE ORDER ASKS FOR, AS A FILING ONLY.**')
    rec('      ### The keystone does two things the row`s entries mostly do not: it ### **NAMES ITS')
    rec('      ### ### MISSING STATEMENT EXACTLY** ### (M3, M4, M5, each a named analytic')
    rec('      ### requirement) and it ### **FILES THE RESIDUE AS THE WHOLE OF THE REMAINING')
    rec('      ### ### WEIGHT.**')
    rec('      ### Of the row`s existing entries: ### `(i)` names the missing thing (*the')
    rec('      ### quantifiers ... are UNOWNED*) and files no residue; ### `(ii)` names the gap')
    rec('      ### (*running the census higher buys more instances*) and files no residue;')
    rec('      ### `(iii)` names it (*an exhaustion at every width is not an exhaustion across')
    rec('      ### widths*) and files no residue; ### `(iv)` ### **DOES BOTH**, naming the one')
    rec('      ### absent element and calling it the only one.')
    rec('      ### ### **SO THE FORM EXISTS IN THE ROW ALREADY, AT ONE ENTRY OF FOUR.** ### That')
    rec('      ### the row COULD be restated in that form throughout is ### **ROUTED TO THE')
    rec('      ### ### AUTHOR AND NOT DONE HERE**, and this act restates nothing.')
    FIG['a1'] = 'ENTERED AS (vi)'
    rec()


def addition_two():
    bar('=')
    rec('### ADDITION TWO -- ONE THEOREM OR TWO. ### **PRICED, NOT PROVED. ### DECIDED BY NOBODY.**')
    bar('=')
    rec('### ### ### **VERDICT : ### TWO THEOREMS -- AND NOT PARTING WHERE `(N5)` SAYS.**')
    rec()
    rec('  ### **(A2a) THE FIRST TERMINAL, AT CONTENT.**')
    cite(M1, 'theorem crt_exhaustiveness', '### `SIDEEffects.Phase15.Module1`', 320)
    cite(M1, 'theorem no_type_d_conspiracies', '### and the exclusion it licenses', 260)
    cite(M1, 'moduli := {L}', '### ### **AND THE MODULI SET IT PRODUCES**', 200)
    rec('      ### ### **THE MODULAR COUPLING HAS A SINGLETON MODULI SET -- THE COUPLING`S OWN')
    rec('      ### ### PERIOD.** ### So the terminal says: ### **A PERIODIC PREDICATE ON THE')
    rec('      ### ### NATURALS IS A CONGRUENCE CONDITION AT ITS OWN PERIOD.** ### That is what is')
    rec('      ### compiled. ### **`CRT` IS THE NAME FOR WHAT IT LICENSES, NOT FOR WHAT IT PROVES**')
    rec('      ### -- and the paper`s own wording, *CRT exhaustiveness via periodic lift*, says the')
    rec('      ### second half correctly.')
    rec()
    rec('  ### **(A2b) THE SECOND TERMINAL, AT CONTENT.**')
    cite(FS, 'theorem finite_side_silence', '### `B329.finite_side_silence`', 420)
    cite(FS, 'Component 4 -- EXHAUSTIVENESS (`finite_side_silence`): one theorem whose',
         '### and what its own module says of it', 420)
    rec('      ### ### **IT IS STATED AT ONE PLACE `p` AND ONE LEVEL `n`, GENERAL IN BOTH, AND')
    rec('      ### ### PER-CELL IN ITS THIRD CONJUNCT.** ### It forms no product over places.')
    rec()
    rec('  ### **(A2c) ONE OR TWO, AND WHERE THEY PART.**')
    rec('      ### ### **TWO.** ### One is about the PERIODICITY OF A PREDICATE ON THE NATURALS;')
    rec('      ### the other about the `p`-ADIC DECOMPOSITION OF AN INDEX IN A GRID. ### Neither')
    rec('      ### mentions the other`s objects.')
    rec('      ### ### **AND `(N5)`S PARTING POINT IS REFUTED BY A PRINTED LINE.** ### It says they')
    rec('      ### part *at the passage from finitely many moduli to a restricted product.* ###')
    rec('      ### **NEITHER OF THEM EVER REACHES A RESTRICTED PRODUCT**, and the first does not')
    rec('      ### even reach finitely-many-plural: its moduli set is `{L}`. ### **THEY PART FAR')
    rec('      ### ### EARLIER THAN THE PLACE THE EXPECTATION NAMES, AND THE PASSAGE IT NAMES IS A')
    rec('      ### ### STEP NEITHER OF THEM TAKES.**')
    rec('      ### ### **SO THE CORPUS HAS NOT PROVED ITS OWN BOUNDARY TWICE.** ### It has proved')
    rec('      ### two different small things on either side of a boundary neither one crosses.')
    rec()
    rec('  ### **(A2d) THE AXIOM PROFILES, AND THE HALF OF THE INSTRUCTION THAT CANNOT BE CARRIED')
    rec('  ### ### OUT.**')
    cite(AP, "'B329.finite_side_silence' does not depend on any axioms",
         '### **READ FROM A PRINTED PROFILE**', 200)
    f = EX['fig']
    rec('      printed-profile files in `SIDE-effects`            : %s'
        % (f.get('se_profile_files') or '### **NONE**'))
    rec('      `.lean` files there carrying a `#print axioms` line : %d'
        % f.get('se_axiomcheck_files', 0))
    rec('      ### ### **SO THE PROFILE OF `no_type_d_conspiracies` CANNOT BE READ FROM THAT')
    rec('      ### ### REPOSITORY AT ALL, AND THE INSTRUMENT LANE IS PARKED SO IT IS NOT BUILT.**')
    rec('      ### ### **IT IS REPORTED UNREAD. ### IT IS NOT INFERRED.**')
    rec()
    rec('  ### **(A2e) AND WHAT THE SOURCES SAY ABOUT THAT PROFILE, WITH THEIR SCOPES.**')
    cite(CONS, '`SIDE-effects` (`c66f3c5`; vanilla Lean 4, no Mathlib). The additive-multiplicative',
         '### ### **THE KEYSTONE`S CLAIM**', 480)
    cite(SERM, 'Axiom-free; core', '### the README`s claim -- and read its whole sentence', 420)
    cite(SERM, 'no-conspiracy result. Genuine content, 0 sorry',
         '### ### **AND WHAT THE README SAYS OF THIS MODULE**', 300)
    rec('      ### ### **THE README SCOPES `Axiom-free; core Lean only, no Mathlib` TO A DIFFERENT')
    rec('      ### ### MODULE, AND OF `Module1` IT SAYS ONLY `Genuine content, 0 sorry`.**')
    cite(M1, 'import Mathlib', '### ### **AND `Module1` IMPORTS MATHLIB**', 160)
    cite(M1, 'classical decidability for the residue filter',
         '### which its own header discloses', 320)
    rec('      ### **AND AT THE REF THE KEYSTONE ITSELF CITES, `c66f3c5` :**')
    for ln in f.get('imports_at_cited_ref', []):
        rec('          > %s' % ln)
    rec('      ### ### **MATHLIB IMPORTED AT THE CITED REF : %s**'
        % f.get('mathlib_at_cited_ref'))
    rec()
    rec('      ### ### ### **SO THE KEYSTONE WIDENS A CLAIM THE REPOSITORY SCOPES NARROWLY, AND IT')
    rec('      ### ### ### DOES SO AT THE REF IT ITSELF CITES.** ### **THE README IS EXACT.**')
    rec('      ### ### **AND WHAT THIS ACT DOES NOT SAY:** ### it does NOT say the terminals carry')
    rec('      ### axioms. ### **AN IMPORT LINE IS NOT A MEASUREMENT**, nothing was built, and a')
    rec('      ### claim shown to rest on a false premise is not thereby shown false.')
    rec('      ### ### **REPORTED AND ROUTED. ### THE KEYSTONE IS NOT EDITED.**')
    FIG['a2'] = 'TWO THEOREMS; (N5) PARTING POINT REFUTED; one profile READ, one UNREAD'
    rec()


def component3():
    bar('=')
    rec('### COMPONENT 3 -- THE ROW`S OWN LAW, TESTED AT SIX.')
    bar('=')
    rec('### ### ### **VERDICT : ### STRAINED.**')
    rec()
    cite(FL, 'A ROW NAMING THREE THINGS THAT LOOK ALIKE',
         '### the row`s own warning, at its own line', 420)
    rec()
    rec('  ### **WHAT THE ROW NOW CARRIES, AND WHY SIX IS NOT THREE.**')
    rec('      `(i)`   the clause`s quantifier          -- indexed by the class and the zeros')
    rec('      `(ii)`  the height coordinate            -- indexed by height')
    rec('      `(iii)` the width coordinate             -- indexed by the support width')
    rec('      `(iv)`  the prime constituent            -- indexed by the support width')
    rec('      `(v)`   the representation constant      -- indexed by `pi`, EMPTY IN KIND (b)')
    rec('      `(vi)`  the Type-D residue               -- indexed by the modulus')
    rec('  ### ### **THREE STRAINS, EACH NAMED RATHER THAN SUMMED.**')
    rec('      ### **(1) TWO SITES SHARE AN INDEX.** ### `(iii)` and `(iv)` are both indexed by the')
    rec('      ### support width and differ only in object -- which `b401` put on the face of its')
    rec('      ### own entry precisely so the pair could not be read as two independent witnesses.')
    rec('      ### **(2) ONE SITE IS EMPTY.** ### `(v)` is empty in kind (b), so a reader counting')
    rec('      ### the row`s instances as live obstructions would over-count by one.')
    rec('      ### **(3) ONE SITE IS FROM A DIFFERENT DISCIPLINE.** ### `(vi)` is additive number')
    rec('      ### theory with a compiled local half; the other five are analytic. ### **A ROW THAT')
    rec('      ### ### SPANS TWO DISCIPLINES IS EITHER A DEEP OBSERVATION OR A LOOSE ONE, AND')
    rec('      ### ### NOTHING IN THE ROW DECIDES WHICH.**')
    rec()
    rec('  ### ### **IS IT STILL NAMING A RESEMBLANCE, OR HAS IT BECOME A CLAIM? ### STILL A')
    rec('  ### ### RESEMBLANCE, AND ONLY BECAUSE ITS REFUSAL IS RESTATED AT EVERY ENTRY.** ### The')
    rec('  ### row types no bridge; every entry that could be mistaken for a witness names what it')
    rec('  ### shares with another; and this act adds two more entries under the same discipline.')
    rec('  ### ### **BUT THE MARGIN IS THINNER AT SIX THAN IT WAS AT THREE, AND THAT IS THE')
    rec('  ### ### STRAIN.**')
    rec()
    rec('  ### **WHAT WOULD RELIEVE IT, ROUTED AND NOT APPLIED.** ### The form Addition One`s')
    rec('  ### filing describes: ### **EVERY ENTRY NAMING ITS MISSING STATEMENT EXACTLY AND FILING')
    rec('  ### ### ITS RESIDUE AS THE WHOLE OF THE REMAINING WEIGHT.** ### An entry in that form is')
    rec('  ### checkable on its own and cannot be read as a witness for another; a row of six such')
    rec('  ### entries carries no accidental equivalence because each one states its own debt in')
    rec('  ### full. ### **ONE OF THE SIX IS ALREADY IN THAT FORM.** ### **ROUTED TO THE AUTHOR.')
    rec('  ### ### THIS ACT RESTATES NOTHING.**')
    FIG['c3'] = 'STRAINED'
    rec()


def main():
    bar('=')
    rec('b404 -- THE FIFTH SITE, THE SIXTH CANDIDATE, AND THE ROW`S LAW. ### THE COMPONENTS.')
    rec('### **RUN AFTER THE LOCK. ### THE FACE IS SEALED AT'
        ' `bad1ea6b2a5a977eaca6a75a5c0bd1e349c2604134db53ab5e98da06b791e172`.**')
    bar('=')
    rec()
    component1()
    component2()
    addition_one()
    addition_two()
    component3()
    bar('=')
    rec('### THE COMPONENTS, COUNTED.')
    bar('=')
    for k, v in (('Component 1', FIG['c1']), ('Component 2', FIG['c2']),
                 ('Addition One', FIG['a1']), ('Addition Two', FIG['a2']),
                 ('Component 3', FIG['c3'])):
        rec('    %-14s : %s' % (k, v))
    bar('=')
    p = run_clock.write(D, 'b404_components_run', L)
    io.open(os.path.join(D, 'b404_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(FIG, indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b404_components.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
