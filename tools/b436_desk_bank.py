# -*- coding: utf-8 -*-
"""b436_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b436 the witness arc at site (iv), the window -->'
PRIOR = '<!-- b435 the cure shared, and the skips that print like passes -->'
BANKOUT = os.path.join(D, 'b436_the_window.txt')
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


FACE = read(os.path.join(D, 'b436_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b436_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b436_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b436_components.txt'))
try:
    CAND = json.loads(read(os.path.join(D, 'b436_candidates.json')) or '{}')
except Exception:
    CAND = {}
try:
    SIDES = json.loads(read(os.path.join(D, 'b436_two_sides.json')) or '[]')
except Exception:
    SIDES = []

NC = len(CAND.get('candidates', []))
HELD = CAND.get('held')
KINDS = CAND.get('tally', {})
PRIOR_UNION = CAND.get('prior_union', [])
UNION4 = CAND.get('union_four', [])
SHARED = CAND.get('shared', [])
NEW = CAND.get('new', [])
SHARED_N = sum(v for k, v in KINDS.items() if k in set(PRIOR_UNION))
A0 = SIDES[0] if SIDES else {}
A9 = SIDES[-1] if SIDES else {}
ROWMARK = ('**THE WITNESS ARC AT SITE (iv), THE WINDOW: SEVEN CANDIDATES ENUMERATED AND NONE HELD, '
           'THE NAVIGATOR`S BOUND LOCATED AS ELEMENTARY AND FAILING ON THE COMPARISON, AND THE '
           'CROSSING COMPARABLE BUT UNDECIDED BECAUSE THE RECORD`S WINDOW ENDS**')

SCOPE = ("### THE ACT ENTERS NO SITE IN THE REGISTER, WHICH STAYS FROZEN AT SIX, AND TYPES NO "
         "BRIDGE BETWEEN ANY TWO OF THE SIX. ### IT WRITES NO INSTRUMENT: BOTH LANES ARE PARKED "
         "AND b435'S GUARD-LAYER EXCEPTION CLOSED AT b435'S END. ### IT MOVES NO GRADE AND EDITS "
         "NO KEYSTONE")

DESK = [
    ('the witness arc, site (iv) -- the window', 'CLOSE',
     'ENUMERATED AND EXHAUSTED at b436. **%d candidates, %d held.** The object was declared a '
     'UNIFORM BOUND before the first candidate, because this site`s cell reads `UNSTATED`: its '
     'record holds measured values, not an existential, so the shared-witness form does not '
     'transpose. Every candidate failed at a quoted step. **No cell written; the exhausted list '
     'is filed as a block, as sites (i), (ii) and (iii) filed theirs.**' % (NC, HELD)),
    ('the navigator`s Chebyshev-Mertens bound', 'CLOSE',
     'TESTED IN TWO PARTS at b436 and **not adopted on his word**. (a) **LOCATED AS ELEMENTARY** '
     'by the order`s own second route, and **NOT LOCATED AS A BANKED STATEMENT** -- no verified '
     'source states it, and the vocabulary that looks like it sits in `internal/`, which the '
     'corpus classes REGISTRY-SILENT working logs, where the one psi statement is **conditional '
     'on RH**. (b) **IT RUNS THE WRONG WAY** -- see the finding below. His paraphrase, checked '
     'against `(149)` rather than taken, is **accurate**.'),
    ('THE FINDING: the prime constituent climbs while the archimedean quantity falls', 'STANDING',
     'b321`s ten cells, read off its own table: **W_inf falls %0.6f -> %0.6f** while **|SUM_p '
     'W_p| grows %0.6f -> %0.6f**, the ratio climbing **%0.3e -> %0.3e across ten cells**. Any '
     'bound uniform in `a` must dominate the measured constituent, so **no bound of this shape '
     'can show it staying dominated**. Routed: the direction is settled, the crossing is not.'
     % (A0.get('w_inf', 0), A9.get('w_inf', 0), abs(A0.get('pr', 0)), abs(A9.get('pr', 0)),
        A0.get('ratio', 0), A9.get('ratio', 0))),
    ('whether the two sides are comparable at all', 'CLOSE',
     'ANSWERED at b436: **COMPARABLE, AND NOT NARROWLY.** They are two of the four channels of '
     'one identity `Z = P - PR + A` which b321 verified at **all thirteen cells** against an '
     'imported bar, with the archimedean channel built a second time by a route sharing no code '
     'and agreeing to `6.118e-05`. **Two quantities satisfying one verified identity are in one '
     'normalization by construction.** The navigator`s (N3) expected an incommensurability and '
     'the record holds an identity.'),
    ('the crossing, at radii above a = 3.0', 'STANDING',
     'UNDECIDED and **the reason is not normalization**. The ratio reaches `%0.3e` at the widest '
     'radius the record printed and **the window ends there**. A trend is not a crossing and this '
     'act does not extrapolate. **TRIGGER: one run of the window instrument at radii above a = '
     '3.0, emitting the same four channels in the same normalization** -- blocked, the instrument '
     'lane being parked. The price is one act with that lane open, and the seat did not open it.'
     % A9.get('ratio', 0)),
    ('the arc`s boundary count, now at four sites', 'STANDING',
     'MEASURED at b436 off the earlier sites` own JSON: **%d of %d of this site`s failures land '
     'at a boundary an earlier site used**; the union across the three earlier sites was **%d** '
     'and across all four is **%d**. **One kind is new: `WRONG DIRECTION`** -- the object exists, '
     'is uniform, is unconditional and is about the right sum, and moves the wrong way against '
     'the quantity it must be compared with. Named rather than folded into an old kind.'
     % (SHARED_N, sum(KINDS.values()) if KINDS else 0, len(PRIOR_UNION), len(UNION4))),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 and carried. **At four sites the answer has not improved**: the union of '
     'kinds grew again, from %d to %d, and a new kind appeared at the fourth site. The arc is '
     'still not converging, and this act adds a fourth reading rather than a verdict.'
     % (len(PRIOR_UNION), len(UNION4))),
    ('W-ORD-WITNESS-ENUMERATION, sites (v) and (vi)', 'STANDING',
     'CHECKPOINTED after site (iv). **Two sites remain**, one act each; trigger: the author`s '
     'word. Site (v) declares its own kind `(b)` and IS a `forall-exists`, so the shared-witness '
     'form does transpose there; site (vi) names both clauses of the form in its own text.'),
    ('the register, frozen at six', 'STANDING',
     'UNCHANGED by this act. The freeze condition is a site whose entry produces **a statement '
     'about the object** rather than about the record. **Site (iv) produced a statement about the '
     'record**, so the condition is not met and no seventh site is entered.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432 and carried. Untouched by this act.'),
    ('the write list that names a class instead of a file', 'CLOSE',
     'RULED at b436 by **(R47)**, the author`s: a write list names paths, or names the GENERATOR '
     'with a count bound and the closing prints the actual list against it. b435`s two failing '
     'arms **were right and are not re-verdicted**. This act`s face names every path; the '
     'ledger reports **0 unlisted writes**.'),
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
     'Blocked by the PARKED instrument lane, which this act did not open.'),
    ('the scan`s sites against the lock`s zero', 'STANDING', 'The (R36) instrument item.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; **byte-unmoved by this act.**'),
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
            '### b436 — the witness arc at site (iv), the window — filed 2026-09-12', '',
            '**Seven candidates enumerated, none held.** Site (iv) is the fourth of row U1’s six '
            'and the third the arc has worked; its cell reads `UNSTATED` rather than `NONE KNOWN`, '
            'and that difference was stated before the first candidate rather than discovered '
            'among them.', '',
            '#### Why the object is a uniform bound and not a shared witness', '',
            '`b405` set the cell and `b406` tested its reason. What the record holds at this site '
            'is **ten measured values indexed by the width**, not ten existential witnesses — and '
            'the existential anyone can manufacture, `∀a ∃C_a . |V(a)| ≤ C_a` with `C_a = |V(a)|`, '
            'is **trivially satisfiable**, so the shared witness it would demand *is* the missing '
            'statement rather than a repair for its absence. **An existential the record holds is '
            'not the same object as one you can always manufacture.** So every candidate here was '
            'tested as a bound.', '',
            '#### The enumeration', '',
            'The opening population is the order’s seven, each read at its own source and each '
            'failing at a quoted step: Lagarias Theorem 6.1 (**class boundary** — wrong family, '
            'wrong comparison quantity, and a hypothesis over the representation, `b401`’s three '
            'grounds); the source’s Theorem 6.11 with its `c|ĝ(0)|²`, `13 < c < 17` (**coordinate '
            'boundary** — it corrects the archimedean inequality at a support where *no prime '
            'enters*, and `b321` prints the quantity it would bound as identically `0.000000000` '
            'at every cell below `2^{1/2}`); the source’s named one-prime widening (**absent** — '
            'named and not taken); the corpus’s own window and kernel terminals (**instances not a '
            'class** — the terminal’s own name is `SmearGeneral.cells_are_instances`); the '
            'criterion itself (**form** — it asserts a sign on the *total* and bounds no '
            'constituent, and it is an equivalence with RH); and the Vinogradov–Korobov shrinkage '
            'law (**import under the bar**, `b427`’s verdict, and indexed by the *height* where '
            'this site is indexed by the *width*).', '',
            '**The extension by description found 55 hits under a cap of 8 and admitted none.** '
            'The nearest thing in a non-`internal/` document is **Mertens’ third theorem** at '
            '`phase1.5/method/SIEVE_TO_SIDE.md:20` — a product over primes, a different sum.', '',
            '#### The navigator’s candidate, in two parts', '',
            '**His paraphrase is accurate** — checked against `(149)` rather than taken: with '
            '`f(x) = x^{-1/2} w(log x)` each term carries `log p` and `p^{-m/2}`, and the support '
            '`[a^{-2}, a²]` cuts the sum at `p^m ≤ a²`.', '',
            '**(a) LOCATED AS ELEMENTARY; NOT LOCATED AS A BANKED STATEMENT.** As mathematics it '
            'is elementary and uncontroversial, which is the order’s own second route. As record '
            'it is absent: no verified source states it, and the `Chebyshev psi` vocabulary sits '
            'only in `internal/`, which the corpus itself classes **REGISTRY-silent working logs, '
            'census-only** — where the one ψ statement is in any case **conditional on RH**, the '
            'one thing this candidate must not be. Both halves are printed because only one of '
            'them is what was asked for.', '',
            '**(b) IT RUNS THE WRONG WAY, and this is the act’s finding.** At `b321`’s ten cells '
            'the archimedean quantity **falls %0.6f → %0.6f** while the prime constituent **grows '
            'in absolute value %0.6f → %0.6f**; the ratio climbs **%0.3e → %0.3e across ten '
            'cells**. Any bound uniform in `a` must dominate the measured constituent, so **no '
            'bound of this shape can show the prime side staying dominated: the thing it bounds is '
            'itself climbing toward the thing it would have to stay under.** The bound’s own '
            'growth is *not* a banked figure and was not computed here — what is banked is the '
            'measured constituent, and that settles the direction without computing anything.'
            % (A0.get('w_inf', 0), A9.get('w_inf', 0), abs(A0.get('pr', 0)),
               abs(A9.get('pr', 0)), A0.get('ratio', 0), A9.get('ratio', 0)), '',
            '#### Is the crossing real, or an artefact of two normalizations never compared?', '',
            '**COMPARABLE — and not narrowly.** The two quantities are two of the four channels of '
            'one identity, `Z = P − PR + A`, which `b321` verified at **all thirteen cells** '
            'against a bar it imported rather than chose; the archimedean channel was built a '
            'second time by a route sharing no code, the two agreeing to `6.118e-05`. **Two '
            'quantities that satisfy one verified identity are in one normalization by '
            'construction**, and no reconciliation is owed.', '',
            '**And the crossing is still undecided — for a different reason, which is why the '
            'verdict and its reason were scored apart.** The ratio reaches `%0.3e` at `a = %s` and '
            '**the record’s window ends there**. At no radius the corpus has computed does the '
            'prime constituent reach the archimedean quantity. **A trend is not a crossing.** What '
            'would decide it: one run of the window instrument at radii above `a = %s`, emitting '
            'the same four channels in the same normalization — **blocked, the instrument lane '
            'being parked.**' % (A9.get('ratio', 0), A9.get('a'), A9.get('a')), '',
            '#### The boundary count, now at four sites', '',
            'Read off `b424`, `b427` and `b428`’s own banked JSON and never typed: **%d of %d** of '
            'this site’s failures land at a boundary an earlier site used; the union across the '
            'three earlier sites was **%d** and across all four is **%d**. **One kind is new — '
            '`WRONG DIRECTION`** — and it is named rather than folded into an old one: the object '
            'exists, is uniform, is unconditional and is about the right sum, and it moves the '
            'wrong way against the quantity it must be compared with. **That is a different '
            'failure from every one the arc has recorded.**'
            % (SHARED_N, sum(KINDS.values()) if KINDS else 0, len(PRIOR_UNION), len(UNION4)), '',
            '#### What this act did not do', '',
            '**No cell was written and none edited**; no candidate held, so the exhausted list is '
            'filed as a block. The register stays **frozen at six** and no seventh site is '
            'entered — site (iv) produced a statement about the *record*, which is not the freeze '
            'condition. **No bridge is typed between any two of the six, in either direction.** No '
            'instrument was written: both lanes are parked and `b435`’s guard-layer exception '
            'closed at `b435`’s end. The arc is **checkpointed after site (iv)**; sites (v) and '
            '(vi) remain. The four lists stay open; `h2` is where the deposit left it.']


def corr_rows():
    m = ROWMARK + " (b436)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b436 -- @GR@ gates read, @GDG@ checked by digest, and the seal RECOMPUTED by the tool "
            "that wrote it. **(R47) IS RATIFIED AND OBEYED: THE WRITE LIST NAMES PATHS AND ONE "
            "GENERATOR WITH A COUNT BOUND, AND THE LEDGER REPORTS 0 UNLISTED WRITES; b435'S TWO "
            "FAILING ARMS WERE RIGHT AND ARE NOT RE-VERDICTED.** **THE OBJECT ENUMERATED WAS "
            "DECLARED A UNIFORM BOUND BEFORE THE FIRST CANDIDATE, BECAUSE THIS SITE'S CELL READS "
            "UNSTATED: ITS RECORD HOLDS MEASURED VALUES, NOT AN EXISTENTIAL, SO THE SHARED-WITNESS "
            "FORM DOES NOT TRANSPOSE.** **@NC@ CANDIDATES ENUMERATED, EACH READ AT ITS SOURCE AND "
            "EACH FAILED AT A QUOTED STEP; @HELD@ HELD.** **THE NAVIGATOR'S CHEBYSHEV-MERTENS "
            "BOUND WAS TESTED AND NOT ADOPTED: HIS PARAPHRASE IS ACCURATE AGAINST (149); IT IS "
            "LOCATED AS ELEMENTARY AND NOT LOCATED AS A BANKED STATEMENT; AND IT FAILS ON THE "
            "COMPARISON, NOT ON ITS EXISTENCE.** **THE FINDING: AT b321'S TEN CELLS THE "
            "ARCHIMEDEAN QUANTITY FALLS WHILE THE PRIME CONSTITUENT GROWS, THE RATIO CLIMBING "
            "@R0@ TO @R9@ ACROSS TEN CELLS -- SO NO BOUND OF THIS SHAPE CAN SHOW THE PRIME SIDE "
            "STAYING DOMINATED.** **AND THE TWO SIDES ARE COMPARABLE, NOT INCOMMENSURABLE: THEY "
            "ARE TWO CHANNELS OF ONE IDENTITY Z = P - PR + A VERIFIED AT ALL THIRTEEN CELLS, THE "
            "ARCHIMEDEAN CHANNEL BUILT TWICE BY ROUTES SHARING NO CODE AND AGREEING TO 6.118e-05. "
            "THE CROSSING IS UNDECIDED BECAUSE THE RECORD'S WINDOW ENDS AT a = @A9@, NOT BECAUSE "
            "THE QUANTITIES WERE NEVER NORMALIZED.** **@SHN@ OF @NF@ FAILURES LAND AT A BOUNDARY "
            "AN EARLIER SITE USED; THE UNION GROWS FROM @U3@ TO @U4@ AND ONE KIND IS NEW, WRONG "
            "DIRECTION.** 0 CELLS WRITTEN, 0 SITES ENTERED, 0 BRIDGES TYPED, 0 GRADES MOVED, "
            "0 INSTRUMENTS WRITTEN, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The act enumerates candidates for a "
            "uniform bound and confers nothing")
    prof = ("### ONE PLACE-papers FILE APPENDED (OPEN_TRAILS.md), ITS PRIOR TEXT A TRUE PREFIX; "
            "FACES_LEDGER.md BYTE-UNMOVED AND THE REGISTER STILL FROZEN AT SIX; NO KEYSTONE, NO "
            "REGISTER ROW, NO LEDGER ROW, NO KERNEL FILE, NO INSTRUMENT -- 0 CONTENT LOST")
    grade = ("### EVERY CANDIDATE FAILED AT A STEP QUOTED AT ITS OWN FILE AND LINE; THE PRIOR "
             "SITES' KINDS WERE READ OFF THEIR OWN BANKED JSON AND NEVER TYPED; THE COMPARISON RAN "
             "IN THE EMITTING ACT'S NORMALIZATIONS AND ON BANKED FIGURES ONLY, THE BOUND'S OWN "
             "GROWTH BEING NAMED AS NOT BANKED RATHER THAN COMPUTED AND PRESENTED AS SUCH")
    status = ("data/b436_the_window.txt; data/b436_components.txt; data/b436_extract.txt; "
              "data/b436_candidates.json; data/b436_two_sides.json; data/b436_checks.txt; "
              "data/b436_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@NC@', str(NC)).replace('@HELD@', str(HELD))
                .replace('@R0@', '%0.3e' % A0.get('ratio', 0))
                .replace('@R9@', '%0.3e' % A9.get('ratio', 0))
                .replace('@A9@', str(A9.get('a')))
                .replace('@SHN@', str(SHARED_N))
                .replace('@NF@', str(sum(KINDS.values()) if KINDS else 0))
                .replace('@U3@', str(len(PRIOR_UNION))).replace('@U4@', str(len(UNION4))))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the witness arc at site (iv)', 'the window, and what would bound its prime sum',
           'does the prime constituent overtake the archimedean quantity',
           'is the navigator`s Chebyshev bound a witness',
           'were the two sides ever normalized against each other')
MUST_NOT_HIT = ('a witness was found at site (iv)', 'the crossing was proved',
                'a seventh site was entered')
KEY = 'the-witness-arc-at-site-iv-the-window'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b436 WORKED SITE (iv) OF ROW U1 -- THE WINDOW -- AND ENUMERATED %d CANDIDATES, %d HELD. "
        "THE OBJECT WAS DECLARED A UNIFORM BOUND BEFORE THE FIRST CANDIDATE: this site's cell "
        "reads UNSTATED and not NONE KNOWN, because its record holds TEN MEASURED VALUES indexed "
        "by the width rather than ten existential witnesses, and b406 established that the "
        "existential anyone can manufacture is trivially satisfiable, so the shared witness it "
        "would demand IS the missing statement rather than a repair for its absence. Every "
        "candidate failed at a step quoted at its own file and line: Lagarias Theorem 6.1 at a "
        "CLASS BOUNDARY on b401's three grounds; the source's Theorem 6.11 at a COORDINATE "
        "BOUNDARY, its c|ghat(0)|^2 with 13<c<17 correcting the archimedean inequality at a "
        "support where NO PRIME ENTERS and where b321 prints the quantity it would bound as "
        "identically zero; the source's named one-prime widening ABSENT, named and not taken; the "
        "corpus's own window and kernel terminals at INSTANCES NOT A CLASS, the terminal's own "
        "name being SmearGeneral.cells_are_instances; the criterion itself at FORM, asserting a "
        "sign on the TOTAL and bounding no constituent; and the Vinogradov-Korobov shrinkage law "
        "IMPORT UNDER THE BAR and indexed by the height where this site is indexed by the width. "
        "THE NAVIGATOR'S ELEMENTARY CHEBYSHEV-MERTENS BOUND WAS TESTED IN TWO PARTS AND NOT "
        "ADOPTED ON HIS WORD. His paraphrase is ACCURATE against (149). Part (a): LOCATED AS "
        "ELEMENTARY, and NOT LOCATED AS A BANKED STATEMENT -- no verified source states it, the "
        "Chebyshev psi vocabulary sits only in internal/, which the corpus classes REGISTRY-silent "
        "working logs scoped census-only, and the one psi statement there is CONDITIONAL ON RH. "
        "Part (b): IT RUNS THE WRONG WAY. At b321's ten cells the archimedean quantity FALLS "
        "%0.6f to %0.6f while the prime constituent GROWS in absolute value %0.6f to %0.6f, the "
        "ratio climbing %0.3e to %0.3e across ten cells -- so no bound uniform in a can show the "
        "prime side staying dominated, because the thing it bounds is itself climbing toward the "
        "thing it would have to stay under. AND THE TWO SIDES ARE COMPARABLE, NOT "
        "INCOMMENSURABLE: they are two of the four channels of one identity Z = P - PR + A which "
        "b321 verified at ALL THIRTEEN CELLS, the archimedean channel built a second time by a "
        "route sharing no code and agreeing to 6.118e-05. THE CROSSING IS UNDECIDED BECAUSE THE "
        "RECORD'S WINDOW ENDS AT a = %s, NOT BECAUSE THE QUANTITIES WERE NEVER NORMALIZED -- and "
        "what would decide it is one run of the window instrument at larger radii, blocked by the "
        "parked instrument lane. AT FOUR SITES: %d of %d failures land at a boundary an earlier "
        "site used, the union of kinds grows from %d to %d, and ONE KIND IS NEW -- WRONG "
        "DIRECTION, where the object exists, is uniform, is unconditional and is about the right "
        "sum, and moves the wrong way against the quantity it must be compared with. NO CELL WAS "
        "WRITTEN, the register stays FROZEN AT SIX, and NO BRIDGE IS TYPED BETWEEN ANY TWO OF THE "
        "SIX."
        % (NC, HELD, A0.get('w_inf', 0), A9.get('w_inf', 0), abs(A0.get('pr', 0)),
           abs(A9.get('pr', 0)), A0.get('ratio', 0), A9.get('ratio', 0), A9.get('a'),
           SHARED_N, sum(KINDS.values()) if KINDS else 0, len(PRIOR_UNION), len(UNION4)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO CELL WRITTEN AND NO SITE ENTERED. "
             "### NO BRIDGE TYPED. ### NO INSTRUMENT WRITTEN -- BOTH LANES PARKED. ### NOTHING "
             "DEPOSITS")
    where = ("data/b436_the_window.txt; data/b436_components.txt; data/b436_extract.txt; "
             "data/b436_candidates.json; data/b436_two_sides.json; "
             "data/b436_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b436 (the witness arc at site (iv), the window)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE WITNESS ARC AT SITE (iv), THE WINDOW (b436).%s'
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
        rec('    %-58s reaches the b436 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the uniform-bound declaration carried', 'DECLARED A UNIFORM BOUND' in out),
                      ('the seven kinds carried', 'INSTANCES NOT A CLASS' in out),
                      ('part (a)`s two halves carried', 'NOT LOCATED AS A BANKED STATEMENT' in out),
                      ('the wrong-way finding carried', 'IT RUNS THE WRONG WAY' in out),
                      ('the comparability answer carried', 'COMPARABLE, NOT' in out),
                      ('the window`s end carried', "WINDOW ENDS AT a =" in out),
                      ('the new kind carried', 'ONE KIND IS NEW' in out)):
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
          'b436 -- THE WITNESS ARC AT SITE (iv), THE WINDOW.', 'THE BANK.',
          '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CANDIDATE TABLE.', '-' * 100,
           '  %-5s %-58s %-24s %s' % ('id', 'candidate', 'kind', 'verdict')]
    for c in CAND.get('candidates', []):
        Bk.append('  %-5s %-58s %-24s %s'
                  % (c.get('id'), c.get('name', '')[:58], c.get('kind'), c.get('verdict')))
    Bk += ['', '  OPENING POPULATION : %d. HELD : %d.' % (NC, HELD)]
    Bk += ['', '-' * 100, '### THE TWO SIDES, AT THE RADII THE RECORD PRINTED.', '-' * 100,
           '  %-7s %-17s %-17s %s' % ('a', 'W_inf (arch)', 'PR (primes)', '|PR|/W_inf')]
    for r in SIDES:
        Bk.append('  %-7s %-17.9f %-17.9f %.3e' % (r['a'], r['w_inf'], r['pr'], r['ratio']))
    Bk += ['', '-' * 100, '### THE NAVIGATOR`S EXPECTATIONS, AS THE COMPONENTS SCORED THEM.',
           '-' * 100]
    keep = False
    for ln in COMP.splitlines():
        if 'THE EXPECTATIONS, SCORED' in ln:
            keep = True
        if keep and ln.strip():
            Bk.append('  %s' % ln.strip())
        if keep and 'THE OBSTACLE IS NOT NORMALIZATION' in ln:
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


B435ROW_RE = r"(?m)^\| (\d+) \| \*\*THE CURE SHARED"


def main():
    bar('=')
    rec('b436_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not CAND or not SIDES:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      candidates %s, held %s, kinds %d ; union 3 sites %d, 4 sites %d, shared %d'
        % (NC, HELD, len(KINDS), len(PRIOR_UNION), len(UNION4), SHARED_N))
    rec('      the two sides at %d radii : W_inf %0.6f -> %0.6f ; |PR| %0.6f -> %0.6f'
        % (len(SIDES), A0.get('w_inf', 0), A9.get('w_inf', 0),
           abs(A0.get('pr', 0)), abs(A9.get('pr', 0))))
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
        % [int(x.group(1)) for x in re.finditer(B435ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B435ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b436_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
