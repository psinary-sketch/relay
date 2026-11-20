# -*- coding: utf-8 -*-
"""b764, (R374)(5): THE PLANTED CONTROLS OF THE REPAIRS, ONE A KEY. Each control reads the fault at the commit before the repair and reads
clean at the repair's commit, both printed ("WHAT A REPAIR MUST SHOW"). Read-only over the relay: each revision's files are taken by
`git show <rev>:<path>` into a scratch folder of the system's temporary directory (removed after), and each revision is probed in its own
interpreter (`python -I`), so no module of one revision is read by the other; the probe calls the revision's functions, writes nothing, and
prints one JSON line. --bank appends the reading to data/b764_repair_controls.txt beneath a head naming the key and both commits; nothing
else is written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b764_repair_controls.py <key> <before> <after> [--bank]
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = '\n'
ACT = 'b764'
BANK = os.path.join(D, 'b764_repair_controls.txt')


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def snapshot(rev, paths, dest):
    """the files `paths` at `rev` under dest, at their relay paths; [(path, present)]."""
    out = []
    for p in paths:
        rc, b = git('show', '%s:%s' % (rev, p))
        out.append((p, rc == 0))
        if rc == 0:
            q = os.path.join(dest, *p.split('/'))
            os.makedirs(os.path.dirname(q), exist_ok=True)
            with open(q, 'wb') as fh:
                fh.write(b)
    return out


def probe(code, snap, *args):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', code, snap] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    lines = [l for l in r.stdout.split(NL) if l.startswith('{')]
    if r.returncode != 0 or not lines:
        return dict(error='exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[-400:]))
    return json.loads(lines[-1])


# ================================================================================ [K10] STEP [21] AGAINST N4
K10_PATHS = ('tools/standing/act.py', 'tools/standing/append.py', 'tools/act_close.py', 'tools/standing/fold/record.tpl',
             'data/standing_clauses_v5.txt')
K10_PROBE = r'''
import json, os, sys
snap, act = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools'))
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import act as A
import act_close as AC
import append as AP
tpl = open(os.path.join(snap, 'tools', 'standing', 'fold', 'record.tpl'), encoding='utf-8').read()
i = tpl.find('def closeorder(')
route = tpl[i:tpl.find('\ndef ', i + 10)]
uses = 'close_order(' in route
steps = A.close_order() if (uses and hasattr(A, 'close_order')) else AC.close_steps_printed()
s21 = [s for s in steps if s[0] == 21]
bank = s21[0][2].replace('<act>', act) if s21 else None
kinds = dict(AP.KINDS)
print(json.dumps(dict(route_reads_close_order=uses, s21_words=s21[0][1] if s21 else None, s21_bank=bank,
                      appended=sorted(A.post_lock_appended(act)), appended_b763=sorted(A.post_lock_appended('b763')), kinds=kinds,
                      route_for_bank=bool(bank) and any('data/%s_%s.txt' % (act, v) == bank for v in kinds.values()),
                      sentence_does_not_keep='a bank the act does not keep' in tpl)))
'''


def n4_guard(p, appended, tracked, act):
    """N4's predicate over one path a commit after the lock touches, as tools/acts/b764.py :2541 writes it (the act's post-lock reader):
    the path not appended by design and either under tools/ or a bank of the act tracked at the lock commit."""
    return p not in appended and (p.startswith('tools/') or (p.startswith('data/%s_' % act) and p in tracked))


def control_k10(before, after):
    """[K10]: the close order's step [21] as the seat reads it, the bank it names put through N4's predicate over a planted commit after a
    planted lock (the act's events, defects and step-zero banks tracked at the lock), the route that writes that bank, and N4's own sentence.
    FAULT: the bank [21] names is one N4's predicate reads as an edit, or no tool writes it, or N4's sentence calls the post-seal bank one the
    act does not keep. CLEAN: none of these. The record instance beside it: b763's [21] commit d784c1da and the files it touched, tracked at
    b763's lock 88e06e13, through the same predicate (b763's N4 REFUTED)."""
    L, res = [], {}
    rc, files = git('show', '--name-only', '--format=', 'd784c1da')
    d784 = [x for x in files.decode('utf-8').split() if x.strip()]
    rc2, tr = git('ls-tree', '-r', '--name-only', '88e06e13')
    tracked63 = set(x for x in tr.decode('utf-8').split(NL) if x.strip())
    planted_tracked = set('data/%s_%s.txt' % (ACT, n) for n in ('events', 'defects', 'stepzero'))
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k10_')
        try:
            got = snapshot(rev, K10_PATHS, tmp)
            j = probe(K10_PROBE, tmp, ACT)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k10_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        bank = j['s21_bank']
        flagged = bool(bank) and n4_guard(bank, set(j['appended']), planted_tracked, ACT)
        rec = [p for p in d784 if n4_guard(p, set(j['appended_b763']), tracked63, 'b763')]
        fault = flagged or not j['route_for_bank'] or j['sentence_does_not_keep']
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    the closeorder route reads standing.act.close_order: %s' % j['route_reads_close_order'],
              '    step [21] as the seat reads it: %s (%s)' % ((j['s21_words'] or '')[:150], bank),
              '    the planted instance: a commit after a lock that tracked %s touches %s -- N4`s predicate reads it as an edit: %s' % (
                  ', '.join(sorted(planted_tracked)), bank, flagged),
              '    a tool writes that bank (tools/standing/append.py`s kinds %s): %s' % (sorted(j['kinds']), j['route_for_bank']),
              '    N4`s sentence calls the post-seal bank one the act does not keep: %s' % j['sentence_does_not_keep'],
              '    the record instance, b763`s [21] commit d784c1da (%s) against its lock 88e06e13: read as an edit %s' % (', '.join(d784), rec or 'NONE'),
              '    %s: %s' % (name, 'THE FAULT READ' if fault else 'CLEAN')]
        res[name] = fault
    return L, res.get('BEFORE') is True and res.get('AFTER') is False


# ================================================================================ [K1] THE VALUE NOT YET SET
K1_PATHS = ('tools/standing/toset.py', 'tools/standing/fold/checks.tpl', 'tools/standing/close.py')
K1_PROBE = r'''
import json, os, sys
snap = sys.argv[1]
st = os.path.join(snap, 'tools', 'standing')
rd = lambda *p: open(os.path.join(*p), encoding='utf-8').read()
tpl, cl = rd(st, 'fold', 'checks.tpl'), rd(st, 'close.py')
k = tpl.find('    for name, reads, pred, pos in arms:')
out = dict(has_toset=os.path.exists(os.path.join(st, 'toset.py')), runner_holds=k > 0 and 'standing.toset' in tpl[max(0, k - 3000):k]
           and 'WITHHELD, NOT RUN: STILL TO SET' in tpl[k:k + 1500], combine_counts="startswith('WITHHELD, NOT RUN')" in cl,
           seal_reads_held="e.get('held')" in cl and 'HELD, NOT RUN IN THE PRE-RUN' in cl, cases={})
if out['has_toset']:
    sys.path.insert(0, st)
    import toset as TS
    for case in ('planted764', 'record763'):
        c = TS.classify_text(rd(snap, case + '_worklist.py'))
        names = TS.code_names(compile(rd(snap, case + '_pred.py'), case, 'exec'), {})
        out['cases'][case] = dict(hit=sorted(names & set(n for n, (s, _w) in c.items() if s == 'TO SET')),
                                  corr=list(c.get('CORR_LINE') or ['BOUND']), weight=list(c.get('WEIGHT_LINE') or ['BOUND']))
print(json.dumps(out))
'''
K1_CORR_OLD = "CORR_LINE = None    # ### FINDINGS: the corrigendum for b763 (Component 1), set when written -- PLANTED by the control: b764's value as it stood"


def _git_text(rev, path):
    rc, b = git('show', '%s:%s' % (rev, path))
    return b.decode('utf-8') if rc == 0 else ''


def _override_after(module_text, arm):
    """the body of the first act-module override after the arm's tuple, as a function's source (its names alone are read)."""
    i = module_text.find("('%s'" % arm)
    a = module_text.find('#⟪OVERRIDE checks', i)
    b = module_text.find('#⟪END⟫', a)
    if i < 0 or a < 0 or b < 0:
        return 'def _none(S):\n    return None\n'
    return 'def _pred(S):\n' + module_text[module_text.find('\n', a) + 1:b]


def _plant_corr(w):
    """b764's worklist with CORR_LINE planted empty where it is bound to a value: a line `CORR_LINE = <value>` replaced by K1_CORR_OLD."""
    ls = w.split('\n')
    for j, l in enumerate(ls):
        if l.startswith('CORR_LINE = ') and not l.startswith('CORR_LINE = None'):
            ls[j] = K1_CORR_OLD
    return '\n'.join(ls)


def control_k1(before, after):
    """[K1]: a worklist constant still to set told apart from one the ruling leaves empty, and the part runner holding an arm that names one.
    The planted instance: b764's worklist at the revision, CORR_LINE planted empty where the revision binds it, with the G-DIFFERS-ERRATA
    predicate of b764's act module at the revision; the record instance: b763's worklist and act module at the commit before 6dc04ffb, where
    CORR_LINE stood None and its probe failed the arm (data/b763_events.txt :723-:729). FAULT: no reader tells the two apart, or the part
    runner runs the arm on a constant still to set, or the combine or the seal does not read the held row. CLEAN: the reader present, the
    runner holding before its arm loop, the combine and the seal reading it, CORR_LINE among the planted arm's constants still to set and
    WEIGHT_LINE read as left empty by its clause."""
    L, res = [], {}
    rec763 = ('6dc04ffb^', _git_text('6dc04ffb^', 'tools/b763_worklist.py'), _override_after(_git_text('6dc04ffb^', 'tools/acts/b763.py'), 'G-DIFFERS-ERRATA'))
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k1_')
        try:
            got = snapshot(rev, K1_PATHS, tmp)
            for case, w, pr in (('planted764', _plant_corr(_git_text(rev, 'tools/b764_worklist.py')),
                                 _override_after(_git_text(rev, 'tools/acts/b764.py'), 'G-DIFFERS-ERRATA')), ('record763', rec763[1], rec763[2])):
                for suf, t in (('_worklist.py', w), ('_pred.py', pr)):
                    with open(os.path.join(tmp, case + suf), 'w', encoding='utf-8', newline='\n') as fh:
                        fh.write(t)
            j = probe(K1_PROBE, tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k1_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        pl, r3 = j['cases'].get('planted764') or {}, j['cases'].get('record763') or {}
        clean = (j['has_toset'] and j['runner_holds'] and j['combine_counts'] and j['seal_reads_held'] and 'CORR_LINE' in (pl.get('hit') or [])
                 and pl.get('weight', [None])[0] == 'EMPTY' and 'CORR_LINE' in (r3.get('hit') or []))
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    a reader telling a constant still to set from one left empty (tools/standing/toset.py): %s' % j['has_toset'],
              '    the part runner holds an arm naming a constant still to set before its arm loop (checks.tpl): %s' % j['runner_holds'],
              '    the combine counts a held row among the withheld (close.py combine_tally): %s ; the seal reads it HELD (close.py neg_shown): %s' % (
                  j['combine_counts'], j['seal_reads_held']),
              '    the planted instance, b764`s worklist at %s with CORR_LINE planted empty, G-DIFFERS-ERRATA`s predicate from tools/acts/b764.py: %s' % (
                  rev[:8], ('constants still to set it names %s ; CORR_LINE %s ; WEIGHT_LINE %s' % (pl.get('hit'), pl.get('corr'), pl.get('weight')))
                  if pl else 'NOT READ -- no reader: the arm runs on CORR_LINE None, nothing printed, WEIGHT_LINE and CORR_LINE on one line told apart by nothing'),
              '    the record instance, b763`s worklist :445 and act module at %s: %s' % (
                  rec763[0], ('constants still to set the arm names %s ; CORR_LINE %s' % (r3.get('hit'), r3.get('corr'))) if r3 else
                  'NOT READ -- no reader: its probe ran the arm on CORR_LINE None (06:23:04Z) and the failure read like any other'),
              '    %s: %s' % (name, 'CLEAN' if clean else 'THE FAULT READ')]
        res[name] = not clean
    return L, res.get('BEFORE') is True and res.get('AFTER') is False


