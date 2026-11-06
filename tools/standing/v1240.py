# -*- coding: utf-8 -*-
"""standing/v1240.py -- THE CONTROLS OF v1.24.0 ((R354)(2)(i)-(xi)), in v1230.py's form: each instance of b743 read through the route as it stood
before the repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with
no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the
blob at BASE (b743's closing), not from disk. The free memory is read and printed before each control. Each class may be run alone, one per call,
in the foreground; `--bank` writes the whole set, every class run in the one call. Written at b744 by the Write tool.

  python -X utf8 -u tools/standing/v1240.py control [prevdry|prevdry-ok|tags|repair|hook|rewrite|branches|order|repeat|version ...] [--bank]
"""
import copy
import io
import json
import os
import subprocess
import sys
import time
import types

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
BASE = 'b41fa006'   # ### b743's closing, the toolset as v1.23.1 left it
LOCK = 'fc32ebd6'   # ### b743's lock commit: tools/acts/b743.py as the lock took it
REPAIR = 'bd968013'  # ### b743's repair commit, the head "b743 repair:"
HOLD = 2560
EF = 'SIDE-explicit-formula'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import facebranches as FBR      # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import prelock as PL            # noqa: E402
import prevdry as PD            # noqa: E402
import pushcheck as PC          # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base_src(rel):
    return _git('show', '%s:%s' % (BASE, rel))


def base_module(rel, name, **deps):
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(base_src(rel), name, 'exec'), m.__dict__)
    m.__dict__.update(deps)
    return m


def _jl(name):
    with io.open(os.path.join(D, name), encoding='utf-8') as f:
        return json.load(f)


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.23.1): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.24.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.24.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def control_prevdry():
    L, g, n = ['### (prevdry) (R354)(2)(i), b743 events (3), (7): THE PRE-LOCK DRY RUNS PREV MODE; b743`S MODULE AT ITS LOCK (%s) UNDER THE DRY' % LOCK], 0, 0
    lock_text = _git('show', '%s:tools/acts/b743.py' % LOCK)
    rep = _git('show', '%s:tools/acts/b743.py' % REPAIR).split(NL)
    mid = lock_text.split(NL)
    mid[560] = rep[560]   # ### the first edit alone (events (4), 14:02:44Z): :561 repaired, :575 as the lock took it
    mid_text = NL.join(mid)
    old_gate = base_src('tools/standing/prelock.py')
    for part, text, ln, needle, which in (('act', lock_text, 561, "jl('b743_kernel_bases.json').get(k_)", 'at the lock (%s)' % LOCK),
                                          ('standing-a1', mid_text, 575, 'first_item=_ct(PP, K.SITTING_PP[0]),', 'with :561 repaired alone (the first lift`s edit)')):
        r = PD.exercise('b743', part, text)
        n += 1
        g += case(L, 'prevdry', 'part %s, tools/acts/b743.py %s (blob %s), replayed as %s: the stop at b743`s :%d' % (part, which, (r.get('blob') or '')[:8], r.get('replayed_as'), ln),
                  'the lock gate read no prev-mode run (prelock.py at %s names prevdry: %s); the stop surfaced after the lock' % (BASE, 'prevdry' in old_gate),
                  'the dry run before the lock: %s%s (%s s)' % ('SOURCES OK' if r['ok'] else 'FAILS', '' if r['ok'] else ', %s, at %s' % ((r.get('err') or '')[:70], (r.get('at') or '')[:90]), r.get('secs')),
                  'prevdry' not in old_gate, not r['ok'] and needle in (r.get('at') or ''))
    return L, g, n


def control_prevdry_ok():
    L, g, n = ['### (prevdry-ok) (R354)(2)(i): THE REPAIRED MODULE (%s) UNDER THE SAME DRY, THE SAME PARTS' % REPAIR], 0, 0
    text = _git('show', '%s:tools/acts/b743.py' % REPAIR)
    for part in ('act', 'standing-a1'):
        r = PD.exercise('b743', part, text)
        n += 1
        g += guard(L, 'prevdry-ok', 'part %s, tools/acts/b743.py at %s (blob %s)' % (part, REPAIR, (r.get('blob') or '')[:8]),
                   '%s (%s s)%s' % ('SOURCES OK' if r['ok'] else 'FAILS', r.get('secs'), '' if r['ok'] else ': %s at %s' % (r.get('err'), r.get('at'))), r['ok'])
    return L, g, n


