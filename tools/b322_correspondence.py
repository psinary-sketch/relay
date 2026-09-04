# -*- coding: utf-8 -*-
"""b322_correspondence.py -- TWO ROWS: THE LADDER, AND THE VERDICT THAT TOOK THE WEAKER BRANCH.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE SAYS A RESIDUAL FALLS AND ITS EXPONENT MATCHES A PREDICTION, AND THAT READS AS
###     ### THE MEMBERSHIP QUESTION SETTLED.** ### It is not. ### It is a falling course at five
###     frames whose SIZE the noise gate refuses at every step. ### The row must carry that the RATE
###     half of the registered expectation was ### REFUTED ### -- `p/q = 0.393` against a band of
###     `[0.5, 2.0]` -- and that no unit is adopted.
###   ### ### **ROW TWO SAYS TWO OF THIS ACT'S OWN SEALED BARS WERE DEFECTIVE, AND THAT IS THE ROW
###     ### THAT MATTERS.** ### A record whose registrations are only ever reported as having worked
###     is a record that has stopped reading them. ### The row states both defects and states that
###     the act took the WEAKER of the two branches its own broken rule licensed.
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
    ("THE UNIT'S RESIDUAL GIVEN A RATE, AND A TRUNCATION TAIL THAT PREDICTS IT (b322)",

     "THE UNIT'S RESIDUAL GIVEN A RATE, AND A TRUNCATION TAIL THAT PREDICTS IT (b322): b319 "
     "measured the unit's membership residual constant at 0.4395 across four GRID refinements and "
     "reported a DOMAIN course without fitting it. This act runs the same quantity on the same "
     "domain ladder at stable rank and fits it. **THE RESIDUAL FALLS AT EVERY STEP** -- 0.797250, "
     "0.644963, 0.439502, 0.286136, 0.197491 at X = 8, 16, 32, 64, 128, ranks 20, 37, 69, 133, 262 "
     "-- so by the bar sealed before any definition was unfolded, **THE RESIDUAL IS THE "
     "TRUNCATION'S AND b300's DERIVATION IS NOT CONTRADICTED BY IT.** The fitted exponent is "
     "**p = -0.519901** (fit rms 0.0543). **AND A SECOND ROUTE SHARING NO CODE PREDICTS IT**: "
     "max x u(x) beyond X/2 measures 1.118582, so u decays like 1/x, so the L2 mass beyond X goes "
     "like X^-1/2 -- predicted -0.500000, measured -0.519901, **AGREE** inside the sealed 20 per "
     "cent. **BUT THE RATE HALF OF THE REGISTERED EXPECTATION IS REFUTED**: against b321's "
     "instrument exponent q = -1.324018 by the same fitter on the same five domains, "
     "p/q = 0.392669, outside the sealed band [0.5, 2.0].",

     "**NO TERMINAL, AND THE ONE DECIDABLE THING IS SAID**: whether five floats decrease is "
     "decidable; that the third of them is the object's membership residual is not, and rests on "
     "b316's construction and b319's cut. **THE LADDER REPRODUCES b319 BEFORE IT EXTENDS IT** -- "
     "fixture (i) requires the residual back at b319's banked four decimals on BOTH cuts at "
     "(1024, 8), 0.7973 and 0.9963, and fixture (ii) shows the arm can miss. **A LADDER THAT COULD "
     "NOT REPRODUCE THE ROW IT EXTENDS WOULD BE A DIFFERENT MEASUREMENT WEARING ITS NAME.** The "
     "fitter recovers a planted -0.5 and a planted -1.25 to 1e-12 and returns -5.2e-17 on a flat "
     "course, so **FLAT WAS REACHABLE AND THE COURSE IS NOT FLAT BECAUSE THE DATA IS NOT.**",

     "**THE ORDER'S OWN CONDITION WAS MET AND IT DECIDED THE ACT**: the reading is taken from the "
     "ladder's DIRECTION and taken BEFORE any definition is unfolded, so Component 2 was written "
     "after Component 1 had reported. **AN ACT THAT UNFOLDED THE DEFINITIONS FIRST WOULD HAVE KNOWN "
     "WHICH ANSWER IT WANTED FROM THE NUMBERS.** Eight constituents were unfolded side by side, "
     "neither in the other's language, all sixteen anchors pulling; two differ -- CONDITION TWO and "
     "THE DOMAIN -- and **THEY ARE NOT INDEPENDENT**: the nonzero number at CONDITION TWO is what "
     "the truncation at THE DOMAIN produces, which is what the ladder measured. (B6) ranks "
     "constituents; it does not know which one causes another, and the row says so.",

     "**A FALLING COURSE AT FIVE FRAMES IS A FALLING COURSE AT FIVE FRAMES.** **SCOPE: the "
     "DIRECTION of this residual is reported and the SIZE of no value on the ladder is** -- the "
     "noise-floor gate REFUSES 4 of 4 steps, every one still moving. **NO UNIT IS ADOPTED AND NONE "
     "IS REPLACED**, which is this act's own central cap; b300's derivation stands at "
     "DERIVES-on-IMPORTS and b316's and b319's measurements stand at theirs. `W-ORD-PHI-MU-L2` "
     "stays OPEN and the instrument cannot see it, because a finite array is square-summable "
     "whatever the function behind it does. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly "
     "where the deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("THE MEMBERSHIP LEFT UNDER-RESOLVED WITH ITS PRICE, AND TWO SEALED BARS FOUND DEFECTIVE (b322)",

     "THE MEMBERSHIP LEFT UNDER-RESOLVED WITH ITS PRICE, AND TWO SEALED BARS FOUND DEFECTIVE "
     "(b322): the three arms disagree. The ladder FALLS and the exponent AGREES with the "
     "truncation-tail prediction; but b316's `taper` moves the residual by 0.3 to 0.5 per cent at "
     "every frame, which by the sealed (B2) reads THE VECTOR and not THE EDGE. **THE ACT'S VERDICT "
     "IS UNDER-RESOLVED, AND IT CARRIES ITS PRICE**: from p = -0.519901 and the residual 0.197491 "
     "at X = 128, the domain at which it would reach 0.01 is **X = 3.973e+04, a factor of "
     "3.104e+02** beyond what was reached. That is an extrapolation of a fitted slope and is "
     "labelled as one. **`W-ORD-ARCH-MEMBERSHIP` IS NOT CLOSED**, and the order's own FOOT allowed "
     "exactly this ending.",

     "**NO TERMINAL. NO UNIT IS ADOPTED AND NONE IS REPLACED**, and the two candidate readings are "
     "reported as candidates. **DEFECT 1, IN THIS ACT'S OWN SEALED (B2): THE DICHOTOMY IS NOT A "
     "PARTITION.** b316's taper smooths the DISCONTINUITY in the last eighth of the domain; **IT "
     "DOES NOT RESTORE THE MASS BEYOND X.** *The step at the end of the domain* and *the "
     "truncation* are different things, so a reading of THE VECTOR means NOT THE EDGE "
     "DISCONTINUITY and does not mean NOT THE TRUNCATION. The numbers say exactly that without "
     "being reinterpreted: a cause that was the edge discontinuity would have moved under the taper "
     "and did not; a cause that is the missing tail would not have moved, and did not.",

     "**DEFECT 2, ALSO IN THE SEAL: (B5)'s BRANCHES ARE NOT MUTUALLY EXCLUSIVE.** With (B1a) FALLS, "
     "(B2) THE VECTOR and (B3) AGREE, both the DIFFERENT VECTORS condition and the UNDER-RESOLVED "
     "condition fire, and the registration did not say which wins. **THE RUNNER'S if/elif CHAIN "
     "PICKED DIFFERENT VECTORS, AND THAT ORDERING IS THE TOOL'S AND NOT THE SEAL'S** -- the run "
     "file prints it and the bank does not hide it. **THE ACT TAKES THE WEAKER OF THE TWO**: "
     "DIFFERENT VECTORS is a positive claim about the object, UNDER-RESOLVED is a claim about this "
     "resolution, and **BETWEEN TWO BRANCHES A DEFECTIVE RULE LICENSES EQUALLY AN ACT MAY NOT HELP "
     "ITSELF TO THE STRONGER ONE.** **NEITHER DEFECT IS EDITED; THE REGISTRATION IS SEALED AND "
     "STAYS SEALED**, hash 332a3a83... unchanged from before the ladder ran.",

     "**A QUESTION THAT CARRIES ITS PRICE IS NOT A QUESTION ANSWERED.** **SCOPE: this act priced "
     "the membership question and did not settle it.** The lore gains the resolving-power rule with "
     "its incident: *a question is under-resolved, not open, when the candidates sit closer "
     "together than the instrument's distance from the answer -- and the price is the ratio*; b321 "
     "bought it one act ago when its identity control held and still could not tell two exponent "
     "copies apart. **AN OPEN QUESTION INVITES ANOTHER OPINION; AN UNDER-RESOLVED ONE INVITES A "
     "BIGGER INSTRUMENT.** `W-ORD-ARCH-MEMBERSHIP` and `W-ORD-PHI-MU-L2` stay OPEN. NO ACT IS "
     "RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b322 -- THE MEMBERSHIP.")
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
    # ### **THE TWO GUARDS THAT MATTER FOR THESE TWO ROWS**, and they are guards against the two
    # ### readings the rows most invite: that a class test everything passes says something, and
    # ### that a control which HOLDS is a result about the object.
    g1 = ('RATE HALF OF THE REGISTERED EXPECTATION IS REFUTED' in r1[1]
          and 'NO UNIT IS ADOPTED' in r1[4]
          and 'REPRODUCES b319' in r1[2])
    g2 = ('UNDER-RESOLVED' in r2[1]
          and 'IS NOT A PARTITION' in r2[2]
          and 'CARRIES ITS PRICE' in r2[4])
    print('  row 1 carries the refuted rate half and the unadopted unit : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 takes the WEAKER branch and declares its own bar defective : %s  %s'
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
