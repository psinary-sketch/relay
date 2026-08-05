# E-25 supporting computation (atoms only, no factorization): decompose the measured
# statistic into (a) a uniform SCALE/OFFSET part and (b) the residual fluctuation part.
# Purpose: test the derivation's claim that the pair-correlation content of c is O(1/log L)
# while the measured c is dominated by the systematic offset between the true zeros and the
# smooth-COUNTING control (the S(T)/convention offset).
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 50

def load(p, n):
    with open(p) as f:
        return [mp.mpf(l.strip()) for l in f if l.strip()][:n]

gz = load(os.path.join(T, "k256_zeros.txt"), 1200)
gc = load(os.path.join(T, "k256_smooth.txt"), 1200)
bz = [1 / (2 * g) ** 2 for g in gz]
bc = [1 / (2 * g) ** 2 for g in gc]

for R in (36, 75, 118, 153):
    band = range(2, R)
    npairs = 0
    raw = mp.mpf(0)
    harm = mp.mpf(0)
    for i in band:
        for j in range(i + 1, R):
            raw += 2 * (mp.log(abs(bz[i] - bz[j])) - mp.log(abs(bc[i] - bc[j])))
            harm += mp.mpf(1) / (j - i)
            npairs += 1
    c_raw = raw / harm
    # (a) the uniform-scale part: the single lambda that best explains the whole sum
    lam = mp.e ** (raw / (2 * npairs))
    # (b) the residual after matching scale: rescale the control's betas by lam and redo
    res = mp.mpf(0)
    for i in band:
        for j in range(i + 1, R):
            res += 2 * (mp.log(abs(bz[i] - bz[j])) - mp.log(abs(lam * (bc[i] - bc[j]))))
    c_res = res / harm
    # the measured endpoint scale ratio (independent check on lambda)
    endr = (bz[2] - bz[R-1]) / (bc[2] - bc[R-1])
    # mean gamma offset in the band
    doff = sum(gc[i] - gz[i] for i in band) / (R - 2)
    print(f"R={R:>4} pairs={npairs:>6} | c_raw = {mp.nstr(c_raw,6):>9} | "
          f"lambda_eff = {mp.nstr(lam,6):>8} | endpoint ratio = {mp.nstr(endr,6):>8} | "
          f"c_residual = {mp.nstr(c_res,4):>10} | mean(gc-gz) = {mp.nstr(doff,4)}")
print("\n(c_residual is c with the uniform scale removed — the part a pair-correlation")
print(" derivation could speak to; c_raw is what the c-sequence has been reporting.)")
