# -*- coding: utf-8 -*-
"""standing/v1140.py -- THE CONTROLS OF v1.14.0 ((R344)(2)(i)-(ix)), in v1130.py's form: each instance read through the route as it stood before the repair (at BASE, the commit before this version) and through
the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. Written at b734 by the Write tool.

  python -X utf8 tools/standing/v1140.py control [probes|ceiling|gitwrite|date|subjects|retired|emptyread|clauses|defectids ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v1140.txt with every control run, nothing else.
"""
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
NL = '\n'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import act_root as AR           # noqa: E402
import cites as CT              # noqa: E402
import close as CL              # noqa: E402
import defectids as DI          # noqa: E402
import gitwrite as GW           # noqa: E402
import prelock as PL            # noqa: E402
import probes as PB             # noqa: E402
import rootprompt as RP         # noqa: E402
import subjects as SJ           # noqa: E402

BASE = '15f2bd8b'               # ### relay's step-zero tip: every route of v1.13.0 as it stood
B733_LOCK, B733_PRELOCK, B733_CLOSE = '09fe2151', '754e419f', '05d53af9'   # ### b733's lock commit, the last commit before it, its closing commit
B732_LOCK, B732_PRELOCK = '0d8d0be0', 'b33ffcc1'   # ### b732's lock commit and the last commit before it
SEAL_SUBJECT = 'b733 seal: the sealed tools` hashes, 62 files'
SESSION = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '7c29db99-62df-4f5e-a436-7e99b58f5dbf.jsonl')
WINDOW = ('2026-11-02T00:40:00Z', '2026-11-02T05:40:00Z')


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def base(rel, at=BASE):
    return _git('show', '%s:%s' % (at, rel))


def tree(at, prefix):
    return [x for x in _git('ls-tree', '-r', '--name-only', at, '--', 'data/').split(NL) if x.startswith(prefix)]


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.13.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.14.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.14.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


def control_probes():
    L, g, n = ['### (probes) (R344)(2)(i), THE CLASS AT ITS HEAD, b729 trap 4, b731`S NAME, b733 EVENT (11): b733`S TREE REPLAYED AGAINST THE GATE WITH NO EDIT, AND b732`S CLEAN LOCK'], 0, 0
    t733 = tree(B733_PRELOCK, 'data/b733_')
    refused, lines = PB.refusal('b733', t733)
    bad = PB.outputs('b733', t733)
    seventeen = set(x for x in bad if '_lsr_' not in x)
    n += 1
    g += case(L, 'probes', 'b733`s tree at %s, the commit before its lock, %d tracked act banks' % (B733_PRELOCK, len(t733)),
              'the gate at BASE reads no tracked path (a refusal in tools/b378_lockgate.py: %s); it permitted the lock' % ('probes' in base('tools/b378_lockgate.py')),
              'the gate refuses, %d paths printed' % len(bad), 'probes' not in base('tools/b378_lockgate.py'), refused and seventeen <= set(bad))
    L += ['      %s' % x for x in lines]
    more = sorted(set(bad) - seventeen)
    moved = [x for x in more if _git('diff', '--name-only', B733_LOCK, B733_CLOSE, '--', x).strip()]
    n += 1
    g += guard(L, 'probes', 'the count: b733 event (11) named seventeen, every one rewritten by the pre-push suite; the gate reads %d, the seven ls-remote banks beside them, tracked at the lock too and rewritten by no later commit' % len(bad),
               'the seventeen among the refused: %d ; the others %d, moved after the lock: %d (the event`s seventeen stands for what N4 read; the class is the wider)' % (len(seventeen & set(bad)), len(more), len(moved)), len(seventeen & set(bad)) == 17 and len(more) == 7 and not moved)
    t732 = tree(B732_PRELOCK, 'data/b732_')
    r2, l2 = PB.refusal('b732', t732)
    n += 1
    g += guard(L, 'probes', 'b732`s lock at %s passes: the gate refuses no clean tree' % B732_PRELOCK, '%d tracked act banks ; %s' % (len(t732), l2[0].strip()), not r2)
    if r2:
        L += ['      %s' % x for x in l2]
    n += 1
    g += guard(L, 'probes', 'a suite part before the lock writes the probe path: b734 has no permitting gate, b733 has one', 'auto(b734) %s ; auto(b733) %s ; the base %s ; part %s' % (PB.auto('b734', D), PB.auto('b733', D), PB.BASE % 'b734', (PB.BASE % 'b734').replace('.txt', '_act.txt')),
               PB.auto('b734', D) and not PB.auto('b733', D))
    n += 1
    g += guard(L, 'probes', 'a tracked probe path is refused too, an untracked one is nothing to the gate ((N4): no tracked path is a probe output)', 'refused %s ; on an empty list %s' % (PB.refusal('b734', ['data/b734_probe_act.txt'])[0], PB.refusal('b734', [])[0]),
               PB.refusal('b734', ['data/b734_probe_act.txt'])[0] and not PB.refusal('b734', [])[0])
    c = PL.compare.__defaults__
    n += 1
    g += guard(L, 'probes', 'the pre-lock comparison reads the probes` banks', 'the default form %s' % (c[-1],), c[-1] == '%s_probe_%s.txt')
    return L, g, n


