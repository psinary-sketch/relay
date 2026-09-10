# -*- coding: utf-8 -*-
"""b399_components.py -- THE WRITES OF b399, EVERY ONE MEASURED AGAINST THE PRE-ACT BLOB.

### ### **THE FACE IS LOCKED AT `80e5e547...` BEFORE THIS FILE RUNS**, and this file writes only
### what the locked face's section (I) names.

### ### **WHAT IT WRITES.**
###   (1) `FINDINGS.md` -- ### **ONE POINTER**, after the ranking's verdict sentence. ### **NO CELL,
###       NO GRADE, NO RANK AND NO VERDICT SENTENCE IS EDITED**, which is Addition Three's own test.
###   (2) `FACES_LEDGER.md` -- the `F2-F3` OWED pair row's LAST CELL only, appended to, still OWED.
###   (3) `OPEN_TRAILS.md` -- the bridge row's owed and trigger cells, and ONE NEW ROW carrying the
###       routed grade propagation with a firable trigger, under RULING (R23).
###   (4) `EMERGING_RESEARCH_PROGRAMMES.md` -- three contacts appended to the `Contacts` section.

### ### **EVERY EDIT IS BY ANCHOR AND BY CONTENT** (`(R2)`), and ### **EVERY EDITING ANCHOR RUNS
### WITH `editing=True` SO IT REFUSES TO RESOLVE INSIDE A PRESERVED BLOCK** (`b396`).
### ### **AND EVERY FILE IS DIFFED AGAINST ITS PRE-ACT BLOB, NOT AGAINST THE INDEX** (`b382`): a
### `git show HEAD:<path>` read, so a working-tree edit cannot be mistaken for the baseline.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
EMERG = os.path.join(PP, 'EMERGING_RESEARCH_PROGRAMMES.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
MEAS = {}


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def blob(repo, relpath):
    """### **THE PRE-ACT BASELINE IS THE COMMITTED BLOB AND NEVER THE INDEX** (`b382`)."""
    out = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + relpath],
                         capture_output=True)
    if out.returncode != 0:
        return None
    return out.stdout.decode('utf-8', 'replace').replace('\r\n', '\n')


def lines_of(txt):
    return [x for x in txt.split('\n')]


def _cellwise_carried(pre_row, post_rows):
    """### **THE BAR FOR A ROW THIS ACT EDITS IN PLACE IS CELL-WISE, NOT WHOLE-LINE.**

    ### The first form of this measure used a WHOLE-ROW PREFIX bar, and it was wrong the moment a
    ### cell in the MIDDLE of a row was appended to: everything after that cell shifts, so the
    ### pre-edit row is no longer a prefix of the post-edit row and a correct edit reads as a loss.
    ### ### **IT FIRED ON THIS ACT'S OWN TRAILS ROW AND THAT IS HOW IT WAS FOUND.**
    ### ### **THE RIGHT BAR: SAME CELL COUNT, AND EVERY PRE-EDIT CELL A PREFIX OF ITS OWN
    ### ### POST-EDIT CELL.** ### Nothing is dropped, nothing is reordered, and any cell that lost
    ### text fails.
    """
    cells = [c.strip() for c in pre_row.split('|')]
    for cand in post_rows:
        pc = [c.strip() for c in cand.split('|')]
        if len(pc) != len(cells):
            continue
        if all(b.startswith(a) for a, b in zip(cells, pc)):
            return True
    return False


