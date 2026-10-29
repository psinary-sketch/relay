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
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,C2_HALT,C2_PRED,C2_REG,C2_SELECT,C3_RELAY,C3_RULE,C4_PRED,C4_RELAY,C6_CENSUS,C6_DRAFTS,C6_FROZEN,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
#⟪DEAD reg_gate ⟫
#⟪DEAD regspec ⟫
#⟪DEAD report ⟫
# Each "#⟪PENDING <tool> <names>⟫" line: names the act`s tool reads on routes carried from the act before that the act has
# still to write for itself; printed at every load; the act`s suite holds them empty at its seal.
#⟪PENDING checks B723_RUNS,C1_I76,C1_V130,C2_REPRINT,C2_WEED_PP,C3_PRED,C4_DIAL,C4_ONSET_TOOL,C4_SUPPORT,C4_ZETAK,C6_AXIOM,C6_RELAY⟫
#⟪PENDING citation ⟫
#⟪PENDING closing ⟫
#⟪PENDING record B723_RUNS,C1_I76,C1_V130,C2_LOCATOR,C2_WEED_PP,C3_PRED,C4_DIAL,C4_SUPPORT,C4_ZETAK,C6_AXIOM,C6_RELAY,REBUILD_COMMITS⟫
#⟪PENDING reg_gate ⟫
#⟪PENDING regspec B723_RUNS,C2_WEED_PP,REBUILD_COMMITS⟫
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
# ### b724, Component 7 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S AXIOM STEP. The template's three runner
# ### functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b724 ran five ((R334)(7), N1),
# ### rowed in data/b724_axiom_rows.json, whose free-memory figures are strings. Replaced for b724 alone; the arms' names and plants stand.
#⟪OVERRIDE checks 1126 1138⟫
def rebuild_wf_ok(S):
    """(R334)(7), b724: the workflow at each rebuild branch's tip -- the five kernels other than SIDE-frobenius carrying build-module.yml on
    main; SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's with b721's two lines (the push trigger to the branch, the
    target fixed) and nothing else, the hold kept; SIDE-kernel's tip carrying main's build-module.yml changed in the four places of its
    kdraft4_clear row and nothing else, the diff equal to that row's (the author's word (7)); no identifier of the author and no secret at
    either tip."""
    import difflib
    st = S['rebuild_state'] or {}
    fr, kn = st.get('SIDE-frobenius') or {}, st.get('SIDE-kernel') or {}
    src = read_blob(EF, 'HEAD:.github/workflows/build-module.yml') or ''
    tip = fr.get('wf_tip') or ''
    d = [x for x in difflib.unified_diff(src.split(NL), tip.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    km = read_blob('D:/SIDE-kernel', 'main:.github/workflows/build-module.yml') or ''
    kt = kn.get('wf_tip') or ''
    kd = [x for x in difflib.unified_diff(km.split(NL), kt.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    row = [r for r in (S['rebuild_rows'] or []) if r.get('kind') == 'kdraft4_clear' and r.get('kernel') == 'SIDE-kernel']
    want = [x for x in (row[-1].get('diff') or []) if x[:1] in '+-' and x[:3] not in ('+++', '---')] if row else None
    return all(v['wf_main'] for k, v in st.items() if k != 'SIDE-frobenius') and fr.get('wf_main') is False \
        and d == ['+  push: { branches: [%s] }' % K.REBUILD_BRANCH, '-      TARGET: ${{ inputs.target }}', '+      TARGET: SIDEFrobenius'] \
        and bool(kt) and bool(want) and kd == want and not any(w in (x or '').lower() for x in (tip, kt) for w in IDENT_WF) \
        and 'hold_mb: "2560"' in tip.lower()
#⟪END⟫
#⟪OVERRIDE checks 1141 1156⟫
def runner_ok(S):
    """(R334)(7), N1, b724: the axiom step read by its run ids -- one run per kernel repaired this act, five, each the worklist's B723_RUNS and
    its dispatch row's, each read once with the build exit read from its artifact: BUILDS, exit 0, no sorry warning; SIDE-frobenius's and
    SIDE-kernel's runs push-triggered; SIDE-kernel's three-place draft HALTED before its four-place draft CLEAR (the author's word (7));
    SIDE-lv-conservation not re-dispatched, its lv row reading the sorry's position; the bank's head figures equal to its rows, five axiom
    steps read success, its foot 6 OF 6 PINS."""
    t, rows = S['rebuild'] or '', S['rebuild_rows'] or []
    reads = dict((r['kernel'], r) for r in rows if r.get('kind') == 'read')
    disp = dict((r['kernel'], r) for r in rows if r.get('kind') == 'dispatch')
    runs = dict(K.B723_RUNS)
    kd = [r.get('kind') for r in rows if r.get('kernel') == 'SIDE-kernel' and (r.get('kind') or '').startswith('kdraft')]
    return sorted(reads) == sorted(disp) == sorted(runs) and all(str(reads[k]['run']) == str(runs[k]) == str(disp[k]['run']) for k in runs) \
        and all(r['verdict'] == 'BUILDS' and str(r['build_exit']) == '0' and str(r['sorry_warnings']) == '0' for r in reads.values()) \
        and sorted(k for k, r in disp.items() if r.get('via') == 'push') == ['SIDE-frobenius', 'SIDE-kernel'] and kd == ['kdraft_halt', 'kdraft4_clear'] \
        and any(r.get('kind') == 'lv' for r in rows) and 'SIDE-lv-conservation' not in disp \
        and 'COMMITTED 5 ; PUSHED 5 ; DISPATCHED 5 (six at most) ; READ 5' in t and t.count('the axiom step success') == 5 \
        and _verdict(t).startswith('THE AXIOM STEP AT 6 OF 6 PINS')
#⟪END⟫
#⟪OVERRIDE checks 1167 1167⟫
    for k, _r in K.B723_RUNS:
#⟪END⟫
#⟪OVERRIDE checks 1173 1173⟫
    return bool(mem) and all(int(r.get('free_mb') or 0) >= K.HOLD for r in mem) and order \
#⟪END⟫
# ### b724, Component 7 (the Edit tool): the corrigendum arm's event rows, written into the template as b723's fifteen; b723's record has nineteen
#⟪OVERRIDE checks 980 980⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 20)) \
#⟪END⟫
# ### b724, Component 7 (the Edit tool): G-RUNNER-READ's plant named b723's lv grade, which b724's axiom bank does not carry (the plant a
# ### no-op, the arm's POS passing); the plant now a push the head did not make
#⟪OVERRIDE checks 1686 1686⟫
     lambda S: runner_ok(S), lambda S: put(S, 'rebuild', (S['rebuild'] or '').replace('COMMITTED 5 ; PUSHED 5 ;', 'COMMITTED 5 ; PUSHED 4 ;'))),
#⟪END⟫
# ### b724, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file
#⟪OVERRIDE checks 1005 1005 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b724.py: sections ' in (rd('b724_fold.txt') or ''))) \
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
# ### b724, Component 7 (the Edit tool): the carried item (b) named b723's orders by hand; (R334)(3)(i) writes the open orders from
# ### tools/standing/orders.py's output, its count from the worklist (G-OFFSET-POST-HOC ties it to the bank's AT HEAD foot)
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: %d of %d at PLACE-papers main by tools/standing/orders.py`s rule (relay data/b724_orders.txt :282), the trail`s' % (WL.ORDERS[1], WL.ORDERS[0]),
    '        open-orders line written from the tool`s output ((R334)(3)(i)), none carried by hand; beside them',
#⟪END⟫
# ### b724, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b723's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b724_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b724_registration_%s.txt' % __import__('b724_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b724, Component 7 (the Edit tool): the carried row read "none: OPEN_TRAILS written by the trail at the close alone"; b724 landed
# ### (R334)(3)(ii)'s three closing lines (9e098548) and the author's word (5)'s dated line (70d9c0d0) before the seal, measured here
#⟪OVERRIDE regspec 78 78⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 'OTLINES', 'OTLINES', 'lines', '### (R334)(3)(ii) and the author`s word (5): 9e098548 and 70d9c0d0, no line rewritten; MEASURED off their numstat.'),
#⟪END⟫
# ### b724, Component 7 (the Edit tool): N1's dispatch commands are tools/b724_axiom.py's `dispatch <kernel>` route ((R334)(7)); the
# ### carried pattern named b723's rebuild tool, which b724 does not have (SIDE-frobenius's and SIDE-kernel's runs went on their pushes,
# ### read in the axiom rows bank by `via`)
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)'
                          r'|(^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b724_axiom\.py dispatch\b', re.M)
#⟪END⟫
# ### b724, Component 7 (the Edit tool): G-SCORER-READS-BANKS's needles named an earlier act's banks (the pin's rows, the derivation),
# ### which no b724 scorer reads; the needles set to the banks b724's N1-N4 read (the command bank and the axiom rows, H-SUPPORT's rule,
# ### the closed form's check, the seal and step banks), the ledger exclusion unchanged; the axiom rows' needle is the read's own form, since
# ### N1's printed label names the bank too (relay data/b724_c7_repair_controls.txt, the planted case)
#⟪OVERRIDE checks 903 904 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_axiom_rows.json' % ACT" in n and '_support_rule.txt' in n and '_c2_check.txt' in n \
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) at the seal, every one the seat's; (a')-(d') and (f')-(m') the seat's and (e') the navigator's, beyond the single letters this floor reads
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b724_corrigendum.txt', 'data/b724_standing_v130.txt', 'data/b724_fold.txt', 'data/b724_fold_run.txt',
                  'data/b724_i76.txt', 'data/b724_orders.txt', 'data/b724_orders_twenty.txt', 'data/b724_registrations.txt',
                  'data/b724_support_rule.txt', 'data/b724_zetak.txt', 'data/b724_support.txt', 'data/b724_dial_price.txt',
                  'data/b724_c2_closed_form.txt', 'data/b724_c2_check.txt', 'data/b724_axiom.txt', 'data/b724_axiom_rows.json',
                  'data/b724_split_price.txt', 'data/b724_reproduce.txt', 'data/b724_reproduce.json', 'data/b724_address_scan.txt',
                  'data/b724_author_words_preseal.txt', 'data/b724_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v8 binds b724 whole and v9 from d9739558 ((R334)(2)(v)), each read by G-SURGERY-CARRIED
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
        # ### (R334)(2)-(8), Component 7, the Edit tool, before the lock (b723's keys over b723's objects in git at b723's suite): the
        # ### registrations at their commit and at HEAD; the ancestry each arm reads; the orders and the twenty (3); the registrations, the rule
        # ### and the three computations (4)-(5); the closed form and its check (6); the axiom step and the split's price (7)-(8); v8 and v9;
        # ### the address scan (R333)(9); the reproduction run under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))), _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS))),
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('reg_rule', K.REG_COMMIT, K.C3_PRED), ('reg_zetak', K.REG_COMMIT, K.C4_ZETAK),
                                 ('pred_onsets', K.C3_PRED, K.C4_SUPPORT), ('tool_onsets', K.C4_ONSET_TOOL, K.C4_SUPPORT),
                                 ('reg_dial', K.REG_COMMIT, K.C4_DIAL), ('v9_v130', K.STANDING_COMMIT, K.C1_V130), ('v130_orders', K.C1_V130, K.C2_RELAY),
                                 ('orders_weed', K.C2_RELAY, K.C2_REPRINT), ('reg_c5', K.REG_COMMIT, K.C5_RELAY))),
        registrations=rd('b724_registrations.txt'), support_rule=rd('b724_support_rule.txt'), zetak=rd('b724_zetak.txt'),
        support=rd('b724_support.txt'), dial=rd('b724_dial_price.txt'), closed_form=rd('b724_c2_closed_form.txt'), c2_check=rd('b724_c2_check.txt'),
        orders=rd('b724_orders.txt'), twenty=rd('b724_orders_twenty.txt'), v130=rd('b724_standing_v130.txt'), fold_bank=rd('b724_fold.txt'),
        reproduce=rd('b724_reproduce.txt'), reproducej=jl('b724_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        address=rd('b724_address_scan.txt'), addr_live=_addr_live(), split=rd('b724_split_price.txt'),
        # ### the standing runner arms read THIS ACT'S axiom step ((R334)(7), N1: five runs, six at most): its bank, its rows, each wave 1
        # ### kernel's rebuild-b721 branch, main and tags (b723's carry named data/b723_rebuild.txt, which no act wrote)
        rebuild=rd('b724_axiom.txt'), rebuild_rows=json.loads(rd('b724_axiom_rows.json') or '[]'), rebuild_state=_rebuild_state(),
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c2pp=_ct(PP, K.C2_PP), reg=_ct(ROOT, K.REG_COMMIT),
               pred=_ct(ROOT, K.C3_PRED), zetak=_ct(ROOT, K.C4_ZETAK), support=_ct(ROOT, K.C4_SUPPORT), dial=_ct(ROOT, K.C4_DIAL),
               c5=_ct(ROOT, K.C5_RELAY), c6=_ct(ROOT, K.C6_RELAY), v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS),
               actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   c2=files_of(ROOT, K.C2_RELAY), c2pp=files_of(PP, K.C2_PP), weedpp=files_of(PP, K.C2_WEED_PP), reprint=files_of(ROOT, K.C2_REPRINT),
                   pred=files_of(ROOT, K.C3_PRED), zetak=files_of(ROOT, K.C4_ZETAK), onset_tool=files_of(ROOT, K.C4_ONSET_TOOL),
                   support=files_of(ROOT, K.C4_SUPPORT), dial=files_of(ROOT, K.C4_DIAL), c5=files_of(ROOT, K.C5_RELAY), v9=files_of(ROOT, K.STANDING_COMMIT),
                   c6=sorted(set(f for c in K.C6_AXIOM for f in files_of(ROOT, c))),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b724's read-first bank's items by path, as its step zero wrote them (Component 7, the Edit tool, before the lock: the carried needles
# ### were b723's items)
READFIRST_NEEDLES = ('relay data/b723_closing.txt |', 'relay data/b723_events.txt |', 'relay data/b723_defects.txt |',
                     'relay data/b723_axiom_diag.txt |', 'relay data/b707_onset.txt |', 'relay data/b709_grid.txt |', 'relay data/b711_list.json |',
                     'PLACE-papers FINDINGS.md | :5667 |', 'PLACE-papers FINDINGS.md | :10206 |', 'PLACE-papers OPEN_TRAILS.md | :14680 |',
                     'PLACE-papers OPEN_TRAILS.md | :16250 |', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md | :2982 |',
                     'relay data/b680_split_price.txt |', 'relay data/b724_ferry.txt | whole |', 'relay data/b724_ferry_addendum.txt | whole |',
                     'relay data/standing_clauses_v8.txt |', 'relay data/b723_steps.json |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R334)(1)-(2))', 'OPEN ORDERS ((R334)(3))', 'REGISTRATIONS ((R334)(4))',
                    'COMPUTATIONS ((R334)(5))', 'C2 CLOSED FORM ((R334)(6))', 'AXIOM STEP ((R334)(7))', 'LEDGER SPLIT ((R334)(8))',
                    'NAME AND ADDRESS ((R333)(9))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (60 = 60 + 0: no miss in the banking run, the dry run's three each
    the seat's own new row, repaired before it -- data/b724_readfirst.txt :5-:8); the bank written before the step-zero banks' commit and that
    commit before Component 1's (Component 7, the Edit tool: the carried 90 = 88 + 2 were b723's own)."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 60 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 7, the Edit tool, before the lock: the carried needles were b720's figures under b723's name)
    return landed(S, 0, ['b723 AT ITS WEIGHT', 'suite 110 of 117; root 0d26295f7b567e20…', 'the closing’s 1607e994', '31 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### Component 7, before the lock, the Edit tool: b724's title in the ferry's Component 7 form adjusted to what the act did (the record
# ### tool's _title over the banks), cut at its objects; the carried needles were b723's
TITLE_NEEDLES = ('## the close tools at v1.3.0 and five repeat classes repaired', '; the open orders generated, 143 open, the twenty read',
                 '; H-SUPPORT at three zeros REFUTED, H-ZETAK HELD, H-DIAL carried', '; the C2 closed form written and checked post hoc',
                 '; the axiom step at 6 of 6 pins', '; the ledger split carried')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R334)(2): the generated entry for b723's nineteen events and thirty-one defects landed (its line in the bank, the title at that line
    through conv): the events by row (1)-(19), the defects by the one lettering ((a)-(z), (a`)-(e`)), no memory item; every item tagged CLAIM
    or CLOSE and NEW or REPEAT, the tags summing (CLAIM 4, CLOSE 46 over 50, REPEAT 25); the CLAIM items defects (f), (k), (w) and (x); the
    repairs at tools/standing/ v1.3.0 with their 68 cases; the corrigenda bank appended at row (43) and nothing before it changed; in
    Component 1's commit (Component 7, the Edit tool, before the lock: the carried figures were b723's corrigendum's, of b721's record)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 31 and len(items) == j.get('items') == 50 and j.get('row') == 43 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 50 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 4 and claims == ['f', 'k', 'w', 'x'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 25 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.3.0' and (j.get('repairs') or {}).get('cases') == 68 \
        and '  (43) ' in S['corrigenda'] and '  (44) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b724_rules.txt and data/b724_rules.txt, by form in (R334)(9)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (Component 7, the Edit tool: the line above is b723's, carried); no author's word of b724 orders a row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b724_rules.txt')) and not os.path.exists(os.path.join(D, 'b724_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b724's keys, the report sections' own heads (Component 7, the Edit tool, before the lock; b723's carried till then)
REPORT_KEYS = ('KERNEL -- THE AXIOM STEP AT THE SIX WAVE 1 PINS', 'CERTIFIED -- H-ZETAK ON Q0`S TWO ONSET WINDOWS',
               'CERTIFIED -- THE C2 CLOSED FORM, CHECKED POST HOC', 'REGISTERED -- H-SUPPORT AT Q0', 'REGISTERED -- H-DIAL',
               'REGISTERED -- THE OPEN ORDERS GENERATED', 'HELD -- THE LEDGER SPLIT',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over THIS ACT'S axiom step ((R334)(7), data/b724_axiom_rows.json; Component 7, the Edit tool): every push, dispatch and read
    row with the host's free memory at or above the hold (each figure read as an integer: the rows carry strings); per kernel run this act
    (K.B723_RUNS, five; SIDE-lv-conservation ran clean at b721 and was not re-dispatched) its push before its run and its run before its read;
    the dispatches five, at most the six N1 allows, two of them push-triggered (rowed `via` push); the capture running the axiom tool's push and
    dispatch routes, b723's rebuild tool not at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b724_axiom\.py (push|dispatch|kcommit|commit)\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b72[12]_rebuild\.py (push|dispatch|push_run|plan)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == len(K.B723_RUNS) <= K.MAX_DISPATCHES == 6 \
        and sorted(r['kernel'] for r in rows if r.get('kind') == 'dispatch' and r.get('via') == 'push') == ['SIDE-frobenius', 'SIDE-kernel'] \
        and bool(S['cmds']) and bool(cmds) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b724 axiom seat <b724-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS and OPEN_TRAILS; (R334)(8)'s archive-3 files not written, the
    split carried), both ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b724's headings and banks, as its _finding_text writes them (Component 7, the Edit tool, before the lock; b723's carried till then)
ENTRY_NEEDLES = ('**The corrigendum and the repeat classes**', '**The open orders**', '**The registrations**', '**H-ZETAK**', '**H-SUPPORT**',
                 '**H-DIAL**', '**The C2 closed form**', '**The axiom step at the six pins**', '**The ledger split**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b724_corrigendum.txt', 'data/b724_standing_v130.txt', 'data/b724_orders.txt', 'data/b724_orders_twenty.txt',
                 'data/b724_registrations.txt', 'data/b724_zetak.txt', 'data/b724_support.txt', 'data/b724_dial_price.txt',
                 'data/b724_c2_closed_form.txt', 'data/b724_c2_check.txt', 'data/b724_axiom.txt', 'data/b724_split_price.txt',
                 'data/b724_address_scan.txt', 'data/b724_touch.txt', 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b724: no single-letter row the navigator's; (e'), (R334)(2)'s "at step zero" against the ferry's order, the navigator's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R334)(4), N2 (Component 7, the Edit tool, over b724's objects): data/b724_registrations.txt committed alone at REG_COMMIT (its one file,
    the step bank aside), its text at HEAD its blob there, its foot naming no zero and no figure at a registered object; that commit an
    ancestor of H-SUPPORT's rule output and predictions (C3_PRED), of H-ZETAK's bank (C4_ZETAK), of H-DIAL's price (C4_DIAL) and of the closed
    form (C5_RELAY); the predictions' commit carrying the rule's bank and no onset bank, its foot ONSETS COMPUTED 0, and an ancestor of the
    onsets' commit (C4_SUPPORT), the onset tool committed before it; each figure bank printing its controls before its figures; the earlier
    acts' registrations at HEAD their blobs at their commits."""
    reg, z, s, p = S['registrations'] or '', S['zetak'] or '', S['support'] or '', S['support_rule'] or ''
    return _own(S['files']['reg']) == [K.REGISTRATIONS] and S['reg_now'][0] is not None and S['reg_now'][0] == S['reg_now'][1] \
        and 'ZEROS NAMED 0 ; FIGURES AT A REGISTERED OBJECT 0' in _verdict(reg) \
        and all(S['anc'].get(k) is True for k in ('reg_rule', 'reg_zetak', 'reg_dial', 'reg_c5', 'pred_onsets', 'tool_onsets')) \
        and 'data/b724_support_rule.txt' in S['files']['pred'] and 'data/b724_support.txt' not in S['files']['pred'] \
        and 'ONSETS COMPUTED 0' in _verdict(p) and 'data/b724_support.txt' in S['files']['support'] \
        and _ctl_first(z, '## (C1) ', '## THE zeta_K FORM AT EACH WINDOW') and _ctl_first(s, '## (C1) ', '## THE ZEROS, IN THE RULE`S ORDER') \
        and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R333)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 7, the Edit tool): tools/b724_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address and name read from history and held in memory -- the address 0, the author's name 0, the previous name 0, its
    four controls as wanted (the second name arm added at Component 1, d0ee06a8); the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R334)(5), N3 (the name the frozen run list carries; Component 7, the Edit tool, over b724's objects): each registered hypothesis graded
    at its bank's end in (R334)(5)'s words, the grade the bank's last line -- H-ZETAK HELD, its controls C1 and C2 as wanted and C3 holding;
    H-SUPPORT REFUTED, C1 as wanted, its zeros three, its falsifier fired; H-DIAL carried, not run, no figure at F_c, its registration
    committed -- each bank in its own commit (C4_ZETAK, C4_SUPPORT, C4_DIAL)."""
    last = lambda t: ((t or '').rstrip(NL).split(NL) or [''])[-1]
    z, s, d = last(S['zetak']), last(S['support']), last(S['dial'])
    return z.startswith('### ### **H-ZETAK: C1 AS WANTED ; C2 AS WANTED ; C3 HOLDS ;') and z.endswith('THE HYPOTHESIS HELD ; 17 s.**') \
        and s.startswith('### ### **H-SUPPORT: C1 AS WANTED ; ZEROS 3 ;') and s.endswith('FALSIFIER FIRED ; THE HYPOTHESIS REFUTED.**') \
        and d.startswith('### ### **H-DIAL: BUILD PRICED ') and d.endswith('FIGURES AT F_c 0 ; NOT RUN ; CARRIED, ITS REGISTRATION COMMITTED.**') \
        and 'data/b724_zetak.txt' in S['files']['zetak'] and 'data/b724_support.txt' in S['files']['support'] \
        and 'data/b724_dial_price.txt' in S['files']['dial']
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R334)(6), N3 (the name the frozen run list carries; Component 7, the Edit tool, over b724's objects): the C2 closed form written as a
    derivation and its check POST HOC wherever named -- every row of the check led POST HOC, the rows the foot's count, each REPRODUCED; the
    planted e_p failing to reproduce, as wanted; the derivation's foot CHECKED POST HOC and NOT COMPILED; both banks and the check's tool in
    Component 5's commit (C5_RELAY), the registrations' commit its ancestor."""
    c, k = S['closed_form'] or '', S['c2_check'] or ''
    rows = re.findall(r'(?m)^  POST HOC  D\s+(-\d+) .*\| (REPRODUCED|DIFFERS|FAILS TO REPRODUCE)$', k)
    lead = re.findall(r'(?m)^  (\S+(?: \S+)?)\s+D\s+-\d+ \(', k)
    f = re.search(r'ROWS (\d+), REPRODUCED (\d+) ;', _verdict(k))
    return 'C1 (PLANTED e_p) FAILS, AS WANTED' in _verdict(k) and 'FAILS TO REPRODUCE, AS WANTED' in k and bool(f) \
        and int(f.group(1)) == len(rows) == len(lead) == 19 and set(lead) == {'POST HOC'} \
        and int(f.group(2)) == sum(1 for r in rows if r[1] == 'REPRODUCED') == 19 \
        and 'CHECKED POST HOC' in _verdict(c) and 'NOT COMPILED' in _verdict(c) and 'EVERY ROW IS POST HOC' in k \
        and all(x in S['files']['c5'] for x in ('data/b724_c2_closed_form.txt', 'data/b724_c2_check.txt', 'tools/b724_c2_check.py')) \
        and S['anc'].get('reg_c5') is True
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R334)(3), N2 (the name the frozen run list carries; Component 7, the Edit tool, over b724's orders): the open orders generated by
    tools/standing/orders.py (C2_RELAY, v1.3.0's commit its ancestor) -- the rule printed before the orders, each order once, the first foot
    the rows' counts at 763ae914; the controls 6 of 6 as wanted; at HEAD (after the author's word (5)'s weed, C2_REPRINT) the worklist's
    193, 143 open, 50 closed; the twenty each against its trigger, the foot's counts summing to twenty; the closing lines on OPEN_TRAILS in
    C2_PP and C2_WEED_PP, OPEN_TRAILS the one file in each."""
    o, w = S['orders'] or '', S['twenty'] or ''
    rows = re.findall(r'(?m)^  (W-ORD-[\w-]+)\s+entry :\d+\s+(OPEN|CLOSED)\s', o)
    a = re.search(r'\*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', o)
    h = re.search(r'\*\*AT HEAD: ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', o)
    tw = re.search(r'\*\*THE TWENTY: TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) \(ACTED THIS ACT (\d+), PRICED AND NAMED (\d+)\) ; '
                   r'DISCHARGED BY READING (\d+) ; OFFERED FOR RETIRE (\d+) ;', w)
    rule, first = o.find('### THE RULE '), o.find('## THE ORDERS ')
    tg = [int(x) for x in tw.groups()] if tw else [0] * 6
    return 0 <= rule < first and bool(a) and len(set(r[0] for r in rows)) == len(rows) \
        and [int(x) for x in a.groups()] == [len(rows), sum(1 for r in rows if r[1] == 'OPEN'), sum(1 for r in rows if r[1] == 'CLOSED')] \
        and bool(h) and (int(h.group(1)), int(h.group(2)), int(h.group(3))) == tuple(K.ORDERS) and K.ORDERS[0] == len(rows) == K.ORDERS[1] + K.ORDERS[2] \
        and '**THE ORDERS` CONTROLS: CASES 6 ; AS WANTED 6 ; ALL AS WANTED.**' in o \
        and bool(tw) and tg[0] + tg[1] + tg[4] + tg[5] == 20 and tg[2] + tg[3] == tg[1] \
        and all(S['anc'].get(k) is True for k in ('v130_orders', 'orders_weed')) and 'tools/standing/orders.py' in S['files']['c2'] \
        and 'data/b724_orders_twenty.txt' in S['files']['c2'] and 'data/b724_orders.txt' in S['files']['reprint'] \
        and S['files']['c2pp'] == ['OPEN_TRAILS.md'] and S['files']['weedpp'] == ['OPEN_TRAILS.md']
#⟪END⟫
#⟪SECTION checks 36⟫
    """(R334)(2)(v), the name the frozen run list carries (Component 7, the Edit tool, over b724's v9): v9 at VERSION 9, v8's rows (1)-(82)
    in it in order line for line and v8 at HEAD its blob at the act's base; row (83) alone beyond them, its clause the ferry's own words (the
    whitespace folded); the foot ROWS 83 with v8's 82 unchanged; its commit (STANDING_COMMIT) the one file, the text at HEAD its blob there,
    an ancestor of v1.3.0's commit."""
    v9, v8 = S['v9'] or '', S['v8'] or ''
    rows = lambda t: [l for l in t.replace('\r', '').split(NL) if re.match(r'^  \(\d+\) |^      \S', l)]
    r8, r9 = rows(v8), rows(v9)
    fer = ' '.join((S['ferry'] or '').replace('’', "'").split())
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and len(r8) >= 164 and r9[:len(r8)] == r8 and len(r9) == len(r8) + 2 \
        and r9[-2].startswith('  (83) ') and r9[-1].strip().replace('’', "'") in fer and 'ROWS 83 ; v8`S ROWS 82 UNCHANGED' in _verdict(v9) \
        and S['files']['v9'] == [K.DATA_STANDING_V9] and _s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V9)) \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """(R334)(2)(iv): no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED
    as b723 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED left the arm list itself at v1.3.0
    (be821907) with the reader (R333)(2)(iii) retired; this suite's run list 116 arms, no standing arm added (Component 7, the Edit tool)."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R334)(7)-(8), the name the frozen run list carries (Component 7, the Edit tool, over b724's axiom step and split): the axiom step at
    6 of 6 pins -- the head COMMITTED, PUSHED, DISPATCHED and READ each the worklist's B723_RUNS (five, six at most), HALTED 0, the sixth pin
    SIDE-lv-conservation clean at b721, NO MAIN OR TAG TOUCHED; the ledger split carried whole to b724 with its price, NOTHING CUT; both banks
    in Component 6's commits (C6_AXIOM)."""
    a, sp, n = _verdict(S['rebuild']), _verdict(S['split']), len(K.B723_RUNS)
    return n == 5 and ('COMMITTED %d ; PUSHED %d ; DISPATCHED %d (six at most) ; READ %d' % (n, n, n, n)) in (S['rebuild'] or '') \
        and a.startswith('THE AXIOM STEP AT 6 OF 6 PINS (5 REPAIRED AND RUN THIS ACT, SIDE-lv-conservation CLEAN AT b721) ; HALTED 0 (none) ; RUNS 5 ;') \
        and a.endswith('NO MAIN OR TAG TOUCHED.') and sp.startswith('THE LEDGER SPLIT: CARRIED WHOLE TO b724 WITH ITS PRICE') and sp.endswith('NOTHING CUT.') \
        and all(x in S['files']['c6'] for x in ('data/b724_axiom.txt', 'data/b724_axiom_rows.json', 'data/b724_split_price.txt', 'tools/b724_axiom.py'))


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b723's (R333)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at its last commit (C1_I76) and the working tree's."""
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
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (K.C1_I76, tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')
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
    # ### Component 8, the Edit tool: b724's ferry names no "standing clauses v<N>" outside a file name (it names data/standing_clauses_v8.txt
    # ### and v8 by row), so the carried `7 in named` read nothing; v7 is read by its bytes below and v8 by G-SURGERY-CARRIED
    return 'RULING (R334) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from 1607e994',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b723's standing arm, carried in the run list of 116 (Component 7, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R333)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows` (68: 64, 0, 4); the tool at its last commit 82e62fd7',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 60 = 60 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b723-closing (1607e994)', 'push-b723-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the close tools at v1.3.0 and five repeat classes repaired; the open orders generated, 143 open, the twenty read; H-SUPPORT at three zeros REFUTED, H-ZETAK HELD, H-DIAL carried; the C2 closed form written and checked post hoc; the axiom step at 6 of 6 pins; the ledger split carried), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R334)(1)-(2): the generated corrigendum for b723`s record, landed at FINDINGS :11401: its nineteen events and thirty-one defects, 50 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 4 CLOSE 46, REPEAT 25; v1.3.0`s repairs, 68 cases; the corrigenda bank appended at row (43)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b724 and no b724 rules bank; (R334)(2)(v)`s row stands in v9)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b724's objects (Component 7, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R334)(4), N2: data/b724_registrations.txt committed alone at 9ad26421, at HEAD its blob there, naming no zero and no figure; an ancestor of H-SUPPORT`s rule output and predictions (0e91c670, no onset there, ONSETS COMPUTED 0), of H-ZETAK`s bank (23f54c74), of H-DIAL`s price (ca2c6a9d) and of the closed form (cdc46c59); the onsets (1530d2f2) after the predictions and the onset tool; each figure bank`s controls before its figures',
     lambda S: registrations_first_ok(S), lambda S: put(S, 'support_rule', (S['support_rule'] or '').replace('ONSETS COMPUTED 0', 'ONSETS COMPUTED 1'))),
    ('G-PREDICTION-FIRST', '(R333)(9)(i), N5, the scan arm: tools/b724_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, the bank`s counts the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R334)(5), N3: each registered hypothesis graded at its bank`s end in (R334)(5)`s words -- H-ZETAK HELD (C1, C2 as wanted, C3 holds); H-SUPPORT REFUTED at three zeros (C1 as wanted, the falsifier fired); H-DIAL carried, not run, no figure at F_c -- each bank in its own commit',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'zetak', (S['zetak'] or '').replace('THE HYPOTHESIS HELD', 'THE HYPOTHESIS REFUTED'))),
    ('G-DERIVATION-GRADED', '(R334)(6), N3: the C2 closed form written as a derivation, NOT COMPILED; its check POST HOC wherever named -- every one of the 19 rows led POST HOC and REPRODUCED, the foot`s count the rows`; the planted e_p failing to reproduce, as wanted; both banks and the check`s tool in cdc46c59, the registrations` commit its ancestor',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'c2_check', (S['c2_check'] or '').replace('  POST HOC  D   -20 ', '  COMPUTED  D   -20 '))),
    ('G-OFFSET-POST-HOC', '(R334)(3), N2: the open orders generated by tools/standing/orders.py (709ba3eb, after v1.3.0`s be821907): the rule before the orders, each order once, the first foot the rows` (193: 147 open, 46 closed at 763ae914); the controls 6 of 6; at HEAD after the weed (9c026ef7) 193, 143 open, 50 closed; the twenty`s foot summing to twenty; OPEN_TRAILS alone in 9e098548 and 70d9c0d0',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'orders', (S['orders'] or '').replace('**AT HEAD: ORDERS 193 ; OPEN 143', '**AT HEAD: ORDERS 193 ; OPEN 144'))),
    ('G-SURGERY-CARRIED', '(R334)(2)(v): v9 at VERSION 9 -- v8`s rows (1)-(82) line for line, v8 at HEAD its blob at 1607e994; row (83) alone beyond them, its clause the ferry`s own words; the foot ROWS 83; committed alone at d9739558, at HEAD its blob there, before v1.3.0`s commit',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', '(R334)(2)(iv): no arm retired through tools/standing/arms.py this act -- the file byte-equal at 1607e994, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R334)(7)-(8): the axiom step at 6 of 6 pins -- five runs committed, pushed, dispatched and read by their ids (six at most), HALTED 0, SIDE-lv-conservation clean at b721, no main or tag touched; the ledger split carried whole to b724 with its price, nothing cut; both in Component 6`s commits',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'split', (S['split'] or '').replace('NOTHING CUT.', 'ONE FILE CUT.'))),
    ('G-DIFFERS-ERRATA', '(R334)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal at 1553808a, no b724 differs or errata bank, the worklist naming none; the weight line and the corrigendum in Component 1`s PLACE-papers commit 763ae914, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9 ((R334) Component 7), N4: data/b724_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R334-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b723`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 1607e994 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R334)(7): the axiom step`s five runs, one per repaired wave 1 kernel, each read once by its id -- BUILDS, exit 0, no sorry; SIDE-frobenius and SIDE-kernel by push, SIDE-kernel`s halt and its four-place clear on the author`s word (7) with the diff; the lv row; the head COMMITTED 5 ; PUSHED 5 ; DISPATCHED 5 ; READ 5 and the step at 6 of 6 pins',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: the axiom step`s order and hold -- free memory at or above 2,560 MB at every push, dispatch and read; per kernel push before run before read; five dispatches, six at most, by tools/b724_axiom.py alone; no b721 or b723 rebuild route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 beyond its pin by the b724 axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the two ledgers alone (FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b723`s trail record on OPEN_TRAILS (:16310) and its root in the chain', lambda S: '### b723 — lane two, act one hundred and forty-nine, the instruments act under (R333)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b723`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: (R334)(7)`s five by tools/b724_axiom.py, read by their ids in data/b724_axiom.txt; -1 the command bank not yet written)' % (
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
tool, Component 7) are the corrigendum and v1.3.0's repeat-class repairs, the open orders and the twenty, the registrations, the three
computations (H-ZETAK, H-SUPPORT, H-DIAL), the C2 closed form and its post hoc check, the axiom step at the six pins, the ledger split's price,
the name and address scan, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R334)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for b724 ((R334)(11)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act on their rebuild-b721 branches alone ((R334)(7)): one commit each at five pins, no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b724 ((R334)(11)); the open orders by tools/standing/orders.py's output and not a hand list ((R334)(3)(i))
    (Component 7, the Edit tool)."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b724 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY, THE CHECKPOINT ACT: THE CLOSE TOOLS AT v1.3.0 AND FIVE '
              'REPEAT CLASSES REPAIRED; THE OPEN ORDERS GENERATED, 143 OPEN, THE TWENTY READ; H-SUPPORT AT THREE ZEROS REFUTED, H-ZETAK HELD, '
              'H-DIAL CARRIED; THE C2 CLOSED FORM WRITTEN AND CHECKED POST HOC; THE AXIOM STEP AT 6 OF 6 PINS; THE LEDGER SPLIT CARRIED, UNDER (R334).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 7, the Edit tool; b723's sections over b723's objects not carried). A row of two
    reads its bank's verdict line by vtail; a row of three reads the line its pattern names (a bank with several verdict lines, or written by
    the Write tool without the verdict line's form)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.3.0: the seven close tools folded and the repeat classes repaired, each controlled on b723`s banks',
                 'b724_standing_v130.txt'),
                ('the fold built: each tool a template and the act`s sections (tools/acts/b724.py)', 'b724_fold.txt',
                 r'(?m)^  tools/acts/b724\.py: [^\n]*'),
                ('the repeat rule, standing clauses v9 row (83): v8`s rows unchanged and the one row (d9739558)', 'standing_clauses_v9.txt',
                 r'(?m)ROWS 83 ; v8`S ROWS 82 UNCHANGED[^;]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE OPEN ORDERS ((R334)(3))', [
                ('tools/standing/orders.py at 763ae914, the rule printed before the orders', 'b724_orders.txt', r'(?m)\*\*ORDERS \d+ ; OPEN \d+ ; CLOSED \d+ ;'),
                ('the orders` controls', 'b724_orders.txt', r'(?m)\*\*THE ORDERS` CONTROLS:[^*]*'),
                ('the locator reading tried on the author`s ruling (3)', 'b724_orders.txt', r'(?m)\*\*THE LOCATOR READING:[^*]*'),
                ('at HEAD after the author`s word (5)`s weed', 'b724_orders.txt', r'(?m)\*\*AT HEAD:[^*]*'),
                ('the twenty of (R333)(14), each against its trigger as written', 'b724_orders_twenty.txt')]),
            ('THE REGISTRATIONS ((R334)(4))', [
                ('H-SUPPORT, H-ZETAK and H-DIAL committed alone at 9ad26421 before any figure at an object they name', 'b724_registrations.txt'),
                ('H-SUPPORT`s rule output and predictions by a commit of their own (0e91c670), before any onset', 'b724_support_rule.txt')]),
            ('THE COMPUTATIONS ((R334)(5))', [
                ('H-ZETAK: zeta_K on Q0`s two onset windows, the controls first, the grade at the end', 'b724_zetak.txt'),
                ('H-SUPPORT: the onsets at the zeros the rule named, the controls first, the grade at the end', 'b724_support.txt'),
                ('H-DIAL: the build priced, not run, carried with its registration', 'b724_dial_price.txt')]),
            ('THE C2 CLOSED FORM ((R334)(6))', [
                ('the closed form written as a derivation, not compiled', 'b724_c2_closed_form.txt'),
                ('its check against the coefficient banks of b711-b723, every row POST HOC', 'b724_c2_check.txt')]),
            ('THE AXIOM STEP ((R334)(7))', [
                ('the six wave 1 pins: five repaired and run by their ids on the rebuild-b721 branches, SIDE-lv-conservation clean at b721', 'b724_axiom.txt')]),
            ('THE LEDGER SPLIT ((R334)(8))', [
                ('the split`s budget printed before any cut', 'b724_split_price.txt')]),
            ('THE NAME AND ADDRESS ((R333)(9))', [
                ('the scan over every commit and bank of the act, the previous address and name held in memory, the counts alone', 'b724_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b723`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b724_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: on the rebuild-b721 branches alone ((R334)(7)) -- one commit each by the b724 axiom seat`s neutral identity at',
    '    SIDE-archimedean, SIDE-rcurve, SIDE-spinor, SIDE-frobenius and SIDE-kernel (SIDE-kernel`s fourth line on the author`s word (7), its',
    '    diff printed before the commit), each pushed and run once, read by its run id ; SIDE-lv-conservation clean at b721, not run ; no',
    '    kernel`s main touched, no tag cut (N5) ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, the challenge branch',
    '    challenge-b720-h2-sign-iff-rh standing ; the pin-b718-de5ce8a9 branches left as banked ; port-b707 of SIDE-lv-conservation at',
    '    b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main and its deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host, the runner dispatches',
    '    (R334)(7)`s five alone (six at most), each read by its id ; free memory read before each computation, push, dispatch and read ;',
    '    the push-b723-* branches of relay and PLACE-papers deleted at step zero by name after --merged listed them, one per command and each',
    '    its own message ; nothing vendored ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file and the',
    '    earlier acts` units files untracked ; N2: the registrations committed alone at 9ad26421 before any figure bank, H-SUPPORT`s rule',
    '    output and predictions at 0e91c670 before any onset, each tool`s controls printed before its figures ; N3: every grade at its bank`s',
    '    end, the C2 closed form`s check labelled POST HOC wherever named ; (R333)(9): no new occurrence of the author`s name or address in',
    '    anything the act wrote, committed or pushed (relay data/b724_address_scan.txt), the commits under the GitHub login and its noreply',
    '    address ; no identifier of the author in any outbound request header, URL, input or payload, or in any workflow file ; no secret',
    '    added ; the seat`s plain requests to github.com (its git reads, pushes, dispatches and run reads) the act`s outbound calls ; the',
    '    deposit route untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS (the weight line, the',
    '    corrigendum, the entry) and OPEN_TRAILS (the closing lines of (R334)(3), the trail) appended ; no paper cut, moved or renamed, the',
    '    ledger split carried whole ((R334)(8)) ; no ERRATA, FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt and the',
    '    corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.3.0 by',
    '    (R334)(2), the seven close tools folded ; data/standing_clauses_v9.txt by a commit of its own ((R334)(2)(v)) ; the hook in',
    '    D:/.claude/settings.json unedited ; the per-act tools of b698-b723 unedited ; the mirror zip written outside every repository over',
    '    the roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ;',
    '    nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R334)(13)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        the twenty of (R333)(14) each against its trigger (relay data/b724_orders_twenty.txt): W-ORD-LEDGER-SPLIT-RESOLVER acted (the',
    '        split priced and carried), five priced and named, W-ORD-PROBE-HOLD discharged by reading, W-ORD-STATUS-CELLS offered for retire',
    '        at the root`s prompt; four moved to CLOSED at HEAD by their closing lines (PROBE-HOLD, Q0-ZEROS-443, READING5-INDEPENDENCE, and',
    '        E1-CFG on the author`s word (5)).',
    '    (c) For b724, each from its bank: H-DIAL`s build as priced, its registration committed (relay data/b724_dial_price.txt); the ledger',
    '        split carried whole with its price (relay data/b724_split_price.txt); the lv sorry`s discharge, not available as stated (relay',
    '        data/b724_axiom.txt), its course the author`s at the root`s prompt; the reproduction`s NOT RUN rows I-56, I-57, I-61, I-107 (relay',
    '        data/b724_reproduce.txt); the C2 compile where the author names it from b723`s price; the report tool outside the sealed list;',
    '        the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); challenge-b720-h2-sign-iff-rh of',
    '        SIDE-explicit-formula; the pin-b718-de5ce8a9 branches as banked; the rebuild-b721 branches of the wave 1 kernels, five carrying',
    '        b724`s axiom commit.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, five rebuild-b721 branches carrying b724`s axiom commit ((R334)(7)), no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b724: the standing repairs are v1.3.0's ((R334)(2), relay data/b724_standing_v130.txt, read in the corrigendum section); the
    # ### carry's diffs here (b724 carried at step zero before the fold; its tools since are the templates and tools/acts/b724.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act, one commit each on '
          'the %s branches of five wave 1 kernels ((R334)(7)); SIDE-lv-conservation`s main untouched, port-b707 at b712`s tip %s, its checkout at main '
          'for this read)' % (len(ks), K.JOIN_NEW_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b724's form over b724's objects (Component 7, the Edit tool; b723's form in git at b723's record tool): the corrigendum's foot and v1.3.0's
    controls; the orders at HEAD, their controls and the twenty; the registrations and H-SUPPORT's rule; H-ZETAK, H-SUPPORT and H-DIAL at their
    feet; the C2 closed form and its check, post hoc; the axiom step; the ledger split; the reproduction run; the address scan; each by its own
    lines through _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v3 = _bfig('%s_standing_v130.txt' % ACT, r'\*\*v1\.3\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ;', 'v1.3.0`s controls')
    od = _bfig('%s_orders.txt' % ACT, r'\*\*AT HEAD: ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ; STATUS MOVED FROM ([0-9a-f]+) (\d+)\.\*\*', 'the orders at HEAD')
    oc = _bfig('%s_orders.txt' % ACT, r'\*\*THE ORDERS` CONTROLS: CASES (\d+) ; AS WANTED (\d+) ;', 'the orders` controls')
    tw = _bfig('%s_orders_twenty.txt' % ACT, r'\*\*THE TWENTY: TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) \(ACTED THIS ACT (\d+), PRICED AND NAMED (\d+)\) ; '
               r'DISCHARGED BY READING (\d+) ; OFFERED FOR RETIRE (\d+) ;', 'the twenty`s foot')
    rg = _bfig('%s_registrations.txt' % ACT, r"\*\*REGISTERED: ([^;]+) ; ZEROS NAMED (\d+) ; FIGURES AT A REGISTERED OBJECT (\d+) ;", 'the registrations` foot')
    sr = _bfig('%s_support_rule.txt' % ACT, r'\*\*H-SUPPORT`S RULE: ZEROS READ (\d+) ; BANKED EXCLUDED (\d+) OF (\d+) ; WITHIN REACH (\d+) ; SELECTED (\d+) ; '
               r'CONTINUES INTO -15/-39 (\w+) ; ONSETS COMPUTED (\d+)\.\*\*', 'H-SUPPORT`s rule`s foot')
    zk = _bfig('%s_zetak.txt' % ACT, r'\*\*H-ZETAK: C1 ([^;]+) ; C2 ([^;]+) ; C3 (\w+) ; rho0 ([^;]+) ; band ([^;]+) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE) ;',
               'H-ZETAK`s foot')
    sp = _bfig('%s_support.txt' % ACT, r'\*\*H-SUPPORT: C1 ([^;]+) ; ZEROS (\d+) ; ONSETS COMPUTED (\d+) ; WITHIN 0\.03 (\d+) ; BEYOND REACH (\d+) ; '
               r'FALSIFIER (FIRED|NOT FIRED) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*', 'H-SUPPORT`s foot')
    dl = _bfig('%s_dial_price.txt' % ACT, r'\*\*H-DIAL: BUILD PRICED \(([^)]*)\) ; FIGURES AT F_c (\d+) ; (NOT RUN|RUN) ; (CARRIED[^.]*)\.\*\*', 'H-DIAL`s foot')
    cf = _bfig('%s_c2_closed_form.txt' % ACT, r'\*\*THE C2 CLOSED FORM: WRITTEN AS A DERIVATION, (\w+) STEPS ; CHECKED POST HOC, (\d+) ROWS OF (\d+) '
               r'REPRODUCED, THE PLANTED e_p FAILING ; NOT COMPILED\.\*\*', 'the closed form`s foot')
    ck = _bfig('%s_c2_check.txt' % ACT, r'\*\*THE C2 CLOSED FORM, POST HOC: C0 AS WANTED ; C1 \(PLANTED e_p\) FAILS, AS WANTED ; ROWS (\d+), REPRODUCED (\d+) ; '
               r'FIELDS (\d+) ; NEGATIVE AT OMEGA <= 3: (\d+) ; A BAD RAMIFIED PRIME AT EVERY FIELD (True|False) ;', 'the check`s foot')
    ax = _bfig('%s_axiom.txt' % ACT, r'\*\*THE AXIOM STEP AT (\d+) OF (\d+) PINS \((\d+) REPAIRED AND RUN THIS ACT, ([^)]*)\) ; HALTED (\d+) \(([^)]*)\) ; '
               r'RUNS (\d+) ; THE lv SORRY`S DISCHARGE ([^;]*) ; NO MAIN OR TAG TOUCHED\.\*\*', 'the axiom step`s foot')
    sl = _bfig('%s_split_price.txt' % ACT, r'\*\*THE LEDGER SPLIT: (CARRIED WHOLE TO b\d{3}|LANDED)[^-]*-- (\d+) CITATION OCCURRENCES MOVED \((\d+) IN LIVE '
               r'TOOLS\), THE SPLIT ABOUT ([\d.-]+) H BEFORE A CLOSE OF ([\d.]+) H ; ([^.]*)\.\*\*', 'the split`s foot')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v130_ctl=v3[0], v130_n=len(re.findall(r'\([a-z]+\)', v3[0])), v130_cases=v3[1], v130_wanted=v3[2],
                od_n=od[0], od_open=od[1], od_closed=od[2], od_from=od[3], od_moved=od[4], oc_cases=oc[0], oc_wanted=oc[1],
                tw_not=tw[0], tw_met=tw[1], tw_acted=tw[2], tw_priced=tw[3], tw_read=tw[4], tw_retire=tw[5],
                rg_names=rg[0], rg_zeros=rg[1], rg_figs=rg[2],
                sr_read=sr[0], sr_excl=sr[1], sr_excl_of=sr[2], sr_reach=sr[3], sr_sel=sr[4], sr_cont=sr[5], sr_onsets=sr[6],
                zk_c1=zk[0], zk_c2=zk[1], zk_c3=zk[2], zk_rho0=zk[3], zk_band=zk[4], zk_grade=zk[5],
                sp_c1=sp[0], sp_zeros=sp[1], sp_onsets=sp[2], sp_within=sp[3], sp_beyond=sp[4], sp_fals=sp[5], sp_grade=sp[6],
                dl_price=dl[0], dl_figs=dl[1], dl_run=dl[2], dl_word=dl[3],
                cf_steps=cf[0], cf_rows=cf[1], cf_of=cf[2], ck_rows=ck[0], ck_rep=ck[1], ck_fields=ck[2], ck_neg=ck[3], ck_ram=ck[4],
                ax_at=ax[0], ax_of=ax[1], ax_rep=ax[2], ax_beside=ax[3], ax_halted=ax[4], ax_halted_names=ax[5], ax_runs=ax[6], ax_lv=ax[7],
                sl_word=sl[0], sl_occ=sl[1], sl_live=sl[2], sl_hours=sl[3], sl_close=sl[4], sl_cut=sl[5],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _axiom_kind(rows, kind):
    """(R334)(7): the axiom step's rows of one kind as banked (data/b724_axiom_rows.json: commit, push, dispatch, read and the drafts)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R334): no lean process runs on this host; the runner dispatches are those of (R334)(7) alone, six at most, each read by its run id.
    From the command bank (the seat's commands, read live from the capture by the `commands` route: local lean none; the dispatch commands
    those of tools/b724_axiom.py dispatch) and the axiom step's rows (relay data/b724_axiom_rows.json: each dispatch, by command or on its
    push, and each read by its run id), against the worklist's B723_RUNS (Component 7, the Edit tool; b723's N1 read b723's runs)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = json.loads(rdn('%s_axiom_rows.json' % ACT) or '[]')
    dsp, rds = _axiom_kind(rows, 'dispatch'), _axiom_kind(rows, 'read')
    ran = sorted((r.get('kernel'), str(r.get('run'))) for r in dsp)
    want = sorted((k, str(r)) for k, r in K.B723_RUNS)
    read_ids = sorted(str(r.get('run')) for r in rds)
    by_cmd = [r for r in dsp if not r.get('via')]
    ok = bool(cm) and not seat_lean and len(ran) <= K.MAX_DISPATCHES and ran == want and read_ids == sorted(r for _k, r in want) \
        and len(disp) == len(by_cmd)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b724_commands.json): %s; dispatch commands in the capture: %s against '
        'the rows` dispatches by command %d; the runs dispatched (relay data/b724_axiom_rows.json) %d of %d at most, equal to the worklist`s '
        'B723_RUNS: %s (%s); each read by its id: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(by_cmd), len(ran), K.MAX_DISPATCHES, ran == want,
            ', '.join('%s %s' % x for x in ran) or 'NONE', read_ids == sorted(r for _k, r in want)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (Component 7, the Edit tool, over b724's objects; b723's chain over b723's registrations in git at b723's record tool): each figure
