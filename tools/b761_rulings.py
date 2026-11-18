# -*- coding: utf-8 -*-
"""tools/b761_rulings.py -- b761, (R371)(7) and (8), with the author's words of 2026-11-18 given during the act (b761 events (18) and
(43)): THE AUTHOR'S RULINGS BANKED AND ENTERED; TWO ORDERS CLOSED IN THE ROSTER'S FORM.

Written by the Write tool at b761's Component 2 and committed before it runs (N2). Its forms are tools/b760_ledgers.py's.

  bank dry|write      (7): data/b761_author_rulings.txt -- [W1] to [W3] read from the ferry bank by their marker lines, verbatim, each
                      beside its rendering ([W1] beside [A1]; [W2] beside [A2]; [W3] beside the clause of [A2] that renders it), the
                      rendering the navigator's, for the author's strike.
  ledgers dry|write   appended at each file's end, no line moving, each file's bytes at HEAD a prefix of its new bytes, <DATE> the UTC
                      date of the write:
                      REGISTRY.md, [A1] with <DATE> filled, after one blank line; rule [Q] (3)'s heading read by its digest at one line
                      before and after, no line above it changing;
                      phase1.5/method/THE_METHOD_CANON.md, [A2] with <DATE> filled, in the form XXII and XXIII were appended (two blank
                      lines, a comment marker, a blank line, the section); after it one dated foot line beside XXIII (C) quoting the
                      author's item (4), item (3) and second word (b761 events (18), (43): beyond the section (12) excepts, on the
                      author's later word, lettered for the navigator);
                      OPEN_TRAILS.md, one dated head for (7) and (8) and under it the line naming [A1]'s block, [A3], [B1] and [B2] with
                      their fields filled; then one dated head for the author's words given during the act, items (1) to (3) and the
                      second word each quoted beside its number, no status word beside an order's name.
                      Controls before the write: each of [A1] to [A3], [B1] and [B2] as entered equal to the ferry's text with its
                      fields filled; [B1]'s and [B2]'s cited lines naming their orders; tools/standing/orders.py's rule run in memory
                      over the new OPEN_TRAILS reading the two orders CLOSED and moving no other order's status; each appended line's
                      backticks even; the identifiers 0 in the texts and their counts equal in each file before and after; the
                      author-rulings bank written and read equal. Bank: data/b761_ledgers.txt and .json, each appended text by line and
                      sha256, its words printed by the dry run alone.

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

ACT, NL = 'b761', '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
FERRY = os.path.join(D, 'b761_ferry.txt')
FERRY_SHA = 'cf0dfbc0a0ce410a'   # ### data/b761_stepzero.txt: the ferry bank's sha256
WORDS = os.path.join(D, 'b761_author_words_preseal.txt')
REG, OT, CANON = 'REGISTRY.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_METHOD_CANON.md'
FILES = (REG, CANON, OT)
QHEAD, QLINE = '53d53060a58f6b9b', 374   # ### rule [Q] (3)'s heading, by the sha256 of its line, at REGISTRY :374 ((R371)(7))
WANT = dict(W1=(38, 38), W2=(42, 42), W3=(46, 46), A1=(50, 52), A2=(56, 60), A3=(64, 64), B1=(68, 68), B2=(72, 72))
B_LINES = (('B1', 'W-ORD-MECHANISM-ATTRIBUTION', 18695), ('B2', 'W-ORD-WSC-KERNEL-CITES', 18697))
CLOSING = ('W-ORD-MECHANISM-ATTRIBUTION', 'W-ORD-WSC-KERNEL-CITES')
OPENING = 'My word, 2026-11-18, for the record.'
W3_CLAUSE = 'each keystone is to inform standing alone'
RBANK = os.path.join(D, 'b761_author_rulings.txt')
LBANK = os.path.join(D, 'b761_ledgers.txt')
LJSON = os.path.join(D, 'b761_ledgers.json')


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
    import b761_address_scan as SC
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
        m = re.match(r'^---- \[([A-Z]\d)\] ', l)
        if m:
            k = m.group(1)
            j = L.index('---- end [%s]' % k, i)
            out[k] = (i + 2, j, NL.join(L[i + 1:j]))
    got = dict((k, (a, b)) for k, (a, b, _t) in out.items())
    if got != WANT:
        die('THE RULING`S TEXTS NOT AT THEIR LINES: %s' % sorted(got.items()))
    return out


def author_words():
    """the author's two words of the act, from their bank: (line, {item: words}) of the first and (line, words) of the second."""
    with open(WORDS, encoding='utf-8') as f:
        L = f.read().replace('\r', '').split(NL)
    w1 = [(i + 1, l) for i, l in enumerate(L) if l.startswith(OPENING + ' (1) ')]
    w2 = [(i + 1, l) for i, l in enumerate(L) if l.startswith(OPENING + ' A trigger, when met')]
    if len(w1) != 1 or len(w2) != 1:
        die('THE AUTHOR`S WORDS NOT READ ONCE EACH (%d, %d)' % (len(w1), len(w2)))
    (n1, t1), (n2, t2) = w1[0], w2[0]
    rest = t1[len(OPENING):]
    parts = re.split(r' \(([1-4])\) ', rest)
    items = dict((parts[i], parts[i + 1].strip()) for i in range(1, len(parts), 2))
    if parts[0] != '' or sorted(items) != ['1', '2', '3', '4'] or ' '.join('(%s) %s' % (k, items[k]) for k in '1234') != rest.strip():
        die('THE FIRST WORD`S ITEMS NOT READ AS (1) TO (4) WHOLE')
    return n1, items, n2, t2[len(OPENING):].strip()


