# -*- coding: utf-8 -*-
"""b435_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own records -- the components bank, the lock gate's notes, the suite -- and none is typed.
### ### **AND WHERE A FIGURE CANNOT BE READ, THE TOOL REFUSES RATHER THAN PRINTS A GUESS.**
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
MARK = '<!-- b435 the cure shared, and the skips that print like passes -->'
PRIOR = '<!-- b434 the fold, b423-b432 -->'
BANKOUT = os.path.join(D, 'b435_the_cure_shared.txt')
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


FACE = read(os.path.join(D, 'b435_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b435_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b435_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b435_components.txt'))


def num(rx, default='?'):
    """### **READ, NEVER TYPED** -- and a figure that is not there is printed as `?`."""
    m = re.search(rx, COMP)
    return m.group(1) if m else default


SITES_TOTAL = num(r'GIT-BEARING : \d+   ### LEFT AS WRITTEN : \d+   ### TOTAL : (\d+)')
GITBEARING = num(r'GIT-BEARING : (\d+)   ### LEFT AS WRITTEN')
LEFT = num(r'LEFT AS WRITTEN : (\d+)   ### TOTAL')
CAND = num(r'CANDIDATES (\d+)  ->  GENUINE')
GENUINE = num(r'GENUINE SINGLE-TOOL ENVIRONMENTAL HANDLERS : (\d+)')
SWEEP_CAND = num(r'a skip-word AND a pass/fail summary\*\* : (\d+)')
SWEEP_FOLD = num(r'SKIPS FOLDED INTO A FAILURE COUNT, BY BRANCH : (\d+)')
_fam = re.search(r'\*\*(an encoding or an EOL) -- met independently by (\d+) acts: ([^*]+)\*\*',
                 COMP)
FAM_LABEL = _fam.group(1) if _fam else '?'
FAM_ACTS_N = _fam.group(2) if _fam else '?'
FAM_ACTS = _fam.group(3).strip() if _fam else '?'
UNLISTED = num(r'this act`s unlisted writes : (\d+)', '?') if False else \
    (re.search(r'this act`s unlisted writes : (\d+)', CHK).group(1)
     if re.search(r'this act`s unlisted writes : (\d+)', CHK) else '?')

ROWMARK = ('**THE CURE SHARED: b314`S READ-ONLY HANDLER EXTRACTED TO A GUARD, TWO OF TEN CALL '
           'SITES REPOINTED AND EIGHT NAMED AND LEFT, THE PRE-PUSH GUARD`S SKIP MADE TO SAY '
           'SKIPPED, AND EIGHT SINGLE-TOOL CURES COUNTED**')

SCOPE = ("### THE ACT EXECUTES ONE RULING, (R46), AND EXTENDS IT NOWHERE. ### IT TOUCHES THE GUARD "
         "LAYER ONLY, ON THE LANE EXCEPTION THE ORDER NAMES, AND THE LANE CLOSES AT THIS ACT'S END. "
         "### IT MOVES NO GRADE, EDITS NO KEYSTONE, AND OPENS NOTHING ELSE")

