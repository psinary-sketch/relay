# -*- coding: utf-8 -*-
"""b375_desk.py -- THE DESK UNDER `(R7)`, AND THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW,
### THE KEY.

### ### **FOUR ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools and the cap counts FILES. ### **A CAP IS NOT A SUGGESTION.**
### ### **AND THE FOUR LISTS `b373` AND `b374` PRODUCED ARE RESTATED `OPEN` BY NAME.** ### This act
### closes none of them; the order says so and a bar measures it.
"""
import datetime
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
MARK = '<!-- b375 the keystone and cluster census; three tests, one word -->'
PRIOR = '<!-- b374 the descriptive layer measured, and the functional equation filed -->'
ACT = 'b375'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


P, CL, IN, RB = J('b375_population'), J('b375_clusters'), J('b375_integration'), J('b375_rubric')
H374 = J('b374_hedge')
K16 = set(H374['keystones'])
K32 = set(P['tests']['order_rubric'])
KT = RB['totals']['KEYSTONE']
ST = RB['totals']['SUPPORT']

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

    # ---- THE FOUR OPEN LISTS, RESTATED OPEN BY NAME --------------------------------------------------
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', None, None,
     'OPEN. ### **b373 executed (R9) and the chain closed for almost none of the set.** ### This act '
     'is an orientation and closes nothing'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND', None, None,
     'OPEN. ### **b373 listed them with their carriers and ROUTED them, with three choices named and '
     'none chosen.** ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', None, None,
     'OPEN. ### **b374 listed every figure stated without a ref in its own sentence.** ### This act '
     'dates none of them'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', None, None,
     'OPEN. ### **b374 found entries the register carries that appear nowhere else under their own '
     'key.** ### This act rewrites none of them'),

    # ---- WHAT THIS ACT ADDS -------------------------------------------------------------------------
    ('the word KEYSTONE naming three different tests', 'STAND', None, None,
     'NEW at b375: the author-ruled taxonomy`s Tier K (certification at a pin), the order`s rubric '
     '(synthesis against other content), and THE_KEYSTONE_CENSUS`s own test. ### **THEY OVERLAP ON '
     'THREE DOCUMENTS OUT OF FORTY-SIX.** ### Which governs is A RULING AND NOT A READ, and this act '
     'measured all three and reconciled none'),
    ('the subject clusters with documents and no keystone', 'STAND', None, None,
     'NEW at b375: subject clusters whose registry rows name documents and none of which reads as a '
     'keystone under the order`s rubric. ### **A FINDING, NOT A HOLE IN THE SWEEP**'),
    ('the 307 documents that declare no class', 'STAND', None, None,
     'NEW at b375: the author-ruled taxonomy requires every corpus document to carry a tier, and most '
     'do not carry a DOCUMENT CLASS line. ### **REPORTED, NOT CONFERRED** -- the order forbids '
     'conferring a class, and this act confers none'),
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
            rec('              %s' % why[150:320])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    stands = [m for m in marks if m['disposition'] == 'STAND']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(stands)))
    rec('    ### ### ### **AND CLOSING NOTHING IS THE RIGHT ANSWER FOR AN ORIENTATION.** ### `(R7)`')
    rec('    ### closes an item whose OCCASION is gone; a census removes no occasion. ### **THE FOUR')
    rec('    ### ### LISTS ARE RESTATED `OPEN` BY NAME, WHICH THE ORDER REQUIRES AND A BAR MEASURES.**')
    return dict(items=len(marks), closed=len(closed), standing=len(stands),
                closures_refused=refused, marks=marks,
                closed_items=[dict(item=m['item'], file='data/%s' % m.get('killing_file'),
                                   date=m.get('date'), own_act=m.get('own_act')) for m in closed])


