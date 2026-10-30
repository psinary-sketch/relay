# -*- coding: utf-8 -*-
"""standing/v160.py -- THE CONTROLS OF v1.6.0 ((R336)(2)(iii)), in v150.py's form: each instance replayed through the route as it stood at HEAD
before the repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Written at b726 by
the Write tool.

  python -X utf8 tools/standing/v160.py control [closing|scores ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v160.txt with every control run, nothing else.
"""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402

BASE = 'HEAD'   # ### the routes before the repair: v1.6.0's files are uncommitted when the controls run, so HEAD carries v1.5.0's
TMP = tempfile.mkdtemp(prefix='v160_')
B725_SESSION = '02c7cf38-4c6a-4f88-b813-a7e15e9b85b4'
B725_ANCHOR = 'RULING (R335) BEGIN'
B725_SEAL = '1e37ee28'          # ### b725's step row 32, phase seal (data/b725_steps.json)
PROJ = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
NEEDLE = 'no identifier of the author ' + 'in any outbound'
ARM = 'G-RULE-SCORES-BEFORE-SEAL'


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob(rel, rev=None):
    r = subprocess.run(['git', '-C', RELAY, 'show', '%s:%s' % (rev or BASE, rel)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def old_module(rel, name):
    """the module at BASE, loaded from a temporary copy under its own name (the live module untouched)"""
    p = os.path.join(TMP, name + '.py')
    with open(p, 'wb') as f:
        f.write(blob(rel))
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.5.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.6.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


# ================================================================================ (closing) THE SENTENCE READ UNWRAPPED
def control_closing():
    """b725 event (5): G-CLOSING-SENTENCE's needle on a sentence the render hard-wraps between "in any" and "outbound". The search text as
    the template reads it now (its own regex, taken from the template's line, not retyped here) over b725's render; the new plant over the
    same render must fail the predicate, and the old plant must have changed nothing."""
    import repeat as RP
    L = ['### (closing) G-CLOSING-SENTENCE -- checks.tpl closing_sentence_ok; instance: tools/acts/b725.py`s closing as rendered (event (5))']
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    m = re.search(r't = re\.sub\(r"(.*?)", \' \', S\[\'closing_src\'\]\)', tpl)
    if not m:
        return L + ['  ### THE TEMPLATE`S SEARCH TEXT NOT READ -- NOT AS WANTED'], 0, 1
    rx = m.group(1)
    src = RP.src(T, 'b725', 'closing')
    flat = re.sub(rx, ' ', src)
    L.append('  the regex read from the template: %s ; the render %d chars, unwrapped %d' % (rx, len(src), len(flat)))
    g = case(L, 'closing', 'the sentence in b725`s render', 'the needle in the raw render %s' % (NEEDLE in src),
             'the needle in the unwrapped render %s' % (NEEDLE in flat), NEEDLE not in src, NEEDLE in flat)
    planted = re.sub(rx, ' ', src.replace('no identifier of the author ' + 'in any', 'x'))
    old_changes = src.replace(NEEDLE, 'x') != src
    g2 = case(L, 'closing', 'the arm`s plant on the same render', 'the old plant changes the render %s' % old_changes,
              'after the new plant the needle in the unwrapped render %s' % (NEEDLE in planted), not old_changes, NEEDLE not in planted)
    return L, int(g) + int(g2), 2


# ================================================================================ (scores) THE FOLD'S ROUTE READ
def control_scores():
    """b725 event (8): tools/rule_arms.py :458 counted calls of "b725_record.py scores"; the fold's route is `fold.py record scores`, so the
    reader read 0 calls. Both readers over b725's own call trace, with b725's seal commit; b723 and b724 carry the same failure, read once."""
    import rule_arms as RA
    L = ['### (scores) G-RULE-SCORES-BEFORE-SEAL -- tools/rule_arms.py :458; instance: b725`s session, its seal %s (event (8))' % B725_SEAL]
    R0 = old_module('tools/rule_arms.py', 'rule_arms_v150')
    calls = RA.transcript(os.path.join(PROJ, B725_SESSION + '.jsonl'), B725_ANCHOR)
    ct = int(_git(RELAY, 'log', '-1', '--format=%ct', B725_SEAL).strip())
    R = dict(act='b725', calls=calls, seal_ct=ct, n=725)
    r0, r1 = R0.reading(ARM, R), RA.reading(ARM, R)
    L.append('  the calls read from the session %d ; the seal commit time %d' % (len(calls), ct))
    g = case(L, 'scores', 'b725`s calls through the arm`s reading', 'ok %s, calls %d ; %s' % (r0[0], r0[1], r0[3]),
             'ok %s, calls %d ; %s' % (r1[0], r1[1], r1[3]), not r0[0], r1[0])
    late = RA.reading(ARM, dict(R, seal_ct=1))
    g2 = case(L, 'scores', 'the same calls against a seal planted before every call', 'not read (the old reader finds no call)',
              'ok %s ; %s' % (late[0], late[3]), not r0[0], not late[0])
    return L, int(g) + int(g2), 2


CONTROLS = dict(closing=control_closing, scores=control_scores)
ORDER = ('closing', 'scores')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.6.0, (R336)(2)(iii): G-CLOSING-SENTENCE`S SEARCH TEXT UNWRAPPED, G-RULE-SCORES-BEFORE-SEAL`S READER '
           'ON THE FOLD`S ROUTE (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
           '### the routes before the repair read at %s (%s); each case its instance through both' % (BASE, _git(RELAY, 'rev-parse', '--short=8', BASE).strip()), '']
    tg = tn = 0
    try:
        for k in names:
            try:
                L, g, n = CONTROLS[k]()
            except Exception as e:  # noqa: BLE001
                L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
            out += L + ['']
            tg, tn = tg + g, tn + n
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    out.append('### ### **v1.6.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (
        ', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v160.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v160.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
