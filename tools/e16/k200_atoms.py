# W-K200 Stage A: atom caches at dps 2100 (J = 960), banked chunks, resume-by-linecount.
# Run repeatedly until complete.  Measured cost ~24-28 s/zero -> CHUNK = 20 per task.
import os, time
import mpmath as mp

T = os.environ.get("TEMP", ".")
ZPATH = os.path.join(T, "k200_zeros.txt")
SPATH = os.path.join(T, "k200_smooth.txt")
CHUNK = 20
SCHUNK = 300
J = 960

def count(path):
    if not os.path.exists(path): return 0
    with open(path) as f:
        return sum(1 for line in f if line.strip())

def smooth_zero(j):
    f = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - j
    return mp.findroot(f, 14 + 6 * j)

def main():
    mp.mp.dps = 2100
    t0 = time.time()
    nz = count(ZPATH)
    if nz < J:
        upto = min(nz + CHUNK, J)
        with open(ZPATH, "a") as f:
            for n in range(nz + 1, upto + 1):
                f.write(mp.nstr(mp.zetazero(n).imag, 2100) + "\n")
                f.flush()
        print(f"zeros: {upto}/{J} banked ({time.time()-t0:.0f} s)")
        if upto < J:
            print("RERUN"); return
    ns = count(SPATH)
    if ns < J:
        upto = min(ns + SCHUNK, J)
        with open(SPATH, "a") as f:
            for n in range(ns + 1, upto + 1):
                f.write(mp.nstr(smooth_zero(n), 2100) + "\n")
                f.flush()
        print(f"smooth: {upto}/{J} banked ({time.time()-t0:.0f} s)")
        if upto < J:
            print("RERUN"); return
    print("STAGE A COMPLETE")

if __name__ == "__main__":
    main()
