# -*- coding: utf-8 -*-
# b752 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R362)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R362)(2) repair it carries. Edited by the Edit tool. Carried at b752 by tools/b752_fold.py (`carry`) from tools/acts/b751.py,
# b751`s names substituted; the citation`s sections adopted from tools/b752_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b751`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b751`s carried till
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
# ### b752, Component 1: THE c1 ROUTE FOR b751'S WEIGHT LINE AND ITS CORRIGENDUM, (R362)(1) and (3). Rewritten at b752 against
# ### b751's own banks (scratch c1sec749.txt, spliced): the closing's lines by needle, the events (5), the defects (18, (i) the navigator's),
# ### the refusals (13 lines at 71bc497a), the v1.29.0 controls and the rules this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = 'd921bceb'          # ### b751's closing push tip, the public relay's main at step zero ((R362)(1))
C1_CLOSING_COMMIT = '2c422414'      # ### b751's closing commit (its closing row, data/b751_steps.json)
C1_REFUSAL_AT = 'd921bceb'          # ### its refusal bank read at its closing push tip (19 lines)
C1_NOTED = '2026-11-10'
C1_CORRIGENDA_LAST = 71
C1_V170 = 'b752_standing_v1320.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.32.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-10 by b752 to b751’s entry (:%d), under `(R362)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## THE_EPSTEIN_CONTROL_OBJECT §5 passed, 1505 words, 77 cites'
C1_TRAIL_NEEDLE = '### b751 — lane two, act one hundred and seventy-eight'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")
# ### b752 step zero: this route written against b751's banks over the carried route (b750's figures under b751's names), which `carry.py ruled`
# ### refused by R5 before the citation check (data/b752_stepzero.txt); nothing composed by the carried route.


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
    for l in _c1_rd('b751_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b751_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b751_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b751_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b751_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b751_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b751_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    sc = json.load(open(os.path.join(D, 'b751_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8 or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b751_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the closing`s scores')
    ar = json.load(open(os.path.join(D, 'b751_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b751_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (ci_, ce_, cf_, cc_, cl_, cr_), l_co = _c1_fl(c, r'^    the generated entry for b750`s events and defects.*: ITEMS (\d+): EVENTS (\d+), DEFECTS (\d+) ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ; ', 'b750`s corrigendum')
    (va, vb), l_v = _c1_fl(c, r'^    tools/standing/ at v1\.31\.0: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.31.0 foot')
    (lq, ls, lsrc, ln_, lenc), l_lt = _c1_fl(c, r'^    the classical theorem read from its source .*: THE LITERATURE: QUERIES (\d+) ; SOURCES READ (\d+) \((arXiv [0-9.v]+), .*; NOT READ (\d+) ; .*THE CERTIFIED ENCLOSURE (.*? CONTAINS Re s = 1) ;', 'the literature')
    (sw, sc_, sp, spp, sdf, sdr), l_s5 = _c1_fl(c, r'^    section 5 as put at \[S5\].*: §5: WORDS (\d+) ; LINE CITES (\d+) ; \[S5\] (PASSED) ; WRITTEN AT PLACE-papers ([0-9a-f]{8}), .*WHERE THE RULING DIFFERS (\d+) \((D1-D\d)\)', '§5')
    (_ln, kst, stg, lm1, lm2), l_ln = _c1_fl(c, r'^    the INTEGRATION line .*: THE LINE: (COMPOSED) ; .*KEYSTONE (\S+) ; STAGE (\S+) ; MATCHED (\d+) OF (\d+) ;', 'the line')
    (rr, rp_, rd_, rn_), l_rp = _c1_fl(c, r'^    tools/research/reproduce\.py.*: ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ;', 'the instruments')
    sca, l_sc = _c1_fl(c, r'^    the scan over every commit and bank of the act.*: PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', 'the scan')
    (_tg,), l_tg = _c1_fl(c, r'^### THE KERNELS: .*(no tag beyond v0\.38)', 'the tag')
    _mv, l_mv = _c1_fl('b751_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz, msha, mmd5), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-10-b751)\.zip ; \d+ bytes ; sha256 ([0-9a-f]{8})[0-9a-f]* ; MANIFEST md5 ([0-9a-f]{8})', 'the mirror`s archive')
    _aw1, l_aw1 = _c1_fl('b751_author_words.txt', r'^(Confirmed: plan act next, the attribution order’s plan act as b752, .* §6 of the paper after it\.)$', 'the author`s word at the root')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R361\)\(4\) AND \(8\)\*\*: (the attribution order`s plan act, .*)$', 'the carried item (a)')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 6)) or len(dr) != 22 or (int(sd), int(se)) != (22, 5):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    nav = [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"]
    return (C1_WEIGHT_HEAD + ' -- b751 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b751_closing.txt):* “%s” (data/b751_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b751_steps.json, the record and closing rows). As its rows read: b750’s corrigendum, items %s (events %s, defects %s), CLAIM %s, CLOSE %s, '
            'REPEAT %s (:%d); standing tools v1.31.0, %s of %s (:%d); the literature read from its source before the draft: queries %s, sources read %s (%s), not read %s, '
            'the certified enclosure %s (:%d; relay data/b751_literature.txt); §5 of THE_EPSTEIN_CONTROL_OBJECT_v0_1 put as [S5] and %s, %s words, %s line cites, written at PLACE-papers %s, '
            'where the ruling differs %s (%s) (:%d; relay data/b751_section5.txt); the INTEGRATION line %s, keystone %s, stage %s, matched %s of %s (:%d; relay data/b751_line.txt); '
            'the instruments %s rows, %s reproduce, %s differ, %s not run (:%d); the address scan %s ; %s ; %s ; %s (:%d); %s (:%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push '
            'and %s of %s post-push (:%d, :%d), the failing the three declared on the face and G-RULE-REMOTE-REREAD, which read a call the hook had refused before it ran '
            '(data/b751_events.txt (1)); G-CURRENTS-UNEDITED passing on b751’s banks and failing on b750’s, no detail line written (data/b751_events.txt (3)). '
            'At the scores’ close SCORES %d OF 8 HELD (data/b751_scores_close.json; the closing’s line :%d). The root %s over %s banks, '
            'chained from %s (data/b751_act_root.json; :%d); the mirror %s at %s, sha256 %s, MANIFEST md5 %s (data/b751_mirror_verify.txt :%d; :%d); '
            'the author’s word at the root “%s” (data/b751_author_words.txt :%d); the closing’s carried item (a): %s (:%d), this act under `(R362)`. %d events in data/b751_events.txt, rows (1)-(%d), '
            'entered after the lock; %d defects, (a)–(v), the navigator’s %s among them (data/b751_defects.txt); the closing commit’s words refused once at 21:20:10Z and re-sent, unbanked by the closing’s rule, '
            'entered by the corrigendum below. The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'Nothing deposited, no merge, no new Zenodo version, the draft held at v5; the corrigendum for these rows follows, under `(R362)`(7).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, ci_, ce_, cf_, cc_, cl_, cr_, l_co, vb, va, l_v, lq, ls, lsrc, ln_, lenc, l_lt,
                sp, sw, sc_, spp, sdf, sdr, l_s5, _ln, kst, stg, lm1, lm2, l_ln, rr, rp_, rd_, rn_, l_rp, sca[0], sca[1], sca[2], sca[3], l_sc,
                _tg, l_tg, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, len(held), l_sl,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, msha, mmd5, l_mv, l_mz, _aw1[0], l_aw1, ca, l_ca, len(ev), max(ev), len(dr),
                ', '.join('(%s)' % x for x in nav), cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b751's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '12:03:22Z', 'defect (a)'), (2, 'READ', '12:04:21Z', 'defect (a)'), (3, 'READ', '12:21:57Z', 'defect (a)'), (4, 'READ', '12:27:48Z', 'defect (f)'),
               (5, 'PIPE', '12:29:37Z', 'defect (f)'), (6, 'READ', '12:34:39Z', 'defect (f)'), (7, 'LIMIT', '12:43:03Z', 'defect (g)'), (8, 'READ', '13:19:59Z', 'defect (n)'),
               (9, 'REDIR', '13:22:46Z', 'defect (n)'), (10, 'READ', '13:24:08Z', 'defect (n)'), (11, 'LIMIT', '14:05:00Z', 'defect (p)'), (12, 'WLIST', '14:25:19Z', 'defect (r)'),
               (13, 'WLIST', '14:25:23Z', 'defect (r)'), (14, 'PIPE', '15:22:51Z', 'defect (t)'), (15, 'READ', '16:47:53Z', 'defect (u)'), (16, 'PIPE', '16:47:59Z', 'defect (u)'),
               (17, 'READ', '16:50:42Z', 'defect (u)'), (18, 'REMOTE', '17:54:14Z', 'defect (v)'), (19, 'READ', '18:56:03Z', 'event (2)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing refusal of b751's in its hook bank: b752's hook bank opens at its own step zero, every line b752's own
C1_FLIP = {}      # ### (R362)(7) flips no tag: each item read as its bank tags it
# ### (R362)(7): two items entered beside b751's banks, each with its owner, tag and column: the closing commit's words refused at 21:20:10Z
# ### (commit.py's own class line: REPEAT of b749 defect (h)), unbanked by the closing's rule, entered as an event; and the navigator's
# ### correction of (R362)(2), lettered in b752's defects bank as the navigator's
C1_CARRIED = [("the refusal of 21:20:10Z", "THE SEAT'S", 'CLOSE', 'REPEAT b749 (h)',
               'the closing commit sent with its words beginning "b751 closing:", refused by commit.py ("THE WORDS REPEAT THE HEAD"), nothing committed and no row written; re-sent with the words alone, relay 2c422414; unbanked by the closing`s rule, entered here as an event'),
              ("(R362)(2)", "THE NAVIGATOR'S", 'CLAIM', 'NEW',
               'on 2026-11-10 the navigator put to the author as new four things the corpus already holds (A9 with B3 and C1; W-ORD-MECHANISM-TABLE`s row; Which_Structure_Confines v2.3.1 :40, :117, :176; W-ORD-PLATT-RUNG), reasoning from recall and not from the export')]
C1_CORR_TITLE = ('## Corrigendum to b751’s record (relay data/b751_events.txt rows (1)-(5) and data/b751_defects.txt (a)-(v)): five events and twenty-two defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT, the navigator’s six among them, with the unbanked refusal of 21:20:10Z and the navigator’s correction of `(R362)`(2); the rulings from recall, the refused call counted apart, '
                 'the arm on the prior act’s banks, the append keyed on time and words, the order that is no order, the carry, the flag read as an act, the limit row, the instances, '
                 'the session change, at tools/standing/ v1.32.0, each controlled, under (R362)(7)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.32.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_rules_line(n):
    t = _c1_rd('b752_rules.txt').split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith('(%d) ' % n)]
    if len(h) != 1:
        sys.exit('### THE RULES BANK: %d LINES OPEN (%d), NOT ONE -- NOTHING COMPOSED' % (len(h), n))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b751_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)   # ### 19 lines at d921bceb
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at[:8] not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if 'hook' not in src.lower() and 'refused' not in src.lower() and at[:5] not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b751_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.32.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(5)', sorted(ev) == list(range(1, 6))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 22', len(dr) == 22), ('the refusals 19, each answered as listed', len(rl) == 19 and not bad_ref),
                              ('the navigator`s rows in b751`s defects bank (e), (h)-(l)', [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"] == ['e', 'h', 'i', 'j', 'k', 'l']),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.32.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl_) == (int(cc), int(cd)))) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; counter %d, %d)' % (bad, bad_ref, nc, nl_))
    s['v170_foot'] = foot[0]
    return s


def _c1_counts(s):
    t = [s['tags'][n][0] for n in sorted(s['events'])] + [x[2] for x in s['defects']]
    rep = sum(1 for n in s['events'] if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def _c1_read_counts(s):
    """the counter as this corrigendum reads the items: the closing's 27 and the two entered beside them, no tag flipped."""
    nc, nl_, rep, n = _c1_counts(s)
    t = [x[2] for x in C1_CARRIED]
    return nc + t.count('CLAIM'), nl_ + t.count('CLOSE'), rep + sum(1 for x in C1_CARRIED if x[3] != 'NEW'), n + len(C1_CARRIED)


def _c1_owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v_, k_.lower().replace("'s", '’s').replace("'", '’')) for k_, v_ in sorted(c.items(), key=lambda kv: -kv[1]))


def _c1_col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’').replace('`', '’')


# ### the repairs each item is met by at v1.32.0 (the controls bank data/b752_standing_v1320.txt, the rules data/b752_rules.txt)
C1_EV_EXTRA = {1: '; repair (refused), `(R362)`(7)(ii): the arm reads the calls that ran, a refused call counted apart and printed',
               2: '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusal printed (data/b751_hook_refusals.txt :19)',
               3: '; repair (currents), `(R362)`(7)(iii): the arm run alone on b750’s banks, its cause printed, a detail line given',
               4: '; repair (append), `(R362)`(7)(iv): a line standing when its time and its words both match, the lines added printed',
               5: '; repair (instances), `(R362)`(7)(ix): the transient remote read and the host’s refusal printed'}
C1_DF_EXTRA = {'a': '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusals printed', 'b': '; repair (carry), `(R362)`(7)(vi), REPEAT',
               'c': '; no item of `(R362)`(7) names it; a pushed bank restored to its blob at step zero',
               'd': '; repair (instances), `(R362)`(7)(ix), REPEAT b736 (e): the dotted name printed',
               'e': '; repair (recall), `(R362)`(7)(i): the navigator’s, lettered as the navigator’s',
               'f': '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusals printed',
               'g': '; repair (limit), `(R362)`(7)(viii): the row reads the command’s own arguments',
               'h': '; repair (recall), `(R362)`(7)(i): the navigator’s', 'i': '; repair (recall), `(R362)`(7)(i): the navigator’s',
               'j': '; repair (recall), `(R362)`(7)(i): the navigator’s', 'k': '; repair (recall), `(R362)`(7)(i): the navigator’s',
               'l': '; repair (recall), `(R362)`(7)(i): the navigator’s',
               'm': '; no item of `(R362)`(7) names it; the dry`s counts alone, carried', 'n': '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusals printed',
               'o': '; no item of `(R362)`(7) names it; two arms of the rewrite read and repaired before the gate',
               'p': '; repair (limit), `(R362)`(7)(viii), REPEAT: the row reads the command’s own arguments',
               'q': '; repair (carry), `(R362)`(7)(vi), REPEAT: the readfirst needles and the trail head’s ordinal printed beside the ruling',
               'r': '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusals printed',
               's': '; no item of `(R362)`(7) names it; v1.31.0’s guard holding on its first live instance',
               't': '; repair (flag), `(R362)`(7)(vii): a tool refuses an act name that begins with a hyphen',
               'u': '; repair (instances), `(R362)`(7)(ix), REPEAT: the refusals printed',
               'v': '; repair (instances), `(R362)`(7)(ix): the transient remote reads and the refusal printed'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b752, to `(R362)`(7)(v): the open-orders line has carried `W-ORD-1` since b748’s trail (OPEN_TRAILS :18002, :18048, :18096, :18144), the count 73 of 208 '
            'where b747 read 72 of 207; the token is the row-ID halt’s text of b746, read by tools/standing/orders.py as an order; no line of a landed trail is rewritten, the correction by this act’s trail.',
            'Dated note, b752, to `(R362)`(7)(x): the session change of b751 (16:47:23Z, session 43048615) entered as the standing rule working: the face’s sentence, the listing of one claude process, '
            'the continuation read by K.SESSIONS_AFTER.')
