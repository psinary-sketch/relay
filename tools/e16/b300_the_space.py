# -*- coding: utf-8 -*-
"""b300 -- THE E0 GATE ON THE ARCHIMEDEAN LOCAL SPACE.

### SCOPE, SAID FIRST AND OBEYED THROUGHOUT. ### **THIS FILE DECIDES NOTHING ABOUT THE SPACE.**
### It runs ONE gate: ### **EVERY CONSTITUENT OF THE CONSTRUCTED SPACE IS UNFOLDED TO A NAMED
### OWNER AND ITS WORDING IS PULLED FROM THAT OWNER'S FILE RATHER THAN TYPED.** ### That is what
### E0 has meant since b247: ### *"every constituent unfolded to its owner, quoted from source."*

### ### **WHY THE GATE IS TEXTUAL AND NOT ARITHMETICAL HERE, SAID BEFORE ANYONE ASKS.** ### At
### b279 the same gate ran over `Son(p,n)` in exact integer arithmetic across seven cells, because
### the finite local space is a finite-dimensional space of vectors on `Z/p^{2n}` and membership in
### it is DECIDABLE. ### **THE ARCHIMEDEAN LOCAL SPACE IS AN INFINITE-DIMENSIONAL SUBSPACE OF
### `L^2(R)_ev` CUT OUT BY THE VANISHING OF A FUNCTION AND OF ITS FOURIER TRANSFORM ON AN
### INTERVAL.** ### There is no cell to enumerate and no finite stand-in whose verdict would be
### about the space rather than about the stand-in -- ### **b291 said exactly this about the
### involution and b292 about the subspace argument, and the reason is the same one.**
### ### **SO THE GATE CHECKS WHAT IT CAN CHECK, AND SAYS SO RATHER THAN DRESSING A TEXT CHECK IN
### ### ARITHMETIC.**
"""

# ### THE LIMITS, IN THE HEADER SO THE GATE IS NOT TRUSTED BEYOND THEM:
# ### (1) ### **IT PULLS A LINE; IT DOES NOT READ A PAPER.** ### It proves the corpus's banked
# ###     wording of a constituent is on disk in the file named as its owner. ### **IT CANNOT
# ###     PROVE THAT WORDING IS THE SOURCE'S.** ### Provenance is graded per row and printed.
# ### (2) ### **A CONSTITUENT NOBODY THOUGHT TO LIST IS INVISIBLE TO IT.** ### The table is the
# ###     reach, and the table is the act's judgement, not the tool's.
# ### (3) ### **`OPEN` ROWS ARE PULLED TOO** -- from the owner that RECORDED them open. ### An
# ###     open constituent with no owner would be an act's own assertion wearing a citation, and
# ###     the census counts supplied and open separately so neither can absorb the other.
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')


def d(name):
    return os.path.join(D, name)


B202 = d('b202_sum_test.txt')
B211 = d('b211_alternation_derived.txt')
B212 = d('b212_odd_family.txt')
B214 = d('b214_orientation_bits.txt')
B226 = d('b226_stated_choice.txt')
B285 = d('b285_archimedean_opening.txt')
B286 = d('b286_the_cc_condition.txt')
B287 = d('b287_the_two_papers.txt')
B291 = d('b291_the_involution.txt')
B292 = d('b292_the_identification.txt')
SRC = d('b300_source_read.txt')      # ### THIS ACT'S OWN AT-CONTENT READ, WRITTEN BEFORE THIS RUN

