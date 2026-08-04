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

def validate_tail(path, min_len=2000):
    """RESUME-PATH GUARD (2026-08-04): a truncated/malformed final line (hard cut mid-write)
    is DROPPED and recomputed, never trusted.  Validation: length >= min_len (full mp.nstr
    at dps 2700 is ~2700 chars), parseable as mpf, magnitude in the sane atom range."""
    if not os.path.exists(path):
        return
    with open(path) as f:
        lines = [l.rstrip("\n") for l in f]
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        open(path, "w").close(); return
    last = lines[-1].strip()
    ok = len(last) >= min_len
    if ok:
        try:
            v = mp.mpf(last)
            ok = 10 < v < 100000
        except Exception:
            ok = False
    if not ok:
        lines.pop()
        with open(path, "w") as f:
            for l in lines:
                f.write(l + "\n")
        log(f"resume validation: dropped malformed tail line in {os.path.basename(path)}")

def main():
    mp.mp.dps = 2700
    validate_tail(ZPATH)
    validate_tail(SPATH)
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
