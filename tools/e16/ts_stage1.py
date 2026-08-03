# W-TWOSIDES stage 1: zeta moments at dps 400 (kmax 33), cached to scratchpad.
import importlib.util, sys, pathlib, os
import mpmath as mp

spec = importlib.util.spec_from_file_location(
    "hb", str(pathlib.Path(__file__).with_name("hankel_bridge.py")))
hb = importlib.util.module_from_spec(spec); sys.modules["hb"] = hb; spec.loader.exec_module(hb)

OUT = os.path.join(os.environ.get("TEMP", "."), "ts_zeta_moments.txt")

def main():
    mp.mp.dps = 400
    s = hb.power_sums(mp.mpf(0), 33)
    with open(OUT, "w") as f:
        for k in range(1, 34):
            f.write(mp.nstr(s[k], 400) + "\n")
    print("zeta moments cached:", OUT)

if __name__ == "__main__":
    main()
