# -*- coding: utf-8 -*-
"""b240_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

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

NEW_TITLE = u"THE FIRST FACE-OFF AT BENCH (b240)"
PRIOR_MARK = u"(b239)"

NEW = (
    u"*** ### **BRANCH (DISSONANT), AT ALL SIX DIAGONAL a^2 CELLS** -- separation **5.85 to 8.09** "
    u"against combined bars **0.203 to 0.745**, i.e. **10.85x to 28.8x** the registered factor "
    u"D = 10. ### **AND THE BANKED MEANING IS QUOTED WHOLE, INCLUDING THE HALF A READER SKIPS:** "
    u"*\"A dissonance is evidence about THE ASSEMBLY THIS ACT PERFORMED before it is evidence "
    u"about the identity.\"* ### **THE CEILING RIDES IN THE RUN'S OWN TABLE HEADER, not only in "
    u"the report** -- b15: *\"a finite-place-set object at a finite cutoff decides nothing "
    u"global\"*; ### **h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.** *** "
    u"### **WHAT MADE \"BEFORE\" CHECKABLE RATHER THAN PROMISED:** every meaning, bar, factor and "
    u"branch banked in `data/b240_meanings.txt` and ### **HASHED** (`ffef2e97...ca50d4c1`) ### "
    u"**BEFORE THE FIRST INSTRUMENT CALL**, with the run printing that hash into its own output. "
    u"### **The gate tests BOTH limbs -- the hash in the run AND the meanings file older on disk; "
    u"either limb alone is forgeable.** The meanings script imports ### **NO INSTRUMENT AT ALL**, "
    u"proved by running the same test against the run script where it fails; and ### **the "
    u"diagnostics tool REFUSES to execute unless the branch is already on disk.** *** "
    u"### **THE REGISTERED EXPECTATION WAS EXACT AS ARITHMETIC AND WRONG AS A DIAGNOSIS, AND BOTH "
    u"HALVES ARE REPORTED.** Written before the run from the instrument's source and no number: "
    u"the instrument defines `resid := Tr_full - A - E2`, so ### **L - R = 2*E2 + Delta_- + "
    u"resid47 + Theta_q + PR** -- ### **REPRODUCED BY THE RUN TO 8.9e-16 AT EVERY CELL.** ### "
    u"**BUT THE SUSPECT I NAMED WAS A MINORITY OF THE SEPARATION:** removing the predicted eps "
    u"double-count (V1) leaves **4.88 to 6.41 of a 5.85 to 8.09 separation** -- ### **at most a fifth**; "
    u"### **the dominant term is `resid47`, 2.31 to 4.05, the largest single term at every cell.** "
    u"b37's *\"resid47: 0 by construction (substitution at content)\"* is the SUBSTITUTED reading, "
    u"and ### **the ruling's C2 binding names the RAW instrument channels.** *** "
    u"### **THE ACT'S MOST USEFUL FINDING IS NOT THE ONE IT WENT LOOKING FOR: THE LEFT SIDE IS THE "
    u"UNCONVERGED SIDE, BY SIX ORDERS OF MAGNITUDE.** `bar_L` 0.203..0.745 against `bar_R ~1e-07`; "
    u"and `bar_L` is FOUR TIMES ### **ONE STEP** of the registered mode refinement (700,10) -> "
    u"(900,11) -- ### **one step of a series whose tail NOTHING IN THIS RECORD BOUNDS, b238's own "
    u"species one level up**, and a step that moves NQ and NMODE together so it mixes quadrature "
    u"with truncation. ### **FILED: `W-ORD-LEFT-MODE-AXIS`.** ### **The right side HELD ITS BANKED "
    u"BARS AT EVERY CELL**, including the three whose K was a declared SURROGATE (a^2 = 8, 9, 12, "
    u"which b238 never measured). *** "
    u"### **THE INDICTMENT RAN IN ITS REGISTERED ORDER AND SUSPECT 4 IS NOT INDICTED.** "
    u"Envelope/axes first (LIVE, larger than expected); the three-normalizations species second "
    u"(LIVE -- mechanism confirmed, size refuted); assembly conventions third (LIVE: flipping "
    u"Theta_q moves the separation by <= 1.04 and closes nothing, and ### **the restricted-product "
    u"assembly (M-2) WAS NEVER PERFORMED, so this act cannot indict it**); ### **THE FORM ITSELF "
    u"LAST AND NOT INDICTED -- suspects 1 and 2 account for the entire separation TERM BY TERM TO MACHINE "
    u"PRECISION and the largest term rides an unbounded truncation.** ### ### **THIS ACT PRODUCES "
    u"NO EVIDENCE AGAINST THE IDENTITY, AND CITING ITS BRANCH AS ANY WOULD BE A MISREADING.** *** "
    u"### **THE CLOSEST CELL IS STATED, NOT ROUNDED PAST: a^2 = 2 CLEARS D = 10 BY 8.5% (10.85). "
    u"HAD THE FACTOR BEEN 12 THAT CELL WOULD READ (INDETERMINATE)** -- the factor was fixed before "
    u"any number and is not revised now, and the branch is unchanged because the other five clear "
    u"by 14x to 29x. *** "
    u"### **THE CHECKLIST NOW READS FIVE ITEMS AND THE FIFTH IS OURS:** (1) `T.value` GREEN; "
    u"(2) M-2 OPEN, ### **not required and not performed -- so this face-off is a PER-CELL "
    u"statement and not a structural one, exactly as b239 said it would have to be**; (3) the "
    u"Interfaces re-print GREEN; (4) the right side's bars ### **AMBER: MEASURED, NOT CERTIFIED**; "
    u"### **(5) THE LEFT SIDE'S OWN BARS -- AMBER, AND WORSE THAN (4).** ### **M-LIST: FOUR OPEN "
    u"(M-2..M-5).** `W-ORD-IMP1-ENVELOPE` ### **STANDING**: its registered role was to gate a "
    u"verdict on (INDETERMINATE), so it does not gate this one and ### **IT IS NOT DISCHARGED.** "
    u"*** "
    u"### **THE AUTHOR'S FORK AT THIS STOP, NAMED: (i) THE PATENT SESSION** -- it can slot at any "
    u"STOP and needs nothing from this act; ### **(ii) THE RECONCILIATION WAVE** -- its trigger "
    u"was the checklist resolved, and the checklist now stands at ### **TWO GREEN, ONE OPEN-BY-"
    u"DESIGN, TWO AMBER**, so the wave is a JUDGEMENT and no longer a countdown; ### **(iii) THE "
    u"ENGINE (M-2..M-5)** -- four named items, one ruling-or-result, two results, one "
    u"construction. ### **AND EITHER WAY TWO BOUNDED BENCH ITEMS STAND READY: "
    u"`W-ORD-LEFT-MODE-AXIS` and `W-ORD-IMP1-ENVELOPE`.** "
    u"Gates 15 of 15 PASS, CLEAN on the first run; C0 void gates, the eps mask algebra and the "
    u"eps'(1+) pins (including the odd split 8.819138 of 22.996476, verified BEFORE Delta_- was "
    u"used) all PASS; G-INDEP PASS read from the instruments' own source. ### **NO MEANING "
    u"INVENTED AFTER THE NUMBERS. NO VARIANT PROMOTED TO PRIMARY. NO BAR WIDENED. NO AXIS "
    u"INTRODUCED AFTER A RESIDUAL. NO GRADE MOVED. NO KERNEL TOUCHED. NOTHING ABOUT h2 BEYOND THE "
    u"REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b239: %r" % old_title
    assert NEW_TITLE not in lead, "### b240 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b239)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    assert u"(DISSONANT)" in new_lead and u"NOT INDICTED" in new_lead
    assert u"W-ORD-LEFT-MODE-AXIS" in new_lead
    assert u"THE AUTHOR'S FORK AT THIS STOP" in new_lead

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
