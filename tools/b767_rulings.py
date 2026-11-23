# -*- coding: utf-8 -*-
"""tools/b767_rulings.py -- b767, (R377)(5), (6) and (7): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b766_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R377)(12) writes neither REGISTRY, ERRATA, the census,
the register nor the two files of the map, so OPEN_TRAILS is the one file here.

  ledgers c2 dry|write   Component 2 (data/b767_ferry.txt :117: "[S1]", "THE REGISTRATION AND THE WINDOW AT GRADED KNOTS, per (6)", "THE
                         LINES OF (7), [R1] and [A2]"), appended at OPEN_TRAILS' end, no line moving, <DATE> the UTC date of the write: one
                         dated head and under it, each a paragraph of its own, in the ruling's order --
                         [S1], and with it the entry line of W-ORD-SOURCE-BUILD in the form tools/standing/orderstate.py :26 reads, its words
                           and trigger cut from [S1]'s own text and read back as a part of it;
                         [G1] where data/b767_window.json reads HELD with its control AS WANTED (data/b767_window.txt), its fields from that
                           bank and the registration's commit; [G2] or [G3] are not this tool's until an Edit gives them;
                         [R1], and with it the entry line of W-ORD-NOVEMBER-RIDERS in that form, its words and trigger cut from [R1]'s
                           own text as [S1]'s are: [R1]'s text is marked as the order's entry line and (7)(c) names that form, which the
                           text as written (no '*Appended' head, no '**' about the name) does not take, so the text enters as written and
                           the line in the form after it;
                         [A2].
                         Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory, before and after: the two
                         orders added OPEN and no other order added or moving. Bank: data/b767_ledgers_c2.txt and .json, each text by line and
                         sha256; the texts' words printed by the dry run alone.
  ledgers c5 dry|write   Component 3's end, (R377)(4) and (5)(c), appended at OPEN_TRAILS' end, no line moving, under one dated head --
                         [P2] (data/b767_ferry.txt :62), where the closing theorem does not compile at this act: <commit> the act's closing
                           Lean commit, the last at which a restored build read exit 0 by tools/b767_controls.py verdicts() over
                           data/b767_dispatch_rows.json; <names> the plan's lemmas compiled there, each name in the population and COMPILED;
                           the step not sent, L9c, with the plan's later steps, each absent from the commit; every theorem of
                           `SIDEExplicitFormula.Window` in print_targets.txt at the commit found once by its declaration line (its
                           namespaces read from `namespace`, `section` and `end`), read at its statement (from its name to its first `:=`)
                           and graded by tools/e0_rule.py grade(head, 'theorem'), its lexicon extended in this tool by the two types
                           this act declares (E0_EXTENSION, the shared file not edited), its axioms print from the read of its run;
                         [S2] (data/b767_ferry.txt :78), where the trial reads [S2] by tools/b767_controls.py trial_state(): its fields from
                           the two reads of the trial and the route's words at data/b767_source_build.txt :62.
                         Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory: no order moving, none
                         added. Bank: data/b767_ledgers_c5.txt and .json.
[C7] or [C8] is a group this tool gains by an Edit committed before its run, where the closing build's read gives it.

No PLACE-papers line is printed but the texts this tool composes; the account is counted, never printed; no git write.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b767_worklist as K   # noqa: E402

ACT, NL = 'b767', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b767_ferry.txt')
FERRY_SHA = 'f4681dd8eec1cf96'   # ### data/b767_stepzero.txt :17: the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C1PP = '216d9715'                # ### PLACE-papers' one commit of the act before this write: the corrigendum (step 7, data/b767_events.txt (41))
WANT = dict(P1=(58, 58), P2=(62, 62), C7=(66, 66), C8=(70, 70), S1=(74, 74), S2=(78, 78), S3=(82, 82), G1=(86, 86), G2=(90, 90),
            G3=(94, 94), R1=(98, 98), A2=(102, 102))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
SOURCE, RIDERS = 'W-ORD-SOURCE-BUILD', 'W-ORD-NOVEMBER-RIDERS'
GROUPS = dict(c2=('S1', 'G1', 'R1', 'A2'), c5=('P2', 'S2'))
WTXT, WJSON = os.path.join(D, 'b767_window.txt'), os.path.join(D, 'b767_window.json')
WCTL = '  THE CONTROL AS WANTED (unit at '
SREF16 = '-6.62468014575'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def today():
    return time.strftime('%Y-%m-%d', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def fsha(p):
    try:
        with open(p, 'rb') as f:
            return sha(f.read())[:16]
    except OSError:
        return 'ABSENT'


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def ids():
    import b767_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def account():
    """the account read from the relay's remote at run time (as tools/project_set.py reads it); counted in the texts, never printed."""
    import project_set as PS
    return PS.owner()


