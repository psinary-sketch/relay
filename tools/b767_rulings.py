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
The groups of Component 3 to 5 ([P1] or [P2], [S2] or [S3], [C7] or [C8]) are groups this tool gains by Edits committed before their runs.

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
GROUPS = dict(c2=('S1', 'G1', 'R1', 'A2'))
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


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
