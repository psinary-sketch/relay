# -*- coding: utf-8 -*-
"""tools/b753_lockgate.py -- b753: THE LOCK GATE RUN WITH THE AUTHOR'S LIFT (data/b753_events.txt (7); data/b753_put_3.json, option 1, the
author's answer at 2026-11-12T00:14:58.306Z, and the author's word with it, (1)-(2)).

b378's gate (tools/b378_lockgate.py) is imported and run unedited, except that the standing reader of (R345)(2)(iv) it calls
(tools/standing/repaircommits.py outside()) is read through a wrapper that leaves out the two commits the v1.33.0 bank names, 0f31d31d and
0db31ce3 (data/b753_standing_v1330.txt :107-:111); every other commit the reader returns stands, and the gate's after-the-gate reader is not
touched. Before the gate runs, the two controls the author's word (2) orders, printed into the gate's notes through the gate's own recorder:
  (A) with nothing left out, the (R345)(2)(iv) reading refuses on 0f31d31d and 0db31ce3 and on no other commit;
  (B) with the two left out and a third id planted in the list of standing commits the reader returns, the reading still refuses, naming
      the planted one.
A control not as wanted refuses the run before the gate is called: nothing written. The version stays v1.33.0 and no standing tool changes.
Written by the Write tool; committed before its run ((R363) N2, each generator commits before it runs).

  python -X utf8 -u tools/b753_lockgate.py b753 data/b753_registration_2026-11-11.txt
"""
import os
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.append(os.path.join(T, 'standing'))
import repaircommits as R   # noqa: E402  -- the same module object the gate imports inside its main()
import b378_lockgate as G   # noqa: E402  -- imported, not run: its main() is called below, unedited

COVERED = ('0f31d31d', '0db31ce3')   # ### the two commits the v1.33.0 bank names, by the author's lift
PLANTED = ('fe11ed00', 'PLANTED: a third commit touching tools/standing/ with VERSION unmoved')
_outside = R.outside


def leave_out(rows, covered=COVERED):
    """the reader's rows less the covered commits, every other row kept in order."""
    return [x for x in rows if x[0][:8] not in covered]


def version_commit():
    """the version commit as the gate reads it (tools/b378_lockgate.py :235)."""
    return subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%h', '--', 'tools/standing/VERSION'], capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def controls(act):
    ver = version_commit()
    late = R.after_gate(act) if hasattr(R, 'after_gate') else []
    whole = _outside(ver) + late                                   # ### the gate's own stray list, nothing left out
    a_ok = sorted(h[:8] for h, _s in whole) == sorted(COVERED)
    planted = leave_out(_outside(ver) + [PLANTED]) + late          # ### the two left out, a third id planted among the reader's rows
    b_ok = bool(planted) and [h for h, _s in planted] == [PLANTED[0]]
    L = ['  ### THE AUTHOR`S LIFT AT THE LOCK (data/b753_events.txt (7); data/b753_put_3.json, option 1, 2026-11-12T00:14:58.306Z):',
         '  ### the (R345)(2)(iv) reading leaves out %s, the two commits the v1.33.0 bank names (data/b753_standing_v1330.txt :107-:111);' % ' and '.join(COVERED),
         '  ### b378`s gate otherwise unedited; the version commit read %s; the after-the-gate reading %s.' % (ver, late or 'NONE'),
         '  ### THE CONTROLS OF THE AUTHOR`S WORD (2), BEFORE THE GATE:',
         '    (A) nothing left out: the reading refuses on %s ; wanted 0f31d31d and 0db31ce3 and no other ; %s' % (
             [h[:8] for h, _s in whole] or 'NONE', 'AS WANTED' if a_ok else '### NOT AS WANTED'),
         '    (B) the two left out, %s planted: the reading refuses on %s ; wanted the planted one alone ; %s' % (
             PLANTED[0], [h for h, _s in planted] or 'NONE', 'AS WANTED' if b_ok else '### NOT AS WANTED'),
         '  ### ### **THE LIFT`S CONTROLS : %s**' % ('2 OF 2 AS WANTED' if a_ok and b_ok else '### NOT AS WANTED -- THE GATE NOT RUN, NOTHING WRITTEN'),
         '']
    return a_ok and b_ok, L


def lifted(version_commit_, tip='HEAD'):
    rows = _outside(version_commit_, tip)
    kept = leave_out(rows)
    G.rec('  ### THE LIFT READ HERE: the reader returned %s ; left out %s ; kept %s' % (
        [h for h, _s in rows] or 'NONE', [h for h, _s in rows if h[:8] in COVERED] or 'NONE', [h for h, _s in kept] or 'NONE'))
    return kept


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] != 'b753':
        print('usage: b753_lockgate.py b753 <face> -- this act`s tool, for b753 alone; nothing read, nothing written')
        return 2
    ok, L = controls(argv[0])
    if not ok:
        print('\n'.join(L))
        return 2
    for ln in L:
        G.rec(ln)
    R.outside = lifted
    return G.main(argv)


if __name__ == '__main__':
    sys.exit(main())