# ### =============================================================================================
# ### THE CONSTITUENTS. ### (label, value-as-constructed, owner file, anchor, status, provenance)
# ### **STATUS IS `SUPPLIED` OR `OPEN`. ### THE CENSUS COUNTS THEM SEPARATELY.**
# ### =============================================================================================
CONSTITUENTS = [
    ("C1  THE UNDERLYING SPACE",
     "L^2(R)_ev -- square integrable EVEN functions on R",
     B286, "of square integrable even", "SUPPLIED",
     "CC 2006.13771, Introduction. ### Banked verbatim by b286, which read it at content;"
     " ### RE-PULLED AT SOURCE THIS ACT and found word-for-word identical (see C2's owner file)"),

    ("C2  THE INNER PRODUCT AND ITS NORMALIZATION",
     "<eta|xi> := (1/2) INT_R eta(x) conj(xi)(x) dx = INT_0^inf eta(x) conj(xi)(x) dx",
     SRC, "We normalize the inner product", "SUPPLIED",
     "CC 2006.13771, SECTION 1, EQUATION (16). ### **READ AT CONTENT THIS ACT.** ### No prior act"
     " in this lane reached it: b285 recorded the inner product OPEN and b287 recorded it ABSENT"),

    ("C3  CONDITION ONE",
     "xi(q) = 0 for all q with |q| <= lambda",
     B287, "xi(q) = 0, for all q, |q| <= lambda", "SUPPLIED",
     "CC 2006.13771, DEFINITION 4.4, equation (72). ### Banked verbatim by b287 from the 57-page"
     " PDF at content. ### NOT re-read this act -- the public render truncates inside section 3"),

    ("C4  CONDITION TWO",
     "(F_eR xi)(p) = 0 for all p with |p| <= mu",
     B287, "(F_eR xi)(p) = 0, for all p, |p| <= mu", "SUPPLIED",
     "CC 2006.13771, DEFINITION 4.4, equation (72), same display as C3"),

    ("C5  THE FIXED SCALE",
     "(lambda, mu) = (1, 1); the cutoff set [-1,1]; the cutoff parameter Lambda set to 1",
     B286, "for cutoff parameter equal to 1", "SUPPLIED",
     "CC 2006.13771, Abstract and text. ### **WHICH PAIR THE KEYSTONE'S 'Connes-Consani scale'"
     " MEANS IS `W-ORD-CC-SCALE-MEANING`, THE AUTHOR'S RULING** -- b287 sharpened it to WHICH"
     " PAIR, and this row carries the source's value, not the keystone's intention"),

    ("C6  THE TRANSFORM",
     "F_eR on L^2(R)_ev: preserves the space globally, and is its own inverse there",
     B291, "is its own inverse", "SUPPLIED",
     "CC 2006.13771, immediately after equation (69). ### Banked verbatim by b291, hypotheses"
     " (space, even restriction, kernel convention) checked and shown there. ### The"
     " preservation clause was RE-PULLED AT SOURCE THIS ACT (see C2's owner file)"),

    ("C7  THE PROJECTION ONTO THE SPACE",
     "S, the orthogonal projection; and R = S, with S(1,1) the eigenspace of P P^ P at 1",
     B287, "orthogonal projection on Sonin", "SUPPLIED",
     "CC 2006.13771, section 4's spectral decomposition. ### Banked verbatim by b287."
     " ### **THIS IS THE ROW THAT MAKES THE SPACE CLOSED, AND CLOSEDNESS IS WHAT R1 BELOW NEEDS**"),

    ("C8  THE SIZE",
     "infinite dimensional",
     B286, "infinite dimensional Sonin", "SUPPLIED",
     "CC 2006.13771, Introduction. ### Banked verbatim by b286"),

    ("C9  THE REAL FIBER'S PLACEMENT IN THE CORPUS'S ADELIC OBJECT",
     "how the real fiber sits inside the corpus's own adelic object -- N-OPEN-B as b287 read it",
     B287, "REMAINS OPEN", "OPEN",
     "### **(ABSENT) FROM BOTH SOURCES AND FROM THE DEFERRED REFERENCE**, b287, against a"
     " positive control. ### C2 supplies the LOCAL space's own normalization; ### **IT DOES NOT"
     " SUPPLY THIS, AND A SOURCE CANNOT ANSWER A QUESTION ABOUT A CONSTRUCTION IT NEVER SAW**"),
]

