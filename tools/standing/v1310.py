# -*- coding: utf-8 -*-
"""standing/v1310.py -- THE CONTROLS OF v1.31.0 ((R361)(3)(i)-(xi); b750 events (1)-(7), defects (a)-(y)), in v1300.py's form: each instance read
through the route as it stood before the repair (tools/standing/ at BASE, b750's closing relay head, read from its blobs) and through the repaired
route on disk; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side. THE COMPILE CONTROL
RUNS FIRST. The free memory is read and printed before each control. Written at b751 by the Write tool; no identifier of the author is read into
any string here.

  python -X utf8 -u tools/standing/v1310.py control [order|wlist|composer|linematch|gatescan|compile|carry|words|limit|instances|version ...] [--bank]
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
BASE = '467a1968'   # ### b750's closing relay head (PRE_RELAY of b751): the routes before this repair
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import carry as CA              # noqa: E402
import commit as CM             # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import limits as LI             # noqa: E402
import linematch as LM          # noqa: E402
import repeat as RP             # noqa: E402
import rootprompt as RPM        # noqa: E402
import standingdry as SD        # noqa: E402
import wlist as WL              # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def rdf(rel, root=RELAY):
    p = os.path.join(root, rel)
    return io.open(p, encoding='utf-8').read().replace('\r', '') if os.path.isfile(p) else ''


def old(rel, name):
    """tools/standing/<rel> as BASE left it, loaded from its blob under another name."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, name + '.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(show(BASE, 'tools/standing/' + rel))
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
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.30.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.31.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.31.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


PARTS = ('standing-a1', 'standing-a2', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'act')


# ================================================================================ (order) (3)(i): THE SUITE PARTS IN THEIR ORDER
def control_order():
    L, g, n = ['### (order) (R361)(3)(i), b750 events (3), (7), REPEAT b717 (3): THE PART RUNNER REFUSES A PART WHOSE PREDECESSOR HAS NO BANK IN THE MODE ASKED, AND PRINTS THE ORDER'], 0, 0
    otpl = show(BASE, 'tools/standing/fold/checks.tpl')
    ev = rdf('data/b750_events.txt').split(NL)
    n += 1
    g += guard(L, 'order', 'the instance found: b750 events (3) (data/b750_events.txt :12-:15)', (ev[11].strip()[:150] if len(ev) > 11 else 'ABSENT'),
               len(ev) > 14 and 'standing-a2 at' in ev[11] and '05:34:36Z' in ev[11] + ev[12])
    # ### at 05:34:36Z none of b750's prev-mode part banks stood (standing-a1 banked its half at 06:20:06Z)
    at_0534 = set()
    old_guard = 'order_refusal' in otpl
    new = RP.order_refusal('standing-a2', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], lambda nm: nm in at_0534)
    n += 1
    g += case(L, 'order', 'b750`s standing-a2 on b750`s banks (`--prev`) at 05:34:36Z, standing-a1`s bank not yet written',
              'checks.tpl at %s: no order guard (%s); the part ran and read G-NO-SORRY-MAIN DIVERGE' % (BASE, 'a guard present' if old_guard else 'order_refusal absent'),
              new or 'NOT REFUSED', not old_guard, bool(new) and 'standing-a1' in (new or '') and ' -> '.join(PARTS) in (new or ''))
    at_0545 = {'b750_prevrun_standing-a1.txt', 'b750_prevrun_standing-a2.txt', 'b750_prevrun_standing-c.txt', 'b750_prevrun_standing-b1.txt'}
    nb3 = RP.order_refusal('standing-b3', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], lambda nm: nm in at_0545)
    n += 1
    g += guard(L, 'order', 'b750`s standing-b3 at 05:45:05Z, before standing-b2a-d (refused at the time by b3`s own guard, exit 4): refused by the order guard too', nb3 or 'NOT REFUSED',
               bool(nb3) and 'standing-b2d' in nb3)
    ex = lambda nm: os.path.isfile(os.path.join(D, nm))   # noqa: E731
    n += 1
    g += guard(L, 'order', 'the first part, and standing-a2 after standing-a1`s bank (b750`s banks as they stand), not refused',
               '%s ; %s' % (RP.order_refusal('standing-a1', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], ex), RP.order_refusal('standing-a2', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], ex)),
               RP.order_refusal('standing-a1', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], ex) is None and RP.order_refusal('standing-a2', PARTS, lambda p: ['b750_prevrun_%s.txt' % p], ex) is None)
    import fold as F
    secs, ovs = F._parse(A.current()['act'])
    txt = F.render(A.current()['act'], 'checks', secs=secs, ovs=ovs)
    n += 1
    g += guard(L, 'order', 'the act`s rendered suite carries the guard before b3`s and compiles', '%d lines ; order_refusal %s' % (txt.count(NL), 'order_refusal' in txt),
               'order_refusal' in txt and bool(compile(txt, 'checks', 'exec')))
    return L, g, n


