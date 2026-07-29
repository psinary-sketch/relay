# rowgen — Correspondence row generator + differ

A **public** tool. It emits from **kernels** (Lean declarations at pins), never from papers — there is no
research content here, only mechanical facts about compiled terminals.

## What it produces

**Mode `generate`** — for each terminal `{name, repo, pin, module, file}`, a record:
- `check` — the `#check @name` statement, verbatim (via `lake env lean`).
- `axioms` — the `#print axioms name` line, verbatim (NOT rounded — `[propext]` stays `[propext]`).
- `doc` — the declaration's docstring first paragraph, verbatim (from source at the pin).
- `body1` — the proof body's first line.
- `defenc` — **DEFINITION-ENCODED** flag: true if any definition named in the conclusion has a body that
  is a literal constant (`:= 0`, `:= true`, `:= 1`, …) or `True`. This is what catches a stand-in
  (e.g. `topological_constant`, whose conclusion references `topological_contribution := 0`).

**Mode `diff`** — given a paper's Correspondence table (markdown) and the records, it flags each row whose:
- **Status contradicts the docstring** (row says DERIVES; doc says stand-in / encoded / placeholder / deprecated / assigns),
- **profile is rounded** (row reads axiom-free while the record shows `[propext]` or more),
- **pin is stale** (the commit in the row ≠ the record's pin),
- **cited terminal no longer exists** (a configured terminal fails to resolve at its pin),
- **is definition-encoded yet graded DERIVES** (defenc true but the row reads DERIVES, not ENCODES).

**Mode `constellation`** — a corpus cross-reference consistency checker. Given a corpus root and one or
more paper paths, it builds an index (every `.md`'s current title + header version, plus REGISTRY
id→title/version/status rows) and, for each paper, flags: a **stale version** (a `vX.Y` cited next to a
`FILE.md` reference that ≠ the target's current header version), a **stale status** (`pending`/`awaiting`/…
language next to a REGISTRY id whose status is READY/RATIFIED/LANDED/…), and a **nonexistent target** (a
backticked `FILE.md` not on disk). It reads paths passed in; it embeds no corpus content.

## Usage

```
python rowgen.py generate      terminals.json               # -> records.json + a printed table
python rowgen.py diff          terminals.json table.md      # -> row-by-row flags (or 'ok')
python rowgen.py constellation <corpus-root> paper.md [...]  # -> cross-ref contradiction flags
```

`terminals.json` is a list of `{name, repo, pin, module, file}`. `generate` runs `lake env lean` in the
repo, so the repo must be checked out at the pin with its `.lake` built (Mathlib repos: `lake exe cache get`
first). Source-only fields (`doc`, `body1`, `defenc`) come from `git show <pin>:<file>` and need no build.

## Scope / honest limits

- The **missing-terminal** check covers terminals in the config; to audit *every* terminal a table cites,
  feed the full cited set as the config.
- `defenc` is a conservative syntactic check (literal-constant / `True` def bodies in the conclusion); it
  flags stand-ins, not every vacuity — pair it with the `X = X` / `X ↔ X` conclusion-tautology sweep
  (`reports/2026-07-29-tautology-sweep.md`) for the tautological-body shapes.
- The tool reads and reports; it never edits a paper or a kernel.
