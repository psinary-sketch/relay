# -*- coding: utf-8 -*-
"""corr_row.py -- CORRESPONDENCE ROWS, WRITTEN BY A TOOL (built b194).

### WHY THIS EXISTS. TWICE, IN THE SAME SHAPE:
### b178 -- a bibliography patch written as a `python -c` string inside a double-quoted
###   bash command. ### THE SHELL'S BACKTICKS ATE EVERY CODE-SPAN and the script
###   REPORTED SUCCESS.
### b193 -- a correspondence row written the same way. ### THE TERMINAL NAMES, THE FILE
###   PATH, THE AXIOM LIST AND THE WORD sorryAx ALL VANISHED, and it reported success.
### b158's standing rule already said: write script FILES, not shell strings.
### ### A RULE THAT HAS FAILED TWICE IN THE SAME SHAPE BELONGS IN A TOOL.

### WHAT IT DOES: takes each cell as a separate argv entry -- ### SO NO ROW EVER PASSES
### THROUGH A HAND-QUOTED SHELL STRING -- validates them, and appends the row.
### argv is delivered by the OS as a list; ### THE SHELL NEVER SEES THE CELL BODIES AS
### CODE, ONLY AS DATA.

# ### THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:
# ### (1) ### IT CANNOT STOP A CALLER FROM STILL WRAPPING ITS ARGUMENTS IN A DOUBLE-QUOTED
# ###     SHELL STRING. It removes the need, not the possibility. ### THE HABIT IS THE
# ###     HAZARD AND A TOOL ONLY LOWERS ITS COST.
# ### (2) It checks cell COUNT and EMPTINESS, not cell TRUTH. ### A ROW OF SIX HONEST-LOOKING
# ###     LIES PASSES.
# ### (3) It appends. It does not verify the row's terminals exist or that the axiom print
# ###     quoted matches a build. ### THAT IS THE ACT'S DUTY, NOT THE TOOL'S.

### ### **THE ROW-NUMBER GUARD, ADDED b488 ON RULING (R98).**
### ### **WHY.** ### b485 wrote a row and then crashed, and the guard against a second row under
### the same number was put in ### *that act's own copy* ### -- so two acts later the defect was
### still reachable by any other caller. ### The same week, `ERRATA.md` was found carrying one id
### twice for exactly the same reason. ### **A CURE IN ONE TOOL IS NOT A GUARD**, and (R98) moves
### this one where `errata_append.py` already keeps its own.
### ### **WHAT IT DOES.** ### Before any byte is written it reads the ledger, collects the row
### numbers already in it, and ### **REFUSES A ROW WHOSE NUMBER IS ALREADY THERE.** ### The
### refusal is a return code, not an exception, and the file is not touched.
### ### **WHAT IT DOES NOT DO.** ### (4) ### **IT CHECKS THE NUMBER, NOT THE CONTENT.** ### Two
###     rows under different numbers saying the same thing pass. ### A duplicate number is a clash
###     the ledger cannot resolve by reading; a duplicate claim is an act's duty.
### ### (5) ### **IT DOES NOT ASSIGN NUMBERS.** ### It refuses a taken one and names the next
###     free one in the refusal; choosing is still the caller's.
"""

import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NCELLS = 6
HEADS = ['statement', 'terminal(s)', 'axiom print', 'grade', 'status']
ROWNUM = re.compile(r'^\|\s*(\d+)\s*\|', re.M)


def numbers_in(text):
    """### ### **EVERY ROW NUMBER THE LEDGER ALREADY CARRIES, AS A SET OF ints.**"""
    return set(int(m.group(1)) for m in ROWNUM.finditer((text or '').replace(chr(13), '')))