def control_ceiling():
    L, g, n = ['### (ceiling) (R344)(2)(ii), b733 EVENT (11): THE PROMPT`S CEILING A DRY SCORE, NOT A TYPED LINE; b733`S PROMPT REGENERATED'], 0, 0
    sc = json.load(io.open(os.path.join(D, 'b733_scores.json'), encoding='utf-8'))
    at_prompt = dict((k, ('REFUTED' if k == 'N5' else 'HELD')) for k in sc)   # ### the scores as b733's prompt read them, data/b733_events.txt :19: N5 REFUTED and the others held; the two answers pending read as may-hold
    tracked = tree(B733_LOCK, 'data/b733_')
    h, of, line = RP.ceiling(at_prompt, tracked, 'b733')
    n += 1
    g += case(L, 'ceiling', 'b733`s prompt, scores at prompt time, its lock commit`s tree', 'the typed line "at most 7 of 8", the seat`s; the close read 6', line, True, h == 6 and of == 8)
    h2, _o, l2 = RP.ceiling(at_prompt, tree(B732_LOCK, 'data/b732_'), 'b732')
    n += 1
    g += guard(L, 'ceiling', 'a clean lock loses nothing to the rule', l2, h2 == 7)
    h3, _o, l3 = RP.ceiling(at_prompt, [], 'b733', modified=['data/b733_defects.txt'])
    n += 1
    g += guard(L, 'ceiling', 'a tracked bank edited after the lock loses N4 at the prompt', l3, h3 == 6)
    return L, g, n


def control_gitwrite():
    import rule_arms as RA
    L, g, n = ['### (gitwrite) (R344)(2)(iii), b733 EVENT (10): GIT_WRITE MATCHES THE COMMAND, NOT THE PATH; b733`S EIGHTH MESSAGE'], 0, 0
    calls = GW.calls_of(SESSION, *WINDOW)
    msg = [c for c in calls if c['ts'].startswith('2026-11-02T04:37:5') and 'push_gated.sh' in c['cmd']]
    cmd = msg[0]['cmd'] if msg else ''
    old = [c for c in GW.commands(cmd) if RA.GIT_WRITE.search(c) and not GW.is_listing(c)]
    new = GW.writes(cmd)
    n += 1
    g += case(L, 'gitwrite', 'the message at 04:37:54Z, the commit ca9c2162 chained to a read of the path', 'writes %d' % len(old), 'writes %d' % len(new), len(old) == 2, len(new) == 1)
    _ok, _n, over, _note = GW.reading(calls)
    n += 1
    g += guard(L, 'gitwrite', 'the arm`s count over b733`s window falls from 8 to the real 7', '%d messages over the row' % len(over), len(over) == 7)
    n += 1
    g += guard(L, 'gitwrite', 'the gated push itself stays a write', 'bash tools/push_gated.sh: %d ; a read naming it: %d' % (len(GW.writes('bash /d/relay/tools/push_gated.sh relay push-b734-x')), len(GW.writes('git grep -n x -- tools/push_gated.sh'))),
               len(GW.writes('bash /d/relay/tools/push_gated.sh relay push-b734-x')) == 1 and not GW.writes('git grep -n x -- tools/push_gated.sh'))
    return L, g, n


