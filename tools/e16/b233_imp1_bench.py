# -*- coding: utf-8 -*-
"""b233_imp1_bench.py -- IMP-1 VERIFIED AT BENCH, WITH THE CORPUS'S OWN INSTRUMENTS.

### WHAT THIS VERIFIES. IMP-1 is the classical explicit formula's two-ended prime side,
### which b232's import ledger carries at TRUSTED-AT-CITE. ### THIS PUTS IT ON OUR OWN BENCH:
### CC's equation (1) -- `f~(0) - SUM_rho f~(rho) + f~(1) = SUM_v W_v(f)` -- computed on BOTH
### SIDES at the corpus's own bump, at the ### DIAGONAL a^2 CELLS 2, 3, 4.

### THE TWO SIDES:
###   ZERO SIDE  -- `Z = 2 * SUM_gamma hhat_w(gamma)^2`, the transform of `corr = w conv w`,
###                 with gamma from ### mpmath.zetazero COMPUTED HERE, not taken from the
###                 banked `zeta_ordinates.npy` (the banked file is used only as a CONTROL).
###   PLACES SIDE -- `P - PR + A` from ### b38_act10.left_side, IMPORTED UNMODIFIED.

### WHY b38 AND NOT carto_atlas.channels: ### THERE ARE TWO PRIME COLUMNS IN THE INSTRUMENT
### LAYER AND THEY ARE FOR DIFFERENT TEST FUNCTIONS. `channels` computes for the bump `w`
### (cutoff p^k <= a); `b38_act10.left_side` computes for `corr = w conv w` (cutoff p^k <= a^2),
### and its `A = INT hhat_w(U)^2 kernel(U) dU / 2pi` and `P = 2 (INT w cosh(v/2))^2` carry the
### SQUARES that are the autocorrelation transform's signature. ### b229 AND b232 ADOPTED FROM
### b38, SO THE BENCH USES b38 -- and the zero side is therefore built from hhat^2.

### THE LINK TO IMP-1's TWO-ENDED FORM: `PR` is the FOLDED one-sided sum with its factor 2.
### b231 compiled the fold identity (FoldedMirrorShadow, 14 terminals, zero axioms) and showed
### the bump's `corr` is even. ### SO VERIFYING THE FORMULA WITH `PR` VERIFIES THE TWO-ENDED
### FORM, VIA A COMPILED IDENTITY. That chain is stated here, not assumed.

### WHAT THIS DOES NOT TOUCH: ### `T` AND `Q` -- THE CORPUS'S LEFT SIDE -- APPEAR NOWHERE.
### This is the import's own two sides against each other. No ledger comparison, no calibration.

### THE AXIS DISCIPLINE: ### N IS REGISTERED AT 1000 BEFORE THE FIRST NUMBER (registration
### 2026-08-28). Any other N below is a VARIED AXIS and is reported as one, never as a repair.
"""
import io
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C        # noqa: E402
import b38_act10 as B38        # noqa: E402

CACHE = (r"C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--"
         r"\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b233_zeros.json")

N_REG = 1000                    # ### THE REGISTERED TRUNCATION
CELLS = [(2, "2"), (3, "3"), (4, "4")]      # ### DIAGONAL a^2 CELLS
PRIMES = (2, 3, 5)              # ### b38's own S4


def zeros_mpmath(n):
    """### COMPUTED HERE WITH mpmath.zetazero -- not read from the banked ordinates."""
    if os.path.isfile(CACHE):
        got = json.load(io.open(CACHE, encoding='utf-8'))
        if len(got) >= n:
            return np.array(got[:n], dtype=float)
    from mpmath import mp, zetazero
    mp.dps = 25
    out = []
    for k in range(1, n + 1):
        out.append(float(zetazero(k).imag))
        if k % 100 == 0:
            sys.stdout.write("   zetazero %d/%d  gamma=%.4f\n" % (k, n, out[-1]))
            sys.stdout.flush()
    io.open(CACHE, 'w', encoding='utf-8').write(json.dumps(out))
    return np.array(out, dtype=float)


def zero_side(a, gam):
    """### Z = 2 * SUM hhat_w(gamma)^2 -- the transform of corr, at the computed zeros."""
    v, w = C.bump(a)
    g = C.hhat(v, w, gam)
    return 2.0 * float(np.sum(g * g))


def tail_bound(a, T, umax=4000.0, npts=20001):
    """### THE OMITTED TAIL, BOUNDED AND QUOTED -- NOT ASSUMED.

    ### |2 SUM_{gamma > T} hhat(gamma)^2| <= 2 INT_T^inf hhat(u)^2 dN(u), and the zero-counting
    ### density is dN/du = log(u/2pi)/2pi. ### THE BOUND IS COMPUTED NUMERICALLY ON A GRID THAT
    ### RUNS WELL PAST WHERE hhat^2 HAS DIED."""
    v, w = C.bump(a)
    u = np.linspace(T, umax, npts)
    g = C.hhat(v, w, u)
    dens = np.log(np.maximum(u, 7.0) / (2.0 * math.pi)) / (2.0 * math.pi)
    return float(2.0 * np.trapezoid(g * g * dens, u))


