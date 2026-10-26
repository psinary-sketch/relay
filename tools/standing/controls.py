# -*- coding: utf-8 -*-
"""standing/controls.py -- THE CLASS REPAIRS' CONTROLS ((R325)(4) of the toolset act), each showing two instances of its class, one from
the record and one constructed. (4)(iii)'s control is the hook's own (tools/standing/hook.py control, data/<act>_hook_control.txt).

  (i)   the previous act's longest phase from its root-named part banks: the act before the previous one's seven part banks give its
        longest phase (the record), the previous act's give the figure this act's arm reads, and a part bank whose bytes differ from its
        root's sha256 is refused (constructed); the old route's combined bank, read where its act never wrote it, gives 0
  (ii)  the withheld field, condition-bound, over the previous act's pre-run exercise banks at its seal: its entry withheld (the record);
        the list emptied, the arm unshown and the seal refused; an entry for an arm whose mutated copy fails, the arm stays shown; the
        condition's file present, the entry not withheld (constructed, as the previous act's word (6) set them)
  (iv)  the components composer: the previous two acts' banks rebuilt by replay (data/<act>_replay.txt object (6)); this act's own
        components composed from the ruling's field and its step bank as it stands (constructed)
  (v)   no standing tool deletes: the delete words of G-DELETE-FREE over tools/standing/'s code (0) and over the previous act's tools'
        code (the record, its defect of a delete call); the planted delete found; the hook control's scratch outside data/ and tools/
  (vi)  every caller of neg_shown reads its three lists: the previous act's repairctl caller's two-name unpack, read from its text and
        run on a three-list return, raises (the record); the standing caller reads the lists by name over the previous act's banks at
        its seal and as they stand (constructed)

  python -X utf8 tools/standing/controls.py          prints; writes nothing
  python -X utf8 tools/standing/controls.py bank     writes data/<act>_standing_controls.txt
"""
import os
import re
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A          # noqa: E402
import arms as AR        # noqa: E402
import close as C        # noqa: E402
import components as CO  # noqa: E402
import scan as SC        # noqa: E402

NL = '\n'


