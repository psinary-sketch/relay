# -*- coding: utf-8 -*-
"""b266_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE STATE OF THE SHADOW (b266)"
PRIOR_MARK = u"(b265)"

NEW = (
    u"*** ### ### **THE J-ARC IS IN THE FINDINGS DOCUMENT WHOLE.** ### Ten acts, b256 -> b265, "
    u"folded into `PLACE-papers/FINDINGS.md` as section `0-ter` with five stable anchors, "
    u"### **PURELY ADDITIVE AT `+126 / -0`** ### -- and F-NOGRADE checks exactly that, because "
    u"### **A FOLD THAT EDITED AN EXISTING GRADE WOULD BE A RE-VERDICT WEARING A FOLD'S "
    u"CLOTHES.** ### **NO GRADE MOVED. ### NO ACT WAS RE-VERDICTED.** *** "
    u"### ### **AND THE FOLD RULE -- *every obstacle a QUOTATION, never a paraphrase* -- WAS MADE "
    u"### MECHANICAL RATHER THAN PROMISED: THE OBSTACLE TABLE IS ### EMITTED ### BY "
    u"`tools/b266_fold.py`, WHICH VERIFIES EVERY STRING VERBATIM AGAINST THE FILE IT IS "
    u"ATTRIBUTED TO AND ### EMITS NOTHING IF ONE IS UNFINDABLE.** ### 12 quotations, 0 "
    u"unfindable, and the checker shown able to miss. ### **A CHECK THAT RUNS AFTER THE WRITING "
    u"CAN ONLY REPORT A PARAPHRASE; ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.** *** "
    u"### **THE FOUR JUNCTION VERDICTS, THEIR OWNERS' AND NOT THIS ACT'S:** ### **J1 DERIVES** "
    u"(b260; termwise domination, index sets identical, `2 log p` on both sides and cancelling -- "
    u"### the arc's first derived limit); ### **J2 REFUTED** (b261; `E2even` rises on `(1, a_0]`, "
    u"`a_0` in `(1.75, 2]`, and ### **b255's LADDER STARTS AT `a^2 = 2` -- PAST THE TURN**); "
    u"### **J3 (GROWS)** (b262; the junction diverges, b263's cause: act 9's range empty at "
    u"`k = n`, first-level primes silent, **73.96% -> 99.95%** of the separation); "
    u"### **J4 (DECAYS)** (b264; `|eps_even(x)| <= C_even/x`, `C_even = 132.781908429`, sharp "
    u"rate `K_even = 1.568231065`). ### **AND J4's REACH IS FOLDED WITH J4: converged `rho <= "
    u"100`, curve `< 238.4`, NOT the `x >= 1000` its registration targeted.** ### **AND ITS "
    u"ENVELOPE ROUTES ### AROUND ### b250's S3(a) WALL: `W-ORD-XI-PERMODE` REMAINS OPEN, BECAUSE "
    u"ROUTING AROUND A WALL IS NOT REMOVING IT.** *** "
    u"### **b265's CERTIFICATION FOLDED WITH ITS SCOPE:** zero cells above the ceiling across both "
    u"swept acts; b255 reproduced at ### **2.220e-16** ### , machine precision cell for cell "
    u"before any grade was assigned; the law `x_cliff = EPS_NQ / k`, `k ~ 3.24`, with the cliff "
    u"### **THE SAME `x` FOR EVERY RESOLVED MODE -- A SINGLE ALIASING WALL, NOT A PER-MODE "
    u"EFFECT.** ### And its scope travels: ### **THE SWEEP IS NOT A SWEEP OF THE RECORD.** *** "
    u"### ### **THE BRANCH IS STATED WITH BOTH HALVES' DERIVED RATES, AND DECIDES NOTHING.** "
    u"### The finite branch: b262's junction ### **DIVERGES `0.374669 -> 19.708927`** ### across "
    u"`a^2 = 1e2 -> 1e8`. ### The archimedean branch: b264's ### **`E2even(a) -> 0` LIKE "
    u"`1/log a`**, monotone to `1.088038386` against a derived asymptote `[1.097174, 1.859...]`. "
    u"### **THE BEARING: `E2even` IS NOT THE OBJECT THAT ABSORBS `J`.** "
    u"### ### **AND THE SENTENCE THAT MATTERS MORE THAN THE BEARING: `E2even` IS ### ONE ### "
    u"ARCHIMEDEAN OBJECT AND IS ### NOT ### 'THE ARCHIMEDEAN SIDE'. ### THE BRANCH COULD BE "
    u"REALIZED BY A DIFFERENT ARCHIMEDEAN OBJECT, AND NOTHING IN THIS ARC EXCLUDES ONE. ### THE "
    u"BRANCH IS NOT DECIDED AND b263's SENTENCE STANDS EXACTLY AS b263 WROTE IT.** ### The four "
    u"refused misreadings are restated ### in the fold itself ### , so a reader of `FINDINGS.md` "
    u"meets them at the same place as the rates. *** "
    u"### ### **THE MONTH'S INSTRUMENT LAWS ARE ONE SET: `HARNESS_LORE.md` GOES FROM TEN RULES TO "
    u"### TWENTY-ONE**, rules 11-21, ### **EVERY ONE OF THE TWENTY-ONE NAMING AN OWNING ACT** "
    u"(F-INCIDENT: 0 of 21 without a citation). ### Among them: ### **a falsifier's verdict is "
    u"bounded by its instrument's resolution -- untestable is not failed**; ### **a "
    u"pre-authorized headline is what an act will reach for**; ### **registrations are "
    u"satisfiability-checked before sealing**; ### **a count is not a reading**; ### **a defect "
    u"set leaning one way is a finding about the seat**; ### **a rediscovery confirming a ruling "
    u"is corroboration, not a finding**; ### **convergence needs interleaved axes -- replicates "
    u"sharing an error source certify nothing**; ### **scope statements travel with results**; "
    u"### **exposure graded by call path before measurement**; ### **a check's scope is stated as "
    u"precisely as its finding.** *** "
    u"### **FIVE OF THE ELEVEN ARE MECHANIZABLE AND ARE MECHANIZED IN SEVEN FIXTURES, EACH IN "
    u"BOTH POLARITIES, ALL PASSING** (`tools/lore_fixtures.py`), ### **each built from its "
    u"incident's own numbers.** ### Both legs are required and the reason is stated in the tool: "
    u"the positive leg shows the violation is DETECTED, the negative that a compliant case is NOT "
    u"flagged -- ### **A DETECTOR THAT ALWAYS FIRES IS NOT A DETECTOR EITHER, AND IT IS THE "
    u"FAILURE MODE THAT LOOKS LIKE RIGOUR.** ### **THE OTHER SIX ARE NAMED AS JUDGEMENT RULES "
    u"RATHER THAN LISTED BESIDE THEM AS THOUGH THEY WERE THE SAME KIND OF THING**, and the "
    u"standing caution is repeated and not retired: ### **LORE IS NOT A GUARD.** *** "
    u"### ### **AND RULE 21 CAUGHT THIS ACT IN THE ACT OF FILING RULE 21: the closing term scan "
    u"was first run with `HARNESS_LORE.md` SCOPED AS A ### CREATED ### FILE WHEN THIS ACT ONLY "
    u"### APPENDED ### TO IT -- 1734 lines swept where the act wrote 102.** ### The verdict was "
    u"CLEAN either way, ### **AND A CLEAN VERDICT OVER AN OVER-BROAD SCOPE IS LUCK, NOT "
    u"EVIDENCE** -- b265's own sentence, quoted back at this act. ### Re-run at the appended-lines "
    u"scope: 1632 lines, CLEAN. ### ### **THIRD APPEARANCE OF THIS DEFECT ON THIS TOOL (b142, "
    u"b265, b266), AND THE FIRST TWO ARE CITED IN THE RULE THE THIRD ONE BROKE. ### WRITING A "
    u"RULE DOWN DOES NOT INSTALL IT.** *** "
    u"### **THE ERRATUM IS FOLDED WITH WHAT SURVIVES IT, NOT ONLY WITH WHAT IT WITHDRAWS.** "
    u"### `RULE B264-CLAUSE: E1` is discharged at `E-2026-08-31-1` and is ### CITED, NOT "
    u"RE-ISSUED ### . ### **`NRES = 7` LANDS ON b244's NUMBER BY A TEST b244 DID NOT USE -- AN "
    u"INDEPENDENT CONFIRMATION OF A STANDING RULING, AND IT IS WORTH HAVING.** ### b264's bank "
    u"stays unedited and its F6 verdict, envelope and rate are untouched. *** "
    u"### **THE DESK IS ONE LIST OF THIRTEEN:** ### M-2 **SPECIFIED-NOT-STATED** with SPEC-1/2/3 "
    u"(*they exclude; they do not determine*); M-3; M-5; `W-ORD-CN-LAW`; `W-ORD-TQ-IDENTIFY`; "
    u"`W-ORD-NQ-CEILING` **discharged, law banked**; `W-ORD-NTERM-FLOOR` **narrowed -- an "
    u"owner-instrument DOCUMENTATION order held under K.4, not an edit**; `W-ORD-EPS-DECAY` "
    u"**discharged with reach**; `W-ORD-XI-PERMODE`; `W-ORD-INDEX-APPEND` (**thirteen keys across "
    u"six acts**); ### **THE `ERRATA` PARTITION QUESTION, NEWLY FILED FOR THE RECONCILIATION "
    u"WAVE** -- the ledger's stated purpose is *the corrections record for the deposited line* "
    u"and four of its nine entries concern INTERNAL records, each correctly marked; ### **A "
    u"DOCUMENT-ARCHITECTURE QUESTION, NOT AN ERRATUM, AND THIS ACT DOES NOT PARTITION A LEDGER ON "
    u"ITS OWN JUDGEMENT**; the wave's trigger; the patent lane's receipts pending. *** "
    u"### **GATES 11/11 WITH EVERY FIXTURE FAILING AS REQUIRED. ### TERM SCAN CLEAN. ### "
    u"REGISTRATION TERM-SCANNED AND SATISFIABILITY-CHECKED ### BEFORE ### SEALING; SEAL "
    u"`dbb5cb0d` INTACT AT THE CLOSE. ### F-NOSHADOW: 0 `.lean` FILES MOVED ACROSS ALL THREE "
    u"REPOSITORIES -- AN ABSENCE THAT IS CHECKED, NOT ASSUMED.** ### **`TECHNE-Core` WAS NOT "
    u"PUSHED: local-only as b257 scoped it, HEAD still `22739c9`** -- said rather than left for a "
    u"reader to assume three repositories moved when the lore did not. *** "
    u"### ### **THE NEXT CAMPAIGN, AND IT AWAITS THE AUTHOR'S WORD: ### M-2's EXISTENCE "
    u"QUESTION.** ### b263 gave M-2 an address and three necessary properties and moved it "
    u"`OPEN -> SPECIFIED-NOT-STATED`, ### **WHICH WAS NOT A DISCHARGE**; this act folds the "
    u"specification and does not advance it. ### **THE SPECIFICATION EXCLUDES; IT DOES NOT "
    u"DETERMINE. ### NO FUNCTION SATISFYING SPEC-1/2/3 IS EXHIBITED AND NONE IS SHOWN TO EXIST -- "
    u"AND WHETHER ONE EXISTS IS THE QUESTION THE ARC HAS BEEN CIRCLING SINCE b197.** ### **THE "
    u"THIRTY-SEVENTH SEAM'S ITEM 1 IS STILL NOT PAID.** *** "
    u"### **NO GRADE MOVED. ### NO ACT RE-VERDICTED. ### NO OBSTACLE PARAPHRASED. ### NO OWNER "
    u"INSTRUMENT AND NO FOLDED ACT'S BANK EDITED. ### PLACE-papers STAGED THROUGH "
    u"`tools/place_add.py`. ### b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 "
    u"BEYOND THE REGISTER SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b265: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b265)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"THE J-ARC IS IN THE FINDINGS DOCUMENT WHOLE",
                 u"PURELY ADDITIVE AT `+126 / -0`",
                 u"EMITS NOTHING IF ONE IS UNFINDABLE",
                 u"J1 DERIVES",
                 u"J2 REFUTED",
                 u"J3 (GROWS)",
                 u"J4 (DECAYS)",
                 u"ROUTING AROUND A WALL IS NOT REMOVING IT",
                 u"A SINGLE ALIASING WALL",
                 u"THE BRANCH IS NOT DECIDED",
                 u"TWENTY-ONE",
                 u"LORE IS NOT A GUARD",
                 u"RULE 21 CAUGHT THIS ACT IN THE ACT OF FILING RULE 21",
                 u"WRITING A RULE DOWN DOES NOT INSTALL IT",
                 u"CITED, NOT",
                 u"THE `ERRATA` PARTITION QUESTION",
                 u"M-2's EXISTENCE",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"ZERO CELLS FALL ABOVE THE CEILING",
                 u"THE RECORD SAID SO IN FIVE PLACES",
                 u"`eps_even` DECAYS, AND THE ENVELOPE IS DERIVED",
                 u"M-2's ADDRESS IS DERIVED",
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