def w3_clause(a2):
    i = a2.find(W3_CLAUSE)
    if i < 0 or a2.count(W3_CLAUSE) != 1:
        die('[A2] DOES NOT CARRY THE CLAUSE THAT RENDERS [W3] ONCE')
    j = a2.find('. ', i)
    return a2[i:j + 1]


# ================================================================================ (7) THE AUTHOR'S RULINGS BANK
def compose_bank(X):
    a2 = X['A2'][2]
    c3 = w3_clause(a2)
    a2_58 = [k for k, l in enumerate(a2.split(NL), X['A2'][0]) if W3_CLAUSE in l]
    L = ['%s -- (R371)(7): THE AUTHOR`S WORDS OF 2026-11-18 ON THE PHASES, ON WHAT A KEYSTONE CARRIES AND ON A DOCUMENT STANDING ALONE, EACH '
         'BESIDE ITS RENDERING (%s)' % (ACT, utc()), '',
         '### tools/b761_rulings.py bank: read from the ferry bank data/b761_ferry.txt (sha256 %s...) by its marker lines, verbatim, nothing changed;' % FERRY_SHA,
         '### each rendering is the navigator`s, for the author`s strike ((R371)(7)); a rendering`s <DATE> is filled where it is entered, not here.', '',
         '## [W1] THE AUTHOR`S WORDS ON THE PHASES, 2026-11-18, VERBATIM (data/b761_ferry.txt :%d)' % X['W1'][0], X['W1'][2], '',
         '## ITS RENDERING, THE NAVIGATOR`S: [A1], for REGISTRY`s end (data/b761_ferry.txt :%d-:%d)' % X['A1'][:2]] + X['A1'][2].split(NL) + ['',
         '## [W2] THE AUTHOR`S WORDS ON WHAT A KEYSTONE CARRIES, 2026-11-18, VERBATIM (data/b761_ferry.txt :%d)' % X['W2'][0], X['W2'][2], '',
         '## ITS RENDERING, THE NAVIGATOR`S: [A2], for THE_METHOD_CANON.md`s end (data/b761_ferry.txt :%d-:%d)' % X['A2'][:2]] + a2.split(NL) + ['',
         '## [W3] THE AUTHOR`S WORDS ON A DOCUMENT STANDING ALONE, 2026-11-18, VERBATIM (data/b761_ferry.txt :%d)' % X['W3'][0], X['W3'][2], '',
         '## ITS RENDERING, THE NAVIGATOR`S: the clause of [A2] that carries it (data/b761_ferry.txt :%d), the seat`s reading of where it stands' % a2_58[0],
         c3, '',
         '### ### **THE AUTHOR`S RULINGS: WORDS 3, EACH VERBATIM FROM THE FERRY ; RENDERINGS [A1] AND [A2], THE NAVIGATOR`S ; NOTHING CHANGED.**']
    return NL.join(L) + NL, c3


