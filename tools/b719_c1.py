# -*- coding: utf-8 -*-
"""b719_c1.py -- COMPONENT 1 OF b719, (R329)(2)-(5): b718 AT ITS WEIGHT, THE CORRIGENDUM FOR b718, THE ELEVEN DIFFERS AND THE ERRATA ENTRY.
Written whole at b719 by the Write tool (no carry: b718's corrigendum tool composed b717's ten events and five items).

Routes, each `dry` (prints the text and the screens, writes nothing) or `write` (lands through b698's guarded landing, banks the line):
  weight       FINDINGS: b718's weight line after its entry (:10858), every figure read from b718's banks by line ((R329)(2)).
  corrigendum  FINDINGS: the corrigendum for b718 from data/b718_events.txt (1)-(13), data/b718_defects.txt and data/b718_hook_refusals.txt,
               each item CLAIM or CLOSE and NEW or REPEAT read from its own bracket; the refusals answered by the letter or event that
               records each, the one unrecorded entered as an item; event (10)'s cite entered as a fact correction of FINDINGS :10847; the
               counter printed ((R329)(3)). Events (14)-(18), entered at b719's step zero after the ruling was written, printed apart and
               counted apart.
  differs      FINDINGS: one corrigendum entry naming each line data/b718_touch.txt marked DIFFERS, the ten on T-COUNT read under
               data/b718_count_read.txt :19, the eleventh printed with its own reading and carried ((R329)(4)).
  errata       ERRATA.md: one entry for SIDE-lv-conservation's RegisterPentagon.lean :149-:152 at its deposit 93c27ec, quoting
               data/b718_join_premise.txt :35 and stating what faces_join uses at SIDE-faces-join v0.1.0 ((R329)(5)); nothing in lv edited.
THE CHECKS BEFORE ANY WRITE: every figure's bank line found exactly once; the event rows (1)-(18); the defect rows 30, each bracketed; each
refusal's answering row carrying its needle; the touch bank's DIFFERS rows eleven, the ten T-COUNT rows as (R329)(4) numbers them; the
faces_join statement at the tag. Any miss: nothing composed.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b719_record as REC          # noqa: E402  ### the guarded landing (b698's), its screens, git
import b719_worklist as K          # noqa: E402
from b652_record import conv, append_to, guard_absent, line_of   # noqa: E402  ### the one conversion and the appends

R = REC.R
PP = 'D:/MY-DOwnloads/PLACE-papers'
ERRATA = os.path.join(PP, 'ERRATA.md')
FACES_JOIN = 'D:/SIDE-faces-join'
FACES_JOIN_TAG = 'v0.1.0'


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def fl(name, pat, what):
    """the one line of a bank matching pat: (groups, line number); any other count exits."""
    hits = [(i, m) for i, l in enumerate(rd(name).split(NL), 1) for m in [re.search(pat, l)] if m]
    if len(hits) != 1:
        sys.exit('### %s: %d LINES OF data/%s MATCH %r, NOT ONE -- NOTHING COMPOSED' % (what, len(hits), name, pat))
    return hits[0][1].groups(), hits[0][0]


def bank_json(name, obj):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


# ================================================================================ (R329)(2): b718 AT ITS WEIGHT
WEIGHT_HEAD = '*Appended 2026-10-28 by b719 to b718’s entry (:%d), under `(R329)`(2)' % K.B711_ENTRY


def weight_text():
    head = rd('b718_closing.txt').split(NL)[0]
    if not head.startswith('b718 closed: relay 098289c8, PLACE-papers b6cbbbd;'):
        sys.exit('### data/b718_closing.txt :1 IS NOT b718`S HEAD LINE -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b718_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing']
    if rec[-1:] != ['098289c8'] or clo != ['9818a7f0']:
        sys.exit('### data/b718_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    _x, l_dec = fl('b718_decomp.txt', r"THE NAVIGATOR`S FIGURES: 15 OF 15 AGREE, 0 DIFFER", 'the decomposition')
    _x, l_der = fl('b718_derivation.txt', r'THE GRADE: CLAUSE 2 A THEOREM \(WRITTEN PROOF\) ; CLAUSE 1 NOT DERIVED, ITS STEP NAMED', 'the grade')
    _x, l_a0 = fl('b718_a0.txt', r'A0 = 10 AT Q1 OF -39: CERTIFIED .* THE PREDICTIONS RE-READ 7, EQUAL TO THE COMMITTED 7', 'A0')
    _x, l_cnt = fl('b718_count_read.txt', r'^DOES NOT\. data/b705_contour\.txt does not discharge T-COUNT', 'the count read')
    _x, l_join = fl('b718_join_premise.txt', r'^DIFFERS, as the premise is worded\.', 'the join`s premise')
    _x, l_r20 = fl('b718_registrations.txt', r'^  D = -20: h = 2 ;', '-20')
    _x, l_r47 = fl('b718_registrations.txt', r'^  D = -47: h = 5 ;', '-47')
    (npin,), l_pin = fl('b718_pin.txt', r'^DISPATCHES (\d+) \(of twelve at most\) ; READ 1 ; BUILDS 1 ;', 'the pin')
    (nrow, nag, ndf), l_tch = fl('b718_touch.txt', r'ROWS (\d+) ; AGREES (\d+) ; DIFFERS (\d+)', 'the touch read')
    pre, l_pre = fl('b718_closing.txt', r'^\s*pre-push : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the pre-push suite')
    post, l_post = fl('b718_closing.txt', r'^\s*post-push : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', 'the post-push suite')
    (ca, cb), l_cl = fl('b718_closing.txt', r'^\s*pre-push, \(R328\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing NONE\)', 'the claim arms')
    (cc, cd), l_cn = fl('b718_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    (nbk,), l_bk = fl('b718_closing.txt', r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = fl('b718_closing.txt', r'^### THE MIRROR .*mirror-refresh-2026-10-27-b718\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b718 '
                       + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = fl('b718_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    ar = json.load(open(os.path.join(D, 'b718_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b718_act_root.json`s root %s IS NOT THE WORKLIST`S -- NOTHING COMPOSED' % ar.get('root'))
    ev = event_rows()
    dr = defect_rows()
    nav = [x for x, o, _t, _c in dr if o == "THE NAVIGATOR'S"]
    if sorted(ev) != list(range(1, 19)) or len(dr) != 30 or nav != ['i']:
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE NAVIGATOR`S %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), nav))
    return (WEIGHT_HEAD + ' -- b718 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b718_closing.txt):* “%s” (data/b718_closing.txt :1); its '
            'relay commit the record’s 098289c8, the closing’s 9818a7f0 (data/b718_steps.json, the record and closing rows), both made and '
            'pushed at b719’s step zero on the author’s word “push both as they stand” (`(R329)`(1)-(2)). As the banks confirm by row: the '
            'navigator’s reading reproduced, 15 of 15 figures agreeing (data/b718_decomp.txt :%d); the coefficient law’s clause 2 a theorem '
            '(written proof) and clause 1 not derived, its step named (data/b718_derivation.txt :%d); A0 = 10 certified at Q1 of -39, the seven '
            'predictions re-read equal to the committed (data/b718_a0.txt :%d); the count law not discharged by b705’s contour '
            '(data/b718_count_read.txt :%d); the join’s premise differing as worded (data/b718_join_premise.txt :%d); -20 and -47 registered, '
            'committed alone at 8146404b (data/b718_registrations.txt :%d, :%d); the federation pin at %s of 12 (data/b718_pin.txt :%d); the '
            'touch read %s rows, %s agreeing and %s differing (data/b718_touch.txt :%d); the suite %s of %s pre-push and %s of %s post-push, '
            'NOT CLEAN both, the claim arms %s of %s (data/b718_closing.txt :%d, :%d, :%d); the counter CLAIM %s, CLOSE %s (:%d); N1-N5 and '
            'S1-S3 HELD (:%d); the root %s over %s banks chained from %s (data/b718_act_root.json; :%d); the mirror (sha256 %s…) CLEAN on all '
            'three clauses with the root line, its manifest control NOT AS WANTED against a carried reference (:%d; event (18)); %d events in '
            'data/b718_events.txt, rows (1)-(%d); %d defects (a)–(z) and (a’)–(d’), (i) the navigator’s, the rest the seat’s '
            '(data/b718_defects.txt). Nothing deposited, nothing published.' % (
                head, l_dec, l_der, l_a0, l_cnt, l_join, l_r20, l_r47, npin, l_pin, nrow, nag, ndf, l_tch,
                pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, l_cn, l_sc, K.B714_ROOT[:8], nbk,
                ar['previous'][:8], l_bk, msha, l_mi, len(ev), max(ev), len(dr)))


# ================================================================================ (R329)(3): THE CORRIGENDUM FOR b718
def event_rows():
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '; its lines after at five."""
    out, cur = {}, None
    for l in rd('b718_events.txt').split(NL):
        m = re.match(r'^    \((\d+)\) (.*)$', l)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None and l.startswith('     '):
            out[cur] += ' ' + l.strip()
        else:
            cur = None
    return out