# ================================================================================ [K5] A NEEDLE READ THROUGH ITS READER WHEN IT IS WRITTEN
K5_TOOL = 'tools/standing/needle.py'
K5_CASES = r'''
import json, os, sys
sys.path.insert(0, os.path.join(sys.argv[1], 'tools', 'standing'))
sys.path.insert(1, os.path.join(sys.argv[1], 'tools'))
import needle as N
snap = sys.argv[2]
rd = lambda n: open(os.path.join(snap, n), encoding='utf-8').read()
f_need = N.foot(rd('l_after.txt'))
l_before, l_after = N.foot_read(rd('l_before.txt'), [f_need]), N.foot_read(rd('l_after.txt'), [f_need])
p_rows = N.conv_read('**The author`s words** (relay data/b763_author_answers.txt)', ['**The author`s words**', '**The author’s words**'])
q_before, q_after = N.bar(rd('q_before.txt')), N.bar(rd('q_after.txt'))
print(json.dumps(dict(l_need=bool(f_need), l_before=l_before, l_after=l_after, p_rows=p_rows,
                      q_before=[len(q_before[0]), len(q_before[1]), q_before[3]], q_after=[len(q_after[0]), len(q_after[1]), q_after[3]])))
'''
K5_HEAD = '### b763 — lane two, act one hundred and ninety, The control’s failure from its coefficients under (R373)'
K5_CARRIED = '### b763 — lane two, act one hundred and eighty-nine, The re-cut of One Page under (R373)'
K5_Q_OLD = 'two arms failing beyond b762`s (defects (n), (o))'
K5_Q_NEW = 'G-WEIGHT-LINE and G-CLOSING-SENTENCE failing beyond b762`s (defects (n), (o))'


def control_k5(before, after):
    """[K5]: one call taking a needle and its reader and composing the text as the reader's route composes it. BEFORE: no such call at the
    revision, each of b763's five read by nothing until the part's probe or the gate's first run. AFTER (the working tree equal to the
    repair's commit for the call's file, read and printed): the call over b763's own instances, each wanted read --
    (l) the recut bank's foot before its repair (data/b763_recut_inputs.txt at 1d8b80a2, a bare bold foot) and after (9779a81f): the
        repaired foot's text does not stand in the first's foot, which reads empty, and stands in the second's;
    (p) the face's trail needle in the backtick form stands raw and not through conv, and the typographic form stands through conv;
    (q) b763's face paragraph as committed at 256c3e8d (tools/b763_face_blocks.txt, the Component 6 paragraph counting two arms) reads an
        arm miss through the gate's bar screen, and the same paragraph with the two arms named reads none;
    (n), (o) the arm route: `needle.py b764 arm G-PRIOR-CLOSED-PUSHED`, --dry, over three needles of b763's trail head -- as OPEN_TRAILS
        :18993 holds it (the apostrophe typographic), in the relay's backtick form, and as the carry left it (b762's head under b763's name)
        -- the arm run on b764's composed sources (PASS or FAIL, not RAISED), the first standing in the text the arm reads (S['ot']), the
        second and third not. The first run of this control (18:40:16Z) read b764's sources halting on the carried stub of the act module's
        checks section 60, which is this arm's needle; the second (18:41:45Z) read b763's suite refused by its root's guard ((R339)(2)(iii))
        for a closed act; section 60 written for b764 (the Edit tool) and the module committed before this case runs. Both readings kept."""
    L = []
    rc, b = git('show', '%s:%s' % (before, K5_TOOL))
    L += ['  BEFORE (relay %s): %s %s' % (before[:8], K5_TOOL, 'present' if rc == 0 else 'ABSENT'),
          '    no call reads a needle through its reader at its writing: b763`s (n) and (o) found at the standing-a2 probe (06:49:59Z), (p) and (q)'
          ' at the gate`s first run (08:22:02Z), (l) by hand at 05:21Z, each after the writing (data/b763_defects.txt :56-:111)',
          '    BEFORE: %s' % ('THE FAULT READ' if rc != 0 else 'CLEAN')]
    before_fault = rc != 0
    rc2, head = git('rev-parse', 'HEAD')
    rc3, blob = git('show', '%s:%s' % (after, K5_TOOL))
    work = open(os.path.join(ROOT, *K5_TOOL.split('/')), 'rb').read() if os.path.exists(os.path.join(ROOT, *K5_TOOL.split('/'))) else None
    same = rc3 == 0 and work is not None and work.replace(b'\r\n', b'\n') == blob.replace(b'\r\n', b'\n')
    L.append('  AFTER (relay %s): %s at the commit %s ; the working file its blob at the repair`s commit: %s (HEAD %s)' % (
        after[:8], K5_TOOL, 'present' if rc3 == 0 else 'ABSENT', same, head.decode().strip()[:8]))
    if not same:
        return L + ['    AFTER: NOT READ -- the call`s file is not the commit`s'], False
    tmp = tempfile.mkdtemp(prefix='b764k5_')
    try:
        qb = _git_text('256c3e8d', 'tools/b763_face_blocks.txt')
        para = [p for p in qb.split('\n\n') if K5_Q_OLD in p]
        for n_, t_ in (('l_before.txt', _git_text('1d8b80a2', 'data/b763_recut_inputs.txt')), ('l_after.txt', _git_text('9779a81f', 'data/b763_recut_inputs.txt')),
                       ('q_before.txt', para[0] if para else ''), ('q_after.txt', para[0].replace(K5_Q_OLD, K5_Q_NEW) if para else '')):
            with open(os.path.join(tmp, n_), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(t_)
        r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', K5_CASES, ROOT, tmp], capture_output=True, text=True, encoding='utf-8', errors='replace')
    finally:
        if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k5_'):
            shutil.rmtree(tmp, ignore_errors=True)
    js = [l for l in r.stdout.split(NL) if l.startswith('{')]
    if r.returncode or not js:
        return L + ['    THE CASES FAILED: exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[-400:])], False
    j = json.loads(js[-1])
    l_ok = j['l_need'] and not j['l_before']['rows'][0][1] and j['l_after']['rows'][0][1]
    p_ok = j['p_rows'][0][1] and not j['p_rows'][0][2] and j['p_rows'][1][2]
    q_ok = bool(para) and j['q_before'][1] >= 1 and j['q_after'][1] == 0
    t0 = time.time()
    nd = [K5_HEAD, K5_HEAD.replace('’', '`'), K5_CARRIED]
    a = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(ROOT, 'tools', 'standing', 'needle.py'), ACT, 'arm', 'G-PRIOR-CLOSED-PUSHED']
                       + nd + ['--dry'], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=560)
    out = a.stdout
    m = re.search(r'ON THE COMPOSED SOURCES: (PASS|FAIL|RAISED[^(]*)', out)
    rows = [w for w in re.findall(r' -- (STANDS|DOES NOT STAND)$', out, re.M)]
    n_ok = bool(m) and not m.group(1).startswith('RAISED') and rows == ['STANDS', 'DOES NOT STAND', 'DOES NOT STAND']
    L += ['    (l) the recut bank`s foot: the repaired foot`s text read %s ; at 1d8b80a2 a verdict line %s, the needle %s ; at 9779a81f a verdict line %s, the needle %s -- %s' % (
              j['l_need'], j['l_before']['foot_found'], 'STANDS' if j['l_before']['rows'][0][1] else 'DOES NOT STAND', j['l_after']['foot_found'],
              'STANDS' if j['l_after']['rows'][0][1] else 'DOES NOT STAND', 'AS WANTED' if l_ok else 'NOT AS WANTED'),
          '    (p) the trail needle: backtick form raw %s, through conv %s ; typographic form through conv %s -- %s' % (
              j['p_rows'][0][1], j['p_rows'][0][2], j['p_rows'][1][2], 'AS WANTED' if p_ok else 'NOT AS WANTED'),
          '    (q) b763`s face paragraph at 256c3e8d (found %s): arm misses %d (multi-arm paragraphs %d) ; with the two arms named: arm misses %d -- %s' % (
              bool(para), j['q_before'][1], j['q_before'][2], j['q_after'][1], 'AS WANTED' if q_ok else 'NOT AS WANTED'),
          '    (n), (o) the arm route, G-PRIOR-CLOSED-PUSHED on b764`s composed sources (exit %d, %.0f s): %s ; the needles (landed form, backtick'
          ' form, as carried) %s -- %s' % (a.returncode, time.time() - t0, m.group(1).strip() if m else 'NO VERDICT LINE',
                                         rows or (a.stderr or out).strip()[-300:], 'AS WANTED' if n_ok else 'NOT AS WANTED')]
    clean = l_ok and p_ok and q_ok and n_ok
    L.append('    AFTER: %s' % ('CLEAN' if clean else 'THE FAULT READ'))
    return L, before_fault and clean


# ================================================================================ [K8] THE ANSWER IN THE NEXT, CARRIED-TO AND RESOLVED LINES
K8_PATHS = ('tools/standing/nextact.py', 'tools/standing/fold/record.tpl', 'tools/standing/fold/checks.tpl', 'tools/b703_record.py',
            'data/b763_author_answers.txt')
K8_PP = 'D:/MY-DOwnloads/PLACE-papers'
K8_LINES = (('carried.txt', 'FINDINGS.md', 15857, '9d0d63ea8682be6c'), ('next.txt', 'FINDINGS.md', 15859, 'b4d0dbfd1a6cc874'),
            ('trail_next.txt', 'OPEN_TRAILS.md', 19051, 'cc2fb63cfaef7b51'), ('resolved.txt', 'OPEN_TRAILS.md', 19045, '6bafcbb72a0773b3'))
K8_PROBE = r'''
import ast, json, os, sys
snap, inst = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import nextact as N
rd = lambda p: open(p, encoding='utf-8').read()
tpl = rd(os.path.join(snap, 'tools', 'standing', 'fold', 'record.tpl'))
chk = rd(os.path.join(snap, 'tools', 'standing', 'fold', 'checks.tpl'))
src = rd(os.path.join(snap, 'tools', 'b703_record.py'))
NUM = ast.literal_eval([n for n in ast.parse(src).body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'NUM'][0].value)
nw = lambda n: NUM[n] if 0 <= n < len(NUM) else str(n)
w = N.word('b763')
want = ('relay data/b763_author_answers.txt :%d, %s' % w) if w else None
car, nxt, trl = (rd(os.path.join(inst, n)).strip('\n') for n in ('carried.txt', 'next.txt', 'trail_next.txt'))
ent = N.entry('b763', car + '\n\n' + nxt)
e_car, e_next = ent.split('\n')[0], ent.split('\n')[2]
wrap = 'NXA7.trail(ACT' in tpl and hasattr(N, 'trail')
t_next = N.trail('b763', trl) if wrap else trl
i = tpl.find('def _for_author():')
fa = tpl[i:tpl.find('\ndef ', i + 10)]
cwf = getattr(N, 'count_word', None)
composes = 'count_word(len(nav))' in fa and 'num_word(len(nav))' not in fa
words = [cwf(0, 'b764', nw), cwf(0, 'b763', nw), cwf(17, 'b764', nw)] if (cwf and composes) else [nw(0), nw(0), nw(17)]
readers = 'wr = (count_word(' in tpl and 'count_word(n_, a_' in chk
print(json.dumps(dict(answer=w, carried=bool(want) and want in e_car, next=bool(want) and want in e_next, trail_wrap=wrap,
                      trail=bool(want) and want in t_next, composes=composes, words=words, num17=nw(17), readers=readers,
                      idem=N.entry('b763', ent) == ent and (N.trail('b763', t_next) == t_next if wrap else True))))
'''


