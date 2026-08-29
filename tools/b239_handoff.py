# -*- coding: utf-8 -*-
"""b239_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

### THE RISK THIS SCRIPT EXISTS TO REMOVE: that bringing the lead current QUIETLY DROPS the
### previous act's headline. ### The demoted title is DERIVED from the file's own line -- never
### typed from memory -- and EVERY assertion below runs BEFORE the write.
"""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE RULING EXECUTED (b239)"

NEW = (
    u"*** ### **THE RULING IS EXECUTED WHOLE: `T.value` IS DEFINED IN THE RECORD BY THE AUTHOR'S "
    u"RULING, ITS RIDER BESIDE IT, AND ITS DEBT NAMED IN THE CORRESPONDENCE ROW.** The ruling, "
    u"verbatim: \"RULE M-1: C2, per-cell instrument realization standing until M-4 closes; "
    u"\u0394\u208b's bookkeeping (M-4) named as the definition's open debt in the correspondence "
    u"row.\" ### **Three clauses, three obligations, all three discharged** -- and the third in "
    u"the CORRESPONDENCE ROW, because *a debt recorded only where the executor writes is a debt "
    u"the next reader will not meet.* *** "
    u"### **THE IDIOM WAS CHOSEN AND SHOWN: DOCUMENTED BINDING, NOT LEAN CODE.** `Tr_full`, `E2` "
    u"and \u0394\u208b have NO formal definitions in this repository; writing `value := Tr_full + "
    u"E2 + \u0394\u208b` as code would mean ### **INVENTING THREE REALIZATIONS THE RECORD DOES NOT "
    u"HAVE** -- exactly the \"realization invented\" b237's scope refused one act ago. ### **The "
    u"choice and the refusal's reason were registered BEFORE the choice was made**, so the "
    u"softer-looking option stands on the record as the disciplined one and not the convenient "
    u"one. *** "
    u"### **THE AMENDMENT MOVED NO CODE, AND THAT WAS VERIFIED EXACTLY RATHER THAN BY EYE:** with "
    u"every comment and docstring stripped, File E's code is ### **IDENTICAL TO ITS HEAD BLOB**; "
    u"the relation stands unmoved at line 107, `T.value + Q.value = W.wInf - W.wPrimes`, ### "
    u"**STATED, NOT PROVED, NOT CLAIMED.** ### **CORRESPONDENCE ROW 90** by the committed tool, "
    u"six cells, no blanks, verified by read-back; grade cell ### **\"DEFINED-BY-RULING (C2), "
    u"REALIZED PER-CELL AT BENCH, OPEN DEBT M-4 (\u0394\u208b trace-class bookkeeping)\"**; "
    u"terminal cell: **no new terminal.** *** "
    u"### **THE DISCLOSED DEBT IS DISCHARGED BY RUNNING IT, NOT BY DISCLOSING IT A FOURTH TIME.** "
    u"b235, b236 and b237 each amended or read File E and disclosed that the Interfaces layer had "
    u"not been re-elaborated; ### **a fourth silence would have become a claim.** ### **TWO PINS, "
    u"BECAUSE THE BANK ITSELF SAYS SO** -- five files at v4.30.0-rc1 / mathlib4 `cecd0c4d56` (the "
    u"README's declared pin) and `RestrictedTensorLayer1` at v4.29.0, its banked profile's own "
    u"header; ### **one pin for both would be comparing a new profile to an old bank and calling a "
    u"toolchain difference a finding.** ### ### **RESULT: 29 TERMINALS PRINTED, 29 MATCHED TO "
    u"BANK, 0 DIFFERING, 0 NOT IN BANK, COUNTS AGREE** -- and "
    u"`FiniteInstanceIdentity.finiteInstanceIdentity` ### **MATCH: File E has been amended TWICE "
    u"and its profile is UNCHANGED.** *A docstring cannot move a profile -- and this act did not "
    u"assert that.* ### **IT RAN THE PRINT.** *A compile is not a verification and the profile is "
    u"read: b227 shipped a file that compiled clean and printed `sorryAx`; b231 shipped one that "
    u"compiled clean and printed EIGHT axiom-bearing terminals.* ### **What the match does NOT "
    u"mean: that the statements are true -- only that their axiom dependencies are what the record "
    u"says. CORE WAS NOT TOUCHED AND ITS 404-LINE PROFILE WAS NOT RE-RUN.** *** "
    u"### **THE FACE-OFF CHECKLIST IS FINAL: THREE GREEN, ONE AMBER.** ### **(1) `T.value` -- "
    u"GREEN**, ruled and executed. **(2) the assembly junction (M-2) -- OPEN, and the per-cell "
    u"bench form does not require it**: ### **the rider's whole content is per-cell realization**, "
    u"and b237 placed the junction at the restricted-product ASSEMBLY across places, not at the "
    u"per-place computation (`\u0398_q` computes each per-place term on `V_inv` without touching "
    u"`S\u0304_v`) -- ### **and the price in the same breath: a per-cell face-off is a PER-CELL "
    u"statement and not a structural one, and b240 must carry that limit in its own words.** "
    u"### **(3) the Interfaces re-print -- GREEN**, discharged this act 29/29. ### **(4) the right "
    u"side's error bars -- AMBER: MEASURED, NOT CERTIFIED**, b238's annotation carried unchanged "
    u"(agreement ~2e-08 relative at a^2=3 and 5e-09 at a^2=4, but the banked bound exceeded at one "
    u"cell of six by 4%, `W-ORD-IMP1-ENVELOPE` the named remainder). ### **THAT IS NOT A BLOCK ON "
    u"b240 -- IT IS A LIMIT b240 MUST STATE.** *** "
    u"### **THE M-LIST, WITH M-1 STRUCK: FOUR OPEN.** ~~M-1 [RULING]~~ ruled and executed; **M-2 "
    u"[RESULT or RULING]** open (b227: *\"THE FIRST IS NOT IN THE RECORD\"*); **M-3 [RESULT]** "
    u"open (class-richness, *\"formalization owed to files B-C\"*); **M-4 [RESULT]** open -- ### "
    u"**and now ALSO the definition's named debt, the one item the executed ruling made "
    u"load-bearing for a DEFINITION rather than only for a proof**; **M-5 [CONSTRUCTION]** open "
    u"(*\"the missing transport\"*). *** "
    u"### **WHAT WAS REFUSED, AND IT WAS THE LARGEST TEMPTATION THIS ARC HAS CARRIED:** with "
    u"`T.value` defined and `A - PR` already adopted, ### **a single instrument call would have "
    u"produced both sides at a cell.** It was named at registration as this act's principal risk "
    u"and it was refused. *** "
    u"### **NEXT IS b240, THE FIRST FACE-OFF AT BENCH**, under its own registration, ### **with "
    u"both sides' meanings fixed before any number is seen**, preconditions ### **THREE GREEN AND "
    u"ONE AMBER -- the amber is (4), the right side's error bars, MEASURED BUT NOT CERTIFIED, and "
    u"b240 states that limit in its own words.** ### **THE RECONCILIATION WAVE'S TRIGGER -- the "
    u"checklist resolved -- IS NOW ONE ACT AWAY. The patent session can slot at any STOP.** "
    u"Gates 12 of 12 PASS, CLEAN on the first run; all three term scans CLEAN, 0 hits (relay 707 "
    u"lines, PLACE 94, SGS 29). ### **NO FACE-OFF. NO NUMBER CROSSED BETWEEN COLUMNS. NO OPERATOR "
    u"CONSTRUCTED. NO GRADE RE-GRADED (b237's index row ANNOTATED, NOT REWRITTEN -- a row is a "
    u"pointer and never a re-grading). CORE UNTOUCHED. NOTHING DEPOSITS. LOCKS LAST.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]

    # ### ASSERTIONS, ALL BEFORE THE WRITE.
    assert lead.startswith(PREFIX), "### lead line is not the expected HANDOFF lead"
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0, "### no ' %s ' separator after the demoted title" % DASH
    old_title = tail[:cut]
    rest = tail[cut + len(SEP):]
    assert old_title.endswith(u"(b238)"), "### derived prior title is not b238: %r" % old_title
    assert NEW_TITLE not in lead, "### b239 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b238)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    # ### THE DEMOTION LOSES NOTHING: the old line's whole content survives verbatim.
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    assert u"b240" in new_lead and u"THREE GREEN AND ONE AMBER" in new_lead
    assert u"MEASURED, NOT CERTIFIED" in new_lead

    lines[2] = new_lead
    out = u"\n".join(lines)
    # ### ONLY LINE 3 MOVES.
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
