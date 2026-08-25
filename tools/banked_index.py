# -*- coding: utf-8 -*-
"""banked_index.py -- THE BANKED-RESULT INDEX (built b160).

### WHY THIS EXISTS. At b154 and again at b158 an act marked an object OPEN --
### the E1/even identification, "owner-quotable only as a reading" -- while the
### derivation sat banked at b35's registration since 2026-08-18. b159 found it.
### ### TWO ACTS DID NOT READ A RESULT THE RECORD ALREADY HELD.
### That is not a calibration error and not a false pass. ### IT IS A READING NOT
### DONE, and no existing law addresses it: the source-read-first law governs HOW
### a source is read, and says nothing about FINDING WHICH OWNER HOLDS A RESULT.

### THE CURE IS AN INDEX, AND THE CONVENTION THAT GOES WITH IT (b160):
### BEFORE AN OBJECT IS MARKED OPEN, NAVIGATOR-ASSERTED, OR REQUIRING A
### CONSTRUCTION, THE INDEX IS QUERIED AND THE QUERY'S RESULT REPORTED.
### An open declared without the query is a claim about the record made without
### reading it.

### THE REACH, STATED HERE AND PRINTED ON EVERY QUERY BECAUSE IT IS THE MOST
### DANGEROUS MISREADING THIS TOOL MAKES AVAILABLE:
### ### ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD.
### The index holds what the scan surfaced and a human read. A future act that
### reads "not in the index" as "not in the corpus" would repeat b158's error
### WITH A TOOL'S AUTHORITY BEHIND IT, which is worse than repeating it without.
### ### QUERYING THE INDEX IS NOT READING THE CORPUS. The convention requires the
### query; it does not license skipping the read.

### AND AN INDEX ENTRY IS A POINTER, NEVER A PROMOTION. Every entry carries the
### grade ITS OWN ACT recorded. ### WHERE THE INDEX AND THE ACT DISAGREE, THE ACT
### WINS. Nothing is re-graded by being indexed.

Usage:
    python banked_index.py --scan                 candidates, with the curation boundary
    python banked_index.py --query <object> ...   what the record holds about an object
    python banked_index.py --table                the curated index as a markdown table
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
REPORTS = os.path.join(ROOT, 'reports')
GRADE = re.compile(r'\b(DERIVED|DERIVES)\b')

REACH = [
    "  ### REACH: ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD.",
    "  ### The index holds what the scan surfaced and a human read at content.",
    "  ### Querying the index is NOT reading the corpus.",
    "  ### An entry is a POINTER, never a promotion; the grade is its own act's,",
    "  ### and where the index and the act disagree, THE ACT WINS.",
]

# ---------------------------------------------------------------------------
# THE CURATED INDEX. Every row was read at content in its own file. The `grade`
# column is quoted from the act that produced the result, never re-assigned.
# ---------------------------------------------------------------------------
INDEX = [
    # (object, act, one-line statement, grade as its own act recorded it, location)
    ("E1/even identification; sector correspondence", "b35",
     "xi_n = sqrt(2)*psi_{2n}, so the E1 sector is xi_n with n EVEN and the (-1) sector n ODD",
     "banked read (P2 resurrection part 2); used at b159 as the bridge's derivation",
     "data/b35_registration_2026-08-18.txt"),
    ("sector occupancy; the arity question", "b159",
     "the layer occupies only two of proj4's four sectors; the +-i sectors are unoccupied",
     "DERIVES (instances) + derived read at owners",
     "data/b159_seam_and_arity.txt; Core/SectorOccupancyShadow.lean"),
    ("the void gate", "b154",
     "sum_n w_n - A = -resid_N*(sum_n u_n - 1): the gate forces the normalization ALONE",
     "DERIVED (exact algebra); decided at instances in Core",
     "data/b154_apportionment_characterization.txt; Core/ApportionmentShadow.lean"),
    ("the apportionment family; the unpinned share", "b154",
     "the admissible apportionments form a ONE-PARAMETER FAMILY containing b38's as one member",
     "DERIVED",
     "data/b154_apportionment_characterization.txt"),
    ("the share's physicality", "b155",
     "the identity's residual moves with the share at rate resid_N; at most one share admits it",
     "DERIVED, conditional on b107's undischarged T-reading",
     "data/b155_nu.txt; Core/ShareDependenceShadow.lean"),
    ("the certified column's double entry", "b156",
     "the column enters the closed equation twice; the entries net to (1 - mu), not cancelling",
     "DERIVED (exact); decided at instances",
     "data/b156_seam_and_joint.txt; Core/DoubleEntryShadow.lean"),
    ("the apportionment-free candidate", "b156",
     "the purely object-side formula equals W+(0): a FAMILY MEMBER, not an escape",
     "DERIVED",
     "data/b156_seam_and_joint.txt"),
    ("file E's requirements as a selection criterion", "b158",
     "no owner-quotable requirement constrains the share; the freedom is DEFINITIONAL",
     "DERIVED (reads at owners); branch (c)",
     "data/b158_selection.txt"),
    ("refinement arity", "b158",
     "a two-fold aggregate does not determine a four-fold split",
     "DERIVES (instances)",
     "data/b158_selection.txt; Core/RefinementArityShadow.lean"),
    ("the exact reduction; the two excesses", "b109",
     "W+ - sigma_even*A = the raw trace's even-share excess minus the eps integral's",
     "DERIVED, exact algebra",
     "data/b109_apportionment_derivation.txt"),
    ("the apportionment's grade", "b107",
     "the joint is CLOSED-AT-BENCH and OPEN-AT-DERIVATION",
     "the two-grade reconciliation, decided at content",
     "data/b107_apportionment.txt"),
    ("the boundary license", "b151",
     "no license derives; all three routed candidates were reads, and a license needs a construction",
     "branch (b); the negative-read fence rides",
     "data/b151_boundary.txt"),
    ("the collapse to one density", "b115",
     "the deviation's window-dependence reduces to a fixed-kernel scale-average of ONE density",
     "DERIVED; decided at instances",
     "data/b115_mechanism.txt; Core/MechanismShadow.lean"),
    ("the mean-zero kernel; uniqueness's sufficient condition", "b116",
     "Phi_K is mean-zero with one sign change, so Psi monotone increasing => the window is unique",
     "DERIVED",
     "data/b116_thirteenth_seam_close.txt"),
]


def scan():
    """### THE MECHANICAL HALF. It surfaces candidates; it does not grade them."""
    hits = []
    for base in (DATA, REPORTS):
        if not os.path.isdir(base):
            continue
        for fn in sorted(os.listdir(base)):
            if not fn.endswith(('.txt', '.md')):
                continue
            p = os.path.join(base, fn)
            try:
                lines = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
            except Exception:
                continue
            for i, L in enumerate(lines, 1):
                if GRADE.search(L):
                    hits.append((fn, i, L.strip()[:96]))
    return hits