def measure(tag, repo, relpath, path, inplace=()):
    """### **CONTENT LOST IS COUNTED, NOT ASSERTED.** ### Every pre-act line must be present after,
    ### EXCEPT the lines this act DECLARED it edits in place -- and each of those must still carry
    ### its own pre-edit content as a PREFIX, which is checked here and not taken on trust.
    ### ### **A ROW NOT ON THE DECLARED LIST GETS THE LINE-IDENTITY BAR, SO THE EXEMPTION CANNOT BE
    ### ### WIDENED BY AN EDIT THE FACE DID NOT NAME.**
    """
    pre = blob(repo, relpath)
    post = io.open(path, encoding='utf-8').read().replace('\r\n', '\n')
    if pre is None:
        rec('    ### **NO PRE-ACT BLOB** -- %s is untracked; nothing to measure against.' % relpath)
        return
    a, b = lines_of(pre), lines_of(post)
    declared = set(inplace)
    seta = {}
    for x in a:
        seta[x] = seta.get(x, 0) + 1
    setb = {}
    for x in b:
        setb[x] = setb.get(x, 0) + 1
    missing = sorted([x for x, n in seta.items() if setb.get(x, 0) < n and x.strip()])
    carried, lost = [], []
    for x in missing:
        if x in declared and _cellwise_carried(x, b):
            carried.append(x)
        else:
            lost.append(x)
    rec('    %-26s lines %d -> %d  (+%d)  ### **CONTENT LOST : %d**'
        % (tag, len(a), len(b), len(b) - len(a), len(lost)))
    rec('      declared in-place edits carried by prefix : %d of %d'
        % (len(carried), len(declared)))
    for x in lost[:5]:
        rec('        ### **LOST:** %s' % x[:150])
    if len(carried) != len(declared):
        rec('        ### **A DECLARED IN-PLACE EDIT WAS NOT CARRIED BY PREFIX** -- counted as a'
            ' loss above.')
    MEAS[tag] = dict(pre=len(a), post=len(b), lost=len(lost), inplace=len(declared),
                     carried=len(carried))


def write(path, lines):
    io.open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))


# ==================================================================================================
#  (1) FINDINGS.md -- THE POINTER. ### NO GRADE MOVES.
# ==================================================================================================
POINTER = (
    '**Where the re-rank of this ranking lives — a pointer added 2026-09-10 (b399), and nothing '
    'else.** The ranking above and its verdict sentence are **b332’s, each as its owning act left '
    'them**, under this section’s own rule that *every grade above is its owner’s and none was '
    'conferred here*. **b333 re-ranked K5 the next day** — `DEFINED-ONLY` superseded by '
    '`DERIVES-ON-IMPORTS`, so K5’s softest grade becomes `MEASURED-AT-COVERED-CELLS` and **K5 and '
    'K6 tie at the softest rank** — and that re-rank is carried **in this same document**, under '
    '*Addendum to `clause-stated` — filed 2026-09-06 (b333)*, at **The re-rank, under the sealed '
    'rule with nothing adjusted**. **b399 added this sentence and moved no grade:** repairing the '
    'row itself would move a grade rather than a citation, so under the order’s own test the row, '
    'its grade cell, its rank, its verdict sentence and the aim-map sentence stand unedited and '
    'the grade move is **ROUTED**, filed in `OPEN_TRAILS.md` with a trigger.')


def do_findings():
    bar('=')
    rec('  ### (1) `FINDINGS.md` -- THE POINTER, AND THE GRADE THAT DID NOT MOVE.')
    bar('=')
    path = FINDINGS
    txt = io.open(path, encoding='utf-8').read().replace('\r\n', '\n')
    ls = txt.split('\n')
    i, ln = AF.find(path, 'The softest rank is held by', editing=True)
    rec('    the verdict sentence, anchored : `FINDINGS.md:%d`' % i)
    rec('      > %s' % ' '.join(ln.split())[:220])
    row_i, row = AF.find(path, '| 1 | **K5** the archimedean distribution | `DEFINED-ONLY`',
                         editing=True)
    rec('    the stale row, PRESERVED VERBATIM AND NOT EDITED : `FINDINGS.md:%d`' % row_i)
    rec('      > %s' % ' '.join(row.split())[:300])
    before_row = ls[row_i - 1]
    before_verdict = ls[i - 1]
    aim_i, aim = AF.find(path, 'The aim-map is named as the act that would chart', editing=True)
    before_aim = ls[aim_i - 1]
    out = ls[:i] + ['', POINTER] + ls[i:]
    write(path, out)
    after = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    rec('    ### ### **THE THREE THINGS THE ORDER FORBIDS MOVING, CHECKED BYTE FOR BYTE AFTER THE'
        ' WRITE:**')
    for tag, want in [('the ranking row', before_row), ('the verdict sentence', before_verdict),
                      ('the aim-map sentence', before_aim)]:
        rec('      %-24s present unchanged : %s' % (tag, want in after))
        MEAS['unchanged:' + tag] = want in after
    rec('    ### **GRADES MOVED : 0. ### GRADES CONFERRED : 0. ### CELLS EDITED : 0.**')
    rec('    ### **POINTERS ADDED : 1.**')
    measure('FINDINGS.md', PP, 'FINDINGS.md', path)


