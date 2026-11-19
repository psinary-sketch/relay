# -*- coding: utf-8 -*-
"""tools/b763_rulings.py -- b763, (R373)(9), with the lines (6), (7) and (8) enter and the author's word of 2026-11-19 on
W-ORD-STATEMENT-FILE given during the act (b763 events (48)): THE AUTHOR'S WORDS BANKED AND ENTERED; THE CANON'S SECTION XXV; THE ROSTER.

Written by the Write tool at b763's Component 2, while dispatch 2 ran, and committed before it runs (N2). Its forms are tools/b761_rulings.py's
(the canon and OPEN_TRAILS appended together, each file's bytes at HEAD a prefix of its new bytes) and tools/b762_rulings.py's (the
roster by tools/standing/orders.py's rule in memory, printed with its wanted figures).

  bank dry|write      (9): data/b763_author_rulings.txt -- [W1] read from the ferry bank by its marker lines (data/b763_ferry.txt :38),
                      verbatim, beside the navigator's rendering of the author's words on the orders, [A1] to [A12] (:60-:104), each
                      verbatim, for the author's strike.
  ledgers dry|write   appended at each file's end, no line moving, <DATE> the UTC date of the write:
                      phase1.5/method/THE_METHOD_CANON.md, [C1] with <DATE> filled, in the form XXII to XXIV were appended (two blank
                      lines, then [C1] whole, whose first line is its marker);
                      OPEN_TRAILS.md, one dated head for (R373) and under it the line naming the bank of [W1], [A1] to [A12], [B1] and
                      [B2]; then the lines the builds enter, each from data/b763_xlines.json: a ferry text ([X1], [X2] or [X3]) with its
                      fields filled from a run, or the line of the author's word on W-ORD-STATEMENT-FILE (SF_BUILT or SF_NOT, the seat's
                      composition from that word, citing it), each a paragraph of its own.
                      Controls before the write: each entered text equal to the ferry's with its fields filled and whole in its file's
                      appended text; no field left; each appended line's backticks even; the identifiers 0 in the texts and their counts
                      equal before and after; the author-rulings bank written, its thirteen texts whole; each run id of a build line in
                      data/b763_dispatch_rows.json. THE ROSTER ((9)), printed and no condition, a status otherwise printed with its line
                      and lettered for the navigator: by tools/standing/orders.py's rule in memory over OPEN_TRAILS with the lines up to
                      [B2] and before the build lines, W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE CLOSED, W-ORD-PREMISE-POSITIONS entering
                      OPEN, no other status moving, 83 open; then over the whole new file, printed beside. Bank: data/b763_ledgers.txt and
                      .json, each appended text by line and sha256, its words printed by the dry run alone.

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

ACT, NL = 'b763', '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
FERRY = os.path.join(D, 'b763_ferry.txt')
FERRY_SHA = 'ae0a4b1b142de092'   # ### data/b763_stepzero.txt :18: the ferry bank's sha256
WORDS = os.path.join(D, 'b763_author_words_preseal.txt')
SF_MARK = "THE AUTHOR'S WORD TO b763 ON W-ORD-STATEMENT-FILE, 2026-11-19"
OT, CANON = 'OPEN_TRAILS.md', 'phase1.5/method/THE_METHOD_CANON.md'
FILES = (CANON, OT)
A_KEYS = ['A%d' % i for i in range(1, 13)]
WANT = dict(W1=(38, 38), C1=(42, 52), I1=(56, 56), B1=(108, 108), B2=(112, 112), X1=(116, 116), X2=(120, 120), X3=(124, 124))
WANT.update(dict(('A%d' % i, (60 + 4 * (i - 1), 60 + 4 * (i - 1))) for i in range(1, 13)))
CLOSING = ('W-ORD-GW-IMPORT', 'W-ORD-TABLE-SHAPE')
ENTERING = 'W-ORD-PREMISE-POSITIONS'
OPEN_WANT = 83
NAME = re.compile(r'`(W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*)`')
FIELD = re.compile(r'<[a-z][a-z0-9 ]*(?: or [A-Z0-9 ]+)?>|<DATE>|<6 or 8>|<A or B>|<the order\'s name>|<what compiled, by name>')
XJSON = os.path.join(D, 'b763_xlines.json')
DROWS = os.path.join(D, 'b763_dispatch_rows.json')
RBANK = os.path.join(D, 'b763_author_rulings.txt')
LBANK = os.path.join(D, 'b763_ledgers.txt')
LJSON = os.path.join(D, 'b763_ledgers.json')

# ### the line of the author's word on W-ORD-STATEMENT-FILE: the seat's composition from that word (b763 events (48)), its two outcomes
SF_BUILT = ('`W-ORD-STATEMENT-FILE` CARRIED under the author’s word of 2026-11-19 (relay `data/b763_author_words_preseal.txt` :<line>), which '
            'amends `(R372)`(8) and `(R373)`(6) in this one matter: its nineteen rows of SIDE-explicit-formula closed by '
            'SIDEExplicitFormula/OnePageStatement.lean at its commit (SIDE-explicit-formula <tag> = <peel>, run <run id>, <axioms>); its object from '
            'here the same file for the three rows in SIDE-kernel, its trigger the next runner build of SIDE-kernel.')
SF_NOT = ('`W-ORD-STATEMENT-FILE` CARRIED whole under the author’s word of 2026-11-19 (relay `data/b763_author_words_preseal.txt` :<line>), which '
          'amends `(R372)`(8) and `(R373)`(6) in this one matter: the file SIDEExplicitFormula/OnePageStatement.lean did not build inside the act’s '
          'ceiling (<reading>); its trigger unchanged, the next runner build of SIDE-explicit-formula.')
SF = dict(SF_BUILT=SF_BUILT, SF_NOT=SF_NOT)


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
    import b763_address_scan as SC
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


def sf_line():
    """the line of data/b763_author_words_preseal.txt on which the author's word on W-ORD-STATEMENT-FILE opens (its title line)."""
    with open(WORDS, encoding='utf-8') as f:
        L = f.read().replace('\r', '').split(NL)
    hit = [i + 1 for i, l in enumerate(L) if l.startswith(SF_MARK)]
    if len(hit) != 1:
        die('THE AUTHOR`S WORD ON W-ORD-STATEMENT-FILE NOT READ ONCE IN ITS BANK (%d)' % len(hit))
    return hit[0]


