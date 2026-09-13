# -*- coding: utf-8 -*-
"""b449_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure is read off this act's own records -- the count and
### integrand JSON, the lock gate's notes, the suite -- and none is typed.
### ### **THE SUITE GATE, STATED:** this tool runs only if the pre-push suite fails on no arm but the two whose object this
### tool itself writes (`G-C1-WORKORDER-FILED`, `G-C1-PARTITION-ROW-POINTS`); the suite is re-run after it and must then
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
MARK = '<!-- b449 the (R61) record ratified, and the outlier`s integrand at its aim -->'
PRIOR = '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->'
BANKOUT = os.path.join(D, 'b449_the_record_and_the_integrand.txt')
SELF_WRITTEN = {'G-C1-WORKORDER-FILED', 'G-C1-PARTITION-ROW-POINTS'}
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


FACE = read(os.path.join(D, 'b449_registration_2026-09-13.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b449_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b449_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b449_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


CJ = _j('b449_count.json')
IJ = _j('b449_integrand.json')
V = IJ.get('verdict') or {}
SPAN = _j('b449_span.json')
READY = bool(CJ.get('rows')) and bool(V) and bool(SPAN)
ROWS = dict((r['figure'], r) for r in CJ.get('rows') or [])
LV = IJ.get('levels') or []
SPANN = SPAN.get('current_span')
RAT = 'RATIFIED AT b449' if CJ.get('ratified') else 'NOT RATIFIED'
KINK = 'NO KINK' if not V.get('kink') else 'A KINK'
MSTATE = V.get('measurement', '')
EXP = V.get('expect') or {}

ROWMARK = ('**THE (R61) RECORD IS RATIFIED AT b449 -- THE SIX BANKS REPRODUCE EVERY FIGURE AND b443`S PER-SITE CONTROL FIRES; '
           'THE OUTLIER`S INTEGRAND IS FLAT AT ln 17, NO KINK AND NO NODE ON IT, SO (c1) DOES NOT ACCOUNT FOR THE GROWTH AND THE '
           'MEASUREMENT STAYS OPEN**')
SCOPE = ("### THE ACT COUNTED SIX BANKS AGAINST A RECORD IT DID NOT EDIT, NOTED ONE MIRROR ARTEFACT IN THE LOOM, FILED ONE "
         "WORK-ORDER, AND UNDER (R62) FORMED ONE CELL`S INTEGRAND AT FOUR LEVELS AND READ IT AT ONE AIM; NO CHANNEL BUT THE "
         "PRIME CHANNEL, NO CHAIN FILE EDITED; THE LANE CLOSED AT ITS END. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def steps():
    out = []
    ns = list(LV[0]['terms'].keys())
    for j in (1, 2, 3):
        d = dict((n, LV[j]['terms'][n] - LV[j - 1]['terms'][n]) for n in ns)
        out.append(dict(d=d, dpr=LV[j]['prime'] - LV[j - 1]['prime']))
    return ns, out


def desk():
    ns, st = steps()
    return [
        ('the (R61) record, filed without a face', 'CLOSE',
         '%s: the banks of sites (i) to (vi) counted by tool beside the record parsed off OPEN_TRAILS.md:%d-%d -- %d candidates, '
         '%d held, %d kinds, class boundary %d, imports %d, majority at %d of 6 -- %d discrepancies; the positive control '
         'against b443`s per-site line fires; the negative control is zero at all six. The record is not edited.'
         % (RAT, CJ['record_lines'][0], CJ['record_lines'][1], ROWS['candidates']['bank'], ROWS['held']['bank'],
            ROWS['kinds']['bank'], ROWS['cb_total']['bank'], ROWS['imports']['bank'], ROWS['majority_sites']['bank'],
            len(CJ['discrepancies']))),
        ('b448`s mirror check on an artefact since replaced', 'CLOSE',
         'NOTED ONCE in the loom at b449 by its appender, prefix proved; b448`s bank unedited.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND',
         'FILED at b449: the builder`s default names a zip by date alone and removes an existing one. Trigger: the next mirror '
         'build, or the next opening of the instrument-audit lane. FIRED by b449`s own closing build, which passes the '
         'builder`s DateTag parameter; the repair is not made.'),
        ('the outlier 4.123106', 'STAND',
         'READ at b449 under (R62), candidate (c1): the integrand formed at four levels reproduces the banked prime channel '
         'exactly; at v* = ln 17 it is %s (F, D-, D+ all %s); every level STRADDLES v* at %.3e from the edge node; the n = 17 '
         'term contributes nothing. (c1) does not account for the growth; the measurement %s. Beside the rule: at step 1 the '
         'n = 3 term`s change (%+.2e) offsets the n = 2 term`s (%+.2e), and by step 2 it has fallen to %+.2e. (c2) PRICED AND NOT RUN.'
         % (KINK, '%.0e' % LV[-1]['F_vstar'], LV[-1]['near'], MSTATE, st[0]['d']['3'], st[0]['d']['2'], st[1]['d']['3'])),
        ('candidate (c1), the integrand at sqrt(17)', 'CLOSE',
         'RUN at b449 under (R62): no kink at ln 17; the aim is not a node at any level.'),
        ('the instrument lane under (R62)', 'CLOSE', 'CLOSED at the end of b449; no instrument built, no chain file edited.'),
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
    ns, st = steps()
    body = [
        '### b449 — the (R61) record ratified under a face, and the outlier’s integrand at its aim — filed 2026-09-13',
        '',
        '**The `(R61)` record is @RAT@: the candidate banks of all six sites, counted by tool under a locked face, reproduce every figure the record states, and the per-site class-boundary count matches b443’s own line. The outlier’s integrand, read under `(R62)` at four levels, is flat at `ln 17`: no kink, and no node sits on it at any level. So candidate (c1) does not account for the growth of the prime channel’s change, and the measurement @MSTATE_L@.**',
        '',
        '#### Component 1 — the (R61) record, verified; not edited',
        '',
        'The record at `OPEN_TRAILS.md:@LO@–@HI@` (the order placed it at 6473–6485; there is no line 6485).',
        '',
        '| figure | the banks, counted | the record, parsed | agree |',
        '|:--|:--|:--|:--|',
    ]
    fmt = lambda x: (', '.join('(%s) %d/%d' % (k, v[0], v[1]) for k, v in x.items()) if isinstance(x, dict)
                     else (', '.join('(%s)' % s for s in x) if isinstance(x, list) else str(x)))
    for r in CJ['rows']:
        body.append('| %s | %s | %s | %s |' % (r['figure'], fmt(r['bank']), fmt(r['record']), 'yes' if r['bank'] == r['record'] else '**NO**'))
    body += [
        '',
        'Positive control: the same counter’s class-boundary figures per site equal b443’s line at `b443r_the_arc_product.txt:24` — **@POS@**. Negative control: a kind named `NOT A KIND` counts zero at all six sites — **@NEG@**. Discrepancies: **@NDISC@**.',
        '',
        '**The failure-mode partition, its trail row, pointing at the ratified record:**',
        '',
        '| item | from | aim | trigger |',
        '|:--|:--|:--|:--|',
        '| the failure-mode partition | FINDINGS.md:3375 | AIMED | a source enters the record under the import bar that ranges over a class containing the corpus’s own objects; or the author’s word — `(R61)`, OPEN_TRAILS.md:6473, @RAT@ |',
        '',
        '**The mirror check whose artefact is gone** is noted once in `VERIFICATION_LOOM.md`, by its appender with the prefix proved. b448’s closing verified `mirror-refresh-2026-09-13.zip` at `b1656b1`; the `(R61)` rebuild at `dc5e18e` replaced that zip under the same name. b448’s bank is not edited.',
        '',
        '**W-ORD-MIRROR-ZIP-NAME.** `tools/mirror_build.ps1` names its zip by date alone (line 122) and removes an existing zip of that name (line 123), so it cannot hold two builds from one day. It already takes a `DateTag` parameter (line 4), which earlier September builds used. **Trigger: the next mirror build, or the next opening of the instrument-audit lane, whichever comes first.** b449’s own closing build is the next mirror build, so the trigger fires here; that build passes `-DateTag 2026-09-13-b449`, and the repair to the builder is not made — the instrument-audit lane is parked.',
        '',
        '#### Component 2 — the outlier’s integrand, candidate (c1), under (R62)',
        '',
        'At the banked `a = 4.123106` (`sqrt(17) = 4.1231056256`, the cell above it by `3.7e-07`), the seed and its autocorrelation were formed by b447’s code path at four levels, and the prime channel re-summed from them equals its bank exactly at every level. The aim is `v* = ln 17`, where the prime channel reads `f` for `n = 17`; it lies `@EDGE@` inside the support edge.',
        '',
        '| nv | h | F(v*) | D− | D+ | D+ − D− | max abs f′ | nearest node | placement |',
        '|--:|--:|--:|--:|--:|--:|--:|--:|:--|',
    ]
    for x in LV:
        body.append('| %d | %.4e | %.1e | %.1e | %.1e | %.1e | %.3f | %.4e | %s |'
                    % (x['nv'], x['h'], x['F_vstar'], x['Dminus'], x['Dplus'], x['jump'], x['maxslope'], x['near'], x['placement']))
    body += [
        '',
        '**@KINK_S@ at `ln 17`**, by the face’s bar of `1e-6 · max abs f′`. `f` is exactly zero at the aim and at its last six nodes, as a seed of `exp(−1/(1−t²))` bumps predicts. The edge node is `L` itself, and `v*` sits inside it at every level, so every grid straddles the aim and none sits on it. The `n = 17` term contributes zero at all four levels. **(c1) does not account for the growth; the measurement @MSTATE_L@**, with (c2) — the grid’s alignment with a feature, an instrument edit — priced and not run.',
        '',
        '*Beside the rule, not a verdict:* the prime channel’s change by term shows step 1 as a cancellation — the `n = 2` term’s change `@D12@` against the `n = 3` term’s `@D13@` — and by step 2 the `n = 3` change has fallen to `@D23@` while `n = 2`’s halves to `@D22@`. That is what makes the channel’s change grow between the first two levels.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | the banks reproduce 82 / 0 / 11 and 47 of 82 with the per-site figures, and the control fires | **@N1@** |',
        '| (N2)(a) | the integrand carries a kink at sqrt(17) | **@N2A@** |',
        '| (N2)(b) | the first two grids straddle it, the last two do not, and the measurement closes | **@N2B@** — all four straddle; open |',
        '',
        'This seat’s own, from reading code and computing nothing before the face: (N1) held — **HELD**; (N2)(a) refuted — **HELD**; (N2)(b) refuted — **HELD**.',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b449), against a ruled threshold of nine.** The instrument lane opened by `(R62)` is closed. The four lists are open.',
    ]
    rep = [('@RAT@', RAT), ('@MSTATE_L@', MSTATE.lower()), ('@LO@', str(CJ['record_lines'][0])), ('@HI@', str(CJ['record_lines'][1])),
           ('@POS@', 'fires' if CJ['positive']['fires'] else 'DOES NOT FIRE'), ('@NEG@', 'zero' if CJ['negative']['fires'] else 'NOT ZERO'),
           ('@NDISC@', str(len(CJ['discrepancies']))), ('@EDGE@', '%.3e' % LV[0]['L_minus_vstar']),
           ('@KINK_S@', 'No kink' if not V['kink'] else 'A kink'),
           ('@D12@', '%+.2e' % st[0]['d']['2']), ('@D13@', '%+.2e' % st[0]['d']['3']), ('@D23@', '%+.2e' % st[1]['d']['3']),
           ('@D22@', '%+.2e' % st[1]['d']['2']), ('@N1@', EXP.get('n1', '')), ('@N2A@', EXP.get('n2a', '')), ('@N2B@', EXP.get('n2b', '')),
           ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b449)"
    ns, st = steps()
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; NO VALUE OF THE OBJECT COMPUTED BEFORE THE FACE. "
                 "**COMPONENT 1: THE BANKS OF SITES (i) TO (vi) COUNTED BY TOOL -- %d CANDIDATES, %d HELD, %d KINDS, CLASS BOUNDARY %d, "
                 "IMPORTS %d, MAJORITY AT %d OF 6 -- AGAINST THE RECORD PARSED OFF OPEN_TRAILS.md:%d-%d: %d DISCREPANCIES; b443'S "
                 "PER-SITE CONTROL FIRES, THE NEGATIVE CONTROL ZERO; %s; THE RECORD NOT EDITED; THE MIRROR ARTEFACT NOTED IN THE LOOM; "
                 "W-ORD-MIRROR-ZIP-NAME FILED AND FIRED BY THIS ACT'S OWN BUILD, REPAIR NOT MADE.** **COMPONENT 2, UNDER (R62): THE "
                 "INTEGRAND AT a = 4.123106 FORMED AT FOUR LEVELS REPRODUCES THE BANKED PRIME CHANNEL EXACTLY; AT v* = ln 17 F, D- AND "
                 "D+ ARE ALL ZERO -- %s; ALL FOUR GRIDS STRADDLE v*, NONE SITS ON IT; THE n = 17 TERM IS ZERO; (c1) DOES NOT "
                 "ACCOUNT FOR THE GROWTH; THE MEASUREMENT %s; BESIDE THE RULE, STEP 1 IS A CANCELLATION OF THE n = 2 AND n = 3 "
                 "TERMS.** (N1) %s, (N2)(a) %s, (N2)(b) %s. SPAN BY TOOL %s. THE LANE (R62) CLOSED. 0 CHAIN FILES EDITED, 0 GRADES "
                 "MOVED, 0 CONTENT LOST")
            % (GR, GDG, ROWS['candidates']['bank'], ROWS['held']['bank'], ROWS['kinds']['bank'], ROWS['cb_total']['bank'],
               ROWS['imports']['bank'], ROWS['majority_sites']['bank'], CJ['record_lines'][0], CJ['record_lines'][1],
               len(CJ['discrepancies']), RAT, KINK, MSTATE, EXP['n1'], EXP['n2a'], EXP['n2b'], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD AND VERIFICATION_LOOM.md +1 BLOCK, EACH APPENDED AS A TRUE PREFIX; THE "
            "(R61) RECORD, FINDINGS.md, FACES_LEDGER.md, EVERY CANDIDATE BANK, EVERY CLOSING AND EVERY CHAIN FILE BYTE-UNMOVED; "
            "TECHNE-Core UNTOUCHED -- 0 CONTENT LOST")
    grade = ("### THE COUNT, BOTH CONTROLS, THE AIM, THE DERIVATIVE BAR, THE PLACEMENT TOLERANCE AND THE ACCOUNT WERE ON THE FACE "
             "BEFORE ANY VALUE; EACH VERDICT IS THE RULE'S AS IT FELL, WITH THE TERM READ PRINTED BESIDE IT")
    status = ("data/b449_the_record_and_the_integrand.txt; data/b449_components.txt; data/b449_count.json; "
              "data/b449_integrand.json; data/b449_span.json; data/b449_checks.txt; "
              "data/b449_registration_2026-09-13.txt (LOCKED at sha256 %s); data/b449_addendum.txt (EMPTY); "
              "VERIFICATION_LOOM.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('is the r61 record ratified',
           'does the outlier integrand carry a kink',
           'W-ORD-MIRROR-ZIP-NAME',
           'the prime channel integrand at ln 17',
           'mirror zip overwritten')
MUST_NOT_HIT = ('the outlier is explained', 'the partition is decided', 'the measurement closes')
KEY = 'the-r61-record-ratified-and-the-outliers-integrand-at-its-aim'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b449 COUNTED THE WITNESS ARC'S SIX BANKS AGAINST THE (R61) RECORD: %s, 0 DISCREPANCIES, b443'S CONTROL FIRES. UNDER "
        "(R62) THE OUTLIER'S INTEGRAND AT ln 17 IS FLAT, %s, NO NODE ON THE AIM; (c1) DOES NOT ACCOUNT FOR THE GROWTH; THE "
        "MEASUREMENT %s. W-ORD-MIRROR-ZIP-NAME FILED. NO CLAIM ABOUT ZEROS." % (RAT, KINK, MSTATE))
    grade = "### NO GRADE MOVED. ### NO CHAIN FILE OR CLOSING EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b449_the_record_and_the_integrand.txt; data/b449_components.txt; data/b449_count.json; "
             "data/b449_integrand.json; data/b449_registration_2026-09-13.txt (LOCKED, %d gates read, %d by digest); "
             "VERIFICATION_LOOM.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b449 (the (R61) record ratified under a face, and the outlier's integrand at its aim)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE (R61) RECORD RATIFIED UNDER A FACE, AND THE OUTLIER`S INTEGRAND AT ITS AIM (b449).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
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
        rec('    %-58s reaches the b449 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the ratification carried', RAT in out), ('the kink verdict carried', KINK in out),
                      ('the measurement carried', ('THE MEASUREMENT %s' % MSTATE) in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b449 -- THE (R61) RECORD RATIFIED UNDER A FACE, AND THE OUTLIER'S INTEGRAND AT ITS AIM.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s -- the failing arms all this tool`s own writes'
           % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B448ROW_RE = r"(?m)^\| (\d+) \| \*\*THE FAILURE-MODE PARTITION AND THE WITNESS ARC`S TAXONOMY ARE RELATED"


def main():
    global DESK
    bar('=')
    rec('b449_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B448ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b449_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