# ==================================================================================================
#  (2) FACES_LEDGER.md -- THE OWED PAIR ROW'S LAST CELL.
# ==================================================================================================
LEDGER_ADD = (
    ' ### **SHARPENED AGAIN 2026-09-10 (b399), AND STILL OWED — AND WHAT WAS OWED IS NOW KNOWN '
    'FALSE.** `(M)` was tested by sign and then attempted. **The sign test: SURVIVES, and '
    'VACUOUSLY** — `(M)` forces `Σ_p W_p(g ⋆ ḡ♯) ≤ 0` on the source’s class, the record’s three '
    'lawful seeds (`a = 1.30, 1.35, 1.41`, the only cells inside Theorem 1’s support window, b318) '
    'read `0.000000000` in **both** of the record’s prime columns, and every cell where the prime '
    'sum changes sign is a cell that **fails** that support condition; the zero is an **empty sum** '
    'and b321 had already said *THAT THE COVERED CELLS ARE SILENT IS A FACT ABOUT A SUPPORT AND NOT '
    'A FINDING.* **The attempt: `(M)` IS REFUTED, by a printed value.** Theorem 4.7 as an equality '
    '(b321) gives `−Tr(θ(g) S θ(g)*) = −W_∞(f) + margin`, so at `a = 1.30` the left side is '
    '`−8.622324442` (or `−8.509769366` with b320’s measured margin) while the right side is `0` '
    'exactly — and no normalization (a positive rescaling), no sign convention (`+8.62 = 0` fails '
    'as `−8.62 = 0` does) and no truncation (a Frobenius norm only grows with the frame) closes it. '
    '**Graded MEASURED-AT-COVERED-CELLS, its weakest link.** So this row is **NOT PAID and NOT '
    'OWED IN THE SAME WAY: the statement it was waiting for is false**, and what it needs instead '
    'is a different statement that **b399 does not name**. The second obstruction is untouched: the '
    'Sonin margin is not defined on the Li family (b327). **NOTHING IS PAID HERE, NO GRADE IS '
    'CONFERRED, AND THE DEPOSIT’S REFUSAL STANDS.**')


def do_faces():
    bar('=')
    rec('  ### (2) `FACES_LEDGER.md` -- THE OWED PAIR ROW, SHARPENED AND STILL OWED.')
    bar('=')
    path = FACES
    ls = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    i, row = AF.find(path, '| F2–F3 | OWED |', editing=True)
    rec('    the row, anchored : `FACES_LEDGER.md:%d`  (%d cells)' % (i, len(row.split('|'))))
    rec('      ### **PRE-EDIT TAIL, PRESERVED:** %s' % ' '.join(row.split())[-220:])
    cells = row.split('|')
    assert cells[-1].strip() == '', 'the row must end on a pipe'
    assert cells[2].strip() == 'OWED', 'the status cell must read OWED before and after'
    cells[-2] = cells[-2].rstrip() + LEDGER_ADD + ' '
    new = '|'.join(cells)
    ls[i - 1] = new
    write(path, ls)
    after = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    st = after[i - 1].split('|')[2].strip()
    rec('    ### **STATUS CELL AFTER THE EDIT : `%s`** ### -- unchanged : %s'
        % (st, st == 'OWED'))
    rec('    ### **CELLS EDITED : 1 (the last). ### GRADES CONFERRED : 0. ### ROWS PAID : 0.**')
    rec('    ### **AND THE PRE-EDIT TEXT IS A PREFIX OF THE POST-EDIT CELL : %s**'
        % (('|'.join(row.split('|')[:-1])).strip().rstrip('|').strip()
           in after[i - 1]))
    MEAS['ledger_status'] = st
    measure('FACES_LEDGER.md', PP, 'FACES_LEDGER.md', path, inplace=(row,))


