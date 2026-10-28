# -*- coding: utf-8 -*-
"""b721_c1.py -- COMPONENT 1 OF b721, (R331)(1)-(2): b720 AT ITS WEIGHT AND THE CORRIGENDUM FOR b720, WITH THE THREE REPAIRS.
Written whole at b721 by the Write tool, in b720_c1.py's form (b720's tool composed b719's ten events and eighteen defects).

Routes, each `dry` (prints the text and the screens, writes nothing) or `write` (lands through b698's guarded landing, banks the line):
  weight       FINDINGS: b720's weight line after its entry (:11072), every figure read from b720's banks by line, and (R331)(1)'s rule
               (relay data/b721_rules.txt (1)).
  corrigendum  FINDINGS: the corrigendum for b720 from data/b720_events.txt (1)-(15) and data/b720_defects.txt (a)-(c'), each item CLAIM or
               CLOSE and NEW or REPEAT read from its own bracket; the refusals (the bank's twelve lines at b720's closing commit) answered by
               the letter or event that records each; the three repairs of (R331)(2) at tools/standing/ v1.2.1, each with its control on
               b720's banks (relay data/b721_standing_v121.txt) -- (i) the title from the answers bank, (ii) writes counted, a listing never
               a write, with event (12)'s cause read again from the transcript, (iii) the MANIFEST control at the build commit, wired into
               mbank, its diff beside (R328)(7)'s -- and the counter.
THE CHECKS BEFORE ANY WRITE: every figure's bank line found exactly once; the event rows (1)-(15), each bracketed; the defect rows 29, each
bracketed; each refusal's answering row carrying its needle; the v1.2.1 controls bank AS WANTED in every case. Any miss: nothing composed.
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

import b721_record as REC          # noqa: E402  ### the guarded landing (b698's), its screens, git
import b721_worklist as K          # noqa: E402
from b652_record import line_of    # noqa: E402

R = REC.R
PREV_CLOSE = '8834a5b6'            # ### b720's closing commit: the refusal bank read at it (its thirteenth line is b721's own, uncommitted)


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


# ================================================================================ (R331)(1): b720 AT ITS WEIGHT
WEIGHT_HEAD = '*Appended 2026-10-28 by b721 to b720’s entry (:%d), under `(R331)`(1)' % K.B711_ENTRY
HEAD_QUOTED = ('b720 closed: relay 6d7cb5f7, PLACE-papers b826da8; suite 111 of 116; root b5a76ed924905059…; 1 prompt answered; scores 7 of 8 '
               'HELD; 29 defects')
RULE_QUOTED = ('From this act: no figure at a registered discriminant is worked, by hand or by tool, before its registration commits; a '
               'model\'s prediction is written into the registration itself')


def weight_text():
    head = rd('b720_closing.txt').split(NL)[0]
    if head != HEAD_QUOTED:
        sys.exit('### data/b720_closing.txt :1 IS NOT THE HEAD LINE (R331)(1) QUOTES -- NOTHING COMPOSED')
    if RULE_QUOTED not in rd('b721_ferry.txt').replace(NL, ' '):
        sys.exit('### (R331)(1)`S RULE NOT FOUND IN THE FERRY AS QUOTED -- NOTHING COMPOSED')
    _x, l_rule = fl('b721_rules.txt', r'^  \(1\) NO FIGURE BEFORE ITS REGISTRATION\.', 'the rules bank`s row (1)')
    steps = json.load(open(os.path.join(D, 'b720_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing']
    if rec[-1:] != ['6d7cb5f7'] or clo != [PREV_CLOSE]:
        sys.exit('### data/b720_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    _x, l_co = fl('b720_coeffs.txt', r'n0\(-35\) = 135, b = -2 ; n0\(-40\) = 100, b = -1/2 ; ROWS 15: HELD 14, REFUTED 1, NOT SCORABLE 0 ; THE LAW REFUTED ; '
                  r'H-DECOMP HELD ; PRED-35 HELD, PRED-40 HELD ; FORCED 2 APART', 'the coefficients')
    _x, l_pr = fl('b720_prediction.txt', r'THE CONTROLS AS WANTED ; PREDICTED n0\(-35\) = 135, b = -2 ; PREDICTED n0\(-40\) = 100, b = -1/2', 'the prediction')
    _x, l_de = fl('b720_derivation.txt', r'CHECKS 5 STEPS x 7 DISCRIMINANTS AND THE C2 TABLE: ALL AS WANTED ; PLANTS: ALL FAIL AS WANTED ; THE GRADE', 'the grade')
    _x, l_rg = fl('b720_registry_diff.txt', r'REGISTRY\.md 200647 -> 218121 bytes', 'the registry cells')
    _x, l_ch = fl('b720_challenge.txt', r"VERDICT: ELABORATES; THE KERNEL'S STATEMENT MATCHES", 'the challenge file')
    _x, l_pi = fl('b720_pin.txt', r'THE PIN AT 1 OF 6 ELIGIBLE \(BUILDS\) ; PUSHED 6 ; DISPATCHED 6 ; READ 6 ; HELD \(BREAKS\) 5', 'the pin')
    _x, l_of = fl('b720_offset_price.txt', r"^b720 -- \(R330\)\(6\): THE OFFSET'S NEXT TIER UNDER H-OFFSET, PRICED, NOTHING RUN", 'the offset price')
    (cn, cl, cr), l_cg = fl('b720_corrigendum.txt', r'ITEMS (\d+): EVENTS 10, DEFECTS 18, MEMORY 1 ; CLAIM (\d+), CLOSE (\d+) ;', 'the corrigendum')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = fl('b720_closing.txt', suite % 'pre-push', 'the pre-push suite')
    post, l_post = fl('b720_closing.txt', suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = fl('b720_closing.txt', r'^\s*pre-push, \(R330\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (cc, cd), l_cn = fl('b720_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    (nbk,), l_bk = fl('b720_closing.txt', r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = fl('b720_closing.txt', r'^### THE MIRROR .*mirror-refresh-2026-10-28-b720\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b720 '
                       + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = fl('b720_closing.txt', r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    scc = json.load(open(os.path.join(D, 'b720_scores_close.json'), encoding='utf-8'))
    n5c = (scc.get('N5') or [None])[0]
    ar = json.load(open(os.path.join(D, 'b720_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT or n5c != 'REFUTED':
        sys.exit('### data/b720_act_root.json`s root %s ; scores_close N5 %s -- NOTHING COMPOSED' % (ar.get('root'), n5c))
    ev = event_rows()
    dr = defect_rows()
    if sorted(ev) != list(range(1, 16)) or len(dr) != 29:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (WEIGHT_HEAD + ' -- b720 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b720_closing.txt):* “%s” (data/b720_closing.txt :1); its '
            'relay commit the record’s 6d7cb5f7, the closing’s %s (data/b720_steps.json, the record and closing rows). As the banks confirm by '
            'row: the corrigendum for b719 at %s items, CLAIM %s, CLOSE %s (data/b720_corrigendum.txt :%d); the shape rule’s prediction committed '
            'before any coefficient, n0(-35) = 135 and n0(-40) = 100 (data/b720_prediction.txt :%d); the least negative index 135 and 100, '
            'b = -2 and -1/2, rows 15, HELD 14, REFUTED 1, the law’s value clause REFUTED at -40 and its prime clause HELD, H-DECOMP, '
            'PRED-35 and PRED-40 HELD, the forced 2 apart (data/b720_coeffs.txt :%d); the -2 of both configurations a theorem in C2 at Omega 4 '
            'with its hypotheses, a written proof checked by tool, the step at h > 2 named (data/b720_derivation.txt :%d); the REGISTRY '
            'attribute block appended, 0 lines removed (data/b720_registry_diff.txt :%d); the challenge file for h2_sign_iff_rh ELABORATES '
            '(data/b720_challenge.txt :%d); the pin at 1 of 6 eligible, 5 held as breaks, unrepaired (data/b720_pin.txt :%d); the offset’s '
            'next tier priced, nothing run (data/b720_offset_price.txt :%d); the surgery carried; the suite %s of %s pre-push and %s of %s '
            'post-push, NOT CLEAN both, the claim arms %s of %s (data/b720_closing.txt :%d, :%d, :%d); the counter CLAIM %s, CLOSE %s (:%d); '
            'N1-N5 and S1-S3 HELD at the record (:%d), N5 REFUTED at `scores close` on its one-git-write clause (data/b720_scores_close.json; '
            'event (12), its cause read again in the corrigendum below); the root %s over %s banks chained from %s (data/b720_act_root.json; '
            ':%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root line, its manifest control NOT AS WANTED against a carried '
            'reference (:%d; event (15)); %d events in data/b720_events.txt, rows (1)-(%d); %d defects (a)–(c’), all the seat’s, CLAIM (e) and '
            '(f) (data/b720_defects.txt). Nothing deposited, nothing published. **The rule from this act ((R331)(1)):** “%s” (relay '
            'data/b721_rules.txt :%d, row (1), with its reading).' % (
                head, PREV_CLOSE, cn, cl, cr, l_cg, l_pr, l_co, l_de, l_rg, l_ch, l_pi, l_of,
                pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, l_cn, l_sc, K.B714_ROOT[:8], nbk,
                ar['previous'][:8], l_bk, msha, l_mi, len(ev), max(ev), len(dr), RULE_QUOTED, l_rule))


# ================================================================================ (R331)(2): THE CORRIGENDUM FOR b720
def event_rows():
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '; its lines after at five."""
    out, cur = {}, None
    for l in rd('b720_events.txt').split(NL):
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
    """(letter, owner, tag, column) for each row of data/b720_defects.txt opening four spaces."""
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b720_defects.txt')):
        b = BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3)))
    return out


