# -*- coding: utf-8 -*-
"""standing/v1320.py -- THE CONTROLS OF v1.32.0 ((R362)(7)(i)-(xi); b751 events (1)-(5), defects (a)-(v)), in v1310.py's form: each instance read
through the route as it stood before the repair (tools/standing/ at BASE, b751's closing relay head, read from its blobs) and through the repaired
route on disk; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL
RUNS FIRST. The free memory is read and printed before each control. Written at b752 by the Write tool; no identifier of the author is read into
any string here.

  python -X utf8 -u tools/standing/v1320.py control [paths|recall|currents|append|orders|carry|flag|limit|cites|instances|session|version ...] [--bank]
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

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = 'd921bceb'   # ### b751's closing relay head (PRE_RELAY of b752): the routes before this repair
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
TX = 'C:/Users/echo chamber/.claude/projects/D--'
S751A, S751B = '6151c0de-d2ec-42cf-a477-c48b99346e01', '43048615-75cd-4480-bfa6-362a3c13092b'
A751A, A751B = 'RULING (R361) BEGIN', 'Go: read free memory in the foreground; at or above 2,750 MB, proceed in the order you listed'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import authorwords as AW        # noqa: E402
import carry as CA              # noqa: E402
import cites as CI              # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import limits as LI             # noqa: E402
import orders as OR             # noqa: E402
import refused as RFC           # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def rdf(rel, root=RELAY):
    p = os.path.join(root, rel)
    return io.open(p, encoding='utf-8').read().replace('\r', '') if os.path.isfile(p) else ''


def old(rel, name, under='tools/standing/'):
    """<under><rel> as BASE left it, loaded from its blob under another name."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, name + '.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(show(BASE, under + rel))
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
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.31.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.32.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.32.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _row(rel, k):
    """the lettered or numbered row (k) of a b751 bank, stripped; '' where absent."""
    return next((l.strip() for l in rdf(rel).split(NL) if l.strip().startswith('(%s) ' % k)), '')


# ================================================================================ (paths) (7)(i): EVERY PATH THE RULING AND THE FERRY NAME
def control_paths():
    L, g, n = ['### (paths) (R362)(7)(i), b751 defect (e), REPEAT b750 (f): THE CITATION CHECK READS EVERY PATH THE RULING AND THE FERRY NAME AT HEAD: OK, NONE, OR THE ACT`S OWN TO BE WRITTEN'], 0, 0
    OCI = old('cites.py', 'cites_v1310')
    act = A.current()['act']
    t752, t751 = rdf('data/%s_ferry.txt' % act), rdf('data/b751_ferry.txt')
    # ### b751's instance: the four relay banks its ferry named that did not exist (defect (e)), read by the new route over b751's ferry at HEAD
    fp = CI.ferry_paths(t751, 'b751', RELAY, PP)
    none = [p for p, _r, s in fp if s == 'NONE']
    want = ('data/b738_sp1.txt', 'data/b740_s5.txt', 'data/b741_c7.txt', 'data/b743_discharge.txt')
    n += 1
    g += case(L, 'paths', 'b751`s ferry: the four read-first banks that do not exist (defect (e)) printed NONE by the check itself',
              'cites.py at %s: ferry_paths %s; the absences found by the seat`s reading of the readfirst rows' % (BASE, 'present' if hasattr(OCI, 'ferry_paths') else 'absent'),
              'paths %d ; NONE %d %s' % (len(fp), len(none), none), not hasattr(OCI, 'ferry_paths'), all(w in none for w in want))
    f2 = CI.ferry_paths(t752, act, RELAY, PP)
    n += 1
    g += guard(L, 'paths', '%s`s ferry at HEAD: NONE 0, the next act`s rules named by form in the (W) list read as the act`s own' % act,
               'paths %d ; OK %d ; NONE %d ; OWN %d' % (len(f2), sum(s == 'OK' for _p, _r, s in f2), sum(s == 'NONE' for _p, _r, s in f2), sum(s.startswith('THE ACT') for _p, _r, s in f2)),
               not any(s == 'NONE' for _p, _r, s in f2) and any(p == 'data/b753_rules.txt' and s.startswith('THE ACT') for p, _r, s in f2))
    pl = CI.ferry_paths(t752 + ' data/b999_planted_absent.txt day1/Planted_Absent_v0.md', act, RELAY, PP)
    n += 1
    g += guard(L, 'paths', 'a planted relay path and a planted PLACE-papers path that stand nowhere: each NONE', [x for x in pl if 'lanted' in x[0]],
               sum(1 for p, _r, s in pl if 'lanted' in p and s == 'NONE') == 2)
    return L, g, n


