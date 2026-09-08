# -*- coding: utf-8 -*-
"""b368_desk.py -- ADDITION FOUR: THE DESK'S OWN FRESHNESS. ### THE RULE, AND ONE SWEEP.

### ### **THE RULE:** ### **EVERY DESK ITEM NAMES THE FILE AND DATE AT WHICH IT WAS LAST CONFIRMED, AND
### ### AN ITEM WITHOUT ONE IS RE-VERIFIED BEFORE IT IS ORDERED.**
### ### **ITS INCIDENTS: `b367` AND `b157`** -- a desk item carried from recall while the kernel had
### retired its subject and an act had banked it thirteen days earlier.
### ### **FILED AS A TECHNE MODULE, BESIDE THE TWO ARM SPECIES, COMMITTED LOCALLY, ### NOT PUSHED.**
### ### ### **AND THE SWEEP PRODUCES MARKS, NOT VERDICTS.** ### `UNCONFIRMED` means ### **THIS ACT COULD
### ### NOT FIND THE FILE THAT WOULD SETTLE THE ITEM** -- not that the item is stale. ### **NO ITEM IS
### ### CLOSED BY THIS ACT**, and the order says so in those words.
### ### **AND THE DESK IS NAMED BEFORE IT IS SWEPT:** ### `b360`'s, the one list the fold placed on the
### record, quoted from its own bank by the anchor tool.
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
MODULE = os.path.join(MODDIR, 'DESK_FRESHNESS.md')
FOLD = os.path.join(D, 'b360_the_fold.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE DESK, ITEM BY ITEM, AS `b360` LISTED IT.** ### (item, the file this act looked for, and what
# ### it looked for in it). ### **THE LOOK-UP IS MECHANICAL; THE MARK IS WHAT THE LOOK-UP RETURNED.**
DESK = [
    ('M-2, under b310 cap', 'data/b310_*.txt', 'M-2'),
    ('the object conditions', 'data/b332_*.txt', 'clause'),
    ('the uniformity row U1, four entries and its own refusal', 'data/b366_faces_row_run.txt', 'U1'),
    ('the instrument lane, PARKED under ruling R4', 'data/b3*_registration_*.txt',
     'INSTRUMENT LANE STAYS PARKED'),
    ('the anchored gate arms, available mechanical work', 'data/b363_the_anchored_gate_arms.txt',
     'gate_needle'),
    ('the wave candidate list, typed and not ranked at b324', 'data/b324_*.txt', 'candidate'),
    ('the wave itself, the author own', 'data/b3*_registration_*.txt', 'THE WAVE STAYS PARKED'),
    ('the routed items, each with its owner', 'data/b359_*.txt', 'rout'),
    ('the patent receipts, absent on the mounted volumes', 'data/b3*_the_*.txt', 'patent'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def q(path, hint, span=1):
    n, _l = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    s = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=s,
                equal=(GN.norm(s) == GN.norm(raw)))


def newest_confirming(glob_pat, needle):
    """### **THE FILE THAT CONFIRMS THE ITEM IS STILL OWED, OR NOTHING.** ### The newest banked file
    ### matching the pattern whose text carries the needle; its own mtime date is the confirmation date."""
    import glob as G
    import datetime
    # ### **THIS ACT'S OWN FILES ARE NOT ALLOWED TO CONFIRM THE DESK.** ### The first run marked two
    # ### items confirmed by `b368`'s own registration -- which restates the standing parks because the
    # ### ferry does. ### **A SWEEP THAT READS ITS OWN PAPERWORK CONFIRMS ITSELF**, so `b368_*` is
    # ### excluded and the confirmation has to come from the record this act inherited.
    best = None
    for p in sorted(G.glob(os.path.join(ROOT, glob_pat.replace('/', os.sep)))):
        if os.path.basename(p).startswith('b368_'):
            continue
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        if needle.lower() in txt.lower():
            st = os.path.getmtime(p)
            if best is None or st > best[1]:
                best = (p, st)
    if best is None:
        return None
    return dict(file=os.path.relpath(best[0], ROOT).replace(os.sep, '/'),
                date=datetime.datetime.fromtimestamp(best[1], datetime.timezone.utc).strftime('%Y-%m-%d'))


