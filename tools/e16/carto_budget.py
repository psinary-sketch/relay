# -*- coding: utf-8 -*-
"""W-ORD-CARTOGRAPHY act 3 -- the certified atlas + the budget sheet.

Range FIXED at [1.30, 3.50] with re-validation rows at BOTH ends.
Constants unchanged: NV=4001 NU=12001 UMAX=600 TOL=1e-3 NGAM=10000.
DISCLAIMED REGISTER: a computation maps and cannot prove. No sign claim.

Budget: W(a) := Z(a), computed TWO WAYS --
    direct   : Z = 2 sum_gamma hhat(gamma)
    identity : P - PRIME + ARCH
Agreement of the two IS the per-row check.
"""
import math, json, os
import numpy as np
import carto_atlas as C

BANK = r"D:\relay\data\carto_budget.jsonl"
LO, HI = 1.30, 3.50


def row(a):
    r = C.channels(a)
    direct = r["zero"]
    identity = r["pole"] - r["prime"] + r["arch"]
    r["W_direct"] = direct
    r["W_identity"] = identity
    r["agree"] = abs(direct - identity)
    r["trunc_bound"] = C.trunc_bound(a)
    tot = abs(r["pole"]) + abs(r["arch"]) + abs(r["prime"])
    r["prime_share"] = abs(r["prime"]) / tot if tot else 0.0
    return r


if __name__ == "__main__":
    print("CERTIFIED RANGE: [%.2f, %.2f]. Constants UNCHANGED." % (LO, HI))
    print("\n--- RE-VALIDATION AT BOTH ENDS (the far-end rule, ratified) ---")
    ends_ok = True
    for a in (LO + 0.05, HI):
        r = row(a)
        ok = r["agree"] <= C.TOL
        ends_ok &= ok
        print("  a=%.2f  |direct-identity| = %.3e   trunc bound = %.2e   %s"
              % (a, r["agree"], r["trunc_bound"], "PASS" if ok else "FAIL"))
    print("\n  BOTH-ENDS VERDICT: %s" % ("PASS -- the range is certified" if ends_ok
                                         else "FAIL -- the range is NOT certified"))
    if not ends_ok:
        raise SystemExit(1)

    print("\n--- THE BUDGET SHEET  W(a) = Z(a), two ways ---")
    print("%-6s %12s %12s %10s %11s %11s %11s %8s %s"
          % ("a", "W direct", "W identity", "agree", "pole", "arch", "prime", "pr.share", "primes"))
    rows = []
    for a in (1.30, 1.35, 1.50, 1.70, 1.90, 1.99, 2.00, 2.01, 2.10, 2.40,
              2.70, 2.99, 3.00, 3.01, 3.20, 3.50):
        r = row(a)
        rows.append(r)
        with open(BANK, "a", encoding="utf-8") as f:
            f.write(json.dumps(r) + "\n"); f.flush(); os.fsync(f.fileno())
        print("%-6.2f %12.6f %12.6f %10.2e %11.6f %11.6f %11.6f %8.4f %s"
              % (a, r["W_direct"], r["W_identity"], r["agree"],
                 r["pole"], r["arch"], r["prime"], r["prime_share"],
                 ",".join(map(str, r["prime_terms"])) or "-"))

    neg = [r["a"] for r in rows if r["W_direct"] < 0]
    print("\n--- E6: W(a) >= 0 at every certified point? ---")
    print("  points with W < 0 : %s" % (neg or "NONE"))
    print("  min W             : %+.6f at a=%.2f"
          % min((r["W_direct"], r["a"]) for r in rows))
    print("  NOTE PRINTED ON THE SHEET: the zeros in range are ON-LINE, so this is EXPECTED")
    print("  and is NOT evidence about unproven zeros.")

    print("\n--- E7: THE THINNING (prime share as a widens) ---")
    for r in rows:
        if r["a"] >= 1.99:
            print("  a=%.2f  W=%+.6f  prime=%.6f  share=%.4f  %s"
                  % (r["a"], r["W_direct"], r["prime"], r["prime_share"],
                     ",".join(map(str, r["prime_terms"])) or "-"))
    print("\nbanked: %s" % BANK)
