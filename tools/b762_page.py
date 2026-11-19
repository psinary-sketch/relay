# -*- coding: utf-8 -*-
"""tools/b762_page.py -- (R372)(6): THE PAGE ENTERED (data/b762_ferry.txt :19). Written by the Write tool at b762's Component 4 and committed
before its first run (N2). It composes day1/ONE_PAGE_PROOF_v2_0.md (the name by (6)'s stem clause, data/b762_misses.txt (1)) from BLOCK P of
part 2 (data/b762_text.txt, the lines between NEW>> and <<NEW) and from nothing else, its one field, the line reading ‹BYLINE›, given way to
line :3 of day1/ONE_PAGE_PROOF.md by its bytes, which no tool and no bank prints; it appends [G1] and [G2] (data/b762_ferry.txt :131, :135)
at REGISTRY's end with DATE, the UTC date of the write, and [G1]'s backticked path set to the page's name, nothing else changed.

ITS CONTROLS, in (6)'s order, each printed before any write; the page is HELD at the earliest that fails, printed, and nothing is written to
PLACE-papers: the composed bytes with line :3 put back to the field's own line hash to (6)'s sha256; the deposited edition's file's sha256
before (and, at the write, after) equal; the nineteen declarations of SIDE-explicit-formula at v0.41 under SIDEExplicitFormula/ and the four
lines of SIDE-kernel at v1.5, each at the path and line the table prints, read as predicates (no kernel line printed), misses 0; the axioms
line of h2_sign_iff_rh at v0.41 read from data/b759_outcomes.txt :29 as within the standard three; 0 live banned stems by the standing sweep
(tools/banned_terms.py --new, over a copy in a temporary folder removed in the same run, its summary lines alone printed); no relay path, act
number or ruling number in the page's bytes; the body's word count, the lines between :5 and the rule, printed beside the navigator's 767 (a
word a run of non-space characters, misses (5); a printed figure, not a condition). Beside them: the page absent at HEAD and in the tree; the
file's form (LF alone, one closing LF); no identifier of the author on any line but :3 (N5); [G1] and [G2] equal to the ferry's lines with
their fields filled and REGISTRY's bytes a prefix of its new bytes, the heading of rule [Q] (3) at its line by its digest.

  control   the planted controls, printed; nothing read of line :3, nothing written
  dry       the page composed in memory and every control printed; nothing written to PLACE-papers or the relay
  write     every control; where all hold, the page and REGISTRY's two lines written, then the after-reads; the bank data/b762_page.txt and
            .json written either way (HELD names the control)
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import subject as S   # noqa: E402

NL = '\n'
ACT = 'b762'
PP = S.PP
EF_REPO = 'D:/SIDE-explicit-formula'
KN_REPO = 'D:/SIDE-kernel'
EF_TAG, KN_TAG = 'v0.41', 'v1.5'
EF_DIR = 'SIDEExplicitFormula/'
TEXT = os.path.join(D, 'b762_text.txt')
FERRY = os.path.join(D, 'b762_ferry.txt')
OUTCOMES = os.path.join(D, 'b759_outcomes.txt')
OUTCOMES_LINE = 29
PAGE = 'day1/ONE_PAGE_PROOF_v2_0.md'            # ### (6)'s stem clause (data/b762_misses.txt (1))
RULED_NAME = 'day1/ONE_PAGE_v2_0.md'            # ### the name (6) and [G1] print, which the stem clause changes
DEPOSITED = 'day1/ONE_PAGE_PROOF.md'
DEPOSITED_SHA16 = '9b4d8cdc21916c31'            # ### the deposited file's sha256 as step zero read it (data/b762_readfirst.txt)
REGISTRY = 'REGISTRY.md'
Q_LINE, Q_DIGEST = 374, '53d53060a58f6b9b'      # ### rule [Q] (3)'s heading, by its line and digest; no line of it printed
FIELD = '‹BYLINE›'
WANT_SHA = '4fdae6951f0f952718340aeb2ef86b39d49dc14e4e671c7d2e14f59e70e260ac'
NAV_WORDS = 767
WANT_DECLS = (19, 4)
G_LINES = (('[G1]', 130, 131, 132), ('[G2]', 134, 135, 136))   # ### the ferry bank's head, text and end lines of each
BANK = os.path.join(D, 'b762_page.txt')
JBANK = os.path.join(D, 'b762_page.json')
RX_RELAY = re.compile(r'(?i)\brelay\b|(?<![\w/])data/[\w./-]+|(?<![\w/])tools/[\w./-]+|\.json\b')
RX_ACT = re.compile(r'(?<![\w.])b\d{3,4}(?!\w)')
RX_RULING = re.compile(r'\(R\d{2,4}\)|(?<![\w.])R\d{3,4}(?!\w)')
RX_ACT_WIDE = re.compile(r'(?i)b\d{3,4}')
DECL_EF = r'\b(theorem|lemma|def|abbrev|structure|inductive|instance|noncomputable def)\s+(\S+\.)?%s\b'
DECL_ANY = r'\b(theorem|lemma|def|abbrev|structure|inductive|instance|noncomputable def)\s+(\S+\.)?%s\b'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.returncode, r.stdout


def block():
    """BLOCK P's lines between its markers, the text bank's line of each, and the field's index."""
    t = io.open(TEXT, encoding='utf-8', newline='').read()
    if '\r' in t:
        die('THE TEXT BANK CARRIES A CARRIAGE RETURN')
    L = t.split(NL)
    a = [i for i, l in enumerate(L) if l == 'NEW>>']
    b = [i for i, l in enumerate(L) if l == '<<NEW']
    if len(a) != 1 or len(b) != 1 or a[0] >= b[0]:
        die('BLOCK P`S MARKERS NOT ONE EACH IN ORDER (%s, %s)' % (a, b))
    lines = L[a[0] + 1:b[0]]
    return lines, a[0] + 2, b[0]


