# -*- coding: utf-8 -*-
"""standing/v1366.py -- THE CONTROLS OF v1.36.6, (R369)(4)(iv): THE SUITE'S READER OF THE KERNELS FACE NAMES SIDE-dirichlet-mod-24, in
v1363.py's form.

The ruling's words (relay data/b759_ferry.txt :15): "(iv) THE SUITE'S READER OF THE KERNELS FACE (tools/standing/fold/checks.tpl :611)
names SIDE-dirichlet-mod-24; its control b758's face read as 24 kernels." b758 defect (f) (relay tools/acts/b758.py :1121-:1127): v1.36.2
taught the face's writer (record.tpl :634) to name SIDE-dirichlet-mod-24 and not the reader (checks.tpl :611), so G-KERNELS-UNTOUCHED's
first clause (tools/b703_checks.py :1349, sorted(face) == sorted(kerns_read)) failed at b758, 24 against 23; b758's module overrode :611
by its mark (f8d771e18f03) and b759's carried the override.

WHERE THE LINE STANDS: tools/standing/fold.py finds an override by the mark of the template lines it covers and refuses a render whose
mark is found other than once (:149-:155, "an edit of them refuses"); the standing dry reads a render compiling at HEAD's templates and
failing at the working ones NOT CLEAN (standingdry.py :111-:117), and the one-call tool refuses a standing commit on that verdict
(commit.py). An edit of :611's bytes therefore refuses b758's sealed render: case (route611). v1.36.6 names SIDE-dirichlet-mod-24 in the
reader's list on :663, the line after the state's dict that completes it (S['kerns_read'], the list b703's arm reads), in place, the
line count kept; :611's bytes unchanged.

  (face)      b758's face (data/b758_kernels_face.json) read as 24 kernels: the reader's list as the template builds it (:611, then :663) with
              the writer's own _kerns (b703's list): BEFORE 23, SIDE-dirichlet-mod-24 absent; AFTER 24, equal to the face's names.
  (arm)       b703_checks.kernels_untouched over b758's face, the kernels read unchanged: BEFORE False (b758 defect (f)), AFTER True.
  (route611)  the ruling's line edited in a planted template (:611's list in the writer's form): b758's checks render refused, its override's
              mark found 0 times; at the working template b758's render stands.
  (renders)   checks.tpl rendered for every act at BASE's template and the working one: each differing in :663 alone (the line count
              equal), or raising alike at both; b758 and b759, their overrides at :611, among the first.
  (version)   tools/standing/VERSION moved to v1.36.6.

  python -X utf8 -u tools/standing/v1366.py control [face|arm|route611|renders|version ...] [--bank]
"""
import io
import json
import os
import re
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '34452b1a'   # ### the relay's HEAD before this change (b759 component 2, step 11, v1.36.5)
FJ, M24 = 'SIDE-faces-join', 'SIDE-dirichlet-mod-24'
NEEDLE = "S['kerns_read'] = list(dict.fromkeys(S['kerns_read'] + ['SIDE-dirichlet-mod-24']))"
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def tpls():
    if 't0' not in _MEMO:
        _MEMO['t0'] = V.show(BASE, 'tools/standing/fold/checks.tpl')
        _MEMO['t1'] = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8', newline='').read()
    return _MEMO['t0'], _MEMO['t1']


def face758():
    return json.load(io.open(os.path.join(D, 'b758_kernels_face.json'), encoding='utf-8')).get('kernels') or {}


def kerns():
    """the writer's _kerns: record.tpl :630 binds b703's list (b698's R._kerns rebound by b703's import)."""
    if 'k' not in _MEMO:
        import b703_record as B3
        _MEMO['k'] = list(B3._kerns())
    return _MEMO['k']


class _Rec(object):
    @staticmethod
    def _kerns():
        return list(kerns())


def reader(tpl):
    """the reader's list as the template builds it for b758: :611's kerns_read expression, then any statement of the template setting
    S['kerns_read'] after the dict (:663 at v1.36.6), each evaluated with the writer's _kerns; nothing else of the template run."""
    lines = tpl.replace('\r', '').split(NL)
    l611 = next(l for l in lines if 'kerns_read=' in l and 'kern_face=' in l)
    expr = re.search(r'kerns_read=(.*?),\s*$', l611).group(1)
    st = dict(kerns_read=eval(expr, dict(REC=_Rec)))   # noqa: S307
    for l in lines:
        m = re.search(r"S\['kerns_read'\] = (list\(dict\.fromkeys\(S\['kerns_read'\] \+ \[[^\]]*\]\)\))", l)
        if m:
            st['kerns_read'] = eval(m.group(1), dict(S=st))   # noqa: S307
    return st['kerns_read'], tpl.replace('\r', '').split(NL).index(l611) + 1


def control_face():
    L = ['### (face): b758`S FACE READ AS 24 KERNELS']
    f = face758()
    t0, t1 = tpls()
    (r0, n0), (r1, n1) = reader(t0), reader(t1)
    writer = list(dict.fromkeys(kerns() + [FJ, M24]))
    return L, case(L, 'face', 'data/b758_kernels_face.json: %d kernels ; the writer`s list (record.tpl :634) over b703`s _kerns %d, equal to the face %s' % (
        len(f), len(writer), writer == list(f)),
                   'the reader (:%d) %d, %s %s' % (n0, len(r0), M24, 'present' if M24 in r0 else 'absent'),
                   'the reader (:%d, then :663) %d, %s %s ; equal to the face`s names %s' % (n1, len(r1), M24, 'present' if M24 in r1 else 'absent',
                                                                                         sorted(r1) == sorted(f)),
                   len(f) == 24 and writer == list(f) and len(r0) == 23 and M24 not in r0,
                   len(r1) == 24 and sorted(r1) == sorted(f)), 1


