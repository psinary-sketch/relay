# -*- coding: utf-8 -*-
"""b389_desk_bank.py -- COMPONENT 4 (`(R18)`, HEAD NOTES ONLY), THE DESK, THE WRITES, THE BANK.

### ### **`(R18)` ADDS A HEAD NOTE TO EACH MAP AND NOTHING ELSE**, and this file is written so it
### cannot do more: it inserts one block into each map`s head, ### **AFTER THE PURPOSE LINE AND
### ### BEFORE ANYTHING ELSE**, and an arm diffs each file against ### **THE PRE-ACT BLOB** ### to
### prove no line outside the head block moved.
### ### **AND NO PRIOR HEAD IS REPLACED.** ### Both maps already carry LAYERED declarations -- a
### standing one and a superseded one, kept side by side -- and ### **THAT PRECEDENT IS THE MAP`S
### ### OWN**, so this note is added beneath them rather than over them.
### ### **THE REFRESH IS IDEMPOTENT BY A MARK.** ### **AN ACT THAT CANNOT BE RE-RUN CANNOT BE
### ### CHECKED** (`b386`).
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
CLUSTERMAP = os.path.join(PP, 'SPIRAL_MAP.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
MARK = '<!-- b389 the look-see, the deposited layer, and the unreached repository; (R18) -->'
PRIOR = '<!-- b388 the map refreshed; (R17) executed; the unreadable rows named -->'
NOTE_MARK = '<!-- b389 (R18) HEAD NOTE -- TWO MAPS, TWO KEYS, 2026-09-09 -->'
ACT = 'b389'
TODAY = '2026-09-09'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b389_components')
LG = J('b389_lockgate')
E = J('b389_reads')
C1, C2, C3 = AC['c1'], AC['c2'], AC['c3']
BANKOUT = os.path.join(D, 'b389_the_look_see.txt')


def blob(repo, path):
    """### **THE PRE-ACT BYTES, FROM THE COMMITTED BLOB AND NOT FROM THIS RUN`S MEMORY.**

    ### `b388`'s `G-PRESERVED` read `False` on an idempotent re-run because it compared the file
    ### against itself WITHIN the run. ### **AN ARM MUST MEASURE THE SAME THING ON EVERY RUN**
    ### (`b352`), and the only fixed point available is the blob at `HEAD`.
    """
    r = subprocess.run(['git', 'show', 'HEAD:' + path], cwd=repo, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


# ==================================================================================================
#  COMPONENT 4 -- (R18) APPLIED. ### HEAD NOTES ONLY.
# ==================================================================================================
CLUSTER_NOTE = [
    '',
    NOTE_MARK,
    '',
    ('**THIS IS THE CLUSTER MAP — RULING `(R18)`, THE AUTHOR’S, 2026-09-09 (b389): TWO MAPS, TWO '
     'KEYS.** *This map **keys on subjects and domains**. The other map — `phase1.5/method/'
     'THE_LOAD_BEARING_MAP.md`, the keystone correspondence union — is the **constellation map**, '
     'and it **keys on interrelated verified statements**: terminals, premises, correspondence '
     'rows and the kernels that carry them. **Neither is merged into the other.*** '
     '### **AND THE TWO DRIFT FOR DIFFERENT REASONS, WHICH IS THE REASON THE RULING GIVES:** '
     '*subjects **emerge** from research and are **RECORDED**, so a cluster map drifts when '
     'nobody records; verifications are **dug for** and are **BUILT**, so a constellation map '
     'drifts when nobody builds.* '
     '### **This note adds nothing else to this document, and replaces no declaration above it.**'),
]

CONST_NOTE = [
    '',
    NOTE_MARK,
    '',
    ('**THIS IS THE CONSTELLATION MAP — RULING `(R18)`, THE AUTHOR’S, 2026-09-09 (b389): TWO '
     'MAPS, TWO KEYS.** *This map **keys on interrelated verified statements** — terminals, '
     'premises, correspondence rows and the kernels that carry them. The other map — '
     '`SPIRAL_MAP.md`, the federation architecture — is the **cluster map**, and it **keys on '
     'subjects and domains**. **Neither is merged into the other.*** '
     '### **AND THE TWO DRIFT FOR DIFFERENT REASONS, WHICH IS THE REASON THE RULING GIVES:** '
     '*subjects **emerge** from research and are **RECORDED**, so a cluster map drifts when '
     'nobody records; verifications are **dug for** and are **BUILT**, so a constellation map '
     'drifts when nobody builds.* '
     '### **This note adds nothing else to this document, and replaces no declaration above it.**'),
]


def head_note(path, repo_rel, note, label):
    """### **ONE HEAD NOTE, INSERTED AFTER THE PURPOSE LINE. ### NOTHING ELSE TOUCHED.**"""
    rec('  ### **%s** -- `%s`' % (label, repo_rel))
    before_txt = io.open(path, encoding='utf-8', newline='').read()
    pre = blob(PP, repo_rel)
    heads_before = [ln for ln in pre.splitlines()[:40] if ln.startswith('**DOCUMENT CLASS')]
    rec('      prior head declarations in the committed blob : %d' % len(heads_before))
    for h in heads_before:
        rec('        > %s' % ' '.join(h.split())[:120])
    if NOTE_MARK in before_txt:
        rec('      ### ALREADY FILED -- the mark is present. ### NOTHING WRITTEN.')
        after_txt = before_txt
        already = True
    else:
        already = False
        lines = before_txt.replace(chr(13) + chr(10), chr(10)).split(chr(10))
        at = None
        for i, ln in enumerate(lines[:40]):
            if ln.startswith('**PURPOSE:**'):
                at = i + 1
        if at is None:
            rec('      ### HARD FAILURE -- no PURPOSE line in the head block. ### NOTHING WRITTEN.')
            return dict(ok=False, halt=True)
        new = lines[:at] + note + lines[at:]
        open(path + '.tmp', 'wb').write((chr(10).join(new)).encode('utf-8'))
        os.replace(path + '.tmp', path)
        after_txt = io.open(path, encoding='utf-8', newline='').read()
        rec('      inserted after the PURPOSE line at index %d ; bytes %d -> %d'
            % (at, len(before_txt.encode('utf-8')), len(after_txt.encode('utf-8'))))
    # ---- THE ARM: every prior head still present, and nothing outside the head block moved -------
    after_n = after_txt.replace(chr(13) + chr(10), chr(10))
    heads_kept = [h for h in heads_before if h in after_n]
    rec('      ### ### **PRIOR HEAD DECLARATIONS RE-READ OUT OF THE FILE AFTER THE WRITE : %d OF '
        '%d.**' % (len(heads_kept), len(heads_before)))
    # ### the body below the head block must be byte-identical to the pre-act blob.
    def body(t):
        ls = t.split(chr(10))
        k = 0
        for i, ln in enumerate(ls[:60]):
            if ln.startswith('**PURPOSE:**'):
                k = i + 1
        return chr(10).join(ls[k:])
    b_pre, b_post = body(pre), body(after_n)
    tail_intact = b_post.endswith(b_pre) or (b_pre in b_post)
    rec('      ### ### **EVERY LINE BELOW THE HEAD BLOCK UNCHANGED AGAINST THE PRE-ACT BLOB : %s.**'
        % tail_intact)
    # ### and the diff itself, counted -- ### **A CLAIM OF `NOTHING ELSE` IS MEASURED, NOT ASSERTED.**
    r = subprocess.run(['git', '-C', PP, 'diff', '--numstat', '--', repo_rel],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    add = dele = 0
    for ln in (r.stdout or '').splitlines():
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            add, dele = int(p[0]), int(p[1])
    rec('      ### ### **THE DIFF : `+%d` / `-%d`. ### DELETIONS MUST BE `0`.**' % (add, dele))
    subprocess.run(['git', '-C', PP, 'add', '--', repo_rel], capture_output=True)
    # ### **`before` IS THE PRE-ACT BLOB, NOT THIS RUN`S `before`.** ### On an idempotent
    # ### re-run the file is already written, so a within-run `before` equals `after` and the
    # ### bank would print `54486 -> 54486` -- a true statement about the re-run and a false
    # ### one about the act. ### **AN ARM MUST MEASURE THE SAME THING ON EVERY RUN** (`b352`,
    # ### `b388`), and the only fixed point is the committed blob.
    return dict(ok=(len(heads_kept) == len(heads_before) and tail_intact and dele == 0),
                already=already, heads=len(heads_before), kept=len(heads_kept),
                tail_intact=tail_intact, added=add, deleted=dele,
                before=len(pre.encode('utf-8')), after=len(after_txt.encode('utf-8')))


def component4():
    rec('=' * 100)
    rec('  ### COMPONENT 4 -- `(R18)` APPLIED. ### **HEAD NOTES ONLY.**')
    rec('=' * 100)
    rec('  ### **THE RULING, IN ITS OWN WORDS:** ### *A CLUSTER map keys on subjects and domains.')
    rec('  ### A CONSTELLATION map keys on interrelated verified statements -- terminals,')
    rec('  ### premises, correspondence rows and the kernels that carry them. The federation map')
    rec('  ### is the cluster map; the keystone correspondence union is the constellation map.')
    rec('  ### Each states in its own head which it is and what the other holds.*')
    rec('  ### ### **AND THE REASON IS RECORDED WITH IT**, because the ruling gives one: subjects')
    rec('  ### ### EMERGE and are RECORDED, so a cluster map drifts when nobody records;')
    rec('  ### ### verifications are DUG FOR and are BUILT, so a constellation map drifts when')
    rec('  ### ### nobody builds.')
    rec('  ### ### ### **`(R18)` ADDS A HEAD NOTE TO EACH AND NOTHING ELSE, AND THIS COMPONENT')
    rec('  ### ### ### DOES EXACTLY THAT.**')
    rec()
    rec('  ### **AND THE PRECEDENT FOR HOW A HEAD NOTE IS ADDED IS THE MAPS` OWN.** ### Both')
    rec('  ### already carry ### **LAYERED** ### declarations -- a standing one and a superseded')
    rec('  ### one, kept side by side, with the retirement stated rather than the retired line')
    rec('  ### deleted. ### **SO THIS NOTE IS ADDED BENEATH THEM AND REPLACES NOTHING**, and an')
    rec('  ### arm re-reads every prior declaration out of the file after the write.')
    rec()
    a = head_note(CLUSTERMAP, 'SPIRAL_MAP.md', CLUSTER_NOTE, 'THE CLUSTER MAP')
    rec()
    b = head_note(CONSTMAP, 'phase1.5/method/THE_LOAD_BEARING_MAP.md', CONST_NOTE,
                  'THE CONSTELLATION MAP')
    rec()
    ok = a.get('ok') and b.get('ok')
    rec('  ### ### **HEAD NOTES WRITTEN : 2. ### PRIOR HEAD DECLARATIONS REMOVED : %d.**'
        % ((a['heads'] - a['kept']) + (b['heads'] - b['kept'])))
    rec('  ### ### **LINES DELETED FROM EITHER MAP : %d.** ### **LINES CHANGED OUTSIDE EITHER'
        % (a['deleted'] + b['deleted']))
    rec('  ### ### HEAD BLOCK : `0`, MEASURED AGAINST THE PRE-ACT BLOB AND NOT ASSERTED.**')
    rec('  ### ### **NEITHER MAP IS MERGED INTO THE OTHER, AND NEITHER NOTE MOVES A ROW, A')
    rec('  ### ### CLUSTER OR A TERMINAL.**')
    rec('  ### ### ### **AND NOTHING ELSE IN EITHER DOCUMENT IS EDITED** -- which is `(R18)`\'s')
    rec('  ### ### ### own boundary, and this act`s locked face repeats it as a bar.')
    return dict(cluster=a, constellation=b, ok=bool(ok), notes=2,
                heads_removed=(a['heads'] - a['kept']) + (b['heads'] - b['kept']),
                deleted=a['deleted'] + b['deleted'])


# ==================================================================================================
DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', "PARKED by the author's ruling"),
    ('the wave candidate list, typed and not ranked at b324', 'STAND', "ranking is the author's"),
    ("the wave itself, the author's own", 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     '### **OPEN -- AND THIS ACT REMOVES THE MEMBER `b388` PUT IN IT.** ### `b388` added '
     '`SIDE-interface-split` on the strength of a sentence it read as a citation. ### The '
     'sentence says Proposition 1 ### *is verified in* ### `SIDE-interfaces` -- which resolves -- '
     'and names `SIDE-interface-split` only as ### *the future ... kernel (LV-L-1b)*. ### '
     '### **THE ADDITION IS WITHDRAWN. ### A LIST LOSING A MEMBER BY WITHDRAWAL IS NOT A '
     'CLOSURE**, and the list STANDS OPEN'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### This act rewrites none'),
    ('the class ruling itself', 'STAND', "STILL THE AUTHOR`S"),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the citation question -- what a finished keystone is cited as', 'STAND',
     '### **AWAITING THE AUTHOR AND NOT MOVED BY THIS ACT.** ### `0` options added, `0` preferred'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND',
     '`NOT-YET-SYNTHESIZED` since b385; `0` opened by this act'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'NAMED at b387 and ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the two emergent clusters, seated at b388', 'STAND', 'SEATED under `(R17)`; not reshaped'),
    ('the map`s five clusters that changed shape', 'STAND',
     '### **THE RESHAPING IS THE AUTHOR`S** ### and this act reshapes none'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**; `0` assigned by this act'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the two maps now say which they are, under `(R18)`', 'STAND',
     'NEW at b389: ### **A HEAD NOTE ON EACH MAP AND NOTHING ELSE**, naming its own key, the '
     'other map`s, and the drift each is prone to. ### **NEITHER MAP IS MERGED INTO THE OTHER, '
     'NO PRIOR HEAD IS REPLACED, AND `0` LINES CHANGED OUTSIDE EITHER HEAD BLOCK.** ### The item '
     'STANDS because a head note declares a key; ### **IT DOES NOT KEEP EITHER MAP CURRENT**'),
    ('the eight cluster syntheses against the registry`s six and the map`s %d', 'STAND',
     'NEW at b389: ### **THREE POPULATIONS THAT DO NOT NEST** -- `%d` on disk, `%d` named in the '
     'registry`s support tier, `%d` whose subject the refreshed table carries -- and ### **THE '
     'MEMBERSHIPS DIFFER AND NOT ONLY THE COUNTS.** ### `PHILOSOPHY_COGNITION` is in the map and '
     'not the registry; `IDENTITY_FORMATION_BIJECTION` is in the registry and not the map. ### '
     '**ROUTED, NOT ACTED ON: SEATING OR RECORDING A SYNTHESIS IS THE AUTHOR`S**'),
    ('the deposited layer, which could not be read', 'STAND',
     'NEW at b389: ### **`0` OF `6` ZENODO ROUTES ANSWERED, WITH A POSITIVE CONTROL AT `200`** -- '
     'so the network is not the cause -- and a sweep of all `%d` DOIs the corpus names enumerated '
     '### **`0` RECORDS.** ### **`(F2)` IS UNTESTED: NEITHER MET NOR REFUTED**, and ### **NO '
     'FIGURE WAS SUBSTITUTED FROM THE CORPUS** for a reading the order sent this act to the '
     'platform to take. ### The item STANDS and is re-openable the moment the platform answers'),
    ('no written rule for what deposits', 'STAND',
     'NEW at b389: ### **`(F3)` MET -- NO WRITTEN DEPOSIT RULE IS LOCATED**, by a search proved '
     'in both halves: `8` names return `0` files, and the content search returns the '
     '### *internal-until-fruit law* ### (which governs ADMISSION) and the ### *sequencing law* '
     '### (which orders PROVISIONING against PARTNERING). ### **NEITHER IS A DEPOSIT RULE, AND '
     'BOTH ARE QUOTED SO THE READING CAN BE OVERTURNED.** ### **A REQUEST FOR ONE IS ROUTED TO '
     'THE AUTHOR; THIS SEAT DID NOT WRITE IT**'),
    ('`SIDE-interface-split` -- and `b388``s finding about it, WITHDRAWN', 'STAND',
     'NEW at b389: ### **THE REPOSITORY IS `UNDECIDABLE-WITHOUT-CREDENTIALS`** -- an '
     'unauthenticated read cannot tell absent from private -- ### **BUT THE CITING DOCUMENT IS '
     'CORRECT AS WRITTEN AND NEEDS NOTHING**, because Proposition 1 is verified in '
     '`SIDE-interfaces`, which resolves. ### **`b388` REPORTED A FALSE DEFECT** ### by harvesting '
     'every `SIDE-*` backtick out of a member document and reading a future-tense mention as a '
     'citation. ### **THE FINDING IS WITHDRAWN AND NO DOCUMENT IS EDITED**'),
    ('the map row `b388` wrote from the same misreading', 'STAND',
     'NEW at b389: `SPIRAL_MAP.md` line `270` seats `SIDE-interface-split` in the cross-domain '
     'cluster`s federation column. ### **IT IS WRONG FOR THE SAME REASON AND THIS ACT DOES NOT '
     'TOUCH IT** -- `(R18)` adds a head note and nothing else, and ### **THE FACE IS NOT WIDENED '
     'MID-ACT TO REPAIR WHAT THIS ACT DISCOVERED.** ### **ROUTED TO THE AUTHOR WITH THE '
     'EVIDENCE**'),
    ('this act`s own face carried a wrong figure', 'STAND',
     'NEW at b389: the locked face says the map`s table carries ### **THREE** ### of the '
     'syntheses` subjects. ### It carries ### **`%d`.** ### The `3` came from the extract`s '
     'predicate, which demanded the whole filename stem as one contiguous string while the map '
     'writes `Cubit / Trivium`. ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE** -- the '
     'same species this act withdraws `b388``s finding for, committed by this act`s own '
     'instrument. ### **THE FACE IS LOCKED AND NOT EDITED; THE CORRECTION IS REPORTED IN THE '
     'COMPONENT AND IN THIS BANK, BESIDE BOTH FIGURES**'),
]