def cmd_scan():
    hits = scan()
    files = len({h[0] for h in hits})
    print("=" * 78)
    print("BANKED-RESULT INDEX -- THE SCAN (candidates only)")
    print("=" * 78)
    print("  grade-word lines found : %d" % len(hits))
    print("  files carrying them    : %d" % files)
    print("  ### CURATED INTO THE INDEX : %d" % len(INDEX))
    print("  ### THE CURATION BOUNDARY IS STATED, NOT HIDDEN: most candidates are")
    print("  ### grade words in prose rather than indexable results, and the")
    print("  ### difference between %d and %d is a HUMAN READ, not a filter."
          % (len(hits), len(INDEX)))
    print("  ### AN INDEX THAT HID ITS OWN SELECTION WOULD BE AN UNSTATED TRUNCATION.")
    for s in REACH:
        print(s)
    return 0


def cmd_query(terms):
    q = " ".join(terms).lower()
    print("=" * 78)
    print("BANKED-RESULT INDEX -- QUERY: %r" % q)
    print("=" * 78)
    found = [e for e in INDEX
             if q in e[0].lower() or q in e[2].lower() or q in e[1].lower()]
    if found:
        print("  ### THE RECORD HOLDS %d INDEXED RESULT(S) ABOUT THIS OBJECT:" % len(found))
        for obj, act, stmt, grade, loc in found:
            print("\n    object   : %s" % obj)
            print("    act      : %s" % act)
            print("    result   : %s" % stmt)
            print("    grade    : %s   ### as its own act recorded it" % grade)
            print("    location : %s" % loc)
    else:
        print("  ### NO INDEXED RESULT MATCHES.")
        print("  ### THIS IS NOT A FINDING THAT THE RECORD HOLDS NOTHING.")
    print()
    for s in REACH:
        print(s)
    return 0


def cmd_table():
    print("| object | act | the result, in one line | grade, as its own act recorded it | location |")
    print("|:--|:--|:--|:--|:--|")
    for obj, act, stmt, grade, loc in INDEX:
        print("| **%s** | `%s` | %s | *%s* | `%s` |" % (obj, act, stmt, grade, loc))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == '--scan':
        return cmd_scan()
    if argv[0] == '--query':
        if len(argv) < 2:
            print("  ### --query needs an object name.")
            return 2
        return cmd_query(argv[1:])
    if argv[0] == '--table':
        return cmd_table()
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