C1_CLASSES = (
    ('recall', 'the navigator’s rulings from recall (`(R362)`(7)(i), defects (e), (h)-(l), REPEAT b750 (f); `(R362)`(2))', 'the citation check prints every path of the ferry with OK or NONE before step zero’s commit. b751’s four absent paths replayed: printed NONE', 1),
    ('refused', 'the arm that read a refused call (`(R362)`(7)(ii), events (1))', 'G-RULE-REMOTE-REREAD reads the calls that ran, a call the hook refused before it ran counted apart and printed. b751’s call record replayed: FAIL before, PASS after with the refused call printed', 2),
    ('currents', 'G-CURRENTS-UNEDITED on the prior act’s banks (`(R362)`(7)(iii), events (3))', 'the arm run alone on b750’s banks, its cause printed, and the arm given a detail line', 3),
    ('append', 'the append keyed on words alone (`(R362)`(7)(iv), events (4))', 'the route treats a line as standing when its time and its words both match, and prints the lines it adds. b751’s two go words replayed: one row before, two after', 4),
    ('orders', 'the order that is no order (`(R362)`(7)(v), OPEN_TRAILS :18002-:18144)', 'tools/standing/orders.py reads an order from its entry form alone; the line and the count regenerated. The reader replayed over OPEN_TRAILS at HEAD: W-ORD-1 read before, absent after, the count printed', 5),
    ('carry', 'the carry (`(R362)`(7)(vi), defects (b), (q), REPEAT)', 'the carry prints every row it brings beside the ruling and refuses the ones it does not name, the readfirst needles and the trail head’s ordinal among them', 6),
    ('flag', 'a flag read as an act (`(R362)`(7)(vii), defect (t))', 'a tool refuses an act name that begins with a hyphen. `wlist.py bank --quiet` replayed: a bank written before, refused after', 7),
    ('limit', 'the limit row’s false refusals (`(R362)`(7)(viii), defects (g), (p))', 'the row reads the command’s own arguments and not a quoted string or a line count; both instances replayed: refused before, passed after', 8),
    ('instances', 'the dotted name, the transient reads and the hook’s refusals (`(R362)`(7)(ix), defects (a), (d), (f), (n), (r), (u), (v), events (2), (5), REPEAT)', 'the instances printed, b751’s nineteen refusals each by its line', 9),
    ('session', 'the session change (`(R362)`(7)(x))', 'entered as the standing rule working: the face’s sentence and the listing', 10),
    ('version', 'the version (`(R362)`(7)(xi))', 'tools/standing/VERSION v1.32.0, landed by a commit of its own (relay %s) with its controls bank and the record’s dry over it, before the gate' % (K.C1_STANDING or '')[:8], 11),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr_, rn = _c1_read_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b751’s events bank (relay data/b751_events.txt) carries five rows, entered after its lock gate and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-two lettered rows, (a)-(v), each tagged in its own bracket (%s); its refusal bank nineteen lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them. '
         'The navigator’s six, (e) and (h)-(l), are lettered in the defects bank as the navigator’s; two items are entered beside the banks below.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R362)`(7), at tools/standing/ v1.32.0, each with a control on b751’s banks or the trail as it stands, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s; the rules relay data/b752_rules.txt):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what, rule_ in C1_CLASSES:
        at_ = 'relay data/%s :%d; data/b752_rules.txt (%d), :%d' % (C1_V170, _c1_v170_line('### (%s) ' % k_), rule_, _c1_rules_line(rule_))
        L += ['**(%s) %s** -- %s (%s).' % (k_, name, what, at_), '']
    L += ['**b751’s events (1)-(5):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?(2026-11-\d\dT)?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b751_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, ''))]
    L += ['', '**b751’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b751_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**Entered beside the banks by `(R362)`(7):**', '']
    for x, o, t, c, tx in C1_CARRIED:
        L += ['**%s** %s (%s; %s; %s).' % (x, _c1_q(tx).replace("'", '’'), o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(c))]
    L += ['', '**b751’s refusals** (relay data/b751_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (five events, twenty-two defects), as b751’s closing prints it (relay data/b751_closing.txt :5); '
          'with the two entered beside them CLAIM %d, CLOSE %d, REPEAT %d of %d; no tag is read otherwise here; the CLAIM items of the banks %s.' % (nc, nl_, rep, n, n, rc, rl_, rr_, rn, ', '.join(claims) or 'none'), '',
          '*Filed at b752 on the author’s ruling `(R362)`(7): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b752.py) from '
          'b751’s events and defects banks read unedited, its refusal bank, the v1.32.0 controls bank and the rules; banked as relay `data/b752_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b751’s record; no sealed tool, face, trail or root-named bank of b751 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr_, rn = _c1_read_counts(s)
    return (['b752 -- THE CORRIGENDUM FOR b751, (R362)(7) (%s)' % utc(), '',
             '### the banks read unedited: data/b751_events.txt rows (1)-(5), data/b751_defects.txt 22 rows, data/b751_hook_refusals.txt 19 '
             'lines at %s; data/%s (the v1.32.0 controls); data/b752_rules.txt; the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 5, DEFECTS 22 ; CLAIM %d, CLOSE %d ; REPEAT %d ; WITH THE TWO ENTERED %d: CLAIM %d, CLOSE %d ; REPEAT %d ; THE NAVIGATOR`S 7, LETTERED (e), (h)-(l) AND (R362)(2) ; DATED NOTES %d ; '
               'v1.32.0: THE RULINGS FROM RECALL, THE REFUSED CALL, THE ARM ON THE PRIOR BANKS, THE APPEND, THE ORDER THAT IS NO ORDER, THE CARRY, THE FLAG, THE LIMIT ROW, '
               'THE INSTANCES, THE SESSION CHANGE, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, rn, rc, rl_, rr_, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b751 at its weight after its entry, and the corrigendum for b751, landed through b698's guarded
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
        rc, rl_, rr_, rn = _c1_read_counts(s)
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=nc, close=nl_, repeat=rep, items=n,
                                                   events=[dict(row=k_, owner=s['tags'][k_][2], tag=s['tags'][k_][0], column=s['tags'][k_][1]) for k_ in sorted(s['events'])],
                                                   entered=[dict(item=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in C1_CARRIED], flipped={},
                                                   with_entered=dict(claim=rc, close=rl_, repeat=rr_, items=rn),
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.32.0', bank='data/' + C1_V170, rules='data/b752_rules.txt'),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; WITH THE TWO ENTERED %d, %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, rc, rl_, rn, rr_, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b752, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b752, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b752's name.
# ### b752's own changes are marked "b752, Component 3". The runner overrides read the act's dispatch rows: (R362)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b752_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R361)(7), as b751 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
#⟪OVERRIDE checks MARK aed8852d751b 16⟫
def runner_ok(S):
    """N1, b752 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
    id the worklist's, read once after it by that id; the plant a dispatch row with no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    return len(ds) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 0 and [int(r.get('run')) for r in ds] == list(K.EF_RUNS) \
        and all(str(r.get('free_mb', '')).isdigit() for r in ds + rs) \
        and all(sum(1 for x in rs if str(x.get('run')) == str(d.get('run'))) == 1
                and rows.index(d) < next(i for i, x in enumerate(rows) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) for d in ds)
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b752: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b752, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R362)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b751, naming tools/standing/hook.py, unedited this act (its last edit b751`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b752, C4, defect (n) (the Edit tool): the step-zero bank writes each deleted ref's tip as "(was 7d34b587)" (data/b752_stepzero.txt :44-:45),
# ### b751's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b751-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b752, Component 3 (the Edit tool): b752's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b751-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b752_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b752_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b752, Component 6 (the Edit tool): b752's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b751's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b752, Component 4 (the Edit tool): b751's overrides of checks 1516 and 1659 (hook.py edited by b751's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b752 as it stands
# ### b752, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b752_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b752, Component 4 (the Edit tool): the corrigendum's events rows (1)-(12), b751's twelve (the template's range is a fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 8)) \
#⟪END⟫
# ### b752, Component 4 (the Edit tool): b751's override of checks 1476-1482 (one ERRATA entry at b751's (R361)(5)) removed -- (R362)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b752 as it stands
# ### b752, Component 3 (the Edit tool): G-BRANCHES-DELETED over b752's two repositories (relay, PLACE-papers) and five
# ### refs; b752, Component 4, defect (m): the step-zero bank writes "KEPT as banked (" -- the seat's row at data/b752_stepzero.txt :43 and the
# ### tool's row (tools/standing/carry.py kept b752) in its dated note -- read in its own wording, the tool's row asked by its own head
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked (the tool`s row, tools/standing/carry.py kept b752' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b752, Component 4 (the Edit tool): G-RUNNER-READ's plant on b752's dispatch rows -- run 2's axiom lines carrying sorryAx (b751's
# ### plant read the lv rows' closure log, which b752 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b752, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b752, Component 6 (the Edit tool): the fold bank was b751's own route
# ### (tools/b751_fold.py); b752's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b752_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b751.py -> tools/acts/b752.py' in (rd('b752_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b752, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b752_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b752, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b752_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b752_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b752, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R362): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R362)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b752')
    return '### THE COUNTER ((R362) Component 5, the act`s events and defects together; relay data/b752_defects.txt, data/b752_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b751, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b752 (defect (d')): the order's
# ### state as b752 leaves it -- the carry from b751 said "as b751 left it ... not touched this act", where b752 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act; W-ORD-MECHANISM-ATTRIBUTION as b751 entered it (PLACE-papers 4ba38687); W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as they were entered;',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b752, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)
#⟪END⟫
# ### b752, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b751's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b752_author_answers.txt', 'b752_answer_check.txt', 'b752_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b752, Component 4's probe: v1.27.0's rdn (repair (7)) refuses a missing file, and _counter (record.tpl :2315) reads the events bank,
# ### which the close writes after the seal; read optional for the events bank alone, the defects bank still refused if missing
#⟪OVERRIDE record MARK 26666a71fb1e 1 REPAIR (reader)⟫
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
#⟪END⟫
# ### b752, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b751's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b752, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b751's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b752_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b752_registration_%s.txt' % __import__('b752_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b752, Component 4 (the Edit tool, before the face): b751's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b752, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b752's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b752, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R362)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b752 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b752_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b752: the controls' one route (N1)
#⟪END⟫
# ### b752, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b751's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b752 scorer reads; the needles set to the banks b752's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b752, (R362)(2)(iii): b751's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b752, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b752_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b752: b751's override of G-DIFFERS-ERRATA (two ERRATA entries at its sitting) retired; b752 writes no ERRATA entry ((R362)(6)), so
# ### the template's arm, ERRATA at HEAD byte-equal to its blob at the act's base, reads b752 as it stands
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'ehijkl' else 'SEAT') for c in tuple('abcdefghijklmn')))   # ### (a)-(n) so far, the navigator's (e) (the read-first paths) and (h)-(l) (§5's, at [S5]), the rest the seat's (data/b752_defects.txt); reset to the letters entered before the lock
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b752_corrigendum.txt', 'data/b752_standing_v1310.txt', 'data/b752_literature.txt', 'data/b752_section5.txt',
                  'data/b752_author_answers.txt', 'data/b752_line.txt', 'data/b752_rules.txt', 'data/b752_pathrefusal.txt',
                  'data/b752_reproduce.txt', 'data/b752_reproduce.json', 'data/b752_address_scan.txt', 'data/b752_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b752 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R362)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b752_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _txt(x):
    """a blob or a file's text as str, bytes decoded as UTF-8, CR dropped; '' for None."""
    if x is None:
        return ''
    if isinstance(x, bytes):
        x = x.decode('utf-8', 'replace')
    return x.replace(chr(13), '')


def _draft_of(t):
    """(R362)(2): the section bank's draft, the lines between `## THE DRAFT BEGIN` and `## THE DRAFT END`, its blank edge lines cut;
    pure in its argument."""
    ls = (t or '').replace(chr(13), '').split(NL)
    try:
        a, b = ls.index('## THE DRAFT BEGIN'), ls.index('## THE DRAFT END')
    except ValueError:
        return []
    d = ls[a + 1:b]
    while d and not d[0].strip():
        d = d[1:]
    while d and not d[-1].strip():
        d = d[:-1]
    return d


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R362)(1)-(4) (b752's keys over b752's objects): the order by time and ancestry; v1.31.0's controls; the literature bank,
        # ### the section bank, the put bank, the paper's §5; the answers bank; the line bank; zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b751's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1310', K.STANDING_COMMIT, K.C1_STANDING), ('v1310_corr', K.C1_STANDING, K.C1_CORR),
                                 ('corr_lit', K.C1_CORR, K.C2_PLAN_FIRST), ('lit_s2', K.C2_PLAN_FIRST, K.C2_RELAY),
                                 ('s2_c3', K.C2_RELAY, K.C3_RELAY[0]))),
        # ### b752 (R362)(1)-(2): the order within PLACE-papers by ancestry -- the weight and corrigendum, then §5 on [S5]'s pass
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('pre_c1', K.PRE_PP, K.C1_PP), ('c1_s5', K.C1_PP, K.C2_PP[0]))),
        v1130=rd('b752_standing_v1310.txt'), v1281=None,
        lit=rd('b752_literature.txt'), lit_blob=_s(blob(ROOT, '%s:data/b752_literature.txt' % K.C2_PLAN_FIRST)),
        sec=rd('b752_section5.txt'), sec_blob=_s(blob(ROOT, '%s:%s' % (K.C2_RELAY, K.SECTION_BANK))), putj=jl('b752_put_1.json'),
        paper=cr0(raw(os.path.join(PP, *K.SECTION_FILE.split('/')))), paper_pre=cr0(blob(PP, '%s:%s' % (K.PRE_PP, K.SECTION_FILE))),
        paper_at=cr0(blob(PP, '%s:%s' % (K.C2_PP[0], K.SECTION_FILE))),
        rows_bank=rd('b752_line.txt'), zanswers=rd('b752_author_answers.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP,) + K.C2_PP),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP,) + K.C2_PP),
        numstat=dict((h_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for h_ in K.C2_PP),
        c3_blobs=dict((p_, _s(blob(ROOT, '%s:%s' % (K.C3_RELAY[0], p_)))) for p_ in ('data/b752_line.txt', 'tools/b752_line.py')),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_TIP, 'refs/heads/' + K.ZQ_BRANCH).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..refs/heads/%s' % (K.ZQ_TIP, K.ZQ_BRANCH)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        zq_tag=(gs(EF, 'rev-parse', 'refs/tags/' + K.ZQ_TAG[0]).strip(), gs(EF, 'rev-parse', K.ZQ_TAG[0] + '^{commit}').strip(),
                gs(EF, 'cat-file', '-p', 'refs/tags/' + K.ZQ_TAG[0])),
        ef_tags_entering=sorted(t for t in gs(EF, 'tag', '--points-at', K.ZQ_ENTERING).split(NL) if t.strip()),
        ef_since=[l for l in gs(EF, 'log', '--all', '--format=%H %ct').split(NL) if l.strip() and int(l.split()[1]) >= (_ct(ROOT, K.ACT_CURRENT_COMMIT) or 0)],   # ### any EF commit since the act opened (none: no Lean file written)
        box_src=_s(blob(EF, '%s:SIDEExplicitFormula/Schema/ZetaBox/Box.lean' % K.ZQ_TIP)),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b752_dispatch_rows.json') or '[]'), reproduce=rd('b752_reproduce.txt'), reproducej=jl('b752_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b752_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b751 left them
        rebuild=None, rebuild_rows=json.loads(rd('b752_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               lit=_ct(ROOT, K.C2_PLAN_FIRST), s5pp=_ct(PP, K.C2_PP[0]), s2=_ct(ROOT, K.C2_RELAY), c3=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), s2=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY[0]),
                   c1pp_=files_of(PP, K.C1_PP), lit=files_of(ROOT, K.C2_PLAN_FIRST), s5pp=files_of(PP, K.C2_PP[0]),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b752's read-first bank's items by path, as its step zero wrote them (data/b752_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b751_closing.txt |', 'relay data/b751_events.txt |', 'relay data/b751_defects.txt |',
                     'relay data/b751_prevrun_standing-a2.txt :70, data/b751_arms_prerun_standing-a2.txt :26, :69 |',
                     'relay data/b751_author_answers.txt :7, :34, :37; data/b751_author_words.txt |',
                     'relay data/b751_section5.txt, data/b751_literature.txt, data/b751_line.txt, data/b751_rules.txt |',
                     'PLACE-papers PATHS_TO_THE_CRITICAL_LINE.md |', 'PLACE-papers OPEN_TRAILS.md |', 'PLACE-papers day1/Which_Structure_Confines.md v2.3.1 |',
                     'PLACE-papers day1/Which_Structure_Confines_v2_4_0.md v2.4.0 |', 'PLACE-papers day1/Seven_Mechanism_Classes.md v3.3.1 |',
                     'PLACE-papers INSTRUMENTS.md |', 'relay data/b750_cq_sign.txt, tools/b750_cq_sign.py (a1655706) |', 'relay data/b725_interference.txt |',
                     'relay data/b746_order_draft.txt, data/b747_order_entry.txt, data/b747_rules.txt, data/b723_dial_price.txt, data/b723_registrations.txt, data/b736_sitting.txt |',
                     'SIDE-kernel at 0e5233f0 (v1.5) |', 'SIDE-explicit-formula at 14ca5725 (v0.38) |', 'D:/.claude/settings.json |',
                     'relay data/b751_ferry.txt |', 'relay data/b751_stepzero.txt |', 'relay data/b751_standing_v1310.txt |', 'relay data/b750_cq_sign.txt |',
                     'relay data/b736_sitting.txt |')   # ### b752 Component 1, (R362)(7)(vi): the 23 rows of data/b752_readfirst_rows.json by their paths, the carried b751 needles (refused by R7) replaced
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R362)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'LITERATURE AND SECTION 5 ((R362)(2))', 'LINE ((R362)(4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (168 = 168 + 0, data/b752_citation_check.txt :182), no miss; the
    check HALTED on one Lean-path row (:183), that row read in the step-zero bank (data/b752_stepzero.txt :62, b736's form: the cites reader
    passing over the dotted name at AbsMax.lean :405, no word of the ruling wrong); the bank written before the step-zero banks' commit and
    that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 168 \
        and '### ### **THE CHECK HALTED** (halts 1: Lean paths and nouns 1, comparatives 0)' in c \
        and '## THE ONE HALT ROW OF THE CITATION CHECK, READ' in (S['stepz'] or '') and 'AbsMax.lean :405' in (S['stepz'] or '') \
#⟪END⟫
# ### b752, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b751's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b752, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R362)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b751()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R362)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b752_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b751's figures, read at FINDINGS :14667 as Component 1 landed them (b751's closing head quoted)
    return landed(S, 0, ['b751 AT ITS WEIGHT', 'suite 112 of 116', 'relay 766f0363', '25 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b752's title in the ferry's Component 4 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## THE_EPSTEIN_CONTROL_OBJECT §5 passed, 1505 words, 77 cites; ',
                 'the located zero an instance of Voronin’s theorem by the banked search at its numerical value, ',
                 'its certified enclosure 0.85326 ≤ Re ρ ≤ 1.05326 holding Re s = 1 and deciding neither side; ',
                 'the part-order guard, the (W) refusal, the composer on every prompt, the line reader’s match and 11 repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R362)(1), (3): the generated entry for b751's seven events and twenty-five defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(7), the defects by the one lettering (a)-(y); every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 3, CLOSE 29 over 32, REPEAT 17; the navigator's (f) among them, none entered apart); the
    repairs at tools/standing/ v1.31.0 by their controls bank; the corrigenda bank appended at row (71) and nothing before it changed; in
    Component 1's commits (the figures read from data/b752_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 25 and len(items) == j.get('items') == 32 and j.get('row') == 71 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 32 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 3 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 17 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.31.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 and len(j.get('entered') or []) == 0 \
        and '  (71) ' in S['corrigenda'] and '  (72) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R362)(3) orders the rules bank data/b752_rules.txt, one row per repair, eleven rows (1)-(11); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here first committed with v1.31.0 (C1_RULES), in no other commit."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', S['rules'] or '')] == list(range(1, 12)) and 'data/b752_rules.txt' in S['files']['rules'] \
        and sorted(gs(ROOT, 'log', '--format=%H', '--', 'data/b752_rules.txt').split()) == sorted(gs(ROOT, 'rev-parse', K.C1_RULES).split()) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b752's keys, the report sections' own heads
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.31.0', 'REGISTERED -- THE LITERATURE', 'REGISTERED -- §5 OF THE_EPSTEIN_CONTROL_OBJECT',
               'REGISTERED -- THE INTEGRATION LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b752: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b752, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b752_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b752, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail; the paper THE_EPSTEIN_CONTROL_OBJECT_v0_1: §5 and its dated note), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b752's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The literature and §5**', '**The integration line**',
                 '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b752_corrigendum.txt', 'data/b752_standing_v1310.txt', 'data/b752_rules.txt', 'data/b752_literature.txt', 'data/b752_section5.txt',
                 'data/b752_author_answers.txt', 'data/b752_line.txt',
                 'data/b752_reproduce.txt', 'data/b752_address_scan.txt', 'data/b752_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage SYNTHESISED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ('e', 'h', 'i', 'j', 'k', 'l')   # ### b752: the navigator's rows of the defects bank, (e) (the read-first paths) and (h)-(l) (§5's, at [S5]); the rest the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R362)(1)-(2), N2, N5 (the name the frozen run list carries): the PLACE-papers writes in their order -- the weight and corrigendum in
    a commit touching FINDINGS alone in one hunk, its first two added lines b751 at its weight ("*Appended 2026-11-10 by b752 to b751’s
    entry") and the corrigendum's heading ("## Corrigendum to b751’s record"), removing none; then §5 on [S5]'s pass, one commit touching
    the paper alone, adding its lines and removing none (numstat 40 0), after the literature bank's relay commit; the paper at that commit
    its base's bytes with lines added alone (every base line kept in order) and the draft of the section bank spliced whole; the plans of
    b744 unedited at their step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    t_ = S['t']
    dd_ = S['disch_diff'] or {}
    a0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    r0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('-') and not l.startswith('---')]
    hunks_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(a0_) >= 2 and len(hunks_) == 1 and a0_[0].startswith('+*Appended 2026-11-10 by b752 to b751’s entry') \
        and a0_[1].startswith('+## Corrigendum to b751’s record') and r0_ == []
    s5_ = K.C2_PP[0]
    num_ = (S['numstat'].get(s5_) or []) == ['40', '0', K.SECTION_FILE]
    pre_ = _txt(S['paper_pre']).split(NL)
    at_ = _txt(S['paper_at']).split(NL)
    it_ = iter(at_)
    kept_ = bool(pre_) and all(any(x_ == y_ for y_ in it_) for x_ in pre_)   # ### every base line kept, in order
    dr_ = _draft_of(S['sec'])
    spliced_ = bool(dr_) and NL.join(dr_) in NL.join(at_)
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    return bool(one_) and S['reg_pp'].get(K.C1_PP) == ['FINDINGS.md'] and S['reg_pp'].get(s5_) == [K.SECTION_FILE] and num_ and kept_ and spliced_ and md_ \
        and t_.get('c1pp') and t_.get('lit') and t_.get('s5pp') and t_['c1pp'] <= t_['lit'] < t_['s5pp'] and K.SECTION_FILE in K.PP_WRITTEN \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b752_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R362)(1)-(4), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, v1.31.0, the weight and
    corrigendum (PLACE-papers, then relay), the literature bank strictly before §5 in PLACE-papers, then the section bank, then the line
    bank; by ancestry within the relay v9, v1.31.0, the corrigendum, the literature, the section bank, the line bank."""
    t_ = S['t']
    ks_ = ('stepzero', 'standing', 'c1pp', 'corr', 'lit', 's5pp', 's2', 'c3')
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) and t_['lit'] < t_['s5pp'] \
        and bool(S['anc']) and len(S['anc']) == 5 and all(v is True for v in S['anc'].values())
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R362)(2), N2, N3 (the name the frozen run list carries): the literature and §5 -- the literature bank at HEAD its blob at its
    commit (C2_PLAN_FIRST), committed without the section bank; its source read (Lee's arXiv 1204.6297v1 by its sha256), the sources not
    read named, its rows K1-K3 and L1-L4 present and in order, its foot naming the enclosure holding Re s = 1 and the navigator's search
    with no finding; the section bank at HEAD its blob at its commit (C2_RELAY), the author's answer at its head verbatim as the answers
    bank carries it, its foot [S5] PASSED written at the PLACE-papers commit, its D1-D6 rows; the put bank naming [S5]; the paper at HEAD
    carrying the draft whole and the dated note; the draft naming Voronin, Lee and Davenport-Heilbronn and the two figures."""
    return _lit_ok(S)


# ### the record section's INTEGRATION_LINE, the same bytes (the checks and the record are separate modules; G-COUNT-ROUTE-PRICED reads the line
# ### bank against it, and the record's entry ends with it)
_INTEG_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
               'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage SYNTHESISED')


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


LIT_SHA = '3a03f046d8fcfb629e886073c55d491628e7820d2c9b12565fb712a8c061e171'   # ### Lee arXiv:1204.6297v1's PDF as the seat read it (data/b752_literature.txt :24)
S5_ANSWER = ('Pass [S5]: §5 written under :170 as drafted, D1-D6 as the draft states them; the ruling’s (v) and its figures in D2-D5 entered as the '
             'navigator’s defects, CLAIM, NEW; one PLACE-papers write, then the dated note after :9, the version v0.1 kept.')


def _lit_ok(S):
    l_ = _txt(S['lit'])
    s_ = _txt(S['sec'])
    t_ = S['t']
    rows_ = [l_.find(r_) for r_ in ('\n  K1  ', '\n  K2  ', '\n  K3  ', '\n  L1  ', '\n  L2  ', '\n  L3  ', '\n  L4  ', '\n  V1  ', '\n  V2  ')]
    lv_ = _vlast(l_)
    sv_ = _vlast(s_)
    dr_ = NL.join(_draft_of(s_))
    head_ = ' '.join(x_[4:].strip() for x_ in s_.split(NL)[2:6])   # ### the section bank's head, :3-:6, its `### ` cut and the lines joined
    pj_ = S['putj'] or {}
    paper_ = _txt(S['paper'])
    lb_, sb_ = _txt(S['lit_blob']), _txt(S['sec_blob'])
    # ### each bank at HEAD its blob at its commit with its foot line appended after it and nothing else (the feet added at Component 4)
    app_ = lambda t_, b_: bool(b_) and t_.startswith(b_) and all(not x_.strip() or x_.startswith('### ### **') for x_ in t_[len(b_):].split(NL))
    return bool(l_) and app_(l_, lb_) and 'data/b752_literature.txt' in S['files']['lit'] and K.SECTION_BANK not in S['files']['lit'] \
        and LIT_SHA in l_ and '## THE SOURCES NOT READ' in l_ and all(i_ >= 0 for i_ in rows_) and rows_ == sorted(rows_) \
        and lv_.startswith('THE LITERATURE: QUERIES 3 ; SOURCES READ 1 ') and 'CONTAINS Re s = 1' in lv_ and lv_.endswith('NO FINDING 1.') \
        and bool(s_) and app_(s_, sb_) and S5_ANSWER in head_ and S5_ANSWER in _txt(S['zanswers']) \
        and sv_.startswith('§5: WORDS 1505 ; LINE CITES 77 ; [S5] PASSED ; WRITTEN AT PLACE-papers %s,' % K.C2_PP[0][:8]) \
        and all(('\n  (D%d) ' % i_) in s_ for i_ in range(1, 7)) and '\n  (D7) ' not in s_ \
        and '[S5]' in json.dumps(pj_, ensure_ascii=False) \
        and bool(dr_) and dr_ in paper_ and '*Dated note, 2026-11-10, b752:' in paper_ \
        and all(w_ in dr_ for w_ in ('Voronin', 'Lee', '1204.6297', 'Davenport', '0.85326', '1.05326', '0.95326')) \
        and t_.get('lit') and t_.get('s2') and t_['lit'] < t_['s2']
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R362)(6) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b751 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b751's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
    worklist's and its peel 14ca5725, the only tag at that commit and no tag added this act; no sitting kernel."""
    tp = S['ef_tips'] or {}
    zt = S['zq_tag'] or ('', '', '')
    return S['ef_main'] == K.EF_MAIN == K.EF_BASE and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and S['zq_files'] == [] and S['zq_log'] == [] and K.ZQ_TIP == K.ZQ_ENTERING and S['ef_since'] == [] and K.ZQ_COMMITS == () and K.ZQ_FILES == () \
        and zt[0] == K.ZQ_TAG[1] and zt[1] == K.ZQ_TAG[2] and ('object %s' % K.ZQ_TAG[2]) in (zt[2] or '') \
        and S['ef_tags_entering'] == [] and 'v0.38' in S['zq_tags'] and not [t_ for t_ in S['zq_tags'] if re.match(r'^v0\.(39|[4-9]\d)', t_)] and not K.SITTING_TIPS

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.31.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1310') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b751's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R362)(2), (4), N2, N3, N5 (the name the frozen run list carries): the answers and the line -- the answers bank written by the record
    tool's appending route (its head the route's, the [S5] prompt with its options and the RESULT row with its time, the author's word on
    [S5] verbatim between BEGIN and END), committed at Component 3 with its json and the line bank, at HEAD its blob there or that blob with
    lines appended (never rewritten); the line bank's foot COMPOSED WITH THE MATCH, STAGE SYNTHESISED, MATCHED 3 OF 3, ALL AS READ, its line
    the act module's INTEGRATION line; Component 3's commit carrying the line bank and its tool; b746's draft unchanged; no Zenodo tool
    this act."""
    r_ = S['rows_bank'] or ''
    v_ = _vlast(r_)
    a_ = _txt(S['zanswers'])
    a3_ = _txt(blob(ROOT, '%s:data/b752_author_answers.txt' % K.C3_RELAY[0]))
    words_ = re.findall(r'BEGIN to END, verbatim:\n([^\n]+)', a_)
    s5row_ = re.search(r'(?m)^RESULT \(transcript line \d+, 2026-11-10T13:11:15\.228Z\): The user answered: "\[S5\]: ', a_)
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b752_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return a_.startswith('### b752 -- THE AUTHOR`S ANSWERS') and bool(a3_) and a_.startswith(a3_) and S5_ANSWER in words_ and s5row_ is not None \
        and 'OPTION 1: Pass [S5] ::' in a_ and 'OPTION 2: Strike [S5] ::' in a_ \
        and {'data/b752_author_answers.txt', 'data/b752_author_answers.json', 'data/b752_line.txt', 'tools/b752_line.py'} <= set(S['files']['c3']) \
        and v_.startswith('THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; STAGE SYNTHESISED ; MATCHED 3 OF 3 ;') \
        and v_.endswith('; ALL AS READ.') and ('      %s' % _INTEG_LINE) in r_ \
        and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at the act's base (unchanged this act) and the working tree's."""
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
    """standing clauses v9 (Component 7 of (R362): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b752_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b751's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R362-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b751's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R362) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b751's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R361)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 8ce7e3ab',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 168 = 168 OK + 0 misses, the check HALTED on one Lean-path row read in the step-zero bank (b736`s form); the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b751-\w+) \((?:was )?[0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s C4 form adjusted to what the act did: THE_EPSTEIN_CONTROL_OBJECT §5 passed, its words and cites; the located zero an instance of Voronin`s theorem by the banked search at its numerical value, the certified enclosure holding Re s = 1 and deciding neither side; the part-order guard, the (W) refusal, the composer, the line reader`s match and the repairs landed, counted from the rules bank',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R362)(1), (3): the generated corrigendum for b751`s record, landed at FINDINGS :14669: its seven events and twenty-five defects, 32 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 3 CLOSE 29, REPEAT 17, the navigator`s (f) among them; v1.31.0`s repairs by data/b752_standing_v1310.txt; the corrigenda bank appended at row (71)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R362)(3)`s rules bank data/b752_rules.txt, eleven rows (1)-(11), committed with v1.31.0 (e46f9e9d) alone',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b752's objects
    ('G-REGISTRATIONS-FIRST', '(R362)(1)-(2), N2, N5: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (42206b44), none removed; §5 on [S5]`s pass one commit touching the paper alone (b07cd7d3), 40 added and none removed, every base line kept and the draft spliced whole, after the literature`s commit (fcc3d9e0); the PLACE-papers order by ancestry',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'numstat', lambda d: d.update({K.C2_PP[0]: ['41', '1', K.SECTION_FILE]}))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b752_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R362)(1)-(4), N2: the act`s order by time -- step zero, v1.31.0, the weight and corrigendum, the literature strictly before §5, the section bank, the line -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(lit_s2=False))),
    ('G-DERIVATION-GRADED', '(R362)(2), N2, N3: the literature bank its blob at fcc3d9e0, without the section bank; Lee`s arXiv 1204.6297v1 by its sha256, the sources not read named, K1-K3 and L1-L4 in order, its foot the enclosure holding Re s = 1 and the navigator`s search with no finding; the section bank its blob at d1180a75, the author`s answer at its head as the answers bank carries it, [S5] PASSED at b07cd7d3, D1-D6; the paper carrying the draft whole and the dated note',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'lit', (S['lit'] or '').replace('NO FINDING 1.', 'NO FINDING 0.'))),
    ('G-OFFSET-POST-HOC', 'N5, (R362)(6): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.31.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R362)(2), (4), N2, N3, N5: the answers bank by the record tool`s appending route, the [S5] prompt with its two options and its RESULT at 2026-11-10T13:11:15.228Z, the author`s word on [S5] verbatim, at HEAD its blob at 3b114797 with lines appended alone; the line bank COMPOSED WITH THE MATCH, stage SYNTHESISED, 3 of 3 matched, ALL AS READ, its line the module`s; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'zanswers', (S['zanswers'] or '').replace('Pass [S5]: §5 written', 'Strike [S5]: §5 written'))),
    ('G-DIFFERS-ERRATA', '(R362)(1), (6): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line and the corrigendum in 42206b44, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b752_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R362-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b751`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b751 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b751 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS, OPEN_TRAILS and THE_EPSTEIN_CONTROL_OBJECT_v0_1, (R362)(1)-(2), (6)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b751`s trail record on OPEN_TRAILS (:18134) and its root in the chain', lambda S: '### b751 — lane two, act one hundred and seventy-eight, the located zero under (R361)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the paper`s §5): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b752 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b751's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b752: (R362)'s rows, written at step zero over b751's carried rows (scratch splice752.py); each figure the ruling states read from a bank or tree it names
    # ### (1)'s line read from the public relay at d921bceb
    pub = _blob('D:/relay', 'd921bceb', 'data/b751_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b751_closing.txt :1, the head line as the public relay carries it at d921bceb', bool(pub) and pub[0] == at(cl, 1) and 'relay 4282ecd2' in pub[0] and 'PLACE-papers 2a94bf8' in pub[0],
        'remote main %s' % rm[:8], '1')
    add('ruling (1)', 'relay remote main read back at d921bceb after b751`s closing push', rm.startswith('d921bceb'), rm[:8], '1')
    for w_ in ('suite 111 of 116', 'root 4dcfc17a6883a7b6', '2 prompts answered', 'scores 8 of 8 HELD', '22 defects'):
        add('ruling (1)', 'data/b751_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1), (7)', 'data/b751_closing.txt :5, the counter CLAIM 10, CLOSE 17, REPEAT 14 OF 27 ; DEFECTS 22, EVENTS 5', 'CLAIM 10, CLOSE 17, REPEAT 14 OF 27' in at(cl, 5) and 'DEFECTS 22, EVENTS 5' in at(cl, 5), at(cl, 5)[-60:], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, d921bceb and 2a94bf8', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('d921bceb') and gr(PP, 'rev-parse', K.PRE_PP).startswith('2a94bf8'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    add('ruling (1)', 'data/b751_closing.txt :141, b750`s corrigendum ITEMS 32 ; CLAIM 3, CLOSE 29 ; REPEAT 17', 'ITEMS 32: EVENTS 7, DEFECTS 25 ; CLAIM 3, CLOSE 29 ; REPEAT 17' in at(cl, 141), at(cl, 141)[-80:], '1')
    add('ruling (1)', 'data/b751_closing.txt :142, tools/standing/ at v1.31.0, CASES 56 ; AS WANTED 56', 'v1.31.0' in at(cl, 142) and 'CASES 56 ; AS WANTED 56' in at(cl, 142), at(cl, 142)[-60:], '1')
    dl1_ = lines_of(p('data', 'b751_defects.txt'))
    ds_ = next((l for l in dl1_ if l.startswith('    (s) ')), '')
    add('ruling (1)', 'data/b751_defects.txt (s), v1.31.0`s scan-left-out guard refusing the component 4 commit', 'commit.scan_left_out' in ds_ and 'Component 4' in ds_, ds_[:60], '1')
    ev1_ = lines_of(p('data', 'b751_events.txt'))
    e2_ = next((l for l in ev1_ if l.startswith('    (2) ')), '')
    add('ruling (1)', 'data/b751_events.txt (2), the part-order guard refusing the act part sent before standing-a1', 'part-order guard' in e2_ and 'standing-a1' in e2_, e2_[:60], '1')
    add('ruling (1)', 'data/b751_closing.txt :147, the literature: QUERIES 3 ; SOURCES READ 1 (arXiv 1204.6297v1) ; NOT READ 3 ; the enclosure 0.85326 <= Re ρ <= 1.05326 CONTAINS Re s = 1',
        all(w_ in at(cl, 147) for w_ in ('QUERIES 3 ; SOURCES READ 1 (arXiv 1204.6297v1', 'NOT READ 3', 'THE CERTIFIED ENCLOSURE 0.85326 <= Re ρ <= 1.05326 CONTAINS Re s = 1')), at(cl, 147)[-60:], '1')
    add('ruling (1)', 'relay fcc3d9e0 adds data/b751_literature.txt (the literature bank before the draft)', 'data/b751_literature.txt' in gr('D:/relay', 'show', '--name-only', '--format=', 'fcc3d9e0').split(), gr('D:/relay', 'log', '-1', '--format=%s', 'fcc3d9e0')[:60], '1')
    add('ruling (1)', 'data/b751_closing.txt :148, §5: WORDS 1505 ; LINE CITES 77 ; [S5] PASSED ; PLACE-papers b07cd7d3 ; D1-D6', all(w_ in at(cl, 148) for w_ in ('WORDS 1505 ; LINE CITES 77 ; [S5] PASSED', 'WRITTEN AT PLACE-papers b07cd7d3', '(D1-D6)')), at(cl, 148)[-60:], '1')
    add('ruling (1)', 'PLACE-papers b07cd7d3 touches THE_EPSTEIN_CONTROL_OBJECT_v0_1.md alone', gr(PP, 'show', '--name-only', '--format=', 'b07cd7d3').split() == ['phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'], gr(PP, 'log', '-1', '--format=%s', 'b07cd7d3')[:60], '1')
    nav_ = [l[5:6] for l in dl1_ if re.match(r"^    \([a-z]\) THE NAVIGATOR'S ", l)]
    lt1_ = [m_.group(1) for m_ in (re.match(r"^    \(([a-z]'?)\) ", l) for l in dl1_) if m_]
    add('ruling (1), (7)', 'data/b751_defects.txt, the navigator`s defects (e), (h), (i), (j), (k), (l); 22 letters (a)-(v)', nav_ == ['e', 'h', 'i', 'j', 'k', 'l'] and lt1_ == list('abcdefghijklmnopqrstuv'), '%s ; %d' % (''.join(nav_), len(lt1_)), '1')
    add('ruling (1)', 'data/b751_closing.txt :153, the line: STAGE SYNTHESISED ; MATCHED 3 OF 3', 'STAGE SYNTHESISED ; MATCHED 3 OF 3' in at(cl, 153), at(cl, 153)[-60:], '1')
    for c_, w_ in (('eb81ada2', 'lock'), ('129a8ca7', 'seal')):
        add('ruling (1)', 'relay %s, b751`s %s' % (c_, w_), gr('D:/relay', 'log', '-1', '--format=%s', c_).startswith('b751 %s' % w_), gr('D:/relay', 'log', '-1', '--format=%s', c_)[:60], '1')
    an1_ = lines_of(p('data', 'b751_author_answers.txt'))
    add('ruling (1)', 'data/b751_author_answers.txt :7, the [S5] answer standing (13:11:15.228Z)', '13:11:15.228Z' in at(an1_, 7) and '[S5]' in at(an1_, 7), at(an1_, 7)[:60], '1')
    e4_ = next((l for l in ev1_ if l.startswith('    (4) ')), '')
    add('ruling (1), (7)(iv)', 'data/b751_events.txt (4), the two identical go words banked as one row', 'answers route' in e4_, e4_[:60], '1')
    add('ruling (1), (3)', 'OPEN_TRAILS.md :18148, the tighter box named as a candidate beside W-ORD-ZQ-FAMILY, no entry written', at(ot, 18148).startswith('**A candidate order beside W-ORD-ZQ-FAMILY, named and not entered:**') and 'no entry written' in at(ot, 18148), at(ot, 18148)[:60], '1')
    add('ruling (1)', 'data/b751_closing.txt :188, (N1)-(N5) and (S1)-(S3) HELD', at(cl, 188).count('HELD') == 8, at(cl, 188)[:60], '1')
    e1_ = next((l for l in ev1_ if l.startswith('    (1) ')), '')
    e3_ = NL.join(ev1_[ev1_.index(next((l for l in ev1_ if l.startswith('    (3) ')), ev1_[0])):][:4])
    add('ruling (1), (7)(ii)', 'data/b751_events.txt (1), G-RULE-REMOTE-REREAD on the call of 17:54:13Z the hook refused', 'G-RULE-REMOTE-REREAD' in e1_ and '17:54:13.904Z' in NL.join(ev1_[:8]), e1_[:60], '1')
    add('ruling (1), (7)(iii)', 'data/b751_events.txt (3), G-CURRENTS-UNEDITED failing on b750`s banks alone', 'G-CURRENTS-UNEDITED' in e3_, 'read' if 'G-CURRENTS-UNEDITED' in e3_ else 'ABSENT', '1')
    pr2_ = lines_of(p('data', 'b751_prevrun_standing-a2.txt'))
    pa2_ = lines_of(p('data', 'b751_arms_prerun_standing-a2.txt'))
    add('ruling (1), (7)(iii), ferry (read first)', 'data/b751_prevrun_standing-a2.txt :70 G-CURRENTS-UNEDITED FAILS on b750`s banks; data/b751_arms_prerun_standing-a2.txt :69 OK on b751`s',
        at(pr2_, 70).split()[:1] == ['G-CURRENTS-UNEDITED'] and at(pr2_, 70).rstrip().endswith('### FAILS') and at(pa2_, 69).split()[:1] == ['G-CURRENTS-UNEDITED'] and at(pa2_, 69).rstrip().endswith('OK'), at(pr2_, 70)[-12:], '1')
    add('ruling (1), (7)(ii), ferry (read first)', 'data/b751_arms_prerun_standing-a2.txt :26, G-RULE-REMOTE-REREAD naming the call of 2026-11-10T17:54:13.904Z', 'G-RULE-REMOTE-REREAD' in at(pa2_, 26) and "['2026-11-10T17:54:13.904Z']" in at(pa2_, 26), at(pa2_, 26)[:60], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar1_ = [x for x in ar_ if x[:1] == ['b751']]
    add('ruling (1)', 'data/act_roots.txt, b751`s root 4dcfc17a chained from fbd3c1d6', len(ar1_) == 1 and ar1_[0][1].startswith('4dcfc17a') and ar1_[0][2].startswith('fbd3c1d6'), ' '.join(x_[:8] for x_ in (ar1_[0] if ar1_ else [])), '1')
    add('ruling (scope), (1)', 'data/b751_closing.txt :173, the mirror sha256 c04ffd05, MANIFEST md5 f4d4055e, CLEAN ON ALL THREE CLAUSES', 'sha256 c04ffd05' in at(cl, 173) and 'MANIFEST md5 f4d4055e' in at(cl, 173) and 'CLEAN ON ALL THREE CLAUSES' in at(cl, 173), at(cl, 173)[:60], '1')
    add('ruling (1), ferry (read first)', 'data/b751_author_answers.txt :37, the author`s word at the root: the plan act as b752, §6 after it',
        at(an1_, 37).startswith('Confirmed: plan act next, the attribution order’s plan act as b752') and at(an1_, 37).rstrip().endswith('§6 of the paper after it.'), at(an1_, 37)[:60], '1')
    aw1_ = rd(p('data', 'b751_author_words.txt')) or ''
    add('ruling (1), ferry (read first)', 'data/b751_author_words.txt carries the root word verbatim', at(an1_, 37).strip() in aw1_, 'read', '1')
    # ### (R362)(2): the navigator's correction -- each corpus line it names, read at HEAD
    pt_ = lines_of(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md'))
    add('ruling (2)(i), (5)(iv), ferry (read first)', 'PATHS_TO_THE_CRITICAL_LINE.md :389 A9, Λ(n) ≥ 0 to the zero-free region near σ = 1, 3-4-1, vonMangoldt_nonneg', at(pt_, 389).startswith('| A9 |') and '3-4-1' in at(pt_, 389) and 'ArithmeticFunction.vonMangoldt_nonneg' in at(pt_, 389), at(pt_, 389)[:60], '1')
    add('ruling (2)(i), (5)(iv), ferry (read first)', 'PATHS_TO_THE_CRITICAL_LINE.md :396 B3, the Λ≥0 → σ gap', at(pt_, 396).startswith('- **B3**') and 'the `Λ≥0 → σ` gap' in at(pt_, 396), at(pt_, 396)[:60], '1')
    add('ruling (2)(i), (5)(iv), ferry (read first)', 'PATHS_TO_THE_CRITICAL_LINE.md :410 C1, positivity to the σ = 1 edge, universally', at(pt_, 410).startswith('- **C1 — Positivity → the σ = 1 edge, *universally*.**'), at(pt_, 410)[:60], '1')
    for n_, nd_ in ((16589, '**`W-ORD-MECHANISM-TABLE` ENTERED 2026-10-30, b725'), (12891, '*Appended 2026-10-04 by b623'), (14396, '*Appended 2026-10-16 by b671'),
                    (15502, '*Appended 2026-10-22 by b703'), (16376, '**The hypotheses:**'), (16591, '**`W-ORD-ADMISSIBLE-CONE` ENTERED 2026-10-30, b725'),
                    (17714, '**`W-ORD-LI-ARITH` ENTERED at b743'), (17716, '**`W-ORD-ZQ-FAMILY` ENTERED at b743'), (17932, '*Appended 2026-11-08 by b747')):
        add('ruling (2), (3), ferry (read first)', 'OPEN_TRAILS.md :%d, %s' % (n_, nd_.strip('*`')[:50]), at(ot, n_).startswith(nd_), at(ot, n_)[:60], '1')
    add('ruling (2)(iv), (3)', 'OPEN_TRAILS.md :12891 W-ORD-PLATT-RUNG, PRICED, NOT STARTED', 'W-ORD-PLATT-RUNG, PRICED, NOT STARTED' in at(ot, 12891), 'read', '1')
    add('ruling (3)', 'OPEN_TRAILS.md :17932 THE ORDER W-ORD-MECHANISM-ATTRIBUTION', 'W-ORD-MECHANISM-ATTRIBUTION' in at(ot, 17932), 'read', '1')
    add('ruling (3)', 'OPEN_TRAILS.md :15502 W-ORD-QUASI-RH-FIELD-WATCH; :16591 Q0`s exit direction', 'W-ORD-QUASI-RH-FIELD-WATCH' in at(ot, 15502) and 'Q0’s exit direction' in at(ot, 16591), 'read', '1')
    for n_ in (18002, 18048, 18096, 18144):
        add('ruling (7)(v), ferry (read first)', 'OPEN_TRAILS.md :%d, an open-orders line carrying `W-ORD-1`' % n_, at(ot, n_).startswith('**The open orders:**') and '`W-ORD-1`' in at(ot, n_), 'W-ORD-1 %s' % ('present' if '`W-ORD-1`' in at(ot, n_) else 'ABSENT'), '1')
    add('ruling (7)(v)', 'OPEN_TRAILS.md :18146, the count 73 of 208', '73 of 208 open' in at(ot, 18146), at(ot, 18146)[:60], '1')
    ws_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines.md'))
    ws4_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines_v2_4_0.md'))
    add('ruling (2)(iii), ferry (read first)', 'day1/Which_Structure_Confines.md at v2.3.1 (:3, the version alone read, the line not printed)', 'v2.3.1' in at(ws_, 3), 'v2.3.1' if 'v2.3.1' in at(ws_, 3) else 'OTHER', '1')
    add('ruling (2)(iii), ferry (read first)', 'Which_Structure_Confines v2.3.1 :40 Davenport-Heilbronn 1936; Voronin 1976 for the Epstein case; :117 the Selberg class; :176 the comparison is the contribution',
        at(ws_, 40).startswith('**Theorem (Davenport–Heilbronn 1936; Voronin 1976 for the Epstein case).**') and 'Selberg class' in at(ws_, 117) and 'comparison is the contribution' in at(ws_, 176), at(ws_, 40)[:60], '1')
    add('ruling (2)(iii), (8), ferry (read first)', 'day1/Which_Structure_Confines_v2_4_0.md at v2.4.0 (:3, the version alone read); the three lines of (2)(iii) at :40, :117, :176 are v2.3.1`s, the v2.4.0 file carrying "the comparison is the contribution" at :198',
        'v2.4.0' in at(ws4_, 3) and 'comparison is the contribution' in at(ws4_, 198) and not at(ws4_, 40).startswith('**Theorem (Davenport–Heilbronn'), 'v2.4.0 :198', '1')
    sm_ = lines_of(os.path.join(PP, 'day1', 'Seven_Mechanism_Classes.md'))
    add('ferry (read first), (5)(i)', 'day1/Seven_Mechanism_Classes.md v3.3.1 (:7); :11 the definition of a mechanism class; :44, :46, :62, :64, :86, :88 classes C1, C2, C4, C5, C6, C7',
        at(sm_, 7).startswith('*v3.3.1') and at(sm_, 11).startswith('**Framing.** A mechanism class is a derivable chain') and all(at(sm_, n_).startswith('**Class C%s' % c_) for n_, c_ in ((44, '₁'), (46, '₂'), (62, '₄'), (64, '₅'), (86, '₆'), (88, '₇'))),
        at(sm_, 11)[:60], '1')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    add('ferry (read first), (4)', 'INSTRUMENTS.md :764, I-109, the sign of cQ(n) over n <= 3000', at(ins_, 764).startswith('## I-109'), at(ins_, 764)[:40], '1')
    # ### (R362)(3)-(5): the relay banks and the trees the act reads
    cq0_ = lines_of(p('data', 'b750_cq_sign.txt'))
    add('ruling (4), ferry (read first)', 'data/b750_cq_sign.txt :39, the control: EXACTLY ZERO 2498, NONNEGATIVE 399, NEGATIVE 102, THE SMALLEST NEGATIVE n = 48',
        all(w_ in at(cq0_, 39) for w_ in ('NEGATIVE 102', 'THE SMALLEST NEGATIVE n = 48', 'EXACTLY ZERO 2498', 'NONNEGATIVE 399')), at(cq0_, 39)[:60], '2')
    add('ruling (4), ferry (read first)', 'tools/b750_cq_sign.py tracked, the route (4) recomputes by', bool(gr('D:/relay', 'ls-files', '--', 'tools/b750_cq_sign.py')), gr('D:/relay', 'log', '-1', '--format=%h', '--', 'tools/b750_cq_sign.py'), '2')
    it_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (6) T0, ferry (read first)', 'data/b725_interference.txt :11, r_Q0 at 2 and 3 zero, at 6 four (the first coefficients)', ' 2: 0 2 2 -1 ' in at(it_, 11) and ' 3: 0 2 2 -1 ' in at(it_, 11) and ' 6: 4 2 4 1 ' in at(it_, 11), at(it_, 11)[:60], '2')
    for f_ in ('data/b746_order_draft.txt', 'data/b747_order_entry.txt', 'data/b747_rules.txt', 'data/b723_dial_price.txt', 'data/b723_registrations.txt', 'data/b736_sitting.txt',
               'data/b751_section5.txt', 'data/b751_literature.txt', 'data/b751_line.txt', 'data/b751_rules.txt'):
        add('ferry (read first)', '%s tracked at d921bceb' % f_, bool(_blob('D:/relay', 'd921bceb', f_)), '%d lines' % len(_blob('D:/relay', 'd921bceb', f_).split(NL)), '2')
    kb_ = _blob('D:/SIDE-kernel', '0e5233f0', 'Bridge/TheBridgeComplete.lean').replace(chr(13), '').split(NL)
    add('ruling (5)(i), ferry (read first)', 'SIDE-kernel v1.5 (0e5233f0) Bridge/TheBridgeComplete.lean :20-:23 inductive MechanismClass, :25 seven_classes',
        at(kb_, 20).startswith('inductive MechanismClass where') and 'C1_schwarz' in at(kb_, 21) and 'C7_hadamard' in at(kb_, 22) and at(kb_, 25).startswith('theorem seven_classes : Fintype.card MechanismClass = 7'),
        at(kb_, 25)[:50], '2')
    add('ruling (5)(i)', 'SIDE-kernel`s tag v1.5 peels to 0e5233f0', gr('D:/SIDE-kernel', 'rev-parse', 'v1.5^{}').startswith('0e5233f0'), gr('D:/SIDE-kernel', 'rev-parse', 'v1.5^{}')[:8], '2')
    EF_ = 'D:/SIDE-explicit-formula'
    ef_ = lambda c_, f_: _blob(EF_, c_, f_).replace(chr(13), '').split(NL)   # noqa: E731
    tp_ = gr(EF_, 'rev-parse', 'v0.38^{}')
    add('ruling (5)(ii), (10)', 'the tag v0.38 on SIDE-explicit-formula peeling to 14ca5725, no tag beyond it', tp_.startswith('14ca5725') and not gr(EF_, 'tag', '--list', 'v0.39*') and not gr(EF_, 'tag', '--list', 'v0.4?'), tp_[:8], '2')
    add('ruling (10)', 'SIDE-explicit-formula main as the worklist carries it (unmoved, no merge)', gr(EF_, 'rev-parse', 'main') == K.EF_MAIN, gr(EF_, 'rev-parse', 'main')[:8], '2')
    ezq_ = ef_('14ca5725', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean')
    ld_ = ef_('14ca5725', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean')
    sp4_ = ef_('14ca5725', 'SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean')
    add('ruling (5)(ii), ferry (read first)', 'Schema/EpsteinZQ.lean :59 def rQ; Schema/ZQ/LogDeriv.lean :63-:65 def cQ, the recursion, at v0.38',
        at(ezq_, 59).startswith('def rQ (k : ℕ) : ℕ :=') and at(ld_, 63).startswith('def cQ (n : ℕ) : ℝ :=') and 'n.properDivisors' in at(ld_, 65), at(ld_, 63)[:40], '2')
    add('ruling (2), ferry (read first)', 'Schema/ZQ/OffZero/SP4.lean :32 zq_offline_zero and :36 zq_li_nonneg_fails at v0.38', at(sp4_, 32).startswith('theorem zq_offline_zero : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1 / 2')
        and at(sp4_, 36).startswith('theorem zq_li_nonneg_fails : ¬ (∀ n : ℕ, 0 ≤ Wide.liCoeff zqZeroConfig n)'), at(sp4_, 32)[:40], '2')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.32.0's commit's parent once it lands, HEAD's blob before
    add('ferry', 'tools/standing/VERSION v1.31.0 entering the act', v0_ == 'v1.31.0', v0_, '1')
    for f_ in ('data/b751_relay_push-b751-closing_push_out.txt', 'tools/mirror_prevbuild.json'):
        add('ruling (7)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (7), ferry (read first)', 'events (1)-(5) and 22 defects (data/b751_events.txt, data/b751_defects.txt)',
        starts == list(range(1, 6)) and len(letters) == 22, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    for n_, k_, w_ in ((4, 1, "THE SEAT'S [CLOSE ; NEW]"), (9, 2, "THE SEAT'S [CLOSE ; REPEAT b750 (3)]"), (13, 3, "THE SEAT'S [CLAIM ; NEW]"),
                       (19, 4, "THE SEAT'S [CLAIM ; NEW]"), (25, 5, "THE HOST'S [CLOSE ; NEW]")):
        add('ruling (7), ferry (read first)', 'data/b751_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    add('ruling (7)(ix)', 'data/b751_events.txt :25-:28, (5) the PLACE-papers push refused at the network and re-sent once', 'Could not' in NL.join(ev[24:28]) and 'the retry is this row' in NL.join(ev[24:28]), at(ev, 25)[:60], '1')
    df_ = lines_of(p('data', 'b751_defects.txt'))
    S_, N_ = "THE SEAT'S", "THE NAVIGATOR'S"
    TAGS_ = (('a', S_, 'CLOSE ; REPEAT b750 (a)'), ('b', S_, 'CLAIM ; REPEAT b750 (d)'), ('c', S_, 'CLOSE ; REPEAT b750 (c)'), ('d', S_, 'CLOSE ; REPEAT b736 (e)'),
             ('e', N_, 'CLAIM ; REPEAT b750 (f)'), ('f', S_, 'CLOSE ; REPEAT b751 (a)'), ('g', S_, 'CLOSE ; NEW'), ('h', N_, 'CLAIM ; NEW'),
             ('i', N_, 'CLAIM ; NEW'), ('j', N_, 'CLAIM ; NEW'), ('k', N_, 'CLAIM ; NEW'), ('l', N_, 'CLAIM ; NEW'),
             ('m', S_, 'CLOSE ; NEW'), ('n', S_, 'CLOSE ; REPEAT b751 (f)'), ('o', S_, 'CLOSE ; NEW'), ('p', S_, 'CLOSE ; REPEAT b751 (g)'),
             ('q', S_, 'CLAIM ; REPEAT b751 (b)'), ('r', S_, 'CLOSE ; REPEAT b751 (n)'), ('s', S_, 'CLOSE ; REPEAT b750 (x)'), ('t', S_, 'CLOSE ; NEW'),
             ('u', S_, 'CLOSE ; REPEAT b751 (n)'), ('v', S_, 'CLOSE ; REPEAT b751 (u)'))
    for n_, (l_, o_, t_) in zip(range(7, 29), TAGS_):
        add('ruling (7), ferry (read first)', "data/b751_defects.txt :%d, (%s) %s [%s]" % (n_, l_, o_, t_), at(df_, n_).startswith("    (%s) %s [%s]" % (l_, o_, t_)), at(df_, n_)[:60], '1')
    add('ruling (7)(viii)', 'data/b751_defects.txt :13 (g) and :22 (p), the LIMIT row`s false refusals (a quoted string; a line count)', 'quoted test string' in at(df_, 13) and '`wc -l`' in at(df_, 22), at(df_, 22)[:60], '1')
    add('ruling (7)(vii)', 'data/b751_defects.txt :26 (t), `--quiet` read as an act', "read `--quiet` as the act" in at(df_, 26), at(df_, 26)[:60], '1')
    add('ruling (7)(vi)', 'data/b751_defects.txt :8 (b) and :23 (q), the carry`s rows unread', 'citation sections 1, 4, 5, 8' in at(df_, 8) and 'READFIRST_NEEDLES' in at(df_, 23), at(df_, 23)[:60], '1')
    add('ruling (7)(ix)', 'data/b751_defects.txt :10 (d), the citation check`s dotted name', 'dotted name' in at(df_, 10), at(df_, 10)[:60], '1')
    add('ruling (7)(iv)', 'data/b751_defects.txt :19 (m), the answers dry printing counts alone', 'the dry printed the counts alone' in at(df_, 19), at(df_, 19)[:60], '1')
    ln4_ = lines_of(p('data', 'b751_line.txt'))
    add('ruling (1), (8)', 'data/b751_line.txt, the line`s foot: SYNTHESISED, 3 of 3', any('SYNTHESISED' in l_ and '3 OF 3' in l_ for l_ in ln4_[-6:]), (ln4_[-2] if len(ln4_) > 1 else '')[:60], '1')
    add('ruling (1)', 'FINDINGS :%d, b751`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## '), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b750`s weight line and corrigendum (b751`s), the form b752`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fi, K.B711_WEIGHT)) and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum'), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b751`s trail record, its hand section' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b751 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (1), (7)(v)', 'OPEN_TRAILS :%d, b751`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('ferry (read first)', 'the hook`s settings file D:/.claude/settings.json by its hash alone', bool(__import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), __import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.31.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.31.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R362)(1): b751's export, the mirror's last
    add('ruling (1)', '%s, b751`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: SIDE-explicit-formula and the other clones at the paths the worklist holds, each listed, a path absent printed absent
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R362)(3), (5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), (6)', 'the push-b751-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R362)(3), (5): act_current alone, then b751's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b751_relay_push-b751-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['tools/mirror_prevbuild.json'])):
        if fs_ == ['tools/mirror_prevbuild.json'] and not c_:   # ### b752: committed alone if it differs from HEAD's blob beyond line endings, else restored
            hb_ = gr('D:/relay', 'rev-parse', 'HEAD:tools/mirror_prevbuild.json')
            add('ruling (3)', 'tools/mirror_prevbuild.json at HEAD`s blob %s (equal, or to be committed alone after this check)' % hb_[:8], True,
                'blob %s ; HEAD %s' % (gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json')[:8], hb_[:8]), '0')
            continue
        if not c_:
            add('ruling (3), (5)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3), (5)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3), (6)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (3), (6)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3), (6)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b752_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b752_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b752 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b751_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.31.0's controls and the rules, the literature bank, the section bank and the answers bank, the line bank, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R362)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R362)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R362)(6): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b752 ((R362)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R361)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b752 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTY-NINE, THE ATTRIBUTION PLAN: b751 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON '
              'THE NAVIGATOR`S RULINGS FROM RECALL AND THE ARM THAT READ A REFUSED CALL; THE CROSS-REFERENCE BANKED; THE CLASS-GROUP SIGNATURE OF THE NEGATIVE n '
              'COMPUTED; THE KERNEL`S CLASSES READ AS STATEMENTS; THE PLAN PUT AS [P1]; NOTHING BUILT, UNDER (R362).**')   # ### b752 Component 1: the ferry`s ACT line (:35); R7 refused the carried title
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b751's sections over b751's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.31.0: the eleven repairs of (R362)(3), among them the write list (wlist.py), the composer`s put bank (rootprompt.py put), the timeout rule (limits.py), the line`s match (linematch.py), each case failing before its repair and passing after', 'b752_standing_v1310.txt'),
                ('the eleven rules of (R362)(3)', 'b752_rules.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE LITERATURE AND SECTION 5 ((R362)(2))', [
                ('the classical theorem read from its source before the draft: Lee`s Theorem 1.1 (Voronin) and Davenport-Heilbronn as Lee states them, the certified enclosure against both', 'b752_literature.txt'),
                ('section 5 as put at [S5] and passed, spliced at PLACE-papers b07cd7d3, D1-D6 where the tree differs from the ruling', 'b752_section5.txt'),
                ('the author`s answers appended by the record tool`s route, the [S5] answer and its time before the lock', 'b752_author_answers.txt',
                 r'(?m)^### b752 -- THE AUTHOR`S ANSWERS[^\n]*'),
                ('the probe-path refusal printed before the lock gate', 'b752_pathrefusal.txt')]),
            ('THE LINE ((R362)(4))', [
                ('the INTEGRATION line from REGISTRY and SPIRAL_MAP with the match, stage SYNTHESISED, the earlier lines read again, none rewritten', 'b752_line.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b752_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b751`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument entered, a planted wrong figure per run row', 'b752_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R361)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R362)(6)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b751 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b751-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the literature bank committed before the draft, the statements and figures printed from the tree and the banks before §5 cites them, the tools` controls before their figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: §5 read where it landed -- the classical theorem named from the literature bank, the certified enclosure printed beside the numerical value, no priority claimed, nothing said of what the zero means for the schema ; no sentence saying a thing was deposited, published or versioned ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b752_address_scan.txt, data/b752_address_scan_postlock.txt, data/b752_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS (the trail), and THE_EPSTEIN_CONTROL_OBJECT_v0_1 (§5 and its dated note, one write on [S5]`s pass) ; no door or ledger row edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b752`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.31.0 by (R362)(3) ; the hook`s matcher in D:/.claude/settings.json given AskUserQuestion at Component 1 (the composer row) ; the per-act tools of b698-b751 unedited, act_current`s shared_edits empty ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R362)(4) AND (8)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s question, the act after this one (the attribution order`s plan act, confirmed or renamed), its answer in relay data/b752_author_answers.txt ;',
    '        the plan act`s opening as (R362)(4) names it, not run: I-109`s figure and the class-group signature of the negative n (relay data/b751_cq_sign.txt) ; the answers route`s dry printing counts alone, for the next corrigendum (relay data/b752_defects.txt (m)) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b752_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b751 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b752: the standing repairs are v1.31.0's ((R362)(3), relay data/b752_standing_v1310.txt, read in the corrigendum section); the
    # ### carry's diffs here (b752 carried at step zero before the fold; its tools since are the templates and tools/acts/b752.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b751 left them; port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b752's form over b752's objects: the corrigendum's foot and v1.31.0's controls; the literature bank's foot; the section bank's foot; the
    line bank's foot; the rules bank's rows; the citation check; the reproduction run; the address scan; each by its own lines through _bfig,
    which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1310.txt' % ACT, r'\*\*v1\.31\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.31.0`s controls')
    si_ = _bfig('%s_section5.txt' % ACT, r'\*\*§5: WORDS (\d+) ; LINE CITES (\d+) ; \[S5\] (PASSED|STRUCK) ; WRITTEN AT PLACE-papers ([0-9a-f]{8}), THE BODY :(\d+)-:(\d+), '
                r'THE NOTE :(\d+) ; WHERE THE RULING DIFFERS (\d+) \(D1-D\d+\) ; THE NAVIGATOR`S DEFECTS (\d+), \(h\)-\(l\)\.\*\*', 'the section bank`s foot')
    cq_ = _bfig('%s_literature.txt' % ACT, r'\*\*THE LITERATURE: QUERIES (\d+) ; SOURCES READ (\d+) \(arXiv 1204\.6297v1, sha256 ([0-9a-f]{12})\.\.\.\) ; NOT READ (\d+) ; '
                r'Z_Q0 MEETS LEE`S THEOREM 1\.1 ; THE CERTIFIED ENCLOSURE ([\d.]+) <= Re ρ <= ([\d.]+) CONTAINS Re s = 1 ; THE NAVIGATOR`S SEARCHES (\d+), RE-READ (\d+), '
                r'NO FINDING (\d+)\.\*\*', 'the literature bank`s foot')
    ln_ = _bfig('%s_line.txt' % ACT, r'\*\*THE LINE: (COMPOSED) ; FROM REGISTRY 1\.5c-21 TO 1\.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE (\S+) ; STAGE (\w+) ; '
                r'MATCHED (\d+) OF (\d+) ; THE EARLIER LINES READ AGAIN (\d+), NONE REWRITTEN ; (ALL AS READ)\.\*\*', 'the line bank`s foot')
    reps_ = [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', rdn('%s_rules.txt' % ACT))]   # ### the rules bank's rows
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b752: no order entered this act ((R362) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], rules_rows=reps_,
                repairs=len(reps_),   # ### the rules bank's rows, one per repair of (R362)(3), the version among them as (R362)(3)(xi) orders it
                s5_words=int(si_[0]), s5_cites=int(si_[1]), s5_state=si_[2], s5_pp=si_[3], s5_body=(int(si_[4]), int(si_[5])), s5_note=int(si_[6]),
                s5_differs=int(si_[7]), s5_nav=int(si_[8]),
                lit_queries=int(cq_[0]), lit_read=int(cq_[1]), lit_sha=cq_[2], lit_notread=int(cq_[3]), lit_lo=cq_[4], lit_hi=cq_[5],
                lit_nav=int(cq_[6]), lit_reread=int(cq_[7]), lit_nofind=int(cq_[8]),
                ln_keystone=ln_[1], ln_stage=ln_[2], ln_matched=int(ln_[3]), ln_of=int(ln_[4]), ln_earlier=int(ln_[5]), ln_ok=(ln_[6] == 'ALL AS READ'),
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R362)(3): the kernel rows of one kind as banked (data/b752_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R362): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
    dispatch command in the capture); every row carrying free_mb; no suite part in the background. From the command bank (the seat's commands, read live from the capture by the
    `commands` route), the dispatch rows beside the worklist's EF_RUNS, and the hook's refusal bank (a suite part sent in the background
    refused BACKGROUND)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    runs_ = sorted(set(reads_)) == sorted(str(x) for x in K.EF_RUNS)
    free_ = [r for r in _ef_kind(rows_, 'dispatch') + _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    bg_ = [l for l in rdn('%s_hook_refusals.txt' % ACT).split(NL) if '| BACKGROUND |' in l]
    bgc_ = [r['n'] for r in ((cm.get('rows') or []) if cm else []) if r.get('bg') and re.search(r'fold\.py"? checks\b|_checks\.py', r.get('cmd') or '')]
    refused_ = _ef_kind(rows_, 'dispatch_refused')
    lic_ = [r for r in _ef_kind(rows_, 'dispatch') if not str((r.get('licence') or {}).get('commit') if isinstance(r.get('licence'), dict) else r.get('licence') or '').startswith(K.STEPZERO_BANKS[:8])]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) + len(refused_) == 0 and len(_ef_kind(rows_, 'dispatch')) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 0 \
        and runs_ and not free_ and not lic_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b752_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b752_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b752's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b752_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b752_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b752_standing_v1310.txt', '## THE CONTROLS', '### ### **v1.31.0: CONTROLS '))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, §5: the literature bank committed before the draft; the statements and figures printed (the literature's K1-K3 and L1-L4) before
# ### the draft that cites them (the section bank's DRAFT BEGIN after the literature's commit)
N2_SECTIONS = ()
N2_LIT_ROWS = ('  K1  ', '  K2  ', '  K3  ', '  L1  ', '  L2  ', '  L3  ', '  L4  ')


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R362): the literature bank committed before the draft and alone of it (the section bank in a later commit); the statements and
    figures printed in the literature bank (K1-K3, L1-L4) before the draft cites them; the paper's §5 one PLACE-papers write touching the
    paper alone, after the literature's commit; each tool's controls before its figures; the standing version before the gate; the (W)
    regeneration, the pre-lock comparison and the probe-path refusal before the lock gate. Step zero, v1.31.0, the weight and corrigendum,
    the corrigendum banks, the literature, §5 in PLACE-papers, the section bank, the line bank in that order by time; v1.31.0 an ancestor
    of the line bank's commit, and that of HEAD."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_PLAN_FIRST),
              (PP, K.C2_PP[0]), (ROOT, K.C2_RELAY), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.C3_RELAY[0]], capture_output=True).returncode == 0 \
        and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C3_RELAY[0], 'HEAD'], capture_output=True).returncode == 0
    disch_ = sorted(x for x in g(PP, 'show', '--name-only', '--format=', K.C2_PP[0]).split() if x.strip()) == [K.SECTION_FILE] \
        and sorted(x for x in g(PP, 'show', '--name-only', '--format=', K.C1_PP).split() if x.strip()) == ['FINDINGS.md']
    litf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_PLAN_FIRST).split() if x.strip()]
    secf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_RELAY).split() if x.strip()]
    gen_ = 'data/b752_literature.txt' in litf_ and K.SECTION_BANK not in litf_ and K.SECTION_BANK in secf_ \
        and _first_add('data/b752_literature.txt') == g(ROOT, 'rev-parse', K.C2_PLAN_FIRST).strip()
    lit_ = rdn('%s_literature.txt' % ACT)
    cites_ = [r_.strip() for r_ in N2_LIT_ROWS if r_ not in lit_]
    sit_ = lit_
    agenda_first_ = bool(all(tm_)) and tm_[4] < tm_[5] < tm_[6]
    sect_ = gen_ and not cites_ and agenda_first_
    route_ = disch_ and sect_
    same_ = True
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the weight and corrigendum (PLACE-papers %s) FINDINGS alone and §5 (PLACE-papers %s) one write touching the paper alone: %s; the literature (relay %s) before §5 and before the section bank: %s; the literature committed alone of the section bank (relay %s), its first add: %s; the literature`s statement and figure rows missing before the draft cites them: %s; the literature`s rows K1-K3, L1-L4 all printed: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.31.0, the weight and corrigendum, the corrigendum banks, the literature, §5, the section bank and the line bank in that order by time: %s (%s), v1.31.0 an ancestor of the line bank`s commit and that of HEAD: %s; the tools` controls before their figures: %s' % (
            K.C1_PP[:8], K.C2_PP[0][:8], disch_, K.C2_PLAN_FIRST, agenda_first_, K.C2_RELAY, gen_, ', '.join(cites_) or 'none',
            not cites_, regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b752's objects; b751's in git at b751's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b752_standing_v1310.txt', ('ALL AS WANTED',)), ('b752_literature.txt', ('THE LITERATURE: QUERIES 3', 'CONTAINS Re s = 1', 'NO FINDING 1')),
             ('b752_section5.txt', ('[S5] PASSED', 'WHERE THE RULING DIFFERS 6')),
             ('b752_line.txt', ('THE LINE: COMPOSED', 'STAGE SYNTHESISED', 'ALL AS READ')),
             ('b752_corrigendum.txt', ('ITEMS',)), ('b752_citation_check.txt', ('THE CHECK HALTED',)), ('b752_reproduce.txt', ('REPRODUCES',)), ('b752_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### the entry's last line, the INTEGRATION line, in canon XXIII (A)'s form, read from REGISTRY and SPIRAL_MAP with the match of
# ### (R362)(3)(iv) through tools/b752_line.py (relay data/b752_line.txt :9): the Epstein instance, its keystone THE_EPSTEIN_CONTROL_OBJECT,
# ### SYNTHESISED, 3 of 3 FINDING names matched
INTEGRATION_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
                    'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage SYNTHESISED')
FIXED_SENTENCES = ()   # ### b752: no fixed sentence ordered by (R362)


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()


def _section_body(n):
    """the paper's section n as PLACE-papers carries it at HEAD: the lines from its heading to the next heading."""
    t = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '')
    i = t.find('\n## %d. ' % n)
    j = t.find('\n## %d.' % (n + 1), i + 1)
    return t[i + 1:j] if i >= 0 and j > i else ''


