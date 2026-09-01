# -*- coding: utf-8 -*-
"""b272_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE ESCAPE CLASS (b272)"
PRIOR_MARK = u"(b271)"

NEW = (
    u"*** ### ### **VERDICT: (CLASS NONEMPTY BUT BLOCKED). ### K1, K2, K3 AND K4 ARE SATISFIED; "
    u"### K5 -- (SPEC-2) -- FAILS FOR EVERY MEMBER OF A SPANNING FAMILY.** ### **NO UNIT IS "
    u"ADOPTED; b226's CHOICE STANDS EXACTLY AS RULED. ### M-2 REMAINS ### SPECIFIED-NOT-STATED "
    u"### . ### NOTHING DEPOSITS.** *** "
    u"### ### **COMPONENT 0 \u2014 THE NOISE-FLOOR CHECK IS BUILT, WIRED, FIRED, AND "
    u"### DISCHARGED ### . ### OWED SINCE b266 AND UNBUILT FOR SIX ACTS RUNNING; IT IS NOW IN "
    u"THE COMMAND PATH.** ### `tools/noise_floor.py`, four exhaustive arms (`EXACT`, `AT_FLOOR`, "
    u"`DRIFTING`, `RESOLVED`), fixtures from b264's own eleven printed modes: ### **11 OF 11 "
    u"VERDICTS REPRODUCED.** ### And building it against real numbers taught what this seat "
    u"registered ahead of any evidence and got right: ### **A MAGNITUDE TEST ALONE WOULD HAVE "
    u"PASSED ALL FOUR OF b264's FALSE MODES** ### \u2014 mode 7 sits at `2.178e-8`, ABOVE "
    u"`sqrt(eps)`. ### **THE OBVIOUS GATE WOULD HAVE SHIPPED AND CAUGHT NOTHING; IT IS THE DRIFT "
    u"ARM THAT BITES.** ### That naive answer is now itself a gate fixture, and it must fail. *** "
    u"### ### **THE CHARACTERIZATION: `E_1` HAS A SPANNING SET LYING ENTIRELY INSIDE THE ESCAPE "
    u"CLASS.** ### From b226's own \u201c4q P_1 = (q + S)(1 + Pi)\u201d at `e_c`: ### **`g_c(m) = "
    u"q([m = c] + [m = -c]) + \u03b6^{mc} + \u03b6^{-mc}`** ### , real-valued, and at `m = 0` both "
    u"exponentials are `1`, so ### **`g_c(0) = 2` FOR EVERY `c \u2260 0` \u2014 AND `0` IS IN THE "
    u"BALL.** ### Verified exactly for every `c` at all eight cells. ### Since `{e_c}` spans and "
    u"`P_1` is onto `E_1`, ### **THE BALL-VANISHING VECTORS \u2014 WHICH INCLUDE ALL OF "
    u"`E_1(Son)`, HENCE ALL OF b226's FAMILY \u2014 ARE A PROPER SUBSPACE. ### ESCAPING IS "
    u"GENERIC; BALL-VANISHING IS THE SPECIAL CONDITION.** *** "
    u"### ### **K3 IS THE DOSSIER'S CENTRE, AND IT IS EXACT: `<u, g_c> = 4q\u00b7u(c)`.** ### "
    u"Derived from `u` being `\u03a0`-even with `S u = q u`, then verified at eight cells. ### At "
    u"`c = 0`, `u(0) = 0` because `0` is in the ball, so ### **`<u, g_0> = 0` EXACTLY, AT EVERY "
    u"PLACE** ### \u2014 whence `\u03a3_v |<u_v,g_v> \u2212 1|` DIVERGES, the sequences are not "
    u"equivalent by von Neumann Def 3.3.2, and by Lemma 4.1.1 the incomplete products are ### "
    u"\u201cMUTUALLY ORTHOGONAL\u201d ### . ### **REPLACING b226's UNIT BY b271's WITNESS WOULD "
    u"NOT ADJUST THE OBJECT \u2014 IT WOULD REPLACE IT WITH AN ORTHOGONAL ONE.** ### b226's own "
    u"recorded warning, now arithmetic. ### **AND IT IS A FACT ABOUT `g_0`, NOT ABOUT THE CLASS: "
    u"for `c \u2260 0` the inner product is NONZERO, controlled in that polarity at every cell.** *** "
    u"### ### **K5 IS THE BLOCK.** ### b270 left `(2,2)`, `k = 1` as the only cell where "
    u"(SPEC-2) has anything to say. ### The whole spanning family was swept, normalized, exact: "
    u"`c=0` gives `3/10`, `c=4,12` give `\u22121/18`, `c=8` gives `\u22121/10`, and the other "
    u"twelve are ### NOT RATIONAL AT ALL ### where act 9's term `2/3` is. ### **MEMBERS "
    u"SATISFYING (SPEC-2): 0 OF 16.** ### So (SPEC-2) now fails for b226's `u_v` AND across a "
    u"SPANNING SET: ### **THE OBSTRUCTION IS NOT A PROPERTY OF b226's PARTICULAR CHOICE.** *** "
    u"### ### **WHAT IS NOT SETTLED, WITH THE RESISTANCE NAMED AS PRECISELY AS THE FINDING:** ### "
    u"whether some OTHER element of `E_1` \u2014 a combination rather than a family member \u2014 "
    u"satisfies K5. ### That asks whether a real quadratic form attains a value on a subspace, "
    u"i.e. it needs the ### SIGNATURE ### of a Hermitian form over `Q(\u03b6_N)`, equivalently "
    u"ORDER COMPARISONS BETWEEN REAL ALGEBRAIC NUMBERS. ### **A DIFFERENT CHANNEL FROM REDUCTION "
    u"MODULO \u03a6_N, NOT WHAT THIS ACT'S SEAL AUTHORIZES, AND NOT OPENED. ### FILED, NOT "
    u"FUDGED.** *** "
    u"### ### **THE DOSSIER, ROUTED, WITH ### NO RECOMMENDATION ### IN ANY DIRECTION.** ### "
    u"Replacing b226's choice costs: ### **the OBJECT ITSELF** ### (orthogonal, per K3); ### "
    u"**b268's RESULT** ### (its nonvanishing is about a different vector and would be spent "
    u"work); ### **THE LEVEL-LIMIT PREMISE** ### (a non-`Son` unit is not in that tower, so the "
    u"placement would be RE-DERIVED, not re-cited); and ### **THE CHOICE-DEPENDENCE TRIPWIRE** ### "
    u"\u2014 b226 records the canonicity as \u201cA DEFINITION MADE BY RULING, NOT A "
    u"THEOREM\u201d, and ### **A SECOND RULED CHOICE DOES NOT ANSWER THE FIRST; IT DOUBLES IT.** "
    u"### What it would settle: ### **NOTHING THIS ACT CAN NAME** ### \u2014 it buys (SPEC-1) and "
    u"loses (SPEC-2), and M-2 would still not be stated. *** "
    u"### ### **THE SELECTION NOTE, AT PATTERN GRADE, NOT PROMOTED.** ### If (SPEC-1) can only be "
    u"met by units with ball support, the identity would CONSTRAIN THE VON NEUMANN CLASS \u2014 "
    u"the choice-dependence question restated as a determination principle. ### Its promotion "
    u"criterion is a derivation that no ball-vanishing unit can meet (SPEC-1); ### **STATUS: "
    u"UNMET, AND THE NEAR MISS IS RECORDED BECAUSE IT IS TEMPTING** ### \u2014 b271's absorption "
    u"lemma gives exactly that for ONE per-place quantity, but (SPEC-1) is a demand on a quantity "
    u"NOT YET CHOSEN. ### **MET FOR ONE CONSTRUCTION AND NOT IN GENERAL IS EXACTLY NOT MEETING "
    u"IT.** *** "
    u"### ### **THE SHADOW: NOTHING BUILT, CONDITION CHECKED, RESIDUES ENUMERATED.** ### Each "
    u"candidate is a definition this seat would write itself, a triviality (`3/10 \u2260 2/3` "
    u"under a header saying \u201c(SPEC-2) fails\u201d \u2014 the double-name species), "
    u"cyclotomic, or already compiled at b270/b271. ### **0 `.lean` FILES MOVED, CHECKED NOT "
    u"ASSUMED.** *** "
    u"### ### **THE DEVIATIONS.** ### Component 0's first fixtures were built from b264's ROUNDED "
    u"PRINTOUT and ### **EVERY RESOLVED MODE'S DRIFT SILENTLY BECAME ZERO** ### \u2014 caught "
    u"only because the self-test divided by it. ### **A FIXTURE BUILT FROM A ROUNDED PRINTOUT IS "
    u"NOT THE MEASUREMENT.** ### The term scan found four live banned stems in the registration "
    u"AND in the tool, before the seal. ### And ### **NO DEAD FIXTURE THIS ACT, MECHANIZED RATHER "
    u"THAN REMEMBERED:** ### gate 13 checks every run-based fixture needle is reachable, after "
    u"b270 and b271 EACH shipped one that could never fire. *** "
    u"### ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED.** ### But ### **THE "
    u"NOISE-FLOOR LINE IS STRUCK FROM THE DEBT LIST \u2014 THE FIRST ONE STRUCK IN THE WHOLE "
    u"ARC.** ### **NOTHING DEPOSITS. ### NOTHING CIRCULATES. ### h2 STANDS EXACTLY WHERE THE "
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b271: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b271)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"VERDICT: (CLASS NONEMPTY BUT BLOCKED)",
                 u"THE NOISE-FLOOR CHECK IS BUILT, WIRED, FIRED",
                 u"A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR",
                 u"`E_1` HAS A SPANNING SET LYING ENTIRELY INSIDE THE ESCAPE CLASS",
                 u"ESCAPING IS\n GENERIC".replace(u"\n ", u" "),
                 u"MUTUALLY ORTHOGONAL",
                 u"A FACT ABOUT `g_0`, NOT ABOUT THE CLASS",
                 u"MEMBERS SATISFYING (SPEC-2): 0 OF 16",
                 u"FILED, NOT",
                 u"NO RECOMMENDATION",
                 u"A SECOND RULED CHOICE DOES NOT ANSWER THE FIRST; IT DOUBLES IT",
                 u"UNMET, AND THE NEAR MISS IS RECORDED",
                 u"CHECKED NOT\n ASSUMED".replace(u"\n ", u" "),
                 u"NO DEAD FIXTURE THIS ACT",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"VERDICT: (ESCAPE)",
                 u"SILENCE IS NOT A PROPERTY OF THE MODEL",
                 u"C1 IS STRUCK",
                 u"THE FORK IS THREE",
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