# ================================================================================ (9) THE AUTHOR'S RULINGS BANK
def compose_bank(X):
    L = ['%s -- (R373)(9): THE AUTHOR`S WORD OF 2026-11-19 ON THE FORM OF A STATEMENT, BESIDE THE NAVIGATOR`S RENDERING OF THE AUTHOR`S WORDS ON '
         'THE ORDERS, FOR THE AUTHOR`S STRIKE (%s)' % (ACT, utc()), '',
         '### tools/b763_rulings.py bank: read from the ferry bank data/b763_ferry.txt (sha256 %s...) by its marker lines, verbatim, nothing changed;' % FERRY_SHA,
         '### the renderings are the navigator`s, put to the author on 2026-11-19 and struck by none, carried by (R373)(9) as the author`s words.', '',
         '## [W1] THE AUTHOR`S WORD, 2026-11-19, VERBATIM (data/b763_ferry.txt :%d)' % X['W1'][0], X['W1'][2], '',
         '## THE NAVIGATOR`S RENDERING OF THE AUTHOR`S WORDS ON THE ORDERS, [A1] TO [A12] (data/b763_ferry.txt :%d-:%d), EACH VERBATIM' % (
             X['A1'][0], X['A12'][1])]
    for k in A_KEYS:
        L += ['  [%s] (:%d)' % (k, X[k][0]), X[k][2]]
    L += ['', '### ### **THE AUTHOR`S RULINGS: WORDS 1, VERBATIM FROM THE FERRY ; RENDERINGS 12, THE NAVIGATOR`S, EACH VERBATIM ; NOTHING CHANGED.**']
    return NL.join(L) + NL


