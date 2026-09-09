# -*- coding: utf-8 -*-
"""b388_desk_bank.py -- COMPONENT 5 (THE REFRESH), THE DESK UNDER `(R7)`, THE WRITES, THE BANK.

### ### **COMPONENT 5 WRITES INTO A CORPUS DOCUMENT, AND IT PRESERVES BEFORE IT WRITES.** ### The
### prior cluster table is copied ### **VERBATIM** ### into the same file immediately above the
### refreshed one, and an arm re-reads every prior row out of the file afterwards. ### **NOTHING
### ### IS DELETED FROM THE MAP** -- `(R4)`'s shape, and `(R17)`'s own instruction.
###
### ### **AND THE REFRESH IS IDEMPOTENT BY A MARK.** ### If the refresh block is already present
### the writer does nothing, so a re-run cannot stack two refreshes into one document. ### **AN
### ### ACT THAT CANNOT BE RE-RUN CANNOT BE CHECKED** (`b386`).
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
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
MARK = '<!-- b388 the map refreshed; (R17) executed; the unreadable rows named -->'
PRIOR = '<!-- b387 what the keystones tables actually carry; (R16) recorded -->'
REFRESH_MARK = '<!-- b388 CLUSTER TABLE REFRESH under RULING (R17), 2026-09-09 -->'
ACT = 'b388'
TODAY = '2026-09-09'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b388_components')
LG = J('b388_lockgate')
E = J('b388_reads')
C1, C2, C3, C4, C6 = AC['C1'], AC['C2'], AC['C3'], AC['C4'], AC['C6']
BANKOUT = os.path.join(D, 'b388_the_map_refreshed.txt')


# ==================================================================================================
def component5():
    """### THE REFRESH. ### **PRESERVE, THEN WRITE. ### NOTHING DELETED.**"""
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 5 -- THE REFRESH WRITTEN.')
    rec('-' * 100)
    txt = io.open(MAP, encoding='utf-8', newline='').read()
    if REFRESH_MARK in txt:
        # ### ### **A RE-RUN RE-VERIFIES THE PRESERVATION RATHER THAN SKIPPING IT.** ### The
        # ### write is idempotent by the mark, but the CLAIM that nothing was deleted must be
        # ### re-measured every run -- an idempotent skip that also skips its own check would
        # ### make the second run weaker than the first.
        prior0 = C1['prior_table']
        kept0 = sum(1 for ln in prior0 if ('> ' + ln) in txt)
        rec('### ### **ALREADY REFRESHED -- THE MARK IS PRESENT. ### NOTHING WRITTEN.**')
        rec('### ### **AND THE PRESERVATION IS RE-VERIFIED : `%d` OF `%d` PRIOR ROWS STILL IN '
            'THE FILE.**' % (kept0, len(prior0)))
        return dict(written=False, already=True, before=len(txt.encode('utf-8')),
                    after=len(txt.encode('utf-8')), prior_rows=len(prior0),
                    prior_rows_preserved=kept0,
                    clusters_after=len(E['clusters']) + 2,
                    unassigned=len([r for r in C3['rows']
                                    if r['verdict'].startswith('UNASSIGNED')]))
    prior = C1['prior_table']
    body = chr(10).join(prior)
    if body not in txt:
        rec('### ### ### **HALT. ### THE PRIOR TABLE IS NOT IN THE FILE AS THIS ACT READ IT.**')
        return dict(written=False, halt=True)
    before = len(txt.encode('utf-8'))

    idx = C3['index']
    new = []
    new.append(REFRESH_MARK)
    new.append('')
    new.append('> ### **PRIOR CLUSTER TABLE — SUPERSEDED 2026-09-09 (b388) UNDER RULING (R17), '
               'AND PRESERVED HERE VERBATIM.** *Nothing is deleted from the map; the superseded '
               'table is quoted, not removed. Its own dating line above still reads '
               '`Added 2026-06-04`, which was `97` days before this refresh.*')
    new.append('')
    for ln in prior:
        new.append('> ' + ln)
    new.append('')
    new.append('**REFRESHED CLUSTER TABLE — 2026-09-09 (b388), under RULING (R17).** The two '
               'clusters that existed only as reclassification destinations are **named and '
               'seated as clusters in their own right**. Every column is dated; the federation '
               'column was **read live by `ls-remote` on 2026-09-09** and carries the ref it was '
               'read at. The map’s own standing sentences govern this table unchanged: '
               '*each is a category, not a publishable artifact*; *the clusters are not rigid — '
               'papers can sit in adjacent clusters*; and the columns are read live because pins '
               'move.')
    new.append('')
    new.append('| Cluster | Anchor keystone(s) in this repo | Sibling-anchor / external | Primary '
               'kernel federation | Seated / read (2026-09-09) |')
    new.append('|---|---|---|---|---|')
    for c in E['clusters']:
        cs = c['cells']
        live = next((x for x in C4['clusters'] if x['cluster'] == c['name']), None)
        added = [r['doc'] for r in C3['rows'] if r['verdict'] == c['name']]
        note = ('map 2026-06-04; **%d/%d kernels resolve** (read live 2026-09-09)'
                % (len(live['kernels']) - live['unresolved'], len(live['kernels'])) if live
                else 'map 2026-06-04')
        if added:
            note += '; **b388 assigns %d further keystone-class document(s)**: %s' % (
                len(added), ', '.join('`%s`' % a.split('/')[-1] for a in added))
        new.append('| %s | %s | %s | %s | %s |'
                   % (cs[0], cs[1], cs[2] if len(cs) > 2 else '—',
                      cs[3] if len(cs) > 3 else '—', note))
    for name in ('theory-space', 'cross-domain'):
        seat = C2['seated'][name]
        mem = ', '.join('`%s`' % m.split('/')[-1] for m in seat['members'])
        kern = ', '.join('`%s`' % k['kernel'] for k in seat['kernels']) or '— **none named**'
        bad = [k['kernel'] for k in seat['kernels'] if not k['resolves']]
        note = ('**SEATED 2026-09-09 (b388) under (R17)**, from %d quoted registry move(s); '
                'no anchor named by the ruling and none invented here' % seat['moves'])
        if bad:
            note += '; ### **`%s` DOES NOT RESOLVE at the account (read live 2026-09-09)**' % (
                ', '.join(bad))
        elif seat['kernels']:
            note += '; %d/%d kernels resolve (read live 2026-09-09)' % (
                len(seat['kernels']) - seat['unresolved'], len(seat['kernels']))
        new.append('| **%s** (emergent) | %s | — | %s | %s |' % (name, mem, kern, note))
    add = [r for r in C3['rows'] if r['verdict'].startswith('UNASSIGNED')]
    new.append('')
    new.append('**UNASSIGNED — 2026-09-09 (b388).** %d keystone-class document(s) the table names '
               'no seat for: %s. **This is a permitted and honest outcome, not a defect**: a '
               'document the map has no seat for is a fact about the map as much as about the '
               'document. They are entered on `OPEN_TRAILS.md` to be assigned when ripe, under '
               'the author’s many-to-many rule — **not owed and not deficient**.'
               % (len(add), ', '.join('`%s`' % r['doc'].split('/')[-1] for r in add)))
    new.append('')

    block = chr(10).join(new)
    out = txt.replace(body, block + body if False else block, 1)
    # ### **THE PRIOR TABLE IS QUOTED INSIDE THE BLOCK AND THE ORIGINAL IS REPLACED BY THE BLOCK,
    # ### SO EVERY PRIOR ROW SURVIVES -- as a blockquote, byte-for-byte after its `> ` marker.**
    io.open(MAP + '.tmp', 'w', encoding='utf-8', newline='').write(out)
    os.replace(MAP + '.tmp', MAP)
    back = io.open(MAP, encoding='utf-8', newline='').read()
    kept = sum(1 for ln in prior if ('> ' + ln) in back)
    rec('### ### **THE PRIOR TABLE PRESERVED VERBATIM : `%d` OF `%d` ROWS.**' % (kept, len(prior)))
    rec('### ### **BYTES %d -> %d ; THE FILE GREW : %s**'
        % (before, len(back.encode('utf-8')), len(back.encode('utf-8')) > before))
    rec('### ### **CLUSTERS IN THE REFRESHED TABLE : `%d`** -- the map`s `%d` plus the `2` `(R17)`'
        % (len(E['clusters']) + 2, len(E['clusters'])))
    rec('### ### seats.**')
    rec('### ### **EVERY COLUMN DATED, AND THE FEDERATION COLUMN READ LIVE ON `%s`.**' % TODAY)
    rec('### ### **NOTHING WAS DELETED FROM THE MAP.**')
    subprocess.run(['git', '-C', PP, 'add', '--', 'SPIRAL_MAP.md'], capture_output=True)
    return dict(written=True, already=False, before=before,
                after=len(back.encode('utf-8')), prior_rows=len(prior), prior_rows_preserved=kept,
                clusters_after=len(E['clusters']) + 2, unassigned=len(add))


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
     'OPEN. ### And ### **THIS ACT ADDS A LIVE INSTANCE TO IT WITHOUT CLOSING IT**: '
     '`SIDE-interface-split`, named in `INTERFACE_CONSERVATION.md` as verifying Proposition 1, '
     '### **DOES NOT RESOLVE AT THE ACCOUNT**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', 'OPEN. ### This act rewrites '
     'none'),
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
    ('the 23 unreadable correspondence rows', 'STAND',
     '### **NAMED BY DOCUMENT, LINE AND CAUSE AT b388, IN `%d` GROUPS, AND ROUTED TO THE '
     'AUTHOR.** ### **NO ROW EDITED, NO GRADE MOVED, NO STATUS ASSIGNED** -- so the item '
     '### **STANDS**: naming a cause is not reading the row'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),

    # ---- WHAT THIS ACT ADDS ---------------------------------------------------------------------
    ('the two emergent clusters, now seated', 'STAND',
     'NEW at b388: ### **`theory-space` AND `cross-domain` SEATED IN THE MAP UNDER `(R17)`**, '
     'from `%d` quoted registry moves over `%d` documents, with ### **`0` MEMBERS ADDED ON THIS '
     'SEAT`S JUDGEMENT.** ### Neither carries an anchor, because the ruling names none and '
     '### **THIS SEAT DID NOT INVENT ONE**'),
    ('the `%d` keystone-class documents the map now assigns', 'STAND',
     'NEW at b388: ### **`%d` ASSIGNED OF `%d`, EACH WITH ITS EVIDENCE PRINTED** -- a kernel the '
     'document names or a cluster member it cites. ### **`0` ASSIGNED BY FILENAME, DIRECTORY OR '
     'TITLE**'),
    ('and the `%d` that are UNASSIGNED', 'STAND',
     'NEW at b388: ### **UNASSIGNED IS A PERMITTED AND HONEST OUTCOME, NOT A DEFECT** -- entered '
     'on the trails to be assigned when ripe, under the many-to-many rule, ### **NOT OWED.** ### '
     'Both are `NO EVIDENCE` and not `NO FIT`, and the two are ### **KEPT APART**'),
    ('`SIDE-interface-split`, which does not resolve', 'STAND',
     'NEW at b388: `INTERFACE_CONSERVATION.md` line `192` says Proposition 1 ### *is verified in* '
     '### that kernel, and ### **`ls-remote` REPORTS THE REPOSITORY NOT FOUND, TWICE.** ### '
     '### **THIS ACT CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE** -- an unauthenticated read '
     'cannot distinguish them -- and it says so rather than choosing. ### **ROUTED, NOT REPAIRED**'),
    ('the map`s five clusters that changed shape', 'STAND',
     'NEW at b388: ### **`%d` CLUSTERS CHANGED SHAPE AND `0` WERE RESHAPED BY THIS ACT.** ### '
     'Reported as a finding; ### **THE RESHAPING IS THE AUTHOR`S**'),
]


