# -*- coding: utf-8 -*-
"""quote_norm.py -- THE SHARED NORMALISER FOR QUOTATION COMPARISON, built b349 by the author's order.

### ### **THE SPECIES: A COMPARISON WHOSE TWO SIDES ARE NORMALISED DIFFERENTLY AGREES OR DISAGREES ABOUT THE
### ### NORMALISATION RATHER THAN ABOUT THE CONTENT.**
###
### ### **IT IS BANKED THREE TIMES IN THIS RECORD, AND THE BYTE HALF OF IT WAS ALREADY CURED.**
### ### **b298** -- a UTF-8 BOM was written into a banked file by a shell redirection. ### The act's own two
### ### comparisons both missed it: one compared the file against ANOTHER redirection-produced file (both carried
### ### the BOM), and the other compared against `git HEAD` LINE BY LINE, *"which normalises exactly this
### ### difference away"*. ### **TWO CHECKS AGREED AND NEITHER OF THEM SAW IT.**
### ### **b309** -- a raw byte comparison failed on a file `git status` called CLEAN, because `core.autocrlf`
### ### had rewritten the working side to CRLF while the blob stayed LF. ### b309 named it *"THE b298 FAMILY
### ### EXACTLY: A BYTE CHECK DEFEATED BY A BYTE NOBODY MEANT TO WRITE"*, and ### **CURED THE BYTE HALF**: both
### ### sides are now put through `b302_kernel.normalise`, IMPORTED and not copied.
### ### **b348** -- the QUOTATION half, still open. ### The fold's emitter stripped the mid-line `###`
### ### separators and the bold markers before writing a quotation into the section; its independent re-checker
### ### stripped only LEADING markers. ### Two quotations that had been emitted correctly read as MISSING, and
### ### the arm reported a defect that was its own.
###
### ### ### **WHAT THIS FILE IS: THE `b302_kernel.normalise` OF QUOTATIONS.** ### One function, imported by
### ### BOTH the side that writes a quotation and the side that checks it. ### **A NORMALISER THAT IS COPIED IS
### ### NOT SHARED, AND THE WHOLE DEFECT IS THAT TWO COPIES DRIFT.**
###
### ### ### **THE REACH, STATED SO IT IS NOT TRUSTED BEYOND IT:**
### ### ### **(1) IT MAKES TWO SIDES COMPARABLE. ### IT DOES NOT MAKE A QUOTATION TRUE.** ### A sentence that
### ### survives this normaliser and means the opposite of its source is still a false quotation, and no
### ### mechanical check here reaches that.
### ### ### **(2) IT DISCARDS PRESENTATION, AND PRESENTATION CAN CARRY MEANING.** ### It folds away the corpus's
### ### own markup -- `###` separators, `**` emphasis, backticks, curly quotes and dashes -- and collapses
### ### whitespace. ### **A DIFFERENCE THAT LIVES ONLY IN THOSE IS INVISIBLE TO A COMPARISON THAT USES IT**, and
### ### an act that needs one of them to be exact must compare raw and say so.
### ### ### **(3) IT IS NOT RETROACTIVE.** ### Every comparison written before it keeps whatever normalisation
### ### its own act gave it. ### **NOTHING IS RE-VERDICTED BY THIS FILE**, and b348's section stands as emitted.
"""
import re
import sys
import unicodedata

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE MARKUP THE CORPUS'S OWN PROSE CARRIES, FOLDED AWAY SO THAT TWO SIDES CAN BE COMPARED.
_MARKER = re.compile(r'#{2,}')
_EMPH = re.compile(r'\*+|`+|_{2,}')
_WS = re.compile(r'\s+')
# ### the typographic pairs that differ between a bank and a markdown emission of the same sentence.
_FOLD = {
    '’': "'", '‘': "'", '“': '"', '”': '"',
    '—': '-', '–': '-', '−': '-', ' ': ' ',
}


def norm(s):
    """### THE ONE NORMALISATION. ### **BOTH SIDES OF EVERY QUOTATION COMPARISON GO THROUGH THIS FUNCTION, OR
    ### THE COMPARISON IS ABOUT THE NORMALISATION AND NOT ABOUT THE CONTENT.**"""
    if s is None:
        return ''
    s = unicodedata.normalize('NFC', s)
    s = s.lstrip('﻿')                 # ### b298's BOM, wherever it landed
    s = s.replace('\r\n', '\n').replace('\r', '\n')   # ### b309's CRLF
    for a, b in _FOLD.items():
        s = s.replace(a, b)
    s = _MARKER.sub(' ', s)                # ### b348's mid-line `###` separators
    s = _EMPH.sub(' ', s)                  # ### and its `**` emphasis and backticks
    return _WS.sub(' ', s).strip()


def contains(haystack, needle):
    """### THE COMPARISON ITSELF, so that no caller can normalise one side and forget the other."""
    return norm(needle) in norm(haystack)


def self_test(verbose=True):
    """### FIXTURES, BOTH POLARITIES, ON SYNTHETIC TEXT DRAWN FROM NO BANK.
    ### ### **A NORMALISER THAT MATCHES EVERYTHING IS NOT A NORMALISER.**"""
    def say(s):
        if verbose:
            print(s)

    r = []
    # ### (1) b348's case: a bank line with mid-line markers against the emitted form with them stripped
    bank = '### REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET.'
    emitted = 'REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED.  THE BAR AS SEALED IS NOT MET.'
    r.append(("b348's case: mid-line markers folded on BOTH sides", contains(bank, emitted)))
    # ### (2) b298's case: a BOM on one side only
    r.append(("b298's case: a BOM on one side only", contains('﻿alpha beta', 'alpha beta')))
    # ### (3) b309's case: CRLF on one side only
    r.append(("b309's case: CRLF against LF", contains('alpha\r\nbeta', 'alpha\nbeta')))
    # ### (4) the curly/straight pair that refused b348's fold on its first emission
    r.append(('the curly apostrophe against the straight one', contains("b315’s reason", "b315's reason")))
    # ### (5) emphasis and backticks folded
    r.append(('bold and backticks folded', contains('**A FOURTH `CONTROL` HOLDS**', 'A FOURTH CONTROL HOLDS')))
    # ### ### **THE OTHER POLARITY, WHICH IS WHAT MAKES THE ABOVE WORTH ANYTHING.**
    r.append(('### a genuinely absent sentence is NOT found', not contains('alpha beta gamma', 'delta epsilon')))
    r.append(('### a CHANGED WORD is NOT normalised away', not contains('the bar IS met', 'the bar is NOT met')))
    r.append(('### a changed NUMBER is NOT normalised away', not contains('worst 4.394e-18', 'worst 4.394e-19')))
    r.append(('### a dropped clause is NOT found', not contains('the identity held', 'the identity held at all indices')))
    for what, ok in r:
        say('    %-58s %s  %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


if __name__ == '__main__':
    print('quote_norm.py -- self-test (both polarities):')
    sys.exit(0 if self_test() else 1)
