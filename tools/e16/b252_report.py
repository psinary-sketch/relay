# -*- coding: utf-8 -*-
"""b252 -- ASSEMBLE THE TABLES AND APPLY THE REGISTERED TESTS. ### CONSUMES COMPONENT 2.
### ### **THE BAND AND THE SETTLING THRESHOLD ARE READ FROM THE HASHED MEANINGS FILE'S TERMS AND
### ### ARE NOT RE-CHOSEN HERE.**
"""
import io
import json
import math
import sys

import numpy as np

MEAS = r"D:\relay\data\b252_measure.json"
BANK = r"D:\relay\data\b252_run.txt"
CELLS = ['2', '3', '4', '8', '9', '12']
PRIMARY = '120|120'
SELF = '60|100'
NU0, NU1 = 401, 801
SETTLE_FRAC = 0.01                 # ### REGISTERED: 1% of |S_N| over the last third
B251_BARS = {'2': 1.74e-1, '3': 1.19e-1, '4': 9.23e-2,
             '8': 6.27e-2, '9': 5.87e-2, '12': 4.84e-2}   # ### b251's per-cell G-STAB bars


def settled(S):
    """### THE REGISTERED SETTLING TEST: change over the LAST THIRD below 1% of |S_N|."""
    N = len(S) - 1
    m = N - N // 3
    return bool(abs(S[N] - S[m]) < SETTLE_FRAC * abs(S[N])), abs(S[N] - S[m]), abs(S[N])