def control_tags():
    L, g, n = ['### (tags) (R354)(2)(iv), b743 events (15): THE CLOSING`S TAG REQUIREMENT READ AT THE PRE-LOCK DRY'], 0, 0
    e96 = _git('show', '96d8e736:data/b743_events.txt')
    e7f = _git('show', '7f41b079:data/b743_events.txt')
    df = _git('show', '7f41b079:data/b743_defects.txt')
    ok96, l96 = PL.tags('b743', e96, df)
    ok7f, l7f = PL.tags('b743', e7f, df)
    n += 1
    g += case(L, 'tags', 'data/b743_events.txt at 96d8e736 (the record`s form), read before the lock',
              'prelock.py at %s reads no tags (names counter: %s); the closing refused after the record push' % (BASE, 'counter' in base_src('tools/standing/prelock.py')),
              l96.strip(), 'counter' not in base_src('tools/standing/prelock.py'), not ok96)
    n += 1
    g += guard(L, 'tags', 'data/b743_events.txt at 7f41b079 (the tagged form)', l7f.strip(), ok7f)
    return L, g, n


def _b743_rows_before_seal():
    rows = _jl('b743_steps.json').get('rows') or []
    i = next((k for k, r in enumerate(rows) if r.get('phase') == 'seal'), len(rows))
    return rows[:i]


def control_repair():
    L, g, n = ['### (repair) (R354)(2)(ii), b743 events (8)-(9): THE REPAIR PHASE; b743`S COMMIT %s REPLAYED UNDER IT' % REPAIR], 0, 0
    rows = _b743_rows_before_seal()
    ev = _git('show', '96d8e736:data/b743_events.txt')
    import re
    diff = _git('diff', '-U0', REPAIR + '~1', REPAIR)
    names = [x for x in _git('diff', '--name-only', REPAIR + '~1', REPAIR).split(NL) if x]
    old_lines = [int(m.group(1)) for m in re.finditer(r'^@@ -(\d+)(?:,\d+)? ', diff, re.M)]
    words = _git('log', '-1', '--format=%s', REPAIR).split(':', 1)[1].strip()
    oldcm = base_module('tools/standing/commit.py', 'old_commit')
    n += 1
    try:
        subj, conds = CM.repair_check('b743', words, rows, ev, CM.settings_sha(), names, old_lines)
        new, ok = '%s ; %s' % (subj[:60], ' '.join(c.strip()[:50] for c in conds)), subj.startswith('b743 repair:')
    except CM.Refused as e:
        new, ok = 'REFUSED: %s' % e, False
    g += case(L, 'repair', '%s: files %s, the HEAD-side lines %s, the rows before the seal %d (a lock row among them %s)' % (REPAIR, names, old_lines, len(rows), any(r.get('phase') == 'lock' for r in rows)),
              'commit.py at %s: the phases %s, no route between the lock and the seal (b743 events (8)); the seat`s shell commit refused, the head chosen by the author' % (BASE, oldcm.PHASES),
              new, 'repair' not in oldcm.PHASES, ok)
    stripped = NL.join(l for l in ev.split(NL) if 'THE LIFT' not in l)
    n += 1
    try:
        CM.repair_check('b743', words, rows, stripped, CM.settings_sha(), names, old_lines)
        r2 = 'ACCEPTED'
    except CM.Refused as e:
        r2 = 'REFUSED: %s' % str(e)[:140]
    g += guard(L, 'repair', 'the same commit with no lift banked (the events` LIFT rows taken out)', r2, r2.startswith('REFUSED'))
    n += 1
    try:
        CM.repair_check('b743', words, rows, ev, CM.settings_sha(), names, old_lines + [600])
        r3 = 'ACCEPTED'
    except CM.Refused as e:
        r3 = 'REFUSED: %s' % str(e)[:140]
    g += guard(L, 'repair', 'the same commit with a line the events do not name (:600) in its diff', r3, r3.startswith('REFUSED'))
    return L, g, n


def control_hook():
    L, g, n = ['### (hook) (R354)(2)(iii), b743 events (4): THE HOOK`S SCOPE, BANKS AND FACES; THE ACT MODULE`S EDIT ALLOWED AND REFUTED'], 0, 0
    oldhk = base_module('tools/standing/hook.py', 'old_hook')
    mod = os.path.join(RELAY, 'tools', 'acts', 'b743.py')
    o, w = oldhk.locked_bank(mod, RELAY, act='b743'), HK.locked_bank(mod, RELAY, act='b743')
    for at in ('08:25:22Z', '08:33:45Z'):
        n += 1
        g += case(L, 'hook', 'the Edit of tools/acts/b743.py at %s, after the lock (events (4))' % at, 'locked_bank %s: REFUSED (LOCKED)' % o, 'locked_bank %s: allowed' % w, o is True, w is False)
    bank = os.path.join(D, 'b743_sitting.txt')
    n += 1
    g += guard(L, 'hook', 'a bank written before the lock, data/b743_sitting.txt, still refused after it', 'locked_bank %s' % HK.locked_bank(bank, RELAY, act='b743'), HK.locked_bank(bank, RELAY, act='b743') is True)
    sc = _jl('b743_scores_close.json').get('N4') or ['?', '']
    n += 1
    g += guard(L, 'hook', 'N4 scored on the act module`s post-lock edit (data/b743_scores_close.json)', '%s: %s' % (sc[0], ' '.join(str(x) for x in sc[1:])[:120]), sc[0] == 'REFUTED')
    return L, g, n


