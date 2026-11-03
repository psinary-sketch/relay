# -*- coding: utf-8 -*-
"""standing/v1170.py -- THE CONTROLS OF v1.17.0 ((R347)(2)(i)-(viii)), in v1160.py's form: each instance read through the route as it stood before the repair and through the repaired route; AS WANTED
where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the
repair is read from the blob at BASE (the act's step-zero commit), not from disk. Written at b737 by the Write tool.

  python -X utf8 -u tools/standing/v1170.py control [amend|gitwrite|locked|snapshot|promise|postseal|emptyread ...] [--bank]
"""
import io
import json
import os
import re
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
PP = 'D:/MY-DOwnloads/PLACE-papers'
SP736 = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf/scratchpad'
T736 = 'C:/Users/echo chamber/.claude/projects/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf.jsonl'
BASE = '58f2c295'   # ### b736's closing, the toolset as v1.16.0 left it
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import amend as AM              # noqa: E402
import compilecontrol as CC     # noqa: E402
import faceform as FF           # noqa: E402
import gitwrite as GW           # noqa: E402
import hook as HK               # noqa: E402
import rootprompt as RP         # noqa: E402
import scratchfsck as SF        # noqa: E402
import dispatchrows as DR       # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _read(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def base_module(rel, name):
    """the module at BASE, read from its blob and run in a fresh namespace, not from disk."""
    m = types.ModuleType(name)
    m.__file__ = os.path.join(RELAY, *rel.split('/'))
    exec(compile(_git('show', '%s:%s' % (BASE, rel)), name, 'exec'), m.__dict__)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.16.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.17.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.17.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return holds


