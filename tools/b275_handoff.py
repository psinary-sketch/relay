# -*- coding: utf-8 -*-
"""b275_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE RULE STATED (b275)"
PRIOR_MARK = u"(b274)"

NEW = (
    u"*** ### ### **VERDICT: (RULE STATED). ### ONE RULE, WRITTEN WHOLE, EVERY CONSTITUENT "
    u"UNFOLDED TO AN OWNER.** ### T1 (SPEC-1) PASSES, DERIVED; T3 and T4 pass; ### **T2 (SPEC-2) "
    u"IS VACUOUS AT SEVEN CELLS AND FAILS AT THE EIGHTH.** ### **AND THE RULE'S OBJECT IS "
    u"MUTUALLY ORTHOGONAL TO b226's \u2014 DERIVED, NOT OPEN.** ### **NOTHING IS ADOPTED. ### M-2 "
    u"REMAINS ### SPECIFIED-NOT-STATED ### . ### NOTHING DEPOSITS.** *** "
    u"### ### **WHAT THE RULE IS NOT, SAID BEFORE WHAT IT IS.** ### It is NOT adopted \u2014 "
    u"replacing a ruling is the author's alone. ### **IT IS NOT SHOWN EQUIVALENT TO b226's "
    u"SEQUENCE; IT IS SHOWN ### NOT ### EQUIVALENT TO IT.** ### And ### **IT DOES NOT INHERIT "
    u"b273's (SPEC-2) SUCCESS: b273's vector is `w + s g_0`, THIS RULE'S IS `g_0`, AND LETTING "
    u"THE ONE ATTACH TO THE OTHER WOULD HAVE BEEN THIS ACT'S WORST AVAILABLE ERROR.** *** "
    u"### ### **THE CANONICAL INDEX DERIVES \u2014 IT IS NOT PICKED.** ### The quotient channel "
    u"is built on `m \u2192 pm`; its fixed points solve `(p\u22121)m = 0 mod N`, and "
    u"`gcd(p\u22121, p^{2n}) = 1` at EVERY prime, so ### **THE ONLY SOLUTION IS `m = 0`: `e_0` IS "
    u"THE UNIQUE BASIS VECTOR FIXED BY THE VERY MAP THE CHANNEL QUOTIENTS BY.** ### Verified at "
    u"all eight cells. ### **AND THE CONVENIENT ARGUMENT IS SHOWN TO FAIL RATHER THAN QUIETLY "
    u"SWAPPED: the involution `\u03a0` alone fixes TWO indices at `p = 2` \u2014 `[0, 8]` \u2014 "
    u"so an act that had argued from `\u03a0` would have had a hole EXACTLY AT THE ONE PLACE THE "
    u"CAMPAIGN CARES MOST ABOUT.** *** "
    u"### ### **THE RULE: `u'_p := 4q P_1 e_0 / \u2016 4q P_1 e_0 \u2016` at the cell "
    u"`(p, \u2113(p))`, with `\u2113(p) = 2 if p = 2, else 1`.** ### Every constituent has an "
    u"owner \u2014 `4q P_1 = (q+S)(1+\u03a0)`, `S`, `\u03a0`, `4q P_1 e_0 = 2q e_0 + 2\u00b71`, "
    u"and `\u2113(p)` from the arrival depth `d_1(2,1) = 0`. ### **AND MEMBERSHIP IS CHECKED, NOT "
    u"INHERITED: `S g_0 = q g_0` verified exactly at all eight cells.** *** "
    u"### ### **T1 \u2014 (SPEC-1) PASSES, DERIVED RATHER THAN SURVEYED.** ### b271 gives "
    u"`<U^\u2113 S_quot g_0, g_0>\u00b7p^{\u2113/2} = 4(N\u2212q)`, and `N = q\u00b2 > q` for "
    u"every `q \u2265 2`, so ### **THE VALUE IS NONZERO AT EVERY PLACE BY ARITHMETIC.** ### "
    u"Controlled exactly: 48, 24, 80, 168, 440, 624, 1088, 1368. *** "
    u"### ### **T2 \u2014 THE RULE FAILS (SPEC-2) AT THE ONE CELL WHERE IT HAS CONTENT.** ### At "
    u"`\u2113 = 1` the range is EMPTY, so (SPEC-2) is ### **VACUOUS THERE \u2014 A VACUITY AND "
    u"NOT A TRIUMPH** \u2014 seven of eight cells, which under b226's `\u2113(p)` is every odd "
    u"place. ### At `(2,2)` the rule gives `R(g_0) = 3/10` against act 9's `2/3`. ### **THEY "
    u"DIFFER. ### SO A RULE THAT MEETS (SPEC-2) MUST BE PIECEWISE AT `p = 2`, TAKING b273's `v` "
    u"THERE.** ### That is writable \u2014 a finite exception, and b226's own rule is already "
    u"piecewise in the LEVEL \u2014 ### **BUT IT IS A COST AND IT IS STATED AS ONE, NOT "
    u"ABSORBED**, and the piecewise branch inherits b273's own openness. *** "
    u"### ### **THE EQUIVALENCE: CHECKED FOR THIS RULE, NOT INHERITED \u2014 AND SETTLED "
    u"NEGATIVELY.** ### b272 derives `<u, g_0> = 0` EXACTLY at every place, re-confirmed here at "
    u"all eight cells; so normalized, `|<u_v,u'_v> \u2212 1| = 1` at EVERY place and the sum "
    u"DIVERGES. ### By von Neumann Def 3.3.2 the sequences are NOT equivalent, and by Lemma 4.1.1 "
    u"the incomplete products are ### **MUTUALLY ORTHOGONAL. ### THE RULE NAMES A DIFFERENT "
    u"OBJECT \u2014 NOT A REFINEMENT OF b226's, NOT A CORRECTION OF IT.** ### **AND "
    u"`W-ORD-EQUIV-CLASS` IS NOT CLOSED BY THIS: its subject is b273's `v`, where `<u, w> \u2260 "
    u"0`. ### A DIFFERENT VECTOR AND A DIFFERENT QUESTION.** *** "
    u"### ### **THE ADOPTION DOSSIER, ROUTED WITH NO RECOMMENDATION.** ### Adopting would cost: "
    u"### **THE OBJECT** ### (orthogonal, so replacement not refinement); ### **THE LEVEL-LIMIT "
    u"PREMISE, WHICH LAPSES OUTRIGHT** ### \u2014 b226's warrant is b198's closure sentence about "
    u"the level tower OF `Son`, and `g_0` is NOT in `Son`, which is precisely what puts it in "
    u"b271's escape class, so this is ### **NOT A WEAKENED PREMISE BUT AN ABSENT ONE**; ### "
    u"**b268's RESULT** ### (a different generator, spent work); and ### **THE CHOICE-DEPENDENCE "
    u"TRIPWIRE \u2014 A SECOND RULED CHOICE DOES NOT ANSWER THE FIRST, IT DOUBLES IT**, now with "
    u"a derived orthogonality attached. *** "
    u"### ### **AND WHY THIS IS STILL NOT M-2, SAID PRECISELY: ### M-2 ASKS FOR AN AGGREGATION "
    u"\u2014 A FUNCTION OVER PLACES WITH A STATED VALUE \u2014 AND THIS ACT PRODUCES A ### UNIT "
    u"RULE ### , WHICH IS AN INPUT TO ONE AND NOT ONE. ### A UNIT AT EVERY PLACE IS NOT A NUMBER "
    u"AT EVERY PLACE, AND M-2 WANTS THE SECOND.** *** "
    u"### ### **THE DEVIATIONS.** ### Every derivation preceded the seal and was read off "
    u"already-banked results, disclosed at `(H1)` \u2014 ### **A WEAK PREDICTION, AND EVERY ONE "
    u"HELD.** ### The act nearly argued canonicity from `\u03a0`, which fails at `p = 2`; caught "
    u"before the registration. ### **AND THE FERRY'S SCOPE LINE SAID THE EQUIVALENCE QUESTION IS "
    u"\u201cNOT SETTLED HERE\u201d \u2014 FOR THIS RULE THAT WOULD HAVE BEEN WRONG, SO THE ACT "
    u"FOLLOWED THE EVIDENCE AND FLAGS THE DEPARTURE RATHER THAN SMOOTHING IT OVER.** ### A gate "
    u"needle was mis-typed for the THIRD act running; filed `W-ORD-NEEDLE-SOURCE` \u2014 ### "
    u"**GATE NEEDLES SHOULD BE EXTRACTED FROM THE EMITTING FILE, NOT RETYPED FROM MEMORY; THE "
    u"CORPUS ALREADY OWNS THE MACHINERY AND THE GATES SIMPLY DO NOT USE IT.** ### Shadow: nothing "
    u"built, residues enumerated, fifth act running on the same ground. ### **0 `.lean` FILES "
    u"MOVED, CHECKED NOT ASSUMED.** *** "
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b274: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b274)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (RULE STATED)",
                 u"WHAT THE RULE IS NOT, SAID BEFORE WHAT IT IS",
                 u"THIS ACT'S WORST AVAILABLE ERROR",
                 u"THE UNIQUE BASIS VECTOR FIXED BY THE VERY MAP",
                 u"THE CAMPAIGN CARES MOST ABOUT",
                 u"NONZERO AT EVERY PLACE BY ARITHMETIC",
                 u"A VACUITY AND\n NOT A TRIUMPH".replace(u"\n ", u" "),
                 u"MUST BE PIECEWISE AT `p = 2`",
                 u"MUTUALLY ORTHOGONAL",
                 u"A DIFFERENT VECTOR AND A DIFFERENT QUESTION",
                 u"NOT A WEAKENED PREMISE BUT AN ABSENT ONE",
                 u"IT DOUBLES IT",
                 u"UNIT RULE",
                 u"W-ORD-NEEDLE-SOURCE",
                 u"CHECKED NOT ASSUMED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (STRADDLE PARTIAL)",
                 u"VERDICT: (ATTAINABLE)",
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