# ================================================================================ (wlist) (3)(ii): THE WRITES OUTSIDE THE (W) LIST
def control_wlist():
    L, g, n = ['### (wlist) (R361)(3)(ii), b750 defects (h), (i): A WRITE OR EDIT OF A TRACKED PATH OUTSIDE THE (W) LIST REFUSED BY THE HOOK BEFORE IT LANDS, THE LIST READ FROM THE REGENERATED BANK'], 0, 0
    OH = old('hook.py', 'hook_v1300')
    inst = {'file_path': os.path.join(RELAY, 'tools', 'act_close.py').replace('\\', '/'), 'old_string': 'x', 'new_string': 'y'}
    o, nw = OH.judge('Edit', inst, relay=RELAY), HK.judge('Edit', inst)
    n += 1
    g += case(L, 'wlist', 'b750`s Edit of tools/act_close.py (defect (i)), replayed against b751`s regenerated list (data/b751_wlist.json)',
              'hook.py at %s: %s' % (BASE, o or 'let through'), nw or 'let through', o is None, bool(nw) and nw[0] == 'WLIST')
    bank = json.load(io.open(WL.bank_path(A.current()['act']), encoding='utf-8'))
    n += 1
    g += guard(L, 'wlist', 'the bank read: data/%s_wlist.json, source %s, %d patterns, sources %s' % (A.current()['act'], bank.get('source'), len(bank.get('patterns') or []),
               ', '.join('%s %s' % (k, v[:8]) for k, v in (bank.get('sources') or {}).items())), 'current (not stale); its reading of tools/act_close.py: %s' % WL.fault(inst['file_path']),
               bool(WL.fault(inst['file_path'])) and 'stale' not in WL.fault(inst['file_path']))
    allowed = [os.path.join(RELAY, 'tools', 'standing', 'hook.py'), os.path.join(RELAY, 'data', '%s_events.txt' % A.current()['act']),
               os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'), os.path.join(SCRATCH, 'not_tracked.txt')]
    res = [(p.replace('\\', '/')[-60:], HK.judge('Edit', {'file_path': p})) for p in allowed]
    n += 1
    g += guard(L, 'wlist', 'paths the list covers or no repository tracks let through: a standing tool, the act`s events bank, the paper, a scratch file', res, all(r is None for _p, r in res))
    refused = [os.path.join(PP, 'README.md'), os.path.join(RELAY, 'tools', 'acts', 'b750.py'), os.path.join(RELAY, 'data', 'b750_closing.txt')]
    res2 = [(p.replace('\\', '/')[-40:], (HK.judge('Write', {'file_path': p}) or ('',))[0]) for p in refused]
    n += 1
    g += guard(L, 'wlist', 'tracked paths outside the list refused: PLACE-papers README.md (no passed item names it), b750`s module and closing', res2, all(r == 'WLIST' for _p, r in res2))
    st = dict(bank, sources=dict(bank.get('sources') or {}, **{'data/%s_ferry.txt' % A.current()['act']: '0' * 64}))
    d = tempfile.mkdtemp(dir=SCRATCH)
    try:
        sp = os.path.join(d, 'wl.json')
        io.open(sp, 'w', encoding='utf-8').write(json.dumps(st))
        p_bank = WL.bank_path
        WL.bank_path = lambda act: sp
        try:
            stale = WL.fault(allowed[0])
        finally:
            WL.bank_path = p_bank
    finally:
        shutil.rmtree(d, ignore_errors=True)
    n += 1
    g += guard(L, 'wlist', 'a stale bank (the ferry`s digest planted) refuses every tracked write until the list is regenerated', stale or 'NOT REFUSED', bool(stale) and 'stale' in stale)
    df = rdf('data/b750_defects.txt').split(NL)
    n += 1
    g += guard(L, 'wlist', 'defect (h) read: tools/standing/deletes.py stands inside the list (tools/standing/*); its fault was the unread overwrite, which the Write tool itself refuses',
               (df[13].strip()[:120] if len(df) > 13 else 'ABSENT') + ' ; judged now: %s' % (HK.judge('Write', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'deletes.py')}),),
               len(df) > 13 and 'deletes.py' in df[13] and HK.judge('Write', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'deletes.py')}) is None)
    return L, g, n


