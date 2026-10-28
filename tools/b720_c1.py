# -*- coding: utf-8 -*-
"""b720_c1.py -- COMPONENT 1 OF b720, (R330)(1)-(2): b719 AT ITS WEIGHT AND THE CORRIGENDUM FOR b719.
Written whole at b720 by the Write tool (no carry: b719's corrigendum tool composed b718's eighteen events and thirty defects).

Routes, each `dry` (prints the text and the screens, writes nothing) or `write` (lands through b698's guarded landing, banks the line):
  weight       FINDINGS: b719's weight line after its entry (:10982), every figure read from b719's banks by line ((R330)(1)).
  corrigendum  FINDINGS: the corrigendum for b719 from data/b719_events.txt (1)-(10) and data/b719_defects.txt (a)-(r), each item CLAIM or
               CLOSE and NEW or REPEAT read from its own bracket; the refusals answered by the letter or event that records each; the three
               items (R330)(2) reads by line first -- (i) dbea2e3f's late step row, (ii) event (9)'s MANIFEST control read from its source
               with the diff of (R328)(7)'s repair beside it, (iii) the seat's memory file overwritten without a read -- and the counter.
THE CHECKS BEFORE ANY WRITE: every figure's bank line found exactly once; the event rows (1)-(10), each bracketed; the defect rows 18, each
bracketed; each refusal's answering row carrying its needle; the late row in data/b719_steps.json at 6755e0c9; the record tool's mirror
control and the standing manifest control at the lines (ii) cites. Any miss: nothing composed.
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

import b720_record as REC          # noqa: E402  ### the guarded landing (b698's), its screens, git
import b720_worklist as K          # noqa: E402
from b652_record import line_of    # noqa: E402

R = REC.R


def rd(name, base=D):
    with open(os.path.join(base, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def fl(name, pat, what, base=D):
    """the one line of a file matching pat: (groups, line number); any other count exits."""
    hits = [(i, m) for i, l in enumerate(rd(name, base).split(NL), 1) for m in [re.search(pat, l)] if m]
    if len(hits) != 1:
        sys.exit('### %s: %d LINES OF %s MATCH %r, NOT ONE -- NOTHING COMPOSED' % (what, len(hits), name, pat))
    return hits[0][1].groups(), hits[0][0]


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


def bank_json(name, obj):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def _bank(name, lines):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(lines) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


# ================================================================================ (R330)(1): b719 AT ITS WEIGHT
WEIGHT_HEAD = '*Appended 2026-10-28 by b720 to b719’s entry (:%d), under `(R330)`(1)' % K.B711_ENTRY
HEAD_QUOTED = ('b719 closed: relay fa268307, PLACE-papers b92bb70; suite 111 of 116; root 09e524a73dde38bf…; 1 prompt answered; scores 7 of 8 '
               'HELD; 18 defects')


def weight_text():
    head = rd('b719_closing.txt').split(NL)[0]
    if head != HEAD_QUOTED:
        sys.exit('### data/b719_closing.txt :1 IS NOT THE HEAD LINE (R330)(1) QUOTES -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b719_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing']
    if rec[-1:] != ['fa268307'] or clo != ['ef648cb9']:
        sys.exit('### data/b719_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    _x, l_co = fl('b719_coeffs.txt', r'n0\(-20\) = 36, b = -2 ; n0\(-47\) = 168, b = -2 ; ROWS 12: HELD 9, REFUTED 3, NOT SCORABLE 0 ; H-24 REFUTED ; H-47 REFUTED', 'the coefficients')
    _x, l_pr = fl('b719_prediction.txt', r'THE CONTROLS AS WANTED ; PREDICTED n0\(-20\) = 36, b = -2 ; PREDICTED n0\(-47\) = 168, b = -2', 'the prediction')
    _x, l_de = fl('b719_derivation.txt', r'THE GRADE: THE CHARACTER FORMS OF a, THE PAIR SUM AND b A WRITTEN PROOF, CHECKED ; CLAUSE 1 NOT DERIVED, ITS STEP NAMED AND NARROWED', 'the grade')
    _x, l_of = fl('b719_offset_read.txt', r'READ POST HOC: -39`S SEVEN OFFSETS POSITIVE, \+54\.9 TO \+161\.7', 'the offset read')
    _x, l_su = fl('b719_surgery.txt', r'THE SURGERY CARRIED ; H-SHAPE REGISTERED AT 965cb8e8 BEFORE ANY NUMBER', 'the surgery')
    _x, l_ar = fl('b719_arm_retire.txt', r'RETIRED 25 CLOSE ARMS ; THE RUN LIST 141 -> 116 ; CLAIM ARMS 38 -> 38 \(UNTOUCHED\) ; NO GUARD RETIRED', 'the arms retired')
    _x, l_cr = fl('b719_count_route_price.txt', r'THE ROUTE PRICED: 19,852 UNIT BANDS AT Q0', 'the count route')
    (cn, cl, cr), l_cg = fl('b719_corrigendum.txt', r'ITEMS (\d+): EVENTS 13, DEFECTS 30, REFUSAL 1 ; CLAIM (\d+), CLOSE (\d+) ;', 'the corrigendum')
    _x, l_df = fl('b719_differs.txt', r'DIFFERS 11: T-COUNT 10 READ UNDER', 'the differs')
    _x, l_er = fl('b719_errata.txt', r'E-2026-10-28-1 FILED AT ERRATA\.md :990', 'the errata')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = fl('b719_closing.txt', suite % 'pre-push', 'the pre-push suite')
    post, l_post = fl('b719_closing.txt', suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = fl('b719_closing.txt', r'^\s*pre-push, \(R329\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing NONE\)', 'the claim arms')
    (cc, cd), l_cn = fl('b719_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    (nbk,), l_bk = fl('b719_closing.txt', r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = fl('b719_closing.txt', r'^### THE MIRROR .*mirror-refresh-2026-10-28-b719\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b719 '
                       + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = fl('b719_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) REFUTED \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    ar = json.load(open(os.path.join(D, 'b719_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b719_act_root.json`s root %s IS NOT THE WORKLIST`S -- NOTHING COMPOSED' % ar.get('root'))
    ev = event_rows()
    dr = defect_rows()
    if sorted(ev) != list(range(1, 11)) or len(dr) != 18 or any(o != "THE SEAT'S" for _x, o, _t, _c in dr):
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (WEIGHT_HEAD + ' -- b719 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b719_closing.txt):* “%s” (data/b719_closing.txt :1); its '
            'relay commit the record’s fa268307, the closing’s ef648cb9 (data/b719_steps.json, the record and closing rows). As the banks '
            'confirm by row: the corrigendum for b718 at %s items, CLAIM %s, CLOSE %s (data/b719_corrigendum.txt :%d), the eleven DIFFERS '
            'entered (data/b719_differs.txt :%d), the join’s premise in ERRATA as E-2026-10-28-1 (data/b719_errata.txt :%d); the rule’s '
            'prediction committed before any coefficient, n0(-20) = 36 and n0(-47) = 168 (data/b719_prediction.txt :%d); the least negative '
            'index 36 and 168, b = -2 at each, rows 12, HELD 9, REFUTED 3, H-24 and H-47 REFUTED (data/b719_coeffs.txt :%d); the character '
            'forms of a, the pair sum and b a written proof, checked, clause 1 not derived, its step named and narrowed '
            '(data/b719_derivation.txt :%d); -39’s seven onset offsets read post hoc, +54.9 to +161.7, H-OFFSET registered for the next tier '
            '(data/b719_offset_read.txt :%d); the surgery carried, H-SHAPE registered at 965cb8e8 before any number (data/b719_surgery.txt '
            ':%d); 25 CLOSE arms retired, the run list 141 to 116, the claim arms 38 untouched (data/b719_arm_retire.txt :%d); the count '
            'law’s route priced at 19,852 unit bands, nothing built (data/b719_count_route_price.txt :%d); the suite %s of %s pre-push and %s '
            'of %s post-push, NOT CLEAN both, the claim arms %s of %s (data/b719_closing.txt :%d, :%d, :%d); the counter CLAIM %s, CLOSE %s '
            '(:%d); N4 REFUTED on its push clause (event (7)), N1-N3, N5 and S1-S3 HELD (:%d); the root %s over %s banks chained from %s '
            '(data/b719_act_root.json; :%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root line, its manifest control NOT '
            'AS WANTED against a carried reference (:%d; event (9)); %d events in data/b719_events.txt, rows (1)-(%d); %d defects (a)–(r), '
            'all the seat’s (data/b719_defects.txt). Nothing deposited, nothing published.' % (
                head, cn, cl, cr, l_cg, l_df, l_er, l_pr, l_co, l_de, l_of, l_su, l_ar, l_cr,
                pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, l_cn, l_sc, K.B714_ROOT[:8], nbk,
                ar['previous'][:8], l_bk, msha, l_mi, len(ev), max(ev), len(dr)))


# ================================================================================ (R330)(2): THE CORRIGENDUM FOR b719
def event_rows():
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '; its lines after at five."""
    out, cur = {}, None
    for l in rd('b719_events.txt').split(NL):
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
    """(letter, owner, tag, column) for each row of data/b719_defects.txt opening four spaces."""
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b719_defects.txt')):
        b = BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3)))
    return out


