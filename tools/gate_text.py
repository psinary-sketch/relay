# -*- coding: utf-8 -*-
"""gate_text.py -- THE GATE FLATTENER, IN ONE PLACE, REPAIRED, built b347 by the author's order.

### ### **THE DEFECT, AND WHERE IT CAME FROM.** ### The corpus's banks wrap prose across lines and prefix every line
### with `###`; a continuation line often carries `### ###`. ### A gate arm that asks whether a bank CONTAINS a
### sentence must therefore compare against a FLATTENED copy. ### The flattener written at b344 stripped
### ### **ONE** ### leading marker per line:
###     `re.sub(r'(?m)^###\\s*', ' ', s)`
### ### **SO A SENTENCE CONTINUED ONTO A `### ###` LINE KEPT A MARKER IN THE MIDDLE OF ITSELF**, and no flattened
### comparison could match it. ### It was copied unchanged into b345 and it silently failed five arms of b346's suite
### in one run before b346 repaired it LOCALLY.
###
### ### **THE REPAIR:** strip repeated leading markers -- `^(?:###\\s*)+` -- in ONE utility, so the next act inherits
### the repair instead of the defect.
###
### ### ### **THE REACH, STATED SO THE UTILITY IS NOT TRUSTED BEYOND IT:**
### ### ### **(1) IT NORMALISES TEXT. ### IT DOES NOT KNOW WHAT A SENTENCE MEANS.** ### An arm that greps a flattened
### ### bank for a phrase still passes on a bank that contains the phrase and means the opposite.
### ### ### **(2) THE COPIES ALREADY IN b342, b343, b344, b345 AND b346 ARE NOT EDITED BY THIS FILE.** ### The record
### ### does not silently overwrite itself. ### Which of their arms the defect weakened is MEASURED by b347 and
### ### reported; ### **NOTHING IS RE-VERDICTED.**
### ### ### **(3) THE DIRECTION OF THE DEFECT IS TOWARD FALSE ALARM.** ### An arm whose phrase failed to match made
### ### its gate FAIL, not pass. ### That is the safe direction, and it is why the defect survived two acts: a
### ### failing arm gets rewritten, and a rewritten arm looks like a passing one.
###
### ### **`flat_b344` IS KEPT HERE FOR ONE PURPOSE ONLY: SO THE FIXTURE CAN DISCRIMINATE.** ### Nothing may call it
### as a flattener.
"""
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def flat(s):
    """### THE FLATTENER, REPAIRED: repeated leading `###` markers are stripped, then whitespace is collapsed."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^(?:###\s*)+', ' ', s.replace('’', "'"))).strip()


def flat_b344(s):
    """### THE OLD BEHAVIOUR, KEPT SO THE FIXTURE CAN DISCRIMINATE. ### **NOT FOR USE.** ### It strips ONE leading
    ### marker, so a sentence continued onto a `### ###` line keeps a marker inside itself."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^###\s*', ' ', s.replace('’', "'"))).strip()


# ### THE FIXTURE'S OWN TEXT, WRITTEN HERE SO IT IS NOT DRAWN FROM ANY BANK.
BROKEN = ('### ### **A SENTENCE THAT RUNS ACROSS A DOUBLED\n'
          '### ### MARKER AND MUST STILL BE FOUND.**\n')
WHOLE = '### **A SENTENCE THAT SITS ON ONE LINE AND MUST BE FOUND UNDER BOTH.**\n'
PHRASE_BROKEN = 'A SENTENCE THAT RUNS ACROSS A DOUBLED MARKER AND MUST STILL BE FOUND'
PHRASE_WHOLE = 'A SENTENCE THAT SITS ON ONE LINE AND MUST BE FOUND UNDER BOTH'


def self_test(verbose=True):
    """### BOTH POLARITIES. ### **THE REPAIR MUST FIND WHAT THE OLD BEHAVIOUR MISSED, AND THE OLD BEHAVIOUR MUST
    ### ACTUALLY MISS IT, OR THE FIXTURE HAS NOT BEEN SEEN TO DISCRIMINATE.**"""
    def say(s):
        if verbose:
            print(s)

    a1 = PHRASE_BROKEN in flat(BROKEN)
    a2 = PHRASE_BROKEN not in flat_b344(BROKEN)
    a3 = PHRASE_WHOLE in flat(WHOLE)
    a4 = PHRASE_WHOLE in flat_b344(WHOLE)
    say('    (1) the doubled-marker sentence IS found by the repair          : %s  %s' % (a1, 'PASS' if a1 else '### FAIL ###'))
    say('    (2) and is NOT found by the old behaviour (the discrimination)  : %s  %s' % (a2, 'PASS' if a2 else '### FAIL ###'))
    say('    (3) a one-line sentence is found by the repair                  : %s  %s' % (a3, 'PASS' if a3 else '### FAIL ###'))
    say('    (4) and by the old behaviour too, so the repair loses nothing   : %s  %s' % (a4, 'PASS' if a4 else '### FAIL ###'))
    ok = a1 and a2 and a3 and a4
    if verbose and not ok:
        say('    ### the old behaviour on the broken case: %r' % flat_b344(BROKEN))
    return ok


if __name__ == '__main__':
    print('gate_text.py -- self-test (both polarities):')
    sys.exit(0 if self_test() else 1)
