# -*- coding: utf-8 -*-
"""tools/b762_onepage_map.py -- (R372)(5): THE MAP BEFORE THE WRITING (data/b762_ferry.txt :17). Written by the Write tool at b762's
Component 3 and committed before its first run (N2); its writes data/b762_onepage_map.txt and data/b762_onepage_map.json alone, before the
page of (6) is composed. It reads PLACE-papers at HEAD by git alone, the live papers as tools/standing/subject.py live_papers gives them
((R370)(8)'s set, the four ledgers and the archived and deposited copies out), and quotes no line of a paper: a hit is printed by path and
line with the name or the words it matched.

THE NAMES' PART: each Lean name of BLOCK P's table between backticks, its Declaration column (data/b762_text.txt; data/b762_misses.txt (2)),
over the live papers, by path and line; One Page's own family (the deposited edition's file, day1/ONE_PAGE_PROOF.md) printed apart and
counted neither among the live papers read nor among the papers that carry a name (misses (3)). A name is carried where a line holds it as a
whole identifier, bare or under its namespace; the qualified shape, the name as the table prints it, is counted beside.
THE POINTERS' PART: each line of the live papers, REGISTRY, SPIRAL_MAP and the census at HEAD that names the page by "One Page" with a space or
a hyphen, case ignored, or by the stem ONE_PAGE_PROOF (misses (4)), classed PROOF-WORDED where, the stem's occurrences removed, the line
carries the word proof (or proofs) in any case, PLAIN otherwise; REGISTRY's rule [Q] (3) section skipped by its heading's digest, as the
subject reader skips it. The wider shapes' yields are printed beside the governing ones for the hand read.

  control   the controls, printed; nothing written
  dry       the map composed and printed; nothing written
  write     the map banked, refused where the page stands at HEAD or in the tree, or a control is not as wanted
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
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import subject as S   # noqa: E402
import handoff as HO   # noqa: E402

NL = '\n'
ACT = 'b762'
PP = S.PP
TEXT = os.path.join(D, 'b762_text.txt')
PAGE = 'day1/ONE_PAGE_PROOF_v2_0.md'            # ### (6)'s stem clause (data/b762_misses.txt (1))
DEPOSITED = 'day1/ONE_PAGE_PROOF.md'
FAMILY = S.family_of(PAGE)
REGISTRY = 'REGISTRY.md'
SPIRAL = 'SPIRAL_MAP.md'
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'   # ### the census the citation check reads (tools/acts/b762.py, ruling (5))
BANK = os.path.join(D, 'b762_onepage_map.txt')
JBANK = os.path.join(D, 'b762_onepage_map.json')
TITLE = re.compile(r'(?i)(?<!\w)one[ -]page(?!\w)')
STEM = re.compile(r'(?i)(?<![A-Za-z0-9])one_page_proof')
WIDE = re.compile(r'(?i)one[\s_-]*page')
PROOF = re.compile(r'(?i)(?<![a-z])proofs?(?![a-z])')
PROOF_NARROW = re.compile(r'(?i)(?<![a-z])proof(?![a-z])')
PROOF_WIDE = re.compile(r'(?i)proof')
WIN = 24
PLANT_NAME = 'B321.b762_planted_name_carried_by_none'
PLANTS = (('the One Page proof, a planted line', 'PROOF-WORDED'), ('One-Page Proofs, planted', 'PROOF-WORDED'),
          ('day1/ONE_PAGE_PROOF.md, a planted line with the stem alone', 'PLAIN'), ('a proof planted alone', None),
          ('a one-pager, planted', None))


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(*a):
    r = subprocess.run(['git', '-C', PP, *a], capture_output=True)
    if r.returncode:
        die('git %s EXITED %d' % (' '.join(a[:2]), r.returncode))
    return r.stdout.decode('utf-8', 'replace')


def names():
    """[(name, text line)] of BLOCK P's table, its Declaration column's backticked spans, in the table's order."""
    t = io.open(TEXT, encoding='utf-8').read().replace('\r', '').split(NL)
    a = [i for i, l in enumerate(t) if l == 'NEW>>']
    b = [i for i, l in enumerate(t) if l == '<<NEW']
    if len(a) != 1 or len(b) != 1 or a[0] > b[0]:
        die('BLOCK P`S MARKERS NOT ONE EACH IN ORDER (%s, %s)' % (a, b))
    out = []
    for i in range(a[0] + 1, b[0]):
        l = t[i]
        if not l.startswith('| '):
            continue
        cells = [c.strip() for c in l.split('|')]
        if len(cells) < 6 or cells[2] == 'Declaration':
            continue
        out += [(m.group(1), i + 1) for m in re.finditer(r'`([^`]+)`', cells[2])]
    return out, (a[0] + 2, b[0])


