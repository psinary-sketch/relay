# -*- coding: utf-8 -*-
"""b328_correspondence.py -- TWO ROWS: THE CONDITION DERIVED AND THE SEEDS BUILT; THE CONTROL'S VERDICT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The verdict words
### and numbers are read from `b328_family.json`, `b328_build.json`, `b328_derive.json`.
### ### **THE HAZARD:** ### `SEES IT` reads as the instrument having seen a counterexample IN GENERAL; it is
### a verdict on this family at this reach; and it says nothing about zeta beyond the control's scope.
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

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rows():
    fam = json.load(io.open(os.path.join(D, 'b328_family.json'), encoding='utf-8'))
    bld = json.load(io.open(os.path.join(D, 'b328_build.json'), encoding='utf-8'))
    der = json.load(io.open(os.path.join(D, 'b328_derive.json'), encoding='utf-8'))
    v = fam['verdict']
    e = [x for x in bld if x['kind'] == 'E']
    o = [x for x in bld if x['kind'] == 'O']
    cells = sorted(fam['cells'], key=lambda c: (c['kind'], c['a']))
    tab = '; '.join('%s%g: Q %s %+.3e, zeta %s %+.3e, Q %s, zeta %s' % (c['kind'], c['a'], c['gate_q']['sign'], c['channels']['places_q'],
                                                                     c['gate_z']['sign'], c['channels']['places_z'], c['closure']['status_q_all'], c['closure']['status_z'])
                    for c in cells)
    r2_verdict = {
        'SEES IT': "**VERDICT: SEES IT** at %s -- the Epstein places side ALONE takes the forbidden sign, the cell closes for the Epstein function with every located zero, the first quadruple accounts for the sign, and zeta under the same seed is certified NEGATIVE and closes." % fam['sees'],
        'ZETA FLIPS': "**VERDICT: ZETA FLIPS** at %s -- reported first and walked link by link in the bank; a defect in the chain until proven otherwise." % fam['flips'],
        'PARTIAL': "**VERDICT: PARTIAL** at %s -- a certified positive Epstein sign whose corroboration is incomplete." % fam['partial'],
        'DOES NOT SEE IT': "**VERDICT: DOES NOT SEE IT** -- no certified positive Epstein places side at any cell of either seed; the reason named from the numbers in the bank.",
    }[v]
    entail = ("**THE ENTAILMENT, AT EXACTLY ITS SCOPE:** on this instrument, at this reach, for this family, the finite-instance places sum computed without any zero distinguishes a function whose hypothesis holds from one whose hypothesis fails; the zeta window is a PASSED TEST for this family -- and for the arc's family b326's verdict stands unmoved."
              if v == 'SEES IT' else "**NO ENTAILMENT IS STATED.** The row records what was measured.")
    return [
        ("THE DISCRIMINATING FAMILY, DERIVED AND BUILT: A LAWFUL SEED'S FOUR-TERM SUM AT AN OFF-LINE QUADRUPLE IS "
         "4 Re(G_e^2 - G_o^2), AND TWO SEEDS AIMED AT THE EPSTEIN FUNCTION'S FIRST OFF-LINE ZERO REACH THE PHASE "
         "CONDITION (b328)",
         "THE DISCRIMINATING FAMILY, DERIVED AND BUILT: A LAWFUL SEED'S FOUR-TERM SUM AT AN OFF-LINE QUADRUPLE IS "
         "4 Re(G_e^2 - G_o^2), AND TWO SEEDS AIMED AT THE EPSTEIN FUNCTION'S FIRST OFF-LINE ZERO REACH THE PHASE "
         "CONDITION (b328): from the source's (147)-(148) and its involution f^7(x) = x^{-1} f(1/x), f = g * g^7 has "
         "f~(s) = g~(s) g~(1 - s), so the quadruple {rho, conj rho, 1 - rho, 1 - conj rho} sums to **4 Re[G(c) G(-c)]**, "
         "c = rho - 1/2; for an even seed (g = g^7) this is **4 ‖G‖^2 cos(2 phi), negative exactly past forty-five "
         "degrees of phase**; an odd component contributes -4 Re G_o^2, negative only below it. **CHECKED AGAINST b326's "
         "BANKED FOUR TERMS** at the thirteen arc cells (the arc's phases %.2f to %.2f degrees, all below the threshold, "
         "every sign the banked sign; the seed-formed sum against the banked sum within %.1e, the discretization of the "
         "square). TWO SEEDS BUILT on the corpus's own bump: the sine-aimed even seed env(v) sin(gamma_1 abs(v)) at phases"
         "%s degrees and the cosine-aimed odd seed sgn(v) env cos(gamma_1 v) at %s degrees, widths a = 20, 40, 81, 160, "
         "each lawful (Definition 3.1 scan; the pole conditions measured to vanish)."
         % (min(der['B3']['phases']), max(der['B3']['phases']), der['B1']['worst'],
            ', '.join('%.2f' % x['transform']['phase_deg'] for x in e), ', '.join('%.3f' % x['transform']['phase_deg'] for x in o)),
         "**NO TERMINAL. A DERIVATION FROM QUOTED TEXT AND A CONSTRUCTION.** The navigator's (F1) DERIVES as asserted; "
         "(F2) is MET -- the even seed reaches the threshold without an odd component at every registered width. "
         "**TWO SEALED BARS FOUND DEFECTIVE BY RUNNING THEM, NEITHER EDITED:** (B1) at 1e-9 relative fails at 1.1e-7 "
         "because the banked terms are the transform of the DISCRETIZED square (the 8193-grid square differs 16 times "
         "more, a second-order grid term); (B4) at 1e-10 fails at 2e-6 because Simpson's rule on the seed's own nodes "
         "straddles a kink in every triple -- on the 2x grid it is exact to 7e-13 and a Gauss-Legendre route integrating "
         "the same function meets the bar at 3e-13. The seat's first diagnosis of (B4) (second order) was refuted by its "
         "own 2x ratio and is kept beside the corrected one.",
         "**THE PHASE IS WHERE b326 SAID THE SIGN STRUCTURE WAS MISSING**, and it comes from sinh(delta v) for an even "
         "seed: zero on the line, small at narrow widths, set near ninety degrees by a sine aimed at the ordinate. The "
         "lore gains the rule with its gate (both polarities). NO GRADE MOVED. NO ACT RE-VERDICTED.",
         "**SCOPE: A DERIVATION, A CONSTRUCTION. NOTHING ABOUT ZETA, h2, OR THE ROSTER FOLLOWS FROM THIS ROW.** The "
         "criterion is the source's, with its pole terms handled by the seed's vanishing at 0 and 1, as Proposition C.1 "
         "requires. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 "
         "restated, still unpaid. NOTHING DEPOSITS.",
         "current"),

        ("THE NEGATIVE CONTROL UNDER THE DISCRIMINATING FAMILY: %s (b328)" % v,
         "THE NEGATIVE CONTROL UNDER THE DISCRIMINATING FAMILY: %s (b328): the places sides computed with NO ZERO "
         "(b326's channels, imported: the pole term, the archimedean channels by two routes, zeta's prime sum by two "
         "routes, the Epstein finite side with Lambda_Q by two routes), every sign through the noise-floor gate at du "
         "and du/4; the closure with every located zero (146 on the line, 17 off it; zeta's 10000 ordinates) as "
         "corroboration, the off-line terms reported separately. THE CELLS: %s. %s" % (v, tab, r2_verdict),
         "**NO TERMINAL.** %s The zeta control under the same seed: %s." % (
             entail,
             'the permitted sign at every cell, certified, and the formula closing' if all(c['gate_z']['sign'] == '-' and c['closure']['status_z'] == 'CLOSES' for c in cells)
             else 'NOT the permitted sign at every cell -- see the bank'),
         "**WHAT THE FAMILY IS:** the first enumerated way the clause could fail on this instrument -- a seed whose "
         "transform at the off-line zero carries a phase past forty-five degrees (even) or below it (odd). The faces "
         "ledger's Epstein row is updated by the writer and the trail W-ORD-DISCRIMINATING-FAMILY carries its status. "
         "**b326's DOES NOT SEE IT ON THE ARC'S FAMILY STANDS**; what changed is the family, not the arc's verdict.",
         "**SCOPE: A COMPUTATION ON THE EXPLICIT-FORMULA INSTRUMENT, ON THIS FAMILY, AT THIS REACH.** NOTHING ABOUT "
         "TOTALITY. NOTHING ABOUT h2 OR THE ROSTER BEYOND THE CONTROL'S OWN SCOPE. NO GRADE MOVED; NO ACT RE-VERDICTED. "
         "NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED). The patent lane carried on the patent seat's "
         "report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",
         "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b328 -- THE DISCRIMINATING FAMILY. ### THE ROWS.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s' % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %d' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))
    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('4 Re[G(c) G(-c)]' in r1[1] and 'FOUND DEFECTIVE' in r1[2] and 'NO GRADE MOVED' in r1[3])
    g2 = ('NO ZERO' in r2[1] and 'VERDICT' in r2[1] and "b326's DOES NOT SEE IT ON THE ARC'S FAMILY STANDS" in r2[3] and 'NOTHING ABOUT TOTALITY' in r2[4])
    print('  row 1 carries the quadruple formula, the defective bars, no grade moved : %s  %s' % (g1, 'PASS' if g1 else '### FAIL ###'))
    print("  row 2 carries no-zero, the verdict, b326 unmoved, nothing about totality : %s  %s" % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s' % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1
    lines = ['| %d | %s | %s | %s | %s | %s |' % (start + k, stmt, term, prof, grade, status) for k, (_m, stmt, term, prof, grade, status) in enumerate(ROWS)]
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS))) and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0 and all(c == 6 for c in cellcounts) and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
