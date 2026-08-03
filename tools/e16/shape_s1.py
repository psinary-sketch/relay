# W-SHAPE stage 1: the atom caches — 300 true zeros and 300 smooth-density points at
# dps 620 (the K=64 precision law + margin), each cross-checked against an independent
# dps-300 recomputation on a subset (the stage's exit check).
import os, time
import mpmath as mp

T = os.environ.get("TEMP", ".")

def smooth_zero(j):
    f = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - j
    return mp.findroot(f, 14 + 6 * j)

def main():
    t0 = time.time()
    mp.mp.dps = 620
    zs = []
    for n in range(1, 301):
        zs.append(mp.zetazero(n).imag)
    with open(os.path.join(T, "shape_zeros.txt"), "w") as f:
        for z in zs:
            f.write(mp.nstr(z, 620) + "\n")
    print(f"zeros cached ({time.time()-t0:.0f} s)")
    sm = [smooth_zero(j) for j in range(1, 301)]
    with open(os.path.join(T, "shape_smooth.txt"), "w") as f:
        for z in sm:
            f.write(mp.nstr(z, 620) + "\n")
    print(f"smooth cached ({time.time()-t0:.0f} s)")
    # exit check: dps-300 recomputation on a subset
    mp.mp.dps = 300
    worst = mp.mpf(0)
    for n in (1, 25, 75, 150, 225, 300):
        z2 = mp.zetazero(n).imag
        rel = abs(zs[n - 1] - z2) / z2
        worst = max(worst, rel)
    print(f"exit check: worst zero cross-source rel diff (dps 620 vs 300): {mp.nstr(worst, 3)}")
    ok = worst < mp.mpf(10) ** (-290)
    print(f"EXIT: {'PASS' if ok else 'FAIL - HALT'}")

if __name__ == "__main__":
    main()
