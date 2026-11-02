# -*- coding: utf-8 -*-
"""standing/v1150.py -- THE CONTROLS OF v1.15.0 ((R345)(2)(i)-(viii)), in v1140.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS; a version's bank that does not carry
its foot does not stand ((R345)(2)(i)). Written at b735 by the Write tool.

  python -X utf8 -u tools/standing/v1150.py control [compile|marks|kept|commits|entry|deletes|counter|exercise ...] [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import allow as AL              # noqa: E402
import compilecontrol as CC     # noqa: E402
import counterline as CN        # noqa: E402
import deletes as DL            # noqa: E402
import fold as F                # noqa: E402
import repaircommits as RC      # noqa: E402

BASE = '5609d5fd'               # ### b734's closing: every route of v1.14.0 as it stood, its two repairs in
V1140 = '59e3efa8'              # ### v1.14.0's commit, the template carrying the syntax error
OLD_KEPT = r'\bkept: [^.;]*?, and the rest as banked'
SESSION = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '7c29db99-62df-4f5e-a436-7e99b58f5dbf.jsonl')


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base(rel, at=BASE):
    return _git('show', '%s:%s' % (at, rel))


def _read(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.14.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.15.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.15.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def control_compile():
    L, g, n = ['### (compile) (R345)(2)(i), THE CONTROLS THAT DID NOT COMPILE, DEFECT (p): v1.14.0`S PARTS AS COMMITTED AT %s READ AS FAILING, v1.15.0`S AS PASSING' % V1140], 0, 0
    secs, _o = F._parse('b734', base('tools/acts/b734.py', V1140))
    tpl = base('tools/standing/fold/checks.tpl', V1140)
    try:
        compile(F.render('b734', 'checks', secs=secs, ovs={}, tpl=tpl), 'b734_checks.py', 'exec')
        err = None
    except SyntaxError as e:
        err = '%s at line %s' % (e.msg, e.lineno)
    c0 = CC.check('b734', V1140)
    now = CC.check(A.current()['act'])
    n += 1
    g += case(L, 'compile', 'the checks render at %s, the template blob with the act`s sections, the render every suite part runs' % V1140, 'v1.14.0`s 25 controls compiled no render: 25 of 25 printed over it; the render reads %s' % err,
              'the control over this tree: %s' % CC.lines(now)[-1], bool(err) and 'and__import__' in tpl, now['ok'])
    L += ['      the tool at %s, %d rows: %s' % (V1140, len(c0['rows']), ' ; '.join('%s %s' % (w, 'OK' if ok else 'FAIL') for w, ok, _d in c0['rows']))]
    n += 1
    g += guard(L, 'compile', 'the tool reads the commit: at %s not clear, at b734`s closing clear' % V1140, '%s ; %s' % (c0['ok'], CC.check('b734', BASE)['ok']), not c0['ok'] and CC.check('b734', BASE)['ok'])
    gate = io.open(os.path.join(T, 'b378_lockgate.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'compile', 'the lock refuses over a render that does not compile', 'tools/b378_lockgate.py reads compilecontrol: %s' % ('compilecontrol' in gate), 'compiled[\'ok\']' in gate)
    return L, g, n


def control_marks():
    L, g, n = ['### (marks) (R345)(2)(ii), DEFECT (q): b734`S THREE MARKERS FOUND AFTER A ONE-LINE INSERTION ABOVE THEM'], 0, 0
    secs, ovs = F._parse('b734', base('tools/acts/b734.py'))
    tpl = base('tools/standing/fold/checks.tpl')
    t0 = tpl.splitlines(keepends=True)
    want = F.render('b734', 'checks', secs=secs, ovs=ovs, tpl=tpl)
    moved = '# one line above them\n' + tpl
    try:
        got, why = F.render('b734', 'checks', secs=secs, ovs=ovs, tpl=moved), None
    except F.FoldRefused as e:
        got, why = None, str(e)
    three = [(a, b) for a, b, _t in ovs['checks'] if a in (1132, 1147, 1173)]
    marked = dict(checks=[(F.mark_of(t0[a - 1:a - 1 + max(b - a + 1, 1)]), b - a + 1, x) for a, b, x in ovs['checks']])
    new = F.render('b734', 'checks', secs=secs, ovs=marked, tpl=moved)
    n += 1
    g += case(L, 'marks', 'b734`s overrides of checks, the three %s among them, the template one line longer at its head' % three, 'keyed by line: %s' % (why or 'the render equal to the wanted: %s' % (got == '# one line above them\n' + want)),
              'keyed by mark: the render equal to the wanted, one line longer: %s' % (new == '# one line above them\n' + want), why or got != '# one line above them\n' + want, new == '# one line above them\n' + want)
    edited = tpl.replace(t0[1131], t0[1131].rstrip('\r\n') + ' # edited\n', 1)
    try:
        F.render('b734', 'checks', secs=secs, ovs=marked, tpl=edited)
        ref = False
    except F.FoldRefused:
        ref = True
    n += 1
    g += guard(L, 'marks', 'a line the override replaces, edited, refuses and is not silently replaced', 'refused %s' % ref, ref)
    try:
        F._parse('b735', '#⟪OVERRIDE checks 1 1⟫\nx\n#⟪END⟫\n')
        r2 = False
    except F.FoldRefused:
        r2 = True
    n += 1
    g += guard(L, 'marks', 'from b735 an override keyed by a line number is refused', 'refused %s ; the module`s own: numbers %d' % (r2, len(re.findall(r'(?m)^#⟪OVERRIDE \w+ \d', F._rd(F.sections_path('b735'))))), r2 and not re.search(r'(?m)^#⟪OVERRIDE \w+ \d', F._rd(F.sections_path('b735'))))
    return L, g, n


def control_kept():
    L, g, n = ['### (kept) (R345)(2)(iii), DEFECT (u): THE KEPT CLAUSE READ BY THE STANDING READER, THE OVERRIDE RETIRED'], 0, 0
    r4, r5 = _read('b734_ferry.txt'), _read('b735_ferry.txt')
    flat = lambda t: re.sub(r'\s+', ' ', t)
    old4, old5 = re.search(OLD_KEPT, flat(r4)), re.search(OLD_KEPT, flat(r5))
    c4, c5 = AL.kept_clause(r4), AL.kept_clause(r5)
    n4, n5 = AL.kept_names(r4), AL.kept_names(r5)
    n += 1
    g += case(L, 'kept', '(R344)(4)`s kept clause', 'the old needle reads %r' % (old4.group(0) if old4 else ''), 'the reader reads %s' % n4, not old4, bool(c4) and 'port-b707' not in n4 and len(n4) >= 4)
    n += 1
    g += case(L, 'kept', '(R345)(4)`s kept clause', 'the old needle reads %r' % (old5.group(0) if old5 else ''), 'the reader reads %s' % n5, not old5, n5 == ['c2-b725', 'keiper-b725', 'detect-b729', 'zq-b730'])
    n += 1
    g += guard(L, 'kept', 'the same names, the two rulings read by one reader; the override retired', 'equal %s ; the template reads kept_clause %s ; an override carrying it in b735`s module: %s' % (n4 == n5, 'STW.kept_clause' in F._rd(os.path.join(F.TPL_DIR, 'checks.tpl')), 'STW.kept_clause' in F._rd(F.sections_path('b735'))),
               n4 == n5 and 'STW.kept_clause' in F._rd(os.path.join(F.TPL_DIR, 'checks.tpl')) and 'STW.kept_clause' not in F._rd(F.sections_path('b735')))
    return L, g, n


def control_commits():
    L, g, n = ['### (commits) (R345)(2)(iv), b734`S TWO COMMITS READ AGAINST v1.14.0`S BANK AS UNCONTROLLED'], 0, 0
    bank = _read('b734_standing_v1140.txt')
    rows = RC.outside(V1140, BASE)
    ids = [h for h, _s in rows]
    n += 1
    g += case(L, 'commits', 'the commits after v1.14.0 to b734`s closing touching tools/standing/, VERSION unmoved', 'the version`s bank names 21a94e81: %s, 117ab5bc: %s; nothing read them' % ('21a94e81' in bank, '117ab5bc' in bank), 'the reader lists %s' % ids,
              '21a94e81' not in bank and '117ab5bc' not in bank, '21a94e81' in ids and '117ab5bc' in ids)
    gate = io.open(os.path.join(T, 'b378_lockgate.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'commits', 'the lock refuses while such a commit stands', 'tools/b378_lockgate.py reads repaircommits.outside: %s' % ('STANDING_REPAIRS.outside' in gate), 'STANDING_REPAIRS.outside' in gate and 'not stray' in gate)
    return L, g, n


def control_entry():
    L, g, n = ['### (entry) (R345)(2)(v), EVENT (5): THE ENTRY NAMES EVERY REPAIR COMMIT THE EVENTS BANK NAMES'], 0, 0
    fd = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
    e = [i for i in range(12750, len(fd)) if fd[i].startswith('## ')][1:2]
    entry = NL.join(fd[12750:(e[0] if e else len(fd))])
    ids = RC.named(_read('b734_events.txt'), _read('b734_defects.txt'))
    old = RC.missing(entry, ids)
    regen = entry + NL + RC.clause(ids)
    n += 1
    g += case(L, 'entry', 'b734`s entry at FINDINGS :12751, %d lines' % entry.count(NL), 'the commits the banks name that it omits: %s' % old, 'regenerated, the clause reads: %s' % RC.clause(ids), '117ab5bc' in old, not RC.missing(regen, ids) and '21a94e81' in ids and '117ab5bc' in ids)
    return L, g, n


def control_deletes():
    L, g, n = ['### (deletes) (R345)(2)(vi), DEFECT (s), G-LISTINGS-BEFORE-CLAUSES: b734`S FIVE DELETES REPLAYED WITH THE LISTING PRINTED'], 0, 0
    five = ('push-b734-closing', 'push-b734-preroot', 'push-b734-record')
    sess = io.open(SESSION, encoding='utf-8', errors='replace')
    hits = 0
    for line in sess:
        if '"timestamp":"2026-11-02T07:2' not in line or '--merged' not in line:
            continue
        o = json.loads(line)
        for x in ((o.get('message') or {}).get('content') or []):
            if isinstance(x, dict) and x.get('type') == 'tool_use' and x.get('name') in ('Bash', 'PowerShell') and re.search(r'git\b.*\bbranch\b.*--merged', (x.get('input') or {}).get('command', '')):
                hits += 1
    sess.close()
    with tempfile.TemporaryDirectory() as td:
        r = os.path.join(td, 'r').replace('\\', '/')
        subprocess.run(['git', 'init', '-q', '-b', 'main', r])
        subprocess.run(['git', '-C', r, '-c', 'user.name=control', '-c', 'user.email=control@example.invalid', 'commit', '-q', '--allow-empty', '-m', 'x'])
        for b in five:
            subprocess.run(['git', '-C', r, 'branch', b])
        keep = DL.bank
        p = os.path.join(td, 'bank.txt')
        DL.bank = lambda: p
        try:
            refused = DL.main(['delete', r, five[0]])
            DL.main(['list', r, 'push-b734-*'])
            rows = DL.listing(DL.rd())
            done = [DL.main(['delete', r, b]) for b in five]
            stray = DL.main(['delete', r, 'zq-b730'])
        finally:
            DL.bank = keep
        left = _git('branch', '--list', 'push-*', repo=r).split()
    n += 1
    g += case(L, 'deletes', 'the deletes with their listing', 'b734`s window, the seat`s tool calls carrying --merged at 07:2x: %d; the step-zero bank wrote the sentence ahead of it' % hits, 'a delete before the listing exit %d ; the listing %s ; the deletes exit %s ; a name outside it exit %d ; left %s' % (refused, rows, done, stray, left),
              hits == 0, refused == 3 and done == [0, 0, 0] and stray == 3 and not left)
    return L, g, n


def control_counter():
    L, g, n = ['### (counter) (R345)(2)(vii), EVENT (10): b734`S TWO FIGURES WITH THEIR DATED NOTE'], 0, 0
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
    hand = ot[17272]
    closing = _read('b734_closing.txt').split(NL)[4]
    a = CN.read(hand, closing)
    note = hand + ' Dated note, b735: the closing carries the last figure, event (10) landing after the record`s push.'
    b = CN.read(note, closing)
    n += 1
    g += case(L, 'counter', 'OPEN_TRAILS :17273 against data/b734_closing.txt :5', 'hand %s, closing %s, equal %s, names the closing %s' % (a['hand'], a['closing'], a['equal'], a['names_closing']), 'with the dated note: names the closing %s' % b['names_closing'], not a['ok'], b['ok'])
    n += 1
    g += guard(L, 'counter', 'equal figures pass with no note', str(CN.read(closing, closing)['ok']), CN.read(closing, closing)['ok'])
    return L, g, n


def control_exercise():
    L, g, n = ['### (exercise) (R345)(2)(viii): data/bNNN_exercise.json COMMITTED AT EVERY CLOSING, THE RULE WRITTEN, b733`S ABSENCE NOTED'], 0, 0
    last733 = _git('log', '-1', '--format=%h', '--', 'data/b733_exercise.json').strip()
    in734 = 'data/b734_exercise.json' in _git('show', '--name-only', '--format=', '5609d5fd').split()
    r = _read('b735_rules.txt')
    n += 1
    g += case(L, 'exercise', 'the bank at each closing', 'b733`s closing 05d53af9 carries it: %s; its last commit %s, the record' % ('data/b733_exercise.json' in _git('show', '--name-only', '--format=', '05d53af9').split(), last733), 'b734`s closing carries it: %s ; the rule in data/b735_rules.txt: %s' % (in734, '(1) THE EXERCISE BANK' in r),
              'data/b733_exercise.json' not in _git('show', '--name-only', '--format=', '05d53af9').split(), in734 and '(1) THE EXERCISE BANK' in r)
    return L, g, n


CONTROLS = dict(compile=control_compile, marks=control_marks, kept=control_kept, commits=control_commits, entry=control_entry, deletes=control_deletes, counter=control_counter, exercise=control_exercise)
ORDER = ('compile', 'marks', 'kept', 'commits', 'entry', 'deletes', 'counter', 'exercise')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.15.0, (R345)(2)(i)-(viii): THE COMPILE CONTROL AT THE HEAD, OVERRIDES BY MARK, THE KEPT CLAUSE, A REPAIR MOVES VERSION, THE ENTRY NAMES EVERY REPAIR, THE DELETE STEP`S LISTING, THE COUNTER`S RULE, THE EXERCISE BANK`S CARRY (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i)):'] + CC.lines(CC.check(act)) + ['', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.15.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1150.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1150.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
