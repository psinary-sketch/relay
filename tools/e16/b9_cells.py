"""B9 — WHY THE TRACE VANISHES (certificates) + THE CROSS-LAG FORM (one cell).

Relay-only. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
POSITIVITY GUARD: whatever any form's sign on the model, it bears not at all on h2.

ITEM 1 CERTIFICATES (the derivation's checkable pieces, registered before running)
==================================================================================
C1  U-INVARIANCE CHECK (the navigator's proposed premise, checked first-thing):
    ||E_B U K|| where E_B = ball evaluation, K = Sonin basis. ZERO would mean U*Son
    satisfies the ball condition (premise may hold); NONZERO refutes the premise.
    Longhand prediction: NONZERO -- U maps shell 1 into the ball. The Fourier-side
    condition is preserved (certified via ||F_B U K|| separately).
C2  FIXED-POINT LOCALIZATION: Tr(U^k) = p^{-k/2} EXACTLY (longhand: the only fixed
    point of m -> p^k m mod p^{2n} is m = 0, since gcd(p^k - 1, p^{2n}) = 1). Then
    t_k = 0 <=> Tr(U^k Pi) = p^{-k/2} (Pi = projection onto the constraint rowspace):
    THE CONSTRAINT SPACE ABSORBS EXACTLY THE FIXED-POINT CONTRIBUTION. Certified per
    cell at machine precision.
C3  MODEL EXACTNESS OF THE FOURIER CONJUGATION: ||F U F^dag - U^T|| = 0 (longhand:
    (Uf)^ = p^{-1/2} f-hat(p*.)), giving reality of the traces.
C4  NO-RECURRENCE SUPPORT: spectral radius of S U S ~ 0 (the compressed shift is
    quasi-nilpotent -- no recurrent spectral content on the Sonin space).

ITEM 2 — THE CROSS-LAG FORM (registered before its numbers)
===========================================================
On the model, the Hermitian cross-lag form built from the DIAGONAL blocks (where the
third law d_k = (p^{n-k}-1)(p^n-1) lives), lags paired k with -k per the
antipode-involution (B5): B(g,g) = Sum_{k>=1} d_k * 2 Re(g_k gbar_{-k}). Hermitian by
construction (d_k real -- certified); POSITIVITY UNKNOWN AND SAID SO (the pairing is
off-diagonal in (k,-k); no claim). The (beta) reading: the lag-log q amplitude is
sqrt(d_k); normalized by sqrt(N) it is predicted (from the third law, longhand):
    sqrt(d_k)/sqrt(N) = sqrt((1 - p^{-(n-k)})(1 - p^{-n})) * p^{-k/2} ~ q^{-1/2}
-- THE WEIL SHAPE. Registered verdicts: (E1') fitted power ~ -1/2 across cells ->
the convention question CLOSED AT THE MODEL (Weil shape), scope said plainly: the
model is OUR candidate, not the Weil functional; (E2') no systematic power -> the
third law's amplitude was a norm artefact, leak deeper; (E3') third shape.

Usage:  python b9_cells.py register | run
"""
import sys
import numpy as np

import b8_sonin_dim as B8
import b8_e1_cell as E1

CELLS = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2)]


def registration():
    print("=" * 100)
    print("B9 — REGISTRATION. NO MEASURED NUMBER.")
    print("=" * 100)
    print(__doc__)
    print("=" * 100)
    sys.stdout.flush()


def run():
    print("--- ITEM 1 CERTIFICATES ---")
    print("  %-4s %-4s %-12s %-12s %-14s %-14s %-12s %-12s"
          % ("p", "n", "C1 ballUK", "C1b FUK", "C2 |TrUkPi - p^-k/2|max", "", "C3 FUF-U^T", "C4 specrad"))
    for p, n in CELLS:
        N, F, ball = B8.model(p, n)
        _, K = B8.sonin_basis(p, n)
        U = B8.scaling_matrix(p, n)
        EB = np.eye(N)[ball]
        FB = F[ball]
        c1 = np.linalg.norm(EB @ U @ K) if K.shape[1] else float("nan")
        c1b = np.linalg.norm(FB @ U @ K) if K.shape[1] else float("nan")
        # C2: Tr(U^k Pi) vs p^{-k/2}
        C = np.vstack([EB, FB])
        # orthonormal basis of rowspace via SVD
        _, s, Vh = np.linalg.svd(C)
        tol = max(C.shape) * np.finfo(float).eps * s[0]
        R = Vh[: int((s > tol).sum())].conj().T           # columns: ON basis of rowspace
        errs = []
        Uk = np.eye(N)
        for k in range(1, 2 * n):
            Uk = U @ Uk
            trPi = np.trace(R.conj().T @ Uk @ R)
            errs.append(abs(complex(trPi) - p ** (-k / 2.0)))
        c2 = max(errs)
        c3 = np.linalg.norm(F @ U @ F.conj().T - U.T)
        if K.shape[1]:
            S = K @ K.conj().T
            ev = np.linalg.eigvals(S @ U @ S)
            c4 = float(np.max(np.abs(ev)))
        else:
            c4 = float("nan")
        print("  %-4d %-4d %-12.3e %-12.3e %-14.3e %-14s %-12.3e %-12.3e"
              % (p, n, c1, c1b, c2, "", c3, c4))
        sys.stdout.flush()

    print("\n--- ITEM 2: THE CROSS-LAG FORM (amplitudes from the third law, measured d_k) ---")
    print("  %-4s %-4s %-8s %-30s %-30s" % ("p", "n", "N", "sqrt(d_k)/sqrt(N)  k=1..", "q^{-1/2} = p^{-k/2}  k=1.."))
    pts = []
    for p, n in [(2, 2), (2, 3), (3, 2), (3, 3), (5, 2)]:
        N = p ** (2 * n)
        _, d, _ = E1.full_channels(p, n, n - 1 if n > 1 else 1)
        amps = [np.sqrt(max(x, 0.0)) / np.sqrt(N) for x in d[: n - 1]]
        ref = [p ** (-k / 2.0) for k in range(1, n)]
        for k, a in enumerate(amps, 1):
            if a > 0:
                pts.append((p ** k, a))
        print("  %-4d %-4d %-8d %-30s %-30s"
              % (p, n, N, " ".join("%.6f" % a for a in amps), " ".join("%.6f" % r for r in ref)))
    lq = np.log([q for q, _ in pts]); la = np.log([a for _, a in pts])
    alpha = float(np.polyfit(lq, la, 1)[0])
    print("  fitted power alpha in amplitude ~ q^alpha over %d points: %+0.4f   (Weil shape = -0.5; registered = +0.5)"
          % (len(pts), alpha))
    sys.stdout.flush()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    run()


if __name__ == "__main__":
    main()
