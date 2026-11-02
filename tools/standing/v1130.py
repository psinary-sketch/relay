# -*- coding: utf-8 -*-
"""standing/v1130.py -- THE CONTROLS OF v1.13.0 ((R343)(2)(i)-(viii)), in v1120.py's form: each instance read through the route as it stood before the repair (at BASE, the commit before this version) and through
the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. Written at b733 by the Write tool.

  python -X utf8 tools/standing/v1130.py control [prelock|rows|needle|note|orcid|postseal|carry ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v1130.txt with every control run, nothing else.
  python -X utf8 tools/standing/v1130.py note
        writes data/<act>_2c_note.txt: the note's words amended as the author's row (6) ruled, the rooted bank unedited.
"""
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
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import allow as AL              # noqa: E402
import carry as CR              # noqa: E402
import dispatchrows as DR       # noqa: E402
import hook as HK               # noqa: E402
import prelock as PL            # noqa: E402

BASE = '0dc27476'               # ### relay's step-zero tip: every route of v1.12.0 as it stood
B732_CLOSE = 'a8a702dd'         # ### b732's closing commit
HOLD_READ = (4314, '2026-11-01T18:41:53Z')   # ### b732's hold, read before its push: command #120, data/b732_commands.txt :189-:193
# ### b732 event (11): the two commands, from the session's transcript at their times; nothing runs them, they are judged
POSTSEAL_CMDS = (('2026-11-01T22:19:23Z', 'git -C /d/MY-DOwnloads/PLACE-papers grep -n -E "^### b731 |^\\*\\*.*b731.*(hand|dated)|^### b730 — " -- OPEN_TRAILS.md'),
                 ('2026-11-01T22:20:08Z', 'wc -l /d/MY-DOwnloads/PLACE-papers/OPEN_TRAILS.md'))
NOTE_OLD = 'make a worked example of three kinds of premise.'
NOTE_NEW = 'and the C2 certificates beside them, make a worked example of three kinds of premise, the five fields instancing two kinds and the C2 certificates the third.'


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def base(rel, at=BASE):
    return _git('show', '%s:%s' % (at, rel))


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.12.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.13.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.13.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def control_prelock():
    L, g, n = ['### (prelock) THE PRE-LOCK FAILING-LIST COMPARISON, (R343)(2)(i), b732 event (3); THE INSTANCE, b732`S TWO ARMS ON b731`S LISTS'], 0, 0
    c = PL.compare('b732', 'b731', form='%s_arms_prerun_%s.txt')
    names = [a for _q, a, _v in c['newly']]
    n += 1
    g += case(L, 'prelock', 'b732`s pre-run lists, seven parts, against b731`s: arms read %d, failing %d and %d' % (c['arms'], len(c['mine']), len(c['theirs'])),
              'the gate at BASE reads no list (a comparison step in reg_gate.tpl: %s; prelock.py at BASE: %s); the lock went at 20:23Z and the lists were read at 20:58Z, b732 event (3)' % ('comparison' in base('tools/standing/fold/reg_gate.tpl'), bool(base('tools/standing/prelock.py'))),
              'newly failing by name: %s' % names, 'comparison' not in base('tools/standing/fold/reg_gate.tpl'), 'G-RUNNER-GATE' in names and 'G-DELETES-ONE-BRANCH' in names and not c['missing'])
    n += 1
    g += guard(L, 'prelock', 'a ruling`s own arm is the same arm across acts: G-R342-ENTERED failing at b732, G-R341-ENTERED at b731', 'G-R342-ENTERED among the newly failing: %s' % ('G-R342-ENTERED' in names),
               'G-R342-ENTERED' in c['mine'] and 'G-R342-ENTERED' not in names)
    _L, u0 = PL.lines(c, '')
    _L, u1 = PL.lines(c, ' '.join(names))
    n += 1
    g += guard(L, 'prelock', 'the gate`s reading: an arm not on the face holds the gate, the same arm on the face does not', 'not on an empty face %d ; not on a face naming them %d' % (len(u0), len(u1)), len(u0) == len(names) and not u1)
    n += 1
    g += guard(L, 'prelock', 'the seal reads the bank again: b732 has none, so the seal of an act without the step refuses', 'stands(b732) %s ; the refusal at close.py: %s' % (PL.stands('b732'), 'STEP [5b]' in open(os.path.join(S, 'close.py'), encoding='utf-8').read()),
               not PL.stands('b732') and 'STEP [5b]' in open(os.path.join(S, 'close.py'), encoding='utf-8').read())
    return L, g, n