def bank(mode):
    X = texts(ferry())
    text = compose_bank(X)
    I = ids()
    n_id = sum(idcount(text, I).values())
    whole = all((NL + X[k][2] + NL) in text for k in ['W1'] + A_KEYS)
    ok = n_id == 0 and whole
    print(text if mode == 'dry' else text.split(NL)[0])
    print('### the identifiers in the bank %d ; the thirteen texts carried whole %s ; %s' % (
        n_id, whole, 'DRY, NOTHING WRITTEN' if mode == 'dry' else ('WRITTEN' if ok else 'HELD')))
    if mode == 'dry':
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(RBANK):
        die('THE BANK STANDS ALREADY')
    put(RBANK, text)
    print('written data/b763_author_rulings.txt (%d lines, sha256 %s)' % (len(text.split(NL)) - 1, sha(text)[:16]))


# ================================================================================ THE BUILD LINES
def xlines(X, sfl):
    """the build lines from data/b763_xlines.json: [{key: X1|X2|X3|SF_BUILT|SF_NOT, fields: [[placeholder, value], ...], runs: [run id, ...]}],
    each template's placeholders replaced in order, once each; returns [(key, text, fields, runs)]."""
    if not os.path.isfile(XJSON):
        die('data/b763_xlines.json ABSENT: THE BUILD LINES NOT COMPOSED')
    J = json.load(open(XJSON, encoding='utf-8'))
    out = []
    for r in J['lines']:
        k = r['key']
        tpl = X[k][2] if k in ('X1', 'X2', 'X3') else SF.get(k)
        if tpl is None:
            die('A BUILD LINE OF NO KNOWN KEY: %r' % k)
        if k in SF:
            tpl = tpl.replace('<line>', str(sfl), 1)
        t = tpl
        for ph, val in r['fields']:
            if ph not in t:
                die('%s: THE FIELD %r NOT IN ITS TEMPLATE' % (k, ph))
            t = t.replace(ph, val, 1)
        out.append((k, t, r['fields'], r.get('runs', [])))
    return out


# ================================================================================ (9) THE LEDGERS
def compose_ledgers(date, base):
    X = texts(ferry())
    sfl = sf_line()
    c1 = X['C1'][2].replace('<DATE>', date)
    n_can = len(base[CANON].split(NL)) - 1
    n_ot = len(base[OT].split(NL)) - 1
    head = ('**Dated head, %s, b763, `(R373)`(9), with the lines of (6), (7) and (8): the lines the ruling orders for OPEN_TRAILS** (relay '
            'data/b763_ferry.txt :25, and :19, :21 and :23 for the lines of the builds), appended at the end of the file after b762’s trail (its '
            'last line :%d) and before this act’s own trail, so that no line of the trail moves: the line naming the bank of the author’s word on '
            'the form of a statement; the author’s words on the orders that waited on them, as the navigator rendered them and the author struck '
            'none; the order of the form’s finite and signed parts widened, and the reading of the named premises entered; then the lines the '
            'builds enter, the last from the author’s word of 2026-11-19 on the statement file.' % (date, n_ot))
    wline = ('The author’s word of 2026-11-19 on the form of a statement, “%s”, stands verbatim in relay `data/b763_author_rulings.txt` beside the '
             'navigator’s rendering of the author’s words on the orders, the lines below, for the author’s strike (`(R373)`(9)).' % X['W1'][2])
    xl = xlines(X, sfl)
    pre = [head, wline] + [X[k][2] for k in A_KEYS] + [X['B1'][2], X['B2'][2]]
    paras = pre + [t for _k, t, _f, _r in xl]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    ot_pre = NL.join(sum(([p, ''] for p in pre), []))[:-1]
    T_ = {CANON: c1, OT: ot}
    new = {CANON: base[CANON] + NL + NL + c1 + NL, OT: base[OT] + NL + ot + NL}
    entered = dict((k, X[k][2]) for k in A_KEYS + ['B1', 'B2'])
    entered['C1'] = c1
    return dict(X=X, texts=T_, new=new, new_pre=base[OT] + NL + ot_pre + NL, entered=entered, xl=xl, head=head, wline=wline,
                canon_head=n_can + 5, ot_first=n_ot + 2, sfl=sfl)


