# -*- coding: utf-8 -*-
"""standing/v1364.py -- THE CONTROLS OF v1.36.4, (R369)(4)(ii): THE PLANT OF G-DELETES-ONE-BRANCH READS KEPT EVERY CLAUSE THAT COVERS A
NAMED REF, in v1363.py's form.

The ruling's words (relay data/b759_ferry.txt :15): "(ii) THE PLANT OF G-DELETES-ONE-BRANCH (tools/standing/allow.py :110): the standing
reader reads kept each clause that covers a named ref, as b758's module did after its lock (plant_every_kept in tools/acts/b758.py); its
control (R368) replayed with its clauses (2) and (5) both read, the plant failing as wanted." b758 events (70) (relay data/b758_events.txt
:554-:566): the plant turned to kept the first delete clause covering the named refs, (R368)(2)'s; (5)'s clause still allowed the names, so
the planted copy passed and the seal refused. tools/standing/allow.py v1.36.4: covering(), and plant_kept reading kept every covering
clause, each of its "delete" words. BEFORE is allow.py at BASE, executed as a module of its own; AFTER the working file. The arm's inputs as
the template gives them (checks.tpl :792, :829, :1706): the named refs from the act's worklist DELETE (read by literal, its file not run),
the deletes read through deletes_read against the ruling and the author's words (words_of).

  (b758)     (R368) REPLAYED: data/b758_ferry.txt, its named refs; the covering clauses read, (2)'s and (5)'s by their ferry lines; the live
             reading allowed at both; the planted reading BEFORE allowed (the plant passing, b758's refusal) and AFTER refused (failing as wanted).
  (others)   the rulings of b724 to b757 with a worklist DELETE: the planted reading AFTER equal to BEFORE at each, the covering clauses one at each.
  (b759)     b759's own ruling and its five named refs: one covering clause, (3)'s; live allowed, planted refused.
  (none)     a ruling with no covering clause: None BEFORE and AFTER (the plant places nothing, the arm's positive control reading DEFECTIVE).
  (diff)     the working allow.py against BASE's: the lines removed within v1.5.0's plant_kept and the two listing lines of its docstring.
  (version)  tools/standing/VERSION moved to v1.36.4.

  python -X utf8 -u tools/standing/v1364.py control [b758|others|b759|none|diff|version ...] [--bank]
"""
import ast
import difflib
import io
import os
import re
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '983ca5b1'   # ### the relay's HEAD before this change (b759 component 2, step 9, v1.36.3)
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import allow as AL              # noqa: E402  (the working file: AFTER)
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def base():
    if 'A0' not in _MEMO:
        src = V.show(BASE, 'tools/standing/allow.py')
        m = types.ModuleType('allow_base')
        m.__file__ = os.path.join(S, 'allow.py')
        exec(compile(src, 'allow.py@%s' % BASE, 'exec'), m.__dict__)   # noqa: S102
        _MEMO['A0'] = m
        _MEMO['src0'] = src
    return _MEMO['A0']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def rd(rel):
    p = os.path.join(RELAY, rel)
    return io.open(p, encoding='utf-8').read() if os.path.exists(p) else None


def named_of(act):
    """the act's named refs as the template reads them (sorted(b for _r, bs in K.DELETE for b in bs)), DELETE read from
    tools/<act>_worklist.py by literal; None where the file or a literal DELETE is absent."""
    src = rd('tools/%s_worklist.py' % act)
    if src is None:
        return None
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'DELETE' for t in node.targets):
            try:
                val = ast.literal_eval(node.value)
            except ValueError:
                return None
            return sorted(b for _r, bs in val for b in bs)
    return None


def reading(mod, ruling, words, named):
    """(the live ruling allows the named refs, the planted copy None or whether it allows them, the planted copy)."""
    rows = [('-', b) for b in named]
    live = mod.deletes_read(rows, ruling, words)['ok']
    p = mod.plant_kept(ruling, named)
    return live, (None if p is None else mod.deletes_read(rows, p, words)['ok']), p


def line_of(ferry, clause):
    """the ferry's line carrying the clause's opening (whitespace collapsed on both sides)."""
    head = clause[:48]
    for i, l in enumerate(ferry.split(NL), 1):
        if head in re.sub(r'\s+', ' ', l):
            return i
    return None


def control_b758():
    L = ['### (b758): (R368) REPLAYED, ITS CLAUSES (2) AND (5) BOTH READ']
    fe, words, named = rd('data/b758_ferry.txt'), AL.words_of('b758'), named_of('b758')
    b0 = base()
    cs0 = [b0.delete_clause(fe, named)]
    cs1 = AL.covering(fe, named)
    lines = [line_of(fe, c) for c in cs1]
    l0, p0, _ = reading(b0, fe, words, named)
    l1, p1, _ = reading(AL, fe, words, named)
    return L, case(L, 'b758', 'data/b758_ferry.txt ; the named refs %s' % named,
                   'the clause planted %d, at ferry :%s ; live allowed %s ; planted allowed %s (the plant passing: b758`s refusal, data/b758_close_dry.txt :2-:6)' % (
                       len([c for c in cs0 if c]), line_of(fe, cs0[0]) if cs0[0] else '-', l0, p0),
                   'the covering clauses %d, at ferry %s ; live allowed %s ; planted allowed %s' % (len(cs1), ', '.join(':%s' % x for x in lines), l1, p1),
                   bool(named) and l0 is True and p0 is True and lines and line_of(fe, cs0[0]) == 11,
                   bool(named) and l1 is True and p1 is False and lines == [11, 17]), 1


