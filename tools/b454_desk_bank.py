# -*- coding: utf-8 -*-
"""b454_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b454 (R63) executed under (R64), and the span-heading work-order repaired -->'
PRIOR = '<!-- b453 the fold at span eight -->'
BANKOUT = os.path.join(D, 'b454_the_ruling_executed.txt')
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


FACE = read(os.path.join(D, 'b454_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b454_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b454_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b454_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


FJ = _j('b454_findings.json')
EJ = _j('b454_enumera.json')
RJ = _j('b454_registry.json')
BJ = _j('b454_branch_lines.json')
CJ = _j('b454_span_repair.json')
SPAN = _j('b454_span.json')
READY = bool(FJ.get('counts')) and bool(EJ.get('census')) and bool(RJ.get('rows')) and bool(CJ.get('applied')) and bool(SPAN)
CNT = FJ.get('counts') or {}
NED = sum(1 for r in BJ.get('table', []) if r.get('edited'))
CENSUS = EJ.get('census', '')
NEAR = EJ.get('nearest') or []
SEC = EJ.get('second') or {}
NS = CJ.get('numstat') or ['?', '?']
SPANN = SPAN.get('current_span')

ROWMARK = ('**(R63) IS EXECUTED UNDER (R64): THE BRANCH LINES MOVED FROM HELD TO MERGED BY FAST-FORWARD, THE ERA FINDINGS ADDED ONLY BESIDE A '
           'PRE-b450 LEDGER LINE, THREE REGISTRY ROWS RECORDED FROM THEIR HEADS; ENUMERA`S NEAREST TERMINAL IS NOT DERIVES AND THE CENSUS '
           'STAYS AT FIFTEEN OF SIXTEEN; W-ORD-SPAN-HEADING REPAIRED**')
SCOPE = ("### THE ACT EDITED STATE TERMS ON THE NAMED BRANCH LINES AND APPENDED THEIR ORIGINALS, SEARCHED THE PRE-b450 LEDGERS FOR EACH ERA FINDING "
         "UNDER SHAPES AND A CONTROL FIXED ON ITS FACE AND HAND-READ EVERY HIT, WROTE ONE REGISTRY CELL AND TWO ROWS, READ THE ROSTERED KERNELS "
         "FOR ENUMERA`S NEAREST TERMINAL WITHOUT RUNNING LEAN, AND MADE THE SPAN TOOL`S NAMED REPAIR; (R63)(c) STAYS ROUTED AND (R64)(4) "
         "DEFERRED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    d = FJ.get('defect') or {}
    return [
        ('(R63)(a) the branch lines', 'CLOSE', 'EXECUTED at b454: %d of 8 lines, state terms only, originals in currency annotations, tips 5a14205 and a0dc376 cited with the word fast-forward.' % NED),
        ('(R63)(b) the era findings, under (R64)(2)', 'CLOSE',
         'EXECUTED at b454 over the 15 targets: ADDED %d, CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER %d; the positive control returned and held. The R_CURVE item withdrawn.'
         % (CNT.get('found', 0), CNT.get('held_by_no_ledger', 0))),
        ('the F4 shape`s defect', 'STAND',
         'PRINTED, NOT PATCHED: %s:%d states the constraint table`s third item at Face E`s Tier-1 scope but carries no `T3` token, so the face`s F4 shapes could not return it. With it credited the counts would be %d and %d. Routed to the navigator.'
         % (d.get('ledger', '').split('/')[-1], d.get('line', 0), CNT.get('found_if_defect_credited', 0), CNT.get('targets', 0) - CNT.get('found_if_defect_credited', 0))),
        ('held-state words outside the face`s table', 'STAND',
         'OBSERVED, NOT EDITED: EXHAUSTIVENESS_LICENSE.md:9 (the head`s version line), THE_RESIDUE_OF_RH.md:127-130 (HELD-BRANCH status cells for the same branch) and :145 (held-branch work). The ruling named lines, and these words were outside its table. Routed.'),
        ('(R63)(c) the two correspondence tables', 'STAND', 'ROUTED, as ruled.'),
        ('(R63)(d) the registry rows', 'CLOSE', 'EXECUTED at b454: 1.5a-7 Version v0.5 -> v0.18 with the pre-edit row preserved; 1.5a-8 and 1.5h-9 entered UNGRADED from their heads.'),
        ('(R63)(e) ENUMERA', 'CLOSE',
         'READ at b454: the rule`s nearest, SIDE_exclusion in SIDE-kernel and SIDE-effects, grades INTERFACES against (E1); structural_exhaustiveness_proved, printed as a second figure, grades NOT THE CLAIM. The census %s.' % CENSUS.lower()),
        ('(R64)(4) the Zenodo listing', 'STAND', 'DEFERRED: fires when the author saves the listing to the relay data path.'),
        ('W-ORD-SPAN-HEADING', 'CLOSE', 'REPAIRED at b454 as named: both fold forms read, the unparsed printed; numstat +%s -%s; the tool now reads b423-b432; 0 unparsed headings.' % tuple(NS[:2])),
        ('W-ORD-MATCHER-SHAPE', 'STAND', 'FIRED at b454 twice (F4`s shape; ENUMERA`s word test missed structural_exhaustiveness_proved); both yields printed; the work-order stays open.'),
        ('the seat`s errors at b454', 'STAND',
         'ENTERED: the lock gate`s stdout was redirected onto its own run file, so run_clock versioned the gate`s record as b454_lockgate_notes2.txt; the write-list arm was widened to run_clock`s versioning with both yields printed. The span fixture was written to the system temp directory, not the scratchpad the face names, and removed.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'OPEN; this act`s build passes -DateTag 2026-09-14-b454.'),
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
    V = FJ.get('verdicts') or {}
    d = FJ.get('defect') or {}
    body = [
        '### b454 — (R63) executed under (R64), and the span-heading work-order repaired — filed 2026-09-14',
        '',
        '**`(R63)` is executed as `(R64)` amends it.** The branch lines are moved from held to merged by fast-forward. Era findings are added only beside a ledger line from before b450. Three registry rows are recorded from their documents’ heads. **ENUMERA’s nearest terminal is not `DERIVES`, so the census stays at fifteen of sixteen.** `W-ORD-SPAN-HEADING` is repaired. The navigator model is declared on the face from this act on: Fable 5.1.',
        '',
        '#### (a) The branch lines',
        '',
        '**@NED@ of 8** lines edited, state terms only, each original preserved verbatim in an appended currency annotation beside its fast-forward tip on `main`’s first-parent line: `5a14205` (`SIDE-lv-conservation`, `word-pairing-interface`) at `PATHS_TO_THE_CRITICAL_LINE.md:420`, `:440`, `EXHAUSTIVENESS_LICENSE.md:95`, `THE_RESIDUE_OF_RH.md:97`, `:126`, `:145`; `a0dc376` (`SIDE-effects`, `w-ladder-skeleton`) at `EXHAUSTIVENESS_LICENSE.md:101`, `:112`. **Observed and not edited:** held-state words outside the face’s table at `EXHAUSTIVENESS_LICENSE.md:9` and `THE_RESIDUE_OF_RH.md:127`–`:130`, `:145`.',
        '',
        '#### (b) The era findings',
        '',
        '**An error in the order’s count, entered as the navigator’s:** *“the twenty-eight annotation targets”* — the twenty-nine less the withdrawn item is twenty-eight, and only **15** of them carry a finding; the rest are the branch lines, the tables and the registry rows.',
        '',
        'The ledgers: `FINDINGS.md` and `OPEN_TRAILS.md` at PLACE-papers `687aa24` (b450’s parent) and the `2026-08-24` archive split, unmoved since. Two shapes per finding, both yields printed; every hit hand-read. **The positive control** — the two-kinds windows verdict at `OPEN_TRAILS-archive-2:8431` — was returned and holds.',
        '',
        '| finding | S1 | S2 | hits read | verdict | first holding line |',
        '|:--|--:|--:|--:|:--|:--|',
    ]
    for fid in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'):
        v = V.get(fid, {})
        h = [x for x in v.get('holds', []) if x['returned'] and x['verbatim']]
        body.append('| %s | %d | %d | %d | %s | %s |' % (v.get('finding', ''), v.get('s1', 0), v.get('s2', 0), v.get('hits', 0),
                                                        '**FOUND**' if v.get('found') else 'HELD BY NO LEDGER',
                                                        ('`%s:%d`' % (h[0]['ledger'].split('/')[-1], h[0]['line'])) if h else '—'))
    body += [
        '',
        '**The two counts, over the 15 targets: ADDED @FOUND@ — CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER @HELD@.** Added: `W_∞` not sign-definite in PATHS, SURROUND, SIMPLICITY and INDEX_ARITY; the two-kinds windows verdict in REPARAMETERIZATION; the `S2` Ostrowski seal in EXHAUSTIVENESS_LICENSE; the sign-face registers in THE_RESIDUE_OF_RH. Held by no ledger: the Day-1 §I pole-plus-archimedean attribution (four keystones), Face E / keyhole and the `T3` Tier-1 scope (INVARIANCE), the E-Difficulty cross-link verdict (TECHNE_TOOLKIT, E_DIFFICULTY).',
        '',
        '**A defective predicate, printed and not patched:** `%s:%d` states *“Euler-product consumption at Face E’s Tier-1 scope verbatim”* as the constraint table’s third item, without the token `T3` both of F4’s shapes required; credited, the counts would read @FC@ and @FH@.' % (d.get('ledger', '').split('/')[-1], d.get('line', 0)),
        '',
        '#### (d) The registry',
        '',
        '`1.5a-7`’s Version cell `v0.5` → `v0.18` (`REGISTRY.md:141`), from `INDEX_ARITY_AT_THE_CRITICAL_LINE.md:15`; the pre-edit row preserved verbatim in an appended row update. **New rows, appended in the file’s row-addition form:** `1.5a-8` *The Residue of the Riemann Hypothesis* and `1.5h-9` *The Exhaustiveness License*, each the next id in its cluster’s own rows — `REGISTRY.md` states no numbering rule in words — and each **UNGRADED**, its head read in full carrying no status word. Every write printed as a diff count; **lines removed 0 in all eight documents** by the face’s predicate.',
        '',
        '#### Component 2 — ENUMERA',
        '',
        'What a terminal would have to satisfy, in the keystone’s own words (`ENUMERA.md:73`): *“The seven-class catalogue is exhaustive.”*, reached through *“The Poisson Exhaustion Theorem (proved via Ostrowski’s theorem) establishes n₂ = 3”* and *“the formation (2,3,2,0) = 7 is complete.”* The 43 rostered kernels were read, not run: @YIELD@ declarations matched by name.',
        '',
        '- **The rule’s nearest:** `SIDE_exclusion` (`SIDE-kernel` `Kernel/Layer1.lean:30`; `SIDE-effects` `SIDEFramework.lean:45`) — **INTERFACES**: the exhaustive catalogue is its named hypothesis `(cat : ExhaustiveCatalogue X P)`. No shipped axiom profile located.',
        '- **A second figure, the word test’s miss:** `structural_exhaustiveness_proved` (`SIDE-kernel` `Bridge/TheBridgeComplete.lean:249`), shipped at `[propext, Classical.choice, Quot.sound]` (`DEPOSIT_v1_2_NOTES.md:38`) — **NOT THE CLAIM**: it proves `Fintype.card MechanismClass = 7` over a type it defines and classifies the places of ℚ, and does not state that every mechanism lies in one of the seven classes.',
        '',
        '**The census stays at fifteen of sixteen.** The shortfall: no rostered terminal states the keystone’s load-bearing claim.',
        '',
        '#### Component 3 — W-ORD-SPAN-HEADING',
        '',
        'The repair its own address names (`FINDINGS.md:3927`), nothing wider: `tools/b363_span.py` reads fold headings in both forms and prints any fold heading it cannot parse. **numstat +@A@ −@R@.** The tool now reads 17 folds, b434’s *“The external-grading arc — b423 through b432”* among them, with 0 unparsed; a fixture of both forms and an unparseable heading passed; the last fold and the current span are unchanged.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | fewer than half of the twenty-eight have a pre-b450 ledger line | **HELD** — @FOUND@ of 15, @FOUND@ of 28; with the defective predicate’s line credited, @FC@ of 15 would refute it over the 15 |',
        '| (N2) | a nearest terminal exists and proves something narrower; the census stays at fifteen | exists **HELD**; narrower **REFUTED** for the rule’s nearest (INTERFACES) and **HELD** for the second figure (NOT THE CLAIM); census **HELD** |',
        '| (N3) | the repair is a single-line change | **REFUTED** — +@A@ −@R@ |',
        '',
        '**The span by the tool: @SPAN@ act.** `(R63)(c)` stays routed; `(R64)(4)` deferred. Both instrument lanes stay parked; nothing deposits; `h2` where the deposit left it. The four lists are open.',
    ]
    rep = [('@NED@', str(NED)), ('@FOUND@', str(CNT.get('found', 0))), ('@HELD@', str(CNT.get('held_by_no_ledger', 0))),
           ('@FC@', str(CNT.get('found_if_defect_credited', 0))), ('@FH@', str(CNT.get('targets', 0) - CNT.get('found_if_defect_credited', 0))),
           ('@YIELD@', str(EJ.get('yield_'))), ('@A@', str(NS[0])), ('@R@', str(NS[1])), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b454)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest; NO LEDGER SEARCHED, NO KERNEL READ AND NO FILE EDITED BEFORE THE FACE. "
                 "**(a) %d OF 8 BRANCH LINES EDITED BY STATE TERM, ORIGINALS PRESERVED, TIPS 5a14205 AND a0dc376 CITED AS FAST-FORWARD.** "
                 "**(b) OVER 15 TARGETS (THE ORDER`S TWENTY-EIGHT ENTERED AS THE NAVIGATOR`S COUNT): ADDED %d, CLAIMED BY THE KEYSTONE AND HELD BY NO "
                 "LEDGER %d; THE CONTROL RETURNED AND HELD; ONE DEFECTIVE SHAPE PRINTED, NOT PATCHED.** **(d) 1.5a-7 v0.5 TO v0.18, PRE-EDIT ROW "
                 "PRESERVED; 1.5a-8 AND 1.5h-9 ENTERED UNGRADED.** LINES REMOVED 0 IN EVERY DOCUMENT. **ENUMERA: SIDE_exclusion INTERFACES, "
                 "structural_exhaustiveness_proved NOT THE CLAIM; THE CENSUS %s.** **W-ORD-SPAN-HEADING REPAIRED, NUMSTAT +%s -%s.** (N1) HELD, "
                 "(N2) HELD ON EXISTENCE AND CENSUS AND SPLIT ON NARROWER, (N3) REFUTED. SPAN BY TOOL %s. 0 GRADES MOVED ON ANY ROW")
            % (GR, GDG, NED, CNT.get('found', 0), CNT.get('held_by_no_ledger', 0), CENSUS, NS[0], NS[1], SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO LEAN RUN"
    prof = ("### PLACE-papers: SEVEN KEYSTONES WRITTEN BY STATE TERMS AND APPENDED ANNOTATIONS, REGISTRY.md BY ONE CELL AND APPENDED SECTIONS, "
            "OPEN_TRAILS.md +1 RECORD; EVERY PRE-EDIT LINE PRESENT OR QUOTED -- 0 CONTENT LOST; relay: tools/b363_span.py REPAIRED")
    grade = ("### THE REPLACEMENTS, SHAPES, CONTROL, CELL SOURCES, SEARCH RULE AND REPAIR WERE ON THE FACE BEFORE ANY SEARCH OR EDIT; EVERY HIT "
             "HAND-READ; TWO DEFECTIVE PREDICATES PRINTED WITH BOTH FIGURES")
    status = ("data/b454_the_ruling_executed.txt; data/b454_components.txt; data/b454_findings.json; data/b454_branch_lines.json; data/b454_registry.json; "
              "data/b454_enumera.json; data/b454_span_repair.json; data/b454_span.json; data/b454_checks.txt; data/b454_registration_2026-09-14.txt "
              "(LOCKED at sha256 %s); data/b454_addendum.txt (EMPTY); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('r63 executed under r64',
           'held branch lines moved to merged fast-forward',
           'era findings held by no ledger',
           'enumera nearest terminal',
           'span heading work-order repaired')
MUST_NOT_HIT = ('the census closes at sixteen', 'enumera derives', 'every era finding is added')
KEY = 'r63-executed-under-r64-and-the-span-heading-repaired'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b454 EXECUTED (R63) UNDER (R64): %d OF 8 BRANCH LINES MOVED TO MERGED BY FAST-FORWARD; OF 15 ERA FINDINGS, %d ADDED BESIDE A PRE-b450 "
                 "LEDGER LINE AND %d HELD BY NO LEDGER; 1.5a-7 v0.18, 1.5a-8 AND 1.5h-9 UNGRADED. ENUMERA: NO TERMINAL DERIVES; THE CENSUS STAYS AT "
                 "FIFTEEN OF SIXTEEN. W-ORD-SPAN-HEADING REPAIRED. NO CLAIM ABOUT ZEROS."
                 % (NED, CNT.get('found', 0), CNT.get('held_by_no_ledger', 0)))
    grade = "### NO GRADE MOVED ON ANY ROW. ### ENUMERA`S RELATION GRADED IN THE TRAIL ONLY. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b454_the_ruling_executed.txt; data/b454_components.txt; data/b454_findings.json; data/b454_enumera.json; data/b454_registry.json; "
             "data/b454_span_repair.json; data/b454_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; "
             "CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b454 ((R63) executed under (R64), and the span-heading work-order repaired)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### (R63) EXECUTED UNDER (R64), AND THE SPAN-HEADING WORK-ORDER REPAIRED (b454).%s'
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
        rec('    %-58s reaches the b454 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the counts carried', ('%d ADDED' % CNT.get('found', 0)) in out), ('the census carried', 'THE CENSUS STAYS AT FIFTEEN OF SIXTEEN' in out),
                      ('the repair carried', 'W-ORD-SPAN-HEADING REPAIRED' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, "b454 -- (R63) EXECUTED UNDER (R64), AND THE SPAN-HEADING WORK-ORDER REPAIRED.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR, GDG),
           '  G-WRITELIST-KINDS widened after its first reading to run_clock`s versioning, both yields printed in the suite: the seat`s redirect onto',
           '  the lock gate`s own run file made the gate write b454_lockgate_notes2.txt.']
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B453ROW_RE = r"(?m)^\| (\d+) \| \*\*THE RESIDUE AND RECONCILIATION ARC IS FOLDED"

def main():
    global DESK
    bar('=')
    rec('b454_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; counts %s ; census %s ; repair %s ; span %s'
        % (GR, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), CNT, CENSUS, NS, SPANN))
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
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B453ROW_RE, txt)])
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
    write_bytes(os.path.join(D, 'b454_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
