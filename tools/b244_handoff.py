# -*- coding: utf-8 -*-
"""b244_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.

### THE DEMOTED TITLE IS DERIVED FROM THE FILE'S OWN LEAD LINE, never typed from memory, and
### EVERY assertion runs BEFORE the write. ### A title typed from memory is how a headline gets
### dropped quietly.
### ### NOTE ON THE PRIOR MARK: b242 and b243 ran PARALLEL and neither touched HANDOFF, per
### ### their own headers. ### SO THE LEAD DEMOTES b241, NOT b243, AND THIS ACT CARRIES BOTH
### ### PARALLEL ACTS' FINDINGS INTO THE NEW HEAD ITSELF.
"""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE SERIALIZING CLOSE (b244)"
PRIOR_MARK = u"(b241)"

NEW = (
    u"*** ### **THE THREE-PART RULING IS IN THE RECORD WITH ITS TEXTS, EXECUTED IN THREE "
    u"CORRESPONDENCE ROWS (91, 92, 93) -- ONE PER CLAUSE, SO THAT STRIKING ONE DOES NOT DISTURB "
    u"THE OTHER TWO.** ### **RULE Q (O1):** `Q.value := -Theta_q`, the five owner texts cited BY "
    u"NUMBER in the binding itself. ### **RULE Delta_- (D1):** `T.value := Tr_full + E2 - "
    u"Delta_-`, per sec 19's own row *\"our object's trace = this - Delta_-(g)\"* and act 8's "
    u"`RIGHT = (Tr_full + E2 - Dneg) - Thq`, the only place in the corpus where the combination "
    u"is written as EXECUTABLE CODE. ### **RULE MODES (K1):** the definition stays Lemma F.1's "
    u"eleven modes; the realization reports the SEVEN computable plus **a tail term in its bar**. "
    u"### **A RULING, NOT A DERIVATION** -- b241 ROUTED the Q-orientation and chose nothing, and "
    u"FILED Delta_-'s sign and executed nothing. ### **THE AUTHOR RULED.** *** "
    u"### **NO CODE MOVED, AND IT WAS PROVED RATHER THAN ASSERTED:** every comment and docstring "
    u"stripped from File E and from its HEAD blob -- ### **19 LINES BOTH SIDES, IDENTICAL**, the "
    u"relation unmoved at `T.value + Q.value = W.wInf - W.wPrimes`; 76 insertions and 2 deletions, "
    u"### **BOTH DELETIONS INSIDE DOCSTRINGS**, the original `+ Delta_-` quoted in place. ### **AND "
    u"THE PROFILE WAS RE-PRINTED, NOT INFERRED:** `lake env lean` from the declared pin gives "
    u"`[propext, Classical.choice, Quot.sound]`, matching the banked line. *** "
    u"### **THE DISCLOSURE THE STANDING CLAUSE REQUIRES, MADE IN THE RULING'S OWN ROWS: BOTH RULED "
    u"ORIENTATIONS SHRINK THE RESIDUAL** -- `Q.value := -Theta_q` **IS** b240's banked variant V2. "
    u"### What makes the execution lawful is not that the shrink is small: the executor did not "
    u"choose it, the warrant is quotation, and ### **NO ORIENTATION CLOSES THE SEPARATION** (V2 "
    u"stays 19x-24x the combined bar, V3 8.6x-19x, `resid47` untouched by every one). ### **THE "
    u"MOVEMENT IS NOT COMPUTED IN THIS ACT.** *** "
    u"### **b242 -- THE LEFT MODE AXIS: BRANCH (SLOW). `bar_L` HELD, NOT CERTIFIED. M-4 NOT PAID "
    u"AT BENCH.** ### Moving NQ and NMODE apart for the first time: ### **(i) b240's `bar_L` IS "
    u"~94% QUADRATURE AND ~6% TRUNCATION** -- the NQ step alone is 1.7584e-01 against b240's whole "
    u"`|dL|(mode)` of 1.8632e-01, the NMODE step alone 1.2775e-02; ### **the bar named for the mode "
    u"axis was measuring the other one.** ### **(ii) float64 CARRIES SEVEN MODES WHERE LEMMA F.1 "
    u"CERTIFIES ELEVEN**, and `n_last = 6` at EVERY NQ from 500 to 1300 -- ### **more quadrature "
    u"buys no modes.** ### **(iii) the NQ-spread jumps 61x-249x exactly when the first sub-floor "
    u"mode enters the sum.** ### **THE ENVELOPE WAS DERIVED, PRINTED AND REFUSED** -- the ratio is "
    u"rising, the extrapolation is unverifiable IN PRINCIPLE at float64, and **no owner proves the "
    u"trace series converges at all**. ### **DISCLOSED AND ROUTED, NOT DRAWN: `bar_L` MAY BE "
    u"2.4x-2.9x TOO SMALL**, and a bar that is too small makes a separation look MORE significant "
    u"than it is. ### `W-ORD-LEFT-MODE-AXIS` **DISCHARGED**. ### **BOTH SEATS' REGISTERED "
    u"EXPECTATIONS WERE WRONG: a floor hides a tail; it does not bound one.** *** "
    u"### **b243 -- THE IMP-1 ENVELOPE: BRANCH (PROMOTED), INCLUDING THE CELL THAT FAILED b238.** "
    u"### `corr(y) = PHI(y/L)/(L*C^2)` with `PHI := phi*phi` ### **UNIVERSAL AND CELL-INDEPENDENT**, "
    u"so one function computed once and ### **no maximum over the instrument's own `corr` samples "
    u"anywhere.** `||PHI''||_inf = 0.409587060753` stable to twelve digits over a twentyfold "
    u"density range; `C` matches b238's mpmath value to **0.000e+00**. ### **`a^2 = 3` AT NV = 6001 "
    u"CARRIES THE SAME RESIDUAL 2.218e-08 IT ALWAYS DID -- nothing about the measurement changed**; "
    u"the bound did, from 2.133e-08 (three samples of a jittering quantity) to 5.150e-08 derived "
    u"from the bump. ### **K CANNOT HAVE BEEN WIDENED TOWARD A RESIDUAL: no residual enters its "
    u"formula**, which is stronger than a refusal to widen. ### **AND THE BOUND IS LOOSE** -- slack "
    u"2.3x at the tightest cell, 1.5e6 at the loosest, printed so a wide margin cannot read as a "
    u"tight agreement. ### `W-ORD-IMP1-ENVELOPE` **DISCHARGED**; the right-side error spec **FILED** "
    u"on (PROMOTED) only; ### **IMP-1 -> VERIFIED-AT-BENCH, A BENCH GRADE AND NOT A PROOF OF CC's "
    u"EQUATION (1).** *** "
    u"### **THE FIVE-TERM LEDGER AFTER THE RULINGS: TWO RULED, THREE STANDING, NONE PROMOTED.** "
    u"`Delta_-` and `Theta_q` ruled; `2*E2`, `resid47` and `PR` standing. ### **`resid47` IS STILL "
    u"THE LARGEST TERM AT EVERY CELL AND IT GROWS MONOTONICALLY ACROSS THE CERTIFIED RANGE -- it is "
    u"M-4's unpaid size, and M-4 IS NOT PAID.** ### **AND THE SENTENCE THE LEDGER STILL CANNOT SAY: "
    u"NOTHING HERE MAKES THE COLUMNS MEET** -- the two ruled terms together are at most ~1.2 of a "
    u"5.85-8.09 separation, and at `a^2 = 2` they are BOTH ZERO while the separation is its "
    u"largest. *** "
    u"### **NEXT IS b245, THE SECOND FACE-OFF. ### PRECONDITIONS: TWO GREEN, TWO AMBER, ONE OPEN BY "
    u"DESIGN.** ### **(1) the rulings executed -- GREEN.** ### **(2) the right side's bars certified "
    u"-- GREEN**, with the looseness rider carried and not dropped. ### **(3) `bar_L` IN ITS HONEST "
    u"FORM PER K1 -- AMBER, AND IT IS THE REAL ONE: b245 CARRIES A BAR WITH AN UNBOUNDED TERM IN IT "
    u"AND MUST SAY SO IN ITS OWN WORDS**, and the direction is already known and against us. "
    u"### **(4) the banked-meanings discipline -- b245's own first act.** ### **(5) M-2 STILL OPEN, "
    u"and the O1 binding does NOT close it, so b245 REMAINS A PER-CELL STATEMENT AND NOT A "
    u"STRUCTURAL ONE.** ### **THE PATENT SESSION CAN SLOT AT THIS EVENING'S STOP AND NEEDS NOTHING "
    u"FROM b245.** *** "
    u"### **NEW WORK-ORDERS: `W-ORD-MODE-PRECISION` (K3 -- an extended-precision prolate "
    u"eigensolver, priced at ~3.45 decimal digits per further mode, ~130-175 dps for a useful "
    u"tail: A DIFFERENT INSTRUMENT, NOT A REFINEMENT OF THIS ONE); `W-ORD-ORDINATE-CACHE` (b238's "
    u"zeta ordinates lived in a SESSION TEMP DIRECTORY THAT NO LONGER EXISTS -- b243 reproduced its "
    u"whole table from the committed `.npy` and matched every printed digit); `W-ORD-STAGING-GUARD` "
    u"(the b241 `git add -A` breach converted to a named guard -- ### **FILED, NOT BUILT**, because "
    u"b148 built a guard and b178 breached again with it PRESENT, WORKING AND UNUSED).** ### **AND "
    u"`W-ORD-FILE-E-WORKING-COPY-STALE` IS NOW WORSE: relay's working copy was stale by TWO "
    u"amendments at b241 and is NOW STALE BY THREE** -- this act amended the governing residence "
    u"copy and did not sync, because moving a kernel-adjacent file between layers is the residence "
    u"ruling's own *\"never by drift\"*. ### **DISCLOSED AGAIN RATHER THAN QUIETLY WIDENED.** *** "
    u"### **M-2..M-5 STAND OPEN AND THIS ACT CLOSED NONE.** ### The loom was APPENDED to -- one "
    u"hunk, 94 lines, PURE INSERTION, prefix verified byte-for-byte -- and ### **THE `RULE M-1` CARD "
    u"IS ANNOTATED BY THE NEW ENTRY, NOT EDITED**, because the ledger is append-only. ### The "
    u"PLACE-papers seat-boundary hook was EXERCISED and reported: **CLEAN, 0 foreign hits**, and "
    u"the patent seat's material was not staged, not committed and not mentioned. ### **NOTHING WAS "
    u"COMPUTED, COMPARED, OR FACED OFF. NO GRADE WAS PROMOTED BEYOND WHAT ITS OWN ACT EARNED. "
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b241: %r" % old_title
    assert NEW_TITLE not in lead, "### b244 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b241)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    # ### THE HEADLINE ASSERTIONS: each names a thing this act must not lose.
    for must in (u"RULE Q (O1)", u"RULE Delta_- (D1)", u"RULE MODES (K1)",
                 u"A RULING, NOT A DERIVATION", u"19 LINES BOTH SIDES, IDENTICAL",
                 u"BOTH RULED ORIENTATIONS SHRINK THE RESIDUAL",
                 u"NO ORIENTATION CLOSES THE SEPARATION",
                 u"2.4x-2.9x TOO SMALL", u"NEXT IS b245, THE SECOND FACE-OFF",
                 u"TWO GREEN, TWO AMBER, ONE OPEN BY", u"W-ORD-MODE-PRECISION",
                 u"NOW STALE BY THREE", u"NOTHING DEPOSITS"):
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
