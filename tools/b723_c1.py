# -*- coding: utf-8 -*-
"""b723_c1.py -- COMPONENT 1 OF b723, (R333)(1)-(2): b722 AT ITS WEIGHT AND THE CORRIGENDUM FOR b722, WITH THE THREE REPAIRS.
Written whole at b723 by the Write tool, in b722_c1.py's form (b722's tool composed b720's fifteen events and twenty-nine defects).

Routes, each `dry` (prints the text and the screens, writes nothing) or `write` (lands through b698's guarded landing, banks the line):
  weight       FINDINGS: b722's weight line after its entry (:11178), every figure read from b722's banks by line, and (R333)(1)'s rule
               (relay data/b723_rules.txt (1)).
  corrigendum  FINDINGS: the corrigendum for b722 from data/b722_events.txt (1)-(15) and data/b722_defects.txt (a)-(z), (a'), each item
               CLAIM or CLOSE and NEW or REPEAT read from its own bracket; the refusals (the bank's ten lines at b722's closing commit and
               b722's line in data/b720_hook_refusals.txt) answered by the letter or event that records each; the three repairs of
               (R333)(2) at tools/standing/ v1.2.2, each with its control on b722's banks (relay data/b723_standing_v122.txt) -- (i) the
               seal's list read from the seal bank, (ii) USED by discriminant and principal form, (iii) the closure reader retired -- and
               the counter.
THE CHECKS BEFORE ANY WRITE: every figure's bank line found exactly once; the event rows (1)-(15), each bracketed; the defect rows 27, each
bracketed; each refusal's answering row carrying its needle; the v1.2.2 controls bank AS WANTED in every case. Any miss: nothing composed.
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

import b723_record as REC          # noqa: E402  ### the guarded landing (b698's), its screens, git
import b723_worklist as K          # noqa: E402
from b652_record import line_of    # noqa: E402

R = REC.R
PREV_CLOSE = '30c0b3c8'            # ### b722's closing commit: the refusal bank read at it (its eleventh and twelfth lines are b723's own, uncommitted)
PREV_RECORD = '74dc741f'


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


# ================================================================================ (R333)(1): b722 AT ITS WEIGHT
WEIGHT_HEAD = '*Appended 2026-10-28 by b723 to b722’s entry (:%d), under `(R333)`(1)' % K.B711_ENTRY
HEAD_QUOTED = ('b722 closed: relay 74dc741f, PLACE-papers 2b19414; suite 112 of 116; root c6e2079dbe1c904f…; 1 prompt answered; scores 6 of 8 '
               'HELD; 27 defects')
RULE_QUOTED = ('From this act: after the lock gate no bank, face or tool is edited, and a restore is an edit; a correction found after the '
               'lock stands as an event.')


def weight_text():
    head = rd('b722_closing.txt').split(NL)[0]
    if head != HEAD_QUOTED:
        sys.exit('### data/b722_closing.txt :1 IS NOT THE HEAD LINE (R333)(1) QUOTES -- NOTHING COMPOSED')
    if RULE_QUOTED not in ' '.join(rd('b723_ferry.txt').split()):
        sys.exit('### (R333)(1)`S RULE NOT FOUND IN THE FERRY AS QUOTED -- NOTHING COMPOSED')
    _x, l_rule = fl('b723_rules.txt', r'^  \(1\) NOTHING EDITED AFTER THE LOCK GATE; A RESTORE IS AN EDIT\.', 'the rules bank`s row (1)')
    steps = json.load(open(os.path.join(D, 'b722_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing']
    if rec[-1:] != [PREV_RECORD] or clo != [PREV_CLOSE]:
        sys.exit('### data/b722_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    _x, l_out = fl('b722_registrations.txt', r'^THE OUTPUT: NONE\. Every one of the eighteen walked fields has a table value of -2 or -1/2', 'the rule`s output')
    _x, l_pc = fl('b722_registrations.txt', r'^THE POSITIVE CONTROL: the same walk with only -2 excluded takes -24 \(n0 36\) and -88 \(n0 484\)', 'the positive control')
    _x, l_wk = fl('b722_registrations.txt', r'^  H-C2-WALK \(the table`s\)|^  H-C2-WALK \(the table\'s\)', 'H-C2-WALK')
    _x, l_31 = fl('b722_registrations.txt', r'^  H-C3-31 \(D = -31;', 'H-C3-31')
    _x, l_55 = fl('b722_registrations.txt', r'^  H-C4-55 \(D = -55;', 'H-C4-55')
    _x, l_de = fl('b722_derivation.txt', r'CHECKS \(1\) \(2\) \(4\): ALL AS WANTED ; PLANTS: ALL FAIL AS WANTED ; THE GRADE', 'the table`s grade')
    _x, l_or = fl('b722_offset_read.txt', r'POST HOC 17: HELD 3, REFUTED 14, NOT SCORABLE 0 ; H-OFFSET REFUTED \(POST HOC\)', 'the offset read')
    _x, l_ot = fl('b722_offset_tier.txt', r'THE RULE`S OUTPUT: 53 CHOSEN BY r\(rho\) <= 0\.05 ; delta_pred FORMED AT 0', 'the offset tier')
    _x, l_su = fl('b722_surgery_carry.txt', r'THE SURGERY CARRIED, NOT STARTED', 'the surgery')
    _x, l_fz = fl('b722_frozen_line.txt', r'SIDE-archimedean EXCEEDS 7, STATED 2 ; SIDE-frobenius EXCEEDS 0, STATED 8 ; SIDE-spinor EXCEEDS 7, STATED 3 ; '
                  r'SIDE-rcurve EXCEEDS 9, STATED 1', 'the frozen line')
    _x, l_rb = fl('b722_rebuild.txt', r'6 OF 6 WAVE 1 KERNELS BUILD AT THEIR OWN PINS \(ONE WITH A SORRY: SIDE-lv-conservation\)', 'the rebuild')
    _x, l_ax = fl('b722_rebuild.txt', r"T3_perClass_to_combinations' depends on axioms: \[propext, sorryAx", 'the sorry`s print')
    (cn, cl, cr), l_cg = fl('b722_corrigendum.txt', r'ITEMS (\d+): EVENTS 15, DEFECTS 29 ; CLAIM (\d+), CLOSE (\d+) ;', 'the corrigendum')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = fl('b722_closing.txt', suite % 'pre-push', 'the pre-push suite')
    post, l_post = fl('b722_closing.txt', suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = fl('b722_closing.txt', r'^\s*pre-push, \(R332\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (cc, cd), l_cn = fl('b722_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    (nbk,), l_bk = fl('b722_closing.txt', r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = fl('b722_closing.txt', r'^### THE MIRROR .*mirror-refresh-2026-10-28-b722\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b722 '
                       + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = fl('b722_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) REFUTED \(N5\) REFUTED ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    _x, l_e9 = fl('b722_events.txt', r'^    \(9\) THE SEAT\'S \[CLOSE ; NEW\]: 18:45Z, AT THE SCORES', 'event (9)')
    _x, l_dh = fl('b722_defects.txt', r'^    \(h\) THE SEAT\'S \[CLOSE ; NEW\]: Component 2, the used-set reader', 'defect (h)')
    ar = json.load(open(os.path.join(D, 'b722_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b722_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev = event_rows()
    dr = defect_rows()
    if sorted(ev) != list(range(1, 16)) or len(dr) != 27:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (WEIGHT_HEAD + ' -- b722 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b722_closing.txt):* “%s” (data/b722_closing.txt :1); its '
            'relay commit the record’s %s, the closing’s %s (data/b722_steps.json, the record and closing rows). As the banks confirm by '
            'row: the corrigendum for b720 at %s items, CLAIM %s, CLOSE %s (data/b722_corrigendum.txt :%d); the C2 rule’s output NONE, every '
            'one of the eighteen fields of class number 2 at a table value of -2 or -1/2 (data/b722_registrations.txt :%d), its positive '
            'control taking -24 and -88 (:%d); H-C2-WALK at the fourteen unused fields committed before any figure (:%d); H-C3-31 (n0 = 80) and '
            'H-C4-55 (n0 = 224), b = -2 at both, the model naming the same n0, committed at e8c3dff4 (:%d, :%d); the table over h = 3, 4, 5 '
            'checked by two routes, not compiled (data/b722_derivation.txt :%d); H-OFFSET on its seventeen post hoc rows HELD 3, REFUTED 14 '
            '(data/b722_offset_read.txt :%d); the next tier 53 chosen, none formed (data/b722_offset_tier.txt :%d); the surgery carried '
            '(data/b722_surgery_carry.txt :%d); the frozen line EXCEEDS 7, 0, 7 and 9, STATED 2, 8, 3 and 1 at SIDE-archimedean, '
            'SIDE-frobenius, SIDE-spinor and SIDE-rcurve (data/b722_frozen_line.txt :%d); 6 of 6 wave 1 kernels building at their own pins, '
            'SIDE-lv-conservation v0.10.0 with one sorry in T3_perClass_to_combinations (data/b722_rebuild.txt :%d, :%d), the axiom prints '
            'read at 1 of 6; the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both, the claim arms %s of %s (data/b722_closing.txt '
            ':%d, :%d, :%d); the counter CLAIM %s, CLOSE %s (:%d); N4 and N5 REFUTED at the record, the rest HELD (:%d) -- N4 by event (9) '
            '(data/b722_events.txt :%d), a restore after the lock gate leaving the hash bank on the edited bytes, N5 as declared; the root %s '
            'over %s banks chained from %s (data/b722_act_root.json; :%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root '
            'line (:%d); %d events in data/b722_events.txt, rows (1)-(%d); %d defects (a)–(z), (a’), CLAIM (d), (g), (i), (k), (u) '
            '(data/b722_defects.txt); defect (h), the USED reader’s needles missing -15, -23 and -39 (data/b722_defects.txt :%d), repaired at '
            '`(R333)`(2)(ii) below. Nothing deposited, nothing published. **The rule from this act ((R333)(1)):** “%s” (relay '
            'data/b723_rules.txt :%d, row (1), with its reading).' % (
                head, PREV_RECORD, PREV_CLOSE, cn, cl, cr, l_cg, l_out, l_pc, l_wk, l_31, l_55, l_de, l_or, l_ot, l_su, l_fz, l_rb, l_ax,
                pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, l_cn, l_sc, l_e9, K.B714_ROOT[:8], nbk,
                ar['previous'][:8], l_bk, msha, l_mi, len(ev), max(ev), len(dr), l_dh, RULE_QUOTED, l_rule))


# ================================================================================ (R333)(2): THE CORRIGENDUM FOR b722
def event_rows():
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '; its lines after at five."""
    out, cur = {}, None
    for l in rd('b722_events.txt').split(NL):
        m = re.match(r'^    \((\d+)\) (.*)$', l)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None and l.startswith('     '):
            out[cur] += ' ' + l.strip()
        else:
            cur = None
    return out