def bank(mode):
    X = texts(ferry())
    text, _c3 = compose_bank(X)
    I = ids()
    n_id = sum(idcount(text, I).values())
    ok = n_id == 0 and all(X[k][2] in text for k in ('W1', 'W2', 'W3', 'A1', 'A2'))
    print(text if mode == 'dry' else text.split(NL)[0])
    print('### the identifiers in the bank %d ; the five texts carried whole %s ; %s' % (
        n_id, all(X[k][2] in text for k in ('W1', 'W2', 'W3', 'A1', 'A2')), 'DRY, NOTHING WRITTEN' if mode == 'dry' else ('WRITTEN' if ok else 'HELD')))
    if mode == 'dry':
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    put(RBANK, text)
    print('written data/b761_author_rulings.txt (%d lines, sha256 %s)' % (len(text.split(NL)) - 1, sha(text)[:16]))


# ================================================================================ (7) AND (8) THE LEDGERS
def compose_ledgers(date, base):
    X = texts(ferry())
    n1, items, n2, second = author_words()
    a1 = X['A1'][2].replace('<DATE>', date)
    a2 = X['A2'][2].replace('<DATE>', date)
    a3, b1, b2 = X['A3'][2], X['B1'][2], X['B2'][2]
    n_reg = len(base[REG].split(NL)) - 1
    n_can = len(base[CANON].split(NL)) - 1
    n_ot = len(base[OT].split(NL)) - 1
    reg_head = n_reg + 2
    marker = '<!-- b761 (R371)(7) WHAT A KEYSTONE CARRIES, %s -->' % date
    foot = ('*Beside XXIII (C), added %s by b761 under the author’s word of 2026-11-18, its item (4): “%s” Its item (3): “%s” The author’s second '
            'word of the day: “%s” (relay `data/b761_author_words_preseal.txt` :%d, :%d). The line is strikeable; it stands beyond the section '
            '`(R371)`(12) excepts, on the author’s later word. No byte above it changes.*' % (date, items['4'], items['3'], second, n1, n2))
    canon = marker + NL + NL + a2 + NL + NL + foot
    head1 = ('**Dated head, %s, b761, `(R371)`(7) and (8): the lines the ruling orders for OPEN_TRAILS** (relay data/b761_ferry.txt :21, :23), '
             'appended at the end of the file after b760’s trail (its last line :%d) and before this act’s own trail, so that no line of the trail '
             'moves: the line naming the block of the phases by subject entered in REGISTRY; the order of the re-cuts; the two orders b760 '
             'discharged, in the roster’s form.' % (date, n_ot))
    a1_line = ('The author’s ruling of 2026-11-18 on the phases stands as one dated block at REGISTRY’s end, **THE PHASES BY SUBJECT** (REGISTRY '
               ':%d), under `(R371)`(7); no row is moved by it, and each row’s placement is put to the author after the cells of `(R371)`(9) are '
               'read. The author’s words stand verbatim in relay `data/b761_author_rulings.txt`.' % reg_head)
    head2 = ('**Dated head, %s, b761: the author’s words of 2026-11-18 given during the act** (relay data/b761_author_words_preseal.txt :%d, :%d), '
             'appended after the lines above and before this act’s own trail under their item (4): “%s” Each item stands beside its number, '
             'quoted whole; these lines enter, close and retire no order, and the sitting of `(R371)`(5) at this act applies item (3) and the '
             'second word.' % (date, n1, n2, items['4']))
    i1 = '(1), on `W-ORD-LI-ARITH` (its first line :17714): “%s”' % items['1']
    i2 = '(2): “%s”' % items['2']
    i3 = '(3): “%s”' % items['3']
    i4 = 'The second word, given after the first: “%s”' % second
    paras = [head1, a1_line, a3, b1, b2, head2, i1, i2, i3, i4]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    T_ = {REG: a1, CANON: canon, OT: ot}
    new = {REG: base[REG] + NL + a1 + NL, CANON: base[CANON] + NL + NL + canon + NL, OT: base[OT] + NL + ot + NL}
    return dict(X=X, texts=T_, new=new, entered=dict(A1=a1, A2=a2, A3=a3, B1=b1, B2=b2), reg_head=reg_head, canon_head=n_can + 5,
                ot_first=n_ot + 2, words=(n1, n2), foot=foot)


