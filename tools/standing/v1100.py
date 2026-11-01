# -*- coding: utf-8 -*-
"""standing/v1100.py -- THE CONTROLS OF v1.10.0 ((R340)(2)), in v190.py's form: each instance replayed through the route as it stood before the repair (read at BASE, the commit
before this version) and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Written at b730 by the Write tool.

  python -X utf8 tools/standing/v1100.py control [own|actroot|exercise|hookact|answers|n5line|rootprompt ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v1100.txt with every control run, nothing else.
(viii), the two dated notes, is a landing and no route: its before and after print at `record c1 notes`.
"""
import importlib
import importlib.util
import json
import os
import re
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
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import faceform as FF           # noqa: E402
import nouns as NO              # noqa: E402
import repeat as RP             # noqa: E402
import rootprompt as RPM        # noqa: E402

BASE = '3b661a42'               # ### relay's step-zero tip: every route of v1.9.0 as it stood
B729_LOCK = '099afbb8'          # ### b729's lock commit (data/b729_scores.json, N4's row)


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def line(bank, n):
    p = os.path.join(RELAY, *bank.split('/'))
    if not os.path.exists(p):
        return None
    t = rd(bank[len('data/'):]).split(NL)
    return t[n - 1] if 0 < n <= len(t) else None


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.9.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.10.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case with no failing side: what the repair must leave standing, printed as that and not as a before and after."""
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.10.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def old_module(rel, name):
    """the module as it stood at BASE, loaded from a scratch file."""
    d = tempfile.mkdtemp(prefix='v1100-')
    p = os.path.join(d, name + '.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(_git('show', '%s:%s' % (BASE, rel)))
    sp = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


HAND = ('ACT_ARMS', 'PARTS', 'HOLD', 'CHAIN_HALVES', 'CHAIN_QUARTERS', 'STANDING_ADDED')   # ### the template's six as BASE carried them, each act's section adding names by hand


def old_read(oldrp, prev, own, n):
    """the reading as it stood before the act's own hand edit to the list: the names above and the component commits; the route at BASE."""
    if n not in HAND and not re.match(r'^C\d+_', n) and oldrp.prev_carries(prev, own, n):
        return getattr(prev, n)
    return getattr(own, n)


def new_read(prev, own, n):
    return getattr(prev, n) if RP.prev_carries(prev, own, n) else getattr(own, n)


def hasattr_read(prev, own, n):
    """the reading b722's run met: the name in the previous worklist read as the previous worklist's, whatever it held (v1.4.0 came after it)."""
    return getattr(prev, n) if hasattr(prev, n) and n not in HAND and n != 'C5_RELAY' else getattr(own, n)


def sweep(prev, own):
    """every exported name read through the new route: (names, a table this act's source could index past, a name read as None where this act's carries a value)."""
    names = RP.exported(own)
    short, none = [], []
    for n in names:
        o, v = getattr(own, n), new_read(prev, own, n)
        if isinstance(o, (tuple, list)) and o and all(isinstance(r, (tuple, list)) for r in o) and len(v) < len(o):
            short.append(n)
        if v is None and o is not None:
            none.append(n)
    return names, short, none


