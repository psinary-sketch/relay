# -*- coding: utf-8 -*-
"""b252_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite.
### b252 is SOLO and owns this write."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE MODE SUM'S LIMIT (b252)"
PRIOR_MARK = u"(b251)"

NEW = (
    u"*** ### **BRANCH (DIVERGES/WANDERS), AT EVERY CELL. ### THE ARCHIMEDEAN MODE SUM DOES NOT "
    u"SETTLE.** ### Measured at extended precision to ### **N = 20 (prolate index 40, "
    u"`mu_20 = 7.162e-80`)**, past the float64 veil, at all six cells, with the quadrature object "
    u"`A + E2` computed beside it from its own owners. ### `S_N` misses the registered "
    u"1%-of-`|S_N|` settling threshold by ### **7.5x to 11.3x.** *** "
    u"### **AND THE THRESHOLD-FREE EVIDENCE, WHICH IS THE REAL ONE:** ### `n * w(n)` RISES AND "
    u"FLATTENS TOWARD A NONZERO CONSTANT AT EVERY CELL -- 1.876, 1.194, 0.949, 0.635, 0.601, "
    u"0.533 -- i.e. ### **`w(n) ~ C/n`, WHOSE SUM DIVERGES LOGARITHMICALLY**, and the log form "
    u"checks against `S_20 - S_10` to about 6%. ### **I SAY THRESHOLD-FREE BECAUSE MY OWN GATE 8 "
    u"FIXTURE MADE THE ALTERNATIVE VISIBLE: THE LAST-THIRD CHANGE IS 7.5% TO 11.3% OF `|S_20|`, SO "
    u"A 12% THRESHOLD WOULD HAVE CALLED EVERY CELL SETTLED.** ### The threshold was fixed in the "
    u"hashed meanings file before any number existed -- ### **AND IT IS STILL NOT THE ACT'S "
    u"PRINCIPAL EVIDENCE. ### `n*w(n)` RISING TO A NONZERO CONSTANT IS INCOMPATIBLE WITH ANY "
    u"CONVERGENT SUM AT ANY TOLERANCE.** *** "
    u"### **AND THE LIMIT IN THE SAME BREATH: A MEASURED DECAY LAW OVER `n = 0..20` IS NOT A "
    u"THEOREM.** ### b242's rule governs -- ### **A MEASURED RATE IS NOT A TAIL BOUND** -- so the "
    u"divergence is the reading the measured form implies, ### **NOT PROVED HERE AND NOT BANKED "
    u"AS PROVED.** *** "
    u"### **THE ONE EXACT FACT, DERIVED FROM SOURCE BEFORE THE INSTRUMENT WAS BUILT: "
    u"`A_n(0) = 1` FOR EVERY `n`.** ### At `u = 0` the overlap is `0.5*||xi_n||^2`, and pin P2's "
    u"half-line norm makes that exactly 1. ### **SO THE INTEGRAND OF `tr[n]` DOES NOT DECAY IN `n` "
    u"AT ALL AT `u = 0`, AND `tr[n]` IS NOT GOVERNED BY `mu_n`, WHICH DOES NOT APPEAR IN IT.** "
    u"### Any expectation that `tr[n]` inherits the eigenvalue's factorial decay (b250's S2) is a "
    u"DOUBLE-NAME and was refused in advance, exactly as b251 refused the envelope. ### The "
    u"instrument reproduces the fact to ### **3.0e-13.** *** "
    u"### **THE FINDING REGISTERED IN ADVANCE AS AN EXPECTED FAILURE, WHICH HAPPENED: b38's "
    u"FLOAT64 EIGENVECTORS FOR `n >= 7` ARE NOISE.** ### Its `tr[n]` collapse by up to **62x** and "
    u"wander non-monotonically (0.0513, 0.0034, 0.0131, 0.0128) while the clean values decay "
    u"smoothly. ### That is b242's `n_last = 6` seen from the other side. ### **G-REPRO WAS SPLIT "
    u"IN TWO SO THIS COULD NOT BE MISTAKEN FOR AN ARITHMETIC ERROR: G-REPRO-A -- this act's "
    u"instrument in b38-EMULATION MODE against b38's float64 for `n <= 6` -- PASSES AT 3.076e-15, "
    u"MACHINE PRECISION.** *** "
    u"### **THE CONSEQUENCE FOR b251, FILED AS A FACT AND NOT AS A RE-VERDICT.** ### b251's "
    u"`TrTail(7)` of `0.0805` at `a^2 = 2` was built from noise; ### **THE CLEAN VALUE OVER THE "
    u"SAME MODES IS 0.801 -- TEN TIMES LARGER -- AND OVER `n = 7..20` IT IS 2.024.** ### **b251's "
    u"BRANCH IS NOT RE-VERDICTED: A BANKED BRANCH IS NOT RE-VERDICTED BECAUSE A LATER ACT EXPLAINS "
    u"IT (b246's RULE). ### THE FACT IS FILED; THE BRANCH STANDS AS BANKED.** ### **AND THE NAME "
    u"`Delta_2real := Tr_inf - A - E2` HAS NO LIMIT TO BE:** b251 computed a PARTIAL SUM at "
    u"`N = 10` and the name presumed a limit the measurement does not find. ### **ANY FUTURE ACT "
    u"QUOTING `Delta_2real` MUST QUOTE ITS `N` WITH IT.** *** "
    u"### **A SECOND SCHEME DIFFERENCE, ALSO NAMED FROM SOURCE BEFORE IT WAS SEEN.** ### "
    u"`trace_modes` runs Gauss-Legendre over the FULL `[-1,1]` while the integrand has been zeroed "
    u"outside `|x| <= 1/lambda` -- ### **A QUADRATURE ACROSS A KINK** -- and interpolates LINEARLY. "
    u"### This act puts its nodes ON the true support with barycentric interpolation; the "
    u"difference over `n <= 6` is `4.3e-04`. ### **A SCHEME DIFFERENCE, REPORTED AS ONE -- NOT AN "
    u"ERROR IN EITHER PARTY, AND NOT A CORRECTION THIS ACT IS ENTITLED TO IMPOSE ON b38's "
    u"RECORD.** *** "
    u"### **M-2-inf: THE DOSSIER IS APPENDED, PREFIX BYTE-FOR-BYTE INTACT, AND STILL NOT DECIDED "
    u"(b237).** ### Its section (5) had asked, in b251's own words, *\"If the mode sum converges to "
    u"something, WHAT?\"* ### **b252 ANSWERS THAT ITEM -- WITH A MEASUREMENT, NOT A DERIVATION, "
    u"AND THE APPENDIX SAYS WHICH.** ### The bearing on the three readings is stated as BEARING: "
    u"### **(R-II) TAKES IT HARDEST -- an object defined as the limit of a sum that does not settle "
    u"is not defined by that limit** -- but that is bearing, not refutation, since a different "
    u"summation could still denote and b252 did not test one. ### **(R-I) IS CONSISTENT WITH IT; "
    u"(R-III) IS UNTOUCHED. ### b252 EXPRESSES NO PREFERENCE.** ### The card is CITATION-SHAPED per "
    u"the pre-banked MEANS, and the ruling requested is unchanged from b251 -- ### **WHAT HAS "
    u"CHANGED IS THAT IT NOW CITES A TABLE.** *** "
    u"### **G-SELF COVERS `n <= 15` AND NOT THE WHOLE RANGE, AND THE ACT SAYS SO RATHER THAN "
    u"LETTING THE GATE'S NAME IMPLY MORE THAN IT CHECKED.** ### dps 120/NQ 120 against dps "
    u"60/NQ 100 agree to `8.5e-16` up to `n = 15` and part at `n = 16` -- ### **THE SAME VEIL ONE "
    u"LEVEL UP: at dps 60 the floor is ~1e-60 and `mu_16` is at it.** ### G-EQ: max "
    u"eigenfunction-equation residual over all 21 modes ### **4.405e-120 -- the vectors are genuine "
    u"eigenvectors, which is the whole difference between this instrument and the float64 one.** "
    u"### The registered target `N = 20` was met and ### **THE AFFORDABILITY CLAUSE DID NOT NEED TO "
    u"BE INVOKED.** *** "
    u"### **THE TWO AXES ARE NOT COMPARABLE, AS A TABLE AND NOT A GUESS:** the quadrature axis "
    u"(`NU` 401 -> 801) moves `S_20` by `3.1e-4` to `1.1e-3`; ### **THE MODE AXIS MOVES IT BY ABOUT "
    u"2.0 BETWEEN `N = 6` AND `N = 20` AND IS STILL MOVING -- THREE ORDERS LARGER.** ### b242's "
    u"finding seen on a different object. *** "
    u"Gates ### **15 of 15 CLEAN ON THE FIRST RUN.** ### Term scan CLEAN, 0 live over 1625 lines. "
    u"### **EVERY CHECK IS A PURE CONJUNCTION -- b251's gate 4 read `(A and ...) or E` and `and` "
    u"binds tighter, so a true `E` carried it; THAT WAS THE THIRD APPEARANCE OF THE DECORATIVE-GATE "
    u"SPECIES AND THIS FILE CONTAINS NO `or` IN ANY CHECK.** ### **AND EVERY NUMPY-VALUED PREDICATE "
    u"IS `bool()`-WRAPPED**, b242's species having REFUSED three of b251's gates. ### **THE "
    u"TAUTOLOGY CONTROL RUNS THE SETTLING TEST ON ARBITRARY SEQUENCES AND REQUIRES IT TO SEPARATE "
    u"THEM** -- harmonic NOT settled, geometric settled -- because a test that passed everything "
    u"would be measuring its own tolerance. ### **PLACE-papers NOT TOUCHED, SO THE HOOK WAS NOT "
    u"EXERCISED AND THE MIRROR NOT REBUILT -- REPORTED EITHER WAY.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE M-2-inf RULING, which now cites a table rather "
    u"than taste.** ### **(2) M-2's finite-place address, M-3, M-5 as the remaining engine items -- "
    u"and the junction piece still waits naked in its own column.** ### **(3) THE PATENT SESSION, "
    u"which slots here on your word and needs nothing from this act.** *** "
    u"### **NO RULING WAS MADE AND NO READING CHOSEN. ### M-2, M-3 AND M-5 STAND OPEN AND THIS ACT "
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
    old_title = tail[:cut]
    rest = tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b251: %r" % old_title
    assert NEW_TITLE not in lead, "### b252 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b251)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"BRANCH (DIVERGES/WANDERS), AT EVERY CELL",
                 u"`w(n) ~ C/n`, WHOSE SUM DIVERGES LOGARITHMICALLY",
                 u"A 12% THRESHOLD WOULD HAVE CALLED EVERY CELL SETTLED",
                 u"A MEASURED DECAY LAW OVER `n = 0..20` IS NOT A\nTHEOREM".replace(u"\n", u" "),
                 u"`A_n(0) = 1` FOR EVERY `n`",
                 u"FLOAT64 EIGENVECTORS FOR `n >= 7` ARE NOISE",
                 u"MACHINE PRECISION",
                 u"THE FACT IS FILED; THE BRANCH STANDS AS BANKED",
                 u"MUST QUOTE ITS `N` WITH IT",
                 u"A QUADRATURE ACROSS A KINK",
                 u"STILL NOT DECIDED",
                 u"COVERS `n <= 15` AND NOT THE WHOLE RANGE",
                 u"NO `or` IN ANY CHECK",
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
