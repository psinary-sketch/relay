# -*- coding: utf-8 -*-
"""b251_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.
### b251 is SOLO and owns this write."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE THIRD FACE-OFF (b251)"
PRIOR_MARK = u"(b250)"

NEW = (
    u"*** ### **THE SHORTFALL'S DOMINANT TERM NOW HAS ITS TRUE NAME, AND THE NAME IS NOT A "
    u"NUMBER.** ### **BRANCH (IMPOSTER-NAMED), ON ITS ACCOUNTING LIMB.** ### The re-attribution "
    u"was derived from the owners' SOURCE TEXT before any run, and it is the whole act: "
    u"### **BOTH OWNERS THAT STATE THE RESIDUE LINE STATE THE SAME THING** -- `b38_act10.py:182` "
    u"`resid = TrN - A - E2N` and `b36_act8.py:184` `resid47 = Tr_full - (A + E2)` -- so "
    u"### **`resid47` IS *ALREADY* A TWO-REALIZATIONS DIFFERENCE**: the archimedean trace built as "
    u"a MODE SUM (`trace_modes`, a corr-weighted dilation overlap) minus the same object built as "
    u"a QUADRATURE (`left_side`, one `U`-axis integral with NO mode index), less `E2`. "
    u"### ### **THE NAME `resid47` CONCEALED ITS SPECIES FOR MANY ACTS. ### IT IS NOT A REMAINDER, "
    u"A DEFECT OR AN ERROR TERM -- IT IS A DISAGREEMENT BETWEEN TWO DEFINITIONS.** *** "
    u"### **THE TABLE, SIX CELLS, THREE NAMED PIECES, NOTHING BEYOND THEM.** "
    u"### `Delta_2real` carries ### **60.775% TO 69.995% OF `L - R` AT EVERY CELL** -- dominant "
    u"without exception. ### The RULED BINDING's own terms `2*E2full - Dneg` carry "
    u"**30.005%-34.546%**, ### **tabulated even though they are not a suspect, because "
    u"suppressing a third of the shortfall would have misreported what `Delta_2real` is being "
    u"credited with.** ### The junction piece `(PR - Theta_q)` carries **0.000%-5.874%** and is "
    u"### **TABULATED NAKED, AS THE MEANINGS FILE REQUIRED -- AND IT IS THE SMALLEST OF THE THREE "
    u"AT EVERY CELL.** ### **MAX LEFTOVER `1.78e-15`: (DISSONANT-BEYOND) IS NOT TRIGGERED.** *** "
    u"### **THE FERRY'S OWN TAIL CLAUSE WAS REFUSED, AND THE REFUSAL WAS BANKED *BEFORE* THE RUN, "
    u"NOT AFTER THE NUMBERS MADE IT CONVENIENT.** ### The ferry directed that the re-attribution "
    u"carry *\"the true tail (<= 1.158e-14 by theorem)\"*. ### **THE FIRST HALF OF ITS "
    u"RE-ATTRIBUTION IS ADOPTED EXACTLY; THE TAIL CLAUSE CANNOT BE EXECUTED**, on b247's "
    u"DOUBLE-NAME ruling: b250's envelope bounds `sum_{n>N} t(n)`, an ENDPOINT-WEIGHT series, "
    u"while `TrTail` is `sum_{n>=NMODE} tr[n]`, a CORR-WEIGHTED DILATION OVERLAP -- ### **TWO "
    u"FUNCTIONALS OF THE SAME EIGENFUNCTIONS WITH NO DERIVATION IN THE RECORD BETWEEN THEM.** "
    u"### Applying it would have been b247's error committed one act after the act that answered "
    u"it. ### **AND THE MEASUREMENT SETTLES HOW FAR OFF THAT WOULD HAVE BEEN: `TrTail` IS 2.9e12 "
    u"TO 7.0e12 TIMES LARGER THAN THE ENVELOPE.** ### The registered executor doubt -- *\"I expect "
    u"`TrTail` to be ORDERS above 1.158e-14; if it comes out at or below, my doubt is wrong and I "
    u"report it wrong\"* -- ### **WAS RIGHT, BY TWELVE ORDERS.** ### **b250 IS NOT RE-VERDICTED; "
    u"ITS THEOREM IS UNTOUCHED. ### WHAT WAS CORRECTED IS THIS FERRY'S APPLICATION OF IT.** *** "
    u"### **M-2-inf: THE DOSSIER IS OPENED AND *NOT* DECIDED (b237).** ### The question stated: "
    u"### **does `Tr_inf = A + E2` hold as an identity of the objects the two constructions each "
    u"intend -- and if not, WHICH construction is the archimedean `E1`-trace that "
    u"`T + Q = W_inf - W_primes` refers to?** ### **SPECIES: (RULING).** ### Not (READ) -- no owner "
    u"text settles it and b251 looked. ### Not (RESULT) -- ### **NO MEASUREMENT CAN SETTLE WHICH "
    u"OF TWO DEFINITIONS IS THE INTENDED ONE. ### A BENCH NUMBER CAN SAY THEY DISAGREE AND BY HOW "
    u"MUCH; IT CANNOT SAY WHICH IS RIGHT.** ### Three readings are set out (R-I, R-II, R-III) with "
    u"### **NO PREFERENCE EXPRESSED AND NO EVIDENCE DISTINGUISHING THEM.** *** "
    u"### **THE BARS ARE WIDE AND THIS ACT WILL NOT DRESS THAT UP.** ### `TrTail` sits at "
    u"### **43% TO 71% OF THE G-STAB BAR**, so limb 1 holds but ### **THE IDENTIFICATION IS "
    u"*CONSISTENT*, NOT *SHARP*, AND A FIT INSIDE A WIDE BAR IS A WEAKER CLAIM THAN A FIT INSIDE A "
    u"NARROW ONE** -- reporting otherwise would be the crime b229 named. ### **AND THE HARDER "
    u"FACT: THE SPREAD DOES NOT SHRINK MONOTONICALLY WITH `NQ`** (500->700 falls, 700->900 rises, "
    u"900->1100 falls), so ### **b251 DID NOT ESTABLISH THAT THE MODE SUM CONVERGES TO ANYTHING**, "
    u"and the dossier records that as the open item it is. *** "
    u"### **A NUMBER IN THIS ACT'S OWN PROSE WAS WRONG AND THE GATE CAUGHT IT.** ### The share "
    u"range was first written **61.4%-70.0%**; the true minimum is **60.775%**, at `a^2 = 8`. "
    u"### **THE MECHANISM IS WORTH MORE THAN THE ERROR: I TOOK THE RANGE FROM THE RUN'S ROUNDED "
    u"TABLE AND READ THE *LAST ROW* AS THE MINIMUM INSTEAD OF SCANNING THE COLUMN.** ### Gate 8 "
    u"recomputes every headline figure FROM THE ARRAYS rather than from this act's sentences, and "
    u"it failed, and ### **THE FAILURE WAS THE DOCUMENT'S, NOT THE RUN'S -- THE ARRAYS AND THE "
    u"PER-CELL TABLE WERE RIGHT THROUGHOUT.** ### **ONLY THE PROSE SUMMARY WAS WRONG, WHICH IS THE "
    u"MOST DANGEROUS PLACE FOR IT TO BE, BECAUSE THE PROSE IS WHAT GETS QUOTED FORWARD.** ### Now "
    u"stated to three decimals so a future act cannot repeat the rounding that hid it. *** "
    u"### **AND A SECOND SELF-CATCH, BEFORE BANKING: GATE 4's FIRST FORM WAS DECORATIVE.** ### It "
    u"read `(A and B and C and D) or E`, and `and` binds tighter than `or`, so a true `E` carried "
    u"the whole conjunction regardless. ### **A GATE THAT PASSES ON ONE DISJUNCT ASSERTS ONLY THAT "
    u"DISJUNCT.** ### b244 caught a fixture that was the exact negation of its own check; b248's "
    u"gate 2 carried this same `or` shape; ### **THIS IS THE THIRD APPEARANCE OF THE "
    u"DECORATIVE-GATE SPECIES**, and it was rewritten as a pure conjunction with the absence limb "
    u"made explicit. *** "
    u"### **THE TAUTOLOGY CONTROL GOVERNED AND IT COST THE ACT ITS HEADLINE.** ### The "
    u"re-attribution `resid47 = Delta_2real - TrTail` holds to `8.9e-16` -- ### **AND THE "
    u"HASH-GATED MEANINGS FILE DECLARED IT ALGEBRAIC-RESTATEMENT BEFORE THE RUN, SO ITS "
    u"CONFIRMATION IS NOT A FINDING. ### AN IDENTITY THAT CANNOT FAIL CANNOT TESTIFY.** ### Same "
    u"for the accounting line: its content is that **no fourth piece was needed**, not that the "
    u"three were derived. ### **THE ONLY EVIDENCE THIS RUN PRODUCED IS THE *SIZE* QUESTION.** *** "
    u"Gates ### **14 of 14 CLEAN**; term scan CLEAN. ### Meanings banked and hashed FIRST "
    u"(`d5284f9e...4b3c`, 11048 bytes) and the hash re-verified at the gates; ### **G-INDEP IS "
    u"STRUCTURAL, NOT ASSERTED** -- every quantity comes from its OWN owner in `b38_act10`, "
    u"imported as a module, none re-implemented; G-STAB at the registered axes plus exactly one "
    u"refinement. ### **b38's NMODE=10 ROW BANK NAMED AND NOT USED** (b245's trap); ### **b38's "
    u"FOUR-DECIMAL PRINT FLOOR ON `resid47` NAMED BEFORE MEASURING**, per the b249 extension. *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE M-2-inf QUESTION -- a RULING for the author, "
    u"and the dominant term of the shortfall now waits on it.** ### **(2) M-2's finite-place "
    u"address, M-3, M-5 as the remaining engine items.** ### **(3) THE PATENT SESSION, which slots "
    u"here on your word and needs nothing from this act.** *** "
    u"### **THE FORM IS NOT INDICTED. ### NO ACT HAS PRODUCED EVIDENCE AGAINST "
    u"`T + Q = W_inf - W_primes`, AND CITING THIS BRANCH AS ANY WOULD BE A MISREADING.** "
    u"### **M-2-inf IS A NEW ADDRESS INSIDE M-2, NOT A REPLACEMENT FOR IT.** ### M-2, M-3 and M-5 "
    u"stand open and this act closed none. ### **NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE "
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b250: %r" % old_title
    assert NEW_TITLE not in lead, "### b251 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b250)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (IMPOSTER-NAMED), ON ITS ACCOUNTING LIMB",
                 u"IS *ALREADY* A TWO-REALIZATIONS DIFFERENCE",
                 u"60.775% TO 69.995% OF `L - R` AT EVERY CELL",
                 u"TABULATED NAKED, AS THE MEANINGS FILE REQUIRED",
                 u"(DISSONANT-BEYOND) IS NOT TRIGGERED",
                 u"THE REFUSAL WAS BANKED *BEFORE* THE RUN",
                 u"WAS RIGHT, BY TWELVE ORDERS",
                 u"OPENED AND *NOT* DECIDED (b237)",
                 u"*CONSISTENT*, NOT *SHARP*",
                 u"DID NOT ESTABLISH THAT THE MODE SUM CONVERGES",
                 u"THE FAILURE WAS THE DOCUMENT'S, NOT THE RUN'S",
                 u"THIRD APPEARANCE OF THE\nDECORATIVE-GATE SPECIES".replace(u"\n", u" "),
                 u"AN IDENTITY THAT CANNOT FAIL CANNOT TESTIFY",
                 u"THE FORM IS NOT INDICTED",
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