# ### bank of a registered object and the commit that landed it, the registrations' commit an ancestor of it and the bank absent at it
N2_REGISTERED = (('data/b724_support_rule.txt', 'C3_PRED'), ('data/b724_zetak.txt', 'C4_ZETAK'), ('data/b724_support.txt', 'C4_SUPPORT'),
                 ('data/b724_dial_price.txt', 'C4_DIAL'))
# ### N2: each tool's controls (or its rule) before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b724_support_rule.txt', 'THE RULE (data/b724_registrations.txt', 'THE ZEROS IN DECREASING'),
               ('data/b724_zetak.txt', '## (C1) ', '## THE zeta_K FORM AT EACH WINDOW'),
               ('data/b724_support.txt', '## (C1) THE BANKED ONSETS', '## THE ZEROS, IN THE RULE`S ORDER'),
               ('data/b724_c2_check.txt', '## (C0) ', '## THE ROWS, EACH POST HOC'),
               ('data/b724_orders.txt', '## THE CONTROLS ((R334)(3)(i))', '## THE ORDERS ('),
               ('data/b724_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R334): the registrations committed before any figure bank -- data/b724_registrations.txt alone at its commit, that commit an ancestor
    of every commit landing a figure bank of a registered object and none of those banks at it, the registrations at HEAD equal to that blob;
    H-SUPPORT's rule output and predictions by a commit of their own before any onset; each tool's controls print before its figures. From
    git (the commits' files, merge-base, the blob at HEAD against the registrations' commit) and the banks' own lines."""
    reg_files = g(ROOT, 'show', '--name-only', '--format=', K.REG_COMMIT).split()
    reg_alone = reg_files == [K.REGISTRATIONS]
    reg_same = bool(_show(ROOT, 'HEAD', K.REGISTRATIONS)) and (_show(ROOT, K.REG_COMMIT, K.REGISTRATIONS) or '') == (_show(ROOT, 'HEAD', K.REGISTRATIONS) or '')
    anc = [(p, getattr(K, c) != K.REG_COMMIT and grc(ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, getattr(K, c)) == 0
            and not _show(ROOT, K.REG_COMMIT, p)) for p, c in N2_REGISTERED]
    pred_files = g(ROOT, 'show', '--name-only', '--format=', K.C3_PRED).split()
    pred_first = pred_files == ['data/b724_support_rule.txt'] and K.C3_PRED != K.C4_SUPPORT \
        and grc(ROOT, 'merge-base', '--is-ancestor', K.C3_PRED, K.C4_SUPPORT) == 0 and not _show(ROOT, K.C3_PRED, 'data/b724_support.txt')
#⟪END⟫
#⟪SECTION record 12⟫
    ok = reg_alone and reg_same and all(o for _p, o in anc) and pred_first and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the registrations` commit %s carrying %s alone: %s; at HEAD equal to its blob there: %s; that commit an ancestor of each figure bank`s '
        'commit, the bank absent at it: %s; H-SUPPORT`s rule output by its own commit %s (%s), before the onsets` %s: %s; each tool`s controls '
        'or rule before its figures: %s' % (
            K.REG_COMMIT[:8], K.REGISTRATIONS, reg_alone, reg_same, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in anc),
            K.C3_PRED[:8], ', '.join(pred_files) or 'unread', K.C4_SUPPORT[:8], pred_first,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (Component 7, the Edit tool, over b724's objects; b723's over its walk and price in git at b723's record tool): the banks whose
# ### grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b724_support_rule.txt', ('ONSETS COMPUTED 0',)), ('b724_zetak.txt', ('THE HYPOTHESIS HELD',)),
             ('b724_support.txt', ('THE HYPOTHESIS REFUTED',)), ('b724_dial_price.txt', ('NOT RUN', 'CARRIED')),
             ('b724_c2_closed_form.txt', ('CHECKED POST HOC', 'NOT COMPILED')), ('b724_c2_check.txt', ('POST HOC', 'REPRODUCED')),
             ('b724_axiom.txt', ('THE AXIOM STEP AT',)), ('b724_split_price.txt', ('CARRIED WHOLE', 'NOTHING CUT')),
             ('b724_orders.txt', ('AT HEAD: ORDERS',)), ('b724_reproduce.txt', ('REPRODUCES',)))
# ### N3: a sentence calling the closed form compiled -- "compiled" not read with its negation (not, never, nor) -- or new
N3_COMPILED = re.compile(r'(?i)\bcompiled\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|un)[ -]?(?:yet |been |\w+ and not )?compiled\b')
N3_NEW = re.compile(r'(?i)\bnew\b')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R334): every grade prints at its end; the C2 closed form's check is labelled POST HOC wherever it is named; no sentence of the entry
    calls it compiled or new. From the graded banks (each bank's last line its foot, the foot carrying its grade's words), the check's rows
    (each led POST HOC, their count the foot's and the closed form's), and the entry as composed (the findings bank's text, or the composer
    before it is written): every sentence naming the closed form and its check carrying POST HOC; none calling it compiled but in negation,
    none calling it new."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
    lead = re.findall(r'(?m)^  (\S+(?: \S+)?)  D\s+-\d+ ', rdn('%s_c2_check.txt' % ACT))
    rows_ph = bool(lead) and all(x == 'POST HOC' for x in lead)
