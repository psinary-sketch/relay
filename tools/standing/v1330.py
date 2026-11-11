# -*- coding: utf-8 -*-
"""standing/v1330.py -- THE CONTROLS OF v1.33.0 ((R363)(7)(i)-(ix) and (R363)-amendment (1); b752 events (6)-(8), (13), defect (h'); b753
defect (i)), in v1320.py's form: each instance read through the route as it stood before the repair (tools/standing/ at BASE, b752's closing
relay head, read from its blobs) and through the repaired route on disk; AS WANTED where the old route fails the instance and the new passes
it. THE COMPILE CONTROL RUNS FIRST. The free memory is read and printed before each control. Written at b753 by the Write tool; no identifier
of the author is read into any string here (the outbound control reads b698's label tuple from its sealed source).

  python -X utf8 -u tools/standing/v1330.py control [gitwrite|subject|outbound|chain|halt|hold|absent|remote|version ...] [--bank]
"""
import importlib.util
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
BASE = '0e855242'   # ### b752's closing relay head (PRE_RELAY of b753): the routes before this repair
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def show(ref, rel):
    r = _git('show', '%s:%s' % (ref, rel))
    return r.stdout.replace('\r', '') if r.returncode == 0 else None


def old(rel, name):
    """tools/standing/<rel> as BASE left it, loaded from its blob under another name; None where BASE has no such file."""
    src = show(BASE, 'tools/standing/' + rel)
    if src is None:
        return None
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, name + '.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    shutil.rmtree(d, ignore_errors=True)
    return m


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.32.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.33.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.33.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _absent_at_base(rel):
    return show(BASE, 'tools/standing/' + rel) is None


# ================================================================================ (gitwrite) (R363)-amendment (1), b753 defect (i)
def control_gitwrite():
    L, g, n = ['### (gitwrite) (R363)-amendment (1), b753 DEFECT (i): THE ONE-CALL CHECK READS A POWERSHELL-FORM RUN OF THE TOOL (relay ba46416f); '
               'its live form entered at b753 events (2)'], 0, 0
    import commit as C
    import gitwrite as NEW
    OLD = types.ModuleType('gitwrite_base')
    OLD.__file__ = NEW.__file__
    exec(compile(show(BASE, 'tools/standing/gitwrite.py'), 'BASE:gitwrite.py', 'exec'), OLD.__dict__)
    cmd = '& "C:\\Users\\x\\python.exe" -X utf8 -u tools/standing/commit.py relay add data/b753_events.txt'
    real = dict(request='2026-11-11T15:10:40.145Z', id='toolu_REAL', at='2026-11-11T15:10:50.624102Z', cmd=cmd, refused=None)
    plant = dict(real, id='toolu_PLANT', at='2026-11-11T15:10:50.900000Z', cmd='git -C D:/relay add data/b753_plant.txt')
    stale = dict(request='2026-11-11T07:47:13.149Z', id='toolu_STALE', at='2026-11-11T07:47:16.716087Z',
                 cmd='python -X utf8 -u tools/standing/commit.py relay add data/b752_steps.json', refused=None)
    led = [stale, plant, real]
    res = {}
    for nm, GW in (('old', OLD), ('new', NEW)):
        sys.modules['gitwrite'] = GW
        res[nm] = C.message_refusal(led, ['relay', 'add'], GW)
    sys.modules['gitwrite'] = NEW
    n += 1
    g += case(L, 'gitwrite', 'a PowerShell-form run of the tool with a planted bare git add in its message, a stale bare-python record in the ledger',
              res['old'][1], (res['new'][0] or '')[:100], res['old'][0] is None, bool(res['new'][0]))
    n += 1
    g += case(L, 'gitwrite', 'the run counted a write by the hook`s reading (gitwrite.writes)', len(OLD.writes(cmd)), len(NEW.writes(cmd)),
              len(OLD.writes(cmd)) == 0, len(NEW.writes(cmd)) == 1)
    return L, g, n