MODULE_TEXT = '''# DESK_FRESHNESS.md — a desk item names the file and date at which it was last confirmed

**Minted b368 (2026-09-08), from two incidents already in the record.**
**Status: JUDGEMENT RULE with a MECHANIZABLE HALF. The halves are listed apart, deliberately.**

## The rule

**Every desk item names the FILE and the DATE at which it was last confirmed. An item without one is
RE-VERIFIED before it is ordered.**

A desk is a list of what is still owed. It is written once and read many times, and **nothing in it
carries its own age**. An item that was true when it was written stays on the list looking exactly like
an item that is true now.

## The incidents

**b367 (2026-09-07).** A ferry ordered the repair of two scaffold terminals in the exclusion kernel,
described from the navigator's recall as written trivially true. The act read the kernel and found **0
live declarations**: the terminals had been retired, and the kernel's own retirement ledger recorded
it. The premise was not wrong when it was formed; it was **old**.

**b157 (2026-08-25).** The same finding, thirteen days earlier, banked in the programme's own trails
ledger: *"THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED — and re-verifying rather than assuming is
what found it."* **The record already held the correction when the later ferry was written.**

**So the cost was not a wrong belief. It was a right belief with no date on it**, and a second act
spent to re-derive what a first act had already banked.

## Why this is the same species as a stale front document

b367 and b368 found a kernel's `AGENTS.md` exporting **eighteen** theorem names its source does not
declare — every one of them retired. **A document that summarises a source keeps claiming what the
source has dropped, and it drifts in one direction only:** removals are what go unrecorded, because a
removal is the one change nobody has to write down anywhere else.

**A desk is a summary of what is owed. It drifts the same way.**

## The mechanizable half, and its limit

**Mechanizable:** whether an item carries a file and a date at all. That is a shape, and a tool can
demand it.

**Not mechanizable:** whether the named file still confirms the item. That is a read, and the read is
the point — a date that is merely present is a date nobody checked.

**So a tool can enforce the FORM and cannot enforce the TRUTH**, and this module says so rather than
letting a later act trust a green tick.

## What follows

- **When you write a desk item, name the file that establishes it and the date you read that file.**
- **When you order work from a desk item that carries no file and date, re-verify it first** — one
  search, before the registration is written, is cheaper than an act.
- **A mark is not a verdict.** A sweep that cannot find the confirming file marks the item
  `UNCONFIRMED`; that says the sweep failed to find it, not that the item is dead.
- **And no sweep closes an item.** Closing is the author's.

## The scope of this module

It states a rule and names two incidents. **It does not claim the desk is stale**, it prices no
re-verification, and **it closes nothing**. b368 swept the desk once against it and produced marks
only.
'''


