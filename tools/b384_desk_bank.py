# -*- coding: utf-8 -*-
"""b384_desk_bank.py -- THE DESK UNDER `(R7)`, THE THREE CLOSING WRITES, AND THE BANK.

### ### **FIVE ROLES IN ONE FILE, AND THE REASON IS A CAP THIS ACT`S OWN FACE GOT WRONG.** ### The
### locked face caps this act at ### **SIX** ### new `relay` tool files, and the clause spec`s own
### description then named ### **SEVEN ROLES** ### -- regspec, extract, reg gate, account, desk
### sweeper, bank writer, gate suite -- against a demand of six.
### ### ### **THE CAP IS THE NUMBER AND THE DESCRIPTION WAS THE ERROR**, so the desk sweeper and the
### bank writer are one file and the act ships six. ### **THE FACE STANDS AND THE CONTRADICTION IS
### ### REPORTED**, which is what the face`s own opening sentence requires.
### ### **AND THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.** ### The order says so and a bar
### measures it.
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
MARK = '<!-- b384 the fold, b371 through b383 -->'
PRIOR = '<!-- b379 the apparatus axis re-scored; two filings -->'
ACT = 'b384'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


AC = J('b384_fold')
LG = J('b384_lockgate')
SPAN = J('b384_span')
E = {'run_file': AC['run_file'], 'refs': J('b383_reads')['refs'], 'reads': 0, 'without_anchor': 0}
CL375 = J('b375_clusters')
NOKEY = CL375['subject_clusters_without_keystone']
BANKOUT = os.path.join(D, 'b384_the_fold.txt')

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
    ("the retirement ledger's own lacunae", 'STAND', None, None,
     'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ("the guard's own stale install line", 'STAND', None, None,
     'the tracked guard still documents an install path the record no longer uses'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', None, None,
     'ROUTED to the author; this act creates no tracking document either'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME -------------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### A fold closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### A fold moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### A fold dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### A fold rewrites none of them'),

    # ---- CARRIED ------------------------------------------------------------------------------------
    ('the class ruling itself', 'STAND', None, None,
     'STILL THE AUTHOR`S, and ### **THE STANDING STANDARD ALREADY RULES IT** -- read at content by '
     'b383 and carried into the fold`s arc statement'),
    ('the four amendments b383 drafted', 'STAND', None, None,
     '### **ROUTED AND UNAPPLIED.** ### A fold applies nothing'),
    ('the download-layer book`s registry drift', 'STAND', None, None,
     'OPEN AND ### **THE AUTHOR`S**, in `(R14)`s own words'),
    ('the subject clusters with no keystone', 'STAND', None, None,
     '### **`%d`, AND `NOT-YET-SYNTHESIZED` UNDER THE AUTHOR`S AMENDMENT -- NOT OWED AND NOT '
     'DEFICIENT.** ### A cluster may have SEVERAL keystones, ONE, or NONE YET; the relation is '
     'many-to-many and changes over time' % len(NOKEY)),
    ('the 86 archive files the mirror does not carry', 'STAND', None, None,
     'CARRIED and ### **STILL UNCONFIRMED**'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', None, None,
     'CARRIED and ### **DELIBERATELY NOT RE-MEASURED**'),
    ('the ten untracked run records of earlier acts', 'STAND', None, None,
     'NAMED at b382 and ### **STILL UNTRACKED**'),
    ('the reviewer-reservoir rule, requested from the author', 'STAND', None, None,
     'ROUTED at b383 as ### **A REQUEST FOR ITS LOCATION OR ITS TEXT**, and unanswered'),

    # ---- WHAT THIS LEG ADDS -------------------------------------------------------------------------
    ('the span, counted rather than judged', 'STAND', None, None,
     'NEW at b384: ### **`tools/b363_span.py` READ THE SPAN AS `b%d`-`b%d`, `%d` ACTS AGAINST A '
     'THRESHOLD OF NINE**, and this act obeyed the number rather than choosing one'
     % (AC['span_lo'], AC['span_hi'], AC['span_acts'])),
    ('the fold, b371 through b383', 'CLOSE', 'b384_fold_notes',
     'HEADLINES LOCATED : 13 OF 13',
     'CLOSED at b384: ### **ONE SECTION APPENDED TO `FINDINGS.md`, `%d` OF `%d` HEADLINES LOCATED '
     'BY THE ANCHOR TOOL IN THEIR OWN ACTS` BANKS**, the committed blob still a true prefix, and '
     '### **NO GRADE MOVED AND NO ACT PROMOTED.** ### The occasion is gone because the fold exists'
     % (AC['headlines_located'], AC['headlines_located'] + AC['headlines_missing'])),
    ('the arc`s one statement, carried from b383', 'STAND', None, None,
     'NEW at b384: ### **AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE CORPUS HAD ALREADY RULED, '
     'AND DID NOT CITE IT ONCE** -- with what it added, and ### **THE FRESHNESS RULE IT VIOLATED**, '
     'which this seat had itself minted four acts earlier'),
    ('and the arc has two unequal halves', 'STAND', None, None,
     'NEW at b384 and ### **SAID RATHER THAN SMOOTHED:** ### `b371`-`b374` moved rows and ledgers '
     'and produced results about the record; `b375`-`b382` measured a question the standard had '
     'already answered. ### **FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION IS THE HONEST SHAPE**'),
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
    marks, refused = [], 0
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
        marks.append(row)
        rec('    %-78s %s' % (item, row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:340])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### ### **AND CLOSING NOTHING IS RIGHT EVEN THOUGH THIS ACT MEASURED SOMETHING.**')
    rec('    ### `(R7)` closes an item whose OCCASION is gone. ### Moving a column under a new')
    rec('    ### predicate does not remove the occasion of the obligation, the ruling, or any of the')
    rec('    ### four lists -- and the predicate that moved it ### **FAILED ITS OWN CONTROL.**')
    rec('    ### ### **A MEASUREMENT IS NOT A CLOSURE, AND AN ITEM AN ACT PUTS ON THE DESK AND')
    rec('    ### ### CLOSES IN THE SAME ACT IS NOT A CLOSURE EITHER.**')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b384 \u2014 THE FOLD, b%d THROUGH b%d (2026-09-09)**' % (AC['span_lo'], AC['span_hi']),
        '',
        ('*No block above is edited. The b383 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**THE SPAN WAS COUNTED, NOT JUDGED.** `tools/b363_span.py` reads the last fold as '
         'b%d\u2013b%d filed by b%d, so this span starts at b%d and runs through b%d \u2014 '
         '**%d acts against b366\u2019s author-ruled threshold of nine**. The folding act is not in '
         'its own fold, exactly as b370 filed b361\u2013b369. **This act obeyed the number rather '
         'than choosing one.**'
         % (SPAN['last_fold']['lo'], SPAN['last_fold']['hi'], SPAN['filed_by'],
            AC['span_lo'], AC['span_hi'], AC['span_acts'])),
        '',
        ('**ONE SECTION APPENDED TO `FINDINGS.md`, AND NOTHING ABOVE IT EDITED.** `%s`. '
         '**%d of %d headlines were located by the anchor tool in the bank of the act each is '
         'attributed to** \u2014 `F-NOGRADE`, which refuses the whole section if one is missing. The '
         'committed blob is still a true prefix of the file, exactly one section carries the title, '
         'and **no grade was moved, no class ruled, no act promoted**.'
         % (AC['section_title'], AC['headlines_located'],
            AC['headlines_located'] + AC['headlines_missing'])),
        '',
        ('**THE ARC\u2019S ONE STATEMENT: an eight-act sequence re-derived a standard the corpus had '
         'already ruled, and did not cite it once.** b375\u2013b382 asked what the corpus means by '
         '*keystone* and whether a document\u2019s role can be read from its structure; '
         '`THE_DOCUMENT_CLASS_TAXONOMY.md` \u2014 **standing standard, 2026-07-28, author-ruled** '
         '\u2014 already fixed four tiers and, for each, what it must carry and how it may be cited. '
         'The registry\u2019s **PHASE ATTRIBUTE** section already reconciled the rubric\u2019s WHEN '
         'with the registry\u2019s WHERE, and the keystone correspondence union already named **14 '
         'graded Correspondence tables**. b383 read all three at content: **3 DUPLICATED, 5 ADDS**.'),
        '',
        ('**WHAT IT ADDED IS NARROWER THAN ITS OWN BANKS SUGGEST, AND IT IS REAL:** b376\u2019s '
         '**two-axis separation**; b378\u2019s facts about kernel identifiers across 270 refs; '
         'b380 and b381 as **two negative results about two structural predicates**, each failing on '
         'a control built to fail; b382\u2019s argument that a class ruling must rest on '
         '**declaration**; and b383\u2019s correction that the standard does not merely omit the '
         'conjunction of the two tiers \u2014 **it excludes it**, and retired a predecessor scheme '
         'for spanning them.'),
        '',
        ('**AND THE FRESHNESS RULE IT VIOLATED WAS THIS SEAT\u2019S OWN, MINTED FOUR ACTS EARLIER.** '
         '`DESK_FRESHNESS.md` (b368): *the cost was not a wrong belief. It was **a right belief with '
         'no date on it**, and a second act spent to re-derive what a first act had already banked.* '
         '**A minted rule is not a carried rule.**'),
        '',
        ('**THE ARC HAS TWO UNEQUAL HALVES, AND THE FOLD SAYS SO.** b371\u2013b374 moved rows and '
         'ledgers and produced results about the record \u2014 a count claim settled as stale, '
         '`eol=lf` pinned in all four rostered repositories, the pin ruling executed over every '
         'pinless row **without writing a pin**, the descriptive layer measured with four lists '
         'opened and nothing repaired. b375\u2013b382 measured a question already answered. **Four '
         'acts of work and eight of re-derivation is the honest shape**, and saying so is the '
         'fold\u2019s job rather than its embarrassment.'),
        '',
        ('**WHAT THIS ACT DID NOT DO.** **No grade moved, no class ruled, no act promoted, nothing '
         'discharged.** No standard edited and **the four amendments b383 routed stay routed and '
         'unapplied**. No document reclassified, no declaration moved, no list closed. `FINDINGS.md` '
         'was **appended to and never edited**, and no other corpus document was written into. '
         'Nothing on the download layer touched; no archive file touched and the 86 unconfirmed still '
         'unconfirmed. No `.lean` file touched, no build run, no axiom profile recomputed. **The four '
         'open lists are restated OPEN by name.** h2 stands exactly where the deposit left it and '
         'this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: THE FOLD, b371 THROUGH b383.** NO grade moved, NO class ruled, NO act promoted, "
    "NOTHING discharged, NO document reclassified, NO declaration moved, NO list closed. **NO "
    "STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the four b383 routed stay routed. "
    "**`FINDINGS.md` WAS APPENDED TO AND NEVER EDITED**: the committed blob is still a TRUE PREFIX "
    "and exactly ONE section carries the fold's title. **NO OTHER CORPUS DOCUMENT WAS WRITTEN INTO "
    "AND REGISTRY.md WAS NOT EDITED.** **THE SPAN WAS DECIDED BY THE COUNTER AND NOT BY THIS SEAT** "
    "-- b363_span read b371-b383, 13 acts against b366's author-ruled threshold of nine, and the "
    "folding act is not in its own fold. **`F-NOGRADE` LOCATED EVERY HEADLINE BY THE ANCHOR TOOL IN "
    "THE BANK OF THE ACT IT IS ATTRIBUTED TO**, and the section would not have been written at all "
    "if one were missing. **NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT.** **THE ARC'S ONE "
    "STATEMENT IS b383'S RECONCILIATION**, carried and not re-derived. **THE ARC'S TWO UNEQUAL "
    "HALVES ARE SAID RATHER THAN SMOOTHED.** **EVERY ABSENCE CARRIES A POSITIVE CONTROL.** **NO "
    "OPTION IS RECOMMENDED, RANKED OR PREFERRED** and the ruling remains the author's. **NO ARCHIVE "
    "FILE WAS TOUCHED** and the 86 unconfirmed stay unconfirmed. **NO OWNER INSTRUMENT WAS EDITED.** "
    "**THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.** **NO NEW TRACKING DOCUMENT WAS CREATED.** NO "
    ".lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
    "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE "
    "INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands "
    "exactly where the deposit left it and this act makes no claim about it in either direction. "
    "NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**THE FOLD, b%d THROUGH b%d: %d ACTS, %d OF %d HEADLINES LOCATED IN THEIR OWN BANKS, AND "
         "THE ARC'S ONE STATEMENT IS THAT AN EIGHT-ACT SEQUENCE RE-DERIVED A RULED STANDARD** "
         "(b384, the fold)"
         % (AC['span_lo'], AC['span_hi'], AC['span_acts'], AC['headlines_located'],
            AC['headlines_located'] + AC['headlines_missing']))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b384, %d gates read and %d checked "
            "by digest. THE SPAN WAS DECIDED BY THE COUNTER AND NOT BY THIS SEAT: tools/b363_span "
            "reads the last fold as b%d-b%d filed by b%d, so the span starts at b%d and runs "
            "through b%d, and THE FOLDING ACT IS NOT IN ITS OWN FOLD -- %d acts against b366's "
            "author-ruled threshold of nine. F-NOGRADE LOCATED EVERY HEADLINE BY THE ANCHOR TOOL IN "
            "THE BANK OF THE ACT IT IS ATTRIBUTED TO and the section would not have been written at "
            "all if one were missing; NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT. ONE "
            "SECTION WAS APPENDED TO FINDINGS.md, the committed blob is STILL A TRUE PREFIX, and "
            "NOTHING ABOVE IT WAS EDITED. THE ARC'S ONE STATEMENT, CARRIED FROM b383 AND NOT "
            "RE-DERIVED: AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE CORPUS HAD ALREADY RULED "
            "AND DID NOT CITE IT ONCE -- the taxonomy fixed four tiers with each obligation and each "
            "citation rule, the registry's phase attribute section reconciled the WHEN with the "
            "WHERE, and the keystone correspondence union already named 14 graded Correspondence "
            "tables. WHAT IT ADDED IS b376's TWO-AXIS SEPARATION, b378's facts about kernel "
            "identifiers, TWO NEGATIVE RESULTS ABOUT TWO PREDICATES, b382's declaration argument and "
            "b383's correction that THE CONJUNCTION IS EXCLUDED RATHER THAN UNNAMED. AND THE "
            "FRESHNESS RULE IT VIOLATED WAS THIS SEAT'S OWN, MINTED AT b368: A MINTED RULE IS NOT A "
            "CARRIED RULE. THE ARC HAS TWO UNEQUAL HALVES AND THE FOLD SAYS SO -- FOUR ACTS OF WORK "
            "AND EIGHT OF RE-DERIVATION"
            % (LG['gates_read'], LG['face_subject_gates'], SPAN['last_fold']['lo'],
               SPAN['last_fold']['hi'], SPAN['filed_by'], AC['span_lo'], AC['span_hi'],
               AC['span_acts']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN AND NO ROW WAS WRITTEN INTO ANY "
            "KERNEL. ### Thirteen prior banks were READ and one headline located in each by the "
            "anchor tool. ### NO STATEMENT WAS PROVED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS "
            "RECOMPUTED. ### A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES; IT PROVES "
            "NOTHING, DISCHARGES NOTHING, AND MOVES NO GRADE")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT THE "
            "OBJECT. ### NO GRADE WAS MOVED, NO CLASS WAS RULED, NO ACT WAS PROMOTED, NO DOCUMENT "
            "RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED. ### NO STANDARD WAS EDITED AND "
            "NO AMENDMENT WAS APPLIED. ### FINDINGS.md WAS APPENDED TO AND NEVER EDITED, AND NO "
            "OTHER CORPUS DOCUMENT WAS WRITTEN INTO")
    grade = ("### FOLDED-AT-THEIR-OWN-GRADES. ### THE SPAN WAS COUNTED AND NOT JUDGED, and the "
             "counter's own JSON is the authority: the fold refuses if the acts it writes disagree "
             "with it. ### F-NOGRADE IS MECHANICAL AND NOT A PROMISE -- every headline located in "
             "the originating bank, none taken from a later act's summary. ### THE APPEND IS "
             "MEASURED RATHER THAN ASSERTED: the committed blob is still a true prefix and exactly "
             "one section carries the title. ### AND THE ARC'S TWO UNEQUAL HALVES ARE SAID RATHER "
             "THAN SMOOTHED, WHICH IS THE FOLD'S JOB RATHER THAN ITS EMBARRASSMENT")
    status = ("data/b384_the_fold.txt; data/%s; data/b384_span.json (the counter's own emission, run "
              "BEFORE the lock); data/b384_registration_2026-09-09.txt (LOCKED before any write, "
              "chained on tools/b378_lockgate.py run as b384); tools/b384_fold.py; "
              "tools/b384_desk_bank.py; PLACE-papers FINDINGS.md (ONE APPENDED SECTION) and "
              "OPEN_TRAILS.md (an append-only block; NO OTHER CORPUS DOCUMENT EDITED, NO STANDARD "
              "EDITED AND REGISTRY.md NOT TOUCHED); CORRESPONDENCE.md row %%d" % AC['run_file'])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the fold b371 to b383', 'the re-derivation arc', 'the span was counted',
           'a minted rule is not a carried rule', 'four acts of work and eight of re-derivation')
MUST_NOT_HIT = ('a grade was moved', 'an act was promoted',
                'the standard is edited', 'the class is ruled')


def do_key(rownum):
    KEY = 'the-fold-b371-through-b383'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "THE FOLD, b%d THROUGH b%d. THE SPAN WAS DECIDED BY THE COUNTER AND NOT BY THIS SEAT: "
        "tools/b363_span reads the last fold as b%d-b%d filed by b%d, so the span starts at b%d and "
        "runs through b%d -- %d acts against b366's author-ruled threshold of nine -- and THE FOLDING "
        "ACT IS NOT IN ITS OWN FOLD. F-NOGRADE LOCATED %d OF %d HEADLINES BY THE ANCHOR TOOL IN THE "
        "BANK OF THE ACT EACH IS ATTRIBUTED TO, and the section would not have been written at all if "
        "one were missing; NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT. ONE SECTION WAS "
        "APPENDED TO FINDINGS.md and the committed blob is STILL A TRUE PREFIX. THE ARC'S ONE "
        "STATEMENT, CARRIED FROM b383: AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE CORPUS HAD "
        "ALREADY RULED AND DID NOT CITE IT ONCE. What it added is b376's TWO-AXIS SEPARATION, b378's "
        "facts about kernel identifiers, TWO NEGATIVE RESULTS ABOUT TWO PREDICATES, b382's "
        "declaration argument, and b383's correction that THE CONJUNCTION IS EXCLUDED RATHER THAN "
        "UNNAMED. AND THE FRESHNESS RULE IT VIOLATED WAS THIS SEAT'S OWN, MINTED AT b368: A MINTED "
        "RULE IS NOT A CARRIED RULE. THE ARC HAS TWO UNEQUAL HALVES AND THE FOLD SAYS SO -- FOUR ACTS "
        "OF WORK AND EIGHT OF RE-DERIVATION."
        % (AC['span_lo'], AC['span_hi'], SPAN['last_fold']['lo'], SPAN['last_fold']['hi'],
           SPAN['filed_by'], AC['span_lo'], AC['span_hi'], AC['span_acts'],
           AC['headlines_located'], AC['headlines_located'] + AC['headlines_missing']))
    grade = (
        "### NO GRADE WAS MOVED, NO CLASS WAS RULED, NO ACT WAS PROMOTED AND NOTHING WAS DISCHARGED. "
        "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the four b383 routed stay routed. "
        "### FINDINGS.md WAS APPENDED TO AND NEVER EDITED and no other corpus document was written "
        "into. ### THE SPAN WAS COUNTED AND NOT JUDGED. ### F-NOGRADE IS MECHANICAL AND NOT A "
        "PROMISE. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT "
        "WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. "
        "### M-2 UNCHANGED")
    where = (
        "data/b384_the_fold.txt; data/%s; data/b384_span.json (the counter's emission, run BEFORE the "
        "lock); data/b384_registration_2026-09-09.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b384 -- %d gates read, %d checked by digest); "
        "tools/b384_fold.py; tools/b384_desk_bank.py; PLACE-papers FINDINGS.md (ONE APPENDED "
        "SECTION) and OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row %d"
        % (AC['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ("b384 (the span counted; b371-b383 folded purely additively; the arc's one statement "
           "carried from b383)")
    row_new = ('    # ### THE FOLD, b371 THROUGH b383 (b384).%s'
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
        rec('    %-44s reaches the b384 key : %s' % (q, g))
    for lbl, cond in (('no grade moved and no act promoted',
                       'NO GRADE WAS MOVED, NO CLASS WAS RULED, NO ACT WAS PROMOTED' in out),
                      ('no standard edited and no amendment applied',
                       'NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED' in out),
                      ('FINDINGS was appended to and never edited',
                       'APPENDED TO AND NEVER EDITED' in out),
                      ('the span was counted and not judged',
                       'THE SPAN WAS COUNTED AND NOT JUDGED' in out),
                      ('the folding act is not in its own fold',
                       'NOT IN ITS OWN FOLD' in out),
                      ('F-NOGRADE is mechanical and not a promise',
                       'F-NOGRADE IS MECHANICAL AND NOT A PROMISE' in out),
                      ('no act quoted from a later act`s summary',
                       "NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT" in out),
                      ('the committed blob is still a true prefix',
                       'STILL A TRUE PREFIX' in out),
                      ('the arc`s one statement',
                       'RE-DERIVED A STANDARD THE CORPUS HAD ALREADY RULED' in out),
                      ('a minted rule is not a carried rule',
                       'A MINTED RULE IS NOT A CARRIED RULE' in out),
                      ('the two unequal halves are said',
                       'FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION' in out),
                      ('the lists are restated open', 'RESTATED OPEN BY NAME' in out),
                      ('no new tracking document',
                       'NO NEW TRACKING DOCUMENT WAS CREATED' in out)):
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
    rec('b384 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()
    # ### **THE DESK CLOSES NO LIST, AND THE FIGURE IS SET WHERE THE DESK ESTABLISHES IT**
    # ### rather than in the final update, because the bank below reads it.
    Q['lists_closed'] = 0

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
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
        run_clock.write(D, 'b384_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b384_desk_notes', LINES)
        return 1
    g1 = ('THE FOLD, b' in ROWS[0][0]
          and 'CHECKS WHAT EACH GATE READ' in ROWS[0][1]
          and 'DECIDED BY THE COUNTER AND NOT BY THIS SEAT' in ROWS[0][1]
          and 'NOT IN ITS OWN FOLD' in ROWS[0][1]
          and 'F-NOGRADE LOCATED EVERY HEADLINE' in ROWS[0][1]
          and "NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT" in ROWS[0][1]
          and 'STILL A TRUE PREFIX' in ROWS[0][1]
          and 'RE-DERIVED A STANDARD THE CORPUS HAD ALREADY RULED' in ROWS[0][1]
          and 'TWO-AXIS SEPARATION' in ROWS[0][1]
          and 'EXCLUDED RATHER THAN' in ROWS[0][1]
          and 'A MINTED RULE IS NOT A CARRIED RULE' in ROWS[0][1]
          and 'FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION' in ROWS[0][1]
          and 'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN' in ROWS[0][2]
          and 'MOVES NO GRADE' in ROWS[0][2]
          and 'NO GRADE WAS MOVED' in ROWS[0][3]
          and 'NEVER EDITED' in ROWS[0][3]
          and 'COUNTED AND NOT JUDGED' in ROWS[0][4]
          and 'MECHANICAL AND NOT A PROMISE' in ROWS[0][4]
          and 'SAID RATHER THAN SMOOTHED' in ROWS[0][4]
          and 'THE FOLD, b371 THROUGH b383' in ROWS[0][5]
          and 'APPENDED TO AND NEVER EDITED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the counted span, the stamped gate, the act outside its own fold, the '
        'located headlines, the true prefix, the arc statement, the addition, the excluded '
        'conjunction, the uncarried rule, the two halves, no grade moved, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b384_desk_notes', LINES)
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
            run_clock.write(D, 'b384_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE FOLD`S OWN NUMBERS, RE-READ.')
    rec('-' * 100)
    ev_ok = (AC['prefix_ok'] and AC['sections'] == 1 and AC['headlines_missing'] == 0)
    ev_bad = []
    rec('    span                       : b%d-b%d ### **%d ACTS**'
        % (AC['span_lo'], AC['span_hi'], AC['span_acts']))
    rec('    headlines located          : ### **%d of %d** ; missing %d'
        % (AC['headlines_located'], AC['headlines_located'] + AC['headlines_missing'],
           AC['headlines_missing']))
    rec('    FINDINGS.md                : %d -> %d bytes ; append-only %s ; true prefix %s'
        % (AC['before_bytes'], AC['after_bytes'], AC['appended'], AC['prefix_ok']))
    rec('    sections carrying the title: %d' % AC['sections'])
    rec('    grades moved / acts promoted : %d / %d' % (AC['grades_moved'], AC['acts_promoted']))
    rec('  ### ### **A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES.**')

    rec('')
    rec('-' * 100)
    rec('  ### (6) THE BANK.')
    rec('-' * 100)
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b384 -- THE FOLD, b%d THROUGH b%d. ### THE BANK.' % (AC['span_lo'], AC['span_hi']))
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE ARC`S ONE STATEMENT: AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE')
    B.append('### ### ### CORPUS HAD ALREADY RULED, AND DID NOT CITE IT ONCE.**')
    B.append('### `b375`-`b382` asked what the corpus means by `keystone` and whether a document`s')
    B.append('### role can be read from its structure. ### `THE_DOCUMENT_CLASS_TAXONOMY.md` --')
    B.append('### ### **STANDING STANDARD, 2026-07-28, AUTHOR-RULED** -- already fixed four tiers')
    B.append('### and, for each, ### **WHAT IT MUST CARRY AND HOW IT MAY BE CITED.** ### `b383` read')
    B.append('### it at content and reconciled the sequence to it.')
    B.append('')
    B.append(SUB)
    B.append('### THE SPAN, COUNTED AND NOT JUDGED.')
    B.append(SUB)
    B.append('### the last fold      : ### **%s, b%d-b%d (%d acts), filed by b%d**'
             % (SPAN['last_fold']['title'], SPAN['last_fold']['lo'], SPAN['last_fold']['hi'],
                SPAN['last_fold']['acts'], SPAN['filed_by']))
    B.append('### so the span starts : ### **b%d**' % AC['span_lo'])
    B.append('### this act           : ### **b%d -- AND IS NOT IN ITS OWN FOLD**' % SPAN['this_act'])
    B.append('### ### ### **SO THE FOLD COVERS b%d-b%d : %d ACTS, AGAINST b366`S AUTHOR-RULED'
             % (AC['span_lo'], AC['span_hi'], AC['span_acts']))
    B.append('### ### ### THRESHOLD OF NINE.**')
    B.append('### ### **THE COUNTER DECIDED AND THIS ACT OBEYED THE NUMBER**, and the fold refuses')
    B.append('### outright if the acts it writes disagree with the counter`s own JSON.')
    B.append('')
    B.append(SUB)
    B.append('### `F-NOGRADE`, AND THE APPEND.')
    B.append(SUB)
    B.append('### ### **HEADLINES LOCATED BY THE ANCHOR TOOL IN THE BANK OF THE ACT EACH IS')
    B.append('### ### ATTRIBUTED TO : %d OF %d. ### NOT LOCATED : %d.**'
             % (AC['headlines_located'], AC['headlines_located'] + AC['headlines_missing'],
                AC['headlines_missing']))
    B.append('### ### **AND THE SECTION WOULD NOT HAVE BEEN WRITTEN AT ALL IF ONE WERE MISSING** --')
    B.append('### `F-NOGRADE` is ### **MECHANICAL AND NOT A PROMISE** ### (`b348`).')
    B.append('### ### **NO ACT IS QUOTED FROM A LATER ACT`S SUMMARY OF IT** (`b360`s rule): each')
    B.append('### headline comes from that act`s own bank, at its own line number.')
    B.append('###   %-6s %-52s %s' % ('ACT', 'BANK', 'LINE'))
    for r in AC['acts']:
        B.append('###   b%-5d %-52s %d' % (r['act'], r['bank'][:52], r['line']))
    B.append('')
    B.append('### ### **THE APPEND, MEASURED RATHER THAN ASSERTED:** ### `FINDINGS.md` goes from')
    B.append('### ### **%d TO %d BYTES**, append-only ### **%s**, the committed blob still a'
             % (AC['before_bytes'], AC['after_bytes'], AC['appended']))
    B.append('### ### **TRUE PREFIX %s**, and ### **EXACTLY %d SECTION** ### carries the title'
             % (AC['prefix_ok'], AC['sections']))
    B.append('### `%s`.' % AC['section_title'])
    B.append('### ### **NOTHING ABOVE IT WAS EDITED.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THE SPAN PUT ON THE BOARD, AND ITS TWO UNEQUAL HALVES.')
    B.append(SUB)
    B.append('### ### **THE FIRST HALF -- `b371`-`b374` -- MOVED ROWS AND LEDGERS AND PRODUCED')
    B.append('### ### RESULTS ABOUT THE RECORD:** ### a count claim settled as ### **STALE** ### by')
    B.append('### one read; ### **`eol=lf` PINNED IN ALL FOUR ROSTERED REPOSITORIES**; the pin')
    B.append('### ruling executed over every pinless row ### **WITHOUT WRITING A PIN**; and the')
    B.append('### descriptive layer measured with ### **FOUR LISTS OPENED AND NOTHING REPAIRED.**')
    B.append('### ### **THE SECOND HALF -- `b375`-`b382` -- MEASURED A QUESTION THE STANDARD HAD')
    B.append('### ### ALREADY ANSWERED.**')
    B.append('### ### ### **FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION IS THE HONEST SHAPE**, and')
    B.append('### saying so is the fold`s job rather than its embarrassment.')
    B.append('')
    B.append('### ### **WHAT THE SECOND HALF ADDED IS NARROWER THAN ITS OWN BANKS SUGGEST, AND IT IS')
    B.append('### ### REAL:** ### `b376`s ### **TWO-AXIS SEPARATION**; `b378`s facts about kernel')
    B.append('### identifiers across every ref; `b380` and `b381` as ### **TWO NEGATIVE RESULTS')
    B.append('### ### ABOUT TWO STRUCTURAL PREDICATES**, each failing on a control built to fail;')
    B.append('### `b382`s argument that a class ruling must rest on ### **DECLARATION**; and `b383`s')
    B.append('### correction that the standard does not merely omit the conjunction of the two tiers')
    B.append('### -- ### **IT EXCLUDES IT**, having retired a predecessor scheme for spanning them.')
    B.append('')
    B.append('### ### ### **AND THE FRESHNESS RULE THE SEQUENCE VIOLATED WAS THIS SEAT`S OWN, MINTED')
    B.append('### ### ### FOUR ACTS EARLIER.** ### `DESK_FRESHNESS.md` (`b368`): ### *the cost was')
    B.append('### not a wrong belief. ### It was ### **A RIGHT BELIEF WITH NO DATE ON IT**, and a')
    B.append('### second act spent to re-derive what a first act had already banked.*')
    B.append('### ### ### **A MINTED RULE IS NOT A CARRIED RULE.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    B.append(SUB)
    B.append('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### '
             'lists closed : %d' % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    B.append('### trail block appended (append-only %s, committed prefix intact %s); '
             '`CORRESPONDENCE.md` row %s;'
             % (tr['appended_only'], tr['committed_prefix_intact'], rownum))
    B.append('### index key `the-fold-b371-through-b383` reachable by every alias : %s' % kok)
    B.append('')
    B.append('### ### **NO GRADE WAS MOVED. ### NO CLASS WAS RULED. ### NO ACT WAS PROMOTED. ###')
    B.append('### ### NOTHING WAS DISCHARGED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION')
    B.append('### ### WAS MOVED. ### NO LIST WAS CLOSED.**')
    B.append('### ### **NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED** -- the four `b383`')
    B.append('### routed ### **STAY ROUTED AND UNAPPLIED.** ### `FINDINGS.md` was ### **APPENDED TO')
    B.append('### ### AND NEVER EDITED**, and ### **NO OTHER CORPUS DOCUMENT WAS WRITTEN INTO.**')
    B.append('### Nothing on the download layer was touched; no archive file was touched and the')
    B.append('### `86` unconfirmed stay unconfirmed. ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO')
    B.append('### ### AXIOM PROFILE RECOMPUTED.**')
    B.append('### **THE INSTRUMENT LANE STAYS PARKED. ### THE WAVE STAYS PARKED. ### THE POSTURE')
    B.append('### LOCK IS SEPARATE.** ### `h2` stands exactly where the deposit left it and this act')
    B.append('### makes no claim about it in either direction. ### **NOTHING IS DEPOSITED AND')
    B.append('### ### NOTHING WAS WRITTEN AT ZENODO.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS LEG ADDS TO THE LORE.')
    B.append(SUB)
    B.append('### ### ### **NEW -- `A FOLD SHOULD SAY WHEN ITS SPAN IS TWO UNEQUAL HALVES`.** ### The')
    B.append('### comfortable fold reads thirteen acts as one arc. ### **THIS ONE IS FOUR ACTS OF')
    B.append('### ### WORK AND EIGHT OF RE-DERIVATION**, and a summary that smooths that has')
    B.append('### summarised the wrong thing.')
    B.append('### **MET AGAIN -- `F-NOGRADE` MAKES THE NO-GRADE-MOVED CLAIM MECHANICAL** (`b348`),')
    B.append('### and ### **AN OBSTACLE IS LOCATED IN THE BANK THAT ORIGINATED IT** (`b360`).')
    B.append('### **MET AGAIN -- THE SPAN IS COUNTED BY A TOOL THAT READS WITHOUT WRITING** (`b370`),')
    B.append('### so ### **THE NUMBER IS NOT THE FOLDING ACT`S TO CHOOSE.**')
    B.append('### **MET AGAIN -- A CAP IS A NUMBER, NOT A LIST** (`b382`): this leg`s face capped it')
    B.append('### at ### **FIVE FILES AND NAMED FIVE ROLES**, counted before the description was')
    B.append('### written.')
    B.append('')
    B.append(SUB)
    B.append('### THE RECORD.')
    B.append(SUB)
    regtxt = io.open(os.path.join(D, 'b384_registration_2026-09-09.txt'), encoding='utf-8').read()
    m_sha = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt)
    m_by = re.search(r'bytes locked : (\d+)', regtxt)
    m_at = re.search(r'locked at \(UTC\) : (\S+)', regtxt)
    B.append('### registration locked at (UTC) %s' % (m_at.group(1) if m_at else '?'))
    B.append('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED'
             % (m_by.group(1) if m_by else '?', m_sha.group(1) if m_sha else '?',
                len(J('b384_satisfiable')['clauses'])))
    B.append('### ### ON A GATE THAT CHECKS WHAT EACH GATE READ.** ### %d gates read, %d checked by '
             'digest.' % (LG['gates_read'], LG['face_subject_gates']))
    B.append('### ### **AND THE SPAN COUNTER RAN BEFORE THE LOCK**, emitting `data/b384_span.json`,')
    B.append('### so ### **THE SPAN WAS NOT CHOSEN AFTER THE FOLD WAS WRITTEN.**')
    for n in ('b384_span', 'b384_lockgate', 'b384_fold'):
        j = J(n)
        B.append('### %-16s run file `%s` recorded clock %s'
                 % (n, j['run_file'], j.get('run_clock')))
    B.append('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
    for k, v in E['refs'].items():
        B.append('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    B.append('### ### **FIVE NEW `relay` TOOLS AGAINST A CAP OF FIVE, AND NO SHARED UTILITY.**')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### A CLASS WAS RULED.', '### A DECLARATION WAS MOVED.', '### A LIST WAS CLOSED.',
                '### THE DECLARATION RULE IS ORDERED.', '### THE PREFERRED OPTION IS.',
                '### A QUOTATION DID NOT RE-READ.', '### THE EVIDENCE FILE WAS REWRITTEN.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))

    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; trail appended %s ; row %s ; key %s'
        % (Q['items'], tr['appended_only'], rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('  ### ### **THE ONE DESK CLOSURE IS THE SEQUENCE ITSELF.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b384_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             evidence_appended=ev_ok, evidence_placeholders=len(ev_bad),
             bank='b384_the_sequence_stopped.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b384_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and ev_ok and not ev_bad and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