#⟪END⟫
#⟪SECTION record 19⟫
    rows_ok = rows_ph and len(lead) == int(f['ck_rows']) and f['ck_rows'] == f['ck_rep']
    foot_ok = f['cf_rows'] == f['ck_rows'] == f['cf_of']
#⟪END⟫
#⟪SECTION record 20⟫
    called = [s.strip()[:120] for s in sents if N3_COMPILED.search(N3_NEGATED.sub('', s))]
    cf_s = [s for s in sents if re.search(r'(?i)closed form', s)]
    unlabelled = [s.strip()[:120] for s in cf_s if re.search(r'(?i)\bcheck', s) and not re.search(r'(?i)post hoc', s)]
    newer = [s.strip()[:120] for s in cf_s if N3_NEW.search(s)]
    ok = all(o for _n, o in graded) and rows_ok and foot_ok and not called and not unlabelled and not newer
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the check`s rows each led POST HOC (relay data/b724_c2_check.txt), %d, equal to '
        'its foot`s %s and the closed form`s %s of %s: %s; the sentences of %s naming the closed form`s check without POST HOC: %s; calling '
        'anything compiled but in negation: %s; calling the closed form new: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), len(lead), f['ck_rows'], f['cf_rows'], f['cf_of'], rows_ok and foot_ok, src,
            unlabelled or 'NONE', called or 'NONE', newer or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R334)(1), N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build at [23] rewrites by the ferry's (W) list ((R334)(11))
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
    # ### (R334)(7), (11), N5 (Component 7, the Edit tool): no kernel's main touched and no tag cut -- every ref of every kernel carrying a
    # ### commit made after the act's opening commit is the rebuild-b721 branch of a kernel of (R334)(7) at the commit banked for it
    # ### (K.REBUILD_COMMITS), and those five are all there; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept; the address scan's count from its bank (relay data/b724_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    rb_want = dict(K.REBUILD_COMMITS)
    lean_w, rb_new = [], []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if r_[0] == 'refs/heads/' + K.REBUILD_BRANCH and kn in rb_want and r_[1].startswith(rb_want[kn]):
                    rb_new.append(kn)
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_ok = sorted(set(rb_new)) == sorted(rb_want)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and rb_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b724_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than the banked %s commits, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s commits banked at their '
            'branches: %s (%s); the branch kept on the six wave 1 kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', K.REBUILD_BRANCH, len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, rb_ok,
                ', '.join(sorted(set(rb_new))) or 'NONE', len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b724 — lane two, act one hundred and fifty, the checkpoint act under (R334): b723 at its weight and its corrigendum; the close '
            'tools at v1.3.0 and the repeat classes; the open orders generated and the twenty read; the registrations; H-ZETAK, H-SUPPORT and '
            'H-DIAL; the C2 closed form, checked post hoc; the axiom step at the six pins; the ledger split priced')
