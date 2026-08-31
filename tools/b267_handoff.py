# -*- coding: utf-8 -*-
"""b267_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE AGGREGATION'S SOURCE (b267)"
PRIOR_MARK = u"(b266)"

NEW = (
    u"*** ### ### **THE AGGREGATION'S TERM IS LOCATED: IT CANNOT COME FROM THE TRACE SIDE, THE "
    u"DATUM IS ON THE ASSEMBLY SIDE, AND THE BRIDGE BETWEEN THEM IS THE THING STILL OWED.** "
    u"### **M-2 REMAINS ### SPECIFIED-NOT-STATED ### . ### NO AGGREGATION IS ADOPTED, STATED OR "
    u"REALIZED, AND NO FUNCTION SATISFYING SPEC-1/2/3 IS EXHIBITED OR SHOWN TO EXIST.** *** "
    u"### ### **TEST 1 -- THE EXTENSION. ### act 9's CLOSED-FORM ### EXPRESSION ### , EVALUATED "
    u"AT `k = n` RATHER THAN DECLARED OUT OF RANGE, RETURNS ### EXACTLY ZERO BY ITS OWN "
    u"ARITHMETIC** -- the numerator `p^n - p^k` vanishes there, on exact fractions at 30 cells, "
    u"`p in {2,3,5,7,11}`. ### **AND THE HALF THE FERRY DID NOT ASK FOR: AT `k > n` THE "
    u"EXPRESSION IS STRICTLY ### NEGATIVE ### AND DOES NOT AGREE WITH THE SUPPLIED `0`. ### SO "
    u"`0 for k >= n` IS THE EXPRESSION'S OWN VALUE AT `k = n` AND AN ### OVERRIDING CONVENTION ### "
    u"FOR `k > n`.** ### That split is the finding: ### **A CONVENTION COULD BE RE-CONVENTIONED; "
    u"AN ARITHMETIC ZERO CANNOT. ### EXTENDING THE RANGE DOES NOT HELP, RE-INDEXING DOES NOT "
    u"HELP, AND THE AGGREGATION IS NOT A RE-INDEXING OF THE QUOTIENT TRACE.** *** "
    u"### ### **TEST 2 -- THE OBJECT'S OWN FACTOR. ### VERDICT (PARTIAL), AND THE (PARTIAL) IS "
    u"THE WHOLE POINT.** ### The odd law `4 d_1 = (q-1)^2` gives `d_1(p,1) = ((p-1)/2)^2 > 0`, "
    u"and the kernel states it ### for every odd prime `p` and every level `n >= 1` ### at zero "
    u"axioms -- so ### **THE OBJECT IS NOT SILENT WHERE THE CLOSED FORM IS.** ### **BUT b226 "
    u"DRAWS THE LINE THIS ACT MUST NOT BLUR, AND IT IS QUOTED: ### d_1 > 0 GIVES E_1 != 0. ### "
    u"IT DOES NOT GIVE u_{1,1} != 0 ... THE STEP WANTS A RESULT ... THIS ACT DID NOT PERFORM IT "
    u"AND DOES NOT CLAIM IT.** ### The ### SECTOR ### is kernel-general; the ### CHOSEN GENERATOR "
    u"### is six-places-measured and its general nonvanishing is b226's OWED RESULT. ### "
    u"**CALLING THIS (SUPPORTED) WOULD HAVE BEEN THIS ACT'S OWN DOUBLE-NAME ERROR, AND THE "
    u"REGISTRATION NAMED THAT TRAP BEFORE THE TEST RAN.** *** "
    u"### **AND A CORRECTION TO THE FERRY'S OWN NUMBER, MADE FROM THE LAW: it carries `d_1 = 1` "
    u"at odd `p`. ### `1` IS THE `p = 3` CELL; THE LAW GIVES `4`, `9`, `25` AT `p = 5, 7, 11`. "
    u"### THE ### NONZERO ### CLAIM GENERALIZES; THE ### VALUE 1 ### DOES NOT.** *** "
    u"### ### **`p = 2` IS THE EXCEPTIONAL PLACE BY THE LAWS' OWN VALUES: `4 d_1 = q(q-2)` at "
    u"`q = 2` gives `d_1 = 0`, and the kernel says ### The death at `(2,1)` is the law's OWN "
    u"value** ### ; b226: ### **THE ARRIVAL DEPTH IS WHY ell(2) = 2 AND NOT 1.** ### **SO AT "
    u"`p = 2` THE OBJECT HAS NO LEVEL-1 DATUM AT ALL** -- not small, not unverified: the sector "
    u"is zero-dimensional and there is no unit to choose. ### ### **CONSEQUENCE FOR (SPEC-3), AND "
    u"IT IS A REAL CONDITION: ANY CANDIDATE SOURCING ITS FIRST-LEVEL TERM FROM THE LEVEL-1 DATUM "
    u"HAS NOTHING TO READ AT `p = 2`, SO IT MUST CARRY b226's STEP-UP OR AN EQUIVALENT AS PART OF "
    u"ITS DEFINITION.** ### b223's own limit travels: *THE (2,1) DEATH IS ISOLATED AND DOES NOT "
    u"PROPAGATE.* *** "
    u"### ### **TEST 3 -- THE ASSEMBLY STEP. ### (ABSENT), AND THE ABSENCE IS b237's FINDING, NOT "
    u"THIS ACT'S GREP.** ### b237: ### **A statement carrying the quotient channel's operator "
    u"onto `S-bar_v`, or carrying `u_v` into `V_inv` -- b227's words; the second is blocked by "
    u"b10; ### the first is not in the record. ### THIS IS THE ASSEMBLY STEP, NOT THE PER-PLACE "
    u"OPERATOR.** ### **AND THE STRUCTURAL FACT THE WHOLE ACT TURNS ON, FROM b227: `omega_u` "
    u"CANNOT BE EVALUATED ON act 9's OPERATOR ### BECAUSE THE OPERATOR ACTS ON A DIFFERENT SPACE "
    u"AND THE SECTOR THAT DEFINES THE UNIT IS ABSENT FROM IT** ### -- `tau_q` acts on `V_inv`, "
    u"`u_v` lives in `E_1(S-bar_v)`. ### **THE ZERO ON ONE SIDE AND THE NONZERO ON THE OTHER ARE "
    u"NOT TWO VALUES OF ONE QUANTITY; THEY ARE VALUES OF TWO OBJECTS THAT DO NOT MEET.** *** "
    u"### **AND THE SEARCH DESIGN'S OWN LIMIT IS DISCLOSED RATHER THAN FIXED AWAY: the needles "
    u"came from b237's OWN SENTENCE NAMING THE ABSENCE, so they find that sentence by "
    u"construction. ### THE HITS ARE ALL SELF-HITS; NO FILE ### STATES ### THE BRIDGE. ### A GREP "
    u"OVER ONE DIRECTORY (1261 files) IS NOT A PROOF OF CORPUS-WIDE ABSENCE AND THIS ACT DOES NOT "
    u"CLAIM ONE.** *** "
    u"### **THE SIZE RESTATED AS A TARGET ONLY (bench control, limit (L-B)): b262's first-level "
    u"family mass runs ### 73.96% AT `a^2 = 1e2` TO 99.95% AT `a^2 = 1e8` ### . ### NO CANDIDATE "
    u"COMPUTED, NO FIT ATTEMPTED. ### A SIZE THE OWED OBJECT MUST ACCOUNT FOR, NOT EVIDENCE THAT "
    u"ANY OBJECT DOES.** *** "
    u"### **THE SHADOW: `Core/AggregationSourceShadow.lean`, VANILLA, `decide` ONLY, ### NINE "
    u"TERMINALS AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED**, four polarity refusals at lean "
    u"exit 1. ### It carries the numerator's vanishing at `k = n` ### WITH ITS FOIL ONE LEVEL "
    u"ABOVE ### , the denominator's positivity, the empty range at `n = 1`, the place-2 zero at "
    u"arrival, the odd law's nonzero, ### **AND THE TWO LAWS' DISAGREEMENT AT `n = 1`.** ### **IT "
    u"COMPILES NO AGGREGATION AND NO OPERATOR, AND ITS HEADER STATES THAT `d_1 > 0` IS ABOUT THE "
    u"SECTOR AND NOT ABOUT b226's GENERATOR.** *** "
    u"### ### **FOUR DEVIATIONS, ALL DECLARED. ### (D1) F-QUOTE FIRED ON THE FIRST PASS** -- a "
    u"typographic apostrophe where the kernel has a straight one; 21 quotations, 1 unfindable, 0 "
    u"after the fix. ### **THE b229/b260/b261/b263 NEEDLE SPECIES, CAUGHT BEFORE IT REACHED THE "
    u"BANK -- AND THE EXPECTATION b266 REGISTERED AND DID NOT GET, b267 GOT.** ### **(D2) TEST "
    u"1's ARITHMETIC PRECEDED THE SEAL AND THE REGISTRATION SAYS SO AT (I1)** -- scored as an "
    u"exhibition, not a prediction. ### **(D3) THE TEST-3 SEARCH IS WEAKER THAN IT LOOKS.** "
    u"### **(D4) GATE 9 SHIPPED WITH AN `or` IN A FILE DECLARING IT HAS NONE -- HARNESS-LORE "
    u"RULE 2's EXACT SPECIES (b251), COMMITTED BY THE SEAT THAT CONSOLIDATED RULE 2 AT b266.** "
    u"### Repaired; all eleven check bodies verified conjunctive. ### ### **SECOND CONSECUTIVE "
    u"ACT IN WHICH A RULE b266 CONSOLIDATED FIRED ON THE ACT APPLYING IT (b266: rule 21; b267: "
    u"rule 2). ### WRITING A RULE DOWN DOES NOT INSTALL IT, NOW WITH TWO INSTANCES BEHIND IT.** *** "
    u"### **GATES 11/11 WITH EVERY FIXTURE FAILING AS REQUIRED. ### TERM SCAN CLEAN. ### "
    u"REGISTRATION TERM-SCANNED AND SATISFIABILITY-CHECKED ### BEFORE ### SEALING; SEAL "
    u"`fcc803df` INTACT AT THE CLOSE. ### NO PRIOR ACT RE-VERDICTED AND b226's OWED RESULT NOT "
    u"RE-GRADED INTO A THEOREM.** *** "
    u"### ### **THE CAMPAIGN'S NEXT ACT IS A FORK OF TWO NAMED STATEMENTS, AND IT IS THE AUTHOR'S "
    u"TO ORDER: ### (1) b226's OWED RESULT -- `4q P_1 f_{1,1} != 0` at every odd `p` at level 1, "
    u"### THE SMALLER AND A ### RESULT ### ; ### (2) b237's M-2 STATEMENT -- carrying the "
    u"quotient channel's operator onto `S-bar_v`, ### THE ONE M-2 ACTUALLY NAMES ### , with b10 "
    u"blocking the other direction and b227's ruling standing: ### IT WANTS A RESULT OR A RULING; "
    u"IT DOES NOT WANT A READ.** ### **THIS SEAT DOES NOT RULE WHICH.** *** "
    u"### **M-2 IS OWED. ### NO GRADE MOVED. ### NO ACT RE-VERDICTED. ### NO OWNER INSTRUMENT OR "
    u"OWNING BANK EDITED. ### b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 "
    u"BEYOND THE REGISTER SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b266: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b266)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"THE AGGREGATION'S TERM IS LOCATED",
                 u"RETURNS ### EXACTLY ZERO BY ITS OWN",
                 u"OVERRIDING CONVENTION",
                 u"AN ARITHMETIC ZERO CANNOT",
                 u"VERDICT (PARTIAL)",
                 u"IT DOES NOT GIVE u_{1,1} != 0",
                 u"VALUE 1 ### DOES NOT",
                 u"NO LEVEL-1 DATUM AT ALL",
                 u"MUST CARRY b226's STEP-UP",
                 u"the first is not in the record",
                 u"TWO OBJECTS THAT DO NOT MEET",
                 u"NINE ",
                 u"GATE 9 SHIPPED WITH AN `or`",
                 u"WRITING A RULE DOWN DOES NOT INSTALL IT",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"THE J-ARC IS IN THE FINDINGS DOCUMENT WHOLE",
                 u"ZERO CELLS FALL ABOVE THE CEILING",
                 u"THE RECORD SAID SO IN FIVE PLACES",
                 u"M-2's ADDRESS IS DERIVED",
                 u"J2 IS ### REFUTED",
                 u"STATES GRADES, CONFERS NONE"):
        assert kept in new_lead, "### prior headline lost in demotion: %r" % kept
    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]
    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)
    back = io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2]
    ok = (back == new_lead)
    sys.stdout.write("  prior title : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title   : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length : %d -> %d\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  prior kept  : %s\n" % ("YES" if rest in back else "NO"))
    sys.stdout.write("  read-back   : %s\n" % ("YES" if ok else "NO"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