def control_arm():
    L = ['### (arm): G-KERNELS-UNTOUCHED (b703_checks.kernels_untouched) OVER b758`S FACE']
    import copy
    import b703_checks as C3
    f = face758()
    t0, t1 = tpls()
    a0 = C3.kernels_untouched(dict(kern_face=f, kern_now=copy.deepcopy(f), kerns_read=reader(t0)[0]))
    a1 = C3.kernels_untouched(dict(kern_face=f, kern_now=copy.deepcopy(f), kerns_read=reader(t1)[0]))
    moved = copy.deepcopy(f)
    k0 = sorted(moved)[0]
    moved[k0] = ['planted'] + list(moved[k0])[1:] if isinstance(moved[k0], list) else 'planted'
    a2 = C3.kernels_untouched(dict(kern_face=f, kern_now=moved, kerns_read=reader(t1)[0]))
    return L, case(L, 'arm', 'the kernels read unchanged from the face ; then one kernel planted moved', 'reads %s (b758 defect (f): 24 against 23)' % a0,
                   'reads %s ; with %s planted moved %s' % (a1, k0, a2), a0 is False, a1 is True and a2 is False), 1


def control_route611():
    L = ['### (route611): THE RULING`S LINE EDITED IN A PLANTED TEMPLATE']
    t0, t1 = tpls()
    lines = t0.splitlines(keepends=True)
    i = next(k for k, l in enumerate(lines) if 'kerns_read=' in l and 'kern_face=' in l)
    planted = ''.join(lines[:i] + [lines[i].replace("kerns_read=list(dict.fromkeys(REC._kerns())) + ['SIDE-faces-join'],",
                                                    "kerns_read=list(dict.fromkeys(REC._kerns() + ['SIDE-faces-join', 'SIDE-dirichlet-mod-24'])),")] + lines[i + 1:])
    out = {}
    for nm, t in (('planted', planted), ('working', t1)):
        try:
            F.render('b758', 'checks', tpl=t)
            out[nm] = 'renders'
        except Exception as e:  # noqa: BLE001
            out[nm] = '%s: %s' % (type(e).__name__, str(e)[:120])
    marks = [m for (mk, _c, _t) in (F.overrides('b758').get('checks') or []) for m in [mk] if isinstance(m, str)]
    return L, case(L, 'route611', ':%d edited to the writer`s form (the planted template differing there alone %s) ; b758`s checks overrides by mark %d, '
                   'f8d771e18f03 among them %s' % (i + 1, planted != t0, len(marks), 'f8d771e18f03' in marks),
                   'b758 at the planted template: %s' % out['planted'], 'b758 at the working template: %s' % out['working'],
                   'f8d771e18f03' in out['planted'] and 'found 0 times' in out['planted'], out['working'] == 'renders'), 1


def control_renders():
    L = ['### (renders): checks.tpl RENDERED FOR EVERY ACT AT BASE`S TEMPLATE AND THE WORKING ONE']
    t0, t1 = tpls()
    acts = sorted(f[:-3] for f in os.listdir(os.path.join(T, 'acts')) if f.endswith('.py') and f[:1] == 'b')
    ones, alike, covered, bad = [], [], [], []
    for a in acts:
        e0 = e1 = None
        try:
            r0 = F.render(a, 'checks', tpl=t0).split(NL)
        except Exception as e:  # noqa: BLE001
            e0 = type(e).__name__
        try:
            r1 = F.render(a, 'checks', tpl=t1).split(NL)
        except Exception as e:  # noqa: BLE001
            e1 = type(e).__name__
        if e0 or e1:
            (alike if e0 and e1 and e0 == e1 else bad).append('%s %s/%s' % (a, e0, e1))
            continue
        dl = [i for i in range(min(len(r0), len(r1))) if r0[i] != r1[i]]
        if len(r0) == len(r1) and len(dl) == 1 and NEEDLE in r1[dl[0]]:
            ones.append(a)
        elif len(r0) == len(r1) and not dl:
            covered.append(a)
        else:
            bad.append('%s lines %d/%d differing %d' % (a, len(r0), len(r1), len(dl)))
    n0, n1 = len(t0.split(NL)), len(t1.split(NL))
    d = [i + 1 for i, (x, y) in enumerate(zip(t0.split(NL), t1.split(NL))) if x != y]
    return L, case(L, 'renders', 'checks.tpl: lines %d at BASE, %d now, differing at %s ; acts %d' % (n0, n1, d, len(acts)), 'the line counts equal %s' % (n0 == n1),
                   'differing in the one line %d (b758 %s, b759 %s) ; raising alike at both %d %s ; covered by the act %d %s ; others %s' % (
                       len(ones), 'b758' in ones, 'b759' in ones, len(alike), [x.split()[0] for x in alike][:30], len(covered), covered, bad or 'NONE'),
                   n0 == n1 and d == [663], 'b758' in ones and 'b759' in ones and not bad), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.5', ver == 'v1.36.6'), 1


CONTROLS = dict(face=control_face, arm=control_arm, route611=control_route611, renders=control_renders, version=control_version)
ORDER = ('face', 'arm', 'route611', 'renders', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    F.install()
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.6, (R369)(4)(iv): THE SUITE`S READER OF THE KERNELS FACE NAMES %s (%s)' % (
        act, M24, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'b758`s face read and not written, the template`s reader evaluated alone; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/fold/checks.tpl at %s) and after (the working file)' % BASE, '']
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
    out.append('### ### **v1.36.6: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1366.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
