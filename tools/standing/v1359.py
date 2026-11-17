# -*- coding: utf-8 -*-
"""standing/v1359.py -- THE CONTROLS OF v1.35.9, (R368)(5) AND (10): THE KERNEL ROUTE OPENED FOR b758, in v1358.py's form.

The ruling's words (relay data/b758_ferry.txt :17): "the holds "no kernel's main touched" and "no branch merged" are lifted for
SIDE-explicit-formula in this act alone"; ":27": "no kernel touched beyond SIDE-explicit-formula's tree and the two local mains of (6)(i)";
":17": "One file is named for a conflicted merge: print_targets.txt". tools/standing/commit.py opens the kernels act by act (KERNEL_ACTS,
v1.35.4) and named b757 alone, so every kernel write of b758's Components 2 and 3 was refused before it was read. v1.35.9 opens
SIDE-explicit-formula for b758 and names print_targets.txt for its conflicted merge; SIDE-dirichlet-mod-24 stays closed to this route, its local
main moved by (6)(i)'s route alone. BEFORE is commit.py at BASE, executed as a module of its own; AFTER the working file. Pure functions alone
are called: nothing is written and no git command is run.

  (open)      repo_refusal('SIDE-explicit-formula', 'b758'): before refused, after None.
  (closed)    repo_refusal('SIDE-dirichlet-mod-24', 'b758'): refused before and after.
  (b757)      repo_refusal for b757 at both kernels: None before and after (b757's opening unmoved).
  (other)     repo_refusal('SIDE-explicit-formula', 'b759') and a third repository's name for b758: refused before and after.
  (named)     conflict_refusal for b758 at SIDE-explicit-formula: print_targets.txt before refused, after None; a Lean file after refused.
  (branch)    kernel_branch_refusal('b758', ...): push-b758-land and push-b758-coeff None; push-b757-join and main refused (unchanged).
  (diff)      the working commit.py against BASE's: the lines changed are KERNEL_ACTS's and NAMED_CONFLICTS's alone.
  (version)   tools/standing/VERSION moved to v1.35.9.

  python -X utf8 -u tools/standing/v1359.py control [open|closed|b757|other|named|branch|diff|version ...] [--bank]
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
BASE = '2f3287de'   # ### the relay's HEAD before this change (b758 component 1, step 19)
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
        exec(compile(src, 'commit.py@%s' % BASE, 'exec'), m.__dict__)
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
    L = ['### (open): SIDE-explicit-formula FOR b758']
    b, a = base().repo_refusal(EF, 'b758'), C1.repo_refusal(EF, 'b758')
    return L, case(L, 'open', 'repo_refusal(%s, b758)' % EF, _r(b), _r(a), b is not None, a is None), 1


def control_closed():
    L = ['### (closed): SIDE-dirichlet-mod-24 FOR b758, CLOSED TO THIS ROUTE']
    b, a = base().repo_refusal(M24, 'b758'), C1.repo_refusal(M24, 'b758')
    return L, case(L, 'closed', 'repo_refusal(%s, b758)' % M24, _r(b), _r(a), b is not None, a is not None), 1


def control_b757():
    L = ['### (b757): b757`S OPENING UNMOVED']
    b = [base().repo_refusal(k, 'b757') for k in (EF, M24)]
    a = [C1.repo_refusal(k, 'b757') for k in (EF, M24)]
    return L, case(L, 'b757', 'repo_refusal at both kernels for b757', b, a, b == [None, None], a == [None, None]), 1


def control_other():
    L = ['### (other): ANOTHER ACT, AND A THIRD REPOSITORY']
    b = [base().repo_refusal(EF, 'b759'), base().repo_refusal('SIDE-lv-conservation', 'b758')]
    a = [C1.repo_refusal(EF, 'b759'), C1.repo_refusal('SIDE-lv-conservation', 'b758')]
    return L, case(L, 'other', '(%s, b759) and (SIDE-lv-conservation, b758)' % EF, [_r(x) for x in b], [_r(x) for x in a],
                   all(x is not None for x in b), all(x is not None for x in a)), 1


def control_named():
    L = ['### (named): THE ONE FILE NAMED FOR (5)`S CONFLICTED MERGE']
    b = base().conflict_refusal('b758', EF, ['print_targets.txt'])
    a = C1.conflict_refusal('b758', EF, ['print_targets.txt'])
    a2 = C1.conflict_refusal('b758', EF, ['print_targets.txt', 'Schema/ZQ/OffZero/Time.lean'])
    return L, case(L, 'named', 'conflict_refusal(b758, %s): print_targets.txt ; then with a Lean file beside it (after)' % EF, _r(b),
                   '%s ; %s' % (_r(a), _r(a2)), b is not None, a is None and a2 is not None and 'Time.lean' in a2), 1


def control_branch():
    L = ['### (branch): THE ACT`S PUSH BRANCHES, UNCHANGED']
    names = ('push-b758-land', 'push-b758-coeff', 'push-b757-join', 'main')
    b = [base().kernel_branch_refusal('b758', n) is None for n in names]
    a = [C1.kernel_branch_refusal('b758', n) is None for n in names]
    want = [True, True, False, False]
    return L, case(L, 'branch', 'passed: %s' % ', '.join(names), b, a, b == want, a == want), 1


def control_diff():
    L = ['### (diff): THE WORKING commit.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    rem = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    keys = all(l[1:].lstrip().startswith(("KERNEL_ACTS", "NAMED_CONFLICTS", "'b758'")) for l in rem)
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d lines changed (%d removed, %d added), each KERNEL_ACTS`s or NAMED_CONFLICTS`s: %s' % (
                       len(rem), sum(1 for l in rem if l[0] == '-'), sum(1 for l in rem if l[0] == '+'), keys),
                   len(s0) > 900, keys and 0 < len(rem) <= 6), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.35.8', ver == 'v1.35.9'), 1


CONTROLS = dict(open=control_open, closed=control_closed, b757=control_b757, other=control_other, named=control_named,
                branch=control_branch, diff=control_diff, version=control_version)
ORDER = ('open', 'closed', 'b757', 'other', 'named', 'branch', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.35.9, (R368)(5) AND (10): THE KERNEL ROUTE OPENED FOR b758 (%s)' % (
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
    out.append('### ### **v1.35.9: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1359.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
