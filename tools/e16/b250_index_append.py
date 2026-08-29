# -*- coding: utf-8 -*-
"""b250 -- FILE THE INDEX KEYS. ### APPEND ONLY.

### `m4-derivation` and `s2-decay-route` were queried BEFORE any step ran (registration section
### (F)) and both returned NO KEY. ### They are keyed here, ON FILING, as the registration said.
### ### **AND A THIRD ROW AMENDS THE K1 TAIL ROWS RATHER THAN REWRITING THEM** -- b244's
### precedent, where a second `q-orientation` row was added instead of editing b241's.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = "    't-series': ['the t series', 't(n)', 'sum t(n)', 'partial sums of t'],\n"
KEY_NEW = (
    "    'm4-derivation': ['the m4 derivation', 'm-4 derivation', 'the trace series theorem',\n"
    "                      'convergence of sum t(n)', 'the endpoint identity', 'mercer identity'],\n"
    "    's2-decay-route': ['the s2 decay route', 'eigenvalue decay at fixed c', 'factorial decay',\n"
    "                       'degenerate kernel truncation', 'the zero-import bound'],\n"
)

ROW_ANCHOR = ("     'data/b249_mode_precision.txt; "
              "reports/2026-08-29-the-precision-veil.md'),\n")
ROW_NEW = (
    "    ('m4-derivation', 'b250 (derivation at content)',\n"
    "     'the ONE THEOREM proved at content about the t(n) series, on b247 statement unchanged. '\n"
    "     '### SIX STEPS: S0 the series identity (eps and t(n) are ONE object, by Leibniz from the '\n"
    "     'supplied (85), NOT by resemblance -- b247 double-name hazard answered); S1 lambda_n < 1 '\n"
    "     'strictly (band-limited + compactly supported => entire and vanishing on a set with an '\n"
    "     'accumulation point => zero); S2 the decay; S3a the per-mode endpoint bound; S3b the '\n"
    "     'summed Mercer identity; S4 the envelope',\n"
    "     '### **GRADE: DERIVES-on-IMP, on FOUR named foundational imports (Plancherel, identity '\n"
    "     'theorem, Schmidt/Eckart-Young, Mercer), ALL TRUSTED-AT-CITE and NONE TOOLED** -- the '\n"
    "     'residence tree carries NO MATHLIB, which this act verified twice (a filesystem search, '\n"
    "     'and `Nat.factorial` failing to resolve in the shadow). ### **THE FERRY BEST-CASE TARGET '\n"
    "     'OF ZERO IMPORTS IS NOT MET AND THE SHORTFALL IS FOUR TEXTBOOK THEOREMS, NAMED.** '\n"
    "     '### **S3a HALTS AND IS REPORTED AS HALTING** (W-ORD-XI-PERMODE) -- the per-mode '\n"
    "     'polynomial bound on xi_n(1)^2 needs the Bouwkamp Legendre-coefficient decay, not at '\n"
    "     'content; the two obvious routes go INVERSE in mu_n, as b247 already measured. ### **THE '\n"
    "     'THEOREM ROUTES AROUND S3a; IT DOES NOT ANSWER IT**, and the price is paid at S4, where '\n"
    "     'the MEASUREMENT-FREE envelope bounds the tail by a constant but CANNOT be made to tend '\n"
    "     'to zero. ### **S3b IS THE FIND, AND IT WAS REGISTERED IN ADVANCE AS A PREDICTION ABOUT '\n"
    "     'THE CORPUS ITSELF: sum_n lambda(n)^2 xi_n(1)^2 = c/pi + sin(2c)/(2 pi), which at '\n"
    "     'c = 2 pi is EXACTLY 2 -- RE-DERIVING the corpus OWN banked C0 gate FROM FIRST '\n"
    "     'PRINCIPLES. A pin carried as a MEASURED NUMBER since b35 is now a THEOREM, and its '\n"
    "     'c-dependence is known (the clean 2 needs sin(2c) = 0, NOT generic).** ### IMP-3 '\n"
    "     '(Landau-Widom) is NOT used and is NOT needed; b243 refusal of it at fixed c stands. '\n"
    "     '### **M-4 pays ONE term of the shortfall. M-2, M-3, M-5 untouched. h2 untouched**',\n"
    "     'data/b250_m4_derivation.txt; data/b250_derivation_checks.txt; '\n"
    "     'Core/M4EnvelopeShadow.lean; reports/2026-08-29-the-m4-derivation.md'),\n"
    "    ('s2-decay-route', 'b250 (derivation at content)',\n"
    "     'HOW the concentration eigenvalues are shown to decay at FIXED c = 2 pi. ### Q = A*A '\n"
    "     'with A the finite Fourier transform, so mu_N = s_N(A)^2; Schmidt/Eckart-Young bounds '\n"
    "     's_N by the error of ANY rank-N approximation; and an ANALYTIC kernel admits degenerate '\n"
    "     'approximations at a FACTORIAL rate. ### **TWO ROUTES, AND THE DIFFERENCE BETWEEN THEM '\n"
    "     'IS THE IMPORT LIST**',\n"
    "     '### **ROUTE (a), ZERO SPECIFIC IMPORTS AND THE ONE THE THEOREM RESTS ON**: the '\n"
    "     'EXPONENTIAL OWN TAYLOR SERIES, with the two rank-one factors elementary integrals of '\n"
    "     'powers, giving mu_N <= T(N)^2, T(N) = sum_{m>=N} (2/(2m+1)) c^m/m! at c = 2 pi. '\n"
    "     '### **NO BESSEL FUNCTION, NO LEGENDRE EXPANSION, NO SPECIAL-FUNCTION IDENTITY.** '\n"
    "     '### **THIS ROUTE WAS NOT IN THE REGISTRATION and is reported as an IMPROVEMENT on the '\n"
    "     'registered route, not as it.** ### ROUTE (b), ONE IMPORT (Jacobi-Anger), sharper by '\n"
    "     'many orders, NOT load-bearing. ### **ITS RANGE CONDITION WAS REGISTERED BEFORE '\n"
    "     'COMPUTING: the Bessel factorial bound needs z^2/4 < k + 3/2, i.e. k >= 9 at c = 2 pi. '\n"
    "     'THE COMPUTATION CONFIRMED k >= 9.** ### The join to Lemma F.1 (k = 0..10) OVERLAPS at '\n"
    "     'k = 9,10 rather than merely abutting -- ### **but F.1 is a TRUNCATION certificate, not '\n"
    "     'a tail bound, so the join is of certificates of DIFFERENT SPECIES and the theorem does '\n"
    "     'NOT use the F.1 half.** Route (a) is valid at every N with no range condition. '\n"
    "     '### Both bounds checked against b249 measured mu_N at N = 9..24 as CONTROLS: both hold '\n"
    "     'at every N, LOOSE BY MANY ORDERS, and the slack is printed rather than hidden',\n"
    "     'data/b250_m4_derivation.txt; data/b250_derivation_checks.txt'),\n"
    "    ('rule-modes', 'b250 (AMENDING b244/b245; the earlier rows STAND)',\n"
    "     '### **THE K1 BAR TAIL TERM IS NO LONGER UNBOUNDED.** ### The rows above record that a '\n"
    "     'bar written per RULE MODES K1 carries an UNBOUNDED term and that b245 must say so in '\n"
    "     'its own words. ### **THOSE ROWS ARE NOT REWRITTEN AND WERE TRUE WHEN WRITTEN** '\n"
    "     '(b244 precedent: a second row, not an edit)',\n"
    "     'b250 S4 bounds the tail: sum_{n>N} t(n) <= (2 - S_N)/(1 - beta_N), and at K1 cut '\n"
    "     'N = 6 the bound is **1.158e-14 on ZERO SPECIFIC IMPORTS** against a measured tail of '\n"
    "     '1.116e-14 -- ### **TIGHT TO ABOUT 4%, NOT LOOSE BY ORDERS** (contrast S2 bounds, which '\n"
    "     'are loose by many orders and are printed that way). ### **AND bar_L AMBER DOES NOT '\n"
    "     'CLEAR: it was amber for TWO reasons and only ONE is paid.** The bar still reports SEVEN '\n"
    "     'computable modes against a definition of ELEVEN, a bench-precision fact b249 measured '\n"
    "     'and b250 did NOT remove. ### AMENDED WHEREVER THE RECORD CARRIES IT (three reports), '\n"
    "     'ORIGINALS INTACT -- and the W-UNION (nonArchimedean, unbounded) QUADRANT is a '\n"
    "     '**DIFFERENT OBJECT** and was deliberately NOT amended',\n"
    "     'data/b250_m4_derivation.txt; reports/2026-08-28-first-face-off.md; '\n"
    "     'reports/2026-08-29-the-serializing-close.md; "
    "reports/2026-08-29-the-second-face-off.md'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'m4-derivation'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: m4-derivation, s2-decay-route, and a SECOND rule-modes row (amending).")


if __name__ == "__main__":
    main()
