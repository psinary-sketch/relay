# -*- coding: utf-8 -*-
"""standing/v1342.py -- THE CONTROLS OF v1.34.2 ((R364)(5)[Q], passed whole on the author's word, relay data/b754_author_answers.txt
:98, 2026-11-13T21:57:50Z), in v1341.py's form: each instance read through the route as it stood at BASE (relay c176c4ed, v1.34.1's own
commit, read from its blobs) and through the route on disk; AS WANTED where the old route fails the instance and the new passes it. THE
COMPILE CONTROL RUNS FIRST. The free memory is printed before each control. No write reaches the relay or PLACE-papers. Written at b754
by the Write tool; no identifier of the author is read into any string here.

  (originsearch)  [Q]'s THE ORIGIN SEARCH: tools/standing/originsearch.py, from the scripts of b753's waiver, its three controls (a line
                  known at the remote main found; a planted line not found; a figure found under other words) and the reach's own (a
                  paraphrase not found), over data/b753_* at the relay's origin/main.
  (version)       tools/standing/VERSION moved to v1.34.2.

  python -X utf8 -u tools/standing/v1342.py control [originsearch|version ...] [--bank]
"""
import io
import os
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'c176c4ed'   # ### v1.34.1's own commit (b754 component 1): the routes before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)


def show(rel):
    return V.show(BASE, rel)


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.1): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.2): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


# ================================================================================ (originsearch)
def control_originsearch():
    L, g, n = ['### (originsearch): [Q]`S THE ORIGIN SEARCH ((R364)(5)[Q])'], 0, 0
    import originsearch as OS
    at_base = show('tools/standing/originsearch.py')
    ok, out = OS.control()
    L += ['      ' + x for x in out]
    n += 1
    g += case(L, 'originsearch', 'a line`s words, figures and formulas sought in the remote main`s tree by one standing route',
              'tools/standing/originsearch.py at BASE: %s' % ('PRESENT' if at_base else 'ABSENT, no route'),
              'tools/standing/originsearch.py on disk: %s' % (out[-1].lstrip('# ') if out else ''), not at_base, ok)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.1', ver == 'v1.34.2')
    return L, g, n


CONTROLS = dict(originsearch=control_originsearch, version=control_version)
ORDER = ('originsearch', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.2, (R364)(5)[Q] PASSED WHOLE (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each change`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.34.2: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1342.txt' % act), NL.join(out))
        print('written data/%s_standing_v1342.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
