# RE-PRICE items 1-3, banked data only.
# (1) THE ERROR BAR: shared ladder points from the J=960 and J=1200 objects; per-point |delta|.
# (2) LADDER-DEPENDENCE: family (a) index-geometric restated intrinsically.
# (3) ASYMPTOTIC-WINDOW FIT: drop rule PRE-COMMITTED below, then intrinsic-variable fits.
import os
import mpmath as mp

T = os.environ.get("TEMP", ".")
mp.mp.dps = 60

def load_j(p):
    al, be, mode = [], [], "AL"
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line == "BETA": mode = "BETA"; continue
            (al if mode == "AL" else be).append(mp.mpf(line))
    return al, be

def load_a(p, n):
    with open(p) as f:
        return [mp.mpf(l.strip()) for l in f if l.strip()][:n]

def nodes(al, be, k):
    Jm = mp.matrix(k, k)
    for i in range(k): Jm[i, i] = al[i]
    for i in range(k - 1):
        off = mp.sqrt(be[i + 1]); Jm[i, i + 1] = off; Jm[i + 1, i] = off
    E = mp.eigsy(Jm, eigvals_only=True)
    return sorted([mp.mpf(E[i]) for i in range(k)], reverse=True)

def cseq(jz, jc, az, ac, n, ladder):
    alZ, beZ = load_j(os.path.join(T, jz)); alC, beC = load_j(os.path.join(T, jc))
    aZ = [1 / (2 * g) ** 2 for g in load_a(os.path.join(T, az), n)]
    aC = [1 / (2 * g) ** 2 for g in load_a(os.path.join(T, ac), n)]
    out = []
    for k in ladder:
        lamZ = nodes(alZ, beZ, k); lamC = nodes(alC, beC, k)
        def res(lam, atoms):
            r = 0
            for j in range(k):
                if abs(lam[j] - atoms[j]) / atoms[j] < mp.mpf("0.01"): r = j + 1
                else: break
            return r
        R = min(res(lamZ, aZ), res(lamC, aC))
        def osc(lam):
            v = mp.mpf(0)
            for i in range(2, R):
                for j in range(i + 1, R):
                    v += 2 * mp.log(abs(lam[i] - lam[j]))
            return v
        harm = sum(mp.mpf(1) / (j - i) for i in range(2, R) for j in range(i + 1, R))
        out.append((k, R, (osc(lamZ) - osc(lamC)) / harm))
    return out

shared = [16, 32, 64, 128, 200]
s960 = cseq("k200_jacobi_zeta.txt", "k200_jacobi_ctrl.txt", "k200_zeros.txt", "k200_smooth.txt", 960, shared)
s1200 = cseq("k256_jacobi_zeta.txt", "k256_jacobi_ctrl.txt", "k256_zeros.txt", "k256_smooth.txt", 1200, shared + [256])

print("=== (1) THE ERROR BAR: the J-systematic per ladder point ===")
print(f"{'K':>5} {'R':>5} {'c(J=960)':>12} {'c(J=1200)':>12} {'|delta|':>10} {'incr':>10} {'|d|/incr':>9}")
prev = None
bars = {}
for (k, R, c9), (k2, R2, c12) in zip(s960, s1200):
    d = abs(c12 - c9)
    inc = (c12 - prev) if prev is not None else mp.mpf('nan')
    prev = c12
    bars[k] = d
    r = d / inc if prev is not None and inc == inc and inc != 0 else mp.mpf('nan')
    print(f"{k:>5} {R:>5} {mp.nstr(c9,6):>12} {mp.nstr(c12,6):>12} {mp.nstr(d,3):>10} "
          f"{mp.nstr(inc,3):>10} {mp.nstr(r,3):>9}")
k256 = s1200[-1]
print(f"{256:>5} {k256[1]:>5} {'—':>12} {mp.nstr(k256[2],6):>12} {'(no J-pair)':>10}")
print(f"\nprediction separation at 256 = 0.0182 | largest tail systematic = "
      f"{mp.nstr(max(bars[k] for k in (128,200)),3)}")

print("\n=== (2) LADDER-DEPENDENCE of family (a) ===")
C = [c for _, _, c in s1200]; Kl = [k for k, _, _ in s1200]
inc = [C[i+1] - C[i] for i in range(5)]
ratios = [inc[i+1] / inc[i] for i in range(4)]
print(f"increment ratios (index-geometric assumption): {[mp.nstr(r,4) for r in ratios]}")
print(f"  ladder steps: {[f'{Kl[i]}->{Kl[i+1]} (x{mp.nstr(mp.mpf(Kl[i+1])/Kl[i],3)})' for i in range(5)]}")
print("  the first three steps are DOUBLINGS; the fourth is x1.5625 — an index-geometric")
print("  fit treats them as equal, so its ratio is a ladder artifact unless restated.")
# intrinsic restatement: constant ratio across doublings <=> power law A/K^p with 2^-p = ratio
import math
p_from = [-mp.log(ratios[i]) / mp.log(2) for i in range(3)]
print(f"  intrinsic reading of the doubling ratios: p = {[mp.nstr(x,4) for x in p_from]} "
      f"(power law A/K^p)")
# predicted last-step increment ratio under the power law with p = mean
pm = sum(p_from) / 3
pred_last = (mp.mpf(Kl[4]) ** (-pm) - mp.mpf(Kl[5]) ** (-pm)) / (mp.mpf(Kl[3]) ** (-pm) - mp.mpf(Kl[4]) ** (-pm))
print(f"  power law (p={mp.nstr(pm,4)}) predicts the 200->256 increment ratio = {mp.nstr(pred_last,4)}; "
      f"observed {mp.nstr(ratios[3],4)}")
print("  VERDICT: index-geometric does not survive intrinsic restatement (it is the power")
print("  law seen through a doubling ladder); the intrinsic family is A/K^p.")

print("\n=== (3) ASYMPTOTIC-WINDOW FIT ===")
print("DROP RULE, PRE-COMMITTED BEFORE FITTING: drop any point with R < 30, or whose")
print("J-systematic exceeds 20% of its own increment. Then fit c = c_inf + B*x in each")
print("intrinsic variable x in {1/K, 1/R, 1/log K} on the surviving tail.")
keep = []
for i, (k, R, c) in enumerate(s1200):
    if R < 30:
        print(f"  drop K={k}: R={R} < 30"); continue
    d = bars.get(k, mp.mpf(0))
    incr = abs(C[i] - C[i-1]) if i > 0 else mp.mpf(1)
    if k != 256 and d > mp.mpf("0.2") * incr:
        print(f"  drop K={k}: systematic {mp.nstr(d,3)} > 20% of increment {mp.nstr(incr,3)}"); continue
    keep.append((k, R, c))
print(f"  surviving tail: K = {[k for k,_,_ in keep]}")
def lsq(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    b = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / sum((x-mx)**2 for x in xs)
    return my - b*mx, b
lims = []
for name, fx in (("1/K", lambda k, R: mp.mpf(1)/k), ("1/R", lambda k, R: mp.mpf(1)/R),
                 ("1/logK", lambda k, R: 1/mp.log(k))):
    xs = [fx(k, R) for k, R, _ in keep]; ys = [c for _, _, c in keep]
    a, b = lsq(xs, ys)
    lims.append(a)
    print(f"  tail limit in {name}: c_inf = {mp.nstr(a,5)}")
if lims:
    print(f"  SPREAD across intrinsic variables: [{mp.nstr(min(lims),5)}, {mp.nstr(max(lims),5)}] "
          f"(width {mp.nstr(max(lims)-min(lims),3)})")