BRACKET = re.compile(r"^(THE SEAT'S|THE NAVIGATOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]: ")


def defect_rows():
    """(letter, owner, tag, column) for each row of data/b718_defects.txt opening four spaces, the primed letters read."""
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b718_defects.txt')):
        b = BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3)))
    return out


# ### the events' needles ((R329)(3) names (1)-(13)); (14)-(18) entered at b719's step zero, after the ruling
EVENTS = [(1, 'G-RULE-HEAD-LINE-QUOTED'), (2, 'G-CLOSING-DRY-STEP'), (3, 'runner dispatches this act 0'), (4, 'a PowerShell listing'),
          (5, "G-ANSWERS-BANKED's positive control"), (6, 'the suite refused the part at 1,852 MB free'), (7, 'defects_ok'),
          (8, 'read its first half as empty'), (9, 'the seal written with its relay head 979282c3'), (10, 'FINDINGS :10847'),
          (11, 'rootprompt'), (12, "the day papers"), (13, "three relay banks quote PLACE-papers f6f6df5's")]
EVENTS_LATE = [(14, 'data/act_current.json'), (15, 'G-DELETES-ONE-BRANCH'), (16, 'G-ANSWERS-BEFORE-WRITES'), (17, 'G-TRAIL-LINES-EQUAL-DEFECTS'),
               (18, 'its MANIFEST control NOT AS WANTED')]

