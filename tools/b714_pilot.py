# -*- coding: utf-8 -*-
"""b714_pilot.py -- THE PILOT, on the author's word (data/b714_author_words_preseal.txt (2)): it reads the record and changes nothing in it,
runs beside the homebrew systems (which stay primary), gates nothing, replaces no arm, tool or bank, moves no score; it writes one bank,
data/b714_pilot.txt, and nothing else.

  (P1) A DECLARATION-EXISTENCE CHECK, the source-level stand-in for checkdecls: for the seven keystones on PLACE-papers main, every Lean name
       each Correspondence section cites, with its repository and pin as the section states them, looked up by git grep for its declaration
       in the local clone at that pin -- FOUND / MISSING / NO PIN STATED, with file and line; beside it the census row or the faces-ledger
       row that grades it, by path and line; a difference between the two readings entered as a finding for the navigator (the homebrew
       reading stands). The compiled-environment check (the runner) priced, not run.
  (P2) A PROSE-LINT TRIAL over the seven: the writing law's stems by the corpus's own matcher (tools/banned_terms.py PAT and classify) and the
       frontdoor patterns, each hit with file, line and sentence, AS DESIGNED (a quotation, a refuted claim named as refuted, a
       bibliography title) or FOR THE AUTHOR; Vale's install and a style priced.
  (P3) THE PRICE OF A BLUEPRINT for the reduction chain alone, nothing built.

### THE SEVEN: the Day-1 companions as relay tools/b703_checks.py :102-:112 names them ("the monograph, the companions"), the day1 papers on
### main less the monograph A_Place_to_Stand -- Silence_of_Foundations (after the merge, a86c9429) and six others. The seat's reading of
### "the other six keystones", printed in the bank for the navigator.
### Routes: `bank [dry]`. Written by the Write tool at b714. Run as `python -X utf8` (it imports tools/banned_terms.py). It runs git
### read commands only (grep, rev-parse, show, diff) and writes data/b714_pilot.txt alone.
"""
import ctypes
import hashlib
import io
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
ACT = 'b714'
OUT = os.path.join(D, 'b714_pilot.txt')
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import banned_terms as BT          # noqa: E402  ### the corpus's own matcher, read, never copied

SEVEN = ['day1/Silence_of_Foundations.md', 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md',
         'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md', 'day1/Which_Structure_Confines.md']
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'
LEDGER = 'FACES_LEDGER.md'
SURROUND = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'
FRONTDOOR = ['RH proof', 'RH proved', 'proof of RH', 'proof of the Riemann', 'proves the Riemann', 'proving the Riemann',
             'Riemann Hypothesis is true', 'two-leg proof', 'The proof enumerates', 'SIDE proof']
GRADE = re.compile(r'\b(T0|T1-lit|T1|T2-INTERFACES|T2|T3|T4|COMPILED|PROVED|KERNEL|NAMED-ONLY|NAMED|NOT COMPILED|MANUSCRIPT-RESIDENT|HELD|'
                   r'IMPORTED|MEASURED|LIVE|DEPOSITED)\b')
PRESENT = {'T0', 'T1-lit', 'T1', 'T2-INTERFACES', 'T2', 'COMPILED', 'PROVED', 'KERNEL'}
ABSENT = {'T4', 'NAMED-ONLY', 'NOT COMPILED', 'MANUSCRIPT-RESIDENT'}
### POSIX ERE (git grep -E): `\w` and `\s` inside a bracket are literal there, so the classes are spelled out (the first dry run's C4).
DECL = (r"^[[:space:]]*(@\[[^]]*\][[:space:]]*)*((private|protected|noncomputable|partial|unsafe|nonrec)[[:space:]]+)*"
        r"(theorem|lemma|def|abbrev|structure|class|instance|inductive|axiom|opaque)[[:space:]]+([A-Za-z0-9_'.]*\.)?%s([[:space:]]|$|:|\(|\{|\[)")
