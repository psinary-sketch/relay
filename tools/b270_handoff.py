# -*- coding: utf-8 -*-
"""b270_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE AMBIENT PAIRING'S PROPERTIES (b270)"
PRIOR_MARK = u"(b269)"

NEW = (
    u"*** ### ### **C1 IS STRUCK. ### VERDICT: (DEAD), BY DERIVATION AND NOT BY RULING.** ### "
    u"`RULE M2-ACT4: D` said C1's ruling is taken only if the derivation supports it and C1 is "
    u"struck if the derivation refutes it; ### **THE DERIVATION REFUTES IT, SO THE SECOND HALF "
    u"FIRED AND NOTHING IS ROUTED BACK.** ### **NO CANDIDATE IS ADOPTED. ### M-2 REMAINS ### "
    u"SPECIFIED-NOT-STATED ### . ### THE FORK IS THREE: C2 / C3 / C4.** *** "
    u"### ### **S1 -- THE PROJECTION DOES NOT VANISH, AND THE NAVIGATOR'S ONE-LINE REFUTATION "
    u"WAS TESTED AND IS ITSELF REFUTED.** ### `S_quot u_v` is NONZERO at all eight cells, and at "
    u"the seven level-1 cells ### **IT EQUALS `u_v` EXACTLY** ### : b268's zero set of `u_v` is "
    u"the multiples of `q`, which at `n = ell(p)` IS the ball, so `u_v` already meets b10's "
    u"\u201cSONIN-TYPE CONDITION TRANSPOSED: support off the ball (the ball-avoidance half)\u201d; "
    u"and at level 1 no off-ball `m` has `pm` off-ball, so `V_inv`'s orbit relation is EMPTY and "
    u"`S_quot` is multiplication by the off-ball indicator. ### **C1 THEREFORE DIED FURTHER DOWN "
    u"THAN THE ONE-LINE ARGUMENT WOULD HAVE KILLED IT, WHICH IS WHY THE ROUTE WAS RUN.** *** "
    u"### ### **S4 -- (SPEC-1) IS REFUTED. ### THE PAIRING IS EXACTLY ZERO AT `k = n`, AT EVERY "
    u"CELL.** ### From the ambient operator's own definition, `P(k) = p^{-k/2} \u03a3_m (S_quot "
    u"u_v)(m) conj(u_v(p^k m))`; at `k = n` the index `p^n m` is a multiple of `p^n` FOR EVERY "
    u"`m` \u2014 that is the ball \u2014 and `u_v` vanishes there, so ### **EVERY SUMMAND CARRIES "
    u"A ZERO FACTOR.** ### act 9's expression also dies at `k >= n`, but ### **BY A DIFFERENT "
    u"MECHANISM: ITS OWN ARITHMETIC, NOT AN ABSORPTION. ### THE AGREEMENT OF RANGES IS A FACT "
    u"ABOUT RANGES AND IS NOT REPORTED AS AN IDENTITY OF OBJECTS.** *** "
    u"### ### **AND THE ABSORPTION REACHES PAST C1: ### `Tr(U^n S_quot) = 0` TOO.** ### `S_quot` "
    u"is zero on ball columns and `p^n m` is always in the ball, so the CHOICE-FREE ambient trace "
    u"is empty at `k = n` as well \u2014 ### **DROPPING `u_v` DOES NOT RESCUE THE ROUTE.** ### "
    u"Scope stated as precisely as the finding: this is about the TRUNCATED MODEL's ambient "
    u"operators at `k = n`, controlled at eight cells; ### **b10's OWN REGISTERED MODEL "
    u"LIMITATION STANDS BESIDE IT UNTOUCHED, AND b10 IS CORROBORATED, NOT RE-VERDICTED.** *** "
    u"### ### **S3 -- (SPEC-2) IS REFUTED TWICE.** ### At SEVEN of eight cells the range "
    u"`1 <= k <= n-1` ### IS EMPTY ### , because b226 puts the unit at level 1 \u2014 ### **THE "
    u"SPEC IS VACUOUS THERE, NOT SATISFIED THERE.** ### At the one testable cell `(2,2)`, `k=1`, "
    u"the pairing is `(64/3)(1 + \u221a2)` against act 9's `2/3`: ### **THEY DIFFER IN KIND, NOT "
    u"IN VALUE \u2014 ONE IS IRRATIONAL AND THE OTHER IS RATIONAL, AND NO NORMALISATION CLOSES "
    u"THAT.** ### Certified by the same reduction modulo `\u03a6_N` that took every verdict. ### "
    u"And structurally: ### **THE PAIRING CARRIES NO `n` AND `\u0398_q`'s TERM VARIES WITH `n`.** *** "
    u"### ### **THE DOUBLE-NAME HAZARD WAS SETTLED BY MEASUREMENT, NOT BY ASSERTION.** ### At "
    u"`(2,2)` `k=1` the pairing is `(64/3)(1+\u221a2)` and b10's trace is `8/3`. ### **A MATRIX "
    u"ELEMENT IS NOT A TRACE**, and b269's stated risk \u2014 that a C1 ruling ### \u201cwould "
    u"have to say why this one is not that\u201d ### \u2014 ### **IS DISCHARGED WITHOUT ANY SUCH "
    u"SAYING: THE CANDIDATE IS REFUTED ON ITS OWN ARITHMETIC, WHICH IS CHEAPER AND STRONGER.** *** "
    u"### ### **THE SHADOW WAS BUILT, AND THE CONDITION WAS CHECKED BEFORE BUILDING IT.** ### "
    u"`Core/BallAbsorptionShadow.lean`, vanilla Lean 4, `decide` only: ### **11 POSITIVE "
    u"TERMINALS + 4 POLARITY REFUSALS, ALL PRINTING \u201cdoes not depend on any axioms\u201d, "
    u"REPORTED FROM THE PRINTED PROFILE**, with the prints IN the banked file and the flip test "
    u"exiting 1. ### b269 built nothing and quoted the reason; ### **THE STANDARD DID NOT CHANGE "
    u"\u2014 THE CONTENT DID: the residue is not a stand-in for the mechanism, IT IS the "
    u"mechanism, and it carries a witness that the operator is not dead below `k = n`, WITHOUT "
    u"WHICH IT WOULD ITSELF HAVE BEEN THE DOUBLE-NAME SPECIES.** *** "
    u"### ### **WHAT THE AUTHOR'S RULING WOULD UNLOCK, PER BRANCH, AND THIS SEAT RANKS "
    u"NOTHING.** ### **C2** (a RESULT \u2014 what `S_quot` does to `E_1`) would let b268's A1 "
    u"transfer; without it A1 does not travel. ### **C3** (BOTH) is the only candidate that would "
    u"give a number defined AT `k = n` \u2014 and this act has shown ### **NEITHER AMBIENT OBJECT "
    u"GIVES ONE**, which is an observation about the others and NOT a recommendation of C3. ### "
    u"**C4** (a RULING \u2014 change the unit) ### **CANNOT ESCAPE THIS ACT'S REFUTATION BY "
    u"CHANGING THE UNIT WITHIN `Son(p,n)`**, because the refutation uses only that `u_v` vanishes "
    u"on the ball, which is what MAKES it a Sonin vector. *** "
    u"### ### **THE DEVIATIONS, AND TWO ARE THIS ACT'S OWN GATES FAILING FIRST.** ### The "
    u"distinctness test's first draft ### **HAD NO ARM FOR A NON-RATIONAL PAIRING AND PRINTED "
    u"\u201cTHEY AGREE\u201d OVER THE ONE CELL WHERE THEY DISAGREE**; a gate fixture ### "
    u"**MATCHED THE PAIRING TABLE'S `ZERO` INSTEAD OF THE PROJECTION'S AND SO TESTED NOTHING, AND "
    u"THE HARNESS REFUSED THE CHECK.** ### Both fixed at the source. ### **F-QUOTE FOUND 2 OF 16 "
    u"NEEDLES UNFINDABLE BEFORE EMISSION \u2014 PUNCTUATION, NOT WORDS \u2014 AND THE SEALED "
    u"REGISTRATION WAS LEFT BYTE-IDENTICAL RATHER THAN EDITED.** ### New work-order "
    u"`W-ORD-PREDICATE-ARM`. ### **THE NOISE-FLOOR CHECK IS UNBUILT FOR THE SIXTH ACT RUNNING.** *** "
    u"### ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED.** ### This act "
    u"removed a way of not stating it; ### **THAT IS NOT STATING IT.** ### **NOTHING DEPOSITS. "
    u"### NOTHING CIRCULATES. ### h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]
    assert lead.startswith(PREFIX)
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b269: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b269)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    # ### THIS ACT'S OWN HEADLINE ASSERTIONS, EACH ONE A SENTENCE THE BANK ALSO CARRIES.
    for must in (u"C1 IS STRUCK",
                 u"(DEAD), BY DERIVATION AND NOT BY RULING",
                 u"THE FORK IS THREE",
                 u"THE PAIRING IS EXACTLY ZERO AT `k = n`",
                 u"EVERY SUMMAND CARRIES",
                 u"A MATRIX ELEMENT IS NOT A TRACE",
                 u"THEY DIFFER IN KIND, NOT",
                 u"DROPPING `u_v` DOES NOT RESCUE THE ROUTE",
                 u"CORROBORATED, NOT RE-VERDICTED",
                 u"REPORTED FROM THE PRINTED PROFILE",
                 u"WHAT THE AUTHOR'S RULING WOULD UNLOCK",
                 u"HAD NO ARM FOR A NON-RATIONAL PAIRING",
                 u"THE HARNESS REFUSED THE CHECK",
                 u"NO CANDIDATE IS ADOPTED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    # ### AND THE PRIOR HEADLINES MUST SURVIVE THE DEMOTION, NOT BE REWRITTEN AWAY.
    for kept in (u"M-2 IS NOT STATED",
                 u"HALT-WITH-DOSSIER",
                 u"S_quot = orthoprojection onto",
                 u"b226's OWED STEP IS ### PAID ###",
                 u"THE AGGREGATION'S TERM IS LOCATED",
                 u"STATES GRADES, CONFERS NONE"):
        assert kept in new_lead, "### prior headline lost in demotion: %r" % kept
    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]
    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)
    back = io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2]
    assert back == new_lead
    sys.stdout.write("  prior title : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title   : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length : %d -> %d chars\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  ### DEMOTED, NOT REWRITTEN: every prior headline still present.\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
