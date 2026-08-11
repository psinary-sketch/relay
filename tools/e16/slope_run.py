# -*- coding: utf-8 -*-
"""W-ORD-SLOPE: the run.

Tolerances were committed at PLACE-papers 67b7dea BEFORE any point was built.
B-DEFINITION FROZEN at B = 2M.  The instrument was recovered from the register's
description and VERIFIED against the family run's ten measured indices.

Per point: multiset built . first-negative index MEASURED . independent
recomputation at the crossing (mpmath, direct powering) . c = n*delta/gamma^2 .
banked with fsync as it lands (resumable: an existing id is not recomputed).

RESTART COMMAND (verbatim, stated before launch):
    cd D:\\relay\\tools\\e16 && python slope_run.py
"""
import json, math, os, sys
import numpy as np
import zeta_ordinates as Zo

BANK = r"D:\relay\data\slope_points.jsonl"
FAMILY = r"D:\relay\data\threshold_law_points.jsonl"
TWO_PI = 2.0 * math.pi

# ---------------------------------------------------------------- instrument
def online_thetas(g):
    return math.pi - 2.0 * np.arctan(2.0 * np.asarray(g, dtype=np.float64))

def quad(gamma, delta):
    out = []
    for s in (+1.0, -1.0):
        rho = complex(0.5 + s * delta, gamma)
        z = 1.0 - 1.0 / rho
        out.append((math.log(abs(z)), math.atan2(z.imag, z.real)))
    return out

def measure(M, gamma, delta, nmax):
    th = online_thetas(Zo.get(M))
    (lrp, pp), (lrm, pm) = quad(gamma, delta)
    base_min = float('inf')
    for n in range(1, nmax + 1):
        base = 2.0 * M - 2.0 * np.sum(np.cos(np.fmod(n * th, TWO_PI)))
        if base < base_min:
            base_min = base
        lam = base + 4.0 \
            - 2.0 * math.exp(n * lrp) * math.cos(math.fmod(n * pp, TWO_PI)) \
            - 2.0 * math.exp(n * lrm) * math.cos(math.fmod(n * pm, TWO_PI))
        if lam < 0.0:
            return n, base_min, float(base)
    return None, base_min, None

def recheck(M, gamma, delta, n):
    """Independent recomputation: mpmath, DIRECT POWERING of (1-1/rho)^n."""
    from mpmath import mp, mpf, mpc, cos, atan, pi, re
    mp.dps = 50
    g = Zo.get(M)
    out = []
    for k in (n - 1, n):
        tot = mpf(0)
        for gg in g:
            rho = mpc(mpf(1) / 2, mpf(float(gg)))
            tot += 2 * (1 - re((1 - 1 / rho) ** k))
        for s in (1, -1):
            rho = mpc(mpf(1) / 2 + s * mpf(str(delta)), mpf(str(gamma)))
            tot += 2 * (1 - re((1 - 1 / rho) ** k))
        out.append(float(tot))
    return out            # [lam(n-1), lam(n)]

# ---------------------------------------------------------------- banking
def load(path):
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding='utf-8') if l.strip()]

def bank(rec):
    with open(BANK, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())

# ---------------------------------------------------------------- the design
# B = 2M spans 2 .. 20000 = exactly 4.0 decades.
# >=1 matched-pair collision at fixed B per new decade: B=2, B=4000, B=20000.
POINTS = [
    (1,     1,     8.0,  0.30),
    (2,     1,    20.0,  0.10),   # collision at B=2
    (3,     2,    12.0,  0.25),
    (4,     5,    30.0,  0.40),
    (5,    15,     6.0,  0.05),
    (6,    50,    45.0,  0.45),
    (7,   200,    10.0,  0.12),
    (8,   800,    25.0,  0.35),
    (9,  2000,    18.0,  0.20),
    (10, 2000,    40.0,  0.45),   # collision at B=4000
    (11, 4000,    15.0,  0.08),
    (12, 7000,    35.0,  0.30),
    (13,10000,    12.0,  0.15),
    (14,10000,    28.0,  0.42),   # collision at B=20000
]

def validate():
    print("=== INSTRUMENT VALIDATION against the family run's ten MEASURED indices ===")
    ok = 0
    for p in load(FAMILY):
        n, bmin, _ = measure(p["M"], p["gamma"], p["delta"], int(p["n"] * 1.4) + 300)
        hit = (n == p["n"])
        ok += hit
        print("  id%-3d M=%-6d expect n=%-7d got %-8s %-6s   base_min %.5f vs %.5f"
              % (p["id"], p["M"], p["n"], n, "MATCH" if hit else "NO", bmin, p["base_min"]))
    print("  --> %d/10 exact" % ok)
    return ok

if __name__ == "__main__":
    if "--run" not in sys.argv:
        sys.exit(0 if validate() == 10 else 1)

    done = {r["id"] for r in load(BANK)}
    print("resuming; %d already banked" % len(done), flush=True)
    for pid, M, gamma, delta in POINTS:
        if pid in done:
            print("  id%-3d already banked, skipped" % pid, flush=True)
            continue
        B = 2.0 * M
        nmax = int(1.9 * (gamma * gamma / delta) * math.log(max(0.55 * B, 1.2))) + 4000
        n, bmin, lam_at = measure(M, gamma, delta, nmax)
        if n is None:
            rec = dict(id=pid, M=M, gamma=gamma, delta=delta, B=B, n=None,
                       status="NO-CROSSING-IN-CAP", nmax=nmax)
            bank(rec); print("  id%-3d NO CROSSING within %d" % (pid, nmax), flush=True)
            continue
        lp, la = recheck(M, gamma, delta, n)
        c = n * delta / (gamma * gamma)
        rec = dict(id=pid, M=M, gamma=gamma, delta=delta, B=B, n=n, c=c,
                   base_min=bmin, base_positive=bool(bmin > 0),
                   lam_prev=lp, lam_at=la,
                   recheck_ok=bool(lp >= 0.0 > la),
                   status="OK" if (lp >= 0.0 > la) else "RECHECK-DISAGREES")
        bank(rec)
        print("  id%-3d M=%-6d B=%-8.0f g=%-5.1f d=%-5.2f  n=%-7d c=%.4f  recheck %s"
              % (pid, M, B, gamma, delta, n, c, "OK" if rec["recheck_ok"] else "DISAGREES"),
              flush=True)
    print("run complete", flush=True)