# ================================================================================ (subject) (7)(i)
def control_subject():
    L, g, n = ['### (subject) (R363)(7)(i): THE SUBJECT READ IN tools/standing/, ITS CONTROL THE FLOOR'], 0, 0
    import subject as SU
    ok, out = SU.control()
    n += 1
    g += case(L, 'subject', '(R362) replayed from cQ, negative, class group, b(n), c(n): the floor FINDINGS :10858, :11072, :11178, :11359, INSTRUMENTS :750, :758',
              'tools/standing/subject.py at BASE: %s' % ('ABSENT, no standing route' if _absent_at_base('subject.py') else 'present'), out[-1][:160],
              _absent_at_base('subject.py'), ok)
    _n, p = SU.pattern('head:class group=class')
    n += 1
    g += guard(L, 'subject', 'the head word `class` does not take `classes` (b753 defect (k))', 'classes matched %s' % bool(p.search('classes')), not p.search('classes'))
    return L, g, n


# ================================================================================ (outbound) (7)(ii)
def control_outbound():
    L, g, n = ['### (outbound) (R363)(7)(ii), b752 DEFECT (h`): THE OUTBOUND MATCHER READS AN IDENTIFIER BY ITS FORM'], 0, 0
    import outbound as OB
    ok, out = OB.control()
    n += 1
    g += case(L, 'outbound', 'b752`s three prompts (AN IDENTIFIER IN 0 wanted) and a planted prompt with a number of the ORCID`s form (1 wanted)',
              'b698`s label reading: 3 of 3', out[0][:200], 'AN IDENTIFIER IN 3 by the labels' in out[0], ok)
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'outbound', 'the record template rebinds b698`s R.outbound to the form reading', 'OUTB.rebind(R) in record.tpl %s' % ('OUTB.rebind(R)' in tpl), 'OUTB.rebind(R)' in tpl)
    return L, g, n


