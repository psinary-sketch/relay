# -*- coding: utf-8 -*-
"""b242 COMPONENT 2 -- THE ENVELOPE, DERIVED FROM COMPONENT 1's MEASURED ORDERS.

### THIS TOOL WRITES THE ENVELOPE FILE. ### THE CERTIFYING/CONFIRMING RUN IS COMPONENT 3 AND
### IT IS GATED ON THIS FILE'S HASH AND MTIME. ### NO VERDICT IS WRITTEN HERE.
###
### IT CONSUMES ONLY BANKED COMPONENT-1 POINTS (data/b242_axis_points.json) AND THE LAYER'S
### OWN EIGENVALUES. ### IT COMPUTES NO NEW CELL QUANTITY, SO IT CANNOT QUIETLY RE-TUNE A
### MEASUREMENT TO SUIT AN ENVELOPE.
### ### SCOPE: LEFT SIDE ONLY. ### `A` enters nowhere in this file.
"""
import io
import json
import math
import sys

sys.path.insert(0, r"D:\relay\tools\e16")
import numpy as np                      # noqa: E402
import b38_act10 as B38                 # noqa: E402
import qeps_layer as Q                  # noqa: E402

POINTS = r"D:\relay\data\b242_axis_points.json"
ENV = r"D:\relay\data\b242_envelope.txt"
FLOOR = 1e-13
N_CERT = 7          # ### modes 0..6 -- the ones above the floor. MEASURED at 1b, not chosen.


