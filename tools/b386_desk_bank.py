# -*- coding: utf-8 -*-
"""b386_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

### ### **ONE DESK ITEM IS CLOSED ON A CONDITION THE ORDER SET, AND THE CONDITION IS EVALUATED
### ### HERE RATHER THAN ASSUMED.** ### The order says the guard item is closed ### *only if
### Component 2's exercise passes* ### and left open with its reason otherwise. ### So this writer
### reads `data/b386_hooks.txt` ### **BEFORE** ### it sweeps, and the item's disposition is a
### function of that record. ### **A CONDITIONAL CLOSURE WHOSE CONDITION IS NOT MEASURED IS AN
### ### UNCONDITIONAL CLOSURE**, which is what `b385` filed.
###
### ### **AND THE EXERCISE HAD TO RUN BEFORE THIS WRITER, WHICH MOVED THE ACT'S ORDER.** ### The
### exerciser refuses on a tree carrying uncommitted paths, so the guard change is committed FIRST,
### the exercise runs on clean trees, and only then is the ledger written. ### **THAT IS THE
### ### ORDER THE ORDER IMPLIES**, and it is stated rather than discovered twice.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import gate_needle as GN          # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b386 the guard made single-sourced; (R15) executed -->'
PRIOR = '<!-- b385 the six on the trails; the rule found; the three done -->'
ACT = 'b386'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b386_components')
LG = J('b386_lockgate')
E = J('b386_reads')
C1, C2, C3, C4 = AC['C1'], AC['C2'], AC['C3'], AC['C4']
BANKOUT = os.path.join(D, 'b386_the_guard_single_sourced.txt')

# ### ### **THE EXERCISE VERDICT, READ OUT OF THE HOOK RECORD AND NOT ASSUMED.**
HOOKREC = os.path.join(D, 'b386_hooks.txt')
_h = io.open(HOOKREC, encoding='utf-8', errors='replace').read() if os.path.exists(HOOKREC) else ''
EX_FAILING0 = '### REPOS FAILING : 0' in _h
EX_ROWS = [ln for ln in _h.split(chr(10))
           if 'REFUSED' in ln and 'ALLOWED' in ln and 'PASS' in ln]
EXERCISE_OK = EX_FAILING0 and len(EX_ROWS) == 4


DESK = [
    ('M-2, under b310 cap', 'STAND', None, None,
     'the aggregation is still SPECIFIED-NOT-STATED and b310 cap still governs'),
    ("the object's conditions", 'STAND', None, None,
     "the conditions are the object's and none has been discharged"),
    ('the uniformity row U1, four entries and its own refusal', 'STAND', None, None,
     "the row's own refusal stands and the entries are unchanged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', None, None,
     "PARKED by the author's ruling; only the author unparks it"),
    ('the wave candidate list, typed and not ranked at b324', 'STAND', None, None,
     "typed and not ranked; ranking is the author's"),
    ("the wave itself, the author's own", 'STAND', None, None, "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', None, None,
     'each still carries its owner and none has been opened'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', None, None,
     "UNCONFIRMED on this seat's record; the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', None, None,
     'no act has been sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', None, None,
     'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', None, None,
     'ROUTED to the author; this act creates no tracking document either'),
    ("the census's definition-versus-operation drift", 'STAND', None, None,
     'FILED at b377 and ### **NOT REPAIRED**'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME ---------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### This act adds nothing to it and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None,
     None, 'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### This act dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### This act rewrites none of them'),

    # ---- CARRIED --------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S, and the standing standard already rules it'),
    ('the three amendments b383 drafted that are still routed', 'STAND', None, None,
     '### **ROUTED AND UNAPPLIED.** ### `(iv)` was answered at b385 by a FINDING rather than by a '
     'ruling; ### **`(i)`, `(ii)` AND `(iii)` REMAIN THE AUTHOR`S**'),
    ('the citation question -- what a finished keystone is cited as', 'STAND', None, None,
     '### **AWAITING THE AUTHOR AND NOT MOVED BY THIS ACT.** ### `%d` options from the standard`s '
     'own ruled borderlines, `%d` recommended, and the failure the tiers exist to prevent quoted '
     'beside them. ### **THIS ACT ADDS NO OPTION AND PREFERS NONE**'
     % (3, 0)),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words'),
    ('the six subject clusters with no keystone', 'STAND', None, None,
     'ON THE TRAILS LEDGER as ### **`NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT** ### since '
     'b385. ### `0` opened, ranked or prioritised by this act'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED.** ### Not this act`s to commit either'),

    # ---- WHAT THIS ACT ADDS TO THE DESK ---------------------------------------------------------
    ('the legacy `.git/hooks/pre-push` copies, one per repository', 'STAND', None, None,
     'NEW at b386 and ### **DISPOSED OF, NOT DELETED.** ### `(R15)`s THIRD disposal -- *the '
     'repository is reconfigured so the source is what runs* -- is already in force via '
     '`core.hooksPath = .githooks`, ### **VERIFIED IN ALL FOUR.** ### **THAT IS A JUDGEMENT AND IT '
     'IS MARKED AS ONE**: deleting them would remove a working fallback if the setting were ever '
     'unset. ### **THE AUTHOR MAY OVERTURN IT**'),
    ('the untracked `.b304-backup` artifacts the installer left', 'STAND', None, None,
     'NEW at b386: the repaired installer wrote a backup beside each guard it replaced, and '
     '### **ONE OF THEM WENT TO `.b304-backup-1` BECAUSE A BACKUP WAS ALREADY THERE.** ### They '
     'are UNTRACKED, they are ### **NOT COMMITTED AND NOT DELETED**, and they are named here '
     'rather than tidied away by an act that was not asked to'),

    # ---- WHAT THIS ACT CLOSES -------------------------------------------------------------------
    ("the guard's own stale install line", 'CLOSE', 'b386_components_notes',
     'ALL FOUR CARRY THE REPAIRED LINE : True',
     'CLOSED at b386, and ### **ONLY BECAUSE THE EXERCISE PASSED** -- the order`s own condition. '
     '### `b385` filed this closed and had to withdraw it; ### **THE OCCASION IS GONE THIS TIME '
     'BECAUSE THE SOURCE THE INSTALLER READS IS THE FILE THAT CARRIES THE REPAIR.** ### All four '
     'rostered repositories LF-normalised-equal to that source`s own git blob'),
    ('the second tracked guard copy, and the topology behind it', 'CLOSE', 'b386_components_notes',
     'THE INSTALLER NOW READS THE FILE THE REPOSITORIES RUN : True',
     'CLOSED at b386 by ### **`(R15)`S FIRST DISPOSAL**: `relay/tools/git-hooks/pre-push` DELETED '
     'after ### **ITS RECOVERABILITY WAS PRINTED, NOT AFTER IT WAS GONE**, and `b304_hooks.py`s '
     '`SOURCE` repointed at `.githooks/pre-push`. ### **EXACTLY ONE TRACKED GUARD PER REPOSITORY. '
     '### THE TOPOLOGY WAS THE DEFECT AND THE TOPOLOGY IS WHAT WAS FIXED**'),
    ('the installer`s backup defect', 'CLOSE', 'b386_components_notes',
     'BOTH POLARITIES HELD : True',
     'CLOSED at b386: the tool ### **NEVER OVERWRITES AN EXISTING BACKUP** ### and takes a fresh '
     'name instead -- ### **AN INVARIANT STRICTLY STRONGER THAN THE ONE THE ORDER ASKED FOR**, '
     'named as a substitution and not slipped in. ### Fixtured in both polarities, and ### **IT '
     'FIRED FOR REAL ON THIS ACT`S OWN INSTALL RUN**: `SIDE-effects` already carried a backup, '
     'which survived byte-for-byte'),
    ('and what the destroyed backup held', 'CLOSE', 'b386_components_notes',
     'THE CRLF EXPANSION IS `3139` BYTES, WHICH IS THE REMOVED FILE`S SIZE : True',
     'CLOSED at b386 by ### **IDENTIFICATION, NOT BY ASSURANCE.** ### The `3139`-byte file `b385` '
     'removed is the CRLF expansion of the `3068`-byte blob at `6de6336:.githooks/pre-push`, '
     'LF-identical to `323fd7a:tools/git-hooks/pre-push`. ### **RECOVERABLE FROM TWO TRACKED '
     'BLOBS** -- and the hazard it exposed is closed by the repair above'),
]


def newest_run(stem):
    cands = sorted(glob.glob(os.path.join(D, stem + '*.txt')))
    best, bstamp = None, ''
    for c in cands:
        s = run_clock.read_stamp(c) or ''
        if s >= bstamp:
            best, bstamp = c, s
    return best, bstamp


def do_desk():
    rec('    ### ### **THE EXERCISE VERDICT, READ FIRST BECAUSE ONE CLOSURE DEPENDS ON IT:**')
    rec('    ###   `data/b386_hooks.txt` carries `REPOS FAILING : 0` : ### **%s**' % EX_FAILING0)
    rec('    ###   repositories exercised in BOTH polarities and passing : ### **%d of 4**'
        % len(EX_ROWS))
    rec('    ###   ### ### **EXERCISE PASSED : %s**' % EXERCISE_OK)
    rec('')
    marks, refused, conditional = [], 0, 0
    for item, want, stem, sentence, why in DESK:
        row = dict(item=item, disposition=want, killing_stem=stem, why=why)
        if want == 'CLOSE':
            p, stamp = newest_run(stem)
            exists = bool(p) and os.path.exists(p)
            carries = False
            if exists:
                body = io.open(p, encoding='utf-8', errors='replace').read()
                carries = GN.norm(sentence) in GN.norm(body)
            row.update(exists=exists, carries=carries, sentence=sentence,
                       killing_file=(os.path.basename(p) if p else None), run_clock=stamp,
                       date=(stamp or '')[:10],
                       own_act=bool(p) and os.path.basename(p).startswith(ACT))
            if not (exists and carries):
                row['disposition'] = 'STAND'
                refused += 1
            # ### **THE ORDER`S CONDITION, APPLIED TO THE ONE ITEM IT NAMES.**
            if item == "the guard's own stale install line":
                row['conditional_on'] = 'Component 2 exercise'
                row['condition_met'] = EXERCISE_OK
                if not EXERCISE_OK:
                    row['disposition'] = 'STAND'
                    row['why'] = ('LEFT OPEN at b386: ### **THE EXERCISE DID NOT PASS**, and the '
                                  'order closes this item ONLY IF it does. ### The reason is in '
                                  '`data/b386_hooks.txt`')
                    why = row['why']
                    conditional += 1
        marks.append(row)
        rec('    %-78s %s' % (item, row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:340])
        if len(why) > 340:
            rec('              %s' % why[340:560])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d. ### CLOSURES '
        'REFUSED FOR WANT OF A KILLING SENTENCE : %d. ### REFUSED BY THE ORDER`S CONDITION : %d.**'
        % (len(marks), len(closed), len(stands), refused, conditional))
    rec('    ### ### ### **AND THE GUARD ITEM IS CLOSED ON A MEASURED CONDITION, NOT ON A')
    rec('    ### ### ### BELIEF.** ### `b385` filed it closed and had to withdraw it one act')
    rec('    ### later, because it wrote the closure before the check that would refute it ran.')
    rec('    ### ### **A CONDITIONAL CLOSURE WHOSE CONDITION IS NOT MEASURED IS AN UNCONDITIONAL')
    rec('    ### ### CLOSURE.**')
    rec('    ### ### **TWO ITEMS ARE ADDED AND LEFT STANDING**: the legacy copies, disposed of by')
    rec('    ### `(R15)`s third clause rather than deleted, and the untracked backups the')
    rec('    ### installer left. ### **NEITHER IS TIDIED AWAY BY AN ACT THAT WAS NOT ASKED TO.**')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, conditional_refusals=conditional, marks=marks,
                exercise_ok=EXERCISE_OK, exercise_rows=len(EX_ROWS),
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b386 — THE GUARD MADE SINGLE-SOURCED (2026-09-09)**',
        '',
        ('*No block above is edited. The b385 block (`%s`) and every block before it stand exactly '
         'as they were written — including the one that filed the guard item closed, which this '
         'act does not rewrite.*' % PRIOR),
        '',
        ('**THE AUTHOR RULED `(R15)`: ONE GUARD, ONE SOURCE.** *A guard has exactly one tracked '
         'source of truth in each repository, and whatever installs it reads from that source.* A '
         'second copy is deleted, made a pointer, or the repository reconfigured so the source is '
         'what runs. **Divergence between two copies of one guard is not a repair job; it is a '
         'topology defect, and the topology is what gets fixed.**'),
        '',
        ('**AND THE DEFECT WAS WIDER THAN b385 SAID.** The survey ran before the lock and counted '
         '**nine copies of the guard on disk, not two** — five tracked, four untracked, across '
         'the four rostered repositories. Every repository tracks `.githooks/pre-push`; `relay` '
         '**also** tracked `tools/git-hooks/pre-push`, which is what `b304_hooks.py` installed '
         'from; and each carries an untracked legacy `.git/hooks/pre-push`. **b385 repaired the '
         'installed copy in one repository, and the other three tracked copies still carried the '
         'stale line.** **0 copies matched no tracked blob**, so nothing this act deleted could '
         'destroy content — and that proof was printed **before** the deletion, which is the '
         'order b385 got wrong.'),
        '',
        ('**b385 PUT THREE OPTIONS AND OPTION (b) IS THE ONE THAT IMPLEMENTS `(R15)`.** All three '
         'were reproduced verbatim with their locations. *(a) repair the source, leaving both '
         'files* makes the copies agree and leaves **two tracked sources of truth** — it '
         'repairs the text and leaves the topology. *(c) neither* leaves both the copies and the '
         'divergence: **it is the state the ruling was written to end.** *(b) retire the source '
         'and repoint the installer* leaves **exactly one tracked source** per repository and '
         'makes **the installer read from it** — the ruling’s two clauses, in order. **No '
         'option was re-worded to make it fit, and this seat invented none.**'),
        '',
        ('**THE REPAIR, EXECUTED.** `relay/tools/git-hooks/pre-push` **deleted** under `(R15)`’s '
         'first disposal, after its recoverability was printed; `b304_hooks.py`’s `SOURCE` '
         '**repointed at `.githooks/pre-push`**, the file `core.hooksPath` makes git run. The '
         'installer was then run and **all four rostered repositories are LF-normalised-equal to '
         'that source’s own git blob and all four carry the repaired line** — compared '
         'against the blob, **never by filename and never by size alone**. **Exactly one tracked '
         'guard copy per repository.**'),
        '',
        ('**THE UNTRACKED LEGACY COPIES ARE DISPOSED OF, NOT DELETED — AND THAT IS A JUDGEMENT, '
         'MARKED AS ONE.** `(R15)`’s **third** disposal, *the repository is reconfigured so the '
         'source is what runs*, is already in force for them: `core.hooksPath = .githooks` in all '
         'four, verified. Deleting them would remove a working fallback if that setting were ever '
         'unset, and the order did not ask for it. **The author may overturn this.**'),
        '',
        ('**AND THE EXERCISE PASSES: `REPOS FAILING : 0`.** The guard was exercised in **both '
         'polarities in all four repositories** — refused from a non-`push-*` branch, allowed '
         'from one, HEAD and remote unchanged, the branch restored. b385’s arm predicate is '
         '**unchanged**: **the failing gate is cleared by the repair and not by the arm.**'),
        '',
        ('**THE INSTALLER’S SECOND DEFECT IS REPAIRED, AND WHAT IT DESTROYED IS IDENTIFIED.** '
         'The `3139`-byte backup b385 lost is the CRLF expansion of the `3068`-byte blob at '
         '`6de6336:.githooks/pre-push`, LF-identical to `323fd7a:tools/git-hooks/pre-push` — '
         '**recoverable from two tracked blobs**, shown by digest rather than asserted. The tool '
         'now **never overwrites an existing backup** and takes a fresh name instead. That '
         'invariant is **strictly stronger than the one the order asked for** — a file cannot '
         'be asked who wrote it — and the substitution is named rather than slipped in. '
         '**It fired for real on this act’s own run**: `SIDE-effects` already carried a backup, '
         'which survived byte-for-byte.'),
        '',
        ('**THE SEARCH LESSON IS MINTED AND, TESTED, IT IS MECHANIZABLE — WITH A LIMIT.** *A '
         'search for a rule uses the rule’s own words, not the name a reader gave it.* b383 '
         'searched for `reservoir`, `reviewer pool`, `reviewer budget`, `reviewers are finite`, '
         '`held in reserve`, `one reviewer` and reported a clean absence; b385 searched `SESSION '
         'PROTOCOL`, `mirror-refresh`, `reviewer set`, `not from recall`, `reviewer’s '
         'authority`, `Currency check`, `reservoir` and found it. The mechanizable shadow — '
         '**is each term attested anywhere in the corpus at all?** — scores **b383 at 2 of 6 '
         'and b385 at 7 of 7** on the sweep that excludes the b383–b386 records. Over the corpus '
         'as it stands it scores **6 of 6 and 7 of 7 and separates nothing**, because those acts’ '
         'own records now contain every one of b383’s terms: **an act’s own records make its '
         'terms attested afterwards**, so the check must exclude the records of the act it is '
         'checking. **And it does not reach the species**: it asks whether a term is attested, not '
         'whether it is the right one — b385’s own `reservoir` probe was attested and still '
         'wrong. **Necessary, not sufficient**, exactly as b378’s control rule turned out to be.'),
        '',
        ('**THE NAVIGATOR’S PARAPHRASE IS CORRECTED ON THE RECORD.** *The export’s manifest is '
         'the reviewer’s authority over recall* is **OVER-STATED**. The rule makes the '
         '**MANIFEST’s digest and `last-commit` columns** the authority; its *Currency check* '
         'widens the disagreement test to three fields — *version, md5, or last-commit* — '
         'and **neither place makes the whole manifest the authority**. **The correction is of a '
         'paraphrase and not of the rule: `REGISTRY.md` is byte-identical to its blob.**'),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No class ruled, no document reclassified, no declaration '
         'moved, no grade moved, no act re-verdicted, no list closed.** **No standard edited** and '
         '**no amendment applied** — the three b383 drafted that remain stay routed. **The '
         'citation question is restated as awaiting the author and is not moved**; no option was '
         'added and none preferred. `REGISTRY.md` was **read and not touched**. No archive file '
         'touched, no cluster opened, **the mirror roster not edited**, and **no `.git/hooks/'
         'pre-push` deleted in any repository**. The untracked `.b304-backup` artifacts the '
         'installer left are **named, not committed and not deleted**. A TECHNE module was written '
         'and **committed locally, not pushed**. No `.lean` file touched, no build run, no axiom '
         'profile recomputed. **The four open lists are restated OPEN by name.** h2 stands exactly '
         'where the deposit left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE GUARD MADE SINGLE-SOURCED UNDER (R15).** NO class ruled, NO document "
    "reclassified, NO declaration moved, NO grade moved, NO act re-verdicted, NO list closed. "
    "**NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the three b383 drafted that remain "
    "stay ROUTED AND UNAPPLIED. **REGISTRY.md WAS READ AND NOT TOUCHED AND THE RULE WAS NOT "
    "EDITED**; the correction is OF A PARAPHRASE AND NOT OF THE RULE. **THE CITATION QUESTION IS "
    "RESTATED AS AWAITING THE AUTHOR AND IS NOT MOVED**, no option added and none preferred. **THE "
    "THREE OPTIONS WERE REPRODUCED VERBATIM WITH THEIR LOCATIONS AND NONE WAS RE-WORDED TO MAKE IT "
    "FIT; THIS SEAT INVENTED NONE.** **THE RECOVERABILITY PROOF WAS PRINTED BEFORE THE DELETION "
    "AND NOT AFTER IT.** **NO COPY WAS DELETED THAT DID NOT MATCH A TRACKED BLOB.** **NO "
    ".git/hooks/pre-push WAS DELETED IN ANY REPOSITORY** -- (R15)'s THIRD disposal is already in "
    "force for them and that judgement is MARKED AS ONE. **THE INSTALLED GUARD WAS COMPARED "
    "AGAINST THE SOURCE'S OWN GIT BLOB, LF-NORMALISED, NEVER BY FILENAME AND NEVER BY SIZE "
    "ALONE.** **THE FAILING GATE WAS CLEARED BY THE REPAIR AND NOT BY THE ARM** -- b385's "
    "predicate is unchanged. **THE BACKUP INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE "
    "ASKED FOR AND IS NAMED AS A SUBSTITUTION.** **THE SEARCH CHECK WAS TESTED BEFORE IT WAS FILED "
    "AND ITS LIMIT IS STATED BESIDE IT: NECESSARY AND NOT SUFFICIENT.** **THE TECHNE MODULE IS "
    "LOCAL AND NOT PUSHED.** **THE UNTRACKED .b304-backup ARTIFACTS ARE NAMED, NOT COMMITTED AND "
    "NOT DELETED.** **THE FACE WAS NOT WIDENED MID-ACT.** **THE FOUR OPEN LISTS ARE RESTATED OPEN "
    "BY NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO ARCHIVE FILE TOUCHED, "
    "NO CLUSTER OPENED, THE MIRROR ROSTER NOT EDITED. NO .lean FILE TOUCHED, NO BUILD RUN, NO "
    "AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. "
    "NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the "
    "roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE "
    "PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
    "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the "
    "patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. "
    "THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left "
    "it and this act makes no claim about it in either direction. NOTHING IS DEPOSITED AND NOTHING "
    "WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE GUARD IS SINGLE-SOURCED UNDER (R15): ONE TRACKED COPY PER REPOSITORY, THE "
         "INSTALLER READING FROM IT, AND THE EXERCISE PASSING IN ALL FOUR** (b386, the guard made "
         "single-sourced)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b386, %d gates read and %d checked "
            "by digest. THE TOPOLOGY SURVEY RAN BEFORE THE LOCK AND THE FACE WAS WRITTEN FROM ITS "
            "NUMBERS: %d COPIES OF THE GUARD ON DISK, NOT TWO -- %d TRACKED AND %d UNTRACKED "
            "ACROSS FOUR REPOSITORIES, %d MATCHING NO TRACKED BLOB. b385 REPAIRED ONE INSTALLED "
            "COPY AND THE OTHER THREE TRACKED COPIES STILL CARRIED THE STALE LINE. b385'S THREE "
            "OPTIONS WERE REPRODUCED VERBATIM WITH THEIR LOCATIONS -- and NOT FROM ITS BANK, WHICH "
            "DOES NOT CARRY THEM, BUT FROM data/b385_closing.txt, WHICH DOES; the discrepancy with "
            "the order is REPORTED RATHER THAN SMOOTHED. OPTION (b) IS THE ONE THAT IMPLEMENTS "
            "(R15) because it leaves EXACTLY ONE TRACKED SOURCE and makes THE INSTALLER READ FROM "
            "IT; (a) repairs the text and leaves the topology, (c) is the state the ruling was "
            "written to end. NO OPTION WAS RE-WORDED AND NONE INVENTED. THE REPAIR: "
            "relay/tools/git-hooks/pre-push DELETED AFTER ITS RECOVERABILITY WAS PRINTED AND NOT "
            "AFTER IT WAS GONE, b304_hooks.py's SOURCE REPOINTED AT .githooks/pre-push, and ALL "
            "FOUR ROSTERED REPOSITORIES LF-NORMALISED-EQUAL TO THAT SOURCE'S OWN GIT BLOB WITH THE "
            "REPAIRED LINE, COMPARED AGAINST THE BLOB AND NEVER BY FILENAME OR SIZE. THE UNTRACKED "
            "LEGACY .git/hooks/pre-push COPIES ARE DISPOSED OF BY (R15)'S THIRD CLAUSE AND NOT "
            "DELETED, core.hooksPath VERIFIED IN ALL FOUR, AND THAT JUDGEMENT IS MARKED AS ONE. "
            "THE EXERCISE PASSES IN BOTH POLARITIES IN ALL FOUR: REPOS FAILING 0, AND THE FAILING "
            "GATE IS CLEARED BY THE REPAIR AND NOT BY THE ARM. THE INSTALLER'S BACKUP DEFECT IS "
            "REPAIRED -- IT NEVER OVERWRITES AN EXISTING BACKUP, AN INVARIANT STRICTLY STRONGER "
            "THAN THE ONE ASKED FOR AND NAMED AS A SUBSTITUTION, FIXTURED IN BOTH POLARITIES AND "
            "FIRING FOR REAL ON THIS ACT'S OWN RUN. THE %d-BYTE BACKUP b385 DESTROYED IS "
            "IDENTIFIED AS THE CRLF EXPANSION OF 6de6336:.githooks/pre-push AND IS RECOVERABLE "
            "FROM TWO TRACKED BLOBS. THE SEARCH LESSON IS MINTED AND TESTED: the mechanizable "
            "shadow scores b383 at %d of %d attested and b385 at %d of %d on the sweep excluding "
            "those acts' own records, and SEPARATES NOTHING on the contaminated sweep BECAUSE AN "
            "ACT'S OWN RECORDS MAKE ITS TERMS ATTESTED AFTERWARDS -- filed %s WITH ITS LIMIT "
            "STATED BESIDE IT, NECESSARY AND NOT SUFFICIENT. AND THE NAVIGATOR'S PARAPHRASE IS "
            "CORRECTED: THE AUTHORITY IS THE MANIFEST'S DIGEST AND last-commit COLUMNS, NOT THE "
            "MANIFEST WHOLESALE, WHICH IS OVER-STATED"
            % (LG['gates_read'], LG['face_subject_gates'],
               E['copies_total'], E['copies_tracked'], E['copies_untracked'],
               E['copies_unrecoverable'], C3['lost_bytes'],
               C4['attestation_rows'][1][1], C4['attestation_rows'][1][2],
               C4['attestation_rows'][1][3], C4['attestation_rows'][1][4], C4['filing']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "CORPUS DOCUMENT. ### A guard was made single-sourced and a tool was repaired; every "
            "quoted line was re-read out of its own file at its own line number, with %d failing. "
            "### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED. "
            "### FIXING A TOPOLOGY IS NOT RULING A CLASS, AND MINTING A CHECK IS NOT ADOPTING IT "
            "AS AN ARM THAT DECIDES" % len(AC['reread_failures']))
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, "
            "NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### NO STANDARD WAS EDITED, "
            "NO AMENDMENT WAS APPLIED, THE RULE WAS NOT EDITED AND REGISTRY.md WAS READ AND NOT "
            "TOUCHED. ### NO ARCHIVE FILE TOUCHED, NO CLUSTER OPENED, THE MIRROR ROSTER NOT "
            "EDITED, AND NO .git/hooks/pre-push DELETED IN ANY REPOSITORY")
    grade = ("### EXECUTED-UNDER-THE-AUTHOR'S-RULING, AND THE CONDITION WAS MEASURED BEFORE THE "
             "CLOSURE WAS FILED. ### b385 FILED THIS ITEM CLOSED AND HAD TO WITHDRAW IT; THIS ACT "
             "RAN THE EXERCISE FIRST AND CLOSED ON ITS RESULT. ### A CONDITIONAL CLOSURE WHOSE "
             "CONDITION IS NOT MEASURED IS AN UNCONDITIONAL CLOSURE. ### THE PROOF WAS PRINTED "
             "BEFORE THE DELETION. ### THE ARM WAS NOT WIDENED AND THE FACE WAS NOT WIDENED "
             "MID-ACT. ### ONE JUDGEMENT IS MARKED AS A JUDGEMENT AND LEFT FOR THE AUTHOR TO "
             "OVERTURN. ### AND ONE SUBSTITUTED INVARIANT IS NAMED AS A SUBSTITUTION RATHER THAN "
             "PRESENTED AS THE THING ASKED FOR")
    status = ("data/b386_the_guard_single_sourced.txt; data/%s; data/%s; data/b386_hooks.txt; "
              "data/b386_install_run.txt; data/b386_registration_2026-09-09.txt (LOCKED before "
              "any write, chained on tools/b378_lockgate.py run as b386); tools/b386_extract.py; "
              "tools/b386_components.py; tools/b386_desk_bank.py; tools/b386_checks.py; relay "
              "tools/b304_hooks.py (SOURCE repointed and the backup defect repaired, both DECLARED "
              "ON THE LOCKED FACE); relay tools/git-hooks/pre-push (DELETED); "
              ".githooks/pre-push in all four rostered repositories (the repaired line, written by "
              "the installer); TECHNE-Core modules/2026-09/SEARCH_BY_THE_RULES_OWN_WORDS.md (LOCAL, "
              "NOT PUSHED); PLACE-papers OPEN_TRAILS.md (an append-only block); CORRESPONDENCE.md "
              "row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('one guard one source', 'the guard made single sourced',
           'the second tracked guard copy deleted', 'the installer repointed',
           'a search uses the rule own words')
MUST_NOT_HIT = ('the guard has two sources', 'a copy was deleted unchecked',
                'the arm was widened', 'a techne module was pushed')


def do_key(rownum):
    KEY = 'the-guard-made-single-sourced-under-r15'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE GUARD IS SINGLE-SOURCED UNDER THE AUTHOR'S RULING (R15), ONE GUARD ONE SOURCE. THE "
        "SURVEY RAN BEFORE THE LOCK AND COUNTED %d COPIES ON DISK, NOT TWO -- %d TRACKED, %d "
        "UNTRACKED, %d MATCHING NO TRACKED BLOB -- and b385 HAD REPAIRED ONLY ONE OF THEM. b385'S "
        "THREE OPTIONS WERE REPRODUCED VERBATIM WITH THEIR LOCATIONS, FROM data/b385_closing.txt "
        "AND NOT FROM ITS BANK, WHICH DOES NOT CARRY THEM. OPTION (b) IMPLEMENTS (R15): it leaves "
        "EXACTLY ONE TRACKED SOURCE per repository and makes THE INSTALLER READ FROM IT. (a) "
        "repairs the text and leaves the topology; (c) is the state the ruling was written to end. "
        "NO OPTION WAS RE-WORDED AND NONE INVENTED. relay/tools/git-hooks/pre-push WAS DELETED "
        "AFTER ITS RECOVERABILITY WAS PRINTED AND NOT AFTER IT WAS GONE; b304_hooks.py's SOURCE "
        "WAS REPOINTED AT .githooks/pre-push; ALL FOUR ROSTERED REPOSITORIES ARE "
        "LF-NORMALISED-EQUAL TO THAT SOURCE'S OWN GIT BLOB AND CARRY THE REPAIRED LINE. THE "
        "UNTRACKED LEGACY .git/hooks/pre-push COPIES ARE DISPOSED OF BY (R15)'S THIRD CLAUSE AND "
        "NOT DELETED, AND THAT JUDGEMENT IS MARKED AS ONE. THE EXERCISE PASSES IN BOTH POLARITIES "
        "IN ALL FOUR, REPOS FAILING 0, AND THE FAILING GATE IS CLEARED BY THE REPAIR AND NOT BY "
        "THE ARM. THE INSTALLER NEVER OVERWRITES AN EXISTING BACKUP NOW -- STRICTLY STRONGER THAN "
        "THE INVARIANT ASKED FOR, NAMED AS A SUBSTITUTION, AND IT FIRED FOR REAL ON THIS ACT'S RUN. "
        "THE %d-BYTE BACKUP b385 DESTROYED IS RECOVERABLE FROM TWO TRACKED BLOBS. THE SEARCH "
        "LESSON IS MINTED AND TESTED: A SEARCH FOR A RULE USES THE RULE'S OWN WORDS, NOT THE NAME "
        "A READER GAVE IT, and its mechanizable shadow scores b383 %d/%d and b385 %d/%d attested "
        "on the sweep excluding those acts' own records while SEPARATING NOTHING on the "
        "contaminated one -- filed %s, NECESSARY AND NOT SUFFICIENT. THE NAVIGATOR'S PARAPHRASE IS "
        "CORRECTED: THE AUTHORITY IS THE MANIFEST'S DIGEST AND last-commit COLUMNS, NOT THE "
        "MANIFEST WHOLESALE."
        % (E['copies_total'], E['copies_tracked'], E['copies_untracked'],
           E['copies_unrecoverable'], C3['lost_bytes'],
           C4['attestation_rows'][1][1], C4['attestation_rows'][1][2],
           C4['attestation_rows'][1][3], C4['attestation_rows'][1][4], C4['filing']))
    grade = (
        "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED. ### NO CLASS WAS RULED, NO "
        "DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO "
        "LIST CLOSED. ### THE RULE WAS NOT EDITED AND REGISTRY.md WAS READ AND NOT TOUCHED -- THE "
        "CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE. ### THE CITATION QUESTION IS AWAITING "
        "THE AUTHOR AND WAS NOT MOVED. ### THE RECOVERABILITY PROOF WAS PRINTED BEFORE THE "
        "DELETION. ### NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY. ### THE FAILING GATE "
        "WAS CLEARED BY THE REPAIR AND NOT BY THE ARM. ### THE FACE WAS NOT WIDENED MID-ACT. ### "
        "THE TECHNE MODULE IS LOCAL AND NOT PUSHED. ### THE UNTRACKED BACKUPS ARE NAMED, NOT "
        "COMMITTED AND NOT DELETED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW "
        "TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### "
        "NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b386_the_guard_single_sourced.txt; data/%s; data/%s; data/b386_hooks.txt; "
        "data/b386_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b386 -- %d gates read, %d checked by digest); "
        "tools/b386_extract.py; tools/b386_components.py; tools/b386_desk_bank.py; "
        "tools/b386_checks.py; relay tools/b304_hooks.py; relay tools/git-hooks/pre-push "
        "(DELETED); .githooks/pre-push in all four rostered repositories; TECHNE-Core "
        "modules/2026-09/SEARCH_BY_THE_RULES_OWN_WORDS.md (LOCAL, NOT PUSHED); PLACE-papers "
        "OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b386 (the author's ruling (R15) executed: one tracked guard per repository, the "
           "installer repointed at it, the exercise passing in all four; the installer's backup "
           "defect repaired; the search lesson minted and tested; the navigator's paraphrase "
           "corrected)")
    row_new = ('    # ### THE GUARD MADE SINGLE-SOURCED (b386).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        rec('    %-40s NO KEY before : %s' % (q, pre[q]))
    KEY_ANCHOR = 'KEYS = {\n'
    ROW_ANCHOR = ('INDEX = [\n'
                  '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')
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
    rec('  READ BACK : %s returns %d row(s)  %s'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-44s reaches the b386 key : %s' % (q, g))
    for lbl, cond in (('the ruling is named and executed', '(R15)' in out),
                      ('the survey counted nine copies, not two',
                       ('%d COPIES ON DISK, NOT TWO' % E['copies_total']) in out),
                      ('option (b) is the one that implements it',
                       'OPTION (b) IMPLEMENTS (R15)' in out),
                      ('no option re-worded or invented',
                       'NO OPTION WAS RE-WORDED AND NONE INVENTED' in out),
                      ('the proof came before the deletion',
                       'AFTER ITS RECOVERABILITY WAS PRINTED AND NOT AFTER IT WAS GONE' in out),
                      ('all four match the blob and carry the line',
                       "LF-NORMALISED-EQUAL TO THAT SOURCE'S OWN GIT BLOB AND CARRY THE REPAIRED "
                       "LINE" in out),
                      ('the legacy copies are disposed of, not deleted',
                       "NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY" in out),
                      ('the gate was cleared by the repair, not the arm',
                       'CLEARED BY THE REPAIR AND NOT BY THE ARM' in out),
                      ('the backup invariant is named a substitution',
                       'NAMED AS A SUBSTITUTION' in out),
                      ('the lost backup is recoverable',
                       'RECOVERABLE FROM TWO TRACKED BLOBS' in out),
                      ('the search species is banked',
                       "A SEARCH FOR A RULE USES THE RULE'S OWN WORDS, NOT THE NAME A READER GAVE "
                       "IT" in out),
                      ('the check is necessary and not sufficient',
                       'NECESSARY AND NOT SUFFICIENT' in out),
                      ('the paraphrase correction is exact',
                       "THE AUTHORITY IS THE MANIFEST'S DIGEST AND last-commit COLUMNS" in out),
                      ('the rule itself was not edited',
                       'THE RULE WAS NOT EDITED AND REGISTRY.md WAS READ AND NOT TOUCHED' in out),
                      ('the face was not widened mid-act',
                       'THE FACE WAS NOT WIDENED MID-ACT' in out),
                      ('the techne module is not pushed',
                       'THE TECHNE MODULE IS LOCAL AND NOT PUSHED' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('no new tracking document in the corpus',
                       'NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        g = pre[q] and no_key(o)
        ok = ok and g
        rec('    %-40s NO KEY after  : %s' % (q, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    rec('=' * 100)
    rec('b386 -- THE DESK UNDER (R7), THE THREE CLOSING WRITES, AND THE BANK.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()
    Q['lists_closed'] = 0

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True,
                  before_bytes=len(before.encode('utf-8')), after_bytes=len(before.encode('utf-8')))
    else:
        rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
        body = chr(10).join(trail_block(Q)) + chr(10)
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
        committed = r.stdout.decode('utf-8', 'replace')
        ao = after.startswith(before)
        pi = (committed.replace(chr(13) + chr(10), chr(10))
              in after.replace(chr(13) + chr(10), chr(10)))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before),
                  before_bytes=len(before.encode('utf-8')),
                  after_bytes=len(after.encode('utf-8')))
    seg = after.split(MARK, 1)[-1]
    tr['says_exercise_passes'] = 'REPOS FAILING : 0' in seg
    tr['says_judgement_marked'] = 'that is a judgement, marked as one' in seg.lower()
    rec('  ### ### **THE BLOCK SAYS THE EXERCISE PASSED : %s ; AND MARKS THE JUDGEMENT AS ONE : '
        '%s**' % (tr['says_exercise_passes'], tr['says_judgement_marked']))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b386_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b386_desk_notes', LINES)
        return 1
    g1 = ('THE GUARD IS SINGLE-SOURCED UNDER (R15)' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'COPIES OF THE GUARD ON DISK, NOT TWO' in ROWS[0][1]
          and 'REPRODUCED VERBATIM WITH THEIR LOCATIONS' in ROWS[0][1]
          and 'WHICH DOES NOT CARRY THEM' in ROWS[0][1]
          and 'OPTION (b) IS THE ONE THAT IMPLEMENTS' in ROWS[0][1]
          and 'NO OPTION WAS RE-WORDED AND NONE INVENTED' in ROWS[0][1]
          and 'AFTER ITS RECOVERABILITY WAS PRINTED AND NOT AFTER IT WAS GONE' in ROWS[0][1]
          and 'NEVER BY FILENAME OR SIZE' in ROWS[0][1]
          and "(R15)'S THIRD CLAUSE AND NOT DELETED" in ROWS[0][1]
          and 'REPOS FAILING 0' in ROWS[0][1]
          and 'CLEARED BY THE REPAIR AND NOT BY THE ARM' in ROWS[0][1]
          and 'NAMED AS A SUBSTITUTION' in ROWS[0][1]
          and 'RECOVERABLE FROM TWO TRACKED BLOBS' in ROWS[0][1]
          and 'NECESSARY AND NOT SUFFICIENT' in ROWS[0][1]
          and 'OVER-STATED' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'FIXING A TOPOLOGY IS NOT RULING A CLASS' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'REGISTRY.md WAS READ AND NOT TOUCHED' in ROWS[0][3]
          and 'A CONDITIONAL CLOSURE WHOSE CONDITION IS NOT MEASURED' in ROWS[0][4]
          and 'MARKED AS A JUDGEMENT' in ROWS[0][4]
          and 'THE GUARD MADE SINGLE-SOURCED UNDER (R15)' in ROWS[0][5]
          and 'THE FACE WAS NOT WIDENED MID-ACT' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the ruling, the stamped gate, the nine copies, the verbatim options and '
        'where they were, the implementing option, the proof before the deletion, the blob '
        'comparison, the third disposal, the passing exercise, the substituted invariant, the '
        'recoverable backup, the tested check and its limit, the corrected paraphrase, and the '
        'scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b386_desk_notes', LINES)
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
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
        cells = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        ok = (got[-1] == start and C.blank_cells(back) == 0
              and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
              and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cells], back.startswith(txt.rstrip(chr(10))),
               'PASS' if ok else '### FAIL ###'))
        if not ok:
            run_clock.write(D, 'b386_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b386 -- THE GUARD MADE SINGLE-SOURCED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE AUTHOR RULED `(R15)`: ONE GUARD, ONE SOURCE -- AND THE DEFECT WAS')
    B.append('### ### ### WIDER THAN `b385` SAID.**')
    B.append('### The survey ran BEFORE the lock and counted ### **`%d` COPIES OF THE GUARD ON'
             % E['copies_total'])
    B.append('### ### DISK, NOT TWO** -- `%d` tracked and `%d` untracked across four repositories,'
             % (E['copies_tracked'], E['copies_untracked']))
    B.append('### with ### **`%d` MATCHING NO TRACKED BLOB.** ### `b385` repaired ONE installed'
             % E['copies_unrecoverable'])
    B.append('### copy; the other three tracked copies still carried the stale line.')
    B.append('### ### ### **A FACE WRITTEN FROM A BELIEF ABOUT THE TOPOLOGY WOULD HAVE FAILED THE')
    B.append('### ### ### SAME WAY `b385`S DID. ### THIS ONE WAS WRITTEN FROM THE SURVEY.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE THREE OPTIONS, AND THE ONE THAT IMPLEMENTS `(R15)`.')
    B.append(SUB)
    B.append('### ### **ONE DISCREPANCY WITH THE ORDER, REPORTED RATHER THAN SMOOTHED:** ### the')
    B.append('### order says to reproduce the options ### *from its bank*, and ### **`b385`S BANK')
    B.append('### ### DOES NOT CARRY THEM : %s.** ### They are in `data/b385_closing.txt`, in that'
             % C1['options_in_bank385'])
    B.append('### act`s DRAFT for this one, and the quotation names where it came from.')
    B.append('### ### **OPTIONS REPRODUCED VERBATIM WITH THEIR LOCATIONS : `%d`. ### INVENTED BY'
             % C1['options_quoted'])
    B.append('### ### THIS SEAT : `%d`. ### RE-WORDED TO MAKE THEM FIT : `0`.**'
             % C1['options_invented'])
    B.append('###   ### **`(a)` REPAIR THE SOURCE, LEAVING BOTH FILES -- DOES NOT IMPLEMENT.** ###')
    B.append('###     It makes the copies AGREE and leaves ### **TWO TRACKED SOURCES OF TRUTH.**')
    B.append('###     ### `(R15)` calls the divergence ### **A TOPOLOGY DEFECT** ### -- `(a)`')
    B.append('###     repairs the text and leaves the topology.')
    B.append('###   ### **`(b)` RETIRE THE SOURCE AND REPOINT THE INSTALLER -- IMPLEMENTS.** ###')
    B.append('###     Exactly one tracked source per repository, and ### **THE INSTALLER READS')
    B.append('###     ### FROM IT** -- the ruling`s two clauses, in order. ### The retirement is')
    B.append('###     `(R15)`s ### **FIRST DISPOSAL.**')
    B.append('###   ### **`(c)` NEITHER -- DOES NOT IMPLEMENT.** ### It leaves both the copies and')
    B.append('###     the divergence. ### **IT IS THE STATE THE RULING WAS WRITTEN TO END.**')
    B.append('### ### ### **OPTION `%s` WAS EXECUTED.**' % C1['chosen'])
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE REPAIR, AND THE ORDER OF OPERATIONS.')
    B.append(SUB)
    B.append('### ### **THE RECOVERABILITY PROOF WAS PRINTED BEFORE THE DELETION : %s.**'
             % C2['proof_before_deletion'])
    B.append('### `relay/tools/git-hooks/pre-push` matched ### **%s**'
             % ', '.join('`%s`' % x for x in C2['recoverable_from']))
    B.append('### ### ### **THAT IS THE ORDER `b385` GOT WRONG** -- it removed a file and worked')
    B.append('### ### ### out afterwards what had been in it. ### **THE ARM AGAINST IT IS AN')
    B.append('### ### ### ORDERING ARM, NOT A CONTENT ARM.**')
    B.append('### ### **TRACKED GUARD COPIES DELETED : `%d`.** ### `relay` now tracks %s.'
             % (C2['deleted'], C2['tracked_pre_push_in_relay']))
    B.append('### ### **THE INSTALLER`S `SOURCE` REPOINTED AT `.githooks/pre-push` : %s** -- the'
             % C2['repointed'])
    B.append('### file `core.hooksPath` makes git run.')
    B.append('')
    B.append('### ### **THE INSTALLED GUARD, AGAINST THE SOURCE`S OWN GIT BLOB (`%s`):**'
             % C2['blob_sha'][:16])
    for r in C2['install_rows']:
        B.append('###   %-22s %5d bytes   blob-equal (LF) : %-5s   repaired line : %-5s   '
                 'hooksPath `%s`'
                 % (r['repo'], r['bytes'], r['matches_blob'], r['carries_repaired_line'],
                    r['hooks_path']))
    B.append('### ### **ALL FOUR EQUAL TO THE BLOB : %s. ### ALL FOUR CARRY THE REPAIRED LINE : '
             '%s.**' % (C2['all_match_blob'], C2['all_carry_line']))
    B.append('### ### ### **COMPARED AGAINST THE BLOB AND `LF`-NORMALISED. ### NEVER BY FILENAME,')
    B.append('### ### ### AND NEVER BY SIZE ALONE** -- `core.autocrlf` makes the working file')
    B.append('### CRLF while the blob stays LF (`b309`), so a working-file comparison would fail')
    B.append('### on a correct install.')
    B.append('')
    B.append('### ### **THE UNTRACKED LEGACY `.git/hooks/pre-push` COPIES : `%d` DELETED.**'
             % C2['legacy_deleted'])
    for r in C2['legacy']:
        B.append('###   %-22s present : %-5s   core.hooksPath `%s`   ### INERT : %s'
                 % (r['repo'], r['exists'], r['hooks_path'], r['hooks_path'] == '.githooks'))
    B.append('### ### **`(R15)`S THIRD DISPOSAL -- *the repository is reconfigured so the source')
    B.append('### ### is what runs* -- IS ALREADY IN FORCE FOR THESE**, verified in each')
    B.append('### repository above.')
    B.append('### ### ### **AND THAT IS A JUDGEMENT, MARKED AS ONE:** ### deleting them would')
    B.append('### ### ### remove a working fallback if `core.hooksPath` were ever unset, and the')
    B.append('### ### ### order did not ask for that. ### **THE AUTHOR MAY OVERTURN IT.**')
    B.append('')
    B.append('### ### ### **AND THE EXERCISE PASSES.**')
    B.append('###   ### **`REPOS FAILING : %s`** ### and ### **`%d` OF 4 EXERCISED IN BOTH'
             % ('0' if EX_FAILING0 else 'NOT 0', len(EX_ROWS)))
    B.append('###   ### POLARITIES AND PASSING** -- refused from a non-`push-*` branch, allowed')
    B.append('###   from one, HEAD and remote unchanged, the branch restored.')
    B.append('### ### **`b385`S ARM PREDICATE IS UNCHANGED. ### THE FAILING GATE IS CLEARED BY THE')
    B.append('### ### REPAIR AND NOT BY THE ARM.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE INSTALLER`S SECOND DEFECT.')
    B.append(SUB)
    B.append('### ### **WHAT WAS LOST, NAMED WITH ITS NUMBERS.** ### The removed')
    B.append('### `.githooks/pre-push.b304-backup` was ### **`%d` BYTES**, which is exactly the'
             % C3['lost_bytes'])
    B.append('### CRLF expansion of the `3068`-byte blob at `6de6336:.githooks/pre-push`')
    B.append('### (sha `%s`), and that blob is LF-identical to' % C3['lost_sha'][:16])
    B.append('### `323fd7a:tools/git-hooks/pre-push` : ### **%s.**' % C3['lf_identical'])
    B.append('### ### ### **`(F2)` IS MET: THE LOST CONTENT IS RECOVERABLE FROM A TRACKED BLOB --')
    B.append('### ### ### FROM TWO OF THEM**, shown by digest rather than asserted.')
    B.append('### ### **AND ONE THING THE RECOVERY DOES NOT UNDO:** ### the backup existed to hold')
    B.append('### what was on disk before an install. ### **THIS ONE HELD NOTHING THE RECORD DID')
    B.append('### ### NOT ALREADY TRACK.** ### Had it held an untracked local edit, ### **IT WOULD')
    B.append('### ### HAVE BEEN GONE** -- and that is the hazard the repair removes.')
    B.append('')
    B.append('### ### **THE TOOL REPAIRED : %s.** ### It ### **NEVER OVERWRITES AN EXISTING'
             % C3['tool_repaired'])
    B.append('### ### BACKUP** ### and takes a fresh name instead.')
    B.append('### ### ### **THE INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE THE ORDER')
    B.append('### ### ### ASKED FOR.** ### The order said ### *a backup it did not create*; ### a')
    B.append('### file cannot be asked who wrote it, so the tool refuses to overwrite ANY existing')
    B.append('### backup. ### **A STRONGER INVARIANT SUBSTITUTED FOR A WEAKER ONE IS STILL A')
    B.append('### ### SUBSTITUTION**, and it is named rather than slipped in.')
    B.append('### ### **FIXTURED IN BOTH POLARITIES : %s** ### (`%d` of `%d`) -- a backup the tool'
             % (C3['polarities_held'], C3['polarities'], 2))
    B.append('### may write, and a foreign one that must survive byte-for-byte.')
    B.append('### ### ### **AND IT FIRED FOR REAL ON THIS ACT`S OWN INSTALL RUN:** ###')
    B.append('### `SIDE-effects` already carried a `.b304-backup`, which ### **SURVIVED')
    B.append('### ### BYTE-FOR-BYTE** ### while the new one went to `.b304-backup-1`. ### **A')
    B.append('### ### FIXTURE PROVES A TOOL IN A TEMPORARY DIRECTORY; THIS PROVED IT IN THE')
    B.append('### ### ROSTER.**')
    B.append('### ### **DISPOSITION : %s. ### ROUTED : %s.**' % (C3['disposition'], C3['routed']))
    B.append('### The repair is INSIDE this act`s face, which names `tools/b304_hooks.py`. ###')
    B.append('### **A COMPONENT ROUTED FOR WANT OF A FACE THIS ACT WROTE ITSELF WOULD BE THIS SEAT')
    B.append('### ### ROUTING ITS OWN OMISSION.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE TWO FILINGS.')
    B.append(SUB)
    B.append('### ### ### **(i) `A SEARCH FOR A RULE USES THE RULE`S OWN WORDS, NOT THE NAME A`')
    B.append('### ### ### `READER GAVE IT`.**')
    B.append('### ### **INCIDENT ONE -- `b383`, A CLEAN ABSENCE THAT WAS WRONG.** ### Terms:')
    B.append('###   %s' % ', '.join('`%s`' % t for t in E['b383_terms']))
    B.append('### ### **INCIDENT TWO -- `b385`, THE SAME RULE, LOCATED.** ### Terms:')
    B.append('###   %s' % ', '.join('`%s`' % t for t in E['b385_terms']))
    B.append('')
    B.append('### ### **IS IT MECHANIZABLE? ### THE ANSWER IS A RESULT, NOT AN OPINION.**')
    B.append('### ### **THE LESSON ITSELF IS NOT:** ### a check for the rule`s own words needs the')
    B.append('### rule, and the rule is what the search was for.')
    B.append('### ### **THE SHADOW IS:** ### is each term ### **ATTESTED ANYWHERE IN THE CORPUS AT')
    B.append('### ### ALL?** ### A term that occurs nowhere cannot find anything.')
    for lbl, a3, t3, a5, t5, ctl in C4['attestation_rows']:
        B.append('###   %-38s `b383` %d/%d attested   `b385` %d/%d   (control fired on %d files)'
                 % (lbl, a3, t3, a5, t5, ctl))
    B.append('### ### **IT SEPARATES THE TWO INCIDENTS ON THE UNCONTAMINATED SWEEP : %s.**'
             % C4['separates_clean'])
    B.append('### ### **AND IT SEPARATES NOTHING ON THE CONTAMINATED ONE**, because')
    B.append('### ### **`b383`-`b385`S OWN RECORDS NOW CONTAIN EVERY ONE OF `b383`S TERMS.**')
    B.append('### ### ### **THAT CONTAMINATION IS ITSELF THE FINDING:** ### an act`s own records')
    B.append('### ### ### make its terms attested afterwards, so ### **THE CHECK MUST EXCLUDE THE')
    B.append('### ### ### RECORDS OF THE ACT IT IS CHECKING** -- `b368`s sweep rule, one level')
    B.append('### out.')
    B.append('### ### ### **FILED AS : %s.**' % C4['filing'])
    B.append('### ### **AND ITS LIMIT IS STATED BESIDE IT, NOT BELOW IT:** ### it asks whether a')
    B.append('### term is attested, ### **NOT WHETHER IT IS THE RIGHT TERM.** ### `b385`s own')
    B.append('### `reservoir` probe was attested and still wrong. ### **NECESSARY AND NOT')
    B.append('### ### SUFFICIENT**, exactly as `b378`s positive-control rule turned out to be --')
    B.append('### and ### **A RULE THAT IS NECESSARY AND NOT SUFFICIENT IS NOT LISTED BESIDE THE')
    B.append('### ### ARMS THAT DECIDE.**')
    B.append('### ### **THE TECHNE MODULE:** ### `%s`, committed locally at `%s` and'
             % (C4['techne']['path'], C4['techne']['head']))
    B.append('### ### **NOT PUSHED : %s.**' % (not C4['techne']['pushed']))
    B.append('')
    B.append('### ### ### **(ii) THE NAVIGATOR`S PARAPHRASE, CORRECTED ON THE RECORD.**')
    B.append('### ### **THE STATEMENT:** ### *the export`s manifest is the reviewer`s authority')
    B.append('### ### over recall.* ### **MARK : OVER-STATED.**')
    B.append('### ### **THE CORRECTION, IN THE RULE`S TERMS:** ### the authority is ### **THE')
    B.append('### ### MANIFEST`S DIGEST AND `last-commit` COLUMNS**, not the manifest wholesale.')
    B.append('### The ### *Currency check* ### widens the disagreement test to three fields --')
    B.append('### ### *version, md5, or last-commit* ### -- and ### **NEITHER PLACE MAKES THE')
    B.append('### ### WHOLE MANIFEST THE AUTHORITY.**')
    B.append('### ### ### **THE CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE.** ###')
    B.append('### `REGISTRY.md` differs from its blob : ### **%s.**' % C4['registry_dirty'])
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### ### **AND THE GUARD ITEM IS CLOSED ON A MEASURED CONDITION.** ### The order')
    B.append('### closes it ### *only if Component 2`s exercise passes*; the exercise ran BEFORE')
    B.append('### this writer and the record was read, not assumed. ### **A CONDITIONAL CLOSURE')
    B.append('### ### WHOSE CONDITION IS NOT MEASURED IS AN UNCONDITIONAL CLOSURE**, which is what')
    B.append('### `b385` filed.')
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-guard-made-single-sourced-under-r15` reachable by every alias : %s'
             % kok)
    B.append('')
    B.append('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION')
    B.append('### ### WAS MOVED. ### NO GRADE WAS MOVED. ### NO ACT WAS RE-VERDICTED. ### NO LIST')
    B.append('### ### WAS CLOSED.**')
    B.append('### ### **NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the three `b383`')
    B.append('### drafted that remain stay ### **ROUTED AND UNAPPLIED.**')
    B.append('### ### **THE RULE WAS NOT EDITED AND `REGISTRY.md` WAS READ AND NOT TOUCHED.**')
    B.append('### ### **THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND IS NOT')
    B.append('### ### MOVED** -- no option added, none preferred.')
    B.append('### ### **NO ARCHIVE FILE TOUCHED. ### NO CLUSTER OPENED. ### THE MIRROR ROSTER NOT')
    B.append('### ### EDITED. ### NO `.git/hooks/pre-push` DELETED IN ANY REPOSITORY.**')
    B.append('### ### **THE UNTRACKED `.b304-backup` ARTIFACTS THE INSTALLER LEFT ARE NAMED, NOT')
    B.append('### ### COMMITTED AND NOT DELETED** -- an act that was not asked to tidy them does')
    B.append('### not tidy them.')
    B.append('### ### **THE FACE WAS NOT WIDENED MID-ACT.** ### Every write this act made is named')
    B.append('### on the face that was locked before the first of them.')
    B.append('### ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this')
    B.append('### act makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **`(F1)` MET IN SUBSTANCE AND REFUTED IN ITS DESCRIPTION.** ### The disposal')
    B.append('### that implements `(R15)` IS deletion plus a repointed installer, exactly as the')
    B.append('### navigator said. ### But the copy deleted was ### **TRACKED, NOT AT AN UNTRACKED')
    B.append('### ### PATH** -- `git ls-files` carried both `.githooks/pre-push` AND')
    B.append('### `tools/git-hooks/pre-push`. ### The untracked copies are the `.git/hooks/` ones,')
    B.append('### and ### **THIS ACT DELETED NONE OF THEM.** ### The substance was right and the')
    B.append('### name for the file was not.')
    B.append('### ### **`(F2)` MET, BY DIGEST.** ### `%d` bytes = the CRLF expansion of a `3068`-'
             % C3['lost_bytes'])
    B.append('### byte tracked blob, recoverable from two refs.')
    B.append('### ### **`(E1)` MET.** ### The exercise passes in every rostered repository.')
    B.append('### ### **`(E2)` MET.** ### `relay` ALREADY IDENTICAL; the three repositories still')
    B.append('### carrying the stale line REPLACED.')
    B.append('### ### **`(E3)` MET.** ### Component 3 is `%s` and not routed.' % C3['disposition'])
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `A SEARCH FOR A RULE USES THE RULE`S OWN WORDS, NOT THE NAME A`')
    B.append('### ### ### `READER GAVE IT`.** ### Mechanizable only in shadow, and the shadow is')
    B.append('### ### **NECESSARY AND NOT SUFFICIENT.**')
    B.append('### ### ### **NEW -- `AN ACT`S OWN RECORDS MAKE ITS TERMS ATTESTED AFTERWARDS`.** ###')
    B.append('### So a check on a past search must exclude the records of the act it is checking.')
    B.append('### **`b368`S SWEEP RULE, ONE LEVEL OUT.**')
    B.append('### ### ### **NEW -- `A CONDITIONAL CLOSURE WHOSE CONDITION IS NOT MEASURED IS AN`')
    B.append('### ### ### `UNCONDITIONAL CLOSURE`.** ### `b385` filed the guard item closed before')
    B.append('### the check that refuted it ran.')
    B.append('### ### ### **NEW -- `A STRONGER INVARIANT SUBSTITUTED FOR A WEAKER ONE IS STILL A`')
    B.append('### ### ### `SUBSTITUTION`.** ### It is named, not slipped in.')
    B.append('### ### ### **NEW -- `A FIXTURE PROVES A TOOL IN A TEMPORARY DIRECTORY; THE ROSTER`')
    B.append('### ### ### `PROVES IT IN THE WORLD`.** ### The backup repair fired for real on the')
    B.append('### same run that fixtured it.')
    B.append('### **MET AGAIN -- `A FILE MOVED IS NOT A FILE REPLACED`** (`b385`), and the')
    B.append('### topology behind it is now fixed rather than the text. ### **MET AGAIN -- AN')
    B.append('### EXIT CODE ABOVE ZERO IS NOT AN ANSWER** (`b378`): this act invoked')
    B.append('### `gate_hash.py --stamp`, a flag that does not exist, and read its self-test`s')
    B.append('### exit `0` as a stamp. ### **THE LOCK GATE CAUGHT IT AND REFUSED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b386_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b386_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by '
             'digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### The extract`s clock is `%s` and the lock`s is `%s`.'
             % (E.get('run_clock'), (m_at.group(1) if m_at else '?')))
    for n in ('b386_reads', 'b386_lockgate', 'b386_components'):
        j = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, j['run_file'], j.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**'
             % (E['reads'], E['without_anchor'], E['anchors_differing']))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLASS WAS RULED.', '### A STANDARD WAS EDITED.',
                '### AN OPTION WAS INVENTED.', '### A COPY WAS DELETED UNCHECKED.',
                '### THE ARM WAS WIDENED.', '### THE RULE WAS EDITED.',
                '### A TECHNE MODULE WAS PUSHED.', '### THE FACE WAS WIDENED MID-ACT.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))

    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; closed %d ; trail appended %s ; row %s ; key %s ; exercise %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok, EXERCISE_OK))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b386_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b386_the_guard_single_sourced.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b386_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and EXERCISE_OK and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
