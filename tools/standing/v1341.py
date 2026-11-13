# -*- coding: utf-8 -*-
"""standing/v1341.py -- THE CONTROLS OF v1.34.1 (b754 amendment row 4 (2) and (3), data/b754_amendments.json), in v1340.py's form: each
instance read through the route as it stood at BASE (relay 5d671461, v1.34.0's own commit, read from its blobs) and through the repaired
route on disk; AS WANTED where the old route fails the instance and the new passes it; a GUARD where no old route can fail. THE COMPILE
CONTROL RUNS FIRST. The free memory is printed before each control. The planted chain stands in a folder made under the state folder on the
data volume and removed by its own absolute path after the control; no write reaches the relay or PLACE-papers. Written at b754 by the Write
tool; no identifier of the author is read into any string here.

  (sessions)  row 4 (2): the close's reads (tools/standing/v1330.py :149, :220; tools/standing/append.py :46) take the act's sessions in chain
              order -- the session the ruling was delivered in, from the delivery's line, then each session after it -- and not one session's
              id. A planted chain of three sessions with one row in each, all three read; the live chain of b754 printed.
  (seatrule)  row 4 (3): the seat file's rule line reads the two clauses the ruling gives, (3)(i) for the file and N5 for what the act writes.
  (version)   tools/standing/VERSION moved to v1.34.1.

  python -X utf8 -u tools/standing/v1341.py control [sessions|seatrule|version ...] [--bank]
"""
import io
import json
import os
import sys
import tempfile
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '5d671461'   # ### v1.34.0's own commit (b754 component 1): the routes before this repair
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import statedir as SD           # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line, remove_tree)


def show(rel):
    return V.show(BASE, rel)


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.1): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.34.1): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'),
          '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _line(text, n):
    ls = (text or '').split(NL)
    return ls[n - 1] if 0 < n <= len(ls) else ''


# ================================================================================ (sessions) row 4 (2)
ANCHOR, TAIL = 'RULING (RX) BEGIN', 'FERRY END (part 1 of 1)'
PLANT = ('11111111-0000-4000-8000-000000000001', '22222222-0000-4000-8000-000000000002', '33333333-0000-4000-8000-000000000003')


