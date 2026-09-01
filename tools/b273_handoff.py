# -*- coding: utf-8 -*-
"""b273_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE SPEC-2 RANGE (b273)"
PRIOR_MARK = u"(b272)"

NEW = (
    u"*** ### ### **VERDICT: (ATTAINABLE). ### act 9's TERM IS ATTAINED BY A UNIT IN `E_1` AT "
    u"`(2,2)`, `k = 1`, AND AN ATTAINING VECTOR IS EXHIBITED EXACTLY.** ### **SCOPE: ONE CELL "
    u"\u2014 THE SECOND CELL WAS RUN AND THE CERTIFICATION DID NOT CLOSE THERE, WHICH IS SAID "
    u"FIRST AND NOT LAST.** ### **NO UNIT IS ADOPTED. ### M-2 REMAINS ### SPECIFIED-NOT-STATED "
    u"### . ### NOTHING DEPOSITS.** *** "
    u"### ### **WHY THIS DOES NOT CONTRADICT b272, SAID BEFORE ANYTHING ELSE.** ### b272's "
    u"\u201c0 OF 16\u201d is TRUE and is re-confirmed here. ### **A SWEEP OF A SPANNING FAMILY IS "
    u"NOT A SWEEP OF THE SPACE:** ### a Rayleigh quotient over a span is not bounded by its "
    u"values at spanning vectors, and the vector that reaches above `2/3` is `g_2 \u2212 g_6`, "
    u"### **WHICH IS NOT A FAMILY MEMBER.** ### b272 also named the exact channel this act opens "
    u"and filed it \u201cFILED, NOT FUDGED\u201d \u2014 ### **IT WAS FILED CORRECTLY AND IT IS "
    u"NOW PAID.** ### **NO PRIOR ACT IS RE-VERDICTED.** *** "
    u"### ### **TWO DIMENSIONS, TWO SPACES.** ### Ambient `dim E_1 = 5` at `(2,2)`, computed by "
    u"exact Gaussian elimination over `Q(\u03b6_16)` with field inversion \u2014 NO NUMERICAL "
    u"RANK. ### b223 records `d_1(2,2) = 2` with `dim Son(2,2) = 9`, and ### **THAT IS THE SECTOR "
    u"INSIDE `Son`. ### AN ACT THAT PUT 2 WHERE 5 BELONGS WOULD HAVE SEARCHED THE WRONG SPACE.** *** "
    u"### ### **THE FORM IS NEITHER HERMITIAN NOR SYMMETRIC, DECIDED FROM ITS OWN DEFINITION** "
    u"\u2014 `A` is RATIONAL and `A \u2260 A^T`. ### **BUT b272's `g_c` ARE REAL, AND ON REAL "
    u"VECTORS THE VALUE DEPENDS ONLY ON THE SYMMETRIC PART.** ### That is the structural fact the "
    u"act turns on, and it is why an EIGENVALUE-FREE, FLOAT-FREE certification exists at all: "
    u"the registration caps eigenvalue decompositions in the deciding runner at ZERO. *** "
    u"### ### **THE STRADDLE, AND BOTH ORDER COMPARISONS ARE RATIONAL.** ### F-CONTROL recovered "
    u"b272's own number: `<A g_0,g_0> = 48`, `<g_0,g_0> = 160`, so ### **`R(g_0) = 3/10`.** ### "
    u"And `w := g_2 \u2212 g_6` gives `<A w,w> = (128/3)(1+\u221a2)`, `<w,w> = 128`, so ### "
    u"**`R(w) = (1+\u221a2)/3`.** ### Then ### **`3/10 < 2/3` because `9 < 20`, and "
    u"`(1+\u221a2)/3 > 2/3` because `\u221a2 > 1` because `2 > 1`.** ### `(\u03b6\u00b2+\u03b6^{-2})\u00b2 "
    u"= 2` verified exactly. ### **NO DECIMAL ENTERS EITHER COMPARISON \u2014 THAT IS THE WHOLE "
    u"COST OF THE ORDERED-FIELD CHANNEL b272 REFUSED, AND IT IS TWO LINES.** *** "
    u"### ### **THE EXHIBITION, EXACT.** ### All three cross terms VANISH, so `v(s) := w + s g_0` "
    u"gives a pure quadratic with no linear term: ### **`s\u00b2 = \u22128/11 + (8/11)\u221a2`**, "
    u"positive by rational arithmetic, and `a_0 + a_2 s\u00b2 = 0` VERIFIED exactly. ### **AND "
    u"WHERE THE COORDINATES LIVE IS CHECKED, NOT ASSUMED:** ### the norms `\u221264/121` and "
    u"`\u221232/121` are both negative, so neither `s\u00b2` nor `s\u00b2/(2+\u221a2)` is a square "
    u"in `Q(\u221a2)` \u2014 ### **THE EXHIBITED VECTOR GENUINELY REQUIRES A QUADRATIC EXTENSION "
    u"OF `Q(\u03b6_16)`. ### REPORTED, NOT HIDDEN.** ### The attaining SET is a CONE, and this "
    u"act exhibits one point of it. *** "
    u"### ### **K1\u2013K4, EACH ANSWERED.** ### K1 YES; K2 YES (`||v||\u00b2 = 128/11 + "
    u"(1280/11)\u221a2`); K4 YES (`v(0) = 10s \u2260 0`, so `v` is ALSO in b271's escape class). "
    u"### **K3 IS THE CHANGE FROM b272:** ### b272 found `<u, g_0> = 0`, forcing ORTHOGONAL "
    u"objects; ### **HERE `<u, w> \u2260 0`, VERIFIED EXACTLY, SO THE ORTHOGONALITY THAT KILLED "
    u"`g_0` AS A REPLACEMENT DOES NOT APPLY TO `v`** ### \u2014 the equivalence-class question is "
    u"OPEN for it, not settled negatively. ### And beyond the K-list, labelled as such: ### **THE "
    u"SAME VECTOR MEETS (SPEC-1) AT `k = n` AND (SPEC-2) AT `k = 1`, AT THIS CELL.** *** "
    u"### ### **THE SECOND CELL WAS RUN AND DID NOT CLOSE.** ### At `(2,3)`, 94 candidates were "
    u"searched at each `k` against `6/7` and `4/7`; 33 have a quotient in `Q(\u221a2)`, ### **ALL "
    u"33 BELOW, NONE ABOVE.** ### **NOT A NEGATIVE RESULT \u2014 A LIMIT OF THE CERTIFICATION, "
    u"NAMED:** ### the order channel reaches `Q(\u221a2)`; the rest live in `Q(\u03b6_64)^+` where "
    u"this act has no exact sign rule and therefore ### MAKES NO CLAIM ### . ### Filed "
    u"`W-ORD-ORDER-CHANNEL`. *** "
    u"### ### **THE FORK, RE-SHAPED.** ### b270 struck C1 ### AGAINST b226's UNIT ### ; this act "
    u"shows both failures were properties of THE UNIT and not of THE CONSTRUCTION, since the same "
    u"ambient pairing against `v` is nonzero at `k = n` and equals act 9's term at `k = 1`. ### "
    u"**SO THE LIVE OBJECT IS C1 COMPOSED WITH C4 \u2014 THE AMBIENT PAIRING WITH A REPLACED UNIT "
    u"\u2014 ONE CANDIDATE, NOT TWO.** ### **C2 AND C3 ARE UNTOUCHED, AND FOR A STATED REASON: "
    u"NEITHER IS A VECTOR STATE.** ### b270's verdict is not disturbed. ### **THIS SEAT RANKS "
    u"NOTHING AND ADOPTS NOTHING.** *** "
    u"### ### **THE SHADOW: NOTHING BUILT, CONDITION CHECKED, RESIDUES ENUMERATED** \u2014 the "
    u"order comparisons are `2 > 1` (a file headed \u201cattainable\u201d whose content is that "
    u"is the double-name species), the values are cyclotomic, ### **AND THE CORE IS THE "
    u"INTERMEDIATE VALUE THEOREM, WHICH IS ANALYSIS AND OUT OF REACH BY CONSTRUCTION.** ### **0 "
    u"`.lean` FILES MOVED, CHECKED NOT ASSUMED.** *** "
    u"### ### **THE DEVIATIONS.** ### This act's exploration ### PRECEDED THE SEAL AND WENT "
    u"FURTHER THAN ANY PRIOR ACT'S ### \u2014 disclosed at `(I1)` before sealing, so its "
    u"\u201cexpectations\u201d are MEASURED NUMBERS and the registration says so in its own body. "
    u"### Part of it used floating point; ### **NO FLOAT ENTERS ANY VERDICT, THE DECIDING RUNNER "
    u"CARRIES ZERO FLOAT TOKENS, AND THE FLOAT PROBE'S HINT ABOUT THE SECOND CELL IS NOT BANKED, "
    u"NOT COUNTED, AND NOT USED.** ### Two patches failed, one silently until the run died on it. "
    u"### And ### **A GATE FAILED ON A NEEDLE THIS SEAT MIS-TYPED \u2014 THE FINDING WAS RIGHT "
    u"AND THE CHECK WAS WRONG, AND THE SUITE SAID `FAIL`, WHICH IS THE ONLY ACCEPTABLE DIRECTION "
    u"FOR THAT ERROR.** *** "
    u"### ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED, AND ONE CELL IS ONE "
    u"CELL.** ### **NOTHING DEPOSITS. ### NOTHING CIRCULATES. ### h2 STANDS EXACTLY WHERE THE "
    u"DEPOSIT LEFT IT.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b272: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b272)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (ATTAINABLE)",
                 u"SCOPE: ONE CELL",
                 u"A SWEEP OF A SPANNING FAMILY IS NOT A SWEEP OF THE SPACE",
                 u"IT WAS FILED CORRECTLY AND IT IS NOW PAID",
                 u"AN ACT THAT PUT 2 WHERE 5 BELONGS WOULD HAVE SEARCHED THE WRONG SPACE",
                 u"NEITHER HERMITIAN NOR SYMMETRIC",
                 u"NO DECIMAL ENTERS EITHER COMPARISON",
                 u"REQUIRES A QUADRATIC EXTENSION",
                 u"DOES NOT APPLY TO `v`",
                 u"ALL\n 33 BELOW, NONE ABOVE".replace(u"\n ", u" "),
                 u"A LIMIT OF THE CERTIFICATION",
                 u"ONE CANDIDATE, NOT TWO",
                 u"NEITHER IS A VECTOR STATE",
                 u"CHECKED NOT ASSUMED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (CLASS NONEMPTY BUT BLOCKED)",
                 u"THE NOISE-FLOOR CHECK IS BUILT, WIRED, FIRED",
                 u"VERDICT: (ESCAPE)",
                 u"C1 IS STRUCK",
                 u"A MATRIX ELEMENT IS NOT A TRACE",
                 u"M-2 IS NOT STATED",
                 u"b226's OWED STEP IS ### PAID ###",
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
