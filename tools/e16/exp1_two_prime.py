"""EXPERIMENT ONE — THE TWO-PRIME ROOM.

Author-called 2026-08-17. Gate RELEASED by the author. Relay-only, bench-grade.
NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

Builds on the resurrected instrument:
    prolate_layer.py   the CC prolate / eps substrate (15/15 certified, pins P1-P3)
    qeps_layer.py      Q_eps via eq. (100), eps via (85), eps'(1+) derived
    phi_layer.py       Phi in the eta coordinate, V-restricted

THE ONE CHANGE THIS FILE MAKES TO THE MEASUREMENT PATH, AND IT IS THE FERRY'S RULING:

    V IS IMPOSED ON EVERY MEASUREMENT — COUNTS AND C ALIKE.

The 2026-08-15 battery found the banked pipeline imposed V when computing C and did
NOT impose it when counting offenders (finding two: 203/549 unconstrained vs 202/548
on V, a shift of order 1e-3, the same order as the residuals the law is judged by).
Every count below is taken on V = { eta : int e^{-t/2} eta(t) dt = 0 }.

USAGE
    python exp1_two_prime.py register     # the registration block only; NO measured number
    python exp1_two_prime.py gate         # the blocking known-answer row (L = 3 on V)
    python exp1_two_prime.py run          # gate, then the six-point sweep
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P

LOG2 = math.log(2.0)

# ----------------------------------------------------------------------------- registration
LS = [3.2, 3.6, 4.2, 4.6, 5.5, 7.0]
OMEGAS = [2.0e-3, 1.0e-3, 5.0e-4]        # the corpus's own L=3 triple: M = 549 / 1099 / 2197
NG_Q = 300                                # phi_layer's quadrature order for Q_eps

# the blocking known-answer row: L = 3 on V, from the 2026-08-15 battery's finding two
GATE_L = 3.0
GATE_TARGETS = {2.0e-3: (202, 548), 1.0e-3: (406, 1098), 5.0e-4: (811, 2196)}


def prime_powers_below(L):
    """[(q, p, k)] for every prime power q = p^k STRICTLY BELOW L."""
    out = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        k = 1
        while p ** k < L:
            out.append((p ** k, p, k))
            k += 1
    return sorted(out)


def coeff(q, p):
    """REGISTERED COEFFICIENT — the ferry's stated sqrt(p) * log p pattern.

    The supplied form (f) carries exactly one prime term, at lag log 2:

        Phi(eta) = <xi | N_I xi> + 2 sqrt(2) log 2 * (eta * eta^*)(log 2)

    and 2 sqrt(2) log 2 = 2 * sqrt(q) * log p at q = 2, p = 2. The registered
    generalization is that same expression read at each prime power:

        C(q = p^k) = 2 * sqrt(q) * log p

    It reproduces the supplied term identically at q = 2. It is registered as the
    coefficient because the ferry names the pattern; see coeff_weil for the reading
    it is contrasted against, which is run as a stated sensitivity, not as the law.
    """
    return 2.0 * math.sqrt(q) * math.log(p)


def coeff_weil(q, p):
    """SENSITIVITY ONLY — the Weil explicit formula's own weight, log p / sqrt(q),
    normalized to agree with the supplied term at q = 2:  C(q) = 4 log p / sqrt(q).

    Registered alongside because the two readings DISAGREE IN DIRECTION: the
    registered coefficient GROWS with q (1.96, 3.81, 2.77, 7.20 at q = 2, 3, 4, 5)
    while the explicit formula's weight DECAYS (1.96, 2.54, 1.39, 2.88). Both agree
    at q = 2, which is the only place the corpus has a supplied value, so nothing in
    the banked record separates them. Named, not silently resolved.
    """
    return 4.0 * math.log(p) / math.sqrt(q)


def lag_schedule(L, cf=coeff):
    """[(label, ell, coefficient)] — the active lags at window length L."""
    out = []
    for q, p, k in prime_powers_below(L):
        lab = "log %d" % q if k == 1 else "%d log %d" % (k, p)
        out.append((lab, math.log(q), cf(q, p)))
    return out


def rooms(L):
    """[(label, ell, room fraction)] — room = the fraction 1 - ell/log L of the window."""
    lg = math.log(L)
    return [(lab, ell, max(0.0, 1.0 - ell / lg)) for lab, ell, _ in lag_schedule(L)]


def e1_union(L):
    """E1-UNION, closed form.

    Every room is an initial segment of the same window, so the rooms are NESTED:
    room(ell) has fraction 1 - ell/log L, decreasing in ell. The union of nested sets
    is the largest of them, and the smallest active lag is always log 2. Therefore

        E1-UNION(L) = 1 - log 2 / log L                    for every L in the sweep,

    counting overlaps once. THIS IS IDENTICAL TO THE ONE-PRIME LAW. The union reading
    predicts nothing new at any L, and that is a registered consequence of the design,
    stated here before any measurement rather than discovered after one.
    """
    return 1.0 - LOG2 / math.log(L)


def registration():
    W = 96
    print("=" * W)
    print("EXPERIMENT ONE — THE TWO-PRIME ROOM · REGISTRATION BLOCK")
    print("PRINTED BEFORE ANY MEASURED NUMBER. No measured quantity appears in this block.")
    print("=" * W)

    print("\n--- THE MEASUREMENT PATH, AND THE ONE RULING APPLIED TO IT ---\n")
    print("  V = { eta : int e^{-t/2} eta(t) dt = 0 } IS IMPOSED ON EVERY MEASUREMENT.")
    print("  Counts and C alike. Grid dim on V is M - 1 where M = round(log L / omega).")
    print("  Offenders = directions where Phi > 0 = positive eigenvalues of the")
    print("  V-restricted Phi matrix (phi_layer's own reading, unchanged).")

    print("\n--- THE LAG SCHEDULE: ACTIVE LAGS = { log q : q a prime power < L } ---\n")
    print("  %-6s %-34s %s" % ("L", "active lags", "count"))
    for L in [GATE_L] + LS:
        lg = lag_schedule(L)
        print("  %-6.1f %-34s %d" % (L, ", ".join(l for l, _, _ in lg), len(lg)))

    print("\n  ### A DISCREPANCY IN THE FERRY'S OWN PRE-REGISTRATION, NAMED NOT RESOLVED:")
    print("  the ferry defines the lag set as { log q : q prime power < L } and then says")
    print("  E2-INTERACTION is 'first at L = 4.2'. Under the prime-power definition TWO")
    print("  LAGS ARE ALREADY LIVE AT L = 3.2 (log 2 and log 3), so E2 is live from the")
    print("  first row of the sweep, not the third. 'First at L = 4.2' is the count under")
    print("  the SUPERSEDED ferry-literal rule (log 2 always; 2 log 2 once L > 4), which")
    print("  the 2026-08-14 sitting recorded as disagreeing with the arithmetic.")
    print("  THIS RUN USES THE PRIME-POWER RULE, which is the definition the ferry gives")
    print("  and the schedule the ferry calls corrected. The parenthetical is treated as")
    print("  a leftover from the rule it replaced.")

    print("\n--- THE ROOMS, PER LAG, PER L ---\n")
    print("  %-6s %-12s %-10s %s" % ("L", "lag", "ell", "room = 1 - ell/log L"))
    for L in LS:
        for lab, ell, r in rooms(L):
            print("  %-6.1f %-12s %-10.6f %.6f" % (L, lab, ell, r))
        print()

    print("--- E1-UNION, CLOSED FORM PER L ---\n")
    print("  The rooms are nested initial segments of one window, so the union is the")
    print("  largest room and the smallest lag is always log 2:")
    print("      E1-UNION(L) = 1 - log 2 / log L,   overlaps counted once.\n")
    print("  %-6s %-14s %s" % ("L", "E1-UNION", "= the one-prime law at the same L"))
    for L in LS:
        print("  %-6.1f %-14.6f %s" % (L, e1_union(L), "identical"))

    print("\n  ### REGISTERED CONSEQUENCE: E1-UNION PREDICTS NOTHING THE ONE-PRIME LAW DOES")
    print("  NOT ALREADY PREDICT, AT ANY L IN THE SWEEP. A union of nested rooms cannot.")
    print("  The experiment's whole discriminating content is therefore E2, below.")

    print("\n--- E2-INTERACTION: THE QUANTITY THAT CAN ACTUALLY FAIL ---\n")
    print("      E2(L) := measured negative fraction on V  -  E1-UNION(L)")
    print("\n  profiled against the number of live lags and against the re-measured")
    print("  one-prime baseline at L = 3 (below), which fixes what a residual of")
    print("  'the banked order' means ONCE V IS IMPOSED.")

    print("\n--- THE COEFFICIENTS, STATED ---\n")
    print("  %-8s %-8s %-16s %-16s" % ("q", "p^k", "REGISTERED", "sensitivity"))
    print("  %-8s %-8s %-16s %-16s" % ("", "", "2 sqrt(q) log p", "4 log p / sqrt(q)"))
    for q, p, k in prime_powers_below(8.0):
        print("  %-8d %-8s %-16.6f %-16.6f"
              % (q, "%d^%d" % (p, k), coeff(q, p), coeff_weil(q, p)))
    print("\n  Both agree at q = 2, where the supplied form fixes the value")
    print("  (2 sqrt2 log 2 = %.6f). Nowhere else does the banked record separate them." % coeff(2, 2))
    print("  ### THE REGISTERED COEFFICIENT GROWS WITH q; THE EXPLICIT FORMULA'S WEIGHT")
    print("  DECAYS. This is registered as a model-vs-true-functional exposure BEFORE")
    print("  the run, so a departure cannot later be attributed to it after the fact.")
    print("  The registered coefficient is what the table reports. The sensitivity is")
    print("  run at omega = 1e-3 only and reported beside the table, never inside it.")

    print("\n--- THE BLOCKING KNOWN-ANSWER ROW (runs first; a failure is the result) ---\n")
    print("  L = 3.0, one live lag (log 2 — 3 is not < 3), on V, at the three omega:")
    for om in OMEGAS:
        n, d = GATE_TARGETS[om]
        print("    omega = %-8.1e  ->  %d / %d = %.6f" % (om, n, d, n / d))
    print("  These are the 2026-08-15 battery's V-restricted counts. The sweep does not")
    print("  run unless all three reproduce exactly. Additionally the fast Householder")
    print("  basis of V is validated against phi_layer's own SVD basis at omega = 2e-3.")

    print("\n--- THE OMEGA-STABILITY TRIPLE ---\n")
    print("  omega in { 2e-3, 1e-3, 5e-4 } — the corpus's own L = 3 triple")
    print("  (M = 549 / 1099 / 2197 there). Reported per L as three measurements, never")
    print("  averaged; a row whose three fractions do not agree to the residual scale is")
    print("  reported UNSTABLE and its verdict withheld.")

    print("\n--- BOTH BRANCHES, LONGHAND (the question-fit law, 2026-08-11) ---\n")
    print("  IF E2(L) is at the one-prime residual scale at every L, with no trend in the")
    print("  number of live lags, THEN: the extra prime powers put no measurable weight on")
    print("  the negative fraction at these window lengths; the one-prime law survives the")
    print("  two-prime room unchanged; and the union reading is confirmed vacuous as a")
    print("  PREDICTOR while correct as a PREDICTION — a generalization that generalizes")
    print("  nothing, which is a reportable property of the design, not of the mechanism.")
    print()
    print("  IF E2(L) departs systematically — growing with the number of live lags, or")
    print("  stepping at the L where a lag switches on — THEN: the negative fraction is")
    print("  NOT a function of the smallest lag alone, the nested-union reading is refuted")
    print("  as a description of the measurement, and the departure's profile in the")
    print("  number of live lags is the experiment's finding.")
    print()
    print("  BOTH SENTENCES FINISH. The quantity can fail and its failure bears on the")
    print("  question the sweep was chartered to ask.")

    print("\n--- WHAT THIS EXPERIMENT DOES NOT MEASURE ---\n")
    print("  Nothing about the sign of W_inf - W_2. Nothing about h2. Nothing about any")
    print("  operator inequality. The negative fraction of Phi in the eta coordinate is a")
    print("  bench quantity of a discretized form, measured at a grid, and is reported as")
    print("  one. Lemma 5.2's re-derivation on (1,3] is UNPAID and every L in this sweep")
    print("  lies beyond it; the whole table is extrapolation past a standing debt and")
    print("  is labelled so per row.")
    print("\n" + "=" * W)
    sys.stdout.flush()


# ----------------------------------------------------------------------------- measurement
def _householder_restrict(A, c):
    """Return B0^T A B0 for an orthonormal basis B0 of c-perp, c a unit vector.

    Exact and basis-independent in the only quantity used (the inertia of A on V).
    O(M^2) where phi_layer's SVD route is O(M^3); validated against that route in gate().
    """
    u = c.copy()
    s = 1.0 if u[0] >= 0.0 else -1.0
    u[0] += s
    nu2 = float(u @ u)
    a = 2.0 / nu2
    Au = A @ u
    uAu = float(u @ Au)
    A -= a * np.outer(u, Au)
    A -= a * np.outer(Au, u)
    A += (a * a * uAu) * np.outer(u, u)
    return A[1:, 1:]


def phi_matrix_V(L, omega, lags, qv, e1):
    """The Phi matrix in the eta coordinate at window L, RESTRICTED TO V.

    Identical to phi_layer.phi_matrix except that (a) the single log-2 prime term is
    replaced by one term per active lag at its own address with its own coefficient,
    and (b) the V basis is built by Householder rather than SVD.
    """
    M = int(round(math.log(L) / omega))
    t = (np.arange(M) + 0.5) * omega

    d = t[:, None] - t[None, :]
    Y = np.where(d >= 0, np.exp(d / 2.0), 0.0) * omega
    del d

    N = qv[np.abs(np.arange(M)[:, None] - np.arange(M)[None, :])] * (omega / (2 * e1))
    N *= -1.0
    N[np.diag_indices(M)] += 1.0
    N *= (-2 * e1)

    A = omega * (Y.T @ N @ Y)
    del Y, N

    for lab, ell, c in lags:
        k = int(round(ell / omega))
        if 0 < k < M:
            idx = np.arange(M - k)
            A[idx + k, idx] += 0.5 * c * omega
            A[idx, idx + k] += 0.5 * c * omega

    A = 0.5 * (A + A.T)

    cv = np.exp(-t / 2.0) * omega
    cv /= np.linalg.norm(cv)
    return _householder_restrict(A, cv), M


def measure(L, omega, lags, qv, e1):
    """(offenders, dim on V, fraction, M) — Phi > 0 directions on V."""
    A, M = phi_matrix_V(L, omega, lags, qv, e1)
    ev = np.linalg.eigvalsh(A)
    del A
    npos = int((ev > 0).sum())
    return npos, len(ev), npos / len(ev), M


def _qv_for(omega, nmax):
    t0 = time.time()
    v = P._qvals(omega, nmax, NG_Q)
    print("      [Q_eps table: omega=%.1e, %d lags, %.1f s]" % (omega, nmax + 1, time.time() - t0))
    sys.stdout.flush()
    return v


def gate(qvs, e1):
    """THE BLOCKING ROW. Returns True only if every target reproduces exactly."""
    W = 96
    print("=" * W)
    print("THE BLOCKING KNOWN-ANSWER ROW — L = 3 ON V, THE RE-MEASURED ONE-PRIME LAW")
    print("=" * W)
    lags = lag_schedule(GATE_L)
    print("  active lags at L = 3.0 : %s" % ", ".join(l for l, _, _ in lags))
    print("  predicted 1 - log2/log3 = %.6f\n" % e1_union(GATE_L))
    print("  %-10s %-8s %-14s %-14s %-12s %s"
          % ("omega", "M", "measured", "target", "fraction", "verdict"))
    ok = True
    got = {}
    for om in OMEGAS:
        n, dim, frac, M = measure(GATE_L, om, lags, qvs[om], e1)
        tn, td = GATE_TARGETS[om]
        good = (n == tn and dim == td)
        ok = ok and good
        got[om] = (n, dim, frac, M)
        print("  %-10.1e %-8d %-14s %-14s %-12.6f %s"
              % (om, M, "%d / %d" % (n, dim), "%d / %d" % (tn, td), frac,
                 "PASS" if good else "### FAIL"))
        sys.stdout.flush()

    # the fast V basis against phi_layer's own SVD basis, same omega, same operator
    om = OMEGAS[0]
    A_svd, M = P.phi_matrix(GATE_L, om, NG_Q)
    n_svd = int((np.linalg.eigvalsh(A_svd) > 0).sum())
    n_hh = got[om][0]
    print("\n  V-basis cross-check at omega = %.1e:" % om)
    print("    phi_layer SVD basis  -> %d offenders on %d dims" % (n_svd, A_svd.shape[0]))
    print("    Householder basis    -> %d offenders on %d dims" % (n_hh, got[om][1]))
    basis_ok = (n_svd == n_hh and A_svd.shape[0] == got[om][1])
    print("    %s" % ("IDENTICAL — the fast basis is the corpus's route"
                      if basis_ok else "### DISAGREE — the fast basis is NOT admissible"))
    ok = ok and basis_ok

    print("\n  GATE: %s" % ("PASS — the sweep runs" if ok else "### FAIL — the sweep does not run"))
    print("=" * W)
    sys.stdout.flush()
    return ok, got


def sweep(qvs, e1, cf=coeff, tag="REGISTERED COEFFICIENT  C(q) = 2 sqrt(q) log p",
          omegas=None):
    omegas = omegas or OMEGAS
    W = 110
    print("\n" + "=" * W)
    print("THE SWEEP — %s" % tag)
    print("=" * W)
    print("  %-6s %-26s %-11s %-30s %-11s %s"
          % ("L", "active lags", "E1 pred", "measured on V (3 omega)", "residual", "verdict"))
    rows = []
    for L in LS:
        lags = lag_schedule(L, cf)
        pred = e1_union(L)
        ms = []
        for om in omegas:
            n, dim, frac, M = measure(L, om, lags, qvs[om], e1)
            ms.append((om, n, dim, frac, M))
        fr = [m[3] for m in ms]
        res = [f - pred for f in fr]
        spread = max(fr) - min(fr)
        verdict = "AT E1" if max(abs(r) for r in res) < 2.5e-3 else "### DEPARTS"
        if spread > 2.5e-3:
            verdict = "UNSTABLE in omega"
        rows.append((L, lags, pred, ms, res, spread, verdict))
        print("  %-6.1f %-26s %-11.6f %-30s %-11s %s"
              % (L, ", ".join(l for l, _, _ in lags), pred,
                 " ".join("%.6f" % f for f in fr),
                 "%+.6f" % res[-1], verdict))
        for om, n, dim, frac, M in ms:
            print("        omega=%-9.1e M=%-6d %6d / %-6d = %.6f   E2 = %+.6f"
                  % (om, M, n, dim, frac, frac - pred))
        sys.stdout.flush()
    print("=" * W)
    return rows


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    if what == "register":
        registration()
        return

    registration()
    print("\n\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    e1 = Q.epsprime1()
    print("  eps'(1+) = %.7f  (target 22.996476)\n" % e1)

    nmax = {om: int(round(math.log(max(LS + [GATE_L])) / om)) for om in OMEGAS}
    qvs = {om: _qv_for(om, nmax[om]) for om in OMEGAS}

    ok, _ = gate(qvs, e1)
    if what == "gate":
        return
    if not ok:
        print("\n### THE GATE DID NOT PASS. THE SWEEP IS NOT RUN. THAT IS THE RESULT.")
        return

    sweep(qvs, e1)

    print("\n\n" + "=" * 110)
    print("SENSITIVITY (reported beside the table, never inside it) — the Weil weight")
    print("C(q) = 4 log p / sqrt(q), at omega = 1e-3 only")
    print("=" * 110)
    sweep(qvs, e1, cf=coeff_weil,
          tag="SENSITIVITY  C(q) = 4 log p / sqrt(q)", omegas=[1.0e-3])

    # C on V, imposed consistently, reported once
    om = 1.0e-3
    M = int(round(math.log(3.0) / om))
    t = (np.arange(M) + 0.5) * om
    d = t[:, None] - t[None, :]
    Aop = om * np.where(d >= 0, np.exp(d / 2.0), 0.0)
    cv = np.exp(-t / 2.0) * math.sqrt(om)
    cv /= np.linalg.norm(cv)
    Pv = np.eye(M) - np.outer(cv, cv)
    print("\n  C on V = %.5f   (banked 0.34481, 'stable to 3 digits')"
          % np.linalg.svd(Aop @ Pv, compute_uv=False)[0])


if __name__ == "__main__":
    main()