def control_rewrite():
    L, g, n = ['### (rewrite) (R354)(2)(iv), b743 events (15): A PUSHED BANK IS NOT REWRITTEN; b743`S THREE PUSHES REPLAYED'], 0, 0
    oldpc = base_src('tools/standing/pushcheck.py')
    got = PC.rewritten(RELAY, 'b743', 'eca0f83c', BASE)
    n += 1
    g += case(L, 'rewrite', 'the closing push, the remote at eca0f83c (the record), push-b743-closing at %s' % BASE,
              'pushcheck.py at %s reads no pushed bank (names rewritten: %s); the events bank rewritten after its push went out' % (BASE, 'def rewritten' in oldpc),
              'refused: %s' % (got or 'NONE'), 'def rewritten' not in oldpc, got == ['data/b743_events.txt'])
    for base, head, what in (('16a36428', '3c306e67', 'the pre-root push'), ('3c306e67', 'eca0f83c', 'the record push')):
        r = PC.rewritten(RELAY, 'b743', base, head)
        n += 1
        g += guard(L, 'rewrite', '%s, %s..%s: banks appended or new, none rewritten' % (what, base, head), 'refused %s' % (r or 'NONE'), r == [])
    a, b = _git('show', '96d8e736:data/b743_events.txt'), _git('show', '7f41b079:data/b743_events.txt')
    n += 1
    g += guard(L, 'rewrite', 'b743`s two forms read as distinct banks, the record`s at 96d8e736 standing', 'equal %s ; the record`s a prefix of the closing`s %s' % (a == b, b.startswith(a)), a != b and not b.startswith(a))
    return L, g, n


def _kern_case(extra, listed_rows):
    face = _jl('b743_kernels_face.json').get('kernels') or {}
    now = copy.deepcopy(face)
    now[EF] = [now[EF][0], now[EF][1], sorted(now[EF][2] + extra)] + list(now[EF][3:])
    S_ = dict(kern_face=face, kern_now=now, kerns_read=sorted(face))
    import b703_checks as C3
    return C3.kernels_untouched(S_), C3.kernels_untouched(dict(S_, kern_now=FBR.strip(now, listed_rows)))


def control_branches():
    L, g, n = ['### (branches) (R354)(2)(v), b743 events (11): THE FACE`S BRANCH LIST; push-b743-sitting REPLAYED AS LISTED'], 0, 0
    rows = [dict(kernel=EF, branch='push-b743-sitting', sha='8fbab45d', at='2026-11-06T17:06:00Z')]
    o, w = _kern_case(['push-b743-sitting'], rows)
    oldtpl = _git('show', '%s:tools/standing/fold/checks.tpl' % BASE)
    n += 1
    g += case(L, 'branches', 'data/b743_kernels_face.json against the kernels with push-b743-sitting on %s (the branch deleted at b744`s step zero; replayed)' % EF,
              'G-KERNELS-UNTOUCHED %s (the template reads no list: %s)' % ('PASSES' if o else 'FAILS', 'facebranches' not in oldtpl), 'the branch listed by its tool: %s' % ('PASSES' if w else 'FAILS'),
              not o and 'facebranches' not in oldtpl, w)
    o2, w2 = _kern_case(['push-b743-other'], rows)
    n += 1
    g += guard(L, 'branches', 'a branch the list does not name (push-b743-other) still fails the arm', 'listed %s -> %s' % ([r['branch'] for r in rows], 'PASSES' if w2 else 'FAILS'), not w2)
    o3, w3 = _kern_case([], [])
    n += 1
    g += guard(L, 'branches', 'the face read with no branch made and no list: the arm as before', 'before %s ; after %s' % (o3, w3), o3 and w3)
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'branches', 'the suite`s arm reads the list (fold/checks.tpl) and the hook leaves the list writable after the lock', 'tpl %s ; exempt %s' % (
        'FBR.listed(ACTN)' in tpl, 'data/b744_face_branches.json' in HK.lock_exempt('b744')), 'FBR.listed(ACTN)' in tpl and 'data/b744_face_branches.json' in HK.lock_exempt('b744'))
    return L, g, n


