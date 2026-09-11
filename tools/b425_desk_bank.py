# -*- coding: utf-8 -*-
"""b425_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every verdict here is read off the read's JSON, never typed;
### a FIRED reading is carried at full prominence with the register row named as the author's to move.
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
MARK = '<!-- b425 the falsifier read, sortie leg 3 -->'
PRIOR = '<!-- b424 the witness arc at site (i), sortie leg 2 -->'
B424ROW = "**THE WITNESS ARC AT SITE (i), THE CLAUSE'S QUANTIFIER: SIXTEEN CANDIDATES READ AT SOURCE, NONE HELD**"
BANKOUT = os.path.join(D, 'b425_the_falsifier_read.txt')
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


FACE = read(os.path.join(D, 'b425_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b425_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
try:
    J = json.loads(read(os.path.join(D, 'b425_the_read.json')))
except Exception:
    J = dict(sources=[], fired=[])
SRC = J['sources']
N = len(SRC)
FIRED = J['fired']
NUND = sum(1 for s in SRC if s['verdict'] == 'UNDECIDED')
SUMMARY = ('FIRED AT %d BY THE LOCKED RULE, UNDECIDED AT %d' % (len(FIRED), NUND)) if FIRED else ('UNDECIDED AT %d' % NUND)
ROWMARK = "**THE FALSIFIER READ: THE LANE'S w = −1 AGAINST THREE SUPERNOVA RESULTS -- %s**" % SUMMARY

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('the falsifier read', 'CLOSE',
     'READ at b425: %d sources chosen by the locked rule, each hashed and read at its text; per source %s.'
     % (N, '; '.join('%s %s' % (s['id'], s['verdict']) for s in SRC))),
    ('the lane`s condition, FIRED at %s by the locked rule' % (', '.join(FIRED) or 'no source'), 'STANDING',
     ('THE AUTHOR`S TO MOVE: REGISTRY.md p2-d6 and FORMATION_DISTANCE.md line 160. No lane verdict changed by the seat.'
      if FIRED else 'Not fired; nothing to move.')),
    ('the rule`s three limits (a word, a window, no combining rule)', 'STANDING', 'ROUTED TO THE AUTHOR AND NOT RULED.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged; the lane`s own STORMER.md names it.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (ii) to (vi)', 'STANDING', 'CHECKPOINTED after site (i) at b424; the author`s word opens the next.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423; trigger: the author rules on it.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING', 'ROUTED at b424.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; unedited by this act.'),
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
    L = ['', MARK, '',
         '### b425 — the falsifier read, sortie leg 3 — filed 2026-09-11', '',
         '#### The lane’s commitment and its condition, at their pins', '',
         'The dark-energy mode’s equation of state is `w = −1` (`FANO_DERIVATION_OF_LAMBDA.md` lines 26 and 119; '
         '`STORMER.md` line 123), and the lane’s condition is *“Evolving dark energy refutes the decomposition”* '
         '(`FORMATION_DISTANCE.md` line 160), naming its test as DESI year-3 and stating no significance. FANO line 246 '
         'leaves the residual’s `w` unspecified. The withdrawn dark-variable document’s weaker *“would constrain it”* does '
         'not govern.', '',
         '#### The sources, chosen by the rule fixed on the locked face', '',
         'Three queries of the arXiv listing, twenty-five newest results each, every result printed; qualifying on a '
         'supernova sample, a test of `w = −1` against an evolving equation of state, and a significance stated in the '
         'abstract; the newest DESI-second-release-titled result first, then the newest others; capped at three, each '
         'hashed and its text on disk:', '']
    for s in SRC:
        L.append('- **arXiv:%s** — %s — part (a): %s; part (c): **%s**.' % (s['id'], tidy(s['title']), tidy(s['same']), s['verdict']))
    L += ['']
    if FIRED:
        L += ['**BY THE LOCKED RULE, THE LANE’S CONDITION READS FIRED AT %d OF %d SOURCES (%s): the source states, in its own '
              'word, that the standard model is excluded — at 2.50σ CL, in the sentence that calls it a moderate preference.** '
              '**The register row carrying the lane — `REGISTRY.md` `p2-d6` — and `FORMATION_DISTANCE.md` line 160 are named as '
              'the author’s to move.** No lane verdict is changed by the seat. The other %d read UNDECIDED: a preference at '
              '3 to 4σ, with no exclusion stated.' % (len(FIRED), N, ', '.join('arXiv:' + x for x in FIRED), NUND), '']
    L += ['#### Routed to the author and not ruled', '',
          '(1) The FIRED clause keys on a source’s own word, used here at 2.50σ CL. (2) The selection window was the newest '
          'twenty-five results per query, so the DESI collaboration’s own second-release paper fell outside it. (3) The '
          'sources disagree under the rule and the face fixed no rule for combining them. Trail O.8 keeps the DESI '
          'five-year release open.', '',
          '#### The four lists', '',
          FOUR, '',
          '#### What this act did not do', '',
          '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 lane verdicts '
          'changed. 0 lane documents or register rows edited. 0 fits, samples or likelihoods. 0 rules struck or amended. '
          '0 orientation-layer lines edited. 0 locked faces edited. 0 prior banks edited. 0 banked ferries edited. 0 kernel '
          'files touched. 0 deposit actions; the only hosts reached were the arXiv listing’s. **And h2 where the deposit '
          'left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS THE LANE'S FALSIFICATION CONDITION READ AGAINST THREE SOURCES CHOSEN BY A LOCKED RULE, "
         "AND ROUTED. ### IT CHANGES NO LANE VERDICT, EDITS NO LANE DOCUMENT OR REGISTER ROW, AND TOUCHES NO KERNEL")


def corr_rows():
    m = ROWMARK + " (b425, sortie leg 3)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, SEARCH OR FETCH**, chained on b378's gate run as b425 -- "
            "@GR@ gates read, @GDG@ checked by digest. **THE LANE: w = −1 FOR THE DARK-ENERGY MODE (FANO 26, 119; STORMER "
            "123); THE CONDITION: 'EVOLVING DARK ENERGY REFUTES THE DECOMPOSITION' (FORMATION_DISTANCE.md 160), NO "
            "SIGNIFICANCE STATED.** **THREE arXiv SOURCES CHOSEN BY THE RULE, EACH HASHED: @PER@.** @FIREDLINE@ **ROUTED: "
            "THE RULE'S THREE LIMITS.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    fired_line = ("**BY THE LOCKED RULE THE CONDITION READS FIRED AT %s; REGISTRY.md p2-d6 AND FORMATION_DISTANCE.md LINE 160 ARE "
                  "THE AUTHOR'S TO MOVE; NO LANE VERDICT CHANGED BY THE SEAT.**" % ', '.join(FIRED)) if FIRED else '**NOT FIRED.**'
    term = "NO TERMINAL ADDED OR MOVED. The lane's documents and register rows read at their pins, not edited"
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX; NO LANE DOCUMENT, NO REGISTER ROW, "
            "NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, ROUTE OR RULE -- 0 CONTENT LOST")
    grade = ("### EACH SOURCE WAS CHOSEN BY A RULE FIXED BEFORE THE SEARCH AND DECIDED BY A RULE FIXED BEFORE THE READ, IN ITS "
             "OWN WORDS; THE RULES' LIMITS WERE PRINTED RATHER THAN REPAIRED")
    status = ("data/b425_the_falsifier_read.txt; data/b425_the_read.txt; data/b425_locate.txt; data/b425_source_*.txt; "
              "data/b425_registration_2026-09-11.txt (LOCKED at sha256 %s); PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md "
              "row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@PER@', '; '.join('%s %s' % (s['id'], s['verdict']) for s in SRC)).replace('@FIREDLINE@', fired_line))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the falsifier read', 'desi w = -1 test', 'evolving dark energy against the lane',
           'the cosmology lane falsification condition', 'b425 sortie leg 3')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-falsifier-read'


def do_key(rownum):
    statement = (
        "b425 READ THE COSMOLOGY LANE'S CONDITION -- w = −1 FOR THE DARK-ENERGY MODE; 'EVOLVING DARK ENERGY REFUTES THE "
        "DECOMPOSITION' (FORMATION_DISTANCE.md 160) -- AGAINST THREE arXiv SOURCES CHOSEN BY A LOCKED RULE: %s. %s No lane "
        "verdict changed by the seat; the rule's limits ROUTED."
        % ('; '.join('%s %s' % (s['id'], s['verdict']) for s in SRC),
           ('**FIRED BY THE RULE AT %s; REGISTRY p2-d6 AND FORMATION_DISTANCE.md 160 ARE THE AUTHOR`S TO MOVE.**' % ', '.join(FIRED))
           if FIRED else 'NOT FIRED.'))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b425_the_falsifier_read.txt; data/b425_the_read.txt; data/b425_locate.txt; "
             "data/b425_registration_2026-09-11.txt (LOCKED, %d gates read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
             % (GR, GDG, rownum))
    act = "b425 (sortie leg 3: the falsifier read)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FALSIFIER READ (b425).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b425 key : %s' % (qq[:58], g2))
    for lbl, cond in (('per-source verdicts carried', all(('%s %s' % (s['id'], s['verdict'])) in out for s in SRC)),
                      ('the author`s to move carried', ('AUTHOR`S TO MOVE' in out) if FIRED else True),
                      ('routed carried', 'ROUTED' in out)):
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
    B = ['=' * 100, 'b425 -- THE FALSIFIER READ. SORTIE LEG 3.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    comp = read(os.path.join(D, 'b425_components.txt'))
    B += ['', '-' * 100, '### THE EXPECTATION, AS THE REPORT SCORED IT.', '-' * 100]
    B += [ln for ln in comp.splitlines() if ln.strip().startswith('(L3)')]
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
    rec('b425_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or N == 0:
        rec('  ### HARD FAILURE -- the lock gate`s record or the read is missing.')
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
    at = lambda mk, s: [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b424`s row by its marker : %s' % at(B424ROW, txt))
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
    rec('  after -- b424`s : %s ; this act`s, by its marker : %s' % (at(B424ROW, after), at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b425_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
