# -*- coding: utf-8 -*-
"""b246_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE TWO TAILS (b246)"
PRIOR_MARK = u"(b245)"

NEW = (
    u"*** ### **BRANCH (TWO OBJECTS) -- AND IT FAILS WIDE, NOT NARROWLY.** ### The question was "
    u"whether b245's shortfall is the even- and odd-sector tails of ONE mode series. "
    u"### **ALL FIVE REGISTERED TESTS FAIL UNDER THE PRIMARY READING, FOUR OF THEM BY THREE TO "
    u"FIVE ORDERS PAST THEIR BANDS:** T-1 by 1.76-2.62 against a 5e-5 floor; T-2 by 0.43-1.22; "
    u"T-3's ratio 4.35-5.85 against the band [1.673, 1.785]; T-4 NOT MONOTONE; T-5 failing at five "
    u"of six cells. ### **THE TWO TERMS STAY SEPARATELY OWNED**, and ### **THE SENTENCE 'paying "
    u"M-4 pays the whole bench shortfall' MAY NOT BE WRITTEN.** *** "
    u"### **AND THE STRUCTURAL REASON, CHECKABLE FROM THE PRINTED COLUMNS RATHER THAN FROM THE "
    u"BANDS:** ### `resid47` is a shortfall of the ### **TRACE** ### series -- b242 measured it "
    u"### **STILL AT 0.257 AT MODE 6** and not converging. ### `-D_dict` is "
    u"`E2full + E2even + (PR - Theta_q)`, which is ### **SECTOR ARITHMETIC ON THE eps SERIES -- "
    u"AND THAT SERIES IS CONVERGED BY MODE 6**, its per-mode terms falling 8.17e-01, 6.74e-01, "
    u"1.85e-01, 4.04e-03, 1.35e-05, 1.56e-08, 7.90e-12, then ### **3.90e-16.** "
    u"### ### **A CONVERGED SERIES HAS NO TAIL, SO `-D_dict` CANNOT BE ONE.** ### The measured "
    u"eps tail beyond K1 is 1e-18 to 5e-13 -- ### **FIFTEEN ORDERS BELOW `D_dict`.** *** "
    u"### **BOTH SEATS' EXPECTATIONS WERE REGISTERED AND BOTH ARE REPORTED: THE NAVIGATOR'S WAS "
    u"(ONE OBJECT) AND IS NOT BORNE OUT; THE EXECUTOR'S WAS (TWO OBJECTS) 'AND I EXPECT IT TO FAIL "
    u"WIDE, NOT NARROWLY' -- BORNE OUT, AND FOR THE REGISTERED REASON**, which was banked before "
    u"the run: *\"the two series do not have comparable tails.\"* *** "
    u"### **THE NEAR-MISS, REPORTED AS A MISS AND NOT AS SUPPORT:** the alternate reading (R3), "
    u"the FULL eps sectors, gives T-3 ratios 1.676, 1.665, 1.647, 1.599, 1.591, 1.572 -- "
    u"### **INSIDE THE BAND AT a^2 = 2 AND NOWHERE ELSE**, drifting 12% low by a^2 = 12. "
    u"### **THREE READINGS WERE REGISTERED IN ADVANCE SO THE ONE-OBJECT HYPOTHESIS GOT ITS BEST "
    u"SHOT**, and (R3) is an ALTERNATE that ### **MAY NOT BE PROMOTED TO PRIMARY AFTER ITS NUMBERS "
    u"ARE SEEN.** ### The coincidence is explained rather than left to be guessed: at a^2 = 2 both "
    u"`PR` and `Theta_q` VANISH, so two different quantities fall within 0.2% of each other and "
    u"### **DIVERGE AS SOON AS THE FINITE PLACES TURN ON.** *** "
    u"### **THE ONE CLEAN CROSS-CHECK OF THIS ARC PASSED:** the parity split of the eps series, "
    u"computed today from b242's arrays, ### **REPRODUCES b38's `D_dictated` COLUMN OF 2026-08-18 "
    u"TO ~1e-6 AT EVERY CELL** -- an eleven-day-old bank, a different code path. ### **THAT IS THE "
    u"CROSS-CHECK b245's T-E WAS TRYING TO BE**, and it worked here for one reason: "
    u"### **THE AXES WERE MATCHED AND PRINTED BEFORE ANY NUMBER WAS COMPARED**, which is "
    u"`W-ORD-TE-SPEC` honoured in form. ### The b38/K1 mismatch (NMODE 10 against 7) was named in "
    u"the run's own header rather than discovered in a diagnostic afterwards. *** "
    u"### **THE DOUBLE NAME WAS COMPUTED AND KEPT APART, NOT CHOSEN BETWEEN:** `Dneg_raw` (the raw "
    u"odd-trace slice, `b36_act8.py:172`) runs 1.617848 down to 0.693004; `Delta_-` (the odd eps "
    u"mask, sec 17/sec 19's definition) runs 0.677615 down to 0.354973. ### The ferry's '(raw odd "
    u"slice - masked odd series)' is reported under its own name ### **`SECTOR_SPLIT_DIFF`**, "
    u"because ### **IT IS NOT `D_dict` AND CALLING IT SO WOULD BE THE DOUBLE-NAME SPECIES b241 "
    u"CAUGHT.** *** "
    u"### **THE FIVE-TERM LEDGER DOES NOT COLLAPSE.** ### `E2` is now shown to sit on a CONVERGED "
    u"series and has no tail to be anyone's; `resid47` is separately owned on the TRACE series; "
    u"`Delta_-` and `Theta_q` stay ruled; `PR` stands. ### **M-4's SCOPE IS NARROWED BY "
    u"MEASUREMENT: IT COVERS `resid47` AND NOT `-D_dict`.** *** "
    u"### **THE MISS OF THIS ACT'S OWN, AND THE TAUTOLOGY GATE CAUGHT IT:** the definitions file "
    u"declares the shortfall identity as `resid47 + D_dict = L - R`. ### **THAT IS FALSE; THE TRUE "
    u"IDENTITY IS `resid47 - D_dict = L - R`.** ### The tautology control tested the `+` form on "
    u"400 random tuples, it did not hold, and ### **THE GATE FAILED -- THE FIRST TIME IN THIS ARC "
    u"A HARNESS CAUGHT A DEFECT IN A *CLAIM* RATHER THAN IN A *STRING*.** ### **THE BANKED "
    u"DEFINITIONS FILE IS NOT EDITED** -- b244's precedent governs -- and the error is disclosed "
    u"in the bank instead. ### **IT CHANGES NO VERDICT:** T-2 was implemented exactly as the FERRY "
    u"worded it, and under BOTH signs the test fails wide (1.30 vs 0.08 with `+`, 6.66 vs 0.08 "
    u"with the true `-`). *** "
    u"### **b247 IS NAMED AS NEXT: THE M-4 STATEMENT AND ROUTE**, its asset list STARTED and "
    u"### **NOT VERIFIED** -- act 15's derived pair geometry (File E's own owner line cites it); "
    u"the Wronskian norm-slope identity (indexed, grade ### **DERIVED AT CONTENT ON NAMED IMPORTS, "
    u"NOT A PROOF FROM NOTHING**); b242's measured decay; Lemma F.1; and ### **Slepian-Widom decay "
    u"as CANDIDATE IMP-3 under the import bar, verified-where-tooled only -- nothing in this corpus "
    u"has read it at content and this act does not pretend otherwise.** ### **THAT IS A LIST OF "
    u"NAMED ASSETS, NOT A ROUTE.** *** "
    u"Gates 15 of 15 PASS, CLEAN on the second run, the first having caught the sign error above. "
    u"Term scans CLEAN, 0 live over 1267 lines. ### **b245's BRANCH WAS NOT REVISED. NO FACE-OFF "
    u"WAS RUN AND NO COLUMN RECOMPUTED. M-2..M-5 STAND OPEN AND THIS ACT CLOSED NONE.** "
    u"### PLACE-papers, the loom and the mirror were NOT touched, so the hook did not run and no "
    u"mirror rebuild was required. ### **THE AUTHOR'S FORK AT THIS STOP: the patent session, which "
    u"slots here on your word and needs nothing from this act; b247 (M-4's statement and route); "
    u"and `W-ORD-MODE-PRECISION` (K3).** ### **NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE "
    u"EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b245: %r" % old_title
    assert NEW_TITLE not in lead, "### b246 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b245)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (TWO OBJECTS)", u"A CONVERGED SERIES HAS NO TAIL",
                 u"MAY NOT BE WRITTEN", u"REPORTED AS A MISS AND NOT AS SUPPORT",
                 u"THE TRUE IDENTITY IS", u"IS NOT EDITED",
                 u"b247 IS NAMED AS NEXT", u"NOT A ROUTE",
                 u"b245's BRANCH WAS NOT REVISED", u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must

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
