# -*- coding: utf-8 -*-
"""b723_c1.py -- COMPONENT 1 OF b723, (R333)(1)-(2): b722 AT ITS WEIGHT AND THE CORRIGENDUM FOR b722, WITH v1.3.0'S REPAIRS.
Written whole at b723 by the Write tool for b722's banks (the carried form, b722_c1.py's, composed b721's; its figures replaced, not
substituted), the record tool read through tools/standing/fold.py (the author's word, Option 2: tools/b723_record.py is the fold's render).

Routes, each `dry` (prints the text and the screens, writes nothing) or `write` (lands through b698's guarded landing, banks the line):
  weight       FINDINGS: b722's weight line after its entry (:11359), every figure read from data/b722_closing.txt by line -- "its rows
               as the closing and its banks print them" ((R333)(1)); the navigator's reading at b723's root is the navigator's.
  corrigendum  FINDINGS: the corrigendum for b722 from data/b722_events.txt (1)-(19) and data/b722_defects.txt (a)-(z), (a')-(e'), each
               CLAIM or CLOSE and NEW or REPEAT read from its own bracket; the refusals (b722's bank, ten lines at its closing commit,
               and its two lines in data/b721_hook_refusals.txt) answered by the row recording each; the three closing sentences
               (the author's word (2)) and the root answer's (a), each with its v8 dated note (standing clauses v8 row (82)); the five
               repairs of (R333)(2) at tools/standing/ v1.3.0 with the root answer's (b), each with its control on b722's banks (relay
               data/b723_standing_v130.txt), and v9 (data/standing_clauses_v9.txt); the counter beside the closing's.
THE CHECKS BEFORE ANY WRITE: every figure's bank line found exactly once; the closing's head line the one (R333)(1) quotes; the event rows
(1)-(19), each bracketed; the defect rows 31, each bracketed; each refusal's answering row carrying its time; each noted sentence found
on its line once; the v1.3.0 controls bank ALL AS WANTED; the counter equal to the closing's. Any miss: nothing composed.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path[:0] = [T, os.path.join(T, 'standing')]
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import fold                        # noqa: E402  ### the author's word, Option 2: the close tools are the fold's renders
fold.install()
import b723_record as REC          # noqa: E402  ### the guarded landing (b698's), its screens, git
import b723_worklist as K          # noqa: E402
from b652_record import line_of    # noqa: E402

R = REC.R
PP = 'D:/MY-DOwnloads/PLACE-papers'
PREV_CLOSE = '1607e994'            # ### b722's closing commit (relay main at b723's step zero): the refusal bank read at it
PREV_RECORD = '65430407'           # ### b722's record commit, its post-push reading's HEAD
NOTED = '2026-10-29'


def rd(name, base=D):
    with open(os.path.join(base, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def fl(name, pat, what, base=D):
    """the one line of a file matching pat: (groups, line number); any other count exits."""
    hits = [(i, m) for i, l in enumerate(rd(name, base).split(NL), 1) for m in [re.search(pat, l)] if m]
    if len(hits) != 1:
        sys.exit('### %s: %d LINES OF %s MATCH %r, NOT ONE -- NOTHING COMPOSED' % (what, len(hits), name, pat))
    return hits[0][1].groups(), hits[0][0]


def git(*a, repo=ROOT):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


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
WEIGHT_HEAD = '*Appended 2026-10-29 by b723 to b722’s entry (:%d), under `(R333)`(1)' % K.B711_ENTRY
ENTRY_NEEDLE = '## The class-number-2 table at its fourteen remaining fields: 14 of 14 HELD'
TRAIL_NEEDLE = '### b722 — lane two, act one hundred and forty-nine, the instruments act under (R332)'


def weight_text():
    head = rd('b722_closing.txt').split(NL)[0]
    q = re.search(r'^\(1\) b722 AT ITS WEIGHT\. "([^"]+)"', rd('b723_ferry.txt'), re.M)
    if not q or q.group(1) != head:
        sys.exit('### data/b722_closing.txt :1 IS NOT THE HEAD LINE (R333)(1) QUOTES -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b722_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing']
    if rec[-1:] != [PREV_RECORD] or clo != [PREV_CLOSE]:
        sys.exit('### data/b722_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    c = 'b722_closing.txt'
    (cc, cd), l_cn = fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    (sa, sb), l_sh = fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    _x, l_rp = fl(c, r'^      research/reproduce\.py +seal - ; close [0-9a-f]{16} ; ABSENT$', 'the reproduction runner`s seal row')
    (gi, gc, gl, gr), l_cg = fl(c, r'ITEMS (\d+): EVENTS 15, DEFECTS 27 ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;', 'the corrigendum for b721')
    (vc,), l_v = fl(c, r'v1\.2\.2: CASES (\d+), AS WANTED \1 ;', 'v1.2.2`s controls')
    _x, l_co = fl(c, r'n0\(-31\) = 80, b = -2 ; n0\(-55\) = 224, b = -2 ; H-C3-31 HELD ; H-C4-55 HELD ;', '-31 and -55')
    _x, l_wk = fl(c, r'H-C2-WALK: 14 OF 14 HELD, REFUTED 0, NOT SCORABLE 0 ; THE CONTROL ROW -15 HELD ;', 'the fourteen')
    _x, l_c2 = fl(c, r'THE C2 STATEMENT: E0 DERIVES ; .* AS WRITTEN, TRUE IN PYTHON AT 18 OF 18 ; PRICED: .*\(B\) THE CERTIFICATE ROUTE '
                     r'UNDER 1\.00e\+06 AT 18 OF 18', 'the C2 statement')
    _x, l_in = fl(c, r'THE RULE`S OUTPUT: 68 INSTRUMENTS \(68 NEW, TO BE ENTERED AS I-41 TO I-108\) ; POPULATION 3171, REUSED 309', 'the instruments')
    _x, l_re = fl(c, r'ROWS 68 ; REPRODUCES 63 ; DIFFERS 1 ; NOT RUN 4 ; PLANTED CONTROLS AS WANTED 64 OF 64 ;', 'the reproduction')
    _x, l_pr = fl(c, r'THE PROPAGATION READ: OBJECTS 3 ; HITS 431 ; .* READS WRONG 12 ; NOTES TO WRITE 58 ; UNREAD 0 ;', 'the propagation read')
    _x, l_ad = fl(c, r'PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PLACES 62 ; CONTROLS 3 OF 3 AS WANTED ;', 'the name and address')
    _x, l_ax = fl(c, r'THE AXIOM STEP AT FIVE PINS: TARGETS ABSENT AT THE PIN 3 ; BUILD TARGET NOT COVERING THE AXIOM FILE`S IMPORTS 0 ; '
                     r'STEP NOT THE PIN`S OWN 2 ; OTHER 0 ; NOTHING COMMITTED, PUSHED OR DISPATCHED ;', 'the axiom step')
    _x, l_ll = fl(c, r'SAME 1 ; DIFFERS 13 ; ABSENT 10 ; DRAFTS 23 ; NOTHING EDITED ;', 'the LLM-contribution line')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = fl(c, suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = fl(c, r'^\s*pre-push, \(R332\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (nbk,), l_bk = fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = fl(c, r'^### THE MIRROR .*mirror-refresh-2026-10-28-b722\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b722 '
                       + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = fl(c, r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) REFUTED \(N5\) REFUTED ; \(S1\) HELD \(S2\) HELD \(S3\) REFUTED$', 'the scores')
    (np_,), l_an = fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    _x, l_e12 = fl('b722_events.txt', r'^    \(12\) THE SEAT\'S \[CLOSE ; NEW\]: 01:49Z-01:50Z, AT THE SEAL', 'event (12)')
    ar = json.load(open(os.path.join(D, 'b722_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b722_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = event_rows(), defect_rows()
    if sorted(ev) != list(range(1, 20)) or len(dr) != 31:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (WEIGHT_HEAD + ' -- b722 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b722_closing.txt):* “%s” (data/b722_closing.txt :1); its '
            'relay commit the record’s %s, the closing’s %s (data/b722_steps.json, the record and closing rows). As the closing’s rows read: '
            'the corrigendum for b721 at %s items, CLAIM %s, CLOSE %s, REPEAT %s, and v1.2.2’s %s controls AS WANTED (:%d, :%d); -31 and -55 '
            'under e8c3dff4, n0 80 and 224, b = -2 at both, H-C3-31 and H-C4-55 HELD (:%d); the fourteen remaining class-number-2 fields '
            'under H-C2-WALK 14 of 14 HELD, the control row -15 HELD (:%d); the C2 statement for Lean graded E0 DERIVES, true as written in '
            'Python at 18 of 18, the certificate route priced under 1.00e+06 at 18 of 18 (:%d); the instruments’ rule choosing 68 of a '
            'population of 3171, entered as I-41 to I-108 (:%d); tools/research/reproduce.py 63 REPRODUCES, 1 DIFFERS (I-76), 4 NOT RUN, '
            'the plants 64 of 64 (:%d); the propagation read 431 hits, 12 reading wrong, 58 notes (:%d); the name and address 0 and 0 '
            '(:%d); the axiom step at five pins diagnosed, nothing dispatched (:%d); the LLM-contribution line SAME 1, DIFFERS 13, ABSENT '
            '10, 23 drafts in the relay alone (:%d). The sealed tools AGREE %s of %s, tools/research/reproduce.py ABSENT from the seal '
            '(:%d, :%d; event (12), data/b722_events.txt :%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both, the claim '
            'arms %s of %s (:%d, :%d, :%d); the counter CLAIM %s, CLOSE %s (:%d); N4, N5 and S3 REFUTED, the rest HELD (:%d); the root %s '
            'over %s banks chained from %s (data/b722_act_root.json; :%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root '
            'line (:%d); %s prompts answered (:%d); %d events in data/b722_events.txt, rows (1)-(%d); %d defects, (a)–(z) and (a’)–(e’) '
            '(data/b722_defects.txt). Nothing deposited, nothing published; the corrigendum for these rows follows, under `(R333)`(2).' % (
                head, PREV_RECORD, PREV_CLOSE, gi, gc, gl, gr, vc, l_cg, l_v, l_co, l_wk, l_c2, l_in, l_re, l_pr, l_ad, l_ax, l_ll,
                sa, sb, l_sh, l_rp, l_e12, pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, l_cn, l_sc,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, msha, l_mi, np_, l_an, len(ev), max(ev), len(dr)))


# ================================================================================ (R333)(2): THE CORRIGENDUM FOR b722
def event_rows():
    """the events bank's rows: {n: text}, a row a line opening four spaces and '(n) '; its lines after at five."""
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