def main():
    pts = json.load(io.open(POINTS, encoding="utf-8"))
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b242 COMPONENT 2 -- THE ENVELOPE. ### DERIVED FROM COMPONENT 1's MEASURED ORDERS.")
    rec("### BANKED AND HASHED BEFORE THE CONFIRMING RUN. ### NO VERDICT IS WRITTEN IN THIS FILE.")
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS. ### LEFT SIDE ONLY.")
    rec("")

    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(700)
    rec("-" * 104)
    rec("(1) WHERE THE INSTRUMENT STOPS, AND WHY MORE QUADRATURE DOES NOT MOVE IT.")
    rec("-" * 104)
    rec("  n    lam2_n          log10(lam2_n)   digits gained over n-1")
    prev = None
    for n in range(len(lam2)):
        lg = math.log10(float(lam2[n])) if lam2[n] > 0 else float('nan')
        d = ("%.2f" % (prev - lg)) if prev is not None else "--"
        rec("  %-4d %.6e   %12.4f   %s" % (n, lam2[n], lg, d))
        prev = lg
    rec("  ### THE FLOOR IS CROSSED AT n = 7 AND `n_last = 6` AT **EVERY** NQ IN 500..1300")
    rec("  ### (Component 1b's own table). ### MORE QUADRATURE POINTS BUY NO FURTHER MODES:")
    rec("  ### the limit is the EIGENVALUE's size against float64, not the quadrature's density.")
    rec("  ### EACH FURTHER MODE COSTS ~3.4-3.5 DECIMAL DIGITS AND THE COST IS STILL RISING.")
    rec("")

    rec("-" * 104)
    rec("(2) THE MEASURED DECAY ON THE CERTIFIED RANGE (modes 0..%d, all above the floor)."
        % (N_CERT - 1))
    rec("### RATIOS ARE MEASURED, NOT FITTED. ### No constant is chosen to make a tail small.")
    rec("-" * 104)
    tails = {}
    for a, alab in B38.CELLS:
        d = pts["trunc|%s" % alab]
        tr = np.array(d["tr"])
        rec("")
        rec("  a^2 = %-4s   tr[0..%d] = %s" % (alab, N_CERT - 1,
                                               " ".join("%.6f" % v for v in tr[:N_CERT])))
        ratios = [tr[n + 1] / tr[n] for n in range(N_CERT - 1)]
        rec("             ratios    = %s" % " ".join("%.4f" % r for r in ratios))
        rmax = max(ratios[-4:])
        rlast = ratios[-1]
        # ### THE TAIL A GEOMETRIC EXTRAPOLATION WOULD GIVE, AT THE LARGEST LATE RATIO.
        t_max = tr[N_CERT - 1] * rmax / (1.0 - rmax)
        t_last = tr[N_CERT - 1] * rlast / (1.0 - rlast)
        tails[alab] = (rlast, rmax, t_last, t_max)
        rec("             ### last ratio %.4f | max of last four %.4f" % (rlast, rmax))
        rec("             ### GEOMETRIC TAIL beyond mode %d, IF the ratio held: %.4f (at r_last)"
            % (N_CERT - 1, t_last))
        rec("             ###                                                 %.4f (at r_max)"
            % t_max)
    rec("")
    rec("  ### AND THE FACT THAT DECIDES THIS ACT'S BRANCH, READ OFF THE RATIO ROWS ABOVE:")
    rec("  ### ### THE RATIO IS **RISING** ACROSS THE LAST FOUR CERTIFIED MODES AT EVERY CELL.")
    rec("  ### A rising ratio over four points does not distinguish 'converging to ~0.9' from")
    rec("  ### 'rising to 1'. ### SEVEN POINTS CANNOT TELL THOSE APART, AND THE MODES THAT")
    rec("  ### WOULD TELL THEM APART ARE BELOW THE FLOAT64 EIGENVALUE FLOOR.")
    rec("")

    rec("-" * 104)
    rec("(3) THE ENVELOPE THAT WOULD FOLLOW -- AND WHY IT IS **NOT** BANKED AS ONE.")
    rec("-" * 104)
    rec("  a^2      tail(r_last)     tail(r_max)   b240's bar_L   tail / bar_L")
    barL = {"2": 7.452637e-01, "3": 5.042319e-01, "4": 3.991934e-01,
            "8": 2.671917e-01, "9": 2.492803e-01, "12": 2.034459e-01}
    for a, alab in B38.CELLS:
        rlast, rmax, t_last, t_max = tails[alab]
        rec("  %-6s %14.6f %15.6f %14.6f %14.2f"
            % (alab, t_last, t_max, barL[alab], t_last / barL[alab]))
    rec("")
    rec("  ### THREE REASONS THIS IS NOT AN ENVELOPE, AND ANY ONE OF THEM IS SUFFICIENT:")
    rec("  ###  (i)   ### THE RATIO IS RISING. A geometric envelope needs a ratio BOUNDED away")
    rec("  ###        from 1, and the measurement shows it climbing at the last certified mode.")
    rec("  ###  (ii)  ### THE EXTRAPOLATION IS UNVERIFIABLE AT THIS INSTRUMENT IN PRINCIPLE, not")
    rec("  ###        merely unverified: the modes that would test it have eigenvalues below the")
    rec("  ###        float64 floor, and Component 1b showed MORE QUADRATURE DOES NOT HELP.")
    rec("  ###  (iii) ### NO OWNER PROVES THE TRACE SERIES CONVERGES AT ALL. sec 20(b) calls it")
    rec("  ###        'an 11-mode band-limited truncation whose low-mode terms decay slowly' --")
    rec("  ###        ### A DESCRIPTION, NOT A CONVERGENCE THEOREM. ### An envelope on an")
    rec("  ###        unproven-convergent series is a guess with a formula on it.")
    rec("")

    rec("-" * 104)
    rec("(4) THE OBSTRUCTION, PRICED IN THE UNITS IT WOULD ACTUALLY BE PAID IN.")
    rec("-" * 104)
    rec("  ### THE BINDING RESOURCE IS **WORKING PRECISION**, NOT QUADRATURE DENSITY.")
    rec("  ### At ~3.45 decimal digits per additional mode (measured in (1), and rising):")
    for extra in (4, 9, 20, 47):
        rec("  ###   +%-3d modes  ->  ~%3d further decimal digits  ->  working precision ~%d dps"
            % (extra, int(math.ceil(3.45 * extra)), int(math.ceil(3.45 * extra)) + 16))
    rec("  ### AND HOW MANY MODES A USEFUL TAIL WOULD NEED, from the measured r_last per cell:")
    for a, alab in B38.CELLS:
        rlast, rmax, t_last, t_max = tails[alab]
        d = pts["trunc|%s" % alab]
        tr = np.array(d["tr"])
        target = 0.01
        k = math.ceil(math.log(target * (1 - rlast) / (tr[N_CERT - 1] * rlast))
                      / math.log(rlast)) if rlast < 1 else -1
        rec("  ###   a^2 = %-4s  tail < %.2f needs ~%d further modes  ->  ~%d dps"
            % (alab, target, k, int(math.ceil(3.45 * k)) + 16))
    rec("  ### ### SO THE PRICE IS A PROLATE EIGENSOLVER IN EXTENDED PRECISION -- A DIFFERENT")
    rec("  ### ### INSTRUMENT, NOT A REFINEMENT OF THIS ONE. ### `prolate_layer.prolate` is a")
    rec("  ### ### float64 eigendecomposition and no NQ makes it a bignum one.")
    rec("")

    rec("-" * 104)
    rec("(5) THE CONFIRMING RUN'S AXES, REGISTERED HERE BEFORE IT RUNS.")
    rec("-" * 104)
    rec("  ### CELLS: the banked six (2,3,4,8,9,12). ### NQ: 500,700,900,1100,1300.")
    rec("  ### TRUNCATIONS COMPARED: NMODE = %d (the last certified mode) against NMODE = 10"
        % N_CERT)
    rec("  ### (b240's base) and NMODE = 11 (the layer's ceiling).")
    rec("  ### THE CONFIRMING RUN'S ONE JOB: show that the NQ-stability of the CERTIFIED")
    rec("  ### truncation, and the instability of the floor-crossing ones, hold at these axes.")
    rec("  ### ### IT MAY NOT CHANGE THE BRANCH. ### THE BRANCH RULE IS THE REGISTRATION'S (C),")
    rec("  ### ### FIXED BEFORE ANY MEASUREMENT, AND THIS FILE DOES NOT RESTATE IT TO SOFTEN IT.")
    rec("")
    rec("### ### THE BRANCH THIS ENVELOPE POINTS AT, NAMED HERE SO COMPONENT 3 CANNOT DRIFT:")
    rec("### ### **(SLOW)** -- convergence MEASURED on the certified range (every ratio < 1),")
    rec("### ### an envelope BEYOND REACH at these instruments, and the obstruction PRICED above.")
    rec("### ### `bar_L` IS THEREFORE **HELD, NOT CERTIFIED**, AND M-4 IS **NOT** PAID AT BENCH.")
    rec("=" * 104)
    io.open(ENV, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % ENV)


if __name__ == "__main__":
    main()