FIELD = r"^[[:space:]]+%s[[:space:]]*:"
META = 'D:/SIDE-meta'
### (P2)'s FOR THE AUTHOR hits as the seat read them by the Read tool after the second dry run (07:08Z); a note beside the matcher's class
HAND = {
    ('Silence_of_Foundations.md', 218, 'blindness'): 'an era annotation recording the corpus`s repair of the old term to SILENCE, the old term '
        'named as replaced (the paper itself classes the residual PROVENANCE-QUOTATION); banned_terms.classify returns None on it',
    ('Exhaustive_Enumeration.md', 92, 'gaps'): 'a live use, in the paper`s history of the classification of finite simple groups',
    ('ONE_PAGE_PROOF.md', 1, 'proof of the riemann'): 'the document`s own title, a live frontdoor wording; for the author',
    ('Spectral_Inertness.md', 191, 'blind'): 'a register note naming the old word as replaced by *silent* (as Silence :218)',
    ('Third_Identity_Element.md', 78, 'gap'): 'a live use in its arithmetic sense (the distance from 4 to 8 in a chain of integers)',
}
SHA = re.compile(r'^[0-9a-f]{7,40}$')
VER = re.compile(r'^v\d+(\.\d+)*$')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def free_mb():
    class M(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('load', ctypes.c_ulong), ('tot', ctypes.c_ulonglong), ('avail', ctypes.c_ulonglong),
                    ('tp', ctypes.c_ulonglong), ('ap', ctypes.c_ulonglong), ('tv', ctypes.c_ulonglong), ('av', ctypes.c_ulonglong),
                    ('ae', ctypes.c_ulonglong)]
    m = M()
    m.l = ctypes.sizeof(M)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.avail // (1 << 20)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout


def rev_of(repo, pin):
    rc, out = git(repo, 'rev-parse', '--verify', '--quiet', pin + '^{commit}')
    return out.strip() if rc == 0 else None


def lookup(repo, rev, name):
    """(file, line, kind) of the declaration of name's last component at rev, or None; a structure field read second."""
    last = name.split('.')[-1]
    esc = re.escape(last)
    for pat, kind in ((DECL % esc, 'decl'), (FIELD % esc, 'field')):
        rc, out = git(repo, 'grep', '-n', '-E', pat, rev, '--', '*.lean')
        hits = [l for l in out.split(NL) if l.strip()]
        if hits:
            p = hits[0].split(':', 3)        # rev:path:line:text
            return p[1], int(p[2]), kind, len(hits)
    return None