def control_rows():
    L, g, n = ['### (rows) EVERY DISPATCH-ROW KIND CARRIES free_mb FROM THE READ BEFORE IT, (R343)(2)(ii), b732 event (1); THE INSTANCE, b732`S PUSH AND DISPATCH ROWS'], 0, 0
    rows = json.loads(rd('b732_dispatch_rows.json'))
    mem = [r for r in rows if r.get('kind') in ('push', 'push2', 'dispatch', 'dispatch_refused', 'read')]
    gate_old = all((r.get('free_mb') or 0) >= DR.HOLD for r in mem)
    bad = DR.check(rows)
    wrote = False
    tmp = os.path.join(tempfile.mkdtemp(prefix='standing-v1130-rows-'), 'rows.json')
    try:
        DR.write(tmp, rows)
        wrote = True
    except ValueError:
        pass
    n += 1
    g += case(L, 'rows', 'data/b732_dispatch_rows.json, %d rows, %s' % (len(rows), [r['kind'] for r in rows]), 'tools/b732_a0.py wrote the file with free_mb on the read row alone, nothing refusing: gate_ok`s memory clause over its rows %s, read after the lock' % gate_old,
              'the one writer refuses them before writing: %s ; a file written %s' % ([(i, k) for i, k, _w in bad], wrote), not gate_old, [k for _i, k, _w in bad] == ['commit', 'push', 'dispatch'] and not wrote and not os.path.exists(tmp))
    fixed = [dict(r, free_mb=HOLD_READ[0], free_at=HOLD_READ[1]) for r in rows]
    n += 1
    g += guard(L, 'rows', 'the same four rows with b732`s own read before them, 4314 MB at 18:41:53Z, pass; a figure under the hold does not', 'refused %d ; under the hold refused %d' % (len(DR.check(fixed)), len(DR.check([dict(fixed[1], free_mb=2559)]))),
               not DR.check(fixed) and len(DR.check([dict(fixed[1], free_mb=2559)])) == 1)
    n += 1
    try:
        DR.row('dispatch', (None, None), run=1)
        refused = False
    except ValueError:
        refused = True
    g += guard(L, 'rows', 'the row route: a row made with no read refuses at the row', 'refused %s' % refused, refused)
    return L, g, n


def control_needle():
    L, g, n = ['### (needle) THE G-DELETES-ONE-BRANCH NEEDLE READ FROM THE ACT`S FERRY, (R343)(2)(iii), b732 event (2); THE INSTANCE, b732`S HAND NEEDLE AGAINST ITS FERRY`S LINE'], 0, 0
    ferry = re.sub(r'\s+', ' ', rd('b732_ferry.txt'))
    m = re.search(r"or '(kept: [^']*)' in S\['ferry'\]", base('tools/acts/b732.py', B732_CLOSE))
    hand = m.group(1)
    read = AL.kept_clause(ferry)
    n += 1
    g += case(L, 'needle', 'tools/acts/b732.py at %s, the override`s string against data/b732_ferry.txt' % B732_CLOSE, 'the hand string "%s" in the ferry: %s' % (hand, hand in ferry),
              'allow.kept_clause reads "%s" ; in the ferry: %s' % (read, bool(read) and read in ferry), hand not in ferry, bool(read) and read in ferry and 'zq-b730' in read)
    f3 = re.sub(r'\s+', ' ', rd('b733_ferry.txt'))
    m3 = re.search(r"or '(kept: [^']*)' in S\['ferry'\]", base('tools/acts/b733.py'))
    r3 = AL.kept_clause(f3)
    n += 1
    g += case(L, 'needle', 'tools/acts/b733.py at BASE, the same string carried a third time against data/b733_ferry.txt', 'the hand string "%s" in the ferry: %s' % (m3.group(1), m3.group(1) in f3),
              'allow.kept_clause reads "%s" ; in the ferry: %s' % (r3, bool(r3) and r3 in f3), m3.group(1) not in f3, bool(r3) and r3 in f3)
    n += 1
    g += guard(L, 'needle', 'a ferry writing no such clause reads none, so the arm`s disjunct cannot pass on nothing', 'kept_clause on a sentence with no clause: %r' % AL.kept_clause('port-b707 kept; the rest deleted.'), AL.kept_clause('port-b707 kept; the rest deleted.') == '')
    return L, g, n