# ### the events' needles ((R331)(2) names (1)-(15))
EVENTS = [(1, 'tools/reg_seal.py --lock'), (2, 'G-PRIOR-CLOSED-PUSHED failed'), (3, 'G-CLOSING-SENTENCE failed'), (4, 'TITLE_NEEDLES'),
          (5, 'ARMS 116, LIVE PASSING 93'), (6, 'PASS 73, FAILED AS b719 FAILED 5'), (7, 'option 3, push both'), (8, 'piped to grep'),
          (9, 'ARMS RUN 116, LIVE PASSING 111'), (10, 'sed -n 3337,3375p'), (11, 'push-b720-preroot_push_out.txt with no limit'),
          (12, 'G-RULE-ONE-GIT-WRITE'), (13, 'the post-push suite in seven parts'), (14, "b719's traps with no limit"),
          (15, 'THE MANIFEST CONTROL reads NOT AS WANTED')]

# ### the refusals (data/b720_hook_refusals.txt at b720's closing commit, one a line) and the row recording each: (line, kind, the row, a needle)
REFUSALS = [(1, 'PIPE', 'defect (h)', 'hook_refusals.txt :1'), (2, 'PIPE', 'defect (i)', 'hook_refusals.txt :2'),
            (3, 'REDIR', 'defect (j)', 'hook_refusals.txt :3'), (4, 'PIPE', 'defect (n)', 'hook_refusals.txt :4'),
            (5, 'REDIR', 'defect (o)', 'hook_refusals.txt :5'), (6, 'PIPE', 'defect (v)', 'rootexclude'),
            (7, 'REDIR', 'defect (x)', '/dev/null'), (8, 'PIPE', "defect (b')", 'Out-Null'), (9, 'PIPE', "defect (c')", 'piped to head'),
            (10, 'PIPE', 'event (8)', '11:49:09Z'), (11, 'READ', 'event (11)', '12:21:21Z'), (12, 'READ', 'event (14)', '12:47:06Z')]

