# -*- coding: utf-8 -*-
"""b366_mint.py -- ADDITION THREE: THE DATED ARM, MINTED, AND KEPT APART FROM THE WRONG ARM.

### ### **TWO SPECIES, TWO MODULES, AND THE SEPARATION IS THE POINT.**
###   ### **THE WRONG ARM** (`b365`'s `WRONG_ARM.md`): ### wrong the day it was written; its cure is a
###     SECOND READER; ### **NO MECHANIZABLE HALF.**
###   ### **THE DATED ARM** (this module): ### right the day it was written; its cure is ### **A DECISION
###     ### ABOUT WHAT A SUITE IS FOR** -- and `b366`'s `(R2)` is that decision, quoted here as its
###     resolution.
### ### **A RECORD THAT COLLAPSED THEM WOULD LOOK FOR A SECOND READER WHERE A RULING WAS NEEDED, OR WAIT
### ### FOR A RULING WHERE ONLY A READER WILL DO.**
### ### **`b364`'s INCIDENT IS THE MODULE'S EVIDENCE**, quoted at `b364`'s own bank by the anchor tool.
### ### **FILED UNDER `modules/2026-09`, COMMITTED LOCALLY, ### NOT PUSHED**, as every module since
### `b330`.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODDIR = os.path.join(TC, 'modules', '2026-09')
MODULE = os.path.join(MODDIR, 'DATED_ARM.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


B364 = d('b364_the_copy_that_did_not_reproduce.txt')
B365 = d('b365_the_owed_read_paid.txt')
FERRY = d('b366_ferry_2026-09-07.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def quote(path, hint, span=1):
    n, _l = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    q = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=q,
                equal=(GN.norm(q) == GN.norm(raw)))


QUOTES = [
    ('SPECIES', B364, 'AND THE SPECIES IS NAMED: A DATED ARM', 1),
    ('OLD', B364, 'IT DOES NOT BECOME WRONG. ### IT BECOMES OLD', 1),
    ('HALVES', B364, 'WHAT THE ARM WAS CERTIFYING -- TWO THINGS, AND ONLY ONE OF THEM HAS FAILED', 1),
    ('CHOICE', B364, 'DOES NOT DECIDE IT EITHER -- IT NAMES THE CHOICE', 1),
    ('R2A', FERRY, '(R2) WHAT A GATE SUITE IS FOR, split by predicate. An arm', 3),
    ('R2B', FERRY, 'the living record is a MOMENT CERTIFICATE unless it is written', 3),
    ('OTHER', B365, 'ITS ONLY CURE IS A SECOND READER.**', 1),
]


def module_text(Q, S):
    return '''# DATED_ARM.md — an arm that was right when it was written and is old now

**Minted b366 (2026-09-07), from one confirmed incident and one author's ruling.**
**Status: JUDGEMENT RULE WITH A RESOLUTION. The resolution is a RULING, not a tool.**

## The species

**An arm whose pass condition is a literal in a frozen file, compared against a quantity recomputed at
every run, is DATED BY CONSTRUCTION.** It does not become wrong; it becomes old, and the moment of its
expiry is set by the next act that moves a line.

In the words of the act that diagnosed it — `%s`, line %d:

> %s

and, line %d:

> %s

## Why it is not the wrong arm

`WRONG_ARM.md` (b365) names the other species: an arm whose predicate tests something other than what
its label says. **The two are opposites in the one way that matters for a cure.**

| | wrong arm | dated arm |
|:--|:--|:--|
| when it was wrong | **the day it was written** | **it was right that day** |
| what is wrong | the QUESTION | the WRITING |
| how it fails | quietly, forever | loudly, later |
| the cure | **a second reader** | **a decision about what a suite is for** |
| mechanizable | **no** | **the shape is; the classification is not** |

The wrong-arm module says its cure — `%s`, line %d:

> %s

**A record that collapsed the two would look for a second reader where a ruling was needed, or wait
for a ruling where only a reader will do.**

## The incident

b363's control ran six banked gate suites as copies; five reproduced their own act's verdict and
b357's did not. b364 ran b357's suite **at its own location, unedited**, and found the same failure —
**so the copy was innocent** and the arm fails wherever it runs.

And b364 found the arm certifies two things, of which only one has failed — `%s`, line %d:

> %s

**(a) that every classified row is still findable at its ledger by the row's own TEXT** — which held
at every row; and **(b) that any row whose LINE NUMBER moved is declared in the act's own bank with
both numbers** — which cannot hold and cannot be made to, because it compares a number computed now
against a literal in an append-only file that may never be edited.

b364 named the choice and refused to make it — `%s`, line %d:

> %s

## The resolution

**The choice was the author's and the author made it.** b366 carries the ruling — `%s`, lines %d–%d:

> %s

> %s

**So the species has a resolution and it is a RULING, not a tool.** An arm testing the act's own
artifacts is a STANDING CHECK and must reproduce; an arm testing the living record is a moment
certificate **unless it is written by CONTENT rather than by ADDRESS**.

## What the ruling makes possible, and what it does not

**IT MAKES THE REWRITE POSSIBLE.** `relay/tools/gate_content.py` carries it as one substitution:

    BEFORE:  io.open(p).read().splitlines()[rec['line'] - 1]
    AFTER :  gate_content.line_by_content(p, rec['text'])

with fixtures in both polarities — on an unmoved file the two agree; **on a moved file the address
form silently reads a different line and the content form finds the right one at its new number**;
and when the text is genuinely gone the content form **raises rather than going quiet**, because a
rewrite that only ever quietened arms would be a softener (b348).

**IT DOES NOT MAKE THE REWRITE ALWAYS AVAILABLE.** An arm whose record banked a line number and no
text has nothing to look the content up BY. b366's sweep found exactly that case: of the dated arms
in the record, **not all are one substitution from standing, and the ones that are not are not harder
to write — they are MISSING THEIR CONTENT.**

**AND IT DOES NOT REACH BACKWARD.** The ruling is prospective. No past suite is rewritten and no past
verdict is withdrawn.

## The measurement, so the species is not inflated

b366 swept every gate suite in the relay repository: **%d suites, %d arms registered by their own
suites, %d dated.** The detector's net flagged %d lines; %d of those were not address predicates at
all, and %d was address-shaped against an act's own frozen artifact — **which is STANDING, and is the
case that shows the classification cannot be left to a detector.**

**THE SPECIES IS REAL, IT IS CONFIRMED, AND IT IS NOT A CLASS THIS RECORD IS RIDDLED WITH.**

## What follows

- **Write arms by content.** A predicate asking whether a file contains a sentence outlives the file's
  formatting; one asking whether a row sits at a number does not.
- **Bank the content, not only the address.** A record that stores a line number without the text it
  found there has made the rewrite impossible for whoever comes next.
- **A failing banked suite is evidence about the arm's KIND before it is evidence about the work.**
  Classify first: standing arms that fail are findings; dated arms that fail are drift.
- **And do not read this module as a repair order.** It states a species and a ruling. **No arm in the
  record is cured by it, and b366 cured none.**
''' % (
        Q['SPECIES']['file'], Q['SPECIES']['line'], Q['SPECIES']['quote'],
        Q['OLD']['line'], Q['OLD']['quote'],
        Q['OTHER']['file'], Q['OTHER']['line'], Q['OTHER']['quote'],
        Q['HALVES']['file'], Q['HALVES']['line'], Q['HALVES']['quote'],
        Q['CHOICE']['file'], Q['CHOICE']['line'], Q['CHOICE']['quote'],
        Q['R2A']['file'], Q['R2A']['line'], Q['R2B']['line'] + Q['R2B']['span'] - 1,
        Q['R2A']['quote'], Q['R2B']['quote'],
        S['suites'], S['arms'], S['dated'], S['flagged'], S['not_address'], S['standing'],
    )


def main():
    rec('=' * 100)
    rec('b366 -- ADDITION THREE: THE DATED ARM, MINTED, AND KEPT APART FROM THE WRONG ARM.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE QUOTATIONS, FROM THE ACTS AND THE ORDER THAT CARRY THEM.')
    rec('-' * 100)
    Q = {}
    for tag, path, hint, span in QUOTES:
        try:
            Q[tag] = quote(path, hint, span)
        except AF.AnchorError as e:
            rec('  ### ### **NO ANCHOR : %s** -- %s' % (tag, str(e).replace(chr(10), ' | ')[:130]))
            run_clock.write(D, 'b366_mint_notes', LINES)
            return 2
        rec('    [%-8s] %-38s line %-6d equal under the normaliser : %s'
            % (tag, Q[tag]['file'], Q[tag]['line'], Q[tag]['equal']))
        rec('        | %s' % Q[tag]['quote'][:150])
    if not all(x['equal'] for x in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b366_mint_notes', LINES)
        return 3

    S = json.load(io.open(d('b366_sweep.json'), encoding='utf-8'))

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE MODULE. ### **LOCAL-ONLY. ### ITS RESOLUTION IS A RULING, NOT A TOOL.**')
    rec('-' * 100)
    if not os.path.isdir(MODDIR):
        rec('  ### ### **NO MODULE DIRECTORY AT %s. ### NOTHING IS WRITTEN.**' % MODDIR)
        run_clock.write(D, 'b366_mint_notes', LINES)
        return 2
    existed = os.path.exists(MODULE)
    body = module_text(Q, S)
    io.open(MODULE, 'w', encoding='utf-8', newline=chr(10)).write(body + chr(10))
    back = io.open(MODULE, encoding='utf-8').read()
    other = os.path.join(MODDIR, 'WRONG_ARM.md')
    ok_mod = (back.startswith('# DATED_ARM.md')
              and 'it was right that day' in back
              and 'a decision about what a suite is for' in back.lower()
              and 'WRONG_ARM.md' in back
              and 'and b366 cured none' in back
              and os.path.exists(other))
    rec('    written : %s   (existed before : %s)' % (os.path.relpath(MODULE, TC), existed))
    rec('    bytes : %d' % len(back.encode('utf-8')))
    rec('    ### **AND THE OTHER SPECIES IS BESIDE IT, NOT INSIDE IT** : %s (%s)'
        % (os.path.exists(other), os.path.relpath(other, TC)))
    rec('    ### **THE MODULE SAYS ITS RESOLUTION IS A RULING AND THAT NO ARM WAS CURED : %s**' % ok_mod)
    mods = sorted(f for f in os.listdir(MODDIR) if f.endswith('.md'))
    rec('    ### modules under %s : %d' % (os.path.relpath(MODDIR, TC), len(mods)))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE COMMIT. ### **LOCAL ONLY. ### NOT PUSHED, AS EVERY MODULE SINCE b330.**')
    rec('-' * 100)
    subprocess.run(['git', '-C', TC, 'add', os.path.relpath(MODULE, TC).replace(os.sep, '/')],
                   capture_output=True, text=True)
    msg = ('DATED_ARM.md -- an arm that was right when it was written and is old now (b366).' + chr(10)
           + chr(10)
           + "A JUDGEMENT RULE WITH A RESOLUTION, and the resolution is the author's ruling (R2), not a"
           + chr(10) + 'tool. Kept apart from WRONG_ARM.md: one was wrong the day it was written and its'
           + chr(10) + 'cure is a second reader; the other was right that day and its cure is a decision'
           + chr(10) + 'about what a suite is for.' + chr(10)
           + chr(10) + 'LOCAL ONLY. NOT PUSHED.' + chr(10))
    subprocess.run(['git', '-C', TC, 'commit', '-q', '-m', msg], capture_output=True, text=True)
    head = subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    st = subprocess.run(['git', '-C', TC, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout.strip()
    ahead = subprocess.run(['git', '-C', TC, 'rev-list', '--count', 'origin/main..HEAD'],
                           capture_output=True, text=True).stdout.strip()
    rec('    local HEAD after the commit : %s' % head)
    rec('    working tree clean : %s' % (not st))
    rec('    ### ### **COMMITS AHEAD OF `origin/main` : %s** ### -- TECHNE-Core is private until the'
        % (ahead or '?'))
    rec('    ### provisionals, and this act does not change that.')
    rec('    ### **NOTHING WAS PUSHED BY THIS TOOL. ### IT RUNS NO `git push`.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b366_mint_notes', LINES)
    io.open(d('b366_mint.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(module=os.path.relpath(MODULE, TC).replace(os.sep, '/'),
             module_bytes=len(back.encode('utf-8')), module_ok=bool(ok_mod),
             other_species_module='modules/2026-09/WRONG_ARM.md', other_exists=os.path.exists(other),
             modules_now=len(mods), existed_before=existed,
             quotes={k: dict(file=v['file'], line=v['line'], equal=v['equal'], quote=v['quote'])
                     for k, v in Q.items()},
             techne_head=head, techne_clean=(not st), commits_ahead_of_origin=ahead, pushed=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok_mod else 1


if __name__ == '__main__':
    sys.exit(main())