# ================================================================================ (recall) (7)(ii): A CALL THE HOOK REFUSED
def control_recall():
    L, g, n = ['### (recall) (R362)(7)(ii), b751 events (1), defect (v): A CALL THE HOOK REFUSED BEFORE IT RAN IS NO REMOTE READ; G-RULE-REMOTE-REREAD COUNTS IT APART AND PRINTS IT'], 0, 0
    import rule_arms as RA
    ORA = old('rule_arms.py', 'rule_arms_v1310', under='tools/')
    s2 = '%s/%s.jsonl' % (TX, S751B)
    cut = next((json.loads(l).get('timestamp') for l in io.open(s2, encoding='utf-8', errors='replace')
                if 'RULING (R362) BEGIN' in l and json.loads(l).get('type') == 'user' and not json.loads(l).get('isCompactSummary')), None)
    calls = [c for c in RA.transcript('%s/%s.jsonl' % (TX, S751A), A751A) + RA.transcript(s2, A751B) if cut is None or c['ts'] < cut]
    R = dict(calls=calls, n=751, act='b751')
    o, nw = ORA.reading('G-RULE-REMOTE-REREAD', R), RFC.reading(RA, R)
    n += 1
    g += case(L, 'recall', 'b751`s calls (two sessions, cut at (R362)`s first line): the PowerShell command of 17:54:13.904Z carrying three ls-remote reads, refused by the hook',
              'rule_arms at %s: %s' % (BASE, str(o)[:150]), str(nw)[:200], not o[0], bool(nw[0]) and '17:54:1' in str(nw))
    pl = dict(R, calls=calls + [dict(mid='p', tid='p1', ts='2026-11-10T23:59:59Z', cmd='git ls-remote a && git ls-remote b', out='')])
    pn = RFC.reading(RA, pl)
    n += 1
    g += guard(L, 'recall', 'a planted command carrying two remote reads that RAN (no refusal in its output): still failing', str(pn)[:160], not pn[0])
    return L, g, n


