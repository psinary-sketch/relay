# -*- coding: utf-8 -*-
"""b278_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE SPACE-LEVEL BARRIER (b278)"
PRIOR_MARK = u"(b277)"

NEW = (
    u"*** ### ### **VERDICT: (UNDECIDED). ### THE RESISTING STEP IS THE DEFINITION OF "
    u"`S\u0304_v` ITSELF.** ### **THE TOWER IS (ABSENT) \u2014 AND WORSE THAN b277 KNEW: THE ACT "
    u"THAT OWNS THE TOWER SAYS IN ITS OWN VOICE THAT IT CONSTRUCTS NO LIMIT OBJECT AND CLAIMS "
    u"NONE.** ### **THE TWO AVAILABLE READINGS GIVE ### OPPOSITE ### ANSWERS, AND THE CORPUS "
    u"SETTLES NEITHER. ### THAT BIVALENCE IS THE FINDING.** ### **NOTHING IS ADOPTED. ### M-2 "
    u"REMAINS ### SPECIFIED-NOT-STATED ### . ### NOTHING DEPOSITS.** *** "
    u"### ### **WHY (UNDECIDED) AND NOT (BARRIER-CONDITIONAL), AND THE REASON IS NOT CAUTION.** "
    u"### The ferry offered the theorem resting on b277's inference with the condition printed. "
    u"### This act went to find the definition and found something stronger and worse. ### **A "
    u"CONDITIONAL BARRIER WOULD BE A THEOREM ABOUT AN OBJECT NO ACT HAS BUILT, DRESSED AS A "
    u"CONDITION \u2014 NOT A WEAKER CLAIM BUT A DIFFERENT KIND OF CLAIM, AND THE DISCIPLINE "
    u"SHOULD REFUSE IT RATHER THAN FORMAT IT.** *** "
    u"### ### **THE TOWER: (ABSENT), WITH A POSITIVE CONTROL \u2014 THE NEAR-MISSES WERE FOUND, "
    u"NOT MERELY UNSEARCHED-FOR.** ### **191 LINES MENTION `S\u0304`; 13 ARE DEFINITION-SHAPED; "
    u"NOT ONE SAYS WHAT THE TOWER IS.** ### They resolve into ### **A CITATION CHAIN TERMINATING "
    u"IN AN UNFILLED REFERENCE:** ### b226 cites b198 (I4); b223 cites it verbatim; and b198 (I4) "
    u"says \u201cS-bar = the L\u00b2-CLOSURE OF THE TOWER'S UNION\u201d \u2014 ### **NAMING THE "
    u"TOWER AND NOT SAYING WHOSE.** *** "
    u"### ### **AND b21, WHICH OWNS THE TOWER, POINTS THE OTHER WAY.** ### Its level space is "
    u"`V_n = { f : supp f in p^{-n}Z_p, f invariant under translation by p^n Z_p }`, \u201can "
    u"honest finite-dimensional subspace of L\u00b2(Q_p)\u201d \u2014 ### **THE FULL LEVEL SPACE, "
    u"WITH `Son(p,n)` SITTING INSIDE IT.** ### And its FOOT is the act's central quotation: ### "
    u"**\u201cthe union of the V_n is dense in L\u00b2(Q_p), but Son(p,n) does NOT stabilize \u2026 "
    u"so nothing here constructs a limit object, and none is claimed.\u201d** ### Stated at exact "
    u"strength: ### **b21 SPEAKS FOR b21; WHAT THIS ACT ADDS IS THAT NO OTHER ACT IT COULD FIND "
    u"CONSTRUCTS ONE EITHER, AND THAT THE SEARCH WAS CONTROLLED RATHER THAN CASUAL.** *** "
    u"### ### **WHAT ### IS ### SETTLED: `Son`'s BALL ### IS ### b270's ABSORPTION SET.** ### "
    u"Ball-vanishing is definitional for `Son` on BOTH halves \u2014 the function and its "
    u"transform \u2014 and the two balls were ### **COMPARED AS SETS AND NOT BY NAME**, the "
    u"absorption set computed from its own property (the indices `p^n m` can land on). ### Same "
    u"set at all eight cells. *** "
    u"### ### **THE TWO READINGS, BOTH DERIVED.** ### **READING TWO** \u2014 `S\u0304_v` a `Son` "
    u"limit: every element vanishes on the ball, b270's absorption gives (SPEC-1) `= 0` "
    u"identically, verified on the spanning family at all eight cells. ### **THE BARRIER HOLDS.** "
    u"### **READING ONE** \u2014 `S\u0304_v` the closure of the `V_n` tower, which b21's foot says "
    u"is dense in `L\u00b2(Q_p)`: then `V_\u2113` lies honestly inside, and ### **`g_0 = 2q e_0 + "
    u"2\u00b71` IS EXHIBITED WITH BALL VALUE `2q+2` AND `P(\u2113)p^{\u2113/2} = 4(N\u2212q)` "
    u"\u2014 48, 24, 80, 168, 440, 624, 1088, 1368, NONZERO AT EVERY CELL. ### THE BARRIER IS "
    u"REFUTED.** *** "
    u"### ### **THE CONSOLIDATION THAT SURVIVES THE BIVALENCE, AND IT IS REAL: ### ON `Son` AT "
    u"ANY FINITE LEVEL, (SPEC-1) IS IDENTICALLY ZERO** \u2014 by b270's absorption AND by b276's "
    u"quadratic bound, two independent routes. ### **SO b269's R3, b270, b273, b275 AND b277 ARE "
    u"FIVE INSTANCES OF ONE THEOREM RATHER THAN FIVE SEPARATE OUTCOMES \u2014 AND NOT ONE OF THEM "
    u"IS RE-VERDICTED.** ### Each was scoped to the ambient `E_1` at a finite level and is exactly "
    u"true there; the consolidation adds a sentence ABOVE them, not a correction INSIDE any. ### "
    u"**AND IT DOES NOT REACH `S\u0304_v`, BECAUSE WE DO NOT KNOW WHAT `S\u0304_v` IS.** *** "
    u"### ### **b277's BLOCK IS NOT RE-VERDICTED, AND ITS STATUS IS SHARPENED:** ### b277 found "
    u"no warrant for the vector; ### **THIS ACT FOUND THAT THE SPACE THE WARRANT WOULD PLACE IT "
    u"IN IS ITSELF UNBUILT.** ### b277's (BLOCKED) would be unchanged under either reading. *** "
    u"### ### **THE BINDING WORK-ORDER IS NOW `W-ORD-SBAR-TOWER`, RESTATED AND SHARPENED: ### "
    u"CONSTRUCT THE LIMIT OBJECT, OR RULE WHICH TOWER `S\u0304_v` CLOSES.** ### **EVERY M-2 "
    u"QUESTION ABOUT THE LIMIT PASSES THROUGH IT.** ### Also carried: `W-ORD-FIBER-GENERAL`, and "
    u"the inherited imports (b262's PNT-plus-saddle, b260's `W-ORD-TQ-IDENTIFY`) travelling with "
    u"every use of either no-go. *** "
    u"### ### **`W-ORD-SELF-NEEDLE` AND THE INVERTED-FIXTURE SPECIES: DISCHARGED BY TOOLING.** ### "
    u"`needle_pull.py` now carries `pull_self` and `absent_exact`; a must-fail fixture built on "
    u"`absent_exact` compares WHOLE LINES, ### **SO A STRING THAT IS MERELY A SUBSTRING OF A "
    u"CORRECT SENTENCE CANNOT SATISFY IT.** ### Controlled in both polarities against b277's own "
    u"inverted string, before the seal. ### **AND THE NEW GATE CAUGHT ITS OWN AUTHOR ON FIRST "
    u"RUN** \u2014 it counted ONE substring-based must-fail fixture, in this act's own suite, and "
    u"REFUSED the check rather than passing it. ### **A RULE THAT CATCHES THE SEAT WHO WROTE IT "
    u"ON THE DAY IT IS WRITTEN IS THE ONLY KIND WORTH KEEPING.** *** "
    u"### ### **THE SHADOW: NOTHING BUILT, AND FOR THE ACT'S OWN REASON \u2014 the ferry's "
    u"candidate residue was the CLOSURE property, and ### **CLOSURE IS A PROPERTY OF A LIMIT "
    u"SPACE THAT IS NOT CONSTRUCTED. ### A LEAN FILE ABOUT THE CLOSURE OF AN UNBUILT SPACE WOULD "
    u"BE THE DOUBLE-NAME SPECIES IN ITS PUREST FORM.** ### **0 `.lean` FILES MOVED, CHECKED NOT "
    u"ASSUMED.** *** "
    u"### ### **THE ARC'S SOBER READING: ### TWELVE ACTS HAVE NARROWED M-2 TO A SINGLE QUESTION, "
    u"AND THAT QUESTION SITS ### UNDERNEATH ### THE CAMPAIGN RATHER THAN INSIDE IT. ### BEFORE "
    u"ANY AGGREGATION CAN BE STATED OVER `S\u0304_v`, SOMEONE MUST SAY WHAT `S\u0304_v` IS \u2014 "
    u"AND THAT IS AN AUTHOR'S RULING OR A CONSTRUCTION, NOT THIS SEAT'S.** ### **THE SEAM'S DEBT, "
    u"ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED. ### NOTHING DEPOSITS. ### NOTHING CIRCULATES. "
    u"### h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b277: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b277)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (UNDECIDED)",
                 u"THE RESISTING STEP IS THE DEFINITION",
                 u"THE REASON IS NOT CAUTION",
                 u"REFUSE IT RATHER THAN FORMAT IT",
                 u"NOT ONE SAYS WHAT THE TOWER IS",
                 u"A CITATION CHAIN TERMINATING",
                 u"nothing here constructs a limit object",
                 u"THE FULL LEVEL SPACE",
                 u"COMPARED AS SETS AND NOT BY NAME",
                 u"THE BARRIER HOLDS",
                 u"THE BARRIER IS REFUTED",
                 u"FIVE INSTANCES OF ONE THEOREM",
                 u"NOT ONE OF THEM IS RE-VERDICTED",
                 u"W-ORD-SBAR-TOWER",
                 u"CAUGHT ITS OWN AUTHOR ON FIRST",
                 u"CHECKED NOT ASSUMED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (BLOCKED)",
                 u"VERDICT: (INCOMPATIBLE)",
                 u"VERDICT: (RULE STATED)",
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
