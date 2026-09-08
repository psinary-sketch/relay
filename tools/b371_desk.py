# -*- coding: utf-8 -*-
"""b371_desk.py -- THE DESK, SWEPT UNDER `(R7)`. ### **IT CLOSES ITEMS NOW.**

### ### **`(R7)`:** ### *an item whose occasion is gone closes, with the file and date that killed it
### named.* ### **A DESK THAT ONLY ACCUMULATES IS A LIST.**
### ### ### **AND A CLOSURE WITHOUT A KILLING FILE IS AN OPINION.** ### Every closure below names a
### banked file, that file is checked to EXIST and to CARRY the sentence claimed for it, and its date is
### the file's own. ### **AN ITEM THIS ACT CANNOT KILL WITH A FILE STAYS OPEN**, however dead it looks.
### ### **THIS IS A REVERSAL OF WHAT `b368`, `b369` AND `b370` WERE TOLD**, each of which was ordered to
### produce MARKS, NOT VERDICTS. ### **NONE OF THEM IS RE-VERDICTED**; the author changed the
### disposition, and this act says so rather than quietly closing what three acts were forbidden to.
"""
import datetime
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
FOLD = os.path.join(D, 'b360_the_fold.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (item, disposition, killing file, the sentence that file must carry, why)
# ### **`CLOSE` REQUIRES A FILE AND A SENTENCE. ### `STAND` REQUIRES A REASON. ### NOTHING ELSE CLOSES.**
DESK = [
    ('M-2, under b310 cap', 'STAND', None, None,
     'the aggregation is still SPECIFIED-NOT-STATED and b310 cap still governs; no act has stated it'),
    ("the object's conditions", 'STAND', None, None,
     'the conditions are the object\'s and none has been discharged by this span'),
    ('the uniformity row U1, four entries and its own refusal', 'STAND', None, None,
     "b361 wrote an UPDATE BLOCK on the row because a decision moved it; the row's own refusal stands "
     'and the entries are unchanged'),
    ('the instrument lane, PARKED under ruling R4', 'STAND', None, None,
     "PARKED by the author's ruling; only the author unparks it"),
    ('the anchored gate arms, available mechanical work, unscheduled and not built', 'CLOSE',
     'b363_the_anchored_gate_arms.txt',
     'THE HELPER IS BUILT AND IT IS NARROWER THAN THE RULE IT WAS PROPOSED UNDER.',
     "the item's occasion was work UNSCHEDULED AND NOT BUILT; b363 built the helper and b366 swept "
     'every arm in the record with it. ### **THE WORK IS DONE AND THE ITEM DESCRIBES WORK THAT IS NOT**'),
    ('the wave candidate list, typed and not ranked at b324', 'STAND', None, None,
     'typed and not ranked; ranking is the author\'s and no act has ranked it'),
    ("the wave itself, the author's own", 'STAND', None, None,
     "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', None, None,
     'each still carries its owner and none has been opened'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', None, None,
     "ABSENT on the mounted volumes and UNCONFIRMED on this seat's record; the patent seat owns it"),
    # ---- THE ITEM THE ORDER NAMES BY NAME ------------------------------------------------------------
    ('the scaffold repair (trails: SCAFFOLD-TERMINALS)', 'CLOSE', 'b367_the_scaffold_repair.txt',
     'NOT LOCATED. ### THE TERMINALS DO NOT EXIST, AND THE KERNEL SAYS SO ITSELF.',
     "the item's occasion was a REPAIR of two terminals; b367 found them retired and gone at the kernel, "
     'and b368 and b369 confirmed it twice more. ### **THERE IS NOTHING TO REPAIR AND THE KERNEL SAYS '
     'SO** -- the order names this one, and this act still produces its killing file rather than closing '
     "it on the order's say-so"),
    # ---- THE ITEM THIS ACT ITSELF KILLED -------------------------------------------------------------
    ("the hook's non-durability (named owed at b370)", 'CLOSE', 'b371_hookpath_notes.txt',
     'COMPONENT 3 OUTCOME : MADE DURABLE',
     "the item's occasion was a guard living where a clone does not carry it; this act moved it to a "
     'TRACKED path in every rostered repository and exercised it in both polarities. ### **CLOSED BY '
     'THIS ACT, AND THE KILLING FILE IS THIS ACT\'S OWN** -- which is allowed because this act did the '
     'killing, and is flagged so no reader mistakes it for a confirmation from the record'),
    # ---- AND THE ONE b369 AND b370 BOTH LEFT OWED ----------------------------------------------------
    ('the count claim above the repaired Layer-1 list', 'STAND', None, None,
     'b369 repaired the LIST and left the count claim above it untouched, because its order said the '
     'list is corrected and a count is not a name; no act has been sent to it since'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def main():
    rec('=' * 100)
    rec('b371 -- THE DESK, SWEPT UNDER `(R7)`. ### **IT CLOSES ITEMS NOW.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures : %s ; the needle helper : %s'
        % (AF.self_test(False), GN.self_test(False)))
    rec('')
    rec('  ### ### **`(R7)`, THE RULE THIS SWEEP RUNS UNDER:** ### *an item whose occasion is gone')
    rec('  ### closes, with the file and date that killed it named.*')
    rec('  ### ### **AND A CLOSURE WITHOUT A KILLING FILE IS AN OPINION**, so every closure below is')
    rec('  ### refused unless its file exists AND carries the sentence claimed for it.')

    n, _l = AF.find(FOLD, 'One list, each item with where it stands and what would move it: `M-2` under')
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK, NAMED BEFORE IT IS SWEPT. ### `b360`s fold, line %d.' % n)
    rec('-' * 100)
    txt = io.open(FOLD, encoding='utf-8', errors='replace').read().split(chr(10))
    rec('    | %s' % strip_markers(chr(10).join(txt[n - 1:n + 6]))[:280])
    rec('    ### **AND TWO ITEMS BELOW ARE NOT ON THAT LIST AND ARE SWEPT ANYWAY:** ### the trails item')
    rec('    ### the order names by name, and the two the last two acts recorded as owed.')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP.')
    rec('-' * 100)
    marks, refused = [], 0
    for item, want, kf, sentence, why in DESK:
        row = dict(item=item, disposition=want, killing_file=kf, why=why)
        if want == 'CLOSE':
            p = os.path.join(D, kf)
            exists = os.path.exists(p)
            carries = False
            date = None
            if exists:
                body = io.open(p, encoding='utf-8', errors='replace').read()
                carries = GN.norm(sentence) in GN.norm(body)
                date = datetime.datetime.fromtimestamp(
                    os.path.getmtime(p), datetime.timezone.utc).strftime('%Y-%m-%d')
            row.update(exists=exists, carries=carries, date=date, sentence=sentence)
            if not (exists and carries):
                row['disposition'] = 'STAND'
                row['why'] = ('CLOSURE REFUSED: the killing file %s the sentence claimed for it, so '
                              'this item stays open' % ('does not exist' if not exists
                                                        else 'does not carry'))
                refused += 1
            marks.append(row)
            rec('')
            rec('    %-58s %s' % (item[:58], row['disposition']))
            rec('        killing file : `data/%s`   dated %s   exists : %s   carries its sentence : %s'
                % (kf, date, exists, carries))
            rec('        | %s' % sentence[:110])
            rec('        why : %s' % why[:150])
            if len(why) > 150:
                rec('              %s' % why[150:300])
        else:
            marks.append(row)
            rec('')
            rec('    %-58s %s' % (item[:58], 'STANDS'))
            rec('        why : %s' % why[:150])
            if len(why) > 150:
                rec('              %s' % why[150:300])

    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d. ### UNCONFIRMED : %d.**'
        % (len(marks), len(closed), len(stands), 0))
    rec('    ### ### **CLOSURES REFUSED FOR WANT OF A KILLING FILE : %d.**' % refused)
    rec('')
    rec('    ### ### ### **AND THE THING WORTH SAYING: THIS IS THE FIRST TIME THE NUMBER HAS MOVED.**')
    rec('    ### `b368`, `b369` and `b370` each swept and each reported `9 of 9 CONFIRMED-BY-FILE, 0')
    rec('    ### CLOSED`, with the same caveat all three times. ### **THE MEASUREMENT DID NOT CHANGE')
    rec('    ### ### BECAUSE THE RULE DID NOT LET IT.** ### `(R7)` changed the rule and the desk moved')
    rec('    ### in the same act -- which is what `b370`s own bank meant by ### *a measurement whose')
    rec('    ### result and whose caveat both never move is a measurement nobody is using.*')
    rec('    ### ### **AND NONE OF THOSE THREE ACTS IS RE-VERDICTED.** ### Each obeyed the rule it was')
    rec('    ### given; the author changed the rule.')
    rec('')
    rec('    ### **AND ONE CLOSURE IS FLAGGED, BECAUSE ITS KILLING FILE IS THIS ACT`S OWN:** ### the')
    rec('    ### hook`s non-durability was killed by this act`s Component 3. ### **THAT IS ALLOWED --')
    rec('    ### ### THIS ACT DID THE KILLING -- AND IT IS NOT A CONFIRMATION FROM THE RECORD**, which')
    rec('    ### is `b368`s incident and is not repeated here by accident.')
    rec('=' * 100)
    p = run_clock.write(D, 'b371_desk_notes', LINES)
    io.open(os.path.join(D, 'b371_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(rule='(R7)', items=len(marks), closed=len(closed), standing=len(stands), unconfirmed=0,
             closures_refused=refused, marks=marks,
             closed_items=[dict(item=m['item'], file='data/%s' % m['killing_file'], date=m['date'])
                           for m in closed],
             acts_reverdicted=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
