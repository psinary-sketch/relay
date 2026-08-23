# b107 -- THE APPORTIONMENT ACT -- an INDEPENDENT verification of b38's recorded
# run, from the recorded numbers alone. This does NOT re-run b38's instrument and
# does not recompute its inputs; it checks the arithmetic the void-gate asserts,
# against the values as printed at data/b38_2026-08-18.txt, so the gate's verdict
# rests on something other than the instrument's own say-so.
# Registration: data/b107_registration_2026-08-22.txt.

TOL_GATE = 1e-5      # the printed values carry 5-6 decimals; the gate's own tol is 1e-10
                     # on the full-precision quantities, which this check cannot see.
rows = [
    # a^2,      A,          W_plus,    W_minus,   f_cell_printed
    (2,  -1.990528, -1.37813, -0.61239, 0.6923),
    (3,  -1.908900, -1.26715, -0.64175, 0.6638),
    (4,  -1.786498, -1.16716, -0.61934, 0.6533),
    (8,  -1.525474, -0.95494, -0.57053, 0.6260),
    (9,  -1.488337, -0.92343, -0.56490, 0.6204),
    (12, -1.405398, -0.85622, -0.54917, 0.6092),
]

fails = []
print("cell |  W+ + W-        A          |diff|    | f=W+/A   printed   |diff|")
for a2, A, wp, wm, f_print in rows:
    s = wp + wm
    d = abs(s - A)
    f = wp / A
    df = abs(f - f_print)
    print(f"{a2:>4} | {s:>10.6f} {A:>10.6f} {d:>9.2e} | {f:>7.5f} {f_print:>8.4f} {df:>9.2e}")
    if d > TOL_GATE:
        fails.append(("sum-gate", a2, d))
    if df > 1e-4:
        fails.append(("f_cell", a2, df))

# the reported trend: f declining toward the t-share 0.6165
f_vals = [wp / A for _, A, wp, _, _ in rows]
monotone = all(f_vals[i] > f_vals[i + 1] for i in range(len(f_vals) - 1))
print()
print("f declines monotonically across the recorded cells:", monotone)
print(f"f range: {f_vals[0]:.4f} -> {f_vals[-1]:.4f}; the report's t-share reference: 0.6165")
print("every f_cell is strictly below the (W-even) threshold 0.9:",
      all(f < 0.9 for f in f_vals))

if fails:
    print("\nFAIL:", len(fails))
    for x in fails:
        print(x)
else:
    print("\nVOID-GATE VERIFIED AT CONTENT from the recorded values: W+ + W- = A at every")
    print("cell within the printed precision; f_cell reproduces; the (W-even) branch is")
    print("excluded by the data and (W-split) is the branch the numbers support.")