def control_k8(before, after):
    """[K8]: b763's own landed lines, as its sealed composition wrote them (PLACE-papers 7db9a66c: the entry's Carried to line FINDINGS :15857
    and Next line :15859, the trail's Next line OPEN_TRAILS :19051, each read by line and sha256, no text printed), read through each
    revision's composition with b763's answers bank (data/b763_author_answers.txt, the author's choice at :8): the entry's two lines through
    nextact.entry(), the trail's through the template's wrap where the revision has one, and the Resolved line's count word for a count of 0
    through _for_author() as the revision's template composes it (b763's item (14), OPEN_TRAILS :19045, "the none navigator misses").
    FAULT: the answer and its bank absent from a line, or the count of 0 composed "none" for b764. CLEAN: the answer and its bank in each of the
    three lines, read twice and read once; "zero" for b764, "none" for b763 as landed, num_word's word for any other count; the dry check's
    reader and the suite's arm reading the same word."""
    L, res = [], {}
    inst = tempfile.mkdtemp(prefix='b764k8i_')
    try:
        shas = []
        for fn, path, ln, sha in K8_LINES:
            r = subprocess.run(['git', '-C', K8_PP, 'show', '7db9a66c:%s' % path], capture_output=True)
            l_ = r.stdout.decode('utf-8').replace('\r', '').split(NL)[ln - 1] if r.returncode == 0 else ''
            got = __import__('hashlib').sha256(l_.encode('utf-8')).hexdigest()[:16]
            shas.append((path, ln, got, got == sha))
            with open(os.path.join(inst, fn), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(l_)
        item14 = '(14) the none navigator misses' in io.open(os.path.join(inst, 'resolved.txt'), encoding='utf-8').read()
        L.append('  THE RECORD INSTANCES (PLACE-papers 7db9a66c, by line and sha256): %s ; b763`s item (14) reads "the none navigator misses": %s' % (
            '; '.join('%s :%d %s %s' % (p, n, s, 'EQUAL' if ok else 'DIFFERS') for p, n, s, ok in shas), item14))
        for name, rev in (('BEFORE', before), ('AFTER', after)):
            tmp = tempfile.mkdtemp(prefix='b764k8_')
            try:
                got = snapshot(rev, K8_PATHS, tmp)
                j = probe(K8_PROBE, tmp, inst)
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k8_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
                res[name] = None
                continue
            clean = bool(j['answer']) and j['carried'] and j['next'] and j['trail_wrap'] and j['trail'] and j['composes'] \
                and j['words'] == ['zero', 'none', j['num17']] and j['readers'] and j['idem']
            fault = (not j['carried']) or (not j['next']) or (not j['trail']) or j['words'][0] != 'zero'
            L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
                  '    b763`s answers bank read by word(): %s' % (('line %d, %s' % tuple(j['answer'])) if j['answer'] else 'NONE'),
                  '    the entry`s Carried to line carries the bank and the answer: %s ; the entry`s Next line: %s' % (j['carried'], j['next']),
                  '    the template binds the trail through nextact`s trail(): %s ; the trail`s Next line carries the bank and the answer: %s' % (
                      j['trail_wrap'], j['trail']),
                  '    _for_author() composes the count through count_word(): %s ; the count words (0 at b764, 0 at b763, 17 at b764): %s ; the dry check`s'
                  ' reader and the arm read it: %s ; read twice, read once: %s' % (j['composes'], j['words'], j['readers'], j['idem']),
                  '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
            res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    finally:
        if os.path.isabs(inst) and os.path.basename(inst).startswith('b764k8i_'):
            shutil.rmtree(inst, ignore_errors=True)
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and all(ok for _p, _n, _s, ok in shas)


# ================================================================================ [K15] THE LIMITS: ROOT PART 1
K15_PATHS = ('tools/standing/repeat.py', 'tools/standing/rootparts.py')
K15_LIVE = r'''
import json, sys
sys.path.insert(0, 'D:/relay/tools/standing')
sys.path.insert(1, 'D:/relay/tools')
sys.argv = ['fold.py', 'record']
import standing.repeat as RP
calls = [0]
orig = RP.committed_root
def counted(R):
    calls[0] += 1
    return orig(R)
RP.committed_root = counted
import fold as F
F.install()
M = F.load('b764', 'record')
f, n = M.R.rootbanks, 0
while hasattr(f, 'first'):
    n += 1
    f = f.first
print(json.dumps(dict(calls=calls[0], layers=n, innermost='%s:%d' % (f.__code__.co_filename.replace('\\', '/').split('/tools/')[-1], f.__code__.co_firstlineno))))
'''
K15_PROBE = r'''
import json, os, sys, types
snap, n = sys.argv[1], int(sys.argv[2])
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import repeat as RP
src = open(os.path.join(snap, 'tools', 'standing', 'rootparts.py'), encoding='utf-8').read()
reads = [0]
R = types.ModuleType('R_standin')
R.root_banks = lambda: ['data/x.txt']
def state(banks):
    reads[0] += 1
    return dict(rows=[dict(bank=b, status='clean', equal=True) for b in banks], pushed=True)
R.root_banks_state = state
def rootbanks(*a):
    state(R.root_banks())
    return True
R.rootbanks = rootbanks
for _ in range(n):
    RP.committed_root(R)
f, layers = R.rootbanks, 0
while hasattr(f, 'first'):
    layers += 1
    f = f.first
reads[0] = 0
R.rootbanks.first()
in_first = reads[0]
reads[0] = 0
R.rootbanks()
print(json.dumps(dict(layers=layers, in_first=in_first, whole=reads[0], guard='GUARD_S = 590' in src and "guard_line('1'" in src and "guard_line('2'" in src
                      and "guard_line('3'" in src and "row['under_guard']" in src)))
'''


def control_k15(before, after):
    """[K15]: root part 1, the first reading of the root route. The record route loads b764's record module, whose import chain renders the
    template line calling standing.repeat.committed_root(R) once for each act's record module, R b698's one module: the number of calls read
    live at the working tree (its two files the repair's commit's, read and printed). Each revision's repeat.py then wraps a stand-in R that
    many times, and its first reading -- root part 1 -- is run, counting the readings of every named bank it makes; rootparts.py read for the
    part's seconds against the 590 s guard and the 600 s limit. The record instance: b762's and b763's parts banks, part 1 against the guard,
    beside the layers each act's load made (one a record module from b721: 42 and 43). FAULT: part 1 reads the banks more than once (its
    seconds the reading's times the layers, past the guard at b763), or no part reads its seconds against the guard. CLEAN: one wrapper, part 1
    one reading and the route whole two (the reading, its writes, the reading after), each part's seconds read against the guard and banked."""
    L, res = [], {}
    rec = []
    for a in ('b762', 'b763'):
        pj = json.load(open(os.path.join(D, '%s_root_banks_parts.json' % a), encoding='utf-8'))
        s1 = float(pj['parts']['1']['seconds'])
        rec.append((a, s1, int(a[1:]) - 720))
    per = rec[1][1] / rec[1][2]
    L.append('  THE RECORD INSTANCE: %s ; one reading at b763 by its part 1 and its layers %.1f s' % (
        '; '.join('%s part 1 %.1f s at %d layers, under the 590 s guard %s, under the 600 s limit %s' % (a, s, k, s < 590, s < 600) for a, s, k in rec), per))
    same = []
    for p in K15_PATHS:
        rc, blob = git('show', '%s:%s' % (after, p))
        work = open(os.path.join(ROOT, *p.split('/')), 'rb').read()
        same.append(rc == 0 and work.replace(b'\r\n', b'\n') == blob.replace(b'\r\n', b'\n'))
    t0 = time.time()
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', K15_LIVE], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=560)
    js = [l for l in r.stdout.split(NL) if l.startswith('{')]
    live = json.loads(js[-1]) if (r.returncode == 0 and js) else None
    L.append('  THE LIVE LOAD at the working tree (its %s the repair`s commit`s: %s ; %.0f s): %s' % (
        ' and '.join(K15_PATHS), all(same), time.time() - t0,
        ('committed_root called %d times, layers over R.rootbanks %d, the innermost %s' % (live['calls'], live['layers'], live['innermost'])) if live
        else 'FAILED: exit %d %s' % (r.returncode, (r.stderr or r.stdout).strip()[-300:])))
    if not live or not all(same):
        return L + ['  NOT READ: the live load failed or the working files are not the commit`s'], False
    n = live['calls']
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k15_')
        try:
            got = snapshot(rev, K15_PATHS, tmp)
            j = probe(K15_PROBE, tmp, str(n))
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k15_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        proj = j['in_first'] * per
        fault = j['in_first'] > 1 or proj >= 590 or not j['guard']
        clean = j['layers'] == 1 and j['in_first'] == 1 and j['whole'] == 2 and j['guard']
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    a stand-in R wrapped %d times, as the load calls it: layers %d ; part 1, the first reading, reads the banks %d time(s), the route'
              ' whole %d ; part 1 at b763`s %.1f s a reading: %.0f s, under the 590 s guard %s' % (n, j['layers'], j['in_first'], j['whole'], per, proj, proj < 590),
              '    each part`s seconds read against the 590 s guard and the 600 s limit and banked (rootparts.py): %s' % j['guard'],
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    ok = res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and live['layers'] == 1
    return L, ok


# ================================================================================ [K16] THE PARTS THAT PASS BY READING NOTHING
K16_PATHS = ('tools/standing/remotecache.py', 'tools/standing/lsrread.py', 'tools/standing/fold/checks.tpl', 'tools/standing/close.py')
K16_PROBE = r'''
import ast, json, os, re, sys
snap, inst = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import remotecache as RC
import lsrread as L
rd = lambda p: open(p, encoding='utf-8').read()
parts = json.load(open(os.path.join(inst, 'parts.json'), encoding='utf-8'))
pr = getattr(L, 'part_read', None)
verdicts = dict((p, (pr(c, ev)[0] if pr else ('PASS AS A PART' if c != 'FAIL' else 'FAIL'))) for p, c, ev in parts)
log = {}
w = RC.wrap(lambda p: {}, 'b764-k16-control-standin-no-cache', log)
w('X:/a-remote-answering-nothing')
cl = L.classify({'X:/a-remote-answering-nothing': 1}, log)['X:/a-remote-answering-nothing'][0]
vd = L.verdict({'X:/a-remote-answering-nothing': 1}, log)
empty_part = pr(vd[0], vd[1])[0] if pr else ('PASS AS A PART' if vd[0] != 'FAIL' else 'FAIL')
chk = rd(os.path.join(snap, 'tools', 'standing', 'fold', 'checks.tpl'))
suite = 'LSRD.part_read(lsv[0], lsv[1], EX, W)' in chk and 'part_read=PRD[0]' in chk and 'PARTS NOT READ %d, COUNTED APART FROM A PASS' in chk
src = rd(os.path.join(snap, 'tools', 'standing', 'close.py'))
node = [n for n in ast.parse(src).body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'VERDICT_LINE'][0]
ns = dict(re=re)
exec(compile(ast.Module(body=[node], type_ignores=[]), 'close_VERDICT_LINE', 'exec'), ns)
m = ns['VERDICT_LINE'].search('  ### ### **VERDICT : ALL ARMS PASS AND EVERY CONTROL BEHAVES ; PARTS NOT READ, COUNTED APART FROM A PASS: 6**')
print(json.dumps(dict(verdicts=verdicts, empty=[cl, vd[0], empty_part], suite=suite, reader=bool(m) and m.group(1).strip() == 'ALL ARMS PASS AND EVERY CONTROL BEHAVES')))
'''


def control_k16(before, after):
    """[K16]: b763's own parts by their banked remote reads (data/b763_lsr_prerun_<part>.json, the pre-run's ten parts, each class as banked:
    standing-c, b2b, b2c, b2d and b3 CACHED, standing-b1 NONE), each given its part's verdict by the revision's reader; a stand-in remote
    answering no branch read through the revision's run cache and its classes (post-push standing-b2a's case, events (21)); the suite's part
    runner and combine, and the verdict reader of close.py, read at the revision. FAULT: a part reading nothing passes as a part (no part
    verdict), or the empty answer is classed READ. CLEAN: the six parts reading nothing NOT READ and the four reading READ, the empty answer
    EMPTY and its part NOT READ, the suite printing and banking each part's verdict and counting NOT READ apart from a pass, and the verdict
    line with that count read back."""
    L, res = [], {}
    parts = []
    for p in ('act', 'standing-a1', 'standing-a2', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b2c', 'standing-b2d', 'standing-b3', 'standing-c'):
        j = json.load(open(os.path.join(D, 'b763_lsr_prerun_%s.json' % p), encoding='utf-8'))
        parts.append((p, j.get('classed'), j.get('events') or []))
    want_nr = sorted(p for p, c, _e in parts if c in ('CACHED', 'NONE'))
    L.append('  THE RECORD INSTANCE: b763`s pre-run parts by their banked classes (data/b763_lsr_prerun_<part>.json): %s' % ', '.join('%s %s' % (p, c) for p, c, _e in parts))
    inst = tempfile.mkdtemp(prefix='b764k16i_')
    try:
        with open(os.path.join(inst, 'parts.json'), 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(parts, fh)
        for name, rev in (('BEFORE', before), ('AFTER', after)):
            tmp = tempfile.mkdtemp(prefix='b764k16_')
            try:
                got = snapshot(rev, K16_PATHS, tmp)
                j = probe(K16_PROBE, tmp, inst)
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k16_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
                res[name] = None
                continue
            nr = sorted(p for p, v in j['verdicts'].items() if v == 'NOT READ')
            rd_ = sorted(p for p, v in j['verdicts'].items() if v == 'READ')
            fault = any(j['verdicts'][p] != 'NOT READ' for p in want_nr) or j['empty'][0] != 'EMPTY'
            clean = nr == want_nr and len(rd_) == len(parts) - len(want_nr) and j['empty'] == ['EMPTY', 'EMPTY', 'NOT READ'] and j['suite'] and j['reader']
            L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
                  '    the parts` own verdicts: NOT READ %s ; READ %d ; others %s' % (nr or 'NONE', len(rd_),
                                                                                   sorted('%s %s' % (p, v) for p, v in j['verdicts'].items() if v not in ('READ', 'NOT READ')) or 'NONE'),
                  '    a remote answering no branch: classed %s, the part`s reads %s, the part %s' % tuple(j['empty']),
                  '    the suite prints and banks each part`s verdict and the combine counts NOT READ apart from a pass: %s ; the verdict line with the count read back: %s' % (
                      j['suite'], j['reader']),
                  '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
            res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    finally:
        if os.path.isabs(inst) and os.path.basename(inst).startswith('b764k16i_'):
            shutil.rmtree(inst, ignore_errors=True)
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K7] THE CLAUSE READER, THE NAME AFTER ITS PATH
K7_PATHS = ('tools/standing/cites.py', 'tools/standing/act.py')
K7_TREES_B763 = [['D:/SIDE-explicit-formula', 'a3aad4cc'], ['D:/SIDE-dirichlet-mod-24', 'e5ebdd15']]   # tools/b763_worklist.py :392
K7_TREES_B764 = [['D:/SIDE-explicit-formula', '819e4a83'], ['D:/SIDE-explicit-formula', 'ec14e9d9'], ['D:/SIDE-explicit-formula', 'a59632eb'],
                 ['D:/SIDE-dirichlet-mod-24', 'e5ebdd15']]   # tools/b764_worklist.py :406-:407
K7_WRONG = 'a stand-in sentence, Schema/Wide/HalfScaleControl.lean at wide_detector, read by no route\n'
K7_WORD = 'a stand-in sentence, SIDEExplicitFormula/H2Sign.lean at the line it names, read by no route\n'
K7_PROBE = r'''
import json, os, sys
snap, inst = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import cites as C
j = json.load(open(inst, encoding='utf-8'))
out = {}
for key, text, trees in j:
    rows = C.lean_rows(text, [tuple(t) for t in trees])
    out[key] = [[r[0], r[1], r[2], bool(r[3])] for r in rows]
print(json.dumps(out))
'''


def control_k7(before, after):
    """[K7]: b763's ferry whole under b763's trees (tools/b763_worklist.py :392), where SCOPE READ's "Schema/Wide/HalfScale.lean at
    wide_detector, ..." (data/b763_ferry.txt :3) halted the check (data/b763_citation_check.txt :93); b764's ferry under b764's trees, which
    must read the same rows at both revisions; and two stand-ins under b763's trees: the name after a path that does not declare it, and a
    word after at that is no name. FAULT: b763's ferry reads a failing row on wide_detector, or the stand-in's wrong path goes unread.
    CLEAN: b763's ferry no failing row and wide_detector read at HalfScale.lean, the wrong path one failing row, the word no row, b764's
    rows equal to the revision before's."""
    L, res, got_ = [], {}, {}
    b763 = open(os.path.join(D, 'b763_ferry.txt'), encoding='utf-8').read()
    b764 = open(os.path.join(D, 'b764_ferry.txt'), encoding='utf-8').read()
    L.append('  THE RECORD INSTANCE: data/b763_ferry.txt whole (%d lines) under b763`s trees %s; data/b764_ferry.txt whole (%d lines) under b764`s %s' % (
        b763.count(NL), ', '.join(r for _p, r in K7_TREES_B763), b764.count(NL), ', '.join(r for _p, r in K7_TREES_B764)))
    L.append('  THE STAND-INS, under b763`s trees: %r ; %r' % (K7_WRONG.strip(), K7_WORD.strip()))
    tmpi = tempfile.mkdtemp(prefix='b764k7i_')
    try:
        inst = os.path.join(tmpi, 'inst.json')
        with open(inst, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump([['b763', b763, K7_TREES_B763], ['b764', b764, K7_TREES_B764], ['wrong', K7_WRONG, K7_TREES_B763], ['word', K7_WORD, K7_TREES_B763]], fh)
        for name, rev in (('BEFORE', before), ('AFTER', after)):
            tmp = tempfile.mkdtemp(prefix='b764k7_')
            try:
                got = snapshot(rev, K7_PATHS, tmp)
                j = probe(K7_PROBE, tmp, inst)
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k7_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
                res[name] = None
                continue
            got_[name] = j
            f763 = [r for r in j['b763'] if not r[3]]
            wide = [r for r in j['b763'] if 'wide_detector' in r[1]]
            fwr = [r for r in j['wrong'] if not r[3]]
            nword = [r for r in j['word'] if not r[1].endswith('.lean')]
            f764 = [r for r in j['b764'] if not r[3]]
            fault = any('wide_detector' in r[1] for r in f763) or not fwr
            clean = (not f763 and any(r[1].startswith('wide_detector at Schema/Wide/HalfScale.lean') and r[3] for r in wide) and len(fwr) == 1
                     and not nword and not f764)
            L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
                  '    b763`s ferry: rows %d ; failing %d %s' % (len(j['b763']), len(f763), ['%s %s | %s' % (r[0], r[1], r[2]) for r in f763] or ''),
                  '    the rows on wide_detector: %s' % (['%s %s | %s | %s' % (r[0], r[1], r[2], 'OK' if r[3] else 'FAILING') for r in wide] or 'NONE'),
                  '    the stand-in, the name after a path that does not declare it: %s' % (['%s | %s | %s' % (r[1], r[2], 'OK' if r[3] else 'FAILING') for r in j['wrong'] if not r[1].endswith('.lean')] or 'NO ROW, UNREAD'),
                  '    the stand-in, a word after at: name rows %d' % len(nword),
                  '    b764`s ferry: rows %d ; failing %d' % (len(j['b764']), len(f764)),
                  '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
            res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    finally:
        if os.path.isabs(tmpi) and os.path.basename(tmpi).startswith('b764k7i_'):
            shutil.rmtree(tmpi, ignore_errors=True)
    same764 = 'BEFORE' in got_ and 'AFTER' in got_ and got_['BEFORE']['b764'] == got_['AFTER']['b764']
    L.append('  b764`s ferry, its rows at the two revisions equal: %s' % same764)
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and same764


# ================================================================================ [K17] THE PASS IN THE PREVIOUS ACT'S MODE
K17_PATHS = ('tools/standing/repeat.py', 'tools/standing/fold/checks.tpl')
K17_PAIRS = (('b761', 'b760'), ('b762', 'b761'), ('b763', 'b762'), ('b764', 'b763'))
K17_PROBE = r'''
import importlib.util, json, os, re, sys
snap, relay = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
sys.path.append(os.path.join(relay, 'tools'))   # the worklists import standing.carry (the live tree's, unchanged by the repair)
import repeat as RP
def load(a):
    sp = importlib.util.spec_from_file_location('wl_' + a, os.path.join(relay, 'tools', a + '_worklist.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m
pv = getattr(RP, 'prev_value', None)
def read(prev, own, n):
    if pv:
        return pv(prev, own, n)[0]
    return getattr(prev, n) if RP.prev_carries(prev, own, n) else getattr(own, n)
IDN = re.compile(r'^[a-z][a-z0-9_]*$')
def iskeyed(v):   # the class the repair names, fixed here alike for both revisions: pairs of strings keyed by distinct names of the chain's form
    if not (isinstance(v, (tuple, list)) and v and all(isinstance(r, (tuple, list)) and len(r) == 2 and isinstance(r[0], str) and isinstance(r[1], str) for r in v)):
        return False
    ks = [r[0] for r in v]
    return len(set(ks)) == len(ks) and all(IDN.match(k) for k in ks)
iskmap = lambda v: isinstance(v, dict) and bool(v) and all(isinstance(k, str) and IDN.match(k) for k in v)
pairs, moved = {}, {}
for own_a, prev_a in json.loads(sys.argv[3]):
    own, prev = load(own_a), load(prev_a)
    rows = []
    mv = []
    for n in sorted(k for k in vars(own) if k.upper() == k and not k.startswith('_')):
        o = getattr(own, n)
        try:
            if read(prev, own, n) != (getattr(prev, n) if RP.prev_carries(prev, own, n) else getattr(own, n)):
                mv.append(n)
        except Exception as e:
            mv.append('%s (%s)' % (n, type(e).__name__))
        if not (iskeyed(o) or iskmap(o)):
            continue
        v = read(prev, own, n)
        keys = [r[0] for r in o] if iskeyed(o) else list(o)
        try:
            got = dict(v)
        except Exception:
            got = {}
        miss = [k for k in keys if k not in got]
        p = getattr(prev, n, None)
        prefix = (not iskeyed(p)) or (not iskeyed(v)) or list(v)[:len(p)] == list(p) or list(v) == list(o)
        rows.append([n, miss, prefix])
    pairs['%s on %s' % (own_a, prev_a)] = rows
    moved['%s on %s' % (own_a, prev_a)] = mv
inst = {}
for own_a, prev_a, n, key in (('b762', 'b761', 'CHAIN', 'registration'), ('b761', 'b760', 'PP_CHAIN', 'pp_rulings'), ('b761', 'b760', 'PP_CHAIN', 'pp_cells'), ('b761', 'b760', 'PP_CHAIN', 'pp_epstein')):
    try:
        inst['%s on %s: dict(K.%s)[%r]' % (own_a, prev_a, n, key)] = 'FOUND %s' % dict(read(load(prev_a), load(own_a), n))[key][:8]
    except KeyError as e:
        inst['%s on %s: dict(K.%s)[%r]' % (own_a, prev_a, n, key)] = 'KeyError %s' % e
tpl = open(os.path.join(snap, 'tools', 'standing', 'fold', 'checks.tpl'), encoding='utf-8').read()
cause = None
i = tpl.find('def _k17_empty(')
j = tpl.find('_JL_OWN = None', i)
if i >= 0 and j > i:
    ns = {}
    exec(compile(tpl[i:j].replace('⟪ACT⟫', 'b764').replace('⟪PREV⟫', 'b763'), 'checks_k17', 'exec'), ns)
    log, base = [], {'a': '', 'b': 'x'}
    rs = ns['_RecS'](base, log)
    rs['a']; rs.get('b'); rs.get('c'); rs['z'] = 1
    c1 = ns['_prev_cause'](dict(raised="KeyError: 'registration'", trace=dict(worklist=[], state=[], banks=[])))
    c2 = ns['_prev_cause'](dict(raised=None, trace=dict(worklist=['CHAIN MERGED +registration'], state=[('fj', True), ('ot', False)], banks=['b763_x.txt'])))
    c3 = ns['_prev_cause'](dict(raised=None, trace=dict(worklist=[], state=[('ot', False)], banks=[])))
    cause = dict(log=log, write_through=base.get('z') == 1, c1=c1, c2=c2, c3=c3)
suite = ("pv['causes'] = dict((n_, _prev_cause(EX[n_]))" in tpl and "globals()['_K17_TRACE'] = dict(worklist=[], state=[], banks=[])" in tpl
         and 'EX[name].update(raised=raised_, trace=trace_)' in tpl and "THE CAUSE, %s: %s" in tpl and '_K17_RUN.add(w_)' in tpl)
print(json.dumps(dict(pairs=pairs, moved=moved, inst=inst, cause=cause, suite=suite)))
'''


def _k17_places():
    """b763's DIVERGE rows (its previous-mode a2 and act banks), each read by where its predicate is written at b763's close (d4ec1edb): the
    template or b763's act module, and the act's own literals its arm text names."""
    tpl = git('show', 'd4ec1edb:tools/standing/fold/checks.tpl')[1].decode('utf-8', 'replace')
    mod = git('show', 'd4ec1edb:tools/acts/b763.py')[1].decode('utf-8', 'replace')
    out = []
    for part, b in (('a2', 'b763_prevrun_standing-a2.txt'), ('act', 'b763_prevrun_act.txt')):
        t = open(os.path.join(D, b), encoding='utf-8').read()
        m = re.search(r"###   DIVERGE\s+(\d+) (\[.*?\])", t)
        arms = json.loads(m.group(2).replace("'", '"'))
        for a in arms:
            where = []
            for nm, src in (('template', tpl), ('act module', mod)):
                i = src.find("('%s'," % a)
                if i >= 0:
                    j = src.find("\n    ('G-", i + 1)
                    seg = src[i:j if j > 0 else i + 3000]
                    lit = len(re.findall(r'b763|\(R373\)', seg))
                    where.append('%s%s' % (nm, (', naming b763`s own text %d times' % lit) if lit else ''))
            out.append((part, a, ' and '.join(where) or 'NOT FOUND'))
    return out


def control_k17(before, after):
    """[K17]: the four act pairs b761 on b760 to b764 on b763, each worklist name of this act's that is a keyed table or a mapping read through
    the revision's --prev rule (repeat.prev_carries, and prev_value where it stands), every key of this act's sought in the table read; the two
    instances by name (b762 on b761, dict(K.CHAIN)['registration'], b763 events (19); b761 on b760, PP_CHAIN, b761 events (25)); the previous
    act's rows keeping their places; the cause of a DIVERGE row read from stand-in traces through the revision's template functions; and the
    suite's text. FAULT: a key of this act's not found (a KeyError), or no cause given. CLEAN: every key found in every pair, the prefix kept,
    the three stand-in causes RAISED, the three trace parts, and NONE OF THESE, the state read recorded and written through, the suite printing
    each row's cause. b763's 38 DIVERGE rows are printed by where each predicate is written (the record instance)."""
    L, res = [], {}
    pl = _k17_places()
    L.append('  THE RECORD INSTANCE: b763`s DIVERGE rows in its previous-mode pass (data/b763_prevrun_standing-a2.txt :133, 20; data/b763_prevrun_act.txt :59, 18),'
             ' each by where its predicate is written at b763`s close (d4ec1edb):')
    for part in ('a2', 'act'):
        rows_ = [(a, w) for p, a, w in pl if p == part]
        L.append('    %s: template %d, act module %d, both %d' % (part, sum(1 for _a, w in rows_ if w == 'template'), sum(1 for _a, w in rows_ if w.startswith('act module')),
                                                                    sum(1 for _a, w in rows_ if ' and ' in w)))
        L += ['      %-30s %s' % (a, w) for a, w in rows_]
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k17_')
        try:
            got = snapshot(rev, K17_PATHS, tmp)
            j = probe(K17_PROBE, tmp, ROOT, json.dumps(K17_PAIRS))
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k17_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        miss = dict((pr, [(n, m) for n, m, _p in rows if m]) for pr, rows in j['pairs'].items())
        nmiss = sum(len(m) for _n, m in sum(miss.values(), []))
        prefix = all(p for rows in j['pairs'].values() for _n, _m, p in rows)
        c = j['cause']
        cause_ok = bool(c) and c['log'] == [['a', True], ['b', False], ['c', True]] and c['write_through'] and c['c1'].startswith('RAISED KeyError') \
            and all(x in c['c2'] for x in ('THE WORKLIST READ AS', 'THE STATE READ EMPTY (1): fj', 'BANKS READ EMPTY (1): b763_x.txt')) and c['c3'].startswith('NONE OF THESE')
        moved_out = dict((pr, [n for n in mv if n not in [r[0] for r in j['pairs'][pr]]]) for pr, mv in j['moved'].items())
        fault = nmiss > 0 or not c
        clean = nmiss == 0 and prefix and cause_ok and j['suite'] and all(v.startswith('FOUND') for v in j['inst'].values()) and not any(moved_out.values())
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got))]
        for pr, rows in j['pairs'].items():
            L.append('    %s: keyed names %d %s ; keys of this act`s not found %s ; the previous act`s rows in place %s ; names read otherwise than prev_carries reads them %s (outside the keyed names %s)' % (
                pr, len(rows), [n for n, _m, _p in rows], ['%s %s' % (n, m) for n, m, _p in rows if m] or 'NONE', all(p for _n, _m, p in rows),
                j['moved'][pr] or 'NONE', moved_out[pr] or 'NONE'))
        L += ['    the instances: %s' % '; '.join('%s %s' % kv for kv in j['inst'].items()),
              '    the cause from a trace: %s' % (('RAISED: %r ; THE THREE PARTS: %r ; NONE: %r ; the state recorded %s, written through %s' % (
                  c['c1'], c['c2'], c['c3'], c['log'], c['write_through'])) if c else 'NO CAUSE GIVEN (the template holds no _prev_cause)'),
              '    the suite prints each DIVERGE and NOT RUN row`s cause from its live trace: %s' % j['suite'],
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K13] THE DESK ROUTE'S MARKER
K13_PATHS = ('tools/standing/fold/record.tpl',)
K13_PROBE = r'''
import contextlib, hashlib, io, json, os, sys
snap, tmpd = sys.argv[1], sys.argv[2]
tpl = open(os.path.join(snap, 'tools', 'standing', 'fold', 'record.tpl'), encoding='utf-8').read()
def standin_desk(*a):   # b698's desk in form: the bank written, nothing printed
    with open(os.path.join(tmpd, 'b764_desk_notes.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('=' * 104 + '\nb764 -- THE DESK.\n' + '=' * 104 + '\n\n  a stand-in row\n')
ns = dict(ROUTES=dict(desk=standin_desk), D=tmpd, ACT='b764', os=os, hashlib=hashlib)
i = tpl.find('_desk_route_composed = ROUTES.get(')
block = ''
if i >= 0:
    j = tpl.find("ROUTES['desk'] = _desk_route", i)
    block = tpl[i:j + len("ROUTES['desk'] = _desk_route")]
    exec(compile(block, 'record_k13', 'exec'), ns)
out = io.StringIO()
with contextlib.redirect_stdout(out):
    ns['ROUTES']['desk']()
lines = out.getvalue().split('\n')
at = next((k + 1 for k, l in enumerate(lines) if 'DESK' in l), None)
b = open(os.path.join(tmpd, 'b764_desk_notes.txt'), 'rb').read()
print(json.dumps(dict(block=bool(block), stdout=lines[:3], marker_at=at, bank_lines=b.count(b'\n'), bank_sha=hashlib.sha256(b).hexdigest()[:16])))
'''


