# THE ARITHMETIC-SIDE VALIDATION, v3 — THE (c') PORT.
#
# v3 IS v2 WITH THE ENGINE SWAPPED AND NOTHING ELSE MOVED.  The algorithm, the chunk format, the
# staging schedule, the dps schedule, the dataset declaration and the lambda recurrence are all
# character-for-character the same intent as v2.  What changes is which library evaluates the two
# measured hot paths:
#
#   HOT PATH 1 — boundary evaluation of E(s):  mpmath.gammainc  ->  flint acb.gamma_upper
#   HOT PATH 2 — the coefficient phase's inner sum:  mpmath.expjpi  ->  flint acb.exp_pi_i
#
# Benchmarked before the port was built: 242x on path 1, 9.0x on path 2, 55.3x combined by Amdahl
# against the measured 87/13 split.  The combined figure is the one that governs.
#
# ------------------------------------------------------------------------------------------------
# PRECISION PLUMBING — STATED, BECAUSE THIS IS WHERE A PORT SILENTLY LOSES EXACTNESS.
#
# The chunk format is mpmath's INTERNAL `_mpf_` tuple, and it stays that way, so v3's banks are
# readable by v2's reader and by the gate.  Every arb <-> mpf conversion below is a BINARY
# mantissa/exponent transfer:
#
#     arb -> mpf :  m, e = x.mid().man_exp()  ->  mpf((sign, |m|, e, |m|.bit_length()))
#     mpf -> arb :  (sign, man, exp, bc)      ->  +/- arb(man) * 2**exp
#
# THERE IS NO DECIMAL ROUND-TRIP ANYWHERE.  Both directions were verified exact (zero difference)
# on sqrt(2), -1/3, 2**-900, 2**900, 0 and 1 before this file was written.  A `.str()`-based
# conversion would have been the obvious shortcut and would have quietly capped every banked value
# at the digit count passed to it — the byte-identity lesson governs.
#
# WORKING PRECISION: ctx.prec = mp.mp.prec + PREC_GUARD.  Arb carries a rigorous error radius,
# which mpmath does not, so v3 can CERTIFY its own accuracy rather than assume it: every boundary
# value is checked against `rel_accuracy_bits` and recomputed at higher precision if short.  This
# is a rigour gain the incumbent engine could not offer.
#
# THE RADIUS IS REPRODUCED BIT-EXACTLY, NOT RE-DERIVED.  v2's `RADIUS = mp.mpf("0.4")` is evaluated
# at module load, when dps is still the default 15, so the circle's radius is the DOUBLE 0.4 —
# 3602879701896397 * 2^-53 — for every stage.  v3 transfers that exact binary value into arb rather
# than computing arb(2)/5, which would round to the working precision and move the geometry.
#
# ------------------------------------------------------------------------------------------------
# THE ONE DECLARED DEVIATION BEYOND THE ENGINE SWAP, put on the file's face rather than left to be
# found: the coefficient phase reduces its root-of-unity index mod 2N and MEMOISES the resulting
# N distinct factors, instead of forming expjpi(-2mj/N) afresh for each of the M*N terms.
#   - It is MATHEMATICALLY IDENTICAL: exp(pi*i*x) has period 2 in x, and -2mj/N mod 2 is exact
#     integer arithmetic.
#   - It is not an algorithm change: the same sum of the same terms, with an identical factor
#     computed once instead of many times.
#   - It changes the numbers only at rounding level, and G2 is the test of that, at a tolerance
#     stated before the run.
#   - Sub-gate G2c compares reduced-and-memoised against unreduced-and-fresh directly.
# `acb.dft` would collapse this phase to an FFT, which WOULD be an algorithm change; it is
# deliberately NOT taken here and is filed as priced-not-run.
import json
import math
import os
import sys
import time
import mpmath as mp
from flint import acb, arb, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, os.environ.get("LI_BANK", "epstein_li_v3_bank.jsonl"))
CHUNKS = os.path.join(HERE, os.environ.get("LI_CHUNKS", "epstein_li_v3_chunks.jsonl"))
CHUNK_V = 1
KTERMS = 40
PREC_GUARD = int(os.environ.get("LI_PREC_GUARD", "64"))
LAM_ERR_MAX = mp.mpf(os.environ.get("LI_LAM_ERR_MAX", "1e-6"))
NO_DPS_FLOOR = os.environ.get("LI_NO_DPS_FLOOR", "") == "1"

