# -*- coding: utf-8 -*-
"""tools/b759_errata.py -- (R369)(10): ERRATA AND THE ORDERS. "ERRATA.md takes BLOCK E's two entries at the file's end, in the form of
E-2026-11-09-1, their fields filled; E-2026-11-06-1 is not edited. OPEN_TRAILS, appended under one dated head, no line moving: b758's root
answer; then W-ORD-MECHANISM-ATTRIBUTION (:17932), its condition read by the navigator as (R368)(5) left it to this ruling: not met. ... The
order stays open on the author's word, those two statements entered beside it, and no sentence of this act says the catalogue has or has not met
the zero. Five orders entered by name, each priced by no build. ..." (data/b759_ferry.txt :31). With (9)'s orders W-ORD-RECUT-<key> for the
lines (9) left (data/b759_corpus.json). Written whole at b759's Component 6; committed before it runs; one PLACE-papers commit an item.

THE SOURCES: BLOCK E of data/b759_text.txt (the two entries, a paragraph a line); the fields DATE and WEILERR from data/b759_fields.json; N
and DEPOSITS from data/b759_fields_corpus.json (tools/b759_fields.py corpus, (7)'s tool), N read equal to the corpus bank's count; the lines'
paragraphs from data/b759_corpus.json's rows and BLOCK D; b758's root answer quoted whole from relay data/b758_author_answers.txt :31 under its
head at :30; T0's words and T1's witness from b758's (5) sentence in data/b758_outcomes.json, and T0's and T1's heads and the witness's statement
read at data/b758_epstein_statements.txt :63, :99, :94; the five orders cut from (10)'s words in the ferry bank. Each relay source read at relay
HEAD. The composed lines are printed whole and banked by digest and length.
  control | dry <errata|trails|all> | write <errata|trails>      BANK data/b759_errata.json
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K     # noqa: E402
import b759_notes as NT       # noqa: E402  (append_lines, check_lf, as committed)

ACT = 'b759'
PP = K.PP
NL = '\n'
LBR, RBR = '‹', '›'
BANK = os.path.join(RELAY, 'data', 'b759_errata.json')
ITEMS = {'errata': 'ERRATA.md', 'trails': 'OPEN_TRAILS.md'}
ORDER = ('errata', 'trails')
B758_ANS, ANS_HEAD_LINE, ANS_LINE, ANS_RESULT = 'data/b758_author_answers.txt', 30, 31, 28
ANS_HEAD = '### THE AUTHOR`S WORD (transcript line 129762), BEGIN to END, verbatim:'
MECH = 'W-ORD-MECHANISM-ATTRIBUTION'
MECH_LINE = 17932
FIVE = ('W-ORD-WSC-KERNEL-CITES', 'W-ORD-LI-INDEX', 'W-ORD-CAPACITY-ATTRIBUTION', 'W-ORD-BIBLIOGRAPHY-LINK', 'W-ORD-EPSTEIN-SECTIONS-3-4')
T0_WORDS = "the control's halved coefficients are not multiplicative"
T48_WORDS = 'its coefficient at 48 is -8 log 2 - 2 log 3'
STATEMENTS = 'data/b758_epstein_statements.txt'
T0_LINE, T0_HEAD = 63, 'T0: THE HALVED COEFFICIENTS OF Z_Q ARE NOT MULTIPLICATIVE.'
T1_LINE, T1_HEAD = 99, 'T1: THE COEFFICIENTS OF −Z_Q′/Z_Q ARE NOT ALL NONNEGATIVE.'
T48_LINE, T48_HEAD = 94, 'theorem cQ_forty_eight : cQ 48 = -(8 * Real.log 2) - 2 * Real.log 3'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, (r.stdout if raw else r.stdout.decode('utf-8', 'replace'))


def digest(s):
    return hashlib.sha256(s if isinstance(s, bytes) else s.encode('utf-8')).hexdigest()[:16]


def relay_head(rel):
    rc, out = git(RELAY, 'show', 'HEAD:%s' % rel)
    if rc:
        raise SystemExit('### %s NOT READ AT RELAY HEAD -- NOTHING DONE' % rel)
    return out.replace('\r', '')


def span(text, a, b):
    """the paragraphs (non-blank lines) between the marker line a and the next line opening b."""
    i = [k for k, l in enumerate(text) if l == a]
    if len(i) != 1:
        raise SystemExit('### THE MARKER %r NOT READ ONCE -- NOTHING DONE' % a)
    out = []
    for l in text[i[0] + 1:]:
        if l.startswith(b):
            break
        if l.strip():
            out.append(l)
    return out


def fill(s, F):
    for k, v in F.items():
        s = s.replace(LBR + k + RBR, v)
    return s


def cut_orders(c10):
    """{order: its words} for the five, cut from (10)'s line, each from its name to the next name or the line's end."""
    pos = [(c10.find(o + ': '), o) for o in FIVE]
    if any(p < 0 for p, _o in pos) or any(c10.count(o + ': ') != 1 for o in FIVE):
        return None
    pos.sort()
    out = {}
    for j, (p, o) in enumerate(pos):
        e = pos[j + 1][0] if j + 1 < len(pos) else len(c10)
        out[o] = c10[p + len(o) + 2:e].strip()
    return out


def line_para(row, BDk, dep):
    key, path, ln, cls, old, new = BDk
    head = '**%s**, `%s` :%d, %s.' % (key, path, ln, cls)
    if row and row['state'] == 'RE-CUT':
        s = '%s The line said: “%s” It now reads: “%s”' % (head, old, new)
        if dep:
            s += ' Its deposited copy (Zenodo record %s, REGISTRY :%d) is not edited; the line stands there as deposited.' % (dep[0][1], dep[0][0])
        return s
    why = row['why'] if row else 'not written'
    return '%s Not edited: %s; the order `W-ORD-RECUT-%s` entered in OPEN_TRAILS with its NEW, trigger the document’s next edition.' % (head, why, key)


def sources():
    import b759_corpus as CO
    F = json.loads(relay_head('data/b759_fields.json'))
    C = json.loads(relay_head('data/b759_corpus.json'))
    S = C.get('summary') or {}
    if not S or any(d.get('commit') is None for d in C['docs'] if d.get('changed')):
        raise SystemExit('### THE CORPUS BANK`S SUMMARY ABSENT OR A DOCUMENT UNCONFIRMED AT RELAY HEAD -- NOTHING DONE')
    text = io.open(os.path.join(RELAY, 'data', 'b759_text.txt'), encoding='utf-8').read().split(NL)
    BD = CO.block_d(text)
    by = dict((r['key'], r) for r in C['rows'])
    newf = dict((b[0], CO.fill(b[5], F) or b[5]) for b in BD)
    BDn = [b[:5] + (newf[b[0]],) for b in BD]
    deps = S.get('deposits') or {}
    paras = [line_para(by.get(b[0]), b, deps.get(b[1]) or []) for b in BDn]
    FE = json.loads(relay_head('data/b759_fields_corpus.json'))
    if FE.get('N') != str(len(S['recut'])) or not FE.get('DEPOSITS'):
        raise SystemExit('### N AND DEPOSITS NOT READ FROM data/b759_fields_corpus.json AT RELAY HEAD, OR N NOT THE CORPUS BANK`S COUNT -- NOTHING DONE')
    e1 = span(text, '@@ ERRATA 1', '@@ WEILERR')
    e2 = span(text, '@@ ERRATA 2', '@@ BLOCK F')
    fl = dict(DATE=F['DATE'], WEILERR=F.get('WEILERR') or '', N=FE['N'], DEPOSITS=FE['DEPOSITS'])
    e1f = [fill(x, fl) for x in e1]
    ph = [k for k, x in enumerate(e2) if x.startswith('**The lines.** ' + LBR)]
    if len(ph) != 1:
        raise SystemExit('### THE LINES` PLACEHOLDER NOT READ ONCE IN ERRATA 2 -- NOTHING DONE')
    e2f = [fill(x, fl) for x in e2]
    e2f = e2f[:ph[0]] + ['**The lines.** ' + paras[0]] + paras[1:] + e2f[ph[0] + 1:]
    A = relay_head(B758_ANS).split(NL)
    if A[ANS_HEAD_LINE - 1] != ANS_HEAD or not A[ANS_RESULT - 1].startswith('RESULT (transcript line 129762, 2026-11-17T14:04:33.961Z): '):
        raise SystemExit('### %s :%d IS NOT THE ROOT`S WORD AS READ -- NOTHING DONE' % (B758_ANS, ANS_LINE))
    o58 = json.loads(relay_head('data/b758_outcomes.json'))
    s58 = ' '.join(r.get('sentence') or '' for r in o58)
    if T0_WORDS not in s58 or T48_WORDS not in s58:
        raise SystemExit('### T0 OR T1`S WITNESS NOT READ IN b758`S OUTCOMES -- NOTHING DONE')
    st = relay_head(STATEMENTS).split(NL)
    for ln, w in ((T0_LINE, T0_HEAD), (T1_LINE, T1_HEAD), (T48_LINE, T48_HEAD)):
        if w not in st[ln - 1]:
            raise SystemExit('### %s :%d DOES NOT CARRY %r -- NOTHING DONE' % (STATEMENTS, ln, w))
    c10 = [l for l in relay_head('data/b759_ferry.txt').split(NL) if l.startswith('(10) ')]
    orders = cut_orders(c10[0]) if len(c10) == 1 else None
    if not orders:
        raise SystemExit('### THE FIVE ORDERS NOT CUT ONCE EACH FROM (10) -- NOTHING DONE')
    return dict(F=F, S=S, e1=e1f, e2=e2f, word=A[ANS_LINE - 1], orders=orders, recut_orders=S.get('orders') or [], date=F['DATE'])


def compose(k, data, X):
    if k == 'errata':
        L = data.decode('utf-8').split(NL)
        if not any(l.startswith('## E-2026-11-06-1 ') for l in L):
            raise SystemExit('### E-2026-11-06-1 NOT READ IN ERRATA -- NOTHING WRITTEN')
        if any(l.startswith('## E-%s-' % X['date']) for l in L):
            raise SystemExit('### AN ENTRY E-%s- STANDS ALREADY -- NOTHING WRITTEN' % X['date'])
        lines = X['e1'] + X['e2']
        left = [x for x in lines if LBR in x]
        if left:
            raise SystemExit('### A FIELD LEFT IN THE ENTRIES: %s -- NOTHING WRITTEN' % sorted(set(re.findall(LBR + '([^' + RBR + ']+)' + RBR, NL.join(left)))))
        d = NT.append_lines(data, lines)
        n = len(L)
        return d, [(n + 1 + 2 * j, s) for j, s in enumerate(lines)], dict(entries=['E-%s-1' % X['date'], 'E-%s-2' % X['date']])
    if k == 'trails':
        L = data.decode('utf-8').split(NL)
        if MECH not in L[MECH_LINE - 1]:
            raise SystemExit('### OPEN_TRAILS :%d DOES NOT CARRY %s -- NOTHING WRITTEN' % (MECH_LINE, MECH))
        nx = [i + 1 for i, l in enumerate(L) if l.startswith('**Next:** ')]
        th = [i + 1 for i, l in enumerate(L) if l.startswith('### b758 — ')]
        if not nx or len(th) != 1 or nx[-1] < th[0]:
            raise SystemExit('### b758`S TRAIL OR ITS NEXT LINE NOT READ AT THE FILE`S END -- NOTHING WRITTEN')
        if any(('`%s`' % o) in l and 'b759' in l for o in FIVE for l in L):
            raise SystemExit('### A FIVE ORDER ENTERED BY b759 STANDS ALREADY -- NOTHING WRITTEN')
        d8 = X['date']
        recut = X['recut_orders']
        head = ('**Dated head, %s, b759, `(R369)`(10): the lines the ruling orders for OPEN_TRAILS** (relay data/b759_ferry.txt :31), appended at the end '
                'of the file after b758’s trail (its last line :%d) and before this act’s own trail, so that no line of the trail moves: b758’s root '
                'answer; `%s`, its condition read; five orders entered by name%s.') % (
            d8, nx[-1], MECH, '; and the orders of `(R369)`(9) for the %d line(s) it left' % len(recut) if recut else '')
        one = ('*Appended %s by b759 to b758’s trail (:%d), under `(R369)`(10):* b758’s one question at the root was answered by the author’s word '
               '(relay data/b758_author_answers.txt :%d, :%d, 2026-11-17T14:04:33Z), quoted whole: “%s”') % (d8, th[0], ANS_RESULT, ANS_LINE, X['word'])
        two = ('`%s` (:%d): its condition read under `(R369)`(10), as `(R368)`(5) left it to this ruling: not met. T0 and T1 state two properties '
               'the control lacks, each compiled within the standard three on SIDE-explicit-formula’s main at v0.40 (relay data/b758_outcomes.txt; '
               'data/b758_epstein_statements.txt :%d, :%d, :%d): T0, %s (`zq_coeff_not_multiplicative`); T1, on the arithmetic side, the '
               'coefficients of −Z_Q′/Z_Q are not all nonnegative (`cQ_not_nonneg`), %s (`cQ_forty_eight`). Neither names a class of the kernel’s '
               'mechanism type, and neither draws the zero from the lack. The order stays open on the author’s word, these two statements entered '
               'beside it.') % (MECH, MECH_LINE, T0_LINE, T1_LINE, T48_LINE, T0_WORDS, T48_WORDS)
        five = ['`%s` entered under `(R369)`(10), priced by no build, in the ruling’s words: “%s”' % (o, X['orders'][o]) for o in FIVE]
        rc_ = ['`%s` entered under `(R369)`(9): %s :%d left; its NEW: “%s”; trigger: %s.' % (o['order'], o['path'], o['line'], o['new'],
                                                                                        o['trigger'].replace('`', '’')) for o in recut]
        lines = [head, one, two] + five + rc_
        d = NT.append_lines(data, lines)
        n = len(L)
        return d, [(n + 1 + 2 * j, s) for j, s in enumerate(lines)], dict(after=nx[-1], trail=th[0])
    raise SystemExit('### NO ITEM %r' % k)


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    t = ['@@ ERRATA 1', '## E-%sDATE%s-1 x' % (LBR, RBR), '', 'b%sWEILERR%s c' % (LBR, RBR), '@@ WEILERR COMPILED', ' w']
    sp = span(t, '@@ ERRATA 1', '@@ WEILERR')
    c('a span`s paragraphs to its next marker, the fields filled; an empty field leaves no gap', [fill(x, dict(DATE='2026-01-02', WEILERR='')) for x in sp],
      [fill(x, dict(DATE='2026-01-02', WEILERR='')) for x in sp] == ['## E-2026-01-02-1 x', 'b c'])
    c10 = '(10) x. Five orders. W-ORD-WSC-KERNEL-CITES: a b. W-ORD-LI-INDEX: c. W-ORD-CAPACITY-ATTRIBUTION: d. W-ORD-BIBLIOGRAPHY-LINK: e. W-ORD-EPSTEIN-SECTIONS-3-4: f g.'
    co = cut_orders(c10)
    c('the five orders cut, each to the next; one missing refused', (co, cut_orders(c10.replace('W-ORD-LI-INDEX: ', ''))),
      co == {'W-ORD-WSC-KERNEL-CITES': 'a b.', 'W-ORD-LI-INDEX': 'c.', 'W-ORD-CAPACITY-ATTRIBUTION': 'd.', 'W-ORD-BIBLIOGRAPHY-LINK': 'e.',
             'W-ORD-EPSTEIN-SECTIONS-3-4': 'f g.'} and cut_orders(c10.replace('W-ORD-LI-INDEX: ', '')) is None)
    b = ('C4', 'day1/A.md', 9, 'SHARPENED', 'old', 'new')
    p1 = line_para({'state': 'RE-CUT', 'why': ''}, b, [(83, '21539167')])
    p2 = line_para({'state': 'LEFT', 'why': 'the OLD stands twice'}, b, [])
    c('a line`s paragraph: re-cut with its deposit named; left with its order', (p1, p2),
      p1 == '**C4**, `day1/A.md` :9, SHARPENED. The line said: “old” It now reads: “new” Its deposited copy (Zenodo record 21539167, REGISTRY :83) is not edited; the line stands there as deposited.'
      and '`W-ORD-RECUT-C4`' in p2 and 'Not edited: the OLD stands twice' in p2)
    return L, ok


def load():
    return json.load(io.open(BANK, encoding='utf-8')) if os.path.exists(BANK) else []


def main(argv):
    if argv[:1] == ['control']:
        L, ok = controls()
        print(NL.join(L))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok), len(ok)))
        return
    if len(argv) != 2 or argv[0] not in ('dry', 'write') or argv[1] not in ORDER + ('all',) or (argv[0] == 'write' and argv[1] == 'all'):
        sys.exit(__doc__)
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    X = sources()
    if time.strftime('%Y-%m-%d', time.gmtime()) != X['date']:
        print('### NOTE: TODAY`S UTC DATE IS NOT THE FIELDS` DATE %s; THE ENTRIES TAKE THE FIELDS` DATE, THE DOCUMENT`S E-NUMBER' % X['date'])
    R = load()
    for k in (ORDER if argv[1] == 'all' else (argv[1],)):
        rel = ITEMS[k]
        p = os.path.join(PP, rel)
        rc, hb = git(PP, 'show', 'HEAD:%s' % rel, raw=True)
        wb = open(p, 'rb').read()
        if rc or hb != wb:
            sys.exit('### %s: THE WORKING COPY IS NOT HEAD`S BLOB -- NOTHING DONE' % rel)
        if argv[0] == 'write' and any(r.get('item') == k for r in R):
            sys.exit('### %s WRITTEN ALREADY (data/b759_errata.json) -- NOTHING DONE' % k)
        if argv[0] == 'write' and k == 'trails' and not any(r.get('item') == 'errata' for r in R):
            sys.exit('### ERRATA NOT WRITTEN FIRST -- NOTHING DONE')
        d, rows, notes = compose(k, hb, X)
        print('## %s (%s): HEAD sha256 %s, %d bytes -> %d bytes, sha256 %s ; %s' % (k, rel, digest(hb), len(hb), len(d), digest(d), notes))
        for ln, s in rows:
            print('  :%d %s' % (ln, s))
        if argv[0] == 'write':
            with open(p, 'wb') as fh:
                fh.write(d)
            back = open(p, 'rb').read()
            print('  written ; read back %s' % ('EQUAL' if back == d else 'NOT EQUAL'))
            R.append(dict(item=k, file=rel, at=stamp(), head_sha=digest(hb), new_sha=digest(back), bytes=len(back),
                          lines=[[ln, digest(s), len(s)] for ln, s in rows], notes=notes, read_back=back == d))
            js = json.dumps(R, indent=1, ensure_ascii=False)
            with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(js + NL)
            os.replace(BANK + '.tmp', BANK)
            print('  banked data/b759_errata.json (%d rows)' % len(R))


if __name__ == '__main__':
    main(sys.argv[1:])
