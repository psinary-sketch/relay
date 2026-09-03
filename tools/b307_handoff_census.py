# -*- coding: utf-8 -*-
"""b307_handoff_census.py -- ### **THE CHECK THAT COUNTS WHAT IS MISSING FROM `HANDOFF.md`.**

### WHY THIS EXISTS, AND IT IS NOT A CONVENIENCE. ### `U-2` is STRUCK: *"a closing sequence asserts
### that a ledger is current."* ### But the strike is ### CONDITIONAL ### , and the record's own
### entry names the condition: ### **"SURVIVES: the same phrase after a check that has COUNTED WHAT
### IS MISSING. ### The strike is conditional in the author's own words and the condition is a real
### check, not a reading."**
### ### ### **NO SUCH CHECK EXISTED. ### THAT IS WHY THE PHRASE HAS BEEN UNUSABLE SINCE b300, AND
### ### ### WHY EVERY ACT SINCE HAS WRITTEN TWO LISTS INSTEAD.** ### This is the check.

### ### **WHAT IT COUNTS, AND THE DEFINITION IS MECHANICAL SO THE ANSWER IS NOT A READING:**
###   ### **(1) THE ARC'S ACTS.** ### Every act id in the folded arc must appear in `HANDOFF.md`.
###   ### **(2) THE LIVE WORK-ORDERS.** ### Every work-order the arc's in-flight registers carry as
###     live must appear.
###   ### **(3) THE ARC'S FINDINGS SECTION.** ### The section this act appends must be pointed at.
### ### **A NAME THAT DOES NOT APPEAR IS MISSING. ### THAT IS THE WHOLE RULE**, and it is chosen
### because it is checkable rather than because it is generous.

### ### ### **THE LIMITS, IN THE HEADER SO THE LICENCE IS NOT OVERDRAWN:**
### ### **(1) IT COUNTS NAMES, NOT UNDERSTANDING.** ### A ledger that names every act in one line
###     each passes this census and may still be a bad handoff. ### **THE CENSUS LICENSES A PHRASE
###     ABOUT COVERAGE AND NOTHING ABOUT QUALITY.**
### ### **(2) IT IS ABOUT `HANDOFF.md` ALONE.** ### It says nothing about `FINDINGS.md`,
###     `REGISTRY.md`, `OPEN_TRAILS.md` or the desk, and ### **ONE COUNTED LEDGER MAY NOT STAND IN
###     FOR THE OTHERS.**
### ### **(3) THE LISTS ARE THIS ACT'S.** ### They are declared here, in the tool, so a later reader
###     can disagree with the scope rather than with a number. ### **A CENSUS OVER A LIST NOBODY CAN
###     SEE IS NOT A CENSUS.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDOFF = os.path.join(ROOT, 'HANDOFF.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (1) THE FOLDED ARC, PLUS THE FOLDING ACT ITSELF.
ACTS = ['b297', 'b298', 'b299', 'b300', 'b301', 'b302',
        'b303', 'b304', 'b305', 'b306', 'b307']

# ### (2) THE LIVE WORK-ORDERS, AS THE ARC'S IN-FLIGHT REGISTERS CARRY THEM.
WORK_ORDERS = [
    'W-ORD-ARCH-NORM-READING',
    'W-ORD-TERM3-ROW',
    'W-ORD-UNIFORM-FORM',
    'W-ORD-FAMILY-OBJECT-DIVISION',
    'W-ORD-SMEAR-GROUP-SPLIT',
    'W-ORD-DIFFERENCE-CONTENT',
    'W-ORD-INSTRUMENT-Q-P',
    'W-ORD-SOURCE-METHOD-APPLICABILITY',
    'W-ORD-JUNCTION-LAST-PLACE',
    'W-ORD-ANCESTOR-ROW-b284',
    'W-ORD-OBJECT-CONDITION-COUNT',
    'W-ORD-DEBT-FRESHNESS',
    'W-ORD-HOOK-COVERAGE',
    'W-ORD-PRINT-COVERAGE',
]

# ### (3) THE SECTION THIS ACT APPENDS TO THE FINDINGS DOCUMENT.
SECTIONS = ['THE ADELIC ARC, b297']


def present(text, name):
    """### IS `name` IN `text`? ### **A WORD-BOUNDARY MATCH FOR ACT IDS, A PLAIN ONE OTHERWISE.**

    ### ### **THE BOUNDARY MATTERS AND IT IS THE ONE THING THIS FUNCTION GETS WRONG IF RUSHED:**
    ### without it, `b30` would be found inside `b300` and an absent act would be reported present.
    """
    if re.fullmatch(r'b\d+', name):
        return re.search(r'\b%s\b' % re.escape(name), text) is not None
    return name in text


def census(text):
    """### RETURNS `(missing_acts, missing_orders, missing_sections)`."""
    ma = [a for a in ACTS if not present(text, a)]
    mo = [w for w in WORK_ORDERS if not present(text, w)]
    ms = [s for s in SECTIONS if not present(text, s)]
    return ma, mo, ms


