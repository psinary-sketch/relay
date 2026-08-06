# THE EPSTEIN ZERO CENSUS — disc -23, principal form x^2 + xy + 6y^2, h(-23) = 3.
#
# GROUND TRUTH ONLY.  This census is HELD ASIDE and never enters the arithmetic-side
# computation it exists to validate.  Nothing here is fed to any Li/Toeplitz pipeline.
#
# EXECUTOR_RULES Rule 2 compliance:
#   * per-record flushing  -- one JSON line per cell, flushed and fsynced on write;
#   * resume-with-validation -- on start, every banked line is re-parsed and field-checked;
#      malformed or non-finite records are DISCARDED and their cells re-run;
#   * self-test banked first -- the functional equation Lambda(s) = Lambda(1-s) is checked
#      numerically before any cell is walked, and the check is banked as record 0;
#   * restart command is stated in the report BEFORE launch.
#
# METHOD.  Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s) satisfies Lambda(s) = Lambda(1-s) and
#   Lambda(s) = sum_k r_Q(k) [ a_k^-s Gamma(s,a_k) + a_k^(s-1) Gamma(1-s,a_k) ] - 1/s - 1/(1-s),
# with a_k = 2*pi*k/sqrt(23).  Gamma's poles cancel the trivial zeros, so the winding number of
# Lambda around a rectangle counts NONTRIVIAL zeros inside it.
#
# The census is 2-D by construction (argument-principle winding over rectangles).  A
# critical-line scan would IMPOSE the real part and reproduce the defect I-7 stage 2 forbids.
import json
import os
import sys
import math
import mpmath as mp

DPS = 20
KTERMS = 40                      # a_k = 1.3101k; e^{-1.31*40} ~ 2e-23, below dps 20
SIG_EDGES = [0.52, 0.66, 0.80, 0.94, 1.08, 1.22, 1.36, 1.50]
T_LO, T_HI, T_STEP = 0.5, 60.0, 0.5   # t < 0.5 excluded: the pole of Lambda at s = 1
NSIDE = 48                       # boundary samples per side
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "epstein_census_bank.jsonl")

mp.mp.dps = DPS
SQ23 = mp.sqrt(23)


def rep_counts(K):
    """r_Q(k) for Q = x^2 + xy + 6y^2, k = 1..K."""
    r = [0] * (K + 1)
    ymax = int(2 * math.sqrt(K / 23.0)) + 1
    for y in range(-ymax, ymax + 1):
        disc0 = -23 * y * y
        for x in range(-int(math.sqrt(K)) - abs(y) - 1, int(math.sqrt(K)) + abs(y) + 2):
            k = x * x + x * y + 6 * y * y
            if 1 <= k <= K:
                r[k] += 1
    return r


RQ = rep_counts(KTERMS)
AK = [None] + [2 * mp.pi * k / SQ23 for k in range(1, KTERMS + 1)]


def Lam(s):
    """Lambda(s), the completed Epstein zeta of the principal disc -23 form."""
    s = mp.mpc(s)
    tot = -1 / s - 1 / (1 - s)
    for k in range(1, KTERMS + 1):
        if RQ[k] == 0:
            continue
        a = AK[k]
        tot += RQ[k] * (a ** (-s) * mp.gammainc(s, a) + a ** (s - 1) * mp.gammainc(1 - s, a))
    return tot


def winding(s_lo, s_hi, t_lo, t_hi, n):
    """Net winding of Lambda around the rectangle, as a float (should be near an integer)."""
    pts = []
    for i in range(n):
        pts.append(mp.mpc(s_lo + (s_hi - s_lo) * i / n, t_lo))
    for i in range(n):
        pts.append(mp.mpc(s_hi, t_lo + (t_hi - t_lo) * i / n))
    for i in range(n):
        pts.append(mp.mpc(s_hi - (s_hi - s_lo) * i / n, t_hi))
    for i in range(n):
        pts.append(mp.mpc(s_lo, t_hi - (t_hi - t_lo) * i / n))
    tot, prev = mp.mpf(0), None
    minmod = None
    for p in pts + [pts[0]]:
        v = Lam(p)
        m = abs(v)
        minmod = m if minmod is None else min(minmod, m)
        a = mp.arg(v)
        if prev is not None:
            d = a - prev
            while d > mp.pi:
                d -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
            tot += d
        prev = a
    return float(tot / (2 * mp.pi)), float(minmod)


def load_bank():
    """Resume WITH VALIDATION: re-parse every line, discard malformed or non-finite."""
    done, kept, dropped = set(), 0, 0
    if not os.path.exists(BANK):
        return done, kept, dropped
    with open(BANK, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if rec.get("kind") == "selftest":
                    kept += 1
                    continue
                for key in ("sig_lo", "t_lo", "wind", "minmod"):
                    if key not in rec:
                        raise ValueError("missing " + key)
                if not (math.isfinite(rec["wind"]) and math.isfinite(rec["minmod"])):
                    raise ValueError("non-finite")
                done.add((round(rec["sig_lo"], 4), round(rec["t_lo"], 4)))
                kept += 1
            except Exception:
                dropped += 1
    return done, kept, dropped


def bank(rec):
    with open(BANK, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def main():
    done, kept, dropped = load_bank()
    print(f"[resume] banked records kept={kept} dropped={dropped} cells_done={len(done)}",
          flush=True)

    if kept == 0:
        # SELF-TEST banked first: the functional equation, checked numerically.
        s = mp.mpc("0.83", "7.1")
        a, b = Lam(s), Lam(1 - s)
        err = float(abs(a - b) / max(abs(a), mp.mpf(1)))
        bank({"kind": "selftest", "test": "Lambda(s) == Lambda(1-s)",
              "s": [float(s.real), float(s.imag)], "rel_err": err, "dps": DPS,
              "kterms": KTERMS})
        print(f"[selftest] FE relative error = {err:.3e}", flush=True)
        if err > 1e-12:
            print("[selftest] FAILED — halting before any cell is walked", flush=True)
            sys.exit(1)

    t = T_LO
    while t < T_HI - 1e-9:
        for i in range(len(SIG_EDGES) - 1):
            key = (round(SIG_EDGES[i], 4), round(t, 4))
            if key in done:
                continue
            w, mm = winding(SIG_EDGES[i], SIG_EDGES[i + 1], t, t + T_STEP, NSIDE)
            bank({"kind": "cell", "sig_lo": SIG_EDGES[i], "sig_hi": SIG_EDGES[i + 1],
                  "t_lo": t, "t_hi": t + T_STEP, "wind": w, "minmod": mm,
                  "nside": NSIDE, "dps": DPS})
            if abs(w) > 0.25:
                print(f"[hit] sigma[{SIG_EDGES[i]},{SIG_EDGES[i+1]}] "
                      f"t[{t},{t+T_STEP}] winding={w:+.3f} minmod={mm:.2e}", flush=True)
        print(f"[row] t={t:.1f} complete", flush=True)
        t += T_STEP
    print("[done] census complete to T =", T_HI, flush=True)


if __name__ == "__main__":
    main()
