# -*- coding: utf-8 -*-
"""b423_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### The verdicts are read off the component's record, never
### typed here; the seat's reading of §10.2 is routed to the author with a trigger, so it is not shelved (R23).
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
MARK = '<!-- b423 the (R37) question read: b407 and b420 against section 10.2 -->'
PRIOR = '<!-- b422 the fold of the kernel arc, and the witness arc named -->'
B422ROW = "**THE KERNEL ARC FOLDED: TWO COMPILED GENERAL THEOREMS ABOUT THE MODEL, AND THE KEYSTONE'S DEFINITION 2.1"
BANKOUT = os.path.join(D, 'b423_the_r37_question_read.txt')
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


FACE = read(os.path.join(D, 'b423_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b423_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
QREC = read(os.path.join(D, 'b423_r37_question.txt'))


def verdict(who):
    ln = next((x for x in QREC.splitlines() if ('VERDICT ON %s`S READING :' % who) in x), '')
    return ln.rsplit(':', 1)[-1].strip() if ln else ''


V407, V420 = verdict('b407'), verdict('b420')

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('whether b407’s and b420’s readings move under (R37)', 'CLOSE',
     'READ at b423: b407’s %s, b420’s %s, each with its deciding sentence; both verdicts rest on hypothesis 5 and '
     'neither is re-verdicted.' % (V407, V420)),
    ('the seat’s reading: under (R37) hypothesis 1 separates no written structure', 'STANDING',
     'ROUTED TO THE AUTHOR AND NOT RULED; trigger: the author rules on it. The keystone is not edited.'),
    ('b421’s price NOT SUPPLIABLE for the test-function structure', 'STANDING',
     'LAPSES UNDER (R37) as a ground: suppliable and not written. b421 is not re-verdicted; its record is unedited.'),
    ('W-ORD-WITNESS-ENUMERATION', 'STANDING', 'OPENED BY THE AUTHOR’S WORD; site (i) is this sortie’s leg 2, b424.'),
    ('the falsifier read', 'STANDING', 'This sortie’s leg 3, b425.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('b420’s sentence that b419 moved a grade inside K3', 'STANDING', 'NAMED IN THE FOLD, NOT REPAIRED, as at b422.'),
    ('the Reader’s encoding; §9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING',
     'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; its witness column is leg 2’s.'),
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
        '### b423 — the (R37) question read, sortie leg 1 — filed 2026-09-11', '',
        '#### The two readings of the lemma’s first hypothesis, each against §10.2', '',
        '**b407’s reading — `ξ` is determined — %s.** Deciding sentence, §10.2: *“the specification is a set-theoretic '
        'definition and uniqueness is a statement inside the ambient theory, which is how the natural numbers, the reals '
        'and ξ are characterized in practice.”* The monograph writes the definition (θ, then the Mellin transform).' % V407,
        '',
        '**b420’s reading — for the structure whose elements are the class’s test functions, hypothesis 1 is NOT '
        'SUPPLIED BY THE RECORD — %s.** Under the internal reading the specification is a set-theoretic definition; the '
        'source defines its pieces with `F` left free (*“a finite set disjoint from Z and containing {0,1}”*), and no '
        'document writes it (b421’s count, 0, and this act’s search, every hit hand-read). **What lapses is b421’s extra '
        'ground:** under the first-order reading the specification was not suppliable; under the internal reading it is '
        'suppliable and not written.' % V420,
        '',
        '**Neither verdict moves, and nobody is re-verdicted:** both rest on hypothesis 5, the proof’s form.',
        '',
        '#### Routed to the author, not ruled', '',
        '**The seat’s reading of §10.2:** read internally, a structure given by an explicit set-theoretic definition is '
        'unique inside ZFC, so hypothesis 1 is met by any structure once its definition is written and no longer '
        'separates one structure from another; whether the lemma applies to anything the witness arc meets then turns on '
        'the fifth hypothesis, which failed at b407 and at b420 on form. Trigger: the author rules on it. The keystone '
        'is not edited.',
        '',
        '#### The sortie', '',
        '**W-ORD-WITNESS-ENUMERATION is opened by the author’s word.** Leg 2 (b424) runs site (i), the clause’s '
        'quantifier over the class, checkpointed after the site; leg 3 (b425) reads the falsifier. Each leg is locked and '
        'closed as its own act.',
        '',
        '#### The four lists', '',
        FOUR,
        '',
        '#### What this act did not do', '',
        '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of '
        '`FACES_LEDGER.md` written. 0 re-verdicts. 0 keystone bytes. 0 rules struck or amended. 0 orientation-layer lines '
        'edited. 0 locked faces edited. 0 prior banks edited. 0 banked ferries edited. 0 kernel files touched. 0 '
        'deposit actions, 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS TWO READINGS OF THE LEMMA'S FIRST HYPOTHESIS READ AGAINST THE AUTHOR'S RULING, AND A "
         "READING ROUTED. ### IT RE-VERDICTS NO ACT, MOVES NO GRADE AND TOUCHES NO KERNEL OR KEYSTONE")


def corr_rows():
    m = ("**THE (R37) QUESTION READ: b407'S AND b420'S READINGS OF THE LEMMA'S FIRST HYPOTHESIS, EACH AGAINST §10.2** "
         "(b423, sortie leg 1)")
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b423 -- @GR@ gates "
            "read, @GDG@ checked by digest. **b407'S READING (xi DETERMINED): @V407@** -- deciding sentence §10.2's "
            "own, which names xi. **b420'S READING (NOT SUPPLIED BY THE RECORD): @V420@** -- under the internal reading "
            "the specification is a set-theoretic definition the source's pieces would make with F fixed, and no "
            "document writes it; b421's NOT SUPPLIABLE lapses as a ground. **BOTH VERDICTS REST ON HYPOTHESIS 5; 0 "
            "RE-VERDICTS.** **ROUTED: UNDER (R37) HYPOTHESIS 1 SEPARATES NO WRITTEN STRUCTURE.** 0 GRADES MOVED, 0 "
            "PREMISES DISCHARGED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. The keystone's §10.2 and Theorem 3.1 are read, not edited"
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX; NO KERNEL FILE; NO KEYSTONE "
            "BYTE; NO GRADE, PREMISE, DOOR, KAPPA, ROUTE, FACES_LEDGER ROW OR RULE -- 0 CONTENT LOST")
    grade = ("### EACH READING WAS SCORED BY WHETHER ITS OWN STATED CONCLUSION STANDS, AND A LAPSED GROUND WAS NAMED "
             "APART FROM THE CONCLUSION IT HAD SUPPORTED")
    status = ("data/b423_the_r37_question_read.txt; data/b423_r37_question.txt; data/b423_components.txt; "
              "data/b423_registration_2026-09-11.txt (LOCKED at sha256 %s); PLACE-papers OPEN_TRAILS.md; "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@V407@', V407)
                .replace('@V420@', V420))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the r37 question read', 'do b407 and b420 move under r37', 'hypothesis 1 under the internal reading',
           'sieve ceiling lemma first hypothesis', 'b423 sortie leg 1')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-r37-question-read'


def do_key(rownum):
    statement = (
        "b423 READ b407'S AND b420'S READINGS OF THE SIEVE CEILING LEMMA'S FIRST HYPOTHESIS AGAINST (R37), THE KEYSTONE'S "
        "§10.2. **b407'S (xi DETERMINED): %s. b420'S (NOT SUPPLIED BY THE RECORD, FOR THE TEST-FUNCTION STRUCTURE): %s** "
        "-- suppliable under the internal reading and not written; b421's NOT SUPPLIABLE lapses as a ground. Both "
        "verdicts rest on hypothesis 5; not re-verdicted. **ROUTED: UNDER (R37) HYPOTHESIS 1 SEPARATES NO WRITTEN "
        "STRUCTURE.**" % (V407, V420))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b423_the_r37_question_read.txt; data/b423_r37_question.txt; data/b423_registration_2026-09-11.txt "
             "(LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b423 (sortie leg 1: the (R37) question read)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE (R37) QUESTION READ (b423).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b423 key : %s' % (qq[:58], g2))
    for lbl, cond in (('b407 verdict carried', ("b407'S (xi DETERMINED): %s" % V407) in out),
                      ('b420 verdict carried', ('%s**' % V420) in out),
                      ('not re-verdicted', 'not re-verdicted' in out),
                      ('routed', 'ROUTED' in out)):
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
    B = ['=' * 100, 'b423 -- THE (R37) QUESTION READ. SORTIE LEG 1.', 'THE BANK.', '=' * 100, '']
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
    rec('b423_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or V407 not in ('CONFIRMED', 'MOVED') or V420 not in ('CONFIRMED', 'MOVED'):
        rec('  ### HARD FAILURE -- the lock gate`s record or a verdict line of the component`s record is missing.')
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
    rec('  b422`s row by its marker : %s' % at(B422ROW, txt))
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
    rec('  after -- b422`s : %s ; this act`s, by its marker : %s' % (at(B422ROW, after), at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b423_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