# ### the events' needles ((R330)(2) names (1)-(10))
EVENTS = [(1, '_PrevWorklist'), (2, 'G-RECEIPT-IN-FULL'), (3, 'G-PUSHOUT-COMMITTED'), (4, 'the twenty-two failures'),
          (5, 'PASS 78, FAILED AS b718'), (6, 'data/b718_standing_control.json'), (7, 'N4 reads REFUTED on its push'),
          (8, 'G-SEALED-AFTER-COMPONENTS'), (9, 'THE MANIFEST CONTROL reads NOT AS'), (10, 'ForEach-Object')]

# ### the refusals (data/b719_hook_refusals.txt, one a line) and the row recording each: (line, kind, the row, a needle in that row)
REFUSALS = [(1, 'PIPE', 'defect (b)', 'hook_refusals.txt :1'), (2, 'PIPE', 'defect (c)', 'hook_refusals.txt :2'),
            (3, 'READ', 'defect (i)', 'hook_refusals.txt :3'), (4, 'REDIR', 'defect (j)', 'hook_refusals.txt :4'),
            (5, 'READ', 'defect (k)', 'hook_refusals.txt :5'), (6, 'READ', 'defect (l)', 'hook_refusals.txt :6'),
            (7, 'READ', 'event (6)', 'hook_refusals.txt :7'), (8, 'PIPE', 'event (10)', 'hook_refusals.txt :8')]

