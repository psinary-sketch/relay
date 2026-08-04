# W-CONVLAW: the convergence-law discrimination on the five uniform-object points.
# Families (a)-(e) per the pre-commit; criterion: no monotone five-point residual +
# best leave-one-out prediction of c(200) from the first four wins.
import mpmath as mp
mp.mp.dps = 40

K = [16, 32, 64, 128, 200]
C = [mp.mpf(x) for x in ("0.578133", "0.729832", "0.825489", "0.886588", "0.932074")]

def lsq(xs, ys):
    n = len(xs)
    mx = sum(xs) / n; my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    b = num / den
    a = my - b * mx
    return a, b   # y = a + b x

def residual_pattern(resids):
    signs = [(r > 0) - (r < 0) for r in resids]
    monotone = all(signs[i] <= signs[i + 1] for i in range(len(signs) - 1)) or \
               all(signs[i] >= signs[i + 1] for i in range(len(signs) - 1))
    return signs, monotone

def report(name, cinf, pred200, resids):
    err = pred200 - C[4]
    signs, mono = residual_pattern(resids)
    print(f"{name:>22}: c_inf = {mp.nstr(cinf, 5)} | LOO pred c(200) = {mp.nstr(pred200, 6)} "
          f"| LOO err = {mp.nstr(err, 3)} | 5pt residual signs {signs} | monotone: {mono}")
    return abs(err), mono

results = {}

# (a) geometric-in-index (spacing-blind): fit ratio on first-four increments; predict 5th
inc = [C[i+1] - C[i] for i in range(3)]
rho = (inc[1] / inc[0] + inc[2] / inc[1]) / 2
pred = C[3] + inc[2] * rho
cinf_a = C[3] + inc[2] * rho / (1 - rho)
# 5-pt residuals: fit rho on all four increments (lsq of log inc vs index)
inc5 = [C[i+1] - C[i] for i in range(4)]
la, lb = lsq(list(range(4)), [mp.log(x) for x in inc5])
fit_inc = [mp.e ** (la + lb * i) for i in range(4)]
res5 = [inc5[i] - fit_inc[i] for i in range(4)]
results["(a) geometric-index"] = report("(a) geometric-index", cinf_a, pred, res5)

# (b) power A/K^p: grid p, linear in (cinf, A) via lsq on x = K^-p; fit on first 4, predict
best = None
for pp in [mp.mpf(i) / 100 for i in range(5, 301, 2)]:
    xs = [mp.mpf(k) ** (-pp) for k in K[:4]]
    a, b = lsq(xs, C[:4])       # c = cinf + b * K^-p  (b = -A)
    sse = sum((C[i] - (a + b * xs[i])) ** 2 for i in range(4))
    if best is None or sse < best[0]:
        best = (sse, pp, a, b)
_, pp, a, b = best
pred_b = a + b * mp.mpf(200) ** (-pp)
xs5 = [mp.mpf(k) ** (-pp) for k in K]
res_b = [C[i] - (a + b * xs5[i]) for i in range(5)]
print(f"    [power family: fitted p = {mp.nstr(pp, 3)}]")
results["(b) power A/K^p"] = report("(b) power A/K^p", a, pred_b, res_b)

# (c) log-corrected A logK/K
xs = [mp.log(k) / k for k in K[:4]]
a, b = lsq(xs, C[:4])
pred_c = a + b * mp.log(200) / 200
xs5 = [mp.log(k) / k for k in K]
res_c = [C[i] - (a + b * xs5[i]) for i in range(5)]
results["(c) A logK/K"] = report("(c) A logK/K", a, pred_c, res_c)

# (d) A/log K
xs = [1 / mp.log(k) for k in K[:4]]
a, b = lsq(xs, C[:4])
pred_d = a + b / mp.log(200)
xs5 = [1 / mp.log(k) for k in K]
res_d = [C[i] - (a + b * xs5[i]) for i in range(5)]
results["(d) A/logK"] = report("(d) A/logK", a, pred_d, res_d)

# (e) Aitken limits (limit estimates only; LOO scored as local-geometric = (a))
def aitken(c1, c2, c3):
    d1, d2 = c2 - c1, c3 - c2
    return c3 + d2 * d2 / (d1 - d2) if d1 != d2 else mp.mpf('nan')
print(f"    [(e) Aitken limits: pts1-3 {mp.nstr(aitken(C[0],C[1],C[2]),5)}, "
      f"pts2-4 {mp.nstr(aitken(C[1],C[2],C[3]),5)}, pts3-5 {mp.nstr(aitken(C[2],C[3],C[4]),5)}]")

print("\n=== THE CRITERION APPLIED ===")
eligible = {k: v for k, v in results.items() if not v[1]}
print(f"families with non-monotone residuals: {list(eligible)}")
if eligible:
    winner = min(eligible, key=lambda k: eligible[k][0])
    print(f"WINNER (best LOO among eligible): {winner} | LOO |err| = {mp.nstr(eligible[winner][0], 3)}")
