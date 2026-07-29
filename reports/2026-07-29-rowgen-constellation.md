# rowgen constellation mode — built + tested — 2026-07-29

Extended `tools/rowgen` with a **constellation** mode: a corpus cross-reference consistency checker. For
each reference a paper makes to another corpus document (backticked `FILE.md`, or a REGISTRY id), it checks
the target's **current** title / header-version / status and flags contradictions — **stale title**,
**stale version**, **"pending" language for something now closed**, or a **nonexistent target**. It reads
paths passed in and embeds no corpus content (the tool stays public/generic; the corpus is the argument).

## Test — four RH-rail papers + SILENCE_STAGES

Index built over 230 `.md` files + 100 REGISTRY rows. Results:

| paper | flags |
|:--|:--|
| `THE_RESIDUE_OF_RH.md` | **0** — clean |
| `PATHS_TO_THE_CRITICAL_LINE.md` | **0** — clean |
| `THE_UNCONDITIONAL_SURROUND.md` | **1** — STALE-VERSION (below) |
| `SIMPLICITY_OF_RIEMANN_ZEROS.md` | **0** — clean |
| `SILENCE_STAGES_DEALIGNMENT.md` | **1** — NONEXISTENT-TARGET (below) |

### Flag 1 — REAL stale-version (actionable; not edited — report-only + rail read-only)

`THE_UNCONDITIONAL_SURROUND.md` L106 cites *"Paths to the Critical Line **v0.2**"*, but
`PATHS_TO_THE_CRITICAL_LINE.md`'s own header is **v0.6** (2026-07-24). The tool read the target's current
header version and caught the citation as two versions behind. **Compounding finding:** the **REGISTRY row**
for PATHS (`1.5a-5`) is *also* stale at **v0.2** — so the citation matches a stale ledger, and both trail the
file's actual v0.6. This is a genuine constellation contradiction (a document and the REGISTRY both cite an
old version of a rail paper). **Not edited** — SURROUND and PATHS are RH rail (read-only, no authorization
sought), and this is a report-only pass; flagged for the author. *(A fix would re-version the SURROUND
citation to v0.6 and update the REGISTRY 1.5a-5 row — both author calls; the REGISTRY update is not a rail
edit and could land independently.)*

### Flag 2 — NONEXISTENT-TARGET (true, but intentional provenance)

`SILENCE_STAGES_DEALIGNMENT.md` L233 references `ERROR_CORRECTION.md`, which no longer exists on disk. The
tool is correct that the file is absent — **but the reference is the intentional rename-provenance line**
(*"File renamed `ERROR_CORRECTION.md` → `SILENCE_STAGES_DEALIGNMENT.md`"*), a deliberate historical record,
not a broken live cross-reference. **No action** — the mention names the old file by design. *(This shows the
tool flags nonexistent targets correctly; the human verdict distinguishes a broken pointer from a provenance
mention. A future refinement could whitelist rename-provenance contexts.)*

## Tool note (honest limit)

An earlier run produced one **false positive** — a bare decimal in prose (`…14.13…`) matched as a version
next to a `FILE.md` reference. Tightened: the *cited* version must carry a literal `v` prefix; the FP is
gone, the real v0.2/v0.6 flag survives. The **current** version is read from the target's header (first 15
lines); if a header embeds a kernel pin as its first `vX.Y`, that could still mislead — the two rail papers
tested read their doc-version correctly, but the header-version heuristic is the mode's soft spot and is
noted in the README.

## Disposition

Constellation mode works: it caught **one real stale-version** (SURROUND + REGISTRY citing PATHS v0.2 vs the
file's v0.6) that prior passes missed, and correctly flagged a nonexistent target (an intentional provenance
mention). **No edits this pass** (report-only; rail read-only). Committed: `tools/rowgen/rowgen.py` +
`README.md`. Nothing deposited.
