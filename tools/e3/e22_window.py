# E-22 — THE WINDOW-COLLAPSE LAW: the n=48 out-of-sample test.
# Registered BEFORE this run (in the sitting report): log-quadratic fit predicts
# w(48) ~ 0.0188; pure-exponential predicts 0.0275; claim: w(48) in [0.012, 0.030].
# The n=48 pencil: W(delta) = W_ext48 + delta * B, B the unique Gleason element with
# A_0 = 0, A_4 = 1, A_8 = 0 (the canonical direction in the 3-dim space; choice stated).
# Window = the floor-k=3 flip root in delta, bisected exactly.

from fractions import Fraction as Fr
import importlib.util, sys, pathlib

spec = importlib.util.spec_from_file_location(
    "dl", str(pathlib.Path(__file__).with_name("duursma_ladder.py")))
dl = importlib.util.module_from_spec(spec); sys.modules["dl"] = dl; spec.loader.exec_module(dl)
spec2 = importlib.util.spec_from_file_location(
    "gs", str(pathlib.Path(__file__).with_name("genus5.py")))
gs = importlib.util.module_from_spec(spec2); sys.modules["gs"] = gs; spec2.loader.exec_module(gs)
spec3 = importlib.util.spec_from_file_location(
    "mech", str(pathlib.Path(__file__).with_name("mechanism.py")))
mech = importlib.util.module_from_spec(spec3); sys.modules["mech"] = mech; spec3.loader.exec_module(mech)

def build_pencil48():
    W8 = dl.W8
    b1 = dl.poly_pow(W8, 6)                                   # W8^6
    b2 = dl.poly_mul(dl.poly_pow(W8, 3), dl.G24)              # W8^3 g24
    b3 = dl.poly_mul(dl.G24, dl.G24)                          # g24^2
    basis = [b1, b2, b3]
    # B: A_0 = 0, A_4 = 1, A_8 = 0
    M = [[basis[j][t] for j in range(3)] for t in (0, 4, 8)]
    sol, ok, rank = dl.solve_linear(M, [Fr(0), Fr(1), Fr(0)])
    assert ok and sol is not None
    B = [sum(sol[j] * basis[j][i] for j in range(3)) for i in range(49)]
    W_ext, d_ext = dl.extremal_type2_enumerator(48)
    assert d_ext == 12
    return W_ext, B

def floor3_sign(W_ext, B, delta):
    W = [W_ext[i] + Fr(delta) * B[i] for i in range(49)]
    H = mech.H_of(W, 48, 4)
    m, L = mech.monic_moments(H, 7)
    D = mech.rdet([[m[i + j + 1] for j in range(3)] for i in range(3)])
    return (D > 0) - (D < 0)

def main():
    W_ext, B = build_pencil48()
    lo, hi = Fr(1, 1000), Fr(1)
    s_lo, s_hi = floor3_sign(W_ext, B, lo), floor3_sign(W_ext, B, hi)
    print(f"floor k=3 sign at delta=1/1000: {s_lo}; at delta=1: {s_hi}")
    if s_lo == s_hi:
        print("no flip in (1/1000, 1) — outside the registered bracket; widen scan")
        for d in (Fr(1, 10000), Fr(2), Fr(5)):
            print(f"  sign at {d}: {floor3_sign(W_ext, B, d)}")
        return
    a, b = lo, hi
    for _ in range(22):
        mid = (a + b) / 2
        if floor3_sign(W_ext, B, mid) == s_lo:
            a = mid
        else:
            b = mid
    print(f"n=48 window: flip root in ({a}, {b}) = ({float(a):.6f}, {float(b):.6f})")
    w = float((a + b) / 2)
    print(f"w(48) ~ {w:.5f} | registered primary prediction 0.0188 | bracket [0.012, 0.030]")
    print(f"within registered bracket: {0.012 <= w <= 0.030}")

if __name__ == "__main__":
    main()
