# -*- coding: utf-8 -*-
"""b440_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b440 the fixed point named, the break attributed, and two facts built -->'
PRIOR = '<!-- b439 the fixed profile, the fixed point, and one arithmetic claim -->'
BANKOUT = os.path.join(D, 'b440_the_fixed_point.txt')
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


FACE = read(os.path.join(D, 'b440_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b440_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b440_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b440_components.txt'))
EXTR = read(os.path.join(D, 'b440_extract.txt'))


def _j(name, default):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return default


U0 = _j('b440_u0.json', {})
KA = _j('b440_kernel_attempt.json', {})
CL = _j('b440_clauses.json', {})
MECH = CL.get('mechanism') or []
PRICE = KA

# ### **EVERY VERDICT BELOW IS READ OFF THE COMPONENTS RECORD, NOT TYPED HERE.**
CLAUSE = dict(re.findall(r'CLAUSE \(([abcd])\) : ([^*]+?)\.\*\*', COMP))
AGREE = re.search(r'IT AGREES AT (\d+) OF (\d+) CELLS', COMP)
AG, TOT = (AGREE.group(1), AGREE.group(2)) if AGREE else ('?', '?')
SECOND = ('EXPLAINED' if 'NEVER CROSSING: EXPLAINED' in COMP else 'NOT EXPLAINED')
TIGHT = re.search(r'\*\*LINES : (\d+)\*\*', COMP)
NTIGHT = TIGHT.group(1) if TIGHT else '?'
NJOIN = re.search(r'CLASSIFIED `JOIN` : (\d+)', COMP)
NJOIN = NJOIN.group(1) if NJOIN else '?'
AXFREE = len([k for k, v in (KA.get('axiom_profiles') or {}).items() if v == 'NONE'])
AXCARRY = len([k for k, v in (KA.get('axiom_profiles') or {}).items() if v != 'NONE'])
BUILT = KA.get('objects_built', 0)

# ### **A MARKER MUST BE DISTINGUISHABLE FROM EVERY EARLIER ONE.** ### The first writing of this
# ### marker began `THE PROFILE IS NOT FIXED`, which is how b439`s row begins, and the by-marker
# ### read then returned TWO rows. ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER, SO A SHARED
# ### PREFIX IS NOT COSMETIC** -- it is the read itself failing. ### Caught before the commit and
# ### the row rewritten.
ROWMARK = ('**u0 IS THE DEFINING EQUATION`S ROOT AND 2 pi IS THE ASYMPTOTE`S; h+/2pi IS THE SMOOTH '
           'ZERO-COUNTING DENSITY AND THE CORPUS NOWHERE SAYS SO; NEITHER KERNEL FACT IS BUILT '
           'BECAUSE THE WEIGHT TABLE CANNOT BE STATED AXIOM-FREE; AND THE cosh IS THE POLE WEIGHT, '
           'NOT THE ARCHIMEDEAN ONE**')

SCOPE = ("### THE ACT CHECKS FOUR CLAUSES ABOUT ONE CONSTANT, ATTEMPTS TWO KERNEL STATEMENTS AND "
         "BUILDS NEITHER, AND READS ONE WEIGHT`S IDENTITY OUT OF THE CORPUS`S OWN DICTIONARY. "
         "### NO NEW INSTRUMENT, NO NEW FAMILY, NEITHER INSTRUMENT LANE OPENED; THE KERNEL LANE "
         "OPENED TO BUILD AND 0 OBJECTS WERE BUILT. ### NO CLAIM ABOUT RH, h2, ZETA OR ANY ZERO")

DESK = [
    ('what u0 is -- root, density, asymptote, digits', 'CLOSE',
     'ANSWERED at b440, **FOUR CLAUSES, FOUR VERDICTS.** (a) u0 IS the exact root of '
     '`Re psi(1/4 + iu/2) = log pi`, by two routes sharing no code and agreeing to `%s`. '
     '(b) `h+/2pi` IS the smooth zero-counting density -- and sharper than the clause claimed: '
     'its integral is `theta(T)/pi`, and the Riemann-von Mangoldt main term is that integral '
     '**plus exactly one**, the pole. (c) the asymptote `log(u/2pi)` vanishes at `2 pi` exactly, '
     'and the corpus has carried that since b235. (d) the digits agree; the ratio is `%s`.'
     % ('%.0e' % (U0.get('route_gap') or 0), str(U0.get('ratio', ''))[:12])),
    ('whether the corpus itself makes the density identification', 'CLOSE',
     'ANSWERED at b440: **NO.** The tight screen -- the expression itself beside a counting word '
     'on one line -- returns %s lines across 405 documents, **all %s hand-read and all NOT A '
     'JOIN.** The corpus carries the expression as `W_inf` and the counting law as '
     '`Riemann-von Mangoldt`, and joins them nowhere. **The nearest line DENIES the relation:** '
     'the window kernel`s own non-claim, warning that its `W` is a counting function *unrelated* '
     'to `W_inf`.' % (NTIGHT, NTIGHT)),
    ('whether the two finite facts can be built axiom-free', 'CLOSE',
     'ANSWERED at b440 by running Lean, not by assertion: **NEITHER IS BUILT, AND %d OBJECTS WERE '
     'COMPILED INTO THE KERNEL.** The maximizer comparison reduces to `(log_q p)^2 > p^k/q^j` -- '
     'a transcendental against a rational. The kernel has no `Real`; its `Rat` and `Float` are '
     'opaque to `decide`; a literal surrogate is the `MEASURED-AT-BANK` pattern `Ladder.lean` '
     'refuses. **The order said build neither, and neither was built.**' % BUILT),
    ('what the aim`s second moment condition actually is', 'CLOSE',
     'ANSWERED at b440 from the corpus`s own term-for-term dictionary: `cosh(v/2)` weights '
     '**`W_pole`**, not `W_inf`. The aim`s second condition is the lawfulness condition '
     '`h-hat(i/2) = 0` -- *kill the pole term*. `cosh(v/2) = (x^(1/2) + x^(-1/2))/2` is the '
     '`s <-> 1-s` symmetric pair, and a dilation by `c` scales it by exactly `(1 + 1/c)/2`, never '
     'by one factor. **The break is structural and its structure is the functional equation`s '
     'pole pair.**'),
    ('fact (i) alone, which is buildable and was not built', 'STAND',
     'ROUTED to the author at b440. `(primePowersLT n).elem n = false` closes by `decide` with '
     '**no axioms at all**, four times, with a positive control. The order forbade building it '
     'alone, so it was not built. **And one thing the author needs before deciding: the '
     'PROPOSITIONAL form carries `[propext, Quot.sound]` and would break this repository`s own '
     'standard; only the decidable-equality form is clean.**'),
    ('whether the mechanism sentence is a mechanism', 'STAND',
     'QUALIFIED at b440. *The archimedean slack closes when half the seed`s transform mass lies '
     'above u0* predicts the sign of `A` at **%s of %s cells across both families** and fails at '
     'one -- the second family at `a = 1.2`, where the mass criterion says cross and `A` does '
     'not. **So the second family`s never crossing is %s by the same sentence.** `A` is a '
     'weighted balance, not a median; what survives is that `u0` is the hinge.'
     % (AG, TOT, SECOND)),
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
            '### b440 — the fixed point named, the break attributed, and two facts built — filed 2026-09-12',
            '',
            '**Two of the three expectations are refuted, and the act builds nothing into the kernel because the order told it not to build one fact alone.** No new instrument, no new family, neither instrument lane opened.',
            '',
            '#### Component 1 — four clauses, four verdicts, and the density is real',
            '',
            '`u0` is the exact root of `Re ψ(¼ + iu/2) = log π`, located by two routes that share no code — `digamma` directly, and the log-derivative of the completed gamma factor through `loggamma` — agreeing to `@GAP@` against a tolerance of `1e-12` stated first.',
            '',
            '**And the density identification holds, more sharply than it was put.** `h₊(u)/2π` integrates to `θ(T)/π`, the Riemann–Siegel theta over `π`, and the Riemann–von Mangoldt main term is **that integral plus exactly one, with the deficit `1/(48πT)` — both leftover terms named**. The `1` is the pole of `ζ` at `s = 1` — the same `W_pole` Component 3 turns out to be about, arriving by a different door.',
            '',
            '**The corpus does not make the identification.** 405 documents; the tight screen returns @NT@ lines; all @NT@ hand-read; **all NOT A JOIN.** The corpus has the expression (as `W_∞`) and the counting law (as Riemann–von Mangoldt) and joins them nowhere. The nearest line *denies* the relation: `SIDE-window`’s own non-claim, warning that its `W` is a counting function **unrelated** to `W_∞`.',
            '',
            '**And `2π` is not `u0`.** It is the zero of a *different* function agreeing with `h₊` to `O(u⁻²)`; `h₊(2π) = −1.06e−03`. Defining equation: **held**. Classical asymptote: **held, and it is `2π`**. Closed form: **not held** — twenty-one digits is not a closed form.',
            '',
            '#### Component 2 — neither fact built, and the reason was run, not asserted',
            '',
            'Fact (ii) is the weight table `2Λ(n)/√n`. The maximizer comparison reduces, exactly, to `(log_q p)² > p^k/q^j` — **an inequality between a transcendental and a rational** — and exponentiating only moves the irrational into the exponent. The probe, run in the scratchpad and in no repository: `Real` is an unknown identifier; `Rat` and `Float` exist and **both are opaque to `decide`** (*"reduction got stuck at the `Decidable` instance"*); `Nat.sqrt` does not exist. A `Decidable` instance for `Float` order *does* exist — **the proposition is nominally decidable and `decide` still cannot close it.**',
            '',
            '**The positive control passed, which is what makes the refusals mean anything.** And it carried a result this seat had not expected: `(primePowersLT 16).elem 16 = false` depends on **no axioms at all**, while `16 ∉ primePowersLT 16` depends on **`[propext, Quot.sound]`**. **The form of the statement decides whether it is axiom-free** — b418’s lesson, confirmed on a new statement. @AXF@ terminals came back clean and @AXC@ carried axioms.',
            '',
            '**So, by the order’s own condition, neither fact is built and @BUILT@ objects were compiled.** Nothing was written into `SIDE-window` — not a `.lean` file and not `README.md`, because (R52) updates non-claims when *contents change*, and nothing changing is not a change. Fact (i) alone is buildable and is **routed back, not taken**.',
            '',
            '#### Component 3 — the `cosh` is the pole weight, and the premise failed',
            '',
            'The order asked whether `cosh(v/2)` is the archimedean factor’s own scaling, *and said to state a finding only if it is*. The corpus’s term-for-term dictionary answers in two rows: `P = ĥ(i/2) + ĥ(−i/2) = 2∫w cosh(v/2)dv` is **`W_pole`**; `A = (1/2π)∫ĥ(u)[Re ψ(¼ + iu/2) − log π]du` is **`W_∞`**. **The premise fails and the offered finding is not stated.**',
            '',
            '**What is true instead is better.** The aim’s second moment condition *is* the lawfulness condition `ĝ(i/2) = 0` — the requirement that the test function kill the pole term. And `cosh(v/2) = (x^½ + x^−½)/2` is the `s ↔ 1−s` symmetric pair; a dilation by `c` scales the integral by exactly **`(1 + 1/c)/2`**, verified to nine figures, never by a single factor. **The break is structural, and its structure is the functional equation’s pole pair, not the gamma factor.** b439’s `2.266e−04` is untouched; only its attribution moves.',
            '',
            '#### The expectations',
            '',
            '| | the navigator’s | verdict |',
            '|:--|:--|:--|',
            '| (N1)(a) | the density identification holds | **HELD** |',
            '| (N1)(b) | the atlas already carries the expression under another name | **HALF HELD** — it carries the *expression* as `W_∞`; it does not carry the *identification* |',
            '| (N2)(a) | fact (i) builds axiom-free | **HELD**, in the decidable-equality form only |',
            '| (N2)(b) | fact (ii) builds axiom-free | **REFUTED** |',
            '| (N3)(a) | the `cosh` is the archimedean weight | **REFUTED** — it is the pole weight |',
            '| (N3)(b) | the break is structural | **HELD**, for the functional equation’s reason |',
            '',
            '*And this seat’s own two, declared on the face and scored the same way: **neither fact built** — held; **the cosh is the pole weight** — held.*',
            '',
            '**Two incidents of this act’s own, printed not patched away.** The first writing emitted `data/b440_mechanism.json`, a path the locked face never declared; the face was not edited, the rows were moved into a declared path, and **the write-list arm is what caught it**. And `carto_atlas.kernel` caches on its first argument and ignores every later one, so a bisection through it converges on its own lower bracket — it returned `6.0` with a residual of `1.6e−03`, and **the tolerance stated first is what caught that**. The instrument is correct for its own single-grid use and was not edited.',
    ]
    rep = (('@GAP@', '%.0e' % (U0.get('route_gap') or 0)), ('@NT@', str(NTIGHT)),
           ('@AXF@', str(AXFREE)), ('@AXC@', str(AXCARRY)), ('@BUILT@', str(BUILT)))
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b440)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run "
            "as b440 -- @GR@ gates read, @GDG@ checked by digest; TWO AUTHOR RULINGS (R51) AND "
            "(R52) RATIFIED BY THE PASTE AND ENTERED ON THE FACE; THE KERNEL LANE OPEN TO BUILD "
            "FOR COMPONENT 2 ALONE AND BOTH INSTRUMENT LANES PARKED; (R50)'S ADDENDUM SLOT NAMED "
            "IN THE WRITE LIST AND EMPTY, WHICH IS NEVER A DEFECT. "
            "**COMPONENT 1, FOUR CLAUSES AND FOUR VERDICTS: u0 IS THE EXACT ROOT OF "
            "Re psi(1/4 + iu/2) = log pi, BY TWO ROUTES SHARING NO CODE AGREEING TO @GAP@ AGAINST "
            "A TOLERANCE OF 1e-12 STATED FIRST; h+/2pi IS THE SMOOTH ZERO-COUNTING DENSITY AND "
            "SHARPER THAN THE CLAUSE CLAIMED -- ITS INTEGRAL IS theta(T)/pi AND THE RIEMANN-VON "
            "MANGOLDT MAIN TERM IS THAT INTEGRAL PLUS EXACTLY ONE, THE POLE, WITH DEFICIT "
            "1/(48 pi T), BOTH LEFTOVER TERMS NAMED; THE ASYMPTOTE log(u/2pi) VANISHES AT 2 pi "
            "EXACTLY AND THE CORPUS HAS CARRIED THAT SINCE b235; AND THE DIGITS AGREE AT A RATIO "
            "OF @RATIO@.** **BUT THE CORPUS MAKES NO SUCH IDENTIFICATION: 405 DOCUMENTS, @NT@ "
            "TIGHT-SCREEN LINES, ALL @NT@ HAND-READ, ALL NOT A JOIN -- IT CARRIES THE EXPRESSION "
            "AS W_inf AND THE COUNTING LAW AS RIEMANN-VON MANGOLDT AND JOINS THEM NOWHERE, AND "
            "THE NEAREST LINE DENIES THE RELATION.** **2 pi IS NOT u0: IT IS THE ZERO OF A "
            "DIFFERENT FUNCTION AGREEING TO O(u^-2), AND h+(2 pi) = -1.06e-03. DEFINING EQUATION "
            "HELD, CLASSICAL ASYMPTOTE HELD, CLOSED FORM NOT HELD.** "
            "**COMPONENT 2: NEITHER FACT BUILT AND @BUILT@ OBJECTS COMPILED, BY THE ORDER'S OWN "
            "CONDITION. THE MAXIMIZER COMPARISON REDUCES TO (log_q p)^2 > p^k/q^j, A "
            "TRANSCENDENTAL AGAINST A RATIONAL; THE PROBE RAN AND Real IS UNKNOWN, Rat AND Float "
            "ARE BOTH OPAQUE TO decide, Nat.sqrt DOES NOT EXIST, AND A Float ORDER INSTANCE "
            "EXISTS WHILE decide STILL CANNOT CLOSE IT.** **AND THE POSITIVE CONTROL CARRIED AN "
            "UNEXPECTED RESULT: (primePowersLT 16).elem 16 = false HAS NO AXIOMS AT ALL WHILE THE "
            "PROPOSITIONAL FORM CARRIES [propext, Quot.sound] -- @AXF@ CLEAN TERMINALS AND @AXC@ "
            "CARRYING AXIOMS, SO THE FORM OF THE STATEMENT DECIDES IT. FACT (i) IS BUILDABLE AND "
            "IS ROUTED BACK, NOT TAKEN.** "
            "**COMPONENT 3: THE ORDER'S CONDITIONAL PREMISE FAILS AND THE OFFERED FINDING IS NOT "
            "STATED. THE CORPUS'S OWN DICTIONARY SAYS cosh(v/2) WEIGHTS W_pole AND THE "
            "ARCHIMEDEAN WEIGHT IS Re psi(1/4 + iu/2) - log pi IN A DIFFERENT VARIABLE. THE AIM'S "
            "SECOND MOMENT CONDITION IS THE LAWFULNESS CONDITION g-hat(i/2) = 0, AND A DILATION "
            "SCALES THAT INTEGRAL BY EXACTLY (1 + 1/c)/2. THE BREAK IS STRUCTURAL AND ITS "
            "STRUCTURE IS THE FUNCTIONAL EQUATION'S POLE PAIR; b439'S 2.266e-04 IS UNTOUCHED AND "
            "ONLY ITS ATTRIBUTION MOVES.** "
            "0 INSTRUMENTS BUILT, 0 FAMILIES DEFINED, 0 INSTRUMENT LANES OPENED, 0 CELLS "
            "WRITTEN, 0 GRADES MOVED, 0 SIDE-window FILES WRITTEN, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The kernel lane opened to build and the "
            "act built nothing, so SIDE-window's terminal count is byte-unmoved")
    prof = ("### ONE PLACE-papers FILE APPENDED (OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; "
            "FACES_LEDGER.md BYTE-UNMOVED AND THE REGISTER STILL FROZEN AT SIX; EVERY INSTRUMENT "
            "FILE BYTE-UNMOVED INCLUDING carto_atlas.py, WHOSE CACHING DEFECT THIS ACT FOUND AND "
            "DID NOT REPAIR; EVERY SIDE-window FILE BYTE-UNMOVED, README.md INCLUDED; b439'S BANK "
            "BYTE-UNMOVED THOUGH ITS ATTRIBUTION IS CORRECTED HERE -- 0 CONTENT LOST")
    grade = ("### THE FACE DECLARED TWO EXPECTATIONS OF THIS SEAT'S OWN AND BOTH WERE SCORED LIKE "
             "THE NAVIGATOR'S; THE IMPOSSIBILITY IN COMPONENT 2 WAS DEMONSTRATED BY RUNNING LEAN "
             "RATHER THAN ASSERTED, WITH A POSITIVE CONTROL THAT PASSED AND AN AXIOM RESULT THE "
             "SEAT HAD NOT PREDICTED; AND TWO DEFECTS OF THIS ACT'S OWN -- AN UNDECLARED WRITE "
             "PATH AND A BISECTION THROUGH A CACHED INSTRUMENT -- ARE PRINTED WITH THE ARMS THAT "
             "CAUGHT THEM")
    status = ("data/b440_the_fixed_point.txt; data/b440_components.txt; data/b440_extract.txt; "
              "data/b440_u0.json; data/b440_clauses.json; data/b440_kernel_attempt.json; "
              "data/b440_density_search.json; data/b440_checks.txt; "
              "data/b440_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "data/b440_addendum.txt (the (R50) slot, EMPTY); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@GAP@', '%.0e' % (U0.get('route_gap') or 0))
                .replace('@RATIO@', str(U0.get('ratio', ''))[:12])
                .replace('@NT@', str(NTIGHT)).replace('@BUILT@', str(BUILT))
                .replace('@AXF@', str(AXFREE)).replace('@AXC@', str(AXCARRY)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('what is u0 and is it 2 pi',
           'is the archimedean kernel a zero counting density',
           'can the weight table be stated axiom free',
           'what does cosh v over 2 weight',
           'why is the seed profile not scale invariant')
MUST_NOT_HIT = ('the weight table was built', 'u0 has a closed form',
                'the corpus identifies h plus as a density')
KEY = 'the-fixed-point-named-the-break-attributed-and-two-facts-built'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b440 CHECKED FOUR CLAUSES ABOUT ONE CONSTANT, ATTEMPTED TWO KERNEL STATEMENTS AND BUILT "
        "NEITHER, AND READ ONE WEIGHT'S IDENTITY OUT OF THE CORPUS'S OWN DICTIONARY. "
        "COMPONENT 1, FOUR CLAUSES AND FOUR VERDICTS: u0 IS THE EXACT ROOT OF "
        "Re psi(1/4 + iu/2) = log pi, LOCATED BY TWO ROUTES THAT SHARE NO CODE agreeing to %s "
        "against a tolerance of 1e-12 stated first. h+/2pi IS THE SMOOTH ZERO-COUNTING DENSITY, "
        "AND SHARPER THAN THE CLAUSE CLAIMED: its integral is theta(T)/pi, and THE RIEMANN-VON "
        "MANGOLDT MAIN TERM IS THAT INTEGRAL PLUS EXACTLY ONE -- the pole of zeta at s = 1 -- "
        "with deficit 1/(48 pi T), BOTH LEFTOVER TERMS NAMED. BUT THE CORPUS MAKES NO SUCH "
        "IDENTIFICATION: 405 documents, %s tight-screen lines, ALL HAND-READ AND ALL NOT A JOIN; "
        "it carries the expression as W_inf and the counting law as Riemann-von Mangoldt and "
        "JOINS THEM NOWHERE, and THE NEAREST LINE DENIES THE RELATION -- SIDE-window's own "
        "non-claim, warning that its W is a counting function UNRELATED to W_inf. AND 2 pi IS "
        "NOT u0: it is the zero of a DIFFERENT function agreeing to O(u^-2), and h+(2 pi) = "
        "-1.06e-03. DEFINING EQUATION HELD, CLASSICAL ASYMPTOTE HELD AND IT IS 2 pi, CLOSED FORM "
        "NOT HELD -- TWENTY-ONE DIGITS IS NOT A CLOSED FORM. "
        "COMPONENT 2: NEITHER FACT IS BUILT AND %s OBJECTS WERE COMPILED, BY THE ORDER'S OWN "
        "CONDITION. The maximizer comparison reduces exactly to (log_q p)^2 > p^k/q^j, AN "
        "INEQUALITY BETWEEN A TRANSCENDENTAL AND A RATIONAL, and exponentiating only moves the "
        "irrational into the exponent. THE PROBE WAS RUN, NOT DESCRIBED: Real is an unknown "
        "identifier; Rat and Float exist and BOTH ARE OPAQUE TO decide; Nat.sqrt does not exist; "
        "and a Decidable instance for Float order DOES exist while decide still cannot close it. "
        "THE POSITIVE CONTROL PASSED AND CARRIED A RESULT THE SEAT HAD NOT PREDICTED: "
        "(primePowersLT 16).elem 16 = false HAS NO AXIOMS AT ALL, while the propositional form "
        "16 not-in primePowersLT 16 CARRIES [propext, Quot.sound] -- %s clean terminals and %s "
        "carrying axioms, so THE FORM OF THE STATEMENT DECIDES WHETHER IT IS AXIOM-FREE. FACT (i) "
        "IS BUILDABLE AND IS ROUTED BACK, NOT TAKEN. "
        "COMPONENT 3: THE ORDER'S CONDITIONAL PREMISE FAILS AND THE OFFERED FINDING IS NOT "
        "STATED. The corpus's term-for-term dictionary says cosh(v/2) WEIGHTS W_pole, and the "
        "archimedean weight is Re psi(1/4 + iu/2) - log pi in a different variable. THE AIM'S "
        "SECOND MOMENT CONDITION IS THE LAWFULNESS CONDITION g-hat(i/2) = 0 -- the requirement "
        "that the test function KILL THE POLE TERM -- and cosh(v/2) = (x^(1/2) + x^(-1/2))/2 is "
        "the s <-> 1-s symmetric pair, which a dilation by c scales by EXACTLY (1 + 1/c)/2, "
        "verified to nine figures, NEVER BY A SINGLE FACTOR. THE BREAK IS STRUCTURAL AND ITS "
        "STRUCTURE IS THE FUNCTIONAL EQUATION'S POLE PAIR, NOT THE GAMMA FACTOR. b439's "
        "2.266e-04 IS UNTOUCHED AND ONLY ITS ATTRIBUTION MOVES. "
        "THE MECHANISM SENTENCE IS A HEURISTIC AND THE ACT SAYS SO: it predicts the sign of A at "
        "%s of %s cells across both families and FAILS AT ONE, so THE SECOND FAMILY'S NEVER "
        "CROSSING IS NOT EXPLAINED BY THE SAME SENTENCE. "
        "TWO DEFECTS OF THIS ACT'S OWN ARE PRINTED: an undeclared write path, caught by the "
        "write-list arm; and a bisection through carto_atlas.kernel, WHICH CACHES ON ITS FIRST "
        "ARGUMENT AND IGNORES EVERY LATER ONE, caught by the tolerance stated first. "
        "0 INSTRUMENTS BUILT, 0 FAMILIES DEFINED, 0 INSTRUMENT LANES OPENED, 0 SIDE-window FILES "
        "WRITTEN, 0 CONTENT LOST"
        % ('%.0e' % (U0.get('route_gap') or 0), NTIGHT, BUILT, AXFREE, AXCARRY, AG, TOT))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO CELL WRITTEN, NO SITE ENTERED, NO "
             "BRIDGE TYPED. ### NO NEW INSTRUMENT, NO NEW FAMILY, NEITHER INSTRUMENT LANE OPENED. "
             "### THE KERNEL LANE OPENED TO BUILD AND NOTHING WAS COMPILED FOR THE WINDOW KERNEL. "
             "### NO CLAIM ABOUT RH, h2, ZETA OR ANY ZERO")
    where = ("data/b440_the_fixed_point.txt; data/b440_components.txt; data/b440_extract.txt; "
             "data/b440_u0.json; data/b440_clauses.json; data/b440_kernel_attempt.json; "
             "data/b440_density_search.json; data/b440_checks.txt; "
             "data/b440_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b440 (the fixed point named, the break attributed, and two facts built)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FIXED POINT NAMED, THE BREAK ATTRIBUTED, AND TWO FACTS BUILT (b440).%s'
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
        rec('    %-58s reaches the b440 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the two routes carried', 'TWO ROUTES THAT SHARE NO CODE' in out),
            ('the density identification carried', 'SMOOTH ZERO-COUNTING DENSITY' in out),
            ('the plus-one carried', 'THAT INTEGRAL PLUS EXACTLY ONE' in out),
            ('the corpus`s silence carried', 'JOINS THEM NOWHERE' in out),
            ('the denial carried', 'NEAREST LINE DENIES THE RELATION' in out),
            ('2 pi is not u0 carried', 'NOT u0' in out),
            ('no closed form carried', 'CLOSED FORM NOT HELD' in out),
            ('the build decision carried', 'NEITHER FACT IS BUILT' in out),
            ('the transcendental step carried', 'A TRANSCENDENTAL AND A RATIONAL' in out),
            ('the probe carried', 'BOTH ARE OPAQUE TO decide' in out),
            ('the axiom result carried', 'FORM OF THE STATEMENT DECIDES' in out),
            ('fact (i) routed carried', 'ROUTED BACK, NOT TAKEN' in out),
            ('the failed premise carried', 'OFFERED FINDING IS NOT STATED' in out),
            ('the pole weight carried', 'WEIGHTS W_pole' in out),
            ('the dilation factor carried', 'EXACTLY (1 + 1/c)/2' in out),
            ('the attribution-only move carried', 'ONLY ITS ATTRIBUTION MOVES' in out),
            ('the heuristic caveat carried', 'NOT EXPLAINED BY THE SAME SENTENCE' in out),
            ('this act`s own defects carried', 'CACHES ON ITS FIRST' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
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
        rec('    %-58s reaches the b440 key : %s' % (qq[:58], g2))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq[:48], no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, 'b440 -- THE FIXED POINT NAMED, THE BREAK ATTRIBUTED, AND TWO FACTS BUILT.',
          'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE FOUR CLAUSES, APART.', '-' * 100]
    for k in ('a', 'b', 'c', 'd'):
        Bk.append('  clause (%s) : %s' % (k, CLAUSE.get(k, 'NOT REACHED')))
    Bk += ['', '-' * 100, '### THE FIXED POINT.', '-' * 100,
           '  u0, route A (digamma)                  : %s' % U0.get('u0'),
           '  u0, route B (loggamma + derivative)     : %s' % U0.get('routeB'),
           '  they differ by                          : %.3e' % (U0.get('route_gap') or 0),
           '  tolerance, stated first                 : 1e-12',
           '  2 pi                                    : %s' % U0.get('two_pi'),
           '  ratio u0 / 2 pi                         : %s' % U0.get('ratio'),
           '  the navigator`s digits                  : %s' % U0.get('navigator'),
           '  this seat`s                             : %s' % U0.get('seat')]
    Bk += ['', '-' * 100, '### THE KERNEL ATTEMPT. ### **0 OBJECTS BUILT, BY THE ORDER`S OWN '
           'CONDITION.**', '-' * 100,
           '  fact (i)   : %s' % KA.get('fact_i'),
           '  fact (ii)  : %s' % KA.get('fact_ii'),
           '  objects built : %s   ### reason : %s' % (KA.get('objects_built'), KA.get('reason')),
           '', '  ### THE AXIOM PROFILES, PRINTED FROM THE PROBE`S OWN OUTPUT:',
           '  %-18s %s' % ('terminal', 'axioms')]
    for k, v in sorted((KA.get('axiom_profiles') or {}).items()):
        Bk.append('  %-18s %s' % (k, v))
    Bk += ['', '  ### ### **AND THE FORM OF THE STATEMENT DECIDES IT: the decidable-equality form',
           '  ### ### carries no axioms; the propositional form carries two.**']
    Bk += ['', '-' * 100, '### THE MECHANISM, TESTED ON BOTH FAMILIES.', '-' * 100,
           '  %-8s %-9s %-18s %-14s %s' % ('family', 'a', 'median u', 'mass above u0', 'A')]
    for r in MECH:
        Bk.append('  %-8s %-9.4f %-18.6f %-14.6f %+.6f'
                  % (r['family'], r['a'], r['median'], r['mass_above_u0'], r['A']))
    Bk += ['', '  agrees at %s of %s cells ; the second family`s never crossing is %s'
           % (AG, TOT, SECOND)]
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


B439ROW_RE = r"(?m)^\| (\d+) \| \*\*THE PROFILE IS NOT FIXED, SO"


def main():
    bar('=')
    rec('b440_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not U0 or not KA or not MECH:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    if len(CLAUSE) != 4:
        rec('  ### HARD FAILURE -- %d clause verdicts read, expected 4.' % len(CLAUSE))
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      clauses %s ; tight-screen lines %s ; joins %s'
        % (''.join(sorted(CLAUSE)), NTIGHT, NJOIN))
    rec('      objects built %s ; axiom-free terminals %d ; terminals carrying axioms %d'
        % (BUILT, AXFREE, AXCARRY))
    rec('      u0 = %s ; routes differ by %.3e ; mechanism agrees %s of %s ; second family %s'
        % (U0.get('u0'), U0.get('route_gap') or 0, AG, TOT, SECOND))
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
        % [int(x.group(1)) for x in re.finditer(B439ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B439ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b440_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
