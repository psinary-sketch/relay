# -*- coding: utf-8 -*-
"""standing/v1362.py -- THE CONTROLS OF v1.36.2, (R368)(6): G-TRAIL-CARRIES-SEAL READS THE SEALED TOOLS FROM THE TRAIL BANK; THE KERNELS FACE
NAMES SIDE-dirichlet-mod-24. In v1360.py's form.

The ruling's words (relay data/b758_ferry.txt :19): "With them: G-TRAIL-CARRIES-SEAL (checks.tpl :1853) reads the tools' names from the trail
bank, where the ledger tool has written them since v1.35.0, its control b756's trail and b757's; the kernels face names
SIDE-dirichlet-mod-24." b757 events (29) (relay data/b758_events.txt :175-:181): the arm wanted "<tool> agree" in the trail record's text, where
tools/standing/ledgers.py (v1.35.0) writes the line by count and the rows by name in data/<act>_trail.json. v1.36.2: ledgers.seal_carried, the
arm's one reading (the bank's rows where it carries them, the text where it carries none), called by the arm at checks.tpl :1853; record.tpl
:634's kernels face list adds SIDE-dirichlet-mod-24. PLACE-papers lines are read and never printed.

  (b756)      b756's trail (no rows in its bank): the new reading True, the old reading True (b756's arm passed, relay data/b756_checks.txt :147).
  (b757)      b757's trail (173 rows in its bank): the new reading True; the old reading False, the failure of b757 events (29).
  (plant)     b757's bank with its first row turned differ, its first sealed tool's row removed, a row twice, and an act sealing nothing: False each.
  (checks)    checks.tpl rendered for every act at BASE's template and the working one: each render differing in the arm's two lines, its
              reading and its positive control (the line count equal), or raising alike at both (the carried failures), or the line covered by the act's own override; b758 among the first.
  (face)      record.tpl rendered likewise, each render differing in the face's one line; and the face's reader on SIDE-dirichlet-mod-24: its main
              and its tag v0.2.0 read.
  (version)   tools/standing/VERSION moved to v1.36.2.

  python -X utf8 -u tools/standing/v1362.py control [b756|b757|plant|checks|face|version ...] [--bank]
"""
import io
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '9bc8cfeb'   # ### the relay's HEAD before this change (b758 component 4, step 26, v1.36.1)
PP = 'D:/MY-DOwnloads/PLACE-papers'
M24 = 'SIDE-dirichlet-mod-24'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import ledgers as LG            # noqa: E402  (the working file: AFTER)
import v1340 as V               # noqa: E402  (show, free_line)


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def old_reading(sealed, tail):
    """the arm as it stood at BASE (checks.tpl :1853): every sealed tool's "<tool> agree" in the trail record's text."""
    return all(('%s agree' % t) in tail for t in sealed)


def sealed_of(act):
    """the tools the act sealed, by name, from its seal record (data/<act>_seal_hashes.json `tools`): the worklist's SEALED is computed at
    import from the tools on disk, so read today it carries the standing tools written after the act's seal (b756's: eleven)."""
    return tuple(sorted(json.load(io.open(os.path.join(D, '%s_seal_hashes.json' % act), encoding='utf-8'))['tools']))


def tail_of(act, tj):
    """OPEN_TRAILS at PLACE-papers HEAD from the trail bank's line to the next act's trail head (or the file's end): read, never printed."""
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:OPEN_TRAILS.md'], capture_output=True)
    L = r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL)
    i = int(tj['line']) - 1
    j = next((k for k in range(i + 1, len(L)) if L[k].startswith('### b7')), len(L))
    return NL.join(L[i:j]), L[i].startswith('### %s ' % act) or L[i].startswith('### %s —' % act)


def tj_of(act):
    return json.load(io.open(os.path.join(D, '%s_trail.json' % act), encoding='utf-8'))


def control_b756():
    L = ['### (b756): b756`S TRAIL, ITS BANK CARRYING NO ROWS']
    tj = tj_of('b756')
    sealed = sealed_of('b756')
    tail, head_ok = tail_of('b756', tj)
    o, n = old_reading(sealed, tail), LG.seal_carried(sealed, tail, tj)
    return L, case(L, 'b756', 'b756: sealed %d ; the bank`s rows %s ; the trail read from its bank`s line, the head there %s' % (
        len(sealed), 'none' if 'sealed' not in tj else len(tj['sealed']), head_ok), 'the old reading %s' % o, 'the new reading %s' % n,
        o and head_ok, n and 'sealed' not in tj), 1


def control_b757():
    L = ['### (b757): b757`S TRAIL, ITS BANK CARRYING THE ROWS']
    tj = tj_of('b757')
    sealed = sealed_of('b757')
    tail, head_ok = tail_of('b757', tj)
    o, n = old_reading(sealed, tail), LG.seal_carried(sealed, tail, tj)
    rows = tj.get('sealed') or []
    return L, case(L, 'b757', 'b757: sealed %d ; the bank`s rows %d, agreeing %d ; the head at the bank`s line %s' % (
        len(sealed), len(rows), sum(1 for r in rows if r.get('at_record') == 'agree'), head_ok),
        'the old reading %s (b757 events (29): failing, undeclared)' % o, 'the new reading %s' % n, (not o) and head_ok, n), 1


