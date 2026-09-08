# -*- coding: utf-8 -*-
"""b373_desk.py -- THE DESK, SWEPT UNDER `(R7)`.

### ### **A CLOSURE WITHOUT A KILLING FILE IS AN OPINION.** ### Every closure names a banked file, that
### file is checked to EXIST and to CARRY the sentence claimed for it, and its date is the file's own.
### ### ### **AND THE KILLING FILE IS RESOLVED BY ITS RECORDED CLOCK, NEVER BY ITS NAME** (`b358`):
### `run_clock` numbers repeats, so a stem names several files and ### **THE ONE THAT RAN FIRST IS NOT
### ### THE ONE THAT DID THE WORK.**
### ### **AND THE SWEEP MAY NOT CONFIRM AN ITEM FROM THIS ACT'S OWN PAPERWORK UNNOTICED** (`b368`'s
### defect): a closure whose killing file belongs to this act is ALLOWED -- this act did the killing --
### ### **AND IS FLAGGED**, so no reader mistakes it for a confirmation from the record.
"""
import datetime
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
ACT = 'b373'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (item, disposition, killing-file STEM, the sentence that file must carry, why)
DESK = [
    ('M-2, under b310 cap', 'STAND', None, None,
     'the aggregation is still SPECIFIED-NOT-STATED and b310 cap still governs; no act has stated it'),
    ("the object's conditions", 'STAND', None, None,
     "the conditions are the object's and none has been discharged by this span"),
    ('the uniformity row U1, four entries and its own refusal', 'STAND', None, None,
     "b361 wrote an UPDATE BLOCK on the row; the row's own refusal stands and the entries are "
     'unchanged'),
    ('the instrument lane, PARKED under ruling R4', 'STAND', None, None,
     "PARKED by the author's ruling; only the author unparks it"),
    ('the wave candidate list, typed and not ranked at b324', 'STAND', None, None,
     "typed and not ranked; ranking is the author's and no act has ranked it"),
    ("the wave itself, the author's own", 'STAND', None, None,
     "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', None, None,
     'each still carries its owner and none has been opened'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', None, None,
     "ABSENT on the mounted volumes and UNCONFIRMED on this seat's record; the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', None, None,
     'b369 repaired the LIST and left the count claim above it untouched; no act has been sent to it '
     'since, and this act was sent to a different kernel'),

    ("the retirement ledger's own lacunae", 'STAND', None, None,
     "b369 filed them under (R5) and b372 found more in a DIFFERENT kernel's ledger. ### **FILED, "
     'NOT INVENTED, AND NOT REPAIRED**, and this act was not sent to them'),

    # ---- WHAT THIS ACT WAS SENT TO, AND WHAT IT DID ABOUT EACH ---------------------------------------
    ('the pinless rows, awaiting a ruling on whether pins are added', 'CLOSE', 'b373_pins_notes',
     'THE PRICE FITS ONE ACT.',
     "the item's occasion was that `(R8)` made the addition of pins A SEPARATE RULING, PRICED AND NOT "
     'ATTEMPTED, so the item stood waiting for one. ### **`(R9)` IS THAT RULING AND THIS ACT EXECUTED '
     'IT AS FAR AS ITS OWN SOURCING RULE ALLOWS.** ### The occasion -- an unmade ruling -- is gone. '
     '### **WHAT THE EXECUTION FOUND IS A NEW ITEM AND IS RECORDED AS ONE, NOT AS THIS ONE '
     'SURVIVING**, because an item that changes its meaning while keeping its name is a desk that '
     'never closes anything'),
    ("the rows that cite at a ref nobody can name", 'STAND', None, None,
     "NEW at b373 and it is not the item above renamed: `(R9)`'s sourcing rule was executed and the "
     'chain closed for almost none of the set. ### **THE PAPERS ARE OLDER THAN THE INSTRUMENTS** -- '
     'most rows were introduced by commits whose subject names no act, and most acts that ARE named '
     'predate the pins instrument. ### **THE CURE IS NOT MORE SEARCHING**, and what it is belongs to '
     'the author'),
    ('the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'NEW at b373: rows asserting a grade against a retired or absent declaration, listed with their '
     'carriers and ROUTED. ### **NO GRADE WAS MOVED BY THIS SEAT**, and the three choices the author '
     'faces are named without one being chosen'),
    ('whether the frozen surfaces should carry pins at all', 'STAND', None, None,
     "NEW at b373: every row this act could pin sits on a deposited companion, an archived snapshot "
     "or an append-only ledger entry, and this seat will not read a citation-hygiene ruling as a "
     'licence to rewrite any of the three. ### **ROUTED, NOT DECIDED**'),
    ("the guard's own front matter", 'CLOSE', 'b373_hooks',
     'NOW PINS `eol=lf` IN EVERY ROSTERED REPOSITORY',
     "the item's occasion was an owner instrument whose closing sentence `b372` had made false. ### "
     '**THE ORDER LICENSED THE CORRECTION AND IT IS MADE, WITH THE CAVEAT KEPT RATHER THAN DELETED '
     'ALONG WITH THE FALSEHOOD.** ### Killed by this act, and flagged as such'),
    ("the guard's own stale install line", 'STAND', None, None,
     'the tracked guard STILL documents an install path the record no longer uses. ### **THIS IS NOT '
     'THE SENTENCE THIS ACT WAS SENT TO CORRECT** -- that one was in the exerciser, this one is in '
     'the guard -- and conflating them would close an item nothing killed'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def newest_run(stem):
    """### **RESOLVE BY THE RECORDED CLOCK, NOT BY THE NAME** (`b358`)."""
    cands = sorted(glob.glob(os.path.join(D, stem + '*.txt')))
    best, bstamp = None, ''
    for c in cands:
        s = run_clock.read_stamp(c) or ''
        if s >= bstamp:
            best, bstamp = c, s
    return best, bstamp


def main():
    rec('=' * 100)
    rec('b373 -- THE DESK, SWEPT UNDER `(R7)`.')
    rec('=' * 100)
    rec('')
    rec('  ### the needle helper fixtures : %s' % GN.self_test(False))
    rec('  ### ### **`(R7)`:** ### *an item whose occasion is gone closes, with the file and date that')
    rec('  ### killed it named.* ### **A DESK THAT ONLY ACCUMULATES IS A LIST.**')
    rec('')
    rec('-' * 100)
    rec('  ### THE SWEEP.')
    rec('-' * 100)
    marks, refused, own = [], 0, 0
    for item, want, stem, sentence, why in DESK:
        row = dict(item=item, disposition=want, killing_stem=stem, why=why)
        if want == 'CLOSE':
            p, stamp = newest_run(stem)
            exists = bool(p) and os.path.exists(p)
            carries, date = False, None
            if exists:
                body = io.open(p, encoding='utf-8', errors='replace').read()
                carries = GN.norm(sentence) in GN.norm(body)
                date = (stamp or '')[:10] or datetime.datetime.fromtimestamp(
                    os.path.getmtime(p), datetime.timezone.utc).strftime('%Y-%m-%d')
            mine = bool(p) and os.path.basename(p).startswith(ACT)
            row.update(exists=exists, carries=carries, date=date, sentence=sentence,
                       killing_file=(os.path.basename(p) if p else None),
                       run_clock=stamp, own_act=mine)
            if not (exists and carries):
                row['disposition'] = 'STAND'
                row['why'] = ('CLOSURE REFUSED: the killing file %s the sentence claimed for it, so '
                              'this item stays open'
                              % ('does not exist' if not exists else 'does not carry'))
                refused += 1
            elif mine:
                own += 1
            marks.append(row)
            rec('')
            rec('    %-58s %s' % (item[:58], row['disposition']))
            rec('        killing file : `data/%s`   recorded clock %s   exists : %s   carries : %s'
                % (row['killing_file'], stamp, exists, carries))
            rec('        | %s' % sentence[:110])
            if mine and row['disposition'] == 'CLOSE':
                rec("        ### ### **FLAGGED: THE KILLING FILE IS THIS ACT`S OWN.** ### Allowed --")
                rec('        ### ### this act did the killing -- and NOT a confirmation from the record.')
            rec('        why : %s' % why[:150])
            if len(why) > 150:
                rec('              %s' % why[150:320])
        else:
            marks.append(row)
            rec('')
            rec('    %-58s %s' % (item[:58], 'STANDS'))
            rec('        why : %s' % why[:150])
            if len(why) > 150:
                rec('              %s' % why[150:320])

    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('=' * 100)
    rec('  ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('  ### ### **CLOSURES REFUSED FOR WANT OF A KILLING FILE : %d.**' % refused)
    rec('  ### ### **CLOSURES WHOSE KILLING FILE IS THIS ACT`S OWN : %d**, each flagged above.' % own)
    rec('  ### **AND NO ITEM CLOSED ON THE ORDER`S SAY-SO.** ### The order named none of these.')
    rec('=' * 100)
    p = run_clock.write(D, 'b373_desk_notes', LINES)
    io.open(os.path.join(D, 'b373_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(rule='(R7)', items=len(marks), closed=len(closed), standing=len(stands),
                        closures_refused=refused, own_act_closures=own, marks=marks,
                        closed_items=[dict(item=m['item'], file='data/%s' % m['killing_file'],
                                           date=m['date'], own_act=m['own_act']) for m in closed],
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
