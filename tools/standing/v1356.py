# -*- coding: utf-8 -*-
"""standing/v1356.py -- THE CONTROLS OF v1.35.6, (R368)(1): THE READER'S REPAIR, in v1355.py's form.

The ruling's words (relay data/b758_ferry.txt :9): "THE READER'S REPAIR, a standing change with VERSION moved: tools/standing/act.py :82
compares the FINDINGS line with the findings bank's head after passing the head through the landing's one conversion (tools/b652_record.py
:35-:36). Its controls, printed before any use: b757's entry read whole; the entries of b749, b752, b754, b755 and b756 read as before; a
head planted one character off refused; the line after b757's head refused." b757 halted at [22] (21:55:35Z): its entry's title was composed
with two backticks, the landing wrote them as ’, and :82 compared the landed line with the bank's head raw. BEFORE is tools/standing/act.py
at BASE, run from its blob in a module of its own; AFTER the working tree's act.py. Every read is at PLACE-papers HEAD.

  (copy)     act.py's copied conversion against tools/b652_record.py's own on every line of FINDINGS.md and on planted strings: equal on all.
  (b757)     b757's entry (data/b757_findings.json): before, refused at :15436; after, read whole -- its first line the landed head, its bytes the
             bank's `append` count less the prefix, its last line the entry's INTEGRATION line.
  (earlier)  the entries of b749, b752, b754, b755 and b756: before and after, equal text.
  (plant)    b757's bank with its head one character off: refused after.
  (next)     b757's bank with its line one past the head: refused after.
  (version)  tools/standing/VERSION moved to v1.35.6.

  python -X utf8 -u tools/standing/v1356.py control [copy|b757|earlier|plant|next|version ...] [--bank]
"""
import io
import json
import os
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '2e103c46'   # ### the relay's HEAD before this change (b758 component 2, step 11)
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

EARLIER = ('b749', 'b752', 'b754', 'b755', 'b756')


def act_at(rev):
    """tools/standing/act.py at `rev`, run from its blob in a module of its own (it imports the standard library alone)."""
    src = V.show(rev, 'tools/standing/act.py')
    m = types.ModuleType('act_at_%s' % rev)
    m.__file__ = os.path.join(S, 'act.py')
    exec(compile(src, 'tools/standing/act.py@%s' % rev, 'exec'), m.__dict__)   # noqa: S102
    return m


def fj_of(act):
    return json.load(io.open(os.path.join(D, '%s_findings.json' % act), encoding='utf-8'))


def read(mod, act, fj):
    """(text, None) or (None, the refusal's words)."""
    try:
        return mod.landed_entry(act, fj), None
    except ValueError as e:
        return None, str(e)


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def after(L, k, what, got, ok):
    L.append('  (%s) %s' % (k, what))
    L.append('      AFTER : %s -> %s' % (got, 'AS WANTED' if ok else 'NOT AS WANTED'))
    return 1 if ok else 0


def control_copy():
    L, gd, n = ['### (copy): THE COPIED CONVERSION AGAINST tools/b652_record.py`S OWN'], 0, 0
    import b652_record as R
    lines = A.git('pp', 'show', 'HEAD:FINDINGS.md').decode('utf-8').split(NL)
    diff = [k + 1 for k, l in enumerate(lines) if A.conv(l) != R.conv(l)]
    moved = sum(1 for l in lines if R.conv(l) != l)
    n += 1
    gd += after(L, 'copy', 'every line of FINDINGS.md at PLACE-papers HEAD through both',
                'lines %d ; lines the conversion changes %d ; lines where the two differ %d %s' % (len(lines), moved, len(diff), diff[:5]),
                not diff and moved > 0)
    pl = ["formula`s four", 'f(x)`s', 'A`B', 'a ` b', '`code`', 'x`y`z', '9`th', '']
    got = [(s, A.conv(s), R.conv(s)) for s in pl]
    n += 1
    gd += after(L, 'copy', 'planted strings (an apostrophe after a letter, a bracket and a digit converted; before a capital, a spaced one, '
                'a code span not)', [g[1] for g in got], all(g[1] == g[2] for g in got) and got[0][1] == 'formula’s four' and got[2][1] == 'A`B'
                and got[4][1] == '`code`')
    return L, gd, n