def control_k13(before, after):
    """[K13]: the desk route through each revision's record template, its foot read and run with a stand-in of b698's desk (the bank written
    to a temporary folder, nothing printed) and the capture's marker DESK sought in its stdout as the capture seeks it, the first line holding
    it. The record instance: b761's to b763's desk banks, each opening "<act> -- THE DESK.", and b763's capture at 12:31:38Z (events (104):
    one empty line, the marker at no line). FAULT: the marker at no line. CLEAN: the marker on the route's line, its lines and sha256 those
    of the bank written."""
    L, res = [], {}
    for a in ('b761', 'b762', 'b763'):
        p = os.path.join(D, '%s_desk_notes.txt' % a)
        t = open(p, encoding='utf-8').read().split(NL) if os.path.exists(p) else []
        L.append('  THE RECORD INSTANCE: data/%s_desk_notes.txt, %d lines, its second line %r' % (a, len(t) - 1, t[1] if len(t) > 1 else None))
    L.append('  b763`s capture of the route (data/b763_events.txt (104), 12:31:38Z): exit 0, stdout one empty line, the marker DESK at no line')
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k13_')
        tmpd = tempfile.mkdtemp(prefix='b764k13d_')
        try:
            got = snapshot(rev, K13_PATHS, tmp)
            j = probe(K13_PROBE, tmp, tmpd)
        finally:
            for t_, pre in ((tmp, 'b764k13_'), (tmpd, 'b764k13d_')):
                if os.path.isabs(t_) and os.path.basename(t_).startswith(pre):
                    shutil.rmtree(t_, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        fault = j['marker_at'] is None
        clean = (j['marker_at'] is not None and j['block'] and ('%d lines' % j['bank_lines']) in j['stdout'][j['marker_at'] - 1]
                 and j['bank_sha'] in j['stdout'][j['marker_at'] - 1])
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    the template`s desk wrap present: %s ; the route`s stdout %r ; the marker DESK at line %s ; the stand-in bank %d lines, sha256 %s' % (
                  j['block'], j['stdout'], j['marker_at'], j['bank_lines'], j['bank_sha']),
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K12] close.py READS tools/mirror_prevbuild.json BY ITS CONTENT
K12_PATHS = ('tools/standing/close.py', 'tools/standing/controls.py')
K12_FILE = 'mirror_prevbuild.json'
K12_SEAL_COMMIT = '77a72b91'   # ### b763's seal commit (data/b763_steps.json), its blob of the file the one b763's seal hashed (5305bacb...)
K12_PROBE = r'''
import ast, hashlib, json, os, sys
snap, inst = sys.argv[1], sys.argv[2]
src = open(os.path.join(snap, 'tools', 'standing', 'close.py'), encoding='utf-8').read()
ctl = open(os.path.join(snap, 'tools', 'standing', 'controls.py'), encoding='utf-8').read()
blob = open(os.path.join(inst, 'blob.bin'), 'rb').read()
work = open(os.path.join(inst, 'work.bin'), 'rb').read()
sha = lambda b: hashlib.sha256(b).hexdigest()
class A:
    blobs = {}
    sha256_bytes = staticmethod(sha)
    blob = staticmethod(lambda rev, rel: A.blobs.get((rev, rel)))
    gs = staticmethod(lambda repo, *a: 'STANDIN-HEAD')
want = ('lf', 'blob_carries', 'seal_guard', 'seal_head')
nodes = [n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name in want]
ns = dict(A=A, os=os)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'close_k12', 'exec'), ns)
t = 'mirror_prevbuild.json'
g1 = ns['seal_guard']([t], rev='REV', read=lambda _t: work, at_rev=lambda _t: blob)
edited = (blob + b'{"an edit after its last commit": 1}\n').replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
g2 = ns['seal_guard']([t], rev='REV', read=lambda _t: edited, at_rev=lambda _t: blob)
A.blobs[('C1', 'tools/' + t)] = blob
h_work = ns['seal_head']({t: sha(work)}, ['C1'])
h_blob = ns['seal_head']({t: sha(blob)}, ['C1'])
h_edit = ns['seal_head']({t: sha(edited)}, ['C1'])
print(json.dumps(dict(defs=[n.name for n in nodes], g1_refused=[w for _t, w in g1['refused']], g1_line_ends=g1.get('line_ends'), g1_head=g1['head'],
                      g2_refused=[w for _t, w in g2['refused']], h_work=h_work, h_blob=h_blob, h_edit=h_edit,
                      controls_reads=('C.blob_carries(sealed(t)' in ctl))))
'''