# ==================================================================================================
#  (3) OPEN_TRAILS.md -- THE BRIDGE ROW, AND ONE NEW ROW WITH A TRIGGER.
# ==================================================================================================
OWED_ADD = (
    ' **b399: the first half of what was owed is now REFUTED, not merely absent.** `(M)` — '
    '`−Tr(θ(g) S θ(g)*) = Σ_p W_p(g ⋆ ḡ♯)` — survives the sign test **vacuously** (every in-class '
    'prime sum in the record is an empty sum) and is then **refuted by value** at `a = 1.30`: '
    '`−8.622324442` against `0` exactly, under either sign convention. So what is owed is a '
    '**different** relation, and **no act has named it**.')
TRIG_ADD = (
    '; **FIRED AGAIN by the b399 ferry, and answered `(M)` IS REFUTED** (b399) — the trigger stays '
    '**THE AUTHOR’S WORD**')
NEWROW = (
    "| **4** | `W-ORD-E0-RANK-PROPAGATION` | **REPAIR** | b332's E0 ranking table in `FINDINGS.md` "
    "still reads `1. K5 ... DEFINED-ONLY`, with the sentence *The softest rank is held by K5* and "
    "an aim-map sentence carrying the same grade; **b333 re-ranked K5 the next day** "
    "(`DEFINED-ONLY` superseded by `DERIVES-ON-IMPORTS`, K5's softest becoming "
    "`MEASURED-AT-COVERED-CELLS`, **K5 and K6 tied**) and that re-rank is carried in the same "
    "document, in b333's own addendum. What is owed is the **grade move** through the table itself: "
    "the row, the rank order, the verdict sentence and the aim-map sentence. **b399 added a pointer "
    "and refused the grade move**, under the ferry's own test — *if repairing it would move a grade "
    "rather than a citation, do NOT repair it*. | unpriced; b399 measured it at four sentences in "
    "one file | **THE AUTHOR'S WORD, on whether a later act may move a grade inside a table whose "
    "own head says every grade in it is its owner's** — and it cannot fire on a seat's own "
    "judgement, which is why b399 routed it |")


def do_trails():
    bar('=')
    rec('  ### (3) `OPEN_TRAILS.md` -- THE BRIDGE ROW, AND THE ROUTED ITEM WITH A TRIGGER.')
    bar('=')
    path = TRAILS
    ls = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    i, row = AF.find(path, '| **1** | `W-ORD-LI-WEIL-BRIDGE` |', editing=True)
    rec('    the bridge row, anchored : `OPEN_TRAILS.md:%d`  (%d cells)'
        % (i, len(row.split('|'))))
    cells = row.split('|')
    rec('      ### **PRE-EDIT TRIGGER CELL:** %s' % ' '.join(cells[-2].split())[:220])
    cells[4] = cells[4].rstrip() + OWED_ADD + ' '
    cells[-2] = cells[-2].rstrip() + TRIG_ADD + ' '
    ls[i - 1] = '|'.join(cells)
    j, last = AF.find(path, '| **3** | `W-ORD-LI-FAMILY-CONTROL` |', editing=True)
    rec('    the last row of the table, anchored : `OPEN_TRAILS.md:%d`' % j)
    ls = ls[:j] + [NEWROW] + ls[j:]
    write(path, ls)
    after = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    rec('    ### **ROWS EDITED : 1. ### ROWS ADDED : 1.**')
    # ### **THE (R23) SWEEP, RUN AGAIN ON THE TABLE'S OWN HEADER-BOUNDED POPULATION** (`b398`).
    hdr = [k for k, x in enumerate(after, 1)
           if x.startswith('| | trail | species | what is owed') and 'trigger' in x]
    rec('    the table`s own header, located : %s' % hdr)
    pop = []
    for k in range(hdr[0] + 1, len(after) + 1):
        x = after[k - 1]
        if not x.startswith('|'):
            break
        if x.startswith('|:--') or x.startswith('|---'):
            continue
        pop.append((k, x))
    rec('    rows in the table, bounded by its own header : %d' % len(pop))
    none_rows = [k for k, x in pop if x.split('|')[-2].strip().lower() in ('none', '`none`', '')]
    rec('    ### ### **ROWS WHOSE TRIGGER READS `none` OR IS EMPTY : %d %s**'
        % (len(none_rows), none_rows or ''))
    MEAS['trails_rows'] = len(pop)
    MEAS['trails_none'] = len(none_rows)
    measure('OPEN_TRAILS.md', PP, 'OPEN_TRAILS.md', path, inplace=(row,))


