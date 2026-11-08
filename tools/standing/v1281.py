# -*- coding: utf-8 -*-
"""standing/v1281.py -- THE CONTROLS OF v1.28.1 ((R358)(3)(iv), b748 defect (k)), in v1280.py's form: each instance read through the route as it stood
before the repair (tools/standing/commit.py at BASE, v1.28.0's commit, loaded from its blob) and through the repaired route on disk; AS WANTED where
the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST. The free memory is
read and printed before each control. Written at b748 by the Write tool; no identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/v1281.py control [root|branch|rows|version ...] [--bank]
"""
import importlib.util
import io
import json
import os
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
BASE = 'bf83b65b'   # ### v1.28.0's commit at b748 Component 1, the route before this repair
B747 = ('7d34b587', 'bc1feeb5')   # ### b747's closing head and its closing commit: the range b747's step-rows commits are read in
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import subjects as SJ           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def old_cm():
    """commit.py as BASE left it, loaded from its blob under another name (its imports resolve against tools/standing as on disk)."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, 'commit_v1280.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(show(BASE, 'tools/standing/commit.py'))
    spec = importlib.util.spec_from_file_location('commit_v1280', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    shutil.rmtree(d, ignore_errors=True)
    return m


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.28.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.28.1): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.28.1): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _try(fn):
    try:
        return True, fn()
    except CM.Refused as e:
        return False, 'REFUSED: %s' % str(e)[:110]
    except Exception as e:  # noqa: BLE001 -- the old module's own Refused class
        if type(e).__name__ == 'Refused':
            return False, 'REFUSED: %s' % str(e)[:110]
        raise


# ================================================================================ (root) THE ROOT BANKS COMMIT THROUGH THE TOOL
def control_root():
    L, g, n = ['### (root) (R358)(3)(iv), b748 defect (k): THE ROOT BANKS COMMIT AN ACT PHASE OF THE ONE-CALL TOOL (b747 committed it by plain git, 66915db5)'], 0, 0
    OC = old_cm()
    w = 'the act root chained, the banks and the pre-root push captures'
    o_ok, o = _try(lambda: OC.act_check('b748', 'root', w))
    n_ok, nw = _try(lambda: CM.act_check('b748', 'root', w))
    n += 1
    g += case(L, 'root', 'act_check(b748, root, <words>)', o, nw, not o_ok, n_ok and nw == 'b748 root: ' + w)
    n += 1
    g += guard(L, 'root', 'the phase list in the subject composer`s order (pre-root, root, record)', ' '.join(CM.ACT_PHASES),
               CM.ACT_PHASES.index('pre-root') < CM.ACT_PHASES.index('root') < CM.ACT_PHASES.index('record') and 'root' in SJ.PHASES)
    n += 1
    b_ok, b = _try(lambda: CM.act_check('b748', 'roots', w))
    g += guard(L, 'root', 'a phase not in the list still refused', b, not b_ok)
    return L, g, n


# ================================================================================ (branch) THE PUSH BRANCH THROUGH THE TOOL
def control_branch():
    L, g, n = ['### (branch) (R358)(3)(iv), b748 defect (k): THE PUSH BRANCH MADE BY THE ONE-CALL TOOL UNDER THE WRITE MARK (b747 made push-b747-preroot, -record, -closing by plain git)'], 0, 0
    OC = old_cm()
    r = tempfile.mkdtemp(dir=SCRATCH)
    try:
        _git('init', '-q', repo=r)
        _git('-c', 'user.email=x@x.invalid', '-c', 'user.name=x', 'commit', '-q', '--allow-empty', '-m', 'base', repo=r)
        o_ok, o = _try(lambda: OC.write_route(r, 'branch', ['push-b999-preroot'], act='b999'))
        o_have = 'push-b999-preroot' in _git('branch', '--list', repo=r)
        n_ok, nw = _try(lambda: CM.write_route(r, 'branch', ['push-b999-preroot'], act='b999'))
        n_have = 'push-b999-preroot' in _git('branch', '--list', repo=r)
        n += 1
        g += case(L, 'branch', 'write_route(<scratch repository>, branch, push-b999-preroot) and the branch list after',
                  '%s ; branch made %s' % (o, 'YES' if o_have else 'NO'), '%s ; branch made %s' % ('WRITTEN' if n_ok else nw, 'YES' if n_have else 'NO'),
                  not o_ok and not o_have, n_ok and n_have)
        n += 1
        g += guard(L, 'branch', 'the write mark released after the branch', 'mark %s' % ('STANDS' if os.path.exists(CM.MARK) else 'ABSENT'), not os.path.exists(CM.MARK))
        for nm, want in (('main', False), ('push-b747-record', False), ('push-b999-x', False), ('push-b999-record', True), ('push-b999-closing', True)):
            bad = CM.branch_refusal('b999', 'branch', nm)
            n += 1
            g += guard(L, 'branch', 'branch_refusal(b999, %s): %s' % (nm, 'accepted' if want else 'refused'), bad or 'ACCEPTED', (bad is None) == want)
        t_ok, t = _try(lambda: CM.write_route(r, 'branch', ['push-b999-record', 'push-b999-closing'], act='b999'))
        n += 1
        g += guard(L, 'branch', 'two branches in one call refused', t, not t_ok)
    finally:
        shutil.rmtree(r, ignore_errors=True)
    return L, g, n


# ================================================================================ (rows) A STEP-ROWS COMMIT WRITES NO ROW OF ITS OWN
def control_rows():
    L, g, n = ['### (rows) (R358)(3)(iv), b748 defect (k): A STEP-ROWS COMMIT THROUGH THE TOOL CARRIES ITS ROWS AND WRITES NONE, SO THE STEP BANK IS CLEAN BEFORE THE PUSH'], 0, 0
    OC = old_cm()
    shas = [h for h in _git('log', '--format=%H', '--grep=the step row', '%s~40..%s' % (B747[1], B747[0])).split(NL) if h][::-1]
    # ### the subject's words open "the step row" (a component commit naming step rows in its body is not one: 0c118109, the first dry's catch)
    shas = [h for h in shas if _git('log', '-1', '--format=%s', h).startswith('b747 ') and _git('log', '-1', '--format=%s', h).split(': ', 1)[-1].startswith('the step row')]
    n += 1
    g += guard(L, 'rows', 'b747`s step-rows commits read (the control: the instances found, not none)', ' '.join(h[:8] for h in shas), len(shas) >= 3)
    for h in shas:
        names = [p for p in _git('show', '--name-only', '--format=', h).split(NL) if p]
        subj = _git('log', '-1', '--format=%s', h).strip()
        head = json.loads(show(h + '^', 'data/b747_steps.json') or '{}')
        mine = json.loads(show(h, 'data/b747_steps.json') or '{}')
        want = SJ.step_rows_words(SJ.step_rows_added(head, mine))
        words = subj.split(': ', 1)[1] if ': ' in subj else ''
        old_only = hasattr(OC, 'rows_only')
        n += 1
        g += case(L, 'rows', '%s "%s", staged %s' % (h[:8], subj[:70], ', '.join(names)),
                  'rows_only %s ; a row written after the commit (record_row always called), the step bank dirty before the push' % ('DEFINED' if old_only else 'UNDEFINED'),
                  'rows_only %s ; the words against the rows` composition %s' % (CM.rows_only('b747', names), 'EQUAL' if words == want else '### DIFFER %r' % want),
                  not old_only, CM.rows_only('b747', names) and words == want)
    for what, names, want in (('the pre-root commit af091b12`s set (the scores and the step bank) is not a step-rows commit', ['data/b747_scores.json', 'data/b747_steps.json'], False),
                              ('the scan bank alone is not a step-rows commit', ['data/b747_address_scan_postlock.txt'], False),
                              ('another act`s step bank is not this act`s', ['data/b746_steps.json'], False)):
        n += 1
        g += guard(L, 'rows', what, 'rows_only %s' % CM.rows_only('b747', names), CM.rows_only('b747', names) == want)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R358)(3)(iv): THE STANDING VERSION PRINTED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = show(BASE, 'tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.28.0', ver == 'v1.28.1')
    return L, g, n


CONTROLS = {'root': control_root, 'branch': control_branch, 'rows': control_rows, 'version': control_version}
ORDER = ('root', 'branch', 'rows', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.28.1, (R358)(3)(iv), b748 defect (k): THE ROOT BANKS COMMIT, THE PUSH BRANCH AND THE STEP-ROWS COMMIT '
           'THROUGH THE ONE-CALL TOOL (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.28.1: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1281.txt' % act), NL.join(out))
        print('written data/%s_standing_v1281.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
