"""W-CONSTRUCTION-1, ACT 2 — R1-4's BENCH BESIDE THE PROOF: THE FAIR-SLICE COVERAGE.

RELAY-ONLY. Rule 4. SCOPE, once: float, declared; the proof landed separately (Hermite
completeness under the Gaussian weight + projections-map-dense-to-dense — the build
document v0.2); this bench is CORROBORATION of its finite shadow, never the proof.

REGISTERED: for each degree d, the twice-projected Weil family Pi+ S Psi_d has rank k_d;
the FAIR comparison truncates E_1(inf) to its k_d most-reachable modes (ordered by the
soft-compression singular value, the prolate ladder's own order) and measures the
principal angles between the family and THAT slice. (C-dense)'s finite shadow predicts:
high coverage of the fair slice at every degree (the family fills E_1 from the reachable
end first), with the un-truncated angles' slow fill (b33, banked) explained as the tail,
not a wall. Branches: (S-covered) coverage of the fair slice >= ~0.8 of k_d directions
within 0.1 rad, rising with d; (S-wall) coverage stalls low - the proof's finite shadow
would be in tension and said so.

N in {1023, 2047}; a in {2, 3}; d in {8, 16, 24, 32, 40}; window/ball as banked.
Usage: python b34_e1_fair_slice.py register | run
"""
import builtins
import math
import sys

import numpy as np

import b32_arch_e1 as B32

_FOLD = {"—": "--", "’": "'", "·": "*", "→": "->", "≤": "<=", "≥": ">=", "±": "+/-"}


def print(*args, **kw):
    args = tuple("".join(_FOLD.get(c, c) if ord(c) > 127 else c for c in a) if isinstance(a, str) else a
                 for a in args)
    builtins.print(*args, **kw)


def orth(M, tol=1e-10):
    if M.shape[1] == 0:
        return M
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    return U[:, s > (s[0] if s.size else 1) * tol]


def even_grid_basis(N):
    c = (N - 1) // 2
    cols = np.zeros((N, c + 1))
    cols[c, 0] = 1.0
    for j in range(1, c + 1):
        cols[c + j, j] = 1 / math.sqrt(2)
        cols[c - j, j] = 1 / math.sqrt(2)
    return cols


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("b34 — REGISTRATION."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    for N in [1023, 2047]:
        m, h, x = B32.grid(N)
        dft = B32.DFT(N)
        for a, alab in [(2.0, "2"), (3.0, "3")]:
            K, ball, nb = B32.sonin_K(N, dft, x, 1.0 / a)
            S_of = lambda V: K @ (K.conj().T @ V)
            Qe, d_ev, _ = B32.part_basis(K, +1)
            Fs = Qe.conj().T @ dft.F(Qe.astype(complex))
            ev, V = np.linalg.eigh((Fs + Fs.conj().T) / 2)
            E1 = Qe @ V[:, ev > 0]
            g = B32.soft_g(x, a)
            Qg = even_grid_basis(N)
            A = Qg.T @ (g[:, None] * dft.F(g[:, None] * Qg.astype(complex)))
            _, sv, Vh = np.linalg.svd(A)
            modes = Qg @ Vh.conj().T                      # prolate-ordered even modes
            # INSTRUMENT FIX (the first run was VOID: SVD-orth scrambled the registered
            # prolate ORDER): keep only the +1-labeled modes (the E_1-type ladder), project
            # to E_1, and orthonormalize ORDER-PRESERVINGLY (QR = sequential Gram-Schmidt).
            keep = []
            for kk in range(modes.shape[1]):
                v = modes[:, kk]
                q = complex(np.vdot(v, dft.F(v.astype(complex))) / np.vdot(v, v))
                if q.real > 0.5:
                    w = E1 @ (E1.conj().T @ v)
                    if np.linalg.norm(w) > 0.3:
                        keep.append(w / np.linalg.norm(w))
                if len(keep) >= 80:
                    break
            reachM = np.stack(keep, axis=1)
            reach, _ = np.linalg.qr(reachM)                # order-preserving
            cols, _ = B32.basis_columns(x, a, kmax=40)
            print("--- N=%d a=%s: d | k_d | fair-slice dim | #<0.1rad | coverage" % (N, alab))
            for d in [8, 16, 24, 32, 40]:
                W = cols[:, :d + 1].astype(complex)
                fam = orth(E1 @ (E1.conj().T @ S_of(W)))
                kd = fam.shape[1]
                slice_ = reach[:, :kd]
                ang = B32.principal_angles(slice_, fam)
                n01 = int((ang < 0.1).sum())
                print("    %-4d %-5d %-15d %-9d %.3f" % (d, kd, slice_.shape[1], n01,
                                                          n01 / max(kd, 1)))
                sys.stdout.flush()
    print("\nFLOAT BENCH COMPLETE (corroboration; the proof is the build document's).")


if __name__ == "__main__":
    main()
