# -*- coding: utf-8 -*-
"""tools/b762_rulings.py -- b762, (R372)(7) and (8), with (5)'s [O6]: THE AUTHOR'S WORD BANKED; THE ORDERS ENTERED AT OPEN_TRAILS' END
UNDER ONE DATED HEAD.

Written by the Write tool at b762's Component 5 and committed before it runs (N2). Its forms are tools/b761_rulings.py's.

  bank dry|write      (8): data/b762_author_rulings.txt -- [W1] read from the ferry bank by its marker lines, verbatim: the author's word
                      (data/b762_ferry.txt :38) beside its rendering, the navigator's (:39), for the author's strike.
  trail dry|write     OPEN_TRAILS.md, appended at its end after b761's trail and before this act's own trail, no line moving, its bytes at
                      HEAD a prefix of its new bytes: one dated head for (7) and (8); under it [T1] to [T14] and [D1] ((7)); one line
                      naming the bank of [W1], then [O1] to [O5] and [P1] ((8)); then [O6], which (5) enters where the map finds a
                      PROOF-WORDED line in a live paper (data/b762_onepage_map.json: o6, d), its <d> filled; each a paragraph of its own.
                      Controls before the write: each text as entered equal to the ferry's with its fields filled and whole in the
                      appended text; no field left; each appended line's backticks even; the identifiers 0 in the appended text and their
                      counts equal before and after; the author-rulings bank written, its two lines whole; [D1]'s declaration at its line
                      at v0.41 (a predicate, no kernel line printed). THE ROSTER, printed and no condition ((7): a status that reads
                      otherwise is printed with its line, left as the reader gives it, and lettered for the navigator): tools/standing/
                      orders.py's rule in memory over the new OPEN_TRAILS, W-ORD-EPSTEIN-COUNT-LEAN CLOSED, the orders of [T1] to [T14] and
                      [P1] OPEN, the orders [O1] to [O6] enter OPEN, no other status moving, the roster 84 open with [O6] and 83 without.
                      Bank: data/b762_ledgers.txt and .json, the appended text by line and sha256, its words printed by the dry run alone.

No PLACE-papers line is printed but the texts this tool composes; no git write.
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
import subject as S   # noqa: E402

ACT, NL = 'b762', '\n'
PP = S.PP
FERRY = os.path.join(D, 'b762_ferry.txt')
FERRY_SHA = 'ed3bc80749d12e66'   # ### data/b762_stepzero.txt: the ferry bank's sha256
MAPJ = os.path.join(D, 'b762_onepage_map.json')
OT = 'OPEN_TRAILS.md'
EF_REPO, EF_TAG = 'D:/SIDE-explicit-formula', 'v0.41'
D1_DECL = ('zq_count_holds', 'SIDEExplicitFormula/Schema/ZQ/Count.lean', 338)
WANT = dict(W1=(38, 39), T1=(43, 43), T2=(47, 47), T3=(51, 51), T4=(55, 55), T5=(59, 59), T6=(63, 63), T7=(67, 67), T8=(71, 71),
            T9=(75, 75), T10=(79, 79), T11=(83, 83), T12=(87, 87), T13=(91, 91), T14=(95, 95), D1=(99, 99), O1=(103, 103), O2=(107, 107),
            O3=(111, 111), O4=(115, 115), O5=(119, 119), O6=(123, 123), P1=(127, 127), G1=(131, 131), G2=(135, 135), H=(139, 150))
T_KEYS = ['T%d' % i for i in range(1, 15)]
O_KEYS = ['O%d' % i for i in range(1, 6)]
CLOSING = 'W-ORD-EPSTEIN-COUNT-LEAN'
OPEN_WANT = (84, 83)   # ### (7): the roster with [O6] and without
NAME = re.compile(r'`(W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*)`')
RBANK = os.path.join(D, 'b762_author_rulings.txt')
LBANK = os.path.join(D, 'b762_ledgers.txt')
LJSON = os.path.join(D, 'b762_ledgers.json')


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
    import b762_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def idcount(text, I):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'))


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


def mapj():
    j = json.load(open(MAPJ, encoding='utf-8'))
    return bool(j['o6']), int(j['d'])


# ================================================================================ (8) THE AUTHOR'S WORD BANK
def compose_bank(X):
    a, b, t = X['W1']
    word, rend = t.split(NL)
    if not rend.startswith("RENDERING, the navigator's: "):
        die('[W1]`S SECOND LINE IS NOT ITS RENDERING')
    L = ['%s -- (R372)(8): THE AUTHOR`S WORD OF 2026-11-18 BESIDE ITS RENDERING, THE NAVIGATOR`S, FOR THE AUTHOR`S STRIKE (%s)' % (ACT, utc()), '',
         '### tools/b762_rulings.py bank: read from the ferry bank data/b762_ferry.txt (sha256 %s...) by its marker lines (:%d-:%d), verbatim,' % (FERRY_SHA, a - 1, b + 1),
         '### nothing changed; the rendering is the navigator`s, for the author`s strike ((R372)(8)).', '',
         '## [W1] THE AUTHOR`S WORD, 2026-11-18, VERBATIM (data/b762_ferry.txt :%d)' % a, word, '',
         '## ITS RENDERING, THE NAVIGATOR`S (data/b762_ferry.txt :%d)' % b, rend, '',
         '### ### **THE AUTHOR`S RULINGS: WORDS 1, VERBATIM FROM THE FERRY ; ITS RENDERING THE NAVIGATOR`S ; NOTHING CHANGED.**']
    return NL.join(L) + NL, word, rend


def bank(mode):
    X = texts(ferry())
    text, word, rend = compose_bank(X)
    I = ids()
    n_id = sum(idcount(text, I).values())
    whole = (NL + word + NL) in text and (NL + rend + NL) in text
    ok = n_id == 0 and whole
    print(text if mode == 'dry' else text.split(NL)[0])
    print('### the identifiers in the bank %d ; the word and its rendering carried whole %s ; %s' % (
        n_id, whole, 'DRY, NOTHING WRITTEN' if mode == 'dry' else ('WRITTEN' if ok else 'HELD')))
    if mode == 'dry':
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(RBANK):
        die('THE BANK STANDS ALREADY')
    put(RBANK, text)
    print('written data/b762_author_rulings.txt (%d lines, sha256 %s)' % (len(text.split(NL)) - 1, sha(text)[:16]))


# ================================================================================ (7) AND (8) THE TRAIL'S LINES
def compose_trail(date, base, o6, d):
    X = texts(ferry())
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b762, `(R372)`(7) and (8): the lines the ruling orders for OPEN_TRAILS** (relay data/b762_ferry.txt :21, :23, '
            'and :17 for the last), appended at the end of the file after b761’s trail (its last line :%d) and before this act’s own trail, so '
            'that no line of the trail moves: each order whose trigger the sitting’s agenda (relay data/b761_sitting_agenda.txt :136) reads as '
            'met, named with the act that takes it; each of the four orders that carried no trigger, given one; one order discharged at its '
            'instance; the line naming the author’s word of 2026-11-18 and its rendering; the orders the reflection enters, and one carried '
            'with its list grown%s.' % (
                date, n_ot, '; and, by `(R372)`(5), the order on the lines that name One Page beside the word proof' if o6 else ''))
    wline = ('The author’s word of 2026-11-18, “%s”, stands verbatim in relay `data/b762_author_rulings.txt` beside its rendering, the '
             'navigator’s, for the author’s strike (`(R372)`(8)).' % X['W1'][2].split(NL)[0])
    entered = dict((k, X[k][2]) for k in T_KEYS + ['D1'] + O_KEYS + ['P1'])
    if o6:
        if X['O6'][2].count('<d>') != 1:
            die('[O6] DOES NOT CARRY ITS FIELD ONCE')
        entered['O6'] = X['O6'][2].replace('<d>', str(d))
    paras = [head] + [entered[k] for k in T_KEYS + ['D1']] + [wline] + [entered[k] for k in O_KEYS + ['P1']] + ([entered['O6']] if o6 else [])
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, text=ot, new=base + NL + ot + NL, entered=entered, head=head, wline=wline, ot_first=n_ot + 2, n_ot=n_ot)


def roster(lines):
    from standing import orders as O
    return dict(O.read(lines))


def decl_d1():
    name, path, k = D1_DECL
    L = git(EF_REPO, 'show', '%s:%s' % (EF_TAG, path)).split(NL)
    ln = L[k - 1] if 0 < k <= len(L) else ''
    return bool(re.search(r'\b(theorem|lemma|def|abbrev)\s+(\S+\.)?%s\b' % re.escape(name), ln)), len(L)


def trail(mode):
    date = today()
    o6, d = mapj()
    base = at_head(OT)
    if '**Dated head, ' in base and ', b762, `(R372)`(7) and (8):' in base:
        die('OPEN_TRAILS CARRIES THIS ACT`S DATED HEAD ALREADY')
    C = compose_trail(date, base, o6, d)
    X, new, E_ = C['X'], C['new'], C['entered']
    I = ids()
    filled = dict((k, X[k][2]) for k in T_KEYS + ['D1'] + O_KEYS + ['P1'])
    if o6:
        filled['O6'] = X['O6'][2].replace('<d>', str(d))
    eq = dict((k, E_[k] == filled[k] and (NL + E_[k] + NL) in (NL + C['text'] + NL)) for k in filled)
    left = [k for k, v in E_.items() if re.search(r'<[a-z]+>|<DATE>', v)]
    ticks = [k + 1 for k, l in enumerate(C['text'].split(NL)) if l.count('`') % 2]
    rb = open(RBANK, encoding='utf-8').read() if os.path.isfile(RBANK) else ''
    rb_ok = bool(rb) and all((NL + x + NL) in rb for x in X['W1'][2].split(NL))
    dok, dn = decl_d1()
    # ### the roster, in memory, before and after
    before, after = roster(base.split(NL)), roster(new.split(NL))
    names = dict((k, NAME.findall(E_[k])[:1]) for k in E_)
    t_names = [names[k][0] for k in T_KEYS if names[k]]
    o_names = [names[k][0] for k in O_KEYS + (['O6'] if o6 else []) if names[k]]
    p_name = names['P1'][0] if names['P1'] else None
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    want_open = OPEN_WANT[0] if o6 else OPEN_WANT[1]
    R = [('%s CLOSED' % CLOSING, (st(before, CLOSING), st(after, CLOSING), (after.get(CLOSING) or {}).get('decided_at')), st(after, CLOSING) == 'CLOSED'),
         ('the orders of [T1] to [T14] and [P1], each entered before and OPEN after', [(n, st(before, n), st(after, n)) for n in t_names + [p_name] if st(after, n) != 'OPEN' or n not in before] or 'all %d' % (len(t_names) + 1),
          len(t_names) == 14 and all(n in before and st(after, n) == 'OPEN' for n in t_names + [p_name])),
         ('the orders [O1] to [O%d] enter, each OPEN' % (6 if o6 else 5), [(n, st(after, n), (after.get(n) or {}).get('entry')) for n in o_names],
          sorted(o_names) == added and all(st(after, n) == 'OPEN' for n in o_names)),
         ('no other order`s status moves', [m for m in moved if m != CLOSING] or 'none', not [m for m in moved if m != CLOSING]),
         ('the roster open, before -> after, wanted %d' % want_open, '%d -> %d (orders %d -> %d)' % (open_b, open_a, len(before), len(after)), open_a == want_open)]
    ctl = [('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('[T1] to [T14], [D1], [O1] to [O5], [P1]%s as entered equal the ruling`s texts with their fields filled, each whole in the appended text' % (', [O6]' if o6 else ''),
            all(eq.values()) and not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts equal before and after, and 0 in the appended text', idcount(base, I) == idcount(new, I) and not any(idcount(C['text'], I).values())),
           ('the author-rulings bank written, its word and rendering whole (sha256 %s)' % (sha(rb)[:16] if rb else 'ABSENT'), rb_ok),
           ('[D1]`s declaration %s at %s :%d at %s (a predicate; file lines %d)' % (D1_DECL[0], D1_DECL[1], D1_DECL[2], EF_TAG, dn), dok)]
    ok = all(o for _w, o in ctl)
    nl_ = new.split(NL)
    P = ['%s -- (R372)(7) AND (8), WITH (5)`S [O6]: OPEN_TRAILS APPENDED AT ITS END UNDER ONE DATED HEAD (%s)' % (ACT, utc()), '',
         '### tools/b762_rulings.py trail; PLACE-papers HEAD %s; the texts from the ferry bank (data/b762_ferry.txt :%d-:%d), [O6]`s <d> %d from' % (
             git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), WANT['T1'][0], WANT['P1'][1], d),
         '### data/b762_onepage_map.json (o6 %s), and the seat`s two lines (the dated head and the line naming the bank of [W1]); DATE %s.' % (o6, date), '',
         '## THE CONTROLS']
    P += ['  %-130s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed; (7): a status otherwise is lettered for the navigator, not held)']
    P += ['  %s: %s -> %s' % (w, g, 'AS WANTED' if o else 'OTHERWISE') for w, g, o in R]
    P += ['', '## THE FILE: %s | lines %d -> %d | the appended text from :%d (the dated head), its sha256 %s | the file`s sha256 %s -> %s' % (
        OT, C['n_ot'], len(nl_) - 1, C['ot_first'], sha(C['text'])[:16], sha(base)[:16], sha(new)[:16])]
    P += ['## THE PARAGRAPHS BY LINE: ' + ' ; '.join('%s :%d' % (k, nl_.index(v) + 1) for k, v in
                                                     [('head', C['head'])] + [(k, E_[k]) for k in T_KEYS + ['D1']] + [('W1 line', C['wline'])] +
                                                     [(k, E_[k]) for k in O_KEYS + ['P1'] + (['O6'] if o6 else [])])]
    P += ['', '### ### **THE TRAIL`S LINES: %d PARAGRAPHS APPENDED, NO LINE MOVING ; [O6] %s ; THE ROSTER %d OPEN, WANTED %d, %d OF %d AS WANTED ; '
              'CONTROLS %d OF %d AS WANTED ; %s.**' % (len(E_) + 2, 'ENTERED, d %d' % d if o6 else 'NOT ENTERED', open_a, want_open, sum(1 for r in R if r[2]), len(R),
                                                     sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO %s (the dry run`s print alone):' % OT)
        print(C['text'])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(LBANK):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, date=date, o6=o6, d=d,
                               files=[dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1, first_new=C['ot_first'], text_sha=sha(C['text'])[:16],
                                           sha_before=sha(base)[:16], sha_after=sha(new)[:16], prefix=new.startswith(base))],
                               entered=dict((k, sha(v)[:16]) for k, v in E_.items()), head_sha=sha(C['head'])[:16], wline_sha=sha(C['wline'])[:16],
                               roster=dict(before_open=open_b, after_open=open_a, want=want_open, closing=[CLOSING, st(before, CLOSING), st(after, CLOSING)],
                                           added=added, moved=moved, rows=[[w, str(g), o] for w, g, o in R]),
                               controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; data/b762_ledgers.txt and .json')


def main(argv):
    what, mode = (argv + ['', ''])[:2]
    if mode not in ('dry', 'write'):
        sys.exit(__doc__)
    if what == 'bank':
        bank(mode)
    elif what == 'trail':
        trail(mode)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