def main():
    rec('=' * 100)
    rec("b368 -- ADDITION FOUR: THE DESK'S OWN FRESHNESS. ### THE RULE, AND ONE SWEEP.")
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK, NAMED BEFORE IT IS SWEPT.')
    rec('-' * 100)
    try:
        dq = q(FOLD, 'One list, each item with where it stands and what would move it: `M-2` under', 7)
        rec('    `b360`s fold, line %d -- the one list the fold placed on the record:' % dq['line'])
        rec('    | %s' % dq['quote'][:400])
    except AF.AnchorError as e:
        rec('    ### ### **THE DESK COULD NOT BE LOCATED : %s. ### NOTHING IS SWEPT.**' % str(e)[:90])
        run_clock.write(D, 'b368_desk_notes', LINES)
        return 2

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP. ### **MARKS, NOT VERDICTS. ### NO ITEM IS CLOSED.**')
    rec('-' * 100)
    marks = []
    for item, pat, needle in DESK:
        hit = newest_confirming(pat, needle)
        mark = 'CONFIRMED-BY-FILE' if hit else 'UNCONFIRMED'
        marks.append(dict(item=item, pattern=pat, needle=needle, mark=mark, hit=hit))
        rec('')
        rec('    %-58s %s' % (item[:58], mark))
        if hit:
            rec('        confirming file : `%s`   last written %s' % (hit['file'], hit['date']))
        else:
            rec('        ### **THIS ACT COULD NOT FIND THE FILE THAT WOULD SETTLE IT** -- searched')
            rec('        ### `%s` for `%s`. ### **THAT IS A MARK, NOT A VERDICT.**' % (pat, needle))
    n_conf = sum(1 for m in marks if m['mark'] == 'CONFIRMED-BY-FILE')
    n_unc = len(marks) - n_conf
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CONFIRMED-BY-FILE : %d. ### UNCONFIRMED : %d.**'
        % (len(marks), n_conf, n_unc))
    rec('    ### ### **AND NO ITEM IS CLOSED BY THIS ACT.** ### A mark records what a search returned;')
    rec('    ### closing is the author’s, and this act closes nothing.')
    rec('    ### **AND THE SWEEP’S OWN REACH, STATED:** ### it looks for a banked file whose text')
    rec('    ### carries a needle for the item. ### **A FILE THAT MENTIONS AN ITEM IS NOT A FILE THAT')
    rec('    ### ### CONFIRMS IT**, and this sweep cannot tell the two apart -- which is the module’s own')
    rec('    ### stated limit, met on its first use.')

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE MODULE. ### **LOCAL-ONLY, BESIDE THE TWO ARM SPECIES.**')
    rec('-' * 100)
    if not os.path.isdir(MODDIR):
        rec('  ### ### **NO MODULE DIRECTORY. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b368_desk_notes', LINES)
        return 2
    existed = os.path.exists(MODULE)
    io.open(MODULE, 'w', encoding='utf-8', newline=chr(10)).write(MODULE_TEXT)
    back = io.open(MODULE, encoding='utf-8').read()
    sib = [f for f in ('WRONG_ARM.md', 'DATED_ARM.md') if os.path.exists(os.path.join(MODDIR, f))]
    # ### **THE CLAUSES ARE READ THROUGH `GN.norm`, NOT RAW.** ### The first run of this tool asked for
    # ### `and it closes nothing` as a raw substring and the module says `and **it closes nothing**` --
    # ### **A BOLD RUN INSIDE THE PHRASE**, which is the wrapping species the shared helper exists to
    # ### strip. ### **THE ARM WAS WRONG; THE MODULE WAS RIGHT**, and this comment is the incident.
    nb = GN.norm(back)
    clauses = [('the rule, in its own words', 'RE-VERIFIED before it is ordered'),
               ('it closes nothing', 'and it closes nothing'),
               ('the limit of the mechanizable half', 'cannot enforce the TRUTH')]
    per = [(lab, GN.norm(t) in nb) for lab, t in clauses]
    ok_mod = (back.startswith('# DESK_FRESHNESS.md') and all(v for _l, v in per) and len(sib) == 2)
    rec('    written : %s   (existed before : %s) ; bytes %d'
        % (os.path.relpath(MODULE, TC), existed, len(back.encode('utf-8'))))
    rec('    ### **THE TWO ARM SPECIES ARE BESIDE IT** : %s' % sib)
    for lab, v in per:
        rec('        clause present (read through the marker-stripping norm) -- %-38s : %s' % (lab, v))
    rec('    ### **AND IT STATES ITS OWN MECHANIZABLE HALF AND ITS LIMIT : %s**' % ok_mod)
    subprocess.run(['git', '-C', TC, 'add', os.path.relpath(MODULE, TC).replace(os.sep, '/')],
                   capture_output=True, text=True)
    msg = ('DESK_FRESHNESS.md -- a desk item names the file and date at which it was last confirmed'
           ' (b368).' + chr(10) + chr(10)
           + 'Incidents: b367 and b157. A ferry ordered the repair of terminals a kernel had already'
           + chr(10) + 'retired and an act had banked thirteen days earlier. The premise was not wrong'
           + chr(10) + 'when it was formed; it was OLD.' + chr(10) + chr(10)
           + 'Mechanizable half: whether an item carries a file and a date. Not mechanizable: whether'
           + chr(10) + 'the named file still confirms it. LOCAL ONLY. NOT PUSHED.' + chr(10))
    subprocess.run(['git', '-C', TC, 'commit', '-q', '-m', msg], capture_output=True, text=True)
    head = subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    clean = not subprocess.run(['git', '-C', TC, 'status', '--porcelain'],
                               capture_output=True, text=True).stdout.strip()
    ahead = subprocess.run(['git', '-C', TC, 'rev-list', '--count', 'origin/main..HEAD'],
                           capture_output=True, text=True).stdout.strip()
    mods = sorted(f for f in os.listdir(MODDIR) if f.endswith('.md'))
    rec('    local HEAD after the commit : %s ; working tree clean : %s' % (head, clean))
    rec('    ### ### **COMMITS AHEAD OF `origin/main` : %s ### -- NOT PUSHED.**' % (ahead or '?'))
    rec('    ### modules under %s : %d' % (os.path.relpath(MODDIR, TC), len(mods)))
    rec('=' * 100)

    p = run_clock.write(D, 'b368_desk_notes', LINES)
    io.open(os.path.join(D, 'b368_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(module=os.path.relpath(MODULE, TC).replace(os.sep, '/'), module_ok=bool(ok_mod),
             module_bytes=len(back.encode('utf-8')), siblings=sib, modules_now=len(mods),
             clauses={lab: v for lab, v in per},
             existed_before=existed, techne_head=head, techne_clean=clean,
             commits_ahead_of_origin=ahead, pushed=False,
             desk_quote=dq, items=len(marks), confirmed=n_conf, unconfirmed=n_unc,
             marks=marks, items_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok_mod else 1


if __name__ == '__main__':
    sys.exit(main())
