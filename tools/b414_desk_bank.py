# -*- coding: utf-8 -*-
"""b414_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.

### ### **THIS ACT WRITES LEAN.** ### `b413` could say *0 `.lean` files touched* and be done; this
### one cannot. ### So the writer records what was ADDED and, separately, what was ### **NOT
### ### EDITED** -- and the two are different claims with different evidence.
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
CORE = os.path.join(SIDE, 'Core')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b414 the predicate named, and the general clause stated without its proof -->'
PRIOR = '<!-- b413 the nearest door read at its edge, and the one named step priced -->'
BANKOUT = os.path.join(D, 'b414_the_predicate_named.txt')
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
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


FACE = read(os.path.join(D, 'b414_registration_2026-09-10.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b414_lockgate.json'), encoding='utf-8'))
GR, GDG = LG['gates_read'], LG['face_subject_gates']
COMP = read(os.path.join(D, 'b414_components.txt'))
NEWSRC = read(os.path.join(CORE, 'SinglePrimeFactor.lean'))
NEWCODE = re.sub(r'(?m)--.*$', ' ', re.sub(r'/-.*?-/', ' ', NEWSRC, flags=re.S))
TERMS = re.findall(r'(?m)^theorem\s+(\w+)', NEWCODE)
NT = len(TERMS)
SORTED_ = read(os.path.join(D, 'b414_sorted.txt'))
GA = int(re.search(r'(?m)^GROUP A \((\d+)\)', SORTED_).group(1)) if re.search(r'(?m)^GROUP A \(', SORTED_) else 0
GB = int(re.search(r'(?m)^GROUP B \((\d+)\)', SORTED_).group(1)) if re.search(r'(?m)^GROUP B \(', SORTED_) else 0

DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane — which this ferry did NOT open. ### The kernel lane '
     'is the one that is open, and it does not reach these.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('(N) act 1 — STATE IT', 'CLOSE',
     '**DONE.** ### The predicate `singlePrimeFactor` is compiled in `Core/`, axiom-free, and the '
     'general clause is recorded as a **NAMED OPEN STATEMENT** in the module docstring and the '
     'correspondence row — **never a sorry, and never a `Prop`-valued definition standing in for '
     'a result.** ### The seven cells survive untouched as the instances they are.'),
    ('the module question — `Core/` or `Interfaces/`', 'CLOSE',
     '**RULED BY A BUILD, NOT BY AN OPINION.** ### The ferry’s strikeable ruling fires on its '
     'FIRST limb: the predicate states in the axiom-free module with no Mathlib and an empty '
     'axiom profile. ### **SO THE NAVIGATOR’S (N5) IS REFUTED — AND ITS REASON SURVIVES.**'),
    ('the primitive `Core/` now carries', 'STANDING',
     'NAMED FOR THE AUTHOR, NOT BURIED. ### `Core/` had **no prime notion in any form**; it now '
     'has `isPrime`, by trial division. ### It costs **0 axioms** and it widens the module’s '
     'vocabulary. ### **THE AUTHOR SHOULD SEE IT NAMED RATHER THAN DISCOVER IT.**'),
    ('the seal’s own caveat (T1.4)', 'STANDING',
     'ROUTED, NOT REPAIRED IN PLACE. ### The file says the missing identification holds *exactly '
     'when p is prime*; the identity holds at **8 composite bases in 2..50**. ### **NO `.lean` '
     'FILE’S EXISTING TEXT IS EDITED** — the correction is additive, in the new module and the '
     'correspondence row. ### The author may want the seal’s header annotated; that is an edit to '
     'a sealed file and is **not this seat’s.**'),
    ('the kernel’s affordability frontier', 'CLOSE',
     'MEASURED AND RECORDED. ### Base 10 decides in seconds; base 12 ran **292s** and did not '
     'land. ### **THE CLIFF IS NOT PROPORTIONAL** — 2.1× the work, more than 28× the time — so it '
     'cannot be predicted and had to be measured. ### And the default recursion depth is a **trap '
     'rather than a limit**: an over-budget `decide` yields `sorryAx`, it does not fail cleanly.'),
    ('the owed sentences', 'STANDING',
     '**SORTED, NOT REPAIRED. ### 0 EDITED.** ### Group A %d would become true as written if the '
     'open statement is proved; Group B %d would be untouched by a proof. ### **THEY STAY OWED '
     'UNTIL THE PROOF**, because a sentence made true by a statement nobody has proved is still '
     'not true.' % (GA, GB)),
    ('§9’s certificate, named only as *a relay record*', 'STANDING',
     'LOCATED at b411, still ROUTED: naming it is an edit to a keystone’s Correspondence row.'),
    ('the `I-7` collision; the misnamed numbering table', 'STANDING', 'ROUTED.'),
    ('the ten arcs carrying no one-statement', 'STANDING',
     'ROUTED, restated at b413 and unchanged here.'),
    ('the deposited title', 'STANDING',
     'ROUTED AS A THIRD KIND at b413 and unchanged here — **no corpus edit reaches it.**'),
    ('row U1', 'STANDING', 'FROZEN AT SIX. ### This act adds nothing to it.'),
    ('M-2', 'STANDING', 'OWED and stays owed. ### Stating a clause discharges nothing.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### This act states a clause about a finite-side identity and '
     'says nothing about h2 in either direction.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1600), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    return [
        '', MARK, '',
        '### b414 — the predicate named, and the general clause stated without its proof — '
        'filed 2026-09-10', '',
        '**This act writes Lean.** b413 named the kernel lane open and used it to READ; this leg '
        'builds in it. One new module, `Core/SinglePrimeFactor.lean`, **%d terminals, every one '
        'axiom-free at its printed profile**, and **0 existing `.lean` files edited**. '
        '`FiniteSideSeal.lean` is not touched and `compact_smear_vanishes_at_cells` is neither '
        'restated nor superseded.' % NT,
        '',
        '**The module question was ruled by a build.** The ferry ruled, strikeably: state the '
        'predicate in the axiom-free module if it can be stated there without an import, else '
        'rule it into the interfaces module. **The antecedent is a question of fact and it is '
        'true** — `singlePrimeFactor` compiles in `Core/` with no Mathlib and an empty axiom '
        'profile. **So the navigator’s (N5) is refuted by a build, and its reason survives its '
        'refutation:** it IS a new primitive in a module defined by having none. `Core/` carried '
        'no prime notion in any form — the survey found three declarations whose *name* carries a '
        'prime stem and **not one of them decides primality**. It now carries `isPrime`, by trial '
        'division, at a cost of **0 axioms** and one widening of the module’s vocabulary, **named '
        'here rather than left to be discovered.**',
        '',
        '**The general clause is stated and is not proved.** For every base `p` with '
        '`singlePrimeFactor p = true` and every level `n`, `ballQ p n * sumAN p n = sumAQ p n`. '
        '**It is a NAMED OPEN STATEMENT in the kernel’s own idiom** — prose in the module '
        'docstring plus a correspondence row, **never a sorry** — the idiom found by description '
        'in four sibling `Core/` modules rather than invented here. **It is not compiled as a '
        '`Prop`-valued definition either:** a definition nobody proves reads to a later seat like '
        'a result, and the kernel’s convention keeps open statements off the compiled surface. '
        '**What IS compiled is the hypothesis**, so the open statement has an exact subject '
        'instead of a phrase.',
        '',
        '**And the kernel now refutes the naive generalisation itself, rather than a '
        'transcription of it.** b413 re-computed the identity in Python from these definitions '
        'copied by hand; a transcription is a second implementation and can be wrong in the same '
        'place twice. Here the seven decided cells are re-decided **inside the kernel** as a '
        'positive control, and `6` — which satisfies the seal’s own `2 ≤ p` — is decided to '
        'break the identity, at 468 against 324. **On the other polarity, 4, 8 and 9 are decided '
        'to keep it while being composite.** The predicate’s own verdict is certified at **all '
        'eighteen** of b413’s bases, because trial division is cheap; the identity is certified '
        'only at the subset kernel reduction affords. **Two different reaches, and they are kept '
        'apart.**',
        '',
        '**The frontier was measured, not guessed, and it is sharp.** Base 10 decides in seconds; '
        'base 12 ran **292 seconds** at `maxRecDepth 2000000` and `maxHeartbeats 1000000` and did '
        'not land. **2.1× the work cost more than 28× the time**, so the frontier cannot be '
        'predicted from a work count. **An affordability limit is a property of kernel reduction, '
        'not a result about the arithmetic** — this kernel not deciding 26 says nothing whatever '
        'about 26, which b413 decided in milliseconds. **And the default recursion depth is a '
        'trap rather than a limit:** an over-budget `decide` does not fail cleanly, it yields a '
        'terminal carrying `sorryAx` while the build prints an error. Measured at this act’s own '
        'probe — three of four terminals compiled to `sorryAx` and the fourth was clean, and '
        '**only the printed profile distinguished them.** A green build is not evidence.',
        '',
        '**The seal wrote the error down in advance, and named the wrong condition for it.** '
        '`FiniteSideSeal.lean`’s (T1.4) says a residue `p` does not divide is a unit of `Z/p^k` '
        '*exactly when `p` is prime*, and that this identification is the library’s and is **not '
        'compiled here**. The navigator has entered on the record, in his own words, that '
        '*"primality unused" was carried across twenty ferries as if it licensed generality, when '
        'it was true of the clauses that carry no value and false of the clause that does.* '
        '**These are the same sentence, and neither is false.** The error is not in either '
        'sentence — it is in carrying one across a clause of a different kind, which is (R28) '
        'exactly, written before anyone knew this act would need it. **And the caveat’s own '
        'condition is too strong:** the identity holds at 8 composite bases in 2..50. **It was '
        'exactly right on the seven cells and wrong everywhere else**, which is why it survived '
        'from b329 to here — 85 acts — without a base outside its range ever being tried. **A '
        'caveat sound on its own evidence is not a caveat tested.** No `.lean` file’s existing '
        'text is edited to fix it; the correction is additive.',
        '',
        '**The twenty-eight are sorted and not repaired, and the sort found something the act did '
        'not expect.** Group A %d would become true as written if the open statement is proved; '
        'Group B %d would be left exactly as they are, because what they assert is about '
        'something else — compilation status, scope, the archimedean place, or a plan. **The fact '
        'that decides most of them: the corpus indexes its finite places by primes, and every '
        'prime has a single prime factor.** So the failure at 6 was never a threat to any of '
        'those sentences. **What was always the threat is that the statement was proved at seven '
        'cells.** 0 sentences are edited, in either group.' % (GA, GB),
        '',
        '**The price, re-taken now that the statement exists.** b413 priced (N) at *at least two '
        'acts, upper end not given*, and named act 1 as *state it*. **This is act 1 and it cost '
        'one act**, so the floor is not moved — it is half-discharged, with at least one '
        'remaining. **And the upper end is still not nameable, and the act can now say why with a '
        'measurement instead of a judgement:** the statement’s evidence is a `decide` over a '
        'finite list, and this act measured what extending that list costs. **A proof cannot be '
        'reached by extending the list** — not because the list is long but because **no finite '
        'list is the statement.** The proof needs an argument about `units p n` being the unit '
        'group, which is a change of kind, and naming its length still requires attempting it.',
        '',
        '**What this act did not do.** 0 existing `.lean` files edited. 0 Mathlib imports added. '
        '0 axioms added. 0 sorries, in code or in any printed profile. 0 grades moved, conferred '
        'or minted. 0 premises discharged — **stating a clause is not proving it.** 0 doors '
        'restated. 0 routes proposed. 0 kappa measured. 0 channels opened. 0 rows of '
        '`FACES_LEDGER.md` written. 0 folds run. 0 orientation-layer lines edited. 0 rules struck '
        'or amended. 0 locked faces or prior banks edited. 0 sentences repaired. 0 deposit '
        'actions and 0 platform calls. 0 build artefacts committed — `build/` and `*.olean` are '
        'ignored by the kernel’s own `.gitignore`, read and not assumed. **And h2 where the '
        'deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A PREDICATE COMPILED, A GENERAL CLAUSE STATED AND LEFT OPEN, A "
         "REFUTATION MOVED FROM A TRANSCRIPTION INTO THE KERNEL, AND A FRONTIER MEASURED. ### IT "
         "PROVES NO GENERAL CLAUSE, DISCHARGES NO PREMISE, MOVES NO GRADE, RESTATES NO DOOR, "
         "EDITS NO EXISTING `.lean` FILE AND REPAIRS NO SENTENCE -- AND ITS CENTRAL FINDING IS "
         "THAT THE KERNEL'S OWN HEADER NAMED THE MISSING IDENTIFICATION AND NAMED THE WRONG "
         "CONDITION FOR IT")


def corr_rows():
    m = ("**THE KERNEL'S OWN HEADER NAMED THE MISSING IDENTIFICATION IN ADVANCE AND NAMED THE "
         "WRONG CONDITION FOR IT: THE SEPARATOR IS A SINGLE PRIME FACTOR, NOT PRIMALITY** (b414, "
         "the predicate named)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b414 -- @GR@ gates read, @GDG@ checked by digest; the survey left 0 anchor misses, and "
            "one sentence of the survey's own was found wrong and REPAIRED BEFORE THE LOCK. "
            "**THIS LEG BUILDS IN THE KERNEL.** One new module Core/SinglePrimeFactor.lean, "
            "**@NT@ TERMINALS, EVERY ONE AXIOM-FREE AT ITS PRINTED PROFILE**, and **0 EXISTING "
            ".lean FILES EDITED**. **COMPONENT 1: THE MODULE QUESTION IS RULED BY A BUILD.** The "
            "ferry's strikeable ruling fires on its FIRST limb -- singlePrimeFactor compiles in "
            "the axiom-free module with no Mathlib and an empty profile -- so **(N5) IS REFUTED "
            "BY A BUILD AND ITS REASON SURVIVES**: it IS a new primitive in a module defined by "
            "having none. Core/ carried **NO PRIME NOTION IN ANY FORM**; three declarations carry "
            "a prime stem in their NAME and **not one decides primality**. **COMPONENT 2: THE "
            "GENERAL CLAUSE IS STATED AND NOT PROVED** -- a NAMED OPEN STATEMENT in the kernel's "
            "own idiom, found by description in four sibling modules, **never a sorry and never a "
            "Prop-valued definition standing in for a result**; what is compiled is the "
            "HYPOTHESIS, so the open statement has an exact subject. **COMPONENT 3: THE "
            "REFUTATION IS NOW THE KERNEL'S.** The seven cells are re-decided inside the kernel "
            "as a positive control; 6 satisfies the seal's own 2 <= p and is decided to break the "
            "identity at 468 against 324; 4, 8 and 9 are decided to keep it while composite. The "
            "predicate's verdict is certified at **ALL EIGHTEEN** of b413's bases; the identity "
            "at the subset reduction affords -- **TWO REACHES, KEPT APART**. **THE FRONTIER WAS "
            "MEASURED AND IT IS SHARP**: base 10 decides in seconds, base 12 ran 292s and did not "
            "land, 2.1x the work for more than 28x the time. **AND AN OVER-BUDGET decide YIELDS "
            "sorryAx RATHER THAN FAILING CLEANLY** -- three of four probe terminals did, and only "
            "the printed profile distinguished them. **THE ADDITION: (T1.4) AND THE NAVIGATOR'S "
            "SENTENCE ARE THE SAME SENTENCE, AND NEITHER IS FALSE** -- the error is carrying one "
            "across a clause of a different kind, which is (R28). The caveat is too strong by 8 "
            "composite bases in 2..50 and **EXCLUDES 0 OF THE SEVEN DECIDED CELLS**, which is why "
            "it survived 85 acts. **COMPONENT 4: THE TWENTY-EIGHT SORTED, @GA@ REACHED BY A PROOF "
            "AND @GB@ NOT, 0 EDITED** -- and the fact that decides them is that the corpus indexes "
            "its finite places by PRIMES, so the failure at 6 was never the threat; **the threat "
            "was always that the statement was proved at seven cells**. **COMPONENT 5: ACT 1 COST "
            "ONE ACT; THE FLOOR OF TWO IS HALF-DISCHARGED, NOT MOVED; THE UPPER END IS STILL NOT "
            "THIS SEAT'S TO GIVE** -- no finite list is the statement. 0 GRADES MOVED, 0 PREMISES "
            "DISCHARGED, 0 SENTENCES REPAIRED, 0 CONTENT LOST")
    term = ("### THE TERMINALS THIS ACT ADDS ARE THE @NT@ OF `SinglePrimeFactor`, EACH CITED AT "
            "ITS PRINTED AXIOM PROFILE, **ALL @NT@ AXIOM-FREE**, READ FROM THE KERNEL'S OWN STDOUT "
            "AND NEVER INFERRED. ### NO EXISTING TERMINAL IS ADDED, RENAMED, RESTATED OR "
            "SUPERSEDED; `B329.compact_smear_vanishes_at_cells` STANDS UNTOUCHED AND ITS SEVEN "
            "CELLS SURVIVE AS THE INSTANCES THEY ARE. ### **THE GENERAL CLAUSE IS A NAMED OPEN "
            "STATEMENT AND IS NOT A TERMINAL** -- IT IS CARRIED BY NO SORRY AND BY NO "
            "Prop-VALUED DEFINITION. ### STATING A CLAUSE IS NOT PROVING IT")
    prof = ("### NO EXISTING `.lean` FILE EDITED, NO MATHLIB IMPORT ADDED, NO AXIOM ADDED, NO "
            "SORRY IN CODE OR IN ANY PRINTED PROFILE, NO BUILD ARTEFACT COMMITTED, NO GRADE MOVED "
            "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
            "CHANNEL OPENED, NO ROUTE PROPOSED, NO ROW OF FACES_LEDGER WRITTEN, NO FOLD RUN, NO "
            "ORIENTATION-LAYER LINE EDITED, NO SENTENCE REPAIRED, NO RULE STRUCK OR AMENDED, NO "
            "IN-PLACE REPAIR, NO LOCKED FACE OR PRIOR BANK EDITED, NO REGISTRY ROW EDITED. ### THE "
            "INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY PARKED; THE KERNEL LANE IS THE ONE THAT "
            "WAS OPEN AND IT WAS USED TO BUILD. ### THE WRITES ARE ONE NEW MODULE, AN APPEND TO "
            "AllPrints.lean, THE REGENERATED AXIOM PROFILE, ONE APPEND-ONLY TRAIL BLOCK AND ONE "
            "APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A RULING'S ANTECEDENT WAS SETTLED BY A BUILD RATHER THAN BY AN OPINION, AND THE "
             "EXPECTATION IT REFUTED HAD ITS REASON PRESERVED IN THE SAME BREATH. ### A "
             "GENERALISATION'S REFUTATION WAS MOVED OUT OF A TRANSCRIPTION AND INTO THE KERNEL, "
             "BECAUSE A TRANSCRIPTION IS A SECOND IMPLEMENTATION AND CAN BE WRONG IN THE SAME "
             "PLACE TWICE. ### AN OPEN STATEMENT WAS KEPT OFF THE COMPILED SURFACE IN THE "
             "KERNEL'S OWN IDIOM, FOUND BY DESCRIPTION AND NOT INVENTED. ### A TOOL'S "
             "AFFORDABILITY LIMIT WAS MEASURED AND THEN EXPLICITLY REFUSED THE STATUS OF A RESULT "
             "ABOUT THE ARITHMETIC. ### A TRAP WAS FOUND IN WHICH A FAILING TACTIC YIELDS AN "
             "AXIOM RATHER THAN AN ERROR, AND THE BAR WAS MOVED FROM THE EXIT CODE TO THE PRINTED "
             "PROFILE. ### A NAVIGATOR'S ERROR AND A KERNEL FILE'S CAVEAT WERE FOUND TO BE THE "
             "SAME SENTENCE, AND NEITHER WAS CALLED FALSE. ### AND A CAVEAT WAS SHOWN TO BE "
             "EXACTLY RIGHT ON ITS OWN EVIDENCE AND WRONG OFF IT, WHICH IS WHY IT SURVIVED "
             "EIGHTY-FIVE ACTS")
    status = ("data/b414_the_predicate_named.txt; data/b414_components.txt; data/b414_sorted.txt; "
              "data/b414_ladder.txt; data/b414_extract.txt; data/b414_build.txt; "
              "data/b414_prints_prefix.txt; "
              "data/b414_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b414); tools/b414_extract.py; "
              "tools/b414_regspec.py; tools/b414_reg_gate.py; tools/b414_components.py; "
              "tools/b414_desk_bank.py; tools/b414_checks.py; "
              "SIDE-global-section Core/SinglePrimeFactor.lean (NEW), AllPrints.lean (appended), "
              "AXIOM_PRINTS.txt (regenerated, prior a true byte prefix); "
              "PLACE-papers OPEN_TRAILS.md (one append-only block); CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])
    sub = lambda s: (s.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                     .replace('@NT@', str(NT)).replace('@GA@', str(GA)).replace('@GB@', str(GB)))
    return [(sub(m), sub(stmt), sub(term), sub(prof), sub(grade), SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what condition does the compact smear identity need',
           'is the finite side seal general in p',
           'does Core carry a primality notion',
           'how does the kernel record a statement it has not proved',
           'how far can decide reach on the finite side grid',
           'what did the seal header get wrong about primality')
MUST_NOT_HIT = ('the general clause is proved', 'conjunct c is now general',
                'a premise was discharged', 'M-2 is decided', 'h2 has moved')
KEY = 'the-predicate-named'


def do_key(rownum):
    statement = (
        "b414 STATED THE PREDICATE AND LEFT THE PROOF OPEN. **THIS LEG BUILDS IN THE KERNEL** -- "
        "one new module Core/SinglePrimeFactor.lean with @NT@ terminals, **EVERY ONE AXIOM-FREE AT "
        "ITS PRINTED PROFILE**, and **0 EXISTING .lean FILES EDITED**. **THE MODULE QUESTION WAS "
        "RULED BY A BUILD:** the ferry's strikeable ruling fires on its FIRST limb because "
        "singlePrimeFactor compiles in the axiom-free module with no Mathlib, so the statement "
        "stays in Core/ -- **AND THE NAVIGATOR'S (N5) IS REFUTED WITH ITS REASON INTACT**, since "
        "it IS a new primitive in a module defined by having none. Core/ carried **NO PRIME "
        "NOTION IN ANY FORM**: three declarations carry a prime stem in their NAME and **NOT ONE "
        "DECIDES PRIMALITY**. **THE GENERAL CLAUSE -- for every p with singlePrimeFactor p and "
        "every n, ballQ p n * sumAN p n = sumAQ p n -- IS A NAMED OPEN STATEMENT AND IS NOT "
        "PROVED**, in the kernel's own idiom found by description in four sibling modules: prose "
        "in the docstring plus a correspondence row, **NEVER A SORRY AND NEVER A Prop-VALUED "
        "DEFINITION**. **THE REFUTATION IS NOW THE KERNEL'S RATHER THAN A TRANSCRIPTION'S**: the "
        "seven cells re-decided inside the kernel as a positive control, 6 decided to break the "
        "identity at 468 against 324 while satisfying the seal's own 2 <= p, and 4, 8, 9 decided "
        "to keep it while composite. **THE PREDICATE IS CERTIFIED AT ALL EIGHTEEN OF b413'S "
        "BASES; THE IDENTITY ONLY AT WHAT REDUCTION AFFORDS -- TWO REACHES, KEPT APART.** **THE "
        "FRONTIER IS SHARP AND WAS MEASURED**: base 10 in seconds, base 12 at 292s not landing, "
        "2.1x the work for more than 28x the time. **AN AFFORDABILITY LIMIT IS NOT A RESULT ABOUT "
        "THE ARITHMETIC.** **AND AN OVER-BUDGET decide YIELDS sorryAx INSTEAD OF FAILING** -- so "
        "the bar moved from the exit code to the printed profile. **THE SEAL'S (T1.4) AND THE "
        "NAVIGATOR'S 'primality unused' ARE THE SAME SENTENCE AND NEITHER IS FALSE**: the error "
        "is carrying one across a clause of a different kind, which is (R28). **THE CAVEAT IS TOO "
        "STRONG BY 8 COMPOSITE BASES AND EXCLUDES 0 OF THE SEVEN DECIDED CELLS**, which is why it "
        "survived 85 acts -- **A CAVEAT SOUND ON ITS OWN EVIDENCE IS NOT A CAVEAT TESTED**. **THE "
        "TWENTY-EIGHT ARE SORTED, @GA@ REACHED BY A PROOF AND @GB@ NOT, 0 EDITED**, and the fact "
        "that decides them is that **THE CORPUS INDEXES ITS FINITE PLACES BY PRIMES**, so the "
        "failure at 6 was never the threat -- **THE THREAT WAS ALWAYS THAT THE STATEMENT WAS "
        "PROVED AT SEVEN CELLS**. **ACT 1 COST ONE ACT: THE FLOOR OF TWO IS HALF-DISCHARGED, NOT "
        "MOVED, AND THE UPPER END IS STILL NOT THIS SEAT'S TO GIVE** -- **NO FINITE LIST IS THE "
        "STATEMENT**.")
    grade = (
        "### NO EXISTING `.lean` FILE EDITED, NO MATHLIB IMPORT ADDED, NO AXIOM ADDED, NO SORRY IN "
        "CODE OR PROFILE, NO BUILD ARTEFACT COMMITTED. ### NO GRADE MOVED CONFERRED OR MINTED, NO "
        "PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO ROUTE "
        "PROPOSED, NO LEDGER ROW WRITTEN, NO FOLD RUN, NO ORIENTATION-LAYER LINE EDITED, NO "
        "SENTENCE REPAIRED, NO RULE STRUCK OR AMENDED, NO LOCKED FACE OR PRIOR BANK EDITED. ### "
        "THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY PARKED. ### NOTHING DEPOSITS AND THE "
        "PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE IS STATED AND HAS NOT BEEN PROVED")
    where = (
        "data/b414_the_predicate_named.txt; data/b414_components.txt; data/b414_sorted.txt; "
        "data/b414_ladder.txt; data/b414_registration_2026-09-10.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b414 -- %d gates read, %d checked by digest); "
        "tools/b414_extract.py; tools/b414_components.py; tools/b414_desk_bank.py; "
        "tools/b414_checks.py; SIDE-global-section Core/SinglePrimeFactor.lean; "
        "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = ("b414 (the single-prime-factor predicate compiled in the axiom-free module, the general "
           "clause stated as a named open statement and not proved, the refutation moved into the "
           "kernel, and the kernel's own caveat found to name the wrong condition)")
    statement = (statement.replace('@NT@', str(NT)).replace('@GA@', str(GA))
                 .replace('@GB@', str(GB)))
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE PREDICATE NAMED (b414).%s'
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
        rec('    %-58s reaches the b414 key : %s' % (qq[:58], g2))
    # ### **A NEEDLE MUST BE IN THE WORDING THE ARTEFACT USES.** ### These are checked against
    # ### the statement string above, not against a sibling's phrasing.
    for lbl, cond in (
            ('the leg builds', 'THIS LEG BUILDS IN THE KERNEL' in out),
            ('terminals axiom-free', 'EVERY ONE AXIOM-FREE AT' in out),
            ('nothing existing edited', '0 EXISTING .lean FILES EDITED' in out),
            ('ruled by a build', 'RULED BY A BUILD' in out),
            ('(N5) refuted, reason intact', "(N5) IS REFUTED WITH ITS REASON INTACT" in out),
            ('Core had no prime notion', 'NO PRIME NOTION IN ANY FORM' in out),
            ('a name is not a notion', 'NOT ONE DECIDES PRIMALITY' in out),
            ('the open statement', 'IS A NAMED OPEN STATEMENT AND IS NOT' in out),
            ('never a sorry', 'NEVER A SORRY AND NEVER A Prop-VALUED' in out),
            ('the kernel refutes it now', "THE REFUTATION IS NOW THE KERNEL'S" in out),
            ('two reaches kept apart', 'TWO REACHES, KEPT APART' in out),
            ('the frontier', 'THE FRONTIER IS SHARP AND WAS MEASURED' in out),
            ('affordability is not a result', 'NOT A RESULT ABOUT' in out),
            ('the sorryAx trap', 'YIELDS sorryAx INSTEAD OF FAILING' in out),
            ('the same sentence', 'THE SAME SENTENCE AND NEITHER IS FALSE' in out),
            ('the caveat too strong', 'TOO STRONG BY 8 COMPOSITE BASES' in out),
            ('sound on its own evidence', 'IS NOT A CAVEAT TESTED' in out),
            ('places indexed by primes', 'INDEXES ITS FINITE PLACES BY PRIMES' in out),
            ('the real threat', 'PROVED AT SEVEN CELLS' in out),
            ('the floor half-discharged', 'HALF-DISCHARGED, NOT' in out),
            ('no finite list', 'NO FINITE LIST IS THE STATEMENT' in out)):
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
    B = ['=' * 100,
         'b414 -- THE PREDICATE NAMED, AND THE GENERAL CLAUSE STATED WITHOUT ITS PROOF.',
         'THE BANK. ### LEG 1 OF A TWO-LEG SORTIE.',
         '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
          % (Q['items'], Q['closed'], Q['standing'])]
    B += ['', '-' * 100, '### THE KERNEL TERMINALS THIS ACT ADDS, AT THEIR PRINTED PROFILES.',
          '-' * 100]
    prints = read(os.path.join(SIDE, 'AXIOM_PRINTS.txt'))
    for t in TERMS:
        line = ''
        for ln in prints.splitlines():
            if ("'SinglePrimeFactor.%s'" % t) in ln:
                line = ln.strip()
                break
        B.append('  %-44s %s' % (t, line or '### NOT PRINTED'))
    B += ['', '  TERMINALS : %d. ### CORRESPONDENCE ROW : %d. ### KEY : %s.'
          % (NT, rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)'
        % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b414_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.')
    bar('=')
    rec('')
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    rec('')
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
        added = 0
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        added = len(t2.splitlines()) - before
        rec('  appended %d lines; prior mark still present : %s' % (added, PRIOR in t2))
    rec('  lines deleted : 0')
    rec('')
    bar()
    rec('### THE CORRESPONDENCE ROW.')
    bar()
    # ### **NO DEFENSIVE `hasattr`.** ### A first draft guarded this call with one, and because
    # ### the module has no such function the guard turned a HARD FAILURE INTO A SILENT NO-OP --
    # ### the row was never written and the act reported the PREVIOUS row number as its own.
    # ### ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM**, and a writer that cannot fail is worse.
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    slip = [mm for mm, s2, _t, _p, _g, _sc, _st in ROWS2 if not s2.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
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
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    rec('  prior row 262 still present : %s' % ('| 262 |' in read(TABLE)))
    rec('')
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    rec('')
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok)
    rec('')
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### NEW .lean MODULES : 1. ### TERMINALS : %d. '
        '### EXISTING .lean FILES EDITED : 0. ### SENTENCES EDITED : 0. ### CORR ROW %d. '
        '### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], NT, rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b414_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