# ================================================================================ (currents) (7)(iii): G-CURRENTS-UNEDITED ON THE PREVIOUS ACT'S BANKS
def control_currents():
    L, g, n = ['### (currents) (R362)(7)(iii), b751 events (3): A `--prev` RUN EXCLUDES THE FILES BOTH ACTS WROTE ON MAIN; THE DETAIL LINE NAMES THE READ, THE EXCLUDED AND THE SIDE THAT DIFFERS'], 0, 0
    import fold as F
    import b703_checks as C3
    act = A.current()['act']
    otpl, ntpl = show(BASE, 'tools/standing/fold/checks.tpl'), io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    secs, ovs = F._parse(act)
    txt = F.render(act, 'checks', secs=secs, ovs=ovs)
    m = re.search(r'(?ms)^def currents_for\(\*ks\):.*?(?=^\S)', txt)
    ns = dict(C3=C3, _renamed=lambda: dict((r['versioned'], r['unversioned']) for r in (json.loads(rdf('data/b706_partners.json') or '{}').get('rows') or [])
                                             if r.get('versioned') and r.get('unversioned')))
    exec(m.group(0), ns) if m else None
    sys.path.insert(0, T)
    K750, K751 = importlib.import_module('b750_worklist'), importlib.import_module('b751_worklist')
    sitting = sorted(set(K750.PP_EDITED) & set(C3.CURRENTS) - set(K751.PP_EDITED))
    old_read = [p for p in C3.CURRENTS if p not in K751.PP_EDITED]      # ### v1.31.0: computed at import from the running act's list alone
    cur, ex = ns['currents_for'](K750, K751) if 'currents_for' in ns else ((), {})
    n += 1
    g += case(L, 'currents', 'b751`s `--prev` run of standing-a2 on b750`s banks (data/b751_prevrun_standing-a2.txt :70): b750`s sitting writes on main %s' % sitting,
              'checks.tpl at %s (currents_for %s): read %d, b750`s writes read as edits %s' % (BASE, 'present' if 'def currents_for' in otpl else 'absent', len(old_read), [p for p in sitting if p in old_read]),
              'read %d, excluded %s' % (len(cur), dict((k, len(v)) for k, v in ex.items())), 'def currents_for' not in otpl and bool(sitting) and all(p in old_read for p in sitting),
              bool(sitting) and not any(p in cur for p in sitting))
    n += 1
    g += guard(L, 'currents', 'the act`s rendered suite: _prev_rebind recomputes the list from both acts, the detail line recorded, and it compiles',
               'currents_for(K707, KS) %s ; currents_detail %s' % ('currents_for(K707, KS)' in txt, 'def currents_detail' in txt),
               'currents_for(K707, KS)' in txt and 'def currents_detail' in txt and 'currents_for' in ntpl and bool(compile(txt, 'checks', 'exec')))
    return L, g, n


# ================================================================================ (append) (7)(iv): THE ANSWERS APPEND
def control_append():
    L, g, n = ['### (append) (R362)(7)(iv), b751 events (4), defect (m): THE AUTHOR`S WORDS KEYED BY PLACE, NOT TEXT; A NEW HEADING`S BLOCK APPENDED WHOLE; THE DRY PRINTS THE LINES'], 0, 0
    OA = old('act.py', 'act_v1310')
    cut = '2026-11-10T19:44:00Z'   # ### b751's answers route ran at 19:44:05Z

    def rows():
        for sid, anc in ((S751A, A751A), (S751B, A751B)):
            start = None
            for i, raw in enumerate(io.open('%s/%s.jsonl' % (TX, sid), encoding='utf-8', errors='replace'), 1):
                try:
                    o = json.loads(raw)
                except ValueError:
                    continue
                if (o.get('timestamp') or '') > cut:
                    break
                if start is None and anc in raw.replace('\u2019', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                    start = i
                if start is not None:
                    yield i, o, start, sid
    ws = AW.author_words(list(rows()), S751A, A751A)
    seen, by_text = set(), []
    for ln, w, _ts in ws:
        if w not in seen:
            seen.add(w)
            by_text.append(ln)
    n += 1
    g += case(L, 'append', 'b751`s author words over both sessions: the second identical go word (43048615, 16:47:23.712Z)',
              'by text (b698`s set): %d words' % len(by_text), 'by place: %d words %s' % (len(ws), [(ln, ts) for ln, _w, ts in ws][-2:]),
              len(by_text) < len(ws), any((ts or '').startswith('2026-11-10T16:47:23') for _ln, _w, ts in ws))
    prior = rdf('data/b751_author_answers.txt')
    comp = ['### b751 -- THE AUTHOR`S ANSWERS (the control`s composition)', '']
    for ln, w, _ts in [x for x in ws if x[0] in by_text]:
        comp += [AW.HEAD % ln] + w.split(NL) + ['']
    comp2, restored = AW.rekey(comp, ws)
    go = next((w for _ln, w, ts in ws if (ts or '').startswith('2026-11-10T16:47:23')), None)
    to, no = OA.answers_append(prior, comp2, 'T')
    tn, nn = A.answers_append(prior, comp2, 'T')
    n += 1
    g += case(L, 'append', 'the re-keyed block appended to b751`s answers bank: rows of the go word', 'act.py at %s: appended %d, the go word %d time(s)' % (BASE, no, to.count(go or '\0')),
              'appended %d, the go word %d time(s) ; restored %s' % (nn, tn.count(go or '\0'), restored), tn.count(go or '\0') > to.count(go or '\0'), tn.count(go or '\0') >= 2)
    t2, n2 = A.answers_append(tn, comp2, 'T2')
    n += 1
    g += guard(L, 'append', 'the append re-run over its own output: appends 0, the bank unchanged', 'appended %d ; equal %s' % (n2, t2 == tn), n2 == 0 and t2 == tn)
    rec = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'append', 'record.tpl`s answers route re-keys by place and prints the added lines', 'AW.author_words %s ; AW.rekey %s' % ('AW.author_words(' in rec, 'AW.rekey(' in rec),
               'AW.author_words(' in rec and 'AW.rekey(' in rec)
    return L, g, n


