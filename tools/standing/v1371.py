# -*- coding: utf-8 -*-
"""standing/v1371.py -- THE CONTROLS OF v1.37.1, (R370)(5)(iv) AND (4): THE REMOVAL ROUTE'S TABLE OPENED FOR b760, in v1367.py's form.

The ruling's words (relay data/b760_ferry.txt :17): "(iv) THE REMOVAL ROUTE'S TABLE opens SIDE-explicit-formula for b760, for the one kernel
branch of (4)"; :15: "The branch push-b759-weil of SIDE-explicit-formula is deleted at its remote by the standing removal route, read there to
be an ancestor of main before and read absent after. ... That list's entry for the kernel's branch of the sentence before lapses with it."
tools/standing/commit.py's RDELETE_ACTS (v1.36.3) named b759 alone, so `rdelete push-b759-weil` was refused for b760 before anything was read.
v1.37.1 opens that one name at that one kernel for b760. BEFORE is commit.py at BASE, executed as a module of its own; AFTER the working file.
Pure functions alone are called, and the act's worklist read for its kept list: nothing is written and no git command is run.

  (open)      THE ORDERED CONTROL: rdelete_refusal(SIDE-explicit-formula, b760, push-b759-weil), the kept list the worklist's: before
              refused, after None.
  (closed)    SIDE-dirichlet-mod-24 for b760: push-b757-mod24 and push-b759-weil refused before and after.
  (named)     at SIDE-explicit-formula for b760, every other name refused after: b759's four, main, a kept name, b760's own push branch.
  (kept)      the worklist's kept list at SIDE-explicit-formula lacks push-b759-weil; a kept list planted with it refuses the removal.
  (b759)      b759's row unmoved: its five names at its two kernels, before and after equal.
  (holds)     KERNEL_ACTS, FF_ACTS and PUSHTO_ACTS name no b760: repo_refusal, ff_refusal and pushto_refusal refused before and after.
  (plan)      rdelete_plan: an absent branch, a tip outside the clone and a tip no ancestor of main refused; all read and an ancestor 'remove'.
  (diff)      the working commit.py against BASE's: the one line removed is b759's row's closing, re-closed for b760's row.
  (version)   tools/standing/VERSION moved to v1.37.1.

  python -X utf8 -u tools/standing/v1371.py control [open|closed|named|kept|b759|holds|plan|diff|version ...] [--bank]
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
BASE = 'a8f8403a'   # ### the relay's HEAD before this change (b760 component 2, step 15, v1.37.0)
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
WEIL = 'push-b759-weil'
B759 = ('push-b757-join', 'push-b757-coeff', 'push-b758-land', 'push-b758-coeff')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as C1             # noqa: E402  (the working file: AFTER)
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def base():
    """commit.py at BASE, executed as a module of its own (its __main__ guard keeps main() unrun)."""
    if 'C0' not in _MEMO:
        src = V.show(BASE, 'tools/standing/commit.py')
        m = types.ModuleType('commit_base')
        m.__file__ = os.path.join(S, 'commit.py')
        exec(compile(src, 'commit.py@%s' % BASE, 'exec'), m.__dict__)   # noqa: S102
        _MEMO['C0'] = m
        _MEMO['src0'] = src
    return _MEMO['C0']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def _r(x):
    return 'None' if x is None else 'REFUSED (%s)' % x[:90]


def control_open():
    L = ['### (open): THE ORDERED CONTROL, push-b759-weil AT SIDE-explicit-formula FOR b760, THE KEPT LIST THE WORKLIST`S']
    b, a = base().rdelete_refusal(EF, 'b760', WEIL), C1.rdelete_refusal(EF, 'b760', WEIL)
    return L, case(L, 'open', 'rdelete_refusal(%s, b760, %s)' % (EF, WEIL), _r(b), _r(a), b is not None and 'DOES NOT OPEN' in b, a is None), 1


def control_closed():
    L = ['### (closed): SIDE-dirichlet-mod-24 FOR b760, CLOSED']
    names = ('push-b757-mod24', WEIL)
    b = [base().rdelete_refusal(M24, 'b760', n, kept=()) for n in names]
    a = [C1.rdelete_refusal(M24, 'b760', n, kept=()) for n in names]
    return L, case(L, 'closed', 'rdelete_refusal(%s, b760, %s)' % (M24, ' | '.join(names)), [_r(x)[:50] for x in b], [_r(x)[:50] for x in a],
                   all(x is not None for x in b), all(x is not None for x in a)), 1


def control_named():
    L = ['### (named): EVERY OTHER NAME AT SIDE-explicit-formula FOR b760']
    kept = C1.kept_names('b760', EF)
    names = B759 + ('main', kept[0] if kept else 'challenge-b720-h2-sign-iff-rh', 'push-b760-weil')
    a = [C1.rdelete_refusal(EF, 'b760', n) for n in names]
    return L, case(L, 'named', 'names: %s' % ', '.join(names), 'not read (the kernel closed for b760 at BASE: case (open))',
                   'refused %d of %d' % (sum(1 for x in a if x is not None), len(names)), True, all(x is not None for x in a)), 1


def control_kept():
    L = ['### (kept): THE KEPT LIST']
    kept = C1.kept_names('b760', EF)
    p = C1.rdelete_refusal(EF, 'b760', WEIL, kept=kept + (WEIL,))
    return L, case(L, 'kept', 'kept_names(b760, %s), then the same list planted with %s' % (EF, WEIL), 'not read (case (open))',
                   'kept %s ; %s on it %s ; planted: %s' % (list(kept), WEIL, WEIL in kept, _r(p)[:70]), True,
                   WEIL not in kept and p is not None and 'KEPT LIST' in p), 1


def control_b759():
    L = ['### (b759): b759`S ROW UNMOVED']
    b = (base().RDELETE_ACTS.get('b759'), [base().rdelete_refusal(EF, 'b759', n, kept=()) for n in B759])
    a = (C1.RDELETE_ACTS.get('b759'), [C1.rdelete_refusal(EF, 'b759', n, kept=()) for n in B759])
    return L, case(L, 'b759', 'RDELETE_ACTS[b759] and its four names at %s' % EF, '%r ; all None %s' % (b[0], all(x is None for x in b[1])),
                   'equal to BEFORE %s ; all None %s' % (a[0] == b[0], all(x is None for x in a[1])),
                   all(x is None for x in b[1]), a[0] == b[0] and all(x is None for x in a[1])), 1


def control_holds():
    L = ['### (holds): NO OTHER KERNEL WRITE OPENED FOR b760']
    def three(m):
        return [m.repo_refusal(EF, 'b760'), m.ff_refusal(EF, 'b760'), m.pushto_refusal(EF, 'b760')]
    b, a = three(base()), three(C1)
    return L, case(L, 'holds', 'repo_refusal, ff_refusal, pushto_refusal at %s for b760' % EF, [x is not None for x in b], [x is not None for x in a],
                   all(x is not None for x in b), all(x is not None for x in a)), 1


def _plan(m, *a):
    try:
        return m.rdelete_plan(*a)
    except m.Refused as e:
        return 'REFUSED (%s)' % str(e)[:40]


def control_plan():
    L = ['### (plan): THE ANCESTRY READ BEFORE THE REMOVAL (pure)']
    M_, W_ = 'a3aad4cc' + '0' * 32, 'a3aad4cc' + '0' * 32
    rows = (('', W_, M_, W_, True), (M_, '', M_, '', False), (M_, W_, M_, '', False), (M_, W_, M_, W_, False), (M_, W_, M_, W_, True))
    b = [_plan(base(), *r) for r in rows]
    a = [_plan(C1, *r) for r in rows]
    want = [False, False, False, False, True]
    return L, case(L, 'plan', 'main unread ; branch absent ; tip not in the clone ; tip no ancestor ; all read and an ancestor',
                   [x == 'remove' for x in b], [x == 'remove' for x in a], [x == 'remove' for x in b] == want, [x == 'remove' for x in a] == want), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    add = [l[1:].strip() for l in d if l[0] == '+']
    row = "'b760': {'SIDE-explicit-formula': ('push-b759-weil',)}}"
    ok = rem == ["'SIDE-dirichlet-mod-24': ('push-b757-mod24',)}}"] and add.count(row) == 1 and \
        "'SIDE-dirichlet-mod-24': ('push-b757-mod24',)}," in add
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed %s ; %d added ; b760`s row added %d' % (len(rem), [r[:50] for r in rem], len(add), add.count(row)), len(s0) > 1000, ok), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.37.0', ver == 'v1.37.1'), 1


CONTROLS = dict(open=control_open, closed=control_closed, named=control_named, kept=control_kept, b759=control_b759, holds=control_holds,
                plan=control_plan, diff=control_diff, version=control_version)
ORDER = ('open', 'closed', 'named', 'kept', 'b759', 'holds', 'plan', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.37.1, (R370)(5)(iv) AND (4): THE REMOVAL ROUTE`S TABLE OPENED FOR b760 (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/commit.py at %s) and after (the working file); pure functions alone and the worklist read, '
           'nothing written, no git command run' % BASE, '']
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
    out.append('### ### **v1.37.1: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1371.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
