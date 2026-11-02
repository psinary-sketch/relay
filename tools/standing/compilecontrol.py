# -*- coding: utf-8 -*-
"""standing/compilecontrol.py -- v1.15.0, (R345)(2)(i), b734 defect (p): THE CONTROLS COMPILED WHAT THEY CONTROLLED. v1.14.0's 25 controls read tools/standing/probes.py and passed over a
syntax error in every suite part, `and__import__` at checks.tpl :126. Every standing version from this one carries this control over every rendered suite part and every rendered act
module, run before the version's figures print. A suite part is the checks render run with its part's name, so the checks render stands for the seven; the act module's seven renders are
the seven tools with the act's sections and overrides, and its worklist compiles beside them. The read is at a commit where one is named (the blobs of the templates and the act's
module), else the working tree.

  python -X utf8 -u tools/standing/compilecontrol.py check [<act>] [--at <commit>]
  check(act, at=None) -> dict(rows [(what, ok, detail)], ok)
  lines(c) -> the bank's lines, its foot the verdict
  stands(act, text) -> the version bank carries the verdict line
"""
import json
import os
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
import fold as F   # noqa: E402

FOOT = '### THE COMPILE CONTROL : %s'


def _blob(at, rel):
    b = subprocess.run(['git', '-C', RELAY, 'show', '%s:%s' % (at, rel)], capture_output=True)
    return b.stdout.decode('utf-8') if b.returncode == 0 else None


def check(act, at=None):
    rows = []
    mod = _blob(at, 'tools/acts/%s.py' % act) if at else None
    secs, ovs = F._parse(act, mod) if at else F._parse(act)
    for tool in F.TOOLS:
        what = '%s render' % tool
        try:
            tpl = _blob(at, 'tools/standing/fold/%s.tpl' % tool) if at else None
            text = F.render(act, tool, secs=secs, ovs=ovs, tpl=tpl)
            compile(text, '%s_%s.py' % (act, tool), 'exec')
            rows.append((what, True, '%d lines' % text.count('\n')))
        except SyntaxError as e:
            rows.append((what, False, 'SyntaxError line %s: %s' % (e.lineno, (e.text or '').strip()[:90])))
        except F.FoldRefused as e:
            rows.append((what, False, 'refused: %s' % e))
    wl = 'tools/%s_worklist.py' % act
    src = _blob(at, wl) if at else (F._rd(os.path.join(RELAY, *wl.split('/'))) if os.path.exists(os.path.join(RELAY, *wl.split('/'))) else None)
    if src is None:
        rows.append((wl, False, 'absent'))
    else:
        try:
            compile(src, wl, 'exec')
            rows.append((wl, True, '%d lines' % src.count('\n')))
        except SyntaxError as e:
            rows.append((wl, False, 'SyntaxError line %s' % e.lineno))
    return dict(act=act, at=at, rows=rows, ok=all(r[1] for r in rows))


def lines(c):
    L = ['  %-24s %-5s %s' % (w, 'OK' if ok else 'FAIL', d) for w, ok, d in c['rows']]
    L.append(FOOT % ('%s COMPILES WHOLE, %d OF %d' % (c['act'], len(c['rows']), len(c['rows'])) if c['ok'] else 'NOT CLEAR, %d OF %d FAIL' % (sum(1 for r in c['rows'] if not r[1]), len(c['rows']))))
    return L


def stands(act, text):
    return (FOOT % ('%s COMPILES WHOLE' % act)) in (text or '')


if __name__ == '__main__':
    a = sys.argv[2:] if sys.argv[1:2] == ['check'] else sys.exit(__doc__)
    at_ = None
    if '--at' in a:
        i = a.index('--at')
        at_ = a[i + 1]
        a = a[:i] + a[i + 2:]
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f_:
        act_ = a[0] if a else json.load(f_)['act']
    c_ = check(act_, at_)
    print('\n'.join(lines(c_)))
    sys.exit(0 if c_['ok'] else 1)