BRACKET = re.compile(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]: ")


def defect_rows():
    """(letter, owner, tag, column) for each row of data/b722_defects.txt opening four spaces."""
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b722_defects.txt')):
        b = BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3)))
    return out


# ### the events' needles ((R333)(2) names (1)-(15))
EVENTS = [(1, 'given the face\'s bare name'), (2, 'AFTER THE LOCK GATE\'S RECORD'), (3, '`git checkout 1e3399e2 -- <the three paths>`'),
          (4, 'G-NOTHING-RAN-AHEAD failed on real state'), (5, 'its act-root chain phase 467 s'), (6, 'LIVE PASSING 94'),
          (7, 'PASS 77, FAILED AS b720 FAILED 3, DIVERGE 35'), (8, 'THE SEAL REFUSED'), (9, 'N4 REFUTED on one clause'),
          (10, 'option 3, push both'), (11, 'G-SEAL-HASHES failed'), (12, 'LIVE PASSING 112'), (13, 'the post-push suite in seven parts'),
          (14, 'with no limit'), (15, 'CLEAN ON ALL THREE CLAUSES')]

# ### the refusals (data/b722_hook_refusals.txt at b722's closing commit, one a line) and the row recording each: (line, kind, the row, a needle)
REFUSALS = [(1, 'PIPE', 'defect (c)', 'hook_refusals.txt :1'), (2, 'PIPE', 'defect (l)', 'hook_refusals.txt :2'),
            (3, 'ENV', 'defect (n)', 'hook_refusals.txt :3'), (4, 'REDIR', 'defect (o)', 'hook_refusals.txt :4'),
            (5, 'PIPE', 'defect (q)', 'hook_refusals.txt :5'), (6, 'PIPE', 'defect (r)', 'hook_refusals.txt :6'),
            (7, 'REDIR', 'defect (s)', 'hook_refusals.txt :7'), (8, 'PIPE', 'defect (v)', 'hook_refusals.txt :8'),
            (9, 'READ', 'defect (z)', 'hook_refusals.txt :9'), (10, 'READ', 'event (14)', 'hook_refusals.txt :10')]
