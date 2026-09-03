# -*- coding: utf-8 -*-
"""b311_correspondence.py -- TWO ROWS: THE PROOF READ, AND THE MECHANISM THAT DOES NOT TYPE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE RECORDS A READ OF SOMEONE ELSE'S PROOF, AND A READ IN A TABLE OF THE CORPUS'S
###     ### OWN RESULTS READS AS A CORPUS RESULT.** ### It is not one, and the grade cell says so
###     before it says anything else -- ### **NOT ONE PROOF OF THE SOURCE'S WAS VERIFIED HERE.**
###   ### **ROW TWO RECORDS A REFUSAL, AND A REFUSAL READS AS A NEGATIVE RESULT ABOUT THE
###     ### ARCHIMEDEAN PLACE.** ### It is not: it is a statement about TYPES -- that a question
###     answered on one side does not parse on the other -- and ### **THE CORPUS HAS DONE NO
###     MATHEMATICS AT INFINITY HERE.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE SOURCE'S PROOF READ (b311)",

     "THE SOURCE'S PROOF READ (b311): CC 2006.13771v1, read at content, artefact pinned by sha256 "
     "`b8e0b54a…` BEFORE a word of it was read. **THE SOURCE DOES NOT EVALUATE THE COMPRESSED TRACE "
     "AT INDIVIDUAL SCALINGS.** It gives the single-scaling trace *formally* (Prop 1.5(ii)) and "
     "recovers trace class ONLY after smearing against a test function (Prop 1.5(iv)); it isolates "
     "a **trace-remainder** `δ(ρ)` (Def 2.1) and observes that, *unlike the distribution τ(ρ) … "
     "that is not a function because of the divergency at ρ = 1*, **δ IS a function** with **a jump "
     "in its first derivative at ρ = 1**; and it turns that jump into Theorem 3.6's `−2 Id + K_I`, "
     "`K_I` compact — essentially negative, so only finitely many linear conditions are needed. "
     "**AND THEOREM 4.7 PINS THE TRACE SIDE TO THE DISTRIBUTION:** `Tr(ϑ(f)S) = W_∞(f) + ∫ f(ρ⁻¹) "
     "ε(ρ) d*ρ` with `ε` a FUNCTION.",

     "**NO TERMINAL. A READ IS NOT A COMPILE**, and nothing here is machine-checked. `tools/"
     "b311_source.py` pins the artefact by hash and locates **20 fragments, 0 unlocated**, across "
     "pages 1, 2, 8, 10, 11, 12, 13, 18, 26, 27 and 47; the flattener and the hash check are "
     "IMPORTED from `b305_source.py`, whose own fixtures caught two defects in it. **THE TOOL "
     "LOCATES; IT DOES NOT READ** — it cannot tell a correct quotation from an invented one, and "
     "what it can do is fail loudly when a claimed fragment is not in the artefact.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** — the profile stands unchanged at 475. The text layer "
     "was measured intact on all 57 pages by the detector b303 built for a scan where it fired, so "
     "*no page image was needed* is a measurement; and none was available, `pdftoppm` not being "
     "installed. **AND A CORRECTION THIS ACT OWES ITSELF: its sealed registration says the local "
     "artefact was not on this machine. IT IS — in seven places, all byte-identical, none of them a "
     "location the corpus owns.** The seat asserted a negative from a search that had not finished.",

     "**AN IMPORT, READ AT CONTENT, AT THE IMPORT BAR.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S "
     "HONESTY: THIS ACT READ STATEMENTS AND THEIR STATED ROLES. IT VERIFIED NO PROOF OF THE "
     "SOURCE'S, AND NOTHING HERE IS EVIDENCE THAT ANY OF THEM IS CORRECT.** The finding is where "
     "the content sits: **the only part of the trace side that is not an integral against a "
     "function is the part at the identity.** What does NOT follow — and the row says so rather "
     "than letting the phrase do silent work — is that the source's result is *about the identity "
     "alone*: `ε` is not nothing and Theorem 3.6 is about a quadratic form on an interval. **NO "
     "ARCHIMEDEAN NUMBER IS COMPUTED BY THIS ACT.** NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.",

     "current"),

    ("THE MECHANISM DOES NOT TYPE AT INFINITY (b311)",

     "THE MECHANISM DOES NOT TYPE AT INFINITY (b311): b310 closed the finite side with one "
     "sentence — `Tr(θ(t)Π)` is a **signed count of the off-ball points `t` fixes**. **THIS ACT "
     "ASKS WHETHER THAT TYPES AT THE ARCHIMEDEAN PLACE AND DECIDES, BY DEFINITIONS, THAT IT DOES "
     "NOT.** The step at which it parts is **the dimension of the object's space**: at a finite "
     "place `Son(p,n)` is FINITE-dimensional — a truncation — so `θ(t)Π` is finite rank and the "
     "trace is an integer count the first condition can kill; at infinity Sonin's space is, in CC's "
     "own words, *the well-known infinite dimensional Sonin's space*, so the single-scaling "
     "compression is not trace class and **there is no count to take**. In both cases the map fixes "
     "only the origin and the origin lies in the excluded region — **but the finite local term is "
     "an EVALUATION and the continuous one is a JACOBIAN, and a vanishing condition acts on the "
     "first and not on the second.**",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** — a quotation is "
     "not decidable and a definitional decision about an infinite-dimensional Hilbert space is not "
     "finite-decidable. **THE DECISION IS TYPED ROW BY ROW** against b285's HAZARD REGISTER, which "
     "named this species in advance: *the word survives; the object does not*. The ball, the level, "
     "the tower, the unit, the sector and the scale each carry a finite meaning and an archimedean "
     "one, and b198 PROVED there is no archimedean ball at all.",

     "**NO PRINT.** What an archimedean instrument on the object's own space would need, typed and "
     "priced: a **truncation** (CONSTRUCTION — nobody owns it; CC characterise `S(1,1)` as the "
     "eigenvalue-one eigenspace of `P P̂ P`, and the only eigenvectors the corpus has there are the "
     "prolate ones, which b292 derived are NOT in the space); the **unit's membership** (RESULT, in "
     "hand — b300's `(IN, DERIVED)`); the **scaling action** (CONSTRUCTION — and CC's own sentence "
     "is the obstacle: *the scaling action does not restrict to this subspace*); the "
     "**compression** (READ then CONSTRUCTION). **THREE ACTS FOR THE TRUNCATION AND ITS CONTROLS, "
     "TWO MORE FOR THE COMPRESSION, AND ONLY IF `W-ORD-ARCH-NORM-READING` IS SETTLED FIRST — THIS "
     "SEAT'S ESTIMATE, NOT A COMMITMENT.**",

     "**A REFUSAL, NOT A NEGATIVE RESULT.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: this "
     "is a statement about TYPES — that a question answered on one side does not parse on the "
     "other — and THE CORPUS HAS DONE NO MATHEMATICS AT INFINITY HERE.** The navigator's second "
     "expectation is **REFUTED in its first half**: the single non-identity compression does not "
     "have a *vanishing* trace, it has NO trace, and where its formal value is a function that "
     "value is nonzero. Its diagnosis was right — the difference lives at the identity. **THE "
     "RESEMBLANCE BETWEEN A DISCRETE COUNT AND A CONTINUOUS WEIGHT IS NAMED AND REFUSED AS "
     "EVIDENCE; this act exhibits no bridging definition and claims none.** The author's `W2` "
     "window ruling is RECORDED VERBATIM AND NOT APPLIED, and what it obligates is listed. NO "
     "BRANCH IS DECIDED. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED "
     "under its cap.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b311 -- THE READ\'S ROW, AND THE REFUSAL\'S.')
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

    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('VERIFIED NO PROOF' in r1[4] and 'NO ARCHIMEDEAN NUMBER IS COMPUTED' in r1[4]
          and 'A READ IS NOT A COMPILE' in r1[2])
    g2 = ('A REFUSAL, NOT A NEGATIVE RESULT' in r2[4]
          and 'NO MATHEMATICS AT INFINITY HERE' in r2[4]
          and 'REFUSED AS' in r2[4] and 'NOT APPLIED' in r2[4])
    print('  row 1 refuses to be read as a corpus result : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the negative-result reading and records the ruling unapplied : %s  %s'
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
