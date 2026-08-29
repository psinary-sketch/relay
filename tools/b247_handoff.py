# -*- coding: utf-8 -*-
"""b247_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"

PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH

NEW_TITLE = u"THE M-4 STATEMENT AND ROUTE (b247)"
PRIOR_MARK = u"(b246)"

NEW = (
    u"*** ### **THE STATEMENT IS WRITABLE FROM OWNERS EXCEPT AT ONE PLACE, AND THAT PLACE IS THE "
    u"THEOREM.** ### Clause (i) requires `lambda(n) -> 0` ### **AT A STATED RATE**, and ### **NO "
    u"OWNER IN THIS CORPUS STATES ONE.** ### Lemma F.1 certifies a TRUNCATION (eleven terms uniform "
    u"to 1e-11), ### **NOT A TAIL AND NOT A RATE**; sec 17 NAMES the debt rather than discharging "
    u"it; and the bench cannot fill it because `lambda(n)^2` reaches the float64 floor at `n = 7`, "
    u"so every point past it is arithmetic noise. ### **THE STATEMENT HALTS AT CLAUSE (i)'s RATE "
    u"AND THE MISSING SENTENCE IS NAMED IN FULL.** *** "
    u"### **EVERY CONSTITUENT OF `t(n)` IS UNFOLDED TO ITS OWNER (the E0 gate):** `lambda(n)^2 = "
    u"mu_{2n}`, the EVEN-INDEXED concentration eigenvalue of the time-and-band limiting operator on "
    u"`L^2[-1,1]` at ### **FIXED c = 2*pi** (Slepian-Pollak 1961, pin P1); `xi_n(1) = "
    u"sqrt(2)*psi_{2n}(1)` under the half-line norm (pin P2), the endpoint ### **NOT extrapolated** "
    u"but obtained from the eigenfunction equation itself. *** "
    u"### **A-1 IS (SAME OBJECT):** act 15's `1/(1-lambda_n^2)` block inverses and `t(n)`'s "
    u"denominator unfold to the same index set, the same eigenvalue and the same expression -- "
    u"### **BUT AN IDENTIFICATION IS NOT AN ESTIMATE.** *** "
    u"### **A-2 IS (DOUBLE-NAME), AND THE DISCRIMINATOR WAS REGISTERED BEFORE THE NUMBER WAS "
    u"SEEN.** ### b212 measured `|alpha_odd|/(pi*Lambda) = 1.0` at every odd eigenvalue -- "
    u"`|alpha|` is ### **CONSTANT IN THE INDEX** -- so if `xi_n(1)` were the same object it would "
    u"be constant too. ### **MEASURED: `xi_n(1)` RUNS 0.026180 TO 4.994344, max/min = 190.77**, "
    u"against a forced constant of 0.945442 if the hypothesis held. ### The difference is quoted "
    u"rather than summarised: ### **TWO DIFFERENT DOMAINS (`[-1,1]` against `[1,infinity)`), TWO "
    u"DIFFERENT ENDPOINTS OF THEM (right against left), AND TWO DIFFERENT NORMALIZATIONS.** "
    u"### **WHAT IS NOT CLAIMED: that no relation exists** -- a transform between the exterior and "
    u"interior problems would be a RESULT owed. *** "
    u"### **IMP-3 IS REFUSED.** ### The family the corpus has seen is the `c -> infinity` one and "
    u"### **OUR `c` IS FIXED AT 2*pi** -- an asymptotic in `c` cannot be applied at a fixed `c`. "
    u"### **NO PRIMARY WAS READ AT CONTENT IN THIS ACT AND NONE EXISTS IN THIS REPOSITORY**; b130's "
    u"own grade on the single quotation the corpus holds is SECONDARY-VERIFIED with the primary NOT "
    u"read. ### b130's precedent governs: ### **\"A CITATION IS NOT A LICENCE; APPLICABILITY IS A "
    u"SEPARATE READ.\"** ### **AND THE HONEST QUALIFIER: A FIXED-c DECAY THEOREM IS A DIFFERENT "
    u"THEOREM FROM THE c -> infinity ONE, AND REFUSING THE SECOND DOES NOT REFUTE THE FIRST** -- "
    u"the fixed-c family was ### **NOT REACHED**, and stays NAVIGATOR-OPEN as b130 filed it. *** "
    u"### **AND A FINDING THE ACT DID NOT GO LOOKING FOR: CLAUSE (ii)'s FIRST DISJUNCT IS FALSE ON "
    u"THE CERTIFIED RANGE.** ### `xi_n(1)^2` is NOT bounded there -- it GROWS from 6.854e-04 to "
    u"24.94 across `n = 0..6`, ### **A FACTOR OF ABOUT 36,000** -- so only the \"growth dominated\" "
    u"form of (ii) is live and ### **THE THEOREM MUST BE STATED THE HARDER WAY.** ### Why it still "
    u"converges on that range: the `lambda^2` decay (~3 orders per mode) OUTRUNS the `xi^2` growth "
    u"(<1 order per mode) -- ### **AN OBSERVATION OVER SEVEN POINTS, NOT A RATE AND NOT A "
    u"THEOREM.** *** "
    u"### **THE ROUTE, PRICED IN FIVE STEPS:** S1 `lambda(n) in (0,1)` -- **IMP owed** (the primary "
    u"is not read here); ### **S2 A DECAY RATE AT FIXED c -- IMP owed OR RESULT owed, AND IT IS THE "
    u"BINDING STEP: NOTHING IN THE CORPUS SUPPLIES IT TODAY**; S3 a bound on `xi_n(1)^2` -- RESULT "
    u"owed, and ### **THE NAIVE ROUTE CLOSES NOTHING**: the endpoint construction is INVERSE in "
    u"`lambda_n`, so the obvious estimate gives a bound that does not decay at all; S4 the assembly "
    u"-- RESULT owed; S5 the cut the envelope is stated at -- ### **RULING owed**, seven (K1) or "
    u"eleven (F.1), and an executor does not settle it. *** "
    u"### **THE DERIVATION ACT IS SPECIFIED AND NOT RUN, FILED FOR THE AUTHOR'S CONFIRMATION** -- "
    u"components, gates, grade target ### **DERIVES-ON-IMPORTS AT CONTENT with a Core shadow where "
    u"finite-decidable, AND NOT HIGHER**, and halt conditions fixed in advance including "
    u"### **HALT IF `xi_n(1)` IS IDENTIFIED WITH THE ARC'S `alpha` ANYWHERE IN IT.** *** "
    u"### **THE EXECUTOR'S OWN EXPECTATION WAS PARTLY WRONG AND THE CORRECTION IS THIS ACT'S OWN:** "
    u"I registered that the statement would be writable whole EXCEPT for (iii)'s envelope. "
    u"### **THE HALT IS NOT AT (iii) BUT AT (i)'s RATE** -- (iii) is a consequence, and without a "
    u"rate there is nothing to compute an envelope FROM. ### **I NAMED THE WRONG CLAUSE AND THE "
    u"READING CORRECTED ME.** *** "
    u"Gates 14 of 14 PASS, CLEAN on the third run. ### **RUN 1 FAILED ON A CONJUNCT THAT ASSERTED "
    u"NOTHING** -- a leftover malformed pattern tested for falsity, which the matcher resolved to "
    u"True. ### **THE GATE WAS RIGHT TO FAIL: A CONJUNCT THAT ASSERTS NOTHING IS A CONJUNCT THAT "
    u"CAN ASSERT ANYTHING.** ### **TWO BANNED STEMS WERE WRITTEN IN THIS ACT'S OWN VOICE AND THE "
    u"SCAN CAUGHT BOTH**; repairing the registration made it younger than the reads file, and "
    u"### **THE ORDERING WAS RESTORED HONESTLY RATHER THAN BACK-DATED** -- the reads tool is "
    u"deterministic, it was re-run, and the re-run changed ### **ZERO LINES**. ### **NO MTIME WAS "
    u"TOUCHED.** ### Term scans CLEAN over 909 lines. *** "
    u"### **NEW: `W-ORD-FIXED-C-DECAY`** -- locate and quote, from a REAL PRIMARY, a decay statement "
    u"for the concentration eigenvalues at FIXED `c`, and check its hypotheses against `Q` at "
    u"`c = 2*pi`. ### **FILED, NOT RUN.** ### **b248 IS NAMED AS NEXT: THE SECOND OBJECT** -- the "
    u"`E2` arrangement read and the junction piece's per-cell split, ### **QUOTATION-ONLY**, with "
    u"the standing clause at registration. *** "
    u"### **M-4 NOW HAS A STATEMENT WITH A NAMED HOLE RATHER THAN A NAME ALONE, AND THAT IS THE "
    u"WHOLE OF THIS ACT'S ADVANCE.** ### **NO DERIVATION WAS PERFORMED. M-2..M-5 STAND OPEN AND "
    u"M-4 IS NOT PAID, NOT PAYABLE TODAY, AND NOT NEARLY SO.** ### **THE AUTHOR'S FORK AT THIS "
    u"STOP: THE PATENT SESSION, WHICH SLOTS HERE ON YOUR WORD AND NEEDS NOTHING FROM THIS ACT; THE "
    u"M-4 DERIVATION ACT, AWAITING YOUR CONFIRMATION; AND b248.** ### PLACE-papers, the loom and "
    u"the mirror were NOT touched, so the hook did not run and no mirror rebuild was required. "
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
    assert old_title.endswith(PRIOR_MARK), "### derived prior title is not b246: %r" % old_title
    assert NEW_TITLE not in lead, "### b247 already in the lead -- refusing to double-demote"

    demoted = u" *(prior: b246)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted

    assert rest in new_lead and old_title in new_lead
    assert new_lead.endswith(rest)
    for must in (u"HALTS AT CLAUSE (i)'s RATE", u"A-1 IS (SAME OBJECT)",
                 u"A-2 IS (DOUBLE-NAME)", u"IMP-3 IS REFUSED",
                 u"REFUSING THE SECOND DOES NOT REFUTE THE FIRST",
                 u"FIRST DISJUNCT IS FALSE", u"BINDING STEP",
                 u"I NAMED THE WRONG CLAUSE", u"W-ORD-FIXED-C-DECAY",
                 u"b248 IS NAMED AS NEXT", u"NOTHING DEPOSITS"):
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