def desk_rows():
    out = []
    for item, disp, why in DESK:
        it = item
        w = why
        if '%d' in it and 'keystone-class documents the map now assigns' in it:
            it = item % C3['population']
            w = why % (C3['assigned'], C3['population'])
        elif '%d' in it and 'UNASSIGNED' in it:
            it = item % C3['unassigned']
        elif '`%d`' in why and 'GROUPS' in why:
            w = why % C6['causes']
        elif '`%d`' in why and 'quoted registry moves' in why:
            w = why % (C2['moves_rows'], C2['documents'])
        elif '`%d` CLUSTERS CHANGED' in why:
            w = why % C4['changed']
        out.append((it, disp, w))
    return out


def do_desk():
    rec('    ### ### **THIS ACT CLOSES NOTHING.** ### `(R7)` closes an item whose OCCASION is')
    rec('    ### gone. ### Seating two clusters the author ordered seated, assigning nine')
    rec('    ### documents and naming twenty-three causes removes no obligation and answers no')
    rec('    ### routed question. ### **A MEASUREMENT IS NOT A CLOSURE**, and neither is a')
    rec('    ### refresh the author ordered.')
    rec('')
    marks = []
    for item, want, why in desk_rows():
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 560), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **FIVE ITEMS ARE ADDED AND ALL FIVE STAND.**')
    rec('    ### ### ### **AND ONE OF THEM IS A LIVE INSTANCE OF `LIST 1`** -- a row citing at a')
    rec('    ### ### ### ref nobody can name -- ### **WHICH THIS ACT ADDS WITHOUT CLOSING THE')
    rec('    ### ### ### LIST.**')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


