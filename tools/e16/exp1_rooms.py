"""EXPERIMENT ONE — the two-prime room. REGISTERED PREDICTIONS, computed exactly.

The measurement half cannot run: the sitting-12 instrument was never banked (see the
report). What CAN be stated exactly, and is stated here BEFORE any instrument exists,
is the arithmetic content of the registered predictions.

A "room" for a lag l in a window of log-length log L is the portion of the window in
which a lag-l term has room to act: width (log L - l), fraction 1 - l/log L. That is
the sitting-12 law with the single lag l = log 2.

The ferry's E1-union says the rooms are "suitably combined - the law generalizes
additively". That phrase admits three natural readings, and they are DIFFERENT
falsifiable predictions, so all three are registered rather than one chosen silently.
"""
import math

LS = [3.2, 3.6, 4.0, 4.4, 5.0, 6.0, 9.5]
log2, log3 = math.log(2), math.log(3)


def lags_ferry(L):
    """The ferry's literal rule: log2 always; 2*log2 once L > 4; log3 once L > 9."""
    out = [("log 2", log2)]
    if L > 4:
        out.append(("2 log 2", 2 * log2))
    if L > 9:
        out.append(("log 3", log3))
    return out


def lags_primepower(L):
    """The arithmetic rule: one room per prime power p^k < L, lag = log(p^k)."""
    out = []
    for p in (2, 3, 5, 7, 11, 13):
        k = 1
        while p ** k < L:
            out.append(("log %d" % p ** k, math.log(p ** k)))
            k += 1
    return sorted(out, key=lambda t: t[1])


def rooms(L, lags):
    return [max(0.0, 1.0 - l / math.log(L)) for _, l in lags]


def U1_nested(r):      # rooms nested -> union is the largest
    return max(r) if r else 0.0


def U2_independent(r):  # 1 - prod(1 - r_i)
    p = 1.0
    for x in r:
        p *= (1 - x)
    return 1 - p


def U3_additive(r):     # min(1, sum) -- the literal "additively"
    return min(1.0, sum(r))


for name, lagfn in (("FERRY-LITERAL LAG RULE", lags_ferry),
                    ("PRIME-POWER LAG RULE", lags_primepower)):
    print("=" * 78)
    print(name)
    print("=" * 78)
    print("   L    lags                          single    U1-nested  U2-indep  U3-add")
    for L in LS:
        lg = lagfn(L)
        r = rooms(L, lg)
        names = ",".join(n for n, _ in lg)
        print("  %4.1f  %-28s %8.5f  %8.5f  %8.5f  %8.5f"
              % (L, names, 1 - log2 / math.log(L), U1_nested(r), U2_independent(r), U3_additive(r)))
    print()

print("=" * 78)
print("WHERE THE THREE READINGS SEPARATE (ferry-literal rule)")
print("=" * 78)
for L in LS:
    r = rooms(L, lags_ferry(L))
    a, b, c = U1_nested(r), U2_independent(r), U3_additive(r)
    print("  L=%4.1f   spread U3-U1 = %.5f   %s"
          % (L, c - a, "DEGENERATE (one room)" if len(r) == 1 else "SEPARATED"))
