# -*- coding: utf-8 -*-
"""b253_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite. ### SOLO."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE M-2\u221e RULING EXECUTED (b253)"
PRIOR_MARK = u"(b252)"

NEW = (
    u"*** ### **THE ARCHIMEDEAN OBJECT NOW DENOTES ONE CONSTRUCTION BY RULING-WITH-A-TABLE.** "
    u"### The author's `RULE M-2\u221e: Q1` is executed: ### **the QUADRATURE construction "
    u"(`left_side`'s one-axis integral, in which NO mode index appears) is the archimedean object "
    u"the identity's left column denotes**; the per-cell realization of the ruled C2+D1 binding is "
    u"RE-BOUND to it; and the mode sum (`trace_modes`) is ### **DEMOTED TO A TRUNCATION "
    u"DIAGNOSTIC** ### under the standing law *'every quoted partial sum carries its N and its "
    u"precision'*. ### **THE DEFINITION DOES NOT MOVE: C2, D1, RULE Q O1 AND RULE MODES K1 ALL "
    u"STAND AS RULED. ### ONLY THE PER-CELL REALIZATION'S BINDING MOVED.** *** "
    u"### **THE RE-BINDING IS DERIVED FROM THE OWNERS' OWN LINES AND SHOWN, NOT ASSERTED.** "
    u"### From `b36_act8.py:184` `resid47 = Tr_full \u2212 (A + E2)`, i.e. (i) `Tr_full = A + E2 + "
    u"resid47`; with the ruled binding (ii) `T.value := Tr_full + E2 \u2212 \u0394\u208b`, "
    u"substituting construction for construction gives ### **(iii) `T.value := A + E2 \u2212 "
    u"\u0394\u208b`.** ### The combination is UNCHANGED; only which construction realizes the "
    u"archimedean trace has moved. *** "
    u"### ### **AND THE COST IS DISCLOSED IN THE EXECUTOR'S OWN VOICE, BECAUSE THE FERRY'S "
    u"DISCLOSURE DID NOT NAME IT ALL: `T.value^OLD \u2212 T.value^NEW = E2 + resid47`.** ### **THE "
    u"RE-BINDING REMOVES `resid47` *AND ONE `E2` TERM*, because the old assembly carried `E2` "
    u"TWICE** -- once in the combination, once inside `Tr_full`'s comparison against `A + E2`. "
    u"### The ferry disclosed *\"~61-70% of the measured shortfall\"*, which names `resid47` alone. "
    u"### **THE REGISTRATION BANKED THE DUTY TO CHECK THIS *BEFORE* THE RE-BINDING WAS WRITTEN, "
    u"SO FINDING IT COULD NOT LOOK LIKE A CONCESSION MADE AFTER THE FACT.** ### In the shortfall's "
    u"algebra: OLD `L \u2212 R = resid47 + 2*E2 \u2212 \u0394\u208b + (PR \u2212 \u0398_q)` -- "
    u"exactly b251's measured decomposition -- and NEW `L \u2212 R = E2 \u2212 \u0394\u208b + "
    u"(PR \u2212 \u0398_q)`. ### **THE SIZE OF THE REMAINDER IS NOT COMPUTED: THAT IS A FACE-OFF, "
    u"AND b253 RAN NONE. ### IT IS b254's.** *** "
    u"### ### **THE R-LABEL MATCH IS HALTED AS AMBIGUOUS AND ROUTED TO THE AUTHOR.** ### Q1's last "
    u"clause required the match and provided the halt, and the halt is taken. ### **BY WORDING Q1 "
    u"IS R-I** -- *\"THE QUADRATURE IS THE OBJECT\"*, almost verbatim. ### **BY CONTENT IT IS NOT: "
    u"Q1 DEMOTES THE MODE SUM TO A *DIAGNOSTIC*, NOT TO AN *APPROXIMATION*, AND R-I's OWN "
    u"CONSEQUENT IS THE APPROXIMATION READING -- WHICH b252 REFUTED** (the mode sum does not "
    u"settle; `\u0394_2real := Tr_\u221e \u2212 A \u2212 E2` has no limit to be, and a quantity "
    u"with no limit is not a convergence error). ### **AND BY CONSEQUENCE Q1 IS R-III: the ferry's "
    u"own *\"removes ... BY DEFINITION\"* is R-III's *\"THE SHORTFALL IS AN ARTEFACT OF THE "
    u"PAIRING RATHER THAN A DEFICIT\"*.** ### ### **WHAT TURNS ON IT: UNDER R-I EVERY NUMBER b254 "
    u"MEASURES IS A DEFICIT STILL OWED; UNDER R-III THE SAME NUMBERS ARE THE RESIDUE OF A PAIRING "
    u"ERROR AND THE 61-70% WAS NEVER OWED AT ALL. ### THE TWO READINGS ASSIGN OPPOSITE MEANINGS TO "
    u"b254's ENTIRE TABLE.** ### b237 governs -- an executor does not settle a definition. *** "
    u"### **THE HALT IS NOT A BLANKET REFUSAL AND THE RECORD SHOWS IT: R-II IS EXCLUDED CLEANLY "
    u"AND WITHOUT DOUBT** (Q1 names the quadrature; R-II names the mode sum). ### **AND THE "
    u"AMBIGUITY WAS REGISTERED BEFORE THE DOSSIER'S TEXT WAS WEIGHED** -- registration section (D) "
    u"banked *\"I EXPECT THE MATCH TO BE AMBIGUOUS AND I SAY SO BEFORE WEIGHING IT\"*, with both "
    u"grounds. ### **AND THE HALT HALTS THE MATCH ONLY: the re-binding is derived from Q1's OWN "
    u"WORDS and the owners' lines and DOES NOT CONSUME THE R-LABEL, so every other component "
    u"executed in full.** *** "
    u"### **THE QUOTED-N LAW NOW STANDS, AND IT BITES THE RECORD IMMEDIATELY.** ### Any quoted "
    u"`Tr_full`, `TrN`, `S_N`, `tr[n]`, `\u0394_2real` or `resid47` must carry its mode count `N` "
    u"and its precision, or it is ### **UNGRADED**. ### b251's `\u0394_2real` is quotable only as "
    u"`(N = 11, float64 modes, suspect above n = 6)`. ### **b251's BRANCH IS NOT RE-VERDICTED "
    u"(b246): THE LAW GOVERNS FUTURE QUOTATION, NOT PAST VERDICTS.** *** "
    u"### **THREE WORK-ORDERS FILED, NONE RUN, AND NONE REPORTED AS DISCHARGED** -- b148 built a "
    u"guard and b178 breached again with it present and unused, so ### **BUILDING A THING IS NOT "
    u"DISCHARGING IT.** ### **`W-ORD-B38-HIGHMODE`** -- sweep the corpus for citations of float64 "
    u"`tr[n]` at `n >= 7` and annotate each `SUSPECT-BY-b252` with its `N`; annotate, ### **NOT "
    u"DELETE AND NOT RECOMPUTE**, and no banked branch re-verdicted. ### Known candidates named "
    u"(b38's own `TRIPLE`, b245, b251) and ### **EXPLICITLY NOT CLAIMED COMPLETE.** ### **THE "
    u"QUOTED-N TERM-SCAN EXTENSION** -- a `QUOTED-N` verdict class, ### **WITH FIXTURES IN BOTH "
    u"POLARITIES, BECAUSE ONE POLARITY IS NOT A FIXTURE.** ### **`W-ORD-CN-LAW`** -- derive the "
    u"`C/n` form from `A_n(0) = 1` and the weight's source form; ### **b252's WIDTH HEURISTIC WAS "
    u"REGISTERED AS A HEURISTIC AND BEING RIGHT DID NOT PROMOTE IT.** *** "
    u"### **b254 -- THE FOURTH FACE-OFF -- IS NAMED WITH ITS PRECONDITIONS AND NOT RUN.** ### "
    u"Expected composition, stated AS AN EXPECTATION: arrangement terms plus the naked junction. "
    u"### Preconditions: **(i)** the halted R-label -- ### **b254 CAN MEASURE BUT CANNOT REPORT "
    u"WHAT ITS TABLE MEANS UNTIL THE LABEL IS RULED**; **(ii)** RULE Q's aggregation is STILL "
    u"UNSTATED, so ### **b254 MUST NOT TREAT MEASURABILITY AS STATEDNESS**; **(iii)** the QUOTED-N "
    u"law applies to every number it quotes; **(iv)** ### **`\u0394\u208b`'s OWN REALIZATION IS "
    u"ALSO A MODE SUM, AND WHETHER Q1 TOUCHES IT IS *NOT DECIDED HERE* AND IS FLAGGED OPEN -- AN "
    u"EXECUTOR WHO SILENTLY EXTENDED Q1 TO `\u0394\u208b` WOULD BE RULING.** *** "
    u"Gates ### **14 of 14 CLEAN** (second run). ### **THREE GATES FAILED FIRST AND ALL THREE WERE "
    u"DEFECTS IN THE GATES, NOT IN THE ARTEFACTS, AND ARE DISCLOSED:** one looked for a phrase in "
    u"the wrong file; one sliced a character off a filename because `.strip()` ate a porcelain "
    u"status space; and ### **ONE MATCHED `left_side` INSIDE A STRING LITERAL THAT QUOTED AN "
    u"OWNER'S NAME AS PROSE -- b248's SPECIES IN A NEW GUISE (b248 MATCHED INSIDE A COMMENT; THIS "
    u"MATCHED INSIDE DATA).** ### **THE FIX TESTED WHAT THE RULE MEANS RATHER THAN WEAKENING IT: a "
    u"filing act MAY quote an owner's name -- the ferry requires it -- but MAY NOT IMPORT OR CALL "
    u"ONE.** ### Term scan CLEAN, 0 live over 942 lines. ### **File E: DOCSTRING ONLY -- "
    u"comment-stripped HEAD against work gives 19 code lines both sides, IDENTICAL, and the "
    u"ORIGINAL C2+D1 BINDING SENTENCE STAYS VISIBLE.** ### CORRESPONDENCE row 94 written by the "
    u"committed tool with its cells as ### **PYTHON LITERALS IN A FILE, NEVER SHELL ARGUMENTS** "
    u"(b158), six cells, no blanks, read back. ### **PLACE-papers NOT TOUCHED, SO THE HOOK WAS NOT "
    u"EXERCISED AND THE MIRROR NOT REBUILT -- REPORTED EITHER WAY.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE HALTED R-LABEL -- one ruling, and b254 waits on "
    u"it for its MEANING though not for its measurement.** ### **(2) b254 THE FOURTH FACE-OFF, "
    u"with the imposter gone and the junction piece naked.** ### **(3) M-2's finite-place address, "
    u"M-3, M-5.** ### **(4) THE PATENT SESSION, which slots here on your word and needs nothing "
    u"from this act.** *** "
    u"### **Q1 IS DEFINITIONAL ONLY AND NO ANALYTIC CLAIM WAS PROMOTED: b252's DIVERGENCE REMAINS "
    u"A BENCH READING. ### NO FACE-OFF RAN. ### M-2, M-3, M-4 AND M-5 STAND OPEN AND THIS ACT "
    u"CLOSED NONE. ### THE FORM IS NOT INDICTED. ### NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE "
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
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b252: %r" % old_title
    assert NEW_TITLE not in lead, "### b253 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b252)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"ONLY THE PER-CELL REALIZATION'S BINDING MOVED",
                 u"DERIVED FROM THE OWNERS' OWN LINES AND SHOWN, NOT ASSERTED",
                 u"AND ONE `E2` TERM",
                 u"THE R-LABEL MATCH IS HALTED AS AMBIGUOUS",
                 u"R-II IS EXCLUDED CLEANLY",
                 u"THE HALT HALTS THE MATCH ONLY",
                 u"THE LAW GOVERNS FUTURE QUOTATION, NOT PAST VERDICTS",
                 u"NONE REPORTED AS DISCHARGED",
                 u"WOULD BE RULING",
                 u"MATCHED INSIDE DATA",
                 u"19 code lines both sides, IDENTICAL",
                 u"NO FACE-OFF RAN",
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
    sys.stdout.write("  new title            : %s\n" % NEW_TITLE.encode('ascii', 'replace').decode())
    sys.stdout.write("  lead length          : %d -> %d\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  prior content kept   : %s\n" % ("YES" if rest in back else "NO"))
    sys.stdout.write("  read-back identical  : %s\n" % ("YES" if ok else "NO"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
