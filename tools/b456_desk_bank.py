# -*- coding: utf-8 -*-
"""b456_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure is read off this act's own records -- the
### fold JSON, the span JSON, the lock gate's notes, the suite -- and none is typed.
### ### **THE SUITE GATE, STATED:** this tool runs only if the pre-push suite fails on no arm; the suite is re-run after it and must then
### fail on none before anything is committed.
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
MARK = '<!-- b456 the errata entry, the live note, and the routed annotations completed -->'
PRIOR = '<!-- b455 the deposit`s exhaustiveness claim read against its own route terminal -->'
BANKOUT = os.path.join(D, 'b456_the_errata_and_the_note.txt')
SELF_WRITTEN = set()   # ### no arm of the suite reads an object only this tool writes before the suite runs
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
DESK = []


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


FACE = read(os.path.join(D, 'b456_registration_2026-09-14.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b456_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR_, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
CHK = read(os.path.join(D, 'b456_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+) ?(\[.*\])?', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3))) if _a else (0, 0, -1))
FAILING = set(re.findall(r"'(G-[A-Z0-9-]+)'", _a.group(4) or '')) if _a else {'?'}
COMP = read(os.path.join(D, 'b456_components.txt'))


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


WJ = _j('b456_writes.json')
PJ = _j('b456_profile.json')
SPAN = _j('b456_span.json')
READY = bool(WJ.get('diffs')) and bool(PJ.get('verdict')) and bool(SPAN)
SPANN = SPAN.get('current_span')
VERD = PJ.get('verdict', '')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b456_components as CMP  # noqa: E402

ROWMARK = ('**(R65) IS EXECUTED: ERRATA E-2026-09-14-1 RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5 EXPLAINS WHY THE DEPOSITED DESCRIPTIONS AND THE '
           'ROUTE TERMINAL DIFFER, AND A LIVE NOTE UNDER (R20) STANDS BESIDE THE PIN; THE ROUTE TERMINALS` PROFILE ARTEFACT AT THE TAG IS ABSENT, A '
           'SECOND DEPOSIT-LEVEL MATTER ROUTED AND NOT TAKEN; OF THE ROUTED ITEMS, INVARIANCE COMPLETED, THE RESIDUE IN PART, THE LICENSE LEFT**')
SCOPE = ("### THE ACT APPENDED ONE ERRATA ENTRY UNDER A TALLY RULE AND REQUIRED CONTENT FIXED ON ITS FACE, INSERTED ONE NOTE SENTENCE BESIDE THE PIN "
         "IN REGISTRY AND README, SEARCHED THE DEPOSITED TAG AND THE RECORD FOR A PRINTED PROFILE, AND COMPLETED OR LEFT THE ROUTED ITEMS BY A TEST "
         "ON ITS FACE; NO LEAN RUN, NO ZENODO WRITE, NO LIVE CLAIM NARROWED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('(R65) (i): the ERRATA entry', 'CLOSE', 'WRITTEN at b456: E-2026-09-14-1, deposit-facing, retained at monograph v1.1.2 and SIDE-kernel v1.5; prose, no tally.'),
        ('(R65) (iii): the live note under (R20)', 'CLOSE', 'INSERTED at b456 beside the pin: REGISTRY.md after the deposit-pin table, README.md beside the kernel line; no line changed.'),
        ('(R65) (ii): the live narrowing', 'STAND', 'WAITS ON THE WAVE, which is parked, as ruled.'),
        ('the route terminals` profile at v1.5', 'STAND', 'VERDICT %s: the tag ships the v1.2 print and check scripts only; the front door`s "re-profiled clean at the v1.5 enactment" and the record`s "All route terminals report" rest on a run whose output nobody shipped. ROUTED as a second deposit-level matter; its disposition (print and bank at the tag, in a lane that permits a lean run) priced and NOT TAKEN.' % VERD),
        ('I1 INVARIANCE_BARRIERS, the T3 Tier-1 scope', 'CLOSE', 'COMPLETED at b456: era annotation beside OPEN_TRAILS-archive-2:7971.'),
        ('I3 THE_RESIDUE_OF_RH:145, held-branch work', 'CLOSE', 'COMPLETED at b456: merged-branch work, the line preserved in a currency annotation.'),
        ('I3 THE_RESIDUE_OF_RH:127-130, HELD-BRANCH cells', 'STAND', 'LEFT FOR A RULING: lines (R63)(a) did not name.'),
        ('I2 EXHAUSTIVENESS_LICENSE:9, the head`s version line', 'STAND', 'LEFT FOR A RULING: a line (R63)(a) did not name, dated at its own version.'),
        ('the seat`s error at b456', 'STAND', 'ENTERED: the satisfiability spec carried from b455 kept "annotations written by this act, cap 0", contradicting the face`s reading (4); the face governed; the stamped record was not re-run.'),
        ('W-ORD-MATCHER-SHAPE', 'STAND', 'OPEN; the tally rule caught the seat`s own first draft (ordinals, "one", "single"), rewritten before any write.'),
        ('W-ORD-MIRROR-ZIP-NAME', 'STAND', 'OPEN; this act`s build passes -DateTag 2026-09-14-b456.'),
    ]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1900], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    body = [
        '### b456 — the errata entry, the live note, and the routed annotations completed — filed 2026-09-14',
        '',
        '**Ruling `(R65)`, the author’s, ratified by the paste and strikeable, is executed.** Dispositions (i) and (iii) are taken, not (ii). `ERRATA.md` carries **E-2026-09-14-1**, retained at monograph v1.1.2 and SIDE-kernel v1.5. A live note under `(R20)` stands beside the pin. The live narrowing waits on the wave, and no Zenodo metadata is edited. **The route terminals’ profile artefact at the deposited tag is @VERD@** — a second deposit-level matter, routed and not taken. Of the routed items, INVARIANCE_BARRIERS is completed, THE_RESIDUE_OF_RH in part, and EXHAUSTIVENESS_LICENSE is left. Nothing deposits; no `lean` was run.',
        '',
        '#### Component 1 — the entry',
        '',
        'The entry explains, in prose, why the deposited words and the terminal differ. The record description and the kernel README say the seven-class catalogue’s exhaustiveness is proved and machine-checked. `structural_exhaustiveness_proved` unfolds to the cardinality seven of a type the kernel defines, a per-constructor exclusion, and Ostrowski’s classification of the places of ℚ. The description writes in the manuscript’s vocabulary about what the kernel checked, so the sentence carries both registers together. The entry says the monograph’s own concordance is precise and grades `DERIVES` against it, and that whether the manuscript proves exhaustiveness is untouched. It passed its face’s tally rule — no digit and no number word but *seven* — after the rule caught the seat’s own first draft.',
        '',
        '#### Component 2 — the live note',
        '',
        '*“' + CMP.NOTE + '”* — inserted in `REGISTRY.md` after the deposit-pin table and in `README.md` beside the kernel line; no existing line changed and no live claim narrowed.',
        '',
        '#### Component 3 — the profile at the deposited tag: @VERD@',
        '',
        'At `v1.5 = 0e5233f` the only printed route-terminal profiles are in `DEPOSIT_v1_2_NOTES.md`, under its heading for the **v1.2** audit; the tag’s `AxiomCheck_*.lean` files are check scripts, inputs and not outputs. The relay, PLACE-papers and the kernel’s working tree hold printed route-terminal profiles only from v1.2-era reports, none beside `0e5233f` or `v1.5`. What exists for v1.5 is statements — the archived loom’s receipt for `offLine_of_codim_two`, the archived trail’s *“verified unmoved at the deposit v1.5”*, the front door’s *“re-profiled clean at the v1.5 enactment”* and the record’s *“All route terminals report {propext, Classical.choice, Quot.sound}”* — and a statement of a run is not its output. **Second deposit-level matter, routed:** print and bank the route terminals’ profiles at the tag, in a lane that permits a `lean` run; priced, **not taken**.',
        '',
        '#### Component 4 — the routed items',
        '',
        '| item | disposition | why |',
        '|:--|:--|:--|',
        '| INVARIANCE_BARRIERS — the `T3` Tier-1 scope | **COMPLETED** | an era annotation beside `OPEN_TRAILS-archive-2:7971`, the line b455 decided |',
        '| THE_RESIDUE_OF_RH `:145` — `held-branch work` | **COMPLETED** | a line `(R63)(a)` named; the term → `merged-branch work`, the line preserved in a currency annotation |',
        '| THE_RESIDUE_OF_RH `:127`–`:130` — `HELD-BRANCH` cells | **LEFT** | lines the ruling did not name; a state-term change needs a ruling |',
        '| EXHAUSTIVENESS_LICENSE `:9` — the head’s version line | **LEFT** | a line the ruling did not name, dated at its own version |',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | the profile artefact is ABSENT at the deposited tag | **@N1@** |',
        '| (N2) | two of the three routed annotations complete without a ruling | **REFUTED** — one whole (INVARIANCE), one in part (THE_RESIDUE_OF_RH `:145`), one left (EXHAUSTIVENESS_LICENSE) |',
        '',
        '*Entered as the seat’s:* the satisfiability spec carried from b455 kept a clause capping this act’s annotations at none, which the face’s own reading contradicts; the face governed.',
        '',
        '**The span by the tool: @SPAN@ acts.** Both instrument lanes stay parked; nothing deposits; `h2` where the deposit left it. The four lists are open.',
    ]
    rep = [('@VERD@', VERD), ('@N1@', 'HELD' if VERD == 'ABSENT' else 'REFUTED'), ('@SPAN@', str(SPANN))]
    out = []
    for ln in body:
        for a, b in rep:
            ln = ln.replace(a, b)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b456)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest. **C1: E-2026-09-14-1 APPENDED, DEPOSIT-FACING, TALLY RULE PASSED, CONTENT (a)-(j) "
                 "PRESENT.** **C2: ONE NOTE SENTENCE INSERTED IN REGISTRY AND README, NO LINE CHANGED.** **C3: PROFILE ARTEFACT AT v1.5 %s -- THE v1.2 "
                 "PRINT AND CHECK SCRIPTS ONLY; STATEMENTS OF A RUN PRINTED APART; THE DISPOSITION PRICED, NOT TAKEN.** **C4: INVARIANCE COMPLETED; "
                 "RESIDUE :145 COMPLETED, :127-130 LEFT; LICENSE :9 LEFT.** (N1) %s, (N2) REFUTED. SPAN BY TOOL %s. 0 GRADES MOVED ON ANY ROW, "
                 "NOTHING DEPOSITS, NOTHING AT ZENODO")
            % (GR_, GDG, VERD, 'HELD' if VERD == 'ABSENT' else 'REFUTED', SPANN))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO LEAN RUN; KERNEL READ AT TAG v1.5 ONLY"
    prof = ("### PLACE-papers: ERRATA.md +1 ENTRY; REGISTRY.md AND README.md +1 NOTE EACH, INSERTED; INVARIANCE_BARRIERS.md +1 ANNOTATION; "
            "THE_RESIDUE_OF_RH.md ONE TERM AND +1 ANNOTATION; OPEN_TRAILS.md +1 RECORD; EVERY PRE-EDIT LINE PRESENT OR QUOTED -- 0 CONTENT LOST")
    grade = ("### THE ENTRY`S REQUIRED CONTENT AND TALLY RULE, THE NOTE`S PLACES, THE ARTEFACT`S DEFINITION AND THE ROUTED ITEMS` TEST WERE ON THE "
             "FACE BEFORE ANY WRITE; A STATEMENT OF A RUN NEVER REPORTED AS ITS OUTPUT")
    status = ("data/b456_the_errata_and_the_note.txt; data/b456_components.txt; data/b456_writes.json; data/b456_profile.json; data/b456_span.json; "
              "data/b456_checks.txt; data/b456_registration_2026-09-14.txt (LOCKED at sha256 %s); data/b456_addendum.txt (EMPTY); ERRATA.md; "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('errata entry E-2026-09-14-1',
           'R65 dispositions errata and live note',
           'route terminal profile artefact at v1.5',
           'invariance barriers T3 tier-1 annotation completed',
           'held-branch cells left for a ruling')
MUST_NOT_HIT = ('zenodo metadata edited', 'the live claim narrowed', 'profile printed at v1.5')
KEY = 'the-errata-entry-the-live-note-and-the-routed-annotations'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = ("b456 EXECUTED (R65): ERRATA E-2026-09-14-1 RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5, AND A LIVE (R20) NOTE BESIDE THE PIN; "
                 "THE ROUTE TERMINALS` PROFILE ARTEFACT AT v1.5 %s, ROUTED AND NOT TAKEN; INVARIANCE ANNOTATION COMPLETED, RESIDUE :145 COMPLETED, "
                 "RESIDUE :127-130 AND LICENSE :9 LEFT FOR A RULING. NO CLAIM ABOUT ZEROS." % VERD)
    grade = "### NO GRADE MOVED ON ANY ROW. ### NOTHING DEPOSITS. ### NO ZENODO METADATA EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b456_the_errata_and_the_note.txt; data/b456_components.txt; data/b456_writes.json; data/b456_profile.json; "
             "data/b456_registration_2026-09-14.txt (LOCKED, %d gates read, %d by digest); ERRATA.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR_, GDG, rownum))
    act = "b456 (the errata entry, the live note, and the routed annotations completed)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE ERRATA ENTRY, THE LIVE NOTE, AND THE ROUTED ANNOTATIONS COMPLETED (b456).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s' % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq[:48], pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL + '    # (key, act, one-line statement, grade as its own act recorded it, location)' + NL)
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
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]' % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b456 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the entry carried', 'E-2026-09-14-1' in out), ('the verdict carried', ('ARTEFACT AT v1.5 %s' % VERD) in out),
                      ('left carried', 'LEFT FOR A RULING' in out), ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq[:48], no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, "b456 -- THE ERRATA ENTRY, THE LIVE NOTE, AND THE ROUTED ANNOTATIONS COMPLETED.", '### THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE CONTROL SUITE (the reading this tool was gated on).', '-' * 100,
           '  arms run %d ; passing %d ; failing %d %s' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL, sorted(FAILING)),
           '  gates read %d ; checked by digest %d' % (GR_, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))


B455ROW_RE = r"(?m)^\| (\d+) \| \*\*THE DEPOSIT STATES THE SEVEN-CLASS CATALOGUE"

def main():
    global DESK
    bar('=')
    rec('b456_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not COMP or not READY:
        rec('  ### HARD FAILURE -- a record this tool reads is missing.')
        return 1
    if ARMS_FAIL < 0 or not FAILING <= SELF_WRITTEN or ARMS_FAIL != len(FAILING):
        rec('  ### HARD FAILURE -- the suite fails on an arm this tool does not write: %s' % sorted(FAILING - SELF_WRITTEN))
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records: gates %s/%s ; arms %s run, %s failing %s ; verdict %s ; diffs %s ; span %s'
        % (GR_, GDG, ARMS_RUN, ARMS_FAIL, sorted(FAILING), VERD, len(WJ.get('diffs') or []), SPANN))
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
            rec('  ### HARD FAILURE -- the prior mark is absent; refusing to append.')
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
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s' % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  the prior act`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B455ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.' % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b456_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
