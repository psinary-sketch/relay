# W-TWOSIDES stage 2: control moments (smooth-density zeros at dps 200, kmax 33), cached.
import importlib.util, sys, pathlib, os
import mpmath as mp

spec3 = importlib.util.spec_from_file_location(
    "cc", str(pathlib.Path(__file__).with_name("constant_control.py")))
cc = importlib.util.module_from_spec(spec3); sys.modules["cc"] = cc; spec3.loader.exec_module(cc)

OUT = os.path.join(os.environ.get("TEMP", "."), "ts_ctrl_moments.txt")

def main():
    mp.mp.dps = 200
    J = 3000
    gam = [cc.smooth_zero(j) for j in range(1, J + 1)]
    betas = [1 / (2 * g) ** 2 for g in gam]
    gJ = gam[-1]
    with open(OUT, "w") as f:
        for k in range(1, 34):
            base = sum(b ** k for b in betas)
            tail = mp.quad(lambda g: mp.log(g / (2 * mp.pi)) / (2 * mp.pi) * (2 * g) ** (-2 * k),
                           [gJ, 10 * gJ, mp.inf])
            f.write(mp.nstr(base + tail, 200) + "\n")
    print("control moments cached:", OUT)

if __name__ == "__main__":
    main()