#⟪END⟫
#⟪SECTION record 29⟫
def _support_lists():
    """H-SUPPORT's falsifier as its bank prints it: (the zeros it fired at, the zeros beyond reach)."""
    t = rdn('%s_support.txt' % ACT)
    a = re.search(r'(?m)^THE FALSIFIER .*: FIRED at \[([^\]]*)\]', t)
    b = re.search(r'(?m)^BEYOND REACH, NO ONSET COMPUTED .*: \[([^\]]*)\]', t)
    return ([x.strip(" '") for x in a.group(1).split(',') if x.strip()] if a else [],
            [x.strip(" '") for x in b.group(1).split(',') if x.strip()] if b else [])


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 7 form ("the close tools at v1.3.0 and <r> repeat classes repaired; the open
    orders generated, <o> open, the twenty read; H-SUPPORT at <z> zeros <HELD | REFUTED | carried>, H-ZETAK <HELD | REFUTED>, H-DIAL <HELD |
    REFUTED | carried>; the C2 closed form written and checked post hoc; the axiom step at <j> of 6 pins; the ledger split <landed | carried>"),
    every figure from the banks (Component 7, the Edit tool; b723's title over b723's objects in git at b723's record tool)."""
#⟪END⟫
#⟪SECTION record 31⟫
    dial = 'carried' if f['dl_run'] == 'NOT RUN' and f['dl_word'].startswith('CARRIED') else f['dl_run']
    return ('## The close tools at %s and %s repeat classes repaired; the open orders generated, %s open, the twenty read; H-SUPPORT at %s zeros '
            '%s, H-ZETAK %s, H-DIAL %s; the C2 closed form written and checked post hoc; the axiom step at %s of %s pins; the ledger split %s' % (
                f['ver'], num_word(f['v130_n']), f['od_open'], num_word(int(f['sp_zeros'])), f['sp_grade'], f['zk_grade'], dial, f['ax_at'],
                f['ax_of'], 'carried' if f['sl_word'].startswith('CARRIED') else 'landed'))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime (b724's gate dry run, defect (e'))
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    fired, beyond = _support_lists()
    return ('(1) the open orders by tools/standing/orders.py`s rule, %s of %s open at PLACE-papers main, the trail’s open-orders line written '
            'from its output, none carried by hand; its controls print after its output, not before (relay data/b724_orders.txt); (2) the twenty '
            'against their triggers as written: %s met, %s acted and %s priced and named, %s discharged by reading, %s offered for retire (relay '
            'data/b724_orders_twenty.txt); (3) H-SUPPORT %s at %s zeros, the falsifier fired at %s; %s beyond reach, not counted as a firing; its successor registered at '
            '%s (relay data/b724_support.txt); H-ZETAK %s; H-DIAL priced and carried, its registration committed (relay data/b724_dial_price.txt); '
            '(4) the C2 closed form written as a derivation and checked post hoc, %s of %s rows reproduced, not compiled, the compile where the '
            'author names it (relay data/b724_c2_check.txt); (5) the axiom step at %s of %s pins, %s runs each read by its id, the lv sorry’s '
            'discharge %s -- the author’s choice at the root’s prompt (relay data/b724_axiom.txt); (6) the ledger split %s with its price, nothing '
            'cut (relay data/b724_split_price.txt); (7) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); '
            '(8) %s and the seat’s %s defect%s as lettered' % (
                f['od_open'], f['od_n'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'], f['tw_retire'], f['sp_grade'], f['sp_zeros'],
                ', '.join(fired) or 'none', ', '.join(beyond) or 'none', K.NEXT_ACT, f['zk_grade'], f['ck_rep'], f['ck_rows'], f['ax_at'],
                f['ax_of'], f['ax_runs'], f['ax_lv'].lower(), f['sl_word'].lower(),
#⟪END⟫
#⟪SECTION record 33⟫
def _axiom_line():
    """the axiom step's runs as its rows bank them: `<kernel> <run> <verdict>` for each read."""
    rows = json.loads(rdn('%s_axiom_rows.json' % ACT) or '[]')
    return ', '.join('%s %s %s' % (r.get('kernel'), r.get('run'), r.get('verdict')) for r in _axiom_kind(rows, 'read')) or 'unread'


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
    a list of (this act's letter, 'b<n-2> (x) -> b<n-1> (y) -> b<n> (z)'). A REPEAT naming an older act, or no letter, is not a run of three."""
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
            'author beside (R334)(11)’s naming of b724): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 7, the Edit tool, over b724's objects;
    b723's composer over b723's objects kept below as _finding_text_b723, not called, and in git at b723's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    fired, beyond = _support_lists()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    dial = 'carried' if f['dl_run'] == 'NOT RUN' and f['dl_word'].startswith('CARRIED') else f['dl_run']
    e = ['', _title(), '',
         'The close tools stand at %s, each folded into one template with the act’s sections beside it and %s repeat classes repaired, their '
         'controls %s of %s as wanted; the open orders are generated from the record by tools/standing/orders.py, %s of %s open at PLACE-papers '
         'main, and the twenty of (R333)(14) are read against their triggers as written; H-SUPPORT, its rule and predictions committed before '
         'any onset, is %s at its %s zeros -- %s onsets computed, %s within 0.03, %s beyond reach -- while H-ZETAK is %s at Q0’s two onset '
         'windows and H-DIAL is priced and %s with its registration committed; the C2 closed form is written as a derivation and checked post '
         'hoc against %s banked rows, %s reproduced, not compiled; the axiom step stands at %s of %s wave 1 pins, %s runs each read by its id; '
         'and the ledger split is %s with its price.' % (
             f['ver'], num_word(f['v130_n']), f['v130_wanted'], f['v130_cases'], f['od_open'], f['od_n'], f['sp_grade'], num_word(int(f['sp_zeros'])),
             f['sp_onsets'], f['sp_within'], f['sp_beyond'], f['zk_grade'], dial, f['ck_rows'], f['ck_rep'], f['ax_at'], f['ax_of'], f['ax_runs'],
             f['sl_word'].lower()), '',
         '*Filed at b724 on the author’s ruling `(R334)`; %d question%s put before the root. Banks: relay `data/b724_corrigendum.txt`, '
         '`data/b724_standing_v130.txt`, `data/b724_orders.txt`, `data/b724_orders_twenty.txt`, `data/b724_registrations.txt`, '
         '`data/b724_support_rule.txt`, `data/b724_zetak.txt`, `data/b724_support.txt`, `data/b724_dial_price.txt`, '
         '`data/b724_c2_closed_form.txt`, `data/b724_c2_check.txt`, `data/b724_axiom.txt`, `data/b724_split_price.txt`, '
         '`data/b724_reproduce.txt`, `data/b724_address_scan.txt`, `data/b724_touch.txt`, `data/b724_standing_figures.txt`, '
         '`data/b724_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repeat classes** ((R334)(1)-(2), `%s`, `%s`, `%s`): b723 entered at its weight (FINDINGS :%s); the '
         'corrigendum of b723’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s); tools/standing/ at %s: the seven close tools folded into templates with the '
         'act’s sections, the pipe-free reader, the lock row, G-READFIRST-DIFF-BANKED retired and the seal’s list from SEALED, its controls %s '
         '-- %s cases, %s as wanted (relay data/b724_standing_v130.txt); standing clauses v9 at `%s`, v8 with row (83), a class repeating in '
         'three acts running the next act’s opening component.' % (
             K.C1_RELAY[:8], K.C1_PP[:8], K.C1_V130[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'],
             f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v130_ctl'], f['v130_cases'], f['v130_wanted'],
             K.STANDING_COMMIT[:8]), '',
         '**The open orders** ((R334)(3), `%s`, `%s`, `%s`): the generator’s rule printed before its output; at PLACE-papers main %s orders, '
         '%s open, %s closed, %s moved from `%s` by the three closing lines of (R334)(3)(ii) and the dated line of the author’s word (5) (relay '
         'data/b724_orders.txt :282); its controls %s of %s as wanted, printed after '
         'its output; the locator reading tried on the author’s word and broken by the record, the rule as ruled earlier standing (`%s`); '
         'the trail’s open-orders line written from the tool’s output, none carried by hand. The twenty of (R333)(14), each against its '
         'trigger as written: not met %s, met %s (acted %s, priced and named %s), discharged by reading %s, offered for retire %s (relay '
         'data/b724_orders_twenty.txt).' % (
             K.C2_RELAY[:8], K.C2_PP[:8], K.C2_WEED_PP[:8], f['od_n'], f['od_open'], f['od_closed'], f['od_moved'], f['od_from'], f['oc_wanted'],
             f['oc_cases'], K.C2_LOCATOR[:8], f['tw_not'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'], f['tw_retire']), '',
         '**The registrations** ((R334)(4), N2, `%s`, `%s`): %s committed alone before any figure at an object they name, zeros named %s, '
         'figures %s (relay data/b724_registrations.txt); H-SUPPORT’s rule printed first and its output, each a*_pred, by a commit of its own '
         'before any onset -- %s off-line zeros read, the banked %s of %s excluded by name, %s within reach, %s selected, onsets computed %s '
         '(relay data/b724_support_rule.txt).' % (
             K.REG_COMMIT[:8], K.C3_PRED[:8], f['rg_names'], f['rg_zeros'], f['rg_figs'], f['sr_read'], f['sr_excl'], f['sr_excl_of'],
             f['sr_reach'], f['sr_sel'], f['sr_onsets']), '',
         '**H-ZETAK** ((R334)(5)(i), N3, `%s`): the Dedekind zeta of Q(sqrt -23) at Q0’s two onset windows, the controls first -- C1 %s, C2 %s, '
         'C3 %s, beside and forced -- then rho0 %s and the band %s: %s (relay data/b724_zetak.txt).' % (
             K.C4_ZETAK[:8], f['zk_c1'], f['zk_c2'], f['zk_c3'], f['zk_rho0'], f['zk_band'], f['zk_grade']), '',
         '**H-SUPPORT** ((R334)(5)(ii), N3, `%s`): onsets by b707’s route on b709’s ladder at the %s zeros its rule named, C1 %s; onsets '
         'computed %s, within 0.03 %s, beyond reach %s; the falsifier fired at %s: %s; %s beyond reach, consistent with the refutation and not '
         'counted as a firing, on the author’s ruling; the products (beta - 1/2) a* printed beside, POST HOC and not a test, no law fitted, '
         'their successor registered at %s (relay data/b724_support.txt).' % (
             K.C4_SUPPORT[:8], f['sp_zeros'], f['sp_c1'], f['sp_onsets'], f['sp_within'], f['sp_beyond'], ', '.join(fired) or 'none',
             f['sp_grade'], ', '.join(beyond) or 'none', K.NEXT_ACT), '',
         '**H-DIAL** ((R334)(5)(iii), `%s`): its build priced (%s), figures at F_c %s, %s; %s (relay data/b724_dial_price.txt).' % (
             K.C4_DIAL[:8], f['dl_price'], f['dl_figs'], f['dl_run'].lower(), f['dl_word'].lower()), '',
         '**The C2 closed form** ((R334)(6), N3, `%s`): written as a derivation in %s steps, the coefficient of log(Z_Q/2) read from log zeta_K '
         'at the bad prime powers (relay data/b724_c2_closed_form.txt); checked POST HOC, the form written knowing the banks, against %s rows '
         'over %s fields of b711-b723, %s reproduced, the planted e_p failing as wanted, negative b(n) at Omega(n) <= 3: %s, a bad ramified '
         'prime at every field: %s (relay data/b724_c2_check.txt); not compiled, the compile carried to where the author names it.' % (
             K.C5_RELAY[:8], f['cf_steps'].lower(), f['ck_rows'], f['ck_fields'], f['ck_rep'], f['ck_neg'], f['ck_ram']), '',
         '**The axiom step at the six pins** ((R334)(7), N1, `%s`): repaired on the %s branches by b723’s priced route, one commit each by the '
         'seat’s neutral identity, one run per kernel read by its id, %s runs of six at most -- %s; %s (its axiom step’s prints read there, '
         'the build carrying its sorry); halted %s; the axiom step at %s of %s '
         'pins; the lv sorry’s discharge %s, its choice put to the author at the root’s prompt; no kernel’s main touched and no tag cut (relay '
         'data/b724_axiom.txt).' % (
             ', '.join(c[:8] for c in K.C6_AXIOM), K.REBUILD_BRANCH, f['ax_runs'], _axiom_line(), f['ax_beside'], f['ax_halted'], f['ax_at'],
             f['ax_of'], f['ax_lv'].lower()), '',
         '**The ledger split** ((R334)(8)): its budget printed before any cut -- %s citation occurrences to move, %s of them in live tools, the '
         'split about %s h before a close of %s h -- and so %s with its price; %s, no ledger rewritten (relay data/b724_split_price.txt).' % (
             f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close'], f['sl_word'].lower(), f['sl_cut'].lower()), '',
         '**The research instruments reproduced** (`%s`): tools/research/reproduce.py over the entered instruments, %s rows: %d REPRODUCES, %s '
         'DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at %s of %s; I-76 read at b544’s pins '
         '(relay data/b724_reproduce.txt, data/b724_i76.txt).' % (
             K.C1_I76[:8], f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R333)(9), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b724_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b724_touch.txt). The act’s counter CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b724 -- %s, %s, %s, %s -- against b723’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b724_standing_figures.txt); standing arms added %d, G-READFIRST-DIFF-BANKED retired at v1.3.0.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the hypotheses and the closed form meet at the banks -- H-SUPPORT reads onsets at '
         'heights its rule chose before any was computed, the closed form reads b(n) at fields whose banks it was written knowing, and each '
         'says which it is; the orders and the repeat classes meet at the record -- an order is open by the trail’s own latest line, a class '
         'repeats by the corrigendum’s tags, and neither is carried by hand.', '',
         '**Carried to:** %s, each from its bank: H-SUPPORT’s successor, registered there (relay data/b724_support.txt); H-DIAL’s build (relay '
         'data/b724_dial_price.txt); the C2 compile where the author names it (relay data/b724_c2_closed_form.txt); the lv sorry’s discharge '
         'on the author’s choice (relay data/b724_axiom.txt); the ledger split with its price (relay data/b724_split_price.txt); the instruments '
         'NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b723():
    """b723's form over b723's objects, kept for the record and not called (Component 8)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 7, the Edit tool, over b724's objects; b723's composer over b723's objects kept below as _trail_text_b723,
    not called, and in git at b723's record tool); its open-orders line written from tools/standing/orders.py's output ((R334)(3)(i))."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    fired, beyond = _support_lists()
    op_line = ORD.open_line(ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1])
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R334) ratified.** Its components as the ferry orders them (relay data/b724_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b723’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             op_line, '',
             '**The orders by the tool:** %s of %s open at PLACE-papers main, %s closed, the line above from tools/standing/orders.py`s output; its '
             'controls %s of %s; the twenty met %s, acted %s, priced %s, discharged by reading %s, offered for retire %s (relay data/b724_orders.txt, '
             'data/b724_orders_twenty.txt).' % (
                 f['od_open'], f['od_n'], f['od_closed'], f['oc_wanted'], f['oc_cases'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'],
                 f['tw_retire']), '',
             '**The hypotheses:** registered at `%s`; H-ZETAK %s (relay data/b724_zetak.txt); H-SUPPORT %s at %s zeros, the falsifier fired at %s; '
             '%s beyond reach, not counted as a firing (relay data/b724_support_rule.txt, data/b724_support.txt); H-DIAL priced, %s, %s (relay data/b724_dial_price.txt).' % (
                 K.REG_COMMIT[:8], f['zk_grade'], f['sp_grade'], f['sp_zeros'], ', '.join(fired) or 'none', ', '.join(beyond) or 'none',
                 f['dl_run'].lower(), f['dl_word'].lower()), '',
             '**The C2 closed form:** written as a derivation; checked POST HOC, %s of %s rows reproduced; not compiled (relay '
             'data/b724_c2_closed_form.txt, data/b724_c2_check.txt).' % (f['ck_rep'], f['ck_rows']), '',
             '**The axiom step:** %s of %s pins; %s runs, each read by its id: %s; the lv sorry’s discharge %s, the author’s choice at the root’s '
             'prompt (relay data/b724_axiom.txt).' % (f['ax_at'], f['ax_of'], f['ax_runs'], _axiom_line(), f['ax_lv'].lower()), '',
             '**The ledger split:** %s with its price, %s (relay data/b724_split_price.txt).' % (f['sl_word'].lower(), f['sl_cut'].lower()), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b724_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b724_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b724_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b724 `%s` (previous `%s`, b723’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b724_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b724_standing_v130.txt); the standing '
             'report tool (relay data/b724_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; one commit each on the %s branches of %d wave 1 kernels by the seat’s '
              'neutral identity, each run read by its id; port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with its one tag %s; no '
              'lean process on this host.' % (
                  K.REBUILD_BRANCH, len(K.REBUILD_COMMITS), K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
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
    """b723's trail record over b723's objects, kept for the record and not called (Component 8)."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R334)(7)`s by tools/b724_axiom.py dispatch, SIDE-frobenius`s and SIDE-kernel`s runs on their pushes; MEASURED off the command bank (each dispatch route run at a command`s head).'),
    ('runner runs read by their ids for the axiom step', 'AXRUNS', 'AXRUNS', 'runs', '### (R334)(7), N1: five, six at most, each read by its id; MEASURED off data/b724_axiom_rows.json against the worklist`s B723_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b724*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act: b721`s rebuild-b721 branches carry (R334)(7)`s repair.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### (R334)(7): the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### each push read back; MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s beside this act`s five, one per kernel of (R334)(7); MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b724*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files written by this act`s rebuild commits', 'RBLEANACT', 'RBLEANACT', 'files', '### none: print_targets.txt at four kernels, SIDE-kernel`s workflow; MEASURED off the five commits` files.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: no main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R334)(9): relay push-b723-closing, push-b723-preroot, push-b723-record; PLACE-papers push-b723-preroot, push-b723-record; each local, by name, after --merged listed it (data/b724_stepzero.txt :70-:76).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s rebuild commits', 'RBWFACT', 'RBWFACT', 'files', '### (R334)(7) and the author`s word (7): SIDE-kernel`s build-module.yml in four places on its rebuild-b721 branch; MEASURED off the five commits` files.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s, b723`s and this act`s; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R334) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (1553808a) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R334)(2): FINDINGS :11401.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R334)(2): one row, b723`s.'),
    ('the open orders generated from the record', 'ORDERS', 'ORDERS', 'orders', '### (R334)(3)(i): tools/standing/orders.py at PLACE-papers main; MEASURED off data/b724_orders.txt :282.'),
    ('open orders at PLACE-papers main', 'OPENORDERS', 'OPENORDERS', 'orders', '### MEASURED off data/b724_orders.txt :282, the trail`s line written from the tool`s output.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the root answer`s (c): tools/research/reproduce.py; MEASURED off data/b724_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R334)(3)-(8): the orders, H-SUPPORT`s rule, H-ZETAK, H-SUPPORT, H-DIAL`s price, the C2 check, the axiom step, the split`s price, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### (R334)(4), N2: data/b724_registrations.txt at 9ad26421, alone; MEASURED off the commit`s files.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### (R334)(4)-(5), N2: H-SUPPORT`s rule, H-ZETAK, H-SUPPORT, H-DIAL`s price; MEASURED off the ancestry from 9ad26421.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### N2: none; MEASURED off each figure bank`s first commit against 9ad26421.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean statements of the C2 closed form written or compiled', 0, 0, 'statements', '### N3: written as a derivation and checked POST HOC, not compiled.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R334)(2): tools/standing/ to v1.3.0 -- the seven close tools folded, the pipe-free reader, the lock row, the seal`s list from SEALED; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 1, 1, 'arms', '### (R334)(2)(iv): G-READFIRST-DIFF-BANKED, at v1.3.0 (be821907); the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 2, 2, 'banks', '### data/act_current.json at step zero and data/standing_clauses_v9.txt by a commit of its own (d9739558, (R334)(2)(v)); data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation, push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R333)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b724_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### (R334)(1), N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs, the dispatches and the run reads ((R334)(7)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0 \
            and c != K.REG_COMMIT

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### N2 (Component 7, the Edit tool): the figure banks of (4)-(5), each first committed after the registrations (9ad26421)
    fig_banks = [p for p in ('data/b724_support_rule.txt', 'data/b724_zetak.txt', 'data/b724_support.txt', 'data/b724_dial_price.txt')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    REGALONE=1 if alone(K.REG_COMMIT) else 0,
                    AXRUNS=jcount('b724_axiom_rows.json', lambda j: len([x for x in j if x.get('kind') == 'read'
                                                                          and (x.get('kernel'), int(x.get('run') or 0)) in set((k, int(r)) for k, r in K.B723_RUNS)])),
                    REPROWS=jcount('b724_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b724_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    ORDERS=tfirst('b724_orders.txt', r'\*\*AT HEAD: ORDERS (\d+) ;'),
                    OPENORDERS=tfirst('b724_orders.txt', r'\*\*AT HEAD: ORDERS \d+ ; OPEN (\d+) ;'),
                    RBWFACT=sum(1 for k_, c_ in K.REBUILD_COMMITS for f_ in _git('D:/' + k_, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split()
                                if f_.startswith('.github/workflows/')),
                    RBLEANACT=sum(1 for k_, c_ in K.REBUILD_COMMITS for f_ in _git('D:/' + k_, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split()
                                  if f_.endswith('.lean')),
                    OTLINES=sum(int((_git(K.PP, 'show', '--numstat', '--format=', c_, '--', 'OPEN_TRAILS.md').split() or ['0'])[0])
                                for c_ in (K.C2_PP, K.C2_WEED_PP)),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('orders', 'support_rule', 'zetak', 'support', 'dial_price', 'c2_check', 'axiom', 'split_price', 'reproduce',
                                               'address_scan') if os.path.exists(os.path.join(ROOT, 'data', 'b724_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'RBWFACT', 'RBLEANACT', 'AXRUNS', 'REPROWS', 'ADDRESS', 'ORDERS', 'OPENORDERS',
              'REGALONE', 'OTLINES', 'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b724_registration_%s.txt -- b724, THE CHECKPOINT ACT: b723 AT ITS WEIGHT AND ITS CORRIGENDUM; THE CLOSE TOOLS "
                             "AT v1.3.0 AND THE REPEAT CLASSES; THE OPEN ORDERS GENERATED AND THE TWENTY READ; H-SUPPORT, H-ZETAK AND H-DIAL UNDER "
                             "THEIR REGISTRATIONS; THE C2 CLOSED FORM CHECKED POST HOC; THE AXIOM STEP AT THE SIX PINS; THE LEDGER SPLIT PRICED, "
                             "UNDER (R334)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b723's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten at Component 7: b723's lines (the
axiom diagnosis, -31 and -55, the fourteen, the C2 statement, the instruments, the propagation read) read banks this act does not write, and
are not carried; the lines are b724's: the axiom step at the six pins, each run by its id (KERNEL), H-ZETAK and the C2 closed form checked
POST HOC, not compiled (CERTIFIED), H-SUPPORT under its rule, H-DIAL priced, the open orders generated and the instruments reproduced
(REGISTERED), and the ledger split and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b724's lines (Component 7, the Edit tool), each from the record tool's figures over b724's banks
    # ------------------------------------------------------------------ KERNEL: THE AXIOM STEP ((R334)(7)), each run read by its id
    # ------------------------------------------------------------------ (N1: no lean on the host, six dispatches at most)
    sk = seat('%s_axiom.txt' % ACT, '**THE AXIOM STEP AT ')
    keys['AXIOM'] = ('KERNEL -- THE AXIOM STEP AT THE SIX WAVE 1 PINS: %s of %s (%s repaired and run this act on rebuild-b721, %s, its axiom '
                     'step`s prints read, the build carrying its sorry); %s runs, '
                     'each read by its id: %s; halted %s; the lv sorry`s discharge %s; no main or tag touched. SOURCE %s.' % (
                         f['ax_at'], f['ax_of'], f['ax_rep'], f['ax_beside'], f['ax_runs'], REC._axiom_line(), f['ax_halted'], f['ax_lv'].lower(),
                         sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: H-ZETAK ((R334)(5)(i)); THE C2 CLOSED FORM ((R334)(6)),
    # ------------------------------------------------------------------ checked POST HOC, not compiled (N3)
    sz = seat('%s_zetak.txt' % ACT, '**H-ZETAK: ')
    keys['ZETAK'] = ('CERTIFIED -- H-ZETAK ON Q0`S TWO ONSET WINDOWS: C1 %s, C2 %s, C3 %s; rho0 %s, the band %s; THE HYPOTHESIS %s. SOURCE %s.' % (
        f['zk_c1'], f['zk_c2'], f['zk_c3'], f['zk_rho0'], f['zk_band'], f['zk_grade'], sz['text']))
    seats.append(sz)
    sw = seat('%s_c2_check.txt' % ACT, '**THE C2 CLOSED FORM, POST HOC: ')   # ### appended by the template after this section
    keys['C2'] = ('CERTIFIED -- THE C2 CLOSED FORM, CHECKED POST HOC: written as a derivation in %s steps; %s rows over %s fields, %s reproduced, '
                  'the planted e_p failing as wanted; not compiled. SOURCE %s.' % (
                      f['cf_steps'].lower(), f['ck_rows'], f['ck_fields'], f['ck_rep'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: H-SUPPORT ((R334)(4)-(5)(ii)); H-DIAL ((R334)(5)(iii));
    # ------------------------------------------------------------------ THE OPEN ORDERS ((R334)(3)(i)); THE INSTRUMENTS REPRODUCED
    fired, beyond = REC._support_lists()
    ss = seat('%s_support.txt' % ACT, '**H-SUPPORT: ')
    keys['SUPPORT'] = ('REGISTERED -- H-SUPPORT AT Q0`S OFF-LINE ZEROS, its rule committed before any onset: %s zeros, onsets computed %s, within '
                       '0.03 %s, beyond reach %s (%s); the falsifier fired at %s; THE HYPOTHESIS %s. SOURCE %s.' % (
                           f['sp_zeros'], f['sp_onsets'], f['sp_within'], f['sp_beyond'], ', '.join(beyond) or 'none', ', '.join(fired) or 'none',
                           f['sp_grade'], ss['text']))
    seats.append(ss)
    sd = seat('%s_dial_price.txt' % ACT, '**H-DIAL: ')
    keys['DIAL'] = ('REGISTERED -- H-DIAL: its build priced (%s), figures at F_c %s, %s; %s. SOURCE %s.' % (
        f['dl_price'], f['dl_figs'], f['dl_run'].lower(), f['dl_word'].lower(), sd['text']))
    seats.append(sd)
    so = seat('%s_orders.txt' % ACT, '**AT HEAD: ORDERS ')
    keys['ORDERS'] = ('REGISTERED -- THE OPEN ORDERS GENERATED by tools/standing/orders.py at PLACE-papers main: %s orders, %s open, %s closed; '
                      'its controls %s of %s; the twenty met %s, discharged by reading %s, offered for retire %s. SOURCE %s.' % (
                          f['od_n'], f['od_open'], f['od_closed'], f['oc_wanted'], f['oc_cases'], f['tw_met'], f['tw_read'], f['tw_retire'], so['text']))
    seats.append(so)
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('REGISTERED -- THE RESEARCH INSTRUMENTS REPRODUCED (tools/research/reproduce.py): %s rows, REPRODUCES %s, DIFFERS %s, NOT RUN '
                     '%s (%s), the planted controls as wanted %s of %s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr'],
                         sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE LEDGER SPLIT ((R334)(8)); THE DRAFT
    sl = seat('%s_split_price.txt' % ACT, '**THE LEDGER SPLIT: ')
    keys['SPLIT'] = ('HELD -- THE LEDGER SPLIT: %s with its price, %s citation occurrences to move (%s in live tools), about %s h before a close '
                     'of %s h; %s. SOURCE %s.' % (
                         f['sl_word'].lower(), f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close'], f['sl_cut'].lower(), sl['text']))
    seats.append(sl)
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['AXIOM']), ('CERTIFIED', ['ZETAK', 'C2']), ('REGISTERED', ['SUPPORT', 'DIAL', 'ORDERS', 'REPRO']), ('HELD', ['SPLIT', 'HELD'])]
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