def note_text():
    src = rd('b732_phase2_frontdoors.txt').split(NL)
    i = next(i for i, l in enumerate(src) if l.startswith('## PART E -- THE 2C NOTE'))
    k = next(j for j in range(i, len(src)) if src[j].startswith('    DRAFT:   '))
    old = src[k][len('    DRAFT:   '):]
    if old.count(NOTE_OLD) != 1:
        sys.exit('### THE NOTE`S SENTENCE NOT READ ONCE -- NOTHING WRITTEN')
    return k + 1, old, old.replace(NOTE_OLD, NOTE_NEW)


def control_note():
    L, g, n = ['### (note) THE 2C NOTE`S WORDS AMENDED AS THE AUTHOR`S ROW (6) RULED, (R343)(2)(iv); THE INSTANCE, THE DRAFT AT data/b732_phase2_frontdoors.txt'], 0, 0
    ln, old, new = note_text()
    bank = rd('b733_2c_note.txt')
    n += 1
    g += case(L, 'note', 'the draft at data/b732_phase2_frontdoors.txt :%d, against the words "the five fields instancing two kinds and the C2 certificates the third"' % ln, 'the words in the rooted draft: %s' % ('the five fields instancing two kinds' in old),
              'the words in data/b733_2c_note.txt: %s' % ('the five fields instancing two kinds and the C2 certificates the third' in bank), 'the five fields instancing two kinds' not in old, 'the five fields instancing two kinds and the C2 certificates the third' in bank and new in bank)
    a, b = old.split(NOTE_OLD)
    n += 1
    g += guard(L, 'note', 'the amendment moves that sentence and nothing else; the rooted bank unedited since b732`s close', 'the rest byte-equal: %s ; data/b732_phase2_frontdoors.txt at HEAD equal to %s: %s' % (new == a + NOTE_NEW + b, B732_CLOSE, base('data/b732_phase2_frontdoors.txt', 'HEAD') == base('data/b732_phase2_frontdoors.txt', B732_CLOSE)),
               new == a + NOTE_NEW + b and base('data/b732_phase2_frontdoors.txt', 'HEAD') == base('data/b732_phase2_frontdoors.txt', B732_CLOSE))
    return L, g, n


def control_orcid():
    L, g, n = ['### (orcid) THE SCAN`S THIRD TARGET HELD IN MEMORY, (R343)(2)(v); THE INSTANCE, A PLANTED STRING IN MEMORY; THE VALUE NEVER PRINTED'], 0, 0
    act = A.current().get('act')
    SC = __import__('%s_address_scan' % act)
    o = SC.author_orcid()
    planted = 'x %s y' % o
    old_src = base('tools/b732_address_scan.py')
    n += 1
    g += case(L, 'orcid', 'a string built in memory carrying the value once, dropped after the count', 'tools/b732_address_scan.py has no third target (a form for it in the file: %s), so the planted string counted 0 at every arm' % ('ORCID_FORM' in old_src),
              'the arm counts %d' % SC.count(planted, o), 'ORCID_FORM' not in old_src, SC.count(planted, o) == 1)
    kinds = ('commit fields', 'commit message', 'commit added lines', 'working tree added lines', 'untracked bank')
    n += 1
    g += guard(L, 'orcid', 'excepted in a paper`s byline under I-23 and nowhere else', 'the byline kind excepts it: %s ; the other kinds excepting it: %s' % (SC.excepted(SC.BYLINE_KIND, 0, 0, 0, 1), [k for k in kinds if SC.excepted(k, 0, 0, 0, 1)] or 'NONE'),
               SC.excepted(SC.BYLINE_KIND, 0, 0, 0, 1) and not any(SC.excepted(k, 0, 0, 0, 1) for k in kinds))
    del o, planted
    return L, g, n


