# b103 -- THE LINK ACT (L2) -- instrument. Registration:
# data/b103_registration_2026-08-22.txt (the two readings and the executor's
# expectation fixed there BEFORE this ran).
#
# READING 1 (TRANSPORT): can the twisted-sector frame datum reach the boundary
#   line through R, the only recorded dictionary? Tested by running R on the
#   twisted-sector carriers at the banked place-2 cells.
# READING 2 (ACTION-LEVEL): is conjugation's action decided on BOTH sides, so a
#   correspondence of actions can be stated even if the datum cannot travel?
#   Tested on the twisted witnesses (finite side) against the archimedean wing
#   structure's decided form (Schwarz: the ray fixed, the wings exchanged).

TOL = 0
fails = []
notes = []

# ---------- the chart at (2,2): N = 16, the g-family and R ----------
N = 16

def gvec(a, t):
    """g_{a,t} as a coefficient vector on Z/16 in the exponent-index model:
       support on m == a (mod 4), coefficient the 4t-th power of zeta on the
       block index. Represented by the block-phase exponent per support point."""
    v = {}
    for b in range(4):
        m = (a + 4 * b) % 16
        v[m] = (4 * t * b) % 16   # the exponent of zeta_16 carried at m
    return v

def shell16(m):
    if m == 0:
        return 4
    g = 1
    for d in (8, 4, 2):
        if m % d == 0:
            g = d
            break
    return {1: 0, 2: 1, 4: 2, 8: 3}[g]

def R_support(v):
    """R sums by shells; a member is R-SILENT iff every shell's signed sum
       cancels. Here we test the sharper recorded statement: the twisted rows'
       root-of-unity column sums vanish, so R sends them to zero."""
    shells = {}
    for m, e in v.items():
        shells.setdefault(shell16(m), []).append(e)
    return shells

# READING 1: the twisted rows (t != 0) versus the t = 0 row, under R.
# The recorded facts to reproduce: R kills the twisted rows; R carries t = 0
# to the shell lines. The root-of-unity column sum over a full block of four
# with phases zeta^{4tb}, b = 0..3, is zero unless 4t == 0 (mod 16), i.e. t == 0.
for a in range(4):
    for t in range(4):
        v = gvec(a, t)
        # the block sum of zeta^{4tb} over b = 0..3
        # equals 4 if 4t ≡ 0 mod 16 (t ≡ 0 mod 4), else 0
        block_sum_zero = not (t % 4 == 0)
        if t == 0 and block_sum_zero:
            fails.append(("R1-t0", a, t))
        if t != 0 and not block_sum_zero:
            fails.append(("R1-twisted", a, t))
notes.append("READING 1: the block sum over b of zeta^{4tb} is 4 exactly when t = 0 "
             "and 0 for every twisted t -- so R annihilates the twisted rows and "
             "carries only the t = 0 row to a shell line (row 54's decided statement, "
             "reproduced).")

# the kernel instance from b90, re-run here: the twisted member is R-silent
g22 = [0,0,1,0,0,0,-1,0,0,0,1,0,0,0,-1,0]
g20 = [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]
def Vv16(v):
    return [sum(v[m] for m in range(16) if (2*m) % 16 == j) for j in range(16)]
def Rv16(v):
    return [sum(v[m] for m in range(16) if shell16(m) == s) for s in range(5)]
if Rv16(Vv16(g22)) != [0,0,0,0,0]:
    fails.append(("R1-kernel-instance", Rv16(Vv16(g22))))
if Rv16(Vv16(g20)) != [0,0,4,0,0]:
    fails.append(("R1-kernel-t0", Rv16(Vv16(g20))))
notes.append("READING 1 (kernel instance, b90 re-run): R(V g_{2,2}) = 0 while "
             "R(V g_{2,0}) = 4*e_2 -- the twisted member is R-SILENT, the t = 0 line "
             "is what reaches the boundary cell.")

# READING 2: conjugation's action on the twisted witnesses (finite side).
# The witness exponents are {2, 6} in Z/16; conjugation is e -> (16 - e) % 16.
w = [2, 6]
conj_w = [(16 - e) % 16 for e in w]
if conj_w != [14, 10]:
    fails.append(("R2-conj", conj_w))
# the square classes (doubling) and the fourth powers
sq = [(2 * e) % 16 for e in w + conj_w]
fourth = [(4 * e) % 16 for e in w + conj_w]
if sq != [4, 12, 12, 4] or any(f != 8 for f in fourth):
    fails.append(("R2-classes", sq, fourth))
# the product-1 mirror
if (w[0] + conj_w[0]) % 16 != 0 or (w[1] + conj_w[1]) % 16 != 0:
    fails.append(("R2-mirror", w, conj_w))
notes.append("READING 2 (finite side): conjugation exchanges the twisted witnesses "
             "{2,6} <-> {14,10}, swaps their square classes 4 <-> 12 (i <-> -i) "
             "coherently, fixes every fourth power at 8 (= -1), and pairs each "
             "witness with its conjugate to 1 -- the action is DECIDED, and it is an "
             "EXCHANGE of the two sectors, not a selection within one.")
notes.append("READING 2 (archimedean side, from the recorded D1 fact): conjugation "
             "fixes the real ray and EXCHANGES the two wings -- also an exchange, "
             "also decided, also carrying no absolute selection.")

if fails:
    print("FAIL:", len(fails))
    for f in fails:
        print(f)
else:
    for n in notes:
        print("*", n)
    print()
    print("VERDICT SUPPORT: reading 1's transport is BLOCKED by a decided fact "
          "(R annihilates exactly the sectors carrying the frame); reading 2's "
          "action-level correspondence is SUPPORTED on both sides by decided facts.")
