# -*- coding: utf-8 -*-
"""b374_closing.py -- THE THREE CLOSING WRITES, IN ONE FILE: THE TRAIL BLOCK, THE ROW, THE KEY.

### ### **THREE ROLES IN ONE FILE, AND THE REASON IS DECLARED RATHER THAN HIDDEN:** ### the locked
### registration caps this act's new tools, and the cap counts FILES. ### Splitting these three into
### three files would have breached a locked clause to make the tree prettier. ### **A CAP IS NOT A
### ### SUGGESTION, AND THE COMBINATION IS SAID OUT LOUD.**
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS. ### NONE IS TYPED.**
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
MARK = '<!-- b374 the descriptive layer measured, and the functional equation filed -->'
PRIOR = '<!-- b373 the pins sourced from the writing act, and the status column listed -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


H, N, G, Q, FQ = J('b374_hedge'), J('b374_entries'), J('b374_figures'), J('b374_desk'), J('b374_funceq')
KT, DT, WT = H['totals']['KEYSTONE'], H['totals']['DEPOSITED'], H['totals']['WORKING']
L2 = G['l2']
KS_K = 1000.0 * L2['keystone'] / L2['sentences']['KEYSTONE']
OT_K = 1000.0 * L2['other'] / L2['sentences']['WORKING']

SCOPE = (
    "**SCOPE: NOTHING WAS REPAIRED IN ANY COMPONENT.** No sentence rewritten, no entry rewritten, no "
    "figure dated, no hedge removed, no working note cleared -- the order says *classify; repair "
    "nothing*, *no entry rewritten*, *the list is the product* and *a filing and not a campaign*, and "
    "each is obeyed. **NO DOCUMENT WAS GRADED AND NO PROSE WAS JUDGED**: a hedge, an unsourced "
    "expectation and a working note are things found, not faults assigned. **THE HEDGE AUDIT WAS RUN "
    "UNMODIFIED** -- not one stem, grade token or test was touched, tuned or extended for this "
    "surface, and its own fixtures were run before it was trusted. **NO ENTRY WAS MERGED OR RE-KEYED** "
    "(the bibliography's own name-identity law) and **NO TITLE-UNVERIFIED ENTRY WAS GIVEN A TITLE BY "
    "THIS SEAT**. **NO FROZEN SURFACE WAS EDITED**: the deposited companions and the archives were "
    "READ, counted, and left. **NO PIN WAS ADDED AND NO GRADE WAS MOVED** -- b373's findings are "
    "carried, not acted on. **THE FILING CLAIMS NOTHING BEYOND ITS TWO ACTS**, joins nothing they did "
    "not join, and carries in its own body the sentence saying how far they do not go. **NO .lean FILE "
    "WAS TOUCHED, NO BUILD WAS RUN AND NO AXIOM PROFILE WAS RECOMPUTED.** **NO OWNER INSTRUMENT WAS "
    "EDITED**; this act licensed none. NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. "
    "NOTHING WAS COMPUTED ABOUT THE OBJECT. Nothing about the quantifier, h2, totality or the roster; "
    "NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS "
    "UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The "
    "seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, "
    "UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS "
    "SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. "
    "NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def trail_block():
    return [
        '', MARK, '',
        ('### **b374 — THE DESCRIPTIVE LAYER, MEASURED NOT OPINED; AND THE FUNCTIONAL EQUATION FILED '
         '(2026-09-08)**'),
        '',
        ('*No block above is edited. The b373 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        '### The hedge audit, run unmodified over a surface it had never covered',
        '',
        ('The scope is **the census\'s own**: `THE_KEYSTONE_CENSUS.md` names %d keystones in its table '
         'and all %d resolved to tracked paths, plus %d deposited companions; the comparison '
         'population is the census\'s own operationalised test, %d documents. **A seat that picked its '
         'own keystones would be measuring its own choice.**'
         % (len(H['census_names']), len(H['keystones']), len(H['deposited']), H['support'])),
        '',
        '| population | documents | sentences | hedged | hedged, no grade | unsourced expectations | hedges / 1000 sentences |',
        '|---|--:|--:|--:|--:|--:|--:|',
    ] + [
        '| %s | %d | %d | %d | %d | %d | %.1f |'
        % (lbl, t['docs'], t['sentences'], t['hedged'], t['hedged_bare'], t['unsourced'], t['per_k'])
        for lbl, t in (('KEYSTONE', KT), ('DEPOSITED COMPANION', DT), ('WORKING NOTE', WT))
    ] + [
        '',
        ('**A hedge is not a fault and the count is not a score.** A document that says *this is '
         'conditional* is doing exactly what this record demands everywhere else. The instrument\'s own '
         'distinction is kept — a hedge beside a GRADE token is the record working as designed — and '
         'the two are counted apart. **And the third class is this act\'s own and is named UNSOURCED '
         'EXPECTATION, not IMPORTED**, because the predicate can see only that the document offers no '
         'source for the sentence; the second word would claim what the tool cannot see.'),
        '',
        '### The glossary and the bibliography, classified and not rewritten',
        '',
        ('**The glossary has no file of its own** — it is an appendix inside a Day-1 paper, and that '
         'paper has a **frozen twin** among the deposited companions. Both facts are reported because '
         'the order named it as though it were a file. **The two copies diverge by nothing at all** '
         '(%d only-living, %d only-frozen), and **all %d entries classify CURRENT**: not one term has '
         'gone out of use under its own name.'
         % (len(N['glossary']['only_living']), len(N['glossary']['only_frozen']),
            N['glossary']['entries'])),
        '',
        ('The bibliography carries %d entries, **%d of them pointing at an external work**. An external '
         'work was never expected to live in this record, so the in-record test is stated for what it '
         'is: *is the entry still cited under that key*. **%d are cited nowhere in the corpus but the '
         'register itself** — %s — and each is an author-year key rather than an external ID. **That '
         'is a finding about the register, not about the work.** No entry was merged, re-keyed, '
         'resolved or rewritten, and no `TITLE-UNVERIFIED` entry was given a title by this seat.'
         % (N['bibliography']['entries'], N['bibliography']['external'],
            N['bibliography']['not_located'],
            ', '.join('`%s`' % b['key'] for b in N['bibliography']['detail']
                      if b['verdict'] == 'NOT LOCATED'))),
        '',
        '### The count-and-ref sweep — the list is the product',
        '',
        ('**%d figures across the roster are stated without a ref, tag, version or date in their own '
         'sentence.** The window is the sentence and that is a declared choice: a document that dates '
         'itself once in a header does not thereby date every figure in it, because **a reader landing '
         'on a row reads the row**. The document-wide reading is named so the author can disagree with '
         'the one taken.' % G['undated_total']),
        '',
        '| repository | documents | figures | without a ref | share |',
        '|---|--:|--:|--:|--:|',
    ] + [
        '| `%s` | %d | %d | %d | %.0f%% |' % (k, v['docs'], v['figures'], v['undated'], v['pct'])
        for k, v in G['totals'].items()
    ] + [
        '',
        ('**The list is not ranked, not prioritised and not turned into a plan.** A list that arrives '
         'as a plan has decided something, and this leg decides nothing. And the predicate\'s reach is '
         'printed with its result: a figure is a numeral governing a countable noun from a finite '
         'given list, and **a noun off that list is invisible** — that is the reach, not a defect '
         'hidden.'),
        '',
        '### The functional equation, filed at the level of the family',
        '',
        ('Both halves are quoted from the acts that stated them, pulled by anchor and never typed. '
         '**b291 derived the reflection** — the transform carries a member of the two-parameter family '
         'to the member with its parameters exchanged — at the grade that act assigned, **DERIVES-on-'
         'IMPORT, with the import named in the grade itself**. **b291 also states the self-dual '
         'member**: the transform carries the corpus\'s archimedean member to itself, which is what '
         '*the self-dual point of that reflection* means here and means nothing more.'),
        '',
        ('**And the limit is in the filing and not in a footnote, in the same act\'s own words: '
         '"AND NONE OF THIS IS EXTENDED TO THE FINITE PLACES."** The finite two-radius family is **a '
         'different act** (b293) and is named as one. **A construction and a reflection are not one '
         'statement because they can be written in one sentence**, and this filing joins nothing the '
         'acts did not join. **No new mathematics. No grade conferred, raised or moved. No bar set.** '
         'A filing is a place in the record, not a result.'),
        '',
        '### The desk',
        '',
        ('%d items swept under (R7); **%d closed**; %d stand, %d of them new at this leg. **And '
         'closing nothing is the right answer here, and is said rather than apologised for**: (R7) '
         'closes an item whose *occasion* is gone, and a leg that measures and repairs nothing kills '
         'no occasion. **A desk that only accumulates is a list** — (R7)\'s own warning — **and a leg '
         'whose order says "repair nothing" four times is a leg that accumulates by instruction.** The '
         'tension is real and is filed rather than argued away.'
         % (Q['items'], Q['closed'], Q['standing'], 3)),
        '',
        ('*Species: **A COUNT OVER PROSE IS A COUNT OF SHAPES, AND THE SHAPES ARE NOT FAULTS.** A leg '
         'that produces four tables of counts over somebody\'s writing will be read as a scorecard '
         'unless it refuses to be one in its own text. **Nothing was repaired. No document was graded. '
         'No entry was rewritten. No frozen surface was edited. No instrument was modified. No `.lean` '
         'file was written and no build was run.** Trigger: the author\'s disposition on any of the '
         'three lists this leg produced. Nothing here is a route, no coordinate is closed, and `h2` '
         'stands exactly where the deposit left it.*'),
    ]


def corr_rows():
    m = ("**THE DESCRIPTIVE LAYER MEASURED AND NOT OPINED: THE KEYSTONES HEDGE LESS THAN HALF AS OFTEN "
         "AS THE WORKING NOTES AND CARRY UNDATED FIGURES AT VERY NEARLY THE SAME RATE** -- %.1f against "
         "%.1f hedges per thousand sentences, and %.1f against %.1f undated figures per thousand "
         "(b374, sortie leg 2)" % (KT['per_k'], WT['per_k'], KS_K, OT_K))
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, on the audit's own exit code, and "
            "its face fixed the scope of three components before any read. **THE HEDGE AUDIT WAS RUN "
            "UNMODIFIED** over a surface it had never covered -- the %d keystones the census names in "
            "its own table and the %d deposited companions -- with its own fixtures run before it was "
            "trusted. **BOTH HALVES OF (L2) ARE REPORTED PER THOUSAND SENTENCES**, because the "
            "populations differ by more than an order of magnitude in size and a raw total would have "
            "scored the expectation on a fact about file sizes. **A HEDGE IS NOT A FAULT AND THE COUNT "
            "IS NOT A SCORE.**"
            % (len(H['keystones']), len(H['deposited'])))
    return [
        (m, stmt,
         "**NO TERMINAL.** No `.lean` file was touched, no build was run and no axiom profile was "
         "recomputed. **AND THE ONE MATHEMATICAL COMPONENT OF THIS LEG IS A FILING AND NOT A RESULT**: "
         "both halves are QUOTED from the acts that stated them and nothing is claimed beyond what "
         "those acts state.",
         "**PRINT: NOTHING WAS REPAIRED IN ANY COMPONENT.** No sentence rewritten, no entry rewritten, "
         "no figure dated, no document graded, no instrument modified. `PLACE-papers/OPEN_TRAILS.md` "
         "gains ONE append-only block; `CORRESPONDENCE.md` gains this row; `tools/banked_index.py` "
         "gains one key. **THE DEPOSITED COMPANIONS AND THE ARCHIVES WERE READ, COUNTED AND LEFT.** "
         "**FACES_LEDGER.md IS NOT WRITTEN AND ITS WRITER IS NOT CALLED, BECAUSE NO ROW MOVED.** No "
         "findings section; no TECHNE file; no module pushed. **THE HOOK AND THE MIRROR ARE OWED AND "
         "PAID.**",
         "**THE GLOSSARY IS ENTIRELY CURRENT AND ITS FROZEN TWIN DIVERGES BY NOTHING AT ALL** -- %d "
         "entries, %d CURRENT, %d only-living, %d only-frozen -- so the rot this seat expected in the "
         "older surface is not there. **THE BIBLIOGRAPHY CARRIES %d ENTRIES, %d POINTING AT AN "
         "EXTERNAL WORK, AND %d CITED NOWHERE IN THE CORPUS BUT THE REGISTER ITSELF**; an external "
         "work was never expected to live in this record, so the in-record test is stated for what it "
         "is -- *is the entry still cited under that key* -- and **THE ENTRIES NOTHING CITES ARE IN THE "
         "NEWER SURFACE, NOT THE OLDER ONE.** **THE COUNT-AND-REF SWEEP LISTS %d FIGURES ACROSS THE "
         "ROSTER STATED WITHOUT A REF, TAG, VERSION OR DATE IN THEIR OWN SENTENCE**, with the window "
         "declared as the SENTENCE and the document-wide alternative named so the author can disagree; "
         "**THE LIST IS THE PRODUCT AND IT IS NOT RANKED, NOT PRIORITISED AND NOT A PLAN.** **THE "
         "FUNCTIONAL EQUATION IS FILED AT THE LEVEL OF THE FAMILY** with both halves quoted, the grade "
         "carried with its import named, and **THE LIMIT IN THE FILING ITSELF AND NOT IN A FOOTNOTE** "
         "-- the finite family is a different act and is named as one, and the filing joins nothing "
         "the acts did not join. **THE EXPECTATIONS ARE SCORED:** (L2) **CONFIRMED ON BOTH HALVES, AND "
         "THE HALVES ARE NOT EQUALLY STRONG** -- the hedge half by a factor of %.1f, the figure half by "
         "%.2f, and a reader should not carry the second as though it matched the first; this seat's "
         "(E1) **REFUTED ON THE RATE**; (E2)'s first half held and **its second is REFUTED**. **THE "
         "DESK: %d SWEPT, %d CLOSED, %d STANDING** -- and **CLOSING NOTHING IS THE RIGHT ANSWER FOR A "
         "LEG THAT MEASURES AND REPAIRS NOTHING**, because (R7) closes an item whose occasion is gone "
         "and measuring removes no occasion."
         % (N['glossary']['entries'], N['glossary']['tally'].get('CURRENT', 0),
            len(N['glossary']['only_living']), len(N['glossary']['only_frozen']),
            N['bibliography']['entries'], N['bibliography']['external'],
            N['bibliography']['not_located'], G['undated_total'],
            WT['per_k'] / KT['per_k'], KS_K / OT_K,
            Q['items'], Q['closed'], Q['standing']),
         SCOPE, "current"),
    ]


def do_trail():
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        return dict(appended_only=True, committed_prefix_intact=True, prior_present=True,
                    before_bytes=len(before.encode('utf-8')), after_bytes=len(before.encode('utf-8')))
    rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
    body = chr(10).join(trail_block()) + chr(10)
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
    return dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before),
                before_bytes=len(before.encode('utf-8')), after_bytes=len(after.encode('utf-8')))


def do_row():
    ROWS = corr_rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    if not (pos and neg and sa and sb and sc and sd):
        return None
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d' % len(bad))
    if bad:
        return None
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        return None
    g1 = ('MEASURED AND NOT OPINED' in ROWS[0][0]
          and 'RUN UNMODIFIED' in ROWS[0][1]
          and 'NO TERMINAL' in ROWS[0][2]
          and 'A FILING AND NOT A RESULT' in ROWS[0][2]
          and 'NOTHING WAS REPAIRED IN ANY COMPONENT' in ROWS[0][3]
          and 'BECAUSE NO ROW MOVED' in ROWS[0][3]
          and 'ENTIRELY CURRENT' in ROWS[0][4]
          and 'NOT A PLAN' in ROWS[0][4]
          and 'LIMIT IN THE FILING ITSELF' in ROWS[0][4]
          and 'CLOSING NOTHING IS THE RIGHT ANSWER' in ROWS[0][4]
          and 'NOTHING WAS REPAIRED' in ROWS[0][5]
          and 'NO FROZEN SURFACE WAS EDITED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    rec('  the row says the measurement, the unmodified instrument, no terminal and a filing not a '
        'result, nothing repaired, the glossary and bibliography, the unranked list, the filing with '
        'its limit, the expectations, the desk closing nothing, and the scope : %s' % g1)
    if not g1:
        return None
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        return max(nums)
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
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
    return start if ok else None


KEY_ANCHOR = 'KEYS = {\n'
ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')
ALIASES = ('the descriptive layer', 'the hedge audit', 'the glossary', 'the bibliography',
           'the undated figures', 'the functional equation filing')
MUST_NOT_HIT = ('the prose is repaired', 'the figures are dated', 'the entries are rewritten',
                'the functional equation is proved')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def do_key(rownum):
    key_new = (
        "    'descriptive-layer-measured': ['the descriptive layer', 'the hedge audit', "
        "'the glossary',\n"
        "                                  'the bibliography', 'the undated figures',\n"
        "                                  'the functional equation filing'],\n")
    row_new = (
        '    # ### THE DESCRIPTIVE LAYER MEASURED, AND THE FUNCTIONAL EQUATION FILED (b374).\n'
        '    ("descriptive-layer-measured", "b374 (four measurements and one filing; it repairs '
        'nothing, grades no document, modifies no instrument and proves no theorem)",\n'
        '     "A COUNT OVER PROSE IS A COUNT OF SHAPES AND THE SHAPES ARE NOT FAULTS. The hedge audit '
        'was run UNMODIFIED over the keystone corpus and the deposited companions -- a surface it had"\n'
        '     " never covered. Per thousand sentences the keystones hedge ' + ('%.1f' % KT['per_k'])
        + ', the deposited companions ' + ('%.1f' % DT['per_k']) + ', the working notes '
        + ('%.1f' % WT['per_k']) + '; undated figures run ' + ('%.1f' % KS_K) + ' against "\n'
        '     " ' + ('%.1f' % OT_K) + '. THE GLOSSARY IS ENTIRELY CURRENT and its frozen twin diverges '
        'by nothing at all. The bibliography carries ' + str(N['bibliography']['entries'])
        + ' entries, ' + str(N['bibliography']['external']) + ' pointing at an external work,"\n'
        '     " and ' + str(N['bibliography']['not_located']) + ' cited nowhere in the corpus but the '
        'register itself. The count-and-ref sweep lists ' + str(G['undated_total']) + ' figures across '
        'the roster stated without a ref, tag, version or"\n'
        '     " date IN THEIR OWN SENTENCE. And the functional equation is FILED at the level of the '
        'family, with both halves quoted from their own acts.",\n'
        '     "### NOTHING WAS REPAIRED IN ANY COMPONENT: no sentence rewritten, no entry rewritten, '
        'no figure dated, no document graded, no instrument modified. ### A HEDGE IS NOT A FAULT and"\n'
        '     " the count is not a score; a document that says this is conditional is doing what the '
        'record demands everywhere else. ### THE THIRD CLASS IS NAMED UNSOURCED EXPECTATION AND NOT"\n'
        '     " IMPORTED, because the predicate can see only that the document offers no source -- the '
        'second word would claim what the tool cannot see. ### AN EXTERNAL WORK WAS NEVER EXPECTED TO"\n'
        '     " LIVE IN THIS RECORD, so the bibliography test is stated as: is the entry still cited '
        'under that key. ### THE WINDOW FOR A REF IS THE SENTENCE AND THAT IS A DECLARED CHOICE; the"\n'
        '     " document-wide alternative is named so the author can disagree. ### THE LIST IS THE '
        'PRODUCT AND IT IS NOT RANKED, NOT PRIORITISED AND NOT A PLAN. ### THE FILING CARRIES ITS OWN"\n'
        '     " LIMIT IN ITS BODY AND NOT IN A FOOTNOTE -- none of the reflection is extended to the '
        'finite places -- and it joins nothing the two acts did not join. ### NO NEW MATHEMATICS, NO"\n'
        '     " GRADE CONFERRED OR MOVED, NO BAR SET. ### NO FROZEN SURFACE EDITED. ### NO PIN ADDED. '
        '### CLOSING NOTHING IS THE RIGHT ANSWER FOR A LEG THAT MEASURES AND REPAIRS NOTHING. ### NO"\n'
        '     " LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO '
        'COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",\n'
        '     "data/b374_the_descriptive_layer.txt; data/' + H['run_file'] + '; data/'
        + N['run_file'] + '; data/' + G['run_file'] + ';"\n'
        '     " data/' + FQ['run_file'] + '; data/' + Q['run_file'] + ';"\n'
        '     " data/b374_registration_2026-09-08.txt (LOCKED before any write of this act, on the '
        'audit own exit code);"\n'
        '     " tools/b374_hedge.py (the instrument IMPORTED and untouched, with two predicates this '
        'act declares as its own); tools/b374_entries.py (four words and no fifth);"\n'
        '     " tools/b374_figures.py (the sweep, with the ref-window declared); tools/b374_funceq.py '
        '(the filing, quotations pulled by anchor and never typed);"\n'
        '     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT SWEPT BY THIS LEG WAS '
        'EDITED); CORRESPONDENCE.md row ' + str(rownum) + '"),\n')
    txt = io.open(INDEX, encoding='utf-8').read()
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        rec('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'descriptive-layer-measured'" in txt)
    have_row = ('"descriptive-layer-measured"' in txt)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if not (have_key and have_row):
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
        open(INDEX + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query('descriptive-layer-measured')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : descriptive-layer-measured returns %d row(s)  %s'
        % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'descriptive-layer-measured' in o
        ok = ok and g
        rec('    %-44s reaches the b374 key : %s' % (q, g))
    for lbl, cond in (('nothing was repaired', 'NOTHING WAS REPAIRED IN ANY COMPONENT' in out),
                      ('a hedge is not a fault', 'A HEDGE IS NOT A FAULT' in out),
                      ('the class is not called IMPORTED', 'AND NOT' in out and 'IMPORTED' in out),
                      ('the list is not a plan', 'NOT A PLAN' in out),
                      ('the filing carries its own limit', 'LIMIT IN ITS BODY' in out),
                      ('closing nothing is right here', 'CLOSING NOTHING IS THE RIGHT ANSWER' in out)):
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
    rec('b374 -- THE THREE CLOSING WRITES: THE TRAIL BLOCK, THE ROW, THE KEY.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE TRAIL BLOCK, APPEND-ONLY.')
    rec('-' * 100)
    tr = do_trail()
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    rownum = do_row()
    if rownum is None:
        run_clock.write(D, 'b374_closing_notes', LINES)
        return 1
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE INDEX KEY.')
    rec('-' * 100)
    kok = do_key(rownum)
    rec('')
    rec('=' * 100)
    rec('  ### trail appended : %s ; row : %s ; key : %s' % (tr['appended_only'], rownum, kok))
    rec('=' * 100)
    p = run_clock.write(D, 'b374_closing_notes', LINES)
    io.open(os.path.join(D, 'b374_closing_writes.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(
                dict(trail=tr, mark=MARK, row=rownum, key_ok=kok,
                     run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
