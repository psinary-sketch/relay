# -*- coding: utf-8 -*-
"""b268_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE GENERATOR'S NONVANISHING (b268)"
PRIOR_MARK = u"(b267)"

NEW = (
    u"*** ### ### **b226's OWED STEP IS ### PAID ### : `4q P_1 f_{1,1} != 0` AT EVERY ODD PRIME "
    u"AT LEVEL 1, AT GRADE ### DERIVES-on-IMP ### WITH ITS IMPORTS NAMED AND NO NEW IMPORT.** "
    u"### Ordered by the author, `RULE M2-ORDER: A1 then A2`; this is A1, ### **THE FIRST ITEM "
    u"THIS CAMPAIGN HAS CLOSED.** *** "
    u"### ### **AND THE ROUTE DELIVERED MORE THAN THE NONVANISHING: `support(u_p) = N - q` "
    u"EXACTLY** -- which b226 recorded as ### *\"AN OBSERVED REGULARITY, RECORDED AS OBSERVED AND "
    u"NOT ASSERTED AS A THEOREM\"* ### at six cells. ### **IT IS NOW DERIVED, GENERICALLY.** "
    u"### **b226 IS NOT RE-VERDICTED BY THAT: IT RECORDED AN OBSERVATION AS AN OBSERVATION AND WAS "
    u"RIGHT TO; A LATER ACT SUPPLIED THE DERIVATION IT DECLINED TO ASSERT, WHICH IS NOT THE SAME "
    u"THING.** *** "
    u"### **THE DERIVATION IN ONE LINE, FROM THE OWNERS' OWN OBJECTS:** ### applying the ### "
    u"BANKED ### identity `4q P_1 = (q + S)(1 + Pi)` to `f_{1,1} = e_{1+q} - e_1` gives "
    u"`u_p(m) = q*[(1+Pi)f](m) + (zeta^{m(1+q)} + zeta^{-m(1+q)} - zeta^{m} - zeta^{-m})`, which "
    u"away from four points vanishes iff `m q = 0 (mod q^2)` or `m(q+2) = 0 (mod q^2)`. "
    u"### ### **AND THE HINGE: FOR ODD `q`, `gcd(q+2, q^2) = 1`** -- a common prime divisor would "
    u"divide `q` and `q+2`, hence `2`, and `q` is odd. ### **SO THE ZERO SET IS EXACTLY THE `q` "
    u"MULTIPLES OF `q`, `support = N - q = q(q-1) >= 6 > 0`, AND `u_p != 0`.** *** "
    u"### **CONTROLLED EXACTLY IN `Z[zeta_N]` AT EIGHT PLACES -- b226's SIX REPRODUCED CELL FOR "
    u"CELL, PLUS `p = 17` AND `p = 19` WHICH NO PRIOR ACT MEASURED; 1039 VALUES REDUCED MODULO "
    u"`Phi_N`.** ### **NO FLOATING POINT DECIDES ANYTHING** (b223's standard), and the exact "
    u"tester was positive-controlled on a known zero AND a known nonzero before it was trusted -- "
    u"### **A TESTER THAT CANNOT SAY BOTH IS NOT A TESTER.** ### The table is ### A CHECK ON THE "
    u"DERIVATION, NEVER ITS EVIDENCE ### , and the unmeasured primes mean the control is not "
    u"confined to the cells the formula was first seen on. *** "
    u"### ### ### **AND THE BOUNDARY, REGISTERED BEFORE THE RESULT AND KEPT AFTER IT: ### A "
    u"SUPPORT IS NOT A CONTRIBUTION. ### (SPEC-1) WOULD READ A NUMBER THE AGGREGATION USES; THIS "
    u"ACT SUPPLIES A VECTOR THAT IS NOT ZERO. ### b226's STEP IS PAID; (SPEC-1) IS NOT TOUCHED; "
    u"M-2 REMAINS ### SPECIFIED-NOT-STATED ### AND NO AGGREGATION IS ADOPTED, STATED OR "
    u"REALIZED.** *** "
    u"### **`p = 2` IS STATED SEPARATELY AND NOT FOLDED IN, BY THE ARGUMENT'S OWN HINGE: AT "
    u"`q = 4`, `gcd(6,16) = 2` AND THE COLLAPSE FAILS.** ### **AND WHAT THE FAILURE DOES NOT DO: "
    u"`p = 2` AT LEVEL 2 STILL LANDS ON `N - q = 12`. ### THE HINGE FAILING CHANGES THE ROUTE TO "
    u"THE COUNT, NOT THE COUNT.** ### So any general statement must read ### **\"AT EVERY ODD `p` "
    u"AT LEVEL 1, AND AT `p = 2` AT LEVEL 2\"** ### ; \"at every prime at level 1\" would be false. "
    u"### **(SPEC-3) INHERITS A CONDITION ON CANDIDATES, NOT A CANDIDATE: ANY AGGREGATION READING "
    u"A FIRST-LEVEL DATUM MUST CARRY b226's STEP-UP OR AN EQUIVALENT, OR BE UNDEFINED AT `p = 2` "
    u"AND FAIL (SPEC-3) OUTRIGHT.** *** "
    u"### **THE SHADOW: `Core/GeneratorSupportShadow.lean`, VANILLA, `decide` ONLY, ### NINE "
    u"TERMINALS AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED**, four polarity refusals at lean "
    u"exit 1. ### It carries the support count and ### ITS POSITIVITY, WITH A POLARITY CONTROL AT "
    u"`q = 1` WHERE THE COUNT VANISHES ### , and ### **THE HINGE WITH ITS FOIL -- "
    u"`gcd(q+2,q^2) = 1` AT THE ODD `q` AND `gcd(6,16) = 2` AT `q = 4`.** ### **IT COMPILES NO "
    u"GENERATOR, NO PROJECTOR AND NO AGGREGATION**, and its header says the identification of the "
    u"count with a support is the DERIVATION's and not the file's. *** "
    u"### ### **FOUR DEVIATIONS, ALL DECLARED. ### (D1) THE PURITY IDENTITY IS BANKED AND THIS ACT "
    u"REDISCOVERED IT** -- registered at (I1) before the run; ### **CORROBORATION, NOT A FINDING** "
    u"(lore rule 17), and the derivation cites b226's line. ### **(D2) THE SUPPORT "
    u"RECONNAISSANCE PRECEDED THE SEAL** -- so S1's expectation is not unsighted, and what the run "
    u"actually settled is narrower and is said so. ### **(D3) THE INCENTIVE IS NAMED: this seat "
    u"wrote b267, whose TEST 2 stands (PARTIAL) on the step this act pays.** ### **(D4) AND A "
    u"DISAGREEMENT WITH THE FERRY'S FRAMING, REGISTERED BEFORE THE RUN AND KEPT: the ferry asks "
    u"S2 to derive that support ### forces ### the (1,1) component nonzero, as though a step lay "
    u"between them. ### THERE IS NONE -- `u_p` IS THE IMAGE OF `f_{1,1}`, SO ITS NONVANISHING IS "
    u"THE GENERATOR'S. ### MANUFACTURING A STEP WOULD HAVE BEEN A DOUBLE-NAME ERROR RUN "
    u"BACKWARDS.** *** "
    u"### **AND b267's OWN DEFECT DID NOT REPEAT, BECAUSE THIS ACT CHECKED RATHER THAN DECLARED: "
    u"b267 shipped an `or` in a check's logic under a header denying it; ### **b268's GATE 11 "
    u"TOKENIZES ITS OWN SOURCE AND REPORTS 12 CHECK BODIES, 0 OFFENDING** -- and its first draft, "
    u"regex-based, reported two FALSE hits and was replaced. ### **A REGEX CANNOT TELL AN OPERATOR "
    u"FROM THE LETTERS INSIDE A STRING; `tokenize` CAN.** *** "
    u"### **GATES 11/11 WITH EVERY FIXTURE FAILING AS REQUIRED. ### TERM SCAN CLEAN. ### "
    u"REGISTRATION TERM-SCANNED AND SATISFIABILITY-CHECKED ### BEFORE ### SEALING; SEAL "
    u"`119973a1` INTACT AT THE CLOSE.** *** "
    u"### ### **NEXT: ### A2 ### -- b237's M-2 STATEMENT, *carrying the quotient channel's "
    u"operator onto `S-bar_v`, or carrying `u_v` into `V_inv`*, the second blocked by b10. "
    u"### **`RULE M2-ORDER` PUTS IT NEXT AND IT AWAITS THE AUTHOR'S WORD.** ### And it can now be "
    u"written over a generator that is ### KNOWN NONZERO ### rather than measured at six places. "
    u"### **b227's RULING STILL GOVERNS ITS SHAPE: *IT WANTS A RESULT OR A RULING; IT DOES NOT "
    u"WANT A READ.*** *** "
    u"### **M-2 IS OWED. ### ITEM 1 OF THE SEAM'S DEBT IS STILL NOT PAID -- A1 WAS b226's STEP, "
    u"NOT M-2. ### NO PRIOR ACT RE-VERDICTED. ### NO OWNER INSTRUMENT OR OWNING BANK EDITED. "
    u"### b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 BEYOND THE REGISTER "
    u"SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b267: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b267)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"b226's OWED STEP IS ### PAID ###",
                 u"RULE M2-ORDER: A1 then A2",
                 u"support(u_p) = N - q",
                 u"gcd(q+2, q^2) = 1",
                 u"1039 VALUES REDUCED MODULO",
                 u"NO FLOATING POINT DECIDES ANYTHING",
                 u"A SUPPORT IS NOT A CONTRIBUTION",
                 u"gcd(6,16) = 2",
                 u"NINE ",
                 u"CORROBORATION, NOT A FINDING",
                 u"DOUBLE-NAME ERROR RUN",
                 u"12 CHECK BODIES, 0 OFFENDING",
                 u"A2 ###",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"THE AGGREGATION'S TERM IS LOCATED",
                 u"THE J-ARC IS IN THE FINDINGS DOCUMENT WHOLE",
                 u"ZERO CELLS FALL ABOVE THE CEILING",
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
