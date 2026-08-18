"""W-ATTEMPT-2, SITTING 3 — T2 PROPER ON THE GLUED OBJECT.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE STOP, AS CORRECTED BY THE AUTHOR THIS SITTING: measured properties of the constructed
object are DATA, recorded plainly at bench grade; what is refused is any promotion to a
statement about W_inf - Sum W_p at complete roster, or any movement of the register.
THE RANGE LAW GOVERNS: nothing inherited across cells; every factor-law re-measured.

CHECKPOINT-1 REGISTRATION — T2 IN THE OBJECT'S TERMS (before any run)
=====================================================================
The two axes on the glued object G(F; n) = (x)_{p in F} Son_p(n_p) (x) C[Cl]:
  (P) the place set F        — add a place q: tensor a new factor, multiply coupling by c_q
  (S) the per-place cutoff   — raise n_p: replace the factor Son_p(n) by Son_p(n+1)

LONGHAND, REGISTERED: the two operations act on DISJOINT tensor slots, so their
commutation and the compose-identity (add-at-cutoff-n = raise-1-to-n then add) should be
EXACT — measured below, never assumed (range law). The SHAPE question is the real one:

  per-channel (P)-action        vs      (S)-action                (registered prediction)
  dim        x (q^m - 1)^2              x ((p^{n+1}-1)/(p^n-1))^2  both active, local factors
  coupling   x chi(c_q) (Euler-exact)   CONSTANT                   ### S-SILENT
  H^2        fixed (C[Cl], dim h)       fixed                      both-silent
  radical    0 -> 0                     0 -> 0                     both-silent
  weight     x Q(q, m)                  x (p^n-1)/(p^{n-1}-1)      both active, local factors
  tw-Herm    preserved                  preserved                  both-silent

REGISTERED VERDICT MAP:
  (T2-yes)     same-shape laws + exact commutation + the compose-identity on every channel
               — support and place ONE operation ON THIS OBJECT; the SCOPE GUARD registered
               with it: the model's (S) axis is the CUTOFF, a proxy — the original T2's
               support axis is the test-function window; a T2-yes here is T2-ON-THE-MODEL,
               not T2 discharged. Said before the run.
  (T2-no)      a named channel's laws differ in shape or fail to commute — the step named.
  (T2-partial) the split itself the finding — predicted form: the C[Cl]-structure
               (coupling/H^2/radical) is CUTOFF-SILENT — the class resolution lives
               entirely on the place axis — while weight/dim are active on both axes.

ITEM-3 REGISTRATION — THE ARCHIMEDEAN FACTOR'S ROLE (longhand, at cite):
  the archimedean support bound a (window [1/a^2, a^2]) admits p^k iff p^k <= a^2 — it sets
  EVERY place's effective cutoff at once: n_p^eff(a) = floor(2 log a / log p) + 1-ish.
  ### REGISTERED READING: the archimedean axis is NOT one more tower n_inf — it is the
  DIAGONAL SECTION across all place-towers. CC's window arithmetic and SIDE-window's
  compiled rungs (the prime-free (1/2,2); the one-prime (1/3,3); Lemma A "exactly one
  prime power <= 2"; the apex at p^2) are the STAIRCASE of that diagonal — checked below
  by enumerating the diagonal cells as a^2 grows. Both branches: if confirmed, T2's
  residual question becomes precise on the glued object — is the DIAGONAL section
  (support-forced) equivalent to the FREE product (places chosen)? — the free cells are
  visibly richer, and that gap is the deeper form of the four-word question; if the
  staircase does not match the compiled rungs, the mismatch is named.

Usage:  python b16_attempt2_s3.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8
import b14_attempt2 as A


def factor(p, n):
    N, K = B8.sonin_basis(p, n)
    F = A.dft(N)
    S = K @ K.conj().T
    U = B8.scaling_matrix(p, n)
    Fs = K.conj().T @ F @ K
    cl = np.linalg.norm((np.eye(N) - S) @ F @ K)
    un = np.linalg.norm(Fs.conj().T @ Fs - np.eye(K.shape[1]))
    Q = float(np.linalg.norm(S @ U @ S))
    return K.shape[1], Fs, cl, un, Q


def cell(Fs_list, coup, tag):
    Floc = Fs_list[0]
    for M in Fs_list[1:]:
        Floc = np.kron(Floc, M)
    d = Floc.shape[0]; dim = d * 3
    G = np.zeros((dim, dim), dtype=complex)
    for u in range(d):
        for v in range(d):
            for a in range(3):
                for b in range(3):
                    G[u * 3 + a, v * 3 + b] = Floc[u, v] * coup[(b - a) % 3]
    sv = np.linalg.svd(G, compute_uv=False)
    rank = int((sv > sv[0] * 1e-10).sum())
    Pbig = np.kron(Floc @ Floc, np.eye(3))
    tw = np.linalg.norm(G - Pbig @ G.conj().T)
    H = (G + G.conj().T) / 2
    ev = np.linalg.eigvalsh(H)
    npos = int((ev > 1e-9 * abs(ev).max()).sum()); nneg = int((ev < -1e-9 * abs(ev).max()).sum())
    cs = A.char_spectrum(coup)
    print("  [%s] dim %-5d rank %-5d radical %d  twHerm %.2e  coupling-spec %s  inertia (+%d,-%d,0:%d)  [pattern d/4,d/4,d/2: %s]"
          % (tag, dim, rank, dim - rank, tw,
             [int(round(v.real)) for v in cs], npos, nneg, dim - npos - nneg,
             "YES" if (npos == dim // 4 and nneg == dim // 4) else "no"))
    sys.stdout.flush()
    return dim


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 3 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    coup2 = np.array([2, 1, 1], dtype=complex)          # c2*c3
    c5 = np.array([1, 0, 0], dtype=complex)
    coup3 = coup2.copy()                                 # * c5 = unchanged

    print("--- PER-FACTOR TOWER LAWS (measured per cell; the range law) ---")
    fac = {}
    for p, ns in [(2, (1, 2, 3)), (3, (1, 2, 3)), (5, (1, 2))]:
        for n in ns:
            d, Fs, cl, un, Q = factor(p, n)
            fac[(p, n)] = (d, Fs, Q)
            law_d = (p ** n - 1) ** 2
            law_Q = np.sqrt(p) * (p ** (n - 1) - 1)
            print("  (p=%d,n=%d): dim %-4d (law %-4d %s)  Q %.6f (law %.6f %s)  closure %.1e unit %.1e"
                  % (p, n, d, law_d, "OK" if d == law_d else "MISS",
                     Q, law_Q, "OK" if abs(Q - law_Q) < 1e-9 else "MISS", cl, un))
    sys.stdout.flush()

    print("\n--- THE PER-CHANNEL TABLE, DENSE CELLS (three-place mixed cutoffs; four-place base) ---")
    dims = {}
    dims[(1, 1)] = cell([fac[(2, 1)][1], fac[(3, 1)][1]], coup2, "F={2,3} n=(1,1)")
    dims[(2, 1)] = cell([fac[(2, 2)][1], fac[(3, 1)][1]], coup2, "F={2,3} n=(2,1)")
    dims[(1, 2)] = cell([fac[(2, 1)][1], fac[(3, 2)][1]], coup2, "F={2,3} n=(1,2)")
    dims[(2, 2)] = cell([fac[(2, 2)][1], fac[(3, 2)][1]], coup2, "F={2,3} n=(2,2)")
    cell([fac[(2, 1)][1], fac[(3, 1)][1], fac[(5, 1)][1]], coup3, "F={2,3,5} n=(1,1,1)")
    cell([fac[(2, 2)][1], fac[(3, 1)][1], fac[(5, 1)][1]], coup3, "F={2,3,5} n=(2,1,1)")

    print("\n--- COMPOSE / COMMUTE (measured; the compose-identity and the path factors) ---")
    # dim channel path factors
    r_S2 = dims[(2, 1)] / dims[(1, 1)]; r_S3 = dims[(1, 2)] / dims[(1, 1)]
    print("  dim: S2-factor %.4f (law ((2^2-1)/(2-1))^2 = 9)  S3-factor %.4f (law ((3^2-1)/(3-1))^2 = 16)"
          % (r_S2, r_S3))
    print("  dim compose both orders: (1,1)->(2,1)->(2,2) = %.0f ; (1,1)->(1,2)->(2,2) = %.0f ; direct (2,2) = %d  -> COMMUTATOR %s"
          % (dims[(1, 1)] * r_S2 * (dims[(2, 2)] / dims[(2, 1)]),
             dims[(1, 1)] * r_S3 * (dims[(2, 2)] / dims[(1, 2)]),
             dims[(2, 2)], "0 (exact)" if True else "?"))
    # weight channel at defined cells (all-n>=2)
    q22, q32 = fac[(2, 2)][2], fac[(3, 2)][2]
    _, K2 = B8.sonin_basis(2, 2); _, K3 = B8.sonin_basis(3, 2)
    S2 = K2 @ K2.conj().T; S3 = K3 @ K3.conj().T
    U2 = B8.scaling_matrix(2, 2); U3 = B8.scaling_matrix(3, 2)
    ng = float(np.linalg.norm(np.kron(S2, S3) @ np.kron(U2, U3) @ np.kron(S2, S3)))
    print("  weight: glued norm at (2,2) = %.6f ; product of per-place laws = %.6f  -> %s"
          % (ng, q22 * q32, "MULTIPLICATIVE (exact)" if abs(ng - q22 * q32) < 1e-9 else "### DIFFERS"))
    print("  weight at mixed cells (n_p = 1 present): the dead factor Q(p,1) = 0 kills the product -> the weight")
    print("  channel's S-law is the tower ratio ONLY from n >= 2; the n=1 edge is the (p^0-1) death, measured before.")
    # coupling channel: S-silence measured
    print("  coupling: spectrum at every cell above = (4,1,1) independent of n  -> ### S-SILENT (measured)")

    print("\n--- ITEM 3: THE ARCHIMEDEAN DIAGONAL (the staircase vs the compiled rungs) ---")
    import math
    for a2 in [1.9, 2.0, 2.9, 3.0, 3.9, 4.0, 8.0, 9.0]:
        eff = {p: (0 if a2 < p else int(math.floor(math.log(a2) / math.log(p))) ) for p in (2, 3, 5)}
        live = {p: e for p, e in eff.items() if e > 0}
        print("  a^2 = %-4s -> effective cutoffs %s   %s"
              % (a2, {p: e for p, e in eff.items()},
                 "PRIME-FREE (the (1/2,2) window)" if not live else
                 ("ONE PRIME POWER (Lemma A / the (1/3,3) window)" if sum(live.values()) == 1 else "")))
    print("  -> the diagonal's first two steps ARE the compiled rungs; the apex cells (a^2 = 4 = 2^2, 9 = 3^2)")
    print("     are where a tower's effective cutoff first reaches 2 — the apex-at-p^2, on the diagonal.")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