def trail_block(Q):
    nokey = CL['subject_clusters_without_keystone']
    return [
        '', MARK, '',
        '### **b375 — THE KEYSTONE AND CLUSTER CENSUS (2026-09-08)**',
        '',
        ('*No block above is edited. The b374 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**This act is an orientation. It classifies and it repairs nothing** — no document repaired, '
         'no class conferred on a document that declares its own, no keystone rewritten, no row '
         'edited, no grade moved, no deposit touched.'),
        '',
        '### The finding the census exists to report',
        '',
        ('**The word "keystone" names three different tests in this record, and they do not select the '
         'same documents.** The author-ruled taxonomy (`phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md`, '
         '2026-07-28) defines **Tier K by certification** — *claims backed by a machine-checked kernel '
         'terminal at a pin* — and **Tier C by synthesis** — *organizes certified results into a '
         'cross-system picture*. The order\'s rubric defines a **KEYSTONE by synthesis against other '
         'available content**. And `phase2/method/THE_KEYSTONE_CENSUS.md` used a third test: external '
         'results **and** a Correspondence table **and** citation by its spine.'),
        '',
        '| test | documents it selects | declare their own class line |',
        '|---|--:|--:|',
        '| the taxonomy\'s `Tier K` (certification at a pin) | %d | %d |'
        % (len(P['tests']['taxonomy_tier_k']),
           sum(1 for f in P['tests']['taxonomy_tier_k']
               if next(r for r in P['rows'] if r['file'] == f)['declared_line'])),
        '| the order\'s rubric (synthesis against other content) | %d | %d |'
        % (len(P['tests']['order_rubric']),
           sum(1 for f in P['tests']['order_rubric']
               if next(r for r in P['rows'] if r['file'] == f)['declared_line'])),
        '| the existing census\'s own test | %d | %d |'
        % (len(P['tests']['existing_census']),
           sum(1 for f in P['tests']['existing_census']
               if next(r for r in P['rows'] if r['file'] == f)['declared_line'])),
        '',
        ('**All three select the same document in %d cases.** The order\'s set and the existing '
         'census\'s set overlap on **%d**. **Nothing here reconciles them — which of the three governs '
         'is a ruling and not a read**, and it is the first entry in what the census does not know.'
         % (len(P['tests']['all_three']), len(K16 & K32))),
        '',
        '### The population, the clusters, and the integration state',
        '',
        ('**%d tracked markdown documents were classified from content and never from a path.** **%d '
         'declare a class line and %d do not** — and the author-ruled taxonomy says *every corpus '
         'document belongs to one of four tiers*. Under the order\'s four words the population reads '
         '%s. **A document whose own text does not say what it does is `OTHER`, not `SUPPORT` by '
         'default**, because defaulting to the larger class would manufacture the census\'s own answer.'
         % (P['documents'], P['declared'], P['not_declared'], P['order_tally'])),
        '',
        ('Clusters were enumerated from the cluster documents themselves and from **the registry\'s own '
         'sections and rows**, never from directory names. **%d subject clusters have documents in the '
         'registry and no keystone**: %s. A dated `Row addition` or `Version-log addition` heading is '
         'the registry maintaining itself and is **not** a subject cluster; both halves are reported.'
         % (len(nokey), ', '.join('`%s`' % x for x in nokey))),
        '',
        ('The integration state is **four columns, never averaged**. Column (d) — *what bears on it and '
         'is not in it* — is **non-empty for %d of %d keystones**, listed by anchor and never '
         'summarized; a ledger line bears on a keystone when it names one of the keystone\'s objects '
         'and the keystone does not name the act that wrote it. Columns reading `NOT DETERMINABLE FROM '
         'THE DOCUMENT`: (a) %d, (b) %d, (c) %d of %d.'
         % (IN['d_nonempty'], IN['keystones'], IN['not_determinable']['a'],
            IN['not_determinable']['b'], IN['not_determinable']['c'], IN['keystones'])),
        '',
        '### The rubric applied — and the measurement that depends on which test you use',
        '',
        ('The rubric says a keystone **may not** carry hedges, open questions or working notes. '
         '`b374`\'s audit was run **unmodified**. Against the order\'s own rubric the keystone layer '
         'carries **%.1f hedges per thousand sentences** and the support layer **%.1f** — the keystone '
         'layer hedging **more** than its control.'
         % (KT['per_k'], ST['per_k'])),
        '',
        ('**And that is the opposite of what b374 measured one act ago, with the same instrument.** '
         'b374 took its keystones from the existing census\'s sixteen and found **%.1f** against '
         '**%.1f** for the working notes — keystones hedging *less*. **The instrument did not change; '
         'the definition of "keystone" did.** The two sets overlap on %d documents. **A measurement of '
         'a layer is a measurement of whichever definition of that layer you used**, and this act '
         'reports both rather than choosing.'
         % (H374['totals']['KEYSTONE']['per_k'], H374['totals']['WORKING']['per_k'],
            len(K16 & K32))),
        '',
        ('**No document is called defective, demoted, or said to fail the rubric.** The measurement is '
         'the product; the disposition is the author\'s and is a later act.'),
        '',
        '### The four open lists, restated OPEN',
        '',
        ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** '
         '**LIST 2** — the rows grading a declaration the record has classified absent (b373). '
         '**OPEN.** **LIST 3** — the undated figures across the roster (b374). **OPEN.** '
         '**LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** '
         '**This act closes none of them and was not sent to.**'),
        '',
        ('*Species: **THREE TESTS, ONE WORD.** A census is only as meaningful as the definition it '
         'runs on, and this corpus carries three definitions of `keystone` that select overlapping but '
         'different documents. **The census measures all three and reconciles none — which governs is '
         'a ruling.** Where the census should live is routed to the author; **it did not create a '
         'tracking document on its own authority.** Trigger: the ruling on which test governs, or any '
         'disposition on the four open lists. Nothing here is a route, no coordinate is closed, and '
         '`h2` stands exactly where the deposit left it — this act makes no claim about it in either '
         'direction.*'),
    ]