def idcount(text, I, acct):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'), account=low.count(acct.lower()) if acct else -1)


def at_head(path):
    b = git(PP, 'show', 'HEAD:' + path, raw=True)
    with open(os.path.join(PP, *path.split('/')), 'rb') as f:
        w = f.read()
    if not b or b != w:
        die('%s: ITS WORKING FILE IS NOT ITS BYTES AT HEAD (%d, %d bytes)' % (path, len(b), len(w)))
    if b'\r' in b or not b.endswith(b'\n'):
        die('%s: CARRIAGE RETURNS OR NO FINAL LINE END' % path)
    return b.decode('utf-8')


# ================================================================================ THE TEXTS
def ferry():
    with open(FERRY, 'rb') as f:
        b = f.read()
    if sha(b)[:16] != FERRY_SHA:
        die('THE FERRY BANK IS NOT ITS STEP-ZERO BYTES (sha256 %s)' % sha(b)[:16])
    return b.decode('utf-8').split(NL)


def texts(L):
    """{key: (first line, last line, text)} for each piece between '---- [K] ...' and '---- end [K]'; the lines checked against WANT."""
    out = {}
    for i, l in enumerate(L):
        m = re.match(r'^---- \[([A-Z]\d*)\] ', l)
        if m:
            k = m.group(1)
            j = L.index('---- end [%s]' % k, i)
            out[k] = (i + 2, j, NL.join(L[i + 1:j]))
    got = dict((k, (a, b)) for k, (a, b, _t) in out.items())
    if got != WANT:
        die('THE RULING`S TEXTS NOT AT THEIR LINES: %s' % sorted(set(got.items()) ^ set(WANT.items())))
    return out


def pattern(tpl):
    pat = re.escape(tpl)
    for ph in sorted(set(FIELD.findall(tpl)), key=len, reverse=True):
        pat = pat.replace(re.escape(ph), '(.+?)')
    return pat


def fill(tpl, values):
    t = tpl
    for ph, v in values:
        if ph not in t:
            die('THE FIELD %r NOT IN ITS TEMPLATE' % ph)
        t = t.replace(ph, v, 1)
    return t


# ================================================================================ THE FIELDS, FROM THE BANKS
def g1_fields():
    """[G1]'s fields from data/b767_window.json and .txt; None where the reading is not HELD or the control's line not AS WANTED."""
    with open(WTXT, encoding='utf-8') as f:
        W = f.read().replace('\r', '').split(NL)
    if not any(l.startswith(WCTL) for l in W):
        return None, 'the window bank`s control line is not AS WANTED'
    with open(WJSON, encoding='utf-8') as f:
        js = json.load(f)
    if js.get('reading') != 'HELD' or js.get('letter') != '[G1]':
        return None, 'the window bank reads %s %s' % (js.get('reading'), js.get('letter'))
    if js['registration']['commit'] != K.REG_COMMIT:
        return None, 'the window bank`s registration %s is not the worklist`s REG_COMMIT %s' % (js['registration']['commit'], K.REG_COMMIT)
    b = js['budget']
    mant, ex = ('%.2e' % float(b['sum_abs_r_float'])).split('e')
    mid, rad = float(js['S'][0]), float(js['S'][1])
    if not mid + rad < 0:
        return None, 'the window bank`s ball of S is not below 0'
    val = '%.12g' % mid
    n, p, dg = js['ncoef'], js['primes'], b['uniform_digits']
    pl = [l for l in W if l.startswith('  THE SEAT`S PRICE THERE: ')]
    want = ['the DATA lemmas at %d coefficients:' % n, '%d lines generated (L2)' % (n + 20), 'the DATA parts 400-1,500 lines by hand and 2-5 dispatches',
            'the enclosures over %d primes: the table %d lines generated and 300-1,000 lines by hand, 1-3 dispatches, at %d digits' % (p, p, dg)]
    if len(pl) != 1 or not all(w in pl[0] for w in want):
        return None, 'the window bank`s price line not read once with its figures (%d lines)' % len(pl)
    price = ("the DATA lemmas, a coefficients' lemma of %d generated lines and 400-1,500 lines by hand in 2-5 dispatches, and the enclosures "
             "over %s primes at %d digits, a table of %d generated lines and 300-1,000 lines by hand in 1-3 dispatches (relay data/b767_window.txt)"
             % (n + 20, '{:,}'.format(p), dg, p))
    return dict(commit=js['registration']['commit'], n=str(n), value=val, primes='{:,}'.format(p),
                sabs='%s x 10^%d' % (mant, int(ex)), digits=str(dg), price=price), None


