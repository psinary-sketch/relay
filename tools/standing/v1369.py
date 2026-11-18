# -*- coding: utf-8 -*-
"""standing/v1369.py -- THE CONTROLS OF v1.36.9, (R370)(5)(ii): THE PLACE OF AN ACT WHOSE FERRY CARRIES NONE, in v1368.py's form.

The ruling's words (relay data/b760_ferry.txt :17): "(ii) THE PLACE OF AN ACT WHOSE FERRY CARRIES NONE: handoff.py reads it from
data/b760_places.txt, banked from BLOCK P, where the ferry has no such line. Its controls: b758's place read from the bank, b757's from its
ferry, an act with neither refused. HANDOFF.md is then built and written, its line count and yields printed." tools/standing/handoff.py
v1.36.9 reads, for each of the twelve acts, the one THE ACT'S PLACE line of its ferry, and where the ferry carries none the one row for the
act in the places banks data/<act>_places.txt at the relay's HEAD (place_rows); the bank data/b760_places.txt was written by
tools/b760_places.py from BLOCK P and committed before these controls (relay e8c32b99). BEFORE is handoff.py at BASE, executed as a module of
its own; AFTER the working file. Every case builds the page in memory from the banks at the two heads or from copies planted in memory;
nothing is written.

  (bank)      THE ORDERED CONTROL: b758's place read from the bank (data/b760_places.txt :7).
  (ferry)     THE ORDERED CONTROL: b757's place read from its ferry (data/b757_ferry.txt :31).
  (neither)   THE ORDERED CONTROL: an act with neither, b758's row taken out of a planted copy of the bank: refused, naming b758's ferry.
  (twice)     a planted bank carrying b758's row twice: refused, one wanted.
  (first)     b757 given a planted row beside its ferry's line: read from its ferry, the planted row not quoted.
  (page)      the page from the banks at the two heads: BEFORE refused at b759's ferry; AFTER built under the cap, twelve acts.
  (control)   handoff.py's own controls: BEFORE raised or not all as wanted; AFTER all as wanted.
  (diff)      the working handoff.py against BASE's: every line removed is one the change names.
  (version)   tools/standing/VERSION moved to v1.36.9.

  python -X utf8 -u tools/standing/v1369.py control [bank|ferry|neither|twice|first|page|control|diff|version ...] [--bank]
"""
import difflib
import io
import os
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'e8c32b99'   # ### the relay's HEAD before this change (b760 component 2, step 12, the places bank; v1.36.8)
BANK = 'data/b760_places.txt'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import handoff as H1            # noqa: E402  (the working file: AFTER)
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def base():
    """handoff.py at BASE, executed as a module of its own (its __main__ guard keeps main() unrun)."""
    if 'H0' not in _MEMO:
        src = V.show(BASE, 'tools/standing/handoff.py')
        m = types.ModuleType('handoff_base')
        m.__file__ = os.path.join(S, 'handoff.py')
        exec(compile(src, 'handoff.py@%s' % BASE, 'exec'), m.__dict__)   # noqa: S102
        _MEMO['H0'] = m
        _MEMO['src0'] = src
    return _MEMO['H0']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def _build(mod, relay=None):
    """('BUILT', page, yields) or ('REFUSED', words, []) for a module's page over the banks at the two heads or a planted copy."""
    src = mod.Source() if relay is None else mod.Planted(mod.Source(), relay=relay)
    try:
        P, Y = mod.build(src)
        return ('BUILT', P, Y['yields'])
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == 'Refuse':
            return ('REFUSED', str(e)[:150], [])
        raise


def _said(r):
    return 'BUILT, %d lines' % len(r[1]) if r[0] == 'BUILT' else 'REFUSED (%s)' % r[1]


def _place(r, act):
    """the yield's THE PLACE READ FROM ... for an act, or None."""
    for y in r[2]:
        if y.startswith('ACT %s ' % act) and 'THE PLACE READ FROM ' in y:
            return y[y.index('THE PLACE READ FROM ') + len('THE PLACE READ FROM '):]
    return None


def bank_lines():
    if 'bank' not in _MEMO:
        _MEMO['bank'] = H1.Source().relay(BANK)
    return _MEMO['bank']


def control_bank():
    L = ['### (bank): THE ORDERED CONTROL, b758`S PLACE READ FROM THE BANK']
    b, a = _build(base()), _build(H1)
    pa = _place(a, 'b758')
    return L, case(L, 'bank', 'the page over the banks at the two heads: where b758`s place is read', _said(b), '%s ; b758 from %s' % (_said(a), pa),
                   b[0] == 'REFUSED', pa == '%s :7' % BANK), 1


def control_ferry():
    L = ['### (ferry): THE ORDERED CONTROL, b757`S PLACE READ FROM ITS FERRY']
    b, a = _build(base()), _build(H1)
    pa = _place(a, 'b757')
    return L, case(L, 'ferry', 'the page over the banks at the two heads: where b757`s place is read', _said(b), '%s ; b757 from %s' % (_said(a), pa),
                   b[0] == 'REFUSED', pa == 'data/b757_ferry.txt :31'), 1


def control_neither():
    L = ['### (neither): THE ORDERED CONTROL, AN ACT WITH NEITHER']
    bl = bank_lines()
    planted = [l for l in bl if not l.startswith('b758 | ')]
    b, a = _build(base(), {BANK: planted}), _build(H1, {BANK: planted})
    return L, case(L, 'neither', '%s planted without b758`s row (%d of %d lines)' % (BANK, len(planted), len(bl)), _said(b), _said(a), b[0] == 'REFUSED',
                   a[0] == 'REFUSED' and 'data/b758_ferry.txt' in a[1] and '0 times in the places banks' in a[1] and _place(a, 'b758') is None), 1


