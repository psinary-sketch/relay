# -*- coding: utf-8 -*-
"""b331_correspondence.py -- TWO ROWS: THE FOLD FILED; THE ARC AS ONE STATEMENT, AT ITS GRADE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The line counts,
### the F-QUOTE tally and the prefix verdicts are read from `b331_fold_rows.json` and `b331_fold_run.txt`,
### never typed from memory of the run. ### **THE HAZARD:** ### a row that reads as if the arc proved
### something. It proved nothing; it filed eight acts at their own grades, and the row says so first.
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


def read_records():
    r = json.load(io.open(os.path.join(D, 'b331_fold_rows.json'), encoding='utf-8'))
    run = io.open(os.path.join(D, 'b331_fold_run.txt'), encoding='utf-8').read()
    fq = re.search(r'F-QUOTE\s*:\s*(\d+) quotations, (\d+) unfindable', run)
    return dict(added=r['lines_added'], before=r['lines_before'], after=r['lines_after'], section=r['section'],
                nres=len(r['results']), nobs=len(r['obstacles']), nbars=len(r['defective_bars']), ncorr=len(r['corrections']),
                pfx=r['prefix_working'] and r['prefix_blob'], fq_n=int(fq.group(1)), fq_bad=int(fq.group(2)),
                nmech=sum(1 for x in r['lore'] if x[2] == 'MECHANIZED'), njud=sum(1 for x in r['lore'] if x[2] == 'JUDGEMENT'))


SCOPE_TAIL = ("**SCOPE: A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER.** NO THEOREM PROVED HERE OR BY ANY ACT IN "
              "THE ARC. NOTHING ABOUT THE IDENTITY, h2, OR THE ROSTER. NO GRADE MOVED; NO ACT RE-VERDICTED. NO AGGREGATION IS "
              "STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
              "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the "
              "deposit left it. NOTHING DEPOSITS.")


def rows():
    k = read_records()
    return [
        ("THE FOLD, b323 THROUGH b330, FILED INTO THE FINDINGS DOCUMENT UNDER ITS OWN RULES (b331)",
         "THE FOLD, b323 THROUGH b330, FILED INTO THE FINDINGS DOCUMENT UNDER ITS OWN RULES (b331): **A FILING, NOT A RESULT.** "
         "`FINDINGS.md` gains the section `%s`, %+d lines (%d -> %d), its eighteenth section: the eight acts each with its "
         "grade as its own act left it, its own quotation, its scope sentence and its obstacle quoted; the arc's corrections to "
         "its own readings (%d rows); the sealed-bars-found-defective table continued (%d rows); the seats' declared defects as "
         "their own table; the lore (%d mechanized, each with its TECHNE module named; %d judgement); the suite this arc added; "
         "the desk. **THE CONSTRUCTIVE GATE:** F-QUOTE %d quotations, %d unfindable, every one checked against the act that "
         "ORIGINATED it, the discrimination arm firing on an altered quotation; F-COUNT the arc exactly; the generator idempotent "
         "on its second run." % (k['section'], k['added'], k['before'], k['after'], k['ncorr'], k['nbars'], k['nmech'], k['njud'], k['fq_n'], k['fq_bad']),
         "**NO TERMINAL. A FILING.**",
         "**THE NO-GRADE-MOVED CHECK, MECHANICAL: PURELY ADDITIVE %s** -- the pre-append working file a true prefix of the "
         "result, and the blob at HEAD a true prefix on normalised bytes." % k['pfx'],
         "**THE JUDGEMENT THE MECHANISM DOES NOT MAKE** -- that each quoted sentence is its act's own voice and not material the "
         "act was quoting -- is this seat's and is declared in the bank. NO GRADE MOVED.",
         SCOPE_TAIL, "current"),

        ("THE ARC AS ONE STATEMENT, AT THE GRADE THE ACTS SUPPORT, SCOPE BESIDE IT (b331)",
         "THE ARC AS ONE STATEMENT, AT THE GRADE THE ACTS SUPPORT, SCOPE BESIDE IT (b331): **the instrument can say no** -- on "
         "the corpus's own counterexample it said no on the arc's family at every reach tried (b325, b326) and, under a family "
         "derived to the phase condition, said no at seven of eight cells while **the zeta window held at all eight** (b328); "
         "**so the zeta window is a passed test for the discriminating family at this reach**, and for the arc's family b326's "
         "verdict stands; **the finite side is compiled** (b329), general where the header says general and per cell where it "
         "says per cell, every terminal zero-axiom; **the two margins are two evaluations of one distribution separated by the "
         "pole constant** (b324, b327), one distribution on two families and not one functional, the bridge owed; **the "
         "object's archimedean unit is in its space by derivation (b300) and priced at bench (b322)**, unchanged by this arc; "
         "**and the clause has not moved** -- no act in the arc claims otherwise, and the keystone re-read found the arc's "
         "source already graded as stalling at the clause the instrument stalls at.",
         "**NO TERMINAL.** Every clause is an act's own verdict at its own grade, carried with the act that owns it.",
         "**NO PRINT.** The statement is the fold's section's own paragraph, with its scope paragraph beside it.",
         "**A SUMMARY AND NOT A VERDICT.** The instrument's no is a verdict on one family, one instrument, one reach; the "
         "compiled finite side certifies the model's arithmetic and the counting form, not the identification with the "
         "source's trace and not the compact part beyond the cells; the margins' relation is a reading under an import bar.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b331 -- THE FOLD. ### THE TWO ROWS.")
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
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = 'A FILING, NOT A RESULT' in ROWS[0][1] and 'PURELY ADDITIVE True' in ROWS[0][3]
    g2 = 'the clause has not moved' in ROWS[1][1] and 'A SUMMARY AND NOT A VERDICT' in ROWS[1][4]
    print('  row 1 says filing-not-result and purely additive : %s ; row 2 says the clause has not moved and summary-not-verdict : %s' % (g1, g2))
    if not (g1 and g2):
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %d' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; rows to append : %d (numbers %d..%d)' % (max(nums), len(ROWS), start, start + len(ROWS) - 1))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS))) and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0 and all(c == 6 for c in cellcounts) and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