def table(lines):
    """[(name, repo, tag, path, line)] from the Correspondence table's Declaration and File-and-line cells."""
    out = []
    for l in lines:
        if not l.startswith('| ') or l.startswith('| Claim') or l.startswith('|:--'):
            continue
        cells = [c.strip() for c in l.split('|')]
        if len(cells) < 6:
            continue
        names = re.findall(r'`([^`]+)`', cells[2])
        fm = re.search(r'`([^`]+\.lean)`((?:\s*:\d+,?)+)', cells[3])
        if not names or not fm:
            continue
        nums = [int(x) for x in re.findall(r':(\d+)', fm.group(2))]
        kern = 'SIDE-kernel' in cells[3]
        if len(nums) != len(names):
            die('A ROW`S NAMES AND LINES DO NOT PAIR (%s)' % cells[2])
        for n, k in zip(names, nums):
            out.append((n, KN_REPO if kern else EF_REPO, KN_TAG if kern else EF_TAG, fm.group(1) if kern else EF_DIR + fm.group(1), k))
    return out


def decl_at(repo, tag, path, k, name, cache):
    key = (repo, tag, path)
    if key not in cache:
        rc, b = git(repo, 'show', '%s:%s' % (tag, path))
        cache[key] = b.decode('utf-8', 'replace').split(NL) if rc == 0 else None
    L = cache[key]
    if L is None:
        return False, [], 0
    short = name.split('.')[-1]
    ln = L[k - 1] if 0 < k <= len(L) else ''
    if repo == EF_REPO:
        ok = bool(re.search(DECL_EF % re.escape(short), ln))
    else:
        ok = bool(re.search(r'\b%s\b' % re.escape(short), ln))
    hits = [i for i, l in enumerate(L, 1) if re.search(DECL_ANY % re.escape(short), l)]
    return ok, hits[:3], len(L)


def byline():
    """line :3 of the deposited edition's file, by its bytes, read at HEAD and in the tree; printed nowhere."""
    rc, blob = git(PP, 'show', 'HEAD:' + DEPOSITED)
    w = open(os.path.join(PP, DEPOSITED), 'rb').read()
    bl = blob.split(b'\n')
    return (bl[2] if len(bl) > 2 else b''), w, blob, rc


