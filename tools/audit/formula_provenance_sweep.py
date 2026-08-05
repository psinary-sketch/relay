# THE FORMULA-PROVENANCE SWEEP.
#
# Same class as the description rule: text that was true when written and never re-derived.
# For every quantitative FORMULA stated in the living ledgers and the keystone, ask whether a
# verification provenance is recorded anywhere near it -- was it numerically or dimensionally
# checked, and where is that written down?
#
# Output: the formulas carrying NO verification provenance, as WORK-ORDERS, not defect claims.
# A formula with no recorded check is not thereby wrong; it is unaudited, which is a different
# and fixable thing.
import re
import pathlib

ROOT = pathlib.Path(r"D:\MY-DOwnloads\PLACE-papers")
FILES = [
    ROOT / "OPEN_TRAILS.md",
    ROOT / "FINDINGS.md",
    ROOT / "VERIFICATION_LOOM.md",
    ROOT / "phase1.5" / "proofs" / "INDEX_ARITY_AT_THE_CRITICAL_LINE.md",
    ROOT / "phase1.5" / "method" / "INSTRUMENTS.md",
]

# A "formula" = a relation between symbols, not a bare number.  Require a relation symbol
# with algebraic material on at least one side.
# A quantitative FORMULA: a named quantity related to an expression that carries genuine
# functional content -- a transcendental function, a constant, a power, or a ratio of
# variables.  Bare integer identities and code fragments are not formulas and are excluded.
MATHY = r"(?:log|exp|sqrt|√|Γ|π|γ(?![a-z])|ζ|ξ|λ|δ|ε|\^|⁻|½|·\s*[a-zA-Z]|/\s*[a-zA-Zπγ])"
REL = re.compile(
    r"(?:[A-Za-zλγδεπζξΛΠΣΔ_][A-Za-z0-9_]{0,12}\s*\([^)]{1,24}\)"      # f(x)
    r"|[A-Za-zλγδεπζξΛΠΣΔ][A-Za-z0-9_]{0,10}(?:_\{?[A-Za-z0-9]{1,6}\}?)?)"  # x_k
    r"\s*(?:=|≈|~|∼|≍|≥|≤)\s*"
    r"(?=[^,.;)\n]{0,80}?" + MATHY + r")"
    r"[^,.;)\n]{2,70}")
CODEY = re.compile(r"(=>|==|:=|\bLean\b|\bBool\b|`|\brfl\b|\bdecide\b|\bcases\b|Mathlib)")

# Words that indicate a verification provenance was recorded near the formula.
PROV = ("verified", "verify", "checked", "check", "computed", "measured", "doubly-sourced",
        "double-sourced", "cross-check", "cross-checked", "instrument", "relay `", "tools/",
        "compiled", "#print axioms", "probe", "recomputed", "re-derived", "salt-check",
        "matches", "agrees", "against the exact", "confirmed")

SKIP = ("http", "```", "| flat file", "md5")


def context(lines, i, half=2):
    lo, hi = max(0, i - half), min(len(lines), i + half + 1)
    return " ".join(lines[lo:hi])


rows = []
for f in FILES:
    if not f.exists():
        continue
    lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
    for i, ln in enumerate(lines):
        if any(s in ln for s in SKIP):
            continue
        for m in REL.finditer(ln):
            frag = m.group(0).strip()
            if len(frag) < 10 or len(frag) > 90:
                continue
            if CODEY.search(frag):
                continue
            ctx = context(lines, i).lower()
            has = any(p.lower() in ctx for p in PROV)
            rows.append((f.name, i + 1, frag, has))

seen, uniq = set(), []
for r in rows:
    key = (r[0], r[2])
    if key not in seen:
        seen.add(key)
        uniq.append(r)

print("=" * 78)
print("THE FORMULA-PROVENANCE SWEEP")
print("=" * 78)
print(f"  files swept: {len([f for f in FILES if f.exists()])}")
print(f"  distinct formula statements found: {len(uniq)}")
withp = [r for r in uniq if r[3]]
without = [r for r in uniq if not r[3]]
print(f"  carrying a verification provenance within +/-2 lines: {len(withp)} "
      f"({len(withp)/max(len(uniq),1):.0%})")
print(f"  carrying NONE: {len(without)} ({len(without)/max(len(uniq),1):.0%})")
print()
print("  NOTE ON THE INSTRUMENT'S OWN LIMITS, stated before its output is read:")
print("   - proximity is a proxy for provenance; a formula checked in a relay report and")
print("     cited three paragraphs away reads here as unprovenanced (FALSE POSITIVE);")
print("   - a nearby word like 'computed' does not prove THIS formula was the thing computed")
print("     (FALSE NEGATIVE).  The output below is a WORK-ORDER LIST to be read by hand,")
print("     not a verdict, and it is filed as such.")
print()
print("=" * 78)
print("WORK-ORDER LIST: formulas with no verification provenance in context")
print("=" * 78)
by_file = {}
for r in without:
    by_file.setdefault(r[0], []).append(r)
for fn, rs in by_file.items():
    print(f"\n--- {fn}  ({len(rs)}) ---")
    for _, ln, frag, _ in rs:
        print(f"  L{ln:<6} {frag}")
