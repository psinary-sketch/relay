# -*- coding: utf-8 -*-
"""b413_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.

### ### **THIS ACT WRITES NO `.lean` FILE, NO KEYSTONE SECTION AND NO LEDGER ROW.** ### The kernel
### lane is OPEN and was used to ### **READ**; the corpus writes are one appended trail block and
### one appended correspondence row.
###
### ### **AND THE OWED SENTENCES ARE COUNTED AND LEFT EXACTLY AS THEY STAND.** ### `0` are edited.
### A ferry is the navigator's, and repairing sentences to say what a proof has not established
### would be the header doing the proof's work -- which is the debt itself.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b413 the nearest door read at its edge, and the one named step priced -->'
PRIOR = '<!-- b412 the classification arc folded, the orientation layer brought current -->'
BANKOUT = os.path.join(D, 'b413_the_nearest_door.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def write_bytes(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


SEALTXT = io.open(os.path.join(D, 'b413_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b413_lockgate.json'), encoding='utf-8'))
COMP = io.open(os.path.join(D, 'b413_components.txt'), encoding='utf-8').read()
GR, GDG = LG['gates_read'], LG['face_subject_gates']
UNQ = int(re.search(r'CARRYING NO PER-CELL QUALIFIER : ### `(\d+)`', COMP).group(1))


DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane — which this ferry did NOT open.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the R4 tail', 'CLOSE',
     'STATED EXACTLY, and the word *both* no longer holds: `ExplicitFormulaDecomp` has **SPLIT** '
     '(finite-set conjunct DERIVES since 2026-07-24), `TailBoundPremise` is absent entire. ### '
     'And the row’s own honest boundary: **extending it to all n IS RH.**'),
    ('the threshold N0(T)', 'CLOSE',
     '**IMPORTED UNDER THE BAR**, Voros’s, a BOUND and not an identity. ### And the derived range '
     'and the discriminating range **meet at 2T² and do not overlap**.'),
    ('VAJRA-PLINKO row 1', 'CLOSE',
     'UNCHANGED BY THE ARC — the only arc act named in the document is b409’s head note. ### **And '
     'the row DID move before the arc** (W-ORD-P1-FINSET, 2026-07-24), printed rather than '
     'allowed to make the verdict right by accident.'),
    ('the smallest real step on R4', 'CLOSE',
     'A BUILD — a Mathlib analytic development, owner named as the Mathlib community. ### **And '
     'the OPEN kernel lane does not reach it either**, since it is not a kernel act.'),
    ('(N), the smallest next statement', 'CLOSE',
     'PRICED FOR THE KERNEL. ### **A general conjunct (c) over `2 ≤ p` would be FALSE** and the '
     'counterexamples are printed. ### The right quantifier is **a single prime factor**. ### '
     'b310’s derivation gives the statement’s SHAPE and none of its CONTENT. ### **AT LEAST TWO '
     'ACTS; the upper end is not this seat’s to give.** ### PRICED; NOT BUILT.'),
    ('the owed sentences', 'CLOSE',
     '**COUNTED AT %d, NOT REPAIRED.** ### 0 sentences edited.' % UNQ),
    ('§9’s certificate, named only as *a relay record*', 'STANDING',
     'LOCATED at b411, still ROUTED: naming it is an edit to a keystone’s Correspondence row.'),
    ('the `I-7` collision; the misnamed numbering table', 'STANDING', 'ROUTED.'),
    ('the ten arcs carrying no one-statement', 'STANDING',
     'RESTATED ROUTED. ### b412 recorded the absence; writing them is **not this seat’s, and not '
     'by invention**.'),
    ('the deposited title', 'STANDING',
     'ROUTED AS A THIRD KIND beside the two records failing the currency obligation — it is '
     'neither a stale figure nor an unpropagated label but **a question about what was '
     'deposited**, and it has been open since b145.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX. ### This act adds nothing to it.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### R4 is a door of h2 and this act read it without moving it.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1400), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block(Q):
    return [
        '', MARK, '',
        '### b413 — the nearest door read at its edge, and the one named step priced as a kernel '
        'act — filed 2026-09-10', '',
        '**The kernel lane was named open by this ferry and used to READ.** Every act from b403 to '
        'b412 carried both lanes parked; this one reads `SIDE-global-section` from its own source '
        'rather than from a paper’s description of it. **0 `.lean` files touched, 0 builds run, 0 '
        'terminals added or restated, and every axiom profile taken from the kernel’s own printed '
        'stdout.** The instrument lane and the instrument-audit lane stay parked.',
        '',
        '**The R4 tail, stated exactly — and the word *both* no longer holds of its two premises.** '
        'The K3 freeze of 2026-07-22 graded both `ExplicitFormulaDecomp` and `TailBoundPremise` '
        '*Mathlib-absent-with-ingredient-named*. Two days later `W-ORD-P1-FINSET` was discharged '
        'and **`ExplicitFormulaDecomp` split**: its finite-set conjunct now DERIVES '
        '(`lowFinset_mem_iff`, lv v0.10.0) and only its **decomposition conjunct (Guinand–Weil)** '
        'is absent, while `TailBoundPremise` is absent entire. **So this seat’s (N1) is refuted in '
        'premise and met on other grounds**: they are no longer in the same condition as each '
        'other, and each still has an unmet part with its ingredient named. **And the row carries '
        'its own honest boundary, which settles the pricing before the pricing is reached:** '
        '*extending `TailBoundPremise` to all n **IS** RH.* That is not a difficulty, it is an '
        'identity — the tail is not a hard step toward RH, the tail **is** RH.',
        '',
        '**The threshold is imported under the bar, and it is a bound and not an identity.** '
        '`N₀(T) ≈ 2T²` is Voros’s detection threshold; the record names him at every statement of '
        'it and instructs that it *must be cited as Voros’s*. The corpus neither derived it (it '
        'claims no derivation) nor measured it (the bench measured `λ_n > 0` for n ≤ 130, a '
        'different quantity the record keeps apart). **And the thing worth printing beside the '
        'verdict: the derived range and the discriminating range meet at `2T²` and do not '
        'overlap** — the certificate proves positivity up to precisely where an off-line zero '
        'could first register **and no further**. That is the same number twice, not a near miss.',
        '',
        '**VAJRA-PLINKO row 1 is unchanged by the arc, and the two questions were kept apart.** '
        'The only act of b403–b411 named anywhere in the chart’s document is b409’s '
        'class-numbering head note, which touches no row. **But the row did move — before the arc '
        'began**, when `W-ORD-P1-FINSET` was discharged into it on 2026-07-24. **A row that moved '
        'before the arc did not move because of it**, and an act reporting *row 1 unchanged* '
        'without printing the earlier movement would be right by accident.',
        '',
        '**The smallest real step on R4 is a build, and the open lane does not reach it.** It is '
        'the Bombieri–Lagarias explicit formula and the Voros tail bound **as Mathlib theorems** — '
        'the record prices it itself as *analyst-startable, community-scale* and *a real analytic '
        'development, not a programme sitting*, with the owner named as the Mathlib community. '
        '**It is not a kernel act at all**, so the lane this ferry opened does not reach it '
        'either; the act says which blocker it met rather than filing it behind the nearest park. '
        '**And *this seat cannot* is not *nobody can*** — the chart names a mover and a route, and '
        'both were there before this act.',
        '',
        '**(N) is priced for the kernel, and the price turns on something nobody had measured.** '
        'The seal `B329.finite_side_silence` is a sandwich: **two clauses general in `p` and `n`** '
        '— `index_decomposes` and `scaling_fixes_nothing_off_ball` — around **one conjunct guarded '
        'by a seven-element list**, discharged by **`decide`, seven times**. Every one of them is '
        '**axiom-free**, read from the kernel’s printed stdout. The seal’s own hypothesis is `2 ≤ '
        'p`, and because conjunct (c) is guarded by cell membership **that hypothesis never bites '
        'there**. So this act re-computed the identity outside the kernel on the kernel’s own '
        'definitions, **with the seven decided cells as a positive control — all seven '
        'reproduced** — and then went beyond them. **A general conjunct (c) over `2 ≤ p` would be '
        'FALSE:** it fails at 6, 10, 12, 14, 15, 18, 20, 21, 22 and 26. **And what separates the '
        'cases is not primality** — 4, 8, 9, 16, 25, 27, 32 and 49 are composite and it holds at '
        'every one. The condition is **a single prime factor**, which is exactly when the kernel’s '
        '`units p n`, defined as `u % p != 0`, is the actual unit group of `Z/p^(2n)`; at p = 6 '
        'that filter admits 2, 3 and 4, which are not units mod 36, and the smear breaks. **So the '
        'general statement sits between the two ends the record had: wider than (N) asks for, '
        'narrower than the seal’s own hypothesis.**',
        '',
        '**And b310’s derivation is the statement’s shape and none of its content.** It collapses '
        'the smear to a weight times a count **with primality unused** — but **a derivation that '
        'uses nothing distinguishing 4 from 6 cannot prove a statement true at 4 and false at 6**. '
        'The record’s own grade says the same (`DERIVED-ON-CONTENT`), and the kernel’s own '
        'docstring adds that *the identification with the source’s trace is b310’s derivation and '
        'is not* compiled. **The price:** act 1 states it — define the single-prime-factor '
        'predicate in `Core/` or rule the statement into `Interfaces/` — and that is the only part '
        'this act can size. **Act 2..n proves it, and there the price stops being a number:** the '
        'seven cells are discharged by `decide`, **which generalises to nothing**, so a general '
        'proof is a change of **kind** and not of size. `Core/` has precedent for general proofs '
        '(`valuation_exists`, by strong recursion) but that is one induction on one variable, and '
        'this is a double sum over a filtered range **in vanilla Lean without Mathlib’s Finset '
        'machinery**. **AT LEAST TWO ACTS, AND THE UPPER END IS NOT THIS SEAT’S TO GIVE** — naming '
        'it would require attempting the combinatorial core, **and attempting it is building**. '
        '**A price that invents its own upper bound is not a price, it is a guess with a decimal '
        'point.**',
        '',
        '**The dependencies are two questions and not one.** `Core/FiniteSideSeal.lean` has **no '
        'imports at all**; six files under `Interfaces/` import Mathlib. The arithmetic the proof '
        'would lean on is **already in `Core/`, vanilla and axiom-free** — but **the quantifier’s '
        'own predicate is absent from `Core/` entirely**: there is no prime notion anywhere in it. '
        '**So the navigator’s (N5) is refuted in premise and met on other grounds:** not all the '
        'dependencies are in the kernel, yet it is still Lean work and nothing is imported under '
        'the bar. The choice between defining the predicate and moving the statement to '
        '`Interfaces/` is a design decision about a module’s import surface, **and that is the '
        'author’s**. **And this is a kernel act that no parked lane names** — b398 said *a kernel '
        'act can take (N) as a work order; this act is not one*, and **neither is this one**. '
        'PRICED; NOT BUILT.',
        '',
        '**And the one line the record owes, counted and not repaired.** Across **%d banked '
        'ferries**, **%d sentences** name the finite side, its seal or its compact part, and **%d '
        'carry no per-cell qualifier**. They are not wrong today — each sits in a ferry whose act '
        'carried the qualifier somewhere in its own face or bank — **but the qualification lives '
        'in a different document from the sentence**, and a proof of (N) would make that '
        'separation harmless instead of load-bearing. **0 sentences edited.** A ferry is the '
        'navigator’s, and repairing them to say what a proof has not established would be **the '
        'header doing the proof’s work, which is the debt itself.**'
        % (Q['nferries'], Q['ntot'], UNQ),
        '',
        '**Nothing deposits.** `0` `.lean` files touched, `0` kernel builds, `0` terminals added '
        'or restated, `0` axiom profiles inferred, `0` acts built, `0` grades moved, `0` premises '
        'discharged, `0` doors restated, `0` κ measured, `0` channels opened, `0` routes '
        'proposed, `0` rows of `FACES_LEDGER.md` written, `0` folds run, `0` orientation-layer '
        'lines edited, `0` sentences repaired, `0` rules struck or amended, `0` locked faces '
        'edited, `0` prior banks edited, `0` content lost. The instrument and instrument-audit '
        'lanes stay parked; the wave stays parked. Registration '
        '`data/b413_registration_2026-09-10.txt`, LOCKED before any write at sha256 `%s`, chained '
        'on `tools/b378_lockgate.py` run as b413 — %d gates read, %d checked by digest. Bank: '
        '`relay/data/b413_the_nearest_door.txt`. **h2 where the deposit left it.**'
        % (SEALHASH, GR, GDG),
    ]


SCOPE = ("### THIS ROW RECORDS A READING OF THE KERNEL, A PROVENANCE, A CHART VERDICT AND TWO "
         "PRICES. ### IT TOUCHES NO `.lean` FILE, RUNS NO BUILD, ADDS NO TERMINAL, DISCHARGES NO "
         "PREMISE, RESTATES NO DOOR, REPAIRS NO SENTENCE AND BUILDS NOTHING -- AND ITS CENTRAL "
         "FINDING IS A COUNTEREXAMPLE TO A GENERALISATION NOBODY HAD YET WRITTEN")


def corr_rows(Q):
    m = ("**THE FINITE-SIDE SEAL'S PER-CELL CONJUNCT CANNOT BE GENERALISED OVER ITS OWN "
         "HYPOTHESIS: IT FAILS AT EVERY p WITH TWO DISTINCT PRIME FACTORS, AND WHAT IT NEEDS IS "
         "NOT PRIMALITY** (b413, the nearest door)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b413 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. **THE "
            "KERNEL LANE WAS NAMED OPEN BY THE FERRY AND USED TO READ**: 0 .lean files touched, 0 "
            "builds run, 0 terminals added, every axiom profile from the printed stdout. "
            "**COMPONENT 5: B329.finite_side_silence IS TWO GENERAL CLAUSES AROUND ONE GUARDED BY "
            "A SEVEN-ELEMENT LIST, DISCHARGED BY decide SEVEN TIMES, ALL AXIOM-FREE.** The seal's "
            "hypothesis 2 <= p never bites on the guarded conjunct, so the identity was "
            "re-computed outside the kernel on the kernel's own definitions **WITH THE SEVEN CELLS "
            "AS A POSITIVE CONTROL -- ALL SEVEN REPRODUCED**. **A GENERAL CONJUNCT OVER 2 <= p "
            "WOULD BE FALSE: it fails at 6, 10, 12, 14, 15, 18, 20, 21, 22 and 26. AND THE "
            "SEPARATOR IS NOT PRIMALITY -- 4, 8, 9, 16, 25, 27, 32 and 49 are composite and it "
            "holds at every one. THE CONDITION IS A SINGLE PRIME FACTOR**, exactly when the "
            "kernel's units filter is the actual unit group. **b310'S DERIVATION IS THE "
            "STATEMENT'S SHAPE AND NONE OF ITS CONTENT**: a derivation using nothing that "
            "distinguishes 4 from 6 cannot prove a statement true at 4 and false at 6. **PRICE: AT "
            "LEAST TWO ACTS, UPPER END NOT GIVEN** -- decide generalises to nothing, so the proof "
            "is a change of KIND not of size, and naming its length would require attempting it, "
            "which is building. **Core/ HAS NO IMPORTS AND NO PRIME PREDICATE; Interfaces/ IMPORTS "
            "MATHLIB IN SIX FILES -- so 'in the kernel or in Mathlib' is two questions.** "
            "**COMPONENT 1: ExplicitFormulaDecomp HAS SPLIT** (finite-set conjunct DERIVES since "
            "2026-07-24) while TailBoundPremise is absent entire, and the row's own boundary is "
            "that **extending it to all n IS RH**. **COMPONENT 2: N0(T) = 2T^2 IS IMPORTED UNDER "
            "THE BAR**, Voros's, a bound and not an identity, and the derived and discriminating "
            "ranges MEET AND DO NOT OVERLAP. **COMPONENT 3: VAJRA ROW 1 IS UNCHANGED BY THE ARC** "
            "-- though it moved before it. **COMPONENT 4: THE SMALLEST STEP IS A MATHLIB BUILD AND "
            "THE OPEN KERNEL LANE DOES NOT REACH IT.** **%d SENTENCES IN THE BANKED FERRIES CARRY "
            "NO PER-CELL QUALIFIER -- COUNTED, NOT REPAIRED.** %d .lean FILES TOUCHED, %d BUILDS "
            "RUN, %d ACTS BUILT, %d SENTENCES EDITED, %d CONTENT LOST"
            % (GR, GDG, UNQ, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED, ADDED, RENAMED OR RESTATED. "
            "### THE KERNEL WAS READ AND NOT BUILT: NO `.lean` FILE TOUCHED, NO BUILD RUN. ### THE "
            "FOUR TERMINALS NAMED -- index_decomposes, scaling_fixes_nothing_off_ball, "
            "compact_smear_vanishes_at_cells, finite_side_silence -- ARE CITED AT THEIR PRINTED "
            "AXIOM PROFILES, ALL FOUR AXIOM-FREE, READ FROM THE KERNEL'S OWN STDOUT AND NEVER "
            "INFERRED. ### READING A SEAL IS NOT GENERALISING IT")
    prof = ("### NO `.lean` FILE TOUCHED, NO KERNEL BUILD RUN, NO TERMINAL ADDED OR RESTATED, NO "
            "AXIOM PROFILE INFERRED, NO ACT BUILT, NO GRADE MOVED CONFERRED OR MINTED, NO PREMISE "
            "DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO ROUTE "
            "PROPOSED, NO ROW OF FACES_LEDGER WRITTEN, NO FOLD RUN, NO ORIENTATION-LAYER LINE "
            "EDITED, NO SENTENCE REPAIRED, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO "
            "LOCKED FACE OR PRIOR BANK EDITED. ### THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY "
            "PARKED; ONLY THE KERNEL LANE WAS OPEN AND IT WAS USED TO READ. ### THE CORPUS WRITES "
            "ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A SEAL WAS READ AT ITS OWN SOURCE RATHER THAN FROM A PAPER'S DESCRIPTION OF IT. "
             "### A GENERALISATION WAS TESTED BEFORE IT WAS PROPOSED, AND THE TEST REFUTED THE "
             "OBVIOUS ONE WITH TEN PRINTED COUNTEREXAMPLES UNDER A CONTROL THAT REPRODUCED ALL "
             "SEVEN DECIDED CELLS. ### A DERIVATION WAS GRADED AS THE STATEMENT'S SHAPE AND NOT "
             "ITS CONTENT, BY THE PROPERTY IT DOES NOT MENTION. ### A PRICE WAS GIVEN A FLOOR AND "
             "REFUSED AN UPPER BOUND, BECAUSE NAMING ONE WOULD HAVE REQUIRED BUILDING. ### TWO "
             "EXPECTATIONS WERE SPLIT UNDER (R27) RATHER THAN AVERAGED. ### A ROW WAS REPORTED "
             "UNCHANGED BY THE ARC WITH THE EARLIER MOVEMENT PRINTED, SO THE VERDICT IS NOT RIGHT "
             "BY ACCIDENT. ### AND OWED SENTENCES WERE COUNTED AND LEFT EXACTLY AS THEY STAND")
    status = ("data/b413_the_nearest_door.txt; data/b413_components.txt; data/b413_price.txt; "
              "data/b413_cells.txt; data/b413_extract.txt; "
              "data/b413_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b413); tools/b413_extract.py; "
              "tools/b413_regspec.py; tools/b413_reg_gate.py; tools/b413_components.py; "
              "tools/b413_desk_bank.py; tools/b413_checks.py; PLACE-papers OPEN_TRAILS.md (one "
              "append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('can the finite side seal be generalised',
           'what does the compact part need beyond seven cells',
           'what would it cost to prove (N) in the kernel',
           'where does the 2T squared threshold come from',
           'is the R4 tail still two Mathlib-absent premises',
           'what is the smallest step on the nearest door')
MUST_NOT_HIT = ('a lean file was touched', 'a kernel build was run', 'a premise was discharged',
                'a terminal was added', 'a sentence was repaired')
KEY = 'the-nearest-door'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    statement = (
        "b413 READ THE NEAREST DOOR AT ITS EDGE AND PRICED (N) AS A KERNEL ACT. **THE KERNEL LANE "
        "WAS NAMED OPEN BY THE FERRY AND USED TO READ** -- 0 .lean files touched, 0 builds run, 0 "
        "terminals added, every axiom profile taken from the kernel's own printed stdout. **THE "
        "SEAL B329.finite_side_silence IS TWO CLAUSES GENERAL IN p AND n AROUND ONE GUARDED BY A "
        "SEVEN-ELEMENT LIST, DISCHARGED BY `decide` SEVEN TIMES -- ALL FOUR TERMINALS "
        "AXIOM-FREE.** Because conjunct (c) is guarded by cell membership, **the seal's own "
        "hypothesis `2 <= p` never bites there** -- so the identity was re-computed outside the "
        "kernel on the kernel's own definitions, **WITH THE SEVEN DECIDED CELLS AS A POSITIVE "
        "CONTROL, ALL SEVEN REPRODUCED**. **A GENERAL CONJUNCT (c) OVER `2 <= p` WOULD BE FALSE: "
        "IT FAILS AT 6, 10, 12, 14, 15, 18, 20, 21, 22 AND 26.** **AND THE SEPARATOR IS NOT "
        "PRIMALITY** -- 4, 8, 9, 16, 25, 27, 32 and 49 are composite and the identity holds at "
        "every one. **THE CONDITION IS A SINGLE PRIME FACTOR**, exactly when the kernel's `units p "
        "n` (defined `u % p != 0`) is the actual unit group of Z/p^(2n); at p=6 that filter admits "
        "2, 3 and 4, which are not units mod 36. **SO THE RIGHT GENERAL STATEMENT SITS BETWEEN THE "
        "TWO ENDS THE RECORD HAD: WIDER THAN (N) ASKS FOR, NARROWER THAN THE SEAL'S OWN "
        "HYPOTHESIS.** **b310'S DERIVATION IS THE STATEMENT'S SHAPE AND NONE OF ITS CONTENT**: it "
        "collapses the smear to a weight times a count with primality unused, and **a derivation "
        "using nothing that distinguishes 4 from 6 cannot prove a statement true at 4 and false at "
        "6**. **THE PRICE: AT LEAST TWO ACTS, AND THE UPPER END IS NOT THIS SEAT'S TO GIVE** -- "
        "act 1 states it (define the single-prime-factor predicate in Core/ or rule the statement "
        "into Interfaces/); the proof is a change of KIND and not of size, because `decide` "
        "generalises to nothing. **Core/ HAS NO IMPORTS AND NO PRIME PREDICATE AT ALL; SIX FILES "
        "UNDER Interfaces/ IMPORT MATHLIB -- so 'already in the kernel or in Mathlib' IS TWO "
        "QUESTIONS.** **THIS IS A KERNEL ACT AND NO PARKED LANE NAMES IT. PRICED; NOT BUILT.** "
        "**THE R4 TAIL: ExplicitFormulaDecomp HAS SPLIT** (its finite-set conjunct DERIVES since "
        "2026-07-24) while TailBoundPremise is absent entire, and the row's own honest boundary is "
        "**extending TailBoundPremise to all n IS RH**. **THE THRESHOLD N0(T)=2T^2 IS IMPORTED "
        "UNDER THE BAR** -- Voros's, a BOUND and not an identity -- and **the derived range and "
        "the discriminating range meet at 2T^2 and do not overlap**. **VAJRA-PLINKO ROW 1 IS "
        "UNCHANGED BY THE ARC**, though it moved before it. **THE SMALLEST REAL STEP ON R4 IS A "
        "MATHLIB BUILD, AND THE OPEN KERNEL LANE DOES NOT REACH IT EITHER.** **AND %d SENTENCES "
        "ACROSS THE BANKED FERRIES CARRY NO PER-CELL QUALIFIER -- COUNTED, NOT REPAIRED, 0 "
        "EDITED.**").replace('@UNQ@', str(UNQ))
    # ### **THE STATEMENT QUOTES THE KERNEL'S OWN `u % p != 0`, SO IT CANNOT CARRY A `%`
    # ### FORMAT.** ### Python read the definition as a format spec and refused. ### The count
    # ### is substituted by name instead -- **A STRING THAT QUOTES CODE MUST NOT ALSO BE A
    # ### ### FORMAT STRING.**
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO TERMINAL ADDED RENAMED OR RESTATED, "
        "NO AXIOM PROFILE INFERRED, NO REPOSITORY CLONED. ### NO ACT BUILT, NO GRADE MOVED "
        "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
        "CHANNEL OPENED, NO ROUTE PROPOSED, NO LEDGER ROW WRITTEN, NO FOLD RUN, NO "
        "ORIENTATION-LAYER LINE EDITED, NO SENTENCE REPAIRED, NO RULE STRUCK OR AMENDED, NO "
        "IN-PLACE REPAIR, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE INSTRUMENT AND "
        "INSTRUMENT-AUDIT LANES STAY PARKED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK "
        "AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED "
        "AT ALL. ### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b413_the_nearest_door.txt; data/b413_components.txt; data/b413_price.txt; "
        "data/b413_cells.txt; data/b413_registration_2026-09-10.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b413 -- %d gates read, %d checked by digest); "
        "tools/b413_extract.py; tools/b413_components.py; tools/b413_desk_bank.py; "
        "tools/b413_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GDG, rownum))
    act = ("b413 (the kernel read at its own source, a general conjunct refuted by ten "
           "counterexamples with the seven cells as control, the separator found to be a single "
           "prime factor and not primality, and the Lean act priced at a floor with no upper "
           "bound)")
    row_new = ('    # ### THE NEAREST DOOR (b413).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b413 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the lane was used to read', 'USED TO READ' in out),
            ('the sandwich', 'TWO CLAUSES GENERAL' in out),
            ('seven decides', '`decide` SEVEN TIMES' in out or 'decide` SEVEN TIMES' in out),
            ('the guard never bites', 'never bites there' in out),
            ('the control', 'ALL SEVEN REPRODUCED' in out),
            ('the general would be false', 'WOULD BE FALSE' in out),
            ('the counterexamples', 'FAILS AT 6, 10, 12' in out),
            ('not primality', 'THE SEPARATOR IS NOT PRIMALITY' in out),
            ('a single prime factor', 'A SINGLE PRIME FACTOR' in out),
            ('between the two ends', 'BETWEEN THE TWO ENDS' in out),
            ('shape not content', "SHAPE AND NONE OF ITS CONTENT" in out),
            ('the floor with no ceiling', 'UPPER END IS NOT THIS SEAT' in out),
            ('two questions', 'IS TWO QUESTIONS' in out),
            ('kernel act, no park', 'NO PARKED LANE NAMES IT' in out),
            ('the split premise', 'HAS SPLIT' in out),
            ('the tail is RH', 'IS RH' in out),
            ('imported under the bar', 'IMPORTED UNDER THE BAR' in out),
            ('row 1 unchanged', 'UNCHANGED BY THE ARC' in out),
            ('counted not repaired', 'COUNTED, NOT REPAIRED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    B = []
    BARR, SUBB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BARR)
    A('b413 -- THE NEAREST DOOR READ AT ITS EDGE, AND THE ONE NAMED STEP PRICED AS A KERNEL ACT.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b413_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b413'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (GR, LG['gates_passing'], GDG))
    A(BARR)
    A('')
    A(SUBB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUBB)
    A('### ### ### **THE FINITE-SIDE SEAL`S PER-CELL CONJUNCT CANNOT BE GENERALISED OVER ITS OWN')
    A('### ### ### HYPOTHESIS -- IT FAILS AT EVERY `p` WITH TWO DISTINCT PRIME FACTORS -- AND WHAT')
    A('### ### ### IT NEEDS IS NOT PRIMALITY.**')
    A('### The seal carries `2 ≤ p`, and conjunct (c) is guarded by a seven-element cell list, so')
    A('### ### **THAT HYPOTHESIS NEVER BITES THERE.** ### Re-computed outside the kernel on the')
    A('### kernel`s own definitions, with ### **THE SEVEN DECIDED CELLS AS A POSITIVE CONTROL AND')
    A('### ### ALL SEVEN REPRODUCED**: the identity ### **FAILS AT `6`, `10`, `12`, `14`, `15`,')
    A('### ### `18`, `20`, `21`, `22` AND `26`** ### -- and ### **HOLDS AT `4`, `8`, `9`, `16`,')
    A('### ### `25`, `27`, `32` AND `49`, EVERY ONE OF THEM COMPOSITE.**')
    A('### ### **THE CONDITION IS A SINGLE PRIME FACTOR**, which is exactly when the kernel`s')
    A('### `units p n` -- defined `u % p != 0` -- is the actual unit group of `Z/p^(2n)`. ### At')
    A('### `p = 6` that filter admits `2`, `3` and `4`, which are not units mod `36`, and the')
    A('### smear breaks.')
    A('')
    A(SUBB)
    A('### (2) WHAT THE SEAL IS, READ AT ITS OWN SOURCE.')
    A(SUBB)
    A('### ### **A SANDWICH.** ### `B329.finite_side_silence` carries ### **TWO CLAUSES GENERAL IN')
    A('### ### `p` AND `n`** -- `index_decomposes` and `scaling_fixes_nothing_off_ball` -- around')
    A('### ### **ONE CONJUNCT GUARDED BY A SEVEN-ELEMENT LIST**, discharged by ### **`decide`,')
    A('### ### SEVEN TIMES**, after an `rcases` peels the membership one alternative at a time.')
    A('### ### **AND ALL FOUR TERMINALS ARE AXIOM-FREE**, read from the kernel`s own printed')
    A('### stdout and never inferred.')
    A('### ### **A PER-CELL CONJUNCT SITTING BETWEEN TWO GENERAL ONES IS A DIFFERENT OBJECT FROM A')
    A('### ### PER-CELL THEOREM STANDING ALONE** -- the seal`s generality is real everywhere')
    A('### except the one place `(N)` names.')
    A('')
    A(SUBB)
    A('### (3) b310`S DERIVATION: THE SHAPE, AND NONE OF THE CONTENT.')
    A(SUBB)
    A('### `b310` collapses the smear to a weight times a count ### **WITH PRIMALITY UNUSED.** ###')
    A('### ### **BUT A DERIVATION THAT USES NOTHING DISTINGUISHING `4` FROM `6` CANNOT PROVE A')
    A('### ### STATEMENT TRUE AT `4` AND FALSE AT `6`.** ### It gives the general conjunct its')
    A('### ### **SHAPE** ### and none of its ### **CONTENT**, because the content is exactly the')
    A('### single-prime-factor condition the derivation does not mention.')
    A('### The record`s own grade says the same -- `DERIVED-ON-CONTENT` -- and the kernel`s own')
    A('### docstring adds that *the identification with the source`s trace is b310`s derivation and')
    A('### is not* compiled.')
    A('')
    A(SUBB)
    A('### (4) THE PRICE.')
    A(SUBB)
    A('### ### **ACT 1 -- STATE IT.** ### Define the single-prime-factor predicate in `Core/`, or')
    A('### rule the statement into `Interfaces/`; restate conjunct (c) generally; leave the proof')
    A('### open. ### **BOUNDED, AND THE ONLY PART THIS ACT CAN SIZE.**')
    A('### ### **ACT 2..n -- PROVE IT.** ### The seven cells are discharged by ### **`decide`,')
    A('### ### WHICH GENERALISES TO NOTHING.** ### `Core/` has precedent for general proofs')
    A('### (`valuation_exists`, strong recursion) but that is one induction on one variable, and')
    A('### this is ### **A DOUBLE SUM OVER A FILTERED RANGE, IN VANILLA LEAN, WITHOUT MATHLIB`S')
    A('### ### FINSET MACHINERY.**')
    A('### ### ### **AT LEAST TWO ACTS, AND THE UPPER END IS NOT THIS SEAT`S TO GIVE.** ### Naming')
    A('### it would require attempting the combinatorial core, ### **AND ATTEMPTING IT IS')
    A('### ### BUILDING.** ### **A PRICE THAT INVENTS ITS OWN UPPER BOUND IS NOT A PRICE, IT IS A')
    A('### ### GUESS WITH A DECIMAL POINT.**')
    A('### ### **AND THE DEPENDENCIES ARE TWO QUESTIONS:** ### `Core/FiniteSideSeal.lean` has ###')
    A('### **NO IMPORTS AT ALL** ### and `Core/` has ### **NO PRIME PREDICATE ANYWHERE**; six')
    A('### files under `Interfaces/` import Mathlib. ### The arithmetic is already in `Core/`,')
    A('### vanilla and axiom-free; ### **THE QUANTIFIER`S OWN PREDICATE IS NOT.**')
    A('### ### **THIS IS A KERNEL ACT AND NO PARKED LANE NAMES IT.** ### `PRICED; NOT BUILT.`')
    A('')
    A(SUBB)
    A('### (5) THE DOOR ITSELF.')
    A(SUBB)
    A('### ### **THE TAIL:** ### `ExplicitFormulaDecomp` has ### **SPLIT** ### -- finite-set')
    A('### conjunct DERIVES since 2026-07-24, decomposition conjunct absent -- while')
    A('### `TailBoundPremise` is absent entire. ### And the row`s own boundary: ### **EXTENDING')
    A('### ### `TailBoundPremise` TO ALL `n` ### IS ### RH.** ### Not a difficulty; an identity.')
    A('### ### **THE THRESHOLD:** ### `N0(T) ≈ 2T²` is ### **IMPORTED UNDER THE BAR**, Voros`s, a')
    A('### ### **BOUND AND NOT AN IDENTITY** -- and the derived range and the discriminating range')
    A('### ### **MEET AT `2T²` AND DO NOT OVERLAP.**')
    A('### ### **ROW 1:** ### ### **UNCHANGED BY THE ARC** -- and it moved BEFORE the arc, which')
    A('### is printed so the verdict is not right by accident.')
    A('### ### **THE SMALLEST STEP:** ### ### **A MATHLIB BUILD**, owner the Mathlib community.')
    A('### ### **AND THE OPEN KERNEL LANE DOES NOT REACH IT EITHER** -- it is not a kernel act.')
    A('')
    A(SUBB)
    A('### (6) THE LINE THE RECORD OWES.')
    A(SUBB)
    A('### Across the banked ferries, ### **`%d` SENTENCES NAME THE FINITE SIDE, ITS SEAL OR ITS'
      % Q['ntot'])
    A('### ### COMPACT PART, AND `%d` CARRY NO PER-CELL QUALIFIER.**' % UNQ)
    A('### They are not wrong today -- each sits in a ferry whose act carried the qualifier')
    A('### somewhere in its own face or bank -- ### **BUT THE QUALIFICATION LIVES IN A DIFFERENT')
    A('### ### DOCUMENT FROM THE SENTENCE**, and a proof of `(N)` would make that separation')
    A('### harmless instead of load-bearing.')
    A('### ### **COUNTED, NOT REPAIRED. ### `0` SENTENCES EDITED.** ### A ferry is the navigator`s,')
    A('### and repairing them to say what a proof has not established would be ### **THE HEADER')
    A('### ### DOING THE PROOF`S WORK, WHICH IS THE DEBT ITSELF.**')
    A('')
    A(SUBB)
    A('### (7) WHAT THIS ACT DID NOT DO.')
    A(SUBB)
    A('### `0` `.lean` files touched. ### `0` kernel builds run. ### `0` terminals added, renamed')
    A('### or restated. ### `0` axiom profiles inferred. ### `0` acts built. ### `0` grades moved,')
    A('### conferred or minted. ### `0` premises discharged. ### `0` doors restated. ### `0` κ')
    A('### measured. ### `0` channels opened. ### `0` routes proposed. ### `0` rows of')
    A('### `FACES_LEDGER.md` written. ### `0` folds run. ### `0` orientation-layer lines edited.')
    A('### `0` sentences repaired. ### `0` rules struck or amended. ### `0` in-place repairs. ###')
    A('### `0` locked faces edited. ### `0` prior acts` banks edited. ### `0` platform calls. ###')
    A('### `0` content lost.')
    A('### ### **THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY PARKED. ### THE WAVE STAYS PARKED.')
    A('### ### ### NOTHING DEPOSITS.** ### **AND `h2` IS WHERE THE DEPOSIT LEFT IT** -- `R4` is a')
    A('### door of `h2` and this act read it without moving it.')
    A('')
    A(BARR)
    A('### THE WRITES, BY KIND.')
    A(BARR)
    A('### **KIND 9** -- `OPEN_TRAILS.md` one appended block; `CORRESPONDENCE.md` row `%d`;'
      % rownum)
    A('###   `banked_index.py` key `%s` -- read back %s.' % (KEY, 'PASS' if kok else 'FAIL'))
    A('### ### **AND NOTHING ELSE, OF ANY KIND. ### NO `.lean` FILE, NO KEYSTONE SECTION, NO')
    A('### ### LEDGER ROW, NO ORIENTATION-LAYER LINE, NO FOLD.**')
    A(BARR)
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  ### BANK WRITTEN : %s  (%d lines, %d bytes)' % (os.path.basename(BANKOUT), len(B), n))
    return len(B)


def main():
    rec('=' * 100)
    rec('b413_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.')
    rec('=' * 100)
    rec('  face LOCKED : %s' % SEALHASH)
    nf = len([f for f in os.listdir(D)
              if re.match(r'^b\d+_ferry(_\d{4}-\d\d-\d\d)?\.txt$', f)])
    ntot = int(re.search(r'its compact part : ### \*\*(\d+)\*\*', COMP).group(1))
    rec('  ### owed sentences : %d of %d, across %d banked ferries' % (UNQ, ntot, nf))
    rec('')
    bar()
    rec('  ### THE DESK.')
    bar()
    Q = do_desk()
    Q['nferries'], Q['ntot'] = nf, ntot

    rec()
    bar()
    rec('  ### KIND 9 -- THE TRAIL BLOCK.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the b413 block is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b412 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=NL).write(NL.join(trail_block(Q)) + NL)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            rec('  ### run record : %s' % run_clock.write(D, 'b413_desk_notes', LINES))
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_lane_open': 'named open by this ferry and used to read' in low,
        'says_no_lean': '0 `.lean` files touched' in low,
        # ### **THE BLOCK'S OWN WORDING, NOT A SIBLING'S.** ### It writes
        # ### `**`ExplicitFormulaDecomp` split**`, not *has split* -- b412's lesson,
        # ### met again one act later and caught by the same arm that exists for it.
        'says_split': 'explicitformuladecomp` split' in low,
        'says_tail_is_rh': 'the tail **is** rh' in low,
        'says_imported': 'imported under the bar' in low,
        'says_meet': 'meet at `2t²` and do not overlap' in low,
        'says_row1': 'unchanged by the arc' in low,
        'says_before_arc': 'did not move because of it' in low,
        'says_build': 'is a build' in low,
        'says_not_reach': 'does not reach it' in low,
        'says_sandwich': 'two clauses general in `p` and `n`' in low,
        'says_decide': '`decide`, seven times' in low,
        'says_axiomfree': 'axiom-free' in low,
        'says_guard': 'never bites' in low,
        'says_control': 'all seven reproduced' in low,
        'says_false': 'would be false' in low,
        'says_counter': 'fails at 6, 10, 12' in low,
        'says_notprime': 'not primality' in low,
        'says_single': 'a single prime factor' in low,
        'says_between': 'between the two ends' in low,
        'says_shape': 'shape and none of its content' in low,
        'says_floor': 'upper end is not this seat' in low,
        'says_kind': 'change of **kind** and not of size' in low,
        'says_two_questions': 'two questions and not one' in low,
        'says_authors': 'that is the author' in low,
        'says_no_park': 'no parked lane names' in low,
        'says_counted': 'counted and not repaired' in low,
        'says_zero_edited': '0 sentences edited' in low,
        'says_nothing_deposits': 'nothing deposits' in low,
        'says_h2': 'h2 where the deposit left it' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        rec('  ### run record : %s' % run_clock.write(D, 'b413_desk_notes', LINES))
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS2 = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS2 if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### run record : %s' % run_clock.write(D, 'b413_desk_notes', LINES))
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS2 if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS2)]
        new = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            rec('  ### run record : %s' % run_clock.write(D, 'b413_desk_notes', LINES))
            return 1
        rownum = start

    rec()
    bar()
    rec('  ### THE INDEX KEY.')
    bar()
    kok = do_key(rownum)

    rec()
    bar()
    rec('  ### THE BANK.')
    bar()
    nb = bank_file(Q, rownum, kok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### `.lean` FILES TOUCHED : 0. ### BUILDS RUN : 0. '
        '### SENTENCES EDITED : 0 (of %d counted). ### CORR ROW %d. ### KEY %s. ### BANK %d '
        'LINES.**'
        % (Q['items'], Q['closed'], UNQ, rownum, 'PASS' if kok else 'FAIL', nb))
    bar('=')
    p = run_clock.write(D, 'b413_desk_notes', LINES)
    print(NL + '  ### THIS RUN WROTE : %s   (stamp %s)'
          % (os.path.basename(p), run_clock.read_stamp(p)))
    lp, ls, note = run_clock.latest(D, 'b413_desk_notes')
    print('  ### AND THE GUARD AGREES : %s   (%s ; %s)'
          % (os.path.basename(lp or '-'), ls, note))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