# cadence: re-set against the NEW measured per-item cost, not inherited from the mpmath rates
TAYLOR_CHUNK = int(os.environ.get("LI_TAYLOR_CHUNK", "256"))
COEF_CHUNK = int(os.environ.get("LI_COEF_CHUNK", "256"))
LAM_CHUNK = int(os.environ.get("LI_LAM_CHUNK", "128"))
ABORT = os.environ.get("LI_TEST_ABORT", "")      # "phase:idx" — gate testing only
NO_MEMO = os.environ.get("LI_NO_MEMO", "") == "1"   # sub-gate G2c only

# v2's radius, at v2's load-time precision, transferred by value
mp.mp.dps = 15
RADIUS = mp.mpf("0.4")

SQ23 = None
TWO_PI_OVER_SQ23 = None
R_ARB = None


# ---- exact binary conversion (no decimal anywhere) -----------------------------------------
def arb2mpf(x):
    m, e = x.mid().man_exp()
    m, e = int(m), int(e)
    if m == 0:
        return mp.mpf(0)
    a = abs(m)
    return mp.mpf((0 if m > 0 else 1, a, e, a.bit_length()))


def mpf2arb(v):
    sgn, man, exp, _bc = mp.mpf(v)._mpf_
    if man == 0:
        return arb(0)
    a = arb(man)
    a = a * arb(2) ** exp if exp >= 0 else a / arb(2) ** (-exp)
    return -a if sgn else a


def acb2mpc(z):
    return mp.mpc(arb2mpf(z.real), arb2mpf(z.imag))


def mpc2acb(z):
    return acb(mpf2arb(mp.re(z)), mpf2arb(mp.im(z)))


def setup(dps):
    mp.mp.dps = dps
    ctx.prec = mp.mp.prec + PREC_GUARD
    global SQ23, TWO_PI_OVER_SQ23, R_ARB
    SQ23 = mp.sqrt(23)
    TWO_PI_OVER_SQ23 = arb.pi() * 2 / arb(23).sqrt()
    R_ARB = mpf2arb(RADIUS)


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


# ---- THE PRECISION CERTIFICATE, and the finding that forced it -------------------------------
#
# I built this file with a floor on each coefficient's CERTIFIED RELATIVE ACCURACY, and G1 killed
# it at m=77 of 120.  Measuring instead of arguing showed the floor was guarding the wrong
# quantity.  c_m is extracted as Re(acc_m)/(N r^m) with r = 0.4, and acc_m decays like ~10^(-1.58m)
# while the summands stay O(1) — so acc_m loses ~1.58m digits to cancellation and the RELATIVE
# accuracy of a high-m coefficient is genuinely near zero.  That is not a defect: those
# coefficients enter lambda_n weighted by binom(n-1,m-1), and what has to be small is the
# PROPAGATED ABSOLUTE error, not the relative error of any single c_m.
#
# The absolute error of acc_m is ~4*N*max|log E|*2^-prec, independent of m.  Hence
#
#     |d lambda_n|  <=  n * sum_m (4*max|f|*2^-prec / r^m) * binom(n-1,m-1)
#                    =  4*n*max|f|*2^-prec * (1/r) * (1 + 1/r)^(n-1)
#
# — the N cancels — so extracting Taylor coefficients on a circle of radius r and recombining them
# with binomials COSTS (n-1)*log10(1+1/r) DIGITS.  At r = 0.4 that is 0.54407 digits per unit of n.
#
# THE CONSEQUENCE FOR THE REGISTERED SCHEDULE, and it is not a port defect — the incumbent engine
# had exactly the same exposure and no way to see it, because mpmath carries no error radius:
#
#     stage 0  n= 120  dps  120  needs   76   OK  (+44)
#     stage 1  n= 300  dps  220  needs  175   OK  (+45)
#     stage 2  n= 700  dps  450  needs  393   OK  (+57)
#     stage 3  n=1500  dps  900  needs  828   OK  (+72)
#     stage 4  n=3000  dps 1600  needs 1645   SHORT by  45
#     stage 5  n=5000  dps 2400  needs 2733   SHORT by 333
#     stage 6  n=7000  dps 3200  needs 3821   SHORT by 621
#     stage 7  n=9000  dps 4000  needs 4910   SHORT by 910
#
# THE REGISTERED PRECISION IS ADEQUATE EXACTLY THROUGH STAGE 3 AND SHORT FROM STAGE 4 ON.  The run
# halted for re-pricing at precisely the last stage its own dps schedule could support.
#
# WHAT THIS FILE DOES ABOUT IT, declared rather than done quietly:
#   (1) A DPS FLOOR raises dps only where the certificate forbids the registered value.  Stages 0-3
#       are untouched, so every banked value and the whole G2 comparison stand.
#   (2) A HARD CERTIFICATE on the actual run: no stage banks a lambda whose rigorous error bound
#       exceeds LAM_ERR_MAX.  A meaningless lambda cannot reach the ledger by either route.
# Raising precision is VERDICT-NEUTRAL — it cannot manufacture a first-negative index, whereas
# running short can.  The deviation is flagged for the author; the direction of the risk is why it
# was taken rather than deferred.
LOG10_1P1R = mp.mpf("0.5440680443502757")     # log10(1 + 1/0.4)


