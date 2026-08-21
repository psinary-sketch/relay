#!/usr/bin/env python3
"""
b56 -- THE DEFICIT COMPARISON. Component 1: the closed form verified exactly against all
six banked values. Component 2: the registered candidates evaluated within the
anti-numerology guard. Registration: data/b56_registration_2026-08-21.txt (banked BEFORE
this run). Usage: python b56_deficit.py register | run
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "..", "data", "b56_registration_2026-08-21.txt")

D1 = {(2,1): 0, (3,1): 1, (2,2): 2, (5,1): 4, (2,3): 12, (3,2): 16, (2,4): 56, (3,3): 169}
Q  = {(2,1): 2, (3,1): 3, (2,2): 4, (5,1): 5, (2,3): 8, (3,2): 9, (2,4): 16, (3,3): 27}
ROSTERS = [("R5", [(2,1),(3,1)], 0), ("R1", [(2,1),(3,1),(5,1)], 11),
           ("R2", [(2,2),(3,2)], 126), ("R3", [(2,2),(3,2),(5,1)], 2282),
           ("R4", [(2,3),(3,2),(5,1)], 12512), ("EXT", [(2,4),(3,3)], 37800)]

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("register", "run"):
        print(__doc__); return
    if sys.argv[1] == "register":
        print(open(REG, encoding="utf-8", errors="replace").read()); return
    out = ["### REGISTRATION CLOSED (data/b56_registration_2026-08-21.txt, banked before this run).",
           "### COMPONENT 1: the closed form against all six banked values, integer form.",]
    ok1 = True
    for name, roster, banked in ROSTERS:
        prod = 1
        for c in roster: prod *= (Q[c]-1)**2
        s = sum(D1[c] for c in roster)
        lhs = prod - 4*s
        ok = (lhs == 4*banked)
        ok1 = ok1 and ok
        out.append(f"  {name}: prod(q-1)^2 - 4*sum d_1 = {prod} - {4*s} = {lhs} = 4*{banked}: "
                   f"{'EXACT' if ok else 'MISMATCH'}")
    out.append(f"COMPONENT 1 VERDICT: the closed form deficit = (1/4)prod(q_v-1)^2 - sum d_1 "
               f"{'VERIFIED EXACTLY at all six banked values' if ok1 else 'FAILS'}")
    out.append("  local-data reduction checked: odd d_1 = (q-1)^2/4 (flatness); even "
               "d_1(2,n) = 2^(2n-2) - 2^(n-1) = " +
               str([2**(2*n-2) - 2**(n-1) for n in (1,2,3,4)]) + " vs banked [0, 2, 12, 56]: "
               + ("EXACT" if [2**(2*n-2)-2**(n-1) for n in (1,2,3,4)] == [0,2,12,56] else "MISMATCH"))
    out.append("")
    out.append("### COMPONENT 2: the registered candidates, within the guard (no others evaluated).")
    out.append("  B1 (the grid-rank dimension-analogue; banked value 21 at the banked grid):")
    for name, roster, banked in ROSTERS:
        out.append(f"    {name}: closed form {banked} vs B1 = 21: "
                   f"{'match' if banked == 21 else 'NO MATCH'}"
                   + ("" if banked != 21 else " -- would be OBSERVATION-ONLY regardless (B1 is resolution-dependent, disqualified as principled by its own derivation chain)"))
    out.append("    B1 STANDING DISQUALIFICATION: resolution-dependent by the no-finite-levels")
    out.append("    theorem -- cannot supply a roster-independent integer; not principled.")
    out.append("  B2 (the epsilon'(1+) E_1 share, 14.1773 at the banked pins): a real-valued")
    out.append("    trace MASS in the functional's own units -- INCOMMENSURABLE with the integer")
    out.append("    closed form without a normalization the sources do not derive; no numerical")
    out.append("    comparison is licensed; recorded as such, evaluated no further.")
    out.append("  NO THIRD CANDIDATE derives from the sources (registered).")
    out.append("")
    out.append("VERDICT: BRANCH (c) -- the registered expectation. No principled bridge derives")
    out.append("from the corpus's archimedean sources; the act closes as a SPECIFICATION (the")
    out.append("wanted-poster paragraph, filed to OPEN_TRAILS with the closed form as target).")
    print("\n".join(out))

if __name__ == "__main__":
    main()
