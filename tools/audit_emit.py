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

### THE RETENTION REPAIR (b156). Until now the sidecar path was one file per
### act-and-tool, so A SECOND RUN OVERWROTE THE FIRST. ### THE RUN A RECORD MOST
### NEEDS IS THE ONE THAT FAILED, AND THAT WAS EXACTLY THE RUN THE TOOL DISCARDED.
### b155 IS THE FOUNDING INSTANCE: its vocabulary review returned NOT CLEAN with
### three live uses in the executor's own prose, the prose was corrected, and the
### passing re-run erased the failing sidecar. The failure survived only because
### the executor chose to write it down.
### THE AMENDED CONVENTION LINE: ### A TOOL THAT DISCARDS ITS OWN FAILURES KEEPS A
### RECORD OF SUCCESSES, NOT OF RUNS.
### THE FIX: paths are RUN-UNIQUE AND APPEND-ONLY. The first run of an act-tool
### pair keeps the plain name (so every earlier sidecar and every shipped report
### that embeds one is untouched); each later run takes `_r2`, `_r3`, ... ### NO
### EMISSION EVER OVERWRITES AN EARLIER ONE. The report embeds THE SHIPPING RUN;
### the act record lists ALL runs for the act, the superseded ones appearing as
### UNUSED, which the verifier already reports and correctly does not call a
### failure.
### ITS REACH, STATED: this preserves runs that HAPPEN. ### IT CANNOT PRESERVE A
### RUN THAT WAS NEVER EMITTED, and it is not retroactive -- b155's lost sidecar
### stays lost, because reconstructing it by hand would be precisely the forgery
### the paragraph above says this mechanism cannot detect.
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
        path = next_path(act, tool)
    with open(path, 'wb') as f:
        f.write(text.encode('utf-8'))
    return text, path


def next_path(act, tool):
    """### RUN-UNIQUE AND APPEND-ONLY (b156). The first run of an act-tool pair
    keeps the plain name -- so every sidecar already on disk, and every shipped
    report embedding one, is untouched -- and each later run takes the next free
    `_r<n>`. ### NOTHING IS EVER OVERWRITTEN.
    """
    safe = re.sub(r'[^A-Za-z0-9_.-]', '_', '%s_%s' % (act, tool))
    base = os.path.join(DATA, 'audit_%s.txt' % safe)
    if not os.path.exists(base):
        return base
    n = 2
    while True:
        cand = os.path.join(DATA, 'audit_%s_r%d.txt' % (safe, n))
        if not os.path.exists(cand):
            return cand
        n += 1


def runs_for(act, tool=None):
    """Every sidecar on disk belonging to an act (optionally one tool), in run
    order. ### THE ACT RECORD LISTS ALL RUNS; THE REPORT EMBEDS THE SHIPPING ONE."""
    if not os.path.isdir(DATA):
        return []
    out = []
    for fn in sorted(os.listdir(DATA)):
        if not (fn.startswith('audit_') and fn.endswith('.txt')):
            continue
        stem = fn[len('audit_'):-len('.txt')]
        a = stem.split('_', 1)[0]
        if a != act:
            continue
        if tool is not None and not stem.startswith('%s_%s' % (act, tool)):
            continue
        n = 1
        m = re.search(r'_r(\d+)$', stem)
        if m:
            n = int(m.group(1))
        out.append((n, fn))
    return [fn for _, fn in sorted(out)]


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
