# -*- coding: utf-8 -*-
"""b397_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **THE ONLY CORPUS WRITE THIS ACT MAKES IS `(R21)`'S, AND `b397_components.py` MADE IT.**
### This file writes the ledgers and the bank, and closes what `(R7)` permits.
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
MARK = '<!-- b397 the unlanded work: eight of nine landed, and a queue with triggers -->'
PRIOR = '<!-- b396 how many findings rest on a backtick: 82 figures at risk -->'

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


SEALTXT = io.open(os.path.join(D, 'b397_registration_2026-09-10.txt'),
                  encoding='utf-8').read()
SEALHASH = re.search(r'sha256 of every byte ABOVE this block : ([0-9a-f]{64})', SEALTXT).group(1)
SEALSTAMP = re.search(r'locked at \(UTC\) : (\S+)', SEALTXT).group(1)

AC = J('b397_components')
LG = J('b397_lockgate')
E = J('b397_reads')
C1, C2, C4 = AC['c1'], AC['c2'], AC['c4']
S1, S2, S3 = E['s1'], E['s2'], E['s3']
BANKOUT = os.path.join(D, 'b397_the_unlanded_work.txt')


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


# ### ### **COMPONENT 3 IS THE DESK'S OWN SHAPE THIS ACT:** ### six items carry a
# ### ### **TRIGGER** ### instead of a priority, under `(R22)`. ### **A TRIGGER SAYS WHEN AN ITEM
# ### ### BECOMES RIPE; IT DOES NOT SAY THE ITEM WILL BE DONE.**
TRIGGERS = [
    ('the `82` at-risk figures',
     'a figure is re-run WHEN AN ACT DEPENDS ON IT, not before'),
    ('the ten now-reachable keystones, for content reading',
     'read WHEN ITS CLUSTER IS NEXT WORKED, or when a claim of its depends on a result the '
     'record has moved'),
    ('the two deposited records` remediation',
     'BEFORE ANY WAVE, and ### **THE AUTHOR PERFORMS IT**'),
    ('`ENUMERA`, the keystone naming no terminal',
     'it needs ### **AN AUTHOR**'),
    ('the two anchorless clusters` first syntheses',
     'WHEN EITHER IS NEXT WORKED, under the many-to-many rule, ### **NOT OWED**'),
    ('the keystone with no correspondence table',
     'writing one is ### **AUTHORING**'),
]

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND',
     'PARKED by the author`s ruling, and ### **NOW PARKED A SECOND TIME BY `(R22)` FOR THE '
     'INSTRUMENT-AUDIT LANE**'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### This act dates none. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the practice that let the phantom drift run', 'STAND',
     'TWO INSTANCES in four acts, and ### **THIS ACT FOUND A THIRD IN A DIFFERENT MEDIUM:** ### '
     'eight branches landed and the keystones still call them held. ### **STILL OPEN**'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392'),
    ('the anchor question, unanswerable for three of five', 'STAND', 'ROUTED at b393'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the self-reading / corpus-reading distinction', 'STAND',
     'FILED at b396 as a limit, not applied as a filter'),
    ('the five deafnesses of b396`s sweep', 'STAND',
     'FILED at b396; ### **EVERY `CONFIRMED` IN THAT ACT STANDS IN FRONT OF THEM**'),
    ('the judgement half of the preservation rule', 'STAND',
     'FILED at b396: `>` is sufficient and not necessary, so the arm is a FLOOR'),

    # ---- WHAT THIS ACT CLOSES ---------------------------------------------------------------------
    ('the fifteen keystones not read', 'CLOSE',
     '### **CLOSED BY `(R22)` AND BY THE QUEUE.** ### The item has stood since `b394` and was '
     'priced at `b396`. ### `(R22)` rules that remaining work goes to the trails ### **WITH A '
     'TRIGGER**, and it now has one: ### *read when its cluster is next worked, or when a claim '
     'of its depends on a result the record has moved.* ### **THE ITEM IS NOT DISCHARGED AND IS '
     'NOT LOST -- IT IS QUEUED**, which is what the ruling asks for'),
    ('the `82` at-risk figures, unrepaired', 'CLOSE',
     '### **CLOSED BY `(R22)`: THE INSTRUMENT-AUDIT LANE IS PARKED.** ### `b396` measured them '
     'and `6` of `6` re-runs CONFIRMED; the ruling states that ### **NO FURTHER ACT SWEEPS '
     'INSTRUMENTS FOR THEIR OWN SAKE.** ### The item is queued with its trigger: ### *a figure '
     'is re-run when an act depends on it, not before*'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the keystones` stale `HELD` prose', 'STAND',
     '### **NEW at `b397`, AND IT IS THE ACT`S LARGEST FINDING.** ### `8` of `9` research '
     'branches are ### **FULLY MERGED INTO `main`** ### and the keystones still describe their '
     'terminals as `HELD`, `UNMERGED` or `BRANCH-RESIDENT`. ### **THE WORK LANDED AND THE PROSE '
     'DID NOT FOLLOW IT.** ### The disclosure rule licenses a STATUS CELL, not a paragraph, so '
     '### **REWRITING THE PROSE IS AUTHORING** ### and this act did not. ### **ROUTED. OPEN**'),
    ('the disclosure rule`s own worked instance is stale', 'STAND',
     '### **NEW at `b397`.** ### `REGISTRY.md:%d` names `word-pairing-interface` as ### *the '
     'held, unmerged branch* ### carrying `THE_RESIDUE_OF_RH`\'s terminals, and that branch is '
     '### **MERGED.** ### **THE RULE DEMANDS A DISCLOSURE THAT IS NO LONGER TRUE**, which is the '
     'clearest instance of the defect the rule itself guards against. ### **AMENDING A STANDING '
     'RULE IS THE AUTHOR`S. ### ROUTED. OPEN**' % S3['rule_registry_line']),
    ('`derivative-engine` carries no printed axiom profile', 'STAND',
     '### **NEW at `b397`.** ### `%d` declarations sit on the branch and `%d` are absent from '
     '`main`; the only profile artefact is a `#print axioms` ### **SOURCE SCRIPT** ### saying '
     '*Expected: ... axiom-free.* ### **EXPECTED IS NOT PRINTED**, so every axiom claim about '
     'that branch in this act is ### **NOT BUILT.** ### One build would settle it and ### '
     '**`(R22)` AND THE PARKED INSTRUMENT LANE FORBID IT.** ### **ROUTED TO THE AUTHOR. OPEN**'
     % (len(S2['decls']), S2['absent'])),
    ('the keystone rows asserting profiles for an unbuilt ref', 'STAND',
     '### **NEW at `b397`, SEEN AND NOT TOUCHED.** ### The `%d` rows this act disclosed assert '
     '`axiom-free (none)` and `{propext, Classical.choice, Quot.sound}` for terminals whose ref '
     'carries ### **NO PRINTED PROFILE.** ### **MOVING A GRADE IS NOT THIS ACT`S SCOPE AND NO '
     'GRADE WAS MOVED.** ### **ROUTED. OPEN**' % C2['repaired']),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES TWO ITEMS BY QUEUEING THEM, WHICH IS WHAT `(R22)` ASKS')
    rec('    ### ### FOR.** ### The ruling parks the instrument-audit lane and sends remaining')
    rec('    ### ### items to the trails ### **WITH A TRIGGER EACH** -- consulted when something')
    rec('    ### ### depends on them, not swept because they exist.')
    rec('    ### ### ### **A QUEUED ITEM IS NOT A DISCHARGED ITEM.** ### Neither is lost, and the')
    rec('    ### ### ### trail block carries the trigger so a later act meets it there.')
    rec('    ### ### **AND FOUR ITEMS OPEN, THE FIRST OF WHICH IS THIS ACT`S LARGEST FINDING.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 900), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **AND THE QUEUE, WITH ITS TRIGGERS : %d ITEMS.**' % len(TRIGGERS))
    for it, tg in TRIGGERS:
        rec('        %-56s TRIGGER: %s' % (it[:56], tg[:110]))
    rec('    ### ### **EACH ENTRY NAMES ITS TRIGGER AND ### NOTHING IS OPENED.**')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks, triggers=len(TRIGGERS))


SCOPE = (
    "**SCOPE: THE UNLANDED WORK -- AND EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED.** "
    "RULING (R22) IS RECORDED: THE INSTRUMENT-AUDIT LANE IS PARKED, remaining audit items go to "
    "the trails WITH A TRIGGER EACH, no further act sweeps instruments for their own sake, and "
    "READING THE CORPUS FOR CONTENT IS NOT AUDIT WORK. b395's partition named ten keystones whose "
    "own text calls their terminals HELD, UNMERGED, RETIRED or BRANCH-RESIDENT; counted IN BOTH "
    "DIRECTIONS with --merged as an independent third witness, the 9 research branches divide 8 "
    "FULLY MERGED and 1 CARRYING COMMITS main DOES NOT HAVE (SIDE-kernel/derivative-engine, 4), "
    "with 2 push branches EXCLUDED AS MECHANICAL and named. **SO THE HELD LANGUAGE IN THOSE "
    "KEYSTONES IS A CORRECTION THAT NEVER PROPAGATED -- THE WORK LANDED AND THE PROSE DID NOT "
    "FOLLOW IT**, b394's species in a new medium. **AND THE COUNTING TRAP IS ON THE RECORD:** "
    "rev-list --left-right --count main...b puts the count of commits ONLY IN MAIN on the left, an "
    "earlier form of the survey read it as ahead, and EIGHT MERGED BRANCHES READ AS ONE COMMIT "
    "AHEAD -- THE EXACT OPPOSITE OF THE TRUTH -- caught by one branch reading 0 0. The live branch "
    "carries 72 declarations of which 4 ARE ABSENT FROM main, the citation test being AGAINST main "
    "AND NOT THE MERGE BASE: invariance_barrier and DeterminedBy already stand on main and are "
    "citable; exactly_c1_derives, onLine_doubleZero_iff_imDeriv_zero and "
    "no_onLine_double_iff_transversal are cited by keystones while NO DEFAULT BRANCH CARRIES THEM; "
    "and derivGrade is CITED BY NOTHING. **THERE IS NO PRINTED PROFILE ON THE REF**, only a "
    "#print axioms SOURCE SCRIPT saying Expected: axiom-free, so every axiom claim about that "
    "branch here is NOT BUILT -- **NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD**, a commit "
    "message is not a printed profile, and NO BUILD IS RUN. **(F1) IS THEREFORE NOT ESTABLISHED** "
    "and was declared so on the face before the components ran: derivGrade is uncited and absent "
    "from main but COMPILED needs a printed profile, and it is a def rather than a theorem. THE "
    "DISCLOSURE RULE IS QUOTED FROM REGISTRY.md AND THE_KEYSTONE_CENSUS.md, **AND ITS OWN WORKED "
    "INSTANCE IS STALE**: it names word-pairing-interface as the held, unmerged branch and that "
    "branch is MERGED, so writing the demanded disclosure into that row WOULD PUT A FALSE "
    "STATEMENT IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE. THE RULE IS NOT STRUCK AND NOT "
    "AMENDED HERE; its instance is ROUTED. THE SWEEP: 15 ROWS SWEPT, 6 REPAIRED, 8 "
    "SWEPT-NOT-REPAIRED, 1 ROUTED, REPORTED APART AND NEVER ADDED; a row is annotated ONLY where "
    "its terminal is absent from main; 2 documents edited, 0 CONTENT LOST, the pre-edit lines "
    "preserved verbatim in an appended annotation, and numstat's in-place deletions printed and "
    "not suppressed. **(F2) IS MET -- 6 OF 15 -- BUT NOT FOR THE REASON THE ORDER GAVE**: not "
    "that rows already disclose in a preamble, but that MOST SWEPT ROWS' TERMINALS HAVE SINCE "
    "LANDED, and a prediction met for the wrong reason is reported with the reason. THE QUEUE "
    "CARRIES 6 ITEMS EACH WITH A TRIGGER AND NOTHING IS OPENED. THE BOARD IS QUOTED FROM THE "
    "CLAUSE ANCHOR AND THE FACES LEDGER WITH 0 NEW CLAIMS. **NOTHING WAS MERGED, PUSHED TO ANY "
    "BRANCH, FETCHED, CREATED OR CHECKED OUT; EVERY REPOSITORY'S BRANCH AND HEAD IS "
    "BYTE-IDENTICAL BEFORE AND AFTER; 0 CLONES, 0 BUILDS, NO .lean FILE TOUCHED IN ANY "
    "REPOSITORY.** NO RULE STRUCK OR AMENDED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CLASS RULED, "
    "NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO PRIOR ACT'S FACE BANK OR "
    "INSTRUMENT EDITED, NO KEYSTONE PROSE REWRITTEN. NOTHING DEPOSITS; **THE PLATFORM WAS NOT "
    "CALLED AT ALL.** **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME, NOW WITH TRIGGERS "
    "ATTACHED.** NO NEW TRACKING DOCUMENT WAS CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE "
    "MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push DELETED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED, NOW BY (R22) AS WELL. THE WAVE STAYS PARKED. THE POSTURE LOCK "
    "IS SEPARATE. h2 stands exactly where the deposit left it and this act makes no claim about it "
    "in either direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b397 — THE UNLANDED WORK (2026-09-10)**',
        '',
        ('*No block above is edited. The b396 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**RULING (R22), THE AUTHOR\u2019S, RATIFIED BY THE FERRY AND STRIKEABLE: THE '
         'INSTRUMENT-AUDIT LANE IS PARKED.** b396 measured the shape-narrow predicate as pervasive '
         'and its six tested figures as confirmed, and the arc\u2019s one moved finding was found '
         'by **reading a document rather than by widening a matcher**. Remaining audit items go to '
         'these trails **with a TRIGGER each** — consulted when something depends on them, not '
         'swept because they exist. **No further act sweeps instruments for their own sake.** '
         '*Reading the corpus for CONTENT is not audit work and is not parked by this ruling.*'),
        '',
        ('**EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED, AND WHAT IS STALE IS THE PROSE.** '
         'b395\u2019s partition named ten keystones whose own text calls their terminals `HELD`, '
         '`UNMERGED`, `RETIRED` or `BRANCH-RESIDENT`. Counted **in both directions**, with '
         '`--merged` read as an independent third witness, the `%d` research branches divide: '
         '**`%d` carry nothing `main` lacks**, and **`%d` carries commits `main` does not have** — '
         '`SIDE-kernel/derivative-engine`, at `4`. Two further branches are `push-*` branches and '
         'are **excluded as mechanical**, named so the classification is visible. **The work '
         'landed and the prose did not follow it** — the *corrected but unpropagated* species this '
         'seat minted at b394, this time about a branch status rather than a version string. '
         '*Rewriting a paper\u2019s prose about its own terminals is authoring; the disclosure '
         'rule licenses a status cell, not a paragraph. Routed.*'
         % (C1['research'], C1['landed'], C1['live'])),
        '',
        ('**AND THE COUNTING TRAP IS ON THE RECORD, BECAUSE IT NEARLY INVERTED THE FINDING.** '
         '`rev-list --left-right --count main...b` puts the count of commits **only in main** on '
         'the left. An earlier form of the survey read that number as `ahead`, and **eight merged '
         'branches read as one commit ahead of main** — *the exact opposite of the truth*. It was '
         'caught by one branch reading `0 0`, a shape the misreading could not explain.'),
        '',
        ('**THE ONE LIVE BRANCH, AND THE INVENTORY IS SMALLER THAN THE QUESTION.** `%d` '
         'declarations sit on `derivative-engine` and **`%d` are absent from `main`**. The '
         'citation test is **against `main`, where a reader resolves it** — not against the merge '
         'base — and two names the branch appears to add (`invariance_barrier`, `DeterminedBy`) '
         '**already stand on `main`** and are citable. Of the four that do not: '
         '`exactly_c1_derives`, `onLine_doubleZero_iff_imDeriv_zero` and '
         '`no_onLine_double_iff_transversal` are **cited by keystones while no default branch '
         'carries them**, and `derivGrade` is **cited by nothing**. **There is no printed profile '
         'on the ref** — the only candidate is a `#print axioms` *source script* whose own comment '
         'says *Expected: … axiom-free* — so every axiom claim about that branch here is **NOT '
         'BUILT**. *No evidence of a build is not evidence of no build*, a commit message is not a '
         'printed profile, and **no build is run**: (R22) and the parked instrument lane forbid '
         'it. **(F1) is therefore NOT ESTABLISHED**, declared on the face before the components '
         'ran: `derivGrade` is uncited and absent from `main`, but *compiled* needs a printed '
         'profile and it is a `def` rather than a theorem.'
         % (C1['decls'], C1['absent'])),
        '',
        ('**THE DISCLOSURE RULE, APPLIED WHERE IT IS TRUE — AND ITS OWN WORKED INSTANCE IS '
         'STALE.** `REGISTRY.md` states that a terminal not on a default branch *belongs in the '
         'status column where a table-reader meets it*, and `THE_KEYSTONE_CENSUS.md` raises it to '
         'a release-blocking line: **a disclosure requirement, not a repair — the branch is sound, '
         'the terminals compile, and the only defect would be letting a reader assume otherwise.** '
         'The rule\u2019s worked instance names `word-pairing-interface` as *the held, unmerged '
         'branch* carrying `THE_RESIDUE_OF_RH`\u2019s terminals — **and that branch is merged.** '
         'Writing the demanded disclosure into that row **would put a false statement in a status '
         'column under the authority of a rule.** The rule is **not struck and not amended here**; '
         'its instance is **routed**. The sweep: **`%d` rows swept, `%d` repaired, `%d` '
         'swept-not-repaired, `%d` routed** — reported apart and never added. A row is annotated '
         '**only** where its terminal is absent from `main`; `%d` documents were edited with **`%d` '
         'content lost**, the pre-edit lines preserved verbatim in an appended annotation. **(F2) '
         'is met — `%d` of `%d` — but not for the reason the order gave**: not that rows already '
         'disclose in a preamble, but that **most swept rows\u2019 terminals have since landed**, '
         'so no disclosure is owed at all. *A prediction met for the wrong reason is reported with '
         'the reason.*'
         % (C2['swept'], C2['repaired'], C2['already'], C2['routed'], C2['docs'], C2['lost'],
            C2['repaired'], C2['swept'])),
        '',
        ('**THE QUEUE, WITH TRIGGERS — `%d` ITEMS, AND NOTHING IS OPENED.** Under (R22) each names '
         'when it becomes **ripe**, not how urgent it is:' % len(TRIGGERS)),
        '',
    ] + ['- **%s** — *TRIGGER:* %s' % (it, tg) for it, tg in TRIGGERS] + [
        '',
        ('**A trigger is not a plan and a queue is not a commitment.** **The four lists stay '
         'OPEN by name, now with triggers attached.** **Nothing deposits and the platform was not '
         'called at all.** **Nothing was merged, pushed to any branch, fetched, created or checked '
         'out; every repository\u2019s branch and HEAD is byte-identical before and after; `0` '
         'clones, `0` builds, and no `.lean` file touched in any repository.**'),
        '',
    ]


def corr_rows(Q):
    m = ("**EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED, THE UNLANDED INVENTORY IS FOUR "
         "DECLARATIONS ON ONE BRANCH, AND THE DISCLOSURE RULE'S OWN WORKED INSTANCE IS STALE** "
         "(b397, the unlanded work)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b397, %d gates read and %d checked "
            "by digest. RULING (R22) IS RECORDED: THE INSTRUMENT-AUDIT LANE IS PARKED, remaining "
            "audit items go to the trails WITH A TRIGGER EACH, and READING THE CORPUS FOR CONTENT "
            "IS NOT AUDIT WORK. Counted IN BOTH DIRECTIONS with --merged as a third witness, the "
            "%d research branches divide %d FULLY MERGED and %d CARRYING COMMITS main DOES NOT "
            "HAVE, with 2 push branches excluded as mechanical. **SO THE HELD LANGUAGE IN THOSE "
            "KEYSTONES IS A CORRECTION THAT NEVER PROPAGATED -- THE WORK LANDED AND THE PROSE DID "
            "NOT FOLLOW IT.** THE COUNTING TRAP IS ON THE RECORD: --left-right puts the main-only "
            "count on the left, an earlier form read it as ahead, and EIGHT MERGED BRANCHES READ "
            "AS ONE AHEAD -- THE EXACT OPPOSITE OF THE TRUTH -- caught by one branch reading 0 0. "
            "The live branch carries %d declarations of which %d ARE ABSENT FROM main, tested "
            "AGAINST main AND NOT THE MERGE BASE; %d are cited by keystones while no default "
            "branch carries them and %d is cited by nothing. **THERE IS NO PRINTED PROFILE ON THE "
            "REF**, only a #print axioms SOURCE SCRIPT saying Expected, so every axiom claim here "
            "is NOT BUILT -- NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD -- and (F1) IS NOT "
            "ESTABLISHED, declared on the face before the components ran. THE DISCLOSURE RULE IS "
            "QUOTED FROM REGISTRY.md:%d AND THE_KEYSTONE_CENSUS.md:%d AND ITS WORKED INSTANCE NAMES "
            "A BRANCH THAT IS MERGED, so writing the demanded disclosure there WOULD PUT A FALSE "
            "STATEMENT IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE; the rule is NOT STRUCK "
            "AND NOT AMENDED and its instance is ROUTED. %d ROWS SWEPT, %d REPAIRED, %d "
            "SWEPT-NOT-REPAIRED, %d ROUTED, reported apart; %d documents edited with %d CONTENT "
            "LOST. (F2) IS MET BUT NOT FOR THE REASON GIVEN: most swept rows' terminals HAVE SINCE "
            "LANDED. THE QUEUE CARRIES %d ITEMS EACH WITH A TRIGGER AND NOTHING IS OPENED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['research'], C1['landed'],
               C1['live'], C1['decls'], C1['absent'], C1['cited'], C1['uncited'],
               S3['rule_registry_line'], S3['rule_census_line'], C2['swept'], C2['repaired'],
               C2['already'], C2['routed'], C2['docs'], C2['lost'], Q['triggers']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### Eleven refs across six kernel "
            "repositories were READ by git show, rev-list and ls-tree; NOTHING WAS MERGED, PUSHED, "
            "FETCHED, CREATED OR CHECKED OUT, every repository's branch and HEAD is BYTE-IDENTICAL "
            "BEFORE AND AFTER, and 0 BUILDS WERE RUN. ### READING A BRANCH IS NOT LANDING IT")
    prof = ("### NO AXIOM PROFILE IS ASSERTED FOR THE LIVE BRANCH; EVERY ONE IS NOT BUILT. ### NO "
            ".lean FILE WAS TOUCHED IN ANY REPOSITORY AND NOTHING WAS COMPUTED ABOUT THE OBJECT. "
            "### NO RULE STRUCK OR AMENDED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO "
            "DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT "
            "EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE PROSE REWRITTEN. ### NOTHING "
            "DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### EVERY BRANCH CARRIES AN AHEAD COUNT, A BEHIND COUNT AND A --merged VERDICT, EACH "
             "BY ITS OWN COMMAND, AND THE MISREADING THAT NEARLY INVERTED THE FINDING IS NAMED "
             "WITH THE NUMBER IT PRODUCED. ### CITABILITY IS TESTED AGAINST main. ### AN UNKNOWN "
             "IS REPORTED AS NOT BUILT AND THE EVIDENCE IS NAMED APART. ### A ROW IS ANNOTATED "
             "ONLY WHERE THE DISCLOSURE IS TRUE, AND ROWS SWEPT AND REPAIRED ARE REPORTED APART. "
             "### 0 CONTENT LOST AND numstat's IN-PLACE DELETIONS PRINTED. ### EVERY QUEUE ENTRY "
             "NAMES A TRIGGER AND 0 ITEMS ARE OPENED. ### THE BOARD IS QUOTATION WITH 0 NEW CLAIMS")
    status = ("data/b397_the_unlanded_work.txt; data/%s; data/%s; "
              "data/b397_registration_2026-09-10.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b397); tools/b397_extract.py; tools/b397_regspec.py; "
              "tools/b397_reg_gate.py; tools/b397_components.py; tools/b397_desk_bank.py; "
              "tools/b397_checks.py; PLACE-papers %d keystone status cells with one appended "
              "annotation each, and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file'], C2['repaired']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what is on the held branches', 'were the held branches already landed',
           'what has the programme compiled that it cannot cite',
           'is the disclosure rule stale', 'what is the queue and what are its triggers',
           'what does the research board say')
MUST_NOT_HIT = ('a branch was merged', 'a branch was checked out', 'a build was run',
                'the platform was called')


def do_key(rownum):
    KEY = 'the-unlanded-work'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b397 READ THE HELD BRANCHES FOR CONTENT AND FOUND THAT %d OF THE %d RESEARCH BRANCHES "
        "WERE ALREADY FULLY MERGED INTO main. Only SIDE-kernel/derivative-engine carries commits "
        "main does not have. **SO THE HELD / UNMERGED / BRANCH-RESIDENT LANGUAGE IN THOSE "
        "KEYSTONES IS A CORRECTION THAT NEVER PROPAGATED: THE WORK LANDED AND THE PROSE DID NOT "
        "FOLLOW IT**, b394's species in a new medium, and rewriting the prose is AUTHORING so it "
        "is ROUTED. THE COUNTING TRAP IS ON THE RECORD: rev-list --left-right --count main...b "
        "puts the MAIN-ONLY count on the left, an earlier form of the survey read it as ahead, and "
        "EIGHT MERGED BRANCHES READ AS ONE COMMIT AHEAD -- THE EXACT OPPOSITE OF THE TRUTH -- "
        "caught by one branch reading 0 0. The live branch carries %d declarations of which %d ARE "
        "ABSENT FROM main, tested AGAINST main AND NOT THE MERGE BASE: invariance_barrier and "
        "DeterminedBy already stand on main and are citable; %d are cited by keystones while no "
        "default branch carries them; and derivGrade is CITED BY NOTHING. THERE IS NO PRINTED "
        "PROFILE ON THE REF -- only a #print axioms SOURCE SCRIPT saying Expected -- so every "
        "axiom claim about that branch is NOT BUILT, NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO "
        "BUILD, and (F1) IS NOT ESTABLISHED, declared on the face before the components ran. THE "
        "DISCLOSURE RULE'S OWN WORKED INSTANCE IS STALE: it names word-pairing-interface as the "
        "held unmerged branch and that branch is MERGED, so writing the demanded disclosure would "
        "PUT A FALSE STATEMENT IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE; NOT STRUCK, NOT "
        "AMENDED, ROUTED. %d ROWS SWEPT, %d REPAIRED, %d SWEPT-NOT-REPAIRED, %d ROUTED, reported "
        "apart, %d documents edited with %d CONTENT LOST. (F2) IS MET BUT NOT FOR THE REASON "
        "GIVEN. RULING (R22) PARKS THE INSTRUMENT-AUDIT LANE and the queue carries %d ITEMS EACH "
        "WITH A TRIGGER, NOTHING OPENED."
        % (C1['landed'], C1['research'], C1['decls'], C1['absent'], C1['cited'],
           C2['swept'], C2['repaired'], C2['already'], C2['routed'], C2['docs'], C2['lost'],
           len(TRIGGERS)))
    grade = (
        "### NOTHING WAS MERGED, PUSHED, FETCHED, CREATED OR CHECKED OUT; EVERY REPOSITORY'S "
        "BRANCH AND HEAD IS BYTE-IDENTICAL BEFORE AND AFTER; 0 CLONES AND 0 BUILDS. ### NO .lean "
        "FILE TOUCHED IN ANY REPOSITORY. ### NO RULE STRUCK OR AMENDED, NO GRADE MOVED, NO CLAIM "
        "WITHDRAWN, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW "
        "EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE PROSE "
        "REWRITTEN. ### THE ONLY CORPUS WRITE IS A STATUS CELL WHERE THE DISCLOSURE IS TRUE, PLUS "
        "ONE APPENDED ANNOTATION PER EDITED DOCUMENT PRESERVING THE PRE-EDIT LINES VERBATIM. ### "
        "AN UNKNOWN IS REPORTED AS NOT BUILT. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED "
        "AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH TRIGGERS. ### M-2 "
        "UNCHANGED")
    where = (
        "data/b397_the_unlanded_work.txt; data/%s; data/%s; "
        "data/b397_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b397 -- %d gates read, %d checked by digest); "
        "tools/b397_extract.py; tools/b397_regspec.py; tools/b397_reg_gate.py; "
        "tools/b397_components.py; tools/b397_desk_bank.py; tools/b397_checks.py; "
        "PLACE-papers keystone status cells and OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b397 (eight of the nine held branches were already landed; the unlanded inventory is '
           "four declarations on one branch; and the disclosure rule's own worked instance is "
           'stale)')
    row_new = ('    # ### THE UNLANDED WORK (b397).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where,
                  chr(10)))
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
        rec('    %-52s reaches the b397 key : %s' % (qq, g2))
    for lbl, cond in (('eight of nine were already landed',
                       'WERE ALREADY FULLY MERGED INTO main' in out),
                      ('the prose is what is stale',
                       'THE PROSE DID NOT FOLLOW IT' in out),
                      ('the counting trap is recorded',
                       'THE EXACT OPPOSITE OF THE TRUTH' in out),
                      ('citability is tested against main',
                       'AGAINST main AND NOT THE MERGE BASE' in out),
                      ('no printed profile, so not built',
                       'THERE IS NO PRINTED PROFILE ON THE REF' in out),
                      ('no evidence of a build is not evidence of no build',
                       'NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD' in out),
                      ('(F1) is not established', '(F1) IS NOT ESTABLISHED' in out),
                      ('the rule`s instance is stale', "WORKED INSTANCE IS STALE" in out),
                      ('a false disclosure was refused',
                       'FALSE STATEMENT IN A STATUS COLUMN' in out),
                      ('swept and repaired are apart', 'SWEPT-NOT-REPAIRED' in out),
                      ('(R22) parks the audit lane',
                       'PARKS THE INSTRUMENT-AUDIT LANE' in out),
                      ('the queue carries triggers and nothing opened',
                       'WITH A TRIGGER, NOTHING OPENED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    bar('=')
    rec('b397 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
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
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True)
    else:
        rec('  ### the b394 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        committed = blob('OPEN_TRAILS.md')
        ao = after.startswith(before)
        pi = committed in after.replace(chr(13) + chr(10), chr(10))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before))
    seg = after.split(MARK, 1)[-1]
    low = seg.lower()
    tr['says_r22'] = 'the instrument-audit lane is parked' in low
    tr['says_content_not_audit'] = 'is not audit work' in low
    tr['says_eight_landed'] = 'carry nothing `main` lacks' in low
    tr['says_prose_stale'] = 'the prose did not follow it' in low
    tr['says_counting_trap'] = 'the exact opposite of the truth' in low
    tr['says_against_main'] = 'where a reader resolves it' in low
    tr['says_not_built'] = 'not\nbuilt' in low or 'not built' in low
    tr['says_no_evidence'] = 'no evidence of a build is not evidence of no build' in low
    tr['says_f1_not_established'] = '(f1) is therefore not established' in low
    tr['says_instance_stale'] = 'and that branch is merged' in low
    tr['says_false_disclosure_refused'] = 'false statement in a status\ncolumn' in low \
        or 'false statement in a status column' in low
    tr['says_apart'] = 'reported apart and never added' in low
    tr['says_triggers'] = 'a trigger is not a plan' in low
    tr['says_lists_open'] = 'lists stay\nopen by name' in low or 'lists stay open by name' in low
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:** ### %s'
        % {k: v for k, v in tr.items() if k.startswith('says_')})

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
        run_clock.write(D, 'b397_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b397_desk_notes', LINES)
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
            run_clock.write(D, 'b397_desk_notes', LINES)
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
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b397 -- THE UNLANDED WORK. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED. ### WHAT IS')
    B.append('### ### ### UNLANDED IS FOUR DECLARATIONS ON ONE BRANCH, AND WHAT IS STALE IS THE')
    B.append('### ### ### PROSE.**')
    B.append('')
    B.append(SUB)
    B.append('### RULING `(R22)`, RECORDED.')
    B.append(SUB)
    B.append('### ### **THE INSTRUMENT-AUDIT LANE IS PARKED**, the author`s, ratified by the')
    B.append('### ### paste and strikeable. ### Remaining audit items go to the trails ###')
    B.append('### ### **WITH A TRIGGER EACH** -- consulted when something depends on them, not')
    B.append('### ### swept because they exist. ### **NO FURTHER ACT SWEEPS INSTRUMENTS FOR THEIR')
    B.append('### ### OWN SAKE.**')
    B.append('### ### **AND THE CLAUSE THAT KEEPS THIS ACT LEGAL:** ### *reading the corpus for')
    B.append('### ### CONTENT is not audit work and is not parked by this ruling.*')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE BRANCHES, COUNTED IN BOTH DIRECTIONS.')
    B.append(SUB)
    B.append('###   %-22s %-26s %-6s %-7s %-7s' % ('repo', 'branch', 'AHEAD', 'behind', 'merged'))
    for x in S1['rows']:
        B.append('###   %-22s %-26s %-6d %-7d %-7s %s'
                 % (x['repo'], x['branch'], x['ahead'], x['behind'], x['merged'],
                    '(a push branch, excluded)' if x['push'] else ''))
    B.append('### ### **RESEARCH BRANCHES `%d` ; PUSH BRANCHES EXCLUDED AS MECHANICAL `%d`.**'
             % (C1['research'], C1['push']))
    B.append('### ### **FULLY MERGED, CARRYING NOTHING `main` LACKS : `%d`.**' % C1['landed'])
    B.append('### ### **CARRYING COMMITS `main` DOES NOT HAVE : `%d`.**' % C1['live'])
    B.append('### ### ### **SO THE `HELD` LANGUAGE IN THOSE KEYSTONES IS A CORRECTION THAT NEVER')
    B.append('### ### ### PROPAGATED. ### THE WORK LANDED AND THE PROSE DID NOT FOLLOW IT** --')
    B.append('### ### ### `b394`s species, in a new medium.')
    B.append('')
    B.append('### **THE COUNTING TRAP, RECORDED BECAUSE IT NEARLY INVERTED THE FINDING:**')
    B.append('### `rev-list --left-right --count main...b` puts the count of commits ###')
    B.append('### **ONLY IN MAIN** ### on the left. ### An earlier form of the survey read it as')
    B.append('### `ahead`, and ### **EIGHT MERGED BRANCHES READ AS ONE COMMIT AHEAD OF MAIN --')
    B.append('### ### THE EXACT OPPOSITE OF THE TRUTH.** ### Caught by one branch reading `0 0`,')
    B.append('### a shape the misreading could not explain.')
    B.append('')
    B.append(SUB)
    B.append('### THE ONE LIVE BRANCH, TERMINAL BY TERMINAL.')
    B.append(SUB)
    B.append('### ### **DECLARATIONS READ : `%d`. ### ABSENT FROM `main` : `%d`.**'
             % (C1['decls'], C1['absent']))
    B.append('### ### **THE CITATION TEST IS AGAINST `main`, WHERE A READER RESOLVES IT** -- and')
    B.append('### ### `invariance_barrier` and `DeterminedBy` ### **ALREADY STAND ON `main`** ###')
    B.append('### ### and are citable.')
    for o in S2['decls']:
        if o['on_main']:
            continue
        B.append('###   **`%s`** (`%s`) in `%s`' % (o['name'], o['kind'], o['file']))
        B.append('###       cited by `%d` corpus document(s)%s'
                 % (len(o['cited_by']),
                    (' -- ' + ', '.join(o['cited_by'][:3])) if o['cited_by']
                    else ' ### **-- CITED BY NOTHING**'))
        B.append('###       ### **AXIOM PROFILE : NOT BUILT.**')
    B.append('### ### **PRINTED PROFILES ON THE REF : `%d`.**' % C1['printed_profiles'])
    B.append('### ### The only candidate is a `#print axioms` ### **SOURCE SCRIPT** ### whose own')
    B.append('### ### comment says ### *Expected: ... axiom-free* ### -- ### **EXPECTED, NOT')
    B.append('### ### PRINTED.** ### **NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD**, a')
    B.append('### ### commit message is not a printed profile, and ### **NO BUILD IS RUN.**')
    B.append('### ### **TERMINALS SAYING `RETIRED` ON THE LIVE BRANCH : `%d`** -- the order`s'
             % C1['retired'])
    B.append('### ### retired-exclusion has no members here, and that is stated rather than')
    B.append('### ### silently unused.')
    B.append('### ### ### **`(F1)` IS %s.** ### `derivGrade` is absent from `main` and cited by'
             % C1['f1'])
    B.append('### ### ### nothing, but ### **`COMPILED` REQUIRES A PRINTED PROFILE AND THE REF')
    B.append('### ### ### CARRIES NONE**, and it is a `def` rather than a theorem. ### One build')
    B.append('### ### ### would settle it and ### **`(R22)` FORBIDS IT.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE DISCLOSURE RULE, APPLIED WHERE IT IS TRUE.')
    B.append(SUB)
    B.append('### **THE RULE, QUOTED:** ### `REGISTRY.md:%d` and `THE_KEYSTONE_CENSUS.md:%d` --'
             % (S3['rule_registry_line'], S3['rule_census_line']))
    B.append('### a terminal not on a default branch ### *belongs in the status column where a')
    B.append('### table-reader meets it*, and it is ### **A DISCLOSURE REQUIREMENT, NOT A REPAIR.**')
    B.append('### ### **AND THE RULE`S OWN WORKED INSTANCE IS STALE:** ### it names')
    B.append('### ### `word-pairing-interface` as ### *the held, unmerged branch*, ### and that')
    B.append('### ### branch is ### **MERGED.** ### **WRITING THE DEMANDED DISCLOSURE THERE WOULD')
    B.append('### ### PUT A FALSE STATEMENT IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE.**')
    B.append('### ### **THE RULE IS NOT STRUCK AND NOT AMENDED HERE. ### ITS INSTANCE IS ROUTED.**')
    B.append('### ### **ROWS SWEPT `%d` ; REPAIRED `%d` ; SWEPT-NOT-REPAIRED `%d` ; ROUTED `%d`.**'
             % (C2['swept'], C2['repaired'], C2['already'], C2['routed']))
    B.append('### ### **REPORTED APART AND NEVER ADDED.**')
    for w in C2['written']:
        B.append('###   `%s` : `%d` row(s) ; `+%d / -%d` ; ### **CONTENT LOST `%d`**'
                 % (w['doc'], w['rows'], w['added'], w['deleted'], w['lost']))
    B.append('### ### **DOCUMENTS EDITED `%d` ; ROWS EDITED `%d` ; CONTENT LOST `%d`.**'
             % (C2['docs'], C2['rows'], C2['lost']))
    B.append('### ### Every pre-edit line is preserved verbatim in an appended annotation, and')
    B.append('### ### `numstat`s in-place deletions are ### **PRINTED AND NOT SUPPRESSED**')
    B.append('### ### (`b390`, `b395`).')
    B.append('### ### **`(F2)` IS MET -- `%d` OF `%d` -- BUT NOT FOR THE REASON THE ORDER GAVE.**'
             % (C2['repaired'], C2['swept']))
    B.append('### ### The order expected rows to disclose already in a preamble; the measurement')
    B.append('### ### says ### **MOST SWEPT ROWS` TERMINALS HAVE SINCE LANDED**, so no disclosure')
    B.append('### ### is owed. ### **A PREDICTION MET FOR THE WRONG REASON IS REPORTED WITH THE')
    B.append('### ### REASON.**')
    B.append('### **AND ONE THING SEEN AND NOT TOUCHED:** ### the repaired rows assert axiom')
    B.append('### profiles for terminals whose ref carries ### **NO PRINTED PROFILE.** ###')
    B.append('### **MOVING A GRADE IS NOT THIS ACT`S SCOPE AND NO GRADE WAS MOVED. ### ROUTED.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE QUEUE, WITH TRIGGERS.')
    B.append(SUB)
    for it, tg in TRIGGERS:
        B.append('###   **%s**' % it)
        B.append('###       TRIGGER: %s' % tg)
    B.append('### ### **`%d` ITEMS, EACH NAMING ITS TRIGGER, AND ### NOTHING IS OPENED.**'
             % Q['triggers'])
    B.append('### ### **A TRIGGER IS NOT A PLAN AND A QUEUE IS NOT A COMMITMENT.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE RESEARCH BOARD. ### **QUOTATION, NOT COMPOSITION.**')
    B.append(SUB)
    B.append('### **THE CLAUSE ANCHOR** ### -- `FINDINGS.md`, `%d` line(s) read.'
             % C4['clause_lines'])
    B.append('### **THE FACES LEDGER** ### -- `%d` rows in `%d` bytes.'
             % (C4['faces_rows'], C4['faces_bytes']))
    B.append('### ### **NEW CLAIMS MADE BY THE BOARD : `%d`.**' % C4['new_claims'])
    B.append('### ### **AND WHAT THE RECORD DOES NOT SAY IS SAID PLAINLY:** ### the clause has')
    B.append('### ### not moved since `b332` stated it; no coordinate is closed; the partition')
    B.append('### ### stays UNDECIDED; and ### **NO ACT IN THIS ARC PRODUCED A RESULT ABOUT THE')
    B.append('### ### OBJECT.** ### **THAT IS A QUOTATION OF AN ABSENCE RATHER THAN A CLAIM')
    B.append('### ### ABOUT ONE.**')
    B.append('')
    B.append(SUB)
    B.append('### THE READ-ONLY BAR, MEASURED BEFORE AND AFTER THE COMPONENTS.')
    B.append(SUB)
    for k in sorted(AC['refs_after']):
        B.append('###   %-24s `%s` = `%s`   unchanged : %s'
                 % (k, AC['refs_after'][k]['branch'], AC['refs_after'][k]['head'],
                    AC['refs_before'][k] == AC['refs_after'][k]))
    B.append('### ### **EVERY REPOSITORY`S BRANCH AND HEAD BYTE-IDENTICAL : %s.**' % AC['readonly'])
    B.append('### ### **`0` MERGES, `0` PUSHES TO ANY BRANCH, `0` CHECKOUTS, `0` CLONES, `0`')
    B.append('### ### BUILDS, `0` `.lean` FILES TOUCHED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK.')
    B.append(SUB)
    B.append('### ### **ITEMS SWEPT `%d` ; CLOSED `%d` ; STANDING `%d`.**'
             % (Q['items'], Q['closed'], Q['standing']))
    B.append('### ### **TWO ITEMS ARE CLOSED BY BEING QUEUED**, which is what `(R22)` asks for --')
    B.append('### ### and ### **A QUEUED ITEM IS NOT A DISCHARGED ITEM.**')
    B.append('### ### **FOUR ITEMS OPEN**, the first of which is this act`s largest finding: ###')
    B.append('### ### **THE KEYSTONES` STALE `HELD` PROSE.**')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME, NOW WITH TRIGGERS')
    B.append('### ### ATTACHED, AND THIS ACT CLOSES NONE OF THEM.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS BANK WAS MADE FROM. ### **NAMED, SO A READER CAN RE-RUN IT.**')
    B.append(SUB)
    B.append('### ### **THE FACE, LOCKED BEFORE ANY WRITE:**')
    B.append('###   `data/b397_registration_2026-09-10.txt`')
    B.append('###   sha256 `%s`' % SEALHASH)
    B.append('###   locked at `%s` (UTC)' % SEALSTAMP)
    B.append('### ### **THE LOCK GATE:** ### `tools/b378_lockgate.py` run as `b397` -- ###')
    B.append('### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### **THE RUN RECORDS, EACH RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`):')
    B.append('###   the extract and its four surveys   `data/%s`  `%s`'
             % (E['run_file'], E['run_clock']))
    B.append('###   the components and the sweep       `data/%s`  `%s`'
             % (AC['run_file'], AC['run_clock']))
    B.append('### ### **AND THE LEDGER WRITES:** ### `CORRESPONDENCE.md` row `%d`; the'
             % rownum)
    B.append('### ### `OPEN_TRAILS.md` block marked `%s`; the index key' % MARK)
    B.append('### ### `the-unlanded-work`.')
    B.append('')
    B.append(SCOPE)
    B.append('')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A DIRECTION WAS ASSUMED.', '### A BRANCH WAS MERGED.',
                '### A BRANCH WAS CHECKED OUT.', '### A BUILD WAS RUN.',
                '### AN UNKNOWN WAS REPORTED AS COMPILED.',
                '### A FALSE DISCLOSURE WAS WRITTEN.', '### AN ITEM WAS OPENED.',
                '### THE PLATFORM WAS CALLED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b397_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b397_the_unlanded_work.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b397_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