BRACKET = re.compile(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


def defect_rows():
    """(letter, owner, tag, column, text) for each row of data/b722_defects.txt opening four spaces."""
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", rd('b722_defects.txt')):
        b = BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


# ### the refusals: b722's bank at its closing commit, one a line, and the row recording each (line, kind, time, row); its first two
# ### lines in b721's bank (the author's word (1): b721's file's 20:23Z and 20:25Z lines are b722's step zero)
REFUSALS = [(1, 'PIPE', '20:50:47Z', "defect (d)"), (2, 'REDIR', '21:18:28Z', "defect (h)"), (3, 'REDIR', '21:47:54Z', "defect (j)"),
            (4, 'PIPE', '21:54:36Z', "defect (l)"), (5, 'READ', '22:09:14Z', "defect (o)"), (6, 'READ', '22:09:26Z', "defect (p)"),
            (7, 'PIPE', '22:23:20Z', "defect (q)"), (8, 'PIPE', '22:46:46Z', "defect (u)"), (9, 'REDIR', '23:19:46Z', "defect (a')"),
            (10, 'ENV', '02:04:50Z', 'event (14)')]
PREV_BANK = [('PIPE', '20:23:29Z', 'defect (a)'), ('REDIR', '20:25:32Z', 'defect (b)')]

CORR_TITLE = ('## Corrigendum to b722’s record (relay data/b722_events.txt rows (1)-(19) and data/b722_defects.txt): nineteen events and '
              'thirty-one defects, each CLAIM or CLOSE and NEW or REPEAT; three closing sentences with their v8 dated notes; and five '
              'repairs at tools/standing/ v1.3.0, each controlled on b722’s banks, under (R333)(2)')
CORRIGENDA_LAST = 42
V130 = 'b723_standing_v130.txt'
V9 = 'standing_clauses_v9.txt'

# ### the noted sentences: (where, repository, path, line, needle, class, its words, the correction) -- the root answer's (a) and the
# ### author's word (2), each found on its line once at the repository's HEAD before any note is written
REPRO_FIX = ('the seal recorded 42 tools and tools/research/reproduce.py was not among them: the seal route read its own list, which lacked '
             'the runner the worklist’s SEALED names (event (12), relay data/b722_events.txt :%d; the sealed tools AGREE 42 of 43, relay '
             'data/b722_closing.txt :%d); the runner was unsealed at b722. From b723 the seal route reads the worklist’s SEALED, one list '
             'feeding both (repair (b) below)')
NEXT_FIX = ('the author’s word A+B named b722’s “Next” naming (R332)(14) and the line landed as composed before the lock, naming b723 the '
            'wave 1 act (event (18), relay data/b722_events.txt :%d); (R333) governs b723, the checkpoint act, and (R332)(14)’s twenty '
            'were carried whole to b723’s step zero')
TWENTY_FIX = ('the twelve orders listed leave out (R332)(14)’s twenty, carried to b723 whole; each was read at b722’s [21] against '
              'OPEN_TRAILS and FINDINGS, CLOSING LINE FOUND 0 of 20, OPEN 20 (event (19), relay data/b722_events.txt :%d), and is read '
              'against its trigger at b723’s Component 2')
NOTES = [
    ('the sealed entry', PP, 'FINDINGS.md', 11373, 'The runner tools/research/reproduce.py, sealed with the act’s tools', 'READS WRONG', 'repro'),
    ('the closing', ROOT, 'data/b722_closing.txt', 464, 'tools/research/reproduce.py sealed with the', 'READS WRONG', 'repro'),
    ('the sealed entry', PP, 'FINDINGS.md', 11395, '**Next.** b723 ((R332)(13)), the wave 1 act', 'READS WRONG', 'next'),
    ('the sealed trail', PP, 'OPEN_TRAILS.md', 16356, '**Next:** b723 ((R332)(13)), the wave 1 act', 'READS WRONG', 'next'),
    ('the closing, CARRIED FORWARD (a)', ROOT, 'data/b722_closing.txt', 470, 'b723 ((R332)(13)), the wave 1 act', 'READS WRONG', 'next'),
    ('the closing, CARRIED FORWARD (b)', ROOT, 'data/b722_closing.txt', 471, '(b) The orders: W-ORD-LV-FORWARD-PORT;', 'READS WRONG', 'twenty'),
]


def _col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’')


def _q(s):
    """a quoted line as the ledger carries quotes: the markdown marks escaped, the banks' backtick apostrophes printed as ’."""
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _written(repo, path, n):
    """the committer time of the commit that last wrote line n of path at HEAD (git blame), UTC."""
    out = git('blame', '--porcelain', '-L', '%d,%d' % (n, n), 'HEAD', '--', path, repo=repo)
    m = re.search(r'(?m)^committer-time (\d+)$', out)
    c = out.split(' ', 1)[0]
    return (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(m.group(1)))) if m else None), c[:8]


