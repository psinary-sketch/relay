# -*- coding: utf-8 -*-
"""tools/b760_ledgers.py -- b760, (R370)(9), (10) and (11): THE EPSTEIN DOCUMENT'S FIVE KEYS, AND THE LEDGERS' APPENDED TEXTS.

Written by the Write tool at b760's Component 5 and committed before it runs (N2).

  epstein dry|write   (9): BLOCK X's five keys (data/b760_text.txt :216-:246) applied to phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, each
                      OLD read to stand once at its line before anything is written, the file's bytes at HEAD equal to its bytes at d711a5d6
                      and to the working file; ‹DATE› the UTC date of the write. Controls printed before the write: the composition differs
                      from those bytes by the five keys alone (four lines replaced, two inserted after :452); v0.1, v2.3.1, v2.4.0 and
                      v2.5.0 unchanged; the identifiers' counts equal and 0 in the added texts. Bank: data/b760_epstein_keys.txt.
  ledgers dry|write   (10) and (11): appended at each file's end, no line moving, each file's bytes at HEAD a prefix of its new bytes --
                      ERRATA.md, BLOCK E's two entries in their order, ‹DATE› and ‹DISCHARGE› filled (the discharge's text where (6) stands,
                      data/b760_discharge.json), their IDs not held; OPEN_TRAILS.md, one dated head and its paragraphs: b759's root answer
                      with the author's correction of 05:17:50Z (data/b759_author_answers.txt :12, quoted whole from the bank), (6)'s
                      discharge in the plan's words with the pins, W-ORD-WSC-KERNEL-CITES discharged by (7), W-ORD-KEYSTONE-HEADS answered
                      for this document, W-ORD-WSC-TITCHMARSH entered in the ruling's words (data/b760_ferry.txt :27), and one order
                      W-ORD-RECUT-QUOTE-<key> for each key of the two searches' orders (data/b760_cut.json, data/b760_late_quotes.json);
                      REGISTRY.md, one dated note naming v2.5.0 beside row d1-3 (:85), which is not edited, rule [Q] (3)'s heading read
                      by its digest at the same line before and after; THE_KEYSTONE_CENSUS_v0_8_3.md, one dated note made of v2.5.0's
                      own version line (:5) and (7)'s sentence with its fields filled. Bank: data/b760_ledgers.txt and .json, each
                      appended text by line and sha256, its words printed by the dry run alone.

No PLACE-papers line is printed but the texts this tool composes; v2.5.0's identifier lines are never read by number; no git write.
"""
import difflib
import json
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import b760_edition as E   # noqa: E402

ACT, NL, PP, D = 'b760', '\n', E.PP, E.D
EPS = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'
EPS1 = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
EPS_BASE = 'd711a5d6'   # ### (N3): "the Epstein document differs from its bytes at d711a5d6 by BLOCK X's five keys alone"
ERRATA, OT, REG = 'ERRATA.md', 'OPEN_TRAILS.md', 'REGISTRY.md'
CEN = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'
UNEDITED = (E.V231, E.V24, E.V25, EPS1)
QHEAD = '53d53060a58f6b9b'   # ### (R370)(5)(i): rule [Q] (3)'s heading, by the sha256 of its line
EBANK = os.path.join(D, 'b760_epstein_keys.txt')
LBANK = os.path.join(D, 'b760_ledgers.txt')
LJSON = os.path.join(D, 'b760_ledgers.json')
HX = re.compile(r'^(X\d) \| :(\d+) \| ([A-Z-]+)$')
VACUITY = 'held, H28a vacuous (no work list carries this document)'   # ### (7)'s "<as scored>": data/b760_edition_diff.txt, H28a's MOVED-IN-MEANING rows 0
# ### the seat's reading of each order's lines, from the hand reads (data/b760_quote.json readings; data/b760_late_quotes.json readings)
ORDER_READ = {
    'W4': 'each states the theorem with the two words W4’s STATUS names, the claim W4 corrects',
    'W8': 'each is its file’s own row or dated note carrying the discharge sentence of `W-ORD-ZQ-OFFLINE-ZERO` that v2.4.0 :95 carried; the claim stands, W8 restating it at v0.41',
    'W9': 'the file’s own dated note of b750, closing with the sentence v2.4.0 :97 closed with; the claim stands, W9 removing a note whose content the subsection states',
    'C4': 'each says of the Epstein family as a whole that its zeros wander off the critical line, the claim C4 sharpened to class number above 1',
}


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(x):
    return E.sha(x)


