# -*- coding: utf-8 -*-
"""b415_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.

### ### **A READ ACT.** ### The corpus writes are one append-only trail block and one appended
### correspondence row. ### The only other write is the memory index, and it is outside every repo.
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
MARK = '<!-- b415 the substrate at grade, the four tuples, and the sibling partition screened -->'
PRIOR = '<!-- b414 the predicate named, and the general clause stated without its proof -->'
BANKOUT = os.path.join(D, 'b415_the_substrate_at_grade.txt')
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


FACE = read(os.path.join(D, 'b415_registration_2026-09-10.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b415_lockgate.json'), encoding='utf-8'))
GR, GDG = LG['gates_read'], LG['face_subject_gates']
COMP = read(os.path.join(D, 'b415_components.txt'))
MEMREC = read(os.path.join(D, 'b415_memory.txt'))
MB = re.search(r'bytes BEFORE  : (\d+)', MEMREC)
MA = re.search(r'bytes AFTER   : (\d+)', MEMREC)
MH = re.search(r'index lines   : (\d+)', MEMREC)
MEMB, MEMA, MEMH = (MB.group(1) if MB else '?'), (MA.group(1) if MA else '?'), \
    (MH.group(1) if MH else '?')

DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane, which this ferry did NOT open.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the substrate’s forcing, at grade', 'CLOSE',
     'READ AT CONTENT. ### **COMPLETE is COMPILED** (`FrobeniusCalibration.g_two_three`, '
     'axiom-free); **FINITE is NAMED and carries no terminal in this keystone**; **PRODUCTIVE is '
     'MIXED BY GARMENT** — `[[7,1,3]]` DERIVES and reaches its target, `4/81` is forced '
     'arithmetic with a **permitted** identification.'),
    ('the ℚ-non-extension’s compilation status', 'CLOSE',
     '**TWO CLAIMS, ONE COMPILED.** ### `element_obstruction` is compiled and axiom-free; **the '
     'dimension-count clause — the one that actually says the substrate does not extend — '
     'carries NO kernel name and is manuscript-resident.** ### A heading that says *at theorem '
     'grade* is not a theorem.'),
    ('the *no other pair* claim’s kind', 'CLOSE',
     '**A MANUSCRIPT ARGUMENT FOR EACH CONJUNCT AND AN ASSERTION FOR THE CONJUNCTION.** ### Each '
     'located sentence gives its reason for ONE property; **no located sentence argues the '
     'conjunction over all three.**'),
    ('the four tuples, derived against stipulated', 'CLOSE',
     '**FROM THE KERNEL’S OWN DECLARATIONS.** ### All four are literal `def`s. ### B, C and D '
     'carry **0** derived components between them — and **class A carries only 2 of 4**: `n₂` '
     'from Ostrowski, `n₃` from the output-stage cardinality, `n₁` and `n₄` stipulated '
     'everywhere. ### **THE RECORD HAS NOT SAID THAT.**'),
    ('the menu’s exactly-four', 'STANDING',
     'ROUTED, unchanged. ### The 2026-06-15 anchor read already records that the four classes '
     'are **defined and shown distinct, but EXACTLY-four is unproven**, and nothing here moves '
     'it.'),
    ('the sibling’s two ratios', 'CLOSE',
     '**BOTH SCREEN AS PERMITTED**, by enumeration and not by opinion: one of **16** and one of '
     '**6** its own shape admits over the same two primitives, with nothing named that selects '
     'it. ### **PERMITTED IS NOT A REFUTATION**, and a second witness is named for each.'),
    ('the S/D experiment', 'STANDING',
     'PRICED AND NOT RUN — **two acts, and the upper end IS nameable here**, unlike (N) at b413, '
     'because both are instrument work the corpus has done before. ### **THE CONTROL MUST COME '
     'FIRST**, and the matched-density randomiser is the part the corpus does NOT bank. ### The '
     'lane stays parked and **the run waits on the author’s word.**'),
    ('the sibling programmes', 'CLOSE',
     '**THERE ARE NONE ON THIS DRIVE.** ### Three passes yield 46, 2 and **0**; every directory '
     'carrying a state document is a module of this programme or a third-party dependency. ### '
     '**SO THE SCREEN RAN AGAINST THE FERRY’S OWN QUOTATION AND NOTHING ELSE**, and no sibling '
     'document was opened because there was none to open.'),
    ('the prime core', 'CLOSE',
     '**SEARCHED BY DESCRIPTION, UNDER A CONTROL THAT HOLDS.** ### The corpus carries exactly one '
     'finite named set of primes with stated inclusion and exclusion criteria, and **it is not '
     'called a prime core — it is called the substrate, and it has a keystone.** ### (E4) is '
     'refuted in premise twice over.'),
    ('the memory index', 'CLOSE',
     '**SHORTENED IN PLACE: %s → %s bytes, %s hooks, 0 removed, 0 failing to resolve, both b387 '
     'hooks present, 0 target files opened for write.**' % (MEMB, MEMA, MEMH)),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING',
     'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### The keystone read here is h2-INDEPENDENT by its own header, '
     'and this act says nothing about h2 in either direction.'),
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
        '### b415 — the substrate at grade, the four tuples, and the sibling’s partition '
        'screened — filed 2026-09-10', '',
        '**A read act.** 0 `.lean` files touched, 0 builds run, 0 terminals added; the instrument '
        'lane stays parked and limb (d) is priced and not run. **Nothing from any sibling '
        'programme is written into any corpus document** — and, as it turns out, nothing could '
        'have been.',
        '',
        '**The substrate’s three selection principles, at grade.** The keystone does not carry '
        '*complete, finite, productive* as a triple; it names three selection principles and '
        'calls their convergence the object’s certificate. **Complete is compiled** — '
        '`FrobeniusCalibration.g_two_three`, axiom-free. **Finite is named** — Størmer, the '
        'Diophantine principle — and carries no terminal in this keystone. **Productive is mixed '
        'by garment**: `[[7,1,3]]` is graded DERIVES and reaches its target; `4/81` is forced '
        'arithmetic with a *permitted* identification, and the keystone says so itself.',
        '',
        '**The ℚ-non-extension is two claims and only one of them is compiled.** The section is '
        'headed *what does not generalize, at theorem grade* — **and a heading is not a '
        'theorem**. `element_obstruction` is compiled and axiom-free, and the keystone names it. '
        'But the clause that actually says the substrate does not extend — the dimension count '
        '`d(K) = 2^(r₁+r₂+2) − 1`, exact, giving 15 at the first real quadratic field — **carries '
        'no kernel name in this keystone and is manuscript-resident.** So the navigator’s (E1) is '
        'met, and met precisely: the two claims are not averaged into one word.',
        '',
        '**And *no other pair satisfies all three* is a manuscript argument for each conjunct and '
        'an assertion for the conjunction.** Searched by description across the live tree with '
        'archive and outputs excluded: the located sentences give reasons — the Frobenius number, '
        'the single unreachable unit — but **each gives its reason for one property at a time, '
        'and none argues the conjunction.**',
        '',
        '**The four tuples, from the kernel’s own declarations rather than from the note that '
        'says so.** `classA ⟨2,3,2,0⟩`, `classB ⟨3,2,2,0⟩`, `classC ⟨3,3,2,0⟩`, `classD '
        '⟨2,2,2,0⟩` — **all four are literal `def`s.** B, C and D carry **0 derived components '
        'between them**, which meets (E2). **And the four-by-four table says what the ferry did '
        'not ask: class A itself carries only two of four.** `n₂ = 3` is derived from Ostrowski’s '
        'classification of the places; `n₃ = 2` from the output-stage cardinality; **`n₁` and '
        '`n₄` are stipulated in every class, including the one the programme rests on.** '
        '`SIDEKernel.formation : 2 + 3 + 2 + 0 = 7` is an arithmetic identity over four numbers, '
        'not a derivation of them. **The right sentence is not *A is derived and B, C, D are '
        'not*; it is *half of A is derived and nothing else is*** — and the record has not said '
        'that. The 2026-06-15 anchor read is quoted beside the measurement as a second witness '
        'and agrees with it; the measurement was taken first.',
        '',
        '**The sibling’s two ratios, screened by enumeration rather than by opinion.** The '
        'standard is the corpus’s own: its structural-fraction closed form has components '
        '*identified rather than fitted* — better than fitted, still not forced — and the cluster '
        'keeps *a pure-mathematical derivation of the 11/12 ceiling* on its own open list. '
        '**The corpus did not grade its own ratio forced.** Against that bar: the amplitude '
        '`(S + D³)/(S + S³)` is **one of 16** expressions its own shape admits over the same two '
        'primitives; the sign rate `(S + D)²/D³` is **one of 6**. Nothing in either claim as '
        'stated selects it from the rest. **Both screen PERMITTED**, so (E3) is met and exceeded, '
        'and the reason is the same for both: **an exponent nobody derived is an exponent '
        'somebody chose.** A second witness is named for each — a count that reaches the '
        'numerator and denominator separately, without writing the ratio down, which is exactly '
        'how {2,3} earned its certificate through three disjoint channels. **And PERMITTED is not '
        'a refutation:** neither ratio is shown false, neither is shown unlikely, and nothing '
        'here says the sibling programme is wrong.',
        '',
        '**There are no sibling programmes on this drive, and the count took three passes to '
        'say so.** The declared test — a directory is a programme if it holds a document stating '
        'its own state — promoted **46 of 56**, of which **43 were `SIDE-*` kernel repositories**, '
        'and found 127 *cross-citations* that were kernel modules naming one another. **A test '
        'that makes every subdirectory of the subject a peer of the subject is counting READMEs.** '
        'The corrected test — does the state document place itself inside PLACE TO STAND — left '
        '**2**. Hand-read, both fall: `PLACE-phase2` carries the federation’s own prefix and sits '
        'beside `PLACE-phase1.5`, which the matcher did classify as a module; '
        '`mathlib4-e960b84-tmp` is a pinned checkout of a third-party library, and **a dependency '
        'is not a sibling**. **46, then 2, then 0 — and all three are printed, because the first '
        'two are facts about the tests.**',
        '',
        '**Which settles something Component 3 needed and the ferry did not ask: the sibling '
        'programme whose ratios were screened is not on this drive.** The screen therefore ran '
        'against the ferry’s own quotation of the two claims and nothing else — exactly what the '
        'order specifies — and **no sibling document was opened, because there was none to open.** '
        'The bar against writing one into the corpus was met by arithmetic, not only by '
        'discipline.',
        '',
        '**The prime core, searched by description under a control that holds.** The description '
        'was fixed in advance — a finite named set of primes with stated inclusion AND exclusion '
        'criteria — and *prime core* was used as a search string and never as a source. **The '
        'control found `{2,3}` in the keystone that owns it.** The population the ferry named for '
        'this search — *in each located document*, of the siblings — is **empty**, and an empty '
        'population is reported as empty rather than as a clean sweep. Run instead over the '
        'population that does exist, the corpus carries **exactly one such set, and it is not '
        'called a prime core: it is called the substrate, and it has a keystone.** The '
        'navigator’s (E4) is **refuted in premise twice**: there is no CHTHONIC state document — '
        'the Chthonic Axioms are a section of this programme’s own `CONVERGENCE.md` — and the '
        'term is not confined anywhere, reaching ten or more documents of this corpus including '
        'an archived `PRIME_CORE_READER.md`. **And no set is reconstructed from anyone’s '
        'recollection.**',
        '',
        '**The S/D experiment, priced and not run.** What the instrument banks: the window '
        '(`SIDE-window`, whose own README figure was already measured stale at b401) and the '
        'prime-sum machinery from b326 onward. **What it does not bank is the matched-density '
        'random-partition control** — and b399 is why that matters, because a control that could '
        'not have produced the failing answer passes **vacuously**. What a run would add: one '
        'number with an error bar, **whose value is entirely in the control and not in the '
        'split** — a split that beats random says the partition carries information, one that '
        'does not says it is decoration, **and either answer is worth the same**, which is the '
        'mark of a test worth running. Two acts, the control first and gated before the split is '
        'ever computed; **and the upper end IS nameable here**, unlike (N) at b413, because both '
        'are instrument work of a kind the corpus has done many times. **The lane is parked, 0 '
        'runs, and the price waits on the author’s word.**',
        '',
        '**And the memory index was shortened in place** — %s → %s bytes, %s hooks, **0 removed, '
        '0 failing to resolve after the write, both hooks b387 recorded as lost checked present, '
        '0 target files opened for write.** Only the hook TEXT was cut, at a word boundary; the '
        'title and the target of every line are untouched, so every link resolves exactly as it '
        'did. The cap was set by the host’s stated load limit and not by taste: **a shortening '
        'that leaves the file above the limit has not solved the problem it was asked to '
        'solve.**' % (MEMB, MEMA, MEMH),
        '',
        '**What this act did not do.** 0 `.lean` files touched, 0 builds run, 0 terminals added. '
        '0 grades moved, conferred or minted. 0 premises discharged. 0 doors restated. 0 routes '
        'proposed. 0 kappa measured. 0 channels opened. 0 rows of `FACES_LEDGER.md` written. 0 '
        'folds run. 0 orientation-layer lines edited. 0 rules struck or amended. 0 locked faces '
        'or prior banks edited. 0 experiment runs. **0 files of any sibling programme written, '
        'edited or quoted into a corpus document, and 0 sibling claims adopted.** 0 deposit '
        'actions and 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A KEYSTONE READ AT GRADE, A FOUR-BY-FOUR TABLE TAKEN FROM "
         "DECLARATIONS, TWO RATIOS SCREENED BY ENUMERATION, AN EXPERIMENT PRICED, AN "
         "ENUMERATION THAT ENDED AT ZERO AND A MEMORY INDEX SHORTENED. ### IT MOVES NO GRADE, "
         "DISCHARGES NO PREMISE, RESTATES NO DOOR, RUNS NO EXPERIMENT, ADOPTS NOTHING FROM ANY "
         "SIBLING PROGRAMME AND COMPILES NOTHING -- AND ITS CENTRAL FINDING IS THAT HALF OF "
         "CLASS A IS DERIVED AND NOTHING ELSE IS")


def corr_rows():
    m = ("**HALF OF CLASS A IS DERIVED AND NOTHING ELSE IS, AND THERE ARE NO SIBLING "
         "PROGRAMMES ON THIS DRIVE** (b415, the substrate at grade)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run "
            "as b415 -- @GR@ gates read, @GDG@ checked by digest; the survey left 0 anchor "
            "misses, one anchor repaired BEFORE the lock. **A READ ACT: 0 .lean files touched, 0 "
            "builds run, 0 terminals added.** **COMPONENT 1: THE THREE SELECTION PRINCIPLES AT "
            "GRADE** -- COMPLETE is COMPILED (FrobeniusCalibration.g_two_three, axiom-free), "
            "FINITE is NAMED with no terminal in this keystone, PRODUCTIVE is MIXED BY GARMENT. "
            "**THE Q-NON-EXTENSION IS TWO CLAIMS AND ONLY ONE IS COMPILED**: element_obstruction "
            "is axiom-free, but the dimension-count clause that actually says the substrate does "
            "not extend **CARRIES NO KERNEL NAME AND IS MANUSCRIPT-RESIDENT** -- **A HEADING THAT "
            "SAYS AT THEOREM GRADE IS NOT A THEOREM**. **AND *NO OTHER PAIR SATISFIES ALL THREE* "
            "IS A MANUSCRIPT ARGUMENT FOR EACH CONJUNCT AND AN ASSERTION FOR THE CONJUNCTION** -- "
            "every located sentence reasons about ONE property. **COMPONENT 2: ALL FOUR TUPLES "
            "ARE LITERAL defs. B, C AND D CARRY 0 DERIVED COMPONENTS BETWEEN THEM, AND CLASS A "
            "CARRIES ONLY 2 OF 4** -- n2 from Ostrowski, n3 from the output-stage cardinality, n1 "
            "and n4 stipulated everywhere. **COMPONENT 3: BOTH SIBLING RATIOS SCREEN AS "
            "PERMITTED**, by enumeration -- one of 16 and one of 6 its own shape admits, nothing "
            "named selecting it; the standard is the corpus's own, which did not grade its "
            "structural fraction forced either. **PERMITTED IS NOT A REFUTATION** and a second "
            "witness is named for each. **COMPONENT 4: THE EXPERIMENT IS PRICED AT TWO ACTS WITH "
            "THE CONTROL FIRST, AND NOT RUN**; the matched-density control is the part the corpus "
            "does NOT bank. **COMPONENT 5: THERE ARE 0 SIBLING PROGRAMMES ON THIS DRIVE** -- "
            "three passes yielding 46, 2 and 0, all printed. **SO THE SCREEN RAN AGAINST THE "
            "FERRY'S OWN QUOTATION AND NO SIBLING DOCUMENT WAS OPENED, BECAUSE THERE WAS NONE TO "
            "OPEN.** The prime core searched by description under a control that holds: the "
            "corpus carries exactly one such set and **IT IS NOT CALLED A PRIME CORE, IT IS "
            "CALLED THE SUBSTRATE**. **COMPONENT 6: THE MEMORY INDEX SHORTENED @MEMB@ -> @MEMA@ "
            "BYTES, @MEMH@ HOOKS, 0 REMOVED, 0 FAILING TO RESOLVE.** 0 GRADES MOVED, 0 PREMISES "
            "DISCHARGED, 0 RUNS, 0 SIBLING CLAIMS ADOPTED, 0 CONTENT LOST")
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED, ADDED, RENAMED OR "
            "RESTATED. ### THE KERNEL WAS READ AND NOT BUILT. ### THE TERMINALS CITED -- "
            "FrobeniusCalibration.g_two_three, element_obstruction, OstrowskiBridge.formation_n2, "
            "CartanBBridge.formation_n_3_eq_two -- ARE CITED AS THEIR OWN DOCUMENTS AND MODULES "
            "NAME THEM, AND THE ACT REPORTS WHICH CLAIMS CARRY A TERMINAL AND WHICH DO NOT. ### "
            "READING A KEYSTONE AT GRADE IS NOT GRADING IT")
    prof = ("### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED, NO GRADE MOVED "
            "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
            "CHANNEL OPENED, NO ROUTE PROPOSED, NO ROW OF FACES_LEDGER WRITTEN, NO FOLD RUN, NO "
            "ORIENTATION-LAYER LINE EDITED, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO "
            "LOCKED FACE OR PRIOR BANK EDITED, NO REGISTRY ROW EDITED, NO EXPERIMENT RUN. ### NO "
            "FILE OF ANY SIBLING PROGRAMME WRITTEN, EDITED OR QUOTED INTO A CORPUS DOCUMENT, AND "
            "NO SIBLING CLAIM ADOPTED. ### THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY PARKED. "
            "### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED "
            "CORRESPONDENCE ROW; THE MEMORY INDEX IS OUTSIDE EVERY REPOSITORY -- 0 CONTENT LOST")
    grade = ("### A KEYSTONE WAS READ AT CONTENT AND ITS HEADING WAS REFUSED THE STATUS OF A "
             "THEOREM. ### A CLAIM GRADED *AT THEOREM GRADE* WAS SPLIT INTO THE PART THAT "
             "COMPILES AND THE PART THAT DOES NOT, RATHER THAN AVERAGED. ### A TABLE WAS TAKEN "
             "FROM DECLARATIONS AND THE NOTE THAT AGREED WITH IT WAS USED AS A SECOND WITNESS "
             "AND NEVER AS THE SOURCE. ### A SCREEN WAS RUN AS AN ENUMERATION SO THAT ITS VERDICT "
             "WOULD BE A COUNT AND NOT AN OPINION, AND ITS *PERMITTED* WAS EXPLICITLY REFUSED THE "
             "STATUS OF A REFUTATION. ### A PROMOTION TEST THAT KEPT NINE TENTHS WAS DISCARDED "
             "WITH ITS YIELD PRINTED, THEN CORRECTED, THEN HAND-READ TO ZERO. ### AN EMPTY "
             "POPULATION WAS REPORTED AS EMPTY RATHER THAN AS A CLEAN SWEEP. ### AND A MEMORY "
             "INDEX WAS SHORTENED WITH EVERY HOOK RESOLVED AFTER THE WRITE RATHER THAN TRUSTED "
             "BEFORE IT")
    status = ("data/b415_the_substrate_at_grade.txt; data/b415_components.txt; "
              "data/b415_extract.txt; data/b415_programmes.txt; data/b415_memory.txt; "
              "data/b415_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b415); tools/b415_extract.py; "
              "tools/b415_regspec.py; tools/b415_reg_gate.py; tools/b415_components.py; "
              "tools/b415_desk_bank.py; tools/b415_checks.py; "
              "PLACE-papers OPEN_TRAILS.md (one append-only block); CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@MEMB@', MEMB).replace('@MEMA@', MEMA).replace('@MEMH@', MEMH))
    return [(sub(m), sub(stmt), sub(term), sub(prof), sub(grade), SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('is the substrate non-extension compiled',
           'which formation tuple components are derived',
           'are the sibling programme ratios forced or permitted',
           'how many sibling programmes are on this drive',
           'what would it cost to run the S D split experiment',
           'does the corpus carry a named finite set of primes')
MUST_NOT_HIT = ('a sibling claim was adopted', 'the experiment was run',
                'the tuples are derived', 'a grade was moved', 'h2 has moved')
KEY = 'the-substrate-at-grade'


def do_key(rownum):
    statement = (
        "b415 READ THE SUBSTRATE AT GRADE AND SCREENED THE SIBLING'S PARTITION. **A READ ACT** -- "
        "0 .lean files touched, 0 builds run, 0 terminals added. **THE THREE SELECTION PRINCIPLES "
        "AT GRADE: COMPLETE IS COMPILED** (FrobeniusCalibration.g_two_three, axiom-free), FINITE "
        "is NAMED and carries no terminal in this keystone, PRODUCTIVE is MIXED BY GARMENT. **THE "
        "NON-EXTENSION IS TWO CLAIMS AND ONLY ONE IS COMPILED**: element_obstruction is axiom-free "
        "and named, but **THE DIMENSION-COUNT CLAUSE THAT ACTUALLY SAYS THE SUBSTRATE DOES NOT "
        "EXTEND CARRIES NO KERNEL NAME AND IS MANUSCRIPT-RESIDENT** -- **A HEADING THAT SAYS AT "
        "THEOREM GRADE IS NOT A THEOREM**. **AND *NO OTHER PAIR SATISFIES ALL THREE* IS A "
        "MANUSCRIPT ARGUMENT FOR EACH CONJUNCT AND AN ASSERTION FOR THE CONJUNCTION.** **ALL FOUR "
        "FORMATION TUPLES ARE LITERAL defs: B, C AND D CARRY 0 DERIVED COMPONENTS BETWEEN THEM, "
        "AND CLASS A CARRIES ONLY 2 OF 4** -- n2 from Ostrowski's classification of the places, n3 "
        "from the output-stage cardinality, **n1 AND n4 STIPULATED IN EVERY CLASS INCLUDING THE "
        "ONE THE PROGRAMME RESTS ON**. SIDEKernel.formation is an arithmetic identity over four "
        "numbers, not a derivation of them, so **THE RIGHT SENTENCE IS HALF OF A IS DERIVED AND "
        "NOTHING ELSE IS**. **BOTH SIBLING RATIOS SCREEN AS PERMITTED, BY ENUMERATION**: the "
        "amplitude is one of 16 and the sign rate one of 6 that their own shapes admit over the "
        "same two primitives, with nothing named that selects them -- **AN EXPONENT NOBODY DERIVED "
        "IS AN EXPONENT SOMEBODY CHOSE**. The standard is the corpus's own, which graded its "
        "structural fraction's components **IDENTIFIED RATHER THAN FITTED** and kept the 11/12 "
        "derivation open. **PERMITTED IS NOT A REFUTATION** and a second witness is named for "
        "each. **THE EXPERIMENT IS PRICED AT TWO ACTS WITH THE CONTROL FIRST AND NOT RUN**; the "
        "matched-density randomiser is the part the corpus does not bank, and b399 is why that "
        "matters. **THERE ARE 0 SIBLING PROGRAMMES ON THIS DRIVE** -- three passes yielding 46, 2 "
        "and 0, all printed, because **A TEST THAT MAKES EVERY SUBDIRECTORY OF THE SUBJECT A PEER "
        "OF THE SUBJECT IS COUNTING READMEs**. **SO THE SCREEN RAN AGAINST THE FERRY'S OWN "
        "QUOTATION AND NO SIBLING DOCUMENT WAS OPENED, BECAUSE THERE WAS NONE TO OPEN.** The prime "
        "core searched by description under a control that holds: **THE CORPUS CARRIES EXACTLY ONE "
        "SUCH SET AND IT IS NOT CALLED A PRIME CORE -- IT IS CALLED THE SUBSTRATE**, and the "
        "Chthonic Axioms are a section of this programme's own CONVERGENCE.md rather than a "
        "sibling's state document. **THE MEMORY INDEX WAS SHORTENED @MEMB@ -> @MEMA@ BYTES, @MEMH@ "
        "HOOKS, 0 REMOVED, 0 FAILING TO RESOLVE AFTER THE WRITE.**")
    grade = (
        "### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED. ### NO GRADE MOVED "
        "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
        "CHANNEL OPENED, NO ROUTE PROPOSED, NO LEDGER ROW WRITTEN, NO FOLD RUN, NO "
        "ORIENTATION-LAYER LINE EDITED, NO RULE STRUCK OR AMENDED, NO LOCKED FACE OR PRIOR BANK "
        "EDITED, NO EXPERIMENT RUN. ### NO FILE OF ANY SIBLING PROGRAMME WRITTEN, EDITED OR "
        "QUOTED INTO A CORPUS DOCUMENT, AND NO SIBLING CLAIM ADOPTED. ### THE INSTRUMENT AND "
        "INSTRUMENT-AUDIT LANES STAY PARKED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED "
        "AT ALL. ### NOTHING WAS COMPILED AND NOTHING WAS PROVED")
    where = (
        "data/b415_the_substrate_at_grade.txt; data/b415_components.txt; data/b415_extract.txt; "
        "data/b415_programmes.txt; data/b415_memory.txt; "
        "data/b415_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b415 -- %d gates read, %d checked by digest); "
        "tools/b415_extract.py; tools/b415_components.py; tools/b415_desk_bank.py; "
        "tools/b415_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GDG, rownum))
    act = ("b415 (the substrate keystone read at grade, the four tuples taken from the kernel's "
           "own declarations, the sibling's two ratios screened by enumeration, the experiment "
           "priced, and the drive's sibling programmes enumerated to zero)")
    statement = (statement.replace('@MEMB@', MEMB).replace('@MEMA@', MEMA)
                 .replace('@MEMH@', MEMH))
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE SUBSTRATE AT GRADE (b415).%s'
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
        rec('    %-58s reaches the b415 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('a read act', 'A READ ACT' in out),
            ('complete is compiled', 'COMPLETE IS COMPILED' in out),
            ('two claims, one compiled', 'TWO CLAIMS AND ONLY ONE IS COMPILED' in out),
            ('a heading is not a theorem', 'IS NOT A THEOREM' in out),
            ('manuscript argument', 'MANUSCRIPT ARGUMENT FOR EACH CONJUNCT' in out),
            ('all four are literal defs', 'ALL FOUR FORMATION TUPLES ARE LITERAL' in out),
            ('B C D zero', 'CARRY 0 DERIVED COMPONENTS BETWEEN THEM' in out),
            ('A only two of four', 'CLASS A CARRIES ONLY 2 OF 4' in out),
            ('half of A', 'HALF OF A IS DERIVED AND NOTHING ELSE IS' in out),
            ('both permitted', 'BOTH SIBLING RATIOS SCREEN AS PERMITTED' in out),
            ('an exponent nobody derived', 'IS AN EXPONENT SOMEBODY CHOSE' in out),
            ('identified not fitted', 'IDENTIFIED RATHER THAN FITTED' in out),
            ('permitted is not refutation', 'PERMITTED IS NOT A REFUTATION' in out),
            ('the experiment priced', 'PRICED AT TWO ACTS WITH THE CONTROL FIRST' in out),
            ('zero siblings', 'THERE ARE 0 SIBLING PROGRAMMES ON THIS DRIVE' in out),
            ('counting READMEs', 'IS COUNTING READMEs' in out),
            ('none to open', 'THERE WAS NONE TO OPEN' in out),
            ('not called a prime core', 'IT IS CALLED THE SUBSTRATE' in out),
            ('the memory index', 'THE MEMORY INDEX WAS SHORTENED' in out)):
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
         'b415 -- THE SUBSTRATE AT GRADE, THE FOUR TUPLES, AND THE SIBLING`S PARTITION SCREENED.',
         'THE BANK. ### LEG 2 OF A TWO-LEG SORTIE.',
         '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
          % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'),
          '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b415_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY AND THE BANK.')
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
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2))
    rec('  lines deleted : 0')
    rec('')
    bar()
    rec('### THE CORRESPONDENCE ROW.')
    bar()
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
    rec('  prior row 263 still present : %s' % ('| 263 |' in read(TABLE)))
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
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### `.lean` FILES TOUCHED : 0. ### BUILDS : 0. '
        '### EXPERIMENT RUNS : 0. ### SIBLING FILES WRITTEN : 0. ### CORR ROW %d. ### KEY %s. '
        '### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b415_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