def control_k12(before, after):
    """[K12]: the seal's guard and its replay, each revision's close.py functions (lf, blob_carries, seal_guard, seal_head, those it has) read
    by ast and run on a stand-in of act.py's three calls, over the record instance: tools/mirror_prevbuild.json's blob at b763's seal commit
    (LF, the bytes b763's seal hashed) and the file's live working bytes (CR LF, git status clean, as at b763's dry of 11:29:43Z). FAULT: the
    working file refused as edited after its last commit. CLEAN: it is read by its content and named among the line ends; a content edit
    (one line appended, written CR LF) still refused; the replay finds the commit whose blob carries the working bytes' sha256, the blob's
    own, and not an edit's; controls.py's (3ii) replay reads close.py's blob_carries."""
    L, res = [], {}
    rc, blob = git('show', '%s:tools/%s' % (K12_SEAL_COMMIT, K12_FILE))
    work = open(os.path.join(ROOT, 'tools', K12_FILE), 'rb').read()
    import hashlib
    sha = lambda b: hashlib.sha256(b).hexdigest()
    st = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--', 'tools/' + K12_FILE], capture_output=True, text=True).stdout
    acr = subprocess.run(['git', '-C', ROOT, 'config', '--get', 'core.autocrlf'], capture_output=True, text=True).stdout.strip()
    L += ['  THE RECORD INSTANCE: tools/%s at b763`s seal commit %s: %d bytes, CR %d, sha256 %s (data/b763_seal_hashes.json records %s)' % (
              K12_FILE, K12_SEAL_COMMIT, len(blob), blob.count(b'\r'), sha(blob)[:16],
              (json.load(open(os.path.join(D, 'b763_seal_hashes.json'), encoding='utf-8')).get('tools') or {}).get(K12_FILE, '?')[:16]),
          '    its working bytes: %d bytes, CR %d, sha256 %s ; equal to the blob with each CR LF read as LF: %s ; equal to the blob`s checkout form '
          '(each LF written CR LF): %s ; git status %r ; core.autocrlf %r' % (
              len(work), work.count(b'\r'), sha(work)[:16], work.replace(b'\r\n', b'\n') == blob, blob.replace(b'\n', b'\r\n') == work, st, acr)]
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k12_')
        inst = tempfile.mkdtemp(prefix='b764k12i_')
        try:
            got = snapshot(rev, K12_PATHS, tmp)
            for n_, b_ in (('blob.bin', blob), ('work.bin', work)):
                with open(os.path.join(inst, n_), 'wb') as fh:
                    fh.write(b_)
            j = probe(K12_PROBE, tmp, inst)
        finally:
            for t_, pre in ((tmp, 'b764k12_'), (inst, 'b764k12i_')):
                if os.path.isabs(t_) and os.path.basename(t_).startswith(pre):
                    shutil.rmtree(t_, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        fault = bool(j['g1_refused'])
        clean = (not j['g1_refused'] and j['g1_line_ends'] == [K12_FILE] and bool(j['g2_refused']) and j['h_work'] == 'C1'
                 and j['h_blob'] == 'C1' and j['h_edit'] is None and j['controls_reads'])
        L += ['  %s (relay %s): the files %s ; close.py`s functions read %s' % (
                  name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got), j['defs']),
              '    the working file (CR LF) against the blob: refused %s ; read by its content (line ends) %s ; the head %s' % (
                  j['g1_refused'] or 'NONE', j['g1_line_ends'], j['g1_head']),
              '    a content edit (one line appended, CR LF) against the blob: refused %s' % (j['g2_refused'] or 'NONE'),
              '    the replay over one commit carrying the blob: for the working bytes` sha256 %s ; for the blob`s own %s ; for the edit`s %s' % (
                  j['h_work'], j['h_blob'], j['h_edit']),
              '    controls.py`s (3ii) replay reads close.py`s blob_carries: %s' % j['controls_reads'],
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K11] THE ADDRESS SCAN AFTER THE LOCK, ITS PLACE AGAINST THE SEAL
K11_PATHS = ('tools/standing/act.py', 'tools/standing/commit.py', 'tools/act_close.py', 'data/standing_clauses_v5.txt')
K11_ACTS = ('b758', 'b759', 'b760', 'b761', 'b762', 'b763')
K11_PROBE = r'''
import ast, json, os, sys
snap, inst = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools'))
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import act as A
steps = A.close_order() if hasattr(A, 'close_order') else []
order = [str(s[0]) for s in steps]
s8a = [[str(s[0]), s[1][:120], s[2]] for s in steps if 'address scan' in s[1] or 'address_scan_postlock' in s[2]]
src = open(os.path.join(snap, 'tools', 'standing', 'commit.py'), encoding='utf-8').read()
tree = ast.parse(src)
fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'postlock_refusal']
run = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'run']
calls = bool(run) and any(isinstance(c, ast.Call) and getattr(c.func, 'id', '') == 'postlock_refusal' for c in ast.walk(run[0]))
cases = json.load(open(os.path.join(inst, 'cases.json'), encoding='utf-8'))
out = {}
if fn:
    ns = dict(RECORD={'seal': '%s_seal_hashes.json', 'lock': '%s_lockgate.json'}, os=os, sys=sys)
    exec(compile(ast.Module(body=fn, type_ignores=[]), 'commit_k11', 'exec'), ns)
    for name, c in sorted(cases.items()):
        read = (lambda c: lambda n: ({'at': c['at']} if n.endswith('_seal_hashes.json') else (c['bank'] if n.endswith('_address_scan_postlock.txt') else None)))(c)
        r = ns['postlock_refusal'](c['act'], read, c['staged'])
        out[name] = r[:160] if r else None
print(json.dumps(dict(order=order, s8a=s8a, defined=bool(fn), run_calls=calls, refusals=out)))
'''


