# -*- coding: utf-8 -*-
"""b419_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### The lock gate's record is its first and only
### run (`b419_lockgate_notes.txt`), which permitted.
"""
import io
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
MARK = '<!-- b419 the helper fixed, the clause printed -->'
PRIOR = '<!-- b418 the ruling carried, the walker measured, the repairs made, and (N) opened -->'
B418ROW = "**THE GENERAL CLAUSE IS OVER-BUDGET WITH ONE HELPER UNSUPPLIED, AND THE WALKER'S MISS WAS A SILENT TIMEOUT**"
BANKOUT = os.path.join(D, 'b419_the_clause_printed.txt')
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


FACE = read(os.path.join(D, 'b419_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b419_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger, the ruling on which test governs or any '
     'disposition on the lists, has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING', 'ROUTED and still routed.'),
    ('(N), the general clause', 'CLOSE',
     'PROVED, ZERO AXIOMS, ON THE FIRST PROBE: b418’s library with pow_pred’s term repaired as b418 named it. The '
     'kernel carries it as Core/SmearGeneral.lean; smear_general and cells_are_instances print clean, and the prior '
     'profile is a true byte prefix of the new.'),
    ('the seal’s caveat (T1.4)', 'CLOSE',
     'ANNOTATED with b416’s drafted words, inserted after the clause and striking nothing; every existing word survives.'),
    ('b414’s twenty-eight sentences', 'CLOSE',
     'RE-CLASSIFIED over b414’s hand-read: its eight GROUP A rows QUALIFIED BY THE PROOF, its twenty GROUP B rows '
     'UNREACHED BY THE PROOF. 0 sentences edited.'),
    ('SinglePrimeFactor’s docstring, which calls the statement open', 'STANDING',
     'DATED BY THE NEW MODULE, NOT EDITED: the file is not on this act’s write list. Its sentence "this act does not '
     'prove it" stays true of b414 and now reads as history. Routed.'),
    ('the lock that refused on a ferry’s own word', 'STANDING',
     'PRICED, NOT RESOLVED. Route 1 (re-paste) and route 3 (a one-act ruling) cost the author one action per hit; '
     'route 2 (a face-named in-paste hit permitted) needs the lock gate changed, the instrument lane’s work, which is '
     'PARKED. The gate has refused one ferry in 43 gated scans. Routed to the author.'),
    ('silent timeouts outside the arc', 'CLOSE',
     'LISTED: 24 walker calls reached the limit across every transcript, 14 over relay or a directory holding it. Two '
     'banked verdicts rest on one: b231’s (ABSENT) and b300’s DIFFERENT, both re-run bounded, and BOTH CONFIRMED. '
     'Every silent call in the scored set was batched, so the guard cannot decide it from the record, and the act '
     'says so.'),
    ('this act’s own face: BAR 3’s clause on AllPrints', 'STANDING',
     'A DEFECT OF THE FACE, REPORTED AND NOT EDITED: it asks for AllPrints’ prior bytes to be a prefix of its new '
     'ones, which Lean’s import rule forbids; the face’s (C)(ii) places the import correctly and that measure is met.'),
    ('the Reader’s encoding', 'STANDING', 'ROUTED, NOT REPAIRED, as at b416.'),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING', 'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1600], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**' % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    return [
        '', MARK, '',
        '### b419 — the helper fixed, the clause printed — filed 2026-09-11', '',
        '#### The general clause', '',
        '**PROVED, with zero axioms, on the first probe.** For every base with a single prime factor and every level, '
        '`ballQ p n * sumAN p n = sumAQ p n`. The library is b418’s attempt, with the one term b418 named repaired: '
        '`pow_pred` now passes `Nat.pow_succ` its base and exponent. The kernel carries it as `Core/SmearGeneral.lean`; '
        '`smear_general` and `cells_are_instances` print "does not depend on any axioms", and the prior profile is a '
        'true byte prefix of the new. The seven decided cells are instances. The seal’s caveat (T1.4) carries b416’s '
        'annotation, and b414’s twenty-eight sentences are re-classified: eight qualified by the proof, twenty unreached '
        'by it, none edited.',
        '',
        '#### The lock and the scan', '',
        '**Priced, not resolved.** The lock gate admits only a ferry scan of zero; the scan says a hit is a site for a '
        'reader. Re-pasting or a one-act ruling costs the author one action per hit; permitting a face-named hit inside '
        'the paste needs the lock gate changed, which is the parked instrument lane’s work. The gate has refused one '
        'ferry in 43 gated scans. Routed to the author.',
        '',
        '#### Silent timeouts outside the arc', '',
        '**Two banked verdicts rested on a timed-out search, and both are CONFIRMED.** Of 24 searches that reached the '
        'tool’s limit, 14 ran over relay or a directory holding it. b231’s absence of the owner’s pair holds on the '
        'relay tree before the call; b300’s reading of "the Sonin sector" holds on every line from its adoption on, '
        'with two earlier usages printed and not ruled on. Every silent call in the set was issued beside others, so '
        'its recorded time is the batch’s and the guard cannot decide it; the act says so.',
        '',
        '#### The four lists', '',
        FOUR,
        '',
        '#### What this act did not do', '',
        '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of '
        '`FACES_LEDGER.md` written. 0 folds run. 0 rules struck or amended. 0 orientation-layer lines edited. 0 locked '
        'faces edited. 0 prior banks edited. 0 bytes of the lock gate or the scan changed. 0 deposit actions, 0 platform '
        'calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS THE NAMED OPEN STATEMENT PROVED AT ZERO AXIOMS, A LOCK CONFLICT PRICED, AND THE "
         "SILENT TIMEOUTS OUTSIDE THE ARC CENSUSED. ### IT MOVES NO GRADE AND DISCHARGES NO PREMISE; THE PROOF IS "
         "OF THE MODEL'S ARITHMETIC, AND ITS IDENTIFICATION WITH THE SOURCE'S TRACE REMAINS b310'S AND UNCOMPILED")


