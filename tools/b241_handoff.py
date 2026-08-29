# -*- coding: utf-8 -*-
"""b241_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

### THE DEMOTED TITLE IS DERIVED FROM THE FILE'S OWN LEAD LINE, never typed from memory, and
### EVERY assertion runs BEFORE the write. ### A title typed from memory is how a headline gets
### dropped quietly.
"""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE RESIDUAL LEDGER (b241)"
PRIOR_MARK = u"(b240)"

NEW = (
    u"*** ### **THE FIVE TERMS HAVE OWNERS NOW, AND THE TALLY IS: ONE RECONCILED-BY-TEXT, TWO "
    u"ROUTED, TWO STANDING -- NONE BY PREFERENCE.** ### **AND NO CORRECTION EXECUTED**: the texts "
    u"identify the objects and locate the real defect, but they do not force an amendment to C2, "
    u"and ### **AMENDING C2 WOULD BE AMENDING A RULING** -- b237's own sentence governs, *\"AN "
    u"EXECUTOR DOES NOT SETTLE A DEFINITION.\"* ### **`RULE M-1` UNAMENDED. FILE E UNTOUCHED. NO "
    u"SIGN INSERTED. NO ORIENTATION CHOSEN.** *** "
    u"### **THE THREE SHARPEST FINDINGS ARE ABOUT WARRANTS, AND TWO OF THEM ARE ABOUT b240's "
    u"OWN.** ### **(1) b240's REGISTRATION CITED THE WRONG SIBLING** -- it attributed to "
    u"`b38_act10.py` a `resid47` formula that `b36_act8.py` contains. b38 subtracts the "
    u"**TEN-of-ELEVEN-MODE** partial sum `E2N`; b36 subtracts the **FULL** eps. ### **COST IN "
    u"DIGITS: 8.9e-15, MEASURED AND NOT ASSUMED. COST IN WARRANT: the relation the whole "
    u"decomposition rests on was never checked against the file it names.** ### **(a) HOLDS "
    u"AMENDED**, the true relation quoted: `A = Tr_full - E2N - resid47`. *** "
    u"### **(2) b240's \"8.9e-16 REPRODUCTION\" IS A TAUTOLOGY.** Its diagnostics DEFINE "
    u"`resid := Tr - A - E2` and then verify a sum that reduces to `x = x`; ### **the reported "
    u"8.882e-16 is float re-association noise and confirms NOTHING.** ### **THIS ACT PROVES IT "
    u"RATHER THAN ASSERTING IT** -- gate 6 runs b240's own algebra on **500 arbitrary tuples**, "
    u"where it passes, with an independent-`resid` fixture that must fail. ### **The prediction "
    u"was genuinely registered in advance and that credit stands; what it was tested against was "
    u"its own restatement.** *** "
    u"### **(3) THE ORIENTATION QUESTION HAS NO OWNER AT ALL -- AND THE INDEX SAID SO BEFORE THE "
    u"EXECUTOR COULD TALK HIMSELF INTO AN ANSWER.** `sec 19`, `b36_act8.py:175` "
    u"(`RIGHT = (Tr_full + E2 - Dneg) - Thq`), `sec 20(c)` and the recurring `(Theta_q - PR)` "
    u"pairing ALL orient `Theta_q` with the prime side's minus -- ### **BUT NONE ASSEMBLES IT "
    u"INTO `Q.value`**, and `quotient-trace` records that ### **\"THE AGGREGATION IS UNSTATED: no "
    u"statement assembles the per-place values into the single real Q.value at a cell (b197, "
    u"re-confirmed b215).\"** ### **(d) ROUTED, dossier O1/O2/O3 filed, NOTHING CHOSEN.** "
    u"### **THE SPECIES, NAMED: FIVE SENTENCES THAT ORIENT AN OBJECT ARE NOT ONE SENTENCE THAT "
    u"DEFINES IT.** *** "
    u"### **THE E2 VERDICT: ONE OBJECT UNDER TWO NAMES -- AND THE DOUBLE-COUNT IS WITHDRAWN.** "
    u"`int g eps` / `E2` / `E2N` / `E2full` are one object at two truncations (8.99e-15 apart), "
    u"and **File E binds the FUNCTION `b38_act10.e2_of_grid` and names no grid argument.** "
    u"### **BUT THERE IS NO DOUBLE-COUNT ACROSS THE EQUALS SIGN**: `L` carries `E2` once, "
    u"`A - PR` carries it none. ### **The `2*E2` comes from substituting `Tr_full = A + E2 + "
    u"resid47`, AND THAT SUBSTITUTION IS VACUOUS** -- `resid47` is DEFINED as the residue, so it "
    u"holds equally with `5*E2`. ### **A DECOMPOSITION WHOSE LAST TERM IS DEFINED AS THE LEFTOVER "
    u"CARRIES NO INFORMATION ABOUT THE DECOMPOSED QUANTITY'S CONTENT.** ### b240 reported this "
    u"limb's SIZE was wrong; ### **b241 reports its ARGUMENT was circular.** *** "
    u"### **(c) NAMED FROM THE TEXTS, NOT ROUTED: THE RAW READING GOVERNS AND `resid47` IS NOT "
    u"ZERO.** b37's *\"0 by construction\"* is an ABSENCE -- ### **`b37_act9.py` contains no trace "
    u"function and calls none**, so there is no raw trace to differ from CC Thm 4.7's value. "
    u"### **File E line 60 binds `Tr_full` to `b38_act10.trace_modes` BY NAME**, and the two "
    u"readings are MUTUALLY EXCLUSIVE. ### **b240's sentence on this point is CONFIRMED.** "
    u"### ### **AND THE LEDGER'S REAL FINDING: `resid47` IS M-4's UNPAID SIZE AT THE BENCH -- THE "
    u"DOMINANT TERM'S OWNER WAS ALREADY OPEN, AND THIS ACT FILES NO NEW ENGINE ITEM.** *** "
    u"### **THE REGISTERED HOPE IS NOT BORNE OUT, AND THE EXECUTOR'S BANKED DISSENT IS -- BUT THE "
    u"ACT DOES NOT GET TO ENJOY THAT.** ### **IT WAS REGISTERED BEFORE ITS VERDICT, NOT BEFORE ITS "
    u"EVIDENCE**, and the registration's section (0) says so in its own words. ### **THE CELL THAT "
    u"SETTLES IT: at a^2 = 2 the `Theta_q`-vs-`PR` pair is IDENTICALLY ZERO -- and that cell "
    u"carries the LARGEST separation of the six, 8.085046.** ### **A pair that is zero where the "
    u"residual is largest is not where the residual concentrates**; at its best cell it is 21.07%. "
    u"### **The junction's bench shadow is the SMALLEST pair on the ledger, not the largest**, and "
    u"the address stays where `sec 20(b)` put it on 2026-08-18: ### **\"THE ARCHIMEDEAN "
    u"CALIBRATION IS UNRESOLVED AT THE BENCH.\"** *** "
    u"### **TWO NEW RULING-ITEMS THIS ACT ADDS AND THE FERRY DID NOT ANTICIPATE:** the "
    u"**Q-ORIENTATION DECISION CARD** and **`Delta_-`'s SIGN** -- act 8 subtracts `Dneg` where C2 "
    u"adds `Delta_-`, and `sec 19` reads *\"our object's trace = this - Delta_-(g)\"*. "
    u"### **`Delta_-`'s DEFINITION is correct and b240 BOUND IT CORRECTLY** (sec 17's odd-index "
    u"`t(n)` series, not act 8's odd raw-trace slice); ### **only the sign is in question, and it "
    u"is FILED, NOT EXECUTED.** ### **A SECOND FACE-OFF RUN BEFORE THESE TWO ARE RULED WOULD "
    u"INHERIT THE SAME SUSPECT 3 IT INHERITED LAST TIME.** *** "
    u"### **AND A SECOND MISS OF THE EXECUTOR'S OWN, FILED AS `W-ORD-FILE-E-WORKING-COPY-STALE`: "
    u"I READ THE WRONG FILE E FIRST AND QUOTED IT INTO A DRAFT.** "
    u"`relay/tools/lean/mathlib-companion/FiniteInstanceIdentity.lean` is ### **STALE BY BOTH "
    u"2026-08-28 AMENDMENTS** -- it carries neither b235's convention repair nor b239's RULE M-1 "
    u"binding, and so it still carries ### **the exact sentence b235 ruled was the defect** "
    u"(*\"in the CC sign convention\"*), which under `wInf - wPrimes` names `-A - PR`, *\"an "
    u"object the corpus does not compute.\"* ### **THE DRIFT RUNS THE WRONG WAY AGAINST THE "
    u"RESIDENCE RULING'S OWN WORDS** -- *\"lands here first and moves to the residence by tag, "
    u"never by drift\"* -- ### **so the residence is AHEAD of the working copy, the one direction "
    u"no check fires on.** ### **NOT REPAIRED (out of a READS act's scope); the other four files "
    u"in that directory are NOT audited and may carry the same drift.** *** "
    u"### **THE MISS THAT MATTERED MOST: I REACHED COMPONENT 4 BELIEVING THE TEXTS FIXED O1 AND "
    u"WAS DRAFTING \"FIXED BY TEXT\".** ### **What stopped it was the `banked_index` query, run "
    u"because `registration_gate.py` PUTS THE b160 CONVENTION IN THE PATH -- not because I "
    u"doubted the reading.** ### **AND THE AGGRAVATING FACT: THE READING I WAS ABOUT TO ADOPT IS "
    u"THE ONE THAT SHRINKS THE RESIDUAL.** That is b229's named crime approached from the "
    u"direction hardest to see -- ### **not by inserting a sign to help, but by ACCUMULATING "
    u"WARRANT FOR A SIGN THAT HAPPENS TO HELP.** ### **THE GATE EARNED ITS KEEP THIS ACT, AGAINST "
    u"THIS EXECUTOR AND NOT A HYPOTHETICAL ONE.** ### **AND THE DISCLOSURE THE STANDING CLAUSE "
    u"OWES: O1 SHRINKS THE RESIDUAL AND THAT IS NOT ITS WARRANT -- and NO orientation on the list "
    u"CLOSES the separation (V2 stays 19x-24x the bar, V3 8.6x-19x, and `resid47` is untouched by "
    u"every one).** *** "
    u"Gates 15 of 15 PASS, CLEAN -- ### **and NOT on the first run, which is reported because "
    u"b240's was**: run 1 produced TWO harness REFUSALS, neither a false pass (a `np.False_` "
    u"return, and a fixture that PASSED because it pointed at the checks file's own string "
    u"literal -- ### **b213's exact species, caught by the witness/fixture guard rather than by "
    u"me**). ### **TWO ABSENCES POSITIVELY CONTROLLED** as the ferry required. Term scan CLEAN, "
    u"0 live over 1264 lines -- ### **after a repair: I wrote the banned stem 9 times in my own "
    u"voice and the scan caught it**, and the repair touched only this act's own new files. "
    u"### **Four index keys filed. NO GRADE MOVED. NO VARIANT PROMOTED. M-2..M-5 STAND OPEN. "
    u"NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]

    assert lead.startswith(PREFIX), "### lead line is not the expected HANDOFF lead"
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0, "### no separator after the demoted title"
    old_title = tail[:cut]
    rest = tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b240: %r" % old_title
    assert NEW_TITLE not in lead, "### b241 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b240)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    # ### THE HEADLINE ASSERTIONS: every one of them names a thing this act must NOT lose.
    assert u"ONE RECONCILED-BY-TEXT, TWO ROUTED, TWO STANDING" in new_lead
    assert u"NO CORRECTION EXECUTED" in new_lead
    assert u"HOLDS AMENDED" in new_lead
    assert u"IS A TAUTOLOGY" in new_lead
    assert u"THE AGGREGATION IS UNSTATED" in new_lead
    assert u"W-ORD-FILE-E-WORKING-COPY-STALE" in new_lead
    assert u"SHRINKS THE RESIDUAL AND THAT IS NOT ITS WARRANT" in new_lead
    assert u"NOTHING DEPOSITS" in new_lead
    # ### AND THE ONE THAT GUARDS AGAINST THE ACT OVERCLAIMING ITS OWN DISSENT.
    assert u"REGISTERED BEFORE ITS VERDICT, NOT BEFORE ITS EVIDENCE" in new_lead

    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]

    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)

    back = io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2]
    ok = (back == new_lead)
    sys.stdout.write("  prior title, DERIVED : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title            : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length          : %d -> %d\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  prior content kept   : %s\n" % ("YES" if rest in back else "NO"))
    sys.stdout.write("  read-back identical  : %s\n" % ("YES" if ok else "NO"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