def _section_cites(bank):
    """the cites a section bank prints (tools/standing/citeprint.py's form): a head `  (n) [relay |PLACE-papers ]<path>[ at <rev>] :a[-:b]`,
    then its lines `      NNN  <text>`; returned (heads, [(where, path, rev, line, text)])."""
    sb_ = rdn(bank)
    reg_ = sb_[sb_.find('### EVERY CITE'):sb_.find('### THE CHECKS')]
    heads_, cites_, cur_ = [], [], None
    for l_ in reg_.split(NL):
        h_ = re.match(r'^  \((\d+)\) (?:(relay|PLACE-papers) )?(\S+)(?: at ([0-9A-Za-z]+))? :(\d+)(?:-:(\d+))?\s*$', l_)
        if h_:
            cur_ = (h_.group(2) or 'lean', h_.group(3), h_.group(4))
            heads_.append(h_.groups())
            continue
        p_ = re.match(r'^ {6,}(\d+)  (.*)$', l_)
        if cur_ and p_:
            cites_.append(cur_ + (p_.group(1), p_.group(2)))
    return heads_, cites_


def _cite_src(where, path, rev, n):
    """the source line a cite names, read from its tree: Lean at its revision under SIDEExplicitFormula/Schema/, the ledger in PLACE-papers at
    its revision, a relay bank from the working file."""
    if where == 'lean':
        s_ = _show(K.EF_DIR, rev, 'SIDEExplicitFormula/Schema/%s' % path) or ''
    elif where == 'PLACE-papers':
        s_ = g(PP, 'show', '%s:%s' % (rev or 'HEAD', path)) or ''
    else:
        s_ = rd(os.path.join(ROOT, *path.split('/'))) or ''
    s_ = s_.replace(chr(13), '').split(NL)
    return s_[int(n) - 1] if 0 < int(n) <= len(s_) else None
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R362): no sentence says anything was deposited, published or versioned; §5 names the classical theorem from the literature bank
    and prints the certified enclosure beside the numerical value, claiming no priority and saying nothing of what the zero means for the
    schema; the entry's INTEGRATION line its last line, reading REGISTRY 1.5c-21 and SPIRAL_MAP's Epstein row as they stand; no sentence calling the work the earliest of its kind in
    any assistant, none naming zeta, RH or h2 as moved outside a negation; the banks' nouns in the entry; the root prompt's sentences about
    the entry the composer's. From the banks' last lines, REGISTRY at PLACE-papers HEAD, the entry's sentences and the root prompt in the
    answers bank."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b752: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    # ### N3 over §5 as it landed (PLACE-papers HEAD, the paper's section 5 and the dated note :11): the classical theorem named from the
    # ### literature bank (Lee's statement of Voronin, arXiv 1204.6297, Davenport-Heilbronn as Lee states them), the certified enclosure and
    # ### the numerical value both printed; no sentence calling the box or the zero the earliest of its kind, none naming ζ, RH or h2 as moved,
    # ### none saying what the zero means for the schema
    _rl = lambda p_: (rd(os.path.join(PP, *p_.split('/'))) or '').replace(chr(13), '').split(NL)
    s5_ = _section_body(5)
    note_ = next((l_ for l_ in _rl(K.SECTION_FILE) if l_.startswith('*Dated note, 2026-11-10, b752:')), '')
    s5sents_ = [x for x in re.split(r'(?<=[.;])\s+', (s5_ + NL + note_).replace(NL, ' ')) if x.strip()]
    said_ = bool(s5_) and bool(note_) and all(w_ in s5_ for w_ in ('Voronin', 'Lee', '1204.6297', 'Davenport', '0.85326', '1.05326', '0.95326'))
    lit_ = [x for x in s5sents_ if re.search(r'\b(?:earliest|novel|priority|no one|never before|for the first time|first (?:of its kind|ever|located|formal|machine))\b', x, re.I)]
    meant_ = [x for x in s5sents_ if re.search(r'\bschema\b', x, re.I) and re.search(r'\b(?:means?|meaning|implies|suggests?|shows that|evidence)\b', x, re.I)]
    more_ = lit_ + meant_   # ### N3: §5 names no priority and says nothing of what the zero means for the schema
    nsents_ = s5sents_
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    dep_ = [x for x in nsents_ + sents if re.search(r'\b(?:deposited|published|versioned)\b', x) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(r'\b(?:RH|GRH|h2|ζ)\b.*\b(?:holds|fails|proved|refuted|moved)\b', x) and not re.search(neg_, x)]
    lines_ = [l for l in text.split(NL) if l.strip()]
    rg_ = _rl('REGISTRY.md')
    sm_ = rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''
    integ_ = bool(lines_) and lines_[-1].strip() == INTEGRATION_LINE \
        and any(l.startswith('| 1.5c-21 |') for l in rg_) and '| **The Epstein instance** (seated 2026-11-09, b751) |' in sm_ and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in sm_
    fixed_ = []
    nouns_ = [w_ for w_ in ('THE_EPSTEIN_CONTROL_OBJECT', 'Voronin', 'Davenport', 'Lee', '1204.6297', '0.85326', '1.05326', '[S5]',
                            'data/%s_literature.txt' % ACT, 'data/%s_section5.txt' % ACT, 'data/%s_line.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and said_ and not more_ and not dep_ and not first_ and not loc_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; §5 read where it landed -- the paper`s section 5 and its dated note naming Voronin, Lee`s arXiv 1204.6297 and Davenport-Heilbronn and printing the enclosure 0.85326-1.05326 beside the value 0.95326: %s; a sentence of §5 or its note claiming priority or saying what the zero means for the schema: %s; a sentence of those writes or the entry saying a thing was deposited, published or versioned outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY 1.5c-21 and SPIRAL_MAP`s Epstein row read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), said_, more_ or 'NONE', dep_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R362) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R362)(5))
# ### (R362)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R362)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
    # ### same reader the ceiling takes; the face's `locked at (UTC)` line no longer dates it
    import lockdate as LD
    lc = LD.lock_of(ACT, os.path.join(ROOT, 'data'))
    lock = LD.lock_epoch(lc, ROOT) if lc else None
    # ### v1.30.0, (R362)(3)(viii), b751 events (12): the lock's time printed from the one reader's epoch; b751's module left lock_iso unset and
    # ### its N4 sentence printed "the lock at NOT LOCKED" at every reading while lock_ok held
    out = dict(lock=lock, lock_iso=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)) if lock else None, lock_commit=lc, after=[], edited=[], dirty=[])
    if lc is None or lock is None:
        return out
    rows = [l.split(' ', 1) for l in g(ROOT, 'log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.PRE_RELAY).split(NL) if l.strip()]
    face_rel = os.path.relpath(FACE, ROOT).replace(os.sep, '/')
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
    # ### (R362) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b751's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b752, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b751's face
# ### read them; (R362)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
# ### 14ca572, main unmoved, the tags containing v0.37 exactly v0.37 and v0.38, v0.38 peeling to 14ca5725
#⟪OVERRIDE record MARK 82a559f5c96c 2⟫
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    tag_one = _ef_now[0] == _ef_prev[0] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **{'v0.38': '14ca572'})
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main == K.EF_MAIN and sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) == ['v0.37', 'v0.38'] \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') and ch_ok \
        and bool(prev) and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R362)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R362)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b751 left them; the address scan's count from its bank (relay data/b752_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R362)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R362)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R362)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    # ### v1.30.0, (R362)(3)(vi), b751 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R362)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and not zdel_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b752_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b752 Component 1, (R362)(7)(vi): R7 refused the carried head (b751's ordinal and its §5 figures); the ruling's ordinal and title, the
    # ### act's own figures added by Component 4 when its banks stand
    return ('### b752 — lane two, act one hundred and seventy-nine, the attribution plan under (R362): b751 at its weight and its corrigendum; '
            'v1.32.0; the cross-reference, the class-group signature of the negative n and the kernel`s classes read as statements; the plan put as [P1]; nothing built')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects in the ferry's C4 form ("THE_EPSTEIN_CONTROL_OBJECT §5 <passed | struck>, <w> words, <c> cites, the
    located zero an instance of Voronin's theorem by the banked search; the part-order guard, the (W) refusal, the composer on every prompt,
    the line reader's match and <r> repairs landed"), adjusted to what the act did: the instance read at the zero's numerical value, the
    certified enclosure printed and deciding neither side of Re s = 1 (relay data/b752_literature.txt L1-L4, [S5]'s D1); every figure from
    the banks (the section bank's foot, the literature bank's foot, the rules bank's rows)."""
#⟪END⟫
#⟪SECTION record 31⟫
    ctl_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if not all(c_ in ctl_ for c_ in ('order', 'wlist', 'composer', 'linematch', 'version')):
        sys.exit('### v1.31.0`S CONTROLS DO NOT NAME (order), (wlist), (composer), (linematch) AND (version) -- NOTHING COMPOSED')
    if f['rules_rows'] != list(range(1, len(f['rules_rows']) + 1)) or len(f['rules_rows']) < 3:
        sys.exit('### THE RULES BANK`S ROWS ARE NOT (1)-(n) IN ORDER -- NOTHING COMPOSED')
    if not f['ln_ok'] or f['ln_matched'] != f['ln_of'] or f['s5_state'] not in ('PASSED', 'STRUCK') or f['lit_read'] < 1:
        sys.exit('### THE LINE BANK, THE SECTION BANK OR THE LITERATURE BANK NOT AS READ -- NOTHING COMPOSED')
    return ('## THE_EPSTEIN_CONTROL_OBJECT §5 %s, %d words, %d cites; the located zero an instance of Voronin’s theorem by the banked search at '
            'its numerical value, its certified enclosure %s ≤ Re ρ ≤ %s holding Re s = 1 and deciding neither side; the part-order guard, the '
            '(W) refusal, the composer on every prompt, the line reader’s match and %d repairs landed' % (
                f['s5_state'].lower(), f['s5_words'], f['s5_cites'], f['lit_lo'], f['lit_hi'], f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the eleven rules of relay data/b752_rules.txt, the seat`s reading of (R362)(3), each for the author`s strike; (2) the located zero read as an instance of Voronin`s theorem and not of Davenport-Heilbronn`s at its numerical value alone, the certified enclosure 0.85326 <= Re ρ <= 1.05326 holding Re s = 1, as §5 states both and the author passed at [S5] (relay data/b752_literature.txt L1-L4, data/b752_section5.txt D1); (3) the answers route`s dry printing its counts alone where its docstring says it prints what would be appended, carried for the next corrigendum (relay data/b752_defects.txt (m)); '
            +
            '(4) %s and the seat’s %s defect%s as lettered' % (
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b752: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R362)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b752's objects; b751's composer in git at
    b751's record tool). Its last line the INTEGRATION line ((R362)(4))."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    if f['s5_state'] not in ('PASSED', 'STRUCK'):
        sys.exit('### THE SECTION BANK`S STATE READS NEITHER PASSED NOR STRUCK -- NOTHING COMPOSED')
    rep, tot = _repeats()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R362)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R361)(2)(v)
    pl_ = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '').split(NL)
    h5_ = [i_ + 1 for i_, l_ in enumerate(pl_) if l_.startswith('## 5. ')]
    dn_ = [i_ + 1 for i_, l_ in enumerate(pl_) if l_.startswith('*Dated note, 2026-11-10, b752:')]
    if len(h5_) != 1 or len(dn_) != 1:
        sys.exit('### THE LINES THE ENTRY CITES DO NOT READ AS EXPECTED (§5`s heading %s, the dated note %s) -- NOTHING COMPOSED' % (h5_, dn_))
    e = ['', _title(), '',
         '§5 of THE_EPSTEIN_CONTROL_OBJECT_v0_1, the located zero, was put to the author once as [S5] and %s: %d words and %d line cites under its heading (:%d), body :%d-:%d, the dated note at :%d, one PLACE-papers write (%s), the version v0.1 kept (relay data/b752_section5.txt). It names the classical theorem from the literature bank and not from recall: Voronin’s theorem as Lee states it (arXiv 1204.6297v1, Theorem 1.1, read in full, sha256 %s...), whose hypotheses Z_Q0 meets (discriminant −23, class number 3), and Davenport-Heilbronn’s, which concerns Re s > 1, as Lee states it; the zero’s numerical real part 0.95326 lies in Voronin’s strip and outside Davenport-Heilbronn’s half-plane, and its certified enclosure %s ≤ Re ρ ≤ %s holds Re s = 1, so the Lean statement decides neither and proves only Re ρ ≠ 1/2 (relay data/b752_literature.txt L1-L4).' % (
             f['s5_state'].lower(), f['s5_words'], f['s5_cites'], h5_[0], f['s5_body'][0], f['s5_body'][1], dn_[0], f['s5_pp'], f['lit_sha'], f['lit_lo'], f['lit_hi']), '',
         '*Filed at b752 on the author’s ruling `(R362)`; %d question%s put before the root. Banks: relay '
         '`data/b752_corrigendum.txt`, `data/b752_standing_v1310.txt`, `data/b752_rules.txt`, `data/b752_literature.txt`, `data/b752_section5.txt`, `data/b752_put_1.json`, `data/b752_author_answers.txt`, `data/b752_line.txt`, `data/b752_prelock.txt`, `data/b752_pathrefusal.txt`, '
         '`data/b752_reproduce.txt`, `data/b752_address_scan.txt`, `data/b752_touch.txt`, `data/b752_standing_figures.txt`, `data/b752_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R362)(1), (3); %s, %s, %s): b751 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b751’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b752_corrigendum.txt); tools/standing/ at %s by a commit of its own, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b752_standing_v1310.txt): the part-order guard, the (W) refusal in the hook over the write list, the composer on every prompt with its put bank, the line reader’s match, the scan at the gate, the rendered modules compiled by the dry, the carry printing every row, the tool’s words and phases, the host’s limit, the refusals printed, the version; the rules, %d rows, in relay data/b752_rules.txt.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], len(f['rules_rows'])), '',
         '**The literature and §5** ((R362)(2), N2, N3): the literature bank committed at relay %s before the draft: %d queries sent, %d source read from its PDF (Lee, arXiv 1204.6297v1), %d not read (Voronin 1976 and Davenport-Heilbronn 1936, each cited only as Lee states it; the search’s other results, nothing taken from them), the kernel’s form read against Lee’s hypotheses, the certified enclosure read against both theorems; the navigator’s searches %d, re-read %d, entered with no finding %d (the search for a located zero of ζ in a proof assistant, entered as a search with no finding, its claim kept out). The draft banked and put once as [S5] in b736’s form, the author’s answer “%s” banked verbatim with its time by the appending route before the lock (relay data/b752_author_answers.txt); the paper written at PLACE-papers %s, the section bank at relay %s; where the tree or the banks differ from the ruling’s words, %d rows (D1-D6), and the ruling’s (v) and its figures in D2-D5 entered as the navigator’s defects, %d, CLAIM, NEW (relay data/b752_defects.txt (h)-(l)).' % (
             K.C2_PLAN_FIRST, f['lit_queries'], f['lit_read'], f['lit_notread'], f['lit_nav'], f['lit_reread'], f['lit_nofind'],
             'Pass [S5]' if f['s5_state'] == 'PASSED' else 'Strike [S5]', K.C2_PP[0], K.C2_RELAY, f['s5_differs'], f['s5_nav']), '',
         '**The integration line** ((R362)(4)): this entry’s line read by tools/b752_line.py from REGISTRY and SPIRAL_MAP with the match of (R362)(3)(iv): the cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23), the keystone %s, stage %s, %d of %d FINDING names matched (relay data/b752_line.txt); the earlier entries’ lines read again, %d of them, none rewritten.' % (
             f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '',
         '**The order of the act** (N2): %s at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the literature at relay %s; §5 at PLACE-papers %s; the section bank at relay %s; the line bank and the answers pair at relay %s; the per-commit scan to its own bank at every commit; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b752_prelock.txt, data/b752_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             f['ver'], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST, K.C2_PP[0], K.C2_RELAY, K.C3_RELAY[0][:8]), '',
         '**What this act is not**: nothing deposits; no new version; no draft published; no Zenodo call; no kernel’s main touched, no branch merged, no tag beyond v0.38, no Lean file written; no door or ledger row edited; the paper’s §5 the one PLACE-papers write on a passed item, with the ledger entries.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b752_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b752_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b752_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b752 -- %s, %s, %s, %s -- against b751’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b752_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the literature and §5 read one way: the bank read the source before the draft cited it, and the source’s own statement set the limit of what §5 says -- the zero instances Voronin’s theorem at its numerical value, and the certificate, whose enclosure holds Re s = 1, carries Re ρ ≠ 1/2 and no more.', '',
         '**Carried to:** %s, per (R362): the root’s question, the act after this one, put once and answered in relay data/b752_author_answers.txt; the eleven rules for the author’s strike; the answers route’s dry printing counts alone (defect (m)) for the next corrigendum; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b751():
    """b751's form over b751's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b752's objects; b751's composer in git at b751's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the literature and §5; the line."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R362)(3)(vii): the composed prompts' rows, the sitting rows read apart
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R362) ratified.** Its components as the ferry orders them (relay data/b752_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b751’s weight), :%s (the corrigendum), :%s (the entry); §5 of THE_EPSTEIN_CONTROL_OBJECT_v0_1 and its dated note, one PLACE-papers write (%s); no order entered; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.C2_PP[0]), '',
             '**The literature and §5:** the literature bank at relay %s before the draft, %d source read, %d not read; [S5] %s, %d words, %d line cites, D1-D%d where the ruling differs, the navigator’s defects %d; the section bank at relay %s (relay data/b752_literature.txt, data/b752_section5.txt, data/b752_author_answers.txt).' % (
                 K.C2_PLAN_FIRST, f['lit_read'], f['lit_notread'], f['s5_state'].lower(), f['s5_words'], f['s5_cites'], f['s5_differs'], f['s5_nav'], K.C2_RELAY), '',
             '**The integration line:** b752’s at the foot of its entry, cluster the Epstein instance, keystone %s, stage %s, %d of %d matched (relay data/b752_line.txt); the earlier lines read again %d, none rewritten.' % (
                 f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**A candidate order beside W-ORD-ZQ-FAMILY, named and not entered:** the tighter box, half-side under 0.046 about the same centre, certifying Re ρ < 1; no entry written (the author’s word, 2026-11-10T16:29:22Z).', '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b752_standing_v1310.txt); the answers route`s dry printing counts alone (defect (m)) for the next corrigendum.' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b752_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b752_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b752_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b752 `%s` (previous `%s`, b751’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b752_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b752_standing_v1310.txt); the standing '
             'report tool (relay data/b752_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b751 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b752_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b751’s %s, %s, %s, %s (relay data/b752_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b752_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b751():
    """b751's trail record over b751's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b751 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none; no kernel`s main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b751-closing, push-b751-preroot, push-b751-record; PLACE-papers push-b751-preroot, push-b751-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b752_stepzero.txt :44-:48).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written this act ((R362)(6)).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R362)(3): FINDINGS :14669.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R362)(3): row (71).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R362)(6)).'),
    ('sitting items decided', 1, 1, 'items', '### (R362)(2): [S5], passed (relay data/b752_section5.txt, data/b752_author_answers.txt).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R362) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b752_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.31.0`s controls, the literature, the line, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none this act: no registered object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R362)(6)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R362)(3): tools/standing/ to v1.31.0, each repair with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended; data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part and computation; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b752_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, the gh reads and the gh description writes under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b752: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b752_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b752_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1310', 'literature', 'line', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b752_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b752_registration_%s.txt -- b752, THE LOCATED ZERO: b751 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.31.0; "
                             "THE LITERATURE; §5 OF THE_EPSTEIN_CONTROL_OBJECT AT [S5]; THE INTEGRATION LINE; NO DEPOSIT, NO LEAN, UNDER (R362)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b751's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b752: b751's lines read banks this
act does not write, and are not carried; the lines are b752's: tools/standing/ v1.31.0 by its controls (CERTIFIED), the literature, §5 and
the INTEGRATION line by their banks (REGISTERED), and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b752's lines, each from the record tool's figures over b752's banks
    # ------------------------------------------------------------------ REGISTERED: (R362)(2), §5, read from its section bank
    sz = seat('%s_section5.txt' % ACT, '**§5: WORDS ')
    sk = sz   # ### (R361)(2)(ii): the name the template appends
    keys['SECTION5'] = ('REGISTERED -- §5 OF THE_EPSTEIN_CONTROL_OBJECT: [S5] %s, %d words, %d line cites, written at PLACE-papers %s (body :%d-:%d, the note :%d); where the ruling differs %d (D1-D6); the navigator`s defects %d. SOURCE %s.' % (
        f['s5_state'], f['s5_words'], f['s5_cites'], f['s5_pp'], f['s5_body'][0], f['s5_body'][1], f['s5_note'], f['s5_differs'], f['s5_nav'], sz['text']))
    snz = seat('%s_literature.txt' % ACT, '**THE LITERATURE: QUERIES ')
    keys['LIT'] = ('REGISTERED -- THE LITERATURE: %d queries; %d source read (arXiv 1204.6297v1, sha256 %s...), %d not read; Z_Q0 meets Lee`s Theorem 1.1 (Voronin); the certified enclosure %s <= Re ρ <= %s holds Re s = 1; the navigator`s searches %d, re-read %d, no finding %d; at relay %s before the draft. SOURCE %s.' % (
        f['lit_queries'], f['lit_read'], f['lit_sha'], f['lit_notread'], f['lit_lo'], f['lit_hi'], f['lit_nav'], f['lit_reread'], f['lit_nofind'], K.C2_PLAN_FIRST, snz['text']))
    seats.append(snz)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.31.0 ((R362)(3)), by its controls
    sw = seat('%s_standing_v1310.txt' % ACT, '**v1.31.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1310'] = ('CERTIFIED -- tools/standing/ v1.31.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the INTEGRATION line ((R362)(4))
    so = seat('%s_line.txt' % ACT, '**THE LINE: ')
    keys['LINE'] = ('REGISTERED -- THE INTEGRATION LINE from REGISTRY and SPIRAL_MAP with the match: cluster the Epstein instance, keystone %s, stage %s, %d of %d matched; the earlier lines read again %d, none rewritten. SOURCE %s.' % (
        f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R362)(6))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1310']), ('REGISTERED', ['LIT', 'SECTION5', 'LINE']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b752 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
