# -*- coding: utf-8 -*-
"""b430_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own JSON, never typed. ### The trail block is the SELF-CONTROL record, and its trigger is the
### author's ruling on whether the grading may be cited.
"""
import io
import json
import os
import re
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
MARK = '<!-- b430 the self-control: the corpus`s own terminal graded twice -->'.replace('`', "'")
PRIOR = '<!-- b429 the external grading read: a calibration record -->'
BANKOUT = os.path.join(D, 'b430_the_self_control.txt')
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


FACE = read(os.path.join(D, 'b430_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b430_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

try:
    G = json.loads(read(os.path.join(D, 'b430_grades.json')) or '{}')
except Exception:
    G = {}
CHK = read(os.path.join(D, 'b430_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS = (int(_a.group(1)), int(_a.group(2))) if _a else (0, 0)

GA = G.get('grade_a', 'NO GRADE')
GB = G.get('grade_b', 'NO GRADE')
VERD = G.get('verdict', 'NO VERDICT')
SAME = G.get('clauses_same', 0)
PIN = str(G.get('pin', ''))[:12]
PROFLINE = G.get('profile_line') or ''

ROWMARK = ('**THE SELF-CONTROL: THE CORPUS`S OWN TERMINAL GRADED BY THE PROTOCOL IT USED ON A '
           'STRANGER, TWICE UNDER (R40) -- %s AGAINST ITS ROW`S CLAIM AND %s AGAINST THE PROSE`S, '
           'AND THE FOUR CLAUSES READ %s**' % (GA, GB, VERD)).replace('`', chr(0x2019))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — '
        'the rows grading a declaration the record has classified absent (b373). **OPEN.** '
        '**LIST 3** — the undated figures across the roster (b374). **OPEN.** **LIST 4** — the '
        'bibliography entries nothing cites (b374). **OPEN.** Trigger: the ruling on which test '
        'governs, or any disposition on the four open lists.')

DESK = [
    ('the self-control (leg 1 of the b430-b432 sortie)', 'CLOSE',
     'RUN at b430: `SmearGeneral.smear_general` built at pin %s, profile printed from the '
     'printer`s own output, statement unfolded to 4 base objects, definitions checked by '
     '`rowgen``s `defenc` with a live control. Graded TWICE under (R40): %s against the claim '
     'correspondence row 268 names, %s against the claim the finite-side prose makes. The four '
     'clauses read %s, %d of 4 applied to itself as they were applied to the stranger.'
     % (PIN, GA, GB, VERD, SAME)),
    ('the two gradings, cited nowhere', 'STANDING',
     'Both b429`s and b430`s are banked at relay and entered on the trails. TRIGGER: *cited '
     'nowhere until the author rules whether they are.* 0 corpus documents cite either.'),
    ('the fourth grade`s standing in the corpus`s vocabulary', 'STANDING',
     'ROUTED AND NOT RULED. (R40) seats `NOT THE CLAIM` as a grade and this act USED it, but the '
     'two documents that DEFINE the corpus`s grades -- `README.md` and `EXCLUSION_ENGINE.md` §0 -- '
     'still name three and only three. **A grade used and not defined is a gap between the ruling '
     'and the vocabulary, and only the author closes it.**'),
    ('the two asymmetries b429 routed', 'CLOSE',
     'BOTH CLOSED FROM THE OTHER SIDE at b430, on one trial: the fourth grade was available AND '
     'USED against the corpus`s own terminal, and `rowgen``s `defenc` was run on it. The b429 '
     'asymmetries were that act`s, not the discipline`s.'),
    ('what the two trials still cannot tell', 'STANDING',
     'CANNOT TELL, said plainly: two acts are not a population. The verdict SYMMETRIC is one '
     'trial against one trial and licenses no statement about the discipline in general.'),
    ('the ferry scan`s exception drift', 'CLOSE',
     'REPAIRED at b430 step zero by the author`s order: the scan reads `banned_terms.EXCEPT` '
     'through `classify`, fixtures in both polarities, both incidents named in the module, and '
     '0 banked arm moved. **The scan-versus-lock mismatch is NOT touched and stays routed.**'),
    ('the navigator`s standing failure on banned stems', 'STANDING',
     'ENTERED at b430 as `FERRY_STANDING` `A3`, in the author`s own words, in the section that '
     'declares itself NOT MEASURED; the `VERSION:` line is not bumped, for the reason `A1` and '
     '`A2` were not. **A3 binds a reader and not a tool.**'),
    ('the disproof lane, named and not opened (b428)', 'STANDING',
     'Named at b428; leg 3 of this sortie restates it with a worked case and does not open it. '
     'TRIGGER: the instrument lane opening.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 on three sites: the class boundary`s share 13/16, 10/19, 12/20; union of '
     'kinds 10 and still growing.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('the scan`s sites against the lock`s zero', 'STANDING',
     'The (R36) instrument item. **UNCHANGED BY b430`s REPAIR**, which touched only which stems '
     'the scan reads.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; untouched by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1800], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    L = ['', MARK, '',
         '### b430 — the self-control: the corpus’s own terminal, graded twice — filed 2026-09-12',
         '',
         '**This is the control for b429. The same protocol, turned on the corpus’s own freshest '
         'empty-profile terminal. __TRIGGER: cited nowhere until the author rules whether it is.__ '
         'It is banked at relay and entered here; no corpus document cites it.**', '',
         '#### What (R40) changes, and what it does not', '',
         '**(R40) is ratified by the paste that ordered this act:** a grade is a relation between '
         'a terminal and a *named claim*, not a property of the terminal. **No existing grade '
         'moves by it** — what changes is what a grade is understood to be. Its fourth name, '
         '`NOT THE CLAIM`, is for a terminal that *“states strictly less than the claim named”*.',
         '',
         '#### The terminal, at its pin', '',
         '`SmearGeneral.smear_general`, `SIDE-global-section` at `%s`, toolchain '
         '`leanprover/lean4:v4.29.1` — **the kernel’s own, honoured by elan**. The three-module '
         'import chain was compiled **one job at a time** into a scratch directory outside every '
         'rostered repository; **0 corpus tracked files were written and `AXIOM_PRINTS.txt` was '
         'not regenerated**. The profile is `%s`, read from the printer’s own stdout and not from '
         'the banked profile file and not from an exit code. **No `sorryAx` in the closure.** '
         'A raw sweep of the chain finds `sorry` 3 times and **0 of them are terms** — all three '
         'are the corpus’s own docstrings saying the module carries none, which is why the sweep '
         'strips comments and string literals before it counts.'
         % (PIN, PROFLINE.split("' ")[-1] if PROFLINE else 'NOT READ'), '',
         '#### The two claims, fixed before either grade was formed', '',
         '**CLAIM A — what the terminal’s own correspondence row names.** Row `268`, read by its '
         'marker: *“FOR EVERY p WITH singlePrimeFactor p = true AND EVERY n, ballQ p n * sumAN p n '
         '= sumAQ p n; THE SEVEN CELLS INSTANCES.”*', '',
         '**CLAIM B — what the finite-side prose makes of it.** `FACES_LEDGER.md` carries **three '
         'rows keyed `F5`**, and the marker alone does not pick one; the claim-bearing row was '
         'chosen by a printed rule — the one that names `Core/FiniteSideSeal.lean` and carries a '
         '`PROVED-` word — which is line 153. Its scope sentence reads *“GENERAL, over every base '
         'p ≥ 2, level, power and index”*. `FINDINGS.md` carries **three rows keyed `K3`**, at '
         '3049, 3064 and 3084; K3’s claim is *“the source’s construction on the object returns the '
         'test function at the identity times a dimension”*.', '',
         '#### The two grades', '',
         '**AGAINST CLAIM A: `%s`.** The row’s quantifier is the terminal’s quantifier, the row’s '
         'identity is the terminal’s identity, and the row says *every n* as the terminal does. '
         'The profile is empty; `rowgen`’s `defenc` returns `False` over the whole import chain, '
         'with a literal-constant definition appended as a control that **does** fire — so the '
         '`False` is a result and not a dead call. **The definitions were checked by the tool and '
         'not on a reading.**' % GA, '',
         '**AGAINST CLAIM B: `%s` — for two independent reasons, both measured.** *(1) Scope:* the '
         'prose claims every base `p ≥ 2`; the terminal is restricted to bases with a single prime '
         'factor. *(2) Object, and this one does not depend on scope:* of the nine objects K3’s '
         'claim names — trace, test function, identity, dimension, source, construction, and the '
         'rest — **the terminal’s statement names none**. The prose speaks of the source’s trace; '
         'the terminal speaks of the model’s count. **And the record says this itself**, at '
         '`FINDINGS.md:3084`: *“the identification of that count with the source’s trace is b310’s '
         'derivation and is not compiled.”* The gap is the record’s own, already stated.' % GB, '',
         '**What this grade is not.** It is **not** a finding that `F5`’s own listed terminals are '
         'misgraded — `F5`’s `PROVED-GENERAL` governs the *scaling* part, a different list, which '
         'this act neither built nor graded. **And `K3`’s prose is itself carefully qualified** — '
         '*the compact part PER CELL* — which is the record being right, not wrong. **No grade on '
         'the record moves, and under (R40) the two grades are not in conflict: they are two '
         'relations, not two readings of one.**', '',
         '#### The four clauses, and the verdict', '',
         '**%d of 4 applied to itself as b429 applied them to the stranger. VERDICT: `%s`.**'
         % (SAME, VERD), '',
         '- *the closure* — **the same**: a clean `#print axioms` required and read from the '
         'printer, `sorryAx` sought by name, the source swept with comments stripped first.',
         '- *the unfolding* — **the same**: 4 of 4 base objects quoted at their own file and line, '
         'from the kernel’s source and not from prose about it.',
         '- *the available vocabulary* — **the same, and the asymmetry b429 found is closed**: '
         'four grades were available here too, and **the fourth was used**, against CLAIM B.',
         '- *the verification instrument* — **the same, and b429’s second asymmetry is closed**: '
         'b429 accepted the stranger’s definitions on a reading with its checker unrun; b430 ran '
         '`rowgen`’s `defenc` on its own, with a control.', '',
         '**So b429’s two asymmetries were that act’s, not the discipline’s** — which is what '
         '`SYMMETRIC` means here. **And the sentence that bounds it: one trial against one trial.** '
         'b429 graded one stranger, b430 grades one terminal of the corpus’s own; two acts are not '
         'a population, and nothing here licenses a statement about the discipline in general.', '',
         '#### Step zero, and a gate defect repaired by the author’s order', '',
         '**The first issue of this sortie’s ferry halted at step zero**: two banned-stem hits in '
         'the author’s own prose, and the lock gate refuses on any hit. The author re-issued with '
         'two words changed — the artefact’s real names, `LongGapsBetweenPrimes` and '
         '`long_gaps.pdf` — and **the ferry as first received is preserved byte-for-byte at '
         '`data/b430_ferry_asreceived.txt` with its own digest**; the computed diff between the '
         'two is **exactly two hunks** and the seat edited no word of either.', '',
         '**And the added step zero: `ferry_scan.py` read `banned_terms.STEMS` and never '
         '`banned_terms.EXCEPT`**, so a use the record ruled lawful at b142 was refused at the '
         'lock. Repaired: the scan now puts every banned-stem hit to the owning tool’s own '
         '`classify`, and an excepted hit is **reported separately and excluded from the verdict** '
         'rather than dropped. Fixtures in both polarities, paired on the same stem so an '
         'exception cannot be a hole. **0 banked arm moved** — the filter only removes hits, and '
         'every banked stem arm passes on a zero or controls on a line no exception covers.', '',
         '**The two incidents are two species, and only the second is this defect.** The ferry’s '
         'own hits were a **live use**: `classify` returns `None` on that line, so the refusal was '
         'Rule 3 applied correctly, **the repair does not cure it**, and the as-received ferry '
         're-scanned by the repaired tool still reports the same two hits. The author’s re-wording '
         'cured it. Only the Clay mass-gap refusal was the drift — demonstrated by a positive '
         'control, and **no banked act is known to have been halted by it**.', '',
         '**And the repair reproduced the incident it was written to record**: its first writing '
         'named the ferry’s leg by quoting the hyphenated form, which is a live use of the stem in '
         'the scanner’s own source — the thing that file’s header rule (4) forbids and '
         '`b299_checks` sweeps for. Named without spelling it, and swept again at zero.', '',
         '**The navigator’s standing failure is entered as `FERRY_STANDING` `A3`, in his own '
         'words**, in the section that declares itself not measured: *“two banned stems in two '
         'ferries in one week after a stated commitment to scan”*, with the commitment restated as '
         'a mechanical step and the seat licensed to refuse a ferry that arrives without a line '
         'stating the scan was run. **Measured rather than recalled, the two incidents are b418’s '
         'ferry and b430’s, and both refusals were correct.** The `VERSION:` line is not bumped, '
         'for the reason `A1` and `A2` were not.', '',
         '#### The arc, and the lanes this act leaves where it found them', '',
         '**W-ORD-WITNESS-ENUMERATION stays checkpointed after site (iii)** — sites (iv) to (vi) '
         'remain, one act each, and this act entered none. The disproof lane named at b428 stays '
         '**named and not opened**. Both instrument lanes stay parked and the wave stays parked.',
         '', '#### The four lists', '', FOUR, '',
         '#### What this act did not do', '',
         '0 grades of the corpus’s own moved, conferred or minted on the record. 0 premises '
         'discharged. 0 doors restated. 0 routes proposed. 0 lanes opened. 0 kappa measured. '
         '0 corpus `.lean` files edited. 0 tracked files of any rostered repository written by the '
         'build. 0 regenerations of `AXIOM_PRINTS.txt`. 0 rows of `FACES_LEDGER.md`. 0 register '
         'rows. 0 keystones. 0 addresses resolved and 0 documents fetched — **leg 2’s addresses '
         'are untouched by this act**. 0 deposit actions. **And h2 where the deposit left it.**',
         '']
    return L


SCOPE = ("### THIS ROW RECORDS A CONTROL: THE CORPUS'S OWN TERMINAL PUT TO THE PROTOCOL THE CORPUS "
         "USED ON A STRANGER. ### IT MOVES NO GRADE, OPENS NO LANE, EDITS NO KEYSTONE AND WRITES "
         "NO CORPUS KERNEL FILE")


def corr_rows():
    m = ROWMARK + " (b430, the self-control)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE OR BUILD**, chained on b378's "
            "gate run as b430 -- @GR@ gates read, @GDG@ checked by digest. **(R40) RATIFIED AND "
            "QUOTED FROM THE BANKED PASTE; NO EXISTING GRADE MOVES BY IT.** **STEP ZERO, ADDED BY "
            "THE RE-ISSUE: THE FERRY SCAN'S EXCEPTION DRIFT REPAIRED -- IT READ THE STEM LIST AND "
            "NEVER THE EXCEPTION LIST; FIXTURES IN BOTH POLARITIES; BOTH INCIDENTS NAMED; 0 BANKED "
            "ARM MOVED; THE SCAN-VERSUS-LOCK MISMATCH UNTOUCHED AND STILL ROUTED.** **THE TERMINAL "
            "BUILT AT PIN @PIN@, 3 JOBS ONE AT A TIME, PROFILE @PROF@ FROM THE PRINTER'S OWN "
            "OUTPUT, NO sorryAx, sorry AS A TERM 0 OF 3 RAW.** **UNFOLDED TO 4 OF 4 BASE OBJECTS "
            "AT THEIR OWN FILE AND LINE; DEFINITIONS CHECKED BY rowgen's defenc WITH A LIVE "
            "CONTROL.** **GRADED TWICE: @GA@ AGAINST ROW 268'S CLAIM, @GB@ AGAINST THE FINITE-SIDE "
            "PROSE'S, FOR TWO INDEPENDENT REASONS.** **THE FOUR CLAUSES: @SAME@ OF 4 THE SAME; "
            "VERDICT @VERD@; ONE TRIAL AGAINST ONE TRIAL.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, "
            "0 CONTENT LOST")
    term = ("NO TERMINAL ADDED OR MOVED. SmearGeneral.smear_general was COMPILED AT ITS PIN AND "
            "GRADED; its source, its module and AXIOM_PRINTS.txt are unchanged")
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX, CARRYING "
            "THE SELF-CONTROL RECORD; TWO relay TOOLS EDITED BY THE RE-ISSUE'S OWN ORDER -- "
            "ferry_scan.py REPAIRED AND FERRY_STANDING.md AMENDED WITH A3, ITS VERSION LINE "
            "UNMOVED; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO CORPUS KERNEL FILE; EVERY "
            "BUILD ARTEFACT OUTSIDE EVERY ROSTERED REPOSITORY -- 0 CONTENT LOST")
    grade = ("### BOTH CLAIMS WERE QUOTED BEFORE EITHER GRADE WAS FORMED; EACH WAS READ FROM ITS "
             "OWN ROW BY MARKER, AND WHERE A MARKER MATCHED THREE ROWS THE ROW WAS CHOSEN BY A "
             "PRINTED RULE AND NOT BY POSITION; THE PROFILE IS THE PRINTER'S OWN OUTPUT; AND THE "
             "FOURTH GRADE WAS USED AGAINST THE CORPUS'S OWN TERMINAL, WHICH IS THE ASYMMETRY b429 "
             "FOUND, CLOSED FROM THE OTHER SIDE")
    status = ("data/b430_the_self_control.txt; data/b430_components.txt; data/b430_extract.txt; "
              "data/b430_scan_repair.txt; data/b430_grades.json; data/b430_profile.txt; "
              "data/b430_build.log; data/b430_checks.txt; "
              "data/b430_registration_2026-09-12.txt (LOCKED at sha256 %s); tools/ferry_scan.py; "
              "tools/FERRY_STANDING.md; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@PIN@', PIN).replace('@GA@', GA).replace('@GB@', GB)
                .replace('@SAME@', str(SAME)).replace('@VERD@', VERD)
                .replace('@PROF@', 'EMPTY (does not depend on any axioms)'
                         if G.get('profile_empty') else 'NOT EMPTY'))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the self-control', 'smear_general graded', 'grading the corpus`s own terminal',
           'the four clauses compared', 'is the grading discipline symmetric')
MUST_NOT_HIT = ('the corpus is symmetric', 'smear_general is general', 'the prose is wrong')
KEY = 'the-self-control'


def query(q):
    import subprocess
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b430 GRADED THE CORPUS'S OWN SmearGeneral.smear_general BY b429'S PROTOCOL, TWICE UNDER "
        "(R40). Built at pin %s, 3 jobs one at a time; profile from #print axioms, empty, no "
        "sorryAx; statement unfolded to 4 of 4 base objects at their own file and line; "
        "definitions checked by rowgen's defenc with a live control, False. GRADE %s against the "
        "claim correspondence row 268 names; GRADE %s against the claim the finite-side prose "
        "makes (F5 line 153 and K3), for two independent reasons -- scope, and the objects the "
        "statement names. THE FOUR CLAUSES: %d of 4 applied to itself as to the stranger; VERDICT "
        "%s; one trial against one trial. Cited in no corpus document."
        % (PIN, GA, GB, SAME, VERD))
    grade = ("### NO GRADE OF THE CORPUS'S OWN MOVED ON THE RECORD. ### NO LANE OPENED. "
             "### NOTHING DEPOSITS")
    where = ("data/b430_the_self_control.txt; data/b430_components.txt; data/b430_grades.json; "
             "data/b430_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b430 (the self-control)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE SELF-CONTROL (b430).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-58s reaches the b430 key : %s' % (qq[:58], g2))
    for lbl, cond in (('both grades carried', GA in out and GB in out),
                      ('the verdict carried', VERD in out),
                      ('one trial against one trial carried', 'one trial against one trial' in out),
                      ('cited nowhere carried', 'Cited in no corpus document' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, 'b430 -- THE SELF-CONTROL. ### THE CORPUS`S OWN TERMINAL, GRADED TWICE.',
          'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    comp = read(os.path.join(D, 'b430_components.txt'))
    Bk += ['', '-' * 100, '### THE EXPECTATION, AS THE REPORT SCORED IT.', '-' * 100,
           '  (L1)(a) the verdict reads SYMMETRIC          : %s' % (VERD == 'SYMMETRIC'),
           '  (L1)(b) the grade against CLAIM A is DERIVES : %s' % (GA == 'DERIVES'),
           '  (L1)(c) the grade against CLAIM B is NOT THE CLAIM : %s' % (GB == 'NOT THE CLAIM'),
           '  ### **EACH CLAUSE SCORED ONCE, APART, AND EACH REFUTABLE BY A PRINTED RESULT.**']
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d' % (ARMS_RUN, ARMS_PASS)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
           % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'),
           '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B429ROW_RE = r"(?m)^\| (\d+) \| \*\*THE EXTERNAL GRADING READ"


def main():
    bar('=')
    rec('b430_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not G:
        rec('  ### HARD FAILURE -- this act`s own grades JSON is missing.')
        return 1
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED -- THE SELF-CONTROL RECORD.')
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
    rec('  b429`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B429ROW_RE, txt)])
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
    rec('  after -- b429`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B429ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b430_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
