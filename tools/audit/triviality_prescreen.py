# RIDING LIGHT — the triviality pre-screen test (Tier N).
#
# Registered before running: "the trivially-closed terminals carry more unclosed clauses --
# if it holds, the salt-check gains a cheap pre-screen; if it fails, it files as failed and
# no screen is adopted."
#
# The proposed screen: flag a terminal whose proof is closed ONLY by closer tactics
# (ring / norm_num / field_simp / decide / omega / linarith / nlinarith / rfl / simp),
# optionally after unfolding -- i.e. a definitional-unfolding closure.
#
# Two things are measured, because a screen has two failure modes:
#   (1) CORRELATION at row level: triviality share vs the row's measured clause count.
#   (2) PRECISION at terminal level: of the terminals the screen FLAGS, how many are actually
#       definitional restatements?  A screen that flags real theorems is not cheap, it is noisy.
import re
import pathlib

SRC = pathlib.Path(r"D:\SIDE-lv-conservation\SIDELvConservation")

CLOSERS = {"ring", "ring_nf", "norm_num", "field_simp", "decide", "omega", "linarith",
           "nlinarith", "rfl", "simp", "compute_degree!", "trivial", "positivity"}
SETUP = {"unfold", "rw", "intro", "constructor", "refine", "exact", "apply", "have",
         "obtain", "rcases", "cases", "induction", "match", "set", "calc", "use",
         "simp_only", "push_neg", "subst", "specialize", "by_cases", "interval_cases",
         "gcongr", "conv", "change", "show", "let", "next", "all_goals", "first"}

ROWS = {
    "D-2a (lead law)": (["FieldLayer.lean", "LeadLaw.lean", "SaltCheck_LeadLaw.lean"], 1),
    "D-2b (genus <= 5)": (["Genus5.lean", "Genus5Confinement.lean"], 2),
    "D-2c (two sides)": (["TwoSidesIdentity.lean"], 3),
}

THM = re.compile(r"^(?:private\s+)?theorem\s+([A-Za-z_][A-Za-z0-9_']*)")


def strip_comments(text):
    """Remove /- ... -/ blocks (including /-- docstrings) and -- line comments."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            i += 2
        elif text.startswith("-/", i) and depth:
            depth -= 1
            i += 2
        elif depth:
            out.append("\n" if text[i] == "\n" else " ")
            i += 1
        elif text.startswith("--", i):
            j = text.find("\n", i)
            i = len(text) if j < 0 else j
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def proofs(path):
    """{name: proof-text} for each theorem, body = everything until the next top-level decl."""
    text = strip_comments(path.read_text(encoding="utf-8"))
    lines = text.splitlines()
    out, cur, body = {}, None, []
    for line in lines:
        m = THM.match(line)
        if m:
            if cur:
                out[cur] = "\n".join(body)
            cur, body = m.group(1), [line]
            continue
        if cur is not None:
            if line and not line[0].isspace():
                out[cur] = "\n".join(body)
                cur, body = None, []
            else:
                body.append(line)
    if cur:
        out[cur] = "\n".join(body)
    return out


def tactics(proof):
    """Every tactic head in the proof body, splitting on newline, ';' and '<;>'."""
    if ":= by" in proof:
        body = proof.split(":= by", 1)[1]
    elif "by\n" in proof:
        body = proof.split("by\n", 1)[1]
    elif ":=" in proof:
        return []                       # term-mode proof: no tactics at all
    else:
        return []
    body = body.replace("<;>", ";")
    heads = []
    for chunk in re.split(r"[;\n]", body):
        s = chunk.strip().lstrip("·|-• ").strip()
        if not s or s.startswith("(") or s.startswith("["):
            continue
        h = s.split()[0].rstrip(",;[]()")
        if h == "simp" and "only" in s.split("\n")[0][:20]:
            h = "simp_only"
        heads.append(h)
    return heads


def classify(proof):
    tac = tactics(proof)
    if not tac:
        return "TRIVIAL", tac           # term-mode one-liner counts as trivial
    if any(t in SETUP for t in tac):
        # a proof that had to build structure is not a definitional-unfolding closure,
        # EXCEPT when the only structure is `unfold`
        if any(t in SETUP and t != "unfold" for t in tac):
            return "SUBSTANTIVE", tac
    return ("TRIVIAL", tac) if all(t in CLOSERS or t == "unfold" for t in tac) \
        else ("SUBSTANTIVE", tac)


print("=" * 78)
print("(1)  ROW-LEVEL CORRELATION: triviality share vs measured clause count")
print("=" * 78)
print(f"{'row':>20} {'terminals':>11} {'trivial':>9} {'share':>8} {'clauses':>9}")
pts, detail = [], {}
for row, (files, clauses) in ROWS.items():
    names = {}
    for f in files:
        names.update({f"{f[:-5]}.{k}": v for k, v in proofs(SRC / f).items()})
    kinds = {n: classify(b) for n, b in names.items()}
    detail[row] = kinds
    triv = sum(1 for v, _ in kinds.values() if v == "TRIVIAL")
    share = triv / len(kinds)
    pts.append((share, clauses))
    print(f"{row:>20} {len(kinds):>11} {triv:>9} {share:>8.2f} {clauses:>9}")

xs, ys = [p[0] for p in pts], [p[1] for p in pts]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
den = (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
r = sum((x - mx) * (y - my) for x, y in pts) / den if den else float("nan")
print(f"\n  Pearson r over {len(pts)} rows = {r:+.4f}")
print("  n = 3.  This number cannot support a claim in either direction; it is printed so")
print("  that it is not later reconstructed as if it could.")

print()
print("=" * 78)
print("(2)  TERMINAL-LEVEL PRECISION: what does the screen actually flag?")
print("=" * 78)
KNOWN_DEFINITIONAL = {"TwoSidesIdentity.ladder_three"}
flagged = [n for kinds in detail.values() for n, (k, _) in kinds.items() if k == "TRIVIAL"]
total = sum(len(k) for k in detail.values())
print(f"  terminals examined: {total}")
print(f"  terminals flagged TRIVIAL by the screen: {len(flagged)}")
for row, kinds in detail.items():
    for n, (k, tac) in sorted(kinds.items()):
        if k == "TRIVIAL":
            mark = "   <-- IS a definitional restatement" if n in KNOWN_DEFINITIONAL else ""
            print(f"    {n:<46} {tac}{mark}")
tp = len([n for n in flagged if n in KNOWN_DEFINITIONAL])
print()
print(f"  of those, actually definitional restatements: {tp}")
print(f"  PRECISION = {tp}/{len(flagged)} = {tp/len(flagged):.3f}"
      if flagged else "  PRECISION undefined (nothing flagged)")
print(f"  RECALL    = {tp}/{len(KNOWN_DEFINITIONAL)} = {tp/len(KNOWN_DEFINITIONAL):.3f}")
print()
print("  THE DECISIVE PAIR:")
for nm in ("heine_three", "ladder_three"):
    for row, kinds in detail.items():
        for n, (k, tac) in kinds.items():
            if n.endswith("." + nm):
                print(f"    {n:<40} {k:<12} {tac}")
print("  One is the Heine/Vandermonde identity in six free variables; the other restates a")
print("  definition.  Whatever the screen does with this pair is what the screen is worth.")
