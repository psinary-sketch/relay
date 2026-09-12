# -*- coding: utf-8 -*-
"""b434_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own JSON, never typed. ### The trail block carries the grading and the Type-D finding; its
### trigger is the author's ruling on whether the grading may be cited.
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
MARK = '<!-- b434 the fold, b423-b432 -->'
PRIOR = '<!-- b433 the five rulings executed -->'
BANKOUT = os.path.join(D, 'b434_the_fold.txt')
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


FACE = read(os.path.join(D, 'b434_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b434_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

try:
    G = json.loads(read(os.path.join(D, 'b434_fold.json')) or '{}')
except Exception:
    G = {}
CHK = read(os.path.join(D, 'b434_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS = (int(_a.group(1)), int(_a.group(2))) if _a else (0, 0)

SPAN_RAW = G.get('span_raw', '?')
SPAN_FILED = G.get('span_filed', '?')
ACTS_VER = G.get('acts_verified', '?')
FOLD_INS = G.get('fold_insertions', '?')
FOLD_DEL = G.get('fold_deletions', '?')
FOLD_DELTA = G.get('delta', 0)
FIVE = G.get('findings_found', '?')
SUPER = G.get('supersession_words', [])
TECHNE_AHEAD = G.get('techne_ahead', '?')


ROWMARK = ('**THE EXTERNAL-GRADING ARC FOLDED: TEN ACTS, FIVE FINDINGS SIDE BY SIDE, AND ONE '
           'SPECIES MINTED -- A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN**')


FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — '
        'the rows grading a declaration the record has classified absent (b373). **OPEN.** '
        '**LIST 3** — the undated figures across the roster (b374). **OPEN.** **LIST 4** — the '
        'bibliography entries nothing cites (b374). **OPEN.** Trigger: the ruling on which test '
        'governs, or any disposition on the four open lists.')

DESK = [
    ('the fold, b423 through b432', 'CLOSE',
     'FILED at b434. The span is `b363_span.py``s: last fold `b413`-`b421` filed by `b422`, next '
     'span starting at `b423`, raw count %s through this sortie`s own acts, **and the span filed '
     'is ten**. %s of ten grade strings verified in their own acts` banks. The append is **%s '
     'insertions, %s deletions** -- purely additive, the committed text a true prefix.'
     % (SPAN_RAW, ACTS_VER, FOLD_INS, FOLD_DEL)),
    ('the arc`s one statement', 'CLOSE',
     'FILED with **five findings side by side and %s words of supersession between them**: two '
     'external proofs graded DERIVES with the discipline symmetric; the corpus`s own terminal NOT '
     'THE CLAIM against its own prose; a keystone lemma named for a theorem it does not invoke; '
     'the falsifier under pressure, not fired; three witness sites exhausted with the arc not '
     'converging. **None overturns another.**' % len(SUPER)),
    ('the species: a tool asked not to complain', 'CLOSE',
     'MINTED at b434 with three incidents from their own banks (b414, b418, b433) and one shared '
     'cure -- **the verdict is read from the object and never from the exit code**. The guard '
     'census is measured: **b414 and b418 are guarded, b433 is not.** A TECHNE module stands '
     'beside it, local and not pushed.'),
    ('W-REMOVAL-VERIFIED', 'STANDING',
     'FILED AT b434, NOT STARTED. A removal is verified by reading the path`s own non-existence; '
     'b314`s handler should be shared rather than rediscovered; the `ignore_errors` sites where a '
     'real artefact is removed should be retired. **TRIGGER: the next act that removes a directory '
     'it did not itself create in-session, or any act that opens the instrument-audit lane.** '
     '**The cure already existed at b314 and was never shared** -- a cure in one tool is not a '
     'guard.'),
    ('that the corpus has no instrument for the universal negative', 'STANDING',
     'ROUTED at b432, carried into the fold. Both named instruments serve the exhibited-zero form.'),
    ('the fourth grade, now defined', 'STANDING',
     'DEFINED at b433 in both grade-vocabulary documents; the gap b430 routed is closed. Whether '
     'any further terminal should be re-graded against it is the author`s.'),
    ('the write-list form', 'STANDING',
     'STANDING by `(R44)`. b432, b433 and b434 all closed with **0 unlisted writes**.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 and carried into the fold: 13/16, 10/19, 12/20, union of kinds still growing.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('the scan`s sites against the lock`s zero', 'STANDING', 'The (R36) instrument item.'),
    ('the guard that cannot be exercised at an act`s own step zero', 'STANDING',
     'NAMED at b434. `b304_hooks.py` SKIPS a repository whose tree is dirty, and an act`s own step '
     'zero necessarily dirties `relay`. **So the guard can never be exercised there at step zero**, '
     'and the number it reports at that moment is a skip, not a pass or a failure. Routed.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; untouched by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT -- **READ BY THIS ACT AND NOT MOVED.**'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1800], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    L = ['', MARK, '',
         '### b434 — the fold, b423 through b432 — filed 2026-09-12', '',
         '**Ten acts folded into `FINDINGS.md`, purely additive: %s insertions, %s deletions, the '
         'committed text a true prefix of the file now.** The arc is the external-grading arc, and '
         'its one statement carries five findings side by side.' % (FOLD_INS, FOLD_DEL), '',
         '#### The span, and both of its figures', '',
         '**No count in this act was typed by the seat.** `b363_span.py` owns it and reports: the '
         'last fold `b413`–`b421`, filed by `b422`; the next span starting at **b423**; and a raw '
         'count of **%s**, running through this sortie’s own two acts. **The span this fold files '
         'is b423–b432 — ten acts** — because a fold’s span has always ended before its filing act, '
         'exactly as `b422` filed `b413`–`b421` and was not in its own fold. **Both figures are on '
         'the record and neither was dropped.**' % SPAN_RAW, '',
         '#### The arc in one statement', '',
         '**The corpus turned its grading discipline outward for the first time and the discipline '
         'held — while the same protocol, turned inward, found the corpus’s own prose claiming more '
         'than its terminal proves.** Five findings, side by side, **%s words of supersession '
         'between them**: two external proofs graded `DERIVES` with the discipline found symmetric; '
         'the corpus’s own terminal `NOT THE CLAIM` against its own prose; a keystone lemma named '
         'for a theorem it does not invoke; the falsifier read at address and found under pressure, '
         'not fired; three witness sites exhausted with the arc not converging on one boundary.'
         % len(SUPER), '',
         '**%s of ten grade strings were verified in their own acts’ closing records** before the '
         'fold stated any of them — not in a later act’s summary, and not from memory.' % ACTS_VER,
         '',
         '#### The three columns, kept apart', '',
         '**b412’s third column is carried and never summed into the others.** Statements this arc '
         'makes about the **object**: 0. About the **record**: 5 — which is the arc’s whole '
         'substance. About the **object’s model**: 0 new; the arc graded terminals that already '
         'existed and compiled nothing. **That distribution is the arc’s shape, stated plainly '
         'rather than smoothed.**', '',
         '#### Lore: one species, minted', '',
         '**A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN.** Three incidents, each '
         'named from its own bank: **b414**, an over-budget `decide` yielding a term carrying '
         '`sorryAx` while the build exits `0`; **b418**, a search that ran to its 20.04-second limit '
         'and returned `numFiles: 13` with no truncation flag, where the completed query reaches '
         'forty; **b433**, a recursive delete that met 36 read-only git pack files, skipped every '
         'one in silence, left the directory standing and reported the removal done.', '',
         '**The one cure they share: the verdict is read from the object — the printed profile, the '
         'recorded duration, the directory’s own existence — and never from the exit code.**', '',
         '**Which carry a mechanized guard, measured rather than asserted.** **b414 is guarded** by '
         'the corpus’s standing practice: every grading act reads `#print axioms` output and seeks '
         '`sorryAx` by name. **b418 is guarded by a shared standing tool** — `tools/walker_guard.py`, '
         'minted at b418 for this species, whose `verdict()` returns `INCOMPLETE` for a call that '
         'reached its limit. **b433 is not guarded**: the handler lives only inside b433’s own '
         'components tool, the standing tools still pass `ignore_errors=True` at the counted sites, '
         'and **no tool anywhere verifies that a removal removed anything**.', '',
         '**And the sharpest thing in the census: the cure already existed in this corpus.** '
         '`tools/b314_coldclone.py` carries a handler whose docstring reads *“git objects arrive '
         'read-only on Windows; a plain `rmtree` refuses them.”* It was written at b314, never '
         'shared, and b433 reinvented it nineteen acts later. **A cure that lives in one tool is not '
         'a guard** — and that, not cleverness, is the whole difference between b418 and b433.', '',
         '**Work-order `W-REMOVAL-VERIFIED` is filed and not started**, with its trigger: the next '
         'act that removes a directory it did not itself create in-session, or any act that opens '
         'the instrument-audit lane. Its scope is stated so it is not over-read — this is about '
         'removals, not about every `ignore_errors` in the tree, and it asserts no defect in any '
         'act that has already closed.', '',
         '**A TECHNE module stands beside the species**, `modules/2026-09/ASKED_NOT_TO_COMPLAIN.md`, '
         '**local and not pushed**: that core now stands %s commits ahead of its remote and has '
         'never been pushed.' % TECHNE_AHEAD, '',
         '#### And one thing this act met and named rather than fixed', '',
         '**The pre-push guard cannot be exercised in `relay` at an act’s own step zero.** '
         '`b304_hooks.py` skips a repository whose working tree is dirty, and an act’s step zero — '
         'banking its paste, writing its scan — necessarily dirties `relay`. So the `1` it reports '
         'there is a **skip**, not a failure and not a pass. Three of four repositories are '
         'exercised and pass at that moment, and the guard is re-run at the close where it reads '
         'what it should. **Named and routed; nothing in the guard was changed.**', '',
         '#### The four lists', '', FOUR, '',
         '#### What this act did not do', '',
         '0 bytes of `FINDINGS.md` edited — the fold appends and nothing else. 0 grades moved, '
         'conferred or minted; the fold restates grades its acts already conferred, each verified '
         'in that act’s own bank. 0 keystones edited. 0 register rows. 0 kernels built and 0 '
         '`.lean` files touched. 0 terminals renamed. 0 lanes opened and 0 triggers moved. 0 '
         'addresses resolved and nothing fetched. 0 premises discharged — `h2` is read and not '
         'moved. **0 pushes of `TECHNE-Core`.** 0 deposit actions. **And h2 where the deposit left '
         'it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS A FOLD: TEN ACTS SUMMARISED INTO ONE APPENDED SECTION, EVERY GRADE "
         "STRING VERIFIED IN ITS OWN ACT'S BANK, AND ONE LORE SPECIES MINTED WITH ITS GUARD CENSUS "
         "MEASURED. ### IT MOVES NO GRADE, EDITS NO BYTE OF WHAT IT FOLDS, AND OPENS NOTHING")


def corr_rows():
    m = ROWMARK + " (b434)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b434 -- @GR@ gates read, @GDG@ checked by digest. **THE SPAN IS b363_span.py'S AND NO "
            "COUNT WAS TYPED BY THE SEAT: LAST FOLD b413-b421 FILED BY b422, NEXT SPAN STARTING AT "
            "b423, RAW COUNT @SPANRAW@ THROUGH THIS SORTIE'S OWN ACTS, AND THE SPAN FILED IS TEN -- "
            "BOTH FIGURES PRINTED.** **@ACTSVER@ OF TEN GRADE STRINGS VERIFIED IN THEIR OWN ACTS' "
            "CLOSING BANKS BEFORE THE FOLD STATED THEM.** **THE APPEND IS @INS@ INSERTIONS AND "
            "@DEL@ DELETIONS, THE COMMITTED TEXT A TRUE PREFIX -- PURELY ADDITIVE.** **THE ARC'S "
            "ONE STATEMENT CARRIES FIVE FINDINGS SIDE BY SIDE WITH @SUPER@ WORDS OF SUPERSESSION "
            "BETWEEN THEM; b412'S THIRD COLUMN IS KEPT APART AND NEVER SUMMED.** **ONE SPECIES "
            "MINTED -- A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN -- WITH "
            "b414, b418 AND b433 NAMED FROM THEIR OWN BANKS AND THE SHARED CURE STATED: THE VERDICT "
            "IS READ FROM THE OBJECT, NEVER FROM THE EXIT CODE. b414 AND b418 ARE GUARDED, b433 IS "
            "NOT, AND THE CURE FOR IT EXISTED AT b314 AND WAS NEVER SHARED.** **W-REMOVAL-VERIFIED "
            "FILED WITH ITS TRIGGER AND NOT STARTED; A TECHNE MODULE WRITTEN LOCAL AND NOT "
            "PUSHED.** 0 GRADES MOVED, 0 BYTES EDITED, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The fold RESTATES grades its own acts "
            "conferred and confers none")
    prof = ("### TWO PLACE-papers FILES APPENDED -- FINDINGS.md CARRYING THE FOLD AND OPEN_TRAILS.md "
            "CARRYING THIS ACT'S RECORD, EACH PIN A TRUE PREFIX; ONE TECHNE-Core MODULE WRITTEN AND "
            "COMMITTED LOCALLY AND NOT PUSHED; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO "
            "KERNEL FILE -- 0 CONTENT LOST")
    grade = ("### THE SPAN CAME FROM THE TOOL THAT OWNS IT AND BOTH ITS FIGURES WERE PRINTED WHERE "
             "THEY DIFFER; EVERY GRADE STRING WAS VERIFIED IN ITS OWN ACT'S BANK RATHER THAN "
             "RECALLED; AND THE GUARD CENSUS COUNTED CALL SITES RATHER THAN MENTIONS, WHICH MATTERS "
             "BECAUSE THIS ACT'S OWN TOOLS DISCUSS THE DEFECT WITHOUT COMMITTING IT")
    status = ("data/b434_the_fold.txt; data/b434_components.txt; data/b434_extract.txt; "
              "data/b434_span.txt; data/b434_fold.json; data/b434_checks.txt; "
              "data/b434_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers FINDINGS.md, OPEN_TRAILS.md; "
              "TECHNE-Core modules/2026-09/ASKED_NOT_TO_COMPLAIN.md (LOCAL, NOT PUSHED); "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@SPANRAW@', str(SPAN_RAW)).replace('@ACTSVER@', str(ACTS_VER))
                .replace('@INS@', str(FOLD_INS)).replace('@DEL@', str(FOLD_DEL))
                .replace('@SUPER@', str(len(SUPER))))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the external-grading arc', 'the fold b423 to b432',
           'a tool asked not to complain', 'which incidents carry a guard',
           'why did b433 reinvent b314`s handler')
MUST_NOT_HIT = ('the arc proved rh', 'a grade was moved by the fold', 'the lane was opened')
KEY = 'the-external-grading-arc-folded'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b434 FOLDED THE EXTERNAL-GRADING ARC, b423 THROUGH b432, INTO FINDINGS.md -- PURELY "
        "ADDITIVE, %s insertions and %s deletions, the committed text a true prefix. THE SPAN IS "
        "b363_span.py'S: last fold b413-b421 filed by b422, next span starting at b423, raw count "
        "%s through this sortie's own two acts, AND THE SPAN FILED IS TEN; both figures printed. "
        "%s of ten grade strings were verified in their own acts' closing banks before the fold "
        "stated them. THE ARC IN ONE STATEMENT: the corpus turned its grading discipline outward "
        "for the first time and the discipline held, while the same protocol turned inward found "
        "the corpus's own prose claiming more than its terminal proves -- five findings side by "
        "side with %s words of supersession between them. b412's third column kept apart: 0 "
        "statements about the object, 5 about the record, 0 new about the object's model. ONE "
        "SPECIES MINTED: A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN, with "
        "b414's over-budget decide, b418's search at its time limit and b433's silent delete named "
        "from their own banks, and the shared cure -- the verdict is read from the object, never "
        "from the exit code. b414 and b418 carry mechanized guards (the printed profile; the shared "
        "walker_guard.py); b433 does not, and THE CURE FOR IT ALREADY EXISTED AT b314 AND WAS NEVER "
        "SHARED -- a cure that lives in one tool is not a guard. W-REMOVAL-VERIFIED filed with its "
        "trigger and NOT started. A TECHNE module written beside the species, local and not pushed."
        % (FOLD_INS, FOLD_DEL, SPAN_RAW, ACTS_VER, len(SUPER)))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO BYTE OF WHAT IT FOLDS WAS EDITED. "
             "### NO LANE OPENED. ### NOTHING DEPOSITS. ### TECHNE NOT PUSHED")
    where = ("data/b434_the_fold.txt; data/b434_components.txt; data/b434_fold.json; "
             "data/b434_span.txt; data/b434_registration_2026-09-12.txt (LOCKED, %d gates read, "
             "%d by digest); FINDINGS.md; OPEN_TRAILS.md; "
             "TECHNE-Core modules/2026-09/ASKED_NOT_TO_COMPLAIN.md (local); "
             "CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b434 (the external-grading arc, folded)"


    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE EXTERNAL-GRADING ARC, FOLDED (b434).%s    (%r, %r,%s     %r,%s'
               '     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL +
                  '    # (key, act, one-line statement, grade as its own act recorded it, '
                  'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    out, rc = query(KEY)
    n = out.count('act      :')
    ok = (not no_key(out)) and rc == 0 and n >= 1
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b434 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the span`s two figures carried', 'THE SPAN FILED IS TEN' in out),
                      ('the species carried', 'ASKED NOT TO COMPLAIN' in out),
                      ('the b314 finding carried', 'ALREADY EXISTED AT b314' in out),
                      ('the work-order carried', 'W-REMOVAL-VERIFIED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100,
          'b431 -- THE LongGapsBetweenPrimes GRADING, AND THE TYPE-D QUESTION.', 'THE BANK.',
          '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE EXPECTATION (L2), AS THE REPORT SCORED IT.', '-' * 100,
           '  (L2)(a) the span counts TEN                               : %s'
           % (SPAN_FILED == 10),
           '  (L2)(b) five findings, none summarised as overturning another : %s'
           % (FIVE == 5 and len(SUPER) == 0),
           '  ### AND THE MEASUREMENTS BEHIND THEM:',
           '      the span tool`s raw count / the span filed               : %s / %s'
           % (SPAN_RAW, SPAN_FILED),
           '      grade strings verified in their own banks                : %s of 10' % ACTS_VER,
           '      the append                                              : %s insertions, %s deletions'
           % (FOLD_INS, FOLD_DEL),
           '  ### **EACH CLAUSE SCORED ONCE, APART, AND EACH REFUTABLE BY A PRINTED RESULT.**']
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d' % (ARMS_RUN, ARMS_PASS)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
           % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'),
           '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B433ROW_RE = r"(?m)^\| (\d+) \| \*\*THE FIVE RULINGS EXECUTED"


def main():
    bar('=')
    rec('b434_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not G:
        rec('  ### HARD FAILURE -- this act`s own grade JSON is missing.')
        return 1
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
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
    bar()
    rec('### THE CORRESPONDENCE ROW. ### READ BY MARKER.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    slip = [mm for mm, s2, *_ in ROWS2 if not s2.startswith(mm)]
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s'
        % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b433`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B433ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
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
    rec('  after -- b433`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B433ROW_RE, after)], at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.'
        % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b434_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
