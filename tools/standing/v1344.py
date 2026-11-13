# -*- coding: utf-8 -*-
"""standing/v1344.py -- THE CONTROLS OF v1.34.4 ((R364)(5)[H1], passed as (a) on the author's word, relay data/b754_author_answers.txt
:131, 2026-11-13T23:08:49Z), in v1342.py's form: each instance read through the route as it stood at BASE (relay 19aa6a12, v1.34.3's own
commit, read from its blobs) and through the route on disk; AS WANTED where the old route fails the instance and the new passes it. THE
COMPILE CONTROL RUNS FIRST. The free memory is printed before each control. No write reaches the relay or PLACE-papers. Written at b754
by the Write tool; no identifier of the author is read into any string here.

  (handoff)  [H1]'s THE PAGE REGENERATED: tools/standing/handoff.py, its nine controls over banks planted in memory (the record's page
             under the cap with twelve acts; a ferry without THE ACT'S PLACE refused; the curly apostrophe found; a twin refused; a closing
             head refused; the quoting rule's word planted beside the Next, the Next cited; no trail heading refused; REGISTRY :373 without a
             heading refused; the cap refused).
  (count)    [H1]'s THE COUNT STOPPED: tools/standing/fold/closing.tpl :427 no longer runs tools/b307_handoff_census.py and :549 reads no
             census_closing bank; the faces and pins counts run as before; the template's line count equal at BASE and on disk; the
             template rendered for the act and compiled at both, through the compile control's route.
  (version)  tools/standing/VERSION moved to v1.34.4.

  python -X utf8 -u tools/standing/v1344.py control [handoff|count|version ...] [--bank]
"""
import io
import os
import re
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '19aa6a12'   # ### v1.34.3's own commit (b754 component 3, [U3]): the routes before this change
TPL = 'tools/standing/fold/closing.tpl'
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
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.3): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.4): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


# ================================================================================ (handoff)
def control_handoff():
    L, g, n = ['### (handoff): [H1]`S THE PAGE REGENERATED ((R364)(5)[H1] (a))'], 0, 0
    import handoff as HO
    at_base = show('tools/standing/handoff.py')
    ok, out = HO.control()
    L += ['      ' + x for x in out]
    n += 1
    g += case(L, 'handoff', 'HANDOFF.md written whole from the banks by one standing route, its needles refusing where missing',
              'tools/standing/handoff.py at BASE: %s' % ('PRESENT' if at_base else 'ABSENT, no route'),
              'tools/standing/handoff.py on disk: %s' % (out[-1].strip('# *.') if out else ''), not at_base, ok)
    return L, g, n


# ================================================================================ (count)
LOOP_B307 = re.compile(r"\('b307_handoff_census\.py'")
READ_CENSUS = re.compile("'⟪ACT⟫_census_closing\\.txt'")


def _code(text):
    """the template's lines that are not comments."""
    return [l for l in text.split(NL) if not l.lstrip().startswith('#')]


def _render(act, at=None):
    """the closing template rendered for the act by the fold and compiled, through the compile control's own route
    (tools/standing/compilecontrol.py check, at a revision's blobs or on disk): (ok, its detail). A first form of this case read the
    template's placeholders as names and compiled the raw text; that read failed at :146 at both revisions, the predicate's and not
    the template's (data/b754_defects.txt (r'))."""
    row = next((r for r in CC.check(act, at=at)['rows'] if r[0] == 'closing render'), None)
    return (row[1], row[2]) if row else (False, 'no closing render row')


def control_count():
    L, g, n = ['### (count): [H1]`S THE COUNT AGAINST THE PAGE STOPPED ((R364)(5)[H1] (a))'], 0, 0
    old = (show(TPL) or '').replace('\r', '')
    new = io.open(os.path.join(RELAY, *TPL.split('/')), encoding='utf-8').read().replace('\r', '')
    oc, nc = _code(old), _code(new)
    o_run, n_run = sum(1 for l in oc if LOOP_B307.search(l)), sum(1 for l in nc if LOOP_B307.search(l))
    o_read, n_read = sum(1 for l in oc if READ_CENSUS.search(l)), sum(1 for l in nc if READ_CENSUS.search(l))
    n += 1
    g += case(L, 'count', 'the close runs tools/b307_handoff_census.py and reads its bank: lines of code naming the run, the read',
              '%s at BASE: run %d, read %d' % (TPL, o_run, o_read), '%s on disk: run %d, read %d' % (TPL, n_run, n_read),
              o_run >= 1 and o_read >= 1, n_run == 0 and n_read == 0)
    kept = [k for k in ("('b327_faces_census.py'", "('b303_pins.py'", "'⟪ACT⟫_faces_census_closing.txt'", "'⟪ACT⟫_pins_closing.txt'")]
    ok_ = [all(any(k in l for l in nc) for k in kept), all(any(k in l for l in oc) for k in kept)]
    n += 1
    g += case(L, 'count', 'the faces and pins counts and their banks: each named in the code (the plain reading, as wanted at both)',
              'at BASE: %s' % ok_[1], 'on disk: %s' % ok_[0], True, ok_[0] and ok_[1])
    L[-3] = '      BEFORE (v1.34.3): at BASE: %s -> (the same at both is wanted)' % ok_[1]
    lo, ln = len(old.split(NL)), len(new.split(NL))
    n += 1
    g += case(L, 'count', 'the template`s line count (line-keyed overrides read it): equal at BASE and on disk',
              'lines at BASE %d' % lo, 'lines on disk %d' % ln, True, lo == ln and lo > 0)
    L[-3] = '      BEFORE (v1.34.3): lines at BASE %d -> (equal wanted)' % lo
    act = A.current().get('act')
    co, cn = _render(act, BASE), _render(act)
    n += 1
    g += case(L, 'count', 'the closing template rendered for %s by the fold and compiled (the compile control`s route)' % act,
              'at BASE: %s, %s' % co, 'on disk: %s, %s' % cn, True, co[0] and cn[0])
    L[-3] = '      BEFORE (v1.34.3): at BASE: %s, %s -> (rendering and compiling at both wanted)' % co
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.3', ver == 'v1.34.4')
    return L, g, n


CONTROLS = dict(handoff=control_handoff, count=control_count, version=control_version)
ORDER = ('handoff', 'count', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.4, (R364)(5)[H1] PASSED AS (a) (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
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
    out.append('### ### **v1.34.4: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1344.txt' % act), NL.join(out))
        print('written data/%s_standing_v1344.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
