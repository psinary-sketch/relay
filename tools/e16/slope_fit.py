# -*- coding: utf-8 -*-
"""W-ORD-SLOPE: the fit and the verdict, against the rule committed at 67b7dea."""
import json, math
import numpy as np

def load(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

NEW = load(r"D:\relay\data\slope_points.jsonl")
FAM = load(r"D:\relay\data\threshold_law_points.jsonl")

def ols(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    n = len(x)
    sx, sy = x.mean(), y.mean()
    sxx = ((x - sx) ** 2).sum()
    b = ((x - sx) * (y - sy)).sum() / sxx
    a = sy - b * sx
    resid = y - (a + b * x)
    s2 = (resid ** 2).sum() / (n - 2)
    se_b = math.sqrt(s2 / sxx)
    return a, b, se_b, resid, n

# Student t, 95%, two-sided
TCRIT = {8:2.306, 9:2.262, 10:2.228, 11:2.201, 12:2.179, 13:2.160, 14:2.145, 18:2.101, 22:2.074}

def report(label, pts):
    x = [math.log(p["B"]) for p in pts]
    y = [p["c"] for p in pts]
    a, b, se, resid, n = ols(x, y)
    t = TCRIT.get(n - 2, 2.10)
    lo, hi = b - t * se, b + t * se
    # residuals under the LAW's slope of exactly 1
    a1 = float(np.mean(np.asarray(y) - np.asarray(x)))
    r1 = np.asarray(y) - (a1 + np.asarray(x))
    print("\n=== %s  (n=%d, B: %.0f .. %.0f = %.2f decades) ===" %
          (label, n, min(p["B"] for p in pts), max(p["B"] for p in pts),
           math.log10(max(p["B"] for p in pts) / min(p["B"] for p in pts))))
    print("  free slope        : %.4f   se %.4f   95%% CI [%.4f, %.4f]" % (b, se, lo, hi))
    print("  intercept         : %.4f" % a)
    print("  contains 1.000    : %s" % (lo <= 1.0 <= hi))
    print("  contains 0.9517   : %s" % (lo <= 0.9517 <= hi))
    print("  --- under slope-1 (the law's exact form) ---")
    print("  implied t         : %.5f  (ln t = %.5f)" % (math.exp(a1), a1))
    print("  max |residual|    : %.4f" % np.abs(r1).max())
    print("  residual sd       : %.4f" % r1.std(ddof=1))
    return b, lo, hi, np.abs(r1).max(), a1, r1, x, y

b, lo, hi, maxr, a1, r1, x, y = report("NEW RUN -- the committed fit, FULL B-range", NEW)

print("\n=== THE VERDICT, against the rule as committed ===")
unity = (lo <= 1.0 <= hi) and (maxr <= 0.30)
sub = not (lo <= 1.0 <= hi)
instr = (lo <= 1.0 <= hi) and (lo <= 0.9517 <= hi)
print("  UNITY-CONFIRMED   : CI contains 1.000 (%s) AND max|resid| <= 0.30 (%s, %.4f)  -> %s"
      % (lo <= 1.0 <= hi, maxr <= 0.30, maxr, unity))
print("  SUB-UNIT-MEASURED : CI excludes 1.000 -> %s" % sub)
print("  INSTRUMENT-LIMITED: CI contains BOTH 1.000 and 0.9517 -> %s" % instr)

print("\n=== MATCHED-PAIR COLLISIONS (same B, different gamma,delta) ===")
from collections import defaultdict
gb = defaultdict(list)
for p in NEW: gb[p["B"]].append(p)
for B in sorted(gb):
    g = gb[B]
    if len(g) > 1:
        cs = [q["c"] for q in g]
        print("  B=%-8.0f spread %.4f in c   (%s)" % (B, max(cs) - min(cs),
              ", ".join("g=%g,d=%g:c=%.4f" % (q["gamma"], q["delta"], q["c"]) for q in g)))
fb = defaultdict(list)
for p in FAM: fb[p["B"]].append(p)
for B in sorted(fb):
    if len(fb[B]) > 1:
        cs = [q["c"] for q in fb[B]]
        print("  B=%-8.0f spread %.4f in c   [FAMILY RUN, for comparison]" % (B, max(cs) - min(cs)))

print("\n=== RESIDUAL vs log B, under slope-1, ordered by B ===")
order = np.argsort(x)
print("  signs: " + " ".join(("+" if r1[i] > 0 else "-") for i in order))
print("  values:" + " ".join("%+.3f" % r1[i] for i in order))
xs = np.asarray(x)[order]; rs = r1[order]
rk = np.argsort(np.argsort(xs)); rr = np.argsort(np.argsort(rs))
nn = len(xs)
rho = 1 - 6 * ((rk - rr) ** 2).sum() / (nn * (nn * nn - 1))
print("  Spearman rho(residual, log B) = %+.3f" % rho)

print("\n=== SET BESIDE, LABELLED BY KIND, NEVER POOLED ===")
report("FAMILY RUN ten points (prior, NOT in the fit above)", FAM)
print("\n  Epstein point (REAL OBJECT, B = S_inf(5938) = 51596, c not recomputed here):")
print("    kind = REAL OBJECT; the family run recorded residual -0.1053 against ITS OWN fit.")
print("    NOT pooled, NOT refitted, and its B is an analytic quantity while the")
print("    synthetic B is a term count -- commensurability untested, as recorded then.")

print("\n=== the two runs' free slopes, side by side (NOT pooled) ===")
xf = [math.log(p["B"]) for p in FAM]; yf = [p["c"] for p in FAM]
_, bf, sef, _, nf = ols(xf, yf)
print("  family run (10 pts, 2.08 dec): slope %.4f  se %.4f" % (bf, sef))
print("  new run    (14 pts, 4.00 dec): slope %.4f  se %.4f" % (b, se := (hi - b) / TCRIT.get(len(NEW) - 2, 2.10)))