def short(n):
    return n.rsplit('.', 1)[-1]


def name_re(n):
    return re.compile(r'(?<!\w)' + re.escape(short(n)) + r'(?!\w)')


def qual_re(n):
    return re.compile(r'(?<![\w.])' + re.escape(n) + r'(?!\w)')


def pointer(line):
    """(names the page, class, matched words) of one line: the title's opening words or the stem; PROOF-WORDED where the line, the stem's
    occurrences removed, carries the word."""
    t_, s_ = [m.group(0) for m in TITLE.finditer(line)], [m.group(0) for m in STEM.finditer(line)]
    if not (t_ or s_):
        return False, None, []
    pw = [m.group(0) for m in PROOF.finditer(STEM.sub(' ', line))]
    return True, 'PROOF-WORDED' if pw else 'PLAIN', t_ + s_ + pw


def corpus():
    head = git('rev-parse', 'HEAD').strip()
    live, fig = S.live_papers('HEAD', PP)
    tree = git('ls-tree', '-r', '-z', '--name-only', 'HEAD').split('\0')
    fam = [p for p in live if S.family_of(p) == FAMILY]
    others = [p for p in live if S.family_of(p) != FAMILY]
    census_eds = sorted(p for p in tree if S.family_of(p) == S.family_of(CENSUS))
    texts = dict((p, S.blob(p, 'HEAD', PP)) for p in set(live) | {REGISTRY, SPIRAL, CENSUS})
    reg = texts[REGISTRY]
    try:
        k = HO.head_line(reg)
    except HO.Refuse as e:
        die('REGISTRY`S RULE [Q] (3) HEADING NOT FOUND BY ITS DIGEST (%s)' % e)
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', reg[k - 1])   # ### handoff.qword's reading of the heading, the word held and never printed
    if not m:
        die('REGISTRY :%d CARRIES THE HEADING`S DIGEST AND NO LEADING WORD' % k)
    q = (re.compile(r'\b%s\b' % re.escape(m.group(2)), re.I), m.group(2), len(m.group(1)), k)
    skip = set(HO.protected(REGISTRY, reg, q))   # ### the section under the heading and the lines about each line carrying the word, cited and not read
    return dict(head=head, live=live, fig=fig, tree=set(tree), fam=fam, others=others, census_eds=census_eds, texts=texts, qskip=skip, qhead=k, qrx=q[0])


def names_part(C, N):
    rows = []
    for n, tl in N:
        rs, rq = name_re(n), qual_re(n)
        hits, qn, dep = {}, 0, []
        for p in C['others']:
            for i, l in enumerate(C['texts'][p], 1):
                if rs.search(l):
                    hits.setdefault(p, []).append(i)
                if rq.search(l):
                    qn += 1
        for p in C['fam']:
            dep += [(p, i) for i, l in enumerate(C['texts'][p], 1) if rs.search(l)]
        rows.append(dict(name=n, text_line=tl, papers=len(hits), lines=sum(len(v) for v in hits.values()), qualified_lines=qn,
                         hits=dict((p, v) for p, v in sorted(hits.items())), deposited=dep))
    return rows


def pointers_part(C):
    files = [(p, 'live') for p in sorted(C['others'])] + [(REGISTRY, 'ledger')] + [(p, 'named by (5), not live') for p in (SPIRAL, CENSUS) if p not in C['live']]
    rows, wide, apart = [], [], []
    for p, cls in files + [(p, 'apart') for p in sorted(C['fam'])]:
        for i, l in enumerate(C['texts'][p], 1):
            if p == REGISTRY and i in C['qskip']:
                continue
            ok, kind, words = pointer(l)
            if ok:
                r = dict(path=p, line=i, cls=cls, kind=kind, words=words,
                         narrow=bool(PROOF_NARROW.search(STEM.sub(' ', l))), wide=bool(PROOF_WIDE.search(STEM.sub(' ', l))))
                (apart if cls == 'apart' else rows).append(r)
            elif WIDE.search(l) and cls != 'apart':
                wide.append(dict(path=p, line=i, cls=cls, words=[m.group(0) for m in WIDE.finditer(l)]))
    return files, rows, wide, apart


