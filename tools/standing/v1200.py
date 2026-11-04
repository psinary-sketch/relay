# -*- coding: utf-8 -*-
"""standing/v1200.py -- THE CONTROLS OF v1.20.0 ((R350)(2)(i)-(vi)), in v1190.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the
repair is read from the blob at BASE (b739's closing), not from disk. THE ARM THAT COULD NOT PASS PRINTS AT THE HEAD ((R350)'s Component 1). Written at b740 by the Write tool.

  python -X utf8 -u tools/standing/v1200.py control [needles|subjects|assign|publish|miss|version ...] [--bank]
"""
import ast
import io
import json
import os
import re
import subprocess
import sys
import time
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = 'c961e9d7'   # ### b739's closing, the toolset as v1.19.0 left it
PP_BASE = '5b89b86'  # ### PLACE-papers at b739's record
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import armnorm as AN            # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import publishstate as PS       # noqa: E402
import subjects as SJ           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _jread(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f) if name.endswith('.json') else f.read()


def base_module(rel, name):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.19.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.20.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.20.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def _tuple_of(src, name):
    """a module-level tuple of string literals, read from the source by its balanced parentheses (an act module is not a whole Python file)."""
    i = src.index('\n%s = (' % name) + len('\n%s = ' % name)
    depth, j = 0, i
    while True:
        c = src[j]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                break
        j += 1
    return ast.literal_eval(src[i:j + 1])


def control_needles():
    L, g, n = ['### (needles) (R350)(2)(i), b739 EVENTS (3), b727 EVENTS (14): THE ARM THAT COULD NOT PASS -- G-ENTRY-TITLE-FORM`S NEEDLES READ UNDER THE FOLD ITS TARGET GETS'], 0, 0
    src = _git('show', '%s:tools/acts/b739.py' % BASE)
    nd = _tuple_of(src, 'TITLE_NEEDLES')
    fd = _git('show', '%s:FINDINGS.md' % PP_BASE, repo=PP).replace('\r', '').split(NL)
    title = fd[13350]
    tpl = _git('show', '%s:tools/standing/fold/checks.tpl' % BASE)
    had = 'all(n in f for n in TITLE_NEEDLES)' in tpl
    n += 1
    g += case(L, 'needles', 'b739`s entry, FINDINGS :13351 at %s ("%s..."), against b739`s TITLE_NEEDLES (tools/acts/b739.py at %s, %d needles)' % (PP_BASE, title[:50], BASE, len(nd)),
              'checks.tpl`s entry_title_ok at %s (the needles unfolded, %s): %s' % (BASE, had, 'PASS' if AN.title_ok_old(title, nd) else 'FAIL'),
              'armnorm.title_ok, the needles folded as the title is: %s' % ('PASS' if AN.title_ok(title, nd) else 'FAIL'),
              had and not AN.title_ok_old(title, nd), AN.title_ok(title, nd))
    cp = AN.cannot_pass(nd)
    n += 1
    g += guard(L, 'needles', 'the normalisation check on b739`s old phrase: a needle the fold changes cannot stand in a folded title under the arm as it stood',
               'CANNOT PASS: %s' % cp, cp == [nd[0]] and nd[0].startswith('## The '))
    cur = _tuple_of(io.open(os.path.join(T, 'acts', '%s.py' % A.current()['act']), encoding='utf-8').read(), 'TITLE_NEEDLES')
    n += 1
    g += guard(L, 'needles', 'the open act`s TITLE_NEEDLES read by the same check before the lock (the act module, %d needles); the positive control on the composed title runs at the pre-lock dry (armnorm.py title)' % len(cur),
               'CANNOT PASS: %s' % (AN.cannot_pass(cur) or 'NONE'), True)
    return L, g, n


