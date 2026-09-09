# -*- coding: utf-8 -*-
"""b383_components.py -- COMPONENTS 1-4. ### **THE STANDARD, THE RECONCILIATION, THE MODEL, THE
### AMENDMENTS.**

### ### **EVERY QUOTED LINE IS RE-READ OUT OF ITS OWN FILE AT ITS OWN LINE NUMBER BEFORE IT IS
### ### WRITTEN HERE.** ### The locked face's BAR 2, and a quotation that does not re-read is a
### ### **HARD FAILURE** ### rather than a footnote.
### ### **THE CONNECTIVE PROSE IS THIS SEAT'S. ### NO OBLIGATION AND NO CITATION RULE IS PARAPHRASED.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


LINES = []
FAILS = []


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
        FAILS.append((label, b['file'], b['line']))
    return b, ok


def say(built, label, indent='###   '):
    b, ok = pull(built, label)
    rec('%s`%s` line %d%s' % (indent, b['file'], b['line'],
                              '' if ok else '  ### ### **DID NOT RE-READ**'))
    rec('%s| %s' % (indent, b['text'].strip()))
    rec('')


def main():
    E = J('b383_reads')
    built = E['built']

    rec('=' * 100)
    rec('b383 -- COMPONENTS 1-4. ### THE STANDARD, THE RECONCILIATION, THE MODEL, THE AMENDMENTS.')
    rec('=' * 100)

    # ================================================= COMPONENT 1 -- THE STANDING STANDARD
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE STANDING STANDARD, QUOTED. ### **READ AT THE CANONICAL DRIVE.**')
    rec('-' * 100)
    rec('### ### **THE THREE SOURCES WERE READ AT `%s`**' % PP)
    rec('### -- the working tree, ### **NOT THE MIRROR ZIP AND NOT A GIT BLOB.**')
    rec('')
    rec('### ### ### **(1a) THE DOCUMENT-CLASS TAXONOMY -- THE AUTHOR-RULED STANDING STANDARD.**')
    rec('### ### **WHAT IT IS, AND THE TWO FAILURES IT WAS BUILT TO PREVENT:**')
    say(built, 'the standard -- the standing standard and the two failures it prevents')
    rec('### ### **THE FOUR TIERS, EACH WITH ITS OBLIGATION AND ITS CITATION RULE, QUOTED WHOLE:**')
    for lbl in ('the standard -- TIER K, its obligation and its citation rule',
                'the standard -- TIER C, its obligation and its citation rule',
                'the standard -- TIER N, its obligation and its citation rule',
                'the standard -- TIER E, its obligation and its citation rule'):
        say(built, lbl)
    rec('### ### **THE FAILURE IT WAS BUILT TO PREVENT, IN THE STANDARD`S OWN ACCOUNT:**')
    say(built, 'the standard -- the failure it was built to prevent')
    rec('### ### **AND THE STANDARD ALREADY NAMES ITS OWN UNFINISHED WORK:**')
    say(built, 'the standard -- per-document confirmation is the standing sweep')
    say(built, 'the standard -- the per-document tier sweep remains the standing follow-on')
    rec('### ### **THE PRESUMPTIVE CLASSIFICATION, AND THE BORDERLINES THE AUTHOR RULED:**')
    for lbl in ('the standard -- Tier K presumptive, the ~50 graded keystones',
                'the standard -- Tier C presumptive, the cluster syntheses',
                'the standard -- the CATALOGOS borderline, read the panels as C and the terminals '
                'as K',
                'the standard -- CONCLUSIONS_OF_RECORD is Tier C by pointer',
                'the standard -- THE_SUBSTRATE is Tier K containing a Related Work section'):
        say(built, lbl)

    rec('### ### ### **(1b) THE REGISTRY`S PHASE ATTRIBUTE SECTION -- THE `WHEN` AND THE `WHERE`.**')
    say(built, 'the registry -- the phase attribute section, the WHEN and the WHERE')
    say(built, 'the registry -- every row carries one of six attributes')
    rec('### ### **THE ATTRIBUTE IS WHAT MAKES A ROW FINDABLE**: `1` is the deposited line, `1.1` is')
    rec('### ### **AN EVENT AND NOT A DOCUMENT SET** ### (no row carries it, *and that is correct')
    rec('### rather than missing*), `1.2` the Riemann-paths work, `1.5` the cascade, `2` the method')
    rec('### applied elsewhere, and:')
    say(built, 'the registry -- SUPPORT covers cluster syntheses and consults')
    rec('### ### ### **THE RECONCILIATION OF THE RUBRIC`S `WHEN` WITH THE REGISTRY`S `WHERE`:** ###')
    rec('### the section`s own heading says the two ### **NOW COEXIST PERMANENTLY.** ### The rubric')
    rec('### orders documents by ### **WHEN THE WORK HAPPENED** ### (phase); the registry files them')
    rec('### by ### **WHERE THEY LIVE IN THE FILE** ### (section). ### **THE ATTRIBUTE COLUMN IS THE')
    rec('### ### JOIN**, and the `1.2` row is the proof it was needed: its documents live under')
    rec('### `1.5A` while their phase is `1.2`, and ### **THE ATTRIBUTE IS WHAT MAKES THIS FINDABLE.**')
    rec('### ### **AND THE SECTION CARRIES THE DISCIPLINE THIS SEQUENCE KEPT RE-LEARNING:**')
    say(built, 'the registry -- an absence that is ruled cannot be mistaken for an oversight')
    rec('')

    rec('### ### ### **(1c) THE KEYSTONE CORRESPONDENCE UNION -- ITS OWN LIST.**')
    say(built, 'the union -- its title names it the keystone correspondence union')
    say(built, 'the union -- its PURPOSE, which terminal backs which claim')
    say(built, 'the union -- THE KEYSTONE SET, fourteen graded Correspondence tables')
    say(built, 'the union -- the fourteen named, and the Day-1 companions')
    rec('### ### ### **SO THE CORPUS ALREADY CARRIES A NAMED, RULED LIST OF THE DOCUMENTS WHOSE')
    rec('### ### ### CORRESPONDENCE TABLES ARE GRADED: FOURTEEN OF THEM, EACH NAMED.**')

    # ============================================ COMPONENT 2 -- THE RECONCILIATION
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE SEQUENCE RECONCILED. ### **PLAINLY AND WITHOUT DEFENCE.**')
    rec('-' * 100)
    ROWS = [
        ('b375', 'what does the corpus mean by `keystone`, and how many documents are one',
         'DUPLICATED',
         'the standard fixes four tiers and names the presumptive membership of each; `keystone` is '
         'its `Tier K`, defined by a machine-checked terminal at a pin'),
        ('b376', 'do the three tests measure one thing or two -- ROLE and APPARATUS',
         'ADDS',
         'the standard states the two properties as separate TIERS; it does not state that a single '
         'test can cross them, and the crossing is a measurement the standard does not contain'),
        ('b377', 'do the documents the apparatus axis marked deficient really lack what the '
         'taxonomy requires',
         'DUPLICATED',
         'the taxonomy states the obligation the act measured against -- `grade . terminal . pin` -- '
         'and the act re-derived which element was missing'),
        ('b378', 'are the identifiers no kernel declares really absent',
         'ADDS',
         'a fact about kernels at refs, which no standard states or could state'),
        ('b379', 'was the apparatus column undercounting',
         'DUPLICATED',
         'the union already names the fourteen graded correspondence tables; the act re-measured a '
         'population the corpus had already listed'),
        ('b380', 'can role be read from what a document DRAWS ON',
         'ADDS',
         'a negative result about a method, and the standard proposes no method for reading role'),
        ('b381', 'does a control rebuilt to fail separate under co-location',
         'ADDS',
         'a second negative result about a second method, on a control the standard does not have'),
        ('b382', 'what does the evidence support about method',
         'ADDS',
         'the conclusion that a class ruling must rest on declaration -- which the standard already '
         'assumes in practice but nowhere argues'),
    ]
    rec('###   %-6s %-62s %s' % ('ACT', 'WHAT IT ASKED', 'VERDICT'))
    for act, asked, verdict, _why in ROWS:
        rec('###   %-6s %-62s ### **%s**' % (act, asked[:62], verdict))
    dup = [r for r in ROWS if r[2] == 'DUPLICATED']
    add = [r for r in ROWS if r[2] == 'ADDS']
    rec('')
    rec('### ### **DUPLICATED : %d ### / ### ADDS : %d.**' % (len(dup), len(add)))
    rec('')
    rec('### ### **WHAT THE SEQUENCE DUPLICATED.**')
    for act, _asked, _v, why in dup:
        rec('###   ### **%s** -- %s.' % (act, why))
    rec('### ### ### **THE STANDARD HAD ALREADY RULED THE CLASS QUESTION, AND THE SEQUENCE SPENT')
    rec('### ### ### THREE ACTS RE-DERIVING IT.** ### The standard names four tiers, each')
    rec('### obligation, each citation rule and the presumptive membership; the union names the')
    rec('### fourteen graded tables. ### **NEITHER WAS CITED BY ANY OF THE EIGHT ACTS.**')
    rec('')
    rec('### ### **AND THE RULE THAT NAMES THE SPECIES WAS ALREADY MINTED, BY THIS SEAT, AT `b368`:**')
    say(built, 'the freshness rule -- every desk item names its file and date')
    say(built, 'the freshness rule -- a right belief with no date on it')
    rec('### ### ### **THE SEQUENCE VIOLATED ITS OWN FRESHNESS RULE.** ### The premise it ran on --')
    rec('### that the corpus`s `keystone` was undefined and had to be measured -- was ### **A BELIEF')
    rec('### ### WITH NO DATE ON IT**, and the standard that dated it was `2026-07-28`,')
    rec('### author-ruled, and sitting in the tree the whole time.')
    rec('')
    rec('### ### **WHAT THE SEQUENCE ADDS.**')
    for act, _asked, _v, why in add:
        rec('###   ### **%s** -- %s.' % (act, why))
    rec('### ### ### **THE ADDITION IS ONE SEPARATION AND THREE RESULTS ABOUT METHOD, AND NOT A')
    rec('### ### ### DEFINITION.** ### `b376`s two-axis separation is the durable one; `b378`s')
    rec('### kernel facts are about kernels; `b380` and `b381` are ### **TWO NEGATIVE RESULTS ABOUT')
    rec('### ### TWO PREDICATES**; `b382` argues a conclusion the standard assumes.')

    # ---------------------------------------------------- THE NAVIGATOR'S READING, TESTED
    rec('')
    rec('### ### ### **THE NAVIGATOR`S READING, TESTED AGAINST THE STANDARD`S OWN WORDS.**')
    rec('### The reading: ### *what the author calls a finished keystone is the standard`s Tier-C')
    rec('### ROLE carrying the Tier-K OBLIGATION -- the both-axes quadrant -- which the standard')
    rec('### names as two tiers and never as their conjunction.*')
    rec('')
    rec('### ### **THE FIRST HALF IS CONFIRMED BY THE TIER TEXTS THEMSELVES.** ### `Tier K`s')
    rec('### obligation is ### **`grade . terminal . pin`** ### -- which is exactly the APPARATUS')
    rec('### axis. ### `Tier C` is the document that ### **`organizes` certified results ...')
    rec('### asserting *relationships* not individually certified** ### -- which is exactly the ROLE')
    rec('### axis. ### **SO THE TWO AXES ARE THE TWO TIERS, IN THE STANDARD`S OWN WORDS.**')
    rec('')
    rec('### ### **AND THE SECOND HALF IS CORRECTED, NOT CONFIRMED.** ### The standard does not')
    rec('### merely fail to name the conjunction. ### **IT FORECLOSES IT AT THE DOCUMENT LEVEL AND')
    rec('### ### THEN DISPOSES OF THE MIXED CASE BY RULING.**')
    rec('###   ### **(a) THE CITATION RULES ARE CONTRADICTORY**, and the standard calls one of them')
    rec('###     its load-bearing rule: `Tier K` ### **may be cited as certification**; `Tier C` is')
    rec('###     ### **cited for orientation and organization -- NEVER as certification.** ### A')
    rec('###     single document cannot carry both citation rules, so ### **THE CONJUNCTION IS NOT')
    rec('###     ### AN UNNAMED CLASS. ### IT IS AN EXCLUDED ONE.**')
    rec('###   ### **(b) AND THE STANDARD ALREADY HANDLES THE MIXED DOCUMENT -- BY RULING ONE TIER')
    rec('###     ### AND READING THE PARTS APART:**')
    say(built, 'the standard -- the CATALOGOS borderline, read the panels as C and the terminals '
               'as K', '###     ')
    rec('###     ### **`READ THE PANELS AS C, THE PINNED TERMINALS AS K`** ### is the standard`s')
    rec('###     answer to exactly the shape the reading calls unnamed.')
    rec('###   ### **(c) AND THE PREDECESSOR THAT DID NAME THE CONJUNCTION WAS RETIRED FOR IT:**')
    say(built, 'the standard -- the retired scheme spanned Tier K and Tier C at once', '###     ')
    rec('###     ### **A CLASS SPANNING TIER K AND TIER C AT ONCE WAS RETIRED AS COLLAPSING THE')
    rec('###     ### VERY DISTINCTION THE TAXONOMY EXISTS TO ENFORCE.**')
    rec('')
    rec('### ### ### **VERDICT : CORRECTED.**')
    rec('### ### **THE READING IS RIGHT THAT THE TWO AXES ARE THE TWO TIERS AND RIGHT THAT THE')
    rec('### ### STANDARD NEVER NAMES THEIR CONJUNCTION.** ### It is wrong that the conjunction is')
    rec('### merely unnamed: ### **THE STANDARD EXCLUDES IT BY ITS LOAD-BEARING CITATION RULE,')
    rec('### ### DISPOSES OF MIXED DOCUMENTS BY RULING ONE TIER AND READING THE PARTS APART, AND')
    rec('### ### RETIRED AN EARLIER SCHEME PRECISELY FOR SPANNING THE TWO.**')
    rec('### ### ### **AND THAT MAKES THE AUTHOR`S FINISHED KEYSTONE A REAL AMENDMENT RATHER THAN A')
    rec('### ### ### CLARIFICATION** -- it asks for a document that is BOTH, which the standing')
    rec('### standard as written does not permit. ### **WHICH IS WHY COMPONENT 4(i) IS AN AMENDMENT')
    rec('### ### AND NOT A GLOSS.**')

    # ============================================ COMPONENT 3 -- THE AUTHOR'S MODEL
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 3 -- THE AUTHOR`S MODEL, BANKED VERBATIM.')
    rec('-' * 100)
    rec('### ### **THE AUTHOR`S STATEMENT OF `2026-09-09`, RATIFIED BY THE PASTE.** ### Sliced whole')
    rec('### from the ferry between two ends each verified unique, ### **NO LINE DROPPED.**')
    ferry = io.open(os.path.join(D, 'b383_ferry_2026-09-09.txt'),
                    encoding='utf-8').read().split(chr(10))
    a = [i for i, x in enumerate(ferry) if x.startswith("COMPONENT 3 - THE AUTHOR'S MODEL")]
    b = [i for i, x in enumerate(ferry) if x.startswith('with glossary, bibliography and other')]
    assert len(a) == 1 and len(b) == 1 and a[0] < b[0], (a, b)
    model = ferry[a[0]:b[0] + 1]
    for ln in model:
        rec('###   | %s' % ln.rstrip())
    rec('### ### **LINES BANKED : %d. ### DROPPED : 0.**' % len(model))
    rec('### ### **IT IS BANKED AS THE AUTHOR`S STATEMENT AND NOT ADOPTED AS THIS SEAT`S FINDING.**')
    rec('### No document is measured against it and ### **NO DOCUMENT IS RULED UNDER IT.**')
    rec('')
    rec('### ### **AND THE AMENDMENT`S OWN REASON, BANKED VERBATIM BESIDE IT:**')
    say(built, 'the amendment -- the author`s reason, banked verbatim: it is a laboratory')
    say(built, 'the amendment -- synthesizing further research with and against these results')

    # ============================================ COMPONENT 4 -- THE AMENDMENTS
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 4 -- THE FOUR AMENDMENTS, DRAFTED AND ROUTED. ### **NO STANDARD IS EDITED.**')
    rec('-' * 100)
    rec('### ### **THESE ARE TEXTS, NOT EDITS.** ### Each is drafted as an amendment to')
    rec('### `THE_DOCUMENT_CLASS_TAXONOMY.md` and ### **ROUTED TO THE AUTHOR. ### THE AUTHOR')
    rec('### ### AMENDS.**')
    rec('')
    rec('### ### ### **AMENDMENT (i) -- THE FINISHED-KEYSTONE FURNITURE OBLIGATION.**')
    rec('### *Proposed as a fifth paragraph after `Tier E`, in the author`s own words of 2026-09-09:*')
    rec('###   > ### **A FINISHED KEYSTONE.** ### *A keystone is finished when it stands on its own,')
    rec('###   > covering all conclusions and insights from its cluster; when its every statement is')
    rec('###   > clear in the body and documented to its kernel witness by a correspondence table')
    rec('###   > accessible after the front matter; and when it carries the glossary, bibliography')
    rec('###   > and other tables its reader needs. ### **Support papers are the process and publish')
    rec('###   > alongside the keystone**, as the deposited group upload did.*')
    rec('### ### **WHY IT IS AN AMENDMENT AND NOT A GLOSS:** ### it requires ONE document to carry')
    rec('### the `Tier C` role and the `Tier K` obligation at once, and the standard`s load-bearing')
    rec('### citation rule ### **CURRENTLY EXCLUDES THAT COMBINATION** (Component 2). ### **SO THE')
    rec('### ### AUTHOR MUST ALSO SAY WHAT A FINISHED KEYSTONE IS CITED AS** -- certification for')
    rec('### its pinned rows and orientation for its synthesis, on the `CATALOGOS` pattern, or')
    rec('### something else. ### **THIS SEAT DOES NOT CHOOSE.**')
    rec('')
    rec('### ### ### **AMENDMENT (ii) -- THE CLUSTER UNIT.** ### *As the author`s amendment of')
    rec('### 2026-09-09 replaced it; its words, not this seat`s:*')
    for lbl in ('the amendment -- (ii) is REPLACED, the cluster unit',
                'the amendment -- read into the cluster`s synthesis rather than sitting isolated',
                'the amendment -- SEVERAL keystones, ONE, or NONE YET',
                'the amendment -- many-to-many, and it changes over time',
                'the amendment -- clusters and kernel constellations are amorphous',
                'the amendment -- a keystone is a synthesis at a moment',
                'the amendment -- another keystone beside it rather than superseding it',
                'the amendment -- NOT-YET-SYNTHESIZED, not owed and not deficient',
                'the amendment -- no cardinality constraint in either direction',
                'the amendment -- the rule is stated beside every count',
                'the amendment -- a plurality is not an anomaly, an absence is not a defect'):
        say(built, lbl)
    CL = J('b375_clusters')
    n_nokey = len(CL['subject_clusters_without_keystone'])
    rec('### ### ### **AND THE CENSUS`S COUNT, RESTATED UNDER THAT RULE:**')
    rec('###   ### **`%d` SUBJECT CLUSTERS HAVE REGISTRY ROWS AND NO KEYSTONE.**' % n_nokey)
    rec('###   ### ### **THE RULE, STATED BESIDE THE COUNT AS THE AMENDMENT REQUIRES:** ### a')
    rec('###   cluster may have SEVERAL keystones, ONE, or NONE YET; the relation is many-to-many')
    rec('###   and it changes over time. ### **A CLUSTER WITH NO KEYSTONE IS `NOT-YET-SYNTHESIZED`,')
    rec('###   ### NOT OWED AND NOT DEFICIENT.**')
    rec('###   ### **SO THE `%d` ARE `NOT-YET-SYNTHESIZED`**, and ### **NO GRADE IS MOVED AND NO ACT'
        % n_nokey)
    rec('###   ### IS RE-VERDICTED** ### by the restatement -- the amendment says so in its own')
    rec('###   words and this act does neither.')
    rec('### ### **AND `b375`S OWN WORDS ALREADY LEANED THIS WAY:**')
    say(built, 'the standard -- Tier C presumptive, the cluster syntheses')
    rec('')
    rec('### ### ### **AMENDMENT (iii) -- THE PER-DOCUMENT TIER SWEEP, PRICED.**')
    rec('### The standard names it as its own unfinished work, quoted in Component 1:')
    rec('### ### **`per-document confirmation is the standing sweep`** ### and ### **`the')
    rec('### ### per-document tier sweep across the full ~200 records remains the standing')
    rec('### ### follow-on`.** ### It has been unrun since `2026-07-28`.')
    P75 = J('b375_population')
    declared = P75['declared'] if isinstance(P75['declared'], int) else len(P75['declared'])
    notdecl = (P75['not_declared'] if isinstance(P75['not_declared'], int)
               else len(P75['not_declared']))
    rec('### ### **PRICED FROM THE RECORD`S OWN FIGURES:**')
    rec('###   the standard`s own estimate of the population : ### **`~200` RECORDS**, its words')
    rec('###   the census`s measured population              : ### **`%d` DOCUMENTS**' % (declared + notdecl))
    rec('###   documents already carrying a class line       : ### **`%d`**' % declared)
    rec('###   documents carrying none                       : ### **`%d`**' % notdecl)
    rec('### ### **SO THE SWEEP`S SIZE IS `%d` DOCUMENTS TO CONFIRM AND `%d` TO DECIDE FROM'
        % (declared, notdecl))
    rec('### ### SCRATCH.** ### And the standard`s `~200` against the census`s `%d` is itself'
        % (declared + notdecl))
    rec('### ### **A FIGURE THE SWEEP WOULD RECONCILE**, since neither is wrong for its own date.')
    rec('### ### ### **WHAT THE RECORD CANNOT PRICE: THE PER-DOCUMENT JUDGEMENT.** ### `b376`')
    rec('### measured that most documents say nothing about their own role, so most tier calls')
    rec('### ### **CANNOT BE MADE FROM THE DOCUMENT`S OWN TEXT.** ### The record counts documents;')
    rec('### it does not count reviewer effort. ### **UNPRICED, AND NAMED UNPRICED RATHER THAN')
    rec('### ### ESTIMATED.**')
    rec('')
    rec('### ### ### **AMENDMENT (iv) -- THE REVIEWER-RESERVOIR RULE.**')
    rec('### ### ### **THIS ACT COULD NOT LOCATE THAT RULE, AND SAYS SO RATHER THAN SUPPLYING IT.**')
    rec('### A controlled sweep of the canonical tree, the relay tools and the TECHNE modules ran')
    rec('### before the lock, ### **WITH A POSITIVE CONTROL THAT FIRED ON A PHRASE KNOWN PRESENT**')
    rec('### (`internal-until-fruit`, `%d` files) and ### **WITH THIS ACT`S OWN FILES EXCLUDED**'
        % E['control_hits'])
    rec('### (`b368`s rule).')
    for k, v in E['reservoir_probes'].items():
        rec('###   probe `%-22s` : ### **%d file(s)**' % (k, v))
    rec('### The only `reservoir` hit is an archived line about phantom kernels; the two `held in')
    rec('### reserve` hits are about ### **THE AUTHOR`S FIAT**, not reviewers.')
    rec('### ### ### **SO (iv) IS ROUTED AS A REQUEST AND NOT AS A RESTATEMENT:**')
    rec('###   > ### **REQUEST TO THE AUTHOR.** ### *The order names a `reviewer-reservoir rule`')
    rec('###   > currently sitting in a session-protocol section. ### It is not locatable in')
    rec('###   > `PLACE-papers`, in `relay/tools`, or in the TECHNE modules under that name or the')
    rec('###   > wordings tried. ### **PLEASE SUPPLY ITS LOCATION OR ITS TEXT** and the restatement')
    rec('###   > beside the class standard is a later act`s.*')
    rec('### ### **A SEAT CANNOT RESTATE A RULE IT CANNOT READ**, and a seat that supplies the words')
    rec('### itself has ### **WRITTEN A NEW RULE UNDER AN OLD NAME.**')

    rec('')
    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s' % (len(FAILS), FAILS or ''))
    rec('### ### **NO STANDARD WAS EDITED. ### NO AMENDMENT WAS APPLIED. ### NO CLASS WAS RULED.')
    rec('### ### NO GRADE WAS MOVED. ### NO ACT WAS RE-VERDICTED.**')
    rec('=' * 100)

    # ------------------------------------------------ THE STANDARDS ARE BYTE-IDENTICAL
    def blob(rel):
        r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True)
        return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None

    unedited = {}
    for rel in ('phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'REGISTRY.md',
                'phase1.5/method/THE_LOAD_BEARING_MAP.md'):
        live = io.open(os.path.join(PP, rel.replace('/', os.sep)),
                       encoding='utf-8', newline='').read()
        bl = blob(rel)
        unedited[rel] = (bl is not None
                         and live.replace(chr(13) + chr(10), chr(10)) == bl.replace(chr(13) + chr(10), chr(10)))
    rec('### **THE THREE STANDING DOCUMENTS, BYTE-IDENTICAL TO THEIR BLOBS AT THE END OF THIS ACT:**')
    for k, v in unedited.items():
        rec('###   %-56s %s' % (k, v))

    p = run_clock.write(D, 'b383_components_notes', LINES)
    out = dict(reread_failures=FAILS, reread_ok=(not FAILS),
               sources_read=3, tiers_quoted=4,
               acts_reconciled=len(ROWS), duplicated=len(dup), adds=len(add),
               rows=[dict(act=a, asked=q, verdict=v, why=w) for a, q, v, w in ROWS],
               verdict='CORRECTED', model_lines=len(model), model_dropped=0,
               amendments_drafted=4, amendments_applied=0, standards_edited=0,
               clusters_without_keystone=n_nokey, clusters_owed=0,
               declared_class_line=declared, not_declared_class_line=notdecl,
               reservoir_located=E['reservoir_located'], control_hits=E['control_hits'],
               standards_unedited=unedited, class_ruled=False, grades_moved=0,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b383_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