SCOPE = (
    "**SCOPE: READS AND CLASSIFICATION ONLY.** NO document repaired, NO class conferred on a document "
    "that declares its own, NO keystone rewritten, NO row edited, NO grade moved, NO deposit touched — "
    "the order's own list, and each is a bar. **A DECLARED CLASS IS QUOTED VERBATIM, NEVER OVERWRITTEN "
    "AND NEVER TRANSLATED INTO THE ORDER'S VOCABULARY**; the order's class is a separate column the "
    "order itself asked for. **A DECLARATION OF `NOT PLACED` IS A DECLARATION** and the census does not "
    "place those documents. **NO CLUSTER WAS ENUMERATED FROM A DIRECTORY NAME AND NO KEYSTONE WAS "
    "ASSIGNED TO A CLUSTER BY RESEMBLANCE**; an unassignable keystone is UNASSIGNED. **NO CELL WAS "
    "INFERRED** — `NOT DETERMINABLE FROM THE DOCUMENT` is a full answer. **NO KERNEL WAS OPENED AND NO "
    "CITATION WAS CHECKED**: column (b) records what the document NAMES. **THE INSTRUMENT WAS RUN "
    "UNMODIFIED** and this act licensed no instrument edit. **NO DOCUMENT IS PRONOUNCED TO FAIL THE "
    "RUBRIC.** **NO LIST WAS CLOSED** — the four b373 and b374 produced are restated OPEN by name. **NO "
    "NEW TRACKING DOCUMENT WAS CREATED**; where the census should live is ROUTED to the author. NO "
    ".lean FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. NOTHING IS CLAIMED ABOUT THE "
    "MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO "
    "COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
    "lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE "
    "STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it and this "
    "act makes no claim about it in either direction. The wave PARKED by the author's ruling. NOTHING "
    "IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def corr_rows(Q):
    nokey = CL['subject_clusters_without_keystone']
    m = ("**THREE TESTS, ONE WORD: THE CORPUS CARRIES THREE DEFINITIONS OF `KEYSTONE` AND THEY SELECT "
         "%d, %d AND %d DOCUMENTS WITH ONLY %d IN ALL THREE** -- the author-ruled taxonomy's Tier K "
         "(certification at a pin), the order's rubric (synthesis against other content), and "
         "THE_KEYSTONE_CENSUS's own test (b375, the keystone and cluster census)"
         % (len(P['tests']['taxonomy_tier_k']), len(P['tests']['order_rubric']),
            len(P['tests']['existing_census']), len(P['tests']['all_three'])))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's exit code, the "
            "registration gate and the term scan together -- and **THE FIRST FACE WAS RE-ISSUED "
            "BECAUSE IT CARRIED A LIVE STRUCK-STEM USE THIS SEAT DID NOT READ BEFORE LOCKING**; the "
            "defective face is left on the record with its seal intact and is named on the face that "
            "replaced it. %d tracked documents were classified from content and never from a path; "
            "**%d declare a class line and %d do not**. **NOTHING IS RECONCILED: WHICH TEST GOVERNS IS "
            "A RULING AND NOT A READ**, and it is the first entry in what the census does not know."
            % (P['documents'], P['declared'], P['not_declared']))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run, no axiom profile was "
         "recomputed, and **NO KERNEL WAS OPENED AT ALL** -- column (b) of the integration state "
         "records what a document NAMES, not whether the thing named is there, which is a check this "
         "act was not sent to run.",
         "**PRINT: NOTHING WAS REPAIRED AND NO CLASS WAS CONFERRED.** Every declared class line is "
         "QUOTED VERBATIM and never overwritten or translated; a declaration of `NOT PLACED` is "
         "honoured as a declaration. `PLACE-papers/OPEN_TRAILS.md` gains ONE append-only block; "
         "`CORRESPONDENCE.md` gains this row; `tools/banked_index.py` gains one key. **NO DOCUMENT "
         "CLASSIFIED BY THIS ACT WAS EDITED, AND THE ARCHIVES AND THE DEPOSIT WERE READ AND COUNTED "
         "AND LEFT.** **FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW "
         "MOVED.** **NO NEW TRACKING DOCUMENT WAS CREATED** -- where the census should live is ROUTED "
         "to the author, which the order required. No findings section; no TECHNE file; no module "
         "pushed. **THE HOOK AND THE MIRROR ARE OWED AND PAID.**",
         "**THE CENSUS: %d DOCUMENTS, %d DECLARING A CLASS AND %d NOT; UNDER THE ORDER'S FOUR WORDS "
         "%s.** **%d SUBJECT CLUSTERS HAVE REGISTRY ROWS AND NO KEYSTONE** (%s), enumerated from the "
         "cluster documents and the registry's own sections and **never from directory names**; a "
         "dated registry-maintenance heading is not a subject cluster and both halves are reported. "
         "**THE INTEGRATION STATE IS FOUR COLUMNS NEVER AVERAGED**, and column (d) -- what bears on it "
         "and is not in it -- is **NON-EMPTY FOR %d OF %d KEYSTONES**, listed by anchor and never "
         "summarized. **THE RUBRIC APPLIED, WITH b374'S AUDIT UNMODIFIED: the keystone layer carries "
         "%.1f hedges per thousand sentences against the support layer's %.1f** -- and **THAT IS THE "
         "OPPOSITE DIRECTION FROM b374'S OWN MEASUREMENT ONE ACT AGO (%.1f against %.1f), WITH THE "
         "SAME INSTRUMENT AND A DIFFERENT DEFINITION OF `KEYSTONE`.** The two sets overlap on %d "
         "documents. **A MEASUREMENT OF A LAYER IS A MEASUREMENT OF WHICHEVER DEFINITION OF THAT LAYER "
         "YOU USED**, and this act reports both rather than choosing. **NO DOCUMENT IS PRONOUNCED TO "
         "FAIL THE RUBRIC.** **THE EXPECTATIONS ARE SCORED:** (F1) **SPLITS THREE WAYS AND HAD TO** -- "
         "%d%%, %d%% and %d%% declare under the three tests, so it is CONFIRMED under one and REFUTED "
         "under two; (F2) **CONFIRMED**; (F3) **CONFIRMED**, %d of %d. **THE DESK: %d SWEPT, %d "
         "CLOSED, %d STANDING** -- closing nothing is the right answer for an orientation, and **THE "
         "FOUR OPEN LISTS ARE RESTATED OPEN BY NAME.**"
         % (P['documents'], P['declared'], P['not_declared'], P['order_tally'],
            len(nokey), ', '.join('`%s`' % x for x in nokey),
            IN['d_nonempty'], IN['keystones'], KT['per_k'], ST['per_k'],
            H374['totals']['KEYSTONE']['per_k'], H374['totals']['WORKING']['per_k'],
            len(K16 & K32),
            _pct('taxonomy_tier_k'), _pct('order_rubric'), _pct('existing_census'),
            IN['d_nonempty'], IN['keystones'], Q['items'], Q['closed'], Q['standing']),
         SCOPE, "current"),
    ]