def sweep(data):
    """tools/banned_terms.py --new over a copy in a temporary folder, removed in the same run; its summary lines alone."""
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, os.path.basename(PAGE))
        with open(p, 'wb') as fh:
            fh.write(data)
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'banned_terms.py'), '--new', p], capture_output=True, cwd=RELAY)
    out = r.stdout.decode('utf-8', 'replace').split(NL)
    live = [l for l in out if l.strip().startswith('live uses')]
    hits = [l for l in out if l.strip().startswith('hits found')]
    verdict = [l for l in out if l.strip().startswith('VERDICT')]
    rows = [re.match(r'^\s+\S+\s+:(\d+)\s+(.*)$', l) for l in out if re.match(r'^   \S+\s+:\d+\s', l)]
    n = int(re.search(r'(\d+)', live[0]).group(1)) if live else -1
    h = int(re.search(r'(\d+)', hits[0]).group(1)) if hits else -1
    return r.returncode, n, h, (verdict[0].split(':', 1)[1].strip() if verdict else '### NO VERDICT'), [(int(m.group(1)), m.group(2)[:60]) for m in rows if m]


def numbers(text, skip=3):
    """the relay paths, act numbers and ruling numbers in the text, by line; line :skip's hits counted and not printed."""
    out = []
    for k, l in enumerate(text.split(NL), 1):
        for nm, rx in (('relay path', RX_RELAY), ('act number', RX_ACT), ('ruling number', RX_RULING)):
            for m in rx.finditer(l):
                out.append((k, nm, '(line :%d, not printed)' % skip if k == skip else m.group(0)))
    return out


def idcount(text):
    import b762_address_scan as SC
    low = text.lower()
    I = dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())
    return dict((k, low.count(v.lower())) for k, v in I.items() if v)


def words(lines):
    """the body: the page's lines after :5 and before the rule (misses (5)); a word a run of non-space characters."""
    try:
        r = lines.index('---', 5) + 1
    except ValueError:
        return None, None, None
    body = NL.join(lines[5:r - 1])
    return len(body.split()), r, dict(en_dash_splitting=len(re.split(r'[\s\u2013\u2014]+', body.strip())),
                                      the_rule_counted=len(NL.join(lines[5:r]).split()))


def g_lines(date):
    F = io.open(FERRY, encoding='utf-8', newline='').read().split(NL)
    out = []
    for tag, h, k, e in G_LINES:
        if not (F[h - 1].startswith('---- %s for REGISTRY' % tag) and F[e - 1] == '---- end %s' % tag):
            die('THE FERRY`S %s MARKERS NOT AT :%d AND :%d' % (tag, h, e))
        src = F[k - 1]
        got = src.replace('<DATE>', date)
        if tag == '[G1]':
            if got.count('`%s`' % RULED_NAME) != 1:
                die('[G1] DOES NOT CARRY THE RULED NAME ONCE')
            got = got.replace('`%s`' % RULED_NAME, '`%s`' % PAGE)
        out.append((tag, k, src, got))
    return out


def g_reversed(src, got, date):
    """the filled line with its fields put back equals the ferry's line: nothing else changed."""
    return got.replace('`%s`' % PAGE, '`%s`' % RULED_NAME).replace(date, '<DATE>', 1) == src and src.count('<DATE>') == 1