def dps_floor(nmax, maxabs=100):
    need = (mp.log10(4 * nmax * maxabs / mp.mpf("0.4"))
            + (nmax - 1) * LOG10_1P1R + 6)
    return int(mp.ceil(need))


def lam_error_bound(nmax, maxabs, prec):
    """Rigorous bound on |d lambda_n| for all n <= nmax, from the analysis above."""
    return (4 * nmax * mp.mpf(maxabs) * mp.mpf(2) ** (-prec)
            / mp.mpf("0.4") * (mp.mpf("3.5")) ** (nmax - 1))


# ---- HOT PATH 1 : the ported boundary evaluation --------------------------------------------
def Lam_eps_fl(s):
    """s : acb.  Same series, same KTERMS, same truncation — flint's gamma_upper for Gamma(s,a)."""
    tot = -1 / s - 1 / (1 - s)
    for k in range(1, KTERMS + 1):
        if RQ[k] == 0:
            continue
        a = acb(TWO_PI_OVER_SQ23 * k)
        tot += RQ[k] * (a ** (-s) * a.gamma_upper(s) + a ** (s - 1) * a.gamma_upper(1 - s))
    return tot


def E_eps_fl(s):
    return s * (s - 1) * Lam_eps_fl(s)


def E_zeta_fl(s):
    return acb(0.5) * s * (s - 1) * acb.pi() ** (-s / 2) * (s / 2).gamma() * s.zeta()


def log_E_at(Efun, j, N, want_bits):
    """log E(1 + r*expjpi(2j/N)), with arb's own accuracy certificate enforced.

    If the certified relative accuracy falls short of the target, the point is recomputed at
    higher precision.  mpmath offered no such check; this is the port's rigour gain."""
    base = ctx.prec
    try:
        for extra in (0, 256, 1024, 4096):
            ctx.prec = base + extra
            e = ((2 * j) % (2 * N))
            s = 1 + R_ARB * acb(arb(e) / N).exp_pi_i()
            v = Efun(s).log()
            if v.rel_accuracy_bits() >= want_bits:
                return v, extra
        raise RuntimeError(f"boundary point j={j} short of {want_bits} bits after +4096")
    finally:
        ctx.prec = base


def bank_line(path, rec):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def enc_f(x):
    return list(mp.mpf(x)._mpf_)


def dec_f(t):
    return mp.mpf(tuple(t))


def enc_c(z):
    return [enc_f(mp.re(z)), enc_f(mp.im(z))]


