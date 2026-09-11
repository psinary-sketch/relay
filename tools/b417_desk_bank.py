# -*- coding: utf-8 -*-
"""b417_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **THE AMENDMENT BINDS THIS FILE'S PROSE:** ### the slots and the fifteen are written in separate
### paragraphs and never in one sentence. ### The trail block carries them under separate headings,
### and the correspondence statement keeps its sentence about the Reader's head apart from every
### sentence about the tuples.
### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER** -- `b416`'s row sits at 265 although its closing
### printed 266, and the row this act appends takes 266.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b417 the contradiction put to its owner, and the second tool cleared -->'
PRIOR = '<!-- b416 the two stipulations named, the dated instrument repaired, the reader placed -->'
B416ROW = 'THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM'
BANKOUT = os.path.join(D, 'b417_the_contradiction_put.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


FACE = read(os.path.join(D, 'b417_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b417_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('the formation contradiction', 'STANDING',
     'PUT TO THE AUTHOR AS A DEFECT REPORT under (R34), both halves side by side in their own words. '
     '### **AWAITS THE AUTHOR’S RULING** -- this seat says neither half is wrong.'),
    ('the two readings', 'STANDING',
     'PRICED FROM ARITHMETIC AND QUOTATION, NEITHER ADOPTED. ### Reading (a) makes B equal C and D equal '
     'A -- four named classes become two distinct tuples -- and falsifies classA_distinct_from_classD. '
     '### Reading (b) moves no figure; the weakening is written already in AT_REST: *with connected '
     'reductive symmetry group G*.'),
    ('`tools/b369_hygiene.py`', 'CLOSE',
     '**REPAIRED AND RUN, SNAPSHOT FIRST.** ### Broken, it wrote 0 files. ### Repaired and run against a '
     'captured snapshot, its writes escaped as one object each into three other repositories’ stores, '
     'through the guard exercise it runs two calls deep. ### Live, it rewrote 2 prior-act records and '
     'created 1; all 3 restored, bytes equal to their blobs. ### Its own verdict, FAILED, reported and '
     'not edited.'),
    ('`b369_hygiene.py`’s dated predicates and its dated label', 'STANDING',
     'ROUTED. ### Its wording pairs cannot re-apply and its hook check reads a path no guard runs from; '
     'its printed label still names the retired path. ### None stops it running.'),
    ('the snapshot harness’s restore predicate', 'CLOSE',
     'REPAIRED IN THIS ACT after its first live use reported 2 files differing whose bytes equalled their '
     'blob -- a size-and-mtime compare after a restore. ### The live record is kept as it ran.'),
    ('the unreferenced objects the guard exercise left', 'STANDING',
     'NAMED, NOT COLLECTED: one loose object per run in each of SIDE-global-section, PLACE-papers and '
     'SIDE-effects, across the snapshot and the live run.'),
    ('the residue backups in SIDE-effects', 'CLOSE',
     'SWEPT BY THE RULE AT (E): 2 removed, their bytes a blob present in SIDE-effects’ and relay’s '
     'stores. ### **Content lost : 0.** SIDE-effects clean.'),
    ('the species', 'CLOSE',
     'MINTED AND FILED: TECHNE-Core `modules/2026-09/SAFE_BY_BEING_BROKEN.md`, beside DATED_ARM and '
     'GUARD_WITH_NOTHING_LISTENING, local commit 4aaf600, **NOT PUSHED**. ### Mechanized half: relay '
     '`tools/repair_snapshot.py`, its fixtures passing in both polarities.'),
    ('the Core/ caveats', 'CLOSE',
     'MARKED UNDER THE PREDICATE AT (F): **1 TESTED, 12 UNTESTED**, the kind printed beside each mark. '
     '### Only (T1.4) has been evaluated outside its own evidence, by b414.'),
    ('the (T1.4) annotation', 'STANDING',
     'DRAFTED AT b416 AND NOT APPLIED. ### **AWAITS THE AUTHOR’S APPROVAL.** Unchanged by this act.'),
    ('the example systems two tables place differently', 'STANDING',
     'ROUTED. ### COMPLEX_ANALYSIS and MATTER_AS_ARITHMETIC place the genetic code, Shannon’s system and '
     'Navier-Stokes at different tuples -- a disagreement of another kind, not folded into the first.'),
    ('b416’s closing row number', 'STANDING',
     'ROUTED. ### b416’s desk appended correspondence row 265; its closing printed 266, and the ferry '
     'carried the closing’s figure. ### This act’s own row takes 266.'),
    ('b416’s count of sums inside the Reader’s stretch', 'STANDING',
     'ROUTED. ### b416’s extract computed nine; its registry row and correspondence row say six. ### A '
     'banked record and a registry row are not this act’s to edit.'),
    ('registry row p2-35', 'STANDING',
     'ROUTED. ### It still says *three-clause currency note* and carries the count of six; the head now '
     'carries four clauses under (R33).'),
    ('the Reader’s arithmetic-desert sentence', 'CLOSE',
     '(R33) EXECUTED: the head note grew one clause naming the seven and citing the Reader’s own '
     'predictions section; b416’s three clauses and the body byte-identical.'),
    ('CONSTANCE’s own lattice sentence', 'STANDING',
     'ROUTED. ### It asserts the stretch empty in its own words, and says no combination of powers yields '
     '43, which is 2^4 + 3^3.'),
    ('the Reader’s encoding', 'STANDING', 'ROUTED, NOT REPAIRED, as at b416.'),
    ('`rg` over relay data', 'STANDING',
     'NOTED. ### It returned no `T1.4` line from records that carry five. ### Every search here is by '
     'Python; the cause is not diagnosed by this act.'),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING',
     'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
]


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def do_desk():
    # ### **WRAPPED AT WORD BOUNDARIES, NOT SLICED** -- the inherited fixed-width slice broke words
    # ### mid-token, and this act's BAR 11 forbids it; repaired before this tool first ran.
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1600], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    return [
        '', MARK, '',
        '### b417 — the contradiction put to its owner, and the second tool cleared — filed 2026-09-11', '',
        '#### The slots', '',
        '**The defect report, side by side.** `phase2/physics/MATTER_AS_ARITHMETIC.md` says, in its '
        'abstract and again in section I, that *three of four formation components are universal across '
        'IDS-amenable systems: n₂ = 3 by Chevalley–Steinberg, n₃ = 2 by bipartite complex analysis, n₄ = 0 '
        'by Schur’s lemma*. The kernel declares `classB := (3, 2, 2, 0)` and `classD := (2, 2, 2, 0)`, and '
        'the owner’s own table eleven lines below the sentence agrees with the kernel. **Both halves are '
        'in the owner’s document.** Under (R34) this act does not say which is wrong; the author rules.',
        '',
        '**Who cites what.** Two shapes were run and the second one’s residue was hand-read. **Two live '
        'documents cite the universality sentence** — the owner, and `phase1.5/structural/AT_REST.md`. '
        '**Five cite the disagreeing tuples and not the sentence.** Five more carry the word *universal* '
        'beside the second component and assert something else: a tuple constant across Dedekind zeta '
        'functions, or a formation total invariant across them.',
        '',
        '**The ratio at the four tuples** matches all four figures the kernel’s header prints, and **n₂ '
        '= 2 is load-bearing for both B and D**: with 3 in its place, B’s ratio moves from 9/32 to 1/27 '
        'and D’s from 1/4 to 4/81.',
        '',
        '**What each resolution would move.** Reading (a), the sentence right: B becomes C’s tuple and D '
        'becomes A’s, **so four named classes become two distinct tuples** — the ferry expected two to '
        'become one, and the arithmetic finds two collisions. Five of the kernel’s stated figures move, '
        '`classA_distinct_from_classD` becomes false and could not compile, and D would sit on the Planck '
        'figure at 0.13σ beside A. Reading (b), the tuples right: **no figure moves anywhere**; the '
        'sentence would be weakened to its own theorem’s hypothesis, *connected reductive symmetry '
        'groups*, which AT_REST already writes inline. **Class A’s value, 4/81, is unmoved under both.** '
        'Neither reading is adopted.',
        '',
        '**The expectations about the slots.** (N1)’s count is refuted at two, and its first clause is '
        'the author’s. (N2) is met. (N4) is met in premise — four distinct pairs need the second '
        'component to vary — and not in conclusion: the header is computed from the same declarations, '
        'so it is one half of the contradiction and cannot decide between the halves. (N5) is refuted: '
        'the only document arguing n₄ that asserts the sentence cites all four tuples.',
        '',
        '**The Core/ caveats, marked.** One tested outside its own evidence — (T1.4), by b414 — and '
        'twelve untested, most of them scope disclaimers or library forms with no bounded condition to '
        'leave. (N3) is met, and nearly vacuously.',
        '',
        '#### The tools', '',
        '**The second tool cleared, snapshot first.** `tools/b369_hygiene.py` broke on the path b386 '
        'retired and, broken, **wrote nothing** — measured, not assumed. Repaired and run first against '
        'a captured snapshot, its writes escaped as **one object each into three other repositories’ '
        'stores**, through a guard exercise two calls deep that its own source never names. Live, it '
        'rewrote two prior-act records and created a third; all three were restored. Its own verdict, '
        'FAILED, is reported and not edited. The two backups in SIDE-effects were swept under the stated '
        'rule, **content lost 0**.',
        '',
        '**The species, minted.** *A broken tool is safe by being broken.* Filed as '
        '`SAFE_BY_BEING_BROKEN.md` in TECHNE-Core beside the dated arm and the guard nobody reads, local, '
        'not pushed; mechanized as relay `tools/repair_snapshot.py`. **And the harness found a defect in '
        'itself on its first live use** — a size-and-mtime check after a restore — which was repaired, '
        'with the live record kept as it ran.',
        '',
        '#### The fifteen', '',
        '**The placed Reader’s set against its live use.** All fifteen members are still cited in a '
        'Prime-Core paragraph of a live document; none is dropped. One live document asserts the Reader’s '
        'arithmetic desert, **CONSTANCE, in its own words** — and its own sentence says no combination of '
        'powers yields 43, which is 2^4 + 3^3.',
        '',
        '**(R33) executed.** The Reader’s head note grew one clause: the desert sentence is false, the '
        'seven sums of powers below one hundred that the set excludes are named, and the Reader’s own '
        'predictions section is cited as naming two of them. b416’s three clauses and the body are '
        'byte-identical. The stretch also carries 113 and 131; they are in this act’s record and not in '
        'the clause, which names what the ruling names.',
        '',
        '#### What this act did not do', '',
        '0 `.lean` files touched, 0 builds run, 0 terminals added. 0 grades moved. 0 premises '
        'discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of `FACES_LEDGER.md` '
        'written. 0 folds run. 0 rules struck or amended. 0 orientation-layer lines edited. 0 locked '
        'faces edited. 0 registry rows written. **0 words of the universality sentence or of any tuple '
        'edited. 0 bytes of the Reader’s body edited. 0 sentences of CONSTANCE edited.** 0 commits pushed '
        'from TECHNE-Core. 0 deposit actions, 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A DEFECT REPORT PUT TO ITS OWNER, TWO READINGS PRICED, A TOOL REPAIRED "
         "AND RUN SNAPSHOT FIRST, A SPECIES MINTED, THIRTEEN CAVEATS MARKED AND ONE CLAUSE ADDED TO A "
         "PLACED DOCUMENT'S HEAD. ### IT MOVES NO GRADE, DISCHARGES NO PREMISE, PROVES NOTHING, EDITS "
         "NEITHER HALF OF THE CONTRADICTION AND RULES ON NEITHER")


def corr_rows():
    m = ("**READING (a) WOULD LEAVE TWO DISTINCT TUPLES WHERE THE MODEL NAMES FOUR CLASSES, AND READING "
         "(b) WOULD MOVE NO FIGURE** (b417, the contradiction put to its owner)")
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b417 "
            "-- @GR@ gates read, @GDG@ checked by digest; the survey left 0 anchor misses on its second "
            "run, its first kept. **A READ ACT IN THE KERNEL: 0 .lean files touched, 0 builds run.** "
            "**COMPONENT 1: THE OWNER'S UNIVERSALITY SENTENCE AND THE KERNEL'S TUPLES ARE PUT SIDE BY "
            "SIDE AS A DEFECT REPORT**, both in the owner's own document; under (R34) this seat says "
            "neither half is wrong. **TWO LIVE DOCUMENTS CITE THE SENTENCE AND FIVE CITE THE "
            "DISAGREEING TUPLES WITHOUT IT.** **COMPONENT 2: THE RATIO MATCHES THE HEADER AT ALL FOUR "
            "TUPLES, AND n2 = 2 IS LOAD-BEARING FOR BOTH B AND D.** **(R34): UNDER READING (a) B "
            "BECOMES C AND D BECOMES A, FIVE KERNEL FIGURES MOVE AND classA_distinct_from_classD "
            "BECOMES FALSE; UNDER READING (b) NO FIGURE MOVES; CLASS A'S 4/81 IS UNMOVED UNDER BOTH.** "
            "**COMPONENT 3: b369_hygiene.py REPAIRED AND RUN SNAPSHOT FIRST** -- broken it wrote 0 "
            "files; repaired, its writes escaped as one object each into three other repositories' "
            "stores; live, 3 prior-act records rewritten and 3 restored; its verdict reported, not "
            "edited; 2 backups swept, content lost 0. **COMPONENT 4: 1 CAVEAT TESTED, 12 UNTESTED.** "
            "**ADDITION ONE: THE SPECIES SAFE_BY_BEING_BROKEN MINTED, LOCAL, NOT PUSHED**, mechanized "
            "as tools/repair_snapshot.py. **ADDITION TWO: BOTH READINGS PRICED, NEITHER ADOPTED.** "
            "**COMPONENT 5 AND (R33), A SEPARATE SUBJECT: all fifteen members still cited live, none "
            "dropped; the Reader's head note grew one clause naming the seven, its body byte-"
            "identical.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED, ADDED, RENAMED OR RESTATED. "
            "### THE KERNEL WAS READ AND NOT BUILT. ### classA_distinct_from_classD IS CITED AS THE "
            "KERNEL DECLARES IT, AND THE ACT REPORTS THAT READING (a) WOULD FALSIFY IT -- A PRICE, NOT "
            "A CHANGE")
    prof = ("### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED, NO GRADE MOVED CONFERRED OR "
            "MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO "
            "ROUTE PROPOSED, NO ROW OF FACES_LEDGER WRITTEN, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO "
            "ORIENTATION-LAYER LINE EDITED, NO LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO "
            "REGISTRY ROW WRITTEN. ### NO WORD OF THE SENTENCE OR ANY TUPLE EDITED, NO BYTE OF THE "
            "PLACED BODY EDITED, NO SENTENCE OF CONSTANCE EDITED, NO TECHNE COMMIT PUSHED. ### THE "
            "CORPUS WRITES ARE ONE HEAD CLAUSE, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED "
            "CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### A CONTRADICTION FOUND BY A PREDECESSOR WAS PUT TO ITS OWNER RATHER THAN RESOLVED BY "
             "A SEAT, AND EACH RESOLUTION WAS PRICED FROM ARITHMETIC. ### A CITATION CEILING FROM ONE "
             "MATCHER WAS WIDENED BEFORE IT WAS BANKED, AND THE RESIDUE HAND-READ. ### A NAVIGATOR'S "
             "WITNESS WAS FOUND TO BE THE SAME HALF STATED TWICE. ### A DORMANT TOOL WAS MEASURED "
             "SAFE WHILE BROKEN, THEN REPAIRED AND RUN AGAINST A SNAPSHOT BEFORE IT RAN LIVE, AND ITS "
             "ESCAPED WRITES WERE FOUND TWO CALLS DEEP. ### THE NEW HARNESS FOUND A DEFECT IN ITSELF ON "
             "ITS FIRST LIVE USE AND BOTH ITS FIGURES ARE KEPT. ### A PRIOR RECORD'S COUNT AND A PRIOR "
             "CLOSING'S ROW NUMBER WERE FOUND WRONG AND ROUTED, NOT EDITED")
    status = ("data/b417_the_contradiction_put.txt; data/b417_components.txt; data/b417_extract.txt; "
              "data/b417_snapshot.txt; data/b417_live.txt; data/b417_sweep.txt; data/b417_place.txt; "
              "data/b417_registration_2026-09-11.txt (LOCKED before any write at sha256 %s, chained on "
              "tools/b378_lockgate.py run as b417); tools/b417_extract.py; tools/b417_regspec.py; "
              "tools/b417_reg_gate.py; tools/b417_components.py; tools/b417_desk_bank.py; "
              "tools/b417_checks.py; tools/repair_snapshot.py (NEW); tools/b369_hygiene.py (REPAIRED); "
              "PLACE-papers heritage/PRIME_CORE_READER.md (ONE HEAD CLAUSE), OPEN_TRAILS.md; TECHNE-Core "
              "modules/2026-09/SAFE_BY_BEING_BROKEN.md (LOCAL 4aaf600, NOT PUSHED); CORRESPONDENCE.md row "
              "%%d" % SEALHASH[:16])

    def sub(x):
        return x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
    return [(sub(m), sub(stmt), sub(term), sub(prof), sub(grade), SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('which half of the formation contradiction is wrong',
           'what would each tuple reading move',
           'is n2 load bearing for class b and d',
           'which core caveats have been tested outside their evidence',
           'what did repairing b369 hygiene write',
           'safe by being broken')
MUST_NOT_HIT = ('the author ruled which half is wrong', 'the species module was pushed',
                'the reader body was edited', 'a grade was moved', 'h2 has moved')
KEY = 'the-contradiction-put'


def do_key(rownum):
    statement = (
        "b417 PUT THE CONTRADICTION TO ITS OWNER AND CLEARED THE SECOND TOOL. **THE OWNER'S "
        "UNIVERSALITY SENTENCE AND THE KERNEL'S TUPLES ARE SET SIDE BY SIDE AS A DEFECT REPORT**, both "
        "halves in MATTER_AS_ARITHMETIC; under (R34) **THIS SEAT SAYS NEITHER HALF IS WRONG**. **TWO LIVE "
        "DOCUMENTS CITE THE SENTENCE** (the owner and AT_REST) **AND FIVE CITE THE DISAGREEING TUPLES "
        "WITHOUT IT**. **n2 = 2 IS LOAD-BEARING FOR BOTH B AND D.** **READING (a) MAKES B EQUAL C AND D "
        "EQUAL A -- FOUR NAMED CLASSES BECOME TWO DISTINCT TUPLES -- AND FALSIFIES "
        "classA_distinct_from_classD; READING (b) MOVES NO FIGURE; CLASS A'S 4/81 IS UNMOVED UNDER "
        "BOTH.** **(N4) IS MET IN PREMISE AND NOT IN CONCLUSION: THE HEADER IS THE SAME HALF STATED "
        "TWICE.** **(N5) IS REFUTED.** **b369_hygiene.py WROTE NOTHING WHILE BROKEN**; repaired and "
        "**RUN AGAINST A CAPTURED SNAPSHOT FIRST**, its writes **ESCAPED AS ONE OBJECT EACH INTO THREE "
        "OTHER REPOSITORIES' STORES**; live, three prior-act records rewritten and restored; its verdict "
        "reported, not edited. **THE SPECIES SAFE_BY_BEING_BROKEN IS FILED LOCAL, NOT PUSHED**, "
        "mechanized as tools/repair_snapshot.py, **WHICH FOUND A DEFECT IN ITSELF ON ITS FIRST LIVE "
        "USE**. **ONE CAVEAT TESTED, TWELVE UNTESTED.** The placed Reader's head note grew one clause "
        "under (R33); its body is byte-identical.")
    grade = (
        "### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED. ### NO GRADE MOVED CONFERRED OR "
        "MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO ROUTE PROPOSED, NO "
        "LEDGER ROW WRITTEN, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO REGISTRY ROW WRITTEN. ### "
        "NEITHER HALF OF THE CONTRADICTION EDITED OR RULED ON. ### NOTHING DEPOSITS AND THE PLATFORM WAS "
        "NOT CALLED AT ALL")
    where = (
        "data/b417_the_contradiction_put.txt; data/b417_components.txt; data/b417_extract.txt; "
        "data/b417_snapshot.txt; data/b417_live.txt; "
        "data/b417_registration_2026-09-11.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b417 -- %d gates read, %d checked by digest); "
        "tools/b417_components.py; tools/repair_snapshot.py; tools/b369_hygiene.py; PLACE-papers "
        "heritage/PRIME_CORE_READER.md, OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = ("b417 (the formation contradiction put to its owner with both readings priced and neither "
           "adopted, the second dated tool repaired and run snapshot first, the species minted, the "
           "Core caveats marked, and one clause added to the Reader's head under (R33))")
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE CONTRADICTION PUT (b417).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b417 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('side by side', 'SIDE BY SIDE AS A DEFECT REPORT' in out),
            ('no seat ruling', 'THIS SEAT SAYS NEITHER HALF IS WRONG' in out),
            ('two citers', 'TWO LIVE DOCUMENTS CITE THE SENTENCE' in out),
            ('load-bearing', 'LOAD-BEARING FOR BOTH B AND D' in out),
            ('four become two', 'FOUR NAMED CLASSES BECOME TWO DISTINCT TUPLES' in out),
            ('class A unmoved', "CLASS A'S 4/81 IS UNMOVED UNDER BOTH" in out),
            ('(N4) split', 'THE HEADER IS THE SAME HALF STATED TWICE' in out),
            ('broken wrote nothing', 'WROTE NOTHING WHILE BROKEN' in out),
            ('snapshot first', 'RUN AGAINST A CAPTURED SNAPSHOT FIRST' in out),
            ('escaped two calls deep', "INTO THREE OTHER REPOSITORIES' STORES" in out),
            ('species local', 'FILED LOCAL, NOT PUSHED' in out),
            ('the harness`s own defect', 'FOUND A DEFECT IN ITSELF' in out),
            ('caveats', 'ONE CAVEAT TESTED, TWELVE UNTESTED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    B = ['=' * 100,
         'b417 -- THE CONTRADICTION PUT TO ITS OWNER, AND THE SECOND TOOL CLEARED.', 'THE BANK.',
         '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
          % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s. ### REGISTRY ROWS WRITTEN : 0.'
          % (rownum, 'PASS' if kok else 'FAIL'),
          '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b417_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s notes do not carry its count line.')
        return 1
    rec('')
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    rec('')
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s ; prior text a TRUE PREFIX : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2, t2.startswith(t.rstrip(NL))))
    rec('  lines deleted : 0')
    rec('')
    bar()
    rec('### THE CORRESPONDENCE ROW. ### READ BY MARKER.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s' % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    slip = [mm for mm, s2, _t, _p, _g2, _sc, _st in ROWS2 if not s2.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1
    b416at = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| \*\*' + re.escape(B416ROW), txt)]
    rec('  b416`s row, by its marker, before : %s' % b416at)
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    present = [mm for mm, _s, _t, _p, _g2, _sc, _st in ROWS2 if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(ROWS2[0][0]), txt)][0]
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS2)]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    b416after = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| \*\*' + re.escape(B416ROW), after)]
    mine = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(ROWS2[0][0]), after)]
    rec('  b416`s row, by its marker, after : %s ; this act`s row, by its marker : %s' % (b416after, mine))
    rec('')
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    rec('')
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok)
    rec('')
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b417_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
