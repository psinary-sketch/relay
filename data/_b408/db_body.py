DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('W-ORD-E0-RANK-PROPAGATION', 'STANDING', 'No grade moves in this act.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the keystone’s widened no-Mathlib claim; SIDE-effects’ absent printed profile',
     'STANDING', 'ROUTED at b404. ### Nothing is built here.'),
    ('the row’s restatement into residue form', 'STANDING',
     'ROUTED at b404, MEASURED at b405, and still not applied.'),
    ('the shape-to-instance route', 'STANDING',
     'PRICED at b405, and b407 added the reason it stays untaken. ### b408 adds a second: even '
     'the writing b407 named would produce a CONDITIONAL, which the lemma does not quantify over '
     'either.'),
    ('the fold', 'CLOSE',
     'NOT DUE. ### The tool counts the span at 6 against (R1)’s threshold of 9 -- THREE SHORT. '
     '### This act proposes no fold and the arithmetic is printed.'),
    ('whether the other two channels have been examined', 'CLOSE',
     'ANSWERED. ### C3 examined ONCE, inside the barrier keystone itself, as T1 of the Tier-1 '
     'toolkit, with Theorem 3.7’s negative result. ### **C4 ABSENT: 7 hits, all hand-read, 0 '
     'examinations** -- and the barrier’s own toolkit does not name it either.'),
    ('the two class numberings', 'STANDING',
     'FOUND AND PRINTED, NOT RECONCILED. ### The corpus carries two schemes that disagree on six '
     'of seven symbols, and the sweep’s two most promising hits are artefacts of it. ### '
     'ROUTED to the author: a reconciliation is a corpus-wide act.'),
    ('the reduction as a classified proof', 'CLOSE',
     'PRICED AND NOT WRITTEN. ### 4 distinct imported premises, none dischargeable by the corpus, '
     'so the result is a PROOF-WITH-HYPOTHESES. ### And a second finding: it would prove a '
     'CONDITIONAL, which Theorem 3.1 does not quantify over -- so the work would still not make '
     'the theorem apply.'),
    ('the four dresses', 'CLOSE',
     'ONE STATEMENT, with the instantiation printed for each. ### 3 independent instances and 1 '
     'restatement. ### The record has no name for it and **THE NAMING IS ROUTED, NOT MINTED.**'),
    ('what kind of instrument row U1 is', 'CLOSE',
     'A BOOKKEEPING ONE, by the banks’ own numbers: 6 sites, 2 coordinates, 0 bridges, 0 grades, '
     '**0 statements about the object**. ### A description, not a demotion.'),
    ('the routed prices', 'STANDING',
     'LISTED IN ONE PLACE for the first time: 2 ROUTED and 1 NAMED-NOT-ROUTED. ### All three stay '
     'with the author or with the research; b408 discharges none.'),
    ('the suite’s growth', 'STANDING',
     'MEASURED AND NOT REFORMED. ### A standing core of 8 arms, none of them about the '
     'mathematics; carry-forward 13%, 45%, 48% -- never half.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT. ### No claim in either direction.'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES FIVE ITEMS AND LEAVES THE REST STANDING.**')
    rec('')
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1200), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b408 — the other two channels, the reduction as a classified proof priced, and the '
        'span counted — filed 2026-09-10',
        '',
        '**Of the three sources Corollary 3.6’s existential ranges over, one has been examined '
        'once and one has never been examined at all.** `C₃` is *"the Γ-factor transformation '
        'under s ↦ 1−s produces the functional equation ξ(s) = ξ(1−s)"*; `C₄` is *"the modular '
        'symmetry group PSL₂(ℤ) ≅ ℤ/2 ∗ ℤ/3 encodes how archimedean and multiplicative places fit '
        'together"* — **and `C₄` is the only one of the three that is itself a relation between '
        'the other two, which is what Definition 2.2 asks an interface to be.** The sweep ran over '
        '`4705` files, the whole live papers tree and every banked relay record, on a predicate '
        'fixed before it: a line naming the class beside one of the corollary’s own channel words. '
        '**`C₃`: 19 hits. `C₄`: 7 hits. Every one hand-read, because a permissive filter’s count '
        'is not a finding.** `C₃` is examined **once, inside the barrier keystone itself**, as `T1` '
        'of the Tier-1 toolkit, where Theorem 3.7 concludes no `T`-derivation establishes `P`. '
        '**`C₄` is ABSENT: zero examinations anywhere** — one hit is this session’s own block, one '
        'is a numbering artefact, the rest name the class in passing. **And the barrier’s own '
        'toolkit does not name `C₄` either: not included, not excluded, not mentioned.** No claim '
        'is made that either channel is open, promising, or worth opening; **an unasked question '
        'is not an opportunity until someone prices it.**',
        '',
        '**And the sweep’s real finding is a hazard the corpus carries and tabulates itself: TWO '
        'CLASS NUMBERINGS that disagree on six of seven symbols.** The classes document’s own '
        'remark gives the correspondence — *C₃ | C₁ | Archimedean / functional equation*, *C₄ | '
        'C₅ | Global / PSL₂ symmetry* — and only `C₇` means the same thing in both. `C₃` is a '
        'TRANSFORMATION-stage class in the paper’s numbering, so a document calling `C₃` an '
        '**output-stage** class is using the monograph’s, where `C₃` is *Local / Cauchy–Riemann*. '
        '**The two most promising hits in the entire sweep — `PATHS_TO_THE_CRITICAL_LINE:107` and '
        '`CRITICAL_RESOLVE:1121`, both reading *output-stage classes (C₃ + C₇) … assembling '
        'without crossing a dark interface* — use the corollary’s vocabulary exactly and are about '
        'a different class.** **A SYMBOL MATCHED ACROSS DOCUMENTS WITH DIFFERENT NUMBERINGS IS A '
        'MATCHER ARTEFACT, NOT AN EXAMINATION.** The hazard is printed and **not reconciled**: a '
        'reconciliation is a corpus-wide act and is routed to the author.',
        '',
        '**The reduction written as a first-order proof with every step classified is priced, and '
        'the price has a second surprise in it.** Of the E0 gate’s eight constituents: `1` is '
        'writable as a step and only at seven cells (`K3`, whose compact part is per-cell); `1` is '
        'a MEASUREMENT and not a step at all (`K5`); `1` is the conclusion (`K8`, UNOWNED); and '
        'the rest carry **four distinct imported premises** — the source’s Definition 3.1, '
        'Proposition C.1, the local term (149), and Theorem 4.7. **All four are the source’s '
        'theorems and the corpus has derived none of them**, which is precisely what importing '
        '*under the bar* means. So each must be **stated as a hypothesis**, and what gets written '
        'is `H ⟹ ∀x P(x)`: **A PROOF-WITH-HYPOTHESES, NOT A PROOF IN THE LEMMA’S SENSE.** **AND '
        'THEN THE SECOND FINDING: Theorem 3.1 is stated about proofs of the universal statement, '
        'and a proof of a CONDITIONAL is not one.** So doing the work `b407` named would produce '
        'an object the lemma STILL does not quantify over — it would need the lemma restated for '
        'conditional conclusions, **a second thing nobody has written**. A second layer is printed '
        'and marked **UNCHECKED**: an import the corpus has not derived may still be a consequence '
        'of the specification, in which case the obstacle is labour and not logic — but whether '
        'each import is first-order expressible over `S` is a question nobody has asked and this '
        'act does not answer. **Priced and not written: 0 lines.**',
        '',
        '**The span is 6 and the threshold is 9, so the fold is not due and this act proposes '
        'none.** The tool was run read-only, its count taken from its own output and not typed, '
        'and the arithmetic is printed rather than dressed as a judgement — **three acts short**.',
        '',
        '**The four dresses are ONE statement, and the sentence is stated without being named.** '
        '*A result applies to an object only if the object is of the kind the result quantifies '
        'over.* Instantiated: b405’s countermodel quantifies over couplings on `ℝ → ℂ` and a row '
        'site is not one; b406’s shared-witness form quantifies over `∀∃ ⟹ ∃∀` statements and '
        '`(i)` has no inner existential while `(iv)`’s is trivially satisfiable; b407’s Theorem '
        '3.1 quantifies over formal first-order proofs and the reduction is not one. **The fourth '
        'is a RESTATEMENT of the third — the exactness of a resemblance does not change what kind '
        'the object is — so four occurrences are three independent instances and one restatement, '
        'and the act says so rather than banking a larger number.** The record has no name for it: '
        'the index returns `NO KEY` on its verdict line for all three queries, and the only near '
        'thing is a *category error* used of a normalisation convention. **THE NAMING IS ROUTED TO '
        'THE AUTHOR. STATING THE SENTENCE THE TEST PRODUCES IS NOT MINTING; GIVING IT A NAME IS.**',
        '',
        '**Row `U1` is a bookkeeping instrument, by the banks’ own numbers.** It is now `19308` '
        'bytes — the largest single row in the ledger — with `6` sites entered, `2` coordinates '
        'added, `1` price corrected, `0` bridges typed, `0` grades conferred, and **`0` statements '
        'about the object**. Every yield is a classification of what the record already held: '
        'which sites resemble which, in what kind a site is empty, whether a witness form applies. '
        '**Not one entry produced a statement about `ξ`, about the Epstein object, or about any '
        'zero.** **And that is a description and not a demotion** — a bookkeeping instrument that '
        'has held a refusal intact through six entries, caught an over-count and forced two '
        'coordinates into existence has earned its place. What would change it: a site whose entry '
        'produced a statement about the OBJECT rather than about the record. **None of the six '
        'has.**',
        '',
        '**THE ROUTED PRICES, IN ONE PLACE FOR THE FIRST TIME — item, act, cost, whose call.** '
        '**(1)** *every write encodes before it opens* — b406 — ROUTED — costs nothing but the '
        'author’s word, and the cost of NOT promoting it is that each ferry must restate it — THE '
        'AUTHOR. **(2)** `(R20)`’s limb 2, *a kernel deposits when a published claim cites its '
        'terminals* — b407 — ROUTED — costs the rule’s own claim about itself, since it says it is '
        '*descriptive before it is prescriptive* and *discovered, not imposed* — THE AUTHOR. '
        '**(3)** the Tier-2 form of the barrier — b407 — **NAMED, NOT ROUTED** — costs open '
        'mathematics; the document calls it *research-frontier and not claimed here*; not a build '
        'and not blocked by the parked lane — NOBODY YET, it is a research question and not a '
        'decision. **So the count is 2 ROUTED and 1 NAMED, which is three items and not three '
        'routings**, and the two dispositions are kept apart. **The list declares its own scope: '
        'it is built from the three acts the ferry names and is not a corpus-wide routed-item '
        'census.**',
        '',
        '**And the gate suite has no standing core worth the name.** Across b404, b405, b406 and '
        'b407 the suites ran 34, 62, 64 and 61 arms; **only 8 arms appear in all four** — '
        '`G-CAP`, `G-FERRY`, `G-KEY`, `G-MUSTFAIL`, `G-MUSTFAIL-CTL`, `G-NOBRIDGE`, `G-SEAL`, '
        '`G-WRITELIST` — **and every one of the eight is an APPARATUS arm: the ferry, the seal, '
        'the key, the write list, the cap, the must-fail fixture. Not one is about the '
        'mathematics.** Carry-forward runs 13%, then 45%, then 48% — **never half**. The suite is '
        'built new each act around a small fixed spine, and that is what the numbers say whether '
        'or not it is what anyone intended. **The measure’s own limit is printed: this counts arm '
        'NAMES, and an arm carried forward by name may have been rewritten inside** — `G-KEY` was '
        'rebuilt at b406 after b405’s substring failure and counts as carried in both — **so 48% '
        'is an upper bound on continuity, not a measurement of it.** **Measured and not reformed: '
        '0 arms added, removed, renamed or promoted.**',
        '',
        '**Nothing deposits.** `0` folds run, `0` rows of `FACES_LEDGER.md` written, `0` in-place '
        'repairs, `0` coordinates added, `0` names minted, `0` rules widened, `0` numbering '
        'schemes reconciled, `0` arms reformed, `0` grades moved, `0` bridges typed, `0` kernels '
        'built, `0` `.lean` files touched, `0` content lost. Both lanes stay parked and the wave '
        'stays parked. Registration `data/b408_registration_2026-09-10.txt`, LOCKED before any '
        'write at sha256 `%s`, chained on `tools/b378_lockgate.py` run as b408 — %d gates read, '
        '%d checked by digest. Bank: `relay/data/b408_the_other_two_channels.txt`. **h2 where the '
        'deposit left it.**'
        % (SEALHASH, LG['gates_read'], LG['face_subject_gates']),
    ]


