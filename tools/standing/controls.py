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


def minted():
    """the act that minted v1.0.0's cases: the first chain act with a standing controls bank (data/<act>_standing_controls.txt)."""
    for a, _r, _p in A.chain():
        if os.path.isfile(os.path.join(A.D, '%s_standing_controls.txt' % a)):
            return a
    return None


def lines():
    cur = A.current()
    act, parts = cur['act'], cur['parts']
    # ### v1.1.0: v1.0.0's cases read the record of the act that minted them (its previous two acts), not the current act's neighbours: their
    # ### record instances are those acts' defects, and the acts after them do not carry the defects (the old route's unwritten bank, the
    # ### delete call, the components composed as prose)
    mact = minted() or act
    prev = A.prev_of(mact)
    pprev = A.prev_of(prev)
    L = ['%s -- THE CLASS REPAIRS` CONTROLS OF THE STANDING TOOLSET, TWO INSTANCES EACH (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are cases: the repair, the instance (RECORD or CONSTRUCTED), what is read, the figure got, the figure wanted, AS WANTED.',
         '### Written by tools/standing/controls.py; (4)(iii)`s control is tools/standing/hook.py`s.',
         '### v1.0.0`s cases (i)-(vi) read the record of the act that minted them, %s (its previous acts %s and %s); v1.1.0`s (3i)-(3vi) read %s`s.' % (
             mact, prev, pprev, A.prev_of(act)), '']
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
    lines_v11(L, case, cur, act, A.prev_of(act))
    reps = sorted(set(r for r, _k, _o in res))
    per = dict((r, (any(k == 'RECORD' for rr, k, _o in res if rr == r), any(k == 'CONSTRUCTED' for rr, k, _o in res if rr == r),
                    all(o for rr, _k, o in res if rr == r))) for r in reps)
    L += ['', '### per repair: %s' % ' ; '.join('(%s) record %s constructed %s as wanted %s' % (r, v[0], v[1], v[2]) for r, v in per.items()),
          '', '### ### **CASES %d ; AS WANTED %d ; REPAIRS %d, EACH WITH BOTH INSTANCES %s ; ALL AS WANTED %s.**' % (
              len(res), sum(1 for r in res if r[2]), len(reps), all(v[0] and v[1] for v in per.values()), all(r[2] for r in res))]
    return L, act, all(r[2] for r in res)


def _section(text, head, stop=r'^## '):
    """the lines of a bank's section from its `head` line to the next `stop` line."""
    L = (text or '').split(NL)
    out, on = [], False
    for l in L:
        if l.startswith(head):
            on = True
            continue
        if on and re.match(stop, l):
            break
        if on:
            out.append(l)
    return out


def _paragraph(text, n):
    """an events bank's item (n): its starting line to the next starting line, joined."""
    out, on = [], False
    for l in (text or '').split(NL):
        m = re.match(r'^\((\d+)\) ', l)
        if m:
            on = int(m.group(1)) == n
        if on:
            out.append(l)
    return ' '.join(out)


def _required_of(src):
    """REQUIRED_BANKS of an act's suite, read from its source by its assignment (not imported)."""
    import ast
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'REQUIRED_BANKS' for t in node.targets):
            return list(ast.literal_eval(node.value))
    return []


