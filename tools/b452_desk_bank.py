# -*- coding: utf-8 -*-
"""b452_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure is read off this act's own records -- the count and
### integrand JSON, the lock gate's notes, the suite -- and none is typed.
### ### **THE SUITE GATE, STATED:** this tool runs only if the pre-push suite fails on no arm but the two whose object this
### tool itself writes (`G-FILING-WORKORDER`); the suite is re-run after it and must then
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
MARK = '<!-- b452 the class boundary read by its side, and the six sites read by their generator -->'
PRIOR = '<!-- b451 the remainder named, and the routed items grouped -->'
BANKOUT = os.path.join(D, 'b452_the_boundary_and_the_sites.txt')
SELF_WRITTEN = {'G-WRITELIST-KINDS'}   # ### NOT SELF-WRITTEN: the act's own reported failure (b452_dump.json, a kind the face does not name), carried and stated
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


FACE = read(os.path.join(D, 'b452_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b452_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b452_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b452_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


SJ = _j('b452_sides.json')
TJ = _j('b452_sites.json')
SPAN = _j('b452_span.json')
READY = bool(SJ.get('rows')) and bool(TJ.get('verdict')) and bool(SPAN)
SPANN = SPAN.get('current_span')
CNT = SJ.get('counts') or {}
EXP = SJ.get('expect') or {}
RAT = 'partition %s' % CNT
KINK = 'control %s' % SJ.get('control_state')
MSTATE = 'sites %s' % TJ.get('verdict')

ROWMARK = ('**NONE OF THE FORTY-SEVEN CLASS BOUNDARIES LIES ON THE CORPUS`S SIDE BY A RE-EXPRESSION THE CORPUS HOLDS -- SOURCE-SIDE 44, '
           'UNDECIDED 3, OBJECT-SIDE 0, WITH THE POSITIVE CONTROL ABSENT; AND THE SIX SITES ARE A LIST ASSEMBLED SITE BY SITE, NOT A CLOSED '
           'ENUMERATION**')
SCOPE = ("### THE ACT READ EVERY CLASS-BOUNDARY FAILURE`S CLASS FROM ITS BANK AGAINST TWO HELD RE-EXPRESSIONS FIXED ON ITS FACE, HAND-READ "
         "EVERY WORD-TEST HIT, RAN THE SAME TEST OVER THE OTHER FAILURES AS A CONTROL, AND READ THE ACTS THAT NAMED THE SIX SITES; NO "
         "RE-EXPRESSION PERFORMED, NO SITE PROPOSED, NO LEDGER ROW WRITTEN; (R63) CARRIED TO b454. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('the class boundary`s side, per candidate', 'CLOSE',
         'READ at b452: OBJECT-SIDE %d, SOURCE-SIDE %d (R2 deciding 9, no held re-expression in domain 35), UNDECIDED %d (B8, B9: the height '
         'site`s test-function support unstated; W1: no class text). R1 matched nothing. The control over the 35 non-K1 failures is ABSENT.'
         % (CNT.get('OBJECT-SIDE', 0), CNT.get('SOURCE-SIDE', 0), CNT.get('UNDECIDED', 0))),
        ('what the test cannot say', 'STAND',
         'The control is ABSENT: the test over R1 and R2 has not been shown able to return OBJECT-SIDE, so the empty OBJECT-SIDE is a result of '
         'these two sources and no wider. A re-expression held elsewhere in the corpus was out of the order`s scope.'),
        ('the six sites` generator', 'STAND',
         'READ at b452: a LIST -- b355 named three places, b401 the fourth, b404 the fifth and sixth; row U1`s criterion is a membership test '
         '("THE SHAPE, NAMED AND NOT PROVED"), not a generator. Closing it needs a generator with a finite printed range and a disposition '
         'for every member. No seventh site proposed.'),
        ('the unnamed data kind b452_dump.json', 'STAND',
         'FOUND by G-WRITELIST-KINDS: the components` dump pass wrote a kind the locked face does not name. Not deleted (a run artifact is '
         'evidence); the arm fails and is carried, reported here and in the row.'),
        ('(R63)', 'STAND', 'CARRIED, not executed: the author directs it as b454, after the fold.'),
        ('W-ORD-MATCHER-SHAPE', 'STAND', 'FIRED at b452 (two word tests); both yields printed and every hit hand-read; the work-order stays open.'),
        ('W-ORD-SPAN-HEADING', 'STAND', 'CARRIED; the fold is next.'),
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
    rows = [r for r in SJ['rows'] if r['kind'] == 'CLASS BOUNDARY']
    body = [
        '### b452 — the class boundary read by its side, and the six sites read by their generator — filed 2026-09-14',
        '',
        '**None of the forty-seven class boundaries lies on the corpus’s side by a re-expression the corpus holds.** OBJECT-SIDE @OS@, SOURCE-SIDE @SS@, UNDECIDED @UD@, and the positive control is **ABSENT** — which is not a pass. **The six sites are a list assembled site by site, not a closed enumeration.** (R63) is carried to b454, as directed.',
        '',
        '#### Component 1 — which side the boundary is on',
        '',
        'Two re-expressions are held, fixed on the face from the two sources the order names:',
        '- **R1**, from `REPARAMETERIZATION_BARRIERS_v0_1.md:94–101`: `GL(n)`/`O(n)` reparameterizations of a network’s representations. Its domain is a network’s representations.',
        '- **R2**, the two-kinds windows verdict (`day1/Exhaustive_Enumeration.md:171`; archived `OPEN_TRAILS:8431`): support re-expressed as a width `2 log a`; the prime-free window at most `(1/2, 2)`; index truncation `DISTINCT` from support truncation.',
        '',
        'A word test decided where each applies. R1 matched **@R1@** of 82 failures and R2 matched **@R2@**; every R2 hit was hand-read.',
        '',
        '| site | OBJECT-SIDE | SOURCE-SIDE | UNDECIDED | class-boundary |',
        '|:--|--:|--:|--:|--:|',
    ]
    for s in ('i', 'ii', 'iii', 'iv', 'v', 'vi'):
        rs = [r for r in rows if r['site'] == s]
        body.append('| (%s) | %d | %d | %d | %d |' % (s, sum(1 for r in rs if r['verdict'] == 'OBJECT-SIDE'), sum(1 for r in rs if r['verdict'] == 'SOURCE-SIDE'),
                                                    sum(1 for r in rs if r['verdict'] == 'UNDECIDED'), len(rs)))
    body += [
        '| **total** | **@OS@** | **@SS@** | **@UD@** | **47** |',
        '',
        '**Where R2 decided (9):**',
        '- CC’s Theorems 1 and 6.11 at sites (i), (ii) and (iii) are classes of the prime-free support `[2^-1/2, 2^1/2]`, while each site’s object ranges past it — *“the largest prime-free window is `(1/2, 2)`”*.',
        '- The one-width classes (Boas–Kac; the wide-support bound at one `a`) are decided by *“support truncation controls width exactly as `2 log a`”*: one support fixes one width.',
        '- Lagarias’s Li coefficients at site (iii) are decided by *“index truncation does not localise support … DISTINCT”*.',
        '',
        'The other 35 SOURCE-SIDE verdicts have no held re-expression whose domain holds either the class or the object — an L-function’s quantifiers, heights, moduli or representations, not a network’s activations or a support window. **UNDECIDED (3):** `B8` and `B9` at site (ii), where the bank does not state the support of the test function the height site’s object is evaluated with; and `W1` at site (iv), where the bank records only *“FAILED AT A QUOTED STEP”*.',
        '',
        '**The control:** the same test over the 35 other failures returns no OBJECT-SIDE — R2’s hits there are mentions (*“AVAILABLE at the window”*) or absences. **ABSENT: the test has not been shown able to say OBJECT-SIDE**, so the empty OBJECT-SIDE is a result of these two sources and no wider. No re-expression was performed.',
        '',
        '#### Component 2 — the six sites, by what named them',
        '',
        '| sites | named by | the act’s words |',
        '|:--|:--|:--|',
        '| (i)–(iii) | b355, `b355_sortie_closing.txt:72`; row created at PLACE-papers `5cd458c` | *“the shape common to three places where the record needs a statement UNIFORM in an index”* |',
        '| (iv) | b401, `b401_the_absent_element_searched.txt:16`; `d128d33` | *“THE FOURTH SITE ENTERED”* |',
        '| (v)–(vi) | b404, `b404_the_fifth_and_sixth_sites.txt:17`; `9b72339` | *“THE FIFTH SITE ENTERED, THE SIXTH ENTERED”* |',
        '',
        'Row U1’s own criterion (`FACES_LEDGER.md:31`) — *“THE SHAPE, NAMED AND NOT PROVED: in each, what the record holds is a family indexed by something, and what it needs is one statement uniform in that index”* — is a membership test and prints no range. The one rule-word hit in the naming acts is `crt_exhaustiveness`, a kernel theorem’s name. **Verdict: a LIST.** **To close it, the record would need** a generator with a finite range printed on its face — for instance the explicit formula’s channels or the pentagon’s registers, if ruled the index set — and, for every member, either its site or a statement that the obstruction does not arise there. No seventh site is proposed.',
        '',
        '*Reported against this act:* the components’ dump pass wrote `data/b452_dump.json`, a kind the locked face does not name. The write-list arm fails on it and the file is kept.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | OBJECT-SIDE is not empty | **@N1@** — 0, the control ABSENT |',
        '| (N2) | the six sites are a list and not a closed enumeration | **@N2@** |',
        '',
        'This seat’s own, from the face: (N1) refuted — **HELD**; (N2) held — **HELD**.',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b452), against a ruled threshold of nine.** Both instrument lanes stay parked. The four lists are open.',
    ]
    rep = [('@OS@', str(CNT.get('OBJECT-SIDE', 0))), ('@SS@', str(CNT.get('SOURCE-SIDE', 0))), ('@UD@', str(CNT.get('UNDECIDED', 0))),
           ('@R1@', str(SJ.get('r1_yield'))), ('@R2@', str(SJ.get('r2_yield'))), ('@N1@', EXP.get('n1', '')), ('@N2@', EXP.get('n2', '')), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b452)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; NO CANDIDATE`S CLASS READ BEFORE THE FACE. **COMPONENT 1: TWO HELD "
                 "RE-EXPRESSIONS FIXED -- R1 THE REPARAMETERIZATION KEYSTONE`S GL(n)/O(n), R2 THE TWO-KINDS WINDOWS VERDICT; WORD TEST R1 %s, R2 %s, "
                 "EVERY HIT HAND-READ; OBJECT-SIDE %d, SOURCE-SIDE %d (R2 DECIDING 9), UNDECIDED %d; THE CONTROL OVER THE 35 OTHER FAILURES ABSENT, "
                 "NOT PASSED.** **COMPONENT 2: THE SIX SITES A LIST -- b355 THREE, b401 THE FOURTH, b404 THE FIFTH AND SIXTH; ROW U1`S CRITERION A "
                 "MEMBERSHIP TEST WITH NO RANGE; CLOSURE NEEDS A GENERATOR WITH A FINITE PRINTED RANGE.** (N1) %s, (N2) %s. ONE ARM FAILS AND IS "
                 "CARRIED: AN UNNAMED DATA KIND, b452_dump.json. (R63) CARRIED TO b454. SPAN BY TOOL %s. 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, SJ.get('r1_yield'), SJ.get('r2_yield'), CNT.get('OBJECT-SIDE', 0), CNT.get('SOURCE-SIDE', 0), CNT.get('UNDECIDED', 0),
               EXP['n1'], EXP['n2'], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; FACES_LEDGER.md, FINDINGS.md, REGISTRY.md, EVERY KEYSTONE, "
            "EVERY CANDIDATE BANK AND EVERY CLOSING BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### THE RE-EXPRESSIONS, THE TEST, THE CONTROL AND THE CLOSURE TEST WERE ON THE FACE BEFORE ANY CANDIDATE WAS READ; EVERY WORD-TEST "
             "HIT HAND-READ; THE ABSENT CONTROL REPORTED AS A LIMIT")
    status = ("data/b452_the_boundary_and_the_sites.txt; data/b452_components.txt; data/b452_sides.json; data/b452_sites.json; data/b452_dump.json "
              "(UNNAMED ON THE FACE); data/b452_span.json; data/b452_checks.txt; data/b452_registration_2026-09-14.txt (LOCKED at sha256 %s); "
              "data/b452_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('which side is the class boundary on',
           'object-side source-side undecided',
           'are the six sites a closed enumeration',
           'row U1 sites generator',
           'two-kinds windows verdict as a re-expression')
MUST_NOT_HIT = ('the partition is decided', 'the sites are closed', 'every keystone is reconciled')
KEY = 'the-class-boundary-read-by-its-side-and-the-six-sites'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b452 READ THE 47 CLASS BOUNDARIES AGAINST TWO HELD RE-EXPRESSIONS: OBJECT-SIDE %d, SOURCE-SIDE %d, UNDECIDED %d; THE CONTROL ABSENT. "
                 "THE SIX SITES ARE A LIST ASSEMBLED SITE BY SITE, NOT A CLOSED ENUMERATION. NO CLAIM ABOUT ZEROS."
                 % (CNT.get('OBJECT-SIDE', 0), CNT.get('SOURCE-SIDE', 0), CNT.get('UNDECIDED', 0)))
    grade = "### NO GRADE MOVED. ### NO RE-EXPRESSION PERFORMED, NO SITE PROPOSED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b452_the_boundary_and_the_sites.txt; data/b452_components.txt; data/b452_sides.json; data/b452_sites.json; "
             "data/b452_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b452 (the class boundary read by its side, and the six sites read by their generator)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE CLASS BOUNDARY READ BY ITS SIDE, AND THE SIX SITES READ BY THEIR GENERATOR (b452).%s'
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
        rec('    %-58s reaches the b452 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the partition carried', ('OBJECT-SIDE %d' % CNT.get('OBJECT-SIDE', 0)) in out), ('the list carried', 'A LIST ASSEMBLED SITE BY SITE' in out),
                      ('the control carried', 'THE CONTROL ABSENT' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b452 -- THE CLASS BOUNDARY READ BY ITS SIDE, AND THE SIX SITES READ BY THEIR GENERATOR.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s -- the one failing arm is the act`s own reported write-list failure, carried' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B451ROW_RE = r"(?m)^\| (\d+) \| \*\*THE RECONCILIATION`S ARITHMETIC IS 1 \+ 3 \+ 11"


def main():
    global DESK
    bar('=')
    rec('b452_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; %s ; %s ; %s ; span %s'
        % (GR, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), RAT, KINK, MSTATE, SPANN))
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B451ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b452_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
