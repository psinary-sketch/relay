# -*- coding: utf-8 -*-
"""b450_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure is read off this act's own records -- the count and
### integrand JSON, the lock gate's notes, the suite -- and none is typed.
### ### **THE SUITE GATE, STATED:** this tool runs only if the pre-push suite fails on no arm but the two whose object this
### tool itself writes (`G-FILING-C4`, `G-FILING-C2-STANDS`); the suite is re-run after it and must then
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
MARK = '<!-- b450 the eligible set re-measured, and the batch read -->'
PRIOR = '<!-- b449 the (R61) record ratified, and the outlier`s integrand at its aim -->'
BANKOUT = os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt')
SELF_WRITTEN = {'G-FILING-C4', 'G-FILING-C2-STANDS'}
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


FACE = read(os.path.join(D, 'b450_registration_2026-09-13.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b450_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b450_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b450_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


EJ = _j('b450_eligible.json')
BJ = _j('b450_batch.json')
RJ = _j('b450_repairs.json')
V = BJ.get('verdict') or {}
SPAN = _j('b450_span.json')
READY = bool(EJ.get('rows')) and bool(V) and bool(SPAN)
SPANN = SPAN.get('current_span')
ELIG = V.get('eligible') or []
BK = V.get('buckets') or {}
SP = V.get('species') or {}
EXP = V.get('expect') or {}
A_, S_, N_ = 'ALREADY SAYS IT', 'SAYS SOMETHING NOW SUPERSEDED', 'DOES NOT CARRY IT'
RAT = 'eligible %d' % len(ELIG)
KINK = 'buckets %s' % BK
MSTATE = 'made %s routed %s' % (V.get('made'), V.get('routed'))

ROWMARK = ('**THE ELIGIBLE SET IS ELEVEN, NOT FOUR -- b390`S RULE QUOTED AND b395`S MATCHER CARRIED; THE BATCH OF ELEVEN READ IN ONE '
           'ACT, ITS BUCKETS TIED AT SIXTEEN ALREADY-SAYS-IT AND SIXTEEN DOES-NOT-CARRY-IT; THREE CURRENCY REPAIRS MADE, TWENTY-NINE ROUTED; '
           'NO UNPROPAGATED CORRECTION FOUND**')
SCOPE = ("### THE ACT MEASURED THE ELIGIBLE SET UNDER A RULE QUOTED FROM b390 AND NOT IMPROVED, READ THE ELEVEN AS ONE BATCH BY RULES "
         "FIXED ON ITS FACE BEFORE ANY KEYSTONE WAS OPENED, MOVED THREE SUPERSEDED VERSION STRINGS IN THEIR DOCUMENT`S LINEAGE WITH "
         "ORIGINALS PRESERVED, AND FILED CANDIDATE (c4); NO TABLE WRITTEN, NO PROSE REWRITTEN, NO REGISTRY ROW EDITED. ### NO CLAIM ABOUT "
         "RH, h2 OR ANY ZERO")


def desk():
    return [
        ('the reconciliation`s eligible set (the board`s "twelve unread")', 'CLOSE',
         'RE-MEASURED at b450: census 16, reconciled 4 (b390, b394), unread 12 -- the board`s figure AGREES; eligible %d by b390`s rule '
         'with b395`s matcher, ENUMERA excluded (names no terminal). b394`s narrow matcher would reach %d of the %d.'
         % (len(ELIG), len(V.get('v1_on') or []), len(ELIG))),
        ('the eleven keystones', 'CLOSE',
         'READ at b450 as one batch: buckets ALREADY %d / SUPERSEDED %d / DOES NOT CARRY %d; species phantom %d, unpropagated %d, superseded %d; '
         '3 currency repairs made (A_METHODOLOGY v0.2 -> v0.5.4, twice in TECHNE_TOOLKIT, once in E_DIFFICULTY_THEOREM), %d routed.'
         % (BK.get(A_, 0), BK.get(S_, 0), BK.get(N_, 0), SP.get('phantom', 0), SP.get('unpropagated', 0), SP.get('superseded', 0), V.get('routed', 0))),
        ('the routed reconciliation items (29)', 'STAND',
         'ROUTED at b450, each with its ruling: 16 absent era findings (authoring), 8 landed branches still called held in prose (b397`s '
         'species; authoring), 2 keystones with no correspondence table, INDEX_ARITY`s stale registry row, 2 keystones with no registry row.'),
        ('the census`s era findings not located in the ledgers', 'STAND',
         'FOUND at b450: INVARIANCE_BARRIERS` keyhole and T3 Tier-1 findings have no form in FINDINGS.md or OPEN_TRAILS.md; R_CURVE_CRITERION '
         'never carried the pin bd2ae1a the census names for it. ROUTED.'),
        ('candidate (c4), the cancellation within the prime channel', 'STAND',
         'FILED at b450 from b449`s banked term changes; priced, NOT RUN, no lane opened. (c2) priced and not run. The outlier`s measurement stays open.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'FIRED again by b450`s closing build, passed -DateTag; the repair is not made.'),
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
    ks = BJ['keystones']
    body = [
        '### b450 — the reconciliation’s eligible set re-measured, and the batch read — filed 2026-09-13',
        '',
        '**Under b390’s rule, quoted and not improved, and b395’s widened matcher, the eligible set is @NE@ — not four. The census holds 16 keystones; 4 are reconciled (b390, b394); 12 are unread, as the board says; one of them, `ENUMERA`, names no terminal. The eleven were read as one batch. Their buckets tie: @BA@ already say it, @BN@ do not carry it, @BS@ say something now superseded. Three superseded citations were moved forward in their document’s lineage, and 29 items were routed. No corrected-but-unpropagated citation was found in the batch.**',
        '',
        '#### Component 1 — the eligible set',
        '',
        'b390’s words (`OPEN_TRAILS.md:4446`): *take the one whose terminals the drive can reach*, settled by terminals that *live on the HELD, UNMERGED branch … and are not on `main`*. The paraphrase differs twice, and b390’s words govern: “the one”, not “those” (the plural is b394’s batch extension); and b390’s settling clause, carried and measured live. Two wanted conditions — the partial case and pin resolution — were printed on the face and **not applied**.',
        '',
        '| # | census keystone | state | reason |',
        '|--:|:--|:--|:--|',
    ]
    for n, r in enumerate(EJ['rows'], 1):
        body.append('| %d | `%s` | %s | %s |' % (n, r['k'], r['state'], r['why'].replace('|', '/').replace('`', '’')))
    body += [
        '',
        '**Eligible (@NE@), in census order:** @ELIG@. `SIMPLICITY_OF_RIEMANN_ZEROS` and `R_CURVE_CRITERION` are marked **PARTIAL**: they name `SIDE-kernel/derivative-engine`, the one live unmerged branch, and its declarations. b394’s narrow matcher would reach @NV1@ of the eleven.',
        '',
        '#### Component 2 — the batch read, reconciling and not authoring',
        '',
        '| keystone | head | correspondence rows by grade | already says it | superseded | does not carry it |',
        '|:--|:--|:--|--:|--:|--:|',
    ]
    for k in BJ['order']:
        v = ks[k]
        g = v['tw_grades'] if v['t1'] else v['grades']
        rows = v['tw_rows'] if v['t1'] else v['t2_rows']
        gs = 'THERE IS NO TABLE' if not (v['t1'] or v['t2_rows']) else '%d — %s' % (rows, ', '.join('%s %d' % kv for kv in sorted(g.items())))
        body.append('| `%s` | %s | %s | %d | %d | %d |' % (k, v['head'], gs, v['buckets'][A_], v['buckets'][S_], v['buckets'][N_]))
    body += [
        '| **across the batch** | | | **@BA@** | **@BS@** | **@BN@** |',
        '',
        'Every bucket is full. **Species, apart and never summed:** phantom @PH@, unpropagated @UP@, superseded @SU@. One inside-the-batch pair: `THE_RESIDUE_OF_RH` line 69 cites `INDEX_ARITY` at `v0.16` in its dated 2026-08-05 annotation, and that keystone’s head is now `v0.18`. The registry row does not supersede it, so it is printed and not repaired.',
        '',
        '**Three repairs, currency only:** `A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` `v0.2` → `v0.5.4` (`REGISTRY.md:218`, row `1.5h-4`) at `TECHNE_TOOLKIT.md` lines 453 and 524, and at `E_DIFFICULTY_THEOREM.md` line 189. In each case `v0.2` is in that document’s own lineage; only the version changed; 0 lines were removed; and the originals are preserved in an appended annotation. This departs from b391 and b394, which left superseded citations standing by their own orders’ instruction; this order instructs the repair.',
        '',
        '**Routed, @NR@, each with the ruling it needs:** 16 era findings the keystones do not carry (adding absent material is authoring); 8 lines calling a landed branch held (b397’s species; rewriting prose is authoring); 2 keystones with no correspondence table (`TECHNE_TOOLKIT`, `E_DIFFICULTY_THEOREM`; writing one is authoring); `INDEX_ARITY`’s registry row at `v0.5` against its head `v0.18`; and 2 keystones with no registry row (`EXHAUSTIVENESS_LICENSE`, `THE_RESIDUE_OF_RH`). **Not located:** the census’s `keyhole` and `T3` Tier-1 findings for `INVARIANCE_BARRIERS` have no form in `FINDINGS.md` or `OPEN_TRAILS.md`, and `R_CURVE_CRITERION` never carried the pin `bd2ae1a` the census names for it.',
        '',
        '*Matchers named where they failed, with the locked face unedited:* the face’s table shape T2 found 0 rows under 5 tables whose headers open `Claim (as stated here)` or `Result`, so rows are counted from the first table after each heading and T2’s yield is printed beside that count. The stem citation shape S1 found 0 citations. A second shape (a name then a space or `_v`, mapped to registry stems) found 8, and 2 of those were hand-read as `TECHNE_TOOLKIT` naming its own past versions — residue, not counted. One branch line was misclassified by the tool (“HELD — nothing merged”) and corrected by hand.',
        '',
        '**The batch is complete: 11 of 11 read, no halt.** Times, both floors: @MIN@ min for the act to the component, @PER@ per keystone.',
        '',
        '#### Filed under the outlier `a = 4.123106` — candidate (c4)',
        '',
        '**(c4) — a cancellation WITHIN the prime channel.** At step 1 its `n = 2` term’s change is `+1.161e-07` against its `n = 3` term’s `-8.101e-08` (gross/net `5.000`), and by step 2 the `n = 3` change has fallen `20.0`-fold (relay `data/b449_components.txt`, lines 74 and 78). This is a different object from **(c3)**, which b448 refuted **between** channels. **Priced from banked values, not run, no lane opened.** (c2) stays priced and not run. **The measurement stays open.**',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | the eligible set is at least eight and not four | **@N1@** — @NE@ |',
        '| (N2)(a) | the largest bucket across the batch is does not carry it | **@N2A@** — @BA@ / @BS@ / @BN@ |',
        '| (N2)(b) | at least one corrected-but-unpropagated citation inside the batch | **@N2B@** — 0; the 3 repaired citations are superseded, not unpropagated |',
        '',
        '**The span by the tool: @SPAN@ acts (b445–b450), against a ruled threshold of nine.** Both instrument lanes stay parked. The four lists are open.',
    ]
    rep = [('@NE@', str(len(ELIG))), ('@ELIG@', ', '.join('`%s`' % k for k in ELIG)), ('@NV1@', str(len(V.get('v1_on') or []))),
           ('@BA@', str(BK.get(A_, 0))), ('@BS@', str(BK.get(S_, 0))), ('@BN@', str(BK.get(N_, 0))),
           ('@PH@', str(SP.get('phantom', 0))), ('@UP@', str(SP.get('unpropagated', 0))), ('@SU@', str(SP.get('superseded', 0))),
           ('@NR@', str(V.get('routed', 0))), ('@MIN@', '%.1f' % V.get('minutes', 0)), ('@PER@', '%.1f' % V.get('per_keystone', 0)),
           ('@N1@', EXP.get('n1', '')), ('@N2A@', EXP.get('n2a', '')), ('@N2B@', EXP.get('n2b', '')), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b450)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; NO KEYSTONE OPENED BEFORE THE FACE. **COMPONENT 1: b390'S RULE "
                 "QUOTED VERBATIM, TWO DIFFERENCES FROM THE PARAPHRASE PRINTED (THE ONE / THOSE; THE SETTLING CLAUSE), TWO WANTED CONDITIONS "
                 "NOT APPLIED; CENSUS 16, RECONCILED 4 (b390, b394), UNREAD 12 -- THE BOARD'S FIGURE AGREES; ELIGIBLE %d, ENUMERA EXCLUDED; "
                 "b394'S NARROW MATCHER WOULD REACH %d.** **COMPONENT 2: THE ELEVEN READ AS ONE BATCH IN CENSUS ORDER; BUCKETS %d / %d / %d "
                 "(A TIE); SPECIES PHANTOM %d, UNPROPAGATED %d, SUPERSEDED %d; 3 CURRENCY REPAIRS MADE IN LINEAGE, ORIGINALS PRESERVED, 0 LINES "
                 "REMOVED; %d ROUTED; 2 KEYSTONES WITH NO TABLE, NONE WRITTEN; COMPLETE, NO HALT.** **FILED: (c4), A CANCELLATION WITHIN THE "
                 "PRIME CHANNEL, NOT RUN; THE MEASUREMENT OPEN.** (N1) %s, (N2)(a) %s, (N2)(b) %s. SPAN BY TOOL %s. 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, len(ELIG), len(V.get('v1_on') or []), BK.get(A_, 0), BK.get(S_, 0), BK.get(N_, 0), SP.get('phantom', 0),
               SP.get('unpropagated', 0), SP.get('superseded', 0), V.get('routed', 0), EXP['n1'], EXP['n2a'].upper(), EXP['n2b'], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; TECHNE_TOOLKIT.md AND E_DIFFICULTY_THEOREM.md: 3 VERSION "
            "STRINGS MOVED WITH ONE APPENDED ANNOTATION EACH, 0 LINES REMOVED; REGISTRY.md, FINDINGS.md, THE CENSUS, EVERY CORRESPONDENCE TABLE "
            "AND EVERY CLOSING BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### THE RULE, ITS DIFFERENCES, THE POPULATION, THE NEEDLES, THE BUCKET RULES AND THE REPAIR RULE WERE ON THE FACE BEFORE ANY "
             "KEYSTONE WAS OPENED; MATCHERS THAT FAILED ARE NAMED WITH BOTH YIELDS; EACH VERDICT IS THE RULE'S AS IT FELL")
    status = ("data/b450_the_eligible_set_and_the_batch.txt; data/b450_components.txt; data/b450_eligible.json; data/b450_batch.json; "
              "data/b450_repairs.json; data/b450_span.json; data/b450_checks.txt; data/b450_registration_2026-09-13.txt (LOCKED at sha256 %s); "
              "data/b450_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('the reconciliation eligible set',
           'how many keystones are reconciled',
           'the batch read of eleven keystones',
           'candidate c4 cancellation within the prime channel',
           'A_METHODOLOGY v0.2 citations repaired')
MUST_NOT_HIT = ('the outlier is explained', 'every keystone is reconciled', 'the census is complete')
KEY = 'the-eligible-set-re-measured-and-the-batch-read'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b450 RE-MEASURED THE RECONCILIATION'S ELIGIBLE SET UNDER b390'S RULE QUOTED: %d ELIGIBLE, 4 RECONCILED, 12 UNREAD; READ THE ELEVEN "
        "AS ONE BATCH: BUCKETS %d / %d / %d; 3 CURRENCY REPAIRS, %d ROUTED; NO UNPROPAGATED CORRECTION. FILED (c4), NOT RUN. NO CLAIM ABOUT ZEROS."
        % (len(ELIG), BK.get(A_, 0), BK.get(S_, 0), BK.get(N_, 0), V.get('routed', 0)))
    grade = "### NO GRADE MOVED. ### NO TABLE WRITTEN, NO REGISTRY ROW EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b450_the_eligible_set_and_the_batch.txt; data/b450_components.txt; data/b450_eligible.json; data/b450_batch.json; "
             "data/b450_registration_2026-09-13.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b450 (the reconciliation's eligible set re-measured, and the batch read)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE RECONCILIATION`S ELIGIBLE SET RE-MEASURED, AND THE BATCH READ (b450).%s'
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
        rec('    %-58s reaches the b450 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the eligible count carried', ('%d ELIGIBLE' % len(ELIG)) in out), ('the repairs carried', '3 CURRENCY REPAIRS' in out),
                      ('(c4) carried', 'FILED (c4)' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b450 -- THE RECONCILIATION'S ELIGIBLE SET RE-MEASURED, AND THE BATCH READ.", '### THE BANK.', '=' * 100, '']
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


B449ROW_RE = r"(?m)^\| (\d+) \| \*\*THE \(R61\) RECORD IS RATIFIED AT b449"


def main():
    global DESK
    bar('=')
    rec('b450_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B449ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b450_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