# ================================================================================ (orders) (7)(v): A ROW ID READ AS AN ORDER
def control_orders():
    L, g, n = ['### (orders) (R362)(7)(v): A TOKEN OF A ROW ID`S FORM (W-ORD-<digits>) READ AS NO ORDER, ITS MENTIONS PRINTED BESIDE; THE SEAT`S NARROWER READING, CARRIED TO THE AUTHOR'], 0, 0
    OO = old('orders.py', 'orders_v1310')
    lines = OR.trail('HEAD')
    o, nw = OO.read(lines), OR.read(lines)
    oo, no = [k for k, _v in o], [k for k, _v in nw]
    op = lambda R: sum(1 for _k, v in R if v['status'] == 'OPEN')   # noqa: E731
    rid = OR.rowid_mentions(lines)
    n += 1
    g += case(L, 'orders', 'the trail at PLACE-papers HEAD: W-ORD-1 (b751`s open-orders line, OPEN_TRAILS :18144)', 'orders.py at %s: %d orders, %d open, W-ORD-1 %s' % (BASE, len(oo), op(o), 'AN ORDER' if 'W-ORD-1' in oo else 'absent'),
              '%d orders, %d open, W-ORD-1 %s ; printed beside %s' % (len(no), op(nw), 'AN ORDER' if 'W-ORD-1' in no else 'no order', dict((k, v[:6]) for k, v in rid.items())),
              'W-ORD-1' in oo, 'W-ORD-1' not in no and 'W-ORD-1' in rid)
    n += 1
    g += guard(L, 'orders', 'the change is the row-ID token alone: every other order and its status as before', 'differing %s' % ([k for k in set(oo) ^ set(no)]),
               set(oo) ^ set(no) == {'W-ORD-1'} and all(dict(o)[k]['status'] == dict(nw)[k]['status'] for k in no))
    n += 1
    g += guard(L, 'orders', 'W-ORD-MECHANISM-ATTRIBUTION, the order this act plans, still an order and OPEN', dict(nw).get('W-ORD-MECHANISM-ATTRIBUTION', {}).get('status'),
               dict(nw).get('W-ORD-MECHANISM-ATTRIBUTION', {}).get('status') == 'OPEN')
    return L, g, n