def desk_rows():
    out = []
    for item, disp, why in DESK:
        it, w = item, why
        if '%d' in it and 'cluster syntheses against' in it:
            it = item % C1['map']
            w = why % (C1['disk'], C1['reg'], C1['map'])
        elif 'DOIs the corpus names' in why:
            w = why % C2['dois']
        elif 'It carries ### **`%d`.**' in why:
            w = why % C1['map']
        out.append((it, disp, w))
    return out


def do_desk():
    rec('    ### ### **THIS ACT CLOSES NOTHING.** ### `(R7)` closes an item whose OCCASION is')
    rec('    ### gone. ### A head note declaring a key does not make either map current; a')
    rec('    ### platform that did not answer leaves its question exactly where it was; and')
    rec('    ### ### **WITHDRAWING A FINDING RE-OPENS NOTHING AND CLOSES NOTHING** -- it removes')
    rec('    ### a member from an open list, which is not a closure.')
    rec('')
    marks = []
    for item, want, why in desk_rows():
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 900), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **SIX ITEMS ARE ADDED AND ALL SIX STAND** -- and ### **ONE OF THEM IS THIS')
    rec('    ### ### SEAT`S OWN FACE, CARRYING A FIGURE THIS ACT CORRECTS IN THE OPEN.**')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


