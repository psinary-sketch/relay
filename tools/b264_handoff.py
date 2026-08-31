# -*- coding: utf-8 -*-
"""b264_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE ARCHIMEDEAN TWIN (b264)"
PRIOR_MARK = u"(b263)"

NEW = (
    u"*** ### ### **`eps_even` DECAYS, AND THE ENVELOPE IS DERIVED.** ### "
    u"### **`|eps_even(x)| <= C_even / x` WITH `C_even = 132.781908429`, EVERY CONSTANT BUILT "
    u"FROM `lambda` ALONE AND NONE MEASURED** -- Cauchy-Schwarz on the `v = rho u` substitution, "
    u"with `INT_0^inf |A_n|^2 = 1/lam^2` by Plancherel through pin P3 and `INT_1^inf |A_n|^2 = "
    u"(1-lam^2)/lam^2` CHECKED at `3.125e-06`. ### **AND THE THING IT SETTLES: `c_n = lam_n/"
    u"sqrt(1-lam_n^2)` CONTAINS NO ENDPOINT VALUE `xi_n(1)^2`, SO THE ENVELOPE ### ROUTES AROUND "
    u"### b250's S3(a) WALL RATHER THAN MEETING IT.** ### `W-ORD-EPS-DECAY` ### DISCHARGED ### . *** "
    u"### **THE SHARP RATE, SEPARATELY GRADED: `x^{3/2} eps_even(x) -> K_even = 1.568231065`, "
    u"`K_n = lam_n^{true} A_n(0)^2 / 2` WITH THE SIGNED `lambda` OF PIN P1** -- and it is confirmed "
    u"### PER MODE ### , not only in the sum: every resolved mode's error HALVES as `x` doubles, "
    u"the `O(1/x)` signature the derivation predicts. ### **F1, F2, F3, F4, F5 DID NOT FIRE.** *** "
    u"### ### **AND THE REACH IS PART OF THE VERDICT, NOT A FOOTNOTE: THE BENCH REACHES "
    u"### `rho <= 100` ### CONVERGED ON THE LADDER AND `rho < 238.4` ON THE CURVE -- ### NOT ### "
    u"THE `x >= 1000` THE REGISTRATION TARGETED. ### A VERDICT QUOTED WITHOUT ITS REACH WOULD BE A "
    u"DIFFERENT AND FALSER SENTENCE.** *** "
    u"### ### **THE ACT WAS SENT TO MEASURE THE `EPS_NG = 400` CEILING AND FOUND THAT CEILING IS "
    u"### NOT THE ONE THAT BINDS ### . ### `EPS_NQ = 700` BINDS FIRST, AT `rho = 238.4`.** ### "
    u"`A_n(x)` integrates `cos(2 pi t x)` over `t in [0,1]`, carrying `x` periods, on the owner's "
    u"FIXED `EPS_NQ` grid: ### **`EPS_NQ/x` NODES PER PERIOD, AND THE FAILURE AT `x ~ 238` IS "
    u"ABOUT THREE.** ### **RAISING `NG` DOES NOT REPAIR IT** -- at `NQ = 700` the inner `A_0(x)` "
    u"is good to `3.4e-08` at `x = 200` and wrong by `9.0e+04` at `x = 300`; `NQ = 3000` moves the "
    u"break to `x ~ 1000`. ### **ON EVERY VALID CELL `NG = 400` DOES NOT DEPART AT ALL "
    u"(`1.895e-09` AT `rho = 100`).** ### **THE HANDOFF'S OWN STANDING SYMPTOM -- *\"a probe gives "
    u"-3.700 where rho = 100 gives 1.358e-03\"* -- IS THIS ARTEFACT, AND ITS CAUSE IS NAMED HERE "
    u"FOR THE FIRST TIME.** ### `W-ORD-NQ-CEILING` FILED, ### **AFFECTED PRIOR ACTS NAMED AND "
    u"NOT RE-VERDICTED**; b247 and b255 are the OPEN sweep and are NOT declared safe either way. *** "
    u"### ### **A SECOND INSTRUMENT FINDING: `qeps_layer` CARRIES `NTERM = 11` AND THE INSTRUMENT "
    u"RESOLVES ### SEVEN ### .** ### Modes 7..10 sit at `~1.5e-8 ~ sqrt(machine epsilon)`, STOP "
    u"decaying where a true prolate spectrum decays super-geometrically, and ### **MOVE UPWARD "
    u"WHEN `NQ` MOVES, WHICH NO EIGENVALUE DOES.** ### The truncation claim is UNHARMED -- they "
    u"enter `C_even` at `7.16e-08` -- ### **BUT THE INSTRUMENT CARRIES FOUR MODES IT CANNOT "
    u"COMPUTE AND NOTHING IN THE RECORD SAID SO.** ### `W-ORD-NTERM-FLOOR` FILED. *** "
    u"### ### **AND THE CORRECTION THIS ACT OWES ITSELF, AT THE PROMINENCE OF THE CLAIM IT "
    u"REPLACES: AN EARLIER PASS READ F6 ACROSS ALL ELEVEN MODES, FOUND `n = 8` AND `n = 10` "
    u"DISAGREEING WITH PIN P1's `(-1)^n`, AND WAS PREPARED TO FILE ### \"PIN P1's SIGN LAW IS NOT "
    u"WHAT THIS INSTRUMENT REALIZES\" ### AS A CORPUS-LEVEL FINDING AT FULL PROMINENCE. ### THAT "
    u"WOULD HAVE BEEN WRONG.** ### Those modes are noise; a sign read off noise is a coin, and the "
    u"two floor modes that DID agree are the same coin landing the other way. ### **PIN P1 IS NOT "
    u"IMPEACHED: IT IS CONFIRMED ON THE SEVEN MODES WHERE IT CAN BE TESTED AND UNTESTED ON THE "
    u"REST, AND UNTESTED IS NOT FAILED.** ### **THE REGISTRATION ### PRE-AUTHORISED ### THAT "
    u"HEADLINE IF F6 FIRED, AND A PRE-AUTHORISED HEADLINE IS EXACTLY THE THING AN ACT WILL REACH "
    u"FOR. ### WHAT STOPPED IT WAS A CHECK THE REGISTRATION DID NOT REQUIRE: ASKING WHETHER THE "
    u"INSTRUMENT CAN COMPUTE WHAT THE FALSIFIER READS.** *** "
    u"### **THREE DEFECTS FOUND IN THIS ACT'S OWN CONTROL FILE, ALL DISCLOSED:** ### **(D1) F1 WAS "
    u"IMPLEMENTED ONE-SIDED WHERE THE SEALED TEXT READS `|eps_even(x)|`** -- the only reason the "
    u"first run printed `F1 DID NOT FIRE` on a ladder carrying `-2.156` against an envelope of "
    u"`0.266`; ### **THAT PRINTED `(DECAYS)` WAS UNSOUND AND IS SUPERSEDED, NOT DEFENDED.** ### "
    u"**(D2) THE REGISTERED `NG` vs `2 NG` TEST CANNOT SEE THE ERROR THAT BINDS** -- both carry the "
    u"same inner `EPS_NQ` error, so they agree while both are wrong; ### **A FALSE PASS, NOT A "
    u"LOOSE ONE**, and five cells were marked converged at `~1e-12` on values wrong by four orders "
    u"of magnitude. ### A second axis was added and a cell now counts as converged only if BOTH "
    u"pass. ### **(D3) A CONTROL WAS RUN ON A VOID CELL.** ### ### **AND THE PATTERN, SAID PLAINLY: "
    u"EVERY ONE OF THE THREE MADE THE ACT LOOK BETTER THAN IT WAS. ### A DEFECT SET THAT LEANS "
    u"ENTIRELY ONE WAY IS ITSELF A FINDING ABOUT THE SEAT THAT WROTE IT.** *** "
    u"### ### **AND A FOURTH, AGAINST THE REGISTRATION RATHER THAN THE RUNNER: CLAUSE (I) WAS "
    u"### INTERNALLY UNSATISFIABLE AS WRITTEN ### .** ### `leggauss(NG)` builds a dense `NG x NG` "
    u"matrix, so `gl(60000)` asks for ### **28.8 GB in one allocation** ### against the same "
    u"clause's `256 MB` cap -- which binds from `NG > 5793`, i.e. from the ### REGISTERED ### "
    u"ladder's own `x = 500` cell. ### **THE LADDER IT REGISTERED COULD NOT BE RUN UNDER THE "
    u"CEILING IT DECLARED.** ### Repaired in this act's OWN runner by panelling the rule into "
    u"panels of `400` -- the owner's own `EPS_NG`, so no new node count is coined -- with the "
    u"total node count, the `NG` law and the `NG` vs `2 NG` test all UNCHANGED. ### `W-ORD-GL-PANEL` "
    u"FILED. *** "
    u"### **S4, THE BEARING, AND IT IS A BEARING: `E2even(a) -> 0` LIKE `1/log a`, NOT A POWER OF "
    u"`a`** -- `E2even * log a` monotone to `1.088` against a derived asymptote `[1.097, 1.859]`, "
    u"the average against `p` PERFORMED and not transported. ### **AGAINST b262's `J`, WHICH "
    u"DIVERGES `0.375 -> 19.709`: ### `E2even` IS NOT THE OBJECT THAT ABSORBS `J`.** ### **SO THIS "
    u"ACT BEARS ### AGAINST ### THE BRANCH ON WHICH THE ARCHIMEDEAN SIDE ABSORBS THE FIRST-LEVEL "
    u"MASS ### THROUGH THIS OBJECT ### .** ### ### **AND THE LIMIT OF THE BEARING IS THE WHOLE "
    u"REASON IT IS ONE: `E2even` IS ### ONE ### ARCHIMEDEAN OBJECT AND IS NOT \"THE ARCHIMEDEAN "
    u"SIDE\". ### THE BRANCH IS NOT DECIDED AND b263's SENTENCE STANDS AS b263 WROTE IT.** ### "
    u"`W-ORD-TQ-IDENTIFY` is OPEN and every `J` number inherits it; the `E2even` column does not. *** "
    u"### **THE REGISTERED EXPECTATIONS, SCORED: TWO CONFIRMED, TWO WRONG.** ### S1 (source and "
    u"period `1`) CONFIRMED at `1.003125`; S4 (`1/log a`) CONFIRMED. ### **S3 WRONG -- `NG = 400` "
    u"fails nowhere the instrument can see. ### S2's SHARP-RATE HALF WRONG, AND WRONG IN ITS "
    u"REASON: it expected the mode sum to MEET b250's wall; the sum is over ELEVEN modes and a "
    u"FINITE sum needs no per-mode bound, and the endpoint that appears is `A_n(0)` and not "
    u"`xi_n(1)`. ### THE WALL RETURNS THE MOMENT THE MODE SUM GOES TO INFINITY, WHICH THIS ACT "
    u"DOES NOT DO.** *** "
    u"### **THE SHADOW: `Core/ArchimedeanTwinShadow.lean`, VANILLA, `decide` ONLY, ### 12 TERMINALS "
    u"AT ZERO AXIOMS, 0 ERRORS, PROFILE PRINTED** (b227's standard). ### Four FALSE statements, one "
    u"of each terminal shape, REFUSED at lean exit 1. ### **AND ITS HEADER STATES WHAT IT MUST NOT "
    u"BE MISREAD AS: THE SIGN-LAW THEOREM IS ARITHMETIC ABOUT `(-1)^n` AND IS ### NOT ### A "
    u"CERTIFICATION THAT THE INSTRUMENT REALIZES PIN P1. ### THAT IS F6's JOB, AND F6 IS MEASURED, "
    u"NOT COMPILED.** ### **IT CARRIES NO PLANCHEREL, NO CAUCHY-SCHWARZ, NO MERCER, NO `eps`, AND "
    u"NO LIMIT.** *** "
    u"### **AND THE TERM SCAN EARNED ITS KEEP AGAIN: ### 10 LIVE USES ### OF THE TWO BANNED STEMS "
    u"IN THIS ACT'S OWN VOICE -- IN THE BANK, THE FILINGS, THE RUNNER ### AND THE GATE FILE ### -- "
    u"ALL CAUGHT AT THE CLOSING SCAN AND CORRECTED BEFORE SHIPPING. ### CLEAN OVER 2792 LINES.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) `W-ORD-NQ-CEILING` -- THE SWEEP FOR EVERY BANKED "
    u"`eps`-INSTRUMENT CELL ABOVE `rho = 238.4`, b247 AND b255 FIRST. ### UNTIL IT RUNS, NO ACT IS "
    u"RE-GRADED AND NO ACT IS DECLARED SAFE.** ### **(2) `W-ORD-TQ-IDENTIFY` (b260) -- the premise "
    u"J1, J3, b263 and this act's `J` column all inherit.** ### **(3) M-2's STATEMENT, THE AUTHOR'S "
    u"TO ADOPT OR ROUTE.** ### **(4) `W-ORD-INDEX-APPEND` -- NOW NINE KEYS ACROSS FOUR ACTS, AND "
    u"THIS ACT'S TWO JOIN THE BACKLOG RATHER THAN JUMPING IT.** ### **(5) M-3; M-5; "
    u"`W-ORD-CN-LAW`; `W-ORD-XI-PERMODE`, WHICH THIS ACT ROUTED AROUND AND DID NOT REMOVE.** ### "
    u"**(6) THE PATENT LANE, INDEPENDENT: RECEIPTS PENDING, CARRIED ON THE FERRY'S WORD AND NOT "
    u"VERIFIED BY THIS SEAT.** *** "
    u"### **NO GRADE MOVED EXCEPT THIS ACT'S TWO ROWS AND `W-ORD-EPS-DECAY`. ### M-2, M-3, M-4, "
    u"M-5 STAND WHERE b263 LEFT THEM AND THIS ACT CLOSED NONE. ### NO PRIOR ACT WAS RE-VERDICTED. "
    u"### NO OWNER INSTRUMENT WAS EDITED. ### PLACE-papers AND THE PATENT TREE WERE NOT TOUCHED. "
    u"### b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 BEYOND THE REGISTER "
    u"SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b263: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b263)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"`eps_even` DECAYS, AND THE ENVELOPE IS DERIVED",
                 u"ROUTES AROUND",
                 u"W-ORD-EPS-DECAY` ### DISCHARGED",
                 u"CONFIRMED\n" if False else u"the `O(1/x)` signature the derivation predicts",
                 u"A VERDICT QUOTED WITHOUT ITS REACH WOULD BE A DIFFERENT AND FALSER SENTENCE",
                 u"NOT THE ONE THAT BINDS",
                 u"RAISING `NG` DOES NOT REPAIR IT",
                 u"W-ORD-NQ-CEILING",
                 u"AFFECTED PRIOR ACTS NAMED AND NOT RE-VERDICTED",
                 u"W-ORD-NTERM-FLOOR",
                 u"THAT WOULD HAVE BEEN WRONG",
                 u"PIN P1 IS NOT IMPEACHED",
                 u"UNTESTED IS NOT FAILED",
                 u"THAT PRINTED `(DECAYS)` WAS UNSOUND AND IS SUPERSEDED, NOT DEFENDED",
                 u"A FALSE PASS, NOT A LOOSE ONE",
                 u"A DEFECT SET THAT LEANS ENTIRELY ONE WAY",
                 u"INTERNALLY UNSATISFIABLE AS WRITTEN",
                 u"W-ORD-GL-PANEL",
                 u"IS NOT THE OBJECT THAT ABSORBS `J`",
                 u"THE BRANCH IS NOT DECIDED",
                 u"TWO CONFIRMED, TWO WRONG",
                 u"12 TERMINALS",
                 u"10 LIVE USES",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"M-2's ADDRESS IS DERIVED",
                 u"THE FIRST-LEVEL PRIMES ARE SILENT",
                 u"OPEN -> SPECIFIED-NOT-STATED",
                 u"THE JUNCTION ### DIVERGES ### ALONG THE CUTOFF LIMIT",
                 u"J2 IS ### REFUTED",
                 u"J1 IS A THEOREM ON THE OWNERS' DEFINITIONS",
                 u"STATES GRADES, CONFERS NONE"):
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