# ================================================================================ (carry) (7)(vi): THE ROWS R1-R6 DID NOT READ
def control_carry():
    L, g, n = ['### (carry) (R362)(7)(vi), b751 defects (b), (q), REPEAT: THE CARRY READS EVERY ACT ORDINAL AND READ-FIRST NEEDLE BESIDE THE RULING (R7)'], 0, 0
    OCA = old('carry.py', 'carry_v1310')
    act = A.current()['act']
    subs = (('b751', 'b752'), ('b750', 'b751'))
    prev, pwl = show(BASE, 'tools/acts/b751.py'), show(BASE, 'tools/b751_worklist.py')
    carried, cwl = CA.substitute(prev, subs), CA.substitute(pwl, subs)
    ruling = rdf('data/%s_ferry.txt' % act)
    ords = dict(x for x in (CA.ordinal_of(ruling), CA.ordinal_of(rdf('data/b751_ferry.txt'))) if x)
    own = NL.join(json.loads(rdf('data/%s_readfirst_rows.json' % act) or '{}').get('own') or [])
    _oL, oref = OCA.ruled(carried, prev, cwl, pwl, ruling, subs, ferry_routed=True)
    _nL, nref = CA.ruled(carried, prev, cwl, pwl, ruling, subs, ferry_routed=True, ordinals=ords, own_rows=own)
    k7 = lambda R: [r for r in R if r[0] == 'R7']   # noqa: E731
    n += 1
    g += case(L, 'carry', 'b751`s module as `carry acts` brings it under b752`s names, beside (R362) (the first carry of b752`s step zero)',
              'carry.py at %s: refused %d, R7 none (ordinals and needles unread)' % (BASE, len(oref)), 'refused %d, R7 %d: %s' % (len(nref), len(k7(nref)), [r[1] for r in k7(nref)][:5]),
              not k7(oref), len(k7(nref)) > 0 and any(r[1].startswith('ordinal') for r in k7(nref)) and any(r[1].startswith('needle') for r in k7(nref)))
    _cL, cref = CA.ruled(rdf('tools/acts/%s.py' % act), prev, rdf('tools/%s_worklist.py' % act), pwl, ruling, subs, ferry_routed=True, ordinals=ords, own_rows=own)
    n += 1
    g += guard(L, 'carry', '%s`s module and worklist as set at Component 1 (needles, :1074 prior head, :1306 title, :1738 trail head): refused 0' % act,
               'refused %d %s ; ordinals %s' % (len(cref), cref[:2], ords), not cref)
    return L, g, n


# ================================================================================ (flag) (7)(vii): A FLAG READ AS AN ACT
def control_flag():
    L, g, n = ['### (flag) (R362)(7)(vii), b751 defect (t): A TOOL THAT TAKES AN ACT REFUSES A NAME BEGINNING WITH A HYPHEN BEFORE IT READS OR WRITES'], 0, 0
    tools_ = ('wlist.py', 'carry.py', 'readfirst.py', 'armnorm.py', 'prelock.py', 'compilecontrol.py')
    ow = show(BASE, 'tools/standing/wlist.py')
    try:
        A.act_name('--quiet', 'wlist.py bank')
        nw = 'NOT REFUSED'
    except SystemExit as e:
        nw = str(e)[:150]
    n += 1
    g += case(L, 'flag', '`wlist.py bank --quiet` (15:22:46Z), which wrote data/--quiet_wlist.json', 'wlist.py at %s: act_name %s; the flag taken as the act' % (BASE, 'act_name(' in ow),
              nw, 'act_name(' not in ow, nw.startswith('### REFUSED'))
    have = dict((t_, 'act_name(' in rdf('tools/standing/' + t_)) for t_ in tools_)
    n += 1
    g += guard(L, 'flag', 'each tool that takes an act name reads it through act.act_name', have, all(have.values()))
    n += 1
    g += guard(L, 'flag', 'an act name passes; no data/--quiet_wlist.json stands', '%s ; %s' % (A.act_name('b752', 'x'), os.path.isfile(os.path.join(D, '--quiet_wlist.json'))),
               A.act_name('b752', 'x') == 'b752' and not os.path.isfile(os.path.join(D, '--quiet_wlist.json')))
    return L, g, n