# ### (R330)(2)(i)-(iii), each read by line first
LATE_COMMIT = '6755e0c9'
MBANK_SPAN = (3370, 3381)        # ### tools/b719_record.py mbank: the inline control against K.RECUT_MERGE
MF_SPAN = (34, 53)               # ### tools/standing/manifest.py control: the repair of (R328)(7)
COVERAGE_LINE = 32               # ### data/b718_toolset_coverage.txt: step [23]'s row, "(10) reaches mbank"
REPAIR_COMMIT = 'a240e6b6'       # ### b718 C4: the toolset at v1.2.0, manifest.py new
MEM_OVERWRITE = ('2026-10-28T06:28:01Z', 16474)
MEM_RESTORE = ('2026-10-28T06:49:30Z', 16555)
ITEM_B = ('B', 'the seat’s memory file feedback_b719_traps.md (the seat’s persistent memory, outside both repositories) replaced whole by the '
          'Write tool at %s, at b719’s close (this session’s transcript line %d), without a read of what it held -- b719’s step-zero traps, '
          'written at 02:28:53Z, lost from it; restored at b720 from the transcript (line 10159) into feedback_b719_stepzero_traps.md at %s '
          '(line %d), the memory index re-pointed. From this act the seat reads a memory file before it replaces one' % (
              MEM_OVERWRITE[0], MEM_OVERWRITE[1], MEM_RESTORE[0], MEM_RESTORE[1]), 'CLOSE', 'NEW')

CORR_TITLE = ('## Corrigendum to b719’s record (relay data/b719_events.txt rows (1)-(10) and data/b719_defects.txt): ten events, eighteen '
              'defects and one item of the seat’s memory, each CLAIM or CLOSE and NEW or REPEAT, and three items read by line, under (R330)(2)')
CORRIGENDA_LAST = 39


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1)


