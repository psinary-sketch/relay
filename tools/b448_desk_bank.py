# -*- coding: utf-8 -*-
"""b448_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own records -- the components' JSON, the lock gate's notes, the suite -- and none is typed.
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
MARK = '<!-- b448 the partition read against the taxonomy, and the outlier`s free candidate -->'
PRIOR = '<!-- b447 the outlier, the arm that bites, and the stock-take -->'
BANKOUT = os.path.join(D, 'b448_the_partition_and_the_channels.txt')
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


FACE = read(os.path.join(D, 'b448_registration_2026-09-13.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b448_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b448_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b448_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


PJ = _j('b448_partition.json')
CJ = _j('b448_channels.json')
SPAN = _j('b448_span.json')
READY = bool(PJ.get('verdict')) and bool(CJ.get('growth')) and bool(SPAN) and not PJ.get('misses')
if READY:
    VERDICT, GROWTH, CHAN, MSTATE, NEW = PJ['verdict'], CJ['growth'], CJ['channel'], CJ['measurement'], CJ['new']
    TAB, KINDS, EXP = PJ['table'], PJ['kinds'], PJ['expect']
    L1, L2, L3, HELD = PJ['l1'], len(PJ['l2']), PJ['l3'], PJ['held']
    STEPS, LV, P1, P2 = CJ['steps'], CJ['levels'], CJ['p1'], CJ['p2']
    SPANN = SPAN['current_span']
else:
    VERDICT = GROWTH = CHAN = MSTATE = NEW = ''
    TAB, KINDS, EXP, STEPS, LV = {}, [], {}, [], []
    L1 = L2 = L3 = HELD = 0
    P1 = P2 = 0.0
    SPANN = None

ROWMARK = ('**THE FAILURE-MODE PARTITION AND THE WITNESS ARC`S TAXONOMY ARE RELATED AND NOT THE SAME -- THE ARC CLASSIFIES '
           'CANDIDATES, THE PARTITION ASKED ABOUT AIMS; THE OUTLIER`S EARLY GROWTH IS THE PRIME CHANNEL`S ALONE, NOT A '
           'CANCELLATION; AND AN ORDER ABOVE THE ASYMPTOTIC IS NOW SUPER-CONVERGENT, NOT REFUSAL**')

SCOPE = ("### THE ACT READ TWO ANCHORED OBJECTS AND FOUR BANKED LEVELS BY RULES FIXED ON ITS FACE AFTER A DECLARED PRE-LOCK "
         "READ, AND APPENDED ONE LINE OF THE AUTHOR`S CORRECTION TO THE BAR-FLOOR MODULE; NO CHAIN RUN, NO BRIDGE TYPED, NO "
         "ITEM CLOSED, NO CLOSING EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    s1, s2 = STEPS[0], STEPS[1]
    return [
        ('the failure-mode partition (b447`s stock-take item)', 'STAND',
         'READ at b448 against the witness arc`s taxonomy: %s by the face`s rule -- the elements are not of one kind (the '
         'partition fails the margin at an aim; the arc fails a candidate at a quoted step), the branch test is not met '
         '(%d held, no obstruction), and the links count L1 %d + L2 %d + L3 %d. The arc gives it vocabulary and an exhausted '
         'search at the height (%d candidates) and the width (%d); it gives no class of aims, no branch, nothing at the '
         'abscissa or the phase. OPEN; NO TRIGGER IN THE RECORD`S WORDS; not closed, restated or shelved.'
         % (VERDICT, HELD, L1, L2, L3, TAB['height']['total'], TAB['width']['total'])),
        ('the outlier 4.123106', 'STAND',
         'READ at b448 from the banked channels: the change of e at steps 1 and 2 is the %s channel`s (shares %.4f, %.4f), '
         'and its own change grows between them while the zero and arch channels` shrink -- %s. (c3) REFUTED. The '
         'measurement %s; the prime channel is evaluated by linear interpolation at fixed points (b321_window.py:118). '
         'Under the corrected window its last order %.2f is %s. (c1) and (c2) PRICED AND NOT RUN.'
         % (CHAN, s1['share'], s2['share'], GROWTH, MSTATE, P2, NEW)),
        ('candidate (c3), the channels cancelling', 'CLOSE',
         'REFUTED at b448: every step is ONE CHANNEL`S, the prime channel`s, with gross/net at most %.4f.'
         % max(s['ratio'] for s in STEPS)),
        ('the convergence window`s upper bound', 'CLOSE',
         'FILED at b448 by the author`s order, one line in TECHNE BAR_FLOOR_RULE.md (local): no upper bound below the '
         'method`s asymptotic order; above it SUPER-CONVERGENT, not refusal; incident b447.'),
        ('the pre-lock read of the channel changes', 'CLOSE',
         'DECLARED on b448`s locked face before any rule it informed: both component rules were written with their inputs '
         'seen, and say so.'),
        ('W-ORD-SPAN-HEADING', 'STAND', 'CARRIED: both instrument lanes parked; not the next fold yet.'),
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
    keyname = dict((k, 'K%d' % (i + 1)) for i, k in enumerate(KINDS))
    body = [
        '### b448 — the partition read against the taxonomy, and the outlier’s free candidate — filed 2026-09-13',
        '',
        '**The failure-mode partition and the witness arc’s taxonomy of eleven failure kinds are @VERDICT@ — not the same object. The arc classifies why a candidate shared witness fails at a quoted step; the partition asked how the margin could fail at an aim. The arc gives the partition vocabulary and an exhausted search at two of its four coordinates, and gives it neither a class of aims nor a branch, so b351’s UNDECIDED stands and the item stays open. The outlier’s early growth is the prime channel’s alone, not a cancellation: candidate (c3) is refuted and the measurement stays open, narrowed to that channel. And by the author’s correction, an order above the method’s asymptotic is super-convergent, not a refusal: the outlier’s last order reads @NEW@.**',
        '',
        '*Both component rules were written after a declared, unbanked pre-lock read of their inputs, and the locked face says so.*',
        '',
        '#### Component 1 — the partition read against the taxonomy',
        '',
        'Read at their own anchors. The partition (b348, `FINDINGS.md:3375`; b351’s face, line 40): the margin `places = prime − arch` *“FAILS at an aim when that room is not”* positive, and its classes are sets of aims. The arc (`OPEN_TRAILS.md:5223`): *“enumerate every candidate shared witness for the site … and fail each at a quoted step or hold it”*, a kind being the reason at the first failing step. **The elements are not of one kind.** The branch test under b351’s own rule, *“An absence of a bound is NOT an obstruction”*: **@HELD@ held, no obstruction — not met.** The links, counted apart: L1 **@L1@** sites whose missing statement names a coordinate, L2 **@L2@** kind named verbatim as a b351 state, L3 **@L3@** candidates citing b351. **Verdict by the face’s rule: @VERDICT@.**',
        '',
        '| coordinate | b351’s state | arc sites | ' + ' | '.join(keyname[k] for k in KINDS) + ' | total |',
        '|:--|:--|:--|' + '--:|' * len(KINDS) + '--:|',
    ]
    for w in ('abscissa', 'height', 'phase', 'width'):
        r = TAB[w]
        body.append('| %s | %s | %s | %s | %d |' % (w, r['b351_state'], ', '.join('(%s)' % s for s in r['sites']) or '—',
                                                 ' | '.join(str(r['cells'][k]) for k in KINDS), r['total']))
    body += [
        '',
        '*Key:* ' + '; '.join('%s %s' % (keyname[k], k) for k in KINDS) + '. Sites (i), (v) and (vi) name no coordinate of the aim plane.',
        '',
        '**What the arc gives the partition:** ' + ' '.join('%s — %s.' % (h.capitalize().replace('`', '’'), t.replace('`', '’')) for h, t in PJ.get('gives', [])),
        '',
        '**What it does not:** ' + ' '.join('%s — %s.' % (h.capitalize().replace('`', '’'), t.replace('`', '’')) for h, t in PJ.get('gives_not', [])),
        '',
        '**The item stays open, with no trigger in the record’s words; it is not closed, restated or shelved.** No bridge is typed; row `U1`’s refusal governs.',
        '',
        '#### Component 2 — the outlier’s free candidate (c3)',
        '',
        '| step | +dZ | −dA | +dPR | −dP | de | largest share | class |',
        '|:--|--:|--:|--:|--:|--:|--:|:--|',
    ]
    for s in STEPS:
        c = s['contrib']
        body.append('| %s | %+.3e | %+.3e | %+.3e | %+.1e | %+.3e | %.4f (%s) | %s |'
                    % (s['step'], c['zero'], c['arch'], c['prime'], c['pole'], s['de'], s['share'], s['top'],
                       s['cls'].replace('`', '’')))
    body += [
        '',
        'The residual is `Z − (P − PR + A)` (`b321_window.py:144`), reconstructed exactly from the banked channels at all four levels. **The growth between the first two levels is @GROWTH@ — the @CHAN@ channel’s:** its own change grows from `@D1@` to `@D2@` while the zero and arch channels’ shrink, and the pole’s sit at the rounding level. **Candidate (c3) is refuted and the measurement @MSTATE_L@.** Read beside the rule: the prime channel is evaluated by linear interpolation of the autocorrelation at fixed points (`b321_window.py:118`), not by the trapezoid rule, and the record states no asymptotic order for that evaluation. Candidates (c1) and (c2) stay priced and not run; both instrument lanes are parked.',
        '',
        '#### Component 3 — the convergence window’s upper bound',
        '',
        'One line appended to TECHNE `BAR_FLOOR_RULE.md`, beside the bar-floor rule, committed locally and not pushed: *a convergence window carries no upper bound below the method’s asymptotic order, and an order above it is reported as SUPER-CONVERGENT and not as refusal* — incident **b447**. **The outlier under the corrected rule:** `p2 = @P2@` above the asymptotic `2`, with the last difference shrinking — **@NEW@**. b447’s bank reads REFUSES and is not edited.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | related: the arc gives the partition its vocabulary and not its answer | **@N1@** |',
        '| (N2)(a) | the growth is a cancellation between the archimedean and prime channels | **@N2A@** — one channel’s, the prime channel’s |',
        '| (N2)(b) | the measurement closes | **@N2B@** — open, narrowed to the prime channel |',
        '',
        'This seat’s own, from the face and taken with its inputs seen: (N1) held — **HELD**; (N2)(a) refuted — **HELD**; (N2)(b) refuted — **HELD**.',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b448), against a ruled threshold of nine.** Both instrument lanes stay parked. The four lists are open.',
    ]
    rep = [('@VERDICT@', VERDICT), ('@NEW@', NEW), ('@HELD@', str(HELD)), ('@L1@', str(L1)), ('@L2@', str(L2)),
           ('@L3@', str(L3)), ('@GROWTH@', GROWTH.replace('`', '’')), ('@CHAN@', CHAN), ('@MSTATE_L@', MSTATE.lower()),
           ('@P2@', '%.2f' % P2), ('@N1@', EXP.get('n1', '')), ('@N2A@', EXP.get('n2a', '')), ('@N2B@', EXP.get('n2b', '')),
           ('@SPAN@', str(SPANN)),
           ('@D1@', '%.2e' % abs(STEPS[0]['d'][CHAN])), ('@D2@', '%.2e' % abs(STEPS[1]['d'][CHAN]))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b448)"
    s = STEPS
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; A PRE-LOCK READ OF THE INPUTS DECLARED ON THE FACE. "
                 "**COMPONENT 1: %s BY THE FACE'S RULE -- ELEMENTS NOT OF ONE KIND (MARGIN AT AN AIM / CANDIDATE AT A QUOTED "
                 "STEP); BRANCH TEST NOT MET (%d HELD, NO OBSTRUCTION); LINKS L1 %d + L2 %d + L3 %d; FOUR COORDINATES AGAINST "
                 "ELEVEN KINDS, HEIGHT %d AND WIDTH %d CANDIDATES, ABSCISSA AND PHASE 0; b351'S UNDECIDED STANDS; THE ITEM "
                 "OPEN, NOT CLOSED, RESTATED OR SHELVED; NO BRIDGE TYPED.** **COMPONENT 2: THE CHANNELS AT a = 4.123106 "
                 "RECONSTRUCT e EXACTLY; EVERY STEP ONE CHANNEL'S (SHARES %.4f, %.4f, %.4f), THE PRIME CHANNEL'S; THE GROWTH "
                 "BETWEEN THE FIRST TWO LEVELS %s; (c3) REFUTED; THE MEASUREMENT %s.** **COMPONENT 3: ONE LINE TO THE "
                 "BAR-FLOOR MODULE, THE AUTHOR'S CORRECTION -- NO UPPER BOUND BELOW THE ASYMPTOTIC ORDER, ABOVE IT "
                 "SUPER-CONVERGENT (INCIDENT b447); THE OUTLIER'S p2 %.2f READS %s; b447'S BANK UNEDITED.** (N1) %s, "
                 "(N2)(a) %s, (N2)(b) %s. SPAN BY TOOL %s. 0 CHAINS RUN, 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, VERDICT, HELD, L1, L2, L3, TAB['height']['total'], TAB['width']['total'], s[0]['share'], s[1]['share'],
               s[2]['share'], GROWTH.replace('`', "'"), MSTATE, P2, NEW, EXP['n1'], EXP['n2a'], EXP['n2b'], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; FINDINGS.md, FACES_LEDGER.md, THE U1 DRAFT, "
            "EVERY CANDIDATE BANK, EVERY CLOSING AND EVERY CHAIN FILE BYTE-UNMOVED; TECHNE-Core BAR_FLOOR_RULE.md +1 LINE, LOCAL "
            "-- 0 CONTENT LOST")
    grade = ("### THE ELEMENT TEST, THE BRANCH TEST, THE LINKS, THE CHANNEL RULE AND THE CORRECTED WINDOW WERE ON THE FACE BEFORE "
             "THE COMPONENTS PRINTED ANY VALUE, WITH THE SEAT'S PRE-LOCK READ DECLARED; EACH VERDICT IS THE RULE'S AS IT FELL")
    status = ("data/b448_the_partition_and_the_channels.txt; data/b448_components.txt; data/b448_partition.json; "
              "data/b448_channels.json; data/b448_span.json; data/b448_checks.txt; "
              "data/b448_registration_2026-09-13.txt (LOCKED at sha256 %s); data/b448_addendum.txt (EMPTY); "
              "TECHNE-Core BAR_FLOOR_RULE.md (LOCAL); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('is the failure-mode partition the witness arc taxonomy',
           'does the witness arc discharge the partition',
           'which channel carries the outlier growth',
           'convergence window upper bound',
           'super-convergent')
MUST_NOT_HIT = ('the partition is decided', 'the outlier is explained', 'the quantifier is owned')
KEY = 'the-partition-read-against-the-taxonomy-and-the-outliers-free-candidate'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b448 READ THE FAILURE-MODE PARTITION AGAINST THE WITNESS ARC'S TAXONOMY: %s -- THE ARC CLASSIFIES CANDIDATES, THE "
        "PARTITION ASKED ABOUT AIMS; VOCABULARY AND AN EXHAUSTED SEARCH, NO BRANCH; THE ITEM OPEN. THE OUTLIER'S EARLY "
        "GROWTH IS THE PRIME CHANNEL'S ALONE, (c3) REFUTED, THE MEASUREMENT OPEN. CORRECTED WINDOW: ITS LAST ORDER %s. "
        "NO CLAIM ABOUT ZEROS." % (VERDICT, NEW))
    grade = "### NO GRADE MOVED. ### NO CHAIN RUN, NO CLOSING EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b448_the_partition_and_the_channels.txt; data/b448_components.txt; data/b448_partition.json; "
             "data/b448_channels.json; data/b448_registration_2026-09-13.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b448 (the partition read against the taxonomy, and the outlier's free candidate)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE PARTITION READ AGAINST THE TAXONOMY, AND THE OUTLIER`S FREE CANDIDATE (b448).%s'
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
        rec('    %-58s reaches the b448 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the verdict carried', ("TAXONOMY: %s" % VERDICT) in out),
            ('the channel carried', "THE PRIME CHANNEL'S ALONE" in out),
            ('the corrected window carried', ('ITS LAST ORDER %s' % NEW) in out),
            ('the item open carried', 'THE ITEM OPEN' in out),
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
    Bk = ['=' * 100, "b448 -- THE PARTITION READ AGAINST THE TAXONOMY, AND THE OUTLIER'S FREE CANDIDATE.", '### THE BANK.', '=' * 100, '']
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


B447ROW_RE = r"(?m)^\| (\d+) \| \*\*THE OUTLIER`S ERROR SHRINKS AT THE THIRD DOUBLING"


def main():
    global DESK
    bar('=')
    rec('b448_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('      partition %s ; growth %s (%s) ; measurement %s ; corrected %s ; span %s'
        % (VERDICT, GROWTH, CHAN, MSTATE, NEW, SPANN))
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
        % [int(x.group(1)) for x in re.finditer(B447ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B447ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b448_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