def control_b757():
    L, gd, n = ['### (b757): b757`S ENTRY, THE ONE THE REPAIR IS FOR'], 0, 0
    fj = fj_of('b757')
    old = act_at(BASE)
    tb, eb = read(old, 'b757', fj)
    ta, ea = read(A, 'b757', fj)
    land = A.git('pp', 'show', 'HEAD:FINDINGS.md').decode('utf-8').split(NL)[int(fj['line']) - 1]
    ap = fj.get('append') or {}
    want = int(ap.get('added', 0)) - (1 if ap.get('prefix') else 0)
    last = [l for l in (ta or '').split(NL) if l.strip()][-1:] or ['']
    nl_ = (int(fj['line']) - 1 + len((ta or '').rstrip(NL).split(NL))) if ta else 0
    n += 1
    # ### PLACE-papers lines are printed by line and digest, never by their words
    gd += case(L, 'b757', 'the bank`s head (%d backticks) against FINDINGS.md :%s' % ((fj.get('head') or '').count('`'), fj['line']),
               'refused: %s' % eb if eb else 'READ (%d characters)' % len(tb or ''),
               ('read: %d characters ; the first line the landed head %s ; bytes %d against the bank`s %d less the prefix (%d) ; the last line :%d '
                'sha256 %s, opening INTEGRATION %s' % (
                    len(ta), ta.split(NL)[0] == land.strip(), len(ta.strip().encode('utf-8')), int(ap.get('added', 0)), want, nl_,
                    A.sha256_bytes(last[0].strip().encode('utf-8'))[:16], last[0].startswith('INTEGRATION')))
               if ta else 'refused: %s' % ea,
               eb is not None and tb is None,
               ta is not None and ta.split(NL)[0] == land.strip() and len(ta.strip().encode('utf-8')) <= want and last[0].startswith('INTEGRATION'))
    return L, gd, n


def control_earlier():
    L, gd, n = ['### (earlier): THE ENTRIES OF b749, b752, b754, b755 AND b756, BEFORE AND AFTER'], 0, 0
    old = act_at(BASE)
    for act in EARLIER:
        fj = fj_of(act)
        tb, eb = read(old, act, fj)
        ta, ea = read(A, act, fj)
        n += 1
        gd += case(L, act, '%s`s entry at FINDINGS.md :%s' % (act, fj['line']),
                   'refused: %s' % eb if eb else 'read, %d characters' % len(tb),
                   'refused: %s' % ea if ea else 'read, %d characters ; equal to before %s' % (len(ta), ta == tb),
                   tb is not None, ta is not None and ta == tb)
    return L, gd, n


def control_plant():
    L, gd, n = ['### (plant): b757`S BANK WITH ITS HEAD ONE CHARACTER OFF'], 0, 0
    fj = dict(fj_of('b757'))
    h = fj.get('head') or ''
    k = len(h) // 2
    while k < len(h) and (h[k] == '`' or not h[k].isalpha()):
        k += 1
    fj['head'] = h[:k] + ('X' if h[k] != 'X' else 'Y') + h[k + 1:]
    ta, ea = read(A, 'b757', fj)
    n += 1
    gd += after(L, 'plant', 'the head`s character :%d %r made %r' % (k + 1, h[k], fj['head'][k]),
                'refused: %s' % ea if ea else 'READ (%d characters)' % len(ta), ea is not None and ta is None)
    return L, gd, n


def control_next():
    L, gd, n = ['### (next): b757`S BANK WITH ITS LINE ONE PAST THE HEAD'], 0, 0
    fj = dict(fj_of('b757'))
    fj['line'] = int(fj['line']) + 1
    ta, ea = read(A, 'b757', fj)
    n += 1
    gd += after(L, 'next', 'the line :%d' % fj['line'], 'refused: %s' % ea if ea else 'READ (%d characters)' % len(ta), ea is not None and ta is None)
    return L, gd, n


def control_version():
    L, gd, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    gd += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.5', ver == 'v1.35.6')
    return L, gd, n


CONTROLS = dict(copy=control_copy, b757=control_b757, earlier=control_earlier, plant=control_plant, next=control_next, version=control_version)
ORDER = ('copy', 'b757', 'earlier', 'plant', 'next', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.6, (R368)(1): THE READER`S REPAIR (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, act.py before read from %s and run from its blob' % BASE, '']
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
    out.append('### ### **v1.35.6: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1356.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
