# THE ARITHMETIC-SIDE VALIDATION, v2 — INTRA-STAGE BANKING.
#
# v1 banked only at stage boundaries, so an interrupted stage lost everything.  With stages
# growing and the stop interval fixed, that gives a crossover past which no stage ever completes.
# v2 banks WITHIN a stage so a stop costs minutes, not a stage.
#
# EXACTNESS.  Chunks store mpmath's INTERNAL representation (the `_mpf_` tuple of ints), not a
# decimal string, so a resumed run reproduces byte-identical values.  A decimal round-trip would
# not guarantee that and the gate below would catch it.
#
# TAIL GUARD (atom-bank precedent).  Every chunk carries v / stage / dps / phase / idx / n and is
# validated on load: parseable, required keys present, version match, STAGE AND DPS MATCH (so a
# resume refuses a cache from a different stage or precision), payload length == n, and every
# payload element a well-formed 4-int mpf tuple with a sane exponent.  Any failure DROPS THE
# TORN TAIL and everything after it; the run recomputes from the last good chunk.
#
# Stage-boundary records are unchanged and the four already banked are neither touched nor
# re-derived.
import json
import math
import os
import sys
import time
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "epstein_li_bank.jsonl")
CHUNKS = os.path.join(HERE, "epstein_li_chunks.jsonl")
CHUNK_V = 1
KTERMS = 40
RADIUS = mp.mpf("0.4")
TAYLOR_CHUNK = int(os.environ.get("LI_TAYLOR_CHUNK", "16"))   # ~5 min at stage-3 cost
COEF_CHUNK = int(os.environ.get("LI_COEF_CHUNK", "32"))
LAM_CHUNK = int(os.environ.get("LI_LAM_CHUNK", "128"))
ABORT = os.environ.get("LI_TEST_ABORT", "")      # "phase:idx" — gate testing only
SQ23 = None


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
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# ---- exact serialization -----------------------------------------------------------------
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


def bank_line(path, rec):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def load_chunks(stage, dps):
    """Resume-with-validation. Returns {phase: {idx: payload}} keeping only a clean prefix."""
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
                    dropped += 1          # a cache from another stage/precision: refused
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
                dropped += 1              # torn tail: this record and nothing after it is kept
                break
    return out, kept, dropped


def _abort(phase, idx):
    if ABORT:
        p, i = ABORT.split(":")
        if p == phase and idx >= int(i):
            print(f"[TEST-ABORT] {phase} at idx {idx}", flush=True)
            sys.exit(97)


# ---- the staged computation, chunked -------------------------------------------------------
def taylor_boundary(Efun, M, r, stage, dps, cache):
    """Boundary values with unwrapping. Sequential, so each chunk carries its unwrap state."""
    N = 2 * M + 2
    vals, prev, unwrap = [], None, mp.mpf(0)
    done = sorted(cache["taylor"].keys())
    resumed = 0
    for idx in done:
        pay = cache["taylor"][idx]
        for p in pay:
            vals.append(dec_c(p))
        resumed = idx + len(pay)
    if resumed:
        prev = mp.im(vals[-1]) if False else None   # prev/unwrap restored below from state file
    # unwrap state is recoverable from the banked values themselves: recompute prev/unwrap
    if vals:
        prev, unwrap = mp.mpf(0), mp.mpf(0)
        # rebuild by replaying the (cheap) angle bookkeeping on banked values
        pv = None
        uw = mp.mpf(0)
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
    buf = []
    for j in range(resumed, N):
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
        w = mp.mpc(mp.re(v), mp.im(v) + unwrap)
        vals.append(w)
        buf.append(enc_c(w))
        if len(buf) >= TAYLOR_CHUNK or j == N - 1:
            bank_line(CHUNKS, {"v": CHUNK_V, "stage": stage, "dps": dps, "phase": "taylor",
                               "idx": len(vals) - len(buf), "n": len(buf), "payload": buf})
            _abort("taylor", len(vals))
            buf = []
    return vals


def taylor_coeffs(vals, M, r, stage, dps, cache):
    N = len(vals)
    c = []
    for idx in sorted(cache["coef"].keys()):
        for p in cache["coef"][idx]:
            c.append(dec_f(p))
    buf = []
    for m in range(len(c) + 1, M + 1):
        acc = mp.mpc(0)
        for j in range(N):
            acc += vals[j] * mp.expjpi(-2 * mp.mpf(m * j) / N)
        x = mp.re(acc / N / r ** m)
        c.append(x)
        buf.append(enc_f(x))
        if len(buf) >= COEF_CHUNK or m == M:
            bank_line(CHUNKS, {"v": CHUNK_V, "stage": stage, "dps": dps, "phase": "coef",
                               "idx": len(c) - len(buf), "n": len(buf), "payload": buf})
            _abort("coef", len(c))
            buf = []
    return c


def lambdas(c, nmax, stage, dps, cache):
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
                if r.get("kind") in ("selftest", "run"):
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


def run_stage(si, nmax, dps, Efun=E_eps):
    setup(dps)
    cache, kept, dropped = load_chunks(si, dps)
    print(f"[stage {si}] nmax={nmax} dps={dps} | chunks kept={kept} dropped={dropped} "
          f"(taylor {len(cache['taylor'])}, coef {len(cache['coef'])}, lam {len(cache['lam'])})",
          flush=True)
    vals = taylor_boundary(Efun, nmax, RADIUS, si, dps, cache)
    print(f"[stage {si}] boundary done ({len(vals)} values)", flush=True)
    c = taylor_coeffs(vals, nmax, RADIUS, si, dps, cache)
    print(f"[stage {si}] coefficients done ({len(c)})", flush=True)
    mn, am, firstneg, last = lambdas(c, nmax, si, dps, cache)
    return mn, am, firstneg, last


def main():
    done, kept, dropped = load_bank()
    print(f"[resume] stage-records kept={kept} dropped={dropped} stages_done={sorted(done)}",
          flush=True)
    nxt = min([i for i in range(len(STAGES)) if i not in done], default=None)
    bank_line(BANK, {"kind": "run", "ts": time.time(),
                     "iso": time.strftime("%Y-%m-%dT%H:%M:%S"),
                     "resumed_into_stage": nxt, "stages_done_at_start": sorted(done),
                     "worker": "v2-intrastage"})
    for si, (nmax, dps) in enumerate(STAGES):
        if si in done:
            continue
        mn, am, firstneg, last = run_stage(si, nmax, dps)
        bank_line(BANK, {"kind": "stage", "stage": si, "nmax": nmax, "dps": dps,
                         "ts": time.time(), "min_lambda": mn, "argmin": am,
                         "first_negative": firstneg, "lambda_last": last})
        print(f"[stage {si}] CHECKPOINT nmax={nmax}: running min lambda = {mn:.6g} at n={am}; "
              f"sign of running minimum = {'NEGATIVE' if mn < 0 else 'positive'}; "
              f"first negative index = {firstneg}", flush=True)
    print("[done] all stages complete", flush=True)


if __name__ == "__main__":
    main()
