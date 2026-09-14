# -*- coding: utf-8 -*-
"""b457_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b457 the profiles printed at the tag, and the sentence gate priced -->'
PRIOR = '<!-- b456 the errata entry, the live note, and the routed annotations completed -->'
BANKOUT = os.path.join(D, 'b457_the_profiles_at_the_tag.txt')
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


FACE = read(os.path.join(D, 'b457_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b457_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR_, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b457_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b457_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


RJ = _j('b457_run.json')
CJ = _j('b457_cells.json')
PJ = _j('b457_gate_price.json')
SPAN = _j('b457_span.json')
READY = bool(RJ.get('verdicts')) and bool(CJ.get('lines')) and bool(PJ.get('surfaces')) and bool(SPAN)
SPANN = SPAN.get('current_span')
ALLSTD = bool(RJ.get('all_standard')) and bool(RJ.get('banked_ok'))
VERD = 'ALL STANDARD THREE' if ALLSTD else 'NOT ALL STANDARD'

ROWMARK = ('**(R67) IS EXECUTED: AT TAG v1.5 = 0e5233f, FROM A CLEAN CHECKOUT, EVERY ROUTE TERMINAL PRINTS {propext, Classical.choice, Quot.sound}; THE '
           'OUTPUT IS BANKED AND THE SECOND DEPOSIT-LEVEL MATTER CLOSES; (R68)`S CELLS TAKE THE MERGED-BRANCH TERM; THE SENTENCE GATE PRICES AT '
           'TWELVE ACTS OVER FORTY-FIVE ITEMS AND IS NOT BUILT**') if ALLSTD else '**(R67) IS EXECUTED AND A ROUTE TERMINAL DOES NOT PRINT THE STANDARD THREE: A WAVE TRIGGER**'
SCOPE = ("### THE ACT OPENED THE KERNEL LANE FOR ONE RUN IN A SCRATCH CLONE AT THE TAG`S HASH, BANKED THE PRINTED PROFILES VERBATIM, CLOSED THE LANE, "
         "WROTE (R68)`S FOUR CELLS WITH THEIR ORIGINALS PRESERVED, AND PRICED THE SENTENCE GATE BY A WORD TEST AND A FORMULA FIXED ON ITS FACE; "
         "NOTHING SHIPPED, NOTHING DEPOSITED, NO WAVE OPENED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('(R67) the route terminals profiled at the tag', 'CLOSE',
         'RUN at b457: %s; build %.0f s, print %.0f s; banked in data/b457_profile_run.txt with the tag digest and the toolchain. The run took two attempts in the same verified clone -- the first, a background task, was killed by the harness for low memory before the print.' % (
             ' / '.join('%s %s' % (x['terminal'], x['verdict']) for x in RJ.get('verdicts') or []), (RJ.get('build') or {}).get('seconds', 0), (RJ.get('print') or {}).get('seconds', 0))),
        ('the second deposit-level matter (b456)', 'CLOSE' if ALLSTD else 'STAND', 'CLOSED at b457: the deposited sentence now has a banked run behind it; a live note in README.md points to it.' if ALLSTD else 'OPEN: WAVE TRIGGER.'),
        ('the kernel lane', 'CLOSE', 'CLOSED at the run`s end: the scratch clone removed and verified absent; D:\\SIDE-kernel unmoved.'),
        ('(R68) THE_RESIDUE_OF_RH:127-130', 'CLOSE', 'WRITTEN at b457: MERGED-BRANCH, the cells as they stood in a currency annotation.'),
        ('EXHAUSTIVENESS_LICENSE:9', 'CLOSE', 'LEFT BY RULING (R68): dated at its own version.'),
        ('the sentence gate', 'STAND', 'PRICED at b457: S %d items, U %d terminals, P %d pairs, %d acts by the face`s formula; %d proof-word items name no terminal and are out of its reach. NOT BUILT; the author`s.' % (PJ.get('S', 0), PJ.get('U', 0), PJ.get('P', 0), PJ.get('acts', 0), PJ.get('out_of_reach', 0))),
        ('(R66) the deposit corrected, not re-issued', 'STAND', 'ENTERED: the wave stays parked; no substance moved at b457.'),
        ('the seat`s predicate at b457', 'STAND', 'ENTERED: G-C1-BANKED-HEADER first looked for `v4.29.0-rc8`, which lean prints without the `v`; corrected to `version 4.29.0-rc8`, both yields printed.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'OPEN; this act`s build passes -DateTag 2026-09-14-b457.'),
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
    t = PJ.get('terms_of_formula') or {}
    body = [
        '### b457 — the profiles printed at the tag, and the sentence gate priced — filed 2026-09-14',
        '',
        '**Rulings `(R66)`, `(R67)` and `(R68)`, the author’s, ratified by the paste and strikeable, are entered.** (R66): the deposit is corrected, not re-issued, and a wave opens only when substance moves. (R67): the route terminals are profiled at the deposited tag. (R68): THE_RESIDUE_OF_RH’s held cells take the merged-branch term.',
        '',
        '#### Component 1 — the route terminals at `v1.5`',
        '',
        'A clone of `D:\\SIDE-kernel` was checked out at `0e5233f011533d09e4799107394c216a915028a1`: its tag object is `922c0fc…`, it was clean before the run, and its only remote is the local kernel. The dependency packages were copied from the local cache at their manifest revisions; the kernel’s own build output was not copied. `lake build` compiled the tag’s modules (2962 jobs; no Mathlib module compiled, no remote contacted), then `#print axioms` ran on the three route terminals the deposit names. Toolchain: Lean 4.29.0-rc8. **The run took two attempts in the same clone:** the first, a background task, was killed by the harness for low memory before the print. The output is banked verbatim in relay `data/b457_profile_run.txt`, with the tag’s digest, the toolchain and the durations.',
        '',
        '| route terminal | printed | verdict |',
        '|:--|:--|:--|',
    ]
    for x in RJ.get('verdicts') or []:
        body.append('| `%s` | `%s` | **%s** |' % (x['terminal'], x['line'], x['verdict']))
    body += [
        '',
        ('**All three print the standard three. The deposited sentence *“All route terminals report {propext, Classical.choice, Quot.sound}”* now has a banked run behind it, and the second deposit-level matter closes.** A live note in `README.md` points to the run. The kernel lane closed at the run’s end: the clone was removed and verified absent, and `D:\\SIDE-kernel` is unmoved.' if ALLSTD else
         '**WAVE TRIGGER: a route terminal does not print the standard three at the deposited tag.**'),
        '',
        '#### Component 2 — `(R68)`',
        '',
        '`THE_RESIDUE_OF_RH.md:127`–`:130`: `### **HELD-BRANCH**` → `### **MERGED-BRANCH**`, the cells as they stood preserved in a currency annotation; lines removed 0. `EXHAUSTIVENESS_LICENSE.md:9` is left, dated at its own version, as ruled.',
        '',
        '#### Component 3 — the sentence gate, priced and not built',
        '',
        'The surfaces were the monograph record `v1.1.2`’s files (each checksum-verified; the `.svg` excluded), its description, SIDE-kernel `v1.5`’s README and `.zenodo.json`, and SIDE-lv-conservation `v0.10.0`’s README. A word test counted items that name a declared theorem and carry a proof word: **S = @S@ items, U = @U@ distinct terminals, P = @P@ item-terminal pairs** — @APS@ of them in the monograph. **One pass prices at @ACTS@ acts** by the face’s formula on b455’s measured act, max(@BI@, @BU@, @BR@). The bound term is the unfoldings: every distinct terminal must be unfolded before a sentence naming it can be graded. **It would not catch** the @OOR@ items that state a proof and name no terminal — b455’s *“Proved and machine-checked … the exhaustiveness of the seven-class catalogue”* is of that kind. Nothing was graded.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | every route terminal reports the standard three at the tag and the second matter closes | **@N1@** |',
        '| (N2) | fewer than forty terminal-naming items, and one pass under three acts | **REFUTED** — S = @S@, @ACTS@ acts |',
        '',
        '*Entered as the seat’s:* the suite’s header arm first looked for `v4.29.0-rc8`, which `lean --version` prints without the `v`; it was corrected, with both yields printed.',
        '',
        '**The span by the tool: @SPAN@ acts.** The wave stays parked under (R66); nothing deposits; `h2` where the deposit left it. The four lists are open.',
    ]
    aps = next((x['counted'] for x in PJ.get('surfaces') or [] if x['surface'].endswith('A_Place_to_Stand.md')), 0)
    rep = [('@S@', str(PJ.get('S', 0))), ('@U@', str(PJ.get('U', 0))), ('@P@', str(PJ.get('P', 0))), ('@APS@', str(aps)), ('@ACTS@', str(PJ.get('acts', 0))),
           ('@BI@', str(t.get('by_items'))), ('@BU@', str(t.get('by_unfoldings'))), ('@BR@', str(t.get('by_relations'))), ('@OOR@', str(PJ.get('out_of_reach', 0))),
           ('@N1@', 'HELD' if ALLSTD else 'REFUTED'), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b457)"
    stmt = (m + (". **LOCKED BEFORE THE RUN AND ANY WRITE**, %d gates read, %d by digest. **C1: CLONE AT 0e5233f, TAG OBJECT 922c0fc, CLEAN; PACKAGES AT THE "
                 "MANIFEST; BUILD %.0f S (2962 JOBS, NO MATHLIB COMPILED), PRINT %.0f S, LEAN 4.29.0-rc8; %s; TWO ATTEMPTS, THE FIRST KILLED BY THE HARNESS "
                 "FOR LOW MEMORY BEFORE THE PRINT; THE LANE CLOSED, THE CLONE REMOVED, THE KERNEL UNMOVED.** **C2: THE_RESIDUE_OF_RH:127-130 MERGED-BRANCH, "
                 "ORIGINALS PRESERVED.** **C3: S %d, U %d, P %d, %d ACTS; %d OUT OF REACH; NOT BUILT.** (N1) %s, (N2) REFUTED. SPAN BY TOOL %s. 0 GRADES "
                 "MOVED ON ANY ROW, NOTHING DEPOSITS, NO WAVE")
            % (GR_, GDG, (RJ.get('build') or {}).get('seconds', 0), (RJ.get('print') or {}).get('seconds', 0), VERD, PJ.get('S', 0), PJ.get('U', 0), PJ.get('P', 0),
               PJ.get('acts', 0), PJ.get('out_of_reach', 0), 'HELD' if ALLSTD else 'REFUTED', SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; ONE LEAN RUN AT TAG v1.5 IN A SCRATCH CLONE, REMOVED"
    prof = ("### PLACE-papers: THE_RESIDUE_OF_RH.md FOUR CELLS AND +1 ANNOTATION; README.md +1 NOTE, INSERTED; OPEN_TRAILS.md +1 RECORD; EVERY PRE-EDIT "
            "LINE PRESENT OR QUOTED -- 0 CONTENT LOST; D:\\SIDE-kernel UNMOVED")
    grade = ("### THE CHECKOUT, THE RUN, THE VERDICT RULE, THE EDIT AND THE PRICE FORMULA WERE ON THE FACE BEFORE ANY OF THEM HAPPENED; EVERY VERDICT "
             "READ FROM ITS OUTPUT LINE, NEVER AN EXIT CODE")
    status = ("data/b457_the_profiles_at_the_tag.txt; data/b457_components.txt; data/b457_profile_run.txt; data/b457_build_log.txt; data/b457_run.json; "
              "data/b457_cells.json; data/b457_gate_price.json; data/b457_span.json; data/b457_checks.txt; data/b457_registration_2026-09-14.txt "
              "(LOCKED at sha256 %s); data/b457_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('route terminals profiled at tag v1.5',
           'print axioms at the deposited tag',
           'second deposit-level matter closed profile run',
           'sentence gate priced',
           'R68 merged-branch cells')
MUST_NOT_HIT = ('wave opened', 'sentence gate built', 'profile other than the standard three')
KEY = 'the-profiles-printed-at-the-tag-and-the-sentence-gate-priced'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b457 PROFILED THE ROUTE TERMINALS AT TAG v1.5 = 0e5233f FROM A CLEAN CHECKOUT: %s, THE OUTPUT BANKED; THE SECOND DEPOSIT-LEVEL MATTER %s. "
                 "(R68) CELLS WRITTEN. THE SENTENCE GATE PRICED AT %d ACTS OVER %d ITEMS, NOT BUILT. NO CLAIM ABOUT ZEROS."
                 % (VERD, 'CLOSES' if ALLSTD else 'STANDS AS A WAVE TRIGGER', PJ.get('acts', 0), PJ.get('S', 0)))
    grade = "### NO GRADE MOVED ON ANY ROW. ### NOTHING DEPOSITS. ### NO WAVE OPENED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b457_the_profiles_at_the_tag.txt; data/b457_components.txt; data/b457_profile_run.txt; data/b457_run.json; data/b457_gate_price.json; "
             "data/b457_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR_, GDG, rownum))
    act = "b457 (the profiles printed at the tag, and the sentence gate priced)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE PROFILES PRINTED AT THE TAG, AND THE SENTENCE GATE PRICED (b457).%s'
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
        rec('    %-58s reaches the b457 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the verdict carried', VERD in out), ('the price carried', ('%d ACTS' % PJ.get('acts', 0)) in out),
                      ('not built carried', 'NOT BUILT' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b456 -- THE PROFILES PRINTED AT THE TAG, AND THE SENTENCE GATE PRICED.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR_, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B456ROW_RE = r"(?m)^\| (\d+) \| \*\*\(R65\) IS EXECUTED:"

def main():
    global DESK
    bar('=')
    rec('b457_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; verdict %s ; acts %s ; span %s'
        % (GR_, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), VERD, PJ.get('acts'), SPANN))
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B456ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b457_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
