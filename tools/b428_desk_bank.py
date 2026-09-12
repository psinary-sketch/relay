# -*- coding: utf-8 -*-
"""b428_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off a component's JSON,
### never typed; the trail block carries Component 2's filing and Component 3's price.
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
MARK = '<!-- b428 site (iii), the disproof lane named, the external read priced -->'
PRIOR = '<!-- b427 the witness arc at site (ii), sortie leg 2 -->'
BANKOUT = os.path.join(D, 'b428_site_iii_and_two_filings.txt')
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


FACE = read(os.path.join(D, 'b428_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b428_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)


def loadj(name, default):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return default


J = loadj('b428_candidates.json', dict(candidates=[], held=0, tally={}, site_i={}, site_i_n=0, site_ii={},
                                       site_ii_n=0, same=0, diff=0, newkinds=[], shared=[],
                                       class_share=[[0, 0, 0], [0, 0, 0]], union_kinds=[]))
DJ = loadj('b428_disproof_lane.json', dict(counts={}, opened=None))
PJ = loadj('b428_external_price.json', dict(probed=[], located=[], acts=0, priced_acts=0, unpriceable_acts=0))
CANDS = J['candidates']
N, HELD, TALLY = len(CANDS), J['held'], J['tally']
CB, NS = J['class_share']
NEWK, SHARED = J['newkinds'], J['shared']
TALLYSTR = '; '.join('%s %d' % (k, v) for k, v in sorted(TALLY.items(), key=lambda x: (-x[1], x[0])))
FEAS = (DJ.get('counts', {}).get('a feasible-reach question', {}) or {}).get('hits')
ROWMARK = ("**SITE (iii), THE WIDTH COORDINATE'S UNION: %d CANDIDATES READ AT SOURCE, %s; "
           "THE DISPROOF LANE NAMED AND NOT OPENED; THE EXTERNAL READ PRICED AND NOT LOCATED**"
           % (N, 'NONE HELD' if HELD == 0 else ('%d HELD' % HELD)))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('site (iii) of W-ORD-WITNESS-ENUMERATION', 'CLOSE',
     'READ at b428: %d candidates, each read at its source and attempted by S1 CLASS, S2 HELD, S3 FORM in b424`s '
     'fixed order; HELD %d. First failing steps by kind: %s.' % (N, HELD, TALLYSTR)),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word opens the next.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED AND NOT RULED, now measured at THREE sites. The class boundary`s share: (i) %d of %d, (ii) %d of %d, '
     '(iii) %d of %d -- it FELL and then rose, and did not rise monotonically. Distinct kinds: (i) %d, (ii) %d, '
     '(iii) %d, UNION over the three %d -- the union is still growing, by %d new kinds at this site (%s).'
     % (CB[0], NS[0], CB[1], NS[1], CB[2], NS[2], len(J['site_i']), len(J['site_ii']), len(TALLY),
        len(J['union_kinds']), len(NEWK), ', '.join(NEWK) or 'none')),
    ('the disproof lane, named and not opened (b428)', 'STANDING',
     'FILED at b428: the corpus holds a certified disproof instrument (F7, the phase condition, the aim map) and a '
     'search over the record`s banks and ledgers returns %s hit(s) for a question about feasible reach. The barrier '
     'keystone`s own clause names no direction, so the proof and disproof lanes are symmetric under the corpus`s own '
     'theory. TRIGGER: the instrument lane opening. NOTHING OPENED.' % FEAS),
    ('the external grading read, priced and NOT LOCATED (b428)', 'STANDING',
     'PRICED at b428 at %d acts, %d priceable and %d UNPRICEABLE FROM BANKED FIGURES; %d of %d candidate addresses '
     'resolved. TRIGGER: the author supplies the address. NOT RUN.'
     % (PJ.get('acts', 0), PJ.get('priced_acts', 0), PJ.get('unpriceable_acts', 0),
        len(PJ.get('located', [])), len(PJ.get('probed', [])))),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424 and still routed; this act appended a third block rather than write inside the cell.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423; trigger: the author rules on it.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane -- and F7 names the same seed the disproof lane would need.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item; trigger: the author opens an instrument lane.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; its line unedited by this act, entry (iii)`s WITNESS still NONE KNOWN.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
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
         '### b428 — site (iii), and two filings from outside — filed 2026-09-12', '',
         '#### Component 1 — the witness arc at site (iii), the width coordinate’s union', '',
         'Row U1’s entry (iii) carries `WITNESS: NONE KNOWN`. The class is the **union over all support widths** — '
         'the criterion quantifies over *“all g in Cc^infty(R+*) with g~(z) = 0 for all z in F”* — while the located '
         'statement exhausts the admissible class **at** a width: *“AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION '
         'ACROSS WIDTHS.”* **And this is the one site of the six whose own banked text supplies the inner existential '
         'in the theorem’s shape**, so the shared-witness form transposes here and what is missing is the object, not '
         'the shape.', '',
         'The navigator’s opening three — monotonicity in the radius; a limit across radii; Boas–Kac at each radius as '
         'the existential the site owns — and %d the search supplied by description, every hit hand-read. Each was '
         'attempted by S1 CLASS, S2 HELD, S3 FORM and failed at the first it failed:' % (N - 3), '']
    for c in CANDS:
        L.append('- **%s** %s — FAILED AT S%s, %s' % (c['id'], tidy(c['name']), c['first'], c['kind']))
    L += ['',
          '**NO WITNESS HELD. %d candidates, %d held.** First failing steps: %s.' % (N, HELD, TALLYSTR), '',
          '**The boundary count at three sites, measured rather than recalled.** The class boundary’s share: '
          '(i) %d of %d, (ii) %d of %d, (iii) %d of %d. Distinct boundary kinds: (i) %d, (ii) %d, (iii) %d, '
          '**union over the three %d**. At this site %d of %d failures land at a boundary an earlier site also used '
          'and %d of %d at a kind new here (%s). **The share fell and then rose rather than rising, and the union of '
          'kinds is still growing — so the arc is still not converging on a single boundary.** Stated as the two '
          'counts show it and no further.'
          % (CB[0], NS[0], CB[1], NS[1], CB[2], NS[2], len(J['site_i']), len(J['site_ii']), len(TALLY),
             len(J['union_kinds']), J['same'], N, J['diff'], N, ', '.join(NEWK) or 'none'), '',
          'Written to `FACES_LEDGER.md` as `<!-- b428 update -->` through the writer’s `append_block`, every quotation '
          'verified first. Row U1’s line is byte-identical, entry (iii)’s `WITNESS: NONE KNOWN` stands, the freeze at '
          'six stands, no seventh site is entered.', '',
          '#### Component 2 — the disproof lane, NAMED AND NOT OPENED', '',
          '**The corpus holds a certified disproof instrument and has never pointed it.** Row `F7` is the Epstein '
          'negative control — *“the arc’s instrument aimed at Z_Q (x² + xy + 6y², disc −23, h = 3), a positive Li '
          'ledger with RH false”* — and it already states its own limit: *“A FAMILY THAT SEES THE FAILURE NEEDS A '
          'SIGN”* structure the construction does not have, and the zeta window at this reach *“IS A TEST THIS FAMILY '
          'CANNOT FAIL”*. Beside it stand b328’s phase condition (the four-term sum `4 |G|² cos(2φ)`, negative exactly '
          'past forty-five degrees) and b334’s aim map, which measured the square and the remainder **NOT REACHED** at '
          'the reaching widths.', '',
          '**A search over every relay act bank, `FACES_LEDGER.md`, `FINDINGS.md` and `OPEN_TRAILS.md` returns %s hits '
          'for a question about feasible reach.** The counterexample-word hits that do exist were hand-read and every '
          'one is a statement that the instrument does *not* see counterexamples, or a figure a later act disproved — '
          'not a lane asking the question.' % FEAS, '',
          '**And the corpus’s own theory says the two lanes are symmetric.** The barrier keystone states that a method '
          'factoring through a `κ = 0` interface can establish *“P holds for x in a density-one subset of each '
          'I-class,” but cannot certify individual elements* — and *“the individual element remains unreached.”* '
          '**That clause names no direction.** Certifying that every element is on the line and certifying that one '
          'element is not are both individual-element statements, so the barrier that stops the proof lane stops the '
          'disproof lane at the same place. Proposition 3.5 is the witness that density-one and universality come '
          'apart, and it is an *Epstein* witness — the same object `F7` already holds.', '',
          '**This is not a claim that a counterexample exists, that one is findable, or that the hypothesis is false. '
          'It is a statement about which lanes the record has run.** **TRIGGER: the instrument lane opening. NOTHING '
          'IS OPENED — 0 lanes, 0 routes, 0 instruments, 0 seeds, 0 figures.**', '',
          '#### Component 3 — the external grading read, PRICED AND NOT RUN', '',
          '**NOT LOCATED.** %d candidate addresses were probed by `ls-remote`, which reads a SHA back from a remote '
          'and clones nothing; **%d resolved.** The seat holds no announcement and the corpus cites none, and the act '
          'does not widen its search until something answers — a URL guessed until it resolves is a manufactured '
          'citation. **The address is the author’s to supply.**'
          % (len(PJ.get('probed', [])), len(PJ.get('located', []))), '',
          '**The price, in acts: %d.** ACT 1 locate the terminal in the README at the pin; ACT 2 print its axiom '
          'profile; ACT 3 read its statement against the Clay formulation’s statement C, quoting both; ACT 4 grade it '
          'by the three grades — DERIVES / INTERFACES / ENCODES-CONCLUSION-or-SHELL — by reading the statement and '
          'never the announcement. **%d of those acts are reads and cost one act each. ACT 2 is not a read but a '
          'BUILD** — the toolchain the repository pins, its dependency graph, and a machine that compiles them — and '
          'the corpus has never built a foreign kernel, so **ACT 2 IS UNPRICEABLE FROM BANKED FIGURES**. The '
          'unpriceable act is the one that carries the certificate; a grading that skipped it would be grading an '
          'announcement.' % (PJ.get('acts', 0), PJ.get('priced_acts', 0)), '',
          '**The navigator’s note, entered as the order gives it:** this would be the first time the corpus’s grading '
          'discipline is aimed at a proof it did not write, and its purpose is calibration. **And one sentence the '
          'seat adds, routed and not ruled:** a discipline that has only ever graded its own work has never been '
          'tested for the failure mode that matters most — grading its own work more generously than a stranger’s. '
          'Calibration measures the instrument; it does not measure the outside proof, and an act that confused the '
          'two would be using a stranger’s work as a mirror.', '',
          '#### The four lists', '',
          FOUR, '',
          '#### What this act did not do', '',
          '0 grades moved, conferred or minted — on this corpus or any other. 0 premises discharged. 0 doors restated. '
          '0 routes proposed. 0 lanes opened. 0 kappa measured. 0 bytes of row U1’s line. 0 seventh sites. 0 witness '
          'cells written. 0 repositories cloned. 0 builds. 0 files of the external proof read at content. 0 rules '
          'struck or amended. 0 orientation-layer lines edited. 0 locked faces edited. 0 prior banks edited. 0 banked '
          'ferries edited. 0 kernel files touched. 0 deposit actions. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS AN EXHAUSTED CANDIDATE LIST AT ONE SITE OF ROW U1, A LANE NAMED AND NOT OPENED, AND A "
         "READ PRICED AND NOT RUN. ### IT CONFERS NO GRADE, OPENS NO LANE, TYPES NO BRIDGE AND TOUCHES NO KERNEL")


def corr_rows():
    m = ROWMARK + " (b428)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, ATTEMPT, SEARCH OR PROBE**, chained on b378's gate "
            "run as b428 -- @GR@ gates read, @GDG@ checked by digest. **SITE (iii): @N@ CANDIDATES, HELD @HELD@; FIRST "
            "FAILING STEPS @TALLY@.** **THE CLASS BOUNDARY'S SHARE AT THREE SITES: @SHARE@; DISTINCT KINDS @KINDS@, "
            "UNION @UNION@ -- THE SHARE DID NOT RISE MONOTONICALLY AND THE UNION IS STILL GROWING, SO THE ARC IS NOT "
            "CONVERGING ON ONE BOUNDARY.** **COMPONENT 2: THE DISPROOF LANE NAMED, @FEAS@ HITS FOR A FEASIBLE-REACH "
            "QUESTION IN THE WHOLE RECORD, THE BARRIER'S CLAUSE NAMING NO DIRECTION -- NOTHING OPENED.** "
            "**COMPONENT 3: @LOC@ OF @PROBED@ ADDRESSES RESOLVED, NOT LOCATED; PRICED AT @ACTS@ ACTS, @UNP@ "
            "UNPRICEABLE -- NOT RUN.** 0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. Row U1's line byte-identical; entry (iii)'s WITNESS cell still NONE KNOWN"
    prof = ("### TWO PLACE-papers FILES WRITTEN -- FACES_LEDGER.md ONE APPENDED BLOCK THROUGH THE WRITER'S "
            "append_block, ITS QUOTATIONS VERIFIED FIRST; OPEN_TRAILS.md ONE APPEND, ITS PIN A TRUE PREFIX; NO ROW "
            "REWRITTEN, NO SEVENTH SITE, NO KEYSTONE, NO REGISTER ROW, NO KERNEL FILE; NO GRADE, PREMISE, DOOR, KAPPA, "
            "ROUTE, LANE OR RULE -- 0 CONTENT LOST")
    grade = ("### EVERY CANDIDATE WAS READ AT ITS SOURCE OR AT THE RECORD'S QUOTATION OF IT AND FAILED AT A QUOTED "
             "STEP, A LEDGER-ROW QUOTATION READ FROM THAT ROW'S OWN LINE; THE THREE-SITE COMPARISON IS COUNTED OFF "
             "b424'S AND b427'S OWN BANKED JSON AND NOT RECALLED; THE EXTERNAL ADDRESS WAS PROBED AND REPORTED NOT "
             "LOCATED RATHER THAN GUESSED UNTIL ONE ANSWERED")
    status = ("data/b428_site_iii_and_two_filings.txt; data/b428_candidates.txt; data/b428_candidates.json; "
              "data/b428_ledger_write.txt; data/b428_disproof_lane.txt; data/b428_external_price.txt; "
              "data/b428_registration_2026-09-12.txt (LOCKED at sha256 %s); PLACE-papers FACES_LEDGER.md, "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@N@', str(N))
                .replace('@HELD@', str(HELD)).replace('@TALLY@', TALLYSTR)
                .replace('@SHARE@', '; '.join('(%s) %d of %d' % (r, a, b)
                                              for r, a, b in zip(('i', 'ii', 'iii'), CB, NS)))
                .replace('@KINDS@', '%d/%d/%d' % (len(J['site_i']), len(J['site_ii']), len(TALLY)))
                .replace('@UNION@', str(len(J['union_kinds']))).replace('@FEAS@', str(FEAS))
                .replace('@LOC@', str(len(PJ.get('located', [])))).replace('@PROBED@', str(len(PJ.get('probed', []))))
                .replace('@ACTS@', str(PJ.get('acts', 0))).replace('@UNP@', str(PJ.get('unpriceable_acts', 0))))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the witness arc at site iii', 'the width coordinate union', 'the disproof lane named',
           'the external grading read priced', 'b428 site iii and two filings')
MUST_NOT_HIT = ('the lock was overridden', 'a witness was found', 'a grade was moved', 'h2 has moved',
                'a lane was opened')
KEY = 'site-iii-and-two-filings'


def do_key(rownum):
    statement = (
        "b428 ATTEMPTED %d CANDIDATES AT ROW U1'S SITE (iii), THE WIDTH COORDINATE'S UNION -- the navigator's opening "
        "three and %d the search supplied -- EACH READ AT ITS SOURCE AND FAILED AT A QUOTED STEP. HELD %d. FIRST "
        "FAILING STEPS: %s. THE CLASS BOUNDARY'S SHARE AT THREE SITES: %s; UNION OF KINDS %d -- the arc is NOT "
        "converging on one boundary. COMPONENT 2 NAMED THE DISPROOF LANE (the barrier's clause names no direction, so "
        "the proof and disproof lanes are symmetric) AND OPENED NOTHING. COMPONENT 3 PRICED THE EXTERNAL READ AT %d "
        "ACTS, %d UNPRICEABLE, AND REPORTED THE ADDRESS NOT LOCATED; NOT RUN."
        % (N, N - 3, HELD, TALLYSTR,
           '; '.join('(%s) %d of %d' % (r, a, b) for r, a, b in zip(('i', 'ii', 'iii'), CB, NS)),
           len(J['union_kinds']), PJ.get('acts', 0), PJ.get('unpriceable_acts', 0)))
    grade = "### NO TERMINAL ADDED OR MOVED, NO GRADE MOVED OR CONFERRED, NO LANE OPENED. ### NOTHING DEPOSITS"
    where = ("data/b428_site_iii_and_two_filings.txt; data/b428_candidates.txt; data/b428_ledger_write.txt; "
             "data/b428_disproof_lane.txt; data/b428_external_price.txt; "
             "data/b428_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); FACES_LEDGER.md; "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b428 (site (iii), and two filings from outside)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### SITE (iii), AND TWO FILINGS FROM OUTSIDE (b428).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
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
        rec('    %-58s reaches the b428 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the held count carried', ('HELD %d' % HELD) in out),
                      ('the three-site share carried', 'THREE SITES' in out),
                      ('nothing opened carried', 'OPENED NOTHING' in out),
                      ('not located carried', 'NOT LOCATED' in out)):
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
    B = ['=' * 100, 'b428 -- SITE (iii), AND TWO FILINGS FROM OUTSIDE.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    comp = read(os.path.join(D, 'b428_components.txt'))
    B += ['', '-' * 100, '### THE EXPECTATIONS, AS THE REPORT SCORED THEM.', '-' * 100]
    B += [ln for ln in comp.splitlines() if ln.strip().startswith(('(N1)', '(N2)'))]
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
          '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


B427ROW_RE = r'(?m)^\| (\d+) \| \*\*THE WITNESS ARC AT SITE \(ii\)'


def main():
    bar('=')
    rec('b428_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g or N == 0:
        rec('  ### HARD FAILURE -- the lock gate`s record or the candidate table is missing.')
        return 1
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED -- IT CARRIES ALL THREE COMPONENTS.')
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
    rec('  b427`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B427ROW_RE, txt)])
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
    rec('  after -- b427`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B427ROW_RE, after)], at(ROWS2[0][0], after)))
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
    io.open(os.path.join(D, 'b428_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
