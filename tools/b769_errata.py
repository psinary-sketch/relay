# -*- coding: utf-8 -*-
"""tools/b769_errata.py -- b769, (R379)(5): THE ERRORS OF W-ORD-NOVEMBER-RIDERS ENTERED IN ERRATA, EACH AFTER ITS LINES AND THE DEPOSITED
COPIES ARE READ, WITH ITS FACT ITEM; [R3].

Written by the Write tool and committed before its run (N2); its forms from tools/b764_rulings.py (the read of outputs/ by each file's lines;
ERRATA's entry by b760's route, the file, a blank line, the entry, a line end) and tools/b769_rulings.py (the texts read from the ferry bank
between their marker lines and checked against their lines; the alternatives resolved by label; each file appended at its end, its bytes at
HEAD a prefix of its new bytes; the controls before the write; the ledger banked by line and sha256).

  read dry|write      Before any entry is filed (data/b769_ferry.txt :23): each line that [E2] to [E5] cite (the lines of their "Records
                      affected" sentences), read at the papers` repository's HEAD for the words the entry quotes as said there (the
                      phrases between double quotes in its "What the lines say." paragraph), each quoted phrase a needle, carried where
                      the line holds the phrase exactly (a reading with curly quotes, asterisks and whitespace normalised printed beside);
                      and outputs/ read for a deposited copy holding such a phrase, in the form of tools/b764_rulings.py deposit: each file
                      by its lines, how many of each cited paper's distinct lines of 40 characters or more stand in it; a file a copy of a
                      paper where it holds a quarter of them or more; a file deposited where it stands under outputs/DEPOSITED; for each
                      needle the lines of each file that hold it; for each deposited copy holding a needle, the copy's line for the cited
                      line (the line whole where it stands once, else the one line holding the needle, else the line holding it nearest
                      the cited line by similarity, the way printed). Counts, booleans and line numbers alone; no line of any file printed.
                      Bank: data/b769_errata_read.txt and .json.
  ledgers dry|write   From the read's bank, at the same HEAD: each entry whose needles are all carried is filed at ERRATA's end, numbered
                      E-<DATE>-1 on in the order [E2] to [E5], an entry not filed taking no number; its heading's alternative resolved by
                      the read (E2's on whether a deposited copy holds the theorem, :1380; E4's on whether one holds a quoted phrase; E3's
                      and E5's on the same, a found branch being the seat's to compose and so held); E2's and E4's clause on a deposited
                      copy composed from the read, naming each deposited copy with its lines and the words that the deposited file is
                      immutable at its version, or the ruling's words where none holds; each filed entry's fact item, [F2] to [F5], and
                      [R3] naming the entries filed, appended at OPEN_TRAILS' end under one dated head. Both files in one write. Controls
                      before the write, printed, four of them planted. Bank: data/b769_ledgers_c3.txt and .json, each text by line and
                      sha256; the texts' words printed by the dry run alone.

No PLACE-papers line is printed but the texts this tool composes; the account is counted, never printed; the [Q] word is derived in memory
from REGISTRY by its heading's digest, counted, never printed; no git write.
"""
import difflib
import hashlib
import json
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b769_rulings as RU   # noqa: E402

ACT, NL, PP, D, RELAY = RU.ACT, RU.NL, RU.PP, RU.D, RU.RELAY
sha, git, utc, today, die, put, jload, fsha = RU.sha, RU.git, RU.utc, RU.today, RU.die, RU.put, RU.jload, RU.fsha
ERRATA, OT, REG = 'ERRATA.md', RU.OT, RU.REG
C3PP = '41170e41'   # ### the papers` repository's last commit of the act before Component 3: [B1], [A4] and [C9] (step 32, events (62))
RBANK, RJSON = os.path.join(D, 'b769_errata_read.txt'), os.path.join(D, 'b769_errata_read.json')
LBANK, LJSON = os.path.join(D, 'b769_ledgers_c3.txt'), os.path.join(D, 'b769_ledgers_c3.json')
AP, TIS = 'day1/A_Place_to_Stand.md', 'phase1.5/deep-structure/TRIVIUM_IDENTITY_SUBSPACE.md'
RCC, P22 = 'phase1.5/rcurve/R_CURVE_CRITERION.md', 'phase1.5/rcurve/P22_REPORT.md'
SRZ, TUS = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'
GRH = 'phase1.5/spectral/GRH_CASCADE.md'
# ### each quoted phrase of an entry's "What the lines say." paragraph beside the line it is quoted from, in the entry's order of lines
NEEDLES = dict(
    E2=[(AP, 1380, 'folds at some'), (AP, 1382, 'attains a local maximum and returns to zero'), (AP, 315, 'no R-curve folds'),
        (AP, 1402, 'the absence of folds implies'), (AP, 1428, 'excluded off-line zeros'),
        (TIS, 558, 'which is equivalent to the Riemann Hypothesis'), (TIS, 562, 'a chain of four independent events'),
        (RCC, 46, 'each R-curve carries exactly one zero'), (RCC, 108, 'without a second crossing'), (RCC, 120, 'to vanish simultaneously')],
    E3=[(RCC, 416, 'Speiser (1934) proved RH'), (P22, 88, "connected to Speiser's theorem")],
    E4=[(SRZ, 156, 'The transversality magnitude grows as'), (SRZ, 349, 'would dramatically improve'), (TUS, 159, 'holds steady at'),
        (AP, 694, 'grows as approximately'), (AP, 1420, 'grows as'), (AP, 1422, 'growth persists at all heights'), (AP, 1792, 'growth rate')],
    E5=[(GRH, 173, 'for the Dirichlet'), (GRH, 67, 'Hooley (1967) proved'), (GRH, 248, 'closes given GRH'), (GRH, 571, 'carried as read'),
        (GRH, 575, 'carried as read'), (GRH, 175, 'With GRH established')])
