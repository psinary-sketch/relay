# -*- coding: utf-8 -*-
"""b245_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

### THE DEMOTED TITLE IS DERIVED FROM THE FILE'S OWN LEAD LINE, never typed from memory, and
### EVERY assertion runs BEFORE the write.
"""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE SECOND FACE-OFF (b245)"
PRIOR_MARK = u"(b244)"

NEW = (
    u"*** ### **BRANCH (DISSONANT-BEYOND)** -- by the rule banked before any number, and "
    u"### **THE BRANCH FIRED ON A TEST THIS EXECUTOR MIS-SPECIFIED.** ### The ruled combination "
    u"`L := (Tr_full + E2 - Delta_-) + (-Theta_q)` was computed ### **FOR THE FIRST TIME BY ANY "
    u"ACT** -- b240 ran the opposite two signs -- against `R := A - PR` at the banked six cells, "
    u"NMODE = 7 per RULE MODES K1. *** "
    u"### **|L - R| RUNS 6.662044 DOWN TO 4.072688 AGAINST BOUNDED BARS OF 1.028 DOWN TO 0.303.** "
    u"### **THE COLUMNS DO NOT MEET AND THEY ARE NOT CLOSE** -- and ### **EVEN CREDITING b242's "
    u"REFUSED TAIL ESTIMATE** (bounded + flagged = 3.10 at a^2 = 2 down to 0.88 at a^2 = 12), "
    u"### **THE SHORTFALL STILL EXCEEDS IT BY 2.1x TO 4.6x**, so the mode tail does not explain "
    u"it either. *** "
    u"### **FOUR OF THE FIVE CONTENTFUL TESTS PASS**, including the two that could most easily "
    u"have failed: ### **T-B, the NV-invariance of the whole comparison** (0.0 to 3.02e-08 against "
    u"a 1e-6 tolerance), and ### **T-C, the endpoint convention at a^2 = 2** where `PR` and "
    u"`Theta_q` are EXACTLY zero and `L - R` reduces to the archimedean channels at 0.000e+00. "
    u"### **T-A HOLDS THE M-4 SHAPE AT EVERY CELL:** `(L-R)/resid47` = 1.673543, 1.761108, "
    u"1.763367, 1.813805, 1.766653, 1.784943 -- ### **AN 8.4% SPREAD ACROSS SIX CELLS**, inside the "
    u"registered band [1.40, 2.10]. *** "
    u"### **T-E FAILED BY 6.78e-02 AGAINST A REGISTERED 1e-5 -- AND THE DIAGNOSTIC, RUN AFTER THE "
    u"BRANCH AND WITHOUT TOUCHING IT, NAMES THE TERM TO FIVE FIGURES.** ### I registered a "
    u"cross-check against b38's bank of 2026-08-18 ### **WHICH WAS COMPUTED AT TEN MODES, WHILE "
    u"THE RULING I EXECUTED THE ACT BEFORE SET SEVEN.** ### The deviation equals "
    u"`tr[7]+tr[8]+tr[9]` at ALL SIX CELLS to 5e-5 -- ### **b38's OWN ROUNDING FLOOR** -- read "
    u"from b242's independently banked per-mode table. ### **SO T-E DETECTED THE RULING DOING "
    u"EXACTLY WHAT IT WAS RULED TO DO, NOT INSTRUMENT DRIFT.** ### **THE BRANCH STANDS: A BANKED "
    u"RULE IS NOT REVISED BECAUSE THE EXECUTOR LATER UNDERSTANDS WHY IT FIRED** -- b238 refused to "
    u"widen a criterion by one keystroke and took (HELD); this act refuses to re-scope a test "
    u"after its result. *** "
    u"### **AND THE FILING THE BRANCH FORBIDS WAS NOT MADE: THE RESIDUAL PROFILE IS *NOT* FILED "
    u"AS M-4's MEASURED SHADOW**, because the ferry conditioned that on (ACCOUNTED). ### b238 set "
    u"the precedent exactly, declining the right-side spec on (HELD). ### **WHAT IS RECORDED AS A "
    u"MEASURED FACT AND NOT AS A FILING:** `resid47` is ### **ONLY 56%-60% OF THE SHORTFALL**, and "
    u"the remainder is the corpus's own dictated deviation `-D_dict` (sec 20(a)) -- ### **WHICH IS "
    u"NOT M-4 AND IS NOT PAID BY PAYING M-4.** ### The executor registered that caveat in the "
    u"meanings file BEFORE the run and it held. *** "
    u"### **THE HONEST K1 BAR IS LARGER THAN b240's, AND THAT RUNS AGAINST THIS PROGRAMME'S "
    u"INTEREST:** b240's `bar_L` at a^2 = 2 was 7.452637e-01; ### **this act's BOUNDED part alone "
    u"is 1.027704e+00**, 1.38x larger, with the FLAGGED tail on top. ### **b242 SAID bar_L MIGHT "
    u"BE TOO SMALL AND THE HONEST FORM IS INDEED BIGGER.** ### The mode refinement moved "
    u"### **NMODE ALONE (7 -> 6) AT NQ HELD** -- b242 showed b240's step was ~94% quadrature and "
    u"this act does not repeat it. ### **AND THE TAIL SENTENCE RIDES IN THE RUN'S OWN TABLE, NOT "
    u"ONLY IN THE REPORT: 'A BAR CARRYING THIS TERM IS NOT A CERTIFIED BAR AND NO NUMBER BESIDE "
    u"IT IS CERTIFIED.'** *** "
    u"### **NO EVIDENCE AGAINST THE IDENTITY'S FORM. SUSPECT 4 IS NOT INDICTED** -- suspects 1 and "
    u"2 carry the shortfall and the branch fired on a mis-specified test. ### **CITING THIS BRANCH "
    u"AS EVIDENCE AGAINST THE IDENTITY WOULD BE A MISREADING**, and a worse one than b240's, "
    u"because here the failing test's cause is MEASURED. *** "
    u"### **THE ALGEBRAIC RESTATEMENT WAS LABELLED BEFORE THE RUN AND CARRIES NO EVIDENTIAL "
    u"WEIGHT:** `L - R = resid47 + (2*E2 - Delta_- + PR - Theta_q)` reproduced at 0.000e+00 at "
    u"every cell, and ### **THAT CONFIRMS NOTHING** -- the harness demonstrates it holds on "
    u"arbitrary tuples. ### b240 reported an 8.9e-16 'reproduction' of this species and b241 found "
    u"it was `x = x`; ### **THIS ACT DID NOT MAKE THAT CLAIM AGAIN.** *** "
    u"### **A DISCLOSED RE-EMISSION: the meanings file was re-emitted ONCE and the whole chain "
    u"re-ran**, because the banned stem `blind` appeared twice in its own voice and the meanings "
    u"file is HASH-GATED. ### **A STANDING TERM LAW AND A STANDING ORDER-OF-OPERATIONS GATE PULLED "
    u"OPPOSITE WAYS, AND BOTH WERE OBEYED:** a line diff shows ### **EXACTLY THREE CHANGED LINES** "
    u"-- the timestamp and the two stems -- ### **NO RULE, BAND, FACTOR, TOLERANCE, BRANCH "
    u"DEFINITION, AXIS OR CONSTANT MOVED**, the pre-repair file is retained so the diff can be "
    u"re-derived, and the re-run reproduced ### **EVERY VALUE IDENTICALLY WITH THE BRANCH "
    u"UNCHANGED.** ### **AN MTIME WAS NOT FORGED; the run tool was honestly edited to carry the "
    u"disclosure and says so in its own header.** *** "
    u"### **THE SPECIES THIS SEAT HAS NOW HAD IN THREE CONSECUTIVE ACTS, NAMED:** b243's sentence "
    u"contradicting its own table, b244's fixture that was its check negated, and b245's "
    u"cross-check against an axis its own prior act had moved. ### **EACH TIME THE ARTEFACT WAS "
    u"CHECKED AGAINST WHAT I INTENDED RATHER THAN AGAINST WHAT THE PRIOR ACT HAD ACTUALLY DONE.** "
    u"### **`W-ORD-TE-SPEC` FILED, NOT BUILT:** a cross-check against a bank must name the axes "
    u"the bank was computed at and refuse if they differ from the run's. *** "
    u"### **THE AUTHOR'S FORK AT THIS STOP, NAMED: (i) THE PATENT SESSION** -- it slots at this "
    u"STOP on the author's word and needs nothing from this act; ### **(ii) M-4** -- the eps "
    u"trace-class bookkeeping, whose bench shadow now has a magnitude and a cell-profile but is "
    u"NOT PAID and whose profile is NOT FILED; ### **(iii) `W-ORD-MODE-PRECISION` (K3)** -- the "
    u"extended-precision prolate eigensolver, priced by b242 at ~130-175 dps for a useful tail, "
    u"### **A DIFFERENT INSTRUMENT AND NOT A REFINEMENT OF THIS ONE.** *** "
    u"Gates 14 of 14 PASS, CLEAN, with ### **every fixture failing for a structurally different "
    u"reason than its check passes**, as the ferry sharpened the rule after b244's self-catch. "
    u"Term scans CLEAN, 0 live over 1725 lines. ### **M-2..M-5 STAND OPEN AND THIS ACT CLOSED "
    u"NONE.** ### PLACE-papers, the loom and the mirror were NOT touched, so the hook did not run "
    u"and no mirror rebuild was required -- said rather than left to be inferred. ### **NO AXIS, "
    u"MESH, MODE COUNT, eps OR CONSTANT CHANGED AFTER A NUMBER WAS SEEN. NO GRADE MOVED. NOTHING "
    u"ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b244: %r" % old_title
    assert NEW_TITLE not in lead, "### b245 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b244)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (DISSONANT-BEYOND)", u"MIS-SPECIFIED",
                 u"THE BRANCH STANDS", u"NOT* FILED", u"56%-60% OF THE SHORTFALL",
                 u"SUSPECT 4 IS NOT INDICTED", u"EXACTLY THREE CHANGED LINES",
                 u"THREE CONSECUTIVE ACTS", u"THE PATENT SESSION",
                 u"W-ORD-MODE-PRECISION", u"NOTHING DEPOSITS"):
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