def places_side(a):
    """### IMPORTED UNMODIFIED FROM b38_act10 -- the adopted instrument, at its pin."""
    v, w, corr, vc, L = B38.family(a)
    A, P, PR = B38.left_side(a, PRIMES, v, w, corr, vc, L)
    return A, P, PR


def run(gam, n, label, umax=None, nu=None):
    """### One axis setting, all three DIAGONAL a^2 cells."""
    old_umax, old_nu = C.UMAX, C.NU
    if umax is not None:
        C.UMAX = umax
    if nu is not None:
        C.NU = nu
    C._KERN = None                      # ### the kernel cache is axis-dependent
    rows = []
    for a_sq, tag in CELLS:
        a = math.sqrt(a_sq)
        A, P, PR = places_side(a)
        Z = zero_side(a, gam[:n])
        places = P - PR + A
        rows.append(dict(cell=tag, a_sq=a_sq, a=a, Z=Z, P=P, A=A, PR=PR,
                         places=places, resid=Z - places,
                         tail=tail_bound(a, float(gam[n - 1]))))
    C.UMAX, C.NU, C._KERN = old_umax, old_nu, None
    return label, rows


def show(label, rows):
    print("\n--- %s" % label)
    print("  %-6s %13s %13s %13s %13s %13s %12s %12s"
          % ("a^2", "Z (zeros)", "P (pole)", "A (arch)", "PR (primes)",
             "places", "residual", "tail bound"))
    for r in rows:
        print("  %-6s %13.9f %13.9f %13.9f %13.9f %13.9f %12.3e %12.3e"
              % (r['cell'], r['Z'], r['P'], r['A'], r['PR'], r['places'],
                 r['resid'], r['tail']))


def main():
    print("=" * 116)
    print("b233 -- IMP-1 AT BENCH: CC eq (1), BOTH SIDES, AT THE DIAGONAL a^2 CELLS 2, 3, 4")
    print("=" * 116)
    print("### THE CORPUS'S LEFT SIDE (T, Q) APPEARS NOWHERE IN THIS COMPUTATION.")
    print("### N REGISTERED AT %d BEFORE THE FIRST NUMBER. Lower N below = a VARIED AXIS." % N_REG)

    print("\n### G-ZEROS -- computing %d ordinates with mpmath.zetazero ..." % N_REG)
    gam = zeros_mpmath(N_REG)
    print("   gamma_1 = %.9f   gamma_%d = %.6f" % (gam[0], N_REG, gam[-1]))

    # ### THE POSITIVE CONTROL: the freshly computed zeros against the banked artifact.
    # ### IF THESE DISAGREE, EITHER THE COMPUTATION OR THE BANK IS WRONG AND NOTHING BELOW
    # ### MEANS ANYTHING. ### A CONTROL, NOT A DECORATION.
    banked = C.GAM[:20]
    dev = float(np.max(np.abs(gam[:20] - banked)))
    print("   ### CONTROL vs banked zeta_ordinates.npy (first 20): max deviation = %.3e" % dev)
    print("   ### %s" % ("CONTROL PASSES -- fresh and banked agree"
                         if dev < 1e-6 else "### CONTROL FAILS -- STOP, nothing below is evidence"))
    if dev >= 1e-6:
        return 1

    runs = [run(gam, N_REG, "AXIS 0 (registered): N=%d, UMAX=%.0f, NU=%d"
                % (N_REG, C.UMAX, C.NU))]
    # ### G-STAB -- the floor-axis law: vary and report, never tune.
    runs.append(run(gam, 500, "AXIS 1 (varied): N=500"))
    runs.append(run(gam, 750, "AXIS 2 (varied): N=750"))
    runs.append(run(gam, N_REG, "AXIS 3 (varied): UMAX=900", umax=900.0))
    runs.append(run(gam, N_REG, "AXIS 4 (varied): NU=18001", nu=18001))

    for label, rows in runs:
        show(label, rows)

    print("\n" + "=" * 116)
    print("  ### THE VERDICT LINE -- registered in advance: THE TRUNCATION TAIL, NOT THE")
    print("  ### MATHEMATICS, BOUNDS THE RESIDUAL. Each cell passes iff |residual| <= tail bound.")
    print("=" * 116)
    ok = True
    for label, rows in runs:
        for r in rows:
            good = abs(r['resid']) <= r['tail']
            ok = ok and good
            print("  %-44s a^2=%-3s |resid|=%.3e  tail=%.3e  %s"
                  % (label[:44], r['cell'], abs(r['resid']), r['tail'],
                     "within" if good else "### ABOVE THE BOUND"))
    print("\n  ### ALL CELLS, ALL AXES, WITHIN THE QUOTED TAIL BOUND: %s" % ("YES" if ok else "NO"))
    print("  ### 'within' MEANS THE FORMULA IS CONFIRMED TO THE PRECISION THE TRUNCATION ALLOWS.")
    print("  ### IT DOES NOT MEAN THE FORMULA IS PROVED HERE. ### NO AXIS WAS TUNED.")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
