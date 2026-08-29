# -*- coding: utf-8 -*-
"""b255_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite. ### SOLO."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE LIMIT PROFILE (b255)"
PRIOR_MARK = u"(b254)"

NEW = (
    u"*** ### **BRANCH (MIXED), AND THE SPLIT IS THE FINDING.** ### The balance measured along the "
    u"cutoff axis over ### **SIXTEEN CELLS, `a^2 = 2` TO `100`.** ### `|resid(A)|` ### **ALTERNATES "
    u"GROW/SHRINK UP TO `a^2 = 20`, THEN RUNS EIGHT CONSECUTIVE SHRINKS TO `a^2 = 100`** -- "
    u"`1.001813` down to `0.486920`, more than halving across the ladder. ### **(RELAXES) IS NOT "
    u"TAKEN, BECAUSE THE BANKED RULE FORBIDS READING AN OSCILLATING STRETCH AS A RELAXATION WITH AN "
    u"EXCUSE.** *** "
    u"### **THE PRICING RAN FIRST AND KEPT NO BALANCE VALUE.** ### The ferry's rule was *'the "
    u"ladder chosen by AFFORDABILITY, never by what its values do'*, and ### **THE ORDER ON DISK IS "
    u"WHAT MAKES THAT CHECKABLE RATHER THAN ASSERTED** -- pricing, then ladder, then hashed "
    u"meanings, then registration, then run. ### Four walls measured: ### **(W1) THE eps "
    u"`rho`-GRID ENDED AT `a^2 = 12.001` AND FAILED *SILENTLY*** -- `np.interp` clamps to `ee[-1]` "
    u"rather than raising, so ### **EVERY CELL PAST 12 WOULD HAVE CARRIED A WRONG `E2` WITH NO "
    u"ERROR RAISED.** ### Rebuilt to `rho_max = 100.001`, `EPS_NRHO 240 -> 445`. ### **(W2) "
    u"`Theta_q`'s `scaling_matrix` IS DENSE `N = p^(2n)`: `a^2 = 100` -> `N = 4096`, ~22 s; "
    u"`a^2 = 128` -> `N = 16384`, 2.1 GB, `>= 1690 s` FOR `p = 2` ALONE -- REFUSED ON COST, AND THE "
    u"REFUSAL RECORDED BEFORE ANY VALUE EXISTED.** ### The ferry's target was `a^2 ~ 50-100 if "
    u"afforded`; ### **it is afforded and the ladder reaches 100.** *** "
    u"### ### **THE STRUCTURAL FINDING: THE JUNCTION IS A SAWTOOTH LOCKED TO b17's STAIRCASE.** "
    u"### `E2even` falls MONOTONICALLY at all sixteen cells (`1.001813` -> `0.410262`, fifteen "
    u"steps, one sign). ### **THE JUNCTION `(PR \u2212 \u0398_q)` DOES NOT -- IT SAWTOOTHS, AND THE "
    u"TEETH ARE THE STAIRCASE STEPS.** ### **BETWEEN STEPS IT RISES: SIX TRANSITIONS, SIX RISES, NO "
    u"EXCEPTIONS. ### AT STEPS IT FALLS AT SIX OF NINE -- AND ON THE UPPER LADDER (`a^2 >= 20`) AT "
    u"ALL FOUR STEPS, WHILE RISING AT ALL FIVE NON-STEPS.** ### The mechanism, read off the columns "
    u"and not assumed: ### **`PR` RISES SMOOTHLY TOWARD 1 WHILE `\u0398_q` RISES IN JUMPS, GAINING "
    u"A WHOLE LEVEL EACH TIME THE STAIRCASE STEPS -- SO THE JUNCTION WIDENS WHEN ONLY `PR` MOVES "
    u"AND SNAPS SHUT WHEN `\u0398_q` CATCHES UP.** ### That is why the lower ladder oscillates and "
    u"the upper does not. *** "
    u"### **MY REGISTERED EXPECTATION WAS BACKWARDS, AND IT IS REPORTED FIRST.** ### The hashed "
    u"meanings file banked *\"(RELAXES) ON THE LOWER LADDER AND I DO NOT PREDICT THE UPPER.\"* "
    u"### ### **THAT IS THE REVERSE OF WHAT HAPPENED: THE LOWER LADDER IS THE OSCILLATING ONE, AND "
    u"THE UPPER -- THE STRETCH I EXPLICITLY DECLINED TO PREDICT -- IS THE CLEAN ONE.** ### **I "
    u"NAMED THE RIGHT DIRECTION AND THE WRONG STRETCH, AND THE STRETCH WAS THE PART I HAD SIX CELLS "
    u"OF EVIDENCE ABOUT.** ### And the falsifier as banked ### **DID NOT FIRE** -- it asked only "
    u"whether `|residual|` decreases across the new cells, which it does. ### **BUT A FALSIFIER "
    u"THAT DOES NOT FIRE IS NOT A PREDICTION CONFIRMED: MINE WAS WRONG IN ITS CONTENT AND MY "
    u"FALSIFIER WAS TOO COARSE TO CATCH IT, AND BOTH ARE MY FAULT AND NOT THE LADDER'S.** *** "
    u"### **NO SIGN-EVENT -- AND THE REASON IS STRUCTURAL, WHICH IS WORTH MORE THAN THE ABSENCE.** "
    u"### The meanings file registered a sign-event as *\"the outcome I most want to catch\"*, so "
    u"catching it could not look like a discovery made to order. ### **IT DID NOT OCCUR: ALL "
    u"THIRTY-TWO ENTRIES ARE NEGATIVE.** ### And `resid(A) = \u2212(E2even + junction)` with "
    u"### **BOTH TERMS POSITIVE AT EVERY CELL -- A SUM OF TWO POSITIVES CANNOT CROSS ZERO.** "
    u"### `\u0398_q` approaches `PR` from below and never reaches it (`0.928192` against `1.004851` "
    u"at `a^2 = 100`), and the separation snaps shut at each step and re-opens between them -- "
    u"### **A STATEMENT ABOUT THIS LADDER AND NOTHING ELSE.** *** "
    u"### **THE G-REPRO DEBT WAS REGISTERED BEFORE IT WAS PAID, AND PAID.** ### Rebuilding the grid "
    u"changes `E2` for the six banked cells too, so the meanings file fixed a `1e-4` band BEFORE "
    u"the rebuild ran. ### **WORST DEVIATION AGAINST b254: `5.64e-06`, INSIDE THE BAND BY A FACTOR "
    u"OF EIGHTEEN. ### b254 IS NOT RE-VERDICTED (b246's RULE).** *** "
    u"### ### **AND THE DISCIPLINE THIS ACT EXISTS UNDER, KEPT: b242 GOVERNS -- 'A MEASURED RATE IS "
    u"NOT A TAIL BOUND.' ### NO FIT WAS MADE, NO SLOPE BANKED, NOTHING EXTRAPOLATED. ### THE WORD "
    u"'LIMIT' IS IN THIS ACT'S TITLE AND IN NONE OF ITS CONCLUSIONS.** ### b15 governs the reach: "
    u"a finite ladder decides no limit, and ### **b14's DOUBLE LIMIT IS UNTOUCHED IN ITS FIRST "
    u"COORDINATE -- `S4 = (2,3,5)` IS FIXED, SO `a^2 = 49` ACTIVATES NO NEW PRIME AND `7` NEVER "
    u"ENTERS. ### THIS LADDER MEASURES POWERS OF A FIXED PRIME SET, NOT A GROWING PLACE SET.** "
    u"### **R-III STILL GOVERNS THE VOCABULARY: NO DEFICIT LANGUAGE.** *** "
    u"Gates ### **14 of 14 CLEAN.** ### Term scan CLEAN ### **on the second pass: the first found "
    u"TWO LIVE USES OF A BANNED STEM IN THIS ACT'S OWN BANK**, and they were replaced rather than "
    u"excepted. ### **THE TAUTOLOGY CONTROL HAD TO SEPARATE TWO THINGS THAT LOOK ALIKE: the "
    u"residual's NEGATIVITY *is* forced once both terms are positive (restatement, and the bank "
    u"says so rather than counting it), while the STAIRCASE CORRELATION is not.** ### Two gates "
    u"failed first and both were ### **MY OWN MEANINGLESS NEGATIVE CONJUNCTS -- demanding the "
    u"ABSENCE of phrases the files legitimately carry. ### NEGATION DOES NOT MAKE A VACUOUS "
    u"CONJUNCT MEANINGFUL, AND THAT IS THE DECORATIVE-GATE DEFECT WEARING A MINUS SIGN.** "
    u"### **PLACE-papers NOT TOUCHED, SO THE HOOK WAS NOT EXERCISED AND THE MIRROR NOT REBUILT -- "
    u"REPORTED EITHER WAY.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) M-2's FINITE-PLACE ADDRESS AND THE AGGREGATION -- "
    u"RULE Q's aggregation is STILL UNSTATED, and this act has now given the junction a "
    u"sixteen-cell profile it did not have.** ### **(2) M-3 (class richness).** ### **(3) M-5 (the "
    u"missing transport).** ### **(4) `W-ORD-CN-LAW`** -- derive the `C/n` form from `A_n(0) = 1` "
    u"and the weight's source form. ### **(5) THE PATENT SESSION, which slots here on your word and "
    u"needs nothing from this act.** *** "
    u"### **THE IDENTITY IS CLAIMED NEITHER REFUTED NOR PROVED. ### NO REALIZATION WAS CHOSEN -- "
    u"(B) RODE BESIDE (A) AT EVERY CELL UNDER b253's QUOTED-N LAW. ### M-2, M-3, M-4 AND M-5 STAND "
    u"OPEN AND THIS ACT CLOSED NONE. ### THE FORM IS NOT INDICTED. ### NOTHING ABOUT h2 BEYOND THE "
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
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b254: %r" % old_title
    assert NEW_TITLE not in lead, "### b255 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b254)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (MIXED), AND THE SPLIT IS THE FINDING",
                 u"THE PRICING RAN FIRST AND KEPT NO BALANCE VALUE",
                 u"AND FAILED *SILENTLY*",
                 u"REFUSED ON COST",
                 u"SAWTOOTH LOCKED TO b17's STAIRCASE",
                 u"SIX TRANSITIONS, SIX RISES, NO EXCEPTIONS",
                 u"THAT IS THE REVERSE OF WHAT HAPPENED",
                 u"A FALSIFIER\nTHAT DOES NOT FIRE IS NOT A PREDICTION CONFIRMED".replace(
                     u"\n", u" "),
                 u"A SUM OF TWO POSITIVES CANNOT CROSS ZERO",
                 u"INSIDE THE BAND BY A FACTOR OF EIGHTEEN",
                 u"NOTHING EXTRAPOLATED",
                 u"7` NEVER ENTERS",
                 u"TWO LIVE USES OF A BANNED STEM",
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