PREV_BANK_LINE = (13, 'PIPE', 'defect (a)', 'data/b720_hook_refusals.txt')   # ### b722's own refusal, in b720's bank (act_current naming b720)

CORR_TITLE = ('## Corrigendum to b722’s record (relay data/b722_events.txt rows (1)-(15) and data/b722_defects.txt): fifteen events and '
              'twenty-seven defects, each CLAIM or CLOSE and NEW or REPEAT, and three repairs at tools/standing/ v1.2.2, each controlled on '
              'b722’s banks, under (R333)(2)')
CORRIGENDA_LAST = 41
V122 = 'b723_standing_v122.txt'


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’')


def v122_reads():
    """the v1.2.2 controls bank: every case AS WANTED, its section lines and the figures each item cites."""
    t = rd(V122).split(NL)
    cases = [l for l in t if re.match(r'^  \((i|ii|iii)\) ', l)]
    bad = [l for l in cases if not l.rstrip().endswith('AS WANTED') or 'NOT AS WANTED' in l]
    sec = dict((m.group(1), i) for i, l in enumerate(t, 1) for m in [re.match(r'^## \((i|ii|iii)\) ', l)] if m)
    foot = [i for i, l in enumerate(t, 1) if l.startswith('### ### **v1.2.2: CASES')]
    if len(cases) != 12 or bad or sorted(sec) != ['i', 'ii', 'iii'] or len(foot) != 1:
        sys.exit('### THE v1.2.2 CONTROLS BANK NOT AS READ (cases %d, not as wanted %d, sections %s) -- NOTHING COMPOSED' % (len(cases), len(bad), sorted(sec)))
    return dict(cases=len(cases), sec=sec, foot=foot[0])