def is_lean_name(t):
    ### ASCII only (C¹_ℚ and its kin are notation), and no ALL-CAPS document name (THE_CARRIER_BUILD and its kin)
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*(\.[A-Za-z_][A-Za-z0-9_']*)*", t):
        return False
    if t.upper() == t:
        return False
    if VER.match(t) or SHA.match(t) or t.lower().endswith(('.md', '.lean', '.py', '.txt', '.json')):
        return False
    if t in ('main', 'h2', 'RH', 'VERIFY', 'NONE'):
        return False
    return '_' in t or '.' in t or re.search(r'[a-z][A-Z]', t) is not None or (t[0].isupper() and len(t) >= 6 and not t.isupper())


def sections(lines):
    hs = [(i + 1, len(m.group(1)), m.group(2)) for i, l in enumerate(lines) for m in [re.match(r'^(#{1,6}) +(.*)$', l)] if m]
    out = []
    for k, (s, lv, t) in enumerate(hs):
        e = next((s2 - 1 for s2, lv2, _t in hs[k + 1:] if lv2 <= lv), len(lines))
        out.append((s, e, lv, t))
    return out


def corr_section(lines):
    secs = [x for x in sections(lines) if 'correspondence' in x[3].lower() and x[2] <= 2]
    return secs[0] if secs else None


def row_pins(kernel, terminal):
    """the pins a table row states: its terminal cell's own `at vX = sha` first, else the kernel cell's DEPOSIT-PIN / WORKING-HEAD / tag."""
    own = re.findall(r'at `(v[\d.]+)` = `([0-9a-f]{7,40})`', terminal)
    if own:
        return [('%s = %s' % (v, s), s) for v, s in own]
    pins = []
    for lab, v, s in re.findall(r'(DEPOSIT-PIN|WORKING-HEAD) `(v[\d.]+)` = `([0-9a-f]{7,40})`', kernel):
        pins.append(('%s %s = %s' % (lab, v, s), s))
    for s in re.findall(r'WORKING-HEAD `([0-9a-f]{7,40})`', kernel):
        pins.append(('WORKING-HEAD %s' % s, s))
    if not pins:
        for v in re.findall(r'tag `(v[\d.]+)`', kernel):
            pins.append(('tag %s' % v, v))
    return pins


def tier_pins(terminal):
    """a tiered row's pins, written after `·` in its terminal cell: `SIDE-x vN[ = `sha`]`, one or more repositories."""
    tail = terminal.split('·', 1)[1] if '·' in terminal else ''
    return [(r, '%s%s' % (v, ' = %s' % s if s else ''), s or v) for r, v, s in
            re.findall(r'(SIDE-[A-Za-z0-9-]+) (v\d+(?:\.\d+)*)(?: = `([0-9a-f]{7,40})`)?', tail)]


def extract(path, text_lines, tiered=False):
    """[(line, name, [(repo, label, rev)], where, status or tier)] for the document's Correspondence section (or, tiered, its
    "Correspondence, tiered" table's rows `| :N | claim | terminal · pin | tier | ...`), and the yield counts."""
    if tiered:
        secs = [x for x in sections(text_lines) if 'correspondence, tiered' in x[3].lower()]
        sec = secs[0] if secs else None
    else:
        sec = corr_section(text_lines)
    if sec is None:
        return None, [], dict(rows=0, prose=0, tokens=0, names=0)
    s, e, _lv, _t = sec
    out, y = [], dict(rows=0, prose=0, tokens=0, names=0)
    prev = []                       ### a kernel cell reading `same` takes the row above's pins (Seven_Mechanism_Classes :280)
    for i in range(s, e + 1):
        l = text_lines[i - 1]
        if not l.startswith('|') and tiered:
            continue                ### the tiered table's rows alone, not its preamble's prose
        if l.startswith('|'):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if tiered:
                if len(cells) < 7 or not re.fullmatch(r':\d+', cells[0]):
                    continue
                y['rows'] += 1
                pins, term, status = tier_pins(cells[2]), cells[2].split('·', 1)[0], cells[3].replace('*', '').strip()
            else:
                if len(cells) < 6 or set(cells[0]) <= set(':-') or cells[0] == 'claim':
                    continue
                y['rows'] += 1
                repo = (re.findall(r'(SIDE-[A-Za-z0-9-]+)', cells[1]) or [None])[0]
                pins = [(repo, lab, rev) for lab, rev in row_pins(cells[1], cells[2])] if repo else []
                if cells[1].lower() == 'same':
                    pins = prev
                prev = pins
                term, status = cells[2], ' '.join(sorted(set(GRADE.findall(cells[4]))))
            for tok in re.findall(r'`([^`]+)`', term):
                y['tokens'] += 1
                if is_lean_name(tok):
                    y['names'] += 1
                    out.append((i, tok, pins, 'table', status))
        else:
            toks = [(m.start(), m.group(1)) for m in re.finditer(r'`([^`]+)`', l)]
            if not toks:
                continue
            y['prose'] += 1
            repos = [(m.start(), m.group(1), m.group(2), m.group(3)) for m in
                     re.finditer(r'(SIDE-[A-Za-z0-9-]+)[ ,]+`?(v\d+(?:\.\d+)*)`?(?:\s*(?:=|\()\s*`?([0-9a-f]{7,40})`?)?', l)]
            for at, tok in toks:
                y['tokens'] += 1
                if not is_lean_name(tok):
                    continue
                y['names'] += 1
                pre = [r for r in repos if r[0] < at]
                if pre:
                    _a, repo, v, sh = pre[-1]
                    out.append((i, tok, [(repo, '%s%s' % (v, ' = %s' % sh if sh else ''), sh or v)], 'prose', ''))
                else:
                    out.append((i, tok, [], 'prose', ''))
    return sec, out, y


def check(name, pins):
    """the name at each stated (repo, pin): ('FOUND' | 'MISSING' | 'MIXED' | 'PINABSENT' | 'NOPIN', the cells). A row naming several
    repositories is FOUND where one of them carries it at all its pins; one repository's pins disagreeing is MIXED."""
    if not pins:
        return 'NOPIN', ''
    res, by = [], {}
    for repo, lab, pin in pins:
        clone = 'D:/' + repo
        rev = rev_of(clone, pin) if os.path.isdir(clone) else None
        h = lookup(clone, rev, name) if rev else None
        s = 'PIN ABSENT LOCALLY' if rev is None else ('FOUND' if h else 'MISSING')
        res.append((repo, lab, s, h))
        by.setdefault(repo, set()).add(s)
    allst = set(r[2] for r in res)
    if any(v == {'FOUND'} for v in by.values()):
        st = 'FOUND'
    elif allst == {'MISSING'}:
        st = 'MISSING'
    elif allst == {'PIN ABSENT LOCALLY'}:
        st = 'PINABSENT'
    else:
        st = 'MIXED'
    return st, ' ; '.join('%s %s: %s' % (repo, lab, ('%s %s:%d (%s)' % (s, h[0], h[1], h[2])) if h else s) for repo, lab, s, h in res)


def homebrew(name, census, ledger):
    """the census row and the faces-ledger row naming the declaration, each by path:line with its grade tokens: the first table row
    (a line opening `|`) that names it, else the first line that does."""
    last = name.split('.')[-1]
    rx = re.compile(r'(?<![\w.])(?:[\w]+\.)*%s(?![\w\'])' % re.escape(last))
    rows = []
    for rel, ls in ((CENSUS, census), (LEDGER, ledger)):
        hit = [(j, l) for j, l in enumerate(ls, 1) if rx.search(l)]
        pick = next(((j, l) for j, l in hit if l.lstrip().startswith('|')), hit[0] if hit else None)
        if pick:
            rows.append((rel, pick[0], sorted(set(GRADE.findall(pick[1])))))
    return rows


def meta_lookup(name):
    """a MISSING name looked up in SIDE-meta (whose description names a parametric SIDESystem template) at each tag and HEAD."""
    if not os.path.isdir(META):
        return 'SIDE-meta NOT CLONED LOCALLY'
    revs = [t for t in git(META, 'tag', '--sort=creatordate')[1].split(NL) if t.strip()] + ['HEAD']
    res = []
    for r in revs:
        h = lookup(META, r, name)
        res.append('%s (%s): %s' % (r, git(META, 'rev-parse', '--short', r + '^{commit}')[1].strip(),
                                    ('FOUND %s:%d (%s)' % (h[0], h[1], h[2])) if h else 'MISSING'))
    return ' ; '.join(res)


def lint(path, lines):
    """(P2): every banned-stem hit and every frontdoor hit with its line, the sentence about it, the class and the reason."""
    refs = [x for x in sections(lines) if x[3].strip().lower().startswith('references') and x[2] <= 2]
    in_refs = lambda i: any(s <= i <= e for s, e, _l, _t in refs)   # noqa: E731
    hits = []
    for i, l in enumerate(lines, 1):
        for m in BT.PAT.finditer(l):
            c = BT.classify(l, m.start(), path)
            hits.append(dict(line=i, kind='STEM', what=m.group(0), sent=_sent(l, m.start()),
                             cls='AS DESIGNED' if c else 'FOR THE AUTHOR', why=c or 'a live use (classify None)'))
        for p in FRONTDOOR:
            for m in re.finditer(re.escape(p), l, re.I):
                sent = _sent(l, m.start())
                why = None
                if in_refs(i):
                    why = 'a bibliography title (the References section)'
                elif l.lstrip().startswith('>') or _quoted(l, m.start()):
                    why = 'a quotation'
                elif re.search(r'refut|not supportable|unsupportable|false|not proved|no proof|withdrawn|retract|struck|retired|does not prove|'
                               r'is not a proof|not a proof|never|no claim', sent, re.I):
                    why = 'a refuted claim named as refuted'
                hits.append(dict(line=i, kind='FRONTDOOR', what=m.group(0), sent=sent, cls='AS DESIGNED' if why else 'FOR THE AUTHOR',
                                 why=why or 'none of the three'))
    return hits


def _sent(l, at):
    a = max(l.rfind('. ', 0, at), l.rfind('; ', 0, at))
    a = 0 if a < 0 else a + 2           ### no break before the hit: the line's start (the first dry run began at 1, C5)
    b = min([p for p in (l.find('. ', at), l.find('; ', at)) if p >= 0] or [len(l)])
    return l[a:b + 1].strip()[:240]


def _quoted(l, at):
    for o, c in (('\u201c', '\u201d'), ('"', '"'), ('*"', '"*')):
        left = l.rfind(o, 0, at)
        if left >= 0 and l.find(c, at) > left:
            return True
    return False


def controls(L):
    ok = []
    ef = 'D:/SIDE-explicit-formula'
    pos = lookup(ef, '38e2734', 'h2_sign_iff_rh')
    ok.append(bool(pos) and pos[0].endswith('Seam.lean') and pos[1] == 101)
    L.append('  (C1) POS `h2_sign_iff_rh` at SIDE-explicit-formula 38e2734 (v0.37): %s -- %s' % (pos, 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    neg = lookup(ef, '38e2734', 'h2_sign_iff_rh_not_a_declaration')
    ok.append(neg is None)
    L.append('  (C2) NEG an absent name at the same pin: %s -- %s' % (neg, 'MISSING AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    early = lookup(ef, '5c72cad', 'h2_sign_sum_iff_rh')
    late = lookup(ef, '38e2734', 'h2_sign_sum_iff_rh')
    ok.append(early is None and bool(late))
    L.append('  (C3) THE PIN READ: `h2_sign_sum_iff_rh` (entered at v0.36, the faces page :174) MISSING at v0.2 = 5c72cad: %s ; FOUND at v0.37: %s -- %s' % (
        early is None, late, 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    fld = lookup('D:/SIDE-kernel', '70aba3c', 'I.is_universal')
    ok.append(bool(fld))
    L.append('  (C4) POS a field: `I.is_universal` at SIDE-kernel v1.8 = 70aba3c (Silence Placement :261, premise :42): %s -- %s' % (
        fld, 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    planted = ['a line saying the RH proof stands here.', 'Not supportable: RH proved; h2_sign proved.', 'a line with no pattern.',
               'a ' + 'bli' + 'nd spot in the text.']
    got = [[(h['what'], h['cls']) for h in lint('planted.md', [p])] for p in planted]
    want = [[('RH proof', 'FOR THE AUTHOR')], [('RH proved', 'AS DESIGNED')], [], [('bli' + 'nd', 'FOR THE AUTHOR')]]
    ok.append(got == want)
    L.append('  (C5) THE LINT ON PLANTED LINES (a live frontdoor hit, a refuted one, a clean line, a live stem): %s -- %s' % (
        got, 'AS WANTED' if ok[-1] else 'NOT AS WANTED (wanted %s)' % want))
    return ok


def bank(*a):
    t0 = time.time()
    fm = free_mb()
    L = ['%s -- THE PILOT ON THE AUTHOR`S WORD: (P1) DECLARATIONS, (P2) PROSE LINT, (P3) A BLUEPRINT`S PRICE (%s)' % (ACT, utc()), '',
         '### beside the homebrew systems, which stay primary; it gates nothing, replaces no arm, tool or bank, moves no score; this bank alone.',
         '### free memory %d MB before the run. PLACE-papers main %s (the merge a86c9429); the seven read from main by git show.' % (
             fm, git(PP, 'rev-parse', '--short', 'main')[1].strip()),
         '### THE SEVEN (the seat`s reading of "the other six keystones", for the navigator): the Day-1 companions as relay tools/b703_checks.py',
         '### :102-:112 names them, the day1 papers on main less the monograph -- %s.' % ', '.join(os.path.basename(p) for p in SEVEN), '',
         '## THE CONTROLS, BEFORE THE FIGURES']
    ok = controls(L)
    census = git(PP, 'show', 'main:' + CENSUS)[1].replace(chr(13), '').split(NL)
    ledger = git(PP, 'show', 'main:' + LEDGER)[1].replace(chr(13), '').split(NL)

    # ------------------------------------------------------------------ (P1)
    L += ['', '## (P1) THE DECLARATION-EXISTENCE CHECK: keystone :line | name | repository | pin as stated | at each pin FOUND file:line (kind) or',
          '##      MISSING | the homebrew rows (census v0.8.1 / FACES_LEDGER, path:line and the grade tokens on that line)']
    tot = dict(FOUND=0, MISSING=0, MIXED=0, NOPIN=0, PINABSENT=0)
    findings = []
    yields = []
    for p in SEVEN:
        lines = git(PP, 'show', 'main:' + p)[1].replace(chr(13), '').split(NL)
        sec, names, y = extract(p, lines)
        yields.append((p, y))
        L.append('')
        if sec is None:
            L.append('  %s: NO CORRESPONDENCE SECTION' % p)
            continue
        L.append('  ### %s -- its Correspondence :%d-:%d ; the matcher`s yield: table rows %d, prose lines with backticks %d, backticked tokens %d,'
                 ' Lean names %d' % (p, sec[0], sec[1], y['rows'], y['prose'], y['tokens'], y['names']))
        for ln, name, pins, where, status in names:
            hb = homebrew(name, census, ledger)
            hbs = ' ; '.join('%s :%d %s' % (r, j, '/'.join(g) or 'no grade token') for r, j, g in hb) or 'NO HOMEBREW ROW'
            st, cells = check(name, pins)
            if st == 'NOPIN':
                tot['NOPIN'] += 1
                L.append('    :%-4d %-44s | NO PIN STATED (%s) | %s' % (ln, name, where, hbs))
                continue
            tot[st] += 1
            L.append('    :%-4d %-44s | %s | status cell %s | %s' % (ln, name, cells, status or '--', hbs))
            gs = set(g for _r, _j, gl in hb for g in gl)
            if st == 'MISSING':
                mt = meta_lookup(name)
                L.append('          ### MISSING at every stated pin: looked up in SIDE-meta beside them -- %s' % mt)
                why = []
                if 'COMPILED' in status.split():
                    why.append('its own status cell (%s :%d) reads COMPILED' % (p, ln))
                if gs & PRESENT:
                    why.append('the homebrew row grades it %s' % hbs)
                if why:
                    findings.append('%s :%d `%s`: MISSING at every stated pin (%s) while %s; in SIDE-meta: %s' % (
                        p, ln, name, cells, ' and '.join(why), mt))
            if st == 'FOUND' and gs and gs <= ABSENT:
                findings.append('%s :%d `%s`: FOUND (%s) while the homebrew row grades it %s' % (p, ln, name, cells, hbs))
            if st in ('MIXED', 'PINABSENT'):
                findings.append('%s :%d `%s`: %s across the stated pins (%s)' % (p, ln, name, st, cells))
    L += ['', '  ### the compiled-environment check (checkdecls in a built environment) needs the runner: priced in (P3), not run.',
          '  ### ### **(P1) NAMES %d: FOUND %d ; MISSING %d ; NO PIN STATED %d ; MIXED ACROSS PINS %d ; PIN ABSENT LOCALLY %d.**' % (
              sum(tot.values()), tot['FOUND'], tot['MISSING'], tot['NOPIN'], tot['MIXED'], tot['PINABSENT'])]

    # ------------------------------------------------------------------ (P2)
    L += ['', '## (P2) THE PROSE-LINT TRIAL: keystone :line | STEM or FRONTDOOR | the hit | AS DESIGNED or FOR THE AUTHOR | why | the sentence']
    lt = dict(AS=0, FOR=0)
    used = set()
    for p in SEVEN:
        lines = git(PP, 'show', 'main:' + p)[1].replace(chr(13), '').split(NL)
        hs = lint(os.path.join(PP, p), lines)
        L.append('  ### %s: hits %d' % (p, len(hs)))
        for h in hs:
            lt['AS' if h['cls'] == 'AS DESIGNED' else 'FOR'] += 1
            L.append('    :%-4d %-9s | %-26s | %-14s | %s | %s' % (h['line'], h['kind'], h['what'], h['cls'], h['why'], h['sent']))
            if h['cls'] == 'FOR THE AUTHOR':
                k = (os.path.basename(p), h['line'], h['what'].lower())
                used.add(k)
                L.append('          ### the seat`s hand-read (the class above is the matcher`s and stands): %s' % HAND.get(k, 'NOT HAND-READ'))
    L += ['  ### Vale is not installed on this host. PRICED for a later act: the install (one binary, vale.sh, a pinned release; or pip vale),',
          '  ###   a .vale.ini at PLACE-papers` root, and one style written from the writing law -- a `existence` rule for the two stems with',
          '  ###   banned_terms` exceptions as `exceptions`, a `existence` rule for the ten frontdoor patterns, and a scope excluding References;',
          '  ###   about 3 hours, no dispatch (it runs locally); its controls the planted lines of (C5).',
          '  ### hand-read notes not met by a hit: %s' % (sorted(set(HAND) - used) or 'NONE'),
          '  ### ### **(P2) HITS %d: AS DESIGNED %d ; FOR THE AUTHOR %d.**' % (lt['AS'] + lt['FOR'], lt['AS'], lt['FOR'])]

    # ------------------------------------------------------------------ (P3)
    L += ['', '## (P3) THE PRICE OF A BLUEPRINT FOR THE REDUCTION CHAIN ALONE, NOTHING BUILT']
    ef = 'D:/SIDE-explicit-formula'
    sl = git(PP, 'show', 'main:' + SURROUND)[1].replace(chr(13), '').split(NL)
    ssec, snames, sy = extract(SURROUND, sl, tiered=True)
    chain = []
    for ln, name, pins, where, tier in snames:
        st, cells = check(name, pins)
        chain.append(('the surround :%d' % ln, name, tier or '--', st, cells or 'NO PIN STATED'))
    for name in ('h2_sign', 'h2_sign_iff_rh', 'rh_strip_imp_rh_holds'):
        st, cells = check(name, [('SIDE-explicit-formula', 'v0.37 = 38e2734', '38e2734')])
        chain.append(('the seam', name, '--', st, cells))
    chain.append(('the target', 'RiemannHypothesis', '--', 'READ', 'Mathlib de5ce8a9 (the faces page :105): '
                  'Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185, read from the faces page, not grepped (no Mathlib clone)'))
    fj = rev_of('D:/SIDE-faces-join', 'v0.1.0')
    st, cells = check('faces_join', [('SIDE-faces-join', 'v0.1.0 = %s' % (fj or '?')[:7], fj or 'v0.1.0')])
    chain.append(('the join', 'faces_join', '--', st, cells))
    L.append('  ### the surround: %s`s tiered Correspondence table %s, its matcher yield %s; each row`s tier its own tier cell.' % (
        SURROUND, ('at :%d-:%d' % (ssec[0], ssec[1])) if ssec else 'NOT FOUND', sy))
    L.append('  ### part | name | tier (the surround`s cell) | at the pin | repository, pin and where | the homebrew rows')
    for part, name, tier, st, cells in chain:
        hb = homebrew(name, census, ledger)
        hbs = ' ; '.join('%s :%d %s' % (r, j, '/'.join(g) or 'no grade token') for r, j, g in hb) or 'NO HOMEBREW ROW'
        L.append('    %-18s | %-44s | %-4s | %-9s | %s | %s' % (part, name, tier, st, cells, hbs))
    n = len(chain)
    L += ['  THE FILES (leanblueprint): blueprint/src/content.tex (one \\definition or \\theorem block per declaration, %d blocks, each with' % n,
          '    \\lean{}, \\leanok where compiled, \\uses{} along the chain), blueprint/src/web.tex, print.tex, macros/common.tex, macros/web.tex,',
          '    macros/print.tex, blueprint/src/plastex.cfg, blueprint/lean_decls (generated by leanblueprint), a `require checkdecls` in the',
          '    kernel`s lakefile with its manifest updated (memory: Lake takes the LAST require`s manifest; the toolchain v4.34.0-rc1 and Mathlib',
          '    de5ce8a9 read against checkdecls` own pin first), and one workflow file for the blueprint build -- each a write in a later act.',
          '  THE DISPATCHES: (1) the lakefile require and `lake update checkdecls` with the package build; (2) `lake exe checkdecls',
          '    blueprint/lean_decls`; (3) `leanblueprint pdf` and `leanblueprint web` (plasTeX, graphviz) -- 3 runner dispatches; a fourth if (1)',
          '    moves the manifest beyond the governing pin and is reverted.',
          '  THE HOURS (an estimate, the seat`s): content.tex at 10 minutes a block (%.1f h), the setup files 1.5 h, the lakefile and manifest' % (n * 10 / 60.0),
          '    read 1 h, the three dispatches with their reading 1.5 h: about %.1f h.' % (n * 10 / 60.0 + 4.0),
          '  ### ### **(P3) THE CHAIN %d DECLARATIONS ; LEANBLUEPRINT FILES 9 + A LAKEFILE REQUIRE + ONE WORKFLOW ; 3 DISPATCHES ; ABOUT %.1f HOURS ; NOTHING BUILT.**' % (
              n, n * 10 / 60.0 + 4.0)]

    # ------------------------------------------------------------------ findings and the foot
    L += ['', '## FINDINGS FOR THE NAVIGATOR (the homebrew reading stands in each; nothing is changed by them)']
    L += ['  (%d) %s' % (k, f) for k, f in enumerate(findings, 1)] or ['  NONE']
    L += ['', '### ### **CONTROLS %d OF %d AS WANTED ; (P1) FOUND %d, MISSING %d, NO PIN STATED %d (MIXED %d, PIN ABSENT %d) ACROSS THE SEVEN ; (P2) AS DESIGNED %d,'
          ' FOR THE AUTHOR %d ; (P3) %d DECLARATIONS, 3 DISPATCHES, ABOUT %.1f HOURS ; FINDINGS %d ; %d s.**' % (
              sum(ok), len(ok), tot['FOUND'], tot['MISSING'], tot['NOPIN'], tot['MIXED'], tot['PINABSENT'], lt['AS'], lt['FOR'], n,
              n * 10 / 60.0 + 4.0, len(findings), int(time.time() - t0))]
    out = NL.join(L) + NL
    print(out)
    if 'dry' in a or not all(ok):
        if not all(ok):
            print('### A CONTROL NOT AS WANTED -- NOTHING WRITTEN')
        return
    data = out.encode('utf-8')
    with open(OUT + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(OUT + '.tmp', OUT)
    print('  %s  data/b714_pilot.txt' % hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'bank':
        print('usage: b714_pilot.py bank [dry]')
        sys.exit(2)
    bank(*sys.argv[2:])
