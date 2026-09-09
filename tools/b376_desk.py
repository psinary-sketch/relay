# -*- coding: utf-8 -*-
"""b376_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools at ten and the cap counts FILES. ### **A CAP IS NOT A
### ### SUGGESTION.**
### ### **AND THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME.** ### The order says so in as many words
### -- `the four open lists stay OPEN by name` -- and a bar measures it. ### **THIS ACT CLOSES NOTHING.**
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
MARK = '<!-- b376 the two-axis read; every test crosses -->'
PRIOR = '<!-- b375 the keystone and cluster census; three tests, one word -->'
ACT = 'b376'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


PR, AX, TS = J('b376_prior'), J('b376_axes'), J('b376_tests')
LG = J('b376_lockgate')
QD = AX['quadrants']
NB = len(TS['axis_b_plus'])
APPARATUS_ONLY = QD.get('A-B+', 0) + QD.get('A?B+', 0)
SILENT = AX['axis_a_tally'].get('A?', 0)
CERTB = TS['cert_by_axis_b']
NCROSS = TS['crosses']

# ### (item, disposition, killing-file STEM, the sentence that file must carry, why)
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
    ("the guard's own stale install line", 'STAND', None, None,
     'the tracked guard still documents an install path the record no longer uses'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', None, None,
     'ROUTED to the author and not answered by a seat; this act creates no tracking document either'),

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME -------------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### **b373 executed (R9) and the chain closed for almost none of the set.** ### This act '
     'is a read and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### **b373 listed them with their carriers and ROUTED them, with three choices named and '
     'none chosen.** ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### **b374 listed every figure stated without a ref in its own sentence.** ### This act '
     'dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### **b374 found entries the register carries that appear nowhere else under their own '
     'key.** ### This act rewrites none of them'),

    # ---- CARRIED FROM b375 --------------------------------------------------------------------------
    ('the word KEYSTONE naming three different tests', 'STAND', None, None,
     'CARRIED from b375 and ### **SHARPENED, NOT SETTLED, AT b376:** ### the three tests do not '
     'disagree because one is wrong. ### **EACH OF THEM ASKS BOTH QUESTIONS AT ONCE.** ### Which '
     'governs is A RULING AND NOT A READ, and this act makes none'),
    ('the subject clusters with documents and no keystone', 'STAND', None, None,
     'CARRIED from b375 and untouched by this act'),
    ('the documents that declare no class', 'STAND', None, None,
     'CARRIED from b375. ### **REPORTED, NOT CONFERRED** -- the order forbids conferring a class and '
     'this act confers none'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ("the census's stated definition and its own operation are different tests", 'STAND', None, None,
     'NEW at b376: the census STATES three clauses and OPERATIONALISES two of them through proxies, '
     '### **DROPS CLAUSE (iii) ENTIRELY AND ADDS A SIZE FLOOR THE DEFINITION NEVER MENTIONS.** ### '
     'Re-applied at the head its own operation returns %d where the census printed %d. ### **FILED, '
     'NOT REPAIRED** -- the census is not this act to edit' % (len(PR['operation_returns']),
                                                               len(PR['census_named']))),
    ('the corpus own prior definition mixes both axes inside one test', 'STAND', None, None,
     "NEW at b376: clause (ii) of the census's stated definition is the APPARATUS question and clauses "
     '(i) and (iii) are the ROLE question, joined by `and`. ### **THE CONFLICT THE THREE TESTS PRODUCE '
     'WAS ALREADY INSIDE THE FIRST ONE**'),
    ('every one of the three tests crosses the quadrants', 'STAND', None, None,
     'NEW at b376: all %d cross, none equals either axis, and their crossings differ in size. ### **A '
     'TEST THAT CROSSES IS A TEST THAT MIXES THE TWO AXES** -- which is the finding this act existed '
     'to produce, and it is a finding and not a ruling' % NCROSS),
    ('the documents that carry the apparatus and say nothing about their role', 'STAND', None, None,
     'NEW at b376: %d documents carry a table row a stranger can traverse and their own text says '
     'nothing about synthesising against other content. ### **THE APPARATUS AND THE PROSE COME '
     'APART**, and this act reclassifies none of them' % APPARATUS_ONLY),
    ('the documents declaring TIER K that carry no traversable row', 'STAND', None, None,
     'NEW at b376: of the %d documents declaring TIER K, ### **%d SCORE `B+` AND %d SCORE `B-`.** ### '
     'The declaration and the apparatus are not the same measurement, and ### **NO DECLARATION WAS '
     'DISPUTED, MOVED OR REMOVED BY THIS ACT**'
     % (sum(CERTB.values()), CERTB.get('B+', 0), CERTB.get('B-', 0))),
    ('the documents that do not say what they are', 'STAND', None, None,
     'NEW at b376: %d of %d score `A?` -- ### **THE CORPUS IS LARGELY SILENT ABOUT ITS OWN ROLE.** ### '
     'That silence is a MEASUREMENT and not a hole in the sweep, and ### **NO SILENT DOCUMENT WAS '
     'ASSIGNED A MARK BY INFERENCE**' % (SILENT, len(AX['scored']))),
    ('the rubric-test set is a floor and not a population', 'STAND', None, None,
     'NEW at b376: `OTHER` contains %d documents satisfying axis A on the strict reading and %d on the '
     'broad. ### **AND MOST QUALIFY ON A CLASS LINE A LATER ACT WROTE INTO THE DOCUMENT**, which axis '
     'A cannot tell from the document`s own voice. ### **THE FLOOR IS REAL AND THE CAVEAT IS PRINTED '
     'BESIDE IT**' % (len(TS['other_satisfying_a']), len(TS['other_satisfying_a_broad']))),
    ('the ruling itself, the class question', 'STAND', None, None,
     'NEW at b376 and ### **EXPLICITLY NOT DECIDED HERE.** ### Component 6 states the options the '
     'evidence supports and what each would oblige, ### **WITHOUT RECOMMENDING ONE.** ### The order '
     'says this act produces the evidence the ruling needs and makes no ruling'),
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
        rec('    %-64s %s' % (item[:64], row['disposition']))
        rec('        why : %s' % why[:150])
        if len(why) > 150:
            rec('              %s' % why[150:330])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### ### **AND CLOSING NOTHING IS THE RIGHT ANSWER FOR A READ.** ### `(R7)` closes an')
    rec('    ### item whose OCCASION is gone. ### **A READ THAT PRODUCES EVIDENCE FOR A RULING REMOVES')
    rec('    ### ### NO OCCASION -- IT SHARPENS ONE.** ### The four lists are restated `OPEN` by name,')
    rec('    ### which the order requires in as many words and a bar measures.')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b376 — THE TWO-AXIS READ (2026-09-08)**',
        '',
        ('*No block above is edited. The b375 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**This act is a read. It produces the evidence a class ruling needs and it makes no '
         'ruling** — no class ruled, no document reclassified, no class line written, no document '
         'repaired, no list closed. **THE FOUR OPEN LISTS BELOW STAY OPEN BY NAME.**'),
        '',
        ('**THE CORPUS ALREADY TRIED TO RULE THIS, AND ITS OWN ATTEMPT MIXES BOTH AXES.** '
         '`THE_KEYSTONE_CENSUS.md` §0 states a three-clause test — (i) states results for external '
         'readers **and** (ii) closes with a Correspondence table naming its terminals **and** (iii) '
         "is cited by its cluster's spine or the trunk — and its `OPERATIONALISED:` line applies "
         '**two of the three through proxies, drops clause (iii) entirely, and adds a `6 KB` size '
         'floor the definition never mentions.** Re-applied at the head, the census’s own operation '
         'returns **%d** documents where the census printed **%d** and recorded its detector at 20. '
         'Clause (ii) is the *apparatus* question; clauses (i) and (iii) are the *role* question; they '
         'are joined by `and`. **THE CONFLICT THE THREE TESTS PRODUCE WAS ALREADY INSIDE THE FIRST '
         'ONE.** The census is quoted, not repaired.'
         % (len(PR['operation_returns']), len(PR['census_named']))),
        '',
        ('**TWO AXES, QUOTED NOT INVENTED, AND EVERY DOCUMENT SCORED ON BOTH.** Axis A — synthesises a '
         "cluster *against other available content* versus gathers a subject's research *at a point in "
         'time* — from the author’s rubric. Axis B — carries a correspondence table naming **kernel, '
         'terminal, pin and grade** that a stranger can traverse — from the taxonomy’s own words. Each '
         'predicate was fixtured in both polarities before it scored anything, and each declares what '
         'it is deaf to. %d tracked documents were scored on both axes, **each axis computed '
         'without sight of the other**. Axis A: %s. Axis B: %s. `NOT DETERMINABLE` is a full '
         'answer and was never rounded '
         'into a quadrant.'
         % (len(AX['scored']), AX['axis_a_tally'], AX['axis_b_tally'])),
        '',
        ('**AND EVERY ONE OF THE THREE TESTS CROSSES THE QUADRANTS.** The certification test (Tier K '
         'declarations) spreads across %d cells, the rubric test across %d, the census test across %d '
         '— and **not one of the three equals either axis.** A test that crosses is a test that mixes '
         'the two axes. **SO THE THREE TESTS DO NOT DISAGREE BECAUSE ONE OF THEM IS WRONG. THEY '
         'DISAGREE BECAUSE EACH IS ASKING BOTH QUESTIONS AT ONCE AND WEIGHTING THEM DIFFERENTLY.** The '
         'overlap of the certification and rubric sets is %d documents; the `A+B+` quadrant is %d; '
         '**they are not the same set**, and both directions of the difference are listed by document '
         'in the bank rather than counted.'
         % (len(TS['tests']['taxonomy_tier_k']['cells']),
            len(TS['tests']['order_rubric']['cells']),
            len(TS['tests']['existing_census']['cells']),
            len(TS['overlap']), len(TS['both_axes']))),
        '',
        ('**THE APPARATUS AND THE PROSE COME APART.** %d documents carry a table row a stranger can '
         'traverse; **%d of them say nothing whatever about synthesising against other content.** And '
         'of the %d documents declaring `TIER K`, **%d carry a traversable row and %d do not** — so '
         'the navigator’s expectation that the certification-test set is close to a clean axis-B set '
         'is **refuted by the print**. No declaration was disputed, moved or removed: a declared class '
         'is quoted and never overwritten. The trap this act’s locked face named before the '
         'measurement stands — where declaration and apparatus agree, **that is reported as agreement '
         'and not as confirmation that the declarations are correct**, because both may be reading the '
         'same habit of writing.'
         % (NB, APPARATUS_ONLY, sum(CERTB.values()), CERTB.get('B+', 0), CERTB.get('B-', 0))),
        '',
        ('**THE RUBRIC-TEST SET IS A FLOOR AND NOT A POPULATION**, said plainly as the order requires: '
         '`OTHER` holds %d documents that satisfy axis A on the strict reading and %d on the broad, '
         'each printed with the sentence that qualifies it. **AND THE CAVEAT IS PRINTED BESIDE THE '
         'FINDING RATHER THAN LEFT IN THE PREDICATE’S SMALL PRINT:** most qualify on a `DOCUMENT '
         'CLASS` or `basis:` line that a *later act* wrote into the document, and **axis A cannot tell '
         'a document’s own voice from an annotation added to it**, because on the page they are the '
         'same words. **THE LARGER FACT IS THE SILENCE:** %d of %d documents score `A?` — they do not '
         'say what they are — and **no count of the documents that speak can bound the documents that '
         'are silent.**'
         % (len(TS['other_satisfying_a']), len(TS['other_satisfying_a_broad']),
            SILENT, len(AX['scored']))),
        '',
        ('**AND THE LOCK READ EVERY GATE THIS TIME.** b375 locked its registration chained on one '
         'gate’s verdict while another read `NOT CLEAN` and nobody looked. b376’s lock gate reads '
         '**%d pre-lock gates**, requires each to carry its own pass phrase, is fixtured in both '
         'polarities — a synthetic clean set must permit and a synthetic dirty set must refuse **for '
         'the right gate** — and the lock was chained on *its* exit code and not on any one gate’s. '
         '**A GATE THAT HAS ONLY EVER SAID YES IS NOT A GATE.** The prior defective face stays on the '
         'record, unedited, with its seal intact.' % LG['gates_read']),
        '',
        ('**WHAT THIS READ CANNOT DECIDE IS THE RULING**, and it does not pretend otherwise. The '
         'options the evidence supports are stated in the bank with the evidence for each and what '
         'each would oblige, **without a recommendation**. The four open lists — the rows citing at an '
         'unnameable ref, the rows grading an absent declaration, the undated figures, the '
         'bibliography entries nothing cites — **ARE RESTATED OPEN BY NAME AND NONE IS CLOSED.** No '
         'new tracking document was created on this act’s authority. h2 stands exactly where the '
         'deposit left it and this act makes no claim about it in either direction.'),
        '',
    ]


SCOPE = (
    "**SCOPE: READS AND CLASSIFICATION ONLY.** NO class ruled, NO document reclassified, NO class line "
    "written, NO document repaired, NO list closed — the order's own list, and each is a bar. **THIS "
    "ACT PRODUCES THE EVIDENCE THE AUTHOR'S CLASS RULING NEEDS AND MAKES NO RULING.** **A MARK ON AN "
    "AXIS IS NOT A CLASS**; two marks were recorded per document and no class was conferred, moved or "
    "removed. **A DECLARED CLASS IS QUOTED VERBATIM AND NEVER OVERWRITTEN.** **NOT DETERMINABLE IS A "
    "FULL ANSWER** and was never rounded into a quadrant. **THE CENSUS WAS QUOTED, NOT REPAIRED**, and "
    "its figures are read as exact when written. **NO OPTION IN COMPONENT 6 CARRIES A PREFERENCE "
    "WORD.** **NO LIST WAS CLOSED** — the four open lists are restated OPEN by name. **NO NEW TRACKING "
    "DOCUMENT WAS CREATED.** NO KERNEL WAS OPENED, NO PIN WAS RESOLVED AND NO CITATION WAS CHECKED: "
    "axis B reads the SHAPE of a traversable row, not the traversal, and not whether the row is true. "
    "NO .lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
    "lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE "
    "STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this "
    "act makes no claim about it in either direction. The wave PARKED by the author's ruling. NOTHING "
    "IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    m = ("**EVERY TEST CROSSES: THE CORPUS'S THREE DEFINITIONS OF `KEYSTONE` EACH MIX TWO INDEPENDENT "
         "AXES, AND SO DOES THE CORPUS'S OWN PRIOR DEFINITION** -- %d of %d documents scored on both "
         "axes, all %d tests crossing quadrants and none equal to either axis (b376, the two-axis "
         "read)" % (len(AX['scored']), len(AX['scored']), NCROSS))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A GATE THAT READS EVERY "
            "PRE-LOCK GATE** -- %d of them, each required to carry its own pass phrase, the gate "
            "fixtured in both polarities and the lock chained on ITS exit code and not on any one "
            "gate's, which is the cure for b375's incident and the defective face from that act stays "
            "on the record unedited with its seal intact. THE CORPUS'S OWN PRIOR ATTEMPT WAS HEARD "
            "FIRST AND QUOTED, NOT OUTVOTED: THE_KEYSTONE_CENSUS STATES A THREE-CLAUSE DEFINITION AND "
            "OPERATIONALISES TWO OF THEM THROUGH PROXIES, DROPS CLAUSE (iii) ENTIRELY AND ADDS A SIZE "
            "FLOOR THE DEFINITION NEVER MENTIONS -- re-applied at the head its own operation returns "
            "%d where it printed %d. Clause (ii) is the apparatus question and clauses (i) and (iii) "
            "are the role question, joined by `and`, so THE CONFLICT THE THREE TESTS PRODUCE WAS "
            "ALREADY INSIDE THE FIRST ONE. TWO AXES WERE BUILT FROM QUOTED WORDS, EACH FIXTURED IN "
            "BOTH POLARITIES AND EACH DECLARING WHAT IT IS DEAF TO, AND EVERY DOCUMENT WAS SCORED ON "
            "BOTH INDEPENDENTLY: axis A %s, axis B %s. ALL %d TESTS CROSS THE QUADRANTS AND NONE "
            "EQUALS EITHER AXIS; the certification/rubric overlap is %d and the A+B+ quadrant is %d "
            "and THEY ARE NOT THE SAME SET, with both directions of the difference listed BY DOCUMENT. "
            "%d documents carry a traversable row and %d of those say nothing about their own role, SO "
            "THE APPARATUS AND THE PROSE COME APART; of the %d declaring TIER K, %d carry a "
            "traversable row and %d do not, WHICH REFUTES THE EXPECTATION THAT THE CERTIFICATION SET "
            "IS A CLEAN AXIS-B SET. THE RUBRIC-TEST SET IS A FLOOR AND NOT A POPULATION -- OTHER holds "
            "%d strict and %d broad axis-A satisfiers -- AND MOST QUALIFY ON A CLASS LINE A LATER ACT "
            "WROTE INTO THE DOCUMENT, which axis A cannot tell from the document's own voice. AND THE "
            "LARGEST FACT IS THE SILENCE: %d of %d documents DO NOT SAY WHAT THEY ARE"
            % (LG['gates_read'], len(PR['operation_returns']), len(PR['census_named']),
               AX['axis_a_tally'], AX['axis_b_tally'], NCROSS, len(TS['overlap']),
               len(TS['both_axes']), NB, APPARATUS_ONLY, sum(CERTB.values()),
               CERTB.get('B+', 0), CERTB.get('B-', 0), len(TS['other_satisfying_a']),
               len(TS['other_satisfying_a_broad']), SILENT, len(AX['scored'])))
    term = ("### NO TERMINAL. ### NO KERNEL WAS OPENED AT ALL and NO PIN WAS RESOLVED: axis B reads "
            "the SHAPE of a row a stranger could traverse -- kernel, terminal, pin and grade together "
            "in one row -- and NEVER THE TRAVERSAL AND NEVER WHETHER THE ROW IS TRUE. b373 measured "
            "resolution; THIS ACT DOES NOT AND SAYS SO. This is a read over documents, not over "
            "mathematics")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED, NO BUILD WAS RUN AND NOTHING WAS "
            "COMPUTED ABOUT THE OBJECT -- no frame, no seed, no transform, no quadrature, no fit, no "
            "score, no series. ### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO CLASS LINE WAS "
            "WRITTEN, NO DOCUMENT WAS REPAIRED AND NO LIST WAS CLOSED -- the order's five prohibitions, "
            "each measured by its own must-fail fixture. ### A MARK ON AN AXIS IS NOT A CLASS")
    grade = ("### EVIDENCE-FOR-A-RULING, THE RULING NOT MADE. ### The two axes are QUOTED FROM THEIR "
             "SOURCES with file and line and were not invented by this seat; each predicate is "
             "FIXTURED IN BOTH POLARITIES and DECLARES WHAT IT IS DEAF TO. ### AXIS A IS DEAF TO A "
             "DOCUMENT THAT SYNTHESISES AND NEVER SAYS SO -- it scores A?, not A- -- AND IT CANNOT "
             "TELL A DOCUMENT'S OWN VOICE FROM A CLASS LINE A LATER ACT ADDED, which is load-bearing "
             "on the floor finding and is printed there. ### AXIS B IS DEAF TO A PIN GIVEN AS A DATE, "
             "A TERMINAL WITHOUT BACKTICKS, AND WHETHER THE PIN RESOLVES. ### BOTH READINGS OF AXIS A "
             "WERE RUN AND BOTH ARE PRINTED; NEITHER IS SUBSTITUTED FOR THE OTHER. ### NOT "
             "DETERMINABLE IS A FULL ANSWER AND WAS NEVER ROUNDED INTO A QUADRANT. ### COMPONENT 6 "
             "STATES THE OPTIONS AND WHAT EACH WOULD OBLIGE WITHOUT RECOMMENDING ONE, and WHICH TEST "
             "GOVERNS REMAINS A RULING AND NOT A READ")
    status = ("data/b376_the_two_axis_read.txt; data/%s; data/%s; data/%s; data/%s; "
              "data/b376_registration_2026-09-08.txt (LOCKED before any write, chained on "
              "tools/b376_lockgate.py which read all %d pre-lock gates and is fixtured in both "
              "polarities); tools/b376_lockgate.py; tools/b376_prior.py; tools/b376_axes.py; "
              "tools/b376_tests.py; PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT "
              "SCORED BY THIS ACT WAS EDITED); CORRESPONDENCE.md row %%d"
              % (PR['run_file'], AX['run_file'], TS['run_file'], LG['run_file'], LG['gates_read']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the two axis read', 'every test crosses', 'the class ruling evidence',
           'the apparatus and the prose', 'the floor question')
MUST_NOT_HIT = ('the class is ruled', 'the documents are reclassified',
                'the lists are closed', 'the keystone test is settled')


def do_key(rownum):
    key_new = (
        "    'every-test-crosses': ['the two axis read', 'every test crosses',\n"
        "                          'the class ruling evidence', 'the apparatus and the prose',\n"
        "                          'the floor question'],\n")
    row_new = (
        '    # ### THE TWO-AXIS READ (b376).\n'
        '    ("every-test-crosses", "b376 (one read over ' + str(len(AX['scored']))
        + ' documents on two axes; it produces the evidence a class ruling needs and MAKES NO RULING)",\n'
        '     "EVERY TEST CROSSES. The corpus three definitions of KEYSTONE each mix two independent '
        'axes -- axis A, synthesises against other available content, and axis B, carries a "\n'
        '     " correspondence table naming kernel, terminal, pin and grade that a stranger can '
        'traverse. All ' + str(NCROSS) + ' tests cross the quadrants and NONE equals either axis, so '
        'THE THREE TESTS DO NOT DISAGREE BECAUSE ONE IS WRONG -- "\n'
        '     " EACH IS ASKING BOTH QUESTIONS AT ONCE. And the corpus own prior attempt does it too: '
        'THE_KEYSTONE_CENSUS states three clauses and operationalises two through proxies, DROPS "\n'
        '     " CLAUSE (iii) ENTIRELY and ADDS A SIZE FLOOR THE DEFINITION NEVER MENTIONS; re-applied '
        'at the head its own operation returns ' + str(len(PR['operation_returns']))
        + ' where it printed ' + str(len(PR['census_named'])) + '. "\n'
        '     " ' + str(NB) + ' documents carry a traversable row and ' + str(APPARATUS_ONLY)
        + ' of those say nothing about their own role, SO THE APPARATUS AND THE PROSE COME APART; of '
        'the ' + str(sum(CERTB.values())) + ' declaring TIER K, ' + str(CERTB.get('B+', 0)) + ' carry a "\n'
        '     " traversable row and ' + str(CERTB.get('B-', 0)) + ' do not. THE RUBRIC-TEST SET IS A '
        'FLOOR AND NOT A POPULATION, and MOST QUALIFIERS QUALIFY ON A CLASS LINE A LATER ACT WROTE INTO '
        'THE DOCUMENT. "\n'
        '     " AND THE LARGEST FACT IS THE SILENCE: ' + str(SILENT) + ' of ' + str(len(AX['scored']))
        + ' documents DO NOT SAY WHAT THEY ARE.",\n'
        '     "### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO CLASS LINE WAS WRITTEN, NO '
        'DOCUMENT WAS REPAIRED AND NO LIST WAS CLOSED. ### A MARK ON AN AXIS IS NOT A CLASS."\n'
        '     " ### WHICH TEST GOVERNS IS A RULING AND NOT A READ, and this act states the options and '
        'what each would oblige WITHOUT RECOMMENDING ONE. ### THE CENSUS WAS QUOTED, NOT REPAIRED."\n'
        '     " ### NOT DETERMINABLE IS A FULL ANSWER AND WAS NEVER ROUNDED INTO A QUADRANT. ### AXIS A '
        'CANNOT TELL A DOCUMENT OWN VOICE FROM A CLASS LINE A LATER ACT ADDED, which is"\n'
        '     " load-bearing on the floor finding and is printed beside it. ### AXIS B READS THE SHAPE '
        'OF A TRAVERSABLE ROW AND NEVER THE TRAVERSAL: NO KERNEL WAS OPENED AND NO PIN RESOLVED."\n'
        '     " ### WHERE DECLARATION AND APPARATUS AGREE THAT IS REPORTED AS AGREEMENT AND NOT AS '
        'CONFIRMATION THAT THE DECLARATIONS ARE CORRECT. ### THE FOUR OPEN LISTS ARE RESTATED"\n'
        '     " OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO '
        'BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ###"\n'
        '     " THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",\n'
        '     "data/b376_the_two_axis_read.txt; data/' + PR['run_file'] + '; data/' + AX['run_file']
        + '; data/' + TS['run_file'] + '; data/' + LG['run_file'] + ';"\n'
        '     " data/b376_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON A GATE THAT '
        'READS EVERY PRE-LOCK GATE -- ' + str(LG['gates_read']) + ' of them, fixtured in both'
        ' polarities);"\n'
        '     " tools/b376_lockgate.py (the cure for b375 incident: a tool that REFUSES, not a note '
        'that remembers); tools/b376_prior.py (the corpus own prior attempt, heard first);"\n'
        '     " tools/b376_axes.py (two axes quoted from their sources, each fixtured in both '
        'polarities, each declaring what it is deaf to); tools/b376_tests.py (the crossings and the'
        ' floor);"\n'
        '     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT SCORED BY THIS ACT WAS '
        'EDITED); CORRESPONDENCE.md row ' + str(rownum) + '"),\n')
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
    if "'every-test-crosses'" not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if '"every-test-crosses"' not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('every-test-crosses')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : every-test-crosses returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'every-test-crosses' in o
        ok = ok and g
        rec('    %-44s reaches the b376 key : %s' % (q, g))
    for lbl, cond in (('no class ruled, none reclassified',
                       'NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED' in out),
                      ('which test governs is a ruling',
                       'IS A RULING AND NOT A READ' in out),
                      ('a mark on an axis is not a class',
                       'A MARK ON AN AXIS IS NOT A CLASS' in out),
                      ('no list was closed', 'NO LIST' in out and 'WAS CLOSED' in out),
                      ('the lists are restated open',
                       'RESTATED' in out and 'OPEN BY NAME' in out),
                      ('no new tracking document', 'NO NEW TRACKING DOCUMENT WAS CREATED' in out)):
        ok = ok and cond
        rec('    %-44s : %s' % (lbl, cond))
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        g = pre[q] and no_key(o)
        ok = ok and g
        rec('    %-40s NO KEY after  : %s' % (q, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    rec('=' * 100)
    rec('b376 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE DESK.')
    rec('-' * 100)
    Q = do_desk()

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
        run_clock.write(D, 'b376_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b376_desk_notes', LINES)
        return 1
    g1 = ('EVERY TEST CROSSES' in ROWS[0][0]
          and 'READS EVERY PRE-LOCK GATE' in ROWS[0][1]
          and 'ALREADY INSIDE THE FIRST ONE' in ROWS[0][1]
          and 'THE APPARATUS AND THE PROSE COME APART' in ROWS[0][1]
          and 'FLOOR AND NOT A POPULATION' in ROWS[0][1]
          and 'DO NOT SAY WHAT THEY ARE' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2] and 'NO KERNEL WAS OPENED AT ALL' in ROWS[0][2]
          and 'NO CLASS WAS RULED' in ROWS[0][3]
          and 'A MARK ON AN AXIS IS NOT A CLASS' in ROWS[0][3]
          and 'FIXTURED IN BOTH POLARITIES' in ROWS[0][4]
          and 'DEAF TO' in ROWS[0][4]
          and 'WITHOUT RECOMMENDING ONE' in ROWS[0][4]
          and 'READS AND CLASSIFICATION ONLY' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says every test crosses, the lock read every gate, the conflict was already in the '
        'first test, the apparatus and the prose, the floor, the silence, no terminal and no kernel '
        'opened, no class ruled, the fixtures and the deafness, no recommendation, and the scope : %s'
        % g1)
    if not g1:
        run_clock.write(D, 'b376_desk_notes', LINES)
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
                 % (start + k, stmt, term, prof, grade, scope, (status % (start + k))
                    if '%d' in status else status)
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
            run_clock.write(D, 'b376_desk_notes', LINES)
            return 1
        rownum = start

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('=' * 100)
    rec('  ### desk swept %d ; trail appended %s ; row %s ; key %s'
        % (Q['items'], tr['appended_only'], rownum, kok))
    rec('  ### ### **LISTS CLOSED : 0. ### THE FOUR ARE RESTATED `OPEN` BY NAME.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b376_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b376_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