def ledgers(mode):
    from standing import orders as O
    date = today()
    base = dict((p, at_head(p)) for p in FILES)
    C = compose_ledgers(date, base)
    X, new, E_ = C['X'], C['new'], C['entered']
    I = ids()
    filled = dict((k, X[k][2]) for k in A_KEYS + ['B1', 'B2'])
    filled['C1'] = X['C1'][2].replace('<DATE>', date)
    where = dict((k, OT) for k in A_KEYS + ['B1', 'B2'])
    where['C1'] = CANON
    eq = dict((k, E_[k] == filled[k] and (NL + E_[k] + NL) in (NL + C['texts'][where[k]] + NL)) for k in filled)
    left = sorted(set(m for t in list(C['texts'].values()) for m in FIELD.findall(t)))
    ticks = [(p, k + 1) for p, t in C['texts'].items() for k, l in enumerate(t.split(NL)) if l.count('`') % 2]
    rb = open(RBANK, encoding='utf-8').read() if os.path.isfile(RBANK) else ''
    rb_ok = bool(rb) and all((NL + X[k][2] + NL) in rb for k in ['W1'] + A_KEYS)
    rows_d = json.load(open(DROWS, encoding='utf-8')) if os.path.isfile(DROWS) else []
    rows_d = rows_d.get('rows', rows_d) if isinstance(rows_d, dict) else rows_d
    runs_known = set(str(r.get('run')) for r in rows_d if isinstance(r, dict) and r.get('run'))
    runs_cited = [str(x) for _k, _t, _f, rr in C['xl'] for x in rr]
    runs_ok = all(x in runs_known for x in runs_cited)
    # ### the roster, in memory: before; with the lines up to [B2] (wanted); with the whole appended text (printed beside)
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before = dict(O.read(base[OT].split(NL)))
    mid = dict(O.read(C['new_pre'].split(NL)))
    after = dict(O.read(new[OT].split(NL)))
    moved = sorted(n for n in mid if n in before and st(before, n) != st(mid, n))
    added = sorted(n for n in mid if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_m = sum(1 for n in mid if st(mid, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    moved_a = sorted(n for n in after if n in mid and st(mid, n) != st(after, n))
    R = [('%s and %s CLOSED' % CLOSING, [(n, st(before, n), st(mid, n), (mid.get(n) or {}).get('decided_at')) for n in CLOSING],
          all(st(mid, n) == 'CLOSED' for n in CLOSING)),
         ('%s enters OPEN' % ENTERING, (ENTERING in added, st(mid, ENTERING), (mid.get(ENTERING) or {}).get('entry')), added == [ENTERING] and st(mid, ENTERING) == 'OPEN'),
         ('no other order`s status moves', [m for m in moved if m not in CLOSING] or 'none', not [m for m in moved if m not in CLOSING]),
         ('the roster open, before -> with the lines up to [B2], wanted %d' % OPEN_WANT, '%d -> %d (orders %d -> %d)' % (open_b, open_m, len(before), len(mid)),
          open_m == OPEN_WANT)]
    rows = []
    for p in FILES:
        b, n_ = base[p], new[p]
        nl_, k_ = n_.split(NL), len(b.split(NL)) - 1
        while k_ < len(nl_) and nl_[k_] == '':
            k_ += 1
        rows.append(dict(path=p, lines_before=len(b.split(NL)) - 1, lines_after=len(n_.split(NL)) - 1, first_new=k_ + 1,
                         sha_before=sha(b)[:16], sha_after=sha(n_)[:16], text_sha=sha(C['texts'][p])[:16], prefix=n_.startswith(b),
                         ids_equal=idcount(b, I) == idcount(n_, I), ids_added=sum(idcount(C['texts'][p], I).values())))
    ctl = [('each file`s bytes at HEAD a prefix of its new bytes: no line moves', all(r['prefix'] for r in rows)),
           ('[C1], [A1] to [A12], [B1] and [B2] as entered equal the ruling`s texts with their fields filled, each whole in its file`s text',
            all(eq.values())),
           ('no field left in the appended texts (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts equal before and after in each file, and 0 in the appended texts',
            all(r['ids_equal'] for r in rows) and not any(r['ids_added'] for r in rows)),
           ('the author-rulings bank written, its thirteen texts whole (sha256 %s)' % (sha(rb)[:16] if rb else 'ABSENT'), rb_ok),
           ('each run id a build line cites in data/b763_dispatch_rows.json (%s)' % (runs_cited or 'none cited'), runs_ok)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R373)(9), WITH THE LINES OF (6), (7) AND (8) AND THE AUTHOR`S WORD ON W-ORD-STATEMENT-FILE: THE METHOD CANON AND OPEN_TRAILS, EACH '
         'APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b763_rulings.py ledgers; PLACE-papers HEAD %s; the texts from the ferry bank (data/b763_ferry.txt :%d-:%d), the build lines from' % (
             git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), WANT['C1'][0], WANT['X3'][1]),
         '### data/b763_xlines.json (sha256 %s), the author`s word on the statement file at data/b763_author_words_preseal.txt :%d, and the seat`s two' % (
             fsha(XJSON), C['sfl']),
         '### lines (the dated head and the line naming the bank of [W1]); <DATE> %s; each by line and sha256 here.' % date, '',
         '## THE CONTROLS']
    P += ['  %-130s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY, WITH THE LINES UP TO [B2] ((9): printed; a status otherwise is lettered '
              'for the navigator, not held)']
    P += ['  %s: %s -> %s' % (w, g, 'AS WANTED' if o else 'OTHERWISE') for w, g, o in R]
    P += ['  BESIDE, WITH THE BUILD LINES: open %d ; statuses moving after [B2] %s' % (
        open_a, [(n, st(mid, n), st(after, n), (after.get(n) or {}).get('decided_at')) for n in moved_a] or 'none')]
    P += ['', '## THE FILES: path | lines before -> after | the appended text from | its sha256 | the file`s sha256 before -> after']
    P += ['  %s | %d -> %d | :%d | %s | %s -> %s' % (r['path'], r['lines_before'], r['lines_after'], r['first_new'], r['text_sha'], r['sha_before'],
                                                     r['sha_after']) for r in rows]
    nl_ot = new[OT].split(NL)
    P += ['', '## THE HEADS: the canon`s section XXV at :%d ; OPEN_TRAILS` first appended line :%d' % (C['canon_head'], C['ot_first']),
          '## THE PARAGRAPHS BY LINE: ' + ' ; '.join('%s :%d' % (k, nl_ot.index(v) + 1) for k, v in
                                                     [('head', C['head']), ('W1 line', C['wline'])] + [(k, E_[k]) for k in A_KEYS + ['B1', 'B2']] +
                                                     [(k, t) for k, t, _f, _r in C['xl']])]
    P += ['', '### ### **THE LEDGERS: FILES 2 OF 2 APPENDED, NO LINE MOVING ; [C1] AS SECTION XXV ; [A1] TO [A12], [B1], [B2] AND %d BUILD LINES ; '
              'THE ROSTER %d OPEN WITH THE LINES UP TO [B2], WANTED %d, %d OF %d AS WANTED ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
                  len(C['xl']), open_m, OPEN_WANT, sum(1 for r in R if r[2]), len(R), sum(1 for _w, o in ctl if o), len(ctl),
                  ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        for p in FILES:
            print(NL + '### THE TEXT APPENDED TO %s (the dry run`s print alone):' % p)
            print(C['texts'][p])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(LBANK):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    for p in FILES:
        with open(os.path.join(PP, *p.split('/')), 'wb') as f:
            f.write(new[p].encode('utf-8'))
    if any(fsha(os.path.join(PP, *p.split('/'))) != sha(new[p])[:16] for p in FILES):
        die('A WRITTEN FILE IS NOT ITS COMPOSITION')
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, date=date, files=rows, heads=dict(canon=C['canon_head'], open_trails=C['ot_first']),
                               roster=dict(before_open=open_b, mid_open=open_m, after_open=open_a, want=OPEN_WANT, rows=[[w, str(g), o] for w, g, o in R],
                                           moved_after_b2=moved_a),
                               entered=dict((k, sha(v)[:16]) for k, v in E_.items()), build_lines=[[k, sha(t)[:16], f, r] for k, t, f, r in C['xl']],
                               head_sha=sha(C['head'])[:16], wline_sha=sha(C['wline'])[:16], xlines_sha=fsha(XJSON),
                               controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written %s and OPEN_TRAILS.md ; data/b763_ledgers.txt and .json' % CANON)


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