def entry_line(date, letter, clause, name, words, trigger):
    return ('*Appended %s by b767, under the author’s ruling `(R377)`%s %s -- THE ORDER **`%s`**: %s. Trigger: %s. Status: OPEN.*'
            % (date, clause, letter, name, words, trigger))


# ### each entry line's words and trigger cut from its own text of the ruling, between these marks, and read back as a part of it
CUTS = dict(S1=('; THE ORDER `W-ORD-SOURCE-BUILD` ENTERED: ', '. Its trigger: ', '(5)'),
            R1=('(7)(c): ', '. Its trigger: ', '(7)(c)'))


def cut(text, k):
    a, b, _cl = CUTS[k]
    if text.count(a) != 1 or text.count(b) != 1 or text.index(a) > text.index(b) or not text.endswith('.'):
        die('[%s]: ITS ENTRY WORDS NOT CUT ONCE FROM ITS TEXT' % k)
    words = text[text.index(a) + len(a):text.index(b)]
    trigger = text[text.index(b) + len(b):-1]
    return words, trigger


def entries(date, TP):
    out = {}
    for k, name in (('S1', SOURCE), ('R1', RIDERS)):
        words, trigger = cut(TP[k], k)
        out[k] = entry_line(date, '[%s]' % k, CUTS[k][2], name, words, trigger)
    return out


# ================================================================================ THE LEDGER
def compose(group, date, base):
    L = ferry()
    X = texts(L)
    TP = dict((k, X[k][2]) for k in X)
    E, miss = {}, []
    keys = GROUPS[group]
    gf, gwhy = g1_fields()
    E['S1'] = TP['S1']
    if gf:
        E['G1'] = fill(TP['G1'], [('<commit>', gf['commit']), ('<n>', gf['n']), ('<value>', gf['value']), ('<n>', gf['primes']),
                                  ('<figure>', gf['sabs']), ('<n>', gf['digits']), ('<the seat\'s figures>', gf['price'])])
    else:
        miss.append('[G1]: %s' % gwhy)
    E['R1'], E['A2'] = TP['R1'], TP['A2']
    EN = entries(date, TP)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b767, `(R377)`(5), (6) and (7): the lines the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b767_ferry.txt :73-:75, :85-:87 and :97-:103), appended at the end of the file (its last line :%d), so that no line before '
            'them moves: the build from source given its order; the window at knots graded by octave; the order of the November riders; the '
            'author’s rulings of 2026-11-22 and 2026-11-23. The lines of the proof and of the build from source are appended beneath them at '
            'Component 3 and after.' % (date, n_ot))
    paras = [head]
    for k in keys:
        if k not in E:
            continue
        paras.append(E[k])
        if k in EN:
            paras.append(EN[k])
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, miss=miss, text=ot, new=base + NL + ot + NL, head=head, keys=keys, gf=gf, n_ot=n_ot, EN=EN, paras=paras)