def at_head(path):
    b = E.git(PP, 'show', 'HEAD:' + path, raw=True)
    with open(os.path.join(PP, *path.split('/')), 'rb') as f:
        w = f.read()
    if not b or b != w:
        die('%s: ITS WORKING FILE IS NOT ITS BYTES AT HEAD (%d, %d bytes)' % (path, len(b), len(w)))
    if b'\r' in b or not b.endswith(b'\n'):
        die('%s: CARRIAGE RETURNS OR NO FINAL LINE END' % path)
    return b.decode('utf-8')


def blocks(t):
    """every keyed piece of BLOCKS X, P, E and F: head -> its OLD (one line) and its NEW (the lines between NEW>> and <<NEW), each with its line."""
    out, i = {}, 0
    while i < len(t):
        l = t[i]
        if l.startswith('@@ ') and not l.startswith('@@ BLOCK'):
            head = l[3:].strip()
            k, old, oat = i + 1, None, None
            if k < len(t) and t[k].startswith('OLD: '):
                old, oat, k = t[k][5:], k + 1, k + 1
            if k < len(t) and t[k] == 'NEW>>':
                j = t.index('<<NEW', k)
                out[head] = dict(old=old, old_at=oat, new=NL.join(t[k + 1:j]), new_at=(k + 2, j))
                i = j
        i += 1
    return out


def unedited():
    return dict((p, E.fsha(os.path.join(PP, *p.split('/')))) for p in UNEDITED)


def today():
    return time.strftime('%Y-%m-%d', time.gmtime())


