# -*- coding: utf-8 -*-
"""standing/v1355.py -- THE CONTROLS OF v1.35.5, (R367)(8)(ii): THE CLOSING PRINTS ONE COUNT IN ONE FORM, in v1354.py's form.

The ruling's words (relay data/b757_ferry.txt :25): "(ii) (F6): the closing prints one count in one form, by a standing change to the
figure at tools/standing/fold/closing.tpl :353-:367: every arm run is counted, the vacuous named, as "<p> OF <n> RUN ; FAILING <f> ;
VACUOUS <v>", equal to the head line's figure; on b756's checks bank it prints 110 OF 116 RUN, FAILING 5, VACUOUS 1 with G-RUNNER-GATE
named." b756's closing printed "THE WHOLE SUITE PASSING 110 OF 115" beside its head's 116 (data/b756_closing.txt :704-:705): the pattern
at :353 kept a row marked PASS or FAIL in all three columns and dropped G-RUNNER-GATE's, whose third column reads VAC (data/b756_checks.txt
:116, :18). BEFORE is the template at BASE; AFTER the working tree. The function is cut from each template's text (ARM_LIVE to the end of
claim_figure) and run here, data/arm_tags.json read for the tags; the template is rendered by no route of this tool.

  (figure)   on b756's checks bank: before, the old figure's whole-suite count of 115; after, "110 OF 116 RUN ; FAILING 5 ... ; VACUOUS 1
             ['G-RUNNER-GATE']".
  (head)     the figure's three counts equal to the bank's head lines (ARMS RUN, LIVE PASSING, LIVE FAILING at :16; VACUOUS at :18).
  (plant)    a planted bank of three rows, one vacuous in its middle column: "1 OF 3 RUN ; FAILING 1 ['G-B'] ; VACUOUS 1 ['G-C']"; an empty
             text NOT YET RUN.
  (lines)    closing.tpl's line count equal to BASE's: the acts before b735 key their overrides by line number (fold.py MARK_FROM 735; b757
             defect (g)), so no line below :368 moves.
  (version)  tools/standing/VERSION moved to v1.35.5.

  python -X utf8 -u tools/standing/v1355.py control [figure|head|plant|lines|version ...] [--bank]
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
BASE = 'c98beed0'   # ### the relay's HEAD before this change (b757 component 5, step 50)
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


def tags():
    p = os.path.join(D, 'arm_tags.json')
    return json.load(io.open(p, encoding='utf-8')) if os.path.isfile(p) else {}


def figure_fn(tpl_text):
    """claim_figure cut from a template's text (ARM_LIVE's line to the function's last line) and made callable, jl reading arm_tags.json."""
    L = (tpl_text or '').split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('ARM_LIVE = ')), None)
    j = next((k for k, l in enumerate(L) if k > (i or 0) and l.startswith('def claim_figure(')), None)
    if i is None or j is None:
        return None
    k = j + 1
    while k < len(L) and (L[k].startswith(' ') or not L[k].strip()):
        if not L[k].strip() and k + 1 < len(L) and L[k + 1] and not L[k + 1].startswith(' '):
            break
        k += 1
    src = NL.join(L[i:k]).replace('⟪RUL⟫', 'R367')
    ns = {'re': re, 'jl': lambda n: tags() if n == 'arm_tags.json' else {}}
    exec(compile(src, 'claim_figure', 'exec'), ns)   # noqa: S102
    return ns['claim_figure']


def case(L, k, what, before, after, ok_b, ok_a):
    good = ok_b and ok_a
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if good else 0