def ledgers(group, mode):
    from standing import orders as O
    from standing import orderstate as OS
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(group, date, base)
    E, new, TP = C['E'], C['new'], C['TP']
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + C['text'] + NL)) for k, v in E.items())
    left = sorted(set(m for m in FIELD.findall(C['text'])))
    ticks = [k + 1 for k, l in enumerate(C['text'].split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before = dict(O.read(base.split(NL)))
    after = dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(C['text'], I, acct)
    present = [k for k, v in E.items() if v in base] + [n for n in (SOURCE, RIDERS) if n in base]
    ems = dict((k, OS.ENTRYFORM.match(v)) for k, v in C['EN'].items())
    gf = C['gf'] or {}
    ctl = [('PLACE-papers` HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]), pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in C['keys'] if k in eq)), bool(eq) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(C['miss']) or 'none missing'), not C['miss'] and all(k in E for k in C['keys'])),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts, and neither order, in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[G1]: data/b767_window.json reads HELD, [G1], its registration the worklist`s REG_COMMIT %s, the window bank`s control AS WANTED' % K.REG_COMMIT,
            bool(gf)),
           ('[S1] and [R1]: each entry line in the form tools/standing/orderstate.py :26 reads, naming its order (%s)' % (
               ', '.join('%s %s' % (k, m.group(1) if m else None) for k, m in sorted(ems.items()))),
            bool(ems.get('S1')) and ems['S1'].group(1) == SOURCE and bool(ems.get('R1')) and ems['R1'].group(1) == RIDERS),
           ('each entry line`s words and trigger a part of its own text of the ruling, read back (%s)' % (
               ', '.join('%s %s' % (k, all(x in TP[k] for x in cut(TP[k], k))) for k in sorted(C['EN']))),
            all(all(x in TP[k] and x in C['EN'][k] for x in cut(TP[k], k)) for k in C['EN'])),
           ('each order`s first line in the appended text its ruling text, its entry line after it (%s)' % (
               ', '.join('%s :%s<:%s' % (k, C['text'].split(NL).index(E[k]) + 1, C['text'].split(NL).index(C['EN'][k]) + 1) for k in sorted(C['EN']))),
            all(C['text'].split(NL).index(E[k]) < C['text'].split(NL).index(C['EN'][k]) for k in C['EN'])),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving (moved %s)' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none'), not moved),
           ('the roster: %s and %s added OPEN and no other order added (added %s)' % (SOURCE, RIDERS, [(n, st(after, n)) for n in added]),
            added == sorted([SOURCE, RIDERS]) and all(st(after, n) == 'OPEN' for n in added))]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R377)(5), (6) AND (7), GROUP %s: OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
         '### tools/b767_rulings.py ledgers %s; PLACE-papers HEAD %s; the texts from the ferry bank (data/b767_ferry.txt, sha256 %s), the fields from'
         % (group, pp_head[:8], FERRY_SHA),
         '### data/b767_window.json and .txt (sha256 %s, %s) and the worklist`s REG_COMMIT %s; <DATE> %s; each text by line and sha256 here; no'
         % (fsha(WJSON), fsha(WTXT), K.REG_COMMIT, date),
         '### PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), [(n, st(after, n)) for n in added] or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    nl_ = new.split(NL)
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(C['text'])[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', C['head'])] + [(k, E[k]) for k in C['keys'] if k in E] + [('%s entry' % k, v) for k, v in sorted(C['EN'].items())]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    n_lines = len(C['paras']) - 1
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([S1] AND ITS ORDER`S ENTRY LINE, '
          '[G1], [R1] AND ITS ORDER`S ENTRY LINE, [A2]) ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              group.upper(), n_lines, sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(C['text'])
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b767_ledgers_%s.txt' % group), os.path.join(D, 'b767_ledgers_%s.json' % group)
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1, first_new=first, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(C['text'])[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()),
                            entry_lines=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in C['EN'].items()),
                            head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]], keys=list(C['keys']), g1=C['gf'],
                            roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


# ================================================================================ GROUP c5: [P2] AND [S2]
C2PP = 'ba23945a'                # ### PLACE-papers' last commit of the act before the c5 write: the lines of (5), (6) and (7) (step 25, data/b767_events.txt (55))
EF, EFK = K.EF_DIR, 'SIDE-explicit-formula'
NS = 'SIDEExplicitFormula.Window.'
WIN_DIR = 'SIDEExplicitFormula/Window/'
STD3 = '[propext, Classical.choice, Quot.sound]'
AX3 = {'propext', 'Classical.choice', 'Quot.sound'}
DROWS = os.path.join(D, 'b767_dispatch_rows.json')
SBANK = os.path.join(D, 'b767_source_build.txt')
PLAN = os.path.join(D, 'b767_plan.txt')
S2_ROUTE_LINE = 62               # ### data/b767_source_build.txt :62: THE ROUTE CHOSEN, (i), in the bank's words
S2_ROUTE = 'the workflow building the library in two parts within one run, the restore off'
P2 = dict(read=16, commit='89fd5b54')   # ### dispatch 16, the act's last restored build exiting 0 (data/b767_events.txt (105), (106))
STEP_ITEMS = ('b', 'c', 'd', 'e')
P2_PLAN = (('L9a', 'archJ_eq_double', 49), ('L9b', 'archJ_basis', 54), ('L9c', 'archJ_comb', 59), ('L10a', 'logPrime_bounds', 67),
           ('L10b', 'gamma_bounds', 75), ('L10c', 'logPi_bounds', 82), ('L11a', 'poleSum_comb', 89), ('L11b', 'logNat_primes', 92),
           ('L11c', 'arith_eq_comb', 95), ('L11d', 'window_arith_neg', 99), ('L12', 'controlFailureExists', 106))   # ### data/b767_plan.txt