CORR_TITLE = ('## Corrigendum to b720’s record (relay data/b720_events.txt rows (1)-(15) and data/b720_defects.txt): fifteen events and '
              'twenty-nine defects, each CLAIM or CLOSE and NEW or REPEAT, and three repairs at tools/standing/ v1.2.1, each controlled on b720’s '
              'banks, under (R331)(2)')
CORRIGENDA_LAST = 40
V121 = 'b721_standing_v121.txt'


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’')


def v121_reads():
    """the v1.2.1 controls bank: every case AS WANTED, its section lines and the figures each item cites."""
    t = rd(V121).split(NL)
    cases = [l for l in t if re.match(r'^  \((i|ii|iii)\) ', l)]
    bad = [l for l in cases if not l.rstrip().endswith('AS WANTED') or 'NOT AS WANTED' in l]
    sec = dict((m.group(1), i) for i, l in enumerate(t, 1) for m in [re.match(r'^## \((i|ii|iii)\) ', l)] if m)
    foot = [i for i, l in enumerate(t, 1) if l.startswith('### ### **v1.2.1: CASES')]
    if len(cases) != 13 or bad or sorted(sec) != ['i', 'ii', 'iii'] or len(foot) != 1:
        sys.exit('### THE v1.2.1 CONTROLS BANK NOT AS READ (cases %d, not as wanted %d, sections %s) -- NOTHING COMPOSED' % (len(cases), len(bad), sorted(sec)))
    return dict(cases=len(cases), sec=sec, foot=foot[0])


