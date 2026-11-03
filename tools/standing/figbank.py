# -*- coding: utf-8 -*-
"""standing/figbank.py -- v1.18.0, (R348)(2)(i), b737 defect (q): FIGURES BEFORE CONTROLS, REFUSED. Every bank that prints a figure opens with its
controls block; the render refuses a figure bank whose controls block is absent or follows its first figure, writing nothing. b737's criteria and box
banks opened on their figures, zeta's 14.134725 and 21.022040 and the reality checks standing inside the rows. Written at b738 by the Write tool.

A FIGURE is a decimal with three places or more (0.573960, 14.134725, 3.0e-39's mantissa excepted); a bank with none is no figure bank and passes.
THE CONTROLS BLOCK is a heading line `## THE CONTROLS` (or `###`), with at least one line under it before the next heading or blank line; the
block may itself carry figures (a control's own value), so it must open before the bank's first figure line outside it.

  reading(text) -> dict(figures, first_figure, controls, ok, why)
  write(path, text)   the bank written LF, atomically, only where reading(text) is ok; otherwise SystemExit naming why, nothing written
  python -X utf8 -u tools/standing/figbank.py read <bank> ...     each bank's reading printed; writes nothing
"""
import os
import re
import sys

FIGURE = re.compile(r'(?<![\w.])\d+\.\d{3,}')
CONTROLS = re.compile(r'^\s*#{2,3} THE CONTROLS\b')
HEADING = re.compile(r'^\s*#{2,3} ')


def reading(text):
    L = (text or '').replace('\r', '').split('\n')
    figs = [i for i, l in enumerate(L, 1) if FIGURE.search(l)]
    ctl = next((i for i, l in enumerate(L, 1) if CONTROLS.match(l)), None)
    body = 0
    if ctl is not None:
        for l in L[ctl:]:
            if not l.strip() or HEADING.match(l):
                break
            body += 1
    if not figs:
        return dict(figures=0, first_figure=None, controls=ctl, ok=True, why='no figure line: no figure bank')
    if ctl is None:
        return dict(figures=len(figs), first_figure=figs[0], controls=None, ok=False, why='no controls block; the first figure at :%d' % figs[0])
    if not body:
        return dict(figures=len(figs), first_figure=figs[0], controls=ctl, ok=False, why='the controls block at :%d is empty' % ctl)
    if ctl > figs[0]:
        return dict(figures=len(figs), first_figure=figs[0], controls=ctl, ok=False, why='the controls block at :%d follows the first figure at :%d' % (ctl, figs[0]))
    return dict(figures=len(figs), first_figure=figs[0], controls=ctl, ok=True, why='the controls block at :%d (%d lines) before the first figure outside it' % (ctl, body))


def write(path, text):
    r = reading(text)
    if not r['ok']:
        raise SystemExit('### FIGBANK REFUSED %s: %s -- NOTHING WRITTEN ((R348)(2)(i))' % (os.path.basename(path), r['why']))
    with open(path + '.tmp', 'wb') as f:
        f.write(((text or '').replace('\r', '').rstrip('\n') + '\n').encode('utf-8'))
    os.replace(path + '.tmp', path)
    return r


def main(argv):
    if len(argv) < 2 or argv[0] != 'read':
        sys.exit(__doc__)
    bad = 0
    for p in argv[1:]:
        with open(p, encoding='utf-8', errors='replace') as f:
            r = reading(f.read())
        bad += not r['ok']
        print('%-8s %s : figures %d ; %s' % ('PASSES' if r['ok'] else 'REFUSED', p, r['figures'], r['why']))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
