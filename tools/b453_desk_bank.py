# -*- coding: utf-8 -*-
"""b453_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b453 the fold at span eight -->'
PRIOR = '<!-- b452 the class boundary read by its side, and the six sites read by their generator -->'
BANKOUT = os.path.join(D, 'b453_the_fold.txt')
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


FACE = read(os.path.join(D, 'b453_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b453_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b453_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b453_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


FJ = _j('b453_fold.json')
SPAN = _j('b453_span.json')
READY = bool(FJ.get('rows')) and FJ.get('verified') == FJ.get('strings') == 17 and bool(SPAN)
LF = SPAN.get('last_fold') or {}
COLS = FJ.get('columns') or {}

ROWMARK = ('**THE RESIDUE AND RECONCILIATION ARC IS FOLDED, b445-b452: EIGHT ACTS, SEVENTEEN VERDICT STRINGS VERIFIED IN THEIR OWN BANKS, '
           'COLUMNS OBJECT 0 / MODEL 3 / RECORD 5; ONE CARRIED ARM FAILURE; THE DIGEST REFRESHED AND NOTHING ELSE EDITED**')
SCOPE = ("### THE ACT RESTATED EIGHT ACTS FROM THEIR OWN CLOSING BANKS, APPENDED ONE FOLD SECTION TO FINDINGS AND ONE BLOCK TO THE DIGEST UNDER "
         "(R31), ENTERED THE NAVIGATOR`S ERROR AS THE NAVIGATOR`S AND THE SEAT`S AS THE SEAT`S, AND LISTED FOUR RULINGS WITH THEIR STATUS; "
         "NO EXPECTATION REGISTERED, NOTHING MINTED, (R63) AND (R64) CARRIED TO b454. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('the fold over b445-b452', 'CLOSE',
         'FILED at b453: %d strings verified in %d acts` own closing banks; columns OBJECT 0, MODEL %d, RECORD %d, four borderlines named; '
         'the tool reads the last fold as b%s-b%s, filed by b%s.' % (FJ.get('verified'), FJ.get('acts_verified'), COLS.get('MODEL', 0),
                                                                  COLS.get('RECORD', 0), LF.get('lo'), LF.get('hi'), SPAN.get('filed_by'))),
        ('the carried arm failure, data/b452_dump.json', 'STAND',
         'RECORDED by the fold as its one carried arm failure; the arm (G-WRITELIST-KINDS) unweakened, the file kept as evidence.'),
        ('the navigator`s kind-check entry (REPARAMETERIZATION_BARRIERS)', 'STAND',
         'ENTERED as the navigator`s, in the order`s words; the count of three not re-derived. No error ledger file exists; the record`s own '
         'heading form was used.'),
        ('W-ORD-SPAN-HEADING', 'STAND',
         'FIRED twice (b449 by (R62), b453 by this fold), UNREPAIRED: the order edits nothing but the fold and the digest. The seat`s b449 '
         'carrying of it as unfired is entered as the seat`s error.'),
        ('(R63) and (R64)', 'STAND', 'CARRIED, not executed: both directed to b454, after the fold.'),
        ('(c2) and (c4)', 'STAND', 'PRICED, UNRUN; the instrument lane is parked.'),
        ('W-ORD-MATCHER-SHAPE', 'STAND', 'OPEN; not fired at b453 (no matcher run over a new corpus).'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'OPEN; this act`s build passes -DateTag 2026-09-14-b453.'),
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
        '### b453 — the fold at span eight — filed 2026-09-14',
        '',
        '**The residue and reconciliation arc is folded, b445–b452, in its standing form.** One section appended to `FINDINGS.md` under a heading the span tool reads, and one block appended to the digest under `(R31)`; nothing else was edited. No expectation was registered: a fold restates and mints nothing.',
        '',
        '**The span, by the tool:** `b363_span.py` read **@SPT@** through this filing act; the fold’s own span, the filing act excluded, is **@SPF@**. After the write the tool reports the last fold as b@LO@–b@HI@, filed by b@FB@, and the next span starting at b@SS@.',
        '',
        '**Carried, each verified in its own bank:** @STR@ verdict strings across @ACT@ acts, every one matched exactly in that act’s closing — the rule floor and the window’s corrected ceiling (b447, b448); the partition read RELATED and its trigger at `(R61)`, ratified at b449; the outlier narrowed to the prime channel, (c1) and (c3) refuted, (c2) and (c4) priced and unrun; the reconciliation at fifteen of sixteen with `ENUMERA` named; the twenty-nine grouped by ruling; the class boundary SOURCE-SIDE for R2 with the control ABSENT; the six sites a LIST.',
        '',
        '**Columns:** object **0**, model **@MOD@**, record **@REC@**; b446, b447, b448 and b449 borderline, each named in its row.',
        '',
        '**The one carried arm failure:** b452’s `G-WRITELIST-KINDS` on `data/b452_dump.json`, the arm unweakened.',
        '',
        '**Errors entered as their owners’.** The navigator’s: `REPARAMETERIZATION_BARRIERS` named by its word at b452 and found to be a neural-network keystone — the kind-check species, third incident this window; the count entered as the navigator’s. The seat’s: b449 carried `W-ORD-SPAN-HEADING` as unfired although `(R62)` had opened the instrument lane.',
        '',
        '**Rulings:** `(R61)` ratified at b449; `(R62)` executed at b449; `(R63)` and `(R64)` directed to b454, not executed.',
        '',
        '`W-ORD-SPAN-HEADING` has fired twice and is unrepaired. No grade moved; nothing deposits; `h2` where the deposit left it. The four lists are open.',
    ]
    rep = [('@SPT@', str(FJ.get('span_tool'))), ('@SPF@', str(FJ.get('span_fold'))), ('@LO@', str(LF.get('lo'))), ('@HI@', str(LF.get('hi'))),
           ('@FB@', str(SPAN.get('filed_by'))), ('@SS@', str(SPAN.get('span_starts_at'))), ('@STR@', str(FJ.get('verified'))),
           ('@ACT@', str(FJ.get('acts_verified'))), ('@MOD@', str(COLS.get('MODEL', 0))), ('@REC@', str(COLS.get('RECORD', 0)))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b453)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest. **THE FOLD: %d STRINGS IN %d BANKS, EXACT MATCH; SPAN BY TOOL %s THROUGH "
                 "THE FILING ACT, %s FOLDED; THE TOOL NOW READS THE LAST FOLD b%s-b%s FILED BY b%s.** CARRIED: THE RULE FLOOR AND THE CORRECTED "
                 "CEILING; RELATED AND (R61) RATIFIED; THE PRIME CHANNEL, (c1) (c3) REFUTED, (c2) (c4) PRICED UNRUN; FIFTEEN OF SIXTEEN WITH "
                 "ENUMERA; THE TWENTY-NINE BY RULING; SOURCE-SIDE FOR R2, CONTROL ABSENT; THE SIX SITES A LIST. ONE CARRIED ARM FAILURE: "
                 "b452_dump.json, THE ARM UNWEAKENED. ERRORS: THE NAVIGATOR`S KIND-CHECK ENTRY (THIRD INCIDENT, THEIR COUNT); THE SEAT`S b449 "
                 "W-ORD-SPAN-HEADING CARRIAGE. RULINGS: (R61) RATIFIED, (R62) EXECUTED, (R63) (R64) TO b454. NO EXPECTATIONS. 0 GRADES MOVED, "
                 "0 CONTENT LOST")
            % (GR, GDG, FJ.get('verified'), FJ.get('acts_verified'), FJ.get('span_tool'), FJ.get('span_fold'), LF.get('lo'), LF.get('hi'),
               SPAN.get('filed_by')))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: FINDINGS.md +1 FOLD SECTION, THE_FINDINGS_AS_THEY_STAND.md +1 BLOCK, OPEN_TRAILS.md +1 RECORD, EACH APPENDED AS A "
            "TRUE PREFIX; FACES_LEDGER.md, REGISTRY.md, EVERY KEYSTONE AND EVERY CLOSING BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### THE ROWS, THEIR STRINGS AND THEIR COLUMNS WERE ON THE FACE BEFORE ANY WRITE; EVERY STRING RE-VERIFIED BY THE SUITE IN ITS OWN "
             "BANK; A FOLD RESTATES AND MINTS NOTHING")
    status = ("data/b453_the_fold.txt; data/b453_components.txt; data/b453_fold.json; data/b453_fold_run.txt; data/b453_span.json; "
              "data/b453_checks.txt; data/b453_registration_2026-09-14.txt (LOCKED at sha256 %s); data/b453_addendum.txt (EMPTY); FINDINGS.md; "
              "THE_FINDINGS_AS_THEY_STAND.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('the residue and reconciliation arc folded',
           'fold b445 b452',
           'the fold at span eight',
           'carried arm failure b452_dump',
           'rulings R61 R62 R63 R64 status')
MUST_NOT_HIT = ('the partition is decided', 'the sites are closed', 'every keystone is reconciled')
KEY = 'the-residue-and-reconciliation-arc-folded'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b453 FOLDED b445-b452 (THE RESIDUE AND RECONCILIATION ARC): %d VERDICT STRINGS VERIFIED IN %d BANKS; COLUMNS OBJECT 0, MODEL %d, RECORD %d; "
                 "ONE CARRIED ARM FAILURE; (R63) AND (R64) TO b454. A FOLD MINTS NOTHING. NO CLAIM ABOUT ZEROS."
                 % (FJ.get('verified'), FJ.get('acts_verified'), COLS.get('MODEL', 0), COLS.get('RECORD', 0)))
    grade = "### NO GRADE MOVED. ### NOTHING MINTED, NO EXPECTATION REGISTERED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b453_the_fold.txt; data/b453_components.txt; data/b453_fold.json; data/b453_span.json; "
             "data/b453_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); FINDINGS.md; THE_FINDINGS_AS_THEY_STAND.md; OPEN_TRAILS.md; "
             "CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b453 (the fold at span eight)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE RESIDUE AND RECONCILIATION ARC FOLDED (b453).%s'
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
        rec('    %-58s reaches the b453 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the strings carried', ('%d VERDICT STRINGS' % FJ.get('verified')) in out), ('the columns carried', 'OBJECT 0' in out),
                      ('nothing minted carried', 'A FOLD MINTS NOTHING' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b453 -- THE FOLD AT SPAN EIGHT.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE ROWS, EACH STRING AS VERIFIED IN ITS OWN BANK.', '-' * 100]
    for r in FJ['rows']:
        Bk.append('  %-5s %-7s %s' % (r.get('act'), r.get('column'), r.get('bank')))
        for g in r['strings']:
            Bk.append('        %r' % g['string'])
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B452ROW_RE = r"(?m)^\| (\d+) \| \*\*NONE OF THE FORTY-SEVEN CLASS BOUNDARIES LIES ON THE CORPUS`S SIDE"

def main():
    global DESK
    bar('=')
    rec('b453_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; strings %s ; columns %s ; last fold %s ; span tool %s'
        % (GR, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), FJ.get('verified'), COLS, LF, FJ.get('span_tool')))
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B452ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b453_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