def corr_state():
    ev = event_rows()
    miss = [n for n, h in EVENTS if h not in ev.get(n, '')]
    tags = {}
    for n, _h in EVENTS:
        m = BRACKET.match(ev.get(n, ''))
        tags[n] = (m.group(2), m.group(3), m.group(1)) if m else (None, None, None)
    dr = defect_rows()
    rl = git('show', '%s:data/b722_hook_refusals.txt' % PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    pl = git('show', '%s:data/b720_hook_refusals.txt' % K.ACT_CURRENT_COMMIT[:8]).replace(chr(13), '').strip(NL).split(NL)
    dtext = dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b722_defects.txt')))
    bad_ref = []
    for ln, kind, row, needle in REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1]:
            bad_ref.append(ln)
        elif row.startswith('defect'):
            if needle not in dtext.get(row.split('(')[1].rstrip(')'), ''):
                bad_ref.append(ln)
        elif needle not in ev.get(int(row.split('(')[1].rstrip(')')), ''):
            bad_ref.append(ln)
    # ### b722's own refusal in b720's bank: its line in the working file (uncommitted, as b722's defect (a) says), read beside the bank at HEAD
    wl = rd('b720_hook_refusals.txt').strip(NL).split(NL)
    pb_ok = len(wl) == PREV_BANK_LINE[0] and '| PIPE |' in wl[-1] and '13:05:54Z' in wl[-1] and PREV_BANK_LINE[3] in dtext.get('a', '')
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', rd('b675_corrigenda.txt'))]
    bad = [k for k, v in (('the event rows (1)-(15)', sorted(ev) == list(range(1, 16))), ('each event`s needle', not miss),
                          ('each event`s bracket', all(t[0] for t in tags.values())), ('the defect rows 27', len(dr) == 27),
                          ('the refusals 10, each answered as listed', len(rl) == 10 and not bad_ref),
                          ('b722`s line in b720`s bank, answered by defect (a)', pb_ok),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; needles missed %s ; refusals %s ; prev-bank lines %d)' % (
            bad, sorted(ev), miss, bad_ref, len(pl)))
    return dict(events=ev, tags=tags, defects=dr, v122=v122_reads())


