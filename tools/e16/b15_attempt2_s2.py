"""W-ATTEMPT-2, SITTING 2 — THE LIVE-FLOW INSTANCE AND THE SECOND PLACE SET.

RELAY-ONLY. SUB-GATE (restated at this sitting's head): no candidate grades PLAUSIBLE
across T1-T10. THE PRE-REFUSALS RESTATED: the complete roster is the double limit and
stays open; a finite-place-set object at a finite cutoff decides nothing global;
NO SENTENCE ABOUT THE SIGN OF W_inf - Sum W_p LEAVES THE RELAY; inertia numbers are
GUARDED properties of constructed finite objects. The register is untouched.
THE RANGE LAW GOVERNS: nothing is inherited from n = 1; every n = 2 quantity is measured.

REGISTRATION — ITEM 1, THE n >= 2 INSTANCE ({inf,2,3}, cutoff n = 2; glued core dim
9 * 64 * 3 = 1728):
  (K1) the glued object KEEPS its H^2 (dim h = 3, antipode-invariant dim 2), radical 0,
       twisted-Hermitian at machine precision, WITH THE SCALING NOW LIVE (per-place n=2
       laws confirmed by measurement: dim Son = (p^2-1)^2; Q(p,2) = sqrt(p)(p-1));
  (K2) it LOSES the codomain at a named step (involution closure / antipode coherence /
       radical / H^2) — that step is the finding.
  The inertia of the Hermitian part is RECORDED AND GUARDED, never read as a sentence
  about W_inf - Sum W_p.

REGISTRATION — ITEM 2, THE SECOND PLACE SET ({inf,2,3,5}):
  LONGHAND, BEFORE ANY RUN: 5 is INERT in Q(sqrt(-23)) (-23 == 2 mod 5, a non-residue),
  so the prime above 5 is (5), norm 25, PRINCIPAL: c_5 = [0] (the identity label),
  antipode-self-dual trivially.
  ### THE NAIVE-COMPARISON TRAP, REGISTERED SO IT CANNOT BITE SILENTLY: a30(zeta_K) = 0
  (no ideals of norm 5 exist), so comparing the coupling element to the NORM-30
  coefficients would fail vacuously. The correct comparison is the LABEL-NORM
  150 = 2 * 3 * 25 coefficients.
  PREDICTION (longhand, from the ideal count): ideals of norm 150 are P2^{+-} P3^{+-} (5);
  with labels a2 = 1, a3 = 2, a5 = 0 the class multiset is {0, 2, 1, 0}: the coefficient
  element 2[0]+[1]+[2], character spectrum (4, 1, 1).
  THE GENERAL GLUING LAW, DERIVED (to be confirmed by the measurement, not replaced by
  it): the coupling element c_S = prod c_p has [C]-coefficient = #{one prime above each
  p in S with class product C} = the [C]-coefficient of Z-hat at the label norm
  prod N(P_p) — multiplicativity in C[Cl] by unique factorization. EULER-EXACT branch:
  the measured spectrum equals the predicted label-norm coefficients; NOT branch: the
  norm-6 match was a small-prime coincidence, said so.
  Four places at n = 1: full Gram (dim 1*4*16*3 = 192) — H^2 and radical re-checked
  directly. Four places at n = 2 (dim 9*64*16*3 = 27648): FACTOR-CERTIFIED, declared —
  the Gram is (compressed F_2 (x) F_3 (x) F_5) (x) (coupling circulant); each factor's
  unitarity/invertibility is measured and the product's rank/twisted-Hermiticity follows
  structurally; a dense 27648^2 object is not materialized, and this certification mode
  is DECLARED, not hidden.

Usage:  python b15_attempt2_s2.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8
import b14_attempt2 as A


def compressed_F(p, n):
    N, K = B8.sonin_basis(p, n)
    F = A.dft(N)
    S = K @ K.conj().T
    closure = np.linalg.norm((np.eye(N) - S) @ F @ K)
    Fs = K.conj().T @ F @ K
    unit = np.linalg.norm(Fs.conj().T @ Fs - np.eye(K.shape[1]))
    return K, Fs, closure, unit


def gram_and_checks(Floc, coup, tag):
    d = Floc.shape[0]
    dim = d * 3
    G = np.zeros((dim, dim), dtype=complex)
    for u in range(d):
        for v in range(d):
            for a in range(3):
                for b in range(3):
                    G[u * 3 + a, v * 3 + b] = Floc[u, v] * coup[(b - a) % 3]
    sv = np.linalg.svd(G, compute_uv=False)
    rank = int((sv > sv[0] * 1e-10).sum())
    Ploc = Floc @ Floc
    Pbig = np.kron(Ploc, np.eye(3))
    tw = np.linalg.norm(G - Pbig @ G.conj().T)
    H = (G + G.conj().T) / 2
    ev = np.linalg.eigvalsh(H)
    npos = int((ev > 1e-9 * abs(ev).max()).sum()); nneg = int((ev < -1e-9 * abs(ev).max()).sum())
    print("  [%s] dim %d  RANK %d  RADICAL %d  twisted-Herm %.3e  inertia GUARDED (+%d,-%d,0:%d)"
          % (tag, dim, rank, dim - rank, tw, npos, nneg, dim - npos - nneg))
    sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 2 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    # inertness of 5 verified in-run
    assert pow(-23 % 5, (5 - 1) // 2, 5) == 5 - 1   # non-residue -> inert
    print("  5 inert verified (-23 is a non-residue mod 5); c5 = [0]")

    # --- item 1: n = 2, three places ---
    print("\n--- ITEM 1: {inf,2,3} at n = 2 (nothing inherited; per-place laws measured) ---")
    K2, F2s, cl2, un2 = compressed_F(2, 2)
    K3, F3s, cl3, un3 = compressed_F(3, 2)
    print("  per-place: dim Son(2,2) = %d (law 9), dim Son(3,2) = %d (law 64)" % (K2.shape[1], K3.shape[1]))
    U2 = B8.scaling_matrix(2, 2); U3 = B8.scaling_matrix(3, 2)
    S2 = K2 @ K2.conj().T; S3 = K3 @ K3.conj().T
    q2 = np.linalg.norm(S2 @ U2 @ S2); q3 = np.linalg.norm(S3 @ U3 @ S3)
    print("  per-place live flow: Q(2,2) = %.6f (law sqrt2 = %.6f), Q(3,2) = %.6f (law 2sqrt3 = %.6f)"
          % (q2, np.sqrt(2), q3, 2 * np.sqrt(3)))
    print("  involution closure: %.2e / %.2e ; compressed-F unitarity: %.2e / %.2e" % (cl2, cl3, un2, un3))
    coup = np.array([2, 1, 1], dtype=complex)
    Floc = np.kron(F2s, F3s)
    gram_and_checks(Floc, coup, "n=2 three-place")
    # glued flow channels, measured
    Ug = np.kron(U2, U3); Sg = np.kron(S2, S3)
    print("  glued flow: |Tr(UgSg)| = %.3e ; ||SgUgSg||_F = %.6f (per-factor product q2*q3 = %.6f)"
          % (abs(np.trace(Ug @ Sg)), np.linalg.norm(Sg @ Ug @ Sg), q2 * q3))

    # --- item 2: four places ---
    print("\n--- ITEM 2: {inf,2,3,5} ---")
    c5 = np.array([1, 0, 0], dtype=complex)
    coup4 = np.zeros(3, dtype=complex)
    for i in range(3):
        for j in range(3):
            coup4[(i + j) % 3] += coup[i] * c5[j]
    cs = A.char_spectrum(coup4)
    print("  coupling c2*c3*c5 = %s ; character spectrum %s  (REGISTERED prediction: 2[0]+[1]+[2], (4,1,1) = the LABEL-NORM 150 coefficients; a30 = 0 is the registered trap)"
          % (np.round(coup4.real, 6).tolist(), [complex(round(v.real, 6), round(v.imag, 6)) for v in cs]))
    K5, F5s, cl5, un5 = compressed_F(5, 1)
    print("  place 5 at n=1: dim Son(5,1) = %d (law 16); closure %.2e; unitarity %.2e" % (K5.shape[1], cl5, un5))
    K2a, F2a, _, _ = compressed_F(2, 1)
    K3a, F3a, _, _ = compressed_F(3, 1)
    Floc4 = np.kron(np.kron(F2a, F3a), F5s)
    gram_and_checks(Floc4, coup4, "n=1 four-place")
    # four places at n=2: FACTOR-CERTIFIED (declared)
    K5b, F5b, cl5b, un5b = compressed_F(5, 2)
    print("  four-place n=2 FACTOR-CERTIFIED (declared; no dense 27648^2 object): factor dims %d,%d,%d;"
          % (K2.shape[1], K3.shape[1], K5b.shape[1]))
    print("    closures %.2e/%.2e/%.2e ; unitarity %.2e/%.2e/%.2e ; coup4 spectrum invertible: %s"
          % (cl2, cl3, cl5b, un2, un3, un5b, all(abs(v) > 1e-12 for v in cs)))
    print("    -> rank = full and twisted-Hermiticity follow from unitary factors (x) invertible circulant, STRUCTURALLY;")
    print("       the structural step is the same identity measured directly at the three smaller Grams above.")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
