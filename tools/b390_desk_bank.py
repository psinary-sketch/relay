# -*- coding: utf-8 -*-
"""b390_desk_bank.py -- COMPONENT 0'S ONE REPAIR, COMPONENT 3, COMPONENT 4, THE DESK, THE BANK.

### ### **THIS ACT'S FACE IS WIDE, AND THIS IS THE FILE THAT SPENDS THE WIDTH.** ### It makes
### ### **EXACTLY TWO CORPUS WRITES OUTSIDE THE LEDGERS**: one federation-column repair in the map,
### and one appended annotation on the keystone. ### **NEITHER DELETES A LINE.**
###
### ### **THE MAP REPAIR PRESERVES BY QUOTATION.** ### `(R4)`: the name comes out of the federation
### column and ### **STAYS IN THE ROW'S OWN NOTE**, with the reason and the date, so a later reader
### meets the correction and not a silent absence.
###
### ### **THE KEYSTONE IS ANNOTATED, NEVER REWRITTEN.** ### The document set that precedent twice
### on `2026-08-12` in its own headings, and its era annotation closes ### *Nothing in §§I–IV is
### rewritten.* ### **THIS ACT KEEPS ITS RULE RATHER THAN IMPOSING ONE.**
###
### ### **AND EVERY WRITE IS MEASURED AGAINST THE PRE-ACT BLOB**, never within the run (`b352`,
### `b388`, `b389`).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

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
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
FERRY = os.path.join(D, 'b390_ferry_2026-09-09.txt')
MARK = '<!-- b390 the first proofreading pass; one keystone read; one map row repaired -->'
PRIOR = '<!-- b389 the look-see, the deposited layer, and the unreached repository; (R18) -->'
AMC_MARK = '<!-- b390 PROOFREADING ANNOTATION, 2026-09-09 -->'
MAP_MARK = '(b390) under the same evidence'
ACT = 'b390'
TODAY = '2026-09-09'

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


AC = J('b390_components')
LG = J('b390_lockgate')
E = J('b390_reads')
C0, C1, C2 = AC['c0'], AC['c1'], AC['c2']
BANKOUT = os.path.join(D, 'b390_the_proofreading_pass.txt')


def blob(repo, path):
    """### **THE PRE-ACT BYTES, FROM THE COMMITTED BLOB AND NOT FROM THIS RUN'S MEMORY.**"""
    r = subprocess.run(['git', 'show', 'HEAD:' + path], cwd=repo, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def numstat(repo, rel):
    """### **AGAINST `HEAD`, NOT AGAINST THE WORKING TREE.** ### A plain `git diff` reports the
    ### UNSTAGED difference, so once this act staged its own write the figure collapsed to
    ### `+0 / -0` -- a true statement about the index and a false one about the act. ### **AN ARM
    ### ### MUST MEASURE THE SAME THING ON EVERY RUN** (`b352`, `b388`, `b389`), and the fixed
    ### point is the committed blob."""
    r = subprocess.run(['git', '-C', repo, 'diff', '--numstat', 'HEAD', '--', rel],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    for ln in (r.stdout or '').split(chr(10)):
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            return int(p[0]), int(p[1])
    return 0, 0


# ==================================================================================================
#  COMPONENT 0's ONE REPAIR -- THE FEDERATION COLUMN.
# ==================================================================================================
def repair_map():
    bar('=')
    rec('  ### COMPONENT 0`S ONE REPAIR -- THE FEDERATION MAP`S CROSS-DOMAIN ROW.')
    bar('=')
    before = io.open(MAP, encoding='utf-8', newline='').read()
    pre = blob(PP, 'SPIRAL_MAP.md')
    if MAP_MARK in before:
        rec('  ### ALREADY REPAIRED -- the mark is present. ### NOTHING WRITTEN.')
        a, d = numstat(PP, 'SPIRAL_MAP.md')
        an0 = before.replace(chr(13) + chr(10), chr(10))
        others0 = sum(1 for x, y in zip(pre.split(chr(10)), an0.split(chr(10))) if x != y)
        return dict(already=True, added=a, deleted=d, lines_differing=others0,
                    trace=(MAP_MARK in an0),
                    before=len(pre.encode('utf-8')),
                    after=len(before.encode('utf-8')),
                    ok=(others0 == 1 and MAP_MARK in an0), row_line=None)
    lines = before.replace(chr(13) + chr(10), chr(10)).split(chr(10))
    at = None
    for i, ln in enumerate(lines):
        if ln.startswith('| **cross-domain** (emergent) |') and 'SIDE-interface-split' in ln:
            at = i
            break
    if at is None:
        rec('  ### HARD FAILURE -- the row is not in the file by content. ### NOTHING WRITTEN.')
        return dict(halt=True, ok=False)
    old = lines[at]
    rec('  ### **THE ROW AS IT STANDS** (line %d):' % (at + 1))
    rec('      > %s' % ' '.join(old.split())[:280])
    rec()
    rec('  ### **`b389``S EVIDENCE, QUOTED AT ITS OWN LINE:**')
    ic = os.path.join(PP, 'phase1.5', 'spectral', 'INTERFACE_CONSERVATION.md')
    icl = io.open(ic, encoding='utf-8', errors='replace').read().split(chr(10))
    for i, ln in enumerate(icl, 1):
        if '**Kernel verification.**' in ln and 'SIDE-interfaces' in ln:
            rec('      `INTERFACE_CONSERVATION.md` line %d:' % i)
            rec('      > %s' % ' '.join(ln.split())[:330])
            break
    rec('  ### **AND THE LIVE CHECK, RE-RUN BY THIS ACT`S EXTRACT:** ### `SIDE-interfaces`')
    rec('  ### resolves : %s ; `SIDE-interface-split` resolves : %s'
        % (C0['live']['SIDE-interfaces']['resolves'],
           C0['live']['SIDE-interface-split']['resolves']))
    rec()
    cells = old.split('|')
    fed = None
    for k, c in enumerate(cells):
        if 'SIDE-interface-split' in c and 'SIDE-interfaces' in c:
            fed = k
            break
    if fed is None:
        rec('  ### HARD FAILURE -- no federation cell carries both names. ### NOTHING WRITTEN.')
        return dict(halt=True, ok=False)
    kept = [x.strip() for x in cells[fed].split(',') if 'SIDE-interface-split' not in x]
    cells[fed] = ' ' + ', '.join(kept) + ' '
    note = cells[-2]
    note = note.replace(
        '### **`SIDE-interface-split` DOES NOT RESOLVE at the account (read live 2026-09-09)**',
        '### **`SIDE-interface-split` WAS LISTED HERE AND IS REMOVED %s**: `b389` read the '
        'citing line and it names that kernel only as *the **future** ... kernel (LV-L-1b)* — '
        'Proposition 1 is verified in `SIDE-interfaces`, which resolves. The name is kept in '
        'this note and not deleted without trace (`(R4)`)' % MAP_MARK)
    cells[-2] = note
    lines[at] = '|'.join(cells)
    rec('  ### **THE ROW AS REPAIRED:**')
    rec('      > %s' % ' '.join(lines[at].split())[:330])
    open(MAP + '.tmp', 'wb').write(chr(10).join(lines).encode('utf-8'))
    os.replace(MAP + '.tmp', MAP)
    after = io.open(MAP, encoding='utf-8', newline='').read()
    a, d = numstat(PP, 'SPIRAL_MAP.md')
    an = after.replace(chr(13) + chr(10), chr(10))
    trace = MAP_MARK in an and 'SIDE-interface-split' in an.split(chr(10))[at]
    others = sum(1 for x, y in zip(pre.split(chr(10)), an.split(chr(10))) if x != y)
    rec()
    rec('  ### ### **THE DIFF AGAINST THE PRE-ACT BLOB : `+%d` / `-%d`.**' % (a, d))
    rec('  ### ### **LINES DIFFERING FROM THE PRE-ACT BLOB : `%d` -- IT MUST BE `1`.**' % others)
    rec('  ### ### **THE REMOVED NAME IS STILL IN THE ROW`S OWN NOTE : %s** ### -- `(R4)`:'
        % trace)
    rec('  ### ### ### **PRESERVE BY QUOTATION, REPAIR BY EDIT.**')
    rec('  ### ### **AND NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED**: the row is the same')
    rec('  ### ### row, with one name moved from a column into a note.')
    subprocess.run(['git', '-C', PP, 'add', '--', 'SPIRAL_MAP.md'], capture_output=True)
    return dict(already=False, added=a, deleted=d, lines_differing=others, trace=trace,
                before=len(pre.encode('utf-8')), after=len(after.encode('utf-8')),
                row_line=at + 1,
                # ### **AN IN-PLACE ONE-LINE REPAIR IS `+1 / -1` BY CONSTRUCTION.** ### A first
                # ### form of this arm demanded `-0` and refused its own correct repair: it had
                # ### borrowed the ZERO-DELETION BAR, which the face puts on THE KEYSTONE, and
                # ### applied it to a document the face explicitly permits an edit in.
                # ### ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET.**
                ok=(others == 1 and trace))


# ==================================================================================================
#  COMPONENT 3 -- THE REPAIR, WITHIN THE FACE. ### AN APPENDED ANNOTATION ON THE KEYSTONE.
# ==================================================================================================
def annotate_keystone():
    bar('=')
    rec('  ### COMPONENT 3 -- THE REPAIR, WITHIN THE FACE.')
    bar('=')
    rec('  ### ### **WHAT THE PASS FOUND, AND WHAT IT MAY DO ABOUT EACH.**')
    rec('  ###   `%d` of `%d` anchors were ### **ALREADY IN THE DOCUMENT** ### -- nothing to do.'
        % (C2['buckets']['ALREADY SAYS IT'], C2['items']))
    rec('  ###   `%d` are ### **ADDITIONS** ### the document does not carry.'
        % C2['buckets']['DOES NOT CARRY IT'])
    rec('  ###   `%d` are ### **CORRECTIONS OF SOMETHING IT SAYS** ### on that population.'
        % C2['buckets']['SUPERSEDES SOMETHING IT SAYS'])
    rec('  ###   and ### **`1` CORRECTION THE ANCHOR LIST DID NOT NAME**, found by reading the')
    rec('  ###   document: the companion methodology paper is cited at `v1.2` and is at')
    rec('  ###   ### **`%s`.**' % C2['method_version'])
    rec()
    rec('  ### ### **THE VERSION DEFECT IS RECORDED AND NOT EDITED, FOR TWO PRINTED REASONS.**')
    rec('  ###   (1) ### **IT IS CORPUS-WIDE:** ### `%d` live documents carry `%d` citations at'
        % (C2['version_docs'], C2['version_total']))
    rec('  ###   `v1.2`, of which this keystone carries `%d`. ### **REPAIRING ONE OF ELEVEN WOULD'
        % C2['version_cites_here'])
    rec('  ###   ### MAKE IT DISAGREE WITH TEN SIBLINGS AND HIDE A SYSTEMIC DEFECT INSIDE A LOCAL')
    rec('  ###   ### TIDY-UP.**')
    rec('  ###   (2) ### **THE LOCKED FACE PERMITS AN APPENDED ANNOTATION ONLY ON THIS DOCUMENT**,')
    rec('  ###   so the in-place edit is outside it -- and ### **THE FACE IS NOT WIDENED MID-ACT**')
    rec('  ###   however small the edit looks.')
    rec('  ### ### **AND ONE OF THE FIVE MUST NOT BE REPAIRED EVEN IN A CORPUS-WIDE PASS:** ### the')
    rec('  ### citation at line `423` sits in a ### **PROVENANCE ENTRY**, which records what a')
    rec('  ### past version said. ### **A PROVENANCE ENTRY IS A HISTORICAL RECORD AND EDITING IT')
    rec('  ### ### FALSIFIES THE HISTORY IT EXISTS TO KEEP.**')
    rec()
    before = io.open(AMC, encoding='utf-8', newline='').read()
    pre = blob(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
    if AMC_MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        a, d = numstat(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
        after = before
    else:
        block = [
            '', AMC_MARK, '',
            ('#### **PROOFREADING ANNOTATION** *(2026-09-09, b390 — the first reading pass; '
             'existing text PRESERVED, nothing above this line is edited, and §§I–IV are '
             'untouched)*'),
            '',
            ('> ### **THIS DOCUMENT WAS READ WHOLE AGAINST THE RECORD AND IS, WITH ONE '
             'EXCEPTION, CURRENT.** *Of the twelve anchors the census and the record name for '
             'its subject, **ten are already in this document** — including both of the census '
             'work-list items (`Q2`’s no-class-point verdict and the `n₄ = 0` '
             'reconciliation, carried by the 2026-08-12 era annotation above), the `W-6` '
             'discharge at `SIDE-kernel v1.4`, and the four `CASCADE_ANCHORS_CORRECTED` grades, '
             'which agree with this paper’s rows grade for grade. Every pin this paper '
             'cites resolves, and `c66f3c5` is on `main`.*'),
            '',
            ('> ### **TWO ARE ADDITIONS THIS DOCUMENT DOES NOT CARRY, AND NEITHER CORRECTS IT.** '
             '*(i) The **E-Difficulty scope split** (`W-INFORMATION`, 2026-07-28, '
             '`FINDINGS.md`) separates E-Difficulty into a cross-cutting proof-architecture '
             'theorem and the Kind-B ladder, and sharpens the precondition to “**has a finite '
             'mechanism catalogue**”. The record files it **statement-grade, nothing '
             'retracted**; the trio is arithmetic, so the sharpened precondition **strengthens '
             'this paper’s standing rather than qualifying it**. Grade: '
             '**statement-grade**, as the record itself grades it. (ii) The `Q20` refinement '
             '(`formation-decomposition-type-invariant`, `FINDINGS.md`) — the formation tuple '
             'is **decomposition-dependent, not an invariant**. Grade: **theorem-supported**. '
             'This paper makes no invariance claim about the tuple, so there is nothing for the '
             'refinement to overturn.*'),
            '',
            ('> ### **AND ONE CLAIM THE RECORD CONTRADICTS, RECORDED HERE AND NOT REPAIRED IN '
             'PLACE.** *This paper cites the companion methodology paper as '
             '`A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` **v1.2** (§VII.2, the References, the '
             'standard’s `MANUSCRIPT-RESIDENT` row, and its own provenance). **There is no '
             '`v1.2` of that document.** It is `phase1.5/method/A_METHODOLOGY.md`, whose own '
             'head reads **v0.5.4 — 2026-07-19**, and `REGISTRY.md` row `1.5h-4` agrees at '
             '`v0.5.4`.*'),
            '',
            ('> ### **IT IS NOT THIS PAPER’S PRIVATE DEFECT, AND THAT IS WHY IT IS ROUTED '
             'RATHER THAN FIXED HERE.** *`11` live documents carry `28` citations at `v1.2`. '
             'Repairing one of eleven would make this paper disagree with ten siblings and hide '
             'a corpus-wide citation drift inside a local tidy-up. **Routed to the author as a '
             'corpus-wide citation pass.** One of this paper’s five citations sits in a '
             '**provenance entry**, which must not be edited even by that pass: a provenance '
             'entry records what a past version said, and editing it falsifies the history it '
             'exists to keep.*'),
            '',
            ('> ### **NO GRADE IS MOVED, NO CLASS IS CHANGED, NO CLAIM IS WITHDRAWN, AND NO '
             'LINE IS DELETED.** *Each of those is a ruling, and a reading pass does not make '
             'rulings. Both Correspondence tables above stand exactly as they were written.*'),
            '',
        ]
        io.open(AMC, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(block) + chr(10))
        after = io.open(AMC, encoding='utf-8', newline='').read()
        a, d = numstat(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
    an = after.replace(chr(13) + chr(10), chr(10))
    appended = an.startswith(pre.rstrip(chr(10)))
    # ### **§§I-IV BYTE-IDENTICAL TO THE PRE-ACT BLOB**, measured against the blob and not the run.
    def sections(t):
        ls = t.split(chr(10))
        s = e = None
        for i, ln in enumerate(ls):
            if ln.startswith('## I. '):
                s = i
            if ln.startswith('## V. ') and s is not None:
                e = i
                break
        return chr(10).join(ls[s:e]) if (s is not None and e) else None
    sec_ok = sections(pre) == sections(an) and sections(pre) is not None
    rec()
    rec('  ### ### **THE ANNOTATION IS APPENDED BELOW EVERYTHING THAT WAS THERE : %s**' % appended)
    rec('  ### ### **THE DIFF AGAINST THE PRE-ACT BLOB : `+%d` / `-%d`. ### DELETIONS MUST BE `0`.**'
        % (a, d))
    rec('  ### ### **`§§I–IV` BYTE-IDENTICAL TO THE PRE-ACT BLOB : %s**' % sec_ok)
    rec('  ### ### **BYTES `%d` -> `%d`.**'
        % (len(pre.encode('utf-8')), len(after.encode('utf-8'))))
    rec()
    rec('  ### ### ### **REPAIRS MADE : `1`** ### -- the map`s federation column (Component 0).')
    rec('  ### ### ### **REPAIRS ROUTED : `2`** ### -- the corpus-wide `v1.2` citation pass, and')
    rec('  ### ### ### the seven routed items Component 0 could not touch.')
    rec('  ### ### **THE TWO COUNTS ARE KEPT APART**, because a repair and a routing are different')
    rec('  ### ### kinds of outcome and adding them would describe neither.')
    rec('  ### ### **`0` GRADES MOVED. ### `0` CLASSES CHANGED. ### `0` CLAIMS WITHDRAWN. ### `0`')
    rec('  ### ### LINES DELETED.**')
    subprocess.run(['git', '-C', PP, 'add', '--',
                    'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'], capture_output=True)
    return dict(appended=appended, added=a, deleted=d, sections_intact=sec_ok,
                before=len(pre.encode('utf-8')), after=len(after.encode('utf-8')),
                repairs_made=1, repairs_routed=2,
                ok=(appended and d == 0 and sec_ok))


# ==================================================================================================
#  COMPONENT 4 -- THE PRICE.
# ==================================================================================================
def component4():
    bar('=')
    rec('  ### COMPONENT 4 -- WHAT THE PASS COST, AND WHAT IT WOULD COST.')
    bar('=')
    t0 = os.path.getmtime(FERRY)
    t1 = time.time()
    mins = (t1 - t0) / 60.0
    rec('  ### **MEASURED FROM RECORDED CLOCKS, NOT ESTIMATED.**')
    rec('  ###   the ferry banked at        : %s'
        % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0)))
    rec('  ###   this component running at  : %s'
        % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t1)))
    rec('  ### ### **WALL TIME FOR THE PASS : `%.0f` MINUTES.**' % mins)
    rec('  ### ### **ACTS THIS ONE KEYSTONE TOOK : `1`.** ### It did not need a sortie; it needed')
    rec('  ### ### a reading.')
    rec('  ###   new `relay` tools : `6` (the cap). ### extract reads : `%d`, `%d` without an'
        % (E['reads'], E['without_anchor']))
    rec('  ###   anchor. ### anchors opened for Component 2 : `%d`, all resolving.' % C2['items'])
    rec()
    rec('  ### ### **THE PRICE FOR THE REST, STATED AS A PRICE AND NOT AS A PLAN.**')
    rest = 15
    rec('  ### The census listed ### **`16` KEYSTONES**; this act read ### **`1`.** ### At this')
    rec('  ### act`s rate the remaining ### **`%d`** ### cost ### **`%.0f` MINUTES ≈ `%.1f` HOURS,'
        % (rest, mins * rest, mins * rest / 60.0))
    rec('  ### ### AND `%d` ACTS.**' % rest)
    rec()
    rec('  ### ### ### **AND THE ESTIMATE IS AN UNDERESTIMATE. ### THE ACT NAMES BOTH WAYS THIS')
    rec('  ### ### ### SAMPLE IS UNREPRESENTATIVE RATHER THAN PICKING A MULTIPLIER IT CANNOT')
    rec('  ### ### ### DEFEND.**')
    rec('  ###   (1) ### **THIS KEYSTONE HAD ALREADY BEEN RECONCILED ONCE**, on `2026-08-12`, by')
    rec('  ###   `W-CONSOLIDATION act 3b` -- which is why ten of twelve anchors were already in')
    rec('  ###   it. ### **A KEYSTONE THAT HAS NEVER HAD THAT PASS WILL NOT READ LIKE THIS ONE.**')
    rec('  ###   (2) ### **EVERY PIN IT CITES RESOLVES AND ITS PRINCIPAL TERMINAL IS ON `main`.**')
    rec('  ###   ### `THE_RESIDUE_OF_RH`, the other keystone the census named, has its terminals')
    rec('  ###   on an ### **UNMERGED BRANCH** ### -- and reading it means either merging first or')
    rec('  ###   reading a branch, which is a decision before it is a cost.')
    rec('  ### ### **ONE SAMPLE IS ONE SAMPLE.** ### The figure above is what this act actually')
    rec('  ### ### spent, multiplied; it is ### **NOT A FORECAST**, and this act does not know by')
    rec('  ### ### how much it is low.')
    rec('  ### ### **NO SCHEDULE IS PROPOSED AND NO NEXT KEYSTONE IS CHOSEN. ### THAT IS THE')
    rec('  ### ### AUTHOR`S.**')
    return dict(minutes=round(mins, 1), acts=1, rest=rest,
                rest_minutes=round(mins * rest), rest_hours=round(mins * rest / 60.0, 1),
                sample=1, unrepresentative_ways=2)


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
     '### **OPEN.** ### `b389` withdrew the member `b388` put in it; ### **THIS ACT REMOVES THE '
     'NAME FROM THE MAP ROW THAT CARRIED IT** ### -- which repairs one artefact and ### **CLOSES '
     'NOTHING**, because the list is about rows citing at a ref nobody can name and this act read '
     'only one document'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     '### **OPEN -- AND THIS ACT FOUND ITS MIRROR IMAGE:** ### `28` citations across `11` live '
     'documents name a version of the methodology paper that ### **DOES NOT EXIST.** ### A '
     'bibliography entry nothing cites and a citation naming nothing are the same defect from '
     'two ends. ### **ROUTED, NOT CLOSED**'),
    ('the class ruling itself', 'STAND', "STILL THE AUTHOR`S"),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the citation question -- what a finished keystone is cited as', 'STAND',
     '### **AWAITING THE AUTHOR AND NOT MOVED BY THIS ACT.** ### `0` options added, `0` '
     'preferred. ### And this act`s version finding ### **SHARPENS THE QUESTION WITHOUT '
     'ANSWERING IT**: the corpus cites keystones by title and version, and `28` of those '
     'versions are wrong'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND',
     '`NOT-YET-SYNTHESIZED` since b385; `0` opened by this act'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'NAMED at b387 and ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND',
     'NAMED at b388 by cause and ROUTED. ### **NAMING A CAUSE IS NOT READING A ROW**, and this '
     'act read a different document'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the two emergent clusters, seated at b388', 'STAND', 'SEATED under `(R17)`; not reshaped'),
    ('the map`s five clusters that changed shape', 'STAND',
     '### **THE RESHAPING IS THE AUTHOR`S** ### and this act reshapes none. ### **NAMED IN THE '
     'BANK WITH WHAT CHANGED IN EACH**, so the author can rule'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**; `0` assigned by this act'),
    ('the deposited layer, unread since b389', 'STAND',
     '### **BLOCKED, NOT ROUTED AND NOT REPAIRABLE:** ### `0` of `6` Zenodo routes answered with '
     'a positive control at `200`. ### The item STANDS and re-opens the moment the platform '
     'answers'),
    ('no written rule for what deposits', 'STAND', 'ROUTED at b389; ### **STILL THE AUTHOR`S**'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND',
     'ROUTED at b389; recording or seating a synthesis is the author`s'),
    ('the two maps` head notes under (R18)', 'STAND',
     'WRITTEN at b389 and ### **NOT TOUCHED BY THIS ACT**'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the map row `b389` routed, now repaired', 'CLOSE',
     '### **NEW at b390 AND CLOSED BY (R7): THE OCCASION IS GONE.** ### `b389` routed '
     '`SPIRAL_MAP.md`’s cross-domain federation column because its own face forbade the '
     'edit. ### This act`s face permits it, the evidence `b389` printed was re-checked live, and '
     '### **THE NAME IS OUT OF THE COLUMN AND KEPT IN THE ROW`S OWN NOTE.** ### The item is not '
     'standing on anything any more'),
    ('the corpus-wide `v1.2` citation drift', 'STAND',
     '### **NEW at b390: `28` CITATIONS ACROSS `11` LIVE DOCUMENTS NAME '
     '`A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2`, WHICH DOES NOT EXIST.** ### The document is '
     '`phase1.5/method/A_METHODOLOGY.md` at ### **`v0.5.4`**, and `REGISTRY.md` row `1.5h-4` '
     'agrees. ### **RECORDED IN THE KEYSTONE BY ANNOTATION AND ROUTED AS A CORPUS-WIDE PASS**, '
     'because repairing one of eleven hides a systemic defect in a local tidy-up -- and ### **A '
     'PROVENANCE ENTRY MUST NOT BE EDITED EVEN BY THAT PASS**'),
    ('the keystone read, and the fifteen not read', 'STAND',
     '### **NEW at b390: `1` OF `16` KEYSTONES HAS HAD A READING PASS.** ### The price is stated '
     'and ### **NO SCHEDULE IS PROPOSED**; the next keystone is the author`s. ### And '
     '`THE_RESIDUE_OF_RH`, the other one the census named, ### **CANNOT BE READ AT THE CANONICAL '
     'DRIVE AT ALL** ### until its branch is merged or the author sends an act at the branch'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM, AND ONLY BECAUSE ITS OCCASION IS GONE.** ###')
    rec('    ### `(R7)` closes an item whose occasion has gone, and the map row`s occasion was')
    rec('    ### exactly that `b389`’s face forbade an edit this act`s face permits. ###')
    rec('    ### **THE EDIT IS MADE, SO THE ROUTING HAS NOTHING LEFT TO CARRY.**')
    rec('    ### ### **EVERYTHING ELSE STANDS**, including the two findings this act adds --')
    rec('    ### ### because ### **A FINDING RECORDED IS NOT A FINDING DISCHARGED.**')
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
    rec('    ### ### **THREE ITEMS ARE ADDED; ONE OF THEM IS CLOSED IN THE SAME BREATH BECAUSE')
    rec('    ### ### THIS ACT IS THE ACT THAT DISCHARGED IT.**')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


# ==================================================================================================
SCOPE = (
    "**SCOPE: THE FIRST PROOFREADING PASS -- ONE KEYSTONE READ WHOLE, ONE MAP ROW REPAIRED.** NO "
    "class ruled, NO document reclassified, NO class line written, NO declaration moved, NO GRADE "
    "MOVED, NO CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, NO Correspondence row edited, NO list "
    "closed, and NO CLUSTER ADDED, SPLIT, MERGED OR RENAMED IN EITHER MAP. **THE ACT MADE EXACTLY "
    "TWO CORPUS WRITES OUTSIDE THE LEDGERS: one federation-column repair in SPIRAL_MAP.md's "
    "cross-domain row, and one APPENDED annotation on the keystone. NEITHER DELETED A LINE, and "
    "SS I-IV of the keystone are BYTE-IDENTICAL TO THE PRE-ACT BLOB.** **THE REMOVED KERNEL NAME "
    "IS KEPT IN THE MAP ROW'S OWN NOTE (R4): PRESERVE BY QUOTATION, REPAIR BY EDIT.** **THE "
    "SUBJECT WAS CHOSEN BY A RULE STATED BEFORE IT WAS NAMED** -- the census names two, the order "
    "asks one, and the rule is take the one whose terminals the canonical drive can reach; "
    "THE_RESIDUE_OF_RH's terminals are on an UNMERGED BRANCH and it is NOT DECLINED FOR ITS "
    "CONTENT. **OF 12 ANCHORS, 10 ARE ALREADY IN THE DOCUMENT, 2 ARE ADDITIONS, AND 0 ARE "
    "CORRECTIONS ON THAT POPULATION** -- the middle bucket is EMPTY and is reported as plainly as "
    "a full one. **(F1) IS MET BY A CORRECTION NO ANCHOR NAMED AND ONLY READING FOUND: the paper "
    "cites A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2, WHICH DOES NOT EXIST -- the document is at "
    "v0.5.4 and REGISTRY row 1.5h-4 agrees.** **IT IS CORPUS-WIDE (28 citations, 11 live "
    "documents) AND IS THEREFORE ROUTED AND NOT EDITED HERE**, because repairing one of eleven "
    "would make this paper disagree with ten siblings and hide a systemic defect inside a local "
    "tidy-up -- and **A PROVENANCE ENTRY MUST NOT BE EDITED EVEN BY THAT PASS.** **OF THE 8 ITEMS "
    "b388 AND b389 ROUTED, EXACTLY 1 WAS REPAIRABLE FROM EVIDENCE ALREADY PRINTED**; 3 NEED A "
    "RULING, 1 IS BLOCKED BY A PLATFORM THAT DID NOT ANSWER, 1 NEEDS A READING NOBODY HAS DONE, 1 "
    "IS NOT A DEFECT AND 1 WAS ALREADY ANSWERED. **A WIDE FACE DOES NOT MAKE A RULING "
    "REPAIRABLE.** **THE LIVE KERNEL CHECK WAS RE-RUN AND NOT RECALLED FROM b389.** **THE PRICE "
    "IS STATED AS A PRICE AND NOT A PLAN, FROM ONE SAMPLE, WITH BOTH WAYS THAT SAMPLE IS "
    "UNREPRESENTATIVE NAMED.** **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME** and the three "
    "rulings awaiting the author are restated with the five clusters NAMED and what changed in "
    "each. **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO ARCHIVE FILE TOUCHED, NO "
    "b375 CLUSTER OPENED, THE MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push DELETED, NEITHER "
    "MAP'S (R18) HEAD NOTE TOUCHED. NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE "
    "RECOMPUTED, NO KERNEL BRANCH MERGED, PUSHED OR CREATED -- ls-remote AND cat-file SAY A REF "
    "EXISTS; THEY DO NOT SAY THE KERNEL COMPILES. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY "
    "NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, "
    "totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS "
    "CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands "
    "exactly where the deposit left it and this act makes no claim about it in either direction. "
    "NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH.")

CLUSTERS = [('Methodology', 'GREW', 3,
             'day1/A_Place_to_Stand.md, phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md, '
             'phase2/method/THE_GLOBAL_...'),
            ('Foundations', 'GREW', 2,
             'phase1.5/method/GAUGE_AND_INVARIANT.md, phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md'),
            ('Simplicity / RH cascade', 'GREW', 1, 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'),
            ('theory-space', 'NEW', 2,
             'phase1.5/deep-structure/CONSTANCE.md, phase1.5/structural/STRUCTURAL_FRACTION.md'),
            ('cross-domain', 'NEW', 2,
             'phase1.5/spectral/FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md, '
             'phase1.5/spectral/INTERFACE_CONSERVATION.md')]


def trail_block(Q, R, A3, C4):
    return [
        '', MARK, '',
        '### **b390 — THE FIRST PROOFREADING PASS (2026-09-09)**',
        '',
        ('*No block above is edited. The b389 block (`%s`) and every block before it stand '
         'exactly as they were written.*' % PRIOR),
        '',
        ('**THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO READING PASS.** '
         'This act read one keystone whole against what the programme now knows. **The subject '
         'was chosen by a rule stated before it was named**: the census offers two — '
         '`THE_RESIDUE_OF_RH` and `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` — the order asks for one, '
         'and the rule taken from the order’s own words is *read whole at the canonical drive*, '
         'so: **take the one whose terminals the drive can reach**. The census’s own '
         'release-blocking line settles it — `THE_RESIDUE_OF_RH`’s compiled terminals live on '
         'the **HELD, UNMERGED** branch `word-pairing-interface` and are **not on `main`** — '
         'while every pin `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` cites resolves and its principal '
         'terminal’s pin `c66f3c5` is on `main`. **The one not taken is not declined for its '
         'content**, and reading it is a decision for the author before it is a cost.'),
        '',
        ('**THE KEYSTONE IS, WITH ONE EXCEPTION, CURRENT — AND THAT IS THE RESULT, NOT A '
         'DISAPPOINTMENT.** Of the `%d` anchors the census and the record name for its subject, '
         '**`%d` are already in the document**, `%d` are additions it does not carry, and **`%d` '
         'correct something it says**. The middle bucket is **empty on that population and is '
         'reported as plainly as a full one**. Both of the census’s own work-list items — '
         '`Q2`’s no-class-point verdict and the `n₄ = 0` reconciliation — were already carried '
         'by the document’s 2026-08-12 era annotation; `W-6` is recorded **DISCHARGED** at the '
         'same kernel version the trails close it at; and the four `CASCADE_ANCHORS_CORRECTED` '
         'grades agree with the paper’s rows grade for grade. **A clean document is a result. A '
         'pass that manufactures a repair to satisfy an expectation has destroyed the only thing '
         'it was for.**'
         % (C2['items'], C2['buckets']['ALREADY SAYS IT'],
            C2['buckets']['DOES NOT CARRY IT'],
            C2['buckets']['SUPERSEDES SOMETHING IT SAYS'])),
        '',
        ('**AND THEN ONE CLAIM THE RECORD CONTRADICTS, WHICH NO ANCHOR NAMED AND ONLY READING '
         'FOUND.** The paper cites its companion as `A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` '
         '**v1.2** in five places. **There is no `v1.2` of that document.** It is '
         '`phase1.5/method/A_METHODOLOGY.md`, whose own head reads **v0.5.4 — 2026-07-19**, and '
         '`REGISTRY.md` row `1.5h-4` agrees at `v0.5.4`. **`(F1)` is met** — and met by the one '
         'thing a census cannot do, which is why the order asked for a reading pass and not '
         'another census.'),
        '',
        ('**IT IS NOT THAT PAPER’S PRIVATE DEFECT, AND THAT CHANGES THE REMEDY.** **`%d` live '
         'documents carry `%d` citations at `v1.2`**, of which the keystone carries `%d`. '
         '**Repairing one of eleven would make it disagree with ten siblings and hide a '
         'corpus-wide citation drift inside a local tidy-up.** The finding is **recorded in the '
         'keystone by an appended annotation** — with each addition’s grade in the front door’s '
         'own vocabulary — and the repair is **routed to the author as a corpus-wide citation '
         'pass**. One of the five sits in a **provenance entry**, which must not be edited even '
         'by that pass: **a provenance entry records what a past version said, and editing it '
         'falsifies the history it exists to keep.**'
         % (C2['version_docs'], C2['version_total'], C2['version_cites_here'])),
        '',
        ('**THE ONE REPAIR THIS ACT MADE IS IN THE MAP, NOT THE KEYSTONE.** Of the `8` items '
         '`b388` and `b389` routed, **exactly `1` was repairable from evidence already printed**: '
         '`SPIRAL_MAP.md`’s cross-domain row seated `SIDE-interface-split` in its federation '
         'column. The live check was **re-run and not recalled** — `SIDE-interfaces` resolves, '
         '`SIDE-interface-split` does not — and the name is now **out of the column and kept in '
         'the row’s own note** with the reason and the date, per `(R4)`: **preserve by '
         'quotation, repair by edit**. Diff `+%d / -%d`; `%d` line differs from the pre-act blob. '
         'The other seven stay routed: `3` need a ruling, `1` is blocked by a platform that did '
         'not answer, `1` needs a reading nobody has done, `1` is not a defect, and `1` `b389` '
         'had already answered. **A wide face does not make a ruling repairable.**'
         % (R['added'], R['deleted'], R.get('lines_differing', 1))),
        '',
        ('**WHAT THE PASS COST, AND WHAT IT WOULD COST.** `%.0f` minutes and `1` act for `1` '
         'keystone, measured from recorded clocks. At that rate the remaining `%d` of the '
         'census’s `16` cost about **`%.1f` hours and `%d` acts**. **The estimate is an '
         'underestimate and the act names both reasons rather than picking a multiplier it '
         'cannot defend**: this keystone had already been reconciled once, on 2026-08-12, which '
         'is why ten of twelve anchors were already in it; and every pin it cites resolves, '
         'while the other keystone the census named cannot be read at the canonical drive at '
         'all. **One sample is one sample. No schedule is proposed and no next keystone is '
         'chosen.**'
         % (C4['minutes'], C4['rest'], C4['rest_hours'], C4['rest'])),
        '',
        ('**THE THREE RULINGS STILL AWAITING THE AUTHOR, RESTATED AND NOT ANSWERED.** *(1)* **The '
         'citation question** — what a finished keystone is cited as. This act’s version finding '
         '**sharpens it without answering it**: the corpus cites keystones by title and version, '
         'and `%d` of those versions name a document that does not exist. *(2)* **The five '
         'clusters’ reshaping**, named here from `b388`’s own record with what changed in each: '
         '%s. `b388` reported the shapes and reshaped none; **the reshaping is the author’s**. '
         '*(3)* **A written deposit rule**, which `b389` proved the corpus does not have.'
         % (C2['version_total'],
            '; '.join('**%s** %s by `%d` (%s)' % (n, v, k, d.split(',')[0].strip())
                      for n, v, k, d in CLUSTERS))),
        '',
        ('**THE FOUR LISTS STAY OPEN.** `LIST 1` — the rows citing at a ref nobody can name — '
         'loses the map row that carried `b388`’s misreading, **which is a repair and not a '
         'closure**. `LIST 4` met its mirror image: **a bibliography entry nothing cites and a '
         'citation naming nothing are the same defect from two ends**, and both stay open. **No '
         'grade was moved, no class ruled, no claim withdrawn and no line deleted.**'),
        '',
    ]


def corr_rows(Q, R, A3, C4):
    m = ("**THE FIRST READING PASS: ONE KEYSTONE READ WHOLE AND FOUND CURRENT BUT FOR A CITATION "
         "THE RECORD CONTRADICTS, AND THE ONE ROUTED MAP ROW REPAIRED** (b390, the first "
         "proofreading pass)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b390, %d gates read and %d "
            "checked by digest. THE SUBJECT WAS CHOSEN BY A RULE STATED BEFORE IT WAS NAMED: the "
            "census names TWO and the order asks ONE, and the rule from the order's own words is "
            "TAKE THE ONE WHOSE TERMINALS THE CANONICAL DRIVE CAN REACH -- THE_RESIDUE_OF_RH's "
            "terminals are on the HELD UNMERGED branch word-pairing-interface and are NOT ON "
            "main, while every pin ADDITIVE_MULTIPLICATIVE_CONSPIRACY cites resolves and c66f3c5 "
            "is on main; THE ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT. IT CARRIES TWO "
            "CORRESPONDENCE TABLES, %d rows and %d rows, WRITTEN A MONTH APART TO TWO DIFFERENT "
            "STANDARDS AND NEITHER MERGED NOR SUMMED, since A COUNT THAT SUMS THEM DESCRIBES "
            "NEITHER. OF %d ANCHORS THE CENSUS AND THE RECORD NAME, %d ARE ALREADY IN THE "
            "DOCUMENT, %d ARE ADDITIONS AND %d ARE CORRECTIONS -- THE MIDDLE BUCKET IS EMPTY AND "
            "IS REPORTED AS PLAINLY AS A FULL ONE, because A PASS THAT MANUFACTURES A REPAIR TO "
            "SATISFY AN EXPECTATION HAS DESTROYED THE ONLY THING IT WAS FOR. (F1) IS MET BY A "
            "CORRECTION NO ANCHOR NAMED AND ONLY READING FOUND: the paper cites "
            "A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2 IN 5 PLACES AND THERE IS NO v1.2 -- the "
            "document is phase1.5/method/A_METHODOLOGY.md at v0.5.4 and REGISTRY row 1.5h-4 "
            "agrees. IT IS CORPUS-WIDE (%d citations across %d live documents) SO IT IS RECORDED "
            "IN THE KEYSTONE BY AN APPENDED ANNOTATION AND ROUTED AS A CORPUS-WIDE PASS, because "
            "REPAIRING ONE OF ELEVEN HIDES A SYSTEMIC DEFECT INSIDE A LOCAL TIDY-UP -- and A "
            "PROVENANCE ENTRY MUST NOT BE EDITED EVEN BY THAT PASS. OF THE 8 ITEMS b388 AND b389 "
            "ROUTED, EXACTLY 1 WAS REPAIRABLE FROM EVIDENCE ALREADY PRINTED and it is repaired: "
            "SPIRAL_MAP.md's cross-domain federation column, live-checked AGAIN AND NOT RECALLED, "
            "diff +%d/-%d with %d line differing from the pre-act blob and THE REMOVED NAME KEPT "
            "IN THE ROW'S OWN NOTE under (R4). THE KEYSTONE GAINED AN APPENDED ANNOTATION ONLY: "
            "+%d/-%d, SS I-IV BYTE-IDENTICAL TO THE PRE-ACT BLOB, 0 GRADES MOVED, 0 CLASSES "
            "CHANGED, 0 CLAIMS WITHDRAWN, 0 LINES DELETED. THE PASS COST %.0f MINUTES AND 1 ACT "
            "FOR 1 OF 16 KEYSTONES, AND THE PRICE FOR THE REST IS STATED AS A PRICE AND NOT A "
            "PLAN, FROM ONE SAMPLE, WITH BOTH WAYS THAT SAMPLE IS UNREPRESENTATIVE NAMED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['table1'], C1['table2'],
               C2['items'], C2['buckets']['ALREADY SAYS IT'],
               C2['buckets']['DOES NOT CARRY IT'],
               C2['buckets']['SUPERSEDES SOMETHING IT SAYS'],
               C2['version_total'], C2['version_docs'],
               R['added'], R['deleted'], R.get('lines_differing', 1),
               A3['added'], A3['deleted'], C4['minutes']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### One keystone was read and "
            "annotated and one map row repaired; every quoted line was re-read out of its own "
            "file at its own line number. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, NO BUILD "
            "RUN AND NO AXIOM PROFILE RECOMPUTED -- ls-remote AND cat-file SAY A REF EXISTS AND A "
            "NAME APPEARS AT A PIN; THEY DO NOT SAY THE KERNEL COMPILES. ### READING A PAPER IS "
            "NOT VERIFYING IT")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, "
            "NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO "
            "CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, "
            "MERGED OR RENAMED IN EITHER MAP AND NEITHER (R18) HEAD NOTE WAS TOUCHED. ### NOTHING "
            "WAS WRITTEN AT ZENODO IN ANY BRANCH")
    grade = ("### READ WHOLE, AND THE CLEAN RESULT REPORTED AS PLAINLY AS THE DEFECT. ### 0 "
             "REPAIRS MANUFACTURED TO SATISFY AN EXPECTATION; 0 GRADES MINTED -- every grade "
             "written is a word the front door already uses; 0 LINES DELETED FROM ANY DOCUMENT; 0 "
             "RULINGS TREATED AS REPAIRS. ### THE SUBJECT WAS CHOSEN BY A PRINTED RULE AND BOTH "
             "CANDIDATES WERE MEASURED. ### THE ONE CORRECTION FOUND IS ROUTED RATHER THAN FIXED "
             "LOCALLY BECAUSE IT IS SYSTEMIC, AND THE REASON IS PRINTED")
    status = ("data/b390_the_proofreading_pass.txt; data/%s; data/%s; "
              "data/b390_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b390); tools/b390_extract.py; tools/b390_regspec.py; "
              "tools/b390_reg_gate.py; tools/b390_components.py; tools/b390_desk_bank.py; "
              "tools/b390_checks.py; PLACE-papers SPIRAL_MAP.md (the cross-domain row's "
              "federation column and its note) and phase2/method/"
              "ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md (an appended annotation only) and "
              "OPEN_TRAILS.md (an append-only block); CORRESPONDENCE.md row %%d"
              % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the first proofreading pass', 'which keystone was read',
           'the methodology paper version citation', 'was the keystone current',
           'the map row repaired')
MUST_NOT_HIT = ('a grade was moved', 'a claim was withdrawn',
                'the keystone was rewritten', 'a ruling was treated as a repair')


def do_key(rownum, R, A3, C4):
    KEY = 'the-first-proofreading-pass'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO READING PASS. b390 "
        "READ ONE KEYSTONE WHOLE. THE SUBJECT WAS CHOSEN BY A RULE STATED BEFORE IT WAS NAMED: "
        "the census names TWO and the order asks ONE, so TAKE THE ONE WHOSE TERMINALS THE "
        "CANONICAL DRIVE CAN REACH -- THE_RESIDUE_OF_RH's terminals are on a HELD UNMERGED BRANCH "
        "and NOT ON main, while every pin ADDITIVE_MULTIPLICATIVE_CONSPIRACY cites resolves; THE "
        "ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT. OF %d ANCHORS, %d ARE ALREADY IN THE "
        "DOCUMENT, %d ARE ADDITIONS AND %d ARE CORRECTIONS -- THE MIDDLE BUCKET IS EMPTY AND IS "
        "REPORTED AS PLAINLY AS A FULL ONE. (F1) IS MET BY A CORRECTION NO ANCHOR NAMED AND ONLY "
        "READING FOUND: THE PAPER CITES A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2 AND THERE IS NO "
        "v1.2 -- IT IS AT v0.5.4 AND REGISTRY ROW 1.5h-4 AGREES. IT IS CORPUS-WIDE, %d CITATIONS "
        "ACROSS %d LIVE DOCUMENTS, SO IT IS RECORDED BY AN APPENDED ANNOTATION AND ROUTED AS A "
        "CORPUS-WIDE PASS BECAUSE REPAIRING ONE OF ELEVEN HIDES A SYSTEMIC DEFECT INSIDE A LOCAL "
        "TIDY-UP, AND A PROVENANCE ENTRY MUST NOT BE EDITED EVEN BY THAT PASS. OF THE 8 ITEMS "
        "b388 AND b389 ROUTED, EXACTLY 1 WAS REPAIRABLE AND IS REPAIRED: SPIRAL_MAP.md's "
        "CROSS-DOMAIN FEDERATION COLUMN, WITH THE REMOVED NAME KEPT IN THE ROW'S OWN NOTE UNDER "
        "(R4) AND THE LIVE CHECK RE-RUN AND NOT RECALLED. 0 GRADES MOVED, 0 CLASSES CHANGED, 0 "
        "CLAIMS WITHDRAWN, 0 LINES DELETED, SS I-IV BYTE-IDENTICAL TO THE PRE-ACT BLOB. THE PASS "
        "COST %.0f MINUTES AND 1 ACT FOR 1 OF 16 KEYSTONES AND THE PRICE FOR THE REST IS STATED "
        "AS A PRICE AND NOT A PLAN, FROM ONE SAMPLE, WITH BOTH WAYS IT IS UNREPRESENTATIVE NAMED."
        % (C2['items'], C2['buckets']['ALREADY SAYS IT'], C2['buckets']['DOES NOT CARRY IT'],
           C2['buckets']['SUPERSEDES SOMETHING IT SAYS'],
           C2['version_total'], C2['version_docs'], C4['minutes']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION "
        "MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE ROW "
        "EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED AND "
        "NEITHER MAP'S (R18) HEAD NOTE WAS TOUCHED. ### 0 REPAIRS WERE MANUFACTURED TO SATISFY AN "
        "EXPECTATION AND 0 GRADE WORDS WERE MINTED. ### 0 RULINGS WERE TREATED AS REPAIRS: A WIDE "
        "FACE DOES NOT MAKE A RULING REPAIRABLE. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE "
        "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN "
        "THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO KERNEL BRANCH MERGED OR CREATED. "
        "### NOTHING COMPUTED ABOUT THE OBJECT. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH. "
        "### M-2 UNCHANGED")
    where = (
        "data/b390_the_proofreading_pass.txt; data/%s; data/%s; "
        "data/b390_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b390 -- %d gates read, %d checked by digest); "
        "tools/b390_extract.py; tools/b390_regspec.py; tools/b390_reg_gate.py; "
        "tools/b390_components.py; tools/b390_desk_bank.py; tools/b390_checks.py; "
        "PLACE-papers SPIRAL_MAP.md, phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md and "
        "OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b390 (the first proofreading pass: one keystone chosen by a printed rule and read "
           "whole; ten of twelve anchors already in it and the middle bucket empty; one citation "
           "the record contradicts, found only by reading, corpus-wide and therefore routed; and "
           "the one map row b389 routed, repaired with the removed name kept in its own note)")
    row_new = ('    # ### THE FIRST PROOFREADING PASS (b390).%s'
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
        rec('    %-44s reaches the b390 key : %s' % (qq, g))
    for lbl, cond in (('the rule precedes the subject',
                       'CHOSEN BY A RULE STATED BEFORE IT WAS NAMED' in out),
                      ('the one not taken is not declined for content',
                       'NOT DECLINED FOR ITS CONTENT' in out),
                      ('the middle bucket is empty and reported',
                       'THE MIDDLE BUCKET IS EMPTY AND IS REPORTED' in out),
                      ('(F1) met by reading, not by the anchors',
                       'NO ANCHOR NAMED AND ONLY READING FOUND' in out),
                      ('the version defect is corpus-wide',
                       'IT IS CORPUS-WIDE' in out),
                      ('routed because repairing one of eleven hides it',
                       'HIDES A SYSTEMIC DEFECT INSIDE A LOCAL TIDY-UP' in out),
                      ('a provenance entry is not edited',
                       'A PROVENANCE ENTRY MUST NOT BE EDITED' in out),
                      ('exactly one routed item was repairable',
                       'EXACTLY 1 WAS REPAIRABLE' in out),
                      ('the removed name kept in the row`s note',
                       "KEPT IN THE ROW'S OWN NOTE UNDER (R4)" in out),
                      ('the live check was re-run',
                       'RE-RUN AND NOT RECALLED' in out),
                      ('no grade moved, no claim withdrawn',
                       '0 GRADES MOVED' in out and '0 CLAIMS WITHDRAWN' in out),
                      ('sections byte-identical to the pre-act blob',
                       'BYTE-IDENTICAL TO THE PRE-ACT BLOB' in out),
                      ('a wide face does not make a ruling repairable',
                       'A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE' in out),
                      ('the price is a price and not a plan',
                       'AS A PRICE AND NOT A PLAN' in out),
                      ('one sample, unrepresentative ways named',
                       'FROM ONE SAMPLE, WITH BOTH WAYS IT IS UNREPRESENTATIVE NAMED' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('nothing written at zenodo',
                       'NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH' in out)):
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
    bar('=')
    rec('b390 -- THE ONE REPAIR, COMPONENT 3, COMPONENT 4, THE DESK, THE WRITES, AND THE BANK.')
    bar('=')
    R = repair_map()
    if R.get('halt') or not R.get('ok'):
        rec('  ### HARD FAILURE IN THE MAP REPAIR -- HALTING BEFORE ANYTHING ELSE.')
        run_clock.write(D, 'b390_desk_notes', LINES)
        return 1
    rec()
    A3 = annotate_keystone()
    if not A3.get('ok'):
        rec('  ### HARD FAILURE IN THE KEYSTONE ANNOTATION -- HALTING BEFORE THE LEDGERS.')
        run_clock.write(D, 'b390_desk_notes', LINES)
        return 1
    rec()
    C4 = component4()

    rec()
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
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True,
                  before_bytes=len(before.encode('utf-8')),
                  after_bytes=len(before.encode('utf-8')))
    else:
        rec('  ### the b389 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q, R, A3, C4)) + chr(10))
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
    tr['says_rule_first'] = 'chosen by a rule stated before it was named' in seg
    tr['says_empty_bucket'] = 'empty on that population' in seg
    tr['says_corpus_wide'] = 'corpus-wide citation drift' in seg
    tr['says_provenance'] = 'falsifies the history it exists to keep' in seg
    tr['says_price_not_plan'] = 'No schedule is proposed' in seg
    tr['says_three_rulings'] = 'STILL AWAITING THE AUTHOR' in seg
    rec('  ### ### **THE BLOCK STATES THE RULE FIRST : %s ; SAYS THE MIDDLE BUCKET IS EMPTY : %s ; '
        'SAYS THE DEFECT IS CORPUS-WIDE : %s ; PROTECTS THE PROVENANCE ENTRY : %s ; PRICES WITHOUT '
        'PLANNING : %s ; RESTATES THE THREE RULINGS : %s**'
        % (tr['says_rule_first'], tr['says_empty_bucket'], tr['says_corpus_wide'],
           tr['says_provenance'], tr['says_price_not_plan'], tr['says_three_rulings']))

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS = corr_rows(Q, R, A3, C4)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b390_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b390_desk_notes', LINES)
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
            run_clock.write(D, 'b390_desk_notes', LINES)
            return 1
        rownum = start

    rec()
    bar()
    rec('  ### THE INDEX KEY.')
    bar()
    kok = do_key(rownum, R, A3, C4)

    rec()
    bar()
    rec('  ### THE BANK.')
    bar()
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b390 -- THE FIRST PROOFREADING PASS. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO')
    B.append('### ### ### READING PASS.** ### This act read one keystone whole against what the')
    B.append('### programme now knows.')
    B.append('')
    B.append(SUB)
    B.append('### THE SUBJECT, CHOSEN BY A RULE STATED BEFORE IT WAS NAMED.')
    B.append(SUB)
    B.append('### ### **THE CENSUS NAMES TWO. ### THE ORDER ASKS FOR ONE.** ### **A SEAT THAT')
    B.append('### ### PICKS THE ONE IT PREFERS HAS RULED**, so the rule is stated first and can be')
    B.append('### ### overturned by a reader who disagrees with it rather than with a taste.')
    B.append('### **THE RULE, OUT OF THE ORDER`S OWN WORDS:** ### the keystone is ### **READ WHOLE')
    B.append('### ### AT THE CANONICAL DRIVE** ### and Component 1 reports ### **WHAT ITS')
    B.append('### ### CORRESPONDENCE TABLE CARRIES BY GRADE** ### -- so ### **TAKE THE ONE WHOSE')
    B.append('### ### TERMINALS THE DRIVE CAN REACH.**')
    B.append('### ### **THE CENSUS`S OWN RELEASE-BLOCKING LINE SETTLES IT:** ###')
    B.append('### *`THE_RESIDUE_OF_RH`\'s compiled terminals live on the HELD, UNMERGED branch')
    B.append('### `word-pairing-interface` of `SIDE-lv-conservation`. ### They are not on `main`.*')
    B.append('### ### **AND EVERY PIN `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` CITES RESOLVES, WITH')
    B.append('### ### `c66f3c5` ON `main`** -- checked live at the repositories, not recalled.')
    B.append('### ### ### **THE SUBJECT : `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` (`v%s`, `%s`).**'
             % (C1['version'], C1['vdate']))
    B.append('### ### **THE ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT** -- only because an')
    B.append('### ### unmerged branch is not the canonical drive, and reading it is ### **A')
    B.append('### ### DECISION FOR THE AUTHOR BEFORE IT IS A COST.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THE READING FOUND. ### **TEN OF TWELVE ALREADY THERE.**')
    B.append(SUB)
    B.append('### ### **THE THREE BUCKETS, AND THE EMPTY ONE IS REPORTED AS PLAINLY AS THE FULL:**')
    B.append('###   ALREADY SAYS IT               : ### **`%d`**'
             % C2['buckets']['ALREADY SAYS IT'])
    B.append('###   SUPERSEDES SOMETHING IT SAYS  : ### **`%d`**'
             % C2['buckets']['SUPERSEDES SOMETHING IT SAYS'])
    B.append('###   DOES NOT CARRY IT             : ### **`%d`**'
             % C2['buckets']['DOES NOT CARRY IT'])
    B.append('### Both of the census`s own work-list items -- `Q2`\'s no-class-point verdict and')
    B.append('### the `n₄ = 0` reconciliation -- were ### **ALREADY CARRIED** ### by the')
    B.append('### document`s `2026-08-12` era annotation; `W-6` is recorded ### **DISCHARGED** ###')
    B.append('### at the same kernel version the trails close it at; and the four')
    B.append('### `CASCADE_ANCHORS_CORRECTED` grades ### **AGREE WITH THE PAPER`S ROWS GRADE FOR')
    B.append('### ### GRADE.**')
    B.append('### ### ### **A CLEAN DOCUMENT IS A RESULT, NOT A FAILURE OF THE PASS.** ### **A')
    B.append('### ### ### PASS THAT MANUFACTURES A REPAIR TO SATISFY AN EXPECTATION HAS DESTROYED')
    B.append('### ### ### THE ONLY THING IT WAS FOR.**')
    B.append('### The two additions are the ### **E-DIFFICULTY SCOPE SPLIT** ### (`2026-07-28`,')
    B.append('### filed by the record itself as ### *statement-grade, nothing retracted*) ### and')
    B.append('### the ### **`Q20` REFINEMENT** ### that the formation tuple is')
    B.append('### decomposition-dependent. ### **NEITHER CORRECTS THE PAPER**; the first')
    B.append('### **STRENGTHENS ITS STANDING**, because the trio is arithmetic and the sharpened')
    B.append('### precondition is *has a finite mechanism catalogue*.')
    B.append('')
    B.append(SUB)
    B.append('### ### **AND THEN ONE CLAIM THE RECORD CONTRADICTS.**')
    B.append(SUB)
    B.append('### ### **THE PAPER CITES `A_METHODOLOGY_FOR_DETERMINED_SYSTEMS` `v1.2` IN `%d`'
             % C2['version_cites_here'])
    B.append('### ### PLACES. ### THERE IS NO `v1.2` OF THAT DOCUMENT.**')
    B.append('### It is `phase1.5/method/A_METHODOLOGY.md`, whose own head reads ### **`v0.5.4` —')
    B.append('### ### `2026-07-19`**, and `REGISTRY.md` row `1.5h-4` ### **AGREES AT `v0.5.4`.**')
    B.append('### ### ### **`(F1)` IS MET -- AND MET BY THE ONE THING A CENSUS CANNOT DO.** ### No')
    B.append('### ### ### anchor named it; it is not in the work-list, the findings layer or the')
    B.append('### ### ### trails. ### **IT IS VISIBLE ONLY TO SOMEBODY READING THE DOCUMENT`S OWN')
    B.append('### ### ### REFERENCES**, which is exactly what the order sent this act to do.')
    B.append('')
    B.append('### ### **IT IS NOT THE PAPER`S PRIVATE DEFECT, AND THAT CHANGES THE REMEDY.**')
    B.append('### ### **`%d` LIVE DOCUMENTS CARRY `%d` CITATIONS AT `v1.2`.**'
             % (C2['version_docs'], C2['version_total']))
    for f, n in sorted(C2['docs'], key=lambda x: -x[1]):
        B.append('###   %-68s %d' % (f[:68], n))
    B.append('### ### ### **REPAIRING ONE OF ELEVEN WOULD MAKE THIS PAPER DISAGREE WITH TEN')
    B.append('### ### ### SIBLINGS AND HIDE A CORPUS-WIDE DRIFT INSIDE A LOCAL TIDY-UP.**')
    B.append('### ### **RECORDED IN THE KEYSTONE BY AN APPENDED ANNOTATION AND ROUTED TO THE')
    B.append('### ### AUTHOR AS A CORPUS-WIDE CITATION PASS.**')
    B.append('### ### **AND ONE OF THE FIVE MUST NOT BE REPAIRED EVEN BY THAT PASS:** ### the')
    B.append('### citation at line `423` sits in a ### **PROVENANCE ENTRY.** ### **A PROVENANCE')
    B.append('### ### ENTRY RECORDS WHAT A PAST VERSION SAID, AND EDITING IT FALSIFIES THE HISTORY')
    B.append('### ### IT EXISTS TO KEEP.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 0 -- THE ONE REPAIR, AND THE SEVEN THAT STAY ROUTED.')
    B.append(SUB)
    B.append('### ### **OF THE `%d` ITEMS `b388` AND `b389` ROUTED, EXACTLY `%d` WAS REPAIRABLE'
             % (C0['routed'], C0['repairable']))
    B.append('### ### FROM EVIDENCE ALREADY PRINTED.**')
    for k in sorted(C0['classes']):
        B.append('###   %-22s %d' % (k, C0['classes'][k]))
    B.append('### ### **THE REPAIR:** ### `SPIRAL_MAP.md`\'s cross-domain row seated')
    B.append('### `SIDE-interface-split` in its federation column. ### The live check was ###')
    B.append('### **RE-RUN AND NOT RECALLED FROM `b389`** -- `SIDE-interfaces` resolves,')
    B.append('### `SIDE-interface-split` does not -- and the name is now ### **OUT OF THE COLUMN')
    B.append('### ### AND KEPT IN THE ROW`S OWN NOTE**, with the reason and the date.')
    B.append('### ### ### **`(R4)`: PRESERVE BY QUOTATION, REPAIR BY EDIT.**')
    B.append('### ### **DIFF AGAINST THE PRE-ACT BLOB : `+%d` / `-%d`; `%d` LINE DIFFERS.**'
             % (R['added'], R['deleted'], R.get('lines_differing', 1)))
    B.append('### ### **AND A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE.** ### Three of the')
    B.append('### ### seven need the author, one needs a platform that did not answer, one needs a')
    B.append('### ### reading nobody has done, one is not a defect at all, and one `b389` had')
    B.append('### ### already answered.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 3 -- WHAT WAS WRITTEN INTO THE KEYSTONE.')
    B.append(SUB)
    B.append('### ### **AN APPENDED ANNOTATION AND NOTHING ELSE.** ### The document set that')
    B.append('### precedent ### **TWICE ON `2026-08-12`** ### in its own headings, and its era')
    B.append('### annotation closes ### *Nothing in §§I–IV is rewritten.* ### **THIS ACT KEPT THE')
    B.append('### ### DOCUMENT`S OWN RULE RATHER THAN IMPOSING ONE.**')
    B.append('### ### **BYTES `%d` -> `%d`; DIFF `+%d` / `-%d`.**'
             % (A3['before'], A3['after'], A3['added'], A3['deleted']))
    B.append('### ### **`§§I–IV` BYTE-IDENTICAL TO THE PRE-ACT BLOB : %s.**'
             % A3['sections_intact'])
    B.append('### ### **REPAIRS MADE : `%d`. ### REPAIRS ROUTED : `%d`. ### KEPT APART**, because'
             % (A3['repairs_made'], A3['repairs_routed']))
    B.append('### ### a repair and a routing are different outcomes and adding them describes')
    B.append('### ### neither.')
    B.append('### ### **`0` GRADES MOVED. ### `0` CLASSES CHANGED. ### `0` CLAIMS WITHDRAWN. ###')
    B.append('### ### `0` LINES DELETED FROM ANY DOCUMENT.** ### Each of those is a ruling, and')
    B.append('### ### **A READING PASS DOES NOT MAKE RULINGS.**')
    B.append('### Every grade the annotation writes is a word the front door already uses --')
    B.append('### *statement-grade*, *theorem-supported* -- and ### **`0` GRADE WORDS WERE MINTED.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE PRICE.')
    B.append(SUB)
    B.append('### ### **`%.0f` MINUTES AND `1` ACT FOR `1` KEYSTONE**, measured from recorded'
             % C4['minutes'])
    B.append('### ### clocks and not estimated.')
    B.append('### The census listed ### **`16`**; this act read ### **`1`.** ### At this act`s')
    B.append('### rate the remaining ### **`%d`** ### cost about ### **`%.1f` HOURS AND `%d`'
             % (C4['rest'], C4['rest_hours'], C4['rest']))
    B.append('### ### ACTS.**')
    B.append('### ### ### **AND THE FIGURE IS AN UNDERESTIMATE. ### THE ACT NAMES BOTH REASONS')
    B.append('### ### ### RATHER THAN PICKING A MULTIPLIER IT CANNOT DEFEND:**')
    B.append('###   (1) this keystone ### **HAD ALREADY BEEN RECONCILED ONCE**, on `2026-08-12`,')
    B.append('###   which is why ten of twelve anchors were already in it;')
    B.append('###   (2) ### **EVERY PIN IT CITES RESOLVES**, while the other keystone the census')
    B.append('###   named ### **CANNOT BE READ AT THE CANONICAL DRIVE AT ALL.**')
    B.append('### ### **ONE SAMPLE IS ONE SAMPLE.** ### It is ### **NOT A FORECAST**, and this act')
    B.append('### ### does not know by how much it is low. ### **NO SCHEDULE IS PROPOSED AND NO')
    B.append('### ### NEXT KEYSTONE IS CHOSEN.**')
    B.append('')
    B.append(SUB)
    B.append('### THE THREE RULINGS AWAITING THE AUTHOR, RESTATED AND NOT ANSWERED.')
    B.append(SUB)
    B.append('### ### **(1) THE CITATION QUESTION** ### -- what a finished keystone is cited as.')
    B.append('### This act`s finding ### **SHARPENS IT WITHOUT ANSWERING IT:** ### the corpus')
    B.append('### cites keystones by title and version, and ### **`%d` OF THOSE VERSIONS NAME A'
             % C2['version_total'])
    B.append('### ### DOCUMENT THAT DOES NOT EXIST.**')
    B.append('### ### **(2) THE FIVE CLUSTERS` RESHAPING**, named here from `b388`\'s own record')
    B.append('### ### with what changed in each, so the author can rule:')
    for n, v, k, d in CLUSTERS:
        B.append('###   %-26s ### **%s** ### by `%d`  -- %s' % (n, v, k, d[:62]))
    B.append('### `b388` reported the shapes and reshaped none. ### **THE RESHAPING IS THE')
    B.append('### ### AUTHOR`S.**')
    B.append('### ### **(3) A WRITTEN DEPOSIT RULE**, which `b389` proved the corpus does not')
    B.append('### ### have, by a search proved by name and by content.')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **THE NAVIGATOR`S:**')
    B.append('###   `(F1)` the keystone carries at least one claim the record has since corrected')
    B.append('###   ### **-- MET**, by the `v1.2` citation. ### **AND THE FACE DECLARED BEFORE THE')
    B.append('###   ### LOCK THAT THE PRE-LOCK SURVEY HAD FOUND NONE**, so the finding is a')
    B.append('###   ### reading result and not a foregone conclusion.')
    B.append('###   `(F2)` most of what bears on it and is not in it is addition rather than')
    B.append('###   correction ### **-- MET**: of the `%d` anchors it does not carry, ### **`%d`'
             % (C2['buckets']['DOES NOT CARRY IT'], C2['buckets']['DOES NOT CARRY IT']))
    B.append('###   ### ARE ADDITIONS AND `0` ARE CORRECTIONS.**')
    B.append('### ### **THIS SEAT`S:**')
    B.append('###   `(E1)` the pass will produce more routed items than repairs ### **-- MET**:')
    B.append('###   `%d` repaired against `%d` routed.' % (A3['repairs_made'], A3['repairs_routed']))
    B.append('###   `(E2)` the one repair of real consequence will be the map row and not the')
    B.append('###   keystone ### **-- MET.** ### The keystone was reconciled on `2026-08-12`; the')
    B.append('###   map row was written from a misreading twenty-eight days later. ### **THE')
    B.append('###   ### NEWER ARTEFACT WAS THE WRONGER ONE.**')
    B.append('###   `(E3)` the price will be an underestimate ### **-- STATED, NOT DECIDED.** ###')
    B.append('###   The act names both reasons the sample is unrepresentative and ### **SAYS IT')
    B.append('###   ### CANNOT SAY BY HOW MUCH**, which is what it registered it would do.')
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
    B.append('### gate run as `b390`: ### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### DIGEST.**')
    regtxt = io.open(os.path.join(D, 'b390_registration_2026-09-09.txt'),
                     encoding='utf-8', errors='replace').read()
    ms = re.search(r'([0-9a-f]{64})', regtxt)
    mt = re.search(r'### locked at \(UTC\) : (\S+)', regtxt)
    B.append('### **THE FACE:** ### `%d` bytes on disk, sha256 `%s`, locked at `%s`.'
             % (len(regtxt.encode('utf-8')), ms.group(1) if ms else '?',
                mt.group(1) if mt else '?'))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint.' % (E['reads'], E['without_anchor'], E['anchors_differing']))
    for n in ('b390_reads', 'b390_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY ADDED.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A GRADE WAS MOVED.', '### A CLASS WAS RULED.',
                '### A CLAIM WAS WITHDRAWN.', '### THE KEYSTONE WAS REWRITTEN.',
                '### A REPAIR WAS MADE TO SATISFY AN EXPECTATION.',
                '### A RULING WAS TREATED AS A REPAIR.',
                '### THE SUBJECT WAS CHOSEN BY PREFERENCE.',
                '### SOMETHING WAS WRITTEN AT ZENODO.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; map repair %s ; keystone annotated %s ; trail %s ; row %s ; '
        'key %s' % (Q['items'], Q['closed'], R['ok'], A3['ok'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b390_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, R=R, A3=A3, C4=C4,
             bank='b390_the_proofreading_pass.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b390_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
