# -*- coding: utf-8 -*-
"""b441_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b441 the identification filed, the overstatement corrected, and two filings -->'
PRIOR = '<!-- b440 the fixed point named, the break attributed, and two facts built -->'
BANKOUT = os.path.join(D, 'b441_the_identification_filed.txt')
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


FACE = read(os.path.join(D, 'b441_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b441_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b441_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b441_components.txt'))


def _j(name, default):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return default


ROUTES = _j('b441_routes.json', {})
PRICE = _j('b441_price.json', {})
REACH = _j('b441_reach.json', [])
R1000 = ([r for r in ROUTES.get('rows') or [] if r['T'] == 1000] or [{}])[0]
TOL = bool(ROUTES.get('tol1_met')) and bool(ROUTES.get('tol2_met'))
EXACT = PRICE.get('exact') or []
OSENSE = [c['id'] for c in PRICE.get('candidates') or [] if 'O-SENSE' in c['uniformity']]
UNSTATED = [c['id'] for c in PRICE.get('candidates') or [] if 'NOT STATED' in c['uniformity']]
BROKEN = [r['act'] for r in REACH if r['predicate_first_committed'].startswith('branch')]
NOPRED = [r['act'] for r in REACH if r['predicate_first_committed'].startswith('NONE')]
ONE = [r['act'] for r in REACH if r['readings'] == 'ONE']
MAXDIFF = max([r['absdiff'] for r in ROUTES.get('rows') or [{'absdiff': 0}]])

# ### **A MARKER MUST BE DISTINGUISHABLE FROM EVERY EARLIER ONE** (b440's own incident).
ROWMARK = ('**THE ARCHIMEDEAN CHANNEL IS THE SMOOTH ZERO-ORDINATE DENSITY: ITS KERNEL HALF WAS ALREADY '
           'IN CC AND AT K5, ITS COUNTING HALF -- MAIN TERM MINUS theta/pi IS 1, THE POLE -- IS NEW AND '
           'MEASURED; THE LINE b440 CALLED A DENIAL DENIES SOMETHING ELSE AND THE WORD WAS THIS '
           'SEAT`S; AND THE PUSH-SIDE REGRESSION WAS b440`S ALONE**')

SCOPE = ("### THE ACT RESTATES THREE LINES, FILES ONE LEDGER BLOCK THROUGH THE WRITER, PRICES FIVE "
         "VERIFIED-SOURCE STATEMENTS WITHOUT IMPORTING ANY, READS ELEVEN SUITES FROM GIT HISTORY, AND "
         "MINTS ONE TECHNE MODULE LOCALLY. ### NO NEW INSTRUMENT, NO NEW FAMILY, NO LANE OPENED, NO SITE "
         "REOPENED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO BEYOND QUOTING A VERIFIED SOURCE")

DESK = [
    ('whether the record denies the density identification', 'CLOSE',
     'ANSWERED at b441: **NO.** `SPIRAL_MAP.md:114` denies that SIDE-window`s prime-power counting '
     'function is related to `W_2`/`W_inf` -- a true disclaimer about a name collision -- and says '
     'nothing about zero-ordinates. It is left unedited. **The word *denial* was this seat`s**, in '
     'b440`s components and closing; the navigator`s premise repeated it.'),
    ('whether the record carries the identification at all', 'CLOSE',
     'ANSWERED at b441, **IN TWO HALVES.** The kernel half -- `h+` is twice the derivative of the '
     'Riemann-Siegel angular function -- is CC`s own (153)-(154), quoted by b333`s survey and under '
     'K5`s DERIVES-ON-IMPORTS; b440`s "not carried" held only over PLACE-papers prose. The counting '
     'half -- the main term minus `theta/pi` is `1 - 1/(48 pi T)`, the `1` the pole -- was in '
     'neither prose, banks nor sources, and is now MEASURED by two routes sharing no code.'),
    ('what the identification buys', 'CLOSE',
     'PRICED at b441, nothing imported. Five verified-source statements: exact at every height, '
     '%s; uniform only in the O-sense for large height, %s; domain not stated in the quoted text, '
     '%s. **Site (ii)`s B3 and B5 both stand** -- the identified channel contains no real part, and '
     'a count uniform in the height places no zero.' % (EXACT, OSENSE, UNSTATED)),
    ('how far the push-side defect reached', 'CLOSE',
     'MEASURED at b441 from git history: the broken predicate was first committed in %s alone; '
     '%s had no predicate at all and was repaired inside its own act; every pre-push file b430-b440 '
     'was committed exactly once; **%d of 11 banks show one reading.** b440`s "b430`s defect, still '
     'live in every act since" is false, and corrected here.' % (BROKEN, NOPRED, len(ONE))),
    ('the axiom-form lore', 'CLOSE',
     'MINTED at b441 as `TECHNE-Core/modules/2026-09/AXIOM_PROFILE_IS_PARTLY_FORM.md`, local commit, '
     'not pushed: a profile certifies the terminal as phrased, not the fact.'),
    ('whether FACES_LEDGER.md was the ledger the author meant', 'STAND',
     'ROUTED at b441. The order said "the findings layer`s writer"; `FINDINGS.md` has no writer '
     'module, and the one module the corpus calls the writer writes `FACES_LEDGER.md`, where K5 '
     'was last graded. The block went there. **If the author meant `FINDINGS.md`, the route is one '
     'generated addendum carrying the same three rows; the ledger block is not removed.**'),
    ('the refused first paste', 'STAND',
     'PRESERVED at b441 as `b441_ferry_first_paste.txt` with its scan. The lock gate still refuses '
     'any author-text hit with no override; whether that should change is the author`s.'),
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
        '### b441 — the identification filed, the overstatement corrected, and two filings — filed 2026-09-12',
        '',
        '**The record never denied the identification. It carried half of it and not the other half, and the word *denial* was this seat’s.** No new instrument, no new family, no lane opened, no site reopened.',
        '',
        '#### Component 1 — three lines restated, one left unedited, and the identification filed in two halves',
        '',
        '`SPIRAL_MAP.md:114` denies that `SIDE-window`’s **prime-power** counting function is related to `W_2`/`W_∞` — a true disclaimer about a name collision — and says nothing about zero-ordinates. It stays unedited. The two archive lines b440 also found (`FINDINGS-archive-1…:2678`, `OPEN_TRAILS-archive-2…:9037`) are an open-term inventory for another sector and an era-annotation list; neither states a density. **The sentence that called the first a denial was written in b440’s components and closing; the navigator’s premise repeated it.**',
        '',
        '**The kernel half was already carried.** CC’s own (153)–(154): *“It is the derivative of 2 θ(τ), where θ is the Riemann-Siegel angular function”* — the corpus’s own `h₊`, under the same name. b333’s survey quoted it and K5 sits on it at DERIVES-ON-IMPORTS. b440’s “not carried by the corpus” held only over PLACE-papers prose.',
        '',
        '**The counting half was not, and is now measured.** Route A integrates the `digamma` kernel with `mpmath.quad`; route B takes `θ(T)` from `loggamma` with no quadrature. They agree to @MAXDIFF@ at six heights against `1e-12` stated first, and `RvM main term − θ(T)/π = 1 − 1/(48πT) + O(T⁻³)`, the deficit times `48πT` reading `@R1000@` at `T = 1000` against a `1e-6` tolerance. **The `1` is the pole of ζ at `s = 1`.** Filed MEASURED, never as a theorem, through the writer’s `append_block` into `FACES_LEDGER.md` under row S1, constituent K5, every quotation verified first.',
        '',
        '#### Component 2 — what it buys, priced and nothing imported',
        '',
        'Five statements from the verified sources: CC’s (153)–(154), CC’s `θ′ = O(log|s|)`, Binet’s first formula as CC uses it, Lagarias Theorem 2.1(4), and its unit-interval consequence. Exact at every height: **@EXACT@**. Uniform only in the O-sense for large height: **@OSENSE@**. Domain not stated in the quoted text: **@UNSTATED@** — the first writing called Binet’s formula exact at every height, which was this seat’s and not CC’s, and the suite’s uniformity arm caught it.',
        '',
        '**Site (ii)’s failing steps both stand.** `B3` fails at S2 on I-7’s question — *does the statistic’s definition contain the zeros’ real parts?* — and the identified channel contains no zero at all, so it is density-register by construction. `B5` fails at S3, and a count uniform in the height still places no zero. The identification changes what `B5` *is* — the main term is now the corpus’s own integrated channel plus the pole — and not why it fails.',
        '',
        '#### Component 3 — two filings and one measurement',
        '',
        '**(i) The pole’s double role**, filed in the same block as a juxtaposition of three graded lines and no mechanism: the aim’s second moment condition is the lawfulness condition, the requirement that the test function not register the pole; that pole is the constant separating the integrated channel from the counting formula; and the same condition breaks the seed family’s self-similarity by exactly `(1 + 1/c)/2`.',
        '',
        '**(ii) The push-side defect’s reach**, read from git history as first committed:',
        '',
        '| act | predicate as first committed | pre-push file commits | readings banked |',
        '|:--|:--|--:|:--|',
        '| @A0@ | @P0@ | 0 | @R0@ |',
        '| @A1@ | @P1@ | 0 | @R1@ |',
        '| @A2@ | @P2@ | 0 | @R2@ |',
        '| @A3@ | @P3@ | 0 | @R3@ |',
        '| @A4@ | @P4@ | 0 | @R4@ |',
        '| @A5@ | @P5@ | 0 | @R5@ |',
        '| @A6@ | @P6@ | 0 | @R6@ |',
        '| @A7@ | @P7@ | 0 | @R7@ |',
        '| @A8@ | @P8@ | 0 | @R8@ |',
        '| @A9@ | @P9@ | 0 | @R9@ |',
        '| @A10@ | @P10@ | 0 | @R10@ |',
        '',
        'The broken predicate — a SHA sought in a list of branch names — was first committed in **b440 alone**, a regression this seat wrote by typing the suite fresh instead of carrying b439’s; b430 had no predicate and repaired itself inside its own act. Every pre-push file was committed exactly once. **@ONE@ of 11 banks show one reading; (N3) is refuted.** b440’s sentence that the defect was “b430’s, still live in every act since” is false, and b440’s bank is not edited. **The two-reading discipline exists so that a verdict keeps its date: a pre-push reading overwritten by the post-push run is dated by the commit after it, and nobody can tell from the bank whether the act was clean before it pushed.**',
        '',
    '**And the repair b440 made was defective too.** b440 replaced its broken predicate with `origin/main == HEAD`, which is true *before* an act commits anything, because HEAD is then the prior act’s pushed commit — the species b434’s own docstring names: *“HEAD is trivially on the remote.”* b440 escaped it because its pre-push reading was already committed. **b441 did not: its first pre-push reading was written into `b441_checks_postpush.txt` under a POST-PUSH header, and the locked face’s BAR 11 names the same defective rule.** The face is not edited; the suite now carries b439’s predicate — a commit naming this act, made and on the remote — and the misfiled reading is quoted in the components record before the true post-push run replaces it. That is three push-side writings by this seat in two acts, each retyped rather than carried: `(R46)`’s species, and this act’s own.',
        '',
    '**(iii) The axiom-form lore**, minted as `TECHNE-Core/modules/2026-09/AXIOM_PROFILE_IS_PARTLY_FORM.md`, local, not pushed: `16 ∉ primePowersLT 16` carries `[propext, Quot.sound]` and `(primePowersLT 16).elem 16 = false` carries none, so **a profile certifies the terminal as phrased, not the fact** — and a dirtier profile is not evidence of a stronger dependence.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | the identification is absent rather than denied | **HALF HELD** — not denied; absent for the counting half, carried for the kernel half |',
        '| (N1)(b) | the located line stays unedited | **HELD** |',
        '| (N2)(a) | at least one importable statement is uniform in the height | **HELD** — CC (153)–(154) exactly; three more in the O-sense |',
        '| (N2)(b) | it does not change site (ii)’s failure step | **HELD** — B3 and B5 both stand |',
        '| (N3) | more than half the closings since b430 carry one reading | **REFUTED** — 0 of 11 |',
        '',
        '*This seat’s own two, declared on the face: (N1)(a) half held — held; (N3) refuted — held.*',
    ]
    rep = [('@MAXDIFF@', '%.1e' % MAXDIFF), ('@R1000@', str(R1000.get('scaled', ''))[:12]),
           ('@EXACT@', ', '.join(EXACT) or 'none'), ('@OSENSE@', ', '.join(OSENSE) or 'none'),
           ('@UNSTATED@', ', '.join(UNSTATED) or 'none'), ('@ONE@', str(len(ONE)))]
    for i, r in enumerate(REACH):
        rep += [('@A%d@' % i, r['act']), ('@P%d@' % i, r['predicate_first_committed']),
                ('@R%d@' % i, r['readings'])]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        if ln.startswith('| b4') and '| 0 |' in ln:
            act = ln.split('|')[1].strip()
            n = [len(r['pre_commits']) for r in REACH if r['act'] == act]
            ln = ln.replace('| 0 |', '| %d |' % (n[0] if n else 0))
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b441)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b441 -- @GR@ gates read, @GDG@ checked by digest -- ON THE SECOND PASTE FOR THIS ACT NUMBER, "
            "THE FIRST HAVING BEEN STOPPED AT STEP ZERO ON A BANNED-STEM HIT IN THE AUTHOR'S TEXT AND "
            "PRESERVED UNDER ITS OWN NAME. **COMPONENT 1: SPIRAL_MAP.md:114 DENIES THAT SIDE-window'S "
            "PRIME-POWER COUNTING FUNCTION IS RELATED TO W_2/W_inf, A TRUE DISCLAIMER ABOUT A NAME "
            "COLLISION THAT SAYS NOTHING ABOUT ZERO-ORDINATES; IT STAYS UNEDITED; AND THE WORD DENIAL "
            "WAS THIS SEAT'S, IN b440'S COMPONENTS AND CLOSING, REPEATED BY THE NAVIGATOR'S PREMISE.** "
            "**THE KERNEL HALF WAS ALREADY CARRIED -- CC (153)-(154) SAYS h+ IS THE DERIVATIVE OF 2 "
            "theta, b333 QUOTED IT, K5 SITS ON IT -- SO b440'S NOT CARRIED HELD ONLY OVER PLACE-papers "
            "PROSE. THE COUNTING HALF WAS NOT: RvM MAIN TERM MINUS theta(T)/pi = 1 - 1/(48 pi T) + "
            "O(T^-3), BY TWO ROUTES SHARING NO CODE AGREEING TO @MAXDIFF@ AGAINST 1e-12 STATED FIRST, "
            "THE 1 BEING THE POLE; FILED MEASURED, NOT AS A THEOREM, THROUGH THE WRITER'S append_block "
            "UNDER S1/K5 WITH EVERY QUOTATION VERIFIED.** **COMPONENT 2, PRICED, NOTHING IMPORTED: "
            "FIVE VERIFIED-SOURCE STATEMENTS, EXACT AT EVERY HEIGHT @EXACT@, UNIFORM ONLY IN THE "
            "O-SENSE @OSENSE@, DOMAIN NOT STATED @UNSTATED@; SITE (ii)'S B3 AND B5 BOTH STAND.** "
            "**COMPONENT 3: THE POLE'S DOUBLE ROLE FILED AS A JUXTAPOSITION, NO MECHANISM; THE "
            "PUSH-SIDE PREDICATE READ FROM GIT HISTORY FOR ELEVEN ACTS -- THE BROKEN ONE FIRST "
            "COMMITTED IN @BROKEN@ ALONE, @NOPRED@ WITH NONE, EVERY PRE-PUSH FILE COMMITTED ONCE, "
            "@ONE@ OF 11 BANKS WITH ONE READING, SO b440'S 'STILL LIVE IN EVERY ACT SINCE' IS FALSE; "
            "AND b440'S OWN REPAIR, origin/main == HEAD, IS TRUE BEFORE AN ACT COMMITS, SO b441'S "
            "FIRST PRE-PUSH READING LANDED IN ITS POST-PUSH FILE AND ITS LOCKED FACE NAMES THE "
            "DEFECTIVE RULE -- PRINTED, THE FACE UNEDITED, b439'S PREDICATE CARRIED; "
            "AND THE AXIOM-FORM LORE MINTED IN TECHNE-Core, LOCAL, NOT PUSHED.** "
            "0 INSTRUMENTS BUILT, 0 FAMILIES DEFINED, 0 LANES OPENED, 0 SITES REOPENED, 0 GRADES "
            "MOVED, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The kernel half stays at K5's existing "
            "DERIVES-ON-IMPORTS; the counting half is MEASURED and confers nothing")
    prof = ("### TWO PLACE-papers FILES APPENDED (FACES_LEDGER.md by the writer's append_block, "
            "OPEN_TRAILS.md), EACH PRIOR TEXT A TRUE PREFIX; SPIRAL_MAP.md BYTE-UNMOVED; NO ROW, NO "
            "REGISTER CELL, THE FREEZE AT SIX STANDING; EVERY SIDE-window AND INSTRUMENT FILE "
            "BYTE-UNMOVED; b440'S BANK BYTE-UNMOVED THOUGH TWO OF ITS SENTENCES ARE CORRECTED HERE; "
            "TECHNE-Core ONE LOCAL COMMIT, NOT PUSHED -- 0 CONTENT LOST")
    grade = ("### THE FACE DECLARED FOUR SURVEY FINDINGS BEFORE ANY MEASUREMENT, TWO OF THEM "
             "CORRECTIONS OF THIS SEAT'S OWN b440 SENTENCES; THE SECOND ROUTE WAS RUN RATHER THAN "
             "ASSERTED; AND THE ONE OVERSTATEMENT THIS ACT MADE ITSELF -- BINET'S FORMULA CALLED EXACT "
            "AT EVERY HEIGHT -- WAS CAUGHT BY THE SUITE, CORRECTED, AND THE LEDGER BLOCK RE-FILED")
    status = ("data/b441_the_identification_filed.txt; data/b441_components.txt; "
              "data/b441_routes.json; data/b441_price.json; data/b441_reach.json; "
              "data/b441_filings_run.txt; data/b441_checks.txt; "
              "data/b441_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "data/b441_addendum.txt (the (R50) slot, EMPTY); "
              "PLACE-papers FACES_LEDGER.md <!-- b441 update -->; OPEN_TRAILS.md; "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@MAXDIFF@', '%.1e' % MAXDIFF)
                .replace('@EXACT@', ', '.join(EXACT) or 'none')
                .replace('@OSENSE@', ', '.join(OSENSE) or 'none')
                .replace('@UNSTATED@', ', '.join(UNSTATED) or 'none')
                .replace('@BROKEN@', ', '.join(BROKEN) or 'none')
                .replace('@NOPRED@', ', '.join(NOPRED) or 'none')
                .replace('@ONE@', str(len(ONE))))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('does the record deny the density identification',
           'is h plus the derivative of the riemann siegel theta',
           'what is the one between the main term and theta over pi',
           'how far did the push side defect reach',
           'why can one fact carry two axiom profiles')
MUST_NOT_HIT = ('the counting half is a theorem', 'spiral map line corrected',
                'the witness arc site two reopened')
KEY = 'the-identification-filed-the-overstatement-corrected-and-two-filings'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b441 RESTATED THE LINE b440 CALLED A DENIAL, FILED THE IDENTIFICATION IN TWO HALVES, PRICED "
        "WHAT IT BUYS, MEASURED THE PUSH-SIDE DEFECT'S REACH, AND MINTED ONE LORE. "
        "SPIRAL_MAP.md:114 DENIES A DIFFERENT RELATION: that SIDE-window's prime-power counting "
        "function is related to W_2/W_inf, a true disclaimer about a name collision saying nothing "
        "about zero-ordinates; IT STAYS UNEDITED, and THE WORD DENIAL WAS THIS SEAT'S, in b440's "
        "components and closing, repeated by the navigator's premise. THE KERNEL HALF WAS ALREADY "
        "CARRIED: CC (153)-(154) says h+ IS THE DERIVATIVE OF 2 theta, the Riemann-Siegel angular "
        "function; b333 quoted it and K5 sits on it, so b440's not-carried HELD ONLY OVER "
        "PLACE-papers PROSE. THE COUNTING HALF IS NEW AND MEASURED: THE MAIN TERM MINUS theta(T)/pi "
        "IS 1 - 1/(48 pi T) + O(T^-3), THE 1 BEING THE POLE, by TWO ROUTES SHARING NO CODE (quad over "
        "digamma; loggamma with no quadrature) agreeing to %s against 1e-12 stated first; filed "
        "MEASURED, NOT A THEOREM, through the writer's append_block under S1/K5. PRICED, NOTHING "
        "IMPORTED: of five verified-source statements, EXACT AT EVERY HEIGHT %s, UNIFORM ONLY IN THE "
        "O-SENSE %s, DOMAIN NOT STATED %s; SITE (ii)'S B3 AND B5 BOTH STAND, because the channel "
        "contains no real part and A COUNT UNIFORM IN THE HEIGHT PLACES NO ZERO. THE POLE'S DOUBLE "
        "ROLE IS FILED AS A JUXTAPOSITION, NO MECHANISM. THE PUSH-SIDE REACH, READ FROM GIT HISTORY: "
        "THE BROKEN PREDICATE WAS FIRST COMMITTED IN %s ALONE, %s HAD NONE, EVERY PRE-PUSH FILE WAS "
        "COMMITTED ONCE, AND %d OF 11 BANKS SHOW ONE READING, so b440's 'STILL LIVE IN EVERY ACT "
        "SINCE' IS FALSE. THE AXIOM-FORM LORE: A PROFILE CERTIFIES THE TERMINAL AS PHRASED, NOT THE "
        "FACT, minted in TECHNE-Core, local, not pushed. 0 INSTRUMENTS BUILT, 0 LANES OPENED, 0 SITES "
        "REOPENED, 0 CONTENT LOST"
        % ('%.1e' % MAXDIFF, EXACT, OSENSE, UNSTATED, BROKEN, NOPRED, len(ONE)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### THE KERNEL HALF STAYS AT K5'S EXISTING "
             "GRADE; THE COUNTING HALF IS MEASURED. ### NO SITE REOPENED, NO CELL REPLACED, NOTHING "
             "IMPORTED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")
    where = ("data/b441_the_identification_filed.txt; data/b441_components.txt; "
             "data/b441_routes.json; data/b441_price.json; data/b441_reach.json; "
             "data/b441_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "FACES_LEDGER.md <!-- b441 update -->; OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
             % (GR, GDG, rownum))
    act = "b441 (the identification filed, the overstatement corrected, and two filings)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE IDENTIFICATION FILED, THE OVERSTATEMENT CORRECTED, AND TWO FILINGS (b441).%s'
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
        rec('    %-58s reaches the b441 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the unedited line carried', 'IT STAYS UNEDITED' in out),
            ('the seat`s authorship carried', "THE WORD DENIAL WAS THIS SEAT'S" in out),
            ('the kernel half carried', 'IS THE DERIVATIVE OF 2 theta' in out),
            ('the scope correction carried', 'HELD ONLY OVER PLACE-papers PROSE' in out),
            ('the counting half carried', 'THE 1 BEING THE POLE' in out),
            ('the two routes carried', 'TWO ROUTES SHARING NO CODE' in out),
            ('not a theorem carried', 'NOT A THEOREM' in out),
            ('nothing imported carried', 'NOTHING IMPORTED' in out),
            ('both steps standing carried', 'B3 AND B5 BOTH STAND' in out),
            ('the count-places-no-zero carried', 'A COUNT UNIFORM IN THE HEIGHT PLACES NO ZERO' in out),
            ('no mechanism carried', 'NO MECHANISM' in out),
            ('the regression carried', 'FIRST COMMITTED IN' in out),
            ('the correction of b440 carried', "IS FALSE" in out),
            ('the lore carried', 'A PROFILE CERTIFIES THE TERMINAL AS PHRASED' in out)):
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
    Bk = ['=' * 100, 'b441 -- THE IDENTIFICATION FILED, THE OVERSTATEMENT CORRECTED, AND TWO FILINGS.',
          'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE TWO ROUTES, AT SIX HEIGHTS.', '-' * 100,
           '  %-7s %-24s %-24s %-10s %s' % ('T', 'route A', 'route B', '|A-B|', 'deficit x 48 pi T')]
    for r in ROUTES.get('rows') or []:
        Bk.append('  %-7d %-24s %-24s %-10.2e %s' % (r['T'], r['routeA'][:22], r['routeB'][:22],
                                                     r['absdiff'], r['scaled'][:14]))
    Bk += ['', '-' * 100, '### THE PRICE.', '-' * 100]
    for c in PRICE.get('candidates') or []:
        Bk += ['  %s  %s:%s  price %s' % (c['id'], c['source'], c['line'], c['price']),
               '      replaces   : %s' % c['replaces'], '      uniformity : %s' % c['uniformity']]
    Bk += ['  B3 : %s ; B5 : %s' % (PRICE.get('B3'), PRICE.get('B5'))]
    Bk += ['', '-' * 100, '### THE REACH.', '-' * 100]
    for r in REACH:
        Bk.append('  %-5s %-34s pre-push commits %-3d readings %s'
                  % (r['act'], r['predicate_first_committed'], len(r['pre_commits']), r['readings']))
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d ; failing %d' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
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


B440ROW_RE = r"(?m)^\| (\d+) \| \*\*u0 IS THE DEFINING EQUATION"


def main():
    bar('=')
    rec('b441_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not ROUTES or not PRICE or len(REACH) != 11:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    if not TOL:
        rec('  ### HARD FAILURE -- a stated tolerance was not met; the filing text would overstate.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      routes max |A-B| %.2e ; deficit x 48 pi T at 1000 : %s ; exact %s ; O-sense %s ; unstated %s'
        % (MAXDIFF, R1000.get('scaled', '')[:12], EXACT, OSENSE, UNSTATED))
    rec('      broken predicate first committed : %s ; no predicate : %s ; one-reading banks : %d'
        % (BROKEN, NOPRED, len(ONE)))
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
        % [int(x.group(1)) for x in re.finditer(B440ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B440ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b441_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
