# -*- coding: utf-8 -*-
"""standing/v1230.py -- THE CONTROLS OF v1.23.0 ((R353)(3)(i)-(vii) and b743 step-zero defect (f)), in v1220.py's form: each instance read through the route as
it stood before the repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing
side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b742's closing),
not from disk. The free memory is read and printed before each control. Written at b743 by the Write tool.

  python -X utf8 -u tools/standing/v1230.py control [cites|remote|subjects|push|dispatch|repeat|origin|version ...] [--bank]
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = '16a36428'   # ### b742's closing, the toolset as v1.22.0 left it
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
BASH = 'C:/Program Files/Git/bin/bash.exe'
HOLD = 2560
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import cites as CI              # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import dispatchrows as DR       # noqa: E402
import figbank as FB            # noqa: E402
import pushcheck as PC          # noqa: E402
import rootprompt as RP         # noqa: E402
import subjects as SJ           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base_module(rel, name, **deps):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk; `deps` replace the modules it imported by name
    (an old commit.py is given the old subjects.py, not the one already loaded)."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    m.__dict__.update(deps)
    return m


def _read(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with io.open(p, encoding='utf-8') as f:
        return json.load(f) if name.endswith('.json') else f.read()


def _lines(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace('\r', '').split(NL)


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.22.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.23.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.23.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def control_cites():
    L, g, n = ['### (cites) b743 STEP-ZERO DEFECT (f): THE CITATION CHECK`S LEAN-PATH READER READ THE LABEL S4` AS NO NAME AND CITED zqFn TO Carrier.lean'], 0, 0
    old = base_module('tools/standing/cites.py', 'old_cites')
    t743 = io.open(os.path.join(D, 'b743_ferry.txt'), encoding='utf-8').read()
    tr743 = ((EF, '14ca5725'), (EF + '/.lake/packages/mathlib', 'de5ce8a9'))
    o = [r for r in old.lean_rows(t743, tr743) if 'beside Carrier.lean' in r[1]]
    nw = [r for r in CI.lean_rows(t743, tr743) if 'beside Carrier.lean' in r[1]]
    n += 1
    g += case(L, 'cites', 'data/b743_ferry.txt :11, (R353)(2)`s "... the zeros of zqFn there (S4`, Carrier.lean :21)", against zq-b730 at 14ca5725',
              'rows beside Carrier.lean: %s' % (o or 'none'), 'rows beside Carrier.lean: %s' % (nw or 'none'),
              any(not r[3] and r[1].startswith('zqFn') for r in o), not nw)
    t742 = io.open(os.path.join(D, 'b742_ferry.txt'), encoding='utf-8').read()
    tr742 = ((EF, '3329eaa1'), (EF + '/.lake/packages/mathlib', 'de5ce8a9'))
    o2, n2 = old.lean_rows(t742, tr742), CI.lean_rows(t742, tr742)
    n += 1
    g += guard(L, 'cites', 'data/b742_ferry.txt`s Lean rows against zq-b730 at 3329eaa1, the reader before and after',
               'v1.22.0 %d rows (%d ok) ; v1.23.0 %d rows (%d ok) ; equal %s' % (len(o2), sum(1 for r in o2 if r[3]), len(n2), sum(1 for r in n2 if r[3]), o2 == n2), o2 == n2)
    return L, g, n


REMOTES742 = {'relay': '13498fd2d2eb9269a0c0190199b3dd457a8937c5', 'pp': 'efce669fd1c86507a9a4127c8b2626a6032dacb4'}
LOCAL742 = {'relay': '86f033a3e8d4665cc4e75438978a5d35dac29b46', 'pp': '6e86bd1ede908508035458583aef26c76b854915'}


def control_remote():
    L, g, n = ['### (remote) (R353)(3)(i), b742 EVENTS (3): THE ROOT PROMPT`S REMOTE FIGURES READ FROM THE REMOTE BY THE COMPOSER, "remote at <sha>; local <n> commits past it"'], 0, 0
    line = _lines('b742_author_answers.txt')[12]
    prompt = line.split('answered: "', 1)[1] if 'answered: "' in line else ''
    old = base_module('tools/standing/rootprompt.py', 'old_rootprompt')
    o_has = 'remote_unbacked' in old.__dict__
    bad = RP.remote_unbacked(prompt, REMOTES742)
    n += 1
    g += case(L, 'remote', 'b742`s root prompt (data/b742_author_answers.txt :13) against the remotes as they stood at prompt time (relay 13498fd2, PLACE-papers efce669)',
              'rootprompt.py at %s: no remote read, no clause checked (remote_unbacked defined: %s); the prompt put' % (BASE, o_has),
              'the clauses refused: %s' % bad, not o_has, bool(bad) and all('bce5605d' in c for c in bad))
    cnt = {k: int(_git('rev-list', '--count', '%s..%s' % (REMOTES742[k], LOCAL742[k]), repo=RELAY if k == 'relay' else PP).strip()) for k in REMOTES742}
    regen = [RP.remote_clause('relay', REMOTES742['relay'], LOCAL742['relay'], cnt['relay']),
             RP.remote_clause('PLACE-papers', REMOTES742['pp'], LOCAL742['pp'], cnt['pp'])]
    text = '; '.join(regen)
    n += 1
    g += guard(L, 'remote', 'b742`s prompt regenerated: the remote figures composed from the remote heads and the local count (git rev-list --count), refused nothing',
               '"%s" ; refused %s' % (text, RP.remote_unbacked(text, REMOTES742) or 'none'),
               regen[0] == 'relay remote at 13498fd2; local 25 commits past it' and not RP.remote_unbacked(text, REMOTES742))
    return L, g, n


SEAL96 = 'b742 seal: the sealed tools` hashes, 96 files, '


def _staged_repo():
    d = tempfile.mkdtemp(prefix='v1230_')
    subprocess.run(['git', 'init', '-q', d], capture_output=True)
    io.open(os.path.join(d, 'f.txt'), 'w', encoding='utf-8').write('x\n')
    subprocess.run(['git', '-C', d, 'add', 'f.txt'], capture_output=True)
    return d


def _pf(mod, act, phase, words, repo, read):
    try:
        return 'ACCEPTED: %r' % mod.preflight(act, phase, words, repo, [], read)[:110]
    except mod.Refused as e:
        return 'REFUSED: %s' % str(e)[:150]


def control_subjects():
    L, g, n = ['### (subjects) (R353)(3)(ii), b742 EVENTS (1)-(2): THE COMMIT TOOL TAKES NO SUBJECT TEXT FOR LOCK, GATE AND SEAL'], 0, 0
    oldsj = base_module('tools/standing/subjects.py', 'old_subjects')
    oldcm = base_module('tools/standing/commit.py', 'old_commit', SJ=oldsj)
    read = CM.reader(D)
    repo = _staged_repo()
    try:
        subj = _git('log', '-1', '--format=%s', '86f033a3').strip()
        words2 = subj[len(SEAL96):]                         # ### the words the seat passed at 21:46:24Z: the subject less the composer's head, opening with the same head again
        words1 = words2.replace('96 files', '97 files').replace('96 tools', '97 tools')   # ### event (1): the same words with the seat's 97
        o1, o1b, n1 = _pf(oldcm, 'b742', 'seal', words1, repo, read), _pf(oldcm, 'b742', 'seal', words2, repo, read), _pf(CM, 'b742', 'seal', words1, repo, read)
        n += 1
        g += case(L, 'subjects', 'b742`s event (1), the seal words sent with "97 files" and "97 tools hashed" (the 96 words with the seat`s 97 where its count stood)',
                  '97: %s ; the same words with 96: %s' % (o1, o1b), n1, o1b.startswith('ACCEPTED'), n1.startswith('REFUSED') and 'SUBJECT TEXT GIVEN' in n1)
        n2 = _pf(CM, 'b742', 'seal', words2, repo, read)
        chk = SJ.check('b742', 'seal', subj, read)
        n += 1
        g += case(L, 'subjects', 'b742`s event (2), the seal commit 86f033a3`s subject, its head twice ("%s...")' % subj[:90],
                  'preflight composes 86f033a3`s subject from the words passed: %s ; check %s' % (oldcm.preflight('b742', 'seal', words2, repo, [], read) == subj, oldsj.check('b742', 'seal', subj, read) or 'NO FAULT'),
                  'preflight %s ; check %s' % (n2[:70], chk), oldcm.preflight('b742', 'seal', words2, repo, [], read) == subj and not oldsj.check('b742', 'seal', subj, read),
                  n2.startswith('REFUSED') and any('words after' in c for c in chk))
        comp = _pf(CM, 'b742', 'seal', '', repo, read)
        n += 1
        g += guard(L, 'subjects', 'the seal subject with no words, the composer`s whole, passes; check of it', '%s ; check %s' % (comp, SJ.check('b742', 'seal', SEAL96.rstrip(', '), read) or 'NO FAULT'),
                   comp == "ACCEPTED: 'b742 seal: the sealed tools` hashes, 96 files'" and not SJ.check('b742', 'seal', SEAL96.rstrip(', '), read))
        gate = _pf(CM, 'b742', 'gate', '', repo, read)
        gw = _pf(CM, 'b742', 'gate', 'step row 13 for 0fa5a670', repo, read)
        n += 1
        g += guard(L, 'subjects', 'the gate subject composed by the tool from the index and b742`s banks; the gate words of a706f62a refused',
                   'composed %s ; with words %s' % (gate, gw[:80]), gate.startswith("ACCEPTED: 'b742 gate: 1 file staged (f.txt)") and gw.startswith('REFUSED'))
        L.append('      NOTE: the subjects with words after the composer`s whole that earlier controls passed (v1.19.0`s b738 lock b1c498e7, v1.20.0`s c1776793) are refused '
                 'from v1.23.0 by (R353)(3)(ii); those banks stand as written at their acts')
    finally:
        shutil.rmtree(repo, ignore_errors=True)
    return L, g, n


def _run_push(script, branch):
    log = tempfile.mktemp(prefix='v1230_push_', suffix='.txt')
    env = dict(os.environ, PUSH_GATED_LOG=log)
    r = subprocess.run([BASH, script, 'D:/relay', branch], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    if os.path.exists(log):
        os.remove(log)
    return r.returncode, ((r.stderr or '') + (r.stdout or '')).strip().replace('\n', ' | ')[-220:]


def control_push():
    L, g, n = ['### (push) (R353)(3)(iii), b742 EVENTS (4): THE PUSH TOOL REFUSES AT ITSELF WHEN ITS BRANCH OR ITS STEP ROW IS ABSENT'], 0, 0
    if _git('rev-parse', '-q', '--verify', 'refs/heads/push-b742-preroot').strip():
        L.append('  (push) push-b742-preroot STANDS in the relay: the replay needs it absent (run after the deletes) -- NOT AS WANTED')
        return L, 0, 1
    tmp = tempfile.mkdtemp(prefix='v1230_sh_')
    try:
        old = os.path.join(tmp, 'push_gated_old.sh')
        io.open(old, 'w', encoding='utf-8', newline='\n').write(_git('show', '%s:tools/push_gated.sh' % BASE))
        orc, oout = _run_push(old, 'push-b742-preroot')
        nrc, nout = _run_push(os.path.join(T, 'push_gated.sh'), 'push-b742-preroot')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n += 1
    g += case(L, 'push', 'b742`s 22:01:12Z send replayed, `push_gated.sh D:/relay push-b742-preroot` with the branch absent (deleted at b743 after its merge)',
              'exit %d: %s' % (orc, oout), 'exit %d: %s' % (nrc, nout), orc == 128 and 'ambiguous argument' in oout, nrc == 13 and 'REFUSED AT THE TOOL' in nout)
    fx = _staged_repo()
    try:
        subprocess.run(['git', '-C', fx, '-c', 'user.email=x@example.invalid', '-c', 'user.name=x', 'commit', '-q', '-m', 'f'], capture_output=True)
        subprocess.run(['git', '-C', fx, 'branch', 'push-fixture'], capture_output=True)
        ok, absent = PC.faults(fx, 'push-fixture', 'b743'), PC.faults(fx, 'push-absent', 'b743')
    finally:
        shutil.rmtree(fx, ignore_errors=True)
    n += 1
    g += guard(L, 'push', 'a fixture repository (tools/test_push_gated.sh`s kind): the branch standing reads CLEAR, the branch absent refused, no act`s step bank asked',
               'standing %s ; absent %s' % (ok or 'CLEAR', absent), not ok and len(absent) == 1 and 'IS NOT IN' in absent[0])
    return L, g, n


def control_dispatch():
    L, g, n = ['### (dispatch) (R353)(3)(v), b742 DEFECTS (k), (l): TARGETS FROM THE PLAN`S MODULE LIST, A NAME NOT IN THE TREE REFUSED; ROW LABELS FROM THE DISPATCH COUNT'], 0, 0
    rows = json.load(io.open(os.path.join(D, 'b742_dispatch_rows.json'), encoding='utf-8'))
    old = base_module('tools/standing/dispatchrows.py', 'old_dispatchrows')
    d4 = [r for r in rows if r.get('kind') == 'dispatch' and r.get('n') == 4][0]
    d5 = [r for r in rows if r.get('kind') == 'dispatch' and r.get('n') == 5][0]
    files = DR.tree_files(EF, d4['sha'])
    mods = d5['target'].split()
    o4 = 'targets_refused' in old.__dict__
    r4, r5 = DR.targets_refused(d4['target'], files, mods), DR.targets_refused(d5['target'], files, mods)
    n += 1
    g += case(L, 'dispatch', 'b742`s dispatch 4 (run %s) at %s, targets "%s"' % (d4['run'], d4['sha'][:8], d4['target'][:60]),
              'dispatchrows.py at %s: no target read (targets_refused defined: %s); the row written' % (BASE, o4),
              'refused %d of %d: %s' % (len(r4), len(d4['target'].split()), r4[:2]), not o4, len(r4) == len(d4['target'].split()))
    n += 1
    g += guard(L, 'dispatch', 'b742`s dispatch 5 (run %s), the same commit, the full module names' % d5['run'], 'refused %s' % (r5 or 'none'), not r5)
    o_series = 'series' in old.__dict__
    s = DR.series(rows, repo=EF, since='')
    dup = [x for x in s if x[1] == 'commit']
    n += 1
    g += case(L, 'dispatch', 'b742`s commit rows: 4c04916c rowed G4-G6 (index %d) and again R5 (index %d), beside the true R5 c2d4f29c' % (
                  rows.index([r for r in rows if r.get('sha', '').startswith('4c04916c') and r.get('kind') == 'commit'][0]),
                  rows.index([r for r in rows if r.get('item') == 'R5' and r.get('kind') == 'commit'][0])),
              'no series read (series defined: %s); both rows written' % o_series, 'refused %s' % s,
              not o_series, len(dup) == 1 and 'already rowed' in dup[0][2] and rows[dup[0][0]]['item'] == 'R5' and rows[dup[0][0]]['sha'].startswith('4c04916c')
              and [x[0] for x in s if x[1] == 'dispatch'] == [rows.index(d4)])
    n += 1
    g += guard(L, 'dispatch', 'the label composed from the dispatch count: after five dispatches R5 (c2d4f29c`s row); b742`s bank read at the landing date refuses nothing',
               'label %s ; series at LANDING %s' % (DR.label(rows[:rows.index([r for r in rows if r.get('sha', '').startswith('c2d4f29c') and r.get('kind') == 'commit'][0])]), DR.series(rows) or 'none'),
               DR.label(rows[:rows.index([r for r in rows if r.get('sha', '').startswith('c2d4f29c') and r.get('kind') == 'commit'][0])]) == 'R5' and not DR.series(rows))
    return L, g, n


def control_repeat():
    L, g, n = ['### (repeat) (R353)(3)(iv), b742 EVENTS (5)-(6): THE HOLD AND THE HOOK HELD; THE INSTANCES PRINTED AS REPEAT'], 0, 0
    ev = _lines('b742_events.txt')
    for k, idx, head in (('the hold', 11, 'THE HOST`S FREE MEMORY'), ('the pipe', 14, 'a PowerShell read of the untracked zero-name file')):
        cls = CM.repeat_of(head + ':', 'b743')
        n += 1
        g += guard(L, 'repeat', '%s, data/b742_events.txt :%d' % (k, idx + 1), '"%s..." ; class %s' % (ev[idx].strip()[:110], cls), head in ev[idx] and cls.startswith('REPEAT of b742 event'))
    return L, g, n


DEFECT_D = 'the bound`s dominant term, VACUOUS where B >= |m|, and the margin`s sign'


def control_origin():
    L, g, n = ['### (origin) (R353)(3)(vi): THE "=" FILE`S ORIGIN, READ FROM THE LOG AND REPRODUCED'], 0, 0
    st = os.stat(os.path.join(RELAY, '='))
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(st.st_mtime))
    b511 = _lines('b511_defects.txt')
    e = [l for l in b511 if 'DOUBLE-QUOTED SHELL STRING' in l]
    n += 1
    g += guard(L, 'origin', 'the relay`s "=" (size %d, last written %s) and b511`s defect (e) (data/b511_defects.txt), the act committed at fc9f9e9d 18:21:02Z' % (st.st_size, at),
               '"%s..."' % (e[0].strip()[:150] if e else 'NONE'), st.st_size == 0 and at.startswith('2026-09-24T18:18') and bool(e))
    tmp = tempfile.mkdtemp(prefix='v1230_eq_')
    try:
        subprocess.run([BASH, '-c', 'x="%s"; true' % DEFECT_D], cwd=tmp, capture_output=True)
        made = sorted(os.listdir(tmp))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n += 1
    g += guard(L, 'origin', 'reproduced in an empty directory: b511 defect (d)`s words in a double-quoted shell string, its backtick span carrying ">="', 'files made %s' % made, made == ['='])
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R353)(3)(vii): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = _git('show', '%s:tools/standing/VERSION' % BASE).strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.22.0', ver == 'v1.23.0')
    return L, g, n


CONTROLS = dict(cites=control_cites, remote=control_remote, subjects=control_subjects, push=control_push, dispatch=control_dispatch, repeat=control_repeat,
                origin=control_origin, version=control_version)
ORDER = ('cites', 'remote', 'subjects', 'push', 'dispatch', 'repeat', 'origin', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.23.0, (R353)(3)(i)-(vii) AND STEP-ZERO DEFECT (f): THE CITATION READER`S LABEL, THE ROOT PROMPT`S REMOTE FIGURES, '
           'NO SEAT WORDS IN LOCK, GATE AND SEAL SUBJECTS, THE PUSH TOOL`S PRE-CHECK, THE DISPATCH TARGETS AND LABELS, THE HOLD AND THE HOOK AS REPEAT, THE "=" ORIGIN, '
           'THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.23.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1230.txt' % act), NL.join(out))
        print('written data/%s_standing_v1230.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