def notes_state():
    ev_ln = dict((k, fl('b722_events.txt', r'^    \(%d\) THE SEAT\'S ' % k, 'event (%d)' % k)[1]) for k in (12, 18, 19))
    _x, l_ab = fl('b722_closing.txt', r'^      research/reproduce\.py +seal - ; close [0-9a-f]{16} ; ABSENT$', 'the runner`s seal row')
    fixes = dict(repro=REPRO_FIX % (ev_ln[12], l_ab), next=NEXT_FIX % ev_ln[18], twenty=TWENTY_FIX % ev_ln[19])
    out = []
    for where, repo, path, n, needle, cls, fx in NOTES:
        lines = git('show', 'HEAD:' + path, repo=repo).replace(chr(13), '').split(NL)
        line = lines[n - 1] if n <= len(lines) else ''
        if line.count(needle) != 1:
            sys.exit('### %s :%d (%s) DOES NOT CARRY ITS SENTENCE ONCE (%d) -- NOTHING COMPOSED' % (path, n, where, line.count(needle)))
        at, c = _written(repo, path, n)
        i = line.index(needle)
        a, b = max(0, i - 40), min(len(line), i + len(needle) + 120)
        quote = ('…' if a else '') + line[a:b].strip() + ('…' if b < len(line) else '')
        if b >= len(line) and repo == ROOT and n < len(lines) and lines[n].startswith('    ') and not lines[n].lstrip().startswith('('):
            # ### a closing paragraph wraps at its own indent: the sentence's end read from the next line, up to its first ';'
            quote += ' ' + lines[n].strip().split(' ; ', 1)[0] + ' …'
        out.append(dict(where=where, place=('relay ' + path) if repo == ROOT else path, line=n, written=at, commit=c, cls=cls,
                        quote=quote, fix=fixes[fx]))
    return out


