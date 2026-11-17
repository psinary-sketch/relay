# -*- coding: utf-8 -*-
"""standing/v1365.py -- THE CONTROLS OF v1.36.5, (R369)(4)(iii): THE ROW WRITER TAKES A ROW PHASE FOR A REPAIR COMMIT, in v1363.py's form.

The ruling's words (relay data/b759_ferry.txt :15): "(iii) THE ROW WRITER takes a row phase for a repair commit
(tools/standing/fold/record.tpl :312-:313); its control b758's repair commit f401a81e replayed." tools/standing/commit.py's `repair`
phase (v1.24.0) hands its row to the record tool's step route with the phase `repair`; record.tpl :312-:313 refused every phase outside
STEP_PHASES (data/act_current.json's components, `record` and `closing`), so b758's repair commit f401a81e took the row phase `seal`
(relay data/b758_steps.json, its row of f401a81e). v1.36.5: :312-:313 take `repair` beside STEP_PHASES, in the same two lines, the
template's line count kept for the act modules' overrides by number.

THE REPLAY writes nothing: record.tpl is rendered for b758 at BASE's template and the working one, the step route (`def step`) cut from each
render and run alone, its readers bound to b758's step rows before f401a81e's (read from the bank, never rewritten) and its writer to a
capture; the rendered module itself is not imported.

  (replay)   f401a81e with the phase `repair`: BEFORE refused ("IS NOT ONE OF"), nothing captured; AFTER one row captured, phase `repair`,
             commit f401a81e, its subject "b758 repair: ...".
  (phases)   AFTER, the same commit: `seal` taken as before; `repiar` refused; a second `lock` refused by one_lock.
  (arm)      G-SEALED-AFTER-COMPONENTS (tools/standing/repeat.py sealed_after) over b758's rows and logs, f401a81e's row read `seal` as banked
             and `repair` as replayed: the two verdicts equal.
  (renders)  record.tpl rendered for every act at BASE's template and the working one: each render differing in the route's two lines (the
             line count equal), or raising alike at both, or the lines covered by the act's own override; b759 among the first.
  (version)  tools/standing/VERSION moved to v1.36.5.

  python -X utf8 -u tools/standing/v1365.py control [replay|phases|arm|renders|version ...] [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '4622b017'   # ### the relay's HEAD before this change (b759 component 2, step 10, v1.36.4)
PP = 'D:/MY-DOwnloads/PLACE-papers'
REPAIR = 'f401a81e'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import act_close as AC          # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import repeat as RP             # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout


def tpls():
    if 't0' not in _MEMO:
        _MEMO['t0'] = V.show(BASE, 'tools/standing/fold/record.tpl')
        _MEMO['t1'] = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8', newline='').read()
    return _MEMO['t0'], _MEMO['t1']


def b758_rows():
    rows = json.load(io.open(os.path.join(D, 'b758_steps.json'), encoding='utf-8'))['rows']
    i = next(k for k, r in enumerate(rows) if r.get('repo') == 'relay' and (r.get('commit') or '').startswith(REPAIR))
    return rows, i


def step_fn(tpl):
    """the step route cut from b758's render of `tpl`, bound to the readers and a capture; returns (step, captured list)."""
    r = F.render('b758', 'record', tpl=tpl).split(NL)
    i0 = next(i for i, l in enumerate(r) if l.startswith('def step('))
    i1 = next(i for i in range(i0 + 1, len(r)) if r[i].startswith(('def ', '# ====')))
    src = NL.join(r[i0:i1])
    pre, post = RP.phases(RELAY)
    rows, i = b758_rows()
    cap = []
    ns = dict(re=re, sys=sys, time=time, AC=AC, ACT='b758', STEP_PHASES=pre + post, PRE_SEAL_PHASES=pre, POST_SEAL_PHASES=post,
              STEP_REPOS=dict(relay=RELAY, pp=PP), g=g, jl=lambda name: dict(rows=[dict(x) for x in rows[:i]]),
              put_json=lambda name, obj: cap.append((name, obj)), utc=lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    exec(compile(src, 'record.tpl step (b758 render)', 'exec'), ns)   # noqa: S102
    return ns['step'], cap


def trial(fn):
    try:
        fn()
        return False, ''
    except SystemExit as e:
        return True, str(e)[:160]


def control_replay():
    L = ['### (replay): b758`S REPAIR COMMIT f401a81e THROUGH THE STEP ROUTE, NOTHING WRITTEN']
    t0, t1 = tpls()
    s0, c0 = step_fn(t0)
    s1, c1 = step_fn(t1)
    r0 = trial(lambda: s0('relay', 'repair', REPAIR))
    r1 = trial(lambda: s1('relay', 'repair', REPAIR))
    row = c1[0][1]['rows'][-1] if c1 else {}
    rows, i = b758_rows()
    return L, case(L, 'replay', '`step relay repair %s` over b758`s %d rows before its row (banked: row %d, phase %r)' % (REPAIR, i, i + 1, rows[i].get('phase')),
                   'refused %s (%s) ; captured %d' % (r0[0], r0[1][:90], len(c0)),
                   'refused %s ; captured %d: %s, phase %r, commit %s, subject %r' % (r1[0], len(c1), c1[0][0] if c1 else '-', row.get('phase'),
                                                                                    (row.get('commit') or '')[:8], (row.get('subject') or '')[:40]),
                   r0[0] and 'IS NOT ONE OF' in r0[1] and not c0,
                   not r1[0] and len(c1) == 1 and row.get('phase') == 'repair' and (row.get('commit') or '').startswith(REPAIR)
                   and (row.get('subject') or '').startswith('b758 repair:') and len(c1[0][1]['rows']) == i + 1), 1


def control_phases():
    L = ['### (phases): THE SAME COMMIT, THE OTHER PHASES, AFTER']
    t1 = tpls()[1]
    out = {}
    for ph in ('seal', 'repiar', 'lock'):
        s1, c1 = step_fn(t1)
        out[ph] = (trial(lambda: s1('relay', ph, REPAIR)), [o['rows'][-1].get('phase') for _n, o in c1])
    return L, case(L, 'phases', '`seal`, `repiar` and a second `lock` for %s' % REPAIR, 'n/a (the route as at BASE for these)',
                   ' ; '.join('%s: refused %s %s captured %s' % (k, v[0][0], v[0][1][:60], v[1]) for k, v in out.items()), True,
                   out['seal'][1] == ['seal'] and not out['seal'][0][0] and out['repiar'][0][0] and 'IS NOT ONE OF' in out['repiar'][0][1]
                   and out['lock'][0][0] and 'A LOCK ROW STANDS' in out['lock'][0][1]), 1


def _log(repo, rows, key):
    cs = [c for r in rows if r.get('repo') == key for c in ([r.get('commit')] + list(r.get('commits') or [])) if c]
    first = cs[0]
    lines = g(repo, 'log', '--reverse', '--format=%H %ct %s', '%s^..%s' % (first, cs[-1])).split(NL)
    return [(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in lines if l.strip()]


def control_arm():
    L = ['### (arm): G-SEALED-AFTER-COMPONENTS OVER b758`S ROWS, f401a81e READ `seal` AND `repair`']
    rows, i = b758_rows()
    rlog, plog = _log(RELAY, rows, 'relay'), _log(PP, rows, 'pp')
    pre, _post = RP.phases(RELAY)

    def files_of(repo, h):
        return [x for x in g(RELAY if repo == 'relay' else PP, 'show', '--name-only', '--format=', h).split(NL) if x.strip()]
    v0 = RP.sealed_after(rows, rlog, plog, pre, files_of, 'b758')
    alt = [dict(r, phase='repair') if k == i else r for k, r in enumerate(rows)]
    v1 = RP.sealed_after(alt, rlog, plog, pre, files_of, 'b758')
    return L, case(L, 'arm', 'b758`s rows %d ; relay log %d, PLACE-papers log %d' % (len(rows), len(rlog), len(plog)),
                   'f401a81e read `seal` (as banked): %s' % (v0,), 'f401a81e read `repair`: %s ; equal %s' % (v1, v0 == v1), True, v0 == v1), 1


def control_renders():
    L = ['### (renders): record.tpl RENDERED FOR EVERY ACT AT BASE`S TEMPLATE AND THE WORKING ONE']
    t0, t1 = tpls()
    acts = sorted(f[:-3] for f in os.listdir(os.path.join(T, 'acts')) if f.endswith('.py') and f[:1] == 'b')
    ones, alike, covered, bad = [], [], [], []
    for a in acts:
        e0 = e1 = None
        try:
            r0 = F.render(a, 'record', tpl=t0).split(NL)
        except Exception as e:  # noqa: BLE001
            e0 = type(e).__name__
        try:
            r1 = F.render(a, 'record', tpl=t1).split(NL)
        except Exception as e:  # noqa: BLE001
            e1 = type(e).__name__
        if e0 or e1:
            (alike if e0 and e1 and e0 == e1 else bad).append('%s %s/%s' % (a, e0, e1))
            continue
        dl = [i for i in range(min(len(r0), len(r1))) if r0[i] != r1[i]]
        if len(r0) == len(r1) and len(dl) == 2 and all("STEP_PHASES + ('repair',)" in r1[i] for i in dl):
            ones.append(a)
        elif len(r0) == len(r1) and not dl:
            covered.append(a)
        else:
            bad.append('%s lines %d/%d differing %d' % (a, len(r0), len(r1), len(dl)))
    n0, n1 = len(t0.split(NL)), len(t1.split(NL))
    return L, case(L, 'renders', 'record.tpl: lines %d at BASE, %d now ; acts %d' % (n0, n1, len(acts)), 'the line counts equal %s' % (n0 == n1),
                   'differing in the route`s two lines %d (b759 among them %s) ; raising alike %d %s ; covered by the act %d %s ; others %s' % (
                       len(ones), 'b759' in ones, len(alike), [x.split()[0] for x in alike][:30], len(covered), covered, bad or 'NONE'),
                   n0 == n1, 'b759' in ones and not bad), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.4', ver == 'v1.36.5'), 1


CONTROLS = dict(replay=control_replay, phases=control_phases, arm=control_arm, renders=control_renders, version=control_version)
ORDER = ('replay', 'phases', 'arm', 'renders', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    F.install()
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.5, (R369)(4)(iii): THE ROW WRITER TAKES A ROW PHASE FOR A REPAIR COMMIT (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'b758`s step bank read and not written, the step route run alone with a capture for its writer; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/fold/record.tpl at %s) and after (the working file)' % BASE, '']
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
    out.append('### ### **v1.36.5: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1365.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