P2_COMPILED = ('archJ_eq_double', 'archJ_basis', 'archJ_basis_local', 'logPrime_bounds', 'gamma_bounds', 'logPi_bounds', 'poleSum_comb',
               'logNat_eq', 'logNat_bounds')
P2_NOT = ('archJ_comb', 'arith_eq_comb', 'window_arith_neg', 'controlFailureExists')
P2_NAMES = ("of L9, L9a `archJ_eq_double` and L9b `archJ_basis` with `archJ_basis_local`, the band over the pairs within three knots; L10 "
            "whole, L10a `logPrime_bounds`, L10b `gamma_bounds` and L10c `logPi_bounds`; of L11, L11a `poleSum_comb` and L11b, the factoring "
            "of the integers to 16,390, as `logNat_eq` and `logNat_bounds`")
P2_STEP = ("L9c `archJ_comb`, the sums of L9b as the combination's coefficients, and after it L11c `arith_eq_comb`, L11d "
           "`window_arith_neg` and L12 `controlFailureExists`")
DECL_RE = re.compile(r'^(?:@\[[^\]\n]*\]\s*)?(?:(?:protected|private|nonrec)\s+)*(?:theorem|lemma)\s+([^\s(\[{:]+)')
NS_RE, SEC_RE, END_RE = re.compile(r'^namespace\s+(\S+)\s*$'), re.compile(r'^section(?:\s+\S+)?\s*$'), re.compile(r'^end(?:\s+\S+)?\s*$')
# ### the E0 rule's lexicon extended in this tool, the shared tools/e0_rule.py not edited (the form of tools/b735_ef.py :133 and
# ### tools/b703_record.py :571): the two types this act declares, each data, each read at its declaration line at the commit
E0_EXTENSION = {'LPEntry': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Window/LogBounds.lean :16 (structure, b767)'),
                'LPTree': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Window/LogBounds.lean :24 (inductive, b767)')}
E0_EXT_DECL = {'LPEntry': ('SIDEExplicitFormula/Window/LogBounds.lean', 16, 'structure LPEntry where'),
               'LPTree': ('SIDEExplicitFormula/Window/LogBounds.lean', 24, 'inductive LPTree where')}
_EXT = {}


def e0_extend():
    """the extension laid over the shared lexicon once; returns the keys the shared lexicon held before it (wanted none)."""
    import e0_rule as E0
    if 'held' not in _EXT:
        _EXT['held'] = sorted(k for k in E0_EXTENSION if k in E0.LEXICON)
        E0.LEXICON.update(E0_EXTENSION)
    return _EXT['held']


def drows():
    with open(DROWS, encoding='utf-8') as f:
        return json.load(f)


def reads_of(R):
    return dict((int(r['run']), r) for r in R if r.get('kind') == 'read' and r.get('kernel') == EFK)


def ax_within(ax):
    s = str(ax or '').strip()
    if not (s.startswith('[') and s.endswith(']')):
        return False
    return set(x.strip() for x in s[1:-1].split(',') if x.strip()) <= AX3


def gate_ok(gates):
    return bool(gates) and all(g['line'] and g['grade'] not in ('NOT READ', 'UNCLASSED') for g in gates)


def decls(src):
    """{full name: [line, ...]} for each theorem or lemma of a Lean source, its namespaces read from `namespace`, `section` and `end`."""
    stack, out = [], {}
    for i, l in enumerate(src.split(NL)):
        m = NS_RE.match(l)
        if m:
            stack.append(m.group(1))
            continue
        if SEC_RE.match(l):
            stack.append(None)
            continue
        if END_RE.match(l):
            if stack:
                stack.pop()
            continue
        m = DECL_RE.match(l)
        if m:
            out.setdefault('.'.join([s for s in stack if s] + [m.group(1)]), []).append(i + 1)
    return out


def e0_at(src, line):
    """the theorem's statement at its declaration line, from its name to its first `:=`, graded by tools/e0_rule.py."""
    import e0_rule as E0
    e0_extend()
    L = src.split(NL)
    m = DECL_RE.match(L[line - 1])
    start = sum(len(x) + 1 for x in L[:line - 1]) + m.end()
    end = src.find(':=', start)
    head = src[start:end] if end > 0 else ''
    try:
        g, why, _b = E0.grade(head, 'theorem')
    except Exception as ex:   # noqa: BLE001
        g, why = 'UNCLASSED', ' '.join(str(ex).split())[:300]
    return dict(line=line, grade=g, why=' '.join(str(why).split()))


def s2_fields(R):
    """[S2]'s fields from the trial's two reads; None where tools/b767_controls.py trial_state() does not read [S2]."""
    import b767_controls as C
    tr = C.trial_state(R)
    if tr['state'] != '[S2]':
        return None, 'the trial reads %s (%s)' % (tr['state'], tr.get('where'))
    pr, off = tr['pair'], tr['offs'][-1]
    on = reads_of(R).get(int(pr['runs'][0]))
    with open(SBANK, encoding='utf-8') as f:
        SB = f.read().replace('\r', '').split(NL)
    rl = SB[S2_ROUTE_LINE - 1] if len(SB) >= S2_ROUTE_LINE else ''
    low = off.get('runner_low_mb')
    lows = [x for x in (off.get('low_part_one'), off.get('low_part_two')) if x is not None]
    facts = dict(off_run=off.get('run'), on_run=on.get('run') if on else None, commit=str(off.get('built_ref'))[:8], low=low, lows=lows,
                 part_one_exit=off.get('part_one_exit'), untouched=bool((off.get('cache') or {}).get('untouched')),
                 sha_on=str(on.get('axioms_sha256'))[:16] if on else None, sha_off=str(off.get('axioms_sha256'))[:16],
                 route_line=bool(rl.startswith('  THE ROUTE CHOSEN, (i): ') and S2_ROUTE.upper() in rl))
    fields = [("<the route in the bank's words>", 'route (i), %s (relay data/b767_source_build.txt :%d)' % (S2_ROUTE, S2_ROUTE_LINE)),
              ('<commit>', facts['commit']), ('<id>', str(off.get('run'))), ('<figure>', '{:,}'.format(int(low)) if low is not None else 'NONE'),
              ('<id>', str(on.get('run') if on else 'NONE')), ('<hash>', str(pr.get('sha'))[:16])]
    return dict(fields=fields, facts=facts, tr=tr), None


def p2_fields(R):
    import b767_controls as C
    V = C.verdicts(R)
    lk = V['last_kernel'] or {}
    reads = reads_of(R)
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == EFK]
    d = [r for r in disp if r.get('n') == P2['read']]
    r = reads.get(int(d[-1]['run'])) if d else None
    if not r:
        return dict(miss='[P2]: no read of dispatch %d in data/b767_dispatch_rows.json' % P2['read'])
    commit = P2['commit']
    st = dict((x[0], (x[1], x[2])) for x in (r.get('names') or []))
    built = str(r.get('built_ref') or '').startswith(commit) and str(r.get('build_exit')) == '0' and r.get('verdict') == 'KERNEL'
    last = bool(lk) and int(lk.get('run', 0)) == int(r['run'])
    later_steps = [x.get('n') for x in disp if x.get('n', 0) > P2['read'] and x.get('item') in STEP_ITEMS]
    closing = [x for x in disp if x.get('item') == 'closing' and str(x.get('sha')).startswith(commit)]
    pt = [x.strip() for x in git(EF, 'show', '%s:print_targets.txt' % commit).split(NL) if x.strip().startswith(NS)]
    files = [p.strip() for p in git(EF, 'ls-tree', '--name-only', commit, WIN_DIR).split(NL) if p.strip().endswith('.lean')]
    where, srcs = {}, {}
    for p in files:
        srcs[p] = git(EF, 'show', '%s:%s' % (commit, p)).replace('\r', '')
        for full, lines in decls(srcs[p]).items():
            for ln in lines:
                where.setdefault(full, []).append((p, ln))
    gates = []
    for full in pt:
        loc = where.get(full, [])
        e = e0_at(srcs[loc[0][0]], loc[0][1]) if len(loc) == 1 else {}
        state, ax = st.get(full, (None, None))
        gates.append(dict(name=full, path=loc[0][0] if len(loc) == 1 else ('NOT FOUND' if not loc else 'IN %d PLACES' % len(loc)),
                          line=e.get('line'), grade=e.get('grade', 'NOT READ'), why=e.get('why', ''), state=state, axioms=ax, built=built))
    with open(PLAN, encoding='utf-8') as f:
        PL = f.read().replace('\r', '').split(NL)
    plan = [(lab, nm, ln, len(PL) >= ln and ('%s %s ' % (lab, nm)) in PL[ln - 1] + ' ') for lab, nm, ln in P2_PLAN]
    ext = [(k, p, ln, p in srcs and len(srcs[p].split(NL)) >= ln and srcs[p].split(NL)[ln - 1] == want) for k, (p, ln, want) in sorted(E0_EXT_DECL.items())]
    fields = [('<commit>', commit), ('<names>', P2_NAMES), ('<its name in the plan>', P2_STEP), ("<the error's opening line | not sent>", 'not sent')]
    return dict(fields=fields, gates=gates, read_names=sorted(n for n in st if n.startswith(NS)), r=r, last=last, later=later_steps,
                closing=closing, files=len(files), where=where, plan=plan, V=V, ext=ext, held=e0_extend())