# ================================================================================ (limit) (7)(viii): THE LIMIT ROW READS THE INTERPRETER'S PLACE
def control_limit():
    L, g, n = ['### (limit) (R362)(7)(viii), b751 defects (g), (p), b752`s 22:11:47Z and 22:11:48Z: THE LIMIT ROW READS A ROUTE IN THE INTERPRETER`S PLACE ALONE, ITS QUOTING PARSED'], 0, 0
    OH, OLI = old('hook.py', 'hook_v1310'), old('limits.py', 'limits_v1310')
    om = OH._mod
    OH._mod = lambda nm: OLI if nm == 'limits' else om(nm)
    lim = lambda H, c: (lambda r: r if r and r[0] == 'LIMIT' else None)(H.judge('Bash', {'command': c}, relay=RELAY))   # noqa: E731
    false_ = (('b751 (p), 14:05:00Z', 'wc -l tools/b750_prepaths.py tools/b750_face.py tools/b750_face_blocks.txt tools/b749_prepaths.py tools/b749_face.py && git log --format=%h -1 -- tools/b750_prepaths.py'),
              ('b752, 22:11:47Z', 'git grep -n -E "def tri\\b|tri = |^def tri" -- tools/standing/fold/checks.tpl tools/b703_checks.py tools/standing/*.py'),
              ('b752, 22:11:48Z', 'git grep -n -E "^CURRENTS|^PP_EDITED" -- tools/b703_checks.py tools/b750_worklist.py tools/b751_worklist.py tools/b752_worklist.py'))
    for what, c in false_:
        o, nw = lim(OH, c), lim(HK, c)
        n += 1
        g += case(L, 'limit', '%s: a route`s name as an argument, refused as a run' % what, 'hook.py at %s: %s' % (BASE, (o or ('let through',))[0]), (nw or ('let through',))[0], bool(o), nw is None)
    q = "python -X utf8 -c \"\nimport sys;sys.path.insert(0,'tools/standing')\nimport hook as H\nprint(H.judge('Bash',{'command':'python tools/b750_prepaths.py --bank'}))\""
    n += 1
    g += guard(L, 'limit', 'b751 (g), 12:43:03Z: a route named inside a quoted program, let through', lim(HK, q) or 'let through', lim(HK, q) is None)
    caught = (('a suite part', 'cd /d/relay && python -X utf8 -u tools/standing/fold.py checks --part standing-a1'),
              ('the probe-path tool', 'python -X utf8 -u tools/b750_prepaths.py --bank'),
              ('the root route', 'cd /d/relay && python -X utf8 -u tools/act_root.py b752'),
              ('the mirror build', 'powershell -File D:\\relay\\tools\\mirror_build.ps1 -DateTag 2026-11-10-b752'),
              ('these controls', 'python -X utf8 -u tools/standing/v1320.py control --bank'))
    for what, c in caught:
        r = lim(HK, c)
        n += 1
        g += guard(L, 'limit', '%s sent with no timeout: still refused; with timeout 600000 let through' % what, '%s ; %s' % ((r or ('LET THROUGH',))[0], HK.judge('Bash', {'command': c, 'timeout': 600000}) or 'let through'),
                   bool(r) and HK.judge('Bash', {'command': c, 'timeout': 600000}) is None)
    return L, g, n