def control_own():
    L, g, n = ['### (own) THE HAND-KEPT-NAMES CLASS, (R340)(2)(i): OWN COMPUTED, NO LIST KEPT; b722`S CRASHES, b729`S CRASH, b724`S PAIR, ONE MORE EXPORTED NAME'], 0, 0
    oldrp = old_module('tools/standing/repeat.py', 'repeat_old')
    w = dict((k, importlib.import_module('%s_worklist' % k)) for k in ('b721', 'b722', 'b723', 'b724', 'b728', 'b729', 'b730'))
    # b729 event (3)
    try:
        r = old_read(oldrp, w['b728'], w['b729'], 'EF_BRANCHES')[2]
        old = 'read %s' % (r,)
        of = False
    except IndexError as e:
        old, of = 'K.EF_BRANCHES[2] on b728`s two rows: IndexError (%s), the crash of b729 event (3)' % e, True
    nv = new_read(w['b728'], w['b729'], 'EF_BRANCHES')[2][0]
    n += 1
    g += case(L, 'own', 'b729 event (3), replayed on b729`s worklist and b728`s, nothing edited', old, 'K.EF_BRANCHES[2] reads %s' % nv, of, nv == 'detect-b729')
    # b722 events (8), (9)
    for name, ev in (('STANDING_COMMIT', '(8)'), ('C6_PP', '(9)')):
        ov = hasattr_read(w['b721'], w['b722'], name)
        v = new_read(w['b721'], w['b722'], name)
        n += 1
        g += case(L, 'own', 'b722 event %s, replayed on b722`s worklist and b721`s, nothing edited: %s' % (ev, name), '%s read as %r: None handed to git' % (name, ov), '%s read as %r' % (name, v), ov is None, v is not None)
    # b724: no crash stands in its banks
    names, short, none = sweep(w['b723'], w['b724'])
    n += 1
    g += guard(L, 'own', 'b724: THE BANKS HOLD NO --prev CRASH AT b724 (no such row in data/b724_events.txt or data/b724_defects.txt; (R334)(2)(i), the order, stands at b724, and v1.4.0 landed it as prev_carries, data/b724_standing_v140.txt): '
               'the pair replayed whole, every exported name of b724`s worklist read over b723`s', '%d names ; a table read short %s ; read None %s' % (len(names), short or 'none', none or 'none'), not short and not none)
    for a, b in (('b721', 'b722'), ('b728', 'b729'), ('b729', 'b730')):
        names, short, none = sweep(w[a], w[b])
        n += 1
        g += guard(L, 'own', 'the pair %s over %s replayed whole, no edit' % (b, a), '%d names ; a table read short %s ; read None %s' % (len(names), short or 'none', none or 'none'), not short and not none)
    # one more exported name, one more row
    own = types.SimpleNamespace(**dict((k, getattr(w['b730'], k)) for k in RP.exported(w['b730'])))
    own.ZZ_NEW = (('a', 'b'), ('c', 'd'))
    own.EF_BRANCHES = tuple(w['b730'].EF_BRANCHES) + (('zq-b730', 'f' * 40),)
    try:
        r = old_read(oldrp, w['b729'], own, 'EF_BRANCHES')[3]
        old, of = 'read %s' % (r,), False
    except IndexError as e:
        old, of = 'K.EF_BRANCHES[3] on b729`s three rows: IndexError (%s)' % e, True
    v, z = new_read(w['b729'], own, 'EF_BRANCHES')[3][0], new_read(w['b729'], own, 'ZZ_NEW')
    n += 1
    g += case(L, 'own', 'a worklist with one more exported name and one more row, read with no edit anywhere', old, 'EF_BRANCHES[3] %s ; ZZ_NEW %s' % (v, z), of, v == 'zq-b730' and z == own.ZZ_NEW)
    # the seat's own probe of this version: a component not yet made
    empty = types.SimpleNamespace(C3_RELAY=())
    n += 1
    g += guard(L, 'own', 'FOUND BY THE REAL RUN, NOT BY THIS CONTROL: `checks --prev --part act` at b730 before this case stood crashed on K.C3_RELAY[0], the first cut of the component rule reading this act`s empty tuple. A component not yet made reads the previous act`s',
               'C3_RELAY read %r' % (new_read(w['b729'], empty, 'C3_RELAY'),), bool(new_read(w['b729'], empty, 'C3_RELAY')))
    # no list kept
    tpl = open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    act = open(os.path.join(T, 'acts', 'b730.py'), encoding='utf-8').read()
    base_tpl = _git('show', '%s:tools/standing/fold/checks.tpl' % BASE)
    n += 1
    g += case(L, 'own', 'no list kept: the template`s OWN tuple and the act`s section checks 63', 'OWN = ( in the template %s' % ('    OWN = (' in base_tpl), 'in the template %s ; the act`s section %s ; self.OWN read %s' % (
        '    OWN = (' in tpl, '⟪SECTION checks 63⟫' in act, 'self.OWN' in tpl), '    OWN = (' in base_tpl, '    OWN = (' not in tpl and '⟪SECTION checks 63⟫' not in act and 'self.OWN' not in tpl)
    L += ['  THE NAMES A --prev RUN AT b730 READS AS ITS OWN, COMPUTED FROM THE TWO MODULES (standing.repeat.own_names; printed, kept nowhere): ' + ', '.join(RP.own_names(w['b729'], w['b730']))]
    L += ['  THE SUITE`S STRUCTURE IS NO NAME IN THAT LIST: it reads KS, bound before the rebinding (fold/checks.tpl :63).']
    return L, g, n


