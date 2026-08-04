# THE SIXTH POINT Stage A worker (detached): both atom caches to J = 1200 at dps 2700;
# per-line banking; resume-by-linecount; safe to kill and restart.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
ZPATH = os.path.join(T, "k256_zeros.txt")
SPATH = os.path.join(T, "k256_smooth.txt")
LOG = os.path.join(T, "k256_atoms.log")
J = 1200

def count(path):
    if not os.path.exists(path): return 0
    with open(path) as f:
        return sum(1 for line in f if line.strip())

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def smooth_zero(j):
    f = lambda g: g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - j
    return mp.findroot(f, 14 + 6 * j)

def main():
    mp.mp.dps = 2700
    log(f"worker start; zeros at {count(ZPATH)}, smooth at {count(SPATH)}")
    try:
        n = count(ZPATH)
        with open(ZPATH, "a") as f:
            while n < J:
                n += 1
                f.write(mp.nstr(mp.zetazero(n).imag, 2700) + "\n")
                f.flush()
                if n % 50 == 0:
                    log(f"zeros {n}/{J}")
        log(f"zeros complete {J}/{J}")
        n = count(SPATH)
        with open(SPATH, "a") as f:
            while n < J:
                n += 1
                f.write(mp.nstr(smooth_zero(n), 2700) + "\n")
                f.flush()
                if n % 300 == 0:
                    log(f"smooth {n}/{J}")
        log("STAGE A COMPLETE")
    except Exception as ex:
        log(f"WORKER ERROR: {ex}")

if __name__ == "__main__":
    main()
