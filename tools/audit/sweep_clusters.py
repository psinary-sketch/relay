# The provenance sweep, EXTENDED: the unverified formulas sorted by cluster, each cluster
# carrying its verification route.  No new mathematics, no reverification run here.
#
# Clusters are assigned by file + line range + keyword, so the counts are derived rather than
# eyeballed.  A NOT-A-FORMULA class is included and reported first, because a work-order list
# that quietly carries its own false positives is the defect it exists to catch.
import re
import subprocess
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
out = subprocess.run([sys.executable, str(HERE / "formula_provenance_sweep.py")],
                     capture_output=True, text=True, encoding="utf-8").stdout

rows, cur = [], None
for ln in out.splitlines():
    m = re.match(r"--- (\S+\.md)\s+\((\d+)\)", ln)
    if m:
        cur = m.group(1)
        continue
    m = re.match(r"\s+L(\d+)\s+(.*)", ln)
    if m and cur:
        rows.append((cur, int(m.group(1)), m.group(2).strip()))

NOISE = ("here =", "closure =", "false=false", "local = remote", "stall =", "wall =",
         "direction =", "complete =", "zeroActing =", "spectrum =", "criterion =",
         "S=22", "completion ~1", "M=vv", "H=xp", "even = twist-even", "CartanBBridge",
         "δ ≈ 3×10⁻⁶ at γ = 16", "reconciles them")

CLUSTERS = [
    ("NOT-A-FORMULA (parser false positives; struck from the list)",
     lambda f, l, t: any(k in t for k in NOISE), "—"),
    ("Li/Weil analysis block",
     lambda f, l, t: (f == "VERIFICATION_LOOM.md" and 2140 <= l <= 2190)
                     or (f == "OPEN_TRAILS.md" and 2150 <= l <= 2160),
     "derivation-at-source (Bombieri–Lagarias; Lagarias 2007) + numerical check "
     "(the Cayley/moment instruments built 2026-08-05 evaluate S_n and E_quad directly)"),
    ("Cosmology / formation-constants block",
     lambda f, l, t: ("Omega" in t or "n1=3" in t or "n3=2" in t or "zeta(-1)" in t
                      or "mu-odd" in t or "formation (2, 3, 2, 0)" in t),
     "NUMERICAL CHECK (the constants have measured counterparts) + dimensional check"),
    ("Spectral-realization / Hilbert–Pólya block",
     lambda f, l, t: f == "VERIFICATION_LOOM.md" and 2800 <= l <= 3500,
     "derivation-at-source (each is an identification at cite, not a computed quantity)"),
    ("Number-field / Dedekind arithmetic",
     lambda f, l, t: ("Dedekind" in t or "d(K)" in t or "ζ_v(s" in t or "Λ(s, χ)" in t
                      or "genus-1 Hadamard" in t),
     "NUMERICAL CHECK on small fields + derivation-at-source"),
    ("Shape discriminant / era measurements",
     lambda f, l, t: f == "INDEX_ARITY_AT_THE_CRITICAL_LINE.md",
     "CITE-ADJACENT REPAIR — these are provenanced in relay reports; the sweep flags them "
     "only because the proximity proxy cannot see three paragraphs away"),
]

assigned, misc = {name: [] for name, _, _ in CLUSTERS}, []
for f, l, t in rows:
    for name, pred, _ in CLUSTERS:
        if pred(f, l, t):
            assigned[name].append((f, l, t))
            break
    else:
        misc.append((f, l, t))

print("=" * 78)
print("THE PROVENANCE SWEEP, SORTED BY CLUSTER")
print("=" * 78)
print(f"  flagged formulas carried forward from the sweep: {len(rows)}")
print()
routes = {name: route for name, _, route in CLUSTERS}
for name, _, route in CLUSTERS:
    items = assigned[name]
    print(f"--- {name}  ({len(items)}) ---")
    if route != "—":
        print(f"    VERIFICATION ROUTE: {route}")
    for f, l, t in items:
        print(f"      {f.split('.')[0][:14]:<14} L{l:<6} {t[:66]}")
    print()
print(f"--- UNCLUSTERED  ({len(misc)}) ---")
print("    VERIFICATION ROUTE: read individually; no common route applies")
for f, l, t in misc:
    print(f"      {f.split('.')[0][:14]:<14} L{l:<6} {t[:66]}")

real = len(rows) - len(assigned[CLUSTERS[0][0]])
print()
print("=" * 78)
print(f"  SUMMARY: {len(rows)} flagged; {len(assigned[CLUSTERS[0][0]])} struck as not formulas;")
print(f"           {real} genuine work-orders remain, in {len(CLUSTERS)-1} named clusters "
      f"plus {len(misc)} unclustered.")
print("  No defect is claimed against any of them and no reverification is run here.")