# ================================================================================ (cites) (7)(ix): THE DECLARATION READER
def control_cites():
    L, g, n = ['### (cites) (R362)(7)(ix), b751 defect (d), REPEAT b736 (e), b752`s step-zero HALT :17: THE READER TAKES inductive, class, axiom, opaque, protected AND A NAMESPACED DOTTED NAME'], 0, 0
    OCI = old('cites.py', 'cites_v1310c')
    res = {}
    for a in ['b%d' % k for k in range(736, 753)]:
        t = rdf('data/%s_ferry.txt' % a)
        if not t:
            continue
        try:
            K = importlib.import_module('%s_worklist' % a)
            trees = list(getattr(K, 'LEAN_TREES', ()) or ())
        except Exception:  # noqa: BLE001
            continue
        if not trees:
            continue
        o, nw = OCI.lean_rows(t, trees), CI.lean_rows(t, trees)
        res[a] = (o, nw)
    o, nw = res.get('b752', ([], []))
    n += 1
    g += case(L, 'cites', 'b752`s ferry :17: MechanismClass at Bridge/TheBridgeComplete.lean :20, an inductive', 'cites.py at %s: rows %d, failing %d' % (BASE, len(o), sum(not x[3] for x in o)),
              'rows %d, failing %d' % (len(nw), sum(not x[3] for x in nw)), any(not x[3] for x in o), bool(nw) and all(x[3] for x in nw))
    o1, n1 = res.get('b751', ([], []))
    dn = 'norm_le_of_forall_mem_frontier_norm_le'
    n += 1
    g += case(L, 'cites', 'b751`s ferry :11: the dotted name at AbsMax.lean :405', 'cites.py at %s: the dotted name read %s' % (BASE, any(dn in str(x) for x in o1)),
              'the dotted name read %s' % any(dn in str(x) for x in n1), not any(dn in str(x) for x in o1), any(dn in str(x) and x[3] for x in n1))
    # ### a failing row the old reader did not fail, keyed by its line and its path (the row's name may be new: the old reader skipped dotted names)
    pth = lambda x: x[1].split(' beside ')[-1]   # noqa: E731
    worse = dict((a, [x for x in nw_ if not x[3] and not any(y[0] == x[0] and pth(y) == pth(x) and not y[3] for y in o_)]) for a, (o_, nw_) in res.items()
                 if a not in ('b751', 'b752'))
    n += 1
    g += guard(L, 'cites', 'the wider replay over the earlier ferries with Lean trees (%s): no failing row the old reader did not fail, b751 and b752`s instances apart' % ', '.join(sorted(res)),
               '%s ; new failing rows %s' % ('; '.join('%s %d->%d' % (a, sum(not x[3] for x in o_), sum(not x[3] for x in nw_)) for a, (o_, nw_) in sorted(res.items())),
                                             [(a, r) for a, v in worse.items() for r in v] or 'NONE'),
               bool(res) and not any(worse.values()))
    pl = CI.lean_rows('Real.exp_bound, Analysis/SpecialFunctions/Stirling.lean ; then Real.exp_bound at Analysis/SpecialFunctions/Stirling.lean', res and list(
        importlib.import_module('b740_worklist').LEAN_TREES) or [])
    n += 1
    g += guard(L, 'cites', 'b740 :29`s shape planted beside the joined shape: the listed name passed over, the joined name read and failing (declared at Complex/Exponential.lean)',
               [(x[1], x[3]) for x in pl if 'beside' in x[1]], sum(1 for x in pl if 'beside' in x[1]) == 1 and not next(x for x in pl if 'beside' in x[1])[3])
    return L, g, n


# ================================================================================ (instances) (7)(ix): THE INSTANCES PRINTED
def control_instances():
    L, g, n = ['### (instances) (R362)(7)(ix), b751 defects (a), (d), (f), (n), (r), (u), (v), events (5), REPEAT: THE HOOK`S REFUSALS, THE TRANSIENT REMOTE READS AND THE HOST`S REFUSAL, THE INSTANCES PRINTED'], 0, 0
    kinds = ('PIPE', 'READ', 'SED', 'REDIR', 'ENV', 'LOCKED', 'WLIST', 'COMPOSER', 'LIMIT', 'REMOTE', 'GIT', 'BYDESIGN')
    for a in ('b751', A.current()['act']):
        rf = [l for l in rdf('data/%s_hook_refusals.txt' % a).split(NL) if l.strip()]
        n += 1
        g += guard(L, 'instances', 'printed: %s`s hook refusals, data/%s_hook_refusals.txt, by kind' % (a, a),
                   '%d rows: %s' % (len(rf), ', '.join('%s %d' % (k, sum(1 for l in rf if '| %s |' % k in l)) for k in kinds if any('| %s |' % k in l for l in rf)) or 'none of the kinds'), bool(rf))
    for k in ('a', 'd', 'f', 'n', 'r', 'u', 'v'):
        row = _row('data/b751_defects.txt', k)
        n += 1
        g += guard(L, 'instances', 'printed: b751 defect (%s)' % k, row[:150] or 'ABSENT', bool(row))
    row = _row('data/b751_events.txt', '5')
    n += 1
    g += guard(L, 'instances', 'printed: b751 events (5), the host`s refusal at the network and the one re-send', row[:150] or 'ABSENT', bool(row) and 'Could not' in rdf('data/b751_events.txt'))
    return L, g, n


