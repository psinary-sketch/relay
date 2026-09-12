# -*- coding: utf-8 -*-
"""b426_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every verdict here is read off the read's JSON, never typed.
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
MARK = '<!-- b426 the falsifier re-read by address, sortie leg 1 -->'
PRIOR = '<!-- b425 the falsifier read, sortie leg 3 -->'
B425ROW = ("**THE FALSIFIER READ: THE LANE'S w = −1 AGAINST THREE SUPERNOVA RESULTS -- "
           "FIRED AT 1 BY THE LOCKED RULE, UNDECIDED AT 2**")
BANKOUT = os.path.join(D, 'b426_the_address_reread.txt')
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


FACE = read(os.path.join(D, 'b426_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1]).group(1)
LG = read(os.path.join(D, 'b426_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)
try:
    J = json.loads(read(os.path.join(D, 'b426_the_address_read.json')))
except Exception:
    J = dict(address=[], prior=[], any_clause=None, weakest_clause=None, diverge=None, fired=None)
ADDR = J.get('address', [])
PRIORS = J.get('prior', [])
ANY_, WEAK = J.get('any_clause'), J.get('weakest_clause')
DIVERGE, FIREDQ = J.get('diverge'), J.get('fired')
A0 = ADDR[0] if ADDR else {}
SUMMARY = ('%s BY THE WEAKEST READING, %s BY THE ANY-SOURCE CLAUSE' % (WEAK, ANY_)) if DIVERGE else ('%s' % WEAK)
ROWMARK = "**THE FALSIFIER RE-READ BY ADDRESS UNDER (R38): %s, AND (R38)'S TWO CLAUSES DIVERGE**" % SUMMARY \
    if DIVERGE else "**THE FALSIFIER RE-READ BY ADDRESS UNDER (R38): %s**" % SUMMARY

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')


def persrc():
    out = []
    for o in ADDR:
        out.append('%s %s/%s' % (o['id'], o['low_verdict'], o['high_verdict']))
    for p in PRIORS:
        out.append('%s %s/%s' % (p['id'], p['low_verdict'], p['high_verdict']))
    return '; '.join(out)


DESK = [
    ('the falsifier re-read by address', 'CLOSE',
     'READ at b426: the collaboration`s own second-release paper located by address (%s), hashed and read at content; '
     'b425`s three restated under (R38). Per source, low/high: %s.'
     % (A0.get('id', 'NOT LOCATED'), persrc())),
    ('the lane`s condition under (R38)', 'STANDING',
     'Combined reading carried: %s (the weakest). The any-source clause reads %s. FIRED (five sigma) reached: %s. '
     'p2-d6 does not move; the row is the author`s to move if (R38) fires.' % (WEAK, ANY_, FIREDQ)),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING' if DIVERGE else 'CLOSE',
     'ROUTED TO THE AUTHOR AND NOT RULED: *"from any source read at address"* reads the set at its strongest member, '
     '*"combined by the WEAKEST reading"* at its weakest; both answers printed.' if DIVERGE
     else 'The two clauses agree on this set; nothing to route.'),
    ('b425`s three limits (a word, a window, no combining rule)', 'CLOSE',
     '(R38) answers all three: the word is replaced by a threshold, the window is closed by reading the '
     'collaboration`s own paper at address, and a combining rule is supplied. A FOURTH limit is opened in their '
     'place and stands above: the combining rule`s own two clauses diverge.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged; the lane`s own STORMER.md names it.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (ii) to (vi)', 'STANDING',
     'CHECKPOINTED after site (i) at b424; site (ii) is this sortie`s leg 2 (b427).'),
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
         '### b426 — the falsifier re-read by address, sortie leg 1 — filed 2026-09-11', '',
         '#### The two rulings, carried as quoted', '',
         '**`(R38)`** keys the lane’s falsification condition on a **threshold, not a word**: UNDER PRESSURE at a '
         'stated preference of three sigma or more from any source read at address; FIRED at five sigma from the '
         'collaboration’s own paper or from two independent analyses each at five; UNDECIDED below three; a source’s '
         'own word quoted and never governing; disagreeing sources combined by the **weakest** reading. **`(R39)`** '
         'holds `p2-d6` in place and gives its status a note. Both are the author’s, ratified by the b426 paste, and '
         'neither is extended here.', '']
    if A0:
        L += ['#### The address, located by the rule and read at content', '',
              '**arXiv:%s** — %s — located by three printed queries of the arXiv listing, qualifying on a title naming '
              'DESI’s second data release, a title naming cosmological constraints or BAO, and an author field naming '
              'the collaboration itself; abstract page and PDF hashed, their text on disk. **Part (a): %s.** '
              '**Part (c), at the paper’s own figures (%s–%sσ): low end %s, high end %s.**'
              % (A0['id'], tidy(A0['title']), tidy(A0['same']), A0['low'], A0['high'],
                 A0['low_verdict'], A0['high_verdict']), '']
    else:
        L += ['#### The address', '',
              '**NOT LOCATED.** No result satisfied the three tests the locked face fixed, and the rule was not '
              'widened to find one.', '']
    L += ['#### b425’s three, re-scored under `(R38)`', '']
    for p in PRIORS:
        L.append('- **arXiv:%s** — b425 read **%s** on the source’s own word; under `(R38)`, at %s–%sσ: low end '
                 '**%s**, high end **%s**.' % (p['id'], p['b425'], p['low'], p['high'], p['low_verdict'], p['high_verdict']))
    L += ['',
          '**The combined reading carried is the weakest: %s.** The same ruling’s *“from any source read at address”* '
          'clause reads **%s** on the same set — **the two clauses of `(R38)` do not agree on a mixed set, and that '
          'divergence is the rule’s and not the set’s.** It is printed rather than repaired and **routed to the author '
          'unruled**. **FIRED requires five sigma and no source in the set states five sigma at either end**, so '
          '`p2-d6` does not move; the row stays the author’s to move if `(R38)` fires.'
          % (WEAK, ANY_) if DIVERGE else
          '**The combined reading is %s**, both clauses of `(R38)` agreeing on this set.' % WEAK, '',
          '#### What was written into the lane, and nothing else', '',
          '`FORMATION_DISTANCE.md` gains **one inserted line** after line 160 carrying `(R38)`’s clause, with line 160 '
          '**byte-identical**; `REGISTRY.md`’s `p2-d6` row gains a note **inside its status cell**, every other cell '
          'byte-identical and the register sentence unchanged. Each was preserved verbatim with its sha256 in a record '
          'written **before** the edit. **No lane verdict is changed by the seat.**', '',
          '#### The four lists', '',
          FOUR, '',
          '#### What this act did not do', '',
          '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa measured. 0 lane '
          'verdicts changed. 0 rows of `FACES_LEDGER.md`. 0 fits, samples or likelihoods; 0 significances converted. '
          '0 rules struck, amended or widened by the seat. 0 orientation-layer lines edited. 0 locked faces edited. '
          '0 prior banks edited. 0 banked ferries edited. 0 kernel files touched. 0 deposit actions; the only hosts '
          'reached were the arXiv listing’s. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS THE LANE'S FALSIFICATION CONDITION RE-READ UNDER (R38) AGAINST THE COLLABORATION'S OWN "
         "PAPER AT ADDRESS, AND ROUTED. ### IT CHANGES NO LANE VERDICT AND TOUCHES NO KERNEL")


def corr_rows():
    m = ROWMARK + " (b426, sortie leg 1)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, SEARCH OR FETCH**, chained on b378's gate run as "
            "b426 -- @GR@ gates read, @GDG@ checked by digest. **(R38) AND (R39) CARRIED AS QUOTED FROM THE BANKED "
            "FERRY; NEITHER EXTENDED.** **THE ADDRESS: @ADDR@, HASHED AND READ AT CONTENT.** **PER SOURCE, LOW/HIGH "
            "UNDER (R38): @PER@.** @DIVLINE@ **FIRED (FIVE SIGMA) REACHED: @FIRED@ -- p2-d6 DOES NOT MOVE.** "
            "0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    divline = (("**(R38)'S TWO CLAUSES DIVERGE ON THIS SET: ANY-SOURCE %s, WEAKEST %s; THE WEAKEST IS CARRIED AND THE "
                "DIVERGENCE IS ROUTED TO THE AUTHOR UNRULED.**" % (ANY_, WEAK)) if DIVERGE
               else ("**BOTH CLAUSES OF (R38) AGREE: %s.**" % WEAK))
    term = "NO TERMINAL ADDED OR MOVED. The lane's register sentence unchanged; its status cell gains a note per (R39)"
    prof = ("### THREE PLACE-papers FILES WRITTEN -- OPEN_TRAILS.md APPENDED (pin a true prefix); "
            "FORMATION_DISTANCE.md ONE INSERTED LINE AFTER LINE 160, LINE 160 BYTE-IDENTICAL; REGISTRY.md p2-d6 STATUS "
            "CELL ONLY, EVERY OTHER CELL BYTE-IDENTICAL -- EACH PRESERVED VERBATIM WITH ITS SHA256 BEFORE THE EDIT; "
            "NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, ROUTE OR RULE -- 0 CONTENT LOST")
    grade = ("### THE ADDRESS WAS CHOSEN BY A RULE FIXED BEFORE THE SEARCH AND SCORED BY (R38)'S THRESHOLDS ON FIGURES "
             "THE SOURCE STATES IN ITS OWN WORDS; A RANGE WAS READ AT BOTH ENDS AND A SPANNING SOURCE RECORDED AS "
             "SPANNING; THE RULE'S OWN DIVERGENCE WAS PRINTED RATHER THAN REPAIRED")
    status = ("data/b426_the_address_reread.txt; data/b426_the_address_read.txt; data/b426_locate.txt; "
              "data/b426_source_*.txt; data/b426_writes.txt; data/b426_preserved_*.txt; "
              "data/b426_registration_2026-09-11.txt (LOCKED at sha256 %s); PLACE-papers OPEN_TRAILS.md, "
              "FORMATION_DISTANCE.md, REGISTRY.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@ADDR@', ('arXiv:' + A0['id']) if A0 else 'NOT LOCATED')
                .replace('@PER@', persrc()).replace('@DIVLINE@', divline).replace('@FIRED@', str(FIREDQ)))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the falsifier re-read by address', 'r38 threshold rule', 'desi dr2 collaboration paper read',
           'the lane condition under r38', 'b426 sortie leg 1')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved')
KEY = 'the-falsifier-reread-by-address'


def do_key(rownum):
    statement = (
        "b426 RE-READ THE COSMOLOGY LANE'S CONDITION UNDER (R38)'S THRESHOLDS AGAINST THE DESI COLLABORATION'S OWN "
        "SECOND-RELEASE PAPER AT ADDRESS (%s) AND b425'S THREE: %s. COMBINED BY THE WEAKEST READING: %s; THE "
        "ANY-SOURCE CLAUSE READS %s. %s No lane verdict changed by the seat; the divergence ROUTED."
        % (('arXiv:' + A0['id']) if A0 else 'NOT LOCATED', persrc(), WEAK, ANY_,
           ('**FIRED (FIVE SIGMA) IS REACHED; REGISTRY p2-d6 IS THE AUTHOR`S TO MOVE.**' if FIREDQ
            else 'FIRED (five sigma) NOT reached; p2-d6 does not move.')))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED, NO PREMISE DISCHARGED. ### NOTHING DEPOSITS"
    where = ("data/b426_the_address_reread.txt; data/b426_the_address_read.txt; data/b426_locate.txt; "
             "data/b426_writes.txt; data/b426_registration_2026-09-11.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; FORMATION_DISTANCE.md; REGISTRY.md p2-d6; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b426 (sortie leg 1: the falsifier re-read by address)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FALSIFIER RE-READ BY ADDRESS (b426).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b426 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the weakest reading carried', (WEAK or 'x') in out),
                      ('the any-source clause carried', (ANY_ or 'x') in out),
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
    B = ['=' * 100, 'b426 -- THE FALSIFIER RE-READ BY ADDRESS. SORTIE LEG 1.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    comp = read(os.path.join(D, 'b426_components.txt'))
    B += ['', '-' * 100, '### THE EXPECTATION, AS THE REPORT SCORED IT.', '-' * 100]
    B += [ln for ln in comp.splitlines() if ln.strip().startswith('(L1)')]
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
    rec('b426_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or not ADDR:
        rec('  ### HARD FAILURE -- the lock gate`s record or the address read is missing.')
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
    rec('  b425`s row by its marker : %s' % at(B425ROW, txt))
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
    rec('  after -- b425`s : %s ; this act`s, by its marker : %s' % (at(B425ROW, after), at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b426_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