def control_order():
    L, g, n = ['### (order) (R354)(2)(vi), b743 events (10): THE KERNEL PUSH ORDERED BEFORE THE ROOT; b743`S SEQUENCE REPLAYED'], 0, 0
    rows = [dict(kernel=EF, branch='push-b743-sitting', sha='8fbab45d', at='2026-11-06T17:06:00Z')]
    old = _git('ls-tree', '--name-only', BASE, '--', 'tools/standing/facebranches.py').strip()
    need, Lo = FBR.order(rows, EF, '8fbab45d8a96', 'badacccb867e')
    n += 1
    g += case(L, 'order', '%s main 8fbab45d, the remote badacccb, at b743`s `record root` (about 17:05Z)' % EF,
              'no order printed (facebranches.py at %s: %s); `record root` refused, NO ROOT, and the push moved by hand' % (BASE, old or 'ABSENT'),
              Lo[0].strip(), not old, need and 'push %s push-b743-sitting' % EF in Lo[0])
    need2, L2 = FBR.order(rows, EF, '8fbab45d8a96', '8fbab45d8a96')
    n += 1
    g += guard(L, 'order', 'after the push, main level with the remote: nothing waits', L2[0].strip(), not need2)
    need3, L3 = FBR.order([], EF, '8fbab45d8a96', 'badacccb867e')
    n += 1
    g += guard(L, 'order', 'no branch of the act listed (b744: no kernel write): nothing ordered', L3[0].strip(), not need3)
    return L, g, n


def control_repeat():
    L, g, n = ['### (repeat) (R354)(2)(vii)-(x): THE REPEAT READINGS AND INSTANCES'], 0, 0
    ev = io.open(os.path.join(D, 'b743_events.txt'), encoding='utf-8').read()
    msg = 'THE STEP BANK data/b743_steps.json CARRIES AN UNCOMMITTED ROW (commit the step rows before the push)'
    cls = CM.repeat_of(msg, 'b744')
    n += 1
    g += guard(L, 'repeat', '(vii) the record push sent with a step row uncommitted (events (13)): the push tool`s refusal of (R353)(3)(iii) working, its class',
               '%s ; events (13) REPEAT %s' % (cls, "(13) THE SEAT'S [CLOSE ; REPEAT]" in ev), cls.startswith('REPEAT') and "(13) THE SEAT'S [CLOSE ; REPEAT]" in ev)
    n += 1
    g += guard(L, 'repeat', '(viii) the post-push suite sent without its name (events (14)): the suite`s self-refusal working', 'events (14) REPEAT %s ; --rerun-postpush named %s' % (
        "(14) THE SEAT'S [CLOSE ; REPEAT]" in ev, '--rerun-postpush b743_checks_postpush.txt' in ev), "(14) THE SEAT'S [CLOSE ; REPEAT]" in ev)
    pc = os.path.join(D, 'b743_checks_postpush_standing-c.txt')
    ph = [l for l in io.open(pc, encoding='utf-8').read().split(NL) if 'PHASE' in l.upper()] if os.path.exists(pc) else []
    n += 1
    g += guard(L, 'repeat', '(ix) the chain class (events (12), standing-c 610 s): the phase table`s rows printed from b743`s post-push standing-c bank',
               '%d phase rows ; the first: %s' % (len(ph), (ph[0].strip()[:90] if ph else 'NONE')), bool(ph))
    j = HK.judge('PowerShell', {'command': 'X_LIFT=1 python lift.py'}, RELAY)
    n += 1
    g += guard(L, 'repeat', '(x) the author`s call refused for an environment prefix (events (5)): the hook`s ENV row working; the lift scripts carry no prefix',
               'judged %s' % (j[0] if j else 'ALLOWED'), bool(j) and j[0] == 'ENV')
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R354)(2)(xi): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = base_src('tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.23.1', ver == 'v1.24.0')
    return L, g, n


CONTROLS = {'prevdry': control_prevdry, 'prevdry-ok': control_prevdry_ok, 'tags': control_tags, 'repair': control_repair, 'hook': control_hook,
            'rewrite': control_rewrite, 'branches': control_branches, 'order': control_order, 'repeat': control_repeat, 'version': control_version}
ORDER = ('prevdry', 'prevdry-ok', 'tags', 'repair', 'hook', 'rewrite', 'branches', 'order', 'repeat', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.24.0, (R354)(2)(i)-(xi): THE PRE-LOCK DRY IN PREV MODE, THE REPAIR PHASE, THE HOOK`S SCOPE, NO PUSHED BANK '
           'REWRITTEN AND THE TAGS AT THE DRY, THE FACE`S BRANCH LIST, THE KERNEL PUSH BEFORE THE ROOT, THE REPEAT READINGS, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
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
    out.append('### ### **v1.24.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1240.txt' % act), NL.join(out))
        print('written data/%s_standing_v1240.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