def control_date():
    L, g, n = ['### (date) (R344)(2)(iv), b733 EVENT (3): ONE DATE SOURCE; "THE FACE IS NOT LOCKED" REPLAYED, close.py SEAL WITH NO SCRATCH CALLER'], 0, 0
    cur = json.loads(_git('show', '%s:data/act_current.json' % B733_LOCK))
    old = CL.lock_of('b733', cur['date']) if os.path.exists(os.path.join(D, 'b733_registration_%s.txt' % cur['date'])) else None
    new = CL.lock_of('b733', CL.act_date('b733'))
    n += 1
    g += case(L, 'date', 'b733 at its lock: act_current`s field %s, the worklist`s DATE %s' % (cur['date'], CL.act_date('b733')), 'close.py built the face from the field: no face, "THE FACE IS NOT LOCKED"', 'the face read, locked at %s' % new, old is None, bool(new))
    src = open(os.path.join(S, 'close.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'date', 'close.py`s main reads no date field of act_current', "cur['date'] in close.py: %d" % src.count("cur['date']"), not src.count("cur['date']"))
    return L, g, n


def _read(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f) if name.endswith('.json') else f.read()


def control_subjects():
    L, g, n = ['### (subjects) (R344)(2)(v), b733 EVENTS (2), (5): THE SUBJECT COMPOSED FROM THE BANK'], 0, 0
    bad = SJ.check('b733', 'seal', SEAL_SUBJECT, _read)
    n += 1
    g += case(L, 'subjects', 'the seal subject', '"%s" typed, the commit took it' % SEAL_SUBJECT, '%s ; composed "%s"' % (bad, SJ.compose('b733', 'seal', '', _read)), True, bad and '63 files' in SJ.compose('b733', 'seal', '', _read))
    subj = _git('log', '-1', '--format=%s', B733_LOCK).strip()
    bad2 = SJ.check('b733', 'lock', subj, _read)
    n += 1
    g += case(L, 'subjects', 'the lock commit`s subject', '"%s..." typed, the commit took it' % subj[:40], '%s' % bad2, True, bool(bad2))
    subj2 = _git('log', '-1', '--format=%s', B732_LOCK).strip()
    n += 1
    g += guard(L, 'subjects', 'b732`s lock subject reads clean', '"%s..." -> %s' % (subj2[:40], SJ.check('b732', 'lock', subj2, _read) or 'NO DIFFERENCE'), not SJ.check('b732', 'lock', subj2, _read))
    return L, g, n


def control_retired():
    import arms as AM
    L, g, n = ['### (retired) (R344)(2)(vi): THE PRINTED NAME G-READ-RULE-STANDING, ON NO ARM OF THE 116 AT b732 AND b733; THE CHOICE: THE PRINT REMOVED, THE ARM STANDING RETIRED'], 0, 0
    old = base('tools/standing/fold/checks.tpl').count('G-READ-RULE-STANDING`S READING')
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    n += 1
    g += case(L, 'retired', 'the suite`s template', 'prints the retired arm`s reading %d time(s), an arm`s name with no row' % old, 'prints it %d time(s)' % tpl.count('G-READ-RULE-STANDING`S READING'), old == 1, not tpl.count('G-READ-RULE-STANDING`S READING'))
    n += 1
    g += guard(L, 'retired', 'the name stands on the retired list, so no row is owed', 'in tools/standing/arms.py`s retired list: %s' % ('G-READ-RULE-STANDING' in open(os.path.join(S, 'arms.py'), encoding='utf-8').read()), 'G-READ-RULE-STANDING' in open(os.path.join(S, 'arms.py'), encoding='utf-8').read())
    return L, g, n


def control_emptyread():
    L, g, n = ['### (emptyread) (R344)(2)(vii), b733 (o): AN EMPTY REMOTE READ IS ITS OWN WORD; b733`S READ REPLAYED OVER A STAND-IN _verify, NO REMOTE TOUCHED'], 0, 0
    empty = ['SIDE-trivium', 'SIDE-yang-mills-formation', 'relay']
    answered = {'refs/heads/main': 'a' * 40}

    def run(mod):
        def fake(p):
            return {} if any(p.endswith(x) for x in empty) else answered

        def stand_in(remote, worktree=None, acts=None):
            why = []
            for r in empty + ['SIDE-grh-transfer']:
                if not remote(mod.path_of(r)).get('refs/heads/main'):
                    why.append('head %s %s not on the remote main ' % (r, 'b' * 12))
            return [('b733', 'DISAGREE' if why else 'AGREE', why), ('b700', 'AGREE', []), ('b701', 'DISAGREE', ['bank data/x changed'])]
        keep = mod._verify
        mod._verify = stand_in
        try:
            return mod.verify(remote=fake)
        finally:
            mod._verify = keep
    src = base('tools/act_root.py')
    oldm = types.ModuleType('old_act_root')
    oldm.__file__ = AR.__file__
    exec(compile(src, 'old_act_root', 'exec'), oldm.__dict__)   # ### the route at BASE, read not run from disk
    old, new = run(oldm), run(AR)
    n += 1
    g += case(L, 'emptyread', 'three repositories read empty, others answered', 'the row reads %s' % old[0][1], 'the row reads %s' % new[0][1], old[0][1] == 'DISAGREE', new[0][1] == 'UNREAD')
    n += 1
    g += guard(L, 'emptyread', 'a row with a reason of its own stays DISAGREE, an AGREE stays', '%s ; %s' % (new[2][1], new[1][1]), new[2][1] == 'DISAGREE' and new[1][1] == 'AGREE')
    return L, g, n


def control_clauses():
    L, g, n = ['### (clauses) (R344)(2)(viii), b733 EVENT (8): THE CLAUSE READ FROM THE RULING`S TEXT; b733`S ENTRY LINE REGENERATED'], 0, 0
    c733 = CT.next_clause(_read('b733_ferry.txt'))
    n += 1
    g += case(L, 'clauses', 'b733`s touch-read line', 'the composer printed "the next act of (R343)(9)", a clause the ruling has not: (R343) has six', '"the next act of %s"' % c733, '(R343)(9)' in base('tools/acts/b733.py'), c733 == '(R343)(6)')
    c734 = CT.next_clause(_read('b734_ferry.txt'))
    n += 1
    g += guard(L, 'clauses', 'b734`s own ruling reads (R344)(6)', c734, c734 == '(R344)(6)')
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'clauses', 'the freeze line prints no typed clause number', 'typed: %s' % ('(⟪RUL⟫)(10) retired' in tpl), '(⟪RUL⟫)(10) retired' not in tpl)
    return L, g, n


def control_defectids():
    L, g, n = ['### (defectids) (R344)(2)(ix), b733 EVENT (9): A DEFECT`S COMMIT IDS READ FROM THE LOG'], 0, 0
    calls = GW.calls_of(SESSION, *WINDOW)

    def log(subject, cmd):
        m = re.search(r'git\s+-C\s+("[^"]+"|\S+)', cmd)
        repo = m.group(1).strip('"') if m else RELAY
        repo = repo if os.path.isdir(repo) else AR.path_of('SIDE-explicit-formula')   # ### a working clone gone since: the kernel's own clone, which holds the branch
        hs = [x for x in _git('log', '--all', '--fixed-strings', '--grep=' + subject.split(chr(10))[0], '--format=%h', repo=repo).split() if x]
        return [(h, os.path.basename(repo.rstrip('/'))) for h in hs]
    rows = DI.commits_over(calls, log)
    ids = [r[1] for r in rows if r[1]]
    L += ['      %s %s %s' % r for r in rows]
    n += 1
    g += case(L, 'defectids', 'b733 defect (q)`s seven', 'the hand list named relay 3471c14b', 'the log`s ids: %d rows; 3471c14b among them: %s ; 834f6ac among them: %s' % (len(rows), any(i.startswith('3471c14') for i in ids), any(i.startswith('834f6ac') for i in ids)),
              '3471c14b' in _read('b733_defects.txt'), not any(i.startswith('3471c14') for i in ids) and any(i.startswith('834f6ac') for i in ids))
    return L, g, n


CONTROLS = dict(probes=control_probes, ceiling=control_ceiling, gitwrite=control_gitwrite, date=control_date, subjects=control_subjects, retired=control_retired, emptyread=control_emptyread, clauses=control_clauses, defectids=control_defectids)
ORDER = ('probes', 'ceiling', 'gitwrite', 'date', 'subjects', 'retired', 'emptyread', 'clauses', 'defectids')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.14.0, (R344)(2)(i)-(ix): THE PROBE-BANK CLASS AT THE HEAD, THE PROMPT`S CEILING, GIT_WRITE ON THE COMMAND, ONE DATE SOURCE, SUBJECTS FROM THE BANK, THE RETIRED PRINT, THE EMPTY READ, CLAUSES FROM THE RULING, DEFECT IDS FROM THE LOG (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.14.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1140.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1140.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
