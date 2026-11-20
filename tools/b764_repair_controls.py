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
    (n), (o) the arm route: `needle.py b763 arm G-DIFFERS-ERRATA` over b763's own corrigendum head needle and a planted needle written
        nowhere, --dry: the arm run on b763's composed sources (PASS or FAIL, not RAISED), the first needle standing in the text the arm
        reads (its FINDINGS line reader's source), the planted one not. b763 and not b764: b764's act module holds carried stubs until its
        sections are written at Component 5 (its checks section 60 among them), so b764's sources halt by design before then (the first run
        of this control, 18:40:16Z, read that halt and is kept in the bank)."""
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
    a = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(ROOT, 'tools', 'standing', 'needle.py'), 'b763', 'arm', 'G-DIFFERS-ERRATA',
                        '## Corrigendum to b762', 'b764 PLANTED NEEDLE WRITTEN NOWHERE', '--dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT, timeout=560)
    out = a.stdout
    m = re.search(r'ON THE COMPOSED SOURCES: (PASS|FAIL|RAISED[^(]*)', out)
    rows = re.findall(r"NEEDLE '([^']*)'.* -- (STANDS|DOES NOT STAND)", out)
    n_ok = bool(m) and not m.group(1).startswith('RAISED') and rows[:2] == [('## Corrigendum to b762', 'STANDS'), ('b764 PLANTED NEEDLE WRITTEN NOWHERE', 'DOES NOT STAND')]
    L += ['    (l) the recut bank`s foot: the repaired foot`s text read %s ; at 1d8b80a2 a verdict line %s, the needle %s ; at 9779a81f a verdict line %s, the needle %s -- %s' % (
              j['l_need'], j['l_before']['foot_found'], 'STANDS' if j['l_before']['rows'][0][1] else 'DOES NOT STAND', j['l_after']['foot_found'],
              'STANDS' if j['l_after']['rows'][0][1] else 'DOES NOT STAND', 'AS WANTED' if l_ok else 'NOT AS WANTED'),
          '    (p) the trail needle: backtick form raw %s, through conv %s ; typographic form through conv %s -- %s' % (
              j['p_rows'][0][1], j['p_rows'][0][2], j['p_rows'][1][2], 'AS WANTED' if p_ok else 'NOT AS WANTED'),
          '    (q) b763`s face paragraph at 256c3e8d (found %s): arm misses %d (multi-arm paragraphs %d) ; with the two arms named: arm misses %d -- %s' % (
              bool(para), j['q_before'][1], j['q_before'][2], j['q_after'][1], 'AS WANTED' if q_ok else 'NOT AS WANTED'),
          '    (n), (o) the arm route, b763`s G-DIFFERS-ERRATA on b763`s composed sources (exit %d, %.0f s): %s ; the needles %s -- %s' % (
              a.returncode, time.time() - t0, m.group(1).strip() if m else 'NO VERDICT LINE', rows or (a.stderr or out).strip()[-300:],
              'AS WANTED' if n_ok else 'NOT AS WANTED')]
    clean = l_ok and p_ok and q_ok and n_ok
    L.append('    AFTER: %s' % ('CLEAN' if clean else 'THE FAULT READ'))
    return L, before_fault and clean


CONTROLS = dict(K10=control_k10, K1=control_k1, K5=control_k5)


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
