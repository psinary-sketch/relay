# -*- coding: utf-8 -*-
"""b274_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE STRADDLE, GENERALLY (b274)"
PRIOR_MARK = u"(b273)"

NEW = (
    u"*** ### ### **VERDICT: (STRADDLE PARTIAL). ### THE LOW SIDE IS DERIVED FOR EVERY PRIME AND "
    u"EVERY LEVEL n \u2265 2; ### THE HIGH SIDE IS CERTIFIED AT EXACTLY ONE CELL, AND THAT ONE IS "
    u"b273's.** ### **NO UNIT IS ADOPTED. ### M-2 REMAINS ### SPECIFIED-NOT-STATED ### . ### "
    u"NOTHING DEPOSITS.** *** "
    u"### ### **THE THING TO TAKE FIRST IS NOT THE VERDICT.** ### (SPEC-2)'s range `1 \u2264 k "
    u"\u2264 n\u22121` is EMPTY at `n = 1`, and b226 puts EVERY ODD PRIME at level 1 with only "
    u"`p = 2` at level 2. ### **SO UNDER THE RULED CHOICE THE ONLY CELL IN THE WHOLE AGGREGATION "
    u"WITH ANY (SPEC-2) CONTENT AT ALL IS (2,2) \u2014 THE CELL b273 ALREADY SETTLED.** ### The "
    u"\u201cgenerally\u201d of this act is a question about cells the aggregation does not visit "
    u"under b226's choice. ### **AN ACT THAT PROVED A GENERAL STRADDLE AND LET IT READ AS A "
    u"STATEMENT ABOUT THE AGGREGATION WOULD BE THE DOUBLE-NAME SPECIES AT THE LEVEL OF CELLS.** *** "
    u"### ### **S1 \u2014 A CLOSED FORM, DERIVED FROM THE OWNERS RATHER THAN FITTED.** ### `g_0` "
    u"is constant `2` off the ball, and for `k \u2264 n\u22121` no off-ball `m` has `p^k m = 0` "
    u"(that needs `p^{2n\u2212k} | m` with `2n\u2212k > n`), so every factor is `2`. ### Hence "
    u"### **R(g_0) = (q\u22121)/(2(q+1)), INDEPENDENT OF k** ### \u2014 verified exactly at (2,2), "
    u"(3,2), (2,3), (2,4), seven rows, and it reproduces b273's banked `3/10`. *** "
    u"### ### **S3 LOW SIDE \u2014 DERIVED GENERALLY, BY RATIONAL ALGEBRA ALONE. ### THIS IS THE "
    u"ACT'S ONE GENERAL RESULT.** ### The claim is `2(q+1)(q\u2212p^k) \u2212 (q\u22121)\u00b2 > "
    u"0`; expanding gives `q\u00b2 \u2212 2q p^k + 4q \u2212 2p^k \u2212 1`, and since `p^k \u2264 "
    u"q/p \u2264 q/2` we get `2q p^k \u2264 q\u00b2` and `2p^k \u2264 q`, so it is ### **\u2265 "
    u"3q \u2212 1 > 0. ### QED.** ### Control: 308 triples, 0 failures, tightest margin "
    u"`767/131070` at (2,8,7) \u2014 thin, positive, and the proof says why it stays positive "
    u"forever. ### **AND THE GATE RE-DERIVES IT INDEPENDENTLY OVER ITS OWN 288 TRIPLES RATHER "
    u"THAN RE-READING THE RUN.** *** "
    u"### ### **S2 \u2014 THE FAMILY, AND ONE STRUCTURAL GIFT INSIDE A NEGATIVE RESULT.** ### The "
    u"family named from b272's structure is `w_c := g_c \u2212 g_{c+q}`, which at (2,2) IS b273's "
    u"`g_2 \u2212 g_6`. ### **DERIVED AND VERIFIED AT ALL FOUR CELLS: `w_c` VANISHES ON THE BALL "
    u"(the exponentials coincide there, `\u03b6^{jq(c+q)} = \u03b6^{jqc+jN}`) AND `S w_c = q w_c`, "
    u"SO ITS TRANSFORM DOES TOO \u2014 `w_c` LIES IN `Son(p,n)`, b226's OWN SECTOR, WHILE `g_0` "
    u"LIES IN b271's ESCAPE CLASS. ### THE STRADDLE AT (2,2) IS BETWEEN A SONIN VECTOR AND AN "
    u"ESCAPE-CLASS VECTOR** \u2014 a structural fact the campaign did not have. ### **BUT R(w_c) "
    u"IS NOT RATIONAL AT ANY CELL, SO ALL SEVEN ROWS ARE ### UNCERTIFIED ### , WHICH UNDER "
    u"`W-ORD-ORDER-CHANNEL` IS NOT THE SAME AS FALSE. ### NO CLOSED FORM AND NO NEW HIGH WITNESS "
    u"IS DERIVED.** *** "
    u"### ### **(SPEC-3): ### NOT ADVANCED.** ### The low-side derivation is defined at every "
    u"`(p, n \u2265 2)`, which sounds like progress and is not \u2014 (SPEC-3) is a condition on "
    u"the quantity the AGGREGATION uses, and under b226's choice that sits at level 1 for every "
    u"odd prime where (SPEC-2) says nothing. ### **AND THE DISTINCTION IN THE VERDICT'S OWN "
    u"WORDS: AN ATTAINABLE RANGE IS NOT A STATED AGGREGATION. ### M-2 ASKS FOR ONE RULE, ALL "
    u"PLACES, WRITTEN DOWN; KNOWING A SOLUTION EXISTS AT EACH OF SEVERAL CELLS IS NOT A RULE. ### "
    u"THAT IS THE WHOLE DISTANCE STILL TO GO.** *** "
    u"### ### **THE DEVIATION THAT MATTERS, STATED WITHOUT SOFTENING.** ### The pre-seal probe "
    u"printed only the FIRST FOUR cyclotomic coefficients of `<A w_c, w_c>`, saw zeros, and ### "
    u"**INFERRED THE ELEMENT WAS RATIONAL. ### IT IS NOT \u2014 it carries five to eleven nonzero "
    u"coefficients at every cell.** ### From that misread this seat computed `2/7`, `1/6`, `1/5`, "
    u"`4/15` \u2014 ### **NUMBERS THAT DO NOT EXIST** \u2014 and the SEALED registration recorded "
    u"a conclusion on their strength. ### A float check later placed every one of those rows below "
    u"the term, as the registration said. ### **THE CONCLUSION SURVIVED AND THE NUMBERS DID NOT. "
    u"### THAT IS LUCK, NOT ACCURACY, AND IT IS RECORDED AS LUCK.** ### The sealed registration is "
    u"NOT edited; the correction lives in the bank. ### **A PRINT WIDTH IS NOT A DATUM.** *** "
    u"### ### **AND THE ACT'S OWN DECIDING CHANNEL CAUGHT IT** \u2014 it tests rationality exactly "
    u"and printed UNCERTIFIED on all seven rows, which is what the sealed `F-UNCERT` demanded. "
    u"### Two gate needles were also mis-typed, producing a FAIL and a REFUSED; ### **BOTH TIMES "
    u"THE FINDING WAS RIGHT AND THE CHECK WAS WRONG, WHICH IS THE ONLY ACCEPTABLE DIRECTION, AND "
    u"IT IS NOW THE SECOND ACT RUNNING WITH THAT SPECIES.** ### A float probe suggested the "
    u"straddle holds at all seven cells tried; ### **IT IS DISCLOSED AND NOT BANKED, NOT COUNTED, "
    u"AND NOT USED \u2014 THE VERDICT IS PARTIAL PRECISELY BECAUSE A FLOAT PROBE IS NOT A "
    u"CERTIFICATE.** *** "
    u"### ### **FILED, NOT OPENED: `W-ORD-EQUIV-CLASS`** \u2014 closing b273's open "
    u"equivalence-class question for `v` would need the normalized inner products `<u_v, v_v>` "
    u"ACROSS PLACES against von Neumann Def 3.3.2, ### **A CONDITION OVER INFINITELY MANY PLACES "
    u"THAT NO FINITE COMPUTATION SETTLES.** ### Shadow: nothing built, residues enumerated \u2014 "
    u"the low-side inequality is universally quantified over an infinite set so `decide` cannot "
    u"touch it, and compiling the 308-triple CONTROL under a header naming the THEOREM is the "
    u"double-name species, refused for the fourth act running. ### **0 `.lean` FILES MOVED, "
    u"CHECKED NOT ASSUMED.** *** "
    u"### ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED.** ### **NOTHING "
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b273: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b273)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (STRADDLE PARTIAL)",
                 u"THE THING TO TAKE FIRST IS NOT THE VERDICT",
                 u"THE CELL b273 ALREADY SETTLED",
                 u"DOUBLE-NAME SPECIES AT THE LEVEL OF CELLS",
                 u"INDEPENDENT OF k",
                 u"THIS IS THE ACT'S ONE GENERAL RESULT",
                 u"3q \u2212 1 > 0",
                 u"RATHER THAN RE-READING THE RUN",
                 u"LIES IN b271's ESCAPE CLASS",
                 u"IS NOT THE SAME AS FALSE",
                 u"NOT ADVANCED",
                 u"AN ATTAINABLE RANGE IS NOT A STATED AGGREGATION",
                 u"NUMBERS THAT DO NOT EXIST",
                 u"THAT IS LUCK, NOT ACCURACY",
                 u"A PRINT WIDTH IS NOT A DATUM",
                 u"W-ORD-EQUIV-CLASS",
                 u"CHECKED NOT ASSUMED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (ATTAINABLE)",
                 u"SCOPE: ONE CELL",
                 u"VERDICT: (CLASS NONEMPTY BUT BLOCKED)",
                 u"THE NOISE-FLOOR CHECK IS BUILT, WIRED, FIRED",
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
