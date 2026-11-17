# -*- coding: utf-8 -*-
"""standing/v1367.py -- THE CONTROLS OF v1.36.7, (R369)(5) AND (11): THE KERNEL ROUTE OPENED FOR b759, in v1359.py's form.

The ruling's words (relay data/b759_ferry.txt :21): "THE HOLDS "no kernel's main touched" and "no branch merged" are lifted for
SIDE-explicit-formula in this act alone, by the author's word in this delivery"; ":33": "no kernel touched beyond SIDE-explicit-formula's tree
and the five branches of (3)". tools/standing/commit.py opens the kernels act by act (KERNEL_ACTS, v1.35.4; FF_ACTS, v1.36.0) and named b757
and b758 alone, so every kernel write of b759's Component 3 was refused before it was read (the seat's read of what the ruling misses, its
second printing). v1.36.7 opens SIDE-explicit-formula for b759 in both tables; SIDE-dirichlet-mod-24 stays closed; no file is named for a
conflicted merge. BEFORE is commit.py at BASE, executed as a module of its own; AFTER the working file. Pure functions alone are called:
nothing is written and no git command is run.

  (open)      repo_refusal('SIDE-explicit-formula', 'b759'): before refused, after None.
  (closed)    repo_refusal('SIDE-dirichlet-mod-24', 'b759'): refused before and after.
  (b758)      repo_refusal for b758 at SIDE-explicit-formula None, at SIDE-dirichlet-mod-24 refused, before and after (b758's opening unmoved).
  (other)     repo_refusal('SIDE-explicit-formula', 'b760') and a third repository's name for b759: refused before and after.
  (ff)        ff_refusal at SIDE-explicit-formula for b759: before refused, after None; at SIDE-dirichlet-mod-24 for b759 refused after.
  (named)     conflict_refusal for b759 at SIDE-explicit-formula: print_targets.txt refused before and after (no merge named).
  (branch)    kernel_branch_refusal('b759', ...): push-b759-weil None; push-b758-coeff and main refused (unchanged).
  (diff)      the working commit.py against BASE's: the lines removed are KERNEL_ACTS's b758 row and FF_ACTS's, each re-closed for b759's row.
  (version)   tools/standing/VERSION moved to v1.36.7.

  python -X utf8 -u tools/standing/v1367.py control [open|closed|b758|other|ff|named|branch|diff|version ...] [--bank]
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
BASE = '8fc653fc'   # ### the relay's HEAD before this change (b759 component 2, step 12, v1.36.6)
EF, M24 = 'SIDE-explicit-formula', 'SIDE-dirichlet-mod-24'
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
    L = ['### (open): SIDE-explicit-formula FOR b759']
    b, a = base().repo_refusal(EF, 'b759'), C1.repo_refusal(EF, 'b759')
    return L, case(L, 'open', 'repo_refusal(%s, b759)' % EF, _r(b), _r(a), b is not None, a is None), 1


def control_closed():
    L = ['### (closed): SIDE-dirichlet-mod-24 FOR b759, CLOSED TO THIS ROUTE']
    b, a = base().repo_refusal(M24, 'b759'), C1.repo_refusal(M24, 'b759')
    return L, case(L, 'closed', 'repo_refusal(%s, b759)' % M24, _r(b), _r(a), b is not None, a is not None), 1


def control_b758():
    L = ['### (b758): b758`S OPENING UNMOVED']
    b = [base().repo_refusal(k, 'b758') for k in (EF, M24)]
    a = [C1.repo_refusal(k, 'b758') for k in (EF, M24)]
    return L, case(L, 'b758', 'repo_refusal at both kernels for b758', [_r(x)[:40] for x in b], [_r(x)[:40] for x in a],
                   b[0] is None and b[1] is not None, a[0] is None and a[1] is not None), 1


def control_other():
    L = ['### (other): ANOTHER ACT, AND A THIRD REPOSITORY']
    b = [base().repo_refusal(EF, 'b760'), base().repo_refusal('SIDE-lv-conservation', 'b759')]
    a = [C1.repo_refusal(EF, 'b760'), C1.repo_refusal('SIDE-lv-conservation', 'b759')]
    return L, case(L, 'other', '(%s, b760) and (SIDE-lv-conservation, b759)' % EF, [_r(x) for x in b], [_r(x) for x in a],
                   all(x is not None for x in b), all(x is not None for x in a)), 1


def control_ff():
    L = ['### (ff): THE LOCAL MAIN`S FAST-FORWARD FOR b759']
    b, a = base().ff_refusal(EF, 'b759'), C1.ff_refusal(EF, 'b759')
    a2 = C1.ff_refusal(M24, 'b759')
    return L, case(L, 'ff', 'ff_refusal(%s, b759) ; then (%s, b759) after' % (EF, M24), _r(b), '%s ; %s' % (_r(a), _r(a2)),
                   b is not None, a is None and a2 is not None), 1


def control_named():
    L = ['### (named): NO FILE NAMED FOR A CONFLICTED MERGE AT b759']
    b = base().conflict_refusal('b759', EF, ['print_targets.txt'])
    a = C1.conflict_refusal('b759', EF, ['print_targets.txt'])
    return L, case(L, 'named', 'conflict_refusal(b759, %s, print_targets.txt)' % EF, _r(b), _r(a), b is not None, a is not None), 1


def control_branch():
    L = ['### (branch): THE ACT`S PUSH BRANCH']
    names = ('push-b759-weil', 'push-b758-coeff', 'main')
    b = [base().kernel_branch_refusal('b759', n) is None for n in names]
    a = [C1.kernel_branch_refusal('b759', n) is None for n in names]
    want = [True, False, False]
    return L, case(L, 'branch', 'passed: %s' % ', '.join(names), b, a, b == want, a == want), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:].strip() for l in d if l[0] == '-']
    add = [l[1:].strip() for l in d if l[0] == '+']
    ok = len(rem) == 2 and all(r.startswith(("'b758': ('SIDE-explicit-formula',)}", "FF_ACTS = {'b758'")) for r in rem) \
        and sum(1 for x in add if x.startswith("'b759': ('SIDE-explicit-formula',)")) == 2
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; the removed: %s ; b759`s rows added %d' % (len(rem), len(add), [r[:50] for r in rem],
                                                                                   sum(1 for x in add if x.startswith("'b759': ('SIDE-explicit-formula',)"))),
                   len(s0) > 1000, ok), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.6', ver == 'v1.36.7'), 1


CONTROLS = dict(open=control_open, closed=control_closed, b758=control_b758, other=control_other, ff=control_ff, named=control_named,
                branch=control_branch, diff=control_diff, version=control_version)
ORDER = ('open', 'closed', 'b758', 'other', 'ff', 'named', 'branch', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.7, (R369)(5) AND (11): THE KERNEL ROUTE OPENED FOR b759 (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/commit.py at %s) and after (the working file); pure functions alone, nothing written' % BASE, '']
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
    out.append('### ### **v1.36.7: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1367.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