def after(L, k, what, got, ok):
    L.append('  (%s) %s' % (k, what))
    L.append('      AFTER : %s -> %s' % (got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    return 1 if ok else 0


def _tpls():
    return (V.show(BASE, TPL) or ''), io.open(os.path.join(RELAY, TPL), encoding='utf-8').read()


def control_figure():
    L, gd, n = ['### (figure): b756`S CHECKS BANK (data/b756_checks.txt) THROUGH THE FIGURE BEFORE AND AFTER'], 0, 0
    b, a = _tpls()
    t = io.open(os.path.join(D, 'b756_checks.txt'), encoding='utf-8').read()
    fb, fa = figure_fn(b), figure_fn(a)
    ob, oa = (fb(t) if fb else 'NOT CUT'), (fa(t) if fa else 'NOT CUT')
    n += 1
    gd += case(L, 'figure', 'b756`s bank: the old figure counts 115 rows, the new one every arm run with the vacuous named', ob, oa,
               'THE WHOLE SUITE PASSING 110 OF 115' in ob,
               oa.startswith('110 OF 116 RUN ; FAILING 5 ') and "VACUOUS 1 ['G-RUNNER-GATE']" in oa)
    return L, gd, n


def control_head():
    L, gd, n = ['### (head): THE FIGURE AGAINST THE BANK`S HEAD LINES'], 0, 0
    _b, a = _tpls()
    t = io.open(os.path.join(D, 'b756_checks.txt'), encoding='utf-8').read()
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) ', t)
    v = re.search(r'VACUOUS, THE PLANT MUTATED NOTHING, COUNTED NEITHER PASSING NOR FAILING : (\d+) ', t)
    fa = figure_fn(a)
    f = fa(t) if fa else ''
    fm = re.match(r'(\d+) OF (\d+) RUN ; FAILING (\d+) .* ; VACUOUS (\d+) ', f)
    head = (m.group(2), m.group(1), m.group(3), v.group(1)) if m and v else None
    got = fm.groups() if fm else None
    n += 1
    gd += after(L, 'head', 'passing, run, failing and vacuous: the head lines :16 and :18 against the figure',
                'head %s ; figure %s' % (head, got), head is not None and head == got)
    return L, gd, n


def control_plant():
    L, gd, n = ['### (plant): A PLANTED BANK AND AN EMPTY TEXT'], 0, 0
    _b, a = _tpls()
    fa = figure_fn(a)
    t = ('  G-A                PASS  PASS  FAIL  0.010    OK\n  G-B                FAIL  FAIL  FAIL  0.010    ### FAILS\n'
         '  G-C                PASS  VAC   PASS  0.010    VACUOUS: THE PLANT MUTATED NOTHING\n')
    o = fa(t) if fa else 'NOT CUT'
    n += 1
    gd += after(L, 'plant', 'three rows, the vacuous one marked in its middle column', o,
                o.startswith("1 OF 3 RUN ; FAILING 1 ['G-B'] ; VACUOUS 1 ['G-C'] ;"))
    e = fa('') if fa else 'NOT CUT'
    n += 1
    gd += after(L, 'plant', 'an empty text', e, e == 'NOT YET RUN')
    return L, gd, n


def control_lines():
    L, gd, n = ['### (lines): closing.tpl`S LINE COUNT, NO LINE BELOW THE FIGURE MOVED'], 0, 0
    b, a = _tpls()
    nb, na = b.count(NL), a.count(NL)
    tail_b, tail_a = b.split(NL)[368:], a.split(NL)[368:]
    n += 1
    gd += case(L, 'lines', TPL, '%d lines' % nb, '%d lines ; every line after :368 equal to BASE`s %s' % (na, tail_a == tail_b),
               nb > 368, na == nb and tail_a == tail_b)
    return L, gd, n


def control_version():
    L, gd, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    gd += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.4', ver == 'v1.35.5')
    return L, gd, n


CONTROLS = dict(figure=control_figure, head=control_head, plant=control_plant, lines=control_lines, version=control_version)
ORDER = ('figure', 'head', 'plant', 'lines', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.5, (R367)(8)(ii): THE CLOSING PRINTS ONE COUNT IN ONE FORM (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, the template before read from %s' % BASE, '']
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
    out.append('### ### **v1.35.5: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1355.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
