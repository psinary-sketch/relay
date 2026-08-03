# W-K200 Stage A worker (detached): loops until both atom caches reach J = 960,
# logging progress; resume-by-linecount; safe to kill and restart at any time.
import os, time
import mpmath as mp

T = os.environ.get("TEMP", ".")
ZPATH = os.path.join(T, "k200_zeros.txt")
SPATH = os.path.join(T, "k200_smooth.txt")
LOG = os.path.join(T, "k200_atoms.log")
J = 960

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
    mp.mp.dps = 2100
    log(f"worker start; zeros at {count(ZPATH)}, smooth at {count(SPATH)}")
    try:
        n = count(ZPATH)
        with open(ZPATH, "a") as f:
            while n < J:
                n += 1
                f.write(mp.nstr(mp.zetazero(n).imag, 2100) + "\n")
                f.flush()
                if n % 40 == 0:
                    log(f"zeros {n}/{J}")
        log(f"zeros complete {J}/{J}")
        n = count(SPATH)
        with open(SPATH, "a") as f:
            while n < J:
                n += 1
                f.write(mp.nstr(smooth_zero(n), 2100) + "\n")
                f.flush()
                if n % 200 == 0:
                    log(f"smooth {n}/{J}")
        log("STAGE A COMPLETE")
    except Exception as ex:
        log(f"WORKER ERROR: {ex}")

if __name__ == "__main__":
    main()
