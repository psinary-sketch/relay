# -*- coding: utf-8 -*-
"""audit_verify.py -- THE CLOSING SEQUENCE'S NEW MEMBER (built b153).

### WHAT IT DOES: reads a REPORT, finds every audit block in it, and requires
### each to match a sidecar in data/ BYTE-FOR-BYTE, with its self-hash intact.

### WHY IT IS THE POINT OF THE WHOLE ACT. `audit_emit` alone would be a new
### HABIT: the actor could emit a sidecar and still type something else into the
### report. ### THIS IS THE MEMBER THAT MAKES IT A STRUCTURE, and the record has
### spent five acts learning that a discipline which must be exercised is not a
### structure that guarantees.

### THE THREE FAILURES IT REPORTS, AND THEY ARE DIFFERENT:
###   ORPHAN  -- a block in the report matching no sidecar. ### THIS IS THE b151
###              SHAPE: a verdict that no tool produced.
###   TAMPERED-- a block whose self-hash does not recompute. ### Emitted, then
###              edited.
###   UNUSED  -- a sidecar this act emitted that no report embeds. ### NOT a
###              failure: a check may be run without being quoted. Reported so
###              the operator can see what was run and not shown.

### THE UNUSED LIST IS SCOPED BY ACT (b155). Before that it took no account of
### which act a sidecar belonged to: run against one act's report it named every
### PRIOR act's sidecars as unused, so
### the list grew monotonically and would have become noise. ### A CHECK WHOSE
### OUTPUT BECOMES NOISE STOPS BEING READ, which is a slower version of the
### failure this file exists to prevent. With `--act X` the listing covers X and
### its suffixed companions (X-core, X-relay) and nothing older. ### MATCHING IS
### NEVER SCOPED -- only the reporting is; a block must still match SOME sidecar
### byte-for-byte, and an ORPHAN is an ORPHAN whatever act it claims.

Usage:
    python audit_verify.py <report.md> [<report.md> ...] [--act <name>]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_emit as AE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sidecars():
    out = {}
    if not os.path.isdir(AE.DATA):
        return out
    for fn in os.listdir(AE.DATA):
        if fn.startswith('audit_') and fn.endswith('.txt'):
            p = os.path.join(AE.DATA, fn)
            out[fn] = open(p, encoding='utf-8', errors='replace').read()
    return out


def act_of(fn):
    """audit_<act>_<tool>.txt -- the act field holds no underscore, tool names do."""
    return fn[len('audit_'):-len('.txt')].split('_', 1)[0]


def in_act(fn, act):
    a = act_of(fn)
    return a == act or a.startswith(act + '-')


def main(argv):
    act = None
    if '--act' in argv:
        i = argv.index('--act')
        act = argv[i + 1] if i + 1 < len(argv) else None
        argv = argv[:i] + argv[i + 2:]
    if not argv:
        print(__doc__)
        return 2
    side = sidecars()
    print("=" * 76)
    print("AUDIT-BLOCK VERIFICATION (audit_verify.py, b153)")
    print("=" * 76)
    print("  sidecars in data/ : %d" % len(side))
    fails, matched = 0, set()
    for rep in argv:
        text = open(rep, encoding='utf-8', errors='replace').read()
        blocks = AE.blocks_in(text)
        print("\n  report : %s" % os.path.basename(rep))
        print("  blocks : %d" % len(blocks))
        if not blocks:
            print("      (no audit blocks embedded)")
        for i, b in enumerate(blocks, 1):
            ok_hash, note = AE.selfhash_ok(b)
            hit = [fn for fn, s in side.items() if b.strip() in s.strip()]
            if not ok_hash:
                print("   %2d  ### TAMPERED -- self-hash does not recompute (%s)" % (i, note))
                fails += 1
            elif not hit:
                print("   %2d  ### ORPHAN -- no sidecar contains this block" % i)
                print("       ### THIS IS THE b151 SHAPE: a verdict no tool produced.")
                fails += 1
            else:
                print("   %2d  MATCHED  %s  (self-hash ok)" % (i, hit[0]))
                matched.update(hit)
    unused = sorted(set(side) - matched)
    if act is not None:
        before = len(unused)
        unused = [u for u in unused if in_act(u, act)]
        print("\n  UNUSED scoped to act '%s': %d in scope, %d older suppressed"
              % (act, len(unused), before - len(unused)))
    if unused:
        print("\n  UNUSED sidecars (run but not embedded) — not a failure:")
        for u in unused:
            print("      %s" % u)
    print("\n  ### VERDICT: %s" % ("CLEAN" if not fails else "FAIL (%d)" % fails))
    print("  ### REACH: this cannot detect a sidecar written by hand from scratch.")
    print("  ### It raises the cost of a false audit from zero to deliberate.")
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