def item_reads():
    """(R330)(2)(i)-(ii), read by line: the late row; the mirror control's source and the repair's, with the repair commit's file list."""
    st = json.load(open(os.path.join(D, 'b719_steps.json'), encoding='utf-8')).get('rows') or []
    late = [r for r in st if (r.get('commit') or '').startswith('dbea2e3f')]
    lc = git('log', '-1', '--format=%h', '--', 'data/b719_steps.json').strip()
    shown = git('show', '--format=', '-U0', LATE_COMMIT, '--', 'data/b719_steps.json')
    mb = rd('b719_record.py', T).split(NL)[MBANK_SPAN[0] - 1:MBANK_SPAN[1]]
    mf = rd(os.path.join('standing', 'manifest.py'), T).split(NL)[MF_SPAN[0] - 1:MF_SPAN[1]]
    cov = rd('b718_toolset_coverage.txt').split(NL)[COVERAGE_LINE - 1]
    files = [l for l in git('show', '--format=', '--name-only', REPAIR_COMMIT).split(NL) if l.strip()]
    callers = [l for l in git('grep', '-n', '-e', 'MF.control', '--', 'tools').split(NL) if l.strip()]
    rec_calls = [l for l in callers if '_record.py' in l]
    bad = [k for k, v in (('the late row, one, labelled LATE', len(late) == 1 and 'LATE' in (late[0].get('late') or '')),
                          ('the late commit touching the step bank', '"late"' in shown),
                          ('mbank`s control against K.RECUT_MERGE', any('K.RECUT_MERGE' in l for l in mb)),
                          ('manifest.py`s control reading ref or head', any('ref = ref or head' in l for l in mf)),
                          ('the coverage row naming mbank', 'reaches mbank' in cov),
                          ('the repair commit adding manifest.py', 'tools/standing/manifest.py' in files),
                          ('the repair commit editing no record tool', not any(f.endswith('_record.py') for f in files)),
                          ('no record tool calling MF.control', not rec_calls)) if not v]
    if bad:
        sys.exit('### THE ITEMS NOT AS READ: %s -- NOTHING COMPOSED' % bad)
    return dict(late=late[0], last_steps_commit=lc, mbank=mb, mf=mf, cov=cov, files=files, callers=callers)