def control_others():
    L = ['### (others): THE RULINGS OF b724 TO b757, THE PLANTED READING AFTER AGAINST BEFORE']
    b0 = base()
    acts = ['b%d' % n for n in range(724, 758)]
    same, differ, unread, ncov = [], [], [], {}
    for a in acts:
        fe, named = rd('data/%s_ferry.txt' % a), named_of(a)
        if fe is None or not named:
            unread.append(a)
            continue
        words = AL.words_of(a)
        r0, r1 = reading(b0, fe, words, named), reading(AL, fe, words, named)
        ncov[a] = len(AL.covering(fe, named))
        (same if (r0[0], r0[1]) == (r1[0], r1[1]) else differ).append('%s %s/%s' % (a, r0[1], r1[1]))
    fails = [x for x in same if x.endswith('/False')]
    multi = sorted(a for a, n in ncov.items() if n != 1)
    return L, case(L, 'others', 'acts %d ; read %d ; unread (no ferry or no literal DELETE) %d %s' % (len(acts), len(same) + len(differ), len(unread), unread),
                   'n/a (the reading compared below)',
                   'the planted reading equal to BEFORE at %d, the plant failing as wanted at %d of them, differing at %d %s ; the covering clauses one at each but %s' % (
                       len(same), len(fails), len(differ), differ or 'NONE', multi or 'NONE'),
                   True, not differ and len(same) >= 30 and not multi), 1


def control_b759():
    L = ['### (b759): b759`S OWN RULING AND ITS FIVE NAMED REFS']
    fe, words, named = rd('data/b759_ferry.txt'), AL.words_of('b759'), named_of('b759')
    cs = AL.covering(fe, named)
    l1, p1, _ = reading(AL, fe, words, named)
    l0, p0, _ = reading(base(), fe, words, named)
    return L, case(L, 'b759', 'data/b759_ferry.txt ; the named refs %s' % named, 'live allowed %s ; planted allowed %s' % (l0, p0),
                   'the covering clauses %d, at ferry %s ; live allowed %s ; planted allowed %s' % (len(cs), ', '.join(':%s' % line_of(fe, c) for c in cs), l1, p1),
                   l0 is True and p0 is False, len(named or ()) == 5 and len(cs) == 1 and line_of(fe, cs[0]) == 13 and l1 is True and p1 is False), 1


def control_none():
    L = ['### (none): A RULING WITH NO COVERING CLAUSE']
    fe = 'The push-b700-* branches are kept. Nothing else is said; port-b707 is NOT deleted.'
    named = ['push-b701-record']
    p0, p1 = base().plant_kept(fe, named), AL.plant_kept(fe, named)
    return L, case(L, 'none', 'a planted ruling naming push-b701-record in no delete clause', 'plant_kept -> %r' % p0, 'plant_kept -> %r ; covering %d' % (
        p1, len(AL.covering(fe, named))), p0 is None, p1 is None and not AL.covering(fe, named)), 1


def control_diff():
    L = ['### (diff): THE WORKING allow.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'allow.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    i0 = next(i for i, l in enumerate(s0) if l.startswith('def plant_kept('))
    i1 = next(i for i in range(i0 + 1, len(s0)) if s0[i].startswith(('def ', '# ###')))
    lst = next(i for i, l in enumerate(s0) if 'plant_kept(ruling, must) -> the ruling' in l)
    allowed = set(range(i0, i1)) | {lst, lst + 1}
    removed = []
    for tag, a1, a2, _b1, _b2 in difflib.SequenceMatcher(None, s0, s1, autojunk=False).get_opcodes():
        if tag in ('replace', 'delete'):
            removed += list(range(a1, a2))
    out = [i for i in removed if i not in allowed]
    return L, case(L, 'diff', 'lines of BASE`s file removed or replaced', 'BASE`s file read, %d lines ; v1.5.0`s plant_kept at :%d-:%d' % (len(s0), i0 + 1, i1),
                   'removed or replaced %d (at %s) ; outside plant_kept and the listing %d' % (len(removed), ', '.join(':%d' % (i + 1) for i in removed), len(out)),
                   len(s0) > 150, bool(removed) and not out), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.3', ver == 'v1.36.4'), 1


CONTROLS = dict(b758=control_b758, others=control_others, b759=control_b759, none=control_none, diff=control_diff, version=control_version)
ORDER = ('b758', 'others', 'b759', 'none', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.36.4, (R369)(4)(ii): THE PLANT OF G-DELETES-ONE-BRANCH READS KEPT EVERY COVERING CLAUSE (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'the rulings read from the relay`s banks, the worklists read by literal and not run; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/allow.py at %s) and after (the working file)' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.36.4: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1364.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
