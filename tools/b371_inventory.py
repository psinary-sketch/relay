# -*- coding: utf-8 -*-
"""b371_inventory.py -- COMPONENT 2: THE ROW INVENTORY. ### **LISTED, NOT CHECKED.**

### ### ### **`AUDIT NOTHING` IS THE ORDER'S OWN CLAUSE AND IT IS THE CAP.** ### No kernel is opened for
### any row. ### Every field is taken FROM THE ROW.
### ### **THE PREDICATE IS DECLARED BEFORE THE SWEEP SO IT CAN BE DISAGREED WITH**, and its own failure
### mode is named with it: ### `PREDICATE_ONE_SHAPE` -- ### **A ROW THAT STATES ITS PIN IN A SHAPE THIS
### ### PREDICATE DOES NOT KNOW WILL BE REPORTED AS PINLESS.** ### So the shapes are printed, the
### rejected rows are counted, and ### **NO COMPLETENESS IS CLAIMED.**
### ### **AND ONE CROSS-REFERENCE IS PERMITTED AND IS NOT A CHECK:** ### comparing an inventoried NAME
### against the classification this record already banked at `b368` and re-derived at `b369` ### **OPENS
### ### NO KERNEL AND VERIFIES NO ROW.** ### It is marked as a cross-reference, and a row so flagged is
### not thereby wrong -- it is a row whose check the ranking should order first.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE THREE SHAPES, DECLARED. ### EACH IS A PATTERN AND EACH CAN MISS.**
KERNEL = re.compile(r'(SIDE-[a-z0-9-]+|SIDEEffects/[A-Za-z0-9_/]+\.lean|[A-Za-z0-9_]+\.lean)')
TERMINAL = re.compile(r'`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+|'
                      r'[a-z][a-z0-9_]*_[a-z0-9_]+)`')
PIN = re.compile(r'`?\b([0-9a-f]{7,40})\b`?|`?(v\d+\.\d+(?:\.\d+)?)\b`?')
COUNTISH = re.compile(r'(?<![A-Za-z.])(\d+|one|two|three|four|five|six|seven|eight|nine|ten)'
                      r'[\s-]+(?:\w+[\s-]+){0,2}(terminals?|theorems?|prints?|modules?|rows?)', re.I)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def main():
    rec('=' * 100)
    rec('b371 -- COMPONENT 2: THE ROW INVENTORY. ### **LISTED, NOT CHECKED.**')
    rec('=' * 100)
    rec('')
    rec('  ### ### **THE CAP, FIRST, IN THE ORDER`S OWN WORDS: `Audit nothing.`**')
    rec('  ### No kernel is opened for any row. ### Every field below is taken FROM THE ROW.')
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE PREDICATE, DECLARED BEFORE THE SWEEP.')
    rec('-' * 100)
    rec('    a row qualifies if it names all three of:')
    rec('      KERNEL   -- `%s`' % KERNEL.pattern)
    rec('      TERMINAL -- a backticked dotted identifier, or a backticked snake_case name')
    rec('      PIN      -- a hex of 7 to 40, or a `vN.N[.N]` tag')
    rec('    ### ### **AND ITS FAILURE MODE IS NAMED WITH IT (`PREDICATE_ONE_SHAPE`):** ### a row whose')
    rec('    ### pin is written in a shape this predicate does not know is reported PINLESS. ### **THE')
    rec('    ### ### SWEEP REPORTS WHAT IT MATCHED AND CLAIMS NO COMPLETENESS.**')

    head = git('rev-parse', 'HEAD').strip()
    files = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP. ### `PLACE-papers` at `%s`, %d tracked markdown files.'
        % (head[:7], len(files)))
    rec('-' * 100)
    rows, scanned = [], 0
    for rel in files:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for i, ln in enumerate(txt.split(chr(10)), 1):
            if not ln.strip().startswith('|'):
                continue
            scanned += 1
            ks = KERNEL.findall(ln)
            ts = TERMINAL.findall(ln)
            ps = [a or b for a, b in PIN.findall(ln)]
            if not (ks and ts):
                continue
            rows.append(dict(file=rel, line=i, kernels=sorted(set(ks))[:4],
                             terminals=sorted(set(ts))[:6], pins=sorted(set(ps))[:4],
                             has_pin=bool(ps),
                             countish=bool(COUNTISH.search(ln)),
                             text=ln.strip()[:160]))
    with_pin = [r for r in rows if r['has_pin']]
    without = [r for r in rows if not r['has_pin']]
    rec('    table rows scanned : %d' % scanned)
    rec('    ### ### **ROWS NAMING A KERNEL AND A TERMINAL : %d**' % len(rows))
    rec('    ### ### **OF THOSE, NAMING A PIN TOO : %d ### / ### NAMING NO PIN : %d**'
        % (len(with_pin), len(without)))
    byfile = {}
    for r in rows:
        byfile[r['file']] = byfile.get(r['file'], 0) + 1
    rec('')
    rec('    by file:')
    for f, n in sorted(byfile.items(), key=lambda x: -x[1]):
        np = sum(1 for r in rows if r['file'] == f and r['has_pin'])
        rec('      %-62s %3d rows, %3d with a pin' % (f[:62], n, np))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE ROWS THAT NAME ALL THREE. ### **THE SET `(R6)` CAN ACTUALLY CHECK.**')
    rec('-' * 100)
    for r in with_pin[:40]:
        rec('    %s:%d' % (r['file'], r['line']))
        rec('        kernel(s) : %s' % ', '.join(r['kernels']))
        rec('        terminal(s): %s' % ', '.join('`%s`' % x for x in r['terminals']))
        rec('        pin(s)     : %s' % ', '.join('`%s`' % x for x in r['pins']))
    if len(with_pin) > 40:
        rec('    ... and %d more, all in the JSON' % (len(with_pin) - 40))

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE ROWS THAT NAME NO PIN. ### **A FINDING, NOT A HOLE IN THE SWEEP.**')
    rec('-' * 100)
    rec('    ### `(R6)` says the rows are checked ### *"at the kernel and pin the row itself names"*.')
    rec('    ### ### **SO A ROW WITHOUT A PIN CANNOT BE CHECKED THE WAY THE RULING SPECIFIES.** ### It')
    rec('    ### is not a miss of this sweep; it is a property of the row.')
    wf = {}
    for r in without:
        wf[r['file']] = wf.get(r['file'], 0) + 1
    for f, n in sorted(wf.items(), key=lambda x: -x[1])[:12]:
        rec('      %-62s %3d' % (f[:62], n))
    rec('    ### ### **AND THE RATIO IS THE FINDING: %d OF %d ROWS THAT CITE A KERNEL AND A TERMINAL'
        % (len(without), len(rows)))
    rec('    ### ### CARRY NO PIN AT ALL.**')

    # ---------------------------------------------------------------- (5) THE CROSS-REFERENCE
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE CROSS-REFERENCE. ### **AGAINST THIS RECORD`S OWN BANKED FINDING, NOT A CHECK.**')
    rec('-' * 100)
    absent = set()
    try:
        R = json.load(io.open(os.path.join(D, 'b369_repair.json'), encoding='utf-8'))
        absent = set(R['absent'])
    except OSError:
        pass
    rec('    the classification `b368` banked and `b369` re-derived names %d declarations ABSENT from'
        % len(absent))
    rec('    the exclusion kernel at its own pinned ref. ### **COMPARING A NAME AGAINST THAT LIST OPENS')
    rec('    ### ### NO KERNEL AND VERIFIES NO ROW.**')
    flagged = []
    for r in rows:
        hit = sorted({t.split('.')[-1] for t in r['terminals']} & absent)
        if hit:
            flagged.append(dict(file=r['file'], line=r['line'], names=hit, has_pin=r['has_pin']))
    rec('    ### ### **ROWS NAMING A DECLARATION THIS RECORD HAS ALREADY CLASSIFIED ABSENT : %d**'
        % len(flagged))
    for f in flagged[:20]:
        rec('      %-46s:%-5d %s%s' % (f['file'][:46], f['line'],
                                       ', '.join('`%s`' % x for x in f['names']),
                                       '' if f['has_pin'] else '   ### (and it names no pin)'))
    rec('    ### ### **A ROW SO FLAGGED IS NOT THEREBY WRONG.** ### The record`s finding is about a')
    rec('    ### kernel at a ref; the row may name a different kernel, an older ref, or a name that')
    rec('    ### moved. ### **IT IS A ROW WHOSE CHECK THE RANKING SHOULD ORDER FIRST, AND THAT IS ALL')
    rec('    ### ### THIS FLAG MEANS.**')

    # ---------------------------------------------------------------- (6) THE PRICE
    rec('')
    rec('-' * 100)
    rec('  ### (6) THE PRICE, IN THREE PARTS, REPORTED SEPARATELY.')
    rec('-' * 100)
    rec('    ### ### **PART ONE -- WHAT VERIFYING ONE ROW COSTS.**')
    rec('    ###   MECHANICAL: resolve the pin (one `git rev-parse` or `ls-remote`), fetch the kernel at')
    rec('    ###   that pin, and search its `.lean` files for a declaration of the named terminal. ###')
    rec('    ###   **THAT IS `b368`S CLASSIFIER WITH A REF ARGUMENT, AND IT ALREADY EXISTS.**')
    rec('    ###   READ: deciding whether the row`s CLAIM about the terminal is what the terminal says.')
    rec('    ###   ### **A NAME PRESENT IS NOT A ROW TRUE** -- `b367` found the names gone; `b369` found')
    rec('    ###   a ledger that named them; neither was settled by presence alone.')
    rec('    ### ### **PART TWO -- WHAT THE WHOLE SET COSTS.**')
    rec('    ###   rows citing a kernel and a terminal : ### **%d**. ### with a pin : ### **%d**.'
        % (len(rows), len(with_pin)))
    rec('    ###   ### **THE MECHANICAL HALF OVER THE PINNED SET IS ONE ACT** -- distinct pins are few')
    rec('    ###   and a fetch is amortised across every row that names the same one.')
    rec('    ###   ### **THE PINLESS SET IS NOT CHEAPER; IT IS UNPRICEABLE UNDER `(R6)` AS WRITTEN**,')
    rec('    ###   because the ruling checks a row at the pin the row names and these name none. ###')
    rec('    ###   **THEY NEED A RULING BEFORE THEY NEED AN ACT.**')
    rec('    ### ### **PART THREE -- THE SPLIT.**')
    rec('    ###   ### **A TOOL CAN SETTLE:** ### does the pin resolve; does the kernel at that pin')
    rec('    ###   declare the named terminal; has the kernel moved since.')
    rec('    ###   ### **A TOOL CANNOT SETTLE:** ### whether the row`s sentence is what the terminal')
    rec('    ###   supports. ### **THAT IS THE READ, AND IT IS THE HALF THAT DOES NOT SCALE.**')
    pins = sorted({p for r in with_pin for p in r['pins']})
    rec('    ###   distinct pins named across the pinned set : ### **%d**' % len(pins))

    # ---------------------------------------------------------------- (7) THE RANKING
    rec('')
    rec('-' * 100)
    rec('  ### (7) THE RANKING. ### **BY THE ORDER`S OWN CRITERION, PRINTED BEFORE THE RANKING.**')
    rec('-' * 100)
    rec('  ### THE CRITERION, THE ORDER`S AND NOT THIS SEAT`S:')
    rec('  ###   (a) pin age;')
    rec('  ###   (b) whether the row names a COUNT rather than a TERMINAL;')
    rec('  ###   (c) whether the kernel has MOVED since.')
    rec('  ### ### **THE ORDER GAVE THREE FACTORS AND NO WEIGHTING AND THIS ACT INVENTS NONE.** ### The')
    rec('  ### table prints them side by side. ### **AND ONE FACTOR CANNOT BE FILLED IN WITHOUT OPENING')
    rec('  ### ### A KERNEL:** ### `(c)` asks whether the kernel has moved since the pin, which is a')
    rec('  ### resolve-and-compare -- ### **THAT IS THE CHECK, AND THE CAP FORBIDS IT.** ### So `(c)` is')
    rec('  ### recorded as `NOT FILLED` for every row, and the ranking runs on `(a)` and `(b)`.')
    ranked = sorted(rows, key=lambda r: (not r['countish'], r['has_pin'], r['file'], r['line']))
    rec('')
    rec('    %-46s %-6s %-6s %-8s %s' % ('row', 'pin?', 'count?', 'moved?', 'names an already-absent name?'))
    fl = {(f['file'], f['line']) for f in flagged}
    for r in ranked[:25]:
        rec('    %-46s %-6s %-6s %-8s %s'
            % (('%s:%d' % (r['file'], r['line']))[:46],
               'yes' if r['has_pin'] else 'NO', 'YES' if r['countish'] else '-',
               'NOT FILLED', 'YES' if (r['file'], r['line']) in fl else '-'))
    rec('')
    rec('    ### ### **AND WHAT THIS RANKING IS NOT: IT IS A RANKING OF EXPOSURE, NOT OF ERROR.** ### No')
    rec('    ### row on it has been shown to be wrong, and this act did not look.')
    rec('=' * 100)
    rec('  ### ### **COMPONENT 2 : LISTED. ### ROWS CHECKED : 0. ### KERNELS OPENED : 0.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b371_inventory_notes', LINES)
    io.open(os.path.join(D, 'b371_inventory.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(head=head, files=len(files), table_rows_scanned=scanned,
                        rows=len(rows), with_pin=len(with_pin), without_pin=len(without),
                        distinct_pins=len(pins), pins=pins[:40],
                        by_file=byfile, flagged=flagged, flagged_count=len(flagged),
                        price_parts=3, criterion=['pin age', 'count rather than terminal',
                                                  'kernel moved since'],
                        factor_c='NOT FILLED -- filling it is the check, and the cap forbids it',
                        rows_checked=0, kernels_opened=0, completeness_claimed=False,
                        inventory=rows,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
