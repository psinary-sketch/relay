# -*- coding: utf-8 -*-
"""b247 -- THE STATEMENT'S BENCH READS. ### NO DERIVATION IS PERFORMED HERE.

### THIS TOOL MEASURES ONLY WHAT THE ASSET VERDICTS NEED, AND EVERY MEASUREMENT ANSWERS A
### QUESTION REGISTERED BEFORE IT RAN:
###   (1) `lambda(n)^2`, `xi_n(1)^2` and `t(n)` across the certified range and beyond it,
###       the BEYOND clearly labelled UNCERTIFIED (Lemma F.1 stops at eleven);
###   (2) ### **THE A-2 DISCRIMINATOR, REGISTERED IN THE REGISTRATION'S SECTION (B):** b212
###       measured `|alpha|` CONSTANT in the eigenvalue index, so if `xi_n(1)` were the arc's
###       `alpha` it too would be constant. ### **IS IT?**
###   (3) the observed decay of `lambda(n)^2`, as the BENCH CONTROL any imported decay must match.
### ### NOTHING HERE GRADES AN IMPORT OR FILLS A ROUTE STEP.
"""
import io
import math
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import prolate_layer as PL              # noqa: E402
import qeps_layer as Q                  # noqa: E402

BANK = r"D:\relay\data\b247_statement_reads.txt"
NQ = 700
CERT = 11        # ### Lemma F.1's certified count. ### NOT a choice of this act.
PROBE = 18       # ### how far the UNCERTIFIED probe runs. ### Labelled at every use.


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b247 -- THE STATEMENT'S BENCH READS. ### NO DERIVATION IS PERFORMED.")
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("")

    # ---------------------------------------------------------------- the layer
    x, w, mu, psi, psi1 = PL.prolate(NQ)
    lam2_all = mu[0::2]
    xi1_all = math.sqrt(2) * np.abs(psi1[0::2])

    rec("-" * 104)
    rec("(1) THE CONSTITUENTS, FROM THEIR OWNERS' OWN CONSTRUCTION, AT NQ = %d." % NQ)
    rec("### `lambda(n)^2 = mu_{2n}` (pin P1: even index only). ### `xi_n(1) = sqrt(2)*psi_{2n}(1)`")
    rec("### (pin P2, half-line norm), and `psi_n(1)` comes from the EIGENFUNCTION EQUATION")
    rec("### `xi_n(1) = (1/lambda_n) INT K(1,y) xi_n(y) dy` -- NOT extrapolated from the grid.")
    rec("-" * 104)
    rec("  %-4s %16s %16s %16s %14s   %s"
        % ("n", "lambda(n)^2", "xi_n(1)", "t(n)", "t(n)/t(n-1)", "range"))
    prev = None
    for n in range(PROBE):
        l2 = float(lam2_all[n])
        x1 = float(xi1_all[n])
        t = l2 * x1 ** 2 / (1.0 - l2) if l2 < 1.0 else float('inf')
        ratio = ("%.4e" % (t / prev)) if (prev not in (None, 0.0)) else "--"
        tag = "certified" if n < CERT else "### UNCERTIFIED"
        rec("  %-4d %16.9e %16.9f %16.9e %14s   %s" % (n, l2, x1, t, ratio, tag))
        prev = t
    rec("  ### **LEMMA F.1 CERTIFIES ELEVEN TERMS. ### EVERYTHING AT n >= 11 IS A PROBE AND IS")
    rec("  ### LABELLED UNCERTIFIED AT EVERY USE.** ### It is printed because the ROUTE needs to")
    rec("  ### know what the instrument does past its certificate, NOT because it may be cited.")
    rec("")

    # ------------------------------------------------- (2) THE A-2 DISCRIMINATOR
    rec("=" * 104)
    rec("(2) ### THE A-2 DISCRIMINATOR, REGISTERED BEFORE THE NUMBER WAS SEEN.")
    rec("### b212 MEASURED `|alpha_odd| / (pi*Lambda) = 1.0` AT EVERY ODD EIGENVALUE AT EVERY")
    rec("### PARAMETER -- i.e. ### **`|alpha|` IS CONSTANT IN THE EIGENVALUE INDEX.**")
    rec("### ### SO IF `xi_n(1)` WERE THE ARC'S `alpha`, `xi_n(1)` WOULD BE CONSTANT IN `n`.")
    rec("=" * 104)
    cert = xi1_all[:CERT]
    rec("  xi_n(1) over the CERTIFIED range n = 0..%d:" % (CERT - 1))
    rec("    %s" % "  ".join("%.6f" % v for v in cert))
    rec("  min = %.9f   max = %.9f   ### max/min = %.6f"
        % (float(cert.min()), float(cert.max()), float(cert.max() / cert.min())))
    const = (float(cert.max() / cert.min()) < 1.01)
    rec("  ### ### IS `xi_n(1)` CONSTANT IN n (to 1%%)?  ### **%s**" % ("YES" if const else "NO"))
    rec("  ### AND THE VALUE `alpha` WOULD HAVE TO TAKE IF IT WERE: the corpus's two banked pins")
    rec("  ### give `sum_n lambda(n)^2 = 2.237484835` and `sum_n lambda(n)^2 xi_n(1)^2 = 2.0`,")
    rec("  ### so a CONSTANT `xi(1)^2` would be forced to `2/2.237484835 = %.9f`,"
        % (2.0 / 2.237484835))
    rec("  ### i.e. `xi(1) = %.9f`. ### That is the number the constancy hypothesis predicts."
        % math.sqrt(2.0 / 2.237484835))
    rec("  ### MEASURED SPREAD AGAINST IT: min %.6f, max %.6f."
        % (float(cert.min()), float(cert.max())))
    rec("")

    # --------------------------------------------- (3) THE DECAY, AS BENCH CONTROL
    rec("=" * 104)
    rec("(3) ### THE OBSERVED DECAY OF `lambda(n)^2` -- ### THE BENCH CONTROL ANY IMPORTED")
    rec("### DECAY MUST MATCH. ### MEASURED, NOT FITTED, AND NOT A THEOREM.")
    rec("=" * 104)
    rec("  %-4s %18s %16s %16s" % ("n", "lambda(n)^2", "ratio to prev", "log10"))
    prev = None
    for n in range(CERT):
        l2 = float(lam2_all[n])
        r = ("%.4e" % (l2 / prev)) if (prev not in (None, 0.0)) else "--"
        rec("  %-4d %18.9e %16s %16.4f" % (n, l2, r, math.log10(l2) if l2 > 0 else float('nan')))
        prev = l2
    rec("  ### THE RATIOS FALL BY ROUGHLY THREE ORDERS PER MODE ACROSS THE CERTIFIED RANGE, AND")
    rec("  ### ### **THE DECAY IS FASTER THAN GEOMETRIC** -- but that is a DESCRIPTION OF SIX OR")
    rec("  ### ### SEVEN MEASURED POINTS, ### NOT A RATE, AND NOT A THEOREM.")
    rec("  ### **b242's FLOOR APPLIES AND IS RESTATED: `lambda(n)^2` REACHES THE float64 FLOOR AT")
    rec("  ### n = 7, so every point past it is arithmetic noise and CANNOT constrain a rate.**")
    rec("")
    rec("### WHAT THIS RUN DID NOT DO: it derived nothing, graded no import, filled no route step,")
    rec("### and claimed no rate. ### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