ORDER = ('E2', 'E3', 'E4', 'E5')
FACT = dict(E2='F2', E3='F3', E4='F4', E5='F5')
THEOREM = (AP, 1380)          # ### "a deposited copy holding the theorem" ([E2]'s heading): the monograph's theorem, its line :1380
COPY_SHARE = 0.25             # ### a file a copy of a paper where it holds this share of the paper's distinct lines of 40 characters or more
DEP = 'outputs/DEPOSITED'     # ### b764's reading: a file deposited where it stands under a DEPOSITED folder
HEAD_FOUND = dict(E2="where the seat's read of outputs/ finds a deposited copy holding the theorem",
                  E4="where the seat's read of outputs/ finds a deposited copy holding a quoted phrase")
HEAD_NONE = 'where it finds none'
FILED_ALT = re.compile(r"<Where the seat['’]s read of outputs/ finds a deposited copy[^<>]*>")
NONE_SEP = '; where it finds none: '
R3_ALL = 'each of the four filed'
Q_DIGEST = '53d53060a58f6b9b'   # ### REGISTRY :374's digest, rule [Q]'s heading (data/b769_stepzero.txt; the word derived in memory, never printed)


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('*', '')
    return re.sub(r'\s+', ' ', s)


def show(rev, path):
    b = git(PP, 'show', '%s:%s' % (rev, path), raw=True)
    return b.decode('utf-8', 'replace').replace('\r', '').split(NL) if b else None


def and_list(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]


def qword():
    """rule [Q]'s word, derived in memory from REGISTRY at HEAD by its heading's digest, as the masking readers derive it; never printed."""
    L = show('HEAD', REG) or []
    hits = [l for l in L if hashlib.sha256(l.encode('utf-8')).hexdigest()[:16] == Q_DIGEST]
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', hits[0]) if len(hits) == 1 else None
    return m.group(2) if m else None


def qcount(text, w):
    return len(re.findall(r'\b%s\b' % re.escape(w), text, re.I)) if w else -1


def quoted(entry):
    para = [l for l in entry.split(NL) if l.startswith('**What the lines say.**')]
    return set(re.findall(r'"([^"]+)"', para[0])) if len(para) == 1 else None


def affected(entry):
    """the (path, line) pairs of the entry's "Record(s) affected" sentence."""
    fl = [l for l in entry.split(NL) if l.startswith('**Filed')]
    if len(fl) != 1 or 'affected: ' not in fl[0]:
        return None
    s = fl[0].split('affected: ', 1)[1].split('<', 1)[0]
    out = set()
    for piece in s.split('; '):
        m = re.match(r'\s*([\w./-]+\.md)', piece)
        if m:
            out |= set((m.group(1), int(n)) for n in re.findall(r':(\d+)', piece))
    return out


# ================================================================================ THE READ
def outputs():
    files = []
    for base, _d, fs in os.walk(os.path.join(PP, 'outputs')):
        for f in sorted(fs):
            files.append(os.path.relpath(os.path.join(base, f), PP).replace('\\', '/'))
    files.sort()
    FL = {}
    for rel in files:
        with open(os.path.join(PP, *rel.split('/')), 'rb') as f:
            FL[rel] = f.read().decode('utf-8', 'replace').replace('\r', '').split(NL)
    return files, FL


def holdings(H, files, FL):
    """{paper: {file: lines held}}, {paper: [copies]}, {(entry, k): {file: [lines holding the needle]}}."""
    held, copies = {}, {}
    for p in sorted(H):
        keys = set(l.strip() for l in H[p] if len(l.strip()) >= 40)
        held[p] = dict((rel, len(keys & set(l.strip() for l in FL[rel]))) for rel in files)
        copies[p] = [rel for rel in files if keys and held[p][rel] >= COPY_SHARE * len(keys)]
    hits = {}
    for e in ORDER:
        for k, (p, ln, nd) in enumerate(NEEDLES[e]):
            hits[(e, k)] = dict((rel, h) for rel, h in ((rel, [i + 1 for i, l in enumerate(FL[rel]) if norm(nd) in norm(l)]) for rel in files) if h)
    return held, copies, hits


