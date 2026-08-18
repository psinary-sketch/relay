"""W-ATTEMPT-2, SITTING 6 — THE ARCHIMEDEAN MODEL: THE ONE UNMODELED SLOT.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA at bench
grade; refused: any promotion to W_inf - Sum W_p at complete roster, or register movement.
This sitting replaces "at cite by symmetry" with a COMPUTED archimedean factor; whatever
it shows is a property of the model, never of the Hypothesis.

RULE-3 DISAGREEMENT, FLAGGED NOT SILENTLY RESOLVED
==================================================
The ferry writes the window as [a^-1, a]; sitting 4's banked registration wrote the
diagonal's archimedean window as [1/a^2, a^2] (the staircase counts NORMS p^k <= a^2;
[a^-1, a] is the absolute-value normalization of the same shape). Per Rule 3 the
disagreement is flagged here and BOTH radii lambda in {1/a, 1/a^2} are measured; no
convention is adjudicated by this bench.

THE MODEL, DECLARED (before any run)
====================================
The finite Fourier model of the real place: N grid points (N ODD), centered indices
m in [-(N-1)/2, (N-1)/2], self-dual spacing h = sqrt(2*pi/N), x_m = m*h; the centered
DFT F[j,k] = exp(2*pi*i*m_j*m_k/N)/sqrt(N), which represents the Fourier transform of
L^2(R) on this grid and satisfies F^2 = parity EXACTLY (checked in-run), F^4 = 1.
The factor enters the section CLASS-SILENTLY (B5): it tensors with the identity on
C[Cl]; nothing archimedean touches the coupling.

THE SONIN CONDITION AT THE REAL PLACE, TWO READINGS — REGISTERED LONGHAND:
(W1, the ball reading — CC's Sonin condition, the local models' mirror): Son_inf(a) =
    {f : f = 0 and F f = 0 on the ball |x| < lambda}, lambda the window's inner radius.
    The outer edge is the GRID EDGE (the model's truncation, the same declared artifact
    as the local towers' finite n); convergence in N is reported, not assumed.
(W2, the hard two-sided window): both f and F f vanish OUTSIDE lambda <= |x| <= Lambda
    (Lambda = a or a^2 per convention). LONGHAND PREDICTION, said before the run: in the
    continuum a function with f and F f both compactly supported is ZERO (the uncertainty
    principle / Paley-Wiener, at cite) — so this space should DIE as N refines. If it
    does, that is not a defect: it is the located reason the archimedean factor is a
    ball-vanishing space with a soft outer edge, never a hard two-sided window — the
    real place's distinctive geometry in this construction.

MEASURED QUANTITIES (registered with the branch map, before any number):
 M1  dim Son_inf(a) under (W1), per (N, lambda): expected positive and N-stable in
     fraction; if 0 anywhere, the ext-no address is "the window holds no Sonin vector".
 M2  T-invariance of the factor: ||(1-S) F K|| with S the orthoprojection onto
     Son_inf(a) — the EXACT mirror of the finite places' certified closure. By the
     two-sided symmetry of the ball this should land at machine zero (the invariance is
     structural, the same mechanism as at the finite places); a nonzero value names the
     failing address at infinity.
 M3  the pairing at infinity: G = K^dag F K; its radical (rank vs dim), the raw
     Hermitian residual ||G - G^dag||, and the parity-twisted residual
     ||G^dag - P_S G|| with P_S = K^dag P K — the real-place instance of the same
     twisted-Hermitian identity certified exactly at the finite places (sitting 5).
 M4  the weight channel at infinity: Q_inf(a) = ||K^dag D K||_F with D the scaling
     GENERATOR D = (X Ptil + Ptil X)/2, Ptil = F X F^dag (the grid's exact affordance;
     the local channel used the group element U_p — the generator-vs-element difference
     is DECLARED, not hidden). Reported per (N, lambda); the punctuated-weight re-read
     places Q_inf beside the banked finite-side weights.

BRANCHES, REGISTERED:
 (ext-yes)     W1 lands: dim > 0 at every a, M2 at machine zero, radical zero, the twist
               identity holds at machine, Q_inf stable in N — D-YES EXTENDS to the full
               section AT THE MODEL (finite factors exact by sitting 5; the infinity
               factor measured here); "at cite" is retired for this slot.
 (ext-no)      W1 fails one of these — the archimedean place named as the one that does
               not interleave; the failing measurement is the codomain absence at its
               exact address.
 (ext-partial) W1 lands and W2 dies under refinement (the registered prediction): D-YES
               extends under the ball reading, and the death of the hard window is
               recorded as the real place's own geometry (uncertainty at cite) — the
               sharp local/global asymmetry: finite places afford hard two-sided
               truncation exactly; the real place does not.

THE PUNCTUATED-WEIGHT RE-READ, registered: the full-section weight at the diagonal cell
is the product Q_inf(a) * prod_p Q(p, n_p(a)). The banked finite side (sitting 4, exact):
0 through a = 2; 6*sqrt(6) at a = 3 on {inf,2,3}; 0 at a = 3 on {inf,2,3,5}. The re-read
reports whether the infinity channel is alive where the finite channels are dead (the
sawtooth's zeros persist in the product; the ledger PER CHANNEL is the new information).

Usage:  python b19_attempt2_s6.py register | run
"""
import math
import sys
import numpy as np