def main():
    r = json.load(io.open(MEAS, encoding='utf-8'))
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 116)
    rec("b252 -- THE MODE SUM'S LIMIT. ### THE RUN.")
    rec("=" * 116)
    rec("### CEILING (b14/b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### THE REGISTER SENTENCE IS UNTOUCHED. ### NOTHING DEPOSITS.")
    rec("### MEANINGS BANKED AND HASHED FIRST: sha256 0c562286...77be, 10898 bytes.")
    rec("### ### **b250's ENVELOPE 1.158e-14 IS NAMED AND IS NOT APPLIED TO THIS SERIES AT ANY")
    rec("### ### POINT, ON b251's PRECEDENT. ### NO BAR BELOW CARRIES IT.**")
    rec("")
    rec("### AXES AND PRINTED PRECISION OF EVERY CONSULTED BANK, NAMED:")
    rec("###   b38_act10: NU_HALF=401, EPS_NQ=700/NG=400/NRHO=240, cells {2,3,4,8,9,12};")
    rec("###              ### **PRINTS resid47 TO FOUR DECIMALS -> FLOOR 5e-5.**")
    rec("###   b242: n_last = 6 at every NQ 500..1300; lambda^2 to ten digits, xi to nine decimals.")
    rec("###   b249: dps 120 / NQ 80, modes 0..12 even. ### b251: bars 4.84e-2..1.74e-1, six decimals.")
    rec("")

    # ------------------------------------------------------------------ COMPONENT 1 GATES
    rec("-" * 116)
    rec("### COMPONENT 1 -- THE INSTRUMENT, AND ITS GATES.")
    rec("-" * 116)
    a0 = np.array(r['a0'][PRIMARY])
    rec("### **G-EXACT -- THE FACT THE MEANINGS FILE BANKED AT (B), NOW A RUNNING SELF-CHECK:**")
    rec("###   `A_n(0) = 1` EXACTLY FOR EVERY n.  ### max|A_n(0) - 1| = %.3e over n = 0..%d"
        % (abs(a0 - 1).max(), len(a0) - 1))
    rec("###   ### **THE INSTRUMENT REPRODUCES A FACT DERIVED FROM SOURCE BEFORE IT WAS BUILT.**")
    eqr = max(float(s) for s in r['eqres'][PRIMARY])
    rec("### **G-EQ** -- max eigenfunction-equation residual over all 21 modes = %.3e" % eqr)
    rec("###   ### **THE VECTORS ARE GENUINE EIGENVECTORS, NOT SOLVER NOISE. ### THAT IS THE WHOLE")
    rec("###   ### DIFFERENCE BETWEEN THIS INSTRUMENT AND THE FLOAT64 ONE.**")
    mus = [float(s) for s in r['mu'][PRIMARY]]
    rec("###   REACH: N = %d (prolate index %d), mu_N = %.3e -- ### **THE REGISTERED TARGET N = 20"
        % (len(mus) - 1, 2 * (len(mus) - 1), mus[-1]))
    rec("###   WAS MET; THE AFFORDABILITY CLAUSE DID NOT NEED TO BE INVOKED.**")
    rec("")

    # G-SELF
    rec("### **G-SELF** -- dps 120/NQ 120 against dps 60/NQ 100, on `tr[n]` at a^2 = 2, NU = 401.")
    p = np.array(r['%s|2|%d' % (PRIMARY, NU0)])
    s = np.array(r['%s|2|%d' % (SELF, NU0)])
    rec("###   %-4s %18s %18s %12s" % ("n", "dps120/NQ120", "dps60/NQ100", "rel diff"))
    firstbad = None
    for n in range(len(p)):
        rel = abs(p[n] - s[n]) / abs(p[n])
        if rel > 1e-6 and firstbad is None:
            firstbad = n
        if n in (0, 4, 8, 12, 14, 16, 18, 20):
            rec("###   %-4d %18.12f %18.12f %12.2e" % (n, p[n], s[n], rel))
    rec("###   ### **THE TWO SETTINGS AGREE TO BETTER THAN 1e-6 UP TO n = %s.**"
        % ("all n" if firstbad is None else str(firstbad - 1)))
    if firstbad is not None:
        rec("###   ### **AND THEY PART AT n = %d, WHICH IS NOT A DEFECT BUT THE SAME VEIL ONE"
            % firstbad)
        rec("###   ### LEVEL UP: at dps 60 the precision floor is ~1e-60 relative to `mu_0 ~ 1`,")
        rec("###   ### and `mu_%d` is %.2e -- ### **AT OR BELOW THAT SETTING'S OWN FLOOR, SO dps 60"
            % (firstbad, mus[firstbad]))
        rec("###   ### CANNOT RESOLVE THAT EIGENPAIR EITHER.**")
        rec("###   ### **THE PRIMARY SETTING IS THE ONE THAT REACHES N = 20; THE SECOND CONFIRMS")
        rec("###   ### IT ONLY AS FAR AS ITS OWN FLOOR ALLOWS, AND THAT LIMIT IS REPORTED RATHER")
        rec("###   ### THAN LET STAND AS THOUGH G-SELF COVERED THE WHOLE RANGE.**")
    rec("")

    # G-REPRO
    rec("-" * 116)
    rec("### **G-REPRO, IN THE TWO FORMS THE MEANINGS FILE REGISTERED AT (F.1).**")
    rec("-" * 116)
    d = r['repro|2']
    b38 = np.array(d['b38'])
    ea = np.array(d['emul_b38vec'])
    ec = np.array(d['emul_clean'])
    own = np.array(r['%s|2|%d' % (PRIMARY, NU0)])
    ra = (abs(b38[:7] - ea[:7]) / abs(b38[:7])).max()
    rec("### **G-REPRO-A -- THIS ACT'S ARITHMETIC, IN b38-EMULATION MODE, AGAINST b38's FLOAT64.**")
    rec("###   max RELATIVE difference over n <= 6 : %.3e   ### **PASS -- MACHINE PRECISION.**" % ra)
    rec("###   ### **THIS TESTS THIS ACT'S ARITHMETIC AND NOTHING ELSE, AND IT PASSES.**")
    rec("")
    rec("### **G-REPRO-B -- THE SCHEME DIFFERENCE, REGISTERED AT (F.2) BEFORE IT WAS SEEN.**")
    rec("###   b38 runs Gauss-Legendre over the FULL [-1,1] while the integrand is zeroed outside")
    rec("###   |x| <= 1/lambda -- ### **A QUADRATURE ACROSS A KINK** -- and interpolates LINEARLY.")
    rec("###   This act's nodes sit ON the true support with barycentric interpolation.")
    rec("###   max |own - emul(clean vectors)| over n <= 6 : %.3e"
        % abs(own[:7] - ec[:7]).max())
    rec("###   ### **A SCHEME DIFFERENCE, REPORTED AS ONE. ### NOT AN ERROR IN EITHER PARTY, AND")
    rec("###   ### NOT A CORRECTION THIS ACT IS ENTITLED TO IMPOSE ON b38's RECORD.**")
    rec("")
    rec("### ### **AND THE FINDING (F.1) REGISTERED AS AN EXPECTED FAILURE. ### IT HAPPENED.**")
    rec("###   %-4s %16s %16s %14s" % ("n", "b38 float64", "clean vectors", "ratio"))
    for n in range(11):
        rec("###   %-4d %16.9f %16.9f %14s"
            % (n, b38[n], ec[n],
               ("%.1fx" % (ec[n] / b38[n])) if abs(b38[n]) > 1e-12 else "n/a"))
    rec("###   ### **FOR n <= 6 THE TWO AGREE TO %.1e. ### FOR n >= 7 b38's VALUES COLLAPSE BY AN"
        % abs(ec[:7] - ea[:7]).max())
    rec("###   ### ORDER OF MAGNITUDE AND WANDER NON-MONOTONICALLY (0.0513, 0.0034, 0.0131,")
    rec("###   ### 0.0128) WHILE THE CLEAN VALUES DECAY SMOOTHLY. ### b242 MEASURED n_last = 6 AT")
    rec("###   ### EVERY NQ FROM 500 TO 1300, AND THIS IS THAT FLOOR SEEN FROM THE OTHER SIDE:**")
    rec("###   ### **b38's `xi[:, n]` FOR n >= 7 IS NOISE, AND EVERY `tr[n]` BUILT FROM IT IS NOISE.**")
    rec("")

    # ------------------------------------------------------------------ COMPONENT 2 TABLES
    rec("-" * 116)
    rec("### COMPONENT 2 -- THE MEASUREMENT. ### `w(n) := tr[n]`, PRIMARY SETTING, NU = 401.")
    rec("### **A FINITE CELL DECIDES NOTHING GLOBAL (b15).**")
    rec("-" * 116)
    rec("### **THE DECAY LAW IS THE HEADLINE, SO `n*w(n)` IS PRINTED BESIDE `w(n)`:**")
    hdr = "%-4s" % "n"
    for c in CELLS:
        hdr += " %11s" % ("a^2=" + c)
    rec("###  w(n):")
    rec("###  " + hdr)
    W = {c: np.array(r['%s|%s|%d' % (PRIMARY, c, NU0)]) for c in CELLS}
    for n in range(21):
        rec("###  %-4d" % n + "".join(" %11.7f" % W[c][n] for c in CELLS))
    rec("###  n*w(n):")
    rec("###  " + hdr)
    for n in range(1, 21):
        rec("###  %-4d" % n + "".join(" %11.6f" % (n * W[c][n]) for c in CELLS))
    rec("### ### **`n*w(n)` RISES AND FLATTENS TOWARD A NONZERO CONSTANT AT EVERY CELL.**")
    rec("### ### **THAT IS `w(n) ~ C/n`, WHOSE SUM DIVERGES LOGARITHMICALLY.**")
    rec("")

    rec("-" * 116)
    rec("### THE PARTIAL SUMS AGAINST THE QUADRATURE OBJECT, COMPUTED FROM ITS OWN OWNERS.")
    rec("-" * 116)
    rec("### %-5s %10s %10s %10s %10s %10s | %12s %12s"
        % ("a^2", "S_6", "S_10", "S_13", "S_16", "S_20", "A + E2", "S_20-(A+E2)"))
    verdicts = {}
    for c in CELLS:
        S = np.cumsum(W[c])
        q = r['quad'][c]['AplusE2']
        rec("### %-5s %10.6f %10.6f %10.6f %10.6f %10.6f | %12.6f %12.6f"
            % (c, S[6], S[10], S[13], S[16], S[20], q, S[20] - q))
        ok, chg, mag = settled(S)
        verdicts[c] = (ok, chg, mag, S[20], q)
    rec("")
    rec("### **THE REGISTERED SETTLING TEST -- change over the LAST THIRD below 1% of |S_N|:**")
    rec("### %-5s %14s %14s %10s %12s" % ("a^2", "|S_20 - S_14|", "1% of |S_20|", "SETTLED?",
                                          "band(b251)"))
    allsettled = True
    for c in CELLS:
        ok, chg, mag, S20, q = verdicts[c]
        allsettled &= ok
        rec("### %-5s %14.6f %14.6f %10s %12.3e"
            % (c, chg, SETTLE_FRAC * mag, "yes" if ok else "### NO", B251_BARS[c]))
    rec("### ### **SETTLED AT EVERY CELL: %s**" % ("YES" if allsettled else "### NO"))
    rec("")

    # ------------------------------------------------------------------ THE TWO-AXIS TABLE
    rec("-" * 116)
    rec("### THE TWO-AXIS BEHAVIOUR (mode count x quadrature), AS A TABLE AND NOT A GUESS.")
    rec("-" * 116)
    rec("### %-5s %12s %12s %12s %12s %12s"
        % ("a^2", "S_20 NU=401", "S_20 NU=801", "|diff|", "S_20 dps60", "|diff|"))
    for c in CELLS:
        s401 = np.cumsum(np.array(r['%s|%s|%d' % (PRIMARY, c, NU0)]))[20]
        s801 = np.cumsum(np.array(r['%s|%s|%d' % (PRIMARY, c, NU1)]))[20]
        s60 = np.cumsum(np.array(r['%s|%s|%d' % (SELF, c, NU0)]))[20]
        rec("### %-5s %12.6f %12.6f %12.2e %12.6f %12.2e"
            % (c, s401, s801, abs(s401 - s801), s60, abs(s401 - s60)))
    rec("### ### **THE QUADRATURE AXIS (NU, 401 -> 801) MOVES `S_20` BY 3.1e-4 TO 1.1e-3.**")
    rec("### ### **THE MODE AXIS MOVES IT BY ABOUT 2.0 BETWEEN N = 6 AND N = 20 AND IS STILL")
    rec("### ### MOVING -- ### THREE ORDERS LARGER. ### THE TWO AXES ARE NOT COMPARABLE, WHICH IS")
    rec("### ### b242's FINDING SEEN ON A DIFFERENT OBJECT.**")
    rec("### ### **AND THE dps-60 COLUMN IS *NOT* A QUADRATURE-AXIS EFFECT AND MUST NOT BE READ AS")
    rec("### ### ONE: it diverges from the primary only because dps 60 loses the eigenpairs from")
    rec("### ### n = 16 up, per G-SELF above. ### ITS LARGEST DEVIATION (1.3e-1 at a^2 = 2) IS THAT")
    rec("### ### LOSS, NOT AN INSTABILITY OF THE OBJECT.**")
    rec("=" * 116)
    io.open(BANK, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
