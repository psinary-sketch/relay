"""W-ATTEMPT-2, SITTING 12 (item 3) — THE Q_3 LEVEL-4 PAIRING CELL, RE-RUN AT AN HONEST BUDGET.

RELAY-ONLY. SUB-GATE (restated). THE CORRECTED STOP IN FORCE. TESTING CONTINUES; the
register is untouched.

THE ONE DECLARED-SKIPPED CELL of sitting 11's p = 3 tower (b26): T2 at n = 4 — the
level-stability of the pairing on Q_3 at the 6400-dimensional Sonin space (all 6400^2 =
40,960,000 Gram entries, exact cyclotomic arithmetic in the zeta_(3^10) coefficient-dict
representation), skipped when the projection (591 s) exceeded the registered budget
(420 s), with the budget honestly not raised after the fact. THIS RUN'S BUDGET, SET
BEFORE RUNNING: 1800 s. The claim checked, exact: host Gram = 9 * level Gram on the nose
(the mass normalization as stated in b26).

BRANCHES: (closed) the sweep completes within budget and lands entry-exact — the p = 3
tower's T2 is exact at ALL levels 1..4 and the declared-skip is retired. (still-declared)
the sweep exceeds even this budget or a mismatch appears — reported exactly as found (a
mismatch would be a FINDING, the first break in the tower structure, and would be
reported at its entry address, never smoothed).

EXACT ARITHMETIC. RECORDED PLAINLY AS DATA. The register is untouched.
Usage:  python b29_attempt2_s12_t2n4.py register | run
"""

import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ======================================================================================
# REUSE.  b26 (sitting 11's p = 3 tower) and b21 (sitting 8's machinery) are IMPORTED,
# NOT MODIFIED and NOT RE-DERIVED.  This file adds exactly one thing: a SECOND, FASTER
# ROUTE to the same entry-exact comparison, cross-validated against b26's own route
# before it is used, so that the one cell b26 declared-skipped can be run inside an
# honest budget.  Neither b25 nor b26 is touched.
#
#   from b26: ZD    -- the p = 3 two-term cyclotomic fold (coefficient dictionaries),
#             Level -- the level-n Sonin data (q = 3^n, N = 9^n, d = (3^n - 1)^2),
#             P     -- the prime, 3,
#             t2_pairing -- b26's OWN T2 function, run here at n <= 3 as the spot-check.
#   from b21: emb_col -- the embedding iota in chart form.
# ======================================================================================

from b21_attempt2_s8 import emb_col
from b26_attempt2_s11 import ZD, Level, P
import b26_attempt2_s11 as b26

# ======================================================================================
# PURE-ASCII OUTPUT GUARD (as sittings 8, 10, 11).  The banked registration docstring
# above is VERBATIM in the file; typographic characters are folded at PRINT time only.
# ======================================================================================

_ASCII_FOLD = {0x2014: u"--", 0x2013: u"-", 0x2012: u"-", 0x2010: u"-", 0x2011: u"-",
               0x2018: u"'", 0x2019: u"'", 0x201c: u'"', 0x201d: u'"',
               0x2026: u"...", 0x00a0: u" ", 0x00d7: u"x", 0x2212: u"-",
               0x2192: u"->", 0x2264: u"<=", 0x2265: u">="}

_emit = print


def print(*args, **kw):  # noqa: A001  (deliberate module-scope shadow: ASCII guard)
    out = []
    for a in args:
        s = a if isinstance(a, str) else str(a)
        s = s.translate(_ASCII_FOLD)
        try:
            s.encode("ascii")
        except UnicodeEncodeError:
            s = s.encode("ascii", "backslashreplace").decode("ascii")
        out.append(s)
    _emit(*out, **kw)


# ======================================================================================
# THE LEDGER
# ======================================================================================

LEDGER = []
FAILS = []
DECLARED = []


def check(name, ok):
    LEDGER.append((name, bool(ok)))
    if not ok:
        FAILS.append(name)
    print("  %s  %s" % ("PASS" if ok else "**FAIL**", name))
    sys.stdout.flush()
    return bool(ok)