# ### the refusals (data/b718_hook_refusals.txt, one a line) and the row recording each: (line, kind, the row, a needle in that row)
REFUSALS = [(1, 'READ', 'defect (n)', 'data/b718_citation_check.txt with no limit'), (2, 'PIPE', 'defect (q)', 'Measure-Object'),
            (3, 'PIPE', 'defect (s)', '21:31:53Z'), (4, 'READ', 'defect (u)', '22:02:11Z'), (5, 'PIPE', 'defect (w)', '22:17:12Z'),
            (6, 'READ', 'defect (x)', '22:21:31Z'), (7, 'PIPE', 'event (4)', 'data/b718_hook_refusals.txt :7'), (8, 'ENV', None, None)]
# ### the one refusal no row records: entered as an item, the seat's tag
ITEM_A = ('A', 'the hook’s refusal at 2026-10-28T00:56:54Z (the 8:57 PM refusal of `(R329)`(3)) of a PowerShell command prefixed by an '
          'environment-variable assignment, an unauthenticated ls-remote of the outside repository (data/b718_hook_refusals.txt :8; row (20)); '
          'nothing ran, the read re-made with git’s own options', 'CLOSE', 'REPEAT of b716 (e) (relay data/b716_defects.txt)')

CORR_TITLE = ('## Corrigendum to b718’s record (relay data/b718_events.txt rows (1)-(13), data/b718_defects.txt and '
              'data/b718_hook_refusals.txt): thirteen events, thirty defects and one refusal no row records, each CLAIM or CLOSE and NEW or '
              'REPEAT, and one fact correction, under (R329)(3)')