def corr_state():
    ev = event_rows()
    miss = [n for n, h in EVENTS if h not in ev.get(n, '')]
    tags = {}
    for n, _h in EVENTS:
        m = BRACKET.match(ev.get(n, ''))
        tags[n] = (m.group(2), m.group(3), m.group(1)) if m else (None, None, None)
    dr = defect_rows()
    rl = git('show', '%s:data/b720_hook_refusals.txt' % PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    dtext = dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b720_defects.txt')))
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
    bad = [k for k, v in (('the event rows (1)-(15)', sorted(ev) == list(range(1, 16))), ('each event`s needle', not miss),
                          ('each event`s bracket', all(t[0] for t in tags.values())), ('the defect rows 29', len(dr) == 29),
                          ('the refusals 12, each answered as listed', len(rl) == 12 and not bad_ref),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; needles missed %s ; refusals %s)' % (bad, sorted(ev), miss, bad_ref))
    return dict(events=ev, tags=tags, defects=dr, v121=v121_reads())


def corr_counts(s):
    t = [s['tags'][n][0] for n, _h in EVENTS] + [x[2] for x in s['defects']]
    rep = sum(1 for n, _h in EVENTS if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def corr_lines(s):
    nc, nl, rep, n = corr_counts(s)
    v = s['v121']
    claims = [('(%d)' % k) for k, _h in EVENTS if s['tags'][k][0] == 'CLAIM'] + [('(%s)' % x[0]) for x in s['defects'] if x[2] == 'CLAIM']
    L = ['*b720’s events bank (relay data/b720_events.txt) carries fifteen rows, entered after its lock and seal and not lettered, each tagged '
         'in its own bracket (fourteen the seat’s, event (7) the author’s); its defects bank twenty-nine lettered rows, (a)-(z) and (a’)-(c’), '
         'each the seat’s and tagged in its own bracket; its refusal bank twelve lines at b720’s closing commit %s, each recorded by a letter '
         'or an event. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence '
         'a reader of the corpus meets, or CLOSE, where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter '
         'of its class. The tags are the banks’ own; this entry edits none of them.*' % PREV_CLOSE, '',
         '**The three repairs (`(R331)`(2)), at tools/standing/ v1.2.1, each controlled on b720’s banks with both instances shown** (relay '
         'data/%s, %d cases, every one AS WANTED, :%d):' % (V121, v['cases'], v['foot']), '',
         '**(i) The title the author reworded** (events (7) and (9); relay data/%s :%d): G-FINDINGS-ENTRY and G-ENTRY-TITLE-FORM compared '
         'the landed title with the record tool’s composition alone, so the author’s word itself failed both. tools/standing/title.py reads '
         'the word from the answers bank’s verbatim block, applies each change of the form “old” reads “new” to the composition (the old '
         'phrase found exactly once, the apostrophe in the ledger’s form) and returns no title where a phrase is not found, so the arm fails '
         'and never guesses. On b720’s banks the old reading is not equal to FINDINGS :11072 and the new one is; an answers bank with no word '
         'leaves the composition, and a word naming a phrase the title does not carry gives no title.' % (V121, v['sec']['i']), '',
         '**(ii) One git write per message, counting writes** (event (12); relay data/%s :%d): tools/standing/gitwrite.py splits each call '
         'into its commands and counts each write; a listing (`git branch` or `git tag` with no name or a listing flag, and every git read) is '
         'never a write. Read again from the transcript, event (12)’s cause was not the listing: the old reading, tools/rule_arms.py’s, did '
         'not count `git branch --list push-b720-*` (its matcher needs a name and a commit after `branch`); the message it counted twice '
         'carried two calls, the PowerShell branch creation and the Bash push through push_gated.sh. The same reading finds a second such '
         'message at the closing push, 12:50:15Z, after `scores close`; and the call-counting reading counts the message of 12:21:16Z once, '
         'though its one call carried a branch creation and a push line. Counting writes, b720’s window reads three messages over one '
         '(12:21:16Z, 12:21:51Z, 12:50:15Z) where the old reading read two; no listing counted. Event (12)’s wording -- “the second a '
         'listing read as a write by the trace’s matcher” -- stands as written; this item is its correction.' % (V121, v['sec']['ii']), '',
         '**(iii) The MANIFEST control at the build commit** (event (15); relay data/%s :%d): tools/standing/manifest.py control_at_build '
         'reads every roster file the zip carries against its blob at the commit the mirror was built at (PLACE-papers HEAD at the build), '
         'and the record tool’s mbank route now calls it in place of its inline loop against the carried K.RECUT_MERGE (a86c9429). On b720’s '
         'zip at b826da8 all 74 roster files read AS WANTED, where the old control read day1/Silence_of_Foundations.md NOT AS WANTED; the '
         'same zip read at a86c9429 as if it were the build fails, as wanted. The member reader was repaired with it: by path, then the '
         'builder’s `<parent>__<name>`, then the flat name, so the root README and the archive’s flattened README each find their own. '
         'Why (R328)(7)’s repair (b718’s a240e6b6) did not take: it added the control to the toolset, whose only caller was the class '
         'controls (tools/standing/classes.py); mbank, which writes the mirror bank, kept its inline loop through every carry from b718 to '
         'b720. Its diff and v1.2.1’s are printed beside each other in the controls bank.' % (V121, v['sec']['iii']), '',
         '**b720’s events (1)-(15):**', '']
    for k, h in EVENTS:
        t, r, o = s['tags'][k]
        extra = {7: '; repair (i)', 9: '; repair (i)', 12: '; its cause read again, repair (ii)', 15: '; repair (iii)'}.get(k, '')
        L += ['**(%d) %s** (relay data/b720_events.txt, row (%d); %s; %s; %s%s).' % (k, h.replace("'", '’'), k, o.lower().replace("'s", '’s'), t, _col(r), extra)]
    L += ['', '**b720’s defects:**', '']
    for x, o, t, c in s['defects']:
        L += ['**(%s)** (relay data/b720_defects.txt; the seat’s; %s; %s).' % (x.replace("'", '’'), t, _col(c))]
    L += ['', '**b720’s refusals** (relay data/b720_hook_refusals.txt at %s, one a line): ' % PREV_CLOSE + '; '.join(
        ':%d %s, recorded at %s' % (ln, kind, row.replace("'", '’')) for ln, kind, row, _n in REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items of `(R331)`(2) (fifteen events, twenty-nine defects); REPEAT %d of %d; the '
          'CLAIM items %s.' % (nc, nl, n, rep, n, ', '.join(claims)), '',
          '*Filed at b721 on the author’s ruling `(R331)`(2): generated by relay `tools/b721_c1.py` corrigendum, written whole at b721, from '
          'b720’s events, defects and refusal banks read unedited and the v1.2.1 controls bank; banked as relay `data/b721_corrigendum.txt`, '
          'the corrigenda bank `data/b675_corrigenda.txt` appended at row (41). It answers b720’s record; no sealed tool, face, trail or '
          'root-named bank of b720 is edited.*']
    return L


def corr_bank_rows(s, ln):
    nc, nl, rep, n = corr_counts(s)
    return (['b721 -- THE CORRIGENDUM FOR b720, (R331)(2) (%s)' % R.utc(), '',
             '### the banks read unedited: data/b720_events.txt rows (1)-(15), data/b720_defects.txt 29 rows, data/b720_hook_refusals.txt 12 '
             'lines at %s; data/%s (the v1.2.1 controls); the corrigenda bank`s last row (%d).' % (PREV_CLOSE, V121, CORRIGENDA_LAST), '']
            + ['  ' + l for l in corr_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 15, DEFECTS 29 ; CLAIM %d, CLOSE %d ; REPEAT %d ; v1.2.1: (i) THE TITLE FROM THE ANSWERS BANK, (ii) WRITES '
               'COUNTED -- EVENT (12)`S CAUSE THE BRANCH AND THE PUSH IN ONE MESSAGE, NOT THE LISTING, (iii) THE CONTROL AT THE BUILD COMMIT, WIRED '
               'INTO mbank ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl, rep, ln)])


# ================================================================================ THE ROUTES
def main(route, mode):
    dry = mode != 'write'
    if route == 'weight':
        text = weight_text()
        REC.land([('FINDINGS.md', WEIGHT_HEAD, NL + text + NL)], 'b721_record_lines.json', 'c1', entry=K.B711_ENTRY,
                 check=[('FINDINGS.md', K.B711_ENTRY, '## The coefficient law at -35 and -40'),
                        ('OPEN_TRAILS.md', K.B711_TRAIL, '### b720 — lane two, act one hundred and forty-seven, the decomposition act')], dry=dry)
        return
    if route == 'corrigendum':
        s = corr_state()
        text = NL + CORR_TITLE + NL + NL + NL.join(corr_lines(s)) + NL
        if dry:
            REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b721_corrigendum_landing.json', 'corrigendum', entry=None, dry=True)
            print(NL.join(corr_bank_rows(s, None)[:60]))
            return
        REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b721_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = line_of(R.FIND, CORR_TITLE)
        nc, nl, rep, n = corr_counts(s)
        _bank('b721_corrigendum.txt', corr_bank_rows(s, ln))
        bank_json('b721_corrigendum.json', dict(at=R.utc(), entry_line=ln, title=CORR_TITLE, claim=nc, close=nl, repeat=rep, items=n,
                                                events=[dict(row=k, owner=s['tags'][k][2], tag=s['tags'][k][0], column=s['tags'][k][1]) for k, _h in EVENTS],
                                                defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c in s['defects']],
                                                repairs=dict(version='v1.2.1', bank='data/' + V121, cases=s['v121']['cases']),
                                                event12_cause='the branch creation and the push in one message, not the listing',
                                                row=CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; FINDINGS :%s' % (nc, nl, n, rep, ln))
        return
    sys.exit('usage: b721_c1.py weight | corrigendum  [dry | write]')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '', sys.argv[2] if len(sys.argv) > 2 else 'dry')