def write_row(path, cells):
    if not cells:
        # ### THE EMPTY CASE. b167's law: a verdict over an empty scope is not a verdict,
        # ### and a row with no cells is not a row.
        return 2, ["### HARD FAILURE -- NO CELLS GIVEN. An empty row is not a row."]
    if any(not c.strip() for c in cells):
        bad = [i for i, c in enumerate(cells) if not c.strip()]
        return 2, ["### HARD FAILURE -- BLANK CELL(S) at position(s) %s." % bad,
                   "### The ledger's own rule: NO BLANK CELLS."]
    if len(cells) != NCELLS:
        return 2, ["### HARD FAILURE -- %d cells given, %d required." % (len(cells), NCELLS)]
    if not os.path.exists(path):
        return 2, ["### HARD FAILURE -- ledger not found: %s" % path]

    # ### ### **THE ROW-NUMBER GUARD (b488, ruling (R98)). ### IT READS BEFORE IT WRITES.**
    have = numbers_in(io.open(path, encoding='utf-8-sig', errors='replace').read())
    offered = cells[0].strip()
    if re.match(r'^\d+$', offered) and int(offered) in have:
        return 2, ["### ### **REFUSED -- ROW NUMBER %s IS ALREADY IN THE LEDGER."
                   " NOTHING WAS WRITTEN.**" % offered,
                   "### rows already present : %d ; highest : %d ; next free : %d"
                   % (len(have), max(have), max(have) + 1),
                   "### A duplicate number is a clash the ledger cannot resolve by reading.",
                   "### ### **THE TOOL REFUSES A TAKEN NUMBER. IT DOES NOT CHOOSE ONE.**"]

    row = '| ' + ' | '.join(c.strip() for c in cells) + ' |'
    t = io.open(path, encoding='utf-8').read().rstrip()
    t = t + '\n' + row + '\n'
    d = t.encode('utf-8')
    open(path + '.tmp', 'wb').write(d)
    os.replace(path + '.tmp', path)

    # ### READ THE ROW BACK FROM DISK AND COUNT ITS CELLS. ### b193's DEFECT WAS CAUGHT BY
    # ### READING BACK, SO THE TOOL READS BACK.
    last = io.open(path, encoding='utf-8').read().rstrip().split('\n')[-1]
    got = [c for c in last.strip().strip('|').split('|')]
    out = ["  ledger      : %s" % os.path.basename(path),
           "  cells given : %d" % len(cells),
           "  cells on disk after write-back read : %d" % len(got)]
    if len(got) != NCELLS or any(not c.strip() for c in got):
        out.append("  ### HARD FAILURE -- THE ROW ON DISK DOES NOT MATCH WHAT WAS GIVEN.")
        return 1, out
    out.append("  VERDICT     : WRITTEN, verified by read-back")
    out.append("  ### and that means the CELLS SURVIVED. It does not mean they are true.")
    return 0, out


def self_test(tmpdir):
    """### ### **BOTH CONTROLS, ON A FIXTURE -- NEVER ON THE LIVE LEDGER.**
    ### ### **POSITIVE CONTROL: A NUMBER THE FIXTURE ALREADY CARRIES. IT MUST REFUSE.**
    ### ### **NEGATIVE CONTROL: THE NEXT FREE NUMBER. IT MUST ACCEPT.**
    ### A positive control that refuses is safe; ### **A NEGATIVE CONTROL THAT ACCEPTS WRITES A
    ### ROW**, which is exactly why neither runs against `CORRESPONDENCE.md`."""
    lines = []
    p = os.path.join(tmpdir, 'CORRESPONDENCE_fixture.md')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(
        '| # | a | b | c | d | e |\n|:--|:--|:--|:--|:--|:--|\n'
        '| 1 | x | x | x | x | x |\n| 2 | x | x | x | x | x |\n')
    before = io.open(p, 'rb').read()
    cells = ['2', 'a second row under a number the ledger holds', 't', 'p', 'g', 's']
    code_dup, _ = write_row(p, cells)
    unchanged = io.open(p, 'rb').read() == before
    lines.append('      POSITIVE CONTROL -- a TAKEN number  : code %d (must be 2) ; '
                 'file unchanged : %s' % (code_dup, unchanged))
    code_new, _ = write_row(p, ['3', 'a row under the next free number', 't', 'p', 'g', 's'])
    grew = io.open(p, 'rb').read() != before
    lines.append('      NEGATIVE CONTROL -- the NEXT FREE   : code %d (must be 0) ; '
                 'file grew : %s' % (code_new, grew))
    ok = (code_dup == 2 and unchanged and code_new == 0 and grew)
    lines.append('      ### ### **BOTH CONTROLS BEHAVE : %s.**' % ok)
    lines.append('      ### ### **AN ARM THAT CANNOT REFUSE IS NOT A GUARD**, so the refusal is')
    lines.append('      ### exercised before the tool is used on the real ledger.')
    try:
        os.remove(p)
    except Exception:
        pass
    return ok, lines


def main(argv):
    if len(argv) == 1 and argv[0] == '--self-test':
        import tempfile
        good, ls = self_test(tempfile.mkdtemp(prefix='corr_'))
        for l in ls:
            print(l)
        return 0 if good else 2
    if len(argv) < 1:
        print(__doc__)
        return 2
    path, cells = argv[0], argv[1:]
    code, msg = write_row(path, cells)
    print("--- CORRESPONDENCE ROW WRITER (b194) ---")
    for l in msg:
        print(l)
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
