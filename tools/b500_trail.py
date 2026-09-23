# -*- coding: utf-8 -*-
"""b500_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
HEADING = ('### b500 — the b498 build log read: exit 0, 57 modules built, all three profiles the '
           'standard three; (R82) HOLDS')

R = json.loads(io.open(os.path.join(D, 'b500_results.json'), encoding='utf-8').read())
body = """
%(h)s

**(R112) ratified.** The ladder's tail moves to the head of `(R104)`: the quadrature repair and the
ladder past sqrt(32) run before the identity is derived and before `h2` is stated as one Prop. The
numerical lane opens for b501 and b502 only and shuts at b502's close. This act, the b498 log read,
takes no place in the sequence. `W-ORD-QUADRATURE-BOUND` fires at b501 and
`W-ORD-EPSTEIN-ISOLATION` at b502, each priced on its face.

**COMPONENT 0.** pid 14280 **GONE**; no `lake` or `lean` process alive; the log %(bytes)d bytes, %(lines)d
lines. **Its content was not opened before the seal.**

**COMPONENT 1 — THE LOG, COMMITTED UNCHANGED**, sha256 `%(sha)s`. Both `END` lines **EXIT 0**.
**57 modules built, every one `Zeta23.*`, none `Mathlib.*`** — the cache b498 fetched did its work.
**Modules that failed, by name: NONE**; three lines carry the word *failed* inside `ring`'s
*"Try this: ring_nf"* `info:` advice and are not errors. Wall time %(wall).1f s from the log's own
marks; `lake`'s summed durations %(summ).1f s across %(spans)d spans — `lake` builds in parallel.

**COMPONENT 2 — THE PROFILES.** `Zeta23.WeilEF.EF_lit_zetaZeroConfig`, `Zeta23.EF.EF_lit` and
`Zeta23.WeilEF.EF_lit_zeta` each read **`[propext, Classical.choice, Quot.sound]`**, matched on the
whole axiom string. **`(R82)` HOLDS AT THIS RUN**, by its own words. **The first reading said ABSENT
for all three**, and was wrong: the axiom matcher carried from b497 was anchored at the start of a
line, while the launcher stamps an instant at the start of every line, so it could not match any real
run — b497's ABSENT was right only because b495's log held no probe output at all. Repaired, both
readings banked.

**COMPONENT 3.** One note appended at the end of REGISTRY restating the `PENDING` profile cell as the
three names and their profile; the `PENDING` paragraph is not edited. **The terminal table did not
move**: its reader takes a profile only from a print-output artefact committed inside the kernel's
own tree, and this act writes no kernel repository — so `EF_lit_zetaZeroConfig` reads `NOT PROFILED`
there while REGISTRY carries the banked profile. **Routed; the tool is not edited and no artefact is
written into the kernel to make it move.**

**(N1) HELD · (N2) HELD · (N3) HELD** (57 against a bar of seventy). The seat's own: **(S1) HELD,
(S2) HELD, (S3) HELD.** No grade conferred; no keystone cites the kernel; nothing at Zenodo written
by the seat outside (R110); nothing deposits; row U1 unedited; `h2` where the deposit left it; the
four lists stay OPEN.
""" % dict(h=HEADING, bytes=R['bytes'], lines=R['lines'], sha=R['sha256'], wall=R['wall_seconds'],
           summ=R['lake_summed'], spans=R['lake_spans'])
before = open(OT, 'rb').read()
if HEADING in before.decode('utf-8'):
    sys.exit('### ALREADY PRESENT')
open(OT, 'ab').write(body.encode('utf-8'))
after = open(OT, 'rb').read()
bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
removed = len(bl) - sum(1 for a, b in zip(al, bl) if a == b)
out = dict(bytes_added=len(after) - len(before), prefix=after.startswith(before), lines_removed=removed,
           headings=after.decode('utf-8').count(HEADING), esc=after.count(b'\x1b') - before.count(b'\x1b'))
msg = ('OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, %(lines_removed)d lines removed, '
       '%(headings)d heading, %(esc)d ESC bytes' % out)
print('  ' + msg)
io.open(os.path.join(D, 'b500_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(msg + NL)