# ==================================================================================================
SCOPE = (
    "**SCOPE: THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED REPOSITORY; (R18) APPLIED AS "
    "HEAD NOTES ONLY.** NO class ruled, NO document reclassified, NO class line written, NO "
    "declaration moved, NO REGISTRY ROW EDITED, NO grade moved, NO Correspondence row edited, NO "
    "list closed, and NO CLUSTER ADDED, SPLIT, MERGED OR RENAMED IN EITHER MAP. **EACH MAP "
    "RECEIVED EXACTLY ONE HEAD NOTE AND NOTHING ELSE; NO PRIOR HEAD DECLARATION WAS REPLACED, "
    "AND 0 LINES CHANGED OUTSIDE EITHER HEAD BLOCK, MEASURED AGAINST THE PRE-ACT BLOB AND NOT "
    "ASSERTED.** **NEITHER MAP IS MERGED INTO THE OTHER.** **NOTHING WAS WRITTEN AT ZENODO IN ANY "
    "BRANCH** -- every platform call was a GET with no credential, no method override and no "
    "body, and this act carried NO WRITE PATH TO THE PLATFORM AT ALL. **THE DEPOSITED LAYER COULD "
    "NOT BE ENUMERATED: 0 OF 6 ROUTES ANSWERED WITH A POSITIVE CONTROL AT 200, AND (F2) IS "
    "UNTESTED -- NEITHER MET NOR REFUTED.** **NO FIGURE IN THAT HALF WAS SOURCED FROM THE CORPUS "
    "INSTEAD**, because the order said READ LIVE and A RECOLLECTION DRESSED AS A LIVE READ WOULD "
    "HAVE ANSWERED THE ONE QUESTION THE ACT WAS SENT TO THE PLATFORM TO ANSWER. **NO WRITTEN "
    "DEPOSIT RULE IS LOCATED**, by a search proved BY NAME AND BY CONTENT, with the two nearest "
    "standing laws QUOTED AND NAMED AS NOT IT; the practice observed is stated AS OBSERVATION AND "
    "NEVER AS RULE, and THIS SEAT DID NOT WRITE THE MISSING RULE. **THE UNREACHED REPOSITORY IS "
    "UNDECIDABLE-WITHOUT-CREDENTIALS AND THE CITING DOCUMENT IS CORRECT AS WRITTEN**; NO DOCUMENT "
    "WAS EDITED. **b388's FINDING ABOUT SIDE-interface-split IS WITHDRAWN AS A COMPONENT RESULT "
    "AND NOT A FOOTNOTE**, and the map row b388 wrote from the same misreading is ROUTED, NOT "
    "REPAIRED, because THE FACE WAS NOT WIDENED MID-ACT. **AND THIS ACT'S OWN LOCKED FACE CARRIED "
    "A WRONG FIGURE -- THE MAP CARRIES 7 OF THE SYNTHESES' SUBJECTS, NOT 3 -- WHICH IS CORRECTED "
    "IN THE OPEN WITH BOTH FIGURES PRINTED AND THE DEFECTIVE PREDICATE NAMED; THE LOCKED FACE IS "
    "NOT EDITED.** **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME**, and LIST 1 LOSES A MEMBER "
    "BY WITHDRAWAL, WHICH IS NOT A CLOSURE. **NO NEW TRACKING DOCUMENT WAS CREATED IN THE "
    "CORPUS.** NO ARCHIVE FILE TOUCHED, NO b375 CLUSTER OPENED, THE MIRROR ROSTER NOT EDITED, NO "
    ".git/hooks/pre-push DELETED. NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE "
    "RECOMPUTED. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS "
    "COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; NO "
    "CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION "
    "STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's "
    "cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent "
    "seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE "
    "STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and "
    "this act makes no claim about it in either direction. NOTHING IS DEPOSITED.")


