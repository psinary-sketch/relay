# -*- coding: utf-8 -*-
"""b307_correspondence.py -- TWO ROWS: WHERE THE ARITHMETIC ENTERS, AND THE SPECIES MATCH.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED** -- from
### `b303_correspondence.py` and `b302_correspondence.py` respectively. ### The guard fired on its
### first reuse at b304, before any write; ### **IT IS REUSED HERE FOR THE SAME REASON: THESE ROWS
### CARRY `W_p` AND `|U|`-SHAPED NOTATION AND A MARKDOWN TABLE READS EVERY BAR AS A CELL BOUNDARY.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE RECORDS A READ OF SOMEONE ELSE'S PAPER**, and a read in a table of the corpus's
###     own results reads as a corpus result. ### **IT IS NOT. ### THE GRADE CELL SAYS SO.**
###   ### **ROW TWO RECORDS AN IDENTIFICATION**, and an identification in this table reads as a
###     route. ### **IT IS NOT: IT SAYS THE CORPUS HAS AN OBJECT, NOT THAT IT CAN DO ANYTHING WITH
###     IT**, and the grade cell says that before it says anything else.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402  ### the blank-cell audit, READ not copied
import b303_correspondence as G   # noqa: E402  ### the notation guard, READ not copied

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE ADELIC ARC FOLDED (b307)",

     "THE ADELIC ARC FOLDED (b307): ten acts, b297–b306, filed into `FINDINGS.md` as **THE ADELIC "
     "ARC, b297–b306 — THE FOLD**. **A FILINGS SECTION: no grade moves, no act is re-verdicted, "
     "nothing in it is new mathematics, and no keystone is written or edited** — the preceding "
     "campaign's keystone (b299) is cross-referenced, not duplicated. Each entry carries its grade "
     "as *its own act* left it, with its scope sentence and **its obstacle, quoted**. The arc as "
     "one statement: the object's two halves now share a form and a dilation; the finite side's "
     "first-level mass is annihilated exactly when either radius clears its threshold; the "
     "archimedean instruments compute with vectors outside the object's own space; and the corpus "
     "works at the open end of a single window parameter whose closed end is the source's forced "
     "positivity.",

     "**NO TERMINAL. A FOLD IS A FILING.** `tools/b307_fold.py` is the section's **generator, not "
     "its reviewer** — a quotation failing `F-QUOTE` never reaches `FINDINGS.md` at all. **20 "
     "quotations, 0 unfindable**, each checked against the act that **originated** it, with a "
     "discrimination arm (an altered quotation must come back unfindable). **TWO FAILED ON THE "
     "FIRST RUN AND THE DOCUMENT WAS NOT WRITTEN**: one spanning a hard wrap, and one that was a "
     "sentence b303 was *quoting from b301* — the gate catching a mis-attribution before it "
     "existed. Both re-pointed at what the files emit; neither re-typed.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** — the profile stands unchanged at 470. "
     "`FINDINGS.md` **+80 / −0**, measured by `numstat`: **F-NOGRADE did not fire, and *purely "
     "additive* is the measurement rather than the assertion.** F-COUNT: results and obstacles "
     "each cover exactly the ten. F-NOKEYSTONE: 0 files under any keystone path. F-NOSHADOW: 0 "
     "`.lean` files touched in either repository.",

     "**A FILING, AND ITS GRADE IS THAT OF THE ACTS IT FOLDS AND NO HIGHER.** **SCOPE, PRINTED "
     "BESIDE THE ARC SENTENCE: nothing about the identity, `h2`, or the complete roster follows "
     "from it.** One half of the one-signed residual is derived (b260's junction) and the other is "
     "at bench (b261's `E2even`), and **a summary may not upgrade a bench result by standing it "
     "next to a derived one.** The family is a definition and not a route; the window sentence is "
     "about two settings of one parameter, not about what either setting proves. **NO AGGREGATION "
     "IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left "
     "it.**",

     "current"),

    ("THE LEDGER CENSUS AND THE CONDITIONAL STRIKE (b307)",

     "THE LEDGER CENSUS AND THE CONDITIONAL STRIKE (b307): the ferry scan fired on the **order's "
     "own closing** — `U-2`, *a closing sequence asserts that a ledger is current*, struck at "
     "b300. **The strike is CONDITIONAL and the record names the condition:** *SURVIVES: the same "
     "phrase after a check that has COUNTED WHAT IS MISSING.* No such check existed, which is why "
     "the phrase had been unusable since b300. **This act built it.** "
     "`tools/b307_handoff_census.py` counts, mechanically, the arc's acts, the live work-orders "
     "and the arc's findings section against `HANDOFF.md`. **BEFORE: 26 missing — ten acts, "
     "fourteen work-orders, one section. AFTER: 0.**",

     "**NO TERMINAL.** The census is a name-count with both polarities fixtured, including the "
     "boundary arm that stops `b30` being found inside `b300` — **without it an absent act reports "
     "present.** It is run **before and after** the ledger is written, and the act's use of the "
     "phrase is conditioned on the after-count rather than on the seat's judgement.",

     "**NO PRINT.** The measured facts: `HANDOFF.md`'s head had read b278 since b293 by the strike "
     "record's own account, and the census confirms it mechanically — **the ledger named none of "
     "the ten acts and none of the fourteen live work-orders.** After the write, 0 of 26 remain.",

     "**A LICENCE EARNED AND BOUNDED.** `U-2`'s `SURVIVES` clause is satisfied for **this ledger "
     "and no other**. **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: the census counts NAMES, "
     "NOT UNDERSTANDING** — a ledger naming every act in one line each would pass it and could "
     "still be a bad handoff — and it says **nothing about `FINDINGS.md`, `REGISTRY.md`, "
     "`OPEN_TRAILS.md`, `VERIFICATION_LOOM.md` or the desk**, which were not counted and are not "
     "claimed. **NO GRADE MOVES. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED.**",

     "current"),
]

_RETIRED_ROWS = [
    ("THE CORPUS'S DIFFERENCE IS NOT THE SOURCE'S (b307)",

     "THE CORPUS'S DIFFERENCE IS NOT THE SOURCE'S (b307): decided by definitions, constituent by "
     "constituent. **VERDICT: DIFFERENT.** The source's difference is Theorem 1's inequality "
     "`W_∞(g * g*) ≥ Tr(ϑ(g) S ϑ(g)*)` — a SINGLE-PLACE statement whose finite places enter "
     "through eq. (149) and are ZEROED, not excluded, by the support condition (*so that rational "
     "primes are not involved*). The corpus's is `L − R = −(E2even + junction)` at cells "
     "`a² ∈ {2,3,4,8,9,12}`. **THE FIRST DIFFERING CONSTITUENT IS THE ARCHIMEDEAN SIDE**, and the "
     "quotation is b291's: *SO NEITHER PAIRED FAMILY LIES IN THE OBJECT'S ARCHIMEDEAN SPACE.* A "
     "trace compressed ONTO Sonin's space is a sum over vectors IN it; the corpus's runs over "
     "vectors provably OUTSIDE it. **The prime side DOES match (b305, carried) — and a difference "
     "of two things is the same object only if both are.**",

     "**NO TERMINAL. A DECISION BY DEFINITIONS IS NOT A COMPILE.** The arithmetic half is "
     "`tools/b307_difference.py`, which parses BOTH tables out of their emitting files — b254's "
     "fourth face-off and b248's second-object split — and never retypes either. Exact `Fraction` "
     "arithmetic, no float; tolerance `1.5e-6` **derived from three six-place roundings and stated, "
     "not chosen after seeing the numbers.**",

     "**NO PRINT. NOTHING COMPILED THIS ACT**; the profile stands unchanged at 470. The checks: "
     "b248's internal identity holds at all six cells; **b254's `D − E2` is the negative of b248's "
     "`E2even` at all six** (largest discrepancy 4.29e-07), which is what settles that the order's "
     "`E2even` is b254's archimedean half and not a shared letter; b254's residual is "
     "`(D − E2) − (PR − Θ_q)` at all twelve rows; the sign is negative 12 of 12. **0 checks "
     "failing. AND A FINDING: b254 and b248 print junctions differing by 1e-6 at `a² = 4` and "
     "`a² = 9`** — within tolerance, no verdict affected, filed as `W-ORD-JUNCTION-LAST-PLACE`.",

     "**DIFFERENT, DECIDED BY DEFINITIONS, WITH FOUR CONSTITUENTS HAVING NO COUNTERPART AT ALL** "
     "(the smeared operator, the compression, `W_∞`, and the places summed over). All three "
     "registered falsifiers HOLD. **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: NO "
     "MEASUREMENT IS DISTURBED AND NO GRADE MOVES.** `E2even` being a different functional says "
     "nothing about whether it was measured correctly; the junction stays `DERIVES`, `E2even` stays "
     "at bench, b254's (IMBALANCED) stands. The source is not criticised — its theorem is about its "
     "own objects at its own window, and **the corpus's window is the complementary choice of the "
     "same knob: the source picks its window so no prime enters, the corpus so every prime up to "
     "`a²` does.** **NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands "
     "exactly where the deposit left it.**",

     "current"),

    ("THE SHARED-TARGET STEM SWEEP (b307)",

     "THE SHARED-TARGET STEM SWEEP (b307): the stem sweep is extended to the files every act "
     "appends to and no act swept — `CORRESPONDENCE.md` and `banked_index.py`. This closes the hole "
     "b305 named in its own bank: *the sweep runs over this act's files and not over "
     "CORRESPONDENCE.md, so the row was caught by the bank's hit and not by its own.* **THE TOOL "
     "REPORTS PER ROW AND DOES NOT REFUSE**, because a hit in a shared file may be older than the "
     "act running, and the row number is the attribution.",

     "**NO TERMINAL.** `tools/b307_stem_scope.py`; the stems are read from `ferry_scan.stems()` "
     "and **never copied**, so a stem added or retired moves the sweep with it. Fixtures on both "
     "polarities and on the row-attribution arm — **a sweep that found a hit but could not say "
     "which row carries it would leave an act unable to tell its own row from an ancestor's, which "
     "is the whole point of extending the scope.**",

     "**NO PRINT.** Three hits on the first run, all one stem, each attributed: "
     "`banked_index.py` line 400 — **THIS SEAT'S OWN, from b305, where the fix touched the "
     "generator and not the generated artefact; REPAIRED and read back by querying the index.** "
     "`CORRESPONDENCE.md` row 101 — b284's, a defect when written (the stem entered the list at "
     "b142) that **the old sweep could not see; NOT REWRITTEN.** Row 2 — predates b142, so **not a "
     "defect at all; a ban is not retroactive.** After the one repair: index 0 hits, table 2, both "
     "ancestors'.",

     "**A SCOPE REPAIR, NOT A RESULT.** **SCOPE: THIS ROW RECORDS THAT A CHECK NOW LOOKS WHERE IT "
     "DID NOT, AND THAT IT IMMEDIATELY FOUND THIS SEAT'S OWN WORK.** The boundary drawn: **repair "
     "what this seat wrote and mis-fixed; file what another act owns** — the append-only law "
     "governs the difference between *cannot* and *will not*. No grade moves, no verdict is "
     "revised, and no ancestor's row is edited. **M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED.**",

     "current"),
]

_RETIRED_ROWS = [
    ("WHERE THE SOURCE'S ARITHMETIC ENTERS (b305)",

     "WHERE THE SOURCE'S ARITHMETIC ENTERS (b305): read at content in CC, arXiv:2006.13771v1. **THE "
     "PRIMES ARE CARRIED BY THE LOCAL WEIL DISTRIBUTION `W_p(f) = (log p) Σ_{m≥1} ( f(p^m) + "
     "f♯(p^m) )` — eq. (149), Appendix B.** So the arithmetic enters through **NEITHER the test "
     "function NOR the operator, but the DISTRIBUTION they are paired against.** The operator "
     "`ϑ(g) S ϑ(g)*` contains no prime — `ϑ` is the scaling action, `S` the Sonin projection, `g` a "
     "bump — and its positivity is the `A*A` shape with `A = S ϑ(g)*`, S being a projection. The "
     "test function contributes a **SUPPORT**, which gates which primes appear: the source's own "
     "reason for taking supp ⊂ (1/2,2) is *so that rational primes are not involved (see (149))*.",

     "**NO TERMINAL. A READ IS NOT A COMPILE**, and nothing here is machine-checked. The artefact "
     "is pinned: 57 pages, sha256 "
     "`b8e0b54ade8535cf3ca633d1ef325bfc5c793b407da577a83d111726935b58e0` — **the same artefact b304 "
     "pinned, with the hash re-computed rather than carried.** `tools/b305_source.py` locates each "
     "quoted fragment by page index and **measures that the text layer is intact** (0 pages "
     "truncated, 0 pages without text), so the act's claim that no page image was needed is a "
     "measurement; the detector it uses is b303's, built for a scan where it fired.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** — the profile stands unchanged at 470. The located "
     "fragments: the test-function class and the *only finitely many primes* sentence (page index "
     "0); the support conditions, the Sonin projection, the positivity sentence and the "
     "∆-normalization (page index 1); Theorem 1 (page index 2); eq. (7) (page index 3); eq. "
     "(148)–(150) (page index 49). **11 of 11 located, 0 missing.**",

     "**AT CONTENT, THIS ACT'S OWN READ.** **SCOPE: THIS ROW REPORTS WHAT A SOURCE SAYS AND IS NOT "
     "A RESULT OF THE CORPUS.** It draws no analogy to the corpus's objects — that is the next "
     "row's work, and keeping them apart is the order's own restriction. **IT REFUTES A REGISTERED "
     "FALSIFIER:** (F1), *the arithmetic enters through the test function and not the operator*, is "
     "**REFUTED in its first half by eq. (149)**; the second half is right. It also settles "
     "`W-ORD-FORCED-POSITIVITY`: the source never asks its positivity to carry arithmetic — "
     "Theorem 1 is an INEQUALITY between an arithmetic distribution and a forced-positive trace, "
     "and the content is in the difference. **NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.**",

     "current"),

    ("THE CORPUS'S PRIME SUM IS THE LOCAL WEIL DISTRIBUTION (b305)",

     "THE CORPUS'S PRIME SUM IS THE LOCAL WEIL DISTRIBUTION (b305): decided by definitions. The "
     "corpus's adopted summand is `w_{p,k} = 2 log p · p^{-k/2} · corr(log p^k)` (b260, adopted "
     "b229). Under **CC's own normalization** `W_v(f) := W_v(Δ^{-1/2} f)`, the k-th term of eq. "
     "(149) is `(log p) · p^{-k/2} · ( f(p^k) + f(p^{-k}) )`. **THESE ARE THE SAME EXPRESSION, "
     "FACTOR BY FACTOR** — same `log p`, same `p^{-k/2}` from the same Δ-normalization, and **the "
     "corpus's factor 2 is CC's `f + f♯` collapsed under evenness.** Against the quotient channel "
     "the answer is the opposite: the orbit ratio `(p^n − p^k)/(p^n − 1)` is dimensionless, carries "
     "neither factor, is silent at the top level by its own range, and is **a WEIGHT applied to a "
     "prime term rather than a carrier of primes.**",

     "**NO TERMINAL.** A species comparison is a decision by definitions, not a compile. Its inputs "
     "are pulled from emitting files: b260 for the `PR` summand and the `w − τ` relation, b220's "
     "extract for act 9's closed form with its range, b17's staircase for the index set. **The one "
     "place the match rests on a convention the corpus records by a factor rather than by a "
     "sentence is named in the bank: the evenness that collapses `f + f♯` into a 2 is carried by "
     "that 2.**",

     "**NO PRINT.** Nothing compiled. The identification is between two written expressions, one "
     "the source's and one the corpus's, and **a finite model of it would certify the model** — "
     "`log p` and `p^{-k/2}` are transcendental and real-valued. The shadow check was run and "
     "returned nothing buildable.",

     "**SAME SPECIES AS THE PRIME SUM — AND THE SAME OBJECT TERM FOR TERM. NOT THE SAME SPECIES AS "
     "THE QUOTIENT CHANNEL.** **(F2) HOLDS, MORE STRONGLY THAN REGISTERED.** **SCOPE, AND IT IS "
     "THE WHOLE OF THE ROW'S HONESTY: HAVING THE OBJECT IS NOT DOING WITH IT WHAT THE SOURCE "
     "DOES.** The source pairs `W_v` against a compressed trace and proves an inequality; the "
     "corpus pairs `PR` against an orbit-count channel and measures a separation. Same left object, "
     "different right object, different statement. **The quotient channel is not demoted by being a "
     "different species — a weight is not a lesser object than a distribution.** **NO AGGREGATION "
     "IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED.**",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b307 -- THE DECISION\'S ROW, AND THE SWEEP-SCOPE ROW.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    # ### THE ROW-SPECIFIC GATES. ### **EACH ROW MUST CARRY THE REFUSAL ITS OWN HAZARD NEEDS.**
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('NO TERMINAL' in r1[2] and 'NO PRINT' in r1[3]
          and 'and no higher' in r1[4].lower())
    g2 = ('counts NAMES, NOT UNDERSTANDING' in r2[4] and 'NO TERMINAL' in r2[2])
    print('  row 1 declares no terminal/print and caps its own grade : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 bounds the licence it records : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