def corr_rows():
    m = "**THE GENERAL CLAUSE IS PROVED, ZERO AXIOMS, ON THE FIRST PROBE** (b419, the clause printed)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b419 -- @GR@ gates "
            "read, @GDG@ checked by digest. **COMPONENT 1: pow_pred REPAIRED AS b418 NAMED IT; FOR EVERY p WITH "
            "singlePrimeFactor p = true AND EVERY n, ballQ p n * sumAN p n = sumAQ p n; THE SEVEN CELLS INSTANCES; "
            "THE PRIOR PROFILE A TRUE BYTE PREFIX; (T1.4) ANNOTATED; b414'S TWENTY-EIGHT RE-CLASSIFIED 8 AND 20.** "
            "**COMPONENT 2: THE LOCK AND THE SCAN PRICED, NOT RESOLVED -- ONLY ONE ROUTE NEEDS THE INSTRUMENT LANE.** "
            "**COMPONENT 3: 24 SEARCHES REACHED THE LIMIT, 14 OVER RELAY; TWO BANKED VERDICTS REST ON ONE, BOTH "
            "CONFIRMED.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = ("SmearGeneral.smear_general and SmearGeneral.cells_are_instances (NEW, Core/SmearGeneral.lean), each "
            "printing 'does not depend on any axioms'")
    prof = ("### ONE MODULE ADDED, ITS IMPORT AND TWO PRINTS IN AllPrints.lean, AXIOM_PRINTS.txt REGENERATED 605 -> "
            "607 LINES WITH THE PRIOR PROFILE A TRUE BYTE PREFIX, AND b416'S ANNOTATION INSERTED IN FiniteSideSeal's "
            "HEADER. ### NO EXISTING TERMINAL MOVED; Classes.lean AND SinglePrimeFactor.lean UNCHANGED; NO GRADE, "
            "PREMISE, DOOR, KAPPA, ROUTE, FACES_LEDGER ROW, FOLD OR RULE -- 0 CONTENT LOST")
    grade = ("### THE VERDICT WAS READ FROM THE PRINTED PROFILE, NEVER FROM THE EXIT CODE. ### A LOCKED FACE'S "
             "UNMEETABLE CLAUSE WAS PRINTED BESIDE THE MEASURE MET, NOT EDITED. ### TWO BANKED VERDICTS WERE RE-RUN, "
             "NOT RE-VERDICTED")
    status = ("data/b419_the_clause_printed.txt; data/b419_components.txt; data/b419_n_probe.txt; data/b419_n_verify.txt; "
              "data/b419_twentyeight.txt; data/b419_lock_priced.txt; data/b419_timeouts.txt; "
              "data/b419_registration_2026-09-11.txt (LOCKED at sha256 %s); Core/SmearGeneral.lean (NEW); AllPrints.lean; "
              "AXIOM_PRINTS.txt; Core/FiniteSideSeal.lean; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])

    def sub(x):
        return x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('is the general smear clause proved', 'smear general zero axioms', 'the clause printed',
           'the lock versus the scan priced', 'silent timeouts outside the arc', 'which banked verdicts rest on a timeout')
MUST_NOT_HIT = ('the lock was overridden', 'the lock gate was changed', 'a grade was moved', 'h2 has moved')
KEY = 'the-clause-printed'


def do_key(rownum):
    statement = (
        "b419 FIXED THE HELPER AND PRINTED THE CLAUSE. **THE GENERAL CLAUSE IS PROVED, ZERO AXIOMS, ON THE FIRST "
        "PROBE: FOR EVERY p WITH A SINGLE PRIME FACTOR AND EVERY n, ballQ p n * sumAN p n = sumAQ p n** "
        "(Core/SmearGeneral.lean, smear_general and cells_are_instances), **THE PRIOR PROFILE A TRUE BYTE PREFIX OF "
        "THE NEW.** The seal's (T1.4) carries b416's annotation; b414's twenty-eight are re-classified, eight qualified "
        "by the proof and twenty unreached. **THE LOCK AND THE SCAN ARE PRICED, NOT RESOLVED**; only a face-named "
        "in-paste permission needs the instrument lane. **OF 24 SEARCHES THAT REACHED THE TOOL'S LIMIT, TWO CARRIED A "
        "BANKED VERDICT, AND BOTH ARE CONFIRMED** by bounded re-runs.")
    grade = ("### ONE MODULE AND TWO TERMINALS ADDED, NO EXISTING TERMINAL MOVED, NO GRADE MOVED, NO PREMISE "
             "DISCHARGED. ### NOTHING DEPOSITS")
    where = ("data/b419_the_clause_printed.txt; data/b419_components.txt; data/b419_n_probe.txt; data/b419_n_verify.txt; "
             "data/b419_timeouts.txt; data/b419_lock_priced.txt; data/b419_registration_2026-09-11.txt (LOCKED, %d "
             "gates read, %d by digest); Core/SmearGeneral.lean; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b419 (the helper fixed and the general clause proved; the lock priced; the silent timeouts censused)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE CLAUSE PRINTED (b419).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
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
        rec('    %-58s reaches the b419 key : %s' % (qq[:58], g2))
    for lbl, cond in (('proved, zero axioms', 'PROVED, ZERO AXIOMS, ON THE FIRST' in out),
                      ('prefix', 'THE PRIOR PROFILE A TRUE BYTE PREFIX' in out),
                      ('priced', 'PRICED, NOT RESOLVED' in out),
                      ('both confirmed', 'BOTH ARE CONFIRMED' in out)):
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
    B = ['=' * 100, 'b419 -- THE HELPER FIXED, THE CLAUSE PRINTED.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b419_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s permitting record does not carry its count line.')
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
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s' % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1
    b418at = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B418ROW), txt)]
    rec('  b418`s row, by its marker, before : %s' % b418at)
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(ROWS2[0][0]), txt)][0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    mine = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(ROWS2[0][0]), after)]
    rec('  b418`s row after : %s ; this act`s row, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B418ROW), after)], mine))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b419_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