# ================================================================================ (composer) (3)(iii): EVERY PROMPT THROUGH THE COMPOSER
def _b750_prompt3():
    ans = rdf('data/b750_author_answers.txt').split(NL)
    q = next((l for l in ans if l.startswith('### PROMPT 3 ([G2] errata): ')), '')
    i = ans.index(q) if q else -1
    opts = []
    for l in ans[i + 1:i + 3] if q else []:
        m = re.match(r'^OPTION \d+: (.*?) :: (.*)$', l)
        if m:
            opts.append(dict(label=m.group(1), description=m.group(2)))
    return dict(question=q.split('): ', 1)[1] if q else '', header='[G2] errata', options=opts, multiSelect=False), (i + 1)


def control_composer():
    L, g, n = ['### (composer) (R361)(3)(iii), N3 BEFORE b750`S ROOT: EVERY PROMPT -- THE SITTING ITEMS, THE HALTS AND THE ROOT -- THROUGH compose_checked BEFORE IT IS PUT, BANKED BY `rootprompt.py put`'], 0, 0
    q, at = _b750_prompt3()
    ORP = old('rootprompt.py', 'rootprompt_v1300')
    n += 1
    g += guard(L, 'composer', 'the instance found: b750`s third sitting prompt (data/b750_author_answers.txt :%d), its clause "b746`s entry,"' % at, q['question'][:110], "b746's entry," in q['question'])
    try:
        RPM.put_check([q], RPM.relay_reader(RELAY), '', rdf('data/b750_ferry.txt'))
        nw = 'NOT REFUSED'
    except SystemExit as e:
        nw = str(e)
    n += 1
    g += case(L, 'composer', 'b750`s sitting prompt 3 replayed through the route every prompt now takes (entry not yet composed, as before b750`s root)',
              'rootprompt.py at %s: no put route (%s); the sitting items put by hand, unchecked' % (BASE, 'put present' if hasattr(ORP, 'put_check') else 'put_check absent'),
              nw[:200], not hasattr(ORP, 'put_check'), nw.startswith('### QUESTION 1') and "b746's entry," in nw)
    OH = old('hook.py', 'hook_v1300c')
    inp = {'questions': [q]}
    o, nh = OH.judge('AskUserQuestion', inp, relay=RELAY), HK.judge('AskUserQuestion', inp)
    n += 1
    g += case(L, 'composer', 'the same prompt sent by AskUserQuestion with no put bank holding it', 'hook.py at %s: %s' % (BASE, o or 'let through'), nh or 'let through',
              o is None, bool(nh) and nh[0] == 'COMPOSER')
    d = tempfile.mkdtemp(dir=SCRATCH)
    try:
        os.makedirs(os.path.join(d, 'data'))
        good = [dict(question='Pass or strike [S5], the section as drafted?', header='[S5]', multiSelect=False,
                     options=[dict(label='Pass [S5]', description='The section written as drafted, one write.'), dict(label='Strike [S5]', description='No write.')])]
        rel = RPM.put('b751', good, '', relay=d)
        ok_ = RPM.put_fault('b751', good, relay=d)
        moved = RPM.put_fault('b751', [dict(good[0], question=good[0]['question'] + ' Now.')], relay=d)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    n += 1
    g += guard(L, 'composer', 'a question composed and banked by put passes the hook`s read; the same question reworded after the bank is refused', '%s ; as banked %s ; reworded %s' % (rel, ok_, (moved or '')[:60]),
               ok_ is None and bool(moved))
    st = io.open('D:/.claude/settings.json', encoding='utf-8').read()
    n += 1
    g += guard(L, 'composer', 'the matcher in the seat`s settings carries AskUserQuestion', re.search(r'"matcher": "([^"]*)"', st).group(1), 'AskUserQuestion' in st)
    return L, g, n