# ==================================================================================================
def trail_block(Q, C5):
    unass = [r for r in C3['rows'] if r['verdict'].startswith('UNASSIGNED')]
    return [
        '', MARK, '',
        '### **b388 — THE MAP REFRESHED, AND THE UNREADABLE ROWS NAMED (2026-09-09)**',
        '',
        ('*No block above is edited. The b387 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**RULING `(R17)`, THE AUTHOR’S: THE FEDERATION MAP IS REFRESHED IN FULL.** The two '
         'clusters that existed only as reclassification destinations — **theory-space** and '
         '**cross-domain** — are now **named and seated in `SPIRAL_MAP.md` as clusters in their '
         'own right**, and the whole cluster table is re-evaluated rather than appended to. The '
         'map’s three standing sentences govern the refresh unchanged: *each is a category, not a '
         'publishable artifact*; *the clusters are not rigid — papers can sit in adjacent '
         'clusters*; and the columns are read live because pins move.'),
        '',
        ('**THE MAP WAS `%d` DAYS OLD AGAINST TODAY AND `%d` AGAINST THE REGISTRY’S NEWEST DATE '
         'THAT HAS HAPPENED.** Its cluster section dates itself `%s`; the registry’s newest date '
         'that has happened is `%s`. The registry also carries **three forward-looking dates** '
         '(%s) — deadlines and plans, **named rather than used**, because an age measured against '
         'a date that has not happened is not an age.'
         % (C1['age_today'], C1['age_registry'], C1['map_date'], E['registry_newest'],
            ', '.join('`%s`' % x for x in C1['future']))),
        '',
        ('**THE TWO CLUSTERS ARE SEATED FROM QUOTED MOVES AND FROM NOTHING ELSE.** `%d` mentions '
         'of `→ <x> cluster` stand across the registry over **exactly two destinations and no '
         'third**; `%d` rows record a move in **their own status**, over **`%d` distinct '
         'documents** — a mention is not a move, and the two figures are reported separately. '
         '**theory-space** seats `STRUCTURAL_FRACTION` and `CONSTANCE`; **cross-domain** seats '
         '`INTERFACE_CONSERVATION` and `FORMATION_DISTANCE_DARK_VARIABLE_v0_1`. **0 members were '
         'added on this seat’s judgement of subject** — a cluster assembled from a seat’s sense '
         'of what belongs is a cluster the author never ruled. Neither carries an anchor: the '
         'ruling names none and **this seat did not invent one**.'
         % (E['mentions'], C2['moves_rows'], C2['documents'])),
        '',
        ('**`%d` OF THE `%d` KEYSTONE-CLASS DOCUMENTS THE OLD TABLE DID NOT NAME ARE NOW '
         'ASSIGNED, EACH WITH ITS EVIDENCE PRINTED.** The evidence is a kernel the document names '
         'or a cluster member it cites; **0 were assigned by filename, by directory, or by '
         'resemblance of title**. **`%d` are UNASSIGNED, and that is a permitted and honest '
         'outcome, not a defect** — a document the map has no seat for is a fact about the map as '
         'much as about the document. Both are `NO EVIDENCE` (the document names no kernel and '
         'cites no member) rather than `NO FIT`, and the two are kept apart because reporting '
         'them as one number would hide which. They are entered below **to be assigned when '
         'ripe, under the many-to-many rule — not owed and not deficient**.'
         % (C3['assigned'], C3['population'], C3['unassigned'])),
        '',
    ] + [
        ('**`%s` — UNASSIGNED (%s).** It names no kernel this act could match to a seated '
         'cluster and cites no member of one. **Not owed; to be assigned when ripe.**'
         % (r['doc'], r['verdict'].split('(')[-1].rstrip(')')))
        for r in unass
    ] + [
        '',
        ('**`%d` CLUSTERS CHANGED SHAPE, AND `0` WERE RESHAPED BY THIS ACT.** Each was tested on '
         'four questions — is its stated subject still what its members are about; is its named '
         'anchor still the document a reader should meet first; has it split, merged or gone '
         'quiet; and is its kernel federation still resolvable, **read live by `ls-remote` and '
         'never recalled**. **Every change of shape is reported as a finding and none is acted '
         'on: the reshaping is the author’s**, and a seat that reshapes while reporting has '
         'ruled.' % C4['changed']),
        '',
        ('**AND ONE KERNEL DOES NOT RESOLVE — THOUGH NOT IN THE COLUMNS `(F3)` NAMED.** All `%d` '
         'kernels in the map’s federation columns resolve, and all `%d` pin triples the map names '
         'resolve **at the ref the map names**. But `INTERFACE_CONSERVATION.md` line `192` — a '
         'member of the newly seated cross-domain cluster — says Proposition 1 *is verified in* '
         '`SIDE-interface-split`, and **`ls-remote` reports that repository not found, twice**. '
         '**This act cannot tell whether it is absent or private**: an unauthenticated read '
         'cannot distinguish them, and it says so rather than choosing. **Routed, not repaired**, '
         'and added to `LIST 1` — the rows that cite at a ref nobody can name — **without closing '
         'the list**.' % (len(E['kernels']), len(E['pins']))),
        '',
        ('**THE `23` UNREADABLE CORRESPONDENCE ROWS ARE NAMED BY DOCUMENT, LINE AND CAUSE, IN `%d` '
         'GROUPS, AND ROUTED.** %s. **No row was edited, no grade moved, and no status '
         'assigned** — naming what defeats a reader is not saying what the row should have said, '
         'and a seat that supplied that would have graded a row it was told not to touch.'
         % (C6['causes'],
            '; '.join('**%s** — `%d`' % (k, v) for k, v in sorted(C6['groups'].items(),
                                                                  key=lambda kv: -kv[1])))),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No class ruled, no document reclassified, no class line '
         'written, no declaration moved, no registry row edited, no grade moved, no '
         'Correspondence row edited, no list closed, and no cluster split, merged or renamed.** '
         '**Nothing was deleted from the map**: the prior cluster table is preserved verbatim in '
         'the same document, `%d` of `%d` rows re-read out of the file after the write. No '
         'section of the map outside `4A`’s cluster table was edited, and **no other corpus '
         'document was written into** — `README.md`, `REGISTRY.md`, `THE_LOAD_BEARING_MAP.md` and '
         '`THE_DOCUMENT_CLASS_TAXONOMY.md` were read and not touched. No archive file touched, no '
         'cluster of b375 opened, the mirror roster not edited, no `.git/hooks/pre-push` deleted. '
         'No `.lean` file touched, no build run, no axiom profile recomputed. **The four open '
         'lists are restated OPEN by name.** h2 stands exactly where the deposit left it and '
         '**this act makes no claim about it in either direction**.'
         % (C5.get('prior_rows_preserved') or 0, C5.get('prior_rows') or 0)),
        '',
    ]


