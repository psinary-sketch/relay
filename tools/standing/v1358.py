# -*- coding: utf-8 -*-
"""standing/v1358.py -- THE CONTROLS OF v1.35.8, (R368)(3): THE TITLE RULE, in v1356.py's form.

The ruling's words (relay data/b758_ferry.txt :13): "THE TITLE RULE, from the halt: an entry's title and a bank's head are composed with the
typographic apostrophe where an apostrophe is meant, and the composer refuses a backtick in either; its control is one planted title."
BEFORE is b698's land and _land_one as R carries them unguarded (record.tpl :38 at BASE); AFTER is the same functions through
tools/standing/titlerule.py's rebind, which record.tpl :38 now calls. Every landing here is DRY (b652's land with dry=True prints and
writes nothing); _land_one, which appends on any call, is read through its guard over a stand-in that records the call and writes nothing.

  (plant)     the one planted title: b757's entry head as its findings bank keeps it (two backticks, the head of the halt at [22]), landed dry
              into FINDINGS.md: before, composed; after, refused, nothing composed.
  (pass)      the same head with each backtick made ’: after, composed dry, the guard silent.
  (one)       _land_one's guard over a stand-in: the planted head refused before the stand-in is called; the ’ head passed to it.
  (heads)     the findings banks' heads of b749, b752, b754, b755, b756 and b757 read by the rule: b757's refused, the five others passed.
  (wired)     the record tools of b758 and b757 loaded as fold.py loads them: R's land and _land_one carry the guard, once.
  (template)  record.tpl rendered for every act with a sections file at BASE's template and at the working one: the same line count, one line
              differing in each render, :38.
  (version)   tools/standing/VERSION moved to v1.35.8.

  python -X utf8 -u tools/standing/v1358.py control [plant|pass|one|heads|wired|template|version ...] [--bank]
"""
import contextlib
import io
import json
import os
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '248cacb8'   # ### the relay's HEAD before this change (b758 component 1, step 14, v1.35.7)
HEADS = ('b749', 'b752', 'b754', 'b755', 'b756', 'b757')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import titlerule as TR          # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def after(L, k, what, got, ok):
    L.append('  (%s) %s' % (k, what))
    L.append('      AFTER : %s -> %s' % (got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    return 1 if ok else 0


def head_of(act):
    fj = json.load(io.open(os.path.join(D, '%s_findings.json' % act), encoding='utf-8'))
    return fj.get('head') or fj.get('title') or ''


def raw_R():
    """b698's module as b758's record tool loads it (record.tpl :37 setting R.SP to the act's scratch folder, as every live route has it), and
    its land and _land_one as they stood before the rebind of :38 (the wrapper's __wrapped__)."""
    if 'R' not in _MEMO:
        F.install()
        cwd = os.getcwd()
        os.chdir(RELAY)
        try:
            R = F.load('b758', 'record', name='b758_record').R
        finally:
            os.chdir(cwd)
        _MEMO['R'] = R
        _MEMO['raw'] = (getattr(R.land, '__wrapped__', R.land), getattr(R._land_one, '__wrapped__', R._land_one))
    return _MEMO['R'], _MEMO['raw']


@contextlib.contextmanager
def quiet():
    so = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = so


def try_land(fn, head):
    """('composed', n characters printed) or ('refused', the refusal's words), a dry landing of one FINDINGS item under `head`."""
    with quiet() as buf:
        try:
            fn([('FINDINGS.md', head, NL + head + NL + NL + 'A planted line beneath the head.' + NL)], 'b758_v1358_none.json', 'v1358', dry=True)
            return 'composed', len(buf.getvalue())
        except SystemExit as e:
            return 'refused', (buf.getvalue().strip() or str(e))[:200]


def control_plant():
    L, gd, n = ['### (plant): THE ONE PLANTED TITLE, b757`S ENTRY HEAD AS ITS FINDINGS BANK KEEPS IT, LANDED DRY'], 0, 0
    R, (land0, _o) = raw_R()
    h = head_of('b757')
    b = try_land(land0, h)
    a = try_land(TR._guard_land(land0), h)
    n += 1
    gd += case(L, 'plant', 'the head (%d characters, %d backticks)' % (len(h), h.count('`')), '%s %s' % b, '%s %s' % a,
               b[0] == 'composed', a[0] == 'refused' and 'THE TITLE RULE' in str(a[1]))
    return L, gd, n


def control_pass():
    L, gd, n = ['### (pass): THE SAME HEAD WITH EACH BACKTICK MADE ’'], 0, 0
    R, (land0, _o) = raw_R()
    h = head_of('b757').replace('`', '’')
    a = try_land(TR._guard_land(land0), h)
    n += 1
    gd += after(L, 'pass', 'the head (%d characters, %d backticks, %d ’)' % (len(h), h.count('`'), h.count('’')), '%s %s' % a, a[0] == 'composed')
    return L, gd, n


def control_one():
    L, gd, n = ['### (one): _land_one`S GUARD OVER A STAND-IN THAT RECORDS THE CALL AND WRITES NOTHING'], 0, 0
    calls = []
    g = TR._guard_one(lambda path, head, e, bank, extra: calls.append(head) or 1)
    h = head_of('b757')
    with quiet():
        try:
            g('FINDINGS.md', h, h, 'none.json', {})
            r1 = 'called'
        except SystemExit:
            r1 = 'refused'
    c1 = len(calls)
    r2 = g('FINDINGS.md', h.replace('`', '’'), h, 'none.json', {})
    n += 1
    gd += after(L, 'one', 'the planted head, then the ’ head', 'planted: %s, the stand-in called %d times ; ’: returned %r, the stand-in called %d times' % (
        r1, c1, r2, len(calls)), r1 == 'refused' and c1 == 0 and r2 == 1 and len(calls) == 1)
    return L, gd, n


def control_heads():
    L, gd, n = ['### (heads): THE FINDINGS BANKS` HEADS OF b749, b752, b754, b755, b756 AND b757 READ BY THE RULE'], 0, 0
    got = [(a, TR.fault(head_of(a)) is None) for a in HEADS]
    n += 1
    gd += after(L, 'heads', 'passed: %s' % ', '.join('%s %s' % x for x in got),
                'b757 refused %s ; the five others passed %s' % (not dict(got)['b757'], all(o for a, o in got if a != 'b757')),
                not dict(got)['b757'] and all(o for a, o in got if a != 'b757'))
    return L, gd, n


def control_wired():
    L, gd, n = ['### (wired): THE RECORD TOOLS OF b758 AND b757 LOADED AS fold.py LOADS THEM'], 0, 0
    R, _raw = raw_R()
    cwd = os.getcwd()
    os.chdir(RELAY)
    try:
        M8 = F.load('b758', 'record', name='b758_record')
        M7 = F.load('b757', 'record', name='b757_record')
    finally:
        os.chdir(cwd)
    same = M8.R is R and M7.R is R
    lw, ow = getattr(R.land, '__titlerule__', False), getattr(R._land_one, '__titlerule__', False)
    once = not getattr(getattr(R.land, '__wrapped__', None), '__titlerule__', False) and not getattr(getattr(R._land_one, '__wrapped__', None), '__titlerule__', False)
    mod_land = getattr(M8.land, '__titlerule__', False)
    n += 1
    gd += after(L, 'wired', 'R shared by both tools %s' % same,
                'R.land guarded %s ; R._land_one guarded %s ; each once %s ; b758`s module land guarded %s' % (lw, ow, once, mod_land),
                same and lw and ow and once and mod_land)
    return L, gd, n


def control_template():
    L, gd, n = ['### (template): record.tpl RENDERED FOR EVERY ACT WITH A SECTIONS FILE, AT BASE`S TEMPLATE AND AT THE WORKING ONE'], 0, 0
    t0 = V.show(BASE, 'tools/standing/fold/record.tpl')
    t1 = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8', newline='').read()
    acts = sorted(f[:-3] for f in os.listdir(os.path.join(T, 'acts')) if f.endswith('.py') and f[:1] == 'b')
    bad, ones = [], 0
    for a in acts:
        try:
            r0, r1 = F.render(a, 'record', tpl=t0).split(NL), F.render(a, 'record', tpl=t1).split(NL)
        except Exception as e:  # noqa: BLE001
            bad.append('%s raised %s' % (a, type(e).__name__))
            continue
        dl = [i + 1 for i in range(min(len(r0), len(r1))) if r0[i] != r1[i]]
        if len(r0) == len(r1) and len(dl) == 1 and 'titlerule' in r1[dl[0] - 1]:
            ones += 1
        else:
            bad.append('%s lines %d/%d differing %s' % (a, len(r0), len(r1), dl[:4]))
    n += 1
    gd += case(L, 'template', 'record.tpl: lines %d at BASE, %d now' % (len(t0.split(NL)), len(t1.split(NL))),
               'BASE`s template, every act rendered (%d)' % len(acts),
               'renders differing in one line, the title rule`s, with the same line count: %d of %d ; others %s' % (ones, len(acts), bad or 'NONE'),
               len(t0.split(NL)) == len(t1.split(NL)), ones == len(acts) and not bad)
    return L, gd, n


def control_version():
    L, gd, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    gd += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.7', ver == 'v1.35.8')
    return L, gd, n


CONTROLS = dict(plant=control_plant, **{'pass': control_pass}, one=control_one, heads=control_heads, wired=control_wired,
                template=control_template, version=control_version)
ORDER = ('plant', 'pass', 'one', 'heads', 'wired', 'template', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.8, (R368)(3): THE TITLE RULE (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (b698`s land and _land_one unguarded, record.tpl :38 at %s) and after (tools/standing/titlerule.py)' % BASE, '']
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
    out.append('### ### **v1.35.8: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1358.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