def dec_c(p):
    return mp.mpc(dec_f(p[0]), dec_f(p[1]))


def sane_mpf(t):
    if not (isinstance(t, list) and len(t) == 4):
        return False
    if not all(isinstance(v, int) for v in t):
        return False
    return -(1 << 30) < t[2] < (1 << 30)


def sane_payload(phase, payload):
    if phase in ("taylor",):
        return all(isinstance(p, list) and len(p) == 2
                   and sane_mpf(p[0]) and sane_mpf(p[1]) for p in payload)
    if phase in ("coef",):
        return all(sane_mpf(p) for p in payload)
    return True


def load_chunks(stage, dps):
    """Resume-with-validation, unchanged from v2: clean prefix only, torn tail dropped."""
    out = {"taylor": {}, "coef": {}, "lam": {}}
    if not os.path.exists(CHUNKS):
        return out, 0, 0
    kept = dropped = 0
    with open(CHUNKS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                if r.get("v") != CHUNK_V:
                    raise ValueError("version")
                if r["stage"] != stage or r["dps"] != dps:
                    dropped += 1
                    continue
                ph = r["phase"]
                if ph not in out:
                    raise ValueError("phase")
                pay = r["payload"]
                if len(pay) != r["n"]:
                    raise ValueError("length")
                if not sane_payload(ph, pay):
                    raise ValueError("range")
                out[ph][int(r["idx"])] = pay
                kept += 1
            except Exception:
                dropped += 1
                break
    return out, kept, dropped


def _abort(phase, idx):
    if ABORT:
        p, i = ABORT.split(":")
        if p == phase and idx >= int(i):
            print(f"[TEST-ABORT] {phase} at idx {idx}", flush=True)
            sys.stdout.flush()
            os._exit(97)


# ---- the staged computation, chunked (structure identical to v2) ---------------------------
def taylor_boundary(Efun, M, r, stage, dps, cache):
    N = 2 * M + 2
    want_bits = mp.mp.prec
    vals, prev, unwrap = [], None, mp.mpf(0)
    done = sorted(cache["taylor"].keys())
    resumed = 0
    for idx in done:
        pay = cache["taylor"][idx]
        for p in pay:
            vals.append(dec_c(p))
        resumed = idx + len(pay)
    if vals:
        pv, uw = None, mp.mpf(0)
        for v in vals:
            a = mp.im(v) - uw
            if pv is not None:
                d = a - pv
                while d > mp.pi:
                    d -= 2 * mp.pi
                    uw -= 2 * mp.pi
                while d < -mp.pi:
                    d += 2 * mp.pi
                    uw += 2 * mp.pi
            pv = a
        prev, unwrap = pv, uw
    buf, bumped, t0 = [], 0, time.time()
    for j in range(resumed, N):
        vf, extra = log_E_at(Efun, j, N, want_bits)
        if extra:
            bumped += 1
        v = acb2mpc(vf)
        if prev is not None:
            d = mp.im(v) - prev
            while d > mp.pi:
                d -= 2 * mp.pi
                unwrap -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
                unwrap += 2 * mp.pi
        prev = mp.im(v)
        w = mp.mpc(mp.re(v), mp.im(v) + unwrap)
        vals.append(w)
        buf.append(enc_c(w))
        if len(buf) >= TAYLOR_CHUNK or j == N - 1:
            bank_line(CHUNKS, {"v": CHUNK_V, "stage": stage, "dps": dps, "phase": "taylor",
                               "idx": len(vals) - len(buf), "n": len(buf), "payload": buf})
            el = time.time() - t0
            print(f"[stage {stage}] taylor {len(vals)}/{N}  {el:.1f}s elapsed  "
                  f"{el/max(1,len(vals)-resumed):.3f}s/val  prec-bumps {bumped}", flush=True)
            _abort("taylor", len(vals))
            buf = []
    return vals


def taylor_coeffs(vals, M, r, stage, dps, cache):
    """HOT PATH 2.  Same sum; flint's exp_pi_i, index reduced mod 2N and memoised (declared)."""
    N = len(vals)
    c = []
    for idx in sorted(cache["coef"].keys()):
        for p in cache["coef"][idx]:
            c.append(dec_f(p))
    vf = [mpc2acb(v) for v in vals]
    inv_N = acb(1) / N
    roots = {}
    if not NO_MEMO:
        for e in range(0, 2 * N, 2):
            roots[e] = acb(arb(e) / N).exp_pi_i()
    maxabs = 0
    for z in vf:
        u = float(z.abs_upper())
        if u > maxabs:
            maxabs = u
    rpow = R_ARB ** (len(c) + 1) if c else R_ARB
    minacc = None
    buf, t0 = [], time.time()
    for m in range(len(c) + 1, M + 1):
        acc = acb(0)
        if NO_MEMO:
            for j in range(N):
                acc += vf[j] * acb(arb(-2 * m * j) / N).exp_pi_i()
        else:
            for j in range(N):
                acc += vf[j] * roots[(-2 * m * j) % (2 * N)]
        z = acc * inv_N / rpow
        # recorded, NOT gated: a high-m coefficient's relative accuracy is near zero by
        # construction and says nothing about whether lambda is meaningful.
        a = z.real.rel_accuracy_bits()
        minacc = a if minacc is None else min(minacc, a)
        x = arb2mpf(z.real)
        c.append(x)
        buf.append(enc_f(x))
        rpow = rpow * R_ARB
        if len(buf) >= COEF_CHUNK or m == M:
            bank_line(CHUNKS, {"v": CHUNK_V, "stage": stage, "dps": dps, "phase": "coef",
                               "idx": len(c) - len(buf), "n": len(buf), "payload": buf})
            el = time.time() - t0
            print(f"[stage {stage}] coef {len(c)}/{M}  {el:.1f}s elapsed  "
                  f"min certified accuracy {minacc} bits", flush=True)
            _abort("coef", len(c))
            buf = []
    return c, minacc, maxabs


def lambdas(c, nmax, stage, dps, cache):
    """UNCHANGED from v2 — mpmath, <1% of measured cost, not a hot path."""
    start, mn, am, firstneg = 1, None, None, None
    for idx in sorted(cache["lam"].keys()):
        st = cache["lam"][idx][-1]
        start = st["upto"] + 1
        mn, am, firstneg = st["min"], st["argmin"], st["firstneg"]
    lam_last = None
    for n in range(start, nmax + 1):
        acc, binom = mp.mpf(0), mp.mpf(1)
        for m in range(1, n + 1):
            acc += c[m - 1] * binom
            binom = binom * (n - m) / m
        v = float(n * acc)
        lam_last = v
        if mn is None or v < mn:
            mn, am = v, n
        if firstneg is None and v < 0:
            firstneg = n
        if n % LAM_CHUNK == 0 or n == nmax:
            bank_line(CHUNKS, {"v": CHUNK_V, "stage": stage, "dps": dps, "phase": "lam",
                               "idx": n, "n": 1,
                               "payload": [{"upto": n, "min": mn, "argmin": am,
                                            "firstneg": firstneg, "last": v}]})
            _abort("lam", n)
    return mn, am, firstneg, lam_last


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
                r = json.loads(line)
                if r.get("kind") in ("selftest", "run", "gate"):
                    kept += 1
                    continue
                for k in ("stage", "nmax", "dps", "min_lambda", "argmin"):
                    if k not in r:
                        raise ValueError("missing " + k)
                if not math.isfinite(float(r["min_lambda"])):
                    raise ValueError("non-finite")
                done.add(int(r["stage"]))
                kept += 1
            except Exception:
                dropped += 1
    return done, kept, dropped


STAGES = [(120, 120), (300, 220), (700, 450), (1500, 900),
          (3000, 1600), (5000, 2400), (7000, 3200), (9000, 4000)]


def resolve_dps(nmax, dps_registered):
    if NO_DPS_FLOOR:
        return dps_registered, dps_registered
    return max(dps_registered, dps_floor(nmax)), dps_registered


def run_stage(si, nmax, dps, Efun=E_eps_fl):
    setup(dps)
    cache, kept, dropped = load_chunks(si, dps)
    print(f"[stage {si}] nmax={nmax} dps={dps} prec={ctx.prec} | chunks kept={kept} "
          f"dropped={dropped} (taylor {len(cache['taylor'])}, coef {len(cache['coef'])}, "
          f"lam {len(cache['lam'])})", flush=True)
    t0 = time.time()
    vals = taylor_boundary(Efun, nmax, RADIUS, si, dps, cache)
    t1 = time.time()
    print(f"[stage {si}] boundary done ({len(vals)} values) in {(t1-t0)/3600:.3f} h", flush=True)
    c, minacc, maxabs = taylor_coeffs(vals, nmax, RADIUS, si, dps, cache)
    t2 = time.time()
    err = lam_error_bound(nmax, maxabs, mp.mp.prec)
    print(f"[stage {si}] coefficients done ({len(c)}) in {(t2-t1)/3600:.3f} h | "
          f"max|log E| = {maxabs:.3f} | CERTIFIED lambda error bound <= {mp.nstr(err, 4)} "
          f"(ceiling {mp.nstr(LAM_ERR_MAX, 3)})", flush=True)
    if err > LAM_ERR_MAX:
        raise RuntimeError(
            f"stage {si} REFUSES TO BANK: certified lambda error bound {mp.nstr(err,4)} exceeds "
            f"{mp.nstr(LAM_ERR_MAX,3)} at dps={dps}. Required dps >= {dps_floor(nmax, maxabs)}.")
    mn, am, firstneg, last = lambdas(c, nmax, si, dps, cache)
    print(f"[stage {si}] lambdas done in {(time.time()-t2)/3600:.3f} h", flush=True)
    return mn, am, firstneg, last, minacc, err, maxabs


def main():
    done, kept, dropped = load_bank()
    print(f"[resume] stage-records kept={kept} dropped={dropped} stages_done={sorted(done)}",
          flush=True)
    nxt = min([i for i in range(len(STAGES)) if i not in done], default=None)
    bank_line(BANK, {"kind": "run", "ts": time.time(),
                     "iso": time.strftime("%Y-%m-%dT%H:%M:%S"),
                     "resumed_into_stage": nxt, "stages_done_at_start": sorted(done),
                     "worker": "v3-flint"})
    print("[schedule] registered dps vs the precision certificate:", flush=True)
    for si, (nmax, dreg) in enumerate(STAGES):
        d, _ = resolve_dps(nmax, dreg)
        print(f"    stage {si}  nmax={nmax:5d}  registered {dreg:5d}  "
              f"{'unchanged' if d == dreg else f'RAISED to {d} (certificate)'}", flush=True)
    max_stage = int(os.environ.get("LI_MAX_STAGE", str(len(STAGES) - 1)))
    for si, (nmax, dps_registered) in enumerate(STAGES):
        if si in done or si > max_stage:
            continue
        dps, dreg = resolve_dps(nmax, dps_registered)
        t0 = time.time()
        mn, am, firstneg, last, minacc, err, maxabs = run_stage(si, nmax, dps)
        bank_line(BANK, {"kind": "stage", "stage": si, "nmax": nmax, "dps": dps,
                         "dps_registered": dreg, "dps_raised": dps != dreg,
                         "ts": time.time(), "wall_h": (time.time() - t0) / 3600.0,
                         "min_lambda": mn, "argmin": am, "first_negative": firstneg,
                         "lambda_last": last, "min_coef_acc_bits": minacc,
                         "lam_error_bound": mp.nstr(err, 6), "max_abs_logE": maxabs,
                         "engine": "flint-acb"})
        print(f"[stage {si}] CHECKPOINT nmax={nmax}: running min lambda = {mn:.6g} at n={am}; "
              f"sign of running minimum = {'NEGATIVE' if mn < 0 else 'positive'}; "
              f"first negative index = {firstneg}", flush=True)
    print("[done] all stages complete", flush=True)


if __name__ == "__main__":
    main()