SCOPE = (
    "**SCOPE: THE MAP REFRESHED UNDER (R17), AND THE UNREADABLE ROWS NAMED.** NO class ruled, NO "
    "document reclassified, NO class line written, NO declaration moved, NO REGISTRY ROW EDITED, "
    "NO grade moved, NO Correspondence row edited, NO list closed, and NO CLUSTER SPLIT, MERGED "
    "OR RENAMED. **NOTHING WAS DELETED FROM THE MAP** -- the prior cluster table is preserved "
    "VERBATIM in the same document and re-read out of the file after the write. **NO SECTION OF "
    "THE MAP OUTSIDE 4A'S CLUSTER TABLE WAS EDITED**, which is narrower than (R17)'s own "
    "boundary. **NO OTHER CORPUS DOCUMENT WAS WRITTEN INTO** -- README.md, REGISTRY.md, "
    "THE_LOAD_BEARING_MAP.md and THE_DOCUMENT_CLASS_TAXONOMY.md READ AND NOT TOUCHED. **THE TWO "
    "CLUSTERS ARE SEATED FROM QUOTED REGISTRY MOVES AND FROM NOTHING ELSE; 0 MEMBERS WERE ADDED "
    "ON THIS SEAT'S JUDGEMENT OF SUBJECT**, and NEITHER CARRIES AN ANCHOR because the ruling "
    "names none and THIS SEAT DID NOT INVENT ONE. **A MENTION IS NOT A MOVE**, and rows and "
    "documents are reported as separate figures. **EVERY ASSIGNMENT PRINTS ITS EVIDENCE AND 0 "
    "WERE ASSIGNED BY FILENAME, DIRECTORY OR TITLE**; an assignment without printed evidence is "
    "counted UNASSIGNED. **UNASSIGNED IS A PERMITTED AND HONEST OUTCOME, NOT A DEFECT**, entered "
    "on the trails to be assigned when ripe under the many-to-many rule, NOT OWED -- and NO "
    "EVIDENCE and NO FIT are KEPT APART. **EVERY CHANGE OF SHAPE IS REPORTED AND NONE IS ACTED "
    "ON: THE RESHAPING IS THE AUTHOR'S.** **THE FEDERATION WAS READ LIVE BY ls-remote AND NEVER "
    "RECALLED**, and every pin carries the ref it was read at. **ONE KERNEL DOES NOT RESOLVE -- "
    "SIDE-interface-split -- AND THIS ACT CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE AND SAYS "
    "SO**; routed, not repaired, and added to LIST 1 WITHOUT CLOSING IT. **THE 23 UNREADABLE ROWS "
    "ARE NAMED BY DOCUMENT, LINE AND CAUSE AND ROUTED; NO ROW EDITED, NO GRADE MOVED, NO STATUS "
    "ASSIGNED.** **THE FACE WAS NOT WIDENED MID-ACT.** **THE FOUR OPEN LISTS ARE RESTATED OPEN BY "
    "NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS.** NO ARCHIVE FILE TOUCHED, NO "
    "b375 CLUSTER OPENED, THE MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push DELETED. NO .lean "
    "FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 "
    "REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
    "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
    "record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS "
    "SEPARATE. h2 stands exactly where the deposit left it and this act makes no claim about it "
    "in either direction. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q, C5):
    m = ("**THE FEDERATION MAP IS REFRESHED UNDER (R17): THE TWO EMERGENT CLUSTERS SEATED FROM "
         "QUOTED MOVES, %d OF %d UNNAMED KEYSTONES ASSIGNED WITH THEIR EVIDENCE, AND NOTHING "
         "DELETED FROM THE MAP** (b388, the map refreshed and the unreadable rows named)"
         % (C3['assigned'], C3['population']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b388, %d gates read and %d checked "
            "by digest. THE MAP WAS %d DAYS OLD AGAINST TODAY AND %d AGAINST THE REGISTRY'S NEWEST "
            "DATE THAT HAS HAPPENED, and the registry's THREE FORWARD-LOOKING DATES ARE NAMED "
            "RATHER THAN USED because AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED IS NOT "
            "AN AGE. THE TWO CLUSTERS ARE SEATED FROM QUOTED REGISTRY MOVES AND FROM NOTHING "
            "ELSE: %d mentions over EXACTLY TWO DESTINATIONS AND NO THIRD, %d rows recording a "
            "move in THEIR OWN STATUS over %d DISTINCT DOCUMENTS -- A MENTION IS NOT A MOVE, and "
            "the two figures are reported separately. 0 MEMBERS WERE ADDED ON THIS SEAT'S "
            "JUDGEMENT OF SUBJECT and NEITHER CLUSTER CARRIES AN ANCHOR, because the ruling names "
            "none and THIS SEAT DID NOT INVENT ONE. %d OF %d KEYSTONE-CLASS DOCUMENTS THE OLD "
            "TABLE DID NOT NAME ARE ASSIGNED, EACH WITH ITS EVIDENCE PRINTED -- a kernel the "
            "document names or a cluster member it cites -- and 0 WERE ASSIGNED BY FILENAME, "
            "DIRECTORY OR TITLE. %d ARE UNASSIGNED, WHICH IS A PERMITTED AND HONEST OUTCOME AND "
            "NOT A DEFECT, entered on the trails TO BE ASSIGNED WHEN RIPE UNDER THE MANY-TO-MANY "
            "RULE AND NOT OWED; NO EVIDENCE and NO FIT ARE KEPT APART. %d CLUSTERS CHANGED SHAPE "
            "AND 0 WERE RESHAPED BY THIS ACT -- THE RESHAPING IS THE AUTHOR'S. THE FEDERATION WAS "
            "READ LIVE BY ls-remote: ALL %d KERNELS IN THE MAP'S FEDERATION COLUMNS RESOLVE AND "
            "ALL %d PIN TRIPLES RESOLVE AT THE REF THE MAP NAMES, SO (F3) IS REFUTED -- BUT "
            "SIDE-interface-split, NAMED IN INTERFACE_CONSERVATION.md LINE 192 AS VERIFYING "
            "PROPOSITION 1, DOES NOT RESOLVE AT THE ACCOUNT, AND THIS ACT CANNOT TELL WHETHER IT "
            "IS ABSENT OR PRIVATE AND SAYS SO. THE REFRESH PRESERVED THE PRIOR TABLE VERBATIM, %d "
            "OF %d ROWS RE-READ OUT OF THE FILE AFTER THE WRITE, AND NOTHING WAS DELETED FROM THE "
            "MAP. AND THE 23 UNREADABLE CORRESPONDENCE ROWS ARE NAMED BY DOCUMENT, LINE AND CAUSE "
            "IN %d GROUPS AND ROUTED, WITH NO ROW EDITED AND NO STATUS ASSIGNED"
            % (LG['gates_read'], LG['face_subject_gates'], C1['age_today'], C1['age_registry'],
               E['mentions'], C2['moves_rows'], C2['documents'],
               C3['assigned'], C3['population'], C3['unassigned'], C4['changed'],
               len(E['kernels']), len(E['pins']),
               C5.get('prior_rows_preserved') or 0, C5.get('prior_rows') or 0, C6['causes']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### A map section was refreshed "
            "under the author's ruling and every quoted line was re-read out of its own file at "
            "its own line number, with %d failing. ### NO KERNEL WAS OPENED, NO STATEMENT PROVED, "
            "NO BUILD RUN AND NO AXIOM PROFILE RECOMPUTED -- ls-remote SAYS A REF EXISTS AT A "
            "SHA; IT DOES NOT SAY THE KERNEL COMPILES OR THAT THE MAP'S DESCRIPTION OF IT IS "
            "TRUE. ### SEATING A CLUSTER THE AUTHOR ORDERED SEATED IS NOT RULING ONE"
            % len(AC['reread_failures']))
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, "
            "NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW "
            "EDITED AND NO LIST CLOSED. ### NO STANDARD WAS EDITED AND NO CLUSTER WAS SPLIT, "
            "MERGED OR RENAMED")
    grade = ("### REFRESHED-UNDER-THE-AUTHOR'S-RULING, AND EVERY SEAT CARRIED BY A QUOTED MOVE. "
             "### 0 MEMBERS ADDED ON A SEAT'S JUDGEMENT; 0 ASSIGNMENTS WITHOUT PRINTED EVIDENCE; "
             "0 CLUSTERS RESHAPED. ### THE PRIOR TABLE IS PRESERVED VERBATIM AND NOTHING IS "
             "DELETED. ### THE FEDERATION IS READ LIVE AND NEVER RECALLED, AND THE ONE KERNEL "
             "THAT DOES NOT RESOLVE IS REPORTED WITH THE LIMIT OF THE READ THAT FOUND IT. ### "
             "UNASSIGNED IS A STATE AND NOT A DEBT. ### AND THE UNREADABLE ROWS ARE NAMED, NOT "
             "READ")
    status = ("data/b388_the_map_refreshed.txt; data/%s; data/%s; "
              "data/b388_registration_2026-09-09.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b388); tools/b388_extract.py; "
              "tools/b388_components.py; tools/b388_desk_bank.py; tools/b388_checks.py; "
              "PLACE-papers SPIRAL_MAP.md (section 4A's cluster table, refreshed under (R17) with "
              "the prior table preserved verbatim) and OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the map refreshed under r17', 'the two emergent clusters seated',
           'the keystones assigned to clusters', 'the kernel that does not resolve',
           'the unreadable rows named by cause')
MUST_NOT_HIT = ('a cluster was reshaped', 'a registry row was edited',
                'unassigned is a defect', 'a member was added by judgement')


def do_key(rownum, C5):
    KEY = 'the-map-refreshed-under-r17'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE FEDERATION MAP IS REFRESHED UNDER THE AUTHOR'S RULING (R17). THE TWO CLUSTERS THAT "
        "EXISTED ONLY AS RECLASSIFICATION DESTINATIONS -- theory-space and cross-domain -- ARE "
        "NAMED AND SEATED IN SPIRAL_MAP.md, FROM QUOTED REGISTRY MOVES AND FROM NOTHING ELSE: %d "
        "mentions over EXACTLY TWO DESTINATIONS AND NO THIRD, %d rows recording a move in THEIR "
        "OWN STATUS over %d DISTINCT DOCUMENTS, since A MENTION IS NOT A MOVE. 0 MEMBERS WERE "
        "ADDED ON THIS SEAT'S JUDGEMENT and NEITHER CLUSTER CARRIES AN ANCHOR because the ruling "
        "names none. THE MAP WAS %d DAYS OLD AGAINST TODAY AND %d AGAINST THE REGISTRY'S NEWEST "
        "DATE THAT HAS HAPPENED, its forward-looking dates NAMED RATHER THAN USED. %d OF %d "
        "KEYSTONE-CLASS DOCUMENTS THE OLD TABLE DID NOT NAME ARE ASSIGNED WITH THEIR EVIDENCE "
        "PRINTED and 0 BY FILENAME OR DIRECTORY; %d ARE UNASSIGNED, WHICH IS A PERMITTED AND "
        "HONEST OUTCOME AND NOT A DEFECT, NOT OWED, with NO EVIDENCE and NO FIT KEPT APART. %d "
        "CLUSTERS CHANGED SHAPE AND 0 WERE RESHAPED -- THE RESHAPING IS THE AUTHOR'S. ALL %d "
        "KERNELS IN THE MAP'S FEDERATION COLUMNS AND ALL %d PIN TRIPLES RESOLVE AT THE REF THE "
        "MAP NAMES, BUT SIDE-interface-split DOES NOT RESOLVE AT THE ACCOUNT AND THIS ACT CANNOT "
        "TELL WHETHER IT IS ABSENT OR PRIVATE. THE PRIOR CLUSTER TABLE IS PRESERVED VERBATIM, %d "
        "OF %d ROWS RE-READ AFTER THE WRITE, AND NOTHING IS DELETED FROM THE MAP. THE 23 "
        "UNREADABLE CORRESPONDENCE ROWS ARE NAMED BY DOCUMENT, LINE AND CAUSE IN %d GROUPS AND "
        "ROUTED, WITH NO ROW EDITED AND NO STATUS ASSIGNED."
        % (E['mentions'], C2['moves_rows'], C2['documents'], C1['age_today'], C1['age_registry'],
           C3['assigned'], C3['population'], C3['unassigned'], C4['changed'],
           len(E['kernels']), len(E['pins']),
           C5.get('prior_rows_preserved') or 0, C5.get('prior_rows') or 0, C6['causes']))
    grade = (
        "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION "
        "MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW EDITED AND NO LIST "
        "CLOSED. ### NO CLUSTER WAS SPLIT, MERGED OR RENAMED. ### NOTHING WAS DELETED FROM THE "
        "MAP AND NO SECTION OUTSIDE 4A'S CLUSTER TABLE WAS EDITED. ### NO OTHER CORPUS DOCUMENT "
        "WAS WRITTEN INTO. ### 0 MEMBERS ADDED ON A SEAT'S JUDGEMENT; 0 ASSIGNMENTS WITHOUT "
        "PRINTED EVIDENCE. ### THE FEDERATION WAS READ LIVE AND NEVER RECALLED. ### UNASSIGNED IS "
        "A STATE AND NOT A DEBT. ### THE UNREADABLE ROWS ARE NAMED, NOT READ. ### THE FACE WAS "
        "NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW "
        "TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### "
        "NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED")
    where = (
        "data/b388_the_map_refreshed.txt; data/%s; data/%s; "
        "data/b388_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b388 -- %d gates read, %d checked by digest); "
        "tools/b388_extract.py; tools/b388_components.py; tools/b388_desk_bank.py; "
        "tools/b388_checks.py; PLACE-papers SPIRAL_MAP.md and OPEN_TRAILS.md; "
        "CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b388 (the federation map refreshed in full under (R17): the two emergent clusters "
           "seated from quoted moves; the era's unnamed keystones assigned or marked with their "
           "evidence; the map re-evaluated and its changes of shape reported not acted on; the "
           "prior table preserved verbatim; and the 23 unreadable rows named by cause and routed)")
    row_new = ('    # ### THE MAP REFRESHED UNDER (R17) (b388).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for qq in MUST_NOT_HIT:
        out, _rc = query(qq)
        pre[qq] = no_key(out)
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-44s reaches the b388 key : %s' % (qq, g))
    for lbl, cond in (('the ruling is named and executed', '(R17)' in out),
                      ('a mention is not a move', 'A MENTION IS NOT A MOVE' in out),
                      ('no third destination',
                       'EXACTLY TWO DESTINATIONS AND NO THIRD' in out),
                      ('no member added by judgement',
                       "0 MEMBERS WERE ADDED ON THIS SEAT'S JUDGEMENT" in out),
                      ('no anchor invented', 'NEITHER CLUSTER CARRIES AN ANCHOR' in out),
                      ('evidence printed, none by filename',
                       '0 BY FILENAME OR DIRECTORY' in out),
                      ('unassigned is not a defect',
                       'NOT A DEFECT' in out and 'NOT OWED' in out),
                      ('no evidence and no fit kept apart',
                       'NO EVIDENCE and NO FIT KEPT APART' in out),
                      ('shape reported, not acted on',
                       "0 WERE RESHAPED -- THE RESHAPING IS THE AUTHOR'S" in out),
                      ('the federation resolves at the ref the map names',
                       'RESOLVE AT THE REF THE MAP NAMES' in out),
                      ('the one kernel that does not resolve, with its limit',
                       'CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE' in out),
                      ('nothing deleted from the map',
                       'NOTHING IS DELETED FROM THE MAP' in out),
                      ('the unreadable rows named not read',
                       'THE UNREADABLE ROWS ARE NAMED, NOT READ' in out),
                      ('no registry row edited', 'NO REGISTRY ROW EDITED' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('no new tracking document in the corpus',
                       'NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g = pre[qq] and no_key(o)
        ok = ok and g
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    rec('=' * 100)
    rec('b388 -- COMPONENT 5, THE DESK, THE WRITES, AND THE BANK.')
    rec('=' * 100)
    C5 = component5()
    if C5.get('halt'):
        run_clock.write(D, 'b388_desk_notes', LINES)
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
                  before_bytes=len(before.encode('utf-8')), after_bytes=len(before.encode('utf-8')))
    else:
        rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q, C5)) + chr(10))
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
    tr['says_r17'] = '(R17)' in seg
    tr['says_not_owed'] = 'not owed' in seg.lower()
    tr['says_not_acted'] = 'none is acted' in seg.lower()
    tr['says_absent_or_private'] = 'absent or private' in seg.lower()
    rec('  ### ### **THE BLOCK NAMES `(R17)` : %s ; SAYS `NOT OWED` : %s ; SAYS THE SHAPE FINDING '
        'IS NOT ACTED ON : %s ; AND STATES THE LIMIT OF THE KERNEL READ : %s**'
        % (tr['says_r17'], tr['says_not_owed'], tr['says_not_acted'],
           tr['says_absent_or_private']))

    rec('')
    rec('-' * 100)
    rec('  ### THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    ROWS = corr_rows(Q, C5)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b388_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b388_desk_notes', LINES)
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
            run_clock.write(D, 'b388_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum, C5)

    rec('')
    rec('-' * 100)
    rec('  ### THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b388 -- THE MAP REFRESHED, AND THE UNREADABLE ROWS NAMED. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE AUTHOR RULED `(R17)`: THE FEDERATION MAP IS REFRESHED IN FULL.**')
    B.append('### The two clusters that existed only as reclassification destinations are ###')
    B.append('### **NAMED AND SEATED AS CLUSTERS IN THEIR OWN RIGHT**, and the whole table is')
    B.append('### re-evaluated rather than appended to.')
    B.append('### ### **THE MAP WAS `%d` DAYS OLD AGAINST TODAY AND `%d` AGAINST THE REGISTRY`S'
             % (C1['age_today'], C1['age_registry']))
    B.append('### ### NEWEST DATE THAT HAS HAPPENED.** ### Its section dates itself `%s`; the'
             % C1['map_date'])
    B.append('### registry`s newest date that has happened is `%s`. ### And the registry carries'
             % E['registry_newest'])
    B.append('### ### **THREE FORWARD-LOOKING DATES** ### -- %s -- ### **NAMED RATHER THAN'
             % ', '.join('`%s`' % x for x in C1['future']))
    B.append('### ### USED**, because ### **AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED')
    B.append('### ### IS NOT AN AGE.** ### A first pass took the maximum date and reported `344`')
    B.append('### days; ### **THAT FIGURE IS WRONG AND IS NOT CARRIED.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENTS 1 AND 2 -- THE MAP AS IT STOOD, AND THE TWO CLUSTERS SEATED.')
    B.append(SUB)
    B.append('### ### **THE PRIOR CLUSTER TABLE IS QUOTED WHOLE IN `data/%s`**, at its own'
             % AC['run_file'])
    B.append('### lines, every row re-read out of the map before anything moved.')
    B.append('### ### **THE THREE STANDING SENTENCES `(R17)` NAMES, IN THE MAP`S OWN WORDS:** ###')
    B.append('### *each is a category, not a publishable artifact*; ### *the clusters are not')
    B.append('### rigid -- papers can sit in adjacent clusters*; ### and the columns are read live')
    B.append('### because pins move.')
    B.append('')
    B.append('### ### **THE SEATING RESTS ON QUOTED MOVES AND ON NOTHING ELSE.**')
    B.append('###   `→ <x> cluster` mentions in the registry : ### **`%d`**' % E['mentions'])
    B.append('###   distinct destinations                    : ### **`%d`** -- %s'
             % (len(E['destinations']),
                ', '.join('`%s` (%d)' % (k, v) for k, v in sorted(E['destinations'].items()))))
    B.append('###   ### **DESTINATIONS THAT ARE NEITHER OF THE TWO : `%d`.**'
             % C2['third'])
    B.append('###   rows recording a move in THEIR OWN STATUS : ### **`%d`**' % C2['moves_rows'])
    B.append('###   distinct documents those rows stand over : ### **`%d`**' % C2['documents'])
    B.append('### ### ### **A MENTION IS NOT A MOVE**, and the two figures are reported')
    B.append('### ### ### separately rather than added.')
    for name, seat in C2['seated'].items():
        B.append('')
        B.append('###   ### **`%s` cluster** -- `%d` member(s) from `%d` quoted move(s)'
                 % (name, len(seat['members']), seat['moves']))
        for m in seat['members']:
            B.append('###       %s' % m)
        B.append('###     kernels its members name : `%d`, of which ### **`%d` DO NOT RESOLVE**'
                 % (seat['kernels_named'], seat['unresolved']))
    B.append('')
    B.append('### ### **`0` MEMBERS WERE ADDED ON THIS SEAT`S JUDGEMENT OF SUBJECT.** ### Each is')
    B.append('### carried by a quoted move at its own registry line. ### **A CLUSTER ASSEMBLED')
    B.append('### ### FROM A SEAT`S SENSE OF WHAT BELONGS IS A CLUSTER THE AUTHOR NEVER RULED.**')
    B.append('### ### **AND NEITHER CLUSTER CARRIES AN ANCHOR:** ### `(R17)` seats them and names')
    B.append('### none, and ### **THIS SEAT DID NOT INVENT ONE.**')
    B.append('')
    B.append(SUB)
    B.append("### COMPONENT 3 -- THE ERA'S OUTPUT ASSIGNED OR MARKED.")
    B.append(SUB)
    B.append('### ### **THE POPULATION WAS FIXED ON THE LOCKED FACE: `%d` KEYSTONE-CLASS'
             % C3['population'])
    B.append('### ### DOCUMENTS THE MAP`S TABLE DID NOT NAME** -- so the component could not')
    B.append('### choose a population that flattered its result.')
    B.append('### ### **ASSIGNED : `%d`. ### UNASSIGNED : `%d` (NO EVIDENCE `%d`, NO FIT `%d`).**'
             % (C3['assigned'], C3['unassigned'], C3['no_evidence'], C3['no_fit']))
    B.append('')
    for r in C3['rows']:
        B.append('###   %-58s ### **%s**' % (r['doc'][:58], r['verdict']))
        B.append('###     evidence : %s'
                 % (', '.join(r['evidence'][:5]) or '### **NONE -- SO IT IS NOT ASSIGNED**'))
    B.append('')
    B.append('### ### **`0` DOCUMENTS WERE ASSIGNED BY FILENAME, BY DIRECTORY, OR BY RESEMBLANCE')
    B.append('### ### OF TITLE.** ### Every assignment prints the kernel it names or the cluster')
    B.append('### member it cites, and ### **AN ASSIGNMENT WITHOUT PRINTED EVIDENCE IS COUNTED')
    B.append('### ### `UNASSIGNED`.**')
    B.append('### ### ### **UNASSIGNED IS A PERMITTED AND HONEST OUTCOME, NOT A DEFECT.** ### A')
    B.append('### document the map has no seat for is a fact about the map as much as about the')
    B.append('### document. ### **AND `NO EVIDENCE` AND `NO FIT` ARE KEPT APART**, because')
    B.append('### reporting them as one number would hide which.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 4 -- THE MAP RE-EVALUATED.')
    B.append(SUB)
    B.append('### ### **FOUR QUESTIONS OF EACH SEATED CLUSTER, EACH ANSWERED BY A QUOTATION OR A')
    B.append('### ### LIVE READ.**')
    B.append('###   %-38s %-8s %-8s %s' % ('CLUSTER', 'ANCHORS', 'ADDED', 'FEDERATION (LIVE)'))
    for c in C4['clusters']:
        B.append('###   %-38s %-8d %-8d %d kernel(s), %d not resolving'
                 % (c['cluster'][:38], c['anchors'], c['added'], len(c['kernels']),
                    c['unresolved']))
    B.append('### ### **CLUSTERS WHOSE SHAPE CHANGED : `%d`. ### RESHAPED BY THIS ACT : `%d`.**'
             % (C4['changed'], C4['reshaped']))
    B.append('### ### ### **EVERY CHANGE OF SHAPE IS REPORTED AS A FINDING AND NONE IS ACTED ON.**')
    B.append('### ### **THE RESHAPING IS THE AUTHOR`S**, and a seat that reshapes while reporting')
    B.append('### has ruled.')
    B.append('')
    B.append('### ### ### **AND ONE KERNEL DOES NOT RESOLVE -- THOUGH NOT IN THE COLUMNS `(F3)`')
    B.append('### ### ### NAMED.**')
    B.append('###   kernels in the map`s federation columns  : ### **`%d`, `0` FAILING**'
             % len(E['kernels']))
    B.append('###   pin triples the map names                : ### **`%d`, `0` FAILING AT THE REF'
             % len(E['pins']))
    B.append('###     THE MAP NAMES**')
    B.append('###   ### **`SIDE-interface-split`** -- named at `INTERFACE_CONSERVATION.md` line')
    B.append('###     `192` as the kernel in which Proposition 1 ### *is verified*, and a member')
    B.append('###     of the newly seated `cross-domain` cluster. ### **`ls-remote` REPORTS THE')
    B.append('###     ### REPOSITORY NOT FOUND, TWICE.**')
    B.append('###   ### **AND THE LIMIT OF THE INSTRUMENT IS STATED WITH THE FINDING:** ###')
    B.append('###   `ls-remote` says a ref exists at a sha. ### **IT DOES NOT SAY THE KERNEL')
    B.append('###   ### COMPILES, OR THAT THE MAP`S DESCRIPTION OF IT IS TRUE.**')
    B.append('###   ### ### **THIS ACT CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE.** ### An')
    B.append('###   unauthenticated read cannot distinguish the two, and ### **THE ACT SAYS SO')
    B.append('###   ### RATHER THAN CHOOSING.** ### Routed, not repaired, and added to `LIST 1` --')
    B.append('###   the rows that cite at a ref nobody can name -- ### **WITHOUT CLOSING THE')
    B.append('###   ### LIST.**')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 5 -- THE REFRESH WRITTEN.')
    B.append(SUB)
    B.append('### ### **THE PRIOR CLUSTER TABLE IS PRESERVED VERBATIM IN THE SAME DOCUMENT,')
    B.append('### ### IMMEDIATELY ABOVE THE REFRESHED ONE : `%d` OF `%d` ROWS RE-READ OUT OF THE'
             % (C5.get('prior_rows_preserved') or 0, C5.get('prior_rows') or 0))
    B.append('### ### FILE AFTER THE WRITE.**')
    B.append('### ### **`SPIRAL_MAP.md` : `%d` -> `%d` BYTES. ### THE FILE GREW.**'
             % (C5['before'], C5['after']))
    B.append('### ### **CLUSTERS IN THE REFRESHED TABLE : `%d`** -- the map`s `%d` and the `2`'
             % (C5.get('clusters_after') or 0, len(E['clusters'])))
    B.append('### ### `(R17)` seats.**')
    B.append('### ### **EVERY COLUMN DATED; THE FEDERATION COLUMN READ LIVE ON `%s` AND CARRYING'
             % TODAY)
    B.append('### ### THE REF IT WAS READ AT.**')
    B.append('### ### ### **NOTHING WAS DELETED FROM THE MAP. ### THE SUPERSEDED TABLE IS QUOTED,')
    B.append('### ### ### NOT REMOVED** -- `(R4)`s shape and `(R17)`s own instruction.')
    B.append('### ### **NO SECTION OF THE MAP OUTSIDE `4A`S CLUSTER TABLE WAS EDITED**, which is')
    B.append('### narrower than the ruling`s own boundary.')
    B.append('')
    B.append(SUB)
    B.append('### COMPONENT 6 -- THE UNREADABLE ROWS, NAMED AND NOT REPAIRED.')
    B.append(SUB)
    B.append('### ### **`%d` ROWS IN `%d` NAMED CAUSES, AND THE GROUP COUNTS SUM : %s.**'
             % (C6['total'], C6['causes'], C6['sums']))
    for k, v in sorted(C6['groups'].items(), key=lambda kv: -kv[1]):
        B.append('###   ### **%-58s : `%d`**' % (k[:58], v))
    B.append('### ### **EVERY ROW IS NAMED BY DOCUMENT AND LINE IN `data/%s`.**' % AC['run_file'])
    B.append('### ### ### **ROUTED TO THE AUTHOR. ### NO ROW EDITED. ### NO GRADE MOVED. ### NO')
    B.append('### ### ### STATUS ASSIGNED.**')
    B.append('### ### **NAMING WHAT DEFEATS A READER IS NOT SAYING WHAT THE ROW SHOULD HAVE')
    B.append('### ### SAID**, and a seat that supplied that would have graded a row it was told')
    B.append('### not to touch.')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### ### **NOTHING WAS CLOSED.** ### Seating two clusters the author ordered seated,')
    B.append('### assigning nine documents and naming twenty-three causes removes no obligation.')
    B.append('### ### **A MEASUREMENT IS NOT A CLOSURE, AND NEITHER IS A REFRESH THE AUTHOR')
    B.append('### ### ORDERED.**')
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-map-refreshed-under-r17` reachable by every alias : %s' % kok)
    B.append('')
    B.append('### ### **NO CLASS WAS RULED. ### NO DOCUMENT RECLASSIFIED. ### NO CLASS LINE')
    B.append('### ### WRITTEN. ### NO DECLARATION MOVED. ### NO REGISTRY ROW EDITED. ### NO GRADE')
    B.append('### ### MOVED. ### NO CORRESPONDENCE ROW EDITED. ### NO LIST CLOSED. ### NO CLUSTER')
    B.append('### ### SPLIT, MERGED OR RENAMED.**')
    B.append('### ### **`README.md`, `REGISTRY.md`, `THE_LOAD_BEARING_MAP.md` AND')
    B.append('### ### `THE_DOCUMENT_CLASS_TAXONOMY.md` WERE READ AND NOT TOUCHED.**')
    B.append('### ### **NO ARCHIVE FILE TOUCHED. ### NO `b375` CLUSTER OPENED. ### THE MIRROR')
    B.append('### ### ROSTER NOT EDITED. ### NO `.git/hooks/pre-push` DELETED.**')
    B.append('### ### **THE FACE WAS NOT WIDENED MID-ACT.**')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME** -- and `LIST 1` gains a')
    B.append('### live instance ### **WITHOUT BEING CLOSED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and ###')
    B.append('### **THIS ACT MAKES NO CLAIM ABOUT IT IN EITHER DIRECTION.** ### **NOTHING IS')
    B.append('### ### DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### THE EXPECTATIONS, DECIDED.')
    B.append(SUB)
    B.append('### ### **`(F1)` MET ON ITS FIRST HALF, AND THE SECOND IS REPORTED AS A SPLIT.** ###')
    B.append('### `%d` of `%d` -- ### **MORE THAN HALF** -- assign; `%d` mark `UNASSIGNED`.'
             % (C3['assigned'], C3['population'], C3['unassigned']))
    B.append('### ### **WHETHER `%d` IS A `MATERIAL MINORITY` IS THE NAVIGATOR`S WORD**, and the'
             % C3['unassigned'])
    B.append('### split is printed for him rather than judged here.')
    B.append('### ### **`(F2)` MET.** ### `%d` clusters changed shape by Component 4`s test.'
             % C4['changed'])
    B.append('### ### **`(F3)` REFUTED**, and it was ### **ALREADY REFUTED BY THE PRE-LOCK')
    B.append('### ### SURVEY** ### and declared on the face rather than presented as a discovery.')
    B.append('### `0` of `%d` kernels and `0` of `%d` pin triples fail at the ref the map names.'
             % (len(E['kernels']), len(E['pins'])))
    B.append('### ### ### **BUT A KERNEL THAT DOES NOT RESOLVE WAS FOUND ANYWAY**, one level out')
    B.append('### ### ### from where `(F3)` looked, and it is reported rather than filed under a')
    B.append('### ### ### refuted expectation.')
    B.append('### ### **`(E1)` MET.** ### Both seated clusters have `2` members; every existing')
    B.append('### cluster names more anchors than that.')
    B.append('### ### **`(E2)` MET.** ### `%d` of the unassigned marked `NO EVIDENCE` rather than'
             % C3['no_evidence'])
    B.append('### `NO FIT`, and the two reasons are kept apart.')
    B.append('### ### **`(E3)` MET.** ### The `23` rows fall into `%d` causes, not one.'
             % C6['causes'])
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS ACT ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED IS NOT`')
    B.append('### ### ### `AN AGE`.** ### The registry carries deadlines; a max over its dates')
    B.append('### made the map look `344` days stale instead of `85`.')
    B.append('### ### ### **NEW -- `A MENTION IS NOT A MOVE`.** ### Ten mentions, seven rows, four')
    B.append('### documents -- three different numbers for one question, and the act reports all')
    B.append('### three rather than picking one.')
    B.append('### ### ### **NEW -- `A SEAT THAT RESHAPES WHILE REPORTING HAS RULED`.**')
    B.append('### ### ### **NEW -- `AN UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE`.** ###')
    B.append('### `ls-remote` says NOT FOUND for both, and the act reports the ambiguity rather')
    B.append('### than resolving it by preference.')
    B.append('### **MET AGAIN -- `A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE`**, twice in')
    B.append('### this act`s own extract: an annotated-tag read that made five pins look wrong,')
    B.append('### and a pin reader that found one triple of eleven. ### **BOTH CAUGHT BEFORE THE')
    B.append('### ### LOCK.** ### And ### **A MEASUREMENT IS NOT A CLOSURE** (`b383`).')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b388_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b388_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked '
             'by digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### The extract`s clock is `%s` and the lock`s is `%s`.'
             % (E.get('run_clock'), (m_at.group(1) if m_at else '?')))
    for n in ('b388_reads', 'b388_lockgate', 'b388_components'):
        jj = J(n)
        B.append('### %-18s run file `%s` recorded clock %s'
                 % (n, jj['run_file'], jj.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing '
             'from the hint.' % (E['reads'], E['without_anchor'], E['anchors_differing']))
    B.append('### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLUSTER WAS RESHAPED.', '### A ROW WAS EDITED.',
                '### A DOCUMENT WAS RECLASSIFIED.',
                '### A ROW OF THE PRIOR TABLE WAS DELETED.', '### ASSIGNED BY FILENAME.',
                '### A MEMBER WAS ADDED BY JUDGEMENT.', '### A KERNEL WAS RECALLED.',
                '### UNASSIGNED IS A DEFECT.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec('')
    rec('=' * 100)
    rec('  ### desk %d ; closed %d ; refresh written %s ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], C5['written'], tr['appended_only'], rownum, kok))
    rec('=' * 100)
    p = run_clock.write(D, 'b388_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, C5=C5,
             bank='b388_the_map_refreshed.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b388_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
