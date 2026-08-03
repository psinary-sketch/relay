# THE ONE BUILD, Stage C1 — the atom caches at dps 1300 (J = 600), RESUMABLE:
# appends to the cache files; on start, resumes from the current line count; run
# repeatedly until both files hold 600 lines.  Chunk size sized to the task ceiling.
import os, sys, time
import mpmath as mp

T = os.environ.get("TEMP", ".")
ZPATH = os.path.join(T, "build_zeros_1300.txt")
SPATH = os.path.join(T, "build_smooth_1300.txt")
CHUNK = 80
J = 600

def count(path):
    if not os.path.exists(path): return 0
    with open(path) as f:
        return sum(1 for line in f if line.strip())

def smooth_zero(j):
    f = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - j
    return mp.findroot(f, 14 + 6 * j)

def main():
    mp.mp.dps = 1300
    t0 = time.time()
    nz = count(ZPATH)
    if nz < J:
        upto = min(nz + CHUNK, J)
        with open(ZPATH, "a") as f:
            for n in range(nz + 1, upto + 1):
                f.write(mp.nstr(mp.zetazero(n).imag, 1300) + "\n")
        print(f"zeros: {upto}/{J} banked ({time.time()-t0:.0f} s)")
        if upto < J:
            print("RERUN for the next chunk"); return
    ns = count(SPATH)
    if ns < J:
        with open(SPATH, "a") as f:
            for n in range(ns + 1, J + 1):
                f.write(mp.nstr(smooth_zero(n), 1300) + "\n")
        print(f"smooth: {J}/{J} banked ({time.time()-t0:.0f} s)")
    if count(ZPATH) >= J and count(SPATH) >= J:
        print("STAGE C1 COMPLETE: both atom caches at 600")

if __name__ == "__main__":
    main()