AS = [(1.3, "1.3"), (math.sqrt(2), "sqrt2"), (1.5, "1.5"), (math.sqrt(3), "sqrt3"), (2.0, "2"), (3.0, "3")]
NS = [255, 511, 1023]


def grid(N):
    m = np.arange(N) - (N - 1) // 2
    h = math.sqrt(2 * math.pi / N)
    F = np.exp(2j * np.pi * np.outer(m, m) / N) / math.sqrt(N)
    return m, h, F


def parity_matrix(N):
    m = np.arange(N) - (N - 1) // 2
    P = np.zeros((N, N))
    idx = {mm: k for k, mm in enumerate(m)}
    for k, mm in enumerate(m):
        P[idx[-mm], k] = 1.0
    return P


def nullspace(C, N):
    _, s, Vh = np.linalg.svd(C, full_matrices=True)
    tol = max(C.shape) * np.finfo(float).eps * (s[0] if len(s) else 1.0)
    rank = int((s > tol).sum())
    return Vh[rank:].conj().T


def sonin_ball(N, F, x, lam):
    ball = np.abs(x) < lam * (1 - 1e-12)
    if not ball.any():
        return None, 0
    C = np.vstack([np.eye(N)[ball], F[ball]])
    K = nullspace(C, N)
    return K, K.shape[1]


def window_dim(N, F, x, lam, Lam):
    outside = ~((np.abs(x) >= lam * (1 - 1e-12)) & (np.abs(x) <= Lam * (1 + 1e-12)))
    C = np.vstack([np.eye(N)[outside], F[outside]])
    K = nullspace(C, N)
    return K.shape[1]


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 6 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    for N in NS:
        m, h, F = grid(N)
        x = m * h
        P = parity_matrix(N)
        f2p = float(np.linalg.norm(F @ F - P))
        print("--- N = %d (odd), h = %.6f, grid extent |x| <= %.3f ---" % (N, h, abs(x).max()))
        print("    F^2 = parity, exactly on the centered grid: ||F^2 - P|| = %.2e" % f2p)
        X = np.diag(x)
        Ptil = F @ X @ F.conj().T
        D = (X @ Ptil + Ptil @ X) / 2
        print("  %-7s %-9s %-6s %-12s %-12s %-12s %-12s %-12s %-10s %s"
              % ("a", "lambda", "dim", "M2:(1-S)FK", "radical", "herm raw", "herm twist", "Q_inf(a)", "W2dim aE", "W2dim a2E"))
        for a, alab in AS:
            for lam, llab in [(1 / a, "1/a"), (1 / a**2, "1/a^2")]:
                K, d = sonin_ball(N, F, x, lam)
                if d == 0:
                    print("  %-7s %-9s %-6d %s" % (alab, llab, 0, "EMPTY — the ext-no address"))
                    continue
                S = K @ K.conj().T
                m2 = float(np.linalg.norm((np.eye(N) - S) @ F @ K))
                G = K.conj().T @ F @ K
                sv = np.linalg.svd(G, compute_uv=False)
                rank = int((sv > sv[0] * 1e-10).sum())
                herm_raw = float(np.linalg.norm(G - G.conj().T))
                PS = K.conj().T @ P @ K
                herm_tw = float(np.linalg.norm(G.conj().T - PS @ G))
                q = float(np.linalg.norm(K.conj().T @ D @ K))
                Lam = a if llab == "1/a" else a**2
                w2a = window_dim(N, F, x, lam, a)
                w2a2 = window_dim(N, F, x, lam, a**2)
                print("  %-7s %-9s %-6d %-12.2e %-12s %-12.2e %-12.2e %-12.4f %-10d %d"
                      % (alab, llab, d, m2, "%d/%d" % (rank, d), herm_raw, herm_tw, q, w2a, w2a2))
                sys.stdout.flush()
        print()

    print("--- THE PUNCTUATED-WEIGHT RE-READ (per-channel ledger at the largest N; lambda = 1/a) ---")
    print("    banked finite side (sitting 4, exact): weight 0 through a = 2;")
    print("    6*sqrt(6) = 14.6969... at a = 3 on {inf,2,3}; 0 at a = 3 on {inf,2,3,5}.")
    print("    Q_inf(a) above is the infinity channel; the full-section weight is the product.")
    print("    The ledger's reading is printed by the report, not asserted by this bench.")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