SCOPE = ("### THIS ROW RECORDS A SEARCH THAT RETURNED ABSENT, A PRICE, AN ARITHMETIC AND FOUR "
         "MEASUREMENTS. ### IT CERTIFIES NO EQUIVALENCE, OPENS NO TERMINAL, MOVES NO GRADE, MINTS "
         "NO NAME, RECONCILES NO NUMBERING AND TYPES NO BRIDGE")


def corr_rows(Q):
    m = ("**ONE OF THE THREE SOURCES A CLOSING PROOF MUST TOUCH HAS NEVER BEEN EXAMINED AS A "
         "CHANNEL BY ANY ACT, KEYSTONE OR LEDGER ROW -- AND THE BARRIER'S OWN TOOLKIT DOES NOT "
         "NAME IT EITHER** (b408, the other two channels)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b408 -- %d gates read, %d checked by digest; the survey left 0 anchor misses. "
            "**ADDITION THREE**: C3 is the Gamma-factor/functional-equation class and C4 the "
            "modular-symmetry class that relates the other two. A sweep over 4705 files on a "
            "predicate fixed in advance returned 19 hits for C3 and 7 for C4; EVERY HIT WAS "
            "HAND-READ. **C3 IS EXAMINED ONCE, INSIDE THE BARRIER KEYSTONE ITSELF, AS T1 OF THE "
            "TIER-1 TOOLKIT, WITH THEOREM 3.7'S NEGATIVE RESULT. C4 IS ABSENT: 0 EXAMINATIONS "
            "ANYWHERE**, and T does not name it -- not included, not excluded, not mentioned. **AND "
            "THE SWEEP'S REAL FINDING IS A HAZARD: THE CORPUS CARRIES TWO CLASS NUMBERINGS THAT "
            "DISAGREE ON SIX OF SEVEN SYMBOLS**, and the two most promising hits use the "
            "corollary's vocabulary exactly while meaning a different class. PRINTED, NOT "
            "RECONCILED. **ADDITION FOUR**: the reduction written as a classified proof is a "
            "PROOF-WITH-HYPOTHESES -- 4 distinct imported premises, all the source's theorems, none "
            "dischargeable by the corpus -- **AND IT WOULD PROVE A CONDITIONAL, WHICH THEOREM 3.1 "
            "DOES NOT QUANTIFY OVER, SO THE WORK WOULD STILL NOT MAKE THE THEOREM APPLY.** A second "
            "layer is marked UNCHECKED. **COMPONENT 1: THE SPAN IS 6 AGAINST A THRESHOLD OF 9; THE "
            "FOLD IS NOT DUE AND NONE IS PROPOSED.** **COMPONENT 2: the four dresses are ONE "
            "STATEMENT** -- a result applies to an object only if the object is of the kind the "
            "result quantifies over -- with 3 independent instances and 1 restatement; the record "
            "has no name and THE NAMING IS ROUTED. **COMPONENT 3: row U1 is a BOOKKEEPING "
            "instrument, 0 statements about the object.** **ADDITION ONE: 2 routed items and 1 "
            "named, listed together for the first time.** **ADDITION TWO: a standing core of 8 "
            "arms, none about the mathematics; carry-forward never reaches half.** %d FOLDS RUN, %d "
            "ROWS WRITTEN, %d NAMES MINTED, %d NUMBERINGS RECONCILED, %d ARMS REFORMED, %d CONTENT "
            "LOST"
            % (LG['gates_read'], LG['face_subject_gates'], 0, 0, 0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT, NO "
            "`.lean` FILE TOUCHED AND NO AXIOM PROFILE READ OR INFERRED. ### THE COMPILED OBJECTS "
            "NAMED ARE NAMED AS THINGS THE RECORD CITES. ### READING A CLASS DOCUMENT IS NOT "
            "OPENING A CHANNEL")
    prof = ("### NO GRADE MOVED OR CONFERRED, NO FOLD RUN, NO ROW OF FACES_LEDGER WRITTEN, NO "
            "COORDINATE ADDED, NO NAME MINTED, NO RULE STRUCK OR WIDENED, NO NUMBERING RECONCILED, "
            "NO ARM ADDED REMOVED RENAMED OR PROMOTED, NO STANDING CORE PROPOSED, NO KEYSTONE "
            "EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY EDITED, NO PRIOR ACT'S BANK EDITED, NO "
            "FERRY_STANDING CLAUSE ADDED, NO SHARED INSTRUMENT AMENDED, NO IN-PLACE REPAIR MADE, NO "
            "LIST CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK CARRYING THE "
            "ROUTED-PRICE LIST, AND ONE APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A PERMISSIVE FILTER'S ENTIRE YIELD WAS PRINTED AND HAND-READ, AND ITS TWO MOST "
             "PROMISING HITS WERE REPORTED AS ARTEFACTS RATHER THAN AS EXAMINATIONS. ### A COUNT OF "
             "FOUR OCCURRENCES WAS REPORTED AS THREE INSTANCES AND ONE RESTATEMENT, BECAUSE THE TWO "
             "ARE DIFFERENT COUNTS. ### A PRICE WAS PRINTED IN TWO LAYERS WITH THE IN-PRINCIPLE "
             "LAYER MARKED UNCHECKED. ### A LIST DECLARED WHAT IT IS NOT. ### A MEASURE PRINTED ITS "
             "OWN LIMIT: IT COUNTS ARM NAMES, AND A NAME CARRIED FORWARD MAY HAVE BEEN REWRITTEN "
             "INSIDE. ### AND A SENTENCE THE TEST PRODUCED WAS STATED WITHOUT BEING NAMED, BECAUSE "
             "STATING IS NOT MINTING AND NAMING IS")
    status = ("data/b408_the_other_two_channels.txt; data/b408_components.txt; "
              "data/b408_extract.txt; data/b408_span.txt; "
              "data/b408_registration_2026-09-10.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b408); tools/b408_extract.py; "
              "tools/b408_regspec.py; tools/b408_reg_gate.py; tools/b408_components.py; "
              "tools/b408_desk_bank.py; tools/b408_checks.py; PLACE-papers OPEN_TRAILS.md (one "
              "append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('has the modular symmetry been examined as a channel',
           'what are the other two bright channels',
           'why does the corpus have two class numberings',
           'what would the reduction be if written as a proof',
           'is the fold due',
           'do the gate suites have a standing core')
MUST_NOT_HIT = ('a channel was opened', 'a fold was run', 'a numbering was reconciled',
                'a name was minted', 'a kernel was built')
KEY = 'the-other-two-channels'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b408 ASKED WHETHER THE OTHER TWO OF COROLLARY 3.6'S THREE CHANNELS HAVE EVER BEEN "
        "EXAMINED. **C3 IS THE ARCHIMEDEAN CLASS** -- *the Gamma-factor transformation under "
        "s -> 1-s produces the functional equation* -- **AND C4 IS THE MODULAR SYMMETRY GROUP "
        "PSL2(Z), WHICH IS THE ONLY ONE OF THE THREE THAT IS ITSELF A RELATION BETWEEN THE OTHER "
        "TWO** -- which is what Definition 2.2 asks an interface to be. A sweep over 4705 files "
        "(the whole live papers tree and every banked relay record), on a predicate fixed before "
        "it, returned **19 hits for C3 and 7 for C4, and EVERY HIT WAS HAND-READ**. **C3 IS "
        "EXAMINED ONCE, AND ONLY INSIDE THE BARRIER KEYSTONE ITSELF**, as T1 of the Tier-1 "
        "toolkit, where Theorem 3.7 concludes no T-derivation establishes P. **C4 IS ABSENT: ZERO "
        "EXAMINATIONS ANYWHERE** -- one hit is this session's own block, one is a numbering "
        "artefact, the rest name the class in passing -- **AND THE BARRIER'S OWN TOOLKIT DOES NOT "
        "NAME C4 EITHER: NOT INCLUDED, NOT EXCLUDED, NOT MENTIONED.** No claim is made that either "
        "is open. **AND THE SWEEP'S REAL FINDING IS A HAZARD THE CORPUS CARRIES AND TABULATES "
        "ITSELF: TWO CLASS NUMBERINGS THAT DISAGREE ON SIX OF SEVEN SYMBOLS.** The two most "
        "promising hits in the whole sweep -- PATHS_TO_THE_CRITICAL_LINE:107 and "
        "CRITICAL_RESOLVE:1121, both reading *output-stage classes (C3 + C7) assembling without "
        "crossing a dark interface* -- use the corollary's vocabulary exactly and are about a "
        "DIFFERENT class, because C3 is transformation-stage in one scheme and Local/Cauchy-Riemann "
        "in the other. **A SYMBOL MATCHED ACROSS DOCUMENTS WITH DIFFERENT NUMBERINGS IS A MATCHER "
        "ARTEFACT, NOT AN EXAMINATION.** Printed, not reconciled. **AND THE REDUCTION WRITTEN AS A "
        "CLASSIFIED FIRST-ORDER PROOF IS PRICED AS A PROOF-WITH-HYPOTHESES**: of the eight "
        "constituents, one is writable as a step and only at seven cells, one is a measurement, one "
        "is the conclusion, and the rest carry FOUR distinct imported premises -- Definition 3.1, "
        "Proposition C.1, the local term (149), Theorem 4.7 -- **ALL FOUR THE SOURCE'S THEOREMS, "
        "NONE DERIVED BY THE CORPUS, SO ALL FOUR MUST BE STATED AS HYPOTHESES. AND THE SECOND "
        "FINDING: WHAT GETS WRITTEN PROVES A CONDITIONAL, AND THEOREM 3.1 IS STATED ABOUT PROOFS OF "
        "THE UNIVERSAL STATEMENT -- SO DOING THE WORK WOULD STILL NOT MAKE THE THEOREM APPLY.** A "
        "second layer, that the imports may be consequences of the specification and the obstacle "
        "labour rather than logic, is printed and marked UNCHECKED. **THE SPAN IS 6 AGAINST (R1)'S "
        "THRESHOLD OF 9: THE FOLD IS NOT DUE AND NONE IS PROPOSED.** **THE FOUR DRESSES ARE ONE "
        "STATEMENT** -- *a result applies to an object only if the object is of the kind the result "
        "quantifies over* -- with the instantiation printed for each, **3 INDEPENDENT INSTANCES AND "
        "1 RESTATEMENT**; the record has no name for it and **THE NAMING IS ROUTED, NOT MINTED**. "
        "**ROW U1 IS A BOOKKEEPING INSTRUMENT BY ITS OWN NUMBERS: 6 SITES, 2 COORDINATES, 0 "
        "BRIDGES, 0 GRADES, 0 STATEMENTS ABOUT THE OBJECT** -- a description, not a demotion. **AND "
        "THE GATE SUITES HAVE A STANDING CORE OF 8 ARMS, NOT ONE OF THEM ABOUT THE MATHEMATICS**, "
        "with carry-forward at 13%, 45%, 48% -- never half.")
    grade = (
        "### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY "
        "CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO FOLD RUN, NO GRADE MOVED, NO ROW OF "
        "FACES_LEDGER WRITTEN, NO COORDINATE ADDED, NO NAME MINTED, NO RULE WIDENED, NO NUMBERING "
        "RECONCILED, NO ARM ADDED REMOVED RENAMED OR PROMOTED, NO STANDING CORE PROPOSED, NO BRIDGE "
        "TYPED, NO IN-PLACE REPAIR MADE, NO SHARED INSTRUMENT AMENDED, NO FERRY_STANDING CLAUSE "
        "ADDED, NO LIST CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE "
        "APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. "
        "### THE CLAUSE HAS NOT MOVED")
    where = (
        "data/b408_the_other_two_channels.txt; data/b408_components.txt; data/b408_extract.txt; "
        "data/b408_span.txt; data/b408_registration_2026-09-10.txt (LOCKED before any write, "
        "chained on tools/b378_lockgate.py run as b408 -- %d gates read, %d checked by digest); "
        "tools/b408_extract.py; tools/b408_components.py; tools/b408_desk_bank.py; "
        "tools/b408_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b408 (the other two channels searched and one found never examined, the two class "
           "numberings found, the classified proof priced as a proof-with-hypotheses, and the "
           "span counted at six against nine)")
    row_new = ('    # ### THE OTHER TWO CHANNELS (b408).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-42s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + chr(10)
    ROW_ANCHOR = ('INDEX = [' + chr(10)
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + chr(10))
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
        rec('    %-58s reaches the b408 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('C4 is reported ABSENT', 'C4 IS ABSENT' in out),
            ('C3 is reported examined once', 'EXAMINED ONCE' in out),
            ('the toolkit does not name C4', 'DOES NOT NAME C4' in out),
            ('the numbering hazard', 'TWO CLASS NUMBERINGS' in out),
            ('the artefact rule', 'MATCHER ARTEFACT' in out),
            ('proof-with-hypotheses', 'PROOF-WITH-HYPOTHESES' in out),
            ('the conditional finding', 'WOULD STILL NOT MAKE THE THEOREM APPLY' in out),
            ('the UNCHECKED layer', 'UNCHECKED' in out),
            ('the fold is not due', 'THE FOLD IS NOT DUE' in out),
            ('one statement', 'ARE ONE STATEMENT' in out),
            ('the naming is routed', 'THE NAMING IS ROUTED, NOT MINTED' in out),
            ('the row is bookkeeping', 'BOOKKEEPING INSTRUMENT' in out),
            ('the standing core', 'STANDING CORE OF 8 ARMS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-42s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b408 -- THE OTHER TWO CHANNELS, THE REDUCTION AS A CLASSIFIED PROOF PRICED, AND THE SPAN.')
    A('### THE BANK. ### 2026-09-10. ### CONCURRENCY: SOLO (research seat).')
    A('### Registration `data/b408_registration_2026-09-10.txt`, LOCKED BEFORE ANY WRITE at')
    A('### `%s`, %d bytes, chained on `b378_lockgate.py` run as b408'
      % (SEALHASH, len(SEALTXT.encode('utf-8'))))
    A('### -- ### **%d GATES READ, %d PASSING, %d CHECKED BY DIGEST.**'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A(BAR)
    A('')
    A(SUB)
    A('### (1) THE ANSWER, FIRST.')
    A(SUB)
    A('### ### ### **ONE OF THE THREE SOURCES A CLOSING PROOF MUST TOUCH HAS NEVER BEEN EXAMINED')
    A('### ### ### AS A CHANNEL BY ANY ACT, KEYSTONE OR LEDGER ROW -- AND THE BARRIER`S OWN')
    A('### ### ### TOOLKIT DOES NOT NAME IT EITHER.**')
    A('### `C₄`, the modular symmetry group `PSL₂(ℤ)`, is ### **THE ONLY ONE OF THE')
    A('### ### THREE THAT IS ITSELF A RELATION BETWEEN THE OTHER TWO** -- which is exactly what')
    A('### Definition 2.2 asks an interface to be. ### A sweep over `4705` files returned `7`')
    A('### hits; ### **EVERY ONE WAS HAND-READ AND NOT ONE IS AN EXAMINATION.**')
    A('### `C₃` fares better and not by much: ### **EXAMINED ONCE, AND ONLY INSIDE THE')
    A('### ### BARRIER KEYSTONE ITSELF**, as `T1` of the Tier-1 toolkit, where Theorem 3.7')
    A('### concludes no `T`-derivation establishes `P`.')
    A('### ### **AND NO CLAIM IS MADE THAT EITHER IS OPEN, PROMISING, OR WORTH OPENING.** ### The')
    A('### act reports what the record holds and what it has never asked. ### **AN UNASKED')
    A('### ### QUESTION IS NOT AN OPPORTUNITY UNTIL SOMEONE PRICES IT.**')
    A('')
    A(SUB)
    A('### (2) THE SWEEP`S REAL FINDING: TWO CLASS NUMBERINGS.')
    A(SUB)
    A('### The corpus carries ### **TWO NUMBERING SCHEMES** ### and tabulates them itself:')
    A('###   *| C₃ | C₁ | Archimedean / functional equation |*')
    A('###   *| C₄ | C₅ | Global / PSL₂ symmetry |*')
    A('### ### **THEY DISAGREE ON SIX OF SEVEN SYMBOLS; ONLY `C₇` MEANS THE SAME IN BOTH.**')
    A('### `C₃` is TRANSFORMATION-stage in the paper`s numbering, so a document calling')
    A('### `C₃` an ### **OUTPUT-STAGE** ### class is using the monograph`s, where `C₃`')
    A('### is *Local / Cauchy-Riemann*.')
    A('### ### ### **AND THE TWO MOST PROMISING HITS IN THE ENTIRE SWEEP ARE EXACTLY THAT.** ###')
    A('### `PATHS_TO_THE_CRITICAL_LINE:107` and `CRITICAL_RESOLVE:1121` both read *output-stage')
    A('### classes (C₃ + C₇) ... assembling without crossing a dark interface* -- ###')
    A('### **THE COROLLARY`S VOCABULARY EXACTLY, ABOUT A DIFFERENT CLASS.**')
    A('### ### **A SYMBOL MATCHED ACROSS DOCUMENTS WITH DIFFERENT NUMBERINGS IS A MATCHER')
    A('### ### ARTEFACT, NOT AN EXAMINATION.** ### **PRINTED AND NOT RECONCILED:** ### a')
    A('### reconciliation is a corpus-wide act and is the author`s.')
    A('')
    A(SUB)
    A('### (3) THE REDUCTION AS A CLASSIFIED PROOF, PRICED -- AND THE SECOND SURPRISE.')
    A(SUB)
    A('### Of the E0 gate`s eight constituents: ### **`1` WRITABLE AS A STEP** ### and only at')
    A('### seven cells (`K3`, whose compact part is per-cell); ### **`1` A MEASUREMENT** ###')
    A('### (`K5`); ### **`1` THE CONCLUSION** ### (`K8`, UNOWNED); and the rest carrying')
    A('### ### **FOUR DISTINCT IMPORTED PREMISES** -- the source`s Definition 3.1, Proposition')
    A('### C.1, the local term (149), Theorem 4.7.')
    A('### ### **ALL FOUR ARE THE SOURCE`S THEOREMS AND THE CORPUS HAS DERIVED NONE OF THEM**,')
    A('### which is what importing *under the bar* means. ### So each is ### **STATED AS A')
    A('### ### HYPOTHESIS**, and what gets written is `H ⇒ ∀x P(x)`: ### ### **A')
    A('### ### PROOF-WITH-HYPOTHESES, NOT A PROOF IN THE LEMMA`S SENSE.**')
    A('### ### ### **AND THEN THE SECOND FINDING, WHICH THE PRICING PRODUCED AND NOBODY ASKED')
    A('### ### ### FOR:** ### Theorem 3.1 is stated about proofs of the ### **UNIVERSAL')
    A('### ### ### STATEMENT**, and a proof of a ### **CONDITIONAL** ### is not one. ### **SO')
    A('### ### ### DOING THE WORK `b407` NAMED WOULD PRODUCE AN OBJECT THE LEMMA STILL DOES NOT')
    A('### ### ### QUANTIFY OVER.** ### It would need the lemma restated for conditional')
    A('### conclusions -- ### **A SECOND THING NOBODY HAS WRITTEN.**')
    A('### **THE SECOND LAYER, MARKED `UNCHECKED`:** ### an import the corpus has not derived may')
    A('### still be a CONSEQUENCE of the specification, in which case the obstacle is ### **LABOUR')
    A('### ### AND NOT LOGIC.** ### But whether each import is first-order expressible over `S` is')
    A('### a question nobody has asked and this act does not answer. ### **BOTH LAYERS PRINTED,')
    A('### ### NEITHER COLLAPSED INTO THE OTHER. ### `0` LINES WRITTEN.**')
    A('')
    A(SUB)
    A('### (4) THE SPAN, AND THE FOUR DRESSES.')
    A(SUB)
    A('### **THE SPAN:** ### the tool counts ### **`6`** ### against `(R1)`s threshold of')
    A('### ### **`9`**. ### ### **THE FOLD IS NOT DUE -- THREE ACTS SHORT -- AND THIS ACT')
    A('### ### PROPOSES NONE.** ### The count was taken from the tool`s output before any number')
    A('### was typed.')
    A('### **THE FOUR DRESSES:** ### ### **ONE STATEMENT.** ### *A result applies to an object')
    A('### only if the object is of the kind the result quantifies over.* ### Instantiated:')
    A('###   `b405` -- the countermodel quantifies over couplings on `ℝ → ℂ`; a row')
    A('###     site is not one.')
    A('###   `b406` -- the shared-witness form quantifies over `∀∃ ⇒ ∃∀`')
    A('###     statements; `(i)` has no inner existential and `(iv)`s is trivially satisfiable.')
    A('###   `b407` -- Theorem 3.1 quantifies over formal first-order proofs; the reduction is')
    A('###     not one.')
    A('###   `b407` again -- ### **A RESTATEMENT**, not a fourth instance: the exactness of a')
    A('###     resemblance does not change what kind the object is.')
    A('### ### **SO FOUR OCCURRENCES ARE THREE INDEPENDENT INSTANCES AND ONE RESTATEMENT, AND THE')
    A('### ### ACT SAYS SO RATHER THAN BANKING A LARGER NUMBER.**')
    A('### ### **THE RECORD HAS NO NAME FOR IT** -- `NO KEY` on the verdict line for all three')
    A('### queries -- ### **AND THE NAMING IS ROUTED TO THE AUTHOR.** ### **STATING THE SENTENCE')
    A('### ### THE TEST PRODUCES IS NOT MINTING; GIVING IT A NAME IS.**')
    A('')
    A(SUB)
    A('### (5) ROW `U1`, THE ROUTED PRICES, AND THE SUITE.')
    A(SUB)
    A('### **ROW `U1`: ### A BOOKKEEPING INSTRUMENT, BY ITS OWN NUMBERS.** ### `19308` bytes --')
    A('### the largest single row in the ledger -- `6` sites entered, `2` coordinates added, `1`')
    A('### price corrected, `0` bridges typed, `0` grades conferred, and ### **`0` STATEMENTS')
    A('### ### ABOUT THE OBJECT.** ### Every yield is a classification of what the record already')
    A('### held. ### **AND THAT IS A DESCRIPTION AND NOT A DEMOTION:** ### a bookkeeping')
    A('### instrument that has held a refusal intact through six entries, caught an over-count and')
    A('### forced two coordinates into existence has earned its place. ### **WHAT WOULD CHANGE IT:')
    A('### ### A SITE WHOSE ENTRY PRODUCED A STATEMENT ABOUT THE OBJECT. ### NONE OF THE SIX')
    A('### ### HAS.**')
    A('### **THE ROUTED PRICES, IN ONE PLACE FOR THE FIRST TIME:** ### `2` ROUTED (`b406`s')
    A('### encode-before-open sentence; `b407`s `(R20)` limb 2) and ### **`1` NAMED-NOT-ROUTED**')
    A('### (`b407`s Tier-2 statement). ### **THREE ITEMS AND NOT THREE ROUTINGS**, and the list')
    A('### declares that it is not a corpus-wide census.')
    A('### **THE SUITE:** ### a standing core of ### **`8` ARMS** ### across four acts, and')
    A('### ### **NOT ONE OF THE EIGHT IS ABOUT THE MATHEMATICS** -- the ferry, the seal, the key,')
    A('### the write list, the cap, the must-fail fixture. ### Carry-forward `13%`, `45%`, `48%`:')
    A('### ### **NEVER HALF.** ### And the measure prints its own limit: ### **IT COUNTS ARM')
    A('### ### NAMES, SO `48%` IS AN UPPER BOUND ON CONTINUITY AND NOT A MEASUREMENT OF IT.**')
    A('### ### **MEASURED AND NOT REFORMED.**')
    A('')
    A(SUB)
    A('### (6) THE WRITES, AND WHAT THEY COST THE RECORD.')
    A(SUB)
    A('### **`OPEN_TRAILS.md`** ### -- one append-only block, carrying the routed-price list.')
    A('### **`CORRESPONDENCE.md`** ### -- row `%d`, appended, six cells non-empty.' % rownum)
    A('### **THE INDEX** ### -- one key, `%s`, %s.' % (KEY, 'PASS' if kok else '### FAIL ###'))
    A('### **AND NOTHING ELSE.** ### `0` folds run, `0` rows of `FACES_LEDGER.md`, `0` in-place')
    A('### repairs, `0` coordinates added, `0` names minted, `0` rules widened, `0` numberings')
    A('### reconciled, `0` arms reformed, `0` grades moved, `0` bridges typed, `0` `.lean` files')
    A('### touched, `0` shared instruments amended, `0` content lost. ### **NOTHING DEPOSITS.**')
    A('')
    A(SUB)
    A('### (7) WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not say `C₄` is a promising channel, an open route, or worth opening. ###')
    A('### **IT SAYS THE CORPUS HAS NEVER ASKED**, which is a fact about the record.')
    A('### It does not say either numbering scheme is the right one, or reconcile them.')
    A('### It does not say the imports are underivable. ### **IT SAYS THE CORPUS HAS NOT DERIVED')
    A('### ### THEM, AND MARKS THE IN-PRINCIPLE QUESTION `UNCHECKED`.**')
    A('### It does not name the one statement. ### It does not fold, reform an arm, or move a')
    A('### grade.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### `h2` STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'wb').write((chr(10).join(B) + chr(10)).encode('utf-8'))
    rec('  bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))
    return len(B)