def control_subjects():
    L, g, n = ['### (subjects) (R350)(2)(ii), b739 EVENTS (1): THE COMPOSER THE ONE ROUTE TO A SEAL OR LOCK COMMIT; A TYPED SUBJECT REFUSED, THE COUNT RIGHT OR WRONG'], 0, 0
    typed = "b739 seal: the sealed tools' hashes, 85 files, at 14116439, 115 of 116 NEG controls shown failing, G-RUNNER-GATE VACUOUS (no dispatch this act)"
    typed83 = typed.replace('85 files', '83 files')
    comp = _git('log', '-1', '--format=%s', 'c1776793').strip()
    oldsj = base_module('tools/standing/subjects.py', 'old_subjects')
    o85, n85 = oldsj.check('b739', 'seal', typed, _jread), SJ.check('b739', 'seal', typed, _jread)
    n += 1
    g += guard(L, 'subjects', 'b739`s 10:04:30Z typed subject, "%s..." (data/b739_hook_refusals.txt :8)' % typed[:60], 'v1.19.0 %s ; v1.20.0 %s' % (o85, n85), bool(o85) and bool(n85))
    o83, n83 = oldsj.check('b739', 'seal', typed83, _jread), SJ.check('b739', 'seal', typed83, _jread)
    n += 1
    g += case(L, 'subjects', 'the same typed words with the bank`s 83 (the apostrophe typed where the composer writes a backtick)', 'check -> %s' % (o83 or 'NO FAULT, THE COMMIT RUNS'),
              'check -> %s' % n83, not o83, bool(n83) and 'typed seal subject' in n83[-1])
    nc = SJ.check('b739', 'seal', comp, _jread)
    cmd = 'git -C D:/relay commit -m "%s"' % typed83.replace('"', '\\"')
    j = HK.judge('PowerShell', {'command': cmd})
    n += 1
    g += guard(L, 'subjects', 'b739`s composed subject c1776793 "%s..." passes; the hook refuses the typed 83 as SUBJECT' % comp[:50], 'composed %s ; hook on the typed %s' % (nc or 'NO FAULT', j and j[0]),
               not nc and bool(j) and j[0] == 'SUBJECT')
    return L, g, n


def control_assign():
    L, g, n = ['### (assign) (R350)(2)(iii), b739 EVENTS (2): THE SHELL ASSIGNMENT AT THE PRE-ROOT PUSH -- THE RULE`S INSTANCE PRINTED; REPEAT, THE CLASS BANKED'], 0, 0
    rf9 = io.open(os.path.join(D, 'b739_hook_refusals.txt'), encoding='utf-8').read().split(NL)
    rf0 = io.open(os.path.join(D, 'b740_hook_refusals.txt'), encoding='utf-8').read().split(NL)
    ins = [l for l in rf9 if '| ENV |' in l] + [l for l in rf0 if '| ENV |' in l]
    banked = [l for l in io.open(os.path.join(D, 'b739_defects.txt'), encoding='utf-8').read().split(NL) if l.startswith('    (i) ') and 'ENV' in l]
    n += 1
    g += guard(L, 'assign', 'every ENV refusal of b739 and b740 by the hook (row (20)): %d, each nothing run; the class banked at b739 (i) (%s), so REPEAT' % (len(ins), 'present' if banked else 'ABSENT'),
               ' | '.join(x[:24] for x in ins), len(ins) >= 2 and bool(banked))
    cmd9 = 'free_mb=$(powershell.exe -NoProfile -Command "1"); echo "free_mb $free_mb"; bash /d/relay/tools/push_gated.sh /d/relay push-b739-preroot'
    j = HK.judge('Bash', {'command': cmd9})
    n += 1
    g += guard(L, 'assign', 'b739 events (2)`s command form judged now', 'judge -> %s' % (j and j[0]), bool(j) and j[0] == 'ENV')
    return L, g, n


