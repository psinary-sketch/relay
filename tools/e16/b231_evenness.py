# -*- coding: utf-8 -*-
"""b231_evenness.py -- THE INSTRUMENT'S OWN corr, TESTED FOR EVENNESS, WITH A POLARITY CONTROL.

### THIS COMPUTES NOTHING AGAINST ANY TARGET. ### It touches no left-side object, forms no
### comparison, and produces no ledger number. ### It asks ONE question of the instrument that
### b229 adopted: is `corr` even, and is `np.convolve(w, w)` the autocorrelation it is called?

### WHY THE CONTROL IS NOT OPTIONAL. ### A test that only ever sees an even bump cannot tell
### the difference between "convolution of an even signal is even" and "convolution is always
### even" -- and the second is FALSE. ### THE NON-EVEN CONTROL IS WHAT GIVES THE PASS CONTENT.
"""
import math
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C   # noqa: E402


def autocorr(w):
    """### THE AUTOCORRELATION AS DEFINED: corr(t) = SUM_s w(s) w(s+t)."""
    return np.correlate(w, w, mode="full")


def conv(w):
    """### WHAT THE INSTRUMENT ACTUALLY WRITES: np.convolve(w, w, mode='full')."""
    return np.convolve(w, w, mode="full")


def asym(x):
    """### max |x(t) - x(-t)| over the centred array. Zero iff exactly even."""
    return float(np.max(np.abs(x - x[::-1])))


def report(name, w):
    cv, ac = conv(w), autocorr(w)
    print("  %-26s len=%-6d" % (name, len(w)))
    print("      w even?                       max|w - w_rev| = %.3e" % asym(w))
    print("      convolve(w,w) even?           max|c - c_rev| = %.3e" % asym(cv))
    print("      correlate(w,w) even?          max|a - a_rev| = %.3e" % asym(ac))
    print("      convolve == correlate?        max|c - a|     = %.3e" % float(np.max(np.abs(cv - ac))))
    return asym(w), asym(cv), float(np.max(np.abs(cv - ac)))


def main():
    print("=" * 84)
    print("b231 -- EVENNESS OF THE ADOPTED INSTRUMENT'S corr, WITH POLARITY CONTROLS")
    print("=" * 84)

    print("\n### CONTROL FIRST (the ferry's order): A NON-EVEN SIGNAL.")
    print("### IF THIS ONE ALSO CAME OUT EVEN, THE TEST WOULD BE MEASURING NOTHING.")
    bad = np.array([1.0, 2.0, 5.0, 1.0, 0.0], dtype=float)
    b_w, b_c, b_d = report("non-even control", bad)

    print("\n### AND A SECOND CONTROL: AN EVEN SIGNAL THAT IS NOT THE BUMP.")
    ev = np.array([1.0, 2.0, 5.0, 2.0, 1.0], dtype=float)
    e_w, e_c, e_d = report("even control", ev)

    print("\n### THE INSTRUMENT'S OWN BUMP, at the adopted cells (b38_act10.CELLS).")
    cells = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
             (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
    worst_w = worst_c = worst_d = 0.0
    for a, tag in cells:
        v, w = C.bump(a)
        print("\n   cell a^2 = %-4s  (a = %.6f,  L = log a = %.6f)" % (tag, a, math.log(a)))
        print("      v symmetric?                  max|v + v_rev| = %.3e" % float(np.max(np.abs(v + v[::-1]))))
        rw, rc, rd = report("bump(a)", w)
        worst_w, worst_c, worst_d = max(worst_w, rw), max(worst_c, rc), max(worst_d, rd)

    print("\n" + "=" * 84)
    print("  VERDICTS")
    print("=" * 84)
    print("  non-even control : w asym %.3e   conv asym %.3e   conv-vs-corr %.3e" % (b_w, b_c, b_d))
    print("      ### THE CONTROL MUST SHOW NONZERO conv ASYMMETRY, or the test is empty.")
    print("      ### control conv NOT even : %s" % ("YES -- the test has content" if b_c > 1e-12 else "NO -- ### TEST IS EMPTY"))
    print("      ### control conv != corr  : %s" % ("YES -- they are different objects" if b_d > 1e-12 else "NO"))
    print("  even control     : w asym %.3e   conv asym %.3e   conv-vs-corr %.3e" % (e_w, e_c, e_d))
    print("  THE BUMP (worst) : w asym %.3e   conv asym %.3e   conv-vs-corr %.3e" % (worst_w, worst_c, worst_d))
    ok = worst_w == 0.0 and worst_c == 0.0 and worst_d == 0.0
    print("\n  ### BUMP EVEN, corr EVEN, AND convolve == correlate, EXACTLY (bit-for-bit): %s"
          % ("YES" if ok else "NO"))
    print("  ### 'EXACTLY' MEANS ZERO, NOT SMALL. ### A tolerance here would hide the very")
    print("  ### thing being tested: the evenness is STRUCTURAL (w depends on t only through t^2),")
    print("  ### not numerical, so anything but 0.0 would be a finding against the reading.")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
