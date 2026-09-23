# -*- coding: utf-8 -*-
"""b495_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


HEADING = '### b495 — SIDE-explicit-formula created: 57 modules vendored, pushed, build launched'

BODY = """
%(heading)s

**(R106) ratified.** b494's Table 2 row 5 is corrected on the record — the Epstein sentence
**is** stated in the corpus, as prose at `A_Place_to_Stand` step (9) (*"the ingredient the
Epstein comparison isolates"*), with **no bank and no terminal**; its address is therefore
**PROSE, NO BANK**, and **`W-ORD-EPSTEIN-ISOLATION`** is filed: the four-channel ledger computed
for an Epstein zeta function with a known off-line zero, on the same ladder, so the sign of
`A − PR` at a non-ξ object is measured beside ξ's. Trigger: the ladder act of (R104), or the
author's word. **`C7_finite_type_false` is to be profiled in the next act that opens the
`SIDE-lv-conservation` lane**, and `OPEN_TRAILS` line 102 annotated by appended note, not
rewritten. And the creation of `SIDE-explicit-formula` is **two acts**: this one creates, pins,
copies, pushes and launches; the next reads the log and profiles. **No row cites the kernel
before the profile is banked.**

**THE PIN IS `v1.0` = `%(pin_sha)s`.** `EF_lit`'s statement was read at tag
`v1.0` and at `fbdc36b` and is **byte-identical** — sha256 `%(stmt)s`
— and so is the whole module. The order's rule selects the tag. **The first reading said
otherwise**: it reported the statement **NOT FOUND** at `v1.0` and would have pinned `fbdc36b`,
because at `v1.0` the tree is rooted at `Zeta23/` and by `fbdc36b` the `zeta23-palomar-layout`
merge has moved it under `zeta23/`. **A path miss is not a finding about the object**; the
module is now resolved in each revision's own tree and the path used is printed beside each
reading.

**THE KERNEL.** `SIDE-explicit-formula`, the **%(mods)d-module** local import closure of
`%(seed)s`, vendored from `anthropics/formal-math` at the pin. Every body byte-identical,
proved per module by a pair of digests — the source blob at the pin and the copied body **read
back from disk before any header was prepended** — agreeing at **%(agree)d of %(mods)d**; and
after the prepend every body was re-read from the file's tail and compared, **intact at %(mods)d
of %(mods)d**. `LICENSE` and `NOTICE` carried whole (Apache 2.0 §4), digests identical. **%(npnt)d**
modules under `Zeta23/FromPNTPlus/` carry a second header naming PrimeNumberTheoremAnd, **as
zeta23's own `NOTICE` names them — the predicate is the source's, not the seat's**; those files
already carry their own upstream notice, so they now hold **three attribution blocks of distinct
provenance**, which is correct and not a defect. Toolchain `%(toolchain)s` and mathlib
`%(mathlib)s`, **as zeta23 pins them** — rule 4's expected divergence, stated.

**PUSHED AND READ BACK.** `%(head)s`, local and `ls-remote` **AGREE**. The pre-push guard was
installed **before the first push the repository ever took** — into the **tracked** `.githooks/`
with `core.hooksPath`, byte-identical to relay's single source (R15). The first version of that
step wrote into `.git/hooks/` from a path that does not exist: **a cure that already had a tool,
reinvented** — caught by the crash.

**RULE 9 WAIVED FOR VENDORED NAMESPACES**, appended beside rule 9 in `SPIRAL_MAP` §7 with this
act as its reason, prefix proved, 0 lines removed. The waiver **names its boundary**: it lapses
the moment this programme edits a vendored body, and it is not retroactive to any kernel.

**ONE REGISTRY ROW, CITING NOTHING.** deposit-pin `NONE`, working-head the pushed SHA, source
zeta23 at the pin, **profile `PENDING`**. The no-citation claim is **measured**: the appended
block was scanned for terminal-shaped names and carries **0**. The one dotted name in it is the
vendoring seed, a module, named as the thing copied.

**THE BUILD IS LAUNCHED AND UNREAD** — pid `%(pid)d`, log `relay/data/b495_ef_build.log`. The
launcher stamps **an instant taken at each line, from the clock**; b480 precomputed one instant
and stamped every mark with it, so its log could not say how long anything took or in what order.
It profiles the three names **whether or not the build exits 0**, because a launcher that skips
the profile hands the next act nothing.

**TWO EXPECTATIONS ARE NOT SCORABLE IN THIS ACT, AND THAT IS THE FINDING.** (N3) and the seat's
(S2) both name **the log's first ten module marks**, and the same order says *"the log is not
read in this act."* Scoring them would break the clause; scoring them from anything else would
answer a different question. **The face did not see the conflict when it was sealed.** The
repair (N3) tests is shown at its mechanism instead — ten consecutive calls to the launcher's
own `stamp()` give ten distinct instants, `say()` calls it per line, and no precomputed
module-level stamp exists — but **the wording's own population is b496's cell to print.**

**NOTHING IS CITED, NOTHING IS GRADED, NOTHING IS PROFILED.** A vendored copy is not a result,
a push is not a verification, and **a launched build is not a built build**. Nothing deposits;
nothing at Zenodo is written; row U1 unedited; `h2` where the deposit left it; the four lists
stay OPEN.
"""


def main():
    pin = json.loads(read(os.path.join(D, 'b495_pin.json')))
    cre = json.loads(read(os.path.join(D, 'b495_create.json')))
    psh = json.loads(read(os.path.join(D, 'b495_push.json')))

    with open(OT, 'rb') as fh:
        before = fh.read()
    if HEADING in before.decode('utf-8', 'replace'):
        print('### ALREADY PRESENT -- REFUSING A SECOND RECORD.')
        return 2
    body = (BODY % dict(heading=HEADING, pin_sha=cre['pin_sha'],
                        stmt=pin['statement_sha'][cre['pin']], mods=cre['modules'],
                        seed=cre['seed'], agree=cre['agreeing'], npnt=len(cre['pnt']),
                        toolchain=cre['toolchain'], mathlib=cre['mathlib'][:12],
                        head=psh['head'][:7], pid=psh['pid'])).encode('utf-8')
    with open(OT, 'ab') as fh:
        fh.write(body)
    with open(OT, 'rb') as fh:
        after = fh.read()
    bl = before.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    al = after.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    removed = len(bl) - sum(1 for a, b in zip(al, bl) if a == b)
    out = dict(bytes_added=len(after) - len(before), prefix=after.startswith(before),
               lines_removed=removed, headings=after.decode('utf-8', 'replace').count(HEADING),
               before_sha=hashlib.sha256(before).hexdigest(),
               after_sha=hashlib.sha256(after).hexdigest())
    print('  OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, '
          '%(lines_removed)d lines removed, %(headings)d heading' % out)
    json.dump(out, io.open(os.path.join(D, 'b495_trail_notes.json'), 'w',
                           encoding='utf-8', newline=NL), indent=1)
    io.open(os.path.join(D, 'b495_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        ('OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, '
         '%(lines_removed)d lines removed, %(headings)d heading' % out) + NL)
    return 0 if (out['prefix'] and removed == 0 and out['headings'] == 1) else 1


if __name__ == '__main__':
    sys.exit(main())