def spans_removed(line, regs):
    cut = [(m.start(), m.end()) for r in regs for m in r.finditer(line)]
    out, k = [], 0
    for a, b in sorted(cut):
        if a > k:
            out.append(line[k:a])
        k = max(k, b)
    out.append(line[k:])
    return [s.strip() for s in out if len(s.strip()) >= WIN]


def quoted(bank, C, N, prow, wide, paths):
    """the 24-character windows of each matched line's text outside its matched spans and outside the paths the bank prints, found in the
    bank: [] wanted."""
    have = set(bank[i:i + WIN] for i in range(len(bank) - WIN + 1))
    path_re = re.compile('|'.join(re.escape(p) for p in sorted(paths, key=len, reverse=True)))
    regs = [name_re(n) for n, _t in N] + [qual_re(n) for n, _t in N] + [TITLE, STEM, PROOF, WIDE, path_re]   # ### every name, word and path the bank prints
    lines = set()
    for n, _t in N:
        rs = name_re(n)
        lines |= set((p, i) for p in C['others'] for i, l in enumerate(C['texts'][p], 1) if rs.search(l))
    lines |= set((r['path'], r['line']) for r in list(prow) + list(wide))
    found = []
    for p, i in sorted(lines):
        for seg in spans_removed(C['texts'][p][i - 1], regs):
            if any(seg[j:j + WIN] in have for j in range(0, len(seg) - WIN + 1, 6)):
                found.append((p, i))
                break
    return found


def idcount(text):
    import b762_address_scan as SC
    low = text.lower()
    I = dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())
    return dict((k, low.count(v.lower())) for k, v in I.items() if v)


def controls(C, N, bank=None, paths=()):
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    dotted = sum(1 for n, _t in N if '.' in n)
    c('BLOCK P`s Declaration column: 23 names, each once, 19 under a namespace and 4 of SIDE-kernel bare', (len(N), len(set(n for n, _ in N)), dotted),
      len(N) == 23 and len(set(n for n, _ in N)) == 23 and dotted == 19)
    pr = name_re(PLANT_NAME)
    ph = [(p, i) for p in C['live'] for i, l in enumerate(C['texts'][p], 1) if pr.search(l)]
    c('a planted name read over every live paper is carried by none', '%s: %d lines' % (PLANT_NAME, len(ph)), not ph)
    pos = bool(name_re('B321.h2_sign_iff_rh').search('see `B321.h2_sign_iff_rh` and h2_sign_iff_rh’s converse'))
    neg = bool(name_re('B321.h2_sign').search('only h2_sign_iff_rh here'))
    c('a planted line carrying a name reads carried; a name inside a longer identifier does not', (pos, neg), pos and not neg)
    got = [(w_, pointer(w_)[1] if pointer(w_)[0] else None) for w_, _k in PLANTS]
    c('the planted lines read as wanted (the page beside the word PROOF-WORDED; the stem alone PLAIN; no page, no pointer)',
      ', '.join('%s' % g for _w, g in got), [g for _w, g in got] == [k for _w, k in PLANTS])
    c('the page absent at HEAD and in the tree (the map stands before the page)', (PAGE in C['tree'], os.path.exists(os.path.join(PP, PAGE))),
      PAGE not in C['tree'] and not os.path.exists(os.path.join(PP, PAGE)))
    c('One Page`s own family among the live papers: the deposited edition`s file alone', C['fam'], C['fam'] == [DEPOSITED])
    c('REGISTRY`s rule [Q] (3) section found by its heading`s digest and skipped, no line of it read or printed', '%d lines from :%d' % (len(C['qskip']), C['qhead']),
      len(C['qskip']) > 0)
    c('the census the act names standing at HEAD, its family`s editions printed', '%s (%s)' % (CENSUS in C['tree'], ', '.join(C['census_eds'])), CENSUS in C['tree'])
    if bank is not None:
        q = quoted(bank, C, N, bank_rows['p'], bank_rows['w'], paths)
        plant = 'the One Page proof planted, a sentence of the paper long enough to stand quoted whole in a bank'
        seg = spans_removed(plant, [TITLE, STEM, PROOF])
        pb = bank + NL + (seg[0] if seg else '')
        have_p = set(pb[i:i + WIN] for i in range(len(pb) - WIN + 1))
        fire = bool(seg) and any(seg[0][j:j + WIN] in have_p for j in range(0, len(seg[0]) - WIN + 1, 6))
        c('the bank quotes no line of a paper beyond the name or the words matched (24-character windows); a planted quotation found', (q[:5], fire), not q and fire)
        ids = idcount(bank)
        c('no identifier of the author in the bank', ids, not any(ids.values()))
        qn = len(C['qrx'].findall(bank))
        c('rule [Q] (3)`s word in the bank (the count alone printed)', qn, qn == 0)
    return L, ok


