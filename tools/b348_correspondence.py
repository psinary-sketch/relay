# -*- coding: utf-8 -*-
"""b348_correspondence.py -- ONE ROW: THE FOLD, b339 THROUGH b347.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if a fold were a result, as if the arc
### amounted to more than its acts, as if the census graded the record, as if a judgement rule were enforced, or as
### if naming the failure-mode partition had opened it.
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

SCOPE_TAIL = ("**SCOPE: A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES. IT PROVES NOTHING, DISCHARGES NOTHING, AND MOVES NO GRADE.** The arc statement stands at the "
              "grade its acts already support and adds none. The rate axis resolves the two CONVENTIONS and does NOT make a convention correct; b313's clause governs. The floor "
              "is NOT explained -- one axis of three was moved. W-ORD-LI-FAMILY-CONTROL stays OWED: the zero side and the finite side are not evaluated. The census is a "
              "measurement OF the record and not a grade on it, and the gate it reports is PROSPECTIVE. The minted species is a JUDGEMENT RULE and is not listed beside the "
              "mechanized ones. THE FAILURE-MODE PARTITION IS NAMED AND NOT OPENED, and no such partition is known to exist. Nothing about the quantifier, h2, totality or the "
              "roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on "
              "the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING "
              "DEPOSITS.")


def rows():
    F = json.load(io.open(os.path.join(D, 'b348_fold.json'), encoding='utf-8'))
    c = F['census']
    m = ("THE PRICED-AND-RESOLVED ARC FOLDED, b339 THROUGH b347: NINE ACTS ARE ONE SECTION OF THE FINDINGS DOCUMENT, PURELY ADDITIVE, WITH EVERY QUOTATION VERIFIED AT THE ACT "
         "THAT ORIGINATED IT AND THE NO-GRADE-MOVED CLAIM ITSELF MECHANICAL; ONE SPECIES MINTED AND FILED AS A JUDGEMENT RULE BECAUSE IT IS NOT MECHANIZABLE IN THE GATE; THE "
         "CENSUS RESTATED AS A FINDING ABOUT THE RECORD; AND THE FAILURE-MODE PARTITION NAMED AS A PROPOSAL AND NOT OPENED (b348)")
    stmt = (m + ": **THE FOLD.** %d rows, each carrying its grade AS ITS OWN ACT LEFT IT, its scope sentence, and its obstacle as a quotation located at that act and nowhere "
            "else; quotations failing %d, grade anchors failing %d -- and a quotation or a grade that could not be found at its own act would never have reached the file. "
            "Three further tables drawn from the acts' own declarations: %d corrections the acts made to their OWN readings, %d sealed bars found defective and tabled rather "
            "than edited into passing, and %d defects the seats declared on their own faces. **THE ADDITIVITY IS MECHANICAL:** after the write the findings document begins "
            "with exactly the bytes it began with and with exactly the bytes of its committed blob; %d lines added, nothing edited, the section present once. **THE ARC AS ONE "
            "STATEMENT, at the grade the acts support:** a question priced UNAFFORDABLE by value on one axis was RESOLVED on another the record already held, at a resolving "
            "power of 63.6 -- and that resolves the two CONVENTIONS, not which of them is correct; the deposit's Li channel and the derived kernel are ONE DISTRIBUTION ON TWO "
            "FAMILIES, measured at the archimedean constituent only, with the trail still OWED; the archimedean instrument has a floor and THE ONE AXIS MOVED DOES NOT EXPLAIN "
            "IT; the room's minimum is BRACKETED at the lowest height charted; and the clause's constituents stand as the stated-clause anchor has them with K8 UNOWNED. **THE "
            "SPECIES MINTED:** a scanner over prose cannot tell use from mention -- a sentence denying a thing contains the thing -- with %d incidents at b316, b317, b345, b346 "
            "and b347's own arm, which found its own search string; its direction FALSE ALARM, NEVER FALSE CLEARANCE, which is why it survived five acts, since a firing arm "
            "gets rewritten and a rewritten arm looks like a passing one; and its cure, arms scoped to code lines or marked mention-regions, NEVER A SOFTENED NEEDLE. **TESTED "
            "FOR MECHANIZABILITY AGAINST A TEST SEALED BEFORE THE ATTEMPT AND FOUND NOT MECHANIZABLE IN THE REGISTRATION GATE** -- the gate reads a registration, which says "
            "what an act will not do, while the defect lives in the checks file that tests that claim afterwards -- **SO IT IS FILED AS A JUDGEMENT RULE AND IS DELIBERATELY NOT "
            "LISTED BESIDE THE MECHANIZED ONES**, and what would mechanize it, a linter over the checks files themselves, is named and not built. Module "
            "modules/2026-09/USE_AND_MENTION.md, committed locally, NOT PUSHED. **THE CENSUS AS A FINDING ABOUT THE RECORD, NOT A GRADE ON IT:** %s registrations gated, %s "
            "would fire, %s clear, and %s of those clear carry neither a numerical threshold nor a multi-arm passage -- **so the record's quiet is mostly the ABSENCE OF STATED "
            "NUMERICAL BARS rather than bars checked and approved** -- and the gate is PROSPECTIVE, binding what is written after it; filed as a work-order for what "
            "registrations state going forward. **THE DESK** carries M-2 under its cap, the object's conditions, the floor's two held axes priceable from b344's printed figures "
            "WITHOUT re-running it, the room's bracketed minimum as the located point of maximum tension, the clause's grade table with K8 unowned, the wave parked, the patent "
            "receipts as the one item with a date -- and **THE FAILURE-MODE PARTITION, A FINITE CLASSIFICATION OF THE WAYS THE MARGIN COULD FAIL OVER THE AIM PLANE'S OWN "
            "COORDINATES, THE METHOD'S EXHAUSTION MOVE AIMED AT THE QUANTIFIER RATHER THAN ITS CONSTITUENTS, NAMED AS A RESEARCH PROPOSAL AND NOT OPENED, WITH THE SENTENCE "
            "THAT NO SUCH PARTITION IS KNOWN TO EXIST.**"
            % (len(F['acts']), F['quotes_failing'], F['grades_failing'], F['corrections'], F['defective'],
               F['seat_defects'], F['lines_added'], len(F['incidents']), c['gated'], c['fire'], c['clear'], c['nothing']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A FOLD RESTATES ITS ACTS AT THEIR OWN GRADES** -- it certifies nothing, and the arc statement it carries is what the nine acts already "
         "hold, said once.",
         "**NO PRINT.** One appended section in FINDINGS.md, purely additive and checked mechanically; one TECHNE module committed LOCALLY and NOT PUSHED; no keystone created "
         "or edited, no owner instrument edited, no deposited text touched.",
         "**NO GRADE MOVED, AND THAT IS CHECKED RATHER THAN ASSERTED:** every grade string in the section was required to appear verbatim in the bank of the act it is "
         "attributed to.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b348 -- THE FOLD, b339 THROUGH b347. ### THE ROW.")
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
    g1 = (all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS)
          and 'NOT OPENED' in ROWS[0][1]
          and 'NOT PUSHED' in ROWS[0][1]
          and 'NOT LISTED BESIDE THE MECHANIZED ONES' in ROWS[0][1]
          and 'CHECKED RATHER THAN ASSERTED' in ROWS[0][4]
          and 'A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, the partition not opened, not pushed, the rule not listed as mechanized, no grade moved : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
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
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