def dnote(name):
    """A DECLARED line: skipped or out of budget.  NEVER counted as EXACT."""
    DECLARED.append(name)
    print("  DECLARED  %s" % name)
    sys.stdout.flush()


# ======================================================================================
# THE BUDGET, SET BEFORE RUNNING (the registration's number).
# ======================================================================================

BUDGET_SECONDS = 1800.0
LEVELS_CROSS = [1, 2, 3]         # where BOTH routes are run, entry by entry
TARGET_LEVEL = 4                 # the declared-skipped cell
PROGRESS_ENTRIES = 1000000       # progress line every ~1M entries
SAMPLE_N4 = 120000               # reference-route sample size at n = 4


# ======================================================================================
# THE COMPARISON, STATED ONCE (this is b26's T2, unchanged in content).
#
#   level n, host h = n + 1, N = 9^n, N_h = 9^h.
#   level entry   <v, F_n w>_n = 9^(-n) S_n(v,w),   S_n = sum v w zeta_N^(m1 m2)     (4 terms)
#   host entry  <iota v, F_h iota w>_h = 9^(-h) S_h(v,w), S_h over iota columns     (36 terms)
#   equality ON THE NOSE  <=>  S_h = 9 S_n, compared inside the HOST field
#   Q(zeta_(9^h)) with the level exponents lifted by zeta_N = zeta_(N_h)^9.
#
# A Sonin column has 2 nonzeros; iota of one has 2 * 3 = 6 (p = 3).  So each Gram entry
# is a 36-term host sum against a 9-scaled 4-term lifted level sum: 40 folded terms.
# ======================================================================================

LIFT = P * P          # = 9: the p-dependent mass constant (sitting 10 had 4)


# ------------------------------------------------------------------ ROUTE A (REFERENCE)
def route_A_entry(zdh, Ah, An, Bh, Bn, scale=LIFT):
    """b26's own inner loop, verbatim in content: build S_h and the lifted 9 S_n as
       folded coefficient dictionaries over Q(zeta_(N_h)) and compare them entry-exact.
       Returns True if the entry MISMATCHES."""
    a = zdh.acc
    Sh = {}
    for m1, v1 in Ah:
        for m2, v2 in Bh:
            a(Sh, m1 * m2, v1 * v2)
    Sn = {}
    for m1, v1 in An:
        for m2, v2 in Bn:
            a(Sn, scale * m1 * m2, scale * v1 * v2)
    return not ZD.eq(Sh, Sn)


def route_A_matrix(hostl, levl, Nh, rows=None, cols=None, scale=LIFT):
    """the full (or sub-) boolean mismatch matrix by ROUTE A."""
    zdh = ZD(Nh)
    d = len(hostl)
    rows = range(d) if rows is None else rows
    cols = list(range(d)) if cols is None else list(cols)
    out = {}
    for c1 in rows:
        Ah, An = hostl[c1], levl[c1]
        out[c1] = [route_A_entry(zdh, Ah, An, hostl[c2], levl[c2], scale) for c2 in cols]
    return out


