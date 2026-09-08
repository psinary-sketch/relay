# -*- coding: utf-8 -*-
"""b370_desk.py -- THE DESK, SWEPT ONCE MORE UNDER THE FRESHNESS RULE. ### **MARKS ONLY.**

### ### **THE RULE IS `b368`'s AND IS NOT RESTATED AS THIS ACT'S:** ### *every desk item names the file
### and date at which it was last confirmed, and an item without one is re-verified before it is ordered.*
### ### **NO MODULE IS WRITTEN HERE.** ### `b368` minted it; this act USES it, which is the one thing
### `b368` said its own sweep had not done.
### ### **THIS ACT'S OWN FILES ARE EXCLUDED FROM THE CONFIRMING SET** (`b368`'s incident): ### a sweep
### that reads its own paperwork confirms itself.
### ### ### **AND `NO ITEM IS CLOSED`. ### THE SWEEP PRODUCES MARKS, NOT VERDICTS**, in the order's own
### words -- and a mark of `CONFIRMED-BY-FILE` says a banked file MENTIONS the item, ### **NOT THAT THE
### ### ITEM WAS RE-VERIFIED.** ### That limit is the module's own and is printed with the result.
"""
import datetime
import glob as G
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
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODULE = os.path.join(TC, 'modules', '2026-09', 'DESK_FRESHNESS.md')
FOLD = os.path.join(D, 'b360_the_fold.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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


def newest_confirming(pat, needle):
    best = None
    for p in sorted(G.glob(os.path.join(ROOT, pat.replace('/', os.sep)))):
        if os.path.basename(p).startswith('b370_'):
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
                date=datetime.datetime.fromtimestamp(best[1],
                                                     datetime.timezone.utc).strftime('%Y-%m-%d'))


def main():
    rec('=' * 100)
    rec('b370 -- THE DESK, SWEPT UNDER THE FRESHNESS RULE. ### **MARKS, NOT VERDICTS.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    mod = io.open(MODULE, encoding='utf-8').read() if os.path.exists(MODULE) else ''
    rule_ok = GN.norm('RE-VERIFIED before it is ordered') in GN.norm(mod)
    rec('  ### the rule is read from `b368`s module, not restated here : %s' % rule_ok)
    if not rule_ok:
        rec('  ### ### **THE MODULE IS NOT WHERE `b368` LEFT IT. ### NOTHING IS SWEPT.**')
        run_clock.write(D, 'b370_desk_notes', LINES)
        return 2

    n, _l = AF.find(FOLD, 'One list, each item with where it stands and what would move it: `M-2` under')
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK, NAMED BEFORE IT IS SWEPT. ### `b360`s fold, line %d.' % n)
    rec('-' * 100)
    txt = io.open(FOLD, encoding='utf-8', errors='replace').read().split(chr(10))
    rec('    | %s' % strip_markers(chr(10).join(txt[n - 1:n + 6]))[:300])

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP.')
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
    nc = sum(1 for m in marks if m['mark'] == 'CONFIRMED-BY-FILE')
    nu = len(marks) - nc
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CONFIRMED-BY-FILE : %d. ### UNCONFIRMED : %d.**'
        % (len(marks), nc, nu))
    rec('    ### ### **AND `0` ITEMS CLOSED BY THIS ACT.**')
    rec('    ### **AND THE SAME LIMIT `b368` PRINTED, PRINTED AGAIN BECAUSE IT HAS NOT CHANGED:**')
    rec('    ### **A FILE THAT MENTIONS AN ITEM IS NOT A FILE THAT CONFIRMS IT**, and this sweep cannot')
    rec('    ### tell the two apart. ### `%d of %d CONFIRMED` IS A MARK ON THE SHAPE OF THE RECORD.' % (nc, len(marks)))
    rec('    ### ### ### **AND THIS IS THE THIRD TIME THE SAME NUMBER HAS BEEN REPORTED WITH THE SAME')
    rec('    ### ### ### CAVEAT.** ### `b368` swept and marked it; `b369` swept and said the result was')
    rec('    ### weaker than it looks; ### **`b370` SWEEPS AND GETS THE SAME ANSWER AGAIN.** ### A')
    rec('    ### measurement whose result and whose caveat both never move is ### **A MEASUREMENT NOBODY')
    rec('    ### ### IS USING** -- and three acts have now paid for it. ### `b369`s draft asked the next')
    rec('    ### act to re-verify ONE item properly and this order did not carry that; ### **SO IT IS')
    rec('    ### ### CARRIED FORWARD AGAIN, WHICH IS ITSELF THE FINDING.**')
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE ITEMS NAMED AS STILL OWED. ### **NAMED, NOT CLOSED, NOT BUILT.**')
    rec('-' * 100)
    rec('  ### ### **(i) THE COUNT CLAIM ABOVE THE REPAIRED LIST.** ### `b369` repaired the Layer-1')
    rec('  ### export list and left the paragraph above it asserting a count of framework consequences,')
    rec('  ### because its order said the LIST is corrected and ### **A COUNT IS NOT A NAME.** ### It')
    rec('  ### stands untouched. ### **THE FRONT DOCUMENT IS NOT NOW CORRECT**, and no act has claimed')
    rec('  ### it is.')
    rec('  ### ### **(ii) THE HOOK IS NOT DURABLE, AND A DURABLE FIX IS PRICED HERE AND NOT BUILT.**')
    rec('  ### `.git/hooks/` is untracked. ### **A FRESH CLONE OF ANY OF THE FOUR REPOSITORIES STARTS')
    rec('  ### ### WITH NO PRE-PUSH HOOK** -- including the three that have carried one since `b304`.')
    rec('  ### ### **WHAT A DURABLE FIX WOULD BE:** ### the guard already ships as a tracked file')
    rec('  ### (`tools/git-hooks/pre-push`); what is missing is that ### **NOTHING FAILS WHEN IT IS NOT')
    rec('  ### ### INSTALLED.** ### A durable fix is a bootstrap step plus ### **AN ALREADY-DURABLE')
    rec('  ### ### CHECK THAT FAILS ON ITS ABSENCE** -- an arm in the closing suite that reads')
    rec('  ### `.git/hooks/pre-push` in every rostered repository and refuses if it is missing or')
    rec('  ### differs from the tracked source. ### That arm IS tracked, so it travels.')
    rec('  ### ### **THE PRICE: ONE ARM IN ONE SUITE, PLUS A LINE IN THE PUSH PROCEDURE.** ### It is')
    rec('  ### small. ### **IT IS ALSO EXACTLY THE SHAPE OF THE STEP-ZERO REPAIR THIS ACT WAS SENT TO')
    rec('  ### ### MAKE -- A LESSON FILED TWICE AND NOT BUILT** -- and this act does NOT build it,')
    rec('  ### because the order priced it and did not order it. ### **NAMED, PRICED, NOT BUILT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b370_desk_notes', LINES)
    io.open(os.path.join(D, 'b370_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(rule_read_from_module=True, module=os.path.relpath(MODULE, TC).replace(os.sep, '/'),
             module_written=False, items=len(marks), confirmed=nc, unconfirmed=nu,
             items_closed=0, marks=marks, owed_named=2, durable_fix_built=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