def corr(cited, nd, lines, cand):
    """the copy's line for a cited line: the line whole where it stands once; else the one line holding the needle; else, among the lines
    holding it, the nearest the cited line by similarity."""
    whole = [i + 1 for i, l in enumerate(lines) if l.strip() and l.strip() == cited.strip()]
    if len(whole) == 1:
        return whole[0], 'the line whole'
    if len(cand) == 1:
        return cand[0], 'the needle alone'
    if cand:
        r = sorted(((difflib.SequenceMatcher(None, cited, lines[c - 1]).ratio(), c) for c in cand), reverse=True)
        return r[0][1], 'the nearest of %d lines holding the needle (ratio %.2f against %.2f)' % (len(cand), r[0][0], r[1][0])
    return None, 'none'


def read_all():
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    pre = jload(os.path.join(D, 'act_current.json'))['pre_pp']
    X = RU.texts(RU.ferry())
    papers = sorted(set(p for v in NEEDLES.values() for p, _l, _n in v))
    H, R0 = dict((p, show('HEAD', p)) for p in papers), dict((p, show(pre, p)) for p in papers)
    rows = []
    for e in ORDER:
        for k, (p, ln, nd) in enumerate(NEEDLES[e]):
            line = (H[p] or [])[ln - 1] if H[p] and 0 < ln <= len(H[p]) else ''
            rows.append(dict(entry=e, k=k, path=p, line=ln, needle=nd, exact=nd in line, norm=norm(nd) in norm(line)))
    filed = dict((e, all(r['exact'] for r in rows if r['entry'] == e)) for e in ORDER)
    files, FL = outputs()
    held, copies, hits = holdings(H, files, FL)
    dep_files = [r for r in files if r.startswith(DEP)]
    stray, outside, dep = [], {}, dict((e, {}) for e in ORDER)
    for e in ORDER:
        for k, (p, ln, nd) in enumerate(NEEDLES[e]):
            for rel, h in hits[(e, k)].items():
                if not rel.startswith(DEP):
                    outside.setdefault(rel, set()).add('%s :%d' % (e, ln))
                    continue
                if rel not in copies[p]:
                    stray.append((e, ln, rel))
                    continue
                cl, how = corr(H[p][ln - 1], nd, FL[rel], h)
                dep[e].setdefault(rel, []).append([p, ln, cl, how])
    theorem = any(any(x[0] == THEOREM[0] and x[1] == THEOREM[1] for x in v) for v in dep['E2'].values())
    found = dict((e, bool(dep[e])) for e in ORDER)
    same = dict((rel, [d for d in dep_files if FL[d] == FL[rel]]) for rel in outside)
    # ### the controls: the quoted phrases and the cited lines read from the entries themselves; and in the form of b764's deposit read
    qs = dict((e, (quoted(X[e][2]), set(nd for _p, _l, nd in NEEDLES[e]))) for e in ORDER)
    af = dict((e, (affected(X[e][2]), set((p, ln) for p, ln, _n in NEEDLES[e]))) for e in ORDER)
    p0, ln0, nd0 = NEEDLES['E3'][0]
    planted_line = H[p0][ln0 - 1].replace(nd0, nd0.replace('proved', 'showed'), 1)
    planted_filed = all((nd0 in planted_line) if (p, ln) == (p0, ln0) else r['exact'] for r in rows if r['entry'] == 'E3'
                        for p, ln in [(r['path'], r['line'])])
    plant_rel = DEP + '-PLANTED/R_CURVE_CRITERION.md'
    FLp = dict(FL)
    FLp[plant_rel] = list(H[RCC])
    _hp, cp, hitp = holdings(H, files + [plant_rel], FLp)
    plant_found = plant_rel in cp[RCC] and plant_rel in hitp[('E3', 0)]
    keys_rcc = set(l.strip() for l in H[RCC] if len(l.strip()) >= 40)
    gone = [l for l in H[RCC] if l.strip() not in keys_rcc]
    gone_copy = len(keys_rcc & set(l.strip() for l in gone)) >= COPY_SHARE * len(keys_rcc)
    ctl = [('the cited papers at the papers` repository`s HEAD %s each its bytes at the act`s start %s (N3): %d of %d' % (
                pp_head[:8], pre[:8], sum(1 for p in papers if H[p] and H[p] == R0[p]), len(papers)),
            all(H[p] and H[p] == R0[p] for p in papers)),
           ('each entry`s quoted phrases, read from its "What the lines say." paragraph, the needles this tool reads: %s' % (
               ' '.join('%s %s' % (e, qs[e][0] == qs[e][1]) for e in ORDER)), all(qs[e][0] == qs[e][1] for e in ORDER)),
           ('each entry`s cited lines, read from its "Records affected" sentence, the lines the needles are read at: %s' % (
               ' '.join('%s %s' % (e, af[e][0] == af[e][1]) for e in ORDER)), all(af[e][0] == af[e][1] for e in ORDER)),
           ('PLANTED: [E3]`s :%d with one word of its phrase changed reads the phrase not carried, the entry not filed (%s)' % (
               ln0, 'NOT FILED' if not planted_filed else 'FILED'), not planted_filed),
           ('PLANTED: a copy of %s under %s reads a copy of the paper holding [E3]`s phrase of :%d (%s)' % (
               RCC, plant_rel, ln0, 'FOUND' if plant_found else 'NOT FOUND'), plant_found),
           ('the paper with its lines of 40 characters or more taken out reads no copy (%s)' % ('A COPY' if gone_copy else 'NO COPY'), not gone_copy),
           ('the files under outputs/ read: %d, %d of them under a DEPOSITED folder' % (len(files), len(dep_files)), len(files) > 0 and len(dep_files) > 0),
           ('each needle held by a deposited file is held in a copy of its own paper (elsewhere %s)' % (stray or 'none'), not stray)]
    return dict(pp_head=pp_head, pre=pre, rows=rows, filed=filed, files=files, held=held, copies=copies, dep=dep, theorem=theorem,
                found=found, outside=dict((r, sorted(v)) for r, v in outside.items()), same=same, ctl=ctl,
                lines=dict((r, len(FL[r]) - 1) for r in files))


