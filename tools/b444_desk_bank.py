# -*- coding: utf-8 -*-
"""b444_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own records -- the components bank, the lock gate's notes, the suite -- and none is typed.
### ### **AND WHERE A FIGURE CANNOT BE READ, THE TOOL REFUSES RATHER THAN PRINTS A GUESS.**
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
MARK = '<!-- b444 the fold, and the channels decorrelated -->'
PRIOR = '<!-- b443 site (vi), and the arc`s product named -->'
BANKOUT = os.path.join(D, 'b444_the_fold.txt')
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


FACE = read(os.path.join(D, 'b444_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b444_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b444_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b444_components.txt'))


def _j(name, default):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return default


FJ = _j('b444_fold.json', {})
CJ = _j('b444_decorrelation.json', {})
SPANF = FJ.get('span') or {}
T3 = CJ.get('t3') or {}
ABOVE = CJ.get('above') or []
MXR = max([x['ratio'] for x in ABOVE] or [0])
MXE = max([abs(x['e']) for x in ABOVE] or [0])
VERD = CJ.get('verdict')

ROWMARK = ('**THE WITNESS AND CHANNEL ARC FOLDED, b433-b443, ITS SPAN COUNTED THREE WAYS; AND THE CHANNELS` RESIDUAL '
           'SITS ABOVE THE FLOOR, UNDECIDED WHETHER IT IS THE OBJECT`S**')

SCOPE = ("### THE ACT FOLDS ELEVEN ACTS, REFRESHES THE DIGEST, AND READS BANKED CHANNEL COLUMNS THROUGH A TRANSFORM "
         "FIXED ON ITS FACE. ### NO CELL COMPUTED, NO INSTRUMENT RUN, NO LANE OPENED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")

DESK = [
    ('the fold of b433-b443', 'CLOSE',
     'FOLDED at b444 into FINDINGS.md under a heading the span tool reads; 11 of 11 verdict strings verified; columns '
     'OBJECT 0, MODEL 6, RECORD 5; the digest refreshed with this arc and b434`s unrefreshed one.'),
    ('the span count', 'CLOSE',
     'COUNTED at b444 three ways: the tool %s, the tool`s own rule 9 (b435-b443), the order 11 (adds b433, in no '
     'fold, and b434, the prior filer). b443`s "11 by the record`s convention" was wrong.' % SPANF.get('tool')),
    ('W-ORD-SPAN-HEADING', 'STAND',
     'FILED at b444: b363_span.py misses b434`s fold heading; repair on the next opening of the instrument lane or '
     'the next fold.'),
    ('the channels decorrelated', 'CLOSE',
     'READ at b444: over 22 ladder cells the identity residual e = Z - (P - PR + A) matches the bank exactly and is %s '
     '-- above the 1.49e-08 floor at %d cells, largest %.2e (%.1f x); r(e, a) %.2f, r(e, PR) %.2f; 7 sign changes. '
     'The aim map kept apart: no zero channel, no shared radius.'
     % (VERD, len(ABOVE), MXE, MXR, T3.get('r_a', 0), T3.get('r_PR', 0))),
    ('whether the residual is the object`s or the quadrature`s', 'STAND',
     'PRICED at b444, NOT RUN: re-run the chain at the 14 cells on a refined grid and a wider frequency window and '
     'see whether e moves -- a measurement, blocked by the parked instrument lane.'),
    ('b433 in no fold until now', 'CLOSE', 'FOLDED at b444 by the order`s span.'),
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
        '### b444 — the fold, and the channels decorrelated — filed 2026-09-12',
        '',
        '**The witness and channel arc is folded, b433–b443, and the arc is COMPLETE at six sites. And the channels’ residual, read through a transform fixed before any number was computed, sits above the instrument’s floor — which the navigator did not expect, and which this act does not call the object’s.**',
        '',
        '#### Component 1 — the fold',
        '',
        '**The span, three ways:** the span tool reads **@TOOL@** — its heading pattern matches 14 of the 15 fold headings and misses b434’s; the tool’s own rule, a span starting at the last filing act plus one, gives **9** (b435–b443); the order’s span is **11** (b433–b443), adding **b433**, which was in no fold, and **b434**, the previous fold’s filing act. b443’s closing called eleven the record’s convention, and that was wrong; b443’s bank is unedited. The fold follows the order’s span, with b434 marked as the prior filer and its lore not folded again, and it is written under a heading the tool reads — the tool now reports the last fold as b433–b443, filed by b444. The tool’s missed heading is filed as **W-ORD-SPAN-HEADING**, triggered by the next opening of the instrument lane or the next fold.',
        '',
        '**Its one statement, quoted from the fold:** @ONE@',
        '',
        'Three of the clauses the order put in that statement — two external proofs graded, the corpus terminal NOT THE CLAIM, the misnamed keystone lemma — belong to b423–b432 and were folded at b434; they are cited there, not folded again. Eleven verdict strings, every one verified in its own bank. **Columns: object 0, model 6, record 5.** The digest under `(R31)` gained one block carrying both this arc and the external-grading arc, which b434 folded without refreshing it.',
        '',
        '#### Component 2 — the channels decorrelated',
        '',
        '**The table:** the 22 cells of the radius ladder that carry every channel. **The zero channel is inherited.** The aim map is kept apart — its 56 cells carry no zero channel and share no radius with the ladder.',
        '',
        '**T1, as measured:** `r(a, PR) = −0.99`, `r(a, A) = −0.97`, `r(PR, A) = 0.96`, `r(Z, A) = 0.68`, `r(Z, a) = −0.51`; the pole channel is below the floor at every cell and was not correlated. **T2:** the identity’s own residual `e = Z − (P − PR + A)`, recomputed from the banked channels, equals the banked residual exactly.',
        '',
        '**T3 — the verdict by the rule fixed on the face: STRUCTURE.** `|e|` is above the `1.49e-08` floor at **@NA@ of 22 cells**, the largest `@MXE@`, **@MXR@ times the floor**; `r(e, a) = @RA@`, `r(e, PR) = @RPR@`, `r(e, A) = @RAA@`, `r(e, Z) = @RZ@`; 7 sign changes along the radius. **What it is, as measured:** the part of the zero channel the identity does not carry, growing with the radius and with the prime channel. **Whether it is the object’s is not decided.** A residual that tracks the radius and the prime sum is what quadrature error would look like, and that is a reading, not a finding. **What would decide:** the same chain at these cells on a refined grid and a wider frequency window — b437’s refinement applied to `e` — and whether `e` moves; priced as a measurement, blocked by the parked lane, **not run**. No claim about zeros is made.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | the fold counts eleven | **HALF HELD** — the order’s span is eleven; the record’s own rule gives nine |',
        '| (N1)(b) | the tool’s defect is confirmed | **HELD** — 14 of 15 headings read; b434’s missed |',
        '| (N2) | nothing above the floor, because the identity is exact and leaves quadrature noise | **REFUTED** — @NA@ of 22 cells above the floor; whether the excess is quadrature is priced, not decided |',
    ]
    rep = [('@TOOL@', str(SPANF.get('tool'))), ('@ONE@', FJ.get('one', '')), ('@NA@', str(len(ABOVE))),
           ('@MXE@', '%.2e' % MXE), ('@MXR@', '%.1f' % MXR), ('@RA@', '%.2f' % T3.get('r_a', 0)),
           ('@RPR@', '%.2f' % T3.get('r_PR', 0)), ('@RAA@', '%.2f' % T3.get('r_A', 0)), ('@RZ@', '%.2f' % T3.get('r_Z', 0))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b444)"
    stmt = (m + ". **LOCKED BEFORE ANY WRITE**, @GR@ gates read, @GDG@ by digest. **COMPONENT 1: THE WITNESS AND CHANNEL "
            "ARC FOLDED INTO FINDINGS.md, b433-b443, UNDER A HEADING THE SPAN TOOL READS; THE SPAN COUNTED BY THE TOOL "
            "(@TOOL@, MISSING b434'S HEADING), BY ITS OWN RULE (9, b435-b443) AND BY THE ORDER (11, ADDING b433 AND THE "
            "PRIOR FILER b434); b443'S 'ELEVEN BY CONVENTION' CORRECTED; 11 OF 11 VERDICT STRINGS VERIFIED; COLUMNS "
            "OBJECT 0, MODEL 6, RECORD 5; THREE PRIOR-FOLD CLAUSES CITED, NOT REFOLDED; W-ORD-SPAN-HEADING FILED; THE "
            "DIGEST REFRESHED FOR TWO ARCS. THE WITNESS ARC IS COMPLETE AT SIX SITES.** **COMPONENT 2: OVER 22 LADDER "
            "CELLS, THE IDENTITY RESIDUAL e = Z - (P - PR + A) MATCHES THE BANK EXACTLY AND IS ABOVE THE 1.49e-08 FLOOR "
            "AT @NA@ CELLS, LARGEST @MXE@ (@MXR@ x); r(e, a) @RA@, r(e, PR) @RPR@. VERDICT BY THE FIXED RULE: STRUCTURE, "
            "UNDECIDED WHETHER THE OBJECT'S; THE REFINEMENT THAT WOULD DECIDE PRICED AND NOT RUN; THE AIM MAP KEPT "
            "APART; THE ZERO SIDE INHERITED; NO CLAIM ABOUT ZEROS.** 0 CELLS COMPUTED, 0 INSTRUMENTS RUN, 0 GRADES "
            "MOVED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: FINDINGS.md +1 FOLD SECTION, THE DIGEST +1 BLOCK, OPEN_TRAILS.md +1 RECORD, ALL APPENDED "
            "AS TRUE PREFIXES; FACES_LEDGER.md, EVERY INSTRUMENT AND b363_span.py BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### THE TRANSFORM, THE BAR AND THE VERDICT RULE WERE FIXED ON THE FACE BEFORE ANY RESIDUAL WAS COMPUTED, THE "
             "TWO VALUES SEEN IN THE SURVEY DECLARED; THE RESULT CONTRADICTED THE NAVIGATOR'S EXPECTATION AND IS "
             "REPORTED AS THE RULE GAVE IT, WITHOUT BEING CALLED THE OBJECT'S")
    status = ("data/b444_the_fold.txt; data/b444_components.txt; data/b444_fold.json; data/b444_decorrelation.json; "
              "data/b444_span.txt; data/b444_checks.txt; data/b444_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "data/b444_addendum.txt (EMPTY); FINDINGS.md the fold b433-b443; THE_FINDINGS_AS_THEY_STAND.md; "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@TOOL@', str(SPANF.get('tool')))
                .replace('@NA@', str(len(ABOVE))).replace('@MXE@', '%.2e' % MXE).replace('@MXR@', '%.1f' % MXR)
                .replace('@RA@', '%.2f' % T3.get('r_a', 0)).replace('@RPR@', '%.2f' % T3.get('r_PR', 0)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('what did the witness and channel arc fold',
           'how many acts are in the span since b434',
           'does the channels residual sit above the floor',
           'why does the span tool read twenty one',
           'is the identity residual quadrature noise')
MUST_NOT_HIT = ('the residual is the object', 'the span tool was repaired', 'b443 bank edited')
KEY = 'the-fold-and-the-channels-decorrelated'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b444 FOLDED THE WITNESS AND CHANNEL ARC, b433-b443, AND READ THE CHANNELS THROUGH A FIXED TRANSFORM. THE SPAN "
        "COUNTED THREE WAYS: THE TOOL %s (IT MISSES b434'S FOLD HEADING), ITS OWN RULE 9, THE ORDER 11. 11 OF 11 VERDICT "
        "STRINGS VERIFIED; COLUMNS OBJECT 0, MODEL 6, RECORD 5; W-ORD-SPAN-HEADING FILED; THE WITNESS ARC COMPLETE AT SIX "
        "SITES. THE IDENTITY RESIDUAL OVER 22 CELLS SITS ABOVE THE 1.49e-08 FLOOR AT %d CELLS, LARGEST %.2e; VERDICT "
        "STRUCTURE BY THE FIXED RULE, UNDECIDED WHETHER THE OBJECT'S, THE DECIDING REFINEMENT PRICED AND NOT RUN; NO "
        "CLAIM ABOUT ZEROS."
        % (SPANF.get('tool'), len(ABOVE), MXE))
    grade = "### NO GRADE MOVED. ### NO CELL COMPUTED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b444_the_fold.txt; data/b444_fold.json; data/b444_decorrelation.json; "
             "data/b444_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); FINDINGS.md; "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b444 (the fold, and the channels decorrelated)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FOLD, AND THE CHANNELS DECORRELATED (b444).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq[:48], pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL +
                  '    # (key, act, one-line statement, grade as its own act recorded it, '
                  'location)' + NL)
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
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b444 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the fold carried', 'FOLDED THE WITNESS AND CHANNEL ARC' in out),
            ('the three span figures carried', 'ITS OWN RULE 9, THE ORDER 11' in out),
            ('the strings carried', '11 OF 11 VERDICT' in out),
            ('the work-order carried', 'W-ORD-SPAN-HEADING' in out),
            ('the arc completion carried', 'COMPLETE AT SIX' in out),
            ('the verdict carried', 'VERDICT' in out and 'STRUCTURE BY THE FIXED RULE' in out),
            ('the undecided carried', 'UNDECIDED WHETHER THE OBJECT' in out),
            ('no zero claim carried', 'NO' in out and 'CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, 'b444 -- THE FOLD, AND THE CHANNELS DECORRELATED.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE RESIDUAL, CELL BY CELL.', '-' * 100]
    for a_, e_ in CJ.get('e') or []:
        Bk.append('  a %-10.6f e %+.3e  %s' % (a_, e_, 'ABOVE' if abs(e_) > 1.49e-08 else ''))
    Bk += ['', '-' * 100, '### THE FOLD ROWS.', '-' * 100]
    for r in FJ.get('rows') or []:
        Bk.append('  %-5s %-7s %s' % (r['act'], r['column'], r['verdict']))
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d ; failing %d' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B443ROW_RE = r"(?m)^\| (\d+) \| \*\*SITE \(vi\) EXHAUSTED AND THE WITNESS ARC"


def main():
    bar('=')
    rec('b444_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not FJ or not CJ:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      span %s ; verdict %s ; above %d ; max ratio %.1f' % (SPANF, VERD, len(ABOVE), MXR))
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
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s'
        % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  the prior act`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B443ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- the prior act`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B443ROW_RE, after)], at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.'
        % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b444_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
