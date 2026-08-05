# THE RELAY-ONLY SWEEP.
#
# A reader of the reviewer mirror sees 21 files.  A term whose only elaboration lives in a relay
# report is, to that reader, an unresolvable anchor -- the failure mode the navigator-coinage
# check names, applied to the corpus as it stands rather than to phrases arriving in a ferry.
#
# OPERATIONALIZATION, stated before the output because it decides what the numbers mean:
#   a bolded phrase is the unit (bolding is how this corpus marks a term as a term);
#   MINTED       = 2+ occurrences inside the mirror set -> the mirror holds it
#   RELAY-ONLY   = exactly 1 mirror occurrence AND 1+ relay occurrences -> the home is outside
#   MIRROR-HAPAX = exactly 1 mirror occurrence and none in relay -> coined in place, used once
#
# LIMITS, also before the output:
#   - occurrence count is a proxy for "held"; a term defined once and well is MINTED in substance
#     and reads as RELAY-ONLY here (false positive);
#   - a term used twice loosely reads as MINTED (false negative);
#   - bolding is a proxy for term-hood.
# The output is a work-order list, not a verdict.  Nothing is repaired here.
import re
import pathlib
import collections

REPO = pathlib.Path(r"D:\MY-DOwnloads\PLACE-papers")
RELAY = pathlib.Path(r"D:\relay\reports")
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

paths = []
for name in ROSTER:
    hits = list(REPO.rglob(name))
    if hits:
        paths.append(hits[0])

BOLD = re.compile(r"\*\*([^*\n]{6,60})\*\*")
STOP = re.compile(r"^[\W\d]|^(the|a|an|and|but|so|it|this|that|no|not|every|each)\b", re.I)


def terms(text):
    out = []
    for m in BOLD.finditer(text):
        t = m.group(1).strip().rstrip(".:,;—-").strip()
        w = t.split()
        if not (2 <= len(w) <= 6):
            continue
        if STOP.search(t):
            continue
        if any(c in t for c in "()[]{}|`$"):
            continue
        out.append(t.lower())
    return out


mirror_text = {}
counts = collections.Counter()
for p in paths:
    tx = p.read_text(encoding="utf-8", errors="replace")
    mirror_text[p.name] = tx
    for t in set(terms(tx)):
        counts[t] += tx.lower().count(t)

relay_blob = "\n".join(
    p.read_text(encoding="utf-8", errors="replace").lower() for p in RELAY.glob("*.md"))

minted, relay_only, hapax = [], [], []
for t, c in counts.items():
    r = relay_blob.count(t)
    if c >= 2:
        minted.append((t, c, r))
    elif r >= 1:
        relay_only.append((t, c, r))
    else:
        hapax.append((t, c, r))

print("=" * 78)
print("THE RELAY-ONLY SWEEP")
print("=" * 78)
print(f"  mirror files scanned: {len(paths)} of {len(ROSTER)} on the roster")
print(f"  relay reports scanned: {len(list(RELAY.glob('*.md')))}")
print(f"  distinct bolded terms in the mirror: {len(counts)}")
print()
print(f"  MINTED       (2+ mirror occurrences)                 : {len(minted)}")
print(f"  RELAY-ONLY   (1 mirror occurrence, home in relay)    : {len(relay_only)}")
print(f"  MIRROR-HAPAX (1 mirror occurrence, no relay home)    : {len(hapax)}")
print()
print("=" * 78)
print("WORK-ORDERS: relay-only terms, most-cited-in-relay first")
print("(a reader of the mirror meets each of these once, with its elaboration outside)")
print("=" * 78)
for t, c, r in sorted(relay_only, key=lambda x: -x[2])[:40]:
    print(f"  relay×{r:<4} {t}")
print()
print(f"  ... {max(0, len(relay_only)-40)} further relay-only terms not printed")
print()
print("  NOT REPAIRED THIS PASS.  No defect is claimed against any term: a term may be")
print("  perfectly well defined at its single mirror occurrence, in which case the flag is")
print("  a false positive of the occurrence-count proxy.")
