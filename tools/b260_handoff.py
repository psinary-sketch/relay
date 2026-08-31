# -*- coding: utf-8 -*-
"""b260_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

### AND ONE THING THIS TOOL SAYS THAT ITS PREDECESSORS DID NOT HAVE TO:
### ### **THE LEAD IT DEMOTES IS b256's, NOT b259's.** ### b257, b258 and b259 are banked
### acts that NEVER ENTERED THE HANDOFF LEAD. ### A demotion that wrote "prior: b256"
### without saying that would imply an unbroken chain, and there is a three-act omission.
### ### **THE OMISSION IS NAMED IN THE NEW LEAD RATHER THAN PAPERED OVER BY THE MECHANISM.**
"""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE JUNCTION'S SIGN (b260)"
PRIOR_MARK = u"(b256)"

NEW = (
    u"*** ### ### **J1 IS A THEOREM ON THE OWNERS' DEFINITIONS: `Theta_q(a) <= PR(a)` AT EVERY "
    u"DIAGONAL `a^2` CELL**, by termwise domination over an index set proved IDENTICAL, and "
    u"### **STRICT at every term carrying non-zero weight.** ### The route: b17's staircase fixes "
    u"one index set for both instruments; act 9 sec 2's closed form "
    u"`tau_q * p^(k/2) = (p^n - p^k)/(p^n - 1)`, `0 for k >= n`, bounds each quotient term; the "
    u"bump's own non-negativity signs the correlation. *** "
    u"### ### **AND THE FERRY'S REGISTERED EXPECTATION ABOUT `2 log p` IS REFUTED -- BY A READ, "
    u"NOT BY A MEASUREMENT. ### THE FACTOR IS ON *BOTH* ASSEMBLED SUMMANDS AND CANCELS. ### SO "
    u"DOES `corr`. ### SO DOES `p^{-k/2}`.** ### **THE ENTIRE INEQUALITY IS act 9's RATIO "
    u"`(p^k - 1)/(p^n - 1)` AND NOTHING ELSE**, and `2 log p` has its first derived *LIMIT* "
    u"rather than its first derived role: ### **IT CANNOT CARRY, WIDEN OR TIGHTEN THE JUNCTION.** "
    u"### **b228 IS NOT CONTRADICTED** -- it paired act 9's BARE `tau_q` against PR's WEIGHT; this "
    u"act pairs the two ASSEMBLED summands. ### **TWO PAIRINGS, AND CONFLATING THEM WOULD BE "
    u"b219's DOUBLE-NAME SPECIES.** ### b10's factor question is promoted in NEITHER direction. *** "
    u"### ### **THE ONE PREMISE, NAMED AND NOT DERIVED: that the instrument's `|tr(U^k S)|/d` IS "
    u"act 9's `tau_q`. ### b220, b228, b229 AND b255 ALL TREAT THEM AS ONE OBJECT AND NOT ONE OF "
    u"THEM CHECKED IT.** ### **b260 CHECKED IT: 119 TERMS, WORST DEVIATION `4.441e-16`, AGAINST A "
    u"`1e-9` BAR FIXED IN THE REGISTRATION BEFORE ANY VALUE EXISTED. ### IT HOLDS -- AND THAT "
    u"CONVERTS AN UNEXAMINED HABIT INTO A NAMED PREMISE, WHICH IS NOT THE SAME AS DISCHARGING IT.** "
    u"### **`W-ORD-TQ-IDENTIFY` FILED.** *** "
    u"### **THE SEPARATION'S STRUCTURE, EXHIBITED: `w - tau = w * (p^k - 1)/(p^n - 1)`.** ### At `k = n` "
    u"the fraction is `1` -- ### **act 9's VALUE VANISHES AND THE WHOLE OF PR's TERM SURVIVES** "
    u"(43 of the 119 terms); below it the fraction is `< 1`. ### **ONE FORMULA AT ITS OWN "
    u"ENDPOINT, NOT TWO PHENOMENA.** ### ### **AND THAT DERIVES b255's SAWTOOTH: when the "
    u"staircase steps, the top level SWITCHES ON.** ### **THE DERIVATION PREDICTS THE BENCH "
    u"OBSERVATION; THE OBSERVATION IS NOT A PREMISE OF IT.** ### The RISES between steps are "
    u"### NOT ### derived and stay bench. *** "
    u"### **UNDER RULE Q THE JUNCTION PIECE `(PR - Theta_q)` IS `>= 0` BY THEOREM.** ### b255's "
    u"\"approaches from below\" is no longer a ladder observation. ### **BUT `resid(A) = "
    u"-(E2even + junction)` HAS TWO TERMS AND ONLY ONE IS SIGNED: ### `E2even` IS BENCH-ONLY AND "
    u"THE (SIGN-EVENT) QUESTION IS NOT CLOSED.** ### **J2 IS THEREFORE THE LIVE ONE -- and its "
    u"ROUTE NOTE is that J1's METHOD DOES NOT TRANSFER: `E2even` has NEITHER a per-term closed "
    u"form NOR an index set to share. ### ITS HONEST FIRST STEP IS A STATEMENT-READ ON `eps`, NOT "
    u"A LADDER**, with b255's (W1) silent-grid failure standing as the warning. *** "
    u"### **THE SHADOW: `Core/JunctionSignShadow.lean`, VANILLA, `decide` ONLY, ### 13 TERMINALS "
    u"AT ZERO AXIOMS, PROFILE PRINTED AND READ.** ### It carries the staircase (both halves), the "
    u"slack range cap, the ratio inequality in EXACT INTEGER ARITHMETIC, and the counts. ### **ITS "
    u"LOAD-BEARING POLARITY CONTROL: at `k = 0` THE STRICT INEQUALITY FAILS, so act 9's `1 <= k` "
    u"EXCLUDES SOMETHING REAL.** ### **AND THE TOOL ITSELF WAS POLARITY-CONTROLLED: two FALSE "
    u"statements of the same shape were REFUSED, lean exit 1.** ### ### **IT DOES NOT COMPILE J1. "
    u"### THE REAL-VALUED INEQUALITY STAYS AT CONTENT AND `Real.rpow` GYMNASTICS WERE REFUSED IN "
    u"THE REGISTRATION, BEFORE THE FILE WAS WRITTEN.** *** "
    u"### ### **THREE DEFECTS IN THIS ACT'S OWN HARNESS, ALL THREE MINE, ALL THREE DISCLOSED.** "
    u"### First run ### **10 PASS / 1 FAIL / 2 REFUSED, NOT CLEAN.** ### (1) a gate asked the "
    u"REGISTRATION for a phrase only the RUN prints -- ### **b229's SPECIES, ONE ACT AFTER b229 "
    u"WROTE THE LESSON DOWN**; (2) the `ast` stripper was applied to a plain-text bank and "
    u"ERRORED; (3) ### **THE GATE DEFENDING THIS ACT'S CENTRAL CLAIM -- that b255 is a CONTROL and "
    u"not a PREMISE -- ANCHORED ON A PATH CONSTANT INSTEAD OF THE LOAD, FINDING THE *NAME* AND NOT "
    u"THE *USE*. ### b164's LAW COMMITTED IN A GATE, AND WEAK IN EXACTLY THE DIRECTION THAT WOULD "
    u"HAVE FLATTERED THE ACT.** ### Re-anchored on the load: ### **240 > 92. THE CLAIM SURVIVES "
    u"ITS OWN REPAIRED GATE.** ### **RE-RUN 13/13 CLEAN. ### BOTH SIDECARS CARRIED, THE FAILING "
    u"ONE FIRST.** *** "
    u"### **THE REACH, SAID AGAINST MY OWN RESULT: THE DERIVATION DOES NOT DEPEND ON THE LADDER, "
    u"ON `S4 = (2,3,5)`, OR ON SIXTEEN CELLS -- IT RUNS AT EVERY CELL. ### AND b15 AND b242 STILL "
    u"GOVERN: A UNIFORM *CELLWISE* INEQUALITY IS NOT A LIMIT FACT.** ### **IT IS NOT EVIDENCE FOR "
    u"OR AGAINST `T + Q = W_inf - W_primes`. ### IT DOES NOT CLOSE M-2 -- RULE Q's AGGREGATION IS "
    u"STILL UNSTATED. ### IT IS SCOPE-BOUND TO THE OWNERS' BUMP: A SIGN-CHANGING TEST FUNCTION CAN "
    u"BREAK S3 TERMWISE.** *** "
    u"### **THE PRIOR LEAD DEMOTED HERE IS b256's, AND THERE IS A THREE-ACT OMISSION: b257 (the "
    u"methodology sweep; SIGNEDNESS discharged), b258 (the history inventory) AND b259 (the six "
    u"blobs graded ALREADY-PUBLIC-ELSEWHERE 6/6, byte-identical rebuild) ARE BANKED AND NEVER "
    u"ENTERED THIS LEAD.** ### **THE OMISSION IS NAMED RATHER THAN PAPERED OVER BY THE DEMOTION.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) J2 -- `E2even`'s monotone decrease, now the only "
    u"unsigned term in `resid(A)`, with its route note saying J1's method does NOT transfer.** "
    u"### **(2) `W-ORD-TQ-IDENTIFY` -- prove the identification J1 carries as a premise.** "
    u"### **(3) M-2's finite address and the aggregation; M-3; M-5; `W-ORD-CN-LAW`.** "
    u"### **(4) THE PATENT LANE, INDEPENDENT: 64/065,864 due 2026-08-31 and 64/065,877 due "
    u"2026-09-01, drawings outstanding -- NOTED, NOT VERIFIED BY THIS SEAT.** *** "
    u"### **NO GRADE MOVED EXCEPT J1's OWN, WHICH THIS ACT EARNED AND WROTE WITH ITS PREMISE "
    u"ATTACHED. ### M-2, M-3, M-4, M-5 STAND OPEN AND THIS ACT CLOSED NONE. ### THE THIRTY-SEVENTH "
    u"SEAM'S DEBT STANDS, UNPAID AND UNTOUCHED. ### PLACE-papers WAS NOT TOUCHED, SO NO MIRROR "
    u"REBUILD IS OWED AND NONE IS CLAIMED, AND THE HOOK WAS NOT EXERCISED -- REPORTED EITHER WAY. "
    u"### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b256: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b256; b257-b259 banked but never in this lead)* %s and at %s%s%s" % (
        DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    # ### THE HEADLINE ASSERTIONS. ### A lead that lost one of these would be a different act's.
    for must in (u"J1 IS A THEOREM ON THE OWNERS' DEFINITIONS",
                 u"IS REFUTED -- BY A READ",
                 u"THE ENTIRE INEQUALITY IS act 9's RATIO",
                 u"b228 IS NOT CONTRADICTED",
                 u"NOT ONE OF THEM CHECKED IT",
                 u"4.441e-16",
                 u"W-ORD-TQ-IDENTIFY",
                 u"THE DERIVATION PREDICTS THE BENCH",
                 u"13 TERMINALS",
                 u"IT DOES NOT COMPILE J1",
                 u"ALL THREE MINE, ALL THREE DISCLOSED",
                 u"b164's LAW COMMITTED IN A GATE",
                 u"A UNIFORM *CELLWISE* INEQUALITY IS NOT A LIMIT FACT",
                 u"IT DOES NOT CLOSE M-2",
                 u"THE OMISSION IS NAMED RATHER THAN PAPERED OVER",
                 u"THE THIRTY-SEVENTH",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    # ### AND THE PRIOR LEAD'S OWN HEADLINES MUST SURVIVE THE DEMOTION.
    for kept in (u"STATES GRADES, CONFERS NONE", u"NO GRADE MOVED",
                 u"EVERY PATENT-FACING ROW IS `NO`", u"LIVE b148 CONDITION"):
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
