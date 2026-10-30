# -*- coding: utf-8 -*-
# b724 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R334)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R334)(2) repair it carries. Edited by the Edit tool. Carried at b724 by tools/b724_fold.py (`carry`) from tools/acts/b723.py,
# b723`s names substituted; the citation`s sections adopted from tools/b724_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b723`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b723`s carried till
# then); the loader prints them at every load, and the seal wants every PENDING line empty.
#⟪DEAD checks ⟫
#⟪DEAD citation ⟫
#⟪DEAD closing ⟫
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,C2_HALT,C2_PRED,C2_REG,C2_SELECT,C3_RULE,C4_PRED,C6_CENSUS,C6_DRAFTS,C6_FROZEN,C6_RELAY,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
#⟪DEAD reg_gate ⟫
#⟪DEAD regspec ⟫
#⟪DEAD report ⟫
# Each "#⟪PENDING <tool> <names>⟫" line: names the act`s tool reads on routes carried from the act before that the act has
# still to write for itself; printed at every load; the act`s suite holds them empty at its seal.
#⟪PENDING checks ⟫
#⟪PENDING citation ⟫
#⟪PENDING closing ⟫
#⟪PENDING record ⟫
#⟪PENDING reg_gate ⟫
#⟪PENDING regspec ⟫
#⟪PENDING report ⟫
# ### b724, Component 1 (the Edit tool): THE c1 ROUTE FOR b723'S WEIGHT LINE AND ITS CORRIGENDUM, (R334)(1)-(2). b723 wrote tools/b723_c1.py
# ### for b722's banks; (R334)(8)'s (W) list names no act tool beyond the fold's file, so b724's composer is this override of the template's
# ### c1 (record.tpl :1428-:1435), its form b723_c1.py's with b723's figures read by needle from b723's banks: `c1 weight|corrigendum
# ### [dry|write]`; dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = 'b8334f17'          # ### b723's closing commit (relay main at b724's step zero): its refusal bank read at it
C1_NOTED = '2026-10-29'
C1_CORRIGENDA_LAST = 43
C1_V140 = 'b724_standing_v140.txt'
C1_WEIGHT_HEAD = '*Appended 2026-10-29 by b724 to b723’s entry (:%d), under `(R334)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The close tools at v1.3.0 and five repeat classes repaired'
C1_TRAIL_NEEDLE = '### b723 — lane two, act one hundred and fifty, the checkpoint act under (R333)'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


def _c1_rd(name, base=None):
    with open(os.path.join(base or D, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def _c1_fl(name, pat, what, base=None):
    """the one line of a bank matching pat: (groups, line number); any other count exits, nothing composed."""
    hits = [(i, m) for i, l in enumerate(_c1_rd(name, base).split(NL), 1) for m in [re.search(pat, l)] if m]
    if len(hits) != 1:
        sys.exit('### %s: %d LINES OF %s MATCH %r, NOT ONE -- NOTHING COMPOSED' % (what, len(hits), name, pat))
    return hits[0][1].groups(), hits[0][0]


def _c1_git(*a, repo=None):
    return subprocess.run(['git', '-C', repo or ROOT] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


def _c1_events():
    out, cur = {}, None
    for l in _c1_rd('b723_events.txt').split(NL):
        m = re.match(r'^    \((\d+)\) (.*)$', l)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None and l.startswith('     '):
            out[cur] += ' ' + l.strip()
        else:
            cur = None
    return out


def _c1_defects():
    out = []
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b723_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b723_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    q = re.search(r'^\(1\) b723 AT ITS WEIGHT\. Its closing head line, quoted from data/b723_closing\.txt :1 as the public relay carries it at '
                  r'b8334f17: "([^"]+)"', _c1_rd('b724_ferry.txt'), re.M)
    if not q or q.group(1) != head:
        sys.exit('### data/b723_closing.txt :1 IS NOT THE HEAD LINE (R334)(1) QUOTES -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b723_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay'
           and 'data/b723_components.txt' in _c1_git('show', '--name-only', '--format=', r['commit']).split(NL)]   # ### the record commit: the one carrying the components
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if not rec or clo[-1:] != [C1_PREV_CLOSE]:
        sys.exit('### data/b723_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    (gi, gc, gl, gr), l_cg = _c1_fl(c, r'ITEMS (\d+): EVENTS 19, DEFECTS 31 ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;', 'the corrigendum for b722')
    (vc,), l_v = _c1_fl(c, r'v1\.3\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED \1 ; ALL AS WANTED', 'v1.3.0`s controls')
    (nsec,), l_fo = _c1_fl(c, r'tools/acts/b723\.py: sections (\d+), overrides', 'the fold')
    _x, l_zk = _c1_fl(c, r'H-ZETAK: C1 AS WANTED ; C2 AS WANTED ; C3 HOLDS ; .* THE HYPOTHESIS HELD ;', 'H-ZETAK')
    _x, l_su = _c1_fl(c, r'H-SUPPORT: C1 AS WANTED ; ZEROS 3 ; ONSETS COMPUTED 2 ; WITHIN 0\.03 0 ; BEYOND REACH 1 ; FALSIFIER FIRED ; THE HYPOTHESIS REFUTED', 'H-SUPPORT')
    _x, l_so = _c1_fl(c, r'the falsifier fired at off12, off27; THE HYPOTHESIS REFUTED', 'H-SUPPORT`s zeros')
    _x, l_di = _c1_fl(c, r'H-DIAL: BUILD PRICED .* ; NOT RUN ; CARRIED, ITS REGISTRATION COMMITTED', 'H-DIAL')
    _x, l_rg = _c1_fl(c, r'^    H-SUPPORT, H-ZETAK and H-DIAL committed alone at 9ad26421 before any figure', 'the registrations')
    _x, l_cf = _c1_fl(c, r'THE C2 CLOSED FORM: WRITTEN AS A DERIVATION, FOUR STEPS ; CHECKED POST HOC, 19 ROWS OF 19 REPRODUCED, THE PLANTED e_p FAILING ; NOT COMPILED', 'the C2 closed form')
    _x, l_ax = _c1_fl(c, r'THE AXIOM STEP AT 6 OF 6 PINS \(5 REPAIRED AND RUN THIS ACT, SIDE-lv-conservation CLEAN AT b721\) ; HALTED 0 \(none\) ; RUNS 5 ;', 'the axiom step')
    (oo, oo_open, oo_closed), l_or = _c1_fl(c, r'\*\*AT HEAD: ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', 'the orders at HEAD')
    _x, l_tw = _c1_fl(c, r'THE TWENTY: TRIGGER NOT MET 12 ; TRIGGER MET 6 .* OFFERED FOR RETIRE 1 ;', 'the twenty')
    _x, l_sp = _c1_fl(c, r'THE LEDGER SPLIT: CARRIED WHOLE TO b724 WITH ITS PRICE', 'the ledger split')
    _x, l_re = _c1_fl(c, r'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4 ; PLANTED CONTROLS AS WANTED 64 OF 64 ;', 'the reproduction')
    _x, l_ad = _c1_fl(c, r'PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; PLACES 22 ; CONTROLS 4 OF 4 AS WANTED ;', 'the name and address')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = _c1_fl(c, r'^\s*pre-push, \(R333\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = _c1_fl(c, r'^### THE MIRROR .*mirror-refresh-2026-10-29-b723\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b723 '
                           + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = _c1_fl(c, r'^\s*\(N1\) HELD \(N2\) REFUTED \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    _x, l_e9 = _c1_fl('b723_events.txt', r'^    \(9\) THE SEAT\'S \[CLAIM ; NEW\]: 18:21:34Z, AT THE ROOT', 'event (9)')
    ar = json.load(open(os.path.join(D, 'b723_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b723_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 19)) or len(dr) != 39:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b723 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b723_closing.txt):* “%s” (data/b723_closing.txt :1); its '
            'relay commit the record’s %s, the closing’s %s (data/b723_steps.json, the record and closing rows). As the closing’s rows read: '
            'the corrigendum for b722 at %s items, CLAIM %s, CLOSE %s, REPEAT %s, and v1.3.0’s %s controls AS WANTED (:%d, :%d); the seven '
            'close tools folded into tools/standing/fold.py, tools/acts/b723.py carrying %s sections (:%d); H-ZETAK HELD on Q0’s two onset '
            'windows (:%d); H-SUPPORT REFUTED, the falsifier fired at off12 and off27, off52 beyond reach (:%d, :%d); H-DIAL priced, not run, '
            'carried with its registration committed (:%d); the registrations committed alone at 9ad26421 before any figure (:%d); the C2 '
            'closed form written as a derivation and checked POST HOC, 19 rows of 19, not compiled (:%d); the axiom step at 6 of 6 pins, '
            'five runs (:%d); the orders generator at %s orders, %s open and %s closed at HEAD (:%d), the twenty read, W-ORD-STATUS-CELLS '
            'offered for retire (:%d); the ledger split carried whole with its price (:%d); tools/research/reproduce.py 64 REPRODUCES, '
            '0 DIFFERS, 4 NOT RUN, the plants 64 of 64 (:%d); the name and address 0 and 0 (:%d). The sealed tools AGREE %s of %s (:%d); the '
            'suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both, the claim arms %s of %s (:%d, :%d, :%d); the counter CLAIM %s, '
            'CLOSE %s, REPEAT %s of %s (:%d); N2 REFUTED, the rest HELD (:%d), two of them REFUTED BY THE SUITE under `(R334)`(1) (the '
            'corrigendum below); the root %s over %s banks chained from %s (data/b723_act_root.json; :%d), carried as recorded, the chain '
            'reading b723 DISAGREE (event (9), data/b723_events.txt :%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root '
            'line (:%d); %s prompts answered (:%d); %d events in data/b723_events.txt, rows (1)-(%d); %d defects, (a)–(z) and (a’)–(m’) '
            '(data/b723_defects.txt). Nothing deposited, nothing published; the corrigendum for these rows follows, under `(R334)`(1)-(2).' % (
                head, rec[-1], C1_PREV_CLOSE, gi, gc, gl, gr, vc, l_cg, l_v, nsec, l_fo, l_zk, l_su, l_so, l_di, l_rg, l_cf, l_ax,
                oo, oo_open, oo_closed, l_or, l_tw, l_sp, l_re, l_ad, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], ca, cb,
                l_pre, l_post, l_cl, cc, cd, rp, rn, l_cn, l_sc, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, l_e9, msha, l_mi,
                np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b723's bank at its closing commit, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '03:42:23Z', 'defect (a)'), (2, 'PIPE', '04:30:06Z', 'defect (h)'), (3, 'ENV', '04:44:46Z', 'defect (i)'),
               (4, 'PIPE', '07:18:22Z', 'defect (j)'), (5, 'PIPE', '10:00:34Z', 'defect (n)'), (6, 'READ', '10:02:51Z', 'defect (o)'),
               (7, 'REDIR', '12:12:42Z', 'defect (p)'), (8, 'REDIR', '14:18:54Z', 'defect (t)'), (9, 'READ', '14:23:46Z', 'defect (u)'),
               (10, 'PIPE', '15:09:38Z', 'defect (x)'), (11, 'PIPE', '16:08:23Z', "defect (f')"), (12, 'REDIR', '16:24:32Z', "defect (k')"),
               (13, 'READ', '18:17:46Z', 'event (11)'), (14, 'READ', '18:24:25Z', 'event (11)')]
C1_CORR_TITLE = ('## Corrigendum to b723’s record (relay data/b723_events.txt rows (1)-(18) and data/b723_defects.txt): eighteen events and '
                 'thirty-nine defects, each CLAIM or CLOSE and NEW or REPEAT; the two score readings ruled, and dated notes beside the '
                 'sentences that read wrong; and the ten repeat classes and the root route repaired at tools/standing/ v1.4.0, each '
                 'controlled on its last banked instance, under (R334)(1)-(2)')
C1_EV15_FIX = ('the cause read wrong: G-SEALED-AFTER-COMPONENTS failed on relay 2be0135c, a commit of data/b723_bank_hashes.json and '
               'data/b723_steps.json alone, whose step row no commit can carry (and after the push on 14bf5ec5, the same kind), not on '
               'b722’s lock-phase class -- b723’s lock commit 85647a2f carried its `lock` row; read by replaying the arm over b723’s step '
               'bank and commits (relay data/b724_standing_v140.txt (iv), :%d), repaired at v1.4.0 (iv)')
C1_NEXT_FIX = ('`(R334)` governs b724, the second checkpoint act; it names b725 the research act and b726 the wave 1 act (relay '
               'data/b724_ferry.txt :%d, clause (10)); `(R333)`(11)’s wave 1 work is b726’s')
C1_SCORE_FIX = ('`(R334)`(1): where a score’s reader and the suite disagree, the suite governs -- %s is REFUTED BY THE SUITE: the score’s '
                'reading %s; the suite’s %s failing pre-push and post-push (relay data/b723_closing.txt :%d, :%d)')
C1_NOTES = [
    ('the closing`s event (15)', None, 'data/b723_closing.txt', 276, 'as at b722 (event (5) of b722)', 'READS WRONG', 'ev15'),
    ('the events bank, row (15)', None, 'data/b723_events.txt', 78, 'as at b722 (event (5) of b722)', 'READS WRONG', 'ev15'),
    ('the sealed entry', PP, 'FINDINGS.md', 11530, '**Next.** b724 ((R333)(11)), the wave 1 act', 'READS WRONG', 'next'),
    ('the sealed trail', PP, 'OPEN_TRAILS.md', 16412, '**Next:** b724 ((R333)(11)), the wave 1 act', 'READS WRONG', 'next'),
    ('the closing, CARRIED FORWARD (a)', None, 'data/b723_closing.txt', 438, 'b724 ((R333)(11)), the wave 1 act', 'READS WRONG', 'next'),
    ('the closing`s N4', None, 'data/b723_closing.txt', 152, '(N4) HELD -- the lock at 2026-10-29T16:44:53Z', 'REFUTED BY THE SUITE', 'n4'),
    ('the closing`s S2', None, 'data/b723_closing.txt', 155, '(S2) HELD -- the root recomputed equal', 'REFUTED BY THE SUITE', 's2'),
]


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_written(repo, path, n):
    out = _c1_git('blame', '--porcelain', '-L', '%d,%d' % (n, n), 'HEAD', '--', path, repo=repo)
    m = re.search(r'(?m)^committer-time (\d+)$', out)
    return (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(m.group(1)))) if m else None), out.split(' ', 1)[0][:8]


def _c1_v140_line(needle):
    t = _c1_rd(C1_V140).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.4.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_notes():
    _x, l_ferry = _c1_fl('b724_ferry.txt', r'^\(10\) THE ACT\'S PLACE ON THE PAPER PATH', 'the ferry`s (10)')
    _x, l_pre = _c1_fl('b723_closing.txt', r'^\s*pre-push : ARMS RUN : 116\. .*G-ACTROOT-VERIFY', 'the pre-push suite')
    _x, l_post = _c1_fl('b723_closing.txt', r'^\s*post-push : ARMS RUN : 116\. .*G-ACTROOT-VERIFY', 'the post-push suite')
    fixes = dict(ev15=C1_EV15_FIX % _c1_v140_line('  (iv) b723`s G-SEALED-AFTER-COMPONENTS'), next=C1_NEXT_FIX % l_ferry,
                 n4=C1_SCORE_FIX % ('N4', 'HELD (no bank after the root waits on it)', 'G-ACTROOT-LAST', l_pre, l_post),
                 s2=C1_SCORE_FIX % ('S2', 'HELD (the root recomputed equal)', 'G-ACTROOT-VERIFY', l_pre, l_post))
    out = []
    for where, repo, path, n, needle, cls, fx in C1_NOTES:
        lines = _c1_git('show', 'HEAD:' + path, repo=repo).replace(chr(13), '').split(NL)
        line = lines[n - 1] if n <= len(lines) else ''
        if line.count(needle) != 1:
            sys.exit('### %s :%d (%s) DOES NOT CARRY ITS SENTENCE ONCE (%d) -- NOTHING COMPOSED' % (path, n, where, line.count(needle)))
        at, cm = _c1_written(repo or ROOT, path, n)
        i = line.index(needle)
        a, b = max(0, i - 40), min(len(line), i + len(needle) + 100)
        quote = ('…' if a else '') + line[a:b].strip() + ('…' if b < len(line) else '')
        out.append(dict(where=where.replace('`', '’'), place=('relay ' + path) if repo is None else path, line=n, written=at, commit=cm,
                        cls=cls, quote=quote, fix=fixes[fx]))
    return out


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b723_hook_refusals.txt' % C1_PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if ('REFUSED BY THE HOOK (%s' % kind) not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b723_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+) ; REPEAT', 'the counter')
    v = _c1_rd(C1_V140)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.4.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=_c1_notes())
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(18)', sorted(ev) == list(range(1, 19))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 39', len(dr) == 39), ('the refusals 14, each answered as listed', len(rl) == 14 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.4.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter equal to the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl_) == (int(cc), int(cd)))) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; counter %d, %d)' % (bad, bad_ref, nc, nl_))
    s['v140_foot'] = foot[0]
    return s