def control_plant():
    L = ['### (plant): b757`S BANK PLANTED FOUR WAYS']
    tj = tj_of('b757')
    sealed = sealed_of('b757')
    tail, _h = tail_of('b757', tj)
    rows = list(tj.get('sealed') or [])
    first = sealed[0]
    nm = LG.trail_name(first)
    differ = dict(tj, sealed=[dict(r, at_record='differ') if r.get('tool') == nm else r for r in rows])
    gone = dict(tj, sealed=[r for r in rows if r.get('tool') != nm])
    twice = dict(tj, sealed=rows + [r for r in rows if r.get('tool') == nm])
    got = [LG.seal_carried(sealed, tail, differ), LG.seal_carried(sealed, tail, gone), LG.seal_carried(sealed, tail, twice), LG.seal_carried((), tail, tj)]
    dup = LG.seal_carried(sealed + (first,), tail, tj)
    import re
    line = 'standing/act.py agree, acts/b757.py agree, b757_x.py differ, b757_y.py absent'
    same = LG.SEALED_ITEM.findall(line) == re.findall(r'([\w.-]+) (agree|differ|absent)\b', line)
    return L, case(L, 'plant', '%s (written %s) differ ; removed ; twice ; no sealed tool -- then the sealed list naming it twice ; the writer`s pattern '
                   'against BASE`s on a planted line' % (first, nm), 'n/a (the reading absent at BASE)', '%s ; %s ; %s' % (got, dup, same),
                   True, got == [False, False, False, False] and dup and same), 1


def _renders(kind, needle, want=1):
    t0 = V.show(BASE, 'tools/standing/fold/%s.tpl' % kind)
    t1 = io.open(os.path.join(S, 'fold', '%s.tpl' % kind), encoding='utf-8', newline='').read()
    acts = sorted(f[:-3] for f in os.listdir(os.path.join(T, 'acts')) if f.endswith('.py') and f[:1] == 'b')
    ones, alike, covered, bad = [], [], [], []
    for a in acts:
        e0 = e1 = None
        try:
            r0 = F.render(a, kind, tpl=t0).split(NL)
        except Exception as e:  # noqa: BLE001
            e0 = type(e).__name__
        try:
            r1 = F.render(a, kind, tpl=t1).split(NL)
        except Exception as e:  # noqa: BLE001
            e1 = type(e).__name__
        if e0 or e1:
            (alike if e0 and e1 and e0 == e1 else bad).append('%s %s/%s' % (a, e0, e1))
            continue
        dl = [i for i in range(min(len(r0), len(r1))) if r0[i] != r1[i]]
        if len(r0) == len(r1) and len(dl) == want and any(needle in r1[i] for i in dl):
            ones.append(a)
        elif len(r0) == len(r1) and not dl:
            covered.append(a)
        else:
            bad.append('%s lines %d/%d differing %d' % (a, len(r0), len(r1), len(dl)))
    return len(t0.split(NL)), len(t1.split(NL)), acts, ones, alike, covered, bad


def control_checks():
    L = ['### (checks): checks.tpl RENDERED FOR EVERY ACT AT BASE`S TEMPLATE AND THE WORKING ONE']
    n0, n1, acts, ones, alike, covered, bad = _renders('checks', 'seal_carried(K.SEALED, trail_tail(S), S[\'tj\'])', want=2)
    return L, case(L, 'checks', 'checks.tpl: lines %d at BASE, %d now ; acts %d' % (n0, n1, len(acts)), 'the line counts equal %s' % (n0 == n1),
                   'differing in the arm`s two lines, its reading and its positive control, %d (b758 among them %s) ; raising alike at both %d %s ; covered by the act %d %s ; others %s' % (
                       len(ones), 'b758' in ones, len(alike), [x.split()[0] for x in alike][:30], len(covered), covered, bad or 'NONE'),
                   n0 == n1, 'b758' in ones and not bad), 1


def control_face():
    L = ['### (face): record.tpl RENDERED LIKEWISE, AND THE FACE`S READER ON SIDE-dirichlet-mod-24']
    n0, n1, acts, ones, alike, covered, bad = _renders('record', "'SIDE-faces-join', 'SIDE-dirichlet-mod-24'")
    import b633_record as R3
    st = R3.kern_state([M24])[M24]
    return L, case(L, 'face', 'record.tpl: lines %d at BASE, %d now ; acts %d' % (n0, n1, len(acts)), 'the line counts equal %s' % (n0 == n1),
                   'differing in the face`s one line %d (b758 among them %s) ; raising alike %d ; covered %d %s ; others %s ; the reader on %s: main %s, '
                   'tags %s, tracked changes %r' % (len(ones), 'b758' in ones, len(alike), len(covered), covered, bad or 'NONE', M24, st[0],
                                                    sorted(st[1].items()), st[3]),
                   n0 == n1, 'b758' in ones and not bad and st[0] == 'e5ebdd1' and st[1].get('v0.2.0') == 'e5ebdd1'), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.1', ver == 'v1.36.2'), 1


CONTROLS = dict(b756=control_b756, b757=control_b757, plant=control_plant, checks=control_checks, face=control_face, version=control_version)
ORDER = ('b756', 'b757', 'plant', 'checks', 'face', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    F.install()
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.2, (R368)(6): G-TRAIL-CARRIES-SEAL READS THE TRAIL BANK; THE KERNELS FACE NAMES %s (%s)' % (
        act, M24, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'PLACE-papers lines read and not printed; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (the templates and tools at %s) and after (the working files)' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.36.2: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1362.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
