# -*- coding: utf-8 -*-
"""b427_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off the table's JSON, never typed.
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
MARK = '<!-- b427 the witness arc at site (ii), sortie leg 2 -->'
PRIOR = '<!-- b426 the falsifier re-read by address, sortie leg 1 -->'
BANKOUT = os.path.join(D, 'b427_the_witness_arc_at_site_ii.txt')
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


def tidy(s):
    return (s or '').replace('`', '’').replace('|', '/')


FACE = read(os.path.join(D, 'b427_registration_2026-09-11.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b427_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
try:
    J = json.loads(read(os.path.join(D, 'b427_candidates.json')))
except Exception:
    J = dict(candidates=[], held=0, tally={}, site_i={}, site_i_n=0, same=0, diff=0)
CANDS = J.get('candidates', [])
N = len(CANDS)
HELD = J.get('held', 0)
TALLY = J.get('tally', {})
TI, NI = J.get('site_i', {}), J.get('site_i_n', 0)
SAME, DIFF = J.get('same', 0), J.get('diff', 0)
NEWKINDS = sorted(set(TALLY) - set(TI))
TALLYSTR = '; '.join('%s %d' % (k, v) for k, v in sorted(TALLY.items(), key=lambda x: (-x[1], x[0])))
TISTR = '; '.join('%s %d' % (k, v) for k, v in sorted(TI.items(), key=lambda x: -x[1]))
ROWMARK = ("**THE WITNESS ARC AT SITE (ii), THE HEIGHT COORDINATE'S ENUMERATION: %d CANDIDATES READ AT SOURCE, "
           "%s; AND THE ARC IS NOT CONVERGING ON ONE BOUNDARY**"
           % (N, 'NONE HELD' if HELD == 0 else ('%d HELD' % HELD)))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('site (ii) of W-ORD-WITNESS-ENUMERATION', 'CLOSE',
     'READ at b427: %d candidates, each read at its source and attempted by S1 CLASS, S2 HELD, S3 FORM in b424`s '
     'fixed order; HELD %d. First failing steps by kind: %s.' % (N, HELD, TALLYSTR)),
    ('W-ORD-WITNESS-ENUMERATION, sites (iii) to (vi)', 'STANDING',
     'CHECKPOINTED after site (ii). Four sites remain, one act each; trigger: the author`s word opens the next.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED AND NOT RULED: %d of %d failures land at a boundary site (i) also used, %d of %d at a boundary new to '
     'this site (%s). The class boundary alone: %d of %d at site (i), %d of %d here.'
     % (SAME, N, DIFF, N, ', '.join(NEWKINDS) or 'none',
        TI.get('CLASS BOUNDARY', 0), NI, TALLY.get('CLASS BOUNDARY', 0), N)),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424 and still routed; this act appended a block again rather than write inside the cell.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423; trigger: the author rules on it.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; its line unedited by this act, entry (ii)`s WITNESS still NONE KNOWN.'),
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
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    L = ['', MARK, '',
         '### b427 — the witness arc at site (ii), sortie leg 2 — filed 2026-09-11', '',
         '#### The site’s own text, quoted before any candidate', '',
         'Row U1’s entry (ii) carries `WITNESS: NONE KNOWN`: the height coordinate is *“BOUNDED BY A MEASUREMENT and '
         'not by an argument”*, and the witness would be **one argument serving every height**, against a method that '
         'produces zeros one at a time. b351 named the class that would have to be proved silent — `gamma > 150`, '
         'where the census stopped — and said in the same act that *“RUNNING THE CENSUS HIGHER BUYS MORE INSTANCES, '
         'AND A CLASS IS NOT MADE OF INSTANCES.”*', '',
         '#### The %d, each failed at a quoted step' % N, '',
         'The navigator’s opening three — the classical zero-free region as bounding abscissa not margin; a growth '
         'bound on the margin in height; the density theorems as the register the channels are bright for — and %d the '
         'search supplied by description from the record and the two verified sources, every hit hand-read. Each was '
         'attempted by three steps in b424’s fixed order — S1 CLASS, S2 HELD, S3 FORM — and failed at the first it '
         'failed:' % (N - 3), '']
    for c in CANDS:
        L.append('- **%s** %s — FAILED AT S%s, %s' % (c['id'], tidy(c['name']), c['first'], c['kind']))
    L += ['',
          '**NO WITNESS HELD. %d candidates, %d held.** First failing steps: %s.' % (N, HELD, TALLYSTR), '',
          '#### The line this site owes the arc, counted', '',
          'Site (i) (b427’s predecessor, b424) failed %d candidates at %s. Site (ii) fails %d at %s. **%d of %d land '
          'at a boundary site (i) also used; %d of %d land at a boundary new to this site** — %s. **The class boundary '
          'alone: %d of %d at site (i), %d of %d at site (ii).** So the arc is **not** converging on a single '
          'boundary: the second site needs %d kinds the first never used. And the expected kind — the '
          'density–placement split — accounts for exactly %d of them, so it is one of the new boundaries and not the '
          'new boundary.'
          % (NI, TISTR, N, TALLYSTR, SAME, N, DIFF, N, ', '.join(NEWKINDS) or 'none',
             TI.get('CLASS BOUNDARY', 0), NI, TALLY.get('CLASS BOUNDARY', 0), N,
             len(NEWKINDS), TALLY.get('DENSITY-PLACEMENT SPLIT', 0)), '',
          '#### Where it was written', '',
          '`FACES_LEDGER.md` gains one block, `<!-- b427 update -->`, through the writer’s `append_block`, every '
          'quotation at a first failing step verified by the writer’s `verify_quotes` first. Row U1’s line is '
          'byte-identical, entry (ii)’s `WITNESS: NONE KNOWN` stands, the freeze at six stands, and no seventh site is '
          'entered. **The cell would have been written only if a candidate held; none did.**', '',
          '#### The arc, checkpointed', '',
          '**W-ORD-WITNESS-ENUMERATION is checkpointed after site (ii).** Sites (iii) to (vi) remain, one act each. '
          'Trigger: the author’s word opens the next site.', '',
          '#### The four lists', '',
          FOUR, '',
          '#### What this act did not do', '',
          '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 bytes of '
          'row U1’s line. 0 seventh sites. 0 witness cells written. 0 rules struck or amended. 0 orientation-layer '
          'lines edited. 0 locked faces edited. 0 prior banks edited. 0 banked ferries edited. 0 kernel files touched. '
          '0 deposit actions, 0 platform calls. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS AN EXHAUSTED CANDIDATE LIST AT ONE SITE OF ROW U1, AND THE COUNTED COMPARISON WITH THE "
         "SITE BEFORE IT. ### IT CONFERS NO GRADE, TYPES NO BRIDGE AND TOUCHES NO KERNEL")


def corr_rows():
    m = ROWMARK + " (b427, sortie leg 2)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b427 -- @GR@ gates "
            "read, @GDG@ checked by digest. **THE SITE`S OWN CELL QUOTED FIRST: the witness would be ONE ARGUMENT "
            "SERVING EVERY HEIGHT, and the coordinate is BOUNDED BY A MEASUREMENT.** **@N@ CANDIDATES, EACH READ AT ITS "
            "SOURCE AND ATTEMPTED BY S1 CLASS, S2 HELD, S3 FORM; HELD @HELD@.** **FIRST FAILING STEPS: @TALLY@.** "
            "**AGAINST SITE (i): @SAME@ OF @N@ AT A BOUNDARY IT ALSO USED, @DIFF@ OF @N@ AT A BOUNDARY NEW TO THIS "
            "SITE (@NEW@) -- THE ARC IS NOT CONVERGING ON ONE BOUNDARY.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, "
            "0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. Row U1's line byte-identical; entry (ii)'s WITNESS cell still NONE KNOWN"
    prof = ("### TWO PLACE-papers FILES WRITTEN -- FACES_LEDGER.md ONE APPENDED BLOCK THROUGH THE WRITER'S "
            "append_block, ITS QUOTATIONS VERIFIED FIRST; OPEN_TRAILS.md ONE APPEND, ITS PIN A TRUE PREFIX; NO ROW "
            "REWRITTEN, NO SEVENTH SITE, NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, ROUTE OR RULE -- 0 CONTENT LOST")
    grade = ("### EVERY CANDIDATE WAS READ AT ITS SOURCE OR AT THE RECORD'S QUOTATION OF IT AND FAILED AT A QUOTED "
             "STEP; THE COMPARISON WITH SITE (i) IS COUNTED OFF b424'S OWN BANKED JSON AND NOT RECALLED")
    status = ("data/b427_the_witness_arc_at_site_ii.txt; data/b427_candidates.txt; data/b427_candidates.json; "
              "data/b427_ledger_write.txt; data/b427_registration_2026-09-11.txt (LOCKED at sha256 %s); "
              "PLACE-papers FACES_LEDGER.md, OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@N@', str(N))
                .replace('@HELD@', str(HELD)).replace('@TALLY@', TALLYSTR).replace('@SAME@', str(SAME))
                .replace('@DIFF@', str(DIFF)).replace('@NEW@', ', '.join(NEWKINDS) or 'none'))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the witness arc at site ii', 'the height coordinate enumeration', 'site ii exhausted list',
           'where the witness arc failures land', 'b427 sortie leg 2')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-witness-arc-at-site-ii'


def do_key(rownum):
    statement = (
        "b427 ATTEMPTED %d CANDIDATES AT ROW U1'S SITE (ii), THE HEIGHT COORDINATE'S ENUMERATION -- the navigator's "
        "opening three and %d the search supplied -- EACH READ AT ITS SOURCE AND FAILED AT A QUOTED STEP BY S1 CLASS, "
        "S2 HELD, S3 FORM. HELD %d. FIRST FAILING STEPS: %s. AGAINST SITE (i): %d of %d at a boundary it also used, "
        "%d of %d at a boundary NEW to this site (%s). No witness found; the cell was not written."
        % (N, N - 3, HELD, TALLYSTR, SAME, N, DIFF, N, ', '.join(NEWKINDS) or 'none'))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b427_the_witness_arc_at_site_ii.txt; data/b427_candidates.txt; data/b427_ledger_write.txt; "
             "data/b427_registration_2026-09-11.txt (LOCKED, %d gates read, %d by digest); FACES_LEDGER.md; "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b427 (sortie leg 2: the witness arc at site (ii))"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE WITNESS ARC AT SITE (ii) (b427).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b427 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the held count carried', ('HELD %d' % HELD) in out),
                      ('the tally carried', TALLYSTR.split(';')[0].strip() in out),
                      ('the comparison carried', 'boundary NEW to this site' in out)):
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
    B = ['=' * 100, 'b427 -- THE WITNESS ARC AT SITE (ii). SORTIE LEG 2.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    comp = read(os.path.join(D, 'b427_components.txt'))
    B += ['', '-' * 100, '### THE EXPECTATION, AS THE REPORT SCORED IT.', '-' * 100]
    B += [ln for ln in comp.splitlines() if ln.strip().startswith('(L2)')]
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


B426ROW_RE = r'(?m)^\| (\d+) \| \*\*THE FALSIFIER RE-READ BY ADDRESS UNDER \(R38\)'


def main():
    bar('=')
    rec('b427_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or N == 0:
        rec('  ### HARD FAILURE -- the lock gate`s record or the candidate table is missing.')
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
    at = lambda mk, s: [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b426`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B426ROW_RE, txt)])
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
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- b426`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B426ROW_RE, after)], at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b427_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
