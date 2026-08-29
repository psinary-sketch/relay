# -*- coding: utf-8 -*-
"""b250_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.
### b250 is SOLO and owns this write."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE M-4 DERIVATION (b250)"
PRIOR_MARK = u"(b248 + b249)"

NEW = (
    u"*** ### **ONE THEOREM, PROVED AT CONTENT. ### GRADE: DERIVES-on-IMP, ON FOUR NAMED "
    u"FOUNDATIONAL IMPORTS.** ### At fixed `c = 2*pi`: the concentration eigenvalues satisfy "
    u"`mu_N = O((c^N/N!)^2)`; the endpoint weights satisfy the EXACT identity "
    u"`sum_n lambda(n)^2 xi_n(1)^2 = 2`; and `sum_n t(n)` CONVERGES with the explicit tail "
    u"envelope `sum_{n>N} t(n) <= (2 - S_N)/(1 - beta_N)`, valid for every `N >= 6`. ### **AND BY "
    u"S0 THE SAME THEOREM IS ABOUT `eps'(1+)`, BECAUSE THE TWO SERIES ARE ONE OBJECT BY "
    u"DERIVATION** -- differentiating the supplied (85) at `rho = 1+`, where the moving lower "
    u"limit is the only surviving Leibniz term. ### **NOT BY RESEMBLANCE: b247's DOUBLE-NAME "
    u"HAZARD IS ANSWERED DEFINITION AGAINST DEFINITION.** *** "
    u"### **THE FERRY'S BEST-CASE TARGET OF ZERO IMPORTS IS NOT MET, AND THE SHORTFALL IS FOUR "
    u"TEXTBOOK THEOREMS, NAMED:** PLANCHEREL, the IDENTITY THEOREM, SCHMIDT/ECKART-YOUNG and "
    u"MERCER -- ### **ALL TRUSTED-AT-CITE AND *NONE* TOOLED.** ### The act LOOKED for the tool and "
    u"there is none: ### **THE RESIDENCE TREE CARRIES NO MATHLIB**, verified twice -- a filesystem "
    u"search, and then `Nat.factorial` failing to resolve when the shadow was compiled. "
    u"### **I REGISTERED S1 AS 'DERIVES, LONGHAND AND ON ZERO IMPORTS' AND THAT PREDICTION WAS "
    u"WRONG IN ITS IMPORT COUNT; IT IS REPORTED WRONG RATHER THAN REDEFINED.** ### **IMP-3 "
    u"(LANDAU-WIDOM) IS NOT USED AND IS NOT NEEDED** -- b243's refusal of it at fixed `c` stands. *** "
    u"### **S3(a) HALTS AND IS REPORTED AS HALTING, THOUGH THE THEOREM SURVIVES BY ANOTHER ROUTE.** "
    u"### The per-mode polynomial bound on `xi_n(1)^2` needs the Bouwkamp Legendre-coefficient "
    u"decay, which is not at content; both obvious routes go ### **INVERSE in `mu_n`**, as b247 "
    u"already measured. ### `W-ORD-XI-PERMODE` FILED. ### **THE HALT WAS REGISTERED IN ADVANCE, "
    u"BEFORE IT HAPPENED** -- a halt predicted in advance is evidence; a halt discovered and then "
    u"declared expected would be nothing. ### **THE THEOREM ROUTES AROUND S3(a); IT DOES NOT ANSWER "
    u"IT, AND THE PRICE IS PAID AT S4**, where the MEASUREMENT-FREE envelope bounds the tail by a "
    u"constant but ### **CANNOT BE MADE TO TEND TO ZERO.** ### **CLAUSE (ii)'s HARDER FORM IS "
    u"THEREFORE *UNNECESSARY*, NOT *PROVEN*, AND THAT DISTINCTION IS NOT BLURRED.** *** "
    u"### **S3(b) IS THE FIND, AND IT WAS REGISTERED IN ADVANCE AS A PREDICTION ABOUT THE CORPUS "
    u"ITSELF.** ### Mercer at the two corners `K(1,1) = c/pi` and `K(1,-1) = sin(2c)/(2 pi)`, with "
    u"the parity `psi_n(-1) = (-1)^n psi_n(1)` DERIVED from the kernel's own symmetry, gives "
    u"### **`sum_n lambda(n)^2 xi_n(1)^2 = c/pi + sin(2c)/(2 pi)`, which at `c = 2*pi` is EXACTLY "
    u"2** -- ### **RE-DERIVING THE CORPUS'S OWN BANKED C0 GATE FROM FIRST PRINCIPLES. A PIN THE "
    u"RECORD HAS CARRIED AS A MEASURED NUMBER SINCE b35 IS NOW A THEOREM.** ### And its "
    u"`c`-dependence is stated rather than hidden: ### **THE CLEAN `2` NEEDS `sin(2c) = 0` AND IS "
    u"NOT GENERIC.** ### The registration fixed the falsifier -- *anything but exactly 2 and the "
    u"route is wrong* -- and the control returns `|sum - 2| = 7.2e-40`. *** "
    u"### **S2's ROUTE IMPROVED ON THE ONE REGISTERED, AND IS REPORTED AS AN IMPROVEMENT RATHER "
    u"THAN AS THE REGISTERED ROUTE.** ### The registered Jacobi-Anger route costs an import; "
    u"### **the EXPONENTIAL'S OWN TAYLOR SERIES costs NONE** and gives the same factorial shape "
    u"with a worse constant, so ### **THE THEOREM RESTS ON THE ZERO-IMPORT BOUND AND JACOBI-ANGER "
    u"ONLY SHARPENS IT.** ### **THE REGISTERED RANGE `k >= 9` WAS BANKED BEFORE ANYTHING WAS "
    u"COMPUTED AND THE COMPUTATION CONFIRMED IT.** ### The join to Lemma F.1 OVERLAPS at `k = 9,10` "
    u"rather than merely abutting -- ### **but F.1 is a TRUNCATION certificate, not a tail bound, "
    u"so the join is of certificates of DIFFERENT SPECIES and the theorem does NOT use the F.1 "
    u"half. ### SAYING SO IS THE POINT.** *** "
    u"### **THE K1 BAR'S 'UNBOUNDED TAIL' IS AMENDED WHEREVER THE RECORD CARRIES IT, ORIGINALS "
    u"INTACT.** ### At K1's cut `N = 6` the tail is bounded by ### **`1.158e-14` ON ZERO SPECIFIC "
    u"IMPORTS**, against a measured tail of `1.116e-14` -- ### **TIGHT TO ABOUT 4%, NOT LOOSE BY "
    u"ORDERS** (contrast S2's bounds, loose by many orders and printed that way). ### **AND THE "
    u"ZERO-IMPORT ENVELOPE'S RANGE CONDITION FIRST HOLDS AT EXACTLY `N = 6`, WHICH IS K1's CUT** -- "
    u"both set by the same `c`, so the record's existing cut needs no adjustment. ### **`bar_L`'s "
    u"AMBER DOES *NOT* CLEAR: it was amber for TWO reasons and only ONE is paid** -- the bar still "
    u"reports SEVEN computable modes against a definition of ELEVEN. ### **AND THE W-UNION "
    u"`(nonArchimedean, unbounded)` QUADRANT IS A DIFFERENT OBJECT AND WAS DELIBERATELY NOT "
    u"AMENDED**; the amending tool matches on FULL SENTENCES, not on the word. *** "
    u"### **A FOURTH CONSECUTIVE PRINT-FLOOR, AND THIS TIME IT WAS THE ACT'S OWN EVALUATION.** "
    u"### The envelope control FAILED at `N = 10, 11` by `7.2e-40` -- ### **EXACTLY the deviation "
    u"of the instrument's 13-term Mercer sum from the exact `2`.** ### At those depths the tail and "
    u"the arithmetic error are the same size, so a finer comparison ### **TESTS THE ARITHMETIC, NOT "
    u"THE THEOREM**; the tolerance is that MEASURED deviation, computed and not chosen, ### **and "
    u"the shadow's polarity controls PROVE it is load-bearing rather than padding.** ### b245 met "
    u"b38's four decimals, b246 floored at 5e-5, b249 met b242's ten digits. ### `W-ORD-TE-SPEC`'s "
    u"pending extension is demonstrated a FOURTH time. *** "
    u"### **TWO GATES FAILED ON THE FIRST RUN AND BOTH ARE DISCLOSED, BECAUSE THEY FAILED IN "
    u"OPPOSITE DIRECTIONS.** ### One caught a REAL DEFECT IN THE ARTEFACT -- the controls file did "
    u"not carry the sentence declaring its measurements non-premises -- and ### **THE ARTEFACT WAS "
    u"FIXED, NOT THE GATE**; re-running the deterministic emitter changed exactly 4 lines and the "
    u"bank was re-written LAST so no mtime was forged (b247's precedent), with ### **ZERO CHANGED "
    u"LINES** proved by diff. ### The other was a DEFECT IN THE GATE: it hunted the substring "
    u"`error` in the axiom profile and matched the profile's own line for the theorem "
    u"`deep_cuts_need_the_evaluation_error`. ### **A LEGITIMATE NAME CONTAINING THE WORD THE GATE "
    u"WAS HUNTING. ### THE GATE WAS NARROWED TO LEAN'S REAL DIAGNOSTIC FORM, NOT RELAXED.** *** "
    u"Gates ### **14 of 14 CLEAN** on the second run. ### Term scan ### **CLEAN, 0 live over 1466 "
    u"lines.** ### The Core shadow compiles vanilla and ### **ITS PROFILE IS PRINTED AND READ, NOT "
    u"INFERRED FROM AN EXIT CODE (b227): 7 of 7 'does not depend on any axioms'** -- and it carries "
    u"### **FOUR POLARITY CONTROLS**, including the two proving the deep cuts genuinely need the "
    u"evaluation-error term and the one proving the range condition excludes `N = 4`. "
    u"### **THE SHADOW DOES NOT CARRY THE THEOREM AND SAYS SO IN ITS OWN HEADER: PLANCHEREL, "
    u"MERCER, THE IDENTITY THEOREM AND THE OPERATOR ARE NOT IN IT, AND A SHADOW THAT APPEARED TO "
    u"CARRY THEM WOULD BE A LIE IN LEAN.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE THIRD FACE-OFF, WITH M-4 NOW PAID AND THE "
    u"JUNCTION PIECE NAKED** -- `resid47` has a theorem behind it, so what remains of the shortfall "
    u"is the archimedean piece on a CONVERGED series plus the junction piece, which names "
    u"### **M-2** again. ### **(2) THE PATENT SESSION, which slots here on your word and needs "
    u"nothing from this act.** ### **(3) M-2, M-3, M-5 AS THE REMAINING ENGINE ITEMS.** *** "
    u"### **M-4 PAYS *ONE TERM* OF THE SHORTFALL AND NOT THE SHORTFALL.** ### b246's ruling that "
    u"M-4 covers `resid47` and nothing else is UNREVISED, and b248's finding that the second object "
    u"is not M-4's is UNREVISED. ### **M-2, M-3 AND M-5 STAND OPEN AND THIS ACT CLOSED NONE.** "
    u"### **NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), \
        "### derived prior title is not b248+b249: %r" % old_title
    assert NEW_TITLE not in lead, "### b250 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b248 + b249)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    # ### THE HEADLINE ASSERTIONS. ### A LEAD THAT LOST ANY OF THESE WOULD BE A DIFFERENT ACT'S.
    for must in (u"GRADE: DERIVES-on-IMP", u"NONE* TOOLED",
                 u"S3(a) HALTS AND IS REPORTED AS HALTING",
                 u"*UNNECESSARY*, NOT *PROVEN*",
                 u"A PIN THE RECORD HAS CARRIED AS A MEASURED NUMBER SINCE b35 IS NOW A THEOREM",
                 u"THE THEOREM RESTS ON THE ZERO-IMPORT BOUND",
                 u"AMBER DOES *NOT* CLEAR",
                 u"A FOURTH CONSECUTIVE PRINT-FLOOR",
                 u"THE ARTEFACT WAS\nFIXED, NOT THE GATE".replace(u"\n", u" "),
                 u"THE GATE WAS NARROWED TO LEAN'S REAL DIAGNOSTIC FORM, NOT RELAXED",
                 u"7 of 7 'does not depend on any axioms'",
                 u"WOULD BE A LIE IN LEAN",
                 u"PAYS *ONE TERM* OF THE SHORTFALL AND NOT THE SHORTFALL",
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
