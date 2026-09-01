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
