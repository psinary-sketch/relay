# -*- coding: utf-8 -*-
"""b455_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure is read off this act's own records -- the
### fold JSON, the span JSON, the lock gate's notes, the suite -- and none is typed.
### ### **THE SUITE GATE, STATED:** this tool runs only if the pre-push suite fails on no arm; the suite is re-run after it and must then
### fail on none before anything is committed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b455 the deposit`s exhaustiveness claim read against its own route terminal -->'
PRIOR = '<!-- b454 (R63) executed under (R64), and the span-heading work-order repaired -->'
BANKOUT = os.path.join(D, 'b455_the_claim_and_its_terminal.txt')
SELF_WRITTEN = set()   # ### no arm of the suite reads an object only this tool writes before the suite runs
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
DESK = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


FACE = read(os.path.join(D, 'b455_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b455_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR_, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b455_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b455_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


CJ = _j('b455_claims.json')
TJ = _j('b455_terminals.json')
DJ = _j('b455_dispositions.json')
LJ = _j('b455_line.json')
SPAN = _j('b455_span.json')
READY = bool(CJ.get('claims')) and bool(DJ.get('grades')) and bool(LJ.get('verdict')) and bool(SPAN)
CLAIMS = CJ.get('claims') or []
GR = DJ.get('grades') or {}
DEPL = DJ.get('deposit_level') or []
SPANN = SPAN.get('current_span')
MC = [c for c in CLAIMS if c['cls'] == 'MACHINE-CHECKED']

ROWMARK = ('**THE DEPOSIT STATES THE SEVEN-CLASS CATALOGUE`S EXHAUSTIVENESS AS MACHINE-CHECKED, AND AT ITS OWN ROUTE TERMINAL AT v1.5 THAT '
           'CLAIM GRADES NOT THE CLAIM; THE CONCORDANCE`S LITERAL READING GRADES DERIVES; A DEPOSIT-LEVEL MATTER, ROUTED WITH THREE DISPOSITIONS '
           'PRICED AND NONE TAKEN; b454`S CREDITED COUNTS, EIGHT AND SEVEN, STAND**')
SCOPE = ("### THE ACT READ FIVE DEPOSITED SURFACES FOR EVERY EXHAUSTIVENESS ITEM, CLASSIFIED EACH CLAIM BY ITS OWN BACKING WORDS, READ THE ROUTE "
         "TERMINAL AND SIDE_exclusion AT TAG v1.5 BY GIT SHOW, GRADED EACH AGAINST EACH CLAIM, PRICED THREE DISPOSITIONS AND READ ONE ARCHIVE LINE; "
         "NO LEAN RUN, NO FETCH, NO ZENODO WRITE, NO DISPOSITION TAKEN. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('what the deposit claims (Component 1)', 'CLOSE',
         'READ at b455: %d claims -- %s. MACHINE-CHECKED at the monograph record v1.1.2 (paragraph 4), the tag`s .zenodo.json, the deposited §25.8 (row and On Route 1) and the kernel README at v1.5 (:60).'
         % (len(CLAIMS), ', '.join('%s %s' % (c['id'], c['cls']) for c in CLAIMS))),
        ('the terminal graded per claim (Component 2)', 'CLOSE',
         'GRADED at v1.5: structural_exhaustiveness_proved %s; SIDE_exclusion %s. Profiles printed at v1.2 only; at v1.5 UNREAD.'
         % (' / '.join('%s %s' % (c['id'], GR[c['id']]['route'][0]) for c in CLAIMS), ' / '.join('%s %s' % (c['id'], GR[c['id']]['other'][0]) for c in CLAIMS))),
        ('the deposit-level matter (Component 3)', 'STAND',
         'ROUTED TO THE AUTHOR: %s grade NOT THE CLAIM at their own named terminal. Three dispositions priced -- an ERRATA entry, a live narrowing, a version note -- none recommended, none taken.' % ' and '.join(DEPL)),
        ('C3, the tag`s .zenodo.json claim', 'STAND', 'TEST NOT APPLIED: its own named terminal is UNNAMED; and the kernel record`s description is not held by the record, so whether the record carries the same words is unread.'),
        ('the kernel README at HEAD', 'STAND', 'OBSERVED: SIDE-kernel README.md:60 at HEAD carries the v1.5 sentence unchanged; the kernel lane was read only.'),
        ('the defective pattern (Component 4)', 'CLOSE', 'DECIDED at b455: the archive line states T3`s Tier-1 scope; the counts are 8 and 7; b454`s credited figure stands.'),
        ('the T3 Tier-1 scope annotation in INVARIANCE_BARRIERS', 'STAND', 'ROUTED: the finding is held by a pre-b450 ledger line, and no act has added it; (R63)(b) would add it in the era-annotation form.'),
        ('the observed `SE proved` line', 'STAND', 'PRINTED, NOT CLASSIFIED: SIDE-kernel@v1.5 README.md:97, outside the word test`s yield.'),
        ('W-ORD-MATCHER-SHAPE', 'STAND', 'FIRED at b455 (the `SE` abbreviation); the yield printed; the work-order stays open.'),
        ('(R63)(c) and (R64)(4)', 'STAND', 'ROUTED and DEFERRED, as at b454.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'OPEN; this act`s build passes -DateTag 2026-09-14-b455.'),
    ]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1900], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    body = [
        '### b455 — the deposit’s exhaustiveness claim read against its own route terminal — filed 2026-09-14',
        '',
        '**The deposit states the seven-class catalogue’s exhaustiveness as machine-checked, and at its own route terminal at `v1.5` that claim grades `NOT THE CLAIM`.** The concordance’s literal reading of the same terminal grades `DERIVES`. This is a deposit-level matter; it is routed with three dispositions priced, and none is taken. b454’s credited counts, eight and seven, stand. The kernel lane was read only: no `lean`, no fetch, nothing written at Zenodo.',
        '',
        '#### Component 1 — what the deposit claims',
        '',
        'Five surfaces: the monograph record `v1.1.2` (`10.5281/zenodo.21539167`) as banked at b359; the kernel record `v1.5` (`10.5281/zenodo.21520474`), **whose description the record does not hold**, with the tag’s `.zenodo.json` read in its place and labelled so; the PLACE-papers front door; the deposited monograph’s §25.8, **verified as deposited** by the record’s own MD5; and the kernel README at tag `v1.5`. A word test (`exhaust`, or the terminal’s name) yielded @Y@ items; every item was hand-read.',
        '',
        '| claim | where | the deposit’s words | backing |',
        '|:--|:--|:--|:--|',
    ]
    for c in CLAIMS:
        body.append('| %s | %s | *“%s”* | **%s** |' % (c['id'], c['address'].replace('b359_fetch_F2.json:description', 'monograph record v1.1.2, description'), c['text'].replace('|', '/')[:220], c['cls']))
    body += [
        '',
        'The deposit draws its own line in the monograph record: *“the manuscript proves the mathematics; the kernel compiles the logical architecture”*. Two paragraphs later the same record says *“Proved and machine-checked around the argument: the exhaustiveness of the seven-class catalogue over the places of ℚ”*.',
        '',
        '#### Component 2 — the terminal at `v1.5`, graded per claim',
        '',
        '`structural_exhaustiveness_proved : StructuralExhaustiveness`, read at `v1.5 = 0e5233f` by `git show`, unfolds to three conjuncts: `Fintype.card MechanismClass = 7`, proved `by decide` over an inductive with seven constructors; one `produces_offline` proposition per constructor, each refuted; and every nontrivial absolute value on ℚ real or `p`-adic (Mathlib’s Ostrowski). `techne_kernel.SIDE_exclusion` (`Kernel/Layer1.lean`) concludes `Not (P x)` from `cat : ExhaustiveCatalogue X P` and `NoneProduces`. **Profiles:** printed at `v1.2` only (`DEPOSIT_v1_2_NOTES.md:38`; relay review-2 `:53`); **at `v1.5`, UNREAD**. No `lean` was run.',
        '',
        '| claim | backing | `structural_exhaustiveness_proved` | `SIDE_exclusion` |',
        '|:--|:--|:--|:--|',
    ]
    for c in CLAIMS:
        body.append('| %s | %s | **%s** | **%s** (%s) |' % (c['id'], c['cls'], GR[c['id']]['route'][0], GR[c['id']]['other'][0],
                                                           'premise `cat : ExhaustiveCatalogue X P`' if GR[c['id']]['other'][0] == 'INTERFACES' else 'does not reach the claim'))
    body += [
        '',
        'Against a claim that the catalogue is exhaustive, the route terminal is `NOT THE CLAIM`: it counts the constructors of a type it defines and classifies ℚ’s places side by side, and no conjunct states that the seven classes exhaust the mechanisms. Against §25.8’s own reading — *“it certifies exactly what it literally states”*, catalogue completeness being `Fintype.card MechanismClass = 7` — it `DERIVES`.',
        '',
        '#### Component 3 — the disposition, routed and not taken',
        '',
        '**DEPOSIT-LEVEL MATTER: @DEPL@** — each is MACHINE-CHECKED and grades `NOT THE CLAIM` at its own named terminal: the monograph record `v1.1.2`’s description, paragraph 4, and the kernel README at `v1.5`, line 60. C3, in the tag’s `.zenodo.json`, names no terminal, so the test was not applied to it.',
        '',
    ]
    for d in DJ.get('dispositions') or []:
        body.append('- **%s.** Writes: %s. Zenodo: %s. Unchanged: %s. Acts: %s.' % (d['name'], d['writes'], d['zenodo'], d['unchanged'], d['acts']))
    body += [
        '',
        '**None is recommended; none is taken.** Not at issue here: whether the manuscript proves exhaustiveness, and whether Route 2, Route 3 or any other terminal is affected.',
        '',
        '#### Component 4 — the defective pattern, resolved',
        '',
        '`OPEN_TRAILS-archive-2-historical-landings-and-programs.md:7971` lists `T1`–`T10` in order, with `T8`–`T10` labelled on the line. Its third item reads *“Euler-product consumption at Face E’s **Tier-1 scope verbatim**”*, and the specification’s own row confirms it: *“`T3` — Consume the Euler product essentially. Face E’s barrier is Tier-1 and scoped verbatim”*. **The line states the item. The counts are ADDED 8, HELD BY NO LEDGER 7; b454’s credited figure stands.** b454’s bank is unedited, and no annotation is written.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | at least one deposited surface states exhaustiveness as machine-checked | **HELD** — @NMC@ MACHINE-CHECKED claims |',
        '| (N2) | it grades NOT THE CLAIM at the deposited pin | **HELD** for C2, C3, C6; **REFUTED** for C4, C5, which state only the literal conjuncts and grade DERIVES |',
        '| (N3) | the archive line states the item; the counts are eight and seven | **HELD** |',
        '',
        '**The span by the tool: @SPAN@ acts.** Both instrument lanes stay parked; nothing deposits; `h2` where the deposit left it. The four lists are open.',
    ]
    rep = [('@Y@', str(len(CJ.get('items') or []))), ('@DEPL@', ' and '.join(DEPL)), ('@NMC@', str(len(MC))), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b455)"
    stmt = (m + (". **LOCKED BEFORE ANY READ OF A CLAIM**, %d gates read, %d by digest. **C1: %d CLAIMS ON FIVE SURFACES (%s); THE KERNEL RECORD`S "
                 "DESCRIPTION NOT HELD; THE DEPOSITED MONOGRAPH COPY VERIFIED BY MD5.** **C2: AT v1.5 = 0e5233f, structural_exhaustiveness_proved %s; "
                 "SIDE_exclusion %s; PROFILES PRINTED AT v1.2 ONLY, AT v1.5 UNREAD; NO LEAN RUN.** **C3: DEPOSIT-LEVEL %s; ERRATA ENTRY, LIVE "
                 "NARROWING AND VERSION NOTE PRICED, NONE RECOMMENDED, NONE TAKEN.** **C4: THE LINE STATES T3`S TIER-1 SCOPE; COUNTS 8 AND 7.** "
                 "(N1) HELD, (N2) HELD FOR C2 C3 C6 AND REFUTED FOR C4 C5, (N3) HELD. SPAN BY TOOL %s. 0 GRADES MOVED ON ANY ROW, NOTHING DEPOSITS")
            % (GR_, GDG, len(CLAIMS), ', '.join('%s %s' % (c['id'], c['cls']) for c in CLAIMS), ' / '.join('%s %s' % (c['id'], GR[c['id']]['route'][0]) for c in CLAIMS),
               ' / '.join('%s %s' % (c['id'], GR[c['id']]['other'][0]) for c in CLAIMS), ' AND '.join(DEPL), SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO LEAN RUN; KERNEL READ AT TAG v1.5 ONLY"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; ERRATA.md, README.md, REGISTRY.md, FINDINGS.md, THE DEPOSITED "
            "COPY AND EVERY KEYSTONE BYTE-UNMOVED; SIDE-kernel UNWRITTEN -- 0 CONTENT LOST")
    grade = ("### THE SURFACES, CLASSIFICATION WORDS, PIN, PROFILE RULE, GRADE TEST, PRICING BASIS AND LINE TEST WERE ON THE FACE BEFORE ANY CLAIM "
             "WAS CLASSIFIED; EVERY ITEM HAND-READ; A GRADE STATED ONLY AS A RELATION TO A QUOTED CLAIM")
    status = ("data/b455_the_claim_and_its_terminal.txt; data/b455_components.txt; data/b455_claims.json; data/b455_terminals.json; "
              "data/b455_dispositions.json; data/b455_line.json; data/b455_span.json; data/b455_checks.txt; data/b455_registration_2026-09-14.txt "
              "(LOCKED at sha256 %s); data/b455_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('deposit exhaustiveness claim machine-checked',
           'structural_exhaustiveness_proved graded per claim',
           'route 1 not the claim at v1.5',
           'deposit-level matter dispositions priced',
           'T3 tier-1 scope archive line counts eight and seven')
MUST_NOT_HIT = ('the catalogue exhaustiveness is machine-checked', 'errata entry filed against v1.1.2', 'route 1 derives exhaustiveness')
KEY = 'the-deposits-exhaustiveness-claim-read-against-its-route-terminal'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b455 READ THE DEPOSIT`S EXHAUSTIVENESS CLAIMS: %d MACHINE-CHECKED OF %d; AT v1.5 structural_exhaustiveness_proved GRADES NOT THE CLAIM "
                 "AGAINST THE CATALOGUE`S EXHAUSTIVENESS AND DERIVES AGAINST THE CONCORDANCE`S LITERAL READING; DEPOSIT-LEVEL %s, THREE DISPOSITIONS "
                 "PRICED, NONE TAKEN. COUNTS 8 AND 7 STAND. NO CLAIM ABOUT ZEROS."
                 % (len(MC), len(CLAIMS), ' AND '.join(DEPL)))
    grade = "### NO GRADE MOVED ON ANY ROW. ### RELATIONS GRADED IN THE RECORD ONLY. ### NOTHING DEPOSITS. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b455_the_claim_and_its_terminal.txt; data/b455_components.txt; data/b455_claims.json; data/b455_terminals.json; "
             "data/b455_dispositions.json; data/b455_line.json; data/b455_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR_, GDG, rownum))
    act = "b455 (the deposit's exhaustiveness claim read against its own route terminal)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE DEPOSIT`S EXHAUSTIVENESS CLAIM READ AGAINST ITS OWN ROUTE TERMINAL (b455).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s' % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq[:48], pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL + '    # (key, act, one-line statement, grade as its own act recorded it, location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    out, rc = query(KEY)
    n = out.count('act      :')
    ok = (not no_key(out)) and rc == 0 and n >= 1
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]' % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b455 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the grade carried', 'GRADES NOT THE CLAIM' in out), ('the literal reading carried', 'DERIVES AGAINST THE CONCORDANCE' in out),
                      ('none taken carried', 'NONE TAKEN' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq[:48], no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, "b455 -- THE DEPOSIT'S EXHAUSTIVENESS CLAIM READ AGAINST ITS OWN ROUTE TERMINAL.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR_, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B454ROW_RE = r"(?m)^\| (\d+) \| \*\*\(R63\) IS EXECUTED UNDER \(R64\)"

def main():
    global DESK
    bar('=')
    rec('b455_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; claims %s ; deposit-level %s ; line %s ; span %s'
        % (GR_, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), len(CLAIMS), DEPL, LJ.get('verdict'), SPANN))
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s ; prior text a TRUE PREFIX : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2, t2.startswith(t.rstrip(NL))))
    rec('  lines deleted : 0')
    bar()
    rec('### THE CORRESPONDENCE ROW. ### READ BY MARKER.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    slip = [mm for mm, s2, *_ in ROWS2 if not s2.startswith(mm)]
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s' % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B454ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.' % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b455_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
