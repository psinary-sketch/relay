# E-25, corrected test (the previous residual was circular by construction and is void).
# NON-CIRCULAR: build a SURROGATE control from zeta's OWN zeros shifted by a constant
# gamma-offset D (the measured mean of gc - gz in the band).  The surrogate has zeta's
# exact fluctuation structure and only the offset; if the measured c is reproduced by the
# surrogate, the statistic is driven by the control's construction offset, not by pair
# correlation.  Then the residual (measured c - surrogate c) is the honest fluctuation part.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 50

def load(p, n):
    with open(p) as f:
        return [mp.mpf(l.strip()) for l in f if l.strip()][:n]

gz = load(os.path.join(T, "k256_zeros.txt"), 1200)
gc = load(os.path.join(T, "k256_smooth.txt"), 1200)

def stat(bA, bB, R):
    s = mp.mpf(0); h = mp.mpf(0)
    for i in range(2, R):
        for j in range(i + 1, R):
            s += 2 * (mp.log(abs(bA[i] - bA[j])) - mp.log(abs(bB[i] - bB[j])))
            h += mp.mpf(1) / (j - i)
    return s / h

print(f"{'R':>5} {'c measured':>12} {'c surrogate':>13} {'share':>8} {'c residual':>12} {'D used':>8}")
for R in (36, 75, 118, 153):
    D = sum(gc[i] - gz[i] for i in range(2, R)) / (R - 2)      # mean offset in the band
    bz = [1 / (2 * g) ** 2 for g in gz]
    bc = [1 / (2 * g) ** 2 for g in gc]
    bs = [1 / (2 * (g + D)) ** 2 for g in gz]                   # surrogate: zeta shifted by D
    c_meas = stat(bz, bc, R)
    c_surr = stat(bz, bs, R)
    print(f"{R:>5} {mp.nstr(c_meas,6):>12} {mp.nstr(c_surr,6):>13} "
          f"{mp.nstr(c_surr/c_meas,4):>8} {mp.nstr(c_meas - c_surr,4):>12} {mp.nstr(D,4):>8}")
print("\nsurrogate = zeta's own zeros with ONLY a constant gamma-offset; it carries no")
print("difference in fluctuation structure at all.  Its share of the measured c is the")
print("share of the statistic explained by the control's construction offset.")
