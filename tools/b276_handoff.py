# -*- coding: utf-8 -*-
"""b276_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"SIZE AGAINST EQUIVALENCE (b276)"
PRIOR_MARK = u"(b275)"

NEW = (
    u"*** ### ### **VERDICT: (INCOMPATIBLE). ### NO EQUIVALENCE-PRESERVING UNIT SEQUENCE SUPPLIES "
    u"THE FIRST-LEVEL MASS b262 DERIVES. ### THE DEMAND FORCES AN ORTHOGONAL OBJECT.** ### "
    u"**AND IT IS NOT A REFUTATION OF THE IDENTITY \u2014 THE BANK SAYS SO BEFORE IT SAYS "
    u"ANYTHING ELSE.** ### **NOTHING IS ADOPTED. ### M-2 REMAINS ### SPECIFIED-NOT-STATED ### . "
    u"### NOTHING DEPOSITS.** *** "
    u"### ### **THE ARGUMENT IN FIVE LINES.** ### (1) Every `u'` in `E_1` splits orthogonally as "
    u"`w + z` with `w` in `E_1(Son)` and SIZE `\u03c3 = \u2016z\u2016/\u2016u'\u2016` \u2014 ### "
    u"**DERIVED, NOT POSITED: a ball-vanishing `E_1` vector IS a Son vector, since its transform "
    u"is `q` times itself.** ### (2) b226's `u` lies in `E_1(Son)`, so `<u,u'> = <u,w>` exactly "
    u"and `|<u\u0302,u\u0302'> \u2212 1| \u2265 \u03c3\u00b2/2`. ### (3) ### **THE FIBER LEMMA** "
    u"### kills the cross term, so SPEC-1's value is EXACTLY QUADRATIC: `|P\u0302| \u2264 "
    u"\u03c3\u00b2`. ### (4) von Neumann Def 3.3.2 makes equivalence a CONVERGENCE, so `\u03a3 "
    u"\u03c3\u00b2 < \u221e` and `\u03a3 |P\u0302| < \u221e`, whence ### **THE WINDOW SUMS TEND "
    u"TO ZERO.** ### (5) b262 derives that the same window must supply a quantity tending to "
    u"INFINITY. ### **A QUANTITY TENDING TO ZERO CANNOT SUPPLY ONE TENDING TO INFINITY.** *** "
    u"### ### **THE FIBER LEMMA IS THE LOAD-BEARING STEP, AND IT PROVES AT LEVEL 1.** ### For "
    u"`w` in `E_1(Son)` and any ball point, the fiber sum `W(b)` is ZERO \u2014 so the cross term "
    u"`\u03a3_b conj(z(b))W(b)` vanishes FOR EVERY `z` AT ONCE. ### At level 1, `S_quot` is the "
    u"off-ball indicator and the fiber of `pc` is a full progression, so a character sum gives "
    u"`W(pc) = \u03a3_r \u03b6^{\u2212prc} w(pr)` using `S w = q w` \u2014 and ### **EVERY `pr` "
    u"IS A BALL POINT WHERE `w` VANISHES. ### QED.** ### Verified besides at all eight cells on "
    u"### **185 BALL-VANISHING VECTORS**, the FULL `f_{i,j}` family at the five cells with `N "
    u"\u2264 121`. ### **SO IT IS PROVED AT LEVEL 1 AND FULLY VERIFIED AT (2,2) \u2014 WHICH IS "
    u"EVERY CELL b226's RULE ACTUALLY USES.** *** "
    u"### ### **THE ATTRIBUTION, WHICH WAS THE ACT'S CENTRAL CARE AND ITS NAMED FAILURE MODE.** "
    u"### b262's growth could come from per-place SIZE or from the NUMBER OF PLACES in the "
    u"window. ### **THE ARGUMENT NEVER ASKS WHICH AND DOES NOT NEED TO: A CONVERGENT SERIES HAS "
    u"VANISHING TAILS HOWEVER MANY TERMS THE WINDOW HOLDS.** ### The tempting error \u2014 "
    u"attributing all growth to place-count and allowing each place a merely BOUNDED "
    u"contribution \u2014 fails because ### **EQUIVALENCE DOES NOT BOUND THE CONTRIBUTIONS, IT "
    u"MAKES THEM SUMMABLE, WHICH IS STRICTLY STRONGER AND IS WHAT KILLS THE WINDOW.** *** "
    u"### ### **THE CONTROLS, AND THREE ACTS' ARITHMETIC MEETING AT ONE NUMBER.** ### b273's `v` "
    u"is ONE POINT of the parameterization: with `s\u00b2 = \u22128/11 + (8/11)\u221a2`, both "
    u"`\u03c3\u00b2` and `P\u0302` carry the same `s\u00b2/\u2016v\u2016\u00b2`, so ### **THE "
    u"BOUND REDUCES TO `48 \u2264 160`, A RATIONAL FACT.** ### And b275's rule is the extreme "
    u"`\u03c3 = 1`, giving `P\u0302 = 48/160 = 3/10` \u2014 ### **EXACTLY b274's CLOSED FORM "
    u"`(q\u22121)/(2(q+1))` AT `q = 4`.** *** "
    u"### ### **THE SELECTION NOTE PROMOTES.** ### b272 filed it at PATTERN grade with the "
    u"criterion \u201ca derivation that no ball-vanishing unit can meet SPEC-1\u201d. ### **THAT "
    u"IS NOW MET AND EXCEEDED:** ### b271's absorption gives the first half; this act gives the "
    u"sharper second \u2014 ### **THE BALL SUPPORT NEEDED TO SUPPLY THE MASS IS ITSELF "
    u"INCOMPATIBLE WITH EQUIVALENCE.** ### So the note promotes to a ### DERIVED STATEMENT ### at "
    u"this scope: ### **THE IDENTITY'S FIRST-LEVEL DEMAND SELECTS THE VON NEUMANN CLASS RATHER "
    u"THAN THE CLASS BEING FREE TO BE CHOSEN BY RULING.** ### **AND THE SCOPE IS THE WHOLE OF THE "
    u"PROMOTION: it is derived for the VECTOR-STATE construction only, and IT IS NOT DERIVED FOR "
    u"C2 OR C3, WHOSE STATUS IS UNCHANGED.** *** "
    u"### ### **WHAT IT DOES NOT SAY.** ### It does not refute the identity \u2014 b262 itself "
    u"records that a divergent junction matched by a divergent archimedean side is consistent, "
    u"and ### **THIS ACT CONSTRAINS THE FINITE-PLACE UNIT SEQUENCE, NOT THE IDENTITY.** ### It "
    u"says nothing about the complete roster or `h2`. ### And ### **IT DOES NOT SAY NO SEQUENCE "
    u"SUPPLIES THE MASS \u2014 ONLY THAT NO EQUIVALENCE-PRESERVING ONE DOES.** ### b275 exhibited "
    u"a mass-supplying rule and found its object orthogonal; ### **b276 EXPLAINS WHY THAT WAS "
    u"FORCED AND NOT AN ACCIDENT OF THAT RULE.** *** "
    u"### ### **`W-ORD-NEEDLE-SOURCE` IS DISCHARGED BY DOING IT.** ### `tools/needle_pull.py` "
    u"extracts each needle as the EXACT LINE its owner emitted, and ### **IT FAILED LOUDLY ON TWO "
    u"ANCHORS TYPED FROM MEMORY BEFORE ANY GATE WAS WRITTEN** \u2014 the exact class that cost "
    u"b273, b274 and b275 a gate apiece, caught at its source. ### **THIS IS THE FIRST ACT IN "
    u"FOUR WITH NO GATE NEEDLE FAILURE, AND IT IS BECAUSE A TOOL NOW PREVENTS IT RATHER THAN "
    u"BECAUSE THIS SEAT WAS MORE CAREFUL.** ### Shadow: nothing built, residues enumerated, sixth "
    u"act on the same ground. ### **0 `.lean` FILES MOVED, CHECKED NOT ASSUMED.** *** "
    u"### ### **M-2's ROW: ### SPECIFIED-NOT-STATED, UNCHANGED.** ### **THIS ACT RULES OUT A "
    u"CLASS OF CANDIDATES; IT NAMES NONE. ### M-2 ASKS FOR A FUNCTION OVER PLACES WITH A STATED "
    u"VALUE.** ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED. ### NOTHING "
    u"DEPOSITS. ### NOTHING CIRCULATES. ### h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b275: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b275)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (INCOMPATIBLE)",
                 u"NOT A REFUTATION OF THE IDENTITY",
                 u"DERIVED, NOT POSITED",
                 u"THE FIBER LEMMA",
                 u"EVERY `pr` IS A BALL POINT WHERE `w` VANISHES",
                 u"185 BALL-VANISHING VECTORS",
                 u"EVERY CELL b226's RULE ACTUALLY USES",
                 u"HOWEVER MANY TERMS THE WINDOW HOLDS",
                 u"MAKES THEM SUMMABLE",
                 u"THE SELECTION NOTE PROMOTES",
                 u"IT IS NOT DERIVED FOR C2 OR C3",
                 u"ONLY THAT NO EQUIVALENCE-PRESERVING ONE DOES",
                 u"DISCHARGED BY DOING IT",
                 u"FIRST ACT IN\n FOUR".replace(u"\n ", u" "),
                 u"CHECKED NOT ASSUMED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (RULE STATED)",
                 u"VERDICT: (STRADDLE PARTIAL)",
                 u"VERDICT: (ATTAINABLE)",
                 u"VERDICT: (CLASS NONEMPTY BUT BLOCKED)",
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
