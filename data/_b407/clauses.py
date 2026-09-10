CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 13: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("instrument runs", 0, 0, "runs", "### section (Z)."),
    ("kernel builds run", 0, 0, "builds", "### section (Z): both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)."),
    ("axiom profiles read or inferred", 0, 0, "profiles", "### section (Z)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules", "### (K) BAR 9."),
    ("grades moved or conferred", 0, 0, "grades", "### section (Z)."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("keystone documents edited", 0, 0, "documents", "### section (Z)."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (W): b406 added A2, not b407."),
    ("in-place repairs of any kind", 0, 0, "repairs", "### (K) BAR 12/(W)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 13."),
    ("coordinates added to the row", 0, 0, "coordinates", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("equivalences compiled", 0, 0, "equivalences", "### section (Z)."),
    ("bridges typed", 0, 0, "bridges", "### (K) BAR 6."),
    ("names minted by the seat", 0, 0, "names", "### section (Z)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 12."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("index queries recorded before a mark of NOT AN INSTANCE or ROUTED", 3, 3, "queries",
     "### section (A), each read from the VERDICT LINE under A2."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("tests run on the six sites for an interface", 2, 2, "tests",
     "### section (B): the strict Definition-2.2 test and the loose split test."),
    ("counts of the six reported alone", 0, 0, "counts",
     "### (K) BAR 1: both are printed, never the kinder one."),
    ("transmission coefficients measured, asserted or inferred", 0, 0, "coefficients",
     "### (K) BAR 2."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("prices of a prior act tested by the harder question", 1, 1, "prices", "### section (C)."),
    ("prices protected because they were this seat`s", 0, 0, "prices", "### (K) BAR 7."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("smallest statements named for the repair", 1, 1, "statements", "### section (D)."),
    ("blockers named without saying which kind they are", 0, 0, "blockers", "### (K) BAR 8."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("limbs of (R20) named as the one that would be widened", 1, 1, "limbs", "### section (E)."),
    ("limbs of (R20) actually widened", 0, 0, "limbs", "### (K) BAR 9: ROUTED, not ruled."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("guards built for the stale-record species", 1, 1, "guards", "### section (F)."),
    ("options priced before the choice was made", 2, 2, "options", "### section (F)."),
    ("existing bytes of run_clock.py changed", 0, 0, "bytes", "### (K) BAR 10: purely additive."),
    ("existing callers of run_clock moved", 0, 0, "callers", "### (K) BAR 10."),
    ("fixtures on the new function, both polarities", 2, 2, "fixtures", "### section (F)."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("hypotheses of Theorem 3.1 put to the halt, each quoted", 5, 5, "hypotheses",
     "### section (G)."),
    ("verdicts on the halt", 1, 1, "verdicts", "### section (G): one of three, and named."),
    ("resemblances reported as instances", 0, 0, "resemblances", "### (K) BAR 4."),
    ("rows of FACES_LEDGER.md written", 0, None, "rows",
     "### (K) BAR 5: MEASURED -- nothing is filed unless the verdict is INSTANCE."),

    # ---- ADDITION FOUR ---------------------------------------------------------------------------
    ("questions answered from the documents` own words", 2, 2, "questions", "### section (H)."),
    ("disclaimers read as their converse", 0, 0, "disclaimers", "### (K) BAR 6."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 13, 13, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 12."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 12."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 12: A2, inherited."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms", "(b403)."),
    ("arms demanding a repository state that predates the act", 0, 0, "arms", "(b404)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 12: b405`s zero-byte husk."),
    ("new `relay` tool files", 6, 6, "files", "### (K) BAR 11/(W) KIND 8."),
    ("shared instruments amended", 1, 1, "instruments", "### (W) KIND 9: additively."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### section (W)."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]
