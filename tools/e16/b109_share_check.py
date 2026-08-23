# b109 -- THE APPORTIONMENT DERIVATION ACT -- the recorded pattern, examined
# against this act's own target (the share statement). Registration:
# data/b109_registration_2026-08-22.txt (the target and both disclosures fixed
# there before this ran).
#
# This does NOT re-run b38 and does NOT re-interpret its verdicts. It examines
# the recorded f sequence against sigma_even, because that comparison IS this
# act's target quantity.

SIGMA_EVEN = 0.6165          # the b35 even t-mass share, as recorded [BENCH]
cells = [2, 3, 4, 8, 9, 12]
f = [0.6923, 0.6638, 0.6533, 0.6260, 0.6204, 0.6092]   # b38's recorded f_cell [BENCH]

print("a^2 |  f_cell   f - sigma_even")
dev = []
for a2, fv in zip(cells, f):
    d = fv - SIGMA_EVEN
    dev.append(d)
    print(f"{a2:>3} | {fv:.4f}   {d:+.4f}")

mono = all(dev[i] > dev[i + 1] for i in range(len(dev) - 1))
signs = {d > 0 for d in dev}
print()
print("deviation strictly decreasing across the recorded cells:", mono)
print("all deviations of one sign:", len(signs) == 1)
print("first cell above sigma_even:", dev[0] > 0, "| last cell above sigma_even:", dev[-1] > 0)

# where the sequence crosses, by linear interpolation between the bracketing cells
cross = None
for i in range(len(dev) - 1):
    if dev[i] > 0 >= dev[i + 1]:
        x0, x1 = cells[i], cells[i + 1]
        y0, y1 = dev[i], dev[i + 1]
        cross = x0 + (x1 - x0) * y0 / (y0 - y1)
        break
print(f"crossing bracketed between a^2 = {cells[3]}..{cells[-1]};"
      f" linear-interpolated crossing at a^2 ~ {cross:.1f}"
      "  [instrument grade; an interpolation, not a recorded value]")

print()
print("READING (this act's target only; b38's own verdicts are fenced and untouched):")
print("  the recorded f sequence does NOT approach sigma_even from above and settle;")
print("  it declines monotonically THROUGH sigma_even and ends below it. A derivation")
print("  of 'f -> sigma_even' must therefore account for the crossing rather than")
print("  cite the decline as though it were convergence.")