# ================================================================================ (session) (7)(x): THE SESSION CHANGE, THE STANDING RULE WORKING
def control_session():
    L, g, n = ['### (session) (R362)(7)(x): b751`s SESSION CHANGE AT 16:47:23Z (THE FACE`S SENTENCE) READ THROUGH THE STANDING RULE (b671`s form, K.SESSIONS_AFTER): THE RULE WORKING'], 0, 0
    fb = rdf('tools/b751_face_blocks.txt')
    m = re.search(r'From 16:47:23Z the act continues in session 43048615[^.]*\.', fb)
    n += 1
    g += guard(L, 'session', 'the face`s sentence (tools/b751_face_blocks.txt)', (m.group(0)[:160] if m else 'ABSENT'), bool(m))
    wl = rdf('tools/b751_worklist.py')
    n += 1
    g += guard(L, 'session', 'b751`s worklist carries the continuation in SESSIONS_AFTER, its first user line the anchor', 'SESSIONS_AFTER 43048615 %s' % ("SESSIONS_AFTER = (('43048615" in wl), "SESSIONS_AFTER = (('43048615" in wl)
    tp = dict((t_, 'SESSIONS_AFTER' in rdf('tools/standing/fold/%s.tpl' % t_)) for t_ in ('record', 'checks', 'citation'))
    n += 1
    g += guard(L, 'session', 'the record, suite and citation routes each read the continuation sessions', tp, all(tp.values()))
    ans = rdf('data/b751_author_answers.txt')
    n += 1
    g += guard(L, 'session', 'b751`s banks read the continuation: the answers bank carries a word of session 43048615', '43048615 in the answers bank %s' % ('43048615' in ans), '43048615' in ans)
    return L, g, n


# ================================================================================ (version) (7)(xi)
def control_version():
    L, g, n = ['### (version) (R362)(7)(xi): THE STANDING VERSION PRINTED AND ITS CONTROLS TALLIED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = show(BASE, 'tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.31.0', ver == 'v1.32.0')
    return L, g, n


CONTROLS = dict(paths=control_paths, recall=control_recall, currents=control_currents, append=control_append, orders=control_orders, carry=control_carry,
                flag=control_flag, limit=control_limit, cites=control_cites, instances=control_instances, session=control_session, version=control_version)
ORDER = ('paths', 'recall', 'currents', 'append', 'orders', 'carry', 'flag', 'limit', 'cites', 'instances', 'session', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.32.0, (R362)(7)(i)-(xi): EVERY PATH AT HEAD, A REFUSED CALL NO REMOTE READ, THE CURRENTS ON THE PREVIOUS ACT`S BANKS, '
           'THE ANSWERS APPEND BY PLACE, A ROW ID NO ORDER, THE CARRY`S ORDINALS AND NEEDLES, A FLAG NO ACT, THE LIMIT ROW`S PLACE, THE DECLARATION READER, '
           'THE INSTANCES, THE SESSION RULE, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
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
    out.append('### ### **v1.32.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1320.txt' % act), NL.join(out))
        print('written data/%s_standing_v1320.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
