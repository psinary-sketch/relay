# -*- coding: utf-8 -*-
"""b342_correspondence.py -- ONE ROW: THE TWO RULES AS MODULES, A FILING; COMMITTED LOCALLY IN TECHNE-Core, NOT PUSHED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's records, never typed. ### **THE HAZARD:** a row that reads as if a module conferred a grade, or as if TECHNE
### were published.
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

SCOPE_TAIL = ("**SCOPE: A FILING -- TWO METHOD MODULES, PRIVATE, LOCAL, NOT PUSHED; THEY STATE THE GRADE THEIR OWNING ACTS CARRY AND CONFER NONE; THE FOLD'S LINES "
              "UNTOUCHED.** Nothing about the quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. "
              "The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands "
              "exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    J = json.load(io.open(os.path.join(D, 'b342_modules.json'), encoding='utf-8'))
    m = "THE TWO RULES AS TECHNE MODULES, AS THE EXECUTOR'S DRAFT STATES THEM -- LIKE_FOR_LIKE.md AND SIGN_RULE.md WITH THE b328 PHASE REFINEMENT CARRIED, COMMITTED LOCALLY AT %s AND NOT PUSHED; THE FOLD'S LORE RE-TYPED FROM TOOL TO MODULE BY AN APPENDED BLOCK (b342, leg 4 of the sortie b339-b343)" % J['committed']
    return [
        (m,
         m + ": the draft banked verbatim from the session transcript (relay data/b342_executor_draft_2026-09-06.txt) and quoted; the like-for-like rule (a "
         "comparator is named with the function it was computed for; a bar sealed against a banked table names the table's function; a mismatch is refused) and "
         "the sign rule (a threshold rule is stated with its sign condition; a phase past the threshold is not a negative term), each a claim-shaped method "
         "module under modules/2026-09 in the September modules' shape with its incident quoted from b333, b334 and b328 at their lines; the sign-rule module "
         "carrying S_4 = 4 (the modulus of G squared) cos 2 phi, negative exactly when 45 deg < the phase's modulus < 135 deg, as b328 derived and b336 filed; "
         "the index appended by one block; every existing module file hashed before and after and byte-identical (%d files; changed %s; added %s); TECHNE-Core's "
         "remote read before and after at %s, EQUAL, NOT PUSHED; the working tree clean, %s commits ahead of origin. FINDINGS gains one appended block naming the "
         "two TOOL-typed lore lines and the modules that now carry them, the fold's lines untouched."
         % (J['files_before'], J['changed'], J['added'], J['remote_after'], J['ahead']),
         "**NO TERMINAL, AND THE REASON: A FILING** -- two method drafts and a re-typing; nothing about the mathematics is decided.",
         "**NO PRINT.** TECHNE-Core private, local, not pushed; FINDINGS appended, not edited; no owner file touched.",
         "**NO GRADE MOVED; THE MODULES BIND NOTHING.** Each states the grade its owning act carries and confers none, the index's own standing condition.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b342 -- THE TWO RULES AS MODULES. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'NOT PUSHED' in ROWS[0][1] and 'THE MODULES BIND NOTHING' in ROWS[0][4] and 'CONFER NONE' in ROWS[0][5]
    print('  the row says NO TERMINAL with the reason, not pushed, the modules bind nothing, confer none : %s' % g1)
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
    tails = back.rstrip(chr(10)).split(chr(10))[-1:]
    cells = [G.split_cells(t) for t in tails]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
