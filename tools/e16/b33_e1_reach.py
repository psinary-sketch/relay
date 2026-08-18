"""W-ATTEMPT-2, SITTING 23 — WHAT REACHES E_1 AT INFINITY.

RELAY-ONLY. SUB-GATE (restated). THE CORRECTED STOP IN FORCE: measured properties of
constructed objects are DATA at bench grade; refused: any promotion to W_inf - Sum W_p
at complete roster, or register movement. SCOPE LINE, once: exact at finite instance and
one place at a time; nothing here concerns complete roster. The register is untouched.

THE QUESTION, REGISTERED: sitting 22 landed the archimedean E_1 identity and REFUSED the
unprojected "Weil's family reaches E_1" reading (the family spreads across both sectors
and leaks off the Sonin space). What DOES reach E_1?

REGISTERED BRANCHES (not mutually exclusive; each lands or fails on its own):
 (R-proj)    the SONIN-PROJECTED Weil family S*Psi_d reaches E_1: its E_-1 component
             tends to 0 with degree — then W-exact and E_1 are reconciled by ONE
             projection and the archimedean sector has an explicit dense family.
 (R-proj')   the executor's longhand sub-branch, registered beside the ferried one: the
             projected family fills BOTH sectors (the E_-1 fraction tending to a
             positive constant), and the reconciliation needs the SECOND projection
             Pi_plus: the twice-projected family Pi_plus*S*Psi_d reaches E_1 (its
             principal angles to E_1 closing with degree) — one more projection than
             (R-proj), recorded plainly if that is what lands.
 (R-prolate) E_1 is spanned by the even prolate-type modes at every SECOND even index —
             the classical alternation: on evens the transform's eigenvalue alternates
             +1, -1 along the mode ladder (the Hermite shadow: eigenvalue (-i)^n, so
             n = 0 mod 4 -> +1, n = 2 mod 4 -> -1), so the constrained sector at
             infinity is NAMED BY CC'S OWN BASIS as the every-other-even prolate list —
             checked on the soft-compression modes, the list computed.
 (R-neither) filed openly.

MEASURED (float declared; N in {511, 1023, 2047}; a in {sqrt2, 2, 3}; the soft window
W-lg1 where the window enters; the ball radius lambda = 1/a as banked):
 M1 the sector split of the projected family: for d in {8, 16, 24, 32, 40}, the
    orthonormalized S*Psi_d subspace's mass fractions ||Pi_plus Q||_F^2 / dim and
    ||Pi_minus Q||_F^2 / dim, by degree, with N-stability — (R-proj) vs (R-proj')
    decided by whether the minus-fraction goes to 0 or stabilizes positive.
 M2 the reach: principal angles of S*Psi_d to E_1 AND of Pi_plus*S*Psi_d to E_1
    (smallest and largest; the count of directions within 0.1 rad), by degree,
    N-stability stated per number (the b27/b32 affordance limit declared: values with
    < 3 stable digits are DATA-with-caveat, trends are the reading). NOTE, said in the
    registration itself: the Pi_plus variant is CONTAINED in E_1 by construction, so
    its angles to E_1 are 0 identically; that clause's informative content is the RANK
    RETENTION of the twice-projected family (does projection collapse its dimension?),
    reported as such.
 M3 the prolate classification: the soft-compression (G F G on the even part) modes in
    decreasing singular value; for each of the top 12: <v, F v> (expected near +1 or
    -1), the sign list printed — the alternation pattern checked (every-other-even),
    and the E_1 membership list named; N-stability of the pattern.
 M4 the control: the odd part's top modes' <v, F v> near +/-i (imaginary), confirming
    the parity structure rides the prolate ladder too.

ROUTING NOTE, recorded not smoothed: the ferry routed this bench to Opus; the Opus lane
failed twice on server overload (API 529) and the bench executed on Fable with this
registration unchanged.

RECORDED PLAINLY AS DATA. The register is untouched; nothing circulates.
Usage:  python b33_e1_reach.py register | run
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


AS = [(math.sqrt(2), "sqrt2"), (2.0, "2"), (3.0, "3")]
NS = [511, 1023, 2047]
DS = [8, 16, 24, 32, 40]
CHECKS = [0, 0]


def check(name, ok, detail=""):
    CHECKS[0] += 1
    CHECKS[1] += ok
    print("  %s  %s %s" % ("PASS" if ok else "FAIL", name, detail))
    assert ok, name


def orth(M, tol_ratio=1e-10):
    if M.shape[1] == 0:
        return M
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    keep = s > (s[0] if s.size else 1.0) * tol_ratio
    return U[:, keep]


def even_grid_basis(N):
    c = (N - 1) // 2
    cols = np.zeros((N, c + 1))
    cols[c, 0] = 1.0
    for j in range(1, c + 1):
        cols[c + j, j] = 1 / math.sqrt(2)
        cols[c - j, j] = 1 / math.sqrt(2)
    return cols


def odd_grid_basis(N):
    c = (N - 1) // 2
    cols = np.zeros((N, c))
    for j in range(1, c + 1):
        cols[c + j, j - 1] = 1 / math.sqrt(2)
        cols[c - j, j - 1] = -1 / math.sqrt(2)
    return cols


def measure(N, a, alab):
    m, h, x = B32.grid(N)
    dft = B32.DFT(N)
    lam = 1.0 / a
    K, ball, nb = B32.sonin_K(N, dft, x, lam)
    S_of = lambda V: K @ (K.conj().T @ V)
    FK = dft.F(K)
    check("Son F-invariance (N=%d a=%s)" % (N, alab),
          np.linalg.norm(FK - S_of(FK)) < 1e-10)
    check("Son P-invariance", np.linalg.norm(B32.apply_P(K) - S_of(B32.apply_P(K))) < 1e-10)

    Qe, d_ev, gap_e = B32.part_basis(K, +1)
    Qo, d_od, gap_o = B32.part_basis(K, -1)
    Fs_e = Qe.conj().T @ dft.F(Qe.astype(complex))
    check("even compressed F Hermitian", np.linalg.norm(Fs_e - Fs_e.conj().T) < 1e-9)
    ev, V = np.linalg.eigh((Fs_e + Fs_e.conj().T) / 2)
    plus = ev > 0
    E1 = Qe @ V[:, plus]
    Em1 = Qe @ V[:, ~plus]
    check("even spectrum +/-1", float(np.abs(np.abs(ev) - 1).max()) < 1e-9,
          "dplus=%d dminus=%d" % (int(plus.sum()), int((~plus).sum())))

    cols, _ = B32.basis_columns(x, a, kmax=max(DS))
    rows1, rows2 = [], []
    for d in DS:
        W = cols[:, :d + 1].astype(complex)
        Qd = orth(S_of(W))
        nc = Qd.shape[1]
        fp = float(np.linalg.norm(E1.conj().T @ Qd) ** 2) / nc
        fm = float(np.linalg.norm(Em1.conj().T @ Qd) ** 2) / nc
        check("fractions sum to 1 (d=%d)" % d, abs(fp + fm - 1) < 1e-8, "")
        ang = B32.principal_angles(E1, Qd)
        n01 = int((ang < 0.1).sum())
        P1W = E1 @ (E1.conj().T @ Qd)
        r2 = orth(P1W).shape[1]
        rows1.append((d, nc, fp, fm))
        rows2.append((d, float(ang.min()) if ang.size else float("nan"),
                      float(ang.max()) if ang.size else float("nan"), n01, r2))
    print("  M1 (N=%d a=%s): d | ncols | E1 fraction | E-1 fraction" % (N, alab))
    for d, nc, fp, fm in rows1:
        print("    %-4d %-6d %-12.6f %-12.6f" % (d, nc, fp, fm))
    print("  M2: d | min angle to E1 | max | #<0.1rad | rank(Pi+ S Psi_d)")
    for d, amin, amax, n01, r2 in rows2:
        print("    %-4d %-16.6f %-9.6f %-9d %d" % (d, amin, amax, n01, r2))
    sys.stdout.flush()

    g = B32.soft_g(x, a)
    for tag, Qg, nmodes, expect in [("even", even_grid_basis(N), 12, "+/-1"),
                                    ("odd", odd_grid_basis(N), 6, "+/-i")]:
        A = (g[:, None] * dft.F(g[:, None] * Qg.astype(complex)))
        C = Qg.T @ A
        U, sv, Vh = np.linalg.svd(C)
        print("  M%s (%s part, N=%d a=%s): k | sigma | <v,Fv> re,im | ||Pi+v||,||Pi-v||"
              % ("3" if tag == "even" else "4", tag, N, alab))
        pat = []
        for k in range(nmodes):
            v = Qg @ Vh[k].conj()
            Fv = dft.F(v.astype(complex))
            q = complex(np.vdot(v, Fv) / np.vdot(v, v))
            pp = float(np.linalg.norm(E1.conj().T @ v)) if tag == "even" else float("nan")
            pm = float(np.linalg.norm(Em1.conj().T @ v)) if tag == "even" else float("nan")
            pat.append("+" if q.real > 0 else "-")
            print("    %-3d %-9.6f %+9.6f %+9.6f   %s"
                  % (k, sv[k], q.real, q.imag,
                     ("%.4f, %.4f" % (pp, pm)) if tag == "even" else "(odd control)"))
        if tag == "even":
            print("    sign pattern (top %d): %s" % (nmodes, " ".join(pat)))
        sys.stdout.flush()
    return rows1, rows2


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    print("=" * 100); print("W-ATTEMPT-2 SITTING 23 — REGISTRATION. NO MEASURED NUMBER."); print("=" * 100)
    print(__doc__); print("=" * 100); sys.stdout.flush()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    Fd = B32.dense_F(511)
    dft = B32.DFT(511)
    check("FFT DFT vs dense (N=511)",
          np.linalg.norm(dft.F(np.eye(511, dtype=complex)) - Fd) < 1e-11)
    allr = {}
    for N in NS:
        for a, alab in AS:
            print("--- N = %d, a = %s ---" % (N, alab))
            allr[(N, alab)] = measure(N, a, alab)
            print()
    print("--- N-stability of the M1 fractions (per a, largest two N, max |delta|) ---")
    for _, alab in AS:
        r1a = allr[(1023, alab)][0]
        r2a = allr[(2047, alab)][0]
        dmax = max(abs(p1 - p2) for (_, _, p1, _), (_, _, p2, _) in zip(r1a, r2a))
        print("  a=%s: max |E1-fraction delta| (N 1023 vs 2047) = %.4f" % (alab, dmax))
    print("\nFLOAT BENCH COMPLETE; ASSERTED CHECKS: %d/%d PASS" % (CHECKS[1], CHECKS[0]))


if __name__ == "__main__":
    main()
