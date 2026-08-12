# -*- coding: utf-8 -*-
"""FINE-STRUCTURE-AT-FIRST-ENTRY -- W-ORD-CARTOGRAPHY strand 2.

QUESTION-FIT, LONGHAND, COMMITTED BEFORE THE RUN
------------------------------------------------
OBJECT: W(f_a) for f_a = g_a * g~_a on the certified instrument, at fine step
        over a in [1.40, 1.75] -- the first-entry band (p=2 enters at a=sqrt(2)
        = 1.41421; p=3 enters at a=sqrt(3) = 1.73205).

QUESTION IT BEARS ON: how the ledger's composition reorganizes as the p=2 term
        activates -- which channel absorbs the new term, at what rate, with what
        local structure.

BOTH BRANCHES, WRITTEN OUT:
  (A) SMOOTH ABSORPTION -- if the arch channel's change tracks the prime term's
      growth continuously and monotonically across the band, then the ledger
      reorganizes without local structure, and any technique's local mechanism
      may treat the entry as a smooth perturbation.
  (B) STRUCTURED ABSORPTION -- if non-monotone features appear at 10x the
      sweep's resolution, then the entry carries local structure, and a
      technique's local mechanism must reproduce that structure, not just the
      trend.
  EITHER BRANCH IS GROUND TRUTH. Neither bears on any unproven sign.

COMMITTED CONSTANTS (unchanged from the certified instrument):
        NV=4001  NU=12001  UMAX=600  TOL=1e-3  NGAM=10000
        step = 0.0025 over [1.40, 1.75]  -> 141 points (10x the sweep)
BOTH-ENDS VALIDATION per the standing law: a=1.40 and a=1.75.

DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim.
"""
import math, json, os
import numpy as np
import carto_atlas as C
import carto_auto as A

BANK = r"D:\relay\data\carto_fine.jsonl"
LO, HI, STEP = 1.40, 1.75, 0.0025


def row(a):
    r = A.channels_auto(a)
    geo = abs(r["arch"]) + abs(r["prime"])
    r["prime_share"] = abs(r["prime"]) / geo if geo else 0.0
    return r


if __name__ == "__main__":
    print("FINE-STRUCTURE-AT-FIRST-ENTRY")
    print("committed: NV=%d NU=%d UMAX=%.0f TOL=%.0e NGAM=%d step=%.4f"
          % (C.NV, C.NU, C.UMAX, C.TOL, C.NGAM, STEP))
    print("band [%.2f, %.2f]; sqrt2=%.5f  sqrt3=%.5f" % (LO, HI, math.sqrt(2), math.sqrt(3)))

    print("\n--- BOTH-ENDS VALIDATION ---")
    ok = True
    for a in (LO, HI):
        r = row(a)
        good = abs(r["residual"]) <= C.TOL
        ok &= good
        print("  a=%.4f  residual %+.3e  %s" % (a, r["residual"], "PASS" if good else "FAIL"))
    print("  VERDICT: %s" % ("PASS -- band certified" if ok else "FAIL -- band NOT certified"))
    if not ok:
        raise SystemExit(1)

    n = int(round((HI - LO) / STEP)) + 1
    rows = []
    if os.path.exists(BANK):
        os.remove(BANK)
    for i in range(n):
        a = LO + i * STEP
        r = row(a)
        rows.append(r)
        with open(BANK, "a", encoding="utf-8") as f:
            f.write(json.dumps(r) + "\n"); f.flush(); os.fsync(f.fileno())

    print("\n--- %d points banked ---" % len(rows))
    print("%-8s %11s %11s %11s %9s %s" % ("a", "W", "arch", "prime", "pr.shr", "primes"))
    for r in rows[::10]:
        print("%-8.4f %11.6f %11.6f %11.6f %9.5f %s"
              % (r["a"], r["zero"], r["arch"], r["prime"], r["prime_share"],
                 ",".join(map(str, r["prime_terms"])) or "-"))

    W = np.array([r["zero"] for r in rows])
    AR = np.array([r["arch"] for r in rows])
    PR = np.array([r["prime"] for r in rows])
    dW, dA, dP = np.diff(W), np.diff(AR), np.diff(PR)

    print("\n--- BRANCH TEST ---")
    print("  max |residual|        : %.2e" % max(abs(r["residual"]) for r in rows))
    print("  W  sign changes in dW : %d" % int(np.sum(np.signbit(dW[:-1]) != np.signbit(dW[1:]))))
    print("  arch monotone?        : %s" % (bool(np.all(dA >= 0)) or bool(np.all(dA <= 0))))
    print("  prime monotone?       : %s" % (bool(np.all(dP >= -1e-15))))
    print("  arch turning points   : %d" % int(np.sum(np.signbit(dA[:-1]) != np.signbit(dA[1:]))))
    print("  corr(dArch, dPrime)   : %.4f" % float(np.corrcoef(dA, dP)[0, 1]))
    print("  W min %.6f at a=%.4f ; W max %.6f at a=%.4f"
          % (W.min(), rows[int(W.argmin())]["a"], W.max(), rows[int(W.argmax())]["a"]))
    print("\nbanked: %s" % BANK)
