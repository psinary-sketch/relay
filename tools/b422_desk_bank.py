# -*- coding: utf-8 -*-
"""b422_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### The trail names the witness arc as a work item with a
### trigger (the author's word), enters its class site's opening list verbatim, and names the question (R37) left
### for a later act -- so neither is shelved under (R23).
"""
import io
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
MARK = '<!-- b422 the fold of the kernel arc, and the witness arc named -->'
PRIOR = '<!-- b421 the finite ambient built, and the span counted -->'
B421ROW = "**THE GRID TRACE DEFINED HERE EQUALS THE MODEL'S COUNTING FORM, ZERO AXIOMS, ON THE THIRD PROBE**"
BANKOUT = os.path.join(D, 'b422_the_kernel_arc_folded.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


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


FACE = read(os.path.join(D, 'b422_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b422_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
FERRY = read(os.path.join(D, 'b422_ferry.txt'))
_o = re.search(r'The\s+navigator\'s first-draft enumeration for the class site\s+—\s+(.*?)\s+—\s+is entered', FERRY, re.S)
OPENING = re.sub(r'\s+', ' ', _o.group(1)) if _o else ''

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('which reading of *unique model* the keystone intends', 'CLOSE',
     'RULED BY THE AUTHOR, (R37): internally to ZFC. Executed as the keystone’s §10.2, appended; Definition 2.1 kept.'),
    ('whether b407’s and b420’s verdicts move under (R37)', 'STANDING',
     'NAMED FOR A LATER ACT AND NOT RUN, as the ruling says.'),
    ('the fold of b413-b421', 'CLOSE',
     'FILED as THE KERNEL ARC in FINDINGS.md; F-NOGRADE and F-NOSUPERSEDE at 0 before the write; the orientation '
     'layer refreshed under (R31), no door restated.'),
    ('b420’s sentence that b419 moved a grade inside K3', 'STANDING',
     'NAMED IN THE FOLD, NOT REPAIRED: b419’s bank and row S1 say no grade moved; b420’s bank is not edited.'),
    ('the witness enumeration', 'STANDING',
     'NAMED AS THE NEXT ARC AND NOT OPENED: one act per site, six sites, checkpointed; site (i)’s opening list entered '
     'verbatim; trigger: the author’s word.'),
    ('the navigator’s three conflations at b420', 'CLOSE', 'CARRIED into the fold’s own section as the navigator’s, with their corrections.'),
    ('the one-statements of the ten earlier folds', 'STANDING', 'ROUTED at b412, unchanged.'),
    ('the Reader’s encoding', 'STANDING', 'ROUTED, NOT REPAIRED, as at b416.'),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING', 'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; its witness column read, not written.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1600], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**' % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    return [
        '', MARK, '',
        '### b422 — the fold of the kernel arc, and the witness arc named — filed 2026-09-11', '',
        '#### (R37), executed', '',
        '**The author’s ruling: the barrier keystone’s *unique model up to isomorphism* is read internally to ZFC.** '
        '`INVARIANCE_BARRIERS.md` carries it as an appended §10.2; Definition 2.1’s sentence is kept, and the '
        'first-order reading it declines is recorded beside it with the Löwenheim–Skolem citation (the seat’s, b421). '
        '**Named for a later act and not run:** whether b407’s and b420’s verdicts move under the internal reading. '
        'Trigger: the author orders that act.',
        '',
        '#### The fold', '',
        '**THE KERNEL ARC, b413–b421, is folded into `FINDINGS.md`.** Its product is two compiled general theorems, '
        'both about the model of the object at a finite place — `SmearGeneral.smear_general` and '
        '`GridTrace.grid_trace_is_signed_count`. Its largest finding about the record is the keystone’s Definition 2.1. '
        'Counted by b412’s measure: 0 statements about the object, 5 about the record, and a third column, declared '
        'before the count, of 3 compiled and 1 measured statements about the object’s model. The orientation layer '
        'is refreshed under (R31), and no door is restated.',
        '',
        '#### W-ORD-WITNESS-ENUMERATION — named, not opened', '',
        '**The next arc, one act per site of row U1, checkpointed after each:** enumerate every candidate shared witness '
        'for the site from the record and the literature by description, attempt each under a cap, and fail each at a '
        'quoted step or hold it. Its product is a witness column that reads, at every site, either a witness or the '
        'exhausted candidate list with each failure’s location. **Priced at six acts, for six sites.** **Trigger: the '
        'author’s word opens it.** The column today reads `NONE KNOWN` or `UNSTATED` at every site. **The opening list '
        'for site (i), the clause’s quantifier, entered as the navigator’s and nothing more:** %s.' % OPENING,
        '',
        '#### The four lists', '',
        FOUR,
        '',
        '#### What this act did not do', '',
        '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of '
        '`FACES_LEDGER.md` written. 0 witness candidates attempted. 0 rules struck or amended. 0 orientation-layer lines '
        'edited. 0 locked faces edited. 0 prior banks edited. 0 banked ferries edited. 0 kernel files touched. 0 '
        'deposit actions, 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A FOLD FILED, A KEYSTONE ANNOTATED UNDER THE AUTHOR'S RULING, THE ORIENTATION LAYER "
         "REFRESHED, AND AN ARC NAMED AND NOT OPENED. ### IT MOVES NO GRADE, DISCHARGES NO PREMISE AND TOUCHES NO KERNEL")


def corr_rows():
    m = ("**THE KERNEL ARC FOLDED: TWO COMPILED GENERAL THEOREMS ABOUT THE MODEL, AND THE KEYSTONE'S DEFINITION 2.1 "
         "RULED** (b422, the fold)")
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b422 -- @GR@ gates "
            "read, @GDG@ checked by digest. **(R37) EXECUTED: INVARIANCE_BARRIERS.md §10.2 APPENDED -- UNIQUE MODEL READ "
            "INTERNALLY TO ZFC, DEFINITION 2.1 KEPT, THE FIRST-ORDER READING RECORDED AS DECLINED; b407 AND b420 NOT "
            "RE-VERDICTED.** **COMPONENT 1: THE KERNEL ARC, b413-b421, FOLDED INTO FINDINGS.md; F-NOGRADE AND "
            "F-NOSUPERSEDE AT 0; OBJECT 0, RECORD 5, OBJECT-MODEL 3 COMPILED AND 1 MEASURED; THE ORIENTATION LAYER "
            "REFRESHED, NO DOOR RESTATED.** **COMPONENT 2: THE THREE CONFLATIONS CARRIED.** **THE WITNESS ARC NAMED, "
            "PRICED AT SIX ACTS, NOT OPENED.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. The fold names SmearGeneral.smear_general and GridTrace.grid_trace_is_signed_count"
    prof = ("### FOUR PLACE-papers FILES APPENDED -- FINDINGS.md, THE_FINDINGS_AS_THEY_STAND.md, PATHS_TO_THE_CRITICAL_"
            "LINE.md, INVARIANCE_BARRIERS.md -- EACH PIN A TRUE PREFIX; NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, "
            "ROUTE, FACES_LEDGER ROW OR RULE -- 0 CONTENT LOST")
    grade = ("### THE COUNT USED THE LAST FOLD'S CRITERION, QUOTED, AND NAMED A NEW COLUMN RATHER THAN BENDING IT. ### "
             "A SENTENCE OF A PRIOR RECORD THAT SAYS A GRADE MOVED WAS NAMED, NOT REPAIRED")
    status = ("data/b422_the_kernel_arc_folded.txt; data/b422_components.txt; data/b422_fold.txt; data/b422_r37.txt; "
              "data/b422_orient.txt; data/b422_witness_arc.txt; data/b422_registration_2026-09-11.txt (LOCKED at sha256 "
              "%s); PLACE-papers FINDINGS.md, THE_FINDINGS_AS_THEY_STAND.md, PATHS_TO_THE_CRITICAL_LINE.md, "
              "INVARIANCE_BARRIERS.md, OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the kernel arc folded', 'fold of b413 to b421', 'unique model internally to zfc', 'r37 definition 2.1 ruling',
           'the witness enumeration arc', 'what did the kernel arc produce')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-kernel-arc-folded'


def do_key(rownum):
    statement = (
        "b422 FOLDED THE KERNEL ARC, b413-b421. **ITS PRODUCT IS TWO COMPILED GENERAL THEOREMS ABOUT THE MODEL OF THE "
        "OBJECT AT A FINITE PLACE** (SmearGeneral.smear_general, GridTrace.grid_trace_is_signed_count); by b412's "
        "measure 0 statements about the object as written, with a third column named. **(R37): THE KEYSTONE'S UNIQUE "
        "MODEL READ INTERNALLY TO ZFC**, appended as §10.2, Definition 2.1 kept; b407 and b420 not re-verdicted. **THE "
        "WITNESS ARC IS NAMED, SIX ACTS, NOT OPENED**; the orientation layer refreshed and no door restated.")
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b422_the_kernel_arc_folded.txt; data/b422_fold.txt; data/b422_r37.txt; data/b422_orient.txt; "
             "data/b422_witness_arc.txt; data/b422_registration_2026-09-11.txt (LOCKED, %d gates read, %d by digest); "
             "FINDINGS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b422 (the kernel arc folded; R37 executed; the orientation layer refreshed; the witness arc named)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE KERNEL ARC FOLDED (b422).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-58s reaches the b422 key : %s' % (qq[:58], g2))
    for lbl, cond in (('two compiled general theorems', 'TWO COMPILED GENERAL THEOREMS' in out),
                      ('internally to zfc', 'INTERNALLY TO ZFC' in out),
                      ('not opened', 'NOT OPENED' in out),
                      ('not re-verdicted', 'not re-verdicted' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    B = ['=' * 100, 'b422 -- THE FOLD OF THE KERNEL ARC, AND THE WITNESS ARC NAMED.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b422_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not OPENING:
        rec('  ### HARD FAILURE -- the lock gate`s record or the ferry`s opening list is missing.')
        return 1
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
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
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
    at = lambda mk, s: [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b421`s row by its marker : %s' % at(B421ROW, txt))
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
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- b421`s : %s ; this act`s, by its marker : %s' % (at(B421ROW, after), at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b422_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
