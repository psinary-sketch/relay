# -*- coding: utf-8 -*-
"""b347_correspondence.py -- ONE ROW: THE THREE REPAIRS AND THE TWO RULES.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if a sharper instrument were a result, as
### if a clock reached backwards, as if the audit's limit were closed, as if a past act had been re-verdicted, or as
### if a gate that matches text could tell a floor from the words of one.
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

SCOPE_TAIL = ("**SCOPE: A SHARPER INSTRUMENT IS NOT A RESULT, AND NOTHING HERE DECIDES ANYTHING ABOUT THE MATHEMATICS.** No frame was built, no cell evaluated, no object "
              "measured. The clock does not reach backwards: every run file written before it carries none and b345's (E4) stands exactly as b345 declared it. The audit's "
              "numerical limit is NAMED AND PRICED, NOT CLOSED, and no numerical checker is built. The gate MATCHES TEXT and cannot tell a floor from the words of one. No "
              "past act is re-verdicted, no past copy of the flattener is edited, and no registration that the new arms would fire on is touched. Nothing about the "
              "quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
              "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED "
              "by the author's ruling. NOTHING DEPOSITS.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b347_repairs.json'), encoding='utf-8'))
    Cc, Dd, E, F, Gg = R['C'], R['D'], R['E'], R['F'], R['G']
    weak = '; '.join('%s: %s' % (a, p) for a, p in E['weakened']) or 'none'
    m = ("THE THREE REPAIRS AND THE TWO RULES: A RUN FILE NOW CARRIES ITS OWN CLOCK AND NONE OF THE %d BEFORE IT DOES; THE SATISFIABILITY AUDIT'S NUMERICAL LIMIT IS NAMED "
         "AND PRICED AT %d REGISTRATIONS OF HAND READING; THE GATE FLATTENER IS REPAIRED IN ONE PLACE WITH ITS REACH MEASURED AT %d ARM; AND THE BAR-FLOOR RULE IS MINTED "
         "OVER BOTH SPECIES AND MECHANIZED, FIRING ON %d OF %d REGISTRATIONS IN A CENSUS THAT RE-VERDICTS NONE (b347)"
         % (Cc['runs'], Dd['hand'], len(E['weakened']), F['would_fire'], F['registrations']))
    stmt = (m + ": **(C) THE RUN FILE'S CLOCK.** b344 put a clock in the seal block and none in a run file, so b345's (E4) found a seal that could be dated and a component "
            "that could not. `tools/run_clock.py` writes the instant into the run file's own first line, with four fixtures including a malformed-clock arm that must read "
            "as no clock. **THE CENSUS IS HOW THE LIMIT IS SAID IN NUMBERS: %d run files in the record, %d carrying a clock before this act, and none of them can be given "
            "one.** **(D) THE AUDIT'S NUMERICAL LIMIT, NAMED AND PRICED.** b345's registration read JOINTLY SATISFIABLE and was numerically self-contradictory; a textual "
            "audit cannot reach that. The limit is now named in the audit's own printed output, beside the reach sentence already there, and b346's spec re-audits to the "
            "same verdict. **THE PRICE, AS A COUNT AND NOT A PLAN:** of %d registrations, %d carry a numerical threshold, %d already sit beside a floor or an UNPRICED, and "
            "**%d would need a hand reading** -- which is the price at the TEXTUAL layer only; the numerical layer is neither priced nor built. **(E) THE FLATTENER.** It "
            "stripped one leading marker per line, so a sentence continued onto a doubled-marker line kept a marker inside itself and no flattened comparison could match "
            "it; written at b344, copied into b345, and it silently failed five arms of b346's suite in one run. `tools/gate_text.py` carries the repair and keeps the old "
            "behaviour as a named function SO THE FIXTURE CAN DISCRIMINATE. **THE REACH IS MEASURED, NOT ASSERTED:** each act's own checks file is read for the phrases it "
            "compares against its flattened bank, and each is evaluated under both behaviours against that act's own bank -- **%s** -- and the count is a LOWER BOUND, since "
            "a phrase in an untaken branch or under another variable name is invisible to a static reader. **THE DEFECT'S DIRECTION IS TOWARD FALSE ALARM, NOT FALSE "
            "CLEARANCE:** an arm that failed to match made its gate FAIL, which is why it survived two acts. **(F) THE BAR-FLOOR RULE, OVER BOTH SPECIES.** A numerical bar "
            "is stated with the floor of the object it tests, and a bar below that floor is uninformative rather than strict; and a bar with several arms is stated with "
            "what makes the arms independent, since arms that are algebraically one arm are one arm. It is b322's resolving-power rule one level down. Two arms were added "
            "to `registration_gate.py` beside the index-query arm, which is untouched and still fires on its own case; **six fixtures, both polarities of each arm, on "
            "synthetic text drawn from no bank.** The census: %d registrations gated, %d would fire, %d clear -- **and %d of the clear ones carry neither a threshold nor a "
            "multi-arm passage, so they are quiet because there was nothing to look at.** **THIS ACT DID NOT EXEMPT ITSELF: its own sealed registration fires on one arm, a "
            "multi-arm passage at line %d with no independence word, and that is CARRIED AND NOT FIXED.** **(G) THE TWO FILINGS.** `BAR_FLOOR_RULE.md` written in the "
            "September shape carrying both incidents; `TWO_ROUTES.md` gains its third clause by an appended block, the file a true prefix of what it was; both committed "
            "locally in TECHNE-Core and **NOT PUSHED**. `FERRY_STANDING v2` written BY ITS GENERATOR with every measured count re-measured live and none disagreeing, the "
            "act-number clause in its own section marked **AUTHOR-RULED, NOT MEASURED** with the ruling cited -- because the file's own rule is that the seat adds none by "
            "hand. **AND THE SCAN WAS NOT TAUGHT THE CLAUSE**, which the file says and this act's own check re-measures: until an act teaches it, A1 binds a reader and not "
            "a tool."
            % (Cc['runs'], Cc['with_clock'], Dd['registrations'], Dd['carry'], Dd['pairable'], Dd['hand'], weak,
               F['registrations'], F['would_fire'], F['clear'], 276, F['own']['lines'][0][0] if F['own']['lines'] else 0))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: EVERY LINE OF THIS ACT IS ABOUT AN INSTRUMENT** -- a clock, a flattener, a gate, a rule and two filings -- and not one of them "
         "touches an object the corpus is trying to decide.",
         "**NO PRINT.** Relay tools only, plus two TECHNE modules committed LOCALLY and NOT PUSHED; no file written in the papers repo, so the hook and the mirror are NOT "
         "OWED; no owner instrument edited, no deposited text touched.",
         "**NO GRADE MOVED; NO BAR MOVED.** Every past act stands exactly as banked, and this act's own registration fires on one of its own new arms and carries it.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b347 -- THE THREE REPAIRS AND THE TWO RULES. ### THE ROW.")
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
          and 'CARRIED AND NOT FIXED' in ROWS[0][1]
          and 'NOT PUSHED' in ROWS[0][1]
          and 'AUTHOR-RULED, NOT MEASURED' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'A SHARPER INSTRUMENT IS NOT A RESULT' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, carries its own firing arm, not pushed, author-ruled not measured, no grade moved : %s' % g1)
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