DOORS = ('PLACE-papers/phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 'PLACE-papers/day1/Which_Structure_Confines_v2_4_0.md', 'PLACE-papers/phase2/physics/STORMER.md')


def b736_amendment():
    """b736's word amending (R346)(4), replayed as an amendment row: data/b736_author_words.txt :5 verbatim, its widened doors the three the passed items wrote."""
    w = [l for l in _read('b736_author_words.txt').split(NL) if l.startswith('BEGINThe author')]
    return dict(at='2026-11-02T22:44:30Z', clause='(R346)(4)', words=(w[0] if w else ''), widens=list(DOORS), narrows=[])


def control_amend():
    L, g, n = ['### (amend) (R347)(2)(i), b736 EVENTS (1): THE (W) ROW AND N5 REGENERATED FROM THE RULING PLUS ITS AMENDMENT ROWS; b736`S AMENDMENT REPLAYED'], 0, 0
    ruling, face = _read('b736_ferry.txt'), _read('b736_registration_2026-11-02.txt')
    row = b736_amendment()
    old = FF.w_missing(ruling, face)
    new = AM.missing(ruling, [row], face)
    n += 1
    g += case(L, 'amend', 'b736`s ruling and face, the amendment of (R346)(4) at the sitting`s head',
              'faceform.w_missing reads the ruling alone, the face lacking %s' % (old or 'nothing'), 'amend.missing with the row: %s' % new,
              not any(d in old for d in DOORS), all(d in new for d in DOORS))
    wr = AM.w_row(ruling, [row], face) or ''
    regen = face.replace('### (Z) THE NOTHINGS', wr + NL + '### (Z) THE NOTHINGS', 1) if '### (Z) THE NOTHINGS' in face else face + NL + wr
    n += 1
    g += guard(L, 'amend', 'the regenerated (W) row names the three doors in the scorer`s form, and a face carrying it lacks none', '%s ; after: %s' % (wr[:150], AM.missing(ruling, [row], regen) or 'none'),
               all('`%s`' % d in wr for d in DOORS) and not AM.missing(ruling, [row], regen))
    n += 1
    g += guard(L, 'amend', 'N5`s clause regenerated names what the face lacks', AM.n5_clause(ruling, [row], face)[:160], 'THE FACE LACKS' in AM.n5_clause(ruling, [row], face))
    nar = dict(row, widens=[], narrows=[DOORS[0]])
    n += 1
    g += guard(L, 'amend', 'a constructed narrowing row takes its path out of the files ordered', '%s' % (DOORS[0] in AM.writes(ruling, [row, nar])), DOORS[0] not in AM.writes(ruling, [row, nar]))
    return L, g, n


def control_gitwrite():
    L, g, n = ['### (gitwrite) (R347)(2)(ii), b736 EVENTS (7): GIT WRITES COUNTED PER MESSAGE ACROSS PARALLEL CALLS, THE SECOND REFUSED; b736`S 05:22Z PAIR REPLAYED'], 0, 0
    calls = GW.calls_of(T736, '2026-11-03T05:22:25', '2026-11-03T05:22:45')
    by = {}
    for c in calls:
        by.setdefault(c['mid'], []).append(c['cmd'])
    pair = [v for v in by.values() if sum(len(GW.writes(x)) for x in v) > 1]
    cmds = pair[0] if pair else []
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    old = [oldh.judge('Bash', {'command': c}) for c in cmds]
    new = [HK.over_one_write(cmds, i, GW) for i in range(len(cmds))]
    n += 1
    g += case(L, 'gitwrite', 'the message of 05:22:31Z: %s' % [c[:60] for c in cmds], 'the hook judged each call alone: %s' % [o and o[0] for o in old],
              'over_one_write by position: %s' % new, len(cmds) == 3 and old == [None, None, None], new == [False, True, False])
    n += 1
    g += guard(L, 'gitwrite', 'add and commit chained in one command, b736`s 22:22Z form, refused by the command alone', str(HK.judge('Bash', {'command': 'git add data/act_current.json && git commit -q -m "x"'})),
               (HK.judge('Bash', {'command': 'git add data/act_current.json && git commit -q -m "x"'}) or ('',))[0] == 'GITWRITE')
    n += 1
    g += guard(L, 'gitwrite', 'one write and a read in one command stand', str(HK.judge('Bash', {'command': 'git -C /d/relay log -1'})), HK.judge('Bash', {'command': 'git -C /d/relay log -1'}) is None)
    tmp = tempfile.mkdtemp(prefix='standing-v1170-gitwrite-')
    tp = os.path.join(tmp, 'session.jsonl')
    a, b = {'command': 'git -C D:/relay add data/x.txt'}, {'command': 'git -C D:/relay commit -q -m "x"'}
    with open(tp, 'w', encoding='utf-8', newline='\n') as f:
        for bid, inp in (('tu_1', a), ('tu_2', b)):
            f.write(json.dumps({'type': 'assistant', 'message': {'id': 'msg_x', 'content': [{'type': 'tool_use', 'id': bid, 'name': 'Bash', 'input': inp}]}}) + NL)
    j1 = HK.judge('Bash', a, ctx={'transcript_path': tp, 'tool_use_id': 'tu_1'})
    j2 = HK.judge('Bash', b, ctx={'transcript_path': tp, 'tool_use_id': 'tu_2'})
    n += 1
    g += guard(L, 'gitwrite', 'a constructed transcript, one message, two parallel calls: the first stands, the second refused (%s)' % tp, '%s ; %s' % (j1, j2 and j2[0]), j1 is None and bool(j2) and j2[0] == 'GITWRITE')
    return L, g, n


def control_locked():
    L, g, n = ['### (locked) (R347)(2)(iii), b736 EVENTS (3): A WRITE TO A LOCKED BANK REFUSED BY THE HOOK BEFORE IT LANDS; THE 04:03Z LETTER REPLAYED'], 0, 0
    oldh = base_module('tools/standing/hook.py', 'old_hook')
    p = os.path.join(D, 'b736_defects.txt')
    inp = {'file_path': p, 'old_string': 'x', 'new_string': 'y'}
    lock_t, close_t = _git('log', '-1', '--format=%cI', '95c40a00').strip(), _git('log', '-1', '--format=%cI', '58f2c295').strip()
    n += 1
    g += case(L, 'locked', 'an Edit of data/b736_defects.txt at 04:03:27Z, after the lock (95c40a00 at %s) and before the closing (%s)' % (lock_t, close_t),
              'the hook`s matcher Read|Bash|PowerShell and judge(Edit) -> %s' % (oldh.judge('Edit', inp),),
              'locked_bank -> %s (b736`s lockgate present %s)' % (HK.locked_bank(p, RELAY, 'b736'), os.path.exists(os.path.join(D, 'b736_lockgate.json'))),
              oldh.judge('Edit', inp) is None, HK.locked_bank(p, RELAY, 'b736') and os.path.exists(os.path.join(D, 'b736_lockgate.json')))
    n += 1
    g += guard(L, 'locked', 'the events bank, appended by the Edit tool after the lock, is exempt', str(HK.locked_bank(os.path.join(D, 'b736_events.txt'), RELAY, 'b736')), not HK.locked_bank(os.path.join(D, 'b736_events.txt'), RELAY, 'b736'))
    n += 1
    g += guard(L, 'locked', 'a file the lock never saw, untracked, passes', str(HK.locked_bank(os.path.join(D, 'b736_not_a_bank.txt'), RELAY, 'b736')), not HK.locked_bank(os.path.join(D, 'b736_not_a_bank.txt'), RELAY, 'b736'))
    tmp = tempfile.mkdtemp(prefix='standing-v1170-locked-')
    os.makedirs(os.path.join(tmp, 'data'))
    with open(os.path.join(tmp, 'data', 'act_current.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'act': 'b999', 'next': 'b1000'}) + NL)
    with open(os.path.join(tmp, 'data', 'b999_defects.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('a test bank\n')
    for a in (['init', '-q'], ['add', 'data/b999_defects.txt'], ['-c', 'user.email=control@invalid', '-c', 'user.name=control', 'commit', '-q', '-m', 'control']):
        subprocess.run(['git', '-C', tmp] + a, capture_output=True)
    before = HK.judge('Edit', {'file_path': os.path.join(tmp, 'data', 'b999_defects.txt')}, relay=tmp)
    with open(os.path.join(tmp, 'data', 'b999_lockgate.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('{}\n')
    after = HK.judge('Edit', {'file_path': os.path.join(tmp, 'data', 'b999_defects.txt')}, relay=tmp)
    n += 1
    g += guard(L, 'locked', 'a constructed relay (%s): the Edit stands before its lock and is refused after it' % tmp, '%s ; %s' % (before, after and after[0]), before is None and bool(after) and after[0] == 'LOCKED')
    return L, g, n


def control_snapshot():
    L, g, n = ['### (snapshot) (R347)(2)(iv), b736 DEFECT (m): FSCK, DISK FREE AND THE PROCESS LISTING BEFORE AND AFTER EVERY CLONE OPERATION AND DISPATCH READ; zqwork3`S READS THE CONTROL'], 0, 0
    oldd = base_module('tools/standing/dispatchrows.py', 'old_dispatchrows')
    zq3, zq1, zq2 = SP736 + '/zqwork3', SP736 + '/zqwork', SP736 + '/zqwork2'
    s1 = SF.snapshot(zq3)
    s2 = SF.snapshot(zq3)
    row = dict(kind='read', free_mb=4000, free_at='x', clone='zqwork3', fsck_before='ok', fsck_after='ok')
    n += 1
    g += case(L, 'snapshot', 'a read row of zqwork3 carrying its two fsck reads and nothing else', 'the v1.16.0 writer: %s' % (oldd.why(row),), 'the v1.17.0 writer: %s' % (DR.why(row),),
              oldd.why(row) is None, bool(DR.why(row)) and DR.why(dict(row, snap_before=s1, snap_after=s2)) is None)
    n += 1
    g += guard(L, 'snapshot', 'zqwork3`s two snapshots, printed: the fsck, the disk`s free space, the processes (the fsck`s verdict a finding, not this guard`s condition)', '%s || %s' % (SF.line(s1), SF.line(s2)),
               all(s.get('fsck') and s['disk_free_mb'] is not None and bool(s['procs']) for s in (s1, s2)))
    ob = os.path.join(zq3, '.git', 'objects')
    lost = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(ob))) if os.path.isdir(ob) else 'ABSENT'
    n += 1
    g += guard(L, 'snapshot', 'THE THIRD LOSS, PRINTED: zqwork3, clean at b736 (data/b736_standing_v1160.txt), reads not clean, its pack and info directories gone, objects/ last written %s; the two before at 2026-11-02T15:33:57Z (zqwork) and 21:44:22Z (zqwork2)' % lost,
               '%s ; pack %s ; info %s' % (s1['fsck'][:70], os.path.isdir(os.path.join(ob, 'pack')), os.path.isdir(os.path.join(ob, 'info'))),
               not s1['fsck_ok'] and not os.path.isdir(os.path.join(ob, 'pack')))
    n += 1
    g += guard(L, 'snapshot', 'a clone operation is a row kind of its own and carries the same', str(DR.why(dict(kind='clone', free_mb=4000, free_at='x', clone='zqwork4'))), bool(DR.why(dict(kind='clone', free_mb=4000, free_at='x', clone='zqwork4'))))
    d1, d2 = SF.read(zq1), SF.read(zq2)
    n += 1
    g += guard(L, 'snapshot', 'the two damaged clones left in place, each still not clean, until the cause is named or the author orders their deletion by name', '%s ; %s' % (d1[1][:80], d2[1][:80]),
               os.path.isdir(zq1) and os.path.isdir(zq2) and not d1[0] and not d2[0])
    return L, g, n


def _b736_entry():
    t = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
    i = next(k for k, l in enumerate(t) if l.startswith('## W-ORD-ZQ-DERIVES discharged on the three premise-free forms'))
    j = next((k for k in range(i + 1, len(t)) if t[k].startswith('## ')), len(t))
    return NL.join(t[i:j])


def control_promise():
    L, g, n = ['### (promise) (R347)(2)(v), b736 EVENTS (5): THE ROOT PROMPT`S SENTENCES ABOUT THE ENTRY TAKEN FROM THE SEALED COMPOSER; b736`S PROMPT REGENERATED WITHOUT THE PROMISE'], 0, 0
    ans = _read('b736_author_answers.txt').split(NL)
    opt = next(l for l in ans if 'OPTION 1 [RECOMMENDED]: Land, N5 REFUTED' in l)
    entry = _b736_entry()
    oldr = base_module('tools/standing/rootprompt.py', 'old_rootprompt')
    rows = [[opt.split(':: ', 1)[1]]]
    try:
        oldr.compose(rows, lambda b, l: None)
        old_ok = True
    except SystemExit:
        old_ok = False
    bad = RP.entry_unbacked(rows[0][0], entry)
    n += 1
    g += case(L, 'promise', 'b736`s recommended option at data/b736_author_answers.txt :332', 'compose passed it: %s' % old_ok, 'entry_unbacked: %s' % bad, old_ok, any('named in the entry' in x for x in bad))
    fixed = rows[0][0].replace('named in the entry and the events bank', 'standing at rows (1) and (2) of the events bank')
    n += 1
    g += guard(L, 'promise', 'the option regenerated without the promise composes', str(RP.entry_unbacked(fixed, entry)), not RP.entry_unbacked(fixed, entry))
    q = 'The entry\'s head reads "W-ORD-ZQ-DERIVES discharged on the three premise-free forms".'
    n += 1
    g += guard(L, 'promise', 'a sentence quoting the composed entry stands; one quoting what it does not carry is refused', '%s ; %s' % (RP.entry_unbacked(q, entry), RP.entry_unbacked(q.replace('three', 'four'), entry)),
               not RP.entry_unbacked(q, entry) and bool(RP.entry_unbacked(q.replace('three', 'four'), entry)))
    return L, g, n


def control_postseal():
    L, g, n = ['### (postseal) (R347)(2)(vi), b736 EVENTS (8): THE POST-SEAL EXCLUDE LIST READ BEFORE ANY READ; THE ARM`S SECOND FAILURE A REPEAT'], 0, 0
    rule = HK.ledger_rule()
    cmd = 'git -C D:/MY-DOwnloads/PLACE-papers grep -c "x" -- FINDINGS.md'
    n += 1
    g += guard(L, 'postseal', 'the rule as the arm holds it, printed by `hook.py excludes`', 'ledgers %s ; excludes %d' % (rule and rule[0], len(rule[1]) if rule else -1), rule is not None and 'FINDINGS.md' in rule[0])
    n += 1
    g += guard(L, 'postseal', 'b736`s 05:20:50Z form, a `git grep` naming FINDINGS.md, is a read the arm counts', str(HK.postseal_read(cmd)), HK.postseal_read(cmd))
    ev = _read('b736_events.txt')
    n += 1
    g += guard(L, 'postseal', 'b736`s second failure of the arm carried as REPEAT in the corrigendum, the first b732 event (11)', 'events (8) printed NEW: %s' % ('(8) THE SEAT\'S [CLOSE ; NEW]' in ev), '(8) THE SEAT\'S [CLOSE ; NEW]' in ev)
    return L, g, n


def control_emptyread():
    L, g, n = ['### (emptyread) (R347)(2)(vii), b736 EVENTS (9): AN EMPTY REMOTE READ IS A REFUSAL WITH ITS OWN WORD; b736`S THREE REPOSITORIES REPLAYED OVER A STAND-IN _verify, NO REMOTE TOUCHED'], 0, 0
    import act_root as AR
    empty = ['SIDE-structural-error-correction', 'SIDE-substrate-cluster', 'SIDE-trivium']
    answered = {'refs/heads/main': 'a' * 40}

    def fake(p):
        return {} if any(p.endswith(x) for x in empty) else answered

    def stand_in(remote, worktree=None, acts=None):
        why = ['head %s %s not on the remote main ' % (r, 'b' * 12) for r in empty + ['SIDE-grh-transfer'] if not remote(AR.path_of(r)).get('refs/heads/main')]
        return [('b632', 'DISAGREE' if why else 'AGREE', why)]
    keep = AR._verify
    AR._verify = stand_in
    try:
        r = AR.verify(remote=fake)
    finally:
        AR._verify = keep
    n += 1
    g += guard(L, 'emptyread', 'three repositories read empty, the others answered: the row reads UNREAD, not AGREE and not DISAGREE', r[0][1], r[0][1] == 'UNREAD')
    b2b = _read('b736_checks_postpush_standing-b2b.txt')
    n += 1
    g += guard(L, 'emptyread', 'b736`s part, re-run alone after one direct read, banked AGREE; its first read`s UNREAD stands in the events bank alone', 'the bank`s AGREE rows %d ; UNREAD %d' % (b2b.count(' AGREE'), b2b.count('UNREAD')),
               'UNREAD' not in b2b and '(9) THE HOST' in _read('b736_events.txt'))
    return L, g, n


CONTROLS = dict(amend=control_amend, gitwrite=control_gitwrite, locked=control_locked, snapshot=control_snapshot, promise=control_promise, postseal=control_postseal, emptyread=control_emptyread)
ORDER = ('amend', 'gitwrite', 'locked', 'snapshot', 'promise', 'postseal', 'emptyread')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.17.0, (R347)(2)(i)-(viii): THE AMENDMENT REGENERATION AT THE HEAD, THE PARALLEL GIT WRITE, THE LOCKED BANK, THE CLONE`S SNAPSHOT, THE ENTRY`S PROMISE, THE POST-SEAL LIST, THE EMPTY REMOTE READ (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + ['', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, c = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
    out.append('### ### **v1.17.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1170.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1170.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
