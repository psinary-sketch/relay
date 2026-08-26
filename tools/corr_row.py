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
"""

import io
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NCELLS = 6
HEADS = ['statement', 'terminal(s)', 'axiom print', 'grade', 'status']


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


def main(argv):
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