def control_k11(before, after):
    """[K11]: the post-lock address scan's place against close.py's seal route and the seal commit. Each revision's close order as the seat
    reads it (standing.act.close_order over the v5 row) and the one-call tool's seal commit (commit.py's run and its postlock_refusal, read
    by ast and run on a stand-in reader) over the record instances, b758 to b763: each act's seal record time (data/<act>_seal_hashes.json),
    its post-lock bank's runs (data/<act>_address_scan_postlock.txt) and the names its seal commit staged (data/<act>_steps.json's seal row),
    with b763's order planted once more without its bank staged. FAULT: no step of the close order places the scan and the seal commit reads
    no place, so the orders of b758 to b760 (before the seal route) and of b761 to b763 (after it) pass alike without a word. CLEAN: step
    [8a] after [8] names the post-lock bank; the seal commit calls the refusal; b758, b759 and b760 refused, b761, b762 and b763 taken, b763
    without its bank staged refused."""
    import re as _re
    L, res, cases = [], {}, {}
    for a in K11_ACTS:
        sj = json.load(open(os.path.join(D, '%s_seal_hashes.json' % a), encoding='utf-8'))
        bank = open(os.path.join(D, '%s_address_scan_postlock.txt' % a), encoding='utf-8').read()
        st = json.load(open(os.path.join(D, '%s_steps.json' % a), encoding='utf-8'))
        rows = st.get('rows') if isinstance(st, dict) else st
        sc = [r['commit'] for r in rows if r.get('phase') == 'seal' and r.get('repo') == 'relay'][0]
        rc, nm = git('show', '--name-only', '--format=', sc)
        staged = [x for x in nm.decode('utf-8').split(NL) if x.strip()]
        runs = _re.findall(r'^## THE RUN AFTER THE LOCK, (\S+)', bank.replace('\r', ''), _re.M)
        cases[a] = dict(act=a, at=sj.get('at'), bank=bank, staged=staged)
        L.append('  THE RECORD INSTANCE %s: the seal record at %s ; the post-lock runs %s ; the seal commit %s staged %d names, the post-lock bank among them: %s' % (
            a, sj.get('at'), runs, sc[:8], len(staged), ('data/%s_address_scan_postlock.txt' % a) in staged))
    c = dict(cases['b763'])
    c['staged'] = [x for x in c['staged'] if x != 'data/b763_address_scan_postlock.txt']
    cases['b763 unstaged'] = c
    L.append('  THE PLANTED INSTANCE b763 unstaged: b763`s order with data/b763_address_scan_postlock.txt taken out of its seal commit`s names')
    want = {'b758': True, 'b759': True, 'b760': True, 'b761': False, 'b762': False, 'b763': False, 'b763 unstaged': True}
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k11_')
        inst = tempfile.mkdtemp(prefix='b764k11i_')
        try:
            got = snapshot(rev, K11_PATHS, tmp)
            with open(os.path.join(inst, 'cases.json'), 'w', encoding='utf-8') as fh:
                json.dump(cases, fh)
            j = probe(K11_PROBE, tmp, inst)
        finally:
            for t_, pre in ((tmp, 'b764k11_'), (inst, 'b764k11i_')):
                if os.path.isabs(t_) and os.path.basename(t_).startswith(pre):
                    shutil.rmtree(t_, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        o = j['order']
        placed = bool(j['s8a']) and '8a' in o and '8' in o and o.index('8a') == o.index('8') + 1 and j['s8a'][0][2] == 'data/<act>_address_scan_postlock.txt'
        refused = dict((k, v is not None) for k, v in j['refusals'].items())
        fault = not j['s8a'] and not (j['defined'] and j['run_calls'])
        clean = placed and j['defined'] and j['run_calls'] and refused == want
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    the close order as the seat reads it: %s' % ' '.join('[%s]' % x for x in o),
              '    the step that places the post-lock scan: %s' % (j['s8a'] or 'NONE'),
              '    the seal commit`s refusal defined %s ; called by run %s' % (j['defined'], j['run_calls']),
              '    each order at the seal commit: %s' % ('; '.join('%s %s' % (k, ('REFUSED: ' + v) if v else 'taken') for k, v in sorted(j['refusals'].items()))
                                                    if j['refusals'] else 'every order taken, no place read'),
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K2] THE CARRIED EXCEPTION AND ITS CITES
K2_PATHS = ('tools/standing/carry.py', 'tools/b764_carry.py', 'tools/b764_address_scan.py', 'data/b764_ferry.txt')
K2_SRC = ('d4ec1edb', 'tools/b763_address_scan.py')   # ### b763's record commit, the scan tool b764's step zero carried (16:55:54Z)
K2_PROBE = r'''
import ast, difflib, json, os, re, sys
snap, inst = sys.argv[1], sys.argv[2]
rd = lambda *p: open(os.path.join(snap, *p), encoding='utf-8').read()
src = open(os.path.join(inst, 'src.py'), encoding='utf-8').read().replace(chr(13), '')
subs = [tuple(x) for x in json.load(open(os.path.join(inst, 'subs.json'), encoding='utf-8'))]
car = rd('tools', 'standing', 'carry.py')
want = ('KEPT_BRANCH', 'DATAP', 'CITE_MOVED', 'substitute', 'shifted_absent', 'shifted_cites', 'cite_lines')
nodes = [n for n in ast.parse(car).body if (isinstance(n, ast.FunctionDef) and n.name in want)
         or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
ns = dict(re=re, difflib=difflib, NL=chr(10))
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'carry_k2', 'exec'), ns)
dst = ns['substitute'](src, subs)
absent = ns['shifted_absent'](src, dst, 'b764', lambda p: True) if 'shifted_absent' in ns else None
moved = ns['shifted_cites'](src, dst, 'b764') if 'shifted_cites' in ns else None
bc = rd('tools', 'b764_carry.py')
fn = [n for n in ast.parse(bc).body if isinstance(n, ast.FunctionDef) and n.name == '_carry']
bc_calls = bool(fn) and any(isinstance(c, ast.Call) and getattr(c.func, 'attr', '') == 'shifted_cites' for c in ast.walk(fn[0]))
sc = rd('tools', 'b764_address_scan.py')
ferry = rd('data', 'b764_ferry.txt')
snodes = [n for n in ast.parse(sc).body if (isinstance(n, ast.FunctionDef) and n.name in ('n5_line', 'exception_head'))
          or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'N5_CLAUSE')]
sns = dict(re=re, NL=chr(10))
exec(compile(ast.Module(body=snodes, type_ignores=[]), 'scan_k2', 'exec'), sns)
if 'exception_head' in sns:
    head = sns['exception_head']('b764', 'R374', sns['n5_line'](ferry), (), False)
else:
    i = sc.find("'## THE EXCEPTION, THE BYLINE UNDER I-23")
    head = 'COMPOSED INLINE IN scan(): ' + sc[i:sc.find('% RULING_N5', i)].replace(chr(10), ' ')[:400]
print(json.dumps(dict(dst_lines=dst.count(chr(10)), absent=None if absent is None else len(absent), moved=moved, b764_carry_calls=bc_calls,
                      head=head, literals_ferry_line=re.findall(r'data/b764_ferry\.txt :\d+', sc), literals_k=sc.count('b764 defect (k)'))))
'''