def corr_counts(s):
    t = [s['tags'][n][0] for n, _h in EVENTS] + [x[2] for x in s['defects']]
    rep = sum(1 for n, _h in EVENTS if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def corr_lines(s):
    nc, nl, rep, n = corr_counts(s)
    v = s['v122']
    claims = [('(%d)' % k) for k, _h in EVENTS if s['tags'][k][0] == 'CLAIM'] + [('(%s)' % x[0]) for x in s['defects'] if x[2] == 'CLAIM']
    L = ['*b722’s events bank (relay data/b722_events.txt) carries fifteen rows, entered after its lock and seal and not lettered, each tagged '
         'in its own bracket (fourteen the seat’s, event (10) the author’s); its defects bank twenty-seven lettered rows, (a)-(z) and (a’), '
         'the seat’s but (d) and (e), the navigator’s, each tagged in its own bracket; its refusal bank ten lines at b722’s closing commit %s, '
         'and b722’s first refusal a line of b720’s bank, each recorded by a letter or an event. Each item is tagged CLAIM, where it touches a '
         'statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches '
         'the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry '
         'edits none of them.*' % PREV_CLOSE, '',
         '**The three repairs (`(R333)`(2)), at tools/standing/ v1.2.2, each controlled on b722’s banks with both instances shown** (relay '
         'data/%s, %d cases, every one AS WANTED, :%d):' % (V122, v['cases'], v['foot']), '',
         '**(i) G-SEAL-HASHES reads its list from the seal bank** (event (11); relay data/%s :%d): the arm compared the seal bank’s tools '
         'with the worklist’s SEALED tuple, a list kept in the suite, which carried b720’s thirty-three when tools/standing/ had gained three '
         'files at v1.2.1; tools/standing/sealcheck.py takes the list from the seal bank’s own `tools` map and reads each name in the tree '
         'at its hash. On b722’s seal read at its closing commit 30c0b3c8 the old reading fails on the list alone (33 against 36) and the '
         'new reads 36 of 36 and passes; a planted name absent from the tree fails it, and so does a planted hash.' % (V122, v['sec']['i']), '',
         '**(ii) USED by the discriminant and by its principal form** (defect (h); relay data/%s :%d): tools/standing/used.py reads each '
         'coefficient bank in every wording b711-b722’s banks carry -- the head’s “AT -15”, “D = -20”, “n0(-35)”, a principal form written '
         'out (“x^2 + xy + 10y^2”), a principal form as a triple (“(1, 1, 6)”), and the programme’s named form Q0 -- where b722’s reader '
         'read `D = ` and `n0(` alone. Over data/b711_coeffs.txt, b713, b717, b719 and b720 it reads -15, -20, -23, -35, -39, -40 and -47 USED; '
         'the old reading read -20, -35, -40 and -47; b711’s bank with its form’s name planted away no longer yields -23, as wanted.' % (V122, v['sec']['ii']), '',
         '**(iii) The readfirst closure reader retired** (relay data/%s :%d): from b723 data/bNNN_readfirst_closure.txt is not written and '
         'the hand list (data/bNNN_readfirst.txt) is the bank of record, as b710’s reading 5 recommended; tools/standing/readfirst.py reads '
         'the hand list present and unchanged since its first commit, and no closure bank. b722 (its closure written) fails the new reading '
         'and b723 at step zero passes; a planted closure bank beside b723’s hand list fails it; no tool of the standing set or the act calls '
         'the closure reader.' % (V122, v['sec']['iii']), '',
         '**b722’s events (1)-(15):**', '']
    for k, h in EVENTS:
        t, r, o = s['tags'][k]
        extra = {3: '; the restore an edit from b723, (R333)(1)', 9: '; ruled at (R333)(1), the rule of relay data/b723_rules.txt (1)',
                 11: '; repair (i)'}.get(k, '')
        L += ['**(%d) %s** (relay data/b722_events.txt, row (%d); %s; %s; %s%s).' % (k, h.replace("'", '’'), k, o.lower().replace("'s", '’s'), t, _col(r), extra)]
    L += ['', '**b722’s defects:**', '']
    for x, o, t, c in s['defects']:
        extra = {'h': '; ruled at (R333)(1), repair (ii)', 'u': '; G-AXIOM-CLAIM failing to the close, declared'}.get(x, '')
        L += ['**(%s)** (relay data/b722_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _col(c), extra)]
    L += ['', '**b722’s refusals** (relay data/b722_hook_refusals.txt at %s, one a line): ' % PREV_CLOSE + '; '.join(
        ':%d %s, recorded at %s' % (ln, kind, row.replace("'", '’')) for ln, kind, row, _n in REFUSALS)
          + '; and b722’s first, relay data/b720_hook_refusals.txt :%d %s, recorded at %s.' % PREV_BANK_LINE[:3], '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items of `(R333)`(2) (fifteen events, twenty-seven defects); REPEAT %d of %d; the '
          'CLAIM items %s.' % (nc, nl, n, rep, n, ', '.join(claims)), '',
          '*Filed at b723 on the author’s ruling `(R333)`(2): generated by relay `tools/b723_c1.py` corrigendum, written whole at b723, from '
          'b722’s events, defects and refusal banks read unedited and the v1.2.2 controls bank; banked as relay `data/b723_corrigendum.txt`, '
          'the corrigenda bank `data/b675_corrigenda.txt` appended at row (42). It answers b722’s record; no sealed tool, face, trail or '
          'root-named bank of b722 is edited.*']
    return L


def corr_bank_rows(s, ln):
    nc, nl, rep, n = corr_counts(s)
    return (['b723 -- THE CORRIGENDUM FOR b722, (R333)(2) (%s)' % R.utc(), '',
             '### the banks read unedited: data/b722_events.txt rows (1)-(15), data/b722_defects.txt 27 rows, data/b722_hook_refusals.txt 10 '
             'lines at %s and b722`s line of data/b720_hook_refusals.txt; data/%s (the v1.2.2 controls); the corrigenda bank`s last row (%d).' % (
                 PREV_CLOSE, V122, CORRIGENDA_LAST), '']
            + ['  ' + l for l in corr_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 15, DEFECTS 27 ; CLAIM %d, CLOSE %d ; REPEAT %d ; v1.2.2: (i) THE SEAL`S LIST FROM THE SEAL BANK, '
               '(ii) USED BY DISCRIMINANT AND PRINCIPAL FORM -- -15, -20, -23, -35, -39, -40, -47, (iii) THE CLOSURE READER RETIRED ; THE ENTRY AT '
               'FINDINGS :%s.**' % (n, nc, nl, rep, ln)])


# ================================================================================ THE ROUTES
def main(route, mode):
    dry = mode != 'write'
    if route == 'weight':
        text = weight_text()
        REC.land([('FINDINGS.md', WEIGHT_HEAD, NL + text + NL)], 'b723_record_lines.json', 'c1', entry=K.B711_ENTRY,
                 check=[('FINDINGS.md', K.B711_ENTRY, '## The C2 table’s rule chose no discriminant'),
                        ('OPEN_TRAILS.md', K.B711_TRAIL, '### b722 — lane two, act one hundred and forty-eight, the table act')], dry=dry)
        return
    if route == 'corrigendum':
        s = corr_state()
        text = NL + CORR_TITLE + NL + NL + NL.join(corr_lines(s)) + NL
        if dry:
            REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b723_corrigendum_landing.json', 'corrigendum', entry=None, dry=True)
            print(NL.join(corr_bank_rows(s, None)[:80]))
            return
        REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b723_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = line_of(R.FIND, CORR_TITLE)
        nc, nl, rep, n = corr_counts(s)
        _bank('b723_corrigendum.txt', corr_bank_rows(s, ln))
        bank_json('b723_corrigendum.json', dict(at=R.utc(), entry_line=ln, title=CORR_TITLE, claim=nc, close=nl, repeat=rep, items=n,
                                                events=[dict(row=k, owner=s['tags'][k][2], tag=s['tags'][k][0], column=s['tags'][k][1]) for k, _h in EVENTS],
                                                defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c in s['defects']],
                                                repairs=dict(version='v1.2.2', bank='data/' + V122, cases=s['v122']['cases']),
                                                row=CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; FINDINGS :%s' % (nc, nl, n, rep, ln))
        return
    sys.exit('usage: b723_c1.py weight | corrigendum  [dry | write]')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '', sys.argv[2] if len(sys.argv) > 2 else 'dry')
