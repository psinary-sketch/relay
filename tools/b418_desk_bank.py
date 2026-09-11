# -*- coding: utf-8 -*-
"""b418_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **THE AMENDMENT'S DISCIPLINE, CARRIED:** the slots and the fifteen are written in separate
### paragraphs and never in one sentence. ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.**
### ### **THE LOCK GATE'S RECORD IS READ FROM ITS PERMITTING RUN** (`b418_lockgate_notes2.txt`); its
### first run refused and is kept as it ran.
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
MARK = '<!-- b418 the ruling carried, the walker measured, the repairs made, and (N) opened -->'
PRIOR = '<!-- b417 the contradiction put to its owner, and the second tool cleared -->'
B417ROW = '**READING (a) WOULD LEAVE TWO DISTINCT TUPLES WHERE THE MODEL NAMES FOUR CLASSES'
BANKOUT = os.path.join(D, 'b418_the_ruling_carried.txt')
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


FACE = read(os.path.join(D, 'b418_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b418_lockgate_notes2.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING', 'ROUTED and still routed.'),
    ('the formation contradiction', 'CLOSE',
     'RULED BY THE AUTHOR, (R35), READING (b), AND EXECUTED: the universality sentence narrowed in place at both '
     'its occurrences to its n2 theorem’s hypothesis, the original quoted beside each, and one line saying B’s and '
     'D’s second component remains STIPULATED. No tuple and no kernel figure moved; class A unmoved.'),
    ('the citer that is not the owner', 'CLOSE', 'AT_REST.md updated by append only, its prior bytes a true prefix.'),
    ('the walker’s blind spot at b417', 'CLOSE',
     'CAUSE FOUND: a silent timeout at the tool’s twenty-second limit, returning a partial set with no flag. Not a '
     'file kind, not a binary heuristic, not an ignore pattern. The arc ran one call over relay’s data; it hit the '
     'limit; no ABSENT verdict rests on it; re-run bounded, it reaches all forty files, file for file with Python.'),
    ('the guard against a silent limit', 'CLOSE',
     'BUILT: relay tools/walker_guard.py, one line reporting INCOMPLETE and never a count; fixtures in both '
     'polarities. No search wrapper existed to carry the line, and the act says so. Its reach is printed: it guards '
     'what a record takes from a result, and it errs toward INCOMPLETE on batched calls.'),
    ('the lock that refused on a ferry’s own word', 'STANDING',
     'ROUTED. The lock gate admits zero ferry-scan hits with no reader override, while the scan’s own doctrine '
     'says the reader rules. The author re-pasted; the mismatch between the two stays for an instrument act.'),
    ('the keystone’s sentence about forty-three', 'CLOSE',
     'REPAIRED BY ONE LINE BELOW IT, the sentence kept byte-for-byte; its class, Tier C, forbids no edit.'),
    ('registry row p2-35', 'CLOSE', 'PRESERVED VERBATIM FIRST, then its two stale figures removed rather than restated.'),
    ('the hygiene tool', 'CLOSE',
     'RETIRED to relay tools/retired/, byte-for-byte, with RETIRED.md: its last verdict FAILED, its writes, the '
     'repair-snapshot guard as what caught it, and the sixteen tools its move dates.'),
    ('(N), the general clause', 'STANDING',
     'OVER-BUDGET AT THE CAP. Sixteen probes: S0, Euclid, S1 to S5 built axiom-free except one helper, pow_pred, whose '
     'term failed at its .trans in the last probe; the general clause elaborates and prints sorryAx by inheritance '
     'only. NEXT STEP: repair pow_pred and compile. The theorem is not claimed.'),
    ('the example systems two tables place differently', 'CLOSE',
     'PARSED: the tables key by different things -- substrate class in one, formation total and toolkit in the other '
     '-- and the Shannon rows name different objects. Counted, not repaired.'),
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
        '### b418 — the ruling carried, the walker measured, the repairs made, and (N) opened — filed 2026-09-11', '',
        '#### The walker', '',
        '**What b417 saw was a timeout, not a blind region.** The one search the arc ran over relay’s data records '
        'took 20.04 seconds, the tool’s limit, and returned the thirteen files it had reached with no flag and no '
        'timeout text. Forty matching files existed. No ignore rule excluded any of them, and no file kind was '
        'skipped. **No ABSENT verdict rests on that call**, so the order’s re-run is over an empty set of verdicts; '
        'the call itself, re-run bounded in six parts, reaches all forty, file for file with a Python walker. The '
        'guard is built as `tools/walker_guard.py`: a call that reached its limit reads INCOMPLETE and never as a count.',
        '',
        '#### The slots', '',
        '**(R35) executed.** The owner’s universality sentence is narrowed in place, at both its occurrences, to its '
        'n₂ theorem’s own hypothesis, *connected reductive symmetry groups*, with the original quoted beside each; one '
        'line beside section I says classes B and D keep their second component STIPULATED. AT_REST is updated by '
        'append. No tuple and no kernel figure moved, and class A is unmoved.',
        '',
        '**The three example systems, parsed.** MATTER keys each system to its substrate class; COMPLEX_ANALYSIS keys '
        'each to its formation total and toolkit. The two Shannon rows name different objects. Gate 1b already says a '
        'tuple is decomposition-dependent. Counted, not repaired.',
        '',
        '#### The kernel', '',
        '**(N) is OVER-BUDGET at the cap.** Sixteen probes built the argument axiom-free: a single-prime-factor base '
        'is a prime power; Euclid’s lemma without gcd; the remainder rebuilt from its own clean equations; the '
        'kernel’s sums rewritten as sums over the off-ball index; the progression count; and the per-index count. '
        '**One helper, `pow_pred`, failed to elaborate in the last probe**, and every declaration that failed did so by '
        'depending on it — including the general clause itself. The next step is to repair that one term and '
        'compile. The theorem is not claimed.',
        '',
        '#### The fifteen', '',
        '**The keystone’s sentence about forty-three** now carries one line below it: 43 = 2⁴ + 3³, so the sentence '
        'is false at 43. **Registry row p2-35** was preserved verbatim and its two stale figures removed.',
        '',
        '#### What this act did not do', '',
        '0 `.lean` files in the kernel touched, 0 kernel builds, 0 terminals added. 0 grades moved. 0 premises '
        'discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 rows of `FACES_LEDGER.md` written. 0 '
        'folds run. 0 rules struck or amended. 0 orientation-layer lines edited. 0 locked faces edited. 0 tuples moved. '
        '0 words of the example systems’ documents edited. 0 deposit actions, 0 platform calls. **And h2 where the '
        'deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS A RULING EXECUTED, A WALKER'S MISS DIAGNOSED AND GUARDED, THREE REPAIRS MADE, AND "
         "A PROOF ATTEMPT THAT REACHED ITS CAP WITH ONE HELPER UNSUPPLIED. ### IT MOVES NO GRADE, DISCHARGES NO "
         "PREMISE, CLAIMS NO THEOREM AND TOUCHES NO KERNEL FILE")


def corr_rows():
    m = ("**THE GENERAL CLAUSE IS OVER-BUDGET WITH ONE HELPER UNSUPPLIED, AND THE WALKER'S MISS WAS A SILENT "
         "TIMEOUT** (b418, the ruling carried)")
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, after one refusal and a re-paste, chained on "
            "b378's gate run as b418 -- @GR@ gates read, @GDG@ checked by digest. **COMPONENT 1: THE ONE WALKER CALL "
            "OVER RELAY'S DATA RAN TO ITS TWENTY-SECOND LIMIT AND RETURNED A PARTIAL SET WITH NO FLAG; NO ABSENT "
            "VERDICT RESTS ON IT; RE-RUN BOUNDED IT REACHES ALL FORTY FILES; THE GUARD IS tools/walker_guard.py.** "
            "**COMPONENT 2: (R35) EXECUTED -- THE SENTENCE NARROWED IN PLACE AT BOTH OCCURRENCES, THE ORIGINAL QUOTED, "
            "ONE STIPULATED LINE; NO TUPLE MOVED.** **COMPONENT 3: THE KEYSTONE'S LINE ADDED, p2-35'S FIGURES REMOVED, "
            "THE HYGIENE TOOL RETIRED.** **COMPONENT 4: (N) OVER-BUDGET AT SIXTEEN PROBES -- EVERY STEP BUILT AXIOM-FREE "
            "BUT ONE HELPER, pow_pred; THE THEOREM IS NOT CLAIMED.** **COMPONENT 5: THE EXAMPLE SYSTEMS PARSED BY "
            "DIFFERENT KEYS.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS ADDED. ### THE ATTEMPT'S LEMMAS LIVE IN SCRATCH PROBES "
            "BANKED AS A RELAY RECORD, NOT IN THE KERNEL. ### classA_distinct_from_classD IS CITED AS THE REASON (R35) "
            "RECORDS")
    prof = ("### NO KERNEL .lean FILE TOUCHED, NO KERNEL BUILD, NO TERMINAL ADDED, NO GRADE MOVED, NO PREMISE "
            "DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO ROUTE PROPOSED, NO FACES_LEDGER ROW, NO FOLD, NO RULE "
            "STRUCK OR AMENDED, NO ORIENTATION-LAYER LINE EDITED, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE CORPUS "
            "WRITES ARE (R35)'S EDIT, AN APPEND, ONE LINE, ONE REGISTRY ROW'S FIGURES, ONE TRAIL BLOCK AND ONE ROW -- 0 "
            "CONTENT LOST")
    grade = ("### A RULING WAS EXECUTED AS WRITTEN. ### A WALKER'S MISS WAS TRACED FROM THE TOOL'S OWN RECORDED TIMES, "
             "NOT GUESSED, AND AN IGNORE HYPOTHESIS WAS REFUTED BEFORE IT WAS BANKED. ### A PROBE THAT LOOKED LIKE A "
             "BLOCK WAS REFUTED BY A WIDER ONE. ### A LOCK THAT REFUSED WAS NOT OVERRIDDEN")
    status = ("data/b418_the_ruling_carried.txt; data/b418_components.txt; data/b418_walker.txt; data/b418_r35.txt; "
              "data/b418_repairs.txt; data/b418_n_attempt.txt; data/b418_registration_2026-09-11.txt (LOCKED at "
              "sha256 %s); tools/walker_guard.py (NEW); tools/retired/ (NEW); PLACE-papers MATTER_AS_ARITHMETIC.md, "
              "AT_REST.md, CONSTANCE.md, REGISTRY.md p2-35, OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('why did the search tool miss relay data records', 'what did the author rule on the formation contradiction',
           'is the smear identity proved for prime powers', 'walker guard incomplete never a count',
           'where is the hygiene tool retired', 'what happened to the keystone sentence about forty three')
MUST_NOT_HIT = ('the smear identity is proved', 'the lock was overridden', 'a grade was moved', 'h2 has moved')
KEY = 'the-ruling-carried'


def do_key(rownum):
    statement = (
        "b418 CARRIED THE AUTHOR'S RULING AND MEASURED THE WALKER. **(R35) READING (b) EXECUTED: THE UNIVERSALITY "
        "SENTENCE NARROWED IN PLACE, THE ORIGINAL QUOTED, B AND D STIPULATED; NO TUPLE MOVED.** **THE WALKER'S MISS "
        "AT b417 WAS A SILENT TIMEOUT AT THE TOOL'S TWENTY-SECOND LIMIT**, not a file kind and not an ignore pattern; "
        "**NO ABSENT VERDICT RESTS ON IT**; **THE GUARD tools/walker_guard.py REPORTS A CALL THAT REACHED ITS LIMIT AS "
        "INCOMPLETE, NEVER AS A COUNT.** **(N) IS OVER-BUDGET AT SIXTEEN PROBES WITH ONE HELPER UNSUPPLIED, pow_pred; "
        "THE THEOREM IS NOT CLAIMED.** The keystone's sentence about 43 carries one correcting line; p2-35's stale "
        "figures are removed; the hygiene tool is RETIRED to tools/retired/.")
    grade = ("### NO KERNEL FILE TOUCHED, NO TERMINAL ADDED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### THE THEOREM IS "
             "NOT CLAIMED. ### NOTHING DEPOSITS")
    where = ("data/b418_the_ruling_carried.txt; data/b418_components.txt; data/b418_walker.txt; data/b418_n_attempt.txt; "
             "data/b418_registration_2026-09-11.txt (LOCKED, %d gates read, %d by digest); tools/walker_guard.py; "
             "tools/retired/RETIRED.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = ("b418 (R35 executed, the walker's miss traced to a silent timeout and guarded, three repairs, and (N) "
           "attempted to OVER-BUDGET with one helper unsupplied)")
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE RULING CARRIED (b418).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b418 key : %s' % (qq[:58], g2))
    for lbl, cond in (('R35 executed', '(R35) READING (b) EXECUTED' in out),
                      ('silent timeout', 'SILENT TIMEOUT' in out),
                      ('no absent verdict', 'NO ABSENT VERDICT RESTS ON IT' in out),
                      ('the guard', 'INCOMPLETE, NEVER AS A COUNT' in out),
                      ('over-budget', 'OVER-BUDGET AT SIXTEEN PROBES' in out),
                      ('not claimed', 'THE THEOREM IS NOT CLAIMED' in out)):
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
    B = ['=' * 100, 'b418 -- THE RULING CARRIED, THE WALKER MEASURED, THE REPAIRS MADE, AND (N) OPENED.', 'THE BANK.',
         '=' * 100, '']
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
    rec('b418_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    b417at = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B417ROW), txt)]
    rec('  b417`s row, by its marker, before : %s' % b417at)
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
    rec('  b417`s row after : %s ; this act`s row, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(B417ROW), after)], mine))
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
    io.open(os.path.join(D, 'b418_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
