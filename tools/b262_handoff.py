# -*- coding: utf-8 -*-
"""b262_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE JUNCTION'S DIVERGENCE (b262)"
PRIOR_MARK = u"(b261)"

NEW = (
    u"*** ### ### **J3: THE JUNCTION ### DIVERGES ### ALONG THE CUTOFF LIMIT. ### `PR - Theta_q` "
    u"RUNS `0.374669` AT `a^2 = 1e2` TO `19.708927` AT `a^2 = 1e8`, DOUBLING PER DECADE, OVER "
    u"### ALL PRIMES ### AND NOT OVER `S4`.** ### The growth is carried entirely by the primes "
    u"with `n_p(a) = 1` -- ### **`a < p <= a^2`, FROM WHICH `Theta_q` RECEIVES ### NOTHING ### , "
    u"BECAUSE act 9's `tau_q` VANISHES AT `k = n`.** ### So ### **`Theta_q / PR -> 0` AND "
    u"`J / PR -> 1`: THE JUNCTION IS ASYMPTOTICALLY THE ENTIRE PRIME SIDE.** *** "
    u"### **THE DERIVATION, ON TWO GRADED IMPORTS:** `J(a) = SUM (2 log p / L) psi(u/L) * "
    u"2 sinh(u/2) / (p^{n_p} - 1)`; the `m=1` family is `F_1(a) ~ 2 INT_1^2 a^{s/2} psi(s) ds`, and "
    u"since `psi` VANISHES TO INFINITE ORDER at `s = 2` the saddle sits at `r* = 2/sqrt(L)`, giving "
    u"### **`F_1 ~ 2 a exp(-2 sqrt(log a))` -- GROWTH, SUB-EXPONENTIALLY DAMPED BUT UNBOUNDED.** "
    u"### **I-1 (PNT, Chebyshev): VERIFIED-AT-BENCH on `[1e3, 1e7]`, NOT VERIFIED at `1e2`, "
    u"TRUSTED-AT-CITE above. ### I-2 (saddle-point): TRUSTED-AT-CITE. ### b260's "
    u"`W-ORD-TQ-IDENTIFY` IS INHERITED AS AN OPEN PREMISE.** *** "
    u"### ### **AND THE FINDING THAT LIMITS EVERY EARLIER NUMBER IN THIS CORPUS: ### THE PLACE "
    u"SET `S4 = (2,3,5)` CONTAINS ### ZERO ### PRIMES WITH `n_p = 1` AT EVERY CELL `a^2 >= 25`.** "
    u"### So the family that decides J3 is ### **STRUCTURALLY INVISIBLE** ### to b255's, b260's and "
    u"b261's tables. ### At `a^2 = 100` the bench junction is `0.0767`; ### **THE TRUE ONE IS "
    u"`0.3747` -- NEARLY FIVE TIMES LARGER -- AND THE RATIO WIDENS WITH `a`.** ### **THIS IS NOT A "
    u"DEFECT IN THOSE ACTS: EACH DECLARED ITS FIXED PLACE SET AT EVERY USE AND b255 WROTE THE "
    u"LIMIT IN ITS OWN WORDS. ### THEY DECLARED THE WALL; THIS ACT MEASURES WHAT IS ON THE OTHER "
    u"SIDE OF IT. ### b246's RULE STANDS: NOTHING IS RE-VERDICTED.** *** "
    u"### **WHAT MADE IT ASKABLE AT ALL: b260's CLOSED FORM MAKES THE ENTIRE JUNCTION ### PURE "
    u"ARITHMETIC ### -- no `quotient_basis`, no dense `p^{2n}` matrices, NO COST WALL. ### b255 "
    u"REFUSED `a^2 = 128` ON COST; THIS ACT REACHED `a^2 = 1e8` IN 18 SECONDS**, and it is b260's "
    u"result that bought that, not any new instrument. ### The G-REPRO ran FIRST: the closed form "
    u"reproduces b260's instrument at all sixteen `S4` cells to ### **2.598e-14**. *** "
    u"### ### **THE LABEL, SETTLED BY DEFINITIONS AS THE FERRY DEMANDED: act 9's LEVEL LIMIT "
    u"(FIX `p`, FIX `k`, LET `n -> inf`) AND THIS ACT'S CUTOFF LIMIT (`a^2 -> inf`, EVERY `n_p` "
    u"MOVING AND THE INDEX SET GROWING) ARE ### DISTINCT OBJECTS WITH A STATED RELATION ### -- "
    u"act 9's IS THE RESTRICTION OF THIS ONE TO A FIXED INDEX.** ### **S2 CONCERNS act 9's AND "
    u"### CONFIRMS ### IT; S3 CONCERNS THE NEWLY-ADMITTED TOP LEVELS, WHICH NO LEVEL LIMIT EVER "
    u"SEES. ### BOTH ARE TRUE AND THEY DO NOT MEET: THE AGGREGATE DIVERGES ### PRECISELY BECAUSE "
    u"### THE DOMINANT TERMS ARE THE ONES act 9's LIMIT NEVER REACHES.** ### **A NEW SPECIES IS "
    u"NAMED: THE DOUBLE-*LIMIT* ERROR -- b219's is two OBJECTS under one word, this is two LIMITS, "
    u"and the corpus had no name for it.** *** "
    u"### **S5's MEANING, WITH ITS REACH BOUNDED: IF THE IDENTITY HOLDS ALONG THIS DIRECTION, "
    u"### THE ARCHIMEDEAN SIDE MUST ABSORB A DIVERGENT QUANTITY.** ### That is the finite-place "
    u"shadow's first asymptotic statement. ### **AND FOUR MISREADINGS ARE REFUSED IN THE BANK: it "
    u"is NOT evidence against the identity; NOT a statement about b14's double limit; it does NOT "
    u"move `h2`; and it does NOT say `Theta_q` is the wrong object -- whether it is meant to track "
    u"`PR` is (L-identity), the undecided thing.** *** "
    u"### **THE SHADOW: `Core/JunctionLimitShadow.lean`, VANILLA, `decide` ONLY, ### 11 TERMINALS "
    u"AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED.** ### It compiles the partition, the fixed-level "
    u"decay, ### **the sharp bound `phi < 1/p` cleared of division** ### -- found only by repairing "
    u"a bad control -- and ### **THE SCOPE WALL AS ARITHMETIC: every `S4` prime has `p^2 <= 100` "
    u"while `11 <= 100 < 11^2`.** ### Three FALSE statements of the same shape were REFUSED, lean "
    u"exit 1. ### **IT DOES NOT COMPILE J3.** *** "
    u"### ### **THIS ACT WAS CUT BY AN API DROP MID-REPAIR AND RESUMED ### FROM DISK ### . ### "
    u"FOUR DEFECTS, ALL MINE, ALL DISCLOSED, AND `b262_run.txt` IS PRESERVED UNCHANGED WITH ALL "
    u"FOUR IN IT.** ### (a) the I-1 grade line ### **CONTRADICTED ITSELF INSIDE ONE BANKED FILE** "
    u"(line 95 said VERIFIED, line 161 said NOT VERIFIED); (b) ### **A REFUSAL THAT WAS ASSERTED "
    u"RATHER THAN PRICED** ### -- `1e8` was declared unaffordable by a hard-coded string, and "
    u"pricing showed 18 seconds; ### **A REFUSAL INVENTED TO LOOK DISCIPLINED IS THE SAME CRIME "
    u"WEARING THE OPPOSITE COAT**; (c) ### **THE PRINTED OUTPUT AND THE BANKED FILE DISAGREED** -- "
    u"b261's species again, mutating already-emitted output; (d) ### **A \"DISCRIMINATOR\" THAT WAS "
    u"A THEOREM** -- `phi < 1/2` read 20000/20000 and my annotation said it must fail. ### **THE "
    u"DEFECT PAID FOR ITSELF: RUNNING IT DOWN PRODUCED THE SHARP BOUND `phi < 1/p`.** *** "
    u"### **`W-ORD-NEEDLE-EXTRACT` DISCHARGED, WITH A SHARPER DIAGNOSIS THAN ITS TITLE: \"typed "
    u"needles\" is half the b229/b260/b261 species; ### THE OTHER HALF IS THAT A PURE CONJUNCTION "
    u"OF SIX `contains()` CALLS REPORTS ### ONE BIT ### AND NAMES NO CONJUNCT.** ### `verify_all` "
    u"now names every missing needle. ### **AND THE EVIDENCE IT WORKED: b262's GATES CAME BACK "
    u"12/12 CLEAN ON THE ### FIRST ### RUN -- THE FIRST ACT IN FOUR WITH NO NEEDLE DEFECT.** *** "
    u"### **`W-ORD-REG-HASH` FILED, AND IT IS THIS ACT'S OWN COST: the ferry asked for the "
    u"registration's hash against its banked line and ### THERE WAS NO BANKED LINE ### . ### After "
    u"the drop the only evidence the registration was unchanged was an mtime ordering and a term "
    u"scan -- both real, both weaker. ### A HASH TAKEN AFTERWARDS IS A DESCRIPTION; A HASH BANKED "
    u"AT WRITING TIME IS PROOF.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) J4 -- `eps_even`'s DECAY (`W-ORD-EPS-DECAY`), THE "
    u"ARCHIMEDEAN TWIN: the finite side's shadow diverges, so what does the archimedean side's do? "
    u"### ITS ROUTE NOTE IS WRITTEN: b250's per-mode tools are the assets, b261's OSCILLATION "
    u"FINDING IS ITS FIRST FACT, AND J3's METHOD DOES ### NOT ### TRANSFER -- `eps_even` has no "
    u"closed form and is not arithmetic.** ### **(2) `W-ORD-TQ-IDENTIFY` (b260) -- the premise "
    u"every one of J1/J3's numbers inherits.** ### **(3) `W-ORD-REG-HASH`.** ### **(4) M-2's "
    u"aggregation; M-3; M-5; `W-ORD-CN-LAW`.** ### **(5) THE PATENT LANE, INDEPENDENT: THE TWO "
    u"UPLOADS ARE DONE AND RECEIPTS ARE PENDING -- CARRIED ON THE FERRY'S WORD, NOT VERIFIED BY "
    u"THIS SEAT.** *** "
    u"### **NO GRADE MOVED EXCEPT J3's OWN. ### M-2..M-5 STAND OPEN AND THIS ACT CLOSED NONE. ### "
    u"THE THIRTY-SEVENTH SEAM'S DEBT STANDS, UNPAID AND UNTOUCHED. ### PLACE-papers WAS NOT "
    u"TOUCHED, SO NO MIRROR REBUILD IS OWED AND NONE IS CLAIMED, AND THE HOOK WAS NOT EXERCISED -- "
    u"REPORTED EITHER WAY. ### b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 "
    u"BEYOND THE REGISTER SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]
    assert lead.startswith(PREFIX)
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b261: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b261)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    # ### THE HEADLINE ASSERTIONS, EACH EXTRACTED FROM THE TEXT ABOVE RATHER THAN RECALLED.
    for must in (u"THE JUNCTION ### DIVERGES ### ALONG THE CUTOFF LIMIT",
                 u"Theta_q / PR -> 0",
                 u"exp(-2 sqrt(log a))",
                 u"ZERO ### PRIMES WITH `n_p = 1`",
                 u"STRUCTURALLY INVISIBLE",
                 u"THEY DECLARED THE WALL",
                 u"NOTHING IS RE-VERDICTED",
                 u"PURE ARITHMETIC",
                 u"DISTINCT OBJECTS WITH A STATED RELATION",
                 u"DOUBLE-*LIMIT* ERROR",
                 u"THE ARCHIMEDEAN SIDE MUST ABSORB A DIVERGENT QUANTITY",
                 u"it does NOT move `h2`",
                 u"11 TERMINALS",
                 u"IT DOES NOT COMPILE J3",
                 u"FOUR DEFECTS, ALL MINE, ALL DISCLOSED",
                 u"SAME CRIME WEARING THE OPPOSITE COAT",
                 u"THE DEFECT PAID FOR ITSELF",
                 u"REPORTS ### ONE BIT",
                 u"THE FIRST ACT IN FOUR WITH NO NEEDLE DEFECT",
                 u"W-ORD-REG-HASH",
                 u"RECEIPTS ARE PENDING",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    # ### AND THE PRIOR LEAD'S OWN HEADLINES MUST SURVIVE THE DEMOTION.
    for kept in (u"J2 IS ### REFUTED",
                 u"A REGISTERED FALSIFIER FIRED -- F4",
                 u"J1 IS A THEOREM ON THE OWNERS' DEFINITIONS",
                 u"STATES GRADES, CONFERS NONE",
                 u"LIVE b148 CONDITION"):
        assert kept in new_lead, "### prior headline lost in demotion: %r" % kept
    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]
    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)
    back = io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2]
    ok = (back == new_lead)
    sys.stdout.write("  prior title : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title   : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length : %d -> %d\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  prior kept  : %s\n" % ("YES" if rest in back else "NO"))
    sys.stdout.write("  read-back   : %s\n" % ("YES" if ok else "NO"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