def planted():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (P%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    lines, _a, _b = block()
    plant = list(lines)
    plant[0] = plant[0] + ' '
    c('a page one byte off BLOCK P hashes otherwise', sha((NL.join(plant) + NL).encode('utf-8'))[:16], sha((NL.join(plant) + NL).encode('utf-8')) != WANT_SHA)
    rc, n, h, v, rows = sweep(('a ga' + 'p remains in a planted line' + NL).encode('utf-8'))
    c('the standing sweep over a planted live stem reads it', (rc, n, h, v), n == 1 and v == 'NOT CLEAN')
    pl = 'see data/b762_events.txt at b762 under (R372) and R371\n`B321.b321_identity`, `B321.classK` and the relay'
    got = [(k, nm, s) for k, nm, s in numbers(pl, skip=0)]
    c('planted relay path, act numbers and ruling numbers read; Lean names under B321 do not', got,
      sorted(nm for _k, nm, _s in got) == ['act number', 'relay path', 'relay path', 'ruling number', 'ruling number'] and all('B321' not in s for _k, _nm, s in got))
    cache = {}
    T_ = table(lines)
    n0, r0, t0, p0, k0 = T_[0]
    good = decl_at(r0, t0, p0, k0, n0, cache)[0]
    bad = decl_at(r0, t0, p0, k0 + 1, n0, cache)[0]
    c('a declaration read at its line, and one line off reads a miss', (n0, good, bad), good and not bad)
    date = time.strftime('%Y-%m-%d', time.gmtime())
    G = g_lines(date)
    rev = [g_reversed(s, g, date) for _t, _k, s, g in G]
    badg = g_reversed(G[0][2], G[0][3] + ' planted', date)
    c('[G1] and [G2] filled read back to the ferry`s lines; a planted change does not', (rev, badg), all(rev) and not badg)
    c('BLOCK P`s field line once, the page`s line :3', (lines.count(FIELD), lines.index(FIELD) + 1 if FIELD in lines else None),
      lines.count(FIELD) == 1 and lines.index(FIELD) == 2)
    return L, ok


def compose():
    t0 = time.time()
    at = utc()
    date = at[:10]
    L, ok, first = [], [], []

    def c(what, got, want, cond=True):
        ok.append(bool(want) if cond else True)
        if cond and not want and not first:
            first.append((len(ok), what))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, ('AS WANTED' if want else 'NOT AS WANTED') if cond else 'PRINTED'))

    lines, a, b = block()
    bl, wdep, blob, rc = byline()
    head = git(PP, 'rev-parse', 'HEAD')[1].decode().strip()
    tree = set(git(PP, 'ls-tree', '-r', '--name-only', 'HEAD')[1].decode('utf-8', 'replace').split(NL))
    # ### the composition: BLOCK P's lines, its one field given way to the byline's bytes
    fi = lines.index(FIELD) if lines.count(FIELD) == 1 else -1
    put_back = (NL.join(lines) + NL).encode('utf-8')
    parts = [l.encode('utf-8') for l in lines]
    if fi >= 0:
        parts[fi] = bl
    page = b'\n'.join(parts) + b'\n'
    ptext = page.decode('utf-8', 'replace')
    plines = ptext.split(NL)[:-1]
    # ### (6)'s controls, in its order
    c('the composed bytes with line :3 put back to the field`s own line, sha256 against (6)`s', sha(put_back)[:16] + '...',
      fi == 2 and sha(put_back) == WANT_SHA and page.replace(bl, FIELD.encode('utf-8'), 1) == put_back)
    dsha = sha(wdep)
    c('the deposited edition`s file %s, its sha256 before (in the tree, at HEAD, as step zero read it)' % DEPOSITED,
      '%s... ; equal at HEAD %s' % (dsha[:16], wdep == blob), dsha[:16] == DEPOSITED_SHA16 and wdep == blob and rc == 0)
    T_ = table(lines)
    cache, miss, rows = {}, 0, []
    for n, repo, tag, path, k in T_:
        okd, hits, nl = decl_at(repo, tag, path, k, n, cache)
        miss += 0 if okd else 1
        rows.append('      %s %s %-45s %s :%-4d %s (declared at %s ; file lines %d)' % (
            os.path.basename(repo), tag, n, path, k, 'AT THE LINE' if okd else '### MISS', hits, nl))
    nef = sum(1 for r in T_ if r[1] == EF_REPO)
    nkn = sum(1 for r in T_ if r[1] == KN_REPO)
    c('the table`s declarations, %d of SIDE-explicit-formula at %s under %s and %d lines of SIDE-kernel at %s, each at the path and line the table prints (predicates; no kernel line printed)' % (
        nef, EF_TAG, EF_DIR, nkn, KN_TAG), 'misses %d' % miss, (nef, nkn) == WANT_DECLS and miss == 0)
    L.extend(rows)
    ol = io.open(OUTCOMES, encoding='utf-8').read().split(NL)
    oline = ol[OUTCOMES_LINE - 1] if len(ol) >= OUTCOMES_LINE else ''
    c('the axioms line of h2_sign_iff_rh at %s, data/b759_outcomes.txt :%d' % (EF_TAG, OUTCOMES_LINE), oline.strip(),
      bool(re.search(r'\bB321\.h2_sign_iff_rh: \[propext, Classical\.choice, Quot\.sound\] -> WITHIN THE STANDARD THREE$', oline.rstrip())))
    src, n, h, v, srows = sweep(page)
    c('the standing sweep, tools/banned_terms.py --new over a copy of the page in a temporary folder (removed): live uses', '%d ; hits %d ; VERDICT %s%s' % (
        n, h, v, (' ; hits by line ' + ', '.join(':%d %s' % (k, '(line :3)' if k == 3 else cl) for k, cl in srows)) if srows else ''), n == 0 and v == 'CLEAN')
    nums = numbers(ptext)
    wide = [m.group(0) for k, l in enumerate(plines, 1) if k != 3 for m in RX_ACT_WIDE.finditer(l)]
    c('no relay path, act number or ruling number in the page`s bytes', '%d%s ; the wider shape (b and digits anywhere, case ignored, line :3 apart) %d: %s' % (
        len(nums), (' -- ' + '; '.join(':%d %s %s' % x for x in nums)) if nums else '', len(wide), ', '.join(sorted(set(wide))) or 'none'), not nums)
    wc, rule, alt = words(plines)
    c('the body`s word count, the lines between :5 and the rule (the rule at :%s), a word a run of non-space characters (misses (5))' % rule,
      '%s ; the navigator`s %d ; the readings that give %d: %s' % (wc, NAV_WORDS, NAV_WORDS, ', '.join('%s %d' % kv for kv in sorted(alt.items())) if alt else 'none'),
      wc is not None, cond=False)
    # ### beside (6)'s
    c('the page absent at HEAD and in the tree before the write', (PAGE in tree, os.path.exists(os.path.join(PP, PAGE))),
      PAGE not in tree and not os.path.exists(os.path.join(PP, PAGE)))
    c('the page`s form: LF alone, one closing LF, its lines BLOCK P`s', 'CR %d ; ends %s ; lines %d against %d' % (
        page.count(b'\r'), 'one LF' if page.endswith(b'\n') and not page.endswith(b'\n\n') else 'otherwise', page.count(b'\n'), len(lines)),
      b'\r' not in page and page.endswith(b'\n') and not page.endswith(b'\n\n') and page.count(b'\n') == len(lines) and b'\r' not in bl and bl.strip() != b'')
    ids = idcount(NL.join(l for k, l in enumerate(plines, 1) if k != 3))
    c('no identifier of the author on any line of the page but :3 (N5; line :3 read by predicate alone)', ids, not any(ids.values()))
    G = g_lines(date)
    reg_w = open(os.path.join(PP, REGISTRY), 'rb').read()
    reg_b = git(PP, 'show', 'HEAD:' + REGISTRY)[1]
    add = ('\n' + G[0][3] + '\n\n' + G[1][3] + '\n').encode('utf-8')
    new_reg = reg_w + add
    rl = new_reg.decode('utf-8').split(NL)
    qd = sha(rl[Q_LINE - 1].encode('utf-8'))[:16] if len(rl) >= Q_LINE else ''
    c('[G1] and [G2] for REGISTRY`s end: each the ferry`s line with DATE %s and [G1]`s path the page`s, nothing else changed; REGISTRY in the tree equal at HEAD, ending in LF, its bytes a prefix of its new bytes, rule [Q] (3)`s heading at :%d by its digest' % (date, Q_LINE),
      'read back %s ; equal at HEAD %s ; ends LF %s ; prefix %s ; :%d digest %s ; lines %d -> %d' % (
          [g_reversed(s, g, date) for _t, _k, s, g in G], reg_w == reg_b, reg_w.endswith(b'\n'), new_reg.startswith(reg_w), Q_LINE, qd,
          reg_w.count(b'\n'), new_reg.count(b'\n')),
      all(g_reversed(s, g, date) for _t, _k, s, g in G) and reg_w == reg_b and reg_w.endswith(b'\n') and new_reg.startswith(reg_w) and qd == Q_DIGEST)
    allok = all(ok)
    ndecl = len(T_)
    sentence = ("One Page stands at v2.0 beside the deposited edition's file, which is unedited: it states the criterion as compiled in both directions, "
                "its instance at each primitive Dirichlet character, three equivalent forms, the control at discriminant -23 with what the control lacks on the "
                "prime side, and how the enumeration located the inequality; its Correspondence names %d declarations at SIDE-explicit-formula v0.41 and "
                "SIDE-kernel v1.5, misses %d; it carries no record of its edition; nothing deposited." % (ndecl, miss))   # ### (6)'s words, its fields filled
    held = ('The re-cut of One Page is held at control (%d) (%s); nothing of it is written to PLACE-papers.' % first[0]) if first else None
    secs = time.time() - t0
    return dict(at=at, date=date, head=head, lines=lines, a=a, b=b, page=page, put_back=put_back, L=L, ok=ok, allok=allok, first=first,
                sentence=sentence, held=held, G=G, add=add, reg_w=reg_w, new_reg=new_reg, wc=wc, alt=alt, ndecl=ndecl, miss=miss,
                dsha=dsha, secs=secs, sweep=(n, h, v), nums=len(nums), ids=ids)


