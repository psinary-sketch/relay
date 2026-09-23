# -*- coding: utf-8 -*-
"""b498_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
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


HEADING = ('### b498 — the build re-launched in its own console, with the cache; '
           'the cause banked and its sender not established')


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def body(R, SC):
    c1, c2, c3 = R['c1'], R['c2'], R['c3']
    if c2.get('closure_run'):
        closure = ('`lake build` on the **%d** external `Mathlib.*` roots of the vendored library '
                   '(computed from its import lines): exit **%d**, wall **%.1f s**; lines reading '
                   '`Built Mathlib.` **%d**, `Replayed Mathlib.` %d. **Replayed is not compiled.**'
                   % (len(c2['closure_roots']), c2['closure_exit'], c2['closure_wall'],
                      c2['built_mathlib'], c2['replayed_mathlib']))
    else:
        closure = ('**The cache was unavailable**, so the closure build did not run in the '
                   'foreground; b475\'s build, as b491 read it: %s' % c2.get('b475_line'))
    return """
%(heading)s

**(R109) ratified.** (1) The three titles are reworded as the navigator drafted them on
2026-09-23 and the author accepted; the five EXCEEDS and two RESTS sentences take the texts of
`zenodo_edits_2026-09-23.txt`; (R102)'s whole-disposition condition is met and the platform session
is the author's. **An ERRATA entry recording the ten edits is filed by the act that fetches them
back; nothing is filed before** — so this act files none. (2) The build is re-launched in its own
process group and console, with Mathlib's compiled cache fetched before `lake build`.

**COMPONENT 1 — THE CAUSE.** b495's launcher was created `CREATE_NEW_PROCESS_GROUP |
DETACHED_PROCESS` — **its own process group, and no console at all**, so it shared neither with the
seat. It started `lake` and `lean` with no creation flags, and Windows' documented behaviour gives a
console program started from a console-less parent **a new console of its own** — that is Windows'
behaviour applied to the flags, not a finding of the record. Both exits `0xC000013A`; **the launcher
survived both** and wrote its own closing line. In the order's clock: the kill is at **14:17:43
local** (18:17:43.807 UTC), inside the order's "at or before 15:02" on the local reading; on a UTC
reading the build had not started by 15:02. From the seat's session transcript: **no tool call by
the seat at either kill instant**, the last one %(lastgap).1f s before the first kill, and **the seat's
b495 turn ended %(te).3f s before it.** **What the record does not show: who or what sent the console
control event. The sender stays NOT ESTABLISHED**; the two kills fall %(apart).1f s apart on two
separate child consoles, which is consistent with a window being closed and is not evidence that one
was.

**COMPONENT 2 — THE CACHE.** `lake exe cache get`: exit **%(cexit)s**, wall %(cwall).1f s; **files
fetched %(fetched)s** — `%(fline)s`. *(The cache directory already held 121141 files before the act,
so this counts what was missing, not what the build needs.)* %(closure)s The kernel's tracked tree
after: %(kstat)s.

**COMPONENT 3 — THE LAUNCH.** `tools/b498_launch.py`, **pid %(pid)d**, creation flags **0x%(flags)08X =
%(fnames)s** — a new console and a new process group, **not** `DETACHED_PROCESS`, so `lake` and `lean`
inherit ONE console, started minimised and titled *"DO NOT CLOSE THIS WINDOW"*. Log
`relay/%(log)s`, each line stamped at the line. **The log is not read in this act and not committed**
— a running process owns it; the act after reads it behind b497's gate. `LEAN_NUM_THREADS` not set.

**(N1) %(n1)s** · **(N2) %(n2)s** · **(N3) %(n3)s**. **(N3)'s cell says less than it seems to:
b495's launcher also had a new process group, and was killed anyway.** The seat's own: **(S1) %(s1)s,
(S2) %(s2)s, (S3) %(s3)s.**

Nothing cited, nothing graded, no profile read; **nothing at Zenodo written by the seat**; no ERRATA
line; nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN;
K1, K2 and K3 not started.
""" % dict(
        heading=HEADING, lastgap=(R['c1_lastgap']), te=c1['kill_after_turn_end_s'],
        apart=R['c1_apart'], cexit=c2['cache_exit'], cwall=c2['cache_wall'],
        fetched=c2['fetched'] if c2['fetched'] is not None else 'NOT FOUND',
        fline=c2.get('fetched_line') or 'no Downloaded line', closure=closure,
        kstat=('clean' if c2.get('kernel_status') == '' else '`%s`' % c2.get('kernel_status')),
        pid=c3['pid'], flags=c3['flags'], fnames=' | '.join(c3['flag_names']), log=c3['log'],
        n1=w(SC['n1']), n2=w(SC['n2']), n3=w(SC['n3']), s1=w(SC['s1']), s2=w(SC['s2']),
        s3=w(SC['s3']))


def main():
    from datetime import datetime
    R = json.loads(read(os.path.join(D, 'b498_results.json')))
    SC = json.loads(read(os.path.join(D, 'b498_scores.json')))
    e = R['c1']['ends']
    f = lambda t: datetime.strptime(t[:23], '%Y-%m-%dT%H:%M:%S.%f')
    R['c1_apart'] = (f(e[-1]['t']) - f(e[0]['t'])).total_seconds()
    R['c1_lastgap'] = (f(e[0]['t']) - f(R['c1']['last_tool_call'])).total_seconds()
    with open(OT, 'rb') as fh:
        before = fh.read()
    if HEADING in before.decode('utf-8', 'replace'):
        print('### ALREADY PRESENT -- REFUSING A SECOND RECORD.')
        return 2
    b = body(R, SC).encode('utf-8')
    with open(OT, 'ab') as fh:
        fh.write(b)
    with open(OT, 'rb') as fh:
        after = fh.read()
    bl = before.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    al = after.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    removed = len(bl) - sum(1 for a, c in zip(al, bl) if a == c)
    out = dict(bytes_added=len(after) - len(before), prefix=after.startswith(before),
               lines_removed=removed, headings=after.decode('utf-8', 'replace').count(HEADING),
               before_sha=hashlib.sha256(before).hexdigest(),
               after_sha=hashlib.sha256(after).hexdigest())
    msg = ('OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, '
           '%(lines_removed)d lines removed, %(headings)d heading' % out)
    print('  ' + msg)
    json.dump(out, io.open(os.path.join(D, 'b498_trail_notes.json'), 'w',
                           encoding='utf-8', newline=NL), indent=1)
    io.open(os.path.join(D, 'b498_trail_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(msg + NL)
    return 0 if (out['prefix'] and removed == 0 and out['headings'] == 1) else 1


if __name__ == '__main__':
    sys.exit(main())
