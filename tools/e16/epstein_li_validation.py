# THE ARITHMETIC-SIDE VALIDATION â€” Li-type coefficients for the disc -23 Epstein object,
# computed from its FUNCTIONAL EQUATION AND TAYLOR DATA ALONE.
#
# I-7, RE-CONFIRMED AT BOTH STAGES BEFORE THE FIRST COEFFICIENT:
#   STAGE 1 (the statistic): lambda_n = sum_rho [1 - (1-1/rho)^n] contains rho, real parts
#     included.  Perturbing a real part moves it.  PASSES.
#   STAGE 2 (the pipeline): every number below is computed from E(s) = s(s-1)Lambda(s) evaluated
#     on a circle about s = 1.  NO ZERO LOCATION IS AN INPUT AT ANY POINT.  The census
#     (D:\relay\tools\e16\epstein_census_bank.jsonl) is HELD ASIDE and is never read by this
#     file.  PASSES.
#
# THE MATHEMATICS, so the pipeline is checkable:
#   E(s) = s(s-1)Lambda(s) is entire, order 1, E(s) = E(1-s), zeros = Lambda's nontrivial zeros.
#   Under the Cayley map z = 1 - 1/s (s = 1/(1-z), s=1 <-> z=0):
#        log E(1/(1-z)) - log E(1) = sum_{n>=1} (lambda_n / n) z^n
#   With log E(s) = sum_m c_m (s-1)^m and (s-1) = z/(1-z), and [z^n] z^m (1-z)^-m = C(n-1,m-1):
#        lambda_n = n * sum_{m=1..n} c_m * C(n-1, m-1)
#   The binomials are ~2^n while lambda_n ~ n log n, so the cancellation costs ~0.3n digits --
#   this is the same cost Johansson paid, and it is why the run is staged.
#
# RULE 2: per-record banking with fsync; resume-with-validation (every banked record re-parsed
# and field-checked, malformed discarded); self-test banked first and the run halts if it fails;
# restart command stated in the report before launch.
import json
import math
import os
import sys
import mpmath as mp

BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "epstein_li_bank.jsonl")
SQ23 = None
KTERMS = 40
RADIUS = mp.mpf("0.4")


def setup(dps):
    mp.mp.dps = dps
    global SQ23
    SQ23 = mp.sqrt(23)


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


def Lam_eps(s):
    tot = -1 / s - 1 / (1 - s)
    for k in range(1, KTERMS + 1):
        if RQ[k] == 0:
            continue
        a = 2 * mp.pi * k / SQ23
        tot += RQ[k] * (a ** (-s) * mp.gammainc(s, a) + a ** (s - 1) * mp.gammainc(1 - s, a))
    return tot


def E_eps(s):
    return s * (s - 1) * Lam_eps(s)


def E_zeta(s):
    """The classical xi, for the known-answer self-test. Not the object under study."""
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def log_taylor(Efun, M, r):
    """c_m for m = 1..M, where log E(s) = sum_m c_m (s-1)^m, by Cauchy on |s-1| = r."""
    N = 2 * M + 2
    vals, prev, unwrap = [], None, mp.mpf(0)
    for j in range(N):
        th = 2 * mp.pi * j / N
        v = mp.log(Efun(1 + r * mp.expjpi(2 * mp.mpf(j) / N)))
        if prev is not None:
            d = mp.im(v) - prev
            while d > mp.pi:
                d -= 2 * mp.pi
                unwrap -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
                unwrap += 2 * mp.pi
        prev = mp.im(v)
        vals.append(mp.mpc(mp.re(v), mp.im(v) + unwrap))
    c = []
    for m in range(1, M + 1):
        acc = mp.mpc(0)
        for j in range(N):
            acc += vals[j] * mp.expjpi(-2 * mp.mpf(m * j) / N)
        c.append(mp.re(acc / N / r ** m))
    return c


def lambdas(c, nmax):
    """lambda_n = n * sum_m c_m C(n-1, m-1)."""
    out = []
    for n in range(1, nmax + 1):
        acc, binom = mp.mpf(0), mp.mpf(1)
        for m in range(1, n + 1):
            acc += c[m - 1] * binom
            binom = binom * (n - m) / m
        out.append(n * acc)
    return out


def bank(rec):
    with open(BANK, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def load_bank():
    done, kept, dropped = set(), 0, 0
    if not os.path.exists(BANK):
        return done, kept, dropped
    with open(BANK, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if rec.get("kind") == "selftest":
                    kept += 1
                    continue
                for k in ("stage", "nmax", "dps", "min_lambda", "argmin"):
                    if k not in rec:
                        raise ValueError("missing " + k)
                if not math.isfinite(float(rec["min_lambda"])):
                    raise ValueError("non-finite")
                done.add(int(rec["stage"]))
                kept += 1
            except Exception:
                dropped += 1
    return done, kept, dropped


# stages: (nmax, dps) -- precision ~0.3n digits plus headroom
STAGES = [(120, 120), (300, 220), (700, 450), (1500, 900),
          (3000, 1600), (5000, 2400), (7000, 3200), (9000, 4000)]


def main():
    done, kept, dropped = load_bank()
    print(f"[resume] kept={kept} dropped={dropped} stages_done={sorted(done)}", flush=True)

    if kept == 0:
        setup(60)
        c = log_taylor(E_zeta, 8, mp.mpf("0.4"))
        lam = lambdas(c, 3)
        l1 = float(lam[0])
        ref = 0.0230957089661210
        err = abs(l1 - ref) / abs(ref)
        bank({"kind": "selftest", "test": "zeta lambda_1 vs published",
              "got": l1, "ref": ref, "rel_err": err})
        print(f"[selftest] zeta lambda_1 = {l1:.16f} vs {ref:.16f}  rel_err={err:.3e}",
              flush=True)
        if err > 1e-8:
            print("[selftest] FAILED â€” halting before the first Epstein coefficient", flush=True)
            sys.exit(1)

    for si, (nmax, dps) in enumerate(STAGES):
        if si in done:
            continue
        setup(dps)
        print(f"[stage {si}] nmax={nmax} dps={dps} â€” computing Taylor coefficients", flush=True)
        c = log_taylor(E_eps, nmax, RADIUS)
        print(f"[stage {si}] Taylor done; running the recurrence", flush=True)
        lam = lambdas(c, nmax)
        vals = [float(x) for x in lam]
        mn = min(vals)
        am = vals.index(mn) + 1
        firstneg = next((i + 1 for i, v in enumerate(vals) if v < 0), None)
        bank({"kind": "stage", "stage": si, "nmax": nmax, "dps": dps,
              "min_lambda": mn, "argmin": am, "first_negative": firstneg,
              "lambda_1": vals[0], "lambda_last": vals[-1]})
        print(f"[stage {si}] CHECKPOINT nmax={nmax}: running min lambda = {mn:.6g} at n={am}; "
              f"sign of running minimum = {'NEGATIVE' if mn < 0 else 'positive'}; "
              f"first negative index = {firstneg}", flush=True)
    print("[done] all stages complete", flush=True)


if __name__ == "__main__":
    main()
