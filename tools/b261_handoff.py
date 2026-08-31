# -*- coding: utf-8 -*-
"""b261_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"E2even's TURN (b261)"
PRIOR_MARK = u"(b260)"

NEW = (
    u"*** ### ### **J2 IS ### REFUTED ### . ### `E2even` DOES NOT DECREASE MONOTONICALLY: IT "
    u"RISES FROM `0` ON `(1, a_0]` AND FALLS ONLY AFTERWARDS, WITH `a_0` IN `(1.75, 2]`.** "
    u"### ### **AND b255's LADDER STARTS AT `a^2 = 2` -- THE FIRST CELL AFTER THE TURN. ### THE "
    u"SIXTEEN-CELL MONOTONE STRETCH IS A FACT ABOUT WHERE THE LADDER BEGINS, NOT ABOUT THE "
    u"FUNCTION.** ### That is not a criticism of b255, which chose its ladder by affordability and "
    u"said so, and `a^2 = 2` is the smallest cell at which the staircase admits any prime at all. "
    u"### **b255 IS NOT RE-VERDICTED (b246's RULE).** *** "
    u"### ### **THE REFUTATION IS ### DERIVED ### , NOT MEASURED, AND IT IS TWO LINES:** "
    u"### `eps_even(1) = 0` is the OWNER'S OWN SUPPORT LINE (*\"integrand supported ONLY on u in "
    u"[rho^-1, 1] -> eps(1) = 0\"*), so `E2even(a) -> 0` as `a -> 1+`; and `E2even > 0` for "
    u"`a > 1`. ### **A FUNCTION THAT STARTS AT ZERO AND IS POSITIVE AFTERWARDS RISES SOMEWHERE.** "
    u"### The six probe cells are the CONTROL that the derived rise is where it was said to be: "
    u"`0.155, 0.295, 0.527, 0.766, 0.903, 0.993` against `1.0023` at `a^2 = 2`, ### **SIX OF SIX "
    u"SMALLER AND RISING.** *** "
    u"### **THE PIVOT WAS A DILATION IDENTITY, EXACT ON THE INSTRUMENT'S OWN GRID:** the bump's "
    u"`t`-grid is `a`-independent and `a` enters ONLY through `L = log a`, so "
    u"### **`corr_a(u) = (1/L) psi(u/L)` WITH `psi` FIXED**, and "
    u"### **`E2even(a) = EXPECTATION over s ~ p of eps_even(a^s)`** with `p := 2 psi` a PROBABILITY "
    u"DENSITY. ### **THE ENTIRE `a`-DEPENDENCE SITS IN THE ARGUMENT.** ### Measured two ways: "
    u"`L*corr_a` identical across 22 cells to `1.307e-13` against a `1e-12` bar fixed before any "
    u"value; and the reduced form against the instrument to `1.334e-13`. *** "
    u"### ### **A REGISTERED FALSIFIER FIRED -- F4 -- AND IT IS THE ACT'S SECOND RESULT: "
    u"### `eps_even` DECAYS ### WITH OSCILLATION ### , NOT MONOTONICALLY.** ### 448 of 1676 "
    u"samples past the peak rise. ### **THE ARTEFACT HYPOTHESIS WAS TESTED FIRST AND KILLED AT "
    u"BOTH AXES: the rise count is 111 at EVERY `NG` from 200 to 1600 and the kernel agrees to "
    u"`~2e-12`; `NQ` 700-1100 agrees to `~1e-9`. ### AND THE SWEEP IS SHOWN ABLE TO SEE A FAILURE "
    u"(`5.674e+00` at a starved `NG = 12`), SO ITS FLATNESS IS EVIDENCE.** ### **THE OSCILLATION "
    u"IS IN THE ### LEADING ### MODE -- mode 0 is the ONE sign-definite mode and still rises past "
    u"its own peak 107 times -- SO THE COMFORTABLE EXPLANATION, CANCELLATION BETWEEN MODES, IS "
    u"WRONG.** ### A third observation, unasked for: on this range `E2even` is effectively a "
    u"TWO-MODE object (modes 4-10 are four to twelve orders below the leading mode). *** "
    u"### **THREE OF THE FERRY'S FOUR STEP-EXPECTATIONS FAILED, ALL THREE DECLARED IN THE "
    u"REGISTRATION BEFORE THE RUN.** ### S2 (`K_even >= 0`) is ### **BENCH-ONLY** ### -- only mode "
    u"0 is sign-definite, so the sum's sign is a CANCELLATION fact and no termwise argument exists; "
    u"b250's S3(a) wall is the same wall. ### S3 (dilated `corr` non-increasing) is "
    u"### **FALSE NECESSARILY**: `r psi(r)` vanishes at both ends, so it must decrease somewhere, "
    u"and the ferry's own S3 falsifier fires by construction. *** "
    u"### **S4b, ABOVE THE TURN: STRICTLY DECREASING AT ### 79 ### STEPS ON A DENSE GEOMETRIC "
    u"LADDER, NOT FIFTEEN.** ### Sixteen cells could not have answered it, because the kernel "
    u"oscillates and `E2even` averages it. ### **AND IT IS STILL BENCH: NO DERIVATION, BECAUSE "
    u"EVERY POSITIVITY ARGUMENT DIED AT S3.** *** "
    u"### **ONE AXIS MOVED AND WAS DECLARED BEFORE ANY VALUE: the `rho`-grid now STARTS AT "
    u"`rho = 1` EXACTLY and is DENSE ON `[1,2]` (1999 points).** ### b255's grid starts above 1 and "
    u"carries ~1.5 points below `a^2 = 1.05`, so ### **(W1)'s `np.interp` CLAMP WOULD HAVE "
    u"FLATTENED EXACTLY THE REGION THE TURN LIVES IN, SILENTLY.** ### The cost is printed: G-REPRO "
    u"against b255 is worst `5.338e-04` at `a^2 = 2`, falling to `6.5e-06` at `a^2 = 64` -- "
    u"### **LARGEST WHERE b255's GRID WAS COARSEST, WHICH IS THE SIGNATURE OF THE REPAIR RATHER "
    u"THAN OF A DISAGREEMENT.** *** "
    u"### **THE SHADOW: `Core/E2EvenMonotoneShadow.lean`, VANILLA, `decide` ONLY, ### 11 TERMINALS "
    u"AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED AND READ.** ### Its load-bearing polarity control "
    u"is `the_ladder_predicate_fails_below_the_turn` -- ### **THE LADDER'S OWN DECREASE PREDICATE "
    u"FAILS ACROSS THE TURN, WHICH IS THE ACT'S FINDING AS ARITHMETIC.** ### Three FALSE statements "
    u"of the same shape were REFUSED by the same `decide`, lean exit 1. ### **IT DOES NOT COMPILE "
    u"J2 IN EITHER DIRECTION.** *** "
    u"### ### **TWO HARNESS DEFECTS, BOTH MINE, BOTH DISCLOSED.** ### First run "
    u"### **10 PASS / 1 FAIL / 1 REFUSED, NOT CLEAN.** ### (1) ### **A SUMMARY LINE I APPENDED TO "
    u"THE PROFILE RESTATED THE EXACT STRING IT WAS COUNTING AND BECAME A TWELFTH MATCH OF IT** -- "
    u"b213's species, arriving through an annotation added for the reader. ### (2) a needle that "
    u"was NEARLY the sentence, dropping two words from the middle. ### ### **THAT IS b229's "
    u"SPECIES AND THE ### THIRD CONSECUTIVE ACT ### CAUGHT BY IT (b229, b260, b261). ### THE "
    u"PATTERN IS NAMED RATHER THAN RE-REPAIRED: A NEEDLE TYPED FROM MEMORY OF A SENTENCE IS NOT "
    u"THE SENTENCE, AND THE HABIT -- NOT THE MATCHER -- IS THE HAZARD.** ### Re-run 12/12 CLEAN. "
    u"### **AND b260's LESSON LANDED: THE REGISTRATION WAS TERM-SCANNED (0 LIVE USES) BEFORE "
    u"BANKING AND NEVER TOUCHED AFTERWARDS, SO ITS mtime EVIDENCE SURVIVES THIS TIME.** *** "
    u"### ### **WHAT THE FOOT ASKED FOR AND WHAT IT GOT, SAID PLAINLY: *\"both terms of resid(A) "
    u"are then signed by theorem or the exception is named.\"* ### NEITHER BRANCH WAS TAKEN. "
    u"### J1 SIGNED THE JUNCTION BY THEOREM; ### **J2 DID NOT SIGN `E2even` -- IT REFUTED THE "
    u"MONOTONICITY CLAIM AND LEFT THE POSITIVITY AT BENCH.** ### **SO b255's (SIGN-EVENT) QUESTION "
    u"IS NOT CLOSED AND IS FURTHER FROM CLOSING THAN THE FOOT PROJECTED.** ### The arc, honestly: "
    u"ONE TERM SIGNED BY THEOREM, ONE TERM'S CLAIM REFUTED AND ITS SIGN STILL BENCH.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) J3 -- THE JUNCTION AT THE LEVEL LIMIT, with b260's "
    u"formula quoted as its object; ### J1's METHOD ### DOES ### TRANSFER TO J3, UNLIKE J2's, "
    u"because there IS a per-term closed form and a shared index set -- but b15 governs and a level "
    u"limit at fixed `p` decides nothing global.** ### **(2) `W-ORD-EPS-DECAY` (NEW) -- prove "
    u"`eps_even -> 0`; it is S5's ONLY import and the limit note rests entirely on it.** "
    u"### **(3) `W-ORD-TQ-IDENTIFY` (b260) -- prove the identification J1 carries as a premise.** "
    u"### **(4) M-2's aggregation; M-3; M-5; `W-ORD-CN-LAW`.** "
    u"### **(5) THE PATENT LANE, INDEPENDENT: the two uploads are DONE and RECEIPTS ARE PENDING -- "
    u"NOTED, NOT VERIFIED BY THIS SEAT.** *** "
    u"### **NO GRADE MOVED EXCEPT J2's OWN, AND THAT ONE MOVED TO ### REFUTED ### . ### M-2..M-5 "
    u"STAND OPEN AND THIS ACT CLOSED NONE. ### THE THIRTY-SEVENTH SEAM'S DEBT STANDS, UNPAID AND "
    u"UNTOUCHED. ### PLACE-papers WAS NOT TOUCHED, SO NO MIRROR REBUILD IS OWED AND NONE IS "
    u"CLAIMED, AND THE HOOK WAS NOT EXERCISED -- REPORTED EITHER WAY. ### b259's BANK REMAINS "
    u"UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. ### "
    u"NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b260: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b260)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"J2 IS ### REFUTED",
                 u"a_0` IN `(1.75, 2]",
                 u"NOT ABOUT THE FUNCTION",
                 u"b255 IS NOT RE-VERDICTED",
                 # ### THIS ASSERTION FIRED ON ITS FIRST RUN, ON `THE OWNER'S OWN SUPPORT LINE`,
                 # ### where the text reads `is the OWNER'S OWN SUPPORT LINE` -- ### **THE SAME
                 # ### SPECIES THE BANK HAD JUST FINISHED NAMING, CAUGHT A THIRD TIME INSIDE THE
                 # ### SAME ACT.** ### The difference that matters: ### **THE ASSERT CAUGHT IT
                 # ### BEFORE THE WRITE**, where the harness gates catch their instances after.
                 u"OWNER'S OWN SUPPORT LINE",
                 u"A REGISTERED FALSIFIER FIRED -- F4",
                 u"THE OSCILLATION IS IN THE ### LEADING ### MODE",
                 u"only mode 0 is sign-definite",
                 u"FALSE NECESSARILY",
                 u"79 ### STEPS",
                 u"FLATTENED EXACTLY THE REGION",
                 u"11 TERMINALS",
                 u"IT DOES NOT COMPILE J2",
                 u"THIRD CONSECUTIVE ACT",
                 u"NEITHER BRANCH WAS TAKEN",
                 u"W-ORD-EPS-DECAY",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    # ### AND THE PRIOR LEAD'S OWN HEADLINES MUST SURVIVE THE DEMOTION.
    for kept in (u"J1 IS A THEOREM ON THE OWNERS' DEFINITIONS",
                 u"NOT ONE OF THEM CHECKED IT",
                 u"b164's LAW COMMITTED IN A GATE",
                 u"STATES GRADES, CONFERS NONE",
                 u"LIVE b148 CONDITION"):
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