# ### =============================================================================================
# ### WHAT THE PRODUCT CONSTRUCTION REQUIRES OF A LOCAL SPACE. ### **QUOTED FROM ITS OWN
# ### REQUIREMENTS, VIA THE ACT THAT READ von NEUMANN 1939 AT THE SOURCE DOCUMENT (b226).**
# ### (label, requirement, owner, anchor, met?, why)
# ### =============================================================================================
REQUIREMENTS = [
    ("R1  A HILBERT SPACE AT EVERY INDEX",
     "Definition 4.1.1 builds the product from the spaces H_a, one per index",
     B226, "H_a be the closed", True,
     "### **MET.** ### C7 gives an ORTHOGONAL PROJECTION onto S(1,1) inside L^2(R)_ev, so S(1,1)"
     " is a CLOSED subspace of a Hilbert space, hence a Hilbert space in the inherited inner"
     " product -- and C2 says which inner product that is, in the source's own normalization."
     " ### **CLOSEDNESS IS NOT ASSUMED FROM THE WORD 'SPACE'; IT IS READ OFF C7.**"),

    ("R2  A NORM, AND A NORM-ONE VECTOR",
     "Lemma 4.1.2 is stated for a C0-sequence with ||f_a|| = 1",
     B226, "with ||f_a|| = 1", True,
     "### **THE NORM: MET** -- it is C2's inner product's norm, and R1 makes it complete."
     " ### **THE VECTOR: NOT DECIDED HERE.** ### Whether the corpus's chosen archimedean unit is"
     " a vector OF THIS SPACE is Component 2's question and this gate does not pre-empt it"),

    ("R3  THE C0 CONDITION ACROSS THE PLACES",
     "the demand that SUM_v | ||f_v|| - 1 | converge",
     B226, "SUM_v | ||f_v|| - 1 | CONVERGE", None,
     "### **NOT THIS ACT'S TO DECIDE.** ### It is a condition on the SEQUENCE across all places,"
     " not on one local space. ### b226 ran it as G-NORM and passed it BY CONSTRUCTION at its own"
     " grade; ### **that grade is carried, not re-earned, and this row is marked neither met nor"
     " unmet because it is not a property of the archimedean fiber**"),
]

CONDITIONAL_ON = (
    "### **C9. ### THE CONSTRUCTION IS STATED CONDITIONALLY ON IT AND IS NOT SILENTLY COMPLETED.**"
    " ### C2 answers what the LOCAL space's inner product IS; ### **whether that normalization is"
    " the one the corpus's adelic object wants of its real fiber is C9, and no owner states it.**")


def census():
    sup = [c for c in CONSTITUENTS if c[4] == 'SUPPLIED']
    opn = [c for c in CONSTITUENTS if c[4] == 'OPEN']
    return sup, opn


def self_test(verbose=True):
    """### **BOTH POLARITIES.**

    ### POSITIVE: every declared anchor pulls from the file declared as its owner.
    ### ### **NEGATIVE (THE DISCRIMINATION ARM): AN ALTERED ANCHOR MUST COME BACK UNPULLABLE.**
    ### A puller that never misses is not pulling, and b299's own suite had to write this arm
    ### against exactly that.
    ### THIRD: the census must not let an OPEN row be counted as supplied.
    """
    ok = True
    if verbose:
        print('  %-46s %s' % ('fixture', 'result'))
    # ### the discrimination arm, built by MUTATING each real anchor rather than by inventing one
    for lbl, _v, path, anchor, _s, _p in CONSTITUENTS + [(r[0], '', r[2], r[3], '', '')
                                                         for r in REQUIREMENTS]:
        bad = anchor[:-1] + 'Z~'
        try:
            needle_pull.pull(path, bad)
            ok = False
            if verbose:
                print('  %-46s ### NO ### (mutated anchor still pulled)' % lbl[:46])
        except LookupError:
            if verbose:
                print('  %-46s YES (mutated anchor is unpullable)' % lbl[:46])
    sup, opn = census()
    third = (len(sup) + len(opn) == len(CONSTITUENTS)) and len(opn) >= 1
    ok = ok and third
    if verbose:
        print('  %-46s %s' % ('census keeps SUPPLIED and OPEN disjoint',
                              'YES' if third else '### NO ###'))
    return ok