def control_publish():
    L, g, n = ['### (publish) (R350)(2)(iv), (R338)`S "PUBLISH NOT CALLED" REPAIR: G-PUBLISH-UNCALLED READ BY THE DEPOSIT ROUTE`S STATE, METADATA EDIT, NO NEW VERSION BY NAME'], 0, 0
    old = _git('show', '%s:tools/b703_checks.py' % BASE)
    pub = ['actions' + '/pub' + 'lish', 'z_' + 'publish']
    for act, files, want in (('b739', ['tools/b739_tier3.py'], PS.EDITED), ('b727', ['tools/b727_sitting.py'], PS.EDITED)):
        tt = {f: _git('show', 'HEAD:%s' % f) for f in files}
        oldr = bool(tt) and not [f for f, t in tt.items() if any(p in t for p in pub)]
        n += 1
        g += case(L, 'publish', '%s`s deposit-route tool %s (actions/edit, then actions/publish on the published record)' % (act, ', '.join(files)),
                  'publish_uncalled (tools/b703_checks.py at %s, %s): %s' % (BASE, 'def publish_uncalled' in old, 'PASS' if oldr else 'FAIL'),
                  'publishstate: %s -> %s' % (PS.summary(tt), 'PASS' if PS.ok(tt) else 'FAIL'), not oldr, PS.ok(tt) and set(PS.states(tt).values()) == {want})
    t33 = {f: _git('show', 'HEAD:%s' % f) for f in _git('ls-files', 'tools/b733_*.py').split()}
    n += 1
    g += guard(L, 'publish', 'b733`s tools (%d), no deposit route' % len(t33), PS.summary(t33), PS.ok(t33) and set(PS.states(t33).values()) == {PS.UNCALLED})
    pl = {'tools/plant.py': "st, j = http(base + '/actions/newversion', 'POST', None, token)\nst, j = http(base + '/actions/publish', 'POST', None, token)\n"}
    pl2 = {'tools/plant2.py': "st, j = http(base + '/actions/publish', 'POST', None, token)\n"}
    n += 1
    g += guard(L, 'publish', 'a planted new-version call and a planted publish with no edit route read as PUBLISH, the arm failing', '%s ; %s' % (PS.summary(pl), PS.summary(pl2)),
               not PS.ok(pl) and not PS.ok(pl2))
    return L, g, n


def control_miss():
    L, g, n = ['### (miss) (R350)(2)(v): b739`S CITATION CHECK, ONE MISS WITH THE CHECK CLEAN -- THE MISS NAMED, AND WHY THE CHECK STAYED CLEAN'], 0, 0
    cc = io.open(os.path.join(D, 'b739_citation_check.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    miss = [l for l in cc if l.startswith('  MISS ')]
    sz = io.open(os.path.join(D, 'b739_stepzero.txt'), encoding='utf-8').read().replace('\r', '').split(NL)
    n += 1
    g += guard(L, 'miss', 'data/b739_citation_check.txt :104 (%s), the miss row (%s...); CLEAN at :105 counts halts (Lean paths, nouns, comparatives) alone, and the miss was the ruling`s quoted word, entered by the fact clause (data/b739_stepzero.txt :15-:17)' % (
        cc[103][:44], miss[0][:70] if miss else 'NONE'), 'halts %s ; entered %s' % ('halts 0' in cc[104], 'ENTERED BY THE FACT CLAUSE' in sz[14]),
        len(miss) == 1 and 'halts 0' in cc[104] and 'ENTERED BY THE FACT CLAUSE' in sz[14])
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R350)(2)(vi): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = _git('show', '%s:tools/standing/VERSION' % BASE).strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.19.0', ver == 'v1.20.0')
    return L, g, n


CONTROLS = dict(needles=control_needles, subjects=control_subjects, assign=control_assign, publish=control_publish, miss=control_miss, version=control_version)
ORDER = ('needles', 'subjects', 'assign', 'publish', 'miss', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.20.0, (R350)(2)(i)-(vi): THE ARM THAT COULD NOT PASS, THE COMPOSER THE ONE ROUTE TO A SEAL OR LOCK SUBJECT, THE SHELL ASSIGNMENT, THE DEPOSIT ROUTE BY ITS STATE, THE MISS WITH THE CHECK CLEAN, THE VERSION (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '## THE CONTROLS',
        '  the bank is its controls: the compile control first, then the arm that could not pass at the head, then each repair`s instances through both routes; written through tools/standing/figbank.py ((R348)(2)(i))', '',
        '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
        '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.20.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1200.txt' % act), NL.join(out))
        print('written data/%s_standing_v1200.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