def _plant(root):
    """three sessions with one row in each (the first a user text that is a delivery), a relay with act_current naming the second session as
    its one id, and a worklist naming the three in chain order; a settings file and a store folder for the store read."""
    proj, relay, store = (os.path.join(root, x) for x in ('proj', 'relay', 'store'))
    for p in (proj, store, os.path.join(relay, 'data'), os.path.join(relay, 'tools')):
        os.makedirs(p)
    rows = ({'type': 'user', 'uuid': 'u1', 'parentUuid': None, 'timestamp': '2026-01-01T00:00:01Z',
             'message': {'role': 'user', 'content': '%s\nthe planted ruling\n%s' % (ANCHOR, TAIL)}},
            {'type': 'user', 'uuid': 'u2', 'parentUuid': None, 'timestamp': '2026-01-02T00:00:01Z', 'message': {'role': 'user', 'content': 'a planted word'}},
            {'type': 'assistant', 'uuid': 'u3', 'parentUuid': None, 'timestamp': '2026-01-03T00:00:01Z', 'message': {'role': 'assistant', 'content': []}})
    for sid, o in zip(PLANT, rows):
        with open(os.path.join(proj, sid + '.jsonl'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(json.dumps(o) + NL)
    with open(os.path.join(relay, 'data', 'act_current.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(dict(act='b999', anchor=ANCHOR, tail=TAIL, session=PLANT[1], prev_session=PLANT[0])))
    with open(os.path.join(relay, 'tools', 'b999_worklist.py'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write("SESSION_ID = '%s'\nSESSIONS_AFTER = (('%s', 'a planted word'), ('%s', 'x'))\n" % PLANT)
    settings = os.path.join(root, 'settings.json')
    with open(settings, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(dict(cleanupPeriodDays=3650)))
    return proj, relay, store, settings


def control_sessions():
    L, g, n = ['### (sessions) b754 AMENDMENT ROW 4 (2): THE CLOSE`S READS TAKE THE ACT`S SESSIONS IN CHAIN ORDER'], 0, 0
    import chain as CH
    v_old, a_old = show('tools/standing/v1330.py') or '', show('tools/standing/append.py') or ''
    v_new = io.open(os.path.join(S, 'v1330.py'), encoding='utf-8').read().replace('\r', '')
    a_new = io.open(os.path.join(S, 'append.py'), encoding='utf-8').read().replace('\r', '')
    sc = os.path.abspath(SD.STATE)
    root = os.path.abspath(tempfile.mkdtemp(prefix='v1341_', dir=sc))
    try:
        proj, relay, store, settings = _plant(root)
        cur = json.load(io.open(os.path.join(relay, 'data', 'act_current.json'), encoding='utf-8'))
        # the route before: act_current's one session id, as v1330.py :149 and append.py :46 read it at BASE
        one = [cur['session']]
        old_rows = [CH.chain(CH.path_of(s, proj))['rows'] for s in one]
        ss = CH.act_sessions(relay=relay, proj=proj)
        new_rows = [CH.chain(CH.path_of(s, proj))['rows'] for s, _at in ss]
        n += 1
        g += case(L, 'sessions', 'a planted chain of three sessions with one row in each, the first holding the delivery (v1330.py :149, append.py :46)',
                  'act_current`s one id: %d of 3 read (%s), rows %s' % (len(one), ', '.join(s[:8] for s in one), old_rows),
                  'the chain: %d of 3 read (%s), rows %s' % (len(ss), ', '.join('%s from :%d' % (s[:8], a) for s, a in ss), new_rows),
                  len(one) != 3, [s for s, _a in ss] == list(PLANT) and new_rows == [1, 1, 1] and ss[0][1] == 1)
        ok_o, lo = CH.store_read(cur['session'], cur['prev_session'], proj=proj, store=store, settings=settings)
        ok_n, ln = CH.store_reads(ss, cur['prev_session'], proj=proj, store=store, settings=settings)
        named = [s[:8] for s in PLANT if any(('session %s by both paths' % s[:8]) in x for x in ln)]
        n += 1
        g += case(L, 'sessions', 'the store read over the planted chain (v1330.py :220): every session read by both paths',
                  'store_read of the one id: %d session line(s)' % len(lo), 'store_reads: %d session line(s), the sessions named %s' % (len(ln) - 1, named),
                  len(lo) != 3, len(ln) == 4 and named == [s[:8] for s in PLANT])
        nod = os.path.join(relay, 'tools', 'b998_worklist.py')
        with open(nod, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write("SESSIONS_AFTER = ()\n")
        try:
            CH.act_sessions(act='b998', relay=relay, proj=proj)
            refused = 'READ'
        except SystemExit as e:
            refused = str(e)[:90]
        n += 1
        g += guard(L, 'sessions', 'a planted worklist naming no SESSION_ID refuses the chain read', refused, refused.startswith('### NO SESSION_ID'))
    finally:
        if os.path.commonpath([sc, root]) == sc and os.path.basename(root).startswith('v1341_') and root != sc:
            V.remove_tree(root)
    gone = not os.path.exists(root)
    n += 1
    g += guard(L, 'sessions', 'the planted folder removed by its own absolute path', 'removed %s' % gone, gone)
    # the three places, at BASE and on disk, read by their lines (the author cites :149 and :220 of v1330.py and :46 of append.py)
    o149, o220, n149, n220 = _line(v_old, 149), _line(v_old, 220), _line(v_new, 149), _line(v_new, 220)
    n += 1
    g += case(L, 'sessions', 'tools/standing/v1330.py :149 and :220 at BASE and on disk',
              ':149 %r ; :220 %r' % (o149.strip()[:70], o220.strip()[:80]), ':149 %r ; :220 %r' % (n149.strip()[:60], n220.strip()[:70]),
              "get('session')" in o149 and "cur.get('session')" in o220,
              'CH.act_sessions()' in n149 and 'CH.store_reads(CH.act_sessions(' in n220)
    n += 1
    g += case(L, 'sessions', 'tools/standing/append.py: the chain read beside the bank', ':46 %r' % _line(a_old, 46).strip()[:70],
              'CHN.act_sessions() %s ; each session from its line %s' % ('CHN.act_sessions()' in a_new, "x[0] >= at" in a_new),
              "get('session')" in _line(a_old, 46), 'CHN.act_sessions()' in a_new and 'x[0] >= at' in a_new and 'CHN.chain' in a_new)
    # the live chain of this act
    live = CH.act_sessions()
    act = A.current().get('act')
    wl = os.path.join(T, '%s_worklist.py' % act)
    k = CH._consts(io.open(wl, encoding='utf-8').read(), ('SESSION_ID', 'SESSIONS_AFTER'))
    want = [k['SESSION_ID']] + [s[0] for s in k['SESSIONS_AFTER']]
    n += 1
    g += guard(L, 'sessions', 'the live chain of %s, read from tools/%s_worklist.py and the delivery`s line' % (act, act),
               ', '.join('%s from :%d' % (s[:8], a) for s, a in live), [s for s, _a in live] == want and live[0][1] > 1 and all(a == 1 for _s, a in live[1:]))
    ok_l, ll = CH.store_reads(live, A.current().get('prev_session'))
    L += ['      ' + x[:400] for x in ll]
    n += 1
    g += guard(L, 'sessions', 'the store read over the live chain, each session by both paths at one size', 'ok %s over %d session(s)' % (ok_l, len(live)), ok_l)
    return L, g, n


# ================================================================================ (seatrule) row 4 (3)
OLD_RULE = '- no identifier of the author, and no path under the user`s profile, in anything the act writes'


def control_seatrule():
    L, g, n = ['### (seatrule) b754 AMENDMENT ROW 4 (3): THE SEAT FILE`S RULE LINE READS (3)(i) FOR THE FILE AND N5 FOR WHAT THE ACT WRITES'], 0, 0
    import seatfile as SF
    old_src = show('tools/standing/seatfile.py') or ''
    new = SF.compose()
    i = next((k for k, x in enumerate(new) if x.startswith('- in this file ((R364)(3)(i))')), None)
    rule = new[i:i + 3] if i is not None else []
    n += 1
    g += case(L, 'seatrule', 'the seat file`s rule line on identifiers and paths',
              'at BASE the composer writes %r: %s' % (OLD_RULE[:60], 'PRESENT' if OLD_RULE in old_src else 'ABSENT'),
              'the composer writes %d line(s): (3)(i) %s ; N5 %s ; the old line %s' % (
                  len(rule), bool(rule), bool(rule) and 'N5' in rule[1], 'ABSENT' if OLD_RULE not in NL.join(new) else 'PRESENT'),
              OLD_RULE in old_src, len(rule) == 3 and 'user`s profile' in rule[0] and '(N5)' in rule[1] and 'own data' in rule[2] and OLD_RULE not in NL.join(new))
    ok, out = SF.control()
    n += 1
    g += guard(L, 'seatfile', 'seatfile.py control after the change: the arm, the copies, the plants', (out[-1] if out else '')[:200], ok)
    disks = [SF.body_of(SF.places()[i][1]) for i in SF.TARGETS]
    eq = [d is not None and d == NL.join(new) for d in disks]
    n += 1
    g += guard(L, 'seatrule', 'both written copies carry the composed block with the corrected line (seatfile.py write run before this bank)',
               'the copies equal to the composer: %s' % eq, len(eq) == 2 and all(eq))
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.0', ver == 'v1.34.1')
    return L, g, n


CONTROLS = dict(sessions=control_sessions, seatrule=control_seatrule, version=control_version)
ORDER = ('sessions', 'seatrule', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.1, b754 AMENDMENT ROW 4 (2) AND (3) (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.34.1: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1341.txt' % act), NL.join(out))
        print('written data/%s_standing_v1341.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