def corr_state():
    ev = event_rows()
    miss = [n for n, h in EVENTS if h not in ev.get(n, '')]
    tags = {}
    for n, _h in EVENTS:
        m = re.match(r"^THE SEAT'S \[(CLAIM|CLOSE) ; ([^\]]*)\]:", ev.get(n, ''))
        tags[n] = (m.group(1), m.group(2)) if m else (None, None)
    dr = defect_rows()
    rl = rd('b719_hook_refusals.txt').strip(NL).split(NL)
    dtext = dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b719_defects.txt')))
    bad_ref = []
    for ln, kind, row, needle in REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1]:
            bad_ref.append(ln)
        elif row.startswith('defect'):
            if needle not in dtext.get(row.split('(')[1].rstrip(')'), ''):
                bad_ref.append(ln)
        elif needle not in ev.get(int(row.split('(')[1].rstrip(')')), ''):
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', rd('b675_corrigenda.txt'))]
    bad = [k for k, v in (('the event rows (1)-(10)', sorted(ev) == list(range(1, 11))), ('each event`s needle', not miss),
                          ('each event`s bracket', all(t[0] for t in tags.values())), ('the defect rows 18', len(dr) == 18),
                          ('the refusals 8, each answered as listed', len(rl) == 8 and not bad_ref),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; needles missed %s ; refusals %s)' % (bad, sorted(ev), miss, bad_ref))
    return dict(events=ev, tags=tags, defects=dr, items=item_reads())


def corr_counts(s):
    t = [s['tags'][n][0] for n, _h in EVENTS] + [x[2] for x in s['defects']] + [ITEM_B[2]]
    rep = (sum(1 for n, _h in EVENTS if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
           + (0 if ITEM_B[3] == 'NEW' else 1))
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def corr_lines(s):
    nc, nl, rep, n = corr_counts(s)
    it = s['items']
    claims = [('(%d)' % k) for k, _h in EVENTS if s['tags'][k][0] == 'CLAIM'] + [('(%s)' % x[0]) for x in s['defects'] if x[2] == 'CLAIM']
    L = ['*b719’s events bank (relay data/b719_events.txt) carries ten rows, entered after its lock and seal and not lettered, each tagged in '
         'its own bracket; its defects bank eighteen lettered rows, (a)-(r), each tagged in its own bracket; its refusal bank eight lines, each '
         'recorded by a letter or an event. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed '
         'figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches the close’s own record of itself; and NEW or REPEAT '
         'with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*', '',
         '**Three items read by line first (`(R330)`(2)):**', '',
         '**(i) dbea2e3f given its late step row** (event (8), defect (f)): the row stands in relay data/b719_steps.json at index 0 by commit '
         'time, phase “step zero”, labelled LATE, written by hand at b720’s step zero and committed alone at %s; b719’s hash bank '
         '(data/b719_bank_hashes.json) left as it stood, so the hand write reads as one. G-SEALED-AFTER-COMPONENTS now finds a row for every '
         'commit of b719; b719’s suite banks stand as written.' % LATE_COMMIT, '',
         '**(ii) event (9), the MANIFEST control’s reference, read from its source.** The control b719’s mirror bank printed is not the '
         'standing control: relay tools/b719_record.py mbank :%d-:%d compares each entry against `git show K.RECUT_MERGE:<path>`, the '
         'worklist’s RECUT_MERGE a86c9429, carried from act to act. (R328)(7)’s repair, b718’s commit %s, added tools/standing/manifest.py, whose '
         '`control` (:%d-:%d) reads each file the act edited against the head the mirror was built at (`ref = ref or head`), and whose only '
         'caller is the class controls in tools/standing/classes.py (%s); the commit’s files (%d) name no record tool, and its coverage table '
         'states the repair reached mbank (relay data/b718_toolset_coverage.txt :%d: “(10) reaches mbank: its MANIFEST control by manifest.py '
         'control … -- not moved”). So the repair was made and controlled in the toolset and never wired into the route that writes the '
         'mirror bank; b718’s and b719’s record tools, each carried from the last, kept the inline loop and its carried reference. A repair '
         'that did not take: REPEAT, as the events bank tags the row (b718 (10)), the class’s earlier rows b717’s event (10) and b718’s '
         'event (18).' % (
             MBANK_SPAN[0], MBANK_SPAN[1], REPAIR_COMMIT, MF_SPAN[0], MF_SPAN[1],
             it['callers'][0].split(':')[0] + ' ' + ', '.join(':' + c.split(':')[1] for c in it['callers']), len(it['files']), COVERAGE_LINE), '',
         '**(iii) (B) %s** (%s; %s).' % ITEM_B[1:], '',
         '**b719’s events (1)-(10):**', '']
    for k, h in EVENTS:
        t, r = s['tags'][k]
        L += ['**(%d) %s** (relay data/b719_events.txt, row (%d); %s; %s).' % (k, h, k, t, _col(r) + ('; the repair of (R328)(7) not wired, item (ii)' if k == 9 else ''))]
    L += ['', '**b719’s defects:**', '']
    for x, o, t, c in s['defects']:
        L += ['**(%s)** (relay data/b719_defects.txt; the seat’s; %s; %s).' % (x, t, _col(c))]
    L += ['', '**b719’s refusals** (relay data/b719_hook_refusals.txt, one a line): ' + '; '.join(
        ':%d %s, recorded at %s' % (ln, kind, row) for ln, kind, row, _n in REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items of `(R330)`(2) (ten events, eighteen defects, one item of the seat’s memory); '
          'REPEAT %d of %d; the CLAIM items %s.' % (nc, nl, n, rep, n, ', '.join(claims)), '',
          '*Filed at b720 on the author’s ruling `(R330)`(2): generated by relay `tools/b720_c1.py` corrigendum, written whole at b720, from '
          'b719’s events, defects and refusal banks read unedited; banked as relay `data/b720_corrigendum.txt`, the corrigenda bank '
          '`data/b675_corrigenda.txt` appended at row (40). It answers b719’s record; no sealed tool, face, trail or root-named bank of b719 is '
          'edited.*']
    return L


def corr_bank_rows(s, ln):
    it = s['items']
    nc, nl, rep, n = corr_counts(s)
    return (['b720 -- THE CORRIGENDUM FOR b719, (R330)(2) (%s)' % R.utc(), '',
             '### the banks read unedited: data/b719_events.txt rows (1)-(10), data/b719_defects.txt 18 rows, data/b719_hook_refusals.txt 8 '
             'lines; the corrigenda bank`s last row (%d).' % CORRIGENDA_LAST, '',
             '## (R330)(2)(ii) READ BY LINE: THE CONTROL b719`S MIRROR BANK RAN (relay tools/b719_record.py :%d-:%d)' % MBANK_SPAN]
            + ['    %d| %s' % (MBANK_SPAN[0] + i, l) for i, l in enumerate(it['mbank'])]
            + ['## BESIDE IT, (R328)(7)`S REPAIR (relay %s, tools/standing/manifest.py new; its control :%d-:%d)' % ((REPAIR_COMMIT,) + MF_SPAN)]
            + ['    %d| %s' % (MF_SPAN[0] + i, l) for i, l in enumerate(it['mf'])]
            + ['## THE REPAIR COMMIT`S FILES (%d): %s' % (len(it['files']), ', '.join(it['files'])),
               '## THE CALLERS OF MF.control IN tools/: %s ; IN A RECORD TOOL: NONE' % ' ; '.join(it['callers']),
               '## THE COVERAGE ROW (data/b718_toolset_coverage.txt :%d): %s' % (COVERAGE_LINE, it['cov'].strip()),
               '## THE REASON: the repair was added and controlled in tools/standing/ and never wired into mbank, which kept its inline loop '
               'against K.RECUT_MERGE (a86c9429) through b718`s and b719`s carries -- REPEAT.',
               '## (R330)(2)(i) THE LATE ROW: %s' % json.dumps(it['late'], ensure_ascii=False), '']
            + ['  ' + l for l in corr_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 10, DEFECTS 18, MEMORY 1 ; CLAIM %d, CLOSE %d ; REPEAT %d ; (i) THE LATE ROW AT %s ; (ii) THE REPAIR NOT '
               'WIRED, REPEAT ; (iii) CLOSE ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl, rep, LATE_COMMIT, ln)])


# ================================================================================ THE ROUTES
def main(route, mode):
    dry = mode != 'write'
    if route == 'weight':
        text = weight_text()
        REC.land([('FINDINGS.md', WEIGHT_HEAD, NL + text + NL)], 'b720_record_lines.json', 'c1', entry=K.B711_ENTRY,
                 check=[('FINDINGS.md', K.B711_ENTRY, '## The coefficient law at -20 and -47'),
                        ('OPEN_TRAILS.md', K.B711_TRAIL, '### b719 — lane two, act one hundred and forty-six, the coefficient act')], dry=dry)
        return
    if route == 'corrigendum':
        s = corr_state()
        text = NL + CORR_TITLE + NL + NL + NL.join(corr_lines(s)) + NL
        if dry:
            REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b720_corrigendum_landing.json', 'corrigendum', entry=None, dry=True)
            print(NL.join(corr_bank_rows(s, None)[:40]))
            return
        REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b720_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = line_of(R.FIND, CORR_TITLE)
        nc, nl, rep, n = corr_counts(s)
        _bank('b720_corrigendum.txt', corr_bank_rows(s, ln))
        bank_json('b720_corrigendum.json', dict(at=R.utc(), entry_line=ln, title=CORR_TITLE, claim=nc, close=nl, repeat=rep, items=n,
                                                events=[dict(row=k, tag=s['tags'][k][0], column=s['tags'][k][1]) for k, _h in EVENTS],
                                                defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c in s['defects']],
                                                item=dict(key=ITEM_B[0], tag=ITEM_B[2], column=ITEM_B[3]), late=LATE_COMMIT,
                                                repair=dict(commit=REPAIR_COMMIT, wired=False), row=CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; FINDINGS :%s' % (nc, nl, n, rep, ln))
        return
    sys.exit('usage: b720_c1.py weight | corrigendum  [dry | write]')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '', sys.argv[2] if len(sys.argv) > 2 else 'dry')