def read_route(mode):
    R = read_all()
    ok = all(o for _w, o in R['ctl'])
    P = ['%s -- (R379)(5): THE LINES [E2] TO [E5] CITE, READ FOR THEIR QUOTED PHRASES, AND outputs/ READ FOR A DEPOSITED COPY (%s)' % (ACT, utc()), '',
         '### tools/b769_errata.py read; the papers` repository at HEAD %s (the act`s start %s); the entries from the ferry bank (data/b769_ferry.txt,'
         % (R['pp_head'][:8], R['pre'][:8]),
         '### sha256 %s); each quoted phrase a needle at the line it is quoted from; each file under outputs/ by its lines, a copy of a paper where it'
         % RU.FERRY_SHA,
         '### holds %d%% of the paper`s distinct lines of 40 characters or more, deposited under %s; counts, booleans and line numbers alone.'
         % (int(COPY_SHARE * 100), DEP), '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in R['ctl']]
    P += ['', '## THE NEEDLES AT THEIR CITED LINES: entry | paper | line | the phrase | carried exactly | carried normalised']
    P += ['  %s | %s | :%d | "%s" | %s | %s' % (r['entry'], r['path'], r['line'], r['needle'], r['exact'], r['norm']) for r in R['rows']]
    P += ['', '## THE FILES UNDER outputs/: path | lines | the cited papers` lines in it (the papers by their file names), a copy marked *']
    for rel in R['files']:
        P.append('  %s | %d | %s' % (rel, R['lines'][rel], ' ; '.join('%s %d%s' % (p.split('/')[-1], R['held'][p][rel], '*' if rel in R['copies'][p] else '')
                                                                       for p in sorted(R['held']) if R['held'][p][rel])))
    P += ['', '## THE DEPOSITED COPIES HOLDING A NEEDLE: entry | copy | the cited line -> the copy`s line, the way']
    for e in ORDER:
        if not R['dep'][e]:
            P.append('  %s | none' % e)
        for rel in sorted(R['dep'][e]):
            for p, ln, cl, how in R['dep'][e][rel]:
                P.append('  %s | %s | %s :%d -> :%s, %s' % (e, rel, p.split('/')[-1], ln, cl, how))
    P += ['', '## FILES OUTSIDE THE DEPOSITED FOLDERS HOLDING A NEEDLE (a reading, no verdict): file | the needles | its lines equal to a deposited file`s']
    P += ['  %s | %s | %s' % (rel, ', '.join(v), R['same'][rel] or 'none') for rel, v in sorted(R['outside'].items())] or ['  none']
    P += ['', '## THE VERDICTS']
    for e in ORDER:
        P.append('  [%s] %s ; a deposited copy holding a quoted phrase: %s%s' % (
            e, 'FILED: each phrase carried at its line' if R['filed'][e] else 'NOT FILED: a phrase not carried', 'FOUND' if R['found'][e] else 'NONE',
            ('; holding the theorem (:%d): %s' % (THEOREM[1], 'FOUND' if R['theorem'] else 'NONE')) if e == 'E2' else ''))
    P += ['', '### ### **THE ERRATA READ: NEEDLES %d, CARRIED %d ; ENTRIES TO FILE %d OF 4 ; FILES %d, DEPOSITED %d ; DEPOSITED COPIES HOLDING A PHRASE '
          'FOR %s ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(R['rows']), sum(1 for r in R['rows'] if r['exact']), sum(R['filed'].values()), len(R['files']),
              sum(1 for r in R['files'] if r.startswith(DEP)), ', '.join('[%s]' % e for e in ORDER if R['found'][e]) or 'NONE',
              sum(1 for _w, o in R['ctl'] if o), len(R['ctl']), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(RBANK) or os.path.exists(RJSON):
        die('THE READ`S BANK STANDS ALREADY')
    I, acct, qw = RU.ids(), RU.account(), qword()
    if acct is None or qw is None or any(RU.idcount(NL.join(P), I, acct).values()) or qcount(NL.join(P), qw):
        die('AN IDENTIFIER, THE ACCOUNT OR THE [Q] WORD IN THE BANK, OR ONE OF THEM NOT READ')
    put(RBANK, NL.join(P) + NL)
    put(RJSON, json.dumps(dict(at=utc(), act=ACT, verdict='WRITTEN', pp_head=R['pp_head'], pre=R['pre'], copy_share=COPY_SHARE, deposited=DEP,
                               rows=R['rows'], filed=R['filed'], found=R['found'], theorem=R['theorem'], dep=R['dep'],
                               copies=R['copies'], outside=R['outside'], same=R['same'], files=dict((r, R['lines'][r]) for r in R['files']),
                               held=dict((p, dict((r, n) for r, n in v.items() if n)) for p, v in R['held'].items()),
                               controls=[[w, o] for w, o in R['ctl']]), ensure_ascii=False, indent=1) + NL)
    print('written data/b769_errata_read.txt and .json')
    return 0


# ================================================================================ THE LEDGERS
def clause(dep):
    """the Filed paragraph's clause where a deposited copy holds a quoted phrase: each copy named with its lines, and the words that the
    deposited file is immutable at its version."""
    parts = []
    for rel in sorted(dep):
        by = {}
        for p, ln, cl, _how in dep[rel]:
            by.setdefault(p, []).append((ln, cl))
        for p in sorted(by):
            parts.append('%s holds the phrases quoted from %s %s at its own %s' % (
                rel, p, and_list([':%d' % ln for ln, _c in by[p]]), and_list([':%d' % c for _l, c in by[p]])))
    return ('The read of outputs/ finds %s holding quoted phrases: %s; each deposited file is immutable at its version.' % (
        'a deposited copy' if len(dep) == 1 else 'deposited copies', '; '.join(parts)))


def entry(e, tpl, date, num, A):
    """the entry composed: its heading's alternative resolved by the read, its clause on a deposited copy composed or the ruling's words."""
    L = tpl.split(NL)
    hit = A['theorem'] if e == 'E2' else A['found'][e]
    if hit and e not in HEAD_FOUND:
        return None, None, None, 'a deposited copy holds a phrase of [%s]: its heading`s found branch is the seat`s to compose' % e
    label = HEAD_FOUND[e] if hit else HEAD_NONE
    h, ch, why = RU.resolve(L[0], label)
    if h is None:
        return None, None, None, why
    body = NL.join(L[1:])
    m = FILED_ALT.search(body)
    tbody = body
    if m:
        none_text = m.group(0)[1:-1].split(NONE_SEP)[1]
        c = clause(A['dep'][e]) if A['found'][e] else none_text
        body = body.replace(m.group(0), c, 1)
        tbody = tbody.replace(m.group(0), '<the clause>', 1)
    text = (h + NL + body).replace('<DATE>', date).replace('<n>', str(num))
    return text, h + NL + tbody, ch, None


def r3(tpl, filed, nums, A):
    """[R3]: the entries filed by number; its alternative resolved to "each of the four filed", or, where one is not, composed naming it
    with the line that did not carry its phrase."""
    if all(filed.values()):
        t, ch, why = RU.resolve(tpl, R3_ALL)
    else:
        miss = [(e, r['path'], r['line']) for e in ORDER if not filed[e] for r in A['rows'] if r['entry'] == e and not r['exact']]
        alts = [(s, x, inner) for s, x, inner in RU.outer(tpl) if len(RU.branches(inner)) > 1]
        if len(alts) != 1:
            return None, [], 'the alternative of [R3] not one'
        s, x, _i = alts[0]
        words = '; '.join('[%s] not filed, %s :%d not carrying its phrase' % m for m in miss)
        t, ch, why = tpl[:s] + words + tpl[x:], [words], None
    if t is None:
        return None, [], why
    return t.replace('<the entries filed, by number>', and_list(['E-%s' % nums[e] for e in ORDER if e in nums]) if nums else 'none', 1), ch, None


def compose(date, base_e, base_o, A, filed=None):
    X = RU.texts(RU.ferry())
    TP = dict((k, X[k][2]) for k in X)
    filed = dict(A['filed']) if filed is None else filed
    nums, E, TE, CH, WHY = {}, {}, {}, {}, {}
    n = 0
    for e in ORDER:
        if not filed[e]:
            continue
        n += 1
        nums[e] = '%s-%d' % (date, n)
        E[e], TE[e], CH[e], WHY[e] = entry(e, TP[e], date, n, A)
    F = dict((FACT[e], TP[FACT[e]].replace('<DATE>', date).replace('<n>', nums[e].split('-')[-1])) for e in ORDER if e in nums)
    R3, ch3, why3 = r3(TP['R3'], filed, nums, A)
    n_ot = len(base_o.split(NL)) - 1
    head = ('**Dated head, %s, b769, `(R379)`(5): the lines the ruling orders for OPEN_TRAILS at Component 3** (relay data/b769_ferry.txt :23 and '
            ':88-:153), appended at the end of the file (its last line :%d), so that no line before them moves: the fact items of the entries of '
            'ERRATA filed at this act, %s, by %s; the errors of the order of the November riders entered by [R3].' % (
                date, n_ot, and_list(['E-%s' % nums[e] for e in ORDER if e in nums]) or 'none', and_list(['[%s]' % FACT[e] for e in ORDER if e in nums]) or 'none'))
    paras = [head] + [F[FACT[e]] for e in ORDER if e in nums] + ([R3] if R3 else [])
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    ents = [E[e] for e in ORDER if e in E and E[e]]
    return dict(TP=TP, nums=nums, E=E, TE=TE, CH=CH, WHY=WHY, F=F, R3=R3, ch3=ch3, why3=why3, head=head, ot=ot, er=(NL + NL).join(ents),
                new_o=base_o + NL + ot + NL, new_e=base_e + NL + (NL + NL).join(ents) + NL, n_ot=n_ot, paras=paras)


def ledgers(mode):
    from standing import orders as O
    A = jload(RJSON)
    date = today()
    base_e, base_o = RU.at_head(ERRATA), RU.at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(date, base_e, base_o, A)
    TP, E, F = C['TP'], C['E'], C['F']
    I, acct, qw = RU.ids(), RU.account(), qword()
    app = C['er'] + NL + C['ot']
    held_dates = re.findall(r'^## E-%s-(\d+)' % re.escape(date), base_e, re.M)
    eqE = dict((e, bool(E.get(e)) and bool(re.fullmatch(RU.pattern(C['TE'][e]), E[e], re.S)) and E[e] in C['er']) for e in C['nums'])
    eqF = dict((f, bool(re.fullmatch(RU.pattern(TP[f]), F[f], re.S)) and (NL + F[f] + NL) in (NL + C['ot'] + NL)) for f in F)
    R3t = TP['R3']
    if all(A['filed'].values()):
        R3t = RU.resolve(TP['R3'], R3_ALL)[0] or TP['R3']
    eq3 = bool(C['R3']) and bool(re.fullmatch(RU.pattern(R3t), C['R3'], re.S)) and (NL + C['R3'] + NL) in (NL + C['ot'] + NL)
    subs = dict((e, bool(C['CH'].get(e)) and all(b in TP[e].split(NL)[0] for b in C['CH'][e])) for e in C['nums'])
    sub3 = bool(C['ch3']) and (not all(A['filed'].values()) or all(b in TP['R3'] for b in C['ch3']))
    labels = dict((e, ('found' if (A['theorem'] if e == 'E2' else A['found'][e]) else 'none')) for e in C['nums'])
    alts = dict((e, len(FILED_ALT.findall(TP[e]))) for e in ORDER)
    named = dict((e, all(rel in (E.get(e) or '') for rel in A['dep'][e])) for e in ('E2', 'E4'))
    left = sorted(set(RU.FIELD.findall(app)))
    ticks = [k + 1 for k, l in enumerate(app.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base_o.split(NL), C['new_o'].split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted((n, st(before, n), st(after, n)) for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    nf = sorted(set(O.NAME.findall(O.mask(' '.join(F.values()) + ' ' + C['head']))))
    n3 = sorted(set(O.NAME.findall(O.mask(C['R3'] or ''))))
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = RU.idcount(base_e + base_o, I, acct), RU.idcount(C['new_e'] + C['new_o'], I, acct), RU.idcount(app, I, acct)
    present = [k for k, v in list(E.items()) + list(F.items()) + [('R3', C['R3'] or '\0')] if v and v in (base_e + base_o)]
    # ### the planted checks, in memory alone
    pf = dict(A['filed'])
    pf['E3'] = False
    Ap = dict(A)
    Ap['rows'] = [dict(r, exact=False) if (r['entry'], r['k']) == ('E3', 0) else r for r in A['rows']]
    Cp = compose(date, base_e, base_o, Ap, filed=pf)
    p_ok = (sorted(Cp['nums']) == ['E2', 'E4', 'E5'] and Cp['nums']['E4'].endswith('-2') and Cp['nums']['E5'].endswith('-3') and 'F3' not in Cp['F']
            and bool(Cp['R3']) and '[E3] not filed' in Cp['R3'] and Cp['R3'] != C['R3'])
    An = dict(A)
    An['theorem'] = False
    h_none = entry('E2', TP['E2'], date, 1, An)[0]
    w5 = (E.get('E5') or '').replace('the paper takes the correction', 'the paper takes a correction', 1)
    w_eq = bool(re.fullmatch(RU.pattern(C['TE']['E5']), w5, re.S)) if 'E5' in C['TE'] else True
    order_name = 'W-ORD-NOVEMBER-RIDERS'
    ctl = [('the papers` repository`s HEAD the act`s last commit there before this write, [B1], [A4] and [C9] %s (%s)' % (C3PP, pp_head[:8]),
            pp_head.startswith(C3PP)),
           ('the read`s bank written at this HEAD (%s), its controls %d of %d as wanted' % (
               A.get('pp_head', '')[:8], sum(1 for _w, o in A['controls'] if o), len(A['controls'])),
            A.get('verdict') == 'WRITTEN' and A.get('pp_head') == pp_head and all(o for _w, o in A['controls'])),
           ('ERRATA`s and OPEN_TRAILS` bytes at HEAD each a prefix of its new bytes: no line moves',
            C['new_e'].startswith(base_e) and C['new_o'].startswith(base_o)),
           ('no entry of ERRATA numbered on %s before the write (%s), so the entries are numbered from 1' % (date, held_dates or 'none'), not held_dates),
           ('each entry filed where its phrases are carried, in the order [E2] to [E5]: %s' % (
               ' '.join('%s %s' % (e, ('E-' + C['nums'][e]) if e in C['nums'] else 'NOT FILED') for e in ORDER)),
            all((e in C['nums']) == A['filed'][e] for e in ORDER) and all(E.get(e) for e in C['nums'])),
           ('each heading`s alternative resolved by the read, the chosen branch a substring of the ruling`s heading: %s' % (
               ' '.join('%s %s %s' % (e, labels[e], subs[e]) for e in C['nums'])), all(subs.values()) and not any(C['WHY'].values())),
           ('the clause on a deposited copy in [E2] and [E4] alone (%s), composed from the read where a copy holds a phrase, each copy named (%s)' % (
               ' '.join('%s %d' % (e, alts[e]) for e in ORDER), ' '.join('%s %s' % (e, named[e]) for e in named)),
            alts == dict(E2=1, E3=0, E4=1, E5=0) and all(named.values())),
           ('each text as entered equals the ruling`s with its fields filled: %s ; %s ; R3 %s' % (
               ' '.join('%s %s' % (e, eqE[e]) for e in C['nums']), ' '.join('%s %s' % (f, eqF[f]) for f in sorted(F)), eq3),
            all(eqE.values()) and all(eqF.values()) and eq3 and sub3),
           ('no field left in what is appended (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after over both files, and 0 in what is appended (the account read from the relay`s '
            'remote, never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('rule [Q]`s word, derived in memory from REGISTRY by its heading`s digest and never printed, in what is appended: %d' % qcount(app, qw),
            qw is not None and qcount(app, qw) == 0),
           ('none of the texts in ERRATA or OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('the fact items and the head name no order (%s); [R3] names %s alone (%s)' % (nf or 'none', order_name, n3 or 'none'),
            not nf and n3 == [order_name]),
           ('the roster: %s %s before and %s after, no order moving and none added (moved %s ; added %s)' % (
               order_name, st(before, order_name), st(after, order_name), moved or 'none', added or 'none'),
            st(before, order_name) == 'OPEN' and not moved and not added),
           ('PLANTED: [E3] not filed (one phrase not carried, in memory) numbers [E4] -2 and [E5] -3, enters no [F3] and puts [R3] in its second form (%s)' % (
               'AS PLANTED' if p_ok else 'NOT AS PLANTED'), p_ok),
           ('PLANTED: [E2]`s heading where no deposited copy holds the theorem reads its other branch (%s)' % (
               'DIFFERS' if h_none and h_none != E.get('E2') and 'NO DEPOSITED ARTIFACT HOLDS THE PASSAGES)' in h_none.split(NL)[0] else 'NOT READ'),
            bool(h_none) and h_none != E.get('E2') and 'NO DEPOSITED ARTIFACT HOLDS THE PASSAGES)' in h_none.split(NL)[0]),
           ('PLANTED: [E5] with one literal word changed reads unequal (%s)' % ('EQUAL' if w_eq else 'UNEQUAL'), bool(w5) and not w_eq),
           ('the appended lines of OPEN_TRAILS outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand)]
    ok = all(o for _w, o in ctl)
    el, ol = C['new_e'].split(NL), nl_
    P = ['%s -- (R379)(5): THE ERRORS OF W-ORD-NOVEMBER-RIDERS ENTERED: ERRATA AND OPEN_TRAILS, EACH APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b769_errata.py ledgers; the papers` repository at HEAD %s; the texts from the ferry bank (data/b769_ferry.txt, sha256 %s); the' % (
             pp_head[:8], RU.FERRY_SHA),
         '### read from data/b769_errata_read.json (sha256 %s); <DATE> %s; each text by line and sha256 here.' % (fsha(RJSON), date), '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE FILES',
          '  ERRATA.md | lines %d -> %d | the entries from :%d | their sha256 %s | the file`s sha256 %s -> %s' % (
              len(base_e.split(NL)) - 1, len(el) - 1, len(base_e.split(NL)) + 1, sha(C['er'])[:16], sha(base_e)[:16], sha(C['new_e'])[:16]),
          '  OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
              C['n_ot'], len(ol) - 1, C['n_ot'] + 2, sha(C['ot'])[:16], sha(base_o)[:16], sha(C['new_o'])[:16])]
    P += ['', '## THE TEXTS BY LINE']
    P += ['  %-6s ERRATA :%d, E-%s (sha256 %s)' % (e, el.index(E[e].split(NL)[0]) + 1, C['nums'][e], sha(E[e])[:16]) for e in ORDER if e in C['nums']]
    P += ['  %-6s OPEN_TRAILS :%d (sha256 %s)' % (k, ol.index(v) + 1, sha(v)[:16]) for k, v in
          [('head', C['head'])] + [(FACT[e], F[FACT[e]]) for e in ORDER if e in C['nums']] + [('R3', C['R3'])]]
    P += ['', '### ### **THE LEDGERS, GROUP C3: ERRATA AND OPEN_TRAILS APPENDED, NO LINE MOVING ; ENTRIES FILED %s ; FACT ITEMS %d ; [R3] %s ; '
          'CONTROLS %d OF %d AS WANTED ; %s.**' % (
              and_list(['E-' + C['nums'][e] for e in ORDER if e in C['nums']]) or 'NONE', len(F), 'EACH OF THE FOUR FILED' if all(A['filed'].values()) else 'ONE NOT FILED',
              sum(1 for _w, o in ctl if o), len(ctl), ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE ENTRIES APPENDED TO ERRATA.md (the dry run`s print alone):')
        print(C['er'])
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(C['ot'])
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    if os.path.exists(LBANK) or os.path.exists(LJSON):
        die('THE BANK STANDS ALREADY')
    if any(RU.idcount(NL.join(P), I, acct).values()) or qcount(NL.join(P), qw):
        die('AN IDENTIFIER, THE ACCOUNT OR THE [Q] WORD IN THE BANK')
    for path, data in ((ERRATA, C['new_e']), (OT, C['new_o'])):
        with open(os.path.join(PP, path), 'wb') as f:
            f.write(data.encode('utf-8'))
        if fsha(os.path.join(PP, path)) != sha(data)[:16]:
            die('THE WRITTEN FILE %s IS NOT ITS COMPOSITION' % path)
    put(LBANK, NL.join(P) + NL)
    put(LJSON, json.dumps(dict(at=utc(), act=ACT, group='c3', date=date, pp_head=pp_head, numbers=C['nums'],
                               files=dict(ERRATA=dict(lines_before=len(base_e.split(NL)) - 1, lines_after=len(el) - 1, sha_before=sha(base_e)[:16],
                                                      sha_after=sha(C['new_e'])[:16]),
                                          OPEN_TRAILS=dict(lines_before=C['n_ot'], lines_after=len(ol) - 1, sha_before=sha(base_o)[:16],
                                                           sha_after=sha(C['new_o'])[:16])),
                               entered=dict([(e, ['ERRATA', el.index(E[e].split(NL)[0]) + 1, sha(E[e])[:16]]) for e in ORDER if e in C['nums']] +
                                            [(FACT[e], ['OPEN_TRAILS', ol.index(F[FACT[e]]) + 1, sha(F[FACT[e]])[:16]]) for e in ORDER if e in C['nums']] +
                                            [('R3', ['OPEN_TRAILS', ol.index(C['R3']) + 1, sha(C['R3'])[:16]])]),
                               head=[ol.index(C['head']) + 1, sha(C['head'])[:16]], controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written ERRATA.md and OPEN_TRAILS.md ; data/b769_ledgers_c3.txt and .json')
    return 0


def main(argv):
    if len(argv) != 2 or argv[0] not in ('read', 'ledgers') or argv[1] not in ('dry', 'write'):
        sys.exit(__doc__)
    return read_route(argv[1]) if argv[0] == 'read' else ledgers(argv[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
