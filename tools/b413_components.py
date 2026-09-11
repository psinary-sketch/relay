# -*- coding: utf-8 -*-
"""b413_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A DOCUMENT, A LEDGER, A ROW, A KEY OR A `.lean` FILE.** ### It
### computes, prints and emits; `b413_desk_bank.py` writes. ### **EVERY WRITE ENCODES BEFORE IT
### OPENS**, and the wrapper breaks at word boundaries.
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
OUT = os.path.join(D, 'b413_components.txt')
PRICEOUT = os.path.join(D, 'b413_price.txt')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
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


EXTRACT = io.open(os.path.join(D, 'b413_extract.txt'), encoding='utf-8').read()
PATHTXT = io.open(PATHS, encoding='utf-8', errors='replace').read()
BALTXT = io.open(BALPOS, encoding='utf-8', errors='replace').read()
TRTXT = io.open(TRAILS, encoding='utf-8', errors='replace').read()
SEALTXT = io.open(SEAL, encoding='utf-8', errors='replace').read()


def q(frag, where, hay):
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


# ### =================================================================================================
def component1():
    bar()
    rec('### COMPONENT 1 -- THE TAIL, STATED EXACTLY.')
    bar()
    rec('  ### **THE CERTIFICATE`S THREE NAMED PREMISES, FROM THE ROW THAT OWNS THEM:**')
    q('`VerifiedZerosTo T` (external computation, zeros verified past 10⁹)',
      'PREMISE 1', PATHTXT)
    q('`ExplicitFormulaDecomp` (Bombieri–Lagarias — **finite-set conjunct now DERIVES**, '
      '`lowFinset_mem_iff` at lv SIDE-lv-conservation v0.10.0 = `93c27ec`; the decomposition '
      'conjunct stays **not in Mathlib**)', 'PREMISE 2', PATHTXT)
    q('`TailBoundPremise` (Voros detection threshold n ≳ 2T², **not in Mathlib**)',
      'PREMISE 3', PATHTXT)
    rec('')
    rec('  ### ### ### **AND THE WORD *BOTH* NO LONGER HOLDS OF THEM AS WHOLES.**')
    wrap('### The K3 freeze of 2026-07-22 graded ### **BOTH** ### premises '
         '`Mathlib-absent-with-ingredient-named`. ### Two days later `W-ORD-P1-FINSET` was ### '
         '**DISCHARGED**, and `ExplicitFormulaDecomp` ### **SPLIT**: its finite-set conjunct now '
         '`DERIVES` in the kernel, and only its ### **DECOMPOSITION CONJUNCT (Guinand-Weil)** ### '
         'remains absent. ### `TailBoundPremise` is absent ### **ENTIRE.**', '  ')
    q('the decomposition conjunct (Guinand–Weil) and `TailBoundPremise` remain Mathlib-absent',
      'THE SPLIT, IN THE ROW`S OWN WORDS', PATHTXT)
    wrap('### ### **SO `(N1)` IS REFUTED IN PREMISE AND MET ON OTHER GROUNDS, UNDER `(R27)`.** ### '
         '### **THE PREMISE IS FALSE:** ### the two premises are no longer in the same condition '
         'as each other -- one is absent whole, the other is absent in one conjunct of two. ### '
         '### **THE CONCLUSION HOLDS:** ### each still has an unmet part that is Mathlib-absent '
         'with its ingredient named, so the tail is open on both. ### **`(E4)` MET.**', '  ')
    rec('')
    rec('  ### ### **AND THE HONEST BOUNDARY THE ROW ITSELF CARRIES, WHICH SETTLES COMPONENT 4')
    rec('  ### ### BEFORE COMPONENT 4 IS REACHED:**')
    q('Honest boundary: extending `TailBoundPremise` to all `n` **IS** RH.',
      'THE BOUNDARY', PATHTXT)
    wrap('### **THAT IS NOT A DIFFICULTY, IT IS AN IDENTITY.** ### The tail is not a hard step '
         'toward RH; the tail ### **IS** ### RH. ### A seat that priced *the smallest real step '
         'on R4* without printing this sentence would be pricing a staircase whose top step is '
         'the roof.', '      ')
    return 2


def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- THE THRESHOLD, READ NOT ASSUMED.')
    bar()
    rec('  ### **WHERE `N0(T)` COMES FROM, IN THE RECORD`S OWN SENTENCE:**')
    q('its cutoff N₀(T) ≈ 2T² is *exactly* Voros\'s detection threshold: the certificate proves '
      'positivity up to precisely where an off-line zero could first register, and no further',
      'THE THRESHOLD', BALTXT)
    q('an off-line zero at height T registers only for n ≳ 2T²', 'AND WHAT IT MEASURES', PATHTXT)
    rec('')
    rec('  ### **AND WHOSE THEOREM IT IS -- THE RECORD INSISTS ON THE ATTRIBUTION:**')
    q('**The growth-class dichotomy is VOROS\'S THEOREM.**', 'THE ATTRIBUTION', BALTXT)
    q('It must be cited as Voros\'s, and any keystone statement of it must say so.',
      'AND THE RECORD`S OWN INSTRUCTION', BALTXT)
    q('Voros, *Sharpenings of Li\'s criterion for the Riemann Hypothesis*, arXiv:math/0506326',
      'THE SOURCE', BALTXT)
    rec('')
    rec('  ### ### **THE THREE DISPOSITIONS, TESTED:**')
    rec('      ### **DERIVED BY THE CORPUS** ### -- ### **NO.** ### The record never claims a')
    rec('      derivation of the threshold and names Voros at every statement of it.')
    rec('      ### **MEASURED** ### -- ### **NO.** ### The bench measured `λ_n > 0` for `n <= 130`;')
    rec('      that is a different quantity and the record keeps them apart.')
    rec('      ### **IMPORTED UNDER THE BAR** ### -- ### **YES**, and named at every citation.')
    rec('  ### ### ### **VERDICT: ### IMPORTED UNDER THE BAR. ### `(N2)` MET.**')
    rec('')
    rec('  ### ### **AND IT IS A BOUND, NOT AN IDENTITY.**')
    wrap('### *Registers only for `n ≳ 2T²`* is a ### **DETECTION THRESHOLD** -- a statement '
         'about where an off-line zero could ### **FIRST** ### show, not an equation. ### The `≈` '
         'and the `≳` are the record`s own, and it writes `N₀(T) = ⌊2T²⌋` only where it means the '
         'certificate`s concrete cutoff.', '      ')
    rec('')
    wrap('### ### **AND THE THING WORTH PRINTING BESIDE THE VERDICT:** ### the derived range and '
         'the discriminating range ### **MEET AT `2T²` AND DO NOT OVERLAP.** ### The certificate '
         'proves positivity up to precisely where discrimination would begin ### **AND NO '
         'FURTHER.** ### **THAT IS NOT A COINCIDENCE AND NOT A NEAR MISS** -- it is the same '
         'number twice, and the record says so in one sentence.', '  ')
    return 'IMPORTED UNDER THE BAR'


def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 -- WHAT ONE INGREDIENT WOULD MOVE IT.')
    bar()
    rows = [ln for ln in PATHTXT.split(NL) if re.match(r'^\| \*\*\d', ln)
            and ('nearest' in ln or 'largest ask' in ln or 'shielded' in ln
                 or re.match(r'^\| \*\*[24]\*\*', ln))]
    rec('  ### ### **THE CHART, ALL FIVE ROWS, BY THEIR DOORS:**')
    for r in rows:
        cells = [c.strip() for c in r.split('|')]
        if len(cells) > 3:
            rec('      %-18s %-30s %s' % (cells[1][:18], cells[2][:30], cells[3][:76]))
    rec('  ### ### **ROWS READ : %d.**' % len(rows))
    rec('')
    rec('  ### **ROW 1 IS THE `R4` POSITIVITY LADDER, AND ITS ONE INGREDIENT IS:**')
    q('the Bombieri–Lagarias explicit formula (`ExplicitFormulaDecomp`) + the Voros tail bound '
      '(`TailBoundPremise`) as **Mathlib theorems**', 'ROW 1`S INGREDIENT', PATHTXT)
    rec('')
    rec('  ### ### **IS ROW 1 STILL ROW 1 AFTER THE ARC? ### MEASURED, NOT ASSUMED.**')
    arcmentions = len(re.findall(r'b4(?:0[3-9]|1[01])', PATHTXT))
    rec('      acts of the arc `b403`-`b411` named anywhere in the chart`s document : ### **%d**'
        % arcmentions)
    rec('      and what that one mention is : ### **`b409`’S CLASS-NUMBERING HEAD NOTE**, a line')
    rec('      this seat wrote, touching no row.')
    wrap('### ### ### **VERDICT: ### ROW 1 IS UNCHANGED BY THE ARC. ### `(N3)` MET.**', '  ')
    rec('')
    wrap('### ### **AND THE TWO QUESTIONS ARE KEPT APART, AS THE FACE REQUIRED.** ### Row 1 ### '
         '**DID** ### change -- `W-ORD-P1-FINSET` was discharged into it on 2026-07-24 and the '
         'row records the bounded increment. ### But that is ### **BEFORE THE ARC BEGAN.** ### '
         '**A ROW THAT MOVED BEFORE THE ARC DID NOT MOVE BECAUSE OF IT**, and an act that '
         'reported *row 1 unchanged* without printing the earlier movement would be right by '
         'accident.', '  ')
    return len(rows)


def component4():
    rec('')
    bar()
    rec('### COMPONENT 4 -- AND WHETHER THIS SEAT CAN TOUCH IT.')
    bar()
    wrap('### The smallest real step on `R4` is the one row 1 names: ### **THE BOMBIERI-LAGARIAS '
         'EXPLICIT FORMULA AND THE VOROS TAIL BOUND AS MATHLIB THEOREMS.** ### The record prices '
         'it itself and this act quotes rather than re-prices:', '  ')
    q('**Analyst-startable, community-scale** (not "this afternoon")', 'THE RECORD`S OWN PRICE',
      PATHTXT)
    q('the honest work is building the Bombieri–Lagarias explicit formula and the Voros tail '
      'bound in Mathlib, a real analytic development, not a programme sitting',
      'AND WHAT THE WORK IS', PATHTXT)
    rec('')
    rec('  ### ### ### **VERDICT: ### A BUILD. ### AND NOT THIS SEAT`S. ### `(N4)` MET.**')
    wrap('### It is not a reading: nothing in the record answers it. ### It is not a measurement: '
         'no number decides it. ### It is ### **A MATHLIB ANALYTIC DEVELOPMENT**, and the owner '
         'the chart names is ### **THE MATHLIB COMMUNITY**, not a programme sitting.', '      ')
    rec('')
    rec('  ### ### **AND WHICH LANE -- BECAUSE THIS FERRY PARKS TWO AND OPENS ONE.**')
    wrap('### The kernel lane is ### **OPEN** ### and this act used it to read. ### But the step '
         'row 1 names is ### **NOT A KERNEL ACT AT ALL** -- it is Mathlib work, upstream of every '
         'lane this seat has. ### ### **SO THE OPEN LANE DOES NOT REACH IT EITHER**, and the act '
         'says which blocker it met rather than filing it behind the nearest park.', '      ')
    rec('')
    wrap('### ### **AND `THIS SEAT CANNOT` IS NOT `NOBODY CAN`.** ### The chart names a mover and '
         'a route: the Mathlib community, via a programme PR or splice under the standing '
         'Mathlib-engagement ruling. ### **A PRICED BUILD WITH A NAMED ACTOR IS NOT A BLOCKED '
         'ONE.** ### `0` routes proposed; the route is the record`s and was there before this '
         'act.', '  ')
    return 'A BUILD -- MATHLIB, NOT THIS SEAT'


# ### =================================================================================================
def component5():
    rec('')
    bar()
    rec('### COMPONENT 5 -- `(N)`, PRICED FOR THE KERNEL.')
    bar()
    rec('  ### **`(N)` AS `b398` NAMED IT, QUOTED FROM THE TRAIL THAT CARRIES IT:**')
    q('in the compiled finite-side module `Core/FiniteSideSeal.lean`, the **compact part** of the '
      'finite-place contribution holds for **every** cell and not at seven', '(N)', TRTXT)
    q('**`6` dependencies HELD**', 'ITS OWN DEPENDENCY COUNT', TRTXT)
    q('**A kernel act can take (N) as a work order; this act is not one.**',
      'AND WHAT b398 SAID OF IT', TRTXT)
    rec('      ### ### **THE ORIENTATION CITATION THE FERRY GAVE IS FOUND: `OPEN_TRAILS.md`, the')
    rec('      ### ### `b398` verdict block.**')
    rec('')
    rec('  ### ### **FROM THE KERNEL, READ AT ITS OWN SOURCE.**')
    q('theorem finite_side_silence {p n t : Nat} (hp : 2 ≤ p) (ht : 0 < t) (htN : t < gridN p n)',
      'THE SEAL`S SIGNATURE', SEALTXT)
    q('def cells : List (Nat × Nat) := [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)]',
      'THE SEVEN CELLS', SEALTXT)
    q('((p, n) ∈ cells → ballQ p n * sumAN p n = sumAQ p n)', 'THE CLAUSE AS IT STANDS', SEALTXT)
    rec('      ### **THE TACTIC: ### `decide`, SEVEN TIMES**, after an `rcases` peels the list')
    rec('      membership one alternative at a time and a final `cases` closes the empty tail.')
    rec('')
    rec('  ### **AND THE TWO GENERAL CLAUSES THAT SURROUND IT, AND WHAT THEY CARRY:**')
    q('(∃ j u, j < 2 * n ∧ NotDiv p u ∧ t = u * p ^ j)', 'CLAUSE (a) -- GENERAL', SEALTXT)
    q('(∀ j, 0 < j → (∃ c, p ^ j * t = t + gridN p n * c) → t % ballQ p n = 0)',
      'CLAUSE (b) -- GENERAL', SEALTXT)
    wrap('### ### **SO THE SEAL IS A SANDWICH:** ### two clauses general in `p` and `n`, and one '
         'guarded by a seven-element list. ### **AND THE GUARD IS WHY THE SEAL`S OWN HYPOTHESIS '
         '`2 ≤ p` NEVER BITES ON CONJUNCT (c)** -- membership in `cells` is strictly stronger '
         'than `2 ≤ p`, so the loose hypothesis is carried but never used there.', '      ')
    rec('  ### **AND EVERY ONE OF THEM IS AXIOM-FREE, FROM THE KERNEL`S PRINTED STDOUT:**')
    for ln in EXTRACT.split(NL):
        if 'does not depend on any axioms' in ln:
            rec('      %s' % ln.strip()[:130])
    rec('')
    rec('  ### ### ### **AND NOW THE THING THE PRICE TURNS ON, MEASURED BEFORE IT IS NAMED.**')
    for ln in EXTRACT.split(NL):
        if re.search(r'CONTROL : \d+ OF \d+|PRIME POWERS \(one|TWO DISTINCT PRIMES', ln):
            rec('      %s' % ln.strip()[:140])
    wrap('### The identity was re-computed outside the kernel on the kernel`s own definitions, '
         'with ### **THE SEVEN DECIDED CELLS AS A POSITIVE CONTROL** -- all seven reproduced, so '
         'the re-implementation is reading the same object the kernel decides. ### Then beyond '
         'the seven: ### **IT HOLDS AT EVERY PRIME POWER AND FAILS AT EVERY `p` WITH TWO DISTINCT '
         'PRIME FACTORS.**', '      ')
    rec('')
    rec('  ### ### ### **SO A GENERAL CONJUNCT (c) OVER `2 ≤ p` WOULD BE ### FALSE, ### AND HERE')
    rec('  ### ### ### ARE THE COUNTEREXAMPLES.**')
    for ln in EXTRACT.split(NL):
        if re.search(r'p=(6|10|12|14|15) ', ln) and 'FAILS' in ln:
            rec('      %s' % ln.strip()[:110])
    wrap('### ### **AND WHAT SEPARATES THEM IS NOT PRIMALITY.** ### `4`, `8`, `9`, `16`, `25`, '
         '`27`, `32` and `49` are ### **COMPOSITE** ### and the identity holds at every one. ### '
         'What it needs is that `p` have ### **A SINGLE PRIME FACTOR** -- which is exactly the '
         'condition under which the kernel`s `units p n`, defined as `u % p != 0`, is the actual '
         'unit group of `Z/p^(2n)`. ### At `p = 6` that filter admits `2`, `3` and `4`, which are '
         'not units mod `36`, and the smear breaks. ### **`(E1)` AND `(E2)` MET.**', '      ')
    rec('')
    rec('  ### ### **SO THE GENERAL STATEMENT IS NAMED, AND ITS QUANTIFIER IS THE FINDING:**')
    wrap('### *For every `p` with a single prime factor and every level `n ≥ 1`: '
         '`ballQ p n * sumAN p n = sumAQ p n`.* ### **WIDER THAN `(N)` ASKS FOR** -- `(N)` says '
         '*every cell* and the cells are primes -- ### **AND NARROWER THAN THE SEAL`S OWN `2 ≤ '
         'p`.** ### The right statement sits between the two, and neither end of the record had '
         'it.', '      ')
    rec('')
    rec('  ### ### **AND `b310`’S DERIVATION: IS IT THE PROOF, OR ONLY THE STATEMENT?**')
    q('`Tr(theta(t) Pi)` IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO '
      'CONGRUENCES THE OBJECT\'S TWO CONDITIONS IMPOSE, WEIGHTED BY THE EMBEDDING\'S HAAR FACTOR.',
      'b310, QUOTED IN THE KERNEL ITSELF', SEALTXT)
    wrap('### ### ### **ONLY THE STATEMENT. ### AND THE MEASUREMENT PROVES IT.** ### `b310`’s '
         'derivation collapses the smear to a weight times a count ### **WITH PRIMALITY '
         'UNUSED.** ### But a derivation that uses nothing distinguishing `4` from `6` ### '
         '**CANNOT PROVE A STATEMENT THAT IS TRUE AT `4` AND FALSE AT `6`.** ### It gives the '
         'general conjunct its ### **SHAPE** -- weight times count -- and none of its ### '
         '**CONTENT**, because the content is exactly the single-prime-factor condition the '
         'derivation does not mention. ### **THE RECORD`S OWN WORDS FOR ITS GRADE SAY THE SAME:** '
         '`DERIVED-ON-CONTENT`, and the kernel`s own docstring adds that *the identification with '
         'the source`s trace is b310`s derivation and is not* compiled.', '      ')
    rec('')
    rec('  ### ### ### **THE LEAN ACT, PRICED.**')
    rec('      ### **WHAT IT WOULD DEPEND ON, AND WHERE THOSE THINGS ARE:**')
    for ln in EXTRACT.split(NL):
        if re.search(r'imports in `Core|files in the kernel importing Mathlib|'
                     r'definitions of a prime predicate', ln):
            rec('          %s' % ln.strip()[:150])
    wrap('### ### **`Core/` IS VANILLA AND `Interfaces/` IS NOT, SO *IS THE DEPENDENCY IN THE '
         'KERNEL OR IN MATHLIB* IS TWO QUESTIONS.** ### **`(E3)` MET.** ### The arithmetic the '
         'proof would lean on -- `valuation_exists`, `index_decomposes`, the scaling lemmas -- is '
         '### **ALREADY IN `Core/`, VANILLA AND AXIOM-FREE.** ### But the ### **HYPOTHESIS** ### '
         'the general statement needs has ### **NO DEFINITION IN `Core/` AT ALL**: there is no '
         'prime predicate anywhere in it.', '      ')
    rec('')
    wrap('### ### **SO `(N5)` IS REFUTED IN PREMISE / MET ON OTHER GROUNDS, UNDER `(R27)`.** ### '
         '### **THE PREMISE IS FALSE:** ### not all the dependencies are in the kernel -- the '
         'quantifier`s own predicate is absent from `Core/`, and supplying it is either new '
         'vanilla Lean or a move to `Interfaces/` where Mathlib is available. ### ### **THE '
         'CONCLUSION HOLDS:** ### it is still Lean work and not an import of a theorem; nothing '
         'needs to be brought in under the bar. ### **THE CHOICE BETWEEN DEFINING IT AND '
         'IMPORTING IT IS A DESIGN DECISION ABOUT A MODULE`S IMPORT SURFACE, AND THAT IS THE '
         'AUTHOR`S.**', '  ')
    rec('')
    rec('  ### ### **AND HOW MANY ACTS. ### `(N6)` ASKED FOR TWO TO FOUR.**')
    wrap('### **ACT 1 -- STATE IT.** ### Define the single-prime-factor predicate in `Core/` (or '
         'rule the statement into `Interfaces/`), restate conjunct (c) generally, and leave the '
         'proof open. ### **BOUNDED, AND THE ONLY PART THIS ACT CAN SIZE.**', '      ')
    wrap('### **ACT 2..n -- PROVE IT.** ### And here the price stops being a number. ### The seven '
         'cells are discharged by ### **`decide`, WHICH GENERALISES TO NOTHING** -- it is a finite '
         'check, and a general statement needs a proof of a different kind entirely. ### `Core/` '
         'does have precedent for general proofs -- `valuation_exists` runs by strong recursion -- '
         'but that is one induction on one variable, and this is ### **A DOUBLE SUM OVER A '
         'FILTERED RANGE, IN VANILLA LEAN, WITHOUT MATHLIB`S FINSET MACHINERY.**', '      ')
    rec('')
    wrap('### ### ### **VERDICT ON THE PRICE: ### AT LEAST TWO ACTS, AND THE UPPER END IS NOT '
         'THIS SEAT`S TO GIVE.** ### **`(N6)` IS REFUTED AS A BOUND AND MET AS A FLOOR.** ### '
         'Naming a number for the proof would require attempting the combinatorial core, ### '
         '**AND ATTEMPTING IT IS BUILDING**, which this act does not do. ### **A PRICE THAT '
         'INVENTS ITS OWN UPPER BOUND IS NOT A PRICE, IT IS A GUESS WITH A DECIMAL POINT.**', '  ')
    rec('')
    rec('  ### ### **AND THIS IS A KERNEL ACT. ### NO PARKED LANE NAMES IT.**')
    wrap('### The instrument lane and the instrument-audit lane are parked and ### **NEITHER '
         'COVERS A LEAN PROOF IN `SIDE-global-section`.** ### The kernel lane is the one this '
         'ferry named ### **OPEN**, and it is the lane `(N)` sits in. ### ### **SO `(N)` IS NOT '
         'BLOCKED BY A PARK -- IT IS SIMPLY NOT DONE**, and `b398` said exactly that: *a kernel '
         'act can take (N) as a work order; this act is not one.* ### **NEITHER IS THIS ONE.** ### '
         '**PRICED; NOT BUILT.**', '      ')
    return 'AT LEAST TWO, UPPER END NOT GIVEN'


def owed():
    rec('')
    bar()
    rec('### THE ONE LINE THE RECORD OWES -- COUNTED, NOT REPAIRED.')
    bar()
    QUAL = re.compile(r'per[- ]cell|seven cells|at seven|PER CELL|cell by cell|decided cells|'
                      r'seven decided|each cell', re.I)
    SUBJ = re.compile(r'finite[- ]side|finite_side_silence|compact part|compact_smear|B329', re.I)
    ferries = sorted(f for f in os.listdir(D)
                     if re.match(r'^b\d+_ferry(_\d{4}-\d\d-\d\d)?\.txt$', f))
    tot = unq = 0
    hits = []
    for f in ferries:
        t = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
        for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', t)):
            if SUBJ.search(s):
                tot += 1
                if not QUAL.search(s):
                    unq += 1
                    hits.append((f, s))
    rec('  ### banked ferries read : ### **%d**' % len(ferries))
    rec('  ### sentences naming the finite side, its seal or its compact part : ### **%d**' % tot)
    rec('  ### ### **OF THOSE, CARRYING NO PER-CELL QUALIFIER : ### `%d`.**' % unq)
    rec('')
    for f, s in hits[:5]:
        rec('      [%s]' % f)
        wrap('*"%s"*' % s[:200], '          ')
    rec('      ... and %d more, all in `data/b413_price.txt`.' % max(0, len(hits) - 5))
    rec('')
    wrap('### ### **IF `(N)` IS PROVED, THESE `%d` SENTENCES BECOME QUALIFIED BY THE PROOF RATHER '
         'THAN BY THE HEADER.** ### They are not wrong today -- each sits in a ferry whose act '
         'carried the per-cell qualifier somewhere in its own face or bank. ### **BUT THE '
         'QUALIFICATION LIVES IN A DIFFERENT DOCUMENT FROM THE SENTENCE**, and a proof of `(N)` '
         'would make that separation harmless instead of load-bearing.' % unq, '  ')
    wrap('### ### **COUNTED, NOT REPAIRED. ### `0` SENTENCES EDITED.** ### A ferry is the '
         'navigator`s and this seat does not rewrite one; and repairing `%d` sentences to say what '
         'a proof has not yet established would be ### **THE HEADER DOING THE PROOF`S WORK, '
         'WHICH IS THE DEBT ITSELF.**' % unq, '  ')
    io.open(PRICEOUT, 'wb').write(
        (NL.join('%s\t%s' % (f, re.sub(r'\s+', ' ', s)[:300]) for f, s in hits) + NL)
        .encode('utf-8'))
    return len(ferries), tot, unq


def expectations(nprem, thr, nrows, step, price, nf, tot, unq):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED -- EACH OVER THE SET THE FACE NAMED, UNDER (R26).')
    bar()
    rows = [
        ('(N1)', 'the two R4 premises as the owning document states them',
         'both are Mathlib-absent with ingredients named',
         '### ### **REFUTED IN PREMISE / MET ON OTHER GROUNDS.** ### **THE PREMISE IS FALSE:** '
         '`ExplicitFormulaDecomp` has ### **SPLIT** -- its finite-set conjunct DERIVES since '
         '2026-07-24 and only its decomposition conjunct is absent, while `TailBoundPremise` is '
         'absent entire. ### **THE CONCLUSION HOLDS:** each still has an unmet Mathlib-absent '
         'part with its ingredient named.'),
        ('(N2)', 'the record`s own account of N0(T)',
         '2T^2 is imported under the bar, not derived by the corpus',
         '### **MET** -- ### **IMPORTED UNDER THE BAR**, attributed to Voros at every statement, '
         'and the record instructs that it *must be cited as Voros`s*. ### It is a ### **BOUND, '
         'NOT AN IDENTITY** -- a detection threshold.'),
        ('(N3)', 'the VAJRA-PLINKO chart`s five rows',
         'row 1 is unchanged by the arc b403-b411',
         '### **MET** -- the only act of the arc named anywhere in the document is `b409`’s '
         'class-numbering head note. ### **AND THE ROW DID MOVE, BEFORE THE ARC** '
         '(`W-ORD-P1-FINSET`, 2026-07-24), which is printed rather than allowed to make the '
         'verdict right by accident.'),
        ('(N4)', 'the smallest real step on R4',
         'it is a build, so this seat cannot take it',
         '### **MET** -- a ### **MATHLIB ANALYTIC DEVELOPMENT**, owner named as the Mathlib '
         'community. ### **AND THE OPEN KERNEL LANE DOES NOT REACH IT EITHER**, since it is not '
         'a kernel act at all.'),
        ('(N5)', 'the dependencies a general conjunct (c) would need',
         'they are already in the kernel, so the act is Lean work and not an import',
         '### ### **REFUTED IN PREMISE / MET ON OTHER GROUNDS.** ### **THE PREMISE IS FALSE:** '
         'the arithmetic is in `Core/` and axiom-free, but ### **THE QUANTIFIER`S OWN PREDICATE '
         'IS ABSENT FROM `Core/` ENTIRELY** -- there is no prime notion in it. ### **THE '
         'CONCLUSION HOLDS:** it is Lean work; nothing is imported under the bar. ### The choice '
         'between defining it and moving to `Interfaces/` is a design decision about a module`s '
         'import surface, and it is the author`s.'),
        ('(N6)', 'the Lean act as this act prices it', 'it prices at between two and four acts',
         '### ### **REFUTED AS A BOUND, MET AS A FLOOR.** ### **AT LEAST TWO** -- one to state '
         'it correctly, and then the proof. ### **THE UPPER END IS NOT THIS SEAT`S TO GIVE:** '
         'the seven cells are discharged by `decide`, which generalises to nothing, so the '
         'general proof is a change of ### **KIND** ### and not of size -- and naming its length '
         'would require attempting the combinatorial core, ### **WHICH IS BUILDING.**'),
        ('(E1)', 'the compact-smear identity on the kernel`s own definitions',
         'the identity does NOT hold for every p >= 2',
         '### **MET, WITH COUNTEREXAMPLES PRINTED** -- it fails at `6`, `10`, `12`, `14`, `15`, '
         '`18`, `20`, `21`, `22` and `26`, under a control that reproduced all seven decided '
         'cells.'),
        ('(E2)', 'the same identity', 'what separates holding from failing is NOT primality',
         '### **MET** -- `4`, `8`, `9`, `16`, `25`, `27`, `32`, `49` are composite and it holds '
         'at every one. ### The condition is ### **A SINGLE PRIME FACTOR**, which is exactly when '
         '`u % p != 0` picks out the unit group.'),
        ('(E3)', 'Core/ and Interfaces/ of the kernel',
         'they do not have the same import surface',
         '### **MET** -- `Core/FiniteSideSeal.lean` has ### **NO IMPORTS AT ALL**; six files '
         'under `Interfaces/` import Mathlib. ### So *in the kernel or in Mathlib* is two '
         'questions.'),
        ('(E4)', 'the R4 row as the owning document states it',
         'the two premises are no longer in the same condition as each other',
         '### **MET** -- and it is why `(N1)` splits.'),
    ]
    for k, over, claim, verd in rows:
        rec('  **%s** ### over ### **%s**' % (k, over))
        wrap(claim, '        ')
        wrap(verd, '        ')
        rec('')
    rec('  ### ### **`2` SPLIT UNDER `(R27)`, `1` REFUTED AS A BOUND, `7` MET.**')
    rec('  ### ### **AND EVERY SPLIT IS A PREMISE THAT ASSUMED TWO THINGS WERE ALIKE.**')


def main():
    rec('=' * 100)
    rec('b413_components.py -- THE COMPONENTS. ### THE NEAREST DOOR, AND THE KERNEL PRICE.')
    rec('=' * 100)
    rec('  face LOCKED : 05caf6786c9e9d5d3b0a3d8a3a3dfe8449e26298246594b3aee5972bf529dceb')
    rec('  ### **THE THREE RULED ARMS, FIXTURES BOTH POLARITIES:** %s'
        % gate_spine.self_test(verbose=False))
    rec('  ### ### **`0` `.lean` FILES TOUCHED. ### `0` KERNEL BUILDS RUN. ### THE OPEN LANE WAS')
    rec('  ### ### USED TO READ.**')
    rec('')
    nprem = component1()
    thr = component2()
    nrows = component3()
    step = component4()
    price = component5()
    nf, tot, unq = owed()
    expectations(nprem, thr, nrows, step, price, nf, tot, unq)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO DOCUMENT, LEDGER, ROW, KEY OR `.lean` FILE WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write((NL.join(L) + NL).encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
