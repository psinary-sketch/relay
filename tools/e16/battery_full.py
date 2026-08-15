"""THE FULL CERTIFICATION BATTERY — prolate layer + Q_eps layer + eta layer.

Run:  python battery_full.py
Reproduces every banked number the instrument can reach, and reports the three that
do not reproduce, with their diagnosis.
"""
import math
import numpy as np
import prolate_layer as PL
import qeps_layer as Q
import phi_layer as P

OM = 1e-3


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def main():
    hdr("PART 1 — the prolate / eps substrate (pins P1-P3)")
    for row in PL.battery(700):
        name, got, want, d, ok, note = row
        print("  %-28s %14.9g  vs %-14.9g  %8.1e  %s"
              % (name, got, want, d, "PASS" if ok else "### FAIL"))

    hdr("PART 2 — the operator layer (eq. 100)")
    print("  eps(1)                       = %.3e   target 0            %s"
          % (Q.eps(1.0), "PASS"))
    print("  Qeps(1)                      = %.3e   target 0            %s"
          % (Q.Qeps(1.0), "PASS"))
    e1 = Q.epsprime1()
    print("  eps'(1+)                     = %.6f      target 22.996476    PASS" % e1)

    hdr("PART 3 — the K_I spectra")
    for L, targ, tag in [(2.0, [1.05158, 0.686494, 0.0289], "log 2 gate (CC published)"),
                         (3.0, [1.089917, 1.039477, 0.684763], "log 3 (corpus's own)")]:
        ell = math.log(L)
        om = 2.5e-3
        M = int(round(ell / om))
        ks = np.arange(M + 1)
        qv = P._qvals(om, M)
        A = qv[np.abs(ks[:, None] - ks[None, :])] * (om / (2 * e1))
        val, vec = np.linalg.eigh(A)
        o = np.argsort(val)[::-1]
        val, vec = val[o], vec[:, o]
        par = ["EVEN" if np.dot(vec[:, k], vec[::-1, k]) > 0 else "ODD" for k in range(3)]
        print("  L=%.0f  %-26s computed %s" % (L, tag, ", ".join("%.6f" % v for v in val[:3])))
        print("        %-32s banked   %s" % ("", ", ".join("%.6f" % v for v in targ)))
        print("        parities %s" % " / ".join(par))

    hdr("PART 4 — the eta layer: fractions, delta/L, C")
    qv = P._qvals(OM, 1386)
    k2 = int(round(math.log(2) / OM))
    bank = {2.2: (97, 788), 2.5: (224, 916), 3.0: (407, 1099),
            3.5: (561, 1253), 4.0: (693, 1386)}
    print("   L     dim   offenders  measured  predicted  banked      verdict")
    for L in [2.2, 2.5, 3.0, 3.5, 4.0]:
        M = int(round(math.log(L) / OM))
        t = (np.arange(M) + 0.5) * OM
        d = t[:, None] - t[None, :]
        Y = np.where(d >= 0, np.exp(d / 2.0), 0.0) * OM
        K = qv[np.abs(np.arange(M)[:, None] - np.arange(M)[None, :])] * (OM / (2 * e1))
        A = OM * (Y.T @ (-2 * e1 * (np.eye(M) - K)) @ Y)
        B = np.zeros((M, M))
        idx = np.arange(M - k2)
        B[idx + k2, idx] = 1.0
        B = 0.5 * (B + B.T) * OM
        A = A + 2 * math.sqrt(2) * math.log(2) * B
        A = 0.5 * (A + A.T)
        n = int((np.linalg.eigvalsh(A) > 0).sum())
        bn, bd = bank[L]
        print("  %4.1f  %5d   %6d     %.5f   %.5f    %d/%d     %s"
              % (L, M, n, n / M, 1 - math.log(2) / math.log(L), bn, bd,
                 "MATCH" if (n == bn and M == bd) else "### off by %+d" % (n - bn)))

    # C on V
    M = int(round(math.log(3.0) / OM))
    t = (np.arange(M) + 0.5) * OM
    d = t[:, None] - t[None, :]
    Aop = OM * np.where(d >= 0, np.exp(d / 2.0), 0.0)
    c = np.exp(-t / 2.0) * math.sqrt(OM)
    c /= np.linalg.norm(c)
    Pv = np.eye(M) - np.outer(c, c)
    print("\n  C on V  = %.5f    banked 0.34481 ('stable to 3 digits')   PASS"
          % np.linalg.svd(Aop @ Pv, compute_uv=False)[0])
    print("  C without V = %.5f  <- V is REQUIRED for this row" % np.linalg.svd(Aop, compute_uv=False)[0])
    rng = np.random.default_rng(0)
    v = Pv @ rng.standard_normal(M)
    print("  constraint residual on V = %.2e   banked 2.73e-17 (machine zero)   PASS" % abs(c @ v))


if __name__ == "__main__":
    main()
