# -*- coding: utf-8 -*-
"""b277_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE AGGREGATION STATED, ATTEMPT (b277)"
PRIOR_MARK = u"(b276)"

NEW = (
    u"*** ### ### **VERDICT: (BLOCKED). ### THE FAILING CONDITION IS von Neumann's Def 3.3.1 "
    u"CLAUSE (i), `f_alpha in H_alpha for all alpha in I`: ### THE CANDIDATE UNIT HAS NO WARRANT "
    u"TO LIE IN THE HILBERT SPACE THE PRODUCT IS TAKEN OVER.** ### **NOTHING IS ADOPTED. ### M-2 "
    u"REMAINS ### SPECIFIED-NOT-STATED ### . ### NOTHING DEPOSITS.** *** "
    u"### ### **THE SHAPE OF THIS ACT IS UNUSUAL AND IS SAID FIRST.** ### Everything the ferry "
    u"asked for was built and almost everything passed: the piecewise rule written whole, the "
    u"aggregation written whole, and ### **AT THE MODEL LEVEL IT IS A FUNCTION OVER PLACES WITH A "
    u"STATED VALUE \u2014 A CLOSED FORM AT EVERY ODD PRIME AND AN EXACT VALUE AT `p = 2`.** ### "
    u"(SPEC-1), (SPEC-2), (SPEC-3) and G-NORM ALL PASS. ### **AND THEN ONE CONSTITUENT FAILS, AND "
    u"IT IS NOT A SPEC: IT IS THE REQUIREMENT THAT THE UNIT LIE IN THE SPACE AT ALL. ### A "
    u"STATEMENT THAT MEETS EVERY SPEC AND HAS NO WARRANTED HOME IS NOT A CANDIDATE.** *** "
    u"### ### **THE STATEMENT, AT THE MODEL LEVEL.** ### `u''_p := 4q P_1 e_0/\u2016\u00b7\u2016` "
    u"at odd `p`; b273's `v` at `(2,2)`; `Q_p(k) := <U^k S_quot u''_p, u''_p>`. ### Every "
    u"constituent unfolded to an owner, `E_1` membership checked at EACH branch. ### **`Q_p(1) "
    u"p^{1/2} = (p\u22121)/(2(p+1))` at every odd place \u2014 `1/4, 1/3, 3/8, 5/12, 3/7, 4/9, "
    u"9/20` \u2014 and `Q_2(2)\u00b72 = 63/199 \u2212 (33/199)\u221a2` at `p = 2`, COMPUTED UNDER "
    u"ITS OWN BRANCH.** ### So it meets b275's own bar: ### **IT IS A NUMBER AT EVERY PLACE, NOT "
    u"ONLY A UNIT.** *** "
    u"### ### **THE BLOCK, LOCATED AND QUOTED AT ITS OWNER.** ### b226 carries the C\u2080 "
    u"condition's first clause as \u201c(i) a vector at every place \u2026 f_alpha in H_alpha for "
    u"all alpha in I\u201d, so the unit must lie in `H_v = S\u0304_v`. ### b198 (I4) makes "
    u"`S\u0304` the L\u00b2-closure of the TOWER'S UNION, and (I2) places a level vector in the "
    u"limit only through the closure of ITS LEVEL TOWER. ### **AND WHICH TOWER IT IS FOLLOWS FROM "
    u"b198's OWN GOAL: ITS WHOLE OBJECT IS TO PROVE `E_1(S\u0304_v)` NONZERO, WHICH WOULD BE "
    u"VACUOUS IF `S\u0304` WERE THE FULL SPACE. ### THE WORK IS ONLY WORK IF THE TOWER IS THE "
    u"`Son` TOWER.** ### And the candidate is ### **NOT IN `Son` AT ANY OF THE EIGHT CELLS** "
    u"\u2014 its nonzero ball value is exactly what put it in b271's escape class. *** "
    u"### ### **STATED AT ITS EXACT STRENGTH AND NOT ABOVE IT: ### IT IS NOT PROVED THAT THE "
    u"CANDIDATE LIES OUTSIDE `S\u0304_v`; IT IS THAT NO WARRANT PLACES IT INSIDE.** ### The "
    u"constituent is MISSING, not false \u2014 and a missing constituent blocks a statement just "
    u"as surely, which is why the verdict is (BLOCKED) and not (UNDECIDED). ### **AND THIS "
    u"SHARPENS b275 RATHER THAN CONTRADICTING IT: b275 recorded the lapse as a COST because it "
    u"was writing a UNIT rule, for which placement is a premise; THIS ACT WRITES THE AGGREGATION, "
    u"FOR WHICH PLACEMENT IS A CONSTITUENT OF THE OBJECT'S DEFINITION.** *** "
    u"### ### **WHAT IT ENTAILS FOR C2 AND C3, AND IT IS NOT A RECOMMENDATION.** ### Both are "
    u"untouched, ### **BECAUSE THEY BOTH WORK INSIDE `S\u0304_v`** \u2014 C2 asks what `S_quot` "
    u"does to `E_1` as a map; C3 changes the structure ON the space, not the space. ### **SO THE "
    u"CAMPAIGN'S REMAINING LIVE ROUTES ARE EXACTLY THE ONES THAT NEVER LEAVE `S\u0304_v`, AND THE "
    u"ESCAPE-CLASS LINE IS THE ONE THAT DID.** ### **AND THAT IS NOT A RE-VERDICT: b271's "
    u"(ESCAPE), b272's characterization, b273's (ATTAINABLE) and b275's (RULE STATED) were each "
    u"scoped to the AMBIENT `E_1` AT A FINITE LEVEL and are exactly true there \u2014 none of "
    u"them was writing the aggregation, and the constituent that blocks here is one none of them "
    u"needed.** *** "
    u"### ### **THE SIZE CONTROL, RUN AFTER THE STATEMENT WAS FIXED, NO FIT.** ### "
    u"`Q_p(1) \u2265 1/(4p^{1/2})`, so the aggregate DIVERGES \u2014 exact lower bound `count/4`, "
    u"no float. ### b262's target also diverges. ### **THE TWO ARE NOT COMPARED IN MAGNITUDE, "
    u"ONLY REPORTED AS BOTH DIVERGENT, AND b276's SENTENCE IS CARRIED: A DIVERGENT MASS IS "
    u"CONSISTENT WITH ORTHOGONALITY.** ### **AND THE CONTROL CHANGES NOTHING: A DIVERGENT "
    u"AGGREGATE FROM AN OBJECT WITH NO WARRANTED HOME IS STILL AN OBJECT WITH NO WARRANTED "
    u"HOME.** *** "
    u"### ### **THE WORK-ORDER THIS ACT TURNS ON, FILED NOT RUN: ### `W-ORD-SBAR-TOWER` \u2014 "
    u"WHAT EXACTLY IS THE TOWER WHOSE CLOSURE IS `S\u0304_v`?** ### This act infers `Son` from "
    u"b198's own goal sentence, ### **WHICH IS AN INFERENCE FROM PURPOSE AND NOT A QUOTATION OF A "
    u"DEFINITION. ### THE CORPUS SHOULD STATE IT OUTRIGHT, AND UNTIL IT DOES THE BLOCK RESTS ON "
    u"AN INFERENCE \u2014 A GOOD ONE, AND STILL AN INFERENCE.** ### Also filed: "
    u"`W-ORD-FIBER-GENERAL`; and b276's inherited imports (b262's PNT-plus-saddle, b260's "
    u"`W-ORD-TQ-IDENTIFY`) restated as travelling with every use of the no-go. *** "
    u"### ### **THE DEVIATIONS.** ### A first draft printed `g_0`'s value under b273's label at "
    u"`(2,2)` \u2014 ### **ONE VECTOR INHERITING ANOTHER'S RESULT WITH A LABEL SAYING SO, THE "
    u"EXACT HAZARD THE REGISTRATION NAMED.** ### The block was found ### BY READING, NOT BY "
    u"COMPUTING ### , before the seal, which is what the owners-first rule is for. ### And four "
    u"gates failed on first run: three needles into this act's OWN files were typed from memory "
    u"\u2014 ### **`needle_pull` COVERS OWNER FILES ONLY, SO `W-ORD-NEEDLE-SOURCE` IS HALF "
    u"DISCHARGED AND THE REMAINDER IS FILED AS `W-ORD-SELF-NEEDLE`** \u2014 and the fourth was "
    u"worse: ### **A FIXTURE THAT FIRED ON THE ### CORRECT ### TEXT, BECAUSE ITS STRING WAS A "
    u"SUBSTRING OF \u2018IT IS NOT PROVED THAT \u2026\u2019. ### AN INVERTED FIXTURE, NOT A DEAD "
    u"ONE, AND GATE 13 CANNOT SEE IT BECAUSE IT IS REACHABLE.** *** "
    u"### ### **M-2's ROW DOES NOT MOVE TO STATED-NOT-ADOPTED**, because what was written is not "
    u"yet a statement about the object M-2 asks about. ### **THE SEAM'S DEBT, ITEM 1, IS STILL "
    u"NOT PAID. ### M-2 IS OWED. ### NOTHING DEPOSITS. ### NOTHING CIRCULATES. ### h2 STANDS "
    u"EXACTLY WHERE THE DEPOSIT LEFT IT.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b276: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b276)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (BLOCKED)",
                 u"NO WARRANT TO LIE IN THE HILBERT SPACE",
                 u"THE SHAPE OF THIS ACT IS UNUSUAL",
                 u"IT IS A NUMBER AT EVERY PLACE",
                 u"COMPUTED UNDER ITS OWN BRANCH",
                 u"THE WORK IS ONLY WORK IF THE TOWER IS THE",
                 u"NOT IN `Son` AT ANY OF THE EIGHT CELLS",
                 u"IT IS THAT NO WARRANT PLACES IT INSIDE",
                 u"SHARPENS b275 RATHER THAN CONTRADICTING IT",
                 u"THEY BOTH WORK INSIDE",
                 u"AND THAT IS NOT A RE-VERDICT",
                 u"STILL AN OBJECT WITH NO WARRANTED",
                 u"W-ORD-SBAR-TOWER",
                 u"A GOOD ONE, AND STILL AN INFERENCE",
                 u"W-ORD-SELF-NEEDLE",
                 u"AN INVERTED FIXTURE, NOT A DEAD",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (INCOMPATIBLE)",
                 u"VERDICT: (RULE STATED)",
                 u"VERDICT: (STRADDLE PARTIAL)",
                 u"VERDICT: (ATTAINABLE)",
                 u"VERDICT: (ESCAPE)",
                 u"C1 IS STRUCK",
                 u"M-2 IS NOT STATED",
                 u"STATES GRADES, CONFERS NONE"):
        assert kept in new_lead, "### prior headline lost in demotion: %r" % kept
    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]
    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)
    assert io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2] == new_lead
    sys.stdout.write("  prior title : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title   : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length : %d -> %d chars\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  ### DEMOTED, NOT REWRITTEN: every prior headline still present.\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