# ==================================================================================================
#  (4) EMERGING_RESEARCH_PROGRAMMES.md -- THE THREE COMPUTE CONTACTS.
# ==================================================================================================
CONTACTS = """
*Provenance of the three below: the navigator's conversation layer, 2026-09-09, ratified by the b399 ferry. Filed here and nowhere research-facing.*

### Contact C — The finite channel as a proved zero-conservation interface

At a finite place the source's construction on the object returns the test function at the identity times a constrained dimension, carrying no logarithm and no sampling at prime powers — the corpus's `K3`, derived on content at b310 and compiled at kernel terminals `B329.*` (24, zero-axiom) and `B310.*`. The contact reads that as an **interface which conserves zero**: a channel that is present, addressable, and contributes nothing arithmetic, so that a place-wise architecture can carry it without paying for it.
- **Anchors:** relay `data/b310_the_smear_collapses.txt` (the collapse to the identity term); `FINDINGS.md`, the clause statement's `K3` row (the kernel terminals and the per-cell compact part); relay `data/b399_the_sign_and_the_refutation.txt` (the finite-place sum measured as an EMPTY SUM at every lawful seed of the record).
- **The one consequence:** an interface whose contribution is provably zero on a class can be composed without a budget — *checkable wherever such an interface is specified, not checked here.*
- **No claim.** Nothing is computed; no architecture is proposed; the corpus's own reading of `K3` stands exactly where b310 and b329 left it.

### Contact D — The collapse to the identity term as a structure-not-arithmetic economy

The same collapse has a second face: what the construction returns is decided by the **structure** of the object at the place (a dimension and an evaluation at one point) and not by the arithmetic of the place. b310's own words for it: *the test function read at one point, times a dimension.* The contact reads that as an **economy**: the cost of a channel falling to a structural constant when the arithmetic would have been the expensive part.
- **Anchors:** relay `data/b310_the_smear_collapses.txt`; relay `data/b305_the_arithmetics_entry.txt` (*the arithmetic enters through neither the test function nor the operator — it enters through the distribution they are paired against*); `FINDINGS.md`, the places-sum paragraph of the clause statement.
- **The one question, not answered here:** *which channels of a place-wise construction are structural in this sense and which are not.*
- **No claim.** No cost model is stated; the word *economy* is the contact's and is not the corpus's.

### Contact E — The pole term that belongs to no channel

The Li side's decomposition has three terms, and the third is not a place: `λ_n = S_∞(n) − S_f(n) + 1`, the `+1` a contribution from the pole of `ξ(s)` at `s = 0` (Lagarias, arXiv:math/0404394v4, read at content from the artefact pinned by sha256 `86f3d3c4…`). The corpus's own arrangement has the same shape from the other side: for a lawful `f` the pole column vanishes identically (b321). The contact reads the pole term as a **caution**: a place-wise architecture that enumerates places will be short exactly one term, and the term it is short is the one that decides constants.
- **Anchors:** `FACES_LEDGER.md`, the Li-side row (`S_∞`, `S_f`, and the pole term named); relay `data/b321_the_window_opened.txt` (the pole column, `~1e-16` at every cell, and the collapse `Σ_v W_v = −Z` it licenses); relay `data/b327_the_faces_ledger.txt` (the deposit's channel as the archimedean place **plus** the pole constant, marked DIFFERENT).
- **The one consequence:** any construction indexed by places needs a declared home for a term that is not a place — *a design obligation, not a result.*
- **No claim.** Nothing follows here about the Li coefficients, the pole, or any architecture; b327's DIFFERENT stands as b327 wrote it.
"""