def trail_block(Q, C4):
    return [
        '', MARK, '',
        '### **b389 — THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED REPOSITORY '
        '(2026-09-09)**',
        '',
        ('*No block above is edited. The b388 block (`%s`) and every block before it stand exactly '
         'as they were written — including the one this act withdraws a finding from, which is '
         'preserved and answered rather than repaired.*' % PRIOR),
        '',
        ('**RULING `(R18)`, THE AUTHOR’S: TWO MAPS, TWO KEYS.** A **cluster** map keys on '
         'subjects and domains; a **constellation** map keys on interrelated verified statements '
         '— terminals, premises, correspondence rows and the kernels that carry them. '
         '`SPIRAL_MAP.md` is the cluster map; `THE_LOAD_BEARING_MAP.md` is the constellation map. '
         '**Each now states in its own head which it is and what the other holds**, with the '
         'ruling’s reason recorded: subjects **emerge** and are **recorded**, so a cluster map '
         'drifts when nobody records; verifications are **dug for** and are **built**, so a '
         'constellation map drifts when nobody builds. **Neither map is merged into the other, '
         'and the ruling adds a head note to each and nothing else** — `%d` prior head '
         'declarations were re-read out of the two files after the write and `%d` were removed; '
         '`%d` lines were deleted from either map.'
         % (C4['cluster']['heads'] + C4['constellation']['heads'], C4['heads_removed'],
            C4['deleted'])),
        '',
        ('**THE CLUSTER SYNTHESES: THREE POPULATIONS THAT DO NOT NEST.** `%d` on disk, `%d` named '
         'in `REGISTRY.md`’s support tier, `%d` whose subject the refreshed cluster table '
         'carries. **The three figures are never added and no average is taken**, because a '
         'difference of counts is not a difference of members: `PHILOSOPHY_COGNITION` is carried '
         'by the map and not named by the registry, and `IDENTITY_FORMATION_BIJECTION` is named '
         'by the registry and not carried by the map. `(F1)` is **met** — and the corpus says it '
         'in its own voice: the theory-space synthesis calls itself *the smallest and least '
         'mature **of the eight***, one day after the map’s cluster section dated itself '
         '`2026-06-04` and named *the six cluster syntheses* as its sources. **Nothing is added '
         'to either map: seating or recording a synthesis is the author’s.**'
         % (C1['disk'], C1['reg'], C1['map'])),
        '',
        ('**THE DEPOSITED LAYER COULD NOT BE READ, AND THE ABSENCE IS PROVED.** `0` of `6` '
         'Zenodo routes answered — the record API, the record page, the DOI resolver, the search '
         'API and both OAI-PMH verbs — while **a positive control on a live host returned `200`, '
         'so the network is not the cause**. A sweep of all `%d` DOIs the corpus names outside '
         '`archive/` enumerated **`0` records**. One route briefly looked like it was working: '
         '`/api/records?q=recid:<id>` returned `200` with `total: 0`. **A 200 carrying an empty '
         'result is an empty result**, and it is counted as not answering. **So `(F2)` — at least '
         'three deposited software records sitting at versions their repositories have passed — '
         'is `UNTESTED`: neither met nor refuted.** The order said READ LIVE, and **no figure in '
         'that half was substituted from the corpus’s own record of its deposits**; what the '
         'corpus claims about itself is reported separately and labelled as the corpus’s claim.'
         % C2['dois']),
        '',
        ('**AND NO WRITTEN RULE FOR WHAT DEPOSITS IS LOCATED — `(F3)` MET.** The search is printed '
         'in both halves: `8` names a reader might give such a rule return `0` files, and the '
         'search by the **content** such a rule would have returns two standing laws, both quoted '
         'so the reading can be overturned. The **internal-until-fruit law** governs *admission* '
         'to the corpus — when a document may exist at Tier N at all — not what leaves it. The '
         '**sequencing law** (*provisioning precedes any partnering*) orders provisioning against '
         'partnering, not depositing against withholding. **Neither is a deposit rule.** The '
         'practice this act observed is stated **as observation and never as rule**, and **a '
         'request for a written rule is routed to the author** — a seat that supplies the words '
         'has written a new rule under an old name.'),
        '',
        ('**THE UNREACHED REPOSITORY — AND `b388`’S FINDING ABOUT IT, WITHDRAWN.** `b388` filed, '
         'as an addition to `LIST 1`, that `SIDE-interface-split` is named in '
         '`INTERFACE_CONSERVATION.md` line `192` as verifying Proposition 1 and does not resolve. '
         '**That is not what the line says.** It says the structural form of Proposition 1 *is '
         'verified in* `SIDE-interfaces` — which is among the `42` repositories the account lists '
         'and resolves — and names `SIDE-interface-split` only as *the **future** … kernel '
         '(LV-L-1b)*, reserved work. Line `262` of the same document says it again: *candidate '
         'kernel name … **or similar***. And the corpus had already audited this exact name and '
         'ruled on it, in writing, before `b388` ran: *✓ correctly hedged as future work; **not** '
         'claims of existing kernels*. `8` of the name’s `10` corpus citations mark it future, '
         'candidate, proposed or reserved. **The finding is withdrawn.** `b388`’s extractor '
         'harvested every `SIDE-*` backtick out of a member document and treated each as a kernel '
         'the cluster federates: **a predicate that knows one shape finds one shape**, and here '
         'it found a defect that was never there. **The answer was on disk and the instrument '
         'walked past it.**'),
        '',
        ('**THE REPOSITORY ITSELF IS `UNDECIDABLE-WITHOUT-CREDENTIALS`, AND IT DOES NOT MATTER.** '
         '`ls-remote` returns *Repository not found* to an unauthenticated reader for **both** an '
         'absent repository and a private one — **an unauthenticated read cannot tell absent from '
         'private** — so this act does not choose between them. **All three branches leave the '
         'citing document correct as written**, because the Proposition never rested on that '
         'kernel. **No document is edited.** `SPIRAL_MAP.md` line `270`, where `b388` seated the '
         'same name in the cross-domain cluster’s federation column, is **wrong for the same '
         'reason and is not touched**: `(R18)` adds a head note and nothing else, and **the face '
         'is not widened mid-act to repair what the act discovered**. Routed to the author with '
         'the evidence.'),
        '',
        ('**AND THIS ACT’S OWN LOCKED FACE CARRIED A WRONG FIGURE.** Section (A) reading (1) says '
         'the map’s table carries **three** of the syntheses’ subjects. It carries **`%d`**. The '
         '`3` came from this act’s own extract, whose predicate demanded a synthesis’s whole '
         'filename stem as one contiguous string while the map writes `Cubit / Trivium` and '
         '`Matter / cosmology`. **It is the same species this act withdraws `b388`’s finding '
         'for**, committed by this act’s own instrument and carried onto a face that was locked '
         'before it was caught. **The locked face is not edited.** Both figures are printed in '
         'the component and in the bank, with the defective predicate named, so the judgement can '
         'be overturned — because **a seat that corrects an error by quietly reporting a '
         'different number has hidden the error inside the correction**, and a locked face is '
         'exactly where that hiding would be easiest.' % C1['map']),
        '',
        ('**WHAT IS ROUTED TO THE AUTHOR.** (1) A **written deposit rule**, which the corpus does '
         'not have. (2) The **eight-versus-six** disagreement between disk, registry and map — '
         'recording or seating a synthesis is the author’s. (3) `SPIRAL_MAP.md` line `270`’s '
         'federation entry for a kernel that does not exist. (4) The **deposited layer**, which '
         'stays unread until the platform answers. **Nothing here is closed and no list is '
         'closed** — `LIST 1` loses a member by withdrawal, which is not a closure.'),
        '',
    ]