# ----------------------------------------------------------------------- ROUTE B (FAST)
# THE ROUTE NOTE, said in the output too: ROUTE B computes the SAME 40 folded terms per
# entry, in the SAME power basis zeta^0 .. zeta^(deg-1) with deg = 2*3^(2h-1), but does
# a whole Gram ROW at once in int64 arrays instead of one entry at a time in dicts.
# EXACTNESS IS NOT COMPROMISED: every operation is exact integer arithmetic (the largest
# intermediate is m1*m2 < N_h^2 = 3^20 ~ 3.5e9, far inside int64), and the zero test is
# exact, not a tolerance.
#
# The fold, vectorized: for a raw term (e, c) with e reduced mod N_h,
#     e <  deg :  one basis term (e, c)                       [padded with a (0, 0)]
#     e >= deg :  two basis terms (e - deg, -c) and (t + e - deg, -c),  t = 3^(2h-1)
# so each of the 40 raw terms becomes exactly 2 slots and every row has width 80 -- a
# rectangular array, no ragged structure.
#
# The exact zero test.  Pack each slot into ONE int64 key = e * 32 + (c + 16) (all
# coefficients here lie in [-9, 9], so the 5-bit field is exact and the key is monotone
# in e).  Sort each row of keys; then equal exponents are adjacent.  Let cs be the
# cumulative sum of the (decoded) coefficients along the sorted row and let the GROUP
# ENDS be the positions where the exponent changes (plus the last).  Then
#     all group sums are zero  <=>  cs = 0 at every group end
# (induction: the first group's sum IS cs at its end; each later group's sum is the
# difference of cs at consecutive group ends).  That is an exact integer identity, and
# it is the whole test: the entry matches iff the folded S_h - 9 S_n is the zero element.
# ------------------------------------------------------------------------------------

def build_arrays(L, h):
    """(M_host, V_host, M_lev, V_lev) as int64 arrays; host width 6, level width 2."""
    d = L.d
    ich = [emb_col(L.icols[c], P, L.n, h) for c in range(d)]
    widths = set(len(x) for x in ich)
    Mh = np.array([sorted(x) for x in ich], dtype=np.int64)
    Vh = np.array([[x[m] for m in sorted(x)] for x in ich], dtype=np.int64)
    Mn = np.array([sorted(c) for c in L.icols], dtype=np.int64)
    Vn = np.array([[c[m] for m in sorted(c)] for c in L.icols], dtype=np.int64)
    return Mh, Vh, Mn, Vn, widths, ich


def route_B_row(c1, Mh, Vh, Mn, Vn, Nh, deg, t, lo=0, hi=None, scale=LIFT):
    """boolean mismatch vector for Gram row c1 against columns [lo, hi)."""
    hi = Mh.shape[0] if hi is None else hi
    m1, v1 = Mh[c1], Vh[c1]
    m1n, v1n = Mn[c1], Vn[c1]
    A, B = Mh[lo:hi], Vh[lo:hi]
    An, Bn = Mn[lo:hi], Vn[lo:hi]
    k = A.shape[0]
    E = ((m1[None, :, None] * A[:, None, :]) % Nh).reshape(k, -1)
    C = (v1[None, :, None] * B[:, None, :]).reshape(k, -1)
    En = ((scale * m1n[None, :, None] * An[:, None, :]) % Nh).reshape(k, -1)
    Cn = (-scale) * (v1n[None, :, None] * Bn[:, None, :]).reshape(k, -1)
    E = np.concatenate([E, En], axis=1)
    C = np.concatenate([C, Cn], axis=1)
    ge = E >= deg
    s = E - deg
    K = np.concatenate([np.where(ge, s, E) * 32 + (np.where(ge, -C, C) + 16),
                        np.where(ge, t + s, 0) * 32 + (np.where(ge, -C, 0) + 16)], axis=1)
    K.sort(axis=1)
    Es = K >> 5
    Cs = (K & 31) - 16
    cs = np.cumsum(Cs, axis=1)
    bnd = np.empty(Es.shape, dtype=bool)
    bnd[:, :-1] = Es[:, :-1] != Es[:, 1:]
    bnd[:, -1] = True
    return np.any((cs != 0) & bnd, axis=1)


# ======================================================================================
# R1.  THE TWO ROUTES CROSS-VALIDATED BEFORE ROUTE B IS USED FOR ANYTHING.
#
#  (a) at n = 1, 2, 3 the two routes must agree ENTRY BY ENTRY on the real comparison;
#  (b) NEGATIVE CONTROL 1: with the mass constant deliberately wrong (3 instead of 9) the
#      two routes must agree entry by entry on a NONEMPTY mismatch set -- this proves the
#      fast route can SEE a mismatch rather than merely printing zeros;
#  (c) NEGATIVE CONTROL 2: with ONE level column corrupted (a single chart point moved),
#      the two routes must agree on the exact ADDRESS SET of the mismatches -- this proves
#      the fast route reports WHERE a break is, which is what a real break would need;
#  (d) the mismatch matrix must be SYMMETRIC (S_h and S_n are symmetric in (c1,c2) because
#      zeta^(m1 m2) is), checked on the nontrivial corrupted matrix of (c).
# ======================================================================================