def main():
    print('=' * 100)
    print('b300 -- THE E0 GATE ON THE ARCHIMEDEAN LOCAL SPACE.')
    print('=' * 100)
    print('\n  SELF-TEST (the discrimination arm: every anchor mutated must go unpullable):')
    if not self_test():
        print('\n  ### REFUSING TO REPORT A GATE FROM A PULLER THAT FAILS ITS OWN FIXTURES.')
        return 2

    fails = []
    print('\n' + '-' * 100)
    print('  THE CONSTITUENTS, EACH UNFOLDED TO ITS OWNER AND PULLED FROM THE OWNER\'S FILE.')
    print('-' * 100)
    for lbl, value, path, anchor, status, prov in CONSTITUENTS:
        try:
            line = needle_pull.pull(path, anchor)
            mark = 'PULLED'
        except LookupError:
            line, mark = '', '### UNPULLABLE ###'
            fails.append(lbl)
        print('\n  %s   [%s]  %s' % (lbl, status, mark))
        print('      AS CONSTRUCTED : %s' % value)
        print('      OWNER          : %s' % os.path.basename(path))
        print('      PULLED LINE    : %s' % line[:150])
        print('      PROVENANCE     : %s' % prov)

    sup, opn = census()
    print('\n' + '-' * 100)
    print('  THE CENSUS. ### SUPPLIED and OPEN counted separately so neither absorbs the other.')
    print('-' * 100)
    print('    constituents listed : %d' % len(CONSTITUENTS))
    print('    SUPPLIED            : %d   %s' % (len(sup), ', '.join(c[0].split()[0] for c in sup)))
    print('    OPEN                : %d   %s' % (len(opn), ', '.join(c[0].split()[0] for c in opn)))
    print('    unpullable          : %d   %s'
          % (len(fails), 'PASS' if not fails else '### FAIL ###'))

    print('\n' + '-' * 100)
    print('  WHAT THE PRODUCT CONSTRUCTION REQUIRES OF A LOCAL SPACE -- QUOTED FROM ITS OWN')
    print('  REQUIREMENTS (von Neumann 1939, via b226\'s at-source read of the numdam extract).')
    print('-' * 100)
    for lbl, req, path, anchor, met, why in REQUIREMENTS:
        try:
            line = needle_pull.pull(path, anchor)
            mark = 'PULLED'
        except LookupError:
            line, mark = '', '### UNPULLABLE ###'
            fails.append(lbl)
        verdict = {True: 'MET', False: '### NOT MET ###', None: 'NOT THIS ACT\'S'}[met]
        print('\n  %s   [%s]  %s' % (lbl, verdict, mark))
        print('      THE REQUIREMENT : %s' % req)
        print('      PULLED LINE     : %s' % line[:150])
        print('      READ AGAINST THE CONSTRUCTION : %s' % why)

    print('\n' + '-' * 100)
    print('  THE CONSTRUCTION IS CONDITIONAL ON:')
    print('-' * 100)
    print('    %s' % CONDITIONAL_ON)

    print('\n' + '=' * 100)
    print('  ### E0: %d constituent(s) unfolded, %d unpullable. ### %s'
          % (len(CONSTITUENTS) + len(REQUIREMENTS), len(fails),
             'PASS' if not fails else '### FAIL ###'))
    print('  ### **AND THE GATE\'S REACH, PRINTED WITH ITS RESULT: IT PROVES THE WORDING IS ON')
    print('  ### DISK IN THE FILE NAMED AS ITS OWNER. ### IT DOES NOT PROVE THE WORDING IS THE')
    print('  ### SOURCE\'S -- THAT IS THE PROVENANCE COLUMN, AND THE PROVENANCE COLUMN IS PROSE.**')
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
