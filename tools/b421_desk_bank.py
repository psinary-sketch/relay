# -*- coding: utf-8 -*-
"""b421_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### The trail carries the closing's added line: the
### navigator's three b420 conflations, entered as the navigator's, with the seat's corrections.
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
MARK = '<!-- b421 the finite ambient built, and the span counted -->'
PRIOR = '<!-- b420 the proof cited, the lock ruled, and the lemma aimed at the right object -->'
B420ROW = "**THE BARRIER LEMMA DOES NOT REACH THE ARC'S POSITIVITY ARGUMENT: NOT AN INSTANCE, ON FORM**"
BANKOUT = os.path.join(D, 'b421_the_finite_ambient.txt')
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


FACE = read(os.path.join(D, 'b421_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b421_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
PROBES = read(os.path.join(D, 'b421_c1_probes.txt'))
_b = re.search(r'probes compiled : (\d+) of the sixteen.*?: ([0-9.]+) of 150', PROBES)
NPROBE, MINS = (int(_b.group(1)), _b.group(2)) if _b else (0, '?')

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('the finite ambient -- b420’s part (i)', 'CLOSE',
     'PROVED, ZERO AXIOMS: GridTrace.grid_trace_is_signed_count -- the trace of a grid operator this act defines '
     'equals the model’s counting form. Its docstring says the source’s trace is not this object.'),
    ('the source’s frame carried to the ambient -- b420’s part (ii)', 'STANDING',
     'Not statable in the kernel’s present character; the step from the source’s space to the grid stays b310’s.'),
    ('the specification hypothesis 1 needs', 'CLOSE',
     'PRICED: under Definition 2.1 read as written, NOT SUPPLIABLE for any infinite structure (the upward '
     'Löwenheim-Skolem theorem, the seat’s citation); under the monograph’s definition, writable in (i) and (ii), '
     'unverified in (iii), and not written. No document holds one.'),
    ('which reading of *unique model* the keystone intends', 'STANDING',
     'ROUTED TO THE AUTHOR: read as written, Definition 2.1 is met by no infinite structure, xi’s included; b407 is '
     'not re-verdicted.'),
    ('the fold of b413-b421', 'STANDING', 'NAMED FOR b422 by the tool’s count against (R1)’s NINE; not run.'),
    ('the navigator’s three conflations at b420', 'CLOSE',
     'ENTERED AS THE NAVIGATOR’S, each with the seat’s correction quoted, in the act’s record and the trail.'),
    ('the Reader’s encoding', 'STANDING', 'ROUTED, NOT REPAIRED, as at b416.'),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING', 'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX.'),
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
        '### b421 — the finite ambient built, and the span counted — filed 2026-09-11', '',
        '#### The finite ambient', '',
        '**PROVED, with zero axioms, on the third of the sixteen probes b418’s budget allows.** '
        '`GridTrace.grid_trace_is_signed_count` (`Core/GridTrace.lean`) says that the trace of a grid operator this act '
        'defines — the scaling map read between off-ball points, less its fibre-summed twin — equals the model’s '
        'counting form, `B329.signedTrace`, for every `p ≥ 1`, every level and every `t ≥ 1`. **Its docstring says the '
        'source’s trace is not this object.** The step from the source’s space to the grid is still b310’s, and still '
        'not statable in the kernel’s present character.',
        '',
        '#### The specification hypothesis 1 needs', '',
        'The keystone works in classical first-order logic and asks, at Definition 2.1, for a finite specification with '
        'the structure as its unique model up to isomorphism. **By the upward Löwenheim-Skolem theorem — the seat’s '
        'citation, which the keystone names nowhere — no infinite structure has that property**, so the specification '
        'is not suppliable as written, for the test functions or for `xi`. Which reading of *unique model* the '
        'keystone intends is routed to the author; b407 is not re-verdicted. Under the monograph’s own definition the '
        'specification is writable and has not been written. No document holds one.',
        '',
        '#### The span', '',
        'The tool counts nine acts since the b412 fold with this act, eight without it. Against (R1)’s threshold of '
        'nine, **the fold of b413–b421 is named for b422, and not run.**',
        '',
        '#### The navigator’s three conflations at b420, and their corrections', '',
        '**Entered as the navigator’s, so the next navigator inherits the correction and not the conflation.** '
        '(1) The b420 ferry described b419’s theorem as returning the function at the identity times a dimension; '
        'those are b310’s words for a derived result, and the theorem is a counting identity that mentions no test '
        'function, dimension or sign. (2) It treated the compressed trace as the finite place’s term; the term in the '
        'functional is `W_p`, and b310 says the arithmetic is in the distribution, not in the compressed trace. (3) It '
        'paraphrased the aim map as *no crossing at any height*; the map says *a passed test over a grid at this reach '
        'and nothing more*. In all three the source governs. The full quotations are in relay '
        '`data/b421_conflations.txt`.',
        '',
        '#### The four lists', '',
        FOUR,
        '',
        '#### What this act did not do', '',
        '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of '
        '`FACES_LEDGER.md` written. 0 folds run. 0 rules struck or amended. 0 orientation-layer lines edited. 0 locked '
        'faces edited. 0 prior banks edited. 0 banked ferries edited. 0 existing kernel files edited. 0 deposit '
        'actions, 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A GRID TRACE DEFINED AND PROVED EQUAL TO THE MODEL'S COUNTING FORM, A SPECIFICATION "
         "PRICED UNDER BOTH DEFINITIONS OF DETERMINED, AND A SPAN COUNTED. ### THE SOURCE'S TRACE IS NOT THE OBJECT "
         "PROVED ABOUT; IT MOVES NO GRADE AND DISCHARGES NO PREMISE")


def corr_rows():
    m = ("**THE GRID TRACE DEFINED HERE EQUALS THE MODEL'S COUNTING FORM, ZERO AXIOMS, ON THE THIRD PROBE** "
         "(b421, the finite ambient)")
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b421 -- @GR@ gates "
            "read, @GDG@ checked by digest. **COMPONENT 1: GridTrace.grid_trace_is_signed_count -- FOR EVERY p >= 1, "
            "EVERY n AND EVERY t >= 1, THE TRACE OF THE GRID OPERATOR q A_t - B_t DEFINED IN THIS MODULE EQUALS "
            "B329.signedTrace; THE SOURCE'S TRACE IS NOT THIS OBJECT; @NP@ PROBES, @MI@ MINUTES, NO MATHLIB.** "
            "**COMPONENT 2: HYPOTHESIS 1'S SPECIFICATION NOT SUPPLIABLE UNDER DEFINITION 2.1 AS WRITTEN (THE SEAT'S "
            "CITATION OF THE UPWARD LOWENHEIM-SKOLEM THEOREM), WRITABLE AND UNWRITTEN UNDER THE MONOGRAPH'S; NO "
            "DOCUMENT HOLDS ONE.** **COMPONENT 3: THE SPAN COUNTS 9 WITH THIS ACT, 8 WITHOUT; THE FOLD OF b413-b421 "
            "NAMED FOR b422, NOT RUN.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = ("GridTrace.grid_trace_is_signed_count (NEW, Core/GridTrace.lean) and six helpers -- key, mod_add_iff, "
            "diagA, diagB, trA_eq, trB_eq -- each printing 'does not depend on any axioms'")
    prof = ("### ONE MODULE ADDED; ONE IMPORT LINE INSERTED IN AllPrints.lean AND ITS PRINTS APPENDED; AXIOM_PRINTS.txt "
            "REGENERATED WITH THE PRIOR PROFILE A TRUE BYTE PREFIX; NO EXISTING KERNEL FILE EDITED; NO GRADE, PREMISE, "
            "DOOR, KAPPA, ROUTE, FACES_LEDGER ROW, FOLD OR RULE -- 0 CONTENT LOST")
    grade = ("### THE LEMMA'S SCOPE WAS EXACT AT BIRTH: ITS STATEMENT NAMES BOTH OBJECTS AND ITS DOCSTRING SAYS WHAT IT "
             "IS NOT ABOUT. ### A CLASSICAL THEOREM WAS CITED AS THE SEAT'S AND ITS BEARING ROUTED, NOT RULED")
    status = ("data/b421_the_finite_ambient.txt; data/b421_components.txt; data/b421_c1_probes.txt; data/b421_c1_verify.txt; "
              "data/b421_c2_specification.txt; data/b421_c3_span.txt; data/b421_conflations.txt; "
              "data/b421_registration_2026-09-11.txt (LOCKED at sha256 %s); Core/GridTrace.lean (NEW); AllPrints.lean; "
              "AXIOM_PRINTS.txt; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@NP@', str(NPROBE))
                .replace('@MI@', str(MINS)))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('grid trace signed count', 'the finite ambient built', 'is definition 2.1 satisfiable by an infinite structure',
           'lowenheim skolem determined', 'when is the next fold', 'the navigator conflations at b420')
MUST_NOT_HIT = ('the lock was overridden', 'the source trace is compiled', 'a grade was moved', 'h2 has moved')
KEY = 'the-finite-ambient'


def do_key(rownum):
    statement = (
        "b421 BUILT THE FINITE AMBIENT. **PROVED, ZERO AXIOMS: THE TRACE OF A GRID OPERATOR DEFINED IN THIS ACT EQUALS "
        "THE MODEL'S COUNTING FORM** (GridTrace.grid_trace_is_signed_count), and its docstring says the source's trace "
        "is NOT THE SOURCE'S OBJECT here -- the step from the source's space stays b310's. **HYPOTHESIS 1'S "
        "SPECIFICATION IS NOT SUPPLIABLE UNDER DEFINITION 2.1 AS WRITTEN**: no infinite structure is the unique model "
        "of a first-order theory (upward Lowenheim-Skolem, the seat's citation); the reading is routed. **THE SPAN "
        "COUNTS 9 WITH THIS ACT; THE FOLD OF b413-b421 IS NAMED FOR b422, NOT RUN.** The navigator's three b420 "
        "conflations are entered with their corrections.")
    grade = "### ONE MODULE AND ITS TERMINALS ADDED, NO EXISTING TERMINAL MOVED, NO GRADE MOVED. ### NOTHING DEPOSITS"
    where = ("data/b421_the_finite_ambient.txt; data/b421_c1_probes.txt; data/b421_c2_specification.txt; "
             "data/b421_c3_span.txt; data/b421_conflations.txt; data/b421_registration_2026-09-11.txt (LOCKED, %d "
             "gates read, %d by digest); Core/GridTrace.lean; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b421 (the finite ambient built; the specification priced; the span counted; the conflations entered)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FINITE AMBIENT (b421).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b421 key : %s' % (qq[:58], g2))
    for lbl, cond in (('proved, zero axioms', 'PROVED, ZERO AXIOMS' in out),
                      ('not the source`s object', "NOT THE SOURCE'S OBJECT" in out),
                      ('not suppliable', 'NOT SUPPLIABLE' in out),
                      ('fold for b422', 'NAMED FOR b422' in out)):
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
    B = ['=' * 100, 'b421 -- THE FINITE AMBIENT BUILT, AND THE SPAN COUNTED.', 'THE BANK.', '=' * 100, '']
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
    rec('b421_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not _b:
        rec('  ### HARD FAILURE -- the lock gate`s record or the probes` budget line is missing.')
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
    rec('  b420`s row by its marker : %s' % at(B420ROW, txt))
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
    rec('  after -- b420`s : %s ; this act`s, by its marker : %s' % (at(B420ROW, after), at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b421_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
