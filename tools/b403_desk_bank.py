# -*- coding: utf-8 -*-
"""b403_desk_bank.py -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK."""
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
MARK = '<!-- b403 the three routed items: one repaired, one applied, one ruled and routed -->'
PRIOR = '<!-- b402 the artefact arc folded, b385-b401 -->'
BANKOUT = os.path.join(D, 'b403_the_three_routed_items.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


SEALTXT = io.open(os.path.join(D, 'b403_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = J('b403_lockgate')
CF = J('b403_components')
X = J('b403_extract')
F = X['fig']

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', 'PARKED'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND',
     'PARKED, and it is what kept this act from installing a guard in `SIDE-window`'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### **AND THIS ACT DATED ONE OF THEM AND SAYS SO:** ### `SIDE-window`s README figure '
     'was undated and is now removed with its history stated. ### **ONE FIGURE IS NOT THE LIST**, '
     'and the list stays OPEN. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', 'OPEN AND THE AUTHOR`S'),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the deposited layer, unread since b389', 'STAND', 'STILL BLOCKED'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND', 'NAMED at b398. ### **OPEN**'),
    ('the grade move inside b332`s E0 ranking table', 'STAND', 'ROUTED at b399. ### **OPEN**'),
    ('`(Q400)`, the prime constituent at a support where the primes enter', 'STAND',
     '### **OPEN**, its absence confirmed by search at b401 and ### **NOT OPENED**'),
    ('row `U1`s fifth site', 'STAND',
     '### **AWAITING ENTRY, AND NOT ENTERED HERE.** ### What the ferry calls the fifth site -- '
     'the window -- is ### **ALREADY THE ROW`S FOURTH**, entered by `b401`; entering it again '
     'would be the double-count that entry was written to prevent. ### **THE DISTINCT FIFTH IS '
     'THE REPRESENTATION-UNIFORMITY:** ### the located bound`s constant DEPENDS ON `pi` while '
     'Theorem 5.1`s is ABSOLUTE, so the record needs a statement uniform in `pi` and holds one '
     'indexed by it. ### **NO BRIDGE TYPED. ### OPEN**'),
    ('`SIDE-window` has no pre-push guard', 'STAND',
     '### **NEW at `b403` AND NOT REPAIRED.** ### The push was made from a `push-*` branch by '
     'hand under Rule 4.10. ### **NO GUARD IS INSTALLED:** ### the installer writes when run and '
     'the instrument-audit lane is PARKED. ### **OPEN**'),
    ('the KINDS write list, three clean-ish residues and no proof', 'STAND',
     '### `b401` and `b402` came out clean; ### **THIS ACT CAME OUT AT `1`** -- '
     '`b403_span_original.txt`, a kind the face did not name. ### **SO KINDS IS NOT COMPLETE '
     'EITHER**, and the order forbids minting until a fourth act shows the same shortfall twice. '
     '### **`0` SPECIES MINTED. ### OPEN**'),

    # ---- WHAT THIS ACT CLOSES --------------------------------------------------------------------
    ('the span counter`s stale threshold line, routed at b402', 'CLOSE',
     '### **CLOSED BY REPAIR.** ### `3` sites in `tools/b363_span.py` -- the module docstring, the '
     'printed line and the JSON field -- now cite `(R1)` at `b366` by name, and ### **THE '
     'SUPERSEDED SENTENCE IS PRESERVED VERBATIM IN THE FILE ITSELF**, not only in the bank, '
     'because a tool that loses its own history will be misread again. ### **`0` FIGURES THE '
     'COUNTER PRINTS MOVED**, tested against a same-moment control after that control had to be '
     'repaired twice'),
    ('`SIDE-window`s stale README count, routed at b401', 'CLOSE',
     '### **CLOSED BY APPLYING THE RULE THE RECORD ALREADY HAD.** ### `b371`s precedent, applied '
     'at `b372`: original banked verbatim first, the figure ### **REMOVED RATHER THAN RESTATED**, '
     'and the edit verified by re-reading the file. ### **AND `43` WAS NOT WRONG -- IT WAS EXACT '
     'AT `v0.4` AND UNDATED**, which corrects this seat`s own `b401` reading'),

    # ---- WHAT THIS ACT ADDS ----------------------------------------------------------------------
    ('a control must match the treatment in everything except the treatment', 'STAND',
     '### **NEW at `b403`, AND IT COST THIS ACT TWO FALSE STOPS.** ### The first control was a '
     'run taken ### **BEFORE THE RECORD CHANGED** ### (`b402`s pre-fold JSON), so the record '
     'advancing moved `6` of `8` fields on its own account. ### The second was a READ-ONLY run '
     'against an ### **EMITTING** ### one, so the two differed in a FOOTER and in no figure. ### '
     '**BOTH TIMES THE ARM STOPPED A CORRECT REPAIR, AND BOTH TIMES THE DEFECT WAS IN THE '
     'CONTROL.** ### **OPEN, AND REFUSABLE**'),
    ('the Addition`s label for one of the two prior repairs', 'STAND',
     '### **NEW at `b403`.** ### The Addition names *the exclusion kernel`s README*; the record '
     'says `b372` repaired the ### **CONSTRUCTION KERNEL`S** ### README and that ### *nothing in '
     'the exclusion kernel`s README was repaired.* ### **BOTH PRIOR REPAIRS ARE ON ONE '
     'REPOSITORY, `SIDE-global-section`.** ### The rule is unaffected. ### **FILED**'),
    ('no named ruling governs repairing another act`s locked face', 'STAND',
     '### **NEW at `b403` AS A SPLIT VERDICT AND NOT A BARE ABSENCE.** ### There is no `(R..)` '
     'ruling; there IS a uniform carried practice -- ### **THE LOCKED FACE IS NOT EDITED; BOTH '
     'FIGURES ARE PRINTED** -- and a mechanism, `b383`s amendment filed BESIDE a face. ### '
     '**SAYING `NO RULE EXISTS` WOULD BE THE FALSE HALF OF A TRUE SENTENCE.** ### Put to the '
     'author with its cost: one act, no instrument, no build. ### **OPEN**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS AND OPENS THREE.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 1500), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0)


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b403 — the three routed items: one repaired, one applied, one ruled and routed — '
        'filed 2026-09-10',
        '',
        '**One routed item is discharged by repair, one by applying a rule the record already had, '
        'and one is ruled and stays routed.** (i) **The span counter’s stale threshold line, routed '
        'at b402, is REPAIRED** — three sites in `tools/b363_span.py` now cite **(R1) at b366** by '
        'name, and **the superseded sentence is preserved verbatim in the file itself**, not only '
        'in the bank, because a tool that loses its own history will be misread again. **0 figures '
        'the counter prints moved.** (ii) **`SIDE-window`’s README count is REPAIRED under b371’s '
        'precedent as b372 applied it**: original banked verbatim first, the figure **removed '
        'rather than restated**, the edit verified by re-reading the file. (iii) **b321’s locked '
        'face stays ROUTED**, and the verdict on it is a split rather than a bare absence.',
        '',
        '**The rule the Addition invokes exists, and it is not phrased as the ferry phrases it.** '
        '*A figure on a claiming surface carries its ref or is not written* appears nowhere in the '
        'record; a search for those words would have returned ABSENT and been wrong — b385’s '
        'species. Searched by **description** instead, the rule is **b371’s precedent, applied at '
        'b372**, and its own words are: the original **preserved verbatim in the bank before any '
        'edit**; a figure **REMOVED RATHER THAN RESTATED, unless the document can name the ref it '
        'holds at**; and **if the repair would rewrite a claim rather than a number, it is routed '
        'and not made**.',
        '',
        '**And `43` was not a wrong number — it was an exact one with no date on it, which corrects '
        'this seat’s own b401 reading.** Measured at content: the four check files the README’s '
        'tables describe carry **43 `#print axioms` invocations, 43 distinct names**; with the '
        '`v0.5` local model the tree carries **69**. So 43 was **exact at v0.4 and is behind by '
        'exactly the 26 the local model added** — b371’s species precisely. b401 reported *43 '
        'against 69* and called it stale **without establishing that 43 was exact anywhere**. '
        '**b401’s bank is not edited; both readings are printed.** And the carve-out permitting a '
        'restated figure **does not reach this README**: the repository ships **no printed profile '
        'at all**, and a quoted sample of what a run would print is not a profile — so removal was '
        'the branch, and it leaves the claim exactly as strong as it was.',
        '',
        '**The Addition misnames one of the two prior repairs, in the way b372 itself caught.** It '
        'says *the construction kernel’s description and the exclusion kernel’s README*. The '
        'record: b371 repaired the `SIDE-global-section` **public description**, and b372 repaired '
        'the `SIDE-global-section` **README** — and b372 states in terms that *nothing in the '
        'exclusion kernel’s README was repaired*, because the order that sent it there named one '
        'object and described another. **Both prior repairs are on one repository.** The rule is '
        'unaffected; the label is corrected and not absorbed.',
        '',
        '**On b321’s locked face the verdict is a split, and the split is the honest answer.** '
        'There is **no (R..) ruling** on repairing another act’s locked face. There **is** a '
        'uniform carried practice, stated by every recent act in its own words — *the locked face '
        'is not edited; both figures are printed* — and a **mechanism**: b383’s amendment filed '
        '**beside** a locked face rather than into it. **Saying “no rule exists” would be the false '
        'half of a true sentence.** An amendment is itself an act and is not this one’s to file on '
        'another act’s behalf, so the item goes to the author with its cost: one act, no '
        'instrument, no build.',
        '',
        '**And this act’s own control was defective twice, which is the sharpest thing in it.** '
        'Component 1 stopped a correct repair twice. The first control was **b402’s span JSON, '
        'emitted before b402 wrote its fold** — the counter reads fold headings out of `FINDINGS.md`, '
        'so the record advancing moved 6 of 8 fields on its own account. The second was a '
        '**read-only run compared against an emitting run** — the two differed in a footer and in '
        'no figure. **A control taken before the record changed cannot isolate a change to the '
        'tool, and a control that differs from the treatment in a flag measures the flag.** Both '
        'stops are printed rather than smoothed away.',
        '',
        '**Row `U1` gains nothing here, and what the ferry calls its fifth site is already its '
        'fourth.** The window — *the prime constituent at a widened support* — was entered by b401 '
        'as (iv); entering it again would be the double-count that entry was written to prevent. '
        '**A genuinely distinct fifth does exist and is restated as awaiting entry, not entered:** '
        'the located bound’s constant **depends on the representation** while Theorem 5.1’s is '
        '**absolute**, so the record needs a statement uniform in `π` and holds one indexed by it. '
        '**No bridge is typed, and the row’s refusal governs.**',
        '',
        '**And one file of a kind the face did not name was written** — `b403_span_original.txt`. '
        'b401 and b402 came out clean on KINDS; **this one did not**, so KINDS is not complete '
        'either. **0 species minted**: the order forbids it until a fourth act shows the same '
        'shortfall twice.',
        '',
        '**The four lists stay OPEN by name**, each with its trigger: LIST 1 — when a row of it is '
        'cited; LIST 2 — when a grade must be defended; LIST 3 — when a figure is quoted forward '
        '(and one undated figure was dated here, which is not the list); LIST 4 — at the next '
        'bibliography pass. **This act closes none of them.**',
        '',
        '*No grade moved or was conferred. No locked face was edited. No instance was added to any '
        'ledger row. No kernel was built and no instrument was run. Nothing deposits and the '
        'platform was not called at all. h2 stands exactly where the deposit left it.*',
        '',
    ]


SCOPE = (
    "**SCOPE: THE THREE ROUTED ITEMS -- ONE REPAIRED, ONE APPLIED, ONE RULED AND ROUTED.** (i) THE "
    "SPAN COUNTER'S STALE THRESHOLD LINE IS REPAIRED at 3 sites in tools/b363_span.py, citing (R1) "
    "at b366 by name, with **THE SUPERSEDED SENTENCE PRESERVED VERBATIM IN THE FILE ITSELF** and 0 "
    "figures the counter prints moved. (ii) SIDE-window's README count is REPAIRED under b371's "
    "precedent as b372 applied it -- original banked verbatim first, the figure **REMOVED RATHER "
    "THAN RESTATED**, the edit verified by re-reading the file. (iii) b321's locked face STAYS "
    "ROUTED. **THE RULE THE ADDITION INVOKES EXISTS AND IS NOT PHRASED AS THE FERRY PHRASES IT:** a "
    "search for the ferry's words would have returned ABSENT (b385's species); searched by "
    "DESCRIPTION it is b371's precedent applied at b372 -- the original preserved before any edit, "
    "a figure REMOVED RATHER THAN RESTATED unless the document can name the ref it holds at, and a "
    "repair that would rewrite A CLAIM RATHER THAN A NUMBER routed and not made. **AND 43 WAS NOT A "
    "WRONG NUMBER -- IT WAS AN EXACT ONE WITH NO DATE ON IT, WHICH CORRECTS THIS SEAT'S OWN b401 "
    "READING:** the four check files the README's tables describe carry 43 `#print axioms` "
    "invocations and 43 distinct names, and the v0.5 local model brought the tree to 69, so 43 was "
    "EXACT AT v0.4 and is behind by exactly the 26 the local model added. b401's bank is NOT edited "
    "and both readings are printed. **THE CARVE-OUT DOES NOT REACH THIS README:** the repository "
    "ships NO PRINTED PROFILE AT ALL, and a quoted sample of what a run would print is not a "
    "profile, so removal was the branch -- and it leaves the claim exactly as strong as it was, "
    "because nothing was built and nothing may be certified. **THE ADDITION MISNAMES ONE OF THE TWO "
    "PRIOR REPAIRS, IN THE WAY b372 ITSELF CAUGHT:** both are on SIDE-global-section, and b372 says "
    "in terms that nothing in the exclusion kernel's README was repaired. **ON b321'S FACE THE "
    "VERDICT IS A SPLIT:** no (R..) ruling, a uniform carried practice (the locked face is not "
    "edited; both figures are printed), and a mechanism (b383's amendment filed BESIDE a face) -- "
    "so NO RULE EXISTS would be the false half of a true sentence; put to the author at one act, no "
    "instrument, no build. **AND THIS ACT'S OWN CONTROL WAS DEFECTIVE TWICE AND STOPPED A CORRECT "
    "REPAIR TWICE:** first against a run taken BEFORE THE RECORD CHANGED, then a READ-ONLY run "
    "against an EMITTING one. A control taken before the record changed cannot isolate a change to "
    "the tool, and a control that differs from the treatment in a flag measures the flag. **ROW U1 "
    "GAINS NOTHING AND ITS FIFTH SITE IS ALREADY ITS FOURTH**; the distinct fifth -- the "
    "representation-uniformity -- is restated as AWAITING ENTRY and NOT ENTERED, no bridge typed. "
    "**ONE FILE OF AN UNNAMED KIND WAS WRITTEN**, so KINDS is not complete either, and 0 SPECIES "
    "ARE MINTED. NO GRADE MOVED OR CONFERRED, NO LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO "
    "INSTANCE ADDED TO ANY LEDGER ROW, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO "
    "CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NEITHER MAP TOUCHED, NO CLUSTER "
    "RESHAPED, NO LIST CLOSED. NOTHING DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**; 0 CLONES, "
    "0 BUILDS, 0 INSTRUMENT RUNS, NO .lean FILE TOUCHED, NO .git/hooks/pre-push DELETED OR "
    "INSTALLED. THE INSTRUMENT LANE AND THE INSTRUMENT-AUDIT LANE STAY PARKED. THE WAVE STAYS "
    "PARKED. M-2 REMAINS (SPECIFIED-NOT-STATED). THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. "
    "**THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED: A MAINTENANCE ACT MOVES NEITHER.** h2 "
    "stands exactly where the deposit left it.")


def corr_rows(Q):
    m = ("**THE RULE EXISTED, THE FIGURE WAS EXACT AND UNDATED RATHER THAN WRONG, AND THIS ACT'S "
         "OWN CONTROL STOPPED A CORRECT REPAIR TWICE** (b403, the three routed items)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b403 -- %d gates read, %d checked by digest; %d reads, %d ANCHORED. **(i) THE SPAN "
            "COUNTER REPAIRED** at %d sites, citing (R1) at b366 by name, the superseded sentence "
            "PRESERVED VERBATIM IN THE FILE ITSELF, and %d figures moved. **(ii) SIDE-window's "
            "README REPAIRED** under b371's precedent as b372 applied it: original banked first, "
            "the figure REMOVED RATHER THAN RESTATED, the edit verified by re-reading. **43 WAS "
            "EXACT AT v0.4 AND UNDATED, NOT WRONG** -- %d invocations across the four check files "
            "the tables describe, %d across five at HEAD -- which CORRECTS THIS SEAT'S OWN b401 "
            "READING, b401's bank unedited and both readings printed. THE CARVE-OUT DOES NOT REACH "
            "IT: the repository ships NO PRINTED PROFILE. **(iii) b321'S LOCKED FACE STAYS ROUTED**, "
            "the verdict a SPLIT -- no (R..) ruling, a uniform carried practice, and b383's "
            "amendment mechanism -- put to the author at one act. THE ADDITION MISNAMES ONE PRIOR "
            "REPAIR AND BOTH ARE ON SIDE-global-section. **AND THE ACT'S OWN CONTROL WAS DEFECTIVE "
            "TWICE**: a run taken before the record changed, then a read-only run against an "
            "emitting one. ROW U1 GAINS %d INSTANCES; its fifth site is already its fourth, and the "
            "distinct fifth is AWAITING ENTRY. %d FILES OF AN UNNAMED KIND, %d SPECIES MINTED, %d "
            "GRADES MOVED, %d LOCKED FACES EDITED"
            % (LG['gates_read'], LG['face_subject_gates'], len(X['reads']),
               sum(1 for r in X['reads'] if r['verdict'].startswith('ANCHORED')),
               CF['c1_sites'], CF['c1_moved'], F['prints_without_localmodel'],
               F['prints_total'], 0, CF['c3_unnamed'], 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED. ### NO KERNEL WAS BUILT AND "
            "NO INSTRUMENT RUN: SIDE-window's SOURCE WAS READ, ITS `.lean` FILES WERE NOT TOUCHED, "
            "AND ITS AXIOM CLAIM IS NEITHER STRENGTHENED NOR WEAKENED -- the removal takes a number "
            "and leaves the assertion. ### REPAIRING A FIGURE IS NOT CERTIFYING WHAT IT COUNTED")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED. ### NO GRADE MOVED OR CONFERRED, NO "
            "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS "
            "RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST "
            "CLOSED, NO LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO INSTANCE ADDED TO ANY "
            "LEDGER ROW. ### THE WRITES ARE ONE PRIOR INSTRUMENT OF THIS SEAT'S OWN, ONE README OF "
            "THE FEDERATION'S, AND ONE APPEND-ONLY TRAIL BLOCK")
    grade = ("### THE RULE APPLIED IS QUOTED FROM THE ACT THAT MADE IT, AT A FILE AND A LINE, AND "
             "WAS FOUND BY SEARCHING ITS DESCRIPTION RATHER THAN THE FERRY'S NAME FOR IT. ### EVERY "
             "ORIGINAL IS BANKED VERBATIM BEFORE ITS EDIT AND EVERY EDIT IS VERIFIED BY RE-READING "
             "THE FILE. ### THE FIGURE IS MEASURED AT CONTENT BEFORE IT IS CALLED STALE, WHICH IS "
             "WHAT ESTABLISHED THAT IT WAS EXACT AND UNDATED RATHER THAN WRONG -- AND THAT "
             "CORRECTION IS AGAINST THIS SEAT'S OWN PRIOR ACT, PRINTED AND NOT EDITED IN. ### THE "
             "VERDICT ON A LOCKED FACE IS A SPLIT AND NOT A BARE ABSENCE. ### AND THE ACT'S OWN "
             "CONTROL FAILED TWICE AND BOTH FAILURES ARE PRINTED, BECAUSE AN ARM THAT STOPS A "
             "CORRECT REPAIR IS A DEFECT WHETHER OR NOT ANYONE NOTICES")
    status = ("data/b403_the_three_routed_items.txt; data/b403_components_run3.txt; "
              "data/b403_extract_notes.txt; data/b403_span_before.txt; data/b403_span_after.txt; "
              "data/b403_readme_original.txt; data/b403_registration_2026-09-10.txt (LOCKED before "
              "any write at sha256 %s, chained on tools/b378_lockgate.py run as b403); "
              "tools/b403_extract.py; tools/b403_regspec.py; tools/b403_reg_gate.py; "
              "tools/b403_components.py; tools/b403_desk_bank.py; tools/b403_checks.py; "
              "tools/b363_span.py (repaired); SIDE-window README.md (repaired); PLACE-papers "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('does the corpus have a rule for a stale figure on a public surface',
           'was the side-window terminal count wrong or undated',
           'may an act repair another act locked face',
           'what did the span counter say about the fold threshold',
           'why did the control stop a correct repair',
           'is the fifth uniformity site entered')
MUST_NOT_HIT = ('a locked face was edited', 'the axiom claim was certified',
                'a species was minted', 'the fifth site was entered',
                'a kernel was built')

KEY = 'the-three-routed-items'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b403 TOOK THE THREE ITEMS THE PRIOR SPAN ROUTED AND DISCHARGED TWO, RULING THE THIRD. "
        "**(i) THE SPAN COUNTER'S STALE THRESHOLD LINE IS REPAIRED** at 3 sites in "
        "tools/b363_span.py, citing (R1) at b366 by name, with the superseded sentence PRESERVED "
        "VERBATIM IN THE FILE ITSELF and 0 figures the counter prints moved. **(ii) SIDE-window's "
        "README COUNT IS REPAIRED** under the rule the record already had. **(iii) b321's LOCKED "
        "FACE STAYS ROUTED.** **THE RULE EXISTS AND IS NOT PHRASED AS THE FERRY PHRASES IT**: a "
        "search for the ferry's words returns ABSENT (b385's species); searched by DESCRIPTION it "
        "is b371's precedent applied at b372 -- the original preserved before any edit, a figure "
        "REMOVED RATHER THAN RESTATED unless the document can name the ref it holds at, and a "
        "repair rewriting A CLAIM RATHER THAN A NUMBER routed. **AND 43 WAS NOT A WRONG NUMBER: IT "
        "WAS EXACT AT v0.4 AND UNDATED** -- 43 `#print axioms` invocations across the four check "
        "files the README's tables describe, 69 across five at HEAD, the difference being exactly "
        "the 26 the v0.5 local model added. **THIS CORRECTS b401's OWN READING**, which called it "
        "stale without establishing that 43 was exact anywhere; b401's bank is not edited and both "
        "readings are printed. **THE CARVE-OUT PERMITTING A RESTATED FIGURE DOES NOT REACH THIS "
        "README**: the repository ships NO PRINTED PROFILE, and a quoted sample of what a run would "
        "print is not a profile. **ON b321's FACE THE VERDICT IS A SPLIT**: no (R..) ruling, a "
        "uniform carried practice (the locked face is not edited; both figures are printed), and a "
        "mechanism (b383's amendment filed BESIDE a face) -- so NO RULE EXISTS would be the false "
        "half of a true sentence. **AND THIS ACT'S OWN CONTROL WAS DEFECTIVE TWICE AND STOPPED A "
        "CORRECT REPAIR TWICE**: first against a run taken BEFORE THE RECORD CHANGED, then a "
        "READ-ONLY run against an EMITTING one. **A CONTROL TAKEN BEFORE THE RECORD CHANGED CANNOT "
        "ISOLATE A CHANGE TO THE TOOL, AND A CONTROL THAT DIFFERS FROM THE TREATMENT IN A FLAG "
        "MEASURES THE FLAG.** Row U1 gains nothing; its fifth site is already its fourth, and the "
        "distinct fifth -- the representation-uniformity -- is AWAITING ENTRY, not entered.")
    grade = (
        "### NO KERNEL WAS BUILT AND NO INSTRUMENT RUN. ### SIDE-window's SOURCE WAS READ AND ITS "
        "`.lean` FILES WERE NOT TOUCHED; ITS AXIOM CLAIM IS NEITHER STRENGTHENED NOR WEAKENED, THE "
        "REMOVAL TAKING A NUMBER AND LEAVING THE ASSERTION. ### NO GRADE MOVED OR CONFERRED, NO "
        "LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO INSTANCE ADDED TO ANY LEDGER ROW, NO "
        "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLASS RULED, NO REGISTRY ROW "
        "EDITED, NO LIST CLOSED. ### EVERY ORIGINAL IS BANKED VERBATIM BEFORE ITS EDIT AND EVERY "
        "EDIT IS VERIFIED BY RE-READING THE FILE. ### ONE FILE OF A KIND THE FACE DID NOT NAME WAS "
        "WRITTEN AND IS PRINTED; 0 SPECIES MINTED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT "
        "CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED")
    where = (
        "data/b403_the_three_routed_items.txt; data/b403_components_run3.txt; "
        "data/b403_span_before.txt; data/b403_span_after.txt; data/b403_readme_original.txt; "
        "data/b403_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b403 -- %d gates read, %d checked by digest); "
        "tools/b403_extract.py; tools/b403_components.py; tools/b403_desk_bank.py; "
        "tools/b403_checks.py; tools/b363_span.py (repaired); SIDE-window README.md (repaired); "
        "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b403 (the rule existed, the figure was exact and undated rather than wrong, and the '
           'act\'s own control stopped a correct repair twice)')
    row_new = ('    # ### THE THREE ROUTED ITEMS (b403).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
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
    if ('"%s"' % KEY) not in txt and ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s' % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-60s reaches the b403 key : %s' % (qq, g2))
    for lbl, cond in (
            ('the rule exists and is quoted', "b371's precedent applied at b372" in out),
            ('the ferry`s wording is absent', "returns ABSENT (b385's species)" in out),
            ('43 was exact and undated', 'EXACT AT v0.4 AND UNDATED' in out),
            ('b401 is corrected, not edited', "THIS CORRECTS b401's OWN READING" in out),
            ('the carve-out does not reach it', 'NO PRINTED PROFILE' in out),
            ('the locked face verdict is a split', 'the false half of a true sentence' in out),
            ('the control failed twice', 'STOPPED A CORRECT REPAIR TWICE' in out),
            ('the control lesson is stated', 'MEASURES THE FLAG' in out),
            ('the fifth site is awaiting entry', 'AWAITING ENTRY, not entered' in out),
            ('the counter moved no figure', '0 figures the counter prints moved' in out)):
        ok = ok and cond
        rec('    %-60s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b403 -- THE THREE ROUTED ITEMS, DISCHARGED OR RULED. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### CONCURRENCY: SOLO (research seat).')
    A('### The face was LOCKED before any write at sha256 `%s`.' % SEALHASH)
    A(BAR)
    A('')
    A(SUB)
    A('### THE THREE VERDICTS.')
    A(SUB)
    A('### ### ### **(i) THE SPAN COUNTER : ### REPAIRED.** ### `%d` sites; `(R1)` at `b366` cited'
      % CF['c1_sites'])
    A('### by name; the superseded sentence PRESERVED VERBATIM IN THE FILE ITSELF; ### **`%d`'
      % CF['c1_moved'])
    A('### ### FIGURES THE COUNTER PRINTS MOVED.**')
    A('### ### ### **(ii) `SIDE-window`S README : ### REPAIRED**, under `b371`s precedent as `b372`')
    A('### applied it. ### **THE COUNT REMOVED RATHER THAN RESTATED**, the original banked verbatim')
    A('### first, and the edit verified by re-reading the file.')
    A('### ### ### **(iii) `b321`S LOCKED FACE : ### RULED AND STILL ROUTED**, the verdict a SPLIT')
    A('### rather than a bare absence, and put to the author with its cost.')
    A('')
    A(SCOPE)
    A('')
    A(SUB)
    A('### THE FIGURE, MEASURED AT CONTENT BEFORE IT WAS CALLED ANYTHING.')
    A(SUB)
    A('###   `the README`s claiming sentence          : all 43 terminals are fully axiom-free`')
    A('###   `#print axioms across the four v0.1-v0.4 check files : %d`'
      % F['prints_without_localmodel'])
    A('###   `#print axioms across all five at HEAD          : %d`' % F['prints_total'])
    A('###   `the difference                                 : %d, exactly the v0.5 local model`'
      % (F['prints_total'] - F['prints_without_localmodel']))
    A('###   `printed profile files in the tree              : %d`' % len(F['sw_profile_files']))
    A('### ### **SO `43` WAS EXACT AT `v0.4` AND UNDATED, NOT WRONG** -- `b371`s species exactly.')
    A('### ### **AND THAT CORRECTS THIS SEAT`S OWN `b401` READING**, which reported `43` against')
    A('### `69` and called it stale ### **WITHOUT ESTABLISHING THAT `43` WAS EXACT ANYWHERE.** ###')
    A('### **`b401`S BANK IS NOT EDITED AND BOTH READINGS ARE PRINTED.**')
    A('')
    A(SUB)
    A('### THE ACT`S OWN DEFECT, AND IT IS THE SHARPEST THING IN IT.')
    A(SUB)
    A('### ### **COMPONENT 1 STOPPED A CORRECT REPAIR TWICE, AND BOTH TIMES THE DEFECT WAS IN THE')
    A('### ### CONTROL AND NOT IN THE REPAIR.**')
    A('###   ### **(1) A CONTROL TAKEN BEFORE THE RECORD CHANGED.** ### The first comparison was')
    A('###     against `b402`s span JSON, emitted ### **BEFORE `b402` WROTE ITS FOLD** ### into')
    A('###     `FINDINGS.md`. ### The counter reads fold headings out of that file, so `6` of `8`')
    A('###     fields moved on the record`s own account.')
    A('###   ### **(2) A CONTROL THAT DIFFERED FROM THE TREATMENT IN A FLAG.** ### The second')
    A('###     compared a READ-ONLY run against an ### **EMITTING** ### one; the two differed in a')
    A('###     FOOTER and in no figure.')
    A('### ### **THE SPECIES: ### A CONTROL MUST MATCH THE TREATMENT IN EVERYTHING EXCEPT THE')
    A('### ### TREATMENT, AND MUST BE TAKEN AT THE SAME MOMENT AS IT.** ### An arm that stops a')
    A('### correct repair is a defect whether or not anyone notices, and both stops are printed.')
    A('')
    A(SUB)
    A('### WHAT THE ACT WROTE, AND WHAT IT DID NOT.')
    A(SUB)
    A('### **THE DESK** ### -- `%d` items swept, `%d` closed, `%d` standing, `%d` lists closed.'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **THE SURVEY** ### -- `%d` reads, `%d` ANCHORED.'
      % (len(X['reads']), sum(1 for r in X['reads'] if r['verdict'].startswith('ANCHORED'))))
    A('### **THE GATE CHAIN** ### -- `%d` gates read, `%d` passing, `%d` checked by digest.'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A('### **THE ROW AND THE KEY** ### -- correspondence row `%d`; index key `%s` : %s.'
      % (rownum, KEY, 'PASS' if kok else 'FAIL'))
    A('### **THE WRITE LIST** ### -- `%d` files of a KIND the face did not name: `%s`. ### **KINDS'
      % (CF['c3_unnamed'], ', '.join(CF['c3_unnamed_names']) or 'none'))
    A('### ### IS NOT COMPLETE EITHER, AND `0` SPECIES ARE MINTED.**')
    A('')
    A(SUB)
    A('### WHAT THIS ACT DOES NOT SAY.')
    A(SUB)
    A('### It does not certify `SIDE-window`s axiom claim. ### **NOTHING WAS BUILT, SO NOTHING MAY')
    A('### ### BE CERTIFIED**, and the removal takes a number and leaves the assertion exactly as')
    A('### strong as it was.')
    A('### It does not say the corpus has no rule about locked faces -- ### **IT HAS A PRACTICE AND')
    A('### ### A MECHANISM AND NO NAMED RULING, AND ALL THREE ARE SAID.**')
    A('### It does not edit `b321`s face, `b401`s bank, or any locked file.')
    A('### It does not enter a fifth instance in row `U1`, and it types no bridge.')
    A('### It does not mint a species from one shortfall.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### h2 STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  ### bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))


def main():
    bar('=')
    rec('b403 -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
    else:
        rec('  ### the b402 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b403_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_counter_repaired': 'is repaired' in low and 'b363_span.py' in low,
        'says_preserved_in_file': 'preserved verbatim in the file itself' in low,
        'says_no_figure_moved': '0 figures' in low,
        'says_readme_repaired': 'removed rather than restated' in low,
        'says_rule_found_by_description': 'b385’s species' in low or 'b385’s species' in low,
        'says_43_exact': 'exact at v0.4' in low,
        'says_corrects_b401': 'corrects this seat’s own b401 reading' in low
                              or 'corrects this seat’s own b401 reading' in low,
        'says_no_profile': 'no printed profile' in low,
        'says_mislabel': 'both prior repairs are on one repository' in low,
        'says_split_verdict': 'the false half of a true sentence' in low,
        'says_control_twice': 'stopped a correct repair twice' in low,
        'says_control_lesson': 'measures the flag' in low,
        'says_fifth_awaiting': 'awaiting entry, not entered' in low,
        'says_unnamed_kind': 'b403_span_original.txt' in low,
        'says_no_mint': '0 species minted' in low,
        'says_lists_open': 'the four lists stay open by name' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-34s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b403_desk_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b403_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b403_desk_notes', LINES)
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
        open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(TABLE + '.tmp', TABLE)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(chr(10))),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            run_clock.write(D, 'b403_desk_notes', LINES)
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
    bank(Q, rownum, kok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### ROW %d. ### KEY %s. ### BANK WRITTEN.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL'))
    bar('=')
    run_clock.write(D, 'b403_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
