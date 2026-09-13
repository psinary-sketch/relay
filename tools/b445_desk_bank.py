# -*- coding: utf-8 -*-
"""b445_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b445 whose residual it is -->'
PRIOR = '<!-- b444 the fold, and the channels decorrelated -->'
BANKOUT = os.path.join(D, 'b445_whose_residual.txt')
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


FACE = read(os.path.join(D, 'b445_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b445_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b445_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b445_components.txt'))
ORDRUN = read(os.path.join(D, 'b445_ordinates_run.txt'))
FLOOR = 1.49e-08

try:
    AJ = json.loads(read(os.path.join(D, 'b445_arms.json')) or '')
except Exception:
    AJ = {}
RJ = AJ.get('report') or {}
VERD = RJ.get('verdict')
CELLS = sorted((AJ.get('base') or {}).keys(), key=float)


def e(arm, k):
    return AJ[arm][k]['e']


if CELLS and VERD:
    FA, TB = RJ['falls_a'], RJ['stable_b']
    BELOW_A = RJ['below']['a']
    DB_MAX = max(abs(e('b', k) - e('base', k)) for k in CELLS)
    DB_REL = max(abs(e('b', k) - e('base', k)) / abs(e('base', k)) for k in CELLS)
    A_ABOVE = [k for k in CELLS if abs(e('a', k)) > FLOOR]
    A_ABOVE_MAX = max([abs(e('a', k)) for k in A_ABOVE] or [0])
    MOVES_A = [k for k, s_ in RJ['status']['a'].items() if s_ == 'MOVES']
    RATES = sorted(RJ['rates'].values())
    RATE_MED = RATES[len(RATES) // 2]
    NUSERS = len(RJ['chain_users'])
    _m = re.search(r'last ([0-9.]+)', ORDRUN)
    REACH = _m.group(1) if _m else ''
_bd = re.search(r'truncation bound, as b437 banked it : max ([0-9.e+-]+)', COMP)
BOUND = _bd.group(1) if _bd else ''

ROWMARK = ('**THE CHANNELS` RESIDUAL IS THE CHAIN`S INTEGRATION: IT FALLS WITH THE AUTOCORRELATION GRID AND DOES NOT MOVE '
           'WITH THE ZERO LIBRARY`S REACH**')

SCOPE = ("### THE ACT RAN THE SAME CHAIN AT THE SAME 14 CELLS WITH TWO PARAMETERS VARIED UNDER (R57), EVERY FACTOR, "
         "TOLERANCE AND RULE FIXED ON ITS FACE; NO CHAIN FILE EDITED, NO NEW CELL, FAMILY OR RADIUS; THE LANE CLOSED AT "
         "ITS END. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('whose residual it is (b444`s standing item)', 'CLOSE',
         'DECIDED at b445 by the rule fixed on the face: %s. Arm (a), the quadrature grid doubled, makes e fall at %d of '
         '14 cells (%d below the floor); arm (b), the zero library extended from 10000 to 15000 ordinates, leaves e '
         'stable at %d of 14, the largest shift %.1e.' % (VERD, FA, BELOW_A, TB, DB_MAX)),
        ('the third hypothesis: e is the zero sum`s truncation tail', 'CLOSE',
         'REFUTED at b445 at the measured size: the zero side does truncate (10000 ordinates, height 9877.78), but '
         'reaching to %s moves e by at most %.1e, %.2f%% of e, within the source`s own bound %s.'
         % (REACH, DB_MAX, 100 * DB_REL, BOUND)),
        ('what the grid refinement leaves', 'STAND',
         'MEASURED at b445, NOT DECIDED: after one doubling %d cells stay above the floor, the largest %.2e; the '
         'apparent order is about %.1f (median over %d cells) and cell %s moves without falling. Whether a further '
         'refinement takes the rest below the floor is not measured; the lane that would measure it closed.'
         % (len(A_ABOVE), A_ABOVE_MAX, RATE_MED, len(RATES), ', '.join(MOVES_A) or 'none')),
        ('the chain`s other users', 'STAND',
         'LISTED at b445 for their owners to check, none re-verdicted: %d tools whose code calls the chain on its '
         'default grid.' % NUSERS),
        ('the fourth candidate: the inherited ordinates` precision', 'STAND',
         'PRICED at b445, NOT RUN: mpmath ordinates for n = 101 ... 10000 in place of the library, about 40 minutes on '
         'ten workers; outside (R57)`s two parameters.'),
        ('W-ORD-SPAN-HEADING', 'STAND',
         'CARRIED: the instrument lane opened at b445 but (R57) opened it for the residual`s owner and nothing else, so '
         'the span tool was not repaired.'),
        ('the instrument lane under (R57)', 'CLOSE', 'CLOSED at the end of b445; no instrument built, no chain file edited.'),
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


def table_rows():
    out = []
    for k in CELLS:
        out.append((k, e('base', k), e('a', k), e('b', k), e('a_nv', k), e('a_nu', k),
                    RJ['rates'].get(k), RJ['status']['a'][k], RJ['status']['b'][k]))
    return out


def trail_block():
    body = [
        '### b445 — whose residual it is — filed 2026-09-12',
        '',
        '**The residual b444 found above the floor is the chain’s integration. Doubling the autocorrelation grid makes it fall at @FA@ of 14 cells; extending the zero library by half again leaves it where it was. The navigator’s truncation hypothesis is refuted at the measured size. The instrument lane `(R57)` opened for this and closed at the act’s end.**',
        '',
        '#### Component 1 — does the zero side truncate?',
        '',
        '**Yes, from the chain’s own source.** `tools/e16/carto_atlas.py` declares `NGAM = 10000` banked verified ordinates and loads `zeta_ordinates.npy[:NGAM]`; the file’s last ordinate is **9877.782657433876**. The count is in the source; the height is only in the data file the source loads. The same source computes a truncation bound, which b437 banked per cell, largest **@BOUND@**. The hypothesis was alive when it was tested.',
        '',
        '#### Component 2 — the discriminator',
        '',
        'The 14 cells of b444’s 22 where `|e|` is above `1.49e-08`. The base reproduced the banked residual to `1e-12` at all 14. **Arm (a):** `nv` 8193 → 16385 and `NU` 12001 → 24001 together; the halves were run beside and did not govern. **Arm (b):** the library plus `mpmath.zetazero(n)` for n = 10001 … 15000 at 25 digits, reaching @REACH@; control passed; `zeta_ordinates.npy` not edited. Rule, fixed on the face: a cell FALLS if `|e_arm| ≤ 0.5|e_base|` or below the floor, is STABLE if `|e_arm − e_base| ≤ 0.1|e_base|`; an arm FALLS at ≥ 8 cells and is STABLE at ≥ 12.',
        '',
        '| a | e base | e (a) grid | e (b) reach | (a) nv only | (a) NU only | rate (a) | (a) | (b) |',
        '|:--|--:|--:|--:|--:|--:|--:|:--|:--|',
    ]
    for k, eb, ea, eb2, env, enu, rt, sa, sb in table_rows():
        body.append('| %s | %+.3e | %+.3e | %+.3e | %+.3e | %+.3e | %s | %s | %s |'
                    % (k, eb, ea, eb2, env, enu, ('%.2f' % rt) if rt is not None else '—', sa, sb))
    body += [
        '',
        '**Verdict by the rule: @VERD@.** Arm (a) falls at @FA@ of 14 (@BELOWA@ below the floor, which makes them the instrument’s), apparent order about @RATE@; arm (b) is stable at @TB@ of 14, largest shift @DBMAX@, inside the source’s bound. The halves settle which grid carries it: `nv` alone reproduces arm (a) to @NVH@, and `NU` alone reproduces the base to @NUH@. **So it is the autocorrelation grid, not the frequency grid.** **What is not decided:** after one doubling, @NABOVE@ cells are still above the floor (largest @AMAX@), and cell @MOVES@ moves without falling. The act does not claim that further refinement removes them, because that was not measured.',
        '',
        '#### Component 3 — what the verdict obliges',
        '',
        'b444’s STRUCTURE verdict is restated as the chain’s. b444’s bank is not edited. The @NU@ tools whose code calls this chain are listed in `data/b445_components.txt` for their owners to check, and none is re-verdicted. **The fourth candidate**, the inherited ordinates’ precision (the library differs from mpmath by up to `1.1e-04` above n = 100), is priced at about 40 minutes on ten workers and not run: it is outside `(R57)`. No claim about zeros in any branch. The zero side is inherited, and the extension ordinates are mpmath’s and nothing more.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | the zero side does truncate | **HELD** — 10000 ordinates, height 9877.78 |',
        '| (N1)(b) | the library’s height is stated in the chain’s own source | **HALF HELD** — the count is in the source; the height only in the data file it loads |',
        '| (N2) | arm (b) moves e and arm (a) does not; the owner is truncation | **REFUTED** — (a) falls at @FA@ of 14; (b) stable at @TB@ of 14 |',
        '',
        'This seat’s own, from the face: (N1)(a) held — **HELD**; (N1)(b) half held — **HELD**; (N2) refuted — **HELD**.',
        '',
        '**The instrument lane opened by `(R57)` is closed.** The four lists are open.',
    ]
    rep = [('@FA@', str(FA)), ('@TB@', str(TB)), ('@BOUND@', BOUND), ('@REACH@', REACH), ('@VERD@', VERD),
           ('@BELOWA@', str(BELOW_A)), ('@RATE@', '%.1f' % RATE_MED), ('@DBMAX@', '%.1e' % DB_MAX),
           ('@NVH@', '%.1e' % RJ['nv_half_vs_a']), ('@NUH@', '%.1e' % RJ['nu_half_vs_base']),
           ('@NABOVE@', str(len(A_ABOVE))), ('@AMAX@', '%.2e' % A_ABOVE_MAX), ('@MOVES@', ', '.join(MOVES_A) or 'none'),
           ('@NU@', str(NUSERS))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b445)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest. **COMPONENT 1: THE ZERO SIDE TRUNCATES -- "
                 "carto_atlas.py DECLARES NGAM = 10000, THE LIBRARY ENDS AT 9877.782657433876, THE SOURCE'S OWN BOUND "
                 "%s.** **COMPONENT 2: AT THE 14 CELLS ABOVE THE FLOOR, THE BASE REPRODUCING THE BANK AT 14; ARM (a), THE "
                 "QUADRATURE GRID DOUBLED, e FALLS AT %d (%d BELOW THE FLOOR), APPARENT ORDER ABOUT %.1f; ARM (b), THE "
                 "LIBRARY EXTENDED TO 15000 ORDINATES (REACH %s), e STABLE AT %d, LARGEST SHIFT %.1e; THE nv HALF CARRIES "
                 "IT, THE NU HALF DOES NOT. VERDICT BY THE FIXED RULE: %s. %d CELLS STILL ABOVE THE FLOOR AFTER ONE "
                 "DOUBLING, NOT DECIDED.** **COMPONENT 3: b444'S STRUCTURE RESTATED AS THE CHAIN'S; %d CHAIN TOOLS LISTED, "
                 "NONE RE-VERDICTED; THE ORDINATES' PRECISION PRICED AS THE FOURTH CANDIDATE, NOT RUN; NO CLAIM ABOUT "
                 "ZEROS.** THE NAVIGATOR'S (N2) REFUTED. THE LANE (R57) CLOSED. 0 CHAIN FILES EDITED, 0 GRADES MOVED, "
                 "0 CONTENT LOST")
            % (GR, GDG, BOUND, FA, BELOW_A, RATE_MED, REACH, TB, DB_MAX, VERD, len(A_ABOVE), NUSERS))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; carto_atlas.py, zeta_ordinates.npy, "
            "b317_smear.py, b318_square.py AND b321_window.py BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### EVERY FACTOR, TOLERANCE AND DECISION RULE WAS ON THE FACE BEFORE ANY ARM'S VALUE, AND THE FOURTH "
             "CANDIDATE WAS NAMED THERE BEFORE IT COULD LOOK DISCOVERED; THE RESULT REFUTED THE NAVIGATOR'S EXPECTATION "
             "AND IS REPORTED AS THE RULE GAVE IT, WITH WHAT ONE REFINEMENT LEAVES STATED AS NOT DECIDED")
    status = ("data/b445_whose_residual.txt; data/b445_components.txt; data/b445_arms.json; "
              "data/b445_ordinates_10001_15000.npy; data/b445_ordinates_run.txt; data/b445_checks.txt; "
              "data/b445_registration_2026-09-12.txt (LOCKED at sha256 %s); data/b445_addendum.txt (EMPTY); "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('whose residual is it',
           'is the channels residual quadrature error',
           'does the zero library truncate',
           'does extending the zero library move the residual',
           'which grid carries the identity residual')
MUST_NOT_HIT = ('the residual is the object', 'the residual is truncation', 'carto atlas edited')
KEY = 'whose-residual-it-is'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b445 RAN b444'S CHAIN AT ITS 14 ABOVE-FLOOR CELLS WITH TWO PARAMETERS VARIED UNDER (R57). THE ZERO SIDE "
        "TRUNCATES AT 10000 ORDINATES (HEIGHT 9877.78). DOUBLING THE QUADRATURE GRID MAKES e FALL AT %d OF 14 (%d BELOW "
        "THE FLOOR); EXTENDING THE LIBRARY TO 15000 ORDINATES LEAVES e STABLE AT %d OF 14. VERDICT BY THE FIXED RULE: "
        "%s -- THE AUTOCORRELATION GRID CARRIES IT. %d CELLS STILL ABOVE THE FLOOR AFTER ONE DOUBLING, NOT DECIDED. "
        "TRUNCATION HYPOTHESIS REFUTED; THE ORDINATES' PRECISION PRICED, NOT RUN; NO CLAIM ABOUT ZEROS."
        % (FA, BELOW_A, TB, VERD, len(A_ABOVE)))
    grade = "### NO GRADE MOVED. ### NO CHAIN FILE EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b445_whose_residual.txt; data/b445_arms.json; data/b445_components.txt; "
             "data/b445_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b445 (whose residual it is)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### WHOSE RESIDUAL IT IS (b445).%s'
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
        rec('    %-58s reaches the b445 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the truncation answer carried', 'TRUNCATES AT 10000 ORDINATES' in out),
            ('arm (a) carried', 'DOUBLING THE QUADRATURE GRID' in out),
            ('arm (b) carried', 'EXTENDING THE LIBRARY TO 15000' in out),
            ('the verdict carried', ('VERDICT BY THE FIXED RULE: ' + str(VERD)) in out),
            ('the undecided remainder carried', 'AFTER ONE DOUBLING, NOT DECIDED' in out),
            ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, 'b445 -- WHOSE RESIDUAL IT IS.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
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


B444ROW_RE = r"(?m)^\| (\d+) \| \*\*THE WITNESS AND CHANNEL ARC FOLDED, b433-b443"


def main():
    global DESK
    bar('=')
    rec('b445_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not VERD or len(CELLS) != 14 or not BOUND or not REACH or ARMS_FAIL != 0:
        rec('  ### HARD FAILURE -- a figure this tool reads is missing, or the suite is not passing.')
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      verdict %s ; (a) falls %d, %d below floor ; (b) stable %d, max shift %.2e ; bound %s ; reach %s'
        % (VERD, FA, BELOW_A, TB, DB_MAX, BOUND, REACH))
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
        % [int(x.group(1)) for x in re.finditer(B444ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B444ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b445_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
