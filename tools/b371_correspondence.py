# -*- coding: utf-8 -*-
"""b371_correspondence.py -- ONE ROW: THE FIRST TARGET, THE DESK CLOSED, THE GUARD MOVED.

### ### **THE HAZARDS THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if the rows had been
### CHECKED; as if a clone were now GUARDED; as if the kernel's README had been repaired; as if three
### earlier acts had been re-verdicted by (R7); or as if `MADE DURABLE` meant `done`.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE = (
    "**SCOPE: NO ROW WAS CHECKED AND NO KERNEL WAS OPENED FOR ANY ROW.** Component 2's cap is the order's own `Audit nothing.`; the inventory takes every field FROM THE ROW and claims no completeness, because a "
    "row whose pin is written in a shape the predicate does not know is reported PINLESS. **NO REPOSITORY IS AUDITED BEYOND THE SINGLE SETTLED CLAIM**, and the second pass (R6) describes is NOT OPENED. **NO "
    ".lean FILE IS TOUCHED, NO BUILD IS RUN AND NO AXIOM PROFILE IS RECOMPUTED** -- the profile was READ as a printed record, at a ref and against its blob. **A CLONE IS NOT GUARDED**: `core.hooksPath` is local "
    "config in an untracked `.git/config`, so a fresh clone carries the guard and still needs one command, and MADE DURABLE is the order's word for what was done, not a claim that it is done. **THE KERNEL'S "
    "README IS NOT REPAIRED** -- its headline, its own breakdown and its assembly ratio disagree with each other and with the profile the same repository ships, and that is recorded and ROUTED, outside this "
    "component's target. **THE GUARD'S OWN FRONT MATTER IS NOT REPAIRED** either: moving the guard made its install line wrong, and the cap licensed one instrument edit. **NO ITEM IS CLOSED WITHOUT ITS KILLING "
    "FILE AND DATE**, and one closure is flagged because its killing file is this act's own. **NO ACT IS RE-VERDICTED**: (R7) reverses a disposition b368, b369 and b370 each carried, and each of them obeyed "
    "the rule it was given -- the author changed the rule. NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT; a count is about what a "
    "document says, not about what is true. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS "
    "CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's "
    "ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    E = json.load(io.open(os.path.join(D, 'b371_reads.json'), encoding='utf-8'))
    S = json.load(io.open(os.path.join(D, 'b371_settle.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b371_repair_desc.json'), encoding='utf-8'))
    I = json.load(io.open(os.path.join(D, 'b371_inventory.json'), encoding='utf-8'))
    H = json.load(io.open(os.path.join(D, 'b371_hookpath.json'), encoding='utf-8'))
    Q = json.load(io.open(os.path.join(D, 'b371_desk.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b371_filing.json'), encoding='utf-8'))
    m = ("**THE ONE CONFIRMED LIVE CLAIM IS `%s`, AND IT WAS EXACT WHEN IT WAS WRITTEN** -- the construction kernel's public description named a `Core` figure of %d, the printed profile carried exactly that at "
         "tag `%s`, and the repository is **%s commits past that tag** with its profile now carrying **%d** (b371, rulings (R6) and (R7))"
         % (S['verdict'], S['figure'], S['tag'], S['head_ahead_of_tag'], S['prints_at_head']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code, and its face declares in unusual detail what was read BEFORE the lock, because the read that settles this "
            "component was begun before it. **THE TEST WAS FIXED BEFORE THE READ, BECAUSE THIS IS WHERE A SEAT WOULD FIT A NUMBER TO A HINT:** SCOPE-DEPENDENT requires that the two words count DIFFERENT "
            "THINGS; STALE is what remains when they count THE SAME THING AT DIFFERENT REFS. They count the same thing -- **the zero-axiom print count of `Core`** -- so the verdict is STALE. **AND THE "
            "ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE AND NOT PROMOTED TO A SCOPE:** the record does name summands that add to the figure, but they are **the composition of the tag's own count, not "
            "a subset of a larger present one**, and reading them as a scope would have been the inference the registration forbade before the read. **THE DESCRIPTION CARRIED NO REF, TAG, VERSION OR DATE AT "
            "ALL**, which is precisely why the figure read as current. BAR 2: the blob and the working file agree (%s) and ls-remote matches HEAD (%s). %d reads, %d without an anchor -- one of the misses was "
            "**a genuinely ambiguous anchor, six identical table headers in one document, and the tool REFUSED it**, which is the tool working."
            % (S['blob_equals_working'], S['pinned'], E['reads'], E['without_anchor']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was recomputed; the profile is a printed record and was read as one, at a named ref and against its committed blob.",
         "**PRINT: FIVE SURFACES, AND ONE OF THEM IS NOT A FILE.** The `SIDE-global-section` **public DESCRIPTION** is repaired and read back byte-for-byte (%s), with the original preserved verbatim in this "
         "act's bank because **a description has no history and nothing else will remember it**; the stale figure is gone (%s) and the register sentence survived the edit (%s). **THE COUNT IS REMOVED RATHER "
         "THAN UPDATED, and that is this seat's judgement, flagged as one** -- replacing one number with another buys one act's correctness and re-arms the same trap, so the description now states the property "
         "the repository asserts everywhere else and names the artifact that holds the number; **the dated-number alternative is banked so the author's choice is one edit away.** `.githooks/pre-push` is NEW and "
         "**TRACKED** in each of the %d rostered repositories, byte-identical to the one source, with `core.hooksPath` set; `tools/b304_hooks.py` -- **the one licensed owner instrument** -- follows the guard, "
         "because a guard that moves while its checker does not is GUARD_WITH_NOTHING_LISTENING. `PLACE-papers/OPEN_TRAILS.md` gains ONE append-only block (%d bytes) **CLOSING `SCAFFOLD-TERMINALS`**. "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** No findings section; no TECHNE file; no module pushed. **THE HOOK AND THE MIRROR ARE OWED AND PAID.**"
         % (R['set_byte_for_byte'], R['stale_figure_gone'], R['register_sentence_survived'],
            len(H['repos']), F['grew']),
         "**THE DESK CLOSED FOR THE FIRST TIME, UNDER (R7): %d ITEMS SWEPT, %d CLOSED, %d STANDING, %d UNCONFIRMED, AND %d CLOSURES REFUSED FOR WANT OF A KILLING FILE.** `SCAFFOLD-TERMINALS` is CLOSED after "
         "b157, b367, b368 and b369; the anchored gate arms close on b363's build and b366's sweep; the hook's non-durability closes on this act. **b368, b369 and b370 each swept and each reported the same "
         "nine marks with the same caveat -- the measurement did not change because the rule did not let it**, and (R7) changed the rule and the desk moved in the same act. **NONE OF THOSE THREE IS "
         "RE-VERDICTED.** **COMPONENT 2, LISTED AND NOT CHECKED:** %d table rows across %d tracked markdown files; **%d name a kernel and a terminal, %d of them with a pin and %d with none**; %d distinct pins. "
         "**A ROW WITHOUT A PIN CANNOT BE CHECKED THE WAY (R6) SPECIFIES**, which checks a row at the kernel and pin the row itself names -- that is a finding, not a hole in the sweep. **%d rows name a "
         "declaration this record has already classified absent**, a cross-reference against a banked finding and **NOT a check**; a row so flagged is not thereby wrong. **THE PRICE SPLITS:** the mechanical "
         "half over the pinned set is one act because a fetch amortises across every row naming the same pin; **the pinless set is not cheaper, it is unpriceable under (R6) as written and needs a ruling before "
         "it needs an act**; and one of the order's three ranking factors **cannot be filled without opening a kernel**, so it is recorded as NOT FILLED for every row. **COMPONENT 3: %s**, chosen by a test and "
         "not by preference -- exercised in both polarities in every repository with %d failing. **AND A CLONE IS STILL NOT GUARDED:** what changed is which half is missing -- before, the clone had neither the "
         "guard nor the wiring; now it carries the guard and lacks one command, `%s`. **A SMALLER HOLE, AND NOT NO HOLE.** The old location is left inert -- **a safety net and a trap** -- and the byte-identity "
         "arm catches the drift. **THE EXPECTATIONS ARE SCORED:** the navigator's SPLITS -- its scope half **REFUTED** (there is no scope, there is a ref) and its unstated half **CONFIRMED and more strongly "
         "than it was put** (no qualifier at all); this seat's (E1) **HALF MET, HALF REFUTED** (pinless rows exist but do not outnumber the pinned); (E2) **MET, and it was the weak one and was recorded as such "
         "before the act ran** -- it predicted that a copy would copy. **AND THE ADJACENT FINDING IS THE SHARPER HALF AND IS ROUTED, NOT REPAIRED:** the kernel's own README says %s terminals, its breakdown sums "
         "to %d, its ratio says %d/%d, and the profile it ships carries %d -- **and the README travels with a clone while the description does not.**"
         % (Q['items'], Q['closed'], Q['standing'], Q['unconfirmed'], Q['closures_refused'],
            I['table_rows_scanned'], I['files'], I['rows'], I['with_pin'], I['without_pin'],
            I['distinct_pins'], I['flagged_count'], H['outcome'], len(H['failing']),
            H['residual_step'], S['readme_headline'], S['readme_breakdown_sum'],
            S['readme_ratio'][0], S['readme_ratio'][1], S['prints_at_head']),
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b371 -- ONE ROW: THE FIRST TARGET, THE DESK CLOSED, THE GUARD MOVED.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (b302): %s %s' % (pos, neg))
    print('  SPLITTER FIXTURE (b303): %s %s %s %s' % (sa, sb, sc, sd))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = ('EXACT WHEN IT WAS WRITTEN' in ROWS[0][0]
          and 'SAME THING AT DIFFERENT REFS' in ROWS[0][1]
          and 'NOT PROMOTED TO A SCOPE' in ROWS[0][1]
          and 'REFUSED it' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'no build was run' in ROWS[0][2]
          and 'has no history' in ROWS[0][3]
          and 'flagged as one' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'CLOSED FOR THE FIRST TIME' in ROWS[0][4]
          and 'NONE OF THOSE THREE IS' in ROWS[0][4]
          and 'NOT a check' in ROWS[0][4]
          and 'CLONE IS STILL NOT GUARDED' in ROWS[0][4]
          and 'SMALLER HOLE, AND NOT NO HOLE' in ROWS[0][4]
          and 'REFUTED' in ROWS[0][4]
          and 'NO ROW WAS CHECKED' in ROWS[0][5]
          and 'A CLONE IS NOT GUARDED' in ROWS[0][5]
          and 'NO ACT IS RE-VERDICTED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says the settling and its test, the coincidence refused, no terminal, the five '
          'surfaces with the description flagged, the desk closing with three acts not re-verdicted, '
          'the inventory with its cap and its unfillable factor, the guard with its residual hole, the '
          'expectations, the adjacent finding routed, and the scope : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK : last row number is %d ; cells on disk %s' % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