# ================================================================================ (linematch) (3)(iv): THE LINE READER'S MATCH
def control_linematch():
    L, g, n = ['### (linematch) (R361)(3)(iv), data/b750_line.txt :31-:32: THE LINE READER MATCHES EACH ENTRY`S FINDINGS AGAINST THE NAMES THE KEYSTONE`S NOTE CARRIES BEFORE IT READS SYNTHESISED'], 0, 0
    F_ = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8').read().split(NL)
    W_ = io.open(os.path.join(PP, 'day1', 'Which_Structure_Confines_v2_4_0.md'), encoding='utf-8').read().split(NL)
    note = W_[96] if len(W_) > 96 else ''
    lb = rdf('data/b750_line.txt').split(NL)
    n += 1
    g += guard(L, 'linematch', '[F2]`s note read (Which_Structure_Confines_v2_4_0.md :97), its names', LM.names(note), '(R360)`(2)[F2]' in note and 'pc_online' in LM.names(note))
    for ln, a in ((14145, 'b745'), (14187, 'b746'), (14299, 'b747'), (14427, 'b748')):
        o_row = next((l for l in lb if 'FINDINGS :%d (%s)' % (ln, a) in l), '')
        o_st = 'SYNTHESISED' if 'as the maps read now SYNTHESISED' in o_row else 'CLUSTERED' if 'as the maps read now CLUSTERED' in o_row else '?'
        r = LM.read(F_, ln, note)
        n += 1
        if r['matched']:
            g += guard(L, 'linematch', '%s (FINDINGS :%d), its heading :%s names %s' % (a, ln, r['heading'], r['names']),
                       'b750 by the cluster %s ; by the match %s (%s matched)' % (o_st, r['stage'], ', '.join(r['matched'])), r['stage'] == 'SYNTHESISED')
        else:
            g += case(L, 'linematch', '%s (FINDINGS :%d), its heading :%s naming no finding the note carries (names %s)' % (a, ln, r['heading'], r['names'] or 'none'),
                      'tools/b750_line.py by the cluster (data/b750_line.txt): %s' % o_st, 'by the match: %s' % r['stage'], o_st == 'SYNTHESISED', r['stage'] == 'CLUSTERED')
    planted = ['## A planted entry: planted_unnamed_finding compiled at a planted pin', 'its body', 'INTEGRATION: cluster the Epstein instance ; keystone ... ; stage ?']
    r = LM.read(planted, 3, note)
    n += 1
    g += case(L, 'linematch', 'a planted entry whose finding the note does not name (planted_unnamed_finding)', 'by the cluster: SYNTHESISED (the note stands in a file the cluster names)',
              'by the match: %s, names %s, matched %s' % (r['stage'], r['names'], r['matched'] or 'none'), True, r['stage'] == 'CLUSTERED')
    return L, g, n