def control_twice():
    L = ['### (twice): b758`S ROW TWICE']
    bl = bank_lines()
    planted = bl + [l for l in bl if l.startswith('b758 | ')]
    b, a = _build(base(), {BANK: planted}), _build(H1, {BANK: planted})
    return L, case(L, 'twice', '%s planted with b758`s row copied to its end' % BANK, _said(b), _said(a), b[0] == 'REFUSED',
                   a[0] == 'REFUSED' and 'data/b758_ferry.txt' in a[1] and '2 times' in a[1] and 'one wanted' in a[1]), 1


def control_first():
    L = ['### (first): THE FERRY READ BEFORE ANY BANK']
    bl = bank_lines()
    planted = bl + ["b757 | THE ACT'S PLACE. a planted row"]
    b, a = _build(base(), {BANK: planted}), _build(H1, {BANK: planted})
    pa = _place(a, 'b757')
    quoted = a[0] == 'BUILT' and any('a planted row' in l for l in a[1])
    return L, case(L, 'first', '%s planted with a row for b757, whose ferry carries the line' % BANK, _said(b),
                   '%s ; b757 from %s ; the planted row quoted %s' % (_said(a), pa, quoted), b[0] == 'REFUSED',
                   pa == 'data/b757_ferry.txt :31' and not quoted), 1


def control_page():
    L = ['### (page): THE PAGE FROM THE BANKS AT THE TWO HEADS (nothing written)']
    b, a = _build(base()), _build(H1)
    acts = sum(1 for y in a[2] if y.startswith('ACT '))
    return L, case(L, 'page', 'build at relay and PLACE-papers HEAD', _said(b), '%s ; acts %d ; each place read %s' % (
        _said(a), acts, all('THE PLACE READ FROM' in y for y in a[2] if y.startswith('ACT '))),
                   b[0] == 'REFUSED' and 'b759_ferry.txt' in b[1], a[0] == 'BUILT' and len(a[1]) < H1.CAP and acts == H1.TWELVE), 1


def _ctl(mod):
    try:
        ok, out = mod.control()
        return ok, out[-1].strip('#* ')
    except Exception as e:  # noqa: BLE001
        return False, 'RAISED %s: %s' % (type(e).__name__, str(e)[:100])


def control_control():
    L = ['### (control): handoff.py`S OWN CONTROLS']
    (ob, sb), (oa, sa) = _ctl(base()), _ctl(H1)
    return L, case(L, 'control', 'handoff.py control', '%s ; %s' % (ob, sb), '%s ; %s' % (oa, sa), not ob, oa), 1


NAMED = ("      ferry line carrying it in any of its three wordings and with either apostrophe.",
         "Y['yields'].append('ACT b%d : %s :1 head line READ ; %s THE ACT`S PLACE %d line(s) %s ; the second shape %d %s' % (",
         "a, cp, fp, len(hits), [':%d' % k for k in hits], len(wide), [':%d' % k for k in wide]))",
         "if len(hits) != 1:",
         "raise Refuse('THE ACT`S PLACE read %d times in %s, one wanted' % (len(hits), fp))",
         "out.append((a, cp, quote(cp, 1, c[0], q, Y), fp, hits[0], quote(fp, hits[0], f[hits[0] - 1], q, Y)))",
         "rec = (len(P) < CAP, sum(1 for y in Y['yields'] if y.startswith('ACT ')), all('PLACE 1 line(s)' in y for y in Y['yields'] if y.startswith('ACT ')))",
         "case('RECORD', 'the page built from the banks at the two heads: under the cap, twelve acts, THE ACT`S PLACE once in each', rec, (True, TWELVE, True))",
         "fp, cp = 'data/b%d_ferry.txt' % newest, 'data/b%d_closing.txt' % newest",
         "case('CONSTRUCTED', 'b%d`s ferry with its THE ACT`S PLACE line taken out: refused, naming that ferry' % newest,",
         "case('CONSTRUCTED', 'b%d`s THE ACT`S PLACE written with the curly apostrophe (b745`s form): found and quoted' % newest, got, True)",
         "case('CONSTRUCTED', 'b%d`s ferry carrying THE ACT`S PLACE twice: refused (one wanted)' % newest,")


def control_diff():
    L = ['### (diff): THE WORKING handoff.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'handoff.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:] for l in d if l[0] == '-']
    add = [l[1:] for l in d if l[0] == '+']
    odd = [r for r in rem if r not in NAMED and r.strip() not in NAMED]
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; removed named %d, other %d %s' % (len(rem), len(add), len(rem) - len(odd), len(odd), [o.strip()[:60] for o in odd]),
                   len(s0) > 400, len(rem) > 0 and not odd), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.8', ver == 'v1.36.9'), 1


CONTROLS = dict(bank=control_bank, ferry=control_ferry, neither=control_neither, twice=control_twice, first=control_first, page=control_page,
                control=control_control, diff=control_diff, version=control_version)
ORDER = ('bank', 'ferry', 'neither', 'twice', 'first', 'page', 'control', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.9, (R370)(5)(ii): THE PLACE OF AN ACT WHOSE FERRY CARRIES NONE (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'the page built in memory, the planted banks in memory; no protected line and not the quoting rule`s word printed; written through '
           'tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/handoff.py at %s) and after (the working file); nothing written' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, str(e)[:160])], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.36.9: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1369.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
