# -*- coding: utf-8 -*-
"""b265_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE NQ-CEILING SWEEP (b265)"
PRIOR_MARK = u"(b264)"

NEW = (
    u"*** ### ### **ZERO CELLS FALL ABOVE THE CEILING, ACROSS BOTH ACTS.** ### b255's SIXTEEN "
    u"CELLS ARE ALL ### INSIDE ### , and they are inside ### BY MEASUREMENT ### and not only by "
    u"the `100 < 238.4` arithmetic: worst movement on the `NQ` axis from 700 to 2800 is "
    u"### **8.868e-10** ### -- three orders below b255's printed digit, six below its own claim "
    u"bar -- and the `NG` axis is quieter still at `1.315e-12`, ### **WHICH IS b264's ATTRIBUTION "
    u"CONFIRMED ON A SECOND ACT'S CELLS.** ### **b247 HAS NO `rho`-INDEXED VALUE AT ALL**; its "
    u"exposure is entirely to the `n`-floor, and b247 handled that itself. ### **NOTHING MOVED. "
    u"### NOTHING IS ROUTED AS A CHANGED VALUE.** *** "
    u"### **AND THE REPRODUCTION IS THE STRONGEST NUMBER IN THE ACT: worst "
    u"`|this act at NQ=700 - b255's banked column|` = ### 2.220e-16 ### . ### MACHINE PRECISION, "
    u"CELL FOR CELL, BEFORE ANY GRADE WAS ASSIGNED TO IT.** ### b247's column reproduces to "
    u"`4.708e-07`, the limit of its own six-decimal printing. *** "
    u"### ### **THE `a^2` -> `rho` CORRESPONDENCE IS AN IDENTITY, NOT AN ESTIMATE:** "
    u"`e2_of_grid` interpolates at `exp(uu)` with `uu in [0, 2 log a]`, so the top eps argument "
    u"at a cell is ### **EXACTLY THE CELL LABEL** ### -- `exp(2 log a) = a^2`, no conversion "
    u"factor and no slack. ### **AND IT IS NOT THIS ACT'S INVENTION: b255's OWN (W1) SAYS THE "
    u"SAME IN ITS OWN WORDS**, having found it as a silent `np.interp` clamp and rebuilt its grid "
    u"to `rho_max = 100.001` because of it. *** "
    u"### ### **`W-ORD-NQ-CEILING` DISCHARGED, AND WITH A LAW RATHER THAN A NUMBER: "
    u"### `x_cliff = EPS_NQ / k`, `k ~ 3.24` NODES PER OSCILLATION PERIOD.** ### `NQ/x_cliff` = "
    u"`3.2558` at `NQ=700` and `3.2333` at `1400`, spread `1.0070` against a registered `1.5`; a "
    u"third point (`3.2037` at `2800`) ### **CORROBORATES BUT IS NOT COUNTED**, its reference "
    u"unverified there. ### **AND THE FINDING INSIDE THE LAW, WHICH THIS ACT DID NOT EXPECT: "
    u"THE CLIFF IS THE SAME `x` FOR EVERY RESOLVED MODE. ### IT IS NOT A PER-MODE ACCURACY "
    u"EFFECT -- IT IS A SINGLE ALIASING WALL THAT TAKES THE WHOLE LAYER AT ONCE.** ### So a "
    u"single number per `NQ` is the right form of the answer and a per-mode table was the wrong "
    u"one. ### b264's `238.4` reproduces at `212.1` on an independent grid, 11.0%. *** "
    u"### ### **AND THE CORRECTION THIS ACT OWES b264, REGISTERED AS OWED ### BEFORE ### THE "
    u"SWEEP RAN SO IT COULD NOT BE PRESENTED AFTERWARDS AS A FINDING OF IT: b264's "
    u"`W-ORD-NTERM-FLOOR` FILED THAT THE INSTRUMENT CARRIES FOUR MODES IT CANNOT COMPUTE AND "
    u"THAT ### NOTHING IN THE RECORD SAID SO ### . ### THE RECORD SAID SO IN FIVE PLACES.** "
    u"### **b242** established the float64 floor; ### **b244's RULE MODES K1 RULED THE "
    u"REALIZATION TO SEVEN MODES BECAUSE OF IT** -- a standing ruling, not an observation; "
    u"### **b247** quotes the `4.746e-16` floor and refuses to use points past it, and its A-4 "
    u"states the certificate-versus-arithmetic distinction outright, adding that "
    u"### **b244 ALREADY RULED ON THE DIFFERENCE** ### ; ### **b253's QUOTED-N law**; "
    u"### **b255** carries `suspect above n = 6` in every table header. "
    u"### ### **SO b264's `NRES = 7` WAS A REDISCOVERY THAT INDEPENDENTLY CONFIRMS b244 BY A "
    u"DIFFERENT TEST -- WORTH SOMETHING AS CONFIRMATION, NOT A FINDING -- AND THE PROVENANCE "
    u"CLAUSE WAS SIMPLY WRONG.** ### The work-order is RESTATED AND NARROWED to what is actually "
    u"owed: the resolved count is not stated beside `NTERM` at the point of use. ### **NO ACT IS "
    u"RE-VERDICTED BY THIS; WHAT IS WITHDRAWN IS ONE PROVENANCE CLAUSE IN ONE FILING, AND THE "
    u"AUTHOR RULES ON WHETHER b264 IS AMENDED OR CARRIES AN ERRATUM.** *** "
    u"### **`W-ORD-GL-PANEL` DISCHARGED BY DOING IT: `tools/reg_satisfiable.py` CHECKS A "
    u"REGISTRATION'S DECLARED CAPS AGAINST THE DEMANDS ITS OWN PARAMETERS IMPLY, ### BEFORE THE "
    u"SEAL ### .** ### It was POSITIVE-CONTROLLED on b264's own clause (I) before being trusted: "
    u"fed the real `256 MB` cap against the `204800 MB` its registered ladder implied, it "
    u"returned ### **CONTRADICTORY / DO NOT SEAL**. ### **A CHECK THAT HAS NEVER SAID NO IS NOT "
    u"A CHECK, AND THIS ONE SAID NO BEFORE IT SAID YES.** ### b265's own binding clause was real: "
    u"`Q.layer(5600)` needs `250.88 MB` in one allocation, which is why the cap is `512 MB`. "
    u"### **AND ITS REACH IS FILED WITH IT: IT COMPARES THE PAIRS IT IS GIVEN, AND THE "
    u"ENUMERATION OF AN ACT'S OWN CEILINGS REMAINS THE OPERATOR'S.** *** "
    u"### ### **FOUR DEFECTS IN THIS ACT'S OWN INSTRUMENT, ALL FOUND BY ITS OWN FALSIFIERS "
    u"FIRING, ALL DISCLOSED:** ### **(D1)** the exposure test named `staircase` as `left_side`'s "
    u"successor and `staircase` is defined ABOVE it, so the split returned the whole remainder of "
    u"the file and found another function's `Q.layer` -- ### **b263's `--name-only` SPECIES; THE "
    u"SUCCESSOR IS NOW FOUND, NEVER NAMED**; ### **(D2)** pin P2 applied twice, a factor of "
    u"exactly `sqrt(2)`; ### **(D3)** the crossover probe grid started ABOVE the crossover and "
    u"returned its own left edge -- ### **A TEST THAT SATURATES AT ITS FIRST POINT HAS MEASURED "
    u"ITS GRID**; ### **(D4), AND THIS ONE IS AGAINST THE SEALED REGISTRATION: THE REGISTERED "
    u"CROSSOVER STATISTIC COULD NOT HAVE PASSED.** ### It set a `1e-8` RELATIVE bar where the "
    u"`NQ`-to-`2NQ` difference is round-off at `~2.5e-14` on an `A_0 ~ 5.6e-07`, a relative floor "
    u"of `~4.4e-08`: ### **THE BAR SAT BELOW THE ROUND-OFF FLOOR OF ITS OWN COMPARISON.** "
    u"### ### **THE PATTERN, AND IT IS NOT b264's: (D1) AND (D4) MADE THE ACT LOOK WORSE BY "
    u"FIRING FALSIFIERS ON NOTHING; (D2) AND (D3) MADE IT WRONG. ### NONE FLATTERED THE RESULT -- "
    u"RECORDED AS A FACT, NOT CLAIMED AS A VIRTUE, SINCE FOUR STILL SHIPPED.** *** "
    u"### **THE CONSEQUENCE TABLE: EVERY AFFECTED CLAIM ### UNCHANGED ### .** ### b255's "
    u"fifteen steps keep one sign at `NQ=700` AND at `2800`. ### b247's M-4 inputs -- the seven "
    u"certified points, clause (i)'s missing rate, and clause (ii)'s first disjunct false on the "
    u"certified range, whose ~36,000x growth runs over `n = 0..6`, ### **ENTIRELY INSIDE THE "
    u"RESOLVED RANGE**. ### b255's `bar (B)` -- this act's `NQ=2800` spread is one to two orders "
    u"### SMALLER ### than the bar b255 published, ### **CONFIRMING ITS CONSERVATISM AND "
    u"FALSIFYING THIS SEAT'S REGISTERED EXPECTATION, WHICH IS REPORTED WRONG.** *** "
    u"### **THE SHADOW: `Core/CeilingSweepShadow.lean`, VANILLA, `decide` ONLY, ### 10 TERMINALS "
    u"AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED**, four polarity refusals at lean exit 1. "
    u"### **IT DOES NOT COMPILE THE CROSSOVER LAW** -- that is a measured relation and an "
    u"observation under b242 -- and it carries the `a^2` identity, the sixteen cell comparisons "
    u"against the ### CONSERVATIVE ### `215` rather than b264's `238`, b244's `7 + 4 = 11`, and "
    u"the nodes-per-period bracket at BOTH measured points. *** "
    u"### **GATES 11/11 WITH EVERY FIXTURE FAILING AS REQUIRED. ### TERM SCAN CLEAN OVER 2090 "
    u"LINES. ### REGISTRATION TERM-SCANNED AND SATISFIABILITY-CHECKED ### BEFORE ### SEALING "
    u"(b263's sequencing defect, not repeated). ### SEAL `263f37a9` INTACT AT THE CLOSE. "
    u"### 159.1 s AGAINST A 1800 s CEILING.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE SWEEP IS NOT A SWEEP OF THE RECORD -- TWO ACTS "
    u"WERE NAMED AND TWO WERE SWEPT, AND NO OTHER ACT IS DECLARED SAFE ON THIS AXIS.** "
    u"### **(2) `W-ORD-TQ-IDENTIFY` (b260), STILL THE PREMISE J1, J3, b263 AND b264's `J` COLUMN "
    u"ALL INHERIT.** ### **(3) M-2's STATEMENT, THE AUTHOR'S TO ADOPT OR ROUTE.** "
    u"### **(4) `W-ORD-INDEX-APPEND` -- NOW ELEVEN KEYS ACROSS FIVE ACTS, AND THIS ACT IS THE "
    u"PROOF OF THE REACH LINE IT KEEPS QUOTING: `nterm-floor` HAS NO INDEX KEY AND THE RECORD "
    u"HELD IT IN FIVE PLACES.** ### **(5) THE NEXT TEMPLATE ORDER, FILED HERE: A BAR CHECKED "
    u"AGAINST THE NOISE FLOOR OF ITS OWN COMPARISON BEFORE SEALING -- (D4) IS EXACTLY THAT "
    u"DEFECT AND `reg_satisfiable.py` CANNOT SEE IT.** ### **(6) M-3; M-5; `W-ORD-CN-LAW`; "
    u"`W-ORD-XI-PERMODE`.** ### **(7) THE PATENT LANE, INDEPENDENT: RECEIPTS PENDING, CARRIED ON "
    u"THE FERRY'S WORD AND NOT VERIFIED BY THIS SEAT.** *** "
    u"### **NO GRADE MOVED. ### NO PRIOR ACT WAS RE-VERDICTED. ### NO VERDICT WAS ALTERED. "
    u"### NO OWNER INSTRUMENT WAS EDITED -- `B38.EPS_NQ`/`EPS_NG` WERE SET AS MODULE ATTRIBUTES "
    u"AND RESTORED, b245's PATTERN, DECLARED IN THE REGISTRATION BEFORE THE RUN. ### PLACE-papers "
    u"AND THE PATENT TREE WERE NOT TOUCHED. ### b259's BANK REMAINS UNTRACKED AS b259 RULED. "
    u"### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b264: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b264)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"ZERO CELLS FALL ABOVE THE CEILING",
                 u"BY MEASUREMENT",
                 u"MACHINE PRECISION",
                 u"EXACTLY THE CELL LABEL",
                 u"W-ORD-NQ-CEILING` DISCHARGED",
                 u"THE CLIFF IS THE SAME `x` FOR EVERY RESOLVED MODE",
                 u"THE RECORD SAID SO IN FIVE PLACES",
                 u"RULE MODES K1 RULED THE",
                 u"REDISCOVERY THAT INDEPENDENTLY CONFIRMS b244",
                 u"W-ORD-GL-PANEL` DISCHARGED BY DOING IT",
                 u"CONTRADICTORY / DO NOT SEAL",
                 u"THE BAR SAT BELOW THE ROUND-OFF FLOOR",
                 u"NONE FLATTERED THE RESULT",
                 u"EVERY AFFECTED CLAIM ### UNCHANGED",
                 u"10 TERMINALS",
                 u"NOT A SWEEP OF THE RECORD",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"`eps_even` DECAYS, AND THE ENVELOPE IS DERIVED",
                 u"NOT THE ONE THAT BINDS",
                 u"M-2's ADDRESS IS DERIVED",
                 u"THE FIRST-LEVEL PRIMES ARE SILENT",
                 u"J2 IS ### REFUTED",
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