# ================================================================================ (gatescan) (3)(v): THE SCAN LEFT OUT OF A COMMIT
def control_gatescan():
    L, g, n = ['### (gatescan) (R361)(3)(v), b750 defect (x), REPEAT b749 (c): NO COMMIT, THE GATE`S AMONG THEM, LEAVES THE ACT`S SCAN BANK WRITTEN AND UNTRACKED'], 0, 0
    OC = old('commit.py', 'commit_v1300')
    first = _git('log', '--diff-filter=A', '--format=%h %cI', '--', 'data/b750_address_scan.txt').strip().split(NL)[-1]
    df = rdf('data/b750_defects.txt').split(NL)
    n += 1
    g += guard(L, 'gatescan', 'the instance found: b750 defect (x) (data/b750_defects.txt :30); the scan bank first committed at %s' % first, (df[29].strip()[:140] if len(df) > 29 else 'ABSENT'),
               len(df) > 29 and 'cc1fc182' in df[29] and first.startswith('8e267be7'))
    for c in ('cc1fc182', 'ac800f3d'):
        names = [x for x in _git('show', '--name-only', '--format=', c).split(NL) if x]
        unt = ['data/b750_address_scan.txt']   # ### written 02:02:49Z, untracked until 8e267be7
        nw = CM.scan_left_out('b750', names, unt)
        n += 1
        g += case(L, 'gatescan', 'relay %s replayed: %d files staged, data/b750_address_scan.txt written and untracked, not among them' % (c, len(names)),
                  'commit.py at %s: %s' % (BASE, 'scan_left_out present' if hasattr(OC, 'scan_left_out') else 'no such refusal; the commit made, the scan`s own run 0 printed'),
                  nw or 'NOT REFUSED', not hasattr(OC, 'scan_left_out'), bool(nw) and 'data/b750_address_scan.txt' in nw)
    n += 1
    g += guard(L, 'gatescan', 'the bank staged (8e267be7`s case) and no scan bank yet (b751 now) not refused', '%s ; %s' % (
        CM.scan_left_out('b750', ['data/b750_address_scan.txt'], ['data/b750_address_scan.txt']), CM.scan_left_out('b751', ['tools/standing/VERSION'], [])),
        CM.scan_left_out('b750', ['data/b750_address_scan.txt'], ['data/b750_address_scan.txt']) is None and CM.scan_left_out('b751', ['tools/standing/VERSION'], []) is None)
    src = io.open(os.path.join(S, 'commit.py'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'gatescan', 'run() reads the relay`s untracked paths after the standing dry`s refusal and before the scan, every phase the gate`s among them',
               'scan_left_out called in run: %s' % ('bad = scan_left_out(act, names,' in src), 'bad = scan_left_out(act, names,' in src)
    return L, g, n


# ================================================================================ (compile) (3)(vi): THE RENDERED MODULE'S INDENTATION
def control_compile():
    L, g, n = ['### (compile) (R361)(3)(vi), b750 defect (j): THE STANDING DRY COMPILES EVERY RENDERED MODULE AND PRINTS THE EARLIEST ERROR WITH ITS LINE'], 0, 0
    import fold as F
    act = A.current()['act']
    rec = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    lines = rec.split(NL)
    planted = NL.join(lines[:1] + ['# ### a line planted above the line-keyed overrides, as v1.30.0`s opening render added lines'] + lines[1:])
    secs, ovs = F._parse(act)
    try:
        compile(F.render(act, 'record', secs=secs, ovs=ovs, tpl=planted), act + '_record.py', 'exec')
        o = 'the act`s own record render compiles; the dry`s one composition (`record findings dry`) reads nothing of the older acts'
        o_fails = True
    except (SyntaxError, F.FoldRefused) as e:
        o, o_fails = 'the act`s own render fails too: %s' % e, False
    ODY = show(BASE, 'tools/standing/standingdry.py')
    head = SD.renders(tpls=SD.head_templates())
    now_p = SD.renders(tpls={'record': planted})
    v, cl = SD.compile_reading(now_p, head)
    new = [x for x in cl if x.startswith('  NEW')]
    n += 1
    g += case(L, 'compile', 'v1.30.0`s opening render replayed: record.tpl with one line planted above the overrides, every act module rendered',
              'standingdry.py at %s (renders %s): %s' % (BASE, 'compiled' if 'def renders' in ODY else 'not compiled', o), '%s ; %d new failure(s), the earliest: %s' % (v, len(new), (new[0].strip()[:110] if new else 'none')),
              o_fails and 'def renders' not in ODY, v == 'NOT CLEAN' and bool(new) and 'line' in new[0])
    v2, cl2 = SD.compile_reading(SD.renders(), head)
    n += 1
    g += guard(L, 'compile', 'the working templates over every act module against HEAD`s: no new failure (the carried ones printed in the dry)', '%s ; %s' % (v2, cl2[0].strip()), v2 == 'CLEAN')
    return L, g, n


# ================================================================================ (carry) (3)(vii): THE CARRY
def control_carry():
    L, g, n = ['### (carry) (R361)(3)(vii), b750 defects (d), (m), (s), REPEAT: THE CARRY PRINTS EVERY ROW AND FIGURE IT BRINGS BESIDE THIS RULING AND REFUSES WHAT IT DOES NOT NAME; THE FERRY BANKED BY THE CITATION ROUTE'], 0, 0
    OCA = old('carry.py', 'carry_v1300')
    subs = (('b750', 'b751'), ('b749', 'b750'))
    prev, pwl = show('HEAD', 'tools/acts/b750.py'), show('HEAD', 'tools/b750_worklist.py')
    carried, cwl = CA.substitute(prev, subs), CA.substitute(pwl, subs)
    ruling = rdf('data/b751_ferry.txt')
    oL, oref = OCA.ruled(carried, prev, cwl, pwl, ruling, subs)
    nL, nref = CA.ruled(carried, prev, cwl, pwl, ruling, subs, ferry_routed=False)
    ok_ = lambda R, k: sum(1 for r in R if r[0] == k)   # noqa: E731
    n += 1
    g += guard(L, 'carry', 'b750`s module and worklist as `carry acts` brings them under b751`s names, read beside (R361): refused by both routes (R4, R5)',
               'before R4 %d R5 %d ; after R4 %d R5 %d' % (ok_(oref, 'R4'), ok_(oref, 'R5'), ok_(nref, 'R4'), ok_(nref, 'R5')), ok_(oref, 'R4') + ok_(oref, 'R5') > 0 and ok_(nref, 'R4') + ok_(nref, 'R5') > 0)
    n += 1
    g += case(L, 'carry', 'the same carry at b750`s step zero, its ferry banked by the Write tool alone (data/b750_ferry_scan.txt first written at Component 4, defect (s))',
              'carry.py at %s: R6 %d, the ferry`s route not read' % (BASE, ok_(oref, 'R6')), 'R6 %d: %s' % (ok_(nref, 'R6'), next((r[2] for r in nref if r[0] == 'R6'), 'none')),
              ok_(oref, 'R6') == 0, ok_(nref, 'R6') == 1)
    orows = sum(1 for l in oL if l.startswith('    add(') or l.startswith('    ') and ' | ' in l)
    nrows = sum(1 for l in nL if l.startswith('    ') and ' | ' in l)
    n += 1
    g += case(L, 'carry', 'every carried row printed with its banks beside the ruling', 'rows printed %d (the counts and the refused rows alone)' % orows,
              'rows printed %d, each bank with the ruling`s line or NOT NAMED' % nrows, orows == 0, nrows > 0)
    now = CA.ruled(rdf('tools/acts/b751.py'), rdf('tools/acts/b750.py'), rdf('tools/b751_worklist.py'), rdf('tools/b750_worklist.py'), ruling, subs,
                   ferry_routed=os.path.isfile(os.path.join(D, 'b751_ferry_scan.txt')))[1]
    n += 1
    g += guard(L, 'carry', 'b751`s module and worklist as rewritten at step zero, its ferry banked by the citation route: refused 0', 'refused %d %s' % (len(now), now[:2]), not now)
    return L, g, n


# ================================================================================ (words) (3)(viii): THE TOOL'S WORDS AND PHASES
def control_words():
    L, g, n = ['### (words) (R361)(3)(viii), b750 defects (b), (k), (o), (u), (y), REPEAT: THE INSTANCES PRINTED; THE ONE-CALL TOOL`S USAGE PRINTED BY THE CARRY AT STEP ZERO'], 0, 0
    df = rdf('data/b750_defects.txt').split(NL)
    for k, i in (('b', 7), ('k', 16), ('o', 20), ('u', 26), ('y', 30)):
        n += 1
        g += guard(L, 'words', 'printed: b750 defect (%s), data/b750_defects.txt :%d' % (k, i + 1), (df[i].strip()[:150] if len(df) > i else 'ABSENT'), len(df) > i and df[i].strip().startswith('(%s)' % k))
    ocs = show(BASE, 'tools/standing/carry.py')
    ncs = io.open(os.path.join(S, 'carry.py'), encoding='utf-8').read()
    u = CM.usage_lines()
    n += 1
    g += case(L, 'words', '`carry.py ruled` at step zero prints the tool`s usage, its phases and its word form', 'carry.py at %s: usage printed %s' % (BASE, 'usage_lines' in ocs),
              'usage printed %s: %d lines, %s' % ('CM.usage_lines()' in ncs, len(u), u[-2].strip()[:90]), 'usage_lines' not in ocs,
              'CM.usage_lines()' in ncs and any('gate | lock | seal (no words)' in x for x in u) and any('the step row for relay' in x for x in u))
    return L, g, n


# ================================================================================ (limit) (3)(ix): THE HOST'S LIMIT
def control_limit():
    L, g, n = ['### (limit) (R361)(3)(ix), b750 defect (t), events (6): A RUN THAT MAY EXCEED THE HOST`S DEFAULT SENT WITH THE LIMIT THE TOOL PRINTS'], 0, 0
    OH = old('hook.py', 'hook_v1300l')
    cmd = 'python -X utf8 -u tools/b750_' + 'prepaths.py --bank'
    o, nw = OH.judge('Bash', {'command': cmd}, relay=RELAY), HK.judge('Bash', {'command': cmd})
    df = rdf('data/b750_defects.txt').split(NL)
    n += 1
    g += guard(L, 'limit', 'the instance found: b750 defect (t) (data/b750_defects.txt :26)', (df[25].strip()[:140] if len(df) > 25 else 'ABSENT'), len(df) > 25 and 'prepaths' in df[25])
    n += 1
    g += case(L, 'limit', 'b750`s probe-path run sent in the foreground with no limit', 'hook.py at %s: %s' % (BASE, o or 'let through; the host moved it to the background at 120 s'),
              nw or 'let through', o is None, bool(nw) and nw[0] == 'LIMIT' and '600000' in nw[1])
    ok3 = [HK.judge('Bash', {'command': cmd, 'timeout': 600000}), HK.judge('Bash', {'command': cmd, 'run_in_background': True}),
           HK.judge('Bash', {'command': 'python -c "print(\'tools/b750_' + 'prepaths.py\')"'})]
    n += 1
    g += guard(L, 'limit', 'the same run with timeout 600000, in the background, and a quoted mention of the route: let through', ok3, all(x is None for x in ok3))
    n += 1
    g += guard(L, 'limit', 'the table the tool prints (tools/standing/limits.py)', '%d routes, each %s ms' % (len(LI.LONG), sorted(set(ms for _w, _r, ms in LI.LONG))), len(LI.LONG) >= 9)
    return L, g, n


# ================================================================================ (instances) (3)(x): THE HOOK'S REFUSALS
def control_instances():
    L, g, n = ['### (instances) (R361)(3)(x), b750 defects (a), (g), (n), (q), (r), (v), (w), events (2), (4), (5), REPEAT: THE HOOK`S REFUSALS, THE INSTANCES PRINTED'], 0, 0
    kinds = ('PIPE', 'READ', 'SED', 'REDIR', 'ENV', 'LOCKED', 'WLIST', 'COMPOSER', 'LIMIT')
    for a in ('b750', A.current()['act']):
        rf = [l for l in rdf('data/%s_hook_refusals.txt' % a).split(NL) if l.strip()]
        n += 1
        g += guard(L, 'instances', 'printed: %s`s hook refusals, data/%s_hook_refusals.txt, by kind' % (a, a),
                   '%d rows: %s' % (len(rf), ', '.join('%s %d' % (k, sum(1 for l in rf if '| %s |' % k in l)) for k in kinds if any('| %s |' % k in l for l in rf))), bool(rf))
    df = rdf('data/b750_defects.txt').split(NL)
    for k, i in (('a', 6), ('g', 12), ('n', 19), ('q', 22), ('r', 23), ('v', 27), ('w', 28)):
        n += 1
        g += guard(L, 'instances', 'printed: b750 defect (%s), :%d' % (k, i + 1), (df[i].strip()[:130] if len(df) > i else 'ABSENT'), len(df) > i and df[i].strip().startswith('(%s)' % k))
    ev = rdf('data/b750_events.txt').split(NL)
    for k in ('(2)', '(4)', '(5)'):
        row = next((l.strip() for l in ev if l.strip().startswith(k + ' ')), '')
        n += 1
        g += guard(L, 'instances', 'printed: b750 events %s' % k, row[:130] or 'ABSENT', bool(row))
    return L, g, n


# ================================================================================ (version) (3)(xi)
def control_version():
    L, g, n = ['### (version) (R361)(3)(xi): THE STANDING VERSION PRINTED AND ITS CONTROLS TALLIED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = show(BASE, 'tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.30.0', ver == 'v1.31.0')
    return L, g, n


CONTROLS = dict(order=control_order, wlist=control_wlist, composer=control_composer, linematch=control_linematch, gatescan=control_gatescan,
                compile=control_compile, carry=control_carry, words=control_words, limit=control_limit, instances=control_instances, version=control_version)
ORDER = ('order', 'wlist', 'composer', 'linematch', 'gatescan', 'compile', 'carry', 'words', 'limit', 'instances', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.31.0, (R361)(3)(i)-(xi): THE PART-ORDER GUARD, THE (W) REFUSAL IN THE HOOK, THE COMPOSER ON EVERY PROMPT, '
           'THE LINE READER`S MATCH, THE SCAN AT THE GATE, THE COMPILED RENDER, THE CARRY, THE TOOL`S WORDS AND PHASES, THE HOST`S LIMIT, THE HOOK`S REFUSALS, '
           'THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
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
    out.append('### ### **v1.31.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1310.txt' % act), NL.join(out))
        print('written data/%s_standing_v1310.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
