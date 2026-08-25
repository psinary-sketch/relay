# -*- coding: utf-8 -*-
"""audit_emit.py -- THE AUDIT SIDECAR (built b153).

### WHY THIS EXISTS. Three times the record produced a false pass, and all three
### were ONE STRUCTURAL HOLE: the check and the thing checked were the same actor.
###   b146 -- a scanner EXCUSED a live use and reported CLEAN.
###   b148 -- a commit message ASSERTED its own compliance in the breaching act.
###   b151 -- a report CLAIMED an audit verdict for a check THAT WAS NEVER RUN.
### The first two were patched at their sites. ### THE THIRD CANNOT BE, because
### the defect is not in any tool -- IT IS THAT A REPORT'S AUDIT BLOCK IS PROSE,
### AND PROSE IS FREE.

### THE FIX MOVES THE AUTHORSHIP. An audit block was written BY THE ACTOR ABOUT
### THE TOOL. It is now WRITTEN BY THE TOOL and only EMBEDDED by the actor.
### A HAND-TYPED VERDICT IS THEREAFTER A VIOLATION, not a risk -- and detectable,
### because an embedded block with no matching sidecar is A FACT ABOUT FILES
### rather than a judgement about intent.

# ### THE REACH OF THIS MECHANISM, STATED IN ITS OWN HEADER BECAUSE A CHECK WHOSE
# ### REACH IS NOT STATED WILL BE TRUSTED BEYOND IT.
# ### IT CLOSES: a verdict typed into a report that no tool ever produced, and a
# ###   sidecar edited after emission (the self-hash catches that).
# ### IT DOES NOT CLOSE: a sidecar written by hand from scratch. Nothing here
# ###   distinguishes a fabricated sidecar from a real one -- the self-hash only
# ###   proves internal consistency, and a forger can compute a hash.
# ### SO THIS RAISES THE COST OF A FALSE AUDIT FROM ZERO TO DELIBERATE. It does
# ### not make one impossible, and the convention must not be cited as if it did.
"""
import hashlib
import io
import os
import re
import time

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
BEGIN = '=== AUDIT SIDECAR (emitted; do not retype) ==='
END = '=== END AUDIT SIDECAR ==='


def emit(tool, act, inputs, rows, verdict, path=None):
    """Write the tool's own audit block to a sidecar and return (text, path).

    ### THE ACTOR NEVER COMPOSES THIS TEXT. It is produced here from values the
    ### tool computed, and the report embeds it verbatim.
    """
    ts = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())
    body = [BEGIN]
    body.append('  tool      : %s' % tool)
    body.append('  act       : %s' % act)
    body.append('  run at    : %s (local)' % ts)
    for i in inputs:
        body.append('  input     : %s' % i)
    for k, v in rows:
        body.append('  %-9s : %s' % (k, v))
    body.append('  VERDICT   : %s' % verdict)
    core = "\n".join(body)
    digest = hashlib.sha256(core.encode('utf-8')).hexdigest()[:32]
    text = core + "\n  self-hash : sha256/32 %s\n%s\n" % (digest, END)

    if path is None:
        safe = re.sub(r'[^A-Za-z0-9_.-]', '_', '%s_%s' % (act, tool))
        path = os.path.join(DATA, 'audit_%s.txt' % safe)
    with open(path, 'wb') as f:
        f.write(text.encode('utf-8'))
    return text, path


def blocks_in(text):
    """Every audit block in a document, verbatim."""
    out = []
    i = 0
    while True:
        a = text.find(BEGIN, i)
        if a < 0:
            break
        b = text.find(END, a)
        if b < 0:
            break
        out.append(text[a:b + len(END)] + "\n")
        i = b + len(END)
    return out


def selfhash_ok(block):
    """### THE SELF-HASH CHECK. Catches a sidecar edited after emission."""
    m = re.search(r'\n  self-hash : sha256/32 ([0-9a-f]{32})\n', block)
    if not m:
        return False, 'no self-hash line'
    core = block[:m.start()]
    want = hashlib.sha256(core.encode('utf-8')).hexdigest()[:32]
    return (want == m.group(1)), ('recomputed %s' % want)