def v130_reads():
    """the v1.3.0 controls bank: its foot ALL AS WANTED, and the line of each control the entry cites."""
    t = rd(V130).split(NL)
    foot = [(i, l) for i, l in enumerate(t, 1) if l.startswith('### ### **v1.3.0: CONTROLS')]
    if len(foot) != 1 or 'ALL AS WANTED' not in foot[0][1]:
        sys.exit('### THE v1.3.0 CONTROLS BANK`S FOOT NOT ALL AS WANTED -- NOTHING COMPOSED')
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', foot[0][1])

    def at(needle):
        h = [i for i, l in enumerate(t, 1) if needle in l]
        if len(h) != 1:
            sys.exit('### THE v1.3.0 BANK: %d LINES CARRY %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
        return h[0]
    return dict(cases=int(m.group(1)), wanted=int(m.group(2)), foot=foot[0][0],
                text=at('THE TEXT CONTROL: 16 RENDERS ; ALL EQUAL BYTE FOR BYTE'), names=at('THE NAMES CONTROL: ALL AS WANTED'),
                prev=at('PREVNAMES: ALL AS WANTED'), twin=at('117 arm rows, EQUAL ARM FOR ARM -- AS WANTED'),
                peek=at('LINES 35 (b720 13, b721 12, b722 10)'), lock=at('with step 26`s phase `lock` (in memory): PASS -- AS WANTED'),
                retired=at('G-READFIRST-DIFF-BANKED in b723`s arms table: False -- AS WANTED (retired)'),
                seal=at('b723`s seal route`s list 47 equal to its worklist`s SEALED 47 -- AS WANTED'))


def corr_state():
    ev = event_rows()
    tags = {}
    for n in sorted(ev):
        m = BRACKET.match(ev[n])
        tags[n] = (m.group(2), m.group(3), m.group(1)) if m else (None, None, None)
    dr = defect_rows()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = git('show', '%s:data/b722_hook_refusals.txt' % PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if 'REFUSED BY THE HOOK (%s' % kind not in src:
            bad_ref.append(ln)
    pl = git('show', 'HEAD:data/b721_hook_refusals.txt').replace(chr(13), '').strip(NL).split(NL)
    bad_prev = [row for kind, at, row in PREV_BANK if not any(at in l and ('| %s |' % kind) in l for l in pl)
                or 'REFUSED BY THE HOOK (%s)' % kind not in dtext.get(row.split('(', 1)[1].rstrip(')'), '')]
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', rd('b675_corrigenda.txt'))]
    (cc, cd), _l = fl('b722_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+)$', 'the counter')
    s = dict(events=ev, tags=tags, defects=dr, v130=v130_reads(), notes=notes_state())
    nc, nl, _rep, _n = corr_counts(s)
    bad = [k for k, v in (('the event rows (1)-(19)', sorted(ev) == list(range(1, 20))),
                          ('each event`s bracket', all(t[0] for t in tags.values())), ('the defect rows 31', len(dr) == 31),
                          ('the refusals 10, each answered as listed', len(rl) == 10 and not bad_ref),
                          ('b722`s two lines in b721`s bank, answered by (a) and (b)', not bad_prev),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST),
                          ('the counter equal to the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl) == (int(cc), int(cd)))) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; prev-bank %s ; counter %d, %d)' % (bad, bad_ref, bad_prev, nc, nl))
    return s


def corr_counts(s):
    t = [s['tags'][n][0] for n in sorted(s['events'])] + [x[2] for x in s['defects']]
    rep = sum(1 for n in s['events'] if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def _owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v, k.lower().replace("'s", '’s')) for k, v in sorted(c.items(), key=lambda kv: -kv[1]))


EV_EXTRA = {5: '; repair (iii)', 6: '; repair (iv)', 8: '; repair (i), the --prev names computed', 9: '; repair (i)', 10: '; repair (i)',
            12: '; repair (b) and the dated notes above', 18: '; the dated notes above', 19: '; the dated note above, and b723’s Component 2'}
REFUSAL_LETTERS = set(row.split('(', 1)[1].rstrip(')') for _l, _k, _a, row in REFUSALS if row.startswith('defect')) | {'a', 'b'}


def corr_lines(s):
    nc, nl, rep, n = corr_counts(s)
    v = s['v130']
    claims = [('(%d)' % k) for k in sorted(s['events']) if s['tags'][k][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    L = ['*b722’s events bank (relay data/b722_events.txt) carries nineteen rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank thirty-one lettered rows, (a)-(z) and (a’)-(e’), each tagged in its own bracket (%s); its '
         'refusal bank ten lines at b722’s closing commit %s, and b722’s first two refusals lines of b721’s bank (the author’s word (1) at '
         'b723), each recorded by a letter or an event. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a '
         'registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches the close’s own record of '
         'itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _owners([s['tags'][k][2] for k in s['events']]), _owners([x[1] for x in s['defects']]), PREV_CLOSE), '',
         '**Three closing sentences, with their v8 dated notes** (standing clauses v8 row (82): every statement naming the corrected object '
         'read, a dated note beside each that reads wrong, no line rewritten; the root answer’s addition (a) and the author’s word (2) at '
         'b723). Each note is dated %s and points to the line it corrects; READS WRONG marks a line wrong as it landed:' % NOTED, '']
    for x in s['notes']:
        L += ['- **%s :%d** (%s; written %s at %s; %s, noted %s): "%s" -- %s.' % (
            x['place'], x['line'], x['where'], x['written'], x['commit'], x['cls'], NOTED, _q(x['quote']), x['fix'])]
    L += ['', '**The repairs (`(R333)`(2) and the root answer’s (b)), at tools/standing/ v1.3.0, each controlled on b722’s banks with both '
          'instances shown** (relay data/%s, %d cases, AS WANTED %d, :%d):' % (V130, v['cases'], v['wanted'], v['foot']), '',
          '**(i) The close tools take the act** (events (8)-(10); the author’s word at b723, Option 2): the seven tools b722 carried as '
          'copies of b721’s -- checks, citation, closing, record, reg_gate, regspec, report -- fold into tools/standing/fold.py, one module '
          'taking the act: a template per tool (tools/standing/fold/), the lines b721’s and b722’s tools share, and an act arms module per '
          'act (tools/acts/) holding its own lines, named by data/act_current.json; the --prev names computed from the worklists, the '
          'act-numbered predecessors imported through tools/standing/legacy.py by name (192), a stated exception to tools/standing/act.py’s '
          'rule, their flattening priced and carried to b724 (relay data/b723_fold.txt). Its controls: every render of b722’s and b721’s '
          'tools equal to the file byte for byte, a planted section differing (:%d); a planted worklist missing one name refused (:%d); the '
          '--prev names owned alike on every name both worklists carry, the --prev reading itself the pre-seal run’s (:%d); b722’s suite '
          'run in a worktree at its record commit by the tool as b722 left it and by the fold, 117 arm rows equal arm for arm (:%d; relay '
          'data/b723_fold_run.txt, the four arms the worktree reads differently from b722’s bank each with its cause).' % (
              v['text'], v['names'], v['prev'], v['twin']), '',
          '**(ii) A pipe-free reader, tools/standing/peek.py** (the refusal-class defects below): search, head, tail, count and list with no '
          'pipe and no redirect; each of b720’s, b721’s and b722’s 35 refusal lines re-run through it, the hook unchanged (:%d).' % v['peek'], '',
          '**(iii) The lock row** (event (5)): the step recorder takes “lock” as a phase, before the seal; G-SEALED-AFTER-COMPONENTS reads '
          'the lock commit by that phase, one lock row. On b722’s steps bank, whose step 26 reads “gate”, the new reading fails as banked and '
          'passes with that row’s phase “lock”; a second lock row fails it (:%d).' % v['lock'], '',
          '**(iv) G-READFIRST-DIFF-BANKED retired** (event (6)), with the reader `(R332)`(2)(iii) retired; v8’s propagation read run over '
          'the suite’s arms for every other arm reading a retired or stopped bank, each found retired, conditional, or reading for '
          'absence (:%d).' % v['retired'], '',
          '**(v) The repeat rule, standing clause v9** (relay data/%s, row (83), its own commit %s): a defect of a class a previous act '
          'recorded is met with a repair, its control printed, or a ruling line saying why not; the closing prints the count of repeats; '
          'a class repeating in three acts running is the next act’s opening component.' % (V9, K.STANDING_COMMIT[:8]), '',
          '**(b) The seal route’s list read from the worklist’s SEALED** (event (12); the root answer’s (b)): one list feeds the seal and '
          'the suite; b723’s seal list equal to its SEALED, tools/research/reproduce.py in it (:%d).' % v['seal'], '',
          '**b722’s events (1)-(19):**', '']
    for k in sorted(s['events']):
        t, r, o = s['tags'][k]
        # ### the row's lead phrase alone (its words before the first colon), the row cited for the rest
        h = re.sub(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k]).split(': ', 1)[0]
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b722_events.txt, row (%d); %s; %s; %s%s).' % (
            k, _q(h).replace("'", '’'), k, o.lower().replace("'s", '’s'), t, _col(r), EV_EXTRA.get(k, ''))]
    L += ['', '**b722’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        extra = '; repair (ii)' if x in REFUSAL_LETTERS else ''
        L += ['**(%s)** (relay data/b722_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _col(c), extra)]
    L += ['', '**b722’s refusals** (relay data/b722_hook_refusals.txt at %s, one a line): ' % PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in REFUSALS)
          + '; and b722’s first two, lines of relay data/b721_hook_refusals.txt: ' + '; '.join(
        '%s %s, recorded at %s' % (kind, at, row) for kind, at, row in PREV_BANK) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items of `(R333)`(2) (nineteen events, thirty-one defects), equal to b722’s '
          'closing’s (relay data/b722_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (nc, nl, n, rep, n, ', '.join(claims)), '',
          '*Filed at b723 on the author’s ruling `(R333)`(2): generated by relay `tools/b723_c1.py` corrigendum, written whole at b723, from '
          'b722’s events, defects and refusal banks read unedited, the lines noted read at their repositories’ HEAD, and the v1.3.0 controls '
          'bank; banked as relay `data/b723_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers '
          'b722’s record; no sealed tool, face, trail or root-named bank of b722 is edited.*' % (CORRIGENDA_LAST + 1)]
    return L


def corr_bank_rows(s, ln):
    nc, nl, rep, n = corr_counts(s)
    return (['b723 -- THE CORRIGENDUM FOR b722, (R333)(2) (%s)' % R.utc(), '',
             '### the banks read unedited: data/b722_events.txt rows (1)-(19), data/b722_defects.txt 31 rows, data/b722_hook_refusals.txt 10 '
             'lines at %s and b722`s two lines of data/b721_hook_refusals.txt; the noted lines at their repositories` HEAD; data/%s (the '
             'v1.3.0 controls); the corrigenda bank`s last row (%d).' % (PREV_CLOSE, V130, CORRIGENDA_LAST), '']
            + ['  ' + l for l in corr_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 19, DEFECTS 31 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.3.0: (i) THE CLOSE TOOLS '
               'FOLDED, (ii) THE PIPE-FREE READER, (iii) THE LOCK ROW, (iv) G-READFIRST-DIFF-BANKED RETIRED, (v) v9, (b) THE SEAL`S LIST FROM '
               'SEALED ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl, rep, len(s['notes']), ln)])


# ================================================================================ THE ROUTES
def main(route, mode):
    dry = mode != 'write'
    if route == 'weight':
        text = weight_text()
        REC.land([('FINDINGS.md', WEIGHT_HEAD, NL + text + NL)], 'b723_record_lines.json', 'c1', entry=K.B711_ENTRY,
                 check=[('FINDINGS.md', K.B711_ENTRY, ENTRY_NEEDLE), ('OPEN_TRAILS.md', K.B711_TRAIL, TRAIL_NEEDLE)], dry=dry)
        return
    if route == 'corrigendum':
        s = corr_state()
        text = NL + CORR_TITLE + NL + NL + NL.join(corr_lines(s)) + NL
        if dry:
            REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b723_corrigendum_landing.json', 'corrigendum', entry=None, dry=True)
            print(NL.join(corr_bank_rows(s, None)))
            return
        REC.land([('FINDINGS.md', CORR_TITLE, text)], 'b723_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = line_of(R.FIND, CORR_TITLE)
        nc, nl, rep, n = corr_counts(s)
        _bank('b723_corrigendum.txt', corr_bank_rows(s, ln))
        bank_json('b723_corrigendum.json', dict(at=R.utc(), entry_line=ln, title=CORR_TITLE, claim=nc, close=nl, repeat=rep, items=n,
                                                events=[dict(row=k, owner=s['tags'][k][2], tag=s['tags'][k][0], column=s['tags'][k][1]) for k in sorted(s['events'])],
                                                defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                notes=s['notes'], repairs=dict(version='v1.3.0', bank='data/' + V130, cases=s['v130']['cases']),
                                                row=CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: b723_c1.py weight | corrigendum  [dry | write]')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '', sys.argv[2] if len(sys.argv) > 2 else 'dry')