def control_actroot():
    L, g, n = ['### (actroot) G-ACTROOT-BANKED AGAINST THE ROUTE`S LIST, (R340)(2)(ii); THE INSTANCE, b729`S ONSET UNITS'], 0, 0
    j = json.loads(rd('b729_act_root.json'))
    paths = sorted(it.split()[0] for it in (j.get('items') or []) if it.startswith('data/'))
    bar = [p for p in paths if p.endswith(('.gz', '.png', '.jsonl'))]

    def pattern(tpl, act):
        ln = [l for l in tpl.split(NL) if l.lstrip().startswith("return re.compile(r'^⟪ACT⟫_(")][0].strip()
        src = ln[len('return '):].split('   # ###')[0].replace('⟪ACT⟫', act)
        return eval(src, dict(re=re, EXCLUDE_KINDS='events|steps', names=[]))

    old = pattern(_git('show', '%s:tools/standing/fold/record.tpl' % BASE), 'b729')
    new = pattern(open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read(), 'b729')
    u = 'b729_onset_units.jsonl'
    n += 1
    g += case(L, 'actroot', 'data/b729_onset_units.jsonl at 40a4e6b0: the route listed it (%d root paths, barred %s) and the arm refused any .jsonl the route lists: two lists' % (len(paths), bar),
              'the route`s exclusion takes it %s, so the root names it and the arm fails' % bool(old.match(u)), 'the route`s exclusion takes it %s, by the rule "a units file is out of the root, tracked or not", the arm`s bar and the route one reading' % bool(new.match(u)),
              bool(bar) and not old.match(u), bool(new.match(u)))
    keep = [p for p in paths if p.endswith('.txt')][:40]
    n += 1
    g += guard(L, 'actroot', 'a bank the route named at b729 and no units file stays in the route', '%d .txt paths tried ; newly excluded %s' % (len(keep), [p for p in keep if new.match(os.path.basename(p)) and not old.match(os.path.basename(p))] or 'none'),
               not [p for p in keep if new.match(os.path.basename(p)) and not old.match(os.path.basename(p))])
    return L, g, n


def control_exercise():
    L, g, n = ['### (exercise) THE PRE-RUN OVER A COMMITTED BANK, (R340)(2)(iii); THE INSTANCE, b729`S TWO EXERCISE BANKS'], 0, 0
    tracked = set(_git('ls-tree', '-r', '--name-only', B729_LOCK, '--', 'data/').split())
    two = ('b729_exercise_act.json', 'b729_exercise_standing-a.json')
    trk = lambda name: 'data/' + name in tracked   # noqa: E731
    for f, part in zip(two, ('act', 'standing-a')):
        np_ = RP.exercise_name('b729', part, 'prerun', trk)
        n += 1
        g += case(L, 'exercise', 'data/%s, tracked at b729`s lock %s' % (f, B729_LOCK), 'the pre-run wrote %s over the committed bank (d96d5df1, N4`s row)' % f, 'the pre-run writes %s' % np_, trk(f), not trk(np_) and np_.endswith('_b729.json'))
    n += 1
    g += guard(L, 'exercise', 'a mid probe has its own name, so nothing the pre-run writes is committed by a mid commit', RP.exercise_name('b730', 'act', 'mid', trk), RP.exercise_name('b730', 'act', 'mid', trk) == 'b730_mid_exercise_act.json')
    n += 1
    g += guard(L, 'exercise', 'a bank not tracked keeps its plain name, and the reader takes the suffixed one where it stands', '%s ; %s' % (RP.exercise_name('b730', 'act', 'prerun', trk), RP.exercise_read('b730', 'act', lambda p: True)),
               RP.exercise_name('b730', 'act', 'prerun', trk) == 'b730_exercise_act.json' and RP.exercise_read('b730', 'act', lambda p: True) == 'b730_exercise_act_b730.json')
    return L, g, n


def control_hookact():
    L, g, n = ['### (hookact) THE HOOK AND A CLOSED ACT`S BANK, (R340)(2)(iv); THE INSTANCE, b729`S TWO ROWS INTO b728`S BANK'], 0, 0
    oldh = old_module('tools/standing/hook.py', 'hook_old')
    newh = importlib.import_module('hook')
    d = tempfile.mkdtemp(prefix='v1100-hook-')
    os.makedirs(os.path.join(d, 'data'))
    with open(os.path.join(d, 'data', 'act_current.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(act='b728', next='b729'), f)
    with open(os.path.join(d, 'data', 'b728_closing.txt'), 'w', encoding='utf-8') as f:
        f.write('b728 closed' + NL)
    o, nw = os.path.basename(oldh.refusals_path(d)), os.path.basename(newh.refusals_path(d))
    rows = [l for l in rd('b729_hook_refusals.txt').split(NL) if l[:20] in ('2026-10-31T21:37:00Z', '2026-10-31T21:46:56Z')]
    n += 1
    g += case(L, 'hookact', 'b729 step zero: act_current still names b728, whose closing stands; the rows %s' % ' ; '.join(r[:20] for r in rows), 'the refusal appended to %s, a closed act`s bank' % o, 'the refusal appended to %s' % nw,
              o == 'b728_hook_refusals.txt' and len(rows) == 2, nw == 'b729_hook_refusals.txt')
    os.remove(os.path.join(d, 'data', 'b728_closing.txt'))
    n += 1
    g += guard(L, 'hookact', 'an open act keeps its own bank', os.path.basename(newh.refusals_path(d)), os.path.basename(newh.refusals_path(d)) == 'b728_hook_refusals.txt')
    return L, g, n


def control_answers():
    L, g, n = ['### (answers) THE ENTRY`S ANSWER CHECKS, (R340)(2)(v); THE INSTANCE, b729`S 0 AGAINST THREE'], 0, 0
    old = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rd('b729_citation_check.txt'), re.M))
    new = NO.answer_checks(rd('b729_answer_check.txt'))
    n += 1
    g += case(L, 'answers', 'b729`s entry, FINDINGS :12242', 'the count read from the step-zero citation bank: %d' % old, 'the count read from data/b729_answer_check.txt: %d' % new, old == 0, new == 3)
    return L, g, n


