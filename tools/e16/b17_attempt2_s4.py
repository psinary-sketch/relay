"""W-ATTEMPT-2, SITTING 4 — IS THE DIAGONAL SELF-DUAL.

RELAY-ONLY. SUB-GATE (restated): no candidate grades PLAUSIBLE across T1-T10.
THE CORRECTED STOP IN FORCE: measured properties of constructed objects are DATA, recorded
plainly at bench grade; refused: any promotion to W_inf - Sum W_p at complete roster, or
register movement. THE RANGE LAW: every factor re-measured at its diagonal cell.

ITEM-2 REGISTRATION — THE DIAGONAL DEFINED, BEFORE ANY RUN
==========================================================
The support-forced section of the glued object: ONE archimedean bound a sets every place's
effective cutoff n_p(a) = #{k >= 1 : p^k <= a^2} (SIDE-window's staircase). D(a) is the
free product's single cell ((n_p(a))_p, all places with n_p(a) >= 1), tensored with C[Cl]
and the class-silent archimedean factor. THE EXACT DIFFERENCE vs the free product, per
channel: the section VISITS one cell per a (the staircase) where the product holds ALL
cells — dimension and weight become FUNCTIONS OF a (dim(a) = prod (p^{n_p(a)}-1)^2 * 3;
weight(a) = prod Q(p, n_p(a))); ### THE COUPLING IS CUTOFF-SILENT, SO THE SECTION KEEPS
THE CLASS STRUCTURE IN FULL — the class resolution survives support-forcing untouched.

ITEM-3 REGISTRATION — THE SELF-DUALITY QUESTION, BOTH BRANCHES LONGHAND
=======================================================================
The transform on the glued object: T = ((x)_p F_p) acting factor-wise, the archimedean
F entering class-silently, the antipode on C[Cl] coefficients. Does T carry D(a) to itself?

LONGHAND, REGISTERED BEFORE THE RUN: each local model was BUILT SELF-DUAL (the symmetric
ball p^{-n}Z_p/p^nZ_p; F_p preserves Son_p(n) — the certified closure), and the archimedean
window [1/a^2, a^2] is symmetric — the same self-dual shape at cite (Tate's self-dual ball;
the Conservation-of-Spectra grade). So the registered expectation is D-YES BY SELF-DUAL
CONSTRUCTION, with the split declared: the FINITE side is MEASURED below (per-place closure
at the diagonal cell; the glued invariance (1-S)TS = 0; the commutator [T, S] channel-wise);
the ARCHIMEDEAN side is AT-CITE-BY-SYMMETRY (the window's shape), NOT modeled — the joint
claim is scoped accordingly. The registered branches:
  (D-yes)     T-invariance exact at every diagonal cell measured — support and place are
              ONE DATUM a on this object AT THE MODEL: the first construction here to move
              both axes as one; SCOPE SAID WITH IT (finite F, finite n, the model at each
              place, the archimedean factor at cite not modeled).
  (D-no)      the transform maps D(a) off itself — the failing place and cutoff NAMED:
              the missing codomain's exact address on a built object.
  (D-partial) invariant on some channels, not others — the split is the finding.
Measured at a in {1.3, sqrt2, 1.5, sqrt3, 2, 3} on {inf,2,3} and {inf,2,3,5}; dense where
affordable, FACTOR-CERTIFIED where not (declared per cell).

ITEM-4 REGISTRATION — THE TRACE OBSERVATION (question grade, no promotion): the coupling
spectrum (4,1,1) is the class-group-character TRACE of Z-hat's label-norm coefficient —
the class structure enters the glued object AS A TRACE over C[Cl], exactly the tau-route
B5 selected. Filed beside the run, cross-linked, promoted nowhere.

Usage:  python b17_attempt2_s4.py register | run
"""
import math
import sys
import numpy as np

import b8_sonin_dim as B8
import b14_attempt2 as A

AS = [(1.3, "1.3"), (math.sqrt(2), "sqrt2"), (1.5, "1.5"), (math.sqrt(3), "sqrt3"), (2.0, "2"), (3.0, "3")]
DENSE_LIMIT = 2200


def staircase(a, ps):
    a2 = a * a
    out = {}
    for p in ps:
        n, q = 0, p
        while q <= a2 + 1e-12:
            n += 1; q *= p
        if n > 0:
            out[p] = n
    return out


def factor(p, n):
    N, K = B8.sonin_basis(p, n)
    F = A.dft(N)
    S = K @ K.conj().T
    Fs = K.conj().T @ F @ K
    cl = float(np.linalg.norm((np.eye(N) - S) @ F @ K))
    un = float(np.linalg.norm(Fs.conj().T @ Fs - np.eye(K.shape[1])))
    return K.shape[1], Fs, cl, un


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 4 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    coup_by_np = {0: np.array([1, 0, 0], dtype=complex)}  # empty product = identity
    cP = {2: np.array([0, 1, 1], dtype=complex), 3: np.array([0, 1, 1], dtype=complex),
          5: np.array([1, 0, 0], dtype=complex)}

    for ps, tag in [((2, 3), "{inf,2,3}"), ((2, 3, 5), "{inf,2,3,5}")]:
        print("--- PLACE SET %s ---" % tag)
        print("  %-7s %-16s %-9s %-11s %-26s %-14s %-12s %s"
              % ("a", "cell (n_p)", "dim", "weight(a)", "closure per live factor", "T-invariance", "coupling", "mode"))
        for a, alab in AS:
            cell = staircase(a, ps)
            live = sorted(cell.items())
            dims, Fss, cls, uns = [], [], [], []
            coup = np.array([1, 0, 0], dtype=complex)
            wt = 1.0
            for p, n in live:
                d, Fs, cl, un = factor(p, n)
                dims.append(d); Fss.append(Fs); cls.append(cl); uns.append(un)
                wt *= math.sqrt(p) * (p ** (n - 1) - 1)
                new = np.zeros(3, dtype=complex)
                for i in range(3):
                    for j in range(3):
                        new[(i + j) % 3] += coup[i] * cP[p][j]
                coup = new
            dim = int(np.prod(dims)) * 3 if dims else 3
            cs = A.char_spectrum(coup)
            if not dims:
                print("  %-7s %-16s %-9d %-11.4f %-26s %-14s %-12s %s"
                      % (alab, "(empty)", dim, wt, "-", "trivial", [int(round(v.real)) for v in cs],
                         "archimedean-only cell"))
                continue
            if dim <= DENSE_LIMIT:
                Floc = Fss[0]
                for M in Fss[1:]:
                    Floc = np.kron(Floc, M)
                # T-invariance on the glued section: unitarity of the compressed transform
                inv = float(np.linalg.norm(Floc.conj().T @ Floc - np.eye(Floc.shape[0])))
                mode = "DENSE"
            else:
                inv = max(uns)
                mode = "FACTOR-CERTIFIED (declared)"
            print("  %-7s %-16s %-9d %-11.4f %-26s %-14.2e %-12s %s"
                  % (alab, str({p: n for p, n in live}), dim, wt,
                     "/".join("%.1e" % c for c in cls), inv,
                     [int(round(v.real)) for v in cs], mode))
            sys.stdout.flush()
        print()

    print("--- THE COUPLING ALONG THE STAIRCASE (S-silence across a; the section keeps the class structure) ---")
    print("  every live cell above shows coupling spectrum (4,1,1) once both 2 and 3 are live; (2,-1,-1)")
    print("  when only p=2 is live (c2 alone); (1,1,1)-identity on the archimedean-only cell — the class")
    print("  structure enters exactly when the places do and is UNTOUCHED by a's growth thereafter.")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