def _c1_counts(s):
    t = [s['tags'][n][0] for n in sorted(s['events'])] + [x[2] for x in s['defects']]
    rep = sum(1 for n in s['events'] if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def _c1_owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v_, k_.lower().replace("'s", '’s')) for k_, v_ in sorted(c.items(), key=lambda kv: -kv[1]))


def _c1_col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’')


# ### the repairs each event or defect is met by at v1.4.0 (the ten classes of (R334)(2) and the root route)
C1_EV_EXTRA = {1: '', 3: '; repair (vi)', 7: '; repair (vi)', 9: '; the root route', 10: '; the root route', 11: '; repair (ii)',
               12: '; the root route', 13: '; repair (vii)', 14: '; repair (vi)', 15: '; repair (iv), the dated notes above',
               16: '; repair (iii), the post-push re-run`s own file', 17: '; the root route', 18: '; repair (vi)'}
C1_DF_EXTRA = {'d': '; repair (ix)', 'b\'': '; repair (ii)', 'g\'': '; repair (iii)', 'l\'': '; repair (v)', 'y': '; repair (v)',
               'v': '; repair (v)', 'w': '; repair (v)'}
C1_REFUSAL_LETTERS = set(row.split('(', 1)[1].rstrip(')') for _l, _k, _a, row in C1_REFUSALS if row.startswith('defect'))
C1_CLASSES = (
    ('i', 'Hook refusals of pipes and redirects', 'tools/standing/peek.py takes the three reads v1.3.0’s control left uncovered -- a tally, a '
          'JSON read, a read by byte offset -- each of b721’s :6 and :7 and b722’s :9 failing on v1.3.0’s reader and passing on v1.4.0’s, '
          'the hook allowing the call'),
    ('ii', 'Read calls with a limit and no offset on files of 200 lines or more', 'the hook refuses them (tools/standing/hook.py): b723’s '
           '(b’) offences replayed, each allowed by v1.3.0’s hook and refused by v1.4.0’s, the same calls with an offset allowed'),
    ('iii', 'Hand-kept name lists', 'CARRIED_FAILING read from the face’s declared line, not a template literal; a part run pre-push after '
            'the record commit refused, the post-push re-run to a file of its own (event (16)); the seal’s list read from the worklist '
            '(v1.3.0, b722’s event (12) replayed); `--prev` reading the previous worklist’s value only where it carries one in this act’s '
            'shape (b722’s events (8)-(10))'),
    ('iv', 'The lock phase and the step recorder’s phases', 'the phases read from data/act_current.json, `lock` among them; '
           'G-SEALED-AFTER-COMPONENTS exempting a bookkeeping-only commit (the step bank, the hashes bank, the hook’s refusals), b723’s arm '
           'replayed over its commits'),
    ('v', 'Arms and routes reading retired banks or unwritten tool files', 'the templates read a tool’s text through the fold and run it '
          'through tools/standing/fold.py where no tools/<act>_<tool>.py exists, and G-READFIRST-DIFF-BANKED retired in the template: '
          'seventeen such reads in v1.3.0’s templates, none in v1.4.0’s'),
    ('vi', 'The chain phase above 450 s', 'b2a re-cut where b723’s banked first-parent walks halve, (b624-b631) and (b632-b658); b723’s b2a '
           '575 s measured, the two cuts projected under 450 s from b723’s two timings (a fixed cost and a cost per walk), measured at '
           'this act’s suite'),
    ('vii', 'Suite parts run concurrently', 'the suite reads the host’s process table before a part starts and refuses while another part '
            'runs (b723’s event (13) replayed on its table)'),
    ('viii', 'The previous act’s window', 'the record tool’s window over the previous act ends at this act’s anchor -- a carry-time '
             'repair already in the template at v1.3.0, no v1.4.0 edit; its control replays the own-session form against it'),
    ('ix', 'The carry’s act-name substitution', 'tools/standing/carry.py refuses a carried form naming a module tools/ lacks where the '
           'source named one that exists, before it writes (b724’s (d), b723_llm_line, replayed)'),
    ('x', 'A fixed grade sentence before its check', 'tools/standing/repeat.py grade composes the sentence from the check’s result and '
          'refuses an unread check (b721’s (i) replayed)'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v140_foot'])
    L = ['*b723’s events bank (relay data/b723_events.txt) carries eighteen rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank thirty-nine lettered rows, (a)-(z) and (a’)-(m’), each tagged in its own bracket (%s); its '
         'refusal bank fourteen lines at b723’s closing commit %s, each recorded by a letter or an event. Each item is tagged CLAIM, where it '
         'touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the '
         'banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_PREV_CLOSE), '',
         '**The two score readings, ruled** (`(R334)`(1)): where a score’s reader and the suite disagree, the suite’s figure governs and the '
         'score is REFUTED BY THE SUITE, both readings beside it; b723’s two stand as printed, the ruling’s note beneath each. **Dated '
         'notes** (standing clauses v8 row (82): no line rewritten, a note beside each that reads wrong), each dated %s:' % C1_NOTED, '']
    for x in s['notes']:
        L += ['- **%s :%d** (%s; written %s at %s; %s, noted %s): "%s" -- %s.' % (
            x['place'], x['line'], x['where'], x['written'], x['commit'], x['cls'], C1_NOTED, _c1_q(x['quote']), x['fix'])]
    L += ['', '**The repeat classes and the root route (`(R334)`(2)), at tools/standing/ v1.4.0, each with a control replaying the class’s '
          'last banked instance, failing on the route before the repair and passing after, both instances printed** (relay data/%s, %s '
          'cases, AS WANTED %s):' % (C1_V140, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v140_line('### (%s) ' % k_)), '']
    L += ['**The root route** (events (9), (10), (12), (17)): the root names committed blobs alone -- the fold’s templates declare their '
          'untracked writes again (b723’s root named data/b723_bank_hashes.json because the declaration lived only in the record template, '
          'which no act wrote out since v1.3.0), the hashes bank excluded from the set the root names (the lower price: no commit and no '
          'walk), no write after the root recorded in it, and the root’s reading taken again after its own writes; b723’s items replayed at '
          'f585420f read AGREE with the hashes bank excluded, DISAGREE with it named (:%d). b723’s corrigendum row is written in b680’s form '
          '(relay data/act_roots.txt, the row beneath b723’s; data/b724_root_corrigendum.txt); verify over it still reads b723 DISAGREE, '
          'one bank, no committed blob carrying its recorded hash -- put to the author at b724’s root.' % _c1_v140_line('### THE ROOT ROUTE'), '',
          '**b723’s events (1)-(18):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_]).split(': ', 1)[0]
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b723_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b723’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        extra = '; repair (i)' if x in C1_REFUSAL_LETTERS else C1_DF_EXTRA.get(x, '')
        L += ['**(%s)** (relay data/b723_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), extra)]
    L += ['', '**b723’s refusals** (relay data/b723_hook_refusals.txt at %s, one a line): ' % C1_PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (eighteen events, thirty-nine defects), equal to b723’s closing’s (relay '
          'data/b723_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b724 on the author’s ruling `(R334)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 '
          'corrigendum`, the act’s override in relay tools/acts/b724.py) from b723’s events, defects and refusal banks read unedited, the '
          'lines noted read at their repositories’ HEAD, and the v1.4.0 controls bank; banked as relay `data/b724_corrigendum.txt`, the '
          'corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b723’s record; no sealed tool, face, trail or '
          'root-named bank of b723 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b724 -- THE CORRIGENDUM FOR b723, (R334)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b723_events.txt rows (1)-(18), data/b723_defects.txt 39 rows, data/b723_hook_refusals.txt 14 '
             'lines at %s; the noted lines at their repositories` HEAD; data/%s (the v1.4.0 controls); the corrigenda bank`s last row (%d).' % (
                 C1_PREV_CLOSE, C1_V140, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 18, DEFECTS 39 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.4.0: THE TEN REPEAT CLASSES '
               'AND THE ROOT ROUTE ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b723 at its weight after its entry, and the corrigendum for b723, landed through b698's guarded
    landing; dry prints and writes nothing."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        text = _c1_weight()
        land([('FINDINGS.md', C1_WEIGHT_HEAD, NL + text + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B711_ENTRY,
             check=[('FINDINGS.md', K.B711_ENTRY, C1_ENTRY_NEEDLE), ('OPEN_TRAILS.md', K.B711_TRAIL, C1_TRAIL_NEEDLE)], dry=dry)
        return
    if route == 'corrigendum':
        from b652_record import line_of
        s = _c1_state()
        text = NL + C1_CORR_TITLE + NL + NL + NL.join(_c1_lines(s)) + NL
        land([('FINDINGS.md', C1_CORR_TITLE, text)], '%s_corrigendum_landing.json' % ACT, 'corrigendum', entry=None, dry=dry)
        if dry:
            print(NL.join(_c1_bank(s, None)))
            return
        ln = line_of(R.FIND, C1_CORR_TITLE)
        nc, nl_, rep, n = _c1_counts(s)
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=nc, close=nl_, repeat=rep, items=n,
                                                   events=[dict(row=k_, owner=s['tags'][k_][2], tag=s['tags'][k_][0], column=s['tags'][k_][1]) for k_ in sorted(s['events'])],
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.4.0', bank='data/' + C1_V140),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b724, Component 6 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S ONE DISPATCH. The template's three runner
# ### functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b724 ran one ((R334)(5), N1),
# ### rowed in data/b724_lv_rows.json. Replaced for b724 alone; the arms' names stand, their plants on b724's rows.
#⟪OVERRIDE checks 1126 1138⟫
def rebuild_wf_ok(S):
    """(R333)(7), as b723 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
    than SIDE-frobenius carrying build-module.yml on main; SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's with b721's
    two lines (the push trigger to the branch, the target fixed) and nothing else, the hold kept; SIDE-kernel's tip carrying main's
    build-module.yml changed in the four places of b723's kdraft4_clear row (data/b723_axiom_rows.json) and nothing else; no identifier of
    the author and no secret at either tip."""
    import difflib
    st = S['rebuild_state'] or {}
    fr, kn = st.get('SIDE-frobenius') or {}, st.get('SIDE-kernel') or {}
    src = read_blob(EF, 'HEAD:.github/workflows/build-module.yml') or ''
    tip = fr.get('wf_tip') or ''
    d = [x for x in difflib.unified_diff(src.split(NL), tip.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    km = read_blob('D:/SIDE-kernel', 'main:.github/workflows/build-module.yml') or ''
    kt = kn.get('wf_tip') or ''
    kd = [x for x in difflib.unified_diff(km.split(NL), kt.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    row = [r for r in (S['rebuild_rows_b723'] or []) if r.get('kind') == 'kdraft4_clear' and r.get('kernel') == 'SIDE-kernel']
    want = [x for x in (row[-1].get('diff') or []) if x[:1] in '+-' and x[:3] not in ('+++', '---')] if row else None
    return all(v['wf_main'] for k, v in st.items() if k != 'SIDE-frobenius') and fr.get('wf_main') is False \
        and d == ['+  push: { branches: [%s] }' % K.REBUILD_BRANCH, '-      TARGET: ${{ inputs.target }}', '+      TARGET: SIDEFrobenius'] \
        and bool(kt) and bool(want) and kd == want and not any(w in (x or '').lower() for x in (tip, kt) for w in IDENT_WF) \
        and 'hold_mb: "2560"' in tip.lower()
#⟪END⟫
#⟪OVERRIDE checks 1141 1156⟫
def runner_ok(S):
    """(R334)(5), N1, b724: the one dispatch read by its run id -- SIDE-lv-conservation's scratch commit (K.C4_LV, over the deposit pin),
    pushed with its remote equal, dispatched once by K.LV_RUNS's id at that commit, read once: completed success, build exit 0, BUILDS, its
    closure log read, the negation's axioms the standard three without sorryAx, the text as written not elaborating printed beside; the
    bank's foot naming the run, ONE DISPATCH and NO MAIN OR TAG TOUCHED."""
    t, rows = S['rebuild'] or '', S['rebuild_rows'] or []
    cm = [r for r in rows if r.get('kind') == 'commit']
    pu = [r for r in rows if r.get('kind') == 'push']
    dp = [r for r in rows if r.get('kind') == 'dispatch']
    rd_ = [r for r in rows if r.get('kind') == 'read']
    runs = dict(K.LV_RUNS)
    cl = NL.join(rd_[0].get('closure_lines') or []) if rd_ else ''
    neg = "'SIDELvConservation.T3.not_T3_perClass_to_combinations' depends on axioms: [propext, Classical.choice, Quot.sound]"
    return len(cm) == len(pu) == len(dp) == len(rd_) == 1 and cm[0].get('sha') == K.C4_LV == pu[0].get('sha') == dp[0].get('sha') \
        and cm[0].get('parent') == K.LV_V0100 and pu[0].get('remote_equal') is True \
        and str(dp[0].get('run')) == str(rd_[0].get('run')) == str(runs.get('SIDE-lv-conservation')) \
        and rd_[0].get('status') == 'completed' and rd_[0].get('conclusion') == 'success' and str(rd_[0].get('build_exit')) == '0' \
        and rd_[0].get('verdict') == 'BUILDS' and rd_[0].get('closure_read') is True and neg in cl \
        and 'Application type mismatch' in cl and '¬T3_perClass_to_combinations' in cl \
        and ('RUN %s' % runs.get('SIDE-lv-conservation')) in _verdict(t) and 'ONE DISPATCH ; NO MAIN OR TAG TOUCHED' in _verdict(t)
#⟪END⟫
#⟪OVERRIDE checks 1167 1167⟫
    for k, _r in K.LV_RUNS:
#⟪END⟫
#⟪OVERRIDE checks 1173 1173⟫
    return bool(mem) and all(int(r.get('free_mb') or 0) >= K.HOLD for r in mem) and order \
#⟪END⟫
# ### b724, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b723's record has eighteen
#⟪OVERRIDE checks 980 980⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 19)) \
#⟪END⟫
# ### b724, Component 6 (the Edit tool): (R334)(10) -- no registration commit (REG_COMMIT None), its files read as none, not by git
#⟪OVERRIDE checks 526 526⟫
                   reg=files_of(ROOT, K.REG_COMMIT) if K.REG_COMMIT else [], actcur=files_of(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
# ### b724, Component 6 (the Edit tool): b724's step-zero bank landed in the step-zero commit after the banks' (d5432f23, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (21681ef9); the arm reads it there
#⟪OVERRIDE checks 751 751⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b724_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b724, Component 6 (the Edit tool): (R334)(8) names the branches "the push-b723-preroot, -record and -closing branches"; allow.py's reader
# ### takes the full names alone, so the abbreviated pair read outside; the ferry's text given to it with each short form written out
#⟪OVERRIDE checks 763 763⟫
    rd_ = STW.deletes_read([('-', b) for b in got], re.sub(r'\b(push-b\d{3})-(\w+), -(\w+) and -(\w+)', r'\1-\2, \1-\3 and \1-\4', S['ferry']),
                           STW.words_of(ACTN))
#⟪END⟫
# ### b724, Component 6 (the Edit tool): b724's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b723's wording
#⟪OVERRIDE checks 776 776⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b724, Component 6 (the Edit tool): v1.4.0 edited tools/standing/hook.py for classes (i)-(ii) ((R334)(2)); the arm read it unedited
# ### since the act's base -- now its blob at HEAD, at v1.4.0's commit and in the working tree the same, edited by that commit alone
#⟪OVERRIDE checks 1516 1516⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) == cr0(blob(ROOT, 'HEAD:tools/standing/hook.py')) \
        and gs(ROOT, 'log', '--format=%H', '%s..HEAD' % PRE['relay'], '--', 'tools/standing/hook.py').split() == [K.C1_STANDING] \
#⟪END⟫
#⟪OVERRIDE checks 1659 1659⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, edited this act by v1.4.0`s commit 69386258 alone (classes (i)-(ii)); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b724, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 985 985⟫
        and 'data/b724_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b724, Component 6 (the Edit tool): (R334)(5) enters one ERRATA entry -- the template's arm wanted none; the arm now reads ERRATA.md
# ### appended at C4_PP alone (the base's text its head, the id once and only in the added text, ERRATA the one file there), no differs bank
#⟪OVERRIDE checks 1476 1482⟫
def differs_errata_ok(S):
    """(R334)(5): one ERRATA entry this act and no DIFFERS entry -- ERRATA.md the base's text with ERRATA_ID's entry appended, its heading
    once and only in the added text, ERRATA the one file of Component 4's PLACE-papers commit; no b724 differs or errata bank; the weight
    line and the corrigendum at FINDINGS in Component 1's PLACE-papers commit, FINDINGS the one file there."""
    now, pre = _s(S['errata_pp_now']), _s(S['errata_pp_pre'])
    add = now[len(pre):] if pre and now.startswith(pre) else ''
    return bool(add.strip()) and K.ERRATA_IDS == (K.ERRATA_ID,) and pre.count(K.ERRATA_ID) == 0 and add.count('## %s ' % K.ERRATA_ID) == 1 \
        and not S['differs'] and not S['errata'] and K.DIFFERS_LINE is None and S['files']['c4pp'] == ['ERRATA.md'] \
        and S['files']['c1pp'] == ['FINDINGS.md'] and 'weight' in fline(S, K.WEIGHT_LINE).lower()
#⟪END⟫
# ### b724, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b723's step-zero wording; b724's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 742 742⟫
        and 'port-b707' in z and 'Kept: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b724, Component 6 (the Edit tool): G-RUNNER-READ's plant named b723's axiom head, which b724's lv bank does not carry (the plant
# ### a no-op); the plant now the read's closure log carrying sorryAx at the negation
#⟪OVERRIDE checks 1686 1686⟫
     lambda S: runner_ok(S), lambda S: put(S, 'rebuild_rows', [dict(r, closure_lines=[x.replace('[propext, Classical.choice, Quot.sound]', '[propext, sorryAx, Classical.choice, Quot.sound]') for x in (r.get('closure_lines') or [])]) for r in (S['rebuild_rows'] or [])])),
#⟪END⟫
# ### b724, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b724, Component 6 (the Edit tool): the fold bank was b723's own route
# ### (tools/b723_fold.py); b724's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b724_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1005 1005 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b723.py -> tools/acts/b724.py' in (rd('b724_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b724, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b724_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 256 263 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b724_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b724, Component 7 (the Edit tool): the closing's counter line with the repeat count beside it (Component 7 of (R334): "the counter
# ### line CLAIM n, CLOSE m, the repeat count beside it"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 339 340⟫
    rows = [l for n_ in ('b724_defects.txt', 'b724_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R334)(2), the act`s events and defects together; relay data/b724_defects.txt, data/b724_events.txt): CLAIM %d, CLOSE %d ; REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b724, Component 6 (the Edit tool): the carried item (b) named b723's orders by hand; (R334)(4)'s triage counts from the worklist
# ### (G-OFFSET-POST-HOC ties them to the bank's foot), the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: %d triaged by the generator`s table at HEAD (relay data/b724_orders_triage.txt :531) -- DONE %d, TRIGGER NOT MET %d, TRIGGER MET %d, AUTHOR`S WORD %d; the trail`s' % WL.ORDERS,
    '        open-orders line written from tools/standing/orders.py`s output, none carried by hand; beside them',
#⟪END⟫
# ### b724, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b723's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b724_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b724_registration_%s.txt' % __import__('b724_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b724, Component 6 (the Edit tool): b723's row measured (R333)(3)(ii)'s closing lines landed before the seal; b724 lands none before
# ### the seal -- the DONE orders' dated closing lines ride in the trail at the close
#⟪OVERRIDE regspec 78 78⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 0, 0, 'lines', '### none: (R334)(4)`s DONE orders` dated closing lines written with the trail at the close; OPEN_TRAILS untouched before the seal.'),
#⟪END⟫
# ### b724, Component 6 (the Edit tool): N1's dispatch command is the seat's lv route `lv724.py dispatch` ((R334)(5)); the carried
# ### pattern named b723's axiom tool, which b724 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)'
                          r'|(^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*lv724\.py dispatch\b', re.M)
#⟪END⟫
# ### b724, Component 6 (the Edit tool): G-SCORER-READS-BANKS's needles named b723's banks (the axiom rows, H-SUPPORT's rule, the closed
# ### form's check), which no b724 scorer reads; the needles set to the banks b724's N1-N4 read (the command bank and the lv rows, v1.4.0's
# ### controls, the split's price, the seal and step banks), the ledger exclusion unchanged; the lv rows' needle is the read's own form
#⟪OVERRIDE checks 903 904 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_lv_rows.json' % ACT" in n and '_standing_v140.txt' in n and '_split_price.txt' in n \
        and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b724, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b723's ruling's form "port-b707 kept;", where (R334)(9)
# ### writes "kept: port-b707, …" (data/b724_ferry.txt :34), so the arm failed on the act's real deletes; both forms read as written
#⟪OVERRIDE checks 764 767 REPAIR (needle)⟫
    # ### (R333)(9) wrote "port-b707 kept;" and (R334)(9) writes "kept: port-b707, …"; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or bool(re.search(r'\bkept: [^.;]*\b%s\b' % re.escape(K.PORT_BRANCH), S['ferry']))) \
#⟪END⟫
# ### b724, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH's plant replaced "the push-b723-* branches", where (R334)(9) writes "the push-b723*
# ### branches", so the plant changed nothing; set to the ruling's own words
#⟪OVERRIDE checks 1621 1621 REPAIR (plant)⟫
     lambda S: deletes_one_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace('the push-b723* branches of relay and PLACE-papers deleted by name', 'the push-b723* branches of relay and PLACE-papers kept by name'))),
#⟪END⟫
# ### b724, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b724_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmno'))   # ### (a)-(o) entered before the lock, every one the seat's (data/b724_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b724_price.txt', 'data/b724_corrigendum.txt', 'data/b724_standing_v140.txt', 'data/b724_tool_repairs.txt',
                  'data/b724_root_corrigendum.txt', 'data/b724_hook_control.txt', 'data/b724_split_price.txt', 'data/b724_orders_triage.txt',
                  'data/b724_lv.txt', 'data/b724_lv_rows.json', 'data/b724_release_list.txt', 'data/b724_legacy.txt',
                  'data/b724_reproduce.txt', 'data/b724_reproduce.json', 'data/b724_address_scan.txt', 'data/b724_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b724 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R334)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b724_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R334)(2)-(6), Component 6, the Edit tool, before the lock (b723's keys over b723's objects in git at b723's suite): no
        # ### registration this act ((R334)(10)); the components' order by ancestry; the price table and v1.4.0's controls (2); the root
        # ### corrigendum; the split's price (3); the triage (4); the lv negation, its rows and the release list (5); the legacy carry (6); v8
        # ### and v9; the address scan (R332)(9); the reproduction run under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### (R334)(10): no registration commit, no registrations bank at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v140', K.STANDING_COMMIT, K.C1_STANDING), ('v140_c1', K.C1_STANDING, K.C1_RELAY),
                                 ('c1_corr', K.C1_RELAY, K.C1_CORR), ('corr_c2', K.C1_CORR, K.C2_RELAY), ('c2_c3', K.C2_RELAY, K.C3_RELAY),
                                 ('c3_c4', K.C3_RELAY, K.C4_RELAY), ('c4_c5', K.C4_RELAY, K.C5_RELAY))),
        anc_pp=subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', K.C1_PP, K.C4_PP]).returncode == 0,
        registrations=rd('b724_registrations.txt'), price=rd('b724_price.txt'), v140=rd('b724_standing_v140.txt'),
        root_corr=rd('b724_root_corrigendum.txt'), triage=rd('b724_orders_triage.txt'), lv=rd('b724_lv.txt'),
        release=rd('b724_release_list.txt'), legacy=rd('b724_legacy.txt'),
        legacy_now=cr0(raw(os.path.join(T, 'standing', 'legacy.py'))), legacy_pre=cr0(blob(ROOT, '%s:tools/standing/legacy.py' % PRE['relay'])),
        routes_dir=os.path.exists(os.path.join(T, 'standing', 'routes')),
        reproduce=rd('b724_reproduce.txt'), reproducej=jl('b724_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b724_address_scan.txt'), addr_live=_addr_live(), split=rd('b724_split_price.txt'),
        # ### the standing runner arms read THIS ACT'S one dispatch ((R334)(5), N1): the lv bank, its rows; the wave 1 kernels' rebuild-b721
        # ### branches, main and tags as b723 left them (its axiom rows read for the workflows there, no kernel commit this act)
        rebuild=rd('b724_lv.txt'), rebuild_rows=json.loads(rd('b724_lv_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),
        lv_scratch=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.LV_SCRATCH_BRANCH),
        lv_scratch_remote=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + K.LV_SCRATCH_BRANCH),
        lv_scratch_parent=gs(LV, 'rev-parse', '--verify', '--quiet', K.C4_LV + '^'),
        lv_scratch_files=[x for x in gs(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.C4_LV).split(NL) if x.strip()],
        lv_scratch_on_main=subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', K.C4_LV, 'main']).returncode == 0,
        lv_scratch_tags=[t for t in gs(LV, 'tag', '--points-at', K.C4_LV).split(NL) if t.strip()],
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               c2=_ct(ROOT, K.C2_RELAY), c3=_ct(ROOT, K.C3_RELAY), c4=_ct(ROOT, K.C4_RELAY), c4pp=_ct(PP, K.C4_PP), c5=_ct(ROOT, K.C5_RELAY),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.C2_RELAY),
                   c3=files_of(ROOT, K.C3_RELAY), c4=files_of(ROOT, K.C4_RELAY), c4pp=files_of(PP, K.C4_PP), c5=files_of(ROOT, K.C5_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b724's read-first bank's items by path, as its step zero wrote them (Component 6, the Edit tool, before the lock: the carried needles
# ### were b723's items)
READFIRST_NEEDLES = ('relay data/b723_closing.txt |', 'relay data/b723_events.txt |', 'relay data/b723_defects.txt |',
                     'relay data/b722_defects.txt |', 'relay data/b721_defects.txt |', 'relay data/b723_split_price.txt |',
                     'relay data/b723_orders.txt |', 'relay data/b723_orders_twenty.txt |', 'PLACE-papers OPEN_TRAILS.md | :14680 |',
                     'relay data/b723_axiom.txt |', 'relay tools/act_root.py |', 'relay tools/standing/VERSION | :1 v1.3.0 |',
                     'relay tools/standing/legacy.py |', 'relay data/b724_ferry.txt |', 'relay data/standing_clauses_v9.txt |',
                     'relay data/b723_author_words.txt | whole |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R334)(1)-(2))', 'LEDGER SPLIT ((R334)(3))', 'OPEN ORDERS ((R334)(4))',
                    'lv NEGATION ((R334)(5))', 'LEGACY IMPORTS ((R334)(6))', 'NAME AND ADDRESS ((R332)(9))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (57 = 56 + 1: the one miss, ruling (8)'s "committed alone" of
    b723's step row 54, which rode with b723's hashes bank -- data/b724_citation_check.txt :37, entered by the fact clause as defect (b)); the
    bank written before the step-zero banks' commit and that commit before Component 1's (Component 6, the Edit tool: the carried 60 = 60 + 0
    were b723's own)."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 1 and int(m.group(1)) == 57 and 'MISS | ruling (8) | data/b723_steps.json committed alone' in c \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 6, the Edit tool, before the lock: the carried needles were b722's figures under b723's name)
    return landed(S, 0, ['b723 AT ITS WEIGHT', 'suite 108 of 116; root 9296406733ce0d44…', 'the closing’s b8334f17', '39 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### Component 6, before the lock, the Edit tool: b724's title in the ferry's Component 6 form adjusted to what the act did (the record
# ### tool's _title over the banks), cut at its objects; the carried needles were b723's
TITLE_NEEDLES = ('## 9 of 10 repeat classes repaired with controls', ', the tenth controlled where b723’s carry repaired it',
                 '; the root route repaired, b723’s row written', '; the ledger split carried at its price',
                 '; 142 open orders triaged: 60 done, 42 trigger not met, 12 acted or priced, 28 for the author’s word',
                 '; the lv negation compiled, the erratum entered', '; the legacy imports carried')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R334)(1)-(2): the generated entry for b723's eighteen events and thirty-nine defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(18), the defects by the one lettering ((a)-(z), (a`)-(m`)), no memory item; every item tagged
    CLAIM or CLOSE and NEW or REPEAT, the tags summing (CLAIM 7, CLOSE 50 over 57, REPEAT 37); the CLAIM items events (8), (9), (10), (17)
    and defects (q), (a`), (c`); the repairs at tools/standing/ v1.4.0 by their controls bank; the two score readings REFUTED BY THE SUITE
    among the dated notes; the corrigenda bank appended at row (44) and nothing before it changed; in Component 1's commits (Component 6,
    the Edit tool, before the lock: the carried figures were b723's corrigendum's, of b722's record)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 39 and len(items) == j.get('items') == 57 and j.get('row') == 44 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 57 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 7 and claims == ["a'", "c'", 'e10', 'e17', 'e8', 'e9', 'q'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 37 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.4.0' and (j.get('repairs') or {}).get('bank') == 'data/b724_standing_v140.txt' \
        and sorted(n.get('where') for n in (j.get('notes') or []) if n.get('cls') == 'REFUTED BY THE SUITE') == ['the closing’s N4', 'the closing’s S2'] \
        and '  (44) ' in S['corrigenda'] and '  (45) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b724_rules.txt and data/b725_rules.txt, by form in (R334)(8)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (Component 6, the Edit tool: the line above is b723's, carried); no author's word of b724 orders a row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b724_rules.txt')) and not os.path.exists(os.path.join(D, 'b725_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b724's keys, the report sections' own heads (Component 6, the Edit tool, before the lock; b723's carried till then)
REPORT_KEYS = ('KERNEL -- THE lv NEGATION ON A SCRATCH BRANCH', 'CERTIFIED -- tools/standing/ v1.4.0', 'REGISTERED -- THE OPEN ORDERS TRIAGED',
               'REGISTERED -- b723`S CORRIGENDUM ROW', 'HELD -- THE LEDGER SPLIT', 'HELD -- THE LEGACY IMPORTS',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over THIS ACT'S one dispatch ((R334)(5), data/b724_lv_rows.json; Component 6, the Edit tool): every push, dispatch and read
    row with the host's free memory at or above the hold (each figure read as an integer); for SIDE-lv-conservation (K.LV_RUNS, the one) its
    push before its run and its run before its read; the dispatches one, the one N1 allows, none push-triggered; the capture running the
    seat's lv route (its commit, push, dispatch and read), no earlier act's rebuild or axiom tool at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*lv724\.py (commit|push|dispatch|read)\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b72[1-4]_(?:rebuild|axiom)\.py (push|dispatch|push_run|plan|kcommit|commit)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == len(K.LV_RUNS) == K.MAX_DISPATCHES == 1 \
        and not [r for r in rows if r.get('kind') == 'dispatch' and r.get('via')] \
        and bool(S['cmds']) and bool(cmds) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS, OPEN_TRAILS and (R334)(5)'s ERRATA; no archive file written,
    (3) carried), both ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b724's headings and banks, as its _finding_text writes them (Component 6, the Edit tool, before the lock; b723's carried till then)
ENTRY_NEEDLES = ('**The corrigendum and the repeat classes**', '**The root route**', '**The ledger split**', '**The open orders triaged**',
                 '**The lv negation**', '**The legacy imports**', '**The research instruments reproduced**', '**The author’s name and address**',
                 '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**', '**Read in mutual light**',
                 '**Carried to:**', '**Next.**',
                 'data/b724_corrigendum.txt', 'data/b724_standing_v140.txt', 'data/b724_root_corrigendum.txt', 'data/b724_split_price.txt',
                 'data/b724_orders_triage.txt', 'data/b724_lv.txt', 'data/b724_release_list.txt', 'data/b724_legacy.txt',
                 'data/b724_reproduce.txt', 'data/b724_address_scan.txt', 'data/b724_touch.txt', 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b724: no row of the defects bank the navigator's ((a)-(o) the seat's)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R334)(10), the name the frozen run list carries (Component 6, the Edit tool, over b724's objects): b724 registers no hypothesis --
    no registration commit (REG_COMMIT None), no data/b724_registrations.txt at HEAD or in the working tree; the components committed in
    their order, each the ancestor of the next (v9, v1.4.0, its controls, the corrigendum, (3), (4), (5), (6)) and Component 1's FINDINGS
    commit an ancestor of (5)'s ERRATA commit; the earlier acts' registrations at HEAD their blobs at their commits."""
    return K.REG_COMMIT is None and S['reg_now'] == (None, None) and not S['registrations'] \
        and all(S['anc'].get(k) is True for k in ('v9_v140', 'v140_c1', 'c1_corr', 'corr_c2', 'c2_c3', 'c3_c4', 'c4_c5')) \
        and S['anc_pp'] is True and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R332)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 6, the Edit tool): tools/b724_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address and name read from history and held in memory -- the address 0, the author's name 0, the previous name 0, its
    four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R334)(3), N3 (the name the frozen run list carries; Component 6, the Edit tool, over b724's split): the ledger split CARRIED WHOLE
    to b725 with its price, NOTHING CUT, the split bank's last line; the price table's choice "(3) CARRIED WHOLE WITH ITS PRICE"; the split
    bank in Component 2's commit (C2_RELAY), nothing of (3) at PLACE-papers (C2_PP None) and no archive file in the act's PLACE-papers
    write list."""
    last = lambda t: ((t or '').rstrip(NL).split(NL) or [''])[-1]
    sp, pr = last(S['split']), last(S['price'])
    return sp.startswith('### ### **THE LEDGER SPLIT: CARRIED WHOLE TO b725 WITH ITS PRICE -- ') and sp.endswith(' ; NOTHING CUT.**') \
        and '(3) CARRIED WHOLE WITH ITS PRICE, (2) AND (4)-(6) RUN.**' in pr and 'data/b724_split_price.txt' in S['files']['c2'] \
        and K.C2_PP is None and not any('archive' in p for p in K.PP_WRITTEN + K.PP_EDITED)
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R334)(5), N5 (the name the frozen run list carries; Component 6, the Edit tool, over b724's lv negation): the negation compiled on
    its scratch branch alone -- scratch-b724 at C4_LV locally and at origin, its parent the deposit pin LV_V0100, its one file
    CircuitClosure.lean, not on main and no tag at it; the bank's last line naming the theorem, the run, the axioms and NO sorryAx, and the
    text as written graded as not elaborating; the release sitting's list one item added, nothing sent; the lv bank, its rows and the list
    in Component 4's relay commit (C4_RELAY)."""
    last = lambda t: ((t or '').rstrip(NL).split(NL) or [''])[-1]
    lv, rl = last(S['lv']), last(S['release'])
    return S['lv_scratch'] == K.C4_LV and S['lv_scratch_remote'] == K.C4_LV and S['lv_scratch_parent'] == K.LV_V0100 \
        and S['lv_scratch_files'] == ['CircuitClosure.lean'] and S['lv_scratch_on_main'] is False and S['lv_scratch_tags'] == [] \
        and lv.startswith('### ### **THE lv NEGATION: not_T3_perClass_to_combinations COMPILES ON scratch-b724 (%s), RUN %d, ' % (K.C4_LV[:8], K.C4_RUN)) \
        and 'AXIOMS [propext, Classical.choice, Quot.sound], NO sorryAx ; THE TEXT AS WRITTEN DOES NOT ELABORATE' in lv \
        and rl == '### ### **THE RELEASE SITTING`S LIST: ONE ITEM ADDED (THE lv DESCRIPTION`S "ZERO SORRY") ; THE DEPOSIT NOT EDITED ; NOTHING SENT.**' \
        and _own(S['files']['c4']) == ['data/b724_lv.txt', 'data/b724_lv_rows.json', 'data/b724_release_list.txt']
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R334)(4), the name the frozen run list carries (Component 6, the Edit tool, over b724's triage): the open orders triaged, each
    once, under the section of its grade -- the rows' counts per grade the sections' heads, the worklist's ORDERS and the foot's, summing
    to 142; TRIGGER MET acted 0 and priced 12; the AUTHOR'S WORD table one row per AUTHOR'S WORD order, its recommendations counted
    RETIRE 19, KEEP 2, RE-SCOPE 7 by its rows and its foot; the citations 321 of 321; the bank alone in Component 3's commit (C3_RELAY),
    nothing at PLACE-papers before the trail (C3_PP None)."""
    o = S['triage'] or ''
    G = ('DONE', 'TRIGGER NOT MET', 'TRIGGER MET', "AUTHOR'S WORD")
    rows = re.findall(r"(?m)^  (W-ORD-[\w-]+) -- (DONE|TRIGGER NOT MET|TRIGGER MET|AUTHOR'S WORD) \(entry ", o)
    heads = [int(re.search(r'(?m)^## %s \((\d+)\)$' % re.escape(g), o).group(1)) if re.search(r'(?m)^## %s \((\d+)\)$' % re.escape(g), o) else -1 for g in G]
    cnt = [sum(1 for r in rows if r[1] == g) for g in G]
    tab = re.findall(r'(?m)^  (W-ORD-[\w-]+)\s+(RETIRE|KEEP|RE-SCOPE)\s{2,}\S', o)
    rec = [sum(1 for t in tab if t[1] == g) for g in ('RETIRE', 'KEEP', 'RE-SCOPE')]
    foot = '### ### **THE OPEN ORDERS: %d TRIAGED -- DONE %d ; TRIGGER NOT MET %d ; TRIGGER MET %d (ACTED 0, PRICED AND NAMED %d) ; ' \
           "AUTHOR'S WORD %d (RETIRE %d, KEEP %d, RE-SCOPE %d) ; CITATIONS 321 OF 321 ON THEIR LINES.**" % ((len(rows),) + tuple(cnt[:3]) + (cnt[2], cnt[3]) + tuple(rec))
    return len(rows) == len(set(r[0] for r in rows)) == 142 == K.ORDERS[0] and cnt == heads == list(K.ORDERS[1:]) \
        and sorted(t[0] for t in tab) == sorted(r[0] for r in rows if r[1] == "AUTHOR'S WORD") and rec == [19, 2, 7] \
        and '  RETIRE 19 ; KEEP 2 ; RE-SCOPE 7' in o and ((o.rstrip(NL).split(NL) or [''])[-1]) == foot \
        and _own(S['files']['c3']) == [K.TRIAGE] and K.C3_PP is None
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries (Component 6, the Edit tool, over b724's v9): standing clauses v9 binding the act whole as b723
    landed it -- the working tree's text its blob at STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's
    base; no v10 written; v9's commit an ancestor of v1.4.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v140') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED as b723
    left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since b723's v1.3.0;
    this suite's run list 116 arms, no standing arm added (Component 6, the Edit tool)."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R334)(6), the name the frozen run list carries (Component 6, the Edit tool, over b724's legacy carry): the legacy imports carried
    with the remaining price, NOTHING COPIED -- the bank's last line; tools/standing/legacy.py byte-equal to its blob at the act's base, no
    tools/standing/routes/ written; the bank alone in Component 5's commit (C5_RELAY)."""
    lg = (S['legacy'] or '').rstrip(NL).split(NL)[-1]
    return lg.startswith('### ### **THE LEGACY IMPORTS: CARRIED WITH THE REMAINING PRICE (') and lg.endswith(' ; NOTHING COPIED, legacy.py UNCHANGED (192 NAMES).**') \
        and bool(S['legacy_now']) and S['legacy_now'] == S['legacy_pre'] and S['routes_dir'] is False \
        and _own(S['files']['c5']) == ['data/b724_legacy.txt']


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b723's (R333)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at the act's base (unchanged this act; Component 6, the Edit
    tool: the carried read named b723's commit of it) and the working tree's."""
    j = S['reproducej'] or {}
    R = j.get('rows') or []
    ids = ['I-%d' % i for i in range(41, 109)]
    run = [r for r in R if r.get('grade') in ('REPRODUCES', 'DIFFERS')]
    nr = [r for r in R if r.get('grade') == 'NOT RUN']
    c = dict((g, sum(1 for r in R if r.get('grade') == g)) for g in ('REPRODUCES', 'DIFFERS', 'NOT RUN'))
    f = re.search(r'ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;', _verdict(S['reproduce']))
    tool = 'tools/research/reproduce.py'
    src = _s(blob(ROOT, 'HEAD:' + tool))
    return bool(R) and [r.get('id') for r in R] == ids and len(run) + len(nr) == len(R) \
        and all(str(r.get('planted_as_wanted')) == 'True' and r.get('planted_grade') == 'DIFFERS' for r in run) \
        and all(re.match(r'(MORE THAN 60 s|A DISPATCH|A NETWORK READ): ', r.get('why') or '') and 'priced' in (r.get('why') or '') for r in nr) \
        and j.get('counts') == c and bool(f) and [int(x) for x in f.groups()] == [len(R), c['REPRODUCES'], c['DIFFERS'], c['NOT RUN'], len(run), len(run)] \
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (PRE['relay'], tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')
#⟪END⟫
#⟪SECTION checks 41⟫
    """standing clauses v9 (Component 7 of (R334): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b724_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b723's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R334-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b723's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R334) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from b8334f17',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b723's standing arm, carried in the run list of 116 (Component 6, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R333)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from b8334f17',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 57 = 56 OK + 1 miss (ruling (8)`s "committed alone" of b723`s step row, defect (b)), the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b723-closing (b8334f17)', 'push-b723-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (nine repeat classes repaired with controls, the tenth controlled; the root route repaired and b723`s row written; the ledger split carried at its price; 142 open orders triaged; the lv negation compiled and the erratum entered; the legacy imports carried), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R334)(1)-(2): the generated corrigendum for b723`s record, landed at FINDINGS :11536: its eighteen events and thirty-nine defects, 57 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 7 CLOSE 50, REPEAT 37; S2 and N4 REFUTED BY THE SUITE among the notes; v1.4.0`s repairs by data/b724_standing_v140.txt; the corrigenda bank appended at row (44)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b724 and no b725 rules bank: no author`s word of b724 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b724's objects (Component 6, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R334)(10): no registration this act -- no registration commit, no data/b724_registrations.txt; the components in their order, each commit the ancestor of the next (d9739558, 69386258, e5f9f7a5, a5a71442, b34fb50e, 688c9e99, bb304a67, 01dd9f44), 88f234ed before c3c6ba86 at PLACE-papers; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: put(S, 'registrations', '### a planted registrations bank')),
    ('G-PREDICTION-FIRST', '(R332)(9)(i), N5, the scan arm: tools/b724_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, the bank`s counts the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R334)(3), N3: the ledger split carried whole to b725 with its price, nothing cut (data/b724_split_price.txt`s last line), the price table`s choice; the bank in b34fb50e; nothing of (3) at PLACE-papers and no archive file in the act`s write list',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'split', (S['split'] or '').replace('NOTHING CUT.', 'ONE FILE CUT.'))),
    ('G-DERIVATION-GRADED', '(R334)(5), N5: the lv negation compiled on scratch-b724 alone -- the branch at c9cd1ea9 locally and at origin over the deposit pin 93c27ec2, its one file CircuitClosure.lean, off main and untagged; the bank`s last line (run 40964150574, the axioms, NO sorryAx, the text as written not elaborating); the release list one item, nothing sent; the three banks in bb304a67',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'lv_scratch_tags', ['v0.15.0'])),
    ('G-OFFSET-POST-HOC', '(R334)(4): the 142 open orders triaged, each once under its grade -- DONE 60, TRIGGER NOT MET 42, TRIGGER MET 12 (acted 0, priced 12), AUTHOR`S WORD 28, the rows` counts the heads`, the worklist`s and the foot`s; the author`s word table one row per such order, RETIRE 19, KEEP 2, RE-SCOPE 7; citations 321 of 321; the bank alone in 688c9e99',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'triage', (S['triage'] or '').replace('  W-ORD-SEAT                               RETIRE ', '  W-ORD-SEAT                               KEEP   '))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at b8334f17, VERSION 9; v8 at HEAD its blob at b8334f17; no v10; v9`s commit an ancestor of v1.4.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- the file byte-equal at b8334f17, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R334)(6): the legacy imports carried with the remaining price, nothing copied (data/b724_legacy.txt`s last line); tools/standing/legacy.py byte-equal at b8334f17, no tools/standing/routes/; the bank alone in 01dd9f44',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'legacy', (S['legacy'] or '').replace('NOTHING COPIED', 'ONE FILE COPIED'))),
    ('G-DIFFERS-ERRATA', '(R334)(5): one ERRATA entry and no DIFFERS entry -- ERRATA.md the text at 698fe441 with E-2026-10-29-1 appended, its heading once and in the added text alone, ERRATA the one file of c3c6ba86; no b724 differs or errata bank; the weight line and the corrigendum in 88f234ed, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b724_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R334-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b723`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at b8334f17 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R334)(5): the lv negation`s one run, 40964150574, read once by its id -- completed, success, build exit 0, BUILDS, the closure read: the negation`s axioms [propext, Classical.choice, Quot.sound] and no sorryAx, the text as written not elaborating; the commit c9cd1ea9 over 93c27ec2, pushed equal to its remote; the bank`s foot ONE DISPATCH, NO MAIN OR TAG TOUCHED',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: the lv dispatch`s order and hold -- free memory at or above 2,560 MB at the push, the dispatch and the read; commit before push before dispatch before read; one dispatch, by the seat`s lv724.py route alone, none by push; no b721-b723 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b723 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s three (ERRATA for (R334)(5), FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b723`s trail record on OPEN_TRAILS (:16366) and its root in the chain', lambda S: '### b723 — lane two, act one hundred and fifty, the checkpoint act under (R333)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (ERRATA, FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b723`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: (R334)(5)`s one by lv724.py, read by its id in data/b724_lv.txt; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b724: (R334)'s rows, b723's (R333) rows pruned. The quote read from the bank (data/b724_ferry.txt :7)
    hq = _quote(rd(p('data', 'b724_ferry.txt')) or '', '"b723 closed: relay 14bf5ec5', '". Its rows')
    add('ruling (1)', 'data/b723_closing.txt :1, the head line as the ruling quotes it (data/b724_ferry.txt :7)', bool(hq) and hq[1:] == at(cl, 1),
        at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', 'b8334f17', 'data/b723_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'the head line as the public relay carries it at b8334f17, its main', bool(pub) and pub[0] == at(cl, 1) and rm.startswith('b8334f17'),
        'remote main %s' % rm[:8], '1')
    add('ruling (1)', 'data/b723_closing.txt :5, the counter CLAIM 7, CLOSE 50, REPEAT 37 of 57',
        bool(re.search(r'CLAIM 7, CLOSE 50 ; REPEAT 37 OF 57$', at(cl, 5))), at(cl, 5)[-40:], '1')
    for f_ in ('b723_zetak.txt', 'b723_support.txt', 'b723_c2_closed_form.txt', 'b723_c2_check.txt', 'b723_axiom.txt', 'b723_orders.txt',
               'b723_split_price.txt'):
        add('ruling (1)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '1')
    add('ruling (1)', 'OPEN_TRAILS :16418, W-ORD-STATUS-CELLS RETIRED, the open orders 143 before and 142 after',
        at(ot, 16418).startswith('**`W-ORD-STATUS-CELLS` RETIRED 2026-10-29, b723,**') and 'Open orders 143 before this line, 142 after' in at(ot, 16418),
        at(ot, 16418)[:60], '3')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), (2)', 'events (1)-(18) and 39 defects (data/b723_events.txt, data/b723_defects.txt; the head line`s "39 defects")',
        starts == list(range(1, 19)) and len(letters) == 39, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((48, 9, 'CLAIM'), (64, 12, 'CLOSE'), (68, 13, 'CLOSE'), (82, 16, 'CLOSE')):
        add('ferry (read first)', 'event (%d) at data/b723_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:40],
            at(ev, n_)[:50], '0')
    add('ferry (read first)', 'data/b723_closing.txt :437, the carried items', at(cl, 437) == '### CARRIED FORWARD.', at(cl, 437)[:30], '0')
    for f_ in ('b721_defects.txt', 'b722_defects.txt', 'b723_orders_twenty.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    add('ferry (read first)', 'OPEN_TRAILS :16366, b723`s trail head, and the three lines beneath it',
        at(ot, 16366).startswith('### b723 — lane two, act one hundred and fifty, the checkpoint act under (R333)') and bool(at(ot, 16368)) and bool(at(ot, 16369 + 1)),
        at(ot, 16366)[:60], '0')
    add('ferry (read first)', 'data/b723_axiom.txt :99, the lv row', at(lines_of(p('data', 'b723_axiom.txt')), 99).startswith('  SIDE-lv-conservation  v0.10.0 = 93c27ec'),
        at(lines_of(p('data', 'b723_axiom.txt')), 99)[:50], '0')
    add('ferry (read first)', 'tools/act_root.py', os.path.exists(p('tools', 'act_root.py')), 'present', '1')
    lg = (rd(p('tools', 'standing', 'legacy.py')) or '')
    add('ferry (read first), ruling (6)', 'the exception file tools/standing/legacy.py, its NAMES not empty', lg.count("    'b") > 0, '%d names' % lg.count("    'b"), '5')
    # ### (R334)(2): the repeat classes and the root route
    add('ferry', 'tools/standing/ at v1.3.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.3.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ruling (2), ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R334)(2)'s root route: its control replays b723's banks at f585420f (the root banks' commit)
    add('ruling (2)', 'f585420f, the commit b723`s root banks rode in (the root route`s control replays b723`s banks there)',
        gr('D:/relay', 'cat-file', '-t', 'f585420f') == 'commit', gr('D:/relay', 'log', '--format=%s', '-1', 'f585420f')[:60], '1')
    # ### (R334)(3): the ledger split
    add('ruling (3)', 'OPEN_TRAILS :14680, W-ORD-LEDGER-SPLIT-RESOLVER and the cut FINDINGS :456-:6949', 'W-ORD-LEDGER-SPLIT-RESOLVER' in at(ot, 14680) and ':456-:6949' in at(ot, 14680),
        at(ot, 14680)[:60], '2')
    sp_ = lines_of(p('data', 'b723_split_price.txt'))
    add('ruling (3)(ii)', 'data/b723_split_price.txt :24, the 528 live-tool citation sites', 'in live tools MOVED 528 ;' in at(sp_, 24), at(sp_, 24)[:70], '2')
    # ### (R334)(5): the lv statements at SIDE-lv-conservation's main
    for n_ in ('T3_perClass_to_combinations', 'T3doubleprime_general_commutation_fails'):
        fs_ = _decl_files(K.LV_DIR, 'main', n_)
        add('ruling (5)', '%s declared at SIDE-lv-conservation main' % n_, bool(fs_), ' '.join(fs_)[:80] or 'NOT DECLARED', '4')
    # ### (R334)(7): the mirror
    add('ruling (7)', 'D:/MY-DOwnloads/mirror-refresh-2026-10-29-b723.zip, already built', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-29-b723.zip'),
        'present' if os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-29-b723.zip') else 'ABSENT', '6')
    # ### (R334)(8): b723's step row 54 and its closing capture, each committed alone after act_current
    for c_, f_ in (('6b1eedb6', 'data/b723_steps.json'), ('9e3f4e39', 'data/b723_relay_push-b723-closing_push_out.txt')):
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (8)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
    # ### PATHS: the four checkpoint kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R334)(8): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (8)', 'the push-b723-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (8)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (8)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (8)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b724_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b724_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b724 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b723_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R334)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with v1.4.0's controls, the root corrigendum and the price table, the ledger split carried, the open
orders triaged, the lv negation and the release list, the legacy carry, the name and address scan, the reproduction run, the touch read of
v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R334)'s counter line
beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after
the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for b725 ((R334)(10)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act on SIDE-lv-conservation's scratch-b724 alone ((R334)(5)): one commit over the deposit pin, no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b725 ((R334)(10)); the open orders by the triage's counts and tools/standing/orders.py's output, not a hand
    list ((R334)(4)) (Component 6, the Edit tool)."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b724 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-ONE, THE SECOND CHECKPOINT ACT: 9 OF 10 REPEAT CLASSES '
              'REPAIRED WITH CONTROLS, THE TENTH CONTROLLED WHERE b723`S CARRY REPAIRED IT; THE ROOT ROUTE REPAIRED, b723`S ROW WRITTEN; THE LEDGER '
              'SPLIT CARRIED AT ITS PRICE; 142 OPEN ORDERS TRIAGED; THE lv NEGATION COMPILED, THE ERRATUM ENTERED; THE LEGACY IMPORTS CARRIED, '
              'UNDER (R334).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 6, the Edit tool; b723's sections over b723's objects not carried). A row of two
    reads its bank's verdict line by vtail; a row of three reads the line its pattern names (a bank with several verdict lines, or a verdict
    wrapped across lines)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.4.0: the ten repeat classes and the root route, each case failing before its repair and passing after',
                 'b724_standing_v140.txt'),
                ('b723`s corrigendum row at act_roots :102 in b680`s form, verify over it and the repaired route`s replay', 'b724_root_corrigendum.txt',
                 r'\*\*THE ROW WRITTEN[^*]*'),
                ('the price table, each component priced before it ran, the choice', 'b724_price.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE LEDGER SPLIT ((R334)(3))', [
                ('carried whole to b725 with its price, nothing cut', 'b724_split_price.txt')]),
            ('THE OPEN ORDERS ((R334)(4))', [
                ('the open orders, each against its trigger as written; the author`s word table for the root`s prompt', 'b724_orders_triage.txt')]),
            ('THE lv NEGATION ((R334)(5))', [
                ('not_T3_perClass_to_combinations on scratch-b724 alone, one dispatch read by its id', 'b724_lv.txt'),
                ('the release sitting`s list', 'b724_release_list.txt')]),
            ('THE LEGACY IMPORTS ((R334)(6))', [
                ('the sources scanned for the previous name, carried with the remaining price', 'b724_legacy.txt')]),
            ('THE NAME AND ADDRESS ((R332)(9))', [
                ('the scan over every commit and bank of the act, the previous address and name held in memory, the counts alone', 'b724_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b723`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b724_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: SIDE-lv-conservation`s scratch-b724 alone ((R334)(5)) -- one commit c9cd1ea9 over the deposit pin 93c27ec2, one',
    '    file at the root (CircuitClosure.lean, imported by no module), pushed and run once (run 40964150574), read by its run id ; no',
    '    kernel`s main touched, no tag cut (N5) ; the rebuild-b721 branches of the wave 1 kernels as b723 left them ; SIDE-explicit-formula`s',
    '    main at badaccc and v0.37 unmoved, the challenge branch challenge-b720-h2-sign-iff-rh standing ; the pin-b718-de5ce8a9 branches left',
    '    as banked ; port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main',
    '    and its deposit v0.10.0 unmoved ; SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this',
    '    host, the runner dispatches (R334)(5)`s one alone, read by its id ; free memory read before each computation, push, dispatch and',
    '    read ; the push-b723-* branches of relay and PLACE-papers deleted at step zero by name after --merged listed them, one per command',
    '    and each its own message ; nothing vendored ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file and',
    '    the earlier acts` units files untracked ; N2: every repair of (R334)(2) printing its control failing before and passing after',
    '    (relay data/b724_standing_v140.txt) ; N3: (R334)(3) carried whole, nothing of it landed ; (R332)(9): no new occurrence of the',
    '    author`s name or address in anything the act wrote, committed or pushed (relay data/b724_address_scan.txt), the commits under the',
    '    GitHub login and its noreply address ; no identifier of the author in any outbound request header, URL, input or payload, or in any',
    '    workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads, pushes, the dispatch and the run read) the',
    '    act`s outbound calls ; the deposit route untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS (the',
    '    weight line, the corrigendum, the entry), ERRATA (E-2026-10-29-1, (R334)(5)) and OPEN_TRAILS (the trail with the DONE orders`',
    '    closing lines) appended ; no paper cut, moved or renamed, the ledger split carried whole ((R334)(3)) ; no FOUNDATIONS, REGISTRY,',
    '    README or faces page byte ; data/act_roots.txt (b723`s corrigendum row) and the corrigenda bank appended ; data/act_current.json',
    '    written at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.4.0 by (R334)(2), the ten classes and the root route ;',
    '    the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b723 unedited ; the mirror zip written outside every',
    '    repository over the roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build',
    '    and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R334)(10)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        the DONE orders` dated closing lines in the trail, the TRIGGER MET orders each priced and its act named, the AUTHOR`S WORD',
    '        orders as the author rules them at the root`s prompt (relay data/b724_orders_triage.txt).',
    '    (c) For b725, each from its bank: the ledger split carried whole with its price (relay data/b724_split_price.txt); the legacy',
    '        imports with the remaining price (relay data/b724_legacy.txt); the reproduction`s NOT RUN rows, each with its price (relay',
    '        data/b724_reproduce.txt); the report tool outside the sealed list; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); scratch-b724 of SIDE-lv-conservation (at',
    '        c9cd1ea9, (R334)(5)`s, off main, untagged); challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9',
    '        branches as banked; the rebuild-b721 branches of the wave 1 kernels as b723 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, SIDE-lv-conservation`s scratch-b724 carrying (R334)(5)`s one commit, no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b724: the standing repairs are v1.4.0's ((R334)(2), relay data/b724_standing_v140.txt, read in the corrigendum section); the
    # ### carry's diffs here (b724 carried at step zero before the fold; its tools since are the templates and tools/acts/b724.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act, one commit on '
          'SIDE-lv-conservation`s %s branch ((R334)(5)); the %s branches of five wave 1 kernels as b723 left them; SIDE-lv-conservation`s main '
          'untouched, port-b707 at b712`s tip %s)' % (len(ks), K.JOIN_NEW_TIP[:8], K.LV_SCRATCH_BRANCH, K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
#⟪END⟫
#⟪SECTION record 2⟫
def _trail_resolved(text):
    """b703's reader of the trail's Resolved line, its navigator letters taken with a prime: this act's navigator letter is (b`), which b703's
    `\\([a-z]\\)` cannot read (the gate's dry run, defect (e`)); otherwise as b703's."""
    m = re.search(r"^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)"
                  r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", text, re.M)
    return (m.group(2), m.group(3)) if m else None
#⟪END⟫
#⟪SECTION record 3⟫
    b724's form over b724's objects (Component 6, the Edit tool; b723's form in git at b723's record tool): the corrigendum's foot and v1.4.0's
    controls; the root corrigendum's verify; the price table; the ledger split; the triage; the lv negation and the release list; the legacy
    carry; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure;
    the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v4 = _bfig('%s_standing_v140.txt' % ACT, r'\*\*v1\.4\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ;', 'v1.4.0`s controls')
    rc = _bfig('%s_root_corrigendum.txt' % ACT, r"\*\*THE ROW WRITTEN IN b680'S FORM ; VERIFY OVER IT: (b\d{3}) (AGREE|DISAGREE), ([^;]*) ; THE REPAIRED "
               r"ROUTE`S\s+(?:### )?REPLAY (AGREES|DISAGREES) ;", 'the root corrigendum`s foot')
    rr, = _bfig('%s_root_corrigendum.txt' % ACT, r'### THE ROW \(data/act_roots\.txt :(\d+),', 'the root corrigendum`s row')
    pr = _bfig('%s_price.txt' % ACT, r'\*\*THE PRICE TABLE: (.*) ; THE CLOSE ([\d.]+) H ; THE BUDGET ([\d.]+) H \(b723\'S ACT\) ; THE CHOICE: ([^*]*)\.\*\*', 'the price table`s foot')
    sl = _bfig('%s_split_price.txt' % ACT, r'(?m)^### ### \*\*THE LEDGER SPLIT: (CARRIED WHOLE TO b\d{3}|LANDED)[^-]*-- (\d+) CITATION OCCURRENCES MOVED \((\d+) IN LIVE '
               r'TOOLS\), THE SPLIT ABOUT ([\d.-]+) H BEFORE A CLOSE OF ([\d.]+) H ; ([^.]*)\.\*\*', 'the split`s foot')
    tr = _bfig('%s_orders_triage.txt' % ACT, r"\*\*THE OPEN ORDERS: (\d+) TRIAGED -- DONE (\d+) ; TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) \(ACTED (\d+), "
               r"PRICED AND NAMED (\d+)\) ; AUTHOR'S WORD (\d+) \(RETIRE (\d+), KEEP (\d+), RE-SCOPE (\d+)\) ; CITATIONS (\d+) OF (\d+) ON THEIR LINES\.\*\*",
               'the triage`s foot')
    lv = _bfig('%s_lv.txt' % ACT, r'\*\*THE lv NEGATION: (\S+) COMPILES ON (\S+) \(([0-9a-f]+)\), RUN (\d+), AXIOMS \[([^\]]*)\], NO sorryAx ; THE TEXT AS '
               r'WRITTEN (DOES NOT ELABORATE|ELABORATES)[^;]* ; DEPENDENTS (\d+) ; ONE DISPATCH ; NO MAIN OR TAG TOUCHED\.\*\*', 'the lv negation`s foot')
    rlist, = _bfig('%s_release_list.txt' % ACT, r'\*\*THE RELEASE SITTING`S LIST: (\w+) ITEMS? ADDED ', 'the release list`s foot')
    lg = _bfig('%s_legacy.txt' % ACT, r'\*\*THE LEGACY IMPORTS: CARRIED WITH THE REMAINING PRICE \(ABOUT ([\d.-]+) H\) -- (\d+) SOURCES SCANNED, (\d+) '
               r'CARR(?:IES|Y) THE PREVIOUS NAME IN CODE \(([^)]*)\), .* ; NOTHING COPIED, legacy\.py UNCHANGED \((\d+) NAMES\)\.\*\*', 'the legacy carry`s foot')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
    cls, noted = _v140_classes()
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v140_ctl=v4[0], v140_cases=v4[1], v140_wanted=v4[2], v140_classes=len(cls), v140_noted=noted,
                rc_act=rc[0], rc_verify=rc[1], rc_why=rc[2], rc_replay=rc[3], rc_row=rr,
                pr_rows=pr[0], pr_close=pr[1], pr_budget=pr[2], pr_choice=pr[3],
                sl_word=sl[0], sl_occ=sl[1], sl_live=sl[2], sl_hours=sl[3], sl_close=sl[4], sl_cut=sl[5],
                tr_n=tr[0], tr_done=tr[1], tr_not=tr[2], tr_met=tr[3], tr_acted=tr[4], tr_priced=tr[5], tr_word=tr[6], tr_retire=tr[7],
                tr_keep=tr[8], tr_rescope=tr[9], tr_cit=tr[10], tr_cit_of=tr[11],
                lv_thm=lv[0], lv_branch=lv[1], lv_sha=lv[2], lv_run=lv[3], lv_axioms=lv[4], lv_text=lv[5], lv_deps=lv[6], rl_items=rlist,
                lg_hours=lg[0], lg_sources=lg[1], lg_named=lg[2], lg_where=lg[3], lg_names=lg[4],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _lv_kind(rows, kind):
    """(R334)(5): the lv negation's rows of one kind as banked (data/b724_lv_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]


def _v140_classes():
    """v1.4.0's controls bank by its class heads (`### (<roman>) ...`): (the classes in the bank's order, those whose section carries a
    `  NOTE: ` line -- the class repaired before v1.4.0, controlled where it stands); the root route has a case and no class head."""
    t = rdn('%s_standing_v140.txt' % ACT)
    heads = [(m.group(1), m.start()) for m in re.finditer(r'(?m)^### \(([a-z]+)\) ', t)]
    out, noted = [], []
    for i, (c, at) in enumerate(heads):
        end = heads[i + 1][1] if i + 1 < len(heads) else len(t)
        out.append(c)
        if re.search(r'(?m)^  NOTE: ', t[at:end]):
            noted.append(c)
    return out, noted
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R334): no lean process runs on this host; one dispatch, (R334)(5)'s, read by its run id. From the command bank (the seat's
    commands, read live from the capture by the `commands` route: local lean none; the dispatch commands the seat's `lv724.py dispatch`)
    and the lv rows (relay data/b724_lv_rows.json: the dispatch by command and the read by its run id), against the worklist's LV_RUNS
    (Component 6, the Edit tool; b723's N1 read b723's axiom runs)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = json.loads(rdn('%s_lv_rows.json' % ACT) or '[]')
    dsp, rds = _lv_kind(rows, 'dispatch'), _lv_kind(rows, 'read')
    ran = sorted((r.get('kernel'), str(r.get('run'))) for r in dsp)
    want = sorted((k, str(r)) for k, r in K.LV_RUNS)
    read_ids = sorted(str(r.get('run')) for r in rds)
    by_cmd = [r for r in dsp if not r.get('via')]
    ok = bool(cm) and not seat_lean and len(ran) <= K.MAX_DISPATCHES and ran == want and read_ids == sorted(r for _k, r in want) \
        and len(disp) == len(by_cmd)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b724_commands.json): %s; dispatch commands in the capture: %s against '
        'the rows` dispatches by command %d; the runs dispatched (relay data/b724_lv_rows.json) %d of %d at most, equal to the worklist`s '
        'LV_RUNS: %s (%s); each read by its id: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(by_cmd), len(ran), K.MAX_DISPATCHES, ran == want,
            ', '.join('%s %s' % x for x in ran) or 'NONE', read_ids == sorted(r for _k, r in want)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (Component 6, the Edit tool, over b724's objects; b723's chain over b723's registrations in git at b723's record tool): the classes
# ### of (R334)(2) and the root route, each read in v1.4.0's controls bank by its cases
N2_CLASSES = ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'root')
N2_CASE = re.compile(r'(?m)^  \(([a-z]+)\) [^\n]*\n      BEFORE \([^)]*\): [^\n]* -> (\w+)\n      AFTER  \([^)]*\): [^\n]* -> (\w+)$')
# ### N2: each tool's controls before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b724_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),)
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R334): every repair prints its control failing before and passing after -- in v1.4.0's controls bank (relay
    data/b724_standing_v140.txt) each case of the ten classes and of the root route a BEFORE line ending FAILS and an AFTER line ending
    PASSES, every class with a case, the foot's CASES and AS WANTED the cases read; the class repaired before v1.4.0 (its NOTE) named; the
    address scan's controls before its places. From the bank's own lines."""
    v = rdn('%s_standing_v140.txt' % ACT)
    cases = {}
    for m in N2_CASE.finditer(v):
        cases.setdefault(m.group(1), []).append(m.group(2) == 'FAILS' and m.group(3) == 'PASSES')
    foot = re.search(r'\*\*v1\.4\.0: CONTROLS [^;]+ ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', v)
    n_cases = sum(len(x) for x in cases.values())
    _cls, noted = _v140_classes()
#⟪END⟫
#⟪SECTION record 12⟫
    ok = sorted(cases) == sorted(N2_CLASSES) and all(all(x) for x in cases.values()) and bool(foot) \
        and int(foot.group(1)) == int(foot.group(2)) == n_cases and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'v1.4.0`s controls (relay data/b724_standing_v140.txt): the classes read by their cases %s; cases %d, each BEFORE FAILS and AFTER '
        'PASSES: %s; the class repaired before v1.4.0, controlled where it stands: %s; the foot`s cases %s, as wanted %s; each tool`s controls '
        'before its figures: %s' % (
            ', '.join('(%s) %d' % (k, len(cases.get(k) or [])) for k in N2_CLASSES), n_cases, all(all(x) for x in cases.values()),
            ', '.join('(%s)' % x for x in noted) or 'none', foot.group(1) if foot else 'unread', foot.group(2) if foot else 'unread',
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (Component 6, the Edit tool, over b724's objects; b723's over its closed form in git at b723's record tool): the banks whose
# ### grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b724_split_price.txt', ('CARRIED WHOLE', 'NOTHING CUT')), ('b724_price.txt', ('(3) CARRIED WHOLE WITH ITS PRICE',)),
             ('b724_standing_v140.txt', ('ALL AS WANTED',)), ('b724_orders_triage.txt', ('TRIAGED', 'ON THEIR LINES')),
             ('b724_lv.txt', ('NO sorryAx', 'ONE DISPATCH')), ('b724_release_list.txt', ('NOTHING SENT',)),
             ('b724_legacy.txt', ('CARRIED WITH THE REMAINING PRICE', 'NOTHING COPIED')), ('b724_reproduce.txt', ('REPRODUCES',)))
# ### N3: the ledgers whose lines a cut of (3) would remove, and the words a sentence uses to say the split landed
N3_LEDGERS = ('FINDINGS.md', 'OPEN_TRAILS.md')
N3_LANDED = re.compile(r'(?i)\b(?:landed|archived|cut|moved to the archive)\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|nothing|no)\b[^.;]{0,24}$')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R334): (3) lands only clean -- carried whole, nothing of it lands: the split bank's foot CARRIED WHOLE and NOTHING CUT, every
    graded bank's grade at its end; at PLACE-papers since the act's base no line removed from FINDINGS or OPEN_TRAILS, no file added (no
    archive file, offset table or pointer header); no sentence of the entry saying the split landed, was cut or archived but in negation. From
    the banks' last lines, git over PLACE-papers (numstat and name-status from PRE_PP), and the entry as composed (the findings bank's text,
    or the composer before it is written)."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
    ns = [l.split('\t') for l in g(PP, 'diff', '--numstat', K.PRE_PP, 'HEAD').split(NL) if l.count('\t') == 2]
    cut = ['%s -%s' % (p_, d_) for _a, d_, p_ in ns if p_ in N3_LEDGERS and d_ != '0']
    added_pp = [l.split('\t')[-1] for l in g(PP, 'diff', '--name-status', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('A', 'R', 'C')]
#⟪END⟫
#⟪SECTION record 19⟫
    carried = f['sl_word'].startswith('CARRIED WHOLE') and f['sl_cut'] == 'NOTHING CUT'
#⟪END⟫
#⟪SECTION record 20⟫
    landed = []
    for s in sents:
        if re.search(r'(?i)ledger split|\(3\)', s):
            for m in N3_LANDED.finditer(s):
                if not N3_NEGATED.search(s[:m.start()]):
                    landed.append(s.strip()[:120])
                    break
    ok = all(o for _n, o in graded) and carried and not cut and not added_pp and not landed
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the split carried whole, nothing cut (relay data/b724_split_price.txt): %s; '
        'lines removed from %s at PLACE-papers since %s: %s; files added there: %s; the sentences of %s saying the split landed, was cut or '
        'archived but in negation: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), carried, ' and '.join(N3_LEDGERS), K.PRE_PP[:8], cut or 'NONE', added_pp or 'NONE', src,
            landed or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R334)(1), N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build at [23] rewrites by the ferry's (W) list ((R334)(8))
N4_APPENDED = ('data/%s_steps.json' % ACT, 'data/%s_bank_hashes.json' % ACT, 'data/%s_hook_refusals.txt' % ACT, 'tools/mirror_prevbuild.json')


def _post_lock_edits():
    """the lock's time from the face (its `locked at (UTC)` line), the lock commit (the first relay commit at or after it, carrying the face),
    the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    face = rd(FACE) or ''
    m = re.search(r'locked at \(UTC\) : (\S+)', face)
    lock = _iso_epoch(m.group(1)) if m else None
    out = dict(lock=lock, lock_iso=m.group(1) if m else None, lock_commit=None, after=[], edited=[], dirty=[])
    if lock is None:
        return out
    rows = [l.split(' ', 1) for l in g(ROOT, 'log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.PRE_RELAY).split(NL) if l.strip()]
    face_rel = os.path.relpath(FACE, ROOT).replace(os.sep, '/')
    lc = next((h for h, ct in rows if int(ct) >= lock and face_rel in g(ROOT, 'show', '--name-only', '--format=', h).split()), None)
    out['lock_commit'] = lc
    if lc is None:
        return out
    tracked = set(x for x in g(ROOT, 'ls-tree', '-r', '--name-only', lc).split(NL) if x.strip())
    guard = lambda p: p not in N4_APPENDED and (p == face_rel or p.startswith('tools/') or (p.startswith('data/%s_' % ACT) and p in tracked))
    hs = [h for h, _ct in rows]
    out['after'] = hs[hs.index(lc) + 1:]
    for h in out['after']:
        for p in g(ROOT, 'show', '--name-only', '--format=', h).split():
            if guard(p):
                out['edited'].append('%s %s' % (h[:8], p))
    out['dirty'] = [p for p in g(ROOT, 'diff', '--name-only', 'HEAD').split() if guard(p)]
    return out
#⟪END⟫
#⟪SECTION record 23⟫
    # ### (R334)(1), N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (Component 8, the Edit tool; b723's
    # ### arm read the drafts and the rebuild branches) -- read from git, not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R334)(5), (9), N5 (Component 6, the Edit tool): no kernel's main touched and no tag cut -- every ref of every kernel carrying a
    # ### commit made after the act's opening commit is SIDE-lv-conservation's scratch branch at C4_LV, its parent the deposit pin, off main
    # ### and untagged, and it is there; no .lean file changed or untracked in a kernel's tree; the rebuild-b721 branches kept as b723 left
    # ### them; the address scan's count from its bank (relay data/b724_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w, lv_new = [], []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if kn == K.KERNEL and r_[0] == 'refs/heads/' + K.LV_SCRATCH_BRANCH and r_[1] == K.C4_LV:
                    lv_new.append(kn)
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    lv_par = g(LV, 'rev-parse', '--verify', '--quiet', K.C4_LV + '^').strip()
    lv_scr_ok = lv_new == [K.KERNEL] and lv_par == K.LV_V0100 and grc(LV, 'merge-base', '--is-ancestor', K.C4_LV, 'main') != 0 \
        and not g(LV, 'tag', '--points-at', K.C4_LV).strip()
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and lv_scr_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b724_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than %s`s %s at %s, or a .lean file in a kernel`s tree (%d kernels read): %s; the scratch branch there, its parent the '
            'deposit pin %s, off main and untagged: %s; the %s branch kept on the six wave 1 kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', K.KERNEL, K.LV_SCRATCH_BRANCH, K.C4_LV[:8], len(K.KERNEL_PATHS), lean_w or 'NONE',
                K.LV_V0100[:8], lv_scr_ok, K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b724 — lane two, act one hundred and fifty-one, the second checkpoint act under (R334): b723 at its weight and its corrigendum; '
            'the ten repeat classes and the root route; the ledger split carried; the open orders triaged; the lv negation and its erratum; the '
            'legacy imports carried')
#⟪END⟫
#⟪SECTION record 29⟫
def _triage_rows(grade=None):
    """(R334)(4): the triage bank's rows as it prints them -- (name, grade, the bank's line, the entry it names) in the bank's order, those of
    one grade when one is given."""
    out = []
    for i, l in enumerate(rdn(K.TRIAGE.split('/')[-1]).split(NL), 1):
        m = re.match(r"^  (W-ORD-[\w-]+) -- (DONE|TRIGGER NOT MET|TRIGGER MET|AUTHOR'S WORD) \(entry (\S+ :\d+)\)$", l)
        if m and (grade is None or m.group(2) == grade):
            out.append((m.group(1), m.group(2), i, m.group(3)))
    return out


def _closing_lines():
    """(R334)(4): the trail's dated closing line for each DONE order, the work cited at its row of the triage bank, one order to a line (so
    tools/standing/orders.py reads each by its own clause)."""
    return ['**`%s` CLOSED 2026-10-29, b724,** done by (R334)(4)`s triage, the work cited at relay data/b724_orders_triage.txt :%d.' % (n, i)
            for n, _g, i, _e in _triage_rows('DONE')]


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 6 form cut at what the act did ("<r> of <n> repeat classes repaired with
    controls, the <n-th> controlled where b723's carry repaired it; the root route repaired, b723's row written; the ledger split carried at
    its price; <o> open orders triaged: <d> done, <t> trigger not met, <m> acted or priced, <w> for the author's word; the lv negation
    compiled, the erratum entered; the legacy imports carried"), every figure from the banks (Component 6, the Edit tool; b723's title over
    b723's objects in git at b723's record tool)."""
#⟪END⟫
#⟪SECTION record 31⟫
    n, k = f['v140_classes'], len(f['v140_noted'])
    nth = {9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
    if k != 1 or n not in nth:
        sys.exit('### THE TITLE: %d CLASSES, %d REPAIRED BEFORE v1.4.0 -- THE FORM NAMES ONE; NOTHING COMPOSED' % (n, k))
    if not f['sl_word'].startswith('CARRIED') or f['rc_replay'] != 'AGREES':
        sys.exit('### THE TITLE: THE SPLIT %s, THE ROOT ROUTE`S REPLAY %s -- NOTHING COMPOSED' % (f['sl_word'], f['rc_replay']))
    return ('## %d of %d repeat classes repaired with controls, the %s controlled where b723’s carry repaired it; the root route repaired, '
            'b723’s row written; the ledger split carried at its price; %s open orders triaged: %s done, %s trigger not met, %s acted or '
            'priced, %s for the author’s word; the lv negation compiled, the erratum entered; the legacy imports carried' % (
                n - k, n, nth[n], f['tr_n'], f['tr_done'], f['tr_not'], f['tr_met'], f['tr_word']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) b723`s root standing as recorded, verify over the corrigendum row at act_roots :%s reading %s %s (%s), the repaired route`s '
            'replay %s -- the chain`s standing reading of b723 for the author at the root`s prompt (relay data/b724_root_corrigendum.txt); (2) the '
            'ledger split %s with its price, nothing cut (relay data/b724_split_price.txt); (3) the %s open orders triaged: %s done, their dated '
            'closing lines with the trail; %s trigger not met; %s trigger met, %s acted and %s priced and named; %s for the author`s word in one table, '
            'RETIRE %s, KEEP %s, RE-SCOPE %s (relay data/b724_orders_triage.txt); (4) the lv negation compiled on %s at %s, run %s, no sorryAx, the '
            'text as written not elaborating, ERRATA %s, the release sitting`s list one item (relay data/b724_lv.txt, data/b724_release_list.txt); '
            '(5) the legacy imports carried with the remaining price, the previous name in code at %s (relay data/b724_legacy.txt); (6) the report '
            'tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); (7) %s and the seat’s %s defect%s as lettered' % (
                f['rc_row'], f['rc_act'], f['rc_verify'], f['rc_why'].lower(), f['rc_replay'].lower(), f['sl_word'].lower(), f['tr_n'],
                f['tr_done'], f['tr_not'], f['tr_met'], f['tr_acted'], f['tr_priced'], f['tr_word'], f['tr_retire'], f['tr_keep'], f['tr_rescope'],
                f['lv_branch'], f['lv_sha'], f['lv_run'], K.ERRATA_ID, f['lg_where'],
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):
        rows += [l for l in rdn(name).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    return sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l)), len(rows)


def _runs3(act=ACT):
    """v9 row (83): "a class that repeats in three acts running is the next act's opening component" -- each row of the act's defects bank
    tagged REPEAT <the previous act> (<letter>) whose row in the previous act's defects bank is itself tagged REPEAT <the act before> (...):
    a list of (this act's letter, 'b<n-2> (x) -> b<n-1> (y) -> b<n> (z)'). A REPEAT naming an older act, a class, or no letter, is not a run
    of three."""
    n = int(act[1:])
    p1, p2 = 'b%d' % (n - 1), 'b%d' % (n - 2)
    tag = re.compile(r"^    \(([a-z]'?)\) THE (?:SEAT|NAVIGATOR)'S \[(?:CLAIM|CLOSE) ; REPEAT (b\d+) \(([a-z]'?)\)\]")
    prev = dict((m.group(1), m) for m in (tag.match(l) for l in rdn('%s_defects.txt' % p1).split(NL)) if m)
    out = []
    for l in rdn('%s_defects.txt' % act).split(NL):
        m = tag.match(l)
        if m and m.group(2) == p1 and m.group(3) in prev and prev[m.group(3)].group(2) == p2:
            out.append((m.group(1), '%s (%s) -> %s (%s) -> %s (%s)' % (p2, prev[m.group(3)].group(3), p1, m.group(3), act, m.group(1))))
    return out


def _runs3_line():
    """the rows of _runs3 grouped by the class's row two acts back, each class once with this act's rows under it."""
    r = _runs3()
    by = {}
    for l, c in r:
        by.setdefault(c.split(' -> ')[0], []).append(l)
    return ('the classes repeating three acts running, by the tags (v9 row (83), each the next act’s opening component, printed for the '
            'author beside (R334)(10)’s naming of b725): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 6, the Edit tool, over b724's objects;
    b723's composer over b723's objects kept below as _finding_text_b723, not called, and in git at b723's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    n, k = f['v140_classes'], len(f['v140_noted'])
    e = ['', _title(), '',
         '%s of the %s repeat classes of (R334)(2) are repaired at tools/standing/ %s, each control failing before and passing after, the %s '
         'controlled where b723’s carry repaired it; the root route is repaired and b723’s corrigendum row written in b680’s form, verify over '
         'it reading %s %s and the repaired route’s replay %s; the %s open orders are triaged -- %s done, %s trigger not met, %s met and priced, '
         '%s for the author’s word in one table; the lv negation compiles on a scratch branch with no sorryAx and its erratum is entered; the '
         'ledger split and the legacy imports are carried with their prices.' % (
             num_word(n - k).capitalize(), num_word(n), f['ver'], {10: 'tenth', 11: 'eleventh'}.get(n, 'last'), f['rc_act'], f['rc_verify'],
             f['rc_replay'], f['tr_n'], f['tr_done'], f['tr_not'], f['tr_met'], f['tr_word']), '',
         '*Filed at b724 on the author’s ruling `(R334)`; %d question%s put before the root. Banks: relay `data/b724_corrigendum.txt`, '
         '`data/b724_standing_v140.txt`, `data/b724_root_corrigendum.txt`, `data/b724_price.txt`, `data/b724_split_price.txt`, '
         '`data/b724_orders_triage.txt`, `data/b724_lv.txt`, `data/b724_lv_rows.json`, `data/b724_release_list.txt`, `data/b724_legacy.txt`, '
         '`data/b724_reproduce.txt`, `data/b724_address_scan.txt`, `data/b724_touch.txt`, `data/b724_standing_figures.txt`, '
         '`data/b724_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repeat classes** ((R334)(1)-(2), N2, `%s`, `%s`, `%s`, `%s`): b723 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b723’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, S2 and N4 printed REFUTED BY THE SUITE with both readings, the corrigenda bank appended at row (%s) (relay '
         'data/b724_corrigendum.txt); tools/standing/ at %s, its controls %s -- %s cases, %s as wanted, each case failing before the repair and '
         'passing after it; class %s repaired before v1.4.0 by b723’s carry and controlled where it stands (relay data/b724_standing_v140.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v140_ctl'], f['v140_cases'],
             f['v140_wanted'], ', '.join('(%s)' % x for x in f['v140_noted'])), '',
         '**The root route** ((R334)(2), `%s`, `%s`): b723’s corrigendum row at act_roots :%s in the form b680’s carries; verify over it reads '
         '%s %s -- %s; the route repaired at v1.4.0, the hashes bank outside the set a root names (the lower of the two forms priced), its replay '
         'of b723’s items %s; b723’s root stands as recorded, the chain’s standing reading of b723 put to the author at the root’s prompt (relay '
         'data/b724_root_corrigendum.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], f['rc_row'], f['rc_act'], f['rc_verify'], f['rc_why'].lower(), f['rc_replay']), '',
         '**The ledger split** ((R334)(3), N3, `%s`): carried whole to b725 with its price -- %s citation occurrences to move, %s of them in live '
         'tools, the split about %s h before a close of %s h, the price table’s choice; nothing cut, no ledger rewritten, no archive file, '
         'offset table or pointer header written (relay data/b724_split_price.txt, data/b724_price.txt).' % (
             K.C2_RELAY[:8], f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close']), '',
         '**The open orders triaged** ((R334)(4), `%s`): the %s open orders at PLACE-papers main read against their triggers as written -- DONE '
         '%s, each with its dated closing line in the trail; TRIGGER NOT MET %s, carried; TRIGGER MET %s, acted %s, priced and named %s; '
         'AUTHOR’S WORD %s in one table for the root’s prompt, RETIRE %s, KEEP %s, RE-SCOPE %s; citations %s of %s on their lines (relay '
         'data/b724_orders_triage.txt).' % (
             K.C3_RELAY[:8], f['tr_n'], f['tr_done'], f['tr_not'], f['tr_met'], f['tr_acted'], f['tr_priced'], f['tr_word'], f['tr_retire'],
             f['tr_keep'], f['tr_rescope'], f['tr_cit'], f['tr_cit_of']), '',
         '**The lv negation** ((R334)(5), N1, N5, `%s`, `%s`, `%s`): `%s` on SIDE-lv-conservation’s %s alone, one file over the deposit pin, '
         'one dispatch, run %s read by its id: it compiles, its axioms [%s], no sorryAx; the text as written does not elaborate (a theorem’s '
         'name is not a Prop), the statement compiled its closure over the deposit statement’s binders; dependents %s; ERRATA %s entered, the '
         'deposit not edited; the release sitting’s list %s item added, the lv description’s “zero sorry”; no main or tag touched (relay '
         'data/b724_lv.txt, data/b724_lv_rows.json, data/b724_release_list.txt).' % (
             K.C4_LV[:8], K.C4_RELAY[:8], K.C4_PP[:8], f['lv_thm'], f['lv_branch'], f['lv_run'], f['lv_axioms'], f['lv_deps'], K.ERRATA_ID,
             f['rl_items'].lower()), '',
         '**The legacy imports** ((R334)(6), `%s`): %s sources scanned, %s carrying the previous name in code (%s), a verbatim copy barred by '
         '(R332)(9)(i); nothing copied, tools/standing/legacy.py unchanged (%s names); carried with the remaining price, about %s h (relay '
         'data/b724_legacy.txt).' % (K.C5_RELAY[:8], f['lg_sources'], f['lg_named'], f['lg_where'], f['lg_names'], f['lg_hours']), '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b724_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R332)(9), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b724_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b724_touch.txt). The act’s counter CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b724 -- %s, %s, %s, %s -- against b723’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b724_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the repairs and the triage meet at the record -- a class repeats by the corrigendum’s '
         'tags and an order is open by the trail’s own latest line, neither carried by hand; the lv negation and the root corrigendum meet at '
         'what a recorded statement is -- each stands as recorded, beside the reading that corrects it.', '',
         '**Carried to:** %s, each from its bank: the ledger split with its price (relay data/b724_split_price.txt); the legacy imports with '
         'theirs (relay data/b724_legacy.txt); the author’s-word orders as the author rules them and the met orders, each priced and its act '
         'named (relay data/b724_orders_triage.txt); the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b723():
    """b723's form over b723's objects, kept for the record and not called (Component 6)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 6, the Edit tool, over b724's objects; b723's composer over b723's objects kept below as _trail_text_b723,
    not called, and in git at b723's record tool); (R334)(4)'s dated closing line for each DONE order, then the open-orders line written
    from tools/standing/orders.py's output over the trail at HEAD with those lines beneath it."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    closing = _closing_lines()
    if len(closing) != int(f['tr_done']):
        sys.exit('### THE TRAIL: %d CLOSING LINES AGAINST THE TRIAGE`S DONE %s -- NOTHING COMPOSED' % (len(closing), f['tr_done']))
    op = ORD.report(ORD.read(ORD.trail('HEAD') + closing), 'HEAD')[1]
    still = [n for n, _g, _i, _e in _triage_rows('DONE') if n in op]
    if still:
        sys.exit('### THE TRAIL: DONE ORDERS STILL OPEN BY THE GENERATOR`S RULE OVER THE CLOSING LINES: %s -- NOTHING COMPOSED' % still)
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R334) ratified.** Its components as the ferry orders them (relay data/b724_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b723’s weight), :%s (the corrigendum), :%s (the entry); ERRATA.md %s; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.ERRATA_ID), '',
             '**The orders closed by the triage** ((R334)(4), relay data/b724_orders_triage.txt, its DONE section; %d):' % len(closing), '']
    rows_ += closing + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the closing lines above, the line above from '
             'tools/standing/orders.py`s output; the triage of the %s: done %s, trigger not met %s, trigger met %s (acted %s, priced and named %s), '
             'the author`s word %s -- RETIRE %s, KEEP %s, RE-SCOPE %s, put at the root`s prompt in one table (relay data/b724_orders_triage.txt).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + closing)), f['tr_n'], f['tr_done'], f['tr_not'], f['tr_met'], f['tr_acted'],
                 f['tr_priced'], f['tr_word'], f['tr_retire'], f['tr_keep'], f['tr_rescope']), '',
             '**The repeat classes and the root route:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay '
             'data/b724_standing_v140.txt); b723’s corrigendum row at act_roots :%s, verify %s %s, the repaired route’s replay %s (relay '
             'data/b724_root_corrigendum.txt).' % (f['ver'], f['v140_cases'], f['v140_wanted'], f['rc_row'], f['rc_act'], f['rc_verify'],
                                                   f['rc_replay']), '',
             '**The ledger split:** carried whole to b725 with its price, nothing cut (relay data/b724_split_price.txt).', '',
             '**The lv negation:** `%s` compiles on SIDE-lv-conservation’s %s (`%s`), run %s, no sorryAx; the text as written does not elaborate; '
             'ERRATA %s; the release sitting’s list %s item (relay data/b724_lv.txt, data/b724_release_list.txt).' % (
                 f['lv_thm'], f['lv_branch'], f['lv_sha'], f['lv_run'], K.ERRATA_ID, f['rl_items'].lower()), '',
             '**The legacy imports:** carried with the remaining price, about %s h, nothing copied (relay data/b724_legacy.txt).' % f['lg_hours'], '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b724_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b724_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b724_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b724 `%s` (previous `%s`, b723’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b724_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b724_standing_v140.txt); the standing '
             'report tool (relay data/b724_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; one commit on SIDE-lv-conservation’s %s at `%s` over the deposit pin, '
              'its one run read by its id; the %s branches as b723 left them; port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with '
              'its one tag %s; no lean process on this host.' % (
                  K.LV_SCRATCH_BRANCH, K.C4_LV[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b724_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b723’s %s, %s, %s, %s (relay data/b724_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b724_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b723():
    """b723's trail record over b723's objects, kept for the record and not called (Component 6)."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R334)(5)`s one, by the seat`s lv724.py dispatch; MEASURED off the command bank (each dispatch route run at a command`s head).'),
    ('runner runs read by their ids for the lv negation', 'AXRUNS', 'AXRUNS', 'runs', '### (R334)(5), N1: one, read by its id; MEASURED off data/b724_lv_rows.json against the worklist`s LV_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b724*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('scratch branches cut on a kernel', 'LVSCRATCH', 'LVSCRATCH', 'branches', '### (R334)(5): SIDE-lv-conservation`s scratch-b724 alone, over the deposit pin; MEASURED off the kernels` refs/heads/scratch-b724.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b723 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b724*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files written by this act`s kernel commit', 'LVLEANACT', 'LVLEANACT', 'files', '### (R334)(5): CircuitClosure.lean on scratch-b724; MEASURED off its commit`s files.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: no main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R334)(8): relay push-b723-closing, push-b723-preroot, push-b723-record; PLACE-papers push-b723-preroot, push-b723-record; each local, by name, after --merged listed it (data/b724_stepzero.txt :15-:17).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commit', 0, 0, 'files', '### none: the scratch commit carries CircuitClosure.lean alone, the closure step main`s (b694).'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R334) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (698fe441) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R334)(1)-(2): FINDINGS :11536.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R334)(2): one row, b723`s (44).'),
    ('root-chain corrigendum rows written', 1, 1, 'rows', '### (R334)(2): b723`s, at data/act_roots.txt :102 in b680`s form; no second root line.'),
    ('the open orders triaged', 'ORDERS', 'ORDERS', 'orders', '### (R334)(4): each against its trigger as written; MEASURED off data/b724_orders_triage.txt :531.'),
    ('open orders closed by a dated line at the trail', 'DONEORDERS', 'DONEORDERS', 'orders', '### (R334)(4): the DONE grade; MEASURED off the triage bank`s DONE section.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b724_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R334)(2)-(6): the price table, v1.4.0`s controls, the root corrigendum, the split`s price, the triage, the lv negation and the release list, the legacy carry, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed', 0, 0, 'commits', '### (R334)(10): none this act.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registration this act; MEASURED off the (empty) list.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean statements written beside the deposit on a scratch branch', 1, 1, 'statements', '### (R334)(5): not_T3_perClass_to_combinations, in CircuitClosure.lean on scratch-b724 alone.'),
    ('ERRATA entries', 1, 1, 'entries', '### (R334)(5): E-2026-10-29-1, the deposit not edited.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R334)(2): tools/standing/ to v1.4.0 -- the ten repeat classes and the root route, each with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; data/act_roots.txt`s corrigendum row (:102) and data/b675_corrigenda.txt`s row (44), each appended; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation, push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R332)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b724_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs, the dispatch and the run read ((R334)(5)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### N2 (Component 6, the Edit tool): (R334)(10) registers nothing, so no figure bank of a registered object
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    AXRUNS=jcount('b724_lv_rows.json', lambda j: len([x for x in j if x.get('kind') == 'read'
                                                                       and (x.get('kernel'), int(x.get('run') or 0)) in set((k, int(r)) for k, r in K.LV_RUNS)])),
                    REPROWS=jcount('b724_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b724_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    ORDERS=tfirst('b724_orders_triage.txt', r'\*\*THE OPEN ORDERS: (\d+) TRIAGED'),
                    DONEORDERS=tfirst('b724_orders_triage.txt', r'(?m)^## DONE \((\d+)\)$'),
                    LVSCRATCH=sum(1 for kp in K.KERNEL_PATHS if os.path.isdir(kp)
                                  and _git(kp, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.LV_SCRATCH_BRANCH).strip()),
                    LVLEANACT=sum(1 for f_ in _git(K.LV_DIR, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.C4_LV).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('price', 'standing_v140', 'root_corrigendum', 'split_price', 'orders_triage', 'lv', 'release_list', 'legacy',
                                               'reproduce', 'address_scan') if os.path.exists(os.path.join(ROOT, 'data', 'b724_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'LVSCRATCH', 'LVLEANACT', 'AXRUNS', 'REPROWS', 'ADDRESS', 'ORDERS', 'DONEORDERS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b724_registration_%s.txt -- b724, THE SECOND CHECKPOINT ACT: b723 AT ITS WEIGHT AND ITS CORRIGENDUM; THE TEN "
                             "REPEAT CLASSES AND THE ROOT ROUTE AT v1.4.0; THE LEDGER SPLIT CARRIED WHOLE; THE OPEN ORDERS TRIAGED; THE lv "
                             "NEGATION ON A SCRATCH BRANCH AND ITS ERRATUM; THE LEGACY IMPORTS CARRIED, UNDER (R334)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b723's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten at Component 6: b723's lines (the
axiom step, H-ZETAK, the C2 closed form, H-SUPPORT, H-DIAL, the open orders generated) read banks this act does not write, and are not
carried; the lines are b724's: the lv negation on its scratch branch, its one run by its id (KERNEL), tools/standing/ v1.4.0 by its controls
(CERTIFIED), the open orders triaged, b723's corrigendum row and the instruments reproduced (REGISTERED), and the ledger split, the legacy
imports and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b724's lines (Component 6, the Edit tool), each from the record tool's figures over b724's banks
    # ------------------------------------------------------------------ KERNEL: THE lv NEGATION ((R334)(5)), its one run read by its id
    # ------------------------------------------------------------------ (N1: no lean on the host, one dispatch)
    sk = seat('%s_lv.txt' % ACT, '**THE lv NEGATION: ')
    keys['LV'] = ('KERNEL -- THE lv NEGATION ON A SCRATCH BRANCH: `%s` compiles on SIDE-lv-conservation`s %s (%s), run %s read by its id, its '
                  'axioms [%s], no sorryAx; the text as written does not elaborate; dependents %s; ERRATA %s; no main or tag touched. SOURCE %s.' % (
                      f['lv_thm'], f['lv_branch'], f['lv_sha'], f['lv_run'], f['lv_axioms'], f['lv_deps'], K.ERRATA_ID, sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.4.0 ((R334)(2)), by its controls (N2)
    sw = seat('%s_standing_v140.txt' % ACT, '**v1.4.0: CONTROLS ')   # ### appended by the template after this section
    keys['V140'] = ('CERTIFIED -- tools/standing/ v1.4.0: the ten repeat classes and the root route, controls %s -- %s cases, %s as wanted, '
                    'each failing before its repair and passing after; class %s controlled where b723`s carry repaired it. SOURCE %s.' % (
                        f['v140_ctl'], f['v140_cases'], f['v140_wanted'], ', '.join('(%s)' % x for x in f['v140_noted']), sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: THE OPEN ORDERS TRIAGED ((R334)(4)); b723'S CORRIGENDUM
    # ------------------------------------------------------------------ ROW ((R334)(2)); THE INSTRUMENTS REPRODUCED
    st = seat('%s_orders_triage.txt' % ACT, '**THE OPEN ORDERS: ')
    keys['TRIAGE'] = ('REGISTERED -- THE OPEN ORDERS TRIAGED: %s -- DONE %s, TRIGGER NOT MET %s, TRIGGER MET %s (acted %s, priced and named %s), '
                      'AUTHOR`S WORD %s (RETIRE %s, KEEP %s, RE-SCOPE %s); citations %s of %s on their lines. SOURCE %s.' % (
                          f['tr_n'], f['tr_done'], f['tr_not'], f['tr_met'], f['tr_acted'], f['tr_priced'], f['tr_word'], f['tr_retire'],
                          f['tr_keep'], f['tr_rescope'], f['tr_cit'], f['tr_cit_of'], st['text']))
    seats.append(st)
    sc = seat('%s_root_corrigendum.txt' % ACT, '**THE ROW WRITTEN IN ')
    keys['ROOTROW'] = ('REGISTERED -- b723`S CORRIGENDUM ROW: at act_roots :%s in b680`s form; verify over it %s %s (%s); the repaired route`s '
                       'replay %s; b723`s root standing as recorded. SOURCE %s.' % (
                           f['rc_row'], f['rc_act'], f['rc_verify'], f['rc_why'].lower(), f['rc_replay'], sc['text']))
    seats.append(sc)
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('REGISTERED -- THE RESEARCH INSTRUMENTS REPRODUCED (tools/research/reproduce.py): %s rows, REPRODUCES %s, DIFFERS %s, NOT RUN '
                     '%s (%s), the planted controls as wanted %s of %s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr'],
                         sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE LEDGER SPLIT ((R334)(3)); THE LEGACY IMPORTS ((R334)(6));
    # ------------------------------------------------------------------ THE DRAFT
    sl = seat('%s_split_price.txt' % ACT, '**THE LEDGER SPLIT: ')
    keys['SPLIT'] = ('HELD -- THE LEDGER SPLIT: %s with its price, %s citation occurrences to move (%s in live tools), about %s h before a close '
                     'of %s h; %s. SOURCE %s.' % (
                         f['sl_word'].lower(), f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close'], f['sl_cut'].lower(), sl['text']))
    seats.append(sl)
    sg = seat('%s_legacy.txt' % ACT, '**THE LEGACY IMPORTS: ')
    keys['LEGACY'] = ('HELD -- THE LEGACY IMPORTS: carried with the remaining price, about %s h; %s sources scanned, %s carrying the previous name '
                      'in code (%s); nothing copied, legacy.py unchanged (%s names). SOURCE %s.' % (
                          f['lg_hours'], f['lg_sources'], f['lg_named'], f['lg_where'], f['lg_names'], sg['text']))
    seats.append(sg)
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['LV']), ('CERTIFIED', ['V140']), ('REGISTERED', ['TRIAGE', 'ROOTROW', 'REPRO']), ('HELD', ['SPLIT', 'LEGACY', 'HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b724 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
