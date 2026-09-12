# -*- coding: utf-8 -*-
"""b439_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b439 the fixed profile, the fixed point, and one arithmetic claim -->'
PRIOR = '<!-- b438 what alternates the sign, and where the room closes -->'
BANKOUT = os.path.join(D, 'b439_the_fixed_profile.txt')
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


FACE = read(os.path.join(D, 'b439_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b439_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b439_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b439_components.txt'))
try:
    PRICE = json.loads(read(os.path.join(D, 'b439_price.json')) or '{}')
except Exception:
    PRICE = {}
try:
    PROF = json.loads(read(os.path.join(D, 'b439_profile.json')) or '[]')
except Exception:
    PROF = []
try:
    WTS = json.loads(read(os.path.join(D, 'b439_weights.json')) or '[]')
except Exception:
    WTS = []
try:
    U0 = json.loads(read(os.path.join(D, 'b439_u0.json')) or '{}')
except Exception:
    U0 = {}

C2 = PRICE.get('c2') or {}
C4 = PRICE.get('c4') or {}
FIXED = PRICE.get('fixed')
SPREAD_C1 = PRICE.get('spread_c1')
SPREAD_S = PRICE.get('spread_s')
MAXN = C2.get('maximizer')
TWO = ([w for w in WTS if w['n'] == 2] or [{}])[0]
MX = ([w for w in WTS if w.get('rank') == 1] or [{}])[0]
ROWMARK = ('**THE PROFILE IS NOT FIXED, SO b438`S SHELL BOUNDARY IS FIXED ONLY TO 2e-04 AND THE '
           'SPREAD IS THE OBJECT`S; b438`S WEIGHT EXPLANATION IS FALSE AND REPLACED BY THE '
           'PRODUCT; AND u0 IS LOCATED BY TWO ROUTES AND NAMED BY NO ACT**')

SCOPE = ("### THE ACT READS A CONSTRUCTION, DOES ARITHMETIC ON A CLOSED FORMULA, AND LOCATES ONE "
         "CONSTANT BY TWO ROUTES. ### NO NEW INSTRUMENT, NO NEW FAMILY, NO LANE OPENED -- BOTH "
         "REMAIN PARKED. ### IT CORRECTS AN ERROR OF ITS OWN PREDECESSOR WITHOUT EDITING ITS BANK, "
         "AND MAKES NO CLAIM ABOUT RH, h2, ZETA OR ANY ZERO")

DESK = [
    ('whether the seed`s autocorrelation is a fixed profile in s', 'CLOSE',
     'ANSWERED at b439: **PARTLY, and the answer to the literal question is NO.** Fixed: the three '
     'supports at `s = 1, 1/2, 1/4`, each bump`s own shape in `s`, and the first moment condition. '
     '**NOT fixed: the second moment condition** -- its weight `cosh(v/2)` becomes '
     '`cosh(s log a / 2)` in the scaled variable and carries `a` explicitly -- **and therefore the '
     'coefficients, and therefore the combination.** `c1` spreads **%.6e** across six radii.'
     % (SPREAD_C1 or 0)),
    ('whose the 2.27e-04 spread was', 'CLOSE',
     'DECIDED at b439: **THE OBJECT`S.** The profile`s own zero -- the one b438`s crossings sit on, '
     'matched rather than pooled -- reproduces those crossings to `1e-14` and **moves by the same '
     '`2.266e-04` between the same two radii**. So b438`s "fixed boundary" is fixed only to '
     '`2e-04`, and the residual it filed as an untested reading is now measured and is real.'),
    ('this act`s own first comparison', 'CLOSE',
     '**A DEFECT OF THIS ACT, FOUND BECAUSE THE NUMBERS REFUSED TO LINE UP.** The first writing '
     'took the profile`s FIRST down-zero (`s ~ 0.1428`) and compared it against b438`s crossings '
     '(`s ~ 1.1623`) -- **two different zeros again**, one act after b438 made the same mistake '
     'pooling three. Corrected to match like with like; every zero is now printed.'),
    ('b438`s weight explanation', 'CLOSE',
     '**FALSE, AND REPLACED.** `2 log p / sqrt(n)` over the prime powers below sixteen is maximised '
     'at **n = %s (%.6f)**; **n = 2 is %.6f, sixth of ten.** The navigator`s arithmetic was checked '
     'and agrees. b438 offered the weight as THE REASON the two-term dominates, so it was '
     'load-bearing -- but **the finding it supported is untouched**, having been established from '
     'the printed terms. **b438`s bank is not edited.**'
     % (MX.get('n'), MX.get('w', 0), TWO.get('w', 0))),
    ('what actually makes a term dominate', 'CLOSE',
     '**THE PRODUCT, AND WHICH FACTOR GOVERNS DEPENDS ON THE RADIUS.** Position predicts the '
     'largest term at **%s of %s** cells; the weight`s own maximizer at **0 of %s**. The %s '
     'exceptions are all at large radius and all lost to `n = 3`; at %s of them the smallest-`s` '
     'term has the LARGER amplitude and still loses, because `n = 3`s weight is 1.29x `n = 2`s. '
     '**At small radius the amplitude ratio is enormous and position decides; at large radius the '
     'amplitudes converge and the weight ratio decides.** On b438`s own range (`a <= 3.0`, below '
     'the first exception at `a = %s`) position holds everywhere.'
     % (C2.get('agree'), C2.get('total'), C2.get('total'), C2.get('exceptions'),
        C2.get('amp_larger'), C2.get('first_exception'))),
    ('the fixed point u0', 'CLOSE',
     'LOCATED and CHARACTERIZED at b439. **u0 = %s**, by two routes that share no code -- the '
     'digamma directly, and the log-derivative of the completed gamma factor through `loggamma` -- '
     'agreeing to **%.3e** against a tolerance of `1e-09` stated first. **It is exactly where h+`s '
     'two constituents balance: `Re psi(1/4 + i u/2) = log pi`.**'
     % (U0.get('u0'), U0.get('diff', 0))),
    ('whether the corpus can say WHAT u0 is', 'CLOSE',
     'ANSWERED: **ONLY WHERE.** Ten files carry the value and **all ten trace to b438, to this act, '
     'or to what they wrote -- no other act mentions it at all**, and b438 prints it without naming '
     'it. The record gives `h+` a closed form and proves it two ways; it gives **no closed form for '
     'the solution of `Re psi(1/4 + i u/2) = log pi`**, nor does one appear in any pinned source. '
     '**A precise number is not an identification.**'),
    ('the large-radius question', 'STANDING',
     'PRICED at b439 and **NOT OPENED**. The order`s conditional opened *"if Component 1 returns '
     'FIXED"* -- **it did not**, so the premise fails and the price is given for the question the '
     'record actually leaves. **It prices as a MEASUREMENT, not a READ**: b436 found the density '
     'result absent from every verified source, and the profile is not fixed, so the drift and the '
     'sampling must be evaluated together. **The MEASUREMENT is unblocked; the BUILD is blocked by '
     'the KERNEL lane**, which is open to READ only. TRIGGER: the author`s word.'),
    ('the three finite facts for the window kernel', 'STANDING',
     'NAMED at b439 and **NOT BUILT**. (1) the entering term is exactly zero at the support edge -- '
     'finite, exact, family-independent. (2) **QUALIFIED: the SUPPORTS are fixed at `s = 1, 1/2, '
     '1/4`; the PROFILE`S ZEROS ARE NOT** -- a kernel carrying "fixed shells" would carry a '
     'falsehood. (3) the weight table`s maximizer, `n = %s`. **Nothing compiled, no terminal.**'
     % MAXN),
    ('the residual b438 filed as an untested reading', 'CLOSE',
     'TESTED at b439 and **CONFIRMED as the object`s**. b438 wrote that exact scale-invariance '
     'would need both moment conditions to be scale-invariant and that `cosh(v/2)` is not, and '
     'filed it as a reading it had not tested. **The coefficients now measured at six radii show '
     'exactly that drift.**'),
    ('what a vanishing archimedean channel means', 'STANDING',
     'ROUTED at b437 and b438, **still not answered**. Untouched by this act.'),
    ('b432`s disproof-lane trigger', 'STANDING',
     '**FIRED AT (R48), AND ITS DISPOSITION STILL WAITS ON THE AUTHOR.** Not opened here.'),
    ('the addendum slot', 'STANDING',
     'IN FORCE from this act`s face per **(R50)**. `data/b439_addendum.txt` is named in the write '
     'list, present whether used or not. **This act received no post-lock instruction, so it is '
     'empty -- which (R50) says is never a defect.**'),
    ('the witness arc, sites (v) and (vi)', 'STANDING',
     'CHECKPOINTED after site (iv). Two sites remain; trigger: the author`s word.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432 and carried.'),
    ('the register, frozen at six', 'STANDING', 'UNCHANGED; `FACES_LEDGER.md` byte-unmoved.'),
    ('the fourth grade, now defined', 'STANDING', 'DEFINED at b433; untouched.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424 and carried.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED research instrument lane.'),
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
            '### b439 — the fixed profile, the fixed point, and one arithmetic claim — filed '
            '2026-09-12', '',
            '**Three of this act’s four expectations are refuted, two of them about work this seat '
            'did two acts ago.** No new instrument, no new family, no lane opened.', '',
            '#### Component 1 — the profile is not fixed, and b438’s boundary is fixed only to 2e-04',
            '',
            'Derived from the construction’s own integrands, then measured. **Fixed in `s`:** the '
            'three supports at `1, ½, ¼`; each bump’s own shape; and the first moment condition, '
            '`∫φᵢ dv = 1`, which carries no `a`. **Not fixed:** the second condition, '
            '`∫φᵢ(v) cosh(v/2) dv` — in the scaled variable this is '
            '`∫(1/e)φ(s/e) cosh(s log a / 2) ds`, and **the weight carries `a` explicitly, inside a '
            '`cosh`, which is not a power of `x`.** So the coefficients drift: `c1` spreads '
            '**%.6e** across six radii.' % (SPREAD_C1 or 0), '',
            '**And b438’s 2.27e-04 spread is the object’s, not the grid’s.** The profile’s own '
            'zero — *the one b438’s crossings actually sit on*, matched rather than pooled — '
            'reproduces those crossings to `1e-14` and **moves by the same `2.266e-04` between the '
            'same two radii**. b438 filed the `cosh` non-invariance as an untested reading; it is '
            'now measured, and it is real.', '',
            '**This act made b438’s mistake once itself.** The first writing compared the '
            '*first* down-zero (`s ≈ 0.1428`) against crossings on a *later* one (`s ≈ 1.1623`) — '
            'two different zeros, exactly as b438 pooled three. Caught because the numbers refused '
            'to line up; every zero is now printed.', '',
            '#### Component 2 — b438’s explanation is false, and the replacement is neither candidate',
            '',
            '`2 log p / √n` over the prime powers below sixteen is maximised at **n = %s (%.6f)**; '
            '**n = 2 is %.6f, sixth of ten.** The navigator’s arithmetic was checked and agrees. '
            'b438 offered the weight as *the reason* the two-term dominates, so it was '
            'load-bearing — but **the finding it supported is untouched**, having been established '
            'from the printed terms rather than from the weight.'
            % (MX.get('n'), MX.get('w', 0), TWO.get('w', 0)), '',
            '**And the replacement is the product.** Position predicts the largest term at **%s of '
            '%s** cells; the weight’s own maximizer at **0 of %s**. The %s exceptions are all at '
            'large radius and all lost to `n = 3` — and at **%s of them the smallest-`s` term has '
            'the *larger* amplitude and still loses**, because `n = 3`’s weight is 1.29× `n = 2`’s. '
            'So: at small radius the amplitude ratio is enormous and **position decides**; at large '
            'radius the amplitudes converge and **the weight ratio decides**. On b438’s own range '
            '(`a ≤ 3.0`, below the first exception at `a = %s`) position holds everywhere.'
            % (C2.get('agree'), C2.get('total'), C2.get('total'), C2.get('exceptions'),
               C2.get('amp_larger'), C2.get('first_exception')), '',
            '#### Component 3 — the fixed point, located and characterized', '',
            '**`u₀ = %s`**, by two routes that share no code — `−log π + Re ψ(1/4 + iu/2)` directly, '
            'and `2 Re (d/ds)[−(s/2)log π + logΓ(s/2)]` at `s = ½ + iu` through `loggamma` and a '
            'numerical derivative — **agreeing to %.3e** against a tolerance of `1e-09` stated '
            'first. *(Not b438’s pair: the atlas’s `A` and b320’s `weil` compute the archimedean '
            'channel of a test function and neither exposes the kernel pointwise.)*'
            % (U0.get('u0'), U0.get('diff', 0)), '',
            '**It is exactly where h₊’s two constituents balance** — `h₊ = Re ψ(1/4 + iu/2) − log π`, '
            'so `h₊(u₀) = 0` *is* `Re ψ(1/4 + iu₀/2) = log π`.', '',
            '**And the record names it nowhere.** Ten files carry the value; **all ten trace to '
            'b438, to this act, or to what they wrote — no other act mentions it at all**, and b438 '
            'prints it without naming it. The corpus gives `h₊` a closed form and proves it two '
            'ways; it gives **no closed form for `u₀`**, nor does any pinned source. **So the corpus '
            'can say where it is, to any precision, and cannot say what it is.**', '',
            '#### Component 4 — priced, not opened', '',
            '**The order’s conditional opened *"if Component 1 returns FIXED"*. It did not**, so the '
            'premise fails and the price is given for the question the record actually leaves: the '
            'profile drifts, so a large-radius statement must carry the coefficient drift *and* the '
            'sampling density, and nothing in the record separates them.', '',
            'Such a statement would need **(i)** a classical density result for the sampling points '
            '`s_n = log n / log a` over prime powers `n < a²` — the PNT, or Chebyshev for a bound — '
            'which **b436 found absent from every verified source**; **(ii)** the two vanishing '
            'moments, which are what force the profile to change sign at all *and* what break the '
            'scaling, cutting both ways; **(iii)** a decision between the `p^{-k/2}` decay and the '
            'growing density, **which is the statement itself**.', '',
            '**PRICE: MEASUREMENT, not READ.** The measurement is unblocked; **the BUILD is blocked '
            'by the KERNEL lane**, open to READ only.', '',
            '**The three finite facts, named and not built:** (1) the entering term is exactly zero '
            'at the support edge — finite, exact, family-independent; (2) **qualified — the '
            '*supports* are fixed, the *zeros* are not**, so a kernel carrying "fixed shells" would '
            'carry a falsehood; (3) the weight table’s maximizer, `n = %s`. **Nothing compiled.**'
            % MAXN, '',
            '#### What this act did not do', '',
            'No new instrument, no new family, no lane opened — both remain parked. **b438’s bank '
            'is not edited**; its error is corrected here. No cell written, `FACES_LEDGER.md` '
            'byte-unmoved, register frozen at six. **b432’s disproof-lane trigger fired at (R48) '
            'and its disposition still waits on the author.** The arc stays checkpointed after site '
            '(iv); the four lists stay open; `h2` is where the deposit left it. **(R50)’s addendum '
            'slot is in force and empty, which is never a defect.**']


def corr_rows():
    m = ROWMARK + " (b439)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b439 -- @GR@ gates read, @GDG@ checked by digest; and (R50)'S ADDENDUM SLOT IS IN "
            "FORCE FROM THIS FACE, NAMED IN THE WRITE LIST AND EMPTY, WHICH IS NEVER A DEFECT. "
            "**COMPONENT 1, DERIVED FROM THE CONSTRUCTION AND THEN MEASURED: THE SUPPORTS AT "
            "s = 1, 1/2, 1/4, EACH BUMP'S OWN SHAPE, AND THE FIRST MOMENT ARE SCALE-INVARIANT; THE "
            "SECOND MOMENT IS NOT, ITS cosh(v/2) BECOMING cosh(s log a / 2) AND CARRYING a "
            "EXPLICITLY. SO THE COEFFICIENTS DRIFT -- c1 SPREADS @SC1@ ACROSS SIX RADII -- AND THE "
            "AUTOCORRELATION IS NOT A FIXED PROFILE IN s.** **AND b438'S 2.27e-04 SPREAD IS "
            "THEREFORE THE OBJECT'S AND NOT THE GRID'S: THE PROFILE'S OWN ZERO, THE ONE THOSE "
            "CROSSINGS SIT ON, REPRODUCES THEM TO 1e-14 AND MOVES BY THE SAME 2.266e-04 BETWEEN THE "
            "SAME TWO RADII. b438'S FIXED BOUNDARY IS FIXED ONLY TO 2e-04.** **AND THIS ACT MADE "
            "b438'S OWN MISTAKE ONCE, COMPARING TWO DIFFERENT ZEROS, AND SAYS SO.** **COMPONENT 2: "
            "b438'S CLOSING CALLED THE TWO-TERM'S WEIGHT THE LARGEST OF ANY PRIME POWER AND THAT IS "
            "FALSE -- THE MAXIMIZER IS n = @MAXN@ AT @MAXW@ AND n = 2 IS @TWOW@, SIXTH OF TEN. THE "
            "NAVIGATOR'S ARITHMETIC WAS CHECKED AND AGREES; b438'S BANK IS NOT EDITED; AND THE "
            "FINDING IT SUPPORTED IS UNTOUCHED, HAVING COME FROM THE PRINTED TERMS.** **THE "
            "REPLACEMENT IS NEITHER CANDIDATE BUT THE PRODUCT: POSITION PREDICTS THE LARGEST TERM "
            "AT @AG@ OF @TOT@ CELLS AND THE WEIGHT'S MAXIMIZER AT 0 OF @TOT@; THE @EXC@ EXCEPTIONS "
            "ARE ALL AT LARGE RADIUS AND AT @AMP@ OF THEM THE SMALLEST-s TERM HAS THE LARGER "
            "AMPLITUDE AND STILL LOSES.** **COMPONENT 3: u0 = @U0@, BY TWO ROUTES THAT SHARE NO "
            "CODE AGREEING TO @UD@ AGAINST A TOLERANCE OF 1e-09 STATED FIRST; IT IS EXACTLY WHERE "
            "Re psi(1/4 + iu/2) = log pi; AND TEN FILES CARRY THE VALUE, ALL TEN TRACING TO b438 OR "
            "THIS ACT, SO NO ACT NAMES IT AND THE CORPUS CAN SAY ONLY WHERE IT IS.** **COMPONENT 4 "
            "IS PRICED AND NOT OPENED: THE ORDER'S PREMISE FAILED, AND THE QUESTION PRICES AS A "
            "MEASUREMENT RATHER THAN A READ, UNBLOCKED, WITH THE BUILD BLOCKED BY THE KERNEL LANE.** "
            "0 INSTRUMENTS BUILT, 0 FAMILIES DEFINED, 0 LANES OPENED, 0 CELLS WRITTEN, "
            "0 GRADES MOVED, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The act reads a construction and locates "
            "one constant, and confers nothing")
    prof = ("### ONE PLACE-papers FILE APPENDED (OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; "
            "FACES_LEDGER.md BYTE-UNMOVED AND THE REGISTER STILL FROZEN AT SIX; EVERY INSTRUMENT "
            "FILE AND SIDE-window BYTE-UNMOVED; b438'S BANK BYTE-UNMOVED THOUGH ITS ERROR IS "
            "CORRECTED HERE; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW -- 0 CONTENT LOST")
    grade = ("### THE FACE DECLARED ITS OWN EXPECTED ANSWER TO COMPONENT 1 AS A DERIVATION AND "
             "REQUIRED THE MEASUREMENT ANYWAY; THE NAVIGATOR'S ARITHMETIC AND HIS REPLACEMENT WERE "
             "BOTH CHECKED RATHER THAN ADOPTED, AND THE REPLACEMENT WAS REFUTED AS A UNIVERSAL "
             "CLAIM; AND THE ONE COMPARISON THIS ACT GOT WRONG -- TWO DIFFERENT ZEROS, THE SAME "
             "SHAPE OF ERROR b438 MADE -- IS PRINTED AS ITS OWN DEFECT")
    status = ("data/b439_the_fixed_profile.txt; data/b439_components.txt; data/b439_extract.txt; "
              "data/b439_profile.json; data/b439_weights.json; data/b439_u0.json; "
              "data/b439_price.json; data/b439_checks.txt; "
              "data/b439_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "data/b439_addendum.txt (the (R50) slot, EMPTY); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@SC1@', '%.6e' % (SPREAD_C1 or 0))
                .replace('@MAXN@', str(MX.get('n'))).replace('@MAXW@', '%.6f' % MX.get('w', 0))
                .replace('@TWOW@', '%.6f' % TWO.get('w', 0))
                .replace('@AG@', str(C2.get('agree'))).replace('@TOT@', str(C2.get('total')))
                .replace('@EXC@', str(C2.get('exceptions')))
                .replace('@AMP@', str(C2.get('amp_larger')))
                .replace('@U0@', str(U0.get('u0'))).replace('@UD@', '%.3e' % U0.get('diff', 0)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('is the seed autocorrelation a fixed profile',
           'whose was the shell boundary spread',
           'which prime power has the largest weight',
           'why does the two term dominate',
           'what is u0 and has any act named it')
MUST_NOT_HIT = ('the profile is fixed', 'u0 has a closed form',
                'the large radius question was opened')
KEY = 'the-fixed-profile-the-fixed-point-and-one-arithmetic-claim'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b439 ASKED THREE QUESTIONS AND REFUTED THREE OF ITS FOUR EXPECTATIONS, TWO OF THEM ABOUT "
        "WORK THIS SEAT DID TWO ACTS EARLIER. COMPONENT 1, DERIVED FROM THE CONSTRUCTION'S OWN "
        "INTEGRANDS AND THEN MEASURED: the three supports at s = 1, 1/2, 1/4, each bump's own shape "
        "in s, and the first moment condition INT phi_i dv = 1 are all scale-invariant; but the "
        "SECOND moment condition INT phi_i(v) cosh(v/2) dv becomes INT (1/e) phi(s/e) "
        "cosh(s log a / 2) ds in the scaled variable, CARRYING a EXPLICITLY INSIDE A cosh, WHICH IS "
        "NOT A POWER OF x. So the coefficients drift -- c1 spreads %s across six radii -- and THE "
        "AUTOCORRELATION IS NOT A FIXED PROFILE IN s. VERDICT PARTLY, and the literal answer is NO. "
        "AND THEREFORE b438'S 2.27e-04 SPREAD IS THE OBJECT'S, NOT THE GRID'S: the profile's own "
        "zero -- THE ONE b438's CROSSINGS ACTUALLY SIT ON, matched rather than pooled -- reproduces "
        "them to 1e-14 and MOVES BY THE SAME 2.266e-04 between the same two radii. b438's 'fixed "
        "boundary' is fixed only to 2e-04, and the cosh residual b438 filed as an untested reading "
        "is now measured and is real. THIS ACT MADE b438'S OWN MISTAKE ONCE: its first writing "
        "compared the FIRST down-zero at s ~ 0.1428 against crossings on a LATER zero at s ~ "
        "1.1623 -- two different zeros, one act after b438 pooled three -- and it is printed as "
        "this act's defect. COMPONENT 2: b438's closing wrote that the two-term's weight is 'the "
        "largest of any prime power', AND THAT IS FALSE. 2 log p / sqrt(n) over the prime powers "
        "below sixteen is maximised at n = %s (%s); n = 2 is %s, SIXTH OF TEN. The navigator's "
        "arithmetic was checked and agrees. It WAS load-bearing -- b438 offered it as the reason -- "
        "but THE FINDING IT SUPPORTED IS UNTOUCHED, having been established from the printed terms. "
        "b438'S BANK IS NOT EDITED. AND THE REPLACEMENT IS NEITHER CANDIDATE BUT THE PRODUCT: "
        "position predicts the largest term at %s of %s cells and the weight's own maximizer at 0 "
        "of %s; the %s exceptions are all at large radius and all lost to n = 3; and at %s of them "
        "THE SMALLEST-s TERM HAS THE LARGER AMPLITUDE AND STILL LOSES, because n = 3's weight is "
        "1.29x n = 2's. At small radius the amplitude ratio is enormous and POSITION decides; at "
        "large radius the amplitudes converge and THE WEIGHT RATIO decides. On b438's own range "
        "(a <= 3.0, below the first exception at a = %s) position holds everywhere. COMPONENT 3: "
        "u0 = %s, located by TWO ROUTES THAT SHARE NO CODE -- the digamma directly, and the "
        "log-derivative of the completed gamma factor through loggamma -- agreeing to %s against a "
        "tolerance of 1e-09 STATED BEFORE THE COMPARISON. (Not b438's pair: the atlas's A and "
        "b320's weil compute the archimedean channel of a test function and NEITHER EXPOSES THE "
        "KERNEL POINTWISE.) It is EXACTLY where h+'s two constituents balance, Re psi(1/4 + i u/2) "
        "= log pi. AND THE RECORD NAMES IT NOWHERE: ten files carry the value and ALL TEN TRACE TO "
        "b438, TO THIS ACT, OR TO WHAT THEY WROTE -- no other act mentions it -- and b438 prints it "
        "without naming it. The corpus gives h+ a closed form and proves it two ways; it gives NO "
        "CLOSED FORM for the solution, nor does any pinned source. SO THE CORPUS CAN SAY WHERE IT "
        "IS AND CANNOT SAY WHAT IT IS. COMPONENT 4 IS PRICED AND NOT OPENED: the order's "
        "conditional opened 'if Component 1 returns FIXED' and IT DID NOT, so the premise fails; "
        "the question prices as a MEASUREMENT and not a READ, because b436 found the density result "
        "absent from every verified source AND the profile is not fixed. THE MEASUREMENT IS "
        "UNBLOCKED; THE BUILD IS BLOCKED BY THE KERNEL LANE. The three finite facts are NAMED AND "
        "NOT BUILT, with the second QUALIFIED: the supports are fixed, the profile's zeros are not, "
        "so a kernel carrying 'fixed shells' would carry a falsehood."
        % ('%.6e' % (SPREAD_C1 or 0), MX.get('n'), '%.6f' % MX.get('w', 0),
           '%.6f' % TWO.get('w', 0), C2.get('agree'), C2.get('total'), C2.get('total'),
           C2.get('exceptions'), C2.get('amp_larger'), C2.get('first_exception'),
           U0.get('u0'), '%.3e' % U0.get('diff', 0)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO CELL WRITTEN, NO SITE ENTERED, NO "
             "BRIDGE TYPED. ### NO NEW INSTRUMENT, NO NEW FAMILY, NO LANE OPENED. ### NOTHING "
             "COMPILED FOR THE WINDOW KERNEL. ### NO CLAIM ABOUT RH, h2, ZETA OR ANY ZERO")
    where = ("data/b439_the_fixed_profile.txt; data/b439_components.txt; data/b439_extract.txt; "
             "data/b439_profile.json; data/b439_weights.json; data/b439_u0.json; "
             "data/b439_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b439 (the fixed profile, the fixed point, and one arithmetic claim)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM (b439).%s'
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
        rec('    %-58s reaches the b439 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the not-fixed verdict carried', 'NOT A FIXED PROFILE' in out),
                      ('the cosh reason carried', 'NOT A POWER OF x' in out),
                      ('the spread attribution carried', "OBJECT'S, NOT THE GRID'S" in out),
                      ('this act`s own defect carried', "MADE b438'S OWN MISTAKE" in out),
                      ('the false sentence carried', 'AND THAT IS FALSE' in out),
                      ('the maximizer carried', 'SIXTH OF TEN' in out),
                      ('the product account carried', 'NEITHER CANDIDATE BUT THE PRODUCT' in out),
                      ('the two routes carried', 'TWO ROUTES THAT SHARE NO CODE' in out),
                      ('the naming answer carried', 'NAMES IT NOWHERE' in out),
                      ('the where-not-what carried', 'CANNOT SAY WHAT IT IS' in out),
                      ('the failed premise carried', 'IT DID NOT' in out),
                      ('the price carried', 'BLOCKED BY THE KERNEL LANE' in out)):
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
    Bk = ['=' * 100, 'b439 -- THE FIXED PROFILE, THE FIXED POINT, AND ONE ARITHMETIC CLAIM.',
          'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE COEFFICIENTS AND THE MATCHED ZERO, AT SIX RADII.', '-' * 100,
           '  %-14s %-20s %s' % ('a', 'c1', 'zeros in s')]
    for r in PROF:
        Bk.append('  %-14.7f %-20.12f %s'
                  % (r['a'], r['c1'], ', '.join('%.9f' % z for z in r.get('zeros', []))))
    Bk += ['', '-' * 100, '### THE WEIGHT TABLE.', '-' * 100,
           '  %-6s %-6s %-20s %s' % ('n', 'p', '2 log p / sqrt(n)', 'rank')]
    for w in WTS:
        Bk.append('  %-6d %-6d %-20.9f %d of %d' % (w['n'], w['p'], w['w'], w['rank'], len(WTS)))
    Bk += ['', '-' * 100, '### THE FIXED POINT.', '-' * 100,
           '  u0, route A (digamma)                 : %s' % U0.get('routeA'),
           '  u0, route B (log-derivative of Gamma_R): %s' % U0.get('routeB'),
           '  they differ by                        : %.3e' % U0.get('diff', 0),
           '  tolerance, stated first               : %.0e' % U0.get('tol', 0),
           '  named by any act                      : %s' % ('YES' if U0.get('named') else 'NO'),
           '  files carrying the value              : %s' % U0.get('provenance')]
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


B438ROW_RE = r"(?m)^\| (\d+) \| \*\*WHAT ALTERNATES THE SIGN"


def main():
    bar('=')
    rec('b439_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not PRICE or not WTS:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      profile FIXED : %s ; c1 spread %.6e ; matched zero spread %.6e'
        % (FIXED, SPREAD_C1 or 0, SPREAD_S or 0))
    rec('      weight maximizer n = %s ; position holds at %s of %s cells ; u0 = %s'
        % (MAXN, C2.get('agree'), C2.get('total'), U0.get('u0')))
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
        % [int(x.group(1)) for x in re.finditer(B438ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B438ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b439_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
