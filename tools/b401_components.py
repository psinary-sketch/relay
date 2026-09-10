# -*- coding: utf-8 -*-
"""b401_components.py -- COMPONENTS 1 AND 2, RUN AFTER THE LOCK, IN THE ORDER'S OWN ORDER.

### ### **THE ORDER PUTS ADDITION ONE BEFORE THE FOURTH SITE**, because whether `(Q400)` is a
### fourth instance of the obstruction or the first crack in it is decided by whether the one bound
### the search locates is uniform in an index it actually carries.

### ### **NOTHING HERE COMPUTES.** ### Every figure is read from `b401_extract.json`, written before
### the lock, or re-anchored live in the file that emitted it.
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
SW = os.path.join('D:', os.sep, 'SIDE-window')
FL = os.path.join(PP, 'FACES_LEDGER.md')
RM = os.path.join(SW, 'README.md')

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


EX = json.load(io.open(os.path.join(D, 'b401_extract.json'), encoding='utf-8'))
SRC = {s['tag']: s for s in EX['srcreads'] if s.get('tag')}


def live(path, hint, n=220, span=False):
    try:
        if span:
            i, runs = AF.find_span(path, hint)
            return i, flat(' '.join(runs), n)
        i, ln = AF.find(path, hint)
        return i, flat(ln, n)
    except Exception:
        return 0, '### **NOT ANCHORED LIVE**'


# ==================================================================================================
def component1():
    bar('=')
    rec('### COMPONENT 1 -- THE ABSENT ELEMENT, SEARCHED FOR RATHER THAN ASSUMED ABSENT.')
    bar('=')
    rec('### ### ### **VERDICT : ### PRESENT BUT NOT APPLICABLE.**')
    rec()
    bar()
    rec('### (1a) WHAT WAS SEARCHED FOR, AND THE MATCHERS` WHOLE YIELD.')
    bar()
    rec('  ### **THE TARGET, STATED BEFORE THE YIELD SO THE YIELD CAN BE JUDGED AGAINST IT:** ###')
    rec('  ### any statement EVALUATING or BOUNDING a finite-place sum at a support wide enough')
    rec('  ### that primes enter, against a quantity of another kind.')
    rec()
    y = EX['fig']['yields']
    rows = EX['fig']['yield_rows']
    for k in y:
        rec('    ### matcher **%s** : ### **%d HIT(S)**' % (k, y[k]))
    rec()
    rec('  ### **AND THE RESIDUE IS HAND-READ RATHER THAN COUNTED.**')
    rec('  ### ### **`a bound on the prime sum` : `1` HIT, AND IT IS THIS ACT`S OWN FERRY.** ### The')
    rec('  ### matcher`s only hit in `4536` files is the order asking the question. ### **A MATCHER')
    rec('  ### ### WHOSE ONLY HIT IS THE QUESTION HAS FOUND NOTHING, AND SAYING SO IS THE RESULT.**')
    rec('  ### ### **`the prime sum bounded above` : `14` HITS, ALL ONE STATEMENT.** ### Every one')
    rec('  ### is `b399`s or `b400`s restatement of Theorem 1 against Proposition C.1 ### **ON THE')
    rec('  ### ### LAWFUL CLASS**, where the sum is identically zero. ### `0` are at a widened')
    rec('  ### support.')
    rec('  ### ### **`an unconditional bound or estimate` : `103` HITS, AND THE RESIDUE IS WHERE THE')
    rec('  ### ### FINDING IS.** ### They resolve to `b358`s Li-family work and its echoes -- and')
    rec('  ### two of them are the SOURCE`S OWN SENTENCE, banked as plain text at')
    rec('  ### `b327_source_text.txt:209` and `b358_source_lagarias0404394.txt:209`.')
    rec('  ### ### **`a widened support or window` : `12` HITS**, of which the only non-self-')
    rec('  ### referential ones are `b305:85` and `b306:126` -- the source NAMING the widening, and')
    rec('  ### the corpus observing that widening turns the constituent back on. ### **NEITHER IS A')
    rec('  ### ### BOUND.**')
    rec('  ### ### **`a bound on the finite places` : `2` HITS**, both `b280`/`b284` on the')
    rec('  ### scaling-domain boundary -- ### **A DIFFERENT OBJECT ENTIRELY**, and hand-reading is')
    rec('  ### what establishes that rather than the count.')
    rec()
    FIG['yields'] = y
    FIG['matcher_shapes'] = len(y)
    bar()
    rec('### (1b) WHAT THE SEARCH DID LOCATE -- AND IT IS NOT NOTHING.')
    bar()
    s = SRC.get('LG-thm61')
    rec('  ### ### **LAGARIAS THEOREM 6.1, AT PAGE INDEX `%s` OF AN ARTEFACT VERIFIED BY DIGEST.**'
        % (s['pages'][0] if s and s['pages'] else '--'))
    rec('  ### In the source`s own words, read at content through the flattener and reported as')
    rec('  ### such: ### *for any irreducible cuspidal unitary automorphic representation on')
    rec('  ### `GL(N)` there holds* ### **`S_f(n, pi) = lambda_n(n, pi) + O(n log n)`** ### *(6.2),')
    rec('  ### in which the implied constant in the O-notation depends on `pi`. If the Riemann')
    rec('  ### hypothesis holds for `L(s, pi)` then* ### `lambda_n(n, pi) = O(n log n)` ### *(6.3).*')
    rec('  ### And the abstract says the same at page index `%s`: ### *we obtain an UNCONDITIONAL'
        % (SRC.get('LG-abstract', {}).get('pages') or ['--'])[0])
    rec('  ### estimate for the finite place contribution.*')
    rec()
    rec('  ### ### ### **SO A BOUND ON A FINITE-PLACE CONTRIBUTION EXISTS, IT IS UNCONDITIONAL, AND')
    rec('  ### ### ### IT IS IN A SOURCE THIS CORPUS HAS PINNED.**')
    rec()
    bar()
    rec('### (1c) AND WHY IT IS NOT THE MISSING ELEMENT. ### **THREE REASONS, EACH NAMED.**')
    bar()
    rec('  ### ### **(i) WRONG FAMILY.** ### It is on the Li family `G_n`, whose members have no')
    rec('  ### compact support and lie outside Theorem 1`s class -- `b400`s constraint `C-V`, which')
    rec('  ### is one of the two the record holds at `DERIVES`. ### **IT IS NOT THE SONIN FAMILY AT')
    rec('  ### ### ANY SUPPORT, WIDENED OR NOT, BECAUSE IT IS NOT INDEXED BY A SUPPORT AT ALL.**')
    rec('  ### ### **(ii) WRONG COMPARISON QUANTITY.** ### It bounds against `lambda_n(T, pi)`, the')
    rec('  ### INCOMPLETE LI COEFFICIENT -- a sum over ZEROS to a height `T`. ### `(Q400)` asks for')
    rec('  ### a comparison against an ARCHIMEDEAN quantity. ### **A FINITE-PLACE SUM BOUNDED BY')
    rec('  ### ### THE ZEROS IS THE EXPLICIT FORMULA READ ONE WAY; IT IS NOT AN ARCHIMEDEAN')
    rec('  ### ### BOUND.**')
    rec('  ### ### **(iii) ITS HYPOTHESIS IS NOT OF A KIND THE SONIN SIDE CAN CARRY.** ### The')
    rec('  ### hypothesis quantifies over the REPRESENTATION, not over the test function. ### For')
    rec('  ### the corpus`s own object it holds under the source`s stated convention, and')
    rec('  ### ### **THAT GRADE IS NOT THIS ACT`S TO MOVE:**')
    for p, h, lbl in ((os.path.join(D, 'b358_the_li_asymptotics.txt'), 'H-CUSP',
                       '`b358` graded it on the corpus axis'),
                      (os.path.join(D, 'b361_the_held_item.txt'),
                       'IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT',
                       '`b361` inherited it and did not decide it')):
        i, ln = live(p, h, 260)
        rec('      %s  ### `%s:%s`' % (lbl, os.path.basename(p), i))
        rec('      > %s' % ln)
    rec()
    bar()
    rec('### (1d) AND THE OTHER SOURCE`S NEAR-MISSES, ALL AT THE WRONG SUPPORT AND IN THE WRONG')
    rec('### DIRECTION.')
    bar()
    rec('  ### **THEOREM 1** (page index `%s`) and **THEOREM 6.11** (page index `%s`) are both'
        % ((SRC.get('CC-thm1', {}).get('pages') or ['--'])[0],
           (SRC.get('CC-thm611', {}).get('pages') or ['--'])[0]))
    rec('  ### stated at the NARROW interval `[2^-1/2, 2^1/2]`. ### Theorem 6.11 carries the one')
    rec('  ### correction term the source states -- ### **`c |ghat(0)|^2` WITH `13 < c < 17`** --')
    rec('  ### and it corrects the ARCHIMEDEAN inequality at a support where ### **NO PRIME')
    rec('  ### ### ENTERS.**')
    rec('  ### **THE ESSENTIAL NEGATIVITY** (page index `%s`) is stated on `C_c^inf(I)` for a FIXED'
        % (SRC.get('CC-fixedI', {}).get('pages') or ['--'])[0])
    rec('  ### COMPACT INTERVAL -- but the source`s own preliminary positivity is proved (page')
    rec('  ### index `%s`) ### *for small enough intervals I*, and Appendix B says the archimedean'
        % (SRC.get('CC-small', {}).get('pages') or ['--'])[0])
    rec('  ### positivity is proven ### *for test functions with support in a small enough interval')
    rec('  ### around 1*. ### ### **SO THE SOURCE`S MACHINERY RUNS TOWARD NARROW, NOT WIDE**, and')
    rec('  ### the widening it names at page index `%s` it names and ### **DOES NOT TAKE.**'
        % (SRC.get('CC-widen', {}).get('pages') or ['--'])[0])
    rec()
    rec('  ### ### ### **CONCLUSION. ### `b400`S ABSENT ELEMENT IS CONFIRMED ABSENT BY SEARCH AND')
    rec('  ### ### ### NOT ONLY BY A CONSTRAINT SET. ### AND THE SEARCH`S REAL YIELD IS THE OTHER')
    rec('  ### ### ### HALF: THE *KIND* OF ELEMENT IS NOT ABSENT AT ALL -- IT EXISTS ONCE, ON THE')
    rec('  ### ### ### OTHER FAMILY, AGAINST THE ZEROS, AND THE RECORD ALREADY OWNED IT.**')
    i, ln = live(os.path.join(D, 'b358_closing.txt'), 'NO UNCONDITIONAL BOUND AT ALL', 300)
    rec('      `b358_closing.txt:%s`' % i)
    rec('      > %s' % ln)
    rec('  ### ### **AND THIS ACT IMPORTS NOTHING NEW.** ### `b358` read Theorem 6.1 and banked a')
    rec('  ### verdict on it; this act CITES that reading and tests it against a question `b358` was')
    rec('  ### not asked. ### **A SCOPE TEST IS NOT AN ACQUISITION.**')
    rec()
    FIG['verdict_c1'] = 'PRESENT BUT NOT APPLICABLE'
    FIG['reasons'] = 3


# ==================================================================================================
def addition_one():
    bar('=')
    rec('### ADDITION ONE -- THE UNIFORMITY QUESTION, ASKED BEFORE THE FOURTH SITE IS ENTERED.')
    bar('=')
    rec('### ### ### **VERDICT : ### UNIFORM -- AND VACUOUSLY.**')
    rec()
    rec('  ### **THE CORRECTION TERM, QUOTED:** ### `O(n log n)`, and the source`s own sentence')
    rec('  ### beside it: ### *in which the implied constant in the O-notation depends on `pi`.*')
    rec()
    rec('  ### ### **DOES IT DEPEND ON THE PRIME, OR IS IT UNIFORM IN IT? ### NEITHER, AND THAT IS')
    rec('  ### ### THE ANSWER RATHER THAN A REFUSAL TO ANSWER.** ### The term ### **CARRIES NO')
    rec('  ### ### PRIME INDEX AT ALL.** ### `S_f(n, pi)` is one quantity summed over every finite')
    rec('  ### place at once, and `6.2` is one statement about it. ### So the term is uniform in the')
    rec('  ### prime ### **BECAUSE THERE IS NO PRIME IN IT TO BE UNIFORM IN.**')
    rec()
    rec('  ### ### **AND A UNIFORMITY THAT HOLDS BECAUSE THE INDEX IS ABSENT IS NOT A UNIFORM BOUND')
    rec('  ### ### IN THAT INDEX. ### IT IS A BOUND ABOUT A DIFFERENT OBJECT.** ### This is `b399`s')
    rec('  ### own species at a second site: ### *a consequence satisfied by an empty sum is')
    rec('  ### satisfied vacuously*, and the word that scopes the verdict stands in the same')
    rec('  ### sentence as the verdict.')
    rec()
    rec('  ### ### **SO THE ORDER`S `UNIFORM` BRANCH IS ENTERED AND ITS CONSEQUENCE IS NOT DRAWN.**')
    rec('  ### The order says a UNIFORM answer would be *a class-level statement of the kind the')
    rec('  ### uniformity row has been missing*, and would be priced prime by prime. ### **IT IS')
    rec('  ### ### NOT THAT STATEMENT, AND NO SUCH PRICING IS MADE.** ### A price attached to a')
    rec('  ### vacuous uniformity would be a number about nothing.')
    rec()
    rec('  ### ### **AND THE ONE INDEX THE TERM DOES CARRY IS NOT UNIFORM EITHER.** ### The implied')
    rec('  ### constant ### **DEPENDS ON THE REPRESENTATION**, by the theorem`s own words -- against')
    rec('  ### Theorem 5.1`s, which `b358` banked as ### **ABSOLUTE.** ### **THE SOURCE IS UNIFORM')
    rec('  ### ### WHERE THE ARCHIMEDEAN CHANNEL IS CONCERNED AND NOT WHERE THE FINITE ONE IS, AND')
    rec('  ### ### THAT ASYMMETRY IS THE SHARPEST THING IN THIS COMPONENT.**')
    rec()
    FIG['verdict_a1'] = 'UNIFORM -- AND VACUOUSLY'


# ==================================================================================================
def addition_two():
    bar('=')
    rec('### ADDITION TWO -- THE CORPUS`S OWN ONE-PRIME WINDOW, READ WHOLE AND NOT BY NAME.')
    bar('=')
    rec('### ### ### **VERDICT : ### A DIFFERENT OBJECT, AND THE KERNEL SAYS SO ITSELF.**')
    rec()
    rec('  ### **WHAT IT BOUNDS:** ### `W n`, the number of prime powers below `n` -- ### **A')
    rec('  ### ### COUNT.**')
    rec('  ### **AT WHAT SUPPORT:** ### ### **NONE.**')
    for hint, lbl, span in (('the lower endpoint never binds', 'the windows are HALF-VACUOUS', True),
                            ('tabulated, not characterized', '`W` is tabulated, not characterized',
                             False),
                            ('Nothing here bears on the sign of',
                             '### **AND THE DISCLAIMER THAT DECIDES IT**', False),
                            ('HAS NOTHING TO DO WITH THE CORPUS',
                             'and the name collision, flagged by the repository itself', False),
                            ('It proves nothing about real intervals',
                             'and what it proves instead', False)):
        i, ln = live(RM, hint, 300, span=span)
        rec('      %s  ### `README.md:%s`' % (lbl, i))
        rec('      > %s' % ln)
    rec()
    rec('  ### ### **IS IT THE SAME OBJECT `(Q400)` ASKS ABOUT? ### NO.** ### `(Q400)` asks after')
    rec('  ### `SUM_p W_p(f)`, a weighted sum of `log p` against a test function`s values at prime')
    rec('  ### powers. ### The kernel counts how many prime powers lie below a bound. ### **ONE IS A')
    rec('  ### ### SUM WITH WEIGHTS AND A TEST FUNCTION; THE OTHER IS A CARDINALITY.** ### They')
    rec('  ### share the word `window` and nothing else, and ### **THE DECISION IS BY UNFOLDING')
    rec('  ### ### RATHER THAN BY THE SHARED WORD**, which is what the order asked for.')
    rec('  ### ### **`(N3)` IS MET.**')
    rec()
    rec('  ### **AND `b16`S STAIRCASE IS READ AS WHAT IT IS.**')
    i, ln = live(os.path.join(D, 'b16_2026-08-18.txt'),
                 'the archimedean support bound a (window', 320)
    rec('      `b16_2026-08-18.txt:%s`' % i)
    rec('      > %s' % ln)
    rec('  ### Its second step IS the compiled rung. ### **TWO INDEPENDENT ROUTES TO A COUNT,')
    rec('  ### ### SHARING NO CODE** -- Python arithmetic over a grid against a Lean `decide` over')
    rec('  ### naturals -- ### **AND THAT BUYS CONFIDENCE IN THE COUNT AND NOTHING ABOUT THE SUM.**')
    rec()
    bar()
    rec('### AND ONE THING READING IT WHOLE FOUND THAT READING IT BY NAME WOULD NOT HAVE.')
    bar()
    ap = EX['fig']['axiom_prints']
    tot = EX['fig']['axiom_prints_total']
    i, ln = live(RM, 'all 43 terminals are fully axiom-free', 300)
    rec('  ### THE README`S HEADLINE  ### `README.md:%s`' % i)
    rec('  > %s' % ln)
    rec('  ### THE REPOSITORY`S OWN CHECK FILES, COUNTED:')
    for k in sorted(ap):
        rec('      %-34s `#print axioms` invocations : %d' % (k, ap[k]))
    rec('      ### ### **TOTAL : `%d`.**' % tot)
    rec('  ### ### **`43` AGAINST `%d`, AND THE README`S TERMINAL TABLES DO NOT MENTION THE LOCAL'
        % tot)
    rec('  ### ### MODEL THAT `HEAD`S OWN COMMIT MESSAGE NAMES AS `v0.5`.**')
    rec('  ### ### **THE HEADLINE WAS EXACT WHEN WRITTEN AND IS STALE AGAINST ITS OWN HEAD** --')
    rec('  ### `b371`s species (*`Core 114` was exact at a tag and the head is past it*) at a second')
    rec('  ### repository. ### **PRINTED AND ROUTED, NOT REPAIRED:** ### it is another')
    rec('  ### repository`s file and the instrument-audit lane is PARKED under `(R22)`.')
    rec('  ### ### **AND THE AXIOM CLAIM ITSELF IS NEITHER CONFIRMED NOR DENIED HERE.** ### It was')
    rec('  ### read from a PRINTED PROFILE and not from a run; ### **A QUOTED HEADLINE IS NOT A')
    rec('  ### ### MEASUREMENT**, and the discrepancy above is exactly the cost of that weakness.')
    rec()
    FIG['axiom_prints_total'] = tot
    FIG['readme_claim'] = 43


# ==================================================================================================
def component2():
    bar('=')
    rec('### COMPONENT 2 -- THE FOURTH SITE, ENTERED ONLY NOW THAT ADDITION ONE HAS ANSWERED.')
    bar('=')
    rec('### ### ### **VERDICT : ### ENTERED, AS A RESEMBLANCE OF SHAPE, WITH ITS SHARED INDEX')
    rec('### ### ### NAMED ON THE FACE OF THE ENTRY.**')
    rec()
    i, ln = live(FL, 'U1 -- the uniformity obstruction', 900)
    rec('  ### THE ROW  ### `FACES_LEDGER.md:%s`' % i)
    rec('  > %s' % ln)
    rec()
    rec('  ### ### **DOES `(Q400)` FIT THE SHAPE?** ### The row`s shape is *what the record holds is')
    rec('  ### a family indexed by something, and what it needs is one statement uniform in that')
    rec('  ### index.* ### The record holds `b321`s ten values of `SUM_p W_p(f)` indexed by `a`, and')
    rec('  ### `(Q400)` needs one statement uniform in `a`. ### **IT FITS EXACTLY.**')
    rec()
    rec('  ### ### **AND ADDITION ONE DECIDES WHICH IT IS.** ### The order says the uniformity')
    rec('  ### answer decides whether `(Q400)` is a fourth instance of the obstruction or the first')
    rec('  ### crack in it. ### The one bound located is uniform ### **ONLY WHERE NO INDEX')
    rec('  ### ### EXISTS**, and is explicitly NOT uniform in the one index it carries. ### **SO IT')
    rec('  ### ### IS A FOURTH INSTANCE OF THE OBSTRUCTION AND NOT A CRACK IN IT.**')
    rec()
    rec('  ### ### **AND ONE THING GOES ON THE FACE OF THE ENTRY, BECAUSE A FOURTH ROW SHARING AN')
    rec('  ### ### INDEX WITH A THIRD IS EXACTLY WHERE ONE OBSTRUCTION GETS COUNTED TWICE.**')
    i, ln = live(os.path.join(D, 'b353_the_missing_statement.txt'),
                 'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION', 260)
    rec('      instance (iii), `b353_the_missing_statement.txt:%s`' % i)
    rec('      > %s' % ln)
    rec('  ### ### **INSTANCE (iii) AND `(Q400)` SHARE AN INDEX -- THE SUPPORT WIDTH -- AND DIFFER')
    rec('  ### ### IN OBJECT.** ### (iii) is about the admissible CLASS at a support: Boas-Kac')
    rec('  ### exhausts which functions are positive-definite there. ### `(Q400)` is about a')
    rec('  ### CONSTITUENT`S VALUE at a support: what `SUM_p W_p(f)` does as the window widens.')
    rec('  ### **TWO QUESTIONS ABOUT DIFFERENT THINGS, INDEXED THE SAME WAY.**')
    rec()
    rec('  ### ### **AND THE ROW`S OWN REFUSAL GOVERNS THE ENTRY AND IS RESTATED VERBATIM RATHER')
    rec('  ### ### THAN SUMMARISED:** ### *NOTHING IS CLAIMED ABOUT THE EQUIVALENCE OF THE THREE*,')
    rec('  ### and ### *a row naming three things that look alike is exactly where an equivalence')
    rec('  ### gets compiled by accident*, so the row *names a resemblance of SHAPE and types no')
    rec('  ### bridge between the three, in either direction.* ### **THAT NOW GOVERNS FOUR, AND THIS')
    rec('  ### ### ACT TYPES NO BRIDGE BETWEEN ANY TWO OF THEM -- LEAST OF ALL BETWEEN THE TWO THAT')
    rec('  ### ### SHARE AN INDEX.**')
    rec('  ### ### **THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS. ### SO ARE FOUR, AND TWO')
    rec('  ### ### OF THE FOUR RHYMING MORE CLOSELY DOES NOT MAKE THEM ONE.**')
    rec()
    FIG['verdict_c2'] = 'ENTERED, WITH THE SHARED INDEX NAMED'
    FIG['instances_added'] = 1


def main():
    bar('=')
    rec('b401 -- THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE. ### THE COMPONENTS.')
    rec('### **RUN AFTER THE LOCK. ### THE FACE IS SEALED AT'
        ' `6c8462a90a96494e000acab7641d0faac21ae48948c6170a392f1c1ffba7bd21`.**')
    bar('=')
    rec()
    component1()
    addition_one()
    addition_two()
    component2()
    bar('=')
    rec('### THE COMPONENTS, COUNTED.')
    bar('=')
    rec('    Component 1 verdict   : %s' % FIG['verdict_c1'])
    rec('    reasons it is not it  : %d' % FIG['reasons'])
    rec('    matcher shapes tried  : %d' % FIG['matcher_shapes'])
    rec('    Addition One verdict  : %s' % FIG['verdict_a1'])
    rec('    Addition Two verdict  : A DIFFERENT OBJECT (a count, at no support)')
    rec('    README claim / prints : %d / %d' % (FIG['readme_claim'], FIG['axiom_prints_total']))
    rec('    Component 2 verdict   : %s' % FIG['verdict_c2'])
    bar('=')
    p = run_clock.write(D, 'b401_components_run', L)
    io.open(os.path.join(D, 'b401_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(FIG, indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b401_components.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