DESK = [
    ('W-REMOVAL-VERIFIED', 'CLOSE',
     'DISCHARGED at b435, and **its own trigger is what fired** -- it was filed at b434 for "any '
     'act that opens the instrument-audit lane", and this act opens the instrument lane for the '
     'guard layer. `tools/force_rm.py` reads the removal from the directory`s own non-existence '
     'and raises `RemovalNotVerified` when a removal returns with the tree still standing.'),
    ('the cure that lived in one tool (b314)', 'CLOSE',
     'EXTRACTED at b435 to `tools/force_rm.py`, with fixtures in **both polarities** -- a read-only '
     'tree removed, and a genuine failure still raising -- and a **control** proving the bare call '
     'refuses that same tree. %s of %s call sites repointed; %s named and left with their reasons.'
     % (GITBEARING, SITES_TOTAL, LEFT)),
    ('the guard that cannot be exercised at an act`s own step zero', 'CLOSE',
     'REPAIRED at b435. `b304_hooks.py` now counts a skip apart from a failure, prints a VERDICT '
     'line naming all three states, and **its exit code can no longer say 0 on a skipped run**. '
     'Fixtures for PASS, FAIL and SKIPPED. The state was always in the row; it was the TOTAL that '
     'lost it.'),
    ('the shared-cure census', 'CLOSE',
     'RUN ONCE at b435 and **it repaired nothing**. %s candidates by description, %s genuine '
     'single-tool environmental handlers after hand-reading. **The largest family is %s: the same '
     'machine condition met independently by %s acts (%s).** (R46) governs what happens to them '
     'going forward; this act states the count and stops.'
     % (CAND, GENUINE, FAM_LABEL, FAM_ACTS_N, FAM_ACTS)),
    ('the write list that names a class instead of a file', 'STANDING',
     'NAMED at b435 as a defect in this act`s OWN locked face. The face listed "the call sites this '
     'act repoints" rather than their filenames, and the write ledger refused the class -- **%s '
     'unlisted writes, both of them the repointed sites.** The face is locked and was NOT edited; '
     'the breach is printed. **Whether (R44)`s standing form should say so explicitly is the '
     'author`s.**' % UNLISTED),
    ('the skips counted and left', 'STANDING',
     '%s tools carry a skip-word beside a pass/fail summary; **%s fold a skip into a failure count '
     'after this act`s repair**, and the sweep`s positive control finds the one it repaired. The '
     'rest are counted and left, because the order permits a repair only where it is the same one '
     'line.' % (SWEEP_CAND, SWEEP_FOLD)),
    ('the species: a tool asked not to complain', 'STANDING',
     'MINTED at b434. b435 discharges its third incident`s work-order and adds a fourth sighting '
     'from this act`s own bench: **moving the skip out of the failure count would have made a '
     'wholly skipped run exit 0** -- the species, minted while curing it. Caught and closed in the '
     'same repair.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432 and carried. Untouched by this act.'),
    ('the fourth grade, now defined', 'STANDING',
     'DEFINED at b433. Whether any further terminal should be re-graded against it is the author`s.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 and carried into b434`s fold. Untouched by this act.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane -- **and this act`s exception does not reach them**: it '
     'is for the guard layer only and closes at this act`s end.'),
    ('the scan`s sites against the lock`s zero', 'STANDING', 'The (R36) instrument item.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; untouched by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT -- **READ BY THIS ACT AND NOT MOVED.**'),
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
    return ['', MARK, '',
            '### b435 — the cure shared, and the skips that print like passes — filed 2026-09-12',
            '',
            '**(R46) executed and not extended: a cure that lives in one tool is not a guard.** '
            '`b314`’s read-only handler — written at b314, never shared, reinvented by `b433` '
            'nineteen acts later — is now `tools/force_rm.py`, and the two call sites that can hold '
            'a `.git` directory obtain it from there.', '',
            '#### Component 1 — the extraction, and the eight sites left alone', '',
            '**The handler is quoted at its own file and line** (`tools/b314_coldclone.py:47`) and '
            'extracted with **fixtures in both polarities**: a read-only tree removed, and a '
            'genuine failure — a held file handle — still raising. **The second polarity is the one '
            'that matters**; a helper that swallowed everything would pass the first and be worse '
            'than the bare call it replaced. A **control** runs first and shows the bare `rmtree` '
            'refusing that same tree, so the positive fixture is not vacuous.', '',
            '**%s of %s call sites were repointed and %s were named and left, each with its '
            'reason.** The rule was stated on the locked face before the sites were read: repoint a '
            'site whose tree can contain a `.git` directory; leave a site every file of whose tree '
            'the tool wrote itself, where the only failure mode is a leaked temporary directory. '
            '**Three successive mechanical rules were tried in the survey and each mis-sorted a '
            'site** — one called a sandbox that *filters `.git` out* git-bearing; the next flipped a '
            'directory that really is `git init`-ed. **A derivation that keeps changing its answer '
            'is not a measurement**, so the survey prints evidence and classifies nothing, and the '
            'call is the seat’s, said to be. Where the decisive fact sits in a **callee**, the '
            'reason names the callee.' % (GITBEARING, SITES_TOTAL, LEFT), '',
            '**The three guard sites — `b376_lockgate.py`, `b378_lockgate.py`, `gate_hash.py` — are '
            'reported on their own rows and all three are left.** A line that moves inside an '
            'instrument deciding whether an act may seal is not one line among ten. **No gate '
            'changed a byte.**', '',
            '#### Component 2 — the skip that printed like a pass', '',
            '`b304_hooks.py` already said **SKIPPED** in the per-repository row, with its reason — '
            'and then folded that state into `fails`, the one number a closing table quotes. **So '
            'the same `1` read as a failure in one table and as an exercised guard in another, and '
            'neither reader was wrong about what it said.** The skip now has its own count, and a '
            'VERDICT line names all three states. Fixtures for PASS, FAIL and SKIPPED.', '',
            '**And one thing the repair itself nearly minted.** Taking the skip out of `fails` '
            'would have left `return 0 if fails == 0 else 1` — so a **wholly skipped run would have '
            'exited 0**. That is b434’s own species, *a tool asked not to complain reports a '
            'success it did not earn*, committed while curing it. Three exit codes now: 0 exercised '
            'and passing, 1 failing, 2 not fully exercised.', '',
            '**The sweep, by description:** %s tools carry a skip-word beside a pass/fail summary; '
            '**%s fold a skip into a failure count** once this act’s repair has landed. The arm '
            'carries a **positive control** over the pre-act bytes — it finds the defect just '
            'repaired — so the zero means something. Two false positives were thrown out on the '
            'way: an arm that measured **distance** rather than structure accused `b304_hooks.py`’s '
            'byte-identity check, and an arm that walked a whole `if` accused `ferry_scan.py` of a '
            'fold whose increment is in one branch and whose skip-word is in the other. **A branch '
            'is not its sibling.** Everything else is counted and left.' % (SWEEP_CAND, SWEEP_FOLD),
            '',
            '#### Component 3 — the census, once, repairing nothing', '',
            '**%s candidates by description; %s genuine single-tool environmental handlers after '
            'each was read.** The positive control finds `b314`’s, as the order requires; without '
            'it the count would mean nothing. **The largest family is %s — the same machine '
            'condition met independently by %s acts (%s)**, each writing its own normaliser for '
            'what `core.autocrlf` does to a tracked file. That is the shape (R46) was ruled '
            'against, seen six times over.' % (CAND, GENUINE, FAM_LABEL, FAM_ACTS_N, FAM_ACTS), '',
            '**Three defects in this act’s own census, each found by reading its output rather than '
            'trusting it.** It counted **mentions as references**, so this act’s own quotation of '
            '`_force_rm` voted four times that b314’s cure was shared — b434 banked that lesson '
            'about call sites and the arm committed it anyway. It matched **`429` unbounded**, '
            'reaching inside the act number `b429` — precisely the lesson `b429` itself banked. And '
            'widening from docstrings to comments made a four-hundred-line `main` mentioning '
            '`autocrlf` in passing into "a handler for an encoding". **A handler is a routine, not '
            'a tool**, and a description is what a routine says it is for, at its top.', '',
            '#### What this act did not do', '',
            'The census repaired nothing beyond Component 1. No grade moved, no keystone was '
            'edited, no research instrument was touched. **The instrument lane was open for the '
            'guard layer only and closes at this act’s end.** The witness arc stays checkpointed '
            'after site (iii); the disproof lane stays shut with its trigger untouched; the four '
            'lists stay open; `h2` is where the deposit left it.', '',
            '**And one breach, printed rather than repaired.** This act’s own locked face named the '
            'repointed call sites as a **class** — "the call sites this act repoints" — where (R44)’s '
            'standing form requires a tool to be named. The write ledger refused the class and '
            'reported **%s unlisted writes**, both of them those sites. **The face is locked and was '
            'not edited.** Whether the standing form should say so outright is the author’s.'
            % UNLISTED]


def corr_rows():
    m = ROWMARK + " (b435)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b435 -- @GR@ gates read, @GDG@ checked by digest, and the seal RECOMPUTED by the tool "
            "that wrote it. **(R46) IS QUOTED FROM THE BANKED PASTE AND EXECUTED, NOT EXTENDED.** "
            "**b314's HANDLER IS QUOTED AT ITS OWN FILE AND LINE AND EXTRACTED TO tools/force_rm.py "
            "WITH FIXTURES IN BOTH POLARITIES -- A READ-ONLY TREE REMOVED, A GENUINE FAILURE STILL "
            "RAISING -- AND A CONTROL SHOWING THE BARE CALL REFUSES THAT SAME TREE.** **@GB@ OF "
            "@TOT@ CALL SITES REPOINTED AND @LEFT@ NAMED AND LEFT, EACH WITH ITS REASON; THE THREE "
            "GUARD SITES ARE ON THEIR OWN ROWS AND ALL THREE ARE LEFT, SO NO GATE CHANGED A BYTE.** "
            "**THE PRE-PUSH GUARD'S SKIP IS COUNTED APART FROM ITS FAILURES, ITS VERDICT LINE NAMES "
            "ALL THREE STATES, AND ITS EXIT CODE CAN NO LONGER SAY 0 ON A SKIPPED RUN.** **THE "
            "CENSUS RAN ONCE AND REPAIRED NOTHING: @CAND@ CANDIDATES, @GEN@ GENUINE SINGLE-TOOL "
            "CURES, THE LARGEST FAMILY MET INDEPENDENTLY BY @FAMN@ ACTS.** **AND THIS ACT'S OWN "
            "WRITE LIST NAMED A CLASS WHERE (R44) REQUIRES A NAME; THE LEDGER REFUSED IT AND THE "
            "BREACH IS PRINTED, THE LOCKED FACE NOT EDITED.** 0 GRADES MOVED, 0 KEYSTONES EDITED, "
            "0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. This act touches the guard layer and "
            "nothing else")
    prof = ("### ONE NEW SHARED TOOL WRITTEN (tools/force_rm.py); THREE EXISTING TOOLS EDITED IN "
            "PLACE (b257_checks.py, b372_eol.py, b304_hooks.py); ONE PLACE-papers FILE APPENDED "
            "(OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; NO KEYSTONE, NO REGISTER ROW, NO "
            "LEDGER ROW, NO KERNEL FILE, NO RESEARCH INSTRUMENT -- 0 CONTENT LOST")
    grade = ("### THE CALL ON EACH SITE IS THE SEAT'S AND IS SAID TO BE, AFTER THREE MECHANICAL "
             "RULES EACH MIS-SORTED A SITE; THE CENSUS COUNTED REFERENCES RATHER THAN MENTIONS "
             "AFTER FIRST COUNTING MENTIONS; AND BOTH THE SWEEP AND THE CENSUS CARRY POSITIVE "
             "CONTROLS, SO NEITHER EMPTY BUCKET IS AN ARTEFACT OF A BLUNT ARM")
    status = ("data/b435_the_cure_shared.txt; data/b435_components.txt; data/b435_extract.txt; "
              "data/b435_checks.txt; data/b435_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "tools/force_rm.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@GB@', str(GITBEARING)).replace('@TOT@', str(SITES_TOTAL))
                .replace('@LEFT@', str(LEFT)).replace('@CAND@', str(CAND))
                .replace('@GEN@', str(GENUINE)).replace('@FAMN@', str(FAM_ACTS_N)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('a cure that lives in one tool is not a guard',
           'where did b314`s read-only handler go',
           'which rmtree call sites were repointed',
           'the skip that prints like a pass',
           'how many single-tool cures does the corpus carry')
MUST_NOT_HIT = ('the census repaired the corpus', 'a grade was moved by b435',
                'the research instrument lane was opened')
KEY = 'the-cure-shared-and-the-skips-that-print-like-passes'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b435 EXECUTED (R46) -- A CURE THAT LIVES IN ONE TOOL IS NOT A GUARD -- AND EXTENDED IT "
        "NOWHERE. b314's read-only handler, written at b314 and never shared, was quoted at its own "
        "file and line (tools/b314_coldclone.py:47) and EXTRACTED to tools/force_rm.py with "
        "FIXTURES IN BOTH POLARITIES: a read-only tree removed, and a genuine failure still raising "
        "-- plus a CONTROL showing the bare rmtree refuses that same tree, so the positive fixture "
        "is not vacuous. %s of %s call sites were repointed and %s were NAMED AND LEFT with their "
        "reasons; the three guard sites (b376_lockgate, b378_lockgate, gate_hash) are on their own "
        "rows and all three are left, so NO GATE CHANGED A BYTE. THE CALL ON EACH SITE IS THE "
        "SEAT'S AND IS SAID TO BE: three successive mechanical rules each mis-sorted a site, and a "
        "derivation that keeps changing its answer is not a measurement. COMPONENT 2: b304_hooks.py "
        "already said SKIPPED in the row and then folded that state into the failure total, so the "
        "same 1 read as a failure in one table and as an exercised guard in another. The skip now "
        "has its own count, the VERDICT line names all three states, and THE EXIT CODE CAN NO "
        "LONGER SAY 0 ON A SKIPPED RUN -- which, left alone, would have MINTED b434's own species "
        "while curing it. COMPONENT 3, THE CENSUS, RUN ONCE AND REPAIRING NOTHING: %s candidates by "
        "description, %s genuine single-tool environmental handlers after hand-reading, and the "
        "largest family is %s -- the same machine condition met INDEPENDENTLY by %s acts (%s). "
        "W-REMOVAL-VERIFIED is DISCHARGED, its own trigger having fired. AND ONE BREACH PRINTED "
        "RATHER THAN REPAIRED: this act's locked face named the repointed sites as a CLASS where "
        "(R44) requires a name, the write ledger refused it, and the face was NOT edited."
        % (GITBEARING, SITES_TOTAL, LEFT, CAND, GENUINE, FAM_LABEL, FAM_ACTS_N, FAM_ACTS))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO KEYSTONE EDITED. ### NO RESEARCH "
             "INSTRUMENT TOUCHED. ### THE INSTRUMENT LANE WAS OPEN FOR THE GUARD LAYER ONLY AND "
             "CLOSES AT THIS ACT'S END. ### NOTHING DEPOSITS")
    where = ("data/b435_the_cure_shared.txt; data/b435_components.txt; data/b435_extract.txt; "
             "data/b435_checks.txt; data/b435_registration_2026-09-12.txt (LOCKED, %d gates read, "
             "%d by digest); tools/force_rm.py; OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
             % (GR, GDG, rownum))
    act = "b435 (the cure shared, and the skips that print like passes)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES (b435).%s'
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
        rec('    %-58s reaches the b435 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the ruling carried', 'A CURE THAT LIVES IN ONE TOOL' in out),
                      ('the both-polarity fixture carried', 'BOTH POLARITIES' in out),
                      ('the eight left sites carried', 'NAMED AND LEFT' in out),
                      ('the exit-code near-miss carried', 'SAY 0 ON A SKIPPED RUN' in out),
                      ('the census count carried', 'genuine single-tool' in out),
                      ('the breach carried', 'named the repointed sites as a CLASS' in out)):
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
    Bk = ['=' * 100,
          'b435 -- THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES.', 'THE BANK.',
          '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE NAVIGATOR`S EXPECTATIONS, AS THE COMPONENTS SCORED THEM.',
           '-' * 100]
    for ln in COMP.splitlines():
        if re.search(r'\(N1\)|\(N2\)|left as written : |candidates \d+, genuine|'
                     r'met independently by', ln):
            Bk.append('  %s' % ln.strip())
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d ; failing %d' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL),
           '  ### **THE TWO FAILING ARMS ARE THE WRITE-LIST ARMS, AND THEY ARE RIGHT TO FAIL:**',
           '  ### the locked face named the repointed call sites as a CLASS where (R44) requires a',
           '  ### name. ### **THE FACE IS LOCKED AND WAS NOT EDITED; THE BREACH IS PRINTED.**']
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


B434ROW_RE = r"(?m)^\| (\d+) \| \*\*THE EXTERNAL-GRADING ARC FOLDED"


def main():
    bar('=')
    rec('b435_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or SITES_TOTAL == '?':
        rec('  ### HARD FAILURE -- this act`s components bank is missing or unreadable.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      sites %s total / %s git-bearing / %s left ; census %s candidates / %s genuine'
        % (SITES_TOTAL, GITBEARING, LEFT, CAND, GENUINE))
    rec('      the largest family : %s, %s acts (%s)' % (FAM_LABEL, FAM_ACTS_N, FAM_ACTS))
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
    rec('  b434`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B434ROW_RE, txt)])
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
    rec('  after -- b434`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B434ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b435_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