def _pct(key):
    fs = P['tests'][key]
    rows = {r['file']: r for r in P['rows']}
    if not fs:
        return 0
    return int(round(100.0 * sum(1 for f in fs if rows[f]['declared_line']) / len(fs)))


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the keystone census', 'three tests one word', 'the cluster census',
           'the document class', 'the integration state')
MUST_NOT_HIT = ('the classes are conferred', 'the clusters are repaired',
                'the lists are closed', 'the keystone test is ruled')


def main():
    rec('=' * 100)
    rec('b375 -- THE DESK UNDER (R7), AND THE THREE CLOSING WRITES.')
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
        run_clock.write(D, 'b375_desk_notes', LINES)
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b375_desk_notes', LINES)
        return 1
    g1 = ('THREE TESTS, ONE WORD' in ROWS[0][0]
          and 'RE-ISSUED' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2] and 'NO KERNEL WAS OPENED AT ALL' in ROWS[0][2]
          and 'NOTHING WAS REPAIRED AND NO CLASS WAS CONFERRED' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'NEVER AVERAGED' in ROWS[0][4]
          and 'OPPOSITE DIRECTION' in ROWS[0][4]
          and 'SPLITS THREE WAYS' in ROWS[0][4]
          and 'RESTATED OPEN BY NAME' in ROWS[0][4]
          and 'READS AND CLASSIFICATION ONLY' in ROWS[0][5]
          and 'NO LIST WAS CLOSED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the three tests, the re-issue, no terminal and no kernel opened, nothing '
        'repaired and no class conferred, the four columns, the opposite direction, the expectations, '
        'the open lists, and the scope : %s' % g1)
    if not g1:
        run_clock.write(D, 'b375_desk_notes', LINES)
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
                 % (start + k, stmt, term, prof, grade, scope, status)
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
            run_clock.write(D, 'b375_desk_notes', LINES)
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
    rec('=' * 100)
    p = run_clock.write(D, 'b375_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok, lists_closed=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b375_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


def do_key(rownum):
    nokey = CL['subject_clusters_without_keystone']
    key_new = (
        "    'three-tests-one-word': ['the keystone census', 'three tests one word',\n"
        "                            'the cluster census', 'the document class',\n"
        "                            'the integration state'],\n")
    row_new = (
        '    # ### THE KEYSTONE AND CLUSTER CENSUS (b375).\n'
        '    ("three-tests-one-word", "b375 (one census over 349 documents; it classifies and repairs '
        'nothing, confers no class, moves no grade and closes no list)",\n'
        '     "THREE TESTS, ONE WORD. The corpus carries three definitions of KEYSTONE and they do not '
        'select the same documents: the author-ruled taxonomy Tier K (certification at a pin) selects "\n'
        '     " ' + str(len(P['tests']['taxonomy_tier_k'])) + ', the order rubric (synthesis against '
        'other content) selects ' + str(len(P['tests']['order_rubric'])) + ', and THE_KEYSTONE_CENSUS '
        'own test selects ' + str(len(P['tests']['existing_census'])) + ' -- and only "\n'
        '     " ' + str(len(P['tests']['all_three'])) + ' documents are in all three. ' + str(P['documents'])
        + ' tracked documents were classified from content and never from a path; ' + str(P['declared'])
        + ' declare a class line and ' + str(P['not_declared']) + ' do not. ' + str(len(nokey)) + ' subject "\n'
        '     " clusters have registry rows and no keystone. Column (d) of the integration state is '
        'non-empty for ' + str(IN['d_nonempty']) + ' of ' + str(IN['keystones']) + ' keystones. And with '
        'b374 audit UNMODIFIED the keystone layer carries "\n'
        '     " ' + ('%.1f' % KT['per_k']) + ' hedges per thousand sentences against the support layer '
        + ('%.1f' % ST['per_k']) + ' -- THE OPPOSITE DIRECTION FROM b374 OWN MEASUREMENT ONE ACT AGO, '
        'WITH THE SAME INSTRUMENT AND A DIFFERENT DEFINITION.",\n'
        '     "### NOTHING WAS REPAIRED AND NO CLASS WAS CONFERRED ON A DOCUMENT THAT DECLARES ITS OWN; '
        'every declared class line is QUOTED VERBATIM and never overwritten or translated. ### A"\n'
        '     " DECLARATION OF NOT PLACED IS A DECLARATION and the census does not place those '
        'documents. ### WHICH OF THE THREE TESTS GOVERNS IS A RULING AND NOT A READ, and this act "\n'
        '     " measured all three and reconciled none. ### A MEASUREMENT OF A LAYER IS A MEASUREMENT '
        'OF WHICHEVER DEFINITION OF THAT LAYER YOU USED. ### NO CLUSTER WAS ENUMERATED FROM A"\n'
        '     " DIRECTORY NAME AND NO KEYSTONE WAS ASSIGNED BY RESEMBLANCE; UNASSIGNED is an answer. '
        '### NO CELL WAS INFERRED -- NOT DETERMINABLE FROM THE DOCUMENT is a full answer. ### NO"\n'
        '     " KERNEL WAS OPENED AND NO CITATION WAS CHECKED. ### NO DOCUMENT IS PRONOUNCED TO FAIL '
        'THE RUBRIC; the measurement is the product and the disposition is the author. ### NO LIST"\n'
        '     " WAS CLOSED -- the four lists b373 and b374 produced are restated OPEN by name. ### NO '
        'NEW TRACKING DOCUMENT WAS CREATED; where the census should live is ROUTED. ### NO LEAN"\n'
        '     " FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS '
        'CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",\n'
        '     "data/b375_the_keystone_and_cluster_census.txt; data/' + P['run_file'] + '; data/'
        + CL['run_file'] + '; data/' + IN['run_file'] + '; data/' + RB['run_file'] + ';"\n'
        '     " data/b375_registration_2026-09-08_reissued.txt (LOCKED before any write, on the audit '
        'exit code AND the registration gate AND the term scan);"\n'
        '     " data/b375_registration_2026-09-08.txt (THE FIRST FACE, LEFT ON THE RECORD WITH ITS SEAL '
        'INTACT: it carried a live struck-stem use this seat did not read before locking);"\n'
        '     " tools/b375_population.py (three columns, never merged); tools/b375_clusters.py (from '
        'the documents and the registry, never from paths);"\n'
        '     " tools/b375_integration.py (four columns, never averaged; column (d) by anchor); '
        'tools/b375_rubric.py (b374 audit UNMODIFIED, with the control beside it);"\n'
        '     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT CLASSIFIED BY THIS ACT '
        'WAS EDITED); CORRESPONDENCE.md row ' + str(rownum) + '"),\n')
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
    if "'three-tests-one-word'" not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if '"three-tests-one-word"' not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('three-tests-one-word')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : three-tests-one-word returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'three-tests-one-word' in o
        ok = ok and g
        rec('    %-44s reaches the b375 key : %s' % (q, g))
    for lbl, cond in (('nothing repaired, no class conferred',
                       'NOTHING WAS REPAIRED AND NO CLASS WAS CONFERRED' in out),
                      ('which test governs is a ruling',
                       'IS A RULING AND NOT A READ' in out),
                      ('a measurement of a layer is of its definition',
                       'WHICHEVER DEFINITION OF THAT LAYER YOU USED' in out),
                      ('no list was closed', 'NO LIST' in out and 'WAS CLOSED' in out),
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


if __name__ == '__main__':
    sys.exit(main())