def control_k2(before, after):
    """[K2]: the carried exception and its cites. THE CARRY: b763's scan tool at b763's record commit carried to b764 by the substitution b764's
    step zero used (its pairs read from data/b764_carry_address_scan.txt :3), through each revision's tools/standing/carry.py (substitute,
    shifted_absent and, where it stands, shifted_cites, read by ast), and whether tools/b764_carry.py's _carry calls the new reader. THE SCAN:
    each revision's tools/b764_address_scan.py, its exception line composed over b764's ferry bank, and its literal cites of b764's ferry by a
    line and of b764's defect (k). The record instance: b764 defect (d) (the carried cites at :158, :179, :187, :196, :266 and :303 shifted from
    b763's). FAULT: the carry reads none of the shifted cites (shifted_absent 0, no other reader) and the scan's exception line carries the
    shifted letter. CLEAN: the carry lists them, the OWN among them b764's ferry at :145 and b764 defect (k); b764's carry route calls it; the
    exception line names N5 at the ferry's line read at run time (:157), no letter in it, the act arm's needle its prefix; no shifted literal."""
    L, res = [], {}
    rc, src = git('show', '%s:%s' % K2_SRC)
    head3 = open(os.path.join(D, 'b764_carry_address_scan.txt'), encoding='utf-8').read().split(NL)[2]
    m = re.search(r'substitution alone \(([^)]*)\)', head3)
    subs = [tuple(x.strip().split(' -> ')) for x in m.group(1).split(',')] if m else []
    ferry = open(os.path.join(D, 'b764_ferry.txt'), encoding='utf-8').read().split(NL)
    n5 = [i + 1 for i, l in enumerate(ferry) if '(N5)' in l]
    L += ['  THE RECORD INSTANCE: %s at %s (%d bytes), carried by the pairs %s (data/b764_carry_address_scan.txt :3); b764 defect (d) names the '
          'shifted cites at :158, :179, :187, :196, :266 and :303' % (K2_SRC[1], K2_SRC[0], len(src), subs),
          '    b764`s ferry bank: "(N5)" on lines %s; the clause opens at :%s ("(N5) nothing deposits")' % (n5, n5[-1] if n5 else None)]
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k2_')
        inst = tempfile.mkdtemp(prefix='b764k2i_')
        try:
            got = snapshot(rev, K2_PATHS, tmp)
            with open(os.path.join(inst, 'src.py'), 'wb') as fh:
                fh.write(src)
            with open(os.path.join(inst, 'subs.json'), 'w', encoding='utf-8') as fh:
                json.dump(subs, fh)
            j = probe(K2_PROBE, tmp, inst)
        finally:
            for t_, pre in ((tmp, 'b764k2_'), (inst, 'b764k2i_')):
                if os.path.isabs(t_) and os.path.basename(t_).startswith(pre):
                    shutil.rmtree(t_, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        mv = j['moved']
        own = [r for r in (mv or []) if r[2] == 'OWN']
        own_c = set(r[1] for r in own)
        fault = mv is None and 'b764 defect (k)' in j['head']
        clean = (mv is not None and {'data/b764_ferry.txt :145', 'b764 defect (k)'} <= own_c and len(own) >= 10 and j['b764_carry_calls']
                 and 'data/b764_ferry.txt :157' in j['head'] and 'defect (' not in j['head']
                 and j['head'].startswith('## THE EXCEPTION, THE BYLINE UNDER I-23: NONE TAKEN: R374`S N5')
                 and not j['literals_ferry_line'] and j['literals_k'] == 0)
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    THE CARRY: %d lines carried ; cites of an absent bank %s ; the cites the shift moved %s' % (
                  j['dst_lines'], j['absent'], ('%d, OWN %d' % (len(mv), len(own))) if mv is not None else 'NOT READ (no reader)')]
        L += ['      :%d %s %s (from %s)' % tuple(r) for r in (mv or [])]
        L += ['    tools/b764_carry.py`s _carry calls the reader: %s' % j['b764_carry_calls'],
              '    THE SCAN`S EXCEPTION LINE over b764`s ferry: %s' % j['head'][:330],
              '    the scan tool`s literal cites of b764`s ferry by a line %s ; of b764 defect (k) %d' % (j['literals_ferry_line'] or 'NONE', j['literals_k']),
              '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K3] THE KERNEL BASES BANK BY THE CARRY
K3_PATHS = ('tools/standing/carry.py', 'tools/standing/commit.py')
K3_ACTS = tuple('b%d' % n for n in range(756, 765))
K3_PROBE = r'''
import ast, io, json, os, re, sys
snap, inst = sys.argv[1], sys.argv[2]
rd_ = lambda *p: open(os.path.join(*p), encoding='utf-8').read()
car = rd_(snap, 'tools', 'standing', 'carry.py')
cm = rd_(snap, 'tools', 'standing', 'commit.py')
KERNELS = ast.literal_eval([n for n in ast.parse(cm).body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'KERNELS'][0].value)
tree = ast.parse(car)
want = ('KERNEL_CLAUSE', 'kernels_named', 'kernel_bases', 'rd')
nodes = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in want) or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in want)]
out = os.path.join(inst, 'out')
ns = dict(re=re, json=json, os=os, io=io, NL=chr(10), D=out)
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'carry_k3', 'exec'), ns)
mainf = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main']
calls = sum(1 for c in ast.walk(mainf[0]) if isinstance(c, ast.Call) and getattr(c.func, 'id', '') == 'kernel_bases') if mainf else 0
acts = json.load(open(os.path.join(inst, 'acts.json'), encoding='utf-8'))
res = {}
for a in sorted(acts):
    rec = acts[a]
    fer = rd_(inst, 'ferries', '%s_ferry.txt' % a)
    if 'kernel_bases' not in ns:
        res[a] = dict(named=None, written=None, lines=[])
        continue
    stub = dict((KERNELS[k], v) for k, v in (rec or {}).items())
    L, _b = ns['kernel_bases'](a, fer, KERNELS, bank_dir=out, main_of=lambda p, s=stub: s.get(p, '0123456789abcdef' * 2 + '01234567'))
    p = os.path.join(out, '%s_kernel_bases.json' % a)
    res[a] = dict(named=[k for k, _ in ns['kernels_named'](fer, sorted(KERNELS))], written=open(p, 'rb').read().decode('utf-8') if os.path.exists(p) else None, lines=L)
planted = None
if 'kernel_bases' in ns:
    p = os.path.join(out, 'b999_kernel_bases.json')
    with open(p, 'w', encoding='utf-8', newline=chr(10)) as fh:
        fh.write('{' + chr(10) + '  "SIDE-explicit-formula": "' + 'f' * 40 + '"' + chr(10) + '}' + chr(10))
    b0 = open(p, 'rb').read()
    L, _b = ns['kernel_bases']('b999', 'no kernel touched beyond SIDE-explicit-formula, and there one file', KERNELS, bank_dir=out, main_of=lambda q: 'e' * 40)
    planted = dict(kept=open(p, 'rb').read() == b0, lines=L)
print(json.dumps(dict(kernels=sorted(KERNELS), main_calls=calls, res=res, planted=planted)))
'''


def control_k3(before, after):
    """[K3]: the kernel bases bank written by the carry where the ruling names a kernel. Each revision's tools/standing/carry.py (its bank
    writer and reader, read by ast, the routes of main that call it) and commit.py (KERNELS) over the ferry banks of b756 to b764, each run
    in a scratch data folder with each kernel's main read as the act's bank on record holds it (a stand-in commit where none stands). The
    record instance: b763 defect (h), REPEAT b759 (b) (b763's first kernel commit refused at 20:31:38Z, "THE SCAN DID NOT READ THE KERNEL",
    the bank then written by the Write tool). FAULT: no route of the carry writes the bank, for any ruling that names a kernel. CLEAN: the
    kernels read from each ruling are the kernels of its bank on record; the bank written equals the bank on record byte for byte (b757,
    b758, b759, b763); no bank written for a ruling that names none (b756, b760-b762); b764's written naming SIDE-explicit-formula; a bank
    standing is not rewritten (planted); the ruled and bases routes call the writer."""
    L, res = [], {}
    acts = {}
    for a in K3_ACTS:
        p = os.path.join(D, '%s_kernel_bases.json' % a)
        acts[a] = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
    L += ['  THE RECORD INSTANCE: b763 defect (h), REPEAT b759 (b); the banks on record: %s' % (
        ', '.join('%s %s' % (a, sorted(v)) for a, v in sorted(acts.items()) if v)),
          '    the ferry banks read: %s (data/<act>_ferry.txt, the record`s); the acts with no bank on record: %s' % (
              ', '.join(K3_ACTS), ', '.join(a for a in K3_ACTS if not acts[a]))]
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k3_')
        inst = tempfile.mkdtemp(prefix='b764k3i_')
        try:
            got = snapshot(rev, K3_PATHS, tmp)
            os.makedirs(os.path.join(inst, 'ferries'))
            os.makedirs(os.path.join(inst, 'out'))
            for a in K3_ACTS:
                shutil.copyfile(os.path.join(D, '%s_ferry.txt' % a), os.path.join(inst, 'ferries', '%s_ferry.txt' % a))
            with open(os.path.join(inst, 'acts.json'), 'w', encoding='utf-8') as fh:
                json.dump(acts, fh)
            j = probe(K3_PROBE, tmp, inst)
        finally:
            for t_, pre in ((tmp, 'b764k3_'), (inst, 'b764k3i_')):
                if os.path.isabs(t_) and os.path.basename(t_).startswith(pre):
                    shutil.rmtree(t_, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        L.append('  %s (relay %s): the files %s ; the kernels of commit.py %s ; the routes of main calling the writer %d' % (
            name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got), j['kernels'], j['main_calls']))
        rows_ok = []
        for a in K3_ACTS:
            r, rec = j['res'][a], acts[a]
            rec_text = open(os.path.join(D, '%s_kernel_bases.json' % a), encoding='utf-8').read().replace(chr(13), '') if rec else None
            if r['named'] is None:
                L.append('    %s: NO WRITER (the bank on record %s)' % (a, sorted(rec) if rec else 'none'))
                rows_ok.append(False)
                continue
            if rec:
                ok = r['named'] == sorted(rec) and r['written'] == rec_text
                what = 'written %s the bank on record byte for byte' % ('EQUAL TO' if r['written'] == rec_text else 'DIFFERING FROM')
            elif a == 'b764':
                w = json.loads(r['written']) if r['written'] else {}
                ok = r['named'] == ['SIDE-explicit-formula'] and sorted(w) == ['SIDE-explicit-formula'] and bool(re.fullmatch('[0-9a-f]{40}', w.get('SIDE-explicit-formula', '')))
                what = 'written %s' % (sorted(w) if w else 'NOTHING')
            else:
                ok = r['named'] == [] and r['written'] is None
                what = 'nothing written' if r['written'] is None else 'WRITTEN WHERE NONE IS NAMED'
            rows_ok.append(ok)
            L.append('    %s: named %s ; %s -- %s' % (a, r['named'] or 'none', what, 'AS ON RECORD' if ok else 'NOT AS ON RECORD'))
        pl = j['planted']
        if pl:
            L.append('    PLANTED: a bank standing for b999 with another commit, the writer run over it: %s (%s)' % (
                'KEPT, not rewritten' if pl['kept'] else 'REWRITTEN', next((x.strip() for x in pl['lines'] if 'STANDS' in x), 'no STANDS line')[:120]))
        fault = all(j['res'][a]['named'] is None for a in K3_ACTS) and j['main_calls'] == 0
        clean = all(rows_ok) and bool(pl and pl['kept']) and j['main_calls'] >= 2
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


# ================================================================================ [K14] THE PRICE'S RATE BY THE KIND OF BUILD
K14_PATHS = ('tools/standing/dispatchrate.py', 'tools/standing/figbank.py', 'tools/b764_ceiling.py', 'tools/b763_ceiling.py',
             'data/b763_price.json', 'data/b764_price.json')
K14_PROBE = r'''
import importlib.util, json, os, sys
snap = sys.argv[1]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
disp = lambda rows: dict((k, [r['lo_h'], r['hi_h'], list(r.get('dispatches') or [0, 0])]) for k, r in rows.items() if max(r.get('dispatches') or [0]) > 0)
out = dict(rate_reader=os.path.exists(os.path.join(snap, 'tools', 'standing', 'dispatchrate.py')))
b764 = os.path.join(snap, 'tools', 'b764_ceiling.py')
if os.path.exists(b764):
    C = load('b764_ceiling', b764)
    j, rows, k8, L, ok = C.price(os.path.join(snap, 'data', 'b763_price.json'), (67.7, 103.9, 7.3), {})
    j4, rows4, k84, L4, ok4 = C.price()
    out.update(reader='tools/b764_ceiling.py price(), through tools/standing/dispatchrate.py', b763=disp(rows), b764=disp(rows4),
               b764_sum=round(j4['spent_h'] + sum(r['lo_h'] for r in rows4.values() if r['summed']), 2), ok=ok and ok4)
else:
    C = load('b763_ceiling', os.path.join(snap, 'tools', 'b763_ceiling.py'))
    j, rows, k8 = C.price()
    out.update(reader='tools/b763_ceiling.py price(), the reader of record (no tools/b764_ceiling.py)', b763=disp(rows), b764=None, b764_sum=None,
               ok=True, h_per_dispatch=j.get('h_per_dispatch'))
print(json.dumps(out))
'''


def control_k14(before, after):
    """[K14]: the price table's reader taking a dispatch's hours from the kind of build it is. Each revision's reader of the price table: at
    the commit before, tools/b763_ceiling.py's price() (no tools/b764_ceiling.py, no tools/standing/dispatchrate.py), over b763's table;
    at the repair's, tools/b764_ceiling.py's price() through tools/standing/dispatchrate.py, over b763's table at the kinds b764's table names
    and over b764's own. The record instance: data/b763_misses.txt (11), b763's table at zq-b730's 0.325 h a dispatch (h_per_dispatch), its
    seven runs 0.25 to 1.73 h each, the completed 67.7 to 103.9 min. FAULT: the reader takes b763's dispatching rows as priced, (7)'s
    statement (one dispatch, a build of the kernel whole) at under a whole build's lower minutes. CLEAN: every dispatching row of b763's read
    at or above its floor by kind, (7)'s statement at 1.13-1.73 h; b764's rows read as priced (AT ITS KIND, the waits of its row :38 read),
    its step-zero sum 17.37 h unmoved."""
    L, res = [], {}
    whole_lo = 67.7 / 60.0
    L.append('  THE RECORD INSTANCE: data/b763_misses.txt (11): b763`s table priced a dispatch at 0.325 h (data/b763_price.json h_per_dispatch, from '
             'data/b757_price.txt :8); b763`s completed runs 67.7-103.9 min each (data/b764_price.txt :8, from data/b763_closing.txt :743)')
    for name, rev in (('BEFORE', before), ('AFTER', after)):
        tmp = tempfile.mkdtemp(prefix='b764k14_')
        try:
            got = snapshot(rev, K14_PATHS, tmp)
            j = probe(K14_PROBE, tmp)
        finally:
            if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b764k14_'):
                shutil.rmtree(tmp, ignore_errors=True)
        if 'error' in j:
            L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
            res[name] = None
            continue
        b3 = j['b763']
        st = b3.get('(7) statements') or [None, None, None]
        L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
              '    THE READER: %s ; the rate reader tools/standing/dispatchrate.py %s' % (j['reader'], 'STANDS' if j['rate_reader'] else 'ABSENT'),
              '    b763`s dispatching rows as the reader returns them (lower-upper h, dispatches): %d' % len(b3)]
        # ### the flag's tolerance a hundredth: the reader rounds its floor to the hundredth (27 x 67.7 / 60 = 30.465 read 30.46)
        L += ['      %-28s %.2f-%.2f h, %d-%d dispatches%s' % (k, v[0], v[1], v[2][0], v[2][1], ' ### UNDER A WHOLE BUILD`S LOWER MINUTES A DISPATCH'
                                                              if v[0] < v[2][0] * whole_lo - 0.01 else '') for k, v in sorted(b3.items())]
        if j['b764'] is not None:
            L.append('    b764`s dispatching rows as the reader returns them: %s ; its step-zero sum at the lower figures %.2f h (the bank`s 17.37 h)' % (
                ', '.join('%s %.2f-%.2f h' % (k, v[0], v[1]) for k, v in sorted(j['b764'].items())), j['b764_sum']))
        fault = (not j['rate_reader']) and st[0] is not None and st[0] < whole_lo - 0.005
        clean = (j['rate_reader'] and j['ok'] and len(b3) == 15 and all(v[0] >= v[2][0] * (7.3 / 60.0) - 0.005 for v in b3.values())
                 and st[:2] == [1.13, 1.73] and j['b764'] == {'(7) reference+save': [1.13, 1.73, [2, 2]], '(7) restore': [0.12, 1.73, [1, 1]]}
                 and abs(j['b764_sum'] - 17.37) <= 0.005)
        L.append('    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ')))
        res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN'


