# -*- coding: utf-8 -*-
"""standing/v1368.py -- THE CONTROLS OF v1.36.8, (R370)(5)(i): THE ANCHOR OF RULE [Q] (3) READ BY ITS HEADING'S DIGEST, in v1367.py's form.

The ruling's words (relay data/b760_ferry.txt :17), the author's: "tools/standing/handoff.py, and each tool that reads REGISTRY's protected
section by the number 373, finds the heading by the sha256 of its line, opening 53d53060a58f6b9b, and prints the line it stands at, :374 at
b759's close with its section running to :400; refused where no line carries that digest or more than one does. Its controls: a line planted
above the heading leaves the section found one line down; the heading removed is refused; a second such heading is refused." Among the
standing tools handoff.py alone read REGISTRY by that number (relay data/b760_misses.txt (2)); b754's sealed readers stand outside the (W)
list and are not edited. BEFORE is handoff.py at BASE, executed as a module of its own; AFTER the working file. Every case reads REGISTRY
through git at PLACE-papers' HEAD or a copy of it planted in memory; nothing is written, no line of the protected section is printed, and the
rule's word is printed nowhere (each case prints line numbers, counts and refusals alone).

  (found)      the heading at the record: BEFORE refused (its line read blank); AFTER found at :374, its section :374-:400.
  (above)      THE ORDERED CONTROL: a line planted above the heading: AFTER the heading at :375, its section one line down.
  (removed)    THE ORDERED CONTROL: the heading removed: refused, no line carrying the digest.
  (second)     THE ORDERED CONTROL: a second such heading: refused, two lines carrying the digest.
  (protected)  the protected set over REGISTRY: BEFORE's set misses most of the section; AFTER's covers it whole.
  (page)       the page: BEFORE refused at the quoting rule; AFTER refused, if at all, at a later needle (the place of (5)(ii)).
  (nonum)      the number read nowhere in the working file; BEFORE's file carries it.
  (diff)       the working handoff.py against BASE's: every line removed carries the number or is one of the lines the change names.
  (version)    tools/standing/VERSION moved to v1.36.8.

  python -X utf8 -u tools/standing/v1368.py control [found|above|removed|second|protected|page|nonum|diff|version ...] [--bank]
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
BASE = 'e90e0860'   # ### the relay's HEAD before this change (b760 component 1, step 9, v1.36.7)
NUM = '3' + '73'    # ### the number the heading stood at before b759's REGISTRY row moved it; spelt in two parts so this file's own read is clean
WANT_LINE, WANT_END = 374, 400
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


def src1():
    return io.open(os.path.join(S, 'handoff.py'), encoding='utf-8').read().replace('\r', '')


def reg():
    if 'reg' not in _MEMO:
        _MEMO['src'] = H1.Source()
        _MEMO['reg'] = _MEMO['src'].pp('REGISTRY.md')
    return _MEMO['reg']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def _q(mod, planted=None):
    """('REFUSED', words) or ('FOUND', line, (first, last, count)) for a module's qword over REGISTRY at PLACE-papers' HEAD or a planted copy;
    no line of REGISTRY is returned."""
    reg()
    src = _MEMO['src'] if planted is None else H1.Planted(_MEMO['src'], pp={'REGISTRY.md': planted})
    try:
        q = mod.qword(src)
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == 'Refuse':
            return ('REFUSED', str(e)[:150])
        raise
    if len(q) < 4:
        return ('FOUND', None, None)
    lines = planted if planted is not None else reg()
    sec = sorted(H1._section(lines, q[3], q[2]))
    return ('FOUND', q[3], (sec[0], sec[-1], len(sec)))


def control_found():
    L = ['### (found): THE HEADING AT THE RECORD, PLACE-papers REGISTRY.md AT ITS HEAD']
    b, a = _q(base()), _q(H1)
    return L, case(L, 'found', 'qword over REGISTRY.md at PLACE-papers %s: the line and the section`s first line, last line and count' % _MEMO['src'].phead,
                   b, a, b[0] == 'REFUSED', a[0] == 'FOUND' and a[1] == WANT_LINE and a[2][:2] == (WANT_LINE, WANT_END)), 1


def control_above():
    L = ['### (above): THE ORDERED CONTROL, A LINE PLANTED ABOVE THE HEADING']
    r = reg()
    a0 = _q(H1)
    k = a0[1]
    planted = r[:k - 1] + ['a planted line'] + r[k - 1:]
    b, a = _q(base(), planted), _q(H1, planted)
    ok = a[0] == 'FOUND' and a[1] == k + 1 and a[2] == (a0[2][0] + 1, a0[2][1] + 1, a0[2][2])
    return L, case(L, 'above', 'a line planted at :%d, the heading below it' % k, b, '%s ; the heading one line down %s, its section one line down %s' % (
        a, a[1] == k + 1 if a[0] == 'FOUND' else False, ok), True, ok), 1


def control_removed():
    L = ['### (removed): THE ORDERED CONTROL, THE HEADING REMOVED']
    r = reg()
    k = _q(H1)[1]
    planted = r[:k - 1] + r[k:]
    b, a = _q(base(), planted), _q(H1, planted)
    return L, case(L, 'removed', 'REGISTRY.md with its line :%d removed' % k, b, a, True,
                   a[0] == 'REFUSED' and '0 lines carry' in a[1] and 'cannot run' in a[1]), 1


def control_second():
    L = ['### (second): THE ORDERED CONTROL, A SECOND SUCH HEADING']
    r = reg()
    k = _q(H1)[1]
    planted = r + [r[k - 1]]
    b, a = _q(base(), planted), _q(H1, planted)
    return L, case(L, 'second', 'REGISTRY.md with its line :%d copied to its end' % k, b, a, True,
                   a[0] == 'REFUSED' and '2 lines carry' in a[1] and 'cannot run' in a[1]), 1


def control_protected():
    L = ['### (protected): THE PROTECTED SET OVER REGISTRY.md']
    r = reg()
    q = H1.qword(_MEMO['src'])
    sec = H1._section(r, q[3], q[2])
    pb = base().protected('REGISTRY.md', r, q[:3])
    pa = H1.protected('REGISTRY.md', r, q)
    mb, ma = len(sec - pb), len(sec - pa)
    return L, case(L, 'protected', 'the section`s %d lines (:%d-:%d) outside the protected set' % (len(sec), min(sec), max(sec)),
                   'missing %d of %d (the set %d lines)' % (mb, len(sec), len(pb)), 'missing %d of %d (the set %d lines)' % (ma, len(sec), len(pa)),
                   mb > 0, ma == 0), 1


def _page(mod):
    try:
        P, Y = mod.build(mod.Source())
        return 'BUILT, %d lines' % len(P)
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == 'Refuse':
            return 'REFUSED (%s)' % str(e)[:140]
        raise


def control_page():
    L = ['### (page): THE PAGE FROM THE BANKS AT THE TWO HEADS (nothing written)']
    b, a = _page(base()), _page(H1)
    return L, case(L, 'page', 'build at relay and PLACE-papers HEAD', b, a, b.startswith('REFUSED') and 'cannot run' in b,
                   'quoting rule' not in a and 'cannot run' not in a), 1


def control_nonum():
    L = ['### (nonum): THE NUMBER READ NOWHERE']
    base()
    nb, na = _MEMO['src0'].count(NUM), src1().count(NUM)
    return L, case(L, 'nonum', 'occurrences of the number in handoff.py', nb, na, nb > 0, na == 0), 1


NAMED = ("FINDINGS :820-:826, OPEN_TRAILS' O.7 whole, two lines either side of the word in a ledger), is cited by path, line and the opening",
         'sixteen characters of its sha256 and not quoted. The word itself is printed nowhere.',
         'rx, _w, level = q', 'rx, word, _lv = qword(base)', "return re.compile(r'\\b%s\\b' % re.escape(m.group(2)), re.I), m.group(2), len(m.group(1))",
         "m = re.match(r'^(#+)\\s*\\**\\s*([A-Za-z][A-Za-z\\-]*)', reg[372])")


def control_diff():
    L = ['### (diff): THE WORKING handoff.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = src1().split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    add = [l[1:].strip() for l in d if l[0] == '+']
    odd = [r for r in rem if NUM not in r and r not in NAMED]
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; removed carrying the number %d, named %d, other %d %s' % (
                       len(rem), len(add), sum(1 for r in rem if NUM in r), sum(1 for r in rem if r in NAMED), len(odd), [o[:50] for o in odd]),
                   len(s0) > 400, len(rem) > 0 and not odd), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.7', ver == 'v1.36.8'), 1


CONTROLS = dict(found=control_found, above=control_above, removed=control_removed, second=control_second, protected=control_protected,
                page=control_page, nonum=control_nonum, diff=control_diff, version=control_version)
ORDER = ('found', 'above', 'removed', 'second', 'protected', 'page', 'nonum', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.8, (R370)(5)(i): THE ANCHOR OF RULE [Q] (3) READ BY ITS HEADING`S DIGEST (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'REGISTRY read through git, its planted copies in memory; no protected line and not the rule`s word printed; written through '
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
    out.append('### ### **v1.36.8: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1368.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