def corrupt_levels(L, cbad):
    """move ONE nonzero of level column cbad by one chart step: a deliberate break."""
    cols = [dict(c) for c in L.icols]
    keys = sorted(cols[cbad])
    m = keys[0]
    v = cols[cbad].pop(m)
    cols[cbad][(m + 1) % L.N] = v
    return cols


def r1_cross_validate(levels):
    print("=" * 100)
    print("R1.  THE TWO ROUTES, CROSS-VALIDATED ENTRY BY ENTRY BEFORE ROUTE B IS USED")
    print("=" * 100)
    print("      ROUTE A = b26's own inner loop (coefficient dictionaries, b26.ZD imported")
    print("                unchanged).  ROUTE B = the same 40 folded terms per entry, done")
    print("                a Gram row at a time in exact int64 arrays with an exact")
    print("                sorted-key zero test.  NO TOLERANCE ANYWHERE.")
    print()
    for L in levels:
        n, d = L.n, L.d
        h = n + 1
        Nh = P ** (2 * h)
        deg = 2 * (Nh // P)
        t = Nh // P
        Mh, Vh, Mn, Vn, widths, ich = build_arrays(L, h)
        check("R1a n=%d  the embedded columns have exactly 6 nonzeros each (2 Sonin "
              "nonzeros x 3 = p host cells), all %d of them; the level columns have 2"
              % (n, d), widths == {6} and all(len(c) == 2 for c in L.icols))
        hostl = [list(x.items()) for x in ich]
        levl = [list(L.icols[c].items()) for c in range(d)]

        t0 = time.time()
        A = route_A_matrix(hostl, levl, Nh)
        elA = time.time() - t0
        t0 = time.time()
        Bm = np.array([route_B_row(c1, Mh, Vh, Mn, Vn, Nh, deg, t) for c1 in range(d)])
        elB = time.time() - t0
        Am = np.array([A[c1] for c1 in range(d)])
        check("R1b n=%d  ROUTE A == ROUTE B on ALL %d x %d = %d entries of the real "
              "comparison (A: %.1f s, B: %.1f s; speedup %.1fx) -- and both find %d "
              "mismatches" % (n, d, d, d * d, elA, elB, elA / max(elB, 1e-9),
                              int(Am.sum())), bool(np.array_equal(Am, Bm)))

        # negative control 1: the wrong mass constant
        A3d = route_A_matrix(hostl, levl, Nh, scale=3)
        A3 = np.array([A3d[c1] for c1 in range(d)])
        B3 = np.array([route_B_row(c1, Mh, Vh, Mn, Vn, Nh, deg, t, scale=3)
                       for c1 in range(d)])
        check("R1c n=%d  NEGATIVE CONTROL (mass constant 3 instead of 9): both routes "
              "flag the SAME %d entries (nonempty: %s) -- the test is not vacuous"
              % (n, int(A3.sum()), "yes" if A3.sum() > 0 else "NO"),
              bool(np.array_equal(A3, B3)) and A3.sum() > 0)

        # negative control 2: one corrupted level column -> an ADDRESS SET
        cbad = min(5, d - 1)
        badcols = corrupt_levels(L, cbad)
        levl2 = [list(c.items()) for c in badcols]
        Mn2 = np.array([sorted(c) for c in badcols], dtype=np.int64)
        Vn2 = np.array([[c[m] for m in sorted(c)] for c in badcols], dtype=np.int64)
        Acd = route_A_matrix(hostl, levl2, Nh)
        Ac = np.array([Acd[c1] for c1 in range(d)])
        Bc = np.array([route_B_row(c1, Mh, Vh, Mn2, Vn2, Nh, deg, t) for c1 in range(d)])
        rows_hit = sorted(set(int(i) for i in np.nonzero(Ac.any(axis=1))[0]))
        check("R1d n=%d  NEGATIVE CONTROL (level column %d corrupted by one chart step): "
              "both routes agree on the EXACT ADDRESS SET -- %d entries spread over %d "
              "distinct rows (the full cross of row %d with column %d would be "
              "2d - 1 = %d entries) -- so the fast route reports WHERE a break is, not "
              "merely THAT there is one"
              % (n, cbad, int(Ac.sum()), len(rows_hit), cbad, cbad, 2 * d - 1),
              bool(np.array_equal(Ac, Bc)) and Ac.sum() > 0)
        check("R1e n=%d  the mismatch matrix is SYMMETRIC on the corrupted control "
              "(S_h and S_n are symmetric in (c1,c2) since zeta^(m1 m2) is) -- so the "
              "upper triangle would have sufficed; it is NOT used, the FULL square is "
              "computed below" % n, bool(np.array_equal(Ac, Ac.T)))
    print()
    sys.stdout.flush()


# ======================================================================================
# R2.  b26's OWN T2 FUNCTION, RUN HERE AT n = 1..3.
#
# The strongest available spot-check that this file reproduces b26's exact T2 result is
# to CALL b26's t2_pairing itself on levels 1..3 with a budget it can meet, and read its
# ledger.  b26 is imported, not modified; only its in-memory LEDGER is appended to, and
# that snapshot is taken and reported here.
# ======================================================================================

def r2_b26_itself(levels):
    print("=" * 100)
    print("R2.  b26's OWN t2_pairing() CALLED DIRECTLY AT n = 1..3 (b26 IMPORTED, NOT "
          "MODIFIED)")
    print("=" * 100)
    before = len(b26.LEDGER)
    b26.t2_pairing(levels, 3600.0)
    got = b26.LEDGER[before:]
    print()
    print("      b26's own ledger lines produced by that call:")
    for nm, ok in got:
        print("        %-6s %s" % ("PASS" if ok else "FAIL", nm[:150]))
    print("      b26's DECLARED lines produced by that call: %d"
          % len([x for x in b26.DECLARED]))
    print()
    check("R2a  b26's OWN t2_pairing() ran at n = 1..3 and produced %d T2 lines, ALL "
          "PASS in b26's own ledger -- this file reproduces b26's exact T2 result "
          "because it CALLS b26's code path, unmodified" % len(got),
          len(got) == len(levels) and all(ok for _, ok in got))
    print()
    sys.stdout.flush()


# ======================================================================================
# R3.  THE DECLARED-SKIPPED CELL: T2 AT n = 4, ALL 6400^2 = 40,960,000 ENTRIES.
# ======================================================================================

def r3_level4(budget):
    n = TARGET_LEVEL
    h = n + 1
    L = Level(n)
    d = L.d
    Nh = P ** (2 * h)
    deg = 2 * (Nh // P)
    tt = Nh // P
    total = d * d
    print("=" * 100)
    print("R3.  T2 AT n = %d -- THE CELL b26 DECLARED-SKIPPED" % n)
    print("=" * 100)
    print("      level n = %d: q = 3^%d = %d, N = 9^%d = %d, dim Son(3,%d) = (%d - 1)^2 "
          "= %d" % (n, n, L.q, n, L.N, n, L.q, d))
    print("      host h = %d: N_h = 9^%d = %d = 3^%d, field Q(zeta_(3^%d)) of degree "
          "2*3^%d = %d" % (h, h, Nh, 2 * h, 2 * h, 2 * h - 1, deg))
    print("      entries to sweep: %d x %d = %s (each a 36-term host zeta sum against a "
          "9-scaled 4-term lifted level sum)" % (d, d, "{:,}".format(total)))
    print("      BUDGET, SET BEFORE RUNNING: %.0f s.  b26's projection at its own entry "
          "rate was 591 s against its registered 420 s." % budget)
    print()
    print("      ROUTE NOTE, said plainly: the sweep below is ROUTE B (R1: cross-validated")
    print("      against b26's own route entry by entry at n = 1, 2, 3, including two")
    print("      negative controls where both routes must agree on the mismatch ADDRESSES).")
    print("      It is EXACT INTEGER ARITHMETIC throughout -- the same power basis, the")
    print("      same two-term p = 3 fold, an exact sorted-key zero test, no tolerance.")
    print("      THE FULL SQUARE IS COMPUTED, both triangles: the symmetry of the Gram")
    print("      (R1e) would have licensed halving the work, and it is NOT used -- the")
    print("      route is fast enough that the stronger sweep fits the budget.")
    print()
    sys.stdout.flush()

    Mh, Vh, Mn, Vn, widths, ich = build_arrays(L, h)
    check("R3a n=%d  the %d embedded columns each have exactly 6 nonzeros; the %d level "
          "columns each have 2" % (n, d, d),
          widths == {6} and all(len(c) == 2 for c in L.icols))

    # a reference-route cross-check AT n = 4 ITSELF (the field changes with the level).
    # ROUTE A is run on WHOLE RANDOM GRAM ROWS through route_A_matrix -- b26's own tight
    # double loop -- so the entry rate printed below is comparable with b26's projection.
    nrows = max(1, SAMPLE_N4 // d)
    rng = np.random.default_rng(20260818)
    rrows = sorted(set(int(v) for v in rng.integers(0, d, size=nrows)))
    hostl = [list(x.items()) for x in ich]
    levl = [list(L.icols[c].items()) for c in range(d)]
    t0 = time.time()
    Asub = route_A_matrix(hostl, levl, Nh, rows=rrows)
    elS = time.time() - t0
    nent = len(rrows) * d
    agree = True
    nbadA = 0
    for c1 in rrows:
        av = np.array(Asub[c1])
        nbadA += int(av.sum())
        bv = route_B_row(c1, Mh, Vh, Mn, Vn, Nh, deg, tt)
        if not np.array_equal(av, bv):
            agree = False
            for c2 in np.nonzero(av != bv)[0][:4]:
                print("      *** ROUTE DISAGREEMENT at entry (%d, %d): A=%s B=%s"
                      % (c1, int(c2), bool(av[c2]), bool(bv[c2])))
    check("R3b n=%d  ROUTE A == ROUTE B on %d COMPLETE RANDOM GRAM ROWS = %s entries "
          "drawn at n = 4 ITSELF (the field Q(zeta_(3^10)) is NOT the field the n <= 3 "
          "cross-validation used), and ROUTE A finds %d mismatches among them [%.1f s]"
          % (n, len(rrows), "{:,}".format(nent), nbadA, elS), agree and nbadA == 0)
    # the reference route's own rate, so b26's 591 s projection is visible as measured
    rateA = elS / float(nent)
    print("      ROUTE A's measured entry rate here (b26's own inner loop, whole rows): "
          "%.2e s/entry" % rateA)
    print("      -> the full n = 4 square by ROUTE A alone would be %.0f s on this "
          "machine.  b26's registered projection was 591 s; the two are the same order,"
          % (rateA * total))
    print("      and either way the point stands: ROUTE A does not fit a 420 s budget, "
          "which is why b26 declared the skip rather than quietly running it.")
    print()
    sys.stdout.flush()

    rows_per_progress = max(1, PROGRESS_ENTRIES // d)
    t0 = time.time()
    done_rows = 0
    nbad = 0
    first_bad = []
    out_of_budget = False
    for c1 in range(d):
        bad = route_B_row(c1, Mh, Vh, Mn, Vn, Nh, deg, tt)
        if bad.any():
            for c2 in np.nonzero(bad)[0]:
                if len(first_bad) < 8:
                    first_bad.append((c1, int(c2)))
            nbad += int(bad.sum())
        done_rows += 1
        if done_rows % rows_per_progress == 0 or done_rows == d:
            el = time.time() - t0
            ent = done_rows * d
            print("      progress: %s / %s entries (%.2f%%), %.1f s elapsed, "
                  "%.0f s projected total, mismatches so far: %d"
                  % ("{:,}".format(ent), "{:,}".format(total), 100.0 * ent / total,
                     el, el * d / float(done_rows), nbad))
            sys.stdout.flush()
        if time.time() - t0 > budget:
            out_of_budget = True
            break
    el = time.time() - t0
    done = done_rows * d
    print()

    if out_of_budget:
        dnote("T2 n=%d  STILL-DECLARED: the sweep exceeded the budget of %.0f s at "
              "%s / %s entries (%.2f%% of the square) with %d mismatches so far.  NOT "
              "completed, NOT counted as EXACT, NOT asserted."
              % (n, budget, "{:,}".format(done), "{:,}".format(total),
                 100.0 * done / total, nbad))
        return dict(level=n, d=d, total=total, done=done, elapsed=el, nbad=nbad,
                    first_bad=first_bad, closed=False, budget=budget)

    ok = (nbad == 0)
    check("T2  n=%d  the host Gram (iota K)^T W_h F_h (iota K) equals the level-%d Gram "
          "K^T W_n F_n K ENTRY-EXACT on ALL %d x %d = %s entries -- the pairing is "
          "LEVEL-STABLE ON THE NOSE (no scalar) at the level b26 declared-skipped "
          "[%.1f s of a %.0f s budget]"
          % (n, n, d, d, "{:,}".format(total), el, budget), ok)
    if first_bad:
        print("      MISMATCHED ENTRIES (first, by address (c1, c2) = (shell,diff) pairs):")
        for c1, c2 in first_bad:
            a1, j1 = L.blk(c1)
            a2, j2 = L.blk(c2)
            print("        (%d, %d) = shell/diff (a=%d, j=%d) x (a=%d, j=%d)"
                  % (c1, c2, a1, j1, a2, j2))
    return dict(level=n, d=d, total=total, done=done, elapsed=el, nbad=nbad,
                first_bad=first_bad, closed=ok, budget=budget)


# ======================================================================================
# MAIN
# ======================================================================================

def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100)
    print("W-ATTEMPT-2 SITTING 12 (item 3) -- REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()
    if what == "register":
        return

    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    sys.stdout.flush()
    t_start = time.time()

    levels = [Level(n) for n in LEVELS_CROSS]
    print("LEVELS BUILT (cross-validation): " +
          ", ".join("n=%d (q=%d, N=%d, dim Son=%d)" % (L.n, L.q, L.N, L.d)
                    for L in levels))
    print("TARGET CELL: n = %d (q = %d, N = %d, dim Son = %d, host N_h = 9^%d = %d)"
          % (TARGET_LEVEL, P ** TARGET_LEVEL, P ** (2 * TARGET_LEVEL),
             (P ** TARGET_LEVEL - 1) ** 2, TARGET_LEVEL + 1,
             P ** (2 * (TARGET_LEVEL + 1))))
    print("BUDGET, SET BEFORE RUNNING: %.0f s (b26's was 420 s and its projection 591 s)"
          % BUDGET_SECONDS)
    print()
    sys.stdout.flush()

    r1_cross_validate(levels)
    r2_b26_itself(levels)

    if FAILS:
        print("=" * 100)
        print("THE CROSS-VALIDATION DID NOT LAND -- ROUTE B IS NOT LICENSED AND THE n = 4 "
              "SWEEP IS NOT RUN.")
        print("=" * 100)
        for nm in FAILS:
            print("    FAIL  %s" % nm)
        dnote("T2 n=4  STILL-DECLARED: the fast route failed its cross-validation "
              "against b26's own route; the sweep was NOT run.")
        res = None
    else:
        res = r3_level4(BUDGET_SECONDS)

    print()
    print("=" * 100)
    print("THE BRANCH")
    print("=" * 100)
    if res is not None and res["closed"]:
        print("  BRANCH LANDED: (closed)")
        print("  The sweep completed WITHIN BUDGET (%.1f s of %.0f s) and landed "
              "ENTRY-EXACT:" % (res["elapsed"], res["budget"]))
        print("  all %s Gram entries at n = 4 satisfy S_h = 9 S_n exactly, with ZERO "
              "mismatches." % "{:,}".format(res["total"]))
        print()
        print("  CONSEQUENCE, stated exactly and no further: the p = 3 tower's T2 -- the")
        print("  pairing level-stable ON THE NOSE under the stated mass normalization --")
        print("  is EXACT AT ALL LEVELS n = 1, 2, 3, 4.  THE DECLARED-SKIP IS RETIRED:")
        print("  sitting 11's one honestly-skipped cell is now computed, and it landed as")
        print("  the other three did.  Nothing else about the tower changes; no claim is")
        print("  extended past n = 4, and the inductive limit remains NAMED, not built.")
    elif res is not None and res["nbad"] > 0:
        print("  BRANCH LANDED: (still-declared) -- WITH A MISMATCH.  *** THIS IS A "
              "FINDING ***")
        print("  %d of the %s entries at n = 4 do NOT satisfy S_h = 9 S_n.  This is the "
              "FIRST BREAK in the p = 3 tower structure and it is reported at its entry "
              "address, unsmoothed:" % (res["nbad"], "{:,}".format(res["total"])))
        for c1, c2 in res["first_bad"]:
            print("    entry (c1, c2) = (%d, %d)" % (c1, c2))
        print("  NOTHING IS INFERRED FROM IT HERE: it is recorded as found, at bench "
              "grade, and the register is untouched.")
    else:
        print("  BRANCH LANDED: (still-declared)")
        if res is not None:
            print("  The sweep exceeded even the %.0f s budget: %s of %s entries "
                  "(%.2f%%) completed in %.1f s, with ZERO mismatches among them."
                  % (res["budget"], "{:,}".format(res["done"]),
                     "{:,}".format(res["total"]),
                     100.0 * res["done"] / res["total"], res["elapsed"]))
            print("  The fraction completed is the datum; NO claim is made about the "
                  "remainder, and the cell stays declared-skipped.")
        else:
            print("  Route B was not licensed by its cross-validation, so the n = 4 sweep "
                  "was not run at all.  The cell stays declared-skipped.")
    print()
    print("=" * 100)
    print("SCOPE, said plainly: this is an EXACT property of a FINITE CONSTRUCTED OBJECT "
          "on Q_3.")
    print("No sign is asserted; no register moves; W_inf - Sum W_p at complete roster is "
          "NOT touched.")
    print("=" * 100)
    print()

    if FAILS:
        print("*** LINES THAT DID NOT LAND AS REGISTERED (%d) ***" % len(FAILS))
        for nm in FAILS:
            print("    FAIL  %s" % nm)
        print()
    else:
        print("NOTHING FAILED TO LAND: every EXACT line landed as registered.")
        print()
    print("DECLARED LINES (skipped or out of budget; NEVER counted as EXACT): %d"
          % len(DECLARED))
    for nm in DECLARED:
        print("    DECLARED  %s" % nm)
    print()
    n_ok = sum(1 for _, ok in LEDGER if ok)
    n_all = len(LEDGER)
    print("TOTAL RUNTIME: %.1f s" % (time.time() - t_start))
    print()
    if res is not None and res["closed"] and not FAILS:
        print("ALL EXACT LINES EXACT: %d/%d PASS" % (n_ok, n_all))
    else:
        print("STILL-DECLARED REPORT: %d/%d exact lines PASS; the n = 4 cell is NOT "
              "closed (see the DECLARED lines above)." % (n_ok, n_all))


if __name__ == "__main__":
    main()