def self_test(verbose=True):
    """### **BOTH POLARITIES, AND THE BOUNDARY ARM IS THE ONE THAT MATTERS.**"""
    bad = 0

    def chk(lbl, got, exp):
        nonlocal bad
        ok = (got == exp)
        bad += 0 if ok else 1
        if verbose:
            print('  %-58s %-14s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-58s %-14s %s' % ('fixture', 'got/exp', 'agree'))
    chk('finds an act id that is there', present('the act b301 did', 'b301'), True)
    chk('### does NOT find one that is absent', present('the act b301 did', 'b302'), False)
    chk('### and b30 is NOT found inside b300', present('at b300 the seat', 'b30'), False)
    chk('### nor b3 inside b307', present('at b307 the seat', 'b3'), False)
    chk('finds a work-order name', present('carried: W-ORD-TERM3-ROW; and', 'W-ORD-TERM3-ROW'),
        True)
    chk('### does not find an absent work-order',
        present('carried: W-ORD-TERM3-ROW; and', 'W-ORD-NOT-A-THING'), False)
    chk('census over empty text reports everything missing',
        census('') == (ACTS, WORK_ORDERS, SECTIONS), True)
    chk('### census over text naming one act drops it from missing',
        'b301' in census('b301')[0], False)
    return bad == 0


def main(argv):
    label = argv[0] if argv else 'CENSUS'
    print('=' * 100)
    print('b307_handoff_census.py -- %s. ### WHAT IS MISSING FROM `HANDOFF.md`, COUNTED.' % label)
    print('=' * 100)
    ok = self_test()
    print('  self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A CENSUS FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2
    if not os.path.exists(HANDOFF):
        print('  ### HARD FAILURE -- THE LEDGER IS NOT AT %s' % HANDOFF)
        return 2

    text = io.open(HANDOFF, encoding='utf-8', errors='replace').read()
    ma, mo, ms = census(text)
    print()
    print('  ledger        : %s' % os.path.basename(HANDOFF))
    print('  bytes / lines : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print()
    print('  ### (1) THE ARC\'S ACTS  -- %d checked, %d MISSING' % (len(ACTS), len(ma)))
    for a in ma:
        print('        ### MISSING  %s' % a)
    print('  ### (2) THE LIVE WORK-ORDERS -- %d checked, %d MISSING'
          % (len(WORK_ORDERS), len(mo)))
    for w in mo:
        print('        ### MISSING  %s' % w)
    print('  ### (3) THE ARC\'S FINDINGS SECTION -- %d checked, %d MISSING'
          % (len(SECTIONS), len(ms)))
    for s in ms:
        print('        ### MISSING  %s' % s)

    total = len(ma) + len(mo) + len(ms)
    print()
    print('  ### ### **TOTAL MISSING : %d**' % total)
    if total == 0:
        print('  ### ### **THE CENSUS HAS COUNTED WHAT IS MISSING AND FOUND NOTHING.**')
        print('  ### ### **`U-2`\'s `SURVIVES` CLAUSE IS THEREFORE SATISFIED FOR THIS LEDGER, AND')
        print('  ### ### THE PHRASE MAY BE USED OF `HANDOFF.md` -- OF THAT LEDGER AND NO OTHER.**')
    else:
        print('  ### ### **THE PHRASE IS NOT LICENSED. ### THE ACT STATES WHAT IT WROTE AND WHAT')
        print('  ### ### IT DID NOT CHECK, WHICH IS THE AUTHOR\'S OWN REPLACEMENT.**')
    print()
    print('  ### **AND WHAT THIS LICENSES IS ONE PHRASE ABOUT ONE LEDGER.** ### It says nothing')
    print('  ### about `FINDINGS.md`, `REGISTRY.md`, `OPEN_TRAILS.md` or the desk, and it counts')
    print('  ### NAMES rather than understanding. ### **A LEDGER NAMING EVERY ACT IN ONE LINE EACH')
    print('  ### PASSES THIS CENSUS AND MAY STILL BE A BAD HANDOFF.**')
    print('=' * 100)
    return 0 if total == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
