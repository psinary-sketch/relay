# THE RESOLVABILITY TEST, replacing the occurrence proxy.
#
# A term is HELD when its STATEMENT appears in the mirror -- not when its NAME appears often.
# Name-frequency is not evidence and runs the wrong way: repetition is what an unresolvable name
# does, since a resolved one is stated once and pointed at thereafter.
#
# For each term: search the mirror for CONTENT MARKERS -- the words or symbols that would have to
# be present if the term were stated, not merely named.  Report RESOLVABLE (with location) or
# UNRESOLVABLE.
import pathlib

REPO = pathlib.Path(r"D:\MY-DOwnloads\PLACE-papers")
ROSTER = [
    "OPEN_TRAILS.md", "FINDINGS.md", "VERIFICATION_LOOM.md", "SPIRAL_MAP.md", "REGISTRY.md",
    "ERRATA.md", "THE_RESIDUE_OF_RH.md", "A_Place_to_Stand.md",
    "PATHS_TO_THE_CRITICAL_LINE.md", "THE_UNCONDITIONAL_SURROUND.md",
    "SIMPLICITY_OF_RIEMANN_ZEROS.md", "EXCLUSION_ENGINE.md",
    "FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md", "INVARIANCE_BARRIERS.md", "GRH_CASCADE.md",
    "BALANCE_AND_POSITIVITY.md", "ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md",
    "FORMATION_DISTANCE_AND_SILENCE_AS_PROTECTION.md", "SILENCE_STAGES_DEALIGNMENT.md",
    "INDEX_ARITY_AT_THE_CRITICAL_LINE.md", "INSTRUMENTS.md",
]
files = {}
for n in ROSTER:
    h = list(REPO.rglob(n))
    if h:
        files[n] = h[0].read_text(encoding="utf-8", errors="replace")

# term -> (name markers, CONTENT markers that must appear if the term is STATED)
TERMS = {
    "two-witness barrier": (
        ["two-witness barrier"],
        ["two witnesses", "two independent witnesses", "witness pair", "both witnesses"]),
    "gamma - 1 - log m": (
        ["γ − 1 − log m", "γ - 1 - log m", "γ−1−log m"],
        ["superposition", "independent thinning", "m independent", "log m"]),
    "m_h = vv†": (
        ["m_h = vv†", "M_h = vv†", "vv†"],
        ["rank-one", "rank one", "outer product", "v v†", "vvᵀ"]),
    "de Branges spaces": (
        ["de Branges space"],
        ["Hermite–Biehler", "Hermite-Biehler", "structure function",
         "E(z)", "reproducing kernel"]),
    "non-discriminating by design": (
        ["non-discriminating by design"],
        ["same value for every", "cannot distinguish", "takes the same value",
         "zero placement power", "insensitive to"]),
}

print("=" * 78)
print("THE RESOLVABILITY SCREEN — the five remaining shortlist terms")
print("=" * 78)
print("  A term is HELD when its STATEMENT appears in the mirror.  For each term below the")
print("  NAME markers locate the mention; the CONTENT markers are what would have to appear")
print("  if the term were stated rather than named.")
print()
for term, (names, content) in TERMS.items():
    nloc, cloc = [], []
    for fn, tx in files.items():
        low = tx.lower()
        for m in names:
            if m.lower() in low:
                nloc.append(fn)
                break
        for m in content:
            if m.lower() in low:
                cloc.append(f"{fn}[{m}]")
                break
    verdict = "RESOLVABLE" if cloc else "UNRESOLVABLE"
    print(f"--- {term}")
    print(f"      named in : {', '.join(sorted(set(nloc))) if nloc else '(nowhere)'}")
    print(f"      stated in: {', '.join(sorted(set(cloc))) if cloc else '(nowhere)'}")
    print(f"      VERDICT  : {verdict}")
    print()

print("=" * 78)
print("THE WORKED EXAMPLE THAT RETIRED THE OLD PROXY")
print("=" * 78)
for name, content in (("Mallows", "4⌊n/24⌋"), ("Gleason", "invariant space"),
                      ("Hankel-ratio", "D_{j+1}")):
    nc = sum(tx.count(name) for tx in files.values())
    cc = sum(tx.count(content) for tx in files.values())
    print(f"  {name:<14} named {nc:>3}x   content marker '{content}' present {cc}x")
print()
print("  Counted before this pass's repairs, the content column was 0 for all three while the")
print("  name column read 8 / 8 / 6.  Frequency of a NAME is not evidence that a term is held.")

print()
print("=" * 78)
print("HAND SPOT-CHECK OF THIS SCREEN'S OWN VERDICTS (recorded, not inferred)")
print("=" * 78)
print("  gamma - 1 - log m : CONFIRMED RESOLVABLE.  OPEN_TRAILS states the derived family")
print("      ('for R2 = 1 - K(r), pi_0 = -log 2pi - 2 int K(r) log r dr -- GUE gamma-1,")
print("       Poisson -log 2pi, m-fold superposition gamma - 1 - log m') and the loom carries")
print("      its DERIVED-BUT-UNVALIDATED status.  The screen was right.")
print()
print("  non-discriminating by design : SCREEN FALSE POSITIVE.  At its point of use")
print("      (OPEN_TRAILS, the LY-REP-A layer-1 verdict) the phrase is a VERDICT LABEL and its")
print("      criterion is NOT stated there; the content markers that passed it matched generic")
print("      phrases in unrelated files.  Verdict corrected by hand to UNRESOLVABLE.")
print()
print("  THE LESSON, and it is the same failure the old proxy had, running the other way:")
print("  the old test counted a NAME anywhere; this one counts CONTENT WORDS anywhere.  Both")
print("  over-credit.  THE MISSING CONDITION IS LOCALITY: the statement must be findable FROM")
print("  the mention -- co-located, or explicitly pointed at.  A screen without it measures")
print("  whether the corpus contains the words, not whether a reader can get from the name to")
print("  the thing.  Filed with the test rather than discovered later.")
