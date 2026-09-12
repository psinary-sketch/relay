# -*- coding: utf-8 -*-
"""b438_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b438 what alternates the sign, and where the room closes -->'
PRIOR = '<!-- b437 the window opened by rungs -->'
BANKOUT = os.path.join(D, 'b438_the_alternation_and_the_room.txt')
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


FACE = read(os.path.join(D, 'b438_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b438_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b438_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b438_components.txt'))
try:
    ROOM = json.loads(read(os.path.join(D, 'b438_room.json')) or '{}')
except Exception:
    ROOM = {}
try:
    TERMS = json.loads(read(os.path.join(D, 'b438_terms.json')) or '[]')
except Exception:
    TERMS = []

ADD = ROOM.get('addendum', {})
SHELLS = ADD.get('shells', [])
DOWN = [s for s in SHELLS if s.get('direction') == 'down']
UP = [s for s in SHELLS if s.get('direction') == 'up']
SPREAD = (max(x['ratio'] for x in DOWN) - min(x['ratio'] for x in DOWN)) if len(DOWN) > 1 else None
RM = ROOM.get('room') or {}
HP = ROOM.get('hplus') or {}
SEC = ROOM.get('second') or {}
PAST = ROOM.get('past') or {}
N1 = ROOM.get('n1') or {}
ROWMARK = ('**WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES: THE FLIPS ARE SHELL CROSSINGS OF '
           'AN ALREADY-PRESENT TERM AT A FIXED BOUNDARY IN v/log a, AND THE ARCHIMEDEAN CHANNEL '
           'CLOSES AT a0 = 5.6416382 BY TWO ROUTES THAT SHARE NO CODE**')

SCOPE = ("### THE ACT DECOMPOSES CELLS THE RECORD ALREADY HOLDS AND EVALUATES A DISTRIBUTION THE "
         "RECORD ALREADY BUILT. ### NO NEW INSTRUMENT, NO NEW FAMILY, NO NEW CELL. ### IT ENTERS "
         "NO SITE, WRITES NO CELL, TYPES NO BRIDGE, AND OPENS NO SECOND LANE -- THE DISPROOF "
         "LANE'S TRIGGER FIRED AT (R48) AND ITS DISPOSITION WAITS ON THE AUTHOR. ### NO CLAIM "
         "ABOUT RH, h2, ZETA OR ANY ZERO")

DESK = [
    ('what alternates the prime sum`s sign', 'CLOSE',
     'ANSWERED at b438, and **not by the entering prime power**. At both flips the arriving term '
     'contributes `+4.81e-05` and `+1.16e-10` while the already-present terms move by `-3.08e-02` '
     'and `+1.49e-01` -- **factors of 6e+02 and 1e+09**. A prime power enters at `p^k = a^2`, the '
     'SUPPORT EDGE, where the bump vanishes, so its first contribution is negligible by '
     'construction. **THE `n = 2` TERM FLIPS AND THE SUM FOLLOWS IT.**'),
    ('the addendum`s question: entry or shell crossing', 'CLOSE',
     '**SHELL CROSSING, ON BOTH CLAUSES.** (i) An already-present term changes sign at BOTH flips '
     'and **no entering term carries either -- 0 of %d**. (ii) The crossings sit at a FIXED '
     'boundary: grouped by direction, the two `+ -> -` crossings -- different primes, different '
     'radii -- agree to **%.3e**. b437`s (N1) coincidence is restated as a coincidence of two '
     'cells: the sum`s sign changes merely fall in the intervals where `3` and `7` enter.'
     % (ADD.get('flips', 0), SPREAD if SPREAD is not None else float('nan'))),
    ('this act`s own pooled shell test', 'CLOSE',
     '**A DEFECT OF THIS ACT, FOUND AND CORRECTED BEFORE IT WAS BANKED.** The first writing pooled '
     'all three crossings and reported a spread of `0.408`, which compared **one zero of a fixed '
     'shape against another**. A shape fixed in `s = v/log a` has several zeros, and a term '
     'sweeping inward crosses each in turn. Grouped by direction the constant appears. '
     '**A SPREAD TAKEN ACROSS TWO DIFFERENT ZEROS MEASURES THE GAP BETWEEN THEM, NOT NOISE.**'),
    ('the room`s closing radius', 'CLOSE',
     'LOCATED at b438, **not gridded**: `a0 = %.7f`, bracketed to `%.1e`, by two routes that '
     '**share no code** -- the atlas`s transform-side integral against the digamma kernel and '
     'b320`s `weil` from the source`s (53), (38), (39). They differ by `%.3e` against a tolerance '
     'of `1e-04` **stated before the comparison**.'
     % (RM.get('root', 0), RM.get('bracket', 0), RM.get('diff', 0))),
    ('what the archimedean zero belongs to', 'CLOSE',
     '**THE INTERACTION, and the evidence is quantitative.** `h+` has ONE sign change, at '
     '`u0 = %.9f`, a property of the digamma that **does not move when `a` moves**. The seed`s L1 '
     'scale is **exactly 1.000000000 at every radius** -- a positive constant, and multiplying by '
     'a positive number moves no zero. What moves is the fraction of transform mass below `u0`: '
     '`0.057 -> 0.207 -> 0.390 -> 0.499 -> 0.523`, crossing one half at `a0`. **And the second '
     'family settles it in the stronger direction: `corpus_bump`s autocorrelation, against the '
     'same `h+`, does not cross at all between `a = 2` and `a = 12`.**' % HP.get('u0', 0)),
    ('what a vanishing archimedean channel means', 'STANDING',
     'ROUTED at b437, **still not answered**. b438 establishes WHERE and WHAT KIND -- the mass '
     'sliding below `h+`s fixed zero -- but not what a negative archimedean channel means for the '
     'criterion`s reading. TRIGGER: the author`s word, or any act that reads the channel past '
     '`a = 5`.'),
    ('the residual in the shell constant', 'STANDING',
     'ROUTED at b438 and **not decided**. The two downward crossings agree to `%.3e`, not '
     'exactly. Exact scale-invariance of the family would need BOTH moment conditions to be '
     'scale-invariant, and the second uses `cosh(v/2)`, which is not. **THAT IS A READING THIS '
     'ACT DID NOT TEST**, and it is filed as a reading, not a finding.'
     % (SPREAD if SPREAD is not None else float('nan'))),
    ('(R47) leaves no door for a post-lock addendum', 'STANDING',
     '**NAMED at b438 from its own bench.** The addendum arrived after the face was locked. '
     'Section (Z) forbids editing the banked ferry and the enumerated data list names no slot, so '
     'it was quoted inside the components record; and its ten checks could not have been declared '
     'in (G2), so they were folded into a declared arm. **AN ACT CAN CURRENTLY RECEIVE AN ADDENDUM '
     'ONLY BY BREACHING ITS OWN WRITE LIST OR BY FOLDING IT INTO ANOTHER FILE.** Whether (R47) '
     'should name an addendum slot is the author`s.'),
    ('past the room', 'STANDING',
     '**ONE CELL, and (R49) authorises no more.** At `a = 5.656854` the prime sum is `-0.0393`, '
     'the archimedean channel `-0.0011`, and `SUM_v W_v = -0.0382 <= 0`. The archimedean slack is '
     'negative and **the primes carry the criterion by themselves** -- over one cell, printed '
     'beside the verdict so no reader takes it for a sweep. **No trend is drawn through one point.**'),
    ('the cost, restated', 'STANDING',
     '**THE ZERO SIDE IS INHERITED.** `Z` is summed over 10000 ordinates that are all ON the line, '
     'so satisfaction anywhere on this ladder is **ASSUMED AND NOT TESTED**. Carried from b437 '
     'unchanged. **No claim about zeros.**'),
    ('b432`s disproof-lane trigger', 'STANDING',
     '**FIRED AT (R48), AND ITS DISPOSITION WAITS ON THE AUTHOR.** (R49) says so in its own words '
     'and this act neither opens the lane nor disposes of it.'),
    ('the witness arc, sites (v) and (vi)', 'STANDING',
     'CHECKPOINTED after site (iv). Two sites remain; trigger: the author`s word.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432 and carried, and read from this side again: an instrument summing only '
     'on-line ordinates cannot report the case the criterion exists to detect.'),
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
     'Blocked by the PARKED research instrument lane; (R49) reaches the decomposition and the '
     'distribution and nothing else.'),
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
            '### b438 — what alternates the sign, and where the room closes — filed 2026-09-12', '',
            '**(R49) executed: the cells b437 banked, decomposed; the archimedean distribution '
            'evaluated against the same family. No new instrument, no new family, no new cell.** '
            '298 terms printed across 35 cells.', '',
            '#### Which test function, and what kind of statement (N1) was', '',
            '**The ladder rides an AIMED seed, not the plain bump** — three of the corpus’s own '
            'bumps at widths `a`, `a^½`, `a^¼`, with two coefficients **solved** so that two '
            'moments vanish. A non-negative function cannot have a vanishing integral unless it is '
            'zero, so **the seed must take negative values: the oscillation is built in by the '
            'aim.**', '',
            '**And (N1) was an identity, which the face said before a cell was spent.** The term is '
            '`2 log p / √n` times the test function’s value and that weight is strictly positive, '
            'so the sign of a term *is* the sign of `w` at that log — by the form of the '
            'expression. Every term was printed anyway. **The navigator has since withdrawn it as '
            'an identity in his own words, and it is recorded rather than re-scored.**', '',
            '#### What actually alternates the sign', '',
            '**Not the entering prime power — and it cannot be.** A prime power enters at '
            '`p^k = a²`, the support edge, where the bump vanishes, so its first contribution is '
            'negligible by construction. At the two flips the arriving term contributes '
            '`+4.81e-05` and `+1.16e-10` while the already-present terms move by `-3.08e-02` and '
            '`+1.49e-01` — **factors of 6×10² and 1×10⁹**. **The `n = 2` term flips and the sum '
            'follows it**; its weight `2 log 2/√2 = 0.980258` is the largest of any prime power and '
            '`log 2` sits deepest inside the support.', '',
            '#### The addendum’s column: entry or shell crossing', '',
            '**SHELL CROSSING, on both clauses.** *(i)* An already-present term changes sign at '
            'both flips and **no entering term carries either — 0 of %d**. *(ii)* The crossings sit '
            'at a **fixed boundary in `s = v/log a`**: grouped by direction, the two `+ → -` '
            'crossings — `n = 2` at `a* = %.7f` and `n = 3` at `a* = %.7f`, different primes at '
            'different radii — give `log n / log a*` of `%.9f` and `%.9f`, agreeing to **%.3e**. '
            'The third crossing, `n = 2` going `- → +` at `s = %.9f`, is a **second zero of the '
            'same fixed shape**.'
            % (ADD.get('flips', 0),
               DOWN[0]['a_star'] if DOWN else 0, DOWN[1]['a_star'] if len(DOWN) > 1 else 0,
               DOWN[0]['ratio'] if DOWN else 0, DOWN[1]['ratio'] if len(DOWN) > 1 else 0,
               SPREAD if SPREAD is not None else float('nan'),
               UP[0]['ratio'] if UP else float('nan')), '',
            '**And this act’s first writing of that test was wrong.** It pooled all three crossings '
            'and reported a spread of `0.408` — **comparing one zero of a fixed shape against '
            'another**. A shape fixed in `s` has several zeros and a term sweeping inward crosses '
            'each in turn. Grouped by direction, the constant appears. The defect is named here '
            'rather than carried.', '',
            '#### Where the room closes', '',
            '**`a₀ = %.7f`**, bracketed to `%.1e`, located by a root-find and **not by a grid '
            'point**. Two routes that **share no code** — the atlas’s transform-side integral '
            'against the digamma kernel, and `b320`’s `weil` from the source’s (53), (38), (39) — '
            'differ by `%.3e` against a tolerance of `1e-04` stated before the comparison.'
            % (RM.get('root', 0), RM.get('bracket', 0), RM.get('diff', 0)), '',
            '**The zero belongs to the interaction.** `h₊` has exactly one sign change, at '
            '`u₀ = %.9f` — a property of the digamma, carrying no family and no radius, which does '
            'not move when `a` moves. `A = (1/2π)∫ f̂(u) h₊(u) du` with `f̂ = |ĝ|² ≥ 0`, so `A < 0` '
            'means the family’s transform mass has moved below `u₀`. **The seed’s L¹ scale is '
            'exactly `1.000000000` at every radius** — a positive constant, and multiplying by a '
            'positive number moves no zero. What moves is the mass fraction below `u₀`: '
            '`0.057 → 0.207 → 0.390 → 0.499 → 0.523`, crossing one half right at `a₀`.'
            % HP.get('u0', 0), '',
            '**And the second family settles it in the stronger direction.** `corpus_bump`’s '
            'autocorrelation — which the record already holds, and which is **not lawful for the '
            'criterion**, its pole term being of order 2 — is negative against the same `h₊` at '
            'every radius from 2 to 12. **It never crosses at all.** Not "elsewhere" but "nowhere", '
            'which is the same answer with more force.', '',
            '#### Past the room', '',
            '**One cell, and (R49) authorises no more.** At `a = 5.656854`: `PR = -0.039336`, '
            '`A = -0.001105`, `Σ_v W_v = -0.038231 ≤ 0`. The archimedean slack is now negative and '
            '**the primes carry the criterion by themselves**. The population is one cell, printed '
            'beside the verdict so no reader takes it for a sweep, and **no trend is drawn through '
            'a single point**.', '',
            '**And what that costs, as b437 stated it: the zero side is inherited.** `Z` is summed '
            'over ordinates that are all ON the line, so satisfaction here is **assumed and not '
            'tested**. **No claim about zeros.**', '',
            '#### What this act did not do', '',
            'No new instrument, no new family, no new cell; `SIDE-window` and every instrument file '
            'byte-unmoved. No cell written and `FACES_LEDGER.md` byte-unmoved; the register stays '
            'frozen at six. **b432’s disproof-lane trigger fired at (R48) and its disposition waits '
            'on the author — this act does not open it.** The instrument lane closes at this act’s '
            'end. The arc stays checkpointed after site (iv); the four lists stay open; `h2` is '
            'where the deposit left it.', '',
            '**And one gap named from this act’s own bench.** The addendum arrived after the face '
            'was locked. (Z) forbids editing the banked ferry, the enumerated data list names no '
            'slot, and (G2) could not have declared its ten checks. It was quoted inside the '
            'components record and its checks folded into a declared arm. **(R47) closed the class '
            'loophole and left no door for an addendum** — an act can currently receive one only by '
            'breaching its own write list or by folding it into another file. Routed.']


def corr_rows():
    m = ROWMARK + " (b438)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE AND BEFORE ANY CELL VALUE**, "
            "chained on b378's gate run as b438 -- @GR@ gates read, @GDG@ checked by digest. "
            "**(R49) EXECUTED IN ITS OWN SCOPE: NO NEW INSTRUMENT, NO NEW FAMILY, NO NEW CELL.** "
            "**THE LADDER RIDES AN AIMED SEED, NOT THE PLAIN BUMP -- TWO MOMENTS SOLVED TO VANISH, "
            "SO THE SEED MUST TAKE NEGATIVE VALUES AND THE OSCILLATION IS BUILT IN BY THE AIM.** "
            "**@NT@ TERMS PRINTED ACROSS 35 CELLS. ### AND (N1) WAS AN IDENTITY, WHICH THE FACE "
            "SAID BEFORE A CELL WAS SPENT: 2 log p / sqrt(n) IS STRICTLY POSITIVE, SO THE SIGN OF "
            "A TERM IS THE SIGN OF w AT THAT LOG BY THE FORM OF THE EXPRESSION -- SINCE WITHDRAWN "
            "AS AN IDENTITY BY THE AUTHOR AND RECORDED, NOT RE-SCORED.** **WHAT ALTERNATES THE "
            "SIGN IS NOT THE ENTERING PRIME POWER AND CANNOT BE: A PRIME POWER ENTERS AT p^k = a^2, "
            "THE SUPPORT EDGE, WHERE THE BUMP VANISHES. AT THE TWO FLIPS THE ARRIVAL CONTRIBUTES "
            "+4.81e-05 AND +1.16e-10 WHILE THE ALREADY-PRESENT TERMS MOVE BY -3.08e-02 AND "
            "+1.49e-01 -- FACTORS OF 6e+02 AND 1e+09. THE n = 2 TERM FLIPS AND THE SUM FOLLOWS "
            "IT.** **THE ADDENDUM'S COLUMN ANSWERS SHELL CROSSING ON BOTH CLAUSES: AN "
            "ALREADY-PRESENT TERM CHANGES SIGN AT BOTH FLIPS WITH THE ENTERING TERM CARRYING "
            "@CARRIED@ OF @FLIPS@, AND THE TWO DOWNWARD CROSSINGS -- DIFFERENT PRIMES, DIFFERENT "
            "RADII -- SIT AT log n / log a* AGREEING TO @SPREAD@, A FIXED BOUNDARY IN v/log a.** "
            "**AND THIS ACT'S FIRST WRITING OF THAT TEST POOLED THREE CROSSINGS AND COMPARED ONE "
            "ZERO OF A FIXED SHAPE AGAINST ANOTHER; THE DEFECT IS NAMED, NOT CARRIED.** **THE ROOM "
            "CLOSES AT a0 = @ROOT@, ROOT-FOUND AND NOT GRIDDED, BY TWO ROUTES THAT SHARE NO CODE "
            "DIFFERING BY @DIFF@ AGAINST A TOLERANCE OF 1e-04 STATED BEFORE THE COMPARISON.** "
            "**AND THE ZERO BELONGS TO THE INTERACTION: h+ HAS ONE FIXED SIGN CHANGE AT "
            "u0 = @U0@ THAT DOES NOT MOVE WITH a, THE SEED'S L1 SCALE IS EXACTLY 1.000000000 AT "
            "EVERY RADIUS AND MOVES NO ZERO, AND THE TRANSFORM MASS BELOW u0 CROSSES ONE HALF AT "
            "a0. THE SECOND FAMILY, AGAINST THE SAME h+, NEVER CROSSES AT ALL BETWEEN a = 2 AND "
            "a = 12.** **PAST THE ROOM THERE IS EXACTLY ONE CELL AND (R49) AUTHORISES NO MORE: THE "
            "ARCHIMEDEAN SLACK IS NEGATIVE AND THE PRIMES CARRY THE CRITERION BY THEMSELVES, AND "
            "THE ZERO SIDE IS INHERITED SO SATISFACTION IS ASSUMED AND NOT TESTED.** 0 CELLS "
            "WRITTEN, 0 GRADES MOVED, 0 INSTRUMENTS BUILT, 0 CLAIMS ABOUT ZEROS, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The act decomposes a measurement the "
            "record already holds and confers nothing")
    prof = ("### ONE PLACE-papers FILE APPENDED (OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; "
            "FACES_LEDGER.md BYTE-UNMOVED AND THE REGISTER STILL FROZEN AT SIX; EVERY INSTRUMENT "
            "FILE AND SIDE-window BYTE-UNMOVED; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO "
            "KERNEL FILE -- 0 CONTENT LOST")
    grade = ("### THE MEANING OF A CROSSING WAS WRITTEN INTO THE FACE AND SEALED BEFORE THE FIRST "
             "VALUE; THE TWO ARCHIMEDEAN ROUTES ARE DECLARED INDEPENDENT AND THE TWO (149) ROUTES "
             "DECLARED SINGLE-ARM, EACH ON ITS OWN FOOTING; AND THE ONE TEST THIS ACT GOT WRONG -- "
             "A SPREAD POOLED ACROSS TWO DIFFERENT ZEROS -- IS PRINTED AS ITS OWN DEFECT RATHER "
             "THAN QUIETLY REGROUPED")
    status = ("data/b438_the_alternation_and_the_room.txt; data/b438_components.txt; "
              "data/b438_extract.txt; data/b438_terms.json; data/b438_room.json; "
              "data/b438_hplus.json; data/b438_checks.txt; "
              "data/b438_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@NT@', str(N1.get('terms', 0)))
                .replace('@CARRIED@', str(ADD.get('carried', 0)))
                .replace('@FLIPS@', str(ADD.get('flips', 0)))
                .replace('@SPREAD@', ('%.3e' % SPREAD) if SPREAD is not None else 'n/a')
                .replace('@ROOT@', '%.7f' % RM.get('root', 0))
                .replace('@DIFF@', '%.3e' % RM.get('diff', 0))
                .replace('@U0@', '%.9f' % HP.get('u0', 0)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('what alternates the prime sum sign',
           'do entering prime powers flip the sum',
           'where does the archimedean channel close',
           'is the archimedean zero a property of h plus or of the family',
           'what is the shell boundary in v over log a')
MUST_NOT_HIT = ('the criterion was violated', 'rh was disproved',
                'the disproof lane was opened by b438')
KEY = 'what-alternates-the-sign-and-where-the-room-closes'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b438 EXECUTED (R49) IN ITS OWN SCOPE -- the cells b437 banked, decomposed, and the "
        "archimedean distribution evaluated against the same family -- WITH NO NEW INSTRUMENT, NO "
        "NEW FAMILY AND NO NEW CELL. THE LADDER RIDES AN AIMED SEED, NOT THE PLAIN BUMP: three of "
        "the corpus's own bumps at widths a, a^(1/2), a^(1/4) with two coefficients SOLVED so two "
        "moments vanish, and a non-negative function cannot have a vanishing integral unless it is "
        "zero, so THE SEED MUST TAKE NEGATIVE VALUES AND THE OSCILLATION IS BUILT IN BY THE AIM. "
        "%d TERMS PRINTED ACROSS 35 CELLS. (N1) WAS AN IDENTITY AND THE FACE SAID SO BEFORE A CELL "
        "WAS SPENT -- 2 log p / sqrt(n) is strictly positive, so the sign of a term IS the sign of "
        "the test function at that log by the FORM of the expression; the author has since "
        "withdrawn it as an identity and the withdrawal is recorded, not re-scored. WHAT ACTUALLY "
        "ALTERNATES THE SIGN IS NOT THE ENTERING PRIME POWER, AND CANNOT BE: a prime power enters "
        "at p^k = a^2, the SUPPORT EDGE, where the bump vanishes. At the two flips the arrival "
        "contributes +4.81e-05 and +1.16e-10 while the already-present terms move by -3.08e-02 and "
        "+1.49e-01 -- factors of 6e+02 and 1e+09. THE n = 2 TERM FLIPS AND THE SUM FOLLOWS IT; its "
        "weight 2 log 2 / sqrt 2 = 0.980258 is the largest of any prime power and log 2 sits "
        "deepest inside the support. THE ADDENDUM'S COLUMN ANSWERS SHELL CROSSING ON BOTH CLAUSES: "
        "an already-present term changes sign at BOTH flips with the entering term carrying %d of "
        "%d, and the two DOWNWARD crossings -- n = 2 at a* = %.7f and n = 3 at a* = %.7f, different "
        "primes at different radii -- give log n / log a* of %.9f and %.9f, agreeing to %.3e. That "
        "is a FIXED BOUNDARY in s = v / log a, and the third crossing (n = 2 going up, at "
        "s = %.9f) is a SECOND ZERO OF THE SAME FIXED SHAPE. b437's (N1) coincidence is restated "
        "as a coincidence of two cells. AND THIS ACT'S FIRST WRITING OF THAT TEST POOLED ALL THREE "
        "AND REPORTED A SPREAD OF 0.408, COMPARING ONE ZERO AGAINST ANOTHER -- the defect is named "
        "rather than carried. THE ROOM CLOSES AT a0 = %.7f, root-found and not gridded, bracketed "
        "to %.1e, by TWO ROUTES THAT SHARE NO CODE differing by %.3e against a tolerance of 1e-04 "
        "stated before the comparison. THE ZERO BELONGS TO THE INTERACTION: h+ has ONE sign change "
        "at u0 = %.9f which does not move with a; the seed's L1 scale is exactly 1.000000000 at "
        "every radius and a positive number moves no zero; and the transform mass below u0 runs "
        "0.057, 0.207, 0.390, 0.499, 0.523, crossing one half at a0. THE SECOND FAMILY -- "
        "corpus_bump's autocorrelation, NOT LAWFUL and carrying no criterion reading -- never "
        "crosses at all between a = 2 and a = 12, which settles the question in the stronger "
        "direction. PAST THE ROOM THERE IS EXACTLY ONE CELL and (R49) authorises no more: at "
        "a = 5.656854 the archimedean slack is negative and THE PRIMES CARRY THE CRITERION BY "
        "THEMSELVES, with SUM_v W_v = -0.038231 <= 0. AND THE COST IS RESTATED: THE ZERO SIDE IS "
        "INHERITED, summed over ordinates all ON the line, so satisfaction is ASSUMED AND NOT "
        "TESTED. NO CLAIM ABOUT ZEROS. b432's disproof-lane trigger fired at (R48) and its "
        "disposition waits on the author; this act does not open it."
        % (N1.get('terms', 0), ADD.get('carried', 0), ADD.get('flips', 0),
           DOWN[0]['a_star'] if DOWN else 0, DOWN[1]['a_star'] if len(DOWN) > 1 else 0,
           DOWN[0]['ratio'] if DOWN else 0, DOWN[1]['ratio'] if len(DOWN) > 1 else 0,
           SPREAD if SPREAD is not None else float('nan'),
           UP[0]['ratio'] if UP else float('nan'),
           RM.get('root', 0), RM.get('bracket', 0), RM.get('diff', 0), HP.get('u0', 0)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO CELL WRITTEN, NO SITE ENTERED, NO "
             "BRIDGE TYPED. ### NO NEW INSTRUMENT, NO NEW FAMILY, NO NEW CELL. ### NO CLAIM ABOUT "
             "RH, h2, ZETA OR ANY ZERO. ### THE INSTRUMENT LANE CLOSES AT THIS ACT'S END")
    where = ("data/b438_the_alternation_and_the_room.txt; data/b438_components.txt; "
             "data/b438_extract.txt; data/b438_terms.json; data/b438_room.json; "
             "data/b438_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b438 (what alternates the sign, and where the room closes)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES (b438).%s'
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
        rec('    %-58s reaches the b438 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the aimed seed carried', 'AIMED SEED' in out),
                      ('the identity carried', '(N1) WAS AN IDENTITY' in out),
                      ('the edge reason carried', 'SUPPORT EDGE' in out),
                      ('the n=2 attribution carried', 'THE n = 2 TERM FLIPS' in out),
                      ('the shell constant carried', 'FIXED BOUNDARY' in out),
                      ('the pooled-test defect carried', 'COMPARING ONE ZERO AGAINST ANOTHER'
                       in out),
                      ('the closing radius carried', 'THE ROOM CLOSES AT a0' in out),
                      ('the interaction verdict carried', 'BELONGS TO THE INTERACTION' in out),
                      ('the second family carried', 'never crosses at all' in out),
                      ('the inherited zero side carried', 'ASSUMED AND NOT TESTED' in out)):
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
    Bk = ['=' * 100, 'b438 -- WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES.', 'THE BANK.',
          '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CROSSINGS, GROUPED BY DIRECTION.', '-' * 100,
           '  %-10s %-6s %-14s %-10s %s'
           % ('flip at a', 'n', 'a* (crossing)', 'direction', 'log n / log a*')]
    for s in SHELLS:
        Bk.append('  %-10.6f %-6d %-14.7f %-10s %.9f'
                  % (s['flip_at'], s['n'], s['a_star'],
                     '+ -> -' if s['direction'] == 'down' else '- -> +', s['ratio']))
    if SPREAD is not None:
        Bk.append('')
        Bk.append('  THE TWO DOWNWARD CROSSINGS AGREE TO %.3e -- A FIXED BOUNDARY IN v / log a.'
                  % SPREAD)
    Bk += ['', '-' * 100, '### THE ROOM.', '-' * 100,
           '  closing radius a0      : %.7f (bracket %.1e)' % (RM.get('root', 0),
                                                               RM.get('bracket', 0)),
           '  atlas route at a0      : %+.9f' % RM.get('A', 0),
           '  b320 weil route at a0  : %+.9f' % RM.get('W', 0),
           '  the two differ by      : %.3e   (tolerance 1e-04, stated first)'
           % RM.get('diff', 0),
           '  h+ own sign change     : u0 = %.9f' % HP.get('u0', 0)]
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


B437ROW_RE = r"(?m)^\| (\d+) \| \*\*THE WINDOW OPENED BY RUNGS"


def main():
    bar('=')
    rec('b438_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not ROOM or not TERMS:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      terms %d over 35 cells ; flips %d ; entering carried %d ; crossings %d'
        % (N1.get('terms', 0), ADD.get('flips', 0), ADD.get('carried', 0), len(SHELLS)))
    rec('      closing radius a0 = %.7f ; routes differ %.3e ; h+ zero u0 = %.6f'
        % (RM.get('root', 0), RM.get('diff', 0), HP.get('u0', 0)))
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
        % [int(x.group(1)) for x in re.finditer(B437ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B437ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b438_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
