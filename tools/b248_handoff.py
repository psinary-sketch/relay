# -*- coding: utf-8 -*-
"""b248_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.
### b248 OWNS THIS WRITE; b249's filings defer to it, per the parallel header."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE SECOND OBJECT AND THE PRECISION VEIL (b248 + b249)"
PRIOR_MARK = u"(b247)"

NEW = (
    u"*** ### **TWO ACTS IN PARALLEL, ONE SEAT. ### b248 OWNS THE LEDGER, PLACE-papers, HANDOFF AND "
    u"MIRROR WRITES; b249's FILINGS DEFER TO THIS CLOSE AND ARE CARRIED HERE.** *** "
    u"### **b248 -- THE E2 ARRANGEMENT: (ADDITIVE-FORCED), AND THE TEXTS FORCED THE READING THAT "
    u"DOES *NOT* SHRINK THE SHORTFALL.** ### **THREE ARRANGEMENTS BY THREE OWNERS, ALL ADDITIVE IN "
    u"`E2`:** sec 19 brackets `[Tr_inf + int g eps]`; `b36_act8.py:175` parenthesizes "
    u"`(Tr_full + E2 - Dneg)`; the ruled C2+D1 form is `Tr_full + E2 - Delta_-`. ### **b38:182 is "
    u"`A`'s EXPRESSION, NOT AN ARRANGEMENT OF `T`** -- sec 20(b) reads that same line as the CC-4.7 "
    u"REPRODUCTION ERROR against `[A + E2]`. ### **AND THE WORD 'REGULARIZED' NAMES A DIFFERENT "
    u"SUBTRACTION, WHICH IS UNPERFORMED:** sec 20(b)'s divergent-part subtraction, whose bench size "
    u"is `resid47` -- ### **THAT IS M-4, NOT `E2`.** *** "
    u"### **THE STANDING CLAUSE WAS OBEYED AT THE HARD END, NOT THE EASY ONE.** ### The registration "
    u"disclosed ### **BEFORE ANY VERDICT WAS DRAFTED** ### that the subtractive reading would have "
    u"cut `L - R` by ### **2*E2 = 1.950128 to 3.358857 -- 45% TO 50% OF A SHORTFALL RUNNING 4.07 TO "
    u"6.66** -- and banked the executor's draft verdict in the same file. ### **NO DECISION CARD WAS "
    u"ASSEMBLED**, because the card was conditional on (SUBTRACTIVE-FORCED): ### **AN EXECUTOR DOES "
    u"NOT MANUFACTURE A CARD FOR A RULING THE TEXTS DID NOT ASK FOR.** *** "
    u"### **THE SECOND OBJECT HAS ITS PER-CELL SPLIT FOR THE FIRST TIME.** "
    u"`-D_dict = (E2full + E2even) + (PR - Theta_q)`: ### **THE ARCHIMEDEAN PIECE CARRIES 88%-100% "
    u"(2.681242 down to 1.595154); THE JUNCTION PIECE 0%-12% (0.000000 to 0.244027).** ### The "
    u"registered prediction is ### **HALF RIGHT AND IS REPORTED AS HALF RIGHT**: limb 1 (vanishes at "
    u"`a^2 = 2`) ### **CONFIRMED EXACTLY**; limb 2 (grows with the active primes) ### **REFUTED**, "
    u"with drops at `a^2 = 4` (0.106484 -> 0.087342) and `a^2 = 9` (0.244027 -> 0.135020). "
    u"### **THE PREDICTION TREATED A DIFFERENCE OF TWO WEIGHTED SUMS AS THOUGH IT WERE A COUNT.** "
    u"### **NEITHER PIECE IS M-4's** -- M-4 covers `resid47` and nothing else (b246, unrevised). *** "
    u"### **b249 -- THE PRECISION VEIL IS LIFTED. ### BRANCH (PLUNGES). ### M-4 IS TRUE-AT-BENCH.** "
    u"### The corpus's OWN prolate instrument was extended into mpmath at ### **dps 120 / NQ 80**, "
    u"reaching `n = 0..12` on the EVEN sub-sequence per pin P1. ### **b205's STEPPER WAS NOT REUSED, "
    u"AND THE REASON IS b247's OWN VERDICT:** it solves the RRJT EXTERIOR ODE on `[1, infinity)`, and "
    u"b247 ruled its `alpha` and the prolate `xi_n(1)` ### **(DOUBLE-NAME)** -- reusing it would have "
    u"been the very error ruled against one act earlier. *** "
    u"### **THE VEIL SAT AT `n = 7`, WHERE b242's float64 SAW ONLY NOISE (4.7e-16). PAST IT, "
    u"`lambda(n)^2` CONTINUES CLEANLY -- 3.85e-16, 4.10e-20, 2.68e-24, 1.13e-28, 3.25e-33, "
    u"6.50e-38 -- AND `t(n)` PLUNGES: 1.12e-14, 1.35e-18, 9.91e-23, 4.65e-27, 1.46e-31, 3.18e-36**, "
    u"strictly decreasing from `n = 6` onward. ### **THE PARTIAL SUMS SETTLE AT "
    u"`22.996475683870529679`, AGAINST THE CORPUS'S INDEPENDENTLY BANKED `eps'(1+)` PIN "
    u"`22.9964757` (b35, 2026-08-18) -- EIGHT SIGNIFICANT DIGITS, AND THE PIN WAS NOT FITTED TO.** "
    u"### G-REPRO, G-SELF and G-EQ all PASS. ### **`W-ORD-MODE-PRECISION` (K3) DISCHARGED.** *** "
    u"### **AND THE FINDING THAT BEARS ON b247's CLAUSE (ii):** `xi_n(1)` DOES keep growing past the "
    u"veil -- 5.38, 5.74, 6.08, 6.40, 6.71, 7.00 -- ### **BUT ONLY SLOWLY, EVERY RATIO UNDER 1.2.** "
    u"### So the factor of 36,000 b247 measured across the certified range is ### **UTTERLY "
    u"DOMINATED** by a `lambda^2` falling four orders per mode. *** "
    u"### **AND THE LIMIT, IN THE SAME BREATH: TRUE-AT-BENCH IS A BENCH GRADE AND NOT A THEOREM.** "
    u"### It is a measurement over finitely many modes at one instrument setting. ### **M-4 IS NOT "
    u"PAID, AND ITS STATEMENT STILL HALTS AT CLAUSE (i)'s RATE, EXACTLY WHERE b247 LEFT IT.** "
    u"### **NO EXTRAPOLATION IS BANKED AS A BOUND** -- b242's refusal is the precedent and ### **A "
    u"MEASURED RATE IS NOT A TAIL BOUND.** ### **THE DERIVATION ACT'S CONFIRMATION IS NOW RECOMMENDED "
    u"TO THE AUTHOR.** *** "
    u"### **A THIRD CONSECUTIVE PRINT-FLOOR, NOW A NAMED DEFECT IN A WORK-ORDER.** ### b249's "
    u"G-REPRO took ### **THREE FORMS** ### before it was right, and the first two are disclosed: a "
    u"CONSTANT tolerance is NOT the ferry's criterion of *'within float64's own error'*, which is "
    u"MODE-DEPENDENT; and the comparison is additionally floored by ### **THE PRINTED PRECISION OF "
    u"b242's BANK** (ten significant digits for `lambda^2`, nine decimals for `xi`). ### **b245's "
    u"T-E MET b38's FOUR DECIMALS; b246 FLOORED AT 5e-5 FOR THE SAME REASON; b249 MET b242's TEN "
    u"DIGITS.** ### `W-ORD-TE-SPEC` requires a bank's AXES be named; ### **IT DOES NOT REQUIRE ITS "
    u"PRINTED PRECISION BE NAMED, AND IT SHOULD. ### FILED FOR EXTENSION.** ### **AND ONE MORE "
    u"RECURRENCE, IN b248's OWN GATES: a scope check matched `left_side` INSIDE A COMMENT** -- b242 "
    u"was forced into that repair and b243 and b246 carried it, and ### **b248 WROTE A FOURTH "
    u"MATCHER WITHOUT IT.** *** "
    u"Gates: b248 ### **11 of 11 CLEAN** (on the second run, the first catching the comment match); "
    u"b249 ### **12 of 12 CLEAN ON THE FIRST RUN.** ### Term scans CLEAN -- 707 lines (b248), 868 "
    u"(b249). ### The PLACE-papers hook was EXERCISED and reported ### **CLEAN, 0 foreign hits**; "
    u"the loom append is ### **ONE HUNK, 91 INSERTIONS, 0 DELETIONS**, prefix verified byte-for-byte; "
    u"### **THE MIRROR REBUILT AND VERIFIED CLEAN ON ALL THREE CLAUSES** (40 files, declared HEAD "
    u"`f5e878c` against ls-remote). *** "
    u"### **M-2..M-5 STAND OPEN AND NEITHER ACT CLOSED ANY.** ### **THE AUTHOR'S FORK AT THIS STOP: "
    u"THE PATENT SESSION, WHICH SLOTS HERE ON YOUR WORD AND NEEDS NOTHING FROM EITHER ACT; AND THE "
    u"M-4 DERIVATION ACT, WHOSE CONFIRMATION b249 NOW RECOMMENDS.** ### **NOTHING ABOUT h2 BEYOND "
    u"THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b247: %r" % old_title
    assert NEW_TITLE not in lead, "### b248 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b247)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"(ADDITIVE-FORCED)", u"NO DECISION CARD WAS\nASSEMBLED".replace("\n", " "),
                 u"HALF RIGHT AND IS REPORTED AS HALF RIGHT", u"BRANCH (PLUNGES)",
                 u"TRUE-AT-BENCH IS A BENCH GRADE AND NOT A THEOREM",
                 u"W-ORD-MODE-PRECISION` (K3) DISCHARGED",
                 u"THIRD CONSECUTIVE PRINT-FLOOR", u"PRINTED PRECISION BE NAMED, AND IT SHOULD",
                 u"THE PIN WAS NOT FITTED TO", u"NOTHING DEPOSITS"):
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
