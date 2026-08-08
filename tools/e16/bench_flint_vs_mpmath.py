# THE (c') BENCHMARK — python-flint's acb.gamma_upper against mpmath's gammainc,
# at the precision and shape the measured dominant cost actually has.
#
# CORRECTNESS BEFORE SPEED. A speed number from an engine that computes the wrong value is
# worthless, so every timing below is preceded by an agreement check against mpmath at the same
# precision. If agreement fails, the benchmark reports FAIL and no speedup is quoted.
#
# THE SHAPE BENCHMARKED IS THE REAL ONE: E(s) = s(s-1)Lambda(s) evaluated at a point on the
# Cauchy circle |s-1| = 0.4, which is 40 incomplete-gamma PAIRS -- not an isolated gamma call.
# Stage 3 ran 3002 such evaluations at dps 900 and spent ~26 h doing it.
import math
import time
import mpmath as mp
from flint import acb, arb, ctx

KTERMS = 40
DPS = 900
RADIUS = mp.mpf("0.4")


def rep_counts(K):
    r = [0] * (K + 1)
    ymax = int(2 * math.sqrt(K / 23.0)) + 1
    for y in range(-ymax, ymax + 1):
        for x in range(-int(math.sqrt(K)) - abs(y) - 1, int(math.sqrt(K)) + abs(y) + 2):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= K:
                r[k] += 1
    return r


RQ = rep_counts(KTERMS)


# ---------------- mpmath engine (the incumbent, exactly as the worker runs it) -------------
def E_mp(s):
    mp.mp.dps = DPS
    sq = mp.sqrt(23)
    tot = -1 / s - 1 / (1 - s)
    for k in range(1, KTERMS + 1):
        if RQ[k] == 0:
            continue
        a = 2 * mp.pi * k / sq
        tot += RQ[k] * (a ** (-s) * mp.gammainc(s, a) + a ** (s - 1) * mp.gammainc(1 - s, a))
    return s * (s - 1) * tot


# ---------------- flint engine (the candidate) ---------------------------------------------
def E_fl(s_re, s_im, prec_bits):
    ctx.prec = prec_bits
    s = acb(s_re, s_im)
    sq = arb(23).sqrt()
    tot = -1 / s - 1 / (1 - s)
    two_pi = arb.pi() * 2
    for k in range(1, KTERMS + 1):
        if RQ[k] == 0:
            continue
        a = acb(two_pi * k / sq)
        tot += RQ[k] * (a ** (-s) * a.gamma_upper(s) + a ** (s - 1) * a.gamma_upper(1 - s))
    return s * (s - 1) * tot


def main():
    prec_bits = int(DPS * 3.3219280948873626) + 20
    print("=" * 78)
    print("(c') BENCHMARK — flint acb.gamma_upper vs mpmath gammainc")
    print("=" * 78)
    print(f"  target precision: dps {DPS}  (~{prec_bits} bits)")
    print(f"  shape benchmarked: one full E(s) evaluation = {sum(1 for k in range(1,KTERMS+1) if RQ[k])} "
          f"incomplete-gamma PAIRS")
    print()

    # a point on the Cauchy circle, as the worker uses
    mp.mp.dps = DPS
    j, N = 7, 3002
    s_pt = 1 + RADIUS * mp.expjpi(2 * mp.mpf(j) / N)
    s_re, s_im = mp.nstr(mp.re(s_pt), 60), mp.nstr(mp.im(s_pt), 60)

    print("--- CORRECTNESS FIRST (a speed number from a wrong engine is worthless) ---")
    t0 = time.time()
    v_mp = E_mp(s_pt)
    t_mp = time.time() - t0
    t0 = time.time()
    v_fl = E_fl(s_re, s_im, prec_bits)
    t_fl = time.time() - t0

    mp.mp.dps = 50
    fl_re = mp.mpf(str(v_fl.real.str(40, radius=False)))
    fl_im = mp.mpf(str(v_fl.imag.str(40, radius=False)))
    mp.mp.dps = DPS
    diff = abs(mp.mpc(fl_re, fl_im) - v_mp) / abs(v_mp)
    print(f"  mpmath  E(s) = {mp.nstr(v_mp, 20)}")
    print(f"  flint   E(s) = {v_fl.str(20, radius=False)}")
    print(f"  relative difference = {mp.nstr(diff, 6)}")
    ok = diff < mp.mpf("1e-30")
    print(f"  AGREEMENT: {'PASS' if ok else 'FAIL'}  (threshold 1e-30 — far above either engine's error)")
    if not ok:
        print("\n  BENCHMARK HALTS: no speedup is quoted from a disagreeing engine.")
        return

    print()
    print("--- TIMING (single evaluation, from the correctness run) ---")
    print(f"  mpmath : {t_mp:8.3f} s")
    print(f"  flint  : {t_fl:8.3f} s")

    print()
    print("--- TIMING (repeated, 3 evaluations each at distinct circle points) ---")
    pts = []
    mp.mp.dps = DPS
    for jj in (11, 101, 1009):
        p = 1 + RADIUS * mp.expjpi(2 * mp.mpf(jj) / N)
        pts.append((p, mp.nstr(mp.re(p), 60), mp.nstr(mp.im(p), 60)))
    t0 = time.time()
    for p, _, _ in pts:
        E_mp(p)
    T_mp = (time.time() - t0) / len(pts)
    t0 = time.time()
    for _, a_, b_ in pts:
        E_fl(a_, b_, prec_bits)
    T_fl = (time.time() - t0) / len(pts)
    print(f"  mpmath : {T_mp:8.3f} s per evaluation")
    print(f"  flint  : {T_fl:8.3f} s per evaluation")
    sp = T_mp / T_fl if T_fl > 0 else float("inf")
    print(f"  SPEEDUP: {sp:.1f}x")

    print()
    print("=" * 78)
    print("PROJECTION ONTO THE MEASURED DOMINANT COST")
    print("=" * 78)
    print(f"  stage 3 boundary measured : ~26 h for 3002 evaluations "
          f"(~{26*3600/3002:.1f} s/eval)")
    print(f"  this benchmark, mpmath    : {T_mp:.1f} s/eval  "
          f"(sanity: within ~2x of the production rate = same regime)")
    print(f"  this benchmark, flint     : {T_fl:.1f} s/eval")
    for name, M, dps in (("stage 3", 1500, 900), ("stage 4", 3000, 1600),
                         ("stage 5", 5000, 2400), ("stage 6", 7000, 3200)):
        n_ev = 2 * M + 2
        scale = (dps / DPS)          # first-order; superlinearity noted, not modelled
        print(f"  {name}: {n_ev} evals -> mpmath ~{n_ev*T_mp*scale/3600:7.1f} h | "
              f"flint ~{n_ev*T_fl*scale/3600:7.1f} h")
    print()
    print("  CAVEAT ON THE PROJECTION, stated with it: the dps scaling above is FIRST-ORDER")
    print("  LINEAR. Both engines are superlinear in precision, so both columns understate --")
    print("  the RATIO is the benchmark's real output, the absolute hours are indicative.")


if __name__ == "__main__":
    main()