def lines_v11(L, case, cur, act, prev):
    """the class repairs of (R326)(3), the toolset at v1.1.0, each with an instance from the record (the previous act's banks) and one
    constructed. Labels 3i-3vi."""
    import allow as AW
    import rootbanks as RB
    import roster as RO
    import words as WO
    L += ['', '### THE CLASS REPAIRS OF v1.1.0 (%s`s ruling %s, its (3)), read over %s`s banks (the record) and constructed:' % (act, cur.get('ruling'), prev)]
    # (3i) the allowances from the ruling
    ruling, wtext = AW.ruling_of(prev), AW.words_of(prev)
    sz = A.rd('%s_stepzero.txt' % prev)
    dels = []
    for l in _section(sz, '## THE BRANCHES'):
        m = re.match(r'^(relay|PLACE-papers): (.*)$', l)
        if m:
            dels += [(m.group(1), b) for b in AW.BRANCH.findall(m.group(2))]
    r1 = AW.deletes_read(dels, ruling, wtext)
    case('3i', 'RECORD', '%s`s step-zero deletes (data/%s_stepzero.txt) against its ruling`s delete clauses: deletes, allowed, outside' % (prev, prev),
         (len(dels), sum(1 for _r, _b, ok in r1['rows'] if ok), r1['outside']), (len(dels), len(dels), []))
    L.append('        the ruling`s delete names %s ; kept %s ; the deletes %s' % (r1['allowed'], r1['kept'], dels))
    ev = A.rd('%s_events.txt' % prev)
    ev7 = []
    for b in AW.BRANCH.findall(_paragraph(ev, 7)):
        if b not in ev7:
            ev7.append(b)
    r2 = AW.deletes_read([('either', b) for b in ev7], ruling, wtext)
    case('3i', 'RECORD', '%s`s event (7): the two push branches deleted outside its ruling`s list, refused' % prev,
         ([b for _r, b in r2['outside']], len(ev7)), (ev7, 2))
    r3 = AW.deletes_read(dels + [('relay', 'push-%s-planted' % act)], ruling, wtext)
    case('3i', 'CONSTRUCTED', 'a seventh delete, a branch the ruling does not name: refused', [b for _r, b in r3['outside']], ['push-%s-planted' % act])
    ans = A.rd('%s_author_answers.txt' % prev)
    p1 = AW.prompts_read(ans, ruling, wtext)
    case('3i', 'RECORD', '%s`s prompts (data/%s_author_answers.txt) against the ruling`s root prompt and the banked words: prompts, allowed, unbanked' % (prev, prev),
         (len(p1['rows']), p1['allowed'], p1['unbanked']), (4, 4, []))
    p2 = AW.prompts_read(ans + '\n### PROMPT 1 (Unbanked): a constructed prompt whose word no bank carries\n', ruling, wtext)
    case('3i', 'CONSTRUCTED', 'a fifth prompt with no banked word: refused', p2['unbanked'], ['Unbanked'])
    # (3ii) the seal commits what it hashes
    sh = A.jl('%s_seal_hashes.json' % prev)
    seal_c = A.step_commit(prev, 'seal')
    order = [r['commit'] for r in A.steps(prev) if r.get('repo') == 'relay' and r.get('phase') in ('gate', 'seal')]
    h = C.seal_head(sh.get('tools') or {}, order)
    case('3ii', 'RECORD', '%s`s seal replayed: the head that carries every byte it hashed is its seal commit, not the head it recorded' % prev,
         ((h or '-')[:8], (h or '') == (seal_c or '-'), (sh.get('relay_head') or '')[:8] == (h or '-')[:8]), ((seal_c or '-')[:8], True, False))
    L.append('        the recorded head %s ; the commits read in order %s' % ((sh.get('relay_head') or '-')[:8], [c[:8] for c in order]))
    tl = sorted(sh.get('tools') or {})
    rec_head = sh.get('relay_head') or ''

    def sealed(t):
        return A.blob(seal_c, 'tools/' + t)
    hashed_ok = all((lambda b: b is not None and A.sha256_bytes(b) == (sh.get('tools') or {})[t])(sealed(t)) for t in tl)
    g_rec = C.seal_guard(tl, rev=rec_head, read=sealed)
    g_seal = C.seal_guard(tl, rev=seal_c, read=sealed)
    case('3ii', 'RECORD', '%s`s %d sealed bytes (its seal commit`s blobs, each equal to its sha256) guarded at the head it recorded: refused ; at its seal commit: passed, the head %s' % (
        prev, len(tl), (seal_c or '-')[:8]), (hashed_ok, len(g_rec['refused']) > 0, g_seal['ok'], (g_seal['head'] or '')[:8]), (True, True, True, (seal_c or '-')[:8]))
    L.append('        refused at the recorded head %s: %s' % (rec_head[:8], [t for t, _w in g_rec['refused']]))
    at_seal = [n[len('tools/'):] for n in (A.gs('relay', 'ls-tree', '-r', '--name-only', seal_c or 'HEAD', 'tools/') or '').split(NL) if n.strip()]
    case('3ii', 'RECORD', 'the sealed list by rule (step [8] run by the core) over the tools at %s`s seal commit: equal to the list it sealed' % prev,
         C.sealed_list(prev, at_seal) == tl, True)
    code, sl = C.seal_write(prev, cur['parts'], prev and '', [], write=False)
    case('3ii', 'CONSTRUCTED', 'the core`s seal route on an act whose face carries no lock: refused, nothing recorded', (code, sl[0][:30]), (3, '### THE FACE IS NOT LOCKED -- '))
    one = tl[0] if tl else None

    def edited(t):
        b = sealed(t)
        return (b + b'# an edit after its last commit\n') if (b is not None and t == one) else b
    g1 = C.seal_guard(tl, rev=seal_c, read=edited)
    case('3ii', 'CONSTRUCTED', 'a tool edited after its last commit (%s): refused at the seal, no head recorded' % one,
         ([t for t, _w in g1['refused']], g1['head']), ([one], None))
    # (3iii) the verifier reads the builder's roster
    sys.path.insert(0, A.T)
    import mirror_verify as MV
    import zipfile
    bj, bhead = RO.build_joins(prev)
    out = A.jl('%s_mirror_build.json' % prev).get('out') or ''
    mz = re.search(r'^built: (.+)$', out, re.M)
    zp = mz.group(1).strip() if mz else None
    names = [n for n in zipfile.ZipFile(zp).namelist() if n != 'MANIFEST.md'] if (zp and os.path.isfile(zp)) else None
    if names is None:
        case('3iii', 'RECORD', '%s`s export %s' % (prev, zp), 'ABSENT', 'PRESENT')
    else:
        c_new, _m = MV.clause3(names, paths=RO.roster_at(bhead), source='roster_at')
        c_old, _m = MV.clause3(names)
        case('3iii', 'RECORD', '%s`s export at clause 3: the builder`s roster from main at its source head CLEAN ; the base roster alone (the old route)' % prev,
             (c_new, c_old), (True, False))
        c_bad, _m = MV.clause3(names + ['A_FILE_THE_ROSTER_LACKS.md'], paths=RO.roster_at(bhead), source='roster_at')
        case('3iii', 'CONSTRUCTED', 'the same export with a file the roster lacks: NOT CLEAN', c_bad, False)
    # (3iv) the answers route reads every word
    ws = WO.words(ans)
    # the old matcher, copied from tools/b698_record.py :321, run over each RESULT's text after its row prefix
    OLD = re.compile(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")')
    old = sum(len(OLD.findall(WO.RESULT.sub('', r['text'], count=1))) for r in WO.results(ans))
    back = WO.read_heads(WO.heads_text(ws))
    case('3iv', 'RECORD', '%s`s answers bank: words read by the repaired route, the old matcher`s count (a word after `="` alone), words read back by their heads, refused' % prev,
         (len(ws), old, len(back['words']), back['refused'], [w['word'] for w in back['words']] == [w['word'] for w in ws]), (4, 3, 4, [], True))
    bad = WO.heads_text(ws).split(NL)
    k = next(i for i, l in enumerate(bad) if l.startswith('## (2)'))
    bad[k] = '## (2 a malformed head'
    rb = WO.read_heads(NL.join(bad))
    case('3iv', 'CONSTRUCTED', 'a malformed head: refused with its line', [(i, l) for i, l, _w in rb['refused']][:1], [(k + 1, '## (2 a malformed head')])
    # (3v) a word after a sealed composition
    at = sh.get('at')
    clauses = ['the entry`s **Carried to:** line, composed by %s`s sealed record tool' % prev,
               'the trail`s two clauses, composed by %s`s sealed record tool' % prev]
    late = WO.after(ws, at)
    bl = WO.beside(clauses, ws, at)
    case('3v', 'RECORD', '%s`s words after its seal (%s): the root word alone, printed beside each of the two clauses' % (prev, at),
         (len(late), (late[-1]['transcript'] if late else None) == (ws[-1]['transcript'] if ws else -1),
          sum(1 for l in bl if 'RECEIVED AFTER IT' in l)), (1, True, 2))
    L += ['      ' + l for l in bl]
    case('3v', 'CONSTRUCTED', 'a composition after every word: none printed ; before every word: all printed',
         (len(WO.after(ws, '9999')), len(WO.after(ws, '0000'))), (0, len(ws)))
    # (3vi) the root's required banks against its exclusions
    req = _required_of(A.rd_path(os.path.join(A.T, '%s_checks.py' % prev)))
    named = A.root_named(prev)
    chain_req = [p for p in req if os.path.basename(p).startswith('%s_chain_' % prev)]
    case('3vi', 'RECORD', '%s`s required chain_ banks read by its root (named among its items)' % prev,
         (len(chain_req) > 0, all(p in named for p in chain_req)), (True, True))
    L.append('        the required chain_ banks %s' % chain_req)
    try:
        RB.guard(req, RB.exclusion(prev, r'chain_half_.*|checks.*|events|steps|hook_refusals'))
        ok_narrow = True
    except SystemExit:
        ok_narrow = False
    try:
        RB.guard(req, RB.exclusion(prev, r'chain_.*|checks.*|events|steps|hook_refusals'))
        planted = None
    except SystemExit as e:
        planted = str(e)
    case('3vi', 'CONSTRUCTED', 'the narrowed kind chain_half_ passes ; the planted overlap (the carried wide kind chain_) refused at import, naming the bank',
         (ok_narrow, planted is not None and all(p in planted for p in chain_req)), (True, True))


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