def old_hook():
    m = types.ModuleType('hook_base')
    m.__file__ = os.path.join(S, 'hook.py')
    exec(compile(base('tools/standing/hook.py'), 'hook.py@%s' % BASE, 'exec'), m.__dict__)
    return m


def scratch_relay(act, sealed_, rule_src=None):
    d = tempfile.mkdtemp(prefix='standing-v1130-hook-')
    os.makedirs(os.path.join(d, 'data'))
    os.makedirs(os.path.join(d, 'tools'))
    with open(os.path.join(d, 'data', 'act_current.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'act': act}) + NL)
    if sealed_:
        with open(os.path.join(d, 'data', '%s_seal_hashes.json' % act), 'w', encoding='utf-8', newline='\n') as f:
            f.write('{}' + NL)
    if rule_src is None:
        shutil.copy(os.path.join(T, 'rule_arms.py'), os.path.join(d, 'tools', 'rule_arms.py'))
    else:
        with open(os.path.join(d, 'tools', 'rule_arms.py'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(rule_src)
    return d


def control_postseal():
    L, g, n = ['### (postseal) THE POST-SEAL READ RULE`S LISTS READ BY THE HOOK, (R343)(2)(vi), b732 event (11); THE INSTANCE, b732`S TWO COMMANDS ON REPLAY, JUDGED, NOT RUN'], 0, 0
    O = old_hook()
    sealed_, open_ = scratch_relay('b732', True), scratch_relay('b732', False)
    rule = HK.ledger_rule(sealed_)
    L.append('  (postseal) the rule as the hook read it from tools/rule_arms.py: ledger names %s ; exclude list %s' % (list(rule[0]), rule[1]))
    for at, cmd in POSTSEAL_CMDS:
        old, new = O.judge('Bash', {'command': cmd}, sealed_), HK.judge('Bash', {'command': cmd}, sealed_)
        n += 1
        g += case(L, 'postseal', '%s: %s' % (at, cmd), 'the hook at BASE: %s, allowed; the arm counted it after it ran' % (old,), 'the hook, the seal recorded: %s' % (new[0] if new else new,), old is None, bool(new) and new[0] == 'POSTSEAL')
    n += 1
    g += guard(L, 'postseal', 'before the seal the same two pass', 'refused %s' % [HK.judge('Bash', {'command': c}, open_) for _a, c in POSTSEAL_CMDS], not any(HK.judge('Bash', {'command': c}, open_) for _a, c in POSTSEAL_CMDS))
    fine = ['git -C /d/relay log --oneline -3 -- FINDINGS.md', 'git -C /d/relay add FINDINGS.md', 'python -X utf8 -u tools/b732_record.py sort FINDINGS.md']
    n += 1
    g += guard(L, 'postseal', 'after the seal the commands the arm does not count pass: no filter, and the exclude list: %s' % fine, 'refused %s' % [c for c in fine if HK.judge('Bash', {'command': c}, sealed_)] , not any(HK.judge('Bash', {'command': c}, sealed_) for c in fine))
    src = open(os.path.join(T, 'rule_arms.py'), encoding='utf-8').read()
    moved = src.replace("LEDGER_READ = ('FINDINGS.md',", "LEDGER_READ = ('PLANTED.md', 'FINDINGS.md',", 1)
    d2 = scratch_relay('b732', True, moved)
    v = HK.judge('Bash', {'command': 'wc -l PLANTED.md'}, d2)
    n += 1
    g += guard(L, 'postseal', 'the list is the arm`s, not the hook`s: a name added to tools/rule_arms.py alone, in a scratch copy, is refused with no hook edit', 'wc -l of the planted name: %s' % (v[0] if v else v,), bool(v) and v[0] == 'POSTSEAL')
    n += 1
    g += guard(L, 'postseal', 'the live relay is not sealed at this control, so the hook passes the same commands now', 'sealed(RELAY) %s' % HK.sealed(), not HK.sealed())
    return L, g, n


def old_substitute():
    src = base('tools/standing/carry.py')
    m = re.search(r'(?ms)^def substitute\(text, subs\):.*?^    return out$', src)
    ns = {}
    exec(m.group(0), ns)
    return ns['substitute']


def control_carry():
    L, g, n = ['### (carry) THE RUNS-OF-THREE ROW b730 (m), b731 (b), b732 (c), THE SHIFT OF A KEPT BRANCH, (R343)(2)(vii); THE INSTANCE, THE zq-b730 SHIFT'], 0, 0
    subs = [('b732', 'b733'), ('b731', 'b732'), ('b730', 'b731')]
    line = "SITTING_REPOS = (('D:/SIDE-explicit-formula', 'SIDE-explicit-formula zq-b730', 'main..zq-b730'),)"
    old_sub = old_substitute()
    o, nw = old_sub(line, subs), CR.substitute(line, subs)
    n += 1
    g += case(L, 'carry', 'the scan`s SITTING_REPOS line through the three pairs', 'the plain replace: %s' % o, 'the standing route: %s' % nw, 'zq-b731' in o, nw == line)
    t2 = 'kept: c2-b725, keiper-b725, detect-b729, zq-b730; b732_stepzero and push-b732-closing'
    want = 'kept: c2-b725, keiper-b725, detect-b729, zq-b730; b733_stepzero and push-b733-closing'
    n += 1
    g += guard(L, 'carry', 'the shift still moves what the act moves: the act`s banks and its push branches', '%s' % CR.substitute(t2, [('b732', 'b733')]), CR.substitute(t2, [('b732', 'b733')]) == want)
    t3 = 'pin-b718-de5ce8a9 rebuild-b721 port-b707 scratch-b724 corrigendum-b723 challenge-b720-h2 x-b721'
    n += 1
    g += guard(L, 'carry', 'the kept forms the step-zero list banks, each held; a name of no kept form still shifts', CR.substitute(t3, [('b721', 'b722'), ('b718', 'b719'), ('b707', 'b708')]),
               CR.substitute(t3, [('b721', 'b722'), ('b718', 'b719'), ('b707', 'b708')]) == t3.replace('x-b721', 'x-b722'))
    src = open(os.path.join(T, 'b733_carry.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'carry', 'the act`s carry tool goes through the standing route, not a copy of the loop', 'CR.substitute in tools/b733_carry.py: %s' % ('CR.substitute(text, SUBS)' in src), 'CR.substitute(text, SUBS)' in src)
    return L, g, n


CONTROLS = dict(prelock=control_prelock, rows=control_rows, needle=control_needle, note=control_note, orcid=control_orcid, postseal=control_postseal, carry=control_carry)
ORDER = ('prelock', 'rows', 'needle', 'note', 'orcid', 'postseal', 'carry')


def write_note(act):
    ln, old, new = note_text()
    L = ['%s -- THE 2C NOTE, ITS WORDS AMENDED AS THE AUTHOR`S ROW (6) RULED, (R343)(2)(iv), BEFORE ANY EDITION READS IT; APPLIED NOWHERE (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### THE SOURCE: data/b732_phase2_frontdoors.txt :%d, PART E, item [111], rooted at b732 and unedited. THE ROW: data/b732_author_words.txt, row (6): the note keeps three kinds, the C2 certificates the instance of the second, the five fields instancing the other two.' % ln,
         '### THE ONE SENTENCE MOVED, BY tools/standing/v1130.py note: "%s" -> "%s". Every other byte of the draft stands.' % (NOTE_OLD, NOTE_NEW),
         '### ITS FIGURES ARE b732`S, AS OF THAT DRAFT. The count field`s row in it reads "open and not touched" and stands so here; the sitting that places the note reads that row against this act`s grade.', '',
         'AMENDED DRAFT:', new, '']
    p = os.path.join(D, '%s_2c_note.txt' % act)
    with open(p + '.tmp', 'wb') as f:
        f.write(NL.join(L).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/%s_2c_note.txt' % act)


def main(argv):
    if argv[:1] == ['note']:
        return write_note(A.current().get('act'))
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.13.0, (R343)(2)(i)-(viii): THE PRE-LOCK COMPARISON, free_mb IN EVERY ROW KIND, THE NEEDLE FROM THE FERRY, THE 2C NOTE, THE ORCID, THE POST-SEAL RULE IN THE HOOK, THE KEPT BRANCH IN THE CARRY (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.13.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1130.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1130.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