def qhead_at(text):
    return [k + 1 for k, l in enumerate(text.split(NL)) if sha(l)[:16] == QHEAD]


def ledgers(mode):
    from standing import orders as O
    date = today()
    base = dict((p, at_head(p)) for p in FILES)
    C = compose_ledgers(date, base)
    X, new, E_ = C['X'], C['new'], C['entered']
    I = ids()
    bad = []
    # ### each entered text equal to the ferry's with its fields filled, whole lines in its file's appended text
    filled = dict(A1=X['A1'][2].replace('<DATE>', date), A2=X['A2'][2].replace('<DATE>', date), A3=X['A3'][2], B1=X['B1'][2], B2=X['B2'][2])
    where = dict(A1=REG, A2=CANON, A3=OT, B1=OT, B2=OT)
    eq = dict((k, E_[k] == filled[k] and ('<' not in E_[k].replace('<!--', '') or k == 'A2') and (NL + E_[k] + NL) in (NL + C['texts'][where[k]] + NL)) for k in filled)
    left = [k for k, v in C['texts'].items() if '<DATE>' in v]
    otl = base[OT].split(NL)
    bl = [(k, n, otl[ln - 1].startswith('`%s`' % n)) for k, n, ln in B_LINES]
    before = dict(O.read(base[OT].split(NL)))
    after = dict(O.read(new[OT].split(NL)))
    moved = sorted(n for n in after if n in before and before[n]['status'] != after[n]['status'])
    added_names = sorted(n for n in after if n not in before)
    closing = dict((n, (before.get(n, {}).get('status'), after.get(n, {}).get('status'), after.get(n, {}).get('decided_at'))) for n in CLOSING)
    li = (before.get('W-ORD-LI-ARITH', {}).get('status'), after.get('W-ORD-LI-ARITH', {}).get('status'))
    ticks = [(p, k + 1) for p, t in C['texts'].items() for k, l in enumerate(t.split(NL)) if l.count('`') % 2]
    qb, qa = qhead_at(base[REG]), qhead_at(new[REG])
    rb = open(RBANK, encoding='utf-8').read() if os.path.isfile(RBANK) else ''
    rb_ok = bool(rb) and all(X[k][2] in rb for k in ('W1', 'W2', 'W3', 'A1', 'A2'))
    rows = []
    for p in FILES:
        b, n_ = base[p], new[p]
        nl_, k_ = n_.split(NL), len(b.split(NL)) - 1
        while k_ < len(nl_) and nl_[k_] == '':   # ### the first appended line that is not blank
            k_ += 1
        rows.append(dict(path=p, lines_before=len(b.split(NL)) - 1, lines_after=len(n_.split(NL)) - 1, first_new=k_ + 1,
                         sha_before=sha(b)[:16], sha_after=sha(n_)[:16], text_sha=sha(C['texts'][p])[:16], prefix=n_.startswith(b),
                         ids_equal=idcount(b, I) == idcount(n_, I), ids_added=sum(idcount(C['texts'][p], I).values())))
    ctl = [('each file`s bytes at HEAD a prefix of its new bytes: no line moves', all(r['prefix'] for r in rows)),
           ('[A1] to [A3], [B1] and [B2] as entered equal the ruling`s texts with their fields filled, each whole in its file`s text %s' % eq, all(eq.values()) and not left),
           ('[B1]`s and [B2]`s cited lines name their orders at HEAD %s' % bl, all(x[2] for x in bl)),
           ('the roster`s rule over the new OPEN_TRAILS in memory: the two orders %s' % closing, all(closing[n][1] == 'CLOSED' for n in CLOSING)),
           ('no other order`s status moves (moved %s) and no order enters (%s)' % ([m for m in moved if m not in CLOSING], added_names),
            not [m for m in moved if m not in CLOSING] and not added_names),
           ('W-ORD-LI-ARITH before and after %s' % (li,), li[0] == 'OPEN' and li[1] == 'OPEN'),
           ('each appended line`s backticks even (odd %s)' % ticks, not ticks),
           ('rule [Q] (3)`s heading by its digest at one line, :%d, the same before and after (%s -> %s); no line above it changing' % (QLINE, qb, qa),
            qb == [QLINE] and qa == [QLINE] and base[REG].split(NL)[:QLINE] == new[REG].split(NL)[:QLINE]),
           ('the identifiers` counts equal before and after in each file, and 0 in the appended texts', all(r['ids_equal'] for r in rows) and not any(r['ids_added'] for r in rows)),
           ('the author-rulings bank written, its five texts whole (sha256 %s)' % (sha(rb)[:16] if rb else 'ABSENT'), rb_ok)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R371)(7) AND (8), WITH THE AUTHOR`S WORDS OF THE ACT: REGISTRY, THE METHOD CANON AND OPEN_TRAILS, EACH APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b761_rulings.py ledgers; PLACE-papers HEAD %s; the texts from the ferry bank (data/b761_ferry.txt :%d-:%d), the author`s words bank' % (
             git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), WANT['A1'][0], WANT['B2'][1]),
         '### (data/b761_author_words_preseal.txt :%d, :%d) and the seat`s lines; <DATE> %s; each by line and sha256 here.' % (C['words'][0], C['words'][1], date), '',
         '## THE CONTROLS']
    P += ['  %-120s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE FILES: path | lines before -> after | the appended text from | its sha256 | the file`s sha256 before -> after']
    P += ['  %s | %d -> %d | :%d | %s | %s -> %s' % (r['path'], r['lines_before'], r['lines_after'], r['first_new'], r['text_sha'], r['sha_before'], r['sha_after']) for r in rows]
    P += ['', '## THE HEADS: REGISTRY`s block at :%d ; the canon`s section XXIV at :%d ; OPEN_TRAILS` first appended line :%d' % (C['reg_head'], C['canon_head'], C['ot_first']),
          '## THE ROSTER: %s ; W-ORD-LI-ARITH %s -> %s' % (' ; '.join('%s %s -> %s (deciding line :%s)' % (n, a, b, d) for n, (a, b, d) in closing.items()), li[0], li[1])]
    P += ['', '### ### **THE LEDGERS: FILES 3 OF 3 APPENDED, NO LINE MOVING ; [A1] TO [A3], [B1] AND [B2] ENTERED AS THE RULING`S ; THE TWO ORDERS %s ; '
              'CONTROLS %d OF %d AS WANTED ; %s.**' % ('CLOSED' if all(closing[n][1] == 'CLOSED' for n in CLOSING) else 'NOT BOTH CLOSED',
                                                   sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        for p in FILES:
            print(NL + '### THE TEXT APPENDED TO %s (the dry run`s print alone):' % p)
            print(C['texts'][p])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if any(idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    for p in FILES:
        with open(os.path.join(PP, *p.split('/')), 'wb') as f:
            f.write(new[p].encode('utf-8'))
    if any(fsha(os.path.join(PP, *p.split('/'))) != sha(new[p])[:16] for p in FILES):
        die('A WRITTEN FILE IS NOT ITS COMPOSITION')
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, date=date, files=rows, heads=dict(registry=C['reg_head'], canon=C['canon_head'], open_trails=C['ot_first']),
                               roster=dict((n, list(v)) for n, v in closing.items()), li_arith=list(li), words_lines=list(C['words']),
                               entered=dict((k, sha(v)[:16]) for k, v in E_.items()), foot_sha256=sha(C['foot'])[:16],
                               controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written REGISTRY.md, %s and OPEN_TRAILS.md; data/b761_ledgers.txt and .json' % CANON)


def main(argv):
    what, mode = (argv + ['', ''])[:2]
    if mode not in ('dry', 'write'):
        sys.exit(__doc__)
    if what == 'bank':
        bank(mode)
    elif what == 'ledgers':
        ledgers(mode)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
