# -*- coding: utf-8 -*-
"""needle_pull.py -- EXTRACT GATE NEEDLES FROM THE EMITTING FILE (built b276).

### WHY THIS EXISTS, AND IT IS A DEFECT REPORT BEFORE IT IS A TOOL.
### b273, b274 AND b275 EACH LOST A GATE TO A NEEDLE TYPED FROM MEMORY: ### `A IS A RATIONAL
### matrix` for `a RATIONAL matrix`; ### `R(g_0) = (q - 1) / (2(q + 1))` for the same formula
### without the inner spaces; ### `ESCAPE-CLASS` for `ESCAPE CLASS`; ### `A DIFFERENT VECTOR
### FROM` looked for in the BANK when it lives in the RUN. ### **THREE ACTS RUNNING, EACH TIME
### THE FINDING WAS RIGHT AND THE CHECK WAS WRONG.** ### b275 filed `W-ORD-NEEDLE-SOURCE` and
### said the corpus already owns the machinery and the gates simply do not use it.
### ### **THIS IS THE GATES USING IT.**

### WHAT IT DOES. ### Given a FILE and a SHORT ANCHOR, it returns the ### EXACT LINE ### from
### that file containing the anchor. ### The gate then matches text the file actually emitted,
### ### **NOT TEXT THIS SEAT REMEMBERED EMITTING.**

### WHAT IT CANNOT DO, STATED SO IT IS NOT TRUSTED BEYOND IT:
###   ### **IT CANNOT TELL WHETHER THE ANCHOR IS THE RIGHT ANCHOR.** ### A gate can still be
###   pointed at a true sentence that does not test the claim. ### **IT REMOVES THE TYPO CLASS
###   AND NOTHING ELSE.**
###   ### **IT CANNOT SEE A NEEDLE THE ACT NEVER PULLS.** ### An anchor that matches nothing is
###   an ERROR here, loudly -- which is the point: a needle that cannot be pulled is a needle
###   that would have silently failed later.
"""
import io
import sys


def pull(path, anchor, occurrence=0):
    """### THE EXACT LINE CONTAINING `anchor`, FROM THE FILE ITSELF.
    ### **RAISES IF THE ANCHOR IS ABSENT OR AMBIGUOUS BEYOND `occurrence`.**"""
    hits = [ln.strip() for ln in io.open(path, encoding='utf-8', errors='replace').read().split('\n')
            if anchor in ln]
    if not hits:
        raise LookupError('### ANCHOR NOT FOUND in %s: %r' % (path, anchor))
    if occurrence >= len(hits):
        raise LookupError('### ANCHOR %r has only %d hits in %s, wanted #%d'
                          % (anchor, len(hits), path, occurrence))
    return hits[occurrence]


def pull_all(spec):
    """### `spec` is a list of `(label, path, anchor)`. ### Returns `{label: exact_line}`."""
    out = {}
    for label, path, anchor in spec:
        out[label] = pull(path, anchor)
    return out


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('usage: needle_pull.py <file> <anchor>\n')
        sys.exit(2)
    print(pull(sys.argv[1], sys.argv[2]))


# ### ------------------------------------------------------------------------------------------
# ### THE b278 EXTENSION. ### `W-ORD-SELF-NEEDLE` AND THE INVERTED-FIXTURE SPECIES.
# ### b277 discharged HALF of `W-ORD-NEEDLE-SOURCE`: owner needles were pulled, but the gates'
# ### needles into the act's OWN run and bank were still typed, and three of them were wrong.
# ### ### **AND A FOURTH FAILURE WAS WORSE: A FIXTURE WHOSE STRING WAS A SUBSTRING OF THE
# ### ### CORRECT SENTENCE, SO IT FIRED ON CORRECTNESS AND REFUSED A CHECK THAT SHOULD HAVE
# ### ### PASSED. ### AN INVERTED FIXTURE IS NOT A DEAD ONE, AND A REACHABILITY TEST CANNOT SEE
# ### ### IT, BECAUSE IT IS REACHABLE.**
# ### THE FIX HAS TWO PARTS AND BOTH ARE HERE:
# ###   `pull_self` -- the act pulls needles from ITS OWN emitted files the same way.
# ###   `absent_exact` -- a must-fail fixture asserts that NO LINE EQUALS the given text, an
# ###      EXACT equality over whole lines. ### **A SUBSTRING CANNOT SATISFY IT, SO IT CANNOT
# ###      FIRE ON A LONGER CORRECT SENTENCE.**
# ### ------------------------------------------------------------------------------------------
def _lines(path):
    return [ln.strip() for ln in
            io.open(path, encoding='utf-8', errors='replace').read().split('\n')]


def pull_self(path, anchor, occurrence=0):
    """### IDENTICAL TO `pull`, NAMED SEPARATELY SO THE ACT'S OWN FILES ARE VISIBLY PULLED
    ### RATHER THAN TYPED. ### The name is the discipline; the code is the same."""
    return pull(path, anchor, occurrence)


def present_exact(path, line):
    """### TRUE IFF SOME WHOLE LINE EQUALS `line` EXACTLY, AFTER STRIPPING."""
    return line.strip() in _lines(path)


def absent_exact(path, line):
    """### THE MUST-FAIL FIXTURE'S PRIMITIVE. ### TRUE IFF NO WHOLE LINE EQUALS `line`.
    ### ### **BECAUSE IT COMPARES WHOLE LINES, A STRING THAT IS MERELY A SUBSTRING OF A
    ### ### CORRECT SENTENCE CANNOT SATISFY IT. ### THAT IS THE b277 SPECIES, CLOSED.**"""
    return line.strip() not in _lines(path)
