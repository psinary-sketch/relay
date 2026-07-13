# Federation sweep — 2026-07-13 (trail item O.20)

Read-only survey of **41 repositories** under `D:\`, then resolution of what it found.

## The survey

**Zero dirty trees. Zero unpushed commits.** Every `SIDE-*` kernel with a remote is in sync with it.
On the criterion O.20 was written to catch — uncommitted work sitting unseen — the SIDE-effects
incident that prompted the sweep was the only one, and it landed the same day (`a27415d`).

## The criterion was too narrow

The sweep surfaced four exposures of a class the trail item had not named: not **unpushed**, but
**unrecorded** — work the corpus cites that version control had never seen, or repositories no remote
had ever seen. Two of the four would have passed a dirty-tree check cleanly, and both were
corpus-cited.

### 1. Two kernels were outside version control entirely — RESOLVED

`SIDE-fano-darkness` and `SIDE-li-map` had **no `.git` directory at all**: no history, no remote, no
branch — while cited by FINDINGS `F.2026-07-09-k` as compiled and machine-checked. A dirty tree is one
`checkout` from loss; these were one `rm` from loss, with nothing to recover *from*.

Both preserved as-found and pushed (private, pending author say-so — nothing unscreened goes public),
then screened: build gate, `#print axioms` at the pin on a clean tree, salt-check on the statements.

**Both pass. Both DERIVE.**

- **Fano** (`0f6ce5b`; `lean FanoTwoDarkness.lean`, exit 0, no `sorry` warning): four theorems at
  `[propext]`, three with **no axioms at all**, two at `[propext, Quot.sound]`. The seven `decide`s
  *compute* the incidence facts from the defined Fano structure — derivation, not stipulation. The
  2-(7,3,1) certificate is real.
- **Li-map** (`73cee42`; exit 0, no `sorry` warning): two theorems axiom-free, one at `[propext]`, five
  at `[propext, Quot.sound]`. No `sorry`, no `decide`, no shell shapes.

**Count correction:** `F.2026-07-09-k` claims "11 theorems" of the Fano kernel; there are **nine**. All
the mathematics that entry describes is present and compiles — the incidence certificate and both
moment theorems. Only the count was wrong. (Fourth count-claim corrected this wave; the reason the
corpus cites named terminals now.)

**Divergence check:** both files are byte-identical to their second copies under
`traversal-2026-07-09/`, so the two-copy hazard flagged in the orphan census resolves with no ruling.

### 2. Two repositories had no remote — PRESERVED, RULING PENDING

Two paper archives existed on one disk only. Both are now pushed (private). Their reconciliation
against PLACE-papers **inverted the assumption**: they are not stale leftovers. For **three papers the
archives hold the later and substantially longer draft**, while PLACE-papers — the declared source of
truth — holds the older one. One of the three is nearly disjoint in text from its PLACE-papers
counterpart.

Consolidate or archive-in-place is an author ruling (OPEN_TRAILS O.21). **Nothing was merged; nothing
was overwritten.** The content is safe either way now.

### 3. A stale duplicate clone — RESOLVED (removed)

`SIDE-kernel-github`, 17 commits behind the same origin as the canonical clone: not a data-loss risk
but a **mis-citation trap** — anyone reading it sees a pre-v1.2 kernel. Gate held before deletion (no
unique commits, branches, stashes, tags or untracked files; the three files it carried that the
canonical clone lacks are deliberately-removed history — a rename and an orphan-probe cleanup —
reachable at `8a06885`, an ancestor of `origin/main`). Removed. **The canonical working clone of the
kernel is `D:\SIDE-kernel` and nothing else.**

### 4. A `.PENDING` twin — RESOLVED (removed)

`DEPOSIT_v1_2_NOTES.md.PENDING`: the unfilled template (`PENDING-S4` placeholders) of the tracked,
completed record. Strict predecessor, nothing in it the tracked file lacks.

## The rule, generalized

The sweep henceforth checks three things, not one:

1. **dirty trees** — uncommitted work (the original criterion);
2. **repositories without remotes** — committed work on one disk only;
3. **content outside version control entirely** — the worst class, because there is no history to
   recover from.

**"Unrecorded" is the class; "dirty" was one instance of it.**

## For the loom's register

Two kernels the corpus has been citing as verified had never been under version control, and their
axiom profiles had never been run at a pin. They pass — but they pass *today*, at a SHA, on a clean
tree, with the command recorded. Before today they were assertions about files on a disk that no one
could reproduce: the same defect as an unpinned profile, arriving one layer earlier. Not "the profile
was run against the wrong tree," but *"there was no tree to run it against."*

## Pending rulings (clearly separated from the settled)

- **Visibility** of `SIDE-fano-darkness` and `SIDE-li-map` — private now; they passed screening, so the
  flip to public is the author's call.
- **O.21** — three archive papers are later than PLACE-papers' copies. Consolidate, or archive in place.