def report(R, after=None):
    written = after is not None and all(x.endswith('-> AS WANTED') for x in after)
    out = ['%s -- (R372)(6): THE PAGE ENTERED, ITS CONTROLS PRINTED BEFORE ITS COMMIT (%s)' % (ACT, R['at']), '',
           '### PLACE-papers HEAD %s; the page %s (by (6)`s stem clause, data/b762_misses.txt (1)), composed from BLOCK P (data/b762_text.txt :%d-:%d)' % (
               R['head'][:8], PAGE, R['a'], R['b']),
           '### and from nothing else, its line :3 the deposited edition`s line :3 by its bytes, printed by no tool and no bank. No line of the page is',
           '### printed here: the page is read by its digest, its counts and its controls. REGISTRY takes [G1] and [G2] at its end.', '',
           '## THE CONTROLS'] + R['L'] + ['']
    if after is not None:
        out += ['## THE WRITE AND THE AFTER-READS'] + after + ['']
    out += ['## [G1] AND [G2] AS ENTERED AT REGISTRY`S END'] + ['  %s (data/b762_ferry.txt :%d): %s' % (t, k, g) for t, k, _s, g in R['G']] + ['']
    out += ['## THE SENTENCE', '  ' + (R['sentence'] if R['allok'] and (after is None or written) else (R['held'] or 'HELD AFTER THE WRITE'))]
    page_sha = sha(R['page'])
    state = ('HELD AT (%d)' % R['first'][0][0]) if R['first'] else ('COMPOSED, NOT WRITTEN' if after is None else ('ENTERED' if written else 'HELD AFTER THE WRITE'))
    foot = '### ### **THE PAGE: %s ; %d BYTES, %d LINES, sha256 %s ; BLOCK P PUT BACK %s ; DECLARATIONS %d, MISSES %d ; SWEEP LIVE %d ; NUMBERS %d ; WORDS %s (THE NAVIGATOR`S %d) ; CONTROLS %d OF %d AS WANTED ; %.1f s.**' % (
        state, len(R['page']), R['page'].count(b'\n'), page_sha[:16],
        sha(R['put_back'])[:16], R['ndecl'], R['miss'], R['sweep'][0], R['nums'], R['wc'], NAV_WORDS, sum(R['ok']), len(R['ok']), R['secs'])
    return NL.join(out + ['', foot]) + NL


