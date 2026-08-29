# -*- coding: utf-8 -*-
"""b246_definitions.py -- THE DEFINITIONS AND THE TESTS. ### EMITTED BEFORE ANY COMPUTATION.

### THIS SCRIPT IMPORTS NO INSTRUMENT and reads NO bank. ### It writes words, definitions and
### pass-bands. ### A gate proves it could not have computed, by running the same test against
### the RUN script, where it fails.
"""
import io
import time

OUT = r"D:\relay\data\b246_definitions.txt"

TEXT = u"""\
====================================================================================================
b246 -- THE TWO TAILS. ### THE DEFINITIONS AND THE TESTS.
### BANKED BEFORE ANY COMPUTATION. ### WRITTEN {stamp} (local). ### CONCURRENCY: SOLO.
====================================================================================================

### THE CEILING, FIRST, AND GOVERNING EVERY LINE BELOW:
###   b14: "a FINITE-PLACE-SET OBJECT AT A FINITE MODEL CUTOFF -- the complete roster is the
###         double limit (all places, cutoff to infinity) and STAYS OPEN whatever this act shows."
###   b15: "A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL."
### ### THE REGISTER SENTENCE, QUOTED UNCHANGED: "RH reduced to a single located clause,
### ### reduction machine-verified. h2 is the clause." ### h2 STANDS EXACTLY WHERE THE DEPOSIT
### ### LEFT IT. ### NOTHING DEPOSITS.

### ### SCOPE: ### **b245's BRANCH IS NOT REVISED.** ### A banked rule is not re-verdicted
### ### because a later act explains it. ### **THIS IS A NEW QUESTION WITH ITS OWN REGISTRATION**,
### ### no face-off is run and no column is recomputed.

====================================================================================================
(0) ### WHAT THIS FILE IS AND IS NOT. ### DISCLOSED, AS EVERY ACT SINCE b241 HAS DISCLOSED IT.
====================================================================================================
### ### **THE EXECUTOR HAS READ THE BANKED PER-MODE NUMBERS BEFORE WRITING THIS FILE.** ### b242's
### ### per-mode table, b37's sector columns and b38's rows are all banked, and this seat read
### ### them at content as the ferry's EXECUTION line orders ("owners read at content first").
### ### **SO THE BANDS BELOW ARE DERIVED FROM BANKED VALUES, NOT SIGHT-UNSEEN**, and where a band
### ### comes from a number the derivation is SHOWN rather than asserted.
### ### **AND ONE THING WAS NOTICED WHILE READING AND IS REGISTERED HERE AS A TEST RATHER THAN
### ### REPORTED LATER AS A DISCOVERY** -- see T-5. ### A finding that arrives before the
### ### registration belongs IN the registration.
### ### **WHAT IS GENUINELY UNDECIDED: whether the two terms of b245's shortfall are two names for
### ### one object.** ### No act has computed the tails by parity from per-mode data, and the
### ### tests below can each fail.

====================================================================================================
(A) THE BANKS CONSULTED, WITH THEIR AXES NAMED. ### W-ORD-TE-SPEC HONOURED IN FORM.
====================================================================================================
### ### **b245 FILED THIS WORK-ORDER BECAUSE IT BROKE THE RULE: a cross-check against a bank must
### ### name the axes the bank was computed at, and REFUSE if they differ from the run's.** ### It
### ### is not built as a tool; it is honoured here in form, and the run PRINTS every axis and
### ### HALTS on a mismatch it can detect.
###   **b242's per-mode bank** (`data/b242_axis_points.json`, key `trunc|<cell>`):
###     NQ = 700 · NMODE_CAP = 11 · NTERM = 11 · EPS_NQ = 700 · EPS_NG = 400 · EPS_NRHO = 240 ·
###     NU_HALF = 401 · place set S4 = {{inf,2,3,5}} · atlas NV = 4001.
###     Fields: `tr` (11 per-mode trace terms), `E2n` (11 per-mode eps terms), `E2full`,
###     `Dm` (the odd eps mask), `A`.
###   **b38's bank** (`data/b38_2026-08-18.txt`): NQ = 700, ### **NMODE = 10** (TRIPLE's middle
###     entry) · EPS_NQ = 700 · NU_HALF = 401 · S4. ### `resid47` printed to FOUR decimals,
###     `D_dictated` to SIX. ### **THE NMODE MISMATCH AGAINST K1's SEVEN IS THE EXACT TRAP b245
###     FELL INTO AND IT IS NAMED HERE BEFORE IT CAN BE FALLEN INTO AGAIN.**
###   **b37's bank** (`data/b37_2026-08-18.txt`): EPS_NQ = 700 · NU_HALF = 401 · S3 and S4;
###     ### **NO TRACE IS COMPUTED IN b37 AT ALL** -- it substitutes at content. ### Columns
###     `E2`, `E2even`, `E2odd`, `Thq`, printed to SIX decimals.
###   **THE MASK CERTIFICATES:** b38 `max|sum_n eps_n - eps_full| = 8.88e-16 PASS`;
###     b37 `max|eps_even + eps_odd - eps_full| = 4.44e-16 PASS`.
###     ### **THESE ARE WHAT LICENSE SPLITTING THE eps SERIES BY PARITY AT ALL.**
### ### **THE RULE THIS ACT ADOPTS FOR ITSELF: every quantity compared is computed from b242's
### ### per-mode arrays at ONE stated mode range, and any comparison to b38's or b37's printed
### ### rows is labelled with BOTH axes and its tolerance set to the coarser bank's floor.**

====================================================================================================
(B) THE DEFINITIONS. ### WRITTEN BEFORE ANY NUMBER IS COMPUTED FROM THEM.
====================================================================================================
### Let `tr[n]` and `E2n[n]`, `n = 0..10`, be b242's banked per-mode arrays at the axes above, and
### let ### **K = 7** be RULE MODES K1's realized mode count (modes 0..6).

### ### **THE PRIMARY READING (R1) -- THE FERRY'S LITERAL WORDS, "the ... remainder of the eps/mode
### ### series BEYOND THE K1 REALIZATION":**
###     `TAIL_even(R1) := sum of tr[n] over n >= K with n EVEN`
###     `TAIL_odd(R1)  := sum of tr[n] over n >= K with n ODD`
### ### **(R1) IS THE PRIMARY AND THE VERDICT IS READ OFF IT.** ### Fixed here so that no reading
### ### can be promoted after its numbers are seen.

### ### TWO ALTERNATE READINGS, REGISTERED NOW **SO THE ONE-OBJECT HYPOTHESIS GETS ITS BEST SHOT**
### ### AND NOT SO THAT A FLATTERING ONE CAN BE CHOSEN LATER:
###     **(R2) the eps-series tail beyond K:** `sum of E2n[n] over n >= K` by parity.
###     **(R3) the FULL eps sectors (not "beyond"):** `E2even := sum E2n[n] over n EVEN`,
###           `E2odd := sum E2n[n] over n ODD`. ### This is sec 17's own sector split, and
###           `E2odd` IS `Delta_-` by sec 19's row.
### ### **ALL THREE ARE COMPUTED AND ALL THREE ARE PRINTED, WHATEVER THEY SAY.**

### ### **`D_dict` COMPUTED INDEPENDENTLY, FROM ITS TWO OWNERS AT MATCHED AXES:**
###     `D_dict_owner := (Theta_q - PR) + (Delta_- - 2*E2full)`   -- sec 20(a), and the formula
###     both `b37_act9.py:169` and `b38_act10.py:188` print.
### ### **AND THE SECOND OWNER, WHICH b241 (4.5) FOUND IS A DIFFERENT OBJECT UNDER THE SAME NAME:**
###     `Dneg_raw := sum of tr[n] over n ODD` -- `b36_act8.py:172`, the RAW ODD-TRACE SLICE.
### ### **b241's FINDING, QUOTED: "DIFFERENT OBJECTS, SAME NAME, ONE CORPUS."** ### sec 19's row
### ### fixes the DEFINITION in favour of the eps-mask series, and b240/b244 bound it that way.
### ### **THIS ACT COMPUTES BOTH AND PRINTS BOTH.** ### The ferry's phrase "(raw odd slice -
### ### masked odd series)" is computed as `Dneg_raw - Delta_-` and reported under its own name
### ### ### **`SECTOR_SPLIT_DIFF`**, because it is NOT equal to `D_dict_owner` and calling it
### ### ### `D_dict` would be the double-name species this programme has already been bitten by.

====================================================================================================
(C) THE TESTS, WITH PASS-BANDS, EACH REQUIRED TO FAIL ON ARBITRARY TUPLES.
====================================================================================================
### **THE FLOOR: `FLOOR := 5e-5`** -- b38's own rounding floor, because its bank prints `resid47`
### to FOUR decimals and nothing finer is readable from it. ### Registered here, not chosen later.

### **T-1 IDENTITY:** `|D_dict_owner - (-TAIL_odd)| <= FLOOR` at every cell, under the primary
###   reading (R1). ### **PASS-BAND: FLOOR.** ### Also computed and printed under (R2) and (R3).
###   ### CAN FAIL: the two are computed from disjoint parts of the banked arrays.
### **T-2 RECOMPOSITION:** `|(resid47 + D_dict_owner) - (TAIL_even + TAIL_odd)| <= FLOOR` at every
###   cell under (R1), where `resid47` is computed from b242's arrays at ### **K = 7 modes** (NOT
###   read from b38's row, whose NMODE is 10 -- ### **W-ORD-TE-SPEC**). ### CAN FAIL.
### **T-3 THE RATIO -- THE ONE-MECHANISM SIGNATURE:**
###   `(TAIL_even + TAIL_odd)/TAIL_even` must lie in ### **[1.673, 1.785]** at every cell -- the
###   band b245 measured for `(L-R)/resid47` and banked. ### **PASS-BAND: that band exactly, NOT
###   widened.** ### CAN FAIL, and it is the sharpest of the four: it asks whether ONE series'
###   parity split reproduces the shortfall's measured ratio.
### **T-4 CELL-PROFILE:** the ratio `TAIL_odd/TAIL_even` must be MONOTONE in `a^2` across the six
###   cells and vary by no more than a factor of ### **1.5** (max/min), matching the 8.4% spread
###   discipline b245 found for its own ratio. ### CAN FAIL.
### **T-5 -- THE EXECUTOR'S OWN, NOTICED WHILE READING AND REGISTERED RATHER THAN SAVED:**
###   while reading b242's arrays this seat computed, at `a^2 = 2` ONLY,
###     `Tr(7 modes) - E2full = 1.990275`  against  `-A = 1.990528`  -- ### **AGREEING TO 2.5e-4**,
###   which would make `resid47 = Tr - A - E2full` approximately `-2A`.
###   ### **REGISTERED TEST: `|resid47 + 2*A| <= 1e-3` at EVERY cell** -- the band is the a^2 = 2
###   observation widened fourfold, fixed here. ### **IT WAS SEEN AT ONE CELL AND IS TESTED AT
###   SIX; FIVE OF THE SIX ARE GENUINELY UNTESTED.** ### CAN FAIL, and I expect it to fail at the
###   larger cells, because nothing I know makes it a law.

### ### **THE TAUTOLOGY CONTROL GOVERNS ALL FIVE.** ### Any identity that passes on arbitrary
### ### tuples is ### **ALGEBRAIC-RESTATEMENT AND CARRIES NO WEIGHT**, and the harness
### ### demonstrates the status of each on random data rather than asserting it.
### ### **ONE IS DECLARED A RESTATEMENT IN ADVANCE, BEFORE ITS NUMBERS EXIST:**
### ### `resid47 + D_dict_owner = L - R` is an ALGEBRAIC RESTATEMENT (b245 established it and the
### ### harness re-demonstrates it). ### **T-2 IS NOT THAT IDENTITY** -- its right-hand side comes
### ### from the per-mode arrays by parity, which is a different construction and can disagree.

====================================================================================================
(D) THE BRANCHES. ### FIXED HERE, IN THESE WORDS.
====================================================================================================
### **(ONE OBJECT)** -- T-1, T-2, T-3 and T-4 ALL within their bands under the PRIMARY reading (R1).
###   ### MEANS: the shortfall is filed as ### **THE MODE TAIL -- ONE OBJECT, TWO PARITY NAMES**;
###   M-4 restated as the single unpaid theorem covering BOTH terms, and the sentence
###   ### **"paying M-4 pays the whole bench shortfall"** enters ### **at the grade this act
###   supports and no higher** -- a bench measurement over six finite cells, not a theorem.
### **(TWO OBJECTS)** -- any of T-1..T-4 fails beyond its band under (R1).
###   ### MEANS: ### **AT FULL PROMINENCE**, and ### **THE TWO TERMS STAY SEPARATELY OWNED.**
###   ### M-4 covers `resid47` and NOT the other term, and no sentence about paying M-4 paying the
###   whole shortfall may be written.
### **(MIXED)** -- the primary reading fails but an ALTERNATE reading passes all four.
###   ### MEANS: the question is REAL but the corpus's own words do not fix which series is meant;
###   ### **ROUTED with both readings quoted, and NOTHING CHOSEN.**
### **(HALT)** -- an axis mismatch the run can detect, or a mask certificate absent.

### ### **BOTH SEATS' EXPECTATIONS, REGISTERED BEFORE THE COMPUTATION:**
### ###   **THE NAVIGATOR'S, QUOTED FROM THE FERRY: ### (ONE OBJECT).**
### ###   **THE EXECUTOR'S: ### (TWO OBJECTS), AND I EXPECT IT TO FAIL WIDE, NOT NARROWLY.**
### ### MY REASONING, REGISTERED SO IT CAN BE WRONG: ### b242 measured the eps per-mode series
### ### **CONVERGED BY MODE 6** (its increments fall to 1e-8 and then to the float floor) while the
### ### trace series was still at 0.257 at mode 6. ### **THE TWO SERIES DO NOT HAVE COMPARABLE
### ### TAILS**, so a parity split of either is unlikely to reproduce a shortfall of order 4 to 7.
### ### **IF THE NUMBERS SAY OTHERWISE, THIS FILE IS THE RECORD THAT I WAS WRONG, AND THE
### ### NAVIGATOR WAS RIGHT.**

====================================================================================================
(E) WHAT NO BRANCH OF THIS ACT MAY DO.
====================================================================================================
### Revise b245's branch. ### Run a face-off or recompute a column. ### Move h2 or the register
### sentence. ### Move any asset's grade. ### Pay or close M-4, M-2, M-3 or M-5. ### Write the
### sentence "paying M-4 pays the whole bench shortfall" on any branch but (ONE OBJECT), and even
### there only at bench grade. ### Promote an alternate reading to primary. ### Deposit anything.
### ### THE CEILING IN THE HEADER GOVERNS ALL OF IT.
====================================================================================================
"""


def main():
    txt = TEXT.format(stamp=time.strftime("%Y-%m-%dT%H:%M:%S"))
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(txt)
    print("banked: %s" % OUT)
    print("bytes : %d" % len(txt.encode("utf-8")))


if __name__ == "__main__":
    main()
