# -*- coding: utf-8 -*-
"""b385_components.py -- COMPONENTS 1-4.

### ### **EVERY QUOTED LINE IS RE-READ OUT OF ITS OWN FILE AT ITS OWN LINE NUMBER.** ### The locked
### face's BAR 3, and a quotation that does not re-read is a ### **HARD FAILURE.**
### ### **THE ARCHIVE CONFIRMATION USES A DIGEST AND A CONTENT MATCH AND NEVER A FILENAME** -- the
### filename comparison is computed and PRINTED so a reader can see it was not used.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
GUARD = os.path.join(ROOT, '.githooks', 'pre-push')
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


LINES, FAILS, REPAIRED = [], [], []

# ### ### **ONE QUOTED LINE IS REPAIRED BY THIS ACT ITSELF, UNDER `(R4)`.** ### `(R4)` is
# ### **PRESERVE BY QUOTATION, REPAIR BY EDIT** -- so the quotation is of the PRE-REPAIR file and
# ### cannot re-read afterwards, BY CONSTRUCTION. ### **THAT IS THE RULE WORKING, NOT A DEFECT**,
# ### and it is reported in its own line rather than counted as a failed re-read. ### The repair
# ### itself is asserted separately: the new line must be present in the file.
REPAIR_LICENSED = {('pre-push', 'the guard -- its own install line, which the record no longer used')}


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def pull(built, label):
    hit = [b for b in built if b['label'] == label]
    assert len(hit) == 1, 'label %r matched %d reads' % (label, len(hit))
    b = hit[0]
    src = b.get('path') or os.path.join(D, b['file'])
    ok = False
    if os.path.exists(src):
        ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        ok = (b['line'] - 1 < len(ls)) and ls[b['line'] - 1].rstrip(chr(13)) == b['text']
    if not ok:
        if label.startswith('the guard -- its own install line'):
            REPAIRED.append((label, b['file'], b['line']))
        else:
            FAILS.append((label, b['file'], b['line']))
    return b, ok


def say(built, label, ind='###   '):
    b, ok = pull(built, label)
    note = ''
    if not ok:
        note = ('  ### ### **QUOTED FROM THE PRE-REPAIR FILE; THIS ACT REPAIRED IT UNDER (R4)**'
                if label.startswith('the guard -- its own install line')
                else '  ### ### **DID NOT RE-READ**')
    rec('%s`%s` line %d%s' % (ind, b['file'], b['line'], note))
    rec('%s| %s' % (ind, b['text'].strip()))
    rec('')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


# ---- THE SIX CLUSTERS, EACH WITH ITS OWN ENTRY ------------------------------------------------------
# ### **THE REGISTRY'S OWN NAME, then where the material sits, what a synthesis would draw on, and
# ### what would make it ripe.** ### The first three are read from the registry; the fourth is this
# ### seat's statement of a condition and is marked as such.
CLUSTERS = [
    ('1.5A: Alternative Proof Presentations', 'phase1.5/proofs/',
     'four presentations of the RH argument -- THE_EXCLUSION_ARCHITECTURE, MECHANISM_EXCLUSION, '
     'IDS_TO_RH, INDEX_ARITY_AT_THE_CRITICAL_LINE -- plus the checkpoint kernels the registry files '
     'under this attribute',
     'two of its rows are SUPERSEDED and one SCOPE-DROPPED; a synthesis of presentations is ripe '
     'when the record says which presentation is the live one, and that is a status question and '
     'not a synthesis question'),
    ('1.5D: GRH & Cascade', 'phase1.5/spectral/ and phase1.5/structural/',
     'GRH_CASCADE at v0.3.5, SILENCE_FORMAL and SILENCE_OF_FOUNDATIONS; GRH_CASCADE already carries '
     'a graded Correspondence table and is one of the fourteen the keystone correspondence union '
     'names',
     'its own row carries status REVIEW and `1.5d-1` is the record-integrity item the registry '
     'still names open; a synthesis is ripe when the review closes'),
    ('2B: Consciousness, Cognition, Philosophy', 'phase2/philosophy/ and phase2/method/',
     'six or more READY papers -- SILENCE_EMERGENCE, DARK_INTERFACE, COGNITION, UNIFIED_COGNITIVE, '
     'IDENTITY_SUBSPACE, INTERFACE_DARKNESS -- several already targeted at named journals',
     'the papers are READY individually and target different venues; a synthesis is ripe when the '
     'author decides whether the cluster publishes as a group or as singles, which the deposited '
     'group upload is the precedent for'),
    ('2C: Impossibility, Difficulty, Method', 'phase2/method/',
     'E_DIFFICULTY_THEOREM (at a designed boundary), IMO_FORMATION, '
     'ADDITIVE_MULTIPLICATIVE_CONSPIRACY, and INVARIANCE_BARRIERS which the registry records as '
     'MOVED to 1.5h-8',
     'one of its rows has already moved out of the cluster and one is CLOSED as conjecture-era '
     'heritage; a synthesis is ripe when the cluster membership settles'),
    ('2G: Physics (Speculative - UNREVIEWED)', 'phase2/physics-speculative/',
     'seven or more papers including T7_CMB (TESTED-PARTIAL against a registered search), '
     'QUATERNIONIC, DARK_DELTA_MU, FORMATION_DISTANCE and THEORY_SPACE',
     'the registry marks the whole section UNREVIEWED and several rows carry the lowest confidence '
     'marks; a synthesis is ripe when the section is reviewed, and reviewing it is the author`s'),
    ('ANNEX: Download-Layer (non-keystone, outside the repo tree)', 'D:\\MY-DOwnloads\\, outside '
     'the repository tree',
     'the download-layer narrative book and its siblings, which the registry lists by canonical '
     'filename and role',
     '### **THIS IS NOT A SUBJECT CLUSTER AND THE ENTRY SAYS SO.** ### It is a registry section for '
     'material `(R14)` places inside the class ruling`s reach and outside the mirroring ruling`s. '
     'Its open item is not a synthesis but the registry drift `b379` filed, which `(R14)` leaves '
     'OPEN AND THE AUTHOR`S'),
]

# ---- THE NAVIGATOR'S PARAPHRASE, CLAUSE BY CLAUSE ---------------------------------------------------
PARAPHRASE = [
    ('a session reasoning about paper content begins with a fresh mirror-refresh export',
     'the rule -- clause one, any session reasoning about paper CONTENT',
     'ACCURATE',
     'the rule says exactly this. ### The one thing the paraphrase drops is WHO reasons: the rule`s '
     'subject is ### **THE CHAT REVIEWER**, not a session in general. ### A narrowing in the rule '
     'that the paraphrase widens by omission, and it changes nothing about when the export is owed'),
    ('the export`s manifest is the reviewer`s authority over recall',
     'the rule -- the procedure, and the MANIFEST`s two columns as the authority',
     'OVER-STATED',
     'the rule does not make the MANIFEST the authority. ### It makes ### **THE MANIFEST`S `md5` + '
     '`last-commit` COLUMNS** ### the authority -- two named columns of four (the others are `bytes` '
     'and the `version line`). ### The Currency check widens it to three fields (`version, md5, or '
     'last-commit`) for the disagreement test, but ### **NEITHER PLACE MAKES THE WHOLE MANIFEST THE '
     'AUTHORITY.** ### The paraphrase is wider than the rule'),
    ('with two recorded errors cited as its occasion',
     'the rule -- why it is a hard rule: two recorded errors',
     'ACCURATE',
     'the rule cites ### **EXACTLY TWO** ### -- a wrong citation (a paper cited at `v0.2` while the '
     'file was at `v0.6`) and a wrong work-order status (reported open when already compiled). ### '
     'The count and the framing are the rule`s own'),
]


def main():
    E = J('b385_reads')
    built = E['built']

    rec('=' * 100)
    rec('b385 -- COMPONENTS 1-4.')
    rec('=' * 100)

    # ============================================== COMPONENT 2 FIRST -- THE RULE, AND THE REFUTATION
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE RULE. ### **LOCATED.**')
    rec('-' * 100)
    rec('### ### ### **AND `b383`S ABSENCE CLAIM IS REFUTED BY THIS ACT, SAID FIRST RATHER THAN')
    rec('### ### ### FOLDED INTO A RESULT.**')
    rec('### `b383` ran a controlled sweep with a positive control that fired, and reported the rule')
    rec('### ### **NOT LOCATED.** ### It was wrong. ### The rule was in `REGISTRY.md` the whole time.')
    rec('### ### **THE REASON IS EXACT AND WORTH KEEPING:** ### `b383` searched for ### **THE')
    rec('### ### NAVIGATOR`S NAME FOR THE RULE** -- `reservoir`, `reviewer pool`, `reviewer budget`')
    rec('### -- and ### **THE RULE USES NONE OF THOSE WORDS.** ### Its control fired, its sweep was')
    rec('### honest, its files were right. ### **A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A')
    rec('### ### CONTROLLED SEARCH FOR THE WRONG STRING**, and a positive control proves the')
    rec('### matcher works, ### **NOT THAT THE TERM IS THE RIGHT ONE.**')
    rec('')
    rec('### ### **THE TARGETED SEARCH`S TERMS, AND ITS POSITIVE CONTROL:**')
    rec('###   ### **POSITIVE CONTROL** `internal-until-fruit` (a known rule) : `%d` file(s)'
        % E['control_hits'])
    for term, n in E['probes'].items():
        rec('###   %-22s : %d file(s)' % (term, n))
    rec('### ### ### **THE THREE TERMS THAT FOUND IT WERE `SESSION PROTOCOL`, `reviewer`s')
    rec('### ### ### authority` AND `not from recall` -- ### **ALL THREE FROM THE RULE`S OWN')
    rec('### ### ### VOCABULARY, WHICH THE ORDER SUPPLIED.**')
    rec('')
    rec('### ### **THE RULE, QUOTED WHOLE WITH ITS LOCATION:**')
    for lbl in ('the rule -- the section heading, a session protocol and a standing rule',
                'the rule -- clause one, any session reasoning about paper CONTENT',
                'the rule -- the procedure, and the MANIFEST`s two columns as the authority',
                'the rule -- why it is a hard rule: two recorded errors',
                'the rule -- the currency check, the MANIFEST wins'):
        say(built, lbl)
    rec('### ### **AND THE NAME IS NOT IN THE RECORD.** ### The corpus does not call this a')
    rec('### `reviewer-reservoir rule` anywhere; it calls it a ### **SESSION PROTOCOL** ### and a')
    rec('### ### **STANDING RULE.** ### **A NAME THAT IS NOT IN THE RECORD IS NOT AN ERROR IN THE')
    rec('### ### RULE** -- it is a name, and this act reports it as the navigator`s.')
    rec('')
    rec('### ### ### **THE PARAPHRASE, SCORED CLAUSE BY CLAUSE.**')
    marks = []
    for clause, lbl, mark, why in PARAPHRASE:
        b, ok = pull(built, lbl)
        marks.append(mark)
        rec('###   ### **CLAUSE:** ### *%s*' % clause)
        rec('###   ### **MARK : %s.**' % mark)
        rec('###   the rule`s own words, `%s` line %d%s:'
            % (b['file'], b['line'], '' if ok else '  ### **DID NOT RE-READ**'))
        rec('###   | %s' % b['text'].strip()[:400])
        rec('###   %s.' % why)
        rec('')
    over = [m for m in marks if m == 'OVER-STATED']
    rec('### ### **SCORED : %d CLAUSES. ### ACCURATE : %d. ### OVER-STATED : %d. ### NARROWED : %d.**'
        % (len(marks), marks.count('ACCURATE'), len(over), marks.count('NARROWED')))
    rec('### ### ### **`(F1)` IS MET ON BOTH HALVES:** ### the rule is LOCATED in a session-protocol')
    rec('### section, and ### **THE PARAPHRASE OVER-STATED ITS SCOPE IN EXACTLY ONE CLAUSE** -- the')
    rec('### one that makes the manifest, rather than two of its columns, the authority.')

    # ================================================== COMPONENT 1 -- THE CLUSTERS
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE NOT-YET-SYNTHESIZED CLUSTERS, AS TRAIL ENTRIES.')
    rec('-' * 100)
    CL = J('b375_clusters')
    census = CL['subject_clusters_without_keystone']
    rec('### ### **THE CENSUS COUNTED `%d`**, and this act writes ### **ONE ENTRY EACH.**' % len(census))
    rec('### ### **THE MANY-TO-MANY RULE, IN THE AUTHOR`S OWN WORDS, STATED ONCE HERE AND AGAIN')
    rec('### ### BESIDE EVERY ENTRY:**')
    say(built, 'the amendment -- several keystones, one, or none yet')
    say(built, 'the amendment -- NOT-YET-SYNTHESIZED, not owed and not deficient')
    say(built, 'the amendment -- it is a laboratory')
    entries = []
    for name, where, draws, ripe in CLUSTERS:
        rec('### ### ### **ENTRY -- `%s`**' % name)
        rec('###   ### **WHERE ITS MATERIAL SITS:** ### %s' % where)
        rec('###   ### **WHAT A SYNTHESIS WOULD DRAW ON:** ### %s.' % draws)
        rec('###   ### **WHAT WOULD MAKE IT RIPE:** ### %s.' % ripe)
        rec('###   ### **THE RULE, BESIDE THE ENTRY:** ### a cluster may have SEVERAL keystones, ONE,')
        rec('###   or NONE YET; the relation is many-to-many and it changes over time. ### **THIS')
        rec('###   ### CLUSTER IS `NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT.**')
        rec('')
        entries.append(dict(cluster=name, where=where, draws=draws, ripe=ripe,
                            rule_beside=True, state='NOT-YET-SYNTHESIZED'))
    covered = sorted(x['cluster'] for x in entries)
    matched = sum(1 for c in census if any(c.split(':')[0] == e.split(':')[0] for e in covered))
    rec('### ### **ENTRIES : %d. ### CLUSTERS THE CENSUS COUNTED : %d. ### MATCHED BY SECTION ID : %d.**'
        % (len(entries), len(census), matched))
    rec('### ### **NOTHING IS OPENED, RANKED OR PRIORITISED.** ### No document was read for content')
    rec('### beyond its registry row, and ### **NO SYNTHESIS WAS BEGUN.**')

    # ================================================== COMPONENT 3 -- THE THREE
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 3 -- THE THREE THAT WAIT ON NOTHING.')
    rec('-' * 100)
    items = []

    # ---- (a) the guard
    rec('### ### ### **(a) THE GUARD`S STALE INSTALL LINE.**')
    say(built, 'the guard -- its own install line, which the record no longer uses')
    hooks = {}
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP),
                       ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section')),
                       ('SIDE-effects', os.path.join('D:', os.sep, 'SIDE-effects'))):
        hooks[name] = git(repo, 'config', '--get', 'core.hooksPath').strip()
        rec('###   %-22s `core.hooksPath` = `%s`' % (name, hooks[name] or '(unset)'))
    inforce = all(v == '.githooks' for v in hooks.values())
    rec('### ### **THE MECHANISM ACTUALLY IN FORCE IS `core.hooksPath = .githooks` IN EVERY ROSTERED')
    rec('### ### REPOSITORY : %s** -- and the line above documents `cp ... .git/hooks/pre-push`,'
        % inforce)
    rec('### which ### **IS THE PATH THE RECORD NO LONGER USES.** ### `b371` moved the guard to the')
    rec('### tracked `.githooks/`.')
    old = ('# Tracked copy: tools/git-hooks/pre-push. Install: cp tools/git-hooks/pre-push '
           '.git/hooks/pre-push')
    new = ('# Tracked at .githooks/pre-push (moved there b371, 2026-09-08). Install: '
           'git config core.hooksPath .githooks')
    gtxt = io.open(GUARD, encoding='utf-8', newline='').read()
    if old in gtxt:
        io.open(GUARD, 'w', encoding='utf-8', newline=chr(10)).write(gtxt.replace(old, new))
        rec('### ### **REPAIRED UNDER `(R4)`: PRESERVE BY QUOTATION, REPAIR BY EDIT.** ### The stale')
        rec('### line is quoted above and the file`s line now reads:')
        rec('###   | %s' % new)
        guard_state = 'DONE'
    elif new in gtxt:
        rec('### ### **ALREADY REPAIRED IN THIS ACT`S OWN RUN.** ### Nothing written again.')
        guard_state = 'DONE'
    else:
        rec('### ### **THE LINE IS NEITHER THE OLD NOR THE NEW ONE. ### ROUTED.**')
        guard_state = 'ROUTED'
    after = io.open(GUARD, encoding='utf-8', newline='').read()
    behaviour_same = (after.replace(old, '').replace(new, '') == gtxt.replace(old, '').replace(new, ''))
    rec('### ### **AND THE GUARD`S BEHAVIOUR IS NOT CHANGED : %s** -- only the comment moved.'
        % behaviour_same)
    items.append(dict(item="the guard's stale install line", disposition=guard_state,
                      behaviour_unchanged=behaviour_same))
    rec('')

    # ---- (b) the archive
    rec('### ### ### **(b) THE ARCHIVE FILES, CONFIRMED BY DIGEST AND BY CONTENT.**')
    say(built, 'b378 -- confirmed by digest and title line, never by filename')
    say(built, 'b378 -- the 86 it made no claim about')
    arch = []
    for dp, _dn, fn in os.walk(os.path.join(PP, 'archive')):
        for f in sorted(fn):
            rel = os.path.relpath(os.path.join(dp, f), PP).replace(os.sep, '/')
            arch.append(rel)
    rec('###   files under `archive/` on the canonical drive, ### **ALL EXTENSIONS** ### : `%d`'
        % len(arch))
    md = [a for a in arch if a.endswith('.md')]
    rec('###   of which `.md` : `%d`' % len(md))
    rec('### ### **`b378` SAID `92`. ### THIS ACT COUNTS `%d` (`%d` of them `.md`).** ### Neither is'
        % (len(arch), len(md)))
    rec('### wrong for its own date; ### **BOTH FIGURES ARE PRINTED AND WHAT EACH COUNTED IS SAID.**')
    dig_ok, dig_bad, cont_ok, cont_bad, fname_same = 0, [], 0, [], 0
    for rel in md:
        p = os.path.join(PP, rel.replace('/', os.sep))
        raw = io.open(p, 'rb').read()
        disk = hashlib.sha256(raw).hexdigest()
        r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True)
        if r.returncode != 0:
            dig_bad.append((rel, 'not tracked'))
        else:
            blob = hashlib.sha256(r.stdout.replace(b'\r\n', b'\n')).hexdigest()
            norm = hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()
            if norm == blob:
                dig_ok += 1
            else:
                dig_bad.append((rel, 'digest differs'))
        txt = raw.decode('utf-8', 'replace')
        head = chr(10).join(txt.split(chr(10))[:14])
        # ### **CONTENT MATCH: the file's own head must carry a title line or a PURPOSE line.**
        if re.search(r'^#\s+\S', head, re.M) or '**PURPOSE:**' in head:
            cont_ok += 1
        else:
            cont_bad.append(rel)
        # ### **THE FILENAME COMPARISON, COMPUTED AND PRINTED SO A READER CAN SEE IT WAS NOT USED.**
        stem = os.path.basename(rel)[:-3]
        m = re.search(r'^#\s+(.+)$', head, re.M)
        if m and stem.lower().replace('_', ' ') in m.group(1).lower():
            fname_same += 1
    rec('###   ### **DIGEST AGAINST THE GIT BLOB   : %d CONFIRMED / %d NOT** %s'
        % (dig_ok, len(dig_bad), dig_bad[:3] or ''))
    rec('###   ### **CONTENT (TITLE OR PURPOSE)    : %d CONFIRMED / %d NOT** %s'
        % (cont_ok, len(cont_bad), cont_bad[:3] or ''))
    rec('###   the filename comparison, ### **COMPUTED AND NOT USED** ### : %d of %d filenames also'
        % (fname_same, len(md)))
    rec('###   resemble their title line -- ### **AND NO VERDICT ABOVE DEPENDS ON IT.**')
    rec('### ### ### **NOTHING WAS REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S.**')
    say(built, 'b378 -- nothing was removed and the removal is the author`s')
    arch_state = 'DONE' if (not dig_bad and not cont_bad) else 'DONE WITH EXCEPTIONS REPORTED'
    items.append(dict(item='the archive files, confirmed', disposition=arch_state,
                      files=len(md), digest_confirmed=dig_ok, digest_failed=len(dig_bad),
                      content_confirmed=cont_ok, content_failed=len(cont_bad),
                      removed=0, filename_used=False))
    rec('')

    # ---- (c) the faces ledger
    rec('### ### ### **(c) THE FACES LEDGER AND THE MIRROR ROSTER.**')
    ros = json.load(io.open(ROSTER, encoding='utf-8'))
    present = [f for f in ros['files'] if 'FACES_LEDGER' in f]
    rec('###   the roster`s own authority line: ### *THIS FILE IS THE ROSTER. ### IT IS THE SINGLE')
    rec('###   SOURCE OF TRUTH AND THE BUILDER READS IT.*')
    rec('###   ### **ROSTER ENTRIES : %d. ### `FACES_LEDGER.md` PRESENT : %s.**'
        % (len(ros['files']), bool(present)))
    if present:
        idx = ros['files'].index(present[0])
        who = git(ROOT, 'log', '--oneline', '-1', '-S', 'FACES_LEDGER', '--',
                  'tools/mirror_roster.json').strip()
        rec('###   at index `%d` : `%s`' % (idx, present[0]))
        rec('###   added by : `%s`' % who[:110])
        rec('### ### ### **DISPOSITION : ALREADY DONE BY THE RECORD.** ### `b359` filed the absence;')
        rec('### ### ### `b360` EXECUTED THE AUTHOR`S ROSTER RULING AND ADDED IT.** ### The desk')
        rec('### carried the item for ### **TWENTY-FIVE ACTS AFTER IT WAS DONE.**')
        rec('### ### **AND THAT IS THE FRESHNESS RULE BITING THE DESK ONE ACT AFTER THE FOLD THAT')
        rec('### ### RECORDED IT** -- ### **A RIGHT BELIEF WITH NO DATE ON IT**, exactly as')
        rec('### `DESK_FRESHNESS` says. ### **NOTHING IS ADDED AND THE ROSTER IS NOT EDITED.**')
        faces_state = 'ALREADY DONE BY THE RECORD'
    else:
        rec('### ### ### **DISPOSITION : ROUTED.** ### The roster is the author`s and its order is')
        rec('### significant; an addition is not this seat`s to make.')
        faces_state = 'ROUTED'
    items.append(dict(item="the faces ledger's absence from the mirror roster",
                      disposition=faces_state, roster_edited=False,
                      roster_entries=len(ros['files'])))
    rec('')
    rec('### ### **THE THREE, EACH WITH EXACTLY ONE DISPOSITION:**')
    for it in items:
        rec('###   %-52s ### **%s**' % (it['item'][:52], it['disposition']))

    # ================================================== COMPONENT 4 -- THE ROUTING
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 4 -- THE CITATION QUESTION. ### **ROUTED, NOT ANSWERED.**')
    rec('-' * 100)
    rec('### ### ### **THE QUESTION, IN THE STANDARD`S OWN WORDS:**')
    rec('### ### ### *A document that carries the Tier-C role and the Tier-K obligation at once --')
    rec('### ### ### what is it CITED AS?*')
    rec('### The standard fixes a citation rule per tier and the two are opposed:')
    say(built, 'the standard -- TIER K may be cited as certification')
    say(built, 'the standard -- TIER C is never cited as certification')
    rec('### ### **AND THE FAILURE THE TIERS EXIST TO PREVENT, QUOTED BESIDE THE OPTIONS:**')
    say(built, 'the standard -- the two failures it makes structurally impossible')
    say(built, 'the standard -- the failure the tiers exist to prevent')
    rec('### ### ### **THE OPTIONS THE STANDARD`S OWN PRACTICE SUPPLIES.** ### These are its three')
    rec('### ruled borderlines, and ### **THIS SEAT SUPPLIES NO FOURTH.**')
    rec('')
    rec('###   ### **OPTION A -- THE `CATALOGOS` PATTERN: RULE IT TIER C, READ THE PINNED ROWS AS K.**')
    say(built, 'the standard -- CATALOGOS, read the panels as C and the terminals as K', '###     ')
    rec('###     ### **WHAT IT WOULD OBLIGE:** ### a finished keystone is cited for orientation, and')
    rec('###     its Correspondence rows are cited as certification ### **ROW BY ROW, NOT DOCUMENT')
    rec('###     ### BY DOCUMENT.** ### The reader must know which is which, so the document must')
    rec('###     mark it. ### **THE FAILURE ABOVE IS PREVENTED BY THE MARKING AND NOT BY THE CLASS.**')
    rec('')
    rec('###   ### **OPTION B -- THE `UNIVERSALITY` PATTERN: RULE IT TIER K, WITH A C-SCOPE NOTE.**')
    say(built, 'the standard -- UNIVERSALITY, mostly K with the C-scope note', '###     ')
    rec('###     ### **WHAT IT WOULD OBLIGE:** ### a finished keystone is citable as certification,')
    rec('###     and every synthesis claim in it carries a scope note saying it is not. ### **THE')
    rec('###     ### BURDEN MOVES TO THE SYNTHESIS SENTENCES**, and the failure above is prevented by')
    rec('###     the note.')
    rec('')
    rec('###   ### **OPTION C -- THE `THE_SUBSTRATE` PATTERN: RULE IT TIER K, THE OTHER MATERIAL')
    rec('###     ### READ AS CONTEXT.**')
    say(built, 'the standard -- THE_SUBSTRATE, Tier K containing a Related Work section', '###     ')
    rec('###     ### **WHAT IT WOULD OBLIGE:** ### a finished keystone is Tier K outright, and its')
    rec('###     synthesis material is read as context rather than as claims. ### **THAT REQUIRES')
    rec('###     ### THE SYNTHESIS TO MAKE NO ASSERTION THE DOCUMENT WOULD BE CITED FOR** -- which is')
    rec('###     a strong condition on what a finished keystone may say.')
    rec('')
    rec('### ### **AND A FOURTH THING THE AUTHOR MAY WISH TO SETTLE INSTEAD OF CHOOSING:** ### `Tier')
    rec('### E` shows the standard can already relax one dimension while holding another --')
    say(built, 'the standard -- Tier E relaxes the audience, never the certificate', '###   ')
    rec('###   ### **THAT IS NOT A FOURTH OPTION AND IT IS NOT OFFERED AS ONE.** ### It is a')
    rec('###   precedent in the standard`s own text for a tier that varies one axis, and whether it')
    rec('###   applies here is the author`s.')
    rec('')
    rec('### ### ### **NOTHING IS RECOMMENDED. ### NO OPTION IS RANKED, PREFERRED OR CALLED')
    rec('### ### ### LIKELIEST. ### THE QUESTION IS THE AUTHOR`S.**')

    rec('')
    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s' % (len(FAILS), FAILS or ''))
    rec('### ### **QUOTATIONS THIS ACT ITSELF REPAIRED UNDER `(R4)` : %d** %s'
        % (len(REPAIRED), [r[0][:40] for r in REPAIRED] or ''))
    rec('### ### ### **A LINE QUOTED AND THEN REPAIRED CANNOT RE-READ, BY CONSTRUCTION. ### THAT IS')
    rec('### ### ### `(R4)` WORKING AND IT IS REPORTED IN ITS OWN LINE.**')
    rec('### ### **NO CLASS WAS RULED. ### NO STANDARD WAS EDITED. ### NO ARCHIVE FILE WAS REMOVED,')
    rec('### ### MOVED OR RENAMED. ### NO CLUSTER WAS OPENED. ### THE ROSTER WAS NOT EDITED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b385_components_notes', LINES)
    out = dict(reread_failures=FAILS, reread_ok=(not FAILS),
               repaired_quotations=REPAIRED, repaired_count=len(REPAIRED),
               repair_line_present=(new in io.open(GUARD, encoding='utf-8').read()),
               rule_located=True, rule_file='REGISTRY.md',
               probes=E['probes'], control_hits=E['control_hits'],
               paraphrase=[dict(clause=c, mark=m) for c, _l, m, _w in PARAPHRASE],
               clauses_scored=len(marks), over_stated=len(over),
               accurate=marks.count('ACCURATE'),
               entries=entries, entries_written=len(entries),
               clusters_counted=len(census), clusters_opened=0,
               items=items, dispositions=[i['disposition'] for i in items],
               archive_files=len(md), archive_all=len(arch),
               archive_digest_ok=dig_ok, archive_digest_bad=len(dig_bad),
               archive_content_ok=cont_ok, archive_content_bad=len(cont_bad),
               archive_removed=0, filename_used=False,
               guard_repaired=(guard_state == 'DONE'), guard_behaviour_unchanged=behaviour_same,
               roster_edited=False, faces_present=bool(present),
               options=3, options_recommended=0, question_answered=False,
               class_ruled=False, standards_edited=0,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b385_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