def lines():
    cur = A.current()
    act, parts = cur['act'], cur['parts']
    prev = A.prev_of(act)
    pprev = A.prev_of(prev)
    L = ['%s -- THE CLASS REPAIRS` CONTROLS OF THE STANDING TOOLSET, TWO INSTANCES EACH (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are cases: the repair, the instance (RECORD or CONSTRUCTED), what is read, the figure got, the figure wanted, AS WANTED.',
         '### Written by tools/standing/controls.py; (4)(iii)`s control is tools/standing/hook.py`s.', '']
    res = []

    def case(rep, kind, what, got, want):
        ok = got == want
        res.append((rep, kind, ok))
        L.append('  (%s) %-11s %s : got %s ; wanted %s ; %s' % (rep, kind, what, got, want, 'AS WANTED' if ok else '### NOT AS WANTED'))

    # (i)
    r2 = AR.prev_longest(pprev, parts)
    case('i', 'RECORD', '%s`s %d part banks against its root`s sha256: read, refused, longest phase (s)' % (pprev, len(parts)),
         (r2['parts_read'], len(r2['refused']), r2['longest'] > 0), (len(parts), 0, True))
    L.append('        %s`s longest pre-run phase %d s ; refused %s' % (pprev, r2['longest'], r2['refused'] or 'none'))
    r1 = AR.prev_longest(prev, parts)
    case('i', 'RECORD', '%s`s part banks, the figure this act`s G-RULE-LONG-PHASE-SPLIT reads: read, refused' % prev,
         (r1['parts_read'], len(r1['refused'])), (len(parts), 0))
    L.append('        %s`s longest pre-run phase %d s, over %d parts (the arm`s plant sets 500 s and one part: it can fail)' % (
        prev, r1['longest'], r1['parts_read']))
    bad_part = 'data/%s_arms_prerun_%s.txt' % (pprev, parts[0])

    def tampered(rel):
        p = os.path.join(A.RELAY, *rel.split('/'))
        b = open(p, 'rb').read() if os.path.isfile(p) else None
        return (b + b'a planted line\n') if (b is not None and rel == bad_part) else b
    rt = AR.prev_longest(pprev, parts, read=tampered)
    case('i', 'CONSTRUCTED', 'one part bank`s bytes altered (%s): refused, the rest read' % bad_part,
         ([x[0] for x in rt['refused']], rt['parts_read']), ([bad_part], len(parts) - 1))
    old = A.rd('%s_arms_prerun.txt' % pprev)
    case('i', 'RECORD', 'the old route: %s`s combined pre-run bank (never written) gives longest phase' % pprev,
         max([int(x) for x in re.findall(r'THE LONGEST PHASE (\d+) s', old)] or [0]), 0)
    # (ii)
    spec = ((cur.get('replay') or {}).get(prev) or {}).get('withheld') or []
    seal_rev = A.step_commit(prev, 'seal')
    banks = C.exercise_banks(prev, parts, seal_rev)
    arms = C.arms_of(banks, parts)
    ns = C.neg_shown(arms, banks, C.withheld_entries(spec, rev=seal_rev))
    case('ii', 'RECORD', '%s`s field at its seal: shown, unshown, withheld' % prev, (len(ns.shown), len(ns.bad), [w[0] for w in ns.withheld]),
         (len(arms) - len(spec), 0, [e['arm'] for e in spec]))
    e0 = C.neg_shown(arms, banks, C.withheld_entries([], rev=seal_rev))
    case('ii', 'CONSTRUCTED', 'the list emptied: the arm unshown, the seal refuses (unshown names)', [b[0] for b in e0.bad], [e['arm'] for e in spec])
    second = next((n for n, p in arms if not ((banks[p].get('exercise') or {}).get(n) or {}).get('pos')), None)
    spec2 = spec + [dict(arm=second, defect='(x)', cause='a constructed entry', absent='data/%s_never_written.txt' % act)]
    e2 = C.neg_shown(arms, banks, C.withheld_entries(spec2, rev=seal_rev))
    case('ii', 'CONSTRUCTED', 'a second entry for %s, whose mutated copy fails: it stays shown, not withheld' % second,
         (second in e2.shown, second in [w[0] for w in e2.withheld]), (True, False))
    e3 = C.neg_shown(arms, banks, C.withheld_entries(spec, exists=lambda rel: True))
    case('ii', 'CONSTRUCTED', 'the condition`s file present: the entry not withheld, the arm unshown', ([w[0] for w in e3.withheld], [b[0] for b in e3.bad]),
         ([], [e['arm'] for e in spec]))
    case('ii', 'RECORD', 'this act`s field read from the ruling (data/act_current.json `withheld`)', cur.get('withheld'), [])
    # (iv)
    for a in (prev, pprev):
        sp = (cur.get('replay') or {}).get(a) or {}
        comp = [l for l in CO.composed(a, sp.get('components') or [], sp.get('ruling')) if l.startswith('### ')]
        bank = [l for l in A.rd('%s_components.txt' % a).split(NL) if l.startswith('### ')]
        named = [x['id'] for x in (cur.get('replay') or {}).get('findings') or [] if a in x['acts'] and x['object'] == '6']
        case('iv', 'RECORD', '%s`s components bank rebuilt: lines equal / lines ; the finding naming a difference' % a,
             (sum(1 for x, y in zip(comp, bank) if x == y), len(bank), named if comp != bank else []),
             (len(bank), len(bank), []) if a == prev else (0, len(bank), named or ['### UNNAMED']))
    mine = [l for l in CO.composed(act, cur.get('components') or [], cur.get('ruling')) if l.startswith('### ')]
    case('iv', 'CONSTRUCTED', 'this act`s components composed from the ruling`s field (one line per component)', len(mine), len(cur.get('components') or []))
    # (v)
    rows = SC.scan()
    case('v', 'RECORD', 'the delete words over tools/standing/`s code', sum(len(r['deletes']) for r in rows), 0)
    hits = []
    for f in sorted(os.listdir(A.T)):
        if f.startswith(prev + '_') and f.endswith('.py'):
            code, _p = SC.split(A.rd_path(os.path.join(A.T, f)))
            if SC.DELETE.search(code):
                hits.append(f)
    case('v', 'RECORD', 'the same words over %s`s tools` code (its delete-call defect): tools hit' % prev, len(hits) > 0, True)
    L.append('        %s`s tools with a delete word in their code: %s' % (prev, hits or 'none'))
    case('v', 'CONSTRUCTED', 'the planted source`s delete found', SC.count(SC.PLANT)['deletes'], 1)
    tmp = os.path.abspath(tempfile.gettempdir())
    case('v', 'CONSTRUCTED', 'the controls` scratch (%s) outside relay data/ and tools/' % tmp,
         any(os.path.normcase(tmp).startswith(os.path.normcase(x)) for x in (A.D, A.T)), False)
    # (vi)
    src = A.rd_path(os.path.join(A.T, '%s_record.py' % prev))
    m = re.search(r'^\s*(\w+), (\w+) = CK\.neg_shown\(\)', src, re.M)
    raised = None
    if m:
        try:
            exec('%s, %s = NS' % (m.group(1), m.group(2)), {'NS': C.NegShown([], [], [])})
        except ValueError as e:
            raised = 'ValueError: %s' % e
    case('vi', 'RECORD', '%s`s repairctl caller (%s) run on a three-list return' % (prev, m.group(0).strip() if m else 'NOT FOUND'),
         raised is not None, True)
    L.append('        raised: %s' % raised)
    case('vi', 'CONSTRUCTED', 'the standing caller over %s`s banks at its seal: shown, unshown, withheld, by name' % prev,
         (len(ns.shown), len(ns.bad), len(ns.withheld)), (len(arms) - len(spec), 0, len(spec)))
    now = C.exercise_banks(prev, parts)
    nn = C.neg_shown(C.arms_of(now, parts), now, C.withheld_entries(spec))
    case('vi', 'CONSTRUCTED', 'the standing caller over %s`s banks as they stand (the post-push modes): no arm shown, every arm unshown' % prev,
         (len(nn.shown), len(nn.bad) == len(C.arms_of(now, parts))), (0, True))
    reps = sorted(set(r for r, _k, _o in res))
    per = dict((r, (any(k == 'RECORD' for rr, k, _o in res if rr == r), any(k == 'CONSTRUCTED' for rr, k, _o in res if rr == r),
                    all(o for rr, _k, o in res if rr == r))) for r in reps)
    L += ['', '### per repair: %s' % ' ; '.join('(%s) record %s constructed %s as wanted %s' % (r, v[0], v[1], v[2]) for r, v in per.items()),
          '', '### ### **CASES %d ; AS WANTED %d ; REPAIRS %d, EACH WITH BOTH INSTANCES %s ; ALL AS WANTED %s.**' % (
              len(res), sum(1 for r in res if r[2]), len(reps), all(v[0] and v[1] for v in per.values()), all(r[2] for r in res))]
    return L, act, all(r[2] for r in res)


def main(route):
    L, act, ok = lines()
    if route == 'bank':
        p = os.path.join(A.D, '%s_standing_controls.txt' % act)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    print(NL.join(L))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
