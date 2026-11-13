# -*- coding: utf-8 -*-
"""standing/v1343.py -- THE CONTROLS OF v1.34.3 ((R364)(5)[U3], passed on the author's word, relay data/b754_author_answers.txt :118,
2026-11-13T22:51:19Z; the row data/b754_rules.txt (12)), in v1342.py's form: each instance read through the route as it stood at BASE (relay
184da293, v1.34.2's own commit, read from its blobs) and through the route on disk; AS WANTED where the old route fails the instance and the
new passes it. THE COMPILE CONTROL RUNS FIRST. The free memory is printed before each control. No write reaches the relay or PLACE-papers:
the guard is read over texts given, and tools/standing/prelock.py's gate, which writes its bank, is read by its source and not run. Written
at b754 by the Write tool; no identifier of the author is read into any string here.

  (refusals)  [U3]'s REFUSALS BY KIND: tools/standing/counter.py's reader, line and guard (refusal_kinds, refusals_line, refusals_guard,
              refusals_gate) and tools/standing/prelock.py's gate reading the guard: b754's bank counted against an independent split; a
              planted b755 with a kind above b754's count and no event (refused), with its event (clear), with the refusal lettered in the
              defects bank (refused), with the act module naming the line once (refused); b754 itself read and not refused (from b755).
  (version)   tools/standing/VERSION moved to v1.34.3.

  python -X utf8 -u tools/standing/v1343.py control [refusals|version ...] [--bank]
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
BASE = '184da293'   # ### v1.34.2's own commit (b754 component 3, [Q]): the routes before this change
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


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else ''


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.2): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.3): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


# ================================================================================ (refusals)
def control_refusals():
    L, g, n = ['### (refusals): [U3]`S REFUSALS BY KIND ((R364)(5)[U3])'], 0, 0
    import counter as CN
    old_reader = 'def refusals_gate' in (show('tools/standing/counter.py') or '')
    old_gate = 'refusals_gate' in (show('tools/standing/prelock.py') or '')
    gate_old = 'tools/standing/prelock.py at BASE: %s' % ('a guard' if old_gate else 'NO GUARD, its gate clear on the instance')

    # (1) b754's bank, by the reader and by an independent split of each row on " | "
    t4, t3 = rd('b754_hook_refusals.txt'), rd('b753_hook_refusals.txt')
    k4 = CN.refusal_kinds(t4)
    ind = {}
    for l in t4.split(NL):
        p = l.split(' | ')
        if len(p) >= 3 and re.match(r'^\d{4}-\d\d-\d\dT', p[0]):
            ind[p[1]] = ind.get(p[1], 0) + 1
    L.append('      ' + CN.refusals_line('b754', 'b753', k4, CN.refusal_kinds(t3)))
    n += 1
    g += case(L, 'refusals', 'b754`s refusals bank counted by kind, beside b753`s: the reader against an independent split of each row',
              'counter.py at BASE: %s' % ('a reader' if old_reader else 'NO READER, no count by kind'),
              'refusal_kinds %s ; the split %s ; equal %s' % (k4, ind, k4 == ind), not old_reader, k4 == ind and sum(k4.values()) > 0)

    # (1b) the line read from the banks prints the letters the defects bank holds: the seat's own first form printed "none lettered" whatever
    # ### the banks held (found by the hand read of this bank's first unbanked run, 22:58Z)
    lb = CN.refusals_line('b754')
    want_l = CN._lettered('b754', rd('b754_defects.txt'))
    L.append('      ' + lb)
    n += 1
    g += case(L, 'refusals', 'the line read from b754`s banks: its lettered clause equal to the defect rows citing the refusals bank',
              'counter.py at BASE: %s' % ('a line' if old_reader else 'NO LINE'),
              'rows citing the bank %d ; the line prints "lettered %d" %s ; "none lettered" printed %s' % (
                  len(want_l), len(want_l), ('lettered %d,' % len(want_l)) in lb, 'none lettered' in lb),
              not old_reader, bool(want_l) and ('lettered %d,' % len(want_l)) in lb and 'none lettered' not in lb)

    # (2)-(5) a planted b755: one PIPE refusal where the planted b754 carries none
    PL = '2026-11-14T10:00:00Z | PIPE | Bash | "a planted command" | a planted refusal' + NL
    EV = '    (1) THE HOOK`S [CLOSE ; NEW]: A KIND ABOVE b754`S COUNT, PIPE 1 against 0 (data/b755_hook_refusals.txt :1).' + NL
    DF = ('    (a) THE SEAT`S [CLOSE ; NEW]: a listing sent with a pipe (refused, PIPE, data/b755_hook_refusals.txt :1), refused before it ran.' + NL)
    M2 = 'entry: CN.refusals_line(a, b, c, d)' + NL + 'trail: CN.refusals_line(a, b, c, d)' + NL
    M1 = 'entry: CN.refusals_line(a, b, c, d)' + NL
    for what, ev, df, mod, want in (
            ('a planted b755: PIPE 1 above b754`s 0, no event naming it', '', '', M2, False),
            ('a planted b755: the same, an event row naming PIPE and the bank, no letter, the module naming the line twice', EV, '', M2, True),
            ('a planted b755: the same, the refusal lettered (a) in the defects bank', EV, DF, M2, False),
            ('a planted b755: the same, no letter, the act module naming the line once', EV, '', M1, False)):
        ok_, lines_ = CN.refusals_guard('b755', 'b754', PL, '', ev, df, mod)
        L += ['      ' + x.strip() for x in lines_]
        n += 1
        g += case(L, 'refusals', what, gate_old, 'the guard %s, wanted %s' % ('CLEAR' if ok_ else 'NOT CLEAR', 'CLEAR' if want else 'NOT CLEAR'),
                  not old_gate, ok_ == want)

    # (6) b754 itself: read and printed, refusing nothing (from b755)
    ok4, l4 = CN.refusals_gate('b754')
    L += ['      ' + x.strip() for x in l4]
    n += 1
    g += case(L, 'refusals', 'b754 itself, its refusals lettered under the rule before it: read, printed and not refused',
              gate_old, 'the gate %s ; NOT IN FORCE printed %s' % (ok4, any('NOT IN FORCE AT b754' in x for x in l4)),
              not old_gate, ok4 and any('NOT IN FORCE AT b754' in x for x in l4))

    # (7) the pre-lock gate reads the guard into its verdict (its source; the gate writes its bank and is not run here)
    src = io.open(os.path.join(S, 'prelock.py'), encoding='utf-8').read()
    reads = 'CN.refusals_gate(act)' in src and 'and rf_ok' in src
    n += 1
    g += case(L, 'refusals', 'tools/standing/prelock.py`s gate: the guard`s lines in its bank and its verdict in CLEAR', gate_old,
              'refusals_gate called %s ; rf_ok in the verdict %s' % ('CN.refusals_gate(act)' in src, 'and rf_ok' in src), not old_gate, reads)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.2', ver == 'v1.34.3')
    return L, g, n


CONTROLS = dict(refusals=control_refusals, version=control_version)
ORDER = ('refusals', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.3, (R364)(5)[U3] PASSED (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
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
    out.append('### ### **v1.34.3: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1343.txt' % act), NL.join(out))
        print('written data/%s_standing_v1343.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