# ================================================================================ (chain) (7)(iii)
def control_chain():
    L, g, n = ['### (chain) (R363)(7)(iii), b752 EVENTS (6): THE ANSWERS ROUTE READS THE BLOB ROW; THE CHAIN READ'], 0, 0
    import chain as CH
    ok, out = CH.control(A.current().get('session'))
    b752 = io.open(os.path.join(D, 'b752_author_answers.txt'), encoding='utf-8').read()
    oldno = 'toolu_01A9s3DAsTnrvU9nRikRpgjB' in b752 and 'RESULT (transcript line None, None): ### NO RESULT' in b752
    n += 1
    g += case(L, 'chain', 'session 43048615 replayed: the nine lost rows; the root`s answer read from the blob row :11286, marked',
              'b752`s bank (route at BASE) for the call: NO RESULT %s' % oldno, out[-1][:180], oldno, ok)
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    ap = io.open(os.path.join(S, 'append.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'chain', 'the answers route (record.tpl) and the author-words route (append.py) print the chain count beside what they bank',
               'route_fill in record.tpl %s ; chain in append.py %s' % ('CHN.route_fill' in tpl, 'CHN.chain' in ap), 'CHN.route_fill' in tpl and 'CHN.chain' in ap)
    return L, g, n


# ================================================================================ (halt) (7)(iv)
def control_halt():
    L, g, n = ['### (halt) (R363)(7)(iv), b752 EVENTS (7), (8): A HALT PRICES FROM THE EXERCISE BANKS AND THE CAPS'], 0, 0
    import haltprice as HP
    ok, out = HP.control()
    n += 1
    g += case(L, 'halt', 'b752`s halt replayed: G-ANSWERS-BANKED in no part of 10; the root cap at its demand; a planted arm found',
              'tools/standing/haltprice.py at BASE: %s (b752 priced the routes at the arm, events (8))' % ('ABSENT' if _absent_at_base('haltprice.py') else 'present'),
              out[-1][:160], _absent_at_base('haltprice.py'), ok)
    return L, g, n


# ================================================================================ (hold) (7)(vii)
def control_hold():
    L, g, n = ['### (hold) (R363)(7)(vii): THE DISK HOLD AND THE RESTART READER'], 0, 0
    import hold as NEW
    OLD = old('hold.py', 'hold_v1320')
    try:
        o = OLD.refuses('a planted route', hold=0, free=10 ** 6, disks={'C:\\': 4000}, floor=5000)
        o_ = 'refused %s' % o
        ofail = not o
    except TypeError as e:
        o_, ofail = 'no disk reading (%s)' % str(e)[:80], True
    ok, out = NEW.control()
    n += 1
    g += case(L, 'hold', 'the system volume planted at 4,000 MB under a 5,000 MB floor, every route refusing; the restart reader given a planted answer',
              o_, out[0][:220], ofail, ok)
    return L, g, n


# ================================================================================ (absent) (7)(viii)
def _act_from(src, session):
    m = re.search(r'(?ms)^def act_from\(\):\n.*?(?=^\S)', src)
    ns = dict(os=os, io=io, sys=sys, SESSION=session)
    exec(m.group(0), ns)
    try:
        return 'returns %s' % ns['act_from'](), False
    except SystemExit as e:
        return str(e)[:120], str(e).startswith('### ABSENT')


def control_absent():
    L, g, n = ['### (absent) (R363)(7)(viii): A READER OPENING A TRANSCRIPT BY A SESSION`S ID PRINTS ABSENT; THE STORE READ AT STEP ZERO'], 0, 0
    planted = 'C:/Users/echo chamber/.claude/projects/D--/00000000-0000-0000-0000-000000000000.jsonl'
    o, oabs = _act_from(show(BASE, 'tools/standing/routes/b644_record.py'), planted)
    nw, nabs = _act_from(io.open(os.path.join(S, 'routes', 'b644_record.py'), encoding='utf-8').read(), planted)
    n += 1
    g += case(L, 'absent', 'act_from() of tools/standing/routes/b644_record.py given a planted id no file holds', o, nw, not oabs, nabs)
    import chain as CH
    try:
        CH.path_of('00000000-0000-0000-0000-000000000000')
        cab = False
    except SystemExit as e:
        cab = str(e).startswith('### ABSENT')
    n += 1
    g += guard(L, 'absent', 'the chain read and the answers fill open a session by its id through path_of, ABSENT on a planted id', 'ABSENT %s' % cab, cab)
    cur = A.current()
    ok, out = CH.store_read(cur.get('session'), cur.get('prev_session'))
    n += 1
    g += guard(L, 'absent', 'the store read: the retention, the junction, the transcript by both paths, the version beside the previous', out[0][:220], ok)
    return L, g, n


# ================================================================================ (remote) (7)(ix)
def control_remote():
    L, g, n = ['### (remote) (R363)(7)(ix), b752 EVENTS (13): A REMOTE READ THAT FAILS IS NOT AN EMPTY ANSWER'], 0, 0
    import remoteread as RR
    ok, out = RR.control()
    n += 1
    g += case(L, 'remote', 'ls-remote against a remote name that does not resolve: b698`s g() and the kept reader', 'b698`s g() returns \'\' (read as no head)', out[0][:200],
              "returns ''" in out[0], ok)
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'remote', 'the record template rebinds b698`s R.g to the kept reader', 'RREAD.rebind(R) in record.tpl %s' % ('RREAD.rebind(R)' in tpl), 'RREAD.rebind(R)' in tpl)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED AND ITS CONTROLS TALLIED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.32.0', ver == 'v1.33.0')
    return L, g, n


CONTROLS = dict(gitwrite=control_gitwrite, subject=control_subject, outbound=control_outbound, chain=control_chain, halt=control_halt,
                hold=control_hold, absent=control_absent, remote=control_remote, version=control_version)
ORDER = ('gitwrite', 'subject', 'outbound', 'chain', 'halt', 'hold', 'absent', 'remote', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.33.0, (R363)(7)(i)-(ix) AND (R363)-amendment (1): THE ONE-CALL CHECK, THE SUBJECT READ, THE OUTBOUND '
           'MATCHER BY FORM, THE BLOB ANSWER AND THE CHAIN READ, THE HALT`S PRICE, THE DISK HOLD, THE ABSENT INPUT, THE FAILED REMOTE READ, THE VERSION (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py ; (7)(v) and (7)(vi) carry no code: the close`s count follows [H1]`s answer, the seat`s repeats '
           'stand in its corrigendum', '',
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
    out.append('### ### **v1.33.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1330.txt' % act), NL.join(out))
        print('written data/%s_standing_v1330.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