def do_contacts():
    bar('=')
    rec('  ### (4) `EMERGING_RESEARCH_PROGRAMMES.md` -- THE THREE COMPUTE CONTACTS.')
    bar('=')
    path = EMERG
    ls = io.open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    i, _h = AF.find(path, '## Contacts — filed 2026-09-05 (b327)', editing=True)
    rec('    the `Contacts` section, anchored : `EMERGING_RESEARCH_PROGRAMMES.md:%d`' % i)
    while ls and ls[-1].strip() == '':
        ls.pop()
    add = [x for x in CONTACTS.split('\n')]
    ls = ls + add
    write(path, ls)
    after = io.open(path, encoding='utf-8').read()
    rec('    ### **CONTACTS APPENDED : %d** ### -- C, D and E, each after the existing A and B.'
        % sum(1 for x in ('### Contact C', '### Contact D', '### Contact E') if x in after))
    rec('    ### **PROVENANCE LINES IN THE SECTION : %d** ### -- `b327`s, covering A and B, and'
        ' this act`s, covering C, D and E.' % after.count("the navigator's conversation layer"))
    rec('    ### **CLAIMS CARRIED : 0** ### -- and the count is the new blocks that end on'
        ' `No claim.`: %d of 3.'
        % sum(1 for x in after.split('### Contact ')[1:] if '**No claim.**' in x
              and x[:1] in 'CDE'))
    rec('    ### **SEEDS CREATED : 0. ### PROMOTION CRITERIA SET : 0.**')
    rec('    ### ### **AND THE FILE IS THE ONLY ONE THEY ARE WRITTEN IN** -- the order`s words:')
    rec('    ### ### *in the emerging-programmes ledger only and nowhere research-facing.*')
    MEAS['contacts'] = sum(1 for x in ('### Contact C', '### Contact D', '### Contact E')
                           if x in after)
    measure('EMERGING_RESEARCH_PROGRAMMES.md', PP, 'EMERGING_RESEARCH_PROGRAMMES.md', path)


def main():
    bar('=')
    rec('b399_components.py -- THE WRITES, EACH MEASURED AGAINST THE PRE-ACT BLOB.')
    rec('### The face is LOCKED at `80e5e547...` and this file writes only what section (I) names.')
    rec('### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    bar('=')
    rec()
    do_findings()
    rec()
    do_faces()
    rec()
    do_trails()
    rec()
    do_contacts()
    rec()
    bar('=')
    lost = sum(v['lost'] for v in MEAS.values() if isinstance(v, dict) and 'lost' in v)
    rec('  ### ### **FILES EDITED : 4. ### TOTAL CONTENT LOST : %d.**' % lost)
    rec('  ### ### **GRADES MOVED : 0. ### GRADES CONFERRED : 0. ### ROWS PAID : 0.**')
    rec('  ### the measurements, carried in this record and in no second file:')
    rec('  ### %s' % json.dumps(MEAS, sort_keys=True))
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = os.path.join(D, 'b399_components_run.txt')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
    # ### **NO SECOND DATA FILE IS WRITTEN.** ### The locked face's section (I) names
    # ### `b399_components_run.txt` and no `.json` beside it, and ### **A FILE THE FACE DOES NOT
    # ### NAME IS NOT WRITTEN JUST BECAUSE IT WOULD BE CONVENIENT.**
    print('\n  wrote %s' % out)
    return 0 if lost == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