def control_n5line():
    L, g, n = ['### (n5line) THE CLOSING`S KERNELS LINE, (R340)(2)(vi): COMPOSED FROM N5`S CLAUSE, NOT CARRIED'], 0, 0
    carried = FF.n5_kernel_clause()
    for act, needle in (('b729', 'no kernel'), ('b730', 'zq-b730')):
        c = FF.n5_clause_of(rd('%s_ferry.txt' % act))
        n += 1
        g += case(L, 'n5line', '%s`s ferry: the closing`s line' % act, 'carried: "%s" (data/b729_closing.txt :325 the form), words %s`s N5 does not hold' % (carried, act), 'composed: "%s"' % c,
                  'README.md alone' not in rd('%s_ferry.txt' % act).split('(N5)')[1].split(NL)[0], bool(c) and needle in c and 'README.md alone' not in c)
    return L, g, n


def control_rootprompt():
    L, g, n = ['### (rootprompt) THE ROOT`S PROMPT COMPOSED, (R340)(2)(vii); THE INSTANCES, b729`S AND b728`S PROMPTS REGENERATED EQUAL TO WHAT WAS PUT',
               '  WHAT EQUALITY SHOWS: the form and the figures. The rows are cut from the text as put, so the words are the seat`s and the equal is no independent reading of them; the figures are what the composer checks against their bank lines.'], 0, 0
    otpl = _git('show', '%s:tools/standing/fold/record.tpl' % BASE)
    ntpl = open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    oldroute = 'hd = rdn(HEADS_DRAFT)' in otpl
    for act, ln in (('b729', 13), ('b728', 7)):
        t = rd('%s_author_answers.txt' % act).split(NL)[ln - 1]
        put = t.split('### PROMPT 2 (Close): ', 1)[1]
        rows = RPM.rows_from(put, line)
        cites = sum(1 for r in rows for p in r if isinstance(p, list))
        out = RPM.compose(rows, line)
        n += 1
        g += case(L, 'rootprompt', '%s`s close prompt, data/%s_author_answers.txt :%d, %d characters' % (act, act, ln, len(put)), 'the route printed b714`s heads draft: reads HEADS_DRAFT %s, the put text in its output False' % oldroute,
                  'composed from %d rows, %d figures found on their bank lines: equal to what was put %s' % (len(rows), cites, out == put), oldroute, out == put and cites >= 5)
        bad = [r if not any(isinstance(p, list) for p in r) else [[p[0], p[1], '999999'] if isinstance(p, list) else p for p in r] for r in rows]
        try:
            RPM.compose(bad, line)
            refused = False
        except SystemExit:
            refused = True
        n += 1
        g += guard(L, 'rootprompt', 'a figure not on its bank line refuses the prompt (%s, every figure made 999999)' % act, 'refused %s' % refused, refused)
    n += 1
    g += guard(L, 'rootprompt', 'the record tool`s route reads the act`s own rows and b714`s draft no longer', "reads HEADS_DRAFT in rootprompt %s" % ('hd = rdn(HEADS_DRAFT)' in ntpl), 'hd = rdn(HEADS_DRAFT)' not in ntpl and '_rootprompt_rows.json' in ntpl)
    return L, g, n


CONTROLS = dict(own=control_own, actroot=control_actroot, exercise=control_exercise, hookact=control_hookact, answers=control_answers, n5line=control_n5line, rootprompt=control_rootprompt)
ORDER = ('own', 'actroot', 'exercise', 'hookact', 'answers', 'n5line', 'rootprompt')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.10.0, (R340)(2)(i)-(vii): THE HAND-KEPT-NAMES CLASS, G-ACTROOT-BANKED AND THE ROUTE`S LIST, THE PRE-RUN OVER A COMMITTED BANK, THE HOOK AND A CLOSED ACT, THE ANSWER CHECKS, THE CLOSING`S KERNELS LINE, THE ROOT`S PROMPT (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.10.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1100.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1100.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