def put(path, data):
    tmp = os.path.join(os.path.dirname(path), '.%s.tmp' % os.path.basename(path))
    with open(tmp, 'wb') as fh:
        fh.write(data)
    os.replace(tmp, path)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L, ok = planted()
        print(NL.join(L))
        print('### ### **THE PAGE TOOL`S PLANTED CONTROLS: %d OF %d AS WANTED.**' % (sum(ok), len(ok)))
        sys.exit(0 if all(ok) else 2)
    elif a[:1] in (['dry'], ['write']):
        if a[:1] == ['write'] and (os.path.exists(os.path.join(PP, PAGE)) or os.path.exists(BANK)):
            die('THE PAGE OR ITS BANK STANDS ALREADY: A SECOND WRITE IS REFUSED')
        PL, pok = planted()
        print(NL.join(['## THE PLANTED CONTROLS'] + PL + ['']))
        if not all(pok):
            die('THE PLANTED CONTROLS NOT AS WANTED')
        R = compose()
        if a[:1] == ['dry']:
            print(report(R))
            sys.exit(0 if R['allok'] else 2)
        after = None
        if R['allok']:
            put(os.path.join(PP, PAGE), R['page'])
            put(os.path.join(PP, REGISTRY), R['new_reg'])
            pw = open(os.path.join(PP, PAGE), 'rb').read()
            rw = open(os.path.join(PP, REGISTRY), 'rb').read()
            dw = open(os.path.join(PP, DEPOSITED), 'rb').read()
            after = ['  (A1) the page read back from the tree equal to the composed bytes: %s -> %s' % (pw == R['page'], 'AS WANTED' if pw == R['page'] else 'NOT AS WANTED'),
                     '  (A2) REGISTRY read back equal to its old bytes and the two lines: %s -> %s' % (rw == R['new_reg'], 'AS WANTED' if rw == R['new_reg'] else 'NOT AS WANTED'),
                     '  (A3) the deposited edition`s file`s sha256 after, equal to before: %s... -> %s' % (sha(dw)[:16], 'AS WANTED' if sha(dw) == R['dsha'] else 'NOT AS WANTED')]
            if not all(x.endswith('-> AS WANTED') for x in after):
                os.remove(os.path.join(PP, PAGE))
                put(os.path.join(PP, REGISTRY), R['reg_w'])
                after.append('  ### AN AFTER-READ NOT AS WANTED: the page removed and REGISTRY restored to its old bytes; HELD')
        text = report(R, after)
        print(text)
        j = dict(at=R['at'], act=ACT, head=R['head'], page=PAGE, page_bytes=len(R['page']), page_lines=R['page'].count(b'\n'), page_sha256=sha(R['page']),
                 put_back_sha256=sha(R['put_back']), deposited_sha256=R['dsha'], declarations=R['ndecl'], misses=R['miss'], sweep=R['sweep'], numbers=R['nums'],
                 words=R['wc'], words_navigator=NAV_WORDS, words_other_readings=R['alt'], ids_outside_line_3=R['ids'],
                 controls=dict(ok=sum(R['ok']), of=len(R['ok'])), first_failing=R['first'], written=after is not None and all(x.endswith('-> AS WANTED') for x in after),
                 g=[[t, k, g] for t, k, _s, g in R['G']], registry_before_sha256=sha(R['reg_w']), registry_after_sha256=sha(R['new_reg']) if after else None,
                 sentence=R['sentence'] if (after and all(x.endswith('-> AS WANTED') for x in after)) else (R['held'] or 'HELD AFTER THE WRITE'))
        js = json.dumps(j, ensure_ascii=False, indent=1)
        if any(idcount(text + js).values()):
            die('AN IDENTIFIER IN THE BANK')
        put(BANK, text.encode('utf-8'))
        put(JBANK, (js + NL).encode('utf-8'))
        print('written data/b762_page.txt (%d bytes, sha256 %s) and data/b762_page.json%s' % (
            len(text.encode('utf-8')), sha(text.encode('utf-8'))[:16], '' if j['written'] else ' ; ### HELD: nothing written to PLACE-papers'))
        sys.exit(0 if j['written'] else 3)
    else:
        sys.exit(__doc__)
