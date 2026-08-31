# -*- coding: utf-8 -*-
"""b271_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE TOP-LEVEL NO-GO (b271)"
PRIOR_MARK = u"(b270)"

NEW = (
    u"*** ### ### **VERDICT: (ESCAPE). ### `E_1` MEMBERSHIP DOES NOT FORCE VANISHING ON THE "
    u"BALL, AND THE WITNESS VANISHES NOWHERE AT ALL.** ### So ### **(SPEC-1) IS SATISFIABLE BY "
    u"AN OBJECT BUILT FROM THE TRUNCATED MODEL AT LEVEL `n`** ### , and ### **THE TOP-LEVEL "
    u"SILENCE IS NOT A PROPERTY OF THE MODEL.** ### **NO CANDIDATE IS ADOPTED. ### M-2 REMAINS "
    u"### SPECIFIED-NOT-STATED ### . ### NOTHING DEPOSITS.** *** "
    u"### ### **THE ACT'S WHOLE VALUE IS THAT IT KEPT TWO SPACES APART.** ### `E_1` is the `+1` "
    u"sector of `M = S/q` on the AMBIENT `Z/N`; `E_1(Son)` is that sector restricted to "
    u"`Son(p,n)`, and b226 defines `Son` as \u201cthe vectors on Z/p^{2n} vanishing on a ball AND "
    u"on its transform image\u201d. ### **SO BALL-VANISHING IS PART OF WHAT `Son` MEANS AND IS "
    u"NOT A FACT ABOUT `E_1`. ### AN ACT THAT CONFLATED THEM WOULD HAVE REPORTED A THEOREM WHERE "
    u"THERE IS A TAUTOLOGY, AND CALLED THE MODEL BARRED WHEN ONLY ONE SUBSPACE OF IT IS.** *** "
    u"### ### **S1 \u2014 THE BALL-ABSORPTION LEMMA, NOW STATED GENERALLY WITH ITS HYPOTHESES.** "
    u"### For `g` vanishing on the ball and ### **`f` ARBITRARY** ### , `\u03a3_m f(m) conj(g(p^n "
    u"m)) = 0`, because `p^n m` lies in the ball for EVERY `m`. ### **THE SUM IS ZERO TERMWISE, "
    u"NOT BY CANCELLATION** \u2014 nothing can be arranged to defeat it. ### b270's `P(n) = 0` is "
    u"this lemma at `f = S_quot u_v`, and b270's `Tr(U^n S_quot) = 0` is the same absorption on "
    u"the diagonal. ### **CONTROLLED IN BOTH POLARITIES WITH TWO UNRELATED `f`.** *** "
    u"### ### **S2 \u2014 THE WITNESS, IN CLOSED FORM FROM b226's OWN IDENTITY.** ### From "
    u"\u201c4q P_1 = (q + S)(1 + Pi)\u201d at `e_0`: `Pi e_0 = e_0` and `S e_0 = 1`, so ### **`g "
    u":= 4q P_1 e_0 = 2q e_0 + 2\u00b71`.** ### Membership CHECKED and not inherited from "
    u"provenance: `(S g)(m) = 2q + 2N[m=0]` equals `q g(m) = 2N[m=0] + 2q` since `q\u00b2 = N`, so "
    u"### **`M g = g`, VERIFIED EXACTLY AT ALL EIGHT CELLS** ### \u2014 and `g(jq) = 2` on the "
    u"ball. *** "
    u"### ### **AND THE ESCAPE IS MATERIAL, NOT MERELY FORMAL.** ### The closed form was "
    u"REGISTERED BEFORE IT WAS COMPUTED and matched at all eight cells: ### **`<U^n S_quot g, g> "
    u"p^{n/2} = 4(N \u2212 q)`** ### \u2014 48, 24, 80, 168, 440, 624, 1088, 1368. ### **A "
    u"PROPERTY OF A CLASS, NOT A CANDIDATE: no table headed by act 9, no target compared, and "
    u"(SPEC-2) AND (SPEC-3) DELIBERATELY NOT TESTED FOR IT.** *** "
    u"### ### **THE ESCAPE CLASS IS `E_1` MINUS `Son` \u2014 THE `+1` SECTOR WITH NONZERO BALL "
    u"MASS \u2014 AND THE WITNESS FAILS BOTH HALVES OF `Son` AT ONCE, FOR ONE REASON:** ### it is "
    u"an eigenvector, `S g = q g`, so its transform is a nonzero multiple of itself and cannot "
    u"vanish where it does not. ### **WHAT THE ACT DOES NOT DO, AND SAYS SO: IT DOES NOT SURVEY "
    u"THE CLASS; THE WITNESS IS THE MOST DEGENERATE MEMBER OF `E_1` THERE IS, CHOSEN BECAUSE A "
    u"REFUTATION WANTS THE SIMPLEST WITNESS; AND IT IS EVIDENCE THE CLASS IS NONEMPTY, NOT THAT "
    u"IT HOLDS ANYTHING THE PROGRAMME WANTS.** ### Filed `W-ORD-ESCAPE-SURVEY`. *** "
    u"### ### **THE SCOPE, STATED AS PRECISELY AS THE VERDICT.** ### It is about the TRUNCATED "
    u"model on `Z/p^{2n}` at `n = ell(p)`. ### **IT SAYS NOTHING ABOUT THE COMPLETE ROSTER** "
    u"(b15's clause governs), ### **NOTHING ABOUT `h2`, AND IT DOES NOT REFUTE THE IDENTITY.** "
    u"### **AND IT DOES NOT RE-VERDICT b270:** ### b270 killed C1 for a `Son` vector; this act "
    u"shows that death was ### NOT A MODEL-WIDE BARRIER ### , which is a statement about SCOPE "
    u"and not a change of verdict. ### b270's `Tr(U^n S_quot) = 0` is re-confirmed as the "
    u"lemma's negative polarity and stands exactly as banked. *** "
    u"### ### **THE ENTAILMENTS, ONE BY ONE, WITH NO RANKING.** ### **C2** \u2014 unchanged in "
    u"kind, but its target `E_1` is now known to be STRICTLY LARGER than `E_1(Son)`. ### **C3** "
    u"\u2014 b269 filed it as \u201cthe only candidate that would give a number defined AT `k = "
    u"n`\u201d, and this act exhibits such a number that does NOT come from C3; ### **WHETHER "
    u"b269's LINE IS AMENDED IS ROUTED TO THE AUTHOR AND NOT TAKEN** \u2014 it was right about "
    u"the candidates in its own dossier, every one of which stays inside `Son`. ### **C4** \u2014 "
    u"### **NOW HAS AN ADDRESS**, the exact complement of what b270 ruled out. *** "
    u"### ### **THE RULING ITEM, STATED IN FULL AND NOT TAKEN.** ### To reach the class the unit "
    u"would have to ### **LEAVE `Son(p,n)`** ### , not merely change index within it; ### **b226's "
    u"WARRANT FOR PLACING THE UNIT IN THE LIMIT WOULD LAPSE**, since that warrant is b198 (I2)'s "
    u"closure sentence about the level tower OF `Son`, so the placement would have to be "
    u"RE-DERIVED and not re-cited; and b268's A1 would have to be re-run for the new unit. ### "
    u"**THAT IS A RULING WITH A REAL PRICE, AND IT IS THE AUTHOR'S.** *** "
    u"### ### **THE SHADOW, WITH ONE STEP DELIBERATELY LEFT OUT.** ### "
    u"`Core/AbsorptionFunctionalShadow.lean`: ### **7 TERMINALS, ALL PRINTING \u201cdoes not "
    u"depend on any axioms\u201d, REPORTED FROM THE PRINTED PROFILE**, flip test exits 1. ### It "
    u"compiles the lemma's functional form for two unrelated `f` AND the converse polarity, "
    u"i.e. exactly ### **BALL-VANISHING IS LOAD-BEARING, NOT DECORATIVE.** ### **IT LEAVES OUT `S "
    u"g = q g`, WHICH RESTS ON A CHARACTER SUM AND IS NOT FINITE-DECIDABLE HERE \u2014 A TOY OF "
    u"IT WOULD HAVE COMPILED CLEANLY AND SETTLED NOTHING. ### AND IT COMPILES NO BARRIER, BECAUSE "
    u"THIS ACT HAS NONE.** *** "
    u"### ### **THE DEVIATIONS, AND THE FIRST TWO ARE THE ACT'S OWN INSTRUMENTS FAILING.** ### "
    u"The shadow's first draft ### **COMPILED WITH EVERY TERMINAL RESTING ON `sorryAx`** ### (it "
    u"used `at`, a Lean keyword) \u2014 ### **ONLY THE PRINTED PROFILE SHOWED IT, WHICH IS WHY "
    u"b227's STANDARD EXISTS.** ### The second draft compiled cleanly and still failed its own "
    u"header, six of seven terminals printing `propext`; ### **THE HEADER WAS NOT WEAKENED TO "
    u"MATCH THE PROFILE \u2014 THE ENCODING WAS CHANGED UNTIL THE PROFILE MATCHED THE HEADER.** "
    u"### And ### **A GATE FIXTURE COULD NEVER HAVE FIRED** ### (it demanded a header followed by "
    u"a row that is never first), the SECOND occurrence of b270's species in the act written "
    u"against it. ### **THE NOISE-FLOOR CHECK IS UNBUILT FOR THE SEVENTH ACT RUNNING, RESTATED AS "
    u"OWED AND NOT STRUCK.** *** "
    u"### ### **THE SEAM'S DEBT, ITEM 1, IS STILL NOT PAID. ### M-2 IS OWED.** ### The act showed "
    u"the obstruction is not where it looked \u2014 ### **IT IS IN `Son`, NOT IN THE MODEL** \u2014 "
    u"and gave C4 an address. ### **THAT IS NOT STATING M-2.** ### **NOTHING DEPOSITS. ### "
    u"NOTHING CIRCULATES. ### h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b270: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b270)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    # ### THIS ACT'S OWN HEADLINE ASSERTIONS, EACH A SENTENCE THE BANK ALSO CARRIES.
    for must in (u"VERDICT: (ESCAPE)",
                 u"DOES NOT FORCE VANISHING ON THE BALL",
                 u"SILENCE IS NOT A PROPERTY OF THE MODEL",
                 u"KEPT TWO SPACES APART",
                 u"THE SUM IS ZERO TERMWISE, NOT BY CANCELLATION",
                 u"VERIFIED EXACTLY AT ALL EIGHT CELLS",
                 u"A PROPERTY OF A CLASS, NOT A CANDIDATE",
                 u"IT DOES NOT SURVEY THE CLASS",
                 u"IT DOES NOT RE-VERDICT b270",
                 u"NOW HAS AN ADDRESS",
                 u"THAT IS A RULING WITH A REAL PRICE",
                 u"REPORTED FROM THE PRINTED PROFILE",
                 u"COMPILED WITH EVERY TERMINAL RESTING ON `sorryAx`",
                 u"A GATE FIXTURE COULD NEVER HAVE FIRED",
                 u"NO CANDIDATE IS ADOPTED",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    # ### AND THE PRIOR HEADLINES MUST SURVIVE THE DEMOTION, NOT BE REWRITTEN AWAY.
    for kept in (u"C1 IS STRUCK",
                 u"THE FORK IS THREE",
                 u"A MATRIX ELEMENT IS NOT A TRACE",
                 u"M-2 IS NOT STATED",
                 u"HALT-WITH-DOSSIER",
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