CORRIGENDA_LAST = 38


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1)


def corr_state():
    ev = event_rows()
    miss = [n for n, h in EVENTS + EVENTS_LATE if h not in ev.get(n, '')]
    tags = {}
    for n, _h in EVENTS + EVENTS_LATE:
        m = re.match(r"^THE SEAT'S \[(CLAIM|CLOSE) ; ([^\]]*)\]:", ev.get(n, ''))
        tags[n] = (m.group(1), m.group(2)) if m else (None, None)
    dr = defect_rows()
    rl = rd('b718_hook_refusals.txt').strip(NL).split(NL)
    dtext = dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b718_defects.txt')))
    bad_ref = []
    for ln, kind, row, needle in REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1]:
            bad_ref.append(ln)
        elif row and row.startswith('defect'):
            if needle not in dtext.get(row.split('(')[1].rstrip(')'), ''):
                bad_ref.append(ln)
        elif row and row.startswith('event'):
            if needle not in ev.get(int(row.split('(')[1].rstrip(')')), ''):
                bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', rd('b675_corrigenda.txt'))]
    bad = [k for k, v in (('the event rows (1)-(18)', sorted(ev) == list(range(1, 19))), ('each event`s needle', not miss),
                          ('each event`s bracket', all(t[0] for t in tags.values())), ('the defect rows 30', len(dr) == 30),
                          ('the refusals 8, each answered as listed', len(rl) == 8 and not bad_ref),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; needles missed %s ; refusals %s)' % (bad, sorted(ev), miss, bad_ref))
    return dict(events=ev, tags=tags, defects=dr)


def corr_counts(s, late=False):
    evs = EVENTS + (EVENTS_LATE if late else [])
    t = [s['tags'][n][0] for n, _h in evs] + [x[2] for x in s['defects']] + [ITEM_A[2]]
    rep = (sum(1 for n, _h in evs if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
           + (0 if ITEM_A[3] == 'NEW' else 1))
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def corr_lines(s, fact_line):
    nc, nl, rep, n = corr_counts(s)
    nc2, nl2, rep2, n2 = corr_counts(s, late=True)
    claims = [('(%d)' % k) for k, _h in EVENTS if s['tags'][k][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    L = ['*b718’s events bank (relay data/b718_events.txt) carries eighteen rows, entered after its lock and seal and not lettered, each '
         'tagged in its own bracket; `(R329)`(3) names rows (1)-(13), and rows (14)-(18) were entered at b719’s step zero, after the ruling, as '
         'b718’s close completed. Its defects bank carries thirty lettered rows, (a)-(z) and (a’)-(d’), each tagged in its own bracket; its '
         'refusal bank eight lines, seven recorded by a letter or an event and one by none. Each item is tagged CLAIM, where it touches a '
         'statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches '
         'the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry '
         'edits none of them.*', '', '**b718’s events (1)-(13):**', '']
    for k, h in EVENTS:
        t, r = s['tags'][k]
        L += ['**(%d) %s** (relay data/b718_events.txt, row (%d); %s; %s).' % (k, h, k, t, _col(r))]
    L += ['', '**b718’s defects:**', '']
    for x, o, t, c in s['defects']:
        L += ['**(%s)** (relay data/b718_defects.txt; %s; %s; %s).' % (x.replace("'", '’'), 'the navigator’s' if o == "THE NAVIGATOR'S" else 'the seat’s', t, _col(c))]
    L += ['', '**b718’s refusals** (relay data/b718_hook_refusals.txt, one a line): ' + '; '.join(
        ':%d %s, %s' % (ln, kind, ('recorded at %s' % row) if row else 'recorded by no row, item (A) below') for ln, kind, row, _n in REFUSALS) + '.',
          '', '**(%s) %s** (%s; %s).' % ITEM_A, '',
          '**A fact correction to FINDINGS :%d** (event (10), relay data/b718_touch.txt row (412)): the line heads “The CLOSE classes for the '
          'toolset’s v1.2.0 (b718’s, (R328)(6))”; the toolset’s clause is `(R328)`(7), “THE TOOLSET AT v1.2.0, per (R327)(11)” (relay '
          'data/b718_ferry.txt :29), and `(R328)`(6) is “TWO READS” (:25). Read the line’s cite as `(R328)`(7). FINDINGS is append-only: the '
          'line stands as written.' % fact_line, '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items of `(R329)`(3) (thirteen events, thirty defects, one refusal); REPEAT %d of '
          '%d; the CLAIM items %s. With rows (14)-(18) beside them: CLAIM %d, CLOSE %d over %d; REPEAT %d of %d.' % (
              nc, nl, n, rep, n, ', '.join(claims), nc2, nl2, n2, rep2, n2), '',
          '*Filed at b719 on the author’s ruling `(R329)`(3): generated by relay `tools/b719_c1.py` corrigendum, written whole at b719, from '
          'b718’s events, defects and refusal banks read unedited; banked as relay `data/b719_corrigendum.txt`, the corrigenda bank '
          '`data/b675_corrigenda.txt` appended at row (39). It answers b718’s record; no sealed tool, face, trail or root-named bank of b718 is '
          'edited.*']
    return L


# ================================================================================ (R329)(4): THE ELEVEN DIFFERS
DIFFERS_TITLE = ('## Corrigendum to the lines b718’s touch read marked DIFFERS (relay data/b718_touch.txt :448): ten on T-COUNT read under '
                 'data/b718_count_read.txt :19, and FINDINGS :10847, under (R329)(4)')
TCOUNT_ROWS = (298, 299, 300, 302, 303, 304, 305, 306, 308, 309)


def differs_state():
    rows = {}
    for m in re.finditer(r'(?m)^  \((\d+)\) FINDINGS\.md:(\d+)  (.+?) -- (AGREES|DIFFERS): (.*)$', rd('b718_touch.txt')):
        rows[int(m.group(1))] = (int(m.group(2)), m.group(3), m.group(4), m.group(5))
    dif = sorted(k for k, v in rows.items() if v[2] == 'DIFFERS')
    (nr, na, nd), lf = fl('b718_touch.txt', r'ROWS (\d+) ; AGREES (\d+) ; DIFFERS (\d+)', 'the touch foot')
    if dif != list(TCOUNT_ROWS) + [412] or int(nd) != 11:
        sys.exit('### THE TOUCH BANK`S DIFFERS ROWS %s (foot %s) -- NOT (R329)(4)`S -- NOTHING COMPOSED' % (dif, nd))
    q, lq = fl('b718_count_read.txt', r'^(DOES NOT\. data/b705_contour\.txt does not discharge T-COUNT: it establishes a premise of the discharge)', 'count_read :19')
    if lq != 19:
        sys.exit('### data/b718_count_read.txt`s line is :%d, NOT :19 -- NOTHING COMPOSED' % lq)
    return dict(rows=rows, quote=q[0], foot=lf)


def _quoted(reading):
    m = re.match(r'^"([^"]+)"', reading)
    return m.group(1) if m else None


def differs_lines(s, corr_line):
    L = ['*b718’s touch read (relay data/b718_touch.txt) looked up by needle each object b718’s entry names and marked each line found AGREES '
         'or DIFFERS: 413 rows, 402 agreeing and 11 differing (:%d). Under data/standing_clauses_v7.txt this entry names each line marked '
         'DIFFERS with the reading beside it; no line of the record is rewritten.*' % s['foot'], '',
         '**The ten on T-COUNT**, read under relay data/b718_count_read.txt :19: “%s”. b705’s contour does not discharge the count law, so each '
         'line that reads the Q0 figures as standing on a discharged count stands on T-COUNT as assumed. The clause the ten were marked '
         'against is b718’s entry’s “which the record derives at b687” (FINDINGS :%d). Each line is quoted as the touch bank quotes it.' % (
             s['quote'], K.B711_ENTRY + 2), '']
    for k in TCOUNT_ROWS:
        ln, _needle, _v, reading = s['rows'][k]
        q = _quoted(reading)
        if not q:
            sys.exit('### TOUCH ROW (%d) QUOTES NOTHING -- NOTHING COMPOSED' % k)
        L += ['- **FINDINGS :%d** (touch row (%d)): “%s” -- stands on T-COUNT as assumed (data/b718_count_read.txt :19).' % (ln, k, q)]
    ln, _needle, _v, reading = s['rows'][412]
    L += ['', '**The eleventh, FINDINGS :%d** (touch row (412)): its head cites `(R328)`(6) for the toolset’s classes, where the clause is '
          '`(R328)`(7) (relay data/b718_ferry.txt :25, :29) -- the reading entered as a fact correction in the corrigendum for b718 (FINDINGS '
          ':%s); printed here with that reading and carried for the author.' % (ln, corr_line), '',
          '*Filed at b719 on the author’s ruling `(R329)`(4): generated by relay `tools/b719_c1.py` differs from b718’s touch bank and count '
          'read, unedited; banked as relay `data/b719_differs.txt`. No ledger line is edited.*']
    return L


# ================================================================================ (R329)(5): THE ERRATA ENTRY
ERRATA_ID = 'E-2026-10-28-1'
ERRATA_TITLE = ('## %s — SIDE-lv-conservation’s deposited wording at RegisterPentagon.lean :149-:152 names “the actual Taylor coefficients of '
                '`log ξ`”, where the compiled join faces_join uses the stream LiCoeff (KERNEL-FACING; THE DEPOSIT IS NOT EDITED)' % ERRATA_ID)


def errata_state():
    jp = rd('b718_join_premise.txt').split(NL)
    if not jp[34].startswith('DIFFERS, as the premise is worded.') or ':149  Over the actual Taylor coefficients of `log ξ`' not in jp[8]:
        sys.exit('### data/b718_join_premise.txt :35 OR :9 NOT AS READ -- NOTHING COMPOSED')
    tip = subprocess.run(['git', '-C', FACES_JOIN, 'rev-parse', FACES_JOIN_TAG + '^{commit}'], capture_output=True, text=True).stdout.strip()
    src = subprocess.run(['git', '-C', FACES_JOIN, 'show', '%s:FacesJoin.lean' % FACES_JOIN_TAG], capture_output=True).stdout.decode('utf-8').replace(chr(13), '').split(NL)
    want = {29: 'theorem faces_join :', 30: '    SIDEExplicitFormula.B321.h2_sign ↔',
            31: '      SIDELvConservation.RegisterPentagon.Register4_positivity SIDEExplicitFormula.LiWeil.LiCoeff :=',
            32: '  SIDEExplicitFormula.B321.h2_sign_iff_rh.trans', 33: '    SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh.symm'}
    off = [k for k, v in want.items() if len(src) < k or src[k - 1] != v]
    if not tip.startswith('11a472b') or off:
        sys.exit('### SIDE-faces-join %s AT %s: LINES OFF %s -- NOTHING COMPOSED' % (FACES_JOIN_TAG, tip[:8], off))
    return dict(premise=jp[34], tip=tip)


def errata_lines(s):
    return ['**Filed 2026-10-28 by b719, on the author’s ruling `(R329)`(5); the read banked at relay `data/b718_join_premise.txt`. Records '
            'affected: SIDE-lv-conservation `SIDELvConservation/RegisterPentagon.lean` :148-:153 at the deposit `v0.10.0` = `93c27ec` (blob '
            '`6c8c9c32`), the docstring of `Register4_positivity`. Nothing in the kernel is edited at this act.**', '',
            '**What the line says.** *“Over the actual Taylor coefficients of `log ξ` this is RH-equivalent (Li 1997; Bombieri–Lagarias 1999) — '
            'that identification is the named manuscript premise on the `R4 ↔ RH` interface edge, not part of this face.”* (:149-:151; the '
            'definition at :152-:153 is `∀ n : ℕ, 1 ≤ n → 0 ≤ lam n` over an abstract stream `lam : ℕ → ℝ`).', '',
            '**What is true.** The read (relay `data/b718_join_premise.txt` :35): *“%s The premise names its object “the actual Taylor '
            'coefficients of `log ξ`” (:149, and :143).”* The object SIDE-explicit-formula v0.37 equates to `LiCoeff` is a different one on '
            'three counts (:37-:41): the logarithmic derivative of ξ(1/(1 − z)), expanded at z = 0, not `log ξ`; the index and factor, '
            '`LiCoeff (n + 1)` being the n-th coefficient of that log-derivative; and the real part. The compiled join `faces_join` at '
            'SIDE-faces-join `v0.1.0` = `%s` (`FacesJoin.lean` :29-:33) states `h2_sign ↔ RegisterPentagon.Register4_positivity LiWeil.LiCoeff` '
            'and proves it as `h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm`: it uses the definition’s body at the stream '
            '`lam := LiCoeff`, the sum over the zeros of Mathlib’s `riemannZeta` (`LiWeil.lean` :243-:244 at v0.37), and not the docstring’s '
            'premise; the premise holds at that stream and not at the object its sentence names (:42-:45).' % (s['premise'].split(' The premise')[0], s['tip'][:7]), '',
            '**The correction.** The docstring’s wording is corrected at SIDE-lv-conservation’s next version, as Phase 1.1 work, to name the '
            'object `faces_join` uses -- the stream `LiCoeff`, Li’s normalisation (relay `data/b718_join_premise.txt` :39-:45) -- in place of '
            '“the actual Taylor coefficients of `log ξ`”. The deposit `93c27ec` stands as deposited, and this entry is its record.', '',
            '**Scope.** One docstring’s wording; the definition, its statement and every theorem over it are unchanged, and `faces_join` is '
            'unaffected, since it reads the definition. No banked number, verdict or grade moves. Nothing here is a statement about RH or any '
            'zero.', '',
            '**Status.** FILED; the kernel’s edit carried to lv’s next version.']


# ================================================================================ THE ROUTES
def _bank(name, lines):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(lines) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def main(route, mode):
    dry = mode != 'write'
    if route == 'weight':
        text = weight_text()
        REC.land([('FINDINGS.md', WEIGHT_HEAD, NL + text + NL)], 'b719_record_lines.json', 'c1', entry=K.B711_ENTRY,
                 check=[('FINDINGS.md', K.B711_ENTRY, '## The coefficient law derived to the step named'),
                        ('OPEN_TRAILS.md', K.B711_TRAIL, '### b718 — lane two, act one hundred and forty-five, the derivation act')], dry=dry)
        return
    if route == 'corrigendum':
        s = corr_state()
        text = NL + CORR_TITLE + NL + NL + NL.join(corr_lines(s, K.B718_CLASSES)) + NL
        REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b719_corrigendum_landing.json', 'corrigendum', entry=None, dry=dry)
        if dry:
            print(NL.join(corr_lines(s, K.B718_CLASSES)[-4:-2]))
            return
        ln = line_of(R.FIND, CORR_TITLE)
        nc, nl, rep, n = corr_counts(s)
        nc2, nl2, rep2, n2 = corr_counts(s, late=True)
        _bank('b719_corrigendum.txt', ['b719 -- THE CORRIGENDUM FOR b718, (R329)(3) (%s)' % R.utc(), '',
                                       '### the banks read unedited: data/b718_events.txt rows (1)-(18), data/b718_defects.txt 30 rows, '
                                       'data/b718_hook_refusals.txt 8 lines; the corrigenda bank`s last row (%d).' % CORRIGENDA_LAST, '']
              + ['  ' + l for l in corr_lines(s, K.B718_CLASSES)]
              + ['', '### ### **ITEMS %d: EVENTS 13, DEFECTS 30, REFUSAL 1 ; CLAIM %d, CLOSE %d ; REPEAT %d ; WITH (14)-(18): CLAIM %d, CLOSE %d OVER '
                 '%d ; THE FACT CORRECTION OF FINDINGS :%d ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl, rep, nc2, nl2, n2, K.B718_CLASSES, ln)])
        bank_json('b719_corrigendum.json', dict(at=R.utc(), entry_line=ln, title=CORR_TITLE, claim=nc, close=nl, repeat=rep, items=n,
                                                with_late=dict(claim=nc2, close=nl2, repeat=rep2, items=n2), fact_correction=K.B718_CLASSES,
                                                events=[dict(row=k, tag=s['tags'][k][0], column=s['tags'][k][1]) for k, _h in EVENTS + EVENTS_LATE],
                                                defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c in s['defects']],
                                                item=dict(key=ITEM_A[0], tag=ITEM_A[2], column=ITEM_A[3]), row=39))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; with (14)-(18) CLAIM %d, CLOSE %d over %d ; FINDINGS :%s' % (nc, nl, n, rep, nc2, nl2, n2, ln))
        return
    if route == 'differs':
        corr_ln = line_of(R.FIND, CORR_TITLE)
        if not corr_ln:
            sys.exit('### THE CORRIGENDUM FOR b718 NOT LANDED -- THE DIFFERS ENTRY CITES IT -- NOTHING COMPOSED')
        s = differs_state()
        text = NL + DIFFERS_TITLE + NL + NL + NL.join(differs_lines(s, corr_ln)) + NL
        REC.land([('FINDINGS.md', DIFFERS_TITLE, text)], 'b719_differs_landing.json', 'differs', entry=None, dry=dry)
        if not dry:
            ln = line_of(R.FIND, DIFFERS_TITLE)
            _bank('b719_differs.txt', ['b719 -- THE ELEVEN DIFFERS OF data/b718_touch.txt, (R329)(4) (%s)' % R.utc(), '']
                  + ['  ' + l for l in differs_lines(s, corr_ln)]
                  + ['', '### ### **DIFFERS 11: T-COUNT 10 READ UNDER data/b718_count_read.txt :19, THE ELEVENTH (412) CARRIED ; NO LEDGER LINE EDITED ; '
                     'THE ENTRY AT FINDINGS :%s.**' % ln])
            print('  FINDINGS :%s' % ln)
        return
    if route == 'errata':
        s = errata_state()
        body = NL.join(errata_lines(s))
        text = NL + NL + ERRATA_TITLE + NL + NL + body + NL
        cells, fired = R.screens([('ERRATA.md', ERRATA_TITLE, conv(text))], 'errata', dry)
        if dry:
            print(conv(text))
            return
        if cells or fired:
            sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
        guard_absent(ERRATA, ERRATA_TITLE)
        append_to(ERRATA, text)
        ln = line_of(ERRATA, ERRATA_TITLE)
        _bank('b719_errata.txt', ['b719 -- THE ERRATA ENTRY FOR THE JOIN`S PREMISE, (R329)(5) (%s)' % R.utc(), '', '  ' + ERRATA_TITLE, '']
              + ['  ' + l for l in errata_lines(s)]
              + ['', '### ### **%s FILED AT ERRATA.md :%s ; SIDE-faces-join %s = %s READ ; NOTHING IN SIDE-lv-conservation EDITED.**' % (
                  ERRATA_ID, ln, FACES_JOIN_TAG, s['tip'][:8])])
        print('  ERRATA.md :%s' % ln)
        return
    sys.exit('usage: b719_c1.py weight | corrigendum | differs | errata  [dry | write]')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '', sys.argv[2] if len(sys.argv) > 2 else 'dry')
