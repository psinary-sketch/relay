# -*- coding: utf-8 -*-
"""standing/v1349.py -- THE CONTROLS OF v1.34.9, (R366)(6)[U1]: THE CADENCE OF THE PASSES (relay data/b754_rules.txt (10)), in force from
b757, in v1348.py's form. BEFORE is the suite as BASE left it (relay 5b7aa91e, v1.34.8's own commit): every part run in every mode, no
cadence, no read record. AFTER is tools/standing/cadence.py and the two places of tools/standing/fold/checks.tpl that call it. Each case is
AS WANTED where the suite before runs the part (or holds no such reading) and the cadence after holds it as the rule orders, or where both
are wanted alike. THE COMPILE CONTROL RUNS FIRST. The free memory is printed before each control. Nothing is written to the relay or to
PLACE-papers but this bank; the banks a held part writes are written to a scratch folder of this run and removed after it, and the act's
data/ folder is not written. Written at b756 by the Write tool; no identifier of the author is read into any string here.

  (fit)      KEEP against the fit printed before the put (relay data/b754_agenda.txt :361, :367, :370), standing-a1 joined beside it.
  (prerun)   over b755's pre-run banks as committed (relay 5009a5e9), the decision read as if b756 were in force: the parts that keep their
             place run; standing-b1 runs where tools/standing/ moved since b755's run (it has: v1.34.7 and v1.34.8 landed) and, with that
             run's head planted at HEAD, is read from the bank; the banks it then writes, to the scratch folder, parsed by the combine's own
             footer pattern (tools/standing/close.py PART_FOOT), the seconds this read's, the source named, the per-part seconds bank 0.0 s.
  (prev)     the sitting read from the ferries' titles (b750 and b754 sittings; b755 and b756 not; an act with no ferry counted a sitting);
             at a non-sitting act the parts outside KEEP not run, their banks in the mode `prev` with no arm (the seal's read finds them).
  (postpush) a synthetic pre-push run recorded over scratch files: no record runs; a record unchanged reads; one file changed runs; the
             chain parts run together where one changed; standing-b2a keeps its place.
  (record)   the read record's classes on real calls: a file opened to read is recorded, one opened to write is not, the Python
             installation's files are not; `git show HEAD:<path>` a blob, `git show <hash>:<path>` none, `git log -- <path>` a listing,
             `git status` the status, a bare `rev-parse HEAD` none.
  (template) checks.tpl calls the cadence after the order refusal and before standing-b3's halves guard, writes its field in the writer,
             and leaves G-GUARD-HELD's line where that arm reads it; before b757 the decision is RUN and no read is recorded.
  (version)  tools/standing/VERSION moved to v1.34.9.

  python -X utf8 -u tools/standing/v1349.py control [fit|prerun|prev|postpush|record|template|version ...] [--bank]
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

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '5b7aa91e'   # ### v1.34.8's own commit (b756 component 4): the suite before this change
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)
from standing import cadence as CAD   # noqa: E402
from standing import close as STC     # noqa: E402

TPL = os.path.join(S, 'fold', 'checks.tpl')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.8): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.9): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.8): %s -> (alike at both is wanted)' % at_base,
          '      AFTER  (v1.34.9): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


class _Forced(object):
    """the cadence read as if b756 were in force (FROM_ACT 756) for the length of a with-block; nothing written by it."""

    def __enter__(self):
        self.was = CAD.FROM_ACT
        CAD.FROM_ACT = 756
        return self

    def __exit__(self, *a):
        CAD.FROM_ACT = self.was


def scratch():
    return tempfile.mkdtemp(prefix='v1349_')


# ================================================================================ (fit)
def control_fit():
    L, g, n = ['### (fit): THE PARTS THAT KEEP THEIR PLACE, AGAINST THE FIT PRINTED BEFORE THE PUT (%s)' % CAD.FIT], 0, 0
    t = io.open(os.path.join(D, 'b754_agenda.txt'), encoding='utf-8').read().split(NL)
    lines = {'prerun': 361, 'post-push': 367, 'prev': 370}
    for mode, ln in lines.items():
        row = t[ln - 1]
        m = re.search(r'parts keeping their place (\d+): (.*)$', row)
        fit = set(re.findall(r'(?:^|; )((?:standing-[a-z0-9]+)|act) \(', m.group(2))) if m else set()
        want = fit | (set(CAD.JOINED) if 'standing-a2' in fit else set())
        n += 1
        g += case(L, 'fit', 'the mode %s: relay data/b754_agenda.txt :%d, the parts keeping their place %s' % (mode, ln, m.group(1) if m else '?'),
                  'no cadence: every part run in every mode', 'KEEP %s ; the fit %s with %s joined where standing-a2 keeps its place' % (
                      sorted(CAD.KEEP[mode]), sorted(fit), list(CAD.JOINED)),
                  True, bool(fit) and set(CAD.KEEP[mode]) == want and int(m.group(1)) == len(fit))
    a2_in = all('standing-a2' in CAD.KEEP[mo] and 'standing-a1' in CAD.KEEP[mo] for mo in CAD.HELD_MODES)
    n += 1
    g += case(L, 'fit', 'standing-a1 joined to every mode where standing-a2 keeps its place (the a1 join, checks.tpl main)', 'every part run',
              'standing-a1 in KEEP wherever standing-a2 is: %s' % a2_in, True, a2_in)
    return L, g, n


# ================================================================================ (prerun)
def control_prerun():
    L, g, n = ['### (prerun): THE PRE-RUN, OVER b755`S PRE-RUN BANKS AS COMMITTED, READ AS IF b756 WERE IN FORCE'], 0, 0
    with _Forced():
        for p in ('act', 'standing-a1', 'standing-a2'):
            d = CAD.decide('b756', p, 'prerun', RELAY, CAD.roots(RELAY, None, None))
            n += 1
            g += both(L, 'prerun', 'part %s' % p, 'run', '%s: %s' % (d['held'], d['why']), True, d['run'])
        src, why = CAD.prerun_source(RELAY, 'b756', 'standing-b1')
        d = CAD.decide('b756', 'standing-b1', 'prerun', RELAY, CAD.roots(RELAY, None, None))
        n += 1
        g += both(L, 'prerun', 'part standing-b1, its last pre-run bank %s (%s)' % (src and src['text_name'], why or 'read at relay %s' % src['commit'][:8]),
                  'run', '%s: %s' % (d['held'], d['why']), bool(src), d['run'] and 'moved' in d['why'])
        head = A.gs('relay', 'rev-parse', 'HEAD').strip()
        mv, st = CAD.standing_moved(RELAY, head)
        diff = [x for x in (A.gs('relay', 'diff', '--name-only', 'HEAD', '--', 'tools/standing') or '').split(NL) if x.strip()]
        n += 1
        g += both(L, 'prerun', 'the working tree`s arm: the source run`s head read as HEAD, tools/standing/`s tracked changes now %s' % diff,
                  'run', 'moved %s ; tree %s then and now ; tracked changes %s' % (mv, (st['now'] or '-')[:12], st['dirty']), True,
                  st['then'] == st['now'] and mv == bool(diff) and sorted(st['dirty']) == sorted(diff))
        planted = dict(src, run_head=head)
        keep_src, keep_mv = CAD.prerun_source, CAD.standing_moved
        CAD.prerun_source = lambda *a, **k: (planted, None)
        CAD.standing_moved = lambda root, rh: (False, dict(then=st['now'], now=st['now'], dirty=[]))
        try:
            dp = CAD.decide('b756', 'standing-b1', 'prerun', RELAY, CAD.roots(RELAY, None, None))
        finally:
            CAD.prerun_source, CAD.standing_moved = keep_src, keep_mv
        n += 1
        g += case(L, 'prerun', 'PLANTED: part standing-b1 with tools/standing/ unmoved since the source run and no tracked change', 'run (no cadence)',
                  '%s: %s' % (dp['held'], dp['why']), True, not dp['run'] and dp['held'] == 'read')
        tmp0 = scratch()
        try:
            CAD.held(dict(d, source=src), 'b756', RELAY, tmp0, out=lambda s: None)
            refused = False
        except SystemExit:
            refused = not os.listdir(tmp0)
        finally:
            shutil.rmtree(tmp0, ignore_errors=True)
        n += 1
        g += both(L, 'prerun', 'held() given a decision that runs the part (standing-b1`s real decision)', 'no held()', 'refused %s' % refused, True, refused)
        tmp = scratch()
        try:
            out = []
            code = CAD.held(dp, 'b756', RELAY, tmp, out=out.append)
            names = sorted(os.listdir(tmp))

            def one(prefix):
                hit = [x for x in names if x.startswith(prefix)]
                if len(hit) != 1:
                    raise SystemExit('the held part`s banks %s hold %d named %s*' % (names, len(hit), prefix))
                return os.path.join(tmp, hit[0])
            txt = io.open(one('b756_arms_prerun_standing-b1'), encoding='utf-8').read()
            m = STC.PART_FOOT.search(txt)
            ms = STC.PART_FOOT.search(src['text'])
            ex = json.load(io.open(one('b756_exercise_standing-b1'), encoding='utf-8'))
            sp = json.load(io.open(one('b756_arm_seconds_standing-b1'), encoding='utf-8'))
            lsr = json.load(io.open(one('b756_lsr_prerun_standing-b1'), encoding='utf-8'))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        n += 1
        g += case(L, 'prerun', 'the held part`s banks, written to a scratch folder: %s' % names, 'none written by a cadence',
                  'the footer read by PART_FOOT: part %s, arms %s (the source`s %s), %s s (the source`s %s s); the source named %s' % (
                      m and m.group(1), m and m.group(2), ms and ms.group(2), m and m.group(10), ms and ms.group(10),
                      'relay data/b755_arms_prerun_standing-b1.txt' in txt),
                  True, bool(m) and m.group(1) == 'standing-b1' and m.group(2) == ms.group(2) and m.group(3) == ms.group(3) and int(m.group(10)) <= 2
                  and 'PRE-SEAL (R202)(3)' in txt and 'READ FROM A BANK BY THE CADENCE' in txt and len(names) == 4)
        n += 1
        g += case(L, 'prerun', 'the exercise, seconds and remote-reads banks of the held part', 'none written by a cadence',
                  'exercise mode %s, verdicts the source`s %s, source %s ; seconds arms %s at 0.0 %s ; remote reads %s %s ; exit %s' % (
                      ex.get('mode'), ex.get('exercise') == src['ex'].get('exercise'), (ex.get('cadence') or {}).get('source_exercise'),
                      len(sp.get('arms') or {}), all(v == 0.0 for v in (sp.get('arms') or {}).values()), lsr.get('lsr'), lsr.get('classed'), code),
                  True, ex.get('mode') == 'prerun' and ex.get('exercise') == src['ex'].get('exercise') and (ex.get('cadence') or {}).get('held') == 'read'
                  and sorted(sp.get('arms') or {}) == sorted(src['ex'].get('exercise') or {}) and lsr.get('lsr') == {} and lsr.get('classed') == 'NONE'
                  and code == 0 and bool(out))
    d0 = CAD.decide('b756', 'standing-b1', 'prerun', RELAY, CAD.roots(RELAY, None, None))
    n += 1
    g += both(L, 'prerun', 'NOT IN FORCE: the same decision at b756 as the cadence stands (FROM_ACT %d)' % CAD.FROM_ACT, 'run',
              '%s: %s' % (d0['held'], d0['why']), True, d0['run'] and 'in force from b757' in d0['why'])
    return L, g, n


# ================================================================================ (prev)
def control_prev():
    L, g, n = ['### (prev): THE PASS IN THE PREVIOUS ACT`S MODE AT SITTINGS'], 0, 0
    want = dict(b750=True, b754=True, b755=False, b756=False, b999=None)
    got = dict((a, CAD.sitting(RELAY, a)) for a in want)
    n += 1
    g += both(L, 'prev', 'the sitting read from each ferry`s title (an act with no ferry: None, counted a sitting)', 'no sitting read',
              got, True, got == want)
    with _Forced():
        dk = CAD.decide('b756', 'standing-a2', 'prev', RELAY, {})
        dc = CAD.decide('b756', 'standing-c', 'prev', RELAY, {})
        keep_s = CAD.sitting
        CAD.sitting = lambda r, a: True
        try:
            ds = CAD.decide('b756', 'standing-c', 'prev', RELAY, {})
        finally:
            CAD.sitting = keep_s
    n += 1
    g += both(L, 'prev', 'standing-a2 keeps its place at a non-sitting act', 'run', '%s: %s' % (dk['held'], dk['why']), True, dk['run'])
    n += 1
    g += case(L, 'prev', 'standing-c at b756, not a sitting', 'run (no cadence)', '%s: %s' % (dc['held'], dc['why']), True,
              not dc['run'] and dc['held'] == 'not run')
    n += 1
    g += both(L, 'prev', 'PLANTED: standing-c at an act read as a sitting', 'run', '%s: %s' % (ds['held'], ds['why']), True, ds['run'])
    tmp = scratch()
    try:
        out = []
        code = CAD.held(dc, 'b756', RELAY, tmp, out=out.append)
        names = sorted(os.listdir(tmp))
        txt = io.open(os.path.join(tmp, 'b756_prevrun_standing-c.txt'), encoding='utf-8').read()
        ex = json.load(io.open(os.path.join(tmp, 'b756_prevrun_exercise_standing-c.json'), encoding='utf-8'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    m = STC.PART_FOOT.search(txt)
    n += 1
    g += case(L, 'prev', 'the not-run part`s banks, written to a scratch folder: %s' % names, 'none written by a cadence',
              'footer part %s arms %s declared %s ; exercise mode %s run %s, the seal`s keys %s ; exit %s' % (
                  m and m.group(1), m and m.group(2), m and m.group(9), ex.get('mode'), ex.get('run'),
                  sorted(k for k in ex if k in ('pass_on_prev', 'fail_as_prev', 'diverge', 'not_run_by_prev')), code),
              True, bool(m) and m.group(1) == 'standing-c' and m.group(2) == '0' and m.group(9) == 'NOTRUN' and ex.get('mode') == 'prev'
              and ex.get('run') == 0 and len(names) == 3 and code == 0)
    return L, g, n


# ================================================================================ (postpush)
def _prepush(root, act, part, rec):
    ex = dict(exercise={'G-X': dict(live=True, neg=True, pos=False)}, run=1, live_failing=[], defective=[], neg_failures=0, withheld=[], part=part,
              mode='pre-push', at='2026-11-15T00:00:00Z', relay_head='0' * 40)
    if rec is not None:
        ex['cadence'] = dict(version=CAD.VERSION, held='run', reads=rec)
    io.open(os.path.join(root, 'data', '%s_exercise_%s.json' % (act, part)), 'w', encoding='utf-8').write(json.dumps(ex))
    io.open(os.path.join(root, 'data', '%s_checks_%s.txt' % (act, part)), 'w', encoding='utf-8').write(
        '=\nx -- THE SUITE. ### **PRE-PUSH READING.** ### PART %s\n=\n  ### PART %s : ARMS 1 ; LIVE PASSING 1 ; LIVE FAILING 0 NONE ; '
        'NEGATIVE-CONTROL FAILURES 0 ; POSITIVE-CONTROL PASSES 0 NONE ; DECLARED EQ RUN True ; 120 s ; WITHHELD, NOT EXERCISABLE 0 NONE\n=\n' % (part, part))


def control_postpush():
    L, g, n = ['### (postpush): THE PASS AFTER THE PUSH, OVER A SYNTHETIC PRE-PUSH RUN IN A SCRATCH FOLDER'], 0, 0
    root = scratch()
    try:
        os.makedirs(os.path.join(root, 'data'))
        f1, f2 = os.path.join(root, 'bank_one.txt'), os.path.join(root, 'bank_two.txt')
        io.open(f1, 'w', encoding='utf-8').write('one\n')
        io.open(f2, 'w', encoding='utf-8').write('two\n')
        rts = dict(scratch=root)
        R = CAD.Reads(rts).start()
        io.open(f1, encoding='utf-8').read()
        io.open(f2, encoding='utf-8').read()
        rec = R.state()
        R.stop()
        rec1 = dict(files=dict((k, v) for k, v in rec['files'].items() if k.endswith('bank_one.txt')), blobs={}, listings={})
        rec2 = dict(files=dict((k, v) for k, v in rec['files'].items() if k.endswith('bank_two.txt')), blobs={}, listings={})
        with _Forced():
            _prepush(root, 'b756', 'standing-c', None)
            d = CAD.decide('b756', 'standing-c', 'post-push', root, rts)
            n += 1
            g += both(L, 'postpush', 'standing-c, its pre-push run with no read record', 'run', '%s: %s' % (d['held'], d['why']), True,
                      d['run'] and 'no read record' in d['why'])
            _prepush(root, 'b756', 'standing-c', rec1)
            d = CAD.decide('b756', 'standing-c', 'post-push', root, rts)
            n += 1
            g += case(L, 'postpush', 'standing-c, its record of 1 file (%s) unchanged' % list(rec1['files']), 'run (no cadence)',
                      '%s: %s' % (d['held'], d['why']), True, not d['run'] and d['held'] == 'read')
            tmp = scratch()
            try:
                code = CAD.held(d, 'b756', root, tmp, out=lambda s: None)
                txt = io.open(os.path.join(tmp, 'b756_checks_postpush_standing-c.txt'), encoding='utf-8').read()
                ex = json.load(io.open(os.path.join(tmp, 'b756_exercise_standing-c.json'), encoding='utf-8'))
                names = sorted(os.listdir(tmp))
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
            m = STC.PART_FOOT.search(txt)
            n += 1
            g += case(L, 'postpush', 'the held part`s banks %s' % names, 'none written by a cadence',
                      'footer part %s seconds %s (the source 120) ; exercise mode %s ; exit %s' % (m and m.group(1), m and m.group(10), ex.get('mode'), code),
                      True, bool(m) and m.group(1) == 'standing-c' and int(m.group(10)) <= 2 and 'POST-PUSH' in txt and ex.get('mode') == 'post-push'
                      and len(names) == 3 and code == 0)
            io.open(f1, 'w', encoding='utf-8').write('one, changed\n')
            d = CAD.decide('b756', 'standing-c', 'post-push', root, rts)
            n += 1
            g += both(L, 'postpush', 'PLANTED: the file standing-c read changed after its pre-push run', 'run', '%s: %s' % (d['held'], d['why']), True,
                      d['run'] and 'changed' in d['why'])
            for p in CAD.CHAIN_GROUP:
                _prepush(root, 'b756', p, rec2)
            db3 = CAD.decide('b756', 'standing-b3', 'post-push', root, rts)
            _prepush(root, 'b756', 'standing-b2c', rec1)
            db3c = CAD.decide('b756', 'standing-b3', 'post-push', root, rts)
            db2b = CAD.decide('b756', 'standing-b2b', 'post-push', root, rts)
            n += 1
            g += case(L, 'postpush', 'the chain parts: all four unchanged, then standing-b2c`s read changed', 'run (no cadence)',
                      'b3 %s ; then b3 %s, b2b %s: %s' % (db3['held'], db3c['held'], db2b['held'], db3c['why'][:120]), True,
                      not db3['run'] and db3c['run'] and db2b['run'] and 'together' in db3c['why'])
            _prepush(root, 'b756', 'standing-b2a', rec2)
            da = CAD.decide('b756', 'standing-b2a', 'post-push', root, rts)
            n += 1
            g += both(L, 'postpush', 'standing-b2a keeps its place (it reads a remote)', 'run', '%s: %s' % (da['held'], da['why']), True, da['run'])
    finally:
        shutil.rmtree(root, ignore_errors=True)
    return L, g, n


# ================================================================================ (record)
def control_record():
    L, g, n = ['### (record): THE READ RECORD`S CLASSES ON REAL CALLS'], 0, 0
    root = scratch()
    try:
        fr, fw = os.path.join(root, 'read_me.txt'), os.path.join(root, 'write_me.txt')
        io.open(fr, 'w', encoding='utf-8').write('x\n')
        rts = dict(relay=RELAY, scratch=root)
        hexh = A.gs('relay', 'rev-parse', 'HEAD').strip()
        R = CAD.Reads(rts).start()
        io.open(fr, encoding='utf-8').read()
        io.open(fw, 'w', encoding='utf-8').write('y\n')
        io.open(os.__file__, encoding='utf-8').read()
        for args in (['show', 'HEAD:tools/standing/VERSION'], ['show', '%s:tools/standing/VERSION' % hexh], ['log', '-1', '--format=%H', '--', 'data/act_current.json'],
                     ['status', '--porcelain', '--untracked-files=no'], ['rev-parse', 'HEAD']):
            subprocess.run(['git', '-C', RELAY] + args, capture_output=True)
        st = R.state()
        R.stop()
    finally:
        shutil.rmtree(root, ignore_errors=True)
    files, blobs, lists = sorted(st['files']), sorted(st['blobs']), sorted(st['listings'])
    for what, got, ok in (
            ('a file opened to read recorded, one opened to write not, the Python installation`s not', files,
             files == ['scratch|read_me.txt']),
            ('`git show HEAD:<path>` a blob; `git show <hash>:<path>` none', blobs, blobs == ['relay|HEAD:tools/standing/VERSION']),
            ('`git log -- <path>` the tree listing; `git status` the status; a bare `rev-parse HEAD` none', lists,
             lists == ['relay|status', 'relay|tree'])):
        n += 1
        g += case(L, 'record', what, 'no read record', got, True, ok)
    lists_ = (['git', '-C', 'D:/a b', 'show', 'HEAD:x y.txt'], ['git', 'log', '--format=%H "q"', '--', 'p\\q\\'], ['git', 'status'], ['a\\\\"b', '', 'c d'])
    rt = [CAD.split_cmdline(subprocess.list2cmdline(x)) == x for x in lists_]
    n += 1
    g += case(L, 'record', 'the Windows command line the audit event carries, split back: %d argument lists through subprocess.list2cmdline and back' % len(lists_),
              'no split', rt, True, all(rt))
    return L, g, n


# ================================================================================ (template)
def control_template():
    L, g, n = ['### (template): tools/standing/fold/checks.tpl CALLS THE CADENCE'], 0, 0
    old = V.show(BASE, 'tools/standing/fold/checks.tpl') or ''
    new = io.open(TPL, encoding='utf-8').read()
    nl = new.split(NL)
    i_ord = next((k for k, l in enumerate(nl) if 'order_refusal' in l and '_ord =' in l), None)
    i_cd = next((k for k, l in enumerate(nl) if l.strip().startswith('_cd = _CAD.decide(')), None)
    i_b3 = next((k for k, l in enumerate(nl) if l.strip().startswith("if PART == 'standing-b3':")), None)
    i_rf = next((k for k, l in enumerate(nl) if 'ex.update(_CAD.run_fields(_cd, _reads))' in l), None)
    i_ep = next((k for k, l in enumerate(nl) if l.strip().startswith('ep = os.path.join(D, __import__(\'standing.repeat\'')), None)
    n += 1
    g += case(L, 'template', 'the decision after the order refusal and before standing-b3`s halves guard; the field before the exercise bank`s path',
              'the cadence named %d times' % old.count('_CAD.'), 'order :%s < decision :%s < b3 guard :%s ; field :%s < exercise path :%s ; once each %s' % (
                  i_ord and i_ord + 1, i_cd and i_cd + 1, i_b3 and i_b3 + 1, i_rf and i_rf + 1, i_ep and i_ep + 1,
                  new.count('_cd = _CAD.decide(') == 1 and new.count('_CAD.run_fields(') == 1),
              old.count('_CAD.') == 0, None not in (i_ord, i_cd, i_b3, i_rf, i_ep) and i_ord < i_cd < i_b3 and i_rf < i_ep
              and new.count('_cd = _CAD.decide(') == 1 and new.count('_CAD.run_fields(') == 1)
    gw = "sp = os.path.join(D, '⟪ACT⟫_arm_seconds_%s.json' % PART)"
    k = next((j for j, l in enumerate(nl) if l.strip() == gw), None)
    ko = next((j for j, l in enumerate(old.split(NL)) if l.strip() == gw), None)
    n += 1
    g += both(L, 'template', 'G-GUARD-HELD`s reading: the per-part seconds write`s own line, the line before it `if PRERUN:`',
              'line :%s, before it %r' % (ko and ko + 1, old.split(NL)[ko - 1].strip() if ko else None),
              'line :%s, before it %r ; the write`s line once in the template %s' % (k and k + 1, nl[k - 1].strip() if k else None,
                                                                                   sum(1 for l in nl if l.strip() == gw) == 1),
              ko is not None and old.split(NL)[ko - 1].strip() == 'if PRERUN:',
              k is not None and nl[k - 1].strip() == 'if PRERUN:' and sum(1 for l in nl if l.strip() == gw) == 1)
    d = CAD.decide('b756', 'standing-c', 'post-push', RELAY, CAD.roots(RELAY, None, None))
    rf = CAD.run_fields(d, None)
    n += 1
    g += both(L, 'template', 'NOT IN FORCE: at b756 the decision RUN and the exercise bank`s field empty (no read recorded)', 'every part run',
              'decision %s (%s) ; field %s' % (d['held'], d['why'], rf), True, d['run'] and rf == {})
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.8', ver == 'v1.34.9' == CAD.VERSION)
    return L, g, n


CONTROLS = dict(fit=control_fit, prerun=control_prerun, prev=control_prev, postpush=control_postpush, record=control_record,
                template=control_template, version=control_version)
ORDER = ('fit', 'prerun', 'prev', 'postpush', 'record', 'template', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.9, (R366)(6)[U1]: THE CADENCE OF THE PASSES, IN FORCE FROM b757 (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'written through tools/standing/figbank.py; the banks a held part writes go to a scratch folder of the run, removed after it', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before and after, the suite before read from %s' % BASE, '']
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
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.34.9: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1349.txt' % act), NL.join(out))
        print('written data/%s_standing_v1349.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
