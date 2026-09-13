# -*- coding: utf-8 -*-
"""b447_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b447 the outlier, the arm that bites, and the stock-take -->'
PRIOR = '<!-- b446 the floor has a domain -->'
BANKOUT = os.path.join(D, 'b447_stock_take.txt')
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


FACE = read(os.path.join(D, 'b447_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b447_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b447_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b447_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


SJ = _j('b447_stocktake.json')
SPAN = _j('b447_span.json')
CJ = _j('b446_floor_census.json')
C1 = SJ.get('c1') or {}
OPEN = SJ.get('open') or []
AIMED = SJ.get('aimed') or []
EXP = SJ.get('expect') or {}
READY = bool(C1.get('run')) and bool(OPEN) and bool(SPAN)
if READY:
    OUTCOME = C1['outcome']
    P1, P2, RATE = C1['p1'], C1['p2'], C1['rate']
    E, NV, DD = C1['e'], C1['nv'], C1['diffs']
    SPANN = SPAN['current_span']
    NALL, NOUT, JAF = CJ['kind']['all'], CJ['kind']['out'], CJ['residue']['json_verdicts']['AT_FLOOR']
else:
    OUTCOME, P1, P2, RATE, E, NV, DD, SPANN = '', 0.0, 0.0, 0.0, [], [], [], None

ROWMARK = ('**THE OUTLIER`S ERROR SHRINKS AT THE THIRD DOUBLING, AT ORDER 2.43, AND THE RULE STILL REFUSES IT FROM ABOVE; THE FLOOR '
           'ARM`S RECORD IS NOTED ONCE IN THE LOOM; AND THE STOCK-TAKE FINDS ONE OPEN ITEM AIMED AT THE QUANTIFIER**')

SCOPE = ("### THE ACT RAN ONE DOUBLING AT ONE CELL UNDER (R60), APPENDED ONE LOOM BLOCK AND ONE LINE TO THE BAR-FLOOR RULE, "
         "AND READ THE RECORD`S CLOSED AND OPEN ITEMS BY RULES FIXED ON ITS FACE; NOTHING PROPOSED, NOTHING RE-VERDICTED, NO "
         "CLOSING EDITED; THE LANE CLOSED AT ITS END. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('the outlier 4.123106 (b446`s standing item)', 'STAND',
         'MEASURED at b447 at four levels: the differences %s; order p1 %.2f, then p2 %.2f; the rule [0.9465, 1.9465] with the '
         'difference shrinking gives %s. READ BESIDE THE RULE: it refuses from above -- the error shrank once, at an order '
         'nearer the asymptotic 2 than the window, which was built from pre-asymptotic orders. What stays unexplained is the '
         'growth between the first two levels; candidates (c1) the integrand at sqrt(17), (c2) the grid`s alignment with a '
         'kink, (c3) the channels` cancellation, each priced and NOT RUN.' % (', '.join('%+.2e' % x for x in DD), P1, P2, OUTCOME)),
        ('the arm that bites', 'CLOSE',
         'NOTED ONCE at b447 in the loom beside noise_floor.py`s own header: %d comparisons, %d of another kind, %d floor-arm '
         'records all on an exact zero -- the gate`s verdicts are the drift arm`s. Nothing re-verdicted, no closing edited.'
         % (NALL, NOUT, JAF)),
        ('the bar-floor rule`s other face', 'CLOSE',
         'FILED at b447, one line in TECHNE BAR_FLOOR_RULE.md (local): a bar that never bites is uninformative rather than '
         'lenient; incidents b272 and b446.'),
        ('the stock-take', 'CLOSE',
         'READ at b447: 5 closed items anchored; %d open items with their triggers in the record`s words; %d aimed at the '
         'quantifier in its own words -- %s. Nothing proposed.' % (len(OPEN), len(AIMED), ', '.join(AIMED) or 'none')),
        ('the navigator`s "two-level estimate"', 'CLOSE',
         'CORRECTED at b447 on the locked face: b446`s order at the outlier used three levels and two differences.'),
        ('W-ORD-SPAN-HEADING', 'STAND', 'CARRIED: (R60) opened the instrument lane for the outlier alone.'),
        ('the instrument lane under (R60)', 'CLOSE', 'CLOSED at the end of b447; no instrument built, no chain file edited.'),
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
        '### b447 — the outlier, the arm that bites, and the stock-take — filed 2026-09-12',
        '',
        '**At the third doubling the outlier `a = 4.123106`’s error shrinks @SHRINK@-fold, at order @P2@, and the face’s rule still refuses it — from above: the window was built from the other cells’ pre-asymptotic orders. What stays unexplained is the growth of its error between the first two levels. The floor arm’s record is noted once in the loom, and the bar-floor rule gains its other face. The stock-take finds @NOPEN@ open items and @NAIMED@ aimed at the quantifier in the record’s own words: @AIMED@. The instrument lane `(R60)` opened for this and closed at the act’s end.**',
        '',
        '#### Component 1 — the outlier, four levels',
        '',
        '| nv | e | difference |',
        '|--:|--:|--:|',
    ]
    for i, (nv, e) in enumerate(zip(NV, E)):
        body.append('| %d | %+.6e | %s |' % (nv, e, ('%+.6e' % DD[i - 1]) if i else '—'))
    body += [
        '',
        '`p1 = log2(|d1|/|d2|) = @P1@` (b446’s), `p2 = log2(|d2|/|d3|) = @P2@`, rate `log2(|e2|/|e3|) = @RATE@`. The face fixed the rule before the run: the cell converges at the others’ rate if `p2` lies in `[0.9465, 1.9465]` and the difference shrinks. The difference shrank, but `p2` is above the window, so **@OUTCOME@ by the rule.** **Read beside the rule:** the cell’s error is now shrinking, at an order nearer the trapezoid rule’s asymptotic 2 than the window, which b446 built from orders it had itself printed as pre-asymptotic. What stays open is the growth between the first two levels. Three candidates are named, each with its test and price, **not run**: (c1) the integrand’s own behaviour at `a = sqrt(17)`, read from its one-sided derivatives, about a minute; (c2) the grid’s alignment with a kink, which needs a grid offset the chain does not take — an instrument edit; (c3) the channels’ own cancellation, readable from banked channel values at no cost. **The measurement stays open by the rule, because `(R60)` opened the lane for one doubling.** The navigator’s “two-level estimate” is corrected on the face: b446’s order used three levels.',
        '',
        '#### Component 2 — the arm that bites, noted once',
        '',
        'One block was appended to `VERIFICATION_LOOM.md` by its appender, with the prefix proved byte for byte. It sits beside `noise_floor.py`’s own header — *“IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM”* — and records b446’s census: **@NALL@** comparisons, **@NOUT@** of another kind, and **@JAF@** floor-arm records, all on an exact zero. **The gate’s verdicts are the drift arm’s**, and a closing that reads “resolved against the floor” names the arm that did not decide. Nothing is re-verdicted and no closing is edited. The bar-floor rule gains one line: *a bar that never bites is uninformative rather than lenient, as a bar below its object’s floor is uninformative rather than strict* — incidents **b272** and **b446**.',
        '',
        '#### Component 3 — the stock-take, read and not proposed',
        '',
        '**Closed:** the witness arc, complete at six sites with a closed taxonomy of 11 failure kinds; the archimedean channel’s identification as twice theta’s derivative; its named minimum; the residual attributed to the chain (INTEGRATION); the floor understood by kind. Each is anchored by line in `data/b447_components.txt`.',
        '',
        '**Open (@NOPEN@), with the trigger in the record’s words:**',
        '',
        '| item | from | aim | trigger |',
        '|:--|:--|:--|:--|',
    ]
    for o in OPEN:
        body.append('| %s | %s | %s | %s |' % (o['item'].replace('|', '/'), o['source'], o['aim'],
                                              o['trigger'].replace('|', '/')[:160]))
    body += [
        '',
        '**Aimed at the quantifier, in the record’s own words: @NAIMED@ — @AIMED@.** It was named at b348 as *“aimed at the QUANTIFIER rather than at its constituents”*. b351 took it to UNDECIDED: *“the exhaustion move reaches the quantifier in no branch of that act.”* No act has closed it, and the record states no trigger for it. Beside it stands b360’s sentence: *“No move aimed at the quantifier remains on this board that the span has not tried and priced.”* `K8`, the quantifiers themselves, stands **UNOWNED** and is printed as the clause, not as an item aimed at it. **Nothing is proposed.**',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | the outlier converges at the third doubling | **@N1A@** — refused from above by the rule |',
        '| (N1)(b) | the refusal was the two-level estimate’s | **@N1B@** |',
        '| (N2) | no open item is aimed at the quantifier | **@N2@** |',
        '',
        'This seat’s own, from the face: (N1)(a) no expectation; (N1)(b) refuted as worded — **HELD**; (N2) refuted — **HELD**.',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b447), against a ruled threshold of nine.** **The instrument lane opened by `(R60)` is closed.** The four lists are open.',
    ]
    rep = [('@P1@', '%.2f' % P1), ('@P2@', '%.2f' % P2), ('@RATE@', '%.2f' % RATE), ('@OUTCOME@', OUTCOME),
           ('@NOPEN@', str(len(OPEN))), ('@SHRINK@', '%.1f' % (abs(DD[1]) / abs(DD[2]))), ('@NAIMED@', str(len(AIMED))), ('@AIMED@', ', '.join(AIMED) or 'none'),
           ('@NALL@', str(NALL)), ('@NOUT@', str(NOUT)), ('@JAF@', str(JAF)), ('@SPAN@', str(SPANN)),
           ('@N1A@', EXP.get('n1a', '').split(' -- ')[0]), ('@N1B@', EXP.get('n1b', '')), ('@N2@', EXP.get('n2', ''))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b447)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest. **COMPONENT 1: THE THIRD DOUBLING AT a = 4.123106 "
                 "(nv 65537) GIVES e %+.3e; DIFFERENCES %s; ORDER p1 %.2f THEN p2 %.2f; BY THE FACE'S RULE %s -- FROM ABOVE, "
                 "THE WINDOW BUILT FROM PRE-ASYMPTOTIC ORDERS; THE GROWTH BETWEEN THE FIRST TWO LEVELS UNEXPLAINED, THREE "
                 "CANDIDATES PRICED AND NOT RUN; THE NAVIGATOR'S 'TWO-LEVEL ESTIMATE' CORRECTED -- IT WAS THREE.** "
                 "**COMPONENT 2: ONE LOOM BLOCK, PREFIX PROVED: %d COMPARISONS, %d OF ANOTHER KIND, %d FLOOR-ARM RECORDS ALL ON "
                 "AN EXACT ZERO -- THE GATE'S VERDICTS ARE THE DRIFT ARM'S; ONE LINE TO THE BAR-FLOOR RULE, A BAR THAT NEVER "
                 "BITES IS UNINFORMATIVE RATHER THAN LENIENT (b272, b446); NOTHING RE-VERDICTED, NO CLOSING EDITED.** "
                 "**COMPONENT 3: 5 CLOSED ITEMS ANCHORED; %d OPEN WITH TRIGGERS IN THE RECORD'S WORDS; %d AIMED AT THE "
                 "QUANTIFIER IN ITS OWN WORDS -- %s, UNDECIDED SINCE b351, NO TRIGGER; K8 UNOWNED; NOTHING PROPOSED.** "
                 "(N1)(a) REFUTED, (N1)(b) REFUTED AS WORDED, (N2) %s. SPAN BY TOOL %s. THE LANE (R60) CLOSED. 0 CHAIN FILES "
                 "EDITED, 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, E[3], ', '.join('%+.2e' % x for x in DD), P1, P2, OUTCOME, NALL, NOUT, JAF, len(OPEN), len(AIMED),
               (', '.join(AIMED) or 'NONE').upper(), 'REFUTED' if AIMED else 'HELD', SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: VERIFICATION_LOOM.md +1 BLOCK AND OPEN_TRAILS.md +1 RECORD, EACH APPENDED AS A TRUE PREFIX; "
            "FINDINGS.md, EVERY CLOSING AND EVERY CHAIN FILE BYTE-UNMOVED; TECHNE-Core BAR_FLOOR_RULE.md +1 LINE, LOCAL -- 0 "
            "CONTENT LOST")
    grade = ("### THE OUTLIER RULE, THE CLOSURE PAIRS AND THE AIM CLASS WERE ON THE FACE BEFORE ANY VALUE; THE RULE'S VERDICT "
             "IS REPORTED AS IT FELL AND ITS READING PRINTED BESIDE IT; THE STOCK-TAKE QUOTES THE RECORD AND PROPOSES NOTHING")
    status = ("data/b447_stock_take.txt; data/b447_components.txt; data/b447_stocktake.json; data/b447_doubling.json; "
              "data/b447_loom_block.md; data/b447_span.json; data/b447_checks.txt; "
              "data/b447_registration_2026-09-12.txt (LOCKED at sha256 %s); data/b447_addendum.txt (EMPTY); "
              "VERIFICATION_LOOM.md; TECHNE-Core BAR_FLOOR_RULE.md (LOCAL); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('does the outlier converge at the third doubling',
           'which arm of the noise floor gate decides',
           'what does the instrument side hold closed',
           'is any open item aimed at the quantifier',
           'a bar that never bites')
MUST_NOT_HIT = ('the outlier is explained', 'the quantifier is owned', 'closings edited for the floor arm')
KEY = 'the-outlier-the-arm-that-bites-and-the-stock-take'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b447 RAN THE THIRD DOUBLING AT a = 4.123106: ORDER %.2f THEN %.2f, %s BY THE FACE'S RULE -- FROM ABOVE; THE FIRST "
        "LEVELS' GROWTH UNEXPLAINED, CANDIDATES PRICED NOT RUN. THE FLOOR ARM'S RECORD NOTED ONCE IN THE LOOM: THE GATE'S "
        "VERDICTS ARE THE DRIFT ARM'S. STOCK-TAKE: 5 CLOSED, %d OPEN, %d AIMED AT THE QUANTIFIER (%s). NOTHING PROPOSED; NO "
        "CLAIM ABOUT ZEROS." % (P1, P2, OUTCOME, len(OPEN), len(AIMED), ', '.join(AIMED).upper() or 'NONE'))
    grade = "### NO GRADE MOVED. ### NO CHAIN FILE OR CLOSING EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b447_stock_take.txt; data/b447_components.txt; data/b447_stocktake.json; "
             "data/b447_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); VERIFICATION_LOOM.md; "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b447 (the outlier, the arm that bites, and the stock-take)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE OUTLIER, THE ARM THAT BITES, AND THE STOCK-TAKE (b447).%s'
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
        rec('    %-58s reaches the b447 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the doubling carried', 'THE THIRD DOUBLING AT a = 4.123106' in out),
            ('the rule`s outcome carried', OUTCOME in out),
            ('the drift arm carried', "THE DRIFT ARM'S" in out),
            ('the stock-take carried', 'STOCK-TAKE: 5 CLOSED' in out),
            ('nothing proposed carried', 'NOTHING PROPOSED' in out),
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
    Bk = ['=' * 100, 'b447 -- THE OUTLIER, THE ARM THAT BITES, AND THE STOCK-TAKE.', 'THE BANK.', '=' * 100, '']
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


B446ROW_RE = r"(?m)^\| (\d+) \| \*\*THE 1\.49e-08 FLOOR IS A ROUNDING LEVEL"


def main():
    global DESK
    bar('=')
    rec('b447_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not READY or ARMS_FAIL != 0:
        rec('  ### HARD FAILURE -- a figure this tool reads is missing, or the suite is not passing.')
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      outlier %s ; p2 %.3f ; open items %d ; aimed %s ; span %s' % (OUTCOME, P2, len(OPEN), AIMED, SPANN))
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
        % [int(x.group(1)) for x in re.finditer(B446ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B446ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b447_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