def ledgers_c5(mode):
    from standing import orders as O
    group, date = 'c5', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    TP = dict((k, v[2]) for k, v in texts(ferry()).items())
    R = drows()
    s2, s2why = s2_fields(R)
    p2 = p2_fields(R)
    E, miss = {}, []
    if p2.get('miss'):
        miss.append(p2['miss'])
        p2 = dict(gates=[], read_names=[], r=None, last=False, later=[], closing=[], files=0, where={}, plan=[], fields=None, ext=[], held=['NOT READ'])
    else:
        E['P2'] = fill(TP['P2'], p2['fields'])
    if s2:
        E['S2'] = fill(TP['S2'], s2['fields'])
    else:
        miss.append('[S2]: %s' % s2why)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b767, `(R377)`(4) and (5)(c): the lines the ruling orders for OPEN_TRAILS where the closing theorem does not '
            'compile at this act and where the trial\'s run from source exits 0 with the restored run\'s axioms file** (relay '
            'data/b767_ferry.txt :61-:63 and :77-:79), appended at the end of the file (its last line :%d), so that no line before them moves: '
            'each compiled theorem of the Lean of this act read at its statement by the E0 gate (relay tools/e0_rule.py) before it is entered, '
            'its name in print_targets.txt at its commit and its axioms print banked (relay data/b767_dispatch_rows.json and '
            'data/b767_ledgers_c5.txt). Where the closing build from source and the restored build print different axioms files, [C7] is '
            'appended beneath them; where the closing build and its repeat each stop under the hold, [C8].' % (date, n_ot))
    paras = [head] + [E[k] for k in GROUPS[group] if k in E]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    before, after = dict(O.read(base.split(NL))), dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    gates = p2['gates']
    grades, axs = {}, {}
    for g in gates:
        grades[g['grade']] = grades.get(g['grade'], 0) + 1
        axs[str(g['axioms'])] = axs.get(str(g['axioms']), 0) + 1
    pop = sorted(g['name'] for g in gates)
    plant_gate = gate_ok([dict(gates[0], line=None, grade='NOT READ')] + gates[1:]) if gates else True
    plant_pop = (pop + [NS + 'b999_planted']) == p2['read_names']
    r = p2['r'] or {}
    sf = (s2 or {}).get('facts') or {}
    absent = [s for s in P2_COMPILED if NS + s not in pop or dict((g['name'], g['state']) for g in gates).get(NS + s) != 'COMPILED']
    present_not = [s for s in P2_NOT if NS + s in pop or NS + s in p2['where']]
    ctl = [('PLACE-papers` HEAD the act`s last commit there before this write, the lines of (5), (6) and (7) %s (%s)' % (C2PP, pp_head[:8]),
            pp_head.startswith(C2PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in GROUPS[group] if k in eq)), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[S2]: tools/b767_controls.py trial_state() reads [S2] (%s)' % (s2['tr']['state'] if s2 else s2why), bool(s2)),
           ('[S2]: the run from source %s at %s, its cache untouched, its part one`s exit %s; the restored run %s; the axioms files` sha256 %s and %s' % (
               sf.get('off_run'), sf.get('commit'), sf.get('part_one_exit'), sf.get('on_run'), sf.get('sha_on'), sf.get('sha_off')),
            bool(sf) and sf['untouched'] and sf['part_one_exit'] == '0' and sf['sha_on'] == sf['sha_off'] and sf['on_run'] is not None),
           ('[S2]: its low %s MB the least of its two parts` lows %s and above the hold`s 2,560' % (sf.get('low'), sf.get('lows')),
            bool(sf) and sf['low'] is not None and bool(sf['lows']) and sf['low'] == min(sf['lows']) and sf['low'] > 2560),
           ('[S2]: the route`s words read at data/b767_source_build.txt :%d, THE ROUTE CHOSEN, (i)' % S2_ROUTE_LINE, bool(sf) and sf['route_line']),
           ('[P2]: THE RUN: dispatch %d read, built at %s with exit 0, KERNEL (run %s)' % (P2['read'], P2['commit'], r.get('run')),
            bool(gates) and all(g['built'] for g in gates)),
           ('[P2]: <commit> the act`s closing Lean commit: the last restored read exiting 0 by verdicts() is dispatch %d`s (%s)' % (
               P2['read'], p2['last']), p2['last']),
           ('[P2]: no step dispatched after it (%s) and the closing build sent at %s (%d row)' % (p2['later'] or 'none', P2['commit'], len(p2['closing'])),
            not p2['later'] and len(p2['closing']) == 1),
           ('[P2]: THE POPULATION: the names of %s in print_targets.txt at %s (%d) equal both ways to those the read of dispatch %d names (%d)' % (
               NS, P2['commit'], len(pop), P2['read'], len(p2['read_names'])), bool(pop) and pop == p2['read_names']),
           ('[P2]: THE E0 RULE`S LEXICON extended in this tool, tools/e0_rule.py not edited: %s each data, each read at its declaration line at the '
            'commit (%s), none held by the shared lexicon before (held: %s)' % (
                ' and '.join(sorted(E0_EXTENSION)), ' '.join('%s :%d %s' % (k, ln, ok_) for k, _p, ln, ok_ in p2['ext']) or 'none', p2['held'] or 'none'),
            len(p2['ext']) == len(E0_EXTENSION) and all(x[3] for x in p2['ext']) and not p2['held']),
           ('[P2]: THE E0 GATE: each of the %d theorems found once by its declaration line among the %d Window files at the commit, read at its '
            'statement and graded (%s)' % (len(gates), p2['files'], ', '.join('%s %d' % kv for kv in sorted(grades.items()))), gate_ok(gates)),
           ('[P2]: each COMPILED in the read, its axioms within %s, sorryAx in none (the prints: %s)' % (
               STD3, '; '.join('%s %d' % kv for kv in sorted(axs.items()))),
            bool(gates) and all(g['state'] == 'COMPILED' and ax_within(g['axioms']) for g in gates)),
           ('[P2]: the %d names <names> gives each in the population and COMPILED (absent: %s)' % (len(P2_COMPILED), absent or 'none'), not absent),
           ('[P2]: the %d names of the steps not sent each declared nowhere at the commit (present: %s)' % (len(P2_NOT), present_not or 'none'),
            not present_not),
           ('[P2]: the plan`s steps each at its line of data/b767_plan.txt (%s)' % (
               ' '.join('%s:%d %s' % (lab, ln, ok_) for lab, _nm, ln, ok_ in p2['plan']) or 'none'),
            len(p2['plan']) == len(P2_PLAN) and all(x[3] for x in p2['plan'])),
           ('PLANTED: a gate row with no statement read as the gate`s failure, and a planted name as the population`s (%s, %s)' % (
               'FAILED' if not plant_gate else 'PASSED', 'DIFFER' if not plant_pop else 'EQUAL'), not plant_gate and not plant_pop),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R377)(4) AND (5)(c), GROUP C5: [P2] AND [S2], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b767_rulings.py ledgers c5; PLACE-papers HEAD %s; the texts from the ferry bank (data/b767_ferry.txt, sha256 %s), the fields from'
         % (pp_head[:8], FERRY_SHA),
         '### data/b767_dispatch_rows.json (sha256 %s), data/b767_source_build.txt (sha256 %s) and SIDE-explicit-formula at %s; <DATE> %s; each'
         % (fsha(DROWS), fsha(SBANK), P2['commit'], date),
         '### text by line and sha256 here; no PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE E0 GATE (tools/e0_rule.py grade(head, \'theorem\'), the head the statement from the name to its first `:=`, read at %s)' % P2['commit']]
    P += ['  %-60s %s :%s ; GRADE %s ; %s ; %s %s' % (g['name'], g['path'], g['line'], g['grade'], g['why'] or '-', g['state'], g['axioms'])
          for g in gates]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    nl_ = new.split(NL)
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in GROUPS[group] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C5: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([P2], [S2]) ; THE E0 GATE %d OF %d '
          'READ ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(paras) - 1, sum(1 for g in gates if g['line']), len(gates), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b767_ledgers_c5.txt'), os.path.join(D, 'b767_ledgers_c5.json')
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=n_ot, lines_after=len(nl_) - 1, first_new=n_ot + 2, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()), head=[nl_.index(head) + 1, sha(head)[:16]],
                            keys=list(GROUPS[group]), run=r.get('run'), commit=P2['commit'], s2=sf,
                            e0=[dict((x, g[x]) for x in ('name', 'path', 'line', 'grade', 'why', 'state', 'axioms')) for g in gates],
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    if argv[1] == 'c5':
        return ledgers_c5(argv[2])
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
