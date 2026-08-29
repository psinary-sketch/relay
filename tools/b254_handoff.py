# -*- coding: utf-8 -*-
"""b254_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite. ### SOLO."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE FOURTH FACE-OFF (b254)"
PRIOR_MARK = u"(b253)"

NEW = (
    u"*** ### **BRANCH (IMBALANCED), AT EVERY CELL, UNDER *BOTH* `\u0394\u208b` REALIZATIONS.** "
    u"### The identity was measured at six cells as the TWO-TERM balance its algebra now is: "
    u"`L := (A + E2 \u2212 \u0394\u208b) + (\u2212\u0398_q)`, `R := A \u2212 PR`, so "
    u"`L \u2212 R = (E2 \u2212 \u0394\u208b) + (PR \u2212 \u0398_q)` with the `A` cancelling "
    u"identically. ### **THAT COMPOSITION IS ALGEBRAIC-RESTATEMENT AND WAS LABELLED SO IN THE "
    u"HASH-GATED MEANINGS FILE BEFORE THE RUN. ### AN IDENTITY THAT CANNOT FAIL CANNOT TESTIFY.** "
    u"### The evidence is the SIZES, SIGNS and CELL-PROFILES, and nothing else the table prints. *** "
    u"### **UNDER REALIZATION (A) -- the odd eps-MASK, the one the ruling's rider names:** residual "
    u"### **`-1.001814` to `-0.800154`, BEYOND BARS BY FOURTEEN ORDERS.** ### **UNDER REALIZATION "
    u"(B) -- the odd TRACE modes, quotable only as `Dneg(N = 11, float64 modes, suspect above "
    u"n = 6)`:** residual ### **`-0.061581` to `-0.533354`, beyond bars by 1.50x to 31x** -- "
    u"### **AND THE 1.50x AT `a^2 = 2` IS REPORTED AS MARGINAL RATHER THAN ROUNDED AWAY: it is the "
    u"one place in the whole table where the answer is nearly within its bar.** *** "
    u"### **THE PROFILE, WHICH IS WHAT THE BANKED MEANS ASKS FOR. ### SIGN: UNIFORMLY NEGATIVE. "
    u"### SIX CELLS, TWO REALIZATIONS, TWELVE ENTRIES, ONE SIGN** -- the cleanest single fact in "
    u"the table. ### **CELL-DEPENDENCE: NEITHER PROFILE IS MONOTONE IN `a^2`**, and the "
    u"non-monotonicity is reported as the finding it is and not smoothed. ### **(MIXED) IS "
    u"EXCLUDED, AND THE `a^2 = 2` ROW IS WHY:** the banked (MIXED) branch was *balanced where "
    u"primes vanish, imbalanced where active*; at `a^2 = 2` `PR` and `\u0398_q` are IDENTICALLY "
    u"ZERO -- the primes vanish -- ### **AND THE CELL IS IMBALANCED ANYWAY, UNDER BOTH "
    u"REALIZATIONS.** *** "
    u"### **THE ALGEBRAIC REDUCTION, DERIVED BEFORE THE RUN AND CONFIRMED BY IT:** under (A), "
    u"`\u0394\u208b \u2212 E2 = E2odd \u2212 (E2even + E2odd) = \u2212E2even`, so the balance IS "
    u"### **`E2even ?= \u0398_q \u2212 PR`.** ### At the pure-archimedean cell that is "
    u"### **`E2even ?= 0`, and `E2even = 1.001814` is a sum of eps sectors -- THE CELL CANNOT "
    u"BALANCE UNLESS `E2even` VANISHES, AND IT DOES NOT.** *** "
    u"### **A STRUCTURAL FINDING THE BAR COLUMN MADE VISIBLE: UNDER (A), *NOTHING IN THE BALANCE "
    u"IS A MODE SUM.*** ### `E2even`, `E2odd`, `PR` and `\u0398_q` are all fixed at the eps and "
    u"carto axes and do not move with `NQ` at all, so (A)'s bar is the eps mask certificate "
    u"(`8.882e-16`) alone. ### **SO Q1's DEMOTION AND b252's DIVERGENCE ARE ENTIRELY IRRELEVANT TO "
    u"THE BALANCE UNDER (A) -- AND THAT IS A STRONGER REASON THAN THE RIDER'S OWN, WHICH RESTED "
    u"ONLY ON CONVERGENCE.** ### Under (B) the balance DOES carry a mode sum, and with it b252's "
    u"suspicion and b253's QUOTED-N law. *** "
    u"### **`\u0394\u208b` HAS TWO REALIZATIONS AND b246 EXPLICITLY DECLINED TO CHOOSE** -- *\"Its "
    u"two realizations remain two objects and this act computed both rather than choosing.\"* "
    u"### **b254 COMPUTED BOTH AND CHOSE NEITHER, ON THAT PRECEDENT**, reading the branch under "
    u"the ruling's realization because the ruling names it and ### **TABULATING THE OTHER BESIDE "
    u"IT SO THE CHOICE IS VISIBLE IN THE TABLE RATHER THAN BURIED IN A BINDING.** ### They "
    u"disagree materially -- **16.3x at `a^2 = 2`** -- and agree on the verdict. *** "
    u"### **AND ONE OF THIS ACT'S OWN THREE CHARGES AGAINST THE RIDER'S CITATION IS WITHDRAWN AS "
    u"MY ERROR.** ### The meanings file banked that *\"by mode 6\" should read \"by mode 7\"*. "
    u"### **IT IS NOT SO: b246 CONTAINS BOTH PHRASES, IN TWO DIFFERENT SENTENCES ABOUT TWO "
    u"DIFFERENT QUANTITIES** -- the E2 ledger row's *\"to 3.9e-16 by mode 7\"* and, quoted from "
    u"b246's own registration, *\"the eps per-mode series CONVERGED BY MODE 6\"*. ### The correct "
    u"charge is that the ferry ### **FUSES TWO SEPARATE b246 SENTENCES INTO ONE CITATION**; each "
    u"half is present, but not together and not about the same quantity. ### **I CHECKED ONE "
    u"SENTENCE, FOUND IT SUFFICIENT, AND BANKED A CHARGE THE OTHER SENTENCE ANSWERS.** ### **THE "
    u"HARNESS CAUGHT IT BY *REFUSING* A GATE WHOSE MUST-FAIL FIXTURE PASSED**, which is exactly "
    u"what must-fail fixtures exist for. ### **THE HASH-GATED MEANINGS FILE WAS *NOT* EDITED "
    u"(b244's precedent, and b246's own when its tautology gate caught a sign error in its "
    u"definitions file): THE GATE WAS FIXED AND THE ERROR IS DISCLOSED IN THE BANK.** ### Charges "
    u"(i) and (iii) stand; ### **A COUNT OF THREE CORRECTIONS BECAME A COUNT OF TWO, AND THE ACT "
    u"SAYS SO RATHER THAN LETTING THE LARGER NUMBER STAND.** *** "
    u"### **A SECOND REGISTERED PREDICTION DID NOT FIRE, AND IS NOT CLAIMED.** ### The meanings "
    u"file banked *\"IF THE TWO REALIZATIONS DISAGREE ENOUGH TO FLIP THE BRANCH, THAT DISAGREEMENT "
    u"IS THE ACT'S REAL FINDING\"*. ### **THEY DO NOT FLIP IT -- BOTH GIVE (IMBALANCED) -- SO THE "
    u"CONDITION I ATTACHED THAT CLAIM TO WAS NOT MET, AND I DO NOT GET TO PROMOTE THE DISAGREEMENT "
    u"ON A CONDITION THAT DID NOT FIRE.** ### And a smaller one owned: I predicted the residual "
    u"*\"shrinking across the cells\"*; ### **IT DOES NOT SHRINK MONOTONICALLY -- IT RISES AT "
    u"`a^2 = 3`.** *** "
    u"### ### **WHAT THIS IMBALANCE IS NOT, FIXED IN THE MEANINGS FILE BEFORE IT WAS SEEN: IT IS "
    u"NOT EVIDENCE AGAINST THE IDENTITY `T + Q = W_inf \u2212 W_primes`.** ### b15 governs -- a "
    u"finite-place-set object at a finite cutoff decides ### **NOTHING GLOBAL** -- and ### **NO ACT "
    u"HAS PRODUCED EVIDENCE AGAINST THE FORM; CITING THIS ONE AS ANY WOULD BE A MISREADING.** "
    u"### **IT IS NOT A DEFICIT AND NO DEFICIT LANGUAGE IS USED: R-III GOVERNS.** ### **WHAT IT IS "
    u"EVIDENCE ABOUT IS THE *REALIZATION*** -- the same species of question M-2\u221e was, one "
    u"level down, which is why both columns are on the table. ### **IT IS `h2`'s BENCH SHADOW AT "
    u"CELLS, IN THE BANKED WORDS, AND `h2` STANDS EXACTLY AS OPEN AS IT DID BEFORE THIS ACT.** *** "
    u"Gates ### **14 of 14 CLEAN.** ### Term scan CLEAN, 0 live over 1207 lines. ### **THE "
    u"TAUTOLOGY CONTROL HAS BOTH HALVES: the composition holds on ARBITRARY values (restatement, "
    u"no evidence) while the residual's SIGN takes both signs on arbitrary values (so \"uniformly "
    u"negative at twelve entries\" is a property of the OPERATOR, not of the formula).** ### The "
    u"no-deficit gate is a POSITIVE CONTROL ON AN ABSENCE that had to be built carefully: "
    u"### **a scan banning the token outright would have banned the rule's own statement**, so it "
    u"checks that every occurrence sits inside a negation. ### **PLACE-papers NOT TOUCHED, SO THE "
    u"HOOK WAS NOT EXERCISED AND THE MIRROR NOT REBUILT -- REPORTED EITHER WAY.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) M-2's FINITE-PLACE ADDRESS -- the junction piece "
    u"`(PR \u2212 \u0398_q)` is now naked in its own column, and RULE Q's aggregation is STILL "
    u"UNSTATED.** ### **(2) M-3 (class richness) and M-5 (the missing transport), both untouched "
    u"by b250-b254.** ### **(3) `W-ORD-CN-LAW`** -- derive the `C/n` form from `A_n(0) = 1` and the "
    u"weight's source form. ### **(4) THE PATENT SESSION, which slots here on your word and needs "
    u"nothing from this act.** *** "
    u"### **THE IDENTITY IS CLAIMED NEITHER REFUTED NOR PROVED FROM FINITE CELLS. ### NO "
    u"REALIZATION WAS CHOSEN. ### M-2, M-3, M-4 AND M-5 STAND OPEN AND THIS ACT CLOSED NONE. "
    u"### THE FORM IS NOT INDICTED. ### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. "
    u"NOTHING DEPOSITS. LOCKS LAST.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]
    assert lead.startswith(PREFIX), "### lead line is not the expected HANDOFF lead"
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0, "### no separator after the demoted title"
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b253: %r" % old_title
    assert NEW_TITLE not in lead, "### b254 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b253)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (IMBALANCED), AT EVERY CELL",
                 u"BEYOND BARS BY FOURTEEN ORDERS",
                 u"TWELVE ENTRIES, ONE SIGN",
                 u"NEITHER PROFILE IS MONOTONE",
                 u"NOTHING IN THE BALANCE\nIS A MODE SUM".replace(u"\n", u" "),
                 u"COMPUTED BOTH AND CHOSE NEITHER",
                 u"IS WITHDRAWN AS\nMY ERROR".replace(u"\n", u" "),
                 u"FUSES TWO SEPARATE b246 SENTENCES INTO ONE",
                 u"WAS *NOT* EDITED",
                 u"THEY DO NOT FLIP IT",
                 u"IT DOES NOT SHRINK MONOTONICALLY",
                 u"NOT EVIDENCE AGAINST THE IDENTITY",
                 u"NO DEFICIT LANGUAGE IS USED",
                 u"NOTHING DEPOSITS"):
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