CONTROLS = dict(K10=control_k10, K1=control_k1, K5=control_k5, K8=control_k8, K15=control_k15, K16=control_k16, K7=control_k7, K17=control_k17,
                K13=control_k13, K12=control_k12, K11=control_k11, K2=control_k2, K3=control_k3, K14=control_k14)


def main(argv):
    if len(argv) < 3 or argv[0] not in CONTROLS:
        sys.exit(__doc__ + '\nkeys: %s' % ', '.join(sorted(CONTROLS)))
    key, before, after = argv[0], argv[1], argv[2]
    rc, b = git('rev-parse', before)
    rc2, a = git('rev-parse', after)
    rc3, p = git('rev-parse', '%s^1' % after)
    if rc or rc2 or rc3:
        sys.exit('### A REVISION DOES NOT RESOLVE -- NOTHING READ')
    b, a, p = b.decode().strip(), a.decode().strip(), p.decode().strip()
    head = ['## [%s] THE PLANTED CONTROL (%s): BEFORE relay %s, THE REPAIR`S COMMIT relay %s, its first parent %s -- %s' % (
        key, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), b[:8], a[:8], p[:8], 'THE COMMIT BEFORE' if p == b else 'NOT THE COMMIT BEFORE')]
    L, ok = CONTROLS[key](b, a)
    ok = ok and p == b
    L = head + L + ['### ### **[%s] THE CONTROL %s: THE FAULT READ BEFORE AND CLEAN AFTER: %s.**' % (key, 'AS WANTED' if ok else 'NOT AS WANTED', ok), '']
    print(NL.join(L))
    if '--bank' in argv:
        prior = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
            'b764 -- THE PLANTED CONTROLS OF THE REPAIRS, (R374)(5), one section a key, each appended by tools/b764_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b764_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