def corr_rows(Q, C4):
    m = ("**THE DEPOSITED LAYER COULD NOT BE READ AND SAYS SO, NO WRITTEN DEPOSIT RULE EXISTS, "
         "AND b388's OWN FINDING ABOUT SIDE-interface-split IS WITHDRAWN AS WRONG** (b389, the "
         "look-see, the deposited layer, and the unreached repository)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b389, %d gates read and %d "
            "checked by digest. THE CLUSTER SYNTHESES STAND IN THREE POPULATIONS THAT DO NOT "
            "NEST: %d ON DISK, %d NAMED IN THE REGISTRY'S SUPPORT TIER, %d WHOSE SUBJECT THE "
            "REFRESHED MAP TABLE CARRIES -- never added and never averaged, because A DIFFERENCE "
            "OF COUNTS IS NOT A DIFFERENCE OF MEMBERS, and the memberships differ in both "
            "directions. (F1) IS MET AND THE CORPUS SAYS IT IN ITS OWN VOICE (*the smallest and "
            "least mature of the eight*). THE DEPOSITED LAYER COULD NOT BE ENUMERATED: 0 OF 6 "
            "ZENODO ROUTES ANSWERED WITH A POSITIVE CONTROL AT 200, so THE NETWORK IS NOT THE "
            "CAUSE, and a sweep of all %d DOIs THE CORPUS NAMES ENUMERATED 0 RECORDS; the "
            "q=recid: route returned 200 WITH total: 0 and A 200 CARRYING AN EMPTY RESULT IS AN "
            "EMPTY RESULT. SO (F2) IS UNTESTED -- NEITHER MET NOR REFUTED -- AND NO FIGURE IN "
            "THAT HALF WAS SOURCED FROM THE CORPUS INSTEAD. (F3) IS MET: NO WRITTEN DEPOSIT RULE "
            "IS LOCATED, by a search proved BY NAME (8 terms, 0 files) AND BY CONTENT, with the "
            "internal-until-fruit law (ADMISSION) and the sequencing law (PROVISIONING BEFORE "
            "PARTNERING) QUOTED AND NAMED AS NOT IT; the practice observed is stated AS "
            "OBSERVATION AND NOT AS RULE and A REQUEST FOR A WRITTEN RULE IS ROUTED. "
            "SIDE-interface-split IS UNDECIDABLE-WITHOUT-CREDENTIALS -- AN UNAUTHENTICATED READ "
            "CANNOT TELL ABSENT FROM PRIVATE -- BUT THE CITING DOCUMENT IS CORRECT AS WRITTEN, "
            "because INTERFACE_CONSERVATION.md LINE 192 SAYS PROPOSITION 1 IS VERIFIED IN "
            "SIDE-interfaces, WHICH RESOLVES, and names SIDE-interface-split only as THE FUTURE "
            "KERNEL (LV-L-1b); 8 OF ITS 10 CORPUS CITATIONS MARK IT FUTURE, CANDIDATE, PROPOSED "
            "OR RESERVED and the archive had ALREADY AUDITED THE NAME AND RULED IT CORRECTLY "
            "HEDGED. SO b388's ADDITION TO LIST 1 IS WITHDRAWN, and the map row b388 wrote from "
            "the same misreading is ROUTED NOT REPAIRED because THE FACE WAS NOT WIDENED "
            "MID-ACT. (R18) IS APPLIED AS HEAD NOTES ONLY: ONE PER MAP, %d PRIOR HEAD "
            "DECLARATIONS PRESERVED AND %d REMOVED, %d LINES DELETED, AND 0 LINES CHANGED OUTSIDE "
            "EITHER HEAD BLOCK MEASURED AGAINST THE PRE-ACT BLOB. AND THIS ACT'S OWN LOCKED FACE "
            "CARRIED A WRONG FIGURE -- THE MAP CARRIES %d SUBJECTS AND NOT 3 -- CORRECTED IN THE "
            "OPEN WITH BOTH FIGURES PRINTED AND THE DEFECTIVE PREDICATE NAMED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['disk'], C1['reg'], C1['map'],
               C2['dois'],
               C4['cluster']['kept'] + C4['constellation']['kept'], C4['heads_removed'],
               C4['deleted'], C1['map']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### A head note was added to two "
            "maps under the author's ruling and every quoted line was re-read out of its own file "
            "at its own line number. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD RUN "
            "AND NO AXIOM PROFILE RECOMPUTED -- ls-remote SAYS A REF EXISTS OR DOES NOT, AND AN "
            "UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE. ### DECLARING WHICH KEY A MAP "
            "USES IS NOT KEEPING THE MAP CURRENT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, "
            "NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW "
            "EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED IN "
            "EITHER MAP. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH")
    grade = ("### READ LIVE WHERE THE ORDER SAID LIVE, AND HALTED WHERE THE PLATFORM DID NOT "
             "ANSWER. ### 0 FIGURES SUBSTITUTED FROM THE CORPUS FOR A LIVE READING; 0 ABSENCES "
             "CLAIMED WITHOUT A POSITIVE CONTROL; 0 PRACTICES PROMOTED INTO RULES. ### THE "
             "WITHDRAWAL OF b388's FINDING IS A COMPONENT RESULT AND NOT A FOOTNOTE, AND THIS "
             "ACT'S OWN FACE IS CORRECTED IN THE OPEN WITH BOTH FIGURES PRINTED. ### 0 LINES "
             "CHANGED OUTSIDE EITHER MAP'S HEAD BLOCK AND 0 PRIOR HEADS REPLACED")
    status = ("data/b389_the_look_see.txt; data/%s; data/%s; "
              "data/b389_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b389); tools/b389_extract.py; "
              "tools/b389_regspec.py; tools/b389_reg_gate.py; tools/b389_components.py; "
              "tools/b389_desk_bank.py; tools/b389_checks.py; PLACE-papers SPIRAL_MAP.md and "
              "phase1.5/method/THE_LOAD_BEARING_MAP.md (one (R18) head note each, nothing else) "
              "and OPEN_TRAILS.md (an append-only block); CORRESPONDENCE.md row %%d"
              % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('two maps two keys', 'the deposited layer could not be read',
           'is there a written deposit rule', 'the unreached repository',
           'b388 was wrong about the kernel')
MUST_NOT_HIT = ('the deposited layer was enumerated', 'a deposit rule was written',
                'the citing document was wrong', 'a cluster was added to the map')


def do_key(rownum, C4):
    KEY = 'two-maps-two-keys-and-the-layer-unread'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "RULING (R18), THE AUTHOR'S: TWO MAPS, TWO KEYS. A CLUSTER MAP KEYS ON SUBJECTS AND "
        "DOMAINS AND DRIFTS WHEN NOBODY RECORDS; A CONSTELLATION MAP KEYS ON INTERRELATED "
        "VERIFIED STATEMENTS AND DRIFTS WHEN NOBODY BUILDS. SPIRAL_MAP.md AND "
        "THE_LOAD_BEARING_MAP.md EACH RECEIVED ONE HEAD NOTE AND NOTHING ELSE -- %d PRIOR HEAD "
        "DECLARATIONS PRESERVED, %d REMOVED, %d LINES DELETED, 0 LINES CHANGED OUTSIDE EITHER "
        "HEAD BLOCK MEASURED AGAINST THE PRE-ACT BLOB -- AND NEITHER MAP IS MERGED INTO THE "
        "OTHER. THE CLUSTER SYNTHESES STAND IN THREE POPULATIONS THAT DO NOT NEST: %d ON DISK, "
        "%d IN THE REGISTRY'S SUPPORT TIER, %d WHOSE SUBJECT THE MAP'S TABLE CARRIES, NEVER "
        "ADDED AND NEVER AVERAGED. THE DEPOSITED LAYER COULD NOT BE ENUMERATED: 0 OF 6 ZENODO "
        "ROUTES ANSWERED WITH A POSITIVE CONTROL AT 200 AND A SWEEP OF ALL %d DOIS RETURNED 0 "
        "RECORDS, SO (F2) IS UNTESTED -- NEITHER MET NOR REFUTED -- AND NO FIGURE WAS SUBSTITUTED "
        "FROM THE CORPUS. NO WRITTEN DEPOSIT RULE IS LOCATED, BY A SEARCH PROVED BY NAME AND BY "
        "CONTENT, WITH THE INTERNAL-UNTIL-FRUIT LAW AND THE SEQUENCING LAW QUOTED AND NAMED AS "
        "NOT IT. SIDE-interface-split IS UNDECIDABLE-WITHOUT-CREDENTIALS BUT THE CITING DOCUMENT "
        "IS CORRECT AS WRITTEN, BECAUSE PROPOSITION 1 IS VERIFIED IN SIDE-interfaces WHICH "
        "RESOLVES; SO b388's ADDITION TO LIST 1 IS WITHDRAWN AS A FALSE DEFECT PRODUCED BY A "
        "PREDICATE THAT READ A FUTURE-TENSE MENTION AS A CITATION. AND THIS ACT'S OWN LOCKED FACE "
        "CARRIED A WRONG FIGURE, CORRECTED IN THE OPEN WITH BOTH FIGURES PRINTED."
        % (C4['cluster']['kept'] + C4['constellation']['kept'], C4['heads_removed'],
           C4['deleted'], C1['disk'], C1['reg'], C1['map'], C2['dois']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION "
        "MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW EDITED AND NO LIST "
        "CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED IN EITHER MAP AND NO PRIOR "
        "HEAD WAS REPLACED. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH AND THIS ACT CARRIED "
        "NO WRITE PATH TO THE PLATFORM. ### 0 FIGURES SUBSTITUTED FROM THE CORPUS FOR A LIVE "
        "READING. ### 0 ABSENCES CLAIMED WITHOUT A POSITIVE CONTROL. ### THE PRACTICE OBSERVED IS "
        "STATED AS OBSERVATION AND NOT AS RULE. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE "
        "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME AND LIST 1 LOSES A MEMBER BY WITHDRAWAL, WHICH "
        "IS NOT A CLOSURE. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN "
        "FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b389_the_look_see.txt; data/%s; data/%s; "
        "data/b389_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b389 -- %d gates read, %d checked by digest); "
        "tools/b389_extract.py; tools/b389_regspec.py; tools/b389_reg_gate.py; "
        "tools/b389_components.py; tools/b389_desk_bank.py; tools/b389_checks.py; "
        "PLACE-papers SPIRAL_MAP.md, phase1.5/method/THE_LOAD_BEARING_MAP.md and OPEN_TRAILS.md; "
        "CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b389 (the look-see: the cluster syntheses in three populations that do not nest; the "
           "deposited layer read live, unanswered on every route, and halted rather than "
           "substituted; no written deposit rule located by a search proved twice; the unreached "
           "repository undecidable but immaterial, with b388's finding about it withdrawn as "
           "wrong; and (R18) applied as one head note per map and nothing else)")
    row_new = ('    # ### TWO MAPS TWO KEYS, AND THE LAYER UNREAD (b389).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for qq in MUST_NOT_HIT:
        out, _rc = query(qq)
        pre[qq] = no_key(out)
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
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
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-44s reaches the b389 key : %s' % (qq, g))
    for lbl, cond in (('the ruling is named and executed', '(R18)' in out),
                      ('two keys, stated apart',
                       'KEYS ON SUBJECTS AND DOMAINS' in out
                       and 'KEYS ON INTERRELATED' in out),
                      ('neither map merged', 'NEITHER MAP IS MERGED INTO THE OTHER' in out),
                      ('no prior head replaced', 'NO PRIOR HEAD WAS REPLACED' in out),
                      ('nothing outside the head block',
                       '0 LINES CHANGED OUTSIDE EITHER HEAD BLOCK' in out),
                      ('the three populations do not nest',
                       'THREE POPULATIONS THAT DO NOT NEST' in out),
                      ('the layer could not be read',
                       '0 OF 6 ZENODO ROUTES ANSWERED' in out),
                      ('the control answered', 'POSITIVE CONTROL AT 200' in out),
                      ('(F2) is untested and not guessed',
                       'UNTESTED -- NEITHER MET NOR REFUTED' in out),
                      ('nothing substituted from the corpus',
                       'NO FIGURE WAS SUBSTITUTED FROM THE CORPUS' in out),
                      ('no deposit rule, and the search proved twice',
                       'PROVED BY NAME AND BY CONTENT' in out),
                      ('the two laws named as not it', 'NAMED AS NOT IT' in out),
                      ('absent or private, undecided',
                       'UNDECIDABLE-WITHOUT-CREDENTIALS' in out),
                      ('the citing document is correct',
                       'THE CITING DOCUMENT IS CORRECT AS WRITTEN' in out),
                      ('b388 withdrawn, and why', 'WITHDRAWN AS A FALSE DEFECT' in out),
                      ('the seat corrects its own face',
                       "THIS ACT'S OWN LOCKED FACE CARRIED A WRONG FIGURE" in out),
                      ('nothing written at zenodo',
                       'NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('withdrawal is not a closure', 'WHICH IS NOT A CLOSURE' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g = pre[qq] and no_key(o)
        ok = ok and g
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


# ==================================================================================================
def main():
    rec('=' * 100)
    rec('b389 -- COMPONENT 4, THE DESK, THE WRITES, AND THE BANK.')
    rec('=' * 100)
    C4 = component4()
    if not C4['ok']:
        rec('  ### HARD FAILURE IN COMPONENT 4 -- HALTING BEFORE THE LEDGERS.')
        run_clock.write(D, 'b389_desk_notes', LINES)
        return 1

    rec('')
    rec('-' * 100)
    rec('  ### THE DESK UNDER (R7).')
    rec('-' * 100)
    Q = do_desk()

    rec('')
    rec('-' * 100)
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True,
                  before_bytes=len(before.encode('utf-8')),
                  after_bytes=len(before.encode('utf-8')))
    else:
        rec('  ### the b388 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q, C4)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        committed = blob(PP, 'OPEN_TRAILS.md')
        ao = after.startswith(before)
        pi = committed in after.replace(chr(13) + chr(10), chr(10))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before),
                  before_bytes=len(before.encode('utf-8')),
                  after_bytes=len(after.encode('utf-8')))
    seg = after.split(MARK, 1)[-1]
    tr['says_r18'] = '(R18)' in seg
    tr['says_untested'] = '`UNTESTED`' in seg
    tr['says_withdrawn'] = 'withdrawn' in seg.lower()
    tr['says_own_face'] = 'OWN LOCKED FACE' in seg
    tr['says_not_widened'] = 'not widened mid-act' in seg.lower()
    rec('  ### ### **THE BLOCK NAMES `(R18)` : %s ; SAYS `(F2)` IS UNTESTED : %s ; SAYS THE '
        'FINDING IS WITHDRAWN : %s ; CORRECTS THIS ACT`S OWN FACE : %s ; SAYS THE FACE WAS NOT '
        'WIDENED : %s**'
        % (tr['says_r18'], tr['says_untested'], tr['says_withdrawn'], tr['says_own_face'],
           tr['says_not_widened']))

    rec('')
    rec('-' * 100)
    rec('  ### THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    ROWS = corr_rows(Q, C4)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b389_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b389_desk_notes', LINES)
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
            run_clock.write(D, 'b389_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum, C4)

    rec('')
    rec('-' * 100)
    rec('  ### THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b389 -- THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED REPOSITORY. ### THE '
             'BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE AUTHOR RULED `(R18)`: TWO MAPS, TWO KEYS.**')
    B.append('### A ### **CLUSTER** ### map keys on subjects and domains. ### A ###')
    B.append('### **CONSTELLATION** ### map keys on interrelated verified statements -- terminals,')
    B.append('### premises, correspondence rows and the kernels that carry them.')
    B.append('### ### **AND THE RULING GIVES ITS OWN REASON, WHICH IS RECORDED WITH IT:** ###')
    B.append('### subjects ### **EMERGE** ### from research and are ### **RECORDED**, so a cluster')
    B.append('### map drifts when nobody records; verifications are ### **DUG FOR** ### and are')
    B.append('### ### **BUILT**, so a constellation map drifts when nobody builds.')
    B.append('### ### ### **NEITHER MAP IS MERGED INTO THE OTHER, AND THE RULING ADDS A HEAD NOTE')
    B.append('### ### ### TO EACH AND NOTHING ELSE.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 1 -- THE CLUSTER SYNTHESES, IN THREE POPULATIONS.')
    B.append(SUB)
    B.append('### ### **ON DISK : `%d`. ### NAMED IN THE REGISTRY`S SUPPORT TIER : `%d`. ### '
             'SUBJECT' % (C1['disk'], C1['reg']))
    B.append('### ### CARRIED BY THE MAP`S REFRESHED TABLE : `%d`.**' % C1['map'])
    B.append('### ### ### **THE THREE ARE NEVER ADDED AND NO AVERAGE IS TAKEN.**')
    B.append('### ### **AND THEY DO NOT NEST : `%s`.** ### A difference of counts is not a'
             % C1['nests'])
    B.append('### difference of members, so the memberships are printed:')
    B.append('###   `PHILOSOPHY_COGNITION` -- carried by the map, ### **NOT NAMED BY THE')
    B.append('###   ### REGISTRY.**')
    B.append('###   `IDENTITY_FORMATION_BIJECTION` -- named by the registry, ### **NOT CARRIED BY')
    B.append('###   ### THE MAP.**')
    B.append('')
    B.append('### ### **`(F1)` MORE THAN SIX CLUSTER SYNTHESES EXIST : `%s`.**' % C1['f1'])
    B.append('### ### **AND THE CORPUS SAYS IT IN ITS OWN VOICE**, which is stronger than this')
    B.append('### seat counting files: the theory-space synthesis (`2026-06-05`) calls itself')
    B.append('### ### *the smallest and least mature ### **of the eight***, one day after the')
    B.append('### map`s cluster section dated itself `2026-06-04` and named ### *the six cluster')
    B.append('### syntheses* ### as its sources.')
    B.append('### ### ### **NOTHING IS ADDED TO EITHER MAP. ### RECORDING OR SEATING A SYNTHESIS')
    B.append('### ### ### IS THE AUTHOR`S, AND THE FINDING IS ROUTED.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 2 -- THE DEPOSITED LAYER. ### **HALTED, AND THE HALT IS PROVED.**')
    B.append(SUB)
    B.append('### ### **`0` OF `6` ZENODO ROUTES ANSWERED. ### THE POSITIVE CONTROL RETURNED')
    B.append('### ### `200`, SO THE NETWORK IS NOT THE CAUSE.**')
    B.append('### The record API, the record page, the DOI resolver, the search API and both')
    B.append('### OAI-PMH verbs were each probed with its code and byte count recorded, and a')
    B.append('### sweep of all `%d` DOIs the corpus names outside `archive/` enumerated'
             % C2['dois'])
    B.append('### ### **`%d` RECORDS.**' % C2['records'])
    B.append('### ### **ONE ROUTE NEARLY BECAME A WORKING ONE:** ### `/api/records?q=recid:<id>`')
    B.append('### returned ### **`200` WITH `total: 0`.**')
    B.append('### ### ### **A `200` CARRYING AN EMPTY RESULT IS AN EMPTY RESULT**, and `b378`\'s')
    B.append('### ### ### rule about exit codes governs status codes by the same argument.')
    B.append('')
    B.append('### ### ### **SO `(F2)` IS `%s`: NEITHER MET NOR REFUTED.**' % C2['f2'])
    B.append('### The order said ### **READ LIVE**, and ### **NO FIGURE IN THAT HALF WAS SOURCED')
    B.append('### ### FROM THE CORPUS INSTEAD.** ### What the corpus claims about its own deposit')
    B.append('### is reported separately and ### **LABELLED AS THE CORPUS`S CLAIM AND NOT AS A')
    B.append('### ### VERIFIED STATE.**')
    B.append('### ### **A RECOLLECTION DRESSED AS A LIVE READ WOULD HAVE BEEN THE WORST OUTCOME')
    B.append('### ### AVAILABLE HERE**, because it would have answered the one question the order')
    B.append('### ### sent this act to the platform to answer, out of the source the order')
    B.append('### ### routed around.')
    B.append('')
    B.append('### ### **`(F3)` NO WRITTEN DEPOSIT RULE IS LOCATED : `%s`.**' % C2['f3'])
    B.append('### The search is printed ### **IN BOTH HALVES**: `8` names a reader might give such')
    B.append('### a rule return `0` files, and the search ### **BY THE CONTENT A DEPOSIT RULE')
    B.append('### ### WOULD HAVE** ### returns two standing laws -- ### **AND NEITHER IS ONE:**')
    B.append('###   the ### *internal-until-fruit law* ### governs ### **ADMISSION** ### to the')
    B.append('###   corpus -- when a document may exist at Tier N at all -- ### **NOT WHAT LEAVES')
    B.append('###   ### IT.**')
    B.append('###   the ### *sequencing law* ### -- ### *provisioning precedes any partnering* ###')
    B.append('###   -- orders ### **PROVISIONING AGAINST PARTNERING**, not depositing against')
    B.append('###   withholding. ### It says what comes FIRST; it does not say WHAT GOES.')
    B.append('### ### **BOTH ARE QUOTED AT THEIR OWN LINES SO THE READING CAN BE OVERTURNED.**')
    B.append('### ### **THE PRACTICE THIS ACT OBSERVED IS STATED AS OBSERVATION AND NEVER AS')
    B.append('### ### RULE, AND A REQUEST FOR A WRITTEN ONE IS ROUTED TO THE AUTHOR** -- ### **A')
    B.append('### ### SEAT THAT SUPPLIES THE WORDS HAS WRITTEN A NEW RULE UNDER AN OLD NAME.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- THE UNREACHED REPOSITORY, AND `b388`\'S FINDING WITHDRAWN.')
    B.append(SUB)
    B.append('### ### **THE VERDICT ON THE REPOSITORY : `%s`.**' % C3['verdict'])
    B.append('### `ls-remote` returns ### *Repository not found* ### to an unauthenticated reader')
    B.append('### for ### **BOTH** ### an absent repository and a private one, and ### **AN')
    B.append('### ### UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE** -- this seat`s own')
    B.append('### species, minted at `b388` and binding here. ### The act does not choose.')
    B.append('')
    B.append('### ### ### **AND IT DOES NOT MATTER, WHICH IS THE REAL FINDING.**')
    B.append('### `INTERFACE_CONSERVATION.md` line `192` says the structural form of Proposition 1')
    B.append('### ### **IS VERIFIED IN `SIDE-interfaces`** ### -- which is among the `42`')
    B.append('### repositories the account lists, and resolves -- and names `SIDE-interface-split`')
    B.append('### only as ### *the ### **future** ### ... kernel (LV-L-1b)*, reserved work.')
    B.append('### Line `262` says it again: ### *candidate kernel name ... ### **or similar***.')
    B.append('### `8` of the name`s `10` corpus citations mark it future, candidate, proposed or')
    B.append('### reserved.')
    B.append('### ### **ALL THREE BRANCHES -- ABSENT, PRIVATE, UNDECIDABLE -- LEAVE THE CITING')
    B.append('### ### DOCUMENT CORRECT AS WRITTEN**, because ### **THE PROPOSITION NEVER RESTED')
    B.append('### ### ON IT.** ### **NO DOCUMENT IS EDITED.**')
    B.append('')
    B.append('### ### ### **SO `b388`\'S FINDING IS WITHDRAWN.**')
    B.append('### `b388` filed, as an addition to `LIST 1`, that a kernel in the map`s federation')
    B.append('### columns does not resolve -- on the strength of a sentence it read as a citation.')
    B.append('### ### **THAT SENTENCE IS NOT A CITATION.**')
    B.append('### `b388`\'s extractor harvested ### **EVERY `SIDE-*` BACKTICK OUT OF A MEMBER')
    B.append('### ### DOCUMENT** ### and treated each as a kernel the cluster federates; a')
    B.append('### future-tense mention and a citation are the same bytes to that predicate.')
    B.append('### ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, and here it found')
    B.append('### ### ### a defect that was never there.')
    B.append('### ### **AND `b388` DID NOT MISREAD A HARD CASE.** ### The archive`s own audit had')
    B.append('### ### already classified this exact name, in writing, before `b388` ran: ###')
    B.append('### ### *correctly hedged as future work; ### **not** ### claims of existing')
    B.append('### ### kernels.* ### **THE ANSWER WAS ON DISK AND THE INSTRUMENT WALKED PAST IT.**')
    B.append('### ### **THE WITHDRAWAL IS A COMPONENT RESULT AND NOT A FOOTNOTE**, because ###')
    B.append('### ### **A SEAT THAT CORRECTS A PRIOR ACT`S ERROR BY QUIETLY REPORTING A DIFFERENT')
    B.append('### ### ANSWER HAS HIDDEN THE ERROR INSIDE THE CORRECTION.**')
    B.append('')
    B.append('### ### **WHAT IS NOT REPAIRED.** ### `SPIRAL_MAP.md` line `270` seats the same')
    B.append('### name in the cross-domain cluster`s federation column. ### **IT IS WRONG FOR THE')
    B.append('### ### SAME REASON AND THIS ACT DOES NOT TOUCH IT.** ### `(R18)` adds a head note')
    B.append('### and nothing else. ### **THE FACE IS NOT WIDENED MID-ACT TO REPAIR WHAT THIS ACT')
    B.append('### ### DISCOVERED**, however small the fix looks. ### **ROUTED WITH ITS EVIDENCE.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- `(R18)` APPLIED. ### **HEAD NOTES ONLY.**')
    B.append(SUB)
    B.append('### ### **ONE HEAD NOTE PER MAP, INSERTED AFTER THE PURPOSE LINE.**')
    B.append('###   `SPIRAL_MAP.md` -- ### **THE CLUSTER MAP** ### -- bytes `%d` -> `%d`, diff'
             % (C4['cluster']['before'], C4['cluster']['after']))
    B.append('###   `+%d` / `-%d`.' % (C4['cluster']['added'], C4['cluster']['deleted']))
    B.append('###   `THE_LOAD_BEARING_MAP.md` -- ### **THE CONSTELLATION MAP** ### -- bytes `%d`'
             % C4['constellation']['before'])
    B.append('###   -> `%d`, diff `+%d` / `-%d`.'
             % (C4['constellation']['after'], C4['constellation']['added'],
                C4['constellation']['deleted']))
    B.append('### ### **PRIOR HEAD DECLARATIONS RE-READ OUT OF THE FILES AFTER THE WRITE : `%d`.'
             % (C4['cluster']['kept'] + C4['constellation']['kept']))
    B.append('### ### ### REMOVED : `%d`.**' % C4['heads_removed'])
    B.append('### **AND THE PRECEDENT IS THE MAPS` OWN:** ### both already carry ### **LAYERED**')
    B.append('### declarations -- a standing one and a superseded one, side by side, with the')
    B.append('### retirement stated rather than the retired line deleted. ### **SO THE NOTE IS')
    B.append('### ### ADDED BENEATH THEM AND REPLACES NOTHING.**')
    B.append('### ### **LINES CHANGED OUTSIDE EITHER HEAD BLOCK : `0`, MEASURED AGAINST THE')
    B.append('### ### PRE-ACT BLOB AND NOT ASSERTED** -- `b352`/`b388`\'s rule: an arm must')
    B.append('### ### measure the same thing on every run, and the only fixed point is the blob.')
    B.append('### ### **NEITHER NOTE MOVES A ROW, A CLUSTER OR A TERMINAL.**')
    B.append('')
    B.append(SUB)
    B.append('### ### **AND THIS ACT`S OWN LOCKED FACE CARRIED A WRONG FIGURE.**')
    B.append(SUB)
    B.append('### Section (A) reading (1) says the map`s table carries ### **THREE** ### of the')
    B.append('### syntheses` subjects. ### It carries ### **`%d`.**' % C1['map'])
    B.append('### The `3` came from this act`s own extract, whose predicate demanded a synthesis`s')
    B.append('### ### **WHOLE FILENAME STEM AS ONE CONTIGUOUS STRING** ### while the map writes')
    B.append('### ### **`Cubit / Trivium`** ### and ### **`Matter / cosmology`.** ### It matched')
    B.append('### three one-word names and missed four subjects the table plainly carries.')
    B.append('### ### ### **IT IS THE SAME SPECIES THIS ACT WITHDRAWS `b388`\'S FINDING FOR**,')
    B.append('### ### ### committed by this act`s own instrument, and carried onto a face that')
    B.append('### ### ### was locked before it was caught.')
    B.append('### ### **THE LOCKED FACE IS NOT EDITED.** ### Both figures are printed, here and in')
    B.append('### the component, with the defective predicate named -- because ### **A SEAT THAT')
    B.append('### ### CORRECTS AN ERROR BY QUIETLY REPORTING A DIFFERENT NUMBER HAS HIDDEN THE')
    B.append('### ### ERROR INSIDE THE CORRECTION**, and a locked face is exactly where that')
    B.append('### hiding would be easiest.')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, ANSWERED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(F1)` more than six cluster syntheses exist ### **-- MET** ### (`%d` on disk).'
             % C1['disk'])
    B.append('###   `(F2)` at least three deposited software records sit at versions their')
    B.append('###   repositories have passed ### **-- UNTESTED. ### THE PLATFORM DID NOT ANSWER,')
    B.append('###   ### AND THIS ACT SAYS SO RATHER THAN GUESSING.**')
    B.append('###   `(F3)` no written deposit rule is located ### **-- MET**, by a search proved')
    B.append('###   by name and by content.')
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the three populations will not nest ### **-- MET**, and the memberships')
    B.append('###   differ in ### **BOTH** ### directions.')
    B.append('###   `(E2)` the verdict will be ABSENT and the document correct ### **-- HALF')
    B.append('###   ### MET.** ### The document is correct as written; ### **THE VERDICT IS NOT')
    B.append('###   ### `ABSENT` BUT `UNDECIDABLE-WITHOUT-CREDENTIALS`**, because an')
    B.append('###   unauthenticated read cannot tell absent from private and this seat registered')
    B.append('###   a verdict its own instrument could not reach. ### **THE EXPECTATION IS')
    B.append('###   ### REPORTED AS PART-REFUTED RATHER THAN RE-READ TO FIT.**')
    B.append('###   `(E3)` the head notes will be the smallest write and the only corpus write')
    B.append('###   that is not a ledger append ### **-- MET**, `+%d` lines across two files with'
             % (C4['cluster']['added'] + C4['constellation']['added']))
    B.append('###   `%d` deleted.' % C4['deleted'])
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### ' + SCOPE.replace('**', ''))
    B.append('')
    B.append(SUB)
    B.append('### THE APPARATUS.')
    B.append(SUB)
    B.append('### **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on `b378`\'s lock')
    B.append('### gate run as `b389`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### DIGEST.**')
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint.' % (E['reads'], E['without_anchor'], E['anchors_differing']))
    for n in ('b389_reads', 'b389_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    regtxt = io.open(os.path.join(D, 'b389_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'### sha256 +: ([0-9a-f]{64})', regtxt) or re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at \(UTC\) : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY '
             'ADDED.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLUSTER WAS ADDED TO THE MAP.', '### THE DEPOSITED LAYER WAS ENUMERATED.',
                '### A DEPOSIT RULE WAS WRITTEN.', '### THE CITING DOCUMENT WAS WRONG.',
                '### A PRIOR HEAD WAS REPLACED.',
                '### A RECORD WAS READ FROM THE CORPUS INSTEAD.',
                '### SOMETHING WAS WRITTEN AT ZENODO.',
                '### b388 WAS RIGHT ABOUT THE KERNEL.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec('')
    rec('=' * 100)
    rec('  ### desk %d ; closed %d ; head notes %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], C4['notes'], tr['appended_only'], rownum, kok))
    rec('=' * 100)
    p = run_clock.write(D, 'b389_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, C4=C4,
             bank='b389_the_look_see.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b389_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
