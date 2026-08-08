# SECOND BENCHMARK — the COEFFICIENT phase, because Amdahl's law decides the real gain.
#
# The first benchmark showed 242x on the boundary phase, which is 87% of stage 3's cost.
# With 13% unaccelerated the total gain is capped at ~7.5x -- so the coefficient phase must be
# measured too, or the headline number is an inflation of the kind this corpus keeps catching.
#
# The coefficient inner loop is:  c_m = Re( (1/N) * sum_j vals[j] * expjpi(-2*m*j/N) / r^m )
# i.e. N complex multiplications plus N transcendental expjpi evaluations, per coefficient.
import time
import mpmath as mp
from flint import acb, arb, ctx

DPS = 900
PREC = int(DPS * 3.3219280948873626) + 20
N = 400          # scaled-down N; the RATIO is what transfers, not the absolute
TRIALS = 2

print("=" * 78)
print("COEFFICIENT-PHASE BENCHMARK — the 13% that Amdahl says decides the outcome")
print("=" * 78)
print(f"  dps {DPS} (~{PREC} bits), N = {N} terms per coefficient, {TRIALS} coefficients")
print()

mp.mp.dps = DPS
vals_mp = [mp.mpc(mp.cos(mp.mpf(j) / 7), mp.sin(mp.mpf(j) / 11)) for j in range(N)]
ctx.prec = PREC
vals_fl = [acb(arb(j) / 7).cos() + acb(0, 1) * acb(arb(j) / 11).sin() for j in range(N)]

# ---- mpmath ----
mp.mp.dps = DPS
t0 = time.time()
res_mp = []
for m in range(1, TRIALS + 1):
    acc = mp.mpc(0)
    for j in range(N):
        acc += vals_mp[j] * mp.expjpi(-2 * mp.mpf(m * j) / N)
    res_mp.append(mp.re(acc / N))
T_mp = (time.time() - t0) / TRIALS

# ---- flint ----
ctx.prec = PREC
t0 = time.time()
res_fl = []
for m in range(1, TRIALS + 1):
    acc = acb(0)
    for j in range(N):
        th = arb(-2 * m * j) / N
        acc += vals_fl[j] * acb(0, arb.pi() * th).exp()
    res_fl.append((acc / N).real)
T_fl = (time.time() - t0) / TRIALS

print("--- CORRECTNESS FIRST ---")
mp.mp.dps = 60
a = mp.mpf(str(res_fl[0].str(40, radius=False)))
mp.mp.dps = DPS
d = abs(a - res_mp[0]) / max(abs(res_mp[0]), mp.mpf("1e-300"))
print(f"  mpmath c_1 = {mp.nstr(res_mp[0], 20)}")
print(f"  flint  c_1 = {res_fl[0].str(20, radius=False)}")
print(f"  relative difference = {mp.nstr(d, 6)}")
ok = d < mp.mpf("1e-30")
print(f"  AGREEMENT: {'PASS' if ok else 'FAIL'}")
print()
print("--- TIMING (per coefficient, N = %d) ---" % N)
print(f"  mpmath : {T_mp:8.3f} s")
print(f"  flint  : {T_fl:8.3f} s")
sp = T_mp / T_fl if T_fl > 0 else float("inf")
print(f"  SPEEDUP: {sp:.1f}x")
print()
print("=" * 78)
print("AMDAHL, WITH BOTH PHASES MEASURED")
print("=" * 78)
BOUND_SP = 242.1
frac_b, frac_c = 0.87, 0.13
tot = 1.0 / (frac_b / BOUND_SP + frac_c / sp)
print(f"  boundary phase   : 87% of stage-3 cost, measured speedup {BOUND_SP:.0f}x")
print(f"  coefficient phase: 13% of stage-3 cost, measured speedup {sp:.1f}x")
print(f"  COMBINED (Amdahl): {tot:.1f}x")
print()
print("  Stage-3-equivalent: ~29.5 h  ->  ~%.1f h" % (29.5 / tot))
print("  Cumulative to n = 7000: ~48 days  ->  ~%.1f days" % (48.0 / tot))
print()
print("  The combined figure is the one to quote. The 242x is a phase result, not a")
print("  project result, and quoting it alone would overstate the gain by the ratio of")
print("  the two numbers.")