# ================================================================================ (9) THE EPSTEIN DOCUMENT
def epstein(mode):
    t = E.text_bank()
    B = blocks(t)
    keys = sorted(((m.group(1), int(m.group(2)), m.group(3), b) for h, b in B.items() for m in [HX.match(h)] if m), key=lambda x: x[1])
    if [k[0] for k in sorted(keys)] != ['X1', 'X2', 'X3', 'X4', 'X5']:
        die('BLOCK X CARRIES %s, NOT X1 TO X5' % [k[0] for k in keys])
    date, before = today(), unedited()
    base = E.git(PP, 'show', '%s:%s' % (EPS_BASE, EPS), raw=True).decode('utf-8')
    head = at_head(EPS)
    if base != head:
        die('%s AT HEAD IS NOT ITS BYTES AT %s' % (EPS, EPS_BASE))
    L = head.split(NL)[:-1]
    new, rows, bad = list(L), [], []
    for key, n, kind, b in keys:
        old, nw = b['old'], b['new'].replace('‹DATE›', date)
        if '‹' in nw or NL in nw:
            bad.append((key, 'a field left or more than one line'))
            continue
        c_line, c_file = L[n - 1].count(old), head.count(old)
        if c_line != 1:
            bad.append((key, 'OLD stands %d times at :%d' % (c_line, n)))
            continue
        rows.append(dict(key=key, line=n, kind=kind, old_at=b['old_at'], new_at=b['new_at'][0], in_file=c_file, before=sha(L[n - 1])[:16],
                         old_sha=sha(old)[:16], new_sha=sha(nw)[:16], new=nw))
        if kind == 'PART':
            new[n - 1] = L[n - 1].replace(old, nw, 1)
        elif kind != 'PARA-AFTER':
            bad.append((key, 'kind %s' % kind))
    if bad:
        die('THE KEYS DO NOT HOLD %s' % bad)
    for r in rows:
        if r['kind'] == 'PARA-AFTER':
            n = r['line']
            if new[n] != '':
                die('%s: THE LINE AFTER :%d IS NOT A PARAGRAPH BREAK' % (r['key'], n))
            new[n:n] = ['', r['new']]   # ### a paragraph after :n, the break after it kept
    out = NL.join(new) + NL
    for r in rows:
        r['after'] = sha(new[r['line'] - 1])[:16]
    # ### THE CONTROLS
    ops = [o for o in difflib.SequenceMatcher(None, L, new, autojunk=False).get_opcodes() if o[0] != 'equal']
    rep = sorted(o[1] + 1 for o in ops if o[0] == 'replace' and o[2] - o[1] == 1 and o[4] - o[3] == 1)
    ins = [(o[1], o[4] - o[3]) for o in ops if o[0] == 'insert']
    pa = [r['line'] for r in rows if r['kind'] == 'PARA-AFTER']
    # ### the four PART lines replaced one for one, two lines inserted at X5's paragraph (difflib may align the break before or after it), nothing else
    diff_ok = (len(ops) == len(rep) + len(ins) and rep == sorted(r['line'] for r in rows if r['kind'] == 'PART')
               and len(ins) == len(pa) and all(i in (n, n + 1) and c == 2 for (i, c), n in zip(ins, pa)))
    I, _SC = E.ids()
    ib, ia, ix = E.idcount(head, I), E.idcount(out, I), E.idcount(NL.join(r['new'] for r in rows), I)
    after_u = unedited()
    ctl = [('the file at HEAD equal to its bytes at %s and to its working file' % EPS_BASE, True),
           ('the composition differs from them by the five keys alone (%d operations: replaced %s, inserted %s)' % (len(ops), rep, ins), diff_ok),
           ('its lines %d -> %d' % (len(L), len(new)), len(new) == len(L) + 2),
           ('the identifiers` counts equal before and after %s' % sorted(ib.items()), ib == ia),
           ('the identifiers in the five added texts 0', not any(ix.values())),
           ('v0.1, v2.3.1, v2.4.0 and v2.5.0 unchanged by the composition', before == after_u)]
    P = ['%s -- (R370)(9): THE EPSTEIN DOCUMENT`S THREE CITATIONS AND ONE LEGEND, CORRECTED IN PLACE BY BLOCK X (%s)' % (ACT, E.utc()), '',
         '### tools/b760_ledgers.py epstein; %s at PLACE-papers HEAD %s (blob sha256 %s), its bytes at %s; BLOCK X of data/b760_text.txt (sha256 %s...).' % (
             EPS, E.git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), sha(head)[:16], EPS_BASE, E.TEXT_SHA[:16]),
         '### Each key`s OLD read to stand once at its line; a line of the document by line and sha256 alone; v0.1 not touched; no quotation search ((9)).', '',
         '## THE CONTROLS']
    P += ['  %-90s %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in ctl]
    P += ['', '## THE KEYS: key | line | kind | OLD at the text block | NEW at the text block | OLD in the file | the line before -> after']
    P += ['  %s | :%d | %s | :%d (sha256 %s) | :%d (sha256 %s) | %d | %s -> %s' % (r['key'], r['line'], r['kind'], r['old_at'], r['old_sha'], r['new_at'],
                                                                              r['new_sha'], r['in_file'], r['before'], r['after']) for r in rows]
    P += ['  X5`s paragraph inserted after :%d, now at :%d, its break kept' % (rows[-1]['line'], rows[-1]['line'] + 2) if rows[-1]['kind'] == 'PARA-AFTER' else '']
    ok = all(o for _w, o in ctl)
    P += ['', '### ### **THE EPSTEIN DOCUMENT: KEYS 5 OF 5 HOLDING, %d APPLIED ; LINES %d -> %d ; CONTROLS %d OF %d AS WANTED ; %s ; v0.1 UNTOUCHED.**' % (
        len(rows) if ok else 0, len(L), len(new), sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE FIVE NEW TEXTS AS FILLED (the dry run`s print alone):')
        for r in rows:
            print('  %s :%d  %s' % (r['key'], r['line'], r['new']))
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if any(E.idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    with open(os.path.join(PP, *EPS.split('/')), 'wb') as f:
        f.write(out.encode('utf-8'))
    if E.fsha(os.path.join(PP, *EPS.split('/'))) != sha(out)[:16] or unedited() != before:
        die('THE WRITTEN FILE IS NOT THE COMPOSITION, OR A FILE BESIDE IT MOVED')
    E.put(EBANK, NL.join(P) + NL)
    print('written %s (%d lines, sha256 %s) and data/b760_epstein_keys.txt' % (EPS, len(new), sha(out)[:16]))


# ================================================================================ (10) AND (11) THE LEDGERS
def ferry_line(n):
    with open(os.path.join(D, 'b760_ferry.txt'), encoding='utf-8') as f:
        return f.read().split(NL)[n - 1]


def relay_line(path, n):
    with open(os.path.join(E.RELAY, *path.split('/')), encoding='utf-8') as f:
        return f.read().replace('\r', '').split(NL)[n - 1]


def sentence7(standing):
    l = ferry_line(21)
    m = re.search(r'THE SENTENCE IF ENTERED: "(.*?)" IF HELD', l)
    if not m:
        die('(7)`S SENTENCE NOT READ AT data/b760_ferry.txt :21')
    s = m.group(1)
    alt = re.search(r'<(its paragraph on the seven classes [^|>]*?) \| (that paragraph stands as v2\.4\.0 printed it)>', s)
    if not alt or '<as scored>' not in s:
        die('(7)`S SENTENCE CARRIES NOT ITS TWO FIELDS')
    s = s.replace(alt.group(0), alt.group(1) if standing else alt.group(2)).replace('<as scored>', VACUITY)
    if '<' in s or '>' in s:
        die('(7)`S SENTENCE LEFT A FIELD')
    return s


def titchmarsh():
    l = ferry_line(27)
    m = re.search(r'W-ORD-WSC-TITCHMARSH, (the sentence of Which Structure Confines .*?next edition\.)', l)
    if not m:
        die('W-ORD-WSC-TITCHMARSH`S WORDS NOT READ AT data/b760_ferry.txt :27')
    return m.group(1)


def paths_lines(v):
    return '; '.join('%s :%d' % (p, n) for p, n in sorted(tuple(x) for x in v))


def compose_ledgers(date):
    t = E.text_bank()
    B = blocks(t)
    with open(os.path.join(D, E.DISCHARGE), encoding='utf-8') as f:
        dj = json.load(f)
    standing = dj.get('standing') == 'STANDS' and dj.get('w14') == 'APPLY'
    ed = dj['errata_discharge']
    if ed['words'] != t[ed['line'] - 1] or ed['line'] != B['DISCHARGE WHERE (6) STANDS']['new_at'][0]:
        die('THE DISCHARGE`S ERRATA TEXT IS NOT BLOCK F`S AT ITS LINE')
    dis = ed['words'] if standing else B['DISCHARGE WHERE THE AUTHOR STRIKES (6)']['new']
    ot_words = dj['open_trails']['words']
    if sha(ot_words)[:16] != dj['open_trails']['words_sha256']:
        die('THE DISCHARGE SENTENCE IS NOT ITS BANKED DIGEST')
    pins = dict((p['name'], p['v0.41']) for p in dj['kernel']['pins'])
    word = relay_line('data/b759_author_answers.txt', 12)
    if not word.startswith('1 -- the keystone is Which Structure Confines'):
        die('THE AUTHOR`S WORD NOT READ AT data/b759_author_answers.txt :12')
    with open(E.CBANK, encoding='utf-8') as f:
        cut = json.load(f)
    with open(E.LJSON, encoding='utf-8') as f:
        late = json.load(f)
    wkeys = dict((k['key'], k) for k in E.block_w(t))
    orders = [(k, v, False) for k, v in sorted(cut['orders'].items())] + [(k, v, True) for k, v in sorted(late['orders'].items())]
    if any(k not in ORDER_READ for k, _v, _l in orders):
        die('AN ORDER`S KEY WITHOUT THE SEAT`S READING %s' % [k for k, _v, _l in orders if k not in ORDER_READ])
    late_src = dict((r['key'], (r['path'], r['line_no'])) for r in late['rows'])
    v25 = E.git(PP, 'show', 'HEAD:' + E.V25, raw=True).decode('utf-8').split(NL)
    vline = v25[4]
    if not (vline.startswith('*v2.5.0, %s (b760' % date) and vline.endswith('*')) or 'zq_coeff_not_multiplicative' not in v25[218] \
            or not v25[213].startswith('**The classical theorem this document rests on'):
        die('v2.5.0`S VERSION LINE (:5), ITS ROW AT :219 OR ITS HEAD SENTENCE AT :214 NOT AS THE ORDERS CITE THEM')
    s7 = sentence7(standing)
    # ### ERRATA
    e1 = B['ERRATA 1']['new'].replace('‹DATE›', date)
    e2 = B['ERRATA 2']['new'].replace('‹DATE›', date).replace('‹DISCHARGE›', dis)
    # ### OPEN_TRAILS
    n_q = ('none', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')[len(orders)] if len(orders) < 10 else str(len(orders))
    paras = [
        '**Dated head, %s, b760, `(R370)`(10): the lines the ruling orders for OPEN_TRAILS** (relay data/b760_ferry.txt :27), appended at the end of the file after b759’s trail (its last line :18689) and before this act’s own trail, so that no line of the trail moves: b759’s root answer with the author’s correction; `W-ORD-MECHANISM-ATTRIBUTION` discharged; `W-ORD-WSC-KERNEL-CITES` discharged; `W-ORD-KEYSTONE-HEADS` answered for this document; one order entered by name; %s orders entered from the quotation searches of `(R370)`(8).' % (date, n_q),
        '*Appended %s by b760 to b759’s trail (:18635), under `(R370)`(10):* b759’s one question at the root was answered by the author’s word (relay data/b759_author_answers.txt :9, :12, 2026-11-18T05:17:50Z), quoted whole: “%s” The correction stands as the author gave it: one order of b759 stands on Which Structure Confines, `W-ORD-WSC-KERNEL-CITES` (:18625), where the question counted three.' % (date, word),
        '`W-ORD-MECHANISM-ATTRIBUTION` (:17932): discharged at b760 by its second clause under `(R370)`(6), on the author’s pass of [P1] (relay data/b752_author_answers.txt :7) and the author’s word in `(R370)`, in the words the plan fixed (relay data/b752_attribution_plan.txt :90-:92): “%s” The pins as they stand: `zq_coeff_not_multiplicative` (%s) and `cQ_not_nonneg` (%s), on SIDE-explicit-formula’s main at v0.41 = %s. The read of `(R369)`(10) at :18623, “not met”, is withdrawn (ERRATA E-%s-2); that line is not edited. The discharge says nothing about zeta and nothing on whether the analysis of the seven classes is complete; B3 stands as PATHS_TO_THE_CRITICAL_LINE has it.' % (
            ot_words, pins['zq_coeff_not_multiplicative'], pins['cQ_not_nonneg'], dj['kernel']['main'], date),
        '`W-ORD-WSC-KERNEL-CITES` (:18625): discharged at b760 under `(R370)`(10) by the edition of `(R370)`(7): Which Structure Confines stands at v2.5.0 (`%s`, PLACE-papers %s), its row at :219 (v2.4.0’s :203) taking `zq_coeff_not_multiplicative` as the terminal of its instance at discriminant −23, and the sentence of its head that the document cites no kernel re-cut with it (:214, v2.4.0’s :198).' % (
            E.V25, E.git(PP, 'log', '-1', '--format=%h', '--abbrev=8', '--', E.V25).strip()),
        '`W-ORD-KEYSTONE-HEADS` (:15454, re-scoped at :16565): answered for Which Structure Confines at v2.5.0, whose opening states its results by terminal and by status (its :13, key W2 of `(R370)`(7)); the order stands for the next re-cut.',
        '`W-ORD-WSC-TITCHMARSH` entered under `(R370)`(10), priced by no build, in the ruling’s words: “%s”' % titchmarsh()]
    for k, v, is_late in orders:
        if is_late:
            sp, sn = late_src[k]
            paras.append('`W-ORD-RECUT-QUOTE-%s` entered under `(R370)`(8), late, priced by no build: key %s of `(R369)`(9) changed %s :%d at b759, before any quotation search of it, and these lines of live papers carry the sentence it changed, none edited: %s. The seat’s reading: %s. Each line is read against the sentence as changed and re-cut to it or kept with its reason; trigger, the next edition of each document named (relay data/b760_late_quotes.txt).' % (
                k, k, sp, sn, paths_lines(v), ORDER_READ[k]))
        else:
            wk = wkeys[k]
            paras.append('`W-ORD-RECUT-QUOTE-%s` entered under `(R370)`(8), priced by no build: key %s of `(R370)`(7) %s the sentence at v2.4.0 :%d of Which Structure Confines, and these lines of live papers carry it, none edited: %s. The seat’s reading: %s. Each line is read against v2.5.0 and re-cut to it or kept with its reason; trigger, the next edition of each document named (relay data/b760_quote.json, data/b760_wsc_cut.txt).' % (
                k, k, 'removes' if wk['kind'] == 'REMOVE' else 're-cuts', wk['n'], paths_lines(v), ORDER_READ[k]))
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    # ### REGISTRY and the census
    reg = '*Dated note, b760, %s, under the author\'s ruling `(R370)`(11), to the row d1-3 (:85): Which Structure Confines stands at v2.5.0 (`%s`) beside v2.4.0 and v2.3.1, each unedited, and confers no grade. No cell of the row and no other row is edited. Nothing here is deposited.*' % (date, E.V25)
    cen = '*Appended %s by b760 under the author\'s ruling `(R370)`(11):* Which Structure Confines stands at v2.5.0 (`%s`), its version line reading “%s” %s No byte above this line changes.' % (
        date, E.V25, vline.strip('*'), s7[0].upper() + s7[1:])
    return dict(standing=standing, s7=s7, orders=orders, texts={ERRATA: e1 + NL + NL + e2, OT: ot, REG: reg, CEN: cen},
                ids_new=['E-%s-1' % date, 'E-%s-2' % date], names_new=['W-ORD-WSC-TITCHMARSH'] + ['W-ORD-RECUT-QUOTE-%s' % k for k, _v, _l in orders])


def qhead_at(text):
    hits = [k + 1 for k, l in enumerate(text.split(NL)) if sha(l)[:16] == QHEAD]
    return hits


def ledgers(mode):
    date, before = today(), unedited()
    C = compose_ledgers(date)
    base = dict((p, at_head(p)) for p in (ERRATA, OT, REG, CEN))
    reg85 = base[REG].split(NL)[84]
    bad = []
    if not (reg85.startswith('| d1-3 |') and 'Which Structure Confines' in reg85):
        bad.append('REGISTRY :85 is not row d1-3')
    for i in C['ids_new']:
        if i in base[ERRATA]:
            bad.append('ERRATA holds %s' % i)
    for nm in C['names_new']:
        if nm in base[OT]:
            bad.append('OPEN_TRAILS holds %s' % nm)
    if any('‹' in x or '›' in x for x in C['texts'].values()):
        bad.append('a field left in a text')
    if bad:
        die('THE LEDGERS DO NOT HOLD %s' % bad)
    new = dict((p, base[p] + NL + C['texts'][p] + NL) for p in base)
    I, _SC = E.ids()
    rows = []
    for p in (ERRATA, OT, REG, CEN):
        b, n_ = base[p], new[p]
        bl, nl_ = b.split(NL)[:-1], n_.split(NL)[:-1]
        rows.append(dict(path=p, lines_before=len(bl), lines_after=len(nl_), first_new=len(bl) + 2, sha_before=sha(b)[:16], sha_after=sha(n_)[:16],
                         text_sha=sha(C['texts'][p])[:16], prefix=n_.startswith(b), ids_equal=E.idcount(b, I) == E.idcount(n_, I),
                         ids_added=sum(E.idcount(C['texts'][p], I).values())))
    qb, qa = qhead_at(base[REG]), qhead_at(new[REG])
    after_u = unedited()
    ctl = [('each file`s bytes at HEAD a prefix of its new bytes: no line moves', all(r['prefix'] for r in rows)),
           ('the identifiers` counts equal before and after in each file', all(r['ids_equal'] for r in rows)),
           ('the identifiers in the appended texts 0', not any(r['ids_added'] for r in rows)),
           ('rule [Q] (3)`s heading by its digest at one line, the same before and after (%s -> %s)' % (qb, qa), len(qb) == 1 and qb == qa),
           ('REGISTRY :85 row d1-3, not edited; nothing added above the heading', base[REG].split(NL)[:qb[0]] == new[REG].split(NL)[:qb[0]] if qb else False),
           ('the IDs %s and the names %s not held before' % (', '.join(C['ids_new']), ', '.join(C['names_new'])), True),
           ('v2.3.1, v2.4.0, v2.5.0 and the Epstein v0.1 unchanged', before == after_u),
           ('(6) %s: the texts where it stands' % ('STANDS' if C['standing'] else 'STRUCK'), C['standing'])]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R370)(10) AND (11): ERRATA, OPEN_TRAILS, REGISTRY AND THE CENSUS, EACH APPENDED AT ITS END (%s)' % (ACT, E.utc()), '',
         '### tools/b760_ledgers.py ledgers; PLACE-papers HEAD %s; each appended text composed from BLOCK E and F (data/b760_text.txt), the discharge bank, the' % E.git(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
         '### ferry (:21, :27), the author`s word (data/b759_author_answers.txt :12) and the two searches` orders; each by line and sha256 here.', '',
         '## THE CONTROLS']
    P += ['  %-110s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE FILES: path | lines before -> after | the appended text from | its sha256 | the file`s sha256 before -> after']
    P += ['  %s | %d -> %d | :%d | %s | %s -> %s' % (r['path'], r['lines_before'], r['lines_after'], r['first_new'], r['text_sha'], r['sha_before'], r['sha_after']) for r in rows]
    P += ['', '## THE ORDERS ENTERED: W-ORD-WSC-TITCHMARSH ; ' + ' ; '.join('W-ORD-RECUT-QUOTE-%s (%d line%s%s)' % (k, len(v), '' if len(v) == 1 else 's', ', late' if l_ else '') for k, v, l_ in C['orders']),
          '## (7)`S SENTENCE AS FILLED, sha256 %s' % sha(C['s7'])[:16]]
    P += ['', '### ### **THE LEDGERS: FILES 4 OF 4 APPENDED, NO LINE MOVING ; ERRATA %s ; ORDERS ENTERED %d ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
        ' AND '.join(C['ids_new']), 1 + len(C['orders']), sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        for p in (ERRATA, OT, REG, CEN):
            print(NL + '### THE TEXT APPENDED TO %s (the dry run`s print alone):' % p)
            print(C['texts'][p])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if any(E.idcount(NL.join(P), I).values()):
        die('AN IDENTIFIER IN THE BANK')
    for p in (ERRATA, OT, REG, CEN):
        with open(os.path.join(PP, *p.split('/')), 'wb') as f:
            f.write(new[p].encode('utf-8'))
    if any(E.fsha(os.path.join(PP, *p.split('/'))) != sha(new[p])[:16] for p in new) or unedited() != before:
        die('A WRITTEN FILE IS NOT ITS COMPOSITION, OR A FILE BESIDE THEM MOVED')
    E.put(LBANK, NL.join(P) + NL)
    E.put(LJSON, json.dumps(dict(at=E.utc(), act=ACT, files=rows, orders=dict((('W-ORD-RECUT-QUOTE-' + k), [list(x) for x in v]) for k, v, _l in C['orders']),
                                 titchmarsh=True, errata=C['ids_new'], sentence7_sha256=sha(C['s7'])[:16], controls=[[w, o] for w, o in ctl]),
                            ensure_ascii=False, indent=1) + NL)
    print('written ERRATA.md, OPEN_TRAILS.md, REGISTRY.md and %s; data/b760_ledgers.txt and .json' % CEN)


def main(argv):
    what, mode = (argv + ['', ''])[:2]
    if mode not in ('dry', 'write'):
        sys.exit(__doc__)
    if what == 'epstein':
        epstein(mode)
    elif what == 'ledgers':
        ledgers(mode)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
