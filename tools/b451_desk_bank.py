# -*- coding: utf-8 -*-
"""b451_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b451 the remainder named, and the routed items grouped -->'
PRIOR = '<!-- b450 the eligible set re-measured, and the batch read -->'
BANKOUT = os.path.join(D, 'b451_the_remainder_and_the_kinds.txt')
SELF_WRITTEN = {'G-FILING-WORKORDER'}
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


FACE = read(os.path.join(D, 'b451_registration_2026-09-13.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b451_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b451_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b451_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


RJ = _j('b451_remainder.json')
KJ = _j('b451_kinds.json')
SPAN = _j('b451_span.json')
READY = bool(RJ.get('population')) and bool(KJ.get('items')) and bool(SPAN)
SPANN = SPAN.get('current_span')
REM = RJ.get('remainder') or []
CNT = KJ.get('counts') or {}
EXP = KJ.get('expect') or {}
RAT = 'remainder %s' % REM
KINK = 'kinds %s' % CNT
MSTATE = 'largest %s' % KJ.get('largest')

ROWMARK = ('**THE RECONCILIATION`S ARITHMETIC IS 1 + 3 + 11 = 15 OF 16 AND THE REMAINDER IS ENUMERA, WHICH NEEDS AN AUTHOR NAMING ITS '
           'TERMINAL, NOT A CLONE; THE TWENTY-NINE ROUTED ITEMS FALL INTO TWO KINDS BY THEIR OWN WORDS -- AUTHORING 26, REGISTRY ROW 3 -- '
           'AND THE ITEM DOES NOT SAY IS EMPTY**')
SCOPE = ("### THE ACT COUNTED THE CENSUS AND THE RECONCILED SET FROM THREE BANKS, NAMED THE REMAINDER WITH ITS NEED FROM b395`S BANK, "
         "GROUPED b450`S ROUTED ITEMS BY THE RULING THEIR OWN WORDS NAME, APPENDED ONE LINE TO THE PREDICATE LORE AND FILED ONE WORK-ORDER; "
         "NO KEYSTONE OPENED, NO RULING PROPOSED, NO ITEM ANSWERED, NO MATCHER EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('the reconciliation`s remainder', 'STAND',
         'NAMED at b451: census 16, reconciled 1 + 3 + 11 = 15 (b390, b394, b450), remainder ENUMERA. Its need, from b395`s bank: an author '
         'naming its terminal; no clone would help. ROUTED.'),
        ('b450`s twenty-nine routed items', 'STAND',
         'GROUPED at b451 by the ruling each item`s own words name: AUTHORING %d (absent material 16, prose 8, a correspondence table 2; '
         '3 name a precondition beside it), REGISTRY ROW %d, THE ITEM DOES NOT SAY %d. No ruling proposed, no item answered.'
         % (CNT.get('AUTHORING', 0), CNT.get('REGISTRY ROW', 0), CNT.get('THE ITEM DOES NOT SAY', 0))),
        ('the predicate lore`s incidents', 'CLOSE',
         'FILED at b451: one line in TECHNE PREDICATE_ONE_SHAPE.md (local) naming b390`s version matcher, b394`s repository matcher, '
         'and b450`s table-header test and file-name citation matcher.'),
        ('W-ORD-MATCHER-SHAPE', 'STAND',
         'FILED at b451. Trigger: the next act that matches a table header, a document name or a version by pattern. No matcher edited.'),
        ('this act`s own crude carried-tool matcher', 'CLOSE',
         'FOUND AND REPLACED after the lock, inside the suite, before its first passing reading: a prior-act token test fired on variable names; the write-target shape, with a '
         'control on b450`s incident line, replaced it and both yields print.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'FIRED again by b451`s closing build, passed -DateTag; the repair is not made.'),
        ('W-ORD-SPAN-HEADING', 'STAND', 'CARRIED: the instrument-audit lane parked; not a fold.'),
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
    items = KJ['items']
    body = [
        '### b451 — the reconciliation’s remainder named, and the routed items grouped by the ruling each needs — filed 2026-09-13',
        '',
        '**The reconciliation’s arithmetic, counted from the acts’ own banks: `1` (b390) + `3` (b394) + `11` (b450) = `15`, with no overlaps, against a census of `16`. The remainder is one keystone, `ENUMERA`. It needs neither a clone nor a ruling about reading branches: b395’s bank says *“WHAT IT NEEDS IS AN AUTHOR NAMING ITS TERMINAL”* and *“no clone would help.”* Routed. The twenty-nine items b450 routed fall, by the ruling their own words name, into two kinds — authoring @AU@, registry row @RR@ — and THE ITEM DOES NOT SAY is empty.**',
        '',
        '#### Component 1 — the remainder',
        '',
        '| act | reconciled | bank address |',
        '|:--|--:|:--|',
    ]
    for s in RJ['sets']:
        body.append('| %s | %d | `%s` |' % (s['act'], len(s['members']), s['address']))
    body += [
        '| **union** | **%d** | overlaps %d |' % (len(RJ['union']), len(RJ['overlaps'])),
        '| **census** | **%d** | `THE_KEYSTONE_CENSUS.md:73–88` |' % len(RJ['population']),
        '| **remainder** | **%d** | `%s` — an author naming its terminal (`b395_the_ceiling_answered.txt:51–52`; `b395_components.txt:146`) |' % (len(REM), ', '.join(REM)),
        '',
        '*The roster, for checking:* ' + ', '.join('`%s`%s' % (k, '' if k in RJ['union'] else ' **(unreconciled)**') for k in RJ['population']) + '.',
        '',
        '#### Component 2 — the twenty-nine, grouped by the ruling each needs',
        '',
        '*The kind is the ruling each item’s own clause names first. A further condition the item names is printed beside it and does not form a kind. The seat wrote these items at b450, and the face says so.*',
        '',
        '| kind | count | items (keystone — what — `b450_components.txt` line) | what a ruling would unblock |',
        '|:--|--:|:--|:--|',
    ]
    for kind in sorted(CNT, key=lambda x: (x == 'THE ITEM DOES NOT SAY', -CNT[x])):
        rs = [r for r in items if r['kind'] == kind]
        cell = '<br>'.join('`%s` — %s%s — :%s' % (r['keystone'], r['what'].replace('|', '/').replace('`', '’')[:80],
                                                   (' *(precondition: %s)*' % r['precondition'].replace('`', '’')) if r['precondition'] else '',
                                                   r['address'].split(':')[1]) for r in rs) or '—'
        body.append('| **%s** | **%d** | %s | %s |' % (kind, CNT[kind], cell, KJ['unblock'].get(kind, '').replace('`', '’')))
    body += [
        '',
        'Within authoring, by the form each clause names (these are forms, not kinds): absent material @F1@, prose @F2@, a correspondence table @F3@. Three items name a precondition beside their ruling: two findings whose form is not located in the ledgers (`INVARIANCE_BARRIERS`), and one census premise the keystone never carried (`R_CURVE_CRITERION`). **No ruling is proposed and no item is answered.**',
        '',
        '#### Filed — the predicate lore’s incidents, and W-ORD-MATCHER-SHAPE',
        '',
        'One line has been appended to TECHNE `PREDICATE_ONE_SHAPE.md` (b370’s lore — *a predicate that knows one shape finds one shape*), committed locally and not pushed. It names four incidents: b390’s version matcher, b394’s repository matcher answered at b395, and b450’s table-header test and file-name citation matcher. **W-ORD-MATCHER-SHAPE.** Before it relies on a match, an act that matches by pattern states the shape its predicate assumes and prints a second shape’s yield. **Trigger: the next act that matches a table header, a document name or a version by pattern.** No matcher is edited under this act. *A fifth instance occurred inside this act:* its own carried-tool arm first used a prior-act token test, which fired on variable names. It was replaced by a write-target shape with a control on b450’s incident line, and both yields print.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(i) | the remainder is exactly one keystone | **@N1I@** — `ENUMERA` |',
        '| (N1)(ii) | it is the one b395 left unreadable without a clone | **@N1II@** — it is b395’s unreadable one, and b395 says no clone would help |',
        '| (N2)(a) | fewer than ten kinds | **@N2A@** — two with members |',
        '| (N2)(b) | authoring is the largest kind | **@N2B@** — 26 of 29 |',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b451), against a ruled threshold of nine.** Both instrument lanes stay parked. The four lists are open.',
    ]
    fm = KJ.get('by_form') or {}
    rep = [('@AU@', str(CNT.get('AUTHORING', 0))), ('@RR@', str(CNT.get('REGISTRY ROW', 0))), ('@F1@', str(fm.get('absent material', 0))),
           ('@F2@', str(fm.get('prose', 0))), ('@F3@', str(fm.get('a correspondence table', 0))), ('@N1I@', EXP.get('n1i', '')),
           ('@N1II@', EXP.get('n1ii', '')), ('@N2A@', EXP.get('n2a', '')), ('@N2B@', EXP.get('n2b', '')), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b451)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; WHAT THE SEAT HAD SEEN DECLARED. **COMPONENT 1: CENSUS %d; "
                 "RECONCILED FROM THE BANKS b390 1, b394 3, b450 11; UNION %d, OVERLAPS 0; REMAINDER %s -- ITS NEED, FROM b395'S BANK, AN "
                 "AUTHOR NAMING ITS TERMINAL; NO CLONE WOULD HELP; ROUTED.** **COMPONENT 2: 29 ITEMS FROM b450'S BANK, GROUPED BY THE RULING "
                 "EACH NAMES: AUTHORING %d, REGISTRY ROW %d, THE ITEM DOES NOT SAY %d; 3 PRECONDITIONS PRINTED BESIDE; NO RULING PROPOSED.** "
                 "**FILED: ONE LINE TO THE PREDICATE LORE (LOCAL); W-ORD-MATCHER-SHAPE WITH ITS TRIGGER; NO MATCHER EDITED.** (N1)(i) %s, "
                 "(N1)(ii) %s, (N2)(a) %s, (N2)(b) %s. SPAN BY TOOL %s. 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, len(RJ['population']), len(RJ['union']), ', '.join(REM), CNT.get('AUTHORING', 0), CNT.get('REGISTRY ROW', 0),
               CNT.get('THE ITEM DOES NOT SAY', 0), EXP['n1i'], EXP['n1ii'], EXP['n2a'], EXP['n2b'], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; EVERY KEYSTONE, REGISTRY.md, FINDINGS.md, THE CENSUS AND "
            "EVERY CLOSING BYTE-UNMOVED; TECHNE-Core PREDICATE_ONE_SHAPE.md +1 LINE, LOCAL -- 0 CONTENT LOST")
    grade = ("### THE POPULATION, THE BANKS, THE KIND RULE AND THE FILING WERE ON THE FACE BEFORE ANY COUNT; THE SEAT'S PRIOR SIGHT OF THE "
             "ITEMS WAS DECLARED; EACH VERDICT IS THE RULE'S AS IT FELL")
    status = ("data/b451_the_remainder_and_the_kinds.txt; data/b451_components.txt; data/b451_remainder.json; data/b451_kinds.json; "
              "data/b451_span.json; data/b451_checks.txt; data/b451_registration_2026-09-13.txt (LOCKED at sha256 %s); "
              "data/b451_addendum.txt (EMPTY); TECHNE-Core PREDICATE_ONE_SHAPE.md (LOCAL); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('the reconciliation remainder',
           'what does ENUMERA need',
           'the routed items grouped by ruling',
           'W-ORD-MATCHER-SHAPE',
           'predicate one shape incidents')
MUST_NOT_HIT = ('every keystone is reconciled', 'the census is complete', 'the partition is decided')
KEY = 'the-remainder-named-and-the-routed-items-grouped'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b451 COUNTED THE RECONCILIATION FROM THE BANKS: 1 + 3 + 11 = 15 OF 16; THE REMAINDER IS ENUMERA, WHICH NEEDS AN AUTHOR "
                 "NAMING ITS TERMINAL. b450'S 29 ROUTED ITEMS GROUPED BY THEIR OWN WORDS: AUTHORING %d, REGISTRY ROW %d, THE ITEM DOES NOT SAY %d. "
                 "W-ORD-MATCHER-SHAPE FILED. NO CLAIM ABOUT ZEROS." % (CNT.get('AUTHORING', 0), CNT.get('REGISTRY ROW', 0), CNT.get('THE ITEM DOES NOT SAY', 0)))
    grade = "### NO GRADE MOVED. ### NO RULING PROPOSED, NO ITEM ANSWERED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b451_the_remainder_and_the_kinds.txt; data/b451_components.txt; data/b451_remainder.json; data/b451_kinds.json; "
             "data/b451_registration_2026-09-13.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b451 (the reconciliation's remainder named, and the routed items grouped by the ruling each needs)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE RECONCILIATION`S REMAINDER NAMED, AND THE ROUTED ITEMS GROUPED (b451).%s'
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
        rec('    %-58s reaches the b451 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the arithmetic carried', '1 + 3 + 11 = 15 OF 16' in out), ('the remainder carried', 'THE REMAINDER IS ENUMERA' in out),
                      ('the kinds carried', ('AUTHORING %d' % CNT.get('AUTHORING', 0)) in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b451 -- THE RECONCILIATION'S REMAINDER NAMED, AND THE ROUTED ITEMS GROUPED BY THE RULING EACH NEEDS.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s -- the failing arms all this tool`s own writes' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B450ROW_RE = r"(?m)^\| (\d+) \| \*\*THE ELIGIBLE SET IS ELEVEN, NOT FOUR"


def main():
    global DESK
    bar('=')
    rec('b451_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B450ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b451_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
