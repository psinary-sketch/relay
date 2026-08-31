# -*- coding: utf-8 -*-
"""b263_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE TOP-LEVEL SILENCE (b263)"
PRIOR_MARK = u"(b262)"

NEW = (
    u"*** ### ### **M-2's ADDRESS IS DERIVED, AND IT IS ONE LINE OF act 9's OWN TEXT.** ### The "
    u"closed form is defined for `1 <= k <= n-1` and supplies `0 for k >= n`, so "
    u"### **THE QUOTIENT CHANNEL CONTRIBUTES ### IDENTICALLY ZERO ### AT A PRIME'S TOP LEVEL** -- "
    u"and a prime with `n_p(a) = 1`, whose only level IS the top, contributes nothing at all. "
    u"### ### **THE FIRST-LEVEL PRIMES ARE SILENT.** ### It is not a small value, not a limit and "
    u"not an approximation: ### **THE FORMULA DOES NOT REACH `k = n` AND THE OWNER SUPPLIES THE "
    u"ZERO EXPLICITLY.** ### b260 saw the consequence and named it (`phi = 1`); ### **THIS ACT "
    u"NAMES ITS CAUSE, WHICH IS A RANGE AND NOT A SIZE.** *** "
    u"### ### **AND THE SILENCE IS NOT A DETAIL: ITS SHARE OF THE SEPARATION `PR - Theta_q` RUNS "
    u"### 73.96% AT `a^2 = 1e2` TO 99.95% AT `a^2 = 1e8` ### ALONG (L-B), ALL PRIMES.** ### b262's "
    u"ladder is CONSUMED as control and no number is re-derived. ### **AND BECAUSE `Theta_q` GETS "
    u"NOTHING FROM THEM, THE `m=1` COLUMN IS SIMULTANEOUSLY THEIR CONTRIBUTION TO `PR` AND TO THE "
    u"SEPARATION -- ONE COLUMN, TWO ROLES.** ### The fixed-level residue falls `0.090425 -> "
    u"0.004814` along the same limit: ### **THAT DECAY IS (L-A) AT WORK AND THE RISING SILENT "
    u"SHARE IS (L-B) AT WORK, AND THE COLUMNS ARE LABELLED SO THEY CANNOT BE CONFUSED.** *** "
    u"### ### **M-2's ROW MOVES: ### OPEN -> SPECIFIED-NOT-STATED ### . ### AND THAT IS NOT A "
    u"DISCHARGE.** ### Whatever the aggregation is, it is ### **THE THING THAT WOULD HAVE TO SPEAK "
    u"WHERE act 9's FORMULA IS SILENT.** ### **THE SPECIFICATION, THREE NECESSARY PROPERTIES: "
    u"(SPEC-1) IT COUNTS FIRST LEVELS; (SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT `k <= n-1`; "
    u"(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET.** ### **THEY EXCLUDE; THEY DO NOT "
    u"DETERMINE. ### NO FUNCTION SATISFYING THEM IS EXHIBITED AND NONE IS SHOWN TO EXIST. ### NO "
    u"AGGREGATION IS ADOPTED, STATED OR REALIZED, AND M-2 IS STILL OWED.** *** "
    u"### **THE CONDITIONAL IS PART OF THE CLAIM AND IS STATED BEFORE IT:** b262 established that "
    u"### **EITHER THE FINITE SIDE SUPPLIES THE FIRST-LEVEL MASS OR THE ARCHIMEDEAN SIDE ABSORBS "
    u"IT, AND NOTHING IN THE RECORD DECIDES WHICH.** ### **THE SPECIFICATION IS FOR THE FIRST "
    u"BRANCH ONLY AND IS VACUOUS ON THE SECOND.** *** "
    u"### ### **AND THE RECONCILIATION WITH b220, MADE EXPLICIT RATHER THAN LEFT TO A READER:** "
    u"b220's verdict -- ### *\"NOT ONE OF THE FOUR EXCLUDES ANY FUNCTION\"* -- ### **STANDS "
    u"UNMOVED: IT IS ABOUT THE FOUR CONSTRAINTS ALREADY IN THE RECORD.** ### This act adds a "
    u"### FIFTH, CONDITIONAL ### one, and ### **(SPEC-1) DOES EXCLUDE -- IT EXCLUDES `Theta_q` "
    u"ITSELF, WHICH ASSIGNS ZERO THERE.** ### So on the first branch the admissible set is no "
    u"longer everything; on the second it still is. ### **b220 IS CONDITIONALLY NARROWED, NOT "
    u"CONTRADICTED.** *** "
    u"### **THE CORPUS SURVEY: ### 27 PRIOR-OWNER LINES READ AT CONTENT, 0 CANDIDATE CONSTRAINTS.** "
    u"### 7 SUPPLIES (act 9 and b11 state the quotient VALUE at `k >= n` -- ### **THE OBJECT BEING "
    u"AGGREGATED, NOT A CONDITION ON THE AGGREGATION**); 2 DEFINES (b16/b17 fix what `n_p` IS); "
    u"18 OTHER. ### **NO PRIOR HOLDING STATES ANY CONDITION ON `Q.value` AT THE TOP LEVEL** -- and "
    u"the classifier is shown able to RETURN `CANDIDATE CONSTRAINT` on a constructed line, so its "
    u"silence is a MEASUREMENT. ### The search is positive-controlled: two held phrases found, an "
    u"invented one not. *** "
    u"### ### **AND A DEFECT IN THIS ACT'S OWN RUN, DISCLOSED BEFORE ITS RESULT WAS USED: "
    u"`b263_run.txt`'s S3 ### COUNTED ### sixteen prior-owner files and then printed \"NO HOLDING "
    u"CONSTRAINS THE TOP LEVEL\" ### HAVING READ NONE OF THEM ### . ### A COUNT IS NOT A READING, "
    u"AND A VERDICT THAT RUNS AHEAD OF ITS EVIDENCE IS THE SPECIES THIS CORPUS HUNTS -- IT DOES "
    u"NOT STOP BEING THAT SPECIES BECAUSE THE VERDICT LATER PROVES RIGHT.** ### The run is "
    u"PRESERVED UNCHANGED; `data/b263_survey.txt` supplies what its S3 owed, with the criterion "
    u"fixed before any line was quoted. *** "
    u"### **S4, IN b236's SEPARATED VOICES: the deposit's FOURTH REGISTER is \"the balance-to-"
    u"positivity distance at the multiplicative place\", which b236 maps at a cell to ### THE SIGN "
    u"OF `A - PR` ### . ### AND `PR`'s GROWTH IS CARRIED, TO 99.95%, BY PRIMES THE QUOTIENT "
    u"CHANNEL IS SILENT ON.** ### **b236's OWN CEILING TRAVELS: \"IT DISCHARGES NOTHING\".** "
    u"### **FIVE MISREADINGS REFUSED, THE FIFTH NEW: THE SPECIFICATION IS NOT A PROPOSAL -- it "
    u"says what an aggregation would have to do, not that any does it, and not that one exists.** *** "
    u"### **`W-ORD-REG-HASH` DISCHARGED BY DOING IT: `tools/reg_seal.py` seals a registration with "
    u"the `sha256` of every byte above the seal block, `--verify` recomputes, and `--reseal` PRINTS "
    u"BOTH HASHES AND WRITES THE SUPERSEDED ONE IN -- ### A TOOL THAT COULD RE-SEAL WITHOUT LEAVING "
    u"A TRACE WOULD UNDO ITS OWN POINT.** ### **ITS REACH IS NOT OVERSOLD: IT PROVES THE BODY HAS "
    u"NOT CHANGED SINCE SEALING; IT PROVES NOTHING ABOUT ### WHEN ### THE SEAL WAS WRITTEN.** *** "
    u"### ### **AND A SEQUENCING DEFECT OF MINE, DISCLOSED, WHICH THE TOOL THEN CAUGHT: I RAN THE "
    u"TERM SCAN AND THE SEAL IN ONE COMMAND AND ### SEALED A REGISTRATION THAT HAD JUST RETURNED "
    u"`NOT CLEAN` ### . ### THEN `--verify` RETURNED `SEAL BROKEN` ON MY OWN CORRECTION -- A "
    u"POSITIVE CONTROL OBTAINED FOR FREE, BEFORE ANY FIXTURE WAS WRITTEN FOR IT.** ### Two further "
    u"live uses were caught in the bank at the closing scan and corrected before shipping. *** "
    u"### **THE SHADOW: `Core/TopLevelSilenceShadow.lean`, VANILLA, `decide` ONLY, ### 9 TERMINALS "
    u"AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED.** ### Its load-bearing polarity control is "
    u"`the_level_below_is_inside_the_range`: ### **THE RANGE EXCLUDES THE TOP LEVEL AND NOTHING "
    u"ELSE.** ### And `first_level_prime_has_a_level_the_range_does_not_reach` pairs `1 <= 1` with "
    u"`NOT (1 <= 0)` -- ### **THAT PAIR ### IS ### THE SILENCE, AS ARITHMETIC.** ### Three FALSE "
    u"statements of the same shape were REFUSED, lean exit 1. ### **IT DOES NOT COMPILE M-2's "
    u"SPECIFICATION.** *** "
    u"### **AND THE b262 INVESTMENT PAID VISIBLY: ONE GATE FAILED ON A NEEDLE THAT READ `THEY "
    u"EXCLUDE` WHERE THE BANK SAYS `THESE EXCLUDE` -- b229's SPECIES AGAIN -- BUT `verify_all` "
    u"NAMED THE ABSENT NEEDLE OUTRIGHT AND THE FIX TOOK ONE `needle_extract` CALL. ### b229, b260 "
    u"AND b261 EACH COST A THROWAWAY PROBE TO LOCATE; THIS COST NONE.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) J4 -- `eps_even`'s DECAY (`W-ORD-EPS-DECAY`), THE "
    u"ARCHIMEDEAN TWIN, AND b263 SHARPENS WHY IT IS LIVE: THE SPECIFICATION'S CONDITION ### IS ### "
    u"THE BRANCH QUESTION, SO J4 IS THE ACT THAT BEARS ON WHICH BRANCH THE SPECIFICATION IS EVEN "
    u"ABOUT.** ### **(2) `W-ORD-TQ-IDENTIFY` (b260) -- the premise J1, J3 and b263 all inherit.** "
    u"### **(3) M-2's STATEMENT ITSELF, now that it has an address -- THE AUTHOR'S TO ADOPT OR "
    u"ROUTE.** ### **(4) M-3; M-5; `W-ORD-CN-LAW`.** ### **(5) THE PATENT LANE, INDEPENDENT: "
    u"RECEIPTS PENDING, CARRIED ON THE FERRY'S WORD AND NOT VERIFIED BY THIS SEAT.** *** "
    u"### **NO GRADE MOVED EXCEPT THIS ACT'S TWO ROWS AND M-2's STATUS. ### M-3, M-4, M-5 STAND "
    u"OPEN AND THIS ACT CLOSED NONE. ### THE THIRTY-SEVENTH SEAM'S DEBT STANDS: THIS IS THE FIRST "
    u"ACT IN THE ARC TO MOVE ITEM 1 AT ALL, AND IT MOVES IT ONLY FROM `OPEN` TO `OPEN, AND NOW "
    u"SPECIFIED`. ### THE DEBT IS NOT PAID. ### PLACE-papers WAS NOT TOUCHED, SO NO MIRROR REBUILD "
    u"IS OWED AND NONE IS CLAIMED, AND THE HOOK WAS NOT EXERCISED -- REPORTED EITHER WAY. ### "
    u"b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 BEYOND THE REGISTER "
    u"SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b262: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b262)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"M-2's ADDRESS IS DERIVED",
                 u"THE FIRST-LEVEL PRIMES ARE SILENT",
                 u"THIS ACT NAMES ITS CAUSE, WHICH IS A RANGE AND NOT A SIZE",
                 u"73.96% AT `a^2 = 1e2` TO 99.95%",
                 u"ONE COLUMN, TWO ROLES",
                 u"OPEN -> SPECIFIED-NOT-STATED",
                 u"THEY EXCLUDE; THEY DO NOT DETERMINE",
                 u"M-2 IS STILL OWED",
                 u"VACUOUS ON THE SECOND",
                 u"CONDITIONALLY NARROWED, NOT CONTRADICTED",
                 u"0 CANDIDATE CONSTRAINTS",
                 u"A COUNT IS NOT A READING",
                 u"IT DISCHARGES NOTHING",
                 u"THE SPECIFICATION IS NOT A PROPOSAL",
                 u"W-ORD-REG-HASH",
                 u"SEAL BROKEN",
                 u"9 TERMINALS",
                 u"IT DOES NOT COMPILE M-2's",
                 u"THIS COST NONE",
                 u"THE DEBT IS NOT PAID",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"THE JUNCTION ### DIVERGES ### ALONG THE CUTOFF LIMIT",
                 u"DOUBLE-*LIMIT* ERROR",
                 u"J2 IS ### REFUTED",
                 u"J1 IS A THEOREM ON THE OWNERS' DEFINITIONS",
                 u"STATES GRADES, CONFERS NONE"):
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
