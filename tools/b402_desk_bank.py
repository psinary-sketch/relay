# -*- coding: utf-8 -*-
"""b402_desk_bank.py -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.

### ### **THE FOLD ITSELF WAS WRITTEN BY `b402_fold.py` AND IS NOT REMADE HERE.** ### This file
### records what the leg swept, files the append-only trail block, appends the correspondence row
### and the index key, and writes the bank.
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
MARK = '<!-- b402 the artefact arc folded, b385-b401 -->'
PRIOR = '<!-- b401 the absent element searched; the fourth site entered -->'
BANKOUT = os.path.join(D, 'b402_the_fold.txt')

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


SEALTXT = io.open(os.path.join(D, 'b402_registration_2026-09-10.txt'), encoding='utf-8').read()
SEALHASH = re.search(r'([0-9a-f]{64})', SEALTXT.split('LOCK')[-1]).group(1)
LG = J('b402_lockgate')
FD = J('b402_fold')
SP = J('b402_span')

DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', 'PARKED'),
    ('the instrument-audit lane, PARKED under ruling R22', 'STAND', 'PARKED at b397'),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND',
     'OPEN. ### **TRIGGER: when a row of it is cited by an act.**'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This leg moves no grade. ### **TRIGGER: when a grade must be defended.**'),
    ('LIST 3 -- the undated figures across the roster', 'STAND',
     'OPEN. ### This leg dates none. ### **TRIGGER: when a figure is quoted forward.**'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND',
     'OPEN. ### **TRIGGER: at the next bibliography pass.**'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', 'OPEN AND THE AUTHOR`S'),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the deposited layer, unread since b389', 'STAND', 'STILL BLOCKED'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('the keystones` stale `HELD` prose', 'STAND', 'ROUTED at b397, OPEN'),
    ('the `82` at-risk figures', 'STAND', 'TRIGGERED at b397, and PARKED by `(R22)`'),
    ('`(N)`, the smallest next statement toward the clause', 'STAND', 'NAMED at b398. ### **OPEN**'),
    ('the grade move inside b332`s E0 ranking table', 'STAND',
     'ROUTED at b399, trigger THE AUTHOR`S WORD. ### **OPEN**'),
    ('`b321`s prime-power rule against its own printed list', 'STAND',
     'ROUTED at b400, restated as routed at b401, and ### **STILL ROUTED**'),
    ('`SIDE-window`s README terminal count, stale against its own head', 'STAND',
     'FOUND at b401, ### **ROUTED AND NOT REPAIRED** -- another repository`s file and the '
     'instrument-audit lane is PARKED'),
    ('`(Q400)`, the prime constituent at a support where the primes enter', 'STAND',
     '### **OPEN**, its absence confirmed by search at b401 and ### **NOT OPENED**'),
    ('the write-list species, twice repaired and twice still short', 'STAND',
     '### `b399` omitted a STAGE; `b400` walked the ritual forward and omitted RE-RUNS and the '
     'LAST step; `b401` and this leg build the list as ### **KINDS.** ### **FILED, AND THE NEXT '
     'FACE WILL SHOW WHETHER KINDS IS ENOUGH**'),

    # ---- WHAT THIS LEG CLOSES --------------------------------------------------------------------
    ('whether the fold is due, and at what count', 'CLOSE',
     '### **CLOSED BY THE COUNTER AND THE RULING, NOT BY THE SEAT.** ### The last fold covered '
     '`b371`-`b383` and was filed by `b384`, so the span starts at `b385`; this act is `b402` and '
     'is ### **NOT IN ITS OWN FOLD**; so the fold covers `b385`-`b401`, ### **`17` ACTS** ### '
     'against a threshold of ### **NINE** ### ruled at `b366` as `(R1)`. ### **THE FOLD IS DUE '
     'AND IS WRITTEN.** ### The navigator`s `sixteen` is printed beside it and ### **REFUTED BY '
     'ONE SUBTRACTION**'),
    ('the span b385-b401, unfolded since b384', 'CLOSE',
     '### **FOLDED INTO `FINDINGS.md` AS `THE ARTEFACT ARC`, PURELY ADDITIVE.** ### `17` of `17` '
     'headlines located by the anchor tool in their own acts` banks; `0` missing; the section '
     'refused to write at all if any had failed. ### The section carries the arc`s one statement '
     'with its scope beside it, the act-by-act table, the corrections table, the defective-bars '
     'table and the seats` own declared defects -- ### **THE LAST REACHING `b400` AND `b401`, '
     'WHICH IS THE POINT OF HAVING IT**'),

    # ---- WHAT THIS LEG ADDS ----------------------------------------------------------------------
    ('the span counter`s own threshold line, stale against `(R1)`', 'STAND',
     '### **NEW at `b402`, AND IT IS THE SPAN`S OWN SPECIES IN THE INSTRUMENT THAT MEASURES THE '
     'SPAN.** ### `b363_span.py` prints ### *THERE IS NO DECLARED THRESHOLD IN THE RECORD* ### and '
     'carries `threshold_declared: false`. ### True when `b363` wrote it; ### **FALSE SINCE '
     '`b366` RULED `(R1)`.** ### A DATED ARM. ### **ROUTED, NOT REPAIRED:** ### this leg reads '
     'the threshold from the ruling and says where it got it. ### **OPEN**'),
    ('the arc`s one statement, as a claim a later act may refute', 'STAND',
     '### **NEW at `b402`.** ### *In nine of seventeen acts the finding was that a limit, a count, '
     'an absence or a version already on the record was an artefact of how it had been measured; '
     'and in the four mathematical acts the limit was real.* ### **A FOLD`S STATEMENT IS ABOUT '
     'WHAT THE SPAN PUT ON THE BOARD AND NOT ABOUT THE OBJECT**, and it is refutable by counting '
     'the nine. ### **OPEN**'),
]


def do_desk():
    rec('    ### ### **THIS LEG CLOSES TWO ITEMS AND OPENS TWO.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 1400), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0)


def trail_block(Q):
    return [
        '',
        MARK,
        '',
        '### b402 — the artefact arc folded, b385–b401 — filed 2026-09-10',
        '',
        '**The fold is due and the count is the tool’s.** `tools/b363_span.py` reads and does not '
        'write: the last fold covered b371–b383 and was filed by b384, so the span starts at b385; '
        'this act is b402 and **is not in its own fold**; so the fold covers **b385–b401, 17 acts** '
        'against a threshold of **nine**, ruled by the author at b366 as (R1). **The navigator’s '
        'count for this span was sixteen. The tool’s is 17, and the tool governs** — the claim is '
        'refuted by one subtraction, and the direction is worth naming: sixteen is the span with '
        'its last act left out.',
        '',
        '**And the counter’s own line on the threshold is stale, which is this span’s species '
        'appearing in the instrument that measures the span.** `b363_span.py` prints *THERE IS NO '
        'DECLARED THRESHOLD IN THE RECORD — these are the folds that happened, not a rule anyone '
        'wrote down*, and its JSON carries `threshold_declared: false`. That was true when b363 '
        'wrote it and **has been false since b366 ruled (R1)**. A dated arm — b364’s species, right '
        'when written and dated by construction. **Routed, not repaired:** this leg reads the '
        'threshold from the ruling and says where it got it.',
        '',
        '**The fold, written into `FINDINGS.md` as `THE ARTEFACT ARC, b385–b401`, purely '
        'additive.** **17 of 17 headlines located by the anchor tool in their own acts’ banks, 0 '
        'missing** — and `F-NOGRADE` would have refused to write the section at all had one '
        'failed. No act is quoted from a later act’s summary of it. The pre-act file **and** the '
        'pre-act committed blob are both true prefixes of the result.',
        '',
        '**The arc’s one statement:** *in nine of these seventeen acts the finding was that a '
        'limit, a count, an absence or a version already on the record was an artefact of how it '
        'had been measured — and in the four mathematical acts that close the span the limit was '
        'real, and the work became stating it exactly.* The two halves are the same lesson at two '
        'scales: **a limit reported by an instrument is a property of the instrument until a second '
        'shape has been tried**, and the mathematical half tried a second shape and the limit held.',
        '',
        '**The section carries four tables and a scope sentence:** the span act by act at its own '
        'grades; the corrections this span made to its own readings and to each other’s; the '
        'defective bars it declared; and **the seats’ own defects, reaching b400 and b401** — the '
        'two most recent acts, each of which failed an arm of its own suite and said so. A defect '
        'table that stopped short of the present would be a table that flatters it.',
        '',
        '*A fold is a summary of its acts at their own grades. It proves nothing, discharges '
        'nothing, opens nothing and moves no grade. No coordinate is closed, the clause has not '
        'moved, `(Q400)` is not opened, and the four lists stay OPEN by name. Nothing deposits and '
        'the platform was not called at all. h2 stands exactly where the deposit left it.*',
        '',
    ]


SCOPE = (
    "**SCOPE: THE FOLD, DUE AND WRITTEN.** The count is the tool's: the last fold covered b371-b383 "
    "and was filed by b384, so the span starts at b385; this act is b402 and IS NOT IN ITS OWN "
    "FOLD; the fold covers **b385-b401, 17 ACTS** against a threshold of NINE ruled at b366 as "
    "(R1). **THE NAVIGATOR'S COUNT WAS SIXTEEN AND IS REFUTED BY ONE SUBTRACTION**, printed beside "
    "the tool's rather than quietly replaced. **AND THE COUNTER'S OWN THRESHOLD LINE IS STALE** -- "
    "it prints THERE IS NO DECLARED THRESHOLD IN THE RECORD and carries threshold_declared: false, "
    "true when b363 wrote it and false since b366; a DATED ARM, ROUTED not repaired, and this leg "
    "reads the threshold from the ruling and says so. **THE FOLD IS WRITTEN INTO FINDINGS.md AS "
    "`THE ARTEFACT ARC, b385-b401`, PURELY ADDITIVE**: 17 of 17 headlines located by the anchor "
    "tool in their own acts' banks, 0 missing, F-NOGRADE refusing to write the section at all had "
    "one failed, no act quoted from a later act's summary of it, and the pre-act FILE and the "
    "pre-act COMMITTED BLOB both true prefixes of the result. **THE ARC'S ONE STATEMENT: in nine of "
    "the seventeen acts the finding was that a limit, a count, an absence or a version already on "
    "the record was an ARTEFACT OF HOW IT HAD BEEN MEASURED -- and in the four mathematical acts "
    "that close the span the limit was REAL, and the work became stating it exactly.** The two "
    "halves are the same lesson at two scales, and the scope sentence stands beside the statement: "
    "this is about what the span put on the board, not about the object. **THE SECTION CARRIES FOUR "
    "TABLES**: the span act by act at its own grades; the corrections this span made to its own "
    "readings and to each other's; the defective bars it declared; and the seats' own defects, "
    "**REACHING b400 AND b401**, the two most recent acts, each of which failed an arm of its own "
    "suite and said so. NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK "
    "OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, "
    "NEITHER MAP TOUCHED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO LINE OF FINDINGS.md EDITED. "
    "NOTHING DEPOSITS; **THE PLATFORM WAS NOT CALLED AT ALL**; 0 BRANCHES TOUCHED, 0 CLONES, 0 "
    "BUILDS, 0 INSTRUMENT RUNS, NO .lean FILE TOUCHED. THE INSTRUMENT LANE AND THE INSTRUMENT-AUDIT "
    "LANE STAY PARKED. THE WAVE STAYS PARKED. M-2 REMAINS (SPECIFIED-NOT-STATED). THE FOUR OPEN "
    "LISTS ARE RESTATED OPEN BY NAME. **A FOLD OPENS AND CLOSES NOTHING: THE CLAUSE HAS NOT MOVED "
    "AND (Q400) IS NOT OPENED.** h2 stands exactly where the deposit left it.")


def corr_rows(Q):
    m = ("**THE ARTEFACT ARC FOLDED, b385-b401: SEVENTEEN ACTS, AND IN NINE OF THEM THE FINDING WAS "
         "THAT A LIMIT ALREADY ON THE RECORD WAS AN ARTEFACT OF HOW IT HAD BEEN MEASURED** (b402, "
         "the fold)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE THE FOLD WAS WRITTEN**, chained on b378's "
            "gate run as b402 -- %d gates read, %d checked by digest. The span is the counter's and "
            "not the seat's: last fold b371-b383 filed by b384, so the span starts at b385, this "
            "act is not in its own fold, and the fold covers **b385-b401, %d ACTS** against a "
            "threshold of %d ruled at b366 as (R1). **THE NAVIGATOR'S COUNT WAS %d AND IS REFUTED "
            "BY ONE SUBTRACTION**, printed beside the tool's. **AND THE COUNTER'S OWN THRESHOLD "
            "LINE IS STALE** -- a DATED ARM, ROUTED not repaired. **%d OF %d HEADLINES LOCATED BY "
            "THE ANCHOR TOOL IN THEIR OWN ACTS' BANKS, %d MISSING**, and F-NOGRADE would have "
            "refused the section entirely had one failed. FINDINGS.md APPENDED TO and never edited: "
            "the pre-act file and the pre-act committed blob are both true prefixes. The section "
            "carries the arc's one statement with its SCOPE beside it, the act-by-act table, the "
            "corrections table, the defective-bars table, and the seats' own defects **REACHING THE "
            "LAST TWO ACTS OF THE SPAN**. %d GRADES MOVED, %d ROWS PAID, %d LINES EDITED, %d "
            "COORDINATES CLOSED"
            % (LG['gates_read'], LG['face_subject_gates'], FD['acts'], FD['threshold'],
               FD['navigator_claim'], FD['located'], FD['located'] + FD['missing'], FD['missing'],
               0, 0, 0, 0))
    term = ("### NO TERMINAL IS CLAIMED BY THIS LEG AND NONE IS OPENED. ### A FOLD IS A SUMMARY OF "
            "ITS ACTS AT THEIR OWN GRADES: IT PROVES NOTHING, DISCHARGES NOTHING, OPENS NOTHING "
            "AND MOVES NO GRADE. ### NO INSTRUMENT WAS RUN, NO KERNEL BUILT, NO OBJECT RECOMPUTED "
            "AND NO .lean FILE TOUCHED")
    prof = ("### NO AXIOM PROFILE IS ASSERTED OR RECOMPUTED. ### NO GRADE MOVED OR CONFERRED, NO "
            "FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS "
            "RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST "
            "CLOSED, NO FACE ROW EDITED. ### THE CORPUS WRITES ARE ONE APPENDED SECTION IN "
            "FINDINGS.md AND ONE APPEND-ONLY TRAIL BLOCK -- 0 LINES EDITED, 0 CONTENT LOST")
    grade = ("### THE SPAN IS READ FROM A COUNTER THAT READS AND DOES NOT WRITE, AND THE GENERATOR "
             "REFUSES IF ITS OWN ACT LIST DISAGREES WITH IT. ### THE THRESHOLD IS READ FROM THE "
             "RULING AND NOT FROM THE COUNTER, WHOSE LINE ON IT IS STALE AND IS PRINTED AS STALE. "
             "### EVERY HEADLINE IS LOCATED BY THE ANCHOR TOOL IN THE BANK OF THE ACT IT IS "
             "ATTRIBUTED TO, AND NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT. ### THE "
             "NAVIGATOR'S COUNT IS PRINTED BESIDE THE TOOL'S AND SCORED RATHER THAN REPLACED. ### "
             "AND THE SEAT-DEFECT TABLE REACHES THE TWO MOST RECENT ACTS, BECAUSE A DEFECT TABLE "
             "THAT STOPS SHORT OF THE PRESENT IS A TABLE THAT FLATTERS IT")
    status = ("data/b402_the_fold.txt; data/b402_fold_notes.txt; data/b402_span_notes.txt; "
              "data/b402_registration_2026-09-10.txt (LOCKED before the fold was written at sha256 "
              "%s, chained on tools/b378_lockgate.py run as b402); tools/b402_fold.py; "
              "tools/b402_regspec.py; tools/b402_reg_gate.py; tools/b402_desk_bank.py; "
              "tools/b402_checks.py; PLACE-papers FINDINGS.md (one appended section) and "
              "OPEN_TRAILS.md (one append-only block); CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what did the span b385 to b401 put on the board',
           'is the fold due and at what count',
           'what is the fold threshold and who ruled it',
           'which acts of the span found an artefact rather than a limit',
           'did the navigator count the span correctly',
           'what defects did the seats declare in this span')
MUST_NOT_HIT = ('the fold proved something', 'a grade was moved by the fold',
                'the clause moved', 'the span was typed by the seat',
                'findings was edited')

KEY = 'the-artefact-arc-folded'


def do_key(rownum):
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b402 FOLDED THE SPAN b385-b401 INTO FINDINGS.md AS **THE ARTEFACT ARC**, PURELY ADDITIVE. "
        "THE COUNT IS THE TOOL'S AND NOT THE SEAT'S: the last fold covered b371-b383 and was filed "
        "by b384, so the span starts at b385; this act is b402 and IS NOT IN ITS OWN FOLD; the fold "
        "covers **17 ACTS** against a threshold of **NINE**, ruled by the author at b366 as (R1). "
        "**THE NAVIGATOR'S COUNT WAS SIXTEEN AND IS REFUTED BY ONE SUBTRACTION**, printed beside "
        "the tool's rather than quietly replaced. **AND THE COUNTER'S OWN THRESHOLD LINE IS "
        "STALE**: b363_span.py prints THERE IS NO DECLARED THRESHOLD IN THE RECORD and carries "
        "threshold_declared: false -- true when b363 wrote it, false since b366. A DATED ARM, "
        "ROUTED and not repaired; the fold reads the threshold from the ruling and says where it "
        "got it. **17 OF 17 HEADLINES LOCATED BY THE ANCHOR TOOL IN THEIR OWN ACTS' BANKS, 0 "
        "MISSING**, F-NOGRADE refusing the section entirely had one failed, and no act quoted from "
        "a later act's summary of it. **THE ARC'S ONE STATEMENT: in nine of the seventeen acts the "
        "finding was that a limit, a count, an absence or a version already on the record was an "
        "ARTEFACT OF HOW IT HAD BEEN MEASURED -- and in the four mathematical acts that close the "
        "span the limit was REAL, and the work became stating it exactly.** The two halves are the "
        "same lesson at two scales: a limit reported by an instrument is a property of the "
        "instrument until a second shape has been tried, and the mathematical half tried a second "
        "shape and the limit held. The section carries the statement WITH ITS SCOPE BESIDE IT, the "
        "act-by-act table, the corrections table, the defective-bars table, and the seats' own "
        "declared defects **REACHING b400 AND b401** -- a defect table that stops short of the "
        "present is a table that flatters it.")
    grade = (
        "### A FOLD PROVES NOTHING, DISCHARGES NOTHING, OPENS NOTHING AND MOVES NO GRADE. ### NO "
        "INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED. ### FINDINGS.md IS APPENDED "
        "TO AND NEVER EDITED: the pre-act FILE and the pre-act COMMITTED BLOB are both true "
        "prefixes of the result, 0 lines edited and 0 content lost. ### NO GRADE MOVED OR "
        "CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, "
        "NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO "
        "LIST CLOSED. ### THE SPAN CAME FROM A COUNTER THAT READS AND DOES NOT WRITE, AND THE "
        "GENERATOR WOULD HAVE REFUSED HAD ITS OWN ACT LIST DISAGREED. ### NOTHING DEPOSITS AND THE "
        "PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED. ### "
        "M-2 UNCHANGED")
    where = (
        "data/b402_the_fold.txt; data/b402_fold_notes.txt; data/b402_span_notes.txt; "
        "data/b402_registration_2026-09-10.txt (LOCKED before the fold was written, chained on "
        "tools/b378_lockgate.py run as b402 -- %d gates read, %d checked by digest); "
        "tools/b402_fold.py; tools/b402_regspec.py; tools/b402_reg_gate.py; "
        "tools/b402_desk_bank.py; tools/b402_checks.py; PLACE-papers FINDINGS.md and "
        "OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b402 (the artefact arc folded: seventeen acts, nine of them finding an artefact where a '
           'limit had been reported, and four finding the limit real)')
    row_new = ('    # ### THE ARTEFACT ARC FOLDED (b402).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where, chr(10)))
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
        rec('    %-56s reaches the b402 key : %s' % (qq, g2))
    for lbl, cond in (
            ('the span and its bounds', 'b385-b401' in out),
            ('the count is the tool`s', "THE COUNT IS THE TOOL'S" in out),
            ('the folding act is excluded', 'IS NOT IN ITS OWN FOLD' in out),
            ('the threshold and its ruling', 'ruled by the author at b366 as (R1)' in out),
            ('the navigator`s claim is scored', 'REFUTED BY ONE SUBTRACTION' in out),
            ('the counter`s own line is stale', "COUNTER'S OWN THRESHOLD LINE IS STALE" in out),
            ('F-NOGRADE is mechanical', '17 OF 17 HEADLINES LOCATED' in out),
            ('the arc statement', 'ARTEFACT OF HOW IT HAD BEEN MEASURED' in out),
            ('and the half where the limit was real', 'the limit was REAL' in out),
            ('the scope stands beside it', 'WITH ITS SCOPE BESIDE IT' in out),
            ('the defect table reaches the present', 'REACHING b400 AND b401' in out),
            ('a fold proves nothing', 'A FOLD PROVES NOTHING' in out),
            ('findings was appended to and not edited', '0 lines edited' in out)):
        ok = ok and cond
        rec('    %-56s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank(Q, rownum, kok):
    B = []
    BAR, SUB = '=' * 100, '-' * 100

    def A(s=''):
        B.append(s)

    A(BAR)
    A('b402 -- THE FOLD, IF DUE, AS ITS OWN ACT. ### THE BANK.')
    A('### Ferry part 1 of 1, receipt confirmed IN FULL (Rule 1). ### 2026-09-10.')
    A('### LEG 2 OF A TWO-LEG SORTIE. ### CONCURRENCY: SOLO (research seat).')
    A('### The face was LOCKED before the fold was written, at sha256 `%s`.' % SEALHASH)
    A(BAR)
    A('')
    A(SUB)
    A('### THE VERDICT.')
    A(SUB)
    A('### ### ### **THE FOLD IS DUE AND IS WRITTEN: ### `%s`, ### `%d` ACTS.**'
      % (FD['title'], FD['acts']))
    A('### ### ### **THE NAVIGATOR`S COUNT WAS `%d`. ### THE TOOL`S IS `%d`. ### THE TOOL '
      'GOVERNS.**' % (FD['navigator_claim'], FD['acts']))
    A('')
    A(SCOPE)
    A('')
    A(SUB)
    A('### THE COUNT, PRINTED SO A READER CAN REDO IT.')
    A(SUB)
    A('###   `the last fold                 : %s, b%d-b%d (%d acts)`'
      % (SP['last_fold']['title'], SP['last_fold']['lo'], SP['last_fold']['hi'],
         SP['last_fold']['acts']))
    A('###   `filed by                      : b%d`' % SP['filed_by'])
    A('###   `so the span starts at         : b%d`' % SP['span_starts_at'])
    A('###   `this act                      : b%d  -- NOT IN ITS OWN FOLD`' % SP['this_act'])
    A('###   `so the fold covers            : b%d-b%d`' % (FD['lo'], FD['hi']))
    A('###   `which is                      : %d acts`' % FD['acts'])
    A('###   `the threshold, (R1) at b366   : %d`' % FD['threshold'])
    A('###   `the navigator`s claim         : %d`' % FD['navigator_claim'])
    A('### ### **`%d >= %d`, SO THE FOLD IS DUE. ### AND `%d != %d`, SO THE CLAIM IS REFUTED.**'
      % (FD['acts'], FD['threshold'], FD['navigator_claim'], FD['acts']))
    A('')
    A(SUB)
    A('### WHAT THE LEG WROTE, AND WHAT IT DID NOT.')
    A(SUB)
    A('### **THE FOLD** ### -- one section appended to `FINDINGS.md`; ### **`%d` OF `%d` HEADLINES'
      % (FD['located'], FD['located'] + FD['missing']))
    A('### LOCATED BY THE ANCHOR TOOL IN THEIR OWN ACTS` BANKS, `%d` MISSING** -- and `F-NOGRADE`'
      % FD['missing'])
    A('### would have refused to write the section AT ALL had one failed. ### **`0` LINES OF')
    A('### ### `FINDINGS.md` EDITED**, the pre-act file and the pre-act committed blob both true')
    A('### prefixes of the result.')
    A('### **THE TRAILS LEDGER** ### -- one append-only block.')
    A('### **THE DESK** ### -- `%d` items swept, `%d` closed, `%d` standing, `%d` lists closed.'
      % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
    A('### **THE GATE CHAIN** ### -- `%d` gates read, `%d` passing, `%d` checked by digest.'
      % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    A('### **THE ROW AND THE KEY** ### -- correspondence row `%d`; index key `%s` : %s.'
      % (rownum, KEY, 'PASS' if kok else 'FAIL'))
    A('')
    A(SUB)
    A('### THE ONE THING THIS LEG FOUND THAT IT WAS NOT LOOKING FOR.')
    A(SUB)
    A('### **THE SPAN COUNTER`S OWN LINE ON THE THRESHOLD IS STALE.** ### `b363_span.py` prints')
    A('### ### *AND THERE IS NO DECLARED THRESHOLD IN THE RECORD -- these are the folds that')
    A('### happened, not a rule anyone wrote down*, and its JSON carries `threshold_declared:')
    A('### false`. ### **THAT WAS TRUE WHEN `b363` WROTE IT AND HAS BEEN FALSE SINCE `b366` RULED')
    A('### ### `(R1)`.** ### A DATED ARM -- `b364`s species, right when written and dated by')
    A('### construction -- ### **AND IT IS THIS SPAN`S OWN SPECIES SHOWING UP IN THE INSTRUMENT')
    A('### ### THAT MEASURES THE SPAN.** ### **ROUTED, NOT REPAIRED:** ### this leg reads the')
    A('### threshold from the ruling and prints where it got it.')
    A('')
    A(SUB)
    A('### WHAT THIS LEG DOES NOT SAY.')
    A(SUB)
    A('### It does not prove, discharge or open anything. ### **A FOLD IS A SUMMARY OF ITS ACTS AT')
    A('### ### THEIR OWN GRADES.**')
    A('### It does not claim the arc`s one statement is true of the object -- ### **ONLY OF WHAT')
    A('### ### THE SPAN PUT ON THE BOARD**, and the scope sentence stands beside it in the section.')
    A('### It does not repair the counter, `b321`s convention split, or `SIDE-window`s README.')
    A('### It does not close a list, move a grade, or touch a map.')
    A('### ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED AT ALL. ### h2 STANDS EXACTLY')
    A('### ### WHERE THE DEPOSIT LEFT IT AND THIS LEG MAKES NO CLAIM ABOUT IT IN EITHER')
    A('### ### DIRECTION.**')
    A(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    rec('  ### bank written : %s (%d lines)' % (os.path.basename(BANKOUT), len(B)))


def main():
    bar('=')
    rec('b402 -- THE DESK, THE TRAIL BLOCK, THE ROW, THE KEY AND THE BANK.')
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
    else:
        rec('  ### the b401 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        ao = after.startswith(before)
        rec('  ### bytes %d -> %d ; append-only %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao))
        if not ao:
            rec('  ### HARD FAILURE -- the write was not append-only.')
            run_clock.write(D, 'b402_desk_notes', LINES)
            return 1
    seg = after.split(MARK, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'says_span': 'b385–b401, 17 acts' in low or 'b385–b401' in low,
        'says_tool_governs': 'the tool governs' in low,
        'says_claim_refuted': 'refuted by one subtraction' in low,
        'says_threshold_ruled': '(r1)' in low,
        'says_counter_stale': 'has been false since b366 ruled (r1)' in low,
        'says_located': '17 of 17 headlines located' in low,
        'says_arc_statement': 'artefact of how it had been measured' in low,
        'says_limit_real': 'the limit was real' in low,
        'says_tables': 'the seats’ own defects' in low or "the seats' own defects" in low,
        'says_reaches_present': 'b400 and b401' in low,
        'says_proves_nothing': 'proves nothing, discharges nothing' in low,
    }
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:**')
    for k, v in says.items():
        rec('      %-26s %s' % (k, v))
    if not all(says.values()):
        rec('  ### HARD FAILURE -- the block does not say what the writer claims: %s'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b402_desk_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)

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
        run_clock.write(D, 'b402_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b402_desk_notes', LINES)
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
            run_clock.write(D, 'b402_desk_notes', LINES)
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
    bank(Q, rownum, kok)

    rec()
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### FOLD %d ACTS. ### ROW %d. ### KEY %s. ### BANK '
        'WRITTEN.**' % (Q['items'], Q['closed'], FD['acts'], rownum, 'PASS' if kok else 'FAIL'))
    bar('=')
    run_clock.write(D, 'b402_desk_notes', LINES)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
