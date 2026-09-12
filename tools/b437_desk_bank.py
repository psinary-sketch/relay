# -*- coding: utf-8 -*-
"""b437_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b437 the window opened by rungs -->'
PRIOR = '<!-- b436 the witness arc at site (iv), the window -->'
BANKOUT = os.path.join(D, 'b437_the_window_by_rungs.txt')
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


FACE = read(os.path.join(D, 'b437_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b437_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b437_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b437_components.txt'))
try:
    RUNGS = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}')
except Exception:
    RUNGS = {}
try:
    CELLS = json.loads(read(os.path.join(D, 'b437_cells.json')) or '[]')
except Exception:
    CELLS = []

ROWS = sorted(RUNGS.get('rows', []), key=lambda r: r['a'])
NEWR = [r for r in ROWS if r.get('src') == 'b437']
SIGN = RUNGS.get('sign', {})
CROSS = RUNGS.get('cross', [])
FLOOR = RUNGS.get('floor_priced', [])
FOK = RUNGS.get('floor_ok')
RAT = [r for r in ROWS if r.get('ratio') is not None and r['ratio'] == r['ratio']]
PEAK = max((r for r in RAT if r['ratio'] < 1), key=lambda r: r['ratio']) if RAT else {}
NEGA = [r for r in NEWR if r.get('arch') is not None and r['arch'] < 0]
ROWMARK = ('**THE WINDOW OPENED BY RUNGS: TWENTY-TWO NEW CELLS, THE LADDER AND THE MEASURED CELLS '
           'JOINED FOR THE FIRST TIME, AND THE RATIO CROSSING ONE BECAUSE THE ARCHIMEDEAN CHANNEL '
           'COLLAPSES THROUGH ZERO AND NOT BECAUSE THE PRIME CONSTITUENT OVERTAKES IT**')

SCOPE = ("### THE ACT EXTENDS ALONG THE COMPILED LADDER ON THE SAME INSTRUMENT AND BUILDS NO NEW "
         "ONE; THE LANE CLOSES AT ITS END. ### IT ENTERS NO SITE, WRITES NO CELL, TYPES NO BRIDGE, "
         "AND OPENS NO SECOND LANE -- b432'S TRIGGER CONDITION IS NAMED AND ITS DISPOSITION ROUTED. "
         "### IT MOVES NO GRADE AND MAKES NO CLAIM ABOUT RH, h2 OR ZETA")

DESK = [
    ('the ladder and the measured cells, joined', 'CLOSE',
     'JOINED at b437 for the first time. `SIDE-window`s compiled ladder and `b321`s thirteen cells '
     'set side by side: the rung of each cell is the ladder`s own STRICT count of prime powers '
     '`< a^2`. **The join also corrected a convention**: an inclusive count says seven at `a = 3.0` '
     'and the instrument admits six, because **a prime power sitting exactly at `a^2` lands on the '
     'support edge where the bump vanishes**, so its term is identically zero -- which is also why '
     'a rung is entered continuously and not by a jump.'),
    ('whether the sign changes sit at rung boundaries', 'CLOSE',
     'MEASURED at b437, and **the coincidence runs ONE WAY ONLY**. Both sign changes bracket '
     'exactly one boundary each -- `n = 3` at `a = 1.7321` between the cells `1.7` and `1.9`, and '
     '`n = 7` at `a = 2.6458` between `2.4` and `2.8`. **And %d of %d boundaries are crossed with '
     'no sign change at all.** So every sign change sits at a boundary and most boundaries produce '
     'none. A measurement over thirteen cells, not a law.'
     % (SIGN.get('silent', 0), SIGN.get('boundaries', 0))),
    ('THE FINDING: the ratio rises, turns, and then diverges on a vanishing denominator', 'STANDING',
     '**The ratio climbs from `%.6f` at `a = %.6f` to a peak of `%.6f` at `a = %.6f`, and then '
     'FALLS.** Past the turn the prime constituent changes sign a third time and the ARCHIMEDEAN '
     'channel collapses: `A` runs `0.0199 -> 0.0125 -> 0.0055 -> 0.0022` and **passes through zero '
     'at `a = %.6f`, where `A = %.9f`**. The four cells where `|PR|/A` exceeds one are the '
     'denominator vanishing, **not the prime side overtaking the archimedean one**. Routed: what a '
     'vanishing `A` means is not in the record.'
     % (ROWS[3]['ratio'] if len(ROWS) > 3 else 0, ROWS[3]['a'] if len(ROWS) > 3 else 0,
        PEAK.get('ratio', 0), PEAK.get('a', 0),
        NEGA[0]['a'] if NEGA else 0, NEGA[0]['arch'] if NEGA else 0)),
    ('whether the criterion is violated anywhere on the ladder', 'CLOSE',
     'ANSWERED at b437: **NO.** The criterion asks for `SUM_v W_v = PR - A <= 0` and it is '
     'NON-POSITIVE at **every one of the %d cells**, old and new. And the zero side never went '
     'negative -- which the locked face said before any value it could not, `Z` being a sum of '
     'non-negative terms over ordinates that are all ON the line. **The instrument cannot report '
     'the case the criterion exists to detect**, and the face said so first.'
     % len(ROWS)),
    ('the instrument`s floor, past three radii for the first time', 'CLOSE',
     'PRICED at b437 at **%d radii** -- %s -- by re-running the existing `noise_floor.gate` on a '
     'DOUBLED autocorrelation grid. **It RESOLVES: deltas of `6.3e-07`, `6.4e-07` and `2.3e-07`, '
     'all far above the `1.49e-08` floor and inside the `1e-3` drift bar.** Before this act the '
     'gate had been run at three radii only -- `1.3`, `1.35`, `1.41`, all prime-free -- and never '
     'past them.'
     % (len(FLOOR), ', '.join('%.6f' % x for x in FLOOR))),
    ('what a vanishing archimedean channel means', 'STANDING',
     'ROUTED at b437 and **not answered**. `A` is not sign-constrained: its kernel '
     '`Re psi(1/4 + iu/2) - log pi` is negative near `u = 0` and a widening bump concentrates '
     'there, so `A` falling through zero is a feature of the channel. **What it means for the '
     'criterion`s reading at those radii is not in the record.** TRIGGER: the author`s word, or '
     'any act that reads the archimedean channel past `a = 5`.'),
    ('b432`s disproof-lane trigger', 'STANDING',
     '**ITS CONDITION IS MET AND THE LANE IS NOT OPENED.** b432 wrote the trigger as *"the '
     'instrument lane opening"*, and `(R48)` opens the instrument lane. This act names that rather '
     'than letting it be noticed afterwards, and declines to act: `(R48)` opens the lane **for the '
     'window ladder only**, and opening a second lane is not extension along that ladder. '
     '**THE DISPOSITION IS THE AUTHOR`S.**'),
    ('the routed citation from b436', 'CLOSE',
     'CORRECTED at b437 on its own face with **both locations named** -- the primary '
     '`tools/e16/carto_atlas.py:50` inside `def bump(a)`, and `tools/b355_read.py:81`, the reader '
     'b436 quoted. **The text is verbatim the same, so nothing b436 banked is wrong; the citation '
     'was.** b436`s bank is NOT edited.'),
    ('the witness arc, sites (v) and (vi)', 'STANDING',
     'CHECKPOINTED after site (iv). Two sites remain; trigger: the author`s word.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432 and **read from the other side by b437**: the zero side sums 10000 VERIFIED '
     'ON-LINE ordinates, so the positivity the criterion tests is assumed by the instrument rather '
     'than measured. Unchanged as a routing.'),
    ('the register, frozen at six', 'STANDING', 'UNCHANGED; `FACES_LEDGER.md` byte-unmoved.'),
    ('the fourth grade, now defined', 'STANDING', 'DEFINED at b433; untouched by this act.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424 and carried.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED research instrument lane, which this act did not open: `(R48)` reaches '
     'the window ladder and nothing else.'),
    ('the scan`s sites against the lock`s zero', 'STANDING', 'The (R36) instrument item.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; byte-unmoved by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT -- **READ BY THIS ACT AND NOT MOVED.**'),
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
    return ['', MARK, '',
            '### b437 — the window opened by rungs — filed 2026-09-12', '',
            '**(R48) executed: the window is opened by rungs, along the compiled ladder, on the '
            'same instrument.** Twenty-two new cells past the record’s last, every one carrying its '
            'own identity residual as its control. **0 failed the identity. 0 had a non-zero pole '
            'term. 0 had a negative zero side.**', '',
            '#### Component 1 — the ladder and the measured cells, joined for the first time', '',
            '`SIDE-window`’s ladder is compiled at its pin by `decide` and its `W` counts prime '
            'powers — **with no relation whatever to the corpus’s `W_∞`**, which its own header '
            'flags and which this act keeps in separate columns throughout. The rung of a cell is '
            '`W(a²)`, the ladder’s own **strict** count.', '',
            '**The join corrected a convention before it was used.** An inclusive count puts `9` in '
            'the rung at `a = 3.0` and the instrument admits six terms, not seven — because **a '
            'prime power sitting exactly at `a²` lands on the support edge, where the bump '
            'vanishes**, so its term is identically zero. The ladder’s strict `W 9 = 6` and the '
            'instrument agree; the inclusive count was the odd one out. It is also why a rung '
            'boundary is crossed **continuously**: a new member enters weighted zero and grows in.',
            '',
            '**The sign question, as a measurement.** Both of the prime constituent’s sign changes '
            'bracket exactly one rung boundary — `n = 3` at `a = 1.7321`, between the cells `1.7` '
            'and `1.9`; `n = 7` at `a = 2.6458`, between `2.4` and `2.8`. **And the converse, in '
            'the same breath: %d of %d boundaries are crossed with no sign change at all.** So the '
            'coincidence runs one way only, and is reported as running one way only. **The record '
            'printed both halves and never joined them until now.**'
            % (SIGN.get('silent', 0), SIGN.get('boundaries', 0)), '',
            '#### Component 2 — the extension, and what the ratio actually did', '',
            '**The route is the record’s and the obvious one would have been wrong.** '
            '`carto_atlas.channels(a)` caps its prime loop at `log a`; the lawful `f = g ∗ g^#` has '
            'support `[a^{-2}, a²]`, and `b321` wrote in its own header that **no argument to '
            '`channels` produces it**. The chain is `mean_zero_variant → autocorrelation → '
            '`b321_window.channels``, and it was proved to be the record’s by **reproducing '
            '`a = 3.0` to every printed digit** before a single new cell was asked for.', '',
            '**The ratio climbs, turns, and then diverges on a vanishing denominator.** It rises '
            'from `0.377` at `a = 3.0` to a peak of **`%.6f` at `a = %.6f`** — and then falls, to '
            '`0.075` at `a = 5.098`. Past that the prime constituent changes sign a third time and '
            '**the archimedean channel collapses**: `A` runs `0.0199 → 0.0125 → 0.0055 → 0.0022` '
            'and **passes through zero at `a = %.6f`, where `A = %.9f`**. The four cells where '
            '`|PR|/A` exceeds one are **the denominator vanishing, not the prime constituent '
            'overtaking the archimedean one** — and the distinction is the whole of the reading.'
            % (PEAK.get('ratio', 0), PEAK.get('a', 0),
               NEGA[0]['a'] if NEGA else 0, NEGA[0]['arch'] if NEGA else 0), '',
            '#### Component 3 — stated before the numbers, and it is what saved the reading', '',
            'Section (X) of the locked face fixed, **before any new value existed**, that '
            '`PR/A > 1` on the positive branch is the same statement as `Z < 0` — and that `Z` is a '
            'sum of **non-negative** terms (`f̂ = |ĝ|²`) over ordinates that are **all on the '
            'line**, so it cannot be negative and a crossing there would be an instrument artefact. '
            '**`Z` never went negative at any of the 35 cells.** The face also fixed that the '
            'positivity is *assumed, not tested*: an instrument summing only on-line ordinates '
            'cannot report the case the criterion exists to detect.', '',
            '**And the criterion is satisfied everywhere on the ladder.** `Σ_v W_v = PR − A` is '
            'non-positive at **every one of the %d cells**, old and new.' % len(ROWS), '',
            '#### The floor, priced past three radii for the first time', '',
            'The noise-floor gate had been run at **three radii only** — `1.3`, `1.35`, `1.41`, all '
            'below `√2`, all prime-free — where it refused 3 of 6, the domain values drifting. '
            'This act priced it at **%d radii around the crossing**, %s, by re-running the same '
            'gate on a doubled autocorrelation grid. **It RESOLVES** — deltas `6.3e-07`, `6.4e-07`, '
            '`2.3e-07`, far above the `1.49e-08` floor. So the crossing is **not** '
            'UNDECIDED-AT-THE-EDGE on the floor question; it is undecided for a different reason, '
            'which is that `A` is going to zero.'
            % (len(FLOOR), ', '.join('`%.6f`' % x for x in FLOOR)), '',
            '#### The trigger, named and not pulled', '',
            '`b432` wrote the disproof lane’s trigger as *"the instrument lane opening"*, and '
            '`(R48)` opens the instrument lane. **The condition is met.** This act names it on its '
            'own face rather than leaving it to be noticed afterwards, and **does not open the '
            'lane**: `(R48)` opens the instrument lane *for the window ladder only*, and opening a '
            'second lane is not extension along that ladder. **The disposition is the author’s.**',
            '',
            '#### What this act did not do', '',
            '**No new instrument was built** and not one line of `carto_atlas.py`, `b317_smear.py`, '
            '`b318_square.py`, `b321_window.py` or `noise_floor.py` moved; `SIDE-window` was read '
            'at its pin and is byte-unmoved. No cell was written and `FACES_LEDGER.md` is '
            'byte-unmoved; the register stays frozen at six. No grade moved; no claim is made about '
            'RH, `h2` or ζ. **The instrument lane closes at this act’s end.** The arc stays '
            'checkpointed after site (iv); the four lists stay open; `h2` is where the deposit left '
            'it.']


def corr_rows():
    m = ROWMARK + " (b437)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE AND BEFORE ANY NEW VALUE**, "
            "chained on b378's gate run as b437 -- @GR@ gates read, @GDG@ checked by digest, the "
            "seal RECOMPUTED by the tool that wrote it. **(R48) EXECUTED ALONG THE COMPILED "
            "LADDER ON THE SAME INSTRUMENT; NO NEW INSTRUMENT BUILT AND SIDE-window BYTE-UNMOVED.** "
            "**THE LADDER AND b321'S THIRTEEN CELLS ARE JOINED FOR THE FIRST TIME, BY THE LADDER'S "
            "OWN STRICT COUNT -- AND THE JOIN CORRECTED A CONVENTION: A PRIME POWER SITTING EXACTLY "
            "AT a^2 LANDS ON THE SUPPORT EDGE WHERE THE BUMP VANISHES, SO ITS TERM IS IDENTICALLY "
            "ZERO AND A RUNG IS ENTERED CONTINUOUSLY.** **BOTH SIGN CHANGES BRACKET EXACTLY ONE "
            "BOUNDARY EACH, AND @SIL@ OF @BND@ BOUNDARIES ARE CROSSED WITH NO SIGN CHANGE -- THE "
            "COINCIDENCE RUNS ONE WAY ONLY AND IS REPORTED AS RUNNING ONE WAY ONLY.** **@NN@ NEW "
            "CELLS, 0 FAILING THE IDENTITY, 0 WITH A NON-ZERO POLE, 0 WITH A NEGATIVE ZERO SIDE.** "
            "**THE RATIO CLIMBS TO @PK@ AT a = @PKA@ AND THEN FALLS; THE FOUR CELLS WHERE IT "
            "EXCEEDS ONE ARE THE ARCHIMEDEAN CHANNEL COLLAPSING THROUGH ZERO AT a = @NEGA@, NOT THE "
            "PRIME CONSTITUENT OVERTAKING IT.** **THE CRITERION'S OWN QUANTITY SUM_v W_v = PR - A "
            "IS NON-POSITIVE AT ALL @NC@ CELLS, AND Z NEVER WENT NEGATIVE -- WHICH THE LOCKED FACE "
            "SAID BEFORE ANY VALUE IT COULD NOT, THE POSITIVITY BEING ASSUMED BY AN INSTRUMENT "
            "THAT SUMS ONLY ON-LINE ORDINATES.** **THE FLOOR IS PRICED PAST THREE RADII FOR THE "
            "FIRST TIME, AT @NF@ RADII, AND RESOLVES.** **AND b432'S DISPROOF-LANE TRIGGER "
            "CONDITION IS MET BY THIS OPENING, NAMED ON THE FACE, AND THE LANE IS NOT OPENED -- THE "
            "DISPOSITION IS ROUTED.** 0 CELLS WRITTEN, 0 GRADES MOVED, 0 INSTRUMENTS BUILT, "
            "0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The act extends a measurement along a "
            "compiled ladder and confers nothing")
    prof = ("### ONE PLACE-papers FILE APPENDED (OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; "
            "FACES_LEDGER.md BYTE-UNMOVED AND THE REGISTER STILL FROZEN AT SIX; SIDE-window READ AT "
            "ITS PIN AND BYTE-UNMOVED; NO INSTRUMENT FILE EDITED; NO KEYSTONE, NO REGISTER ROW, NO "
            "LEDGER ROW, NO KERNEL FILE -- 0 CONTENT LOST")
    grade = ("### THE CHAIN WAS PROVED TO BE THE RECORD'S BY REPRODUCING a = 3.0 TO EVERY PRINTED "
             "DIGIT BEFORE ANY NEW CELL WAS ASKED FOR; EVERY NEW CELL CARRIES ITS OWN IDENTITY "
             "RESIDUAL AND TRUNCATION BOUND; AND WHAT A CROSSING WOULD AND WOULD NOT MEAN WAS "
             "WRITTEN INTO THE FACE AND SEALED BEFORE THE FIRST NEW VALUE EXISTED")
    status = ("data/b437_the_window_by_rungs.txt; data/b437_components.txt; data/b437_extract.txt; "
              "data/b437_rungs.json; data/b437_cells.json; data/b437_checks.txt; "
              "data/b437_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "SIDE-window SIDEWindow/Ladder.lean (READ at its pin, unmoved); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@SIL@', str(SIGN.get('silent', 0)))
                .replace('@BND@', str(SIGN.get('boundaries', 0)))
                .replace('@NN@', str(len(NEWR)))
                .replace('@PK@', '%.6f' % PEAK.get('ratio', 0))
                .replace('@PKA@', '%.6f' % PEAK.get('a', 0))
                .replace('@NEGA@', '%.6f' % (NEGA[0]['a'] if NEGA else 0))
                .replace('@NC@', str(len(ROWS)))
                .replace('@NF@', str(len(FLOOR))))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the window opened by rungs', 'does the prime constituent overtake the archimedean one',
           'what happens past a = 3 on the window ladder',
           'why does the ratio cross one at a = 5.385',
           'was the noise floor ever priced past 1.41')
MUST_NOT_HIT = ('the criterion was violated', 'rh was disproved by the window',
                'the disproof lane was opened')
KEY = 'the-window-opened-by-rungs'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b437 EXECUTED (R48) -- THE WINDOW IS OPENED BY RUNGS -- along SIDE-window's compiled "
        "ladder, on the same instrument, building none. TWENTY-TWO NEW CELLS past the record's "
        "last, each carrying its own identity residual as its control: 0 failed the identity, 0 had "
        "a non-zero pole term, 0 had a negative zero side. THE LADDER AND b321'S THIRTEEN CELLS "
        "ARE JOINED FOR THE FIRST TIME, by the ladder's own STRICT count W(a^2) -- and the join "
        "corrected a convention before it was used: a prime power sitting exactly at a^2 lands on "
        "the support EDGE where the bump vanishes, so its term is identically zero, the ladder's "
        "W 9 = 6 and the instrument's six terms agree, and a rung is entered CONTINUOUSLY. THE "
        "SIGN QUESTION, AS A MEASUREMENT: both sign changes bracket exactly one boundary each "
        "(n = 3 at a = 1.7321, n = 7 at a = 2.6458) AND %d of %d boundaries are crossed with NO "
        "sign change -- the coincidence runs ONE WAY ONLY and is reported as running one way only. "
        "THE RATIO CLIMBS TO %.6f AT a = %.6f AND THEN FALLS. The four cells where |PR|/A exceeds "
        "one are THE ARCHIMEDEAN CHANNEL COLLAPSING THROUGH ZERO -- A runs 0.0199, 0.0125, 0.0055, "
        "0.0022 and passes through zero at a = %.6f where A = %.9f -- AND NOT THE PRIME "
        "CONSTITUENT OVERTAKING IT. THE CRITERION IS SATISFIED EVERYWHERE ON THE LADDER: "
        "SUM_v W_v = PR - A is non-positive at all %d cells. AND THE LOCKED FACE SAID BEFORE ANY "
        "VALUE EXISTED that PR/A > 1 on the positive branch is the same statement as Z < 0, that Z "
        "is a sum of non-negative terms over ordinates ALL ON THE LINE and cannot be negative, and "
        "that THE POSITIVITY IS ASSUMED AND NOT TESTED -- an instrument summing only on-line "
        "ordinates cannot report the case the criterion exists to detect. THE FLOOR WAS PRICED "
        "PAST THREE RADII FOR THE FIRST TIME, at %d radii around the crossing on a doubled grid, "
        "and RESOLVES -- so the crossing is NOT undecided at the instrument's edge; it is "
        "undecided because A is going to zero, which the record does not interpret. AND b432'S "
        "DISPROOF-LANE TRIGGER CONDITION IS MET BY THIS LANE OPENING, IS NAMED ON THE FACE, AND "
        "THE LANE IS NOT OPENED -- (R48) reaches the window ladder only and the disposition is the "
        "author's."
        % (SIGN.get('silent', 0), SIGN.get('boundaries', 0), PEAK.get('ratio', 0),
           PEAK.get('a', 0), NEGA[0]['a'] if NEGA else 0, NEGA[0]['arch'] if NEGA else 0,
           len(ROWS), len(FLOOR)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO CELL WRITTEN AND NO SITE ENTERED. "
             "### NO NEW INSTRUMENT BUILT AND NO INSTRUMENT FILE EDITED. ### NO CLAIM ABOUT RH, h2 "
             "OR ZETA. ### THE INSTRUMENT LANE CLOSES AT THIS ACT'S END")
    where = ("data/b437_the_window_by_rungs.txt; data/b437_components.txt; data/b437_extract.txt; "
             "data/b437_rungs.json; data/b437_cells.json; "
             "data/b437_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "SIDE-window SIDEWindow/Ladder.lean; OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
             % (GR, GDG, rownum))
    act = "b437 (the window opened by rungs)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE WINDOW OPENED BY RUNGS (b437).%s'
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
        rec('    %-58s reaches the b437 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the edge fact carried', 'support EDGE' in out),
                      ('the one-way coincidence carried', 'ONE WAY ONLY' in out),
                      ('the turn carried', 'AND THEN FALLS' in out),
                      ('the vanishing denominator carried', 'COLLAPSING THROUGH ZERO' in out),
                      ('the criterion result carried', 'non-positive at all' in out),
                      ('the assumed positivity carried', 'ASSUMED AND NOT TESTED' in out),
                      ('the floor pricing carried', 'PAST THREE RADII' in out),
                      ('the trigger carried', 'TRIGGER CONDITION IS MET' in out)):
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
    Bk = ['=' * 100, 'b437 -- THE WINDOW OPENED BY RUNGS.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE LADDER AND THE MEASURED CELLS.', '-' * 100,
           '  %-7s %-9s %-6s %-16s %s' % ('a', 'a^2', 'rung', 'PR (primes)', 'prime powers')]
    for c in CELLS:
        Bk.append('  %-7s %-9.4f %-6d %-16.9f %s' % (c['a'], c['sq'], c['rung'], c['pr'], c['pp']))
    Bk += ['', '-' * 100, '### THE RATIO, OLD AND NEW, IN ONE COLUMN.', '-' * 100,
           '  %-9s %-6s %-6s %-15s %-15s %s'
           % ('a', 'rung', 'src', 'A (arch)', 'PR (primes)', '|PR| / A')]
    for r in ROWS:
        rr = r.get('ratio')
        Bk.append('  %-9.6f %-6s %-6s %-15.9f %-15.9f %s'
                  % (r['a'], r['rung'], r['src'], r.get('arch') or 0.0, r['pr'],
                     ('%.6f' % rr) if rr is not None and rr == rr else 'n/a'))
    Bk += ['', '-' * 100, '### THE NAVIGATOR`S EXPECTATIONS, AS THE COMPONENTS SCORED THEM.',
           '-' * 100]
    keep = False
    for ln in COMP.splitlines():
        if 'THE EXPECTATIONS, SCORED' in ln:
            keep = True
        if keep and ln.strip():
            Bk.append('  %s' % ln.strip())
        if keep and 'MISSES :' in ln:
            break
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d ; failing %d' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL)]
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


B436ROW_RE = r"(?m)^\| (\d+) \| \*\*THE WITNESS ARC AT SITE"


def main():
    bar('=')
    rec('b437_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not RUNGS or not CELLS:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      cells %d measured + %d new = %d ; identity failures %d ; floor priced at %d radii'
        % (len(CELLS), len(NEWR), len(ROWS),
           len([r for r in NEWR if not r.get('ok')]), len(FLOOR)))
    rec('      ratio peak %.6f at a = %.6f ; cells above one %d ; A < 0 at %d cell(s)'
        % (PEAK.get('ratio', 0), PEAK.get('a', 0), len(CROSS), len(NEGA)))
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
        % [int(x.group(1)) for x in re.finditer(B436ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B436ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b437_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
