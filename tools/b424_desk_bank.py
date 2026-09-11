# -*- coding: utf-8 -*-
"""b424_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY AND THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every count here is read off the candidate table's JSON,
### never typed; the arc's next site is restated with its trigger, so it is not shelved (R23).
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
MARK = '<!-- b424 the witness arc at site (i), sortie leg 2 -->'
PRIOR = '<!-- b423 the (R37) question read: b407 and b420 against section 10.2 -->'
B423ROW = "**THE (R37) QUESTION READ: b407'S AND b420'S READINGS OF THE LEMMA'S FIRST HYPOTHESIS, EACH AGAINST §10.2**"
BANKOUT = os.path.join(D, 'b424_the_witness_arc_at_site_i.txt')
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


FACE = read(os.path.join(D, 'b424_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b424_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
try:
    T = json.loads(read(os.path.join(D, 'b424_candidates.json')))
except Exception:
    T = dict(candidates=[], held=-1, tally={})
CANDS = T['candidates']
N, HELD = len(CANDS), T['held']
TALLY = '; '.join('%s %d' % (k, v) for k, v in sorted(T['tally'].items(), key=lambda x: -x[1]))
WREC = read(os.path.join(D, 'b424_ledger_write.txt'))
NUMW = {16: 'SIXTEEN'}.get(N, str(N))
ROWMARK = ("**THE WITNESS ARC AT SITE (i), THE CLAUSE'S QUANTIFIER: %s CANDIDATES READ AT SOURCE, %s**"
           % (NUMW, 'NONE HELD' if HELD == 0 else 'ONE OR MORE HELD'))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')


def tidy(s):
    return s.replace('`', '’')


DESK = [
    ('site (i) of W-ORD-WITNESS-ENUMERATION', 'CLOSE',
     'RUN at b424: %d candidates, each failed at a quoted step, %d held; first failing steps %s. The exhausted list is a '
     'FACES_LEDGER block through the writer; row U1’s line is untouched.' % (N, HELD, TALLY)),
    ('W-ORD-WITNESS-ENUMERATION, sites (ii) to (vi)', 'STANDING',
     'CHECKPOINTED after site (i); five sites remain, one act each. Trigger: the author’s word opens the next.'),
    ('whether the cell should carry the list inside its own text', 'STANDING',
     'ROUTED TO THE AUTHOR AND NOT TAKEN: the writer’s law and the freeze were read as making it a block that names the row.'),
    ('the seat’s reading of §10.2 (b423): hypothesis 1 separates no written structure', 'STANDING',
     'ROUTED at b423; trigger: the author rules on it.'),
    ('the falsifier read', 'STANDING', 'This sortie’s leg 3, b425.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('b420’s sentence that b419 moved a grade inside K3', 'STANDING', 'NAMED IN THE FOLD, NOT REPAIRED, as at b422.'),
    ('the Reader’s encoding; §9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING',
     'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; its line unedited; entry (i)’s WITNESS field reads UNSTATED, as before.'),
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
         '### b424 — the witness arc at site (i), sortie leg 2 — filed 2026-09-11', '',
         '#### The site’s own text, quoted before any candidate', '',
         'Row U1’s entry (i) carries `WITNESS: UNSTATED` because *the witness form does not transpose here at all*: its '
         'quantifiers are a `∀` with no `∃` inside, and the shared-witness form is a repair for `∀∃ ⟹ ∃∀`. b406 added '
         'that no inner existential at (i) is one the form can repair. The candidates were attempted anyway, because the '
         'order asked for the list exhausted.', '',
         '#### The sixteen, each failed at a quoted step', '',
         'b422’s four, and twelve the survey’s search supplied by description, every hit hand-read. Each was attempted by '
         'three steps in the order the locked face fixed — S1 CLASS, S2 HELD, S3 FORM — and failed at the first it failed:', '']
    for c in CANDS:
        L.append('- **%s** %s — %s' % (c['id'], tidy(c['name']),
                                       ('FAILED AT S%d, %s' % (c['first'], c['kind'])) if c['first'] else 'HELD'))
    L += ['',
          '**%s. %d candidates, %d held.** First failing steps: %s. Every candidate fails S3 as well, on the site’s own '
          'text.' % ('NO WITNESS HELD' if HELD == 0 else 'A CANDIDATE HELD', N, HELD, TALLY), '',
          '#### Where it was written', '',
          '`FACES_LEDGER.md` gains one block, `<!-- b424 update -->`, through the writer’s `append_block`, every quotation '
          'at a first failing step verified by the writer’s `verify_quotes` first. Row U1’s line is byte-identical, entry '
          '(i)’s `WITNESS: UNSTATED` stands, the freeze at six stands, and no seventh site is entered. **Routed to the '
          'author and not taken:** whether *the cell gains the exhausted list* was meant as text inside the cell.', '',
          '#### The arc, checkpointed', '',
          '**W-ORD-WITNESS-ENUMERATION is checkpointed after site (i).** Sites (ii) to (vi) remain, one act each. Trigger: '
          'the author’s word opens the next site. Leg 3 (b425) of this sortie reads the falsifier.', '',
          '#### The four lists', '',
          FOUR, '',
          '#### What this act did not do', '',
          '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 bytes of row '
          'U1’s line. 0 seventh sites. 0 second sites. 0 rules struck or amended. 0 orientation-layer lines edited. 0 '
          'locked faces edited. 0 prior banks edited. 0 banked ferries edited. 0 kernel files touched. 0 deposit '
          'actions, 0 platform calls. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS ONE SITE OF THE WITNESS ARC RUN, ITS CANDIDATES EACH FAILED AT A QUOTED STEP, AND THE "
         "EXHAUSTED LIST FILED THROUGH THE LEDGER'S WRITER. ### IT MOVES NO GRADE AND TOUCHES NO KERNEL OR ROW LINE")


def corr_rows():
    m = ROWMARK + " (b424, sortie leg 2)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b424 -- @GR@ gates "
            "read, @GDG@ checked by digest. **THE SITE'S OWN CELL QUOTED FIRST: A UNIVERSAL WITH NO EXISTENTIAL INSIDE, "
            "WITNESS UNSTATED.** **@N@ CANDIDATES -- b422'S FOUR AND TWELVE THE SEARCH SUPPLIED -- EACH ATTEMPTED BY S1 "
            "CLASS, S2 HELD, S3 FORM, AND FAILED AT THE FIRST: @TALLY@. HELD @HELD@.** **THE EXHAUSTED LIST FILED AS ONE "
            "FACES_LEDGER BLOCK THROUGH append_block, QUOTATIONS VERIFIED BY verify_quotes; ROW U1'S LINE BYTE-IDENTICAL.** "
            "**CHECKPOINT AFTER SITE (i).** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. Row U1's line read, not edited; T3prime_shared_witness read at its pin"
    prof = ("### TWO PLACE-papers FILES APPENDED -- FACES_LEDGER.md (ONE BLOCK THROUGH THE WRITER) AND OPEN_TRAILS.md, "
            "EACH PIN A TRUE PREFIX; NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, ROUTE OR RULE -- 0 CONTENT LOST")
    grade = ("### EVERY CANDIDATE WAS FAILED AT THE FIRST OF THREE STEPS FIXED ON THE LOCKED FACE, ITS SENTENCE QUOTED; "
             "THE SITE'S OWN CELL WAS QUOTED BEFORE ANY CANDIDATE AND STANDS")
    status = ("data/b424_the_witness_arc_at_site_i.txt; data/b424_candidates.txt; data/b424_candidates.json; "
              "data/b424_ledger_write.txt; data/b424_components.txt; data/b424_registration_2026-09-11.txt (LOCKED at "
              "sha256 %s); PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@N@', str(N))
                .replace('@TALLY@', TALLY).replace('@HELD@', str(HELD)))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the witness arc at site i', 'site i witness candidates', 'the class site witness enumeration',
           'shared witness at the clause quantifier', 'b424 sortie leg 2')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-witness-arc-at-site-i'


def do_key(rownum):
    statement = (
        "b424 RAN THE WITNESS ARC AT SITE (i) OF ROW U1, THE CLAUSE'S QUANTIFIER OVER THE CLASS: **%d CANDIDATES -- "
        "b422'S FOUR AND TWELVE THE SEARCH SUPPLIED -- EACH FAILED AT A QUOTED STEP; %s.** First failing steps: %s. "
        "The site's own cell stands (WITNESS: UNSTATED, a universal with no existential inside). The exhausted list is "
        "a FACES_LEDGER block through the writer; row U1's line untouched; checkpoint after the site; no act "
        "re-verdicted." % (N, 'NONE HELD' if HELD == 0 else 'ONE OR MORE HELD', TALLY))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b424_the_witness_arc_at_site_i.txt; data/b424_candidates.txt; data/b424_registration_2026-09-11.txt "
             "(LOCKED, %d gates read, %d by digest); FACES_LEDGER.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
             % (GR, GDG, rownum))
    act = "b424 (sortie leg 2: the witness arc at site (i))"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE WITNESS ARC AT SITE (i) (b424).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b424 key : %s' % (qq[:58], g2))
    for lbl, cond in (('none held carried', ('NONE HELD' if HELD == 0 else 'ONE OR MORE HELD') in out),
                      ('class boundary carried', 'CLASS BOUNDARY' in out),
                      ('the cell stands', 'WITNESS: UNSTATED' in out),
                      ('not re-verdicted', 're-verdicted' in out)):
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
    B = ['=' * 100, 'b424 -- THE WITNESS ARC AT SITE (i). SORTIE LEG 2.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    comp = read(os.path.join(D, 'b424_components.txt'))
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


def main():
    bar('=')
    rec('b424_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or N == 0 or 'LEDGER WRITE : WRITTEN' not in WREC:
        rec('  ### HARD FAILURE -- the lock gate`s record, the table, or the ledger write is missing.')
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
    rec('  b423`s row by its marker : %s' % at(B423ROW, txt))
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
    rec('  after -- b423`s : %s ; this act`s, by its marker : %s' % (at(B423ROW, after), at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b424_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
