# -*- coding: utf-8 -*-
"""b325_correspondence.py -- TWO ROWS: THE NEGATIVE CONTROL, AND WHAT ITS CONTROL CAUGHT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### ### **ROW ONE SAYS THE INSTRUMENT DID NOT SEE A FAILING HYPOTHESIS, AND THAT READS AS THE
###     ### INSTRUMENT DISCREDITED.** ### It is not. ### At the arc's cells the arithmetic is
###     essentially absent from BOTH objects -- the form represents nothing between 1 and 4 -- so
###     there was nothing there to see. ### **THE ROW MUST CARRY THE STRUCTURAL REASON AND THE
###     ### PRICED REACH**, or a reader will take a scope statement for a capability statement.
###   ### ### **ROW TWO SAYS A CONTROL CAUGHT A DEFECT IN AN INHERITED CONSTANT, AND THAT READS AS
###     ### b321 IMPEACHED.** ### It is not. ### b321's eleven-prime list is ample at b321's own
###     cells and the two channels agree there to every printed digit. ### **THE ROW MUST SAY SO IN
###     ### THE SAME BREATH**, and must carry this act's own three deviations rather than only the
###     defect it found in someone else's file.
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
    ("THE NEGATIVE CONTROL: THE INSTRUMENT DOES NOT SEE A FAILING HYPOTHESIS AT THE ARC'S CELLS "
     "(b325)",

     "THE NEGATIVE CONTROL: THE INSTRUMENT DOES NOT SEE A FAILING HYPOTHESIS AT THE ARC'S CELLS "
     "(b325): b324 handed on the Epstein discrimination test as the sharpest insight the corpus "
     "held unused. It is run here on the confinement keystone's own object -- the principal form "
     "x^2 + xy + 6y^2, disc -23, h = 3, whose argument-principle census banks TWO ZEROS OFF THE "
     "LINE. The Epstein places sum `SUM_v W_v = PR_Q - A_Q` is **NEGATIVE AT ALL THIRTEEN CELLS**, "
     "from -16.069614947 to -2.243190916. The order's falsifier asked for the forbidden POSITIVE "
     "sign and no cell gives one. **VERDICT: DOES NOT SEE IT. THE REGISTERED EXPECTATION IS "
     "REFUTED AT THE CURRENT REACH.**",

     "**NO TERMINAL, AND THE REASON IS STRUCTURAL RATHER THAN MARGINAL.** The form represents "
     "NOTHING between 1 and 4 -- r_Q(2) = r_Q(3) = 0 -- so the finite channel is **IDENTICALLY "
     "ZERO UNTIL a = 2** and is still only 0.006348865 at a = 3 against an archimedean 2.249539781. "
     "**THE ARITHMETIC HAS BARELY ENTERED AT THE WIDTHS THE ARC SPANS.** Two constituents had to "
     "be built and neither transfers: the archimedean factor is `(sqrt23/2pi)^s Gamma(s)` where "
     "zeta's is `pi^-s/2 Gamma(s/2)` -- the corpus states it in its own census header -- and the "
     "finite side is the coefficient sequence of -Z_Q'/Z_Q, obtained from r_Q by Dirichlet "
     "inversion, **NOT r_Q ITSELF** (they differ by up to 15.74 below n = 60). The lawful class "
     "DOES transfer: Lambda_Q's poles sit at s = 0, 1 as zeta's do, measured pole term -5.03e-17.",

     "**AND THE SILENCE IS A MATTER OF REACH, NOT OF KIND -- PRICED, NEVER VERDICTED.** Beyond the "
     "arc's cells the Epstein sign **CROSSES TO POSITIVE AT a = 22** and stays positive at 24, 28, "
     "32, 50, while zeta stays permitted at every width. **THIS IS NOT A `SEES IT`**: the order's "
     "verdict needs the zero side as corroboration and the corpus owns the OFF-line Epstein zeros "
     "and not the ON-line ones -- the census began at sigma = 0.52 because it was hunting off-line "
     "zeros. **NEITHER CONTROL THE ZETA WINDOW CARRIED TRANSFERS**: the explicit formula cannot "
     "close without those zeros, and Connes-Consani's Theorem 1 does not cover Z_Q at all. What "
     "the price buys is one thing a price should: it converts *try wider cells* into **a measured "
     "width, a ~ 22, at which the instrument would first distinguish a failing hypothesis from a "
     "holding one.**",

     "**A SCOPE STATEMENT IS NOT A CAPABILITY STATEMENT.** **SCOPE: this act decided what the ZETA "
     "WINDOW WAS, at exactly that scope and nowhere wider.** b321 found the zeta window's sign "
     "FORCED by construction and said so before counting; this act finds that at the same widths a "
     "KNOWN-FAILING object's window is equally uninformative, and for a related reason -- not "
     "because the criterion is empty but because the finite side has not arrived. **NOTHING HERE "
     "SAYS ANYTHING ABOUT ZETA, h2, OR THE ROSTER.** NO GRADE MOVED. NO ACT RE-VERDICTED. NO "
     "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands "
     "exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("THE POSITIVE CONTROL FIRED AND CAUGHT AN INHERITED CONSTANT'S UNWRITTEN SCOPE (b325)",

     "THE POSITIVE CONTROL FIRED AND CAUGHT AN INHERITED CONSTANT'S UNWRITTEN SCOPE (b325): zeta "
     "run through the same channels is a control whose correct answer b321 already proved -- for a "
     "lawful f the zeta places sum is -Z with Z a sum of squared moduli, hence **NEVER POSITIVE.** "
     "At a = 32 it came out **+0.003489041**, a value that theorem forbids. The cause is "
     "`b321_window.PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)`, copied from the atlas's own "
     "prime loop, and b321's own header explains why it was left at eleven: the largest cell in this "
     "arc has f supported below 9, so the list is far longer than it needs to be. At a = 32 the support reaches 1024. **WITH EVERY PRIME THE VALUE IS -0.000389214 "
     "AND THE CONTROL PASSES AT EVERY WIDTH TESTED.**",

     "**b321 IS NOT RE-VERDICTED.** At the arc's own cells the two channels agree to every printed "
     "digit -- -0.315810512 at a = 3 from both -- because the list is sufficient there. **THE "
     "CONSTANT IS SCOPE-BOUND, THE SCOPE WAS NEVER WRITTEN DOWN, AND THIS IS THE ACT WHERE IT "
     "BIT.** A second latent defect was found in the owner and NOT repaired there: "
     "`carto_atlas.kernel` memoises without keying on its grid, so a caller that once asked for "
     "nine points gets nine forever. It never bit the atlas, whose every call uses one grid; it "
     "bit this act immediately. **GUARDED IN THE CALLER, REPORTED, LEFT ALONE IN THE OWNER.**",

     "**AND THIS ACT DECLARES THREE FAILINGS OF ITS OWN, NOT ONLY THE ONE IT FOUND ELSEWHERE.** "
     "**(A) THE SEAT RAN AHEAD OF ITS OWN EXECUTION BLOCK** -- the registration was sealed AFTER "
     "the instrument had run. It is section (0) of the sealed file, naming every value already "
     "seen, with every bar marked [ORDER] or [SEAT, POST-HOC] so a reader may discount the second "
     "class entirely; the decisive bar, the falsifier, is the navigator's and could not have been "
     "tuned. **(B) THE SATISFIABILITY CHECKER REFUSED TO SEAL** when that deviation was typed into "
     "the caps table, and it was right -- a cap is a forward commitment, a deviation a historical "
     "fact -- so the clause moved to the registration's face, where it is more prominent, not "
     "less. **(C) THE NOISE-FLOOR GATE WAS FED PAIRS THAT WERE NOT A REFINEMENT**, adjacent cells "
     "rather than one cell at two resolutions; repaired, all three RESOLVED to nine decimals.",

     "**A CONTROL THAT FIRES IS WORTH MORE THAN ONE THAT PASSES.** **SCOPE: the control condemned "
     "an instrument at a width, not an object and not an act.** Every number this act reports from "
     "a width where the positive control failed was withdrawn and recomputed before it was banked. "
     "The e16 tools and the atlas are READ, never edited. NO GRADE MOVED. NO ACT RE-VERDICTED. NO "
     "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED). The seam's debt item 1 restated, "
     "still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this "
     "seat's record. h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]

def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b325 -- THE NEGATIVE CONTROL.")
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
    # ### readings the rows most invite: that an instrument which did not see a failing hypothesis
    # ### is an instrument discredited, and that a control which FIRED impeaches the act it fired on.
    g1 = ('DOES NOT SEE IT' in r1[1]
          and 'REFUTED' in r1[1]
          and 'r_Q(2) = r_Q(3) = 0' in r1[2]
          and 'PRICED, NEVER VERDICTED' in r1[3]
          and 'a ~ 22' in r1[3])
    g2 = ('POSITIVE CONTROL' in r2[1]
          and 'b321 IS NOT RE-VERDICTED' in r2[2]
          and 'RAN AHEAD OF ITS OWN EXECUTION BLOCK' in r2[3]
          and 'NOTHING DEPOSITS' in r2[4])
    print('  row 1 carries DOES NOT SEE IT, the refutation, the reason and the priced reach : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 carries the control firing, b321 unmoved, and this act deviation : %s  %s'
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