bank_rows = {}


def compose():
    t0 = time.time()
    N, (a, b) = names()
    C = corpus()
    nrows = names_part(C, N)
    files, prow, wide, apart = pointers_part(C)
    bank_rows.update(p=prow, w=wide)
    f = len(C['others'])
    carried = [r for r in nrows if r['papers']]
    pw = [r for r in prow if r['kind'] == 'PROOF-WORDED']
    pw_live = [r for r in pw if r['cls'] == 'live']
    d = sorted(set(r['path'] for r in pw_live))
    ledger_pw = [r for r in pw if r['cls'] != 'live']
    paths = set(C['live']) | {REGISTRY, SPIRAL, CENSUS, PAGE, DEPOSITED}
    at = utc()
    sentence = 'the map: %d names read over %d live papers, %d carried by another paper; %d lines name the page, %d of them PROOF-WORDED in %d live papers' % (
        len(N), f, len(carried), len(prow), len(pw), len(d))
    L = ['%s -- (R372)(5): THE MAP BEFORE THE WRITING: THE NAMES OF ONE PAGE`S TABLE AND THE LINES THAT NAME THE PAGE, OVER PLACE-papers` LIVE PAPERS AT HEAD (%s)' % (ACT, at), '',
         '### PLACE-papers HEAD %s; its live papers by tools/standing/subject.py live_papers: %d (REGISTRY names %d paths, %d families, %d unresolved; the' % (
             C['head'][:8], len(C['live']), C['fig'].get('named', 0), C['fig'].get('families', 0), C['fig'].get('unresolved', 0)),
         '### four ledgers and the archived and deposited copies out). One Page`s own family (%s): %s, printed apart and counted neither among the %d live' % (
             FAMILY, ', '.join(C['fam']), f),
         '### papers read nor among the papers that carry a name (data/b762_misses.txt (3)); the page, %s, absent at HEAD and in the tree.' % PAGE,
         '### THE NAMES: BLOCK P`s Declaration column (data/b762_text.txt :%d-:%d), %d names. A name is carried where a line holds it as a whole identifier,' % (a, b, len(N)),
         '### bare or under its namespace (the governing shape); the qualified shape, the name as the table prints it, counted beside.',
         '### THE POINTERS: a line names the page where it carries "One Page" with a space or a hyphen, case ignored, or the stem ONE_PAGE_PROOF, case',
         '### ignored; PROOF-WORDED where, the stem`s occurrences removed, it carries the word proof or proofs in any case; PLAIN otherwise. Files: the',
         '### live papers; REGISTRY, a ledger, its rule [Q] (3) section skipped by its heading`s digest (%d lines, none read or printed); SPIRAL_MAP and' % len(C['qskip']),
         '### the census (%s) at HEAD, %s. No line of a paper is quoted: a hit is printed by path and line with the name or words it matched.' % (
             CENSUS, 'each among the live papers' if SPIRAL in C['live'] and CENSUS in C['live'] else 'SPIRAL_MAP %s, the census %s' % (
                 'live' if SPIRAL in C['live'] else 'not live', 'live' if CENSUS in C['live'] else 'not live')), '']
    body = ['## THE NAMES` PART: %d NAMES OVER %d LIVE PAPERS' % (len(N), f)]
    for k, r in enumerate(nrows, 1):
        body.append('  (%d) %s [data/b762_text.txt :%d] | carried by %d live papers, %d lines | the qualified shape %d lines | the deposited edition: %s' % (
            k, r['name'], r['text_line'], r['papers'], r['lines'], r['qualified_lines'], ', '.join(':%d' % i for _p, i in r['deposited']) or 'none'))
        body += ['      %s %s' % (p, ', '.join(':%d' % i for i in v)) for p, v in r['hits'].items()] or ['      carried by none']
    body += ['', '## THE POINTERS` PART: %d LINES NAME THE PAGE, %d PROOF-WORDED, IN %d FILES' % (len(prow), len(pw), len(set(r['path'] for r in prow)))]
    body += ['  %s (%s) :%d %s -- matched: %s' % (r['path'], r['cls'], r['line'], r['kind'], ', '.join(r['words'])) for r in prow] or ['  none']
    body += ['', '## ONE PAGE`S OWN FAMILY, APART: %d LINES' % len(apart)]
    body += ['  %s :%d %s -- matched: %s' % (r['path'], r['line'], r['kind'], ', '.join(r['words'])) for r in apart] or ['  none']
    body += ['', '## THE WIDER SHAPES, FOR THE HAND READ',
             '  the names, the qualified shape beside the governing: lines %d against %d; names carried in the qualified shape by another paper %d against %d' % (
                 sum(r['qualified_lines'] for r in nrows), sum(r['lines'] for r in nrows), sum(1 for r in nrows if r['qualified_lines']), len(carried)),
             '  the pointers, "one" and "page" with any separator or none, the governing shapes not matching: %d lines%s' % (
                 len(wide), (' -- ' + '; '.join('%s :%d (%s)' % (r['path'], r['line'], ', '.join(r['words'])) for r in wide)) if wide else ''),
             '  the word among the pointer lines: proof alone %d, proof or proofs %d (governing), proof as any part of a word %d' % (
                 sum(1 for r in prow if r['narrow']), len(pw), sum(1 for r in prow if r['wide']))]
    body += ['', '## WHAT FOLLOWS ((R372)(5))']
    if pw_live:
        body += ['  [O6] ENTERED: %d live papers name One Page beside the word proof, at %s; no paper is edited.' % (
            len(d), '; '.join('%s :%d' % (r['path'], r['line']) for r in pw_live))]
    else:
        body += ['  [O6] NOT ENTERED: no live paper calls the page a proof.']
    body += ['  the ledgers` and the named files` PROOF-WORDED lines, printed and not edited: %s' % ('; '.join('%s :%d' % (r['path'], r['line']) for r in ledger_pw) or 'none'),
             '  REGISTRY`s row of One Page answered by [G1] at Component 4.', '', '## THE ENTRY`S SENTENCE', '  ' + sentence]
    secs = time.time() - t0
    draft = NL.join(L + body)
    Lc, ok = controls(C, N, draft, paths)
    foot = '### ### **THE MAP: NAMES %d OVER %d LIVE PAPERS, %d CARRIED BY ANOTHER PAPER, %d BY NONE ; POINTER LINES %d, PROOF-WORDED %d IN %d LIVE PAPERS ; [O6] %s ; CONTROLS %d OF %d AS WANTED ; %.1f s.**' % (
        len(N), f, len(carried), len(N) - len(carried), len(prow), len(pw), len(d), 'ENTERED' if pw_live else 'NOT ENTERED', sum(ok), len(ok), secs)
    text = NL.join(L + ['## THE CONTROLS'] + Lc + [''] + body + ['', foot]) + NL
    j = dict(at=at, act=ACT, head=C['head'], live_papers=len(C['live']), read=f, family_apart=C['fam'], page=PAGE, names=nrows,
             pointers=prow, apart=apart, wide=wide, proof_worded_live=[[r['path'], r['line']] for r in pw_live], d=len(d), d_papers=d,
             ledgers_proof_worded=[[r['path'], r['line'], r['cls']] for r in ledger_pw], o6=bool(pw_live), sentence=sentence,
             controls=dict(ok=sum(ok), of=len(ok)), seconds=round(secs, 1), census=CENSUS, census_editions=C['census_eds'], qskip=len(C['qskip']))
    return text, j, all(ok), Lc


def put(path, text):
    with open(path + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        N, _ab = names()
        C = corpus()
        print(NL.join(controls(C, N)[0]))
    elif a[:1] in (['dry'], ['write']):
        text, j, allok, Lc = compose()
        print(text)
        if a[:1] == ['dry']:
            sys.exit(0 if allok else 2)
        if not allok:
            die('THE CONTROLS NOT AS WANTED')
        js = json.dumps(j, ensure_ascii=False, indent=1)
        if any(idcount(js).values()):
            die('AN IDENTIFIER IN THE JSON')
        put(BANK, text)
        put(JBANK, js + NL)
        print('written data/b762_onepage_map.txt (%d bytes, sha256 %s) and data/b762_onepage_map.json' % (
            len(text.encode('utf-8')), hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]))
    else:
        sys.exit(__doc__)
